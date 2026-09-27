#!/usr/bin/env python3
"""
B16 – Fliesen und Parkett als echte 3D-Einzelobjekte: Verlegemuster auf
mehrfachem Gefälle, Verschnitt, Reststück-Wiederverwendung, Rasterursprung.

Eingabe:  daten/b16_fliesen_verlegung.json (Raum, Gefälle, Fliesen, Muster)
Ausgabe:  ausgabe/b16_ergebnis.json          (Kennzahlen aller Fälle)
          ausgabe/b16_<fall>.svg             (Draufsicht der besten Lage)
          ausgabe/b16_stuecke_<fall>.json    (3D-Polygone je Stück, Referenzfall)
          ausgabe/b16_<fall>_einzeln.ifc     (optional --ifc: IfcCovering je Stück)
          ausgabe/b16_<fall>_aggregiert.ifc  (optional --ifc: ein IfcCovering,
                                              IfcMappedItem für ganze Fliesen)

ALLE Zahlen im JSON sind BEISPIELWERTE. Normbezug und Quellen: Recherche 17.

Rechenweg (siehe Recherche 17, Abschnitt 4):

  1. Raum: regelmäßiges Achteck (Innenkreis d), Wandfuge nach innen.
  2. Gefälle: stückweise ebene Flächen z = a·x + b·y + c.
     Punktablauf: 8 Dreiecke Mitte→Wand, Knicklinien Mitte→Ecke (Kehlen).
     Zwei Rinnen: zwei geneigte Flächen, Grat in der Mitte, ebene Rinnenzonen.
     Knicklinien sind Fugen: Fliesen werden dort geschnitten (Grat-/Kehlschnitt),
     denn eine starre Fliese kann nicht über zwei Ebenen liegen.
  3. Muster als periodische Kachelung: Motiv (1–2 Rohlinge) + Gittervektoren
     t1, t2. Gerade/Verband, Fischgrät (2 Stäbe je Zelle), Chevron (L/R-Stab,
     Sollform Parallelogramm; aus Rechteck-Rohling mit 2 Gehrungsschnitten
     oder als Formteil).
  4. Clipping: Sollform ∩ Verlegefläche je Gefällefläche (shapely). Jede
     Schnittkante wird nach Lage klassifiziert: Wand (gerade/schräg zur
     Fliesenkante), Knicklinie (Gratschnitt), Ablauf, Gehrung (Formschnitt).
  5. Bedarf: (a) je Rasterposition ein Rohling, (b) Greedy-Reststückverwertung:
     Stücke absteigend nach Fläche; ein Stück darf aus einem Reststück kommen,
     wenn es nach einer Symmetrie des Rohlings (0°/180°, bei Quadrat auch
     90°/270°, keine Spiegelung) im Reststück liegt UND seine Fabrikkanten
     wieder auf Fabrikkanten fallen (Schnittkante nie in die Fläche drehen).
  6. Rasterursprung: Grid-Search über u, v ∈ {0, 1/n, …} der Gittervektoren,
     Ziel = Materialkosten + Schnittzeit·Lohn + Malus für Kleinstücke.
  7. 3D: jede Stückkontur senkrecht auf ihre Gefälleebene gehoben
     (Längenfehler ≤ 1 − cos(arctan 0,015) ≈ 0,011 %).

Aufruf:   python b16_fliesen_verlegung.py [--ifc] [--schritte 6]
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import shapely
from shapely import affinity
from shapely.geometry import LineString, MultiPolygon, Point, Polygon, box
from shapely.ops import unary_union
from shapely.prepared import prep

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b16_fliesen_verlegung.json"
AUSGABE = HIER / "ausgabe"

# Fester Namensraum für uuid5 (einmalig erzeugt und fixiert).
GUID_NAMENSRAUM = uuid.UUID("5d1f7a90-3c2e-5b4a-9e61-b16f11e5e001")

EPS = 1e-6          # mm, Geometrie-Toleranz
TOL_LINIE = 0.05    # mm, Kante liegt auf einer Bezugslinie
SCHNITTARTEN = ("gerade", "schraeg", "gehrung", "gratschnitt", "ablauf", "sonstig")
# Rangfolge für die Stück-Kategorie (aufwendigster Schnitt bestimmt die Kategorie)
RANG = {"gratschnitt": 5, "ablauf": 4, "schraeg": 3, "gehrung": 2, "gerade": 1, "sonstig": 0}


# ---------------------------------------------------------------------------
# 0. Affine Hilfen (3×3-Matrizen, homogen)
# ---------------------------------------------------------------------------

def m_rot(grad: float) -> np.ndarray:
    w = math.radians(grad)
    c, s = math.cos(w), math.sin(w)
    return np.array([[c, -s, 0.0], [s, c, 0.0], [0.0, 0.0, 1.0]])


def m_trans(dx: float, dy: float) -> np.ndarray:
    return np.array([[1.0, 0.0, dx], [0.0, 1.0, dy], [0.0, 0.0, 1.0]])


def m_mul(*ms: np.ndarray) -> np.ndarray:
    out = np.eye(3)
    for m in ms:
        out = out @ m
    return out


def anwenden(geom, m: np.ndarray):
    """shapely-Geometrie mit 3×3-Matrix transformieren."""
    return affinity.affine_transform(geom, [m[0, 0], m[0, 1], m[1, 0], m[1, 1], m[0, 2], m[1, 2]])


def polygone(geom) -> list[Polygon]:
    """Alle Polygon-Teile einer Geometrie (deterministische Reihenfolge)."""
    if geom.is_empty:
        return []
    if isinstance(geom, Polygon):
        return [geom]
    teile = [p for teil in getattr(geom, "geoms", []) for p in polygone(teil)]
    return sorted(teile, key=lambda p: (round(p.centroid.x, 3), round(p.centroid.y, 3), round(p.area, 3)))


def inkreis_durchmesser(p: Polygon) -> float:
    """Durchmesser des größten einbeschriebenen Kreises (Maß für 'Breite')."""
    if p.is_empty or p.area <= 0:
        return 0.0
    return 2.0 * shapely.maximum_inscribed_circle(p, 0.5).length


# ---------------------------------------------------------------------------
# 1. Raum und Gefälle
# ---------------------------------------------------------------------------

def achteck(innenradius: float) -> Polygon:
    """Regelmäßiges Achteck, Seiten senkrecht zu x/y (Ecken bei 22,5° + k·45°)."""
    r_um = innenradius / math.cos(math.radians(22.5))
    return Polygon([(r_um * math.cos(math.radians(22.5 + 45 * k)),
                     r_um * math.sin(math.radians(22.5 + 45 * k))) for k in range(8)])


@dataclass
class Facette:
    name: str
    poly: Polygon                       # Draufsicht
    ebene: tuple[float, float, float]   # z = a·x + b·y + c (mm)

    def z(self, x: float, y: float) -> float:
        a, b, c = self.ebene
        return a * x + b * y + c


@dataclass
class Knicklinie:
    linie: LineString
    art: str      # "kehle" oder "grat"


@dataclass
class Raum:
    raum: Polygon
    facetten: list[Facette]
    knicke: list[Knicklinie]
    ablauf: Polygon | None
    verlegeflaechen: list[Polygon]      # je Facette, nach Fugen-Abzug
    wand_rand: object                   # Linienzug der Belagsgrenze an der Wand
    knick_rand: object                  # Ränder der Knickfugen
    ablauf_rand: object                 # Rand der Ablauf-/Rinnenfuge
    entwaesserung: str
    fuge: float
    _puffer: dict = field(default_factory=dict)

    def puffer(self, name: str):
        """Vorbereitete Toleranzpuffer der Bezugslinien (einmal je Raum)."""
        if name not in self._puffer:
            linie = getattr(self, name)
            self._puffer[name] = None if linie.is_empty else prep(linie.buffer(TOL_LINIE))
        return self._puffer[name]

    @property
    def flaeche(self) -> float:
        return self.raum.area


def knickart(f1: Facette, f2: Facette, linie: LineString) -> str:
    """Kehle, wenn die Knicklinie tiefer liegt als die Nachbarflächen beiderseits."""
    m = linie.interpolate(0.5, normalized=True)
    (x0, y0), (x1, y1) = linie.coords[0], linie.coords[-1]
    n = math.hypot(x1 - x0, y1 - y0)
    nx, ny = -(y1 - y0) / n * 10, (x1 - x0) / n * 10
    seiten = []
    for px, py in ((m.x + nx, m.y + ny), (m.x - nx, m.y - ny)):
        f = f1 if f1.poly.buffer(EPS).contains(Point(px, py)) else f2
        seiten.append(f.z(px, py))
    return "kehle" if f1.z(m.x, m.y) < 0.5 * sum(seiten) else "grat"


def baue_raum(daten: dict, entwaesserung: str) -> Raum:
    r_i = daten["raum"]["innenkreis_durchmesser_mm"] / 2.0
    s = daten["gefaelle_prozent"] / 100.0
    fuge = float(daten["fuge_mm"])
    randfuge = float(daten["raum"]["randfuge_mm"])
    raum = achteck(r_i)
    ecken = list(raum.exterior.coords)[:-1]
    facetten: list[Facette] = []
    ablauf = None
    anschluss = 0.0

    if entwaesserung == "eben":
        facetten = [Facette("eben", raum, (0.0, 0.0, 0.0))]
    elif entwaesserung == "punkt":
        ed = daten["entwaesserungen"]["punkt"]
        for k in range(8):
            wn = math.radians(45 * k)               # Außennormale der Seite k
            nx, ny = math.cos(wn), math.sin(wn)
            v0, v1 = ecken[(k - 1) % 8], ecken[k]   # Seite k liegt zwischen Ecke k-1 und k
            facetten.append(Facette(f"F{k}", Polygon([(0, 0), v0, v1]), (s * nx, s * ny, 0.0)))
        h = ed["rost_mm"] / 2.0
        ablauf = box(-h, -h, h, h)
        anschluss = float(ed["anschlussfuge_mm"])
    elif entwaesserung == "zwei_rinnen":
        ed = daten["entwaesserungen"]["zwei_rinnen"]
        b = float(ed["rinne_breite_mm"])
        xr = r_i - b                                # Innenkante Rinne
        gross = box(-2 * r_i, -2 * r_i, 2 * r_i, 2 * r_i)
        teile = {
            "West_Rinnenzone": (box(-2 * r_i, -2 * r_i, -xr, 2 * r_i), (0.0, 0.0, 0.0)),
            "West": (box(-xr, -2 * r_i, 0.0, 2 * r_i), (s, 0.0, s * xr)),        # z = s·(xr + x)
            "Ost": (box(0.0, -2 * r_i, xr, 2 * r_i), (-s, 0.0, s * xr)),         # z = s·(xr − x)
            "Ost_Rinnenzone": (box(xr, -2 * r_i, 2 * r_i, 2 * r_i), (0.0, 0.0, 0.0)),
        }
        for name, (bx, eb) in teile.items():
            p = raum.intersection(bx.intersection(gross))
            facetten.append(Facette(name, p, eb))
        # Rinnen: Rechteck an der Wand, auf Wandlänge gekürzt
        seite = 2 * r_i * math.tan(math.radians(22.5))
        ablauf = unary_union([box(xr, -seite / 2, r_i, seite / 2), box(-r_i, -seite / 2, -xr, seite / 2)])
        anschluss = float(ed["anschlussfuge_mm"])
    else:
        raise ValueError(f"unbekannte Entwässerung: {entwaesserung}")

    # Knicklinien = gemeinsame Kanten benachbarter Facetten mit verschiedener Ebene
    knicke: list[Knicklinie] = []
    for i in range(len(facetten)):
        for j in range(i + 1, len(facetten)):
            fi, fj = facetten[i], facetten[j]
            if np.allclose(fi.ebene, fj.ebene):
                continue
            g = fi.poly.intersection(fj.poly)
            for teil in ([g] if isinstance(g, LineString) else list(getattr(g, "geoms", []))):
                if isinstance(teil, LineString) and teil.length > 1.0:
                    knicke.append(Knicklinie(teil, knickart(fi, fj, teil)))

    innen = raum.buffer(-randfuge, join_style="mitre")
    knick_puffer = unary_union([k.linie.buffer(fuge / 2, cap_style="flat", join_style="mitre") for k in knicke]) \
        if knicke else Polygon()
    ablauf_puffer = ablauf.buffer(anschluss, join_style="mitre") if ablauf is not None else Polygon()
    verlege = []
    for f in facetten:
        v = f.poly.intersection(innen).difference(knick_puffer).difference(ablauf_puffer)
        verlege.append(v)
    return Raum(
        raum=raum, facetten=facetten, knicke=knicke, ablauf=ablauf, verlegeflaechen=verlege,
        wand_rand=innen.exterior,
        knick_rand=knick_puffer.boundary if not knick_puffer.is_empty else LineString(),
        ablauf_rand=ablauf_puffer.boundary if not ablauf_puffer.is_empty else LineString(),
        entwaesserung=entwaesserung, fuge=fuge,
    )


# ---------------------------------------------------------------------------
# 2. Muster als periodische Kachelung
# ---------------------------------------------------------------------------

@dataclass
class Motiv:
    name: str                 # H/V (Fischgrät), R/L (Chevron), Q (gerade)
    artikel: str              # Bestell-Artikel (bei Formteil L/R getrennt)
    rohling: Polygon          # Rohling im Rohling-Koordinatensystem
    soll: Polygon             # Sollform im Rohling-Koordinatensystem
    m: np.ndarray             # Rohling-lokal → Musterkoordinaten


@dataclass
class Muster:
    name: str
    typ: str
    fliese: str
    motive: list[Motiv]
    t1: np.ndarray
    t2: np.ndarray


def muster_bauen(name: str, spec: dict, fliesen: dict, fuge: float) -> Muster:
    fl = fliesen[spec["fliese"]]
    L, W, f = float(fl["laenge_mm"]), float(fl["breite_mm"]), fuge
    rechteck = box(0, 0, L, W)
    typ = spec["typ"]
    if typ == "gerade":
        a, b = L + f, W + f
        mot = [Motiv("Q", spec["fliese"], rechteck, rechteck, np.eye(3))]
        return Muster(name, typ, spec["fliese"], mot, np.array([a, 0.0]),
                      np.array([spec.get("versatz_anteil", 0.0) * a, b]))
    if typ == "fischgraet":
        # Treppen-Fischgrät, achsparallel aufgebaut, danach um 45° gedreht
        # (Zopfachse = y). Zelle: liegender Stab H und stehender Stab V.
        a, b = L + f, W + f
        m_h = np.eye(3)
        m_v = m_mul(m_trans(a + W, b - a), m_rot(90))   # Rechteck [0,L]x[0,W] → [a,a+W]x[b-a,b-a+L]
        rg = m_rot(45)
        mot = [Motiv("H", spec["fliese"], rechteck, rechteck, m_mul(rg, m_h)),
               Motiv("V", spec["fliese"], rechteck, rechteck, m_mul(rg, m_v))]
        t1 = (rg @ np.array([b, b, 0.0]))[:2]
        t2 = (rg @ np.array([a, -a, 0.0]))[:2]
        return Muster(name, typ, spec["fliese"], mot, t1, t2)
    if typ == "chevron":
        phi = math.radians(spec.get("gehrungswinkel_grad", 45))
        off = W / math.tan(phi)                        # Versatz der Gehrung längs des Stabs
        beta = 90.0 - spec.get("gehrungswinkel_grad", 45)   # Stabneigung zur Waagerechten
        cb, sb = math.cos(math.radians(beta)), math.sin(math.radians(beta))
        soll_r = Polygon([(0, 0), (L - off, 0), (L, W), (off, W)])     # Gehrung parallel zur Zopfachse
        soll_l = Polygon([(0, W), (L - off, W), (L, 0), (off, 0)])     # gespiegelte Sollform im selben Rechteck
        spalte = (L - off) * cb                                         # Spaltenbreite in x
        h = (W + f) / math.cos(math.radians(beta))                      # Stapelabstand in y
        m_r = m_rot(beta)
        # L-Stab: um −beta drehen, dann so schieben, dass er Spiegelbild von R an x = spalte + f/2 ist
        m_l0 = m_rot(-beta)
        p_l = anwenden(soll_l, m_l0)
        p_r = anwenden(soll_r, m_r)
        ziel = affinity.scale(p_r, xfact=-1, yfact=1, origin=(spalte + f / 2, 0))
        dx = ziel.bounds[0] - p_l.bounds[0]
        dy = ziel.bounds[1] - p_l.bounds[1]
        m_l = m_mul(m_trans(dx, dy), m_l0)
        if spec.get("rohling", "rechteck") == "rechteck":
            mot = [Motiv("R", spec["fliese"], rechteck, soll_r, m_r),
                   Motiv("L", spec["fliese"], rechteck, soll_l, m_l)]
        else:   # Formteil: Rohling = Sollform, L und R sind getrennte Artikel
            mot = [Motiv("R", spec["fliese"] + "_R", soll_r, soll_r, m_r),
                   Motiv("L", spec["fliese"] + "_L", soll_l, soll_l, m_l)]
        return Muster(name, typ, spec["fliese"], mot, np.array([0.0, h]), np.array([2 * (spalte + f), 0.0]))
    raise ValueError(f"unbekannter Mustertyp: {typ}")


# ---------------------------------------------------------------------------
# 3. Verlegen: Clipping und Schnittklassifikation
# ---------------------------------------------------------------------------

@dataclass
class Stueck:
    rohling_id: str
    motiv: str
    artikel: str
    facette: int
    poly: Polygon                   # Draufsicht, global
    lokal: Polygon                  # im Rohling-Koordinatensystem
    m_global: np.ndarray            # Rohling-lokal → global
    ganz: bool                      # Rohling unverändert (kein Schnitt)
    soll_ganz: bool                 # Sollform unverändert (nur Formschnitte)
    breite: float                   # Inkreisdurchmesser (mm)
    schnitte: list[tuple[str, float]] = field(default_factory=list)   # (Art, Länge mm)

    @property
    def kategorie(self) -> str:
        if self.ganz:
            return "ganz"
        if not self.schnitte:
            return "ganz"
        return max((a for a, _ in self.schnitte), key=lambda a: RANG[a])


def _kanten(p: Polygon):
    """Kanten eines Polygons nach Zusammenfassen kollinearer Punkte."""
    q = p.simplify(0.01, preserve_topology=True)
    for ring in [q.exterior, *q.interiors]:
        cs = list(ring.coords)
        for i in range(len(cs) - 1):
            yield LineString([cs[i], cs[i + 1]])


def _auf(seg: LineString, puffer) -> bool:
    return puffer is not None and puffer.contains(seg)


def klassifiziere_schnitte(teil: Polygon, rohling_g: Polygon, soll_g: Polygon, raum: Raum,
                           achswinkel: float) -> list[tuple[str, float]]:
    """Jede Kante, die nicht auf der Rohling-Kante (Fabrikkante) liegt, ist ein Schnitt."""
    out = []
    rand_roh = prep(rohling_g.exterior.buffer(TOL_LINIE))
    rand_soll = prep(soll_g.exterior.buffer(TOL_LINIE))
    for seg in _kanten(teil):
        if seg.length < 0.05 or _auf(seg, rand_roh):
            continue
        if _auf(seg, raum.puffer("knick_rand")):
            art = "gratschnitt"
        elif _auf(seg, raum.puffer("ablauf_rand")):
            art = "ablauf"
        elif _auf(seg, raum.puffer("wand_rand")):
            (x0, y0), (x1, y1) = seg.coords
            w = (math.degrees(math.atan2(y1 - y0, x1 - x0)) - achswinkel) % 90.0
            art = "gerade" if min(w, 90.0 - w) < 0.5 else "schraeg"
        elif _auf(seg, rand_soll):
            art = "gehrung"
        else:
            art = "sonstig"
        out.append((art, seg.length))
    return out


def verlege(raum: Raum, muster: Muster, u: float, v: float, regeln: dict) -> dict:
    """Muster mit Rasterursprung o = u·t1 + v·t2 (Bezug: Raummitte) verlegen."""
    o = u * muster.t1 + v * muster.t2
    T = np.column_stack([muster.t1, muster.t2])
    T_inv = np.linalg.inv(T)
    xmin, ymin, xmax, ymax = raum.raum.bounds
    stuecke: list[Stueck] = []
    verworfen = []            # zu schmal: wird verfugt
    positionen = set()
    prep_flaechen = [prep(v) if not v.is_empty else None for v in raum.verlegeflaechen]
    for mot in muster.motive:
        soll_m = anwenden(mot.soll, mot.m)
        diag = math.hypot(soll_m.bounds[2] - soll_m.bounds[0], soll_m.bounds[3] - soll_m.bounds[1])
        rand = diag / min(np.linalg.norm(muster.t1), np.linalg.norm(muster.t2)) + 2
        ecken = np.array([[xmin, ymin], [xmin, ymax], [xmax, ymin], [xmax, ymax]]) - o
        ij = (T_inv @ ecken.T).T
        imin, jmin = np.floor(ij.min(axis=0) - rand).astype(int)
        imax, jmax = np.ceil(ij.max(axis=0) + rand).astype(int)
        achswinkel = math.degrees(math.atan2(mot.m[1, 0], mot.m[0, 0]))
        bx0, by0, bx1, by1 = soll_m.bounds
        for i in range(imin, imax + 1):
            for j in range(jmin, jmax + 1):
                d = o + i * muster.t1 + j * muster.t2
                if bx0 + d[0] > xmax or bx1 + d[0] < xmin or by0 + d[1] > ymax or by1 + d[1] < ymin:
                    continue
                mg = m_mul(m_trans(d[0], d[1]), mot.m)
                soll_g = anwenden(mot.soll, mg)
                if not soll_g.intersects(raum.raum):
                    continue
                roh_g = anwenden(mot.rohling, mg)
                rid = f"{mot.name}/{i}/{j}"
                inv = np.linalg.inv(mg)
                for k, (fl, pf) in enumerate(zip(raum.verlegeflaechen, prep_flaechen)):
                    if pf is None or not pf.intersects(soll_g):
                        continue
                    if pf.contains(soll_g):
                        teile = [soll_g]
                    else:
                        teile = polygone(soll_g.intersection(fl))
                    for teil in teile:
                        if teil.area < 1.0:
                            continue
                        breite = inkreis_durchmesser(teil)
                        if breite < regeln["verlegbar_min_breite_mm"]:
                            verworfen.append(teil)
                            continue
                        soll_ganz = abs(teil.area - soll_g.area) < 1e-6 * soll_g.area + 1e-6
                        ganz = soll_ganz and abs(soll_g.area - roh_g.area) < 1e-6 * roh_g.area
                        schn = [] if ganz else klassifiziere_schnitte(teil, roh_g, soll_g, raum, achswinkel)
                        stuecke.append(Stueck(rid, mot.name, mot.artikel, k, teil, anwenden(teil, inv), mg,
                                              ganz, soll_ganz, breite, schn))
                        positionen.add((rid, mot.artikel))
    stuecke.sort(key=lambda s: (s.rohling_id, s.facette, round(s.poly.centroid.x, 3), round(s.poly.centroid.y, 3)))
    return {"stuecke": stuecke, "verworfen": verworfen, "positionen": sorted(positionen),
            "muster": muster, "u": u, "v": v}


# ---------------------------------------------------------------------------
# 4. Reststück-Wiederverwendung (Greedy)
# ---------------------------------------------------------------------------

def symmetrien(rohling: Polygon) -> list[np.ndarray]:
    """Eigentliche Symmetrien des Rohlings (Drehungen um die Mitte, keine Spiegelung)."""
    c = rohling.centroid
    out = []
    for w in (0, 90, 180, 270):
        m = m_mul(m_trans(c.x, c.y), m_rot(w), m_trans(-c.x, -c.y))
        bild = anwenden(rohling, m)
        if bild.symmetric_difference(rohling).area < 1e-6 * rohling.area:
            out.append(m)
    return out


def wiederverwendung(stuecke: list[Stueck], rohlinge: dict[str, Polygon], schnittfuge: float,
                     rest_min: float) -> dict:
    """Greedy Best-Fit: jedes Schnittstück zuerst aus einem passenden Reststück.

    Rückgabe: je Artikel Anzahl neu angebrochener Rohlinge, Zuordnung und
    verbleibende Reststücke."""
    pools: dict[str, list[dict]] = {a: [] for a in rohlinge}
    neu: dict[str, int] = {a: 0 for a in rohlinge}
    herkunft = {}
    sym = {a: symmetrien(r) for a, r in rohlinge.items()}
    fabrik = {a: r.exterior.buffer(0.01) for a, r in rohlinge.items()}
    zu = [s for s in stuecke if not s.ganz]
    zu.sort(key=lambda s: (-round(s.poly.area, 3), s.rohling_id, s.facette))
    for s in zu:
        a = s.artikel
        p = s.lokal
        fk_p = p.exterior.intersection(fabrik[a])       # Fabrikkanten des Stücks
        best = None
        for idx, rest in enumerate(pools[a]):
            if rest["poly"].area + EPS < p.area:
                continue
            for m in sym[a]:
                q = anwenden(p, m)
                if not rest["prep"].contains(q):
                    continue
                if fk_p.length > 0.05:
                    fk_q = anwenden(fk_p, m)
                    if not rest["fabrik"].buffer(0.05).contains(fk_q):
                        continue
                kand = (rest["poly"].area, idx, m, q)
                if best is None or kand[0] < best[0]:
                    best = kand
                break
        if best is None:
            neu[a] += 1
            rid = f"{a}#{neu[a]}"
            herkunft[id(s)] = (rid, "neu")
            rest_poly = rohlinge[a].difference(p.buffer(schnittfuge / 2, join_style="mitre"))
            _pool_add(pools[a], rest_poly, rohlinge[a], rid, rest_min)
        else:
            _, idx, m, q = best
            rest = pools[a].pop(idx)
            herkunft[id(s)] = (rest["rid"], "reststueck")
            rest_poly = rest["poly"].difference(q.buffer(schnittfuge / 2, join_style="mitre"))
            _pool_add(pools[a], rest_poly, rohlinge[a], rest["rid"], rest_min)
    reste = {a: sum(r["poly"].area for r in pool) for a, pool in pools.items()}
    return {"neu": neu, "herkunft": herkunft, "rest_flaeche": reste}


def _pool_add(pool: list, geom, rohling: Polygon, rid: str, rest_min: float):
    for teil in polygone(geom):
        if teil.area < rest_min:
            continue
        fk = teil.exterior.intersection(rohling.exterior.buffer(0.01))
        pool.append({"poly": teil, "prep": prep(teil.buffer(1e-4, join_style="mitre")),
                     "fabrik": fk, "rid": rid})


# ---------------------------------------------------------------------------
# 5. Kennzahlen
# ---------------------------------------------------------------------------

def auswerten(raum: Raum, erg: dict, daten: dict, mit_greedy: bool = True) -> dict:
    muster: Muster = erg["muster"]
    fliesen = daten["fliesen"]
    regeln = daten["regeln"]
    kalk = daten["kalkulation"]
    stuecke: list[Stueck] = erg["stuecke"]
    rohlinge = {m.artikel: m.rohling for m in muster.motive}
    soll_fl = {m.name: m.soll.area for m in muster.motive}
    a_roh = {a: r.area for a, r in rohlinge.items()}

    verlegt = sum(s.poly.area for s in stuecke)
    n_ganz = sum(1 for s in stuecke if s.ganz)
    n_soll_ganz = sum(1 for s in stuecke if s.soll_ganz)
    kat = {k: 0 for k in ("ganz", *SCHNITTARTEN)}
    for s in stuecke:
        kat[s.kategorie] += 1
    schnitt_n = {a: 0 for a in SCHNITTARTEN}
    schnitt_l = {a: 0.0 for a in SCHNITTARTEN}
    for s in stuecke:
        for a, l in s.schnitte:
            schnitt_n[a] += 1
            schnitt_l[a] += l
    zeit_min = sum(schnitt_n[a] * kalk["zeit_min_je_schnitt"][a] for a in SCHNITTARTEN)

    klein_flaeche = [s for s in stuecke if not s.soll_ganz and s.poly.area < regeln["min_flaechenanteil"] * soll_fl[s.motiv]]
    klein_breite = [s for s in stuecke if not s.soll_ganz and s.breite < regeln["min_breite_mm"]]

    # (a) je Rasterposition ein Rohling
    n_pos = {a: 0 for a in rohlinge}
    for _, a in erg["positionen"]:
        n_pos[a] += 1
    # (c) naiv: jedes Stück eigener Rohling
    n_naiv = {a: 0 for a in rohlinge}
    for s in stuecke:
        n_naiv[s.artikel] += 1

    def verschnitt(n: dict) -> float:
        brutto = sum(n[a] * a_roh[a] for a in n)
        return (brutto - verlegt) / brutto if brutto > 0 else 0.0

    out = {
        "muster": muster.name, "entwaesserung": raum.entwaesserung,
        "u": round(erg["u"], 4), "v": round(erg["v"], 4),
        "raumflaeche_m2": raum.flaeche / 1e6,
        "verlegt_m2": verlegt / 1e6,
        "fugen_m2": (raum.flaeche - verlegt) / 1e6,
        "anzahl_stuecke": len(stuecke),
        "anzahl_ganz": n_ganz,
        "anzahl_sollform_ganz": n_soll_ganz,
        "stuecke_nach_kategorie": kat,
        "schnitte_anzahl": schnitt_n,
        "schnitte_laenge_m": {a: round(l / 1000, 3) for a, l in schnitt_l.items()},
        "schnitte_gesamt": sum(schnitt_n.values()),
        "schnittlaenge_gesamt_m": round(sum(schnitt_l.values()) / 1000, 3),
        "schnittzeit_min": round(zeit_min, 1),
        "kleinstuecke_unter_flaechenanteil": len(klein_flaeche),
        "kleinstuecke_unter_mindestbreite": len(klein_breite),
        "nicht_verlegt_verfugt": len(erg["verworfen"]),
        "rohlinge_je_position": n_pos,
        "rohlinge_naiv": n_naiv,
        "verschnitt_je_position": verschnitt(n_pos),
        "verschnitt_naiv": verschnitt(n_naiv),
    }
    if mit_greedy:
        wv = wiederverwendung(stuecke, rohlinge, daten["schnittfuge_mm"], regeln["rest_min_flaeche_mm2"])
        ganz_je_art = {a: sum(1 for s in stuecke if s.ganz and s.artikel == a) for a in rohlinge}
        n_bed = {a: ganz_je_art[a] + wv["neu"][a] for a in rohlinge}
        out["rohlinge_nach_wiederverwendung"] = n_bed
        out["aus_reststueck"] = sum(1 for h in wv["herkunft"].values() if h[1] == "reststueck")
        out["verschnitt_nach_wiederverwendung"] = verschnitt(n_bed)
        out["verschnitt_stueck"] = round(sum(n_bed.values()) - verlegt / (sum(a_roh.values()) / len(a_roh)), 2)
        out["_herkunft"] = wv["herkunft"]
        pakete = {}
        preis = 0.0
        for a, n in n_bed.items():
            fl = fliesen[muster.fliese]
            pakete[a] = math.ceil(n / fl["paket_stueck"]) if n else 0
            preis += n * fl["preis_eur_stueck"]
        out["pakete"] = pakete
        out["pakete_gesamt"] = sum(pakete.values())
        out["material_eur"] = round(preis, 2)
        out["zielwert_eur"] = round(preis + zeit_min / 60 * kalk["stundensatz_eur"]
                                    + (len(klein_flaeche) + len(klein_breite)) * kalk["strafe_kleinstueck_eur"], 2)
    return out


# ---------------------------------------------------------------------------
# 6. Rasterursprung optimieren
# ---------------------------------------------------------------------------

def optimiere(raum: Raum, muster: Muster, daten: dict, schritte: int) -> dict:
    """Grid-Search über u, v ∈ {0, 1/n, …}; Ziel: zielwert_eur, dann Stückzahl."""
    kandidaten = []
    for iu in range(schritte):
        for iv in range(schritte):
            u, v = iu / schritte, iv / schritte
            erg = verlege(raum, muster, u, v, daten["regeln"])
            k = auswerten(raum, erg, daten)
            kandidaten.append((k["zielwert_eur"], sum(k["rohlinge_nach_wiederverwendung"].values()),
                               k["schnitte_gesamt"], iu, iv, k, erg))
    kandidaten.sort(key=lambda t: t[:5])
    bester, schlechtester = kandidaten[0], kandidaten[-1]
    mitte = next(t for t in kandidaten if t[3] == 0 and t[4] == 0)
    return {"bester": bester[5], "bester_erg": bester[6], "schlechtester": schlechtester[5],
            "mitte": mitte[5], "anzahl_kandidaten": len(kandidaten),
            "spanne_zielwert_eur": round(schlechtester[0] - bester[0], 2)}


# ---------------------------------------------------------------------------
# 7. 3D-Stücke, SVG, IFC
# ---------------------------------------------------------------------------

def stueck_3d(raum: Raum, s: Stueck) -> list[tuple[float, float, float]]:
    fct = raum.facetten[s.facette]
    return [(round(x, 2), round(y, 2), round(fct.z(x, y), 3)) for x, y in list(s.poly.exterior.coords)[:-1]]


FARBE = {"ganz": "#9ecae1", "gerade": "#c7e9c0", "schraeg": "#fdd0a2", "gehrung": "#dadaeb",
         "gratschnitt": "#fc9272", "ablauf": "#bcbddc", "sonstig": "#ffffff"}


def svg(raum: Raum, erg: dict, kz: dict, pfad: Path, regeln: dict):
    skal = 0.25
    xmin, ymin, xmax, ymax = raum.raum.buffer(40).bounds
    w, h = (xmax - xmin) * skal, (ymax - ymin) * skal

    def pts(geom):
        return " ".join(f"{(x - xmin) * skal:.1f},{(ymax - y) * skal:.1f}" for x, y in geom.coords)

    teile = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h + 60:.0f}" '
             f'viewBox="0 0 {w:.0f} {h + 60:.0f}" font-family="sans-serif" font-size="11">',
             '<rect width="100%" height="100%" fill="#ffffff"/>',
             f'<polygon points="{pts(raum.raum.exterior)}" fill="#e5e5e5" stroke="#333" stroke-width="2"/>']
    klein = {id(s) for s in erg["stuecke"] if not s.soll_ganz and s.breite < regeln["min_breite_mm"]}
    for s in erg["stuecke"]:
        rand = "#d7301f" if id(s) in klein else "#555"
        teile.append(f'<polygon points="{pts(s.poly.exterior)}" fill="{FARBE[s.kategorie]}" '
                     f'stroke="{rand}" stroke-width="{1.5 if id(s) in klein else 0.4}"/>')
    if raum.ablauf is not None:
        for p in polygone(raum.ablauf):
            teile.append(f'<polygon points="{pts(p.exterior)}" fill="#636363" stroke="none"/>')
    for k in raum.knicke:
        teile.append(f'<polyline points="{pts(k.linie)}" fill="none" stroke="#08519c" stroke-width="1.2" '
                     f'stroke-dasharray="{"6,3" if k.art == "kehle" else "2,2"}"/>')
    y = h + 16
    x = 6
    for name, farbe in FARBE.items():
        if name == "sonstig":
            continue
        teile.append(f'<rect x="{x}" y="{y - 9}" width="10" height="10" fill="{farbe}" stroke="#555"/>'
                     f'<text x="{x + 13}" y="{y}">{name}</text>')
        x += 13 + 7 * len(name) + 12
    teile.append(f'<text x="6" y="{y + 18}">{kz["muster"]} / {kz["entwaesserung"]}: '
                 f'{sum(kz["rohlinge_nach_wiederverwendung"].values())} Rohlinge, Verschnitt '
                 f'{kz["verschnitt_nach_wiederverwendung"] * 100:.1f} %, {kz["schnitte_gesamt"]} Schnitte '
                 f'({kz["schnittlaenge_gesamt_m"]:.1f} m); rot umrandet: unter Mindestbreite; '
                 f'blau gestrichelt: Kehle, gepunktet: Grat</text>')
    teile.append("</svg>")
    pfad.parent.mkdir(parents=True, exist_ok=True)
    pfad.write_text("\n".join(teile), encoding="utf-8")


class IfcSchreiber:
    """Kleiner deterministischer IFC-Schreiber (Muster wie B14)."""

    def __init__(self, projekt: dict, dateiname: str):
        import ifcopenshell
        import ifcopenshell.guid
        self.io = ifcopenshell
        self.f = ifcopenshell.file(schema="IFC4X3_ADD2")
        self.pj = projekt
        self.dateiname = dateiname
        self._pfade: set[str] = set()

    def guid(self, pfad: str) -> str:
        if pfad in self._pfade:
            raise ValueError(f"Pfad doppelt: {pfad}")
        self._pfade.add(pfad)
        return self.io.guid.compress(uuid.uuid5(GUID_NAMENSRAUM, pfad).hex)

    def root(self, klasse: str, pfad: str, **attr):
        return self.f.create_entity(klasse, GlobalId=self.guid(pfad), **attr)

    def punkt(self, *c):
        return self.f.createIfcCartesianPoint([float(round(v, 3)) for v in c])

    def richtung(self, *c):
        return self.f.createIfcDirection([float(v) for v in c])

    def platzierung(self, relativ_zu=None):
        return self.f.createIfcLocalPlacement(relativ_zu, self.f.createIfcAxis2Placement3D(self.punkt(0, 0, 0)))

    def wert(self, v):
        if isinstance(v, bool):
            return self.f.create_entity("IfcBoolean", v)
        if isinstance(v, int):
            return self.f.create_entity("IfcInteger", v)
        if isinstance(v, float):
            return self.f.create_entity("IfcReal", v)
        s = str(v)
        return self.f.create_entity("IfcText" if len(s) > 255 else "IfcLabel", s)

    def pset(self, objekte: list, pfad: str, name: str, werte: dict, qto: bool = False):
        if qto:
            props = [self.f.create_entity("IfcQuantityArea" if k.endswith("Area") else "IfcQuantityLength",
                                          Name=k, **({"AreaValue": v} if k.endswith("Area") else {"LengthValue": v}))
                     for k, v in werte.items()]
            ps = self.root("IfcElementQuantity", pfad + "#" + name, Name=name, Quantities=props)
        else:
            props = [self.f.createIfcPropertySingleValue(k, None, self.wert(v), None) for k, v in werte.items()
                     if v is not None]
            ps = self.root("IfcPropertySet", pfad + "#" + name, Name=name, HasProperties=props)
        typen = [o for o in objekte if o.is_a("IfcTypeObject")]
        for t in typen:
            t.HasPropertySets = list(t.HasPropertySets or []) + [ps]
        rest = [o for o in objekte if not o.is_a("IfcTypeObject")]
        if rest:
            self.root("IfcRelDefinesByProperties", pfad + "#" + name + "#zuordnung",
                      RelatedObjects=rest, RelatingPropertyDefinition=ps)
        return ps

    def facettenkoerper(self, unten: list, oben: list):
        """Geschlossenes Prisma als IfcPolygonalFaceSet (oben = Belagoberfläche)."""
        n = len(oben)
        pts = self.f.createIfcCartesianPointList3D([list(map(float, p)) for p in oben + unten])
        flaechen = [self.f.createIfcIndexedPolygonalFace(list(range(1, n + 1))),
                    self.f.createIfcIndexedPolygonalFace(list(range(2 * n, n, -1)))]
        for i in range(n):
            j = (i + 1) % n
            flaechen.append(self.f.createIfcIndexedPolygonalFace([i + 1, n + i + 1, n + j + 1, j + 1]))
        return self.f.createIfcPolygonalFaceSet(pts, True, flaechen, None)

    def grundgeruest(self):
        import ifcopenshell.api.context
        import ifcopenshell.api.unit
        f = self.f
        projekt = self.root("IfcProject", "/projekt", Name=self.pj["name"])
        einheiten = [ifcopenshell.api.unit.add_si_unit(f, unit_type="LENGTHUNIT", prefix="MILLI"),
                     ifcopenshell.api.unit.add_si_unit(f, unit_type="AREAUNIT"),
                     ifcopenshell.api.unit.add_si_unit(f, unit_type="PLANEANGLEUNIT")]
        projekt.UnitsInContext = f.createIfcUnitAssignment(einheiten)
        modell = ifcopenshell.api.context.add_context(f, context_type="Model")
        self.body = ifcopenshell.api.context.add_context(f, context_type="Model", context_identifier="Body",
                                                         target_view="MODEL_VIEW", parent=modell)
        site = self.root("IfcSite", "/projekt/grundstueck", Name="Grundstück", ObjectPlacement=self.platzierung())
        geb = self.root("IfcBuilding", "/projekt/gebaeude", Name=self.pj["gebaeude"],
                        ObjectPlacement=self.platzierung(site.ObjectPlacement))
        gs = self.root("IfcBuildingStorey", "/projekt/gebaeude/gs", Name=self.pj["geschoss"], Elevation=0.0,
                       ObjectPlacement=self.platzierung(geb.ObjectPlacement))
        raum = self.root("IfcSpace", "/projekt/gebaeude/gs/raum", Name=self.pj["raum"],
                         ObjectPlacement=self.platzierung(gs.ObjectPlacement))
        for pfad, ob, unter in (("/projekt", projekt, site), ("/projekt/grundstueck", site, geb),
                                ("/projekt/gebaeude", geb, gs), ("/projekt/gebaeude/gs", gs, raum)):
            self.root("IfcRelAggregates", pfad + "#aggregiert", RelatingObject=ob, RelatedObjects=[unter])
        return raum

    def schreibe(self, pfad: Path):
        h = self.f.header
        h.file_description.description = ("ViewDefinition [NotAssigned]",)
        h.file_name.name = self.dateiname
        h.file_name.time_stamp = self.pj["zeitstempel"]
        h.file_name.author = (self.pj["autor"],)
        h.file_name.organization = (self.pj["organisation"],)
        h.file_name.authorization = "keine"
        pfad.parent.mkdir(parents=True, exist_ok=True)
        self.f.write(str(pfad))
        return pfad


def erzeuge_ifc(daten: dict, raum: Raum, erg: dict, kz: dict, modus: str, pfad: Path) -> dict:
    """modus 'einzeln': je Stück ein IfcCovering (Kind des Belags, IfcRelAggregates).
    modus 'aggregiert': ein IfcCovering; ganze Fliesen als IfcMappedItem, Schnittstücke als Facettenkörper."""
    muster: Muster = erg["muster"]
    fl = daten["fliesen"][muster.fliese]
    dicke = float(fl["dicke_mm"])
    w = IfcSchreiber(daten["projekt"], pfad.name)
    f = w.f
    ifc_raum = w.grundgeruest()
    herkunft = kz.get("_herkunft", {})

    # Typen je Artikel mit Hersteller-Pset und Darstellungsvorlage (Sollform je Motiv)
    typen, vorlagen = {}, {}
    for mot in muster.motive:
        if mot.artikel not in typen:
            t = w.root("IfcCoveringType", f"/typ/{mot.artikel}", Name=mot.artikel, PredefinedType="FLOORING")
            w.pset([t], f"/typ/{mot.artikel}", "Pset_ManufacturerTypeInformation",
                   {"GlobalTradeItemNumber": fl["gtin"], "ArticleNumber": mot.artikel, "Manufacturer": "Beispiel"})
            typen[mot.artikel] = t
        prof = f.createIfcArbitraryClosedProfileDef(
            "AREA", None, f.createIfcPolyline([f.createIfcCartesianPoint([float(x), float(y)])
                                               for x, y in mot.soll.exterior.coords]))
        koerper = f.createIfcExtrudedAreaSolid(prof, f.createIfcAxis2Placement3D(w.punkt(0, 0, -dicke)),
                                               w.richtung(0, 0, 1), dicke)
        vorlagen[mot.name] = f.createIfcRepresentationMap(
            f.createIfcAxis2Placement3D(w.punkt(0, 0, 0)),
            f.createIfcShapeRepresentation(w.body, "Body", "SweptSolid", [koerper]))
    for t in typen.values():
        t.RepresentationMaps = [vorlagen[m.name] for m in muster.motive if typen[m.artikel] is t]

    belag = w.root("IfcCovering", "/belag", Name=f"Duschboden {muster.name}", PredefinedType="FLOORING",
                   ObjectPlacement=w.platzierung(ifc_raum.ObjectPlacement))
    w.root("IfcRelContainedInSpatialStructure", "/belag#enthalten", RelatingStructure=ifc_raum,
           RelatedElements=[belag])
    w.root("IfcRelCoversSpaces", "/belag#bedeckt", RelatingSpace=ifc_raum, RelatedCoverings=[belag])
    w.pset([belag], "/belag", "HP_Verlegung", {
        "Muster": muster.typ, "Rasterursprung_u": float(kz["u"]), "Rasterursprung_v": float(kz["v"]),
        "Fugenbreite": float(daten["fuge_mm"]), "Gefaelle_Prozent": float(daten["gefaelle_prozent"]),
        "Entwaesserung": raum.entwaesserung, "Verschnitt": float(round(kz["verschnitt_nach_wiederverwendung"], 4)),
        "RohlingeBedarf": int(sum(kz["rohlinge_nach_wiederverwendung"].values())),
        "Pakete": int(kz["pakete_gesamt"]), "Kaliber": fl["kaliber"]})
    w.pset([belag], "/belag", "Pset_ManufacturerOccurrence", {"BatchReference": fl["charge"]})
    w.pset([belag], "/belag", "Qto_CoveringBaseQuantities",
           {"Width": dicke, "GrossArea": round(raum.flaeche / 1e6, 4), "NetArea": round(kz["verlegt_m2"], 4)},
           qto=True)

    stuecke: list[Stueck] = erg["stuecke"]
    if modus == "einzeln":
        kinder = []
        for n, s in enumerate(stuecke):
            oben = stueck_3d(raum, s)
            unten = [(x, y, z - dicke) for x, y, z in oben]
            form = f.createIfcProductDefinitionShape(None, None, [f.createIfcShapeRepresentation(
                w.body, "Body", "Tessellation", [w.facettenkoerper(unten, oben)])])
            pf = f"/belag/stueck/{n:04d}"
            c = w.root("IfcCovering", pf, Name=f"{s.rohling_id}#{s.facette}", ObjectType=s.kategorie,
                       ObjectPlacement=w.platzierung(belag.ObjectPlacement), Representation=form)
            kinder.append(c)
            h = herkunft.get(id(s), (s.rohling_id, "ganz"))
            schn = {a: 0 for a in SCHNITTARTEN}
            for a, _ in s.schnitte:
                schn[a] += 1
            w.pset([c], pf, "HP_Fliesenstueck", {
                "Stueckart": s.kategorie, "Motiv": s.motiv, "Rasterposition": s.rohling_id,
                "Gefaelleflaeche": raum.facetten[s.facette].name, "Rohling": h[0], "Herkunft": h[1],
                "Schnitte": int(len(s.schnitte)),
                "Schnittlaenge": float(round(sum(l for _, l in s.schnitte), 1)),
                "Schnittarten": ",".join(a for a in SCHNITTARTEN if schn[a])})
            w.pset([c], pf, "Qto_CoveringBaseQuantities",
                   {"Width": dicke, "NetArea": round(s.poly.area / 1e6, 6)}, qto=True)
        w.root("IfcRelAggregates", "/belag#teile", RelatingObject=belag, RelatedObjects=kinder)
        by_typ = {}
        for s, c in zip(stuecke, kinder):
            by_typ.setdefault(s.artikel, []).append(c)
        for a, objs in by_typ.items():
            w.root("IfcRelDefinesByType", f"/typ/{a}#zuordnung", RelatingType=typen[a], RelatedObjects=objs)
    else:
        items = []
        ursprung = f.createIfcAxis2Placement3D(w.punkt(0, 0, 0))
        identitaet = f.createIfcCartesianTransformationOperator3D(None, None, w.punkt(0, 0, 0), None, None)
        for s in stuecke:
            fct = raum.facetten[s.facette]
            if s.soll_ganz:
                # ganze Sollform: Vorlage des Typs, gedreht und auf die Gefälleebene gekippt
                mg = s.m_global
                ox, oy = mg[0, 2], mg[1, 2]
                a, b, _ = fct.ebene
                ax1 = np.array([mg[0, 0], mg[1, 0], a * mg[0, 0] + b * mg[1, 0]])
                ax1 /= np.linalg.norm(ax1)
                ax3 = np.array([-a, -b, 1.0]) / math.sqrt(a * a + b * b + 1)
                ax2 = np.cross(ax3, ax1)
                op = f.createIfcCartesianTransformationOperator3D(
                    w.richtung(*ax1), w.richtung(*ax2), w.punkt(ox, oy, fct.z(ox, oy)), None, w.richtung(*ax3))
                items.append(f.createIfcMappedItem(vorlagen[s.motiv], op))
            else:
                # Schnittstück: eigene Geometrie (Facettenkörper) als Einmal-Vorlage
                oben = stueck_3d(raum, s)
                koerper = w.facettenkoerper([(x, y, z - dicke) for x, y, z in oben], oben)
                vl = f.createIfcRepresentationMap(ursprung, f.createIfcShapeRepresentation(
                    w.body, "Body", "Tessellation", [koerper]))
                items.append(f.createIfcMappedItem(vl, identitaet))
        belag.Representation = f.createIfcProductDefinitionShape(None, None, [
            f.createIfcShapeRepresentation(w.body, "Body", "MappedRepresentation", items)])
        if len(typen) == 1:
            a = next(iter(typen))
            w.root("IfcRelDefinesByType", f"/typ/{a}#zuordnung", RelatingType=typen[a], RelatedObjects=[belag])
    w.schreibe(pfad)
    return {"datei": pfad.name, "bytes": pfad.stat().st_size, "entitaeten": len(list(f)),
            "coverings": len(f.by_type("IfcCovering"))}


# ---------------------------------------------------------------------------
# 8. Ablauf
# ---------------------------------------------------------------------------

def lade(pfad: Path = STANDARD_EINGABE) -> dict:
    return json.loads(pfad.read_text(encoding="utf-8"))


def fall(daten: dict, muster_name: str, entwaesserung: str, schritte: int) -> dict:
    raum = baue_raum(daten, entwaesserung)
    m = muster_bauen(muster_name, daten["muster"][muster_name], daten["fliesen"], daten["fuge_mm"])
    opt = optimiere(raum, m, daten, schritte)
    return {"raum": raum, "muster": m, **opt}


def oeffentlich(kz: dict) -> dict:
    """Kennzahlen ohne interne Felder, Flächen gerundet."""
    out = {k: v for k, v in kz.items() if not k.startswith("_")}
    for k, v in list(out.items()):
        if isinstance(v, float):
            out[k] = round(v, 4)
        elif isinstance(v, dict):
            out[k] = {kk: (round(vv, 4) if isinstance(vv, float) else vv) for kk, vv in v.items()}
    return out


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--ifc", action="store_true", help="IFC-Dateien für den Referenzfall schreiben")
    ap.add_argument("--schritte", type=int, default=None, help="Raster-Schritte je Richtung (Standard aus JSON)")
    ap.add_argument("--eingabe", type=Path, default=STANDARD_EINGABE)
    args = ap.parse_args(argv)
    daten = lade(args.eingabe)
    schritte = args.schritte or daten["optimierung"]["raster_schritte"]
    ergebnis = {"_hinweis": "Beispielwerte; Prototyp B16, siehe Recherche 17", "schritte": schritte, "faelle": {}}
    referenz = {}
    for ent in ("punkt", "zwei_rinnen"):
        for mn in daten["muster"]:
            r = fall(daten, mn, ent, schritte)
            key = f"{mn}__{ent}"
            b = r["bester"]
            ergebnis["faelle"][key] = {"bester": oeffentlich(b), "mitte_u0_v0": oeffentlich(r["mitte"]),
                                       "schlechtester": oeffentlich(r["schlechtester"]),
                                       "spanne_zielwert_eur": r["spanne_zielwert_eur"]}
            svg(r["raum"], r["bester_erg"], b, AUSGABE / f"b16_{key}.svg", daten["regeln"])
            print(f"{key:40s} Rohl.={sum(b['rohlinge_nach_wiederverwendung'].values()):4d} "
                  f"(Pos. {sum(b['rohlinge_je_position'].values()):4d}) "
                  f"VS={b['verschnitt_nach_wiederverwendung'] * 100:5.1f} % "
                  f"(Pos. {b['verschnitt_je_position'] * 100:5.1f} %) "
                  f"Schnitte={b['schnitte_gesamt']:4d} L={b['schnittlaenge_gesamt_m']:6.2f} m "
                  f"klein(B)={b['kleinstuecke_unter_mindestbreite']:3d} u,v=({b['u']},{b['v']})")
            if key in ("chevron_60x10__punkt", "gerade_60x60__punkt"):
                referenz[key] = r
    # 3D-Stückliste für den Referenzfall
    r = referenz["chevron_60x10__punkt"]
    liste = [{"rasterposition": s.rohling_id, "motiv": s.motiv, "kategorie": s.kategorie,
              "gefaelleflaeche": r["raum"].facetten[s.facette].name, "flaeche_mm2": round(s.poly.area, 1),
              "schnitte": [(a, round(l, 1)) for a, l in s.schnitte], "polygon_3d_mm": stueck_3d(r["raum"], s)}
             for s in r["bester_erg"]["stuecke"]]
    (AUSGABE / "b16_stuecke_chevron_60x10__punkt.json").write_text(
        json.dumps(liste, ensure_ascii=False, indent=1), encoding="utf-8")
    if args.ifc:
        ergebnis["ifc"] = {}
        for key, r in referenz.items():
            for modus in ("einzeln", "aggregiert"):
                info = erzeuge_ifc(daten, r["raum"], r["bester_erg"], r["bester"], modus,
                                   AUSGABE / f"b16_{key}_{modus}.ifc")
                try:
                    import ifcopenshell.validate
                    log = ifcopenshell.validate.json_logger()
                    ifcopenshell.validate.validate(str(AUSGABE / info["datei"]), log, express_rules=True)
                    info["validierung_befunde"] = len(log.statements)
                except Exception as exc:  # Validator optional
                    info["validierung_befunde"] = f"nicht geprüft: {exc}"
                ergebnis["ifc"][f"{key}_{modus}"] = info
                print("IFC", info)
    (AUSGABE / "b16_ergebnis.json").write_text(json.dumps(ergebnis, ensure_ascii=False, indent=1), encoding="utf-8")
    return ergebnis


if __name__ == "__main__":
    main()

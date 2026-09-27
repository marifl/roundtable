#!/usr/bin/env python3
"""
B17 – Grundstücksentwässerung (Schmutz- und Niederschlagswasser) vom Gebäude
bis zum öffentlichen Kanal bzw. zur Versickerung, Referenzstadt München (MSE).

Eingabe:  daten/b17_grundstuecksentwaesserung.json (Beispielgrundstück 20 x 30 m,
          Gelände mit Gefälle, Mischwasserkanal in der Straße, vier Szenarien)
Ausgabe:  ausgabe/b17_<szenario>.json          Haltungen, Schächte, Rigole, Prüfergebnis
          ausgabe/b17_<szenario>_lageplan.svg  Lageplan
          ausgabe/b17_<szenario>_abwicklung.svg Abwicklung des SW-Hauptstrangs
          ausgabe/b17_bericht.md               Tabellen aller Szenarien
          ausgabe/b17_<szenario>.ifc           nur mit --ifc (IFC4X3_ADD2)

ALLE Eingabezahlen sind BEISPIELWERTE (Regenreihe, kf, Höhen, Kanal). Normwerte
stehen im JSON-Block "regeln" mit Quelle und Status [V]/[U]; Herleitung in
docs/holzbau/recherche/18-grundstuecksentwaesserung-versickerung.md.
Das Ergebnis ist KEIN Entwässerungsantrag und keine Bemessung im Rechtssinn.

Rechenweg
---------
1. Niederschlagswasser (DWA-A 138-1:2024, "einfaches Verfahren" nach DWA-A 117):
     A_C  = Σ A_i · C_m,i                              (abflusswirksame Fläche)
     k_i  = k_f · f_Ort · f_Methode   (f_k <= 1)        (bemessungsrelevante Infiltrationsrate)
     Rigole (Kap. 6.4.2), Versickerung über Sohle, Seiten und Stirnseiten bis zur
     halben Höhe, mittlere Sickerfläche  A_S,m = b·L + h·(L + b):
       L(D) = [A_C·1e-7·r_D(n) − b·h·k_i − Q_Dr·1e-3] / [b·h·s_R/(D·60·f_Z) + (b + h)·k_i]
       L    = max über alle Dauerstufen D der Regenreihe (T = 5 a, n = 0,2)
     Speichernachweis: V(D) = (r_D·A_C·1e-4 − Q_S)·D·60·f_Z·1e-3 <= s_R·b·h·L
     Mulde (Vergleich NWFreiV § 3 Abs. 2): V(D) = (r_D·(A_C + A_S)·1e-4 − k_i·A_S·1e3)·D·60·f_Z·1e-3,
       Einstau V/A_S <= 0,30 m, zusätzlich A_S >= A_E/15 (TRENGW Tab. 1).
   Die Formeln sind an zwei veröffentlichten A-138-1-Rechnungen geprüft (tests/test_b17.py).
2. Schmutzwasser: Q_ww = K·√ΣDU (K = 0,5, mindestens größter Einzel-DU), Nennweite
   über Prandtl-Colebrook (k_b = 1 mm) mit Teilfüllung h/d = 0,5 (innen) bzw. 0,7 (außen).
3. Routing (deterministisch, ohne Zufall):
   Sichtbarkeitsgraph aus Quellen, Ziel, Ecken der Hindernisse (versetzt) und
   Austrittspunkten senkrecht zu den Außenwänden. Kantenkosten = Länge
   + Zuschlag innerhalb des Gebäudes / im Fundamentstreifen + Strafe je Kreuzung
   mit Sparten + Strafe je Formstück. Harte Hindernisse: Wurzelbereiche geschützter
   Bäume, Versickerungsanlage, Grundstücksgrenze. Mehrere Quellen: Steiner-Heuristik
   nach Takahashi-Matsuyama (die fernste Quelle zuerst, jede weitere Quelle an den
   nächsten Punkt des bestehenden Baums, Abtastung 0,5 m; der Baum selbst ist für
   neue Kanten ein Hindernis, damit nichts kreuzt oder doppelt läuft).
4. Höhenplan: Vorwärtsdurchlauf in Fließrichtung, Sohle(v) = min(Sohle(u) − L·s_min,
   GOK(v) − Frosttiefe) für Knoten außerhalb des Gebäudes; Rückwärtsdurchlauf
   begrenzt das Gefälle auf s_max, indem oberstromige Knoten tiefer gelegt werden.
5. Schächte: Revisionsschacht am Ende der Anlage auf eigenem Grund (EWS § 8 Abs. 4),
   Schacht an Zusammenführungen und Richtungswechseln > 45° außerhalb des Gebäudes,
   Reinigungsöffnung im Gebäude, Zusatzschacht bei Überschreitung des Höchstabstands.
   Schachtgröße aus der Einbautiefe (Tabelle im JSON).
6. Regelprüfung: EWS/MSE-Leitfaden, DIN 1986-100, NWFreiV/TRENGW, DWA-A 138-1.

Aufruf:   python b17_grundstuecksentwaesserung.py [--szenario ID] [--ifc]
"""
from __future__ import annotations

import argparse
import copy
import heapq
import json
import math
import uuid
from pathlib import Path

from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union
from shapely.prepared import prep

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b17_grundstuecksentwaesserung.json"
AUSGABE = HIER / "ausgabe"
GUID_NAMENSRAUM = uuid.uuid5(uuid.NAMESPACE_URL, "https://example.org/roundtable/holzbau/b17")

# Innendurchmesser KG-Rohr (DIN 1986-100 Tab. A.3, Kopfzeile) in m
INNENDURCHMESSER = {100: 0.096, 125: 0.113, 150: 0.146, 200: 0.184}
NU_WASSER = 1.31e-6          # kinematische Zähigkeit bei 10 °C in m²/s
G = 9.81


# ---------------------------------------------------------------- Eingabe ---

def lade(pfad: Path | str = STANDARD_EINGABE) -> dict:
    return json.loads(Path(pfad).read_text(encoding="utf-8"))


def setze(d: dict, pfad: str, wert) -> None:
    """Punkt-Pfad 'a.b.c' im verschachtelten dict setzen (Szenario-Änderungen)."""
    teile = pfad.split(".")
    for t in teile[:-1]:
        d = d[t]
    d[teile[-1]] = wert


def szenario_daten(basis: dict, szenario: str) -> dict:
    d = copy.deepcopy(basis)
    sz = next(s for s in basis["szenarien"] if s["id"] == szenario)
    for k, v in sz["aenderungen"].items():
        setze(d, k, v)
    d["_szenario"] = sz
    return d


def R(d: dict, name: str):
    """Regelwert aus dem JSON-Block 'regeln'."""
    return d["regeln"][name]["wert"]


def gok(d: dict, x: float, y: float) -> float:
    g = d["gelaende"]
    return g["z0"] + g["gx"] * x + g["gy"] * y


# -------------------------------------------------------------- Hydraulik ---

def q_ww(summe_du: float, k: float, max_du: float) -> float:
    """Schmutzwasserabfluss DIN EN 12056-2/DIN 1986-100: Q = K·√ΣDU, >= größter DU (l/s)."""
    return max(k * math.sqrt(summe_du), max_du) if summe_du > 0 else 0.0


def q_voll(di: float, gefaelle: float, kb_mm: float) -> float:
    """Vollfüllung nach Prandtl-Colebrook in l/s (di in m, Gefälle als Verhältnis)."""
    kb = kb_mm / 1000.0
    w = math.sqrt(2 * G * di * gefaelle)
    v = -2.0 * math.log10(2.51 * NU_WASSER / (di * w) + kb / (3.71 * di)) * w
    return v * math.pi * di ** 2 / 4.0 * 1000.0


def teilfuellungsfaktor(h_d: float) -> float:
    """Q(h)/Q_voll über die Kreisgeometrie mit dem Ansatz Q ~ A·R^(2/3)
    (Näherung; bei h/d = 0,5 exakt 0,5, weil R_halb = R_voll)."""
    th = 2.0 * math.acos(1.0 - 2.0 * h_d)
    a = (th - math.sin(th)) / 8.0
    p = th / 2.0
    av, rv = math.pi / 4.0, 0.25
    return (a / av) * ((a / p) / rv) ** (2.0 / 3.0)


def q_regen(r: float, c: float, a: float) -> float:
    """Regenwasserabfluss Q = r·C·A/10 000 in l/s (r in l/(s·ha), A in m²)."""
    return r * c * a / 10000.0


def waehle_dn(q: float, dn_min: int, gefaelle_fn, h_d: float, kb_mm: float) -> tuple[int, float]:
    """Kleinste Nennweite >= dn_min, deren Teilfüllungsleistung bei s_min(DN) reicht."""
    for dn in sorted(INNENDURCHMESSER):
        if dn < dn_min:
            continue
        cap = q_voll(INNENDURCHMESSER[dn], gefaelle_fn(dn), kb_mm) * teilfuellungsfaktor(h_d)
        if cap >= q:
            return dn, cap
    dn = max(INNENDURCHMESSER)
    return dn, q_voll(INNENDURCHMESSER[dn], gefaelle_fn(dn), kb_mm) * teilfuellungsfaktor(h_d)


# ----------------------------------------------------- Versickerung A 138-1 --

def k_i(kf: float, f_ort: float, f_methode: float) -> float:
    """Bemessungsrelevante Infiltrationsrate k_i = k·f_k mit f_k = f_Ort·f_Methode <= 1."""
    return kf * min(1.0, f_ort * f_methode)


def rigole_laenge(a_c: float, serie: dict[int, float], b: float, h: float, s_r: float,
                  ki: float, f_z: float, q_dr: float = 0.0) -> tuple[float, int, list]:
    """Erforderliche Rigolenlänge nach DWA-A 138-1 Kap. 6.4.2 (Sohle + Seiten + Stirn,
    mittlere Einstauhöhe h/2). Rückgabe (L_max, maßgebende Dauer D, Tabelle)."""
    tab = []
    for dauer in sorted(serie):
        r = serie[dauer]
        zaehler = a_c * 1e-7 * r - b * h * ki - q_dr * 1e-3
        nenner = b * h * s_r / (dauer * 60.0 * f_z) + (b + h) * ki
        tab.append((dauer, r, max(0.0, zaehler / nenner)))
    l_max, d_mass = max((l, dd) for dd, _, l in tab)
    return l_max, d_mass, tab


def rigole_sickerflaeche(b: float, h: float, laenge: float) -> float:
    """Mittlere Versickerungsfläche A_S,m = b·L + h·(L + b) (Sohle + halbe Seiten- und Stirnflächen)."""
    return b * laenge + h * (laenge + b)


def rigole_speicher(a_c: float, serie: dict[int, float], b: float, h: float, laenge: float,
                    s_r: float, ki: float, f_z: float) -> dict:
    """Speichernachweis für eine gewählte Rigole: V_erf = max_D (Q_zu − Q_S)·D·60·f_Z·1e-3."""
    a_s = rigole_sickerflaeche(b, h, laenge)
    q_s = ki * a_s * 1e3                                   # l/s
    tab = [(dd, r, max(0.0, (r * a_c * 1e-4 - q_s) * dd * 60.0 * f_z * 1e-3)) for dd, r in sorted(serie.items())]
    v_erf, d_mass = max((v, dd) for dd, _, v in tab)
    v_vorh = s_r * b * h * laenge
    return {"a_s": a_s, "q_s": q_s, "v_erf": v_erf, "d_mass": d_mass, "v_vorh": v_vorh,
            "entleerung_h": (v_erf / (q_s * 1e-3) / 3600.0) if q_s > 0 else math.inf, "tabelle": tab}


def mulde_flaeche(a_c: float, serie: dict[int, float], ki: float, f_z: float, einstau_max: float) -> float:
    """Kleinste Muldenfläche A_S (= überregnete Fläche) mit V/A_S <= Einstau_max (Bisektion)."""
    def einstau(a_s):
        v = max((r * (a_c + a_s) * 1e-4 - ki * a_s * 1e3) * dd * 60.0 * f_z * 1e-3 for dd, r in serie.items())
        return max(0.0, v) / a_s
    lo, hi = 0.5, 10000.0
    if einstau(hi) > einstau_max:
        return math.inf
    for _ in range(80):
        mid = 0.5 * (lo + hi)
        if einstau(mid) > einstau_max:
            lo = mid
        else:
            hi = mid
    return hi


# ------------------------------------------------------------ Geometrie -----

def ablenkung_grad(p0, p1, p2) -> float:
    """Richtungsänderung am Punkt p1 (0° = geradeaus)."""
    a = math.atan2(p1[1] - p0[1], p1[0] - p0[0])
    b = math.atan2(p2[1] - p1[1], p2[0] - p1[0])
    d = abs(math.degrees(b - a)) % 360.0
    return 360.0 - d if d > 180.0 else d


def rnd(p) -> tuple[float, float]:
    return (round(p[0], 3), round(p[1], 3))


def versatz_ecken(poly: Polygon, abstand: float) -> list[tuple[float, float]]:
    """Ecken eines (konvexen) Polygons, diagonal um 'abstand' nach außen versetzt."""
    c = poly.centroid
    pts = []
    for x, y in list(poly.exterior.coords)[:-1]:
        dx, dy = x - c.x, y - c.y
        sx = 0.0 if abs(dx) < 1e-9 else math.copysign(1.0, dx)
        sy = 0.0 if abs(dy) < 1e-9 else math.copysign(1.0, dy)
        pts.append(rnd((x + sx * abstand, y + sy * abstand)))
    return pts


def kreis_knoten(x, y, r, n=8) -> list[tuple[float, float]]:
    """Regelmäßiges n-Eck außerhalb eines Kreises (Umkreis-Ecken für den Sichtbarkeitsgraphen)."""
    rr = r / math.cos(math.pi / n) + 0.05
    return [rnd((x + rr * math.cos(2 * math.pi * k / n + math.pi / n), y + rr * math.sin(2 * math.pi * k / n + math.pi / n)))
            for k in range(n)]


def austrittspunkte(gebaeude: Polygon, p, abstand: float) -> list[tuple[float, float]]:
    """Punkte senkrecht vor jeder Außenwand (für den kürzesten Weg aus dem Gebäude)."""
    minx, miny, maxx, maxy = gebaeude.bounds
    x, y = p
    return [rnd((minx - abstand, y)), rnd((maxx + abstand, y)), rnd((x, miny - abstand)), rnd((x, maxy + abstand))]


# -------------------------------------------------------------- Routing -----

class Netz:
    """Baum in Fließrichtung: jeder Knoten hat höchstens einen Nachfolger."""

    def __init__(self, praefix: str):
        self.praefix = praefix
        self.knoten: dict[str, dict] = {}
        self.nach: dict[str, str | None] = {}
        self._n = 0

    def neu(self, xy, typ="punkt", name=None, **attr) -> str:
        if name is None:
            self._n += 1
            name = f"{self.praefix}K{self._n}"
        self.knoten[name] = {"x": round(xy[0], 3), "y": round(xy[1], 3), "typ": typ, **attr}
        self.nach.setdefault(name, None)
        return name

    def xy(self, k) -> tuple[float, float]:
        return (self.knoten[k]["x"], self.knoten[k]["y"])

    def kanten(self) -> list[tuple[str, str]]:
        return [(u, v) for u, v in self.nach.items() if v is not None]

    def vor(self, k) -> list[str]:
        return sorted(u for u, v in self.nach.items() if v == k)

    def laenge(self, u, v) -> float:
        return math.dist(self.xy(u), self.xy(v))

    def topologisch(self) -> list[str]:
        """Knoten von oberstrom nach unterstrom (deterministisch nach Name)."""
        grad = {k: len(self.vor(k)) for k in self.knoten}
        bereit = sorted(k for k, g in grad.items() if g == 0)
        out = []
        while bereit:
            k = bereit.pop(0)
            out.append(k)
            v = self.nach[k]
            if v is not None:
                grad[v] -= 1
                if grad[v] == 0:
                    bereit.append(v)
                    bereit.sort()
        return out

    def teile(self, u, v, xy, typ="punkt", **attr) -> str:
        """Kante u->v an xy teilen."""
        j = self.neu(xy, typ, **attr)
        self.nach[u] = j
        self.nach[j] = v
        return j

    def linien(self) -> list[LineString]:
        return [LineString([self.xy(u), self.xy(v)]) for u, v in self.kanten()]


class Router:
    """Sichtbarkeitsgraph mit gewichteten Kanten und Dijkstra (deterministisch)."""

    def __init__(self, grenze: Polygon, hart, zonen: list[tuple[Polygon, float]],
                 kreuzungen: list[tuple[LineString, float, str]], knick: float):
        self.grenze = prep(grenze)
        self.hart = prep(hart.buffer(-1e-3)) if hart is not None and not hart.is_empty else None
        self.zonen = [(z, prep(z), f) for z, f in zonen]
        self.kreuzungen = kreuzungen
        self.knick = knick

    def kosten(self, p, q, baum_hart) -> float | None:
        if p == q:
            return None
        seg = LineString([p, q])
        if not self.grenze.contains(seg):
            return None
        if self.hart is not None and self.hart.intersects(seg):
            return None
        if baum_hart is not None:
            bh, bh_p = baum_hart
            if bh_p.intersects(seg) and seg.intersection(bh).length > 0.05:
                return None
        laenge = seg.length
        c = laenge + self.knick
        for z, zp, f in self.zonen:
            if zp.intersects(seg):
                c += (f - 1.0) * seg.intersection(z).length
        for linie, strafe, _ in self.kreuzungen:
            if seg.intersects(linie):
                c += strafe
        return c

    def weg(self, start, knoten: list, ziele: set[int], baum_hart) -> tuple[float, list[int]] | None:
        """Dijkstra vom Startpunkt (Index 0 in 'knoten') zu einem der Zielindizes."""
        n = len(knoten)
        dist = {0: 0.0}
        vorg: dict[int, int] = {}
        heap = [(0.0, 0)]
        fertig = set()
        while heap:
            c, i = heapq.heappop(heap)
            if i in fertig:
                continue
            fertig.add(i)
            if i in ziele:
                pfad = [i]
                while pfad[-1] != 0:
                    pfad.append(vorg[pfad[-1]])
                return c, pfad[::-1]
            for j in range(n):
                if j in fertig:
                    continue
                k = self.kosten(knoten[i], knoten[j], baum_hart)
                if k is None:
                    continue
                nc = round(c + k, 9)
                if nc < dist.get(j, math.inf) - 1e-12:
                    dist[j] = nc
                    vorg[j] = i
                    heapq.heappush(heap, (nc, j))
        return None

    def kreuzt(self, p, q) -> list[str]:
        seg = LineString([p, q])
        return [name for linie, _, name in self.kreuzungen if seg.intersects(linie)]


def baue_baum(router: Router, praefix: str, quellen: list[dict], ziel: dict,
              basis_knoten: list[tuple[float, float]], abtastung: float = 0.5) -> tuple[Netz, list[str]]:
    """Steiner-Heuristik: fernste Quelle zuerst zum Ziel, jede weitere an den Baum."""
    netz = Netz(praefix)
    zk = netz.neu((ziel["x"], ziel["y"]), "ziel", name=ziel["id"])
    protokoll = []
    # Reihenfolge: Einzelkosten zum Ziel, absteigend (bei Gleichstand nach Id)
    einzel = []
    for q in quellen:
        pts = [rnd((q["x"], q["y"]))] + basis_knoten + [rnd((ziel["x"], ziel["y"]))]
        r = router.weg(pts[0], pts, {len(pts) - 1}, None)
        if r is None:
            raise RuntimeError(f"Quelle {q['id']} nicht an {ziel['id']} anschließbar")
        einzel.append((-r[0], q["id"], q))
    einzel.sort(key=lambda t: (t[0], t[1]))
    for _, _, q in einzel:
        # Anschlusspunkte am bestehenden Baum: Knoten (ohne Quellen) + Abtastpunkte auf Kanten
        ziele_xy, ziel_ref = [], []
        for k, a in netz.knoten.items():
            if a["typ"] != "quelle":
                ziele_xy.append(netz.xy(k))
                ziel_ref.append(("knoten", k, None))
        for u, v in netz.kanten():
            L = netz.laenge(u, v)
            n = int(L / abtastung - 1e-9)
            for i in range(1, n + 1):
                t = i * abtastung / L
                pu, pv = netz.xy(u), netz.xy(v)
                ziele_xy.append(rnd((pu[0] + t * (pv[0] - pu[0]), pu[1] + t * (pv[1] - pu[1]))))
                ziel_ref.append(("kante", u, v))
        linien = netz.linien()
        baum_hart = None
        if linien:
            bh = unary_union(linien).buffer(0.02)
            baum_hart = (bh, prep(bh))
        # Basisknoten, die auf dem bestehenden Baum liegen, würden ein Berühren ohne
        # Anschluss erlauben -> entfernen (der Baum ist über die Abtastpunkte vertreten)
        if linien:
            bl = unary_union(linien)
            basis_f = [p for p in basis_knoten if bl.distance(Point(p)) > 0.03]
        else:
            basis_f = list(basis_knoten)
        pts = [rnd((q["x"], q["y"]))] + basis_f + ziele_xy
        off = 1 + len(basis_f)
        r = router.weg(pts[0], pts, set(range(off, len(pts))), baum_hart)
        if r is None:
            raise RuntimeError(f"Quelle {q['id']} nicht an das Netz anschließbar")
        kosten, pfad = r
        art, a1, a2 = ziel_ref[pfad[-1] - off]
        if art == "knoten":
            end = a1
        else:
            end = netz.teile(a1, a2, pts[pfad[-1]], "punkt")
        vorher = netz.neu(pts[0], "quelle", name=q["id"], **{k: v for k, v in q.items() if k not in ("id", "x", "y")})
        for idx in pfad[1:-1]:
            k = netz.neu(pts[idx])
            netz.nach[vorher] = k
            vorher = k
        netz.nach[vorher] = end
        protokoll.append(f"{q['id']} -> {end} (Kosten {kosten:.2f} m-Äquivalent)")
    return netz, protokoll


def wanddurchfuehrungen(netz: Netz, gebaeude: Polygon) -> None:
    """Knoten an den Schnittpunkten mit der Gebäudeaußenwand einfügen (Hauswanddurchführung)."""
    rand = gebaeude.exterior
    for u, v in list(netz.kanten()):
        seg = LineString([netz.xy(u), netz.xy(v)])
        s = seg.intersection(rand)
        punkte = [s] if s.geom_type == "Point" else [g for g in getattr(s, "geoms", []) if g.geom_type == "Point"]
        punkte = [p for p in punkte if 1e-3 < seg.project(p) < seg.length - 1e-3]
        punkte.sort(key=seg.project)
        a = u
        for p in punkte:
            a = netz.teile(a, v, (p.x, p.y), "austritt")


def bereinige(netz: Netz) -> None:
    """Gerade durchlaufende Zwischenknoten ohne Funktion entfernen."""
    geaendert = True
    while geaendert:
        geaendert = False
        for k in sorted(netz.knoten):
            a = netz.knoten[k]
            v = netz.nach.get(k)
            vor = netz.vor(k)
            if a["typ"] == "punkt" and v is not None and len(vor) == 1:
                if ablenkung_grad(netz.xy(vor[0]), netz.xy(k), netz.xy(v)) < 0.5:
                    netz.nach[vor[0]] = v
                    del netz.nach[k], netz.knoten[k]
                    geaendert = True
                    break


# ------------------------------------------------------------ Höhenplan -----

def hoehenplan(netz: Netz, d: dict, gebaeude: Polygon, art: str) -> None:
    """Sohlhöhen: vorwärts (Mindestgefälle, Frosttiefe außen), rückwärts (Höchstgefälle)."""
    frost = R(d, "frosttiefe_sw" if art == "SW" else "frosttiefe_nw")
    s_max = R(d, "gefaelle_max")
    for k, a in netz.knoten.items():
        a["gok"] = gok(d, a["x"], a["y"])
        a["innen"] = gebaeude.contains(Point(a["x"], a["y"])) and a["typ"] != "austritt"
    topo = netz.topologisch()
    kanten = {(u, v): netz._kante_attr[(u, v)] for u, v in netz.kanten()}
    for _ in range(50):
        alt = {k: a.get("sohle") for k, a in netz.knoten.items()}
        for k in topo:
            a = netz.knoten[k]
            vor = netz.vor(k)
            if not vor:
                a["sohle"] = min(a["sohle_start"], a.get("sohle", math.inf))
            else:
                a["sohle"] = min(min(netz.knoten[u]["sohle"] - netz.laenge(u, k) * kanten[(u, k)]["s_min"] for u in vor),
                                 a.get("sohle_max_fix", math.inf), a.get("sohle", math.inf))
            if not a["innen"]:
                a["sohle"] = min(a["sohle"], a["gok"] - frost)
        for k in reversed(topo):
            v = netz.nach[k]
            if v is None:
                continue
            L = netz.laenge(k, v)
            a, b = netz.knoten[k], netz.knoten[v]
            if a["sohle"] - b["sohle"] > L * s_max + 1e-9:
                a["sohle"] = b["sohle"] + L * s_max
        if all(abs((alt[k] if alt[k] is not None else math.inf) - netz.knoten[k]["sohle"]) < 1e-9 for k in netz.knoten):
            break


# ----------------------------------------------------------- Bemessung ------

def dimensioniere(netz: Netz, d: dict, gebaeude: Polygon, art: str) -> None:
    """Last je Kante (ΣDU bzw. Q), Nennweite, Mindestgefälle."""
    kb = R(d, "rauheit_kb_mm")
    netz._kante_attr = {}
    topo = netz.topologisch()
    last: dict[str, float] = {}
    maxdu: dict[str, float] = {}
    for k in topo:
        a = netz.knoten[k]
        own = a.get("last", 0.0)
        last[k] = own + sum(last[u] for u in netz.vor(k))
        maxdu[k] = max([a.get("max_du", 0.0)] + [maxdu[u] for u in netz.vor(k)])
    for k in topo:
        v = netz.nach[k]
        if v is None:
            continue
        mitte = Point((netz.knoten[k]["x"] + netz.knoten[v]["x"]) / 2, (netz.knoten[k]["y"] + netz.knoten[v]["y"]) / 2)
        innen = gebaeude.contains(mitte)
        if art == "SW":
            q = q_ww(last[k], R(d, "abflusskennzahl_k"), maxdu[k])
            dn_min = R(d, "dn_min_innen") if innen else R(d, "dn_min_aussen_sw")
        else:
            q = last[k]
            dn_min = R(d, "dn_min_nw")
        h_d = R(d, "fuellgrad_innen") if innen else R(d, "fuellgrad_aussen")
        sfn = (lambda dn: R(d, "gefaelle_min_innen")) if innen else (lambda dn: 1.0 / dn)
        dn, _ = waehle_dn(q, dn_min, sfn, h_d, kb)
        # Nennweite in Fließrichtung nicht verringern
        dn = max([dn] + [netz._kante_attr[(u, k)]["dn"] for u in netz.vor(k)])
        netz._kante_attr[(k, v)] = {"innen": innen, "last": last[k], "q": q, "dn": dn,
                                    "s_min": sfn(dn), "h_d": h_d}


def kanten_tabelle(netz: Netz, d: dict, router: Router) -> list[dict]:
    kb = R(d, "rauheit_kb_mm")
    rows = []
    for u in netz.topologisch():
        v = netz.nach[u]
        if v is None:
            continue
        ka = netz._kante_attr[(u, v)]
        a, b = netz.knoten[u], netz.knoten[v]
        L = netz.laenge(u, v)
        s = (a["sohle"] - b["sohle"]) / L
        cap = q_voll(INNENDURCHMESSER[ka["dn"]], max(s, 1e-6), kb) * teilfuellungsfaktor(ka["h_d"])
        rows.append({
            "von": a.get("label", u), "nach": b.get("label", v), "_u": u, "_v": v,
            "lage": "Gebäude" if ka["innen"] else "Erdreich",
            "dn": ka["dn"], "laenge": round(L, 2), "gefaelle": round(s, 5), "gefaelle_min": round(ka["s_min"], 5),
            "sohle_oben": round(a["sohle"], 3), "sohle_unten": round(b["sohle"], 3),
            "gok_oben": round(a["gok"], 3), "gok_unten": round(b["gok"], 3),
            "q": round(ka["q"], 3), "q_zul": round(cap, 3), "auslastung": round(ka["q"] / cap, 3) if cap > 0 else None,
            "last": round(ka["last"], 3), "kreuzungen": router.kreuzt(netz.xy(u), netz.xy(v)),
        })
    return rows


def schacht_dn(d: dict, tiefe: float) -> tuple[int, str]:
    for grenze, dn, art in d["schachtgroessen"]["stufen"]:
        if tiefe <= grenze:
            return dn, art
    return 1000, "Einsteigschacht"


def setze_schaechte(netz: Netz, d: dict, art: str, ziel_art: str) -> None:
    """Schächte/Reinigungsöffnungen festlegen und Knoten beschriften."""
    grad_max = R(d, "richtungswechsel_schacht_grad")
    zaehl = {"S": 0, "RÖ": 0, "B": 0, "A": 0, "W": 0}
    for k in netz.topologisch():
        a = netz.knoten[k]
        vor = netz.vor(k)
        v = netz.nach[k]
        abl = max((ablenkung_grad(netz.xy(u), netz.xy(k), netz.xy(v)) for u in vor), default=0.0) if v and vor else 0.0
        a["ablenkung"] = round(abl, 1)
        if a["typ"] == "ziel":
            a["bauwerk"] = ziel_art
            a["label"] = k
            a["grund"] = "Ende der Grundstücksentwässerungsanlage (EWS § 8 Abs. 4)" if art == "SW" else "Vorreinigung vor der Rigole (NWFreiV § 3 Abs. 2)"
            continue
        if a["typ"] == "quelle":
            a["bauwerk"] = "Reinigungsöffnung"
            a["label"] = k
            a["grund"] = "Fuß der Fallleitung" if art == "SW" else "Standrohr mit Laubfangkorb (TRENGW Tab. 2)"
            continue
        if len(vor) >= 2:
            a["typ"] = "abzweig"
        elif abl >= 1.0 and a["typ"] == "punkt":
            a["typ"] = "bogen"
        grund = None
        if a["typ"] == "abzweig":
            grund = "Zusammenführung"
        elif abl > grad_max:
            grund = f"Richtungsänderung {abl:.0f}° > {grad_max:.0f}°"
        if grund and not a["innen"]:
            zaehl["S"] += 1
            a["bauwerk"], a["label"], a["grund"] = "Schacht", f"{art}-S{zaehl['S']}", grund
        elif grund:
            zaehl["RÖ"] += 1
            a["bauwerk"], a["label"], a["grund"] = "Reinigungsöffnung", f"{art}-RÖ{zaehl['RÖ']}", grund + " (im Gebäude)"
        else:
            key = {"austritt": "W", "abzweig": "A", "bogen": "B"}.get(a["typ"], "B")
            zaehl[key] += 1
            a["bauwerk"] = {"austritt": "Wanddurchführung", "abzweig": "Abzweig", "bogen": "Bogen"}.get(a["typ"], "Formstück")
            a["label"] = f"{art}-{key}{zaehl[key]}"


def pruefe_abstaende(netz: Netz, d: dict, art: str) -> None:
    """Höchstabstand zwischen Reinigungsöffnungen; bei Überschreitung Zusatzschacht auf der Kante."""
    reinigung = {"Schacht", "Reinigungsöffnung", "Revisionsschacht", "Filterschacht"}
    rest: dict[str, float] = {}
    n_extra = 0
    for k in netz.topologisch():
        a = netz.knoten[k]
        vor = netz.vor(k)
        acc = max((rest[u] + netz.laenge(u, k) for u in vor), default=0.0)
        if a.get("bauwerk") in reinigung:
            acc = 0.0
        rest[k] = acc
        v = netz.nach[k]
        if v is None:
            continue
        dn = netz._kante_attr[(k, v)]["dn"]
        limit = R(d, "ro_abstand_max_gross") if dn >= 150 else R(d, "ro_abstand_max_klein")
        L = netz.laenge(k, v)
        if acc + L > limit + 1e-9 and not netz._kante_attr[(k, v)]["innen"]:
            t = (limit - acc) / L
            pu, pv = netz.xy(k), netz.xy(v)
            j = netz.teile(k, v, (pu[0] + t * (pv[0] - pu[0]), pu[1] + t * (pv[1] - pu[1])), "punkt")
            netz._kante_attr[(k, j)] = dict(netz._kante_attr[(k, v)])
            netz._kante_attr[(j, v)] = netz._kante_attr.pop((k, v))
            n_extra += 1
            netz.knoten[j].update({"bauwerk": "Schacht", "label": f"{art}-SZ{n_extra}",
                                   "grund": f"Höchstabstand {limit:.0f} m", "gok": gok(d, *netz.xy(j)), "innen": False})
            netz.knoten[j]["sohle"] = netz.knoten[k]["sohle"] - t * (netz.knoten[k]["sohle"] - netz.knoten[v]["sohle"])
            rest[j] = 0.0


def schacht_tabelle(netz: Netz, d: dict, art: str) -> list[dict]:
    rows = []
    for k in netz.topologisch():
        a = netz.knoten[k]
        if a.get("bauwerk") not in ("Schacht", "Revisionsschacht", "Reinigungsöffnung", "Filterschacht"):
            continue
        tiefe = a["gok"] - a["sohle"]
        if a["bauwerk"] == "Reinigungsöffnung":
            dn, typ = None, "Reinigungsrohr/-öffnung"
        else:
            dn, typ = schacht_dn(d, tiefe)
            if a["bauwerk"] == "Revisionsschacht":
                dn = max(dn, d["schachtgroessen"]["revisionsschacht_dn_min"])
                typ = "Revisionsschacht (Übergabeschacht)"
            if a["bauwerk"] == "Filterschacht":
                typ = "Filterschacht (Vorreinigung)"
        a["dn_schacht"] = dn
        rows.append({"id": a["label"], "bauwerk": a["bauwerk"], "art": typ, "x": a["x"], "y": a["y"],
                     "deckel": round(a["gok"], 3), "sohle": round(a["sohle"], 3), "tiefe": round(tiefe, 3),
                     "dn": dn, "grund": a.get("grund", ""), "im_gebaeude": a["innen"]})
    return rows


# --------------------------------------------------------- Hauptrechnung ----

def pruefung(liste: list, pid: str, regel: str, quelle: str, ok: bool | None, text: str, stufe: str = "Verstoß") -> None:
    """ok=True -> erfüllt, ok=False -> Verstoß/Hinweis nach 'stufe', ok=None -> Hinweis."""
    status = "erfüllt" if ok else ("Hinweis" if ok is None else stufe)
    liste.append({"id": pid, "regel": regel, "quelle": quelle, "status": status, "text": text})


def platziere_rechteck(erlaubt: Polygon, laenge: float, breite: float, bezug, raster: float = 0.5):
    """Achsparalleles Rechteck (L x B) in 'erlaubt', möglichst nahe am Bezugspunkt."""
    ep = prep(erlaubt)
    minx, miny, maxx, maxy = erlaubt.bounds
    best = None
    for orient in ("x", "y"):
        lx, ly = (laenge, breite) if orient == "x" else (breite, laenge)
        nx = int(math.floor((maxx - minx - lx) / raster + 1e-9))
        ny = int(math.floor((maxy - miny - ly) / raster + 1e-9))
        for i in range(nx + 1):
            for j in range(ny + 1):
                x0, y0 = round(minx + i * raster, 3), round(miny + j * raster, 3)
                r = box(x0, y0, x0 + lx, y0 + ly)
                if not ep.contains(r):
                    continue
                c = r.centroid
                key = (round(math.dist((c.x, c.y), bezug), 6), orient, x0, y0)
                if best is None or key < best[0]:
                    best = (key, r, orient)
    return (None, None) if best is None else (best[1], best[2])


def berechne(d: dict) -> dict:
    """Komplette Berechnung eines Szenarios."""
    sz = d["_szenario"]
    geb = d["gebaeude"]
    gebaeude = Polygon(geb["polygon"])
    parzelle = Polygon(d["grundstueck"]["polygon"])
    pr: list[dict] = []
    warn: list[str] = []
    keller = bool(geb["keller"])

    # ---------- Niederschlagswasser: Flächen, Rigole --------------------
    rg = d["rigole"]
    serie = {int(k): float(v) for k, v in d["regen"]["t5"].items()}
    ab = d["abflussbeiwerte"]
    fl_rig = [f for f in d["flaechen"] if f["angeschlossen"] == "rigole"]
    a_e = sum(f["flaeche"] for f in fl_rig)
    a_c = sum(f["flaeche"] * ab[f["art"]]["cm"] for f in fl_rig)
    a_c_s = sum(f["flaeche"] * ab[f["art"]]["cs"] for f in fl_rig)
    bo = d["boden"]
    ki = k_i(bo["kf"], bo["f_ort"], bo["f_methode"])

    # Abstand der Versickerungsanlage zum Gebäude (DWA-A 138-1 5.3.2)
    gok_geb = gok(d, *gebaeude.centroid.coords[0])
    if keller:
        t_grube = gok_geb - geb["kellersohle_uk"]
        a_geb = geb["arbeitsraum"] + R(d, "abstand_gebaeude_faktor") * t_grube
    else:
        t_grube = geb["gruendungstiefe"]
        a_geb = R(d, "abstand_gebaeude_faktor") * t_grube
    baeume = d["hindernisse"]["baeume"]
    sparten = d["hindernisse"]["sparten"]
    befestigt = [Polygon(f["polygon"]) for f in d["flaechen"] if "polygon" in f]
    erlaubt = parzelle.buffer(-R(d, "abstand_grenze_versickerung"), join_style=2)
    erlaubt = erlaubt.difference(gebaeude.buffer(a_geb, join_style=2))
    for b in baeume:
        erlaubt = erlaubt.difference(Point(b["x"], b["y"]).buffer(b["kronenradius"]))
    for p in befestigt:
        erlaubt = erlaubt.difference(p.buffer(0.5, join_style=2))
    for s in sparten:
        erlaubt = erlaubt.difference(LineString(s["linie"]).buffer(s["abstand"]))
    quellen_nw_xy = [(r["x"], r["y"]) for r in geb["regenfallrohre"]] + \
                    [(f["ablauf"]["x"], f["ablauf"]["y"]) for f in fl_rig if "ablauf" in f]
    bezug = (sum(p[0] for p in quellen_nw_xy) / len(quellen_nw_xy), sum(p[1] for p in quellen_nw_xy) / len(quellen_nw_xy))

    rig = None
    for reihen in range(1, rg["max_reihen"] + 1):
        b_r, h_r = reihen * rg["element_b"], rg["element_h"]
        l_req, d_mass, l_tab = rigole_laenge(a_c, serie, b_r, h_r, rg["s_r"], ki, rg["f_z"])
        l_gew = round(math.ceil(l_req / rg["element_l"] - 1e-9) * rg["element_l"], 3)
        rect, orient = platziere_rechteck(erlaubt, l_gew, b_r, bezug)
        if rect is not None:
            sp = rigole_speicher(a_c, serie, b_r, h_r, l_gew, rg["s_r"], ki, rg["f_z"])
            rig = {"reihen": reihen, "b": b_r, "h": h_r, "l_erf": l_req, "l": l_gew, "d_mass": d_mass,
                   "rechteck": rect, "orient": orient, "speicher": sp, "l_tabelle": l_tab,
                   "elemente": reihen * round(l_gew / rg["element_l"])}
            break
    if rig is None:
        raise RuntimeError("Rigole passt nicht auf das Grundstück")
    rect = rig["rechteck"]
    minx, miny, maxx, maxy = rect.bounds
    # Zulaufseite = Stirnseite nahe am Schwerpunkt der Zuläufe, Filterschacht 1 m davor
    if rig["orient"] == "x":
        enden = [((minx, (miny + maxy) / 2), (minx - 1.0, (miny + maxy) / 2)), ((maxx, (miny + maxy) / 2), (maxx + 1.0, (miny + maxy) / 2))]
    else:
        enden = [(((minx + maxx) / 2, miny), ((minx + maxx) / 2, miny - 1.0)), (((minx + maxx) / 2, maxy), ((minx + maxx) / 2, maxy + 1.0))]
    enden.sort(key=lambda e: (round(math.dist(e[0], bezug), 6), e[0]))
    zulauf, fs_xy = enden[0]

    # Mulde als Vergleich (NWFreiV § 3 Abs. 2: Rigole nur, wenn flächenhaft nicht möglich)
    a_mulde_hyd = mulde_flaeche(a_c, serie, ki, rg["f_z"], R(d, "mulde_einstau_max"))
    a_mulde = max(a_mulde_hyd, a_e * R(d, "mulde_flaechenanteil"))
    seite = math.sqrt(a_mulde / 2.0)          # Mulde 2:1 als Platzhalter
    m_rect, _ = platziere_rechteck(erlaubt, 2 * seite, seite, bezug)

    # ---------- Schmutzwasser-Netz ---------------------------------------
    k_sw = "kosten_innen_faktor_keller" if keller else "kosten_innen_faktor"
    ein = d["kanal"]["einlass"]
    rs = {"id": "SW-RS", "x": ein["x"], "y": R(d, "rs_abstand_grenze")}
    baum_zonen = [Point(b["x"], b["y"]).buffer(b["kronenradius"] + R(d, "baum_wurzelzuschlag")) for b in baeume]
    hart_sw = unary_union(baum_zonen + [rect.buffer(1.0, join_style=2)])
    zonen = [(gebaeude, R(d, k_sw)),
             (gebaeude.buffer(R(d, "abstand_fundament"), join_style=2).difference(gebaeude), R(d, "kosten_fundament_faktor"))]
    kreuz_sw = [(LineString(s["linie"]), R(d, "kosten_kreuzung"), s["id"]) for s in sparten]
    grenze_leit = parzelle.buffer(-0.5, join_style=2)
    router_sw = Router(grenze_leit, hart_sw, zonen, kreuz_sw, R(d, "kosten_knick"))
    basis = versatz_ecken(gebaeude, R(d, "abstand_fundament") + 0.05)
    for b in baeume:
        basis += kreis_knoten(b["x"], b["y"], b["kronenradius"] + R(d, "baum_wurzelzuschlag"))
    basis += versatz_ecken(rect.buffer(1.0, join_style=2), 0.05)
    sohle_start_sw = geb["ffb_eg"] - (geb["sohle_unter_ffb_keller"] if keller else geb["sohle_unter_ffb_bodenplatte"])
    quellen_sw = []
    for fl in geb["fallleitungen"]:
        basis += austrittspunkte(gebaeude, (fl["x"], fl["y"]), R(d, "abstand_fundament") + 0.05)
        quellen_sw.append({"id": fl["id"], "x": fl["x"], "y": fl["y"], "last": round(sum(fl["du"].values()), 3),
                           "max_du": max(fl["du"].values()), "sohle_start": sohle_start_sw})
    basis = [p for p in dict.fromkeys(basis) if grenze_leit.contains(Point(p))]
    sw, prot_sw = baue_baum(router_sw, "SW-", quellen_sw, rs, basis)
    wanddurchfuehrungen(sw, gebaeude)
    bereinige(sw)
    dimensioniere(sw, d, gebaeude, "SW")
    for k, a in sw.knoten.items():
        a.setdefault("sohle_start", math.inf)
    hoehenplan(sw, d, gebaeude, "SW")
    setze_schaechte(sw, d, "SW", "Revisionsschacht")
    pruefe_abstaende(sw, d, "SW")
    haltungen_sw = kanten_tabelle(sw, d, router_sw)
    schaechte_sw = schacht_tabelle(sw, d, "SW")

    # Anschlusskanal (MSE: geradlinig, ohne Gefällewechsel, bis 1:1)
    rsk = sw.knoten["SW-RS"]
    l_ak = math.dist((rsk["x"], rsk["y"]), (ein["x"], ein["y"]))
    dn_ak = d["kanal"]["dn_anschlusskanal"]
    s_ak = (rsk["sohle"] - ein["sohle"]) / l_ak
    ak = {"von": "SW-RS", "nach": "Kanal-Einlass", "dn": dn_ak, "laenge": round(l_ak, 2), "gefaelle": round(s_ak, 5),
          "sohle_oben": round(rsk["sohle"], 3), "sohle_unten": round(ein["sohle"], 3),
          "q_zul": round(q_voll(INNENDURCHMESSER[dn_ak], max(s_ak, 1e-6), R(d, "rauheit_kb_mm")) * teilfuellungsfaktor(R(d, "fuellgrad_aussen")), 3)}

    # ---------- Niederschlagswasser-Netz --------------------------------
    fs = {"id": "NW-FS", "x": round(fs_xy[0], 3), "y": round(fs_xy[1], 3)}
    r52 = d["regen"]["r_5_2"]
    quellen_nw = []
    for rf in geb["regenfallrohre"]:
        q = q_regen(r52, ab["schraegdach_ziegel"]["cs"], rf["dachflaeche"])
        quellen_nw.append({"id": rf["id"], "x": rf["x"], "y": rf["y"], "last": round(q, 4), "flaeche": rf["dachflaeche"]})
    for f in fl_rig:
        if "ablauf" in f:
            q = q_regen(r52, ab[f["art"]]["cs"], f["flaeche"])
            quellen_nw.append({"id": f["ablauf"]["id"], "x": f["ablauf"]["x"], "y": f["ablauf"]["y"], "last": round(q, 4), "flaeche": f["flaeche"]})
    sw_linien = sw.linien()
    hart_nw = unary_union(baum_zonen + [rect.buffer(0.2, join_style=2), gebaeude])
    kreuz_nw = [(LineString(s["linie"]), R(d, "kosten_kreuzung"), s["id"]) for s in sparten] + \
               [(ln, 2.0, "SW-Leitung") for ln in sw_linien]
    band = gebaeude.buffer(R(d, "abstand_fundament"), join_style=2).difference(gebaeude)
    zonen_nw = [(band, R(d, "kosten_fundament_faktor_nw")),
                (unary_union(sw_linien).buffer(R(d, "abstand_nw_sw")), R(d, "kosten_nahe_sw_faktor"))]
    router_nw = Router(grenze_leit, hart_nw, zonen_nw, kreuz_nw, R(d, "kosten_knick"))
    basis_nw = versatz_ecken(gebaeude, R(d, "abstand_fundament") + 0.05) + versatz_ecken(rect.buffer(0.2, join_style=2), 0.05)
    for b in baeume:
        basis_nw += kreis_knoten(b["x"], b["y"], b["kronenradius"] + R(d, "baum_wurzelzuschlag"))
    basis_nw = [p for p in dict.fromkeys(basis_nw) if grenze_leit.contains(Point(p))]
    for q in quellen_nw:
        q["sohle_start"] = gok(d, q["x"], q["y"]) - R(d, "frosttiefe_nw")
    nw, prot_nw = baue_baum(router_nw, "NW-", quellen_nw, fs, basis_nw)
    bereinige(nw)
    dimensioniere(nw, d, gebaeude, "NW")
    for k, a in nw.knoten.items():
        a.setdefault("sohle_start", math.inf)
    hoehenplan(nw, d, gebaeude, "NW")
    setze_schaechte(nw, d, "NW", "Filterschacht")
    pruefe_abstaende(nw, d, "NW")
    haltungen_nw = kanten_tabelle(nw, d, router_nw)
    schaechte_nw = schacht_tabelle(nw, d, "NW")

    # Rigolenhöhen
    fsk = nw.knoten["NW-FS"]
    rig_ok = fsk["sohle"] - rg["zulauf_absturz"]
    rig_sohle = rig_ok - rig["h"]
    gok_rig = gok(d, rect.centroid.x, rect.centroid.y)
    sickerraum = rig_sohle - bo["mhgw"]
    abstand_geb_ist = rect.distance(gebaeude)

    # ---------- Prüfungen: Schmutzwasser --------------------------------
    rs_dn = next(s["dn"] for s in schaechte_sw if s["id"] == "SW-RS")
    rs_kreis = Point(rsk["x"], rsk["y"]).buffer(rs_dn / 2000.0 + 0.1)
    pruefung(pr, "SW-01", "Revisionsschacht am Ende der Anlage auf eigenem Grund", "EWS § 8 Abs. 4 [V]",
             parzelle.contains(rs_kreis), f"Revisionsschacht DN {rs_dn} bei ({rsk['x']:.2f}; {rsk['y']:.2f}), "
             f"Außenkante {rs_kreis.exterior.distance(parzelle.exterior):.2f} m innerhalb der Grenze")
    platz = min(pt[1] for pt in gebaeude.exterior.coords) - 0.0
    pruefung(pr, "SW-02", "Außenliegender Revisionsschacht nur bei >= 5 m zwischen Grenze und Gebäudekante",
             "MSE-Leitfaden 2.6 [V]", platz >= R(d, "rs_min_platz_gebaeude"),
             f"Abstand Straßengrenze-Gebäude {platz:.2f} m")
    frost_fehler = [f"{a.get('label', k)} ({a['gok'] - a['sohle']:.2f} m)" for k, a in sw.knoten.items()
                    if not a["innen"] and a["gok"] - a["sohle"] < R(d, "frosttiefe_sw") - 1e-6]
    pruefung(pr, "SW-03", "Frostfreie Tiefe 1,20 m (GOK bis Rohrsohle) für erdverlegte SW-Leitungen",
             "MSE-Leitfaden 2.7, EWS § 8 Abs. 3 [V]", not frost_fehler, ", ".join(frost_fehler) or "alle Knoten >= 1,20 m")
    gef_fehler = [f"{h['von']}-{h['nach']} {h['gefaelle'] * 100:.2f} % < {h['gefaelle_min'] * 100:.2f} %"
                  for h in haltungen_sw if h["gefaelle"] < h["gefaelle_min"] - 1e-6]
    pruefung(pr, "SW-04", "Mindestgefälle Grundleitungen (0,5 % im Gebäude, 1:DN außerhalb)", "DIN 1986-100 [V]",
             not gef_fehler, ", ".join(gef_fehler) or "eingehalten")
    steil = [f"{h['von']}-{h['nach']} {h['gefaelle'] * 100:.1f} %" for h in haltungen_sw if h["gefaelle"] > R(d, "gefaelle_max") + 1e-6]
    pruefung(pr, "SW-05", "Höchstgefälle 1:20 (sonst Absturzbauwerk)", "kommunale Merkblätter [U]", not steil,
             ", ".join(steil) or "eingehalten")
    s_ak_min = 1.0 / dn_ak
    if s_ak < s_ak_min - 1e-9:
        pruefung(pr, "SW-06", "Anschlusskanal mit Mindestgefälle im Freispiegel",
                 "EWS § 8 Abs. 5, MSE-Leitfaden 2.6 [V]", False,
                 f"Gefälle {s_ak * 100:.2f} % < {s_ak_min * 100:.2f} % (Sohle RS {rsk['sohle']:.3f} / Einlass {ein['sohle']:.3f}): "
                 "Freispiegelentwässerung nicht möglich -> Abwasserhebeanlage (DIN EN 12050-1, DIN EN 12056-4) für das Gebäude erforderlich")
    else:
        pruefung(pr, "SW-06", "Anschlusskanal geradlinig, ohne Gefällewechsel, Gefälle 1:DN bis 1:1",
                 "MSE-Leitfaden 2.6 [V]", s_ak <= R(d, "gefaelle_max_anschlusskanal") + 1e-9,
                 f"L = {l_ak:.2f} m, Gefälle {s_ak * 100:.1f} % (zulässig {s_ak_min * 100:.2f}-100 %)")
    dn_fehler = [f"{h['von']}-{h['nach']}" for h in haltungen_sw for g in haltungen_sw
                 if g["nach"] == h["von"] and g["dn"] > h["dn"]]
    pruefung(pr, "SW-07", "Nennweite in Fließrichtung nicht verringern", "DIN 1986-100 6.1.8 [V]", not dn_fehler,
             ", ".join(dn_fehler) or "eingehalten")
    ausl = max(h["auslastung"] for h in haltungen_sw)
    pruefung(pr, "SW-08", "Hydraulische Leistungsfähigkeit (Q_ww <= Q bei h/d 0,5 innen / 0,7 außen)",
             "DIN 1986-100 14.1.5 [V/U]", ausl <= 1.0, f"max. Auslastung {ausl:.2f}")
    n_s = sum(1 for s in schaechte_sw if s["bauwerk"] == "Schacht")
    n_ro = sum(1 for s in schaechte_sw if s["bauwerk"] == "Reinigungsöffnung")
    pruefung(pr, "SW-09", "Reinigungsöffnungen an Fallleitungsfüßen, Zusammenführungen, Richtungsänderungen > 45°, Abstand <= 20/40 m",
             "DIN 1986-100 6.6 [U]", True, f"{n_s} Schacht/Schächte außen, {n_ro} Reinigungsöffnung(en), Revisionsschacht DN {rs_dn}")
    rse = d["strasse"]["rueckstauebene"]
    tief = []
    if geb["ffb_eg"] <= rse:
        tief.append(f"EG (FFB {geb['ffb_eg']:.2f})")
    if keller:
        tief.append(f"UG (FFB {geb['ffb_ug']:.2f}): " + ", ".join(a["id"] for a in geb["ablaufstellen_ug"]))
    if tief:
        faek = any(a["faekalienhaltig"] for a in geb["ablaufstellen_ug"]) if keller else True
        gefaelle_da = (geb["ffb_ug"] - 0.3) > ein["sohle"] if keller else True
        pruefung(pr, "SW-10", "Ablaufstellen unter der Rückstauebene gegen Rückstau sichern",
                 "EWS § 8 Abs. 6, MSE-Leitfaden 2.2/2.3, DIN EN 12056-4, DIN 1986-100 Abschn. 13 [V]", False,
                 f"Rückstauebene {rse:.2f} m (Straßenoberkante). Unter RSE: {'; '.join(tief)}. "
                 f"Abwasserhebeanlage {'DIN EN 12050-1' if faek else 'DIN EN 12050-2 (fäkalienfrei)'} mit Rückstauschleife über RSE; "
                 f"Rückstauverschluss (DIN EN 13564) nur bei Gefälle zum Kanal ({'ja' if gefaelle_da else 'nein'}), "
                 "Räumen untergeordneter Nutzung, kleinem Benutzerkreis und WC über RSE (MSE-Merkblatt Kellerüberflutung)",
                 stufe="Auflage")
    else:
        pruefung(pr, "SW-10", "Ablaufstellen unter der Rückstauebene gegen Rückstau sichern",
                 "EWS § 8 Abs. 6, MSE-Leitfaden 2.2 [V]", True,
                 f"alle Ablaufstellen über RSE {rse:.2f} m (FFB EG {geb['ffb_eg']:.2f}); keine Rückstausicherung nötig")
    alle_sw = unary_union(sw.linien() + [LineString([(rsk["x"], rsk["y"]), (ein["x"], ein["y"])])])
    nahe = [f"{b['id']} ({alle_sw.distance(Point(b['x'], b['y'])):.1f} m)" for b in baeume
            if b.get("geschuetzt") and alle_sw.distance(Point(b["x"], b["y"])) <= R(d, "baum_meldeabstand")]
    pruefung(pr, "SW-11", "Geschützte Gehölze <= 5 m zur Leitungsachse im Plan 1:100 darstellen, ggf. Stellungnahme Baumschutz",
             "MSE-Genehmigungsantrag Ziff. 3, MSE-Leitfaden 3.2 [V]", None if nahe else True,
             ("darzustellen: " + ", ".join(nahe)) if nahe else "keine geschützten Gehölze im 5-m-Bereich")
    kreuz = sorted({f"{h['von']}-{h['nach']} x {k}" for h in haltungen_sw for k in h["kreuzungen"]})
    pruefung(pr, "SW-12", "Kreuzungen mit Versorgungsleitungen im Plan eintragen, Abstände mit Netzbetreiber klären",
             "MSE-Leitfaden 3.2 (Sparten im Bereich von SW-Leitungen) [V], Abstandswerte [U]", None if kreuz else True,
             ", ".join(kreuz) or "keine Kreuzung")
    l_innen = sum(h["laenge"] for h in haltungen_sw if h["lage"] == "Gebäude")
    pruefung(pr, "SW-13", "Grundleitungen innerhalb von Gebäuden vermeiden; in der Bodenplatte genehmigungspflichtig",
             "DIN 1986-100 6.1.1, MSE-Leitfaden 2.1 [V]", None,
             f"{l_innen:.2f} m Leitung im/unter dem Gebäude ({'Sammelleitung im Keller' if keller else 'Grundleitung unter Bodenplatte'})")

    # ---------- Prüfungen: Niederschlagswasser --------------------------
    kf = bo["kf"]
    pruefung(pr, "NW-01", "Durchlässigkeit im Bereich 1e-6 bis 1e-3 m/s", "DWA-A 138-1, MSE-Leitfaden 3.2 [V]",
             R(d, "kf_min") <= kf < R(d, "kf_max"), f"k_f = {kf:.1e} m/s, k_i = {ki:.2e} m/s (f_k = {min(1.0, bo['f_ort'] * bo['f_methode']):.2f})")
    if sickerraum >= R(d, "sickerraum_min") - 1e-9:
        pruefung(pr, "NW-02", "Sickerraum >= 1 m (Sohle bis MHGW)", "TRENGW Nr. 6, DWA-A 138-1 [V]", True,
                 f"Sohle {rig_sohle:.2f}, MHGW {bo['mhgw']:.2f} -> {sickerraum:.2f} m")
    elif sickerraum >= R(d, "sickerraum_absolut_min") - 1e-9:
        pruefung(pr, "NW-02", "Sickerraum >= 1 m (Sohle bis MHGW)", "TRENGW Nr. 6, DWA-A 138-1, MSE-Leitfaden 3.2 [V]", False,
                 f"{sickerraum:.2f} m < 1,0 m: nicht erlaubnisfrei, wasserrechtliche Erlaubnis bei der MSE nötig; "
                 "Oberbodenversickerung oder flachere Zuleitung prüfen", stufe="Erlaubnispflicht")
    else:
        pruefung(pr, "NW-02", "Sickerraum >= 0,5 m (absolute Untergrenze)", "MSE-Leitfaden 3.2 (WWA München) [V]", False,
                 f"{sickerraum:.2f} m < 0,5 m: unzulässig; Mulde/Flächenversickerung oder andere Lösung erforderlich")
    pruefung(pr, "NW-03", "Sohle der Versickerungsanlage <= 5 m unter GOK", "TRENGW Nr. 6 [V]",
             gok_rig - rig_sohle <= R(d, "sohle_max_tiefe"), f"{gok_rig - rig_sohle:.2f} m")
    pruefung(pr, "NW-04", "Angeschlossene befestigte Fläche je Anlage <= 1000 m²", "NWFreiV § 3 Abs. 1 [V]",
             a_e <= R(d, "flaeche_max_erlaubnisfrei"), f"A_E,b = {a_e:.1f} m²")
    pruefung(pr, "NW-05", "Rigole nur, wenn flächenhafte Versickerung (Mulde) nicht möglich ist",
             "NWFreiV § 3 Abs. 2, TRENGW Nr. 4 [V]", None if m_rect is not None else True,
             (f"Mulde mit A_S >= {a_mulde:.1f} m² (hydraulisch {a_mulde_hyd:.1f} m², TRENGW 1/15: {a_e / 15:.1f} m²) "
              "passt auf das Grundstück -> Rigole begründen oder Mulde wählen") if m_rect is not None
             else f"Mulde mit {a_mulde:.1f} m² passt nicht; Rigole zulässig")
    vorr = ["Dach: Laubfangkörbe/Grobstoffrückhalt", "Terrasse: Hofablauf mit Schlammeimer"]
    pruefung(pr, "NW-06", "Vorreinigung vor unterirdischer Versickerung", "TRENGW Tab. 2 [V]; DWA-A 138-1 Tab. 7 [U]", None,
             "; ".join(vorr) + "; Filterschacht NW-FS vor der Rigole. Nach DWA-A 138-1 sind auch Dachabflüsse zu behandeln "
             "(Gesamtwirkungsgrad je Flächenkategorie) – Produkt mit Nachweis wählen")
    metall = [f["id"] for f in d["flaechen"] if f.get("material_metall_unbeschichtet") and f["flaeche"] > R(d, "metalldach_grenze")]
    pruefung(pr, "NW-07", "Unbeschichtete Cu/Zn/Pb-Flächen > 50 m² nur über zugelassenen Filter", "NWFreiV § 3 Abs. 2 [V]",
             not metall, ", ".join(metall) or "keine")
    pruefung(pr, "NW-08", "Abstand Versickerungsanlage-Gebäude >= 1,5 x Baugruben-/Fundamenttiefe",
             "DWA-A 138-1 5.3.2 [V (Sekundärquelle)]", abstand_geb_ist >= a_geb - 1e-6,
             f"vorhanden {abstand_geb_ist:.2f} m, erforderlich {a_geb:.2f} m ({'Keller' if keller else 'Fundament'}tiefe {t_grube:.2f} m)")
    pruefung(pr, "NW-09", "Abstand zur Grundstücksgrenze >= 2 m", "kommunale Leitfäden [U]",
             rect.distance(parzelle.exterior) >= R(d, "abstand_grenze_versickerung") - 1e-6, f"{rect.distance(parzelle.exterior):.2f} m")
    pruefung(pr, "NW-10", "Kein Überlauf der Versickerungsanlage an den städtischen Kanal", "MSE-Leitfaden 5.2 [V]",
             not rg["ueberlauf_kanal"], "kein Notüberlauf zum Kanal vorgesehen" if not rg["ueberlauf_kanal"] else "Überlauf geplant")
    pruefung(pr, "NW-11", "Überflutungsnachweis bei A_C > 800 m²", "DIN 1986-100 14.9, DWA-A 138-1 5.3.4 [V]",
             True if a_c_s <= R(d, "ueberflutung_ac_grenze") else False,
             f"A_C (C_s) = {a_c_s:.1f} m² -> {'nicht erforderlich; nach DWA-A 138-1 Überflutungsfolgen trotzdem qualitativ bewerten' if a_c_s <= 800 else 'erforderlich (r(D,30))'}")
    frost_nw = [f"{a.get('label', k)}" for k, a in nw.knoten.items() if a["gok"] - a["sohle"] < R(d, "frosttiefe_nw") - 1e-6]
    pruefung(pr, "NW-12", "Frosttiefe 0,80 m für NW-Leitungen zur Versickerung", "MSE-Leitfaden 2.7 [V]",
             not frost_nw, ", ".join(frost_nw) or "eingehalten")
    gs = d["grundstueck"]
    pruefung(pr, "NW-13", "Erlaubnisfrei nur außerhalb von Wasserschutzgebieten und Altlastverdachtsflächen",
             "NWFreiV § 1 [V]", not (gs["wasserschutzgebiet"] or gs["altlastverdacht"]),
             "laut Technischem Formblatt (hier Beispielangabe: nein/nein)")
    pruefung(pr, "NW-14", "Niederschlagswasser nicht in den städtischen Kanal einleiten (kein Anspruch)",
             "EWS § 4 Abs. 4, MSE-Leitfaden 2.4/5 [V]", True, "vollständige Versickerung auf dem Grundstück")
    sp = rig["speicher"]
    pruefung(pr, "NW-15", "Speichernachweis der Rigole V_vorh >= V_erf", "DWA-A 138-1 Gl. 8 [V (Sekundärquelle)]",
             sp["v_vorh"] >= sp["v_erf"] - 1e-9,
             f"V_vorh = {sp['v_vorh']:.2f} m³ >= V_erf = {sp['v_erf']:.2f} m³ (D = {sp['d_mass']} min), Entleerung {sp['entleerung_h']:.1f} h")

    # ---------- Gebühren (EAS München) -----------------------------------
    gebuehr = {
        "grundstuecksflaeche": parzelle.area, "gebietsabflussbeiwert": gs["gebietsabflussbeiwert"],
        "reduzierte_flaeche": round(parzelle.area * gs["gebietsabflussbeiwert"], 2),
        "nw_gebuehr_pauschal_eur_a": round(parzelle.area * gs["gebietsabflussbeiwert"] * R(d, "gebuehr_nw_satz"), 2),
        "nw_gebuehr_bei_vollversickerung_eur_a": 0.0,
        "hinweis": "Pauschale nach EAS § 8 Abs. 2-3; bei vollständiger Versickerung Antrag nach § 8 Abs. 5 (tatsächliche Ableitungsfläche 0 m²). Sätze gelten bis 31.12.2026 (Kalkulationszeitraum).",
    }

    return {
        "szenario": sz["id"], "beschreibung": sz["beschreibung"],
        "schmutzwasser": {"haltungen": haltungen_sw, "anschlusskanal": ak, "schaechte": schaechte_sw,
                          "routing": prot_sw, "l_gesamt": round(sum(h["laenge"] for h in haltungen_sw) + l_ak, 2),
                          "l_im_gebaeude": round(l_innen, 2)},
        "niederschlagswasser": {
            "a_e": a_e, "a_c": round(a_c, 2), "a_c_spitze": round(a_c_s, 2), "k_i": ki,
            "rigole": {"reihen": rig["reihen"], "b": rig["b"], "h": rig["h"], "l_erforderlich": round(rig["l_erf"], 3),
                       "l_gewaehlt": rig["l"], "elemente": rig["elemente"], "d_massgebend": rig["d_mass"],
                       "a_s": round(sp["a_s"], 2), "q_s": round(sp["q_s"], 4), "v_erf": round(sp["v_erf"], 3),
                       "v_vorh": round(sp["v_vorh"], 3), "v_brutto": round(rig["b"] * rig["h"] * rig["l"], 3),
                       "entleerung_h": round(sp["entleerung_h"], 2),
                       "lage": [round(v, 3) for v in rect.bounds], "orientierung": rig["orient"],
                       "zulauf": [round(zulauf[0], 3), round(zulauf[1], 3)],
                       "oberkante": round(rig_ok, 3), "sohle": round(rig_sohle, 3), "gok": round(gok_rig, 3),
                       "ueberdeckung": round(gok_rig - rig_ok, 3), "sickerraum": round(sickerraum, 3),
                       "abstand_gebaeude": round(abstand_geb_ist, 2), "abstand_gebaeude_erf": round(a_geb, 2),
                       "l_tabelle": [(dd, r, round(l, 3)) for dd, r, l in rig["l_tabelle"]]},
            "mulde_vergleich": {"a_s_hydraulisch": round(a_mulde_hyd, 2), "a_s_trengw": round(a_e / 15.0, 2),
                                "a_s": round(a_mulde, 2), "passt": m_rect is not None},
            "haltungen": haltungen_nw, "schaechte": schaechte_nw, "routing": prot_nw,
        },
        "pruefung": pr,
        "gebuehren": gebuehr,
        "_netze": {"sw": sw, "nw": nw, "rigole": rect, "mulde": m_rect, "gebaeude": gebaeude, "parzelle": parzelle},
    }


# -------------------------------------------------------------- Ausgabe -----

def export_json(e: dict) -> dict:
    return {k: v for k, v in e.items() if not k.startswith("_")}


def svg_lageplan(d: dict, e: dict) -> str:
    s, m = 20.0, 40.0
    xmin, xmax, ymin, ymax = -2.0, 22.0, -9.0, 31.0
    w, h = (xmax - xmin) * s + 2 * m, (ymax - ymin) * s + 2 * m + 60

    def pt(x, y):
        return (m + (x - xmin) * s, m + (ymax - y) * s)

    def poly(coords, **a):
        p = " ".join(f"{pt(x, y)[0]:.1f},{pt(x, y)[1]:.1f}" for x, y in coords)
        at = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
        return f'<polygon points="{p}" {at}/>'

    def line(p, q, **a):
        (x1, y1), (x2, y2) = pt(*p), pt(*q)
        at = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
        return f'<line x1="{x1:.1f}" y1="{y1:.1f}" x2="{x2:.1f}" y2="{y2:.1f}" {at}/>'

    def text(x, y, t, **a):
        px, py = pt(x, y)
        at = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
        return f'<text x="{px:.1f}" y="{py:.1f}" {at}>{t}</text>'

    N = e["_netze"]
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" font-family="sans-serif" font-size="10">',
         f'<rect width="{w:.0f}" height="{h:.0f}" fill="#ffffff"/>']
    o.append(poly([(xmin, 0), (xmax, 0), (xmax, -8), (xmin, -8)], fill="#e6e6e6", stroke="none"))
    o.append(text(xmin + 0.3, -1.0, f"Straße – Rückstauebene {d['strasse']['rueckstauebene']:.2f} m NHN", fill="#555"))
    ky = d["kanal"]["achse_y"]
    o.append(line((xmin, ky), (xmax, ky), stroke="#7a4b00", stroke_width="4", opacity="0.6"))
    o.append(text(xmax - 9, ky - 0.9, f"{d['kanal']['system']}kanal DN {d['kanal']['dn']}, Sohle {d['kanal']['sohle']:.2f}", fill="#7a4b00"))
    o.append(poly(d["grundstueck"]["polygon"], fill="none", stroke="#000", stroke_width="1.5", stroke_dasharray="6,3"))
    for f in d["flaechen"]:
        if "polygon" in f:
            o.append(poly(f["polygon"], fill="#f3e9c6", stroke="#b8a15a"))
            c = Polygon(f["polygon"]).centroid
            o.append(text(c.x - 1.5, c.y, f["id"], fill="#6b5a1e"))
    o.append(poly(d["gebaeude"]["polygon"], fill="#d9d9d9", stroke="#333", stroke_width="1.5"))
    gc = N["gebaeude"].centroid
    o.append(text(gc.x - 3.5, gc.y, f"EFH, FFB EG {d['gebaeude']['ffb_eg']:.2f}" + (" (Keller)" if d["gebaeude"]["keller"] else ""), fill="#333"))
    for b in d["hindernisse"]["baeume"]:
        cx, cy = pt(b["x"], b["y"])
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{b["kronenradius"] * s:.1f}" fill="#bfe3b4" stroke="#3a7d2c"/>')
        o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{(b["kronenradius"] + R(d, "baum_wurzelzuschlag")) * s:.1f}" fill="none" stroke="#3a7d2c" stroke-dasharray="3,3"/>')
        o.append(text(b["x"] - 0.4, b["y"] - 0.2, b["id"], fill="#3a7d2c"))
    for sp in d["hindernisse"]["sparten"]:
        o.append(line(sp["linie"][0], sp["linie"][1], stroke="#8a2be2", stroke_width="1.5", stroke_dasharray="8,3"))
        o.append(text(sp["linie"][1][0] + 0.2, sp["linie"][1][1] - 1.5, sp["id"], fill="#8a2be2", font_size="8"))
    rg = e["niederschlagswasser"]["rigole"]
    x0, y0, x1, y1 = rg["lage"]
    o.append(poly([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], fill="#cfe8ff", stroke="#1f5fa8", stroke_width="1.5"))
    rtxt = f"Rigole {rg['l_gewaehlt']:.1f} x {rg['b']:.1f} x {rg['h']:.2f} m, V = {rg['v_vorh']:.1f} m³"
    if rg["orientierung"] == "x":
        o.append(text(x0, y1 + 0.3, rtxt, fill="#1f5fa8"))
    else:                                   # längs beschriften (gedreht)
        tx, ty = pt(x0 - 0.25, y0 + 0.3)
        o.append(f'<text x="{tx:.1f}" y="{ty:.1f}" fill="#1f5fa8" transform="rotate(-90 {tx:.1f} {ty:.1f})">{rtxt}</text>')
    belegt: list[tuple[float, float, float, float]] = []

    def frei(x, y, t, groesse=0.55):
        """Beschriftungsposition ohne Überlappung (einfaches Verschieben nach unten)."""
        bw_, bh_ = len(t) * groesse * 0.55, groesse
        for _ in range(8):
            kasten = (x, y - bh_, x + bw_, y + 0.1)
            if not any(not (kasten[2] < b[0] or kasten[0] > b[2] or kasten[3] < b[1] or kasten[1] > b[3]) for b in belegt):
                belegt.append(kasten)
                return x, y
            y -= 0.7
        belegt.append((x, y - bh_, x + bw_, y + 0.1))
        return x, y
    for netz, farbe in ((N["sw"], "#8b4513"), (N["nw"], "#1f5fa8")):
        for u, v in netz.kanten():
            ka = netz._kante_attr[(u, v)]
            o.append(line(netz.xy(u), netz.xy(v), stroke=farbe, stroke_width="2.5" if ka["dn"] >= 150 else "1.8"))
        for k, a in netz.knoten.items():
            bw = a.get("bauwerk")
            cx, cy = pt(a["x"], a["y"])
            if bw in ("Schacht", "Revisionsschacht", "Filterschacht"):
                r = max(4.0, (a.get("dn_schacht") or 400) / 2000.0 * s)
                o.append(f'<circle cx="{cx:.1f}" cy="{cy:.1f}" r="{r:.1f}" fill="#fff" stroke="{farbe}" stroke-width="1.5"/>')
                lx, ly = frei(a["x"] + 0.5, a["y"] + 0.3, a["label"])
                o.append(text(lx, ly, a["label"], fill=farbe, font_weight="bold"))
            elif bw == "Reinigungsöffnung":
                o.append(f'<rect x="{cx - 3:.1f}" y="{cy - 3:.1f}" width="6" height="6" fill="{farbe}"/>')
                lx, ly = frei(a["x"] + 0.3, a["y"] + 0.3, a["label"], 0.45)
                o.append(text(lx, ly, a["label"], fill=farbe, font_size="8"))
    ein = d["kanal"]["einlass"]
    rs = N["sw"].knoten["SW-RS"]
    o.append(line((rs["x"], rs["y"]), (ein["x"], ein["y"]), stroke="#8b4513", stroke_width="2.5", stroke_dasharray="5,2"))
    ak = e["schmutzwasser"]["anschlusskanal"]
    o.append(text(ein["x"] + 0.3, -2.4, f"Anschlusskanal DN {ak['dn']}, {ak['gefaelle'] * 100:.0f} %", fill="#8b4513", font_size="9"))
    # Haltungsbeschriftung (SW)
    for hh in e["schmutzwasser"]["haltungen"]:
        a, b = N["sw"].xy(hh["_u"]), N["sw"].xy(hh["_v"])
        if hh["laenge"] >= 2.5:
            o.append(text((a[0] + b[0]) / 2 + 0.2, (a[1] + b[1]) / 2, f"DN {hh['dn']} {hh['gefaelle'] * 100:.2f} %", fill="#8b4513", font_size="8"))
    # Nordpfeil, Maßstab, Legende
    nx, ny = pt(20.8, 29.0)
    o.append(f'<path d="M {nx:.1f} {ny - 18:.1f} L {nx - 6:.1f} {ny:.1f} L {nx + 6:.1f} {ny:.1f} Z" fill="#000"/>')
    o.append(f'<text x="{nx - 4:.1f}" y="{ny + 12:.1f}">N</text>')
    sx, sy = pt(0, -8.6)
    o.append(f'<line x1="{sx:.1f}" y1="{sy:.1f}" x2="{sx + 5 * s:.1f}" y2="{sy:.1f}" stroke="#000" stroke-width="2"/>')
    o.append(f'<text x="{sx:.1f}" y="{sy - 4:.1f}">5 m</text>')
    ly = h - 45
    o.append(f'<text x="{m:.0f}" y="{ly:.0f}" font-weight="bold">B17 Lageplan – Szenario „{e["szenario"]}“ (Beispiel, kein Antragsplan)</text>')
    o.append(f'<text x="{m:.0f}" y="{ly + 14:.0f}" fill="#8b4513">■ Schmutzwasser (Revisionsschacht, Schächte, Reinigungsöffnungen)</text>')
    o.append(f'<text x="{m:.0f}" y="{ly + 28:.0f}" fill="#1f5fa8">■ Niederschlagswasser → Filterschacht → Rigole (Versickerung)</text>')
    o.append("</svg>")
    return "\n".join(o)


def svg_abwicklung(d: dict, e: dict) -> str:
    """Abwicklung des SW-Hauptstrangs (längste Quelle bis Kanal) in wahrer Länge (schematisch)."""
    sw = e["_netze"]["sw"]
    quellen = [k for k, a in sw.knoten.items() if a["typ"] == "quelle"]

    def strang(q):
        out = [q]
        while sw.nach[out[-1]] is not None:
            out.append(sw.nach[out[-1]])
        return out
    haupt = max((strang(q) for q in sorted(quellen)), key=lambda st: sum(sw.laenge(a, b) for a, b in zip(st, st[1:])))
    stat = [0.0]
    for a, b in zip(haupt, haupt[1:]):
        stat.append(stat[-1] + sw.laenge(a, b))
    ein = d["kanal"]["einlass"]
    rs = sw.knoten["SW-RS"]
    l_ak = math.dist((rs["x"], rs["y"]), (ein["x"], ein["y"]))
    xs = stat + [stat[-1] + l_ak]
    sohlen = [sw.knoten[k]["sohle"] for k in haupt] + [ein["sohle"]]
    goks = [sw.knoten[k]["gok"] for k in haupt] + [d["strasse"]["rueckstauebene"]]
    labels = [sw.knoten[k].get("label", k) for k in haupt] + ["Einlass"]
    zmin, zmax = min(sohlen + [d["kanal"]["sohle"]]) - 0.5, max(goks + [d["gebaeude"]["ffb_eg"]]) + 0.8
    sx, sz, m = 25.0, 100.0, 50.0
    w, h = xs[-1] * sx + 2 * m + 60, (zmax - zmin) * sz + 2 * m + 20

    def pt(x, z):
        return (m + x * sx, m + (zmax - z) * sz)
    o = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" font-family="sans-serif" font-size="9">',
         f'<rect width="{w:.0f}" height="{h:.0f}" fill="#fff"/>']

    def pl(xz, **a):
        at = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in a.items())
        return '<polyline points="' + " ".join(f"{pt(x, z)[0]:.1f},{pt(x, z)[1]:.1f}" for x, z in xz) + f'" fill="none" {at}/>'
    o.append(pl(list(zip(xs, goks)), stroke="#3a7d2c", stroke_width="1.5"))
    o.append(pl([(x, g - R(d, "frosttiefe_sw")) for x, g in zip(xs[:-1], goks[:-1])], stroke="#6fa8dc", stroke_dasharray="4,3"))
    o.append(pl(list(zip(xs, sohlen)), stroke="#8b4513", stroke_width="2.5"))
    rse = d["strasse"]["rueckstauebene"]
    o.append(pl([(0, rse), (xs[-1], rse)], stroke="#cc0000", stroke_dasharray="8,4"))
    x0, y0 = pt(0, rse)
    o.append(f'<text x="{x0 + 2:.1f}" y="{y0 - 3:.1f}" fill="#cc0000">Rückstauebene {rse:.2f}</text>')
    ffb = d["gebaeude"]["ffb_eg"]
    o.append(pl([(0, ffb), (xs[1], ffb)], stroke="#333", stroke_width="1.2"))
    x0, y0 = pt(0, ffb)
    o.append(f'<text x="{x0 + 2:.1f}" y="{y0 - 3:.1f}" fill="#333">FFB EG {ffb:.2f}</text>')
    for i, (x, zs, zg, lb) in enumerate(zip(xs, sohlen, goks, labels)):
        a, b = pt(x, zs), pt(x, zg)
        o.append(f'<line x1="{a[0]:.1f}" y1="{a[1]:.1f}" x2="{b[0]:.1f}" y2="{b[1]:.1f}" stroke="#999" stroke-width="0.8"/>')
        o.append(f'<text x="{a[0] + 2:.1f}" y="{a[1] + 11 + 11 * (i % 3):.1f}" fill="#8b4513">{lb} {zs:.2f}</text>')
    o.append(f'<text x="{m:.0f}" y="{h - 10:.0f}" font-weight="bold">B17 Abwicklung SW-Hauptstrang, Szenario „{e["szenario"]}“ '
             f'(Länge 1:{1000 / sx:.0f}, Höhe 1:{1000 / sz:.0f} überhöht; grün GOK, blau Frostgrenze 1,20 m)</text>')
    o.append("</svg>")
    return "\n".join(o)


def markdown(ergebnisse: list[dict]) -> str:
    z = ["# B17 – Grundstücksentwässerung: Ergebnisse (Beispielrechnung, keine Bemessung im Rechtssinn)", ""]
    for e in ergebnisse:
        n = e["niederschlagswasser"]
        rg = n["rigole"]
        z += [f"## Szenario `{e['szenario']}` – {e['beschreibung']}", "",
              "### Schmutzwasser-Haltungen", "",
              "| von | nach | Lage | DN | L [m] | Gefälle [%] | min [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] | Kreuzung |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for hh in e["schmutzwasser"]["haltungen"]:
            z.append(f"| {hh['von']} | {hh['nach']} | {hh['lage']} | {hh['dn']} | {hh['laenge']:.2f} | {hh['gefaelle'] * 100:.2f} | "
                     f"{hh['gefaelle_min'] * 100:.2f} | {hh['sohle_oben']:.3f} | {hh['sohle_unten']:.3f} | {hh['q']:.2f} | {hh['q_zul']:.2f} | "
                     f"{', '.join(hh['kreuzungen']) or '–'} |")
        ak = e["schmutzwasser"]["anschlusskanal"]
        z.append(f"| {ak['von']} | {ak['nach']} | Anschlusskanal | {ak['dn']} | {ak['laenge']:.2f} | {ak['gefaelle'] * 100:.2f} | "
                 f"{100 / ak['dn']:.2f} | {ak['sohle_oben']:.3f} | {ak['sohle_unten']:.3f} | – | {ak['q_zul']:.2f} | – |")
        z += ["", "### Schächte und Reinigungsöffnungen", "",
              "| Id | Bauwerk | Art | x | y | Deckel | Sohle | Tiefe | DN | Grund |", "|---|---|---|---|---|---|---|---|---|---|"]
        for s in e["schmutzwasser"]["schaechte"] + n["schaechte"]:
            z.append(f"| {s['id']} | {s['bauwerk']} | {s['art']} | {s['x']:.2f} | {s['y']:.2f} | {s['deckel']:.2f} | {s['sohle']:.2f} | "
                     f"{s['tiefe']:.2f} | {s['dn'] or '–'} | {s['grund']} |")
        z += ["", "### Niederschlagswasser-Haltungen", "",
              "| von | nach | DN | L [m] | Gefälle [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] |", "|---|---|---|---|---|---|---|---|---|"]
        for hh in n["haltungen"]:
            z.append(f"| {hh['von']} | {hh['nach']} | {hh['dn']} | {hh['laenge']:.2f} | {hh['gefaelle'] * 100:.2f} | {hh['sohle_oben']:.3f} | "
                     f"{hh['sohle_unten']:.3f} | {hh['q']:.2f} | {hh['q_zul']:.2f} |")
        z += ["", "### Rigole (DWA-A 138-1, einfaches Verfahren)", "",
              f"A_E,b = {n['a_e']:.1f} m², A_C = {n['a_c']:.1f} m² (C_m), k_i = {n['k_i']:.2e} m/s; "
              f"{rg['reihen']} Reihe(n), b = {rg['b']:.2f} m, h = {rg['h']:.2f} m, L_erf = {rg['l_erforderlich']:.2f} m → "
              f"L = {rg['l_gewaehlt']:.2f} m ({rg['elemente']} Elemente), D_maßg = {rg['d_massgebend']} min; "
              f"A_S,m = {rg['a_s']:.2f} m², Q_S = {rg['q_s']:.3f} l/s, V_erf = {rg['v_erf']:.2f} m³ ≤ V_vorh = {rg['v_vorh']:.2f} m³; "
              f"Entleerung {rg['entleerung_h']:.1f} h; OK {rg['oberkante']:.2f}, Sohle {rg['sohle']:.2f}, Sickerraum {rg['sickerraum']:.2f} m; "
              f"Abstand Gebäude {rg['abstand_gebaeude']:.2f} m (erf. {rg['abstand_gebaeude_erf']:.2f} m). "
              f"Vergleich Mulde: A_S ≥ {n['mulde_vergleich']['a_s']:.1f} m² ({'passt' if n['mulde_vergleich']['passt'] else 'passt nicht'}).", "",
              "### Regelprüfung", "", "| Id | Status | Regel | Quelle | Befund |", "|---|---|---|---|---|"]
        for p in e["pruefung"]:
            z.append(f"| {p['id']} | {p['status']} | {p['regel']} | {p['quelle']} | {p['text']} |")
        g = e["gebuehren"]
        z += ["", f"Niederschlagswassergebühr pauschal {g['nw_gebuehr_pauschal_eur_a']:.2f} EUR/a "
                  f"({g['grundstuecksflaeche']:.0f} m² × {g['gebietsabflussbeiwert']} × 1,77 EUR/m²); bei Vollversickerung 0 EUR/a (Antrag EAS § 8 Abs. 5).", ""]
    return "\n".join(z)


# ------------------------------------------------------------------ IFC -----

def erzeuge_ifc(d: dict, e: dict, pfad: Path) -> Path:
    """IFC4X3_ADD2 mit Systemen, Rohrsegmenten, Schächten, Filterschacht und Rigole (Einheit mm)."""
    from b14_fussbodenaufbau import IfcSchreiber
    w = IfcSchreiber(GUID_NAMENSRAUM, d["projekt"], pfad.name)
    f = w.f
    _, gs = w.grundgeruest([("EG", 0.0)])
    site = f.by_type("IfcSite")[0]
    gebaeude_ifc = f.by_type("IfcBuilding")[0]
    mm = 1000.0
    sz = e["szenario"]
    enthalten = []

    def plz(x, y, z):
        return w.platzierung(site.ObjectPlacement, (x * mm, y * mm, z * mm))

    # Gelände als IfcGeographicElement TERRAIN (Dreiecksnetz)
    par = d["grundstueck"]["polygon"]
    pts = f.createIfcCartesianPointList3D([[float(x * mm), float(y * mm), float(round(gok(d, x, y) * mm, 1))] for x, y in par])
    tfs = f.createIfcTriangulatedFaceSet(Coordinates=pts, CoordIndex=[[1, 2, 3], [1, 3, 4]])
    terr = w.root("IfcGeographicElement", f"/{sz}/gelaende", Name="Gelände (Ebene aus DGM, Beispiel)", PredefinedType="TERRAIN",
                  ObjectPlacement=w.platzierung(site.ObjectPlacement), Representation=w.form(w.body, "Tessellation", [tfs]))
    enthalten.append(terr)

    systeme = {}
    for art, enum, name in (("SW", "SEWAGE", "Schmutzwasser"), ("NW", "RAINWATER", "Niederschlagswasser")):
        systeme[art] = w.root("IfcDistributionSystem", f"/{sz}/system/{art}", Name=name, PredefinedType=enum)
        w.root("IfcRelServicesBuildings", f"/{sz}/system/{art}#gebaeude", RelatingSystem=systeme[art], RelatedBuildings=[gebaeude_ifc])
    mitglieder = {"SW": [], "NW": []}
    mat_pvc = w.material("pvc", "PVC-U (KG)", "Kunststoff")
    rohre = []

    def port(pfad_, el, name, richtung, sysenum, xyz):
        p = w.root("IfcDistributionPort", pfad_, Name=name, FlowDirection=richtung, PredefinedType="PIPE",
                   SystemType=sysenum, ObjectPlacement=plz(*xyz))
        return p

    def verbinde(pfad_, a, b):
        w.root("IfcRelConnectsPorts", pfad_, RelatingPort=a, RelatedPort=b)

    for art in ("SW", "NW"):
        netz = e["_netze"][art.lower()]
        sysenum = "SEWAGE" if art == "SW" else "RAINWATER"
        ein_ports: dict[str, list] = {}   # Knoten -> ankommende SOURCE-Ports
        aus_ports: dict[str, object] = {}  # Knoten -> abgehender SINK-Port der nächsten Kante
        for u, v in netz.kanten():
            a, b = netz.knoten[u], netz.knoten[v]
            ka = netz._kante_attr[(u, v)]
            p0 = (a["x"], a["y"], a["sohle"])
            dx, dy, dz = b["x"] - a["x"], b["y"] - a["y"], b["sohle"] - a["sohle"]
            l3 = math.sqrt(dx * dx + dy * dy + dz * dz)
            r_aussen = (ka["dn"] + 10) / 2.0 / 1000.0
            achse = (dx / l3, dy / l3, dz / l3)
            pfad_ = f"/{sz}/{art}/rohr/{u}->{v}"
            geo = w.zylinder(r_aussen * mm, l3 * mm, (0.0, 0.0, r_aussen * mm), achse)
            seg = w.root("IfcPipeSegment", pfad_, Name=f"{a.get('label', u)} → {b.get('label', v)}", PredefinedType="RIGIDSEGMENT",
                         ObjectPlacement=plz(*p0), Representation=w.form(w.body, "SweptSolid", [geo]))
            L2 = math.hypot(dx, dy)
            w.pset([seg], pfad_, "Pset_PipeSegmentTypeCommon", {
                "NominalDiameter": ("IfcPositiveLengthMeasure", float(ka["dn"])),
                "InnerDiameter": ("IfcPositiveLengthMeasure", INNENDURCHMESSER[ka["dn"]] * mm),
                "Length": ("IfcPositiveLengthMeasure", round(L2 * mm, 1))})
            w.pset([seg], pfad_, "Pset_PipeSegmentOccurrence", {
                "Gradient": ("IfcPositiveRatioMeasure", round(max(-dz / L2, 1e-6), 6)),
                "InvertElevation": ("IfcLengthMeasure", round(a["sohle"] * mm, 1))})
            w.pset([seg], pfad_, "B17_Entwaesserung", {"Lage": "Gebäude" if ka["innen"] else "Erdreich",
                                                       "Abfluss_l_s": round(ka["q"], 3), "Sohle_unten_m": round(b["sohle"], 3)})
            ps_in = port(pfad_ + "/zulauf", seg, "Zulauf", "SINK", sysenum, p0)
            ps_out = port(pfad_ + "/ablauf", seg, "Ablauf", "SOURCE", sysenum, (b["x"], b["y"], b["sohle"]))
            w.root("IfcRelNests", pfad_ + "#ports", RelatingObject=seg, RelatedObjects=[ps_in, ps_out])
            ein_ports.setdefault(v, []).append(ps_out)
            aus_ports[u] = ps_in
            rohre.append(seg)
            mitglieder[art].append(seg)
            enthalten.append(seg)
        # Knotenbauwerke
        for k in netz.topologisch():
            a = netz.knoten[k]
            ins = ein_ports.get(k, [])
            out = aus_ports.get(k)
            bw = a.get("bauwerk")
            pfad_ = f"/{sz}/{art}/knoten/{k}"
            el = None
            if bw in ("Schacht", "Revisionsschacht"):
                dn = a.get("dn_schacht") or 1000
                typ = "MANHOLE" if dn >= 1000 else "INSPECTIONCHAMBER"
                tiefe = a["gok"] - a["sohle"]
                geo = w.zylinder(dn / 2.0 + 60, (tiefe + 0.15) * mm, (0.0, 0.0, -150.0))
                el = w.root("IfcDistributionChamberElement", pfad_, Name=a["label"], PredefinedType=typ,
                            ObjectPlacement=plz(a["x"], a["y"], a["sohle"]), Representation=w.form(w.body, "SweptSolid", [geo]))
                if typ == "MANHOLE":
                    w.pset([el], pfad_, "Pset_DistributionChamberElementTypeManhole", {
                        "InvertLevel": ("IfcLengthMeasure", round(a["sohle"] * mm, 1)), "HasSteps": tiefe > 1.2,
                        "AccessLengthOrRadius": ("IfcPositiveLengthMeasure", 625.0 / 2.0), "IsShallow": tiefe <= 1.2,
                        "AccessCoverLoadRating": ("IfcText", "B 125 (Beispiel)")})
                else:
                    w.pset([el], pfad_, "Pset_DistributionChamberElementTypeInspectionChamber", {
                        "InspectionChamberInvertLevel": ("IfcLengthMeasure", round(a["sohle"] * mm, 1)),
                        "ChamberLengthOrRadius": ("IfcPositiveLengthMeasure", dn / 2.0),
                        "AccessCoverLoadRating": ("IfcText", "B 125 (Beispiel)")})
            elif bw == "Filterschacht":
                geo = w.zylinder(500.0, (a["gok"] - a["sohle"] + 0.3) * mm, (0.0, 0.0, -300.0))
                el = w.root("IfcInterceptor", pfad_, Name=a["label"], PredefinedType="USERDEFINED",
                            ObjectType="Filterschacht Niederschlagswasser (Vorreinigung)",
                            ObjectPlacement=plz(a["x"], a["y"], a["sohle"]), Representation=w.form(w.body, "SweptSolid", [geo]))
                w.pset([el], pfad_, "Pset_InterceptorTypeCommon", {"NominalBodyDepth": ("IfcPositiveLengthMeasure", round((a["gok"] - a["sohle"] + 0.3) * mm, 1))})
            elif (len(ins) >= 2) or (bw in ("Bogen", "Abzweig", "Reinigungsöffnung") and ins and out is not None):
                typ = "JUNCTION" if len(ins) >= 2 else "BEND"
                el = w.root("IfcPipeFitting", pfad_, Name=a.get("label", k), PredefinedType=typ, ObjectPlacement=plz(a["x"], a["y"], a["sohle"]))
            if el is not None:
                mitglieder[art].append(el)
                enthalten.append(el)
                kp = []
                for i, pin in enumerate(ins):
                    pe = port(pfad_ + f"/zulauf{i}", el, f"Zulauf {i + 1}", "SINK", sysenum, (a["x"], a["y"], a["sohle"]))
                    verbinde(pfad_ + f"/zulauf{i}#rel", pin, pe)
                    kp.append(pe)
                if out is not None or bw in ("Revisionsschacht", "Filterschacht"):
                    pa = port(pfad_ + "/ablauf", el, "Ablauf", "SOURCE", sysenum, (a["x"], a["y"], a["sohle"]))
                    kp.append(pa)
                    if out is not None:
                        verbinde(pfad_ + "/ablauf#rel", pa, out)
                    aus_ports[k] = pa
                if kp:
                    w.root("IfcRelNests", pfad_ + "#ports", RelatingObject=el, RelatedObjects=kp)
            elif out is not None:
                for i, pin in enumerate(ins):
                    verbinde(pfad_ + f"/direkt{i}#rel", pin, out)
        if art == "SW":
            # Anschlusskanal bis zum Einlassstück
            ein = d["kanal"]["einlass"]
            a = netz.knoten["SW-RS"]
            dx, dy, dz = ein["x"] - a["x"], ein["y"] - a["y"], ein["sohle"] - a["sohle"]
            l3 = math.sqrt(dx * dx + dy * dy + dz * dz)
            dn = d["kanal"]["dn_anschlusskanal"]
            pfad_ = f"/{sz}/SW/anschlusskanal"
            r_aussen = (dn + 10) / 2.0
            geo = w.zylinder(r_aussen, l3 * mm, (0.0, 0.0, r_aussen), (dx / l3, dy / l3, dz / l3))
            seg = w.root("IfcPipeSegment", pfad_, Name="Anschlusskanal SW-RS → Kanal", PredefinedType="RIGIDSEGMENT",
                         ObjectPlacement=plz(a["x"], a["y"], a["sohle"]), Representation=w.form(w.body, "SweptSolid", [geo]))
            w.pset([seg], pfad_, "Pset_PipeSegmentTypeCommon", {"NominalDiameter": ("IfcPositiveLengthMeasure", float(dn))})
            if dz < 0:
                w.pset([seg], pfad_, "Pset_PipeSegmentOccurrence", {"Gradient": ("IfcPositiveRatioMeasure", round(-dz / math.hypot(dx, dy), 6))})
            pin = port(pfad_ + "/zulauf", seg, "Zulauf", "SINK", "SEWAGE", (a["x"], a["y"], a["sohle"]))
            w.root("IfcRelNests", pfad_ + "#ports", RelatingObject=seg, RelatedObjects=[pin])
            verbinde(pfad_ + "#rel", aus_ports["SW-RS"], pin)
            mitglieder["SW"].append(seg)
            enthalten.append(seg)
            rohre.append(seg)
    # Rigole
    rg = e["niederschlagswasser"]["rigole"]
    x0, y0, x1, y1 = rg["lage"]
    geo = w.quader((x1 - x0) * mm, (y1 - y0) * mm, rg["h"] * mm)
    rig = w.root("IfcDistributionChamberElement", f"/{sz}/NW/rigole", Name="Rigole (Füllkörper)", PredefinedType="USERDEFINED",
                 ObjectType="Versickerungsrigole", ObjectPlacement=plz(x0, y0, rg["sohle"]),
                 Representation=w.form(w.body, "SweptSolid", [geo]))
    bo = d["boden"]
    w.pset([rig], f"/{sz}/NW/rigole", "B17_Versickerung", {
        "Bemessung": "DWA-A 138-1 (2024), einfaches Verfahren, T = 5 a (Beispielreihe)",
        "kf_m_s": float(bo["kf"]), "ki_m_s": float(e["niederschlagswasser"]["k_i"]), "Speicherkoeffizient": float(d["rigole"]["s_r"]),
        "V_erf_m3": rg["v_erf"], "V_vorh_m3": rg["v_vorh"], "A_C_m2": e["niederschlagswasser"]["a_c"],
        "MHGW_m": float(bo["mhgw"]), "Sickerraum_m": rg["sickerraum"], "Entleerung_h": rg["entleerung_h"]})
    pr = port(f"/{sz}/NW/rigole/zulauf", rig, "Zulauf", "SINK", "RAINWATER", (rg["zulauf"][0], rg["zulauf"][1], rg["oberkante"]))
    w.root("IfcRelNests", f"/{sz}/NW/rigole#ports", RelatingObject=rig, RelatedObjects=[pr])
    verbinde(f"/{sz}/NW/rigole#rel", aus_ports["NW-FS"], pr)
    mitglieder["NW"].append(rig)
    enthalten.append(rig)
    w.root("IfcRelAssociatesMaterial", f"/{sz}/material/pvc", RelatedObjects=rohre, RelatingMaterial=mat_pvc)
    for art in ("SW", "NW"):
        w.root("IfcRelAssignsToGroup", f"/{sz}/system/{art}#mitglieder", RelatedObjects=mitglieder[art], RelatingGroup=systeme[art])
    w.root("IfcRelContainedInSpatialStructure", f"/{sz}/grundstueck#enthaelt", RelatedElements=enthalten, RelatingStructure=site)
    return w.schreibe(pfad)


# ------------------------------------------------------------------ main ----

def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--szenario", default=None)
    ap.add_argument("--ifc", action="store_true", help="zusätzlich IFC4X3_ADD2 je Szenario schreiben")
    arg = ap.parse_args()
    basis = lade()
    ids = [arg.szenario] if arg.szenario else [s["id"] for s in basis["szenarien"]]
    AUSGABE.mkdir(exist_ok=True)
    ergebnisse = []
    kurz = {}
    for sid in ids:
        d = szenario_daten(basis, sid)
        e = berechne(d)
        ergebnisse.append(e)
        (AUSGABE / f"b17_{sid}.json").write_text(json.dumps(export_json(e), ensure_ascii=False, indent=1), encoding="utf-8")
        (AUSGABE / f"b17_{sid}_lageplan.svg").write_text(svg_lageplan(d, e), encoding="utf-8")
        (AUSGABE / f"b17_{sid}_abwicklung.svg").write_text(svg_abwicklung(d, e), encoding="utf-8")
        if arg.ifc:
            erzeuge_ifc(d, e, AUSGABE / f"b17_{sid}.ifc")
        rg = e["niederschlagswasser"]["rigole"]
        kurz[sid] = {"sw_laenge": e["schmutzwasser"]["l_gesamt"], "schaechte": len(e["schmutzwasser"]["schaechte"]),
                     "ak_gefaelle_pct": round(e["schmutzwasser"]["anschlusskanal"]["gefaelle"] * 100, 2),
                     "rigole_l": rg["l_gewaehlt"], "rigole_v": rg["v_vorh"], "sickerraum": rg["sickerraum"],
                     "befunde": {p["id"]: p["status"] for p in e["pruefung"] if p["status"] != "erfüllt"}}
    (AUSGABE / "b17_bericht.md").write_text(markdown(ergebnisse), encoding="utf-8")
    print(json.dumps(kurz, ensure_ascii=False, indent=1))


if __name__ == "__main__":
    main()

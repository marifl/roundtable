#!/usr/bin/env python3
"""
B18 – Baustellenlogistik und Montageplanung für ein Holzfertighaus:
Elementgewichte, Kranwahl, Kranstellplatz, LKW-Ladungen, Montagezeitplan,
Baustelleneinrichtungsplan (SVG) und Montageplan als IFC4X3_ADD2.

Eingabe:  daten/b18_baustelle.json, ausgabe/wandelement.ifc (aus B1)
Ausgabe:  ausgabe/b18_kranplanung.json, ausgabe/b18_be_plan_<szenario>.svg,
          ausgabe/b18_montage.ifc

Ablauf (deterministisch, keine Zufallszahlen):
  1. Flächengewicht der Außenwand aus B1: Volumen je Bauteil (Qto NetVolume,
     Schrauben als Zylinder) × MassDensity aus Pset_MaterialCommon.
     Decke und Dach aus Schichtaufbauten (dicke × Dichte × Holzanteil).
  2. Synthetisches Haus: 12 Wand-, 6 Decken-, 8 Dachelemente mit Maßen,
     Schwerpunkt im Grundriss und Oberkante (Hakenhöhe).
  3. Montagereihenfolge: EG-Wände → Decke → DG-Giebel → Dach
     (geschossweise, „Wände vor Decke vor Dach“).
  4. LKW-Ladungen: Wände/Giebel/Dach stehend im Innenlader, Decken liegend
     auf dem Plateau; Next-Fit in Montagereihenfolge (Just-in-time), Grenzen
     Nutzlast, Gestellbreite bzw. Stapelhöhe, § 32 StVZO / § 22 StVO.
  5. Rastersuche Stellplatz × Orientierung × Kran:
       harte Regeln  – Abstützfläche inkl. Unterlegplatten auf zulässiger
                       Stellfläche (Grundstück/Straße, nicht Nachbar, nicht
                       Abladezone, Abstand Baugrube nach DIN 4124, Baum-
                       und Schachtschutz);
                     – Heck-Schwenkradius ≥ 0,5 m von Haus und Baumkrone;
                     – jeder Hub: Radius im Bereich, Hakenhöhe, Auslastung
                       ≤ 80 % der (Beispiel-)Traglast inkl. Anschlagmittel
                       und Hakenflasche;
                     – Freileitung: Last, Ausleger, Heck halten den
                       Schutzabstand (2D, konservativ);
                     – Bodenpressung p = F_max / A_Platte ≤ p_zul.
       Ziel          – minimale Kosten (Beispiel-Tagessätze), dann wenige
                       Lasthübe über Nachbargrund, dann geringe Auslastung.
       Warnungen     – Überschwenken Nachbar (mit/ohne Last), Straße
                       (Sondernutzung, Haltverbot München), Wind bei großer
                       Windangriffsfläche (EN 13000: 1,2 m²/t), Freileitung
                       < 5 m (BaustellV Anh. II Nr. 4), Übermaß Transport.
  6. Zeitplan (Rüsten, Hübe, LKW-Ankunft) und IFC: IfcWorkSchedule, IfcTask
     INSTALLATION/MOVE mit IfcTaskTime und IfcRelSequence,
     IfcConstructionEquipmentResource (ERECTING/TRANSPORTING),
     IfcTransportElement LIFTINGGEAR (Kran), IfcVehicle VEHICLEWHEELED (LKW),
     IfcSpatialZone CONSTRUCTION/TRANSPORT/RESERVATION.

ALLE Kran-, Fahrzeug-, Kosten- und Zeitwerte sind BEISPIELWERTE. Die
Traglastkurven sind vereinfachte, gerundete Kurven und keine Herstellerdaten.
Das Ergebnis ersetzt keine Hubplanung mit Herstellersoftware und keinen
Einsatzplan des Kranunternehmers.

Aufruf:  python b18_kranplanung.py [--szenario basis|einfahrt_belegt] [--raster 0.5]
"""
from __future__ import annotations

import argparse
import copy
import datetime as dt
import json
import math
import uuid
from dataclasses import dataclass, field
from pathlib import Path

import numpy as np
import shapely
from shapely.geometry import LineString, Point, Polygon, box
from shapely.ops import unary_union
from shapely.prepared import prep

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b18_baustelle.json"
B1_IFC = HIER / "ausgabe" / "wandelement.ifc"
AUSGABE = HIER / "ausgabe"
G = 9.81  # m/s², Umrechnung t → kN

SZENARIEN = ("basis", "einfahrt_belegt")


# ---------------------------------------------------------------------------
# Hilfsfunktionen für Normwerte (Quellen: Recherche 19)
# ---------------------------------------------------------------------------

def schutzabstand_freileitung(kv: float | None) -> float:
    """Sicherheitsabstand zu Freileitungen nach DGUV Vorschrift 52 § 39
    bzw. DGUV Vorschrift 38 § 16 (Tabelle nach DIN VDE 0105)."""
    if kv is None:
        return 5.0            # unbekannte Nennspannung
    if kv <= 1.0:
        return 1.0
    if kv <= 110.0:
        return 3.0
    if kv <= 220.0:
        return 4.0
    return 5.0                # bis 380 kV


def abstand_baugrube(gesamtgewicht_t: float, bg: dict) -> tuple[float, bool]:
    """Abstand der Abstützung zur Böschungskante nach DIN 4124 (Wiedergabe
    BG BAU B 213): bis 12 t ≥ 1,00 m, über 12 t bis 40 t ≥ 2,00 m.
    Über 40 t fordert die Norm einen rechnerischen Nachweis – hier ein
    Beispielabstand und das Flag nachweis_noetig."""
    if gesamtgewicht_t <= 12.0:
        return bg["abstand_bis_12t_m"], False
    if gesamtgewicht_t <= 40.0:
        return bg["abstand_bis_40t_m"], False
    return bg["abstand_ueber_40t_m_annahme"], True


def bodenpressung(f_kn: float, flaeche_m2: float) -> float:
    """p = F / A in kN/m² (DGUV Information 208-059, Formel 4.3)."""
    return f_kn / flaeche_m2


def mindestflaeche(f_kn: float, p_zul: float) -> float:
    """A_erf = F_max / p_zul in m²."""
    return f_kn / p_zul


def wind_zulaessig(v_tab: float, masse_t: float, a_w_m2: float, ref_m2_je_t: float = 1.2) -> float:
    """Zulässige Windgeschwindigkeit (3-s-Böe in max. Hubhöhe) bei großer
    Windangriffsfläche nach Liebherr „Einfluss des Windes“ / FEM 5.016:
        v_max = v_max_TAB · sqrt(1,2 m²/t · m_H / A_W),  A_W = A_P · c_W.
    Ist das Ergebnis größer als v_max_TAB, gilt v_max_TAB."""
    if a_w_m2 <= 0:
        return v_tab
    return min(v_tab, v_tab * math.sqrt(ref_m2_je_t * masse_t / a_w_m2))


def traglast(kran: dict, r: np.ndarray | float) -> np.ndarray:
    """Beispiel-Traglast (t) als stückweise lineare Interpolation der
    Stützpunkte (Radius, Traglast); außerhalb [r_min, r_max] → 0."""
    tab = np.asarray(kran["traglast_t"], dtype=float)
    r = np.asarray(r, dtype=float)
    t = np.interp(r, tab[:, 0], tab[:, 1])
    return np.where((r < kran["r_min_m"]) | (r > tab[-1, 0]), 0.0, t)


def hakenhoehe_max(kran: dict, r: np.ndarray) -> np.ndarray:
    """Größte Hakenhöhe (m) beim Radius r. Autokran: Teleskop voll
    ausgefahren, Anlenkpunkt + sqrt(L² − r²) − 2 m (Rollenkopf/Flasche;
    vereinfachend, die Traglastkurve ist eine Hüllkurve über alle
    Auslegerlängen). Mobilbaukran: feste Hakenhöhe (Ausleger horizontal)."""
    r = np.asarray(r, dtype=float)
    if kran["typ"] == "mobilbaukran":
        return np.full_like(r, kran["hakenhoehe_fest_m"])
    L = kran["auslegerlaenge_max_m"]
    return kran["anlenkhoehe_m"] + np.sqrt(np.clip(L * L - r * r, 0.0, None)) - 2.0


# ---------------------------------------------------------------------------
# 1. Flächengewichte
# ---------------------------------------------------------------------------

def gewicht_aus_ifc(pfad: Path | str = B1_IFC, dichte_membran: float = 900.0) -> dict:
    """Masse des B1-Wandelements aus Volumen × Dichte je Material.
    Volumen: Qto_*BaseQuantities.NetVolume bzw. Qto_BodyGeometryValidation;
    Schrauben ohne Qto: Zylinder π/4·d²·l aus NominalDiameter/-Length.
    Dichte: Pset_MaterialCommon.MassDensity (fehlt sie, wie bei der
    Dampfbremse, gilt dichte_membran als Annahme)."""
    import ifcopenshell
    import ifcopenshell.util.element as ue

    f = ifcopenshell.open(str(pfad))
    wand = f.by_type("IfcWall")[0]
    qw = ue.get_psets(wand, qtos_only=True).get("Qto_WallBaseQuantities", {})
    je_material: dict[str, dict] = {}
    for teil in sorted(ue.get_decomposition(wand), key=lambda e: e.id()):
        if not teil.is_a("IfcElement") or teil.is_a("IfcFeatureElement"):
            continue
        mat = ue.get_material(teil)
        name = getattr(mat, "Name", None) or "ohne Material"
        rho = None
        if mat is not None:
            rho = ue.get_psets(mat).get("Pset_MaterialCommon", {}).get("MassDensity")
        if rho is None:
            rho = dichte_membran
        vol = None
        for q in ue.get_psets(teil, qtos_only=True).values():
            if "NetVolume" in q:
                vol = q["NetVolume"]
                break
        if vol is None and teil.is_a("IfcMechanicalFastener"):
            d, l = teil.NominalDiameter / 1000.0, teil.NominalLength / 1000.0   # mm → m
            vol = math.pi / 4 * d * d * l
        if vol is None:
            continue
        e = je_material.setdefault(name, {"anzahl": 0, "volumen_m3": 0.0, "dichte_kg_m3": float(rho), "masse_kg": 0.0})
        e["anzahl"] += 1
        e["volumen_m3"] += vol
        e["masse_kg"] += vol * rho
    masse = sum(e["masse_kg"] for e in je_material.values())
    brutto = qw.get("GrossSideArea") or (qw["Length"] * qw["Height"] / 1e6)
    for e in je_material.values():
        e["volumen_m3"] = round(e["volumen_m3"], 5)
        e["masse_kg"] = round(e["masse_kg"], 2)
    return {
        "datei": Path(pfad).name,
        "element": wand.Name,
        "laenge_m": qw["Length"] / 1000.0,
        "hoehe_m": qw["Height"] / 1000.0,
        "dicke_m": qw["Width"] / 1000.0,
        "bruttoflaeche_m2": brutto,
        "masse_kg": round(masse, 2),
        "flaechengewicht_kg_m2": round(masse / brutto, 3),
        "je_material": dict(sorted(je_material.items())),
    }


def flaechengewicht_aufbau(schichten: list[dict], dichten: dict) -> tuple[float, float]:
    """Flächengewicht (kg/m²) und Dicke (m) eines Schichtaufbaus. Schichten
    mit Anteil < 1 liegen im selben Gefach (Holz + Dämmung) und zählen
    für die Dicke nur einmal."""
    q = sum(s["dicke_mm"] / 1000.0 * dichten[s["material"]] * s["anteil"] for s in schichten)
    dicke, gefach = 0.0, 0.0
    for s in schichten:
        if s["anteil"] < 1.0:
            gefach = max(gefach, s["dicke_mm"])
        else:
            dicke += s["dicke_mm"]
    return q, (dicke + gefach) / 1000.0


# ---------------------------------------------------------------------------
# 2. Synthetisches Haus
# ---------------------------------------------------------------------------

@dataclass
class Element:
    id: str
    art: str                  # wand | decke | giebel | dach
    geschoss: str             # EG | DG
    laenge: float             # m, größte Abmessung in der Transportlage
    hoehe: float              # m, Höhe (Wand) bzw. Breite (Decke/Dach)
    dicke: float              # m
    flaeche: float            # m², Ansichtsfläche
    masse_t: float
    schwerpunkt: tuple[float, float]   # Grundriss (x, y)
    oberkante: float          # m über OK Keller
    unterkante: float
    neigung: float            # Hubneigung in Grad (0 = senkrecht hängend bei Wänden)
    reihenfolge: int = 0
    transport: str = ""
    lkw: int = 0
    hinweise: list[str] = field(default_factory=list)

    def windflaeche(self, h: dict) -> float:
        """Projizierte Windfläche A_P (m²) in ungünstiger Stellung:
        Wände/Giebel = Ansichtsfläche; Decken/Dach = Grundfläche × sin(Hubneigung)
        + Länge × Dicke (Annahme: Decke ~10° schief, Dach in Dachneigung)."""
        if self.art in ("wand", "giebel"):
            return self.flaeche
        return self.flaeche * math.sin(math.radians(self.neigung)) + self.laenge * self.dicke


def erzeuge_haus(d: dict, q_wand_b1: float, dicke_wand: float) -> list[Element]:
    """12 Wand-, 6 Decken- und 8 Dachelemente für ein 1,5-geschossiges
    Satteldachhaus (Beispiel). Außenwände: B1-Flächengewicht + Zuschläge."""
    h = d["haus"]
    x0, y0 = h["ursprung"]
    L, B, hw = h["laenge_x_m"], h["breite_y_m"], h["wandhoehe_eg_m"]
    zu = d["aufbauten"]["aussenwand_zuschlaege_kg_m2"]
    q_wand = q_wand_b1 + zu["putzsystem"] + h["fensteranteil_aussenwand"] * zu["fenster_je_m2_fensterflaeche"]
    q_decke, d_decke = flaechengewicht_aufbau(d["aufbauten"]["decke"], d["materialdichten_kg_m3"])
    q_dach, d_dach = flaechengewicht_aufbau(d["aufbauten"]["dach"], d["materialdichten_kg_m3"])
    alpha = h["dachneigung_grad"]
    z_dg = hw + d_decke
    firsthoehe = z_dg + B / 2 * math.tan(math.radians(alpha))
    el: list[Element] = []

    def wand(eid, a, b, geschoss="EG"):
        (xa, ya), (xb, yb) = a, b
        l = math.hypot(xb - xa, yb - ya)
        fl = l * hw
        el.append(Element(eid, "wand", geschoss, l, hw, dicke_wand, fl, fl * q_wand / 1000.0,
                          ((xa + xb) / 2, (ya + yb) / 2), hw, 0.0, 0.0))

    n_t, n_g = h["wandelemente_je_traufseite"], h["wandelemente_je_giebelseite"]
    # EG-Außenwände, gegen den Uhrzeigersinn ab Südwestecke
    for i in range(n_t):
        wand(f"W-S{i + 1}", (x0 + i * L / n_t, y0), (x0 + (i + 1) * L / n_t, y0))
    for i in range(n_g):
        wand(f"W-O{i + 1}", (x0 + L, y0 + i * B / n_g), (x0 + L, y0 + (i + 1) * B / n_g))
    for i in range(n_t):
        wand(f"W-N{i + 1}", (x0 + L - i * L / n_t, y0 + B), (x0 + L - (i + 1) * L / n_t, y0 + B))
    for i in range(n_g):
        wand(f"W-W{i + 1}", (x0, y0 + B - i * B / n_g), (x0, y0 + B - (i + 1) * B / n_g))
    # Decke: Streifen quer zum First (spannen über die Hausbreite)
    nd = h["deckenelemente"]
    for i in range(nd):
        b = L / nd
        fl = b * B
        el.append(Element(f"D-{i + 1}", "decke", "EG", B, b, d_decke, fl, fl * q_decke / 1000.0,
                          (x0 + (i + 0.5) * b, y0 + B / 2), hw + d_decke, hw,
                          d["hub"]["neigung_hub_decke_grad"]))
    # DG-Giebel: je Giebelseite zwei rechtwinklige Dreiecke (Hälfte bis First)
    hg = firsthoehe - z_dg
    for seite, x in (("W", x0), ("O", x0 + L)):
        for teil, (ya, yb) in (("S", (y0, y0 + B / 2)), ("N", (y0 + B / 2, y0 + B))):
            fl = 0.5 * (B / 2) * hg
            ys = yb - (B / 2) / 3 if teil == "S" else ya + (B / 2) / 3   # Schwerpunkt 1/3 vom First
            el.append(Element(f"G-{seite}{teil}", "giebel", "DG", B / 2, hg, dicke_wand, fl, fl * q_wand / 1000.0,
                              (x, ys), firsthoehe, z_dg, 0.0))
    # Dach: je Seite n Elemente, Sparrenlänge inkl. Überstand
    nr = h["dachelemente_je_seite"]
    ue_ = h["dachueberstand_m"]
    lh = B / 2 + ue_
    ls = lh / math.cos(math.radians(alpha))
    for seite, ym in (("S", y0 - ue_ + lh / 2), ("N", y0 + B + ue_ - lh / 2)):
        for i in range(nr):
            b = L / nr
            fl = b * ls
            el.append(Element(f"R-{seite}{i + 1}", "dach", "DG", ls, b, d_dach, fl, fl * q_dach / 1000.0,
                              (x0 + (i + 0.5) * b, ym), firsthoehe + d_dach, z_dg, alpha))
    return el


# ---------------------------------------------------------------------------
# 3. Montagereihenfolge
# ---------------------------------------------------------------------------

RANG = {("EG", "wand"): 0, ("EG", "decke"): 1, ("DG", "giebel"): 2, ("DG", "dach"): 3}


def montagereihenfolge(el: list[Element]) -> list[Element]:
    """Geschossweise: EG-Wände → Decke → DG-Giebel → Dach. Innerhalb einer
    Gruppe bleibt die Erzeugungsreihenfolge (umlaufend) erhalten."""
    idx = {e.id: i for i, e in enumerate(el)}
    out = sorted(el, key=lambda e: (RANG[(e.geschoss, e.art)], idx[e.id]))
    for n, e in enumerate(out, start=1):
        e.reihenfolge = n
    return out


def pruefe_reihenfolge(el: list[Element]) -> list[str]:
    """Regel „Wände vor Decke vor Dach“: liefert Verstöße (leer = in Ordnung)."""
    fehler = []
    for a in el:
        for b in el:
            if RANG[(a.geschoss, a.art)] < RANG[(b.geschoss, b.art)] and a.reihenfolge > b.reihenfolge:
                fehler.append(f"{a.id} ({a.art}) nach {b.id} ({b.art})")
    return fehler


# ---------------------------------------------------------------------------
# 4. LKW-Ladungen
# ---------------------------------------------------------------------------

def transportart(e: Element, fz: dict) -> tuple[str, list[str]]:
    """Wand/Giebel/Dach stehend im Innenlader, Decke liegend auf dem Plateau.
    Liefert Art und Hinweise zu Übermaßen (§ 32 StVZO, § 22 StVO)."""
    il, pl, gr = fz["innenlader"], fz["plateau"], fz["grenzen_stvzo"]
    hinweise: list[str] = []
    if e.art in ("wand", "giebel", "dach"):
        if e.hoehe <= il["ladehoehe_m"] and e.laenge <= il["ladelaenge_m"]:
            return "innenlader", hinweise
        hinweise.append("passt nicht stehend in den Innenlader")
    if e.hoehe <= gr["breite_m"] and e.laenge <= pl["ladelaenge_m"]:
        return "plateau", hinweise
    hinweise.append(f"Übermaß liegend: Breite {e.hoehe:.2f} m > {gr['breite_m']} m bzw. Länge > {pl['ladelaenge_m']} m "
                    "→ Erlaubnis § 29 Abs. 3 StVO, Ausnahmegenehmigung § 46 Abs. 1 Nr. 5 StVO / § 70 StVZO")
    return "plateau_uebermass", hinweise


def lkw_ladungen(el: list[Element], fz: dict) -> list[dict]:
    """Next-Fit in Montagereihenfolge: Ein LKW nimmt aufeinanderfolgende
    Elemente derselben Transportart auf, bis Nutzlast, Gestellbreite
    (Innenlader) oder Stapelhöhe (Plateau, 4,00 m − Ladeflächenhöhe) voll ist.
    Beladen wird in umgekehrter Montagereihenfolge (zuerst benötigtes
    Element oben bzw. außen)."""
    lkws: list[dict] = []
    akt = None
    for e in el:
        art, hinw = transportart(e, fz)
        e.transport, e.hinweise = art, e.hinweise + hinw
        basis = "plateau" if art.startswith("plateau") else "innenlader"
        v = fz[basis]
        if basis == "innenlader":
            belegung = e.dicke + v["abstand_m"]
            grenze = v["gestellbreite_m"]
        else:
            belegung = e.dicke + v["zwischenlage_m"]
            grenze = fz["grenzen_stvzo"]["hoehe_m"] - v["ladeflaechenhoehe_m"]
        if (akt is None or akt["art"] != basis or akt["masse_t"] + e.masse_t > v["nutzlast_t"]
                or akt["belegung_m"] + belegung > grenze + 1e-9):
            akt = {"nr": len(lkws) + 1, "art": basis, "fahrzeug": v["name"], "elemente": [], "masse_t": 0.0,
                   "belegung_m": 0.0, "grenze_m": grenze, "uebermass": False}
            lkws.append(akt)
        akt["elemente"].append(e.id)
        akt["masse_t"] += e.masse_t
        akt["belegung_m"] += belegung
        akt["uebermass"] |= art == "plateau_uebermass"
        e.lkw = akt["nr"]
    for k in lkws:
        k["masse_t"] = round(k["masse_t"], 3)
        k["belegung_m"] = round(k["belegung_m"], 3)
        k["beladereihenfolge"] = list(reversed(k["elemente"]))
    return lkws


# ---------------------------------------------------------------------------
# 5. Gelände, Aufstellung und Rastersuche
# ---------------------------------------------------------------------------

@dataclass
class Gelaende:
    grundstueck: Polygon
    strasse: Polygon
    nachbarn: list[tuple[str, Polygon]]
    nachbar_union: object
    haus: Polygon
    baugrube: Polygon
    baumzonen: list[Polygon]          # Wurzelbereich (Stellflächen-Sperre)
    baumkronen: list[Polygon]         # Kronen (Heck-Sperre)
    schachtzonen: list[Polygon]
    abladezone: Polygon
    aufnahmepunkt: tuple[float, float]
    leitung: LineString
    leitung_abstand: float
    leitung_kv: float
    bodenzonen: list[tuple[str, float, object]]
    sperren: list[Polygon]


def baue_gelaende(d: dict, szenario: str = "basis") -> Gelaende:
    g = d["gelaende"]
    h = d["haus"]
    x0, y0 = h["ursprung"]
    haus = box(x0, y0, x0 + h["laenge_x_m"], y0 + h["breite_y_m"])
    baumz, baumk, schacht = [], [], []
    for o in g["hindernisse"]:
        p = Point(o["mitte"])
        if o["art"] == "baum":
            baumk.append(p.buffer(o["kronenradius_m"], 64))
            baumz.append(p.buffer(o["kronenradius_m"] + o["wurzelzuschlag_m"], 64))
        elif o["art"] == "schacht":
            schacht.append(p.buffer(o["radius_m"] + o["abstand_m"], 64))
    fl = g["freileitung"]
    # Bodenzonen: spätere Zonen überschreiben frühere (z. B. Einfahrt im Grundstück)
    roh = [(z["id"], z["p_zul_kn_m2"], Polygon(z["polygon"])) for z in g["bodenzonen"]]
    zonen = []
    for i, (zid, p, poly) in enumerate(roh):
        spaeter = unary_union([q for _, _, q in roh[i + 1:]]) if i + 1 < len(roh) else None
        eff = poly.difference(spaeter) if spaeter is not None else poly
        zonen.append((zid, p, eff))
    sperren = [Polygon(p) for p in g.get("sperrflaechen_szenario", {}).get(szenario, [])]
    if szenario not in SZENARIEN:
        raise ValueError(szenario)
    return Gelaende(
        grundstueck=Polygon(g["grundstueck"]), strasse=Polygon(g["strasse"]["polygon"]),
        nachbarn=[(n["id"], Polygon(n["polygon"])) for n in g["nachbarn"]],
        nachbar_union=unary_union([Polygon(n["polygon"]) for n in g["nachbarn"]]),
        haus=haus, baugrube=Polygon(g["baugrube"]["kante"]), baumzonen=baumz, baumkronen=baumk,
        schachtzonen=schacht, abladezone=Polygon(d["abladezone"]["polygon"]),
        aufnahmepunkt=tuple(d["abladezone"]["aufnahmepunkt"]), leitung=LineString(fl["achse"]),
        leitung_abstand=schutzabstand_freileitung(fl["nennspannung_kv"]) + fl["zuschlag_ausschwingen_m"],
        leitung_kv=fl["nennspannung_kv"], bodenzonen=zonen, sperren=sperren)


def stellflaeche(ge: Gelaende, kran: dict, d: dict):
    """Zulässige Fläche für die Abstützung (inkl. Unterlegplatten) eines Krans:
    (Grundstück ∪ Straße) − Abladezone − Haus+0,5 m − Baugrube+Abstand(DIN 4124)
    − Baum-Wurzelbereich − Schächte − Szenario-Sperrflächen."""
    abst, _ = abstand_baugrube(kran["gesamtgewicht_t"], d["gelaende"]["baugrube"])
    frei = unary_union([ge.grundstueck, ge.strasse])
    weg = [ge.abladezone, ge.haus.buffer(0.5, join_style=2), ge.baugrube.buffer(abst, join_style=2),
           *ge.baumzonen, *ge.schachtzonen, *ge.sperren]
    return frei.difference(unary_union(weg))


def abstuetzung(x: float, y: float, kran: dict, ori: int, platte: float) -> tuple[Polygon, list[Polygon]]:
    """Rechteck der Abstützung (Stützenmitten ± halbe Platte) und die vier
    Unterlegplatten. abstuetzbasis_m = [Längs, Quer]; ori 0 = Längsachse in x."""
    a, b = kran["abstuetzbasis_m"]
    if ori == 90:
        a, b = b, a
    s = platte / 2
    pads = [box(x + sx * a / 2 - s, y + sy * b / 2 - s, x + sx * a / 2 + s, y + sy * b / 2 + s)
            for sx in (-1, 1) for sy in (-1, 1)]
    return box(x - a / 2 - s, y - b / 2 - s, x + a / 2 + s, y + b / 2 + s), pads


def p_zul_unter(pad: Polygon, ge: Gelaende) -> float:
    """Kleinste zulässige Bodenpressung aller Bodenzonen unter einer Platte."""
    werte = [p for _, p, z in ge.bodenzonen if z.intersection(pad).area > 1e-9]
    return min(werte) if werte else 0.0


def pfad_punkte(c: np.ndarray, p: np.ndarray, s: np.ndarray, n: int = 25) -> np.ndarray:
    """Hakenweg von Aufnahme p zu Absetzpunkt s um den Drehpunkt c: kürzeste
    Drehung, Radius linear über den Drehwinkel (Schwenken + Einziehen)."""
    r1, r2 = np.linalg.norm(p - c), np.linalg.norm(s - c)
    a1 = math.atan2(p[1] - c[1], p[0] - c[0])
    a2 = math.atan2(s[1] - c[1], s[0] - c[0])
    da = (a2 - a1 + math.pi) % (2 * math.pi) - math.pi
    t = np.linspace(0.0, 1.0, n)
    r = r1 + (r2 - r1) * t
    a = a1 + da * t
    return np.column_stack([c[0] + r * np.cos(a), c[1] + r * np.sin(a)])


@dataclass
class Hub:
    element: str
    last_t: float
    radius_aufnahme: float
    radius_absetzen: float
    traglast_t: float
    auslastung: float
    hakenhoehe_erf: float
    hakenhoehe_max: float
    wind_zul_ms: float
    ueber_nachbar_mit_last: bool = False


def bewerte_huebe(kran: dict, c: np.ndarray, el: list[Element], ge: Gelaende, h: dict) -> list[Hub]:
    p = np.asarray(ge.aufnahmepunkt, dtype=float)
    s = np.array([e.schwerpunkt for e in el], dtype=float)
    r_s = np.linalg.norm(s - c, axis=1)
    r_p = float(np.linalg.norm(p - c))
    r = np.maximum(r_s, r_p)
    last = np.array([e.masse_t for e in el]) + h["anschlagmittel_t"] + kran["hakenflasche_t"]
    tl = traglast(kran, r)
    # erforderliche Hakenhöhe: max(Oberkante Absetzen, LKW-Ladung) + Anschlaghöhe; geprüft bei beiden Radien
    h_erf = np.array([max(e.oberkante, 1.0 + e.hoehe) for e in el]) + h["hakenhoehe_zuschlag_m"]
    h_max = np.minimum(hakenhoehe_max(kran, r_s), hakenhoehe_max(kran, np.full_like(r_s, r_p)))
    out = []
    for i, e in enumerate(el):
        a_w = e.windflaeche(h) * h["wind_cw"]
        out.append(Hub(e.id, float(last[i]), round(r_p, 3), round(float(r_s[i]), 3), float(tl[i]),
                       float(last[i] / tl[i]) if tl[i] > 0 else math.inf, float(h_erf[i]), float(h_max[i]),
                       wind_zulaessig(h["wind_tabelle_ms"], float(last[i]), a_w, h["wind_referenz_m2_je_t"])))
    return out


@dataclass
class Kandidat:
    kran: str
    x: float
    y: float
    ori: int
    platte_m: float
    p_kn_m2: float
    p_zul_kn_m2: float
    auf_strasse: bool
    kosten_eur: float
    einsatztage: int
    max_auslastung: float
    lasthuebe_ueber_nachbar: int
    huebe: list[Hub]

    def schluessel(self):
        return (self.kosten_eur, self.lasthuebe_ueber_nachbar, int(self.auf_strasse),
                round(self.max_auslastung, 6), self.kran, self.x, self.y, self.ori)


def einsatzdauer_h(kran: dict, el: list[Element], h: dict) -> float:
    return kran["ruestzeit_h"] * 2 + sum(h["hubzeit_min"][e.art] for e in el) / 60.0   # Auf- und Abrüsten


def kosten(kran: dict, el: list[Element], d: dict, auf_strasse: bool, platte: float) -> tuple[float, int]:
    h, k = d["hub"], d["kosten"]
    tage = math.ceil(einsatzdauer_h(kran, el, h) / h["arbeitstag_stunden"] - 1e-9)
    eur = tage * kran["tagessatz_eur"] + kran["anfahrt_eur"]
    if auf_strasse:
        eur += k["strasse_sondernutzung_pauschale_eur"]
    if platte >= k["grosse_unterlegplatten_ab_m"]:
        eur += k["grosse_unterlegplatten_eur"]
    return float(eur), tage


def last_radius(e: Element) -> float:
    """Halbe größte Abmessung: Das hängende Element kann sich drehen."""
    return 0.5 * max(e.laenge, e.hoehe)


def freileitung_ok(kran: dict, c: np.ndarray, el: list[Element], ge: Gelaende) -> tuple[bool, float]:
    """2D-Prüfung Schutzabstand: Last (Hakenweg ± Lastradius), Ausleger
    (Drehpunkt → Haken; beim Mobilbaukran die volle feste Auslegerlänge über
    den überstrichenen Drehwinkel) und Heck. Liefert (ok, kleinster Abstand)."""
    d_req = ge.leitung_abstand
    d_c = ge.leitung.distance(Point(c))
    reichweite = kran.get("ausleger_fest_m") or max(
        max(np.linalg.norm(np.asarray(e.schwerpunkt) - c) for e in el),
        float(np.linalg.norm(np.asarray(ge.aufnahmepunkt) - c))) + max(last_radius(e) for e in el)
    if d_c - reichweite >= d_req:
        return True, round(d_c - reichweite, 3)                 # schnelle Vorprüfung
    p = np.asarray(ge.aufnahmepunkt, dtype=float)
    mins = [d_c - kran["heckradius_m"]]
    winkel = []
    for e in el:
        pts = pfad_punkte(c, p, np.asarray(e.schwerpunkt, dtype=float))
        dist_last = shapely.distance(shapely.points(pts), ge.leitung) - last_radius(e)
        mins.append(float(dist_last.min()))
        if kran["typ"] == "mobilbaukran":
            winkel.extend(np.degrees(np.arctan2(pts[:, 1] - c[1], pts[:, 0] - c[0])).tolist())
        else:
            segs = shapely.linestrings(np.stack([np.repeat(c[None, :], len(pts), 0), pts], axis=1))
            mins.append(float(shapely.distance(segs, ge.leitung).min()))
    if kran["typ"] == "mobilbaukran":
        L = kran["ausleger_fest_m"]
        grad = np.arange(math.floor(min(winkel)), math.ceil(max(winkel)) + 1, 1.0)
        spitzen = np.column_stack([c[0] + L * np.cos(np.radians(grad)), c[1] + L * np.sin(np.radians(grad))])
        segs = shapely.linestrings(np.stack([np.repeat(c[None, :], len(spitzen), 0), spitzen], axis=1))
        mins.append(float(shapely.distance(segs, ge.leitung).min()))
    m = min(mins)
    return m >= d_req, round(m, 3)


def lasthuebe_ueber_nachbar(c: np.ndarray, el: list[Element], ge: Gelaende) -> list[str]:
    p = np.asarray(ge.aufnahmepunkt, dtype=float)
    ids = []
    for e in el:
        pts = shapely.points(pfad_punkte(c, p, np.asarray(e.schwerpunkt, dtype=float)))
        if bool(np.any(shapely.dwithin(pts, ge.nachbar_union, last_radius(e)))):
            ids.append(e.id)
    return ids


def suche(d: dict, el: list[Element], ge: Gelaende, raster: float | None = None) -> dict:
    """Rastersuche über alle Krane, Stellplätze und Orientierungen."""
    h, su = d["hub"], d["suche"]
    raster = raster or su["raster_m"]
    x0, y0, x1, y1 = su["bbox"]
    xs = np.round(np.arange(x0, x1 + 1e-9, raster), 3)
    ys = np.round(np.arange(y0, y1 + 1e-9, raster), 3)
    platten = sorted(d["unterlegplatten_m"])
    hindernis_heck = unary_union([ge.haus.buffer(0.5), *[k.buffer(0.5) for k in ge.baumkronen]])
    stat: dict[str, dict] = {}
    beste: Kandidat | None = None
    alle_zulaessig: list[Kandidat] = []
    for kran in d["krane"]:
        st = stat.setdefault(kran["id"], {"gepruefte_stellungen": 0, "stellflaeche_ok": 0, "boden_ok": 0,
                                          "heck_ok": 0, "traglast_ok": 0, "freileitung_ok": 0, "zulaessig": 0,
                                          "beste_kosten_eur": None})
        flaeche = prep(stellflaeche(ge, kran, d))
        strasse = prep(ge.strasse)
        for x in xs:
            for y in ys:
                for ori in su["orientierungen_grad"]:
                    st["gepruefte_stellungen"] += 1
                    # kleinste Platte, deren Abstützrechteck auf der Stellfläche liegt und die Bodenpressung einhält
                    wahl = None
                    for pl in platten:
                        rect, pads = abstuetzung(float(x), float(y), kran, ori, pl)
                        if not flaeche.contains(rect):
                            break               # größere Platten passen erst recht nicht
                        if wahl is None:
                            st["stellflaeche_ok"] += 1
                            wahl = False
                        p_zul = min(p_zul_unter(pd, ge) for pd in pads)
                        p = bodenpressung(kran["stuetzkraft_max_kn"], pl * pl)
                        if p <= p_zul:
                            wahl = (pl, p, p_zul, rect)
                            break
                    if not wahl:
                        continue
                    st["boden_ok"] += 1
                    c = np.array([x, y], dtype=float)
                    if Point(c).buffer(kran["heckradius_m"], 32).intersects(hindernis_heck):
                        continue
                    st["heck_ok"] += 1
                    huebe = bewerte_huebe(kran, c, el, ge, h)
                    if any(u.auslastung > h["auslastung_max"] or u.hakenhoehe_erf > u.hakenhoehe_max for u in huebe):
                        continue
                    st["traglast_ok"] += 1
                    ok, _ = freileitung_ok(kran, c, el, ge)
                    if not ok:
                        continue
                    st["freileitung_ok"] += 1
                    pl, p, p_zul, rect = wahl
                    auf_str = strasse.intersects(rect)
                    eur, tage = kosten(kran, el, d, auf_str, pl)
                    ueber = lasthuebe_ueber_nachbar(c, el, ge)
                    for u in huebe:
                        u.ueber_nachbar_mit_last = u.element in ueber
                    k = Kandidat(kran["id"], float(x), float(y), ori, pl, round(p, 1), p_zul, auf_str, eur, tage,
                                 max(u.auslastung for u in huebe), len(ueber), huebe)
                    st["zulaessig"] += 1
                    if st["beste_kosten_eur"] is None or eur < st["beste_kosten_eur"]:
                        st["beste_kosten_eur"] = eur
                    alle_zulaessig.append(k)
                    if beste is None or k.schluessel() < beste.schluessel():
                        beste = k
    return {"beste": beste, "statistik": stat, "anzahl_zulaessig": len(alle_zulaessig),
            "je_kran_bester": {kid: min((k for k in alle_zulaessig if k.kran == kid), key=Kandidat.schluessel,
                                        default=None) for kid in stat}}


# ---------------------------------------------------------------------------
# 6. Warnungen, Zeitplan
# ---------------------------------------------------------------------------

def warnungen(d: dict, el: list[Element], lkws: list[dict], ge: Gelaende, best: Kandidat) -> list[dict]:
    kran = next(k for k in d["krane"] if k["id"] == best.kran)
    h = d["hub"]
    c = np.array([best.x, best.y])
    w: list[dict] = []

    def add(kat, text, quelle):
        w.append({"kategorie": kat, "text": text, "quelle": quelle})

    add("Straße", "Abladezone liegt auf öffentlichem Verkehrsgrund: vorübergehendes Haltverbot beim Mobilitätsreferat "
        "München (MOR-GB2.3) beantragen; Bearbeitung ca. 10 Arbeitstage; Schilder mind. 3 volle Kalendertage vor "
        "Gültigkeit aufstellen, Vornotierungsliste führen.",
        "stadt.muenchen.de Temporäre Anordnungen; Antrag HV Umzug/Baustelle")
    if best.auf_strasse:
        add("Straße", "Kranabstützung auf öffentlichem Grund: Sondernutzungserlaubnis + verkehrsrechtliche Anordnung "
            "(§ 45 StVO) mit Verkehrszeichenplan und MVAS-verantwortlicher Person; Autokran im Antrag angeben.",
            "Mobilitätsreferat München, Antrag Baustelle privat")
    if best.lasthuebe_ueber_nachbar:
        ids = [u.element for u in best.huebe if u.ueber_nachbar_mit_last]
        add("Nachbar", f"{len(ids)} Hübe führen Last über Nachbargrund ({', '.join(ids)}): Anzeige nach Art. 46b Abs. 3 "
            "BayAGBGB mind. 1 Monat vorher; bei Ablehnung Duldungsklage, keine Selbsthilfe.",
            "OLG München, Urt. v. 15.10.2020 – 8 U 5531/20")
    heck = Point(c).buffer(kran["heckradius_m"], 64)
    ueber_heck = [nid for nid, poly in ge.nachbarn if heck.intersection(poly).area > 1e-6]
    ausleger = []
    p = np.asarray(ge.aufnahmepunkt, dtype=float)
    for e in el:
        pts = pfad_punkte(c, p, np.asarray(e.schwerpunkt, dtype=float))
        if kran["typ"] == "mobilbaukran":
            L = kran["ausleger_fest_m"]
            a = np.arctan2(pts[:, 1] - c[1], pts[:, 0] - c[0])
            pts = np.column_stack([c[0] + L * np.cos(a), c[1] + L * np.sin(a)])
        segs = shapely.linestrings(np.stack([np.repeat(c[None, :], len(pts), 0), pts], axis=1))
        if bool(np.any(shapely.intersects(segs, ge.nachbar_union))):
            ausleger.append(e.id)
    if ueber_heck or ausleger:
        add("Nachbar", f"Überschwenken ohne Last: Heck über {', '.join(ueber_heck) or '–'}; Ausleger bei "
            f"{len(ausleger)} Hüben über Nachbargrund. Auch lastfreies Überschwenken fällt unter Art. 46b BayAGBGB.",
            "OLG München 8 U 5531/20; LG München II 13 O 3296/20 (Duldung lastfrei in 17 m Höhe, Einzelfall)")
    krit = [u for u in best.huebe if u.wind_zul_ms < h["wind_plan_boe_ms"]]
    if krit:
        vmin = min(u.wind_zul_ms for u in best.huebe)
        add("Wind", f"{len(krit)} Hübe mit A_W > 1,2 m²/t: zulässige Böe unter {h['wind_plan_boe_ms']} m/s "
            f"(min. {vmin:.1f} m/s). Hubplanung mit Windrechner des Herstellers, Windmesser am Kran.",
            "EN 13000 (1,2 m²/t); Liebherr „Einfluss des Windes“; FEM 5.016")
    _, d_min = freileitung_ok(kran, c, el, ge)
    if ge.leitung_kv > 1.0:
        add("Freileitung", f"Kleinster Abstand Last/Ausleger zur {ge.leitung_kv:.0f}-kV-Leitung {d_min:.1f} m "
            f"(gefordert {ge.leitung_abstand:.1f} m inkl. Zuschlag); Netzbetreiber informieren."
            + (" < 5 m: besonders gefährliche Arbeit (BaustellV Anh. II Nr. 4) → SiGe-Plan." if d_min < 5.0 else ""),
            "DGUV Vorschrift 52 § 39; BaustellV Anhang II")
    abst, nachweis = abstand_baugrube(kran["gesamtgewicht_t"], d["gelaende"]["baugrube"])
    if nachweis:
        add("Baugrube", f"Kran > 40 t: Abstand zur Böschung ({abst} m angesetzt) nur mit rechnerischem Nachweis.",
            "DIN 4124 (über BG BAU B 213)")
    add("Boden", f"Bodenpressung {best.p_kn_m2:.0f} kN/m² ≤ {best.p_zul_kn_m2:.0f} kN/m² mit Platte "
        f"{best.platte_m:.1f} × {best.platte_m:.1f} m, gerechnet mit F_max = {kran['stuetzkraft_max_kn']:.0f} kN. "
        "Tragfähigkeit nur aus Tabellenwerten geschätzt; bei Zweifel Baugrund prüfen lassen.",
        "DGUV Information 208-059 Abschn. 4; Liebherr „Untergrund für sichere Kraneinsätze“")
    for k in lkws:
        if k["uebermass"]:
            add("Transport", f"LKW {k['nr']}: Übermaß → Erlaubnis § 29 Abs. 3 StVO / Ausnahme § 70 StVZO.",
                "§ 22 Abs. 2 StVO, § 32 StVZO")
    if any(e.oberkante > 7.0 for e in el):
        add("SiGe", "Absturzhöhe > 7 m möglich (BaustellV Anh. II Nr. 1) → SiGe-Plan bei mehreren Arbeitgebern.",
            "BaustellV § 2 Abs. 3, Anhang II")
    add("SiGe", "Aufbau von Bauelementen mit Kran: ob vorgefertigte Holzelemente „Massivbauelemente“ im Sinne von "
        "BaustellV Anh. II Nr. 10 sind, ist ungeklärt [U] – im Zweifel SiGe-Plan.", "BaustellV Anhang II Nr. 10")
    add("Daten", "Alle Kran-, Fahrzeug- und Kostenwerte sind Beispielwerte; Freigabe nur mit Herstellersoftware "
        "(z. B. LICCON-Einsatzplaner, Crane Planner 2.0) und Einsatzplan des Kranunternehmers.", "–")
    return w


def zeitplan(d: dict, el: list[Element], lkws: list[dict], kran: dict) -> dict:
    """Sequentieller Tagesplan: Rüsten, Hübe in Montagereihenfolge, Abrüsten.
    LKW k kommt lkw_puffer_min vor dem ersten Hub seiner Ladung."""
    h = d["hub"]
    tag0 = dt.datetime.fromisoformat(f"{d['projekt']['montagedatum']}T{h['arbeitstag_beginn']}:00")
    tag_min = int(round(h["arbeitstag_stunden"] * 60))
    t = 0   # Arbeitsminuten seit Beginn Tag 1

    def uhr(arbeitsmin: int) -> dt.datetime:
        tag, rest = divmod(arbeitsmin, tag_min)
        return tag0 + dt.timedelta(days=tag, minutes=rest)

    def block(dauer: int) -> tuple[int, int]:
        nonlocal t
        tag_rest = tag_min - (t % tag_min)
        if dauer > tag_rest:            # nicht über Feierabend hinaus: auf nächsten Tag
            t += tag_rest
        a = t
        t += dauer
        return a, t

    ruest = int(round(kran["ruestzeit_h"] * 60))
    vorgaenge = [{"id": "RUESTEN", "art": "Kran aufrüsten", "start": block(ruest)}]
    for e in el:
        vorgaenge.append({"id": e.id, "art": f"Montage {e.art}", "start": block(h["hubzeit_min"][e.art]),
                          "lkw": e.lkw})
    vorgaenge.append({"id": "ABRUESTEN", "art": "Kran abrüsten", "start": block(ruest)})
    out = []
    for v in vorgaenge:
        a, b = v["start"]
        out.append({"id": v["id"], "art": v["art"], "beginn": uhr(a).isoformat(), "ende": uhr(b).isoformat(),
                    "dauer_min": b - a, **({"lkw": v["lkw"]} if "lkw" in v else {})})
    ankunft = []
    for k in lkws:
        erster = next(v for v in out if v["id"] == k["elemente"][0])
        letzter = next(v for v in out if v["id"] == k["elemente"][-1])
        an = dt.datetime.fromisoformat(erster["beginn"]) - dt.timedelta(minutes=h["lkw_puffer_min"])
        ab = dt.datetime.fromisoformat(letzter["ende"])
        ankunft.append({"lkw": k["nr"], "ankunft": an.isoformat(), "abfahrt": ab.isoformat(),
                        "standzeit_min": int((ab - an).total_seconds() // 60),
                        "abfahrt_werk": (an - dt.timedelta(minutes=h["lkw_fahrzeit_min"])).isoformat()})
    tage = sorted({v["beginn"][:10] for v in out})
    return {"vorgaenge": out, "lkw": ankunft, "montagetage": len(tage), "tage": tage,
            "einsatzstunden": round(einsatzdauer_h(kran, el, h), 2)}


# ---------------------------------------------------------------------------
# 7. SVG-Baustelleneinrichtungsplan
# ---------------------------------------------------------------------------

def _poly_svg(poly, stil: str, T) -> str:
    teile = []
    geoms = getattr(poly, "geoms", [poly])
    for g in geoms:
        if g.is_empty:
            continue
        pts = " ".join(f"{T(x, y)[0]:.1f},{T(x, y)[1]:.1f}" for x, y in g.exterior.coords)
        teile.append(f'<polygon points="{pts}" {stil}/>')
    return "".join(teile)


def svg_be_plan(d: dict, el: list[Element], ge: Gelaende, best: Kandidat, szenario: str) -> str:
    kran = next(k for k in d["krane"] if k["id"] == best.kran)
    x0, y0, x1, y1 = -14.0, -12.0, 36.0, 38.0
    m = 14.0                      # px je m
    W, H = (x1 - x0) * m, (y1 - y0) * m + 120

    def T(x, y):
        return (x - x0) * m, (y1 - y) * m

    c = (best.x, best.y)
    s = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{W:.0f}" height="{H:.0f}" viewBox="0 0 {W:.0f} {H:.0f}" '
         f'font-family="sans-serif" font-size="11">', '<rect width="100%" height="100%" fill="#ffffff"/>']
    for nid, poly in ge.nachbarn:
        s.append(_poly_svg(poly, 'fill="#eeeeee" stroke="#999999"', T))
        cx, cy = T(*poly.representative_point().coords[0])
        s.append(f'<text x="{cx:.1f}" y="{cy:.1f}" fill="#777777">Nachbar {nid}</text>')
    s.append(_poly_svg(ge.strasse, 'fill="#d9d9d9" stroke="#888888"', T))
    s.append(_poly_svg(ge.grundstueck, 'fill="#f4f9ec" stroke="#2e7d32" stroke-width="2"', T))
    for z in ge.sperren:
        s.append(_poly_svg(z, 'fill="#ffe0b2" stroke="#e65100" stroke-dasharray="4 3"', T))
    s.append(_poly_svg(ge.baugrube, 'fill="none" stroke="#795548" stroke-dasharray="6 3"', T))
    s.append(_poly_svg(ge.haus, 'fill="#c8a27a" stroke="#5d4037" stroke-width="2"', T))
    for bz in ge.baumzonen:
        s.append(_poly_svg(bz, 'fill="#a5d6a7" fill-opacity="0.5" stroke="#2e7d32" stroke-dasharray="3 2"', T))
    for sz in ge.schachtzonen:
        s.append(_poly_svg(sz, 'fill="#90a4ae" stroke="#455a64"', T))
    s.append(_poly_svg(ge.leitung.buffer(ge.leitung_abstand), 'fill="#ef9a9a" fill-opacity="0.35" stroke="none"', T))
    (lx0, ly0), (lx1, ly1) = T(*ge.leitung.coords[0]), T(*ge.leitung.coords[-1])
    s.append(f'<line x1="{lx0:.1f}" y1="{ly0:.1f}" x2="{lx1:.1f}" y2="{ly1:.1f}" stroke="#c62828" stroke-width="2"/>')
    s.append(_poly_svg(ge.abladezone, 'fill="#bbdefb" stroke="#1565c0" stroke-width="1.5"', T))
    ax, ay = T(*ge.aufnahmepunkt)
    s.append(f'<circle cx="{ax:.1f}" cy="{ay:.1f}" r="3" fill="#1565c0"/>')
    # Lastwege
    cc = np.array(c)
    p = np.asarray(ge.aufnahmepunkt, dtype=float)
    for e, u in zip(el, best.huebe):
        pts = pfad_punkte(cc, p, np.asarray(e.schwerpunkt, dtype=float), 13)
        farbe = "#d32f2f" if u.ueber_nachbar_mit_last else "#6a1b9a"
        s.append('<polyline fill="none" stroke="' + farbe + '" stroke-width="0.8" stroke-opacity="0.7" points="'
                 + " ".join(f"{T(*q)[0]:.1f},{T(*q)[1]:.1f}" for q in pts) + '"/>')
        ex, ey = T(*e.schwerpunkt)
        s.append(f'<circle cx="{ex:.1f}" cy="{ey:.1f}" r="2" fill="{farbe}"/>')
    # Kran
    rect, pads = abstuetzung(best.x, best.y, kran, best.ori, best.platte_m)
    s.append(_poly_svg(rect, 'fill="#fff59d" fill-opacity="0.7" stroke="#f9a825" stroke-width="1.5"', T))
    for pd in pads:
        s.append(_poly_svg(pd, 'fill="#f57f17" stroke="#e65100"', T))
    kx, ky = T(*c)
    r_max = max(max(u.radius_absetzen, u.radius_aufnahme) for u in best.huebe)
    s.append(f'<circle cx="{kx:.1f}" cy="{ky:.1f}" r="{kran["heckradius_m"] * m:.1f}" fill="none" stroke="#f57f17" '
             'stroke-dasharray="2 2"/>')
    s.append(f'<circle cx="{kx:.1f}" cy="{ky:.1f}" r="{r_max * m:.1f}" fill="none" stroke="#6a1b9a" '
             'stroke-dasharray="8 4"/>')
    if kran["typ"] == "mobilbaukran":
        s.append(f'<circle cx="{kx:.1f}" cy="{ky:.1f}" r="{kran["ausleger_fest_m"] * m:.1f}" fill="none" '
                 'stroke="#ff6f00" stroke-dasharray="1 3"/>')
    s.append(f'<circle cx="{kx:.1f}" cy="{ky:.1f}" r="4" fill="#000000"/>')
    s.append(f'<text x="{kx + 6:.1f}" y="{ky - 6:.1f}" font-weight="bold">{best.kran}</text>')
    # Nordpfeil, Maßstab
    s.append(f'<path d="M {W - 30:.0f} 50 l 8 20 l -8 -6 l -8 6 z" fill="#000"/><text x="{W - 34:.0f}" y="44">N</text>')
    s.append(f'<line x1="20" y1="{(y1 - y0) * m - 16:.0f}" x2="{20 + 10 * m:.0f}" y2="{(y1 - y0) * m - 16:.0f}" '
             f'stroke="#000" stroke-width="3"/><text x="20" y="{(y1 - y0) * m - 22:.0f}">10 m</text>')
    # Legende
    ly = (y1 - y0) * m + 18
    u_krit = max(best.huebe, key=lambda u: u.auslastung)
    zeilen = [
        f"BE-Plan B18 (Beispiel, Szenario „{szenario}“): {kran['name']} bei ({best.x:.1f} | {best.y:.1f}), "
        f"Orientierung {best.ori}°, Unterlegplatten {best.platte_m:.1f} m, p = {best.p_kn_m2:.0f} ≤ {best.p_zul_kn_m2:.0f} kN/m²",
        f"Max. Auslastung {best.max_auslastung * 100:.1f} % (kritischer Hub {u_krit.element}, r = "
        f"{max(u_krit.radius_absetzen, u_krit.radius_aufnahme):.1f} m); Kosten {best.kosten_eur:.0f} € (Beispielsätze), "
        f"{best.einsatztage} Einsatztag(e)",
        "gelb/orange: Abstützung und Platten · gestrichelt orange: Heckradius · violett: Lastwege und max. Arbeitsradius · "
        "rot: Lastweg über Nachbar",
        "blau: Abladezone LKW · rot schraffiert: Schutzstreifen Freileitung · grün: Baum-Wurzelbereich · braun gestrichelt: "
        "Böschungskante",
    ]
    for i, z in enumerate(zeilen):
        s.append(f'<text x="10" y="{ly + i * 16:.0f}">{z}</text>')
    s.append("</svg>")
    return "\n".join(s) + "\n"


# ---------------------------------------------------------------------------
# 8. IFC4X3_ADD2: Montageplan
# ---------------------------------------------------------------------------

class IfcSchreiber:
    """Kleiner deterministischer IFC-Schreiber: GlobalId = uuid5(Namensraum, Pfad)."""

    def __init__(self, projekt: dict):
        import ifcopenshell
        import ifcopenshell.guid
        self.ios = ifcopenshell
        self.f = ifcopenshell.file(schema="IFC4X3_ADD2")
        self.ns = uuid.UUID(projekt["guid_namensraum"])
        self.pj = projekt
        self._pfade: set[str] = set()

    def root(self, klasse: str, pfad: str, **attr):
        if pfad in self._pfade:
            raise ValueError(f"Pfad doppelt: {pfad}")
        self._pfade.add(pfad)
        return self.f.create_entity(klasse, GlobalId=self.ios.guid.compress(uuid.uuid5(self.ns, pfad).hex), **attr)

    def platz(self, rel, x=0.0, y=0.0, z=0.0):
        pt = self.f.createIfcCartesianPoint([float(round(x, 3)), float(round(y, 3)), float(round(z, 3))])
        return self.f.createIfcLocalPlacement(rel, self.f.createIfcAxis2Placement3D(pt, None, None))

    def wert(self, v):
        if isinstance(v, tuple):
            return self.f.create_entity(v[0], v[1])
        if isinstance(v, bool):
            return self.f.create_entity("IfcBoolean", v)
        if isinstance(v, int):
            return self.f.create_entity("IfcInteger", v)
        if isinstance(v, float):
            return self.f.create_entity("IfcReal", v)
        return self.f.create_entity("IfcLabel", str(v))

    def pset(self, obj, pfad: str, name: str, werte: dict):
        props = [self.f.createIfcPropertySingleValue(k, None, self.wert(v), None) for k, v in werte.items()]
        ps = self.root("IfcPropertySet", f"{pfad}#{name}", Name=name, HasProperties=props)
        self.root("IfcRelDefinesByProperties", f"{pfad}#{name}#rel", RelatedObjects=[obj], RelatingPropertyDefinition=ps)

    def qto(self, obj, pfad: str, name: str, werte: dict):
        typ = {"Length": ("IfcQuantityLength", "LengthValue"), "Width": ("IfcQuantityLength", "LengthValue"),
               "Height": ("IfcQuantityLength", "LengthValue"), "Depth": ("IfcQuantityLength", "LengthValue"),
               "GrossArea": ("IfcQuantityArea", "AreaValue"), "GrossSideArea": ("IfcQuantityArea", "AreaValue"),
               "GrossWeight": ("IfcQuantityWeight", "WeightValue")}
        qs = [self.f.create_entity(typ[k][0], Name=k, **{typ[k][1]: float(v)}) for k, v in werte.items()]
        q = self.root("IfcElementQuantity", f"{pfad}#{name}", Name=name, Quantities=qs)
        self.root("IfcRelDefinesByProperties", f"{pfad}#{name}#rel", RelatedObjects=[obj], RelatingPropertyDefinition=q)

    def flaeche(self, kontext, poly: Polygon, hoehe: float = 0.1):
        pts = [self.f.createIfcCartesianPoint([float(round(x, 3)), float(round(y, 3))]) for x, y in poly.exterior.coords]
        prof = self.f.createIfcArbitraryClosedProfileDef("AREA", None, self.f.createIfcPolyline(pts))
        solid = self.f.createIfcExtrudedAreaSolid(prof, self.f.createIfcAxis2Placement3D(
            self.f.createIfcCartesianPoint([0.0, 0.0, 0.0]), None, None),
            self.f.createIfcDirection([0.0, 0.0, 1.0]), float(hoehe))
        rep = self.f.createIfcShapeRepresentation(kontext, "Body", "SweptSolid", [solid])
        return self.f.createIfcProductDefinitionShape(None, None, [rep])

    def schreibe(self, pfad: Path):
        h = self.f.header
        h.file_description.description = ("ViewDefinition [NotAssigned]",)
        h.file_name.name = pfad.name
        h.file_name.time_stamp = self.pj["zeitstempel"]
        h.file_name.author = (self.pj["autor"],)
        h.file_name.organization = (self.pj["organisation"],)
        h.file_name.preprocessor_version = f"IfcOpenShell {self.ios.version}"
        h.file_name.originating_system = "B18 Kranplanung (Beispiel)"
        h.file_name.authorization = "none"
        self.f.write(str(pfad))


def erzeuge_ifc(d: dict, el: list[Element], lkws: list[dict], ge: Gelaende, best: Kandidat, plan: dict):
    import ifcopenshell.api.context
    import ifcopenshell.api.unit
    w = IfcSchreiber(d["projekt"])
    f = w.f
    kran = next(k for k in d["krane"] if k["id"] == best.kran)
    projekt = w.root("IfcProject", "/projekt", Name=d["projekt"]["name"])
    einheiten = [ifcopenshell.api.unit.add_si_unit(f, unit_type=u) for u in
                 ("LENGTHUNIT", "AREAUNIT", "VOLUMEUNIT", "PLANEANGLEUNIT", "TIMEUNIT")]
    einheiten.append(ifcopenshell.api.unit.add_si_unit(f, unit_type="MASSUNIT", prefix="KILO"))
    projekt.UnitsInContext = f.createIfcUnitAssignment(einheiten)
    modell = ifcopenshell.api.context.add_context(f, context_type="Model")
    body = ifcopenshell.api.context.add_context(f, context_type="Model", context_identifier="Body",
                                                target_view="MODEL_VIEW", parent=modell)
    site = w.root("IfcSite", "/site", Name="Baugrundstück (Beispiel)", ObjectPlacement=w.platz(None))
    geb = w.root("IfcBuilding", "/gebaeude", Name=d["projekt"]["gebaeude"], ObjectPlacement=w.platz(site.ObjectPlacement))
    w.root("IfcRelAggregates", "/projekt#agg", RelatingObject=projekt, RelatedObjects=[site])
    w.root("IfcRelAggregates", "/site#agg", RelatingObject=site, RelatedObjects=[geb])
    gs = {}
    for name, z in (("EG", 0.0), ("DG", el[0].oberkante + next(e.dicke for e in el if e.art == "decke"))):
        gs[name] = w.root("IfcBuildingStorey", f"/gebaeude/{name}", Name=name, Elevation=float(round(z, 3)),
                          ObjectPlacement=w.platz(geb.ObjectPlacement, 0, 0, z))
    w.root("IfcRelAggregates", "/gebaeude#agg", RelatingObject=geb, RelatedObjects=list(gs.values()))

    # Bauelemente (ohne Geometrie; Platzierung im Schwerpunkt, Gewicht als Qto)
    produkte, je_geschoss = {}, {"EG": [], "DG": []}
    for e in el:
        pf = f"/element/{e.id}"
        pl = w.platz(gs[e.geschoss].ObjectPlacement, e.schwerpunkt[0], e.schwerpunkt[1], 0.0)
        if e.art in ("wand", "giebel"):
            obj = w.root("IfcWall", pf, Name=e.id, ObjectPlacement=pl, PredefinedType="ELEMENTEDWALL", Tag=e.id)
            w.qto(obj, pf, "Qto_WallBaseQuantities", {"Length": e.laenge, "Height": e.hoehe, "Width": e.dicke,
                                                      "GrossSideArea": e.flaeche, "GrossWeight": e.masse_t * 1000})
        else:
            obj = w.root("IfcSlab", pf, Name=e.id, ObjectPlacement=pl, Tag=e.id,
                         PredefinedType="FLOOR" if e.art == "decke" else "ROOF")
            w.qto(obj, pf, "Qto_SlabBaseQuantities", {"Length": e.laenge, "Width": e.hoehe, "Depth": e.dicke,
                                                      "GrossArea": e.flaeche, "GrossWeight": e.masse_t * 1000})
        w.pset(obj, pf, "HRB_Montage", {"Montagenummer": e.reihenfolge, "Transportart": e.transport,
                                        "LKW": e.lkw, "Hubgewicht_kg": round((e.masse_t + d["hub"]["anschlagmittel_t"]) * 1000, 1)})
        produkte[e.id] = obj
        je_geschoss[e.geschoss].append(obj)
    for g, objs in je_geschoss.items():
        w.root("IfcRelContainedInSpatialStructure", f"/gebaeude/{g}#enthaelt", RelatingStructure=gs[g], RelatedElements=objs)

    # Baustellenflächen als IfcSpatialZone
    rect, _ = abstuetzung(best.x, best.y, kran, best.ori, best.platte_m)
    r_max = max(max(u.radius_absetzen, u.radius_aufnahme) for u in best.huebe)
    zonen = [("Kranstellfläche", "CONSTRUCTION", rect), ("Abladezone LKW", "TRANSPORT", ge.abladezone),
             ("Schwenkbereich Last (max. Arbeitsradius)", "RESERVATION", Point(best.x, best.y).buffer(r_max, 32))]
    zobj = []
    for i, (name, typ, poly) in enumerate(zonen):
        z = w.root("IfcSpatialZone", f"/zone/{i}", Name=name, PredefinedType=typ, ObjectPlacement=w.platz(site.ObjectPlacement),
                   Representation=w.flaeche(body, poly))
        minx, miny, maxx, maxy = poly.bounds
        w.qto(z, f"/zone/{i}", "Qto_SpatialZoneBaseQuantities", {"Length": maxx - minx, "Width": maxy - miny, "Height": 0.1})
        zobj.append(z)
    w.root("IfcRelReferencedInSpatialStructure", "/site#zonen", RelatingStructure=site, RelatedElements=zobj)

    # Kran und LKW als Produkte, zugeordnet zu Ressourcen
    k_obj = w.root("IfcTransportElement", "/kran", Name=kran["name"], PredefinedType="LIFTINGGEAR",
                   ObjectPlacement=w.platz(site.ObjectPlacement, best.x, best.y, 0.0))
    w.pset(k_obj, "/kran", "Pset_TransportElementCommon",
           {"Reference": kran["id"], "CapacityWeight": ("IfcMassMeasure", float(max(t for _, t in kran["traglast_t"]) * 1000))})
    w.pset(k_obj, "/kran", "HRB_Kranaufstellung", {"Stuetzkraft_max_kN": float(kran["stuetzkraft_max_kn"]),
                                                   "Unterlegplatte_m": best.platte_m, "Bodenpressung_kN_m2": best.p_kn_m2,
                                                   "Bodenpressung_zul_kN_m2": best.p_zul_kn_m2, "Orientierung_Grad": best.ori,
                                                   "Beispieldaten": True})
    fahrzeuge = []
    for k in lkws:
        v = d["fahrzeuge"][k["art"]]
        o = w.root("IfcVehicle", f"/lkw/{k['nr']}", Name=f"LKW {k['nr']} – {v['name']}", PredefinedType="VEHICLEWHEELED",
                   ObjectPlacement=w.platz(site.ObjectPlacement, *ge.aufnahmepunkt, 0.0))
        w.qto(o, f"/lkw/{k['nr']}", "Qto_VehicleBaseQuantities", {"Length": v["laenge_m"], "Width": v["breite_m"],
                                                                   "Height": v["hoehe_m"]})
        fahrzeuge.append(o)
    w.root("IfcRelContainedInSpatialStructure", "/site#enthaelt", RelatingStructure=site,
           RelatedElements=[k_obj, *fahrzeuge])
    r_kran = w.root("IfcConstructionEquipmentResource", "/res/kran", Name=f"Kran {kran['id']}", PredefinedType="ERECTING")
    w.root("IfcRelAssignsToResource", "/res/kran#produkt", RelatingResource=r_kran, RelatedObjects=[k_obj])
    r_lkw = w.root("IfcConstructionEquipmentResource", "/res/lkw", Name="LKW-Transporte", PredefinedType="TRANSPORTING")
    w.root("IfcRelAssignsToResource", "/res/lkw#produkte", RelatingResource=r_lkw, RelatedObjects=fahrzeuge)

    # Arbeitsplan
    beginn = plan["vorgaenge"][0]["beginn"]
    ws = w.root("IfcWorkSchedule", "/plan", Name="Montageplan (Beispiel)", PredefinedType="PLANNED",
                CreationDate=d["projekt"]["zeitstempel"], StartTime=beginn)
    haupt = w.root("IfcTask", "/plan/montage", Name="Montage Holzfertighaus", IsMilestone=False, PredefinedType="CONSTRUCTION",
                   TaskTime=f.createIfcTaskTime(DurationType="WORKTIME", ScheduleStart=beginn,
                                                ScheduleFinish=plan["vorgaenge"][-1]["ende"]))
    w.root("IfcRelAssignsToControl", "/plan#task", RelatingControl=ws, RelatedObjects=[haupt])
    w.root("IfcRelAssignsToProcess", "/plan/montage#kran", RelatingProcess=haupt, RelatedObjects=[r_kran])

    def dauer(minuten: int) -> str:
        return f"PT{minuten // 60}H{minuten % 60}M"

    kinder, vorher = [], None
    hubs = {u.element: u for u in best.huebe}
    for v in plan["vorgaenge"]:
        typ = "INSTALLATION" if v["id"] in produkte else "CONSTRUCTION"
        t = w.root("IfcTask", f"/plan/task/{v['id']}", Name=v["art"] + ("" if typ != "INSTALLATION" else f" {v['id']}"),
                   Identification=v["id"], IsMilestone=False, PredefinedType=typ,
                   TaskTime=f.createIfcTaskTime(DurationType="WORKTIME", ScheduleDuration=dauer(v["dauer_min"]),
                                                ScheduleStart=v["beginn"], ScheduleFinish=v["ende"]))
        if v["id"] in produkte:
            w.root("IfcRelAssignsToProduct", f"/plan/task/{v['id']}#produkt", RelatingProduct=produkte[v["id"]],
                   RelatedObjects=[t])
            u = hubs[v["id"]]
            w.pset(t, f"/plan/task/{v['id']}", "HRB_Kranhub", {
                "Hublast_kg": round(u.last_t * 1000, 1), "Radius_Aufnahme_m": u.radius_aufnahme,
                "Radius_Absetzen_m": u.radius_absetzen, "Traglast_Beispiel_kg": round(u.traglast_t * 1000, 1),
                "Auslastung": round(u.auslastung, 4), "Wind_zul_ms": round(u.wind_zul_ms, 2),
                "LastUeberNachbar": u.ueber_nachbar_mit_last})
        if vorher is not None:
            w.root("IfcRelSequence", f"/plan/seq/{v['id']}", RelatingProcess=vorher, RelatedProcess=t,
                   SequenceType="FINISH_START")
        kinder.append(t)
        vorher = t
    # Anlieferungen (MOVE) je LKW, Nachfolger = erster Hub der Ladung
    task_by_id = {k.Identification: k for k in kinder}
    for a, k in zip(plan["lkw"], lkws):
        t = w.root("IfcTask", f"/plan/lkw/{k['nr']}", Name=f"Anlieferung LKW {k['nr']}", Identification=f"LKW{k['nr']}",
                   IsMilestone=False, PredefinedType="MOVE",
                   TaskTime=f.createIfcTaskTime(DurationType="ELAPSEDTIME", ScheduleStart=a["abfahrt_werk"],
                                                ScheduleFinish=a["abfahrt"]))
        w.pset(t, f"/plan/lkw/{k['nr']}", "Pset_PackingInstructions",
               {"SpecialInstructions": ("IfcText", f"{d['fahrzeuge'][k['art']]['name']}; Beladereihenfolge "
                                        + ", ".join(k["beladereihenfolge"]))})
        w.root("IfcRelAssignsToProcess", f"/plan/lkw/{k['nr']}#res", RelatingProcess=t, RelatedObjects=[r_lkw])
        w.root("IfcRelSequence", f"/plan/lkw/{k['nr']}#seq", RelatingProcess=t, RelatedProcess=task_by_id[k["elemente"][0]],
               SequenceType="FINISH_START")
        kinder.append(t)
    w.root("IfcRelNests", "/plan/montage#nest", RelatingObject=haupt, RelatedObjects=kinder)
    return w


# ---------------------------------------------------------------------------
# Gesamtablauf
# ---------------------------------------------------------------------------

def lade_eingabe(pfad: Path | str = STANDARD_EINGABE) -> dict:
    return json.loads(Path(pfad).read_text(encoding="utf-8"))


def b1_gewicht() -> dict:
    if not B1_IFC.exists():             # B1 bei Bedarf erzeugen
        import b1_wandelement
        b1_wandelement.schreibe_ifc(json.loads((HIER / "daten" / "wandelement.json").read_text(encoding="utf-8")))
    return gewicht_aus_ifc(B1_IFC, lade_eingabe()["materialdichten_kg_m3"]["dampfbremse"])


def plane(d: dict, szenario: str = "basis", raster: float | None = None, b1: dict | None = None) -> dict:
    b1 = b1 or b1_gewicht()
    el = montagereihenfolge(erzeuge_haus(d, b1["flaechengewicht_kg_m2"], b1["dicke_m"]))
    lkws = lkw_ladungen(el, d["fahrzeuge"])
    ge = baue_gelaende(d, szenario)
    erg = suche(d, el, ge, raster)
    best: Kandidat = erg["beste"]
    res = {"szenario": szenario, "b1": b1, "elemente": el, "lkws": lkws, "gelaende": ge, "suche": erg, "beste": best}
    if best is None:
        res["warnungen"] = [{"kategorie": "Kran", "text": "Kein zulässiger Kran/Stellplatz gefunden.", "quelle": "–"}]
        return res
    kran = next(k for k in d["krane"] if k["id"] == best.kran)
    res["warnungen"] = warnungen(d, el, lkws, ge, best)
    res["zeitplan"] = zeitplan(d, el, lkws, kran)
    return res


def bericht(d: dict, res: dict) -> dict:
    best: Kandidat = res["beste"]
    el: list[Element] = res["elemente"]
    q_decke, d_decke = flaechengewicht_aufbau(d["aufbauten"]["decke"], d["materialdichten_kg_m3"])
    q_dach, d_dach = flaechengewicht_aufbau(d["aufbauten"]["dach"], d["materialdichten_kg_m3"])
    out = {
        "szenario": res["szenario"],
        "hinweis": "Beispielrechnung; Kran-, Fahrzeug- und Kostenwerte fiktiv.",
        "flaechengewichte_kg_m2": {"aussenwand_b1_roh": res["b1"]["flaechengewicht_kg_m2"],
                                   "decke": round(q_decke, 2), "dach": round(q_dach, 2)},
        "b1": res["b1"],
        "elemente": [{"id": e.id, "art": e.art, "geschoss": e.geschoss, "reihenfolge": e.reihenfolge,
                      "masse_t": round(e.masse_t, 3), "laenge_m": round(e.laenge, 3), "hoehe_breite_m": round(e.hoehe, 3),
                      "dicke_m": round(e.dicke, 3), "flaeche_m2": round(e.flaeche, 3),
                      "schwerpunkt": [round(e.schwerpunkt[0], 3), round(e.schwerpunkt[1], 3)],
                      "oberkante_m": round(e.oberkante, 3), "transport": e.transport, "lkw": e.lkw,
                      "hinweise": e.hinweise} for e in el],
        "summe_masse_t": round(sum(e.masse_t for e in el), 3),
        "reihenfolge_verstoesse": pruefe_reihenfolge(el),
        "lkw": res["lkws"],
        "statistik_suche": res["suche"]["statistik"],
        "anzahl_zulaessige_stellungen": res["suche"]["anzahl_zulaessig"],
        "je_kran_bester": {kid: (None if k is None else {"x": k.x, "y": k.y, "ori": k.ori, "kosten_eur": k.kosten_eur,
                                                          "max_auslastung": round(k.max_auslastung, 4),
                                                          "auf_strasse": k.auf_strasse,
                                                          "lasthuebe_ueber_nachbar": k.lasthuebe_ueber_nachbar})
                           for kid, k in res["suche"]["je_kran_bester"].items()},
        "warnungen": res["warnungen"],
    }
    if best is not None:
        krit = max(best.huebe, key=lambda u: u.auslastung)
        out["gewaehlt"] = {"kran": best.kran, "x": best.x, "y": best.y, "orientierung_grad": best.ori,
                           "unterlegplatte_m": best.platte_m, "bodenpressung_kn_m2": best.p_kn_m2,
                           "bodenpressung_zul_kn_m2": best.p_zul_kn_m2, "auf_strasse": best.auf_strasse,
                           "kosten_eur": best.kosten_eur, "einsatztage": best.einsatztage,
                           "max_auslastung": round(best.max_auslastung, 4), "kritischer_hub": krit.element,
                           "lasthuebe_ueber_nachbar": best.lasthuebe_ueber_nachbar,
                           "min_wind_zul_ms": round(min(u.wind_zul_ms for u in best.huebe), 2)}
        out["huebe"] = [{"element": u.element, "last_t": round(u.last_t, 3), "r_aufnahme_m": u.radius_aufnahme,
                         "r_absetzen_m": u.radius_absetzen, "traglast_t": round(u.traglast_t, 3),
                         "auslastung": round(u.auslastung, 4), "hakenhoehe_erf_m": round(u.hakenhoehe_erf, 2),
                         "hakenhoehe_max_m": round(u.hakenhoehe_max, 2), "wind_zul_ms": round(u.wind_zul_ms, 2),
                         "last_ueber_nachbar": u.ueber_nachbar_mit_last} for u in best.huebe]
        out["zeitplan"] = res["zeitplan"]
    return out


def main(argv=None) -> dict:
    ap = argparse.ArgumentParser(description=__doc__.splitlines()[1])
    ap.add_argument("--szenario", choices=SZENARIEN, default=None, help="nur ein Szenario rechnen")
    ap.add_argument("--raster", type=float, default=None)
    a = ap.parse_args(argv)
    d = lade_eingabe()
    AUSGABE.mkdir(exist_ok=True)
    b1 = b1_gewicht()
    gesamt = {}
    for sz in ([a.szenario] if a.szenario else list(SZENARIEN)):
        res = plane(copy.deepcopy(d), sz, a.raster, b1)
        gesamt[sz] = bericht(d, res)
        if res["beste"] is not None:
            (AUSGABE / f"b18_be_plan_{sz}.svg").write_text(
                svg_be_plan(d, res["elemente"], res["gelaende"], res["beste"], sz), encoding="utf-8")
            if sz == "basis":
                erzeuge_ifc(d, res["elemente"], res["lkws"], res["gelaende"], res["beste"], res["zeitplan"]).schreibe(
                    AUSGABE / "b18_montage.ifc")
    (AUSGABE / "b18_kranplanung.json").write_text(json.dumps(gesamt, ensure_ascii=False, indent=1), encoding="utf-8")
    kurz = {sz: g.get("gewaehlt") for sz, g in gesamt.items()}
    print(json.dumps(kurz, ensure_ascii=False, indent=1))
    return gesamt


if __name__ == "__main__":
    main()

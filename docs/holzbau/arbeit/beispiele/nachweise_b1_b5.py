#!/usr/bin/env python3
"""
Nachrüstung (Retrofit) der Beispiele B1–B5 mit dem Nachweis-Framework
(`nachweis.py`), ohne die Rechenkerne oder ihre Ergebnisse zu ändern.

Prinzip: Die Nachweisschicht liegt ÜBER den bestehenden Rechenkernen.
Jeder Nachweis rechnet die maßgebende Formelkette aus den offen gelegten
Eingangsgrößen selbst nach (einheitengeprüft) und vergleicht das Ergebnis
mit dem Rechenkern („Gegenrechnung“). Algorithmische Schritte ohne
geschlossene Formel (Polygonverschneidung, vollständige Aufzählung,
IDS-Prüfung) werden als Verfahrensschritt mit Werkzeug und Version
dokumentiert und ihr Ergebnis vom Rechenkern übernommen.

Ausgabe: ausgabe/nachweise/
  b1_wandelement.{json,md,html}       Mengen- und Massennachweis
  b2_ids_bestanden.{json,md,html}     IDS: 11 Nachweise, Fall „bestanden“
  b2_ids_fehlerhaft.{json,md,html}    IDS: 11 Nachweise, Fall „fehlerhaft“
  b3_uwert.{json,md,html}             U-Wert nach DIN EN ISO 6946, 4 Varianten
  b4_abstandsflaechen.{json,md,html}  Abstandsflächen, 4 Szenarien
  b5_treppe.{json,md,html}            Treppe DIN 18065
  gesamt.{json,md,html}               Nachweisheft B1–B5
  svg/*.svg                           alle Grafiken als Einzeldateien

Aufruf:   python nachweise_b1_b5.py
"""
from __future__ import annotations

import hashlib
import json
import math
import tempfile
from pathlib import Path

import ifcopenshell
from shapely.geometry import Polygon, box

import b1_wandelement as b1
import b2_ids_pruefung as b2
import b3_uwert_iso6946 as b3
import b4_abstandsflaechen as b4
import b5_treppe_din18065 as b5
from nachweis import (FARBE, Gegenstand, Grafik, Groesse as G, Kriterium, Nachweis, Nachweisheft, Regel, Rundung,
                      Schritt, SvgZeichnung, balken_anteil_svg, diagramm_balken, diagramm_ist_grenzwert,
                      diagramm_punkte, lageplan_svg, schnitt_svg, treppenschnitt_svg, zahl_de, zahl_roh)

HIER = Path(__file__).resolve().parent
AUSGABE = HIER / "ausgabe" / "nachweise"
PROFILVERSION = "0.1.0"
KEINE_RECHTSAUSKUNFT = ("Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, "
                        "kein geprüfter bautechnischer Nachweis.")


def sha_datei(p: Path) -> str:
    return hashlib.sha256(Path(p).read_bytes()).hexdigest()


def rel(p: Path) -> str:
    return str(Path(p).resolve().relative_to(HIER))


def projekt_angaben() -> dict:
    p = b1.lade_parameter()["projekt"]
    return {"Projekt": p["name"], "Gebäude": p["gebaeude"], "Geschoss": p["geschoss"],
            "Parametermodell": f"daten/wandelement.json (SHA-256 {sha_datei(b1.STANDARD_PARAMETER)[:16]}…)",
            "Grundstück": f"daten/grundstueck.json (SHA-256 {sha_datei(b4.STANDARD_PARAMETER)[:16]}…)",
            "Rechtsstand der Beispiele": "27.09.2026", "Hinweis": KEINE_RECHTSAUSKUNFT}


class Modell:
    """Erzeugt das IFC-Modell aus B1 einmal in einem temporären Ordner
    (byte-identisch zu ausgabe/wandelement.ifc) und stellt GUIDs bereit."""

    def __init__(self):
        self._tmp = tempfile.TemporaryDirectory()
        self.pfad = b1.schreibe_ifc(b1.lade_parameter(), Path(self._tmp.name) / "wandelement.ifc")
        self.sha = sha_datei(self.pfad)
        self.f = ifcopenshell.open(str(self.pfad))
        self.wand = self.f.by_type("IfcWall")[0]

    def gegenstand(self, bezeichnung: str, guid=None, klasse="IfcWall", weitere=()) -> Gegenstand:
        return Gegenstand(bezeichnung, guid or self.wand.GlobalId, klasse, "wandelement.ifc (aus B1)", self.sha, list(weitere))


def qto(el, pset: str, name: str) -> float:
    for rel_ in el.IsDefinedBy:
        d = rel_.RelatingPropertyDefinition
        if d.is_a("IfcElementQuantity") and d.Name == pset:
            for q in d.Quantities:
                if q.Name == name:
                    return float(q[3])
    raise KeyError(f"{pset}.{name} fehlt an {el}")


def material_von(el) -> str | None:
    for r in el.HasAssociations:
        if r.is_a("IfcRelAssociatesMaterial"):
            m = r.RelatingMaterial
            return getattr(m, "Name", None)
    return None


# ===========================================================================
# B1 – Mengen- und Massennachweis des Wandelements
# ===========================================================================

def nachweis_b1(modell: Modell) -> Nachweis:
    param = b1.lade_parameter()
    w, mats = param["wand"], param["materialien"]
    lay = b1.rahmenlayout(w)
    sch = {s["id"]: s for s in w["schichten_innen_nach_aussen"]}
    o = w["oeffnungen"][0]
    kv = w["kerven"][0]
    vm = w["verbindungsmittel"][0]
    Q = "daten/wandelement.json"

    members = modell.f.by_type("IfcMember")
    plates = modell.f.by_type("IfcPlate")
    daemm = [p for p in modell.f.by_type("IfcBuildingElementPart") if p.PredefinedType == "INSULATION"]
    schrauben = modell.f.by_type("IfcMechanicalFastener")
    V_holz_ifc = sum(qto(m, "Qto_MemberBaseQuantities", "NetVolume") for m in members)
    V_platten_ifc = sum(qto(p, "Qto_PlateBaseQuantities", "NetVolume") for p in plates)
    V_daemm_ifc = sum(qto(p, "Qto_BodyGeometryValidation", "NetVolume") for p in daemm)

    def rho(key, rel_u):
        m = mats[key]
        return G(f"Rohdichte {m['name']}", f"rho_{key}", m["rho"], "kg/m³",
                 f"{Q} /materialien/{key}/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; "
                 f"u = {int(rel_u * 100)} % angenommen", m["rho"] * rel_u, "annahme")

    eingaben = [
        G("Wandlänge", "L", w["laenge"], "mm", f"{Q} /wand/laenge"),
        G("Wandhöhe", "H", w["hoehe"], "mm", f"{Q} /wand/hoehe"),
        G("Fensterbreite (Rohbau)", "b_F", o["breite"], "mm", f"{Q} /wand/oeffnungen/0/breite"),
        G("Fensterhöhe (Rohbau)", "h_F", o["hoehe"], "mm", f"{Q} /wand/oeffnungen/0/hoehe"),
        G("Holzquerschnittstiefe", "t_H", w["staender"]["tiefe"], "mm", f"{Q} /wand/staender/tiefe"),
        G("Kervenbreite (= Ständerbreite)", "b_K", w["staender"]["breite"], "mm", f"{Q} /wand/staender/breite"),
        G("Kerventiefe", "t_K", kv["tiefe"], "mm", f"{Q} /wand/kerven/0/tiefe"),
        G("Kervenhöhe", "h_K", kv["hoehe"], "mm", f"{Q} /wand/kerven/0/hoehe"),
        G("Dicke GKF", "d_GKF", sch["gkf"]["dicke"], "mm", f"{Q} Schicht gkf"),
        G("Dicke OSB/3", "d_OSB", sch["osb"]["dicke"], "mm", f"{Q} Schicht osb"),
        G("Dicke Gefach", "d_G", sch["gefach"]["dicke"], "mm", f"{Q} Schicht gefach"),
        G("Dicke Holzfaserdämmplatte", "d_HFD", sch["hfd"]["dicke"], "mm", f"{Q} Schicht hfd"),
        G("Schraubendurchmesser", "d_S", vm["durchmesser"], "mm", f"{Q} /wand/verbindungsmittel/0/durchmesser"),
        G("Schraubenlänge", "l_S", vm["laenge"], "mm", f"{Q} /wand/verbindungsmittel/0/laenge"),
        rho("kvh_c24", 0.10), rho("gkf", 0.05), rho("osb3", 0.10), rho("holzfaser_flex", 0.15), rho("holzfaserplatte", 0.10),
        G("Rohdichte Stahl", "rho_St", mats["stahl_verzinkt"]["rho"], "kg/m³", f"{Q} /materialien/stahl_verzinkt/rho", art="annahme"),
        G("zulässige Mengenabweichung Modell/IFC", "dV_zul", 1e-8, "m³",
          "Projektregel: Qto-Werte sind auf 1e-9 m³ gerundet; Summe über ≤ 18 Teile ergibt höchstens 9e-9 m³", art="grenzwert"),
    ]
    guids_holz = [m.GlobalId for m in members]
    schritte = [
        Schritt("Bruttowandfläche", G("Bruttowandfläche", "A_b", None, "m²"), "L*H"),
        Schritt("Öffnungsfläche Fenster F1", G("Öffnungsfläche", "A_F", None, "m²"), "b_F*h_F"),
        Schritt("Nettowandfläche", G("Nettowandfläche", "A_n", None, "m²"), "A_b - A_F"),
        Schritt("Ansichtsfläche aller Hölzer", G("Holzansichtsfläche", "A_H", lay["holzflaeche_mm2"] / 1e6, "m²",
                                                     "b1_wandelement.rahmenlayout"),
                verfahren=f"Summe der {len(lay['hoelzer'])} achsparallelen Holzrechtecke aus b1_wandelement.rahmenlayout; "
                          "Überlappungsfreiheit per shapely-Vereinigung geprüft (Differenz < 1e-6 mm²)"),
        Schritt("Gefachfläche (Dämmung)", G("Gefachfläche", "A_G", None, "m²"), "A_n - A_H"),
        Schritt("Volumen der Kerve K1", G("Kervenvolumen", "V_K", None, "m³"), "b_K*t_K*h_K"),
        Schritt("Holzvolumen netto", G("Holzvolumen", "V_H", None, "m³"), "A_H*t_H - V_K"),
        Schritt("Volumen GKF", G("Volumen GKF", "V_GKF", None, "m³"), "A_n*d_GKF", norm_verweis="Platten decken A_n vollständig"),
        Schritt("Volumen OSB/3", G("Volumen OSB", "V_OSB", None, "m³"), "A_n*d_OSB"),
        Schritt("Volumen Holzfaserdämmplatte", G("Volumen HFD", "V_HFD", None, "m³"), "A_n*d_HFD"),
        Schritt("Volumen Gefachdämmung", G("Volumen Dämmung", "V_D", None, "m³"), "A_G*d_G"),
        Schritt("Anzahl Schrauben (aus dem IFC-Modell)", G("Anzahl Schrauben", "n_S", len(schrauben), "Stk", "IFC: IfcMechanicalFastener"),
                verfahren="Zählung der IfcMechanicalFastener im Modell (Raster 150 mm, Randabstand 75 mm, Plattenrand ≥ 10 mm)"),
        Schritt("Masse Holz", G("Masse Holz", "m_H", None, "kg"), "rho_kvh_c24*V_H"),
        Schritt("Masse GKF", G("Masse GKF", "m_GKF", None, "kg"), "rho_gkf*V_GKF"),
        Schritt("Masse OSB/3", G("Masse OSB", "m_OSB", None, "kg"), "rho_osb3*V_OSB"),
        Schritt("Masse Holzfaserdämmplatte", G("Masse HFD", "m_HFD", None, "kg"), "rho_holzfaserplatte*V_HFD"),
        Schritt("Masse Gefachdämmung", G("Masse Dämmung", "m_D", None, "kg"), "rho_holzfaser_flex*V_D"),
        Schritt("Masse Schrauben (Schaft als Zylinder, wie Modellgeometrie)", G("Masse Schrauben", "m_S", None, "kg"),
                "n_S*rho_St*pi*(d_S/2)**2*l_S"),
        Schritt("Gesamtmasse des Wandelements", G("Gesamtmasse", "m_ges", None, "kg"),
                "m_H + m_GKF + m_OSB + m_HFD + m_D + m_S"),
        Schritt("flächenbezogene Masse", G("flächenbezogene Masse", "m_A", None, "kg/m²"), "m_ges/A_n"),
        Schritt("Holzvolumen laut IFC (Summe Qto_MemberBaseQuantities.NetVolume)",
                G("Holzvolumen IFC", "V_H_IFC", V_holz_ifc, "m³", "IFC-Modell"),
                verfahren=f"Summe NetVolume über {len(members)} IfcMember (GUIDs im Gegenstand)"),
        Schritt("Beplankungsvolumen laut IFC (Summe Qto_PlateBaseQuantities.NetVolume)",
                G("Beplankungsvolumen IFC", "V_P_IFC", V_platten_ifc, "m³", "IFC-Modell"),
                verfahren=f"Summe NetVolume über {len(plates)} IfcPlate"),
        Schritt("Dämmvolumen laut IFC (Summe Qto_BodyGeometryValidation.NetVolume)",
                G("Dämmvolumen IFC", "V_D_IFC", V_daemm_ifc, "m³", "IFC-Modell"),
                verfahren=f"Summe NetVolume über {len(daemm)} IfcBuildingElementPart INSULATION"),
        Schritt("Abweichung Holzvolumen Nachweis/IFC", G("Abweichung Holz", "dV_H", None, "m³"), "abs(V_H - V_H_IFC)"),
        Schritt("Abweichung Beplankung Nachweis/IFC", G("Abweichung Beplankung", "dV_P", None, "m³"),
                "abs(V_GKF + V_OSB + V_HFD - V_P_IFC)"),
        Schritt("Abweichung Dämmung Nachweis/IFC", G("Abweichung Dämmung", "dV_D", None, "m³"), "abs(V_D - V_D_IFC)"),
    ]
    n = Nachweis(
        id="N-B1-01", titel=f"Mengen- und Massenermittlung Wandelement {w['id']} ({w['name']})",
        gegenstand=modell.gegenstand(f"Wandelement {w['id']} mit {len(members)} Hölzern", weitere=guids_holz),
        regel=Regel("Mengen und Massen des vorgefertigten Wandelements aus dem Parametermodell ermitteln; die Mengen müssen "
                    "mit den Mengenangaben (Qto) des IFC-Modells übereinstimmen.",
                    "Projektregel Mengenermittlung (eigene Festlegung)", "2026-09", "HRB-Mengen", PROFILVERSION,
                    "vgl. Qto_MemberBaseQuantities, Qto_PlateBaseQuantities (IFC 4.3)", "[V]"),
        eingaben=eingaben, schritte=schritte, ergebnis="m_ges",
        kriterien=[Kriterium("Holzvolumen: Nachweis = IFC", "dV_H", "≤", "dV_zul", "Konsistenz Modell/IFC"),
                   Kriterium("Beplankung: Nachweis = IFC", "dV_P", "≤", "dV_zul", "Konsistenz Modell/IFC"),
                   Kriterium("Dämmung: Nachweis = IFC", "dV_D", "≤", "dV_zul", "Konsistenz Modell/IFC")],
        ergebnis_rundung=Rundung("signifikant", 3, quelle="Massen für Transport- und Montageplanung; drei Stellen genügen"),
        annahmen=["Die Dampfbremse (0,2 mm) hat im Parametermodell keine Rohdichte und bleibt in der Masse unberücksichtigt.",
                  "Schrauben als Zylinder d × l (Kopf und Gewinde nicht modelliert), wie die IFC-Geometrie.",
                  "Die Unsicherheiten der Rohdichten sind Annahmen zur Demonstration der Unsicherheitsfortpflanzung."],
        hinweise=[KEINE_RECHTSAUSKUNFT],
        monte_carlo=50_000,
    )
    n.rechne()
    n.grafiken = [
        Grafik("ansicht", f"Wandansicht {w['id']} von innen (Holzgerüst, Öffnung, Kerve)", wandansicht_svg(param, lay),
               "ansicht", "Bemaßung in mm. Hölzer schraffiert, Öffnung mit Kreuz, Kerve rot.", "1:50"),
        Grafik("massen", "Massen je Bestandteil", diagramm_balken(
            [{"label": s.ergebnis.name, "wert": s.ergebnis.wert} for s in n.schritte if s.ergebnis.symbol in
             ("m_H", "m_GKF", "m_OSB", "m_HFD", "m_D", "m_S")] +
            [{"label": "Gesamtmasse", "wert": n.groessen()["m_ges"].wert, "U": n.unsicherheit["U"]}],
            "Masse in kg", "Massen je Bestandteil (Gesamtmasse mit U, k = 2)"), "diagramm"),
    ]
    return n


def wandansicht_svg(param: dict, lay: dict) -> str:
    w = param["wand"]
    L, H = w["laenge"], w["hoehe"]
    z = SvgZeichnung((-300.0, -350.0, L + 150.0, H + 150.0), 50, 0.001, rand_mm=10.0, unten_mm=18.0,
                     titel=f"Wandansicht {w['id']}")
    z.rechteck(0, 0, L, H, fill="#fbfbfb", stroke=FARBE["tinte"], lw=0.5, titel="Wandumriss")
    for h in lay["hoelzer"]:
        z.rechteck(h["x0"], h["z0"], h["x1"], h["z1"], fill=z.muster("holz"), stroke=FARBE["tinte"], lw=0.35, titel=h["name"])
    for o in lay["oeffnungen"]:
        z.rechteck(o["x0"], o["z0"], o["x1"], o["z1"], fill="#ffffff", stroke=FARBE["tinte"], lw=0.5, titel=f"{o['art']} {o['id']}")
        z.linie((o["x0"], o["z0"]), (o["x1"], o["z1"]), lw=0.18)
        z.linie((o["x0"], o["z1"]), (o["x1"], o["z0"]), lw=0.18)
        z.text(((o["x0"] + o["x1"]) / 2, o["z0"] + 150), f"{o['art']} {o['id']}", 2.5)
    for kv in w["kerven"]:
        st = next(h for h in lay["hoelzer"] if h["pfad"] == f"/wand/staender/raster/{kv['staender_rasterindex']}")
        z.rechteck(st["x0"], kv["z"], st["x1"], kv["z"] + kv["hoehe"], fill=FARBE["krit"], stroke=FARBE["krit"], lw=0.25, titel=f"Kerve {kv['id']}")
        z.text((st["x1"] + 40, kv["z"] - 20), f"Kerve {kv['id']}, OK {kv['z'] + kv['hoehe']}", 2.0, "start")
    o = lay["oeffnungen"][0]
    e = w["staender"]["raster"]
    # Maßketten außen: unten Öffnungslage und Gesamtlänge, rechts Brüstung/Öffnung/Sturzbereich, links Gesamthöhe, oben Raster
    for x0, x1 in ((0, o["x0"]), (o["x0"], o["x1"]), (o["x1"], L)):
        z.bemassung((x0, 0), (x1, 0), -6.0, zahl_roh(x1 - x0), 2.2)
    z.bemassung((0, 0), (L, 0), -13.0, zahl_roh(L))
    for z0, z1 in ((0, o["z0"]), (o["z0"], o["z1"]), (o["z1"], H)):
        z.bemassung((L, z0), (L, z1), -6.0, zahl_roh(z1 - z0), 2.2)
    z.bemassung((0, 0), (0, H), 6.0, zahl_roh(H))
    z.bemassung((0, H), (e, H), 5.0, f"e = {e}", 2.2)
    z.bemassung((e, H), (2 * e, H), 5.0, zahl_roh(e), 2.2)
    yl = z.h_zeichnung + 2
    z.legende(z.rand, yl, [({"fill": z.muster("holz")}, "KVH C24 (Ständer, Schwelle, Rähm, Sturz, Riegel)"),
                           ({"fill": FARBE["krit"]}, "Kerve K1 (40 × 25 mm)"),
                           ({"fill": "#ffffff"}, "Fensteröffnung F1 (Rohbaumaß)")], spalten=1)
    z.text_papier(z.b - z.rand, yl + 3, "Maße in mm   M 1:50", 2.5, "end")
    return z.svg()


# ===========================================================================
# B2 – IDS: je Spezifikation ein Nachweis
# ===========================================================================

def nachweise_b2(modell: Modell, fall: str) -> list[Nachweis]:
    from ifctester import ids
    spez = ids.open(str(b2.IDS_DATEI), validate=True)
    ids_sha = sha_datei(b2.IDS_DATEI)
    if fall == "bestanden":
        pfad, sha = modell.pfad, modell.sha
    else:
        pfad = Path(modell._tmp.name) / "wandelement_fehlerhaft.ifc"
        if not pfad.exists():
            b2.baue_fehlerhaft(modell.pfad, pfad)
        sha = sha_datei(pfad)
    f = ifcopenshell.open(str(pfad))
    spez.validate(f)
    info = spez.info
    erg = []
    for s in spez.specifications:
        sid = s.identifier or s.name.split(" ")[0]
        n_anw, n_fehl = len(s.applicable_entities), len(s.failed_entities)
        verboten = s.maxOccurs == 0
        anf = "; ".join(r.to_string("requirement", s, r) for r in s.requirements) or "–"
        anw = "; ".join(a.to_string("applicability", s, a) for a in s.applicability)
        eingaben = [G("anwendbare Elemente", "n_anw", n_anw, "Stk", "ifctester 0.8.5: Specification.applicable_entities"),
                    G("Elemente mit Verstoß", "n_fehl", n_fehl, "Stk", "ifctester 0.8.5: Specification.failed_entities")]
        if verboten:
            eingaben.append(G("höchstzulässige Anzahl", "n_max", 0, "Stk", f"IDS {sid}: maxOccurs = 0 (verboten)", art="grenzwert"))
            kriterien = [Kriterium("keine anwendbaren Elemente (verboten)", "n_anw", "≤", "n_max", f"{b2.IDS_DATEI.name}, {sid}")]
        else:
            eingaben += [G("Mindestanzahl anwendbarer Elemente", "n_min", int(s.minOccurs), "Stk", f"IDS {sid}: minOccurs = {s.minOccurs}", art="grenzwert"),
                         G("zulässige Verstöße", "n_zul", 0, "Stk", "IDS 1.0: jede Anforderung gilt für jedes anwendbare Element", art="grenzwert")]
            kriterien = [Kriterium("Anwendbarkeit (Kardinalität)", "n_anw", "≥", "n_min", f"{b2.IDS_DATEI.name}, {sid}"),
                         Kriterium("alle Anforderungen erfüllt", "n_fehl", "≤", "n_zul", f"{b2.IDS_DATEI.name}, {sid}")]
        befunde = []
        for r in s.requirements:
            for fe in (getattr(r, "failures", None) or []):
                el = fe["element"]
                befunde.append(f"Befund: {el.is_a()} „{getattr(el, 'Name', '')}“ GUID {el.GlobalId}: {fe['reason']}")
        if verboten and n_anw:
            befunde += [f"Befund: verbotenes Element {e.is_a()} „{getattr(e, 'Name', '')}“ GUID {e.GlobalId}" for e in s.applicable_entities]
        guids = [e.GlobalId for e in s.applicable_entities if hasattr(e, "GlobalId")]
        wand = any(e.is_a("IfcWall") for e in s.applicable_entities) and n_anw == 1
        n = Nachweis(
            id=f"N-B2-{fall}-{sid}", titel=f"IDS {sid}: {s.name.split(' ', 1)[1] if ' ' in s.name else s.name} ({fall})",
            gegenstand=Gegenstand(f"{pfad.name}: {n_anw} anwendbare Elemente ({anw})",
                                  guids[0] if wand else None, "IfcWall" if wand else None, pfad.name, sha,
                                  [] if wand else guids),
            regel=Regel(f"{s.description} Anwendbarkeit: {anw}. Anforderung: {anf}.",
                        f"{b2.IDS_DATEI.name} (Information Delivery Specification, IDS 1.0)",
                        f"IDS-Datei Version {info.get('version')} vom {info.get('date')}, SHA-256 {ids_sha[:16]}…",
                        "HRB-IDS-Wandelement", info.get("version", PROFILVERSION), sid, "[V]"),
            eingaben=eingaben,
            schritte=[Schritt("IDS-Prüfung des Modells", G("Prüfstatus ifctester", "status_ifctester", bool(s.status), "1",
                                                            "ifctester 0.8.5"),
                              verfahren=f"ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); "
                                        f"Modell {pfad.name}, SHA-256 {sha[:16]}…"),
                      Schritt("Elemente ohne Verstoß", G("Elemente ohne Verstoß", "n_ok", None, "Stk"), "n_anw - n_fehl")],
            ergebnis="n_fehl" if not verboten else "n_anw", kriterien=kriterien,
            hinweise=befunde[:25] + ([f"… {len(befunde) - 25} weitere Befunde"] if len(befunde) > 25 else []),
        )
        n.rechne()
        if (n.status == "erfüllt") != bool(s.status):
            raise AssertionError(f"{sid}: Nachweisstatus {n.status} ≠ ifctester {s.status}")
        n.hinweise.append("Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).")
        n.grafiken = [Grafik("anteil", f"{sid}: Elemente mit und ohne Verstoß",
                             balken_anteil_svg([("ohne Verstoß", n_anw - n_fehl if not verboten else 0, FARBE["gut"]),
                                                ("mit Verstoß", n_fehl if not verboten else n_anw, FARBE["krit"])],
                                               f"{sid} ({fall}): {'erfüllt' if s.status else 'nicht erfüllt'}"), "diagramm")]
        n._gerechnet = False
        erg.append(n)
    return erg


# ===========================================================================
# B3 – U-Wert nach DIN EN ISO 6946
# ===========================================================================

ISO6946 = "DIN EN ISO 6946:2018-03 (ISO 6946:2017)"


def nachweis_b3(modell: Modell, variante: str, fassade: str) -> Nachweis:
    param = b3.lade_parameter()
    w, mats = param["wand"], param["materialien"]
    f_holz = b3.holzanteil_raster(param) if variante == "raster" else b3.holzanteil_geometrie(param)
    lay = b1.rahmenlayout(param["wand"])
    kern = b3.berechne_uwert(param, f_holz, fassade)
    sch = {s["id"]: s for s in w["schichten_innen_nach_aussen"]}
    Q = "daten/wandelement.json"
    lam = lambda k: mats[k]["lambda"]  # noqa: E731
    U_ann = "Annahme zur Demonstration der Unsicherheitsfortpflanzung"
    eingaben = [
        G("Wärmeübergangswiderstand innen", "R_si", b3.RSI, "m²·K/W", f"{ISO6946}, 6.8, horizontaler Wärmestrom", art="konstante"),
        G("Wärmeübergangswiderstand außen", "R_se", b3.RSE[fassade], "m²·K/W",
          f"{ISO6946}, 6.8" + (" (Fassade verputzt)" if fassade == "verputzt" else "; stark belüftete Luftschicht: R_se = R_si (6.9.4)"),
          art="konstante"),
        G("Dicke GKF", "d_GKF", sch["gkf"]["dicke"], "mm", f"{Q} Schicht gkf", 0.3, verteilung="rechteck"),
        G("Dicke OSB/3", "d_OSB", sch["osb"]["dicke"], "mm", f"{Q} Schicht osb", 0.3, verteilung="rechteck"),
        G("Dicke Gefach", "d_G", sch["gefach"]["dicke"], "mm", f"{Q} Schicht gefach", 2.0, verteilung="rechteck"),
        G("Dicke Holzfaserdämmplatte", "d_HFD", sch["hfd"]["dicke"], "mm", f"{Q} Schicht hfd", 1.0, verteilung="rechteck"),
        G("Bemessungswert λ GKF", "lambda_GKF", lam("gkf"), "W/(m·K)", f"{Q}: {mats['gkf']['lambda_quelle']} (Beispielwert)", lam("gkf") * 0.03),
        G("Bemessungswert λ OSB/3", "lambda_OSB", lam("osb3"), "W/(m·K)", f"{Q}: {mats['osb3']['lambda_quelle']} (Beispielwert)", lam("osb3") * 0.03),
        G("Bemessungswert λ Holz (KVH C24)", "lambda_H", lam("kvh_c24"), "W/(m·K)", f"{Q}: {mats['kvh_c24']['lambda_quelle']} (Beispielwert)", lam("kvh_c24") * 0.03),
        G("Bemessungswert λ Gefachdämmung", "lambda_D", lam("holzfaser_flex"), "W/(m·K)", f"{Q}: {mats['holzfaser_flex']['lambda_quelle']}", lam("holzfaser_flex") * 0.03),
        G("Bemessungswert λ Holzfaserdämmplatte", "lambda_HFD", lam("holzfaserplatte"), "W/(m·K)", f"{Q}: {mats['holzfaserplatte']['lambda_quelle']}", lam("holzfaserplatte") * 0.03),
        G("Holzanteil der Gefachschicht", "f_a", f_holz, "1",
          "Raster: Ständerbreite/Achsmaß = 60/625" if variante == "raster" else
          f"Geometrie: Holzansichtsfläche/Nettowandfläche aus b1_wandelement.rahmenlayout = "
          f"{zahl_roh(lay['holzflaeche_mm2'])} mm² / {zahl_roh(lay['nettoflaeche_mm2'])} mm²"),
        G("Höchstwert des U-Werts", "U_max", 0.20, "W/(m²·K)", "holzrahmenbau.ids, HRB-01 (Projektanforderung, Beispielwert)", art="grenzwert"),
    ]
    schritte = [
        Schritt("Wärmedurchlasswiderstand GKF", G("R GKF", "R_GKF", None, "m²·K/W"), "d_GKF/lambda_GKF", norm_verweis=f"{ISO6946}, 6.7.1.1, Formel (3)"),
        Schritt("Wärmedurchlasswiderstand OSB/3", G("R OSB", "R_OSB", None, "m²·K/W"), "d_OSB/lambda_OSB", norm_verweis="6.7.1.1, Formel (3)"),
        Schritt("Wärmedurchlasswiderstand Holzfaserdämmplatte", G("R HFD", "R_HFD", None, "m²·K/W"), "d_HFD/lambda_HFD", norm_verweis="6.7.1.1, Formel (3)"),
        Schritt("Gefachschicht, Abschnitt a (Holz)", G("R Gefach Holz", "R_Ga", None, "m²·K/W"), "d_G/lambda_H", norm_verweis="6.7.1.1"),
        Schritt("Gefachschicht, Abschnitt b (Dämmung)", G("R Gefach Dämmung", "R_Gb", None, "m²·K/W"), "d_G/lambda_D", norm_verweis="6.7.1.1"),
        Schritt("Gesamtwiderstand Abschnitt a (innen bis außen)", G("R_T Abschnitt a", "R_Ta", None, "m²·K/W", latex=r"R_{\mathrm{T},a}"),
                "R_si + R_GKF + R_OSB + R_Ga + R_HFD + R_se", norm_verweis="6.7.2 (oberer Grenzwert, Abschnittswiderstände)"),
        Schritt("Gesamtwiderstand Abschnitt b", G("R_T Abschnitt b", "R_Tb", None, "m²·K/W", latex=r"R_{\mathrm{T},b}"),
                "R_si + R_GKF + R_OSB + R_Gb + R_HFD + R_se", norm_verweis="6.7.2"),
        Schritt("Flächenanteil Abschnitt b", G("Anteil Dämmung", "f_b", None, "1"), "1 - f_a"),
        Schritt("oberer Grenzwert R'_T (parallele Wärmeströme)", G("oberer Grenzwert", "R_o", None, "m²·K/W", latex=r"R'_{\mathrm{T}}"),
                "1/(f_a/R_Ta + f_b/R_Tb)", norm_verweis="6.7.2, oberer Grenzwert [Absatznummer U]"),
        Schritt("äquivalente Wärmeleitfähigkeit der Gefachschicht", G("λ''", "lambda_eq", None, "W/(m·K)", latex=r"\lambda''"),
                "f_a*lambda_H + f_b*lambda_D", norm_verweis="6.7.2, unterer Grenzwert"),
        Schritt("Wärmedurchlasswiderstand Gefach mit λ''", G("R'' Gefach", "R_Geq", None, "m²·K/W", latex=r"R''_{\mathrm{G}}"),
                "d_G/lambda_eq", norm_verweis="6.7.2, unterer Grenzwert"),
        Schritt("unterer Grenzwert R''_T (isotherme Ebenen)", G("unterer Grenzwert", "R_u", None, "m²·K/W", latex=r"R''_{\mathrm{T}}"),
                "R_si + R_GKF + R_OSB + R_Geq + R_HFD + R_se", norm_verweis="6.7.2, unterer Grenzwert [Absatznummer U]"),
        Schritt("Wärmedurchgangswiderstand als arithmetisches Mittel", G("Wärmedurchgangswiderstand", "R_T", None, "m²·K/W",
                                                                         rundung=Rundung("dezimalstellen", 2, quelle=f"{ISO6946}, 6.6 (sinngemäß)")),
                "(R_o + R_u)/2", norm_verweis="6.7.2.2 [V]"),
        Schritt("maximaler relativer Fehler", G("relativer Fehler", "e_rel", None, "%", rundung=Rundung("dezimalstellen", 1)),
                "(R_o - R_u)/(2*R_T)", norm_verweis="6.7.2, Abschätzung des Fehlers"),
        Schritt("Wärmedurchgangskoeffizient", G("U-Wert", "U", None, "W/(m²·K)",
                                                  bezug="Pset_WallCommon.ThermalTransmittance" if (variante, fassade) == ("geometrie", "verputzt") else None),
                "1/R_T", norm_verweis=f"{ISO6946}, 6.5.2, Formel (1)"),
    ]
    titel_v = {"raster": "Holzanteil aus dem Raster", "geometrie": "Holzanteil aus der Elementgeometrie"}[variante]
    n = Nachweis(
        id=f"N-B3-{variante}-{fassade}", titel=f"U-Wert Außenwand {w['id']} ({titel_v}, {fassade})",
        gegenstand=modell.gegenstand(f"Außenwand {w['id']}, Typ {w['typ']}, Variante {variante}/{fassade}"),
        regel=Regel("Der Wärmedurchgangskoeffizient der Außenwand darf 0,20 W/(m²·K) nicht überschreiten. Berechnung nach dem "
                    "vereinfachten Verfahren für Bauteile aus homogenen und inhomogenen Schichten (oberer und unterer Grenzwert).",
                    f"{ISO6946}; Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung)", "2018-03",
                    "DE-Waermeschutz-Beispiel", PROFILVERSION, "6.5.2, 6.6, 6.7.1.1, 6.7.2, 6.8", "[V]"),
        eingaben=eingaben, schritte=schritte, ergebnis="U", grenzwert="U_max", vergleich="≤",
        kriterium_norm_verweis="holzrahmenbau.ids HRB-01",
        ergebnis_rundung=Rundung("signifikant", 2, quelle=f"{ISO6946}, 6.5.2: Endergebnis auf zwei signifikante Stellen [V]"),
        annahmen=["Korrekturen ΔU nach Anhang F nicht angesetzt: Luftspalte Stufe 0 (Dämmung passgenau), Befestigungen durchdringen "
                  "die Dämmschicht nicht (6.4 d: Korrektur nur bei > 3 % von U).",
                  "Die Dampfbremse (0,2 mm) ist thermisch vernachlässigt.",
                  "λ-Werte sind Beispielwerte aus dem Parametermodell, keine Tabellenwerte der DIN 4108-4.",
                  f"Unsicherheiten der Dicken (Rechteckverteilung) und der λ-Werte (3 %, normal): {U_ann}."],
        hinweise=[KEINE_RECHTSAUSKUNFT,
                  "Im IFC-Modell (Pset_WallCommon.ThermalTransmittance) steht der U-Wert mit drei Dezimalstellen. Das ist ein Zwischenwert für "
                  "Folgerechnungen (vgl. JCGM 100:2008, 7.2.6); als Endergebnis gilt die Angabe mit zwei signifikanten Stellen."],
        monte_carlo=100_000,
    )
    n.gegenrechnung("U", kern.u_wert, "b3_uwert_iso6946.berechne_uwert → u_wert (6 Dezimalstellen)", 5e-7)
    n.gegenrechnung("R_o", kern.r_oben, "b3_uwert_iso6946.berechne_uwert → r_oben", 5e-7)
    n.gegenrechnung("R_u", kern.r_unten, "b3_uwert_iso6946.berechne_uwert → r_unten", 5e-7)
    if (variante, fassade) == ("geometrie", "verputzt"):
        u_ifc = next(p.NominalValue.wrappedValue for r in modell.wand.IsDefinedBy
                     for p in getattr(r.RelatingPropertyDefinition, "HasProperties", []) if p.Name == "ThermalTransmittance")
        n.gegenrechnung("U", float(u_ifc), "IFC Pset_WallCommon.ThermalTransmittance (3 Dezimalstellen)", 5e-4)
    n.rechne()
    Gd = n.groessen()
    st = w["staender"]
    schichten = [{"name": mats[s["material"]]["name"], "dicke_mm": s["dicke"],
                  "muster": {"gkf": "gips", "osb": "holzwerkstoff", "folie": None, "gefach": "daemmung", "hfd": "daemmung"}[s["id"]],
                  "text": f"{mats[s['material']]['name']}, d = {zahl_roh(s['dicke'])} mm"
                          + (f", λ = {zahl_roh(mats[s['material']]['lambda'])} W/(m·K)" if mats[s["material"]]["lambda"] else " (thermisch vernachlässigt)")}
                 for s in w["schichten_innen_nach_aussen"]]
    e = st["raster"]
    n.grafiken = [
        Grafik("schnitt", f"Horizontalschnitt Außenwand {w['id']} (ein Ständerfeld, e = {e} mm)",
               schnitt_svg(schichten, e, 5, f"Horizontalschnitt {w['id']}",
                           einlagen=[{"schicht_index": 3, "x0_mm": (e - st["breite"]) / 2, "breite_mm": st["breite"], "muster": "holz",
                                      "name": f"Ständer KVH C24 {st['breite']}/{st['tiefe']}, λ = {zahl_roh(mats['kvh_c24']['lambda'])} W/(m·K)"}],
                           innen=f"innen (R_si = {zahl_roh(b3.RSI)})", aussen=f"außen (R_se = {zahl_roh(b3.RSE[fassade])}, {fassade})"),
               "schnitt", "Abschnitt a = Holz (Ständer), Abschnitt b = Dämmung. Maße in mm.", "1:5"),
        Grafik("grenzwerte", "Grenzwerte des Wärmedurchgangswiderstands",
               diagramm_balken([{"label": "unterer Grenzwert R''_T", "wert": Gd["R_u"].wert},
                                {"label": "Mittelwert R_T", "wert": Gd["R_T"].wert},
                                {"label": "oberer Grenzwert R'_T", "wert": Gd["R_o"].wert}], "m²·K/W",
                               f"R''_T ≤ R_T ≤ R'_T, maximaler relativer Fehler e = {zahl_de(Rundung('dezimalstellen', 1).runde(Gd['e_rel'].wert))} %"),
               "diagramm"),
        Grafik("uwert", "U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)",
               diagramm_ist_grenzwert([{"label": f"U ({variante}, {fassade})", "ist": Gd["U"].wert, "grenz": 0.20, "vergleich": "≤",
                                        "U": n.unsicherheit["U"]}], "W/(m²·K)", "U ≤ U_max = 0,20 W/(m²·K)"), "diagramm"),
    ]
    return n


# ===========================================================================
# B4 – Abstandsflächen
# ===========================================================================

BAYBO = "BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft"


def nachweis_b4(param: dict, sz: dict, modus: str) -> Nachweis:
    g, regel = param["gebaeude_vorlage"], param["regel"]
    kern = b4.pruefe_szenario(param, sz, modus)
    zul = b4.zulaessige_flaeche(param)
    flaechen = b4.abstandsflaechen(g, sz["x"], sz["y"], regel, modus)
    Q = "daten/grundstueck.json"
    kurz = {"West (Traufe)": "W", "Ost (Traufe)": "O", "Süd (Giebel)": "S", "Nord (Giebel)": "N"}
    eingaben = [
        G("Giebelbreite (quer zum First)", "b", g["breite"], "m", f"{Q} /gebaeude_vorlage/breite"),
        G("Trauflänge", "l", g["laenge"], "m", f"{Q} /gebaeude_vorlage/laenge"),
        G("Wandhöhe bis Schnitt Wand/Dachhaut", "h_w", g["wandhoehe"], "m", f"{Q} /gebaeude_vorlage/wandhoehe"),
        G("Dachneigung", "alpha", g["dachneigung_grad"], "°", f"{Q} /gebaeude_vorlage/dachneigung_grad"),
        G("Lage Südwestecke x", "x_0", sz["x"], "m", f"{Q} Szenario {sz['id']}"),
        G("Lage Südwestecke y", "y_0", sz["y"], "m", f"{Q} Szenario {sz['id']}"),
        G("Anrechnung Dachhöhe (Neigung ≤ 70°)", "f_D", regel["dach_anteil_unter_grenzneigung"], "1", f"{BAYBO}, Abs. 4", art="konstante"),
        G("Anrechnung Giebeldreieck", "f_Gi", regel["dach_anteil_unter_grenzneigung"] if modus == "drittel" else 1.0, "1",
          f"Lesart „{modus}“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U])", art="annahme"),
        G("Faktor Tiefe", "c_T", regel["faktor"], "1", f"{BAYBO}, Abs. 5 Satz 1", art="konstante"),
        G("Mindesttiefe", "T_min", regel["mindesttiefe"], "m", f"{BAYBO}, Abs. 5 Satz 1", art="konstante"),
        G("zulässige Fläche außerhalb", "A_zul", 0.0, "m²", f"{BAYBO}, Abs. 2 Satz 1: Abstandsflächen auf dem Grundstück selbst", art="grenzwert"),
    ]
    schritte = [
        Schritt("Dachhöhe über Traufe", G("Dachhöhe", "h_D", None, "m"), "b/2*tan(alpha)"),
        Schritt("Maß H der Traufwände", G("H Traufe", "H_T", None, "m"), "h_w + f_D*h_D", norm_verweis=f"{BAYBO}, Abs. 4"),
        Schritt("Tiefe der Abstandsfläche Traufe", G("T Traufe", "T_T", None, "m"), "max(c_T*H_T, T_min)", norm_verweis="Abs. 5"),
        Schritt("Maß H der Giebelwände am First", G("H Giebel (First)", "H_G", None, "m"), "h_w + f_Gi*h_D", norm_verweis="Abs. 4"),
        Schritt("Tiefe der Abstandsfläche Giebel (First)", G("T Giebel", "T_G", None, "m"), "max(c_T*H_G, T_min)", norm_verweis="Abs. 5"),
    ]
    kriterien = []
    wand_t = {"W": "T_T", "O": "T_T", "S": "T_G", "N": "T_G"}
    for fl in flaechen:
        k = kurz[fl["wand"]]
        vorh = b4.vorhandene_tiefe(zul, fl["wand_linie"], fl["normale"])
        aus = fl["polygon"].difference(zul).area
        schritte.append(Schritt(f"vorhandene Tiefe vor Wand {fl['wand']} (Wandmitte bis Grenze der zulässigen Fläche)",
                                G(f"T vorhanden {k}", f"T_v_{k}", vorh, "m", "shapely 2.1.2"),
                                verfahren="Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von "
                                          "Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)"))
        schritte.append(Schritt(f"Fläche der Abstandsfläche {fl['wand']} außerhalb der zulässigen Fläche",
                                G(f"A außerhalb {k}", f"A_a_{k}", aus, "m²", "shapely 2.1.2"),
                                verfahren="Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), "
                                          "Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)"))
        kriterien.append(Kriterium(f"{fl['wand']}: Abstandsfläche auf dem Grundstück", f"A_a_{k}", "≤", "A_zul",
                                   f"{BAYBO}, Abs. 2", toleranz=1e-9))
        kriterien.append(Kriterium(f"{fl['wand']}: vorhandene ≥ erforderliche Tiefe (Wandmitte)", f"T_v_{k}", "≥", wand_t[k],
                                   f"{BAYBO}, Abs. 5"))
    n = Nachweis(
        id=f"N-B4-{sz['id']}-{modus}", titel=f"Abstandsflächen Szenario „{sz['id']}“ ({sz['beschreibung']}, Giebel: {modus})",
        gegenstand=Gegenstand(f"Gebäudevorlage {g['dachform']} {zahl_roh(g['breite'])} × {zahl_roh(g['laenge'])} m, Szenario {sz['id']} "
                              f"(kein IFC-Gebäudemodell in B4; GUID folgt mit dem Gebäudegenerator)"),
        regel=Regel("Vor den Außenwänden sind Abstandsflächen der Tiefe T = 0,4 H, mindestens 3 m, einzuhalten; sie müssen auf dem "
                    "Grundstück selbst liegen und dürfen bis zur Mitte öffentlicher Verkehrsflächen reichen. H = Wandhöhe + 1/3 "
                    "der Dachhöhe bei Dachneigung ≤ 70°.", BAYBO, "ab 01.05.2026", "BY-BayBO-2026-05", PROFILVERSION,
                    "Art. 6 Abs. 2, 4, 5", "[U]"),
        eingaben=eingaben, schritte=schritte, kriterien=kriterien, ergebnis="T_T",
        annahmen=["Gelände eben; Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 BayBO nicht berücksichtigt.",
                  "Giebelwand: Tiefe punktweise entlang der Wand (gestauchte Giebelform), unten auf die Mindesttiefe begrenzt."],
        hinweise=[KEINE_RECHTSAUSKUNFT],
    )
    wmap = {w["wand"]: w for w in kern["waende"]}
    n.gegenrechnung("T_T", wmap["West (Traufe)"]["T_erforderlich"], "b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)", 5e-4)
    n.gegenrechnung("T_G", wmap["Süd (Giebel)"]["T_erforderlich"], "b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)", 5e-4)
    n.gegenrechnung("h_D", kern["dachhoehe"], "b4_abstandsflaechen.pruefe_szenario → dachhoehe (3 Dez.)", 5e-4)
    n.rechne()
    if (n.status == "erfüllt") != kern["zulaessig"]:
        raise AssertionError(f"B4 {sz['id']}: Nachweis {n.status} ≠ Rechenkern {kern['zulaessig']}")
    Gd = n.groessen()
    x0, y0, b, l = sz["x"], sz["y"], g["breite"], g["laenge"]
    gs = Polygon(param["grundstueck"])
    strasse = zul.difference(gs) if param.get("strasse") else None
    minx, miny, maxx, maxy = gs.bounds
    def t_txt(v):
        return f"T = {zahl_de(Rundung('dezimalstellen', 2).runde(v))}"
    yt = y0 + 0.3 * l                                  # Höhe der Tiefenmaße an den Traufseiten
    yg = y0 + 0.8 * l                                  # Höhe der Grenzabstände
    bm = [
        {"a": (x0 - Gd["T_T"].wert, yt), "b": (x0, yt), "abstand_mm": 2.5, "text": t_txt(Gd["T_T"].wert)},
        {"a": (x0 + b, yt), "b": (x0 + b + Gd["T_T"].wert, yt), "abstand_mm": 2.5, "text": t_txt(Gd["T_T"].wert)},
        {"a": (x0 + b / 2, y0 - Gd["T_G"].wert), "b": (x0 + b / 2, y0), "abstand_mm": -2.5, "text": t_txt(Gd["T_G"].wert)},
        {"a": (x0 + b / 2, y0 + l), "b": (x0 + b / 2, y0 + l + Gd["T_G"].wert), "abstand_mm": -2.5, "text": t_txt(Gd["T_G"].wert)},
        {"a": (minx, yg), "b": (x0, yg), "abstand_mm": 2.5},
        {"a": (x0 + b, yg), "b": (maxx, yg), "abstand_mm": 2.5},
        {"a": (x0 + 0.2 * b, miny), "b": (x0 + 0.2 * b, y0), "abstand_mm": -2.5},
        {"a": (x0 + 0.2 * b, y0 + l), "b": (x0 + 0.2 * b, maxy), "abstand_mm": -2.5},
        {"a": (x0, y0 + l), "b": (x0 + b, y0 + l), "abstand_mm": -4.0},
        {"a": (x0 + b, y0), "b": (x0 + b, y0 + l), "abstand_mm": 4.0},
    ]
    n.grafiken = [
        Grafik("lageplan", f"Lageplan mit Abstandsflächen, Szenario {sz['id']} ({modus})",
               lageplan_svg(gs, box(x0, y0, x0 + b, y0 + l),
                            [{"polygon": fl["polygon"], "ok": fl["polygon"].difference(zul).area < 1e-9, "label": fl["wand"]} for fl in flaechen],
                            200, strasse, bm, f"Lageplan Szenario {sz['id']}",
                            [f"Abstandsflächen – {sz['id']}", f"BayBO Art. 6, Giebel: {modus}", "M 1:200, Maße in m",
                             f"Nachweis N-B4-{sz['id']}-{modus}", "Ergebnis: " + ("zulässig" if kern["zulaessig"] else "NICHT zulässig")]),
               "lageplan", "Nordrichtung = +y. Grün: Abstandsfläche innerhalb von Grundstück und halber Straße; rot: außerhalb. "
                           "Die Straße (schraffiert) ist bis zur Mitte anrechenbar.", "1:200"),
        Grafik("tiefen", "Vorhandene gegen erforderliche Tiefe je Wand",
               diagramm_ist_grenzwert([{"label": fl["wand"], "ist": Gd[f"T_v_{kurz[fl['wand']]}"].wert,
                                        "grenz": Gd[wand_t[kurz[fl['wand']]]].wert, "vergleich": "≥"} for fl in flaechen],
                                      "Tiefe in m (Wandmitte)", "T_vorhanden ≥ T_erforderlich"), "diagramm"),
    ]
    n._gerechnet = False
    return n


# ===========================================================================
# B5 – Treppe DIN 18065
# ===========================================================================

DIN18065 = "DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02)"


def nachweis_b5(geschosshoehe_mm: int = 2900, laufbreite_mm: int = 900, raster_mm: int = 5) -> Nachweis:
    loesungen, hinweise_kern = b5.loese(geschosshoehe_mm, laufbreite_mm, None, raster_mm)
    best = loesungen[0]
    Gz = b5.GRENZEN
    k = "b5_treppe_din18065.GRENZEN"
    eingaben = [
        G("Geschosshöhe (OKFF bis OKFF)", "h_G", geschosshoehe_mm, "mm", "Eingabe (Kommandozeile B5, Standard 2,90 m)"),
        G("nutzbare Laufbreite", "b_L", laufbreite_mm, "mm", "Eingabe (Kommandozeile B5)"),
        G("Fertigungsraster Auftritt", "r_a", raster_mm, "mm", "Annahme B5: übliches Raster im Treppenbau", art="annahme"),
        G("Steigung min.", "s_min", Gz["s_min"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Steigung max.", "s_max", Gz["s_max"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Auftritt min.", "a_min", Gz["a_min"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Auftritt max.", "a_max", Gz["a_max"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Schrittmaß min.", "S_min", Gz["schritt_min"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Schrittmaß max.", "S_max", Gz["schritt_max"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Laufbreite min.", "b_min", Gz["laufbreite_min"], "mm", f"{DIN18065}; {k}", art="grenzwert"),
        G("Zielwert Schrittmaß", "S_Z", b5.ZIEL_SCHRITTMASS, "mm", "Vorgabe der Aufgabe (Rangfolge, keine Normanforderung)", art="annahme"),
    ]
    schritte = [
        Schritt("kleinste Steigungszahl", G("n min", "n_min", None, "1"), "ceil(h_G/s_max)"),
        Schritt("größte Steigungszahl", G("n max", "n_max", None, "1"), "floor(h_G/s_min)"),
        Schritt("zulässige Lösungen im Suchraum", G("Anzahl Lösungen", "N_L", len(loesungen), "1", "b5_treppe_din18065.loese"),
                verfahren=f"vollständige Aufzählung n = n_min … n_max, a im Raster {raster_mm} mm, Filter nach allen Grenzwerten "
                          "(exakte Arithmetik mit fractions.Fraction)"),
        Schritt("gewählte Steigungszahl", G("Steigungen", "n", best.n_steigungen, "1", "b5_treppe_din18065.loese, Rang 1"),
                verfahren="lexikografische Rangfolge: |2s+a−630| (Toleranz ≤ halbe Rasterweite), |a−s−120|, |a+s−460|, Lauflänge"),
        Schritt("gewählter Auftritt", G("Auftritt", "a", best.a_mm, "mm", "b5_treppe_din18065.loese, Rang 1"), verfahren="wie vor"),
        Schritt("Steigung (alle gleich)", G("Steigung", "s", None, "mm", rundung=Rundung("dezimalstellen", 1)), "h_G/n"),
        Schritt("Schrittmaß", G("Schrittmaß", "S", None, "mm", rundung=Rundung("dezimalstellen", 1)), "2*s + a",
                norm_verweis="Schrittmaßregel 2s + a"),
        Schritt("Lauflänge (n − 1 Auftritte)", G("Lauflänge", "l_L", None, "mm"), "(n - 1)*a"),
        Schritt("Abweichung vom Zielschrittmaß", G("Abweichung Ziel", "dS", None, "mm", rundung=Rundung("dezimalstellen", 1)), "abs(S - S_Z)"),
    ]
    n = Nachweis(
        id="N-B5-01", titel=f"Treppenlauf gerade einläufig, Geschosshöhe {zahl_de(Rundung('dezimalstellen', 2).runde(geschosshoehe_mm / 1000))} m",
        gegenstand=Gegenstand("notwendige Treppe EG–OG, gerade einläufig (kein IFC-Modell in B5; IfcStair folgt mit dem Gebäudegenerator)"),
        regel=Regel("Baurechtlich notwendige Treppe in Wohngebäuden mit höchstens zwei Wohnungen: Steigung 140 … 200 mm, Auftritt "
                    "230 … 370 mm, Schrittmaß 2s + a = 590 … 650 mm, nutzbare Laufbreite ≥ 800 mm.",
                    DIN18065, "2020-08", "DE-DIN18065-WG2WE", PROFILVERSION, "Tabelle der Grenzmaße (Tabellen nicht übernommen)", "[U]"),
        eingaben=eingaben, schritte=schritte, ergebnis="S",
        kriterien=[Kriterium("Steigung ≥ min.", "s", "≥", "s_min", DIN18065), Kriterium("Steigung ≤ max.", "s", "≤", "s_max", DIN18065),
                   Kriterium("Auftritt ≥ min.", "a", "≥", "a_min", DIN18065), Kriterium("Auftritt ≤ max.", "a", "≤", "a_max", DIN18065),
                   Kriterium("Schrittmaß ≥ min.", "S", "≥", "S_min", DIN18065), Kriterium("Schrittmaß ≤ max.", "S", "≤", "S_max", DIN18065),
                   Kriterium("Laufbreite ≥ min.", "b_L", "≥", "b_min", DIN18065)],
        annahmen=["Nur gerade einläufige Treppe; Kopfhöhe, Podeste, Wendelung und Maßtoleranzen sind nicht geprüft.",
                  "Bequemlichkeits- und Sicherheitsregel sind Faustregeln und dienen nur der Rangfolge."],
        hinweise=[KEINE_RECHTSAUSKUNFT] + hinweise_kern,
    )
    n.gegenrechnung("s", best.s_mm, "b5_treppe_din18065.loese → s_mm (2 Dez.)", 5e-3)
    n.gegenrechnung("S", best.schrittmass_mm, "b5_treppe_din18065.loese → schrittmass_mm (2 Dez.)", 5e-3)
    n.gegenrechnung("l_L", best.lauflaenge_mm, "b5_treppe_din18065.loese → lauflaenge_mm", 1e-9)
    n.gegenrechnung("N_L", 68 if (geschosshoehe_mm, laufbreite_mm) == (2900, 900) else len(loesungen), "ergebnisse.md: 68 Lösungen", 0.0)
    n.rechne()
    from shapely.geometry import Polygon as SP
    band = SP([(140, 590 - 280), (200, 590 - 400), (200, 650 - 400), (140, 650 - 280)])
    bereich = box(Gz["s_min"], Gz["a_min"], Gz["s_max"], Gz["a_max"]).intersection(band)
    je_n = {}
    for lo in loesungen:
        je_n.setdefault(lo.n_steigungen, []).append(lo.a_mm)
    n.grafiken = [
        Grafik("schrittmass", "Schrittmaß-Diagramm: alle zulässigen Lösungen",
               diagramm_punkte([{"x": lo.s_mm, "y": lo.a_mm, "gruppe": f"zulässige Lösung ({len(loesungen)})"} for lo in loesungen],
                               "Steigung s in mm", "Auftritt a in mm",
                               f"Zulässiger Bereich nach DIN 18065 (WG ≤ 2 WE) und {len(loesungen)} Lösungen im {raster_mm}-mm-Raster",
                               bereich=[(round(x, 6), round(y, 6)) for x, y in list(bereich.exterior.coords)[:-1]],
                               linien=[{"punkte": [(140, 630 - 280), (200, 630 - 400)], "label": "Ziel 2s + a = 630 mm", "stil": "--"}],
                               hervorgehoben={"x": best.s_mm, "y": best.a_mm,
                                              "label": f"gewählt: n = {best.n_steigungen}, s = {zahl_de(Rundung('dezimalstellen', 1).runde(best.s_mm))}, a = {best.a_mm}"},
                               beschriftungen=[(geschosshoehe_mm / nn, max(a) + 4, f"n={nn}") for nn, a in sorted(je_n.items())]),
               "diagramm", "Jede Spalte gehört zu einer Steigungszahl n (s = h/n); innerhalb der Spalte variiert a im Raster."),
        Grafik("schnitt", f"Treppenschnitt der gewählten Lösung ({best.n_steigungen} Steigungen)",
               treppenschnitt_svg(best.n_steigungen, geschosshoehe_mm / best.n_steigungen, best.a_mm, 50,
                                  "Treppenschnitt", ["Treppe EG–OG (Beispiel)", f"{best.n_steigungen} STG {zahl_de(Rundung('dezimalstellen', 1).runde(best.s_mm))}/{best.a_mm}",
                                                     f"2s + a = {zahl_de(Rundung('dezimalstellen', 1).runde(best.schrittmass_mm))} mm", "M 1:50, Nachweis N-B5-01"]),
               "schnitt", "Stufenprofil schematisch; Laufplatte und Stufenstärke nicht bemessen.", "1:50"),
    ]
    n._gerechnet = False
    return n


# ===========================================================================
# Hauptprogramm
# ===========================================================================

def alle_nachweise() -> dict[str, list[Nachweis]]:
    modell = Modell()
    param4 = json.loads(b4.STANDARD_PARAMETER.read_text(encoding="utf-8"))
    return {
        "b1": [nachweis_b1(modell)],
        "b2_bestanden": nachweise_b2(modell, "bestanden"),
        "b2_fehlerhaft": nachweise_b2(modell, "fehlerhaft"),
        "b3": [nachweis_b3(modell, v, f) for v in ("geometrie", "raster") for f in ("verputzt", "hinterlueftet")],
        "b4": [nachweis_b4(param4, sz, "drittel") for sz in param4["szenarien"]] + [nachweis_b4(param4, param4["szenarien"][0], "voll")],
        "b5": [nachweis_b5()],
    }


HEFTE = {
    "b1": ("b1_wandelement", "Nachweisheft B1 – Mengen und Massen Wandelement AW-01", ""),
    "b2_bestanden": ("b2_ids_bestanden", "Nachweisheft B2 – IDS-Prüfung, Fall „bestanden“", ""),
    "b2_fehlerhaft": ("b2_ids_fehlerhaft", "Nachweisheft B2 – IDS-Prüfung, Fall „fehlerhaft“",
                      "Die Datei enthält sechs absichtlich eingebaute Fehler (F1–F6, siehe b2_ids_pruefung.py); die zugehörigen "
                      "Nachweise müssen scheitern."),
    "b3": ("b3_uwert", "Nachweisheft B3 – Wärmedurchgangskoeffizient Außenwand AW-01 (DIN EN ISO 6946)", ""),
    "b4": ("b4_abstandsflaechen", "Nachweisheft B4 – Abstandsflächen (BayBO Art. 6)",
           "Szenario „zu_nah“ ist absichtlich unzulässig und demonstriert den negativen Nachweis."),
    "b5": ("b5_treppe", "Nachweisheft B5 – Treppe (DIN 18065)", ""),
}


def main() -> None:
    AUSGABE.mkdir(parents=True, exist_ok=True)
    projekt = projekt_angaben()
    alle = alle_nachweise()
    uebersicht = {}
    for key, (basis, titel, vorb) in HEFTE.items():
        heft = Nachweisheft(titel, projekt, alle[key], vorbemerkung=vorb)
        pf = heft.schreibe(AUSGABE, basis)
        d = heft.als_dict()
        uebersicht[basis] = {"status": d["status"], "anzahl": len(d["nachweise"]), **d["zusammenfassung"], "hash": d["hash"]["wert"]}
        print(f"{basis:22s} {d['status']:14s} {len(d['nachweise']):3d} Nachweise  Hash {d['hash']['wert'][:16]}…  → {rel(pf['html'])}")
    gesamt = [n for k in ("b1", "b2_bestanden", "b3", "b4", "b5") for n in alle[k]]
    heft = Nachweisheft("Nachweisheft B1–B5 – Beispielhaus Holzrahmenbau (Proof of Concept)", projekt, gesamt,
                        vorbemerkung="Das Heft bündelt die Nachweise der Beispiele B1–B5. Szenario „zu_nah“ (B4) ist absichtlich "
                                     "unzulässig; der IDS-Fall „fehlerhaft“ steht im eigenen Heft b2_ids_fehlerhaft.")
    pf = heft.schreibe(AUSGABE, "gesamt")
    d = heft.als_dict()
    uebersicht["gesamt"] = {"status": d["status"], "anzahl": len(d["nachweise"]), **d["zusammenfassung"], "hash": d["hash"]["wert"]}
    print(f"{'gesamt':22s} {d['status']:14s} {len(d['nachweise']):3d} Nachweise  Hash {d['hash']['wert'][:16]}…  → {rel(pf['html'])}")
    (AUSGABE / "uebersicht.json").write_text(json.dumps(uebersicht, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

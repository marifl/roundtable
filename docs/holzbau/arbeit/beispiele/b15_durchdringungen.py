#!/usr/bin/env python3
"""
B15 – Rohrdurchmesser und Durchdringungen an der richtigen Stelle:
Abwasser-Fallleitung DN 100 (WC im OG) durch Holzbalkendecke, Ständerwand
und luftdichte Dachebene; dazu zwei Querbohrungen in Deckenbalken.

Eingabe:  daten/b15_durchdringungen.json
Ausgabe:  ausgabe/b15_durchdringungen.json   (Entscheidungen, Verstöße)
          ausgabe/b15_durchdringungen.ifc    (IFC4X3_ADD2)
          ausgabe/b15_bearbeitungen.btlx     (BTLx-artige Bearbeitungen, Schema
                                              NICHT validiert – XSD offline nicht
                                              erreichbar)

Regeln (Kennwerte mit Quelle, Details in Recherche 16):
  * Öffnungsdurchmesser = da + 2·(Dämmschlauch + Ringspalt), auf 10 mm
    aufgerundet (Beispielwerte).
  * Senkrechte Leitung durch Balken- oder Ständerraster: Die Öffnung muss mit
    Randabstand a ins Gefach passen. Sonst (1) Achse verschieben, wenn eine
    gemeinsame freie Lage für alle Raster innerhalb von verschiebung_max
    liegt, oder (2) Wechsel/Auswechslung (Stichbalken + 2 Wechsel bzw.
    Ständer kürzen + Riegel) → statischer Nachweis nötig.
  * Querbohrung in Biegeträgern (DIN EN 1995-1-1/NA, NCI NA.6.7):
    Öffnung ≤ 50 mm → Querschnittsschwächung (Nettoquerschnitt);
    > 50 mm → Durchbruch, unverstärkt nur bei hd ≤ 0,15 h, hro/hru ≥ 0,35 h,
    lA ≥ h/2 (Auflager), lz ≥ max(1,5 h; 300 mm). prEN 1995-1-1: in
    Vollholz verstärken (Entwurf) → Warnung.
  * Luftdichtheitsebene (DIN 4108-7): Systemmanschette nach Durchmesser.
  * Lüftungsmündung über Dach (DIN 1986-100 6.5): ≥ 1 m über Fenstersturz
    oder ≥ 2 m seitlich von Fenstern von Aufenthaltsräumen.
  * Brandschutz (MLAR/LAR Bayern 4.1.1): keine Abschottung in GK 1/2 und
    innerhalb von Wohnungen; sonst Abschottung mit Verwendbarkeitsnachweis,
    bei Holzbalkendecken für diese Konstruktion oder Betonverguss.
  * GModG Anlage 8: Abwasser ohne Dämmpflicht (b14.gmodg_mindestdaemmung).

Aufruf:   python b15_durchdringungen.py [--eingabe ...] [--ifc]
"""
from __future__ import annotations

import argparse
import copy
import json
import math
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

import b14_fussbodenaufbau as b14

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b15_durchdringungen.json"
AUSGABE = HIER / "ausgabe"
GUID_NAMENSRAUM = uuid.UUID("8d5a0f6e-2b7c-5e41-9a03-6c1f4b2e7d95")
NS_BTLX = "https://www.design2machine.com"


# ---------------------------------------------------------------------------
# 1. Geometrische Grundregeln
# ---------------------------------------------------------------------------

def oeffnung_d(da: float, entk: dict, extra_ringspalt: float | None = None) -> float:
    spalt = entk["ringspalt_mm"] if extra_ringspalt is None else extra_ringspalt
    roh = da + 2 * (entk["daemmschlauch_mm"] + spalt)
    r = entk["raster_rundung_mm"]
    return math.ceil(roh / r) * r


def achsen(erste: float, e: float, n: int) -> list[float]:
    return [erste + i * e for i in range(n)]


def kollision(p: float, ax: list[float], b: float, r: float, a: float) -> int | None:
    for i, x in enumerate(ax):
        if abs(p - x) < b / 2 + r + a - 1e-9:
            return i
    return None


def freie_intervalle(ax: list[float], b: float, r: float, a: float) -> list[tuple[float, float]]:
    iv = []
    for x0, x1 in zip(ax, ax[1:]):
        lo, hi = x0 + b / 2 + r + a, x1 - b / 2 - r - a
        if lo <= hi:
            iv.append((lo, hi))
    return iv


def gemeinsame_lage(p: float, intervall_listen: list[list[tuple[float, float]]]) -> float | None:
    """Nächste Achslage zu p, die in allen Rastern frei ist (Schnitt der
    Intervallmengen); None, wenn keine existiert."""
    schnitt = intervall_listen[0]
    for liste in intervall_listen[1:]:
        neu = []
        for a0, a1 in schnitt:
            for b0, b1 in liste:
                lo, hi = max(a0, b0), min(a1, b1)
                if lo <= hi:
                    neu.append((lo, hi))
        schnitt = neu
    if not schnitt:
        return None
    kand = [min(max(p, lo), hi) for lo, hi in schnitt]
    return min(kand, key=lambda x: (abs(x - p), x))


# ---------------------------------------------------------------------------
# 2. Regelprüfungen
# ---------------------------------------------------------------------------

def pruefe_balkendurchbruch(h: float, b: float, d: float, y: float, z_achse: float, z_uk: float,
                            auflager: list[float], andere_y: list[float] = ()) -> dict:
    """Querbohrung (rund) in einem Biegeträger nach DIN EN 1995-1-1/NA NCI NA.6.7."""
    erg = {"d_mm": d, "h_mm": h, "verstoesse": [], "hinweise": []}
    hru = (z_achse - d / 2) - z_uk
    hro = (z_uk + h) - (z_achse + d / 2)
    lA = min(abs(y - s) for s in auflager) - d / 2
    erg.update({"hro_mm": hro, "hru_mm": hru, "lA_mm": lA})
    if d <= 50:
        erg["einstufung"] = "Querschnittsschwächung (≤ 50 mm, NA: Nettoquerschnitt nachweisen)"
        if abs(hro - hru) > 0.1 * h:
            erg["hinweise"].append("Bohrung nicht mittig: Lage in der Schwerachse bevorzugen.")
        return erg
    erg["einstufung"] = "Durchbruch (> 50 mm, NA.6.7)"
    if d > 0.15 * h:
        erg["verstoesse"].append(f"hd = {d:g} mm > 0,15·h = {0.15 * h:g} mm → unverstärkt unzulässig "
                                 "(Leitung parallel zu den Balken führen, Wechsel oder Verstärkung mit Nachweis).")
    for name, wert in (("hro", hro), ("hru", hru)):
        if wert < 0.35 * h:
            erg["verstoesse"].append(f"{name} = {wert:g} mm < 0,35·h = {0.35 * h:g} mm.")
    if lA < h / 2:
        erg["verstoesse"].append(f"lA = {lA:g} mm < h/2 = {h / 2:g} mm (Abstand zum Auflager).")
    for y2 in andere_y:
        lz = abs(y2 - y) - d
        if lz < max(1.5 * h, 300):
            erg["verstoesse"].append(f"lz = {lz:g} mm < max(1,5·h; 300 mm).")
    erg["hinweise"].append("prEN 1995-1-1 (Entwurf): Durchbrüche in Vollholz/KVH verstärken; unverstärkt nur GL/LVL.")
    return erg


def pruefe_fenster(leitung: dict, fenster: list[dict]) -> list[dict]:
    """DIN 1986-100 6.5: Mündung ≥ 1 m über Fenstersturz oder ≥ 2 m seitlich."""
    aus = []
    for fe in fenster:
        seitlich = math.hypot(fe["x_kante"] - leitung["x"], fe["y"] - leitung["y"])
        ueber = leitung["z_muendung"] - fe["z_sturz"]
        ok = ueber >= 1000 or seitlich >= 2000
        e = {"fenster": fe["id"], "seitlich_mm": round(seitlich, 1), "ueber_sturz_mm": ueber, "ok": ok}
        if not ok:
            e["vorschlag"] = (f"Mündung auf z >= {fe['z_sturz'] + 1000} mm anheben (+{fe['z_sturz'] + 1000 - leitung['z_muendung']} mm) "
                              f"oder Abstand zum Fenster >= 2000 mm (fehlen {2000 - seitlich:.0f} mm).")
        aus.append(e)
    return aus


def brandschutz(geb: dict, bauteil: dict, leitung: dict) -> dict:
    if geb["gebaeudeklasse"] <= 2 or geb.get("nutzungseinheiten", 1) == 1:
        return {"abschottung": False, "grund": "MLAR/LAR 4.1.1: nicht erforderlich in GK 1 und 2 bzw. innerhalb von Wohnungen."}
    if not bauteil.get("feuerwiderstand"):
        return {"abschottung": False, "grund": "Bauteil ohne Feuerwiderstandsanforderung (raumabschließend) – keine Abschottung."}
    txt = (f"MLAR/LAR 4.1.2: Abschottung {bauteil['feuerwiderstand']} mit Verwendbarkeitsnachweis (abZ/aBG). ")
    if leitung["brennbar"] and leitung["da_mm"] > 32:
        txt += "Brennbares Rohr > 32 mm: Erleichterungen 4.3 nicht anwendbar → Brandschutzmanschette. "
    txt += ("Holzbauteil: Nachweis muss die Holzbalkendecke/Holztafel abdecken, sonst Betonverguss als Massivbauteil "
            "einbinden; MHolzBauRL beachten.")
    return {"abschottung": True, "grund": txt}


def manschette(katalog: list[dict], d: float) -> dict | None:
    for m in katalog:
        if m["d_min"] <= d <= m["d_max"]:
            return m
    return None


# ---------------------------------------------------------------------------
# 3. Planung der Durchdringungen
# ---------------------------------------------------------------------------

def plane(daten: dict) -> dict:
    L, entk, geb = daten["leitung"], daten["entkopplung"], daten["gebaeude"]
    de, wa, da = daten["decke"], daten["wand"], daten["dach"]
    d_oe = oeffnung_d(L["da_mm"], entk)
    r = d_oe / 2
    ax_d = achsen(de["erste_achse_x"], de["achsabstand"], de["anzahl"])
    ax_w = achsen(wa["erste_achse_x"], wa["achsabstand"], int(wa["laenge"] // wa["achsabstand"]) + 1)
    ax_s = achsen(da["erste_achse_y"], da["achsabstand"], da["anzahl"])
    d_dach = oeffnung_d(L["da_mm"], {**entk, "daemmschlauch_mm": 0}, da["ringspalt_luftdicht_mm"])
    ergebnis = {"leitung": L["id"], "oeffnung_decke_wand_mm": d_oe, "oeffnung_dach_mm": d_dach,
                "durchdringungen": [], "verstoesse": [], "hinweise": [], "fertigung": []}
    # --- Achse gegen Balken- und Ständerraster (beide in x) -------------
    k_d = kollision(L["x"], ax_d, de["balken_b"], r, de["randabstand_mm"])
    k_w = kollision(L["x"], ax_w, wa["staender_b"], r, wa["randabstand_mm"])
    x_frei = gemeinsame_lage(L["x"], [freie_intervalle(ax_d, de["balken_b"], r, de["randabstand_mm"]),
                                      freie_intervalle(ax_w, wa["staender_b"], r, wa["randabstand_mm"])])
    x_neu, strategie = L["x"], "Gefach"
    if k_d is not None or k_w is not None:
        if x_frei is not None and abs(x_frei - L["x"]) <= L["verschiebung_max_mm"]:
            x_neu, strategie = x_frei, "Verschiebung"
            ergebnis["hinweise"].append(f"Achse von x = {L['x']:g} auf {x_frei:g} mm verschieben "
                                        f"(Δ = {x_frei - L['x']:g} mm ≤ {L['verschiebung_max_mm']} mm): Balken- und Ständerraster frei.")
        else:
            strategie = "Wechsel"
            if x_frei is not None:
                ergebnis["hinweise"].append(
                    f"Nächste in Decke und Wand freie Achse x = {x_frei:g} mm läge {abs(x_frei - L['x']):g} mm entfernt "
                    f"> zulässig {L['verschiebung_max_mm']} mm (WC-Vorwand) → Wechsel/Auswechslung. Planungsempfehlung: "
                    "Fallleitungen in Gefachmitte des 625-mm-Rasters legen (Decke und Wand haben dasselbe Raster).")
    ergebnis["achse_x_mm"] = x_neu
    ergebnis["strategie"] = strategie

    # --- D1: Holzbalkendecke (senkrecht) ---------------------------------
    d1 = {"id": "D1", "bauteil": de["id"], "art": "senkrecht durch Holzbalkendecke", "oeffnung_d_mm": d_oe,
          "x": x_neu, "y": L["y"], "z_uk": de["z_uk_balken"], "tiefe_mm": de["balken_h"] + de["beplankung"]["dicke"],
          "massnahmen": [], "verstoesse": []}
    k = kollision(x_neu, ax_d, de["balken_b"], r, de["randabstand_mm"])
    if k is not None:
        xb = ax_d[k]
        y1 = L["y"] - r - de["randabstand_mm"] - de["balken_b"] / 2
        y2 = L["y"] + r + de["randabstand_mm"] + de["balken_b"] / 2
        d1["wechsel"] = {"balken_index": k, "balken_x": xb,
                         "wechsel_y": [y1, y2], "von_x": ax_d[k - 1] + de["balken_b"] / 2, "bis_x": ax_d[k + 1] - de["balken_b"] / 2,
                         "stichbalken": [[de["y0"], y1 - de["balken_b"] / 2], [y2 + de["balken_b"] / 2, de["y0"] + de["laenge"]]]}
        d1["massnahmen"].append(f"Wechsel: Balken {k} (x = {xb:g}) zwischen y = {y1 - 50:g} und {y2 + 50:g} unterbrechen, "
                                f"2 Wechsel {de['balken_b']}/{de['balken_h']} zwischen den Nachbarbalken; Stichbalken und "
                                "Wechselbalken statisch nachweisen (EC5, Balkenschuhe).")
        d1["massnahmen"].append("Senkrechter Durchbruch durch den Balken selbst ist ausgeschlossen (Querschnitt durchtrennt).")
    else:
        d1["massnahmen"].append("Öffnung im Gefach: nur Beplankung/Unterdecke schneiden, Balken unberührt.")
    d1["massnahmen"].append("Schallentkopplung: Dämmschlauch im Durchbruch, keine starre Verbindung Rohr–Holz; Rohrschellen mit Gummieinlage.")
    bs = brandschutz(geb, de, L)
    d1["brandschutz"] = bs
    if de["luftdichtheitsebene"]:
        d1["massnahmen"].append("Luftdichtheit: Manschette nach DIN 4108-7.")
    ergebnis["durchdringungen"].append(d1)
    ergebnis["fertigung"].append({"durchdringung": "D1", "bauteil": de["beplankung"]["name"] + " (Deckenelement)",
                                  "bearbeitung": "Drilling", "d_mm": d_oe, "x": x_neu, "y": L["y"],
                                  "start_x": x_neu - (de["erste_achse_x"] - de["balken_b"] / 2), "start_y": L["y"] - de["y0"],
                                  "anlage": "Multifunktionsbrücke: Bohrung mit Fräser (Ø ≥ ca. 70 mm, cadwork/Weinmann-Handbuch)"})

    # --- D2: Ständerwand (waagrechter WC-Anschluss) ----------------------
    z_a = L["z_anschluss_wc"]
    d2 = {"id": "D2", "bauteil": wa["id"], "art": "waagrecht durch Ständerwand (WC-Anschlussleitung)", "oeffnung_d_mm": d_oe,
          "x": x_neu, "y": wa["y_kern"], "z": z_a, "tiefe_mm": wa["kern_tiefe"] + sum(p["dicke"] for p in wa["beplankung"]),
          "massnahmen": [], "verstoesse": []}
    z_schwelle_ok = wa["z_uk"] + wa["schwelle_h"]
    z_raehm_uk = wa["z_uk"] + wa["hoehe"] - wa["raehm_h"]
    if z_a - r - wa["randabstand_mm"] < z_schwelle_ok or z_a + r + wa["randabstand_mm"] > z_raehm_uk:
        d2["verstoesse"].append("Öffnung schneidet Schwelle oder Rähm → Höhenlage ändern.")
    k = kollision(x_neu, ax_w, wa["staender_b"], r, wa["randabstand_mm"])
    fr = wa["firmenregel_staenderbohrung"]
    if k is not None:
        if d_oe <= fr["max_anteil_tiefe"] * wa["kern_tiefe"]:
            d2["massnahmen"].append(f"Bohrung im Ständer {k} zulässig nach Firmenregel ({fr['quelle']}).")
        else:
            z_u = z_a - r - wa["randabstand_mm"] - wa["schwelle_h"]
            z_o = z_a + r + wa["randabstand_mm"]
            d2["auswechslung"] = {"staender_index": k, "staender_x": ax_w[k], "riegel_z": [z_u, z_o],
                                  "von_x": ax_w[k - 1] + wa["staender_b"] / 2, "bis_x": ax_w[k + 1] - wa["staender_b"] / 2}
            d2["massnahmen"].append(
                f"Ständer {k} (x = {ax_w[k]:g}) trifft die Öffnung Ø {d_oe:g}: Bohrung {d_oe:g} mm > "
                f"{fr['max_anteil_tiefe']:.0%} der Ständertiefe {wa['kern_tiefe']} mm (Firmenregel-Platzhalter) → "
                "Ständer auswechseln: Ständer kürzen, Riegel ober- und unterhalb, Lastabtrag über Nachbarständer nachweisen "
                "(tragende Wand) oder Leitung in der Vorwand führen.")
    else:
        d2["massnahmen"].append("Öffnung im Gefach zwischen zwei Ständern: Beplankung beidseitig und Dämmung ausschneiden.")
    d2["massnahmen"].append("Schallentkopplung: Dämmschlauch, Gefach um die Leitung mit Mineralwolle stopfen (nicht starr).")
    d2["brandschutz"] = brandschutz(geb, wa, L)
    ergebnis["durchdringungen"].append(d2)
    for p in wa["beplankung"]:
        ergebnis["fertigung"].append({"durchdringung": "D2", "bauteil": f"{p['name']} ({p['seite']}, Wandtafel {wa['id']})",
                                      "bearbeitung": "Drilling", "d_mm": d_oe, "x": x_neu, "z": z_a,
                                      "start_x": x_neu, "start_y": z_a - wa["z_uk"],
                                      "anlage": "Multifunktionsbrücke (WUP/BTLx), Rückverfolgung über Leitungs-GUID"})

    # --- D3: luftdichte Dachebene + Mündung -------------------------------
    r3 = d_dach / 2
    d3 = {"id": "D3", "bauteil": da["id"], "art": "senkrecht durch luftdichte Ebene und Dach (Hauptlüftung DN 100)",
          "oeffnung_d_mm": d_dach, "x": x_neu, "y": L["y"], "z_uk": da["z_uk_sparren"] - da["beplankung"]["dicke"],
          "tiefe_mm": da["beplankung"]["dicke"] + da["sparren_h"], "massnahmen": [], "verstoesse": []}
    k = kollision(L["y"], ax_s, da["sparren_b"], r3, da["randabstand_mm"])
    if k is not None:
        d3["verstoesse"].append(f"Sparren {k} (y = {ax_s[k]:g}) im Weg → Sparrenwechsel nötig.")
    else:
        d3["massnahmen"].append("Öffnung zwischen zwei Sparren.")
    m = manschette(daten["manschetten"], L["da_mm"])
    if da["luftdichtheitsebene"]:
        if m:
            d3["manschette"] = m
            d3["massnahmen"].append(f"Luftdichtheit DIN 4108-7: {m['name']} (Ø {m['d_min']}–{m['d_max']} mm), mit Systemklebeband.")
        else:
            d3["verstoesse"].append(f"Keine Systemmanschette für Ø {L['da_mm']} mm im Katalog.")
        d3["massnahmen"].append("Winddichtung/Unterdeckung: Dunstrohrmanschette; Dacheindeckung: Lüfterdurchgang DN 100 nach oben offen.")
    fe = pruefe_fenster({**L, "x": x_neu}, da["fenster"])
    d3["fensterabstand"] = fe
    for e in fe:
        if not e["ok"]:
            d3["verstoesse"].append(f"Mündung zu nah an {e['fenster']}: seitlich {e['seitlich_mm']:g} mm, "
                                    f"{e['ueber_sturz_mm']:g} mm über Sturz (DIN 1986-100 6.5: ≥ 1 m über Sturz oder ≥ 2 m seitlich). "
                                    + e["vorschlag"])
    d3["brandschutz"] = {"abschottung": False, "grund": "Dach: keine Abschottung (MLAR 4.1.1, GK 1)."}
    ergebnis["durchdringungen"].append(d3)
    ergebnis["fertigung"].append({"durchdringung": "D3", "bauteil": da["beplankung"]["name"], "bearbeitung": "Drilling",
                                  "d_mm": d_dach, "x": x_neu, "y": L["y"], "start_x": x_neu - da["x0"], "start_y": L["y"],
                                  "anlage": "Dachelement (Werk) oder Baustelle"})

    # --- Querbohrungen in Balken ------------------------------------------
    for bd in daten["balkendurchbrueche"]:
        d = bd["da_mm"] + 2 * bd["spiel_mm"]
        pr = pruefe_balkendurchbruch(de["balken_h"], de["balken_b"], d, bd["y"], bd["z_achse"], de["z_uk_balken"], bd["auflager_y"])
        pr.update({"id": bd["id"], "bezeichnung": bd["bezeichnung"], "balken_index": bd["balken_index"]})
        ergebnis["durchdringungen"].append(pr)
        if not pr["verstoesse"]:
            ergebnis["fertigung"].append({"durchdringung": bd["id"], "bauteil": f"Deckenbalken {bd['balken_index']}",
                                          "bearbeitung": "Drilling", "d_mm": d, "y": bd["y"], "z": bd["z_achse"],
                                          "start_x": bd["y"] - de["y0"], "start_y": bd["z_achse"] - de["z_uk_balken"],
                                          "anlage": "Abbundanlage (BTLx Drilling)"})
    mind, grund = b14.gmodg_mindestdaemmung({"medium": "abwasser"})
    ergebnis["hinweise"].append(f"Dämmung {L['bezeichnung']}: {grund}; Schallschutz im EFH nur vertraglich (DIN 4109 schützt fremde Räume).")
    for dd in ergebnis["durchdringungen"]:
        ergebnis["verstoesse"].extend(f"{dd['id']}: {v}" for v in dd.get("verstoesse", []))
    return ergebnis


# ---------------------------------------------------------------------------
# 4. IFC
# ---------------------------------------------------------------------------

def erzeuge_ifc(daten: dict, erg: dict):
    L, de, wa, da = daten["leitung"], daten["decke"], daten["wand"], daten["dach"]
    w = b14.IfcSchreiber(GUID_NAMENSRAUM, daten["projekt"], "b15_durchdringungen.ifc")
    f = w.f
    _, gs = w.grundgeruest([("EG", 0.0), ("OG", de["z_uk_balken"] + de["balken_h"] + de["beplankung"]["dicke"]), ("DG", 5600.0)])
    welt = gs["EG"].ObjectPlacement  # alle Elemente in globalen Koordinaten relativ zum EG
    inhalt = {"EG": [], "OG": [], "DG": []}

    def teil(klasse, pfad, name, ursprung, dx, dy, dz, geschoss, **attr):
        e = w.root(klasse, pfad, Name=name, ObjectPlacement=w.platzierung(welt, ursprung),
                   Representation=w.form(w.body, "SweptSolid", [w.quader(dx, dy, dz)]), **attr)
        inhalt[geschoss].append(e)
        return e

    x_p, y_p = erg["achse_x_mm"], L["y"]
    d1, d2, d3 = erg["durchdringungen"][:3]
    # Decke: Balken (ggf. mit Wechsel) + OSB
    ax_d = achsen(de["erste_achse_x"], de["achsabstand"], de["anzahl"])
    b, h, z0 = de["balken_b"], de["balken_h"], de["z_uk_balken"]
    balken = {}
    for i, x in enumerate(ax_d):
        if "wechsel" in d1 and d1["wechsel"]["balken_index"] == i:
            for j, (ya, yb) in enumerate(d1["wechsel"]["stichbalken"]):
                balken[f"{i}s{j}"] = teil("IfcBeam", f"/decke/balken/{i}/stich/{j}", f"Stichbalken {i}.{j}",
                                          (x - b / 2, ya, z0), b, yb - ya, h, "EG", PredefinedType="JOIST")
            for j, yw in enumerate(d1["wechsel"]["wechsel_y"]):
                xa, xb = d1["wechsel"]["von_x"], d1["wechsel"]["bis_x"]
                teil("IfcBeam", f"/decke/wechsel/{j}", f"Wechsel {j}", (xa, yw - b / 2, z0), xb - xa, b, h, "EG",
                     PredefinedType="USERDEFINED", ObjectType="Wechsel")
        else:
            balken[str(i)] = teil("IfcBeam", f"/decke/balken/{i}", f"Deckenbalken {i}", (x - b / 2, de["y0"], z0),
                                  b, de["laenge"], h, "EG", PredefinedType="JOIST")
    osb = teil("IfcPlate", "/decke/osb", de["beplankung"]["name"], (ax_d[0] - b / 2, de["y0"], z0 + h),
               ax_d[-1] - ax_d[0] + b, de["laenge"], de["beplankung"]["dicke"], "EG", PredefinedType="SHEET")
    # Wand: Ständer + Beplankung
    ax_w = achsen(wa["erste_achse_x"], wa["achsabstand"], int(wa["laenge"] // wa["achsabstand"]) + 1)
    sb, zt = wa["staender_b"], wa["z_uk"]
    wand = w.root("IfcWall", "/wand", Name=wa["name"], PredefinedType="ELEMENTEDWALL", ObjectPlacement=w.platzierung(welt))
    inhalt["OG"].append(wand)
    wandteile = []
    for i, x in enumerate(ax_w):
        x = min(max(x, sb / 2), wa["laenge"] - sb / 2)
        if "auswechslung" in d2 and d2["auswechslung"]["staender_index"] == i:
            zu, zo = d2["auswechslung"]["riegel_z"]
            e1 = w.root("IfcMember", f"/wand/staender/{i}/unten", Name=f"Ständer {i} unten", PredefinedType="STUD",
                        ObjectPlacement=w.platzierung(welt, (x - sb / 2, wa["y_kern"], zt + wa["schwelle_h"])),
                        Representation=w.form(w.body, "SweptSolid", [w.quader(sb, wa["kern_tiefe"], zu - zt - wa["schwelle_h"])]))
            e2 = w.root("IfcMember", f"/wand/staender/{i}/oben", Name=f"Ständer {i} oben", PredefinedType="STUD",
                        ObjectPlacement=w.platzierung(welt, (x - sb / 2, wa["y_kern"], zo + wa["schwelle_h"])),
                        Representation=w.form(w.body, "SweptSolid", [w.quader(sb, wa["kern_tiefe"], zt + wa["hoehe"] - wa["raehm_h"] - zo - wa["schwelle_h"])]))
            wandteile += [e1, e2]
            for j, zr in enumerate((zu, zo)):
                xa, xb = d2["auswechslung"]["von_x"], d2["auswechslung"]["bis_x"]
                wandteile.append(w.root("IfcMember", f"/wand/riegel/{j}", Name=f"Wechselriegel {j}", PredefinedType="PLATE",
                                        ObjectPlacement=w.platzierung(welt, (xa, wa["y_kern"], zr)),
                                        Representation=w.form(w.body, "SweptSolid", [w.quader(xb - xa, wa["kern_tiefe"], wa["schwelle_h"])])))
        else:
            wandteile.append(w.root("IfcMember", f"/wand/staender/{i}", Name=f"Ständer {i}", PredefinedType="STUD",
                                    ObjectPlacement=w.platzierung(welt, (x - sb / 2, wa["y_kern"], zt + wa["schwelle_h"])),
                                    Representation=w.form(w.body, "SweptSolid", [w.quader(sb, wa["kern_tiefe"], wa["hoehe"] - wa["schwelle_h"] - wa["raehm_h"])])))
    platten = []
    for j, p in enumerate(wa["beplankung"]):
        y = wa["y_kern"] - p["dicke"] if p["seite"] == "sued" else wa["y_kern"] + wa["kern_tiefe"]
        platten.append(w.root("IfcPlate", f"/wand/beplankung/{j}", Name=f"{p['name']} {p['seite']}", PredefinedType="SHEET",
                              ObjectPlacement=w.platzierung(welt, (0.0, y, zt)),
                              Representation=w.form(w.body, "SweptSolid", [w.quader(wa["laenge"], p["dicke"], wa["hoehe"])])))
    wandteile += platten
    w.root("IfcRelAggregates", "/wand#aggregiert", RelatingObject=wand, RelatedObjects=wandteile)
    # Dach: luftdichte OSB-Ebene
    dach = teil("IfcPlate", "/dach/osb", da["beplankung"]["name"], (da["x0"], 0.0, da["z_uk_sparren"] - da["beplankung"]["dicke"]),
                da["laenge"], da["erste_achse_y"] + (da["anzahl"] - 1) * da["achsabstand"] + da["erste_achse_y"],
                da["beplankung"]["dicke"], "DG", PredefinedType="SHEET")
    # Leitung: System, Typ, Segmente, Ports
    system = w.root("IfcDistributionSystem", "/system/SW", Name="Schmutzwasser", PredefinedType="WASTEWATER")
    ptyp = w.root("IfcPipeSegmentType", "/typ/rohr_dn100", Name="Schallschutzrohr DN 100", PredefinedType="RIGIDSEGMENT")
    w.pset([ptyp], "/typ/rohr_dn100", "Pset_PipeSegmentTypeCommon", {
        "NominalDiameter": ("IfcPositiveLengthMeasure", float(L["dn"])),
        "OuterDiameter": ("IfcPositiveLengthMeasure", float(L["da_mm"])),
        "InnerDiameter": ("IfcPositiveLengthMeasure", float(L["di_mm"]))})
    ra = L["da_mm"] / 2
    segs = []
    abschnitte = [("fall_eg", "Fallleitung EG", (x_p, y_p, L["z_fuss"]), (0, 0, 1), L["z_anschluss_wc"] - L["z_fuss"], "EG"),
                  ("lueftung", "Hauptlüftung über Dach", (x_p, y_p, L["z_anschluss_wc"]), (0, 0, 1), L["z_muendung"] - L["z_anschluss_wc"], "OG"),
                  ("anschluss_wc", "WC-Anschlussleitung", (x_p, L["wc"]["y"], L["z_anschluss_wc"]), (0, -1, 0), L["wc"]["y"] - y_p, "OG")]
    for key, name, ursprung, richtung, laenge, gsn in abschnitte:
        seg = w.root("IfcPipeSegment", f"/leitung/{key}", Name=name, PredefinedType="RIGIDSEGMENT",
                     ObjectPlacement=w.platzierung(welt, ursprung, z=richtung, x=(1, 0, 0) if richtung[0] == 0 else (0, 1, 0)),
                     Representation=w.form(w.body, "SweptSolid", [w.zylinder(ra, laenge)]))
        inhalt[gsn].append(seg)
        # Fließrichtung: Wasser fällt (Fallleitung oben SINK, unten SOURCE); WC-Anschluss vom WC (SINK) zum
        # Strang (SOURCE); Lüftung in beide Richtungen.
        richt = {"fall_eg": ("SOURCE", "SINK"), "lueftung": ("SOURCEANDSINK", "SOURCEANDSINK"),
                 "anschluss_wc": ("SINK", "SOURCE")}[key]
        ports = []
        for j, (fl, zpos) in enumerate(zip(richt, (0.0, laenge))):
            ports.append(w.root("IfcDistributionPort", f"/leitung/{key}/port/{j}", Name=f"{name} Port {j}",
                                FlowDirection=fl, PredefinedType="PIPE", SystemType="WASTEWATER",
                                ObjectPlacement=w.platzierung(seg.ObjectPlacement, (0.0, 0.0, zpos))))
        w.root("IfcRelNests", f"/leitung/{key}#ports", RelatingObject=seg, RelatedObjects=ports)
        segs.append((seg, ports))
    # Abzweig 87° am WC-Anschluss (IfcPipeFitting JUNCTION) mit drei Ports
    abzw = w.root("IfcPipeFitting", "/leitung/abzweig", Name="Abzweig DN 100/100 87°", PredefinedType="JUNCTION",
                  ObjectPlacement=w.platzierung(welt, (x_p, y_p, L["z_anschluss_wc"] - ra)),
                  Representation=w.form(w.body, "SweptSolid", [w.zylinder(ra + 5.0, 2 * ra)]))
    inhalt["OG"].append(abzw)
    fports = [w.root("IfcDistributionPort", f"/leitung/abzweig/port/{j}", Name=f"Abzweig Port {j}", FlowDirection=fl,
                     PredefinedType="PIPE", SystemType="WASTEWATER",
                     ObjectPlacement=w.platzierung(abzw.ObjectPlacement, pos))
              for j, (fl, pos) in enumerate((("SINK", (0.0, ra, ra)), ("SOURCE", (0.0, 0.0, 0.0)),
                                              ("SOURCEANDSINK", (0.0, 0.0, 2 * ra))))]
    w.root("IfcRelNests", "/leitung/abzweig#ports", RelatingObject=abzw, RelatedObjects=fports)
    w.root("IfcRelDefinesByType", "/typ/rohr_dn100#typisiert", RelatedObjects=[s for s, _ in segs], RelatingType=ptyp)
    w.root("IfcRelDeclares", "/projekt#deklariert", RelatingContext=f.by_type("IfcProject")[0], RelatedDefinitions=[ptyp])
    w.root("IfcRelAssignsToGroup", "/system/SW#gruppe", RelatedObjects=[s for s, _ in segs] + [abzw], RelatingGroup=system)
    fall, lue, ans = segs
    for j, (a_, b_) in enumerate(((ans[1][1], fports[0]), (fports[1], fall[1][1]), (fports[2], lue[1][0]))):
        w.root("IfcRelConnectsPorts", f"/leitung#verbindung/{j}", RelatingPort=a_, RelatedPort=b_)
    # Schallentkopplung als Umhüllung
    huelle = w.root("IfcCovering", "/leitung/daemmschlauch", Name="Dämmschlauch Schallentkopplung", PredefinedType="WRAPPING",
                    ObjectPlacement=w.platzierung(welt, (x_p, y_p, de["z_uk_balken"] - 50.0)),
                    Representation=w.form(w.body, "SweptSolid", [w.zylinder(ra + daten["entkopplung"]["daemmschlauch_mm"],
                                                                            de["balken_h"] + de["beplankung"]["dicke"] + 100.0)]))
    inhalt["EG"].append(huelle)
    w.root("IfcRelCoversBldgElements", "/leitung/fall_eg#umhuellt", RelatingBuildingElement=segs[0][0], RelatedCoverings=[huelle])

    # Durchdringungen: Provision (TGA) → Öffnung (Holzbau) → Füllung (Manschette)
    def durchbruch(dd, pfad, element, ursprung, achse, tiefe, dia, geschoss, rohr):
        prov = w.root("IfcVirtualElement", pfad + "/provision", Name=f"{dd['id']} Aussparungsvorschlag", PredefinedType="PROVISIONFORVOID",
                      ObjectPlacement=w.platzierung(welt, ursprung, z=achse, x=(1, 0, 0) if achse[0] == 0 else (0, 1, 0)),
                      Representation=w.form(w.body, "SweptSolid", [w.zylinder(dia / 2, tiefe)]))
        w.pset([prov], pfad + "/provision", "Pset_ProvisionForVoid", {
            "VoidShape": "Round", "Diameter": ("IfcPositiveLengthMeasure", float(dia)),
            "Depth": ("IfcPositiveLengthMeasure", float(tiefe)), "System": "Schmutzwasser"})
        inhalt[geschoss].append(prov)
        oe = w.root("IfcOpeningElement", pfad + "/oeffnung", Name=f"{dd['id']} Durchbruch Ø{dia:g}", PredefinedType="OPENING",
                    ObjectPlacement=w.platzierung(element.ObjectPlacement,
                                                  tuple(u - o for u, o in zip(ursprung, element.ObjectPlacement.RelativePlacement.Location.Coordinates)),
                                                  z=achse, x=(1, 0, 0) if achse[0] == 0 else (0, 1, 0)),
                    Representation=w.form(w.body, "SweptSolid", [w.zylinder(dia / 2, tiefe)]))
        w.root("IfcRelVoidsElement", pfad + "#schneidet", RelatingBuildingElement=element, RelatedOpeningElement=oe)
        w.root("IfcRelInterferesElements", pfad + "#durchdringt", RelatingElement=element, RelatedElement=rohr,
               InterferenceType="Durchdringung", ImpliedOrder=True)
        w.pset([oe], pfad + "/oeffnung", "B15_Durchdringung", {"Durchdringung": dd["id"], "Leitung": L["id"],
                                                               "Strategie": erg["strategie"]})
        return oe

    durchbruch(d1, "/durchbruch/D1", osb, (x_p, y_p, de["z_uk_balken"] + de["balken_h"] - 1.0), (0, 0, 1),
               de["beplankung"]["dicke"] + 2.0, d1["oeffnung_d_mm"], "EG", segs[0][0])
    for j, p in enumerate(platten):
        yk = p.ObjectPlacement.RelativePlacement.Location.Coordinates[1]
        durchbruch({**d2, "id": f"D2.{j}"}, f"/durchbruch/D2/{j}", p, (x_p, yk - 1.0, L["z_anschluss_wc"]), (0, 1, 0),
                   wa["beplankung"][j]["dicke"] + 2.0, d2["oeffnung_d_mm"], "OG", segs[2][0])
    oe3 = durchbruch(d3, "/durchbruch/D3", dach, (x_p, y_p, da["z_uk_sparren"] - da["beplankung"]["dicke"] - 1.0), (0, 0, 1),
                     da["beplankung"]["dicke"] + 2.0, d3["oeffnung_d_mm"], "DG", segs[1][0])
    if d3.get("manschette"):
        m = d3["manschette"]
        acc = w.root("IfcDiscreteAccessory", "/durchbruch/D3/manschette", Name=m["name"], PredefinedType="USERDEFINED",
                     ObjectType="Luftdichtheitsmanschette",
                     ObjectPlacement=w.platzierung(welt, (x_p - 100.0, y_p - 100.0, da["z_uk_sparren"] - da["beplankung"]["dicke"] - 1.0)),
                     Representation=w.form(w.body, "SweptSolid", [w.quader(200.0, 200.0, 1.0)]))
        inhalt["DG"].append(acc)
        w.root("IfcRelFillsElement", "/durchbruch/D3#gefuellt", RelatingOpeningElement=oe3, RelatedBuildingElement=acc)
        w.pset([acc], "/durchbruch/D3/manschette", "B15_Manschette", {"Norm": "DIN 4108-7", "DurchmesserMin": float(m["d_min"]),
                                                                       "DurchmesserMax": float(m["d_max"])})
    for gsn, liste in inhalt.items():
        if liste:
            w.root("IfcRelContainedInSpatialStructure", f"/projekt/gebaeude/{gsn}#enthaelt",
                   RelatingStructure=gs[gsn], RelatedElements=liste)
    w.root("IfcRelServicesBuildings", "/system/SW#versorgt", RelatingSystem=system,
           RelatedBuildings=[f.by_type("IfcBuilding")[0]])
    return w


# ---------------------------------------------------------------------------
# 5. BTLx-artige Bearbeitungsliste (Rückverfolgung zur Leitung)
# ---------------------------------------------------------------------------

def schreibe_btlx(daten: dict, erg: dict, pfad: Path, leitungs_guid: str) -> Path:
    ET.register_namespace("", NS_BTLX)
    q = lambda t: f"{{{NS_BTLX}}}{t}"
    root = ET.Element(q("BTLx"), {"Version": "2.1.0", "Language": "de"})
    fh = ET.SubElement(root, q("FileHistory"))
    ET.SubElement(fh, q("InitialExportProgram"), {"CompanyName": daten["projekt"]["organisation"], "ProgramName": "b15_durchdringungen",
                                                  "ProgramVersion": "0.1", "ExportDate": daten["projekt"]["zeitstempel"][:10],
                                                  "ExportTime": daten["projekt"]["zeitstempel"][11:19]})
    pj = ET.SubElement(root, q("Project"), {"Name": daten["projekt"]["name"]})
    parts = ET.SubElement(pj, q("Parts"))
    for n, fa in enumerate(erg["fertigung"], start=1):
        part = ET.SubElement(parts, q("Part"), {"SingleMemberNumber": str(n), "Designation": fa["bauteil"], "Count": "1"})
        proc = ET.SubElement(part, q("Processings"))
        dr = ET.SubElement(proc, q("Drilling"), {"Name": f"Durchdringung {fa['durchdringung']}", "Process": "yes",
                                                  "ReferencePlaneID": "1"})
        ua = ET.SubElement(dr, q("UserAttributes"))
        for k, v in (("LeitungGUID", leitungs_guid), ("Durchdringung", fa["durchdringung"]), ("Anlage", fa["anlage"])):
            ET.SubElement(ua, q("UserAttribute"), {"Name": k}).text = v
        for k, v in (("StartX", fa["start_x"]), ("StartY", fa["start_y"]), ("Angle", 0.0),
                     ("Inclination", 90.0), ("DepthLimited", "no"), ("Depth", 0.0), ("Diameter", fa["d_mm"])):
            ET.SubElement(dr, q(k)).text = v if isinstance(v, str) else f"{float(v):.3f}"
    ET.indent(root)
    pfad.parent.mkdir(parents=True, exist_ok=True)
    ET.ElementTree(root).write(pfad, encoding="utf-8", xml_declaration=True)
    return pfad


def lade_eingabe(pfad: Path | str = STANDARD_EINGABE) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def main() -> None:
    ap = argparse.ArgumentParser()
    ap.add_argument("--eingabe", default=str(STANDARD_EINGABE))
    ap.add_argument("--ifc", action="store_true")
    a = ap.parse_args()
    daten = lade_eingabe(a.eingabe)
    erg = plane(daten)
    AUSGABE.mkdir(exist_ok=True)
    (AUSGABE / "b15_durchdringungen.json").write_text(json.dumps(erg, ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"Leitung {erg['leitung']}: Öffnung Decke/Wand Ø {erg['oeffnung_decke_wand_mm']:g} mm, Dach Ø {erg['oeffnung_dach_mm']:g} mm, "
          f"Achse x = {erg['achse_x_mm']:g} mm, Strategie: {erg['strategie']}")
    for dd in erg["durchdringungen"]:
        print(f"\n{dd['id']} {dd.get('art', dd.get('bezeichnung'))}: {dd.get('einstufung', '')}")
        for mm in dd.get("massnahmen", []):
            print("   Maßnahme: " + mm)
        for v in dd.get("verstoesse", []):
            print("   VERSTOSS: " + v)
        for h in dd.get("hinweise", []):
            print("   Hinweis: " + h)
        if "brandschutz" in dd:
            print("   Brandschutz: " + dd["brandschutz"]["grund"])
    for h in erg["hinweise"]:
        print("Hinweis: " + h)
    if a.ifc:
        import ifcopenshell.validate
        w = erzeuge_ifc(daten, erg)
        pfad = w.schreibe(AUSGABE / "b15_durchdringungen.ifc")
        log = ifcopenshell.validate.json_logger()
        ifcopenshell.validate.validate(str(pfad), log, express_rules=True)
        print(f"\nIFC {pfad.name}: {len(log.statements)} Validierungsfehler")
        guid = w.f.by_type("IfcPipeSegment")[0].GlobalId
        print("BTLx:", schreibe_btlx(daten, erg, AUSGABE / "b15_bearbeitungen.btlx", guid).name)


if __name__ == "__main__":
    main()

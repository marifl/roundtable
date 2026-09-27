#!/usr/bin/env python3
"""
B14 – Fußbodenaufbau und Höhenausgleich: gleiche Fertigfußbodenhöhe (OKFF)
je Geschoss bei unterschiedlichen Belägen, raumweise berechnet.

Eingabe:  daten/b14_fussbodenaufbau.json (Kataloge, 4 Räume, 2 Varianten)
Ausgabe:  ausgabe/b14_<variante>.json   (Schichtenfolge, Nachweise, Verstöße)
          ausgabe/b14_<variante>.ifc    (IFC4X3_ADD2, optional mit --ifc)

ALLE Zahlen im JSON sind BEISPIELWERTE. Normwerte stehen dort nur als
einzelne Kennwerte mit Normverweis (DIN 18560-2, DIN EN 1264, DIN 18202,
DIN 18040-2, DIN 18534, GModG Anlage 8), Herstellerwerte sind markiert.

Rechenweg (siehe Recherche 16, Abschnitt 4):

  Gegeben je Raum: OK Rohdecke (= 0), Ziel-Aufbauhöhe H (gleich für alle
  Räume des Geschosses), Belag b, Leitungen im Aufbau, Dusche, FBH.
  Gesucht: Schichtenfolge (Material, Dicke) von unten nach oben.

  1. Diskrete Wahl (Aufzählung): welche optionalen Schichten aktiv sind und
     welche Handelsdicke Platten haben (Dämmung in Handelsdicken, Wabe 30/60,
     Wärmedämmung bis 2 Lagen).
  2. Stetige Wahl (je diskreter Kombination exakt gelöst): nivellierende
     Schichten (Schüttung, Fließestrich, Mittelbett, Spachtel) und
     Verlegewerkstoff haben Dicken im Bereich [lo, hi]. Die Summe muss die
     Resthöhe R = H - Σ feste Schichten treffen. Weil Ziel und Nebenbedingung
     linear sind, ist die Lösung ein "Füllen nach Stückkosten": alle auf lo,
     dann Rest in die Schicht mit den geringsten Kosten je mm (Masse und Geld
     gewichtet), bis hi, dann die nächste. Das ist das exakte Optimum des
     kontinuierlichen Teilproblems (Rucksack mit teilbaren Gütern), auf ganze
     mm gerundet.
  3. Harte Nebenbedingungen (Kandidat verworfen): Estrich-Mindestdicke mit
     Rohrüberdeckung, Gefälle und Rohdeckentoleranz; Leitungen überdeckt bzw.
     Dämmplatten bündig; Σ Zusammendrückbarkeit; U-Wert; R_ins unter FBH;
     Flächenmasse; Beschwerung; Toleranzkette über dem Nivellierhorizont
     <= okff_toleranz_mm; Trockenestrich nur mit Ausgleichsschicht.
  4. Ziel: min w_m·Masse + w_k·Kosten + w_l·Lagenzahl; Gleichstand wird über
     die Textdarstellung der Kombination aufgelöst (deterministisch).
  5. Weiche Regeln (werden gemeldet, Kandidat bleibt): Belag-Untergrund-
     Eignung, R_λ,B <= 0,15 m²K/W, Gefälle <= 2 cm, Rinneneinbauhöhe,
     Übergänge, Belegreife.
  6. Ist kein Kandidat zulässig, wird der Konflikt erklärt: erreichbare
     Aufbauhöhen [H_min, H_max] und die häufigsten Ausschlussgründe.

Aufruf:   python b14_fussbodenaufbau.py [--variante A_bodenplatte_nass] [--ifc]
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
import uuid
from collections import Counter
from dataclasses import dataclass, field
from pathlib import Path

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b14_fussbodenaufbau.json"
AUSGABE = HIER / "ausgabe"

# Fester Namensraum für uuid5 (selbst gewählt, einmalig erzeugt und fixiert).
GUID_NAMENSRAUM = uuid.UUID("3b8e2c41-7d0a-5f19-b6e4-90c2a1d57e33")


# ---------------------------------------------------------------------------
# 0. GModG Anlage 8 (Leitungsdämmung) – auch von B15 genutzt
# ---------------------------------------------------------------------------

def gmodg_mindestdaemmung(leitung: dict, lage: str = "fussboden_ein_nutzer") -> tuple[float | None, str]:
    """Mindestdämmdicke nach GModG Anlage 8 Nr. 1 (bezogen auf λ = 0,035
    W/(m K)); Rückgabe (mm oder None, Begründung).

    lage: "fussboden_ein_nutzer" (Bauteil zwischen beheizten Räumen eines
    Nutzers), "fussboden_verschiedene_nutzer", "durchbruch", "frei".
    Nur Wärmeverteilungs- und Warmwasserleitungen fallen unter Nr. 1;
    Kaltwasser und Abwasser haben keine GModG-Anforderung (Schutz nach
    DIN 1988-200 bzw. Tauwasser: privatrechtlich/aaRdT)."""
    medium = leitung.get("medium")
    if medium not in ("heizung", "trinkwasser_warm", "zirkulation"):
        return None, "keine Anforderung nach GModG Anlage 8 (nur Wärmeverteilung/Warmwasser)"
    di = float(leitung["di_mm"])
    if di <= 22:
        basis = 20.0
    elif di <= 35:
        basis = 30.0
    elif di <= 100:
        basis = di
    else:
        basis = 100.0
    if medium == "trinkwasser_warm" and not leitung.get("zirkulation") and \
            leitung.get("stichleitung_volumen_l", 99) <= 3 and lage != "fussboden_verschiedene_nutzer":
        return 0.0, "Anl. 8 Nr. 1 c: Stichleitung <= 3 l ohne Zirkulation/Begleitheizung in beheizten Räumen – ausgenommen"
    if medium == "heizung" and leitung.get("absperrbar_im_raum") and lage == "fussboden_ein_nutzer":
        return 0.0, "Anl. 8 Nr. 1 b: in beheizten Räumen eines Nutzers mit frei liegender Absperrung – ausgenommen"
    if lage == "durchbruch":
        return basis / 2, "Anl. 8 Nr. 1 ee: Wand-/Deckendurchbruch – halber Wert"
    if lage == "fussboden_verschiedene_nutzer":
        if medium == "heizung":
            return 6.0, "Anl. 8 Nr. 1 gg: Wärmeverteilung im Fußbodenaufbau zwischen Nutzern – 6 mm"
        return basis / 2, "Anl. 8 Nr. 1 ff: zwischen beheizten Räumen verschiedener Nutzer – halber Wert"
    return basis, f"Anl. 8 Nr. 1 aa–dd: di = {di:g} mm – {basis:g} mm"


def leitungshoehe(l: dict) -> float:
    """Benötigte Höhe einer Leitung im Aufbau: Außendurchmesser + 2 × Dämmung
    + Höhenzuwachs aus Gefälle (Schwerkraftleitungen)."""
    h = float(l["da_mm"]) + 2 * float(l.get("daemmung_mm", 0))
    if l.get("gefaelle_prozent"):
        h += float(l["laenge_m"]) * 1000 * float(l["gefaelle_prozent"]) / 100
    return h


def leitungsbreite(ls: list[dict], abstand: float = 20.0) -> float:
    return sum(float(l["da_mm"]) + 2 * float(l.get("daemmung_mm", 0)) for l in ls) + abstand * max(0, len(ls) - 1)


# ---------------------------------------------------------------------------
# 1. Datenmodell
# ---------------------------------------------------------------------------

@dataclass
class Schicht:
    rolle: str
    material: str
    dicke: float
    stetig: bool = False          # Dicke wird im Schritt 2 gelöst
    lo: float = 0.0
    hi: float = 0.0
    c_mm: float = 0.0             # Zusammendrückbarkeit (in dicke schon abgezogen)

    def kurz(self) -> str:
        return f"{self.rolle}:{self.material}:{self.dicke:g}" + ("s" if self.stetig else "")


@dataclass
class Ergebnis:
    raum: dict
    schichten: list[Schicht] = field(default_factory=list)
    estrich: str = ""
    kennwerte: dict = field(default_factory=dict)
    verstoesse: list[str] = field(default_factory=list)
    hinweise: list[str] = field(default_factory=list)
    zulaessig: bool = True
    diagnose: dict = field(default_factory=dict)


def lade_eingabe(pfad: Path | str = STANDARD_EINGABE) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


# ---------------------------------------------------------------------------
# 2. Kandidatenerzeugung
# ---------------------------------------------------------------------------

def _slot_optionen(slot: dict, mat: dict) -> list[list[Schicht]]:
    """Alle Belegungen eines Schicht-Slots als Liste von Schichtlisten
    (leer = Slot nicht belegt)."""
    aus: list[list[Schicht]] = [] if slot.get("pflicht") else [[]]
    for opt in slot["optionen"]:
        m = mat[opt["material"]]
        c = float(m.get("c_mm", 0))
        if "bereich" in opt:
            lo, hi = opt["bereich"]
            aus.append([Schicht(slot["rolle"], opt["material"], float(lo), True, float(lo), float(hi))])
            continue
        dicken = [float(d) for d in opt["dicken"]]
        einzel = [[Schicht(slot["rolle"], opt["material"], d - c, c_mm=c)] for d in dicken]
        aus.extend(einzel)
        if opt.get("lagen_max", 1) >= 2:
            for d1, d2 in itertools.combinations_with_replacement(dicken, 2):
                aus.append([Schicht(slot["rolle"], opt["material"], d1 - c, c_mm=c),
                            Schicht(slot["rolle"], opt["material"], d2 - c, c_mm=c)])
    return aus


def _estrich_waehlen(raum: dict, var: dict, est: dict) -> tuple[str, list[str]]:
    hinweise = []
    key = var["estrich_standard"]
    if raum.get("dusche", {}).get("bodengleich") and not est[key]["feuchteunempfindlich"]:
        neu = var["estrich_gefaellebereich"]
        hinweise.append(
            f"Estrich im Bad {est[key]['name']} → {est[neu]['name']}: Gefälleflächen mit feuchteunempfindlichem "
            "Estrich (IGG-Merkblatt 5 Holz-/Trockenbau; DIN 18534-1 W2-I). Estrichwechsel an der Badtür = "
            "Bewegungsfuge (DIN 18560-2 6.3.3).")
        key = neu
    return key, hinweise


def _stack(raum: dict, var: dict, daten: dict, wahl: tuple, estrich_key: str) -> list[Schicht]:
    """Schichtenfolge unten → oben (Rohdecke ausgenommen) für eine Wahl."""
    mat, est, bel = daten["materialien"], daten["estriche"], daten["belaege"][raum["belag"]]
    unten, oben = wahl
    s: list[Schicht] = [copy.copy(x) for grp in unten for x in grp]
    e = est[estrich_key]
    if e["art"] == "nass":
        s.append(Schicht("estrich", e["material"], 0.0, True, 0.0, 0.0))
    else:
        s.append(Schicht("estrich", e["material"], float(e["dicke_mm"])))
    s.extend(copy.copy(x) for grp in oben for x in grp)
    if raum.get("dusche", {}).get("bodengleich"):
        s.append(Schicht("abdichtung_aiv", "aiv_mineralisch", 2.0))
    vw = bel["verlegewerkstoff"]
    if vw["max_mm"] > vw["nenn_mm"]:
        s.append(Schicht("verlegewerkstoff", vw["material"], float(vw["nenn_mm"]), True,
                         float(vw["nenn_mm"]), float(vw["max_mm"])))
    else:
        s.append(Schicht("verlegewerkstoff", vw["material"], float(vw["nenn_mm"])))
    s.append(Schicht("belag", bel["material"], float(bel["dicke_mm"])))
    return s


# ---------------------------------------------------------------------------
# 3. Bewertung eines Kandidaten
# ---------------------------------------------------------------------------

class Verworfen(Exception):
    pass


def _gefaelle_mm(raum: dict) -> float:
    d = raum.get("dusche") or {}
    if not d.get("bodengleich"):
        return 0.0
    return round(d["gefaelle_prozent"] / 100 * d["gefaelle_laenge_m"] * 1000, 1)


def _loese_stetig(s: list[Schicht], rest: float, mat: dict, gew: dict) -> None:
    """Schritt 2: stetige Schichten füllen (exakt, lineares Teilproblem)."""
    stetig = [x for x in s if x.stetig]
    for x in stetig:
        x.dicke = x.lo
    fehl = rest - sum(x.lo for x in stetig)
    if fehl < -1e-9:
        raise Verworfen("hoehe_zu_gross")
    def stueckkosten(i_x):
        i, x = i_x
        m = mat[x.material]
        return (gew["masse"] * m["rho"] / 1000 + gew["kosten"] * m["kosten_mm"], i)
    for _, x in sorted(enumerate(stetig), key=stueckkosten):
        mehr = min(fehl, x.hi - x.lo)
        x.dicke = x.lo + mehr
        fehl -= mehr
    if fehl > 1e-9:
        raise Verworfen("hoehe_zu_klein")


def bewerte(raum: dict, var: dict, daten: dict, wahl: tuple, estrich_key: str,
            mit_ziel: bool = True) -> Ergebnis:
    mat, est = daten["materialien"], daten["estriche"]
    bel = daten["belaege"][raum["belag"]]
    rd, fbh, gr = var["rohdecke"], var["fbh"], var["grenzen"]
    e = est[estrich_key]
    s = _stack(raum, var, daten, wahl, estrich_key)
    t_rd = float(rd["ebenheit_toleranz_mm"])
    dh = _gefaelle_mm(raum)
    res = Ergebnis(raum=raum, estrich=estrich_key)

    # --- Leitungen im Aufbau ---------------------------------------------
    im_aufbau = [l for l in raum.get("leitungen", []) if l.get("fuehrung") == "im_aufbau"]
    h_leit = max((leitungshoehe(l) for l in im_aufbau), default=0.0)
    if im_aufbau:
        traeger = None
        for x in s:
            m = mat[x.material]
            if x.rolle == "installationsebene":
                traeger = x
                break
            if x.rolle == "beschwerung" and "nimmt_leitungen_auf" in m and x.dicke >= h_leit \
                    and leitungsbreite(im_aufbau) <= m["nimmt_leitungen_auf"]["max_breite_mm"]:
                traeger = x
                break
        if traeger is None:
            raise Verworfen("leitungen_ohne_installationsebene")
        m = mat[traeger.material]
        if traeger.stetig:
            traeger.lo = max(traeger.lo, math.ceil(h_leit + m.get("ueberdeckung_leitung_mm", 0)))
            if traeger.lo > traeger.hi:
                raise Verworfen("installationsebene_zu_duenn")
        elif traeger.rolle == "installationsebene":
            # Dämmplatten als Ausgleich: bündig zu den Leitungen, höchstens 2 Höhen (DIN 18560-2:2022 5.2)
            hoehen = sorted({round(leitungshoehe(l)) for l in im_aufbau})
            if len(hoehen) > 2:
                raise Verworfen("daemmplatten_mehr_als_2_hoehen")
            if not (h_leit <= traeger.dicke <= h_leit + gr["buendig_toleranz_mm"]):
                raise Verworfen("daemmplatte_nicht_buendig")

    # --- Estrich-Mindestdicke --------------------------------------------
    est_s = next(x for x in s if x.rolle == "estrich")
    if e["art"] == "nass":
        e_min = float(e["nenndicke_min_mm"])
        c_sum = sum(x.c_mm for x in s)
        if fbh["aktiv"] and fbh["system"] == "nass_A":
            d = float(fbh["rohr_da_mm"])
            e_min = max(e_min + d, d + float(e["rohrueberdeckung_min_mm"]))
            if c_sum > gr["summe_c_max_mm"]:
                raise Verworfen("zusammendrueckbarkeit_heizestrich")
        elif c_sum > 5:
            e_min += 5  # DIN 18560-2: Zusammendrückbarkeit > 5 mm → Nenndicke + 5 mm
        e_req = e_min + dh
        est_s.lo = e_req
        est_s.hi = e_min + float(e["mehrdicke_max_mm"]) + dh
        res.kennwerte["estrich_nenndicke_min_mm"] = e_min
    # --- Toleranzausgleich der Rohdecke ----------------------------------
    niv_unten = [x for x in s if mat[x.material]["nivellierend"]]
    if not niv_unten:
        raise Verworfen("kein_toleranzausgleich")
    tiefste = niv_unten[0]
    if tiefste.rolle == "estrich" and not var.get("toleranz_im_estrich_anrechnen", True):
        pass
    elif tiefste.stetig:
        tiefste.lo += t_rd
        if tiefste.lo > tiefste.hi:
            raise Verworfen("toleranzausgleich_zu_duenn")
    # Trockenestrich: vollflächige Auflage – nivellierende Schicht unterhalb nötig
    if e["art"] == "trocken":
        idx_e = s.index(est_s)
        if not any(mat[x.material]["nivellierend"] for x in s[:idx_e]):
            raise Verworfen("trockenestrich_ohne_ausgleich")

    # --- Stetige Dicken lösen --------------------------------------------
    H = float(var["ziel_aufbauhoehe_mm"])
    fest = sum(x.dicke for x in s if not x.stetig)
    if mit_ziel:
        _loese_stetig(s, H - fest, mat, var["gewichte"])
        for x in s:
            if x.stetig:
                x.dicke = float(round(x.dicke))
        if abs(sum(x.dicke for x in s) - H) > 1e-6:
            raise Verworfen("rundung")
    else:
        res.kennwerte["h_bereich"] = (fest + sum(x.lo for x in s if x.stetig),
                                      fest + sum(x.hi for x in s if x.stetig))

    res.schichten = s
    # --- Kennwerte --------------------------------------------------------
    masse = sum(mat[x.material]["rho"] * x.dicke / 1000 for x in s)
    kosten = sum(mat[x.material]["kosten_fix"] + mat[x.material]["kosten_mm"] * x.dicke for x in s if x.dicke > 0)
    res.kennwerte.update({"aufbauhoehe_mm": sum(x.dicke for x in s), "flaechenmasse_kg_m2": round(masse, 2),
                          "kosten_eur_m2_beispiel": round(kosten, 2), "lagen": len([x for x in s if x.dicke > 0])})
    idx_e = s.index(est_s)
    # Wärmedurchlasswiderstand des Belags (inkl. Verlegewerkstoff)
    r_b = sum(x.dicke / 1000 / mat[x.material]["lambda"] for x in s if x.rolle in ("belag", "verlegewerkstoff"))
    res.kennwerte["R_lambda_B"] = round(r_b, 4)
    # R_ins unter der Heizebene
    if fbh["aktiv"]:
        grenze = idx_e if fbh["system"] == "nass_A" else next(i for i, x in enumerate(s) if x.rolle == "fbh") + 1
        r_ins = sum(x.dicke / 1000 / mat[x.material]["lambda"] for x in s[:grenze])
        res.kennwerte["R_ins"] = round(r_ins, 3)
        if gr.get("r_ins_min") and r_ins < gr["r_ins_min"]:
            raise Verworfen("r_ins_zu_klein")
    # U-Wert gegen Erdreich (vereinfachend: Rsi 0,17, Rse 0, ohne DIN EN ISO 13370)
    if rd["unten"] == "erdreich" and gr.get("u_wert_max"):
        r = 0.17 + rd["dicke_mm"] / 1000 / rd["lambda"] + sum(x.dicke / 1000 / mat[x.material]["lambda"] for x in s)
        u = 1 / r
        res.kennwerte["U_W_m2K"] = round(u, 3)
        if u > gr["u_wert_max"]:
            raise Verworfen("u_wert")
    if gr.get("max_flaechenmasse_kg_m2") and masse > gr["max_flaechenmasse_kg_m2"]:
        raise Verworfen("flaechenmasse")
    if gr.get("masse_unter_trittschall_min_kg_m2"):
        i_t = next(i for i, x in enumerate(s) if x.rolle == "trittschall")
        m_b = sum(mat[x.material]["rho"] * x.dicke / 1000 for x in s[:i_t])
        res.kennwerte["beschwerung_kg_m2"] = round(m_b, 2)
        if m_b < gr["masse_unter_trittschall_min_kg_m2"]:
            raise Verworfen("beschwerung")
    # Toleranzkette über dem Nivellierhorizont
    i_h = max(i for i, x in enumerate(s) if mat[x.material]["nivellierend"])
    tol = sum(mat[x.material]["toleranz_mm"] for x in s[i_h + 1:])
    res.kennwerte["toleranz_ueber_nivellierhorizont_mm"] = round(tol, 2)
    res.kennwerte["nivellierhorizont"] = s[i_h].rolle
    if tol > daten["okff_toleranz_mm"]:
        raise Verworfen("toleranzkette")
    if e["art"] == "nass":
        res.kennwerte["estrich_tiefpunkt_mm"] = est_s.dicke - dh
    res.kennwerte["gefaelle_mm"] = dh
    res.kennwerte["leitungshoehe_mm"] = h_leit
    return res


def zielwert(res: Ergebnis, gew: dict) -> float:
    k = res.kennwerte
    return gew["masse"] * k["flaechenmasse_kg_m2"] + gew["kosten"] * k["kosten_eur_m2_beispiel"] + gew["lagen"] * k["lagen"]


# ---------------------------------------------------------------------------
# 4. Raumweise Optimierung
# ---------------------------------------------------------------------------

def optimiere_raum(raum: dict, var: dict, daten: dict) -> Ergebnis:
    mat = daten["materialien"]
    estrich_key, hinw = _estrich_waehlen(raum, var, daten["estriche"])
    unten_opts = [_slot_optionen(sl, mat) for sl in var["schichten"]]
    oben_opts = [_slot_optionen(sl, mat) for sl in var.get("oberhalb_estrich", [])]
    beste, bester_wert, gruende = None, None, Counter()
    bereich = [math.inf, -math.inf]
    for unten in itertools.product(*unten_opts):
        for oben in itertools.product(*oben_opts):
            wahl = (unten, oben)
            try:
                r = bewerte(raum, var, daten, wahl, estrich_key)
            except Verworfen as ex:
                gruende[str(ex)] += 1
                try:  # erreichbare Höhe dieser Kombination (für die Diagnose)
                    r0 = bewerte(raum, var, daten, wahl, estrich_key, mit_ziel=False)
                    lo, hi = r0.kennwerte["h_bereich"]
                    bereich = [min(bereich[0], lo), max(bereich[1], hi)]
                except Verworfen:
                    pass
                continue
            w = (round(zielwert(r, var["gewichte"]), 6), " | ".join(x.kurz() for x in r.schichten))
            if bester_wert is None or w < bester_wert:
                beste, bester_wert = r, w
    if beste is None:
        res = Ergebnis(raum=raum, estrich=estrich_key, zulaessig=False)
        H = var["ziel_aufbauhoehe_mm"]
        text = f"Kein zulässiger Aufbau für H = {H} mm."
        if bereich[0] < math.inf:
            if H < bereich[0]:
                text += f" Mindestens erreichbar: {bereich[0]:g} mm (fehlen {bereich[0] - H:g} mm)."
            elif H > bereich[1]:
                text += f" Höchstens erreichbar: {bereich[1]:g} mm (zu hoch um {H - bereich[1]:g} mm)."
        haeufig = ", ".join(f"{g} ({n}×)" for g, n in sorted(gruende.items(), key=lambda kv: (-kv[1], kv[0]))[:4])
        res.verstoesse.append(text + " Häufigste Ausschlussgründe: " + haeufig)
        res.diagnose = {"h_erreichbar_mm": bereich if bereich[0] < math.inf else None, "gruende": dict(gruende)}
        res.hinweise.extend(hinw)
        return res
    beste.hinweise.extend(hinw)
    beste.kennwerte["zielwert"] = bester_wert[0]
    beste.kennwerte["kandidaten_verworfen"] = dict(sorted(gruende.items()))
    weiche_regeln(beste, var, daten)
    return beste


def weiche_regeln(res: Ergebnis, var: dict, daten: dict) -> None:
    raum, mat, est = res.raum, daten["materialien"], daten["estriche"]
    bel = daten["belaege"][raum["belag"]]
    e = est[res.estrich]
    bm = e["bindemittel"]
    if bm in bel["untergrund_zulaessig"]:
        pass
    elif bm in bel["untergrund_mit_freigabe"]:
        res.hinweise.append(f"{bel['name']} auf {e['name']}: nur mit Herstellerfreigabe (System, Format, Armierung).")
    else:
        res.verstoesse.append(f"{bel['name']} auf {e['name']} nicht zulässig (Untergrund {bm}).")
    k = res.kennwerte
    if var["fbh"]["aktiv"] and k["R_lambda_B"] > 0.15:
        res.verstoesse.append(f"R_λ,B = {k['R_lambda_B']:.3f} m²K/W > 0,15 (DIN EN 1264, Belag inkl. Unterlage).")
    if raum.get("dusche", {}).get("bodengleich"):
        d = raum["dusche"]
        if k["gefaelle_mm"] > 20:
            res.verstoesse.append(f"Absenkung Duschplatz {k['gefaelle_mm']:g} mm > 20 mm (DIN 18040-2 5.5.5).")
        rinne = daten["rinnen"][d["rinne"]]
        z_est = sum(x.dicke for x in res.schichten[: res.schichten.index(next(x for x in res.schichten if x.rolle == 'estrich')) + 1])
        h_einlauf = z_est - k["gefaelle_mm"]
        k["estrichhoehe_am_einlauf_mm"] = h_einlauf
        if h_einlauf < rinne["estrichhoehe_min_mm"]:
            fehl = rinne["estrichhoehe_min_mm"] - h_einlauf
            if var["rohdecke"]["typ"] == "holzbalkendecke":
                res.hinweise.append(
                    f"Rinne braucht {rinne['estrichhoehe_min_mm']} mm Estrichhöhe am Einlauf, vorhanden {h_einlauf:g} mm: "
                    f"Ablaufkörper {fehl:g} mm in die Balkenlage absenken → Deckendurchbruch/Wechsel prüfen (B15).")
            else:
                res.verstoesse.append(
                    f"Rinne braucht {rinne['estrichhoehe_min_mm']} mm am Einlauf, vorhanden {h_einlauf:g} mm: "
                    f"Aussparung {fehl:g} mm in der Bodenplatte im Rohbau einplanen oder flache Rinne wählen.")
        elif h_einlauf > rinne["estrichhoehe_max_mm"]:
            res.hinweise.append(f"Einlaufhöhe {h_einlauf:g} mm > {rinne['estrichhoehe_max_mm']} mm: Verlängerung/anderes Rohbauset.")
        res.hinweise.append("Duschbereich W2-I (DIN 18534-1): Verbundabdichtung, am Boden keine Dispersionsabdichtung (DIN 18534-3); "
                            "Rückstau nur 5–10 l aufnehmbar → keine Schwelle (DIN 18040-2 ≤ 2 cm), Gefälle weg von der Tür.")
        if e["art"] == "trocken":
            res.hinweise.append("Gefälle im Trockenbau über Herstellersystem (vorgefertigtes Gefälle-Element); "
                                "Einbauhöhe laut Hersteller prüfen.")
    for l in raum.get("leitungen", []):
        mind, grund = gmodg_mindestdaemmung(l)
        if mind is not None and float(l.get("daemmung_mm", 0)) < mind:
            res.verstoesse.append(f"{l['bezeichnung']}: Dämmung {l.get('daemmung_mm', 0)} mm < {mind:g} mm ({grund}).")
        elif mind is not None:
            res.hinweise.append(f"{l['bezeichnung']}: {grund}.")
        if l.get("fuehrung") == "unter_rohdecke":
            res.hinweise.append(f"{l['bezeichnung']}: {var.get('abwasser_fuehrung_hinweis', 'unter der Rohdecke')}.")
    # Belegreife
    if e["art"] == "nass":
        g = daten["cm_grenzwerte"][bel["cm_gruppe"]][bm]
        k["belegreife_cm_max"] = g[1] if var["fbh"]["aktiv"] else g[0]
    else:
        k["belegreife_cm_max"] = None
        res.hinweise.append("Trockenestrich: keine CM-Belegreife; Materialfeuchte nach Herstellerangabe.")
    if var["rohdecke"]["typ"] == "holzbalkendecke" and e["art"] == "nass":
        res.hinweise.append("Nassestrich auf Holzbalkendecke: Baufeuchte und Trocknungszeit (Holzfeuchte, Werksplanung).")


# ---------------------------------------------------------------------------
# 5. Geschoss: Nachweis gleiche OKFF und Übergänge
# ---------------------------------------------------------------------------

def berechne_variante(daten: dict, variante: str) -> dict:
    var = daten["varianten"][variante]
    ergebnisse = [optimiere_raum(r, var, daten) for r in daten["raeume"]]
    H = float(var["ziel_aufbauhoehe_mm"])
    tol_max = float(daten["okff_toleranz_mm"])
    raeume_out, alle_ok = [], True
    for res in ergebnisse:
        z, lagen = 0.0, []
        for x in res.schichten:
            if x.dicke <= 0:
                continue
            lagen.append({"rolle": x.rolle, "material": x.material, "name": daten["materialien"][x.material]["name"],
                          "dicke_mm": x.dicke, "uk_mm": z, "ok_mm": z + x.dicke})
            z += x.dicke
        okff = z if res.zulaessig else None
        tol = res.kennwerte.get("toleranz_ueber_nivellierhorizont_mm")
        ok = res.zulaessig and abs(okff - H) + tol <= tol_max + 1e-9
        alle_ok &= ok
        raeume_out.append({
            "id": res.raum["id"], "name": res.raum["name"], "belag": res.raum["belag"], "estrich": res.estrich,
            "zulaessig": res.zulaessig, "okff_mm": okff, "okff_toleranz_mm": tol, "nachweis_okff": ok,
            "schichten": lagen, "kennwerte": res.kennwerte, "verstoesse": res.verstoesse, "hinweise": res.hinweise,
            "diagnose": res.diagnose})
    per_id = {r["id"]: r for r in raeume_out}
    uebergaenge = []
    for u in daten["uebergaenge"]:
        a, b = per_id[u["a"]], per_id[u["b"]]
        eintrag = {"a": a["name"], "b": b["name"], "art": u["art"], "hinweise": [], "verstoesse": []}
        if a["okff_mm"] is None or b["okff_mm"] is None:
            eintrag["verstoesse"].append("Übergang nicht bewertbar (Raum ohne zulässigen Aufbau).")
        else:
            delta = a["okff_mm"] - b["okff_mm"]
            kante = abs(delta) + a["okff_toleranz_mm"] + b["okff_toleranz_mm"]
            eintrag.update({"delta_okff_mm": delta, "kante_worst_case_mm": round(kante, 2)})
            if kante > tol_max + 1e-9:
                eintrag["verstoesse"].append(f"mögliche Kante {kante:.1f} mm > {tol_max:g} mm (Stolperkante).")
            bel_a, bel_b = daten["belaege"][a["belag"]], daten["belaege"][b["belag"]]
            fuge = a["estrich"] != b["estrich"] or "Tuer" in u["art"]
            if fuge:
                eintrag["hinweise"].append("Estrichfeldgrenze → Bewegungsfuge durch Estrich und Belag (DIN 18560-2 6.3.3).")
                for bel in (bel_a, bel_b):
                    if not bel["ueberbrueckt_bewegungsfugen"]:
                        eintrag["hinweise"].append(f"{bel['name']}: Fuge im Belag übernehmen → höhengleiches Fugenprofil.")
            elif a["belag"] != b["belag"]:
                eintrag["hinweise"].append("Belagwechsel ohne Estrichfuge: höhengleiche Trennschiene/elastische Fuge "
                                           "(Parkett-Randfuge).")
            if "Bad" in u["art"]:
                eintrag["hinweise"].append("Badtür: schwellenlos (DIN 18040-2 ≤ 2 cm); Abdichtung W2-I in die Türleibung "
                                           "und Gefälle weg von der Tür.")
        uebergaenge.append(eintrag)
    alle_ok &= all(not u["verstoesse"] for u in uebergaenge)
    return {"variante": variante, "name": var["name"], "geschoss": var["geschoss"], "rohdecke": var["rohdecke"]["name"],
            "ziel_aufbauhoehe_mm": H, "okff_toleranz_mm": tol_max, "nachweis_gleiche_okff": alle_ok,
            "raeume": raeume_out, "uebergaenge": uebergaenge,
            "hinweis": "Alle Kennwerte Beispielwerte; Normwerte nur als Kennwerte mit Verweis (siehe Eingabe-JSON)."}


# ---------------------------------------------------------------------------
# 6. IFC-Ausgabe (IFC4X3_ADD2): IfcSlab + IfcCovering FLOORING je Raum
# ---------------------------------------------------------------------------

class IfcSchreiber:
    """Kleiner deterministischer IFC-Schreiber (auch von B15 genutzt).

    Jede IfcRoot-Instanz bekommt ihre GlobalId aus uuid5(Namensraum, Pfad);
    Beziehungen werden explizit mit Listen angelegt (keine set-Iteration),
    der Header-Zeitstempel kommt aus der Eingabe."""

    def __init__(self, namensraum: uuid.UUID, projekt: dict, dateiname: str):
        import ifcopenshell
        self.ifcopenshell = ifcopenshell
        self.f = ifcopenshell.file(schema="IFC4X3_ADD2")
        self.ns = namensraum
        self.pj = projekt
        self.dateiname = dateiname
        self._pfade: set[str] = set()
        self._mat: dict[str, object] = {}

    def guid(self, pfad: str) -> str:
        if pfad in self._pfade:
            raise ValueError(f"Pfad doppelt: {pfad}")
        self._pfade.add(pfad)
        return self.ifcopenshell.guid.compress(uuid.uuid5(self.ns, pfad).hex)

    def root(self, klasse: str, pfad: str, **attr):
        return self.f.create_entity(klasse, GlobalId=self.guid(pfad), **attr)

    # Geometrie
    def punkt(self, *c):
        return self.f.createIfcCartesianPoint([float(round(v, 3)) for v in c])

    def richtung(self, *c):
        return self.f.createIfcDirection([float(v) for v in c])

    def achse3d(self, ursprung=(0.0, 0.0, 0.0), z=None, x=None):
        return self.f.createIfcAxis2Placement3D(self.punkt(*ursprung), self.richtung(*z) if z else None,
                                                self.richtung(*x) if x else None)

    def platzierung(self, relativ_zu, ursprung=(0.0, 0.0, 0.0), z=None, x=None):
        return self.f.createIfcLocalPlacement(relativ_zu, self.achse3d(ursprung, z, x))

    def quader(self, dx, dy, dz):
        prof = self.f.createIfcRectangleProfileDef(
            "AREA", None, self.f.createIfcAxis2Placement2D(self.f.createIfcCartesianPoint([dx / 2, dy / 2]), None),
            float(dx), float(dy))
        return self.f.createIfcExtrudedAreaSolid(prof, self.achse3d(), self.richtung(0, 0, 1), float(dz))

    def zylinder(self, r, h, ursprung=(0.0, 0.0, 0.0), z=(0, 0, 1)):
        prof = self.f.createIfcCircleProfileDef("AREA", None, None, float(r))
        return self.f.createIfcExtrudedAreaSolid(prof, self.achse3d(ursprung, z, None), self.richtung(0, 0, 1), float(h))

    def form(self, kontext, typ, items):
        rep = self.f.createIfcShapeRepresentation(kontext, kontext.ContextIdentifier, typ, items)
        return self.f.createIfcProductDefinitionShape(None, None, [rep])

    # Merkmale
    def wert(self, v):
        if isinstance(v, tuple):
            return self.f.create_entity(v[0], v[1])
        if isinstance(v, bool):
            return self.f.create_entity("IfcBoolean", v)
        if isinstance(v, int):
            return self.f.create_entity("IfcInteger", v)
        if isinstance(v, float):
            return self.f.create_entity("IfcReal", v)
        s = str(v)
        return self.f.create_entity("IfcText" if len(s) > 255 else "IfcLabel", s)

    def pset(self, objekte: list, pfad: str, name: str, werte: dict):
        props = [self.f.createIfcPropertySingleValue(k, None, self.wert(v), None) for k, v in werte.items() if v is not None]
        ps = self.root("IfcPropertySet", pfad + "#" + name, Name=name, HasProperties=props)
        self.root("IfcRelDefinesByProperties", pfad + "#" + name + "#zuordnung",
                  RelatedObjects=objekte, RelatingPropertyDefinition=ps)
        return ps

    def material(self, key: str, name: str, kategorie: str | None = None):
        if key not in self._mat:
            self._mat[key] = self.f.createIfcMaterial(name, None, kategorie)
        return self._mat[key]

    # Grundgerüst
    def grundgeruest(self, geschosse: list[tuple[str, float]]):
        import ifcopenshell.api.context
        import ifcopenshell.api.unit
        f = self.f
        projekt = self.root("IfcProject", "/projekt", Name=self.pj["name"])
        einheiten = [
            ifcopenshell.api.unit.add_si_unit(f, unit_type="LENGTHUNIT", prefix="MILLI"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="AREAUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="VOLUMEUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="PLANEANGLEUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="MASSUNIT", prefix="KILO"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="THERMODYNAMICTEMPERATUREUNIT"),
        ]
        projekt.UnitsInContext = f.createIfcUnitAssignment(einheiten)
        modell = ifcopenshell.api.context.add_context(f, context_type="Model")
        self.body = ifcopenshell.api.context.add_context(f, context_type="Model", context_identifier="Body",
                                                         target_view="MODEL_VIEW", parent=modell)
        site = self.root("IfcSite", "/projekt/grundstueck", Name="Grundstück", ObjectPlacement=self.platzierung(None))
        geb = self.root("IfcBuilding", "/projekt/gebaeude", Name=self.pj["gebaeude"],
                        ObjectPlacement=self.platzierung(site.ObjectPlacement))
        self.root("IfcRelAggregates", "/projekt#aggregiert", RelatingObject=projekt, RelatedObjects=[site])
        self.root("IfcRelAggregates", "/projekt/grundstueck#aggregiert", RelatingObject=site, RelatedObjects=[geb])
        gs = {}
        for name, z in geschosse:
            gs[name] = self.root("IfcBuildingStorey", f"/projekt/gebaeude/{name}", Name=name, Elevation=float(z),
                                 ObjectPlacement=self.platzierung(geb.ObjectPlacement, (0, 0, z)))
        self.root("IfcRelAggregates", "/projekt/gebaeude#aggregiert", RelatingObject=geb, RelatedObjects=list(gs.values()))
        return projekt, gs

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


def erzeuge_ifc(daten: dict, ergebnis: dict):
    var = daten["varianten"][ergebnis["variante"]]
    w = IfcSchreiber(GUID_NAMENSRAUM, daten["projekt"], f"b14_{ergebnis['variante']}.ifc")
    f = w.f
    _, gs = w.grundgeruest([(var["geschoss"], 0.0)])
    storey = gs[var["geschoss"]]
    rd = var["rohdecke"]
    rx0 = min(r["x0"] for r in daten["raeume"])
    ry0 = min(r["y0"] for r in daten["raeume"])
    rx1 = max(r["x0"] + r["breite"] for r in daten["raeume"])
    ry1 = max(r["y0"] + r["tiefe"] for r in daten["raeume"])
    enthalten = []
    # Rohdecke als IfcSlab mit Schichtaufbau
    slab_typ = "BASESLAB" if rd["typ"] == "bodenplatte" else "FLOOR"
    slab = w.root("IfcSlab", "/rohdecke", Name=rd["name"], PredefinedType=slab_typ,
                  ObjectPlacement=w.platzierung(storey.ObjectPlacement, (rx0, ry0, -rd["dicke_mm"])),
                  Representation=w.form(w.body, "SweptSolid", [w.quader(rx1 - rx0, ry1 - ry0, rd["dicke_mm"])]))
    m_rd = w.material("rohdecke", rd["name"], "Rohdecke")
    ls_rd = f.createIfcMaterialLayerSet([f.createIfcMaterialLayer(m_rd, float(rd["dicke_mm"]), None, "Rohdecke", None, None, None)],
                                        "Rohdecke " + rd["typ"], None)
    use_rd = f.createIfcMaterialLayerSetUsage(ls_rd, "AXIS3", "POSITIVE", 0.0, None)
    w.root("IfcRelAssociatesMaterial", "/rohdecke#material", RelatedObjects=[slab], RelatingMaterial=use_rd)
    w.pset([slab], "/rohdecke", "Pset_SlabCommon", {"LoadBearing": True, "IsExternal": rd["typ"] == "bodenplatte"})
    enthalten.append(slab)
    raeume_ifc = []
    for rj, rr in zip(ergebnis["raeume"], daten["raeume"]):
        pfad = f"/raum/{rr['id']}"
        space = w.root("IfcSpace", pfad, Name=rr["id"], LongName=rr["name"], PredefinedType="INTERNAL",
                       ObjectPlacement=w.platzierung(storey.ObjectPlacement, (rr["x0"], rr["y0"], 0.0)),
                       Representation=w.form(w.body, "SweptSolid", [w.quader(rr["breite"], rr["tiefe"], 2500.0)]))
        raeume_ifc.append(space)
        if not rj["zulaessig"]:
            continue
        h = rj["okff_mm"]
        cov = w.root("IfcCovering", pfad + "/fussbodenaufbau", Name=f"Fußbodenaufbau {rr['name']}",
                     PredefinedType="FLOORING",
                     ObjectPlacement=w.platzierung(storey.ObjectPlacement, (rr["x0"], rr["y0"], 0.0)),
                     Representation=w.form(w.body, "SweptSolid", [w.quader(rr["breite"], rr["tiefe"], h)]))
        lagen = [f.createIfcMaterialLayer(w.material(s["material"], s["name"], daten["materialien"][s["material"]]["kategorie"]),
                                          float(s["dicke_mm"]), None, s["rolle"], None, None, None) for s in rj["schichten"]]
        ls = f.createIfcMaterialLayerSet(lagen, f"FB {rr['id']} {rr['name']}", None)
        use = f.createIfcMaterialLayerSetUsage(ls, "AXIS3", "POSITIVE", 0.0, None)
        w.root("IfcRelAssociatesMaterial", pfad + "/fussbodenaufbau#material", RelatedObjects=[cov], RelatingMaterial=use)
        w.root("IfcRelCoversSpaces", pfad + "#belegt", RelatingSpace=space, RelatedCoverings=[cov])
        k = rj["kennwerte"]
        w.pset([cov], pfad + "/fussbodenaufbau", "Pset_CoveringCommon",
               {"Reference": f"{ergebnis['variante']}/{rr['id']}", "Finish": daten["belaege"][rr["belag"]]["name"]})
        w.pset([cov], pfad + "/fussbodenaufbau", "B14_Fussbodenaufbau", {
            "OKFF": ("IfcLengthMeasure", float(h)), "Estrich": rj["estrich"],
            "Flaechenmasse_kg_m2": float(k["flaechenmasse_kg_m2"]),
            "R_lambda_B": ("IfcThermalResistanceMeasure", float(k["R_lambda_B"])),
            "NachweisOKFF": bool(rj["nachweis_okff"]), "BelegreifeCMmax": k.get("belegreife_cm_max"),
            "Gefaelle": ("IfcLengthMeasure", float(k["gefaelle_mm"])) if k["gefaelle_mm"] else None})
        bel = daten["belaege"][rr["belag"]]
        w.pset([space], pfad, "Pset_SpaceCoveringRequirements", {
            "FloorCovering": bel["name"],
            "FloorCoveringThickness": ("IfcPositiveLengthMeasure", float(bel["dicke_mm"] + bel["verlegewerkstoff"]["nenn_mm"]))})
        enthalten.append(cov)
        d = rr.get("dusche")
        if d and d.get("bodengleich"):
            rinne = daten["rinnen"][d["rinne"]]
            wt = w.root("IfcWasteTerminal", pfad + "/rinne", Name=rinne["name"][:60], PredefinedType="FLOORTRAP",
                        ObjectPlacement=w.platzierung(storey.ObjectPlacement, (d["x"], d["y"], h - k["gefaelle_mm"] - 90.0)),
                        Representation=w.form(w.body, "SweptSolid", [w.quader(800.0, 70.0, 90.0)]))
            w.pset([wt], pfad + "/rinne", "B14_Rinne", {"NennweiteDN": int(rinne["dn"]),
                                                              "Ablaufleistung_l_s": float(rinne["ablaufleistung_l_s"])})
            enthalten.append(wt)
    w.root("IfcRelAggregates", f"/projekt/gebaeude/{var['geschoss']}#raeume", RelatingObject=storey, RelatedObjects=raeume_ifc)
    w.root("IfcRelContainedInSpatialStructure", f"/projekt/gebaeude/{var['geschoss']}#enthaelt",
           RelatingStructure=storey, RelatedElements=enthalten)
    return w


# ---------------------------------------------------------------------------
# 7. Ausgabe
# ---------------------------------------------------------------------------

def bericht_text(e: dict) -> str:
    z = [f"{e['name']} – Ziel-Aufbauhöhe {e['ziel_aufbauhoehe_mm']:g} mm, Nachweis gleiche OKFF: "
         f"{'erfüllt' if e['nachweis_gleiche_okff'] else 'NICHT erfüllt'}"]
    for r in e["raeume"]:
        k = r["kennwerte"]
        z.append(f"\n{r['name']} ({r['belag']}, Estrich {r['estrich']}): OKFF {r['okff_mm']} mm ± {r['okff_toleranz_mm']} mm")
        for s in reversed(r["schichten"]):
            z.append(f"   {s['ok_mm']:6.0f}  {s['dicke_mm']:5.0f} mm  {s['name']}")
        if r["zulaessig"]:
            z.append(f"   Masse {k['flaechenmasse_kg_m2']} kg/m², R_λ,B {k['R_lambda_B']}, "
                     f"R_ins {k.get('R_ins')}, U {k.get('U_W_m2K')}, CM max {k.get('belegreife_cm_max')}")
        for v in r["verstoesse"]:
            z.append("   VERSTOSS: " + v)
        for h in r["hinweise"]:
            z.append("   Hinweis: " + h)
    for u in e["uebergaenge"]:
        z.append(f"\nÜbergang {u['a']} – {u['b']} ({u['art']}): ΔOKFF {u.get('delta_okff_mm')} mm, "
                 f"Kante worst case {u.get('kante_worst_case_mm')} mm")
        for v in u["verstoesse"]:
            z.append("   VERSTOSS: " + v)
        for h in u["hinweise"]:
            z.append("   Hinweis: " + h)
    return "\n".join(z)


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--eingabe", default=str(STANDARD_EINGABE))
    ap.add_argument("--variante", default=None, help="Standard: alle Varianten")
    ap.add_argument("--ifc", action="store_true", help="IFC-Datei schreiben und validieren")
    a = ap.parse_args()
    daten = lade_eingabe(a.eingabe)
    for v in ([a.variante] if a.variante else list(daten["varianten"])):
        e = berechne_variante(daten, v)
        AUSGABE.mkdir(exist_ok=True)
        (AUSGABE / f"b14_{v}.json").write_text(json.dumps(e, ensure_ascii=False, indent=1), encoding="utf-8")
        print(bericht_text(e))
        if a.ifc:
            import ifcopenshell.validate
            pfad = erzeuge_ifc(daten, e).schreibe(AUSGABE / f"b14_{v}.ifc")
            log = ifcopenshell.validate.json_logger()
            ifcopenshell.validate.validate(str(pfad), log, express_rules=True)
            print(f"\nIFC {pfad.name}: {len(log.statements)} Validierungsfehler")
        print("\n" + "=" * 78 + "\n")


if __name__ == "__main__":
    main()

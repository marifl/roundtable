#!/usr/bin/env python3
"""
B19 – Schallschutz gegen Außenlärm: von der Lärmbelastung am Grundstück bis zur
Bauteilwahl je Raum und zur Empfehlung „anders planen“.

Beispiel: Autobahn 150 m nördlich eines zweigeschossigen Holzrahmenhauses
(11 m × 8 m). Zwei Grundrissvarianten im Obergeschoss:
  A „Ursprung“: Schlafen und Kind an der Nordfassade (zur Autobahn),
  B „Tausch“:   Schlafen und Kind an der Südfassade, Arbeiten/Bad nach Norden.

ALLE Pegel, Schalldämm-Maße und Preise im Beispiel sind BEISPIELWERTE.
Normwerte stehen im Code nur als einzelne Kennwerte mit Normverweis, keine
Normtabellen. Grundlage: Recherche 20 (docs/holzbau/recherche/20-aussenlaerm-
schallschutz.md).

Rechenweg (DIN 4109-1:2018-01 Abschn. 7, DIN 4109-2:2018-01 Abschn. 4.4, 5.3.3):

  1. Fassadenpegel je Himmelsrichtung aus einem Bezugspegel (Beurteilungspegel
     Lr,T / Lr,N nach RLS-19 aus Gutachten oder B-Plan, Freifeld am Ort der
     Nordfassade). Vereinfachte Ausbreitung (ANNAHME, keine Norm):
       - Abstandsmaß einer langen Linienquelle: ΔL_d = 10·lg(d_ref / d)
       - Eigenabschirmung: Anteil des Sichtwinkels auf die Quelle, der von der
         Fassade aus frei ist (shapely-Sichtprüfung gegen den eigenen Baukörper),
         ΔL_o = 10·lg(Anteil).
     Modus „nachweis“ (Standard): Nur Fassaden ohne jede Sicht auf die Quelle
       werden gemindert, und zwar pauschal um 5 dB (offene Bebauung) bzw.
       10 dB (geschlossene Bebauung/Innenhof), DIN 4109-2, 4.4.5.1.
       Seitenfassaden mit Streifsicht bleiben ungemindert.
     Modus „planung“: ΔL_o = max(10·lg(Anteil), −5 dB). Nur für Varianten-
       vergleiche; für den Nachweis braucht eine Minderung von Seitenfassaden
       einen Gutachternachweis.
  2. Maßgeblicher Außenlärmpegel La je Fassade (DIN 4109-2, 4.4.5):
       La,Tag   = Lr,T + 3 dB
       La,Schlaf = max(La,Tag, Lr,N + 3 dB + 10 dB), der Nachtterm nur wenn
                   Lr,T − Lr,N < 10 dB (4.4.5.2 ff.)
       Schiene: Beurteilungspegel pauschal −5 dB (4.4.5.3).
       Mehrere Quellen: energetische Summe, +3 dB nur einmal (4.4.5.7, Gl. 44).
  3. Anforderung je Raum (DIN 4109-1, 7.1, Gl. 6):
       erf R'w,ges = La,max − K_Raumart, mindestens 30 dB (Wohnen)
       K_AL = 10·lg(S_S / (0,8·S_G))                       (DIN 4109-2, Gl. 33)
     Fassaden eines Raums mit geringerem La: K_LPB = La,max − La,i wird auf die
     Schalldämm-Maße dieser Fassadenteile addiert (DIN 4109-2, 4.4.1).
  4. Nachweis (DIN 4109-2, Gl. 32, 35, 37, 38; 5.3.3):
       R'w,ges = −10·lg( Σ S_i/S_S · 10^(−(R_i+K_LPB,i)/10)
                         + Σ A0/S_S · 10^(−(D_n,e,w,j+K_LPB,j)/10) ),  A0 = 10 m²
       erfüllt, wenn R'w,ges − 2 dB ≥ erf R'w,ges + K_AL
     Holzbau: keine Flankenübertragung (DIN 4109-2, 4.4.3).
  5. Automatische Wahl: je Raum und Fassade die Fensterklasse (VDI 2719,
     Prüfstandswert), je Raum Rollladenkasten und ALD; Ziel: minimale Mehrkosten,
     bei Gleichstand kleinste Klassen. Zuerst nur Regnauer-Katalog (KlimaPlus
     optional SSK 3/4 nur einflüglig), dann Fremdprodukte (SSK 5/6).
  6. Assistenz: BayTB-Nachweispflicht, Lüftungskonzept (DIN 1946-6) bei hohen
     Nachtpegeln, Fensterverzicht an der lautesten Fassade, Grundrisstausch
     (Varianten A/B mit Mehrkosten), WHO-Hinweis (nicht bindend), Grenzen.

Aufruf:   python b19_aussenlaerm.py [--modus nachweis|planung] [--lueftung ALD|KWL] [--ifc]
Ausgabe:  ausgabe/b19_aussenlaerm.json, ausgabe/b19_aussenlaerm.md,
          optional ausgabe/b19_aussenlaerm_<A|B>.ifc (IFC4X3_ADD2)
"""
from __future__ import annotations

import argparse
import copy
import itertools
import json
import math
import uuid
from pathlib import Path

import numpy as np
from shapely.geometry import LineString, Point, Polygon, box

HIER = Path(__file__).resolve().parent
AUSGABE = HIER / "ausgabe"

# Fester Namensraum für uuid5 (selbst gewählt, einmalig erzeugt und fixiert).
GUID_NAMENSRAUM = uuid.UUID("6f0c2b9e-4a51-5d7e-9b13-2c8e7f4d1a60")

# ---------------------------------------------------------------------------
# 0. Kennwerte aus Normen und Verwaltungsvorschriften (einzeln, mit Verweis)
# ---------------------------------------------------------------------------
ZUSCHLAG_LA = 3.0            # DIN 4109-2:2018-01, 4.4.5.2–4.4.5.6: +3 dB auf den Beurteilungspegel
NACHTZUSCHLAG = 10.0         # dito: Zuschlag Nacht für Räume, die überwiegend zum Schlafen genutzt werden können
NACHT_DIFFERENZ = 10.0       # dito: Nachtregel greift, wenn Lr,T − Lr,N < 10 dB
SCHIENE_ABSCHLAG = 5.0       # DIN 4109-2:2018-01, 4.4.5.3: Beurteilungspegel Schiene pauschal −5 dB
ABGEWANDT_OFFEN = 5.0        # DIN 4109-2:2018-01, 4.4.5.1: abgewandte Seite, offene Bebauung
ABGEWANDT_GESCHLOSSEN = 10.0 # dito: geschlossene Bebauung bzw. Innenhof
K_RAUMART = {"wohnen": 30.0, "buero": 35.0, "bettenraum": 25.0}   # DIN 4109-1:2018-01, 7.1, Gl. (6)
MINDEST_RWGES = {"wohnen": 30.0, "buero": 30.0, "bettenraum": 35.0}  # dito, Mindestwerte
U_PROG = 2.0                 # DIN 4109-2:2018-01, 5.3.3: Sicherheitsbeiwert Luftschall 2 dB
A0 = 10.0                    # DIN 4109-2:2018-01, Gl. (38): Bezugsabsorptionsfläche 10 m²
KAL_FAKTOR = 0.8             # DIN 4109-2:2018-01, Gl. (33): K_AL = 10 lg(S_S/(0,8·S_G))
EINZELFALL_RWGES = 50.0      # DIN 4109-1, 7.1 / BayTB 11/2025 Anl. A 5.2/1 Nr. 1 und 3
EINZELFALL_LA = 80.0         # dito (La > 80 dB: Bauaufsicht legt fest, Messung)
BAYTB_SCHWELLE = {"wohnen": 61.0, "bettenraum": 61.0, "buero": 66.0}  # BayTB 11/2025 Anl. A 5.2/1 Nr. 5 b
# Verfahren, aus denen ein Beurteilungspegel für den Nachweis stammen darf (DIN 4109-2, 4.4.5.2 ff.)
NACHWEIS_VERFAHREN = {"RLS-19", "Schall 03", "TA Lärm", "TA Lärm IRW", "DIN 18005 Diagramm", "FluLärmG", "Messung DIN 4109-4"}
# Assistenzschwellen (keine Nachweisgrößen)
OW_WA = (55.0, 45.0)         # DIN 18005 Beiblatt 1:2023-07, WA Verkehr tags/nachts (Orientierungswert)
LUEFTUNG_NACHT_BBL = 45.0    # DIN 18005 Bbl. 1: ab > 45 dB(A) nachts Schlaf bei Kippfenster oft gestört [U, Sekundärzitat]
LUEFTUNG_NACHT_VDI = 50.0    # VDI 2719:1987, Abschn. 10: > 50 dB(A) fensterunabhängige Lüftung [U, Sekundärzitat]
WHO_STRASSE = (53.0, 45.0)   # WHO 2018 Lden/Lnight Straße (nicht bindend, Recherche 15)


# ---------------------------------------------------------------------------
# 1. Beispiel-Eingabe (alles BEISPIELWERTE)
# ---------------------------------------------------------------------------

def beispiel_eingabe() -> dict:
    """Grundstück, Quelle, Haus mit zwei OG-Varianten, Bauteilkatalog."""
    raumhoehe = 2.5
    fenster = lambda b, h, fl=False, rk=True: {"b": b, "h": h, "mehrfluegelig": fl, "rollladen": rk}  # noqa: E731
    eg = [
        {"name": "Wohnen/Essen", "geschoss": "EG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": True,
         "polygon": [[0, 0], [7, 0], [7, 8], [0, 8]],
         "fenster": {"N": [fenster(1.5, 1.4)], "W": [fenster(1.25, 1.4)],
                     "S": [fenster(3.0, 2.2, fl=True), fenster(1.0, 2.2)]}},
        {"name": "Küche", "geschoss": "EG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "bemerkung": "Arbeitsküche ohne Essplatz: kein schutzbedürftiger Raum (DIN 4109-1, 3.16 nennt Wohnküchen)",
         "polygon": [[7, 4], [11, 4], [11, 8], [7, 8]], "fenster": {"N": [fenster(1.2, 1.2)]}},
        {"name": "Flur/HWR", "geschoss": "EG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[7, 0], [11, 0], [11, 4], [7, 4]], "fenster": {"S": [fenster(1.0, 2.2, rk=False)]}},
    ]
    og_a = [
        {"name": "Schlafen", "geschoss": "OG", "nutzung": "wohnen", "schlafen": True, "schutzbeduerftig": True,
         "polygon": [[0, 4], [4.5, 4], [4.5, 8], [0, 8]],
         "fenster": {"N": [fenster(2.0, 1.4)], "W": [fenster(1.0, 1.4)]}},
        {"name": "Bad", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[4.5, 4], [7, 4], [7, 8], [4.5, 8]], "fenster": {"N": [fenster(0.8, 1.0, rk=False)]}},
        {"name": "Kind", "geschoss": "OG", "nutzung": "wohnen", "schlafen": True, "schutzbeduerftig": True,
         "polygon": [[7, 4], [11, 4], [11, 8], [7, 8]],
         "fenster": {"N": [fenster(1.5, 1.4)], "E": [fenster(1.0, 1.4)]}},
        {"name": "Arbeiten", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": True,
         "bemerkung": "als Tagraum eingestuft; wird er als Gästezimmer genutzt, gilt die Nachtregel [U]",
         "polygon": [[0, 0], [4, 0], [4, 4], [0, 4]],
         "fenster": {"S": [fenster(1.5, 1.4)], "W": [fenster(1.0, 1.4)]}},
        {"name": "Flur/Treppe", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[4, 0], [11, 0], [11, 4], [4, 4]], "fenster": {"S": [fenster(1.0, 1.4, rk=False)]}},
    ]
    og_b = [
        {"name": "Arbeiten", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": True,
         "bemerkung": "als Tagraum eingestuft [U]",
         "polygon": [[0, 4], [4.5, 4], [4.5, 8], [0, 8]],
         "fenster": {"N": [fenster(1.5, 1.4)], "W": [fenster(1.0, 1.4)]}},
        {"name": "Bad", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[4.5, 4], [7, 4], [7, 8], [4.5, 8]], "fenster": {"N": [fenster(0.8, 1.0, rk=False)]}},
        {"name": "Flur/Treppe", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[7, 4], [11, 4], [11, 8], [7, 8]], "fenster": {"N": [fenster(1.0, 1.4, rk=False)]}},
        {"name": "Kind", "geschoss": "OG", "nutzung": "wohnen", "schlafen": True, "schutzbeduerftig": True,
         "bemerkung": "Westwand ohne Fenster (Seitenfassade mit Streifsicht auf die Autobahn)",
         "polygon": [[0, 0], [3.5, 0], [3.5, 4], [0, 4]], "fenster": {"S": [fenster(1.5, 1.4)]}},
        {"name": "Schlafen", "geschoss": "OG", "nutzung": "wohnen", "schlafen": True, "schutzbeduerftig": True,
         "polygon": [[3.5, 0], [8, 0], [8, 4], [3.5, 4]], "fenster": {"S": [fenster(2.0, 1.4), fenster(1.0, 1.4)]}},
        {"name": "Ankleide", "geschoss": "OG", "nutzung": "wohnen", "schlafen": False, "schutzbeduerftig": False,
         "polygon": [[8, 0], [11, 0], [11, 4], [8, 4]], "fenster": {"E": [fenster(0.8, 1.0, rk=False)]}},
    ]
    return {
        "hinweis": "Alle Zahlen sind Beispielwerte. Pegel nicht aus einer realen Lärmkarte.",
        "grundstueck": {"polygon": [[-7, -12], [18, -12], [18, 18], [-7, 18]], "gebiet": "WA"},
        "haus": {"footprint": [[0, 0], [11, 0], [11, 8], [0, 8]], "raumhoehe": raumhoehe,
                 "bebauung": "offen"},
        "quellen": [{
            "name": "Autobahn (Beispiel)", "art": "strasse", "verfahren": "RLS-19",
            "herkunft": "Beispielwert, wie aus schalltechnischer Untersuchung zum B-Plan",
            # Achse 150 m nördlich der Nordfassade, 4 km lang (Linienquelle)
            "achse": [[-2000.0, 158.0], [2000.0, 158.0]],
            "bezugspunkt": [5.5, 8.0], "lr_tag": 66.0, "lr_nacht": 59.0,
            "eu_laermkarte": {"lden": 68.0, "lnight": 59.0, "quelle": "Beispielwert, wie LfU-WMS Hauptverkehrsstraßen 2022"},
        }],
        "bplan": {"festsetzung_9_1_24": False},
        "lueftung": "ALD",   # "ALD" (dezentrale Außenwandluftdurchlässe) oder "KWL" (zentrale Lüftung mit WRG)
        "varianten": {"A_ursprung": eg + og_a, "B_tausch": eg + og_b},
        "katalog": katalog_beispiel(),
    }


def katalog_beispiel() -> dict:
    """Bauteilkatalog. Schalldämm-Maße: BEISPIELWERTE bzw. VDI-2719-Klassengrenzen.
    Preise: frei gewählte Beispiel-Mehrpreise, KEINE Markt- oder Regnauer-Preise."""
    return {
        "aussenwand": {"name": "Holzrahmen + Holzfaser-WDVS (Beispiel, orientiert an ift-Prüfbericht 47 dB)",
                       "rw": 47.0},
        # Fenster: Rw = Prüfstandswert, den VDI 2719 Tab. 2 für die Klasse verlangt (27/32/37/42/47/52 dB)
        "fenster": [
            {"klasse": 2, "rw": 32.0, "mk_eur_m2": 0.0, "regnauer": True, "mehrfluegelig": True},
            {"klasse": 3, "rw": 37.0, "mk_eur_m2": 60.0, "regnauer": True, "mehrfluegelig": False},
            {"klasse": 4, "rw": 42.0, "mk_eur_m2": 150.0, "regnauer": True, "mehrfluegelig": False},
            {"klasse": 5, "rw": 47.0, "mk_eur_m2": 380.0, "regnauer": False, "mehrfluegelig": True},
            {"klasse": 6, "rw": 52.0, "mk_eur_m2": 800.0, "regnauer": False, "mehrfluegelig": True},
        ],
        # Rollladenkasten als Element mit D_n,e,w (DIN 4109-2, Gl. 38); Kastenhöhe 0,30 m
        "rollladen": [
            {"typ": "Aufsatzkasten Standard", "dnew": 44.0, "mk_eur_m": 0.0, "kastenhoehe": 0.30},
            {"typ": "Aufsatzkasten schallgedämmt", "dnew": 50.0, "mk_eur_m": 90.0, "kastenhoehe": 0.30},
            {"typ": "Vorbau-Raffstore (kein Kasten in der Wand)", "dnew": None, "mk_eur_m": 160.0, "kastenhoehe": 0.0},
        ],
        # Außenwandluftdurchlass je schutzbedürftigem Raum (nur bei Lüftungskonzept "ALD")
        "ald": [
            {"typ": "ALD Standard", "dnew": 36.0, "eur": 0.0},
            {"typ": "ALD schallgedämmt", "dnew": 44.0, "eur": 180.0},
            {"typ": "ALD Schallschutz hoch", "dnew": 52.0, "eur": 420.0},
        ],
        "dachflaechenfenster": [   # nur für die generische Rechnung (Dachräume), im Beispiel nicht verwendet
            {"typ": "DFF Standard", "rw": 35.0}, {"typ": "DFF Schallschutz", "rw": 41.0},
        ],
    }


# ---------------------------------------------------------------------------
# 2. Akustische Grundfunktionen
# ---------------------------------------------------------------------------

def pegel_summe(pegel: list[float]) -> float:
    """Energetische Summe von Pegeln in dB (DIN 4109-2, Gl. 44 ohne Zuschlag)."""
    werte = [p for p in pegel if p is not None and math.isfinite(p)]
    if not werte:
        return -math.inf
    return 10.0 * math.log10(float(np.sum(np.power(10.0, 0.1 * np.asarray(werte)))))


def rw_ges(bauteile: list[dict], elemente: list[dict]) -> float:
    """Gesamtes bewertetes Bau-Schalldämm-Maß der Fassade eines Raums
    (DIN 4109-2, Gl. 35 mit 37 und 38).
    bauteile: {"flaeche", "rw", "k_lpb"}; Einträge mit rw = None (Kastenflächen
    von Rollladenkästen) zählen nur zu S_S, ihre Übertragung steckt im D_n,e,w.
    elemente: {"dnew", "k_lpb"}. S_S = Summe aller Teilflächen (4.4.2)."""
    s_s = sum(b["flaeche"] for b in bauteile)
    if s_s <= 0:
        raise ValueError("Fassadenfläche S_S muss > 0 sein")
    tau = sum(b["flaeche"] / s_s * 10.0 ** (-(b["rw"] + b.get("k_lpb", 0.0)) / 10.0)
              for b in bauteile if b.get("rw") is not None)
    tau += sum(A0 / s_s * 10.0 ** (-(e["dnew"] + e.get("k_lpb", 0.0)) / 10.0) for e in elemente)
    return -10.0 * math.log10(tau)


def k_al(s_s: float, s_g: float) -> float:
    """Korrekturwert Außenlärm (DIN 4109-2, Gl. 33)."""
    return 10.0 * math.log10(s_s / (KAL_FAKTOR * s_g))


def la_aus_lpb(lpb: str) -> float | None:
    """Lärmpegelbereich → maßgeblicher Außenlärmpegel, wenn nur LPB vorliegen
    (DIN 4109-1:2018-01, 7.1, Tab. 7: Obergrenze des 5-dB-Bands, I = 55 dB).
    LPB VII: None (> 80 dB, Einzelfall)."""
    stufen = ["I", "II", "III", "IV", "V", "VI"]
    if lpb == "VII":
        return None
    return 55.0 + 5.0 * stufen.index(lpb)


def massgeblicher_aussenlaermpegel(quellen: list[dict]) -> dict:
    """La für Tag und für Räume mit Schlafnutzung aus Beurteilungspegeln je Quelle
    (DIN 4109-2, 4.4.5). quellen: {"art", "lr_tag", "lr_nacht"}. Je Quelle wird
    der maßgebliche Wert ohne +3 dB gebildet (Nachtregel je Quelle), dann
    energetisch summiert und einmal +3 dB addiert (4.4.5.7). Die Anwendung der
    Nachtregel je Quelle ist eine Auslegung [U], wie im Beispiel des Instituts
    für Holzbau (2024)."""
    tag, schlaf = [], []
    for q in quellen:
        abschlag = SCHIENE_ABSCHLAG if q["art"] == "schiene" else 0.0
        lt = q["lr_tag"] - abschlag
        ln = q["lr_nacht"] - abschlag
        tag.append(lt)
        nacht_relevant = (q["lr_tag"] - q["lr_nacht"]) < NACHT_DIFFERENZ
        schlaf.append(max(lt, ln + NACHTZUSCHLAG) if nacht_relevant else lt)
    return {"la_tag": pegel_summe(tag) + ZUSCHLAG_LA, "la_schlaf": pegel_summe(schlaf) + ZUSCHLAG_LA}


def baytb_nachweis_erforderlich(la_je_raum: list[tuple[str, float]], bplan_festsetzung: bool) -> tuple[bool, str]:
    """BayTB 11/2025, Anlage A 5.2/1 Nr. 5: Nachweis der Luftschalldämmung von
    Außenbauteilen erforderlich bei B-Plan-Festsetzung nach § 9 Abs. 1 Nr. 24
    BauGB oder La ≥ 61 dB(A) (Aufenthaltsräume) bzw. ≥ 66 dB(A) (Büro).
    la_je_raum: (nutzung, maßgeblicher La des Raums)."""
    if bplan_festsetzung:
        return True, "B-Plan setzt Vorkehrungen nach § 9 Abs. 1 Nr. 24 BauGB fest"
    for nutzung, la in la_je_raum:
        if la >= BAYTB_SCHWELLE[nutzung]:
            return True, f"La = {la:.1f} dB ≥ {BAYTB_SCHWELLE[nutzung]:.0f} dB ({nutzung})"
    return False, "keine Festsetzung und La unter der Schwelle"


# ---------------------------------------------------------------------------
# 3. Fassadenpegel: vereinfachte Ausbreitung mit Eigenabschirmung (ANNAHME)
# ---------------------------------------------------------------------------
RICHTUNGEN = {"N": (0.0, 1.0), "E": (1.0, 0.0), "S": (0.0, -1.0), "W": (-1.0, 0.0)}


def fassaden_des_hauses(footprint: Polygon) -> dict[str, LineString]:
    """Fassadenkanten des (achsparallelen) Grundrisses je Himmelsrichtung."""
    fassaden: dict[str, list] = {}
    ring = list(footprint.exterior.coords)
    if footprint.exterior.is_ccw is False:
        ring = ring[::-1]
    for (x1, y1), (x2, y2) in zip(ring[:-1], ring[1:]):
        dx, dy = x2 - x1, y2 - y1
        n = (dy, -dx)                       # Außennormale bei Gegenuhrzeigersinn
        laenge = math.hypot(dx, dy)
        n = (round(n[0] / laenge, 9), round(n[1] / laenge, 9))
        for r, v in RICHTUNGEN.items():
            if abs(n[0] - v[0]) < 1e-6 and abs(n[1] - v[1]) < 1e-6:
                fassaden.setdefault(r, []).append(LineString([(x1, y1), (x2, y2)]))
    # je Richtung die längste Kante (bei achsparallelem Rechteck genau eine)
    return {r: max(k, key=lambda s: s.length) for r, k in sorted(fassaden.items())}


def sichtanteil(p: Point, normale: tuple[float, float], achse: LineString, gebaeude: Polygon,
                n_stuetz: int = 4001) -> float:
    """Anteil der von P aus frei sichtbaren Quelle, gewichtet mit dem Sichtwinkel
    (inkohärente Linienquelle: dI ∝ dθ). Sichtbar heißt: vor der Fassade
    ((Q−P)·n > 0) und die Sichtlinie schneidet den Baukörper nicht."""
    s = np.linspace(0.0, achse.length, n_stuetz)
    pts = [achse.interpolate(float(si)) for si in s]
    q = np.array([[pt.x, pt.y] for pt in pts])
    px, py = p.x, p.y
    theta = np.arctan2(q[:, 1] - py, q[:, 0] - px)
    dtheta = np.abs(np.gradient(np.unwrap(theta)))
    vor = (q[:, 0] - px) * normale[0] + (q[:, 1] - py) * normale[1] > 1e-9
    innen = gebaeude.buffer(-1e-6)
    frei = np.array([bool(v) and not LineString([(px, py), (qx, qy)]).intersects(innen)
                     for v, (qx, qy) in zip(vor, q)])
    gesamt = float(dtheta.sum())
    return float(dtheta[frei].sum()) / gesamt if gesamt > 0 else 0.0


def fassadenpegel(eingabe: dict, modus: str = "nachweis") -> dict:
    """Beurteilungspegel Lr,T/Lr,N je Fassade und Quelle, daraus La je Fassade."""
    haus = eingabe["haus"]
    fp = Polygon(haus["footprint"])
    fassaden = fassaden_des_hauses(fp)
    minderung_abgewandt = ABGEWANDT_OFFEN if haus.get("bebauung", "offen") == "offen" else ABGEWANDT_GESCHLOSSEN
    ergebnis = {}
    for r, kante in fassaden.items():
        mitte = kante.interpolate(0.5, normalized=True)
        n = RICHTUNGEN[r]
        p = Point(mitte.x + 0.05 * n[0], mitte.y + 0.05 * n[1])
        je_quelle = []
        nachweis_tauglich = True
        for qd in eingabe["quellen"]:
            achse = LineString(qd["achse"])
            d_ref = achse.distance(Point(qd["bezugspunkt"]))
            d = achse.distance(p)
            dl_d = 10.0 * math.log10(d_ref / d)            # ANNAHME: lange Linienquelle, 3 dB je Abstandsverdopplung
            anteil = sichtanteil(p, n, achse, fp)
            if modus == "nachweis":
                dl_o = 0.0 if anteil > 0.0 else -minderung_abgewandt
                grund = "zugewandt oder Streifsicht: keine Minderung ohne Gutachten" if anteil > 0 else \
                    f"abgewandt: −{minderung_abgewandt:.0f} dB ohne besonderen Nachweis (DIN 4109-2, 4.4.5.1)"
            else:
                dl_o = max(10.0 * math.log10(anteil), -minderung_abgewandt) if anteil > 0 else -minderung_abgewandt
                grund = "Sichtwinkelmodell (ANNAHME, nur Variantenvergleich)"
            if qd.get("verfahren") not in NACHWEIS_VERFAHREN:
                nachweis_tauglich = False
            je_quelle.append({"quelle": qd["name"], "art": qd["art"], "verfahren": qd.get("verfahren"),
                              "abstand_m": round(d, 1), "dL_abstand": round(dl_d, 2), "sichtanteil": round(anteil, 3),
                              "dL_orientierung": round(dl_o, 2), "begruendung": grund,
                              "lr_tag": qd["lr_tag"] + dl_d + dl_o, "lr_nacht": qd["lr_nacht"] + dl_d + dl_o})
        la = massgeblicher_aussenlaermpegel(je_quelle)
        ergebnis[r] = {"quellen": [{k: (round(v, 2) if isinstance(v, float) else v) for k, v in q.items()} for q in je_quelle],
                       "la_tag": round(la["la_tag"], 2), "la_schlaf": round(la["la_schlaf"], 2),
                       "nachweis_tauglich": nachweis_tauglich}
    return ergebnis


# ---------------------------------------------------------------------------
# 4. Räume: Geometrie, Fassadenteile, Nachweis und Bauteilwahl
# ---------------------------------------------------------------------------

def raum_fassaden(raum: dict, footprint: Polygon, raumhoehe: float) -> dict[str, float]:
    """Außenwandlängen des Raums je Himmelsrichtung (Kanten auf dem Hausumriss)."""
    rp = Polygon(raum["polygon"])
    fass = fassaden_des_hauses(footprint)
    laengen = {}
    for r, kante in fass.items():
        gemeinsam = rp.exterior.intersection(kante)
        if gemeinsam.length > 1e-6:
            laengen[r] = round(gemeinsam.length, 4)
    return laengen


def bauteile_des_raums(raum: dict, laengen: dict[str, float], raumhoehe: float, katalog: dict,
                       wahl: dict, la: dict[str, float], la_max: float, lueftung: str) -> tuple[list, list, dict]:
    """Bauteile (Wand, Fenster) und Elemente (Rollladenkasten, ALD) eines Raums
    mit K_LPB je Fassade. wahl: {"klasse": {richtung: k}, "rollladen": typ, "ald": typ}."""
    kl = {f["klasse"]: f for f in katalog["fenster"]}
    rk = {r["typ"]: r for r in katalog["rollladen"]}[wahl["rollladen"]]
    bauteile, elemente = [], []
    flaechen = {}
    for r, laenge in sorted(laengen.items()):
        k_lpb = la_max - la[r]
        s_fassade = laenge * raumhoehe
        s_fenster = 0.0
        s_kasten = 0.0
        for i, f in enumerate(raum["fenster"].get(r, [])):
            fk = kl[wahl["klasse"][r]]
            s_fenster += f["b"] * f["h"]
            bauteile.append({"bauteil": f"Fenster {r}{i + 1} SSK {fk['klasse']}", "flaeche": f["b"] * f["h"],
                             "rw": fk["rw"], "k_lpb": k_lpb})
            if f["rollladen"] and rk["dnew"] is not None:
                s_kasten += f["b"] * rk["kastenhoehe"]
                elemente.append({"element": f"{rk['typ']} {r}{i + 1}", "dnew": rk["dnew"], "k_lpb": k_lpb,
                                 "flaeche": f["b"] * rk["kastenhoehe"]})
        s_wand = s_fassade - s_fenster - s_kasten
        if s_wand < -1e-9:
            raise ValueError(f"{raum['name']}: Öffnungen größer als die Fassade {r}")
        bauteile.append({"bauteil": f"Außenwand {r}", "flaeche": s_wand, "rw": katalog["aussenwand"]["rw"], "k_lpb": k_lpb})
        flaechen[r] = s_fassade
    # Kastenflächen gehören zu S_S (Teilflächen aller Bauteile und Elemente, DIN 4109-2, 4.4.2)
    for e in elemente:
        bauteile.append({"bauteil": "(Kastenfläche)", "flaeche": e["flaeche"], "rw": None, "k_lpb": e["k_lpb"], "nur_flaeche": True})
    if lueftung == "ALD" and wahl.get("ald"):
        ald = {a["typ"]: a for a in katalog["ald"]}[wahl["ald"]]
        r_ald = wahl.get("ald_fassade") or max(laengen, key=lambda r: (la[r], r))  # ohne Angabe: lauteste Fassade
        elemente.append({"element": f"{ald['typ']} ({r_ald})", "dnew": ald["dnew"], "k_lpb": la_max - la[r_ald]})
    return bauteile, elemente, flaechen


def pruefe_raum(raum: dict, laengen: dict[str, float], s_g: float, raumhoehe: float, pegel: dict,
                katalog: dict, wahl: dict, lueftung: str) -> dict:
    """Nachweis für einen Raum und eine Bauteilwahl: je Zeitraum (Tag; bei
    Schlafnutzung zusätzlich Schlaf/Nacht) erf R'w,ges, K_AL, vorh. R'w,ges."""
    k = K_RAUMART[raum["nutzung"]]
    zeitraeume = ["tag"] + (["schlaf"] if raum["schlafen"] else [])
    s_s = sum(laengen.values()) * raumhoehe
    kal = k_al(s_s, s_g)
    ergebnisse = {}
    for z in zeitraeume:
        la = {r: pegel[r][f"la_{z}"] for r in laengen}
        la_max = max(la.values())
        erf = max(la_max - k, MINDEST_RWGES[raum["nutzung"]])
        bt, el, _ = bauteile_des_raums(raum, laengen, raumhoehe, katalog, wahl, la, la_max, lueftung)
        vorh = rw_ges(bt, el)
        ergebnisse[z] = {"la_max": round(la_max, 2), "erf_rw_ges": round(erf, 2), "k_al": round(kal, 2),
                         "rw_ges": round(vorh, 2), "rw_ges_minus_uprog": round(vorh - U_PROG, 2),
                         "ziel": round(erf + kal, 2), "reserve": round(vorh - U_PROG - (erf + kal), 2),
                         "erfuellt": vorh - U_PROG >= erf + kal - 1e-9}
    massg = max(ergebnisse, key=lambda z: (ergebnisse[z]["ziel"], z))
    return {"zeitraeume": ergebnisse, "massgebend": massg, "erfuellt": all(e["erfuellt"] for e in ergebnisse.values()),
            "s_s": round(s_s, 2), "s_g": round(s_g, 2)}


def kosten(raum: dict, wahl: dict, katalog: dict, lueftung: str) -> float:
    """Mehrkosten der Wahl gegenüber Standard (Beispielpreise)."""
    kl = {f["klasse"]: f for f in katalog["fenster"]}
    rk = {r["typ"]: r for r in katalog["rollladen"]}[wahl["rollladen"]]
    eur = 0.0
    for r, fl in raum["fenster"].items():
        for f in fl:
            eur += f["b"] * f["h"] * kl[wahl["klasse"][r]]["mk_eur_m2"]
            if f["rollladen"]:
                eur += f["b"] * rk["mk_eur_m"]
    if lueftung == "ALD" and wahl.get("ald"):
        eur += {a["typ"]: a for a in katalog["ald"]}[wahl["ald"]]["eur"]
    return round(eur, 2)


def zulaessige_klassen(raum: dict, richtung: str, katalog: dict, nur_regnauer: bool) -> list[int]:
    """Fensterklassen, die für alle Fenster einer Fassade lieferbar sind."""
    fl = raum["fenster"].get(richtung, [])
    out = []
    for f in katalog["fenster"]:
        if nur_regnauer and not f["regnauer"]:
            continue
        if nur_regnauer and any(x["mehrfluegelig"] for x in fl) and not f["mehrfluegelig"]:
            continue   # Regnauer: SSK 3/4 nur im einflügligen Bereich (Ausstattungsbeschreibung 10/2024)
        out.append(f["klasse"])
    return out


def waehle_bauteile(raum: dict, laengen: dict[str, float], s_g: float, raumhoehe: float, pegel: dict,
                    katalog: dict, lueftung: str) -> dict:
    """Vollständige Aufzählung (deterministisch): minimale Mehrkosten, dann
    kleinste maximale Klasse, dann kleinste Klassensumme, dann Text."""
    richtungen = sorted(r for r in laengen if raum["fenster"].get(r))
    hat_rk = any(f["rollladen"] for fl in raum["fenster"].values() for f in fl)
    rk_optionen = [r["typ"] for r in katalog["rollladen"]] if hat_rk else [katalog["rollladen"][0]["typ"]]
    ald_optionen = [a["typ"] for a in katalog["ald"]] if lueftung == "ALD" else [None]
    # ALD-Lage ist Teil der Wahl: an einer leiseren Fassade wirkt K_LPB zugunsten des ALD
    ald_fassaden = sorted(laengen) if lueftung == "ALD" else [None]
    for stufe, nur_regnauer in (("Regnauer-Katalog", True), ("mit Fremdprodukten", False)):
        klassen = [zulaessige_klassen(raum, r, katalog, nur_regnauer) for r in richtungen]
        if any(not k for k in klassen):
            continue
        kandidaten = []
        for kombi in itertools.product(*klassen):
            for rk in rk_optionen:
                for ald, ald_f in itertools.product(ald_optionen, ald_fassaden):
                    wahl = {"klasse": dict(zip(richtungen, kombi)), "rollladen": rk, "ald": ald, "ald_fassade": ald_f}
                    pr = pruefe_raum(raum, laengen, s_g, raumhoehe, pegel, katalog, wahl, lueftung)
                    if pr["erfuellt"]:
                        schluessel = (kosten(raum, wahl, katalog, lueftung), max(kombi) if kombi else 0,
                                      sum(kombi), json.dumps(wahl, sort_keys=True))
                        kandidaten.append((schluessel, wahl, pr))
        if kandidaten:
            kandidaten.sort(key=lambda t: t[0])
            s, wahl, pr = kandidaten[0]
            return {"gefunden": True, "stufe": stufe, "wahl": wahl, "mehrkosten_eur": s[0], "pruefung": pr,
                    "anzahl_zulaessig": len(kandidaten)}
    # nichts gefunden: beste (größte Reserve) Kombination mit Maximalausstattung melden
    wahl = {"klasse": {r: max(f["klasse"] for f in katalog["fenster"]) for r in richtungen},
            "rollladen": katalog["rollladen"][-1]["typ"] if hat_rk else katalog["rollladen"][0]["typ"],
            "ald": katalog["ald"][-1]["typ"] if lueftung == "ALD" else None,
            "ald_fassade": min(laengen, key=lambda r: (pegel[r]["la_schlaf"], r)) if lueftung == "ALD" else None}
    pr = pruefe_raum(raum, laengen, s_g, raumhoehe, pegel, katalog, wahl, lueftung)
    return {"gefunden": False, "stufe": "keine Lösung im Katalog", "wahl": wahl,
            "mehrkosten_eur": kosten(raum, wahl, katalog, lueftung), "pruefung": pr, "anzahl_zulaessig": 0}


# ---------------------------------------------------------------------------
# 5. Variante auswerten, Assistenzregeln
# ---------------------------------------------------------------------------

def werte_variante_aus(eingabe: dict, raeume: list[dict], pegel: dict, lueftung: str) -> dict:
    haus = eingabe["haus"]
    fp = Polygon(haus["footprint"])
    h = haus["raumhoehe"]
    katalog = eingabe["katalog"]
    zeilen, verstoesse, la_liste = [], [], []
    for raum in raeume:
        laengen = raum_fassaden(raum, fp, h)
        s_g = Polygon(raum["polygon"]).area
        zeile = {"raum": raum["name"], "geschoss": raum["geschoss"], "schutzbeduerftig": raum["schutzbeduerftig"],
                 "schlafnutzung": raum["schlafen"], "fassaden": laengen, "flaeche_m2": round(s_g, 2)}
        if raum.get("bemerkung"):
            zeile["bemerkung"] = raum["bemerkung"]
        if not raum["schutzbeduerftig"]:
            zeile["ergebnis"] = "nicht schutzbedürftig (DIN 4109-1, 3.16): keine Anforderung"
            zeilen.append(zeile)
            continue
        if not laengen:
            zeile["ergebnis"] = "keine Außenfläche"
            zeilen.append(zeile)
            continue
        res = waehle_bauteile(raum, laengen, s_g, h, pegel, katalog, lueftung)
        pr = res["pruefung"]
        z = pr["zeitraeume"][pr["massgebend"]]
        la_liste.append((raum["nutzung"], z["la_max"]))
        zeile.update({"massgebend": pr["massgebend"], "la_max": z["la_max"], "erf_rw_ges": z["erf_rw_ges"],
                      "k_al": z["k_al"], "ziel_rw_ges_minus_2": z["ziel"], "rw_ges": z["rw_ges"],
                      "reserve": z["reserve"], "erfuellt": pr["erfuellt"], "stufe": res["stufe"],
                      "wahl": res["wahl"], "mehrkosten_eur": res["mehrkosten_eur"],
                      "max_klasse": max(res["wahl"]["klasse"].values()) if res["wahl"]["klasse"] else None,
                      "zeitraeume": pr["zeitraeume"]})
        if not res["gefunden"]:
            verstoesse.append({"raum": raum["name"], "regel": "DIN 4109-1, 7.1 / DIN 4109-2, Gl. (32)",
                               "text": f"Anforderung {z['ziel']:.1f} dB (inkl. K_AL) mit Katalog nicht erreichbar "
                                       f"(max. {z['rw_ges_minus_uprog']:.1f} dB nach Abzug u_prog)"})
        elif res["stufe"] != "Regnauer-Katalog":
            verstoesse.append({"raum": raum["name"], "regel": "Katalogregel (Firma)",
                               "text": "nur mit Fremdprodukt (SSK 5/6 oder mehrflüglig > SSK 2) nachweisbar"})
        if z["erf_rw_ges"] > EINZELFALL_RWGES or z["la_max"] > EINZELFALL_LA:
            verstoesse.append({"raum": raum["name"], "regel": "BayTB Anl. A 5.2/1 Nr. 1 und 3",
                               "text": "R'w,ges > 50 dB oder La > 80 dB: Bauaufsicht legt fest, Messung nötig"})
        zeilen.append(zeile)
    pflicht, grund = baytb_nachweis_erforderlich(la_liste, eingabe["bplan"]["festsetzung_9_1_24"])
    geschuetzt = [z for z in zeilen if "erf_rw_ges" in z]
    return {"raeume": zeilen, "regelverstoesse": verstoesse,
            "baytb_nachweis_erforderlich": pflicht, "baytb_grund": grund,
            "summe_mehrkosten_eur": round(sum(z["mehrkosten_eur"] for z in geschuetzt), 2),
            "max_klasse": max((z["max_klasse"] or 0) for z in geschuetzt) if geschuetzt else None,
            "anzahl_fenster_ssk_ab_4": zaehle_fenster(geschuetzt, raeume, 4)}


def zaehle_fenster(zeilen: list[dict], raeume: list[dict], ab_klasse: int) -> int:
    """Anzahl Fenster mit gewählter Klasse ≥ ab_klasse."""
    nach_name = {(r["geschoss"], r["name"]): r for r in raeume}
    n = 0
    for z in zeilen:
        raum = nach_name[(z["geschoss"], z["raum"])]
        for r, k in z["wahl"]["klasse"].items():
            if k >= ab_klasse:
                n += len(raum["fenster"].get(r, []))
    return n


def fensterverzicht_test(eingabe: dict, raeume: list[dict], pegel: dict, lueftung: str) -> list[dict]:
    """Assistenz: Schlafräume mit Fenstern an ≥ 2 Fassaden – was bringt es, die
    Fenster an der lautesten Fassade wegzulassen (mind. 1 Fenster bleibt)?"""
    fp = Polygon(eingabe["haus"]["footprint"])
    h = eingabe["haus"]["raumhoehe"]
    out = []
    for raum in raeume:
        if not (raum["schutzbeduerftig"] and raum["schlafen"]):
            continue
        mit_fenster = [r for r, fl in raum["fenster"].items() if fl]
        if len(mit_fenster) < 2:
            continue
        laut = max(mit_fenster, key=lambda r: (pegel[r]["la_schlaf"], r))
        if pegel[laut]["la_schlaf"] - min(pegel[r]["la_schlaf"] for r in mit_fenster) < 3.0:
            continue   # Fassaden etwa gleich laut (< 3 dB Unterschied): kein nennenswerter Gewinn
        laengen = raum_fassaden(raum, fp, h)
        s_g = Polygon(raum["polygon"]).area
        vorher = waehle_bauteile(raum, laengen, s_g, h, pegel, eingabe["katalog"], lueftung)
        r2 = copy.deepcopy(raum)
        r2["fenster"][laut] = []
        nachher = waehle_bauteile(r2, laengen, s_g, h, pegel, eingabe["katalog"], lueftung)
        out.append({"raum": raum["name"], "fassade_ohne_fenster": laut,
                    "vorher": {"klassen": vorher["wahl"]["klasse"], "eur": vorher["mehrkosten_eur"], "stufe": vorher["stufe"]},
                    "nachher": {"klassen": nachher["wahl"]["klasse"], "eur": nachher["mehrkosten_eur"], "stufe": nachher["stufe"]},
                    "hinweis": "Mindestfensterfläche/Belichtung (Art. 45 BayBO) und zweiten Rettungsweg prüfen"})
    return out


def empfehlungen(eingabe: dict, pegel: dict, varianten: dict, lueftung: str) -> list[dict]:
    """Assistenz-Empfehlungen (Laientext + Fachtext + Quelle)."""
    out = []
    q = eingabe["quellen"][0]
    a, b = varianten["A_ursprung"], varianten["B_tausch"]
    # 1. Grundrisstausch
    def schlaf(v):
        return {z["raum"]: z for z in v["raeume"] if z.get("schlafnutzung") and "erf_rw_ges" in z}
    sa, sb = schlaf(a), schlaf(b)
    delta = {n: round(sa[n]["erf_rw_ges"] - sb[n]["erf_rw_ges"], 1) for n in sa if n in sb}
    besser = b["summe_mehrkosten_eur"] < a["summe_mehrkosten_eur"] or len(b["regelverstoesse"]) < len(a["regelverstoesse"])
    out.append({"id": "E1-grundriss-tausch", "prioritaet": 1 if besser else 3,
                "laie": ("Legen Sie Schlafzimmer und Kinderzimmer auf die Südseite. Dort ist es nachts deutlich leiser. "
                         f"Die Fenster brauchen dann eine niedrigere Schallschutzklasse, das spart ca. "
                         f"{a['summe_mehrkosten_eur'] - b['summe_mehrkosten_eur']:.0f} € (Beispielpreise)."),
                "fach": ("Variante B senkt erf R'w,ges der Schlafräume um "
                         + ", ".join(f"{n} {d:.1f} dB" for n, d in sorted(delta.items())) + "; max. Fensterklasse "
                         f"{a['max_klasse']} → {b['max_klasse']}; Regelverstöße {len(a['regelverstoesse'])} → "
                         f"{len(b['regelverstoesse'])}; Mehrkosten {a['summe_mehrkosten_eur']:.0f} € → "
                         f"{b['summe_mehrkosten_eur']:.0f} €."),
                "quelle": "DIN 4109-2, 4.4.5.1 (−5 dB abgewandte Seite); BVerwG 4 CN 2.06; BVerwG 4 BN 8.15",
                "evidenz": "N (Norm) / Recht"})
    # 2. Lüftungskonzept
    ln_nord = max(qq["lr_nacht"] for qq in pegel["N"]["quellen"])
    if ln_nord > LUEFTUNG_NACHT_BBL:
        text_kwl = ("Die zentrale Lüftung mit Wärmerückgewinnung (Regnauer-Standard) erfüllt das; "
                    "Außen- und Fortluftdurchlässe mit Schalldämpfer planen.") if lueftung == "KWL" else \
            ("Bei dezentraler Lüftung: schallgedämmte Außenwandluftdurchlässe (ALD) – sie gehen in den Nachweis ein.")
        out.append({"id": "E2-lueftung", "prioritaet": 1,
                    "laie": ("An der Nordseite ist es nachts so laut, dass man bei gekipptem Fenster schlecht schläft. "
                             "Schlafräume brauchen eine Lüftung, die ohne Fensteröffnen funktioniert. " + text_kwl),
                    "fach": (f"Lr,N an der Nordfassade {ln_nord:.0f} dB(A) > {LUEFTUNG_NACHT_BBL:.0f} dB(A) "
                             f"(DIN 18005 Bbl. 1, Hinweis) bzw. > {LUEFTUNG_NACHT_VDI:.0f} dB(A) (VDI 2719, Abschn. 10): "
                             "fensterunabhängige, schallgedämmte Lüftung der Schlafräume; Lüftungskonzept nach DIN 1946-6 "
                             "(Recherche 08). Schallschutz wirkt nur bei geschlossenem Fenster (DIN 4109-1, 7.3)."),
                    "quelle": "DIN 4109-1:2018, 7.3; VDI 2719:1987; DIN 1946-6:2019-12; BVerwG 4 C 4.05",
                    "evidenz": "N / Recht; Schwellen [U]"})
    # 3. Nachweispflicht
    out.append({"id": "E3-nachweispflicht", "prioritaet": 2,
                "laie": ("Für dieses Grundstück ist ein rechnerischer Schallschutznachweis gegen Außenlärm Pflicht."
                         if a["baytb_nachweis_erforderlich"] else "Ein Schallschutznachweis gegen Außenlärm ist nicht Pflicht."),
                "fach": f"BayTB 11/2025 Anl. A 5.2/1 Nr. 5: {a['baytb_grund']}. Bautechnischer Nachweis nach Art. 62 BayBO, § 12 BauVorlV.",
                "quelle": "BayTB Ausgabe November 2025; BayBO Art. 62; BauVorlV § 12", "evidenz": "N/Recht"})
    # 4. Abstand vs. Abschirmung
    achse = LineString(q["achse"])
    grund = Polygon(eingabe["grundstueck"]["polygon"])
    d_jetzt = achse.distance(Point(q["bezugspunkt"]))
    d_sued = achse.distance(Point(q["bezugspunkt"][0], grund.bounds[1] + 8.0))
    gewinn = 10 * math.log10(d_sued / d_jetzt)
    out.append({"id": "E4-abstand-riegel", "prioritaet": 3,
                "laie": (f"Das Haus weiter nach Süden zu schieben bringt nur ca. {abs(gewinn):.1f} dB – kaum hörbar. "
                         "Wirksam sind die Grundrissorientierung und ggf. eine Garage oder Wand im Norden als Riegel."),
                "fach": (f"Linienquelle: ΔL = 10 lg({d_sued:.0f}/{d_jetzt:.0f}) = {gewinn:.1f} dB (ANNAHME Freifeld). "
                         "Abschirmung durch Nebengebäude/Lärmschutzwand nur mit Gutachten (16. BImSchV/RLS-19) anrechenbar "
                         "(DIN 4109-2, 4.4.5.1)."),
                "quelle": "DIN 4109-2, 4.4.5.1; RLS-19", "evidenz": "Physik/N"})
    # 5. Außenwohnbereich
    lr_t_sued = max(qq["lr_tag"] for qq in pegel["S"]["quellen"])
    if lr_t_sued > OW_WA[0]:
        out.append({"id": "E5-terrasse", "prioritaet": 3,
                    "laie": "Auch auf der Südterrasse ist die Autobahn zu hören. Eine Terrasse im Windschatten des Hauses oder eine Mauer hilft.",
                    "fach": f"Lr,T Südfassade ≈ {lr_t_sued:.0f} dB(A) > OW WA {OW_WA[0]:.0f} dB(A) (DIN 18005 Bbl. 1:2023, kein Grenzwert).",
                    "quelle": "DIN 18005 Beiblatt 1:2023-07", "evidenz": "N (Orientierungswert)"})
    # 6. WHO
    eu = q.get("eu_laermkarte")
    if eu and (eu["lden"] > WHO_STRASSE[0] or eu["lnight"] > WHO_STRASSE[1]):
        out.append({"id": "E6-who", "prioritaet": 4,
                    "laie": ("Die Lärmkarte zeigt Werte, bei denen die Weltgesundheitsorganisation gesundheitliche Folgen "
                             "erwartet. Das ist kein Bauverbot, aber ein Grund, Schlafräume ruhig zu legen."),
                    "fach": (f"EU-Lärmkarte Lden {eu['lden']:.0f} / Lnight {eu['lnight']:.0f} dB > WHO-Empfehlung Straße "
                             f"{WHO_STRASSE[0]:.0f}/{WHO_STRASSE[1]:.0f} dB (WHO 2018, Evidenzgrad A in Recherche 15). "
                             "EU-Lärmkarten sind für La nicht zulässig (DIN 4109-2, 4.4.5.2, Anm.)."),
                    "quelle": "WHO 2018; DIN 4109-2:2018, 4.4.5.2", "evidenz": "A (Wirkung), nicht bindend"})
    return sorted(out, key=lambda e: (e["prioritaet"], e["id"]))


def berechne(eingabe: dict | None = None, modus: str = "nachweis", lueftung: str | None = None) -> dict:
    eingabe = copy.deepcopy(eingabe or beispiel_eingabe())
    lueftung = lueftung or eingabe["lueftung"]
    pegel = fassadenpegel(eingabe, modus)
    varianten = {name: werte_variante_aus(eingabe, raeume, pegel, lueftung)
                 for name, raeume in sorted(eingabe["varianten"].items())}
    verzicht = {name: fensterverzicht_test(eingabe, raeume, pegel, lueftung)
                for name, raeume in sorted(eingabe["varianten"].items())}
    a, b = varianten["A_ursprung"], varianten["B_tausch"]
    anders_planen = bool(a["regelverstoesse"]) or (a["summe_mehrkosten_eur"] - b["summe_mehrkosten_eur"] > 0)
    return {
        "b19": "Schallschutz gegen Außenlärm – Beispielrechnung",
        "hinweis": eingabe["hinweis"],
        "modus": modus, "lueftung": lueftung,
        "nachweis_tauglich": all(p["nachweis_tauglich"] for p in pegel.values()),
        "fassadenpegel": pegel,
        "varianten": varianten,
        "fensterverzicht": verzicht,
        "vergleich": {
            "mehrkosten_eur": {"A": a["summe_mehrkosten_eur"], "B": b["summe_mehrkosten_eur"]},
            "max_klasse": {"A": a["max_klasse"], "B": b["max_klasse"]},
            "fenster_ab_ssk4": {"A": a["anzahl_fenster_ssk_ab_4"], "B": b["anzahl_fenster_ssk_ab_4"]},
            "regelverstoesse": {"A": len(a["regelverstoesse"]), "B": len(b["regelverstoesse"])},
            "empfehlung_anders_planen": anders_planen,
        },
        "empfehlungen": empfehlungen(eingabe, pegel, varianten, lueftung),
        "annahmen": [
            "Bezugspegel Lr,T/Lr,N sind Beispielwerte (wie aus Gutachten nach RLS-19), keine Lärmkarte.",
            "Ausbreitung am Haus: lange Linienquelle (3 dB je Abstandsverdopplung) und Sichtwinkelanteil; keine Reflexionen, "
            "kein Boden, keine Meteorologie, keine Geschosshöhe.",
            "Modus 'nachweis': Minderung nur an Fassaden ohne Sicht (−5 dB, DIN 4109-2, 4.4.5.1).",
            "Fenster-Rw = Prüfstandswert der VDI-2719-Klasse; Außenwand-Rw 47 dB (Beispiel).",
            "ALD je schutzbedürftigem Raum an der lautesten Fassade; Rollladenkästen als Element D_n,e,w.",
            "Nachtregel je Quelle vor der Summenbildung (Auslegung [U]).",
            "Dach/Decke zum Dachraum nicht betrachtet (DIN 4109-1, 7.2 gesondert).",
            "Preise sind frei gewählte Beispiel-Mehrpreise.",
        ],
    }


# ---------------------------------------------------------------------------
# 6. Ausgabe: Markdown-Tabelle, optional IFC4X3_ADD2
# ---------------------------------------------------------------------------

def als_markdown(erg: dict) -> str:
    z = [f"# B19 Außenlärm – Ergebnis (Modus {erg['modus']}, Lüftung {erg['lueftung']})", "",
         "**Alle Zahlen sind Beispielwerte.**", "", "## Fassadenpegel", "",
         "| Fassade | Lr,T | Lr,N | Sichtanteil | ΔL Orient. | La,Tag | La,Schlaf |", "|---|---|---|---|---|---|---|"]
    for r, p in erg["fassadenpegel"].items():
        q = p["quellen"][0]
        z.append(f"| {r} | {q['lr_tag']:.1f} | {q['lr_nacht']:.1f} | {q['sichtanteil']:.2f} | {q['dL_orientierung']:+.1f} "
                 f"| {p['la_tag']:.1f} | {p['la_schlaf']:.1f} |")
    for name, v in erg["varianten"].items():
        z += ["", f"## Variante {name}", "",
              "| Raum | Fassaden | maßg. | La,max | erf R'w,ges | K_AL | Ziel (erf+K_AL) | R'w,ges−2 | Klassen | RK | ALD | Mehrkosten |",
              "|---|---|---|---|---|---|---|---|---|---|---|---|"]
        for r in v["raeume"]:
            if r["geschoss"] != "OG" and r["raum"] != "Wohnen/Essen":
                continue
            if "erf_rw_ges" not in r:
                z.append(f"| {r['raum']} ({r['geschoss']}) | {','.join(r['fassaden'])} | – | – | – | – | – | – | – | – | – | {r['ergebnis'][:28]} |")
                continue
            zt = r["zeitraeume"][r["massgebend"]]
            kl = ", ".join(f"{k}:{v2}" for k, v2 in r["wahl"]["klasse"].items())
            z.append(f"| {r['raum']} ({r['geschoss']}) | {','.join(r['fassaden'])} | {r['massgebend']} | {r['la_max']:.1f} | "
                     f"{r['erf_rw_ges']:.1f} | {r['k_al']:.1f} | {r['ziel_rw_ges_minus_2']:.1f} | {zt['rw_ges_minus_uprog']:.1f} | "
                     f"SSK {kl} | {r['wahl']['rollladen'].replace('Aufsatzkasten ', 'AK ')} | {r['wahl']['ald'] or '–'} | "
                     f"{r['mehrkosten_eur']:.0f} € |")
            if r["wahl"].get("ald_fassade"):
                z[-1] = z[-1].replace(f"| {r['wahl']['ald']} |", f"| {r['wahl']['ald']} ({r['wahl']['ald_fassade']}) |")
        z += ["", f"Summe Mehrkosten: {v['summe_mehrkosten_eur']:.0f} € · max. Klasse: {v['max_klasse']} · "
                  f"BayTB-Nachweis: {'ja' if v['baytb_nachweis_erforderlich'] else 'nein'} ({v['baytb_grund']})"]
        for rv in v["regelverstoesse"]:
            z.append(f"- **Verstoß** {rv['raum']}: {rv['text']} ({rv['regel']})")
    z += ["", "## Empfehlungen", ""]
    for e in erg["empfehlungen"]:
        z.append(f"- **{e['id']}** (Prio {e['prioritaet']}): {e['laie']}  \n  _Fach:_ {e['fach']}  \n  _Quelle:_ {e['quelle']}")
    return "\n".join(z) + "\n"


def exportiere_ifc(erg: dict, eingabe: dict, variante: str, pfad: Path) -> Path:
    """Minimale IFC4X3_ADD2-Datei: Räume mit Anforderungs-Pset, Fenster mit
    Pset_WindowCommon.AcousticRating, Fassaden-Immissionsorte als IfcAnnotation.
    Eigene Psets mit Präfix „HB_“ (nicht „Pset_“, das ist buildingSMART vorbehalten)."""
    import ifcopenshell
    import ifcopenshell.guid

    f = ifcopenshell.file(schema="IFC4X3_ADD2")
    g = lambda pfad_: ifcopenshell.guid.compress(uuid.uuid5(GUID_NAMENSRAUM, f"{variante}{pfad_}").hex)  # noqa: E731
    einheiten = f.create_entity("IfcUnitAssignment", Units=[
        f.create_entity("IfcSIUnit", UnitType="LENGTHUNIT", Name="METRE"),
        f.create_entity("IfcSIUnit", UnitType="AREAUNIT", Name="SQUARE_METRE")])
    ursprung = f.create_entity("IfcAxis2Placement3D", Location=f.create_entity("IfcCartesianPoint", Coordinates=(0.0, 0.0, 0.0)))
    kontext = f.create_entity("IfcGeometricRepresentationContext", ContextType="Model", CoordinateSpaceDimension=3,
                              Precision=1e-5, WorldCoordinateSystem=ursprung)
    projekt = f.create_entity("IfcProject", GlobalId=g("/projekt"), Name=f"B19 Außenlärm {variante}",
                              UnitsInContext=einheiten, RepresentationContexts=[kontext])
    site = f.create_entity("IfcSite", GlobalId=g("/site"), Name="Grundstück (Beispiel)")
    bau = f.create_entity("IfcBuilding", GlobalId=g("/building"), Name="Holzrahmenhaus (Beispiel)")
    geschosse = {n: f.create_entity("IfcBuildingStorey", GlobalId=g(f"/storey/{n}"), Name=n, Elevation=e)
                 for n, e in (("EG", 0.0), ("OG", 2.75))}
    f.create_entity("IfcRelAggregates", GlobalId=g("/rel/p-s"), RelatingObject=projekt, RelatedObjects=[site])
    f.create_entity("IfcRelAggregates", GlobalId=g("/rel/s-b"), RelatingObject=site, RelatedObjects=[bau])
    f.create_entity("IfcRelAggregates", GlobalId=g("/rel/b-g"), RelatingObject=bau, RelatedObjects=list(geschosse.values()))

    def pset(ziel, name, props: dict, pfad_: str):
        werte = []
        for k, (typ, v) in props.items():
            werte.append(f.create_entity("IfcPropertySingleValue", Name=k, NominalValue=f.create_entity(typ, v)))
        ps = f.create_entity("IfcPropertySet", GlobalId=g(f"/pset/{pfad_}"), Name=name, HasProperties=werte)
        f.create_entity("IfcRelDefinesByProperties", GlobalId=g(f"/rdp/{pfad_}"), RelatingPropertyDefinition=ps,
                        RelatedObjects=[ziel])

    # Fassaden-Immissionsorte
    orte = []
    for r, p in erg["fassadenpegel"].items():
        q = p["quellen"][0]
        a = f.create_entity("IfcAnnotation", GlobalId=g(f"/io/{r}"), Name=f"Immissionsort Fassade {r}",
                            ObjectType="Immissionsort", PredefinedType="USERDEFINED")
        pset(a, "HB_Fassadenpegel", {
            "Himmelsrichtung": ("IfcLabel", r),
            "LrTag": ("IfcSoundPressureLevelMeasure", float(q["lr_tag"])),
            "LrNacht": ("IfcSoundPressureLevelMeasure", float(q["lr_nacht"])),
            "LaTag": ("IfcSoundPressureLevelMeasure", float(p["la_tag"])),
            "LaSchlaf": ("IfcSoundPressureLevelMeasure", float(p["la_schlaf"])),
            "Verfahren": ("IfcLabel", str(q["verfahren"])),
            "Annahme": ("IfcText", q["begruendung"]),
        }, f"io/{r}")
        orte.append(a)
    f.create_entity("IfcRelContainedInSpatialStructure", GlobalId=g("/rel/io"), RelatingStructure=site, RelatedElements=orte)

    raeume = {(r["geschoss"], r["name"]): r for r in eingabe["varianten"][variante]}
    kl = {k["klasse"]: k for k in eingabe["katalog"]["fenster"]}
    je_geschoss: dict[str, list] = {"EG": [], "OG": []}
    fenster_je_geschoss: dict[str, list] = {"EG": [], "OG": []}
    for z in erg["varianten"][variante]["raeume"]:
        sp = f.create_entity("IfcSpace", GlobalId=g(f"/space/{z['geschoss']}/{z['raum']}"), Name=z["raum"],
                             PredefinedType="SPACE")
        je_geschoss[z["geschoss"]].append(sp)
        props = {"Schutzbeduerftig": ("IfcBoolean", bool(z["schutzbeduerftig"])),
                 "Schlafnutzung": ("IfcBoolean", bool(z["schlafnutzung"]))}
        if "erf_rw_ges" in z:
            props.update({"KRaumart": ("IfcReal", K_RAUMART["wohnen"]),
                          "LaMassgeblich": ("IfcSoundPressureLevelMeasure", float(z["la_max"])),
                          "ErfRwGes": ("IfcReal", float(z["erf_rw_ges"])), "KAL": ("IfcReal", float(z["k_al"])),
                          "RwGesVorhanden": ("IfcReal", float(z["rw_ges"])),
                          "NachweisErfuellt": ("IfcBoolean", bool(z["erfuellt"])),
                          "Normgrundlage": ("IfcLabel", "DIN 4109-1:2018-01 7.1; DIN 4109-2:2018-01 4.4")})
        pset(sp, "HB_Aussenlaerm_Raum", props, f"space/{z['geschoss']}/{z['raum']}")
        raum = raeume[(z["geschoss"], z["raum"])]
        for r, fl in sorted(raum["fenster"].items()):
            for i, fe in enumerate(fl):
                klasse = z["wahl"]["klasse"].get(r, 2) if "wahl" in z else 2
                w = f.create_entity("IfcWindow", GlobalId=g(f"/win/{z['geschoss']}/{z['raum']}/{r}{i}"),
                                    Name=f"{z['raum']} {r}{i + 1}", OverallHeight=fe["h"], OverallWidth=fe["b"],
                                    PredefinedType="WINDOW")
                fenster_je_geschoss[z["geschoss"]].append(w)
                pset(w, "Pset_WindowCommon", {"AcousticRating": ("IfcLabel", f"Rw {kl[klasse]['rw']:.0f} dB (SSK {klasse} VDI 2719)")},
                     f"win/{z['geschoss']}/{z['raum']}/{r}{i}")
                pset(w, "HB_Schallschutz_Bauteil", {"Rw": ("IfcReal", kl[klasse]["rw"]),
                                                     "Schallschutzklasse": ("IfcInteger", klasse),
                                                     "Fassade": ("IfcLabel", r)},
                     f"hb/win/{z['geschoss']}/{z['raum']}/{r}{i}")
    for n, st in geschosse.items():
        f.create_entity("IfcRelAggregates", GlobalId=g(f"/rel/space/{n}"), RelatingObject=st, RelatedObjects=je_geschoss[n])
        if fenster_je_geschoss[n]:
            f.create_entity("IfcRelContainedInSpatialStructure", GlobalId=g(f"/rel/win/{n}"), RelatingStructure=st,
                            RelatedElements=fenster_je_geschoss[n])
    # fester Header, damit die Datei byte-identisch reproduzierbar ist
    h = f.header
    h.file_description.description = ("ViewDefinition [NotAssigned]",)
    h.file_name.name = pfad.name
    h.file_name.time_stamp = "2026-09-27T00:00:00"
    h.file_name.author = ("B19 Beispiel",)
    h.file_name.organization = ("Dissertation Holzbau (Beispiel)",)
    h.file_name.authorization = "keine"
    pfad.parent.mkdir(parents=True, exist_ok=True)
    f.write(str(pfad))
    return pfad


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--modus", choices=["nachweis", "planung"], default="nachweis")
    ap.add_argument("--lueftung", choices=["ALD", "KWL"], default=None)
    ap.add_argument("--ifc", action="store_true")
    args = ap.parse_args()
    eingabe = beispiel_eingabe()
    erg = berechne(eingabe, args.modus, args.lueftung)
    AUSGABE.mkdir(exist_ok=True)
    (AUSGABE / "b19_aussenlaerm.json").write_text(json.dumps(erg, ensure_ascii=False, indent=1, sort_keys=True), encoding="utf-8")
    md = als_markdown(erg)
    (AUSGABE / "b19_aussenlaerm.md").write_text(md, encoding="utf-8")
    if args.ifc:
        for v in ("A_ursprung", "B_tausch"):
            exportiere_ifc(erg, eingabe, v, AUSGABE / f"b19_aussenlaerm_{v[0]}.ifc")
    print(md)
    print(json.dumps(erg["vergleich"], ensure_ascii=False, sort_keys=True))


if __name__ == "__main__":
    main()

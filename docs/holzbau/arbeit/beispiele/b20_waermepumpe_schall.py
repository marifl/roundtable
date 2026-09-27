#!/usr/bin/env python3
"""
B20 – Schallimmissionsprognose und Standortoptimierung für Wärmepumpen-Außengeräte
(Monoblock R290 und Split) nach TA Lärm mit Ausbreitungsrechnung nach DIN ISO 9613-2.

Eingabe:  daten/b20_waermepumpe.json  (BEISPIELDATEN, keine Herstellerangaben)
Ausgabe:  ausgabe/b20_waermepumpe.json   vollständige Nachweise (Formel, Zwischenwert, Einheit, Quelle)
          ausgabe/b20_waermepumpe.md     Tabellen je Immissionsort
          ausgabe/b20_laermkarte.svg     Rasterlärmkarte L_r,Nacht mit Isolinien 35/40/45 dB(A)
          ausgabe/b20_standortkarte.svg  Raster der Aufstellorte: Reserve zum Irrelevanz-Zielwert

Rechenweg (je Punktquelle, je Pfad; A-bewertet mit den Dämpfungstermen bei 500 Hz nach
DIN ISO 9613-2:1999-10 = ISO 9613-2:1996, Abschnitt 1 Anm. 1; TA Lärm A.2.3.1 letzter Absatz):

    L_AT(DW) = L_WA + D_c − A                                       ISO 9613-2 Gl. (3)
    D_c      = D_I + D_Ω,  D_Ω nach Gl. (11) (Bodenreflexion, alternatives Verfahren 7.3.2)
    A        = A_div + A_atm + A_gr + A_bar                         Gl. (4), A_misc = 0
    A_div    = 20 lg(d/1 m) + 11 dB                                 Gl. (7)
    A_atm    = α·d/1000, α = 1,9 dB/km (500 Hz, 10 °C, 70 %)        Gl. (8), Tab. 2
    A_gr     = 4,8 − (2 h_m/d)(17 + 300/d) ≥ 0                      Gl. (10)
    A_bar    = D_z − A_gr > 0 (über die Kante), D_z (seitlich)      Gl. (12), (13)
    D_z      = 10 lg[3 + (C2/λ) C3 z K_met], C2 = 20                Gl. (14)
    C3       = [1 + (5λ/e)²] / [1/3 + (5λ/e)²]                      Gl. (15)
    z        = Umweg (Gummiband über bzw. um die Hindernisse)       Gl. (16), (17)
    K_met    = exp[−(1/2000)·√(d_ss·d_sr·d/(2z))] für z > 0, sonst 1  Gl. (18)
    Reflexion: Spiegelquelle, L_W,im = L_W + 10 lg ρ + D_Ir         Gl. (19), (20), Tab. 4
    Summe:   L_AT = 10 lg Σ 10^(0,1·L_i)                            Gl. (5)
    C_met    = 0 für d_p ≤ 10(h_s + h_r), sonst C0[1 − 10(h_s+h_r)/d_p]   Gl. (21), (22)

Beurteilung nach TA Lärm (1998, geändert 2017):
    L_r = 10 lg[(1/T_r) Σ T_j 10^(0,1(L_Aeq,j − C_met + K_T,j + K_I,j + K_R,j))]  Anhang A.1.4 (G2)
    Nacht: lauteste volle Nachtstunde (Nr. 6.4), K_R = 0; Tag: 16 h, K_R = 6 dB 06–07, 20–22 Uhr (Nr. 6.5)
    Richtwert Nr. 6.1, Spitzenpegel Nr. 6.1 letzter Satz, Irrelevanz Nr. 3.2.1 Abs. 2 (−6 dB)
    Rundung: Zwischenwerte ungerundet, Ausweisung 0,1 dB; L_r auf volle dB nach DIN 1333
    (LAI-Hinweise zur Auslegung der TA Lärm, Stand 24.02.2023, Anhang "Rundungsvorschriften").

Vereinfachungen (alle im Ergebnis dokumentiert): ebenes Gelände, poröser Boden (Garten),
Gebäude als Prismen mit Traufhöhe (Dach vernachlässigt → konservativ), konvexe Hindernisse,
seitliche Beugung nur auf dem Direktpfad, Spiegelquellen bis 2. Ordnung (2. Ordnung nur für
Flächen im Nahbereich der Quelle), keine Richtwirkung des Geräts (D_I = 0), keine tieffrequente
Beurteilung (DIN 45680 ist Messverfahren im Raum, keine Prognose), kein Körperschall.
Das Ergebnis ist KEIN Schallgutachten und KEINE Rechtsauskunft.

Aufruf:   python b20_waermepumpe_schall.py [--eingabe datei.json] [--ohne-karte]
"""
from __future__ import annotations

import argparse
import copy
import html
import json
import math
import re
from dataclasses import dataclass
from datetime import date, timedelta
from pathlib import Path

import numpy as np
from shapely.geometry import LineString, Point, Polygon

HIER = Path(__file__).resolve().parent
STANDARD_EINGABE = HIER / "daten" / "b20_waermepumpe.json"
AUSGABE = HIER / "ausgabe"

try:  # Nachweis-Modul der Arbeit (wird parallel gebaut) – falls vorhanden, nur vermerken
    import nachweis as _nachweis_modul  # noqa: F401
    NACHWEIS_MODUL = "vorhanden (nicht verwendet, JSON-Felder kompatibel gehalten)"
except ImportError:  # pragma: no cover - abhängig vom Stand des Repos
    NACHWEIS_MODUL = "nicht vorhanden → eigenes JSON-Format (regel, quelle, eingaben, schritte, ergebnis, grenzwert, ausnutzung, status)"

# --------------------------------------------------------------------------------------
# 1  Norm- und Richtwerte (jeweils mit Quelle)
# --------------------------------------------------------------------------------------
Q_TAL = "TA Lärm vom 26.08.1998 (GMBl S. 503), geändert 01.06.2017 (BAnz AT 08.06.2017 B5)"
Q_ISO = "DIN ISO 9613-2:1999-10 (= ISO 9613-2:1996), von TA Lärm A.2.3.4 in Bezug genommen"
Q_LAI = "LAI-Leitfaden stationäre Geräte, 3. Aktualisierung, Stand 28.08.2023 (UMK-Umlaufbeschluss 47/2023)"
Q_BWP = "BWP-Leitfaden Schall / BWP-Schallrechner (überschlägige Prognose TA Lärm A.2.4.3, G4)"

#: TA Lärm Nr. 6.1 (Immissionsrichtwerte außen, dB(A)): (tags, nachts)
IRW = {"GI": (70.0, 70.0), "GE": (65.0, 50.0), "MU": (63.0, 45.0), "MK": (60.0, 45.0),
       "MD": (60.0, 45.0), "MI": (60.0, 45.0), "WA": (55.0, 40.0), "WS": (55.0, 40.0),
       "WR": (50.0, 35.0), "KUR": (45.0, 35.0)}
#: TA Lärm Nr. 6.5 i. d. F. der Korrektur vom 07.07.2017 (Buchstaben e bis g): Zuschlag K_R = 6 dB
KR_GEBIETE = {"WA", "WS", "WR", "KUR"}
KR_WERT = 6.0
#: TA Lärm Nr. 6.4 / 6.5: Teilzeiten tags (Werktag) (Bezeichnung, Dauer h, K_R ja/nein)
TEILZEITEN_TAG = (("06–07 Uhr", 1.0, True), ("07–20 Uhr", 13.0, False), ("20–22 Uhr", 2.0, True))
SPITZE_TAG, SPITZE_NACHT = 30.0, 20.0   # TA Lärm Nr. 6.1 letzter Satz
IRRELEVANZ = 6.0                        # TA Lärm Nr. 3.2.1 Abs. 2; LAI 2023 Kap. 4.1.1

C_SCHALL = 340.0                        # ISO 9613-2 Gl. (19): λ = 340 m/s / f
C2 = 20.0                               # ISO 9613-2 Gl. (14): C2 = 20 (Bodenreflexion enthalten)
OKTAVEN = (63, 125, 250, 500, 1000, 2000, 4000, 8000)
#: ISO 9613-2 Tab. 2, 10 °C, 70 % rel. Feuchte, dB/km
ALPHA_OKTAV = {63: 0.1, 125: 0.4, 250: 1.0, 500: 1.9, 1000: 3.7, 2000: 9.7, 4000: 32.8, 8000: 117.0}

#: LAI 2023 Tab. 5 (Mindestabstand in m) für die Spalte WR; WA = WR um 5 dB verschoben,
#: MD/MI/MU/MK = WR um 10 dB verschoben (Spaltenstruktur der Tabelle, abgeleitet aus IRW-Differenzen)
LAI_TAB5_WR = (1.0, 1.1, 1.2, 1.4, 1.7, 1.9, 2.2, 2.6, 3.0, 3.4, 3.9, 4.5, 5.2, 5.9, 6.7, 7.6, 8.6, 9.7,
               10.9, 12.3, 13.9, 15.6, 17.6, 19.7, 22.2, 23.7, 25.4, 27.3, 29.4, 31.8, 34.4, 37.4, 40.8,
               44.6, 48.8, 53.6, 58.9, 64.9, 71.7, 79.2, 87.6)   # Emissionspegel 40 … 80 dB
LAI_HS, LAI_HR, LAI_ALPHA = 1.5, 2.0, 2.0   # LAI 2023 Kap. 4.1.3 (Modellannahmen)


def runde_din1333(x: float, stellen: int = 0) -> float:
    """Rundung nach DIN 1333:1992-02 Nr. 4.5.1 ("halben Stellenwert addieren, abschneiden");
    für negative Zahlen betragsweise. Beispiel: 40,5 → 41; 40,49 → 40."""
    f = 10.0 ** stellen
    s = -1.0 if x < 0 else 1.0
    return s * math.floor(abs(x) * f + 0.5 + 1e-9) / f


def r1(x: float) -> float:
    """Ausweisung von Zwischenwerten mit einer Nachkommastelle (nur Anzeige)."""
    return float(runde_din1333(x, 1))


def energiesumme(pegel) -> float:
    """L_ges = 10 lg Σ 10^(0,1 L_i)  (ISO 9613-2 Gl. 5; TA Lärm A.2.5.1 G5)."""
    werte = [p for p in pegel if p is not None and math.isfinite(p)]
    if not werte:
        return -math.inf
    return 10.0 * math.log10(sum(10.0 ** (0.1 * p) for p in werte))


# --------------------------------------------------------------------------------------
# 2  Nachweis-Objekt (strukturiertes JSON, kompatibel zu nachweis.py)
# --------------------------------------------------------------------------------------
class Nachweis:
    """Sammelt einen rechnerischen Nachweis: Regel, Quelle, Eingaben, Schritte, Ergebnis."""

    def __init__(self, regel: str, quelle: str):
        self.d = {"regel": regel, "quelle": quelle, "eingaben": [], "schritte": [],
                  "ergebnis": None, "grenzwert": None, "ausnutzung": None, "status": None}

    def eingabe(self, name, wert, einheit, quelle):
        self.d["eingaben"].append({"name": name, "wert": wert, "einheit": einheit, "quelle": quelle})
        return wert

    def schritt(self, formel, wert, einheit, beschreibung=""):
        self.d["schritte"].append({"formel": formel, "zwischenwert": wert if not isinstance(wert, float) else r1(wert),
                                   "zwischenwert_ungerundet": wert, "einheit": einheit,
                                   "beschreibung": beschreibung})
        return wert

    def abschluss(self, ergebnis, grenzwert, einheit, kleiner_gleich=True, status=None):
        self.d["ergebnis"] = {"wert": ergebnis, "einheit": einheit}
        self.d["grenzwert"] = {"wert": grenzwert, "einheit": einheit}
        if grenzwert not in (None, 0) and isinstance(ergebnis, (int, float)):
            self.d["ausnutzung"] = round(10 ** (0.1 * (ergebnis - grenzwert)), 3) if einheit.startswith("dB") \
                else round(ergebnis / grenzwert, 3)
        if status is None and isinstance(ergebnis, (int, float)) and isinstance(grenzwert, (int, float)):
            ok = ergebnis <= grenzwert if kleiner_gleich else ergebnis >= grenzwert
            status = "erfüllt" if ok else "nicht erfüllt"
        self.d["status"] = status
        return self.d


# --------------------------------------------------------------------------------------
# 3  Geometrie (konvexe Polygone, deterministisch, ohne Zufall)
# --------------------------------------------------------------------------------------
def konvexe_huelle(punkte):
    """Monotone-Chain-Hülle (Andrew), gegen den Uhrzeigersinn, ohne kollineare Punkte."""
    p = sorted(set((float(x), float(y)) for x, y in punkte))
    if len(p) <= 2:
        return p

    def kreuz(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    unten, oben = [], []
    for q in p:
        while len(unten) >= 2 and kreuz(unten[-2], unten[-1], q) <= 1e-12:
            unten.pop()
        unten.append(q)
    for q in reversed(p):
        while len(oben) >= 2 and kreuz(oben[-2], oben[-1], q) <= 1e-12:
            oben.pop()
        oben.append(q)
    return unten[:-1] + oben[:-1]


@dataclass(frozen=True)
class Hindernis:
    """Schallschirm/Reflektor: konvexes Prisma (Grundriss CCW, Höhe über Gelände)."""
    id: str
    name: str
    art: str            # "gebaeude" | "mauer"
    ecken: tuple        # ((x, y), …) gegen den Uhrzeigersinn
    hoehe: float
    rho: float

    @property
    def polygon(self) -> Polygon:
        return Polygon(self.ecken)

    def kanten(self):
        n = len(self.ecken)
        return [(self.ecken[i], self.ecken[(i + 1) % n]) for i in range(n)]


def mache_hindernis(id_, name, art, punkte, hoehe, rho) -> Hindernis:
    h = konvexe_huelle(punkte)
    if abs(Polygon(h).area - Polygon(punkte).area) > 1e-9:
        raise ValueError(f"Hindernis {id_} ist nicht konvex – bitte in konvexe Teile zerlegen")
    return Hindernis(id_, name, art, tuple(h), float(hoehe), float(rho))


def mauer_als_polygon(achse, dicke):
    (x0, y0), (x1, y1) = achse
    L = math.hypot(x1 - x0, y1 - y0)
    nx, ny = -(y1 - y0) / L * dicke / 2, (x1 - x0) / L * dicke / 2
    return [(x0 + nx, y0 + ny), (x0 - nx, y0 - ny), (x1 - nx, y1 - ny), (x1 + nx, y1 + ny)]


def clip_strecke(p0, p1, ecken, eps=1e-9):
    """Cyrus-Beck: Parameterintervall [t0, t1] ⊂ [0, 1] der Strecke p0→p1 im Inneren des
    konvexen CCW-Polygons, sonst None. Berührungen (Intervall < eps) zählen nicht."""
    dx, dy = p1[0] - p0[0], p1[1] - p0[1]
    te, tl = 0.0, 1.0
    n = len(ecken)
    for i in range(n):
        ax, ay = ecken[i]
        bx, by = ecken[(i + 1) % n]
        nx, ny = (by - ay), -(bx - ax)          # äußere Normale bei CCW
        num = nx * (ax - p0[0]) + ny * (ay - p0[1])
        den = nx * dx + ny * dy
        if abs(den) < 1e-15:
            if num < 0:
                return None
            continue
        t = num / den
        if den < 0:
            te = max(te, t)
        else:
            tl = min(tl, t)
        if te > tl:
            return None
    L = math.hypot(dx, dy)
    if (tl - te) * L < 1e-6 + eps:
        return None
    return te, tl


def spiegel(p, a, b):
    """Spiegelpunkt von p an der Geraden durch a, b (Grundriss)."""
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)
    fx, fy = a[0] + t * dx, a[1] + t * dy
    return (2 * fx - p[0], 2 * fy - p[1])


def schnitt_param(p, q, a, b):
    """Schnitt der Strecken p→q und a→b: (t auf p→q, u auf a→b) oder None."""
    rx, ry = q[0] - p[0], q[1] - p[1]
    sx, sy = b[0] - a[0], b[1] - a[1]
    den = rx * sy - ry * sx
    if abs(den) < 1e-15:
        return None
    t = ((a[0] - p[0]) * sy - (a[1] - p[1]) * sx) / den
    u = ((a[0] - p[0]) * ry - (a[1] - p[1]) * rx) / den
    return t, u


def vorderseite(p, a, b) -> float:
    """> 0, wenn p auf der Außenseite der CCW-Kante a→b liegt."""
    return (b[1] - a[1]) * (p[0] - a[0]) - (b[0] - a[0]) * (p[1] - a[1])


def abstand_punkt_strecke(p, a, b):
    dx, dy = b[0] - a[0], b[1] - a[1]
    t = max(0.0, min(1.0, ((p[0] - a[0]) * dx + (p[1] - a[1]) * dy) / (dx * dx + dy * dy)))
    return math.hypot(p[0] - a[0] - t * dx, p[1] - a[1] - t * dy)


# --------------------------------------------------------------------------------------
# 4  Dämpfungsterme DIN ISO 9613-2
# --------------------------------------------------------------------------------------
def a_div(d: float) -> float:
    """Gl. (7): A_div = 20 lg(d/d0) + 11 dB, d0 = 1 m."""
    return 20.0 * math.log10(d) + 11.0


def a_atm(d: float, alpha_db_km: float) -> float:
    """Gl. (8): A_atm = α d / 1000."""
    return alpha_db_km * d / 1000.0


def d_omega(dp: float, hs: float, hr: float) -> float:
    """Gl. (11): D_Ω = 10 lg{1 + [dp² + (hs − hr)²] / [dp² + (hs + hr)²]} dB."""
    return 10.0 * math.log10(1.0 + (dp ** 2 + (hs - hr) ** 2) / (dp ** 2 + (hs + hr) ** 2))


def a_gr_alternativ(d: float, hm: float) -> float:
    """Gl. (10): A_gr = 4,8 − (2 h_m / d)(17 + 300/d) ≥ 0 dB."""
    return max(0.0, 4.8 - (2.0 * hm / d) * (17.0 + 300.0 / d))


def c3_faktor(e: float, lam: float) -> float:
    """Gl. (15): C3 = [1 + (5λ/e)²] / [1/3 + (5λ/e)²]; e = 0 → C3 = 1."""
    if e <= 1e-9:
        return 1.0
    q = (5.0 * lam / e) ** 2
    return (1.0 + q) / (1.0 / 3.0 + q)


def k_met(dss: float, dsr: float, d: float, z: float) -> float:
    """Gl. (18): K_met = exp[−(1/2000) √(dss·dsr·d/(2z))] für z > 0, sonst 1."""
    if z <= 0:
        return 1.0
    return math.exp(-(1.0 / 2000.0) * math.sqrt(dss * dsr * d / (2.0 * z)))


def d_z(z: float, lam: float, c3: float, kmet: float, grenze: float) -> float:
    """Gl. (14): D_z = 10 lg[3 + (C2/λ) C3 z K_met]; z < 0 (Sichtlinie über der Kante) nach
    ISO 9613-2:1996 mit negativem Vorzeichen, Argument ≤ 1 → 0 dB; begrenzt auf 20/25 dB."""
    arg = 3.0 + (C2 / lam) * c3 * z * kmet
    if arg <= 1.0:
        return 0.0
    return min(10.0 * math.log10(arg), grenze)


# --------------------------------------------------------------------------------------
# 5  Pfade: Direktpfad mit Abschirmung (oben + seitlich) und Spiegelquellen
# --------------------------------------------------------------------------------------
def _oberer_rand(punkte):
    """Obere konvexe Hülle (Gummiband) einer nach s sortierten Punktfolge im Profil (s, h)."""
    h = []
    for p in punkte:
        while len(h) >= 2:
            (x1, y1), (x2, y2) = h[-2], h[-1]
            if (x2 - x1) * (p[1] - y1) - (y2 - y1) * (p[0] - x1) >= -1e-12:
                h.pop()
            else:
                break
        h.append(p)
    return h


def profil_ueber_kante(polylinie, hs, hr, hindernisse, lam, ausschluss=()):
    """Beugung über die Oberkanten entlang eines (ggf. gespiegelten, entfalteten) Pfads.

    polylinie: Grundrisspunkte [S, (P1, P2,) R]; Höhen linear entlang der entfalteten Länge.
    Rückgabe: dict mit z (m, negativ = Sichtlinie frei über Hindernis), dss, dsr, e, C3, K_met,
    D_z, Kanten, geschnittene Hindernisse – oder None, wenn kein Hindernis im Grundriss gekreuzt wird.
    """
    s_kum = [0.0]
    for a, b in zip(polylinie[:-1], polylinie[1:]):
        s_kum.append(s_kum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
    L = s_kum[-1]
    oben_punkte, gekreuzt = [], []
    for k, (a, b) in enumerate(zip(polylinie[:-1], polylinie[1:])):
        lk = s_kum[k + 1] - s_kum[k]
        for hi in hindernisse:
            if hi.id in ausschluss:
                continue
            iv = clip_strecke(a, b, hi.ecken)
            if iv is None:
                continue
            gekreuzt.append(hi.id)
            oben_punkte.append((s_kum[k] + iv[0] * lk, hi.hoehe, hi.id))
            oben_punkte.append((s_kum[k] + iv[1] * lk, hi.hoehe, hi.id))
    if not oben_punkte:
        return None
    S, R = (0.0, hs), (L, hr)
    d = math.hypot(L, hr - hs)
    pkt = [S] + sorted((p[0], p[1]) for p in oben_punkte) + [R]
    rand = _oberer_rand(pkt)
    kanten = rand[1:-1]
    if kanten:  # Sichtlinie unterbrochen: z > 0
        dss = math.hypot(kanten[0][0] - S[0], kanten[0][1] - S[1])
        dsr = math.hypot(R[0] - kanten[-1][0], R[1] - kanten[-1][1])
        e = sum(math.hypot(q[0] - p[0], q[1] - p[1]) for p, q in zip(kanten[:-1], kanten[1:]))
        z = dss + e + dsr - d
    else:       # Sichtlinie frei: z < 0 für die Kante mit dem kleinsten Umweg (Gl. 16, Vorzeichen)
        best = None
        for s, h, _ in oben_punkte:
            um = math.hypot(s, h - hs) + math.hypot(L - s, hr - h) - d
            if best is None or um < best[0]:
                best = (um, s, h)
        dss = math.hypot(best[1], best[2] - hs)
        dsr = math.hypot(L - best[1], hr - best[2])
        e, z = 0.0, -best[0]
    c3 = c3_faktor(e, lam)
    km = k_met(dss, dsr, d, z)
    grenze = 25.0 if e >= lam else 20.0   # ISO 9613-2 7.4: 20 dB Einfach-, 25 dB Doppelbeugung
    dz = d_z(z, lam, c3, km, grenze)
    return {"z_m": z, "dss_m": dss, "dsr_m": dsr, "e_m": e, "C3": c3, "K_met": km, "D_z_dB": dz,
            "grenze_dB": grenze, "anzahl_kanten": len(kanten), "sichtlinie_frei": not kanten,
            "hindernisse": sorted(set(gekreuzt))}


def seitliche_pfade(S, R, hs, hr, gekreuzte, alle, lam):
    """Seitliche Beugung um senkrechte Kanten (ISO 9613-2 Gl. 13, Bild 5): Gummiband im
    Grundriss links und rechts um die konvexe Hülle der gekreuzten Hindernisse; K_met = 1."""
    ergebnisse, verworfen = [], 0
    d_plan = math.hypot(R[0] - S[0], R[1] - S[1])
    d = math.hypot(d_plan, hr - hs)
    sS, sR = (float(S[0]), float(S[1])), (float(R[0]), float(R[1]))

    def ketten(gruppe):
        pts = [c for hi in gruppe for c in hi.ecken] + [sS, sR]
        huelle = konvexe_huelle(pts)
        if sS not in huelle or sR not in huelle:
            return None
        iS, iR, n = huelle.index(sS), huelle.index(sR), len(huelle)
        out = []
        for richtung in (1, -1):
            kette, i = [huelle[iS]], iS
            while i != iR:
                i = (i + richtung) % n
                kette.append(huelle[i])
            out.append(("links" if richtung == 1 else "rechts", kette))
        return out

    gruppen = [gekreuzte]
    k_ges = ketten(gekreuzte)
    if k_ges is None:          # Quelle/Empfänger liegt in der Hülle der Gruppe → einzeln
        gruppen = [[hi] for hi in gekreuzte]
    for gruppe in gruppen:
        kk = k_ges if len(gruppen) == 1 and k_ges is not None else ketten(gruppe)
        if kk is None:
            verworfen += 2
            continue
        ids = {hi.id for hi in gruppe}
        for seite, kette in kk:
            blockiert = any(clip_strecke(a, b, hi.ecken) is not None
                            for a, b in zip(kette[:-1], kette[1:]) for hi in alle if hi.id not in ids)
            if blockiert:
                verworfen += 1
                continue
            lc = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(kette[:-1], kette[1:]))
            kanten = kette[1:-1]
            e = sum(math.hypot(b[0] - a[0], b[1] - a[1]) for a, b in zip(kanten[:-1], kanten[1:]))
            z = math.hypot(lc, hr - hs) - d
            c3 = c3_faktor(e, lam)
            grenze = 25.0 if e >= lam else 20.0
            ergebnisse.append({"seite": seite, "gruppe": sorted(ids), "z_m": z, "e_m": e,
                               "C3": c3, "K_met": 1.0, "D_z_dB": d_z(z, lam, c3, 1.0, grenze),
                               "laenge_grundriss_m": lc, "kanten": [list(map(r1, k)) for k in kanten]})
    return ergebnisse, verworfen


class Szene:
    """Hindernisse, Reflexionsflächen und Rechenparameter einer Situation."""

    def __init__(self, daten: dict, mit_mauer: bool = True, rho_override: float | None = None):
        self.daten = daten
        b = daten["berechnung"]
        self.f = float(b["frequenz_Hz"])
        self.lam = C_SCHALL / self.f
        self.alpha = float(b["alpha_dB_km"])
        self.C0 = float(b["C0_dB"])
        self.ordnung = int(b["reflexion_ordnung_max"])
        self.r2 = float(b["reflexion_radius_2_ordnung_m"])
        self.io_fassade_ignorieren = bool(b["eigene_fassade_io_ignorieren"])
        self.hindernisse = []
        for g in daten["gebaeude"]:
            rho = g["rho"] if rho_override is None else rho_override
            self.hindernisse.append(mache_hindernis(g["id"], g["name"], "gebaeude", g["polygon"], g["hoehe_m"], rho))
        if mit_mauer:
            for m in daten["mauern"]:
                self.hindernisse.append(mache_hindernis(m["id"], m["name"], "mauer",
                                                        mauer_als_polygon(m["achse"], m["dicke_m"]),
                                                        m["hoehe_m"], m["rho"]))
        # Reflexionsflächen = Kanten aller Hindernisse (senkrechte Flächen), ρ ≥ 0,2 (ISO 7.5)
        self.flaechen = []
        for hi in self.hindernisse:
            for a, b2 in hi.kanten():
                if hi.rho >= 0.2:
                    self.flaechen.append({"hindernis": hi.id, "a": a, "b": b2, "hoehe": hi.hoehe, "rho": hi.rho,
                                          "laenge": math.hypot(b2[0] - a[0], b2[1] - a[1])})

    # ---- Spiegelquellen (quellenabhängig, einmal je Quelle berechnen) ------------------
    def spiegelquellen(self, S):
        """Liste der Spiegelquellen bis zur eingestellten Ordnung: (Bildpunkt, [Flächenindizes])."""
        bilder = []
        for i, f in enumerate(self.flaechen):
            if vorderseite(S, f["a"], f["b"]) <= 0:
                continue
            bilder.append((spiegel(S, f["a"], f["b"]), [i]))
        if self.ordnung >= 2:
            nah = [i for i, f in enumerate(self.flaechen) if abstand_punkt_strecke(S, f["a"], f["b"]) <= self.r2]
            erste = [(p, k) for p, k in bilder if k[0] in nah]
            for p1, k in erste:
                for j in nah:
                    if j == k[0]:
                        continue
                    f2 = self.flaechen[j]
                    if vorderseite(p1, f2["a"], f2["b"]) <= 0:
                        continue
                    bilder.append((spiegel(p1, f2["a"], f2["b"]), [k[0], j]))
        return bilder

    def _reflexionspfad(self, S, hs, R, hr, bild, kette, io_gebaeude, lam):
        """Prüft einen Spiegelpfad und liefert seine Kenngrößen (oder None, wenn ungültig)."""
        # Reflexionspunkte rückwärts konstruieren: letzter Spiegel zuerst
        bildpunkte = [S]
        for idx in kette:
            f = self.flaechen[idx]
            bildpunkte.append(spiegel(bildpunkte[-1], f["a"], f["b"]))
        ziel = R
        punkte = []
        for stufe in range(len(kette), 0, -1):
            f = self.flaechen[kette[stufe - 1]]
            if self.io_fassade_ignorieren and io_gebaeude and f["hindernis"] == io_gebaeude:
                return None
            quelle_bild = bildpunkte[stufe]
            if vorderseite(ziel, f["a"], f["b"]) <= 0:
                return None
            sp = schnitt_param(quelle_bild, ziel, f["a"], f["b"])
            if sp is None or not (1e-9 < sp[0] < 1 - 1e-9) or not (0.0 <= sp[1] <= 1.0):
                return None
            P = (quelle_bild[0] + sp[0] * (ziel[0] - quelle_bild[0]), quelle_bild[1] + sp[0] * (ziel[1] - quelle_bild[1]))
            punkte.insert(0, (P, f))
            ziel = P
        poly = [S] + [p for p, _ in punkte] + [R]
        s_kum = [0.0]
        for a, b in zip(poly[:-1], poly[1:]):
            s_kum.append(s_kum[-1] + math.hypot(b[0] - a[0], b[1] - a[1]))
        Lp = s_kum[-1]
        rho_ges, pruef = 1.0, []
        for k, (P, f) in enumerate(punkte):
            hP = hs + (hr - hs) * s_kum[k + 1] / Lp
            if hP > f["hoehe"] or hP < 0:
                return None
            # Mindestgröße der Fläche, ISO 9613-2 Gl. (19)
            dso = math.hypot(s_kum[k + 1], hP - hs)
            dor = math.hypot(Lp - s_kum[k + 1], hr - hP)
            ux, uy = (poly[k + 1][0] - poly[k][0]), (poly[k + 1][1] - poly[k][1])
            fx, fy = (f["b"][0] - f["a"][0]) / f["laenge"], (f["b"][1] - f["a"][1]) / f["laenge"]
            lu = math.hypot(ux, uy)
            cosb = abs(ux * (-fy) + uy * fx) / lu if lu > 0 else 1.0  # |cos β| zur Flächennormalen
            lmin = min(f["laenge"], f["hoehe"])
            if cosb < 1e-6 or 1.0 / lam <= (2.0 / (lmin * cosb) ** 2) * (dso * dor / (dso + dor)):
                return None
            rho_ges *= f["rho"]
            pruef.append({"flaeche": f"{f['hindernis']}:{list(map(r1, f['a']))}–{list(map(r1, f['b']))}",
                          "rho": f["rho"], "h_reflexion_m": r1(hP)})
        return poly, Lp, rho_ges, pruef

    # ---- Immissionspegel an einem Punkt ------------------------------------------------
    def pegel(self, S, hs, R, hr, LW, io_gebaeude=None, lam=None, alpha=None, bilder=None,
              mit_details=False, DI=0.0):
        """A-bewerteter Mitwind-Mittelungspegel L_AT(DW) am Punkt R für die Quelle S."""
        lam = self.lam if lam is None else lam
        alpha = self.alpha if alpha is None else alpha
        hm = (hs + hr) / 2.0            # ebenes Gelände: mittlere Höhe (ISO 9613-2 Bild 3)
        beitraege, details = [], {}
        # --- Direktpfad ---
        dp = math.hypot(R[0] - S[0], R[1] - S[1])
        d = math.hypot(dp, hr - hs)
        adiv, aatm = a_div(d), a_atm(d, alpha)
        agr, dom = a_gr_alternativ(d, hm), d_omega(dp, hs, hr)
        prof = profil_ueber_kante([S, R], hs, hr, self.hindernisse, lam)
        seitlich, verworfen = [], 0
        if prof is None:
            abar = 0.0
        elif prof["sichtlinie_frei"]:
            abar = max(prof["D_z_dB"] - agr, 0.0)
        else:
            teil = [max(prof["D_z_dB"] - agr, 0.0)]                      # Gl. (12)
            gekreuzt = [h for h in self.hindernisse if h.id in prof["hindernisse"]]
            seitlich, verworfen = seitliche_pfade(S, R, hs, hr, gekreuzt, self.hindernisse, lam)
            # Relevanz seitlicher Pfade: nur wenn z_seitlich ≤ 8·z_oben (Praxisregel nach ISO/TR 17534-3,
            # zitiert u. a. im EMD-WindPRO-Handbuch; verhindert, dass sehr lange Schirme über die 20-dB-Kappung
            # immer −20 dB "Umwegenergie" erhalten) [U]
            relevant = [p for p in seitlich if p["z_m"] <= 8.0 * prof["z_m"]]
            for p in seitlich:
                p["relevant"] = p in relevant
            teil += [p["D_z_dB"] for p in relevant]                       # Gl. (13)
            abar = -10.0 * math.log10(sum(10.0 ** (-0.1 * a) for a in teil))  # Pfade energetisch (ISO 7.4)
        L_dir = LW + DI + dom - adiv - aatm - agr - abar
        beitraege.append(L_dir)
        cmet = 0.0 if dp <= 10.0 * (hs + hr) else self.C0 * (1.0 - 10.0 * (hs + hr) / dp)
        if mit_details:
            details["direkt"] = {"d_m": d, "dp_m": dp, "A_div_dB": adiv, "A_atm_dB": aatm, "A_gr_dB": agr,
                                 "D_Omega_dB": dom, "D_I_dB": DI, "A_bar_dB": abar, "L_dB": L_dir,
                                 "oben": prof, "seitlich": seitlich, "seitlich_verworfen": verworfen}
        # --- Spiegelquellen ---
        refl = []
        for bild, kette in (self.spiegelquellen(S) if bilder is None else bilder):
            r = self._reflexionspfad(S, hs, R, hr, bild, kette, io_gebaeude, lam)
            if r is None:
                continue
            poly, Lp, rho_ges, pruef = r
            di = math.hypot(Lp, hr - hs)
            ausschluss = ()
            pr = profil_ueber_kante(poly, hs, hr, self.hindernisse, lam, ausschluss)
            agr_i = a_gr_alternativ(di, hm)
            ab_i = 0.0 if pr is None else max(pr["D_z_dB"] - agr_i, 0.0)
            L_i = (LW + DI + 10.0 * math.log10(rho_ges) + d_omega(Lp, hs, hr) - a_div(di)
                   - a_atm(di, alpha) - agr_i - ab_i)
            beitraege.append(L_i)
            if mit_details:
                refl.append({"ordnung": len(kette), "flaechen": pruef, "d_m": di, "rho_ges": rho_ges,
                             "10lg_rho_dB": 10.0 * math.log10(rho_ges), "A_bar_dB": ab_i, "L_dB": L_i})
        L = energiesumme(beitraege)
        if mit_details:
            details["reflexionen"] = refl
            details["L_refl_summe_dB"] = energiesumme([x["L_dB"] for x in refl]) if refl else None
            details["C_met_dB"] = cmet
            details["L_AT_DW_dB"] = L
            return L - cmet, details
        return L - cmet


# --------------------------------------------------------------------------------------
# 6  Beurteilung nach TA Lärm
# --------------------------------------------------------------------------------------
def beurteilung(L_nacht, L_tag, L_max, wp, gebiet, io_id):
    """Beurteilungspegel Nacht/Tag, Spitzenpegel, Irrelevanz mit vollständigen Nachweisen."""
    irw_t, irw_n = IRW[gebiet]
    kt, ki = wp["KT_dB"], wp["KI_dB"]
    # Nacht: lauteste volle Nachtstunde, T_r = 1 h
    nw = Nachweis(f"TA Lärm Nr. 6.1/6.4, A.1.4 (G2) – Beurteilungspegel Nacht {io_id}", Q_TAL)
    nw.eingabe("L_Aeq,N (Prognose, lauteste Stunde)", r1(L_nacht), "dB(A)", Q_ISO)
    nw.eingabe("K_T", kt, "dB", wp["quelle_KT"])
    nw.eingabe("K_I", ki, "dB", wp["quelle_KI"])
    te = wp["einwirkzeit_nacht_min"]
    nw.eingabe("T_E Nacht", te, "min", "Annahme: Dauerbetrieb in der lautesten Stunde")
    dt = 10.0 * math.log10(te / 60.0)
    nw.schritt("ΔL_T = 10 lg(T_E / 60 min)", dt, "dB")
    lr_n = L_nacht + kt + ki + dt
    nw.schritt("L_r,N = L_Aeq,N + K_T + K_I + ΔL_T  (K_R = 0 nachts)", lr_n, "dB(A)")
    lr_n_g = runde_din1333(lr_n)
    nw.schritt("L_r,N gerundet (DIN 1333)", lr_n_g, "dB(A)", "Vergleich mit IRW in vollen dB")
    nw.abschluss(lr_n_g, irw_n, "dB(A)")
    # Tag: 16 h mit Teilzeiten und K_R
    tw = Nachweis(f"TA Lärm Nr. 6.1/6.5, A.1.4 (G2) – Beurteilungspegel Tag {io_id}", Q_TAL)
    tw.eingabe("L_Aeq,T (Prognose)", r1(L_tag), "dB(A)", Q_ISO)
    summe = 0.0
    for name, tj, mit_kr in TEILZEITEN_TAG:
        kr = KR_WERT if (mit_kr and gebiet in KR_GEBIETE) else 0.0
        summe += tj * 10.0 ** (0.1 * (L_tag + kt + ki + kr))
        tw.schritt(f"T_j = {tj:g} h ({name}), K_R = {kr:g} dB", L_tag + kt + ki + kr, "dB(A)",
                   "L_Aeq + K_T + K_I + K_R in der Teilzeit")
    lr_t = 10.0 * math.log10(summe / 16.0)
    tw.schritt("L_r,T = 10 lg[(1/16 h) Σ T_j 10^(0,1(L_Aeq + K_T + K_I + K_R,j))]", lr_t, "dB(A)")
    lr_t_g = runde_din1333(lr_t)
    tw.abschluss(lr_t_g, irw_t, "dB(A)")
    # Spitzenpegel
    sp = Nachweis(f"TA Lärm Nr. 6.1 letzter Satz – kurzzeitige Geräuschspitzen nachts {io_id}", Q_TAL)
    sp.eingabe("L_WA,max − L_WA,Nacht", wp["LWA_max_dB"] - wp["LWA_nacht_dB"], "dB", wp["quelle_LWA"])
    sp.schritt("L_AFmax = L_Aeq,N − L_WA,N + L_WA,max (gleiche Ausbreitung)", L_max, "dB(A)")
    sp.abschluss(runde_din1333(L_max), irw_n + SPITZE_NACHT, "dB(A)")
    return {"L_r_N": lr_n, "L_r_N_gerundet": lr_n_g, "L_r_T": lr_t, "L_r_T_gerundet": lr_t_g,
            "L_AFmax_N": L_max, "IRW_T": irw_t, "IRW_N": irw_n,
            "reserve_N_dB": irw_n - lr_n, "reserve_T_dB": irw_t - lr_t,
            "reserve_irrelevanz_N_dB": irw_n - IRRELEVANZ - lr_n,
            "irrelevant_N": lr_n_g <= irw_n - IRRELEVANZ,
            "nachweise": [nw.d, tw.d, sp.d]}


# --------------------------------------------------------------------------------------
# 7  Vereinfachte Verfahren (Abgrenzung): BWP (TA Lärm A.2.4.3) und LAI 2023
# --------------------------------------------------------------------------------------
def lai_pegel_modell(L_E: float, dp: float) -> float:
    """LAI 2023 Kap. 4.1.3: L = L_E − A_div − A_atm − A_gr + K0 mit h_s = 1,5 m, h_r = 2 m,
    α = 2 dB/km, K0 = D_Ω (ISO 9613-2 Gl. 11), A_gr nach Gl. (10). Eigene Rekonstruktion."""
    d = math.hypot(dp, LAI_HS - LAI_HR)
    return (L_E - a_div(d) - a_atm(d, LAI_ALPHA) - a_gr_alternativ(d, (LAI_HS + LAI_HR) / 2)
            + d_omega(dp, LAI_HS, LAI_HR))


def lai_mindestabstand(L_E: float, gebiet: str) -> float:
    """Mindestabstand (horizontal, m) so, dass L = IRW_N − 6 dB (Bisektion, ≥ 1,0 m)."""
    ziel = IRW[gebiet][1] - IRRELEVANZ
    lo, hi = 0.01, 1000.0
    for _ in range(200):
        m = 0.5 * (lo + hi)
        if lai_pegel_modell(L_E, m) > ziel:
            lo = m
        else:
            hi = m
    return max(1.0, 0.5 * (lo + hi))


def lai_tabelle5(L_E: float, gebiet: str) -> float | None:
    """Tabellenwert LAI Tab. 5 (nächsthöherer Emissionspegel, Kap. 4.2)."""
    versatz = {"WR": 0, "KUR": 0, "WA": 5, "WS": 5, "MD": 10, "MI": 10, "MU": 10, "MK": 10}[gebiet]
    k = math.ceil(L_E - 1e-9) - versatz - 40
    if k < 0:
        return 1.0
    return LAI_TAB5_WR[k] if k < len(LAI_TAB5_WR) else None


def zaehle_reflektoren(S, szene, radius=3.0):
    """Anzahl reflektierender Flächen näher als 3 m (LAI Tab. 3 / BWP Aufstellsituation);
    Flächen desselben Hindernisses mit gleicher Richtung zählen einmal."""
    gef = set()
    for f in szene.flaechen:
        if abstand_punkt_strecke(S, f["a"], f["b"]) < radius and vorderseite(S, f["a"], f["b"]) > 0:
            ang = round(math.degrees(math.atan2(f["b"][1] - f["a"][1], f["b"][0] - f["a"][0])) % 180.0)
            gef.add((f["hindernis"], ang))
    return len(gef)


def sichtklasse(S, hs, R, hr, szene):
    """Operationalisierung LAI Tab. 2 / BWP „Abschirmung" [U]: 0 dB Sicht frei; 5 dB Sicht nur
    durch Mauer/fremdes Gebäude unterbrochen; 15 dB Quelle auf der abgewandten Seite des eigenen Hauses."""
    prof = profil_ueber_kante([S, R], hs, hr, szene.hindernisse, szene.lam)
    if prof is None or prof["sichtlinie_frei"]:
        return 0.0, "direkte Sicht"
    if "EIGEN" in prof["hindernisse"]:
        return 15.0, "abgewandte Seite (eigenes Haus)"
    return 5.0, "indirekte Sicht (Hindernis)"


def bwp_lr(LWA: float, KT: float, K0: float, s: float, D_abschirm: float = 0.0, KR: float = 0.0) -> float:
    """BWP-Leitfaden Schall Gl. (4.1) = TA Lärm A.2.4.3 (G4) mit Zuschlägen:
    L_r = L_W,Aeq + K_T + K0 − 20 lg(s_m) − 11 dB (− Abschirmmaß) (+ K_R nur tags, pauschal)."""
    return LWA + KT + K0 - 20.0 * math.log10(s) - 11.0 - D_abschirm + KR


def vereinfachte_verfahren(S, hs, R, hr, szene, wp, gebiet):
    """BWP-Rechner (TA Lärm G4) und LAI-Tabelle zum Vergleich mit der detaillierten Prognose."""
    n_ref = zaehle_reflektoren(S, szene)
    dp = math.hypot(R[0] - S[0], R[1] - S[1])
    s = math.hypot(dp, hr - hs)
    sicht_db, sicht_txt = sichtklasse(S, hs, R, hr, szene)
    k0 = {0: 3.0, 1: 6.0}.get(n_ref, 9.0)                 # BWP: 3/6/9 dB
    lr_bwp_n = bwp_lr(wp["LWA_nacht_dB"], wp["KT_dB"], k0, s, sicht_db)
    refl_lai = {0: 0.0, 1: 3.0}.get(n_ref, 6.0)            # LAI Tab. 3: 0/3/6 dB
    L_E = wp["LWA_nacht_dB"] - sicht_db + refl_lai + wp["KT_dB"]   # LAI Kap. 4.2
    lr_lai_n = lai_pegel_modell(L_E, dp)
    tab = lai_tabelle5(L_E, gebiet)
    return {"reflektoren_unter_3m": n_ref, "sicht": sicht_txt, "D_sicht_dB": sicht_db,
            "BWP_K0_dB": k0, "BWP_L_r_N": lr_bwp_n, "LAI_Reflexionswert_dB": refl_lai,
            "LAI_Emissionspegel_dB": L_E, "LAI_L_N_Modell": lr_lai_n,
            "LAI_Tab5_Mindestabstand_m": tab, "Abstand_horizontal_m": dp,
            "LAI_Tab5_eingehalten": (tab is not None and dp >= tab)}


# --------------------------------------------------------------------------------------
# 8  Aufstellregeln (R290-Schutzbereich, Leitungslänge, Ausblas, BayBO, F-Gase)
# --------------------------------------------------------------------------------------
def f_gase_pruefung(wp: dict, stichtag: str) -> dict:
    """VO (EU) 2024/573 Anhang IV (Inverkehrbringensverbote) für Wärmepumpen ≤ 12 kW."""
    nw = Nachweis("VO (EU) 2024/573 Art. 11 Abs. 1 i. V. m. Anhang IV", "EUR-Lex, ABl. L 2024/573 (Anhang IV Nr. 8, 9)")
    tag = date.fromisoformat(stichtag)
    gwp, p, bauart = wp["gwp"], wp.get("nennleistung_kW", 7.0), wp["bauart"]
    nw.eingabe("Bauart", bauart, "-", "Eingabe")
    nw.eingabe("GWP Kältemittel", gwp, "-", wp.get("quelle_gwp", ""))
    nw.eingabe("Nennleistung", p, "kW", "Eingabe")
    regeln = []
    if bauart == "Monoblock" and p <= 12:
        regeln = [("Anhang IV Nr. 8 b: in sich geschlossene WP ≤ 12 kW, GWP ≥ 150", date(2027, 1, 1), 150),
                  ("Anhang IV Nr. 8 c: in sich geschlossene WP ≤ 12 kW, jedes F-Gas", date(2032, 1, 1), 0)]
    elif bauart == "Split" and p <= 12:
        regeln = [("Anhang IV Nr. 9 b: Luft-Wasser-Split ≤ 12 kW, GWP ≥ 150", date(2027, 1, 1), 150),
                  ("Anhang IV Nr. 9 d: Split ≤ 12 kW, jedes F-Gas", date(2035, 1, 1), 0)]
    ist_fgas = wp["kaeltemittel"].upper() not in ("R290", "R744", "R600A", "R1270")
    status, hinweise = "zulässig", []
    for text, ab, grenze in regeln:
        betroffen = ist_fgas and gwp >= grenze
        nw.schritt(f"{text}: ab {ab.isoformat()}", "betroffen" if betroffen else "nicht betroffen", "-")
        if betroffen:
            if tag >= ab:
                status = "verboten (Inverkehrbringen)"
            elif status == "zulässig":
                status = f"zulässig bis {(ab - timedelta(days=1)).isoformat()} (danach Verbot des Inverkehrbringens, Ausnahme nur bei Sicherheitsanforderungen am Standort)"
            hinweise.append(text)
    nw.d["hinweis"] = "Installation/Befüllung nur durch zertifiziertes Personal (Art. 10 VO (EU) 2024/573); Verbote betreffen das Inverkehrbringen, nicht den Weiterbetrieb."
    nw.abschluss(status, None, "-", status=status)
    return nw.d


def leitungslaenge(xy, hs, haus_ecken, leitung):
    """Leitungslänge = Grundriss bis zur nächsten Wanddurchführung + Innenweg (Manhattan)
    + Höhenunterschied + Zuschlag (Beispielansatz, keine Norm)."""
    haus = Polygon(haus_ecken)
    rand = haus.exterior
    e = rand.interpolate(rand.project(Point(xy)))
    aussen = Point(xy).distance(e)
    ix, iy = leitung["inneneinheit_xy"]
    innen = abs(e.x - ix) + abs(e.y - iy)
    dh = abs(hs - leitung["inneneinheit_h_m"])
    return aussen + innen + dh + leitung["zuschlag_m"], dh


def pruefe_standort(xy, daten, szene, wp, ios):
    """Alle Aufstellregeln an einem Kandidatenort. Rückgabe: (zulässig, Gründe, Zusatzdaten)."""
    gruende = []
    r = wp["radius_huellkreis_m"]
    grund = Polygon(daten["grundstueck"]["polygon"])
    p = Point(xy)
    geraet = p.buffer(r, 32)
    if not grund.contains(geraet):
        gruende.append("Gerät außerhalb des Grundstücks")
    for hi in szene.hindernisse:
        if hi.polygon.distance(p) < r + wp["abstand_ansaug_wand_m"] - 1e-9:
            gruende.append(f"Abstand zu {hi.id} < Hüllkreis + {wp['abstand_ansaug_wand_m']} m")
    if wp["geraetehoehe_m"] > 2.0:
        gruende.append("Höhe > 2 m: Abstandsflächenpflicht (BayBO Art. 6 Abs. 1 S. 3 Nr. 4)")
    sb = wp.get("schutzbereich")
    zone = None
    if sb:
        zone = p.buffer(r + sb["boden_m"], 32)
        if not grund.contains(zone):
            gruende.append("R290-Schutzbereich ragt über die Grundstücksgrenze")
        for o in daten["oeffnungen_eigen"]:
            if zone.intersects(LineString(o["linie"])) and o["unterkante_m"] < wp["geraetehoehe_m"] + sb["oberkante_m"]:
                gruende.append(f"R290-Schutzbereich enthält Öffnung {o['id']} ({o['art']})")
        for s in daten["senken_eigen"]:
            if zone.intersects(Polygon(s["polygon"])):
                gruende.append(f"R290-Schutzbereich enthält Senke {s['id']} ({s['art']})")
    haus = next(g for g in daten["gebaeude"] if g["id"] == "EIGEN")["polygon"]
    L, dh = leitungslaenge(xy, wp["hoehe_quelle_m"], haus, wp["leitung"])
    if L > wp["leitung"]["max_m"]:
        gruende.append(f"Leitungslänge {r1(L)} m > {wp['leitung']['max_m']} m")
    if dh > wp["leitung"]["hoehenunterschied_max_m"]:
        gruende.append("Höhenunterschied Leitung zu groß")
    # Ausblasrichtung: 8 Richtungen, frei ≥ ausblas_frei_m, innerhalb des Grundstücks,
    # gewählt wird die Richtung mit dem größten Mindestwinkel zu allen Immissionsorten.
    beste = None
    for k in range(8):
        az = math.radians(45 * k)
        ende = (xy[0] + (r + wp["ausblas_frei_m"]) * math.cos(az), xy[1] + (r + wp["ausblas_frei_m"]) * math.sin(az))
        if not grund.contains(Point(ende)):
            continue
        if any(clip_strecke(tuple(xy), ende, hi.ecken) is not None for hi in szene.hindernisse):
            continue
        wmin = min(abs((math.degrees(math.atan2(io[1] - xy[1], io[0] - xy[0])) - 45 * k + 180) % 360 - 180)
                   for io in ios)
        if beste is None or wmin > beste[1] + 1e-9:
            beste = (45 * k, wmin)
    if beste is None:
        gruende.append("keine Ausblasrichtung mit ≥ 1 m freiem Raum")
    return (not gruende), gruende, {"leitung_m": L, "ausblas_azimut_grad": None if beste is None else beste[0],
                                    "ausblas_winkel_zum_naechsten_IO_grad": None if beste is None else beste[1],
                                    "schutzbereich": zone}


# --------------------------------------------------------------------------------------
# 9  Immissionsorte, Standortbewertung, Optimierung
# --------------------------------------------------------------------------------------
def immissionsorte(daten):
    """IO = 0,5 m vor Fenstermitte (TA Lärm A.1.3 a); Linien-IO an Baugrenze (A.1.3 b)."""
    ios = []
    for io in daten["immissionsorte"]:
        fx, fy = io["fenster_mitte"]
        nx, ny = io["normale"]
        ios.append({"id": io["id"], "xy": (fx + 0.5 * nx, fy + 0.5 * ny), "h": io["hoehe_m"],
                    "gebaeude": io["gebaeude"], "gebiet": io["gebiet"], "raum": io["raum"], "teil": None})
    for li in daten.get("immissionslinien", []):
        (x0, y0), (x1, y1) = li["von"], li["bis"]
        L = math.hypot(x1 - x0, y1 - y0)
        n = int(round(L / li["schritt_m"]))
        for i in range(n + 1):
            t = i / n
            for h in li["hoehen_m"]:
                ios.append({"id": li["id"], "xy": (x0 + t * (x1 - x0), y0 + t * (y1 - y0)), "h": h,
                            "gebaeude": None, "gebiet": li["gebiet"], "raum": li["beschreibung"],
                            "teil": f"{r1(x0 + t * (x1 - x0))}/{r1(y0 + t * (y1 - y0))}/h{h}"})
    return ios


def bewerte_standort(xy, szene, wp, ios, mit_details=False):
    """Nacht-Beurteilungspegel an allen IO (Linien-IO: Maximum über die Stützpunkte)."""
    hs = wp["hoehe_quelle_m"]
    bilder = szene.spiegelquellen(xy)
    je_io = {}
    for io in ios:
        L = szene.pegel(xy, hs, io["xy"], io["h"], wp["LWA_nacht_dB"], io["gebaeude"], bilder=bilder, DI=wp["DI_dB"])
        lr = L + wp["KT_dB"] + wp["KI_dB"] + 10 * math.log10(wp["einwirkzeit_nacht_min"] / 60.0)
        res = IRW[io["gebiet"]][1] - lr
        if io["id"] not in je_io or res < je_io[io["id"]]["reserve"]:
            je_io[io["id"]] = {"L_r_N": lr, "reserve": res, "io": io}
    return je_io


def optimiere(daten, szene, wp, ios):
    """Rastersuche: zulässige Orte, Ziel = max. kleinste Reserve zum Nacht-Richtwert.
    Gleichstand: kürzere Leitung, dann kleineres (x, y) – vollständig deterministisch."""
    step = daten["berechnung"]["raster_standorte_m"]
    xs = np.arange(step / 2, 18.0, step)
    ys = np.arange(step / 2, 32.0, step)
    io_punkte = [io["xy"] for io in ios]
    kandidaten, unzulaessig = [], {}
    for y in ys:
        for x in xs:
            xy = (float(round(x, 6)), float(round(y, 6)))
            ok, gruende, extra = pruefe_standort(xy, daten, szene, wp, io_punkte)
            if not ok:
                for g in gruende:
                    key = re.sub(r"\d+(\.\d+)?", "#", g)
                    unzulaessig[key] = unzulaessig.get(key, 0) + 1
                kandidaten.append({"xy": xy, "zulaessig": False, "gruende": gruende})
                continue
            je_io = bewerte_standort(xy, szene, wp, ios)
            rmin = min(v["reserve"] for v in je_io.values())
            kandidaten.append({"xy": xy, "zulaessig": True, "reserve_min": rmin, "leitung_m": extra["leitung_m"],
                               "ausblas_azimut_grad": extra["ausblas_azimut_grad"],
                               "L_r_N": {k: v["L_r_N"] for k, v in je_io.items()}})
    zul = [k for k in kandidaten if k["zulaessig"]]
    zul.sort(key=lambda k: (-round(k["reserve_min"], 9), round(k["leitung_m"], 9), k["xy"][0], k["xy"][1]))
    return kandidaten, zul, unzulaessig


# --------------------------------------------------------------------------------------
# 10  Karten (Marching Squares, SVG)
# --------------------------------------------------------------------------------------
def rasterkarte(szene, wp, S, daten):
    """L_r,Nacht auf einem Raster in Kartenhöhe (Zellen in Gebäuden/Mauern = NaN)."""
    b = daten["berechnung"]
    x0, y0, x1, y1 = b["karte_bbox"]
    st = b["raster_karte_m"]
    xs = np.arange(x0, x1 + 1e-9, st)
    ys = np.arange(y0, y1 + 1e-9, st)
    hr = b["kartenhoehe_m"]
    bilder = szene.spiegelquellen(S)
    Z = np.full((len(ys), len(xs)), np.nan)
    polys = [hi.polygon for hi in szene.hindernisse]
    zus = wp["KT_dB"] + wp["KI_dB"] + 10 * math.log10(wp["einwirkzeit_nacht_min"] / 60.0)
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            if math.hypot(x - S[0], y - S[1]) < 0.5:
                continue
            pt = Point(x, y)
            if any(p.covers(pt) for p in polys):
                continue
            Z[j, i] = szene.pegel(S, wp["hoehe_quelle_m"], (float(x), float(y)), hr, wp["LWA_nacht_dB"],
                                  None, bilder=bilder, DI=wp["DI_dB"]) + zus
    return xs, ys, Z


def marching_squares(xs, ys, Z, stufe):
    """Isolinien-Segmente [(x1, y1, x2, y2)] für einen Pegel; Zellen mit NaN werden übersprungen."""
    seg = []
    for j in range(len(ys) - 1):
        for i in range(len(xs) - 1):
            v = (Z[j, i], Z[j, i + 1], Z[j + 1, i + 1], Z[j + 1, i])
            if any(np.isnan(v)):
                continue
            p = ((xs[i], ys[j]), (xs[i + 1], ys[j]), (xs[i + 1], ys[j + 1]), (xs[i], ys[j + 1]))
            idx = sum((1 << k) for k in range(4) if v[k] >= stufe)
            if idx in (0, 15):
                continue

            def kante(k):
                a, b2 = k, (k + 1) % 4
                t = (stufe - v[a]) / (v[b2] - v[a])
                return (p[a][0] + t * (p[b2][0] - p[a][0]), p[a][1] + t * (p[b2][1] - p[a][1]))
            ks = [k for k in range(4) if (v[k] >= stufe) != (v[(k + 1) % 4] >= stufe)]
            if len(ks) == 2:
                seg.append(kante(ks[0]) + kante(ks[1]))
            elif len(ks) == 4:  # Sattel: Mittelwert entscheidet
                mitte = sum(v) / 4.0
                paare = ((0, 1), (2, 3)) if (mitte >= stufe) == (v[0] >= stufe) else ((0, 3), (1, 2))
                paare = ((ks[paare[0][0]], ks[paare[0][1]]), (ks[paare[1][0]], ks[paare[1][1]]))
                for a, b2 in paare:
                    seg.append(kante(a) + kante(b2))
    return seg


SVG_STIL = """
  :root, svg { --flaeche:#fcfcfb; --tinte:#0b0b0b; --tinte2:#52514e; --gitter:#d9d8d4; --geb:#8a8984;
    --k0:#cde2fb; --k1:#b7d3f6; --k2:#86b6ef; --k3:#5598e7; --k4:#2a78d6; --k5:#1c5cab; --k6:#0d366b;
    --neg3:#b8302f; --neg2:#e34948; --neg1:#f2a09f; --neu:#f0efec; --pos1:#9ec5f4; --pos2:#3987e5; --pos3:#184f95;
    --unz:#e4e3df; }
  @media (prefers-color-scheme: dark) { :root:not([data-theme="light"]), svg { --flaeche:#1a1a19; --tinte:#ffffff;
    --tinte2:#c3c2b7; --gitter:#3a3a37; --geb:#6d6c66; --unz:#2c2c2a; --neu:#383835; } }
  text { font-family: system-ui, -apple-system, "Segoe UI", sans-serif; fill: var(--tinte); }
  .klein { font-size: 11px; fill: var(--tinte2); }
"""
KLASSEN_KARTE = ((-1e9, 20), (20, 25), (25, 30), (30, 35), (35, 40), (40, 45), (45, 1e9))


class SvgRahmen:
    def __init__(self, bbox, skala, rand_links=40, rand_oben=70, breite_legende=300):
        self.x0, self.y0, self.x1, self.y1 = bbox
        self.s = skala
        self.rl, self.ro = rand_links, rand_oben
        self.w = rand_links + (self.x1 - self.x0) * skala + breite_legende
        self.h = rand_oben + (self.y1 - self.y0) * skala + 40

    def X(self, x):
        return self.rl + (x - self.x0) * self.s

    def Y(self, y):
        return self.ro + (self.y1 - y) * self.s


def _svg_szene(teile, R, daten, szene, S=None, zone=None, ios=None):
    grund = daten["grundstueck"]["polygon"]
    teile.append('<polygon points="' + " ".join(f"{R.X(x):.1f},{R.Y(y):.1f}" for x, y in grund)
                 + '" fill="none" stroke="var(--tinte)" stroke-width="1.5" stroke-dasharray="6 3"/>')
    for hi in szene.hindernisse:
        pts = " ".join(f"{R.X(x):.1f},{R.Y(y):.1f}" for x, y in hi.ecken)
        teile.append(f'<polygon points="{pts}" fill="var(--geb)" stroke="var(--tinte)" stroke-width="0.8">'
                     f'<title>{hi.name}, Höhe {hi.hoehe} m, ρ = {hi.rho}</title></polygon>')
        c = hi.polygon.centroid
        if hi.art == "gebaeude":
            teile.append(f'<text x="{R.X(c.x):.1f}" y="{R.Y(c.y):.1f}" text-anchor="middle" font-size="12" '
                         f'fill="var(--flaeche)">{hi.id}</text>')
    for o in daten["oeffnungen_eigen"]:
        (ax, ay), (bx, by) = o["linie"]
        teile.append(f'<line x1="{R.X(ax):.1f}" y1="{R.Y(ay):.1f}" x2="{R.X(bx):.1f}" y2="{R.Y(by):.1f}" '
                     f'stroke="var(--flaeche)" stroke-width="3"><title>{o["id"]}: {o["art"]}, UK {o["unterkante_m"]} m</title></line>')
    for sk in daten.get("senken_eigen", []):
        pts = " ".join(f"{R.X(x):.1f},{R.Y(y):.1f}" for x, y in sk["polygon"])
        teile.append(f'<polygon points="{pts}" fill="var(--tinte)" stroke="var(--tinte)" stroke-width="2">'
                     f'<title>{sk["id"]}: {sk["art"]}</title></polygon>')
    if zone is not None:
        pts = " ".join(f"{R.X(x):.1f},{R.Y(y):.1f}" for x, y in zone.exterior.coords)
        teile.append(f'<polygon points="{pts}" fill="none" stroke="var(--neg3)" stroke-width="1.6" stroke-dasharray="3 2">'
                     f'<title>R290-Schutzbereich</title></polygon>')
    if ios:
        gesehen = set()
        for io in ios:
            x, y = io["xy"]
            if io["teil"] is None:
                teile.append(f'<circle cx="{R.X(x):.1f}" cy="{R.Y(y):.1f}" r="5" fill="var(--flaeche)" stroke="var(--tinte)" stroke-width="2">'
                             f'<title>{io["id"]}: {io["raum"]}, h = {io["h"]} m</title></circle>')
                teile.append(f'<text x="{R.X(x) + 7:.1f}" y="{R.Y(y) - 7:.1f}" font-size="12" font-weight="600">{io["id"]}</text>')
            elif (x, y) not in gesehen:
                gesehen.add((x, y))
                teile.append(f'<rect x="{R.X(x) - 3:.1f}" y="{R.Y(y) - 3:.1f}" width="6" height="6" fill="var(--flaeche)" '
                             f'stroke="var(--tinte)" stroke-width="1.5"><title>{io["id"]} Baugrenze {io["teil"]}</title></rect>')
        li = daten.get("immissionslinien", [])
        if li:
            x, y = li[0]["bis"]
            teile.append(f'<text x="{R.X(x) + 7:.1f}" y="{R.Y(y):.1f}" font-size="12" font-weight="600">{li[0]["id"]} (Baugrenze)</text>')
    if S is not None:
        teile.append(f'<rect x="{R.X(S[0]) - 6:.1f}" y="{R.Y(S[1]) - 6:.1f}" width="12" height="12" fill="var(--neg2)" '
                     f'stroke="var(--tinte)" stroke-width="1.5"><title>WP-Außengerät ({r1(S[0])}/{r1(S[1])})</title></rect>')


def _legende_symbole(lx, y, mit_isolinien):
    """Legende mit den tatsächlichen Symbolen (Identität nie nur über Farbe)."""
    t, zeilen = [], []
    if mit_isolinien:
        zeilen += [("iso40", "Isolinie 40 dB(A) = IRW Nacht WA"), ("iso35", "Isolinien 35 und 45 dB(A)")]
    zeilen += [("wp", "WP-Außengerät (Punktquelle)"), ("sb", "R290-Schutzbereich (1 m + Hüllkreis)"),
               ("io", "Immissionsort 0,5 m vor Fenster"), ("iol", "IO5: Stützpunkte Baugrenze"),
               ("geb", "Gebäude / Gartenmauer M1"), ("oeff", "Öffnung eigenes Haus (weiß)"),
               ("senke", "Senke/Einlauf (Schutzbereich)"), ("grenze", "Grundstücksgrenze")]
    for n, (art, txt) in enumerate(zeilen):
        yy = y + 18 * n
        if art == "iso40":
            t.append(f'<line x1="{lx}" y1="{yy - 4}" x2="{lx + 18}" y2="{yy - 4}" stroke="var(--tinte)" stroke-width="2.4"/>')
        elif art == "iso35":
            t.append(f'<line x1="{lx}" y1="{yy - 4}" x2="{lx + 18}" y2="{yy - 4}" stroke="var(--tinte)" stroke-width="1.4" stroke-dasharray="5 3"/>')
        elif art == "wp":
            t.append(f'<rect x="{lx + 3}" y="{yy - 10}" width="12" height="12" fill="var(--neg2)" stroke="var(--tinte)" stroke-width="1.5"/>')
        elif art == "sb":
            t.append(f'<circle cx="{lx + 9}" cy="{yy - 4}" r="7" fill="none" stroke="var(--neg3)" stroke-width="1.6" stroke-dasharray="3 2"/>')
        elif art == "io":
            t.append(f'<circle cx="{lx + 9}" cy="{yy - 4}" r="5" fill="var(--flaeche)" stroke="var(--tinte)" stroke-width="2"/>')
        elif art == "iol":
            t.append(f'<rect x="{lx + 6}" y="{yy - 7}" width="6" height="6" fill="var(--flaeche)" stroke="var(--tinte)" stroke-width="1.5"/>')
        elif art == "geb":
            t.append(f'<rect x="{lx}" y="{yy - 11}" width="18" height="14" fill="var(--geb)" stroke="var(--tinte)" stroke-width="0.8"/>')
        elif art == "oeff":
            t.append(f'<rect x="{lx}" y="{yy - 11}" width="18" height="14" fill="var(--geb)"/><line x1="{lx + 2}" y1="{yy - 4}" x2="{lx + 16}" y2="{yy - 4}" stroke="var(--flaeche)" stroke-width="3"/>')
        elif art == "senke":
            t.append(f'<rect x="{lx + 5}" y="{yy - 8}" width="8" height="8" fill="var(--tinte)"/>')
        elif art == "grenze":
            t.append(f'<line x1="{lx}" y1="{yy - 4}" x2="{lx + 18}" y2="{yy - 4}" stroke="var(--tinte)" stroke-width="1.5" stroke-dasharray="6 3"/>')
        t.append(f'<text x="{lx + 26}" y="{yy}" font-size="12">{txt}</text>')
    return "\n".join(t)


def svg_laermkarte(xs, ys, Z, S, daten, szene, zone, ios, titel):
    wp_lwa, wp_kt = daten["waermepumpe"]["LWA_nacht_dB"], daten["waermepumpe"]["KT_dB"]
    R = SvgRahmen(daten["berechnung"]["karte_bbox"], 13.0)
    st = daten["berechnung"]["raster_karte_m"]
    t = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{R.w:.0f}" height="{R.h:.0f}" viewBox="0 0 {R.w:.0f} {R.h:.0f}" role="img" aria-label="{titel}">',
         f"<style>{SVG_STIL}</style>", f'<rect width="100%" height="100%" fill="var(--flaeche)"/>',
         f'<text x="{R.rl}" y="22" font-size="15" font-weight="600">{titel}</text>',
         f'<text x="{R.rl}" y="40" class="klein">DIN ISO 9613-2 (A-bewertet, Dämpfung bei 500 Hz), Spiegelquellen bis 2. Ordnung, Rasterhöhe {daten["berechnung"]["kartenhoehe_m"]} m</text>',
         f'<text x="{R.rl}" y="56" class="klein">L_r,N = L_AT + K_T; L_WA,Nacht = {wp_lwa} dB, K_T = {wp_kt} dB – BEISPIELDATEN, kein Gutachten</text>']
    for j, y in enumerate(ys):
        for i, x in enumerate(xs):
            v = Z[j, i]
            if np.isnan(v):
                continue
            k = next(n for n, (a, b) in enumerate(KLASSEN_KARTE) if a <= v < b)
            t.append(f'<rect x="{R.X(x - st / 2):.1f}" y="{R.Y(y + st / 2):.1f}" width="{st * R.s + 0.4:.1f}" '
                     f'height="{st * R.s + 0.4:.1f}" fill="var(--k{k})"/>')
    for stufe, breite in ((35, 1.4), (40, 2.4), (45, 1.4)):
        seg = marching_squares(xs, ys, Z, stufe)
        d = " ".join(f"M{R.X(a):.1f} {R.Y(b):.1f}L{R.X(c):.1f} {R.Y(e):.1f}" for a, b, c, e in seg)
        strich = ' stroke-dasharray="5 3"' if stufe != 40 else ""
        t.append(f'<path d="{d}" fill="none" stroke="var(--tinte)" stroke-width="{breite}"{strich}>'
                 f'<title>Isolinie {stufe} dB(A)</title></path>')
        if seg:
            a, b, c, e = max(seg, key=lambda s_: (s_[0] + s_[2], s_[1]))
            for halo in (True, False):
                zus = ' stroke="var(--flaeche)" stroke-width="3"' if halo else ""
                t.append(f'<text x="{R.X(a) + 3:.1f}" y="{R.Y(b) - 3:.1f}" font-size="11" font-weight="600"{zus}>{stufe}</text>')
    _svg_szene(t, R, daten, szene, S, zone, ios)
    lx, ly = R.X(R.x1) + 20, R.ro + 10
    t.append(f'<text x="{lx}" y="{ly}" font-size="12" font-weight="600">L_r,Nacht in dB(A)</text>')
    namen = ("&lt; 20", "20–25", "25–30", "30–35", "35–40", "40–45", "≥ 45")
    for n, nm in enumerate(namen):
        t.append(f'<rect x="{lx}" y="{ly + 10 + 20 * n}" width="18" height="14" fill="var(--k{n})" rx="2"/>'
                 f'<text x="{lx + 26}" y="{ly + 21 + 20 * n}" font-size="12">{nm}</text>')
    y2 = ly + 170
    t.append(_legende_symbole(lx, y2, mit_isolinien=True))
    t.append(f'<text x="{lx}" y="{y2 + 190}" class="klein">Maßstab: {R.s:g} px = 1 m; Nord oben</text>')
    t.append("</svg>")
    return "\n".join(t)


def svg_standortkarte(kandidaten, opt, daten, szene, ios, titel):
    bbox = (-15.0, -3.0, 33.0, 48.0)
    R = SvgRahmen(bbox, 13.0)
    st = daten["berechnung"]["raster_standorte_m"]
    t = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{R.w:.0f}" height="{R.h:.0f}" viewBox="0 0 {R.w:.0f} {R.h:.0f}" role="img" aria-label="{titel}">',
         f"<style>{SVG_STIL}</style>", '<rect width="100%" height="100%" fill="var(--flaeche)"/>',
         f'<text x="{R.rl}" y="22" font-size="15" font-weight="600">{titel}</text>',
         f'<text x="{R.rl}" y="40" class="klein">Farbe je 0,5-m-Rasterpunkt: kleinste Reserve (IRW − 6 dB) − L_r,N über alle IO</text>',
         f'<text x="{R.rl}" y="56" class="klein">schraffiert = unzulässig (R290-Schutzbereich, Leitungslänge, Abstände, Ausblas) – Tooltip nennt den Grund</text>',
         '<defs><pattern id="schraff" width="5" height="5" patternUnits="userSpaceOnUse" patternTransform="rotate(45)">'
         '<line x1="0" y1="0" x2="0" y2="5" stroke="var(--tinte2)" stroke-width="0.6"/></pattern></defs>']
    klassen = ((-1e9, -6, "neg3"), (-6, -3, "neg2"), (-3, -1, "neg1"), (-1, 1, "neu"), (1, 3, "pos1"), (3, 6, "pos2"), (6, 1e9, "pos3"))
    for k in kandidaten:
        x, y = k["xy"]
        if k["zulaessig"]:
            ri = k["reserve_min"] - IRRELEVANZ
            farbe = next(f for a, b, f in klassen if a <= ri < b)
            t.append(f'<rect x="{R.X(x - st / 2):.1f}" y="{R.Y(y + st / 2):.1f}" width="{st * R.s:.1f}" height="{st * R.s:.1f}" '
                     f'fill="var(--{farbe})"><title>({x}/{y}): Reserve zu IRW−6 = {r1(ri)} dB, Leitung {r1(k["leitung_m"])} m</title></rect>')
        else:
            t.append(f'<rect x="{R.X(x - st / 2):.1f}" y="{R.Y(y + st / 2):.1f}" width="{st * R.s:.1f}" height="{st * R.s:.1f}" '
                     f'fill="url(#schraff)"><title>({x}/{y}): {html.escape("; ".join(k["gruende"]))}</title></rect>')
    _svg_szene(t, R, daten, szene, opt["xy"], opt.get("zone"), ios)
    lx, ly = R.X(R.x1) + 20, R.ro + 10
    t.append(f'<text x="{lx}" y="{ly}" font-size="12" font-weight="600">Reserve zu IRW − 6 dB</text>')
    namen = ("&lt; −6 dB", "−6 … −3", "−3 … −1", "−1 … +1", "+1 … +3", "+3 … +6", "≥ +6 dB")
    for n, (nm, (_, _, f)) in enumerate(zip(namen, klassen)):
        t.append(f'<rect x="{lx}" y="{ly + 10 + 20 * n}" width="18" height="14" fill="var(--{f})" rx="2"/>'
                 f'<text x="{lx + 26}" y="{ly + 21 + 20 * n}" font-size="12">{nm}</text>')
    t.append(f'<rect x="{lx}" y="{ly + 150}" width="18" height="14" fill="url(#schraff)" stroke="var(--tinte2)" stroke-width="0.5"/>'
             f'<text x="{lx + 26}" y="{ly + 161}" font-size="12">unzulässig</text>')
    t.append(_legende_symbole(lx, ly + 185, mit_isolinien=False))
    t.append(f'<text x="{lx}" y="{ly + 345}" class="klein">Optimum: x = {opt["xy"][0]:.2f} m, y = {opt["xy"][1]:.2f} m</text>')
    t.append("</svg>")
    return "\n".join(t)


# --------------------------------------------------------------------------------------
# 11  Gesamtrechnung
# --------------------------------------------------------------------------------------
def lade_eingabe(pfad: Path = STANDARD_EINGABE) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def standort_bericht(xy, daten, szene, wp, ios, name):
    """Vollständige Tabelle je IO (alle Terme) für einen Standort."""
    hs = wp["hoehe_quelle_m"]
    zeilen = []
    punkte = [io for io in ios if io["teil"] is None]
    # Linien-IO: maßgeblicher (lautester) Stützpunkt
    lin = {}
    for io in ios:
        if io["teil"] is None:
            continue
        L = szene.pegel(xy, hs, io["xy"], io["h"], wp["LWA_nacht_dB"], None, DI=wp["DI_dB"])
        if io["id"] not in lin or L > lin[io["id"]][0]:
            lin[io["id"]] = (L, io)
    punkte += [v[1] for v in lin.values()]
    for io in punkte:
        L_n, det = szene.pegel(xy, hs, io["xy"], io["h"], wp["LWA_nacht_dB"], io["gebaeude"], mit_details=True, DI=wp["DI_dB"])
        L_t = L_n - wp["LWA_nacht_dB"] + wp["LWA_tag_dB"]
        L_max = L_n - wp["LWA_nacht_dB"] + wp["LWA_max_dB"]
        be = beurteilung(L_n, L_t, L_max, wp, io["gebiet"], io["id"])
        vv = vereinfachte_verfahren(xy, hs, io["xy"], io["h"], szene, wp, io["gebiet"])
        dr = det["direkt"]
        oben = dr["oben"]
        # Ausbreitungsnachweis (ISO 9613-2) des Direktpfads
        aw = Nachweis(f"DIN ISO 9613-2 Direktpfad {name} → {io['id']}", Q_ISO)
        aw.eingabe("L_WA,N", wp["LWA_nacht_dB"], "dB", wp["quelle_LWA"])
        aw.eingabe("h_s", hs, "m", "Gerätemitte (Beispiel)")
        aw.eingabe("h_r", io["h"], "m", "Fenstermitte (Beispiel)")
        aw.schritt("d = √(d_p² + (h_s − h_r)²)", dr["d_m"], "m")
        aw.schritt("A_div = 20 lg(d/1 m) + 11", dr["A_div_dB"], "dB", "Gl. (7)")
        aw.schritt("A_atm = α d/1000, α = %.1f dB/km" % szene.alpha, dr["A_atm_dB"], "dB", "Gl. (8), Tab. 2")
        aw.schritt("A_gr = 4,8 − (2h_m/d)(17 + 300/d) ≥ 0", dr["A_gr_dB"], "dB", "Gl. (10)")
        aw.schritt("D_Ω = 10 lg{1 + [d_p² + (h_s−h_r)²]/[d_p² + (h_s+h_r)²]}", dr["D_Omega_dB"], "dB", "Gl. (11)")
        if oben:
            aw.schritt("z (Gummiband, Oberkante)", oben["z_m"], "m", f"Hindernisse {oben['hindernisse']}, e = {r1(oben['e_m'])} m")
            aw.schritt("D_z = 10 lg[3 + (20/λ) C3 z K_met]", oben["D_z_dB"], "dB",
                       f"λ = {r1(szene.lam * 100) / 100} m, C3 = {oben['C3']:.3f}, K_met = {oben['K_met']:.3f}")
            for p in dr["seitlich"]:
                aw.schritt(f"D_z seitlich {p['seite']} (z = {r1(p['z_m'])} m)", p["D_z_dB"], "dB", "Gl. (13), K_met = 1")
        aw.schritt("A_bar (Pfade energetisch)", dr["A_bar_dB"], "dB", "Gl. (12)/(13), ISO 7.4")
        aw.schritt("L_dir = L_W + D_I + D_Ω − A_div − A_atm − A_gr − A_bar", dr["L_dB"], "dB(A)", "Gl. (3), (4)")
        aw.schritt("L_refl = 10 lg Σ Spiegelquellen", det["L_refl_summe_dB"] if det["L_refl_summe_dB"] is not None else "keine", "dB(A)",
                   f"{len(det['reflexionen'])} gültige Spiegelpfade, Gl. (20)")
        aw.schritt("L_AT(DW) = 10 lg(10^0,1·L_dir + 10^0,1·L_refl) − C_met", L_n, "dB(A)", "Gl. (5), (6)")
        aw.abschluss(r1(L_n), None, "dB(A)", status="berechnet")
        zeilen.append({
            "io": io["id"], "raum": io["raum"], "xy": [r1(io["xy"][0]), r1(io["xy"][1])], "h_m": io["h"],
            "d_m": dr["d_m"], "A_div": dr["A_div_dB"], "A_atm": dr["A_atm_dB"], "A_gr": dr["A_gr_dB"],
            "D_Omega": dr["D_Omega_dB"], "z_oben_m": None if not oben else oben["z_m"],
            "D_z_oben": None if not oben else oben["D_z_dB"], "A_bar": dr["A_bar_dB"], "L_dir": dr["L_dB"],
            "n_refl": len(det["reflexionen"]), "L_refl": det["L_refl_summe_dB"], "C_met": det["C_met_dB"],
            "L_AT_N": L_n, "K_T": wp["KT_dB"], "K_I": wp["KI_dB"], **{k: v for k, v in be.items() if k != "nachweise"},
            "vereinfacht": vv, "nachweise": [aw.d] + be["nachweise"],
            "reflexionen": det["reflexionen"], "seitlich": dr["seitlich"], "oben": oben})
    return zeilen


def oktavvergleich(xy, daten, szene, wp, io):
    """Oktavbandrechnung (Beispielspektrum) gegen die A/500-Hz-Rechnung am selben Punkt.
    Boden weiterhin nach 7.3.2 (A-bewertetes Verfahren) – Hybridansatz [U]."""
    spek = {int(k): v for k, v in daten["oktavspektrum_A_relativ_dB"].items() if not k.startswith("_")}
    norm = wp["LWA_nacht_dB"] - energiesumme(spek.values())
    teil = {}
    for f in OKTAVEN:
        LWj = spek[f] + norm
        teil[f] = szene.pegel(xy, wp["hoehe_quelle_m"], io["xy"], io["h"], LWj, io["gebaeude"],
                              lam=C_SCHALL / f, alpha=ALPHA_OKTAV[f], DI=wp["DI_dB"])
    L_okt = energiesumme(teil.values())
    L_500 = szene.pegel(xy, wp["hoehe_quelle_m"], io["xy"], io["h"], wp["LWA_nacht_dB"], io["gebaeude"], DI=wp["DI_dB"])
    return {"io": io["id"], "L_A_oktav": L_okt, "L_A_500Hz": L_500, "differenz_dB": L_okt - L_500,
            "baender": {str(f): r1(v) for f, v in teil.items()}}


def rechne(daten: dict, mit_karte: bool = True) -> dict:
    wp = daten["waermepumpe"]
    szene = Szene(daten)
    ios = immissionsorte(daten)
    kandidaten, zul, unz = optimiere(daten, szene, wp, ios)
    if not zul:
        raise RuntimeError("kein zulässiger Aufstellort gefunden")
    opt = dict(zul[0])
    ok, gr, extra = pruefe_standort(opt["xy"], daten, szene, wp, [io["xy"] for io in ios])
    opt["zone"] = extra["schutzbereich"]
    tabelle_opt = standort_bericht(opt["xy"], daten, szene, wp, ios, "Optimum")
    # Referenzstandorte (typische Wahl) zum Vergleich
    refs = []
    for r in daten["berechnung"]["referenzstandorte"]:
        xy = tuple(r["xy"])
        okr, grr, _ = pruefe_standort(xy, daten, szene, wp, [io["xy"] for io in ios])
        tab = standort_bericht(xy, daten, szene, wp, ios, r["id"])
        refs.append({"id": r["id"], "name": r["name"], "xy": list(xy), "zulaessig": okr, "gruende": grr,
                     "reserve_min": min(z["reserve_N_dB"] for z in tab), "tabelle": tab})
    # Teilraum-Optima: bester zulässiger Ort je Grundstücksbereich (zeigt den Zielkonflikt)
    haus = Polygon(next(g for g in daten["gebaeude"] if g["id"] == "EIGEN")["polygon"])
    hx0, hy0, hx1, hy1 = haus.bounds
    bereiche = {"Vorgarten (Süd, straßenseitig)": lambda x, y: y < hy0,
                "Ostseite (zwischen Haus und Gartenmauer)": lambda x, y: x > hx1 and hy0 <= y <= hy1,
                "Westseite (zum Nachbarn West)": lambda x, y: x < hx0 and hy0 <= y <= hy1,
                "Garten (Nord)": lambda x, y: y > hy1}
    teilraum = {}
    for name, bed in bereiche.items():
        kk = [k for k in zul if bed(*k["xy"])]
        teilraum[name] = None if not kk else {"xy": list(kk[0]["xy"]), "reserve_min_N_dB": kk[0]["reserve_min"],
                                              "leitung_m": kk[0]["leitung_m"], "anzahl_zulaessig": len(kk)}
    ost = teilraum["Ostseite (zwischen Haus und Gartenmauer)"]

    # Sensitivität (am Optimum und am besten Ort der Ostseite)
    def rmin_fuer(wp_v, szene_v, xy):
        return min(v["reserve"] for v in bewerte_standort(xy, szene_v, wp_v, ios).values())
    sens = {}
    orte = {"Optimum": opt["xy"]}
    if ost:
        orte["Ostseite"] = tuple(ost["xy"])
    for ort, xy in orte.items():
        s_ = {"basis": rmin_fuer(wp, szene, xy)}
        for dl in (-1.0, +1.0):
            w2 = copy.deepcopy(wp)
            w2["LWA_nacht_dB"] += dl
            s_[f"LWA_{dl:+.0f}dB"] = rmin_fuer(w2, szene, xy)
        for kt in (0.0, 6.0):
            w2 = copy.deepcopy(wp)
            w2["KT_dB"] = kt
            s_[f"KT_{kt:.0f}dB"] = rmin_fuer(w2, szene, xy)
        s_["rho_1.0_alle_Flaechen"] = rmin_fuer(wp, Szene(daten, rho_override=1.0), xy)
        w2 = copy.deepcopy(wp)
        w2["hoehe_quelle_m"] = 1.6
        s_["Wandkonsole_hs_1.6m"] = rmin_fuer(w2, szene, xy)
        s_["ohne_Gartenmauer"] = rmin_fuer(wp, Szene(daten, mit_mauer=False), xy)
        b2 = copy.deepcopy(daten)
        b2["berechnung"]["reflexion_ordnung_max"] = 1
        s_["nur_Reflexion_1_Ordnung"] = rmin_fuer(wp, Szene(b2), xy)
        sens[ort] = s_
    # Rangfolge unter ±1 dB L_WA: alle Pegel verschieben sich um genau ±1 dB → Reihenfolge identisch
    rang_stabil = all(abs((sens[o]["LWA_+1dB"] - sens[o]["basis"]) + 1.0) < 1e-9 for o in sens)
    # Split-Variante: gleiche Akustik, andere Aufstellregeln
    wsp = copy.deepcopy(wp)
    for k, v in daten["variante_split"].items():
        wsp[k] = v
    _, zul_sp, unz_sp = optimiere(daten, szene, wsp, ios)
    split = {"f_gase": f_gase_pruefung(wsp, daten["stichtag"]), "anzahl_zulaessig": len(zul_sp),
             "unzulaessig_gruende": unz_sp,
             "optimum": None if not zul_sp else {"xy": list(zul_sp[0]["xy"]), "reserve_min": zul_sp[0]["reserve_min"],
                                                 "leitung_m": zul_sp[0]["leitung_m"]}}
    # Oktavvergleich (Beispielspektrum) je IO am Optimum und am besten Ort der Ostseite
    def io_zu_zeile(z):
        return next(io for io in ios if io["id"] == z["io"] and
                    (io["teil"] is None or ([r1(io["xy"][0]), r1(io["xy"][1])] == z["xy"] and io["h"] == z["h_m"])))
    okt = {"Optimum": [oktavvergleich(opt["xy"], daten, szene, wp, io_zu_zeile(z)) for z in tabelle_opt]}
    if ost:
        tab_ost = standort_bericht(tuple(ost["xy"]), daten, szene, wp, ios, "Ostseite")
        okt["Ostseite"] = [oktavvergleich(tuple(ost["xy"]), daten, szene, wp, io_zu_zeile(z)) for z in tab_ost]
    erg = {
        "beispiel": "B20 Wärmepumpe Schall und Aufstellung",
        "nachweis_modul": NACHWEIS_MODUL,
        "quellen": [Q_TAL, Q_ISO, Q_LAI, Q_BWP],
        "annahmen": {"gebiet": daten["grundstueck"]["gebiet"], "IRW_N": IRW[daten["grundstueck"]["gebiet"]][1],
                     "lambda_m": szene.lam, "alpha_dB_km": szene.alpha, "C0_dB": szene.C0,
                     "reflexion_ordnung": szene.ordnung, "waermepumpe": {k: v for k, v in wp.items() if k != "schutzbereich"}},
        "f_gase_monoblock": f_gase_pruefung(wp, daten["stichtag"]),
        "raster": {"anzahl": len(kandidaten), "zulaessig": len(zul), "unzulaessig_gruende": unz},
        "optimum": {"xy": list(opt["xy"]), "reserve_min_N_dB": opt["reserve_min"], "leitung_m": opt["leitung_m"],
                    "ausblas_azimut_grad": opt["ausblas_azimut_grad"], "tabelle": tabelle_opt},
        "top5": [{"xy": list(k["xy"]), "reserve_min_N_dB": k["reserve_min"], "leitung_m": k["leitung_m"]} for k in zul[:5]],
        "referenzstandorte": refs,
        "teilraum_optima": teilraum,
        "sensitivitaet_reserve_min_N_dB": {**sens, "rangfolge_bei_LWA_pm1dB_unveraendert": rang_stabil},
        "split_variante": split,
        "oktav_vs_500Hz": okt,
        "_intern": {"kandidaten": kandidaten, "opt": opt, "szene": szene, "ios": ios},
    }
    if mit_karte:
        xs, ys, Z = rasterkarte(szene, wp, opt["xy"], daten)
        erg["_intern"]["karte"] = (xs, ys, Z)
        r1xy = tuple(daten["berechnung"]["referenzstandorte"][0]["xy"])
        erg["_intern"]["karte_R1"] = (rasterkarte(szene, wp, r1xy, daten), r1xy,
                                      pruefe_standort(r1xy, daten, szene, wp, [io["xy"] for io in ios])[2]["schutzbereich"])
    return erg


# --------------------------------------------------------------------------------------
# 12  Ausgabe
# --------------------------------------------------------------------------------------
def _json_sicher(o):
    if isinstance(o, dict):
        return {k: _json_sicher(v) for k, v in o.items() if not k.startswith("_") and k != "zone"}
    if isinstance(o, (list, tuple)):
        return [_json_sicher(v) for v in o]
    if isinstance(o, float):
        return None if not math.isfinite(o) else round(o, 6)
    if isinstance(o, (np.floating,)):
        return round(float(o), 6)
    return o


def markdown_tabelle(zeilen, titel):
    kopf = ("| IO | Raum | d m | A_div | A_atm | A_gr | D_Ω | z m | A_bar | L_dir | n_refl | L_refl | L_AT,N | K_T | "
            "L_r,N | gerundet | IRW N | Reserve | irrelevant? | L_r,T | L_AFmax | BWP L_r,N | LAI L_N | LAI Tab. 5 |\n"
            "|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|---|")
    z = [f"**{titel}**", "", kopf]
    for r in zeilen:
        v = r["vereinfacht"]
        z.append(f"| {r['io']} | {r['raum']} | {r1(r['d_m'])} | {r1(r['A_div'])} | {r1(r['A_atm'])} | {r1(r['A_gr'])} | "
                 f"{r1(r['D_Omega'])} | {'–' if r['z_oben_m'] is None else r1(r['z_oben_m'])} | {r1(r['A_bar'])} | "
                 f"{r1(r['L_dir'])} | {r['n_refl']} | {'–' if r['L_refl'] is None else r1(r['L_refl'])} | {r1(r['L_AT_N'])} | "
                 f"{r['K_T']:g} | {r1(r['L_r_N'])} | {r['L_r_N_gerundet']:.0f} | {r['IRW_N']:.0f} | {r1(r['reserve_N_dB'])} | "
                 f"{'ja' if r['irrelevant_N'] else 'nein'} | {r1(r['L_r_T'])} | {r1(r['L_AFmax_N'])} | {r1(v['BWP_L_r_N'])} | "
                 f"{r1(v['LAI_L_N_Modell'])} | {v['LAI_Tab5_Mindestabstand_m']} m / ist {r1(v['Abstand_horizontal_m'])} m "
                 f"{'✓' if v['LAI_Tab5_eingehalten'] else '✗'} |")
    return "\n".join(z)


def schreibe_ausgaben(erg, daten, ziel: Path = AUSGABE):
    ziel.mkdir(parents=True, exist_ok=True)
    (ziel / "b20_waermepumpe.json").write_text(json.dumps(_json_sicher(erg), ensure_ascii=False, indent=1), encoding="utf-8")
    md = ["# B20 – Wärmepumpe: Schallprognose und Aufstellort (BEISPIELDATEN)", "",
          f"Optimum: x = {erg['optimum']['xy'][0]} m, y = {erg['optimum']['xy'][1]} m, kleinste Reserve zum Nacht-IRW "
          f"{r1(erg['optimum']['reserve_min_N_dB'])} dB, Leitungslänge {r1(erg['optimum']['leitung_m'])} m.", "",
          markdown_tabelle(erg["optimum"]["tabelle"], "Optimum")]
    for r in erg["referenzstandorte"]:
        md += ["", markdown_tabelle(r["tabelle"], f"{r['id']} {r['name']} – {'zulässig' if r['zulaessig'] else 'UNZULÄSSIG: ' + '; '.join(r['gruende'])}")]
    (ziel / "b20_waermepumpe.md").write_text("\n".join(md) + "\n", encoding="utf-8")
    it = erg["_intern"]
    if "karte" in it:
        xs, ys, Z = it["karte"]
        (ziel / "b20_laermkarte.svg").write_text(
            svg_laermkarte(xs, ys, Z, it["opt"]["xy"], daten, it["szene"], it["opt"].get("zone"), it["ios"],
                           "B20 Rasterlärmkarte L_r,Nacht – WP am optimalen Aufstellort"), encoding="utf-8")
    if "karte_R1" in it:
        (xs, ys, Z), xy, zone = it["karte_R1"]
        ref = erg["referenzstandorte"][0]
        (ziel / "b20_laermkarte_R1.svg").write_text(
            svg_laermkarte(xs, ys, Z, xy, daten, it["szene"], zone, it["ios"],
                           f"B20 Rasterlärmkarte L_r,Nacht – Referenz {ref['id']}: {ref['name']}"), encoding="utf-8")
    (ziel / "b20_standortkarte.svg").write_text(
        svg_standortkarte(it["kandidaten"], it["opt"], daten, it["szene"], it["ios"],
                          "B20 Aufstellorte: Reserve zum Irrelevanz-Zielwert (Nacht)"), encoding="utf-8")


def main(argv=None):
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--eingabe", type=Path, default=STANDARD_EINGABE)
    ap.add_argument("--ohne-karte", action="store_true")
    a = ap.parse_args(argv)
    daten = lade_eingabe(a.eingabe)
    erg = rechne(daten, mit_karte=not a.ohne_karte)
    schreibe_ausgaben(erg, daten)
    o = erg["optimum"]
    print(f"Optimum ({o['xy'][0]}/{o['xy'][1]}): Reserve min {r1(o['reserve_min_N_dB'])} dB, Leitung {r1(o['leitung_m'])} m")
    for z in o["tabelle"]:
        print(f"  {z['io']}: L_r,N = {r1(z['L_r_N'])} → {z['L_r_N_gerundet']:.0f} dB(A) (IRW {z['IRW_N']:.0f}), "
              f"L_r,T = {r1(z['L_r_T'])}, BWP {r1(z['vereinfacht']['BWP_L_r_N'])}, LAI {r1(z['vereinfacht']['LAI_L_N_Modell'])}")
    print(f"zulässig {erg['raster']['zulaessig']} von {erg['raster']['anzahl']} Rasterpunkten")
    return erg


if __name__ == "__main__":
    main()

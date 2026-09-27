#!/usr/bin/env python3
"""
B5 – Treppenlauf-Solver nach den Grenzwerten der DIN 18065:2020-08 für
Wohngebäude mit höchstens zwei Wohnungen (Kennwerte nach Recherche 02,
Abschnitt 5; keine Normtexte übernommen).

Eingabe (Kommandozeile): Geschosshöhe (Fußboden OK bis OK), Laufbreite,
optional verfügbare Lauflänge.
Ausgabe: alle zulässigen Lösungen (Tabelle), beste Lösung, ausgabe/treppe.json

Grenzwerte (Wohngebäude ≤ 2 WE, "baurechtlich notwendige Treppe"):
  Steigung s        14 … 20 cm
  Auftritt a        23 … 37 cm
  Schrittmaß 2s + a 59 … 65 cm
  nutzbare Laufbreite ≥ 80 cm

Suchraum und Verfahren:
  * n = Anzahl Steigungen (ganzzahlig), s = Geschosshöhe / n (alle
    Steigungen gleich hoch).
  * a wird im Raster von 5 mm gewählt (übliches Fertigungsraster im
    Treppenbau; Parameter --raster-mm).
  * Geradläufige Treppe: n Steigungen, n − 1 Auftritte, Lauflänge = (n − 1)·a.
  * Der Suchraum ist klein (einige Dutzend Kombinationen); die vollständige
    Aufzählung ist exakt, deterministisch und nachvollziehbar. Ein
    Constraint-Solver (z. B. OR-Tools) ist hier nicht nötig.

Bewertung der zulässigen Lösungen (lexikografisch, kleiner = besser):
  1. |2s + a − 63 cm|              (Zielwert Schrittmaß, Vorgabe der Aufgabe);
                                   Abweichungen bis zur halben Rasterweite
                                   (2,5 mm) gelten als "Ziel erreicht" (= 0),
                                   weil a nur im Raster gewählt werden kann.
                                   Ohne diese Toleranz entschieden
                                   Rundungsreste zugunsten einer 20-stufigen
                                   Treppe mit 6,46 m Lauflänge.
  2. |a − s − 12 cm|               (Bequemlichkeitsregel, Faustregel)
  3. |a + s − 46 cm|               (Sicherheitsregel, Faustregel)
  4. Lauflänge                     (kürzer ist besser)
Die Faustregeln 2 und 3 sind keine Normanforderungen, sondern übliche
Planungsregeln und dienen nur der Auswahl unter gleichwertigen Lösungen.

Aufruf:   python b5_treppe_din18065.py [--geschosshoehe 2.90] [--laufbreite 0.90]
                                        [--max-lauflaenge 4.50]
"""
from __future__ import annotations

import argparse
import json
import math
from dataclasses import dataclass, asdict
from fractions import Fraction
from pathlib import Path

HIER = Path(__file__).resolve().parent

GRENZEN = {  # alle Werte in mm
    "s_min": 140, "s_max": 200,
    "a_min": 230, "a_max": 370,
    "schritt_min": 590, "schritt_max": 650,
    "laufbreite_min": 800,
}
ZIEL_SCHRITTMASS = 630


@dataclass(frozen=True)
class Loesung:
    n_steigungen: int
    n_auftritte: int
    s_mm: float          # Steigung
    a_mm: int            # Auftritt
    schrittmass_mm: float
    lauflaenge_mm: int
    abw_ziel_mm: float
    abw_bequem_mm: float
    abw_sicher_mm: float
    ziel_stufe_mm: float  # 0, wenn |2s+a−630| ≤ Toleranz, sonst die Abweichung

    def schluessel(self):
        return (self.ziel_stufe_mm, self.abw_bequem_mm, self.abw_sicher_mm, self.lauflaenge_mm, self.n_steigungen)


def loese(geschosshoehe_mm: int, laufbreite_mm: int, max_lauflaenge_mm: int | None = None,
          raster_mm: int = 5) -> tuple[list[Loesung], list[str]]:
    """Alle zulässigen Lösungen und Hinweise (z. B. warum keine Lösung)."""
    hinweise = []
    if laufbreite_mm < GRENZEN["laufbreite_min"]:
        hinweise.append(f"Laufbreite {laufbreite_mm} mm < {GRENZEN['laufbreite_min']} mm: unzulässig")
        return [], hinweise
    n_min = math.ceil(geschosshoehe_mm / GRENZEN["s_max"])
    n_max = math.floor(geschosshoehe_mm / GRENZEN["s_min"])
    loesungen = []
    for n in range(n_min, n_max + 1):
        s = Fraction(geschosshoehe_mm, n)  # exakt rechnen, erst zur Ausgabe runden
        a_von = max(GRENZEN["a_min"], math.ceil(GRENZEN["schritt_min"] - 2 * s))
        a_bis = min(GRENZEN["a_max"], math.floor(GRENZEN["schritt_max"] - 2 * s))
        a_von = math.ceil(a_von / raster_mm) * raster_mm
        for a in range(a_von, a_bis + 1, raster_mm):
            lauf = (n - 1) * a
            if max_lauflaenge_mm is not None and lauf > max_lauflaenge_mm:
                continue
            schritt = 2 * s + a
            abw = abs(float(schritt) - ZIEL_SCHRITTMASS)
            loesungen.append(Loesung(
                n_steigungen=n, n_auftritte=n - 1, s_mm=round(float(s), 2), a_mm=a,
                schrittmass_mm=round(float(schritt), 2), lauflaenge_mm=lauf,
                abw_ziel_mm=round(abs(float(schritt) - ZIEL_SCHRITTMASS), 2),
                abw_bequem_mm=round(abs(a - float(s) - 120), 2),
                abw_sicher_mm=round(abs(a + float(s) - 460), 2),
                ziel_stufe_mm=0.0 if abw <= raster_mm / 2 else round(abw, 2)))
    if not loesungen:
        hinweise.append("keine zulässige Kombination im Suchraum")
    return sorted(loesungen, key=Loesung.schluessel), hinweise


def main() -> None:
    ap = argparse.ArgumentParser(description="B5 – Treppenlauf nach DIN 18065 (Wohngebäude ≤ 2 WE)")
    ap.add_argument("--geschosshoehe", type=float, default=2.90, help="m")
    ap.add_argument("--laufbreite", type=float, default=0.90, help="m")
    ap.add_argument("--max-lauflaenge", type=float, default=None, help="m (optional)")
    ap.add_argument("--raster-mm", type=int, default=5)
    args = ap.parse_args()
    gh = round(args.geschosshoehe * 1000)
    lb = round(args.laufbreite * 1000)
    ml = None if args.max_lauflaenge is None else round(args.max_lauflaenge * 1000)
    loesungen, hinweise = loese(gh, lb, ml, args.raster_mm)

    print(f"Geschosshöhe {gh} mm, Laufbreite {lb} mm, max. Lauflänge {ml or '—'} mm, Raster a {args.raster_mm} mm")
    for h in hinweise:
        print("Hinweis:", h)
    print(f"{len(loesungen)} zulässige Lösungen\n")
    print(f"{'Rang':>4} {'n':>3} {'s [mm]':>8} {'a [mm]':>7} {'2s+a':>7} {'Lauf [mm]':>9} {'|Δ63|':>6} {'|a-s-12|':>8}")
    for i, l in enumerate(loesungen, 1):
        print(f"{i:4d} {l.n_steigungen:3d} {l.s_mm:8.2f} {l.a_mm:7d} {l.schrittmass_mm:7.2f} {l.lauflaenge_mm:9d} "
              f"{l.abw_ziel_mm:6.2f} {l.abw_bequem_mm:8.2f}")
    je_n = {}
    for l in loesungen:
        je_n.setdefault(l.n_steigungen, []).append(l.a_mm)
    uebersicht = {n: {"s_mm": round(gh / n, 2), "a_min": min(a), "a_max": max(a), "anzahl": len(a)} for n, a in sorted(je_n.items())}
    beste = loesungen[0] if loesungen else None
    if beste:
        print(f"\nBeste Lösung: {beste.n_steigungen} Steigungen à {beste.s_mm} mm, Auftritt {beste.a_mm} mm, "
              f"Schrittmaß {beste.schrittmass_mm} mm, Lauflänge {beste.lauflaenge_mm} mm")
    out = {"eingabe": {"geschosshoehe_mm": gh, "laufbreite_mm": lb, "max_lauflaenge_mm": ml, "raster_mm": args.raster_mm},
           "grenzen_mm": GRENZEN, "ziel_schrittmass_mm": ZIEL_SCHRITTMASS, "hinweise": hinweise,
           "anzahl_loesungen": len(loesungen), "uebersicht_je_n": uebersicht,
           "beste": asdict(beste) if beste else None, "loesungen": [asdict(l) for l in loesungen]}
    (HIER / "ausgabe").mkdir(exist_ok=True)
    (HIER / "ausgabe" / "treppe.json").write_text(json.dumps(out, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
B3 – U-Wert eines Holzrahmen-Wandaufbaus nach DIN EN ISO 6946 (Verfahren für
Bauteile aus homogenen und inhomogenen Schichten, Abschnitt "Oberer und unterer
Grenzwert des Wärmedurchgangswiderstands").

Eingabe:  daten/wandelement.json (dasselbe Parametermodell wie B1)
Ausgabe:  ausgabe/uwert.json und Konsolenbericht

Vorgehen (ISO 6946, inhomogene Schicht):
  * Das Bauteil wird in Abschnitte (a = Holz, b = Dämmung) mit den
    Flächenanteilen f_a + f_b = 1 zerlegt.
  * Oberer Grenzwert R'_T:  1/R'_T = f_a/R_Ta + f_b/R_Tb
    (parallele Wärmeströme, jeder Abschnitt von innen nach außen gerechnet).
  * Unterer Grenzwert R''_T: jede inhomogene Schicht erhält die äquivalente
    Wärmeleitfähigkeit λ'' = Σ f_i·λ_i; dann R''_T = Rsi + Σ d_j/λ''_j + Rse.
  * R_T = (R'_T + R''_T)/2,  U = 1/R_T,
    maximaler relativer Fehler e = (R'_T − R''_T)/(2·R_T).

Wärmeübergangswiderstände (horizontaler Wärmestrom):
  * Rsi = 0,13 m²K/W.
  * Rse = 0,04 m²K/W, wenn der Putz direkt auf der Holzfaserplatte liegt
    (Außenoberfläche frei bewittert).
  * Rse = 0,13 m²K/W bei hinterlüfteter Fassade: Nach ISO 6946 werden bei einer
    stark belüfteten Luftschicht der Widerstand der Luftschicht und aller
    Schichten außerhalb davon vernachlässigt; als äußerer Übergangswiderstand
    wird der Wert für ruhende Luft (= Rsi) angesetzt, weil die Bekleidung die
    Oberfläche vor Wind schützt. Die Holzfaserplatte liegt in diesem Fall
    innerhalb der Luftschicht und zählt weiter mit.

λ-Werte: BEISPIELWERTE aus typischen Herstellerangaben (Bemessungswerte) bzw.
der Größenordnung nach DIN EN ISO 10456. Die Tabellen der DIN 4108-4 wurden
bewusst NICHT übernommen (Urheberrecht, siehe Recherche 02, Abschnitt 7).

Korrekturen ΔU (ISO 6946, Anhang F): Luftspalte ΔU_g = 0 (Stufe 0, Dämmung
passgenau im Gefach angenommen); mechanische Befestigungen ΔU_f = 0, weil die
Schrauben nur OSB und Ständer verbinden und die Dämmschicht nicht durchdringen.

Aufruf:   python b3_uwert_iso6946.py [--fassade verputzt|hinterlueftet]
"""
from __future__ import annotations

import argparse
import json
from dataclasses import dataclass, asdict
from pathlib import Path

HIER = Path(__file__).resolve().parent
STANDARD_PARAMETER = HIER / "daten" / "wandelement.json"

RSI = 0.13  # m²K/W, horizontaler Wärmestrom
RSE = {"verputzt": 0.04, "hinterlueftet": 0.13}


@dataclass
class Schichtwiderstand:
    id: str
    material: str
    dicke_m: float
    lambda_holz: float | None      # Abschnitt a (Holz) – bei homogener Schicht = lambda
    lambda_daemmung: float | None  # Abschnitt b (Gefach)
    r_holz: float                  # m²K/W im Abschnitt a
    r_daemmung: float              # m²K/W im Abschnitt b
    r_unten: float                 # m²K/W mit λ'' (unterer Grenzwert)


@dataclass
class UWertErgebnis:
    fassade: str
    rsi: float
    rse: float
    holzanteil: float
    r_t_holz: float
    r_t_gefach: float
    r_oben: float        # R'_T
    r_unten: float       # R''_T
    r_t: float
    u_wert: float        # W/(m²K), ungerundet
    u_wert_gerundet: float
    relativer_fehler: float
    schichten: list


def lade_parameter(pfad: Path | str = STANDARD_PARAMETER) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def holzanteil_raster(param: dict) -> float:
    """Holzanteil der Gefachschicht nur aus Ständerbreite und Raster (b/e)."""
    st = param["wand"]["staender"]
    return st["breite"] / st["raster"]


def holzanteil_geometrie(param: dict) -> float:
    """Holzanteil aus der tatsächlichen Ansichtsfläche aller Hölzer (Ständer,
    Schwelle, Rähm, Sturz, Brüstungsriegel) bezogen auf die Wandfläche ohne
    Öffnungen. Nutzt das Rahmenlayout aus B1 (reine Geometrie, kein IFC)."""
    from b1_wandelement import rahmenlayout  # lokal, um Zyklen zu vermeiden

    lay = rahmenlayout(param["wand"])
    return lay["holzflaeche_mm2"] / lay["nettoflaeche_mm2"]


def berechne_uwert(param: dict, holzanteil: float, fassade: str | None = None) -> UWertErgebnis:
    wand = param["wand"]
    mats = param["materialien"]
    fassade = fassade or wand["aussenseite"]["fassade"]
    rse = RSE[fassade]
    lam_holz = mats[wand["staender"]["material"]]["lambda"]
    f_a, f_b = holzanteil, 1.0 - holzanteil

    schichten: list[Schichtwiderstand] = []
    for s in wand["schichten_innen_nach_aussen"]:
        d = s["dicke"] / 1000.0
        lam = mats[s["material"]]["lambda"]
        if s["rolle"] == "gefach":
            # inhomogene Schicht: Holz (a) und Dämmung (b)
            lam_eq = f_a * lam_holz + f_b * lam
            schichten.append(Schichtwiderstand(s["id"], s["material"], d, lam_holz, lam,
                                               d / lam_holz, d / lam, d / lam_eq))
        elif lam is None:
            # Folie: thermisch vernachlässigbar
            schichten.append(Schichtwiderstand(s["id"], s["material"], d, None, None, 0.0, 0.0, 0.0))
        else:
            r = d / lam
            schichten.append(Schichtwiderstand(s["id"], s["material"], d, lam, lam, r, r, r))

    r_ta = RSI + sum(s.r_holz for s in schichten) + rse
    r_tb = RSI + sum(s.r_daemmung for s in schichten) + rse
    r_oben = 1.0 / (f_a / r_ta + f_b / r_tb)
    r_unten = RSI + sum(s.r_unten for s in schichten) + rse
    r_t = (r_oben + r_unten) / 2.0
    u = 1.0 / r_t
    e = (r_oben - r_unten) / (2.0 * r_t)
    return UWertErgebnis(
        fassade=fassade, rsi=RSI, rse=rse, holzanteil=round(holzanteil, 6),
        r_t_holz=round(r_ta, 6), r_t_gefach=round(r_tb, 6),
        r_oben=round(r_oben, 6), r_unten=round(r_unten, 6), r_t=round(r_t, 6),
        u_wert=round(u, 6), u_wert_gerundet=round(u, 3),
        relativer_fehler=round(e, 6),
        schichten=[asdict(s) for s in schichten],
    )


def uwert_fuer_ifc(param: dict) -> float:
    """U-Wert, der in B1 in Pset_WallCommon.ThermalTransmittance geschrieben
    wird: Holzanteil aus der Elementgeometrie (konservativer als das Raster)."""
    return berechne_uwert(param, holzanteil_geometrie(param)).u_wert_gerundet


def bericht(param: dict) -> dict:
    """Alle Varianten: Holzanteil Raster/Geometrie × Fassade verputzt/hinterlüftet."""
    erg = {}
    for name, f in (("raster", holzanteil_raster(param)), ("geometrie", holzanteil_geometrie(param))):
        for fassade in ("verputzt", "hinterlueftet"):
            erg[f"{name}_{fassade}"] = asdict(berechne_uwert(param, f, fassade))
    return erg


def main() -> None:
    ap = argparse.ArgumentParser(description=__doc__.split("\n")[1])
    ap.add_argument("--parameter", default=str(STANDARD_PARAMETER))
    ap.add_argument("--ausgabe", default=str(HIER / "ausgabe" / "uwert.json"))
    args = ap.parse_args()
    param = lade_parameter(args.parameter)
    erg = bericht(param)
    Path(args.ausgabe).parent.mkdir(parents=True, exist_ok=True)
    with open(args.ausgabe, "w", encoding="utf-8") as f:
        json.dump(erg, f, ensure_ascii=False, indent=2, sort_keys=True)
        f.write("\n")
    print(f"{'Variante':28s} {'f_Holz':>7s} {'R_T':>7s} {'R_oben':>7s} {'R_unten':>7s} {'e':>6s} {'U':>7s}")
    for k, v in erg.items():
        print(f"{k:28s} {v['holzanteil']:7.4f} {v['r_t']:7.3f} {v['r_oben']:7.3f} "
              f"{v['r_unten']:7.3f} {v['relativer_fehler']*100:5.2f}% {v['u_wert']:7.4f}")
    print(f"-> {args.ausgabe}")


if __name__ == "__main__":
    main()

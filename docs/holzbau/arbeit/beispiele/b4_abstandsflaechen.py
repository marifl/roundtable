#!/usr/bin/env python3
"""
B4 – Abstandsflächen nach BayBO Art. 6 (Fassung ab 01.05.2026, siehe
Recherche 02, Abschnitt 3) für ein Satteldachhaus, Prüfung gegen die
Grundstücksgrenzen mit shapely.

Eingabe:  daten/grundstueck.json
Ausgabe:  ausgabe/abstandsflaechen.json, ausgabe/abstandsflaechen.md,
          ausgabe/abstandsflaechen_<szenario>.svg

Umgesetzte Regeln (vereinfacht, ebenes Gelände):
  * Abs. 4: Wandhöhe = Gelände bis Schnittpunkt Außenwand/Dachhaut bzw. oberer
    Wandabschluss. H = Wandhöhe + 1/3 der Dachhöhe bei Dachneigung ≤ 70°,
    + volle Dachhöhe bei Dachneigung > 70°.
  * Abs. 5: Tiefe T = 0,4 H, mindestens 3 m (Nicht-Gewerbegebiet).
  * Abs. 2: Abstandsflächen liegen auf dem Grundstück selbst; sie dürfen bis
    zur Mitte einer angrenzenden öffentlichen Verkehrsfläche reichen.
  * Traufseiten: T konstant über die Wandlänge.
  * Giebelseiten: T wird punktweise entlang der Giebelwand bestimmt. Daraus
    ergibt sich eine "gestauchte Giebelform", die unten auf 3 m begrenzt ist.
    Zwei Lesarten sind umschaltbar (Parameter giebel_modus):
      - "drittel" (Standard, entspricht der Aufgabenstellung): Wandhöhe bis
        Traufniveau, das Giebeldreieck zählt wie Dachfläche (≤ 70°) zu 1/3.
      - "voll": das Giebeldreieck ist Teil der Wand und zählt voll
        (Lesart "Giebel sind normale Wände").
    Welche Lesart dem Wortlaut der BayBO 2026 entspricht, ist in dieser Arbeit
    nicht am Primärtext geprüft [U]. Der Zugriff auf gesetze-bayern.de war in der
    Build-Umgebung gesperrt. Das Beispiel zeigt nur die Mechanik.

Nicht umgesetzt: Abs. 5a (Gemeinden > 250.000 Einwohner), Abs. 6
(Dachüberstände, Balkone, Vorbauten), Abs. 7 (Grenzgaragen), Satzungen nach
Art. 81, geneigtes Gelände, Überdeckungsverbot mehrerer Gebäude. Das Ergebnis
ist KEINE Rechtsauskunft.

Aufruf:   python b4_abstandsflaechen.py [--giebel-modus drittel|voll]
"""
from __future__ import annotations

import argparse
import json
import math
from pathlib import Path

from shapely.geometry import LineString, Polygon, box
from shapely.ops import unary_union

HIER = Path(__file__).resolve().parent
STANDARD_PARAMETER = HIER / "daten" / "grundstueck.json"
AUSGABE = HIER / "ausgabe"


def dachhoehe(breite: float, neigung_grad: float) -> float:
    """Höhe des Satteldachs über der Traufe (First mittig)."""
    return breite / 2.0 * math.tan(math.radians(neigung_grad))


def mass_h(wandhoehe: float, dh: float, neigung_grad: float, regel: dict) -> float:
    """BayBO Art. 6 Abs. 4: H = Wandhöhe + Anteil der Dachhöhe."""
    anteil = regel["dach_anteil_unter_grenzneigung"] if neigung_grad <= regel["grenzneigung_grad"] else 1.0
    return wandhoehe + anteil * dh


def tiefe(h: float, regel: dict) -> float:
    """BayBO Art. 6 Abs. 5: T = 0,4 H, mindestens 3 m."""
    return max(regel["faktor"] * h, regel["mindesttiefe"])


def giebelprofil(g: dict, regel: dict, modus: str) -> list[tuple[float, float]]:
    """Tiefe T(u) entlang der Giebelwand (u = 0 … Breite) als Stützpunkte
    [(u, T)]. H(u) ist stückweise linear, T(u) = max(0,4·H(u), 3) daher auch;
    Knickpunkte: Wandenden, First, Übergang zur Mindesttiefe."""
    b, hw, neig = g["breite"], g["wandhoehe"], g["dachneigung_grad"]
    dh = dachhoehe(b, neig)
    if modus == "drittel":
        anteil = regel["dach_anteil_unter_grenzneigung"] if neig <= regel["grenzneigung_grad"] else 1.0
    elif modus == "voll":
        anteil = 1.0
    else:
        raise ValueError(modus)

    def h_von(u):  # Höhe des Giebels an der Stelle u, mit Anrechnungsanteil
        return hw + anteil * dh * (1.0 - abs(u - b / 2) / (b / 2))

    stellen = {0.0, b / 2, b}
    # Übergang zur Mindesttiefe: faktor·h(u) = mindesttiefe
    h_grenz = regel["mindesttiefe"] / regel["faktor"]
    if hw < h_grenz < hw + anteil * dh:
        t = (h_grenz - hw) / (anteil * dh)  # Anteil der halben Breite
        stellen |= {t * b / 2, b - t * b / 2}
    return [(round(u, 6), round(tiefe(h_von(u), regel), 6)) for u in sorted(stellen)]


def abstandsflaechen(g: dict, x0: float, y0: float, regel: dict, modus: str) -> list[dict]:
    """Abstandsflächen der vier Außenwände als Polygone (First in y-Richtung)."""
    b, l = g["breite"], g["laenge"]
    dh = dachhoehe(b, g["dachneigung_grad"])
    h_trauf = mass_h(g["wandhoehe"], dh, g["dachneigung_grad"], regel)
    t_trauf = tiefe(h_trauf, regel)
    prof = giebelprofil(g, regel, modus)
    erg = []
    # Traufseiten West/Ost
    erg.append(dict(wand="West (Traufe)", art="Traufe", H=h_trauf, T_max=t_trauf,
                    normale=(-1, 0), wand_linie=((x0, y0), (x0, y0 + l)),
                    polygon=Polygon([(x0 - t_trauf, y0), (x0, y0), (x0, y0 + l), (x0 - t_trauf, y0 + l)])))
    erg.append(dict(wand="Ost (Traufe)", art="Traufe", H=h_trauf, T_max=t_trauf,
                    normale=(1, 0), wand_linie=((x0 + b, y0), (x0 + b, y0 + l)),
                    polygon=Polygon([(x0 + b, y0), (x0 + b + t_trauf, y0), (x0 + b + t_trauf, y0 + l), (x0 + b, y0 + l)])))
    # Giebelseiten Süd/Nord
    t_max = max(t for _, t in prof)
    h_max = t_max / regel["faktor"] if t_max > regel["mindesttiefe"] else None
    sued = [(x0, y0)] + [(x0 + u, y0 - t) for u, t in prof] + [(x0 + b, y0)]
    nord = [(x0 + b, y0 + l)] + [(x0 + u, y0 + l + t) for u, t in reversed(prof)] + [(x0, y0 + l)]
    erg.append(dict(wand="Süd (Giebel)", art="Giebel", H=h_max, T_max=t_max, normale=(0, -1),
                    wand_linie=((x0, y0), (x0 + b, y0)), polygon=Polygon(sued), profil=prof))
    erg.append(dict(wand="Nord (Giebel)", art="Giebel", H=h_max, T_max=t_max, normale=(0, 1),
                    wand_linie=((x0, y0 + l), (x0 + b, y0 + l)), polygon=Polygon(nord), profil=prof))
    return erg


def zulaessige_flaeche(param: dict) -> Polygon:
    """Grundstück + halbe angrenzende öffentliche Verkehrsfläche (Abs. 2 S. 2)."""
    gs = Polygon(param["grundstueck"])
    st = param.get("strasse")
    if not st:
        return gs
    minx, miny, maxx, maxy = gs.bounds
    halb = st["breite"] / 2
    streifen = {"sued": box(minx, miny - halb, maxx, miny), "nord": box(minx, maxy, maxx, maxy + halb),
                "west": box(minx - halb, miny, minx, maxy), "ost": box(maxx, miny, maxx + halb, maxy)}[st["seite"]]
    return unary_union([gs, streifen])


def vorhandene_tiefe(zul: Polygon, wand_linie, normale) -> float:
    """Abstand von der Wandmitte bis zur Grenze der zulässigen Fläche in
    Richtung der Außennormalen (Strahl mit 1 km Länge)."""
    (xa, ya), (xb, yb) = wand_linie
    mx, my = (xa + xb) / 2, (ya + yb) / 2
    strahl = LineString([(mx, my), (mx + 1000 * normale[0], my + 1000 * normale[1])])
    schnitt = strahl.intersection(zul.boundary)
    pts = [schnitt] if schnitt.geom_type == "Point" else list(getattr(schnitt, "geoms", []))
    return round(min(math.hypot(p.x - mx, p.y - my) for p in pts), 6)


def pruefe_szenario(param: dict, sz: dict, modus: str) -> dict:
    g, regel = param["gebaeude_vorlage"], param["regel"]
    zul = zulaessige_flaeche(param)
    flaechen = abstandsflaechen(g, sz["x"], sz["y"], regel, modus)
    zeilen = []
    for fl in flaechen:
        verletzung = fl["polygon"].difference(zul)
        vorh = vorhandene_tiefe(zul, fl["wand_linie"], fl["normale"])
        zeilen.append(dict(
            wand=fl["wand"], H=None if fl["H"] is None else round(fl["H"], 3), T_erforderlich=round(fl["T_max"], 3),
            T_vorhanden_mitte=vorh, flaeche_m2=round(fl["polygon"].area, 3),
            ueberschreitung_m2=round(verletzung.area, 3), zulaessig=verletzung.area < 1e-9,
            polygon=[(round(x, 3), round(y, 3)) for x, y in fl["polygon"].exterior.coords]))
    return dict(szenario=sz["id"], beschreibung=sz["beschreibung"], giebel_modus=modus,
                x=sz["x"], y=sz["y"], zulaessig=all(z["zulaessig"] for z in zeilen), waende=zeilen,
                dachhoehe=round(dachhoehe(g["breite"], g["dachneigung_grad"]), 3))


def svg(param: dict, erg: dict) -> str:
    """Einfache Lageplan-Skizze (1 m = 20 px), deterministisch formatiert."""
    s = 20.0
    zul = zulaessige_flaeche(param)
    minx, miny, maxx, maxy = zul.buffer(4).bounds
    w, h = (maxx - minx) * s, (maxy - miny) * s

    def pt(x, y):  # y-Achse nach oben
        return f"{(x - minx) * s:.1f},{(maxy - y) * s:.1f}"

    def poly(coords, **attr):
        a = " ".join(f'{k.replace("_", "-")}="{v}"' for k, v in attr.items())
        return f'<polygon points="{" ".join(pt(x, y) for x, y in coords)}" {a}/>'

    g = param["gebaeude_vorlage"]
    teile = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{w:.0f}" height="{h:.0f}" viewBox="0 0 {w:.0f} {h:.0f}" font-family="sans-serif" font-size="11">',
             f'<rect width="{w:.0f}" height="{h:.0f}" fill="#ffffff"/>']
    if param.get("strasse"):
        st_poly = zul.difference(Polygon(param["grundstueck"]))
        teile.append(poly(list(st_poly.exterior.coords), fill="#e6e6e6", stroke="#999999", stroke_dasharray="4 3"))
    teile.append(poly(param["grundstueck"], fill="none", stroke="#000000", stroke_width="2"))
    for z in erg["waende"]:
        farbe = "#4c9a2a" if z["zulaessig"] else "#c0392b"
        teile.append(poly(z["polygon"], fill=farbe, fill_opacity="0.35", stroke=farbe))
    haus = [(erg["x"], erg["y"]), (erg["x"] + g["breite"], erg["y"]), (erg["x"] + g["breite"], erg["y"] + g["laenge"]), (erg["x"], erg["y"] + g["laenge"])]
    teile.append(poly(haus, fill="#8d6e63", stroke="#3e2723", stroke_width="1.5"))
    fx = erg["x"] + g["breite"] / 2
    teile.append(f'<line x1="{pt(fx, erg["y"]).split(",")[0]}" y1="{pt(fx, erg["y"]).split(",")[1]}" '
                 f'x2="{pt(fx, erg["y"] + g["laenge"]).split(",")[0]}" y2="{pt(fx, erg["y"] + g["laenge"]).split(",")[1]}" stroke="#ffffff" stroke-dasharray="6 3"/>')
    x_t, y_t = pt(minx + 0.5, maxy - 1.2).split(",")
    teile.append(f'<text x="{x_t}" y="{y_t}">Szenario {erg["szenario"]} ({erg["giebel_modus"]}): '
                 f'{"zulässig" if erg["zulaessig"] else "NICHT zulässig"}</text>')
    teile.append("</svg>")
    return "\n".join(teile) + "\n"


def markdown(ergebnisse: list[dict]) -> str:
    z = ["# Abstandsflächen BayBO Art. 6 – Ergebnisse (Beispiel)", ""]
    for e in ergebnisse:
        z += [f"## Szenario `{e['szenario']}` – {e['beschreibung']} (Giebel: {e['giebel_modus']})", "",
              f"Dachhöhe {e['dachhoehe']:.2f} m · Ergebnis: **{'zulässig' if e['zulaessig'] else 'nicht zulässig'}**", "",
              "| Wand | H [m] | T erf. [m] | T vorh. (Mitte) [m] | Fläche [m²] | außerhalb [m²] | ok |",
              "|---|---:|---:|---:|---:|---:|---|"]
        for w in e["waende"]:
            hs = "–" if w["H"] is None else f"{w['H']:.2f}"
            z.append(f"| {w['wand']} | {hs} | {w['T_erforderlich']:.2f} | {w['T_vorhanden_mitte']:.2f} | "
                     f"{w['flaeche_m2']:.2f} | {w['ueberschreitung_m2']:.2f} | {'✔' if w['zulaessig'] else '✘'} |")
        z.append("")
    z.append("H bei Giebeln: größtes angerechnetes Maß (am First); „–“, wenn überall die Mindesttiefe 3 m maßgebend ist.")
    return "\n".join(z) + "\n"


def main() -> None:
    ap = argparse.ArgumentParser(description="B4 – Abstandsflächen BayBO Art. 6")
    ap.add_argument("--parameter", default=str(STANDARD_PARAMETER))
    ap.add_argument("--giebel-modus", default="drittel", choices=["drittel", "voll"])
    args = ap.parse_args()
    with open(args.parameter, encoding="utf-8") as f:
        param = json.load(f)
    AUSGABE.mkdir(exist_ok=True)
    ergebnisse = [pruefe_szenario(param, sz, args.giebel_modus) for sz in param["szenarien"]]
    # Vergleich der Lesarten für das erste Szenario
    ergebnisse.append(pruefe_szenario(param, param["szenarien"][0], "voll" if args.giebel_modus == "drittel" else "drittel"))
    for e in ergebnisse:
        (AUSGABE / f"abstandsflaechen_{e['szenario']}_{e['giebel_modus']}.svg").write_text(svg(param, e), encoding="utf-8")
    (AUSGABE / "abstandsflaechen.json").write_text(json.dumps(ergebnisse, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md = markdown(ergebnisse)
    (AUSGABE / "abstandsflaechen.md").write_text(md, encoding="utf-8")
    print(md)


if __name__ == "__main__":
    main()

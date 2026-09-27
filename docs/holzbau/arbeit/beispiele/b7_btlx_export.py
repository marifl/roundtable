#!/usr/bin/env python3
"""
B7 (optional) – BTLx-Export der Hölzer des Wandelements aus B1 mit
compas_timber (MIT-Lizenz, Beta; siehe Recherche 01).

Eingabe:  daten/wandelement.json (dasselbe Rahmenlayout wie B1)
Ausgabe:  ausgabe/wandelement.btlx

Vorgehen:
  * Jedes Holz aus b1_wandelement.rahmenlayout() wird zu einem
    compas_timber-Beam (Mittellinie, Breite, Höhe, z-Vektor). Die Koordinaten
    sind die Wandkoordinaten aus B1 (mm).
  * Die Kerve K1 wird als BTLx-Bearbeitung "Lap" (Blatt/Kerve) aus dem
    Abzugsvolumen erzeugt (Lap.from_volume_and_beam).
  * compas_timber 2.2.0 schreibt Material/TimberGrade leer, Datum/Uhrzeit der
    Systemuhr und zufällige GUIDs (uuid4). Für Reproduzierbarkeit wird das
    XML nachbearbeitet: Material "KVH C24", TimberGrade "C24", Datum und Zeit
    aus dem JSON, Transformation-GUIDs = uuid5(Pfad des Holzes) wie in B1.
    ElementNumber (die ersten vier Zeichen der GUID) wird entsprechend gesetzt.

Grenzen: keine Verbindungen (Joints) zwischen den Hölzern, keine Nagel-/
Schraubbilder, keine Plattenbauteile. Weinmann-Anlagen lesen WUP statt BTLx
(Recherche 01); B7 zeigt nur den Abbundpfad.

Aufruf:   python b7_btlx_export.py
"""
from __future__ import annotations

import re
import uuid
import xml.etree.ElementTree as ET
from pathlib import Path

from compas.geometry import Box, Frame, Line, Point, Vector
from compas.tolerance import Tolerance
from compas_timber.elements import Beam
from compas_timber.fabrication import BTLxWriter, Lap
from compas_timber.model import TimberModel

import b1_wandelement as b1

HIER = Path(__file__).resolve().parent
AUSGABE = HIER / "ausgabe" / "wandelement.btlx"
NS = "https://www.design2machine.com"


def baue_modell(param: dict) -> tuple[TimberModel, list[str]]:
    w = param["wand"]
    lay = b1.rahmenlayout(w)
    y_kern = b1.schichtlage(w)["gefach"]
    tiefe = w["staender"]["tiefe"]
    y_mitte = y_kern[0] + tiefe / 2
    modell = TimberModel(tolerance=Tolerance(unit="MM"))
    pfade, beams = [], {}
    for h in lay["hoelzer"]:
        liegend = h["typ"] == "PLATE" or h["rolle"] == "Sturz"
        if liegend:  # Achse in x, Querschnitt (Höhe in z) × (Tiefe in y)
            zc = (h["z0"] + h["z1"]) / 2
            linie = Line(Point(h["x0"], y_mitte, zc), Point(h["x1"], y_mitte, zc))
            breite = h["z1"] - h["z0"]
        else:        # Achse in z
            xc = (h["x0"] + h["x1"]) / 2
            linie = Line(Point(xc, y_mitte, h["z0"]), Point(xc, y_mitte, h["z1"]))
            breite = h["x1"] - h["x0"]
        beam = Beam.from_centerline(linie, width=breite, height=tiefe, z_vector=Vector(0, 1, 0))
        beam.name = h["name"]
        modell.add_element(beam)
        beams[h["pfad"]] = (beam, h)
        pfade.append(h["pfad"])
    # Kerven als Lap-Bearbeitung
    for kv in w["kerven"]:
        beam, h = beams[f"/wand/staender/raster/{kv['staender_rasterindex']}"]
        xc = (h["x0"] + h["x1"]) / 2
        u = b1.UEBERSTAND
        box = Box(h["x1"] - h["x0"] + 2 * u, kv["tiefe"] + u, kv["hoehe"],
                  frame=Frame(Point(xc, y_kern[0] + (kv["tiefe"] - u) / 2, kv["z"] + kv["hoehe"] / 2), Vector(1, 0, 0), Vector(0, 1, 0)))
        lap = Lap.from_volume_and_beam(box.to_polyhedron(), beam)
        beam.add_feature(lap)
    return modell, pfade


def deterministisch(xml: str, pfade: list[str], param: dict) -> str:
    """Datum/Uhrzeit, GUIDs, Material nachtragen (siehe Modulkommentar)."""
    ET.register_namespace("", NS)
    ET.register_namespace("xsi", "http://www.w3.org/2001/XMLSchema-instance")
    root = ET.fromstring(xml)
    datum, zeit = param["projekt"]["zeitstempel"].split("T")
    for e in root.iter(f"{{{NS}}}InitialExportProgram"):
        e.set("Date", datum)
        e.set("Time", zeit)
    teile = list(root.iter(f"{{{NS}}}Part"))
    assert len(teile) == len(pfade), (len(teile), len(pfade))
    for part, pfad in zip(teile, pfade):
        g = str(uuid.uuid5(b1.GUID_NAMENSRAUM, "btlx:" + pfad))
        part.set("Material", "KVH C24")
        part.set("TimberGrade", "C24")
        part.set("ElementNumber", g[:4])
        for t in part.iter(f"{{{NS}}}Transformation"):
            t.set("GUID", "{" + g + "}")
    ET.indent(root, space="   ")
    return '<?xml version="1.0" encoding="UTF-8"?>\n' + ET.tostring(root, encoding="unicode") + "\n"


def exportiere(param: dict, ziel: Path = AUSGABE) -> Path:
    modell, pfade = baue_modell(param)
    writer = BTLxWriter(project_name=param["projekt"]["name"], company_name=param["projekt"]["organisation"],
                        file_name=ziel.name, comment="B7 – Beispiel, Hölzer aus B1")
    xml = writer.model_to_xml(modell)
    ziel.parent.mkdir(parents=True, exist_ok=True)
    ziel.write_text(deterministisch(xml, pfade, param), encoding="utf-8")
    return ziel


def main() -> None:
    param = b1.lade_parameter()
    ziel = exportiere(param)
    text = ziel.read_text(encoding="utf-8")
    print(f"{ziel}: {len(re.findall('<Part ', text))} Parts, "
          f"{len(re.findall('<Lap ', text))} Lap-Bearbeitung(en), {ziel.stat().st_size} Bytes")


if __name__ == "__main__":
    main()

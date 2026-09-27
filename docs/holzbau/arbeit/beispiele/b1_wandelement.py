#!/usr/bin/env python3
"""
B1 – Parametrisches Holzrahmen-Wandelement: Parametermodell (JSON) →
deterministischer Code → IFC4X3_ADD2 (ISO 16739-1:2024).

Eingabe:  daten/wandelement.json
Ausgabe:  ausgabe/wandelement.ifc

Klassen-Mapping (vgl. Recherche 01, geprüft an IfcOpenShell 0.8.5):

  Bauteil                         IFC-Klasse                     PredefinedType
  ------------------------------  -----------------------------  -----------------
  Wandelement                     IfcWall (+IfcRelAggregates,    ELEMENTEDWALL
                                  +IfcMaterialLayerSetUsage)
  Wandtyp                         IfcWallType (+IfcMaterialLayerSet) ELEMENTEDWALL
  Ständer, Königs-, Sturzauflager-,
  Füllständer, Sturz              IfcMember                      STUD
  Schwelle, Rähm, Brüstungsriegel IfcMember                      PLATE
  Beplankung GKF, OSB, HFD        IfcPlate                       SHEET
  Gefachdämmung                   IfcBuildingElementPart         INSULATION
  Dampfbremse                     IfcBuildingElementPart         USERDEFINED/MEMBRANE
                                  (alternativ IfcCovering MEMBRANE, s. u.)
  Kerve                           IfcVoidingFeature              NOTCH
                                  (+IfcRelVoidsElement)
  Schraube                        IfcMechanicalFastener          SCREW
                                  (+IfcMechanicalFastenerType mit NominalDiameter
                                  und NominalLength, Geometrie als IfcMappedItem)
  Fensteröffnung                  IfcOpeningElement              OPENING

Begründung Folie als IfcBuildingElementPart (Standard, umschaltbar über
"folie_als" im JSON):
  * Die Dampfbremse wird im Werk als Bestandteil des vorgefertigten Elements
    eingebaut. IfcBuildingElementPart ist in IFC 4.3 genau für Teile gedacht,
    die zu einem Bauteil zusammengesetzt werden (Beispiel der Norm: Dämmung in
    einer Ständerwand). Damit hängen ALLE Schichten einheitlich über
    IfcRelAggregates an der IfcWall.
  * IfcCovering beschreibt in IFC eine Bekleidung, die über
    IfcRelCoversBldgElements auf ein Bauteil aufgebracht wird (Oberfläche,
    Ausbau). Das passt zu einer innenliegenden Schicht im Elementquerschnitt
    schlechter. Vorteil von IfcCovering wäre das Enum MEMBRANE und der
    Pset_CoveringTypeMembrane; bei IfcBuildingElementPart fehlt ein solches
    Enum, daher USERDEFINED mit ObjectType "MEMBRANE" und eigenem Pset.

Determinismus:
  * GlobalIds: uuid5(Namensraum, Pfad im Parametermodell), z. B.
    "/wand/staender/raster/3" → ifcopenshell.guid.compress(uuid.hex).
    Beziehungen und Psets erhalten Pfade, die aus dem Pfad ihres Bezugsobjekts
    abgeleitet werden (z. B. "/wand/staender/raster/3#Pset_MemberCommon").
    Folge: Ein Ständer behält seine GUID, wenn sich an anderer Stelle der Wand
    etwas ändert (Änderungsverfolgung).
  * Zeitstempel im STEP-Header kommt aus dem JSON, nicht aus der Uhr.
  * Alle Listen werden in fester Reihenfolge erzeugt (keine dict/set-Iteration
    über Hashwerte); Polygone aus shapely werden kanonisch normalisiert.
  * Die Datei ist damit bei gleicher Eingabe und gleicher IfcOpenShell-Version
    byte-identisch (siehe tests/test_b1_wandelement.py).

Koordinaten des Elements (lokal zur Wand): x entlang der Wand (0…Länge),
y durch den Querschnitt (0 = Raumseite, positiv nach außen), z nach oben.
Längeneinheit mm, Flächen m², Volumen m³.

Aufruf:   python b1_wandelement.py [--parameter daten/wandelement.json]
                                    [--ausgabe ausgabe/wandelement.ifc]
"""
from __future__ import annotations

import argparse
import json
import uuid
from pathlib import Path

import ifcopenshell
import ifcopenshell.api
import ifcopenshell.api.classification
import ifcopenshell.api.context
import ifcopenshell.api.material
import ifcopenshell.api.pset
import ifcopenshell.api.root
import ifcopenshell.api.unit
import ifcopenshell.guid
from shapely.geometry import Point, Polygon, box
from shapely.geometry.polygon import orient
from shapely.ops import unary_union

HIER = Path(__file__).resolve().parent
STANDARD_PARAMETER = HIER / "daten" / "wandelement.json"
STANDARD_AUSGABE = HIER / "ausgabe" / "wandelement.ifc"

# Fester Namensraum für uuid5 (selbst gewählt, einmalig erzeugt und hier fixiert).
GUID_NAMENSRAUM = uuid.UUID("6f1c3b0e-8a52-5d7e-9c4b-2a1d0e7f4b10")
UEBERSTAND = 1.0  # mm, Überstand von Abzugskörpern (Kerve)


# ---------------------------------------------------------------------------
# 1. Reine Geometrie: Rahmenlayout (ohne IFC, auch von B3 genutzt)
# ---------------------------------------------------------------------------

def rahmenlayout(wand: dict) -> dict:
    """Berechnet alle Hölzer als achsparallele Rechtecke in der Wandansicht
    (x, z) sowie Öffnungen, Gefache und Flächenkennwerte.

    Regeln (Holzrahmenbau, vereinfacht):
      * Schwelle unten und Rähm oben über die ganze Länge.
      * Randständer an beiden Enden, Rasterständer bei k·Raster (Achsmaß).
      * Je Öffnung: Königsständer (durchgehend), Sturzauflagerständer
        (Jack-Stud, bis Unterkante Sturz), Sturz über beide Auflager,
        Brüstungsriegel unter der Öffnung, Füllständer ober- und unterhalb
        an Rasterpositionen, die in die Öffnung fallen.
      * Rasterständer, die mit Königs-/Sturzauflagerständern kollidieren,
        entfallen (werden durch diese ersetzt).
    """
    L, H = wand["laenge"], wand["hoehe"]
    b = wand["staender"]["breite"]
    e = wand["staender"]["raster"]
    hs, hr = wand["schwelle"]["hoehe"], wand["raehm"]["hoehe"]
    z_u, z_o = hs, H - hr  # lichter Bereich zwischen Schwelle und Rähm

    hoelzer: list[dict] = []

    def holz(pfad, name, typ, x0, x1, z0, z1, rolle):
        if x1 - x0 <= 0 or z1 - z0 <= 0:
            return
        hoelzer.append(dict(pfad=pfad, name=name, typ=typ, rolle=rolle,
                            x0=x0, x1=x1, z0=z0, z1=z1))

    holz("/wand/schwelle", "Schwelle", "PLATE", 0, L, 0, hs, "Schwelle")
    holz("/wand/raehm", "Rähm", "PLATE", 0, L, z_o, H, "Rähm")
    holz("/wand/staender/rand/links", "Randständer links", "STUD", 0, b, z_u, z_o, "Randständer")
    holz("/wand/staender/rand/rechts", "Randständer rechts", "STUD", L - b, L, z_u, z_o, "Randständer")

    oeffnungen = []
    sperrzonen = []  # (x0, x1, Öffnung) – Bereich Königsständer bis Königsständer
    for o in wand["oeffnungen"]:
        xo, w = o["x"], o["breite"]
        zb, h, hst = o["bruestungshoehe"], o["hoehe"], o["sturz_hoehe"]
        p = f"/wand/oeffnungen/{o['id']}"
        if xo - 2 * b < b or xo + w + 2 * b > L - b:
            raise ValueError(f"Öffnung {o['id']}: zu nah am Wandende")
        if zb + h + hst > z_o or zb - b < z_u:
            raise ValueError(f"Öffnung {o['id']}: passt nicht zwischen Schwelle und Rähm")
        oeffnungen.append(dict(pfad=p, id=o["id"], art=o["art"], x0=xo, x1=xo + w, z0=zb, z1=zb + h))
        holz(f"{p}/koenigsstaender/links", f"Königsständer links {o['id']}", "STUD", xo - 2 * b, xo - b, z_u, z_o, "Königsständer")
        holz(f"{p}/koenigsstaender/rechts", f"Königsständer rechts {o['id']}", "STUD", xo + w + b, xo + w + 2 * b, z_u, z_o, "Königsständer")
        holz(f"{p}/sturzauflager/links", f"Sturzauflagerständer links {o['id']}", "STUD", xo - b, xo, z_u, zb + h, "Sturzauflagerständer")
        holz(f"{p}/sturzauflager/rechts", f"Sturzauflagerständer rechts {o['id']}", "STUD", xo + w, xo + w + b, z_u, zb + h, "Sturzauflagerständer")
        holz(f"{p}/sturz", f"Sturz {o['id']}", "STUD", xo - b, xo + w + b, zb + h, zb + h + hst, "Sturz")
        holz(f"{p}/bruestungsriegel", f"Brüstungsriegel {o['id']}", "PLATE", xo, xo + w, zb - b, zb, "Brüstungsriegel")
        sperrzonen.append((xo - 2 * b, xo + w + 2 * b, o))

    k = 1
    while True:
        c = k * e
        x0, x1 = c - b / 2, c + b / 2
        if x1 > L - b:
            break
        pfad = f"/wand/staender/raster/{k}"
        kollision = None
        for s0, s1, o in sperrzonen:
            if x0 < s1 and x1 > s0:
                kollision = o
                break
        if kollision is None:
            holz(pfad, f"Ständer R{k}", "STUD", x0, x1, z_u, z_o, "Ständer")
        else:
            o = kollision
            xo, w = o["x"], o["breite"]
            if x0 >= xo and x1 <= xo + w:
                zb, h, hst = o["bruestungshoehe"], o["hoehe"], o["sturz_hoehe"]
                holz(f"{pfad}/unten", f"Füllständer R{k} unten", "STUD", x0, x1, z_u, zb - b, "Füllständer")
                holz(f"{pfad}/oben", f"Füllständer R{k} oben", "STUD", x0, x1, zb + h + hst, z_o, "Füllständer")
            # sonst: entfällt, ersetzt durch Königs-/Sturzauflagerständer
        k += 1

    # Gefache = Wandfläche − Öffnungen − Hölzer
    wandflaeche = box(0, 0, L, H)
    oeff_union = unary_union([box(o["x0"], o["z0"], o["x1"], o["z1"]) for o in oeffnungen]) if oeffnungen else Polygon()
    holz_union = unary_union([box(h["x0"], h["z0"], h["x1"], h["z1"]) for h in hoelzer])
    gefach_geom = wandflaeche.difference(oeff_union).difference(holz_union)
    gefache = sorted((kanonisch(p) for p in _polygone(gefach_geom)), key=lambda p: (p.bounds[0], p.bounds[1]))

    holzflaeche = sum((h["x1"] - h["x0"]) * (h["z1"] - h["z0"]) for h in hoelzer)
    # Plausibilität: Hölzer dürfen sich nicht überlappen
    assert abs(holz_union.area - holzflaeche) < 1e-6, "Hölzer überlappen sich"
    netto = wandflaeche.difference(oeff_union).area
    return dict(hoelzer=hoelzer, oeffnungen=oeffnungen, gefache=gefache,
                holzflaeche_mm2=holzflaeche, nettoflaeche_mm2=netto,
                bruttoflaeche_mm2=L * H, oeffnungen_union=oeff_union)


def _polygone(geom) -> list[Polygon]:
    if geom.is_empty:
        return []
    if geom.geom_type == "Polygon":
        return [geom]
    return [g for g in geom.geoms if g.geom_type == "Polygon" and g.area > 1e-9]


def _ring_kanonisch(coords: list[tuple[float, float]]) -> list[tuple[float, float]]:
    """Ring ohne Schlusspunkt, beginnend beim lexikografisch kleinsten Punkt,
    kollineare Zwischenpunkte entfernt → unabhängig von der GEOS-Ausgabe."""
    pts = [(round(x, 3), round(y, 3)) for x, y in coords[:-1]]
    # kollineare Punkte entfernen
    sauber = []
    n = len(pts)
    for i in range(n):
        a, p, c = pts[i - 1], pts[i], pts[(i + 1) % n]
        if abs((p[0] - a[0]) * (c[1] - p[1]) - (p[1] - a[1]) * (c[0] - p[0])) > 1e-9:
            sauber.append(p)
    i0 = sauber.index(min(sauber))
    return sauber[i0:] + sauber[:i0]


def kanonisch(poly: Polygon) -> Polygon:
    poly = orient(poly, 1.0)  # außen gegen den Uhrzeigersinn, Löcher im Uhrzeigersinn
    aussen = _ring_kanonisch(list(poly.exterior.coords))
    innen = sorted((_ring_kanonisch(list(r.coords)) for r in poly.interiors), key=lambda r: r[0])
    return Polygon(aussen, innen)


def schichtlage(wand: dict) -> dict:
    """y-Lage jeder Schicht (innen → außen): {id: (y_innen, y_aussen)}."""
    lage, y = {}, 0.0
    for s in wand["schichten_innen_nach_aussen"]:
        lage[s["id"]] = (round(y, 3), round(y + s["dicke"], 3))
        y += s["dicke"]
    return lage


def plattenteilung(wand: dict, schicht: dict, oeff_union) -> list[tuple[str, Polygon]]:
    """Platten einer Beplankungsschicht: Raster der Plattenbreite ab x = 0,
    Öffnungen ausgeschnitten. Rückgabe: [(pfad, polygon)]."""
    L, H = wand["laenge"], wand["hoehe"]
    pb = schicht.get("plattenbreite", L)
    teile, j, x = [], 1, 0
    while x < L:
        roh = box(x, 0, min(x + pb, L), H).difference(oeff_union)
        polys = sorted((kanonisch(p) for p in _polygone(roh)), key=lambda p: (p.bounds[0], p.bounds[1]))
        for i, p in enumerate(polys):
            suffix = "" if len(polys) == 1 else f"/teil/{i + 1}"
            teile.append((f"/wand/schichten/{schicht['id']}/platte/{j}{suffix}", p))
        x += pb
        j += 1
    return teile


# ---------------------------------------------------------------------------
# 2. IFC-Erzeugung
# ---------------------------------------------------------------------------

class IfcWandBauer:
    """Baut die IFC-Datei. Jede erzeugte IfcRoot-Instanz wird mit ihrem Pfad
    registriert; die GUIDs werden am Ende deterministisch gesetzt."""

    def __init__(self, param: dict):
        self.p = param
        self.wand = param["wand"]
        self.f = ifcopenshell.file(schema="IFC4X3_ADD2")
        self.pfade: dict[int, str] = {}
        self._mat_cache: dict[str, object] = {}

    # --- kleine Helfer ----------------------------------------------------
    def neu(self, ifc_klasse: str, pfad: str, name: str | None = None, predefined: str | None = None, **attr):
        ent = ifcopenshell.api.root.create_entity(self.f, ifc_class=ifc_klasse, predefined_type=predefined, name=name)
        for k, v in attr.items():
            setattr(ent, k, v)
        self.pfade[ent.id()] = pfad
        return ent

    def punkt(self, *c):
        return self.f.createIfcCartesianPoint([float(round(v, 3)) for v in c])

    def richtung(self, *c):
        return self.f.createIfcDirection([float(v) for v in c])

    def achse3d(self, ursprung=(0.0, 0.0, 0.0), z=None, x=None):
        return self.f.createIfcAxis2Placement3D(
            self.punkt(*ursprung), self.richtung(*z) if z else None, self.richtung(*x) if x else None)

    def platzierung(self, relativ_zu, ursprung=(0.0, 0.0, 0.0)):
        return self.f.createIfcLocalPlacement(relativ_zu, self.achse3d(ursprung))

    def form(self, kontext, typ: str, items):
        rep = self.f.createIfcShapeRepresentation(kontext, kontext.ContextIdentifier, typ, items)
        return self.f.createIfcProductDefinitionShape(None, None, [rep])

    def quader_entlang(self, dx, dy, dz, achse: str):
        """Quader mit Ursprung (0,0,0) und Kantenlängen dx, dy, dz als
        IfcExtrudedAreaSolid; extrudiert entlang der Bauteilachse
        ('z' für Ständer, 'x' für liegende Hölzer)."""
        if achse == "z":
            prof = self.f.createIfcRectangleProfileDef(
                "AREA", None, self.f.createIfcAxis2Placement2D(self.f.createIfcCartesianPoint([dx / 2, dy / 2]), None), dx, dy)
            return self.f.createIfcExtrudedAreaSolid(prof, self.achse3d(), self.richtung(0, 0, 1), float(dz))
        # achse == "x": Profil in der (y,z)-Ebene, extrudiert in +x
        prof = self.f.createIfcRectangleProfileDef(
            "AREA", None, self.f.createIfcAxis2Placement2D(self.f.createIfcCartesianPoint([dy / 2, dz / 2]), None), dy, dz)
        return self.f.createIfcExtrudedAreaSolid(prof, self.achse3d(z=(1, 0, 0), x=(0, 1, 0)), self.richtung(0, 0, 1), float(dx))

    def platte_solid(self, poly: Polygon, x0: float, z0: float, dicke: float):
        """Polygon in der Wandebene (x, z), relativ zu (x0, z0), extrudiert um
        'dicke' in Richtung −y (Platzierung liegt auf der Außenseite der Schicht).
        Lokales System: x = Wand-x, y = Wand-z, z = −Wand-y."""
        def kurve(ring):
            pts = [self.f.createIfcCartesianPoint([float(round(x - x0, 3)), float(round(z - z0, 3))]) for x, z in ring]
            return self.f.createIfcPolyline(pts + [pts[0]])
        aussen = kurve(list(poly.exterior.coords)[:-1])
        loecher = [kurve(list(r.coords)[:-1]) for r in poly.interiors]
        if loecher:
            prof = self.f.createIfcArbitraryProfileDefWithVoids("AREA", None, aussen, loecher)
        else:
            prof = self.f.createIfcArbitraryClosedProfileDef("AREA", None, aussen)
        return self.f.createIfcExtrudedAreaSolid(prof, self.achse3d(z=(0, -1, 0), x=(1, 0, 0)), self.richtung(0, 0, 1), float(dicke))

    def material(self, key: str):
        if key in self._mat_cache:
            return self._mat_cache[key]
        m = self.p["materialien"][key]
        mat = ifcopenshell.api.material.add_material(self.f, name=m["name"], category=m["kategorie"])
        if m.get("lambda") is not None:
            ps = ifcopenshell.api.pset.add_pset(self.f, product=mat, name="Pset_MaterialThermal")
            ifcopenshell.api.pset.edit_pset(self.f, pset=ps, properties={"ThermalConductivity": float(m["lambda"])})
        if m.get("rho") is not None:
            ps = ifcopenshell.api.pset.add_pset(self.f, product=mat, name="Pset_MaterialCommon")
            ifcopenshell.api.pset.edit_pset(self.f, pset=ps, properties={"MassDensity": float(m["rho"])})
        if m["kategorie"] == "wood":
            ps = ifcopenshell.api.pset.add_pset(self.f, product=mat, name="Pset_MaterialWood")
            ifcopenshell.api.pset.edit_pset(self.f, pset=ps, properties={"Species": m["art"], "StrengthGrade": m["festigkeit"]})
        self._mat_cache[key] = mat
        return mat

    def pset(self, produkt, name, werte: dict):
        ps = ifcopenshell.api.pset.add_pset(self.f, product=produkt, name=name)
        ifcopenshell.api.pset.edit_pset(self.f, pset=ps, properties=werte)

    def qto(self, produkt, name, werte: dict):
        q = ifcopenshell.api.pset.add_qto(self.f, product=produkt, name=name)
        ifcopenshell.api.pset.edit_qto(self.f, qto=q, properties=werte)

    def beziehung(self, klasse: str, pfad: str, **attr):
        """Objektbeziehung (IfcRel*) direkt anlegen statt über ifcopenshell.api.

        Grund: Einige API-Funktionen (aggregate.assign_object, unit.assign_unit,
        type.assign_type, material.assign_material für mehrere Objekte) arbeiten
        intern mit Python-Mengen (set). Deren Iterationsreihenfolge hängt vom
        Hash-Seed des Interpreters ab; Platzierungen und Listen wurden dann in
        wechselnder Reihenfolge erzeugt (im Test mit PYTHONHASHSEED=1/2/3/99
        nachgewiesen: vier verschiedene Prüfsummen). Mit expliziten Listen ist
        die Ausgabe byte-identisch."""
        ent = self.f.create_entity(klasse, GlobalId=ifcopenshell.guid.compress(uuid.uuid5(GUID_NAMENSRAUM, pfad).hex), **attr)
        self.pfade[ent.id()] = pfad
        return ent

    # --- Aufbau -----------------------------------------------------------
    def baue(self) -> ifcopenshell.file:
        f, w, pj = self.f, self.wand, self.p["projekt"]
        lay = rahmenlayout(w)
        lage = schichtlage(w)
        dicke_gesamt = round(sum(s["dicke"] for s in w["schichten_innen_nach_aussen"]), 3)
        y_kern = lage["gefach"]

        # Projekt, Einheiten, Kontexte
        projekt = self.neu("IfcProject", "/projekt", pj["name"])
        einheiten = [
            ifcopenshell.api.unit.add_si_unit(f, unit_type="LENGTHUNIT", prefix="MILLI"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="AREAUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="VOLUMEUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="PLANEANGLEUNIT"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="MASSUNIT", prefix="KILO"),
            ifcopenshell.api.unit.add_si_unit(f, unit_type="THERMODYNAMICTEMPERATUREUNIT"),
        ]
        projekt.UnitsInContext = f.createIfcUnitAssignment(einheiten)  # feste Reihenfolge
        modell = ifcopenshell.api.context.add_context(f, context_type="Model")
        body = ifcopenshell.api.context.add_context(f, context_type="Model", context_identifier="Body", target_view="MODEL_VIEW", parent=modell)
        axis = ifcopenshell.api.context.add_context(f, context_type="Model", context_identifier="Axis", target_view="GRAPH_VIEW", parent=modell)

        # Georeferenzierung (IfcMapConversion → EPSG:25832)
        geo = pj.get("georeferenz", {})
        if geo.get("aktiv"):
            meter = f.createIfcSIUnit(None, "LENGTHUNIT", None, "METRE")
            crs = f.createIfcProjectedCRS(geo["epsg"], "ETRS89 / UTM zone 32N", "ETRS89", "DHHN2016", "UTM", "32N", meter)
            f.createIfcMapConversion(modell, crs, geo["ostwert_m"], geo["nordwert_m"], geo["hoehe_m"],
                                     geo["x_achse_abszisse"], geo["x_achse_ordinate"], 0.001)

        # Räumliche Struktur
        site = self.neu("IfcSite", "/projekt/grundstueck", "Grundstück", ObjectPlacement=self.platzierung(None))
        geb = self.neu("IfcBuilding", "/projekt/gebaeude", pj["gebaeude"], ObjectPlacement=self.platzierung(site.ObjectPlacement))
        gs = self.neu("IfcBuildingStorey", "/projekt/gebaeude/" + pj["geschoss"], pj["geschoss"],
                      ObjectPlacement=self.platzierung(geb.ObjectPlacement), Elevation=0.0)
        for eltern, kind in ((projekt, site), (site, geb), (geb, gs)):
            self.beziehung("IfcRelAggregates", self.pfade[eltern.id()] + "#aggregiert",
                           RelatingObject=eltern, RelatedObjects=[kind])

        # Wandtyp mit Schichtaufbau (IfcMaterialLayerSet)
        wtyp = self.neu("IfcWallType", "/typen/wand/" + w["typ"], w["typ"], "ELEMENTEDWALL")
        lset = ifcopenshell.api.material.add_material_set(f, name=w["typ"], set_type="IfcMaterialLayerSet")
        for s in w["schichten_innen_nach_aussen"]:
            if s["rolle"] == "gefach":
                st = w["staender"]
                lname = (f"Gefach: {self.p['materialien'][s['material']]['name']} {s['dicke']:g} mm "
                         f"zwischen {self.p['materialien'][st['material']]['name']} {st['breite']}/{st['tiefe']}, e = {st['raster']} mm")
            else:
                lname = f"{self.p['materialien'][s['material']]['name']} {s['dicke']:g} mm"
            layer = ifcopenshell.api.material.add_layer(f, layer_set=lset, material=self.material(s["material"]), name=lname)
            ifcopenshell.api.material.edit_layer(f, layer=layer, attributes={"LayerThickness": float(s["dicke"])})
        self.beziehung("IfcRelAssociatesMaterial", "/typen/wand/" + w["typ"] + "#material",
                       RelatingMaterial=lset, RelatedObjects=[wtyp])
        typen = [wtyp]  # werden am Ende per IfcRelDeclares am Projekt deklariert

        # Wand
        L, H = w["laenge"], w["hoehe"]
        wand = self.neu("IfcWall", "/wand", w["name"], "ELEMENTEDWALL", Tag=w["id"],
                        ObjectPlacement=self.platzierung(gs.ObjectPlacement))
        achse = f.createIfcPolyline([f.createIfcCartesianPoint([0.0, 0.0]), f.createIfcCartesianPoint([float(L), 0.0])])
        wand.Representation = self.form(axis, "Curve2D", [achse])
        self.beziehung("IfcRelContainedInSpatialStructure", self.pfade[gs.id()] + "#enthaelt",
                       RelatingStructure=gs, RelatedElements=[wand])
        self.beziehung("IfcRelDefinesByType", self.pfade[wtyp.id()] + "#typisiert",
                       RelatingType=wtyp, RelatedObjects=[wand])
        usage = f.createIfcMaterialLayerSetUsage(lset, "AXIS2", "POSITIVE", 0.0, None)
        self.beziehung("IfcRelAssociatesMaterial", "/wand#material", RelatingMaterial=usage, RelatedObjects=[wand])

        from b3_uwert_iso6946 import uwert_fuer_ifc
        u = uwert_fuer_ifc(self.p)
        self.pset(wand, "Pset_WallCommon", {"Reference": w["typ"], "IsExternal": bool(w["aussenwand"]),
                                            "LoadBearing": bool(w["tragend"]), "ThermalTransmittance": u})
        netto_m2 = lay["nettoflaeche_mm2"] / 1e6
        self.qto(wand, "Qto_WallBaseQuantities", {
            "Length": float(L), "Height": float(H), "Width": float(dicke_gesamt),
            "GrossSideArea": round(L * H / 1e6, 6), "NetSideArea": round(netto_m2, 6),
            "GrossVolume": round(L * H * dicke_gesamt / 1e9, 6), "NetVolume": round(netto_m2 * dicke_gesamt / 1e3, 6)})
        kl = w["klassifikation"]
        system = ifcopenshell.api.classification.add_classification(f, classification=kl["system"])
        system.Edition = kl["ausgabe"]
        ifcopenshell.api.classification.add_reference(f, products=[wand], identification=kl["code"], name=kl["bezeichnung"], classification=system)

        teile = []  # alle aggregierten Teile in fester Reihenfolge
        nach_material: dict[str, list] = {}

        def mat_zu(key, obj):
            nach_material.setdefault(key, []).append(obj)

        # Öffnungen (IfcOpeningElement, schneidet die Wand)
        for o in lay["oeffnungen"]:
            op = self.neu("IfcOpeningElement", o["pfad"], f"{o['art']} {o['id']}", "OPENING",
                          ObjectPlacement=self.platzierung(wand.ObjectPlacement, (o["x0"], 0.0, o["z0"])))
            op.Representation = self.form(body, "SweptSolid", [self.quader_entlang(o["x1"] - o["x0"], dicke_gesamt, o["z1"] - o["z0"], "z")])
            self.beziehung("IfcRelVoidsElement", o["pfad"] + "#schneidet", RelatingBuildingElement=wand, RelatedOpeningElement=op)

        # Hölzer (IfcMember)
        st = w["staender"]
        holz_obj = {}
        for h in lay["hoelzer"]:
            dx, dz = h["x1"] - h["x0"], h["z1"] - h["z0"]
            m = self.neu("IfcMember", h["pfad"], h["name"], h["typ"], ObjectType=h["rolle"],
                         ObjectPlacement=self.platzierung(wand.ObjectPlacement, (h["x0"], y_kern[0], h["z0"])))
            liegend = h["typ"] == "PLATE" or h["rolle"] == "Sturz"
            m.Representation = self.form(body, "SweptSolid", [self.quader_entlang(dx, st["tiefe"], dz, "x" if liegend else "z")])
            laenge = dx if liegend else dz
            quer = (dz if liegend else dx) * st["tiefe"]
            self.pset(m, "Pset_MemberCommon", {"LoadBearing": True})
            holz_obj[h["pfad"]] = (m, h, laenge, quer)
            mat_zu(st["material"], m)
            teile.append(m)

        # Kerven (IfcVoidingFeature NOTCH) – vor den Mengen, damit NetVolume stimmt
        abzug = {}
        for kv in w["kerven"]:
            pfad_st = f"/wand/staender/raster/{kv['staender_rasterindex']}"
            m, h, _, _ = holz_obj[pfad_st]
            vf = self.neu("IfcVoidingFeature", f"/wand/kerven/{kv['id']}", f"Kerve {kv['id']}", "NOTCH",
                          Description=kv.get("_zweck"),
                          ObjectPlacement=self.platzierung(m.ObjectPlacement, (-UEBERSTAND, -UEBERSTAND, kv["z"] - h["z0"])))
            # Der Abzugskörper steht seitlich und zur Raumseite um UEBERSTAND über
            # den Ständer hinaus: keine koplanaren Flächen → robuste Boolesche Operation.
            vf.Representation = self.form(body, "SweptSolid", [self.quader_entlang(
                h["x1"] - h["x0"] + 2 * UEBERSTAND, kv["tiefe"] + UEBERSTAND, kv["hoehe"], "z")])
            self.beziehung("IfcRelVoidsElement", f"/wand/kerven/{kv['id']}#schneidet", RelatingBuildingElement=m, RelatedOpeningElement=vf)
            abzug[pfad_st] = abzug.get(pfad_st, 0) + (h["x1"] - h["x0"]) * kv["tiefe"] * kv["hoehe"]

        for pfad, (m, h, laenge, quer) in holz_obj.items():
            brutto = laenge * quer
            self.qto(m, "Qto_MemberBaseQuantities", {
                "Length": float(laenge), "CrossSectionArea": round(quer / 1e6, 6),
                "GrossVolume": round(brutto / 1e9, 9), "NetVolume": round((brutto - abzug.get(pfad, 0)) / 1e9, 9)})

        # Schichten: Beplankung (IfcPlate), Folie, Gefachdämmung
        for s in w["schichten_innen_nach_aussen"]:
            y0, y1 = lage[s["id"]]
            mname = self.p["materialien"][s["material"]]["name"]
            if s["rolle"] == "beplankung":
                for pfad, poly in plattenteilung(w, s, lay["oeffnungen_union"]):
                    bx0, bz0, bx1, bz1 = poly.bounds
                    pl = self.neu("IfcPlate", pfad, f"{mname} {pfad.split('/platte/')[1]}", "SHEET", ObjectType="Beplankung",
                                  ObjectPlacement=self.platzierung(wand.ObjectPlacement, (bx0, y1, bz0)))
                    pl.Representation = self.form(body, "SweptSolid", [self.platte_solid(poly, bx0, bz0, s["dicke"])])
                    self.pset(pl, "Pset_PlateCommon", {"LoadBearing": s["id"] == "osb", "IsExternal": s["id"] == "hfd"})
                    self.qto(pl, "Qto_PlateBaseQuantities", {
                        "Width": float(s["dicke"]), "Perimeter": round(poly.length, 3),
                        "GrossArea": round((bx1 - bx0) * (bz1 - bz0) / 1e6, 6), "NetArea": round(poly.area / 1e6, 6),
                        "NetVolume": round(poly.area * s["dicke"] / 1e9, 9)})
                    mat_zu(s["material"], pl)
                    teile.append(pl)
            elif s["rolle"] == "folie":
                poly = kanonisch(box(0, 0, L, H).difference(lay["oeffnungen_union"]))
                if w["folie_als"] == "IfcCovering":
                    fo = self.neu("IfcCovering", "/wand/schichten/folie", mname, "MEMBRANE")
                else:
                    fo = self.neu("IfcBuildingElementPart", "/wand/schichten/folie", mname, "USERDEFINED", ObjectType="MEMBRANE")
                fo.ObjectPlacement = self.platzierung(wand.ObjectPlacement, (0.0, y1, 0.0))
                fo.Representation = self.form(body, "SweptSolid", [self.platte_solid(poly, 0.0, 0.0, s["dicke"])])
                self.pset(fo, "HRB_Feuchteschutz", {"Funktion": "Dampfbremse, luftdichte Ebene",
                                                     "SdWert_m": float(self.p["materialien"][s["material"]]["sd_m"])})
                mat_zu(s["material"], fo)
                teile.append(fo)
            elif s["rolle"] == "gefach":
                for poly in lay["gefache"]:
                    bx0, bz0, _, _ = poly.bounds
                    pfad = f"/wand/gefach/x{bx0:g}_z{bz0:g}"
                    d = self.neu("IfcBuildingElementPart", pfad, f"Gefachdämmung x={bx0:g} z={bz0:g}", "INSULATION",
                                 ObjectPlacement=self.platzierung(wand.ObjectPlacement, (bx0, y1, bz0)))
                    d.Representation = self.form(body, "SweptSolid", [self.platte_solid(poly, bx0, bz0, s["dicke"])])
                    self.qto(d, "Qto_BodyGeometryValidation", {"NetVolume": round(poly.area * s["dicke"] / 1e9, 9)})
                    mat_zu(s["material"], d)
                    teile.append(d)

        # Verbindungsmittel (IfcMechanicalFastener mit Typ)
        for vm in w["verbindungsmittel"]:
            ftyp = self.neu("IfcMechanicalFastenerType", f"/typen/verbindungsmittel/{vm['id']}", vm["typ_name"], vm["art"],
                            NominalDiameter=float(vm["durchmesser"]), NominalLength=float(vm["laenge"]))
            r = vm["durchmesser"] / 2
            kreis = f.createIfcCircleProfileDef("AREA", None, f.createIfcAxis2Placement2D(f.createIfcCartesianPoint([0.0, 0.0]), None), float(r))
            schaft = f.createIfcExtrudedAreaSolid(kreis, self.achse3d(z=(0, 1, 0), x=(1, 0, 0)), self.richtung(0, 0, 1), float(vm["laenge"]))
            rep = f.createIfcShapeRepresentation(body, "Body", "SweptSolid", [schaft])
            rmap = f.createIfcRepresentationMap(self.achse3d(), rep)
            ftyp.RepresentationMaps = [rmap]
            operator = f.createIfcCartesianTransformationOperator3D(None, None, self.punkt(0, 0, 0), None, None)
            self.beziehung("IfcRelAssociatesMaterial", f"/typen/verbindungsmittel/{vm['id']}#material",
                           RelatingMaterial=self.material("stahl_verzinkt"), RelatedObjects=[ftyp])
            typen.append(ftyp)

            y_kopf = lage[vm["schicht"]][0]  # Schraubenkopf auf der Raumseite der OSB
            osb_flaeche = unary_union([p for _, p in plattenteilung(w, next(s for s in w["schichten_innen_nach_aussen"] if s["id"] == vm["schicht"]), lay["oeffnungen_union"])])
            zulaessig = osb_flaeche.buffer(-10.0)  # 10 mm Mindestabstand zum Plattenrand/Ausschnitt
            schrauben = []
            for h in lay["hoelzer"]:
                if h["typ"] != "STUD" or h["rolle"] == "Sturz":
                    continue
                xc = (h["x0"] + h["x1"]) / 2
                z, i = h["z0"] + vm["randabstand"], 1
                while z <= h["z1"] - vm["randabstand"] + 1e-9:
                    if zulaessig.contains(Point(xc, z)):
                        sc = self.neu("IfcMechanicalFastener", f"/wand/verbindungsmittel/{vm['id']}{h['pfad'][5:]}/{i}",
                                      f"{vm['typ_name']} #{len(schrauben) + 1}", vm["art"],
                                      ObjectPlacement=self.platzierung(wand.ObjectPlacement, (xc, y_kopf, z)))
                        # NominalDiameter/NominalLength stehen am Typ UND redundant am
                        # Exemplar: IDS 1.0 vererbt Attribute (anders als Properties)
                        # nicht vom Typ, eine Prüfung "jede Schraube hat einen
                        # Durchmesser" schlüge sonst fehl (siehe B2).
                        sc.NominalDiameter = float(vm["durchmesser"])
                        sc.NominalLength = float(vm["laenge"])
                        # Geometrie als Verweis auf die Typ-Geometrie (IfcMappedItem)
                        sc.Representation = self.form(body, "MappedRepresentation", [f.createIfcMappedItem(rmap, operator)])
                        schrauben.append(sc)
                        i += 1
                    z += vm["abstand"]
            self.beziehung("IfcRelDefinesByType", f"/typen/verbindungsmittel/{vm['id']}#typisiert",
                           RelatingType=ftyp, RelatedObjects=schrauben)
            teile.extend(schrauben)

        # Materialzuordnung (eine Beziehung je Material, feste Reihenfolge)
        for key in sorted(nach_material):
            self.beziehung("IfcRelAssociatesMaterial", f"/materialien/{key}#zuordnung",
                           RelatingMaterial=self.material(key), RelatedObjects=nach_material[key])
        self.beziehung("IfcRelAggregates", "/wand#aggregiert", RelatingObject=wand, RelatedObjects=teile)
        self.beziehung("IfcRelDeclares", "/projekt#deklariert", RelatingContext=projekt, RelatedDefinitions=typen)

        self._setze_guids()
        self._setze_header()
        return f

    # --- Determinismus ----------------------------------------------------
    def _pfad(self, ent) -> str:
        if ent.id() in self.pfade:
            return self.pfade[ent.id()]
        k = ent.is_a()
        if k == "IfcRelAggregates":
            return self._pfad(ent.RelatingObject) + "#aggregiert"
        if k == "IfcRelContainedInSpatialStructure":
            return self._pfad(ent.RelatingStructure) + "#enthaelt"
        if k == "IfcRelDefinesByType":
            return self._pfad(ent.RelatingType) + "#typisiert"
        if k == "IfcRelVoidsElement":
            return self._pfad(ent.RelatedOpeningElement) + "#schneidet"
        if k == "IfcRelDefinesByProperties":
            return self._pfad(ent.RelatingPropertyDefinition) + "#zuordnung"
        if k in ("IfcPropertySet", "IfcElementQuantity"):
            if ent.DefinesOccurrence:
                return self._pfad(ent.DefinesOccurrence[0].RelatedObjects[0]) + "#" + ent.Name
            if ent.DefinesType:
                return self._pfad(ent.DefinesType[0]) + "#" + ent.Name
        if k == "IfcRelAssociatesMaterial":
            m = ent.RelatingMaterial
            name = getattr(m, "Name", None) or getattr(m, "LayerSetName", None) or (m.ForLayerSet.LayerSetName if m.is_a("IfcMaterialLayerSetUsage") else m.is_a())
            return f"material:{m.is_a()}:{name}#" + self._pfad(ent.RelatedObjects[0])
        if k == "IfcRelAssociatesClassification":
            k2 = ent.RelatingClassification
            kenn = k2.Identification if k2.is_a("IfcClassificationReference") else k2.Name
            return f"klassifikation:{k2.is_a()}:{kenn}#" + self._pfad(ent.RelatedObjects[0])
        if k == "IfcRelDeclares":
            return self._pfad(ent.RelatingContext) + "#deklariert"
        raise KeyError(f"Kein Pfad für {ent}")

    def _setze_guids(self):
        gesehen = {}
        for ent in self.f.by_type("IfcRoot"):
            pfad = self._pfad(ent)
            if pfad in gesehen:
                raise ValueError(f"Pfad doppelt: {pfad}")
            gesehen[pfad] = ent
            ent.GlobalId = ifcopenshell.guid.compress(uuid.uuid5(GUID_NAMENSRAUM, pfad).hex)

    def _setze_header(self):
        pj = self.p["projekt"]
        h = self.f.header
        h.file_description.description = ("ViewDefinition [NotAssigned]",)
        h.file_name.name = "wandelement.ifc"
        h.file_name.time_stamp = pj["zeitstempel"]
        h.file_name.author = (pj["autor"],)
        h.file_name.organization = (pj["organisation"],)
        h.file_name.authorization = "keine"


def lade_parameter(pfad: Path | str = STANDARD_PARAMETER) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def erzeuge_ifc(param: dict) -> ifcopenshell.file:
    return IfcWandBauer(param).baue()


def schreibe_ifc(param: dict, ausgabe: Path | str = STANDARD_AUSGABE) -> Path:
    ausgabe = Path(ausgabe)
    ausgabe.parent.mkdir(parents=True, exist_ok=True)
    erzeuge_ifc(param).write(str(ausgabe))
    return ausgabe


def kennzahlen(pfad: Path | str) -> dict:
    """Kennzahlen einer erzeugten Datei (für ergebnisse.md)."""
    import hashlib
    from collections import Counter

    pfad = Path(pfad)
    f = ifcopenshell.open(str(pfad))
    zaehl = Counter(e.is_a() for e in f)
    klassen = ["IfcWall", "IfcMember", "IfcPlate", "IfcBuildingElementPart", "IfcCovering", "IfcMechanicalFastener",
               "IfcVoidingFeature", "IfcOpeningElement", "IfcRelAggregates", "IfcPropertySet", "IfcElementQuantity"]
    members = f.by_type("IfcMember")
    return {
        "datei": pfad.name,
        "schema": f.schema_identifier,
        "groesse_bytes": pfad.stat().st_size,
        "sha256": hashlib.sha256(pfad.read_bytes()).hexdigest(),
        "entitaeten_gesamt": len(list(f)),
        "ifcroot": len(f.by_type("IfcRoot")),
        "je_klasse": {k: zaehl.get(k, 0) for k in klassen},
        "member_stud": sum(1 for m in members if m.PredefinedType == "STUD"),
        "member_plate": sum(1 for m in members if m.PredefinedType == "PLATE"),
    }


def main() -> None:
    ap = argparse.ArgumentParser(description="B1 – Holzrahmen-Wandelement nach IFC4X3_ADD2")
    ap.add_argument("--parameter", default=str(STANDARD_PARAMETER))
    ap.add_argument("--ausgabe", default=str(STANDARD_AUSGABE))
    args = ap.parse_args()
    pfad = schreibe_ifc(lade_parameter(args.parameter), args.ausgabe)
    kz = kennzahlen(pfad)
    print(json.dumps(kz, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

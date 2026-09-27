#!/usr/bin/env python3
"""
B2 – IDS-Prüfung (IDS 1.0) der in B1 erzeugten IFC-Datei mit ifctester.

Eingabe:  holzrahmenbau.ids, ausgabe/wandelement.ifc (wird bei Bedarf mit B1 erzeugt)
Ausgabe:  ausgabe/ids_bericht_<fall>.json | .html | .md
          ausgabe/wandelement_fehlerhaft.ifc

Zwei Fälle:
  1. "bestanden":   die unveränderte Datei aus B1.
  2. "fehlerhaft":  dieselbe Datei mit absichtlich eingebauten Fehlern
     (jeder Fehler zielt auf genau eine Spezifikation):
       F1  U-Wert der Außenwand auf 0,25 W/(m²K) gesetzt           → HRB-01
       F2  Klassifikationsbezug der Wand entfernt                   → HRB-03
       F3  Material eines Ständers entfernt                         → HRB-05
       F4  NominalDiameter am Verbindungsmitteltyp gelöscht         → HRB-08
       F5  NominalDiameter einer Schraube auf 20 mm gesetzt         → HRB-09
       F6  ein IfcBuildingElementProxy ergänzt                      → HRB-11

Aufruf:   python b2_ids_pruefung.py
"""
from __future__ import annotations

import json
from pathlib import Path

import ifcopenshell
import ifcopenshell.api.root
import ifcopenshell.guid
from ifctester import ids, reporter

HIER = Path(__file__).resolve().parent
IDS_DATEI = HIER / "holzrahmenbau.ids"
IFC_DATEI = HIER / "ausgabe" / "wandelement.ifc"
AUSGABE = HIER / "ausgabe"

# ifctester 0.8.5 liest das IDS-Attribut "identifier" nicht ein (bleibt None);
# die ID wird daher ersatzweise aus dem Namensanfang "HRB-xx" gelesen.
ERWARTET_FEHLERHAFT = {"HRB-01", "HRB-03", "HRB-05", "HRB-08", "HRB-09", "HRB-11"}


def stelle_ifc_sicher() -> Path:
    if not IFC_DATEI.exists():
        import b1_wandelement
        b1_wandelement.schreibe_ifc(b1_wandelement.lade_parameter(), IFC_DATEI)
    return IFC_DATEI


def baue_fehlerhaft(quelle: Path, ziel: Path) -> list[str]:
    """Erzeugt die fehlerhafte Variante. Rückgabe: Liste der Änderungen."""
    f = ifcopenshell.open(str(quelle))
    log = []
    wand = f.by_type("IfcWall")[0]

    # F1: U-Wert zu hoch
    for rel in wand.IsDefinedBy:
        ps = rel.RelatingPropertyDefinition
        if ps.is_a("IfcPropertySet") and ps.Name == "Pset_WallCommon":
            for p in ps.HasProperties:
                if p.Name == "ThermalTransmittance":
                    p.NominalValue = f.createIfcThermalTransmittanceMeasure(0.25)
    log.append("F1 Pset_WallCommon.ThermalTransmittance = 0.25")

    # F2: Klassifikationsbezug entfernen
    for rel in list(wand.HasAssociations):
        if rel.is_a("IfcRelAssociatesClassification"):
            f.remove(rel)
    log.append("F2 IfcRelAssociatesClassification der Wand entfernt")

    # F3: Material eines Ständers entfernen
    staender = next(m for m in f.by_type("IfcMember") if m.Name == "Ständer R2")
    for rel in staender.HasAssociations:
        if rel.is_a("IfcRelAssociatesMaterial"):
            rel.RelatedObjects = [o for o in rel.RelatedObjects if o != staender]
    log.append("F3 Materialzuordnung von 'Ständer R2' entfernt")

    # F4: Typ ohne Nenndurchmesser
    typ = f.by_type("IfcMechanicalFastenerType")[0]
    typ.NominalDiameter = None
    log.append(f"F4 {typ.Name}: NominalDiameter gelöscht")

    # F5: Schraube mit unplausiblem Durchmesser
    sc = f.by_type("IfcMechanicalFastener")[0]
    sc.NominalDiameter = 20.0
    log.append(f"F5 {sc.Name}: NominalDiameter = 20 mm")

    # F6: Proxy-Element
    proxy = ifcopenshell.api.root.create_entity(f, ifc_class="IfcBuildingElementProxy", name="Unbekanntes Bauteil")
    proxy.GlobalId = ifcopenshell.guid.compress("00000000000000000000000000000001")
    log.append("F6 IfcBuildingElementProxy ergänzt")

    f.write(str(ziel))
    return log


def pruefe(ifc_pfad: Path, fall: str) -> dict:
    """IDS laden (mit XSD-Validierung), IFC prüfen, Berichte schreiben."""
    spez = ids.open(str(IDS_DATEI), validate=True)
    modell = ifcopenshell.open(str(ifc_pfad))
    spez.validate(modell)

    rj = reporter.Json(spez)
    rj.report()
    rj.to_file(str(AUSGABE / f"ids_bericht_{fall}.json"))
    rh = reporter.Html(spez)
    rh.report()
    rh.to_file(str(AUSGABE / f"ids_bericht_{fall}.html"))

    zusammenfassung = []
    for s in spez.specifications:
        anwendbar = len(s.applicable_entities)
        fehler = len(s.failed_entities)
        zusammenfassung.append({
            "id": s.identifier or s.name.split(" ")[0], "name": s.name, "status": bool(s.status),
            "anwendbar": anwendbar, "fehlerhaft": fehler,
        })
    ergebnis = {"fall": fall, "datei": ifc_pfad.name,
                "bestanden": all(z["status"] for z in zusammenfassung),
                "spezifikationen": zusammenfassung,
                "fehlgeschlagen": [z["id"] for z in zusammenfassung if not z["status"]]}
    schreibe_markdown(ergebnis, rj.results, AUSGABE / f"ids_bericht_{fall}.md")
    return ergebnis


def schreibe_markdown(erg: dict, json_ergebnis: dict, pfad: Path) -> None:
    z = [f"# IDS-Prüfbericht: {erg['datei']} (Fall: {erg['fall']})", "",
         f"IDS: `{IDS_DATEI.name}` · Ergebnis: **{'bestanden' if erg['bestanden'] else 'nicht bestanden'}**", "",
         "| ID | Spezifikation | anwendbar | fehlerhaft | Status |", "|---|---|---:|---:|---|"]
    for s in erg["spezifikationen"]:
        z.append(f"| {s['id']} | {s['name']} | {s['anwendbar']} | {s['fehlerhaft']} | {'✔' if s['status'] else '✘'} |")
    # Details der Fehler aus dem JSON-Bericht von ifctester
    details = []
    for spec in json_ergebnis.get("specifications", []):
        for req in spec.get("requirements", []):
            for fe in req.get("failed_entities", [])[:3]:
                details.append(f"- {spec['name'].split(' ')[0]}: {fe.get('class')} „{fe.get('name')}“ – {fe.get('reason')}")
        if spec.get("status") is False and not spec.get("requirements") or \
                (spec.get("status") is False and all(not r.get("failed_entities") for r in spec.get("requirements", []))):
            details.append(f"- {spec['name'].split(' ')[0]}: {spec.get('description')} (Anwendbarkeit verletzt: "
                           f"{spec.get('total_applicable')} Elemente gefunden)")
    if details:
        z += ["", "## Fehlerdetails (max. 3 je Anforderung)", ""] + details
    pfad.write_text("\n".join(z) + "\n", encoding="utf-8")


def main() -> None:
    AUSGABE.mkdir(exist_ok=True)
    ok = pruefe(stelle_ifc_sicher(), "bestanden")
    ziel = AUSGABE / "wandelement_fehlerhaft.ifc"
    aenderungen = baue_fehlerhaft(IFC_DATEI, ziel)
    nok = pruefe(ziel, "fehlerhaft")
    print(json.dumps({"bestanden": ok, "fehlerhaft": nok, "eingebaute_fehler": aenderungen}, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()

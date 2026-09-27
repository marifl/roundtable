# Recherche 01: IFC-Holzbau, BTLx, Fertigungsformate

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft oder selbst getestet, **[U]** = unsicher.

## Ergebnis in 5 Punkten

1. **Eine Design Transfer View für IFC 4.3 gibt es nicht.** Offiziell sind nur die Reference View und die Alignment-based View. Deshalb: Schema IFC4X3_ADD2 (ISO 16739-1:2024), eigene Anforderungen als IDS, Prüfung mit dem buildingSMART Validation Service.
2. **Das Wandelement ist in 4.3 `IfcWall` + `IfcRelAggregates`, nicht `IfcElementAssembly`.** Dazu kommen immer `IfcMaterialLayerSetUsage`, denn viele Programme lesen nur die Schichten.
3. **Weinmann-Wandanlagen lesen WUP, nicht BTLx.** WUP ist proprietär. Ein WUP-Writer ist Pflicht, die Spezifikation muss bei Homag angefragt werden.
4. **compas_timber + timber_design (MIT)** liefern Ständerraster, Verbindungen und BTLx, aber kein IFC. Das IFC-Mapping bauen wir selbst mit IfcOpenShell.
5. **dataholz.eu liefert Schichtaufbauten (IFC nach Registrierung, IDS, bSDD), keine Ständer.** Die Daten sind urheberrechtlich geschützt, deshalb eine Lizenz anfragen.

## Korrekturen am Konzept

1. **„IFC 4.3 DTV“ streichen.** Die DTV wurde für 4.3 nie veröffentlicht, und für IFC4 ist sie nur ein Draft (DTV 1.1) [V].
   - Quellen:
     - ifc43-docs.standards.buildingsmart.org (Introduction)
     - buildingSMART-Forum „Official MVDs for IFC 4.3“
     - MVD-Policy 2021
     - MVD-Database technical.buildingsmart.org
2. **Schema-Wahl:** IFC4X3_ADD2 als Standardausgabe, den Generator schema-agnostisch bauen, IFC4 als Fallback. IFC4 hat derzeit die breitere Unterstützung in Software [V].
3. In IFC4X3 ist `IfcWallElementedCase` entfallen, und `IfcBuildingElement` heißt jetzt `IfcBuiltElement` [V].
4. **Maschinenformat:** Nicht „BTL oder BTLx“, sondern:
   - BTLx für Abbund
   - **WUP** für Weinmann-Wandanlagen
   - ggf. BVX für Hundegger (ob Cambium BTLx liest, ist [U])
5. **dataholz:** „fast 1.500 Aufbauten“ ist ungenau. Belegt sind etwa 1.500 Konstruktionen **und Anschlüsse** [V/U]. Der IFC-Download braucht eine Registrierung. Die Nutzung in Deutschland regeln eigene Nutzungsbedingungen.

## Klassen-Mapping Holzrahmenwand (geprüft an IFC 4.3 und IfcOpenShell 0.8.5)

| Bauteil | IFC-Klasse | PredefinedType | Status |
|---|---|---|---|
| Wandelement | `IfcWall` + `IfcRelAggregates` + `IfcMaterialLayerSetUsage` | – | [V] |
| Ständer | `IfcMember` | STUD | [V] |
| Schwelle / Rähm | `IfcMember` | PLATE | [V] |
| Beplankung (OSB, GK, GF) | `IfcPlate` | SHEET | [V] Enum, Zuordnung ist Konvention |
| Gefachdämmung | `IfcBuildingElementPart` | INSULATION („infill in stud walls“) | [V] |
| Folie / Dampfbremse | `IfcBuildingElementPart` (konsistenter) oder `IfcCovering` MEMBRANE | – | [U] Konvention |
| Kerve, Bohrung, Fase | `IfcVoidingFeature` + `IfcRelVoidsElement` | NOTCH, HOLE, CHAMFER, MITER, CUTOUT | [V] selbst getestet: wird volumengenau abgezogen |
| Schraube, Nagel, Klammer | `IfcMechanicalFastener` (+ Type mit NominalDiameter, NominalLength) | SCREW, NAIL, STAPLE | [V] |
| Nagel- und Klammerbild | `IfcRepresentationMap` + `IfcMappedItem` am Typ | – | [U] Designentscheidung |
| Energie-Raumbegrenzung | `IfcRelSpaceBoundary2ndLevel` | – | [V], optional für Energie |

- **Praxis-Warnung** [V]: Das dataholz-Projekt TIMBIM hat die Schichtaggregation in `IfcWall` wieder verworfen, weil Autorensoftware sie nicht umsetzt. **Deshalb beides liefern: Layer-Set und Aggregation.**

## Bausteine

| Baustein | Liefert | Lizenz | Urteil |
|---|---|---|---|
| **IfcOpenShell 0.8.5** | `ifcopenshell.api`: aggregate, nest, feature, material, type, geometry, boundary. Kein Framing-Werkzeug | LGPL-3.0+ [V] | **übernehmen** als IFC-Kern |
| **compas_timber 2.2.0** github.com/gramaziokohler/compas_timber | Beam/Plate/Panel, ca. 28 Verbindungstypen, 18 BTLx-Bearbeitungen, BTLx lesen und schreiben. Kein IFC | MIT, Beta [V] | **adaptieren** |
| **timber_design 0.3.1** github.com/gramaziokohler/timber_design | `wall_populator.py`: Ständer, King- und Jack-Studs, Sturz, Brüstung, Rähm/Schwelle, Öffnungen. PanelPopulator als offenes PR | MIT, Beta [V] | **adaptieren** |
| **BTLx 2.3** design2machine.com | XSD + PDF frei; 2.3 mit Nagel-, Schrauben- und Klammerattributen und Abschnitt „Prefabrication“; 2.4 Beta seit 08/2026 | Lizenz nicht ausgewiesen [U] | **übernehmen**, Lizenz klären |
| btlx-parser (JAIKIN) | nur BTLx lesen | MIT [V] | Referenz |
| **WUP (Weinmann)** | Format der Wandanlagen (WALLTEQ, wupWorks); wupViewer kostenlos | proprietär [V] | **selbst bauen**, Spezifikation bei Homag anfragen |
| **dataholz.eu** | Layer-IFC (IfcWall/IfcSlab), IDS aller Aufbauten (seit 11/2025), bSDD „dataholz 1.5“ | geschützt, keine API [V] | adaptieren über IDS/bSDD, Lizenz anfragen |
| **lignumdata.ch** | öffentliche API v1.2.1, IFC4 LOD300 + XLSX je Bauteil, Schweizer Nachweise | [U] | adaptieren als Schichtdatenquelle |

## Verbindungsmittel als BIM-Daten [V]

| Hersteller | Formate | Hinweis |
|---|---|---|
| Rothoblaas | IFC, RFA, Bibliotheken für cadwork, Dietrich's, hsbcad | – |
| Würth | IFC, RFA | ASSY nach ETA-11/0190 |
| Simpson Strong-Tie | IFC (voll/vereinfacht), RFA, XML | – |
| SPAX | über CADENAS, parametrische Attribute | **CC BY-ND 4.0** |
| SFS, HECO | über CADENAS/3Dfindit | ETA nur als PDF |

**Urteil:** Eine eigene Tabelle (Typ, Durchmesser, Länge, ETA) anlegen. Hersteller-IFC nur zur Visualisierung nutzen.

## Leitfäden

- Einen bSI-Implementierungsleitfaden für Holzbau gibt es nicht [V].
- **buildingSMART Deutschland, Fachgruppe „BIM im Holzbau“:** LP5, IFC-Mapping, IDS-Prüfregeln, in Arbeit (buildingsmart.de/node/208) [V].
- **BIMwood** (TUM/HSLU): How-To und Referenzprozess [V].
- **Bauen digital Schweiz:** „Projektabwicklung mit BIM im Holzbau“ [V].

## Kommerzielle Referenzen (Gegenprobe beim Import)

- cadwork: BTL/BTLx, BVN/BVX
- Dietrich's: WUP, BTL, BTLx
- hsbcad
- AGACAD Wood Framing (WUP-Export)
- ArchiFrame: BVN, BTL, WUP, Randek

Ausgereifte Open-Source-Framing-Generatoren mit IFC gibt es nicht [V].

## Selbst zu bauen

1. JSON → IFC-Mapping nach der Tabelle oben
2. IDS-Profil „Holzrahmenbau“ statt DTV
3. WUP-Writer für Weinmann
4. Logik für Nagel- und Klammerbilder

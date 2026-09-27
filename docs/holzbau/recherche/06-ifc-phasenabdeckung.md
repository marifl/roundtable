# Recherche 06: Kann IFC 4.3 die ganze Kette „Idea to Factory“ tragen?

Stand: 27.09.2026. **[V]** = an Primärquelle oder maschinell am Schema IFC4X3_ADD2 geprüft (IfcOpenShell 0.8.5), **[U]** = unsicher oder eigene Bewertung.

## Ergebnis in 5 Punkten

1. **Schemakonform ja, fast jede Phase.** IFC 4.3 ADD2 (= ISO 16739-1:2024) hat Entitäten für Kosten, Freigaben, Genehmigung, Bemusterung, Fertigungsteile, 4D und Betrieb [V].
2. **Kein offizielles MVD deckt das ab.** „Konform“ heißt deshalb: schemavalide, normative Regeln des Validation Service erfüllt, dazu eigene IDS [V].
3. **Varianten und Versionen gehören nicht in die Datei.** Pro Datei ist nur ein IfcProject erlaubt, und IfcOwnerHistory speichert nur die letzte Änderung. Versionen verwaltet eine CDE nach ISO 19650 [V].
4. **Die Software hinkt hinterher.** hsbcad und cadwork exportieren nur bis IFC4, Archicad bietet kein IFC 4.3, Allplan schon [V]. Deshalb schema-agnostisch generieren und bei Bedarf IFC4 ableiten.
5. **Einen Hersteller, der „ein IFC von Entwurf bis Fertigung“ lebt, habe ich nicht gefunden** [U]. BIMwood arbeitet mit Modellen und verknüpften Dokumenten. Genau das ist die Lücke dieser Arbeit.

## Phase → IFC-Mechanismus → Grenze und Lösung

| Phase | IFC-4.3-Mechanismus [V] | Grenze / standardkonforme Lösung |
|---|---|---|
| Entwurf, Varianten | IfcProject, IfcOwnerHistory, IfcGroup | höchstens 1 IfcProject pro Datei (Regel `IfcSingleProjectInstance`), OwnerHistory nur mit letzter Änderung. **Varianten als Revisionen in der CDE**, nur die gewählte kommt ins Hauptmodell |
| Angebot, Kosten | IfcCostSchedule (ESTIMATE, TENDER, PRICEDBILLOFQUANTITIES …), IfcCostItem, IfcCostValue mit **ApplicableDate/FixedUntilDate**, IfcRelAssignsToControl, DIN 276 als IfcClassification | Preise mit Gültigkeit **sind** abbildbar (Korrektur am Zielbild). Kaum eine Software liest das. GAEB DA XML 3.3 bzw. BIM-LV-Container nach DIN 18290-2:2023 als Export |
| Vertrag, Baubeschreibung | IfcProjectOrder (CHANGEORDER …), IfcApproval + IfcRelAssociatesApproval, IfcDocumentReference/-Information (ValidFrom/Until, Revision) | keine Vertragsentität und keine Signatur. Signiertes PDF per IfcDocumentReference einbinden, Hash als eigene Property [U] |
| Bemusterung | IfcElementType + Pset_ManufacturerTypeInformation (GTIN, ArticleNumber), IfcProjectLibrary + IfcRelDeclares, bSDD-URI in IfcClassificationReference | Optionen als nicht zugeordnete Typen in der Projektbibliothek. Die Wahl ist ein IfcRelDefinesByType. Ein eigenes Konzept „Option“ fehlt [U] |
| Bauantrag | IfcPermit (BUILDING), IfcActor/IfcActorRole, IfcSite.LandTitleNumber, IfcMapConversion + IfcProjectedCRS (EPSG:25832), IfcSpatialZone, Pset_SiteCommon | „Entwurfsverfasser“ nur als USERDEFINED-Rolle. Gemarkung, Flur und mehrere Flurstücke brauchen ein eigenes Pset. Pset_SiteCommon-Kennzahlen **≠ GRZ/GFZ nach BauNVO**. Abstandsflächen haben keine eigene Semantik |
| Statik | IfcStructuralAnalysisModel, IfcStructuralMember, Lasten | Holzbau-Statiksoftware liest das kaum [U]. Geometrie und Material übergeben, Ergebnis als Dokument |
| Energie | IfcRelSpaceBoundary2ndLevel, ThermalTransmittance in Pset_*Common, Pset_MaterialThermal, IfcSpatialZone THERMAL | Import in Software für DIN V 18599 ungeprüft [U]; Nachweis als Dokument referenzieren |
| Werkplanung, Fertigung | IfcWall (ELEMENTEDWALL) + IfcRelAggregates → IfcMember STUD/PLATE, IfcPlate SHEET, IfcBuildingElementPart INSULATION, IfcMechanicalFastener, IfcVoidingFeature; Pset_ManufacturerOccurrence (SerialNumber, BarCode, BatchReference), Pset_MaterialWood, Pset_Tolerance | **Maschinendaten gibt es in IFC nicht**, deshalb BTLx/WUP als Export. Das Aggregat hat keine eigene Body-Geometrie. Für Beton gibt es das MVD „IFC4Precast“, für Holz nichts Vergleichbares |
| Logistik, Montage | IfcWorkSchedule, IfcTask (LOGISTIC, MOVE, INSTALLATION), IfcTaskTime, IfcRelSequence, Pset_PackingInstructions, **IfcVehicle** | **IfcTransportElement ist Kran/Aufzug, nicht LKW** (Korrektur). Tourenplanung im ERP/TMS |
| Übergabe, Betrieb | IfcAsset, IfcTask MAINTENANCE, Pset_Warranty, Pset_ServiceLife | COBie V3 mappt auf IFC 4.3, ist aber US-Standard |
| Firmenregeln | IfcConstraint/IfcObjective/IfcMetric, IfcProjectLibrary | Software wertet IfcConstraint kaum aus. **Katalog als IfcProjectLibrary, Merkmalsregeln als IDS daneben, geometrische Regeln in eigener Regelmaschine, Ergebnisse als BCF** |

## Standardstatus [V]

- **IFC 4.3.2.0 (ADD2) = ISO 16739-1:2024**, Status Official. IFC4 ADD2 TC1 (ISO 16739-1:2018) ist ebenfalls noch Official, IFC 4.4 ist in Arbeit.
- **MVDs für 4.3:** nur Reference View und Alignment-based View. Die DTV wurde nie veröffentlicht; die Reference View ist laut Doku „not a full exchange of the design intent“.
- **IFCX (IFC5):**
  - Alpha-Stand.
  - Am 26.08.2026 hat der Projektplan die nächste Genehmigungsphase bestanden; kein Release-Termin.
  - **Nicht warten.** Stabile GlobalIds, bSDD-URIs und IDS erleichtern eine spätere Migration [U].
- **Validation Service** (validate.buildingsmart.org, Code: github.com/buildingSMART/validate):
  - Er prüft Syntax, Schema samt Where-Rules, normative Regeln, Industry Practices (als Warnung) und bSDD.
  - **Projekt- und Firmenregeln prüft er nicht.** Dafür ist IDS da.
- **IDS 1.0** ist seit Juni 2024 final; `IFC4X3_ADD2` ist zulässig.

## „Keine Abweichung vom Standard“: technische Absicherung [U, abgeleitet]

1. Nur `FILE_SCHEMA(('IFC4X3_ADD2'))` schreiben, bei Bedarf einen IFC4-Export ableiten.
2. Keine `IfcBuildingElementProxy`. PredefinedType immer setzen, sonst USERDEFINED mit ObjectType.
3. Eigene Daten nur in eigenen Psets ohne das Präfix „Pset_“, das dem Standard vorbehalten ist. Dazu bSDD-Klassen.
4. Jede Revision automatisch mit dem Validation Service bzw. dessen Open-Source-Regeln prüfen.
5. Bei jedem Freigabe-Gate eine IDS-Prüfung.

## Bauantrag

- **Modellierungsrichtlinie BIM-basierter Bauantrag** (BIM Deutschland 2020) [V]:
  - IFC4 ADD2 TC1 + Reference View 1.2, mvdXML, eigene Psets („BauantragAllgemein“, XBau-Codelisten), Georeferenz.
  - https://www.bimdeutschland.de/fileadmin/media/Downloads/Download-Liste/BIM-basierter_Bauantrag/20_2_Modellierungsrichtlinie_2020-08-18.pdf
- **NRW-Abschlussbericht** (23.04.2026) [V]:
  - Empfiehlt eine formale Vorprüfung per **IDS** und öffentliche IDS-Dateien. Eine neue Richtlinie ist für Mitte 2026 angekündigt.
  - https://www.mhkbd.nrw/system/files/media/document/file/2026-04-23_abschlussbericht_machbarkeitsstudie_pilotprojekte_nrw.pdf
  - https://bimbauantrag.nrw/
- **XBau 2.3.1:** Ein BIM-Modell soll „perspektivisch“ übermittelt werden. XBau bleibt ein abgeleiteter Export [V].
- **Ein bundesweites IDS für den Bauantrag** habe ich nicht gefunden [U].

## Praxisprojekte

| Projekt | Befund | Quelle |
|---|---|---|
| BIMwood (TUM, FNR 2019–2023) | Referenzprozess, Merkmallisten, Bauteilkatalog als verlinkte Daten, **kein Ein-Datei-Ansatz** [V] | https://mediatum.ub.tum.de/1732213 (DOI 10.14459/2024md1732213); https://www.fnr.de/fileadmin/projektdatenbank/22031118.pdf |
| BIMwood CH (HSLU) | „Mit dem IFC-Datenschema ist es nicht möglich, Komponenten zu parametrisieren“ [V] | https://bimwood.info/wp-content/uploads/2022/07/BIMwood_How-To_Abschlussbericht.pdf |
| bSD Fachgruppe Holzbau | Anwendungsfall „Modelldatenaustausch holzbaurelevante Ausführungsplanung“, Prüfregeln als IDS, Stand H1/2026 [V] | https://www.buildingsmart.de/node/208 |
| Sys.Wood (Holzcluster Steiermark 2026) | empfiehlt IFC 4.3.2.0, in der Praxis ist zu 56 % IFC4 im Einsatz; es fehlen Fertigungsmerkmale [V] | https://www.holzcluster-steiermark.at/wp-content/uploads/2026/02/SysWood_Planungsmethoden.pdf |
| TUM-Paper Akustik-IFC | Modellierungsregeln für Holzrahmenwände; Knotenpunkte lassen sich nicht standardkonform abbilden [V] | https://mediatum.ub.tum.de/doc/1688601/1688601.pdf |
| leanWOOD | Baufritz arbeitet mit Closed BIM [V] | – |

## Was IFC nicht abdeckt, und wie man es standardkonform löst

1. **Maschinendaten:** BTLx/WUP als Export, rückverfolgbar über GlobalId und Tag.
2. **Vertrag und Signatur:** signiertes PDF über IfcDocumentReference, Status über IfcApproval.
3. **Varianten und Historie:** CDE nach ISO 19650.
4. **Ausschreibung:** GAEB bzw. DIN-18290-Container.
5. **Behördenverfahren:** XBau mit IFC als Anlage, ggf. als IFC4-Export.
6. **Geometrische Firmenregeln:** eigene Regelprüfung, Ergebnisse als BCF.
7. **Knotenpunkte, Schall- und Brandschutzdetails:** eigene Psets plus Dokumente, kein Eingriff ins Schema.

## Folge für das Zielbild

„Eine Datei“ wird präzisiert: Pro freigegebenem Projektstand gibt es **ein** IFC als Wahrheit. Daneben stehen drei Dinge:

- **Versionen** in einer CDE
- **Regeln** als IDS und bSDD
- **abgeleitete Exporte** (BTLx, WUP, GAEB, XBau, PDF)

Nichts davon wird von Hand bearbeitet, und jeder Export ist über GlobalIds zum IFC zurückverfolgbar.

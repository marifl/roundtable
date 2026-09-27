# 8 Informationsmodell

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle oder maschinell am Schema IFC4X3_ADD2 geprüft) oder [U] (unsicher oder eigene Bewertung). Alle Zahlen zu Beispielen stammen aus den Dateien in `beispiele/ausgabe/` und wurden am 27.09.2026 mit IfcOpenShell 0.8.5 nachgezählt.

## 8.0 Einordnung und Vorgehen

Dieses Kapitel beantwortet die Forschungsfrage FF1 im Entwurf: Lässt sich die Informationskette eines Holzrahmenbau-Fertighauses standardkonform in einem IFC-4.3-Modell abbilden, wo liegen die Grenzen, und wie werden sie ohne proprietäre Erweiterung überbrückt? Es konkretisiert die Teilbeiträge B1 und B2 aus Abschnitt 5.8.3 und adressiert die Lücken L4 (Holzrahmenbau-Semantik in IFC 4.3 ist nicht beschrieben) und L5 (Validierung eines generierten IFC ist methodisch nicht beschrieben).

Kapitel 5 hat gezeigt, dass die Gegenbefunde zu einem durchgängigen IFC vor allem *Autorenwerkzeuge* betreffen [@orozco2023codesign; @geier2022bimwood; @timbim2024]. Die Arbeit verfolgt einen anderen Weg: Das Modell wird aus einem Parametermodell regelbasiert **erzeugt**, nicht von Hand gebaut und zwischen Programmen ausgetauscht. Die Parametrik liegt im Generator, das IFC ist ihr Ergebnis. Daraus folgen zwei Pflichten. Der Generator muss seine Konformität selbst nachweisen, und jede Designentscheidung am Schema muss begründet und prüfbar sein.

**Vorgehen.** Jede Abbildung in diesem Kapitel ist an mindestens einer der drei folgenden Stellen belegt:

1. an der Schemadefinition IFC4X3_ADD2, maschinell über IfcOpenShell 0.8.5 abgefragt,
2. an einem lauffähigen Beispiel aus `beispiele/` (B1, B14 bis B19), dessen Ausgabe mit `ifcopenshell.validate` einschließlich der EXPRESS-Regeln geprüft ist,
3. an der Recherchedokumentation in `../recherche/` (01, 06, 08, 09, 10, 13, 14, 16 bis 20, 22).

**Einschränkung [V].** Der buildingSMART Validation Service war aus der Arbeitsumgebung nicht erreichbar (Proxy 403). Geprüft wurde deshalb nur lokal gegen Schema und EXPRESS-Where-Rules, nicht gegen die Gherkin-Regeln des Service (`beispiele/ergebnisse.md`). Aussagen „validiert“ meinen in diesem Kapitel diese lokale Prüfung.

**Form der Entscheidungen.** Designentscheidungen sind als E8.1 bis E8.28 nummeriert. Jede nennt die Entscheidung, die Begründung und den Beleg. Kapitel 9 (Regelraum), 11 (Reifegrade) und 20 (Evaluation) verweisen auf diese Nummern.

## 8.1 Schemawahl: IFC4X3_ADD2 und IFC4 als abgeleiteter Export

### 8.1.1 Die Optionen

Zur Wahl stehen zwei offizielle Schemata. IFC 4.3.2.0 (IFC4X3_ADD2) ist als ISO 16739-1:2024 genormt [@iso2024ifc]. IFC4 ADD2 TC1 (ISO 16739-1:2018) ist daneben weiterhin offiziell und hat heute die breitere Unterstützung in Software (Recherche 06). IFC 4.4 ist in Arbeit, IFC 5 im Alpha-Stand [@vanberlo2021future].

Für den Holzrahmenbau sind die Unterschiede zwischen den Schemata gering, für die übrigen Phasen erheblich. Die maschinelle Gegenüberstellung beider Schemata in IfcOpenShell 0.8.5 ergibt [V]:

| Konzept | IFC4 | IFC4X3_ADD2 | Bedeutung für die Arbeit |
|---|---|---|---|
| Oberklasse der Bauteile | `IfcBuildingElement` | `IfcBuiltElement` | abstrakt, beim Export umbenennbar |
| Elementierte Wand | `IfcWallElementedCase` vorhanden | entfallen; `IfcWall` ELEMENTEDWALL | Mapping 8.2 gilt in beiden, der Sonderfall entfällt |
| Aussparungsvorschlag | `IfcVirtualElement` **ohne** PredefinedType | `IfcVirtualElement` PROVISIONFORVOID | TGA-Koordination (8.4) nur in 4.3 typisiert |
| Verteiler | nur `IfcElectricDistributionBoard` | `IfcDistributionBoard` (alte Klasse deprecated) | Umbenennung beim Export |
| Fahrzeug (LKW) | fehlt | `IfcVehicle` | Logistik (B18) nur in 4.3 |
| Baugrund, Aushub | fehlen | `IfcGeotechnicalStratum`, `IfcEarthworksCut`, `IfcBorehole` | Grundwasser und Versickerung (B17) nur in 4.3 |
| Hebezeug | `IfcTransportElement` LIFTINGGEAR | dto., zusätzlich HAULINGGEAR | in beiden abbildbar |
| Enum-Umfang | z. B. `IfcPlateTypeEnum` mit 4 Werten | 11 Werte | engere Typisierung in 4.3 |

Die elementierte Holzrahmenwand selbst ist also in beiden Schemata abbildbar. Die Entscheidung für IFC 4.3 fällt deshalb nicht am Wandelement, sondern an den Phasen davor und danach: Aussparungskoordination, Baugrund, Entwässerung, Logistik.

**E8.1 – IFC4X3_ADD2 ist das kanonische Schema.** *Entscheidung.* Der Generator schreibt ausschließlich `FILE_SCHEMA(('IFC4X3_ADD2'))`. *Begründung.* Nur dieses Schema ist zugleich ISO-Norm in aktueller Ausgabe und inhaltlich breit genug für die Phasen nach 8.4. Mehrere Konzepte der Kette (PROVISIONFORVOID, `IfcVehicle`, `IfcGeotechnicalStratum`) fehlen in IFC4. Die Praxisempfehlung aus Österreich weist in dieselbe Richtung [@tugraz2025syswood]. *Beleg.* ISO 16739-1:2024 [@iso2024ifc]; Schemavergleich oben [V]; alle Beispielausgaben B1 und B14 bis B19 sind IFC4X3_ADD2 und bestehen die lokale Validierung mit 0 Meldungen [V].

### 8.1.2 Konformität ohne Model View Definition

Eine MVD legt fest, welche Teilmenge des Schemas in einem Austausch mit welcher Detaillierung geliefert wird [@eastman2010exchange; @venugopal2012semantics]. Für IFC 4.3 sind nur die Reference View und die Alignment-based View offiziell. Eine Design Transfer View wurde nie veröffentlicht, und die Reference View ist laut Dokumentation kein vollständiger Austausch der Entwurfsabsicht [@bsiMvd43] (Recherche 01 und 06). Dass bestehende MVDs vorgefertigte Bauweisen nicht abdecken, ist auch für den Modulbau belegt [@ramaji2017extending].

Die Arbeit kann sich deshalb nicht auf eine MVD berufen. Alle erzeugten Dateien schreiben folgerichtig `FILE_DESCRIPTION(('ViewDefinition [NotAssigned]'),'2;1')` in den Kopf [V, B1 und B14 bis B19]. Das ist keine Nachlässigkeit, sondern die ehrliche Angabe, dass keine offizielle Sicht erfüllt wird.

„Standardkonform“ wird stattdessen als **Prüfkette** operationalisiert. Sie verbindet vier Stufen, die sich in ihrer Reichweite ergänzen:

| Stufe | Prüfgegenstand | Werkzeug | Reichweite | Stand im Prototyp |
|---|---|---|---|---|
| K1 | Syntax, Schema, EXPRESS-Where-Rules | `ifcopenshell.validate(..., express_rules=True)` | jede Instanz | umgesetzt, 0 Meldungen [V] |
| K2 | normative Regeln (Implementer Agreements, Informal Propositions), Industry Practices, bSDD | buildingSMART Validation Service [@bsi2025validation; @bsiValidation] | Konventionen des Standards | nicht erreichbar, offen |
| K3 | Informationsanforderungen je Übergabe und Reifegrad | IDS 1.0 [@bsi2024ids] | Merkmale, Klassifikation, Material, Beziehungen | 11 Spezifikationen in B2 [V] |
| K4 | geometrische und berechnete Regeln | eigene Regelmaschine (Kapitel 9) | Geometrie, elementübergreifende Regeln | B3 bis B5, B14 bis B20 |

Die Stufen sind nicht austauschbar. Der Validation Service prüft keine Projekt- und Firmenregeln (Recherche 06). IDS prüft das Vorhandensein und die Werte von Merkmalen, nicht die Geometrie und nicht Beziehungen über mehrere Elemente [@fischer2024extending; @akbas2025holistic]. Erst alle vier Stufen zusammen ergeben eine prüffähige Aussage. Der Ansatz, Prüfregeln bei jeder Revision automatisch auszuführen, geht auf Moult und Krijnen zurück [@moult2020compliance]. Die Beschränkung auf deklarative, werkzeugunabhängige Anforderungen folgt dem Befund von Tomczak et al., dass keine einzelne Spezifikationsmethode alle Aspekte abdeckt [@tomczak2022review].

**E8.2 – Konformität ist das Bestehen der Prüfkette K1 bis K4, nicht die Erfüllung einer MVD.** *Entscheidung.* Jede Revision durchläuft K1 und K2. An jedem Freigabe-Gate kommen die IDS des Gates (K3) und die Regelmaschine (K4) hinzu. Eine Revision, die eine Stufe nicht besteht, wird nicht freigegeben. *Begründung.* Für die Breite von Entwurf bis Fertigung existiert keine offizielle MVD. Eine eigene MVD wäre nicht offiziell und damit kein Beleg für Konformität. Die Prüfkette dagegen verwendet nur offizielle Werkzeuge (Schema, Validation Service, IDS 1.0) und macht die eigenen Regeln als solche sichtbar. *Beleg.* [@bsiMvd43; @bsi2025validation; @bsi2024ids]; CHEK wählt aus demselben Grund IDS statt mvdXML [@chek2024d22]; B2 findet in einem absichtlich fehlerhaften Modell genau die sechs eingebauten Fehler (HRB-01, 03, 05, 08, 09, 11) [V].

### 8.1.3 Software-Unterstützung und IFC4-Fallback

Die Werkzeugpraxis hinkt dem Standard hinterher. hsbcad und cadwork exportieren nur bis IFC4, Archicad bietet kein IFC 4.3 an, Allplan schon (Recherche 06) [V]. In einer österreichischen Erhebung ist in der Praxis zu 56 % IFC4 im Einsatz [@tugraz2025syswood]. Das deckt sich mit dem historischen Befund, dass ein im Schema reicher Standard in der Werkzeugpraxis oft nur teilweise umgesetzt wird [@laakso2012ifc], und mit dokumentierten Verlusten beim Austausch zwischen heterogenen Programmen [@lai2018interoperability; @pazlar2008interoperability].

Für die Arbeit folgt daraus ein Zielkonflikt. Das kanonische Modell soll das reichere Schema nutzen, die Werkstatt und das Holzbau-CAD sollen es aber lesen können. Die Lösung ist ein Export, der aus dem kanonischen Modell *abgeleitet* wird und dessen Verluste bekannt sind.

**E8.3 – Der Generator ist schema-agnostisch; IFC4 entsteht nur als abgeleiteter Export mit Verlustprotokoll.** *Entscheidung.* Das Klassenmapping wird als Tabelle je Schema gepflegt, nicht im Code verstreut. Ein IFC4-Export wird bei Bedarf aus demselben Parametermodell erzeugt, nicht durch Rückkonvertierung der 4.3-Datei. Jeder Export listet die Konzepte, die in IFC4 fehlen (Tabelle 8.1.1), und die Elemente, die davon betroffen sind. *Begründung.* Eine Rückkonvertierung auf Dateiebene müsste fehlende Konzepte raten. Die Erzeugung aus dem Parametermodell kann sie gezielt ersetzen: PROVISIONFORVOID etwa durch ein untypisiertes `IfcVirtualElement` mit Pset, `IfcDistributionBoard` durch die IFC4-Klasse. *Beleg.* Schemavergleich 8.1.1 [V]; Softwarestand Recherche 06 [V]. Der IFC4-Export ist im Prototyp **nicht umgesetzt**. Die Aussage ist deshalb eine Entwurfsentscheidung [U], deren Tragfähigkeit Kapitel 20 mit einem Import in hsbcad oder cadwork prüfen muss.

### 8.1.4 Ausblick IFCX

IFC 5 zielt auf Modularisierung, eine sprachunabhängige Basisstruktur und ein „Late Binding“ fachlicher Inhalte [@vanberlo2021future]. Binäre Formate wie HDF5 zeigen, wie Zugriff, Kompression und Revisionen effizienter werden können [@krijnen2020efficient]. Die Serialisierung IFCX ist im Alpha-Stand. Am 26.08.2026 hat der Projektplan die nächste Genehmigungsphase bestanden, ein Release-Termin ist nicht bekannt (Recherche 06) [U].

**E8.4 – Die Arbeit wartet nicht auf IFCX und bleibt bei der STEP-Datei.** *Entscheidung.* Kanonische Serialisierung ist die STEP-Physical-File (ISO 10303-21) nach IFC4X3_ADD2. Die Migration wird vorbereitet, nicht vorweggenommen: stabile GlobalIds (E8.27), bSDD-Verweise für alle eigenen Merkmale (E8.21) und Anforderungen als IDS (E8.2). *Begründung.* Validation Service und IDS-Werkzeuge arbeiten heute auf STEP-Dateien. Ein binäres oder vorläufiges Format würde die Prüfkette K2 und K3 unterbrechen. Die drei vorbereitenden Maßnahmen sind vom Serialisierungsformat unabhängig. *Beleg.* [@vanberlo2021future; @krijnen2020efficient]; Recherche 06.

## 8.2 Klassenmapping des Holzrahmenbaus

### 8.2.1 Das Mapping

Ein Implementierungsleitfaden von buildingSMART für den Holzbau existiert nicht, und die Fachgruppe „BIM im Holzbau“ von buildingSMART Deutschland hat ihren Anwendungsfall noch nicht veröffentlicht (Recherche 01 und 06). Das Mapping in Tabelle 8.2 ist deshalb eine eigene Konvention. Jede Zeile ist am Schema IFC4X3_ADD2 geprüft und in B1 (`beispiele/b1_wandelement.py`) umgesetzt. Die Spalte „B1“ nennt die Anzahl in `ausgabe/wandelement.ifc` für eine Außenwand von 4,80 × 2,75 m mit einem Fenster von 1,26 × 1,385 m.

**Tabelle 8.2: Klassenmapping der Holzrahmenwand (IFC4X3_ADD2)**

| Bauteil | IFC-Klasse | PredefinedType / ObjectType | Beziehung | B1 | Status |
|---|---|---|---|---:|---|
| Wandelement | `IfcWall` | ELEMENTEDWALL | `IfcRelAggregates` → Teile; `IfcRelContainedInSpatialStructure` → Geschoss | 1 | [V] |
| Wandtyp mit Schichtaufbau | `IfcWallType` + `IfcMaterialLayerSet` | ELEMENTEDWALL | `IfcRelDefinesByType`; am Exemplar `IfcMaterialLayerSetUsage` | 1 Typ, 5 Schichten | [V] |
| Ständer, Königs-, Sturzauflager-, Füllständer | `IfcMember` | STUD; Rolle im ObjectType | Teil der Wand | 15 (inkl. Sturz) | [V] |
| Schwelle, Rähm, Brüstungsriegel | `IfcMember` | PLATE; Rolle im ObjectType | Teil der Wand | 3 | [V] |
| Beplankung (GKF, OSB, Holzfaser) | `IfcPlate` | SHEET; ObjectType „Beplankung“ | Teil der Wand | 10 | [V] Enum, Zuordnung Konvention |
| Gefachdämmung | `IfcBuildingElementPart` | INSULATION („infill in stud walls“) | Teil der Wand, je Gefach | 12 | [V] |
| Dampfbremse, Folie | `IfcBuildingElementPart` | USERDEFINED / ObjectType MEMBRANE; Pset `HRB_Feuchteschutz` | Teil der Wand | 1 | [U] Konvention, umschaltbar auf `IfcCovering` MEMBRANE |
| Kerve, Bohrung, Fase | `IfcVoidingFeature` | NOTCH, HOLE, CHAMFER, MITER, CUTOUT, EDGE | `IfcRelVoidsElement` → Holz | 1 (NOTCH) | [V] volumengenau abgezogen |
| Fenster-, Türöffnung | `IfcOpeningElement` | OPENING | `IfcRelVoidsElement` → Wand | 1 | [V] |
| Schraube, Nagel, Klammer | `IfcMechanicalFastener` | SCREW, NAIL, STAPLE | Teil der Wand; `IfcRelDefinesByType` | 176 | [V] |
| Verbindungsmitteltyp | `IfcMechanicalFastenerType` | SCREW; NominalDiameter, NominalLength | `IfcRelDeclares` am Projekt | 1 | [V] |
| Nagel- und Schraubbild | `IfcRepresentationMap` am Typ + `IfcMappedItem` je Exemplar | – | Geometrieverweis | 1 Map, 176 Items | [U] Designentscheidung |
| Energie-Raumbegrenzung | `IfcRelSpaceBoundary2ndLevel` | – | Raum ↔ Wand | – | [V], optional (8.4) |

Die Materialien tragen die bauphysikalischen und holztechnischen Kennwerte als Standard-Psets am `IfcMaterial`: `Pset_MaterialThermal.ThermalConductivity`, `Pset_MaterialCommon.MassDensity` und für Holz `Pset_MaterialWood` mit Species und StrengthGrade. An der Wand stehen `Pset_WallCommon` (IsExternal, LoadBearing, ThermalTransmittance = 0,187 W/(m²K) aus B3) und `Qto_WallBaseQuantities`. Die Wand ist nach DIN 276, Ausgabe 2018-12, als Kostengruppe 331 „Tragende Außenwände“ klassifiziert und über `IfcMapConversion` auf EPSG:25832 georeferenziert. Die Georeferenz ist ein bekannter Schwachpunkt exportierter Modelle [@jaud2020georeferencing; @jaud2022georeferencing]; im generierten Modell ist sie ein Parameter und wird nicht von Hand gesetzt.

Insgesamt enthält die Datei 2 393 Entitäten, davon 391 `IfcRoot`-Instanzen, 30 Property-Sets und 42 Mengen-Sets, bei 135 927 Bytes. Unter der Wand hängen über eine einzige `IfcRelAggregates` 217 Teile: 18 `IfcMember`, 10 `IfcPlate`, 13 `IfcBuildingElementPart` und 176 `IfcMechanicalFastener` [V].

### 8.2.2 Ausschnitt aus B1

Listing 8.1 zeigt die tragenden Zeilen der erzeugten Datei. Die Zeilen sind unverändert übernommen. Lange Referenzlisten sind mit „…“ gekürzt.

**Listing 8.1: Ausschnitt aus `beispiele/ausgabe/wandelement.ifc` (IFC4X3_ADD2, SHA-256 `5a796ea7…f8bb478b`)**

```text
FILE_DESCRIPTION(('ViewDefinition [NotAssigned]'),'2;1');
FILE_SCHEMA(('IFC4X3_ADD2'));
#34=IFCWALLTYPE('2zeMBsHyLNShJEUzdCSStb',$,'AW-HRB-01',$,$,$,$,$,$,.ELEMENTEDWALL.);
#35=IFCMATERIALLAYERSET((#41,#47,#49,#55,#61),'AW-HRB-01',$);
#41=IFCMATERIALLAYER(#36,12.5,$,'Gipsplatte Typ DF (GKF) 12.5 mm',$,$,$);
#66=IFCWALL('0gsiGQj_bG3wx8M0qwRA0U',$,'Au\X2\00DF\X0\enwand Nord, Element 1',$,$,#65,#71,'AW-01',.ELEMENTEDWALL.);
#70=IFCSHAPEREPRESENTATION(#15,'Axis','Curve2D',(#69));
#73=IFCRELDEFINESBYTYPE('2wxG5FEoXS7huWWe7MQiFf',$,$,$,(#66),#34);
#74=IFCMATERIALLAYERSETUSAGE(#35,.AXIS2.,.POSITIVE.,0.,$);
#75=IFCRELASSOCIATESMATERIAL('3p1oxa9oXOWRZhbUsAWNaE',$,$,$,(#66),#74);
#112=IFCMEMBER('3N9BxbmVjJqfMasIm6VCTu',$,'Schwelle',$,'Schwelle',#111,#123,$,.PLATE.);
#148=IFCMEMBER('0ruebnGhrPUPaN5fsim6Vf',$,'Randst\X2\00E4\X0\nder links',$,'Randst\X2\00E4\X0\nder',#147,#157,$,.STUD.);
#408=IFCVOIDINGFEATURE('2wzspq7qPLDQOqcQt$qavq',$,'Kerve K1','Kerve f\X2\00FC\X0\r Elektro-Leerrohr (Beispiel), …',$,#407,#417,$,.NOTCH.);
#418=IFCRELVOIDSELEMENT('26reED$iDQSQquU8q9MZLr',$,$,$,#280,#408);
#1123=IFCMECHANICALFASTENERTYPE('10kcZK2DzMauPxIfg5Yrjt',$,'Spanplattenschraube 4,0x50',$,$,$,(#1136),$,$,.SCREW.,4.,50.);
#1136=IFCREPRESENTATIONMAP(#1135,#1133);
#1148=IFCMECHANICALFASTENER('39T8Vw55TT3BNaXCjVnHka',$,'Spanplattenschraube 4,0x50 #1',$,$,#1147,#1151,$,4.,50.,.SCREW.);
#1149=IFCMAPPEDITEM(#1136,#1138);
#1150=IFCSHAPEREPRESENTATION(#14,'Body','MappedRepresentation',(#1149));
#2392=IFCRELAGGREGATES('3H$X1wKCnSyfz6MaSj_7C9',$,$,$,#66,(#112,#130,#148,#164,#180, … ));
#2393=IFCRELDECLARES('17aKl5sN5P6hlC7TY$2CDz',$,$,$,#1,(#34,#1123));
```

Das Listing zeigt fünf Eigenschaften des Mappings:

1. Die Wand (#66) hat **nur eine Achsrepräsentation** (`Axis`, `Curve2D`), keinen eigenen Körper. Ihre Geometrie ist die Summe der Teile. Das Aggregat hat in IFC keine eigene Body-Geometrie, die zu den Teilen konsistent gehalten werden müsste (Recherche 06).
2. Der Schichtaufbau hängt am Typ (#34, #35) und über `IfcMaterialLayerSetUsage` (#74) am Exemplar. Die Aggregation (#2392) liefert daneben die Einzelteile. Beide Darstellungen stehen in derselben Datei (Abschnitt 8.3).
3. Die Rolle eines Holzes steht im ObjectType (#148: „Randständer“), der PredefinedType ist immer gesetzt (STUD, PLATE).
4. Die Kerve (#408) ist ein `IfcVoidingFeature` mit eigener Beziehung (#418) zum Ständer (#280), nicht eine geänderte Ständergeometrie.
5. Die Schraube (#1148) trägt NominalDiameter und NominalLength redundant zum Typ (#1123) und verweist mit einem `IfcMappedItem` (#1149) auf die Typ-Geometrie (#1136).

### 8.2.3 Begründung der Einzelentscheidungen

**E8.5 – Das Wandelement ist `IfcWall` ELEMENTEDWALL mit `IfcRelAggregates`, nicht `IfcElementAssembly`.** *Entscheidung.* Jedes vorgefertigte Wand-, Decken- oder Dachelement ist ein Bauteil der passenden Klasse (`IfcWall`, `IfcSlab`, `IfcRoof`), das seine Teile aggregiert. `IfcElementAssembly` bleibt Baugruppen ohne eigene Bauteilsemantik vorbehalten, etwa der Gaube (8.4). *Begründung.* Nur so trägt das Element zugleich die Bauteilsemantik, die Bauantrag, Energie- und Schallnachweis brauchen (Außenwand, tragend, U-Wert, Feuerwiderstand), und die Fertigungsstruktur. In IFC4X3 ist der Sonderfall `IfcWallElementedCase` entfallen, das Muster „Bauteil aggregiert Teile“ ist der vorgesehene Ersatz. Die Hierarchie Haus – Element – Wand – Ständer – Verbindungsmittel entspricht dem Produktarchitekturmodell vorgefertigter Bauten [@ramaji2016product; @ramaji2017product]. *Beleg.* Recherche 01 [V]; Schemavergleich 8.1.1 [V]; IDS-Spezifikation HRB-07 („jedes Member, Plate und Part ist Teil einer IfcWall“) findet in B1 alle 41 Teile [V].

**E8.6 – PredefinedType ist immer gesetzt, die fachliche Rolle steht im ObjectType, Proxy-Elemente sind verboten.** *Entscheidung.* Kein Element wird als `IfcBuildingElementProxy` oder mit NOTDEFINED geschrieben. Fehlt ein passender Enum-Wert, gilt USERDEFINED mit einem ObjectType aus einem kontrollierten Vokabular (E8.15). Rollen, die das Enum nicht unterscheidet (Königs-, Sturzauflager-, Füllständer), stehen im ObjectType. *Begründung.* Proxies und NOTDEFINED machen die Semantik für Prüfregeln unsichtbar. Das kontrollierte Vokabular im ObjectType lässt sich per IDS prüfen und später auf bSDD-Klassen abbilden. *Beleg.* Recherche 06 (Absicherung „keine Abweichung vom Standard“); IDS-Spezifikation HRB-11 in B2 erkennt ein eingefügtes Proxy-Element [V]. **Offener Punkt [U]:** B1 führt den Sturz als `IfcMember` STUD mit ObjectType „Sturz“. Das Schema bietet mit `IfcBeam` LINTEL eine semantisch genauere Klasse [V, Enum]. Die Entscheidung ist vor der Werkplanung zu revidieren, weil Statik- und Abbundsoftware den Sturz als Biegeträger erwarten dürften.

**E8.7 – Die Dampfbremse ist ein `IfcBuildingElementPart`, nicht ein `IfcCovering`.** *Entscheidung.* Folien im Elementquerschnitt werden als `IfcBuildingElementPart` USERDEFINED mit ObjectType MEMBRANE und eigenem Pset (`HRB_Feuchteschutz` mit Funktion und sd-Wert) aggregiert. Die Alternative `IfcCovering` MEMBRANE ist im Generator per Schalter verfügbar. *Begründung.* Die Dampfbremse wird im Werk als Teil des vorgefertigten Elements eingebaut. `IfcBuildingElementPart` ist in IFC 4.3 für Teile gedacht, die zu einem Bauteil zusammengesetzt werden; die Norm nennt die Dämmung einer Ständerwand als Beispiel. So hängen alle Schichten einheitlich über `IfcRelAggregates` an der Wand. `IfcCovering` beschreibt dagegen eine Bekleidung, die über `IfcRelCoversBldgElements` auf ein Bauteil aufgebracht wird. Ihr Vorteil, das Enum MEMBRANE und `Pset_CoveringTypeMembrane`, wiegt den Bruch der Aggregationslogik nicht auf. *Beleg.* Recherche 01 (Status [U], Konvention); Begründung im Modulkommentar von B1; der Test „Folie als IfcCovering“ belegt, dass beide Varianten validieren [V].

**E8.8 – Bearbeitungen am Holz sind `IfcVoidingFeature`; Plattenausschnitte stehen in der Profilgeometrie.** *Entscheidung.* Kerven, Bohrungen, Fasen und Gehrungen an Stäben werden als `IfcVoidingFeature` mit `IfcRelVoidsElement` modelliert. Beplankungsplatten erhalten den Fensterausschnitt dagegen direkt als Profil mit Aussparung (`IfcArbitraryProfileDefWithVoids`); die Öffnung (`IfcOpeningElement`) schneidet nur die Wand. *Begründung.* Stabbearbeitungen sind Fertigungsoperationen, die als eigene Objekte in BTLx übergeben werden (B7: Kerve als `Lap` in Ständer R1). Als eigenständige Features sind sie identifizierbar, zählbar und rückverfolgbar. Plattenausschnitte dagegen entstehen beim Zuschnitt und sind keine eigene Bearbeitung am Werkstück. *Beleg.* Recherche 01: `IfcVoidingFeature` wird volumengenau abgezogen [V, selbst getestet]. In B1 stimmt für alle 41 Teile das tesselierte Volumen mit Qto NetVolume überein (Abweichung < 10⁻⁹ m³), einschließlich Ständer R1 mit Kerve (0,03150 statt 0,03156 m³) [V]. **Befund:** Der Abzugskörper braucht 1 mm Überstand; koplanare Flächen lieferten sonst keinen korrekten Booleschen Abzug [V].

**E8.9 – Verbindungsmittel sind Einzelobjekte mit Typ; die Geometrie ist ein `IfcMappedItem` auf die Typ-Geometrie.** *Entscheidung.* Jede Schraube, jeder Nagel und jede Klammer ist ein `IfcMechanicalFastener` mit eigener Platzierung. Durchmesser und Länge stehen am `IfcMechanicalFastenerType` und redundant am Exemplar. Die Körpergeometrie existiert einmal als `IfcRepresentationMap` am Typ. *Begründung.* Das Einzelobjekt macht jedes Verbindungsmittel adressierbar, für Nachweise, Mengen und Maschinendaten (BTLx 2.3 kennt Nagel-, Schrauben- und Klammerattribute [@btlx23]). Die Redundanz der Attribute ist eine Folge von IDS 1.0: Attribute werden anders als Properties nicht vom Typ vererbt, eine Regel „jede Schraube hat einen Durchmesser“ schlüge sonst fehl [V, B1/B2]. Das `IfcMappedItem` hält die Datei klein, weil die Geometrie nicht 176-mal wiederholt wird. *Beleg.* B1: 176 Schrauben 4,0 × 50 mm, Abstand 150 mm, Randabstand 75 mm, mindestens 10 mm zum Plattenrand oder Ausschnitt [V]. **Kosten der Entscheidung [V]:** Jede Schraube belegt sieben Entitäten (Punkt, Achse, lokale Platzierung, Exemplar, MappedItem, Repräsentation, Produktform). Die 176 Schrauben stellen 1 232 der 2 393 Entitäten (51,5 %) und 69 467 der 135 927 Bytes (51,1 %). Bei Klammerbildern mit deutlich kleinerem Abstand wächst dieser Anteil entsprechend; eine Messung steht aus. Als Rückfallebene bleibt ein Nagelbild als *eine* Repräsentation mit vielen Items am Typ; dann geht die Einzeladressierung verloren [U].

Tabelle 8.2 zeigt, dass die Holzrahmenwand ohne Schemaerweiterung und ohne Proxy bis zum einzelnen Verbindungsmittel abbildbar ist. Dass das Mapping schemakonform ist, war nach Kapitel 5 zu erwarten (Abschnitt 5.3.2). Neu ist der Nachweis an einem erzeugten, byte-reproduzierbaren Modell mit Volumenprobe und IDS-Prüfung. Offen ist, ob Fremdsoftware es liest. Das führt zur doppelten Darstellung.

## 8.3 Doppelte Darstellung: Schichtenmodell und Einzelteile

### 8.3.1 Der TIMBIM-Befund

Das österreichische Projekt TIMBIM stellt die Schichtaufbauten von dataholz.eu als IFC und als Datenvorlagen nach ISO 23387 im bSDD bereit [@timbim2024; @iso23387]. Geplant war, jede Schicht als eigene Komponente über eine Aggregation in `IfcWall` abzubilden. Diese Variante wurde **verworfen**, weil die Autorensoftware sie nicht umsetzte; laut Recherche 11 war die Design Transfer View in der Autorensoftware nicht implementiert. Die Schichten werden seither nur alphanumerisch transportiert (graue Literatur) [V].

Der Befund ist für die Arbeit ein Warnsignal und kein Gegenbeweis. Er zeigt, dass ein Modell *nur* mit Aggregation für viele Programme leer oder unvollständig ist. Er zeigt nicht, dass die Aggregation falsch ist. Im Gegenteil: Die Fertigung braucht die Einzelteile, weil Maschinendaten, Stücklisten und Mengen je Holz erzeugt werden [@alwisy2019bim; @liu2016ontology; @darwish2022automated].

### 8.3.2 Zwei Sichten auf dasselbe Bauteil

Das Modell liefert deshalb beide Darstellungen, und zwar gleichzeitig und am selben Objekt:

| Sicht | Träger in IFC | Leser | Inhalt in B1 |
|---|---|---|---|
| Schichtenmodell | `IfcMaterialLayerSet` am `IfcWallType`, `IfcMaterialLayerSetUsage` an der `IfcWall` | Autorensoftware, Energie- und Bauphysikprogramme, Bauteilkataloge | 5 Schichten, 287,7 mm: GKF 12,5 – OSB 15 – Dampfbremse 0,2 – Gefach 200 – Holzfaser 60 |
| Einzelteilmodell | `IfcRelAggregates` an der `IfcWall` | Werkplanung, BTLx/WUP, Stückliste, Mengen, Statik | 217 Teile: 18 Hölzer, 10 Platten, 13 Teile, 176 Schrauben |

**E8.10 – Beide Darstellungen werden aus einer Quelle erzeugt und nie von Hand bearbeitet.** *Entscheidung.* Der Generator schreibt jedes vorgefertigte Element mit Layer-Set *und* Aggregation. Beide entstehen aus demselben Parametermodell (`daten/wandelement.json`: Schichtfolge innen nach außen, Ständerraster, Öffnungen, Verbindungsmittel). Keine Anwendung ändert eine der beiden Sichten direkt; Änderungen laufen über das Parametermodell. *Begründung.* Werden beide Sichten aus einer Quelle abgeleitet, können sie nicht auseinanderlaufen. Die Redundanz ist dann kein Konsistenzrisiko, sondern ein Kompatibilitätsmittel: Programme, die nur Schichten lesen, erhalten Schichten, die Fertigung erhält Teile. Der Vorschlag entspricht der Folgerung aus Recherche 01 („deshalb beides liefern“). *Beleg.* [@timbim2024]; B1 [V]. Das Multi-LOD-Metamodell von Abualdenien und Borrmann liefert mit `IsRefinedBy` die formale Grundlage, zwei Detaillierungen desselben Bauteils konsistent zu halten [@abualdenien2019metamodel].

### 8.3.3 Konsistenz als prüfbare Invariante

Dass beide Sichten aus einer Quelle stammen, genügt als Argument nicht. Es muss in jeder Revision nachgewiesen werden. B1 prüft dafür im Test und in der IDS folgende Invarianten:

1. Die Summe der Schichtdicken ist gleich der Wanddicke im Mengen-Set (287,7 mm = `Qto_WallBaseQuantities.Width`).
2. Jedes Teil liegt in der y-Lage seiner Schicht; die Platzierungen werden aus derselben Funktion `schichtlage()` berechnet.
3. Das aus der Geometrie tesselierte Volumen jedes Teils ist gleich seinem NetVolume (41 von 41 Teilen) [V].
4. Die Hölzer überlappen sich nicht (Assertion im Layout).
5. Jedes Teil ist über `IfcRelAggregates` genau einer Wand zugeordnet (IDS HRB-07) [V].

Eine sechste Invariante fehlt noch: die Übereinstimmung der Materialvolumina je Schicht zwischen beiden Sichten, also Plattenvolumen je Beplankungsschicht gegen Schichtdicke mal Nettofläche. Sie ist als Test nachzurüsten.

### 8.3.4 Welche Sicht rechnet?

Die doppelte Darstellung verlangt eine Festlegung, welche Sicht maßgeblich ist, wenn aus ihr ein Kennwert entsteht. Das Beispiel U-Wert zeigt, dass die Frage nicht akademisch ist. Die Gefachschicht ist inhomogen: Dämmung zwischen Hölzern. Das `IfcMaterialLayerSet` kennt keine inhomogene Schicht. B1 schreibt deshalb die Zusammensetzung in den Schichtnamen („Gefach: Holzfaser-Dämmmatte (flexibel) 200 mm zwischen KVH C24 (Nadelholz) 60/200, e = 625 mm“), was für Menschen lesbar, für Programme aber nur Text ist.

B3 berechnet den U-Wert nach DIN EN ISO 6946 [@iso6946_2017] auf zwei Wegen [V, `ausgabe/kennzahlen.json`]:

| Variante | Holzanteil im Gefach | U (hinterlüftet) | U (verputzt) |
|---|---:|---:|---:|
| aus der Einzelteilgeometrie (Ständer, Stürze, Riegel, Schwelle, Rähm) | 22,5 % | 0,183 W/(m²K) | 0,187 W/(m²K) |
| aus dem Raster (Ständerbreite / Achsmaß = 60/625) | 9,6 % | 0,160 W/(m²K) | 0,163 W/(m²K) |

Der Rasteransatz, der dem Schichtenmodell entspricht, unterschätzt den Holzanteil um mehr als die Hälfte und den U-Wert um rund 13 %. Grund sind Königs- und Sturzauflagerständer, Sturz, Brüstungsriegel, Schwelle und Rähm, die im Raster nicht vorkommen. Für die Außenwand mit einem Fenster ist das der Unterschied zwischen einem bequemen und einem knappen Nachweis gegen einen Grenzwert von 0,20 W/(m²K) (IDS HRB-01).

**E8.11 – Kennwerte, die von der Holzverteilung abhängen, werden aus dem Einzelteilmodell berechnet; das Schichtenmodell trägt das Ergebnis.** *Entscheidung.* U-Wert, Masse, Holzanteil und Mengen werden aus der Geometrie der Einzelteile ermittelt und als Standard-Property (`Pset_WallCommon.ThermalTransmittance`) oder Mengen-Set an die Wand geschrieben. Das Layer-Set dient der Kompatibilität, nicht der Berechnung. *Begründung.* Nur die Einzelteile bilden die tatsächliche Holzverteilung ab. Eine Berechnung aus dem Schichtenmodell wäre systematisch zu günstig. *Beleg.* B3 [V]; Nachweisführung in Kapitel 7a. **Offener Punkt:** B1 berechnet die Masse je Teil maschinell (MassDensity × NetVolume), schreibt aber noch kein `Qto_WallBaseQuantities.GrossWeight`. Das braucht die Kranplanung (Recherche 19) und ist nachzurüsten [V].

### 8.3.5 Granularität nach Reifegrad: der Fall Fliese

Das Muster „Sammelobjekt mit Parametern oder Einzelteile“ wiederholt sich im Innenausbau. Recherche 17 und B16 bilden einen Fliesenbelag in einem achteckigen Duschraum von 4,77 m² auf zwei Arten ab, beide validiert [V]:

- **aggregiert:** ein `IfcCovering` FLOORING mit dem Pset `HP_Verlegung` (Muster, Versatz, Winkel, Rasterursprung, Fuge, Fugenmörtel) und je einem `IfcMappedItem` pro Stück,
- **einzeln:** je Stück ein `IfcCovering` als Teil des Belags über `IfcRelAggregates`, mit dem Pset `HP_Fliesenstueck` (Stückart, Schnitte, Schnittlänge, Rohling, Herkunft neu oder Reststück).

| Fall (4,77 m² Dusche) | aggregiert: Bytes / Entitäten / Coverings | einzeln: Bytes / Entitäten / Coverings |
|---|---|---|
| gerade 60 × 60, Punktablauf | 30 647 / 440 / 1 | 70 346 / 1 011 / 33 |
| Chevron 60 × 10, Punktablauf | 175 961 / 2 144 / 1 | 429 779 / 5 670 / 193 |

Hochgerechnet auf 60 m² Fliese und Parkett in einem Haus ähnlicher Stückdichte ergeben sich etwa 5 MB (einzeln) bzw. 2 MB (aggregiert) [U, Schätzung Recherche 17]. Das ist tragbar. Die Aggregation von Coverings ist in der IfcCovering-Dokumentation allerdings **kein** dokumentiertes Konzept. Sie besteht die EXPRESS-Prüfung, ihr Verhalten im Validation Service ist offen [U].

**E8.12 – Die Granularität folgt dem Reifegrad.** *Entscheidung.* In den Reifegraden P und R (Kapitel 11) werden Beläge als ein `IfcCovering` mit Verlegeparametern und Fläche geführt, in Reifegrad A als Einzelstücke mit Herkunft und Charge. Ganze Stücke sind `IfcMappedItem`-Instanzen der Typ-Vorlage, Schnittstücke eigene Körper. Dasselbe gilt sinngemäß für Verbindungsmittel (E8.9). *Begründung.* Einzelstücke sind erst nötig, wenn Verschnitt, Reststückverwertung und Charge festgeschrieben werden. Früher erzeugen sie nur Dateigröße. Die LOIN-Rahmenbedingungen Zweck, Meilenstein und Akteur rechtfertigen genau diese Staffelung [@dineniso7817-1; @abualdenien2022levels]. *Beleg.* B16 [V]; Recherche 17. Die Festschreibung der Auswahl umfasst in Reife A auch den Rasterursprung und die Stückliste; beide gehen in den Hash ein (Recherche 13).

## 8.4 Phasenabdeckung

### 8.4.1 Methode

Recherche 06 hat für jede Phase der Kette geprüft, welcher IFC-4.3-Mechanismus sie trägt, wo er endet und wie die Lücke standardkonform überbrückt wird. Die Recherchen 08 bis 22 haben diese Prüfung für TGA, Dach, Entwässerung, Logistik, Schall und Bemusterung vertieft. Sechs Teilmodelle sind als Beispiele erzeugt und validiert. Tabelle 8.3 fasst das Ergebnis zusammen. Die Spalte „Beleg“ nennt die Recherche und, wo vorhanden, das Beispiel mit der Zahl seiner Entitäten.

### 8.4.2 Übersicht

**Tabelle 8.3: Phase → IFC-4.3-Mechanismus → Grenze → standardkonforme Lösung**

| Phase | IFC-4.3-Mechanismus [V] | Grenze | Standardkonforme Lösung | Beleg |
|---|---|---|---|---|
| Entwurf, Varianten | `IfcProject`, `IfcOwnerHistory`, `IfcGroup` | höchstens ein `IfcProject` je Datei (Regel `IfcSingleProjectInstance`); OwnerHistory speichert nur die letzte Änderung | Varianten als Revisionen in der CDE, nur die gewählte im Hauptmodell (E8.13) | R06 |
| Angebot, Kosten | `IfcCostSchedule` (ESTIMATE, TENDER …), `IfcCostItem`, `IfcCostValue` mit ApplicableDate/FixedUntilDate, `IfcRelAssignsToControl`, DIN 276 als `IfcClassification` | kaum eine Software liest Kosten aus IFC | GAEB DA XML bzw. BIM-LV-Container nach DIN 18290-2 als Export [@din18290-2] | R06, R10 |
| Vertrag, Baubeschreibung | `IfcProjectOrder`, `IfcApproval` + `IfcRelAssociatesApproval`, `IfcDocumentReference`/`IfcDocumentInformation` (Revision, ValidFrom/Until) | keine Vertragsentität, keine Signatur | signiertes PDF per Dokumentverweis, Hash als eigenes Property (E8.24) | R06 |
| Bemusterung | `IfcElementType` + `Pset_ManufacturerTypeInformation` (GTIN, ArticleNumber), `IfcProjectLibrary` + `IfcRelDeclares`, bSDD-URI in `IfcClassificationReference`, PBR-Stil `PHYSICAL` | kein Konzept „Option“; Regeln außerhalb der Datei; glTF-Export verliert Texturen und UV | Optionen als deklarierte Typen, Wahl als `IfcRelDefinesByType` (E8.14); eigener Exporter für Texturen | R10, R13 |
| Bauantrag | `IfcPermit` (BUILDING), `IfcActor`/`IfcActorRole`, `IfcSite.LandTitleNumber`, `IfcMapConversion` + `IfcProjectedCRS` (EPSG:25832), `IfcSpatialZone`, `Pset_SiteCommon` | „Entwurfsverfasser“ nur als USERDEFINED-Rolle; Gemarkung, Flur, mehrere Flurstücke fehlen; `Pset_SiteCommon`-Kennzahlen ≠ GRZ/GFZ nach BauNVO; keine Semantik für Abstandsflächen | eigene Psets, Abstandsflächen in der Regelmaschine; XBau und PDF als Export | R06, R14; [@bimbauantrag2020; @nrw2026bimbauantrag] |
| Gebäudetyp, Nutzungseinheit | `IfcBuilding` je Gebäude, `IfcZone` je Wohnung, `IfcSpatialZone` FIRESAFETY/OCCUPANCY, Unter-`IfcSite` je Flurstück, `Pset_PropertyAgreement` am `IfcSpace` | `IfcBuilding` hat kein PredefinedType; Brand- und Schallanforderungen der Zonen fehlen in Standard-Psets | Typ in ObjectType und bSDD-Klasse; Rollen und Anforderungen in eigenem Pset (E8.17) | R14 (Testmodell 0 Befunde) |
| Statik | `IfcStructuralAnalysisModel`, `IfcStructuralMember`, Lasten | Holzbau-Statiksoftware liest das kaum [U] | Geometrie und Material übergeben, Ergebnis als Dokument und Nachweis (Kapitel 7a) | R06 |
| Energie | `IfcRelSpaceBoundary2ndLevel`, `ThermalTransmittance` in `Pset_*Common`, `Pset_MaterialThermal`, `IfcSpatialZone` THERMAL | Import in Software für DIN V 18599 ungeprüft [U] | Kennwerte aus Einzelteilen (E8.11), Space Boundaries eigens erzeugen [@bazjanac2010space]; Nachweis als Dokument | R06, B1/B3 |
| Schallschutz Außenlärm | `Pset_*Common.AcousticRating` (nur `IfcLabel`), `IfcSoundPressureLevelMeasure`, `IfcAnnotation` für Immissionsort und Isolinien, `IfcAirTerminal`, `IfcShadingDevice` | kein numerisches Rw, kein Standard-Pset für Raumanforderung und Fassadenpegel; Lärmkarte ist kein IFC-Objekt | Vokabular der Labels per IDS; Zahlen in eigenen Psets; Lärmkarte als GeoTIFF per Dokumentverweis | R20, B19 (253/258 Entitäten) |
| Wärmepumpe, Schall | `IfcUnitaryEquipment` (USERDEFINED bzw. SPLITSYSTEM), `Pset_SoundGeneration.SoundCurve` als Tabelle, `IfcSpatialZone` RESERVATION | keine `IfcHeatPump`; kein Standard-Pset für L_WA; Widerspruch Messtyp/Beschreibung in `SoundCurve` | USERDEFINED + ObjectType (E8.15); eigenes Pset für L_WA, Tonhaltigkeit, Kältemittel; R290-Schutzbereich als `IfcSpatialZone` | R22; B20 ohne IFC |
| TGA | `IfcDistributionSystem` (DOMESTICCOLDWATER, VENTILATION, …), `IfcPipeSegment`, `IfcCableCarrierSegment`, `IfcDistributionPort` über `IfcRelNests`, `IfcRelConnectsPorts`, `IfcDistributionBoard` | Fallen: `IfcElectricDistributionBoard`, `IfcRelConnectsPortToElement` deprecated; kein `IfcElbow`; Typ-Psets nur über `HasPropertySets` | Mapping-Tabelle nach R08; Validierung jeder Revision fängt Deprecated-Klassen ab | R08 (Testmodell 0 Fehler) |
| Durchdringungen | `IfcVirtualElement` PROVISIONFORVOID + `Pset_ProvisionForVoid`, `IfcOpeningElement`, `IfcRelVoidsElement` je Teil, `IfcRelInterferesElements`, `IfcRelFillsElement`, `IfcCovering` WRAPPING | kein Typ für Abschottung und Manschette; keine `IfcSealing`; kein TRIMMER für Wechsel | Abschottung als `IfcDiscreteAccessory` USERDEFINED, Wechsel als `IfcBeam` USERDEFINED; Koordination über BCF (E8.16) | R16, B15 (699 Entitäten) |
| Fußbodenaufbau | `IfcSlab`, `IfcCovering` FLOORING, `IfcRelCoversSpaces`, `IfcWasteTerminal` | kein Standard-Property für OKFF-Kette, R_λ,B, Belegreife | eigenes Pset je Raumaufbau | R16, B14 (300/301 Entitäten) |
| Fliesen, Parkett | `IfcCoveringType` + `RepresentationMaps`, `IfcMappedItem`, `Qto_CoveringBaseQuantities`, `Pset_ManufacturerOccurrence.BatchReference` | Muster, Fuge, Achse, R-Klasse fehlen (`Pset_CoveringFlooring` nur boolesch); Aggregation von Coverings undokumentiert | `HP_Verlegung`, `HP_Fliesenstueck`; Granularität nach Reifegrad (E8.12) | R13, R17, B16 |
| Treppe | `IfcStair` mit `IfcStairFlight` WINDER, `IfcRailing`, `IfcMember` STRINGER, `Pset_StairFlightCommon` | Flight-Attribute deprecated; Verziehungsmethode fehlt | Werte im Pset, Verziehung in `HP_Verziehung` | R13 |
| Dach, Einbauteile | `IfcRoof` (GABLE_ROOF, HIP_ROOF, HIPPED_GABLE_ROOF, MANSARD_ROOF …) aggregiert `IfcSlab` ROOF und `IfcMember` RAFTER/PURLIN/COLLAR; `IfcCovering` ROOFING/MEMBRANE über `IfcRelCoversBldgElements`; `IfcWindow` SKYLIGHT; `IfcStackTerminal` COWL | keine Enums für Latte, Schneefang, Dachtritt, First und Grat | `IfcDiscreteAccessory` FLASHING bzw. USERDEFINED; Gaube als `IfcElementAssembly` USERDEFINED | R09 (Testmodell 0 Fehler); [@zvdh2024] |
| Photovoltaik | `IfcSolarDevice` SOLARPANEL, `IfcTransformer` INVERTER, `IfcElectricFlowStorageDevice` BATTERY | Ertrag und Belegungsregeln sind kein IFC-Inhalt | Berechnung außerhalb, Ergebnis als Pset und Dokument | R08, R09 |
| Dachentwässerung | `IfcPipeSegment` GUTTER (`Pset_PipeSegmentTypeGutter`), RIGIDSEGMENT, `IfcStackTerminal` RAINWATERHOPPER, `IfcPipeFitting` BEND | Bemessungsregen ist kein Modellinhalt | Bemessung in der Regelmaschine, Eingangsdaten mit Quelle | R09 |
| Grundstücksentwässerung | `IfcDistributionSystem` SEWAGE/RAINWATER/STORMWATER, `IfcPipeSegment` mit `Pset_PipeSegmentOccurrence` (Gradient, InvertElevation), `IfcDistributionChamberElement` MANHOLE/INSPECTIONCHAMBER, `IfcInterceptor`, `IfcTank` STORAGE, `IfcGeographicElement` TERRAIN, `IfcGeotechnicalStratum` WATER | keine Klasse für Rigole und Sickerschacht | `IfcDistributionChamberElement` USERDEFINED „Versickerungsrigole“ + eigenes Pset (k_f, V_erf, MHGW) | R18, B17 (885–1 048 Entitäten) |
| Werkplanung, Fertigung | Mapping 8.2; `Pset_ManufacturerOccurrence` (SerialNumber, BarCode, BatchReference), `Pset_MaterialWood`, `Pset_Tolerance` | **keine Maschinendaten in IFC**; kein Holzbau-MVD vergleichbar IFC4Precast | BTLx und WUP als abgeleitete Exporte mit GlobalId (E8.26) [@btlx23; @compastimber] | R01, R06, B1, B7 |
| Logistik, Montage | `IfcWorkSchedule`, `IfcTask` (INSTALLATION, MOVE), `IfcTaskTime`, `IfcRelSequence`, `Pset_PackingInstructions`, `IfcConstructionEquipmentResource` ERECTING, `IfcTransportElement` LIFTINGGEAR, `IfcVehicle`, `IfcSpatialZone` CONSTRUCTION/TRANSPORT/RESERVATION | `IfcTransportElement` ist Kran oder Aufzug, nicht LKW; `Qto_VehicleBaseQuantities` ohne Gewicht; `Qto_RoofBaseQuantities` ohne Gewicht; Tourenplanung kein IFC-Inhalt | Kran als Ressource *und* Objekt (E8.18); Dachelemente als `IfcSlab` ROOF wegen Gewicht; Tourenplanung im ERP | R19, B18 (1 134 Entitäten) |
| Übergabe, Betrieb | `IfcAsset`, `IfcTask` MAINTENANCE, `Pset_Warranty`, `Pset_ServiceLife` | COBie ist US-Standard | Hausakte als Sicht auf das Modell, Dokumente per Verweis | R06 |
| Firmenregeln | `IfcConstraint`, `IfcObjective`, `IfcMetric`, `IfcProjectLibrary` | Software wertet `IfcConstraint` kaum aus | Katalog als Projektbibliothek, Merkmalsregeln als IDS, geometrische Regeln in der Regelmaschine, Ergebnisse als BCF (E8.25) | R06 |

R = Recherche. Alle genannten Beispiele (B1, B14 bis B19) bestehen `ifcopenshell.validate` mit EXPRESS-Regeln ohne Meldung [V, am 27.09.2026 nachgeprüft].

### 8.4.3 Befunde

**Befund 1: Das Schema trägt fast jede Phase [V].** In keiner Zeile der Tabelle 8.3 musste das Schema erweitert oder ein Proxy verwendet werden. Recherche 06 korrigiert dabei eine Annahme des Zielbilds: Preise mit Gültigkeit *sind* in IFC abbildbar, über `IfcCostValue.ApplicableDate` und `FixedUntilDate`.

**Befund 2: Die Grenzen liegen an vier Stellen.** Sie wiederholen sich über die Phasen:

1. **Prozessinformation:** Varianten, Versionen, Signaturen und Prüfergebnisse gehören nicht in eine Datei (8.6).
2. **Maschinen- und Behördenformate:** BTLx, WUP, GAEB, XBau und PDF sind eigene Formate. IFC ist ihre Quelle, nicht ihr Ersatz.
3. **Fehlende Enum-Werte:** Wärmepumpe, Rigole, Wechsel, Abschottung, Schneefang, Dachtritt, Lärmschutzwand und Übergangsprofil haben keinen PredefinedType.
4. **Fehlende oder zu schwache Standard-Properties:** Rw nur als Text, Rutschhemmung nur boolesch, keine OKFF-Kette, keine Hubdaten.

Keine dieser Grenzen erzwingt eine Schemaerweiterung. Die Stellen 3 und 4 sind mit USERDEFINED und eigenen Psets lösbar (E8.15, E8.21), die Stellen 1 und 2 mit standardisierten Nachbarformaten (8.6).

**Befund 3: Die Fallen liegen in der Schemaversion [V].** Drei Klassen und Beziehungen, die in IFC4 üblich waren, sind in 4.3 deprecated: `IfcElectricDistributionBoard`, `IfcRelConnectsPortToElement` und das Proxy mit PROVISIONFORVOID (Recherche 08). Zwei Regeln der EXPRESS-Prüfung fielen erst in den Beispielen auf: Typ-Psets müssen über `HasPropertySets` am Typ hängen, nicht über `IfcRelDefinesByProperties`, und jede Achse mit Axis braucht eine RefDirection (B15). Rohrsegmente brauchen immer eine Platzierung (Recherche 08). Solche Fehler fängt nur eine Validierung jeder Revision (E8.2).

**Befund 4: Die Phasenkette ist im Prototyp nur in Teilmodellen belegt.** B1 bis B19 sind getrennte Dateien. Ein Gesamtmodell eines Hauses, das alle Zeilen der Tabelle 8.3 zugleich enthält, existiert noch nicht. B20 (Wärmepumpe) schreibt bisher kein IFC, sondern JSON, Markdown und SVG. Die Aussage „IFC 4.3 trägt die Kette“ ist damit für jede Phase einzeln, aber nicht für das Zusammenspiel belegt. Das Zusammenspiel prüft Kapitel 20.

### 8.4.4 Entscheidungen zur Phasenabdeckung

**E8.13 – Varianten und Versionen liegen außerhalb der Datei.** *Entscheidung.* Pro freigegebenem Projektstand gibt es genau ein IFC. Entwurfsvarianten sind Revisionen in einer gemeinsamen Datenumgebung nach ISO 19650 [@iso19650]; nur die gewählte Variante gelangt in das Hauptmodell. *Begründung.* Die Regel `IfcSingleProjectInstance` erlaubt ein Projekt je Datei, und `IfcOwnerHistory` speichert nur die letzte Änderung. Varianten als Gruppen in derselben Datei würden jede Prüfung mehrdeutig machen. Die Literatur zum Variantenmanagement im BIM bestätigt, dass Varianten eine eigene Verwaltung brauchen [@mattern2018bimbased]. *Beleg.* Recherche 06 [V].

**E8.14 – Bemusterungsoptionen sind deklarierte Typen einer Projektbibliothek; die Wahl ist eine Typzuordnung.** *Entscheidung.* Der Katalog ist eine `IfcProjectLibrary` (z. B. „Bemusterung 2026“), die alle Optionen über `IfcRelDeclares` als Typen führt, etwa `IfcSanitaryTerminalType` TOILETPAN. Die Wahl des Kunden ist ein `IfcRelDefinesByType` vom Typ zum Exemplar. Mehr- und Minderpreise sind `IfcCostItem` mit `IfcCostValue` (Category, ApplicableDate, FixedUntilDate), die Unterschrift der Ausstattungsfestlegung ein `IfcApproval`. *Begründung.* Ein Konzept „Option“ fehlt in IFC. Die Kombination aus Bibliothek, Deklaration und Typzuordnung bildet es mit Standardmitteln nach, ohne dass nicht gewählte Optionen als Exemplare im Modell stehen. B1 nutzt dieselbe Deklaration bereits für Wand- und Schraubentyp (Listing 8.1, #2393). *Beleg.* Recherche 10, Abschnitt „Standardkonforme Verknüpfung“ [V am Schema, Muster U]. Die Bemusterung ist beim Referenzhersteller ein Fertigungs-Gate: Die Montage beginnt frühestens 12 Wochen nach der unterschriebenen Ausstattungsfestlegung (Recherche 10) [V].

**E8.15 – Fehlende Enum-Werte werden mit USERDEFINED und einem kontrollierten ObjectType-Vokabular gelöst.** *Entscheidung.* Das Vokabular ist eine Tabelle im Generator und in der IDS. Stand der Beispiele und Recherchen:

| Sachverhalt | Klasse | ObjectType | Quelle |
|---|---|---|---|
| Luft-Wasser-Wärmepumpe, Monoblock | `IfcUnitaryEquipment` | AirToWaterHeatPump_Monoblock | R22 |
| Wechsel in Holzbalkendecke | `IfcBeam` | Wechsel | R16, B15 |
| Brandschutz-, Luftdichtheitsmanschette | `IfcDiscreteAccessory` | Brandschutzmanschette / Luftdichtheitsmanschette | R16, B15 |
| Versickerungsrigole | `IfcDistributionChamberElement` | Versickerungsrigole | R18, B17 |
| Schneefang, Dachtritt, Sicherheitshaken | `IfcDiscreteAccessory` | SNOWGUARD / ROOFSTEP / SAFETYHOOK | R09 |
| First, Grat, Ortgang | `IfcDiscreteAccessory` | RIDGE / HIP / VERGE | R09 |
| Lärmschutzwand | `IfcWall` | Laermschutzwand | R20 |
| Übergangsprofil Boden | `IfcCovering` | Übergangsprofil | R13 |
| Immissionsort | `IfcAnnotation` | Immissionsort | R20, B19 |
| R290-Schutzbereich | `IfcSpatialZone` | R290_Schutzbereich | R22 |
| Dampfbremse im Element | `IfcBuildingElementPart` | MEMBRANE | B1 |

*Begründung.* USERDEFINED mit ObjectType ist der im Schema vorgesehene Weg, wenn kein Enum-Wert passt. Er erhält die Klassensemantik (Verteilungselement, Zubehör, Wand) und bleibt per IDS prüfbar. *Beleg.* Recherche 06 und 09 [V]. **Befund:** Das Vokabular ist in den Beispielen noch uneinheitlich (Deutsch und Englisch, CamelCase und Großbuchstaben). Es ist vor Kapitel 20 zu vereinheitlichen und als bSDD-Klassen zu veröffentlichen (E8.21).

**E8.16 – Durchdringungen laufen als Vorschlag, Prüfung und Freigabe.** *Entscheidung.* Die TGA erzeugt einen Aussparungsvorschlag als `IfcVirtualElement` PROVISIONFORVOID mit `Pset_ProvisionForVoid` und ohne Material. Der Holzbau prüft ihn gegen die Bohr- und Durchbruchsregeln (Kapitel 13) und antwortet als BCF-Thema mit Viewpoint und Komponenten-GUIDs: Annahme, Verschiebung oder Ablehnung. Bei Annahme entstehen je durchdrungenem Teil ein `IfcOpeningElement` mit `IfcRelVoidsElement`, eine `IfcRelInterferesElements` zwischen Leitung und Bauteil und eine Fertigungsbearbeitung. *Begründung.* Im Holzbau wird die Öffnung nicht im Raum, sondern im Ständer, Balken und in der Platte gerechnet. Die Trennung von Vorschlag und Öffnung hält den Nachweis der Querschnittsschwächung vor der Fertigung. *Beleg.* B15: 4 Vorschläge, 4 Öffnungen mit 4 `IfcRelVoidsElement`, 4 `IfcRelInterferesElements`, 1 `IfcRelFillsElement` mit Luftdichtheitsmanschette, 0 Validierungsfehler [V]; BTLx-Bearbeitungen tragen die GlobalId der Leitung (8.6).

**E8.17 – Rechtsbegriffe werden auf räumliche und gruppierende Strukturen abgebildet.** *Entscheidung.* Jede Doppelhaushälfte oder Reihenhauseinheit ist ein eigenes `IfcBuilding`, weil die Gebäudeklasse je Gebäude bestimmt wird. Jede Nutzungseinheit ist eine `IfcZone` (ObjectType „Wohnung“) über `IfcRelAssignsToGroup`, Brand- und Rauchabschnitte sind `IfcSpatialZone` FIRESAFETY, Flurstücke aggregierte Unter-`IfcSite`. *Begründung.* Diese Abbildung trägt die Regeldeltas der Gebäudetypen (Kapitel 9a), ohne das Schema zu erweitern. `Pset_PropertyAgreement` gilt nur für räumliche Strukturelemente, also für `IfcSpace`, nicht für `IfcZone` [V]. *Beleg.* Recherche 14: Testmodell mit einer Site, zwei Unter-Sites, vier Gebäuden, `IfcZone`, `IfcSpatialZone` OCCUPANCY und Haustrennwand mit 0 Befunden [V].

**E8.18 – Der Kran ist Ressource und Objekt zugleich.** *Entscheidung.* Der Einsatz des Krans ist eine `IfcConstructionEquipmentResource` ERECTING, die Vorgängen über `IfcRelAssignsToProcess` zugeordnet ist. Das Gerät selbst ist ein `IfcTransportElement` LIFTINGGEAR, mit der Ressource über `IfcRelAssignsToResource` verbunden. LKW sind `IfcVehicle` VEHICLEWHEELED mit einer Ressource TRANSPORTING. Hubdaten stehen in einem eigenen Pset am `IfcTask`. *Begründung.* Die Ressource trägt Zeit und Zuordnung, das Objekt trägt Lage und Tragfähigkeit (`Pset_TransportElementCommon.CapacityWeight`). CRANEWAY meint eine Kranbahn in einer Halle und passt für den Mobilkran nicht [V]. *Beleg.* B18: 2 Ressourcen, 1 Hebezeug, 6 Fahrzeuge, 35 Vorgänge, 33 Reihenfolgebeziehungen, 3 Zonen, 1 134 Entitäten, 0 Meldungen, byte-identisch über Läufe und Hash-Seeds [V]. Die Kranwerte in B18 sind ausdrücklich Beispielwerte (Recherche 19).

## 8.5 Klassifikation und Merkmale

### 8.5.1 Drei Fragen an ein Objekt

Die Klasse beantwortet, *was* ein Objekt im Schema ist. Für Prüfung, Kosten, Bestellung und Bauantrag reicht das nicht. Drei weitere Fragen sind zu beantworten:

1. **Wozu gehört es?** Klassifikation nach Kostengruppe, Leistungsbereich oder Produktklasse.
2. **Welche Eigenschaften hat es?** Merkmale mit Einheit und definierter Bedeutung.
3. **Welches reale Produkt ist es?** Hersteller, Artikelnummer, GTIN, Charge.

Tomczak et al. zeigen, dass bSDD mit ISO 12006, Property Templates, Product Data Templates und IDS unterschiedliche Teile dieser Fragen abdecken und keine Methode alle [@tomczak2022review]. Die Arbeit kombiniert sie deshalb und legt die Rangfolge fest.

### 8.5.2 Klassifikation

**E8.19 – Klassifikationen werden geschichtet, nicht vermischt.** *Entscheidung.* Jedes Objekt kann mehrere Klassifikationen tragen, jede über `IfcRelAssociatesClassification` mit eigener `IfcClassification`:

| Zweck | System | Beispiel | Stand |
|---|---|---|---|
| Kosten, Baubeschreibung | DIN 276 | 331 „Tragende Außenwände“ (B1) | umgesetzt [V] |
| Leistung, Ausschreibung | STLB-Bau Leistungsbereiche | LB 024 Fliesen- und Plattenarbeiten, LB 028 Parkett | Recherche 13 [V] |
| Produkt, Bemusterung | ETIM 10.0 über bSDD | Klasse EC003535 „interior door“ | Recherche 10 [V] |
| Bauteilaufbau | dataholz im bSDD („dataholz 1.5“) | Aufbau-Kennung | Recherche 01 [V], Lizenz offen |
| eigene Klassen | bSDD-Dictionary der Firma | ObjectType-Vokabular (E8.15) | geplant |

In IFC 4.3 heißt das Feld für die Quelle an `IfcClassification` **Specification**, nicht mehr Location; es trägt die bSDD-URI des Dictionaries, `IfcClassificationReference.Location` die URI der Klasse (Recherche 10) [V]. *Begründung.* Die Systeme beantworten verschiedene Fragen und haben verschiedene Lizenzen. ETIM ist frei (ODC-By 1.0) und im bSDD mit IFC 4.3 verknüpft, 97 Gruppen und 491 Klassen [V]. ECLASS ist lizenzpflichtig und wird nur auf Kundenwunsch geführt. *Beleg.* Recherche 10 und 13. **Warnung [V]:** ETIM-Klassennummern für Fliese, Parkett und Wandfarbe sind nicht verifiziert, weil das ETIM-Portal nicht erreichbar war. Sie werden erst eingetragen, wenn sie geprüft sind.

Für die Holzbranche beschreibt die Schweizer Plattform Wald & Holz 4.0 Produkt- und Materialdaten nach ETIM und BMEcat für CAD und ERP [@standtke2024etim] (graue Literatur, Jahr erschlossen [U]). Das stützt die Wahl von ETIM als Produktklassifikation auch für Holzwerkstoffe, ohne sie zu belegen.

### 8.5.3 Merkmale

Die Merkmale kommen aus vier Quellen mit abnehmender Verbindlichkeit:

1. **Standard-Psets und Qto-Sets des Schemas.** Beispiele aus B1: `Pset_WallCommon`, `Pset_MemberCommon`, `Pset_PlateCommon`, `Pset_MaterialWood`, `Qto_MemberBaseQuantities`. Sie sind Teil von ISO 16739-1 [@iso2024ifc].
2. **Veröffentlichte Merkmale mit URI.** Das BIM-Portal des Bundes stellt Merkmale nach Musterbauordnung für die Genehmigungsplanung, AIA-Vorlagen, einen IDS-Export und eine REST-API unter der Datenlizenz DL-DE-Zero-2.0 bereit [@bimportal]. dataholz.eu liefert je Aufbau Feuerwiderstand, U-Wert, Rw und Ln,w, Masse und Ökokennwerte, als IFC nach Registrierung, als IDS und im bSDD [@dataholz]. ETIM-Features stehen im bSDD. Ökobilanzdaten liefert die ÖKOBAUDAT [@oekobaudat].
3. **Product Data Templates nach ISO 23387.** Sie regeln, wie Herstellermerkmale normgerecht beschrieben und mit IFC-Klassen verknüpft werden [@iso23387]. Eine offene Plattform mit bSDD-Anbindung zeigt, dass das praktisch umsetzbar ist [@elsibaii2025open].
4. **Eigene Psets.** Nur, wo keine der ersten drei Quellen ein Merkmal bietet.

**E8.20 – Rangfolge der Merkmale: Standard vor veröffentlicht vor eigen.** *Entscheidung.* Ein Merkmal wird zuerst in einem Standard-Pset gesucht, dann im BIM-Portal, im bSDD (dataholz, ETIM) und in Data Templates, zuletzt in einem eigenen Pset. Wird ein Wert aus einer geschützten Quelle übernommen, etwa dataholz, steht die Quelle als `IfcClassificationReference` oder Dokumentverweis am Objekt, und der Wert selbst wird nur im Rahmen der Lizenz gespeichert. *Begründung.* Jede Stufe weiter unten verliert an Interoperabilität. Die Rangfolge schützt davor, bekannte Merkmale unter neuem Namen zu duplizieren. *Beleg.* [@bimportal; @dataholz; @iso23387]. dataholz liefert keine Ständerebene und ist urheberrechtlich geschützt; eine Lizenz ist anzufragen (Recherche 01; Kapitel 4.9).

**Standard-Properties mit Schwächen.** Drei Muster kehren wieder [V]:

- **Text statt Zahl:** `AcousticRating`, `FireRating` und verwandte Properties sind `IfcLabel`. Ihr Vokabular wird per IDS beschränkt, etwa auf „REI 30“ oder „Rw 42 dB (SSK 4 VDI 2719)“. Die Zahl steht zusätzlich in einem eigenen Pset (Recherche 14 und 20).
- **Boolesch statt Klasse:** `Pset_CoveringFlooring.HasNonSkidSurface` kennt nur Ja und Nein; die R-Klasse braucht ein eigenes Property (Recherche 13).
- **Falscher Begriff:** `ThermalTransmittance` in `Pset_CoveringCommon` ist ein U-Wert, kein Wärmedurchlasswiderstand R_λ,B für Beläge auf Fußbodenheizung (Recherche 13).

### 8.5.4 Eigene Property-Sets

Das Präfix „Pset_“ ist Property-Sets des Standards vorbehalten. Eigene Psets tragen es deshalb nicht (Recherche 06). Die Beispiele halten das ein, verwenden aber sechs verschiedene Präfixe [V, am 27.09.2026 aus den IFC-Dateien gezählt]:

| Pset | Objekt | schließt die Lücke | Beispiel |
|---|---|---|---|
| `HRB_Feuchteschutz` | Dampfbremse | Funktion, sd-Wert | B1 |
| `B14_Fussbodenaufbau`, `B14_Rinne` | Raumaufbau, Rinne | OKFF, Estrich, Belegreife, R_λ,B, Gefälle, Nachweis OKFF | B14 |
| `B15_Durchdringung`, `B15_Manschette` | Öffnung, Abschottung | Durchdringungsart, Prüfergebnis, Nachweisnummer | B15 |
| `HP_Verlegung`, `HP_Fliesenstueck` | Belag, Stück | Muster, Fuge, Rasterursprung, Stückart, Schnitte, Herkunft | B16 |
| `B17_Entwaesserung`, `B17_Versickerung` | Leitung, Rigole | Bemessung, k_f, V_erf, MHGW | B17 |
| `HRB_Kranhub`, `HRB_Kranaufstellung`, `HRB_Montage` | Vorgang, Kran | Hublast, Radius, Auslastung, Windgrenze | B18 |
| `HB_Schallschutz_Bauteil`, `HB_Aussenlaerm_Raum`, `HB_Fassadenpegel` | Bauteil, Raum, Immissionsort | Rw als Zahl, La, erf. R′w,ges, Pegel | B19 |
| `HP_Verziehung`, `HP_Fliese` | Treppe, Fliese | Verziehungsmethode, Fliesenmerkmale | nur Recherche 13 |

Recherche 22 schlägt für die Wärmepumpe `Pset_Holzbau_WPSchall` vor. **Das verstößt gegen die eigene Regel** und wird nicht übernommen.

**E8.21 – Alle eigenen Psets tragen ein einziges Präfix und werden als bSDD-Dictionary veröffentlicht.** *Entscheidung.* Das Präfix ist `HRB_` (Holzrahmenbau), wie in B1, B18 und den IDS-Kennungen HRB-01 bis HRB-11. Die übrigen Präfixe (B14_, B15_, B17_, HP_, HB_) werden vor Kapitel 20 umbenannt; aus `Pset_Holzbau_WPSchall` wird `HRB_WPSchall`. Jedes eigene Property erhält eine bSDD-URI und wird über `IfcExternalReferenceRelationship` mit ihr verknüpft; `IfcResourceObjectSelect` lässt `IfcPropertyAbstraction` als Ziel zu (Recherche 10) [V]. Zahlenwerte verwenden die passenden Messtypen, etwa `IfcSoundPressureLevelMeasure` für Pegel. *Begründung.* Ein Präfix je Beispiel ist ein Artefakt der Entstehung, kein Entwurf. Für Fremdsoftware und IDS muss erkennbar sein, dass alle Psets aus einem Namensraum stammen. Die bSDD-Veröffentlichung macht die Bedeutung jedes Properties unabhängig vom Code nachlesbar und bereitet die Migration vor (E8.4). *Beleg.* Recherche 06 (Präfixregel); Zählung oben [V]. Der Weg über bSDD und IDS in einem IFC4X3-Arbeitsablauf ist für wiederverwendete Bauteile gezeigt; IDS prüft dort Vorhandensein und Struktur, nicht die Richtigkeit der Werte [@fonsati2026leveraging].

### 8.5.5 Produktdaten

**E8.22 – Herstellerdaten stehen am Typ, Lieferdaten am Exemplar; Hersteller-IFC liefert nur Geometrie.** *Entscheidung.* `Pset_ManufacturerTypeInformation` (GlobalTradeItemNumber, ArticleNumber, ModelReference, Manufacturer) steht am Typ, `Pset_ManufacturerOccurrence` (SerialNumber, BatchReference) erst bei Lieferung am Exemplar. Datenblatt, Montageanleitung, Leistungserklärung und später der digitale Produktpass sind `IfcDocumentReference` über `IfcRelAssociatesDocument`. Aus Hersteller-IFC wird nur die Geometrie übernommen; Klasse, Typ, Psets und Klassifikation erzeugt der Generator. *Begründung.* Hersteller-IFC ist oft nicht 4.3-tauglich: Ein geprüftes Objekt eines Sanitärherstellers lag als IFC2X3 mit leerer GTIN und proprietären Psets vor (Recherche 10) [V]. Für Verbindungsmittel gilt dasselbe: Eine eigene Tabelle mit Typ, Durchmesser, Länge und Zulassung ist verlässlicher als Hersteller-IFC, das nur zur Visualisierung dient (Recherche 01). *Beleg.* Recherche 10 und 17; die GTIN ist Pflichtfeld des Reifegrads A (Kapitel 11).

## 8.6 Grenzen und standardkonforme Überbrückung

### 8.6.1 Was nicht in die Datei gehört

Abschnitt 8.4 hat die Grenzen phasenweise benannt. Sie lassen sich auf sieben Arten zurückführen. Für jede gibt es ein standardisiertes Nachbarformat oder eine Konvention, die ohne Eingriff ins Schema auskommt.

| Grenze | Warum nicht im IFC | Überbrückung | Verbindung zum IFC | Beleg |
|---|---|---|---|---|
| Versionen, Varianten, Freigabestatus | ein Projekt je Datei, OwnerHistory nur mit letzter Änderung | CDE nach ISO 19650 | GlobalIds bleiben über Revisionen gleich (E8.27) | [@iso19650; @jaskula2024common] |
| Vertrag, Signatur, Nachweishefte | keine Vertragsentität, keine Signatur | signierte PDF-Dokumente | `IfcDocumentReference` + Hash-Property, Status als `IfcApproval` | [@alfaro2025chek; @fakour2025exploring] |
| Prüfergebnisse, Rückfragen | keine Kommunikationssemantik | BCF-Themen mit Viewpoint | Komponenten-GUIDs im Thema | Recherche 06, 16 |
| Maschinendaten | keine Bearbeitungssemantik für Anlagen | BTLx (Abbund), WUP (Wandanlagen) | GlobalId als Attribut je Teil oder Bearbeitung | [@btlx23]; Recherche 01 |
| Leistungsverzeichnis, Behördenverfahren | eigene Fachformate | GAEB bzw. BIM-LV-Container, XBau, PDF-Bauvorlagen | Linkmodell bzw. IFC als Anlage | [@din18290-2; @bimbauantrag2020abschluss] |
| Parametrik, Regeln | IFC beschreibt Ergebnisse, nicht ihr Zustandekommen | Parametermodell, IDS, Regelmaschine | Pfad im Parametermodell ↔ GlobalId | [@geier2022bimwood] |
| Knotenpunkte, Stoßstellen, Detailnachweise | nicht standardkonform abbildbar (Recherche 06) | eigene Psets und Dokumente | Verweis an den beteiligten Bauteilen | [@chateauvieux2023bim; @chateauvieuxhellwig2025schallschutz] |

Die letzte Zeile verdient eine Anmerkung. Für den Schallschutz im Holzbau schlagen Châteauvieux-Hellwig und Weise eine Schemaerweiterung und ein eigenes Datenschema für das Fachmodell Akustik vor [@chateauvieuxhellwig2025schallschutz]. Die Arbeit folgt dem nicht, weil eine Erweiterung die Prüfkette K2 verlassen würde. Sie übernimmt aber das Ergebnis der Stoßstellenanalyse [@chateauvieuxhellwig2022timber] als Nachweisdokument mit Verweis auf die GUIDs der beteiligten Bauteile.

**E8.23 – Versionen und Freigabestatus liegen in genau einer CDE.** *Entscheidung.* Jede freigegebene Revision ist eine unveränderliche Datei mit SHA-256-Prüfsumme in einer CDE nach ISO 19650. Der Status (in Arbeit, geteilt, veröffentlicht) wird dort geführt, nicht im IFC. Änderungen zwischen Revisionen werden über GlobalIds verglichen. *Begründung.* Ein Review nach PRISMA über 46 Dokumente mit 15 Experteninterviews benennt die parallele Nutzung mehrerer CDEs als Hauptproblem für Zurechenbarkeit, Transparenz und Verlässlichkeit [@jaskula2024common]. Inhaltliche und graphbasierte Vergleichsverfahren für IFC-Stände existieren [@shi2018ifcdiff; @esser2022graphbased]; ein Vergleich über GlobalIds ist schon früh als automatisierbarer Test vorgeschlagen worden [@ma2006testing]. Mit deterministischen GlobalIds reduziert sich der Vergleich auf den Abgleich zweier Mengen [U, eigene Bewertung]. *Beleg.* Recherche 06 [V]; Zielbild, Prinzip 1.

**E8.24 – Dokumente werden verwiesen, nicht eingebettet; ihr Hash steht im Modell.** *Entscheidung.* Vertrag, Baubeschreibung, Ausstattungsfestlegung, Nachweishefte (Kapitel 7a) und Datenblätter sind eigenständige Dateien. Das Modell verweist auf sie über `IfcDocumentReference` und `IfcDocumentInformation` (Revision, ValidFrom, ValidUntil) und speichert ihren SHA-256-Wert in einem eigenen Property. Freigaben sind `IfcApproval`. Signiert wird auf Dateiebene. *Begründung.* IFC hat keine Signatur. Die Signatur einer IFC-Datei mit qualifizierter elektronischer Signatur ist im CHEK-Projekt als Prototyp umgesetzt: Hash der Datei, Signatur über einen Vertrauensdiensteanbieter, Zeitstempel, eingebetteter Umschlag [@alfaro2025chek]. Signaturen auf Objektebene sind dagegen Forschungsstand; offen sind IFC-Struktur, Langzeitprüfbarkeit und Teiländerungen [@fakour2025exploring]. Container nach ISO 21597, die IFC und verknüpfte Dokumente bündeln, sind eine standardisierte Alternative für die Übergabe [@hagedorn2023semantic; @liu2023definition]. *Beleg.* Recherche 06 und 23. Der Hash belegt Unverändertheit, keine Urheberschaft (Kapitel 7a.5).

**E8.25 – Prüfergebnisse und Rückfragen gehen als BCF zurück.** *Entscheidung.* Jede Meldung der Regelmaschine, jede IDS-Verletzung und jede Antwort auf einen Aussparungsvorschlag ist ein BCF-Thema mit Viewpoint und den GlobalIds der betroffenen Komponenten. BCF ist das Kommunikations-, IFC das Modellformat. *Begründung.* Prüfergebnisse sind Aussagen *über* das Modell, nicht Teil davon. Ein mvdXML-basierter Prüfer mit BCF-Berichten ist bereits früh beschrieben [@zhang2015interoperable]; das deutsche Projekt zum BIM-basierten Bauantrag nutzt BCF-Vorgänge für Abweichungsanträge [@bimbauantrag2020abschluss]. `IfcConstraint` würde das Modell mit Aussagen füllen, die kaum eine Software auswertet (Recherche 06). *Beleg.* Recherche 06 und 16 [U, Konvention]. Im Prototyp sind BCF-Themen noch nicht erzeugt; die Prüfberichte liegen als JSON, Markdown und HTML vor (B2).

**E8.26 – Exporte werden abgeleitet, nie bearbeitet, und tragen die GlobalId ihrer Quelle.** *Entscheidung.* BTLx, WUP, GAEB, XBau, PDF-Bauvorlagen, glTF und der IFC4-Export entstehen automatisch aus dem Modell bzw. dem Parametermodell. Jeder Export trägt je Objekt die IFC-GlobalId seiner Quelle, in BTLx als `UserAttribute`. Wo ein Format kein Freitextfeld hat, entsteht eine Zuordnungstabelle neben dem Export. *Begründung.* Nur so lässt sich eine Bearbeitung an der Maschine auf das Bauteil, den Nachweis und die Freigabe zurückführen. *Beleg.* **Befund [V]:** B15 schreibt die GlobalId der Fallleitung als `UserAttribute Name="LeitungGUID"` an jede Bohrung. B7 dagegen setzt die `Transformation GUID` jedes Holzes auf `uuid5(Namensraum, "btlx:" + Pfad)`. Diese GUID ist aus demselben Pfad abgeleitet und damit reproduzierbar, aber **nicht** gleich der IFC-GlobalId des Holzes. Die Rückverfolgung gelingt dort nur über den Pfad. B7 ist deshalb nachzurüsten. Für WUP wurde kein dokumentiertes Freitextfeld gefunden (Recherche 16) [U]. Beim glTF-Export aus IfcOpenShell gehen Texturen und UV-Koordinaten verloren (Recherche 09 und 10) [V]; auch dieser Export braucht einen eigenen Schritt.

### 8.6.2 Deterministische GlobalIds

Die Rückverfolgbarkeit hängt an der Identität der Objekte. In IFC ist das die GlobalId, ein 128-Bit-Wert, komprimiert auf 22 Zeichen. Werkzeuge vergeben sie üblicherweise zufällig. Für ein erzeugtes Modell hat das eine unerwünschte Folge: Jeder Lauf des Generators erzeugt neue GUIDs, auch wenn sich nichts geändert hat. Versionsvergleich, Nachweisverweise und BCF-Themen würden bei jedem Lauf ungültig.

**Das Schema in B1.** B1 bildet jede GlobalId als namensbasierte UUID der Version 5 (SHA-1) aus einem festen Namensraum und dem Pfad des Objekts im Parametermodell:

```text
GlobalId = compress( uuid5( NAMENSRAUM, pfad ) )
NAMENSRAUM = 6f1c3b0e-8a52-5d7e-9c4b-2a1d0e7f4b10   (einmalig erzeugt, im Code fixiert)
```

Beziehungen, Psets und Mengen erhalten Pfade, die aus dem Pfad ihres Bezugsobjekts abgeleitet sind. Die folgende Tabelle zeigt Pfade und die daraus berechneten GlobalIds; jede wurde gegen `wandelement.ifc` geprüft [V]:

| Pfad im Parametermodell | Objekt | GlobalId |
|---|---|---|
| `/projekt` | `IfcProject` | `3n9mhceD9U_ez8SJ26bpTm` |
| `/wand` | `IfcWall` | `0gsiGQj_bG3wx8M0qwRA0U` |
| `/wand/schwelle` | `IfcMember` PLATE | `3N9BxbmVjJqfMasIm6VCTu` |
| `/wand/staender/rand/links` | `IfcMember` STUD | `0ruebnGhrPUPaN5fsim6Vf` |
| `/wand/kerven/K1` | `IfcVoidingFeature` NOTCH | `2wzspq7qPLDQOqcQt$qavq` |
| `/wand/kerven/K1#schneidet` | `IfcRelVoidsElement` | `26reED$iDQSQquU8q9MZLr` |
| `/wand#aggregiert` | `IfcRelAggregates` | `3H$X1wKCnSyfz6MaSj_7C9` |
| `/typen/verbindungsmittel/osb_staender` | `IfcMechanicalFastenerType` | `10kcZK2DzMauPxIfg5Yrjt` |

Nach dem Aufbau vergibt eine Funktion allen `IfcRoot`-Instanzen ihre GUID und bricht ab, wenn ein Pfad doppelt vorkommt. Eine Kollision ist damit nicht nur unwahrscheinlich, sondern ausgeschlossen, solange Pfade eindeutig sind.

**Befunde zur Reproduzierbarkeit [V].** Die Tests in `tests/test_b1_wandelement.py` belegen drei Eigenschaften:

1. **Byte-Identität.** Zwei Läufe erzeugen dieselbe Datei, auch in getrennten Prozessen mit `PYTHONHASHSEED` 1 und 4711 (SHA-256 `5a796ea7…f8bb478b`). Dieselbe Eigenschaft zeigen B16, B17 (`d548ea48…`) und B18 (`e4d8de10…`).
2. **Stabilität gegenüber Änderungen.** Wird die Brüstungshöhe von 900 auf 850 mm geändert, behalten Wand, Rasterständer, Schwelle, Rähm und Brüstungsriegel ihre GlobalId.
3. **Unabhängigkeit von Bibliotheksinterna.** Mit den Funktionen `aggregate.assign_object`, `unit.assign_unit`, `type.assign_type` und `material.assign_material` von `ifcopenshell.api` entstanden zunächst vier verschiedene Prüfsummen bei vier Hash-Seeds, weil die Funktionen über Python-Mengen iterieren. B1 legt die Beziehungen deshalb direkt und mit fester Listenreihenfolge an. Zeitstempel kommen aus dem Parametermodell, nicht aus der Uhr.

**Kritische Würdigung.** Das Schema hat zwei Schwächen, die B1 noch nicht behebt:

- **Globale Eindeutigkeit.** Der Namensraum ist für alle Projekte derselbe. Zwei Projekte mit einem Objekt am Pfad `/wand` erhielten dieselbe GlobalId. Innerhalb einer Datei ist das unschädlich, in einer CDE mit vielen Projekten aber nicht. Die GlobalId soll global eindeutig sein.
- **Identität ist Pfadsemantik.** Ein Rasterständer heißt `/wand/staender/raster/3`, weil er an der dritten Rasterposition steht. Ändert sich das Achsmaß, bleibt die GUID, aber der Ständer steht an anderer Stelle. Das ist gewollt, wenn „der dritte Rasterständer“ fachlich dasselbe Objekt ist. Ändert sich die Pfadstruktur des Parametermodells, ändern sich dagegen alle GUIDs darunter, obwohl sich am Gebäude nichts geändert hat.

**E8.27 – Die GlobalId ist `uuid5(Projektnamensraum, Pfad)`; der Pfad ist Teil der Schnittstelle.** *Entscheidung.* Der Namensraum wird je Projekt abgeleitet: `uuid5(Firmennamensraum, Projektkennung)`. Pfade sind eine versionierte Schnittstelle des Parametermodells. Eine Änderung der Pfadstruktur ist eine Schemamigration mit Zuordnungstabelle alt → neu, die in der CDE abgelegt wird. Innerhalb eines Pfades stehen stabile Kennungen (`F1`, `K1`, `osb_staender`) vor Indizes. *Begründung.* Die Ableitung je Projekt stellt globale Eindeutigkeit her, ohne den Determinismus aufzugeben. Die Pfadversionierung macht die zweite Schwäche beherrschbar. *Beleg.* B1 [V] für das Grundschema; Projektnamensraum und Pfadversionierung sind Entwurf [U]. Die Nachweisführung (Kapitel 7a.5) verweist bereits auf GlobalId und Dateiprüfsumme und profitiert unmittelbar von der Stabilität.

**E8.28 – Byte-Reproduzierbarkeit ist ein Abnahmekriterium des Generators.** *Entscheidung.* Jede Änderung am Generator muss nachweisen, dass gleiche Eingaben bei gleicher Umgebung (Python 3.11.15, IfcOpenShell 0.8.5, `requirements-lock.txt`) byte-identische Dateien ergeben, auch unter verschiedenen Hash-Seeds. *Begründung.* Nur dann belegt eine Prüfsumme die fachliche Aussage „dieses Modell, geprüft nach Profil *P* in Version *v*“. Ohne Reproduzierbarkeit misst der Hash die Laufzeitumgebung. Die Bedingung entspricht den Grundsätzen für zitierfähige und nachnutzbare Forschungssoftware [@smith2016softwarecitation; @barker2022fair4rs]. *Beleg.* B1, B16, B17, B18 [V]; Kapitel 7a.5 kommt für Nachweise zum gleichen Ergebnis (Zahlen-Normalform).

### 8.6.3 Die Kette der Rückverfolgbarkeit

Mit E8.23 bis E8.28 entsteht eine lückenlose Kette von der Kundenentscheidung bis zur Maschine:

1. Das **Parametermodell** (JSON) hält die Entscheidung, etwa die Brüstungshöhe von F1.
2. Der **Pfad** (`/wand/oeffnungen/F1/…`) benennt jedes erzeugte Objekt.
3. Die **GlobalId** folgt deterministisch aus Projektnamensraum und Pfad.
4. Die **IFC-Datei** hat eine Prüfsumme und liegt als Revision in der CDE.
5. Jeder **Nachweis** verweist auf GlobalId und Dateiprüfsumme und hat selbst einen Hash (Kapitel 7a).
6. Jede **Freigabe** ist ein `IfcApproval`, jedes signierte Dokument ein Verweis mit Hash.
7. Jeder **Export** trägt je Objekt die GlobalId (E8.26).

In umgekehrter Richtung beantwortet die Kette die Frage, die Produkthaftung und Prüfverfahren stellen (Kapitel 4.8): Aus welcher Entscheidung, nach welcher Regel und mit welcher Freigabe ist diese Bohrung in diesem Ständer entstanden? Belegt ist sie heute für die Glieder 1 bis 5. Die Glieder 6 und 7 sind für B15 umgesetzt, für B7 nachzurüsten, für Signatur und CDE Entwurf.

## 8.7 Zwischenfazit

Das Kapitel beantwortet FF1 für das Informationsmodell mit drei Aussagen.

1. **IFC4X3_ADD2 trägt die Holzrahmenwand bis zum Verbindungsmittel und fast jede Phase der Kette ohne Schemaerweiterung.** Tabelle 8.2 und Listing 8.1 zeigen das Mapping an einem erzeugten, validierten und byte-reproduzierbaren Modell mit 217 Teilen. Tabelle 8.3 zeigt für 22 Phasen und Teilgebiete, dass die Grenzen mit USERDEFINED, eigenen Psets und standardisierten Nachbarformaten überbrückt werden. Sechs Teilmodelle (B14 bis B19) sind validiert.
2. **„Standardkonform“ ist eine Prüfkette, keine MVD.** Weil für IFC 4.3 keine passende MVD existiert, definiert die Arbeit Konformität über Schema, normative Regeln, IDS und Regelmaschine (E8.2). Die Kette macht eigene Konventionen sichtbar, statt sie hinter einer vermeintlichen Sicht zu verbergen.
3. **Die Redundanz ist gewollt und kontrolliert.** Schichtenmodell und Einzelteile stehen nebeneinander, weil Autorensoftware die Aggregation nicht liest [@timbim2024]. Sie entstehen aus einer Quelle, und maßgebliche Kennwerte werden aus den Einzelteilen berechnet. Das U-Wert-Beispiel zeigt, dass die Wahl der Sicht den Nachweis um rund 13 % verschiebt.

These 3 der Arbeit („IFC 4.3 trägt die Kette bis zur Werkplanung vollständig“) wird damit präzisiert: Das Schema trägt die Kette. Maschinendaten, Versionen, Signaturen und Prüfergebnisse liegen nachweislich außerhalb und sind über GlobalIds angebunden.

**Offen und für Kapitel 20 vorzumerken:**

- Prüfung aller Beispiele mit dem buildingSMART Validation Service (K2), insbesondere der Aggregation von Coverings und von Elementen ohne Geometrie,
- Round-Trip in Fremdsoftware (hsbcad, cadwork, ein Viewer) für Layer-Set und Aggregation,
- IFC4-Export mit Verlustprotokoll (E8.3),
- ein zusammenhängendes Hausmodell, das alle Zeilen der Tabelle 8.3 zugleich enthält,
- Vereinheitlichung der Pset-Präfixe und des ObjectType-Vokabulars (E8.15, E8.21) sowie deren Veröffentlichung im bSDD,
- GlobalId in jedem Export (E8.26) und Projektnamensraum (E8.27),
- Sturz als `IfcBeam` LINTEL (E8.6) und `GrossWeight` je Element (E8.11),
- IFC-Ausgabe für B20.

## Verwendete Schlüssel

Das Kapitel zitiert 51 Schlüssel. Alle stammen aus `literatur/lit-*.bib`. Für die bekannten Dubletten sind die führenden Schlüssel verwendet (`iso2024ifc` statt `iso16739-2024`, `bsi2024ids` statt `ids2024`, siehe `literatur/KORREKTUREN.md`).

`abualdenien2019metamodel`, `abualdenien2022levels`, `akbas2025holistic`, `alfaro2025chek`, `alwisy2019bim`, `barker2022fair4rs`, `bazjanac2010space`, `bimbauantrag2020`, `bimbauantrag2020abschluss`, `bimportal`, `bsi2024ids`, `bsi2025validation`, `bsiMvd43`, `bsiValidation`, `btlx23`, `chateauvieux2023bim`, `chateauvieuxhellwig2022timber`, `chateauvieuxhellwig2025schallschutz`, `chek2024d22`, `compastimber`, `darwish2022automated`, `dataholz`, `din18290-2`, `dineniso7817-1`, `eastman2010exchange`, `elsibaii2025open`, `esser2022graphbased`, `fakour2025exploring`, `fischer2024extending`, `fonsati2026leveraging`, `geier2022bimwood`, `hagedorn2023semantic`, `iso19650`, `iso2024ifc`, `iso23387`, `iso6946_2017`, `jaskula2024common`, `jaud2020georeferencing`, `jaud2022georeferencing`, `krijnen2020efficient`, `laakso2012ifc`, `lai2018interoperability`, `liu2016ontology`, `liu2023definition`, `ma2006testing`, `mattern2018bimbased`, `moult2020compliance`, `nrw2026bimbauantrag`, `oekobaudat`, `orozco2023codesign`, `pazlar2008interoperability`, `ramaji2016product`, `ramaji2017extending`, `ramaji2017product`, `shi2018ifcdiff`, `smith2016softwarecitation`, `standtke2024etim`, `timbim2024`, `tomczak2022review`, `tugraz2025syswood`, `vanberlo2021future`, `venugopal2012semantics`, `zhang2015interoperable`, `zvdh2024`

### Python-Key-Check

```python
import re, glob, pathlib
text = pathlib.Path("08-informationsmodell.md").read_text(encoding="utf-8")
body = text.split("## Verwendete Schlüssel")[0]
cited = set(re.findall(r"@([A-Za-z0-9_\-:]+)", body))
bib = set()
for f in glob.glob("literatur/lit-*.bib"):
    bib |= set(re.findall(r"^@\w+\{([^,\s]+),", open(f, encoding="utf-8").read(), re.M))
print(len(cited), "zitiert;", "fehlend:", sorted(cited - bib) or "keine")
```

Ergebnis (27.09.2026, aus `arbeit/` ausgeführt): siehe unten.

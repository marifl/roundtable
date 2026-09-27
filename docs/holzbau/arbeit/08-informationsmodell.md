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

**Form der Entscheidungen.** Designentscheidungen sind als E8.1 bis E8.28 nummeriert. Jede nennt die Entscheidung, die Begründung und den Beleg. Kapitel 9 (Regelraum), 11 (Reifegrade) und 20 (Evaluation) verweisen auf diese Nummern. Abschnitt 8.8 übersetzt die Entscheidungen in Umsetzungsvorgaben für die App: Anforderungen ANF-08-01 bis ANF-08-31 mit prüfbarem Abnahmekriterium, die vollständige Mapping-Tabelle (zugleich `spezifikation/ifc-mapping.csv`) und die GUID-Regel.

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

Der Befund ist ein Warnsignal, kein Gegenbeweis. Ein Modell *nur* mit Aggregation ist für viele Programme unvollständig. Die Fertigung braucht aber die Einzelteile, weil Maschinendaten, Stücklisten und Mengen je Holz erzeugt werden [@alwisy2019bim; @liu2016ontology; @darwish2022automated].

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

**Befund 3: Die Fallen liegen in der Schemaversion [V].** `IfcElectricDistributionBoard`, `IfcRelConnectsPortToElement` und das Proxy mit PROVISIONFORVOID sind in 4.3 deprecated (Recherche 08). Erst in den Beispielen fielen zwei EXPRESS-Regeln auf: Typ-Psets hängen über `HasPropertySets` am Typ, nicht über `IfcRelDefinesByProperties`, und jede Achse mit Axis braucht eine RefDirection (B15). Solche Fehler fängt nur eine Validierung jeder Revision (E8.2).

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

Die Schweizer Plattform Wald & Holz 4.0 beschreibt Produktdaten nach ETIM und BMEcat auch für die Holzbranche [@standtke2024etim] (graue Literatur, Jahr erschlossen [U]); das stützt die Wahl von ETIM, ohne sie zu belegen.

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

**Offen und für Kapitel 20 vorzumerken** sind vor allem die Prüfung mit dem Validation Service (K2), der Round-Trip in Fremdsoftware, der IFC4-Export, ein zusammenhängendes Hausmodell über alle Zeilen der Tabelle 8.3, die Vereinheitlichung von Pset-Präfixen und ObjectType-Vokabular, die GlobalId in jedem Export, der Projektnamensraum, der Sturz als `IfcBeam` LINTEL, `GrossWeight` je Element und eine IFC-Ausgabe für B20. Abschnitt 8.8 macht daraus und aus E8.1 bis E8.28 prüfbare Anforderungen an die Implementierung.

## 8.8 Umsetzungsvorgaben für die App

Die Arbeit ist die fachliche Grundlage einer App, die am Ende voll funktionieren soll. Dieser Abschnitt übersetzt die Entscheidungen E8.1 bis E8.28 deshalb in Vorgaben, nach denen ein Entwickler den IFC-Generator und seine Prüfschicht direkt implementieren kann. Er besteht aus vier Teilen: den Anforderungen mit Abnahmekriterium (8.8.1), der vollständigen Mapping-Tabelle (8.8.2), der GUID-Regel (8.8.3) und dem ObjectType-Vokabular (8.8.4).

**Verbindlichkeit.**

- **Muss** heißt: freigabeblockierend. Ein Build, der das Abnahmekriterium verfehlt, darf kein Modell an Kunden, Behörde oder Werk ausliefern.
- **Soll** heißt: umzusetzen. Eine Abweichung ist nur mit schriftlicher Begründung im Änderungsprotokoll zulässig.

**Form der Abnahmekriterien.** Jedes Kriterium ist als automatisierbarer Testfall formuliert. Referenzdaten sind die Beispiele B1, B2 und B14 bis B19 in `beispiele/`. Die Anforderungen sind zur Übernahme in `spezifikation/anforderungen.csv` bestimmt; die Mapping-Tabelle liegt maschinenlesbar in `spezifikation/ifc-mapping.csv`.

### 8.8.1 Anforderungen

| ID | Prio | Anforderung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-08-01 | Muss | Jede erzeugte Datei schreibt `FILE_SCHEMA(('IFC4X3_ADD2'))` und `FILE_DESCRIPTION(('ViewDefinition [NotAssigned]'),'2;1')`. | E8.1, E8.2 | Für jede Ausgabe gilt `ifcopenshell.open(p).schema_identifier == "IFC4X3_ADD2"`, und die Header-Beschreibung ist genau `('ViewDefinition [NotAssigned]',)`. |
| ANF-08-02 | Muss | Jede Revision wird gegen Schema und EXPRESS-Regeln geprüft (Stufe K1). | E8.2; B1 | `ifcopenshell.validate.validate(f, json_logger(), express_rules=True)` ergibt 0 Meldungen. |
| ANF-08-03 | Muss | Vor jeder Freigabe wird mit dem buildingSMART Validation Service geprüft (K2), als Dienst oder lokal aus dem Open-Source-Code betrieben. | E8.2; [@bsi2025validation] | Der Bericht meldet 0 Fehler in Syntax, Schema und normativen Regeln. Warnungen (Industry Practices) stehen einzeln im Freigabeprotokoll. |
| ANF-08-04 | Muss | Je Freigabe-Gate und Reifegrad wird eine IDS geprüft (K3). `beispiele/holzrahmenbau.ids` ist das Basisprofil. | E8.2; B2 | ifctester meldet für alle Spezifikationen des Gates „bestanden“. Negativtest: `ausgabe/wandelement_fehlerhaft.ifc` verfehlt genau HRB-01, 03, 05, 08, 09 und 11. |
| ANF-08-05 | Muss | Kein `IfcBuildingElementProxy`. Hat eine Klasse das Attribut PredefinedType, ist es gesetzt und nicht NOTDEFINED. USERDEFINED ist nur mit einem ObjectType aus dem Vokabular 8.8.4 zulässig. | E8.6, E8.15 | Anzahl `IfcBuildingElementProxy` = 0. Für jedes `IfcElement` und `IfcElementType` mit PredefinedType gilt: Wert ∉ {leer, NOTDEFINED}; bei USERDEFINED ist ObjectType bzw. ElementType ∈ Vokabular. |
| ANF-08-06 | Muss | In IFC 4.3 deprecated Konstrukte werden nicht geschrieben: `IfcElectricDistributionBoard`, `IfcRelConnectsPortToElement`, Proxy mit PROVISIONFORVOID, die Zahlenattribute von `IfcStairFlight`, `IfcSurfaceTexture.Parameter`. | R08, R10, R13 | Anzahl der genannten Klassen = 0; die genannten Attribute sind leer; Treppenwerte stehen in `Pset_StairFlightCommon`. |
| ANF-08-07 | Muss | Jedes vorgefertigte Element ist `IfcWall` ELEMENTEDWALL, `IfcSlab` oder `IfcRoof` mit genau einer `IfcRelAggregates` zu seinen Teilen. Wand- und Deckenelemente tragen zusätzlich `IfcMaterialLayerSetUsage`. Das Wandelement hat nur eine Axis-Repräsentation. | E8.5, E8.10 | Je Element `len(IsDecomposedBy) == 1`; Materialzuordnung ist `IfcMaterialLayerSetUsage`; \|Σ LayerThickness − `Qto_WallBaseQuantities.Width`\| ≤ 0,01 mm. |
| ANF-08-08 | Muss | Jedes Teil eines Elements (`IfcMember`, `IfcBeam`, `IfcPlate`, `IfcBuildingElementPart`, `IfcMechanicalFastener`) hängt an genau einem Element. | E8.5 | IDS HRB-07 besteht; kein Teil hat 0 oder mehr als 1 `Decomposes`. |
| ANF-08-09 | Muss | Das tesselierte Volumen jedes Teils ist gleich seinem Qto NetVolume. | E8.8, E8.10 | Abweichung < 10⁻⁹ m³ für alle Teile, wie im Test von B1. |
| ANF-08-10 | Muss | Stabbearbeitungen sind `IfcVoidingFeature` mit `IfcRelVoidsElement`. Der Abzugskörper steht an freien Seiten 1 mm über. | E8.8 | NetVolume des Stabs = Bruttovolumen − Bearbeitungsvolumen; das tesselierte Volumen nach Boolescher Auswertung stimmt damit überein (Regressionswert Ständer R1: 0,03150 m³). |
| ANF-08-11 | Muss | Verbindungsmittel haben einen Typ. NominalDiameter und NominalLength stehen an Typ und Exemplar. Die Körpergeometrie ist ein `IfcMappedItem`, dessen MappingSource in den `RepresentationMaps` des Typs liegt. | E8.9 | IDS HRB-08 und HRB-09 bestehen; für jedes `IfcMechanicalFastener` gilt MappingSource ∈ Typ.RepresentationMaps. |
| ANF-08-12 | Muss | U-Wert, Masse und Mengen werden aus der Einzelteilgeometrie berechnet und in `Pset_WallCommon.ThermalTransmittance` bzw. `Qto_*BaseQuantities` geschrieben. Ab Reifegrad A trägt jedes Element `GrossWeight`. | E8.11; B3; R19 | U-Wert = Rechenkern B3 (Variante Geometrie) ± 0,001 W/(m²K); `GrossWeight` = Σ MassDensity · NetVolume der Teile ± 0,1 %. |
| ANF-08-13 | Muss | Eigene Psets tragen nur das Präfix `HRB_`. Namen mit `Pset_` oder `Qto_` sind nur zulässig, wenn sie im Template IFC4X3 existieren; in Standard-Psets stehen nur Template-Properties. | E8.21 | Jeder Name von `IfcPropertySet` und `IfcElementQuantity` passt auf `^(Pset_\|Qto_\|HRB_)`; jeder `Pset_`-/`Qto_`-Name wird von `ifcopenshell.util.pset.PsetQto("IFC4X3").get_by_name()` gefunden. |
| ANF-08-14 | Muss | Typ-Psets hängen über `HasPropertySets` am Typ, nie über `IfcRelDefinesByProperties`. | R16; B15 | Keine `IfcRelDefinesByProperties` enthält ein `IfcTypeObject` in RelatedObjects. |
| ANF-08-15 | Soll | Jede `HRB_`-Property hat eine bSDD-URI und ist über `IfcExternalReferenceRelationship` mit ihr verknüpft. | E8.21 | 100 % der `HRB_`-Properties haben einen Verweis; im Freigabelauf ist jede URI auflösbar. |
| ANF-08-16 | Muss | Ab Reifegrad R trägt jedes Bauteil eine DIN-276-Klassifikation mit gesetzter Edition. Produkte der Bemusterung tragen ETIM mit `IfcClassification.Specification` = bSDD-URI. Ungeprüfte Klassennummern werden nicht geschrieben. | E8.19 | IDS: jedes `IfcBuiltElement` hat eine Referenz auf DIN 276; jede ETIM-Referenz hat eine Location in der bSDD-Domäne und steht in der geprüften Nummernliste. |
| ANF-08-17 | Muss | Bemusterungsoptionen sind Typen einer `IfcProjectLibrary` (`IfcRelDeclares`). Die Wahl ist nur ein `IfcRelDefinesByType`. In Reifegrad A tragen gewählte Typen GTIN, Hersteller und Artikelnummer. | E8.14, E8.22 | Jeder Typ eines gewählten Produkts ist von genau einer Bibliothek deklariert; die GTIN hat 8, 12, 13 oder 14 Stellen mit gültiger Prüfziffer (Modulo 10). |
| ANF-08-18 | Muss | Genau ein `IfcProject` je Datei. Varianten stehen nicht als Gruppen im Modell. Jede Revision liegt unveränderlich mit SHA-256 in der CDE. | E8.13, E8.23 | Anzahl `IfcProject` = 1; SHA-256 der Datei = CDE-Eintrag; ein zweiter Schreibversuch auf dieselbe Revision wird abgewiesen. |
| ANF-08-19 | Muss | Dokumente sind `IfcDocumentReference` mit `HRB_Dokument.SHA256`. Freigaben sind `IfcApproval` mit Datum und Akteur. | E8.24 | Für jeden Verweis existiert die Datei, und ihr SHA-256 stimmt; jedes durchlaufene Freigabe-Gate hat ein `IfcApproval`. |
| ANF-08-20 | Soll | Prüfergebnisse aus IDS, Regelmaschine und Aussparungskoordination werden als BCF-Themen mit den GlobalIds der betroffenen Komponenten ausgegeben. | E8.25, E8.16 | Für jede Verletzung im Prüfbericht existiert ein BCF-Thema; jede GlobalId darin wird von `f.by_guid()` gefunden. |
| ANF-08-21 | Muss | Durchdringungen: Der Vorschlag ist `IfcVirtualElement` PROVISIONFORVOID ohne Material. Nach Annahme entstehen je durchdrungenem Teil ein `IfcOpeningElement` mit `IfcRelVoidsElement` und eine `IfcRelInterferesElements` (ImpliedOrder TRUE). | E8.16; B15 | Kein `IfcVirtualElement` hat eine Materialzuordnung; Anzahl Öffnungen = Anzahl durchdrungener Teile; Regressionswerte B15: 4 Vorschläge, 4 Öffnungen, 4 Voids, 4 Interferes, 1 Fills. |
| ANF-08-22 | Muss | Jeder Export trägt je Objekt die IFC-GlobalId. BTLx: `UserAttribute Name="IfcGlobalId"` an jedem `Part` und jeder Bearbeitung, `Transformation GUID` = UUID des IFC-Objekts (Regel G7). Formate ohne Freitextfeld (WUP) erhalten eine Zuordnungsdatei `export_guid.csv`. | E8.26 | Für jeden BTLx-Part existiert das Attribut, und `f.by_guid()` findet das Objekt; `uuid.UUID(transformation_guid).hex == ifcopenshell.guid.expand(global_id)`. |
| ANF-08-23 | Muss | GlobalIds werden nach der Regel 8.8.3 gebildet. | E8.27 | Die Regressionsvektoren in 8.8.3 stimmen; kein Pfad kommt doppelt vor; alle GlobalIds außerhalb des geänderten Teilbaums bleiben gleich, wenn ein Parameter geändert wird (Testfall: Brüstungshöhe 900 → 850 mm). |
| ANF-08-24 | Muss | Gleiche Eingabe und gleiche Umgebung ergeben eine byte-identische Datei. Der Zeitstempel kommt aus dem Parametermodell oder aus `SOURCE_DATE_EPOCH`, nie aus der Uhr. Beziehungen werden mit fester Listenreihenfolge angelegt, nicht über `ifcopenshell.api`-Funktionen, die über Mengen iterieren. | E8.28 | Zwei Läufe in getrennten Prozessen mit `PYTHONHASHSEED` 1 und 4711 ergeben denselben SHA-256; `header.file_name.time_stamp` = Eingabewert. |
| ANF-08-25 | Muss | Die Granularität folgt dem Reifegrad nach den Spalten P, R und A der Mapping-Tabelle. Teile, Verbindungsmittel, Bearbeitungen und Belagstücke entstehen erst in Reifegrad A. | E8.12 | IDS je Reifegrad besteht; in P und R existiert kein `IfcMechanicalFastener` und kein `IfcVoidingFeature`. |
| ANF-08-26 | Muss | Georeferenz über `IfcMapConversion` und `IfcProjectedCRS` mit Name `EPSG:25832`; Scale passt zur Längeneinheit. | B1 | Name = `EPSG:25832`; Scale = 0,001 bei mm; der Ursprung des Modells wird auf die Rechts- und Hochwerte des Parametermodells abgebildet. |
| ANF-08-27 | Muss | Einheiten: Länge mm, Fläche m², Volumen m³, Winkel rad, Masse kg, Temperatur K, in dieser Reihenfolge in `IfcUnitAssignment`. | B1 | `IfcUnitAssignment` enthält genau diese sechs Einheiten in dieser Reihenfolge. |
| ANF-08-28 | Muss | Das `IfcProject` trägt `HRB_Generator` mit GeneratorVersion, PfadschemaVersion, Namensraum (UUID), ParameterHash (SHA-256 des kanonischen Parameter-JSON) und den Regelwerk-Profilen mit Version. | E8.27; Kap. 7a | Das Pset ist vorhanden; ParameterHash = SHA-256 der kanonisierten Eingabe; Namensraum = `NS_PROJEKT` nach G1. |
| ANF-08-29 | Soll | Ein IFC4-Export wird aus dem Parametermodell erzeugt und protokolliert seine Verluste. | E8.3 | Die IFC4-Datei besteht K1 mit 0 Meldungen; das Protokoll listet jedes Objekt, dessen Klasse oder Enum-Wert in IFC4 fehlt (Tabelle 8.1.1). |
| ANF-08-30 | Soll | Der glTF-Export überträgt Texturen und UV-Koordinaten in einem eigenen Schritt. | R09, R10 | Die GLB enthält `images`, `textures` und `TEXCOORD_0` für jedes Material mit `IfcImageTexture`. |
| ANF-08-31 | Muss | Das Klassenmapping ist Konfiguration, nicht Code: Der Generator liest `spezifikation/ifc-mapping.csv`. Die CSV wird in der CI gegen das Schema geprüft. | E8.3 | Das Prüfskript meldet 0 Fehler: Jede Klasse, jeder PredefinedType und jedes Standard-Pset der CSV existiert in IFC4X3_ADD2; jedes eigene Pset beginnt mit `HRB_`. |

### 8.8.2 Mapping-Tabelle

Die Tabelle 8.4 ist die verbindliche Zuordnung von Bauteil zu IFC-Klasse, PredefinedType, ObjectType, Beziehungen und Psets. Sie ist identisch mit `spezifikation/ifc-mapping.csv` und wurde aus ihr erzeugt.

**Spalten und Codes.**

- `predefined_type`, `object_type`: Mehrere zulässige Werte sind durch `|` getrennt. Leer heißt: Die Klasse hat kein PredefinedType, oder der Wert ist frei.
- `psets`: durch `|` getrennt. Ein Suffix `@R` oder `@A` heißt „Pflicht ab Reifegrad R bzw. A“. Ohne Suffix ist das Pset Pflicht ab dem ersten Reifegrad, in dem das Objekt Pflicht ist.
- `pflicht_reifegrad_P/R/A`: **M** = das Objekt muss mit den Psets erzeugt werden; **O** = optional; **-** = wird in diesem Reifegrad nicht erzeugt. Die Zuordnung zu den Reifegraden ist ein Vorschlag nach E8.12 und Recherche 10. Verbindlich wird sie mit Kapitel 11.
- `status`: **V** = am Schema oder in einem Beispiel geprüft; **U** = Konvention oder Vorschlag; **V/U** = Klasse geprüft, Konvention offen.
- `quelle`: R = Recherche, B = Beispiel, E = Entscheidung dieses Kapitels.

**Prüfung [V].** Ein Skript hat alle 116 Zeilen am 27.09.2026 gegen IfcOpenShell 0.8.5 geprüft: Jede Klasse existiert in IFC4X3_ADD2, jeder PredefinedType ist ein Wert des zugehörigen Enums, jedes `Pset_`- und `Qto_`-Set existiert im Template IFC4X3, und jedes eigene Pset trägt das Präfix `HRB_`. Ergebnis: 0 Fehler. Nicht geprüft ist, ob jede genannte Beziehung für die Klasse zulässig ist. Das deckt ANF-08-02 bei jeder erzeugten Datei ab.

**Umbenennung der Prototyp-Psets (E8.21).** Die Beispiele sind bei der nächsten Überarbeitung umzustellen:

| bisher | neu | Beispiel |
|---|---|---|
| `B14_Fussbodenaufbau`, `B14_Rinne` | `HRB_Fussbodenaufbau`, `HRB_Rinne` | B14 |
| `B15_Durchdringung`, `B15_Manschette` | `HRB_Durchdringung`, `HRB_Manschette` | B15 |
| `HP_Verlegung`, `HP_Fliesenstueck`, `HP_Fliese`, `HP_Verziehung` | `HRB_Verlegung`, `HRB_Fliesenstueck`, `HRB_Fliese`, `HRB_Verziehung` | B16, R13 |
| `B17_Entwaesserung`, `B17_Versickerung` | `HRB_Entwaesserung`, `HRB_Versickerung` | B17 |
| `HB_Schallschutz_Bauteil`, `HB_Aussenlaerm_Raum`, `HB_Fassadenpegel` | `HRB_Schallschutz_Bauteil`, `HRB_Aussenlaerm_Raum`, `HRB_Fassadenpegel` | B19 |
| `Pset_Holzbau_WPSchall` (Vorschlag) | `HRB_WPSchall` | R22 |

`HRB_Feuchteschutz`, `HRB_Kranhub`, `HRB_Kranaufstellung` und `HRB_Montage` bleiben unverändert.

**Tabelle 8.4: Vollständiges Klassen- und Pset-Mapping (= `spezifikation/ifc-mapping.csv`)**

| bauteil | ifc_klasse | predefined_type | object_type | beziehung | psets | pflicht_reifegrad_P | pflicht_reifegrad_R | pflicht_reifegrad_A | status | quelle |
|---|---|---|---|---|---|---|---|---|---|---|
| Projekt | IfcProject |  |  | IfcRelAggregates -> IfcSite; IfcRelDeclares -> Typen; IfcUnitAssignment mm/m2/m3/rad/kg/K | HRB_Generator | M | M | M | V/U | Kap. 8.8.3; B1 |
| Georeferenz | IfcMapConversion |  | EPSG:25832 | IfcProjectedCRS; SourceCRS = Modellkontext; Scale = 0.001 bei mm |  | M | M | M | V | B1; jaud2020georeferencing |
| Grundstück | IfcSite |  |  | IfcRelAggregates <- IfcProject; IfcRelAggregates -> IfcBuilding | Pset_SiteCommon\|HRB_Grundstueck@R | M | M | M | V/U | R06; R14; B1 |
| Flurstück | IfcSite |  | Flurstueck | IfcRelAggregates <- IfcSite (Grundstück) | HRB_Flurstueck | O | M | M | U | R06; R14 |
| Gebäude (je DHH-/RH-Einheit) | IfcBuilding |  | Gebaeudetyp aus Vokabular | IfcRelAggregates -> IfcBuildingStorey | Pset_BuildingCommon\|HRB_Gebaeude@R | M | M | M | V | R14; E8.17 |
| Geschoss | IfcBuildingStorey |  |  | IfcRelContainedInSpatialStructure -> Bauteile | Pset_BuildingStoreyCommon | M | M | M | V | B1 |
| Raum | IfcSpace | SPACE\|PARKING\|EXTERNAL |  | IfcRelAggregates <- IfcBuildingStorey | Pset_SpaceCommon\|Pset_SpaceOccupancyRequirements\|Qto_SpaceBaseQuantities\|HRB_Wohnflaeche@R\|HRB_Aussenlaerm_Raum@R | M | M | M | V/U | R14; R20; B19 |
| Nutzungseinheit | IfcZone |  | Wohnung\|Gewerbe | IfcRelAssignsToGroup <- IfcSpace; IfcRelReferencedInSpatialStructure -> Geschoss | Pset_ZoneCommon | O | M | M | V | R14; E8.17 |
| Brand-/Rauchabschnitt | IfcSpatialZone | FIRESAFETY |  | IfcRelReferencedInSpatialStructure | Pset_SpatialZoneCommon\|HRB_Brandabschnitt | - | M | M | V/U | R14 |
| Raumbegrenzung 2. Ebene | IfcRelSpaceBoundary2ndLevel |  |  | IfcSpace <-> IfcWall/IfcSlab |  | - | O | O | V | R06; bazjanac2010space |
| Wandelement | IfcWall | ELEMENTEDWALL |  | IfcRelAggregates -> Teile (genau 1); IfcRelContainedInSpatialStructure -> Geschoss; IfcRelAssociatesMaterial -> IfcMaterialLayerSetUsage | Pset_WallCommon\|Qto_WallBaseQuantities\|HRB_Schallschutz_Bauteil@R\|HRB_Montage@A | M | M | M | V | B1; B18; E8.5 |
| Wandtyp | IfcWallType | ELEMENTEDWALL |  | IfcRelDefinesByType -> IfcWall; IfcRelAssociatesMaterial -> IfcMaterialLayerSet; IfcRelDeclares <- IfcProject |  | M | M | M | V | B1 |
| Baustoff | IfcMaterial |  |  | in IfcMaterialLayer und IfcRelAssociatesMaterial je Teil | Pset_MaterialCommon\|Pset_MaterialThermal\|Pset_MaterialWood | M | M | M | V | B1 |
| Ständer (Rand-, Raster-, Königs-, Sturzauflager-, Füllständer) | IfcMember | STUD | Randstaender\|Staender\|Koenigsstaender\|Sturzauflagerstaender\|Fuellstaender | IfcRelAggregates <- IfcWall | Pset_MemberCommon\|Qto_MemberBaseQuantities | - | O | M | V | B1; E8.6 |
| Schwelle, Rähm, Brüstungsriegel | IfcMember | PLATE | Schwelle\|Raehm\|Bruestungsriegel | IfcRelAggregates <- IfcWall | Pset_MemberCommon\|Qto_MemberBaseQuantities | - | O | M | V | B1 |
| Sturz | IfcBeam | LINTEL | Sturz | IfcRelAggregates <- IfcWall | Pset_BeamCommon\|Qto_BeamBaseQuantities | - | O | M | U | E8.6 (B1 noch IfcMember STUD) |
| Beplankung (GKF, OSB, Holzfaser) | IfcPlate | SHEET | Beplankung | IfcRelAggregates <- IfcWall; Ausschnitt im Profil (IfcArbitraryProfileDefWithVoids) | Pset_PlateCommon\|Qto_PlateBaseQuantities | - | O | M | V | B1; E8.8 |
| Gefachdämmung | IfcBuildingElementPart | INSULATION |  | IfcRelAggregates <- IfcWall; je Gefach ein Teil | Qto_BodyGeometryValidation | - | O | M | V | B1 |
| Dampfbremse, Folie | IfcBuildingElementPart | USERDEFINED | MEMBRANE | IfcRelAggregates <- IfcWall | HRB_Feuchteschutz\|Qto_BodyGeometryValidation | - | O | M | U | B1; E8.7 |
| Kerve, Bohrung, Fase, Gehrung | IfcVoidingFeature | NOTCH\|HOLE\|CHAMFER\|MITER\|CUTOUT\|EDGE |  | IfcRelVoidsElement -> IfcMember/IfcBeam; 1 mm Überstand |  | - | - | M | V | B1; E8.8 |
| Öffnung in Bauteil | IfcOpeningElement | OPENING\|RECESS |  | IfcRelVoidsElement -> IfcWall/IfcSlab; IfcRelFillsElement <- IfcWindow/IfcDoor |  | M | M | M | V | B1 |
| Fenster | IfcWindow | WINDOW |  | IfcRelFillsElement -> IfcOpeningElement; Typ in IfcProjectLibrary | Pset_WindowCommon\|HRB_Schallschutz_Bauteil@R\|Pset_ManufacturerTypeInformation@A | M | M | M | V | R10; R20; B19 |
| Tür | IfcDoor | DOOR |  | IfcRelFillsElement -> IfcOpeningElement; Typ in IfcProjectLibrary | Pset_DoorCommon\|Pset_ManufacturerTypeInformation@A | M | M | M | V | R13; R14 |
| Verbindungsmittel (Schraube, Nagel, Klammer) | IfcMechanicalFastener | SCREW\|NAIL\|STAPLE |  | IfcRelAggregates <- IfcWall; IfcRelDefinesByType <- Typ; Body = IfcMappedItem auf Typ-RepresentationMap; NominalDiameter/NominalLength redundant am Exemplar |  | - | - | M | V | B1; E8.9 |
| Verbindungsmitteltyp | IfcMechanicalFastenerType | SCREW\|NAIL\|STAPLE |  | IfcRelDeclares <- IfcProject; RepresentationMaps (1); NominalDiameter/NominalLength | Pset_ManufacturerTypeInformation\|HRB_Verbindungsmittel | - | - | M | V/U | B1; R01 |
| Deckenelement | IfcSlab | FLOOR |  | IfcRelAggregates -> Teile; IfcRelAssociatesMaterial -> IfcMaterialLayerSetUsage | Pset_SlabCommon\|Qto_SlabBaseQuantities\|HRB_Schallschutz_Bauteil@R\|HRB_Montage@A | M | M | M | V | R06; R14; B15; B18 |
| Deckenbalken | IfcBeam | JOIST |  | IfcRelAggregates <- IfcSlab | Pset_BeamCommon\|Qto_BeamBaseQuantities | - | O | M | V | R16; B15 |
| Wechsel, Stichbalken | IfcBeam | USERDEFINED | Wechsel\|Stichbalken | IfcRelAggregates <- IfcSlab | Pset_BeamCommon\|Qto_BeamBaseQuantities | - | O | M | V | R16; B15 |
| Dach | IfcRoof | GABLE_ROOF\|HIP_ROOF\|HIPPED_GABLE_ROOF\|PAVILION_ROOF\|SHED_ROOF\|MANSARD_ROOF\|GAMBREL_ROOF\|BUTTERFLY_ROOF\|FLAT_ROOF |  | IfcRelAggregates -> IfcSlab ROOF, IfcMember; IfcRelContainedInSpatialStructure -> Geschoss | Pset_RoofCommon | M | M | M | V | R09 |
| Dachfläche, Dachelement | IfcSlab | ROOF |  | IfcRelAggregates <- IfcRoof | Pset_SlabCommon\|Qto_SlabBaseQuantities\|HRB_Montage@A | M | M | M | V | R09; R19 |
| Sparren, Pfette, Kehlbalken, Stiel, Strebe | IfcMember | RAFTER\|PURLIN\|COLLAR\|POST\|STRUT |  | IfcRelAggregates <- IfcRoof bzw. IfcSlab ROOF | Pset_MemberCommon\|Qto_MemberBaseQuantities | - | O | M | V | R09 |
| Dachdeckung | IfcCovering | ROOFING |  | IfcRelCoversBldgElements <- IfcSlab ROOF; IfcMaterialLayerSet (Ziegel, Latte, Konterlatte) | Pset_CoveringCommon | M | M | M | V | R09; zvdh2024 |
| Unterdeckbahn | IfcCovering | MEMBRANE |  | IfcRelCoversBldgElements <- IfcSlab ROOF | Pset_CoveringCommon | - | O | M | V | R09 |
| First, Grat, Ortgang, Kehlblech, Eindeckrahmen | IfcDiscreteAccessory | FLASHING\|USERDEFINED | RIDGE\|HIP\|VERGE | IfcRelAggregates bzw. IfcRelNests an IfcCovering ROOFING |  | O | O | M | V/U | R09; E8.15 |
| Schneefang, Dachtritt, Sicherheitshaken | IfcDiscreteAccessory | USERDEFINED | SNOWGUARD\|ROOFSTEP\|SAFETYHOOK | IfcRelAggregates an IfcCovering ROOFING |  | - | O | M | U | R09; E8.15 |
| Dachfenster | IfcWindow | SKYLIGHT |  | IfcRelFillsElement -> IfcOpeningElement in IfcSlab ROOF | Pset_WindowCommon\|Pset_ManufacturerTypeInformation@A | M | M | M | V | R09 |
| Gaube | IfcElementAssembly | USERDEFINED | DORMER | IfcRelAggregates -> IfcRoof, IfcWall, IfcWindow |  | M | M | M | U | R09 |
| PV-Modul | IfcSolarDevice | SOLARPANEL |  | IfcRelAssignsToGroup -> IfcDistributionSystem POWERGENERATION | Pset_ManufacturerTypeInformation@A | M | M | M | V | R08; R09 |
| Wechselrichter | IfcTransformer | INVERTER |  | IfcRelAssignsToGroup -> IfcDistributionSystem | Pset_ManufacturerTypeInformation | - | O | M | V | R08; R09 |
| Batteriespeicher | IfcElectricFlowStorageDevice | BATTERY |  | IfcRelAssignsToGroup -> IfcDistributionSystem | Pset_ManufacturerTypeInformation | - | O | M | V | R08 |
| Dachrinne | IfcPipeSegment | GUTTER |  | IfcRelAssignsToGroup -> IfcDistributionSystem RAINWATER; Ports über IfcRelNests | Pset_PipeSegmentTypeGutter | O | M | M | V | R09 |
| Fallrohr | IfcPipeSegment | RIGIDSEGMENT |  | IfcRelAssignsToGroup -> IfcDistributionSystem RAINWATER | Pset_PipeSegmentTypeCommon | O | M | M | V | R09 |
| Rinnenkessel | IfcStackTerminal | RAINWATERHOPPER |  | IfcRelAssignsToGroup -> IfcDistributionSystem RAINWATER |  | - | O | M | V | R09 |
| Sanitärlüfter-Mündung | IfcStackTerminal | COWL |  | auf IfcPipeSegment VENT; IfcOpeningElement in IfcSlab ROOF |  | - | O | M | V | R08; R09 |
| TGA-System | IfcDistributionSystem | DOMESTICCOLDWATER\|DOMESTICHOTWATER\|SEWAGE\|WASTEWATER\|RAINWATER\|STORMWATER\|VENT\|VENTILATION\|HEATING\|ELECTRICAL\|LIGHTING\|DATA\|POWERGENERATION |  | IfcRelAssignsToGroup -> Elemente; IfcRelServicesBuildings -> IfcBuilding |  | - | M | M | V | R08; R18; B15; B17 |
| Stromkreis | IfcDistributionCircuit | ELECTRICAL |  | Untersystem von IfcDistributionSystem ELECTRICAL |  | - | M | M | V | R08 |
| Rohrleitung | IfcPipeSegment | RIGIDSEGMENT\|FLEXIBLESEGMENT |  | Ports über IfcRelNests; Typ-Pset über HasPropertySets | Pset_PipeSegmentTypeCommon\|Pset_PipeSegmentOccurrence | - | M | M | V | R08; R16; B15 |
| Luftkanal | IfcDuctSegment | RIGIDSEGMENT\|FLEXIBLESEGMENT |  | Ports über IfcRelNests | Pset_DuctSegmentTypeCommon | - | M | M | V | R08; R16 |
| Formteil Rohr | IfcPipeFitting | BEND\|JUNCTION\|TRANSITION\|CONNECTOR |  | Ports über IfcRelNests; IfcRelConnectsPorts |  | - | M | M | V | R08; B15; B17 |
| Anschlusspunkt | IfcDistributionPort | PIPE\|DUCT\|CABLE\|CABLECARRIER |  | IfcRelNests <- Element; IfcRelConnectsPorts <-> Port; FlowDirection SOURCE\|SINK | Pset_DistributionPortTypePipe | - | M | M | V | R08; R16; B15 |
| Leerrohr | IfcCableCarrierSegment | CONDUITSEGMENT |  | Ports über IfcRelNests | Pset_CableCarrierSegmentTypeConduitSegment | - | M | M | V | R08; R16 |
| Kabel | IfcCableSegment | CABLESEGMENT |  | IfcRelAssignsToGroup -> IfcDistributionCircuit |  | - | O | M | V | R08 |
| Installationsdose | IfcJunctionBox | POWER\|DATA |  | IfcRelContainedInSpatialStructure; Bearbeitung in Beplankung als IfcOpeningElement |  | - | M | M | V | R08 |
| Steckdose, Datendose | IfcOutlet | POWEROUTLET\|DATAOUTLET |  | IfcRelAssignsToGroup -> IfcDistributionCircuit | Pset_ManufacturerTypeInformation@A | M | M | M | V | R08 |
| Schalter | IfcSwitchingDevice | TOGGLESWITCH\|DIMMERSWITCH\|MOMENTARYSWITCH |  | IfcRelAssignsToGroup -> IfcDistributionCircuit | Pset_ManufacturerTypeInformation | M | M | M | V | R08 |
| Schutzgerät | IfcProtectiveDevice | CIRCUITBREAKER\|RESIDUALCURRENTCIRCUITBREAKER |  | IfcRelAggregates <- IfcDistributionBoard |  | - | O | M | V | R08 |
| Verteiler | IfcDistributionBoard | CONSUMERUNIT\|DISTRIBUTIONBOARD |  | Ports über IfcRelNests |  | - | M | M | V | R08 |
| Zähler | IfcFlowMeter | ENERGYMETER\|WATERMETER |  | IfcRelAssignsToGroup -> System |  | - | O | M | V | R08 |
| Leuchte | IfcLightFixture | POINTSOURCE\|DIRECTIONSOURCE |  | IfcRelAssignsToGroup -> IfcDistributionSystem LIGHTING | Pset_ManufacturerTypeInformation | M | M | M | V | R08 |
| Lüftungsgerät mit Wärmerückgewinnung | IfcAirToAirHeatRecovery | FIXEDPLATECOUNTERFLOWEXCHANGER |  | IfcRelAssignsToGroup -> IfcDistributionSystem VENTILATION | Pset_ManufacturerTypeInformation | - | M | M | V | R08 |
| Luftdurchlass, Außenluftdurchlass | IfcAirTerminal | DIFFUSER\|GRILLE\|LOUVRE |  | IfcRelAssignsToGroup -> IfcDistributionSystem VENTILATION | Pset_AirTerminalTypeCommon\|HRB_Schallschutz_Bauteil | O | M | M | V | R08; R20 |
| Heizkörper | IfcSpaceHeater | RADIATOR\|CONVECTOR |  | IfcRelAssignsToGroup -> IfcDistributionSystem HEATING | Pset_ManufacturerTypeInformation | M | M | M | V | R08 |
| Speicher | IfcTank | STORAGE |  | IfcRelAssignsToGroup -> System | Pset_TankTypeCommon | - | M | M | V | R08; R18 |
| Pumpe | IfcPump | CIRCULATOR\|SUMPPUMP\|SUBMERSIBLEPUMP |  | IfcRelAssignsToGroup -> System |  | - | O | M | V | R08; R18 |
| Armatur, Ventil | IfcValve | ISOLATING\|CHECK\|REGULATING\|MIXING |  | IfcRelAssignsToGroup -> System |  | - | O | M | V | R08; R18 |
| Wärmepumpe Monoblock | IfcUnitaryEquipment | USERDEFINED | AirToWaterHeatPump_Monoblock | IfcRelAssignsToGroup -> IfcDistributionSystem HEATING | Pset_UnitaryEquipmentTypeCommon\|Pset_SoundGeneration@R\|HRB_WPSchall@R\|HRB_Kaeltemittel@R | M | M | M | V/U | R22; E8.15 |
| Wärmepumpe Split-Außeneinheit | IfcUnitaryEquipment | SPLITSYSTEM |  | IfcRelAssignsToGroup -> IfcDistributionSystem HEATING | Pset_UnitaryEquipmentTypeCommon\|Pset_SoundGeneration@R\|HRB_WPSchall@R\|HRB_Kaeltemittel@R | M | M | M | V/U | R22 |
| R290-Schutzbereich | IfcSpatialZone | USERDEFINED | R290_Schutzbereich | IfcRelAssignsToProduct -> IfcUnitaryEquipment |  | - | M | M | U | R22; E8.15 |
| Wartungs- und Luftführungsbereich | IfcSpatialZone | RESERVATION |  | IfcRelAssignsToProduct -> IfcUnitaryEquipment |  | - | M | M | V/U | R22 |
| Sanitärobjekt | IfcSanitaryTerminal | TOILETPAN\|WASHHANDBASIN\|SHOWER\|BATH |  | IfcRelDefinesByType <- Typ aus IfcProjectLibrary; Ports über IfcRelNests am Typ | Pset_ManufacturerTypeInformation@A | M | M | M | V | R10; E8.14 |
| Bodenablauf, Duschrinne | IfcWasteTerminal | FLOORTRAP\|USERDEFINED | Duschrinne | IfcRelAssignsToGroup -> IfcDistributionSystem WASTEWATER | HRB_Rinne | M | M | M | V/U | R13; B14 |
| Aussparungsvorschlag | IfcVirtualElement | PROVISIONFORVOID |  | ohne Material; Tiefe >= Bauteildicke | Pset_ProvisionForVoid | - | M | O | V | R08; R16; B15; E8.16 |
| Freigegebene Durchdringung | IfcOpeningElement | OPENING |  | je durchdrungenem Teil IfcRelVoidsElement; IfcRelInterferesElements Leitung <-> Bauteil (ImpliedOrder TRUE) | HRB_Durchdringung | - | O | M | V | R16; B15; E8.16 |
| Manschette, Abschottung | IfcDiscreteAccessory | USERDEFINED | Brandschutzmanschette\|Luftdichtheitsmanschette | IfcRelFillsElement -> IfcOpeningElement | HRB_Manschette | - | O | M | V/U | R16; B15 |
| Dämmschlauch, Schutzrohr | IfcCovering | WRAPPING\|SLEEVING |  | IfcRelCoversBldgElements <- IfcPipeSegment | Pset_CoveringCommon | - | O | M | V | R16; B15 |
| Fußbodenaufbau je Raum | IfcCovering | FLOORING |  | IfcRelCoversSpaces -> IfcSpace; IfcMaterialLayerSet (Belag, Estrich, Dämmung) | Pset_CoveringCommon\|HRB_Fussbodenaufbau | M | M | M | V/U | R16; B14 |
| Rohdecke, Bodenplatte | IfcSlab | FLOOR\|BASESLAB |  | IfcRelContainedInSpatialStructure -> Geschoss | Pset_SlabCommon\|Qto_SlabBaseQuantities | M | M | M | V | B14 |
| Fliesen- oder Parkettbelag | IfcCovering | FLOORING\|CLADDING |  | IfcRelCoversSpaces -> IfcSpace; IfcRelContainedInSpatialStructure -> IfcSpace; IfcRelDefinesByType <- IfcCoveringType mit RepresentationMaps | Pset_CoveringCommon\|Pset_CoveringFlooring\|Qto_CoveringBaseQuantities\|HRB_Verlegung\|Pset_ManufacturerOccurrence@A | M | M | M | V | R13; R17; B16 |
| Fliesen- oder Parketttyp | IfcCoveringType | FLOORING\|CLADDING |  | IfcRelDeclares <- IfcProjectLibrary; RepresentationMaps je Sollform | HRB_Fliese\|Pset_ManufacturerTypeInformation@A | M | M | M | V/U | R13; R17; B16 |
| Fliesen- oder Parkettstück | IfcCovering | FLOORING |  | IfcRelAggregates <- Belag; ganze Stücke als IfcMappedItem, Schnittstücke als IfcPolygonalFaceSet | HRB_Fliesenstueck\|Pset_ManufacturerOccurrence | - | - | M | U | R17; B16; E8.12 |
| Sockelleiste | IfcCovering | SKIRTINGBOARD |  | IfcMaterialProfileSet; IfcRelCoversSpaces | Pset_CoveringCommon | - | O | M | V | R13 |
| Übergangsprofil | IfcCovering | USERDEFINED | Uebergangsprofil | IfcRelCoversSpaces | Pset_CoveringCommon | - | O | M | U | R13; E8.15 |
| Treppe | IfcStair | STRAIGHT_RUN_STAIR\|QUARTER_WINDING_STAIR\|HALF_WINDING_STAIR\|QUARTER_TURN_STAIR\|HALF_TURN_STAIR |  | IfcRelAggregates -> IfcStairFlight, IfcRailing, IfcMember STRINGER | Pset_StairCommon\|HRB_Verziehung@R | M | M | M | V/U | R13 |
| Treppenlauf | IfcStairFlight | STRAIGHT\|WINDER |  | IfcRelAggregates <- IfcStair | Pset_StairFlightCommon | M | M | M | V | R13 |
| Treppenwange | IfcMember | STRINGER |  | IfcRelAggregates <- IfcStair | Pset_MemberCommon | - | O | M | V | R13 |
| Geländer, Handlauf | IfcRailing | HANDRAIL\|BALUSTRADE\|GUARDRAIL |  | IfcRelAggregates <- IfcStair oder frei | Pset_RailingCommon | M | M | M | V | R13; R09 |
| Grund- und Anschlussleitung | IfcPipeSegment | RIGIDSEGMENT |  | IfcRelAssignsToGroup -> IfcDistributionSystem SEWAGE\|RAINWATER\|STORMWATER; Ports über IfcRelNests | Pset_PipeSegmentTypeCommon\|Pset_PipeSegmentOccurrence\|HRB_Entwaesserung | - | M | M | V | R18; B17 |
| Revisions-, Kontrollschacht | IfcDistributionChamberElement | MANHOLE\|INSPECTIONCHAMBER |  | Ports über IfcRelNests | Pset_DistributionChamberElementTypeManhole\|Pset_DistributionChamberElementTypeInspectionChamber | - | M | M | V | R18; B17 |
| Pumpenschacht | IfcDistributionChamberElement | SUMP |  | mit IfcPump SUMPPUMP und IfcValve CHECK |  | - | O | M | V | R18 |
| Versickerungsrigole, Sickerschacht | IfcDistributionChamberElement | USERDEFINED | Versickerungsrigole\|Sickerschacht | Ports über IfcRelNests | HRB_Versickerung | - | M | M | V/U | R18; B17; E8.15 |
| Abscheider | IfcInterceptor | GREASE\|OIL\|PETROL |  | Ports über IfcRelNests | Pset_InterceptorTypeCommon | - | O | M | V | R18; B17 |
| Zisterne | IfcTank | STORAGE |  | IfcRelAssignsToGroup -> IfcDistributionSystem RAINWATER | Pset_TankTypeCommon\|HRB_Versickerung | - | M | M | V | R18 |
| Gelände | IfcGeographicElement | TERRAIN |  | IfcRelContainedInSpatialStructure -> IfcSite; IfcTriangulatedFaceSet |  | M | M | M | V | R18; B17 |
| Versickerungsmulde | IfcGeographicElement | USERDEFINED | Versickerungsmulde | IfcRelContainedInSpatialStructure -> IfcSite | HRB_Versickerung | - | O | M | U | R18 |
| Grundwasser | IfcGeotechnicalStratum | WATER |  | IfcRelContainedInSpatialStructure -> IfcSite | Pset_GeotechnicalStratumCommon | - | O | O | V | R18 |
| Immissionsort, Fassadenpegel | IfcAnnotation | USERDEFINED | Immissionsort | IfcRelContainedInSpatialStructure -> IfcSite | HRB_Fassadenpegel | - | M | M | V/U | R20; R22; B19 |
| Isolinie Lärmkarte | IfcAnnotation | CONTOURLINE |  | IfcRelContainedInSpatialStructure -> IfcSite | HRB_Fassadenpegel | - | O | O | V | R22 |
| Lärmschutzwand | IfcWall | USERDEFINED | Laermschutzwand | IfcRelContainedInSpatialStructure -> IfcSite | Pset_WallCommon\|HRB_Schallschutz_Bauteil | O | M | M | V/U | R20 |
| Rollladen | IfcShadingDevice | SHUTTER\|JALOUSIE |  | IfcRelAggregates bzw. Nachbarschaft zu IfcWindow | HRB_Schallschutz_Bauteil | M | M | M | V/U | R20 |
| Montageplan | IfcWorkSchedule | PLANNED |  | IfcRelAssignsToControl -> IfcTask (Sammelvorgang) |  | - | - | M | V | R19; B18 |
| Montagevorgang | IfcTask | INSTALLATION |  | IfcRelNests <- Sammelvorgang; IfcRelAssignsToProduct -> Element; IfcRelSequence FINISH_START; IfcTaskTime | HRB_Kranhub | - | - | M | V/U | R19; B18 |
| Anlieferung | IfcTask | MOVE |  | IfcRelAssignsToProcess <- IfcConstructionEquipmentResource TRANSPORTING | Pset_PackingInstructions | - | - | M | V | R19; B18 |
| Kraneinsatz | IfcConstructionEquipmentResource | ERECTING |  | IfcRelAssignsToProcess -> IfcTask; IfcRelAssignsToResource <- IfcTransportElement |  | - | - | M | V | R19; B18; E8.18 |
| Transporteinsatz | IfcConstructionEquipmentResource | TRANSPORTING |  | IfcRelAssignsToProcess -> IfcTask MOVE; IfcRelAssignsToResource <- IfcVehicle |  | - | - | M | V | R19; B18 |
| Kran | IfcTransportElement | LIFTINGGEAR |  | IfcRelContainedInSpatialStructure -> IfcSite | Pset_TransportElementCommon\|HRB_Kranaufstellung | - | - | M | V/U | R19; B18 |
| LKW | IfcVehicle | VEHICLEWHEELED |  | IfcRelAssignsToResource -> Transporteinsatz | Qto_VehicleBaseQuantities | - | - | M | V | R19; B18 |
| Stellfläche, Abladezone, Schwenkbereich | IfcSpatialZone | CONSTRUCTION\|TRANSPORT\|RESERVATION |  | IfcRelReferencedInSpatialStructure -> IfcSite | Qto_SpatialZoneBaseQuantities | - | - | M | V/U | R19; B18 |
| Kostenplan | IfcCostSchedule | ESTIMATE\|TENDER\|PRICEDBILLOFQUANTITIES |  | IfcRelAssignsToControl -> Elemente; IfcRelNests -> IfcCostItem |  | O | M | M | V | R06; R10 |
| Kostenposition, Mehr-/Minderpreis | IfcCostItem |  |  | IfcCostValue mit Category, ApplicableDate, FixedUntilDate |  | O | M | M | V | R06; R10; E8.14 |
| Bemusterungskatalog | IfcProjectLibrary |  |  | IfcRelDeclares -> Options-Typen; IfcRelDeclares <- IfcProject |  | M | M | M | V | R10; E8.14 |
| Freigabe | IfcApproval |  |  | IfcRelAssociatesApproval -> Objekt; GivingApproval = IfcActor |  | - | M | M | V | R06; R10 |
| Dokument (Vertrag, Nachweisheft, Datenblatt) | IfcDocumentReference |  |  | IfcRelAssociatesDocument -> Objekt; IfcDocumentInformation (Revision, ValidFrom, ValidUntil) | HRB_Dokument | O | M | M | V/U | R06; E8.24 |
| Genehmigung | IfcPermit | BUILDING |  | IfcRelAssignsToControl -> IfcBuilding |  | - | M | M | V | R06 |
| Beteiligter (Entwurfsverfasser) | IfcActor |  | Entwurfsverfasser | IfcActorRole Role = USERDEFINED, UserDefinedRole = Entwurfsverfasser |  | - | M | M | V | R06 |
| Klassifikation DIN 276 | IfcClassificationReference |  |  | IfcRelAssociatesClassification; ReferencedSource = IfcClassification DIN 276, Edition 2018-12 |  | - | M | M | V | B1; E8.19 |
| Klassifikation ETIM | IfcClassificationReference |  |  | IfcRelAssociatesClassification; IfcClassification.Specification = bSDD-URI; Location = Klassen-URI |  | - | M | M | V/U | R10; E8.19 |

### 8.8.3 GUID-Regel

Die folgende Regel ist normativ. Sie erweitert das Schema aus B1 um den Projektnamensraum (E8.27) und die Übernahme in Exporte (E8.26).

**G1 – Namensräume.**

- `NS_FIRMA` ist eine UUID, die einmal zufällig erzeugt, in der Konfiguration der App fest hinterlegt und nie geändert wird.
- `NS_PROJEKT = uuid5(NS_FIRMA, "projekt:" + projekt_id)`. Dabei ist `projekt_id` die unveränderliche Projektkennung der CDE als Unicode-Zeichenkette in Normalform NFC.
- Kompatibilität: Die Beispiele B1 bis B19 verwenden unmittelbar `NS_PROJEKT = 6f1c3b0e-8a52-5d7e-9c4b-2a1d0e7f4b10`.

**G2 – Pfadgrammatik.**

```text
pfad       = "/" segment { "/" segment } ;
segment    = zeichen { zeichen } ;
zeichen    = "A".."Z" | "a".."z" | "0".."9" | "_" | "-" | "." ;
abgeleitet = ( pfad | abgeleitet ) "#" rolle ;
rolle      = "aggregiert" | "enthaelt" | "typisiert" | "schneidet" | "fuellt"
           | "deklariert" | "material" | "zuordnung" | "ports" | "verbunden"
           | psetname ;
```

Pfade unterscheiden Groß- und Kleinschreibung und enden nie auf `/`. Umlaute und Leerzeichen sind in Segmenten nicht zulässig.

**G3 – Wer welchen Pfad bekommt.** Jedes Objekt, das der Generator aus dem Parametermodell erzeugt, erhält einen expliziten Pfad, der seine Lage im Parametermodell beschreibt, etwa `/wand/oeffnungen/F1/sturz`. Beziehungen, Psets und Mengen erhalten einen abgeleiteten Pfad:

| IfcRoot-Instanz | Pfad | Beispiel aus B1 |
|---|---|---|
| `IfcRelAggregates` | Pfad(RelatingObject) + `#aggregiert` | `/wand#aggregiert` |
| `IfcRelContainedInSpatialStructure` | Pfad(RelatingStructure) + `#enthaelt` | `/projekt/gebaeude/EG#enthaelt` |
| `IfcRelDefinesByType` | Pfad(RelatingType) + `#typisiert` | `/typen/wand/AW-HRB-01#typisiert` |
| `IfcRelVoidsElement` | Pfad(RelatedOpeningElement) + `#schneidet` | `/wand/kerven/K1#schneidet` |
| `IfcRelFillsElement` | Pfad(RelatedBuildingElement) + `#fuellt` | neu |
| `IfcRelDeclares` | Pfad(RelatingContext) + `#deklariert` | `/projekt#deklariert` |
| `IfcRelAssociatesMaterial` am Einzelobjekt | Pfad(Objekt) + `#material` | `/wand#material` |
| `IfcRelAssociatesMaterial` für viele Objekte | `/materialien/<schluessel>#zuordnung` | `/materialien/kvh_c24#zuordnung` |
| `IfcPropertySet`, `IfcElementQuantity` | Pfad(Objekt) + `#` + Name | `/wand#Pset_WallCommon` |
| `IfcRelDefinesByProperties` | Pfad(Pset) + `#zuordnung` | `/wand#Pset_WallCommon#zuordnung` |
| `IfcDistributionPort` | Pfad(Element) + `/port/<name>` | neu |
| `IfcRelNests` (Ports) | Pfad(RelatingObject) + `#ports` | neu |
| `IfcRelConnectsPorts` | Pfad(RelatingPort) + `#verbunden` | neu |

**G4 – Berechnung.**

```python
import uuid, ifcopenshell.guid
def global_id(ns_projekt: uuid.UUID, pfad: str) -> str:
    return ifcopenshell.guid.compress(uuid.uuid5(ns_projekt, pfad).hex)   # 22 Zeichen
```

`uuid.uuid5` kodiert den Pfad intern als UTF-8. Die GlobalId wird erst nach dem vollständigen Aufbau des Modells gesetzt, in einem Durchlauf über alle `IfcRoot`-Instanzen.

**G5 – Eindeutigkeit.** Die Abbildung Objekt → Pfad ist je Datei injektiv. Kommt ein Pfad doppelt vor, bricht der Generator mit einem Fehler ab. Er hängt keinen Zähler an.

**G6 – Stabilität.**

- Segmente verwenden stabile Kennungen des Parametermodells (`F1`, `K1`, `osb_staender`).
- Indizes sind nur für Objekte zulässig, deren Identität ihre Position ist: Rasterständer k (Achse k · e), Platte j (j-te Platte ab x = 0), Teilstück i, wenn eine Platte durch Öffnungen zerfällt, Gefach nach Lage (`/wand/gefach/x1280_z60`).
- Indizes aus der Iterationsreihenfolge von Mengen oder Dictionaries sind verboten.
- Jede Änderung der Pfadstruktur erhöht `HRB_Generator.PfadschemaVersion` und legt eine Migrationstabelle `pfad_alt, pfad_neu, guid_alt, guid_neu` in der CDE ab.

**G7 – Exporte.** In BTLx ist `Transformation GUID = "{" + str(uuid5(NS_PROJEKT, pfad)) + "}"`, also dieselbe UUID wie im IFC. Zusätzlich trägt jeder `Part` `UserAttribute Name="IfcGlobalId"` mit der komprimierten GlobalId. Das ersetzt das bisherige Schema von B7 (`uuid5(Namensraum, "btlx:" + Pfad)`).

**G8 – Regressionsvektoren.** Mit dem Namensraum der Beispiele müssen die folgenden Werte entstehen. Sie sind gegen `ausgabe/wandelement.ifc` geprüft [V]:

| Pfad | GlobalId |
|---|---|
| `/projekt` | `3n9mhceD9U_ez8SJ26bpTm` |
| `/wand` | `0gsiGQj_bG3wx8M0qwRA0U` |
| `/wand/schwelle` | `3N9BxbmVjJqfMasIm6VCTu` |
| `/wand/staender/rand/links` | `0ruebnGhrPUPaN5fsim6Vf` |
| `/wand/kerven/K1` | `2wzspq7qPLDQOqcQt$qavq` |
| `/wand/kerven/K1#schneidet` | `26reED$iDQSQquU8q9MZLr` |
| `/wand#aggregiert` | `3H$X1wKCnSyfz6MaSj_7C9` |
| `/typen/verbindungsmittel/osb_staender` | `10kcZK2DzMauPxIfg5Yrjt` |

Ein zusätzlicher Test muss zeigen, dass zwei verschiedene `projekt_id` für denselben Pfad verschiedene GlobalIds ergeben.

### 8.8.4 ObjectType-Vokabular

Das Vokabular für USERDEFINED und für Rollen im ObjectType ist die Vereinigung der Spalte `object_type` in `spezifikation/ifc-mapping.csv`. Es ist geschlossen: Ein Wert, der dort nicht steht, ist ein Fehler nach ANF-08-05. Für die Werte gilt:

1. Sie sind ASCII, ohne Umlaute und Leerzeichen (`Laermschutzwand`, `Uebergangsprofil`, `Fuellstaender`).
2. Werte, die einen englischen Enum-Wert ergänzen, sind in Großbuchstaben geschrieben (`MEMBRANE`, `RIDGE`, `SNOWGUARD`, `DORMER`). Fachliche Rollen und deutsche Fachbegriffe stehen in Binnenmajuskel (`Koenigsstaender`, `Versickerungsrigole`).
3. Ein neuer Wert braucht einen Eintrag in der CSV mit Quelle und später eine bSDD-Klasse (ANF-08-15).

**Abweichung der Prototypen.** B1 schreibt Rollen derzeit mit Umlaut und Leerzeichen (etwa „Randständer“ im Listing 8.1). Das verstößt gegen Punkt 1 und ist mit der Umbenennung der Psets zu bereinigen. Die Klartextbezeichnung bleibt im Attribut `Name` erhalten.

## Verwendete Schlüssel

Das Kapitel enthält 92 Zitatstellen zu 64 Schlüsseln. Alle stammen aus `literatur/lit-*.bib`. Für die bekannten Dubletten sind die führenden Schlüssel verwendet (`iso2024ifc` statt `iso16739-2024`, `bsi2024ids` statt `ids2024`, siehe `literatur/KORREKTUREN.md`). Zugeordnet ist jeweils die erste Datei, in der ein Schlüssel steht.

**lit-A-acc-bim.bib** (14): `bazjanac2010space`, `bimbauantrag2020abschluss`, `bsi2024ids`, `bsi2025validation`, `chek2024d22`, `iso2024ifc`, `jaud2020georeferencing`, `jaud2022georeferencing`, `krijnen2020efficient`, `lai2018interoperability`, `moult2020compliance`, `tomczak2022review`, `vanberlo2021future`, `zhang2015interoperable`

**lit-B-vorfertigung-ki.bib** (2): `compastimber`, `geier2022bimwood`

**lit-C-recht-normen.bib** (11): `bimbauantrag2020`, `bimportal`, `bsiMvd43`, `bsiValidation`, `btlx23`, `dataholz`, `din18290-2`, `iso19650`, `nrw2026bimbauantrag`, `oekobaudat`, `zvdh2024`

**lit-D-vergleich-vorfertigung.bib** (5): `alwisy2019bim`, `chateauvieux2023bim`, `orozco2023codesign`, `ramaji2017product`, `timbim2024`

**lit-E-vergleich-automation.bib** (5): `abualdenien2019metamodel`, `abualdenien2022levels`, `elsibaii2025open`, `ma2006testing`, `pazlar2008interoperability`

**lit-G-luecken.bib** (2): `standtke2024etim`, `tugraz2025syswood`

**lit-H-ff4-ff5.bib** (3): `alfaro2025chek`, `fakour2025exploring`, `jaskula2024common`

**lit-I-schneeball-a.bib** (12): `darwish2022automated`, `eastman2010exchange`, `fischer2024extending`, `fonsati2026leveraging`, `hagedorn2023semantic`, `laakso2012ifc`, `liu2016ontology`, `liu2023definition`, `ramaji2016product`, `ramaji2017extending`, `shi2018ifcdiff`, `venugopal2012semantics`

**lit-I-schneeball-b.bib** (4): `chateauvieuxhellwig2022timber`, `chateauvieuxhellwig2025schallschutz`, `dineniso7817-1`, `iso23387`

**lit-J-schneeball-runde2.bib** (3): `akbas2025holistic`, `esser2022graphbased`, `mattern2018bimbased`

**lit-M-nachweis.bib** (3): `barker2022fair4rs`, `iso6946_2017`, `smith2016softwarecitation`

### Python-Key-Check

```python
import re, glob, pathlib
text = pathlib.Path("08-informationsmodell.md").read_text(encoding="utf-8")
body = text.split("## Verwendete Schlüssel")[0]
cited = {k.strip().lstrip("@") for grp in re.findall(r"\[(@[^\]]+)\]", body) for k in grp.split(";")}
bib = set()
for f in glob.glob("literatur/lit-*.bib"):
    bib |= set(re.findall(r"^@\w+\{([^,\s]+),", open(f, encoding="utf-8").read(), re.M))
print(len(cited), "zitiert;", "fehlend:", sorted(cited - bib) or "keine")
```

Ergebnis (27.09.2026, aus `arbeit/` ausgeführt): `64 zitiert; fehlend: keine`.

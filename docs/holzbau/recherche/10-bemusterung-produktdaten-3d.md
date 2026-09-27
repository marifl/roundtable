# Recherche 10: Bemusterung, Produktdaten, 3D-Präsentation

Stand: 27.09.2026. **[V]** = an Primärquelle oder maschinell geprüft (IfcOpenShell 0.8.5, Schema IFC4X3_ADD2), **[U]** = unsicher oder eigene Ableitung.

## Ergebnis in 5 Punkten

1. **IFC 4.3 kann die ganze Bemusterung tragen, aber nur als Summe mehrerer Mechanismen.** Dazu gehören Typen in einer IfcProjectLibrary, ETIM über bSDD, Pset_ManufacturerTypeInformation (GTIN, Artikelnummer), IfcCostItem für Mehr- und Minderpreise, IfcApproval für die unterschriebene Ausstattungsfestlegung und PBR-Oberflächen mit `PHYSICAL` und Textur-Modes [V]. Ein Konzept „Option“ fehlt. Regeln bleiben außerhalb der Datei (IDS plus eigene Regelmaschine).
2. **Die Bemusterung ist bei Regnauer kein Innenausbau-Thema, sondern ein Fertigungs-Gate.** Dosenbohrungen, Zugdrähte, Sanitäranschlüsse, WC-Tragkonstruktion und Unterputzarmaturen werden schon in der Wandfertigung eingebaut. Der Montagebeginn liegt frühestens 12 Wochen nach der vollständigen, unterschriebenen Ausstattungsfestlegung [V]. „Ausführungsfertig“ muss deshalb vor der Werkplanung erreicht sein.
3. **Produktdaten gibt es, fertig verknüpft sind sie nicht.**
   - ETIM 10.0 ist frei (ODC-By 1.0), liegt im bSDD und ist zum Teil mit IFC 4.3 verknüpft. Dazu kommt ETIM MC für Geometrie (LOD ≈ 200) [V].
   - ECLASS ist lizenzpflichtig. VDI 3805 ist kostenpflichtig, aber für TGA technisch am tiefsten [V].
   - Herstellerdaten sind uneinheitlich. Ein BIMobject-IFC von Duravit ist IFC2X3 mit leerer GTIN und proprietären Psets [V].
4. **Die 3D-Pipeline IFC → glTF verliert heute Texturen.** IfcOpenShell 0.8.5 schreibt Farbe, Metallic und Roughness, aber keine Bilder und keine UV-Koordinaten [V, selbst getestet]. Dafür ist ein eigener Exporter nötig: Material per Name bzw. GlobalId an eine PBR-Bibliothek binden (CC0: ambientCG, Poly Haven [V]). Die Bemusterungsvarianten gehören als **KHR_materials_variants** (ratifiziert [V]) in eine einzige GLB. AR läuft über model-viewer (WebXR, Scene Viewer, automatisch erzeugtes USDZ für Quick Look [V]).
5. **Die drei Reifegrade lassen sich normkonform als LOIN nach DIN EN ISO 7817-1:2024-11 definieren** (ersetzt DIN EN 17412-1 [V]). Die Norm kennt „Appearance“ ausdrücklich als geometrischen Aspekt [V]. Präsentationsfertig, prüffertig und ausführungsfertig sind dann drei LOIN-Profile mit je eigenem Zweck, Meilenstein, Akteur und IDS-Prüfung.

## 1. Umfang der Bemusterung

### Regnauer, Bau- und Ausstattungsbeschreibung 10/2024 [V]
Quelle: https://cms20683.livestep.de/hausbau/downloads/Regnauer_Bauleistungs-Ausstattungsbeschreibung_1024.pdf (volltextlich gelesen, Kap. 1–25 und AGB)

- **Ort und Rolle:**
  - Die „Beratung und Ausstattungsfestlegung“ macht der Projektleiter im **Bauherrenzentrum Seebruck**.
  - Nach § 650n BGB erhält der Kunde vor der Ausführung eine „Ausstattung als textliche Beschreibung“ und einen **Ausstattungsplan**.
- **Vertrag:**
  - Detail-Pauschalvertrag. Mehr- und Minderpreise aus der Ausstattungsfestlegung werden saldiert (AGB § 8).
  - **Visualisierungen und Modelle sind unverbindlich** (AGB § 2).
  - Baubeginn erst, wenn die Ausstattungsfestlegung „endgültig abgeschlossen“ und unterschrieben ist. Montage frühestens 12 Wochen danach (AGB § 5/§ 6).
- **Budgetlogik statt Artikelliste:**
  - Boden- und Wandfliesen 50 €/m² brutto Material, bis 30 × 60 cm, Kreuzfuge.
  - Parkett 80 €/m² brutto (UVP), ca. 13,5 mm mit 3,5 mm Nutzschicht, schwimmend verlegt, „z. B. Haro“.
  - Sonstige Beläge und Teppich 50 €/m².
- **Mengenregeln:**
  - Wandfliesen im Bad umlaufend 120 cm hoch, an Wanne und Dusche 200 cm.
  - WC-Fliesenspiegel 1,00 × 1,00 m.
  - Elektro-Grundausstattung je Raumtyp (z. B. Kinderzimmer: 1 Lichtauslass, 1 Doppel- und 3 Einfachsteckdosen).
- **Standardobjekte:**
  - Sanitär: Bad mit Wanne 75/170, Waschtisch 60, Wand-WC, bodengleiche Dusche 75/90, 80/80 oder 90/90 mit ESG. UP-Spülkasten 9 l.
  - Die Serien heißen „Derby, Tesi, Lua“; die Hersteller sind nicht genannt [U].
  - Innentüren: Echtholzfurnier Ahorn oder Buche bzw. 8 Dekore. Im Text taucht „Herholz“ auf.
  - Schalter: „weißes Oberflächenprogramm eines Markenherstellers“, Marke offen.
  - Treppe: Buche, keilgezinkt. Geländerstäbe aus Buche oder Edelstahl.
  - Fenster: KlimaPlus Holz-Alu, **11 Alu-Farben**, Ug 0,5. Sprossen aufgeklebt oder innenliegend. Rollladen, Raffstore oder Laden immer elektrisch.
  - Dach: Tonziegel mit Engobe, Hagelwiderstandsklasse 4.
  - Fassade: Putz K3 oder Stülpschalung Fichte, dazu 5 weitere Schalungsvarianten.
  - HLK: KWL mit WRG ist Standard. Wahl zwischen Luft/Wasser-WP (R290) mit Fußbodenheizung und Proxon Luft/Luft-WP mit separater Trinkwasser-WP (300 l).
  - Smart Home ist ein individuelles Paket. AFDD (Brandschutzschalter) ist nicht enthalten, die Beratung dazu findet „bei der Bemusterung“ statt.
- **Werksvorfertigung:**
  - „Bereits bei der Wandproduktion“ werden Dosenbohrungen und Zugdrähte vorbereitet, dazu Sanitäranschlüsse, Tragkonstruktion Hänge-WC, UP-Spülkästen und UP-Armaturen.
  - Innenwände haben eine 40-mm-Installationsebene. Bei der Außenwand liegt die Vliesdampfbremse direkt hinter 25 mm Gips; eine Installationsebene wird nicht beschrieben.
- **Eigenleistungspakete** SF1, SF2, TA1–TA3, TBH für 14 Gewerke. Die Kürzel sind nicht erklärt [U].
- **Küche** ist nicht Teil der Leistung. Enthalten sind nur die Anschlüsse für Spüle, Geschirrspüler und Herd sowie 2–3 Lichtauslässe.
- **Widerspruch zu Recherche 04:** Die BLB fixiert L'n,w ≤ 52 dB (vertraglicher Wert); Recherche 04 nannte 49 dB am Bau. Beide Werte können zugleich stimmen (Zusage vs. Messung) [U]. Die Riegelstärke der Vitalwand beträgt in der BLB 10/2024 200 mm.

### Markt [V]
- **Bien-Zenker** (Mülheim-Kärlich, ca. 1.800 m²): Die Bemusterung dauert 1–2 Tage. Vorher gibt es eine **Online-Bemusterung**, vor Ort erfasst der Berater „direkt elektronisch“. Die Artikelliste landet in der Bauherren-App. Vorab erhält der Kunde Elektropläne zum Einzeichnen.
- **Hanse Haus:** Bauherrenzentrum mit ca. 1.800 m² und „geführter Vorbemusterung“.
- **WeberHaus World of Living:** über 3.500 m² Ausstellung, Küchen eingeschlossen.
- **Ratgeber** (fertighaus.de): 10.000–50.000 € Aufbemusterung seien „keine Seltenheit“ [U, Branchenportal, keine Studie]. Eine VPB-eigene Bemusterungs-Checkliste habe ich nicht gefunden; der VPB fokussiert auf Bauvertrag und Baubeschreibung [V].

### Bemusterungs-Taxonomie mit Abhängigkeiten

„Freeze“ = spätester Festlegungszeitpunkt. **W** = vor Werkplanung/Wandfertigung, **A** = vor Ausbau. Die IFC-Abbildung ist an IFC4X3_ADD2 geprüft [V]; die Abhängigkeiten sind aus BLB und Herstellerquellen abgeleitet [V/U].

| Kategorie | Auswahlpunkte | IFC (Typ/PredefinedType) | Abhängigkeiten → | Freeze |
|---|---|---|---|---|
| Fassade | Putz/Schalung/Mischfassade, Holzart, Farbe, Fugenprofil | IfcCovering CLADDING + Layer-Set | Wanddicke 345–381 mm → Laibung, Dachüberstand, U-Wert; Farbe ↔ Bebauungsplan | W |
| Dach | Ziegelmodell/-farbe, Spenglermaterial (Zink/Kupfer), Dachfenster, Schneefang, PV Auf-/Indach | IfcCovering ROOFING, IfcWindow SKYLIGHT | Farbe ↔ Bebauungsplan; PV ↔ Zählerschrank, Statik | W |
| Fenster | Alu-Farbe außen (11), Innenfarbe, Sprossen, Glasfunktion (RC2, VSG, Schallschutz), Fensterbänke | IfcWindowType + Pset_WindowCommon, Pset_DoorWindowGlazingType | Innenliegende Sprossen und Funktionsglas → Ug/Uw → GEG-Nachweis; Außenfarbe ↔ Fassade | W |
| Sonnenschutz | Rollladen/Raffstore/Laden, Kastenart, Antrieb, Steuerung | IfcShadingDevice SHUTTER/JALOUSIE | Kasten ↔ Sturz/Wandaufbau; Antrieb ↔ Elektro (Leitung, Smart Home); sommerlicher Wärmeschutz | W |
| Haustür | Modell, RAL 7016/9016/Holz, Glas, Seitenteil, Griff, Zutritt | IfcDoor DOOR | Seitenteil → Öffnungsmaß; Smart Lock → Elektro | W |
| Treppe | Holzart, Setzstufen, Wange, Geländer | IfcStair + IfcStairFlight, IfcRailing | Deckenöffnung, Laufmaße nach DIN 18065 | W |
| Innentüren | Oberfläche, Glas, Zarge, Drücker (Edelstahl/Messing/Neusilber) | IfcDoorType + Pset_DoorLiningProperties | Türunterschnitt oder Überströmdichtung ↔ KWL; Türhöhe ↔ Bodenaufbau | A (Maße W) |
| Böden | Parkett (Holz, Sortierung, Oberfläche), Vinyl, Laminat, Teppich, Fliese | IfcCovering FLOORING + SKIRTINGBOARD | Rλ,B ≤ 0,15 m²K/W ↔ FBH-Auslegung; Aufbauhöhe ↔ Türen und Schwellen | A |
| Fliesen | Format, Serie, Fuge, Verlegemuster, Höhen, Abschlussschienen | IfcCovering FLOORING/CLADDING | > 30 × 60 → Mehrpreis, Untergrund; Naturstein → Flächenlast; Gefälle ↔ bodengleiche Dusche | A |
| Sanitär | Serie oder Design-Linie, WC, WT, Wanne, Dusche, Armaturen, Glas, Accessoires | IfcSanitaryTerminalType TOILETPAN/WASHHANDBASIN/BATH/SHOWER/CISTERN | WC → Montageelement → Holzständer; Dusch-WC → Stromanschluss; Wannenlast → Decke | **W** |
| Elektro | Schalterprogramm/Farbe, Anzahl und Lage der Auslässe, Daten, AFDD, Außen, Wallbox | IfcSwitchingDevice TOGGLESWITCH …, IfcOutlet POWEROUTLET/DATAOUTLET, IfcJunctionBox | Lage → **werkseitige Dosenbohrung**; Programm ↔ Dosentyp und Rahmenraster | **W** |
| Smart Home | Umfang (Beschattung, Licht, Heizung, Alarm), System (KNX/Funk) | IfcController, IfcSensor, IfcActuator [U] | Tiefe Dosen, Leitungswege, Verteilergröße | **W** |
| Heizung/Lüftung | L/W-WP + FBH oder Proxon L/L, Heizkörper Bad, KWL-Optionen | IfcUnitaryEquipment, IfcSpaceHeater, IfcAirTerminal | FBH ↔ Beläge; Außeneinheit ↔ Schall/Fundament; KWL ↔ Dunstabzug, Kaminofen | W |
| Wand/Decke | Q2 Standard/Q3–Q4, Farbe, Tapete, Sichtschalung | IfcSurfaceStyle am IfcMaterial; IfcCovering CEILING | Einbauleuchten ↔ 30 mm Abstandsschalung, Schall, F30 [U] | A |
| Balkon/Terrasse | Lärche/Stahl, Geländer, Loggia | IfcSlab, IfcRailing, IfcCovering | Schwelle 15 cm (Flachdachrichtlinie, laut BLB) ↔ Außenanlage | W |
| Küche (extern) | Planung meist durch Küchenstudio | IfcFurniture USERDEFINED, IfcElectricAppliance | Anschlüsse, Hängeschränke, Abluft/Umluft ↔ KWL | W (Anschlüsse) |
| Außenanlagen | meist bauherrenseitig, Podeste, Lichtschächte | IfcGeographicElement, IfcCivilElement [U] | Sockelhöhe ≈ 30 cm (BLB) | – |

## 2. Produktdatenstandards

| Standard | Stand [V] | Inhalt | Lizenz/Zugang [V] | IFC-Bezug | Urteil |
|---|---|---|---|---|---|
| **ETIM 10.0** | 05.12.2024, 5.640–5.799 Klassen | Klassen und Merkmale Elektro, SHK, HLK, Bau | **frei**, ODC-By 1.0; EN und DE frei per API | im bSDD (verified); 97 Gruppen und 491 Klassen mit IFC 4.3 verknüpft, Beispiel EC003535 „interior door“ | **übernehmen** als Primärklassifikation |
| **ETIM MC** (Modelling Classes) | Guidelines 2.0 (01/2026); bSDD-Preview 03/2025 | parametrische Geometrie-Blueprints, SVG-Referenzzeichnungen, PortCodes, **LOD ≈ 200** | ODC-By 1.0 | über bSDD mit IFC 4.3 und EC verknüpft | **übernehmen** für generische Ersatzgeometrie |
| **ETIM xChange** | 2.0 (27.11.2025; ETIM D nennt 27.12.2025 [U]) | JSON-Produktstammdaten, Product → TradeItem → Verpackung | frei | keiner direkt | **übernehmen** als Importformat |
| ETIM BMEcat 5.0 | Leitfaden 5.0 | XML auf Basis BMEcat 2005 | frei | keiner | lesen können |
| **BMEcat 2005** | eingefroren | Katalog, Preise, **PRODUCT_CONFIG_DETAILS** (CONFIG_STEP, CONFIG_RULES, CONFIG_FORMULAS) | XSD frei beim BME | keiner | Konfigurationsschritte als Vorbild |
| **ECLASS 16.0** | 27.11.2025 | Klassen und Merkmale (ISO 13584) | **lizenzpflichtig** nach Firmengröße, nur ASSET frei; Suche frei | bSDD-Mapping „in Arbeit“ (05/2024), Status heute [U] | nur bei Kundenwunsch |
| **VDI 3805** | Blatt 1 (2022-07), Blatt 45 Sanitärobjekte (2021-03) u. v. m. | TGA-Technikdaten, **Störräume**, Anschlüsse, Varianten per Funktion (Satzart 820) | kostenpflichtig (DIN Media); BDH-Webportal für Daten | ISO 16757 als Internationalisierung | adaptieren für Heizung und Sanitär |
| DATANORM 5 / Open Masterdata | DATANORM alt; OMD als On-demand-API (BVBS, ZVSHK, DG Haustechnik) | Artikel, Preise, Fliesen- und Parkettsatz | Branchenzugang | keiner | nur für Preise und Lieferbarkeit |
| DQR 10.0 (ARGE Neue Medien) | jährlich zum 1.4. | Datenqualität SHK, **GTIN je Artikel** | frei | keiner | Qualitätskriterium |
| „VDS-Datenstandard“ | **nicht gefunden** | Die VDS ist Dachverband ohne eigenes Datenformat | – | – | streichen, VDI 3805 Bl. 45 + ETIM nutzen |
| **DCC IDM Küche/Bad 3.1.0** | aktuell | Möbel- und Küchenkatalog mit **Varianten und Regeln (DECISIONS, ACTIONS)** | Download beim DCC | keiner | Schnittstelle Küchenstudio |
| OFML (IBA) | aktuell | Büromöbel, Produktlogik und OCD-Preise | Spezifikation offen [U] | keiner | Referenz für Regeln |
| **ISO 23386:2020 / ISO 23387:2025** | 23387 Ed. 2, DIN EN ISO 23387:2026-01 (ersetzt 2020-12) | Merkmals-Governance, **Data Templates**, XSD | kostenpflichtig | Regeln für Links zu IFC-Klassen im Data Dictionary | Methode für eigene Regnauer-Templates |
| GS1 GTIN | – | globale Artikel-ID | GS1-Mitgliedschaft für Vergabe | `Pset_ManufacturerTypeInformation.GlobalTradeItemNumber` [V] | Pflichtfeld „ausführungsfertig“ |
| **DPP** | ESPR (EU) 2024/1781; für Bauprodukte **CPR (EU) 2024/3110 Art. 75 ff.**, gilt seit 08.01.2026 | digitaler Produktpass | DPP-Pflicht erst 18 Monate nach dem delegierten Rechtsakt, der noch fehlt | „ohne Beeinträchtigung der Interoperabilität mit BIM“ (Art. 75) | vorbereiten: DPP-URI als IfcDocumentReference |

### Standardkonforme Verknüpfung in IFC 4.3 [V am Schema, Muster U]
1. **Katalog:** eine `IfcProjectLibrary` „Regnauer Bemusterung 2026“ mit `IfcRelDeclares` auf alle Options-Typen (z. B. `IfcSanitaryTerminalType` TOILETPAN). Die Wahl ist ein `IfcRelDefinesByType` zur Occurrence.
2. **Klassifikation:** `IfcClassification` (Source „ETIM International“, Edition „10.0“, **Specification** = bSDD-URI; in 4.3 heißt das Feld nicht mehr Location). Dazu `IfcClassificationReference` (Identification „EC…“, Location = bSDD-Klassen-URI) über `IfcRelAssociatesClassification`.
3. **Merkmale:** ETIM-Features in einem eigenen Pset (kein Präfix „Pset_“). Jede Property über `IfcExternalReferenceRelationship` mit ihrer bSDD-Property-URI verknüpfen; `IfcResourceObjectSelect` erlaubt `IfcPropertyAbstraction` [V].
4. **Hersteller:** `Pset_ManufacturerTypeInformation` (GlobalTradeItemNumber, ArticleNumber, ModelReference, ModelLabel, Manufacturer). Die Occurrence bekommt `Pset_ManufacturerOccurrence` (SerialNumber, BatchReference) erst bei Lieferung [V].
5. **Dokumente:** Datenblatt, Montageanleitung, DoPC und später der DPP als `IfcDocumentReference` über `IfcRelAssociatesDocument`.
6. **Preis:** `IfcCostSchedule` (ESTIMATE, bei Unterschrift TENDER) mit `IfcCostItem` je Bemusterungsposition. `IfcCostValue` trägt Category „Mehrpreis/Minderpreis“, ApplicableDate und FixedUntilDate. Verknüpfung über `IfcRelAssignsToControl` [V].
7. **Freigabe:** `IfcApproval` („Ausstattungsfestlegung unterzeichnet“, GivingApproval = Bauherr) über `IfcRelAssociatesApproval`.
8. **Randbedingung (deklarativ):** `IfcMetric` oder `IfcObjective` (Qualifier REQUIREMENT, z. B. Rλ,B ≤ 0,15) über `IfcRelAssociatesConstraint`. Nur zur Dokumentation, da kaum Software das auswertet [U].
9. **Anschlüsse:** `IfcDistributionPort` (per `IfcRelNests` am Typ) für Abwasser DN, Kalt- und Warmwasser, Strom. Das entspricht den VDI-3805-Anschlüssen und ETIM-MC-PortCodes [U].

## 3. Herstellerdaten

| Hersteller | Daten [V] | Formate/Plattform | Lizenz | Urteil |
|---|---|---|---|---|
| **Villeroy & Boch** | BIM-Datenbibliothek, 2D/3D auf Kollektionsebene | pro.villeroy-boch.com | Nutzungsbedingungen [U] | adaptieren |
| **Hansgrohe/AXOR** | Armaturen, Brausen, Installationstechnik, **LOD 300** | Revit, ArchiCAD, AutoCAD, SketchUp, **IFC**, 3DS; auch BIMobject | [U] | adaptieren |
| **Duravit** | über BIMobject; das IFC ist **IFC2X3**, `IfcFlowTerminal` + `IfcSanitaryTerminalType` NOTDEFINED, GTIN leer, Psets `ePset_BIMobject_BO` | BIMobject | BIMobject-AGB [U] | nur Geometrie; **korrigiert Recherche 04 („nur .rfa“)** |
| **Geberit** | Revit-Plug-in (2024–2026) plus **Datenpakete im Produktkatalog**; Montageregeln für die Holzständerwand | RFA, Katalog | kostenlos | adaptieren; **korrigiert Recherche 04** |
| **Grohe** | BIM-Daten (nicht im Detail geprüft) | [U] | [U] | prüfen |
| **Gira** | alle Produkte als **IFC-Gesamtdatei (ca. 14–15 MB)** und Revit; HeinzeBIM | Download-Portal | „für den deutschen Markt kostenlos“ | **übernehmen** |
| **JUNG** | Revit- und Archicad-Konfigurator mit **Logikprüfung** gegen falsche Kombinationen, ca. 10.000 Artikel, LOD 100/350, ETIM 8; JUNG.Partcommunity (CADENAS) mit über 120 Formaten; FBX/OBJ der Serie LS | Plug-ins, 3Dfindit | kostenlos | Geometrie übernehmen; **Regeln fehlen als Daten** |
| Busch-Jaeger | nicht verifiziert | [U] | [U] | offen |
| **Hörmann** | über 100 Produkte, Revit, Archicad, **IFC auf Anfrage**, 8 Sprachen | ProduktPortal, BIMobject | kostenlos | adaptieren |
| **Schüco** | BIM Catalog, generische Revit-Fenster | Revit, ArchiCAD, AutoCAD | [U] | Referenz (Alu) |
| **Internorm** | KF 410, HF 410 parametrisch | ArchiCAD, Revit über BIMobject, B2B-Portal | kostenlos | Referenz |
| **HARO** | CAD-Texturen **5 × 5 m, nicht kachelnd**, Room Visualizer | HARO-Portal | [U] | anfragen (Regnauer-Partner) |
| **Bauwerk** | CAD- und BIM-Texturen **über mtextur** | mtextur | mtextur-Lizenz | nur mit Genehmigung |
| Agrob Buchtal, Marazzi | Artikeldaten [V], Texturen nicht verifiziert | [U] | [U] | anfragen |
| **Regnauer KlimaPlus** | Eigenfertigung, **keine öffentlichen BIM-Daten** | – | – | parametrisch selbst modellieren |

**Plattformen:**
- **BIMobject:** kostenlos, Qualität schwankt [V, vgl. Recherche 04].
- **CADENAS 3Dfindit / PARTcommunity:** Basis der JUNG-Daten [V].
- **HeinzeBIM** (Gira) [V].
- **mtextur:** über 50.000 Herstellertexturen [U]. **Die Lizenz verbietet die Nutzung in Datenbanken, Webapplikationen und Softwareprodukten, das Speichern auf eigenen Servern und KI-Training** [V]. Für einen Web-Konfigurator ist mtextur ohne schriftliche Genehmigung ausgeschlossen.
- Syncronia, Plan.One, ArchiExpo: nicht geprüft [U]. **„herstellerdaten.de“ habe ich nicht gefunden.**

## 4. 3D-Pipeline

### Was IFC 4.3 an Material kann [V, Schema und Doku]
- `IfcSurfaceStyleRendering.ReflectanceMethod = PHYSICAL` folgt dem X3D-Physical-Modell:
  - DiffuseColour = baseColor
  - SpecularColour (als Faktor) = metallic
  - SpecularHighlight (IfcSpecularRoughness) = roughness
  - TransmissionColour, DiffuseTransmissionColour und ReflectionColour sind in 4.3 **deprecated**.
- `IfcSurfaceTexture.Mode` ist seit 4.3.0 der Map-Typ: `DIFFUSE`, `NORMAL`, `METALLICROUGHNESS`, `OCCLUSION`, `EMISSIVE` (für PHYSICAL), dazu `AMBIENT`, `SHININESS`, `SPECULAR` (für PHONG). Pro Mode ist höchstens eine Textur erlaubt. `Parameter` ist deprecated.
- Weitere Bausteine:
  - Texturen: `IfcImageTexture` (URL), `IfcBlobTexture`, `IfcPixelTexture`
  - UV-Koordinaten: `IfcIndexedTriangleTextureMap` + `IfcTextureVertexList`
  - Skalierung: `TextureTransform`, z. B. Parkett in echter Größe
  - Brechung: `IfcSurfaceStyleRefraction` (IOR)
  - **`IfcExternallyDefinedSurfaceStyle`** (URI) als normkonformer Haken auf eine MaterialX- oder glTF-Materialdefinition
- **Test mit IfcOpenShell 0.8.5** (Skript im Scratchpad):
  - Eine IfcCovering mit PHYSICAL, DIFFUSE- und NORMAL-Textur und UV-Map exportiert nach GLB `pbrMetallicRoughness` mit baseColorFactor, metallic 0 und roughness 0,6.
  - **Es fehlen images, textures und TEXCOORD_0.**
  - baseColor kommt aus SurfaceColour statt aus DiffuseColour, abweichend von der Doku.

### Empfohlene Pipeline [U, Entwurf]
1. Generator (IfcOpenShell) schreibt IFC4X3_ADD2: Geometrie, Typen, Materialien und `IfcSurfaceStyle` am **IfcMaterial** (`IfcMaterialDefinitionRepresentation`), damit ein Materialtausch alle Bauteile umfärbt.
2. Tessellierung über `ifcopenshell.geom`. **Eigener glTF-Writer** (z. B. glTF-Transform, MIT [V]): UV aus der IFC-Texturmap oder per Box-Mapping nach realem Maß, PBR-Maps aus der Bibliothek, **KHR_materials_variants** je Bemusterungsposition, KHR_texture_transform, KTX2/basisu und Meshopt.
3. Materialbibliothek: ambientCG und Poly Haven (**CC0**, HDRIs eingeschlossen) als Platzhalter. Herstellertexturen nur mit schriftlicher Lizenz.
4. Viewer:
   - three.js (MIT) mit WebGLRenderer; der WebGPURenderer ist laut Doku noch „experimental“ [V].
   - Fotorealistische Standbilder mit **three-gpu-pathtracer** (MIT, 0.0.24).
   - Fachmodell-Ansicht mit @thatopen/components (MIT) und web-ifc (MPL-2.0).
5. AR: **model-viewer** (Apache-2.0, 4.3.1) mit `ar-modes="webxr scene-viewer quick-look"`. Ohne `ios-src` erzeugt es das USDZ automatisch [V]; Animationen fehlen dann.
6. Sonne: Sonnenstand nach NREL-SPA (Reda & Andreas 2004) oder SunCalc (npm ohne Lizenzangabe, vermutlich BSD-2 [U]) plus Himmelsmodell. Für Präsentationen reicht das. Tageslicht-Nachweise sind ein eigenes Thema [U].

### Bausteine [V: Version/Lizenz per npm/PyPI]
| Baustein | Version | Lizenz | Rolle |
|---|---|---|---|
| IfcOpenShell | 0.8.5 | LGPL-3.0+ | IFC schreiben, tessellieren |
| three.js | 0.186.1 | MIT | Renderer |
| three-gpu-pathtracer | 0.0.24 | MIT | Pathtracing im Browser |
| @thatopen/components / fragments | 3.4.8 / 3.4.7 | MIT | BIM-Viewer (Texturunterstützung [U]) |
| web-ifc | 0.0.78 | MPL-2.0 | IFC im Browser |
| Babylon.js | 9.28.0 | Apache-2.0 | Alternative mit WebGPU |
| @gltf-transform/core | 4.5.0 | MIT | glTF-Nachbearbeitung, Varianten |
| @google/model-viewer | 4.3.1 | Apache-2.0 | AR (Android, iOS, WebXR) |
| MaterialX | 1.39.5 | Apache-2.0 [U] | Materialaustausch |
| OpenPBR | **1.1.1** (17.04.2026) | ASWF, Apache-2.0 [U] | Shading-Modell |
| usd-core (OpenUSD) | 26.8 | **TOST-1.0** (laut PyPI) | USDZ/USD-Export |

- **glTF oder USD:** glTF 2.0 (ISO/IEC 12113 [U]) ist das Liefer- und Web-Format mit ratifizierten KHR_materials-Erweiterungen [V]:
  - clearcoat, sheen, transmission, volume, ior, specular, iridescence, anisotropy, dispersion, emissive_strength, **variants**
  - diffuse_transmission ist Release Candidate.
- **OpenUSD:** die AOUSD Core Spec 1.0 ist seit 17.12.2025 ratifiziert [V]. USD ist das Autoren- und Austauschformat für Offline-Rendering und Apple.
- **Empfehlung:** GLB als Master, USDZ abgeleitet [U].
- **Konfiguratoren:**
  - Automotive-Konfiguratoren rendern meist serverseitig in Game-Engines und streamen das Bild. Threekit ist ein proprietäres SaaS-Beispiel [U, nicht geprüft].
  - Im Holzhaus-Markt ist der Stand niedrig: Regnauer bietet ein Formular, Bien-Zenker eine Online-Bemusterung ohne verifiziertes 3D [V, vgl. Recherche 04].

## 5. Reifegrade: präsentations-, prüf-, ausführungsfertig

**Normbezug:**
- **DIN EN ISO 7817-1:2024-11** ersetzt DIN EN 17412-1:2021-06; auf EN-Ebene ersetzt EN ISO 7817-1:2024 die EN 17412-1:2020 [V].
- Die LOIN-Rahmenbedingungen sind Zweck, Meilenstein, Akteure und Objekt.
- Die Informationsarten sind: geometrisch (Detail, Dimensionalität, Lage, **Appearance**, parametrisches Verhalten), alphanumerisch (Identifikation, Informationsgehalt) und Dokumentation.
- Teil 7817-3 (Schema) ist in Arbeit [U].
- BIMForum-LOD (Spec 2024, 31.12.2024; auf der Website liegt schon „LOD Spec 2025“ [U]) dient nur als Vergleich. Part I steht unter CC BY-NC-ND [V].
- „Fertigstellungsgrad“ ist ein Begriff aus der Praxis (BIM4INFRA), keine Norm [U]. Ich empfehle, ihn nicht zu verwenden.

| LOIN-Aspekt | R1 präsentationsfertig | R2 prüffertig | R3 ausführungsfertig |
|---|---|---|---|
| Zweck | Entscheidung des Kunden (Visualisierung, AR) | Regel-, Kompatibilitäts-, Kosten- und Normprüfung | Bestellung, Werkplanung, Montage, Übergabe |
| Meilenstein | Vorbemusterung, Angebot | Entwurf der Ausstattungsfestlegung | **unterschriebene Ausstattungsfestlegung, ≥ 12 Wochen vor Montage** (Regnauer) |
| Akteure | Kunde, Verkauf | Ausstatter, Projektleitung, TGA, Statik | Werkplanung, Einkauf, Montage |
| Detail/Dimension | 3D-Sichtgeometrie, Hersteller-Mesh oder generisch | Einbau- und Störraum (VDI 3805), Anschlussports | Einbaumaße, Anschlusslagen ± mm, Befestigung |
| Lage | Raum, grob | Wand/Raum, maßlich | exakt (Dosenlage, Achsen, Höhen) |
| **Appearance** | **PBR-Material, reale Texturgröße, Variante** | Farbcode (RAL/NCS [U]), Format | wie R2 plus Charge oder Sortierung |
| Parametrik | Variantenschalter | parametrische Typen (ETIM MC) | fixe Instanz |
| Identifikation | Katalog-Option-ID | ETIM-Klasse (bSDD-URI), Hersteller + Serie | **GTIN, Artikelnummer, Hersteller**, Menge |
| Informationsgehalt | Name, Bild, Preisindikation | Prüfmerkmale (Gewicht, Rλ,B, Format, Leistung, DN, Anschlusswerte), Mehrpreis, Lieferzeit | Bestellmenge inkl. Verschnitt, Liefertermin, Montagereihenfolge |
| Dokumentation | Disclaimer „unverbindlich“ (AGB § 2) | Datenblatt, Prüfprotokoll (BCF) | Montageanleitung, DoPC/DPP, Garantie (Pset_Warranty), IfcApproval |
| Prüfung | IDS „R1“ | IDS „R2“ + Regelmaschine | IDS „R3“ + Freigabe |

## 6. Konfigurationslogik

- **Regeltypen:**
  - Kompatibilität, z. B. Rahmen × Einsatz × Farbe oder Armatur × Waschtisch-Hahnloch
  - Abhängigkeit/Implikation, z. B. Dusch-WC → Steckdose im Vorwandelement
  - Ausschluss, z. B. Naturstein 60 × 120 auf Holzbalkendecke nur mit Nachweis
  - Mengen- und Preisformeln
  - Lieferzeit gegen Freeze-Termin
  - Budgetregel (Materialpreis-Deckel)
  - Mehrpreis für Beläge [U, Logik bei Regnauer offen]: `max(0; UVP − 50 €/m²) × Fläche × (1 + Verschnitt) + Verlegezuschlag`, für Parkett mit 80 €/m².
- **Standards mit Regelanteil:**
  - BMEcat 2005 `PRODUCT_CONFIG_DETAILS` (Schritte, Regeln, Formeln) [V]
  - DCC IDM (`DECISIONS`, `OPTION_COMBINATION`, `ACTIONS`, Formelstring) [V]
  - OFML/OCD [V]
  - VDI 3805 (Varianten per Funktion, Satzart 820) [V]
  - Einen herstellerübergreifenden Standard für Bau-Bemusterungsregeln habe ich **nicht gefunden** [U]. JUNG hat die Logik im Revit-Plug-in, aber nicht als offene Daten [V].
- **Technik** [U]:
  - Regeln als Daten (JSON/YAML mit bSDD-IDs), gerechnet mit einem Constraint-Solver.
  - OR-Tools CP-SAT (Apache-2.0) oder clingo (MIT) für Erklärungen und Minimalkorrekturen (Diagnose nach Felfernig et al.).
  - Merkmalspräsenz per IDS 1.0 (final seit 01.06.2024 [V]).
  - Ergebnisse als BCF.
- **Stand der Forschung:**
  - wissensbasierte Konfiguration (Felfernig et al. 2014)
  - SAT-Validierung im Automobilbau (Sinz et al. 2003)
  - Konfiguratoren im Bauwesen (Jensen et al. 2012, 2015; Wikberg et al. 2014)
  - **Bad-Konfigurator mit Installationsschacht** (Kudsk et al. 2013), dicht an unserem Fall.

## 7. Abhängigkeiten zu TGA und Tragwerk

| Auswahl | Wirkung | Regel/Quelle | Status |
|---|---|---|---|
| Wand-WC | Montageelement in der Holzständerwand: Ständer 60 × 80 mm, Beplankung beidseitig ≥ 18 mm, lichter Ständerabstand 50 cm, sonst Querriegel, 4 Befestigungspunkte | Geberit Baustelleneinweisung 06/2018 (DIN 4103-4) | [V] |
| Wand-WC-Last | Prüflast 400 kg für Wand-WCs | DIN EN 997 | [U, nicht eingesehen] |
| Bodengleiche Dusche mit Wandablauf | Estrichhöhe am Einlauf 65–90 mm oder 90–200 mm, je nach Element | Geberit Duofix-Sortiment | [V]; ↔ OG-Aufbau ca. 150 mm (BLB) |
| Dusch-WC | Strom- und Leerrohr am Montageelement | Geberit Produktübersicht 2025 | [V] → Elektro vor Wandfertigung |
| Badewanne 170/75 gefüllt | Beispielrechnung: ca. 180 l Wasser + Wanne 30 kg + Person 80 kg ≈ 2,9 kN auf 1,28 m² ≈ **2,3 kN/m²**, lokal über der Wohn-Nutzlast (A2: 1,5 kN/m²) | EN 1991-1-1/NA; Rechnung eigen | [U] → Statik je Grundriss |
| Naturstein/Großformat | Zusatzmasse → Eigenfrequenz der Decke, Durchbiegung; Fliese auf Estrich über Holzbalkendecke | BDF-Merkblatt 02-04 (in BLB zitiert); Holz als Fliesenuntergrund normativ nicht erfasst, 1–2 mm Durchbiegung schadensrelevant | [V/U] |
| Parkett auf FBH | Rλ,B ≤ 0,15 m²K/W; Oberfläche ≤ 29 °C; **schwimmend nur bedingt geeignet** (Luftschicht, Unterlage) | BVPF/VdP-Merkblatt, Weitzer MB-020 | [V]; Konflikt mit Regnauer-Standard „schwimmend“ |
| Feuchtraum | Abdichtung, Ständerabstand und Beplankung für Fliesen im Holzbau (z. B. 12,5 mm GK bis 420 mm Achse) | Merkblatt „Bäder und Feuchträume im Holzbau und Trockenbau“ (Herausgeber [U]), DIN 18534 | [V/U] |
| Innentür bei KWL | Überströmung per Türunterschnitt: 0,32 × Länge × Höhe m³/h bei 1 Pa; Bad 75–100 cm² | DIN 1946-6 (Beispielauslegung), Herstellerblatt | [V/U] |
| Dunstabzug, Kaminofen | Abluft mit KWL und raumluftabhängiger Feuerstätte nur mit Sicherheitseinrichtung, sonst Umluft | DIN 1946-6, FeuVO | [U] |
| Einbauleuchten | Decke: 25 mm GK auf **30 mm Abstandsschalung mit Schwingungselementen** → Einbautiefe, Schall, F30 B; unter dem Dach liegt die Dampfbremse direkt dahinter | BLB 10/2024; Folgerung eigen | [U] → Frage an Regnauer |
| Steckdosen Außenwand | Dampfbremse direkt hinter der Gipslage → luftdichte Dosen oder Verzicht | BLB; DIN 4108-7 | [U] |
| Hängeschränke Küche | „an jeder Stelle“ möglich (25 mm Gips) | BLB | [V] |

## Literatur (DOI per Crossref geprüft [V])

1. Felfernig, A.; Hotz, L.; Bagley, C.; Tiihonen, J. (Hrsg.) (2014): *Knowledge-Based Configuration: From Research to Business Cases.* Morgan Kaufmann. doi:10.1016/C2011-0-69705-4
2. Sabin, D.; Weigel, R. (1998): Product configuration frameworks – a survey. *IEEE Intelligent Systems* 13(4), 42–49. doi:10.1109/5254.708432
3. Sinz, C.; Kaiser, A.; Küchlin, W. (2003): Formal methods for the validation of automotive product configuration data. *AI EDAM* 17(1). doi:10.1017/S0890060403171065
4. Forza, C.; Salvador, F. (2002): Managing for variety in the order acquisition and fulfilment process: The contribution of product configuration systems. *Int. J. Production Economics* 76(1), 87–98. doi:10.1016/S0925-5273(01)00157-8
5. Hvam, L.; Mortensen, N. H.; Riis, J. (2008): *Product Customization.* Springer. doi:10.1007/978-3-540-71449-1
6. Haug, A.; Shafiee, S.; Hvam, L. (2019): The costs and benefits of product configuration projects in engineer-to-order companies. *Computers in Industry.* doi:10.1016/j.compind.2018.11.005
7. Barlow, J. et al. (2003): Choice and delivery in housebuilding: lessons from Japan for UK housebuilders. *Building Research & Information* 31(2), 134–145. doi:10.1080/09613210302003
8. Jensen, P.; Olofsson, T.; Johnsson, H. (2012): Configuration through the parameterization of building components. *Automation in Construction* 23, 1–8. doi:10.1016/j.autcon.2011.11.016
9. Jensen, P.; Lidelöw, H.; Olofsson, T. (2015): Product configuration in construction. *Int. J. Mass Customisation.* doi:10.1504/IJMASSC.2015.069601
10. Wikberg, F.; Olofsson, T.; Ekholm, A. (2014): Design configuration with architectural objects. *Construction Management and Economics* 32(1–2), 196–207. doi:10.1080/01446193.2013.864780
11. Kudsk, A.; Hvam, L.; Thuesen, C. (2013): Using a configuration system to design toilets and place installation shafts. *Open Construction and Building Technology Journal* 7. doi:10.2174/1874836801307010158
12. Abualdenien, J.; Borrmann, A. (2022): Levels of detail, development, definition, and information need: a critical literature review. *ITcon* 27. doi:10.36680/j.itcon.2022.018
13. Du, J.; Zou, Z.; Shi, Y.; Zhao, D. (2018): Zero latency: Real-time synchronization of BIM data in virtual reality for collaborative decision-making. *Automation in Construction.* doi:10.1016/j.autcon.2017.10.009
14. Reda, I.; Andreas, A. (2004): Solar position algorithm for solar radiation applications. *Solar Energy* 76(5), 577–589. doi:10.1016/j.solener.2003.12.003

**Normen und Spezifikationen** (ohne DOI):
- ISO 16739-1:2024
- DIN EN ISO 7817-1:2024-11
- ISO 23386:2020, ISO 23387:2025
- VDI 3805 Bl. 1 und 45
- DIN 1946-6:2019-12, DIN EN 1264-3:2021-08
- IDS 1.0 (buildingSMART, 2024)
- glTF 2.0 und Khronos Extension Registry
- AOUSD Core Spec 1.0.1
- OpenPBR 1.1.1
- ETIM MC Guidelines 2.0
- Verordnungen (EU) 2024/1781 und 2024/3110

## Korrekturen/Warnungen

1. **EN 17412-1 ist ersetzt:** DIN EN ISO 7817-1:2024-11 [V]. Die Muster-AIA von BIM Deutschland (05/2023) zitieren noch EN 17412-1.
2. **ISO 23387:2020 ist zurückgezogen:** ISO 23387:2025 bzw. DIN EN ISO 23387:2026-01 [V]. Ob ISO 23386:2020 revidiert wurde, habe ich nicht geprüft [U].
3. **„ETIM 9/10“:** gültig ist ETIM 10.0 vom 05.12.2024. ETIM Deutschland schreibt fälschlich „exakt ein Jahr“ nach 9.0 (05.12.2022). Das Austauschformat der Zukunft ist ETIM xChange 2.0, nicht BMEcat.
4. **ECLASS ist nicht frei;** der bSDD-Status ist offen. ETIM ist frei, verlangt aber Namensnennung (ODC-By).
5. **„VDS-Datenstandard“ existiert nicht** (nicht gefunden). Für Sanitär gelten VDI 3805 Bl. 45, ETIM und DQR.
6. **Korrekturen an Recherche 04:**
   - Duravit gibt es auch als IFC (über BIMobject, IFC2X3).
   - Geberit liefert auch Datenpakete im Katalog, nicht nur das Revit-Plug-in.
   - Die Riegelstärke laut BLB 10/2024 ist 200 mm.
7. **IfcOpenShell-glTF verliert Texturen und UVs** [V]. Einen texturierten IFC→glTF-Weg ohne eigenen Code gibt es nicht [U].
8. **Hersteller-IFC ist oft nicht 4.3-tauglich:** IFC2X3, falsche oder NOTDEFINED-Typen, leere GTIN [V]. Deshalb **nur die Geometrie übernehmen** und Typ, Pset und Klassifikation selbst erzeugen.
9. **Lizenz der Texturen:** mtextur verbietet Web-Apps [V]. HARO, V&B und die anderen müssen schriftlich zustimmen. CC0-Material stellt nicht das Originalprodukt dar, also im Viewer als „ähnlich“ kennzeichnen [U].
10. **Präsentation ist nicht Vertrag:** Regnauer schließt die Verbindlichkeit von Visualisierungen aus (AGB § 2) [V]. Farbtreue auf Bildschirmen ist nicht zusicherbar, mtextur schließt sie selbst aus [V].
11. **DPP:** Für Bauprodukte gilt die CPR 2024/3110 und nicht die ESPR. Die Pflicht ist noch nicht in Kraft [V]. Wärmepumpen und PV fallen vorrangig unter die ESPR.
12. **three.js WebGPURenderer** ist „experimental“ [V]. WebGPU läuft seit 11/2025 in allen großen Browsern, Linux und Firefox-Android fehlen noch [V].
13. **Die OpenUSD-Lizenz** ist laut PyPI „TOST-1.0“, nicht Apache. Vor der Weitergabe prüfen [U].
14. **Parkett schwimmend auf FBH** (Regnauer-Standard) ist nach Branchenmerkblättern nur bedingt geeignet [V]. Rλ,B muss je Belag geprüft werden.

## Offene Fragen an Regnauer

1. **Bemusterungskatalog als Daten:** Liegen alle Optionen mit Regnauer-Nr., Hersteller-Artikelnr., GTIN, Mehr- oder Minderpreis, Lieferzeit und Gültigkeit vor, und in welchem System und Format (ERP-Export, Excel, BMEcat)?
2. **Bemusterungssoftware in Seebruck:** Gibt es eine Online-Vorbemusterung? Wie ist der Ausstattungsplan nach § 650n aufgebaut? Würde ein IFC- oder PDF-Ausstattungsplan akzeptiert?
3. **Freeze-Termine:** Wann müssen Elektro-Auslässe, Sanitärobjekte, Sonnenschutz und Smart Home festliegen, relativ zur Werkplanung? Was kostet eine Änderung danach?
4. **Sanitär:** Welche Hersteller stehen hinter „Derby, Tesi, Lua“ und den Design-Linien? Welches Vorwand- und Montagesystem ist in der Wand (Geberit, TECE, eigenes)? Mit welchem Ständerraster?
5. **Elektro:** Welche Marke und welche Aufpreisprogramme hat das Schalterprogramm? Welche Dosentypen gibt es in der Außenwand ohne Installationsebene (luftdicht)? Was steckt im Smart-Home-Paket (KNX oder Funk)?
6. **Fliesen und Naturstein:** Gibt es Grenzwerte für Format und Flächenlast auf der Silence-Decke? Wie wird der Mehrpreis für Großformate und andere Verlegearten berechnet?
7. **Parkett auf FBH:** Welche Rλ,B hat die Musterkollektion? Bleibt es bei schwimmender Verlegung, oder ist Verkleben möglich?
8. **Einbauleuchten:** Sind sie in Decke und Dachschräge zulässig (30-mm-Ebene, Schall, F30 B)?
9. **Fenster:** Wie heißen die 11 Alu-Farben (RAL-Codes), und welche Innenfarben gibt es? Wie wirken die Sprossentypen auf Uw? Wie ist der Rollladen- oder Raffstorekasten konstruiert (Sturz, Wandaufbau)?
10. **Dach und Fassade:** Welche Ziegelmodelle und -farben gibt es? Wer prüft gegen den Bebauungsplan?
11. **Preislogik:** Wie genau werden die Budgets (50/80 €/m² UVP) verrechnet, mit Verschnitt und Verlegezuschlag?
12. **Rechte:** Darf Regnauer Bilder, Texturen und BIM-Daten der Partner (HARO, Herholz, Sanitärhersteller) in einem Web-Konfigurator nutzen?
13. **Lüftung:** Wie ist die Überströmung gelöst (Unterschnitt oder Dichtung)? Ist der Dunstabzug Pflicht Umluft? Welche Regeln gelten für Kaminöfen zusammen mit Proxon?
14. **Küche:** Wie läuft die Schnittstelle zum Küchenstudio (Anschlussplan, IDM-Daten)? Bis wann muss der Plan vorliegen?
15. **Eigenleistungspakete:** Wofür stehen SF1, SF2, TA1–TA3 und TBH? Wie sollen bauherrenseitige Leistungen im Modell gekennzeichnet werden?

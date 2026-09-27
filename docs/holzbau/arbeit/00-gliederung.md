# Durchgängige, regelbasierte Entwurfs- und Fertigungskette für Holzrahmenbau-Fertighäuser auf Basis von IFC 4.3

**Untertitel:** Ein Design-Science-Ansatz für kundengesteuerten Entwurf mit Sprachschnittstelle, Regelprüfung nach deutschem Bau- und Handwerksrecht und Ableitung von Bauvorlagen und Maschinendaten aus einem einzigen Informationsmodell

Status: Gliederung v0.3 (27.09.2026): Umfang erweitert um Bemusterung, TGA mit Routing, Dach und Fassade im Detail, 3D-Präsentation, vollständigen Innenausbau- und Interior-Katalog sowie alle Wohngebäudetypen

---

## Leitlinien für die Arbeit

1. **Jede Quelle ist verifiziert.** Autor, Jahr, Titel, Venue und DOI sind über Crossref oder die Verlagsseite geprüft. Normen, Gesetze und graue Literatur sind als solche gekennzeichnet.
2. **Jedes technische Argument hat ein Beispiel.** Beispiele sind lauffähig, deterministisch und mit Tests versehen (`beispiele/`).
3. **Trennung von Befund und Bewertung.** Recherchebefunde tragen den Status [V] (verifiziert) oder [U] (unsicher). Eigene Bewertungen sind als solche formuliert.
4. **Keine Rechtsberatung.** Rechtliche Kapitel sind Befunde zur Rechtslage mit Paragrafen-Nachweis.
5. **Zitierweise:** Autor-Jahr, Pandoc-Syntax `[@key]`, Literaturverzeichnis als BibTeX (`literatur/*.bib`).

---

## Forschungsfragen

- **FF1 Informationsmodell:** Lässt sich die Informationskette eines Holzrahmenbau-Fertighauses von der Kundenidee über Vertrag, Bauantrag und Nachweise bis zur Fertigung standardkonform in einem IFC-4.3-Modell abbilden? Wo liegen die Grenzen, und wie werden sie ohne proprietäre Erweiterung überbrückt?
- **FF2 Regelraum:** Wie lassen sich öffentlich-rechtliche Regeln, Normen, Handwerksregeln und Herstellerregeln so formalisieren, dass sie einen Laienentwurf in Echtzeit begrenzen und das Ergebnis maschinell prüfbar machen (IDS)?
- **FF3 Sprachschnittstelle:** Wie wird gesprochene deutsche Sprache zuverlässig in deterministische Modelländerungen übersetzt? Welche Aufgaben übernimmt das Sprachmodell, welche der Code?
- **FF4 Verantwortung:** Welche Freigaben verlangt das deutsche Recht, und wie werden sie im Modell nachvollziehbar abgebildet?
- **FF5 Wirkung:** Welche Wirkung hat das System auf Durchlaufzeit, Planungsschleifen, Fehlerquote und die Arbeitsteilung zwischen Kunde, Vertrieb, Architekt, Ingenieur und Werk?
- **FF6 Detailtiefe:** Wie werden Bemusterung, Technische Gebäudeausrüstung (Elektro, Netzwerk, Lüftung, Heizung, Trinkwasser kalt/warm, Abwasser, Licht, PV) sowie Dach und Fassade mit allen Details und Einbauteilen regelbasiert erzeugt? Die drei Reifegrade präsentationsfertig, prüffertig und ausführungsfertig sollen dabei aus demselben Modell entstehen.

## Thesen

1. **Keine neue Grundlagentechnik nötig.** Für den Einfamilienhaus-Holzrahmenbau existieren alle nötigen Bausteine: Datenstandard, Regeln, Kennwerte und Rechenkerne. Der Beitrag der Arbeit ist ihre **Integration** in ein standardkonformes Informationsmodell.
2. **Der Regelraum ist entscheidend, nicht die KI.** Qualität und Haftbarkeit des Ergebnisses hängen an der Formalisierung der Regeln, nicht am Sprachmodell.
3. **IFC 4.3 trägt die Kette bis zur Werkplanung vollständig.** Maschinendaten und Einreichungsformate lassen sich verlustfrei und automatisch ableiten, sind aber immer Ableitungen.

---

## Teil I: Grundlagen

### 1. Einleitung
1. Problemstellung: Planungsschleifen, Medienbrüche, Fachkräftemangel
2. Zielsetzung und Why (Golden Circle, siehe `../00-zielbild.md`)
3. Forschungsfragen und Thesen
4. Abgrenzung: alle Wohngebäudetypen vom Einfamilienhaus über Zweifamilien-, Doppel- und Reihenhaus bis zum Mehrfamilienhaus und Geschosswohnungsbau in Holz (GK 1–5), Holzbau (Schwerpunkt Holzrahmenbau), Bayern als Referenzbundesland
5. Aufbau der Arbeit

### 2. Forschungsdesign
1. Design Science Research als Rahmen (Hevner 2004, Peffers 2007, Gregor & Hevner 2013)
2. Vorgehen: Problem → Ziele → Artefakt → Demonstration → Evaluation → Kommunikation
3. Recherchemethodik: systematische Literatur- und Quellenrecherche, Verifikationsregeln [V]/[U]
4. Evaluationsdesign: technisch (Beispiele, Tests), analytisch (Abdeckungsmatrix), empirisch (Experteninterviews, Nutzerstudie)
5. Gütekriterien: Reproduzierbarkeit, Nachvollziehbarkeit, Standardkonformität

### 3. Holzrahmenbau und Fertighausindustrie
1. Bauweise: Ständer, Beplankung, Dämmung, Luftdichtheit, Verbindungsmittel
2. Industrielle Vorfertigung: Wandtafel, Decke, Dach, Abbund, Wandanlagen
3. Markt: Fertigbauquote 26,5 % (DE), 27,5 % (BY) 2025
4. Prozess heute: Beratung → Entwurf → Vertrag → Bemusterung → Bauantrag → Werkplanung → Fertigung → Montage
5. Fallbeispiel Regnauer: Produkte, Aufbauten, Konfigurator

### 4. Rechtlicher und normativer Rahmen
1. Bauplanungsrecht: BauGB, BauNVO, Bebauungsplan, XPlanung
2. Bauordnungsrecht Bayern: Abstandsflächen, Gebäudeklassen, Vollgeschoss, Bauvorlageberechtigung, Freistellung, Typengenehmigung
3. Technische Baubestimmungen: BayTB, HolzBauRL, EC 5, DIN 4102-4, DIN 4109, DIN 68800
4. Energie: GModG 2026, DIN V 18599, Modellgebäudeverfahren, EPBD
5. Vertragsrecht: Verbraucherbauvertrag, Baubeschreibung Art. 249 EGBGB
6. Handwerk und Güte: Fachregeln Zimmerer, ZVDH, RAL-GZ 422, QDF
7. Querschnitt: Produkthaftung, AI Act, DSGVO, BFSG, Urheberrecht an Normen

### 5. Stand der Forschung und Technik
1. BIM und IFC: Entwicklung, IFC 4.3 / ISO 16739-1:2024, MVD, IDS, IFC5
2. Automatisierte Regelprüfung: von Eastman 2009 bis zu LLM-basierten Ansätzen; digitaler Bauantrag
3. Digitale Prozesskette im Holzbau: BIMwood, compas_timber, BTLx, WUP
4. Mass Customization und Produktkonfiguration im Hausbau
5. Generatives Design, Grundriss- und Möblierungssolver
6. Sprach- und Sprachmodell-Schnittstellen in AEC: Text2BIM, NADIA-S, Intent-Modelle
7. Vergleichbare Arbeiten: Dissertationen und Projekte zu Vorfertigung, Konfiguration, Design Automation, Compliance-by-Design, TGA-Routing und Dachautomatisierung, gegenübergestellt in einer Vergleichsmatrix. Dazu, was sich übernehmen lässt und was zu vermeiden ist
8. Forschungslücken und Abgrenzung der eigenen Arbeit

---

## Teil II: Konzept

### 6. Anforderungen
1. Stakeholder und Rollen
2. Funktionale Anforderungen je Phase
3. Nichtfunktionale Anforderungen: Standardkonformität, Determinismus, Latenz, Datenschutz, Barrierefreiheit
4. Harte Grenzen aus Recht und Norm

### 7. Systemarchitektur
1. Neuro-symbolische Trennung: Sprachmodell entscheidet über die Absicht, der Code rechnet
2. Parametermodell → IFC-Generator → Prüfschicht → Ableitungen
3. Deterministische GUIDs, Versionierung, Undo, Audit-Trail
4. Bausteinwahl: übernehmen, adaptieren oder selbst bauen (mit Lizenzanalyse)

### 8. Informationsmodell
1. Schemawahl IFC4X3_ADD2, Fallback IFC4
2. Holzrahmenbau-Klassenmapping (IfcWall/Aggregation, IfcMember STUD/PLATE, IfcPlate, IfcBuildingElementPart, IfcVoidingFeature, IfcMechanicalFastener)
3. Doppelte Darstellung: Schichtenmodell und Einzelteile
4. Phasenabdeckung: Kosten, Vertrag, Bemusterung, Bauantrag, Nachweise, Fertigung, Montage, Übergabe
5. Klassifikation und Merkmale: bSDD, BIM-Portal des Bundes, dataholz
6. Grenzen und standardkonforme Überbrückung

### 9. Regelraum
1. Taxonomie der Regeln: Gesetz, Norm, Handwerk, Hersteller, Kunde
2. Formalisierung: IDS (Informationsanforderungen) und ausführbare Regeln (Geometrie, Berechnung)
3. Regelwerk-Profile und Versionierung (z. B. GEG → GModG)
4. Beispiele: Abstandsflächen, Vollgeschoss, Treppe, Fensterfläche, Dachneigung, Bewegungsflächen
5. Ablehnen mit Begründung und Alternative
6. Rechtliche Nutzung von Normwerten

### 9a. Gebäudetypen und typabhängige Regelprofile
1. Typologie: EFH, EFH mit Einliegerwohnung, ZFH, Doppelhaus, Reihenhaus, MFH, Geschosswohnungsbau in Holz
2. Regeldeltas je Typ: Gebäudeklasse, Bauvorlageberechtigung, Prüfpflichten, Brand- und Schallschutz zwischen Nutzungseinheiten, Barrierefreiheit, Aufzug, Spielplatz, Stellplätze
3. Wohnfläche (WoFlV), Flächen (DIN 277), Wohnungseigentum (Aufteilungsplan, Abgeschlossenheit)
4. Holzbau in GK 4/5 nach HolzBauRL 2024
5. Gebäudetyp E und Typengenehmigung für serielles Bauen

### 9b. Entwurfsqualität: Architekturpsychologie und Kulturprofile
Assistenz statt Vorschrift. Das System hilft Laien, gute Räume zu planen, ohne sie zu bevormunden.

1. Regelklasse R5 „Empfehlungen“: weiche Regeln mit Score, Begründung und Evidenzgrad; getrennt von den harten Regeln R1–R4
2. Evidenzbasierte Wirkfaktoren:
   - Tageslicht, Blick ins Grüne, Prospect-Refuge
   - Raumhöhe, Privatheitsgradient, Crowding, Akustik
   - Orientierung (Space Syntax)
3. Rechenbares Grundrisswissen:
   - Raumbeziehungen, Zonierung, Himmelsrichtungen
   - Möblierbarkeit, Stauraum, Verkehrsflächenanteil
4. Wohnqualitäts-Scoring, z. B. nach dem Schweizer Wohnungs-Bewertungs-System (WBS)
5. Kulturprofile als optionale Wahl des Kunden: Feng Shui, Vastu, Baubiologie. Jede Regel wird mit Evidenzgrad gekennzeichnet und mit evidenzbasierten Faktoren abgeglichen (z. B. Feng-Shui-„Kommandoposition“ ≈ Prospect-Refuge)
6. Evidenzgrad-Schema (A Meta-Analyse bis D Tradition ohne empirische Prüfung) und Ethik der Assistenz (Nudging, Transparenz)

### 10. Sprachschnittstelle
1. Spracherkennung Deutsch: Streaming, Fachbegriffe
2. Intent-Erkennung mit typisierten Fragen (choice, score, noul), Kalibrierung, Hierarchie unter 20 Optionen
3. Deterministischer Werteparser und Referenzauflösung
4. Fehlerbehandlung, Rückfragen, Transparenz nach AI Act

### 11. Reifegrade: präsentationsfertig, prüffertig, ausführungsfertig
1. Informationsbedarf nach Level of Information Need (DIN EN ISO 7817-1) **[prüfen]**
2. Reifegrad P (präsentationsfertig): Geometrie, Materialien und Oberflächen für fotorealistisches 3D und AR
3. Reifegrad R (prüffertig): alle Merkmale für Regel-, Nachweis- und Kostenprüfung
4. Reifegrad A (ausführungsfertig): bestellbare Artikel, Einbauinformation, Fertigungsteile, Maschinendaten
5. Reifegrade je Bauteilgruppe und Phase, geprüft über IDS je Reifegrad

### 12. Bemusterung, Innenausbau und Interior-Katalog
Leitbild: eine ernsthafte, an die deutsche Bauwirtschaft angebundene Version des Baumodus von „Die Sims“. Es ist ein Hausplaner, kein Lebenssimulator: Jedes Element ist ein realer, bestellbarer, normkonformer Artikel.

1. Taxonomie der Bemusterung: Fenster, Türen, Treppe, Böden, Fliesen, Sanitär, Elektro-Schalterprogramm, Heizung, Lüftung, Oberflächen, Fassade, Dach, Außenanlagen
2. Innenausbau im Detail:
   - Fliesen: Format, Rutschhemmung, Verlegemuster, Fugenbild und Fugenfarbe, Abdichtung
   - Parkett und Böden: Holzart, Sortierung, Oberfläche, Verlegemuster, Sockelleisten, Übergänge
   - Fußbodenaufbau mit Höhenausgleich: Estrich-, Dämm- und Ausgleichsschichten werden je Raum so berechnet, dass die Fertigfußbodenhöhe bei Parkett, Feinsteinzeug, Naturstein, Beton Ciré und Vinyl gleich bleibt. So entstehen keine Kanten an Übergängen, einschließlich schwellenfreier Duschen
   - Wandfarben, Putze einschließlich Keller, Oberflächenqualität Q1–Q4
   - Treppenformen, Stufenverziehung, Holzarten, Geländer
   - Innentüren und Beschläge
   - Sanitärobjekte mit Bewegungsflächen
   - Küche
3. Möblierung in 3D: Datenstandards für konfigurierbare Möbel (IDM des DCC, OFML), Stell- und Bewegungsflächen
4. Festschreibung und Suchbarkeit: eindeutige Spezifikation je Auswahl (Artikel + Farbe + Oberfläche + Format + Muster + Fuge), gestuft nach Reifegrad P/R/A
5. Abhängigkeiten zwischen Optionen (z. B. Wand-WC → Vorwand → Tragständer → Abwasser)
6. Produktdatenstandards: ETIM, ECLASS, BMEcat, VDI 3805, GTIN, Product Data Templates (ISO 23386/23387) und ihre Kopplung an IFC
7. Konfigurationslogik: wissensbasierte Konfiguration, Kompatibilität, Mehrpreise, Lieferzeiten
8. Abgrenzung zu Consumer-Planern (Planner 5D, Roomle, IKEA Kreativ) und Fachsoftware (Palette CAD, Pytha)

### 13. Technische Gebäudeausrüstung und automatisches Routing
1. Elektro und Netzwerk: DIN 18015 mit Installationszonen, Mindestausstattung, Schutzbereiche im Bad, Zählerschrank, Wohnungsverkabelung
2. Trinkwasser kalt/warm, Zirkulation, Hygiene
3. Abwasser mit Lüftung über Dach
4. Lüftung nach DIN 1946-6 mit Kanalnetz
5. Heizung: Heizlast, Wärmepumpe (Aufstellung, Schall), Fußbodenheizung, hydraulischer Abgleich
6. Lichtplanung: Leuchtendaten (GLDF, EULUMDAT), Tageslicht
7. IFC-Abbildung: Systeme, Segmente, Ports, Verbindungen, Durchbrüche
8. Dimensionierung (Nennweiten, Dämmstärken) und Durchdringungen:
   - Lage und Größe von Bohrungen in Ständern und Balken, Wechsel in Holzbalkendecken
   - Luftdichtheitsmanschetten, Brand- und Schallschutzabschottungen
   - Übergabe als BTLx- bzw. WUP-Bearbeitung
9. Routing-Algorithmen unter Regeln (Installationszonen, Ständerschwächung, Luftdichtheit, Kollisionsfreiheit)

### 14. Dach, Fassade und Einbauteile
1. Dachformen: Sattel, Walm, Krüppelwalm, Zelt, Pult, Mansarde, Gauben; Geometrie über Straight Skeleton
2. Dachtragwerk: Sparren, Pfetten, Grat- und Kehlsparren, Schifter, Wechsel
3. Deckung: Ziegelformen und Farben, Lattung, First, Grat, Kehle, Ortgang, Traufe, Mansardenknick nach ZVDH
4. Einbauteile: Dachfenster mit Eindeckrahmen, Lüfterziegel/Sanitärlüfter, Solar- und Antennendurchgänge, Schneefang, Dachtritte
5. Dachentwässerung nach DIN 1986-100 mit Regenspende (KOSTRA-DWD)
6. Photovoltaik: Belegung, Randabstände, Ertrag (pvlib, PVGIS), Anmeldung
7. Fassadenvarianten: Holzschalung nach Fachregel 01, Putz auf Holzfaser, Farben, Gestaltungssatzungen

### 15. Fachmodule
1. Energie: H'T, Modellgebäudeverfahren, Monatsbilanz, Space Boundaries
2. Tragwerk: Vorbemessung nach EC 5 mit deutschem NA
3. Brand- und Schallschutz
4. Mengen, Kosten (DIN 276, GAEB), Ökobilanz (ÖKOBAUDAT, QNG)

### 16. 3D-Präsentation
1. IFC → glTF/USD mit PBR-Materialien
2. Materialbibliotheken und Herstellertexturen (Lizenzen)
3. Browser-Rendering, Pfadverfolgung, AR auf dem Grundstück
4. Sonnenstand, Tageslicht, Innenraumansichten

### 17. Fertigung
1. Vom IFC zu BTLx (Abbund) und WUP (Wandanlage)
2. Werkseitige Vorinstallation: Leerrohre, Dosen, Vorwandelemente
3. Fertigungsregeln: Elementgrößen, Transport, Raster
4. Verbindungsmittel und Nagelbilder

### 18. Freigaben und Bauantrag
1. Freigabe-Gates: Vertrag, Bauvorlage, Statik, Produktion
2. IfcApproval, IfcActor, IfcPermit
3. Ableitung von Bauvorlagen nach BauVorlV (PDF 1:100, Lageplan, Baubeschreibung) und XBau
4. Perspektive: modellbasierte Genehmigung

---

## Teil III: Validierung

### 19. Prototyp und Beispiele
- B1 Wandelement in IFC4X3 mit deterministischen GUIDs
- B2 IDS-Profil Holzrahmenbau und Prüfung
- B3 U-Wert nach DIN EN ISO 6946
- B4 Abstandsflächen nach BayBO Art. 6
- B5 Treppe nach DIN 18065
- B6 Sprachpipeline: Werteparser, Raumreferenz, Intent-Anwendung mit Regelprüfung
- B7 (geplant) Walmdach über Straight Skeleton mit Deckung, Grat und Kehle
- B8 (geplant) Routing einer Abwasser- und einer Elektroleitung unter Installationszonen
- B9 (geplant) Bemusterungsoption Wand-WC mit Folgeänderungen an Vorwand, Ständer und Abwasser
- B11 (geplant) Fliesenverlegung mit Verlegemuster, Fugenbild und Schnittplan als festgeschriebene Auswahl
- B12 (geplant) Wechsel des Gebäudetyps EFH → ZFH mit automatisch umgeschaltetem Regelprofil
- B14 Fußbodenaufbau-Solver: gleiche Fertigfußbodenhöhe über vier Beläge mit Fußbodenheizung
- B15 (geplant) Durchdringung einer Abwasserleitung DN 100 durch Holzbalkendecke und Ständerwand mit Bohrungsprüfung, Durchbruch, Wechsel und Manschette
- B13 (geplant) Assistenz: Grundriss-Score (Tageslicht, Zonierung, Space-Syntax-Integration) mit Empfehlung, Begründung und Evidenzgrad; optional Feng-Shui-Profil
- B10 (geplant) glTF-Export mit PBR-Materialien

### 20. Evaluation
1. Technische Evaluation: Tests, Validierung, Round-Trip in Fremdsoftware
2. Analytische Evaluation: Abdeckungsmatrix Phase × IFC-Mechanismus × Regelquelle
3. Empirische Evaluation (Plan): Experteninterviews (Architekt, Tragwerksplaner, Werkplaner, Vertrieb), Nutzerstudie mit Kunden, Kennzahlen bei Regnauer

### 21. Diskussion
1. Beantwortung der Forschungsfragen
2. Grenzen der Arbeit
3. Übertragbarkeit auf andere Hersteller und Bundesländer

### 22. Fazit und Ausblick

---

## Anhänge
- A Quellenverzeichnis der Recherche (`../recherche/`)
- B Literaturverzeichnis (`literatur/`)
- C Beispielcode und Ergebnisse (`beispiele/`)
- D Fragenkatalog an Regnauer
- E Glossar

---

## Offene Aufgaben für die empirische Evaluation

Eine Doktorarbeit braucht eigene empirische Daten. Folgende Daten kann nur die Praxis liefern:

1. **Ausgangswerte bei Regnauer:** Durchlaufzeiten, Anzahl der Planstände je Projekt, Änderungsaufwand im Vertrieb (aus CRM und CAD-Versionen).
2. **Experteninterviews:** 6–10 Personen aus Vertrieb, Planung, Statik und Werk.
3. **Nutzerstudie:** Laien entwerfen mit dem Prototyp. Gemessen werden Aufgabenerfolg, Zeit, Regelverstöße und Zufriedenheit.

# Durchgängige, regelbasierte Entwurfs- und Fertigungskette für Holzrahmenbau-Fertighäuser auf Basis von IFC 4.3

**Untertitel:** Ein Design-Science-Ansatz für kundengesteuerten Entwurf mit Sprachschnittstelle, Regelprüfung nach deutschem Bau- und Handwerksrecht und Ableitung von Bauvorlagen und Maschinendaten aus einem einzigen Informationsmodell

Status: Gliederung v0.1 (27.09.2026)

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
4. Abgrenzung: Einfamilien- und Doppelhaus, Holzrahmenbau, Bayern, GK 1–3
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
7. Forschungslücken

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

### 10. Sprachschnittstelle
1. Spracherkennung Deutsch: Streaming, Fachbegriffe
2. Intent-Erkennung mit typisierten Fragen (choice, score, noul), Kalibrierung, Hierarchie unter 20 Optionen
3. Deterministischer Werteparser und Referenzauflösung
4. Fehlerbehandlung, Rückfragen, Transparenz nach AI Act

### 11. Fachmodule
1. Energie: H'T, Modellgebäudeverfahren, Monatsbilanz, Space Boundaries
2. Tragwerk: Vorbemessung nach EC 5 mit deutschem NA
3. Brand- und Schallschutz
4. Mengen, Kosten (DIN 276, GAEB), Ökobilanz (ÖKOBAUDAT, QNG)

### 12. Fertigung
1. Vom IFC zu BTLx (Abbund) und WUP (Wandanlage)
2. Fertigungsregeln: Elementgrößen, Transport, Raster
3. Verbindungsmittel und Nagelbilder

### 13. Freigaben und Bauantrag
1. Freigabe-Gates: Vertrag, Bauvorlage, Statik, Produktion
2. IfcApproval, IfcActor, IfcPermit
3. Ableitung von Bauvorlagen nach BauVorlV (PDF 1:100, Lageplan, Baubeschreibung) und XBau
4. Perspektive: modellbasierte Genehmigung

---

## Teil III: Validierung

### 14. Prototyp und Beispiele
- B1 Wandelement in IFC4X3 mit deterministischen GUIDs
- B2 IDS-Profil Holzrahmenbau und Prüfung
- B3 U-Wert nach DIN EN ISO 6946
- B4 Abstandsflächen nach BayBO Art. 6
- B5 Treppe nach DIN 18065
- B6 Sprachpipeline: Werteparser, Raumreferenz, Intent-Anwendung mit Regelprüfung

### 15. Evaluation
1. Technische Evaluation: Tests, Validierung, Round-Trip in Fremdsoftware
2. Analytische Evaluation: Abdeckungsmatrix Phase × IFC-Mechanismus × Regelquelle
3. Empirische Evaluation (Plan): Experteninterviews (Architekt, Tragwerksplaner, Werkplaner, Vertrieb), Nutzerstudie mit Kunden, Kennzahlen bei Regnauer

### 16. Diskussion
1. Beantwortung der Forschungsfragen
2. Grenzen der Arbeit
3. Übertragbarkeit auf andere Hersteller und Bundesländer

### 17. Fazit und Ausblick

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

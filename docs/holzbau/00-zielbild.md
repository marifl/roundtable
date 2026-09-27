# Zielbild: Vom Kundenwunsch bis ins Werk in einer IFC-Datei

Status: v0.3 (27.09.2026): Interior-Katalog und alle Gebäudetypen ergänzt. Die Prüfmarker aus v0.1 sind mit Quellen aufgelöst; die Belege stehen in `recherche/01` bis `07`.

Aufbau nach Simon Sineks Golden Circle: erst Why, dann How, dann What.

---

## 0. Endergebnis

**Eine voll funktionierende App.** Die wissenschaftliche Arbeit in `arbeit/` ist ihre fachliche Grundlage. Jedes Kapitel endet mit Umsetzungsvorgaben, die direkt in Code, Regelkataloge und Tests übergehen.

---

## 1. Why

**Fertighauskunden entwerfen ihr Haus selbst, innerhalb der Regeln der Firma.**

So kann sich jede Rolle wieder auf ihre eigentliche Arbeit konzentrieren:

| Rolle | Heute | Im Zielbild |
|---|---|---|
| Kunde | wartet auf Planstände, formuliert Wünsche über Dritte | entwirft selbst, sieht Kosten und Folgen sofort |
| Vertrieb | zeichnet, rechnet nach, trägt Änderungen hin und her | berät und verkauft |
| Architekt | setzt Kundenwünsche in Pläne um | gestaltet Hausmodelle und Regelraum, prüft Abweichungen, zeichnet als bauvorlageberechtigte Person |
| Ingenieur | tippt Geometrie für Statik und Energie ab | definiert Bemessungsregeln, prüft und zeichnet Nachweise |
| Werk | bekommt Pläne, modelliert für die Fertigung neu | bekommt ein freigegebenes Modell, leitet Maschinendaten ab |

Kurz: **Niemand tippt etwas ab, was schon im Modell steht.**

**Leitbild:** eine ernsthafte, an die deutsche Bauwirtschaft angebundene Version des Baumodus von „Die Sims“. Es ist ein Hausplaner ohne Lebenssimulation. Jede Fliese, jede Farbe und jedes Möbel ist ein realer, bestellbarer und normkonformer Artikel.

**Gebäudetypen:** Abgebildet werden alle Wohngebäudetypen:
- Einfamilienhaus, auch mit Einliegerwohnung
- Zweifamilienhaus
- Doppel- und Reihenhaus
- Mehrfamilienhaus
- Geschosswohnungsbau in Holz

Jeder Typ hat ein eigenes Regelprofil. Gebäudeklasse, Brand- und Schallschutz zwischen Wohnungen, Barrierefreiheit, Aufzug, Spielplatz und Stellplätze schalten automatisch mit (Beleg folgt in `recherche/14`).

**Belege für den Handlungsdruck** (Recherche 07):
- Fertigbauquote EFH/ZFH 2025: 26,5 % in Deutschland, 27,5 % in Bayern (3.633 Häuser, +19 % zum Vorjahr).
- Bauplanung: 306 offene Stellen je 100 Arbeitslose (VDI/IW Q3/2025).
- Rund 10.000 Bauplaner fehlen (IW 09/2025).

---

## 2. How (Prinzipien)

1. **Ein Modell ist die Wahrheit.** Pro freigegebenem Projektstand gibt es genau ein IFC. Alles, was für die Baupraxis relevant ist, steht darin oder ist daraus referenziert. Drei Dinge stehen daneben, standardkonform:
   - **Versionen** in einer Projektplattform nach ISO 19650 (IFC erlaubt nur ein Projekt pro Datei und speichert nur die letzte Änderung)
   - **Prüfregeln** als IDS-Dateien und bSDD-Klassen
   - **signierte Dokumente** (Vertrag, Nachweise) über `IfcDocumentReference`
2. **Nur der Standard, keine Eigenbauten.**
   - Schema: IFC4X3_ADD2 (= ISO 16739-1:2024).
   - Ein offizielles MVD für diese Breite gibt es nicht. „Standardkonform“ heißt daher: Jede Version besteht den buildingSMART Validation Service (Syntax, Schema, normative Regeln, bSDD) und alle Firmen-IDS.
   - Keine Proxy-Elemente. Eigene Daten nur in eigenen Psets.
   - Für Software, die nur IFC4 liest (z. B. hsbcad, cadwork), wird ein IFC4-Export abgeleitet.
3. **Programme interpretieren, sie besitzen nichts.** CAD, Statik, Energie, Kalkulation und Werk lesen das Modell. Rückmeldungen fließen über das Parametermodell zurück ins IFC.
4. **Andere Formate sind nur Ableitungen.** Sie werden nie von Hand bearbeitet und sind über GlobalIds zum IFC zurückverfolgbar:
   - BTLx (Abbund)
   - **WUP** (Weinmann-Wandanlagen)
   - GAEB/DIN 18290 (Leistungsverzeichnis)
   - XBau und PDF-Bauvorlagen
5. **Die Regeln der Firma sind Daten, kein Code.**
   - Der Katalog liegt als `IfcProjectLibrary` vor.
   - Merkmalsregeln stehen als IDS daneben.
   - Geometrische Regeln (Raster, Elementlängen, Abstandsflächen) laufen in einer eigenen Regelmaschine; ihre Ergebnisse gehen als BCF zurück.
6. **Nichts erfinden, alles übernehmen.** Gesetze, Normen, Handwerksregeln und Open-Source-Bausteine werden zusammengeführt. Die Lizenzen sind geprüft (Recherchen 03 und 05).
7. **Die KI versteht, der Code entscheidet.**
   - Das Intent-Modell (Laya lokal, Jev als Fallback) erkennt nur die Absicht und liefert Wahrscheinlichkeiten.
   - Werte, Regeln, Statik und Kosten berechnet deterministischer Code.
8. **Assistieren statt bevormunden.** Neben den harten Regeln gibt es Empfehlungen aus Architektur- und Umweltpsychologie, etwa zu Tageslicht, Zonierung, Blickbeziehungen und Möblierbarkeit. Jede Empfehlung kommt mit Begründung und Evidenzgrad. Kulturprofile wie Feng Shui, Vastu oder Baubiologie kann der Kunde wählen. Sie sind transparent als Tradition gekennzeichnet und werden nie als Wissenschaft ausgegeben. So plant niemand aus Versehen Unsinn, und trotzdem entscheidet der Kunde.
9. **Alles wird rechnerisch und grafisch nachgewiesen, mit wissenschaftlicher Präzision.** Jede Prüfung erzeugt einen Nachweis, den ein Prüfingenieur, eine Behörde oder ein Gutachter ohne Zugriff auf den Code nachvollziehen kann. Er enthält:
   - Regel mit Quelle und Fassung
   - Eingaben mit Einheit und Herkunft
   - Formeln und Zwischenwerte
   - Ergebnis, Grenzwert und Ausnutzung
   - Rundungsregel und Unsicherheit
   - Grafik (Lageplan, Schnitt, Diagramm, Lärmkarte)

   Der Nachweis ist verknüpft mit der IFC-GUID und der Version des Regelwerks. Beispiel: Die Aufstellung der Wärmepumpe wird nicht nur mit einem Schallrechner abgeschätzt, sondern nach DIN ISO 9613-2 und TA Lärm je Immissionsort berechnet und als Rasterlärmkarte dargestellt.
10. **Menschen unterschreiben, was das Gesetz verlangt.**
   - Die Firma ist Entwurfsverfasser unter Leitung einer namentlich benannten bauvorlageberechtigten Person (Art. 61 Abs. 6 BayBO). Bei freistehenden oder einseitig angebauten Wohngebäuden der GK 1–3 mit höchstens 3 Wohnungen kann das auch ein Zimmerermeister sein (Abs. 3). Das Reihenmittelhaus fällt nicht darunter. Bei größeren Gebäuden, etwa Mehrfamilienhäusern, braucht es Architekt oder Ingenieur mit Listeneintrag. Für GK 4/5 kommen Prüfingenieure und Prüfsachverständige hinzu. Das System wählt das Freigabe-Gate passend zum Gebäudetyp.
   - Jede Freigabe steht als `IfcApproval` im Modell.

---

## 3. What (der Endzustand)

### 3.1 Ein Durchlauf, wie er am Ende aussehen soll

1. **Idee.** Familie H. öffnet die App und wählt ein Regnauer-Hausmodell und ihr Grundstück.
   - Frei verfügbar (CC BY 4.0): Hausumringe, Gelände (DGM) und Luftbild.
   - Kostenpflichtig: das Flurstück (ALKIS, ca. 2,90 €).
   - Der Bebauungsplan liegt in Bayern meist nur als PDF vor. GRZ, GFZ und Dachneigung werden deshalb im Dialog bestätigt oder aus dem PDF extrahiert.
2. **Entwurf.** Sie sagt: „Das Bad oben einen Meter größer, Richtung Süden.“
   - Das Modell ändert sich.
   - Kosten, Wohnfläche, H'T und Abstandsflächen aktualisieren sich sofort.
   - Unzulässiges lehnt die App mit Grund und Alternative ab.
   - Die App weist darauf hin, dass eine KI beteiligt ist (Art. 50 AI Act).
3. **Angebot und Vertrag.**
   - Aus dem Modell entstehen Angebot und Baubeschreibung. Die Baubeschreibung wird gegen die 9 Pflichtpunkte in Art. 249 § 2 EGBGB geprüft und vor der Unterschrift in Textform übergeben.
   - Der Vertragsstand wird mit einem Hash eingefroren.
   - Die Widerrufsbelehrung läuft im Ablauf mit.
4. **Bemusterung.**
   - Fliesen, Fenster, Treppe und Sanitär liegen als Produkttypen in der Projektbibliothek.
   - Die Wahl wird als Typzuordnung gespeichert.
5. **Freigabe durch Fachleute.**
   - Architekt oder Zimmermeister und Tragwerksplaner sehen nur die Abweichungen vom Regelraum.
   - Ihre Freigabe steht als `IfcApproval` im Modell, ihr Name erscheint automatisch in den Planköpfen.
6. **Bauantrag.**
   - Aus demselben Modell entstehen die Bauvorlagen nach BauVorlV: Lageplan, Pläne 1:100, Baubeschreibung mit Gebäudeklasse und Baukosten.
   - Dazu kommen die Formulardaten für das BayernPortal bzw. XBau. Das IFC geht als Anlage mit.
   - Bei Genehmigungsfreistellung (Art. 58) gehen die Unterlagen an die Gemeinde.
7. **Werkplanung und Fertigung.**
   - Jedes Wandelement steht mit Ständern, Beplankung, Dämmung, Folie und Verbindungsmitteln im Modell.
   - Daraus werden BTLx und WUP erzeugt.
   - Produktion beginnt erst nach Genehmigung bzw. Freistellungsfrist **und** nach der Widerrufsfrist.
8. **Montage und Übergabe.**
   - Montagereihenfolge und Elementnummern stehen im Modell (`IfcTask`, `IfcWorkSchedule`).
   - Der Kunde bekommt bei der Übergabe dasselbe Modell als Hausakte. Die Hausakte ist nach QDF Pflicht.

### 3.2 Was im Modell lebt, Phase für Phase

| Phase | Inhalt im IFC 4.3 | Freigabe durch | Abgeleitete Exporte |
|---|---|---|---|
| Entwurf | Geschosse, Räume, Wände, Dach, Fenster, Möbel | Kunde | Visualisierung |
| Angebot | `IfcCostSchedule`/`IfcCostItem`, Preise mit Gültigkeit (`ApplicableDate`, `FixedUntilDate`), DIN 276 als Klassifikation | Vertrieb | Angebots-PDF, GAEB |
| Vertrag | `IfcProjectOrder`, `IfcApproval`, Baubeschreibung als signierter Dokumentverweis | Kunde + Firma | Vertrag, Baubeschreibung |
| Bemusterung | Produkttypen mit `Pset_ManufacturerTypeInformation` (GTIN, Artikel) | Kunde | Bemusterungsprotokoll |
| Bauantrag | `IfcPermit`, `IfcActor` (Bauherr, Entwurfsverfasser), `IfcMapConversion` EPSG:25832, eigenes Pset für Flurstück | bauvorlageberechtigte Person | PDF 1:100, Lageplan, XBau |
| Nachweise | Schichtaufbauten, `ThermalTransmittance`, `IfcRelSpaceBoundary2ndLevel`, Lasten | Tragwerksplaner, Energieberater | Eingangsdaten Statik und GModG |
| Fertigung | `IfcWall` aggregiert aus `IfcMember` STUD/PLATE, `IfcPlate`, `IfcBuildingElementPart`, `IfcMechanicalFastener`, `IfcVoidingFeature`; Seriennummer/Barcode | Werkplanung | BTLx, WUP |
| Montage | `IfcWorkSchedule`, `IfcTask` (INSTALLATION, MOVE), `IfcVehicle` für LKW | Bauleitung | Montageplan |
| Übergabe | `IfcAsset`, Wartung, Gewährleistung (`Pset_Warranty`) | Firma | Hausakte |

### 3.3 Detailtiefe: alles, was gebaut wird, steht im Modell

**Diese Gewerke sind vollständig abgedeckt:**

| Bereich | Inhalt |
|---|---|
| Bemusterung außen | Fenster, Haustür, Fassade, Dach, Balkon, Terrasse, Außenanlagen |
| Innenausbau und Interior | jede Fliese mit Format, Verlegemuster, Fugenbild und Fugenfarbe; jeder Boden mit Holzart, Sortierung, Oberfläche, Verlegemuster und Sockelleiste; Wandfarben und Putze einschließlich Keller; Treppenform, Holzart und Geländer; Innentüren und Beschläge; Sanitärobjekte; Küche; Möblierung in 3D. Jeweils festgeschrieben und durchsuchbar |
| Elektro, Netzwerk | Leitungen in Installationszonen, Dosen, Zählerschrank, Netzwerk, Smart Home |
| Wasser | Trinkwasser kalt und warm, Zirkulation, Abwasser mit Lüftung über Dach |
| Dimensionen und Durchdringungen | Nennweite jeder Leitung berechnet. Jede Bohrung, jeder Durchbruch, jeder Wechsel und jede Manschette ist geplant, regelgeprüft und als Fertigungsbearbeitung übergeben |
| Fliesen und Parkett in 3D | jede Fliese als echtes 3D-Objekt. Verschnitt, Reststücke und Mehraufwand werden real berechnet, auch bei Chevron oder Fischgrät in einem achteckigen Duschraum mit mehrfachem Gefälle |
| Grundstücksentwässerung | Grundleitungen, Kontroll- und Revisionsschächte, Rückstausicherung, Versickerung über Rigolen mit Bemessung nach DWA-A 138-1, Entwässerungsantrag nach kommunaler Satzung (z. B. MSE München) |
| Schallschutz | innen zwischen Wohnungen und außen gegen Autobahn, Bahn, Flughafen und Gewerbe. Lärmkarten liefern den Pegel am Grundstück. Das System wählt Fenster und Lüfter; wo das nicht reicht, schlägt es eine andere Planung vor (Schlafräume zur ruhigen Seite) |
| Baustellenlogistik | Elementgewichte, Kranwahl nach Ausleger und Traglast, Kranstellplatz, Abstellflächen für Wechselbrücken, Transportgenehmigungen, Montagereihenfolge |
| Fußbodenaufbau | Estrich- und Dämmhöhen werden je Raum so berechnet, dass die Fertigfußbodenhöhe bei jedem Belag gleich bleibt (Parkett, Fliese, Naturstein, Beton Ciré). Keine Kante an Übergängen |
| Lüftung, Heizung | Lüftungskonzept und Kanalnetz, Heizlast, Fußbodenheizung. Die Wärmepumpe (Monoblock oder Split mit Außeneinheit) wird mit Schallnachweis je Nachbarfenster aufgestellt, dazu R290-Schutzbereich, Kältemittelleitung und Kondensat |
| Licht, PV | Lichtplanung mit Leuchtendaten, Photovoltaik mit Belegung und Ertrag |
| Dach | Dachform, Tragwerk, Ziegelform und -farbe, First, Grat, Kehle, Ortgang, Traufe, Mansarde, Gauben |
| Dacheinbauteile | Dachfenster, Lüfterziegel, Solar- und Antennendurchgänge, Schneefang, Entwässerung |
| Fassade | Varianten, Materialien, Farben |

**Jedes Bauteil durchläuft drei Reifegrade**, die jeweils per IDS geprüft werden:

| Reifegrad | Bedeutung | Beispiel Dachfenster |
|---|---|---|
| **P – präsentationsfertig** | fotorealistisch in 3D und AR, mit Material und Farbe | Modell, Rahmenfarbe, Lage im Dach sichtbar |
| **R – prüffertig** | alle Merkmale für Regeln, Nachweise und Kosten | Uw-Wert, Rettungsweg-Maße, Preis, Abstand zur Traufe geprüft |
| **A – ausführungsfertig** | bestellbarer Artikel, Einbauinformation, Fertigungsteile | Artikelnummer, Eindeckrahmen passend zum Ziegel, Wechsel im Sparren als Abbundteil |

Belege folgen in `recherche/08` (TGA), `recherche/09` (Dach, Fassade, PV) und `recherche/10` (Bemusterung, Produktdaten, 3D).

---

## 4. Erfolgskriterien (messbar)

1. Ein Kunde erreicht ohne Mitarbeiter einen zulässigen, kalkulierten Entwurf.
2. Zwischen Vertrag und Werk wird **null Mal** neu modelliert oder abgetippt.
3. Jede freigegebene Version besteht den Validation Service und alle Firmen-IDS.
4. Bauvorlagen nach BauVorlV entstehen vollständig aus dem Modell.
5. BTLx und WUP entstehen vollständig aus dem Modell.
6. Durchlaufzeit Vertrag → Produktionsfreigabe und Anzahl der Planstände sinken messbar. Öffentliche Zahlen dazu gibt es nicht; den Ausgangswert liefert Regnauer aus CRM und CAD-Historie.

---

## 5. Harte Grenzen

1. **Unterschriften bleiben menschlich.** Ohne namentlich benannte bauvorlageberechtigte Person gibt es keinen Bauantrag. Den Tragwerksnachweis erstellen gelistete Personen.
2. **Bayern nimmt heute PDF, nicht IFC.** Das IFC geht nur als Anlage mit. Ein Gesetz für „digital only“ ist im Entwurf (07/2026).
3. **Maschinen lesen kein IFC.** BTLx und WUP bleiben Exporte. Die WUP-Spezifikation muss bei Homag angefragt werden.
4. **Normtexte sind geschützt.** Kennwerte werden mit Normverweis implementiert, Texte und Tabellen nicht kopiert (§ 5 Abs. 3 UrhG).
5. **Regnauers interne Daten** sind nicht öffentlich: Aufbauten, Nachweise, Preise, Werkssoftware (9 Fragen in Recherche 04).
6. **Produkthaftung:** Ab 09.12.2026 ist Software ein Produkt. Das System braucht deshalb Audit-Trail und Versionierung der Regelwerke.

---

## 6. Strategische Option

**Typengenehmigung nach Art. 73a BayBO** für das Bauteilsystem der Firma „mit festgelegter zulässiger Veränderbarkeit“. Der Regelraum der App wäre dann genau dieser genehmigte Spielraum, und der Bautechnik-Nachweis gilt als erbracht.

---

## 7. Offene Entscheidungen

1. Zielkunde der ersten Version: nur Regnauer oder mehrere Hersteller?
2. Erste Ausbaustufe: bis Vertrag, bis Bauantrag oder bis Werk?
3. Firmenregeln: Die Recherche empfiehlt Katalog als `IfcProjectLibrary`, Merkmalsregeln als IDS daneben und geometrische Regeln in einer eigenen Regelmaschine. Bestätigen?

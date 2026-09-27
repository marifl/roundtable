# 11 Reifegrade: präsentationsfertig, prüffertig, ausführungsfertig

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle, am Schema IFC4X3_ADD2 oder mit ifctester 0.8.5 geprüft) oder [U] (unsicher, Konvention oder eigene Bewertung). Alle Prüfergebnisse dieses Kapitels sind mit `spezifikation/pruefe_kap11_12.py` am 27.09.2026 erzeugt und reproduzierbar.

## 11.0 Einordnung und Vorgehen

Das Zielbild verlangt, dass jedes Bauteil drei Reifegrade durchläuft: präsentationsfertig (P), prüffertig (R) und ausführungsfertig (A). Alle drei sollen aus demselben Modell entstehen und per IDS geprüft werden. Die Forschungsfrage FF6 fragt, wie das für Bemusterung, TGA, Dach und Fassade gelingt. Dieses Kapitel liefert dafür den begrifflichen und prüftechnischen Rahmen. Kapitel 12 füllt ihn für die Bemusterung, Kapitel 13 und 14 später für TGA und Dach.

Die Reifegrade beantworten drei praktische Fragen:

1. **Was darf der Kunde sehen?** Eine fotorealistische Ansicht darf nicht den Eindruck erwecken, sie sei geprüft.
2. **Was darf die Regelmaschine entscheiden?** Eine Regel kann nur über Merkmale urteilen, die im Modell stehen (Kapitel 9.2.1).
3. **Was darf ins Werk?** Beim Praxispartner beginnt die Montage frühestens zwölf Wochen nach der unterschriebenen Ausstattungsfestlegung [@regnauerBLB2024] [V]. Bis dahin müssen Artikel, Einbaumaße und Anschlusslagen feststehen, denn Dosenbohrungen, Sanitäranschlüsse und die WC-Tragkonstruktion entstehen schon in der Wandfertigung (Kapitel 3.4.2).

**Vorgehen.** Abschnitt 11.1 verankert die Reifegrade in der Norm zur Informationsbedarfstiefe, DIN EN ISO 7817-1:2024-11 [@dineniso7817-1], und grenzt sie von den LOD-Konzepten ab. Die Abschnitte 11.2 bis 11.4 definieren P, R und A nach den Aspekten dieser Norm. Abschnitt 11.5 überträgt die Definition auf Bauteilgruppen und Phasen, erzeugt daraus IDS-Dateien und prüft sie an den Prototypen B1, B14 und B16 sowie an synthetischen Modellen. Maschinenlesbar liegen die Ergebnisse in `spezifikation/reifegrade.yaml`, in zwölf IDS-Dateien unter `spezifikation/ids/` und im Regelkatalog `spezifikation/regelkatalog-11.yaml`.

**Form der Entscheidungen.** Designentscheidungen sind als E11.1 bis E11.9 nummeriert. Sie bauen auf E8.12 (Granularität folgt dem Reifegrad), E8.14 (Bemusterung als Projektbibliothek), E8.21 (Präfix `HRB_`) und E8.22 (Herstellerdaten am Typ) auf.

## 11.1 Informationsbedarf nach Level of Information Need

### 11.1.1 Von LOD zu LOIN

Für den Fortschritt eines Modells gibt es mehrere konkurrierende Begriffe: Level of Detail, Level of Development, Level of Definition und Level of Information Need. Abualdenien und Borrmann haben 58 LOD-Richtlinien und 299 begutachtete Publikationen ausgewertet. Die Begriffe sehen ähnlich aus, weichen aber in ihren Grundlagen erheblich voneinander ab [@abualdenien2022levels]. Für die Arbeit folgen daraus drei Festlegungen:

- **Keine LOD-Stufen.** Die LOD-Spezifikation des BIMForum dient nur zum Vergleich. „Fertigstellungsgrad“ ist ein Praxisbegriff ohne Norm und wird nicht verwendet (Recherche 10) [U].
- **Keine rein geometrische Staffel.** Geometrische LOD-Stufen wie die 16 verfeinerten Stufen für CityGML-Gebäudemodelle beschreiben die Außenhülle, nicht die Bauteilebene [@biljecki2016lod]. Sie taugen für die Umgebung im 3D-Viewer, nicht für die Reifegrade.
- **Keine Stufen ohne Zweck.** Hooper zeigt an zwei Fallprojekten, dass LOD in der Praxis uneinheitlich verstanden wird. Nützlich wird es erst, wenn der geplante Modellfortschritt automatisch mit dem Ist-Stand verglichen wird [@hooper2015lod]. Genau diesen Vergleich leistet die IDS-Prüfung je Gate (Abschnitt 11.5).

### 11.1.2 Rahmenbedingungen und Informationsarten der Norm

DIN EN ISO 7817-1:2024-11 ersetzt DIN EN 17412-1:2021-06 [V, Recherche 10]. Die Norm legt Konzepte und Grundsätze fest, mit denen sich Informationsbedarf und Informationslieferungen einheitlich spezifizieren lassen, und gilt für den ganzen Lebenszyklus [@dineniso7817-1]. Recherche 10 hat die Struktur der Norm ausgewertet [V]:

| Ebene | Bestandteile nach DIN EN ISO 7817-1 | Umsetzung in dieser Arbeit |
|---|---|---|
| Rahmenbedingungen | Zweck, Meilenstein, Akteure, Objekt | Reifegrad (Zweck, Akteure), Gate (Meilenstein), Bauteilgruppe (Objekt) |
| geometrische Information | Detaillierung, Dimensionalität, Lage, **Erscheinung (appearance)**, parametrisches Verhalten | Block `geometrie` je Gruppe und Reifegrad |
| alphanumerische Information | Identifikation, Informationsgehalt | Block `information` und `pflichtmerkmale` |
| Dokumentation | Dokumentarten | Block `dokumentation` |

Dass die Norm die Erscheinung ausdrücklich als geometrischen Aspekt führt, ist für diese Arbeit zentral. Der Reifegrad P ist dadurch kein „Vorstadium“ ohne Normbezug, sondern ein vollwertiges LOIN-Profil mit einem eigenen Zweck: der Kaufentscheidung. Teil 3 der Normreihe mit einem maschinenlesbaren Schema ist nach Stand der Recherche in Arbeit [U].

### 11.1.3 LOIN und IDS

LOIN beschreibt den Bedarf, IDS prüft seine Erfüllung. Tomczak und Kollegen haben acht Methoden zur Spezifikation von Informationsanforderungen verglichen: Data Dictionaries, IDM, Property Templates, IDS, LOIN, mvdXML, Product Data Templates und SHACL. Keine deckt alle Aspekte ab; die Wahl muss sich nach dem Zweck richten [@tomczak2022review]. Akbas und Kollegen untersuchen die Integration von IDS und dem LOIN-XML-Schema. LOIN deckt mehr Aspekte ab, IDS vor allem alphanumerische Anforderungen. Eine Integration ist möglich, lässt aber Lücken [@akbas2025holistic]. Liu und Kollegen nutzen das LOIN-Schema als Grundlage einer Ontologie für die Qualität von Datencontainern [@liu2023definition].

Für die Architektur folgt daraus eine klare Arbeitsteilung:

| LOIN-Aspekt | geprüft durch | Grund |
|---|---|---|
| Identifikation, Informationsgehalt | IDS 1.0 [@bsi2024ids] | Merkmale, Klassifikationen, Materialien, Teil-von-Beziehungen |
| Detaillierung, Dimensionalität | Regelmaschine, Granularitätsverbote per IDS | IDS kennt keine Geometriefacette |
| Lage | Regelmaschine (Kapitel 9.2.3) | Abstände und Toleranzen sind Geometrie |
| Erscheinung | Darstellungsprüfung des glTF-Exports | IDS prüft keine Oberflächenstile |
| parametrisches Verhalten | Parametermodell (Kapitel 7) | liegt vor dem IFC |
| Dokumentation | Dokumentverweise mit Hash (E8.24) | IDS prüft nur das Vorhandensein |

Die geometrische Prüfung ist das offene Feld. Ein lernbasierter Ansatz klassifiziert den geometrischen Detaillierungsgrad von Bauteilen automatisch und hält die semantische Prüfung für gelöst, die geometrische nicht [@abualdenien2022ensemble]. Diese Arbeit prüft die Granularität deterministisch über das Vorhandensein von Teilobjekten (11.5.2), nicht über die Form.

**E11.1 – Die Reifegrade P, R und A sind LOIN-Profile nach DIN EN ISO 7817-1, keine LOD-Stufen.** *Entscheidung.* Jeder Reifegrad ist durch Zweck, Meilenstein und Akteure definiert. Je Bauteilgruppe legt er die geometrischen, alphanumerischen und dokumentarischen Anforderungen fest. Die alphanumerischen Anforderungen werden als IDS geprüft, die übrigen durch Regelmaschine und Exportprüfung. *Begründung.* Die LOD-Begriffe sind uneinheitlich [@abualdenien2022levels]; LOIN ist die geltende Norm und führt die Erscheinung ausdrücklich [@dineniso7817-1]. Die Kombination LOIN plus IDS ist möglich, deckt aber nicht alles ab [@akbas2025holistic; @tomczak2022review]. *Beleg.* Recherche 10 [V]; `spezifikation/reifegrade.yaml`, Block `reifegrade`.

## 11.2 Reifegrad P: präsentationsfertig

**Zweck** ist die Entscheidung des Kunden: fotorealistische 3D-Ansicht, AR auf dem Grundstück und Preisindikation. **Meilensteine** sind Entwurf, Vorbemusterung und Angebot. **Akteure** sind Generator und Vertrieb als Lieferer, Kunde und Vertrieb als Nutzer.

| LOIN-Aspekt | Anforderung in P |
|---|---|
| Detaillierung | Sichtgeometrie: Wandkörper als Schichtenmodell, Sanitärobjekt als Hersteller-Mesh oder generisch, Belag als Fläche mit Dicke |
| Lage | im Raum, Toleranz etwa ± 10 mm |
| Erscheinung | PBR-Material mit realer Texturgröße; Varianten als `KHR_materials_variants` |
| parametrisches Verhalten | Variantenschalter (Farbe, Format, Muster) |
| Identifikation | Katalog-Option (`HRB_Auswahl.OptionID`) |
| Informationsgehalt | Muster, Fläche, Preisindikation |
| Dokumentation | Hinweis „Visualisierung unverbindlich“ |

**Erscheinung in IFC 4.3 [V].** Das Schema trägt physikalisch basierte Materialien. `IfcSurfaceStyleRendering` mit `ReflectanceMethod = PHYSICAL` bildet baseColor, metallic und roughness ab. `IfcSurfaceTexture.Mode` benennt seit 4.3.0 den Map-Typ (DIFFUSE, NORMAL, METALLICROUGHNESS, OCCLUSION, EMISSIVE). UV-Koordinaten stehen in `IfcIndexedTriangleTextureMap`. Der Stil hängt am `IfcMaterial`, damit ein Materialtausch alle Bauteile umfärbt (Recherche 10).

**Befund zur Pipeline [V].** IfcOpenShell 0.8.5 schreibt beim Export nach glTF Farbe, metallic und roughness, aber keine Bilder und keine UV-Koordinaten (Recherche 10, eigener Test). Der Reifegrad P lässt sich deshalb im IFC vollständig beschreiben, aber nicht ohne eigenen Exporter darstellen. ANF-08-30 verlangt diesen Schritt. Die IDS kann ihn nicht prüfen; E11.2 verlagert die Prüfung in den Export.

**Verbindlichkeit.** Der Praxispartner erklärt Visualisierungen und Modelle vertraglich für unverbindlich (AGB § 2) [@regnauerBLB2024] [V]. Farbtreue auf Bildschirmen ist nicht zusicherbar. Für die Darstellung heißt das zweierlei:

- **Unsicherheit sichtbar machen.** Visualisierungen unsicherer Bauteilinformationen sind bisher nur mit Fachleuten bewertet [@abualdenien2020vagueness]. Die App kennzeichnet jedes Objekt unter Reifegrad R als „ungeprüft“ (ANF-11-13).
- **Herkunft der Textur offenlegen.** Das Merkmal `HRB_Auswahl.Darstellung` unterscheidet `herstellertextur`, `aehnlich` (CC0-Material) und `generisch`. Herstellertexturen brauchen eine schriftliche Lizenz. Eine verbreitete Texturplattform verbietet die Nutzung in Web-Anwendungen ausdrücklich (Recherche 10) [V].

In einer Studie mit 76 Teilnehmenden erzielte AR gegenüber Bildschirm und VR die höchste Akzeptanz bei der Entwurfsprüfung [@lee2020augmented]. Das stützt den Aufwand für P, ersetzt aber keine Prüfung.

**E11.2 – Die Erscheinung wird im Export geprüft, nicht in der IDS.** *Entscheidung.* Die P-IDS verlangt Material und Katalog-Option. Dass jedes P-Objekt einen `IfcSurfaceStyle` mit `PHYSICAL` trägt und dass die GLB Bilder, Texturen und `TEXCOORD_0` enthält, prüft der glTF-Exporter selbst. *Begründung.* IDS 1.0 hat keine Facette für Darstellungen [@bsi2024ids; @akbas2025holistic]. *Beleg.* Recherche 10 [V]; ANF-08-30, ANF-11-12.

## 11.3 Reifegrad R: prüffertig

**Zweck** ist die Regel-, Nachweis-, Kompatibilitäts- und Kostenprüfung. **Meilensteine** sind Vertrag, Bauvorlage und der Entwurf der Ausstattungsfestlegung. **Akteure** sind Regelmaschine, bauvorlageberechtigte Person, Tragwerksplanung, TGA und Kalkulation.

R ist der Reifegrad, an dem Kapitel 9 hängt. Eine R1-Regel liefert nach der fünfwertigen Logik aus Abschnitt 9.2.1 `unbestimmt`, wenn ihr eine R2-Voraussetzung fehlt. Die R-IDS einer Bauteilgruppe ist genau die Liste dieser Voraussetzungen. Im Regelkatalog steht sie im Feld `vorbedingung.r2_voraussetzung`, etwa `IDS.RG-treppe-R` für die neue Regel `DE.DIN18065.Kopfhoehe` (Kapitel 12).

| LOIN-Aspekt | Anforderung in R |
|---|---|
| Detaillierung | Einbau- und Störraum, Bewegungsfläche, Anschlussports; Einzelteile, soweit Kennwerte sie brauchen |
| Lage | Wand und Raum maßlich, ± 1 bis 5 mm je Gruppe |
| Erscheinung | wie P, dazu Farbcode |
| parametrisches Verhalten | parametrischer Typ (Raster, Steigungszahl, Verlegeparameter) |
| Identifikation | Hersteller, Serie, Klassifikation (DIN 276, STLB-Bau) |
| Informationsgehalt | alle Prüfmerkmale: U-Wert, Format, Fuge, W-Klasse, R_λ,B, Nennweite, Steigung, Auftritt |
| Dokumentation | Datenblatt, Nachweis (Kapitel 7a), Prüfprotokoll als BCF |

**Einzelteile schon in R.** Die Mapping-Tabelle aus Kapitel 8 führt Ständer, Beplankung und Dämmung in R als optional. Das ist eine bewusste Abweichung von einer strengen Staffel. Nach E8.11 wird der U-Wert aus der Einzelteilgeometrie berechnet, weil das Schichtenmodell den Holzanteil um mehr als die Hälfte unterschätzt. Ein prüffertiges Wandelement braucht deshalb die Teile, die den Nachweis tragen. Verbindungsmittel und Stabbearbeitungen braucht es nicht; sie sind in R verboten (ANF-08-25).

> **Beispiel 11.1 (Treppe im Reifegrad R).** B5 zählt für eine Geschosshöhe von 2,90 m und eine Laufbreite von 0,90 m 68 zulässige Lösungen. Die beste hat 17 Steigungen à 170,59 mm und 16 Auftritte à 290 mm, das Schrittmaß beträgt 631,18 mm, die Lauflänge 4,64 m (`beispiele/ausgabe/treppe.json`).
>
> Diese Werte stehen im Reifegrad R in `Pset_StairFlightCommon` (NumberOfRiser, RiserHeight, TreadLength, WalkingLineOffset, Headroom). Die Verziehungsmethode steht in `HRB_Verziehung`. Ein synthetisches Modell mit genau diesen Werten erfüllt `treppe-R.ids` mit 6 von 6 Spezifikationen.
>
> Die Regel `DE.DIN18065.WG2WE` ist damit `erfuellt`. Die Regel `DE.DIN18065.Kopfhoehe` bleibt `unbestimmt`, solange die Deckenöffnung nicht festliegt (`spezifikation/beispiele/bemusterung-auswahl-treppe.json`). Das Gate „Ausstattungsfestlegung“ bleibt deshalb gesperrt, obwohl alle Maße der Treppe stimmen.

Die IDS stellt sicher, dass die Regel rechnen *kann*; ob das Ergebnis zulässig ist, entscheidet die Regel.

## 11.4 Reifegrad A: ausführungsfertig

**Zweck** sind Bestellung, Werkplanung, Fertigung, Montage und Ausbau. **Meilenstein** ist die unterschriebene Ausstattungsfestlegung, spätestens vor der Werkplanung. **Akteure** sind Werkplanung, Einkauf, Werk, Lieferanten und Ausbaugewerke.

A hat vier Bestandteile:

1. **Bestellbarer Artikel.** Handelsware trägt GTIN und Artikelnummer in `Pset_ManufacturerTypeInformation` am Typ (E8.22). Einzelanfertigungen wie eine Treppe haben keine GTIN; an ihre Stelle treten Hersteller und Auftragsnummer. Die GTIN wird auf 8, 12, 13 oder 14 Ziffern mit gültiger Prüfziffer geprüft (ANF-08-17).
2. **Einbauinformation.** Dazu gehören Montagehöhe, Anschlussports mit Nennweite, Befestigungspunkte, Verlegeplan und Rasterursprung.
3. **Fertigungsteile.** Ständer, Beplankung, Verbindungsmittel, Bearbeitungen und Belagstücke entstehen erst hier (E8.12).
4. **Festschreibung.** Die Auswahl wird durch einen Inhaltshash eingefroren (Kapitel 12.4). Der Hash steht in `HRB_Auswahl.Inhaltshash` und in der Festschreibung. Eine Änderung danach ist nur noch als Nachtrag möglich.

Maschinendaten sind ausdrücklich *nicht* Teil des Reifegrads. BTLx und WUP sind Ableitungen aus einem Modell im Reifegrad A (E8.26).

> **Beispiel 11.2 (Belag im Reifegrad A).** B16 bildet einen achteckigen Duschraum von 4,77 m² mit Punktablauf auf zwei Arten ab (Kapitel 8.3.5):
>
> | Fall | aggregiert: Bytes / Entitäten / Coverings | einzeln: Bytes / Entitäten / Coverings |
> |---|---|---|
> | gerade 60 × 60 | 30 647 / 440 / 1 | 70 346 / 1 011 / 33 |
> | Chevron 60 × 10 | 175 961 / 2 144 / 1 | 429 779 / 5 670 / 193 |
>
> Im Reifegrad A ist die Stückliste Teil der Festschreibung: Beim Chevron sind das 192 Stücke, von denen 94 aus Reststücken stammen (Recherche 17). In P und R wäre dieselbe Information reine Dateigröße.
>
> Die A-IDS verlangt am Belag GTIN, Artikelnummer, Status „festgeschrieben“, Inhaltshash, Verschnitt, Rasterursprung, Rohlinge und Pakete. An jedem Stück verlangt sie Stückart, Herkunft und Rohling. Die B16-Ausgabe trägt als GTIN den Platzhalter „BEISPIEL-GTIN-F6060“. Er verletzt das Muster `[0-9]{8}|[0-9]{12,14}` – der Platzhalter kann also nie versehentlich ins Werk gehen.

**Lieferdaten sind Ist-Daten.** Charge, Kaliber, Seriennummer und Garantie kennt man erst bei der Lieferung. Sie gehören zur Hausakte, nicht zur Planung. Würden sie zur Pflicht des Reifegrads A, könnte die Werkplanung nie beginnen, bevor der Fliesenhändler geliefert hat.

**E11.3 – Lieferdaten gehören nicht zum Reifegrad A.** *Entscheidung.* Die A-IDS enthält Lieferdaten (`Pset_ManufacturerOccurrence.BatchReference`, `SerialNumber`, `Pset_Warranty`, `HRB_Verlegung.Kaliber`) nur mit `cardinality="optional"`: Fehlt das Merkmal, ist das kein Fehler. Ist es vorhanden, werden Datentyp und Wert geprüft. Erst am Gate G7 „Übergabe“ werden sie Pflicht (Regel `M.Reifegrad.Lieferdaten`). Der Inhaltshash der Festschreibung schließt die Lieferdaten aus. *Begründung.* LOIN definiert Anforderungen je Meilenstein [@dineniso7817-1]; die Lieferung ist ein eigener Meilenstein. *Beleg.* `reifegrade.yaml`, Block `lieferdaten`; Spezifikationen `BEL-A-L01` und `SAN-A-L01`.

## 11.5 Reifegrade je Bauteilgruppe und Phase, geprüft über IDS

### 11.5.1 Die Spezifikationsdatei

`spezifikation/reifegrade.yaml` ist die einzige Quelle der Reifegrade. Sie hat fünf Teile:

1. `reifegrade`: P, R, A mit Zweck, Meilenstein, Akteuren und Prüfweg (E11.1),
2. `gates`: acht Meilensteine G0 bis G7,
3. `phasen_matrix`: der Mindestreifegrad je Bauteilgruppe und Gate,
4. `hrb_psets`: die eigenen Property-Sets mit Merkmal, Messtyp und Wertebereich,
5. `bauteilgruppen`: 16 Gruppen mit je P, R und A. Jede Stufe hat die Blöcke `geometrie`, `information`, `dokumentation`, `pflichtmerkmale`, `verbote`, gegebenenfalls `lieferdaten`, und `ids`.

Die Gruppen verweisen über `mapping_zeilen` auf `ifc-mapping.csv`. Alle 67 Verweise existieren, und die Spalten P, R und A der Mapping-Tabelle widersprechen nicht [V]. Damit sind diese Spalten, die Kapitel 8 als Vorschlag markiert hatte, verbindlich.

### 11.5.2 Formalisierung

Die Reifegrade bilden eine Ordnung − < P < R < A. Für eine Bauteilgruppe *k* sei *S*(*k*, *L*) die Menge der Pflichtspezifikationen des Reifegrads *L* und *V*(*k*, *L*) die Menge seiner Verbote.

**Monotonie der Merkmale.** Es gilt *S*(*k*, P) ⊆ *S*(*k*, R) ⊆ *S*(*k*, A). Die Datei erzwingt das durch `erbt: P` bzw. `erbt: R`. Wer ausführungsfertig ist, erfüllt also alle Merkmale von prüffertig.

**Keine Monotonie der Granularität.** Die Verbote werden nicht vererbt. Ein Modell im Reifegrad A enthält Verbindungsmittel und verletzt damit das Verbot `WAND-R-V01`. Der Reifegrad eines Modells wird deshalb nur über die Pflichtspezifikationen bestimmt:

$$\mathrm{rg}(k) = \max\{\, L \in \{\mathrm{P},\mathrm{R},\mathrm{A}\} \mid \text{alle } s \in S(k,L) \text{ bestanden} \,\}$$

Die Verbote prüft die App nur beim *Export* eines Modells, das als Stufe *L* ausgeliefert wird. Eine Präsentationsdatei für den Kunden darf keine Stückliste enthalten, eine Prüfdatei für die Statik keine Schrauben.

**Gate-Bedingung.** Ein Gate *g* öffnet genau dann, wenn für alle Gruppen rg(*k*) ≥ soll(*k*, *g*) gilt, mit soll aus `phasen_matrix` (Regel `M.Reifegrad.Gate`). Der Modellreifegrad ist damit ein Vektor, keine Zahl. Ein „Haus in Reifegrad R“ gibt es nicht; es gibt ein Haus, dessen Wände in A, dessen Böden in R und dessen Möbel in P sind.

**Tabelle 11.1: Mindestreifegrad je Bauteilgruppe und Gate** (Auszug aus `phasen_matrix`)

| Gruppe | G0 Entwurf | G1 Angebot | G2 Vertrag | G3 Bauvorlage | G4 Ausstattung | G5 Produktion | G6 Ausbau | G7 Übergabe |
|---|---|---|---|---|---|---|---|---|
| wandelement, decke, dach | P | P | R | R | R | A | A | A |
| fenster_aussentuer, fassade, treppe, sanitaer, elektro, heizung_lueftung | P | P | R | R | **A** | A | A | A |
| belag, innentuer | P | P | P | R | R | R | A | A |
| wandoberflaeche, kueche_moebel | P | P | P | P | R | R | A | A |
| tga_leitungen | − | − | − | R | R | A | A | A |

Die Spalte G4 zeigt den technischen Mindeststand nach Recherche 10: Kategorien mit Freeze „W“ müssen vor der Werkplanung ausführungsfertig sein, Kategorien mit Freeze „A“ erst vor dem Ausbau. Der Praxispartner verlangt vertraglich mehr. Der Baubeginn setzt voraus, dass die Ausstattungsfestlegung „endgültig abgeschlossen“ ist [@regnauerBLB2024] [V]. Das Herstellerprofil `M-Regnauer` hebt deshalb alle Bemusterungsgruppen an G4 auf A.

**E11.4 – Das Gate prüft einen Reifegradvektor gegen eine Sollmatrix; technischer und vertraglicher Freeze sind getrennt.** *Entscheidung.* Der Reifegrad wird je Bauteilgruppe als höchste Stufe mit bestandenen Pflichtspezifikationen bestimmt. Ein Gate öffnet, wenn der Vektor die Sollzeile erreicht. Die technische Matrix ist Teil des Profils `HRB-IDS-Reifegrad`; Herstellerprofile dürfen sie nur verschärfen (Monotonie nach Kapitel 9.3.3). *Begründung.* Die Bauteilgruppen haben verschiedene Freeze-Termine (Recherche 10). Ein skalarer Modellreifegrad würde entweder die Werkplanung blockieren oder unfertige Sanitärobjekte durchlassen. *Beleg.* `reifegrade.yaml`, Blöcke `phasen_matrix` und `herstellerprofile`; Regeln `M.Reifegrad.Gate` und `M.Regnauer.Ausstattung-vor-Montage`.

### 11.5.3 Erzeugung der IDS

Die IDS-Dateien werden nicht von Hand gepflegt. `pruefe_kap11_12.py erzeugen` schreibt sie mit ifctester 0.8.5 aus der Facetten-Notation der YAML-Datei. Dabei prüft das Skript jede Klasse und jeden PredefinedType gegen IFC4X3_ADD2, jedes `Pset_`- und `Qto_`-Merkmal gegen das Template und jedes `HRB_`-Merkmal gegen `hrb_psets`. Jede Datei wird gegen das lokale `ids.xsd` validiert und erneut eingelesen. Ergebnis für zwölf Dateien: 0 Schema- oder Template-Fehler. Die Dateien sind gültig nach XSD und werden von ifctester geparst [V]. Zwei Läufe ergaben dieselbe SHA-256-Prüfsumme über alle Dateien.

**Tabelle 11.2: Erzeugte IDS-Dateien**

| Gruppe | P | R | A | Beispiel für eine Pflichtspezifikation in A |
|---|---|---|---|---|
| wandelement | 4 (1 + 3 Verbote) | 5 (3 + 2 Verbote) | 8 | `WAND-A-01`: `Qto_WallBaseQuantities.GrossWeight` > 0 und `HRB_Montage.Montagenummer` |
| belag | 2 (1 + 1) | 7 (6 + 1) | 10 (9 + Lieferdaten) | `BEL-A-01`: GTIN nach Muster, Inhaltshash `sha256:[0-9a-f]{64}` |
| sanitaer | 2 (1 + 1) | 5 | 7 (6 + Lieferdaten) | `SAN-R-04`: Port PIPE mit NominalDiameter, Teil des Sanitärobjekts über `IfcRelNests` |
| treppe | 3 (2 + 1) | 6 | 8 | `TRE-A-02`: `IfcMember` STRINGER mit Material als Teil der Treppe |

**Einheiten.** IDS 1.0 verlangt Zahlenwerte in SI-Einheiten. Eine Probe mit einem Projekt in Millimetern zeigte: `RiserHeight` = 170,59 mm besteht die Einschränkung [0,14; 0,20], verfehlt aber [140; 200] [V, ifctester 0.8.5]. ifctester rechnet also die Projekteinheit um. Alle Grenzen in `reifegrade.yaml` stehen deshalb in m, m² und kg, die Kommentare nennen die Millimeter.

**E11.5 – IDS-Dateien sind Ableitungen der Reifegrad-Spezifikation und tragen nur Präsenz- und Plausibilitätsgrenzen.** *Entscheidung.* Normative Grenzwerte, die vom Profil abhängen, bleiben in der Regelmaschine. Beispiele sind die Steigung 140–200 mm nach DIN 18065 für höchstens zwei Wohnungen oder der U-Wert einer Außenwand. Die IDS prüft Vorhandensein, Datentyp, Vokabular und weite Plausibilitätsgrenzen (Steigung 0,05–0,30 m). Eine Ausnahme sind Projektanforderungen wie HRB-01, die ausdrücklich als solche gekennzeichnet sind. *Begründung.* Eine IDS gehört zu einem Profil (Kapitel 9.2.2). Profilabhängige Grenzen in der IDS würden bei einem Wechsel des Gebäudetyps (Kapitel 9a) stumm falsche Ergebnisse liefern. IDS prüft Vorhandensein und Struktur, nicht die Richtigkeit der Werte [@fonsati2026leveraging]. *Beleg.* `reifegrade.yaml`, Spezifikation `TRE-R-01` mit Verweis auf `DE.DIN18065.WG2WE`.

### 11.5.4 Prüfung an Prototypen und Testmodellen

Die IDS-Dateien wurden gegen alle IFC-Ausgaben der Prototypen geprüft, die eine der vier Gruppen enthalten. Hinzu kamen zwei Migrationen und je drei synthetische Modelle für Sanitär und Treppe (`pruefe_kap11_12.py modelle`).

**Tabelle 11.3: Ergebnisse der IDS-Prüfung (bestanden / Spezifikationen; verfehlte Spezifikationen)**

| Modell | P | R | A |
|---|---|---|---|
| B1 `wandelement.ifc` | 1/4: V01–V03 | 3/5: R-V01, R-V02 | 7/8: A-01 |
| B1 `wandelement_fehlerhaft.ifc` | 1/4: V01–V03 | 2/5: R-01, V01, V02 | 4/8: R-01, A-01, A-02, A-04 |
| B16 gerade 60 × 60 aggregiert, unverändert | 1/2: P-01 | 4/7 | 6/10 |
| B16 Chevron einzeln, unverändert | 0/2: P-01, P-V01 | 3/7 | 5/10 |
| B14 Variante A, unverändert | 1/2: P-01 | 4/7 | 6/10 |
| B16 gerade 60 × 60, migriert ohne Messtypen | 1/2: P-01 | 3/7 | 3/10 |
| B16 gerade 60 × 60, migriert mit Messtypen | **2/2** | **7/7** | **10/10** |
| B16 Chevron einzeln, migriert mit Messtypen | 1/2: P-V01 | 5/7: R-01, R-V01 | 8/10: R-01, A-01 |
| dito, zusätzlich Typ am Belag | 1/2: P-V01 | 6/7: R-V01 | **10/10** |
| synthetisch Sanitär, Modell P / R / A | 2/2 · 1/2 · 1/2 | 2/5 · **5/5** · 5/5 | 3/7 · 6/7 · **7/7** |
| synthetisch Treppe, Modell P / R / A | 3/3 · 3/3 · 2/3 | 4/6 · **6/6** · 6/6 | 4/8 · 6/8 · **8/8** |

Die Spalten der synthetischen Modelle bestätigen die Formalisierung aus 11.5.2 [V]:

- **Jedes Modell erreicht genau seinen Reifegrad.** Das Sanitärmodell R besteht R mit 5/5 und verfehlt in A nur `SAN-A-01` (GTIN, Montagehöhe, Festschreibung). Sein Reifegrad ist also R.
- **Höhere Modelle erfüllen alle Merkmale der niedrigeren Stufen.** Sie verfehlen dort nur die Verbote. Das Sanitärmodell A verfehlt in P nur `SAN-P-V01` (Ports), das Treppenmodell A nur `TRE-P-V01` (Wangen als Einzelteile).

### 11.5.5 Befunde

**Befund 1: B1 ist fast ausführungsfertig [V].** Das Wandelement verfehlt in A nur `WAND-A-01`: Es fehlen `GrossWeight` und `HRB_Montage.Montagenummer`. Das bestätigt den offenen Punkt aus E8.11: B1 berechnet die Masse, schreibt sie aber nicht. B18 schreibt beide Merkmale bereits (Montagenummer 1, Gewicht 1 228 kg für ein Wandelement). Die Nachrüstung ist also nur eine Frage der Zusammenführung. In P und R verfehlt B1 nur die Verbote. Das ist korrekt, denn B1 ist ein Modell in Granularität A.

**Befund 2: Die Prototypen schreiben falsche Messtypen [V].** Nach Umbenennung der Präfixe (E8.21) und Ergänzung der fehlenden Psets ohne explizite Messtypen bestand der B16-Fall nur 3 von 10 A-Spezifikationen. ifctester meldete Datentypfehler: B16 schreibt GTIN, ArticleNumber und BatchReference als `IfcLabel` statt `IfcIdentifier`. Das Template von `Pset_ManufacturerTypeInformation` schreibt `IfcIdentifier` vor. Zahlen in eigenen Psets stehen als `IfcReal` statt als Messtyp. Die Ursache ist banal: `ifcopenshell.api` leitet den Typ aus dem Python-Wert ab, wenn kein Template existiert. Mit expliziten Messtypen bestand derselbe Fall 10 von 10. Die IDS erzwingt damit, was E8.21 nur fordert: „Zahlenwerte verwenden die passenden Messtypen“.

**Befund 3: In der Einzelvariante von B16 trägt nur das Stück den Artikel [V].** Der Belag der Variante „einzeln“ hat keinen Typ, nur die 192 Stücke sind dem `IfcCoveringType` zugeordnet. Damit fehlen am Belag Hersteller und GTIN (`BEL-R-01`, `BEL-A-01`). Nach Zuordnung des Typs auch zum Belag bestand A mit 10/10. Das ist eine Konvention, die B16 bei der Überarbeitung übernehmen muss (ANF-11-10).

**Befund 4: Die Teil-von-Facette für räumliche Einbettung ist transitiv [V].** Eine Anwendbarkeit „IFCCOVERING FLOORING, Teil von IFCSPACE über IFCRELCONTAINEDINSPATIALSTRUCTURE“ traf im Chevron-Fall 193 Objekte: den Belag und alle 192 Stücke, die nur über die Aggregation mit dem Raum verbunden sind. ifctester wertet die Einbettung also über die Aggregation hinweg aus. Die Belag-Spezifikationen wählen den Belag deshalb über das Merkmal `HRB_Auswahl.Kategorie` aus, die Stücke über „Teil von IFCCOVERING“. Ob ein anderes Prüfwerkzeug dieselbe Auslegung wählt, ist offen [U]. Das bestätigt den Befund aus Kapitel 9.2.2, dass deklarative Anforderungen von der Implementierung des Werkzeugs abhängen [@cerovsek2025advancing].

**Befund 5: B14 und B16 überlappen [U].** Beide schreiben je Raum ein `IfcCovering` FLOORING, B14 für den Aufbau, B16 für den Belag; die Mapping-Tabelle führt zwei Zeilen. In einem Hausmodell würde dieselbe Fläche doppelt gezählt.

**E11.6 – Ein Belag ist ein Covering je Raum und Fläche; es trägt Aufbau, Verlegung und Auswahl, seine Stücke sind Teile.** *Entscheidung.* Je Raum und Fläche gibt es ein `IfcCovering` FLOORING bzw. CLADDING. Es trägt das Layer-Set (Estrich, Dämmung, Verlegewerkstoff, Belag) sowie `HRB_Fussbodenaufbau`, `HRB_Verlegung`, `HRB_Belag` und `HRB_Auswahl`. Der Typ trägt den Artikel und ist dem Belag zugeordnet. In A werden die Stücke der obersten Schicht über `IfcRelAggregates` Teile dieses Coverings; sie tragen `HRB_Fliesenstueck` und denselben Typ. *Begründung.* Eine Fläche darf nur einmal in Mengen, Kosten und Nachweisen erscheinen. Die Auswahl über `HRB_Auswahl.Kategorie` umgeht Befund 4. *Beleg.* Befunde 3 bis 5; `reifegrade.yaml`, Gruppe `belag`, Feld `konvention`.

**E11.7 – `HRB_Auswahl` verbindet jedes gewählte Exemplar mit seiner Festschreibung.** *Entscheidung.* Jedes Exemplar, das aus der Bemusterung stammt, trägt `HRB_Auswahl` mit OptionID, Kategorie, Reifegrad, Status, Darstellung, ab A auch AuswahlID und Inhaltshash. *Begründung.* Die Wahl ist im IFC nur eine Typzuordnung (E8.14). Kontext und Leistung der Festschreibung – Muster, Fuge, Achse, Mengen – brauchen einen stabilen Schlüssel zum Objekt. *Beleg.* `hrb_psets.HRB_Auswahl`; Kapitel 12.4.

**E11.8 – Messtypen sind Teil des Vertrags zwischen Generator und Prüfung.** *Entscheidung.* Der Generator schreibt jedes Merkmal mit dem Messtyp, den das Template (Standard-Psets) oder `hrb_psets` (eigene Psets) vorgibt. Die IDS prüft den Messtyp mit. *Begründung.* Befund 2. *Beleg.* ANF-11-08.

## 11.6 Grenzen

1. **Geometrie und Erscheinung sind nicht per IDS prüfbar.** Sie hängen an Regelmaschine und Exporter (11.1.3) und müssen durch Tests abgesichert sein.
2. **Die Sanitär- und Treppenmodelle sind synthetisch.** Sie belegen die Semantik der IDS, nicht einen realen Generator. B5 rechnet Treppen, schreibt aber kein IFC.
3. **Zwölf von 48 möglichen IDS-Dateien existieren.** Für die übrigen zwölf Gruppen stehen die Pflichtmerkmale in `reifegrade.yaml` als Liste (`pflichtmerkmale_liste`), noch nicht in Facetten-Notation.
4. **Kein LOIN-XML.** Solange das maschinenlesbare Schema der Normreihe fehlt, ist `reifegrade.yaml` ein eigenes Format [U]. Die Struktur folgt der Norm, damit eine spätere Übersetzung möglich bleibt [@akbas2025holistic].
5. **Die Sollmatrix ist ein Vorschlag.** Die Freeze-Kategorien stammen aus der Bau- und Leistungsbeschreibung und aus Herstellerquellen [V/U]. Die tatsächlichen Termine je Kategorie muss der Praxispartner liefern (DAT-08, DAT-11-01).
6. **Der Validation Service ist nicht geprüft** (wie in Kapitel 8).

## 11.7 Zwischenfazit

Das Kapitel beantwortet den Teil von FF6, der fragt, wie drei Reifegrade aus einem Modell entstehen, mit vier Aussagen.

1. **Die Reifegrade sind normgerecht definierbar.** P, R und A sind drei LOIN-Profile nach DIN EN ISO 7817-1 mit eigenem Zweck, Meilenstein und Akteur. Weil die Norm die Erscheinung ausdrücklich führt, hat auch der Präsentationsgrad eine normative Grundlage.
2. **Merkmale wachsen monoton, Granularität nicht.** Ausführungsfertig schließt prüffertig ein. Eine Datei für den Kunden darf aber keine Stückliste enthalten. Diese Trennung macht die Reifegrade prüfbar, ohne die Dateien aufzublähen.
3. **Das Gate prüft einen Vektor.** Der Reifegrad ist eine Eigenschaft der Bauteilgruppe, nicht des Hauses. Die Freeze-Kategorien des Praxispartners machen die Bemusterung zum Fertigungs-Gate. Das Herstellerprofil verschärft die technische Matrix, ohne sie zu ersetzen.
4. **Die Prüfung findet echte Fehler.** Schon die ersten zwölf IDS-Dateien decken in den Prototypen falsche Messtypen, einen fehlenden Typ am Belag und fehlende Montagedaten auf. Nach deren Korrektur besteht der B16-Belag den Reifegrad A vollständig.

Kapitel 12 füllt den Rahmen für die Bemusterung: mit Katalogartikeln, festgeschriebenen Auswahlen und dem Abhängigkeitsgraphen, der aus einer Wahl die Folgen für Tragwerk, TGA und Aufbau ableitet.

## 11.8 Umsetzungsvorgaben für die App

Es gelten die Regeln aus Kapitel 8.8: „Muss“ ist freigabeblockierend, „Soll“ ist umzusetzen, eine Abweichung ist zu begründen. Die Abnahmekriterien sind Testfälle mit Referenzwerten aus `pruefe_kap11_12.py`.

### 11.8.1 Anforderungen

| ID | Muss/Soll | Beschreibung | Beleg im Kapitel | Abnahmekriterium |
|---|---|---|---|---|
| ANF-11-01 | Muss | Die Reifegrade werden aus `spezifikation/reifegrade.yaml` geladen. Die Datei ist Konfiguration, kein Code. Beim Laden werden alle Klassen, PredefinedTypes und Merkmale gegen IFC4X3_ADD2, das Template und `hrb_psets` geprüft. | 11.5.1, 11.5.3 | `pruefe_kap11_12.py erzeugen` meldet 0 Schema- oder Template-Fehler. Ein eingefügtes Merkmal `Pset_WallCommon.Foo` erzeugt den Fehler „Pset_WallCommon.Foo fehlt im Template“. |
| ANF-11-02 | Muss | Je Gruppe und Reifegrad wird die IDS aus der YAML-Datei erzeugt, nie von Hand gepflegt. Die Erzeugung ist deterministisch. | E11.5 | 12 Dateien, alle XSD-gültig und von ifctester geparst; zwei Läufe ergeben dieselbe SHA-256 über `ids/*.ids`. |
| ANF-11-03 | Muss | Die Pflichtspezifikationen sind monoton: *S*(P) ⊆ *S*(R) ⊆ *S*(A) für jede Gruppe. | 11.5.2 | Prüfung „Monotonie“ in `pruefe_kap11_12.py pruefen`: wandelement 1 ⊆ 3 ⊆ 8, belag 1 ⊆ 6 ⊆ 9, sanitaer 1 ⊆ 5 ⊆ 6, treppe 2 ⊆ 6 ⊆ 8. |
| ANF-11-04 | Muss | Granularitätsverbote gelten nur für den Export der jeweiligen Stufe. P: keine Teile in Wänden, keine Ports an Sanitärobjekten, keine Treppenwangen, keine Belagstücke. P und R: keine Verbindungsmittel, keine Stabbearbeitungen. | 11.5.2, E8.12 | B1 gegen `wandelement-R.ids`: verfehlt genau `WAND-R-V01` und `WAND-R-V02`; gegen `wandelement-P.ids` genau `WAND-P-V01` bis `-V03`. |
| ANF-11-05 | Muss | Der Reifegrad einer Gruppe ist die höchste Stufe, deren Pflichtspezifikationen alle bestanden sind. Verbote gehen nicht ein. | 11.5.2 | Synthetisches Sanitärmodell R: R 5/5, A 6/7 ⇒ Reifegrad R. Synthetisches Sanitärmodell A: P verfehlt nur `SAN-P-V01` ⇒ Reifegrad A. |
| ANF-11-06 | Muss | Ein Gate öffnet nur, wenn der Reifegradvektor die Zeile der `phasen_matrix` erreicht. Die Meldung nennt Gruppe, Ist und Soll. | E11.4 | Treppe im Reifegrad R an G4: „Gate G4 gesperrt: treppe hat Reifegrad R, verlangt ist A“. Belag im Reifegrad R an G4 ohne Herstellerprofil: Gate offen. |
| ANF-11-07 | Muss | Das Herstellerprofil `M-Regnauer` verlangt an G4 für alle Bemusterungsgruppen A. Die Montage liegt mindestens 84 Tage nach G4. | 11.5.2 | G4 am 20.07.2026 ⇒ Montage frühestens 12.10.2026; Montage am 05.10.2026 ⇒ `verletzt` (77 Tage). Belag im Reifegrad R an G4 mit Profil ⇒ Gate gesperrt. |
| ANF-11-08 | Muss | Der Generator schreibt jedes Merkmal mit dem Messtyp aus Template bzw. `hrb_psets`. Zahlenwerte in IDS-Facetten stehen in SI-Einheiten. | E11.8, 11.5.3 | B16 unverändert migriert: `BEL-A-01` verfehlt mit „IfcLabel does not match IFCIDENTIFIER“; mit Messtypen: 10/10. Probe: `RiserHeight` 170,59 mm besteht [0,14; 0,20]. |
| ANF-11-09 | Muss | Jedes gewählte Exemplar trägt `HRB_Auswahl`; ab A mit AuswahlID (UUID) und Inhaltshash, die mit der Festschreibung übereinstimmen. | E11.7 | Für jede Auswahl im Status „festgeschrieben“ existiert genau ein Exemplar mit gleicher AuswahlID und gleichem Inhaltshash; B16 60 × 60 migriert besteht `belag-A.ids` mit 10/10. |
| ANF-11-10 | Muss | Belag nach E11.6: ein Covering je Raum und Fläche mit Aufbau, Verlegung und Auswahl; der Typ ist dem Belag *und* den Stücken zugeordnet. | E11.6, Befunde 3–5 | B16 Chevron einzeln ohne Typ am Belag: `BEL-R-01` und `BEL-A-01` verfehlt; mit Typ: A 10/10. Gesamtfläche aller FLOORING-Coverings eines Raums = NetFloorArea ± 1 %. |
| ANF-11-11 | Muss | Lieferdaten sind in der A-IDS optional mit Wertprüfung und an G7 Pflicht. Der Inhaltshash schließt sie aus. | E11.3 | Nachtrag von `BatchReference` ändert den Inhaltshash nicht; G7-Variante ohne `BatchReference` am Belag: `M.Reifegrad.Lieferdaten` verletzt. |
| ANF-11-12 | Soll | Der glTF-Export prüft die Erscheinung: jedes P-Objekt mit `IfcSurfaceStyle` PHYSICAL; GLB mit `images`, `textures`, `TEXCOORD_0`; Varianten als `KHR_materials_variants`. | E11.2 | Export eines Belags mit zwei Farbvarianten: GLB enthält 2 Varianten, 1 Mesh, Bilder und UV; Objekt ohne Stil ⇒ Exportfehler mit GlobalId. |
| ANF-11-13 | Muss | Objekte unter Reifegrad R werden im Viewer als „ungeprüft“ gekennzeichnet. Jede Ansicht trägt den Hinweis zur Unverbindlichkeit (vgl. ANF-03-24). | 11.2 | Treppe im Reifegrad P: Kennzeichnung sichtbar; nach Erreichen von R: Kennzeichnung entfällt. |
| ANF-11-14 | Muss | Fehlt eine R-Pflicht, liefern die abhängigen R1-Regeln `unbestimmt` und nennen die fehlende IDS-Spezifikation. | 11.3 | Treppe ohne `Headroom`: `DE.DIN18065.Kopfhoehe` = `unbestimmt`, Meldung nennt `TRE-R-01`. |
| ANF-11-15 | Muss | IDS-Befunde werden über das ID-Präfix im Spezifikationsnamen einer Regel-ID aus `regelkatalog-11.yaml` zugeordnet (vgl. ANF-09-04). | 11.5.3 | Jeder Befund aus Tabelle 11.3 trägt eine Regel-ID `IDS.RG-<gruppe>-<Stufe>` und die Spezifikations-ID, z. B. `WAND-A-01`. |
| ANF-11-16 | Soll | Die App zeigt je Gruppe und Gate Soll und Ist des Reifegrads als Fortschrittsbericht. | 11.1.1 | Bericht für B1: wandelement Ist R (A verfehlt `WAND-A-01`), Soll an G5 A ⇒ rot mit Verweis auf `GrossWeight` und `Montagenummer`. |
| ANF-11-17 | Muss | Die Prototypen werden migriert: Präfix `HRB_`, Messtypen nach E11.8, Typ am Belag, `HRB_Auswahl` am Belag. | Befunde 2–5 | Nach Migration: B16 beide Varianten `belag-A` 10/10; B14 `belag-R` 7/7. |
| ANF-11-18 | Muss | B1 schreibt `Qto_WallBaseQuantities.GrossWeight` und `HRB_Montage.Montagenummer`. | Befund 1 | B1 gegen `wandelement-A.ids`: 8/8; `GrossWeight` = Σ MassDensity · NetVolume der Teile ± 0,1 % (vgl. ANF-08-12). |
| ANF-11-19 | Soll | Jede IDS trägt in `info` Zweck und Meilenstein aus `reifegrade.yaml`. Sobald ein LOIN-XML-Schema vorliegt, wird die Datei zusätzlich dorthin exportiert. | 11.1.2, 11.6 | Alle 12 IDS haben nicht leere `purpose` und `milestone`, gleich den YAML-Werten. |

### 11.8.2 Datenstrukturen und Parameter

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `reifegrad` | enum | – | P, R, A (Ordnung − < P < R < A) | E11.1 |
| `gate.id` | enum | – | G0 … G7 | `reifegrade.yaml#gates` |
| `phasen_matrix[gruppe][gate]` | enum | – | −, P, R, A; je Zeile monoton | E11.4 |
| `herstellerprofil.ausstattung_vollstaendig_an` | enum | – | Gate-ID (M-Regnauer: G4) | [@regnauerBLB2024] |
| `herstellerprofil.montage_nach_G4_min_tage` | int | d | ≥ 0 (M-Regnauer: 84) | [@regnauerBLB2024] |
| `spezifikation.id` | string | – | `^[A-Z]{3,4}-[PRA]-(V|L)?[0-9]{2}$` | 11.5.3 |
| `spezifikation.min_vorkommen` | int | – | 0 oder 1 | IDS 1.0 |
| `reifegradvektor[gruppe]` | enum | – | −, P, R, A | ANF-11-05 |
| `HRB_Auswahl.AuswahlID` | IfcIdentifier | – | UUID | E11.7 |
| `HRB_Auswahl.OptionID` | IfcIdentifier | – | `K-[A-Z]{3}-[0-9]{4}` | E11.7, Kap. 12 |
| `HRB_Auswahl.Status` | IfcLabel | – | entwurf, geprueft, festgeschrieben, nachtrag | E11.7 |
| `HRB_Auswahl.Inhaltshash` | IfcIdentifier | – | `sha256:` + 64 Hex | E11.7, Kap. 12.4 |
| `HRB_Auswahl.Darstellung` | IfcLabel | – | herstellertextur, aehnlich, generisch | E11.2 |
| `HRB_Verlegung.Rasterursprung_u/_v` | IfcNormalisedRatioMeasure | – | 0–1 | B16 |
| `HRB_Verlegung.Fugenbreite` | IfcPositiveLengthMeasure | m (SI) | 0,001–0,02 | Kap. 12.2.1 |
| `HRB_Fussbodenaufbau.R_lambda_B` | IfcThermalResistanceMeasure | m²K/W | 0–0,5 | B14 |
| `HRB_Montage.Montagenummer` | IfcInteger | – | ≥ 1 | B18 |
| `Qto_WallBaseQuantities.GrossWeight` | IfcMassMeasure | kg | > 0 | ANF-08-12 |
| `lieferdaten` | Liste | – | Merkmale mit `cardinality="optional"` bis G7 | E11.3 |

### 11.8.3 Datenlieferungen von Regnauer

| ID | Inhalt | gewünschtes Format | Ersatz bis zur Lieferung | blockiert |
|---|---|---|---|---|
| DAT-11-01 | spätester Festlegungstermin je Bauteilgruppe relativ zu Werkplanung, Produktion und Ausbau; Kosten einer Änderung danach (Präzisierung von DAT-08) | Tabelle Gruppe × Gate | `phasen_matrix` nach Recherche 10; an G4 alles A (AGB § 5/6) | ANF-11-06, ANF-11-07 |
| DAT-11-02 | Informationsanforderungen des Werks je Bauteilgruppe: welche Merkmale die Werkplanung und das CAD/CAM-System wirklich lesen | Merkmalsliste oder vorhandene AIA/Prüfliste | A-Pflichtmerkmale aus `reifegrade.yaml` | ANF-11-02, ANF-11-18 |
| DAT-11-03 | Datenlieferung der Zulieferer für Einzelanfertigungen (Treppe, Fenster KlimaPlus): Werkzeichnung, Auftragsnummer, 3D-Daten | Muster je Zulieferer | Auftragsnummer als `ArticleNumber`, generische Geometrie | ANF-11-05 (Treppe A) |
| DAT-11-04 | ein abgeschlossenes Projekt mit Ausstattungsplan und Freigabeterminen zur Kalibrierung der Sollmatrix | PDF-Ausstattungsplan, Terminliste | synthetische Modelle aus 11.5.4 | Evaluation Kap. 20 |
| DAT-11-05 | Formale Anforderungen an den Ausstattungsplan nach § 650n BGB, die das Werk heute verwendet | Muster-Ausstattungsplan | Sicht auf die Festschreibungen (Kap. 12.4) | ANF-11-09 |

### 11.8.4 Maschinenlesbare Dateien

| Datei | Inhalt | Prüfung am 27.09.2026 |
|---|---|---|
| `spezifikation/reifegrade.yaml` | LOIN-Profile P/R/A, 8 Gates, Phasenmatrix für 16 Gruppen, 8 eigene Psets, Pflichtmerkmale und Verbote | YAML parsebar; 67 Mapping-Verweise vorhanden; Phasenmatrix je Zeile monoton |
| `spezifikation/ids/{wandelement,belag,sanitaer,treppe}-{P,R,A}.ids` | 12 IDS-1.0-Dateien mit zusammen 67 Spezifikationen | XSD `ids.xsd` (ifctester 0.8.5) gültig; `ids.open` parst alle; deterministisch |
| `spezifikation/regelkatalog-11.yaml` | 12 IDS-Regeln `IDS.RG-*`, `M.Reifegrad.Gate`, `M.Regnauer.Ausstattung-vor-Montage`, `M.Reifegrad.Lieferdaten` | gültig nach `regel.schema.json`; keine ID-Kollision mit `regelkatalog.yaml` |
| `spezifikation/pruefe_kap11_12.py` | Erzeugung (`erzeugen`), Dateiprüfung (`pruefen`), Modelltests (`modelle`) | läuft mit ifcopenshell/ifctester 0.8.5, jsonschema 4.26, xmlschema 4.3 |

Das neue Profil `HRB-IDS-Reifegrad` (S5) ist in `regelprofile.yaml` (Kapitel 9a) zu registrieren; die Datei wurde hier nicht geändert.

## Verwendete Schlüssel

Das Kapitel zitiert 14 Schlüssel aus `literatur/lit-*.bib`; zugeordnet ist die erste Datei, in der ein Schlüssel steht. Für die bekannte Dublette ist der führende Schlüssel `bsi2024ids` verwendet (siehe `literatur/KORREKTUREN.md`).

**lit-A-acc-bim.bib** (2): `bsi2024ids`, `tomczak2022review`

**lit-C-recht-normen.bib** (1): `regnauerBLB2024`

**lit-E-vergleich-automation.bib** (1): `abualdenien2022levels`

**lit-I-schneeball-a.bib** (3): `cerovsek2025advancing`, `fonsati2026leveraging`, `liu2023definition`

**lit-I-schneeball-b.bib** (6): `abualdenien2020vagueness`, `abualdenien2022ensemble`, `biljecki2016lod`, `dineniso7817-1`, `hooper2015lod`, `lee2020augmented`

**lit-J-schneeball-runde2.bib** (1): `akbas2025holistic`

### Python-Key-Check

```python
import re, glob, pathlib
text = pathlib.Path("11-reifegrade.md").read_text(encoding="utf-8")
body = text.split("## Verwendete Schlüssel")[0]
cited = {k.strip().lstrip("@") for grp in re.findall(r"\[(@[^\]]+)\]", body) for k in grp.split(";")}
bib = set()
for f in glob.glob("literatur/lit-*.bib"):
    bib |= set(re.findall(r"^@\w+\{([^,\s]+),", open(f, encoding="utf-8").read(), re.M))
print(len(cited), "zitiert;", len(cited - bib), "fehlend", sorted(cited - bib))
```

Ergebnis (27.09.2026, aus `arbeit/` ausgeführt): `14 zitiert; 0 fehlend []`. Die Schlüssel in den Feldern `bib` von `regelkatalog-11.yaml` und `reifegrade.yaml` (`bsi2024ids`, `dineniso7817-1`, `regnauerBLB2024`) sind mit demselben Abgleich geprüft; es fehlt keiner.

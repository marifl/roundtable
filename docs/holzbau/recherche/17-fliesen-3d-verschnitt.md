# Recherche 17: Fliesen und Parkett als 3D-Einzelobjekte – Verschnitt auf Gefälle und komplexe Verlegemuster

Stand: 27.09.2026. **[V]** = an Primärquelle, Herstellerunterlage, Verlagsseite oder maschinell geprüft (IfcOpenShell 0.8.5, Schema IFC4X3_ADD2; DOIs über die Crossref-API), **[U]** = unsicher, Sekundärquelle oder eigene Bewertung. Baut auf **Recherche 13** auf (Normen Fliese/Parkett, Pset `HP_Verlegung`, Festschreibungsschema, STLB-Bau-LB). Was dort steht, wird hier nicht wiederholt. Normtexte sind geschützt: Kennwerte stehen hier nur mit Normverweis.

Prototyp: `arbeit/beispiele/b16_fliesen_verlegung.py`, Tests `arbeit/beispiele/tests/test_b16.py`, Eingabe `arbeit/beispiele/daten/b16_fliesen_verlegung.json`. **Alle Prototyp-Zahlen sind Beispielwerte.**

## Ergebnis in 5 Punkten

1. **Für das Duschgefälle gibt es keine Normzahl.** DIN 18534 verlangt nur „ausreichendes Gefälle“ und nennt keinen Wert. Die üblichen 1–2 % stammen von Herstellern (TECE: mind. 1 %, empfohlen 1–2 %) und aus der Praxis (Estrich „im Regelfall 2 %“). DIN 18040-2 begrenzt die Absenkung auf 2 cm. Die Grenze „Gefälle < 2 %“ geht laut nullbarriere auf VDI 6008 Blatt 2 zurück. Mehrere Ratgeberseiten schreiben „DIN 18534 schreibt 1,5–2 % vor“. **Das ist falsch** [V/U, siehe Warnungen].
2. **Verschnitt ist nicht normiert, sondern ein Kalkulationsrisiko.** ATV DIN 18352 rechnet nach hergestellter Fläche ab. Aussparungen bis 0,1 m² werden übermessen: Punktablauf und Rinne zählen also als Belagfläche. Schrägschnitte und Gehrungen sind eigene Längenpositionen (Abschnitt 0.5.2). Zuschläge von 5–20 % je Muster sind Ratgeberwerte. Hersteller von Fischgrätparkett nennen etwa 10 %. Die tarifvertraglich anerkannten ARH-Tabellen führen Zulagen für „diagonal einschließlich Zuschnitt“ (0,05–0,10 h/m²). Einen Gefälle- oder Fischgrätzuschlag zeigt die öffentliche Leseprobe nicht [V/U].
3. **Die Geometrie entscheidet mehr als das Muster.** Im achteckigen Duschraum (Ø 2,4 m, Punktablauf, 8 Kehllinien) bleibt im Prototyp **keine einzige 60×60-Fliese ganz**. Es entstehen 32 Gratschnitte, und die Schnittlänge beträgt 27,8 m auf 4,8 m². Mit zwei Rinnen sinkt sie auf 10,9 m. Chevron aus Rechteck-Stäbchen verliert konstruktionsbedingt **mindestens 1/6 (16,7 %)** durch die zwei Gehrungen je Stab. Nach der Reststückverwertung bleiben 23 % Verschnitt, mit Formteilen 9 %. Fischgrät liegt bei 11,0 % (Punkt) bzw. 6,2 % (Rinnen), die gerade Verlegung 60×10 bei 5,5 % bzw. 5,0 % [Beispielwerte].
4. **Die Reststückverwertung ist der größte Hebel, und sie ist fachlich begrenzbar.** Rechnet man je Rasterposition einen Rohling, liegt der Verschnitt bei 19–39 %. Das Greedy-Nesting senkt ihn auf 5–24 %. Dabei darf ein Stück nur um 0°/180° gedreht werden, nicht gespiegelt, und Fabrikkanten müssen Fabrikkanten bleiben. Die Optimierung des Rasterursprungs spart zwischen bester und schlechtester Lage 106–287 € im Zielwert (Material + Schnittzeit + Kleinstück-Malus, Beispielpreise). Für 60×60 mit Punktablauf ist das Fugenkreuz auf dem Ablauf zugleich die beste Lage. Das deckt sich mit der Handwerksregel [Beispielwerte].
5. **IFC 4.3 trägt Einzelstücke.** Zwei Varianten bestanden `ifcopenshell.validate` mit EXPRESS-Regeln ohne Befund:
   - je Stück ein `IfcCovering`, als Teil des Belag-`IfcCovering` über `IfcRelAggregates`;
   - ein `IfcCovering` mit je einem `IfcMappedItem` pro Stück (ganze Fliesen als gekippte Instanz der Typ-Vorlage).

   Für den Chevron-Fall ergab das 430 kB gegenüber 176 kB. `Qto_CoveringBaseQuantities` kennt nur Width, GrossArea und NetArea. Stückart, Schnittlänge, Rohling-Herkunft und Reststückverwertung brauchen deshalb ein eigenes Pset (`HP_Fliesenstueck`, Vorschlag). Die Charge steht in `Pset_ManufacturerOccurrence.BatchReference`. Die Aggregation von Coverings ist in der IfcCovering-Doku **kein** eigenes Konzept. Das sollte der Validation Service prüfen [V/U].

---

## 1. Fachregeln Gefälle, Fugen, Schnitt

| Regel | Kernwert / Aussage | Quelle | Status |
|---|---|---|---|
| Gefälle in DIN 18534 | Wasserführende Ebenen sind mit ausreichendem Gefälle zum Entwässerungspunkt auszuführen. **Die Norm nennt keine konkreten Gefällevorgaben.** Deshalb bieten Hersteller Duschboards mit vorgeformtem Gefälle von ca. 2 % an | Schlüter (DIN-18534-Seite); Göke (Dallmer) in IHKS-Fachjournal und Bundesbaublatt 06/2018 | [V] Hersteller-Fachartikel |
| Ausnahmen vom Gefälle | kein Gefälle, wenn es die Rutschgefahr unverhältnismäßig erhöht oder das Wasser anders abgeführt wird | bauindex-online (Zusammenfassung DIN 18534) | [U] |
| Praxiswert Duschfläche | mindestens 1 %, üblich 1–2 % | TECE TI Entwässerungstechnik (Duschprofil) | [V] Hersteller |
| Estrichgefälle | „im Regelfall 2 %“ zum Ablauf; Anschlussleitung ≥ 1 %, ≤ 4 m, ≤ 3 Umlenkungen, sonst Belüftung (DIN EN 12056) | Jenke/Göke, IKZ-Fachartikel | [V] Fachartikel |
| Österreich | im wasserableitenden Bereich mind. 1 % im Oberbelag, dafür mind. 2 % im verlegereifen Untergrund. Gefällespachtelung auf der Abdichtung unzulässig | FCT/ÖFV Merkblatt 3 (Verbundabdichtung, Schnittstellen Installateur) | [V] (AT, nur Vergleich) |
| Barrierefreiheit | Duschplatz niveaugleich, Absenkung ≤ 2 cm, Übergang geneigt; rutschhemmend (Bewertungsgruppe B) | DIN 18040-2 5.5.5 bzw. DIN 18040-1 5.3.5, zitiert im BBSR-Leitfaden und von OBB Bayern | [V] Sekundärzitat |
| Gefälle „≤ 2 %“ | Die Grenze < 2 % stammt laut Checkliste aus **VDI 6008 Blatt 2:2012-12**, nicht aus DIN 18040. nullbarriere empfiehlt 0,5–1,5 % Mindestgefälle je nach Material, 2 % nicht wesentlich überschreiten, bei Raumteiler-Rinne ≥ 0,5 % | nullbarriere.de | [U] |
| Punktablauf vs. Rinne | Die Linienentwässerung vermeidet das durch „Diagonalfugen und Gefälleschnitte“ gestörte Belagbild des Punktablaufs | Jenke/Göke, IKZ | [V] Fachartikel |
| Format auf Gefälle | Beim Punktablauf Mosaik bzw. ≤ 15×15 cm empfohlen; Großformat ≥ 60×60 „nur bei Linienentwässerung praktikabel“, sonst Lippenbildung und Kippeln über mehrere Gefälleebenen | mehrere Ratgeber (hausindustrie, holztools, fliesen-kugel) | [U] |
| Großformat-Merkblatt | ZDB „Groß- und Megaformate“ 2026-02 | Recherche 13 | [U], nicht eingesehen |
| Knicklinien als Fuge | Grat- und Kehllinien werden als Fuge ausgebildet; die Fliese wird entlang der Linie geschnitten („Briefumschlag“ beim Punktablauf). Eine starre Fliese kann nicht über zwei Ebenen liegen | eigene Ableitung + Fachartikel oben | [U] |
| Anschluss an Rinne | bei Sekundärentwässerung Anschlussfuge Fliese–Einbauteil zementär; Rinnen ohne Sekundärentwässerung: kapillarbrechende Verlegung = Sonderkonstruktion (Mehraufwand) | FCT MB 3 | [V] (AT) |
| Rinne kürzen | Duschprofil kürzbar bis ≥ 500 mm; für Bodenbeläge 8–25 mm inkl. Kleberbett einstellbar; Profil ist tiefster Punkt, bündig oder leicht tiefer als die Fliese | TECE TI | [V] Hersteller |
| Mindestschnittmaß | **keine Normregel.** Fachbuch Büchner „Fliesenarbeiten“ (Zitat im Forum): „Teilstreifen in Sichtflächen nicht kleiner als eine halbe Fliese … ökonomischer Materialaufwand ist zu beachten“. Ratgeber sagen ebenfalls ½ Fliese, Recherche 13 nennt ⅓ | bauexpertenforum (Zitat Büchner); mein-eigenheim (Zeichnung Ceresit/Henkel) | [U] |
| Fliesenspiegel | von der Mitte einteilen, symmetrische Randstücke, Armaturen, WC und Ablauf auf Fuge oder Fliesenmitte | wie oben; Recherche 13 | [U] |
| Bewegungsfugen | Feldbegrenzungsfugen bis ca. 8 m, Seitenverhältnis bis ca. 1:2 (Außenbeläge); **Diagonalverlegung und Formate ≥ 0,20 m² bzw. > 60 cm außen vermeiden** | ZDB-Fliesenhandbuch 9. Aufl. 2019 (Leseprobe) | [V] Leseprobe |
| Bedenkenhinweis | Der Auftragnehmer muss Bedenken anmelden bei fehlendem oder ungenügendem Gefälle der Unterlage und bei Abweichung vom geplanten Gefälle | ATV DIN 18352 3.1.1 (WEKA) | [V] Sekundär |
| Fischgrät/Chevron-Parkett | je Paket gleich viele L- und R-Stäbe; ein Starterdreieck bzw. „Zopf“ an der Raummitte. Die Reststücke des Startzopfs werden am Reihenende wiederverwendet | Hafro (Chevron- und Fischgrät-Anleitung 11/2025); Scheucher MULTIflor Französisch Fischgrät („Verschnittteile vom Beginn am Ende der Bahn verwenden“) | [V] Hersteller |
| Französisch Fischgrät Formate | 45°: 740×140 mm (Deckbreite 523 mm); 60°: 500×140 mm; A- und B-Stäbe getrennt | Scheucher | [V] Hersteller |

**Parkett und Gefälle.** Parkett gehört nicht in die Dusche; das Referenzbeispiel ist Keramik. Für Parkett in Wohnräumen gelten dieselben Algorithmen **ohne** Gefälle, aber mit anderen Wiederverwendungsregeln (siehe Warnung 6).

## 2. Verschnitt, Kalkulation und Abrechnung

### Abrechnung nach VOB/C ATV DIN 18352 (2019-09)

| Punkt | Inhalt | Folge für den Planer | Quelle / Status |
|---|---|---|---|
| 5.1 | Abrechnung nach den Maßen der hergestellten bzw. bekleideten Fläche (Abschnitt 5 wurde 2019 überarbeitet) | Verschnitt ist **nicht** Abrechnungsmenge; er steckt im Einheitspreis | baunormenlexikon; dinmedia-Änderungsvermerk [V] |
| 5.3 Übermessen | Aussparungen **bis 0,1 m²** Einzelgröße werden übermessen, darüber abgezogen (kleinste Maße) | Punktablauf 150×150 (0,0225 m²) und Rinne 70×994 (0,070 m²) werden übermessen: Der AN bekommt die Fläche bezahlt, obwohl er dort schneiden muss | bauprofessor (f:data) [V Sekundär] |
| 4.1 Nebenleistung | Anarbeiten an Aussparungen ≤ 0,1 m² | Ablaufschnitt kleiner Aussparungen ist im Flächenpreis enthalten | bau-doch-selber [U] |
| 0.5.2 Längenmaß | u. a. Sockel, Kehlen, **Gehrungen an Fliesen- und Plattenkanten**, **Schrägschnitte**, Rinnen und Roste, Schienen, Bewegungsfugen | Die Schnittlänge je Schnittart aus dem Prototyp ist direkt eine LV-Menge (m) | bau-doch-selber [U] |
| 0.5.3 Stück | u. a. Anarbeiten an Aussparungen > 0,1 m², Einsetzen von Sinkkastenaufsätzen, elastische Fugenfüllung an Bodenentwässerungen | Punktablauf: Stückposition „Aufsatz einsetzen“ | bau-doch-selber [U] |
| Projekt-ZTV (Beispiel) | „Mit dem Preis sind die üblichen Verlegearten (Kreuzfuge, Verband, **Diagonalverlegung**) abgegolten. **Schrägschnitte**, die bei Diagonalverlegung in verstärktem Maße vorhanden sind, können zusätzlich berechnet werden, wenn diese Verlegeart nicht in der Leistungsposition ausdrücklich vorgesehen ist.“ Besondere Leistung u. a.: „Verlegen im Gefälle“, „Friese, Bordüren“, „Ausbilden von Rinnen“ | Muster und Gefälle **explizit** ins LV schreiben, sonst folgt ein Nachtrag | Cosuno-Ausschreibung WGH 34 WE [V als LV-Beispiel, keine ATV] |

**STLB-Bau LB 024:** Die Leistungstexte (Dynamische BauDaten) sind lizenzpflichtig. Zulagepositionen für Muster, Gefälle und Schnitte habe ich **nicht eingesehen**. Deshalb nenne ich keine Positionsnummern [U].

### Arbeitswerte (was öffentlich ist)

- **ARH-Tabellen** (Zeittechnik-Verlag, hrsg. von ZDB und HDB mit IG BAU). Sie sind nach § 3 Rahmentarifvertrag Leistungslohn maßgebend und durch Zeitmessungen ermittelt. Teil 1 deckt Kleinformate 10×10 bis 45×45 ab, Teil 2 Großformate 30×60 bis 60×120 [V].
  - Laut Leseprobe Teil 2, Bodenbeläge bis 5 m² je Raum: Rüsten 0,18 h/m², Ansetzen 0,50 / 0,55 / 0,86 / 1,06 h/m² je Formatgruppe (5–6 bis 1–2 Stück/m²), Verfugen 0,11–0,12 h/m², Zulage rektifiziert 0,08–0,10 h/m² [V].
  - Außerdem Zulagen „diagonal verlegt einschließlich Zuschnitt“ und „richtungsgebundenes Dekor“ mit **0,05 bzw. 0,10 h/m²**. Die Spaltenzuordnung ist im extrahierten Text nicht eindeutig [V Werte / U Zuordnung].
  - Das Handzuschneiden steckt im Ansetzen; Löcher werden mit 0,5 je m² angesetzt [V].
  - Fischgrät-, Chevron- oder Gefällezuschläge sind in der Leseprobe nicht sichtbar [U]. Die Vollversion ist kostenpflichtig.
- **sirAdos Kalkulationshandbuch Fliesen- und Bodenleger 2026** (Leseprobe): Mittellohn Fliesenarbeiten 56,35 €/h, Facharbeiter mittel 59,30 €/h; Positionen mit Minuten je m², z. B. Mosaik Wand 58,8 min/m² [V Leseprobe]. Im Prototyp dient das nur als Beispielstundensatz.
- **Fachverband Fliesen und Naturstein:** Eine öffentliche Kalkulationshilfe mit Musterzuschlägen habe ich nicht gefunden [U].

### Verschnittzuschläge (nur Richtwerte)

| Muster | Zuschlag | Quelle | Status |
|---|---|---|---|
| gerade, Kreuzfuge | 5–8 % (bis 10 %) | Ratgeber und Rechner (materialwissen, rechnerplus, chillicut) | [U] |
| Halb- und Drittelverband | 8–14 % | dieselben | [U] |
| diagonal | 10–20 % | dieselben; werkflow (AT, „nach ÖNORM B 2207“: Diagonal 10–15 %) | [U] |
| Fischgrät | 15–20 % (Fliese, Ratgeber) bzw. **ca. 10 %** (Parkett) | Boen-Verlegeanleitung (über GHZ Cham); Daedelow („+10 % Verschnitt“) | [V] Hersteller / [U] Ratgeber |
| Chevron | keine Herstellerzahl gefunden | – | – |
| Branchenbenchmark | 10–15 % | Wu et al. 2021 (Journal of Cleaner Production) | [V] |

EN 14411 und DIN 18352 nennen **keinen** Verschnittfaktor [U, bestätigt durch Rechner-Hersteller]. Zuschläge je Muster ignorieren die Raumform, die Knicklinien und die Reststückverwertung. Sie sind für Duschen mit mehrfachem Gefälle ungeeignet (siehe Abschnitt 5).

**Vorschlag Kalkulationskette:** Material nach **Stück** aus dem Verlegeplan (nach Reststückverwertung), dazu Bruch und Reserve als eigener Zuschlag, aufgerundet auf Pakete. Die Leistung nach VOB-Fläche + Schrägschnitt/Gehrung in m (0.5.2) + Stückpositionen (0.5.3) + Besondere Leistung „Gefälle“ und „Muster“. Die Arbeitszeit aus ARH-Grundwert + Zulagen oder, im Prototyp, aus Schnittanzahl × Minuten je Schnittart (Beispielwerte).

## 3. Algorithmen

### Muster als periodische Kachelung

Jedes Muster ist ein **Motiv** (1–2 Rohlinge mit Sollform) plus zwei **Gittervektoren** t1 und t2 (Kristallographie der Ebene: Wallpaper Groups, Schattschneider 1978).

| Muster | Motiv | Gittervektoren (L = Länge, W = Breite, f = Fuge) | Füllgrad | Symmetriegruppe [U, eigene Bestimmung] |
|---|---|---|---|---|
| Kreuzfuge | 1 Rechteck | (L+f, 0), (0, W+f) | LW/((L+f)(W+f)) | p4m (Quadrat) bzw. pmm |
| Verband Versatz k | 1 Rechteck | (L+f, 0), (k(L+f), W+f) | wie oben | cmm (k = ½), p2 (k = ⅓) |
| Fischgrät | H- und V-Stab | (W+f, W+f), (L+f, −(L+f)), dann um 45° gedreht | wie oben | pgg |
| Chevron (Gehrung φ) | R- und L-Parallelogramm, Versatz W/tan φ | (0, (W+f)/cos β), (2((L−W/tan φ)cos β + f), 0), β = 90° − φ | (L−W/tan φ)W / Zelle | pmg |

Die Füllgrade prüft `test_fuellgrad_formeln`. Die Tests `test_flaechenbilanz` und `test_stuecke_eben_und_nicht_ueber_knick` stellen sicher, dass die verlegten Stücke überlappungsfrei sind.

### Pseudocode (Prototyp B16)

```
eingabe: Raumpolygon R, Gefälle s, Entwässerung, Muster M(Motive, t1, t2), Fuge f, Regeln
1  Facetten F_k (Ebene z = a_k x + b_k y + c_k, Draufsicht-Polygon P_k) aus Entwässerung
   Knicklinien K = {P_i ∩ P_j | Ebene_i ≠ Ebene_j}; Art = Kehle, wenn z(K) < Mittel der Nachbarn
2  Verlegeflächen V_k = P_k ∩ R⁻(Randfuge) − Puffer(K, f/2) − Puffer(Ablauf, Anschlussfuge)
3  für Rasterursprung (u, v) ∈ {0, 1/n, …}²:                          # Grid-Search
4    für jedes Motiv m, jede Gitterzelle (i, j) mit Hüllbox ∩ R ≠ ∅:
5      T = Trans(u t1 + v t2 + i t1 + j t2) · M_m;  S = T(Sollform_m)
6      für jede Facette k mit V_k ∩ S ≠ ∅:
7        für jedes Teilpolygon p ∈ S ∩ V_k:
8          wenn Inkreis(p) < 2f: als Fuge verfüllen, weiter
9          Kanten e von p, die nicht auf der Rohlingkante liegen, sind Schnitte:
             e ⊂ Knickfugenrand → Gratschnitt; e ⊂ Ablaufrand → Ablauf;
             e ⊂ Wandrand → gerade (∥/⊥ Fliesenachse) sonst schräg;
             e ⊂ Sollrand (nicht Rohlingrand) → Gehrung (Formschnitt Chevron)
10         Stück(p, Facette k, lokal = T⁻¹(p), Schnitte)
11   Bedarf je Position = Anzahl berührter (i, j, m)
12   Greedy-Reststück (je Artikel):
       Schnittstücke absteigend nach Fläche;
       für Stück q: suche Rest r im Pool und Symmetrie g ∈ Sym⁺(Rohling) (0°/180°, Quadrat +90°/270°)
                    mit g(q) ⊂ r und Fabrikkanten(g(q)) ⊂ Fabrikkanten(r); wähle kleinstes r (Best Fit)
       gefunden: r ← r − Puffer(g(q), Schnittfuge/2); sonst neuer Rohling, Rest = Rohling − Puffer(q)
       Reste < Mindestfläche → Abfall
13   Kennzahlen: ganz, Stücke je Kategorie, Schnitte je Art (Anzahl, Länge), Kleinstücke,
     Verschnitt = (N·A_Rohling − A_verlegt)/(N·A_Rohling), Pakete = ⌈N/Paketinhalt⌉
14   Ziel = N·Preis + Σ Schnitte·Minuten·Lohn/60 + Kleinstücke·Malus
15 Ergebnis = argmin Ziel (Gleichstand: Stückzahl, Schnitte, u, v → deterministisch)
16 3D: jeder Stückpunkt (x, y) → (x, y, z_k(x, y)); IFC je Stück oder aggregiert
```

**Einordnung:** Nach der Typologie von Wäscher et al. (2007) ist die Reststückverwertung ein zweidimensionales, **irreguläres** Input-Minimierungsproblem mit identischen Rohlingen (Bin Packing mit Restverwertung). Dafür gibt es exakte Verfahren seit Gilmore/Gomory (1961, eindimensional LP) und Nesting-Geometrie (No-Fit-Polygon; Bennell/Oliveira 2008).

Der Greedy-Ansatz ist bewusst fachlich eingeschränkt. Er erlaubt nur Drehungen, die den Rohling auf sich abbilden, also keine freie Verschiebung. Dadurch landet eine Schnittkante nie in der Fläche. Das ist strenger als freies Nesting mit OpenNest, wie es Wu et al. und Domonkos et al. nutzen. Dafür ist es ohne Schnittplan-Nachbearbeitung fachgerecht. Freies Nesting mit Kantenregel wäre der nächste Schritt (Xu et al. 2023: „edge-to-edge cutting“ nach Handwerksregeln).

**Was die Literatur schon kann:**
- Muster über eine allgemeine Darstellung (Gitter, Chevron, Fischgrät), Breitensuche und komplementäre Schnittstücke: Xu, Wang, Yang (2023).
- Startpunkt per evolutionärem Algorithmus, Verschnitt 3,4–5,5 % statt 10–15 %: Wu et al. (2021, 2022).
- Geometrie-Perturbation von Wänden: Domonkos et al. (2024).
- Revit bzw. BIM: Karunasena et al. (2024), Ergen/Bettemir (2025).
- Nesting und Mehrzieloptimierung: Pham et al. (2025).

**Was fehlt (Lücke für die Arbeit):** In keiner der gefundenen Arbeiten kommen **mehrfaches Gefälle mit Grat- und Kehlschnitten** vor, auch keine **Fabrikkanten-Regel** bei der Restverwertung und keine **IFC-Einzelstücke mit Rohling-Herkunft und Charge** [U, Stand der Suche].

### Software als Referenz

- **Palette CAD:** Fliesenplaner mit automatischen Verlegemustern und Einzelbearbeitung der Fliesen. Die Verschnittoptimierung legt Schnittart, Zuschnittausrichtung, Schnittbreite und Zuschläge fest und gibt Stücklisten, Verschnittpläne und **Etiketten mit Barcodes** aus. Die Academy hat ein Kapitel „Bodengleiche Dusche mit Rinne und Gefälle einfügen“ [V Hersteller]. Ob Grat- und Kehlschnitte beim Punktablauf automatisch entstehen, habe ich nicht geprüft [U].
- **Dynamo Generative Design** (Autodesk): Workflow „Reducing Material Waste“ mit den Zielen ganze Fliesen maximieren, Teilfliesen und Abfall minimieren sowie Drehung und Versatz als Variablen [V].
- **OpenNest** (Grasshopper): Nesting-Plugin, in Wu 2022 und Domonkos 2024 benutzt [V über die Aufsätze].
- Ein Open-Source-Werkzeug speziell für Fliesenverlegung mit Gefälle habe ich nicht gefunden [U].

## 4. IFC-Mapping

| Frage | Ergebnis | Status |
|---|---|---|
| Klasse je Stück | `IfcCovering` (FLOORING über den Typ) als Kind eines Belag-`IfcCovering` per `IfcRelAggregates`. `IfcCovering` ist in IFC 4.3 ein `IfcBuiltElement`. Die IfcCovering-Doku listet die Konzepte Body SweptSolid, Surface Geometry, Material Set, Object Typing, Psets/Qto und Spatial Containment, aber **keine Dekomposition** | GitHub IFC4.3.x-development, IfcCovering.md [V]; Validation Service offen [U] |
| Alternative Klasse | `IfcBuildingElementPart`: Das Enum (APRON, ARMOURUNIT, INSULATION, PRECASTPANEL, SAFETYCAGE) enthält keine Fliese, also nur USERDEFINED. Außerdem geht dann die Covering-Semantik verloren (Raumbezug, FLOORING) | Schema IFC4X3_ADD2 [V]; Bewertung [U] |
| Raumbezug | Belag mit eigener Geometrie: `IfcRelContainedInSpatialStructure` im `IfcSpace` (Doku-Leitlinie); zusätzlich `IfcRelCoversSpaces` | IfcCovering-Doku [V] |
| Geometrie Schnittstück | geschlossenes `IfcPolygonalFaceSet` (Oberseite auf der Gefälleebene, Unterseite −Dicke) | Prototyp, validiert [V] |
| Geometrie ganze Fliese | `IfcMappedItem` auf die `RepresentationMap` des `IfcCoveringType`, `IfcCartesianTransformationOperator3D` mit Axis1 in der Ebene und Axis3 = Flächennormale (gekippt). Pro Sollform (L/R) eine Vorlage | Prototyp, validiert [V] |
| Mengen | `Qto_CoveringBaseQuantities` = {Width, GrossArea, NetArea}, nicht mehr. Schnittlänge, Stückzahl und Verschnitt gehören in eigene Sets | Schema-Templates IfcOpenShell [V] |
| Artikel | `Pset_ManufacturerTypeInformation.GlobalTradeItemNumber` am Typ (je Artikel; bei Formteil L und R zwei Typen) | [V], vgl. Recherche 13 |
| Charge / Kaliber | `Pset_ManufacturerOccurrence` = {AcquisitionDate, BarCode, SerialNumber, **BatchReference**, AssemblyPlace, ManufacturingDate}. Charge am Belag; bei gemischten Chargen je Stück. Das Kaliber hat kein Standard-Property → `HP_Verlegung.Kaliber` | Schema [V]; Vorschlag [U] |
| Verlegeparameter | `HP_Verlegung` aus Recherche 13, ergänzt um Rasterursprung u/v, Gefälle, Entwässerung, Verschnitt, RohlingeBedarf, Pakete | Vorschlag [U] |
| Stückdaten | **`HP_Fliesenstueck`** (Vorschlag): Stueckart (ganz/gerade/schraeg/gehrung/gratschnitt/ablauf), Motiv (H/V/L/R/Q), Rasterposition, Gefaelleflaeche, Rohling (Artikel#Nr), Herkunft (neu/reststueck), Schnitte, Schnittlaenge, Schnittarten | Prototyp [U] |
| Dateigröße (4,77 m² Dusche) | 60×60: einzeln 70 kB / 1 011 Entitäten / 33 Coverings; aggregiert 31 kB / 440. Chevron 60×10: einzeln **430 kB / 5 670 / 193**; aggregiert **176 kB / 2 144 / 1** | Prototyp [V] |
| Hochrechnung | 60 m² Fliese/Parkett im Haus bei ähnlicher Stückdichte ≈ 12 × → rund 5 MB (einzeln) bzw. 2 MB (aggregiert). Das ist tragbar; für Viewer ist die aggregierte Form mit Instanzen günstiger | Schätzung [U] |
| Reifegrad | P/R: nur `HP_Verlegung` + Fläche. A: Einzelstücke mit Herkunft und Charge. So bleibt das Festschreibungsschema aus Recherche 13 gültig; der Hash umfasst dann auch u/v und die Stückliste | Vorschlag [U] |

**Beide Varianten bestanden `ifcopenshell.validate` mit EXPRESS-Regeln ohne Befund. Beide Läufe erzeugten byte-identische Dateien** (Test `test_ifc_deterministisch_und_vollstaendig`) [V].

## 5. Prototyp-Ergebnisse (alle Zahlen Beispielwerte)

**Eingabe:**
- Raum: regelmäßiges Achteck, Innenkreis 2 400 mm, Fläche 4,772 m², Wandfuge 3 mm.
- Gefälle: 1,5 %.
- Entwässerung **Punkt**: Rost 150×150 mm mittig, 8 Dreiecksflächen, 8 Kehlen, Randhöhe 18 mm.
- Entwässerung **Zwei Rinnen**: wandbündig Ost/West, 70 mm breit, auf Wandlänge 994 mm gekürzt; Grat in der Mitte, Kehlen an den Rinnen-Innenkanten, ebene Rinnenzonen (Zwickel).
- Fuge 3 mm, Schnittfuge 1,5 mm.
- Fliesen: 60×60 (3 Stück/Paket, 18 €) und Stäbchen 60×10 (24 Stück/Paket, 4,50 €); Chevron-Formteil L/R 5,40 €.
- Kleinstück-Regeln: < ⅓ Sollfläche, < 20 mm Inkreis; unter 6 mm wird verfugt.
- Grid-Search 6 × 6 = 36 Ursprünge je Fall.

**Laufzeit:** 3 min für alle 10 Fälle (je Lage 0,1–1 s).

### Beste Lage je Fall

„Position“ = je berührter Rasterposition ein Rohling. „Greedy“ = nach Reststückverwertung. „naiv“ = jedes Stück aus eigenem Rohling. Schnitte = Anzahl der Kanten je Art (obere Schranke; ein Schnitt über zwei Stücke wird doppelt gezählt).

| Fall | u, v | Rohlinge Position → Greedy | naiv | Verschnitt Position → Greedy | Verschnitt Stück | ganz / Sollform ganz | Stücke | Pakete | Schnitte ger/schr/Gehr/Grat/Abl | Schnittlänge m | Schnittzeit min | klein < ⅓ / < 20 mm | verfugt |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
| gerade 60×60, Punkt | 0,00 / 0,00 | 16 → 14 | 32 | 19,2 → **7,6 %** | 1,1 | 0 / 0 | 32 | 5 | 8/12/0/32/16 | 27,8 | 176 | 12 / 0 | 0 |
| gerade 60×10 (⅓-Verband), Punkt | 0,67 / 0,83 | 104 → 80 | 177 | 27,3 → **5,5 %** | 4,4 | 9 / 9 | 177 | 4 | 26/34/0/147/13 | 26,9 | 514 | 76 / 7 | 4 |
| Fischgrät 60×10, Punkt | 0,83 / 0,00 | 96 → 85 | 168 | 21,2 → **11,0 %** | 9,4 | 7 / 7 | 168 | 4 | 24/32/0/147/15 | 27,0 | 516 | 67 / 2 | 3 |
| Chevron 60×10 aus Rechteck, Punkt | 0,67 / 0,33 | 115 → 98 | 192 | 34,6 → **23,2 %** | 22,8 | 0 / 15 | 192 | 5 | 27/30/220/158/14 | 50,7 | 868 | 78 / 5 | 13 |
| Chevron-Formteil L/R, Punkt | 0,67 / 0,33 | 115 → 99 | 192 | 21,5 → **8,8 %** | 8,7 | 15 / 15 | 192 | 5 | 27/30/0/158/14 | 25,5 | 538 | 78 / 5 | 13 |
| gerade 60×60, 2 Rinnen | 0,00 / 0,83 | 18 → 14 | 22 | 29,6 → **9,5 %** | 1,3 | 2 / 2 | 22 | 5 | 4/16/0/13/8 | 10,9 | 100 | 8 / 0 | 0 |
| gerade 60×10, 2 Rinnen | 0,00 / 0,67 | 99 → 78 | 127 | 25,2 → **5,0 %** | 3,9 | 27 / 27 | 127 | 4 | 7/33/0/58/30 | 13,1 | 338 | 38 / 1 | 3 |
| Fischgrät 60×10, 2 Rinnen | 0,17 / 0,17 | 96 → 79 | 117 | 22,8 → **6,2 %** | 4,9 | 33 / 33 | 117 | 4 | 29/18/0/43/24 | 13,0 | 268 | 33 / 0 | 4 |
| Chevron aus Rechteck, 2 Rinnen | 0,17 / 0,00 | 120 → 97 | 124 | 38,5 → **23,9 %** | 23,1 | 0 / 49 | 124 | 5 | 32/20/177/27/24 | 34,8 | 501 | 32 / 0 | 3 |
| Chevron-Formteil, 2 Rinnen | 0,17 / 0,00 | 120 → 98 | 124 | 26,1 → **9,6 %** | 9,4 | 49 / 49 | 124 | 6 | 32/20/0/27/24 | 10,7 | 236 | 32 / 0 | 3 |

Flächenbilanz (Chevron, Punkt): 4,772 m² Raum = 4,514 m² Fliese + 0,258 m² Fugen (5,4 %). Bei 60×60: 4,655 + 0,117 m² (2,4 %).

### Wirkung des Rasterursprungs

Zielwert = Material + Schnittzeit × 56,35 €/h + 5 € je Kleinstück.

| Fall | Ziel best / Mitte (0,0) / schlechtest | Rohlinge best/Mitte/schlecht | Verschnitt best/Mitte/schlecht | Kleinstücke < ⅓ best/Mitte/schlecht |
|---|---|---|---|---|
| gerade 60×60, Punkt | 477 / 477 / 724 € | 14/14/15 | 7,6/7,6/13,9 % | 12/12/43 |
| gerade 60×10, Punkt | 1 257 / 1 323 / 1 482 € | 80/83/83 | 5,5/8,9/9,0 % | 76/81/92 |
| Fischgrät, Punkt | 1 212 / 1 297 / 1 491 € | 85/84/84 | 11,0/10,0/10,1 % | 67/73/99 |
| Chevron Rechteck, Punkt | 1 671 / 1 802 / 1 958 € | 98/99/97 | 23,2/23,9/22,4 % | 78/88/96 |
| Chevron Formteil, Punkt | 1 455 / 1 582 / 1 751 € | 99/99/106 | 8,8/8,7/14,7 % | 78/88/94 |
| gerade 60×60, Rinnen | 386 / 399 / 492 € | 14/14/15 | 9,5/9,4/15,7 % | 8/8/18 |
| gerade 60×10, Rinnen | 863 / 893 / 982 € | 78/81/81 | 5,0/8,5/8,6 % | 38/39/44 |
| Fischgrät, Rinnen | 773 / 831 / 898 € | 79/82/82 | 6,2/9,6/9,7 % | 33/36/41 |
| Chevron Rechteck, Rinnen | 1 067 / 1 087 / 1 238 € | 97/96/94 | 23,9/23,1/21,5 % | 32/34/44 |
| Chevron Formteil, Rinnen | 910 / 934 / 1 062 € | 98/98/98 | 9,6/9,6/9,6 % | 32/34/46 |

### Beobachtungen [eigene Bewertung, Beispielwerte]

1. **Punktablauf im Achteck:** Alle Stäbchenmuster brauchen 147–158 Gratschnitte. Bei 60×60 ist jede Fliese geschnitten, im Mittel 2,1 Schnitte je Stück. Die Schnittlänge je m² ist beim Punktablauf 2- bis 2,6-mal so hoch wie bei zwei Rinnen. Das bestätigt die Faustregel „Großformat nur mit Linienentwässerung“ quantitativ: Der Verschnitt steigt dabei kaum, die Arbeit schon.
2. **Chevron aus Rechteck-Stäbchen** verdoppelt Schnitte und Schnittzeit gegenüber dem Formteil (449 gegenüber 229 Schnitten, 868 gegenüber 538 min) und kostet 14,6 Prozentpunkte mehr Verschnitt. Das Formteil ist im Beispiel trotz 20 % höherem Stückpreis im Zielwert 216 € günstiger. Die L/R-Bestellung kann aber ein Paket mehr kosten (Rinnen: 3 + 3 statt 5).
3. **Fischgrät ist beim Punktablauf teurer als gerade** (11,0 % gegenüber 5,5 %), bei Rinnen fast gleich (6,2 % gegenüber 5,0 %).
4. **Reststückverwertung:** Beim Chevron (Punkt) kommen 94 von 192 Stücken aus Resten. Ein Teil davon sind die zwei Hälften einer über die Kehle geschnittenen Fliese. Ohne Verwertung („je Position“) lägen alle Fälle bei 19–39 %. Das ist die Spanne, in der pauschale Zuschläge von 10–20 % zu niedrig sind.
5. **Der Rasterursprung** wirkt beim Punktablauf stärker (Zielspanne 247–287 €) als bei Rinnen (106–171 €). Bei 60×60 halbiert er die Kleinstücke (12 statt 43). Das Ziel „Kosten“ wählt nicht immer die kleinste Stückzahl (Chevron: 98 statt 97 Rohlinge), weil die Schnittzeit dominiert.
6. **Kleinstücke unter ⅓ der Sollfläche** sind bei Stäbchen auf Gefälle unvermeidbar (33–78 Stück). Die ⅓-Regel aus dem Rechteckraster ist für Fischgrät, Chevron und Knicklinien **nicht erfüllbar**. Sinnvoll ist eine Breitenregel (Inkreis ≥ 20 mm), die im Optimum fast immer erreichbar ist (0–7 Verstöße).

**Ausgaben:**
- `ausgabe/b16_ergebnis.json` (alle Fälle: beste Lage, Mitte, schlechteste Lage)
- `ausgabe/b16_<fall>.svg` (10 Draufsichten, Farben nach Stückart, Kleinstücke rot, Kehle/Grat gestrichelt)
- `ausgabe/b16_stuecke_chevron_60x10__punkt.json` (192 Stücke mit 3D-Polygon)
- `ausgabe/b16_{gerade_60x60,chevron_60x10}__punkt_{einzeln,aggregiert}.ifc`

**Tests:** `python -m pytest tests/test_b16.py` → **15 bestanden in ca. 10 s**. Geprüft werden:
- Achteckfläche und Facetten, Kehle/Grat, Höhen;
- Flächenbilanz (Summe Stücke + Fugen = Raum, keine Überlappung, Füllgrad ± 1,2 %);
- jedes Stück eben in genau einer Facette, kein Stück über einer Knicklinie, alle Schnitte klassifiziert;
- Determinismus von Kennzahlen, 3D-Stückliste und IFC (byte-identisch), IFC-Vollständigkeit (Coverings, Aggregation, MappedItems, Qto, GTIN);
- Chevron-Verschnitt größer als gerade (60×10 und 60×60, beide Entwässerungen, ≥ 1/6), Formteil mindestens 8 Prozentpunkte besser;
- Wiederverwendung (Greedy ≤ Position ≤ naiv, 180°-Fall, keine Spiegelung);
- Kleinstück-Regel;
- Rasteroptimierung (best ≤ Mitte, Kleinstücke best ≤ schlechtest);
- Pakete (L/R getrennt).

## 6. Warnungen

1. **„DIN 18534 schreibt 1,5–2 % vor“ ist falsch.** Ratgeber schreiben das (rechenportal, holztools), die Hersteller-Fachartikel sagen das Gegenteil (Dallmer/Göke). info-bauleitung hat „mindestens 2 %“ selbst auf „maximal 2 %“ korrigiert [V/U].
2. **Die 2-%-Grenze „barrierefrei“ steht nicht in DIN 18040-2.** Dort stehen nur niveaugleich und ≤ 2 cm Absenkung; laut nullbarriere stammt die Grenze aus VDI 6008-2. Vor der Übernahme in eine Regel-ID am Normtext prüfen [U].
3. **Begriffe „Gehrung“ und „Schrägschnitt“:** In ATV DIN 18352 0.5.2 ist die „Gehrung an Fliesen- und Plattenkanten“ die Kantengehrung durch die Dicke (Außenecke). Der Winkelschnitt in der Draufsicht (Chevron, Diagonale, Achteckwand) ist ein **Schrägschnitt**. Die Prototyp-Kategorie `gehrung` meint den Chevron-Formschnitt und gehört ins LV als Schrägschnitt [U].
4. **Übermessungsgrenze nicht verwechseln:** Für DIN 18352 gilt 0,1 m². Die 2,5 m², die eine Ratgeberseite für „Fliesen“ nennt, gelten für andere ATV (Putz, Trockenbau, Maler) [V/U].
5. **Der Greedy-Wert ist optimistisch.** Er setzt voraus, dass jedes Reststück auf der Baustelle sortiert, gelagert und wiedergefunden wird. Bruch, Fehlschnitt, Reserve für Reparaturen (gleiche Charge!) und Paketrundung sind **nicht** im Verschnitt enthalten. Der Realwert liegt zwischen „Greedy“ und „je Position“. Empfehlung: Greedy-Menge + 3–5 % Bruch/Reserve, dann auf Pakete runden [U].
6. **Parkett ist nicht Keramik.** Bei Nut/Feder-Stäben vertauscht eine 180°-Drehung Nut und Feder. Die zulässige Symmetrie ist dann nur die Identität, und L/R-Stäbe sind getrennte Artikel. Das geht im Prototyp nur über den Formteil-Modus; für Parkett braucht es einen Schalter „drehbar“ je Artikel. Dasselbe gilt für richtungsgebundenes Dekor (Holzoptik, Maserung) bei Fliesen [U].
7. **Chevron aus Rechteckfliesen legt Schnittkanten in die Sichtfläche** (Mitte des Zopfs). Bei glasierter Keramik müssen diese Kanten nachgearbeitet werden, oder man nimmt Formteile. Der Prototyp zählt die Gehrungen, bewertet aber nicht die Kantenqualität [U].
8. **Mindestschnittmaße sind Handwerksregeln.** Die ⅓- bzw. ½-Regel ist für Fischgrät, Chevron und Gefälleflächen nicht einhaltbar (Beobachtung 6). Die Breitenregel 20 mm und die Verfug-Grenze 6 mm sind **Beispielwerte**. Das gehört als vereinbarte Firmenregel ins LV, nicht als „Norm“.
9. **Die Geometrie ist idealisiert:** exakt ebene Facetten, Rost und Rinne auf Nullniveau, Rinnenzonen eben, Wandfuge konstant. Die Draufsicht wird senkrecht auf die Ebene projiziert (Längenfehler ≤ 0,011 % bei 1,5 %). Die Seitenflächen der Stücke im IFC stehen lotrecht statt normal zur Ebene. Die Rohbautoleranz (DIN 18202) und das Kaliber der Fliesen sind nicht modelliert.
10. **Schnittzählung:** Jede Stückkante zählt als Schnitt. Eine über die Kehle geteilte Fliese zählt deshalb zweimal. Die Minuten je Schnittart sind Beispielwerte, **keine ARH-Werte**. Die ARH-Zulagen „diagonal/richtungsgebunden“ (0,05/0,10 h/m²) sind in der Spaltenzuordnung unsicher.
11. **IFC-Aggregation von Coverings** ist in der Doku kein eigenes Konzept. Die EXPRESS-Prüfung ist bestanden; Validation Service und MVD/IDS-Regeln sind noch offen. `IfcBuildingElementPart` als Alternative hat keinen passenden PredefinedType.
12. **Die Zielfunktion und alle Preise sind Beispielwerte.** Die „beste Lage“ hängt an den Gewichten. Für Thesenaussagen immer die Spanne (best/Mitte/schlechtest) berichten, nicht nur das Optimum.
13. **Quellenzugang:** Crossref war per curl gesperrt; alle DOIs habe ich über die Crossref-API via Exa-Abruf geprüft. ZDB-Merkblätter („Bodengleiche Duschen“, „Groß- und Megaformate“), STLB-Bau LB 024 und die ARH-Vollversion habe ich **nicht eingesehen** (kostenpflichtig oder lizenziert).

## Literatur (DOIs über die Crossref-API geprüft)

- Wu, S.; Zhang, N.; Luo, X.; Lu, W.-Z. (2021): Intelligent optimal design of floor tiles: A goal-oriented approach based on BIM and parametric design platform. *Journal of Cleaner Production* 299, 126754. doi:10.1016/j.jclepro.2021.126754 [V]
- Wu, S. et al. (2022): Automated Layout Design Approach of Floor Tiles: Based on Building Information Modeling (BIM) via Parametric Design (PD) Platform. *Buildings* 12(2), 250. doi:10.3390/buildings12020250 [V]
- Xu, Y.; Wang, J.; Yang, Z. (2023): Generic goal-oriented design for layout and cutting of floor tiles. *Automation in Construction* 152, 104903. doi:10.1016/j.autcon.2023.104903 [V; Band laut Verlag: Ausgabe 08/2023]
- Karunasena, S.; Park, S.; Ju, S.; Heo, J. (2024): Optimal Floor Tile Layout Plan Generation Based on Building Information Modeling (BIM). *Computing in Civil Engineering 2023*, ASCE. doi:10.1061/9780784485231.036 [V]
- Domonkos, N.; Martinek, J. Z.; Fehér, E. (2024): Optimal Layout of Modular Systems by Geometric Perturbations. *Építés – Építészettudomány* 52(3–4), 235–250. doi:10.1556/096.2024.00123 [V]
- Pham, V. H. S.; Dau, T. D.; Nguyen, T. T. (2025): Optimizing floor tile design in residential spaces using nesting algorithm and multi-objective optimization with BIM data. *Canadian Journal of Civil Engineering* 52(4), 431–445. doi:10.1139/cjce-2024-0241 [V]
- Ergen, F.; Bettemir, Ö. H. (2025): BIM-driven software and algorithm for optimal floor tile layout minimizing material waste. *Automation in Construction* (05/2025). doi:10.1016/j.autcon.2025.106115 [V]
- Wäscher, G.; Haußner, H.; Schumann, H. (2007): An improved typology of cutting and packing problems. *European Journal of Operational Research* 183(3). doi:10.1016/j.ejor.2005.12.047 [V]
- Bennell, J. A.; Oliveira, J. F. (2008): The geometry of nesting problems: A tutorial. *European Journal of Operational Research* 184(2). doi:10.1016/j.ejor.2006.11.038 [V]
- Gilmore, P. C.; Gomory, R. E. (1961): A Linear Programming Approach to the Cutting-Stock Problem. *Operations Research* 9(6), 849–859. doi:10.1287/opre.9.6.849 [V]
- Schattschneider, D. (1978): The Plane Symmetry Groups: Their Recognition and Notation. *American Mathematical Monthly* 85(6). doi:10.1080/00029890.1978.11994612 [V]
- Borgmeier, A.; Braunreiter, H. (2009): Bautechnik für Fliesen-, Platten- und Mosaikleger. Vieweg+Teubner. doi:10.1007/978-3-8348-9287-4. Enthält u. a. „Materialbedarf Gefälleboden zu einer Rinne / zu einem Punkt“ und „rechnerische Einteilung Diagonalverlegung“ [V Verlagsseite, Inhalt nicht eingesehen]

**Normen, Regelwerke, Hersteller (ohne DOI):**
- DIN 18534-1/-3 (2025-10);
- ATV DIN 18352:2019-09 (dinmedia, baunormenlexikon);
- DIN 18040-1/-2; VDI 6008 Blatt 2:2012-12 (nicht eingesehen);
- ZDB-Fliesenhandbuch 9. Aufl. (Leseprobe, pageplace);
- ARH-Tabellen Fliesen Teil 1/2 (Zeittechnik-Verlag, Leseprobe);
- sirAdos Kalkulationshandbuch 2026 (Leseprobe);
- TECE TI Entwässerungstechnik (2025-05);
- Dallmer/Göke (IHKS-Fachjournal; Bundesbaublatt 29.06.2018);
- Jenke/Göke (IKZ);
- FCT/ÖFV Merkblatt 3;
- Hafro-, Boen-, Daedelow-, Scheucher- und HKS-Verlegeanleitungen;
- Palette CAD (Features, Blog 06/2023, Academy);
- Dynamo Blog 10/2022.

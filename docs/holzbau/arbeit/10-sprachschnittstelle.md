# 10 Sprachschnittstelle

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle geprüft) oder [U] (unsicher); eigene Bewertungen und Designentscheidungen sind als solche formuliert. Zahlen aus dem Prototyp stammen aus `beispiele/b6_intent_pipeline.py`, `beispiele/ausgabe/intent_protokoll.json`, `beispiele/tests/test_b6_b7.py` und aus Messläufen, die in diesem Kapitel mit Datum und Umgebung angegeben sind. **Alle Wahrscheinlichkeiten im Prototyp B6 sind feste, erfundene Stub-Werte und keine Modellausgaben.**

## 10.0 Einordnung und Vorgehen

Das Zielbild beschreibt den Entwurf als Gespräch: Familie H. sagt „Das Bad oben einen Meter größer, Richtung Süden“, und das Modell ändert sich, Kosten und Nachweise folgen, Unzulässiges wird mit Grund und Alternative abgelehnt (`../00-zielbild.md`, Abschnitt 3.1). Kapitel 5 hat gezeigt, dass die Sprach-BIM-Forschung diesen Schritt bisher fast immer dem Sprachmodell überlässt. Das Modell schreibt Code, Daten oder Constraints, die anschließend geprüft werden (Abschnitt 5.6.4). Eine strengere Aufgabenteilung ist nicht dokumentiert (Lücke L6), und für deutschsprachige Intent-Erkennung im Hausentwurf gibt es weder Korpus noch Evaluation (Lücke L7). Dieses Kapitel beantwortet deshalb die Forschungsfrage FF3:

> Wie wird gesprochene deutsche Sprache zuverlässig in deterministische Modelländerungen übersetzt? Welche Aufgaben übernimmt das Sprachmodell, welche der Code?

Die Antwort folgt der Verarbeitungskette einer Äußerung:

1. **Spracherkennung** (10.1): Audio wird lokal und im Strom in Text übersetzt. Fachbegriffe werden begünstigt, und ein Latenzbudget begrenzt die Antwortzeit.
2. **Intent-Erkennung** (10.2): Ein Entscheidungsmodell beantwortet typisierte Fragen aus einem hierarchischen Katalog. Es liefert kalibrierte Wahrscheinlichkeiten, aber keine Werte.
3. **Werteparser und Referenzauflösung** (10.3): Deterministischer Code liest Zahlen, Einheiten und Richtungen und löst „das Bad oben“ gegen den Modellzustand in eine IFC-GlobalId auf.
4. **Dialogsteuerung** (10.4): Schwellwerte je Risikoklasse entscheiden über Ausführen, Vorschau, Rückfrage oder Ablehnung. Transparenz nach Art. 50 KI-VO und Datenschutz sind Teil dieser Steuerung.
5. **Evaluation** (10.5): Ein deutsches Testset mit Fachbegriffen und ein Messplan für WER, Intent-Accuracy, Slot-F1, Kalibrierungsfehler und End-to-End-Erfolg, dazu ein Plan für das Fine-Tuning des Intent-Modells.

Der Prototyp B6 implementiert den deterministischen Teil der Kette: Werteparser, Raumreferenz, Anwendung eines Intents mit Regelprüfung. Das Intent-Modell ist darin ein Stub. Der Stub hat dieselbe Schnittstelle wie Laya bzw. Jev, liefert aber feste Wahrscheinlichkeiten aus einer Schlüsselworttabelle. Neu in diesem Kapitel sind drei maschinenlesbare Dateien: der vollständige Intent-Katalog `spezifikation/intents.yaml`, die Grammatik des Werteparsers `spezifikation/werteparser-grammatik.md` und das Testset `spezifikation/sprach-testset.jsonl`. B6 wurde gegen dieses Testset gemessen. Die Messung zeigt, was der Prototyp heute kann und wo die Grammatik über ihn hinausgeht.

## 10.1 Spracherkennung für Deutsch

### 10.1.1 Anforderungen aus dem Entwurfsdialog

Die Spracherkennung (ASR) eines Entwurfswerkzeugs unterscheidet sich von Diktat und Sprachassistent in vier Punkten:

- **Zahlen tragen die Bedeutung.** „Eins zwanzig“ und „eins fünfzig“ unterscheiden sich um 30 cm Raumbreite. Ein Erkennungsfehler an einer Zahl ist folgenreicher als an einem Füllwort. Die Wortfehlerrate (WER) allein misst das nicht.
- **Fachbegriffe sind selten.** „Kniestock“, „Ortgang“, „Rigole“ oder „Zwerchgiebel“ kommen in allgemeinen Trainingsdaten kaum vor. Deutsche Sprachdatensätze aus dem Bauwesen wurden nicht gefunden (Recherche 03) [V].
- **Die Äußerungen sind kurz, der Kontext ist bekannt.** Eine Äußerung umfasst typischerweise fünf bis fünfzehn Wörter. Das System kennt aber den Modellzustand, die Auswahl und die zuletzt gestellte Rückfrage. Diesen Kontext kann die Erkennung nutzen.
- **Die Antwort muss schnell kommen.** Eine Sprachschnittstelle, die langsamer ist als ein Klick, wird für einfache Änderungen nicht genutzt. Chen et al. berichten laut Einzelbewertung, dass Nutzer bei Änderungen eines einzelnen Parameters den Schieberegler bevorzugen [@chen2025agent]. Sprache muss sich daher bei zusammengesetzten Änderungen lohnen und darf bei einfachen nicht bremsen.

Große, schwach überwachte Modelle wie Whisper erreichen eine hohe Robustheit ohne Feinabstimmung [@radford2023whisper]. Für seltenes Vokabular ist Contextual Biasing das Standardverfahren: Eine Liste von Kontextphrasen wird zur Laufzeit begünstigt. Das End-to-End-Verfahren CLAS senkte die relative WER gegenüber einer nachgeschalteten Fusion um bis zu 68 % [@pundak2018deep]. Die Arbeit übernimmt nur das Prinzip über die Boosting-Funktionen verfügbarer Modelle, nicht das Google-interne System.

### 10.1.2 Modellvergleich

Recherche 03 hat die für Deutsch verfügbaren offenen Modelle gesichtet. Tabelle 10.1 fasst den Befund zusammen.

**Tabelle 10.1: Spracherkennung für Deutsch (Recherche 03)**

| Modell | Lizenz | Streaming | Fachbegriffe | Befund | Urteil |
|---|---|---|---|---|---|
| Voxtral Mini 4B Realtime 2602 | Apache 2.0 | ja, Verzögerung 80–2400 ms einstellbar | [U] | DE-WER 6,19 % bei 480 ms Verzögerung [V] | übernehmen (Favorit) |
| Parakeet-TDT-0.6b-v3 | CC-BY-4.0 | ja | Phrase Boosting per Liste | [V] | übernehmen, wenn Fachbegriffe entscheiden |
| Canary-1b-v2 | [U] | ja | Boosting | [V] | Alternative |
| Qwen3-ASR 0.6B/1.7B | [U] | über vLLM | [U] | [V] | Alternative |
| Whisper large-v3-turbo (auch primeline German) | MIT | nur in Stücken | `hotwords`, `initial_prompt` | [V] | Rückfallebene |
| Kyutai STT, Moonshine | – | – | – | kein Deutsch | ungeeignet |

Zwei Befunde prägen die Wahl. Erstens gibt es für den Favoriten keine Angabe zum Fachvokabular, für Parakeet dagegen eine dokumentierte Boosting-Funktion. Zweitens stammt die einzige deutsche Fehlerrate aus der Modellangabe selbst und nicht aus einem Test mit Bauvokabular. Ob Voxtral oder Parakeet für diesen Anwendungsfall besser ist, lässt sich deshalb nur am eigenen Testset entscheiden (Abschnitt 10.5).

> **E10.1 (Spracherkennung).** Die Spracherkennung läuft lokal hinter einer austauschbaren Schnittstelle. Diese liefert n-beste Hypothesen mit Konfidenz und Wortzeiten. Voxtral Realtime ist das Primärmodell, Parakeet v3 mit Boosting wird parallel gemessen, Whisper ist die Rückfallebene. Die endgültige Wahl trifft die Messung von WER, Fachbegriff-Fehlerrate und Zahlfehlerrate am Audio-Testset (10.5.2), nicht die Modellangabe.

Die n-besten Hypothesen sind kein Selbstzweck. Kou und Tan steuerten CAD per Sprache und stellten fest, dass eine CAD-spezifische Grammatik deutlich besser erkennt als freies Diktat [@kou2008design]. Die Folgearbeit filtert Kandidaten nach dem Modellkontext und fragt bei Mehrdeutigkeit nach [@kou2010knowledge]. Übertragen heißt das: Ist die beste Hypothese im aktuellen Kontext unzulässig, etwa weil sie einen Raum nennt, den es nicht gibt, prüft das System die zweite und dritte, bevor es zurückfragt.

### 10.1.3 Fachbegriffe: Boosting und Nachkorrektur

Die Fachbegriffe werden an zwei Stellen behandelt.

**Vor der Erkennung (Boosting).** Die Liste `fachbegriffe` in `intents.yaml` enthält 60 Begriffe mit Varianten. Ihr Kern ist die Startliste aus Recherche 03 (Kniestock, Gaube, Pfette, Sparren, OSB, Schwelle). Erweitert wird sie um alle Slot-Werte des Katalogs, die ein Laie aussprechen könnte, etwa „Krüppelwalmdach“, „Hebeschiebetür“, „Frischwasserstation“ und „Rigole“. Die Liste wird dem Modell als Boosting- bzw. Hotword-Liste übergeben, soweit es das unterstützt (Tabelle 10.1).

**Nach der Erkennung (Nachkorrektur).** Die Varianten der Liste bilden typische Fehltranskripte auf den Begriff ab: „Knie Stock“ wird zu „Kniestock“, „H T Strich“ zu H′T. Varianten, die nur phonetisch ähnlich sind, werden unscharf gegen die Liste abgeglichen (Recherche 03). Die Nachkorrektur ist deterministisch und wird im Protokoll ausgewiesen, damit sich eine falsche Korrektur zurückverfolgen lässt.

Das Testset enthält 40 Sätze mit Fachbegriffen und drei Sätze mit typischen Erkennungsartefakten wie „Den Knie Stock auf eins zwanzig“ und „Eine Schlepp Gaube übers Bad oben“. Herstellerbegriffe wie Wand- und Deckenbezeichnungen fehlen in der Liste noch. Sie sind als Datenlieferung DAT-10-01 geführt.

### 10.1.4 Latenzbudget

Tabelle 10.2 verteilt das Zeitbudget vom Ende der Äußerung bis zur sichtbaren Modelländerung. Das Gesamtziel von 1,5 s ist eine Designentscheidung [U]. Sie ist in der Nutzerstudie zu prüfen (Kapitel 20). Die Zeilen mit „Messung“ sind am 27.09.2026 in der Arbeitsumgebung dieses Kapitels gemessen (Python 3.11.15, Linux-Container), nicht auf der Zielhardware.

**Tabelle 10.2: Latenzbudget einer Äußerung**

| Stufe | Quelle | Wert | Budget |
|---|---|---|---|
| Endpunkterkennung (Sprechpause) | Designwert | – | ≤ 300 ms [U] |
| Spracherkennung, Verzögerung des Stroms | Recherche 03 (Voxtral) | 80–2400 ms einstellbar; 480 ms bei DE-WER 6,19 % [V] | 480 ms |
| Intent-Modell, bis zu drei Aufrufe | Recherche 03 (Laya-Model-Card) | etwa 7 ms je Frage bei zehn Fragen auf einer T4 [V] | 3 × 70 ms = 210 ms (Rechnung) |
| Werteparser, Referenz und Anwendung (B6) | Messung, 1 800 Läufe über die neun B6-Sätze | Median 0,13 ms, 95 %-Quantil 0,23 ms | < 1 ms |
| Regelprüfung je Regel (B4 Abstandsfläche, B5 Treppe) | Messung, je 150 bzw. 50 Läufe | Median 0,62 bzw. 0,57 ms, 95 %-Quantil 0,91 bzw. 0,79 ms | 40 Regeln × 1 ms = 40 ms |
| Neuaufbau von IFC-Ausschnitt und Ansicht | Designwert | Messung ausstehend | ≤ 300 ms [U] |
| **Summe** | | | **≈ 1,33 s ≤ 1,5 s** |

Zwei Folgerungen ergeben sich aus der Tabelle:

1. **Der deterministische Teil ist nicht der Engpass.** Parser, Referenzauflösung und Regelprüfung zusammen liegen zwei bis drei Größenordnungen unter der Spracherkennung. Die Anforderung, nur die von einer Änderung betroffenen Regeln neu auszuwerten (ANF-09-19), dient deshalb weniger der Rechenzeit als der Nachvollziehbarkeit.
2. **Das Budget hängt an der Streaming-Verzögerung.** Mit Whisper, das nur in Stücken arbeitet, ist es nicht einzuhalten. Deshalb ist Whisper nur Rückfallebene (E10.1).

Damit das Warten nicht leer bleibt, zeigt die Oberfläche während des Sprechens das Teiltranskript und nach der Intent-Erkennung sofort die Interpretation („Verstanden: Bad OG · Breite · 2,60 m“), noch bevor das Modell neu aufgebaut ist (10.4.3).

> **E10.2 (Aktivierung).** Das Mikrofon ist nur aktiv, solange der Nutzer eine Taste hält oder nach einem Tippen bis zur Sprechpause (Push-to-talk). Es gibt kein Dauerlauschen und kein Aktivierungswort. Begründung: Unbeabsichtigte Aufnahmen werden vermieden, statt sie nachträglich löschen zu müssen [@edpb2021vva]. Zugleich ist der Beginn einer Äußerung eindeutig, was die Endpunkterkennung vereinfacht.

## 10.2 Intent-Erkennung mit typisierten Fragen

### 10.2.1 Aufgabenteilung: was das Modell entscheidet

In der klassischen Tradition des Spoken Language Understanding wird eine Äußerung in Domäne, Absicht (Intent) und Attribut-Wert-Paare (Slots) überführt [@tur2011spoken]. Gemeinsame Modelle für Intent und Slots sind der Stand der Technik [@chen2019bert; @weld2022survey]. Im Bauwesen zerlegt T2S4BIM Nutzeranfragen mit Transformer-Modellen in Intent und Slots und führt sie als Revit-Aktion aus. Laut Abstract erreichen dort Encoder-Decoder-Modelle wie T5 und FLAN-T5 mit synthetisch erzeugten Trainingsdaten ähnliche Werte wie deutlich größere Decoder-Modelle, bei höherer Effizienz [@wei2025texttostructure]. NADIA-S gliedert eine Speech-to-BIM-Anwendung in sechs Schritte: interpret, fill, match, structure, execute, check [@lee2024generalized].

Die Arbeit übernimmt diese Zerlegung, verteilt die Schritte aber strenger als die Vorbilder. Tabelle 10.3 stellt die Schritte von NADIA-S der eigenen Kette gegenüber und nennt für jeden Schritt, wer entscheidet.

**Tabelle 10.3: Aufgabenteilung zwischen Modell und Code**

| Schritt (NADIA-S) | Aufgabe in dieser Arbeit | entscheidet | Ausgabe |
|---|---|---|---|
| interpret | Transkript; Gruppe, Intent, Aufzählungswerte, Ja/Nein-Merkmale, Stärke | Spracherkennung und Intent-Modell (KI) | Wahrscheinlichkeiten über geschlossene Optionen |
| fill | Zahlen, Einheiten, Richtungen, Ordinale | Werteparser (Code) | Messwerte mit Herkunft |
| match | Raum, Bauteil, Möbel, Katalogartikel | Referenzauflösung und Katalogsuche (Code) | GlobalId bzw. Typobjekt oder Kandidatenliste |
| structure | typisierter Frame nach `intents.yaml` | Code | Frame-JSON |
| execute | Änderung des Parametermodells, Solver | Code | neuer Zustand und Änderungsliste |
| check | Regelprüfung R1–R4, Empfehlungen R5 | Regelmaschine (Code) | Nachweis, Ablehnung mit Alternative |

Das Intent-Modell erzeugt also keinen Code, keine Geometrie und keinen Wert. Es wählt nur aus Optionen, die der Katalog vorgibt. Drei Befunde der Literatur begründen diese Grenze:

- **Rechnen gehört in den Interpreter.** Sprachmodelle, die das Rechnen an einen Interpreter abgeben, lösen Rechenaufgaben deutlich besser als solche, die selbst schrittweise rechnen [@gao2023pal]. In der Architekturgeneration machte die Selbstprüfung von GPT-4 Rechenfehler (Recherche 12) [@kodnongbua2024zeroshot].
- **Räumliches Schließen ist unzuverlässig.** Sprachmodelle bilden Text zuverlässig auf räumliche Relationen ab, scheitern aber am mehrstufigen Schließen [@li2024spatial]. „Das Bad oben“ erkennen sie, welcher Raum das im aktuellen Modell ist, sollen sie nicht entscheiden.
- **Freie Ausgaben halluzinieren.** Flüssige, aber falsche Ausgaben sind ein systematisches Merkmal generativer Modelle [@ji2023hallucination]. Bei geschlossenen Optionen kann eine Halluzination nur die Wahl einer falschen Option sein, und diesen Fehler begrenzt der Schwellwert (10.2.5).

Die Grenze ist zugleich die rechtliche. Nach den Leitlinien der Kommission fallen rein menschlich definierte Regeln und einfache Datenverarbeitung aus dem Begriff des KI-Systems heraus [@eu2025aidefinition]. In der hier gewählten Architektur ist deshalb voraussichtlich nur das Intent-Modell ein KI-System, die Regelmaschine nicht (Recherche 27). Haftungsrechtlich entspricht das der Auslegung als automatisiertes System mit festen, nachvollziehbaren Regeln, nicht als autonomes System [@wilhelmi2020haftung]. Kapitel 7 dokumentiert diese Grenze in der Architektur.

### 10.2.2 Fragetypen: choice, score, noul

Die Intent-Schicht folgt dem Schnittstellenmuster von Jev (Recherche 03) [V]. Eingabe ist ein Zustand und eine Menge typisierter Fragen, Ausgabe sind typisierte Antworten mit Wahrscheinlichkeiten. Das Modell erzeugt keinen Text. Drei Fragetypen werden verwendet:

- **choice:** eine Frage mit 1 bis 255 festen Optionen. Die Antwort ist eine Wahrscheinlichkeitsverteilung über die Optionen. Beispiel: „Welche Dachform ist gemeint?“ mit acht Optionen.
- **score:** eine Rubrik mit 2 bis 10 Stufen. Beispiel: „Wie stark soll die Änderung sein?“ mit den Stufen „sehr wenig“ bis „sehr stark“. Die Frage ersetzt keinen Zahlwert. Sie wird nur gestellt, wenn der Parser keinen Wert gefunden hat („a bissl größer“), und die Stufe führt immer zu einer Vorschau (Regel D10 der Grammatik).
- **noul:** eine Ja/Nein-Frage, die P(wahr) zwischen 0 und 1 liefert, keinen Wahrheitswert. Den Schwellwert legt der eigene Code je Frage fest, abhängig davon, wie teuer ein Fehler ist (Recherche 03) [V].

Alle Fragen eines Aufrufs laufen parallel. Der Katalog nutzt 112 choice-, 11 score- und 15 noul-Fragen. Von den choice-Fragen sind eine die Gruppenfrage `q.gruppe`, 16 die Intent-Fragen der Gruppen (`q.intent.<gruppe>`) und 95 Slotfragen. Fünf Fragen sind global und werden bei jeder Äußerung gestellt: `q.gruppe` und vier noul-Fragen. Tabelle 10.4 zeigt die vier noul-Fragen.

**Tabelle 10.4: Globale noul-Fragen**

| ID | Frage | Schwelle | Wirkung |
|---|---|---|---|
| `n.korrektur` | Korrigiert oder widerruft der Sprecher seine vorige Äußerung? | 0,60 | vorigen Frame ersetzen statt neuen anlegen |
| `n.nur_frage` | Will der Sprecher nur eine Auskunft, ohne etwas zu ändern? | 0,65 | Gruppe „anzeigen_auswerten“ bevorzugen, keine Änderung |
| `n.bezug_vorher` | Bezieht sich die Äußerung auf das zuletzt genannte oder ausgewählte Objekt? | 0,60 | Referenz aus dem Dialogkontext |
| `n.verneinung` | Enthält die Äußerung eine Verneinung des Wunsches? | 0,60 | Aktion invertieren oder zurückfragen |

Die globalen noul-Fragen fangen Dialogphänomene ab, die ein reiner Intent-Klassifikator übersieht. „Nein, nicht das Bad, das Kinderzimmer 1“ ist kein neuer Intent, sondern die Korrektur eines Slots im vorigen Frame. „Wie breit ist das Bad oben?“ und „Mach das Bad oben breiter“ teilen fast alle Wörter, gehören aber zu verschiedenen Gruppen. Laut Model Card meldet der noul-Typ von Laya „wahr“ teils zu selten (Recherche 03) [V]. Die Schwellen der noul-Fragen liegen deshalb unter denen der Intent-Wahl und werden nach der Kalibrierung neu festgelegt (10.2.5).

### 10.2.3 Hierarchie unter 20 Optionen

Laut Model Card verschlechtert sich Laya bei mehr als etwa 20 Optionen einer choice-Frage deutlich (Recherche 03) [V]. Ein flacher Katalog mit 138 Intents ist damit ausgeschlossen. Der Katalog ist deshalb ein Baum mit drei Ebenen:

1. **Gruppe:** eine choice-Frage mit 16 Optionen (`q.gruppe`), dazu die globalen noul-Fragen.
2. **Intent:** die choice-Frage `q.intent.<gruppe>` der gewählten Gruppe, mit höchstens 13 Optionen.
3. **Slotfragen:** die choice-, score- und noul-Fragen des gewählten Intents, etwa „Welche Dachform?“. Diese Ebene entfällt, wenn der Intent keine vom Modell zu beantwortenden Slots hat.

Die größte choice-Frage des Katalogs hat 18 Optionen (Nutzung eines Raums). Der Validator lehnt jede Frage mit mehr als 19 Optionen ab (10.7.1).

Die Hierarchie hat eine bekannte Schwäche: Ein Fehler auf der Gruppenebene lässt sich auf der Intent-Ebene nicht mehr korrigieren. Zwei Maßnahmen begrenzen das.

- **Zwei Gruppen parallel.** Liegt die beste Gruppe unter ihrer Schwelle, wird die Intent-Frage für die beiden besten Gruppen parallel gestellt. Maßgeblich ist dann die Verbundwahrscheinlichkeit P(Gruppe) · P(Intent | Gruppe).
- **Kontextfilter.** Optionen, die im aktuellen Zustand nicht zulässig sind, werden gar nicht angeboten. „Bestätigen“ und „Verneinen“ gibt es nur bei offener Rückfrage, „Alternative wählen“ nur nach einer angebotenen Alternative, „Bemusterung abschließen“ nur in der Bemusterungsphase. Das entspricht der kontextbewussten Inferenz nach Kou et al. [@kou2010knowledge] und verkleinert zugleich die Optionsmengen.

> **E10.3 (Intent-Modell).** Das Intent-Modell ist Laya, lokal betrieben, feinabgestimmt und kalibriert (10.5.4). Jev wird nur mit ausdrücklicher Einwilligung als Cloud-Rückfallebene mit Zero Data Retention genutzt. Ist kein Modell verfügbar, übernimmt ein Schlüsselwortklassifikator nach dem Muster von Shapeshift (Recherche 03) die Intents der Risikoklassen R0 und R1. Alle anderen Intents werden dann über die Oberfläche angeboten.
>
> **E10.4 (Hierarchie).** Der Katalog ist ein Baum aus Gruppe, Intent und Slotfragen. Keine choice-Frage hat mehr als 19 Optionen. Unter der Gruppenschwelle werden zwei Gruppen parallel bewertet, und unzulässige Optionen werden vorab herausgefiltert.

### 10.2.4 Der Intent-Katalog

Der Katalog `spezifikation/intents.yaml` (Version 0.1.0) deckt alle Themen der Gliederung ab. Tabelle 10.5 zeigt die Gruppen mit ihren Intents.

**Tabelle 10.5: Intent-Katalog (Gruppen → Intents)**

| Gruppe | Intents | Beispiele für Intents | betroffene Kapitel |
|---|---:|---|---|
| grundriss | 10 | raum_groesse_aendern, raum_hinzufuegen, raeume_tauschen, raeume_zusammenlegen, innenwand_versetzen, innentuer_setzen | 9, 9b |
| geschosse_baukoerper | 10 | kniestock_aendern, geschosshoehe_aendern, keller_festlegen, dachgeschoss_ausbau, haus_verschieben, hoehenlage_aendern | 4.3, 9 |
| huelle | 10 | fenster_einfuegen, fenster_groesse_aendern, fenster_typ_aendern, terrassentuer_setzen, wandaufbau_waehlen, sonnenschutz_setzen | 8, 15 |
| dach | 10 | dachform_aendern, dachneigung_aendern, dachueberstand_aendern, gaube_hinzufuegen, dachfenster_einfuegen, dacheindeckung_waehlen | 14 |
| fassade | 6 | fassade_material_waehlen, schalung_art_waehlen, fassade_teilflaeche, sockel_gestalten | 14.7 |
| bemusterung_interior | 13 | bodenbelag_waehlen, fliese_waehlen, fliese_muster_fuge, wandoberflaeche_waehlen, treppe_bemustern, sanitaerobjekt_setzen, kueche_planen | 12 |
| tga | 10 | steckdose_setzen, netzwerk_setzen, heizsystem_waehlen, waermepumpe_aufstellen, lueftung_waehlen, wallbox_setzen | 13 |
| licht | 5 | leuchte_setzen, lichtschalter_setzen, lichtsteuerung_waehlen, aussenbeleuchtung_setzen | 13.7 |
| pv | 4 | pv_belegen, pv_modul_waehlen, batteriespeicher_waehlen | 14.6 |
| aussenanlagen | 9 | terrasse_anlegen, garage_carport_hinzufuegen, zisterne_hinzufuegen, versickerung_waehlen, rueckstausicherung_waehlen, gelaende_modellieren | 14a |
| moeblierung | 6 | moebel_platzieren, moebel_verschieben, raum_moeblieren, einbauschrank_planen | 12.3 |
| gebaeudetyp_nutzung | 8 | einliegerwohnung_hinzufuegen, wohnung_hinzufuegen, anbauart_aendern, barrierefreiheit_vorsehen, nutzerprofil_waehlen, kulturprofil_waehlen | 9a, 9b |
| steuerung | 12 | rueckgaengig, variante_anlegen, varianten_vergleichen, ansicht_wechseln, bestaetigen, alternative_waehlen | 7.3 |
| anzeigen_auswerten | 12 | kosten_anzeigen, energie_anzeigen, schall_anzeigen, masse_abfragen, begruendung_erfragen, regelstatus_anzeigen | 15, 9.5 |
| freigabe_prozess | 7 | zur_pruefung_senden, angebot_anfordern, bemusterung_abschliessen, abweichung_beantragen, freigabe_erklaeren | 18 |
| meta | 6 | hilfe, ki_transparenz, datenschutz_steuern, ausschluss_thema, ausserhalb_umfang, unklar | 4.8, 9b.6 |
| **Summe** | **138** | | |

Jeder Intent trägt die Felder, die die App zur Laufzeit braucht:

- Beschreibung und Risikoklasse R0–R3 (10.2.5)
- mindestens drei deutsche Beispielsätze, insgesamt 415
- Slots mit Typ, Einheit, Wertebereich, Pflichtkennzeichen und Quelle (`parser`, `referenz`, `katalog` oder `modell`), insgesamt 316
- die Fragen an das Intent-Modell mit Schwellwert
- die betroffenen Regeln als IDs aus `regelkatalog.yaml` und `empfehlungen.yaml`, dazu die noch zu formalisierenden Regeln als `regeln_geplant`
- die betroffenen Module
- der Rückfragetext

Zwei Gestaltungsregeln des Katalogs folgen aus früheren Kapiteln.

**Der Gebäudetyp wird nicht gewählt.** Kapitel 9a hat gezeigt, dass ein gewähltes Etikett „Haustyp“ veralten würde, weil Gebäudeklasse und Profil aus Merkmalen folgen, die der Kunde im Entwurf ändert (Abschnitt 9a.2.1). Die Gruppe `gebaeudetyp_nutzung` enthält deshalb keinen Intent „Typ wählen“. Sie enthält Intents, die Merkmale ändern: eine Einliegerwohnung anlegen, eine weitere Wohnung anlegen, die Anbauart ändern. Das Regelprofil ermittelt anschließend die Profilableitung aus dem geänderten Merkmalsvektor. Diese Intents haben mindestens die Risikoklasse R2, weil sie Gebäudeklasse, Schallschutz und Bauvorlageberechtigung verschieben können; das Zurücknehmen einer Wohnung ist R3.

**Freigaben gehen nicht per Sprache.** Die Gruppe `freigabe_prozess` stößt Prozessschritte nur an. Der Intent `freigabe_erklaeren` erkennt den Versuch, per Sprache eine rechtserhebliche Erklärung abzugeben, etwa „Ich gebe den Bauantrag frei“ oder „Hiermit bestelle ich das Haus verbindlich“. Er führt sie aber nie aus, sondern verweist auf das Freigabe-Gate der Oberfläche (E10.9).

> **Beispiel 10.1 (Katalogeintrag `kniestock_aendern`).** Gruppe `geschosse_baukoerper`, Risikoklasse R2.
>
> - **Slots:** `wert` (Länge, m, Wertebereich 0,0–2,5), `modus` (absolut, relativ_plus, relativ_minus; Quelle Parser), `staerke` (Stufe 1–5, nur ohne Zahlwert).
> - **Fragen:** `n.relativ` (noul, Schwelle 0,70; nur wenn der Parser keinen Modus erkennt) und `s.staerke` (score, fünf Stufen, Schwelle 0,60).
> - **Regeln:** `BY.BayBO.2-5.aF2007.Vollgeschoss`, `BY.BayBO.6.T`, `BY.BayBO.2-3.Gebaeudeklasse`, `BY.Profil.Schwellenwarnung`.
> - **Rückfrage:** „Auf welche Höhe soll der Kniestock? Ab {k_stern} wird das Dachgeschoss zum Vollgeschoss.“
>
> Der Platzhalter {k_stern} ist die Vollgeschoss-Schwelle aus Beispiel 4.2. Das System meldet sie vor der Ausführung (ANF-09-19). Der Kunde erfährt also nicht erst nach der Änderung, dass sein Haus ein Geschoss zu viel hat. Er erfährt es in der Vorschau, die die Risikoklasse R2 ohnehin verlangt.

### 10.2.5 Kalibrierung und Schwellwerte

Ein Schwellwert ist nur so gut wie die Wahrscheinlichkeit, auf die er angewendet wird. Laya wird laut Model Card **unkalibriert** ausgeliefert. Ohne Fine-Tuning liegt die Genauigkeit bei 0,342, das Zufallsniveau wäre 0,318 (Recherche 03) [V]. Eine Ausgabe „p = 0,9“ bedeutet vor der Kalibrierung also nicht, dass das Modell in neun von zehn Fällen richtig liegt.

**Kalibrierungsfehler.** Gemessen wird der erwartete Kalibrierungsfehler (ECE). Die Vorhersagen werden nach ihrer Konfidenz in *B* = 15 gleich breite Intervalle $B_b$ geteilt, und je Intervall wird die mittlere Konfidenz mit der beobachteten Trefferquote verglichen:

$$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|B_b|}{n}\,\bigl|\,\mathrm{acc}(B_b) - \mathrm{conf}(B_b)\,\bigr|$$

Die Definition ist ein Standardmaß der Kalibrierungsforschung. Ein Literaturnachweis dafür fehlt im Bestand und ist nachzutragen [U].

**Temperaturskalierung.** Kalibriert wird je Fragetyp mit einer Temperatur *T*, die auf dem Entwicklungsset die negative Log-Likelihood minimiert: $\hat p_i = p_i^{1/T} / \sum_j p_j^{1/T}$. Das Verfahren braucht nur die Wahrscheinlichkeiten, nicht die internen Logits, und funktioniert damit auch mit dem Jev-Protokoll. Für noul-Fragen wird dieselbe Transformation auf das Paar (p, 1 − p) angewendet. *T* ist Teil der Modellversion und steht im Protokoll jeder Äußerung.

**Entscheidungsregel.** Für einen Intent der Risikoklasse *k* mit bester kalibrierter Wahrscheinlichkeit $\hat p_1$ und zweitbester $\hat p_2$ gilt:

$$\text{ausführen} \iff \hat p_1 \ge \tau_k \;\wedge\; \hat p_1 - \hat p_2 \ge \delta_k$$

Sonst folgt eine Rückfrage. Die Werte $\tau_k$ und $\delta_k$ stehen in Tabelle 10.6. B6 verwendet für alle Intents $\tau$ = 0,70 und $\delta$ = 0,20. Das entspricht der Klasse R1.

**Tabelle 10.6: Risikoklassen und Startschwellen (`intents.yaml`, Abschnitt `risikoklassen`)**

| Klasse | Bedeutung | $\tau_k$ | $\delta_k$ | Bestätigung | Intents |
|---|---|---:|---:|---|---:|
| R0 | Auskunft, Ansicht, Dialog; ändert das Modell nicht | 0,55 | 0,15 | keine | 29 |
| R1 | reversible Änderung mit lokaler Wirkung | 0,70 | 0,20 | keine; Interpretationsanzeige und Undo | 75 |
| R2 | Folgen für Profil, Gebäudeklasse, Kosten über einer Schwelle oder mehrere Gewerke | 0,80 | 0,25 | Vorschau mit Folgen, Bestätigung per Sprache oder Klick | 27 |
| R3 | schwer umkehrbar oder rechtserheblich (Löschen, Senden, Abschließen) | 0,90 | 0,30 | ausdrücklich auf dem Bildschirm; Sprache genügt nie | 7 |

Die Staffelung folgt dem Grundsatz aus Recherche 03, die Schwelle nach den Fehlerkosten zu wählen. Ein Fehler in R1 kostet einen Undo-Schritt, in R2 eine falsch verstandene Kostenfolge, in R3 unter Umständen eine verlorene Variante oder eine Erklärung gegenüber der Firma. Die Startwerte sind Designentscheidungen [U]. Sie werden nach der Kalibrierung so gesetzt, dass die Fehlausführungsrate am Entwicklungsset die Zielwerte aus Tabelle 10.10 einhält. Das ist ein Verfahren der selektiven Vorhersage: Die Rückfrage ist die Enthaltung, und berichtet wird das Paar aus Abdeckung und Fehlerrate.

> **E10.5 (Schwellen).** Schwellen gelten nur für kalibrierte Wahrscheinlichkeiten und je Risikoklasse. Sie sind Konfiguration mit Version, nicht Code. Jede Änderung einer Schwelle oder einer Temperatur erzeugt eine neue Katalog- bzw. Modellversion im Protokoll.

## 10.3 Deterministischer Werteparser und Referenzauflösung

### 10.3.1 Warum ein eigener Parser

Laut Recherche 03 beantworten Jev und Laya typisierte Fragen, liefern aber keine Werte wie „1,20 m“ oder „35 Grad“ [V]. Die Recherche nennt zwei Wege, die Werte zu gewinnen: einen deutschen Parser für Zahlen und Einheiten oder ein Sprachmodell mit JSON-Schema bzw. Constrained Decoding. Kakadoo geht einen Mittelweg und parst strukturierte Befehle wie „Set the Height to 12“ deterministisch. Das Sprachmodell kommt dort nur bei unscharfen Angaben wie „höher“ zum Zug [@atakan2025kakadoo]. Die Arbeit geht einen Schritt weiter.

> **E10.6 (Werte).** Zahlwerte, Einheiten, Richtungen und Ordinale entstehen im Betrieb ausschließlich im deterministischen Werteparser. Ein Sprachmodell mit JSON-Schema wird nicht zur Wertgewinnung eingesetzt. Offline darf es Paraphrasen für Trainingsdaten erzeugen, die ein Mensch prüft (10.5.4). Unscharfe Angaben ohne Zahl ergeben eine Stufe der score-Frage und eine Vorschau, nie einen stillschweigend gesetzten Wert.

Die Begründung ist die des ganzen Kapitels: Ein Wert, der in das Modell und damit in Nachweis und Vertrag eingeht, muss sich auf eine Regel zurückführen lassen. Der Parser ist eine Funktion ohne Zustand und Zufall. Der Test `test_pipeline_deterministisch` bestätigt, dass zweimaliges Verarbeiten der neun B6-Sätze identische Protokolle ergibt.

### 10.3.2 Grammatik

Die Datei `spezifikation/werteparser-grammatik.md` beschreibt die Sprache des Parsers in EBNF nach ISO/IEC 14977 auf zwei Ebenen. Die **Wortebene** kennt fünf Muster für Maßausdrücke, geordnet nach Priorität:

- **A:** Zahl, „Meter“, Zahl unter 100: „zwei Meter sechzig“ = 2,60 m, „ein Meter fünf“ = 1,05 m
- **B:** Zahl mit Einheit: „1,20 m“, „35 Grad“, „zwölf Quadratmeter“
- **C:** umgangssprachliches Maß: „eins zwanzig“ = 1,20 m, erweitert um „eins null fünf“ und die Zusammenschreibung „einsachtzig“
- **F:** Produkt: „vier mal sechs Meter“
- **D:** Zahl ohne Einheit

Hinzu kommen Modus-, Richtungs-, Ordinal- und Anzahlausdrücke. Die **Morphemebene** zerlegt Zahlwörter wie „fünfunddreißig“ oder „zweihundertzwanzig“ innerhalb eines Wortes und erweitert den Bereich von B6 (bis 999) auf Tausender. Vierzehn Disambiguierungsregeln D1–D14 legen fest, wie Mehrdeutigkeiten entschieden werden. Die wichtigsten sind:

- **D1 Tausenderpunkt:** Ein Punkt mit genau drei Ziffern danach trennt Tausender, sonst ist er Dezimaltrenner. „2.500 mm“ = 2,50 m, „1.20m“ = 1,20 m.
- **D3 Mehrdeutiges Umgangsmaß:** „eins fünf“ hat die Kandidaten 1,05 m und 1,50 m. Liegt nur ein Kandidat im Wertebereich des Slots, gilt er, sonst folgt eine Rückfrage.
- **D4 Einheit aus dem Slot:** „Dachneigung auf fünfunddreißig“ ergibt 35°, weil der Slot die Einheit Grad hat. Die ergänzte Einheit wird in der Interpretationsanzeige ausgewiesen.
- **D5 Nummer gehört zur Referenz:** In „Kinderzimmer 2 auf 3,20 m“ gehört die 2 zum Raum, nicht zum Wert.
- **D9 Komparativ macht relativ:** „zwanzig Zentimeter schmaler“ ergibt −0,20 m relativ. Bei Widerspruch gewinnt der Komparativ, und die Anzeige zeigt beide Lesarten.

Jeder Messwert trägt seine Herkunft: Textausschnitt, Muster, Herkunft der Einheit (Text, Slot oder Konvention), Mehrdeutigkeit und Kandidaten. Die Dimensionen umfassen Länge, Fläche, Winkel, Anteil, Leistung, Energie, Volumen, Farbtemperatur, U-Wert und Anzahl. B6 kennt davon die ersten drei.

### 10.3.3 Was B6 kann: neun Sätze, 16 Parserfälle

Die Testdatei `tests/test_b6_b7.py` enthält 23 Tests, darunter 16 parametrisierte Parserfälle, einen Test für mehrdeutige Maße und Zahlwörter, Tests für Raumreferenzen, Annahme mit Ausgleich, Ablehnung, Flächenangabe mit Rückfragen und Determinismus (`beispiele/ergebnisse.md`). Im Lauf vom 27.09.2026 in der Arbeitsumgebung dieses Kapitels bestanden 22 Tests. Einer wurde übersprungen, weil `compas_timber` für den BTLx-Test (B7) nicht installiert war. Beispiel 10.2 zeigt das Ergebnis der neun Beispielsätze.

> **Beispiel 10.2 (B6, `ausgabe/intent_protokoll.json`).** Referenzzustand `daten/haus_state.json`: Innenbreite 9,40 m, Raster 5 cm, Projektregeln Mindestbreite Bad 1,70 m, Kinderzimmer 2,60 m und 10,00 m². Die Intent-Wahrscheinlichkeiten sind Stub-Werte.
>
> | Äußerung | Intent (p, Stub) | Maß (Muster) | Ergebnis |
> |---|---|---|---|
> | Mach das Bad oben zwei Meter sechzig breit | raum_aendern 0,91 | 2,60 m (A) | angenommen: Bad 2,40 → 2,60 m; Kinderzimmer 1 3,50 → 3,30 m |
> | Das Bad oben bitte eins zwanzig breit | raum_aendern 0,91 | 1,20 m (C) | abgelehnt: 1,20 m < Mindestbreite 1,70 m |
> | Das Bad soll zwanzig Zentimeter breiter werden | raum_aendern 0,91 | 0,20 m (B) | Rückfrage: Raumreferenz mehrdeutig (2 Bäder) |
> | Mach das Kinderzimmer 2 auf 3,20 m | raum_aendern 0,78 | 3,20 m (B) | angenommen: Kinderzimmer 2 3,50 → 3,20 m; Kinderzimmer 1 3,50 → 3,80 m |
> | Das zweite Kinderzimmer soll zwölf Quadratmeter haben | raum_aendern 0,91 | 12 m² (B) | angenommen: Kinderzimmer 2 3,50 → 3,55 m (12,07 m² bei 3,40 m Tiefe); Kinderzimmer 1 3,50 → 3,45 m |
> | Mach das Kinderzimmer 1 einen Meter zwanzig schmaler | raum_aendern 0,91 | 1,20 m (A) | abgelehnt: 2,30 m < 2,60 m; 7,82 m² < 10,00 m² |
> | Das Bad oben eins fünf breiter | raum_aendern 0,91 | 1,05 m (C, mehrdeutig) | Rückfrage: 1,05 m oder 1,50 m? |
> | Stell die Dachneigung auf 35 Grad | dach_aendern 0,88 | 35° (B) | nicht umgesetzt (im Prototyp nur raum_aendern) |
> | Kannst du das mal anders machen | sonstiges 0,46 | – | Rückfrage: Intent unsicher (p = 0,46, Abstand 0,15) |
>
> Die Raumreferenz „das Bad oben“ wird zur IfcSpace-GlobalId `1cRQfmv29HlfHiIPofgLWT` aufgelöst. Die Summe der Breiten der Zeile OG-Nord bleibt 9,40 m, das Außenmaß ist unverändert (Test `test_intent_angenommen_mit_ausgleich`).

Das Beispiel belegt die Arbeitsteilung aus Tabelle 10.3 am lauffähigen Code. Von neun Äußerungen werden drei angenommen, zwei nach Regeln abgelehnt und drei zurückgefragt, eine ist nicht umgesetzt. Die Rückfragen haben drei verschiedene Ursachen: eine unsichere Absicht, einen mehrdeutigen Wert und eine mehrdeutige Referenz. Keine davon hätte ein Sprachmodell mit gleicher Sicherheit auflösen können, alle lassen sich mit einer geschlossenen Frage an den Kunden klären.

Beispiel 10.2 zeigt aber auch eine **implizite Annahme** des Prototyps. Bei „Mach das Kinderzimmer 2 auf 3,20 m“ setzt B6 stillschweigend die Breite. Der Satz nennt aber weder Breite noch Tiefe, und das Kinderzimmer misst 3,50 × 3,40 m. Chen et al. lassen fehlende Angaben nach „gesundem Menschenverstand“ ergänzen. Kapitel 5 hat das als offene Annahme kritisiert (Abschnitt 5.6.4) [@chen2025agent], und B6 tut an dieser Stelle dasselbe. Das Testset erwartet deshalb für diesen Satz eine Rückfrage „Breite oder Tiefe?“ (Testfall T004, ANF-10-14). Eine Voreinstellung ist nur dort zulässig, wo der Katalog sie ausdrücklich festlegt: `geschosshoehe_aendern` versteht „höher“ als lichte Höhe (`standard: lichte_hoehe`), und die Interpretationsanzeige weist das aus.

### 10.3.4 Was B6 nicht kann: Messung am Testset

Das Testset enthält 76 Zahlslots, deren Wert im Satz steht. Die Funktion `parse_masse` aus B6 wurde am 27.09.2026 auf alle Sätze angewendet (`spezifikation/pruefe_sprache.py`). Gezählt wurde ein Slot als richtig, wenn ein erkannter Messwert der richtigen Dimension genau den erwarteten Wert hat bzw. ein mehrdeutiger Wert als mehrdeutig markiert ist. Tabelle 10.7 zeigt das Ergebnis.

**Tabelle 10.7: B6-Werteparser am Testset (Messung 27.09.2026)**

| Teilmenge | richtig | Ursache der Fehler | Regel der Grammatik |
|---|---:|---|---|
| alle Zahlslots | 47 von 76 | – | – |
| Dimensionen, die B6 kennt (m, m², °) | 46 von 54, dazu 1 von 1 mehrdeutig markiert | siehe folgende Zeilen | – |
| Zusammenschreibung („einsachtzig“, „einsfünfzig“) | 0 von 2 | Wort nicht als Zahl erkannt | 3.2 `kompositum_mass` |
| Tausenderpunkt („2.500 mm“) | 0 von 1 | als 2,5 mm gelesen, Ergebnis 0,0025 m | D1 |
| Einheit fehlt („Dachneigung auf fünfunddreißig“) | 0 von 2 | Zahl ohne Dimension | D4 |
| Dialekt („an Meter“) | 0 von 1 | Artikel nicht erkannt | D8 |
| Produkt („vier mal sechs Meter“) | 2 von 4 | erster Faktor ohne Einheit | D7 |
| andere Dimensionen (Anzahl, %, kW, kWp, kWh, l, m³, K, U-Wert, Format) | 0 von 21 | nicht implementiert | 3.3 |

Innerhalb seines Geltungsbereichs liest B6 also 46 von 54 Werten richtig. Über das gesamte Testset sind es 47 von 76. Die Fehler sind keine Zufallsfehler, sondern fehlende Regeln, und jede ist in der Grammatik benannt. Zwei Fehler sind gefährlicher als die übrigen:

- **Tausenderpunkt.** „Die Terrassentür im Wohnzimmer 2.500 mm breit“ ergibt in B6 einen gültigen Messwert von 0,0025 m. Das ist ein stiller Fehler: Der Wert hat die richtige Dimension und würde nur an der Plausibilitätsprüfung scheitern, die B6 für Türbreiten nicht hat. Die Sondierung mit „1.250 mm“ ergab ebenso 0,0013 m. Regel D1 und die Wertebereichsprüfung D13 schließen diesen Fehler aus (ANF-10-11).
- **Einheit fehlt.** „Mach die Dachneigung auf fünfunddreißig“ ist eine natürliche Äußerung. Ohne D4 fehlt der Wert, und das System müsste nachfragen, obwohl die Absicht klar ist.

Dass B6 für „eins fünf“ die Mehrdeutigkeit erkennt, obwohl es nur den ersten Kandidaten 1,05 m ausgibt, ist dagegen richtig gelöst. Die Grammatik ergänzt nur die Kandidatenliste, damit die Rückfrage beide Werte nennen kann.

### 10.3.5 Referenzauflösung über das State-JSON

„Das Bad oben“ ist kein Wert, sondern ein Verweis auf ein Objekt im Modell. B6 löst solche Verweise gegen ein kompaktes State-JSON auf. Es enthält je Raum GlobalId, Typ, Name, Geschoss, Zeile und Maße. Die GlobalIds sind deterministisch aus einem UUID-5 über den Pfad `/haus/raeume/<id>` erzeugt, mit demselben Verfahren wie in B1 (Abschnitt 8.6.2). Die Auflösung filtert die Kandidaten schrittweise:

1. **Raumtyp** über eine Synonymtabelle: „Bad“, „Badezimmer“, „Duschbad“ und „Dusche“ ergeben den Typ Bad.
2. **Geschoss** über Lagewörter: „oben“ ist das höchste Geschoss, in dem ein Kandidat liegt, „unten“ das niedrigste, „OG“ und „EG“ sind explizit.
3. **Nummer oder Ordinal**: „Kinderzimmer 2“, „das zweite Kinderzimmer“.
4. **Größenattribut**: „das größere“, „das kleine“.

Bleibt genau ein Kandidat, ist das Ergebnis dessen GlobalId. Bleiben mehrere, lautet das Ergebnis „mehrdeutig“ mit Kandidatenliste, bleibt keiner, „keine“. Im Testset löst B6 55 von 58 Raumslots richtig auf. Die Kontextfälle sind dabei ausgenommen. Die drei Fehler zeigen zwei fehlende Kriterien:

- **Name vor Typ.** „Die Diele“ und „In der Diele“ ergeben „mehrdeutig“, weil „Diele“ als Synonym des Typs Flur geführt wird und es zwei Flure gibt. Der Raum im Erdgeschoss heißt aber „Diele“. Die Auflösung muss einen exakten Namensvergleich vor den Typvergleich stellen.
- **Mengen.** „In jedes Kinderzimmer zwei Netzwerkdosen“ meint beide Kinderzimmer. Ein Quantor wie „jedes“ oder „alle“ macht aus der Mehrdeutigkeit eine Menge, auf die die Aktion für jedes Element angewendet wird.

Zwei weitere Kriterien verlangt das Testset über B6 hinaus:

- **Dialogkontext:** „Mach es zwanzig Zentimeter breiter“ nach „Wie breit ist das Bad oben?“. Die noul-Frage `n.bezug_vorher` entscheidet, ob der Verweis im Kontext aufgelöst wird. Welches Objekt gemeint ist, entscheidet dann der Code aus dem Dialogprotokoll.
- **Relationen:** „die Wand zwischen Bad und Kinderzimmer 1“ wird über die Raumbegrenzungen im Modell aufgelöst (`IfcRelSpaceBoundary`, Kapitel 8).

Katalogartikel wie Fliesen, Farben oder Möbel werden analog über eine deterministische unscharfe Suche in der Projektbibliothek gefunden (Kapitel 12). Auch dort gilt: Mehr als ein Treffer führt zur Rückfrage mit höchstens fünf Kandidaten.

> **E10.7 (Referenzen).** Referenzen werden ausschließlich deterministisch gegen den Modellzustand aufgelöst. Die Kriterien sind in dieser Reihenfolge: exakter Name, Typ, Geschoss, Nummer oder Ordinal, Größe, Relation, Dialogkontext. Bei Mehrdeutigkeit fragt das System mit den Kandidaten zurück und wählt nie den „wahrscheinlichsten“ Raum. Quantoren erzeugen Mengen. Das Ergebnis ist immer eine GlobalId oder eine Liste von GlobalIds, nie ein Name.

## 10.4 Dialogsteuerung, Fehlerbehandlung und Transparenz

### 10.4.1 Zustände einer Äußerung

Jede Äußerung endet in genau einem von acht Ergebnissen. Tabelle 10.8 zeigt sie mit ihren Auslösern. Die Häufigkeiten stammen aus der Spalte `erwartet` des Testsets.

**Tabelle 10.8: Ergebnisse einer Äußerung**

| Ergebnis | Auslöser | Reaktion | Testset |
|---|---|---|---:|
| ausführen | R1, alle Schwellen erfüllt, Slots vollständig, Regeln erfüllt | Änderung, Interpretationsanzeige, Undo | 116 |
| Vorschau mit Bestätigung | R2 oder unscharfe Stärke | Vorschau mit Folgen (Kosten, Profil, Regeln), Bestätigung per Sprache oder Klick | 46 |
| Bestätigung am Bildschirm | R3 | Dialog am Bildschirm; Sprache allein genügt nicht | 6 |
| Auskunft | R0 | Anzeige, keine Änderung | 32 |
| Rückfrage | Intent unter Schwelle; Slot fehlt; Wert oder Referenz mehrdeutig | geschlossene Frage mit Optionen | 8 |
| Ablehnung nach Regel | Wunsch außerhalb des Lösungsraums | Begründung, Werte, Quelle, Alternative (Kapitel 9.5) | 4 |
| Verweis auf die Oberfläche | rechtserhebliche Erklärung | Freigabeseite öffnen | 2 |
| Abweisung | Ausschlussthema oder außerhalb des Umfangs | fester Katalogtext | 2 |

Die Reihenfolge der Prüfungen ist fest. Zuerst kommen die Intent-Schwellen, dann die Vollständigkeit und Eindeutigkeit der Slots und Referenzen, dann die Regeln. Eine Regel wird also nie gegen eine unsichere Absicht geprüft. Damit hat eine Ablehnung immer eine eindeutig verstandene Absicht zum Gegenstand.

### 10.4.2 Rückfrage ist nicht Ablehnung

Kapitel 9 hat verlangt, Rückfragen zur Absicht von Ablehnungen nach Regeln zu trennen (Abschnitt 9.5.3, ANF-09-15). Die Oberfläche macht den Unterschied sichtbar:

- **Die Rückfrage** ist eine Frage des Systems an sich selbst, die der Kunde beantwortet. Sie hat keine Regel, keinen Nachweis und keinen roten Status. Ihr Text steht im Feld `rueckfrage` des Intents mit Platzhaltern für Kandidaten, zum Beispiel „Welchen Raum meinen Sie: Duschbad EG oder Bad OG?“.
- **Die Ablehnung** ist eine Aussage über den Entwurf. Sie nennt nach Abschnitt 9.5.1 die Konfliktmenge, die Begründung mit Werten und Quelle und mindestens eine Alternative. Sie erzeugt einen Nachweis mit rotem Status (ANF-09-16).

Für die Alternative gilt die gemeinsame Projektion auf alle Regeln. Beim Satz „Mach das Kinderzimmer 1 einen Meter zwanzig schmaler“ ist nicht die zuerst gemeldete Mindestbreite bindend, sondern die Mindestfläche. Die richtige Alternative lautet deshalb „höchstens 0,55 m schmaler (2,95 m; 10,03 m²)“ (Abschnitt 9.5.3, ANF-09-13). Sie wird im Dialog als Option angeboten und lässt sich mit dem Intent `alternative_waehlen` („Dann nimm das“) übernehmen.

Die Texte von Rückfrage, Ablehnung und Auskunft stammen aus dem Katalog, nicht von einem Sprachmodell. In einem Experiment mit 1.506 Teilnehmenden verschob ein meinungsgeprägter Schreibassistent nicht nur die Texte, sondern auch die später erhobene Einstellung [@jakesch2023cowriting]. Kapitel 9b hat daraus abgeleitet, dass kein Meldungstext zur Laufzeit von einem Sprachmodell erzeugt wird (ANF-09b-09). Erklärungen folgen den dort beschriebenen Grundsätzen: kontrastiv, selektiv, höchstens drei Gründe [@miller2019explanation]. Eine Nutzerstudie zu Erklärungen fand außerdem, dass Vollständigkeit wichtiger ist als Genauigkeit und dass starke Vereinfachung Vertrauen kostet [@kulesza2013explanations]. Für die Ablehnung heißt das, dass sie alle verletzten Regeln der Konfliktmenge nennt, nicht nur die erste.

> **E10.8 (Dialog).** Rückfrage und Ablehnung sind getrennte Ergebnisse mit getrennter Darstellung. Eine Rückfrage ist immer eine geschlossene Frage mit höchstens fünf Optionen. Nach zwei erfolglosen Rückfragen in Folge wechselt das System zur Auswahl am Bildschirm, etwa zum Antippen des gemeinten Raums. Alle Texte kommen aus dem Katalog.

### 10.4.3 Fehlertoleranz

Keine Sprachschnittstelle ist fehlerfrei. Entscheidend ist, dass Fehler sichtbar, billig und umkehrbar sind. Das System setzt fünf Mechanismen ein:

1. **Interpretationsanzeige.** Vor bzw. mit jeder Ausführung zeigt die App, was sie verstanden hat, in der Form „Bad (OG) · Breite · 2,60 m (absolut)“. Ergänzte Einheiten und Voreinstellungen sind markiert. Die Anzeige ist zugleich das wichtigste Transparenzmittel (10.4.4).
2. **Undo als Sprachbefehl.** „Mach das rückgängig“, „Nimm das zurück“ und „Nein, das war besser vorher“ gehören zum Intent `rueckgaengig` der Klasse R1. Weil jede R1-Änderung mit einem Schritt umkehrbar ist, kann ihre Schwelle niedriger liegen als die von R2.
3. **Korrektur im Satz.** „Nein, nicht das Bad, das Kinderzimmer 1“ und „Ach nein, lieber achtundzwanzig“ werden über `n.korrektur` als Ersetzung eines Slots im vorigen Frame behandelt. Das Testset enthält drei Korrektur- und drei Anapherfälle.
4. **n-beste Hypothesen mit Kontextfilter.** Wie in 10.1.2 beschrieben, wird eine im Kontext unzulässige Hypothese durch die nächste ersetzt, bevor das System nachfragt [@kou2010knowledge].
5. **Automatische Variante vor R3.** Vor dem Löschen eines Geschosses oder einer Wohnung legt das System eine Variante an. Der Rückweg bleibt auch dann offen, wenn der Undo-Stapel verworfen wird.

Ein Mechanismus wird bewusst **nicht** eingesetzt: die Bestätigung jeder Änderung per Klick. Sie würde die Sprache für R1-Änderungen entwerten. Außerdem zeigt die Forschung zu Automation Bias, dass Bestätigungen unter Last zur Routine werden. Complacency und Automation Bias treten bei Laien und Experten auf und lassen sich durch Übung oder Anweisung nicht beseitigen [@parasuraman2010complacency]. Eine Bestätigung ist deshalb nur dort vorgesehen, wo sie einen Inhalt hat, nämlich die Vorschau der Folgen in R2. Bei R3 ist sie keine Bestätigung im Dialogfluss, sondern ein eigener Bildschirmschritt.

> **E10.9 (Rechtserhebliche Erklärungen).** Freigaben, Unterschriften, Bestellungen und der Abschluss einer Bemusterungskategorie werden nie per Sprache ausgeführt. Die Sprache kann den Schritt anstoßen, erklärt wird er am Bildschirm mit dem Freigabe-Gate aus Kapitel 18.

### 10.4.4 Transparenz nach Art. 50 KI-VO

Gebäudeentwurf gehört nicht zu den Hochrisiko-Anwendungen der KI-Verordnung (Kapitel 4.8.2) [@aiact2024]. Recherche 27 hat das auch für den Produktweg über Anhang I bestätigt. Es bleiben zwei Pflichten: die Transparenzpflicht nach Art. 50 und die durch die Omnibus-Verordnung abgeschwächte Pflicht zu Maßnahmen der KI-Kompetenz nach Art. 4 [@eu2026omnibus]. Art. 50 Abs. 1 verlangt, dass Nutzer erkennen können, dass sie mit einem KI-System interagieren. Die Umsetzung hat drei Teile:

- **Hinweis bei der ersten Aktivierung des Mikrofons** mit festem Katalogtext: „Ihre Sprache wird von einer KI verstanden. Die KI erkennt nur, was Sie ändern möchten. Maße, Regeln, Kosten und Nachweise berechnet ein festes Programm. Sie sehen vor jeder Änderung, was verstanden wurde.“
- **Dauerhaftes Symbol** während der Spracheingabe, dazu die Interpretationsanzeige (10.4.3).
- **Auskunft auf Nachfrage** über den Intent `ki_transparenz` („Rede ich hier mit einem Computer?“, „Wer entscheidet hier eigentlich?“), ebenfalls mit festem Text.

Art. 50 Abs. 2 verlangt die maschinenlesbare Kennzeichnung synthetisch erzeugter Audio- und Textinhalte. Für Altsysteme gilt er nach der Omnibus-Verordnung ab dem 02.12.2026 [@eu2026omnibus]. Die App erzeugt keine Texte mit einem Sprachmodell. Ob das Vorlesen fester Katalogtexte durch eine Sprachsynthese als Erzeugung synthetischer Audioinhalte gilt, ist ungeklärt [U]. Bis zur Klärung wird eine Sprachausgabe, falls sie angeboten wird, maschinenlesbar gekennzeichnet (ANF-10-22).

Die Transparenz hat neben der rechtlichen eine funktionale Seite. Die Interpretationsanzeige macht den Fehler des Modells sichtbar, bevor er zum Fehler im Modell wird. Rechtliche Pflicht und Fehlertoleranz fallen hier zusammen.

> **E10.10 (Interpretationsanzeige).** Jede ausgeführte oder vorgeschaute Änderung zeigt den verstandenen Frame in Klartext. Ergänzte Einheiten und Voreinstellungen sind gekennzeichnet.

### 10.4.5 Datenschutz

Sprachaufnahmen sind personenbezogene Daten (Kapitel 4.8.3). Die Leitlinien des EDPB zu Sprachassistenten verlangen, die Speicherung zu begrenzen und versehentliche Aufnahmen zu löschen. Stimmdaten sind danach nur dann biometrisch, wenn sie zur Identifizierung verarbeitet werden [@edpb2021vva]. Für den Zugriff auf das Mikrofon gilt § 25 TDDDG. Die Einwilligung ist entbehrlich, wenn der Zugriff für den angefragten Dienst unbedingt erforderlich ist [@tdddg25]. Die DSK verlangt datenschutzfreundliche Voreinstellungen, kein Training mit Eingaben ohne Grundlage und keine automatisierte Letztentscheidung [@dsk2024ki]. Daraus folgt:

> **E10.11 (Datenschutz).** Spracherkennung und Intent-Modell laufen lokal. Rohaudio wird nicht über die Sitzung hinaus gespeichert. Das Protokoll enthält nur Transkript, Hypothesen und Frame. Es gibt keine Sprechererkennung, damit entstehen keine biometrischen Daten. Aufnahmen werden nur mit gesonderter Einwilligung für Training und Evaluation verwendet. Jev als Cloud-Rückfallebene erhält nur Transkripte, nie Audio, mit Zero Data Retention und nur nach Einwilligung. Beratungsgespräche mit dem Vertrieb werden nur mit Einwilligung aller Beteiligten aufgezeichnet [@stgb201].

Die DSK-Forderung nach einer menschlichen Letztentscheidung trifft auch die Ablehnung. Nach dem SCHUFA-Urteil kann eine automatisierte Bewertung schon dann eine Entscheidung im Sinne von Art. 22 DSGVO sein, wenn ein Vertragsschluss maßgeblich von ihr abhängt [@eugh2023schufa]. Die Sprachschnittstelle bietet deshalb zu jeder Ablehnung den Intent `abweichung_beantragen` an („Das hätten wir gern als Abweichung geprüft“). Er merkt den Wunsch zur menschlichen Prüfung vor und öffnet den Anfechtungsweg aus Recherche 27. Über eine Abweichung entscheidet dann die Behörde bzw. die Firma, nicht die App.

Barrierefreiheit ist die Kehrseite. Die Sprachsteuerung kann Menschen mit motorischen Einschränkungen helfen, schließt aber Menschen mit Sprech- oder Hörbeeinträchtigung aus, wenn sie der einzige Weg ist. Elghaish et al. bauten ihren Sprachassistenten für BIM ausdrücklich auch für Nutzer mit Behinderung [@elghaish2022voice]. Fällt die App unter das Barrierefreiheitsstärkungsgesetz (Kapitel 4.8.3) [@bfsg], muss jede Funktion auch ohne Sprache erreichbar sein (ANF-10-25).

## 10.5 Evaluationsdesign

### 10.5.1 Testset

Die NL-BIM-Datensätze sind englisch, und die Arbeiten evaluieren überwiegend mit Fachleuten (Lücken L7, L8). IFC-Bench ist der einzige offene Datensatz mit Referenz-IFCs, deckt aber nur Abfragen ab [@hellin2026bim]. Das Review von Park et al. findet über 61 BIM-LLM-Studien eine industrielle Validierung in nur 44,3 % der Fälle [@park2026bimllm]. Die Arbeit baut deshalb ein eigenes deutsches Testset, `spezifikation/sprach-testset.jsonl`. Es umfasst 216 Sätze und deckt alle 138 Intents und alle 16 Gruppen ab. Jeder Eintrag enthält:

- Satz, erwartete Gruppe, erwarteten Intent und erwartete Slots mit Werten in SI-Einheiten
- für Raumslots die erwartete `raum_id` im Referenzzustand `beispiele/daten/haus_state.json` oder die erwartete Mehrdeutigkeit
- das erwartete Ergebnis nach Tabelle 10.8 und die Risikoklasse
- Kategorien für die Auswertung nach Teilmengen, gegebenenfalls einen Dialogkontext

Die Kategorien stehen für die Schwierigkeiten, die in den Abschnitten 10.1 bis 10.4 beschrieben sind: 40 Sätze mit Fachbegriffen, 22 mit Zahlwörtern, 18 Abfragen, 9 vage Angaben, je 3 Sätze mit Dialekt, Erkennungsartefakten, Korrekturen und Anaphern, 4 mit mehrdeutiger Referenz, dazu die 9 B6-Sätze. Die Sätze des Testsets sind nicht die Beispielsätze des Katalogs. Der Validator prüft das und meldet eine Überschneidung als Fehler. Bei der ersten Prüfung fand er 42 solche Leckagen. Sie wurden durch Umformulierung der Beispielsätze beseitigt.

Das Testset ist ein Textset. Es prüft Intent-Erkennung, Werteparser, Referenzauflösung und Dialogentscheidung unter der Annahme eines korrekten Transkripts. Für die Spracherkennung wird es zum Audio-Testset erweitert (10.5.2).

### 10.5.2 Messgrößen

Tabelle 10.9 fasst die Messgrößen zusammen. Die Zielwerte in Tabelle 10.10 sind Designentscheidungen [U]. Sie werden vor der Messung festgelegt, damit das Ergebnis sie nicht nachträglich rechtfertigt.

**Tabelle 10.9: Messgrößen der Sprachschnittstelle**

| Messgröße | Definition | Ebene | Daten |
|---|---|---|---|
| WER | (Ersetzungen + Auslassungen + Einfügungen) / Wörter der Referenz | ASR | Audio-Testset |
| Fachbegriff-Fehlerrate | Anteil falsch transkribierter Begriffe der Liste `fachbegriffe` | ASR | Audio-Testset |
| Zahlfehlerrate | Anteil der Zahlslots, deren Wert nach dem Parser vom Sollwert abweicht | ASR und Parser | Audio-Testset |
| Intent-Accuracy@1 und @3 | Anteil der Sätze mit richtigem Intent auf Platz 1 bzw. unter den ersten drei, je Ebene (Gruppe, Intent) | Intent | Textset, Audio-Testset |
| Slot-F1 | harmonisches Mittel aus Präzision und Vollständigkeit über (Slot, Wert)-Paare; Werte nach Normalisierung exakt | Parser, Referenz | Textset |
| Frame-Accuracy | Anteil der Sätze mit richtigem Intent und allen Slots richtig | gesamt | Textset |
| ECE | erwarteter Kalibrierungsfehler, 15 Intervalle, je Fragetyp | Intent | Entwicklungsset, Textset |
| Abdeckung | Anteil der Sätze ohne Rückfrage | Dialog | Textset |
| Fehlausführungsrate | Anteil der ausgeführten Frames, die falsch sind, je Risikoklasse | Dialog | Textset, Studie |
| Ergebnisgenauigkeit | Anteil der Sätze mit dem erwarteten Ergebnis nach Tabelle 10.8 | Dialog | Textset |
| End-to-End-Erfolg | Anteil der Aufgabenkarten, die ohne Hilfe und ohne falsche Endänderung gelöst werden; dazu Zeit, Dialogrunden und Abbrüche | gesamt | Nutzerstudie |
| wahrgenommene Gebrauchstauglichkeit | SUS und BUS-15 | gesamt | Nutzerstudie |

**Tabelle 10.10: Zielwerte für die Abnahme [U]**

| Messgröße | Ziel |
|---|---|
| WER (Deutsch, Audio-Testset) | ≤ 8 % |
| Fachbegriff-Fehlerrate | ≤ 5 % |
| Zahlfehlerrate | ≤ 2 % |
| Intent-Accuracy@1 (Intent-Ebene, Textset) | ≥ 0,90 |
| Slot-F1 (Parser- und Referenzslots, Textset) | ≥ 0,98 |
| ECE nach Kalibrierung | ≤ 0,05 |
| Fehlausführungsrate R1 / R2 / R3 | ≤ 2 % / ≤ 1 % / 0 |
| End-to-End-Erfolg in der Nutzerstudie | ≥ 0,80 |

Zwei Messgrößen verdienen eine Begründung. Die **Fehlausführungsrate** ist wichtiger als die Accuracy, weil eine falsche Ausführung Schaden anrichtet, eine Rückfrage nur Zeit kostet. Ein System, das häufiger zurückfragt, kann eine niedrigere Accuracy auf Platz 1 haben und trotzdem besser sein. Deshalb wird immer das Paar aus Abdeckung und Fehlausführungsrate berichtet. pass@k passt für Codegeneratoren, nicht für eine Intent-Schicht. Recherche 12 empfiehlt stattdessen Intent-Accuracy@1/@3 plus Slot-F1 je Ebene. Die **Slot-F1** der deterministischen Slots kann auf den Kategorien, die die Grammatik abdeckt, 1,0 erreichen. Ein Wert darunter zeigt dort einen Implementierungsfehler, keinen Modellfehler. Die Messung aus Tabelle 10.7 ist in diesem Sinn die Ausgangsmessung für B6.

### 10.5.3 Studiendesign

Die Evaluation hat drei Stufen.

1. **Textstufe.** Das Textset wird automatisch gegen die Pipeline gefahren, bei jeder Änderung von Katalog, Grammatik oder Modell (ANF-10-26). Vergleichssysteme sind der Schlüsselwortklassifikator (Rückfallebene nach E10.3), Laya ohne Fine-Tuning und Laya mit Fine-Tuning. Jev dient als externer Vergleich, nur mit dem Textset, weil es keine personenbezogenen Daten enthält.
2. **Audiostufe.** Jeder Satz des Textsets wird von mindestens 12 Sprecherinnen und Sprechern aufgenommen, mit einer Mischung aus Hochdeutsch und regionaler Färbung, in zwei Umgebungen: ruhig sowie Wohnraum mit Hintergrundgeräusch. Das ergibt mindestens 2.592 Aufnahmen. Gemessen werden WER, Fachbegriff- und Zahlfehlerrate für Voxtral, Parakeet mit Boosting und Whisper mit Hotwords (E10.1). Synthetische Sprache dient nur der Trainingsaugmentation, nie dem Test. Alle Aufnahmen setzen eine Einwilligung voraus (E10.11).
3. **Nutzerstudie.** Laien lösen Aufgabenkarten wie „Bad vergrößern, Dachgaube hinzufügen“. Das Muster stammt aus Recherche 12 und lehnt sich an Niemeijer an, der Studierende Constraints zu fehlerhaften Entwürfen formulieren ließ [@niemeijer2011constraint]. Jede Aufgabe wird einmal per Sprache und einmal per Direktbedienung gelöst, mit ausbalancierter Reihenfolge. Das entspricht dem Vergleich von Drag-and-Drop- und Konversationsoberfläche bei Dahlem et al. [@dahlem2026comparing]. Gemessen werden Aufgabenerfolg, Zeit, Dialogrunden, Rückfragen und Abbrüche. Die Gebrauchstauglichkeit wird nach ISO 9241-11 operationalisiert [@iso2018usability], die Zufriedenheit mit SUS [@brooke1996sus; @lewis2018system] und BUS-15. BUS-15 ist ein Instrument speziell für Konversationsagenten mit einer Reliabilität von 0,76 bis 0,87, eine deutsche Fassung fehlt allerdings [@borsci2022chatbot]. Formative Runden mit je fünf Personen finden nach Virzi rund 80 % der Probleme [@virzi1992subjects]. Die summative Runde braucht eine größere Stichprobe, die Kapitel 20 festlegt.

Die Nutzerstudie prüft auch die Hypothese aus Chen et al.: Sprache lohnt sich bei zusammengesetzten Änderungen, der Schieberegler bei einzelnen Parametern [@chen2025agent]. Aufgabenkarten beider Art gehören deshalb in die Studie. Ein Ergebnis zugunsten der Direktbedienung bei Einzelparametern wäre kein Misserfolg, sondern ein Gestaltungshinweis für die Oberfläche. Ein Evaluationsmuster aus dem Bauwesen liefert VISA4D: Dort wurden 71 von 80 baubezogenen Sprachbefehlen (89 %) richtig klassifiziert, ergänzt durch eine Befragung [@jaff2025visa4d].

### 10.5.4 Fine-Tuning-Plan für Laya

Ohne Fine-Tuning liegt Laya nahe am Zufallsniveau (10.2.5). Tabelle 10.11 beschreibt die Schritte bis zur Abnahme.

**Tabelle 10.11: Fine-Tuning und Kalibrierung von Laya**

| Schritt | Inhalt | Ergebnis |
|---|---|---|
| 1 Saatdaten | 415 Beispielsätze aus `intents.yaml`, je Intent mindestens drei | versioniert mit Katalogversion |
| 2 Erweiterung | Schablonen mit Slot-Werten aus dem Katalog; Paraphrasen, offline von einem Sprachmodell erzeugt und von einem Menschen geprüft (E10.6); Negativbeispiele für `meta` | Zielgröße etwa 50 Sätze je Intent [U] |
| 3 ASR-Rauschen | Sprachsynthese und Rückerkennung eines Teils der Sätze, damit die Trainingstexte echte Transkriptfehler enthalten | Transkriptvarianten |
| 4 Teilung | Training, Entwicklung und Test nach Schablonenfamilie und Sprecher getrennt; `sprach-testset.jsonl` nie im Training | Leckageprüfung durch den Validator |
| 5 Training | Kaggle-Notebook laut Model Card auf 2 × T4, Dauer etwa 4–5 Stunden (Recherche 03) [V]; getrennte Köpfe bzw. Fragen je Hierarchieebene | Modellgewichte mit Hash |
| 6 Kalibrierung | Temperatur je Fragetyp auf dem Entwicklungsset (10.2.5) | *T* je Fragetyp, ECE-Bericht |
| 7 Abnahme | Messgrößen nach Tabelle 10.9 am Textset gegen die Zielwerte von Tabelle 10.10; Vergleich mit Schlüsselwortklassifikator und Laya ohne Fine-Tuning | Abnahmebericht |
| 8 Pflege | neuer Intent ⇒ nur die betroffene Gruppenfrage neu trainieren und kalibrieren; Modell- und Katalogversion im Protokoll | Versionierung |

Der Plan übernimmt zwei Befunde aus T2S4BIM: die synthetische Erzeugung von Trainingsdaten und die Beobachtung, dass kleinere Encoder-Decoder-Modelle bei dieser Aufgabe mit größeren Decoder-Modellen mithalten können [@wei2025texttostructure]. Wang et al. stützen dasselbe Muster aus der Konfiguratorforschung. Dort bilden Text-Embeddings mit einem mehrschichtigen Perzeptron vage Bedarfsbeschreibungen genauso gut auf Attribute ab wie aufwendigere Verfahren [@wang2022natural]. Die Hierarchie hat beim Training einen weiteren Vorteil: Ein neuer Intent verändert nur die Frage seiner Gruppe. Das Modell muss also nicht vollständig neu kalibriert werden.

## 10.6 Grenzen und Zwischenfazit

**Grenzen.** Erstens ist die Intent-Schicht nicht gemessen. Alle Wahrscheinlichkeiten in B6 sind Stub-Werte, und keine Aussage dieses Kapitels über die Güte von Laya, Jev oder Voxtral stammt aus eigener Messung. Die Modelle sind seit etwa Mitte September 2026 öffentlich und damit sehr jung (Recherche 03) [V]. Zweitens deckt B6 nur einen Intent ab. Der Katalog ist eine Spezifikation, keine Implementierung. Drittens ist das Testset von einem Autor geschrieben. Es bildet die Sprache der Kunden nur so weit ab, wie der Autor sie vorhersieht. Die Datenlieferung DAT-10-02 soll das beheben. Viertens sind Zielwerte, Schwellen und Latenzbudget begründete Designentscheidungen ohne empirische Grundlage im Anwendungsfeld. Fünftens fehlt für die Definition des Kalibrierungsfehlers ein Literaturnachweis im Bestand.

**Zwischenfazit.** Das Kapitel beantwortet FF3 in vier Punkten:

1. **Das Modell wählt, der Code bestimmt.** Das Intent-Modell beantwortet nur typisierte Fragen über geschlossene Optionen, mit 112 choice-, 11 score- und 15 noul-Fragen im Katalog. Werte, Referenzen, Katalogartikel, Geometrie und Regeln entstehen im Code. Damit ist die Aufgabenteilung strenger als in allen Vergleichssystemen aus Kapitel 5 (Lücke L6).
2. **Zuverlässigkeit entsteht durch Enthaltung, nicht durch Treffsicherheit allein.** Kalibrierte Wahrscheinlichkeiten und Schwellen je Risikoklasse entscheiden zwischen Ausführen, Vorschau, Bildschirmbestätigung und Rückfrage. Rechtserhebliches geht nie per Sprache.
3. **Der deterministische Teil ist prüfbar und schnell.** B6 liest innerhalb seines Geltungsbereichs 46 von 54 Werten richtig, löst 55 von 58 Raumreferenzen auf und braucht dafür im Median 0,13 ms. Jeder gemessene Fehler entspricht einer benannten Regel der Grammatik.
4. **Die deutsche Sprachschnittstelle für den Hausentwurf ist spezifiziert** (Lücke L7): 16 Gruppen, 138 Intents, 415 Beispielsätze, eine Grammatik mit 58 Regeln und 14 Disambiguierungsregeln sowie ein Testset mit 216 Sätzen. Die empirische Prüfung folgt dem Plan in 10.5 und ist Gegenstand von Kapitel 20.

## 10.7 Umsetzungsvorgaben für die App

Die Arbeit ist die fachliche Grundlage einer App, die am Ende voll funktionieren soll. Es gelten die Regeln aus Kapitel 3.7: „Muss“ heißt, dass ohne die Anforderung ein Rechts-, Nachweis- oder Fehlausführungsfehler entstehen kann. „Soll“ heißt, dass sie Qualität oder Nutzen erhöht. Jedes Abnahmekriterium ist ein Testfall. Testfälle mit der Kennung T*nnn* stehen in `spezifikation/sprach-testset.jsonl`.

### 10.7.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/intents.yaml` | Intent-Katalog v0.1.0: Risikoklassen mit Schwellen, 5 globale Fragen, 29 Slottypen, 60 Fachbegriffe mit Varianten, 16 Gruppen mit je einer Intent-Frage und zusammen 138 Intents (je Beschreibung, Risikoklasse, ≥ 3 Beispielsätze, Slots mit Typ, Einheit, Wertebereich und Quelle, Fragen mit Schwelle, Regel-IDs, geplante Regeln, Module, Rückfragetext) |
| `spezifikation/werteparser-grammatik.md` | EBNF der Wort- und Morphemebene (58 Regeln), Einheitentabelle, Disambiguierungsregeln D1–D14, Slotzuordnung, 20 Referenzfälle mit dem heutigen B6-Ergebnis |
| `spezifikation/sprach-testset.jsonl` | 216 Testsätze mit erwarteter Gruppe, erwartetem Intent, Slots, Ergebnis, Risikoklasse, Kategorien und gegebenenfalls Dialogkontext; Referenzzustand `beispiele/daten/haus_state.json` |
| `spezifikation/pruefe_sprache.py` | Validator und Messung: Struktur des Katalogs, höchstens 19 Optionen, Regel-IDs gegen `regelkatalog.yaml` und `empfehlungen.yaml`, Testset gegen Katalog, Leckage, EBNF-Konsistenz, Messung von B6 |

**Prüfung (Python 3.11.15, PyYAML 6.0.1, 27.09.2026).** Aufruf aus `arbeit/`: `python spezifikation/pruefe_sprache.py`. Ergebnis:

- **Katalog:** 16 Gruppen, 138 Intents, 415 Beispielsätze, 316 Slots, Fragen 112 choice, 15 noul, 11 score, höchstens 18 Optionen je choice-Frage. Risikoklassen R0 29, R1 75, R2 27, R3 7. Alle Regel-IDs existieren.
- **Testset:** 216 Sätze, 138 Intents abgedeckt, keine Leckage.
- **Grammatik:** 2 EBNF-Blöcke, 58 Regeln, alle verwendeten Nichtterminale definiert.
- **Messung B6:** Werteparser 47 von 76 Zahlslots, Raumreferenz 55 von 58.
- **Fehler: 0.**

Eine Gegenprobe mit einem absichtlich undefinierten Nichtterminal wurde als Fehler gemeldet. Neue Regeln im Schema von `regel.schema.json` entstehen in diesem Kapitel nicht. Die geplanten Regeln stehen als Text im Feld `regeln_geplant` und sind in den Kapiteln 12 bis 15 zu formalisieren.

### 10.7.2 Anforderungen

**Spracherkennung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-01 | Muss | Die Spracherkennung läuft lokal und im Strom. Das Teiltranskript erscheint während des Sprechens, das Endtranskript ≤ 0,8 s nach Sprechende. | 10.1.4, E10.1 | Referenzaufnahme „Mach das Bad oben zwei Meter sechzig breit“ auf Zielhardware: Teiltranskript sichtbar vor Sprechende; Endtranskript ≤ 0,8 s danach; kein Netzwerkverkehr während der Erkennung. |
| ANF-10-02 | Muss | Die ASR-Schnittstelle liefert mindestens drei Hypothesen mit Konfidenz und Wortzeiten. Das Modell ist per Konfiguration austauschbar. | 10.1.2 | Umschalten Voxtral → Whisper in der Konfiguration ohne Codeänderung; beide liefern JSON mit `nbest[≥3]`, `konfidenz`, `woerter[].start/ende`. |
| ANF-10-03 | Muss | Fachbegriffe aus `intents.yaml/fachbegriffe` werden als Boosting-Liste übergeben und nach der Erkennung deterministisch nachkorrigiert. Die Korrektur steht im Protokoll. | 10.1.3 | Transkript „Den Knie Stock auf eins zwanzig“ (T034) ⇒ normalisiert „Den Kniestock auf eins zwanzig“, Protokolleintrag `nachkorrektur: Knie Stock → Kniestock`; Intent `kniestock_aendern`, Wert 1,20 m. |
| ANF-10-04 | Muss | Das Mikrofon ist nur nach Nutzeraktion aktiv (Push-to-talk); der Status ist sichtbar. | E10.2 | Ohne Tastendruck keine Audiodaten im Puffer (Test mit Mikrofonattrappe); Statussymbol wechselt innerhalb von 100 ms. |

**Intent-Erkennung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-05 | Muss | Das Intent-Modell beantwortet nur Fragen aus `intents.yaml`. Antworten außerhalb der Optionen werden verworfen, freier Text wird nie ausgeführt. | 10.2.1, 10.2.2 | Modellattrappe liefert die Option „dach_loeschen“, die nicht im Katalog steht ⇒ Ergebnis `rueckfrage_intent`, Protokoll „Option unbekannt“. |
| ANF-10-06 | Muss | Der Katalog wird beim Start validiert; jede choice-Frage hat höchstens 19 Optionen. | 10.2.3, 10.7.1 | `pruefe_sprache.py` meldet 0 Fehler. Kopie mit 20 Optionen in `q.gruppe` ⇒ Ladefehler „mehr als 19“. |
| ANF-10-07 | Muss | Die Erkennung ist hierarchisch (Gruppe → Intent → Slotfragen). Unter der Gruppenschwelle werden zwei Gruppen parallel bewertet. Ein Kontextfilter entfernt unzulässige Optionen. | 10.2.3, E10.4 | „Ja, genau so“ (T177) mit offener Rückfrage ⇒ `bestaetigen`; derselbe Satz ohne offene Rückfrage ⇒ `bestaetigen` nicht unter den Optionen, Ergebnis `rueckfrage_intent`. |
| ANF-10-08 | Muss | Wahrscheinlichkeiten werden je Fragetyp und Modellversion per Temperatur kalibriert; *T* steht im Protokoll. | 10.2.5 | Kalibrierbericht am Entwicklungsset: ECE (15 Intervalle) ≤ 0,05 je Fragetyp; jedes Äußerungsprotokoll enthält `kalibrierung.T` und `modell_version`. |
| ANF-10-09 | Muss | Ausgeführt wird nur bei $\hat p_1 \ge \tau_k$ und $\hat p_1 - \hat p_2 \ge \delta_k$ der Risikoklasse *k*; Schwellen sind versionierte Konfiguration. | 10.2.5, Tab. 10.6 | B6 „Kannst du das mal anders machen“ (p = 0,46; Abstand 0,15) ⇒ Rückfrage. Attrappe R1 mit (0,75; 0,40) ⇒ ausführen; R2 mit (0,75; 0,40) ⇒ Rückfrage (τ = 0,80). |
| ANF-10-10 | Soll | Ohne verfügbares Intent-Modell übernimmt ein Schlüsselwortklassifikator die Intents von R0 und R1; R2 und R3 werden auf die Oberfläche umgeleitet. | E10.3 | Modell abgeschaltet: „Mach das rückgängig“ ⇒ Undo ausgeführt; „Wir wollen einen Keller“ ⇒ Hinweis und Bildschirmauswahl, keine Änderung. |

**Werteparser und Referenzauflösung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-11 | Muss | Werte entstehen nur im Werteparser nach `werteparser-grammatik.md`, einschließlich Tausenderpunkt (D1) und Wertebereichsprüfung (D13). | 10.3.2, 10.3.4, E10.6 | Alle 20 Referenzfälle der Grammatik (Abschnitt 6, Spalte „Soll“); die 16 Parserfälle aus `test_b6_b7.py` bleiben grün; „2.500 mm“ ⇒ 2,50 m, „1.20m“ ⇒ 1,20 m. |
| ANF-10-12 | Muss | Mehrdeutige Werte führen zu einer Rückfrage mit allen Kandidaten im Wertebereich. | D3, 10.3.4 | „Das Bad oben eins fünf breiter“ (T007) ⇒ Rückfrage „1,05 m oder 1,50 m?“. |
| ANF-10-13 | Muss | Eine Zahl ohne Einheit erhält die Einheit des Slots (D4); die Interpretationsanzeige kennzeichnet das. | D4 | „Mach die Dachneigung auf fünfunddreißig“ (T070) ⇒ 35°, Anzeige „35° (Einheit ergänzt)“; Vorschau wegen R2. |
| ANF-10-14 | Muss | Keine implizite Dimension: Fehlt ein Pflichtslot ohne Voreinstellung im Katalog, folgt eine Rückfrage. | 10.3.3 | „Mach das Kinderzimmer 2 auf 3,20 m“ (T004) ⇒ Rückfrage „Breite oder Tiefe?“ (B6 heute: stillschweigend Breite). „Das Obergeschoss zehn Zentimeter höher“ (T037) ⇒ lichte Höhe nach `standard`, gekennzeichnet. |
| ANF-10-15 | Muss | Referenzen werden gegen das State-JSON aufgelöst: exakter Name vor Typ, dann Geschoss, Nummer, Größe, Relation, Kontext; Quantoren ergeben Mengen. Ergebnis ist eine GlobalId oder eine Liste. | 10.3.5, E10.7 | Alle 58 Raumslots des Testsets ohne Kontextfälle richtig (B6: 55); „Die Diele zwanzig Zentimeter schmaler“ (T018) ⇒ `3VNmzLkorKaPT3n1GT$V3f`; „In jedes Kinderzimmer …“ (T114) ⇒ beide Kinderzimmer. |
| ANF-10-16 | Muss | Bei mehrdeutiger Referenz fragt das System mit höchstens fünf Kandidaten zurück und wählt nie selbst. | E10.7 | „Das Bad soll zwanzig Zentimeter breiter werden“ (T003) ⇒ Rückfrage „Duschbad EG oder Bad OG?“, keine Änderung. |
| ANF-10-17 | Muss | Korrekturen und Anaphern werden über den Dialogkontext der letzten drei Äußerungen aufgelöst (`n.korrektur`, `n.bezug_vorher`). | 10.4.3 | Testfälle T212–T216 mit Kontext: erwarteter Intent und alle Slots richtig; „Nein, nicht das Bad, das Kinderzimmer 1“ ersetzt nur den Raum im vorigen Frame. |

**Dialog, Transparenz, Datenschutz**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-18 | Muss | Rückfrage und Ablehnung sind getrennt. Eine Ablehnung trägt Konfliktmenge, Begründung und Alternative nach Kapitel 9.5 und ist mit `alternative_waehlen` übernehmbar. | 10.4.2, ANF-09-13, ANF-09-15 | „Mach das Kinderzimmer 1 einen Meter zwanzig schmaler“ (T006) ⇒ Ablehnung mit {Mindestbreite, Mindestfläche} und Alternative „höchstens 0,55 m schmaler (2,95 m; 10,03 m²)“; „Nimm die zweite Möglichkeit“ übernimmt eine angebotene Alternative. |
| ANF-10-19 | Muss | Jede Ausführung zeigt den verstandenen Frame (Interpretationsanzeige); jede R1/R2-Änderung ist mit einem Schritt umkehrbar. | 10.4.3, E10.10 | Nach T001 Anzeige „Bad (OG) · Breite · 2,60 m (absolut)“; „Nimm das zurück“ (T166) ⇒ SHA-256 des Zustands gleich dem Ausgangszustand. |
| ANF-10-20 | Muss | R3-Intents werden nie per Sprache allein ausgeführt; `freigabe_erklaeren` verweist auf das Freigabe-Gate. | E10.9, Tab. 10.6 | „Ich gebe den Bauantrag jetzt frei“ (T202) und „Hiermit bestelle ich das Haus verbindlich“ (T203) ⇒ `verweis_ui`, kein `IfcApproval`; „Lösch die Variante mit Garage“ (T172) ⇒ Bildschirmdialog, Variante besteht bis zur Bestätigung. |
| ANF-10-21 | Muss | Nach zwei erfolglosen Rückfragen in Folge wechselt der Dialog zur Auswahl am Bildschirm. | E10.8 | Skript: „Das Bad größer“ → Rückfrage → „das andere“ → Rückfrage → „weiß nicht“ ⇒ Grundriss mit markierten Kandidaten zum Antippen. |
| ANF-10-22 | Muss | KI-Hinweis nach Art. 50 Abs. 1 KI-VO bei der ersten Mikrofonaktivierung, dauerhaftes Symbol während der Spracheingabe, fester Antworttext für `ki_transparenz`; eine Sprachausgabe wird maschinenlesbar gekennzeichnet. | 10.4.4 | UI-Test: Hinweistext aus dem Katalog erscheint vor der ersten Erkennung; „Bist du eine KI“ (T204) ⇒ Katalogtext; Audiodatei der Sprachausgabe enthält die Kennzeichnung. |
| ANF-10-23 | Muss | Kein Rohaudio über die Sitzung hinaus, keine Sprechererkennung. Jev nur mit Einwilligung, Zero Data Retention und nur mit Transkript. Aufnahmen für Training nur mit gesonderter Einwilligung. | 10.4.5, E10.11 | Nach Sitzungsende keine Audiodatei im Speicher (Dateisystem- und Datenbankprüfung); ohne Einwilligung kein Aufruf des Jev-Endpunkts (Netzwerkprotokoll); „Lösch bitte meine Sprachaufnahmen“ (T206) entfernt alle Aufnahmen des Nutzers. |
| ANF-10-24 | Muss | Jede Äußerung wird mit ASR-Modell und Version, Hypothesen, Fragen und Wahrscheinlichkeiten, Katalogversion, Parser- und Referenzergebnis, Entscheidung, betroffenen GlobalIds und Zustands-Hash protokolliert. Das Protokoll ist ohne Modell reproduzierbar. | 10.3.1, 4.8.1 | Protokoll nach Tabelle 10.12 für T001; Wiedergabe mit den protokollierten Modellantworten ergibt bitgleichen Frame und Zustand (Erweiterung von `test_pipeline_deterministisch`). |
| ANF-10-25 | Muss | Jede Funktion, die per Sprache erreichbar ist, ist auch ohne Sprache erreichbar. | 10.4.5 | Abbildungstest: Für jeden der 138 Intents existiert ein Bedienpfad der Oberfläche; fehlender Pfad ⇒ Testfehler. |
| ANF-10-26 | Soll | Das Textset läuft bei jeder Änderung von Katalog, Grammatik oder Modell; die Abnahme folgt den Zielwerten aus Tabelle 10.10. | 10.5 | CI-Lauf erzeugt Bericht mit Intent-Accuracy@1/@3, Slot-F1, Frame-Accuracy, ECE, Abdeckung und Fehlausführungsrate je Risikoklasse; Unterschreitung eines Zielwerts ⇒ Freigabe gesperrt. |
| ANF-10-27 | Soll | Fine-Tuning und Kalibrierung von Laya sind reproduzierbar dokumentiert (Datensatz-Hash, Katalogversion, Modell-Hash, *T*). | 10.5.4 | Abnahmebericht nennt alle vier Werte; Leckageprüfung Testset ↔ Trainingsdaten: 0 Treffer. |
| ANF-10-28 | Soll | Unscharfe Stärkeangaben ergeben eine Stufe der score-Frage und immer eine Vorschau; die Schrittweite je Stufe ist Konfiguration. | D10, 10.2.2 | „Mach des Bad oben a bissl größer“ (T013) ⇒ Stufe 1, Vorschau mit der konfigurierten Schrittweite der Stufe 1, gekennzeichnet als Voreinstellung; keine Änderung ohne Bestätigung. |

### 10.7.3 Datenstrukturen

Tabelle 10.12 beschreibt den Frame, den die Pipeline je Äußerung erzeugt und protokolliert. Er erweitert das Format von `beispiele/ausgabe/intent_protokoll.json`.

**Tabelle 10.12: Frame einer Äußerung**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `aeusserung_id` | string (UUID) | – | eindeutig je Sitzung | Dialog |
| `transkript` | string | – | ≤ 1024 Tokens (Kontext Laya, Recherche 03) | ASR |
| `nbest` | list[{text, konfidenz}] | – | ≥ 3 Einträge, konfidenz 0–1 | ASR, ANF-10-02 |
| `asr_modell`, `asr_version` | string | – | z. B. Voxtral Mini 4B Realtime 2602 | Konfiguration |
| `nachkorrektur` | list[{von, nach}] | – | Begriffe aus `fachbegriffe` | 10.1.3 |
| `gruppe` | {option, p} | – | Option aus `q.gruppe`; p 0–1 kalibriert | Intent-Modell |
| `intent` | {option, p, p2, risikoklasse} | – | Intent aus `intents.yaml`; R0–R3 | Intent-Modell, Katalog |
| `fragen` | list[{id, typ, antwort, p}] | – | typ ∈ {choice, score, noul} | Intent-Modell |
| `slots` | map[name → {wert, einheit, quelle_text, muster, einheit_herkunft, mehrdeutig, kandidaten}] | SI (m, m², °, …) | Wertebereich je Slot in `intents.yaml` | Werteparser |
| `referenzen` | map[name → {status, guid, guids, kandidaten, kriterien}] | – | status ∈ {eindeutig, mehrdeutig, menge, keine} | Referenzauflösung |
| `kontext` | {vorher_id, korrektur, bezug_vorher} | – | Tiefe ≤ 3 Äußerungen | Dialog, ANF-10-17 |
| `entscheidung` | enum | – | ausfuehren, vorschau_bestaetigung, bestaetigung_ui, auskunft, rueckfrage_{intent, slot, wert, referenz}, ablehnung_regel, verweis_ui, abgewiesen_{ausschluss, umfang} | Dialogsteuerung, Tab. 10.8 |
| `begruendung` | string | – | Katalogtext mit eingesetzten Werten | Katalog, Regelmaschine |
| `nachweis_id` | string | – | nur bei Ablehnung | Kapitel 7a, ANF-09-16 |
| `katalog_version`, `grammatik_version`, `modell_version` | string (SemVer) | – | z. B. 0.1.0 | Konfiguration |
| `kalibrierung` | {T_choice, T_score, T_noul} | – | T > 0 | 10.2.5 |
| `schwellen` | {tau, delta} | – | je Risikoklasse | `intents.yaml` |
| `state_hash_vor`, `state_hash_nach` | string (SHA-256) | – | 64 Hex-Zeichen | Parametermodell |
| `zeitstempel`, `latenz_ms` | ISO 8601, map | ms | je Stufe aus Tab. 10.2 | Laufzeit |

### 10.7.4 Datenlieferungen von Regnauer

| ID | Inhalt | gewünschtes Format | Ersatz bis zur Lieferung | blockiert |
|---|---|---|---|---|
| DAT-10-01 | Fach- und Produktbegriffe des Herstellers (Hausmodelle, Wand- und Deckenbezeichnungen, Bemusterungsartikel), die Kunden aussprechen | CSV: Begriff, Varianten, Bedeutung | Liste `fachbegriffe` in `intents.yaml` (60 Begriffe) | ANF-10-03 |
| DAT-10-02 | anonymisierte, schriftlich notierte Kundenwünsche aus Beratungsgesprächen (keine Aufnahmen ohne Einwilligung aller Beteiligten, § 201 StGB) | Text oder CSV, je Wunsch ein Satz | synthetische Sätze aus `intents.yaml` | ANF-10-26, ANF-10-27 |
| DAT-10-03 | Zugang zu Sprecherinnen und Sprechern aus Kundschaft und Belegschaft mit Einwilligung für das Audio-Testset | Teilnehmerliste mit Einwilligung | eigene Aufnahmen im Forschungsteam | ANF-10-01, 10.5.3 |
| DAT-10-04 | Kostenschwelle, ab der eine Änderung als folgenreich gilt (Risikoklasse R2) | Betrag in € und Bezug (absolut oder relativ zum Angebot) | 1 000 € [U] | ANF-10-09 |
| DAT-10-05 | Suchbegriffe und Synonyme des Bemusterungskatalogs für die Katalogsuche (Ergänzung zu DAT-07) | Spalte im Katalogexport | Artikelbezeichnung | Katalogslots, 10.3.5 |
| DAT-10-06 | Freeze-Termine je Bemusterungskategorie für den Text von `bemusterung_abschliessen` (Ergänzung zu DAT-08) | Tabelle Kategorie × Frist | Hinweis ohne Datum | ANF-10-20 |

---

## Verwendete Schlüssel

Das Kapitel enthält 48 Zitatstellen zu 41 Schlüsseln. Alle stammen aus `literatur/lit-*.bib`. Zugeordnet ist jeweils die erste Datei in alphabetischer Reihenfolge, in der ein Schlüssel steht. Für die KI-Verordnung ist der führende Schlüssel `aiact2024` verwendet, nicht die Dublette `eu2024aiact`. Für die DSGVO und für den erwarteten Kalibrierungsfehler (ECE) fehlt ein Eintrag im Literaturverzeichnis; beide Stellen sind im Text ohne Schlüssel genannt und als Lücke markiert.

**lit-B-vorfertigung-ki.bib** (8): `atakan2025kakadoo`, `chen2019bert`, `chen2025agent`, `ji2023hallucination`, `lee2024generalized`, `pundak2018deep`, `radford2023whisper`, `tur2011spoken`

**lit-C-recht-normen.bib** (2): `aiact2024`, `bfsg`

**lit-E-vergleich-automation.bib** (5): `hellin2026bim`, `kodnongbua2024zeroshot`, `kou2008design`, `kou2010knowledge`, `niemeijer2011constraint`

**lit-F-architekturpsychologie.bib** (1): `miller2019explanation`

**lit-G-luecken.bib** (2): `brooke1996sus`, `iso2018usability`

**lit-H-ff4-ff5.bib** (2): `parasuraman2010complacency`, `wilhelmi2020haftung`

**lit-I-schneeball-b.bib** (10): `borsci2022chatbot`, `elghaish2022voice`, `gao2023pal`, `jaff2025visa4d`, `jakesch2023cowriting`, `kulesza2013explanations`, `li2024spatial`, `park2026bimllm`, `virzi1992subjects`, `wang2022natural`

**lit-J-schneeball-runde2.bib** (3): `dahlem2026comparing`, `lewis2018system`, `wei2025texttostructure`

**lit-K-ff4-jur.bib** (7): `dsk2024ki`, `edpb2021vva`, `eu2025aidefinition`, `eu2026omnibus`, `eugh2023schufa`, `stgb201`, `tdddg25`

**lit-L-schneeball-runde3.bib** (1): `weld2022survey`

### Python-Key-Check

```python
import re, glob, pathlib
text = pathlib.Path("10-sprachschnittstelle.md").read_text(encoding="utf-8")
body = text.split("## Verwendete Schlüssel")[0]
cited = {k.strip().lstrip("@") for grp in re.findall(r"\[(@[^\]]+)\]", body) for k in grp.split(";")}
bib = set()
for f in glob.glob("literatur/lit-*.bib"):
    bib |= set(re.findall(r"^@\w+\{([^,\s]+),", open(f, encoding="utf-8").read(), re.M))
print(len(cited), "zitiert;", len(cited - bib), "fehlend:", sorted(cited - bib) or "keine")
```

Ergebnis (27.09.2026, aus `arbeit/` ausgeführt): `41 zitiert; 0 fehlend: keine`, also **0 fehlend**.

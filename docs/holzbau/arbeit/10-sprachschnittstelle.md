# 10 Sprachschnittstelle

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle geprüft) oder [U] (unsicher); eigene Bewertungen und Designentscheidungen sind als solche formuliert. Zahlen aus dem Prototyp stammen aus `beispiele/b6_intent_pipeline.py`, `beispiele/ausgabe/intent_protokoll.json`, `beispiele/tests/test_b6_b7.py` und aus Messläufen, die in diesem Kapitel mit Datum und Umgebung angegeben sind. **Alle Wahrscheinlichkeiten im Prototyp B6 sind feste, erfundene Stub-Werte und keine Modellausgaben.**

## 10.0 Einordnung und Vorgehen

Im Zielbild sagt Familie H. „Das Bad oben einen Meter größer, Richtung Süden“, und das Modell ändert sich; Unzulässiges wird mit Grund und Alternative abgelehnt (`../00-zielbild.md`, Abschnitt 3.1). Kapitel 5 hat gezeigt, dass die Sprach-BIM-Forschung diesen Schritt fast immer dem Sprachmodell überlässt, das Code, Daten oder Constraints erzeugt (Abschnitt 5.6.4). Eine strengere Aufgabenteilung ist nicht dokumentiert (Lücke L6), und für deutschsprachige Intent-Erkennung im Hausentwurf fehlen Korpus und Evaluation (Lücke L7). Das Kapitel beantwortet deshalb FF3:

> Wie wird gesprochene deutsche Sprache zuverlässig in deterministische Modelländerungen übersetzt? Welche Aufgaben übernimmt das Sprachmodell, welche der Code?

Die Antwort folgt der Verarbeitungskette einer Äußerung:

1. **Spracherkennung** (10.1): lokal, im Strom, mit Fachbegriff-Boosting und Latenzbudget.
2. **Intent-Erkennung** (10.2): Ein Entscheidungsmodell beantwortet typisierte Fragen aus einem hierarchischen Katalog und liefert kalibrierte Wahrscheinlichkeiten, aber keine Werte.
3. **Werteparser und Referenzauflösung** (10.3): Code liest Zahlen, Einheiten und Richtungen und löst „das Bad oben“ in eine IFC-GlobalId auf.
4. **Dialogsteuerung** (10.4): Schwellen je Risikoklasse entscheiden über Ausführen, Vorschau, Rückfrage oder Ablehnung; dazu Transparenz und Datenschutz.
5. **Evaluation** (10.5): Testset, Messgrößen und Fine-Tuning-Plan.

Der Prototyp B6 implementiert den deterministischen Teil: Werteparser, Raumreferenz, Anwendung eines Intents mit Regelprüfung. Das Intent-Modell ist darin ein Stub mit derselben Schnittstelle wie Laya bzw. Jev. Neu sind drei Dateien: der Intent-Katalog `spezifikation/intents.yaml`, die Grammatik `spezifikation/werteparser-grammatik.md` und das Testset `spezifikation/sprach-testset.jsonl`, gegen das B6 gemessen wurde.

## 10.1 Spracherkennung für Deutsch

### 10.1.1 Anforderungen aus dem Entwurfsdialog

Die Spracherkennung (ASR) eines Entwurfswerkzeugs unterscheidet sich von Diktat und Sprachassistent in vier Punkten:

- **Zahlen tragen die Bedeutung.** „Eins zwanzig“ und „eins fünfzig“ trennen 30 cm Raumbreite. Die Wortfehlerrate (WER) gewichtet diesen Fehler wie den an einem Füllwort.
- **Fachbegriffe sind selten.** „Kniestock“, „Ortgang“, „Rigole“ oder „Zwerchgiebel“ kommen in allgemeinen Trainingsdaten kaum vor. Deutsche Sprachdatensätze aus dem Bauwesen wurden nicht gefunden (Recherche 03) [V].
- **Die Äußerungen sind kurz, der Kontext ist bekannt.** Modellzustand, Auswahl und letzte Rückfrage kann die Erkennung nutzen.
- **Die Antwort muss schnell kommen.** Bei Änderungen eines einzelnen Parameters bevorzugen Nutzer laut Einzelbewertung den Schieberegler [@chen2025agent]. Sprache muss sich bei zusammengesetzten Änderungen lohnen und darf bei einfachen nicht bremsen.

Große, schwach überwachte Modelle wie Whisper erreichen eine hohe Robustheit ohne Feinabstimmung [@radford2023whisper]. Für seltenes Vokabular ist Contextual Biasing das Standardverfahren: Eine Liste von Kontextphrasen wird zur Laufzeit begünstigt. CLAS senkte die relative WER gegenüber nachgeschalteter Fusion um bis zu 68 % [@pundak2018deep]; übernommen wird nur das Prinzip über die Boosting-Funktionen verfügbarer Modelle.

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

Für den Favoriten fehlt eine Angabe zum Fachvokabular, für Parakeet ist Boosting dokumentiert. Die einzige deutsche Fehlerrate ist eine Modellangabe ohne Bauvokabular. Welches Modell besser passt, entscheidet deshalb nur das eigene Testset (10.5).

> **E10.1 (Spracherkennung).** Die Spracherkennung läuft lokal hinter einer austauschbaren Schnittstelle. Diese liefert n-beste Hypothesen mit Konfidenz und Wortzeiten. Voxtral Realtime ist das Primärmodell, Parakeet v3 mit Boosting wird parallel gemessen, Whisper ist die Rückfallebene. Die endgültige Wahl trifft die Messung von WER, Fachbegriff-Fehlerrate und Zahlfehlerrate am Audio-Testset (10.5.3), nicht die Modellangabe.

Die n-besten Hypothesen haben einen Zweck. Bei Kou und Tan erkannte eine CAD-spezifische Grammatik deutlich besser als freies Diktat [@kou2008design]; die Folgearbeit filtert Kandidaten nach dem Modellkontext und fragt bei Mehrdeutigkeit nach [@kou2010knowledge]. Nennt die beste Hypothese etwa einen Raum, den es nicht gibt, prüft das System die zweite und dritte, bevor es zurückfragt.

### 10.1.3 Fachbegriffe: Boosting und Nachkorrektur

Die Fachbegriffe werden an zwei Stellen behandelt.

**Vor der Erkennung (Boosting).** Die Liste `fachbegriffe` in `intents.yaml` enthält 60 Begriffe mit Varianten: die Startliste aus Recherche 03 (Kniestock, Gaube, Pfette, Sparren, OSB, Schwelle) und Slot-Werte des Katalogs wie „Krüppelwalmdach“, „Hebeschiebetür“ oder „Rigole“. Sie geht als Boosting- bzw. Hotword-Liste an das Modell (Tabelle 10.1).

**Nach der Erkennung (Nachkorrektur).** Die Varianten bilden typische Fehltranskripte auf den Begriff ab („Knie Stock“ → „Kniestock“, „H T Strich“ → H′T); nur phonetisch ähnliche Formen werden unscharf abgeglichen (Recherche 03). Die Korrektur ist deterministisch und steht im Protokoll.

Das Testset enthält 40 Sätze mit Fachbegriffen und drei mit Erkennungsartefakten. Herstellerbegriffe fehlen noch (DAT-10-01).

### 10.1.4 Latenzbudget

Tabelle 10.2 verteilt das Zeitbudget vom Ende der Äußerung bis zur sichtbaren Änderung. Das Ziel von 1,5 s ist eine Designentscheidung [U], die die Nutzerstudie prüft (Kapitel 20). „Messung“ heißt: am 27.09.2026 in der Arbeitsumgebung gemessen (Python 3.11.15, Linux-Container), nicht auf Zielhardware.

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

Der deterministische Teil ist nicht der Engpass: Parser, Referenz und Regelprüfung liegen zwei bis drei Größenordnungen unter der Spracherkennung. Das Budget hängt an der Streaming-Verzögerung und ist mit Whisper, das nur in Stücken arbeitet, nicht einzuhalten (E10.1). Während des Sprechens zeigt die Oberfläche das Teiltranskript, nach der Intent-Erkennung sofort die Interpretation („Verstanden: Bad OG · Breite · 2,60 m“), noch vor dem Neuaufbau des Modells (10.4.3).

> **E10.2 (Aktivierung).** Das Mikrofon ist nur nach Tastendruck oder Tippen bis zur Sprechpause aktiv (Push-to-talk), ohne Dauerlauschen und Aktivierungswort. So entstehen keine versehentlichen Aufnahmen, die zu löschen wären [@edpb2021vva], und der Beginn einer Äußerung ist eindeutig.

## 10.2 Intent-Erkennung mit typisierten Fragen

### 10.2.1 Aufgabenteilung: was das Modell entscheidet

Spoken Language Understanding überführt eine Äußerung in Domäne, Absicht (Intent) und Attribut-Wert-Paare (Slots) [@tur2011spoken]; gemeinsame Modelle für beides sind Stand der Technik [@chen2019bert; @weld2022survey]. Im Bauwesen zerlegt T2S4BIM Nutzeranfragen in Intent und Slots und führt sie als Revit-Aktion aus; laut Abstract erreichen T5 und FLAN-T5 mit synthetischen Trainingsdaten ähnliche Werte wie deutlich größere Decoder-Modelle [@wei2025texttostructure]. NADIA-S gliedert Speech-to-BIM in sechs Schritte: interpret, fill, match, structure, execute, check [@lee2024generalized]. Die Arbeit übernimmt die Zerlegung, verteilt die Schritte aber strenger (Tabelle 10.3).

**Tabelle 10.3: Aufgabenteilung zwischen Modell und Code**

| Schritt (NADIA-S) | Aufgabe in dieser Arbeit | entscheidet | Ausgabe |
|---|---|---|---|
| interpret | Transkript; Gruppe, Intent, Aufzählungswerte, Ja/Nein-Merkmale, Stärke | Spracherkennung und Intent-Modell (KI) | Wahrscheinlichkeiten über geschlossene Optionen |
| fill | Zahlen, Einheiten, Richtungen, Ordinale | Werteparser (Code) | Messwerte mit Herkunft |
| match | Raum, Bauteil, Möbel, Katalogartikel | Referenzauflösung und Katalogsuche (Code) | GlobalId bzw. Typobjekt oder Kandidatenliste |
| structure | typisierter Frame nach `intents.yaml` | Code | Frame-JSON |
| execute | Änderung des Parametermodells, Solver | Code | neuer Zustand und Änderungsliste |
| check | Regelprüfung R1–R4, Empfehlungen R5 | Regelmaschine (Code) | Nachweis, Ablehnung mit Alternative |

Das Intent-Modell erzeugt keinen Code, keine Geometrie und keinen Wert; es wählt nur aus Optionen des Katalogs. Drei Befunde begründen die Grenze:

- **Rechnen gehört in den Interpreter.** Sprachmodelle, die das Rechnen an einen Interpreter abgeben, lösen Rechenaufgaben deutlich besser [@gao2023pal]; die Selbstprüfung von GPT-4 machte Rechenfehler (Recherche 12) [@kodnongbua2024zeroshot].
- **Räumliches Schließen ist unzuverlässig.** Sprachmodelle bilden Text auf räumliche Relationen ab, scheitern aber am mehrstufigen Schließen [@li2024spatial]. „Das Bad oben“ erkennen sie; welcher Raum das ist, entscheidet der Code.
- **Freie Ausgaben halluzinieren** [@ji2023hallucination]. Bei geschlossenen Optionen ist eine Halluzination nur die Wahl einer falschen Option, und diese begrenzt der Schwellwert (10.2.5).

Die Grenze ist auch die rechtliche. Rein menschlich definierte Regeln und einfache Datenverarbeitung fallen nach den Leitlinien der Kommission aus dem Begriff des KI-Systems [@eu2025aidefinition]; voraussichtlich ist nur das Intent-Modell ein KI-System, die Regelmaschine nicht (Recherche 27). Haftungsrechtlich entspricht das einem automatisierten, nicht autonomen System [@wilhelmi2020haftung].

### 10.2.2 Fragetypen: choice, score, noul

Die Intent-Schicht folgt dem Schnittstellenmuster von Jev (Recherche 03) [V]: Eingabe sind ein Zustand und typisierte Fragen, Ausgabe typisierte Antworten mit Wahrscheinlichkeiten, kein Text.

- **choice:** 1 bis 255 feste Optionen, Antwort ist eine Verteilung, z. B. „Welche Dachform ist gemeint?“.
- **score:** Rubrik mit 2 bis 10 Stufen, z. B. „Wie stark soll die Änderung sein?“. Sie ersetzt keinen Zahlwert, wird nur ohne erkannten Wert gestellt („a bissl größer“) und führt immer zu einer Vorschau (Regel D10).
- **noul:** Ja/Nein-Frage mit P(wahr) zwischen 0 und 1; den Schwellwert setzt der Code je Frage nach den Fehlerkosten (Recherche 03) [V].

Alle Fragen eines Aufrufs laufen parallel. Der Katalog nutzt 112 choice-Fragen (die Gruppenfrage `q.gruppe`, 16 Intent-Fragen `q.intent.<gruppe>` und 95 Slotfragen), 11 score- und 15 noul-Fragen. Global, also bei jeder Äußerung, laufen `q.gruppe` und die vier noul-Fragen der Tabelle 10.4.

**Tabelle 10.4: Globale noul-Fragen**

| ID | Frage | Schwelle | Wirkung |
|---|---|---|---|
| `n.korrektur` | Korrigiert oder widerruft der Sprecher seine vorige Äußerung? | 0,60 | vorigen Frame ersetzen statt neuen anlegen |
| `n.nur_frage` | Will der Sprecher nur eine Auskunft, ohne etwas zu ändern? | 0,65 | Gruppe „anzeigen_auswerten“ bevorzugen, keine Änderung |
| `n.bezug_vorher` | Bezieht sich die Äußerung auf das zuletzt genannte oder ausgewählte Objekt? | 0,60 | Referenz aus dem Dialogkontext |
| `n.verneinung` | Enthält die Äußerung eine Verneinung des Wunsches? | 0,60 | Aktion invertieren oder zurückfragen |

Sie fangen Dialogphänomene ab, die ein Intent-Klassifikator übersieht: „Nein, nicht das Bad, das Kinderzimmer 1“ korrigiert einen Slot im vorigen Frame; „Wie breit ist das Bad oben?“ und „Mach das Bad oben breiter“ teilen fast alle Wörter, gehören aber zu verschiedenen Gruppen. Weil der noul-Typ von Laya laut Model Card „wahr“ teils zu selten meldet (Recherche 03) [V], liegen diese Schwellen niedriger und werden nach der Kalibrierung neu gesetzt.

### 10.2.3 Hierarchie unter 20 Optionen

Laut Model Card verschlechtert sich Laya bei mehr als etwa 20 Optionen deutlich (Recherche 03) [V]. Ein flacher Katalog mit 138 Intents scheidet aus. Der Katalog ist ein Baum mit drei Ebenen: **Gruppe** (`q.gruppe`, 16 Optionen, dazu die globalen noul-Fragen), **Intent** (`q.intent.<gruppe>`, höchstens 13 Optionen) und **Slotfragen** des Intents, etwa „Welche Dachform?“. Die größte choice-Frage hat 18 Optionen (Nutzung eines Raums); der Validator lehnt jede Frage mit mehr als 19 ab.

Ein Fehler auf der Gruppenebene ist auf der Intent-Ebene nicht mehr korrigierbar. Zwei Maßnahmen begrenzen das. Liegt die beste Gruppe unter ihrer Schwelle, wird die Intent-Frage für die zwei besten Gruppen parallel gestellt, und maßgeblich ist P(Gruppe) · P(Intent | Gruppe). Ein **Kontextfilter** bietet unzulässige Optionen gar nicht an: „Bestätigen“ nur bei offener Rückfrage, „Alternative wählen“ nur nach einer angebotenen Alternative. Das entspricht der kontextbewussten Inferenz nach Kou et al. [@kou2010knowledge].

> **E10.3 (Intent-Modell).** Laya, lokal, feinabgestimmt und kalibriert (10.5.4). Jev nur mit Einwilligung als Cloud-Rückfallebene mit Zero Data Retention. Ohne Modell übernimmt ein Schlüsselwortklassifikator nach dem Muster von Shapeshift (Recherche 03) die Intents von R0 und R1; alle anderen gehen über die Oberfläche.
>
> **E10.4 (Hierarchie).** Baum aus Gruppe, Intent und Slotfragen mit höchstens 19 Optionen je Frage, zwei Gruppen parallel unter der Gruppenschwelle, Kontextfilter.

### 10.2.4 Der Intent-Katalog

Der Katalog `spezifikation/intents.yaml` (v0.1.0) deckt alle Themen der Gliederung ab (Tabelle 10.5).

**Tabelle 10.5: Intent-Katalog (Gruppen → Intents)**

| Gruppe | Intents | Beispiele für Intents | betroffene Kapitel |
|---|---:|---|---|
| grundriss | 10 | raum_groesse_aendern, raeume_tauschen, raeume_zusammenlegen, innenwand_versetzen | 9, 9b |
| geschosse_baukoerper | 10 | kniestock_aendern, geschosshoehe_aendern, keller_festlegen, haus_verschieben | 4.3, 9 |
| huelle | 10 | fenster_einfuegen, fenster_typ_aendern, wandaufbau_waehlen, sonnenschutz_setzen | 8, 15 |
| dach | 10 | dachform_aendern, dachneigung_aendern, gaube_hinzufuegen, dacheindeckung_waehlen | 14 |
| fassade | 6 | fassade_material_waehlen, schalung_art_waehlen, sockel_gestalten | 14.7 |
| bemusterung_interior | 13 | bodenbelag_waehlen, fliese_muster_fuge, treppe_bemustern, sanitaerobjekt_setzen | 12 |
| tga | 10 | steckdose_setzen, heizsystem_waehlen, waermepumpe_aufstellen, lueftung_waehlen | 13 |
| licht | 5 | leuchte_setzen, lichtschalter_setzen, lichtsteuerung_waehlen | 13.7 |
| pv | 4 | pv_belegen, pv_modul_waehlen, batteriespeicher_waehlen | 14.6 |
| aussenanlagen | 9 | terrasse_anlegen, zisterne_hinzufuegen, versickerung_waehlen, rueckstausicherung_waehlen | 14a |
| moeblierung | 6 | moebel_platzieren, raum_moeblieren, einbauschrank_planen | 12.3 |
| gebaeudetyp_nutzung | 8 | einliegerwohnung_hinzufuegen, anbauart_aendern, nutzerprofil_waehlen, kulturprofil_waehlen | 9a, 9b |
| steuerung | 12 | rueckgaengig, variante_anlegen, ansicht_wechseln, alternative_waehlen | 7.3 |
| anzeigen_auswerten | 12 | kosten_anzeigen, schall_anzeigen, masse_abfragen, begruendung_erfragen | 15, 9.5 |
| freigabe_prozess | 7 | zur_pruefung_senden, bemusterung_abschliessen, abweichung_beantragen, freigabe_erklaeren | 18 |
| meta | 6 | ki_transparenz, datenschutz_steuern, ausschluss_thema, unklar | 4.8, 9b.6 |
| **Summe** | **138** | | |

Jeder Intent trägt Beschreibung, Risikoklasse (10.2.5), mindestens drei deutsche Beispielsätze (zusammen 415), Slots mit Typ, Einheit, Wertebereich, Pflichtkennzeichen und Quelle (`parser`, `referenz`, `katalog`, `modell`; zusammen 316), die Fragen mit Schwellwert, die betroffenen Regel-IDs aus `regelkatalog.yaml` und `empfehlungen.yaml`, noch zu formalisierende Regeln (`regeln_geplant`), Module und Rückfragetext. Zwei Gestaltungsregeln folgen aus früheren Kapiteln.

**Der Gebäudetyp wird nicht gewählt.** Ein Etikett „Haustyp“ würde veralten, weil Gebäudeklasse und Profil aus Merkmalen folgen, die der Kunde im Entwurf ändert (Abschnitt 9a.2.1). Die Gruppe `gebaeudetyp_nutzung` ändert deshalb Merkmale (Einliegerwohnung, weitere Wohnung, Anbauart), und die Profilableitung folgt daraus. Diese Intents sind mindestens R2, das Zurücknehmen einer Wohnung ist R3.

**Freigaben gehen nicht per Sprache.** Der Intent `freigabe_erklaeren` erkennt Äußerungen wie „Ich gebe den Bauantrag frei“, führt sie aber nie aus, sondern öffnet das Freigabe-Gate der Oberfläche (E10.9).

> **Beispiel 10.1 (Katalogeintrag `kniestock_aendern`).** Gruppe `geschosse_baukoerper`, Risikoklasse R2.
>
> - **Slots:** `wert` (Länge, m, Wertebereich 0,0–2,5), `modus` (absolut, relativ_plus, relativ_minus; Quelle Parser), `staerke` (Stufe 1–5, nur ohne Zahlwert).
> - **Fragen:** `n.relativ` (noul, Schwelle 0,70; nur wenn der Parser keinen Modus erkennt) und `s.staerke` (score, fünf Stufen, Schwelle 0,60).
> - **Regeln:** `BY.BayBO.2-5.aF2007.Vollgeschoss`, `BY.BayBO.6.T`, `BY.BayBO.2-3.Gebaeudeklasse`, `BY.Profil.Schwellenwarnung`.
> - **Rückfrage:** „Auf welche Höhe soll der Kniestock? Ab {k_stern} wird das Dachgeschoss zum Vollgeschoss.“
>
> {k_stern} ist die Vollgeschoss-Schwelle aus Beispiel 4.2. Der Kunde erfährt in der Vorschau, die R2 ohnehin verlangt, und nicht erst nach der Änderung, dass sein Haus ein Geschoss zu viel hätte (ANF-09-19).

### 10.2.5 Kalibrierung und Schwellwerte

Ein Schwellwert ist nur so gut wie die Wahrscheinlichkeit, auf die er wirkt. Laya wird laut Model Card **unkalibriert** ausgeliefert; ohne Fine-Tuning liegt die Genauigkeit bei 0,342 bei einem Zufallsniveau von 0,318 (Recherche 03) [V]. „p = 0,9“ heißt vor der Kalibrierung nicht, dass das Modell in neun von zehn Fällen richtig liegt.

**Kalibrierungsfehler.** Gemessen wird der erwartete Kalibrierungsfehler (ECE) über *B* = 15 gleich breite Konfidenzintervalle $B_b$:

$$\mathrm{ECE} = \sum_{b=1}^{B} \frac{|B_b|}{n}\,\bigl|\,\mathrm{acc}(B_b) - \mathrm{conf}(B_b)\,\bigr|$$

Das Maß ist Standard der Kalibrierungsforschung; ein Literaturnachweis fehlt im Bestand [U].

**Temperaturskalierung.** Je Fragetyp wird eine Temperatur *T* bestimmt, die auf dem Entwicklungsset die negative Log-Likelihood minimiert: $\hat p_i = p_i^{1/T} / \sum_j p_j^{1/T}$. Das braucht nur Wahrscheinlichkeiten, keine Logits, und passt damit auch zum Jev-Protokoll; für noul gilt es für das Paar (p, 1 − p). *T* gehört zur Modellversion und steht im Protokoll.

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

Die Staffelung folgt den Fehlerkosten (Recherche 03): In R1 kostet ein Fehler einen Undo-Schritt, in R2 eine missverstandene Kostenfolge, in R3 unter Umständen eine verlorene Variante oder eine Erklärung gegenüber der Firma. Die Startwerte sind Designentscheidungen [U]; nach der Kalibrierung werden sie so gesetzt, dass die Fehlausführungsrate am Entwicklungsset die Ziele aus Tabelle 10.10 einhält. Die Rückfrage ist dabei die Enthaltung einer selektiven Vorhersage, berichtet wird das Paar aus Abdeckung und Fehlerrate.

> **E10.5 (Schwellen).** Schwellen gelten je Risikoklasse für kalibrierte Wahrscheinlichkeiten. Sie sind versionierte Konfiguration; jede Änderung von Schwelle oder Temperatur erzeugt eine neue Katalog- bzw. Modellversion.

## 10.3 Deterministischer Werteparser und Referenzauflösung

### 10.3.1 Warum ein eigener Parser

Jev und Laya liefern keine Werte wie „1,20 m“ oder „35 Grad“ (Recherche 03) [V]. Die Recherche nennt zwei Wege: einen deutschen Parser oder ein Sprachmodell mit JSON-Schema bzw. Constrained Decoding. Kakadoo parst strukturierte Befehle deterministisch und ruft das Sprachmodell nur für unscharfe Angaben wie „höher“ [@atakan2025kakadoo]. Die Arbeit geht weiter.

> **E10.6 (Werte).** Zahlwerte, Einheiten, Richtungen und Ordinale entstehen im Betrieb ausschließlich im deterministischen Werteparser. Ein Sprachmodell mit JSON-Schema wird nicht zur Wertgewinnung eingesetzt. Offline darf es Paraphrasen für Trainingsdaten erzeugen, die ein Mensch prüft (10.5.4). Unscharfe Angaben ohne Zahl ergeben eine Stufe der score-Frage und eine Vorschau, nie einen stillschweigend gesetzten Wert.

Ein Wert, der in Nachweis und Vertrag eingeht, muss auf eine Regel zurückführbar sein. Der Parser hat weder Zustand noch Zufall; `test_pipeline_deterministisch` bestätigt identische Protokolle bei wiederholter Verarbeitung.

### 10.3.2 Grammatik

`spezifikation/werteparser-grammatik.md` beschreibt den Parser in EBNF nach ISO/IEC 14977. Die **Wortebene** kennt fünf Muster für Maßausdrücke in fester Priorität: **A** „zwei Meter sechzig“ = 2,60 m; **B** Zahl mit Einheit („1,20 m“, „35 Grad“); **C** Umgangsmaß („eins zwanzig“ = 1,20 m, neu auch „eins null fünf“ und „einsachtzig“); **F** Produkt („vier mal sechs Meter“); **D** Zahl ohne Einheit. Dazu kommen Modus-, Richtungs-, Ordinal- und Anzahlausdrücke. Die **Morphemebene** zerlegt Zahlwörter wie „fünfunddreißig“ und erweitert B6 (bis 999) auf Tausender. Vierzehn Disambiguierungsregeln entscheiden Mehrdeutigkeiten, darunter:

- **D1 Tausenderpunkt:** Ein Punkt mit genau drei Ziffern danach trennt Tausender, sonst ist er Dezimaltrenner. „2.500 mm“ = 2,50 m, „1.20m“ = 1,20 m.
- **D3 Mehrdeutiges Umgangsmaß:** „eins fünf“ hat die Kandidaten 1,05 m und 1,50 m. Liegt nur ein Kandidat im Wertebereich des Slots, gilt er, sonst folgt eine Rückfrage.
- **D4 Einheit aus dem Slot:** „Dachneigung auf fünfunddreißig“ ergibt 35°, weil der Slot die Einheit Grad hat. Die ergänzte Einheit wird in der Interpretationsanzeige ausgewiesen.
- **D5 Nummer gehört zur Referenz:** In „Kinderzimmer 2 auf 3,20 m“ gehört die 2 zum Raum, nicht zum Wert.
- **D9 Komparativ macht relativ:** „zwanzig Zentimeter schmaler“ ergibt −0,20 m relativ. Bei Widerspruch gewinnt der Komparativ, und die Anzeige zeigt beide Lesarten.

Jeder Messwert trägt Textausschnitt, Muster, Herkunft der Einheit, Mehrdeutigkeit und Kandidaten. Von den zehn Dimensionen (Länge, Fläche, Winkel, Anteil, Leistung, Energie, Volumen, Farbtemperatur, U-Wert, Anzahl) kennt B6 die ersten drei.

### 10.3.3 Was B6 kann: neun Sätze, 16 Parserfälle

`tests/test_b6_b7.py` enthält 23 Tests: 16 Parserfälle, mehrdeutige Maße und Zahlwörter, Raumreferenzen, Annahme mit Ausgleich, Ablehnung, Fläche mit Rückfragen, Determinismus und BTLx (`beispiele/ergebnisse.md`). Am 27.09.2026 bestanden in der Arbeitsumgebung 22; der BTLx-Test (B7) wurde mangels `compas_timber` übersprungen.

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

Drei Äußerungen werden angenommen, zwei nach Regeln abgelehnt, drei zurückgefragt, eine ist nicht umgesetzt. Die Rückfragen haben drei Ursachen: unsichere Absicht, mehrdeutiger Wert, mehrdeutige Referenz. Alle lassen sich mit einer geschlossenen Frage klären.

Das Beispiel zeigt aber auch eine **implizite Annahme**: Bei „Mach das Kinderzimmer 2 auf 3,20 m“ setzt B6 stillschweigend die Breite, obwohl der Satz weder Breite noch Tiefe nennt und der Raum 3,50 × 3,40 m misst. Kapitel 5 hat dasselbe Vorgehen bei Chen et al., die fehlende Angaben nach „gesundem Menschenverstand“ ergänzen, kritisiert (Abschnitt 5.6.4) [@chen2025agent]. Das Testset erwartet hier die Rückfrage „Breite oder Tiefe?“ (T004, ANF-10-14). Voreinstellungen gibt es nur, wo der Katalog sie festlegt, etwa `standard: lichte_hoehe` bei `geschosshoehe_aendern`, und die Interpretationsanzeige weist sie aus.

### 10.3.4 Was B6 nicht kann: Messung am Testset

Das Testset enthält 76 Zahlslots, deren Wert im Satz steht. `parse_masse` aus B6 wurde am 27.09.2026 auf alle Sätze angewendet (`spezifikation/pruefe_sprache.py`). Richtig heißt: ein Messwert der richtigen Dimension mit genau dem Sollwert, bzw. bei Mehrdeutigkeit die Markierung (Tabelle 10.7).

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

Im eigenen Geltungsbereich liest B6 46 von 54 Werten richtig, über das ganze Testset 47 von 76. Die Fehler sind fehlende Regeln, jede ist in der Grammatik benannt. Zwei wiegen schwerer:

- **Tausenderpunkt.** „Die Terrassentür im Wohnzimmer 2.500 mm breit“ ergibt einen gültig aussehenden Wert von 0,0025 m, ebenso „1.250 mm“ 0,0013 m. Dieser stille Fehler hat die richtige Dimension; ihn fangen erst D1 und die Wertebereichsprüfung D13 (ANF-10-11).
- **Einheit fehlt.** Ohne D4 fehlt bei „Mach die Dachneigung auf fünfunddreißig“ der Wert, obwohl die Absicht klar ist.

Richtig gelöst ist dagegen „eins fünf“: B6 markiert die Mehrdeutigkeit; die Grammatik ergänzt nur die Kandidatenliste für die Rückfrage.

### 10.3.5 Referenzauflösung über das State-JSON

B6 löst Verweise wie „das Bad oben“ gegen ein kompaktes State-JSON auf, das je Raum GlobalId, Typ, Name, Geschoss, Zeile und Maße enthält. Die GlobalIds entstehen deterministisch per UUID-5 über `/haus/raeume/<id>` wie in B1 (Abschnitt 8.6.2). Gefiltert wird schrittweise nach **Raumtyp** (Synonyme: „Bad“, „Duschbad“, „Dusche“ → Bad), **Geschoss** („oben“ = höchstes Geschoss mit Kandidat, „unten“ = niedrigstes, „OG“, „EG“), **Nummer oder Ordinal** und **Größe**. Ergebnis ist eine GlobalId, „mehrdeutig“ mit Kandidaten oder „keine“.

Im Testset löst B6 55 von 58 Raumslots richtig auf (ohne Kontextfälle). Die drei Fehler zeigen zwei fehlende Kriterien:

- **Name vor Typ.** „Die Diele“ ergibt „mehrdeutig“, weil „Diele“ als Synonym für Flur gilt und es zwei Flure gibt; der Raum im Erdgeschoss heißt aber „Diele“.
- **Mengen.** „In jedes Kinderzimmer zwei Netzwerkdosen“ meint beide Kinderzimmer; Quantoren machen aus der Mehrdeutigkeit eine Menge.

Darüber hinaus verlangt das Testset den **Dialogkontext** („Mach es zwanzig Zentimeter breiter“ nach „Wie breit ist das Bad oben?“; ob der Kontext gilt, entscheidet `n.bezug_vorher`, welches Objekt, der Code) und **Relationen** („die Wand zwischen Bad und Kinderzimmer 1“ über `IfcRelSpaceBoundary`, Kapitel 8). Katalogartikel findet eine deterministische unscharfe Suche in der Projektbibliothek (Kapitel 12); mehr als ein Treffer führt zur Rückfrage mit höchstens fünf Kandidaten.

> **E10.7 (Referenzen).** Referenzen werden nur deterministisch gegen den Modellzustand aufgelöst, in der Reihenfolge exakter Name, Typ, Geschoss, Nummer, Größe, Relation, Dialogkontext. Bei Mehrdeutigkeit fragt das System zurück und wählt nie den „wahrscheinlichsten“ Raum. Quantoren erzeugen Mengen. Ergebnis ist immer eine GlobalId oder eine Liste davon.

## 10.4 Dialogsteuerung, Fehlerbehandlung und Transparenz

### 10.4.1 Zustände einer Äußerung

Jede Äußerung endet in genau einem von acht Ergebnissen (Tabelle 10.8; Häufigkeiten aus der Spalte `erwartet` des Testsets).

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

Die Prüfreihenfolge ist fest: Intent-Schwellen, dann Vollständigkeit und Eindeutigkeit von Slots und Referenzen, dann Regeln. Eine Ablehnung betrifft deshalb immer eine eindeutig verstandene Absicht.

### 10.4.2 Rückfrage ist nicht Ablehnung

Kapitel 9 verlangt, Rückfragen zur Absicht von Ablehnungen nach Regeln zu trennen (ANF-09-15). Die **Rückfrage** klärt die Absicht; sie hat keine Regel, keinen Nachweis und keinen roten Status, ihr Text steht im Feld `rueckfrage` („Welchen Raum meinen Sie: Duschbad EG oder Bad OG?“). Die **Ablehnung** ist eine Aussage über den Entwurf mit Konfliktmenge, Begründung, Quelle, Alternative und rotem Nachweis (Abschnitt 9.5.1, ANF-09-16).

Die Alternative ist die gemeinsame Projektion auf alle Regeln. Bei „Mach das Kinderzimmer 1 einen Meter zwanzig schmaler“ bindet nicht die zuerst gemeldete Mindestbreite, sondern die Mindestfläche: „höchstens 0,55 m schmaler (2,95 m; 10,03 m²)“ (ANF-09-13). Der Kunde übernimmt sie mit `alternative_waehlen` („Dann nimm das“).

Alle Texte stammen aus dem Katalog. Ein meinungsgeprägter Schreibassistent verschob bei 1.506 Teilnehmenden auch die später erhobene Einstellung [@jakesch2023cowriting]; Kapitel 9b schließt deshalb Laufzeittexte aus Sprachmodellen aus (ANF-09b-09). Erklärungen sind kontrastiv und selektiv [@miller2019explanation]. Weil Vollständigkeit wichtiger ist als Genauigkeit und starke Vereinfachung Vertrauen kostet [@kulesza2013explanations], nennt eine Ablehnung alle Regeln der Konfliktmenge.

> **E10.8 (Dialog).** Rückfrage und Ablehnung sind getrennt dargestellt. Eine Rückfrage ist geschlossen mit höchstens fünf Optionen; nach zwei erfolglosen Rückfragen folgt die Auswahl am Bildschirm. Alle Texte kommen aus dem Katalog.

### 10.4.3 Fehlertoleranz

Fehler müssen sichtbar, billig und umkehrbar sein. Dazu dienen fünf Mechanismen:

1. **Interpretationsanzeige** „Bad (OG) · Breite · 2,60 m (absolut)“ mit markierten Ergänzungen, zugleich das wichtigste Transparenzmittel (10.4.4).
2. **Undo per Sprache** („Mach das rückgängig“, „Nimm das zurück“). Weil jede R1-Änderung mit einem Schritt umkehrbar ist, darf ihre Schwelle niedriger liegen.
3. **Korrektur im Satz** („Nein, nicht das Bad, das Kinderzimmer 1“) über `n.korrektur` als Ersetzung eines Slots im vorigen Frame; das Testset enthält je drei Korrektur- und Anapherfälle.
4. **n-beste Hypothesen mit Kontextfilter** (10.1.2) [@kou2010knowledge].
5. **Automatische Variante vor R3**, damit der Rückweg auch ohne Undo-Stapel offen bleibt.

Bewusst **nicht** eingesetzt wird die Klickbestätigung jeder Änderung. Sie entwertet die Sprache und wird zur Routine: Complacency und Automation Bias treten bei Laien und Experten auf und lassen sich durch Übung oder Anweisung nicht beseitigen [@parasuraman2010complacency]. Bestätigt wird nur, wo die Bestätigung einen Inhalt hat, nämlich die Folgenvorschau in R2; R3 ist ein eigener Bildschirmschritt.

> **E10.9 (Rechtserhebliche Erklärungen).** Freigaben, Unterschriften, Bestellungen und der Abschluss einer Bemusterungskategorie werden nie per Sprache ausgeführt. Die Sprache kann den Schritt anstoßen, erklärt wird er am Bildschirm mit dem Freigabe-Gate aus Kapitel 18.

### 10.4.4 Transparenz nach Art. 50 KI-VO

Gebäudeentwurf ist keine Hochrisiko-Anwendung der KI-Verordnung (Kapitel 4.8.2) [@aiact2024], auch nicht über Anhang I (Recherche 27). Es bleiben Art. 50 und die durch die Omnibus-Verordnung abgeschwächte Pflicht zur KI-Kompetenz nach Art. 4 [@eu2026omnibus]. Für Art. 50 Abs. 1, nach dem Nutzer die Interaktion mit einem KI-System erkennen müssen, gilt:

- **Hinweis bei der ersten Aktivierung des Mikrofons** mit festem Katalogtext: „Ihre Sprache wird von einer KI verstanden. Die KI erkennt nur, was Sie ändern möchten. Maße, Regeln, Kosten und Nachweise berechnet ein festes Programm. Sie sehen vor jeder Änderung, was verstanden wurde.“
- **Dauerhaftes Symbol** während der Spracheingabe, dazu die Interpretationsanzeige (10.4.3).
- **Auskunft auf Nachfrage** über den Intent `ki_transparenz` („Rede ich hier mit einem Computer?“, „Wer entscheidet hier eigentlich?“), ebenfalls mit festem Text.

Art. 50 Abs. 2 verlangt die maschinenlesbare Kennzeichnung synthetischer Audio- und Textinhalte, für Altsysteme ab dem 02.12.2026 [@eu2026omnibus]. Die App erzeugt keine Texte mit Sprachmodellen; ob das Vorlesen fester Katalogtexte per Sprachsynthese darunter fällt, ist ungeklärt [U]. Eine Sprachausgabe wird bis zur Klärung gekennzeichnet (ANF-10-22). Funktional macht die Interpretationsanzeige den Fehler des Modells sichtbar, bevor er zum Fehler im Modell wird; Rechtspflicht und Fehlertoleranz fallen zusammen.

> **E10.10 (Interpretationsanzeige).** Jede ausgeführte oder vorgeschaute Änderung zeigt den verstandenen Frame in Klartext. Ergänzte Einheiten und Voreinstellungen sind gekennzeichnet.

### 10.4.5 Datenschutz

Sprachaufnahmen sind personenbezogene Daten (Kapitel 4.8.3). Nach den EDPB-Leitlinien ist die Speicherung zu begrenzen, versehentliche Aufnahmen sind zu löschen, und Stimmdaten sind nur bei Identifizierung biometrisch [@edpb2021vva]. Für den Mikrofonzugriff gilt § 25 TDDDG mit Ausnahme bei unbedingter Erforderlichkeit [@tdddg25]. Die DSK verlangt datenschutzfreundliche Voreinstellungen und keine automatisierte Letztentscheidung [@dsk2024ki].

> **E10.11 (Datenschutz).** Spracherkennung und Intent-Modell laufen lokal. Rohaudio wird nicht über die Sitzung hinaus gespeichert, protokolliert werden nur Transkript, Hypothesen und Frame. Es gibt keine Sprechererkennung. Aufnahmen dienen Training und Evaluation nur mit gesonderter Einwilligung. Jev erhält nur Transkripte, mit Zero Data Retention und Einwilligung. Beratungsgespräche werden nur mit Einwilligung aller Beteiligten aufgezeichnet [@stgb201].

Die menschliche Letztentscheidung betrifft auch die Ablehnung: Nach dem SCHUFA-Urteil kann eine automatisierte Bewertung eine Entscheidung nach Art. 22 DSGVO sein, wenn ein Vertragsschluss maßgeblich von ihr abhängt [@eugh2023schufa]. Zu jeder Ablehnung bietet der Dialog deshalb `abweichung_beantragen` an. Der Wunsch wird zur menschlichen Prüfung vorgemerkt (Anfechtungsweg nach Recherche 27); entscheiden Behörde oder Firma, nicht die App.

Sprache hilft Menschen mit motorischen Einschränkungen [@elghaish2022voice], schließt aber Menschen mit Sprech- oder Hörbeeinträchtigung aus, wenn sie der einzige Weg ist. Unter dem Barrierefreiheitsstärkungsgesetz (Kapitel 4.8.3) [@bfsg] muss jede Funktion auch ohne Sprache erreichbar sein (ANF-10-25).

## 10.5 Evaluationsdesign

### 10.5.1 Testset

NL-BIM-Datensätze sind englisch, evaluiert wird meist mit Fachleuten (Lücken L7, L8). IFC-Bench deckt nur Abfragen ab [@hellin2026bim], und über 61 BIM-LLM-Studien finden Park et al. eine industrielle Validierung in nur 44,3 % der Fälle [@park2026bimllm]. Das eigene Testset `spezifikation/sprach-testset.jsonl` umfasst 216 Sätze über alle 138 Intents. Jeder Eintrag nennt Satz, Gruppe, Intent, Slots in SI-Einheiten, für Raumslots die `raum_id` im Referenzzustand `beispiele/daten/haus_state.json` oder die erwartete Mehrdeutigkeit, das erwartete Ergebnis nach Tabelle 10.8, die Risikoklasse, Kategorien und gegebenenfalls einen Dialogkontext. Die Kategorien umfassen unter anderem 40 Sätze mit Fachbegriffen, 22 mit Zahlwörtern, 18 Abfragen, 9 vage Angaben, je 3 mit Dialekt, Erkennungsartefakten, Korrekturen und Anaphern sowie die 9 B6-Sätze. Testsätze dürfen keine Beispielsätze des Katalogs sein; der Validator fand bei der ersten Prüfung 42 solche Leckagen, die durch Umformulierung beseitigt wurden. Das Textset setzt ein korrektes Transkript voraus; für die Spracherkennung wird es zum Audio-Testset erweitert (10.5.3).

### 10.5.2 Messgrößen

Die Zielwerte in Tabelle 10.10 sind Designentscheidungen [U], festgelegt vor der Messung.

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

Die **Fehlausführungsrate** zählt mehr als die Accuracy: Eine falsche Ausführung richtet Schaden an, eine Rückfrage kostet Zeit. Berichtet wird deshalb immer das Paar aus Abdeckung und Fehlausführungsrate. Statt pass@k, das für Codegeneratoren gedacht ist, empfiehlt Recherche 12 Intent-Accuracy@1/@3 und Slot-F1 je Ebene. Die **Slot-F1** deterministischer Slots kann auf den von der Grammatik abgedeckten Kategorien 1,0 erreichen; ein Wert darunter ist ein Implementierungsfehler. Tabelle 10.7 ist die Ausgangsmessung für B6.

### 10.5.3 Studiendesign

Die Evaluation hat drei Stufen.

1. **Textstufe.** Das Textset läuft bei jeder Änderung von Katalog, Grammatik oder Modell (ANF-10-26), verglichen werden Schlüsselwortklassifikator, Laya ohne und mit Fine-Tuning sowie Jev als externer Vergleich (nur mit dem Textset, das keine personenbezogenen Daten enthält).
2. **Audiostufe.** Jeder Satz wird von mindestens 12 Sprecherinnen und Sprechern (Hochdeutsch und regionale Färbung) in zwei Umgebungen (ruhig, Wohnraum mit Hintergrundgeräusch) aufgenommen, also mindestens 2.592 Aufnahmen mit Einwilligung (E10.11). Gemessen werden WER, Fachbegriff- und Zahlfehlerrate für Voxtral, Parakeet mit Boosting und Whisper mit Hotwords (E10.1). Synthetische Sprache dient nur der Trainingsaugmentation.
3. **Nutzerstudie.** Laien lösen Aufgabenkarten wie „Bad vergrößern, Dachgaube hinzufügen“, ein Muster nach Recherche 12 in Anlehnung an Niemeijer [@niemeijer2011constraint], je einmal per Sprache und per Direktbedienung in ausbalancierter Reihenfolge wie bei Dahlem et al. [@dahlem2026comparing]. Gemessen werden Erfolg, Zeit, Dialogrunden, Rückfragen und Abbrüche, die Gebrauchstauglichkeit nach ISO 9241-11 [@iso2018usability], SUS [@brooke1996sus; @lewis2018system] und BUS-15, ein Instrument für Konversationsagenten mit Reliabilität 0,76 bis 0,87, aber ohne deutsche Fassung [@borsci2022chatbot]. Formative Runden mit fünf Personen finden rund 80 % der Probleme [@virzi1992subjects]; die summative Stichprobe legt Kapitel 20 fest.

Die Studie prüft auch, ob sich Sprache bei zusammengesetzten und der Schieberegler bei einzelnen Parametern lohnt [@chen2025agent]; ein Vorteil der Direktbedienung wäre ein Gestaltungshinweis, kein Misserfolg. VISA4D klassifizierte 71 von 80 baubezogenen Sprachbefehlen (89 %) richtig und ergänzte eine Befragung [@jaff2025visa4d]; das ist das nächste Evaluationsmuster aus dem Bauwesen.

### 10.5.4 Fine-Tuning-Plan für Laya

Ohne Fine-Tuning liegt Laya nahe am Zufallsniveau (10.2.5); Tabelle 10.11 zeigt den Weg zur Abnahme.

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

Der Plan übernimmt aus T2S4BIM die synthetischen Trainingsdaten und den Befund, dass kleinere Modelle mit größeren mithalten [@wei2025texttostructure]. Aus der Konfiguratorforschung stützen Wang et al. das Muster: Ein leichter Klassifikator bildet vage Bedarfsbeschreibungen so gut auf Attribute ab wie aufwendigere Verfahren [@wang2022natural]. Die Hierarchie begrenzt zudem den Aufwand, weil ein neuer Intent nur die Frage seiner Gruppe ändert.

## 10.6 Grenzen und Zwischenfazit

**Grenzen.** Erstens ist die Intent-Schicht nicht gemessen: Alle Wahrscheinlichkeiten in B6 sind Stub-Werte, und keine Aussage über die Güte von Laya, Jev oder Voxtral stammt aus eigener Messung; die Modelle sind erst seit etwa Mitte September 2026 öffentlich (Recherche 03) [V]. Zweitens deckt B6 nur einen Intent ab; der Katalog ist Spezifikation, nicht Implementierung. Drittens stammt das Testset von einem Autor und bildet die Sprache der Kunden nur so weit ab, wie er sie vorhersieht (DAT-10-02). Viertens sind Zielwerte, Schwellen und Latenzbudget empirisch ungeprüfte Designentscheidungen. Fünftens fehlt ein Literaturnachweis für den ECE.

**Zwischenfazit.** Das Kapitel beantwortet FF3 in vier Punkten:

1. **Das Modell wählt, der Code bestimmt.** Das Intent-Modell beantwortet nur typisierte Fragen über geschlossene Optionen, mit 112 choice-, 11 score- und 15 noul-Fragen im Katalog. Werte, Referenzen, Katalogartikel, Geometrie und Regeln entstehen im Code. Damit ist die Aufgabenteilung strenger als in allen Vergleichssystemen aus Kapitel 5 (Lücke L6).
2. **Zuverlässigkeit entsteht durch Enthaltung, nicht durch Treffsicherheit allein.** Kalibrierte Wahrscheinlichkeiten und Schwellen je Risikoklasse entscheiden zwischen Ausführen, Vorschau, Bildschirmbestätigung und Rückfrage. Rechtserhebliches geht nie per Sprache.
3. **Der deterministische Teil ist prüfbar und schnell.** B6 liest innerhalb seines Geltungsbereichs 46 von 54 Werten richtig, löst 55 von 58 Raumreferenzen auf und braucht dafür im Median 0,13 ms. Jeder gemessene Fehler entspricht einer benannten Regel der Grammatik.
4. **Die deutsche Sprachschnittstelle für den Hausentwurf ist spezifiziert** (Lücke L7): 16 Gruppen, 138 Intents, 415 Beispielsätze, eine Grammatik mit 58 Regeln und 14 Disambiguierungsregeln sowie ein Testset mit 216 Sätzen. Die empirische Prüfung folgt dem Plan in 10.5 und ist Gegenstand von Kapitel 20.

## 10.7 Umsetzungsvorgaben für die App

Es gelten die Regeln aus Kapitel 3.7: „Muss“ verhindert einen Rechts-, Nachweis- oder Fehlausführungsfehler, „Soll“ erhöht Qualität oder Nutzen. Testfälle T*nnn* stehen in `spezifikation/sprach-testset.jsonl`.

### 10.7.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/intents.yaml` | Intent-Katalog v0.1.0: Risikoklassen mit Schwellen, 5 globale Fragen, 29 Slottypen, 60 Fachbegriffe mit Varianten, 16 Gruppen mit je einer Intent-Frage und zusammen 138 Intents (je Beschreibung, Risikoklasse, ≥ 3 Beispielsätze, Slots mit Typ, Einheit, Wertebereich und Quelle, Fragen mit Schwelle, Regel-IDs, geplante Regeln, Module, Rückfragetext) |
| `spezifikation/werteparser-grammatik.md` | EBNF der Wort- und Morphemebene (58 Regeln), Einheitentabelle, Disambiguierungsregeln D1–D14, Slotzuordnung, 20 Referenzfälle mit dem heutigen B6-Ergebnis |
| `spezifikation/sprach-testset.jsonl` | 216 Testsätze mit erwarteter Gruppe, erwartetem Intent, Slots, Ergebnis, Risikoklasse, Kategorien und gegebenenfalls Dialogkontext; Referenzzustand `beispiele/daten/haus_state.json` |
| `spezifikation/pruefe_sprache.py` | Validator und Messung: Struktur des Katalogs, höchstens 19 Optionen, Regel-IDs gegen `regelkatalog.yaml` und `empfehlungen.yaml`, Testset gegen Katalog, Leckage, EBNF-Konsistenz, Messung von B6 |

**Prüfung** (Python 3.11.15, PyYAML 6.0.1, 27.09.2026; `python spezifikation/pruefe_sprache.py` aus `arbeit/`):

- **Katalog:** 16 Gruppen, 138 Intents, 415 Beispielsätze, 316 Slots, Fragen 112 choice, 15 noul, 11 score, höchstens 18 Optionen je choice-Frage. Risikoklassen R0 29, R1 75, R2 27, R3 7. Alle Regel-IDs existieren.
- **Testset:** 216 Sätze, 138 Intents abgedeckt, keine Leckage.
- **Grammatik:** 2 EBNF-Blöcke, 58 Regeln, alle verwendeten Nichtterminale definiert.
- **Messung B6:** Werteparser 47 von 76 Zahlslots, Raumreferenz 55 von 58.
- **Fehler: 0.**

Eine Gegenprobe mit undefiniertem Nichtterminal wurde als Fehler gemeldet. Neue Regeln nach `regel.schema.json` entstehen nicht; `regeln_geplant` ist in den Kapiteln 12 bis 15 zu formalisieren.

### 10.7.2 Anforderungen

**Spracherkennung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-01 | Muss | Spracherkennung lokal und im Strom; Endtranskript ≤ 0,8 s nach Sprechende. | 10.1.4, E10.1 | Aufnahme von T001 auf Zielhardware: Teiltranskript vor Sprechende sichtbar, Endtranskript ≤ 0,8 s danach, kein Netzwerkverkehr. |
| ANF-10-02 | Muss | ASR liefert ≥ 3 Hypothesen mit Konfidenz und Wortzeiten; Modell per Konfiguration austauschbar. | 10.1.2 | Umschalten Voxtral → Whisper ohne Codeänderung; beide liefern `nbest[≥3]`, `konfidenz`, `woerter[].start/ende`. |
| ANF-10-03 | Muss | Fachbegriffe aus `fachbegriffe` als Boosting-Liste; deterministische Nachkorrektur mit Protokoll. | 10.1.3 | T034 „Den Knie Stock auf eins zwanzig“ ⇒ „Kniestock“, Protokoll `nachkorrektur`; Intent `kniestock_aendern`, 1,20 m. |
| ANF-10-04 | Muss | Das Mikrofon ist nur nach Nutzeraktion aktiv (Push-to-talk); der Status ist sichtbar. | E10.2 | Ohne Tastendruck keine Audiodaten im Puffer (Test mit Mikrofonattrappe); Statussymbol wechselt innerhalb von 100 ms. |

**Intent-Erkennung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-10-05 | Muss | Das Intent-Modell beantwortet nur Katalogfragen; Antworten außerhalb der Optionen werden verworfen. | 10.2.1 | Attrappe liefert „dach_loeschen“ (nicht im Katalog) ⇒ `rueckfrage_intent`, Protokoll „Option unbekannt“. |
| ANF-10-06 | Muss | Der Katalog wird beim Start validiert; jede choice-Frage hat höchstens 19 Optionen. | 10.2.3, 10.7.1 | `pruefe_sprache.py` meldet 0 Fehler. Kopie mit einer choice-Frage mit 20 Optionen ⇒ Ladefehler „> 19 Optionen“. |
| ANF-10-07 | Muss | Hierarchie Gruppe → Intent → Slotfragen, zwei Gruppen parallel unter der Gruppenschwelle, Kontextfilter. | 10.2.3, E10.4 | „Ja, genau so“ (T177) mit offener Rückfrage ⇒ `bestaetigen`; derselbe Satz ohne offene Rückfrage ⇒ `bestaetigen` nicht unter den Optionen, Ergebnis `rueckfrage_intent`. |
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
| ANF-10-15 | Muss | Referenzauflösung gegen das State-JSON nach E10.7; Ergebnis GlobalId oder Liste. | 10.3.5, E10.7 | Alle 58 Raumslots des Testsets ohne Kontextfälle richtig (B6: 55); „Die Diele zwanzig Zentimeter schmaler“ (T018) ⇒ `3VNmzLkorKaPT3n1GT$V3f`; „In jedes Kinderzimmer …“ (T114) ⇒ beide Kinderzimmer. |
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
| ANF-10-24 | Muss | Jede Äußerung wird als Frame nach Tabelle 10.12 protokolliert und ist ohne Modell reproduzierbar. | 10.3.1, 4.8.1 | Protokoll nach Tabelle 10.12 für T001; Wiedergabe mit den protokollierten Modellantworten ergibt bitgleichen Frame und Zustand (Erweiterung von `test_pipeline_deterministisch`). |
| ANF-10-25 | Muss | Jede Funktion, die per Sprache erreichbar ist, ist auch ohne Sprache erreichbar. | 10.4.5 | Abbildungstest: Für jeden der 138 Intents existiert ein Bedienpfad der Oberfläche; fehlender Pfad ⇒ Testfehler. |
| ANF-10-26 | Soll | Das Textset läuft bei jeder Änderung von Katalog, Grammatik oder Modell; die Abnahme folgt den Zielwerten aus Tabelle 10.10. | 10.5 | CI-Lauf erzeugt Bericht mit Intent-Accuracy@1/@3, Slot-F1, Frame-Accuracy, ECE, Abdeckung und Fehlausführungsrate je Risikoklasse; Unterschreitung eines Zielwerts ⇒ Freigabe gesperrt. |
| ANF-10-27 | Soll | Fine-Tuning und Kalibrierung von Laya sind reproduzierbar dokumentiert (Datensatz-Hash, Katalogversion, Modell-Hash, *T*). | 10.5.4 | Abnahmebericht nennt alle vier Werte; Leckageprüfung Testset ↔ Trainingsdaten: 0 Treffer. |
| ANF-10-28 | Soll | Unscharfe Stärkeangaben ergeben eine Stufe der score-Frage und immer eine Vorschau; die Schrittweite je Stufe ist Konfiguration. | D10, 10.2.2 | „Mach des Bad oben a bissl größer“ (T013) ⇒ Stufe 1, Vorschau mit der konfigurierten Schrittweite der Stufe 1, gekennzeichnet als Voreinstellung; keine Änderung ohne Bestätigung. |

### 10.7.3 Datenstrukturen

Tabelle 10.12 beschreibt den Frame je Äußerung; er erweitert `beispiele/ausgabe/intent_protokoll.json`.

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

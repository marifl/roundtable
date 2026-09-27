# 25 Schneeballverfahren Runde 1, Teil B: FF3, FF5, FF6

Status: v0.1 (27.09.2026). Diese Recherche setzt Protokoll 2a.3 Nr. 3 und 2a.6 Schritt 4 um (`../arbeit/02a-review-protokoll.md`): eine Runde Schneeballverfahren nach Wohlin (2014), rückwärts (Referenzen der Startquelle) und vorwärts (zitierende Arbeiten). Teil A (FF1, FF2, FF4) steht in `24-schneeball-ff1-ff2-ff4.md`. Die 175 neuen Quellen stehen in `../arbeit/literatur/lit-I-schneeball-b.bib`. Überschneidende Startquellen wurden hier ebenfalls bearbeitet, aufgenommen sind aber nur Kandidaten mit Bezug zu FF3, FF5 oder FF6.

**Prüfweg.** Semantic Scholar, OpenAlex und Crossref sind direkt gesperrt (Proxy 403); der Exa-Fetch liefert für Semantic Scholar keine JSON-Antwort. Referenzen und Zitierende stammen deshalb aus OpenAlex (`api.openalex.org/works?filter=cited_by:…` bzw. `cites:…`), abgerufen über den Exa-Fetch. Metadaten und Abstracts kommen aus dem OpenAlex-Record (DOI-Filter), für Tagungsbände und Buchkapitel zusätzlich aus Crossref (Exa-Fetch). Wo OpenAlex kein Abstract führt, wurde es bei zentralen Quellen über Verlags- oder Repositoriumsseiten nachgelesen (Exa-Suche). Die Existenz jeder aufgenommenen Quelle ist über ihren DOI-Record belegt; das `note`-Feld nennt den Prüfweg.

**Dublettenabgleich.** Jeder Kandidat wurde über DOI und normalisierten Titel gegen `quellen-master.csv` und alle `.bib`-Dateien geprüft, einschließlich `lit-I-schneeball-a.bib` (Stand 27.09.2026, 17:47). Fünf Quellen, die beide Teile gefunden haben, führt Teil A laut seinem Kopfkommentar nur hier (`piazzi2022graphical`, `abualdenien2020consistent`, `vareilles2013renovation`, `jalaliyazdi2021clt`, `mellenthinfilardo2026requirements`). Eine DOI-Überschneidung zwischen Teil A und Teil B besteht nicht; Keys kollidieren nicht.

**Legende.** Passung 0–3 je FF nach 2a.5 (vorläufig, Einzelbewertung steht aus). R = rückwärts, V = vorwärts. [U] = Teilangabe unsicher (Grund im `note`-Feld).

---

## Ergebnis in 5 Punkten

1. **FF3: Die Übersetzung von Freitext in Konfiguratorparameter ist außerhalb des Bauwesens erprobt, im Bauwesen kaum industriell validiert.**
   - Wang et al. (2022) konfigurieren Produkte direkt aus natürlichsprachlichen Beschreibungen (Text-Embeddings + MLP); Huang et al. (2024) und Wang et al. (2021, zwei Arbeiten) schließen die „semantische Lücke“ zwischen Kundenbedarf und Spezifikation. Diese Linie fehlte im Bestand und stützt die Intent-Schicht direkt.
   - Im Bauwesen: Sprachassistent für BIM-Daten (Elghaish et al. 2022), LLM-formalisierte Änderungsstrategien für code-konforme Bauteiländerungen (Wu et al. 2026), Jang & Lee (2024) als Vorläufer von NADIA.
   - Das Review von Park et al. (2026) über 61 BIM-LLM-Studien findet 70,5 % technische, aber nur 44,3 % industrielle Validierung.
   - Allgemeine KI-Evidenz für „KI versteht, Code entscheidet“: PAL (Gao et al. 2023) lagert das Rechnen an einen Interpreter aus und übertrifft damit auf GSM8K PaLM-540B mit Chain-of-Thought um 15 Prozentpunkte (top-1); Toolformer (Schick et al. 2023) lernt Werkzeugaufrufe. Li et al. (2024) belegen systematische Schwächen von LLMs beim räumlichen Schließen.
2. **FF5: Die Zeitwirkung von Konfiguratoren ist großzahlig belegt; im Fertigbau ist sie nicht selbstverständlich.**
   - Trentin et al. (2011): Konfiguratoreinsatz verbessert die Zeitperformance in 238 Werken aus drei Branchen und acht Ländern. Hvam et al. (2006) zeigen den Effekt auf den Angebotsprozess, Campo Gay et al. (2026) im Längsschnitt auf die Qualität von Bauspezifikationen.
   - Gegenbefund: In der Mehrfallstudie von Chen et al. (2023) erreichten 66,7 % der Fertigbauprojekte eine schlechte Bauzeitperformance; entscheidend waren Technik- und Abwicklungssystem.
   - Laien-Evaluation mit Wohnbezug: GUI für Co-Design im Wohnungsbau (Raposo et al. 2024), Längsschnitt-Usability einer Hausentwurfs-Pipeline über Web, VR und AR (Sužnjević et al. 2025), Grundrisspräferenzen von Architekten vs. Laien (Boumová & Zdráhalová 2016). Instrument für die Sprachschnittstelle: Chatbot Usability Scale (Borsci et al. 2022).
   - Gestaltungsprinzipien für Kunden-Toolkits: Randall et al. (2005), von Hippel (2001), von Hippel & Katz (2002).
3. **FF6: Für Schall, Dach und Reifegrade gibt es übernehmbare, regelbasierte Bausteine.**
   - Schall im Holzbau: Aus IFC-Modellen früher Phasen werden 15 akustisch unterscheidbare Stoßstellentypen per Topologie und Regeln erkannt (Châteauvieux-Hellwig et al. 2022), fortgeschrieben im Bauphysik-Kalender 2025.
   - Dach: gewichtete Straight Skeletons für unterschiedliche Neigungen (Held & Palfrader 2017; Biedl et al. 2015), robuste CGAL-Implementierung mit exakter Arithmetik (Eder et al. 2021), graphbasierte Dachtopologie (Ren et al. 2021).
   - Reifegrade: DIN EN ISO 7817-1:2024 (LOIN) und ISO 23387:2020 fehlten im Bestand. Leite et al. (2011) messen den Modellierungsaufwand je Detaillierungsgrad; Mellenthin Filardo et al. (2026) beschreiben die Praxis in Deutschland.
   - Bemusterung/Produktdaten: Herstellerdaten per Semantic Web (Kebede et al. 2022), Katalog-Modell-Kopplung (Costa & Madrazo 2015); TGA-Vorfertigung (Lopez et al. 2022; Zhao et al. 2025).
4. **FF6 Architekturpsychologie: Empfehlungen lassen sich an rechenbare Maße binden.**
   - Isovist-Kennwerte sagen Bewegung und Erleben voraus (Wiener et al. 2007; Dosen & Ostwald 2017); Hwang & Lee (2018) leiten Fensterplanung parametrisch aus Prospect-Refuge ab.
   - Licht: melanopische Beleuchtungsstärke als Wirkgröße (Brown 2020), Rechenwerkzeug luox (Spitschan et al. 2021), Abendlicht in Wohnungen (Cain et al. 2020). Lärm: Nutzen einer ruhigen Fassadenseite (Öhrström et al. 2006; Bodin et al. 2015).
   - Critiquing in der Architektur (Oh et al. 2008, 2010) und die Küchenplanung JANUS (Fischer et al. 1989) sind Vorbilder für Empfehlungen mit Begründung. Kulturprofile: Hong et al. (2016) prüfen ein Feng-Shui-Modell im Schlafraum empirisch.
5. **Sättigung ist nicht erreicht.** Nur 42 von 257 Kandidaten (16%) waren schon im Bestand; die Runde lieferte 175 neue Quellen mit Relevanz ≥ 2, davon 19 mit Relevanz 3. Nach 2a.3 Nr. 3 ist eine zweite Runde nötig (Abschnitt E).

---

## A Startmenge

Auswahlregel: `kern = ja` und `art = W` und (max(ff3, ff5, ff6) = 3 oder (max(ff3, ff5, ff6) ≥ 2 und P ≥ 6)), angewandt auf `quellen-bewertung.csv` (Stand 17:29, 530 Zeilen). Ergebnis: **38 Startquellen**. Acht davon (Q477–Q502, alle FF5) kamen erst mit Bewertung Teil 5 hinzu und wurden nachträglich bearbeitet.

| ID | Key | ff3 | ff5 | ff6 | P | Titel (gekürzt) |
|---|---|---|---|---|---|---|
| Q027 | `du2026text2bim` | 3 | 0 | 0 | 5.5 | Text2BIM: Generating Building Models Using a Large Language Model-Base |
| Q103 | `trentin2013sales` | 1 | 3 | 0 | 5.5 | Sales configurator capabilities to avoid the product variety paradox:  |
| Q110 | `schoenwitz2017product` | 0 | 1 | 3 | 6.5 | Product, process and customer preference alignment in prefabricated ho |
| Q118 | `randall2007user` | 3 | 1 | 0 | 5.5 | User Design of Customized Products |
| Q123 | `lee2024generalized` | 3 | 0 | 0 | 5.0 | A Generalized LLM-Augmented BIM Framework: Application to a Speech-to- |
| Q213 | `kwiecinski2019customers` | 0 | 3 | 1 | 5.5 | Customers Perspective on Mass-customization of Houses |
| Q227 | `johnsson2009defects` | 0 | 3 | 0 | 5.5 | Defects in offsite construction: timber module prefabrication |
| Q234 | `chateauvieux2023bim` | 0 | 0 | 3 | 6.5 | BIM-gestützter Planungsprozess zur Berechnung des Schallschutzes im Ho |
| Q242 | `wang2019automatic` | 0 | 3 | 0 | 5.5 | Automatic Material Estimation by Translating BIM Data into ERP Readabl |
| Q275 | `kodnongbua2024zeroshot` | 3 | 1 | 0 | 5.0 | Zero-shot Sequential Neuro-symbolic Reasoning for Automatically Genera |
| Q290 | `aichholzer1995novel` | 0 | 0 | 3 | 6.5 | A Novel Type of Skeleton for Polygons |
| Q292 | `kelly2011interactive` | 0 | 0 | 3 | 6.5 | Interactive architectural modeling with procedural extrusions |
| Q294 | `abualdenien2019metamodel` | 0 | 0 | 3 | 6.5 | A meta-model approach for formal specification and consistent manageme |
| Q295 | `abualdenien2022levels` | 0 | 0 | 2 | 6.0 | Levels of detail, development, definition, and information need: a cri |
| Q300 | `elsibaii2025open` | 0 | 0 | 3 | 5.5 | An Open and Standards-Compliant Platform for Product Data Templates in |
| Q318 | `brown2022recommendations` | 0 | 0 | 3 | 7.0 | Recommendations for Daytime, Evening, and Nighttime Indoor Light Expos |
| Q325 | `dosen2016prospect` | 0 | 0 | 3 | 6.0 | Evidence for Prospect-Refuge Theory: A Meta-Analysis of the Findings o |
| Q326 | `spoerrle2010sleeping` | 0 | 0 | 3 | 6.5 | Sleeping in Safe Places: An Experimental Investigation of Human Sleepi |
| Q339 | `basner2014noise` | 0 | 0 | 2 | 6.0 | Auditory and Non-Auditory Effects of Noise on Health |
| Q344 | `hanson1998decoding` | 0 | 0 | 3 | 5.5 | Decoding Homes and Houses |
| Q384 | `meseguer2006soft` | 0 | 0 | 2 | 6.5 | Soft Constraints |
| Q385 | `fischer1991critiquing` | 2 | 0 | 3 | 6.5 | The Role of Critiquing in Cooperative Problem Solving |
| Q386 | `silverman1992critiquing` | 1 | 0 | 2 | 6.0 | Survey of Expert Critiquing Systems: Practical and Theoretical Frontie |
| Q388 | `miller2019explanation` | 2 | 0 | 3 | 7.0 | Explanation in Artificial Intelligence: Insights from the Social Scien |
| Q393 | `guyatt2008grade` | 0 | 1 | 3 | 6.0 | GRADE: An Emerging Consensus on Rating Quality of Evidence and Strengt |
| Q452 | `sonnenberg2012evaluations` | 0 | 3 | 0 | 6.5 | Evaluations in the Science of the Artificial – Reconsidering the Build |
| Q453 | `mayring2022inhaltsanalyse` | 0 | 3 | 0 | 6.5 | Qualitative Inhaltsanalyse. Grundlagen und Techniken |
| Q455 | `bogner2014interviews` | 0 | 3 | 0 | 6.5 | Interviews mit Experten. Eine praxisorientierte Einführung |
| Q457 | `brooke1996sus` | 0 | 3 | 0 | 5.5 | SUS: A „quick and dirty“ usability scale |
| Q459 | `hart1988development` | 0 | 3 | 0 | 5.5 | Development of NASA-TLX (Task Load Index): Results of Empirical and Th |
| Q477 | `parasuraman2010complacency` | 0 | 2 | 0 | 6.0 | Complacency and Bias in Human Use of Automation: An Attentional Integr |
| Q485 | `haug2011impact` | 0 | 3 | 0 | 5.5 | The impact of product configurators on lead times in engineering-orien |
| Q488 | `kristjansdottir2018return` | 0 | 3 | 0 | 5.5 | Return on investment from the use of product configuration systems – A |
| Q490 | `love2018unpacking` | 0 | 3 | 0 | 6.0 | Unpacking the ambiguity of rework in construction: making sense of the |
| Q493 | `sacks2008impact` | 0 | 3 | 0 | 5.5 | Impact of three-dimensional parametric modeling of buildings on produc |
| Q497 | `prat2015taxonomy` | 0 | 3 | 0 | 6.5 | A Taxonomy of Evaluation Methods for Information Systems Artifacts |
| Q499 | `faulkner2003beyond` | 0 | 3 | 0 | 6.5 | Beyond the five-user assumption: Benefits of increased sample sizes in |
| Q502 | `dellacqua2026navigating` | 1 | 3 | 0 | 5.5 | Navigating the Jagged Technological Frontier: Field Experimental Evide |

Überschneidung mit Teil A: Startquellen mit zusätzlicher FF1/FF2/FF4-Relevanz (etwa `du2026text2bim`, `abualdenien2019metamodel`, `elsibaii2025open`) wurden vollständig abgefragt; Kandidaten ohne Bezug zu FF3/FF5/FF6 blieben für Teil A liegen.

## B Protokoll je Startquelle

Spalten: R/V = gesichtete Datensätze rückwärts/vorwärts; K = nach Titel/Abstract vorausgewählte Kandidaten; D = davon Dubletten zu Bestand oder Teil A; A = aufgenommen (eine Quelle kann mehreren Startquellen zugeordnet sein). Bei Startquellen mit sehr vielen Zitierenden (GRADE, NASA-TLX, SUS, Miller, Basner, Brown, Hanson, Aichholzer, Bogner, Mayring) ist die Vorwärtssuche **gezielt**: Volltextfilter innerhalb der Zitierenden (`cites:W…&search=…`), Suchbegriffe in der Tabelle.

| ID | Key | R | V | K | D | A | Anmerkung |
|---|---|---|---|---|---|---|---|
| Q027 | `du2026text2bim` | 44 | 24 | 26 | 5 | 15 | vollständig |
| Q103 | `trentin2013sales` | 120 | 50 | 26 | 5 | 17 | vollständig |
| Q110 | `schoenwitz2017product` | 75 | 69 | 21 | 2 | 14 | vorwärts gemeinsam mit Q213/Q242 abgefragt (77 Datensätze) |
| Q118 | `randall2007user` | 38 | 199 | 14 | 0 | 15 | vollständig |
| Q123 | `lee2024generalized` | 25 | 1 | 1 | 0 | 2 | Referenzen aus dem arXiv-PDF (in OpenAlex keine); vorwärts gemeinsam mit Q275 |
| Q213 | `kwiecinski2019customers` | – | 4 | 0 | 0 | 0 | Referenzen nicht in OpenAlex; vorwärts in Sammelabfrage mit Q110 |
| Q227 | `johnsson2009defects` | 36 | 122 | 13 | 2 | 9 | vollständig |
| Q234 | `chateauvieux2023bim` | – | 1 | 1 | 0 | 1 | Dissertation nicht in OpenAlex; Folgesuche zur Autorin: Kalenderbeitrag 2025 und dessen 6 Referenzen |
| Q242 | `wang2019automatic` | 7 | 4 | 1 | 0 | 0 | vorwärts in Sammelabfrage mit Q110 |
| Q275 | `kodnongbua2024zeroshot` | 34 | 0 | 14 | 4 | 5 | Referenzen aus der arXiv-HTML-Fassung |
| Q290 | `aichholzer1995novel` | 3 | 85 | 3 | 0 | 3 | vorwärts: Filter „roof“ über 333 Zitierende beider Fassungen (Springer 1996, JUCS) |
| Q292 | `kelly2011interactive` | 21 | 105 | 14 | 0 | 11 | vollständig |
| Q294 | `abualdenien2019metamodel` | 78 | 129 | 6 | 1 | 5 | rückwärts gemeinsam mit Q295; vorwärts gemeinsam mit Q295 und Q300 |
| Q295 | `abualdenien2022levels` | (Q294) | (Q294) | 11 | 0 | 11 | siehe Q294 |
| Q300 | `elsibaii2025open` | 80 | (Q294) | 8 | 1 | 7 | vorwärts in Sammelabfrage (2 Zitierende) |
| Q318 | `brown2022recommendations` | 200 von 206 | 20 | 6 | 0 | 6 | rückwärts gemeinsam mit Q339; vorwärts Filter „residential lighting design dwelling“ über 616 Zitierende |
| Q325 | `dosen2016prospect` | 92 | 161 | 18 | 5 | 12 | rückwärts und vorwärts gemeinsam mit Q326 |
| Q326 | `spoerrle2010sleeping` | (Q325) | (Q325) | 5 | 1 | 4 | siehe Q325 |
| Q339 | `basner2014noise` | (Q318) | 42 | 8 | 0 | 7 | vorwärts Filter „dwelling sound insulation building acoustics“ über 2 509 Zitierende |
| Q344 | `hanson1998decoding` | – | 65 | 4 | 0 | 4 | Buch ohne Referenzen in OpenAlex; vorwärts Filter „dwelling layout plan“ über 452 Zitierende |
| Q384 | `meseguer2006soft` | – | 4 | 2 | 0 | 2 | Kapitel nicht einzeln indexiert; vorwärts über das Handbook of Constraint Programming, Filter „floor plan layout building“ |
| Q385 | `fischer1991critiquing` | 84 | 259 | 7 | 0 | 5 | rückwärts und vorwärts gemeinsam mit Q386 |
| Q386 | `silverman1992critiquing` | (Q385) | (Q385) | 2 | 0 | 3 | siehe Q385 |
| Q388 | `miller2019explanation` | 153 | 40 | 1 | 0 | 1 | vorwärts: 1 300 Treffer mit Filter „building design“ über 5 237 Zitierende, die 40 relevantesten gesichtet |
| Q393 | `guyatt2008grade` | (Sammel) | 30 | 0 | 0 | 0 | vorwärts: 35 Treffer (Filter „built environment housing design“) über 23 439 Zitierende, 30 gesichtet |
| Q452 | `sonnenberg2012evaluations` | (Sammel) | 40 | 7 | 3 | 2 | vorwärts: 43 Treffer (Filter „construction building“) über 303 Zitierende, 40 gesichtet |
| Q453 | `mayring2022inhaltsanalyse` | – | 0 | 0 | 0 | 0 | Ausgabe 2022 nicht indexiert; vorwärts über Ausgabe 2003 gemeinsam mit Q455, Filter „BIM Bauwesen Holzbau“ |
| Q455 | `bogner2014interviews` | (Sammel) | 0 | 0 | 0 | 0 | siehe Q453 |
| Q457 | `brooke1996sus` | (Sammel) | 86 | 6 | 0 | 6 | vorwärts: 40 von 489 Treffern (Filter „building information modeling architectural design“); mit Q459 zusätzlich 29 („BIM natural language“) und 17 („configurator“) |
| Q459 | `hart1988development` | (Sammel) | (Q457) | 1 | 0 | 0 | siehe Q457 |
| Q477 | `parasuraman2010complacency` | 200 von 242 | 100 von 121 | 0 | 0 | 0 | rückwärts gemeinsam mit Q497, Q499, Q502; vorwärts gemeinsam mit Q497, Q499: Filter „building design construction architecture“ über 2 968 Zitierende |
| Q485 | `haug2011impact` | 70 | 86 | 7 | 5 | 2 | rückwärts und vorwärts gemeinsam mit Q488 |
| Q488 | `kristjansdottir2018return` | (Q485) | (Q485) | 4 | 1 | 2 | siehe Q485 |
| Q490 | `love2018unpacking` | 105 | 200 von 205 | 5 | 1 | 4 | rückwärts und vorwärts gemeinsam mit Q493 |
| Q493 | `sacks2008impact` | (Q490) | (Q490) | 9 | 2 | 5 | siehe Q490 |
| Q497 | `prat2015taxonomy` | (Q477) | (Q477) | 2 | 0 | 2 | siehe Q477 |
| Q499 | `faulkner2003beyond` | (Q477) | (Q477) | 2 | 1 | 1 | siehe Q477 |
| Q502 | `dellacqua2026navigating` | (Q477) | 153 | 2 | 2 | 0 | vorwärts vollständig; Zitierende fast nur Management-/Arbeitsmarktforschung ohne Baubezug |

Befunde je Cluster:

- **LLM/BIM (Q027, Q123, Q275):** Text2BIM ist 24-mal zitiert, fast ausschließlich 2026; die vorwärts gefundenen Arbeiten (Multiagenten-Grundriss, Function-Calling, Fehlerkorrektur, Baustelleneinrichtung per RAG) sind neu. Rückwärts sind die BIM-LLM-Kernarbeiten (NADIA, BIM-GPT/Zheng & Fischer, HouseDiffusion) bereits im Bestand.
- **Konfiguratoren (Q103, Q118):** Die Referenzlisten von Trentin et al. (2013) und Randall et al. (2007) erschließen die Mass-Customization-Marketingforschung (Toolkits, Überforderung, Selbstdesign), die im Bestand nur mit Franke et al. (2010) und Iyengar & Lepper (2000) vertreten war. Vorwärts erscheint die Linie „Konfiguration aus natürlicher Sprache“ (FF3).
- **Fertighaus/Vorfertigung (Q110, Q227, Q242, Q213):** Vorwärts vor allem Kundenintegration im Wohnungsbau (Hentschke et al., drei Arbeiten), Qualität und Nacharbeit; die Klassiker (Barlow et al. 2003, Josephson & Hammarlund 1999, Pan et al. 2007) sind im Bestand.
- **Dach/prozedurale Modellierung (Q290, Q292):** Die Straight-Skeleton-Linie ist bis auf Kelly (2011/2014) und Aichholzer et al. (1995) neu.
- **Reifegrade/Produktdaten (Q294, Q295, Q300):** Neu sind LOIN-Norm, Datenvorlagen-Norm, LOD-Aufwand und Informationsreife. Drei Funde teilt diese Gruppe mit Teil A (hier geführt), eine Arbeit (Zahedi et al. 2022) steht nur in Teil A.
- **Architekturpsychologie, Licht, Lärm (Q318, Q325, Q326, Q339, Q344):** Höchste Dublettenquote der Runde (Ulrich 1984, Hildebrand 1999, Coburn et al. 2017/2020, Bonin 2023, Zhong 2022). Neu sind rechenbare Maße (Isovisten) und Wohn-spezifische Licht- und Lärmstudien.
- **Critiquing/Erklärung (Q384–Q388):** Fischer, Oh und Gross sowie Gregor & Benbasat (1999) sind neu; Millers Referenzen sind überwiegend sozialwissenschaftlich und brachten nur Kulesza et al. (2013).
- **Nachtrag FF5 (Q477–Q502):** Konfigurator- und Nacharbeitsliteratur ist durch `lit-H-ff4-ff5.bib` schon breit im Bestand (12 von 31 Kandidaten Dubletten). Neu sind Kosten und Scheitern von Konfigurationsprojekten (Haug et al. 2018, 2019), Mängelkosten im Wohnungsbau (Mills et al. 2009; Forcada et al. 2012), Planungsrevisionen (Manavazhi & Zhang 2001), MacLeamy-Kurven empirisch (Lu et al. 2015) und Virzi (1992) zur Stichprobengröße. Automation-Bias-Literatur aus Q477 gehört zu FF4 (Teil A).
- **Methoden (Q393, Q452, Q453, Q455, Q457, Q459):** Die DSR-Grundlagen (Hevner, Peffers, Sein, Venable) sind im Bestand. Neu sind Evaluationsmuster (Sonnenberg & vom Brocke 2012b), vom Brocke et al. (2020) und Evaluationsstudien mit SUS/NASA-TLX im Wohn- und BIM-Kontext. GRADE, Bogner und Mayring lieferten keine Kandidaten mit Bezug zu FF3/FF5/FF6.

## C PRISMA-Zahlen dieser Runde

```
Gesichtete Datensätze (Titel)           3637   (rückwärts 1558, vorwärts 2079; Listen überlappen, nicht bereinigt)
  -> vorausgewählte Kandidaten             257
     - Dubletten Bestand / Teil A           42   (quellen-master.csv und .bib: 40; lit-I-schneeball-a.bib: 1; Titelvariante A Pattern Language: 1)
     - interne Dubletten                     3   (Preprint und Verlagsfassung derselben Arbeit)
  -> eindeutige neue Kandidaten            212   (Existenz über DOI-Record bzw. PMLR geprüft)
     - ausgeschlossen nach Abstract         37   (Relevanz < 2 für FF3/FF5/FF6, redundant oder anderer FF)
  -> aufgenommen (Relevanz >= 2)           175   (FF3 28, FF5 67, FF6 80 nach Schwerpunkt; 19 mit Relevanz 3; [U] 5)
```

Ausschlussgründe (Auswahl): Bild- statt Modellgenerierung (z. B. Text-zu-Interior per Diffusion), lernbasierte Grundriss- oder Dachgenerierung ohne Regelbezug, Zuordnung zu FF2/FF4 (Regelumwandlung für ACC, Entwurfsbegründung), Redundanz zu vorhandenen Quellen (Überforderung: `iyengar2000choice`; DSR-Evaluation: `venable2016feds`), Kontext ohne Übertragbarkeit (Büro, Lehre, Massivbau Korea). Die vollständige Liste steht in Anhang G.

## D Aufgenommene Quellen

Vorläufige Relevanz ff3/ff5/ff6; Einordnung nach Schwerpunkt. Kurzbegründung auf Basis von Abstract bzw. Titel und Zitationskontext (siehe `note`-Feld).

### FF3 Sprachschnittstelle (28)

| Key | Quelle | Schneeball von | ff3 | ff5 | ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `elghaish2022voice` | Elghaish et al. (2022) | kodnongbua2024zeroshot (R) | 3 | 0 | 0 | KI-Sprachassistent (ASR + NLP) für BIM-Datenabfrage und -verwaltung; unmittelbarer Vorläufer einer gesprochenen Schnittstelle (FF3). |
| `park2026bimllm` | Park et al. (2026) | du2026text2bim (V) | 3 | 1 | 0 | Systematisches Review von 61 BIM-LLM-Studien: technische Validierung 70,5 %, industrielle nur 44,3 %. Belegt, dass Sprach-BIM-Kopplungen selten im Betrieb erprobt sind; stützt die Forderung nach deterministischer Ausführung und Evaluation (FF3, Kap. 6). |
| `wang2022natural` | Wang et al. (2022) | trentin2013sales (V), randall2007user (V) | 3 | 2 | 0 | Produktkonfiguration aus freiem Text über Text-Embeddings und MLP; zeigt, dass Wunschbeschreibungen von Laien auf Konfiguratorparameter abgebildet werden können. Kernbaustein für Intent → Parameter (FF3). |
| `wu2026alterations` | Wu et al. (2026) | du2026text2bim (V) | 3 | 0 | 1 | LLM formalisiert menschliche Änderungsstrategien, die dann regelbasiert Bauteile code-konform ändern. Direkter Baustein für die Trennung "KI versteht, Code entscheidet" bei Modelländerungen. |
| `chen2026critiquecrew` | Chen et al. (2026) | fischer1991critiquing (V) | 2 | 0 | 1 | LLM-Agenten liefern Designkritik aus mehreren Perspektiven; aktuelle LLM-Fortschreibung des Critiquing-Ansatzes (Fischer 1991). |
| `dieng2026hvac` | Dieng et al. (2026) | du2026text2bim (V) | 2 | 0 | 1 | LLM-Agenten mit wissensgeleiteter Selbstprüfung konfigurieren HVAC-Modelle in EnergyPlus; relevant für Sprachschnittstelle zur TGA-Auslegung. |
| `dinis2024nui` | Dinis et al. (2024) | brooke1996sus (V) | 2 | 1 | 0 | Natürliche Benutzerschnittstellen (Sprache/Gesten) zur semantischen Anreicherung von IFC-Modellen, mit Usability-Validierung; offene Formate. |
| `erculiani2019layout` | Erculiani et al. (2019) | meseguer2006soft (V) | 2 | 0 | 1 | Layout-Synthese mit konstruktiver Präferenzabfrage: Nutzerpräferenzen werden gelernt, ein Constraint-Solver erzeugt Grundrisse. Muster für Präferenz (weich) + Solver (hart), vgl. Soft Constraints. |
| `fernandes2024gptassistant` | Fernandes et al. (2024) | du2026text2bim (R) | 2 | 0 | 0 | GPT-Assistent (DAVE) für Echtzeit-Interaktion mit BIM-Modellen; Vergleichssystem für die Sprachschnittstelle. |
| `gao2023pal` | Gao et al. (2023) | kodnongbua2024zeroshot (R) | 2 | 0 | 0 | LLM erzeugt Programme, ein Interpreter rechnet: Genauigkeit steigt gegenüber reinem Chain-of-Thought. Allgemeiner KI-Beleg für "KI versteht, Code entscheidet". |
| `gregor1999explanations` | Gregor & Benbasat (1999) | silverman1992critiquing (V) | 2 | 0 | 1 | Theorie der Erklärungskomponenten wissensbasierter Systeme (Art, Zeitpunkt, Form); stützt Empfehlungen mit Begründung (Prinzip 8) und die Erklärbarkeit der Intent-Erkennung. |
| `huang2024semanticgap` | Huang et al. (2024) | randall2007user (V) | 2 | 1 | 0 | Soft-Prompts auf vortrainierten Sprachmodellen überbrücken die semantische Lücke zwischen Kundenbedarf und Produktspezifikation (C2M). Methode übertragbar auf Kundenwunsch → Bauteilparameter. |
| `ibrahim2026llmreview` | Ibrahim et al. (2026) | du2026text2bim (V) | 2 | 0 | 0 | Review zu LLM in der Gebäudeperformance mit Schwerpunkt Evaluationspraxis und Zuverlässigkeit; stützt die Evaluationsanforderungen an FF3. |
| `jaff2025visa4d` | Jaff et al. (2025) | sonnenberg2012evaluations (V) | 2 | 1 | 0 | Sprachgesteuerter Terminplanungsassistent für 4D-BIM, als Design-Science-Artefakt entwickelt und evaluiert; Vorbild für Sprachschnittstelle plus Evaluation. |
| `jang2024interactivedesign` | Jang & Lee (2024) | du2026text2bim (R), lee2024generalized (R) | 2 | 0 | 0 | Vorläufer von NADIA: GPT erzeugt und ändert BIM-Objekte im Dialog. Belegt den Schritt interpret-fill-structure-execute, auf dem Lee et al. (2024) aufbauen. |
| `jiang2024epluslm` | Jiang et al. (2024) | du2026text2bim (R) | 2 | 0 | 0 | LLM übersetzt Textbeschreibungen in lauffähige EnergyPlus-Modelle; Beleg für das Muster "Sprache → Eingabedatei eines deterministischen Rechenkerns". |
| `li2024spatial` | Li et al. (2024) | du2026text2bim (R) | 2 | 0 | 0 | Evaluation räumlichen Schließens von LLMs (StepGame): systematische Fehler bei Lagebeziehungen. Begründet, warum Geometrie deterministisch berechnet und nicht vom Sprachmodell entschieden wird. |
| `li2026functioncalling` | Li et al. (2026) | du2026text2bim (V) | 2 | 0 | 0 | Function-Calling-Agenten, deren Werkzeugaufrufe von Experten vorgeplant sind (Zeichnungsfall im Bauwesen); Muster für begrenzte, geprüfte Befehlsmenge statt freier Codegenerierung. |
| `lin2026defects` | Lin et al. (2026) | du2026text2bim (V) | 2 | 1 | 0 | LLM erkennt und korrigiert merkmalsbezogene Modellfehler in BIM; relevant für die Prüfschleife nach einer Sprachänderung (FF3) und für Fehlerquote (FF5). |
| `makatura2024llm` | Makatura et al. (2024) | kodnongbua2024zeroshot (R) | 2 | 0 | 0 | Untersucht LLM-Einsatz entlang der Kette Text → Spezifikation → Entwurfsraum → Fertigung mit Fähigkeiten und Grenzen; begutachtete Fassung des bei Kodnongbua zitierten Preprints. |
| `moshari2026material` | Moshari et al. (2026) | du2026text2bim (V) | 2 | 0 | 1 | LLM gleicht Materialbezeichnungen zwischen BIM und Performance-Werkzeugen semantisch ab; entspricht dem Match-Schritt (Lee et al. 2024) für Materialien/Produkte. |
| `ratul2026handdrawn` | Ratul et al. (2026) | du2026text2bim (V) | 2 | 1 | 0 | Mensch-KI-Multiagentenrahmen von Handskizze zu 3D-BIM; relevant für multimodale Eingabe neben Sprache und für Rückfragen an den Nutzer. |
| `schick2023toolformer` | Schick et al. (2023) | kodnongbua2024zeroshot (R) | 2 | 0 | 0 | Sprachmodell lernt, externe Werkzeuge (Rechner, Suche) per API aufzurufen; Grundlage der Werkzeugaufruf-Architektur einer Sprachschnittstelle. |
| `wang2021knowledge` | Wang et al. (2021) | randall2007user (V) | 2 | 0 | 0 | Wissensgestütztes Multitask-Lernen zwischen Kundenbedarf und Konstruktionsspezifikation; ergänzt wang2021needsbased um Domänenwissen. |
| `wang2021needsbased` | Wang et al. (2021) | randall2007user (V) | 2 | 1 | 0 | Bedarfsbasierter Konfigurator: hierarchisches Attention-Netz leitet Spezifikationen aus Bedarfsaussagen ab. Stützt Intent-Erkennung statt Parameterabfrage. |
| `wu2019retrieval` | Wu et al. (2019) | kodnongbua2024zeroshot (R) | 2 | 0 | 1 | Natürlichsprachliche Suche in einer BIM-Objektdatenbank; Baustein für den Match-Schritt (Begriff → Katalogartikel) bei der Bemusterung. |
| `yin2023ontology` | Yin et al. (2023) | elsibaii2025open (R) | 2 | 0 | 0 | Ontologiegestützte, natürlichsprachliche BIM-Abfrage mit mehreren Bedingungen; zeigt Nutzen expliziter Semantik für die Übersetzung Sprache → Abfrage. |
| `zhang2026multiagent` | Zhang & Zhang (2026) | du2026text2bim (V) | 2 | 0 | 0 | Multiagenten-LLM für frühe Grundrissplanung mit freier Anforderungseingabe; Vergleichsarbeit zu Text2BIM, zeigt Grenzen räumlichen Schließens. |

### FF5 Wirkung (67)

| Key | Quelle | Schneeball von | ff3 | ff5 | ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `bakhshi2021dfma` | Bakhshi et al. (2021) | schoenwitz2017product (V) | 0 | 3 | 1 | BIM-DfMA-Rahmen mit parametrisch-algorithmischer Konfiguration (Revit/Dynamo), der Kunden an der Konfiguration von Offsite-Bauten beteiligt; nächstverwandter Ansatz zum Zielbild. |
| `campogay2026quality` [U] | Campo Gay et al. (2026) | schoenwitz2017product (V) | 0 | 3 | 0 | Längsschnitt-Fallstudie: Konfigurationssysteme verbessern die Qualität von Bauspezifikationen; empirischer Beleg für die Fehlerquote-Hypothese (FF5). |
| `hvam2006quotation` | Hvam et al. (2006) | trentin2013sales (R) | 0 | 3 | 0 | Fallstudie: Produktkonfiguration verkürzt und verbessert den Angebotsprozess (Durchlaufzeit, Fehler); direkter Vergleichswert für die Angebotsphase im Fertighausvertrieb. |
| `randall2005principles` | Randall et al. (2005) | trentin2013sales (R), randall2007user (R) | 0 | 3 | 0 | Gestaltungsprinzipien für User Design (parameter- vs. bedarfsbasierte Konfiguration, Prototypen, Startlösungen); direkt übernehmbar für die Gestaltung der Kundenoberfläche. |
| `raposo2024bridging` | Raposo et al. (2024) | brooke1996sus (V) | 0 | 3 | 1 | GUI für Co-Design im kundenindividuellen Wohnungsbau, mit Nutzerstudie (SUS) evaluiert; nächstverwandte Laienevaluation zum Zielbild. |
| `suznjevic2025longitudinal` | Sužnjević et al. (2025) | brooke1996sus (V) | 0 | 3 | 2 | Längsschnitt-Usability (Web, VR, mobiles AR) einer Hausentwurfs-Pipeline; Vorbild für Evaluationsdesign mit Laien und Darstellungsvarianten. |
| `trentin2011overcoming` | Trentin et al. (2011) | trentin2013sales (R) | 0 | 3 | 0 | Großzahlige Studie (238 Werke, 8 Länder): Konfiguratoreinsatz verbessert die Zeitperformance bei kundenindividuellen Produkten signifikant. Empirischer Beleg für die Durchlaufzeit-Hypothese (FF5). |
| `attia2024usability` | Attia et al. (2024) | prat2015taxonomy (V) | 0 | 2 | 0 | Usability- und Eignungstests von Gebäudesimulationswerkzeugen mit Architekten und Ingenieuren; Evaluationsvorbild im Bauwesen. |
| `borsci2022chatbot` | Borsci et al. (2022) | brooke1996sus (V) | 1 | 2 | 0 | Chatbot Usability Scale (BUS-15): validiertes Instrument, das SUS für Konversationsagenten ergänzt; einsetzbar in der Laienevaluation der Sprachschnittstelle (FF5). |
| `boumova2016apartment` | Boumová & Zdráhalová (2016) | hanson1998decoding (V) | 0 | 2 | 2 | Grundrisspräferenzen von Architekten und Laien unterscheiden sich systematisch; stützt die Rollenverteilung Laie/Architekt und Empfehlungslogik. |
| `cannas2022eto` | Cannas et al. (2022) | schoenwitz2017product (V) | 0 | 2 | 0 | Mehrfallstudie zur Einführung von Konfiguratoren in Engineer-to-Order-Betrieben; Übertragung auf Fertighaus (ETO-nah). |
| `chen2023factors` | Chen et al. (2023) | schoenwitz2017product (V) | 0 | 2 | 0 | Mehrfallstudie: Bauzeitverzug im Fertigbau hängt von Technik- und Abwicklungssystem ab; relativiert pauschale Zeitgewinne (FF5). China, Geschossbau. |
| `darwish2020estimating` | Darwish (2020) | schoenwitz2017product (V) | 0 | 2 | 0 | Kalkulationsrahmen für die Fertigung im leichten Holzrahmenbau (Alberta); Referenz für automatische Kostenableitung aus dem Modell. |
| `dellaert2005marketing` | Dellaert & Stremersch (2005) | trentin2013sales (R) | 0 | 2 | 0 | Experiment: Nutzen vs. Komplexität verschiedener Mass-Customization-Konfigurationen; stützt Regeln für Umfang und Reihenfolge der Auswahlschritte. |
| `duncheva2019productivity` | Duncheva & Bradley (2019) | johnsson2009defects (V) | 0 | 2 | 0 | Produktivitätsvergleich von Offsite-Holzbau-Strategien in Kontinentaleuropa und Großbritannien; Vergleichswerte für Durchlaufzeit und Automatisierung. |
| `fogliatto2012mass` | Fogliatto et al. (2012) | trentin2013sales (R) | 0 | 2 | 0 | Übersichtsarbeit zu zehn Jahren Mass-Customization-Forschung (Fogliatto et al.); Einordnung der Konfiguratorliteratur. |
| `forcada2012buildingtype` | Forcada et al. (2012) | love2018unpacking (R) | 0 | 2 | 0 | Einfluss des Gebäudetyps auf Mängel nach Übergabe im Wohnungsbau; Messgrundlage für Fehlerquote je Gebäudetyp. |
| `forcada2016handover` | Forcada et al. (2016) | johnsson2009defects (V) | 0 | 2 | 0 | Vergleich von Mängeln bei Bau und nach Übergabe; Kundensicht auf Fehler als Wirkungsgröße. |
| `franke2003toolkits` | Franke & Piller (2003) | trentin2013sales (R) | 0 | 2 | 0 | Forschungsagenda zur Nutzerinteraktion mit Toolkits (Franke & Piller); Kontext für die Laienevaluation. |
| `franke2009testing` | Franke et al. (2009) | randall2007user (V) | 0 | 2 | 0 | Experimente: Mehrwert individueller Produkte hängt von Präferenzklarheit und Ausdrucksfähigkeit ab; Moderatoren für die Laienevaluation. |
| `franke2010selfdesigned` | Franke & Schreier (2010) | trentin2013sales (R), randall2007user (V) | 0 | 2 | 0 | Prozessfreude und Aufwand erklären den Wert selbst entworfener Produkte; relevant für die Wirkungshypothese auf Kundenzufriedenheit. |
| `franke2014niche` | Franke & Hader (2014) | randall2007user (V) | 0 | 2 | 0 | Toolkits als Lerninstrumente: Kunden wissen anfangs nicht, was sie wollen; stützt iterative Exploration statt einmaliger Abfrage. |
| `grenzfurtner2026failure` | Grenzfurtner & Gronalt (2026) | schoenwitz2017product (V) | 0 | 2 | 0 | FMEA zur kontinuierlichen Prozessverbesserung im industrialisierten Hausbau (Nacharbeit, Fehler); Methode zur Messung von Fehlerquellen. |
| `han2012nonvalue` | Han et al. (2012) | love2018unpacking (R) | 0 | 2 | 0 | Identifikation und Quantifizierung nicht wertschöpfender Aufwände aus Fehlern und Änderungen; Methode zur Messung von Planungsschleifen. |
| `haubl2000decisionaids` | Häubl & Trifts (2000) | randall2007user (R) | 0 | 2 | 0 | Interaktive Entscheidungshilfen (Empfehlung, Vergleichsmatrix) verbessern Entscheidungsqualität bei geringerem Aufwand; Grundlage für Assistenzfunktionen. |
| `haug2018costs` | Haug et al. (2018) | kristjansdottir2018return (V) | 0 | 2 | 0 | Kosten und Nutzen von Konfigurationsprojekten in Engineer-to-Order-Unternehmen; Grundlage für die Wirtschaftlichkeitsbetrachtung (FF5). |
| `haug2019causes` | Haug et al. (2019) | kristjansdottir2018return (V) | 0 | 2 | 0 | Ursachen des Scheiterns von Konfigurationsprojekten; Risikoliste für die Einführung beim Hersteller. |
| `hentschke2019conjoint` | Hentschke et al. (2019) | schoenwitz2017product (V) | 0 | 2 | 1 | Conjoint-Analyse zu Kundenpräferenzen bei Anpassungsoptionen im Wohnungsbau; Methodenvorbild für Präferenzmessung. |
| `hentschke2020customer` | Hentschke et al. (2020) | schoenwitz2017product (V) | 0 | 2 | 1 | Rahmen zur Kundenintegration in Mass-Customised-Housing-Projekten; ordnet Entscheidungspunkte des Kunden im Projektablauf. |
| `hentschke2022method` | Hentschke et al. (2022) | schoenwitz2017product (V) | 0 | 2 | 2 | Methode zur Erfassung von Anpassungswünschen im Wohnungsbau mit Abwägung Kundennutzen vs. Betriebskosten; relevant für Bemusterung und Katalogzuschnitt. |
| `hofman2006variation` | Hofman et al. (2006) | schoenwitz2017product (R) | 0 | 2 | 2 | Conjoint-Studie zu Kundenpräferenzen bei Varianten im Wohnungsbau (Niederlande); Datenbasis für Bemusterungsumfang. |
| `huffman1998variety` | Huffman & Kahn (1998) | trentin2013sales (R), schoenwitz2017product (R) | 0 | 2 | 0 | Experiment: attributbasierte Präsentation senkt Überforderung bei großer Variantenvielfalt; stützt die Bemusterungsdarstellung. |
| `hvam2004quotation` | Hvam et al. (2004) | haug2011impact (R) | 0 | 2 | 0 | IT-gestützte Produktkonfiguration im komplexen Angebots- und Engineeringprozess (Fallstudie); ergänzt hvam2006quotation. |
| `hyun2020rework` | Hyun et al. (2020) | johnsson2009defects (V) | 0 | 2 | 0 | Integrierter Planungsprozess für Modulbau zur Reduktion von Nacharbeit; stützt die Hypothese weniger Planungsschleifen. |
| `jakesch2023cowriting` | Jakesch et al. (2023) | prat2015taxonomy (V) | 1 | 2 | 1 | Experiment: Ein meinungsgeprägtes Sprachmodell als Schreibassistent verschiebt die Ansichten der Nutzer; Risiko für "Assistieren statt bevormunden" und Evaluationsgröße. |
| `krause2024abandonment` | Krause & Franke (2024) | randall2007user (V) | 0 | 2 | 0 | Dynamische Analyse von Abbrüchen im Self-Design; Messgröße und Risiko für die Wirkungsevaluation mit Laien. |
| `kristjansdottir2018challenges` | Kristjansdottir et al. (2018) | trentin2013sales (V) | 0 | 2 | 0 | Mehrfallstudie zu Hürden bei Einführung und Nutzung von Konfiguratoren (Wissenspflege, Organisation); stützt die Diskussion der Arbeitsteilung und Einführungskosten. |
| `leclercq2022expectations` | Leclercq et al. (2022) | trentin2013sales (V) | 0 | 2 | 0 | Empirische Befragung zu Erwartungen an Web-Konfiguratoren (Visualisierung, Preis, Fehlermeldungen); Anforderungsquelle für die Kundenoberfläche. |
| `lee2020augmented` | Lee et al. (2020) | brooke1996sus (V) | 0 | 2 | 1 | Endnutzer prüfen Architekturentwürfe mit AR; Evaluation der Wirksamkeit aus Nutzersicht. |
| `leishman2006substitution` | Leishman & Warren (2006) | schoenwitz2017product (R) | 0 | 2 | 0 | Anpassung über Haustyp-Substitution im britischen Wohnungsbau; Vergleichsstrategie zur freien Konfiguration. |
| `leite2011modeling` | Leite et al. (2011) | abualdenien2019metamodel (R) | 0 | 2 | 2 | Misst Modellierungsaufwand und Nutzen verschiedener Detaillierungsgrade (Kollisionsprüfung); Beleg für den Aufwand je Reifegrad. |
| `liu2022offsite` | Liu et al. (2022) | johnsson2009defects (V) | 0 | 2 | 0 | Review der Qualitätskontrolle im Offsite-Bau; Einordnung der Fehlerquote als Wirkungsgröße. |
| `love2022rework` | Love et al. (2022) | love2018unpacking (V) | 0 | 2 | 0 | Übersicht zum Stand der Nacharbeitsforschung (Ursachen, Folgen, Gegenmaßnahmen); Einordnung der Fehlerquote. |
| `lu2015timeeffort` | Lu et al. (2015) | sacks2008impact (V) | 0 | 2 | 0 | Empirische Prüfung der MacLeamy-Kurven (Zeit-Aufwand-Verteilung) mit und ohne BIM; Vergleich für die Verlagerung von Planungsaufwand. |
| `macarulla2013defects` | Macarulla et al. (2013) | johnsson2009defects (V) | 0 | 2 | 0 | Validierte Klassifikation von Mängeln im Wohnungsbau; übernehmbares Schema zur Messung der Fehlerquote. |
| `mahlamaki2020adoption` | Mahlamäki et al. (2020) | trentin2013sales (V) | 0 | 2 | 0 | Akzeptanz von Vertriebskonfiguratoren durch Kunden im B2B; relevant für die neue Arbeitsteilung Kunde/Vertrieb. |
| `manavazhi2001revisions` | Manavazhi & Zhang (2001) | sacks2008impact (R) | 0 | 2 | 0 | Rahmen zur Bewertung von Häufigkeit und Ursachen von Planungsrevisionen; Messgröße für Planungsschleifen. |
| `mills2009defect` | Mills et al. (2009) | love2018unpacking (R) | 0 | 2 | 0 | Mängelkosten im australischen Wohnungsbau aus Gewährleistungsdaten; Vergleichswert für die Fehlerquote im Einfamilienhausbau. |
| `panya2023change` | Panya et al. (2023) | sacks2008impact (V) | 0 | 2 | 1 | Interaktive Änderungsmethode mit BIM, VR und AR; relevant für Änderungsschleifen mit Kunden. |
| `piroozfar2013mass` | Piroozfar & Piller (2013) | schoenwitz2017product (R) | 0 | 2 | 1 | Sammelband (Piroozfar & Piller) zu Mass Customisation in Architektur und Bau; Kontext und Fallbeispiele. |
| `renner2025copilot` | Renner et al. (2025) | brooke1996sus (V) | 1 | 2 | 0 | KI-Co-Pilot (GNN) für Entwurfs-Autovervollständigung, mit Architekten evaluiert; Evaluationsvorbild mit Experten. |
| `sacks2005benchmark` | Sacks et al. (2005) | sacks2008impact (R) | 0 | 2 | 0 | Benchmark des Nutzens parametrischer 3D-Modellierung im Fertigteilbau (Sacks et al.); Vergleichswerte für Planungsaufwand. |
| `salvador2004configuring` | Salvador & Forza (2004) | haug2011impact (R) | 0 | 2 | 0 | Befragungsbasierte Studie zu Managementfragen beim Konfigurieren unter dem Druck von Individualisierung und Reaktionszeit; theoretischer Unterbau der Durchlaufzeit-Hypothese. |
| `sonnenberg2012patterns` | Sonnenberg & vom Brocke (2012) | sonnenberg2012evaluations (R) | 0 | 2 | 0 | Evaluationsmuster für DSR-Artefakte (ex ante/ex post, künstlich/naturalistisch); ergänzt Sonnenberg & vom Brocke (2012a) um konkrete Muster für das Evaluationsdesign. |
| `stablein2011variety` | Stäblein et al. (2011) | schoenwitz2017product (R) | 0 | 2 | 2 | Misst tatsächlich gewählte gegenüber angebotener Varianz; relevant für den Zuschnitt des Bemusterungskatalogs. |
| `tang2017novice` | Tang et al. (2017) | randall2007user (V) | 0 | 2 | 0 | Design-Science-Studie zu Entscheidungsunterstützung für Laienkäufer; Vorbild für Artefakt-Evaluation mit Novizen. |
| `terwiesch2004collaborative` | Terwiesch & Loch (2004) | randall2007user (R) | 0 | 2 | 0 | Modell kollaborativen Prototypings: Zahl der Iterationen zwischen Kunde und Anbieter als Kostentreiber; stützt die Hypothese weniger Planungsschleifen (FF5). |
| `trentin2014increasing` | Trentin et al. (2014) | trentin2013sales (V), randall2007user (V) | 0 | 2 | 0 | Experiment: Konfiguratorfähigkeiten (Vergleich, Navigation, Vorschau) erhöhen den wahrgenommenen Nutzen des Laien; Messmodell für die Laienevaluation. |
| `valenzuela2009contingent` | Valenzuela et al. (2009) | trentin2013sales (R) | 0 | 2 | 0 | Reihenfolge und Art der Selbstkonfiguration beeinflussen Entscheidungszufriedenheit; Gestaltungshinweis für Auswahlprozesse. |
| `virzi1992subjects` | Virzi (1992) | faulkner2003beyond (R) | 0 | 2 | 0 | Drei Experimente zur Zahl der Testpersonen in Usability-Tests; ergänzt faulkner2003beyond für die Stichprobenplanung. |
| `vombrocke2020introduction` | vom Brocke et al. (2020) | du2026text2bim (R) | 0 | 2 | 0 | Einführung in Design Science Research (vom Brocke et al.) mit Evaluationszyklen; methodische Ergänzung zu Sonnenberg & vom Brocke (2012). |
| `vonhippel2001user` | von Hippel (2001) | trentin2013sales (R) | 0 | 2 | 1 | Fünf Anforderungen an Nutzer-Toolkits (Versuch-und-Irrtum, begrenzter Lösungsraum, Bausteinbibliothek, Übersetzung in Fertigung); entspricht Regelraum und Katalog des Zielbilds. |
| `vonhippel2002shifting` | von Hippel & Katz (2002) | trentin2013sales (R) | 0 | 2 | 0 | Toolkits verlagern Entwurfsarbeit auf Nutzer und senken Iterationen zwischen Hersteller und Kunde; theoretische Grundlage für "Kunde entwirft selbst". |
| `wang2023perception` | Wang et al. (2023) | randall2007user (V) | 0 | 2 | 0 | Wahrgenommene Zeit im Online-Konfigurationsprozess und ihre Folgen; relevant für Durchlaufzeit aus Kundensicht. |
| `wyke2025productivity` [U] | Wyke et al. (2025) | sacks2008impact (V) | 0 | 2 | 0 | Einflussfaktoren auf die Planungsproduktivität in Dänemark; Messansatz für Planungsproduktivität. |
| `yi2022configurator` | Yi et al. (2022) | trentin2013sales (V) | 0 | 2 | 1 | Studie zur Interaktionsgestaltung von Konfiguratoren und Zahlungsbereitschaft; stützt Gestaltungsentscheidungen der Oberfläche (FF5). |
| `zhao2019toolkits3d` | Zhao et al. (2019) | randall2007user (V) | 0 | 2 | 2 | Übersicht und Bewertungsmodell für webbasierte 3D-Mass-Customization-Toolkits; verbindet Laienevaluation (FF5) mit 3D-Darstellung (FF6). |

### FF6 Detailtiefe (80)

| Key | Quelle | Schneeball von | ff3 | ff5 | ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `chateauvieuxhellwig2022timber` | Châteauvieux-Hellwig et al. (2022) | abualdenien2019metamodel (V) | 0 | 0 | 3 | Aus IFC-Modellen früher Phasen werden Stoßstellen im Holzbau per Topologie und Regeln erkannt (15 akustische Stoßstellentypen); übernehmbarer Baustein für Schallschutz im Holzbau (FF6). |
| `chateauvieuxhellwig2025schallschutz` [U] | Châteauvieux-Hellwig & Weise (2025) | chateauvieux2023bim (V) | 0 | 0 | 3 | Open-BIM-Planungsprozess für den Schallschutz im Holzbau (Bauphysik-Kalender 2025); deutschsprachige Fortschreibung der Dissertation Châteauvieux (2023). |
| `dineniso7817-1` | DIN (2024) | elsibaii2025open (R) | 0 | 0 | 3 | Norm zur Informationsbedarfstiefe (LOIN), Nachfolger von DIN EN 17412-1; normative Grundlage für die drei Reifegrade (FF6). |
| `held2017roofs` | Held & Palfrader (2017) | kelly2011interactive (V) | 0 | 0 | 3 | Additiv und multiplikativ gewichtete Straight Skeletons zur algorithmischen Erzeugung von Dächern mit unterschiedlichen Neigungen und Traufhöhen; direkt übernehmbarer Dachbaustein. |
| `hwang2018window` | Hwang & Lee (2018) | dosen2016prospect (V) | 0 | 0 | 3 | Parametrisches Modell zur Fensterplanung nach Prospect-Refuge-Maßen im Wohnbau; direkt übertragbarer Baustein für Empfehlungen zu Fenstern. |
| `oh2008critiquing` | Oh et al. (2008) | fischer1991critiquing (V), silverman1992critiquing (V) | 0 | 0 | 3 | Lessons learned zu Critiquing-Systemen in der Architektur; direkt übertragbar auf Architekturpsychologie-Empfehlungen im Entwurf. |
| `ren2021roof` | Ren et al. (2021) | kelly2011interactive (V) | 0 | 0 | 3 | Graphbasierte Dachmodellierung für Rekonstruktion und Synthese mit planaren Dachflächen; Baustein für editierbare Dachtopologie. |
| `wiener2007isovist` | Wiener et al. (2007) | dosen2016prospect (R) | 0 | 0 | 3 | Experimente: Isovist-Kennwerte von Innenräumen sagen Bewegung und affektives Erleben voraus; rechenbares Maß für architekturpsychologische Empfehlungen. |
| `abualdenien2020consistent` | Abualdenien et al. (2020) | abualdenien2019metamodel (R) | 0 | 0 | 2 | Konsistentes Management und Bewertung von Varianten in frühen Phasen über mehrere LOD; Baustein für Reifegrade aus einem Modell. |
| `abualdenien2020vagueness` | Abualdenien & Borrmann (2020) | abualdenien2019metamodel (R) | 0 | 0 | 2 | Visualisierung von Unschärfe in Gebäudemodellen über Entwurfsphasen; relevant für präsentationsfertig vs. prüffertig. |
| `abualdenien2022ensemble` | Abualdenien & Borrmann (2022) | abualdenien2022levels (R) | 0 | 0 | 2 | Klassifikation des geometrischen Detaillierungsgrads (LOG) von Bauteilen per Ensemble-Lernen; automatische Reifegradprüfung. |
| `ahn2013roofs` | Ahn et al. (2013) | aichholzer1995novel (V) | 0 | 0 | 2 | Realistische Dächer über rechtwinkligen Polygonen (Vermeidung unrealistischer Dachflächen); Randbedingungen für Walm- und Satteldächer. |
| `aichholzer1996general` | Aichholzer & Aurenhammer (1996) | kelly2011interactive (R) | 0 | 0 | 2 | Erweiterung des Straight Skeleton auf allgemeine polygonale Figuren (Aichholzer & Aurenhammer); Grundlage für Dächer über Grundrissen mit Löchern. |
| `ali2013critiquing` | Ali et al. (2013) | silverman1992critiquing (V) | 1 | 0 | 2 | Taxonomie und Kartierung rechnergestützter Critiquing-Werkzeuge; Einordnung der Empfehlungskomponente. |
| `alonso2021windows` | Alonso et al. (2021) | basner2014noise (V) | 0 | 0 | 2 | Anforderungen und Empfehlungen zur akustischen Ertüchtigung von Fenstern in Wohnfassaden; Fassade/Außenlärm. |
| `alshorafa2020modeluses` | Alshorafa & Ergen (2020) | abualdenien2022levels (V) | 0 | 0 | 2 | Informationsanforderungen und LOD je Modellnutzung; Ableitung der Detailtiefe aus dem Anwendungsfall. |
| `appleton1984prospects` | Appleton (1984) | dosen2016prospect (R) | 0 | 0 | 2 | Appletons Rückblick auf zehn Jahre Prospect-Refuge-Theorie; Primärquelle der Theorie für Empfehlungen. |
| `appolloni2021housing` | Appolloni & D’Alessandro (2021) | hanson1998decoding (V) | 0 | 0 | 2 | Vergleich der Mindestmaße für Wohnräume in neun europäischen Ländern; Referenz für Möblierbarkeit und Raumgrößen. |
| `asare2026dimensionality` | Asare et al. (2026) | abualdenien2022levels (V) | 0 | 0 | 2 | Dimensionen von BIM-LOD über den Lebenszyklus bis zum digitalen Zwilling; Einordnung der drei Reifegrade. |
| `basner2010guidance` | Basner et al. (2010) | basner2014noise (R) | 0 | 0 | 2 | Praxisleitfaden zur Bewertung von Schlafstörungen durch Verkehrslärm; Kenngrößen für den Außenlärm an Schlafräumen. |
| `biedl2015weighted` | Biedl et al. (2015) | kelly2011interactive (V) | 0 | 0 | 2 | Theorie gewichteter Straight Skeletons (Biedl et al.); Grundlage für unterschiedliche Dachneigungen je Traufseite. |
| `bildsten2011kitchen` | Bildsten et al. (2011) | johnsson2009defects (V) | 0 | 1 | 2 | Wertorientierter Einkauf individueller Küchen im industrialisierten Wohnungsbau; Bemusterung Küche als Kosten- und Prozessfaktor. |
| `biljecki2016lod` | Biljecki et al. (2016) | kelly2011interactive (V), abualdenien2022levels (R) | 0 | 0 | 2 | Verfeinerte LOD-Spezifikation für 3D-Gebäudemodelle (CityGML, Biljecki et al.); Vergleich geometrischer Detailstufen. |
| `bodin2015quiet` | Bodin et al. (2015) | basner2014noise (V) | 0 | 0 | 2 | Nutzen einer ruhigen Fassadenseite gegen Belästigung und Schlafstörung; Empfehlung zur Grundrissorientierung (Schlafräume). |
| `brinkmann2025maturity` | Brinkmann & Wynn (2025) | abualdenien2022levels (V) | 0 | 0 | 2 | Aspekte der Informationsreife in Konstruktion und Entwicklung; theoretische Grundlage für Reifegrade präsentations-/prüf-/ausführungsfertig. |
| `brown2020melanopic` | Brown (2020) | brown2022recommendations (R) | 0 | 0 | 2 | Melanopische Beleuchtungsstärke bestimmt die Stärke circadianer Lichtwirkungen; wissenschaftliche Grundlage der mEDI-Richtwerte von Brown et al. (2022). |
| `cain2020evening` | Cain et al. (2020) | brown2022recommendations (R) | 0 | 0 | 2 | Messung in Wohnungen: übliche Abendbeleuchtung zu Hause unterdrückt Melatonin; begründet Empfehlungen zu warmem, gedimmtem Abendlicht im Wohnbereich. |
| `cajochen2022evening` | Cajochen et al. (2022) | brown2022recommendations (V) | 0 | 0 | 2 | Systematisches Review mit Metaanalyse zu Abendlicht und polysomnografischem Schlaf; Evidenzgrad für Licht-Empfehlungen im Schlafbereich. |
| `cheung2012cost` | Cheung et al. (2012) | abualdenien2019metamodel (R) | 0 | 1 | 2 | Mehrstufige Kostenschätzung für schematische BIM-Modelle; Kosten je Reifegrad. |
| `costa2015catalogues` | Costa & Madrazo (2015) | elsibaii2025open (R) | 0 | 0 | 2 | Verknüpfung von Bauteilkatalogen mit BIM-Modellen über semantische Technik (Fertigteile); Vorbild für Katalog-Modell-Kopplung. |
| `dawes2014wright` | Dawes & Ostwald (2014) | dosen2016prospect (R) | 0 | 0 | 2 | Isovist-Analyse von Prospect-Refuge in Wohnhäusern (Frank Lloyd Wright); Methodenbeispiel für Grundrissanalyse. |
| `delval2017descriptors` | del Val et al. (2017) | basner2014noise (V) | 0 | 0 | 2 | Übersetzung zwischen Trittschall-Kennwerten und Vorschlag eines gemeinsamen Schallschutz-Klassenschemas; relevant für Schallschutzstufen. |
| `deniz2025enter` | Deniz et al. (2025) | dosen2016prospect (V) | 0 | 0 | 2 | Objektive visuelle Merkmale von Innenraumszenen sagen Annäherung/Vermeidung und Affekt voraus; aktuelle Evidenz für Interior-Empfehlungen. |
| `ding2025fitout` | Ding et al. (2025) | lee2024generalized (V) | 0 | 1 | 2 | Synchronisation von vorgefertigtem Innenausbau mit einem Fertigungssteuerungssystem; relevant für Interior-Vorfertigung und Logistik. |
| `dosen2013methodological` | Dosen & Ostwald (2013) | dosen2016prospect (R) | 0 | 0 | 2 | Methodenvergleich der Prospect-Refuge-Forschung; Grundlage für die Einstufung des Evidenzgrads. |
| `dosen2017lived` | Dosen & Ostwald (2017) | dosen2016prospect (V) | 0 | 0 | 2 | Vergleich wahrgenommener Enge/Offenheit mit metrischen Raum- und Isovist-Kennwerten; Validierung rechenbarer Maße. |
| `edelsbrunner2016roofs` | Edelsbrunner et al. (2016) | kelly2011interactive (V) | 0 | 0 | 2 | Konstruktive Dächer aus Volumenprimitiven (erweiterte Fassung von Constructive Roof Geometry, CW 2014); Alternative zum Skelettansatz für zusammengesetzte Dächer. |
| `eder2018volume` | Eder et al. (2018) | aichholzer1995novel (V) | 0 | 0 | 2 | Dächer minimalen/maximalen Volumens aus Bisektorgraphen über Gebäudegrundrissen; zeigt Mehrdeutigkeit der Dachlösung. |
| `eder2021exact` | Eder et al. (2021) | kelly2011interactive (V) | 0 | 0 | 2 | CGAL-Implementierungen von Straight Skeletons mit exakter Arithmetik; relevant für robuste, reproduzierbare Dachberechnung. |
| `emmitt2023bedroom` | Emmitt (2023) | spoerrle2010sleeping (V) | 0 | 0 | 2 | Zusammenhang von Schlafzimmergestaltung und Schlafqualität bei Hitze; Empfehlungen zu Lage und Verschattung. |
| `eppstein1999raising` | Eppstein & Erickson (1999) | kelly2011interactive (R) | 0 | 0 | 2 | Algorithmus für gerade Skelette (Straight Skeleton) mit Anwendung auf Dachflächen; algorithmische Grundlage der Dachgenerierung. |
| `femenias2020adaptable` | Femenias & Geromel (2020) | hanson1998decoding (V) | 0 | 0 | 2 | Quantitative Studie zu von Bewohnern umgebauten Wohnungsgrundrissen; Evidenz für anpassbare Zonierung. |
| `fischer1989environments` | Fischer et al. (1989) | fischer1991critiquing (R) | 0 | 0 | 2 | JANUS: konstruktive und argumentative Entwurfsumgebung für Küchen mit regelbasierten Kritikern; frühes Vorbild für Interior-Empfehlungen mit Begründung. |
| `fischer1993critics` | Fischer et al. (1993) | fischer1991critiquing (V) | 1 | 0 | 2 | Einbettung von Kritikern in Entwurfsumgebungen (Küchenplanung JANUS); Architektur für kontextbezogene Empfehlungen. |
| `franz2003vr` | Franz et al. (2003) | dosen2016prospect (R) | 0 | 1 | 2 | VR-Experiment: Raummerkmale rechteckiger Innenräume und affektive Bewertung; Methode für Bewertung im 3D-Viewer. |
| `herthogs2019saga` | Herthogs et al. (2019) | hanson1998decoding (V) | 0 | 0 | 2 | SAGA-Methode: gewichtete Graphen messen Nutzungsneutralität und Anpassbarkeit von Grundrissen; rechenbares Kriterium. |
| `hong2016fengshui` | Hong et al. (2016) | spoerrle2010sleeping (V) | 0 | 0 | 2 | Empirische Prüfung eines Form-School-Feng-Shui-Modells im Schlafraum (Präferenz, subjektive Schlafqualität); Evidenzbasis für das Kulturprofil und dessen Abgrenzung. |
| `hooper2015lod` | Hooper (2015) | abualdenien2022levels (R) | 0 | 1 | 2 | Automatische Planung des Modellfortschritts über Level of Development; Anschluss Reifegrad → Terminplan. |
| `iso23387` [U] | ISO (2020) | elsibaii2025open (R) | 0 | 0 | 2 | Norm zu Datenvorlagen (Product Data Templates) für Bauobjekte; Grundlage für Produktdaten in der Bemusterung. |
| `jalaliyazdi2021clt` | Jalali Yazdi et al. (2021) | johnsson2009defects (V) | 0 | 1 | 2 | Mass Customisation von Brettsperrholz-Wandsystemen in frühen Phasen; regelbasierte Wanderzeugung im Holzbau (CLT statt Holzrahmen). |
| `kebede2022manufacturers` | Kebede et al. (2022) | elsibaii2025open (R) | 0 | 0 | 2 | Integration von Herstellerproduktdaten in BIM-Plattformen mit Semantic-Web-Technik; Baustein für reale, bestellbare Artikel im Katalog. |
| `kozniewski2020roof` | Koźniewski & Banaszak (2020) | aichholzer1995novel (V) | 0 | 0 | 2 | Dachgeometrie über Skelettformen zur Vermeidung von Planungsfehlern im Gebäudeumriss; praxisnaher Anschluss an die Dachplanung. |
| `kulesza2013explanations` | Kulesza et al. (2013) | miller2019explanation (R) | 1 | 1 | 2 | Experiment zu Umfang und Vollständigkeit von Erklärungen für Endnutzer: vollständige Erklärungen verbessern mentale Modelle; Richtwert für die Begründung von Empfehlungen an Laien. |
| `li2026sitelayout` | Li et al. (2026) | du2026text2bim (V) | 1 | 0 | 2 | RAG-gestütztes LLM für automatische Baustelleneinrichtungsplanung; relevant für Logistik/Kran und als FF3-Muster. |
| `locher2018windows` | Locher et al. (2018) | basner2014noise (V) | 0 | 0 | 2 | Messung der Pegeldifferenz außen/innen bei offenem, gekipptem und geschlossenem Fenster; Kennwerte für Außenlärm-Nachweis und Fensterstellung. |
| `lopez2022mep` | Lopez et al. (2022) | johnsson2009defects (V) | 0 | 1 | 2 | Qualitative Studie zu Hürden der Vorfertigung von Holz- und TGA-Leistungen (MEP) zwischen Bauunternehmen und Zulieferern; stützt TGA-Integration in Wandelemente. |
| `lovset2013scaffold` | Løvset et al. (2013) | kelly2011interactive (V) | 0 | 0 | 2 | Regelbasierte automatische Gerüstplanung aus 3D-Gebäudemodellen; Baustein für Baustellenlogistik. |
| `mellenthinfilardo2026requirements` [U] | Mellenthin Filardo et al. (2026) | abualdenien2022levels (V) | 0 | 0 | 2 | Praxis und Umsetzung von Informationsanforderungen in Deutschland; direkter Deutschlandbezug für Reifegrade/LOIN. |
| `mueller2006procedural` | Müller et al. (2006) | kelly2011interactive (R) | 0 | 0 | 2 | CGA-Shape-Grammatik zur prozeduralen Gebäudemodellierung; Vorbild für regelbasierte Fassadenerzeugung. |
| `muta2025granularity` | Muta et al. (2025) | abualdenien2022levels (V) | 0 | 0 | 2 | Modellgranularität verfälscht Energiebewertungen im BIM-BEM-Workflow; belegt Mindestdetailtiefe für prüffertige Nachweise. |
| `oh2010furniture` | Oh et al. (2010) | fischer1991critiquing (V) | 0 | 0 | 2 | Constraint-basierter Möbel-Entwurfskritiker; Muster für Möblierbarkeitsprüfung mit Kritik. |
| `ohrstrom2006quietness` | Öhrström et al. (2006) | basner2014noise (R) | 0 | 0 | 2 | Feldstudie: Zugang zu einer ruhigen Seite der Wohnung mindert Belästigung durch Straßenverkehrslärm; Primärbeleg für Grundrissorientierung von Schlafräumen. |
| `palos2014productdata` | Palos et al. (2014) | elsibaii2025open (R) | 0 | 0 | 2 | Perspektiven von Produktdatenbibliotheken im BIM; Kontext für Bemusterungskatalog. |
| `park2017impact` | Park & Lee (2017) | basner2014noise (V) | 0 | 0 | 2 | Psychophysiologische Wirkung von Trittschall; begründet Trittschallanforderungen zwischen Wohnungen. |
| `pasini2017innovance` | Pasini et al. (2017) | elsibaii2025open (R) | 0 | 0 | 2 | Italienische INNOVance-Bibliothek für Bauprodukte im BIM; Vergleichsansatz für Produktdatenstruktur. |
| `piazzi2022graphical` | Piazzi et al. (2022) | abualdenien2022levels (V) | 0 | 0 | 2 | Konzepte zur Spezifikation grafischer Informationsanforderungen (EIR); Ergänzung zu LOIN für die geometrische Detailtiefe. |
| `potocnik2024daylight` | Potočnik et al. (2024) | abualdenien2022levels (V) | 0 | 0 | 2 | Einfluss der Modellkomplexität auf spektrale Tageslichtsimulation; Mindestdetailtiefe für Licht-Empfehlungen. |
| `potter2025sleep` | Potter et al. (2025) | brown2022recommendations (V) | 0 | 0 | 2 | Narratives Review zur Schlafumgebung (Licht, Lärm, Temperatur) im Wohnraum; Übersicht für Empfehlungen. |
| `scott1993interior` | Scott (1993) | dosen2016prospect (R) | 0 | 0 | 2 | Präferenzrelevante visuelle Merkmale von Innenräumen (Faktorenanalyse); Grundlage für Interior-Empfehlungen. |
| `spitschan2021luox` | Spitschan et al. (2021) | brown2022recommendations (R) | 0 | 0 | 2 | Offene Web-Plattform zur Berechnung physiologisch relevanter Lichtgrößen (mEDI nach CIE S 026); übernehmbares Open-Source-Werkzeug für Lichtnachweise. |
| `stamps2006interior` | Stamps (2006) | dosen2016prospect (R) | 0 | 0 | 2 | Zwei Experimente zu Prospect-Refuge in Innenräumen; Übertragung der Theorie von Landschaft auf Räume. |
| `trinh2023medi` | Trinh et al. (2023) | brown2022recommendations (V) | 0 | 0 | 2 | Bestimmung und Messung der melanopischen Beleuchtungsstärke (mEDI) für integrative Beleuchtung; operationalisiert Brown et al. (2022) für die Lichtplanung. |
| `ulusoy2020semantics` | Ulusoy et al. (2020) | dosen2016prospect (V) | 0 | 0 | 2 | Farbsemantik in Wohninnenräumen je Raumtyp; Grundlage für Farbempfehlungen in der Bemusterung. |
| `ulusoy2024preferences` | Ulusoy (2024) | dosen2016prospect (V) | 0 | 0 | 2 | Farbpräferenzen für Flächenformen auf Innenwänden im Wohnbau; ergänzende Evidenz zu Farbe (schwächere Quelle). |
| `vanberlo2014dutch` | van Berlo & Bomhof (2014) | abualdenien2022levels (R) | 0 | 0 | 2 | Entwicklung der niederländischen BIM-Informationsniveaus als nationaler Standard; Vergleich zu LOD/LOIN. |
| `vareilles2013renovation` | Vareilles et al. (2013) | meseguer2006soft (V) | 1 | 0 | 2 | Konfiguration vorgefertigter Fassadenelemente zur Sanierung als Constraint-Satisfaction-Problem; Fassade + Solver. |
| `wichlinski2022sleep` | Wichlinski (2022) | spoerrle2010sleeping (V) | 0 | 0 | 2 | Evolutionspsychologische Übersicht zur Verwundbarkeit im Schlaf; theoretische Stütze für Bettplatzierung. |
| `wonka2003instant` | Wonka et al. (2003) | kelly2011interactive (R) | 0 | 0 | 2 | Split-Grammatiken für automatische Architekturmodellierung; regelbasierte Fassadengliederung. |
| `zhang2026taboos` | Zhang et al. (2026) | spoerrle2010sleeping (V) | 0 | 0 | 2 | Kansei-Experiment zu traditionellen Raumtabus bei "Halbgläubigen" (Hotelzimmer); relevant für optionale Kulturprofile. |
| `zhao2025mep` | Zhao et al. (2025) | johnsson2009defects (V) | 0 | 0 | 2 | Review zu Modulteilungsmethoden für TGA-Systeme (MEP); Grundlage für Leitungsführung über Elementgrenzen. |

## E Sättigungseinschätzung

- **Gesamt:** Dublettenquote 16% (42 von 257 Kandidaten). Die Runde hat 175 neue Quellen mit Relevanz ≥ 2 geliefert; das Abbruchkriterium aus 2a.3 Nr. 3 ist nicht erfüllt.
- **Nahe an Sättigung:** Wirkung von Konfiguratoren und Nacharbeit (Nachtrag Q477–Q502: 12 von 31 Kandidaten Dubletten, weil `lit-H-ff4-ff5.bib` dieses Feld schon abdeckt), LLM-BIM-Kern (Text2BIM rückwärts: 5 von 15) und Prospect-Refuge/Neuroarchitektur (6 von 23). Hier ist die nächste Runde voraussichtlich klein.
- **Nicht gesättigt:** (a) Freitext-zu-Konfiguration und bedarfsbasierte Konfiguratoren (FF3, neue Linie), (b) Mass-Customization-Marketing zu Toolkits und Selbstdesign (FF5), (c) Dachgeometrie/Straight Skeletons, (d) Reifegrade/LOIN und Produktdaten, (e) Licht- und Lärmwirkung im Wohnraum (FF6).
- **Lücken dieser Runde:** Rückwärts nicht erhoben für Q213 (keine Referenzen in OpenAlex), Q234 (Dissertation nicht indexiert), Q344 und Q453 (Bücher), Q384 (Kapitel). Bei Sammelabfragen über 200 Treffern wurde nur die erste Seite gesichtet (Brown/Basner rückwärts 200 von 206, Q477-Gruppe rückwärts 200 von 242, Q490/Q493 vorwärts 200 von 205). Vorwärts bei Startquellen mit mehr als 400 Zitierenden nur gezielt (Filter), nicht erschöpfend. Semantic Scholar war nicht nutzbar; OpenAlex-Zitationsgraphen sind für Tagungsbände (eCAADe, CAADRIA) lückenhaft.
- **Empfehlung Runde 2:** Startmenge aus den neuen Quellen mit Relevanz 3: `bakhshi2021dfma`, `campogay2026quality`, `chateauvieuxhellwig2022timber`, `chateauvieuxhellwig2025schallschutz`, `dineniso7817-1`, `elghaish2022voice`, `held2017roofs`, `hvam2006quotation`, `hwang2018window`, `oh2008critiquing`, `park2026bimllm`, `randall2005principles`, `raposo2024bridging`, `ren2021roof`, `suznjevic2025longitudinal`, `trentin2011overcoming`, `wang2022natural`, `wiener2007isovist`, `wu2026alterations`. Zusätzlich die Referenzlisten der Dissertation Châteauvieux (2023) aus dem mediaTUM-PDF und von Kwiecinski et al. (2019) aus CumInCAD manuell erheben.

## F Nächste Schritte

1. Neue Quellen in `quellen-master.csv` übernehmen (IDs fortlaufend) und in `quellen-bewertung.csv` einzeln nach 2a.5 bewerten; die vorläufigen ff-Werte oben sind nur eine Screening-Einstufung.
2. Crossref-Abgleich vor Abgabe (2a.7): Heftjahrgänge, bei denen OpenAlex das Online-Jahr führt, sind im `note`-Feld markiert.
3. Runde 2 mit der Startmenge aus Abschnitt E.

## G Anhang: ausgeschlossene Kandidaten

| DOI / Quelle | Grund |
|---|---|
| 10.1007/978-3-658-33519-9_17 | Büro-Kontext, ff6=1 |
| 10.1007/bf00872289 | redundant zu Fischer 1989/1993 |
| 10.1007/s10901-024-10135-4 | Smart-Home-Psychologie, ff6=1 |
| 10.1016/j.apacoust.2017.01.012 | Massivbau Korea, ff6=1 |
| 10.1016/j.autcon.2017.03.011 | Toleranzen Modulbau, ff6=1 |
| 10.1016/j.autcon.2018.05.011 | Modellierleistung, ff5=1 |
| 10.1016/j.autcon.2022.104470 | GAN-Grundrisse, kein FF3-Baustein (ff3=1) |
| 10.1016/j.autcon.2023.105187 | generative Tragwerksbilder, ff3=1 |
| 10.1016/j.autcon.2024.105817 | Regelumwandlung für ACC → FF2 (Parallelagent) |
| 10.1016/j.caeai.2026.100682 | Lehrkontext Studierende, ff5=1 |
| 10.1016/j.enbuild.2024.114788 | redundant zu EPlus-LLM, ff3=1 |
| 10.1016/j.ijpe.2020.107775 | Temperaturregler-Fall, ff5=1 |
| 10.1080/0144619032000134093 | Kundenorientierung allgemein, ff5=1 |
| 10.1080/0144619032000134129 | Lieferkette, ff5=1 |
| 10.1080/17480272.2021.1903993 | Produktplattform → FF1/FF2 |
| 10.1086/341573 | Web-Priming, ff5=1 |
| 10.1108/imds-05-2016-0185 | redundant zu trentin2014 |
| 10.1109/cw.2014.17 | Vorfassung von 10.1007/978-3-662-49247-5_2 |
| 10.1109/ieem58616.2023.10406559 | Nachhaltigkeitskonfigurator, Interviewstudie, ff5=1 |
| 10.1109/tg.2019.2957733 | Spiele-Innenräume, ff6=1 |
| 10.1111/j.1540-5885.2008.00321.x | Nutzer-Communities, ff5=1 |
| 10.1145/3807955 | lernbasierte Dachgenerierung, nicht regelbasiert (ff6=1) |
| 10.1145/74224.74233 | redundant zu 10.1145/67449.67501 |
| 10.1287/mksc.1040.0109 | redundant zu iyengar2000choice (Q120) |
| 10.1287/mksc.1070.0302 | Standardprodukt vs. MC, ff5=1 |
| 10.1287/mnsc.2021.04025 | Preis-/Informationsmodell, ff5=1 |
| 10.14288/1.0076315 | Produktionsplanung, ff5=1 |
| 10.3390/buildings12111896 | Konzeptpapier, ff5=1 |
| 10.3390/buildings13071861 | Bildgenerierung, keine Modelländerung (ff3=1) |
| 10.3390/su14074084 | redundant zu su12020530 |
| 10.3390/su14074141 | Leitfaden Sozialbau, ff5=1 |
| 10.3390/systems13080674 | redundant zu Informationsreife (s00163-025-00450-4) |
| 10.70401/jbde.2026.0034 | Zeitschrift ohne Indexierung, redundant |
| 10.7939/r39g5gq7z | redundant zu liu2018bim (Q241), Zeitschriftenfassung im Bestand |
| Architext (Galanos et al. 2023) | Text → Grundriss ohne deterministische Modelländerung, ff3=1 |
| Graph2Plan (Hu et al. 2020) | lernbasierte Grundrissgenerierung, ff3=1 |
| Strategies for Design Science Research Evaluation (Pries-Heje et al. 2008) | durch FEDS (venable2016feds, Q156) überholt |

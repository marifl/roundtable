# Recherche 28: Schneeballverfahren Runde 3 (gezielt: R3-Funde, FF3, FF2/FF4)

Status: v0.1 (27.09.2026), **Teilergebnis, Runde nicht abgeschlossen.** Nicht committet. Gehört zu `../arbeit/02a-review-protokoll.md` (2a.3 Nr. 3, 2a.6 Schritt 4) und setzt Runde 2 fort (`26-schneeball-runde-2.md`; Methodik Runde 1: `24-schneeball-ff1-ff2-ff4.md`, `25-schneeball-ff3-ff5-ff6.md`).
Literaturdatei: `../arbeit/literatur/lit-L-schneeball-runde3.bib` (7 Einträge, alle [V] über Verlags-/Repositoriumsseiten per Websuche; Crossref-Abgleich ausstehend).

**Verfahren:** Wohlin (2014), eine Iteration je Startquelle, rückwärts (Referenzen) und vorwärts (zitierende Arbeiten), Screening gegen FF1–FF6 nach `literatur/bewertung/AUFTRAG.md`. Aufnahme nur bei Relevanz ≥ 2 in mindestens einer FF und bibliografisch bestätigter Existenz. Maßstäbe für Relevanz 2 und 3, Umgang mit fremden Domänen (höchstens 1) und mit redundanten Funden wie in Runde 2 (Recherche 26, Einleitung).

## Ergebnis in Kürze

1. **Abbruch nach Teil (a).** Nach den Abfragen für die drei Relevanz-3-Startquellen war das Kontingent des Exa-Dienstes erschöpft (HTTP 402, 27.09.2026, 18:47 UTC). Alle anderen Wege zu Zitationsdaten sind per Egress-Proxy gesperrt (403): api.openalex.org, openalex.org, api.semanticscholar.org, www.semanticscholar.org, api.crossref.org, doi.org, OpenAIRE, Wikidata, fatcat, Unpaywall, ORCID, DataCite sowie die Verlagsseiten (ScienceDirect, Springer, T&F, MDPI, ACM, IEEE). Auch WebFetch ist für diese Hosts gesperrt. Übrig bleibt nur die Websuche. Sie liefert Titel, URLs und Kurzfassungen, aber keine Referenzlisten und keine Listen zitierender Arbeiten. Damit lässt sich kein Schneeball durchführen.
2. **Bearbeitet:** 3 von 53 Startquellen (`wei2025texttostructure`, `an2020bimbased`, `zhang2022bimbased`), beide Richtungen vollständig.
   - 193 Datensätze gesichtet (rückwärts 114, vorwärts 79)
   - 49 Kandidaten, davon 20 Bestand und 2 schon in Runde 2 ausgeschlossen
   - 27 neue Kandidaten, **7 aufgenommen**, davon **1 mit Relevanz 3** (`cao2022ontologybased`)
3. **Offen:** 50 Startquellen aus den Clustern FF3 (12) und FF2/FF4 (38). Laut OpenAlex-Metadaten sind das rund 1 760 Referenzen und 2 590 Zitierende. Bei `mcdermott1982rulebased` (957 Zitierende) ist ein Themenfilter nötig.
4. **Sättigung:** **Nicht nachgewiesen, die Suche kann nicht als gesättigt abgeschlossen werden.**
   - Im bearbeiteten Teil liegt die Rohquote bei 3,6 % und damit über der Abbruchschwelle aus Runde 2 (unter 2 %).
   - Mit `cao2022ontologybased` kommt eine neue Quelle mit Relevanz 3 hinzu. Sie stammt aus derselben Linie wie `an2020bimbased`: Fertigbarkeitsprüfung im Entwurf, Herstellerregeln als Daten.
   - Für die Cluster FF3 und FF2/FF4 gibt es noch keine Messung.
   - Die Zeichen der Sättigung nehmen zu: Die Trefferquote je neuem Kandidaten sinkt auf 26 %, und 41 % der Kandidaten sind Bestandsdubletten.

## 1 Startmenge

**Auswahlregel** (Auftrag, Empfehlung aus Recherche 26 Abschnitt 6):

- **(a)** die drei Relevanz-3-Funde aus Runde 2: `wei2025texttostructure`, `an2020bimbased`, `zhang2022bimbased`
- **(b)** alle in Runde 2 aufgenommenen Quellen (`lit-J-schneeball-runde2.bib`), die zwei Bedingungen erfüllen:
  - Sie stammen aus einer Startquelle der Cluster „Sprache/Konfiguration (FF3)“ oder „Regelprüfung/Bauantrag (FF2/FF4)“.
    - FF3: `park2026bimllm`, `wang2022natural`, `wu2026alterations`
    - FF2/FF4: `bloch2023unbalanced`, `fischer2024extending`, `lee2026automated`, `narayanaswamy2019bim`, `niemeijer2014freedom`, `nuyts2024comparative`, `pinto2026exhaustive`, `senousy2026automated`, `urban2026development`, `wu2025design`, `zentgraf2023concept`, `zhang2023rule`
    - Die Zuordnung geht über das Feld „Schneeball R2 von“.
  - Sie haben dort, also in ff2, ff3 oder ff4, vorläufig Relevanz ≥ 2.

**Ergebnis:** 51 Quellen nach (b), dazu `an2020bimbased` und `zhang2022bimbased` nach (a). `wei2025texttostructure` erfüllt (a) und (b). Zusammen sind das **53 Startquellen**.

- Die sieben in Recherche 26 namentlich empfohlenen Quellen sind alle enthalten: `yin2023twostage`, `guo2025advancing`, `yang2026llmpowered`, `hagedorn2025ontobpr`, `fauth2025baugenehmigungsv`, `hartmann2026status`, `recski2024briseplandok`.
- **Abgrenzung:**
  - Nicht aufgenommen sind die elf Cluster-Funde ohne ff2/ff3/ff4 ≥ 2, etwa `barr2015oracle`, `lewis2018system` und `mattern2018bimbased`.
  - Ebenfalls nicht aufgenommen sind 19 Quellen mit ff2/ff3/ff4 ≥ 2 aus anderen Clustern, etwa die Konfigurations- und Erklärungsliteratur aus `trentin2011overcoming`, `gregor1999explanations` und `vestin2022information`. Diese Cluster gelten nach Recherche 26 als gesättigt.
- Die Startquellen wurden nicht erst in `quellen-bewertung.csv` eingepflegt, wie es Recherche 26 vorsah (Kernbestand P ≥ 5). Die Auswahl folgt stattdessen der vorläufigen Relevanz. Die Menge ist damit eher weiter gefasst.

Alle 53 sind in OpenAlex auffindbar (DOI-Filter, `vanberlo2019creating` per Titelsuche). Relevanz ff1–ff6 wie in `lit-J` (vorläufig). „Refs / Zit. (OpenAlex)“ = `referenced_works_count` / `cited_by_count` am 27.09.2026. „gesichtet r / v“ = tatsächlich abgerufene Datensätze.

| Nr. | Key | Gruppe | ff1–ff6 | OpenAlex-ID | Refs / Zit. (OpenAlex) | gesichtet r / v | Status |
|---|---|---|---|---|---|---|---|
| 1 | `ghannad2019automated` | (b) FF2/FF4 | 1/2/0/0/0/0 | W2919359201 | 33 / 77 | – | offen |
| 2 | `olsson2018automation` | (b) FF2/FF4 | 0/2/0/1/0/0 | W2886998832 | 43 / 73 | – | offen |
| 3 | `fauth2022conceptual` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4280561253 | 23 / 37 | – | offen |
| 4 | `fischer2023automation` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4386913954 | 51 / 25 | – | offen |
| 5 | `ilal2022integrating` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4281296798 | 79 / 12 | – | offen |
| 6 | `meijer2006deregulation` | (b) FF2/FF4 | 0/0/0/2/0/0 | W2062705329 | 6 / 42 | – | offen |
| 7 | `ciotta2021structural` | (b) FF2/FF4 | 1/0/0/2/0/0 | W3214910372 | 12 / 14 | – | offen |
| 8 | `krischmann2020entwicklung` | (b) FF2/FF4 | 0/2/0/2/0/0 | W3122483860 | 0 / 11 | – | offen |
| 9 | `messaoudi2020virtual` | (b) FF2/FF4 | 0/0/0/2/0/0 | W3042773534 | 4 / 10 | – | offen |
| 10 | `meijer2017quality` | (b) FF2/FF4 | 0/0/0/2/0/0 | W2742182325 | 20 / 23 | – | offen |
| 11 | `daum2014processing` | (b) FF2/FF4 | 0/2/0/0/0/0 | W1991959674 | 42 / 126 | – | offen |
| 12 | `yang2024promptbased` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4403320529 | 68 / 50 | – | offen |
| 13 | `kruiper2024platformbased` | (b) FF2/FF4 | 0/2/0/1/0/0 | W4400150442 | 86 / 34 | – | offen |
| 14 | `hagedorn2025ontobpr` | (b) FF2/FF4 | 0/2/0/2/0/0 | W4410251223 | 92 / 20 | – | offen |
| 15 | `mowbray2023representing` | (b) FF2/FF4 | 0/2/0/1/0/0 | W4321770013 | 0 / 12 | – | offen |
| 16 | `hjelseth2015public` | (b) FF2/FF4 | 0/2/0/1/0/0 | W2239149652 | 6 / 22 | – | offen |
| 17 | `gelle2003solving` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2141123969 | 52 / 64 | – | offen |
| 18 | `zech2024bimreason` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4405199717 | 21 / 7 | – | offen |
| 19 | `recski2024briseplandok` | (b) FF2/FF4 | 0/2/2/0/0/0 | W4400383903 | 48 / 4 | – | offen |
| 20 | `lottaz1998constraint` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2170990972 | 27 / 19 | – | offen |
| 21 | `lee2006specifying` | (b) FF2/FF4 | 2/2/0/0/0/0 | W2104143012 | 51 / 398 | – | offen |
| 22 | `zimmermann2013computing` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2135611412 | 23 / 89 | – | offen |
| 23 | `lee2019efficient` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2917212430 | 36 / 50 | – | offen |
| 24 | `esser2022graphbased` | (b) FF2/FF4 | 2/0/0/2/0/0 | W4283270306 | 56 / 30 | – | offen |
| 25 | `urban2025augmented` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4416404543 | 22 / 5 | – | offen |
| 26 | `solimanjunior2022designers` | (b) FF2/FF4 | 0/2/0/0/1/0 | W4206152562 | 74 / 10 | – | offen |
| 27 | `fauth2023process` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4389511728 | 48 / 12 | – | offen |
| 28 | `sei2025understanding` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4410396153 | 35 / 10 | – | offen |
| 29 | `liu2025coordination` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4415736509 | 39 / 5 | – | offen |
| 30 | `akbas2025holistic` | (b) FF2/FF4 | 2/2/0/0/0/2 | W4410568467 | 23 / 3 | – | offen |
| 31 | `fauth2025baugenehmigungsv` | (b) FF2/FF4 | 0/0/0/2/2/0 | W4410774337 | 17 / 3 | – | offen |
| 32 | `fauth2024pace` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4397000832 | 28 / 3 | – | offen |
| 33 | `weinkauf2024decision` | (b) FF2/FF4 | 0/2/0/2/0/0 | W4405481878 | 23 / 1 | – | offen |
| 34 | `feng2026bridging` | (b) FF2/FF4 | 0/0/2/0/0/2 | W7127341327 | 31 / 0 | – | offen |
| 35 | `yang2026llmpowered` | (b) FF2/FF4 | 0/2/2/0/0/0 | W7162694042 | 5 / 0 | – | offen |
| 36 | `hartmann2026status` | (b) FF2/FF4 | 1/0/0/2/0/0 | W7164846815 | 11 / 0 | – | offen |
| 37 | `fauth2023requirements` | (b) FF2/FF4 | 1/0/0/2/0/0 | W4383682229 | 12 / 4 | – | offen |
| 38 | `vanberlo2019creating` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2982547348 | 0 / 6 | – | offen |
| 39 | `wang2022transfer` | (b) FF3 | 0/0/2/0/0/0 | W4281756024 | 58 / 41 | – | offen |
| 40 | `yin2023twostage` | (b) FF3 | 0/0/2/0/0/0 | W4367838951 | 84 / 30 | – | offen |
| 41 | `guo2025advancing` | (b) FF3 | 0/0/2/0/0/0 | W4412072183 | 33 / 27 | – | offen |
| 42 | `gao2025lifecycle` | (b) FF3 | 0/2/0/0/0/0 | W4409096846 | 94 / 18 | – | offen |
| 43 | `bagasi2025bim` | (b) FF3 | 0/0/2/0/1/0 | W4411158086 | 35 / 17 | – | offen |
| 44 | `dong2025bim` | (b) FF3 | 0/0/2/0/0/0 | W4414568512 | 54 / 17 | – | offen |
| 45 | `jin2026evaluating` | (b) FF3 | 0/0/2/0/0/0 | W7135017563 | 45 / 4 | – | offen |
| 46 | `mcdermott1982rulebased` | (b) FF3 | 0/2/0/0/0/0 | W2005004006 | 15 / 957 (Filter nötig) | – | offen |
| 47 | `wang2018mapping` | (b) FF3 | 0/0/2/0/0/0 | W2799557147 | 16 / 78 | – | offen |
| 48 | `xie2005modelling` | (b) FF3 | 0/2/0/0/0/0 | W2154241265 | 9 / 81 | – | offen |
| 49 | `rasmussen2020guidelines` | (b) FF3 | 0/2/0/0/0/0 | W3029987277 | 43 / 9 | – | offen |
| 50 | `dudek2023mass` | (b) FF3 | 0/1/2/0/1/0 | W4362453679 | 30 / 0 | – | offen |
| 51 | `wei2025texttostructure` | (a) R3, zugleich (b) FF3 | 0/0/3/0/0/0 | W4408393296 | 88 / 10 | 65 / 10 | **bearbeitet** |
| 52 | `an2020bimbased` | (a) R3 | 2/3/0/0/0/0 | W2998429966 | 28 / 53 | 23 / 53 | **bearbeitet** |
| 53 | `zhang2022bimbased` | (a) R3 | 2/0/0/0/0/3 | W4293084103 | 26 / 16 | 26 / 16 | **bearbeitet** |

**Befund zur Startmenge:**
- Die Startmenge ist stark nach FF4 und FF2 ausgerichtet: 38 Quellen aus dem Bauantrags- und Regelprüfungs-Cluster, 12 aus Sprache/Konfiguration, 3 R3-Funde.
- Elf Startquellen haben höchstens 3 Zitierende, meist Arbeiten von 2024 bis 2026. Zwei haben in OpenAlex keine Referenzen (`krischmann2020entwicklung`, `mowbray2023representing`), `vanberlo2019creating` ebenfalls nicht. Diese Quellen hätten auch bei freiem Zugang wenig beigetragen.

## 2 Suchweg, Werkzeuge und Sperren

- **Kanten:** OpenAlex über `mcp__Exa__web_fetch_exa`, wie in Runde 2:
  - rückwärts `works?filter=cited_by:<W-ID>`
  - vorwärts `works?filter=cites:<W-ID>`
  - jeweils `per_page=200`, eine Seite genügte
  - Startquellen-Metadaten per DOI-Filter (zwei Sammelabfragen mit je 26 DOIs)
- **Sperre ab der vierten Startquelle:**
  - Exa meldet ab 18:47 UTC „exceeded your credits limit“ (402), für `web_fetch_exa` und `web_search_exa`.
  - Direktzugriffe per `curl` scheitern an allen oben genannten Hosts mit CONNECT 403. Laut `/root/.ccr/README.md` ist das eine Richtlinienentscheidung der Umgebung und nicht zu umgehen.
  - WebFetch meldet für api.openalex.org und semanticscholar.org „EGRESS_BLOCKED“.
- **Verifikation:**
  - Crossref war nicht erreichbar, weder direkt noch über Exa.
  - Existenz, Autoren, Venue, Band und Artikelnummer der 7 aufgenommenen Quellen sind stattdessen über die Websuche geprüft. Maßgeblich waren Treffer auf der Verlagsseite (ScienceDirect-PII, ACM DL, PLOS/PubMed/PMC, nature.com) und in mindestens einem Repositorium. Die Kurzfassung stammt aus denselben Treffern.
  - Nicht belegte Felder sind weggelassen, etwa der Band bei `cortezlara2026bimsimulated`. Bei zwei Einträgen sind die Vornamen nur als Initialen belegt, bei `kim2022bim` ist der Band aus dem Heftmonat abgeleitet (im `note` vermerkt).
  - Das ist schwächer als der Crossref-Weg von Runde 2. Die Einträge tragen [V] mit genauem Prüfweg. Der Crossref-Abgleich ist nach 2a.7 vor der Abgabe nachzuholen.
- **Dubletten:**
  - gegen `quellen-master.csv` (1 046 Zeilen, enthält inzwischen `lit-J`) und alle `lit-*.bib` (DOI exakt, Titel normalisiert auf 60 Zeichen, Präfixabgleich)
  - zusätzlich gegen die ausgeschlossenen Kandidaten aus Runde 1 (Recherche 25, Anhang G) und Runde 2 (Recherche 26, Anhang A), 199 DOIs; Treffer dort zählen als Wiederholung
- **Keys:** keine Kollision mit `lit-A` … `lit-K`, `lit-J` und `quellen-master.csv`.

## 3 Protokoll je Startquelle

Zählweise wie in Runde 2: „gesichtet“ = abgerufene OpenAlex-Datensätze, „Kandidaten“ = nach Titel-Screening zur Abstract-Prüfung vorgemerkt, einschließlich Bestandsdubletten.

| Start | Refs gesichtet | Zit. gesichtet | Kandidaten r / v | davon Bestand r / v | davon früher ausgeschl. r / v | aufgenommen r / v | Anmerkung |
|---|---|---|---|---|---|---|---|
| `wei2025texttostructure` | 65 (von 88) | 10 | 13 / 4 | 6 / 1 | 1 / 0 | 2 / 0 | Referenzliste zu großen Teilen allgemeine LLM-/NLP-Literatur (arXiv, ACL-Bände), ohne Baubezug; die NL-BIM-Abfrageliteratur ist fast vollständig Bestand (`wu2019retrieval`, `shin2021bimasr`, `elghaish2022voice`, `zheng2023dynamic`, `jang2024nadia`, `tur2011spoken`). Vorwärts: 10 Zitierende 2025/2026, zwei davon ohne auffindbaren Verlagsnachweis. |
| `an2020bimbased` | 23 (von 28) | 53 | 7 / 15 | 5 / 6 | 0 / 1 | 0 / 2 | Rückwärts gesättigt (5 von 7 Kandidaten Bestand). Vorwärts: Alberta- und DfMA-Umfeld weitgehend Bestand (`mtehrani2025streamlining`, `kim2024rule`, `baradaran2022parametric`, `gharaibeh2023digital`, `loboscalquin2024implementation`); neu `cao2022ontologybased` (R3). |
| `zhang2022bimbased` | 26 | 16 | 5 / 5 | 1 / 1 | 0 / 0 | 1 / 2 | Rückwärts fast nur Wegsuch-Algorithmen (Dijkstra, A\*, Zuschnitt) und allgemeine Vorfertigungsliteratur. Vorwärts: TGA-Netzoptimierung und Tafelaufteilung. |
| **Summe (a)** | **114** | **79** | **25 / 24** | **12 / 8** | **1 / 1** | **3 / 4** | 193 Datensätze, 49 Kandidaten, 7 Aufnahmen |
| 50 Startquellen (b) | – | – | – | – | – | – | **nicht bearbeitet** (Sperre, Abschnitt 2) |

## 4 PRISMA-Zahlen und Sättigung: Vergleich R1 / R2 / R3

R3 bezieht sich nur auf den bearbeiteten Teil (a) mit 3 von 53 Startquellen. Die Werte sind deshalb nur eingeschränkt vergleichbar, siehe die Hinweise unter der Tabelle.

| Kennzahl | Runde 1 (gesamt) | Runde 2 | **Runde 3, Teil (a)** |
|---|---|---|---|
| Startquellen | 61 (56 verschieden) | 47 | **3 von 53** |
| Datensätze gesichtet (roh) | 6 437 | 4 911 | **193** (r 114, v 79) |
| Kandidaten zur Abstract-Prüfung | 468 | 411 | **49** |
| davon Bestandsdubletten | 16,3 % (Teil B) | 17,5 % (72) | **40,8 %** (20) |
| davon in früherer Runde ausgeschlossen | – | – | **2** |
| neue Kandidaten | 423 | 339 | **27** |
| ausgeschlossen | 137 | 177 | **20** |
| – Relevanz < 2 | 109 | 102 | 10 |
| – redundant | 10 | 49 | 5 |
| – Vorfassung/Tagungsfassung | 5 | 10 | 2 |
| – nicht verifizierbar | 4 | 9 | 3 |
| **aufgenommen** | 286 | 162 | **7** |
| davon Relevanz 3 | 29 (10,1 %) | 3 (1,9 %) | **1 (14 %)** |
| **Rohquote aufgenommen / gesichtet** | **4,4 %** | **3,3 %** | **3,6 %** |
| Trefferquote aufgenommen / neue Kandidaten | 67,6 % | 47,8 % | **25,9 %** |
| Anteil redundant + Vorfassung unter neuen Kandidaten | 3,5 % | 17,4 % | **25,9 %** (7 von 27) |
| Wiederholungen insgesamt unter Kandidaten (Bestand + früher ausgeschlossen + redundant + Vorfassung) | – | 32 % (131 von 411) | **59 %** (29 von 49) |

**Zur Vergleichbarkeit:**

- **Auswahl der Startquellen:** Teil (a) enthält nur die drei ertragreichsten Startquellen von Runde 2. Das hebt die Rohquote von R3 eher an, sie ist also keine Schätzung für die ganze Runde.
- **Wenige Datensätze:** Mit 193 Datensätzen ist die Zahl klein. Eine Aufnahme mehr oder weniger verschiebt die Quote um 0,5 Prozentpunkte. Der R3-Anteil von 14 % beruht auf einer einzigen Quelle.
- **Robuste Signale:** Die Wiederholungsanteile sind belastbarer als die Quote. Sie steigen von Runde zu Runde deutlich: Bestandsdubletten von 17 % auf 41 %, Wiederholungen insgesamt von 32 % auf 59 %, redundant oder Vorfassung von 3,5 % über 17 % auf 26 %.
- **Trefferquote:** Die Trefferquote je neuem Kandidaten halbiert sich gegenüber Runde 2 nahezu (47,8 % → 25,9 %).

**Urteil nach der Abbruchregel aus Recherche 26 (keine neue Relevanz 3 und Rohquote unter 2 %):**

- **Teil (a): nicht gesättigt.**
  - Die Rohquote liegt mit 3,6 % über 2 %.
  - `cao2022ontologybased` erreicht Relevanz 3.
  - Die Linie ist aber eng: Der Fund setzt `an2020bimbased` fort und belegt dasselbe zentrale Argument (Herstellerregeln als maschinenlesbares Wissen begrenzen den Entwurf in Echtzeit) mit einem ontologiebasierten, auf Holztafelbau erprobten Baustein.
  - Die Sprachlinie (`wei2025texttostructure`) ist rückwärts praktisch gesättigt: 7 von 13 Kandidaten sind Bestand oder früher ausgeschlossen, neu sind nur eine Übersicht und eine Methodenübersicht. Vorwärts ist sie noch zu jung (10 Zitierende).
- **Teil (b): nicht gemessen.** Für FF3 und FF2/FF4 fehlt jede Messung. Die Frage aus Recherche 26 bleibt offen, ob diese beiden Cluster, die in Runde 2 noch über dem Niveau von Runde 1 lieferten (9,6 % bzw. 6,6 %), jetzt abfallen.
- **Gesamt: Die Suche kann nicht als gesättigt abgeschlossen werden.** Die steigenden Wiederholungsanteile sprechen für eine nahe Sättigung. Das formale Kriterium ist aber weder für den bearbeiteten Teil erfüllt noch für den Rest prüfbar.

## 5 Aufgenommene Quellen (7)

Einteilung nach Haupt-FF wie in Runde 2. Relevanz vorläufig (Titel und Kurzfassung, kein Volltext). Relevanz 3 **fett**.

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| **`cao2022ontologybased`** | 2022 | Ontology-based manufacturability analysis automation for industrialized construction | Automation in Construction 139 | an2020bimbased (vorwärts) | 2/3/0/0/0/0 | Ontologie verbindet Bauteilmerkmale, Produktionsfähigkeiten und Fertigungsregeln. Semantisches Reasoning meldet Fertigbarkeitsverstöße dem Planer in Echtzeit, erprobt an einem Holztafelbau-Projekt (ETH Zürich). Übernehmbarer Baustein für FF2: Herstellerregeln als Daten statt Code (Zielbild, Prinzip 5). |
| `fisher2024paad` | 2024 | PAAD: Panelization algorithm for architectural designs | PLOS ONE 19(6) | zhang2022bimbased (vorwärts) | 2/1/0/0/0/0 | automatische Aufteilung von Wänden in Tafeln unter Fertigungsrestriktionen (genetischer Algorithmus, 2D-Bin-Packing), auch bei Schrägwänden und Öffnungen; stützt die Ableitung der Wandtafeln aus dem Modell (FF1) |
| `kim2022bim` | 2022 | BIM data requirements for 2D deliverables in construction documentation | Automation in Construction 140 | an2020bimbased (vorwärts) | 2/0/0/0/1/0 | Informationsanforderungen für die Planableitung aus BIM (Delphi). Der Zusatzaufwand beim Ableiten von Zeichnungen sinkt von 41 % auf 7,1 %. Stützt „Pläne sind Ableitungen“ (FF1), ergänzt `kim2024rule`. |
| `saka2023conversational` | 2023 | Conversational artificial intelligence in the AEC industry: A review of present status, challenges and opportunities | Advanced Engineering Informatics 55 | wei2025texttostructure (rückwärts) | 0/0/2/0/0/0 | Übersicht Konversations-KI (Sprache und Text) im Bauwesen: Stand, Hürden, Forschungsbedarf; Einordnung für Kap. 5.6 |
| `weld2022survey` | 2022 | A Survey of Joint Intent Detection and Slot Filling Models in Natural Language Understanding | ACM Computing Surveys 55(8) | wei2025texttostructure (rückwärts) | 0/0/2/0/0/0 | methodische Grundlage der Zerlegung in Intent und Slots, auf der `wei2025texttostructure` aufbaut; stützt die Intent-Schicht (FF3) |
| `wang2016building` | 2016 | Building information modeling-based integration of MEP layout designs and constructability | Automation in Construction 61 | zhang2022bimbased (rückwärts) | 1/0/0/0/0/2 | TGA-Modell in fünf Detaillierungsstufen vom Vorentwurf bis zum Vorfertigungsmodell; stützt Reifegrade der TGA aus einem Modell (FF6) |
| `cortezlara2026bimsimulated` | 2026 | A BIM-simulated annealing approach to optimize cost, size, and environmental impact of building water networks | Scientific Reports | zhang2022bimbased (vorwärts) | 0/0/0/0/0/2 | regelbasierte Dimensionierung und Optimierung von Gebäudewassernetzen in Revit/Python, Code offen (Zenodo); stützt TGA-Trinkwasser/Abwasser (FF6) |

**Schwerpunkt:** FF1 2, FF2 1, FF3 2, FF6 2 (nach Haupt-FF). Kein FF4-Fund. Das war zu erwarten, weil die FF4-Startquellen in Teil (b) liegen.

## 6 Nächste Schritte

1. **Zugang wiederherstellen**, eine der beiden Möglichkeiten genügt:
   - Exa-Kontingent aufladen, oder
   - in den Netzwerkeinstellungen der Umgebung `api.openalex.org` und `api.crossref.org` freigeben, besser auch `api.semanticscholar.org`.
2. **Teil (b) nachholen:** 50 Startquellen, rund 1 760 Referenzen und 2 590 Zitierende. Bei `mcdermott1982rulebased` gilt die Filterregel aus Runde 2 (Volltextfilter „building OR construction OR configurator OR architecture OR housing“).
3. **Nach der Abbruchregel zusätzlich** `cao2022ontologybased` als Startquelle in beide Richtungen (Relevanz-3-Fund aus Teil (a)).
4. **Crossref-Abgleich** der 7 Einträge aus `lit-L`: volle Vornamen, Band von `kim2022bim` und `cortezlara2026bimsimulated`, Heftjahr von `weld2022survey`.
5. **Danach** Sättigungsurteil über die ganze Runde. Die Tabelle in Abschnitt 4 um „Runde 3 gesamt“ ergänzen.

## 7 Grenzen

- Nur 3 von 53 Startquellen bearbeitet (Abschnitt 2). Alle Sättigungsaussagen gelten nur für diesen Teil.
- Verifikation über die Websuche statt über Crossref (Abschnitt 2). Die Kurzfassungen stammen aus Suchtreffern und nicht aus dem Verlagsabstract selbst. Bei der Zweitbewertung für κ bevorzugt prüfen, vor allem `cao2022ontologybased` (R3) und `kim2022bim`.
- Referenzlisten in OpenAlex sind unvollständig aufgelöst: `wei2025texttostructure` 65 von 88, `an2020bimbased` 23 von 28.
- Einstufung „redundant“ und „nicht verifizierbar“ durch einen einzelnen Bewerter (2a.7). Die Fälle sind in Anhang A begründet.

## Anhang A: ausgeschlossene bzw. nicht aufgenommene Kandidaten (42)

**Bestandsdubletten (20):**
- `zheng2023dynamic`, `wu2019retrieval`, `jang2024nadia`, `elghaish2022voice`, `shin2021bimasr`, `tur2011spoken`, `park2026bimllm` (von `wei2025texttostructure`)
- `yin2019building`, `liu2016ontology`, `manrique2015automated`, `patlakas2015potential`, `abanda2017bim`, `kim2024rule`, `lei2023measurement`, `loboscalquin2024implementation`, `gharaibeh2023digital`, `baradaran2022parametric`, `mtehrani2025streamlining` (von `an2020bimbased`)
- `tserng2011modularization`, `gao2025lifecycle` (von `zhang2022bimbased`)

**In Runde 2 bereits ausgeschlossen (2):** 10.1061/(asce)cp.1943-5487.0001019 (redundant), 10.1016/j.autcon.2020.103287 (redundant).

**Neue Kandidaten, ausgeschlossen (20):**

| DOI | Titel (gekürzt) | Start | Grund |
|---|---|---|---|
| 10.1111/mice.12151 | Natural-language-based approach to intelligent data retrieval … cloud BIM | wei2025 r | redundant (NL-BIM-Abfrage durch `wu2019retrieval`, `zheng2023dynamic`, `yin2023twostage` getragen) |
| 10.36680/j.itcon.2023.013 | Leveraging NLP for automated information inquiry from BIM | wei2025 r | redundant (wie oben) |
| 10.1016/j.compind.2022.103733 | Pretrained domain-specific language model … AEC | wei2025 r | Relevanz < 2 (Sprachmodell-Vortraining, keine Modelländerung) |
| 10.1016/j.autcon.2020.103384 | Alternatives … transformation of BIM data using semantic query languages | wei2025 r | Relevanz < 2 |
| 10.1016/j.autcon.2026.106989 | Conversational programming for structural model review and editing (CCG) | wei2025 v | nicht verifizierbar (nur OpenAlex-Datensatz, kein Verlags- oder Repositoriumsnachweis über die Websuche); inhaltlich möglicherweise FF3 = 2, **nachprüfen** |
| 10.1016/j.autcon.2026.107155 | Human–AI collaboration in architectural design: … controllability | wei2025 v | nicht verifizierbar (wie oben); **nachprüfen** |
| 10.1016/j.autcon.2026.107260 | Agentic search for BIM information extraction | wei2025 v | Relevanz < 2 (Informationsabfrage, keine Modelländerung) |
| 10.1016/j.autcon.2018.11.023 | Safe tool-paths … light gauge steel panels | an2020 r | Relevanz < 2 (Stahlleichtbau, Maschinenpfad) |
| 10.22260/isarc2019/0095 | Ontology-based knowledge modeling for frame assemblies manufacturing | an2020 r | Tagungsbeitrag derselben Linie (ISARC 2019, S. 709–715), Argument durch `an2020bimbased` und `cao2022ontologybased` getragen: redundant |
| 10.1016/j.autcon.2022.104194 | BIM-based simulation of construction robotics … wood frames | an2020 v | Relevanz < 2 (Robotersimulation Montage) |
| 10.1016/j.autcon.2023.105191 | Target-path planning and manufacturability check for robotic CLT machining | an2020 v | redundant zu `an2020bimbased`/`cao2022ontologybased`; Brettsperrholz statt Holzrahmenbau |
| 10.1061/jcemd4.coeng-15141 | Defining information requirements for off-site construction management (Canada) | an2020 v | Relevanz < 2 (Managementinformation) |
| 10.22260/isarc2020/0047 | BIM-based approach for optimizing HVAC design … panelized houses | an2020 v | Tagungsfassung zu `baradaran2022parametric` (Bestand) |
| 10.1155/2021/6638236 | BIM-based generative design for drywall installation planning | an2020 v | Relevanz < 2 |
| 10.1016/j.autcon.2024.105945 | Automation in manufacturing and assembly of industrialised construction | an2020 v | Relevanz < 2 (Übersicht, Argument im Bestand) |
| 10.1061/9780784482865.121 | BIM-based automated drainage system design in prefabrication construction | zhang2022 r | Tagungsfassung zu `zhang2022bimbased` |
| 10.1016/j.autcon.2019.03.021 | DSM and hierarchical clustering … module identification in MEP systems | zhang2022 r | redundant zu `tserng2011modularization`, `suarez2023optimizing` |
| 10.3390/app7060547 | Modular and offsite construction of piping: barriers and route | zhang2022 r | Relevanz < 2 |
| 10.3390/app131910847 | Concealed conduit routing in building slabs | zhang2022 v | Relevanz < 2 (Leerrohrführung in Stahlbetondecken, auf Holzrahmenbau nicht übertragbar) |
| 10.1016/j.eswa.2026.133364 | BIM-integrated generative wiring design for residential interior lighting circuits (ILP) | zhang2022 v | nicht verifizierbar (DOI und Titel nur in OpenAlex, kein Verlagsnachweis über die Websuche); inhaltlich wahrscheinlich FF6 = 2 (Elektro-Routing Wohnbau), **nachprüfen** |

**Hinweis ohne Aufnahme** (kein Schneeball-Fund, nur als Beifang der Websuche): IEDW, ein BIM-basierter Algorithmus für die Elektroverteilung im Innenraum (Advanced Engineering Informatics 2023, ScienceDirect S1474034623001271). Er ist ein möglicher FF6-Kandidat für eine Lückenrecherche TGA-Routing, gehört aber nicht zum Zitationsnetz dieser Runde und wird hier nicht gezählt.

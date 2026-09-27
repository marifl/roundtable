# Recherche 28: Schneeballverfahren Runde 3 (gezielt: R3-Funde, FF3, FF2/FF4)

Status: v0.2 (27.09.2026), **Runde abgeschlossen** (Teil (a), Teil (b), Anschlussprüfung (c)). Nicht committet. Gehört zu `../arbeit/02a-review-protokoll.md` (2a.3 Nr. 3, 2a.6 Schritt 4) und setzt Runde 2 fort (`26-schneeball-runde-2.md`; Methodik Runde 1: `24-schneeball-ff1-ff2-ff4.md`, `25-schneeball-ff3-ff5-ff6.md`).
Literaturdatei: `../arbeit/literatur/lit-L-schneeball-runde3.bib` (26 Einträge: 7 aus Teil (a), [V] über Verlags-/Repositoriumsseiten, inzwischen per Crossref bestätigt; 3 Nachträge zu Teil (a) und 16 aus Teil (b), [V] über Crossref; Abschnitt 8).

**Verfahren:** Wohlin (2014), eine Iteration je Startquelle, rückwärts (Referenzen) und vorwärts (zitierende Arbeiten), Screening gegen FF1–FF6 nach `literatur/bewertung/AUFTRAG.md`. Aufnahme nur bei Relevanz ≥ 2 in mindestens einer FF und bibliografisch bestätigter Existenz. Maßstäbe für Relevanz 2 und 3, Umgang mit fremden Domänen (höchstens 1) und mit redundanten Funden wie in Runde 2 (Recherche 26, Einleitung).

## Ergebnis in Kürze

1. **Ablauf:**
   - Teil (a) mit den drei Relevanz-3-Startquellen lief vollständig. Danach war das Exa-Kontingent erschöpft (HTTP 402, 18:47 UTC), die Runde wurde unterbrochen. Teil (a) ist in den Abschnitten 2, 3 und 5 im Stand vor der Unterbrechung dokumentiert.
   - Nach dem Aufladen folgten Teil (b) mit den übrigen 50 Startquellen (Abschnitte 8–10) und nach der Abbruchregel aus Recherche 26 die Anschlussprüfung (c) mit dem Relevanz-3-Fund `cao2022ontologybased` aus Teil (a) (Abschnitt 11).
2. **Umfang Runde 3 gesamt (a + b):**
   - 53 Startquellen, **3 641 Datensätze** gesichtet (rückwärts 1 648, vorwärts 1 993)
   - 545 Kandidaten, davon 187 Bestand (34 %) und 54 schon in Runde 1, 2 oder Teil (a) ausgeschlossen
   - 304 neue Kandidaten, **26 aufgenommen** (10 aus (a) einschließlich 3 Nachträgen, 16 aus (b)), davon **1 mit Relevanz 3** (`cao2022ontologybased`, Teil (a))
   - Teil (c): 108 Datensätze, 26 Kandidaten, **keine Aufnahme**
3. **Quoten:**
   - Rohquote aufgenommen/gesichtet: Runde 3 gesamt **0,71 %**, Teil (b) **0,46 %**, Teil (c) **0 %** (Runde 1: 4,4 %, Runde 2: 3,3 %)
   - Trefferquote je neuem Kandidaten: 8,6 % (Runde 2: 47,8 %)
   - Wiederholungen unter den Kandidaten (Bestand, früher ausgeschlossen, redundant, Vorfassung): 54 % (Runde 2: 32 %)
   - Die beiden Cluster, die in Runde 2 noch über Runde 1 lagen, fallen deutlich ab: FF3 von 9,6 % auf 0,86 %, FF2/FF4 von 6,6 % auf 0,29 %.
4. **Stärkste neue Befunde aus Teil (b), alle Relevanz 2:**
   - **FF4:** europäischer Vergleich der Genehmigungsverfahren in 17 Ländern (`fauth2024investigating`); Folgen privatisierter Bauaufsicht (`vanderheijden2010peanuts`); Vorfertigung passt schlecht zu baustellenbezogener Aufsicht (`meacham2022fire`); Kosten der Verfahrensvorschriften einer Landesbauordnung (`schleich2018kosteneinsparpotenziale`)
   - **FF3:** Zuverlässigkeit LLM-generierter BIM-Skripte, 48 % der Fehler API-Fehlgebrauch (`alwashah2026reliable`); Modelländerung über definierte Werkzeuge (`gao2026multiagent`); natürliche Sprache bis Fertigungsdaten im individualisierten Wohnbau (`yang2026natural`, nur nach Titel eingestuft)
   - **FF2:** Diagnose unvereinbarer Kundenwünsche im Konfigurator (`felfernig2011personalized`); Wissensbasis getrennt von der Inferenz (`vanhertum2016kb`); Holzvorfertigungsregeln im Einfamilienhausentwurf (`ostrowskawawryniuk2020prefabrication`)
   - **FF5:** Rückmeldung zu Bauvorschriften im Frühentwurf (`nowak2023identifying`); Transparenz und Vertrauen in digitale Genehmigungssysteme (`xiao2026trusting`); Nutzerbewertung eines sprachgesteuerten BIM-Systems (`jang2026understanding`)
5. **Sättigung: erreicht, das Schneeballverfahren ist abgeschlossen** (Abschnitt 4).
   - Die Abbruchregel aus Recherche 26 lautet: keine neue Quelle mit Relevanz 3 und Rohquote unter 2 %.
   - Teil (b) erfüllt beide Bedingungen (0 Relevanz-3-Funde, 0,46 %).
   - Der einzige Relevanz-3-Fund der Runde (`cao2022ontologybased`, Teil (a)) wurde nach der Regel weiterverfolgt. Die Anschlussprüfung (c) liefert keine Aufnahme (0 %).
   - Das strenge Ursprungskriterium aus 2a.3 Nr. 3 („keine neue Quelle mit Relevanz ≥ 2“) ist mit 26 Aufnahmen nicht erfüllt. Für Runde 3 hat Recherche 26 aber die Abbruchregel an seine Stelle gesetzt.

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

Alle 53 sind in OpenAlex auffindbar (DOI-Filter, `vanberlo2019creating` per Titelsuche). Relevanz ff1–ff6 wie in `lit-J` (vorläufig). „Refs / Zit. (OpenAlex)“ = `referenced_works_count` / `cited_by_count` am 27.09.2026. „gesichtet r / v“ = tatsächlich abgerufene Datensätze. In Teil (b) wurden kleine Startquellen teils gemeinsam abgefragt (OpenAlex-Filter mit ODER); G1 bis G14 bezeichnen diese Sammelabfragen, Aufschlüsselung in Abschnitt 8.

| Nr. | Key | Gruppe | ff1–ff6 | OpenAlex-ID | Refs / Zit. (OpenAlex) | gesichtet r / v | Status |
|---|---|---|---|---|---|---|---|
| 1 | `ghannad2019automated` | (b) FF2/FF4 | 1/2/0/0/0/0 | W2919359201 | 33 / 77 | 29 / 77 | **bearbeitet (b)** |
| 2 | `olsson2018automation` | (b) FF2/FF4 | 0/2/0/1/0/0 | W2886998832 | 43 / 73 | 42 / 72 | **bearbeitet (b)** |
| 3 | `fauth2022conceptual` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4280561253 | 23 / 37 | 22 / 36 | **bearbeitet (b)** |
| 4 | `fischer2023automation` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4386913954 | 51 / 25 | 42 / 24 | **bearbeitet (b)** |
| 5 | `ilal2022integrating` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4281296798 | 79 / 12 | 75 / 12 | **bearbeitet (b)** |
| 6 | `meijer2006deregulation` | (b) FF2/FF4 | 0/0/0/2/0/0 | W2062705329 | 6 / 42 | G1 / 42 | **bearbeitet (b)** |
| 7 | `ciotta2021structural` | (b) FF2/FF4 | 1/0/0/2/0/0 | W3214910372 | 12 / 14 | G1 / G2 | **bearbeitet (b)** |
| 8 | `krischmann2020entwicklung` | (b) FF2/FF4 | 0/2/0/2/0/0 | W3122483860 | 0 / 11 | 0 / G2 | **bearbeitet (b)** |
| 9 | `messaoudi2020virtual` | (b) FF2/FF4 | 0/0/0/2/0/0 | W3042773534 | 4 / 10 | G1 / G2 | **bearbeitet (b)** |
| 10 | `meijer2017quality` | (b) FF2/FF4 | 0/0/0/2/0/0 | W2742182325 | 20 / 23 | 19 / 23 | **bearbeitet (b)** |
| 11 | `daum2014processing` | (b) FF2/FF4 | 0/2/0/0/0/0 | W1991959674 | 42 / 126 | 37 / 125 | **bearbeitet (b)** |
| 12 | `yang2024promptbased` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4403320529 | 68 / 50 | 59 / 51 | **bearbeitet (b)** |
| 13 | `kruiper2024platformbased` | (b) FF2/FF4 | 0/2/0/1/0/0 | W4400150442 | 86 / 34 | 70 / 34 | **bearbeitet (b)** |
| 14 | `hagedorn2025ontobpr` | (b) FF2/FF4 | 0/2/0/2/0/0 | W4410251223 | 92 / 20 | 65 / G3 | **bearbeitet (b)** |
| 15 | `mowbray2023representing` | (b) FF2/FF4 | 0/2/0/1/0/0 | W4321770013 | 0 / 12 | 0 / G3 | **bearbeitet (b)** |
| 16 | `hjelseth2015public` | (b) FF2/FF4 | 0/2/0/1/0/0 | W2239149652 | 6 / 22 | 6 / G3 | **bearbeitet (b)** |
| 17 | `gelle2003solving` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2141123969 | 52 / 64 | 43 / 64 | **bearbeitet (b)** |
| 18 | `zech2024bimreason` | (b) FF2/FF4 | 0/2/0/0/0/0 | W4405199717 | 21 / 7 | G4 / G5 | **bearbeitet (b)** |
| 19 | `recski2024briseplandok` | (b) FF2/FF4 | 0/2/2/0/0/0 | W4400383903 | 48 / 4 | G4 / G5 | **bearbeitet (b)** |
| 20 | `lottaz1998constraint` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2170990972 | 27 / 19 | 25 / 19 | **bearbeitet (b)** |
| 21 | `lee2006specifying` | (b) FF2/FF4 | 2/2/0/0/0/0 | W2104143012 | 51 / 398 | 41 / 398 | **bearbeitet (b)** |
| 22 | `zimmermann2013computing` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2135611412 | 23 / 89 | 23 / 89 | **bearbeitet (b)** |
| 23 | `lee2019efficient` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2917212430 | 36 / 50 | 32 / 50 | **bearbeitet (b)** |
| 24 | `esser2022graphbased` | (b) FF2/FF4 | 2/0/0/2/0/0 | W4283270306 | 56 / 30 | 41 / 30 | **bearbeitet (b)** |
| 25 | `urban2025augmented` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4416404543 | 22 / 5 | 22 / 5 | **bearbeitet (b)** |
| 26 | `solimanjunior2022designers` | (b) FF2/FF4 | 0/2/0/0/1/0 | W4206152562 | 74 / 10 | 72 / G6 | **bearbeitet (b)** |
| 27 | `fauth2023process` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4389511728 | 48 / 12 | 45 / G6 | **bearbeitet (b)** |
| 28 | `sei2025understanding` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4410396153 | 35 / 10 | 35 / G6 | **bearbeitet (b)** |
| 29 | `liu2025coordination` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4415736509 | 39 / 5 | 39 / G6 | **bearbeitet (b)** |
| 30 | `akbas2025holistic` | (b) FF2/FF4 | 2/2/0/0/0/2 | W4410568467 | 23 / 3 | G7 / G8 | **bearbeitet (b)** |
| 31 | `fauth2025baugenehmigungsv` | (b) FF2/FF4 | 0/0/0/2/2/0 | W4410774337 | 17 / 3 | G9 / G8 | **bearbeitet (b)** |
| 32 | `fauth2024pace` | (b) FF2/FF4 | 0/0/0/2/0/0 | W4397000832 | 28 / 3 | G9 / G8 | **bearbeitet (b)** |
| 33 | `weinkauf2024decision` | (b) FF2/FF4 | 0/2/0/2/0/0 | W4405481878 | 23 / 1 | G7 / G8 | **bearbeitet (b)** |
| 34 | `feng2026bridging` | (b) FF2/FF4 | 0/0/2/0/0/2 | W7127341327 | 31 / 0 | G10 / G8 | **bearbeitet (b)** |
| 35 | `yang2026llmpowered` | (b) FF2/FF4 | 0/2/2/0/0/0 | W7162694042 | 5 / 0 | G10 / G8 | **bearbeitet (b)** |
| 36 | `hartmann2026status` | (b) FF2/FF4 | 1/0/0/2/0/0 | W7164846815 | 11 / 0 | G9 / G8 | **bearbeitet (b)** |
| 37 | `fauth2023requirements` | (b) FF2/FF4 | 1/0/0/2/0/0 | W4383682229 | 12 / 4 | G9 / G8 | **bearbeitet (b)** |
| 38 | `vanberlo2019creating` | (b) FF2/FF4 | 0/2/0/0/0/0 | W2982547348 | 0 / 6 | 0 / G8 | **bearbeitet (b)** |
| 39 | `wang2022transfer` | (b) FF3 | 0/0/2/0/0/0 | W4281756024 | 58 / 41 | 43 / 40 | **bearbeitet (b)** |
| 40 | `yin2023twostage` | (b) FF3 | 0/0/2/0/0/0 | W4367838951 | 84 / 30 | 48 / 29 | **bearbeitet (b)** |
| 41 | `guo2025advancing` | (b) FF3 | 0/0/2/0/0/0 | W4412072183 | 33 / 27 | 29 / 26 | **bearbeitet (b)** |
| 42 | `gao2025lifecycle` | (b) FF3 | 0/2/0/0/0/0 | W4409096846 | 94 / 18 | 79 / 18 | **bearbeitet (b)** |
| 43 | `bagasi2025bim` | (b) FF3 | 0/0/2/0/1/0 | W4411158086 | 35 / 17 | 31 / G11 | **bearbeitet (b)** |
| 44 | `dong2025bim` | (b) FF3 | 0/0/2/0/0/0 | W4414568512 | 54 / 17 | 54 / G11 | **bearbeitet (b)** |
| 45 | `jin2026evaluating` | (b) FF3 | 0/0/2/0/0/0 | W7135017563 | 45 / 4 | 45 / G12 | **bearbeitet (b)** |
| 46 | `mcdermott1982rulebased` | (b) FF3 | 0/2/0/0/0/0 | W2005004006 | 15 / 957 (Filter nötig) | G13 / 299 (Filter) | **bearbeitet (b)** |
| 47 | `wang2018mapping` | (b) FF3 | 0/0/2/0/0/0 | W2799557147 | 16 / 78 | G13 / 78 | **bearbeitet (b)** |
| 48 | `xie2005modelling` | (b) FF3 | 0/2/0/0/0/0 | W2154241265 | 9 / 81 | G13 / 81 | **bearbeitet (b)** |
| 49 | `rasmussen2020guidelines` | (b) FF3 | 0/2/0/0/0/0 | W3029987277 | 43 / 9 | G14 / G12 | **bearbeitet (b)** |
| 50 | `dudek2023mass` | (b) FF3 | 0/1/2/0/1/0 | W4362453679 | 30 / 0 | G14 / 0 | **bearbeitet (b)** |
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
| 50 Startquellen (b) | – | – | – | – | – | – | nachgeholt, siehe Abschnitt 9 |

## 4 PRISMA-Zahlen und Sättigung: Vergleich R1 / R2 / R3

Zählweise wie in Runde 2: „gesichtet“ = abgerufene OpenAlex-Datensätze; „Kandidaten“ = nach Titel-Screening zur Abstract-Prüfung vorgemerkt, einschließlich Bestandsdubletten. Teil (a) zählt Kandidaten je Startquelle, Teil (b) eindeutig (eine Quelle, die mehrere Startquellen erreicht, zählt einmal). Teil (c) ist die Anschlussprüfung nach der Abbruchregel und gehört nicht zu Runde 3 im engeren Sinn.

| Kennzahl | Runde 1 (gesamt) | Runde 2 | R3 Teil (a) | R3 Teil (b) | **Runde 3 gesamt** | Teil (c) |
|---|---|---|---|---|---|---|
| Startquellen | 61 (56 verschieden) | 47 | 3 | 50 | **53** | 1 (`cao2022ontologybased`) |
| Datensätze gesichtet (roh) | 6 437 | 4 911 | 193 | 3 448 (r 1 534, v 1 914) | **3 641** (r 1 648, v 1 993) | 108 (r 64, v 44) |
| Kandidaten zur Abstract-Prüfung | 468 | 411 | 49 | 496 | **545** | 26 |
| davon Bestandsdubletten | 16,3 % (Teil B) | 17,5 % (72) | 40,8 % (20) | 33,7 % (167) | **34,3 %** (187) | 38,5 % (10) |
| davon in früherer Runde ausgeschlossen | – | – | 2 | 52 | **54** | 2 |
| neue Kandidaten | 423 | 339 | 27 | 277 | **304** | 14 |
| ausgeschlossen | 137 | 177 | 17 | 261 | **278** | 14 |
| – Relevanz < 2 | 109 | 102 | 10 | 207 | 217 | 13 |
| – redundant | 10 | 49 | 5 | 32 | 37 | 1 |
| – Vorfassung/Tagungsfassung/Preprint | 5 | 10 | 2 | 13 | 15 | 0 |
| – nicht verifizierbar/nicht verifiziert | 4 | 9 | 0 (3 nachgetragen) | 9 | 9 | 0 |
| **aufgenommen** | 286 | 162 | 10 (7 + 3 Nachträge) | 16 | **26** | **0** |
| davon Relevanz 3 | 29 (10,1 %) | 3 (1,9 %) | 1 | 0 | **1 (3,8 %)** | 0 |
| **Rohquote aufgenommen / gesichtet** | **4,4 %** | **3,3 %** | 5,2 % | **0,46 %** | **0,71 %** | **0 %** |
| Trefferquote aufgenommen / neue Kandidaten | 67,6 % | 47,8 % | 37,0 % | 5,8 % | **8,6 %** | 0 % |
| Anteil redundant + Vorfassung unter neuen Kandidaten | 3,5 % | 17,4 % | 25,9 % | 16,2 % | **17,1 %** | 7 % |
| Wiederholungen insgesamt unter Kandidaten (Bestand + früher ausgeschlossen + redundant + Vorfassung) | – | 32 % (131 von 411) | 59 % (29 von 49) | 53 % (264 von 496) | **54 %** (293 von 545) | 50 % (13 von 26) |

**Cluster in Teil (b)** (Rohquote Runde 2 nach Recherche 26, Abschnitt 6):

| Cluster | Startquellen | gesichtet | Kandidaten (Bestand / früher ausgeschl. / neu) | aufgenommen | Rohquote R3 (b) | Rohquote R2 |
|---|---|---|---|---|---|---|
| Sprache/Konfiguration (FF3) | 12 | 1 049 (r 432, v 617) | 130 (43 / 17 / 70) | 9 | **0,86 %** | 9,6 % |
| Regelprüfung/Bauantrag (FF2/FF4) | 38 | 2 399 (r 1 102, v 1 297) | 366 (124 / 35 / 207) | 7 | **0,29 %** | 6,6 % |

**Zur Vergleichbarkeit:**

- **Teil (a) gegen Teil (b):** Teil (a) enthält die drei ertragreichsten Startquellen von Runde 2, Teil (b) den Rest. Die hohe Quote von (a) (5,2 % mit den drei Nachträgen, vorher 3,6 %) beruht auf 193 Datensätzen und hebt die Gesamtquote kaum an.
- **Nachträge zu (a):** Die drei in (a) als „nicht verifizierbar“ ausgeschlossenen Kandidaten sind jetzt über Crossref bestätigt und aufgenommen (Abschnitt 8). Die Spalten (a) und „gesamt“ enthalten sie. Abschnitt 3 und Anhang A zeigen den Stand vor dem Nachtrag.
- **Zählweise:** Die eindeutige Zählung in (b) senkt die Zahl der Kandidaten gegenüber der Zählung je Startquelle leicht (17 Mehrfachtreffer). Die Quoten ändern sich dadurch um weniger als 0,1 Prozentpunkte.
- **Robuste Signale:**
  - Die Rohquote fällt von 4,4 % über 3,3 % auf 0,71 %. Sie liegt damit bei rund einem Sechstel von Runde 1.
  - Die Trefferquote je neuem Kandidaten fällt von 67,6 % über 47,8 % auf 8,6 %.
  - Ein Drittel der Kandidaten sind Bestandsdubletten. Mehr als die Hälfte sind Wiederholungen.
  - Relevanz 3 fällt von 29 über 3 auf 1.
- **Warum die Quote in (b) so niedrig ist:**
  - Die Zitationsnetze der FF2/FF4-Startquellen sind weitgehend dieselben. Dieselben Kerntexte zur Regelprüfung und zur digitalen Baugenehmigung erscheinen bei fast jeder Startquelle (etwa `eastman2009automatic`, `noardo2022ifc`, `fauth2022conceptual`, `bloch2023unbalanced`).
  - Was neu ist, liegt meist außerhalb der Fragestellung: NLP-Regelextraktion für fremde Normen, E-Permit-Fallstudien außerhalb Deutschlands, allgemeine Konfigurations- und CSP-Methodik, reine BIM-Abfragen ohne Modelländerung.

**Sättigungsurteil nach der Abbruchregel aus Recherche 26** (Abschnitt 6 Nr. 3):

Sättigung ist erreicht, wenn keine neue Quelle mit Relevanz 3 hinzukommt und die Rohquote unter 2 % liegt, also unter der Hälfte von Runde 1. Kommt erneut Relevanz 3 hinzu, wird nur von diesen Quellen aus weitergesucht.

| Prüfschritt | Relevanz-3-Funde | Rohquote | Bedingungen erfüllt |
|---|---|---|---|
| Runde 3, Teil (a) | 1 (`cao2022ontologybased`) | 5,2 % | nein, nein |
| Runde 3, Teil (b) | 0 | 0,46 % | **ja, ja** |
| Runde 3 gesamt | 1 | 0,71 % | nein (Relevanz 3), ja (Quote) |
| Anschlussprüfung (c) ab `cao2022ontologybased` | 0 | 0 % | **ja, ja** |

- **Urteil: Die Suche ist gesättigt. Das Schneeballverfahren ist mit Runde 3 und der Anschlussprüfung (c) abgeschlossen.**
  - Beide Cluster, für die Recherche 26 eine weitere Runde empfohlen hatte, liegen jetzt weit unter 2 %: FF3 bei 0,86 %, FF2/FF4 bei 0,29 %.
  - Der einzige Relevanz-3-Fund der Runde wurde regelgemäß weiterverfolgt. Seine Netze sind zu 50 % Wiederholung und liefern keine Aufnahme.
  - Die Alberta-/ETH-Linie der Fertigbarkeitsprüfung (`an2020bimbased`, `cao2022ontologybased`) ist damit ausgeschöpft.
- **Eine vierte Runde ist nicht nötig.** Die Abbruchregel gibt keine weiteren Startquellen vor.
- **Ursprungskriterium:** Das strengere Kriterium aus 2a.3 Nr. 3 („keine neue Quelle mit Relevanz ≥ 2“) wird nicht erreicht, Teil (b) liefert noch 16 Relevanz-2-Funde. Recherche 26 hat deshalb für Runde 3 die Abbruchregel festgelegt. Die Relevanz-2-Funde bestätigen und verfeinern vorhandene Argumente, eine neue Argumentlinie eröffnen sie nicht.
- **Vorbehalt FF4:** Juristische Quellen stehen nicht im Zitationsnetz. Dazu gehören Kommentare zur BayBO, die Haftung des Entwurfsverfassers und die Rolle der Prüfsachverständigen. Diese Lücke bleibt eine Aufgabe der gezielten Rechtsrecherche (`lit-K-ff4-jur.bib`) und ist kein Mangel der Sättigung.

## 5 Aufgenommene Quellen Teil (a) (7)

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

1. **Einpflegen:** Die 26 Einträge aus `lit-L` gehören in `quellen-master.csv` (Lauf von `bibmerge.py`) und mit `qualitaet`, `uebertragbarkeit` und P in `quellen-bewertung.csv`. Beides ist in dieser Runde nicht geschehen.
   - `bibmerge.py` schreibt die Masterliste aus allen `lit-*.bib` neu. Ein Probelauf änderte außer den neuen Zeilen auch Q1060–Q1067, weil `lit-M-nachweis.bib` inzwischen von der Masterliste abweicht. Er wurde deshalb zurückgenommen.
2. **Korrekturen an Teil (a) aus dem Crossref-Abgleich** (Abschnitt 8) übernehmen. Die Einträge sind in dieser Runde bewusst unverändert geblieben.
3. **Volltextprüfung** der vier nur nach Titel eingestuften Aufnahmen: `yang2026natural`, `sanchez2022feature`, `lee2026conversational`, `huang2026bimintegrated`. Dazu kommen die zwei Nachprüfhinweise in Anhang B: „Automatisierungspotenziale in der Verwaltung“ und „Information management in industrial housing design and manufacture“.
4. **Zweitbewertung für κ** (2a.7) bevorzugt an diesen Quellen:
   - `cao2022ontologybased` (Relevanz 3)
   - die FF4-Funde `fauth2024investigating`, `vanderheijden2010peanuts`, `meacham2022fire`, `schleich2018kosteneinsparpotenziale`
   - die Konfigurationsfunde `felfernig2011personalized`, `vanhertum2016kb`. Hier ist die Grenze zwischen „stützt ein Argument“ und „redundant zu `felfernig2014knowledge`“ eng.
5. **Kein weiteres Schneeballverfahren** (Abschnitt 4). FF4 wird über die Rechtsrecherche weitergeführt (`lit-K-ff4-jur.bib`).
6. **PRISMA-Flussdiagramm** nach 2a.6 Schritt 5 mit den Zahlen aus Abschnitt 4 erstellen: Runden 1 bis 3 und Teil (c).
7. **Protokoll 2a.3 Nr. 3** nennt noch das strenge Ursprungskriterium. Es sollte an die tatsächlich angewandte Abbruchregel angeglichen werden. Die Entscheidung liegt beim Autor, `02a-review-protokoll.md` ist hier nicht geändert.

## 7 Grenzen

- **Verifikation Teil (a):** Die Einträge aus (a) wurden zunächst über die Websuche statt über Crossref geprüft (Abschnitt 2). Der Crossref-Abgleich in Abschnitt 8 bestätigt alle sieben. Die Kurzfassungen aus (a) stammen weiter aus Suchtreffern.
- **Abstracts in Teil (b):** Titel-Screening, Abstract-Prüfung für die 56 Kandidaten der Kurzliste über OpenAlex, in fünf Fällen ergänzt über Verlags- oder Repositoriumsseiten. Die übrigen neuen Kandidaten sind nach Titel, Venue und Startquelle ausgeschlossen, meist als Relevanz < 2, Gründe in Anhang B.
- **Titelbasierte Aufnahmen:** Vier Aufnahmen beruhen nur auf Titel, Venue und gegebenenfalls Referenzliste, weil kein Abstract zugänglich war (Abschnitt 6 Nr. 3).
- **Sammelabfragen:** Kleine Startquellen wurden in Teil (b) teils gemeinsam abgefragt (G1–G14, Abschnitt 8). Die Zuordnung der Kandidaten zu einer Startquelle ist dort nach Thema erfolgt. Für die Aufnahmen aus Sammelabfragen ist sie über `referenced_works` bestätigt (`nowak2023identifying`, `zarghami2024explainable`, `abdelazizshawky2026product`).
- **Filter:** Bei `mcdermott1982rulebased` wurden vorwärts nur die 299 von 957 Zitierenden gesichtet, die der Volltextfilter liefert (Regel aus Runde 2).
- **Unvollständige Referenzlisten** in OpenAlex: Die Zahl der aufgelösten Referenzen liegt teils unter `referenced_works_count`, etwa `ilal2022integrating` 75 von 79 und `lee2006specifying` 41 von 51. Bei `krischmann2020entwicklung`, `mowbray2023representing` und `vanberlo2019creating` fehlen Referenzen ganz.
- **Einzelbewertung:** Relevanz, „redundant“ und „nicht verifiziert“ wurden von einem einzelnen Bewerter eingestuft (2a.7).

## 8 Teil (b): Suchweg, Sammelabfragen, Crossref-Abgleich

- **Zugang:** Das Exa-Kontingent war wieder verfügbar. Alle Abfragen liefen über `mcp__Exa__web_fetch_exa`, Direktzugriffe blieben gesperrt.
  - **Kanten:** OpenAlex, rückwärts `works?filter=cited_by:<W-ID>`, vorwärts `works?filter=cites:<W-ID>`, `per_page=200`, bei `lee2006specifying` und `mcdermott1982rulebased` zwei Seiten.
  - **Abstracts:** OpenAlex `abstract_inverted_index` in zwei Sammelabfragen über den DOI-Filter.
  - **Verifikation:** Crossref `api.crossref.org/works?filter=doi:…`.
  - **Aufwand:** 69 OpenAlex-Anfragen in 15 Exa-Abrufen für die 50 Startquellen, also rund 1,4 Anfragen je Startquelle. Dazu kamen 7 Abrufe für Abstracts, Verifikation, Zuordnung und Teil (c) sowie 5 gezielte Websuchen.
- **Sammelabfragen:** Kleine Startquellen wurden gemeinsam abgefragt (ODER-Filter). Die Kandidaten sind der thematisch passenden Startquelle zugeordnet.

| Gruppe | Richtung | Startquellen | Datensätze |
|---|---|---|---|
| G1 | r | `meijer2006deregulation`, `ciotta2021structural`, `messaoudi2020virtual` | 21 |
| G2 | v | `ciotta2021structural`, `krischmann2020entwicklung`, `messaoudi2020virtual` | 31 |
| G3 | v | `hagedorn2025ontobpr`, `mowbray2023representing`, `hjelseth2015public` | 53 |
| G4 | r | `zech2024bimreason`, `recski2024briseplandok` | 61 |
| G5 | v | `zech2024bimreason`, `recski2024briseplandok` | 10 |
| G6 | v | `solimanjunior2022designers`, `fauth2023process`, `sei2025understanding`, `liu2025coordination` | 33 |
| G7 | r | `akbas2025holistic`, `weinkauf2024decision` | 46 |
| G8 | v | `vanberlo2019creating`, `akbas2025holistic`, `fauth2025baugenehmigungsv`, `fauth2024pace`, `weinkauf2024decision`, `fauth2023requirements`, `feng2026bridging`, `yang2026llmpowered`, `hartmann2026status` | 19 |
| G9 | r | `fauth2025baugenehmigungsv`, `fauth2024pace`, `hartmann2026status`, `fauth2023requirements` | 55 |
| G10 | r | `feng2026bridging`, `yang2026llmpowered` | 35 |
| G11 | v | `bagasi2025bim`, `dong2025bim` | 33 |
| G12 | v | `rasmussen2020guidelines`, `jin2026evaluating` | 13 |
| G13 | r | `mcdermott1982rulebased`, `wang2018mapping`, `xie2005modelling` | 32 |
| G14 | r | `rasmussen2020guidelines`, `dudek2023mass` | 71 |

- **Dubletten:** DOI exakt, Titel normalisiert auf 60 Zeichen, Präfixabgleich auf 40 Zeichen. Geprüft gegen:
  - `quellen-master.csv` (1 067 Zeilen)
  - alle `lit-*.bib`, einschließlich der Einträge aus Teil (a)
  - die ausgeschlossenen Kandidaten aus Recherche 25 (Anhang G), 26 (Anhang A) und 28 (Anhang A)
- **Keys:** keine Kollision mit `lit-A` … `lit-M` und `quellen-master.csv`. `bibmerge.py` meldet nur die bekannten Altfälle (`du2026text2bim`, `mbo2bim2023`).
- **Crossref-Abgleich der sieben Einträge aus Teil (a):** Alle sieben sind bestätigt. Abweichungen gegenüber `lit-L` sind unten aufgeführt. Sie sind **nicht eingearbeitet**, weil bestehende Einträge unverändert bleiben sollten (Abschnitt 6 Nr. 2).
  - `kim2022bim`: volle Vornamen Yije Kim, Sangyoon Chin, Seungyeon Choo. Band 140 ist bestätigt.
  - `wang2016building`: volle Vornamen Jun Wang, Xiangyu Wang, Wenchi Shou, Heap-Yih Chong, Jun Guo.
  - `cortezlara2026bimsimulated`: Band 16, Heft 1, Artikel 11345.
  - `weld2022survey`: Crossref nennt die Seiten 1–38 und den 23.12.2022. Die Artikelnummer 156 steht nur beim Verlag.
  - `fisher2024paad`: Heft 6 ist bestätigt.
  - `cao2022ontologybased` und `saka2023conversational`: ohne Abweichung.
- **Nachträge zu Teil (a):** Die drei in (a) als „nicht verifizierbar, nachprüfen“ geführten Kandidaten sind über Crossref bestätigt und aufgenommen:
  - `lee2026conversational` (FF3 = 2, nach Titel)
  - `fattahitabasi2026human` (FF5 = 2, Abstract gelesen)
  - `huang2026bimintegrated` (FF6 = 2, nach Titel)

## 9 Teil (b): Protokoll je Startquelle

Zählweise wie in Abschnitt 3, Kandidaten jedoch eindeutig: Eine Quelle zählt bei der ersten Startquelle, die sie erreicht. „gesichtet r / v“ nach Abschnitt 1, Gruppen nach Abschnitt 8.

| Start | gesichtet r / v | Kandidaten r / v | davon Bestand r / v | davon früher ausgeschl. r / v | aufgenommen r / v | Anmerkung |
|---|---|---|---|---|---|---|
| `ghannad2019automated` | 29 / 77 | 15 / 19 | 10 / 8 | 2 / 2 | 0 / 0 |  |
| `olsson2018automation` | 42 / 72 | 7 / 25 | 4 / 15 | 0 / 3 | 0 / 1 | Vorwärts fast nur GeoBIM/E-Permit; 15 von 25 Vorwärts-Kandidaten Bestand; neu `xiao2026trusting`. |
| `fauth2022conceptual` | 22 / 36 | 11 / 12 | 3 / 6 | 2 / 2 | 1 / 1 | Neu `schleich2018kosteneinsparpotenziale` (r), `fauth2024investigating` (v). |
| `fischer2023automation` | 42 / 24 | 10 / 5 | 4 / 2 | 1 / 0 | 0 / 0 |  |
| `ilal2022integrating` | 75 / 12 | 9 / 2 | 3 / 1 | 1 / 1 | 0 / 0 |  |
| `meijer2006deregulation` | G1 / 42 | 2 / 10 | 0 / 1 | 0 / 0 | 0 / 1 | Vorwärts Linie private Bauaufsicht (van der Heijden); neu `vanderheijden2010peanuts`. |
| `ciotta2021structural` | G1 / G2 | 2 / 3 | 0 / 2 | 2 / 0 | 0 / 0 |  |
| `krischmann2020entwicklung` | 0 / G2 | 0 / 3 | 0 / 1 | 0 / 0 | 0 / 0 | keine Referenzen in OpenAlex |
| `messaoudi2020virtual` | G1 / G2 | 3 / 1 | 1 / 0 | 0 / 0 | 0 / 0 |  |
| `meijer2017quality` | 19 / 23 | 7 / 5 | 1 / 1 | 0 / 0 | 0 / 1 | Neu `meacham2022fire` (Vorfertigung und Bauaufsicht). |
| `daum2014processing` | 37 / 125 | 5 / 17 | 2 / 7 | 0 / 3 | 0 / 0 | NL-/Abfrageliteratur fast vollständig Bestand oder reine Abfrage. |
| `yang2024promptbased` | 59 / 51 | 10 / 19 | 1 / 9 | 1 / 2 | 0 / 0 | Rückwärts El-Gohary-Linie (Regelextraktion) nicht im Bestand, Relevanz < 2. |
| `kruiper2024platformbased` | 70 / 34 | 7 / 4 | 3 / 0 | 3 / 1 | 0 / 0 |  |
| `hagedorn2025ontobpr` | 65 / G3 | 12 / 6 | 8 / 4 | 2 / 1 | 0 / 0 |  |
| `mowbray2023representing` | 0 / G3 | 0 / 0 | 0 / 0 | 0 / 0 | 0 / 0 | keine Referenzen in OpenAlex; vorwärts (G3) ohne Kandidaten |
| `hjelseth2015public` | 6 / G3 | 3 / 2 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `gelle2003solving` | 43 / 64 | 3 / 12 | 0 / 1 | 0 / 0 | 0 / 0 | Vorwärts allgemeine CSP-/Konfiguratormethodik ohne Baubezug. |
| `zech2024bimreason` | G4 / G5 | 3 / 1 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `recski2024briseplandok` | G4 / G5 | 3 / 1 | 0 / 1 | 0 / 0 | 0 / 0 |  |
| `lottaz1998constraint` | 25 / 19 | 3 / 5 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `lee2006specifying` | 41 / 398 | 6 / 17 | 1 / 7 | 0 / 0 | 0 / 0 | 398 Zitierende, fast nur allgemeine BIM-Literatur. |
| `zimmermann2013computing` | 23 / 89 | 0 / 2 | 0 / 0 | 0 / 0 | 0 / 0 | Vorwärts Lösungsraummethode im Fahrzeug- und Maschinenbau. |
| `lee2019efficient` | 32 / 50 | 3 / 5 | 0 / 1 | 0 / 0 | 0 / 0 |  |
| `esser2022graphbased` | 41 / 30 | 5 / 5 | 3 / 0 | 0 / 0 | 0 / 0 |  |
| `urban2025augmented` | 22 / 5 | 0 / 1 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `solimanjunior2022designers` | 72 / G6 | 9 / 6 | 2 / 2 | 3 / 0 | 0 / 1 | Neu `nowak2023identifying` (v). |
| `fauth2023process` | 45 / G6 | 6 / 2 | 0 / 0 | 2 / 1 | 0 / 0 |  |
| `sei2025understanding` | 35 / G6 | 4 / 3 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `liu2025coordination` | 39 / G6 | 2 / 0 | 1 / 0 | 0 / 0 | 0 / 0 |  |
| `akbas2025holistic` | G7 / G8 | 4 / 2 | 1 / 2 | 0 / 0 | 0 / 0 |  |
| `fauth2025baugenehmigungsv` | G9 / G8 | 2 / 1 | 0 / 1 | 0 / 0 | 0 / 0 |  |
| `fauth2024pace` | G9 / G8 | 2 / 0 | 1 / 0 | 0 / 0 | 0 / 0 |  |
| `weinkauf2024decision` | G7 / G8 | 2 / 0 | 1 / 0 | 0 / 0 | 0 / 0 |  |
| `feng2026bridging` | G10 / G8 | 4 / 0 | 1 / 0 | 0 / 0 | 1 / 0 | Neu `zarghami2024explainable` (r). |
| `yang2026llmpowered` | G10 / G8 | 3 / 0 | 1 / 0 | 0 / 0 | 0 / 0 |  |
| `hartmann2026status` | G9 / G8 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `fauth2023requirements` | G9 / G8 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `vanberlo2019creating` | 0 / G8 | 0 / 1 | 0 / 0 | 0 / 0 | 0 / 0 | keine Referenzen in OpenAlex |
| `wang2022transfer` | 43 / 40 | 2 / 12 | 0 / 4 | 0 / 1 | 0 / 0 |  |
| `yin2023twostage` | 48 / 29 | 5 / 3 | 3 / 0 | 0 / 2 | 0 / 1 | Neu `jang2026understanding` (v). |
| `guo2025advancing` | 29 / 26 | 6 / 7 | 2 / 2 | 3 / 1 | 0 / 2 | Neu `alwashah2026reliable`, `gao2026multiagent` (v). |
| `gao2025lifecycle` | 79 / 18 | 17 / 1 | 11 / 0 | 1 / 0 | 2 / 1 | 11 von 17 Rückwärts-Kandidaten Bestand; neu `ostrowskawawryniuk2020prefabrication`, `sanchez2022feature` (r), `yang2026natural` (v). |
| `bagasi2025bim` | 31 / G11 | 3 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `dong2025bim` | 54 / G11 | 3 / 7 | 1 / 0 | 0 / 1 | 0 / 0 |  |
| `jin2026evaluating` | 45 / G12 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| `mcdermott1982rulebased` | G13 / 299 (Filter) | 1 / 24 | 0 / 5 | 0 / 4 | 0 / 2 | Volltextfilter: 299 von 957; neu `felfernig2011personalized`, `vanhertum2016kb`. |
| `wang2018mapping` | G13 / 78 | 0 / 4 | 0 / 2 | 0 / 1 | 0 / 0 | Vorwärts Kundenbedarfsanalyse im Maschinenbau. |
| `xie2005modelling` | G13 / 81 | 6 / 14 | 2 / 5 | 0 / 2 | 0 / 1 | Neu `abdelazizshawky2026product` (v, auch über `rasmussen2020guidelines`). |
| `rasmussen2020guidelines` | G14 / G12 | 12 / 1 | 6 / 0 | 1 / 0 | 0 / 0 |  |
| `dudek2023mass` | G14 / 0 | 1 / 0 | 0 / 0 | 0 / 0 | 0 / 0 |  |
| **Summe (b)** | **1 534 / 1 914** | **226 / 270** | **77 / 90** | **24 / 28** | **4 / 12** | 3 448 Datensätze, 496 Kandidaten (eindeutig), 16 Aufnahmen |

**Befund:**
- **FF2/FF4:**
  - In den 38 Startquellen des Bauantrags- und Regelprüfungsclusters sind 124 von 366 Kandidaten Bestand, 35 schon früher ausgeschlossen.
  - Die sieben Aufnahmen kommen fast alle aus Randlinien: private Bauaufsicht, Vorfertigung und Aufsicht, Ökonomie der Landesbauordnung, Rückmeldung und Vertrauen.
  - Aus dem Kern der Regelprüfung (ACC, NLP-Regelextraktion, Ontologien) kommt kein neuer Fund über Relevanz 1.
- **FF3:**
  - Die Sprachlinie ist rückwärts gesättigt. `wang2022transfer`, `yin2023twostage` und `guo2025advancing` führen fast nur zu Bestand oder zu reinen Abfragesystemen.
  - Neu sind vorwärts drei Arbeiten von 2026 zur Zuverlässigkeit und Steuerung LLM-gestützter Modelländerung.
- **Konfiguration:**
  - Die Startquellen `mcdermott1982rulebased`, `xie2005modelling`, `rasmussen2020guidelines` und `gelle2003solving` erreichen fast nur allgemeine Konfigurations- und CSP-Methodik. Diese ist im Bestand durch `felfernig2014knowledge`, `sabin1998product` und `soininen1998general` getragen.
  - Aufgenommen sind nur drei Arbeiten mit eigenem Baustein: Diagnose, Wissensbasis-Paradigma und eine aktuelle Übersicht.

## 10 Aufgenommene Quellen Teil (b) (16) und Nachträge zu Teil (a) (3)

Einteilung und Kennzeichnung wie in Abschnitt 5. Relevanz vorläufig. † = nur nach Titel, Venue und Referenzliste eingestuft (kein Abstract zugänglich).

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `fauth2024investigating` | 2025 | Investigating building permit processes across Europe: characteristics and patterns | Building Research & Information 53(4) | fauth2022conceptual (vorwärts) | 0/0/0/2/0/0 | Vergleich der Genehmigungsverfahren in 17 europäischen Ländern (Interviews); ordnet das deutsche Verfahren ein (FF4) |
| `vanderheijden2010peanuts` | 2010 | On Peanuts and Monkeys: Private Sector Involvement in Australian Building Control | Urban Policy and Research 28(2) | meijer2006deregulation (vorwärts) | 0/0/0/2/0/0 | 56 Interviews zu beabsichtigten und unbeabsichtigten Folgen privater Bauaufsicht; stützt die Abwägung, wie viel Prüfverantwortung beim Entwurfsverfasser liegen kann (FF4) |
| `meacham2022fire` | 2022 | Fire performance and regulatory considerations with modern methods of construction | Buildings and Cities 3(1) | meijer2017quality (vorwärts) | 0/1/0/2/0/0 | Vorfertigung passt schlecht zu Aufsicht, die auf Kontrollen an der Baustelle beruht; Nachweise für Werksfertigung nötig (FF4, Fertighaus) |
| `schleich2018kosteneinsparpotenziale` | 2018 | Kosteneinsparpotenziale einer effizienteren Landesbauordnung | Springer Vieweg (Dissertation) | fauth2022conceptual (rückwärts) | 0/0/0/2/0/0 | ökonomische Analyse der BauO NRW gegenüber England, Transaktionskosten der Verfahrensvorschriften, drei Wohnbau-Fallstudien (FF4, deutsche Landesbauordnung) |
| `nowak2023identifying` | 2023 | Identifying Visualization Opportunities to Help Architects Manage the Complexity of Building Codes | IEEE Computer Graphics and Applications 43(6) | solimanjunior2022designers (vorwärts) | 0/1/0/0/2/0 | Studien mit Architekten: Rückmeldung zu Spielräumen und Folgen von Entwurfsentscheidungen unter Bauvorschriften schon im Frühentwurf (FF5) |
| `xiao2026trusting` | 2026 | Trusting the algorithm: transparency, information control and continuance intention in China's digital building permit systems | Building Research & Information | olsson2018automation (vorwärts) | 0/0/0/1/2/0 | 468 Befragte: Transparenz und Fairness des Algorithmus tragen Vertrauen und Weiternutzung digitaler Genehmigungssysteme (FF5) |
| `zarghami2024explainable` | 2024 | Explainable Artificial Intelligence in Generative Design for Construction | EC3 2024, Computing in Construction 5 | feng2026bridging (rückwärts) | 0/0/0/0/2/0 | Übersicht: Erklärbarkeit generativer Entwurfsverfahren im Bauwesen kaum untersucht, Black Box hemmt Einsatz (FF5, Forschungslücke) |
| `jang2026understanding` | 2026 | Understanding User Requirements in LLM-Augmented BIM Systems: A TAM-Based Evaluation of NADIA-S | Computing in Civil Engineering 2025 (ASCE) | yin2023twostage (vorwärts) | 0/0/1/0/2/0 | Expertenbewertung (TAM) eines sprachgesteuerten Systems für Detaillierung und Regelprüfung; ergänzt `jang2024nadia` um Nutzersicht (FF5) |
| `alwashah2026reliable` | 2026 | Reliable LLM-driven BIM automation through capability-based multi-dimensional evaluation | Automation in Construction 187 | guo2025advancing (vorwärts) | 0/0/2/0/1/0 | 31 Revit-Aufgaben, 238 Fehler, 48 % API-Fehlgebrauch, Zuverlässigkeit sinkt mit der Komplexität; stützt eine deterministische Zwischenschicht statt frei generierten Codes (FF3) |
| `gao2026multiagent` | 2026 | Multi-agent framework for schema-guided reasoning and tool-augmented interaction with IFC models | Automation in Construction 186 | guo2025advancing (vorwärts) | 0/0/2/0/0/0 | Abfrage und Änderung von IFC-Modellen in natürlicher Sprache über definierte Werkzeuge, nachvollziehbare Abläufe (FF3) |
| `yang2026natural` † | 2026 | From natural language to manufacturing data: A study of LLM-Mediated workflow for customized residential construction | Journal of Building Engineering 120 | gao2025lifecycle (vorwärts) | 0/1/2/0/0/0 | Titel beschreibt die Kette vom Kundenwunsch in natürlicher Sprache zu Fertigungsdaten im individualisierten Wohnbau (FF3); Volltext prüfen |
| `felfernig2011personalized` | 2011 | Personalized diagnoses for inconsistent user requirements | AI EDAM 25(2) | mcdermott1982rulebased (vorwärts) | 0/2/0/0/1/0 | Diagnose unvereinbarer Nutzeranforderungen im Konfigurator (PersDiag); Baustein für „Wunsch verletzt Herstellerregel, was tun?“, ergänzt `yang2012constraint` (FF2) |
| `vanhertum2016kb` | 2017 | The KB paradigm and its application to interactive configuration | Theory and Practice of Logic Programming 17(1) | mcdermott1982rulebased (vorwärts) | 0/2/0/0/0/0 | eine Wissensbasis, mehrere Inferenzen (Prüfen, Propagieren, Erklären); stützt „Herstellerregeln als Daten“ (FF2, Prinzip 5) |
| `abdelazizshawky2026product` | 2026 | Product configuration for mass customisation: a systematic literature review | International Journal of Production Research 64(18) | xie2005modelling, rasmussen2020guidelines (vorwärts) | 0/2/1/0/0/0 | PRISMA-Übersicht über 122 Arbeiten (2000–2025), einschließlich Umsetzung von Nutzeranforderungen; aktualisiert `zhang2014product` (FF2) |
| `ostrowskawawryniuk2020prefabrication` | 2021 | Prefabrication 4.0: BIM-aided design of sustainable DIY-oriented houses | International Journal of Architectural Computing 19(2) | gao2025lifecycle (rückwärts) | 1/2/0/0/0/0 | Revit/Dynamo-Werkzeug passt Einfamilienhausentwurf an kleinteilige Holzvorfertigung an (FF2) |
| `sanchez2022feature` † | 2022 | Feature modeling for configurable and adaptable modular buildings | Advanced Engineering Informatics 51 | gao2025lifecycle (rückwärts) | 0/2/0/0/0/0 | Merkmalsmodellierung für konfigurierbare Modulgebäude; Volltext prüfen, ob redundant zu `khaliliaraghi2020variability` (FF2) |
| `lee2026conversational` † (Nachtrag a) | 2026 | Conversational programming for structural model review and editing via conversational corrective grounding (CCG) | Automation in Construction 188 | wei2025texttostructure (vorwärts) | 0/0/2/0/0/0 | dialogische Prüfung und Bearbeitung von Modellen mit korrigierender Rückkopplung (FF3); Volltext prüfen |
| `fattahitabasi2026human` (Nachtrag a) | 2026 | Human–AI collaboration in architectural design: Interaction, design process and controllability | Automation in Construction 191 | wei2025texttostructure (vorwärts) | 0/0/1/0/2/0 | Übersicht (96 Arbeiten): Kollaborationsmodi und Informationsfluss bestimmen die menschliche Kontrolle über KI-Ergebnisse (FF5) |
| `huang2026bimintegrated` † (Nachtrag a) | 2026 | BIM-integrated generative wiring design for residential interior lighting circuits: A network flow-based ILP optimization approach | Expert Systems with Applications 331 | zhang2022bimbased (vorwärts) | 0/0/0/0/0/2 | Leitungsführung für Beleuchtungsstromkreise im Wohnbau aus BIM (FF6); Volltext prüfen |

**Schwerpunkt Teil (b), nach Haupt-FF:** FF2 5, FF3 3, FF4 4, FF5 4. Kein FF1-Fund, kein FF6-Fund und keine Relevanz 3. Mit den Nachträgen zu (a) kommen FF3 1, FF5 1 und FF6 1 hinzu.

## 11 Teil (c): Anschlussprüfung ab `cao2022ontologybased`

Die Abbruchregel verlangt, von einem neuen Relevanz-3-Fund aus weiterzusuchen. Deshalb wurde `cao2022ontologybased` (OpenAlex W4225113775, 77 Referenzen, 44 Zitierende) in beide Richtungen verfolgt.

| Richtung | gesichtet | Kandidaten | Bestand | früher ausgeschl. | neu | aufgenommen |
|---|---|---|---|---|---|---|
| rückwärts | 64 | 14 | 7 (`yuan2018design`, `he2021bim`, `liu2016ontology`, `lu2021dfma`, `tan2020construction`, `gbadamosi2020big`, `an2020bimbased`) | 1 (R2) | 6 | 0 |
| vorwärts | 44 | 12 | 3 (`gao2025lifecycle`, `vakaj2023ontology`, `luo2024ontologybased`) | 1 (R3 a) | 8 | 0 |
| **Summe** | **108** | **26** | **10** | **2** | **14** | **0** |

- **Neue Kandidaten, alle ausgeschlossen:**
  - Relevanz < 2 (13): Ontologie für Fertigungsressourcen, Fertigbarkeitsanalyse im Maschinenbau, digitale Fertigung und früher Einbezug des Unternehmers, BIM-Objekte in der Fertigung, Ontologiesuite, Wissensmanagement Vorfertigung (Übersicht), Fassadenpaneele im Hochhaus, Automobilfertigung, Komplexitätsmetrik Modularisierung, Konstruierbarkeit panelisierter Gebäude, LLM mit Semantic Web für Vorfertigungswissen (reine Abfrage), additive Fertigung
  - redundant (1): ontologiebasierte DfX-Kriterien (10.1061/jmenea.meeng-6901) zu `cao2022ontologybased`
- **Befund:** Die Linie Fertigbarkeitsprüfung im Entwurf ist ausgeschöpft. Die Hälfte der Kandidaten sind Wiederholungen, die Rohquote liegt bei 0 %.


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

**Nachtrag (Teil (b)):** Die drei oben als „nicht verifizierbar, nachprüfen“ geführten Kandidaten (10.1016/j.autcon.2026.106989, 10.1016/j.autcon.2026.107155, 10.1016/j.eswa.2026.133364) sind inzwischen über Crossref bestätigt und aufgenommen (Abschnitte 8 und 10).

## Anhang B: Teil (b), Bestandsdubletten, früher ausgeschlossene und nicht aufgenommene Kandidaten

**B.1 Bestandsdubletten (167, eindeutig):**

- **Cluster FF2/FF4 (124):** `amor2021promise`, `ataide2023digital`, `battisti2022automatic`, `beach2015rulebased`, `beach2020towards`, `beach2024digital`, `bloch2023unbalanced`, `borrmann2009topological`, `chateauvieuxhellwig2022timber`, `cheung2026institutionalizing`, `ciotta2021structural`, `comai2026definition`, `demarco2024enriching`, `dimyadi2017evaluating`, `doukari2022object`, `du2026text2bim`, `eastman2009automatic`, `fauth2022conceptual`, `fauth2023ontology`, `fauth2023process`, `fauth2023requirements`, `fauth2023understanding`, `fauth2024pace`, `fauth2024taxonomy`, `fauth2025baugenehmigungsv`, `fischer2023automation`, `fischer2024extending`, `fischer2025bridging`, `fuchs2022neural`, `fuchs2025exploring`, `gade2021exploration`, `gan2022graph`, `gao2025lifecycle`, `ghannad2019automated`, `haeussler2021code`, `hagedorn2023semantic`, `hagedorn2025ontobpr`, `hartmann2026status`, `hellin2025natural`, `hettiarachchi2025codeaccord`, `hjelseth2011capturing`, `hjelseth2015public`, `hosseinigourabpasi2025developing`, `ilal2022integrating`, `iversen2026leveraging`, `jang2024nadia`, `jedrzejewska2026eurocode`, `kim2020kbim`, `kremer2023extending`, `krischmann2020entwicklung`, `kruiper2024platformbased`, `lee2016modularized`, `lee2016translating`, `lee2020comparative`, `lee2026automated`, `li2026functioncalling`, `liu2016ontology`, `liu2018bim`, `liu2022offsite`, `liu2023definition`, `liu2025coordination`, `macitilal2017computer`, `madireddy2025large`, `malsane2015development`, `mazairac2013bimql`, `meda2024twinning`, `meijer2006deregulation`, `meijer2017quality`, `mellenthinfilardo2026requirements`, `messaoudi2020virtual`, `napps2026digitalizing`, `narayanaswamy2019bim`, `nawari2019generalized`, `niemeijer2014freedom`, `noardo2020integrating`, `noardo2020opportunities`, `noardo2022ifc`, `noardo2022unveiling`, `nuyts2024comparative`, `olsson2018automation`, `palmirani2011legalruleml`, `pauwels2011semantic`, `pauwels2017performance`, `pinto2026exhaustive`, `piroozfar2019configuration`, `preidel2015automated`, `preidel2016towards`, `preidel2018bim`, `sacks2004parametric`, `sei2025understanding`, `senousy2026automated`, `shafiee2025enhancing`, `shahi2019automated`, `shi2018ifcdiff`, `shi2025finetuning`, `singh2017integrating`, `sobral2026challenges`, `solihin2015classification`, `solimanjunior2022designers`, `sun2026global`, `thajudeen2022supporting`, `tomczak2022review`, `tonguc2026code`, `urban2024adapting`, `urban2025augmented`, `urban2026development`, `vilgertshofer2017graph`, `wu2019retrieval`, `wu2025design`, `wu2026alterations`, `wu2026revisiting`, `xie2005modelling`, `yin2023ontology`, `yin2023twostage`, `zahedi2022bim`, `zhang2016semantic`, `zhang2017integrating`, `zhang2017logic`, `zhang2023rule`, `zhang2023unpacking`, `zheng2026translating`, `zhou2023platforming`, `zou2022investigating`, `zou2023lessons`
- **Cluster FF3 (43):** `alwisy2019bim`, `bakhshi2021dfma`, `baradaran2022parametric`, `blessing2009drm`, `cao2022ontologybased`, `chen2024automated`, `daum2014processing`, `elghaish2022voice`, `felfernig2014knowledge`, `fernandes2024gptassistant`, `fischer1991critiquing`, `fogliatto2012mass`, `forza2002configuration`, `forza2002managing`, `forza2006product`, `gelle2003solving`, `guo2025advancing`, `haug2019causes`, `he2021bim`, `hvam2008product`, `isaac2016methodology`, `jiang2024epluslm`, `jin2026evaluating`, `liao2021structgan`, `mattern2018bimbased`, `moshari2026material`, `park2026bimllm`, `sabin1998product`, `shin2021bimasr`, `soininen1998general`, `trentin2011overcoming`, `trentin2012product`, `trentin2014increasing`, `wang2021knowledge`, `wang2021needsbased`, `wang2022natural`, `wang2022transfer`, `wei2025texttostructure`, `yang2012constraint`, `yuan2018design`, `zhang2014product`, `zhang2022bimbased`, `zheng2023dynamic`

**B.2 In Runde 1, 2 oder 3 (a) bereits ausgeschlossen (52):** 10.1186/s40327-017-0055-0 (R2), 10.1016/j.aei.2015.05.006 (R2), 10.3390/app15010049 (R2), 10.1061/9780784483961.105 (R2), 10.3390/buildings12010045 (R2), 10.3846/ijspm.2020.13676 (R2), 10.5194/isprs-archives-xliii-b4-2022-529-2022 (R2), 10.1088/1755-1315/323/1/012102 (R2), 10.2749/newyork.2019.1560 (R2), 10.12688/openreseurope.18553.2 (R2), 10.1061/jladah.ladr-1310 (R2), 10.1016/j.autcon.2020.103248 (R2), 10.1061/9780784413616.067 (R2), 10.1080/09613218.2026.2637965 (R2), 10.1061/(asce)ae.1943-5568.0000049 (R2), 10.1061/(asce)ae.1943-5568.0000382 (R2), 10.3233/sw-180297 (R2), 10.1016/j.aei.2025.103375 (R2), 10.7939/r39g5gq7z (R1), 10.1061/(asce)cp.1943-5487.0000427 (R2), 10.1061/jcemd4.coeng-18122 (R2), 10.1016/j.autcon.2026.107038 (R2), 10.1016/j.autcon.2022.104524 (R2), 10.1061/(asce)cp.1943-5487.0000922 (R2), 10.18653/v1/2021.nllp-1.14 (R2), 10.36680/j.itcon.2025.002 (R2), 10.1016/j.jobe.2024.111515 (R2), 10.1088/1755-1315/1101/9/092007 (R2), 10.1016/j.aei.2026.104735 (R2), 10.1016/j.autcon.2009.07.008 (R2), 10.1061/9780784412343.0036 (R2), 10.1061/9780784412367.084 (R2), 10.1016/j.aei.2023.102137 (R2), 10.1007/10929179_70 (R2), 10.1108/sasbe-01-2026-0077 (R2), 10.1016/j.compind.2023.104063 (R2), 10.1016/j.aei.2026.105075 (R2), 10.36680/j.itcon.2026.025 (R2), 10.1111/mice.12151 (R3a), 10.1061/(asce)cp.1943-5487.0001019 (R2), 10.36680/j.itcon.2023.013 (R3a), 10.1016/j.autcon.2026.107260 (R3a), 10.1080/13467581.2024.2329351 (R2), 10.2139/ssrn.7428103 (R2), 10.1145/62065.62067 (R2), 10.1007/978-0-387-34930-5_7 (R2), 10.1016/0166-3615(94)00041-n (R2), 10.1016/j.ijpe.2020.107775 (R1), 10.1109/tase.2020.2986774 (R2), 10.1016/j.jmsy.2025.06.013 (R2), 10.1007/s10845-011-0544-2 (R2), 10.1016/s0954-1810(01)00016-4 (R2)

**B.3 Neue Kandidaten, nicht aufgenommen (261):** Nr. = laufende Nummer der Kandidatenliste Teil (b); Start mit Richtung (r = rückwärts, v = vorwärts).

| Nr. | DOI | Titel (gekürzt) | Start | Grund |
|---|---|---|---|---|
| 1 | 10.13140/2.1.4920.4161 | Automated Building Code Compliance Checking - Where is it at? | ghannad2019automated r | redundant zu `amor2021promise` (Stand der Regelprüfung) |
| 2 | 10.1201/b17396-30 | A visual BIM query language | ghannad2019automated r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 3 | 10.1061/9780784481264.026 | Graphical Scripting Approach Integrated with Speech Recognition for BI | ghannad2019automated r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 4 | 10.36680/j.itcon.2023.001 | Invariant Signature, Logic Reasoning, and Semantic NLP-Based Automated | ghannad2019automated v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 5 | 10.1016/j.asej.2024.103173 | From BIM to computational BIM: A systematic review of visual programmi | ghannad2019automated v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 6 | 10.1061/jmenea.meeng-5344 | Factors Influencing the Acceptance of BIM-Based Automated Code Complia | ghannad2019automated v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 7 | 10.1007/978-3-030-88207-5_9 | Practitioner Experiences and Requirements for Rule Translation Used fo | ghannad2019automated v | redundant zu `gade2021exploration` |
| 8 | 10.1007/978-3-658-33361-4_23 | Prüfung der Einhaltung von Normen und Richtlinien mittels BIM | ghannad2019automated v | redundant: deutschsprachige Fassung zu `preidel2018bim` (Bestand), redundant |
| 9 | 10.1007/978-981-99-7965-3_46 | Information Requirement Analysis for Establishing BIM-Oriented Natural | ghannad2019automated v | Tagungsfassung zu 10.26599/jic.2025.9180084 (selbst Relevanz < 2) |
| 10 | 10.2139/ssrn.5460396 | Open-source compliance check web application for Digital Building Perm | ghannad2019automated v | SSRN-Preprint, nicht begutachtet |
| 11 | 10.1016/j.compind.2023.103945 | Semi-automatic representation of design code based on knowledge graph  | ghannad2019automated v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 12 | 10.1061/jccee5.cpeng-4884 | Facilitating Knowledge Transfer during Code Compliance Checking Using  | ghannad2019automated v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 13 | 10.5194/isprsannals-ii-2-w1-279-2013 | Experiment for integrating Dutch 3D spatial planning and BIM for check | olsson2018automation r | redundant zu `noardo2020opportunities`, `noardo2022ifc` |
| 14 | 10.3390/ijgi5020014 | A Generic Model to Exploit Urban Regulation Knowledge | olsson2018automation r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 15 | 10.1016/j.aei.2015.07.006 | Toward robust and quantifiable automated IFC quality validation | olsson2018automation r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 16 | 10.1016/j.autcon.2021.103743 | Loose coupling of GIS and BIM data models for automated compliance che | olsson2018automation v | redundant zu `ilal2022integrating` |
| 17 | 10.1088/1755-1315/1101/5/052008 | Digitalisation of the building permit process - a case study in Italy | olsson2018automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 18 | 10.18485/arh_pt.2020.7.ch24 | Digital Planning, Construction Submission and Approval Processes in Au | olsson2018automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 20 | 10.1007/978-3-032-06850-7_21 | Developing BIM Models for Building Approval | olsson2018automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 21 | 10.1088/1755-1315/1101/2/022049 | Code Checking using BIM for Digital Building Permit: a case study in a | olsson2018automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 22 | 10.3846/jcem.2022.17274 | Readiness assessment for BIM-based building permit processes using fuz | olsson2018automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 23 | 10.1016/j.jcde.2018.08.002 | Visual language approach to representing KBimCode-based Korea building | fauth2022conceptual r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 24 | 10.1061/9780784482421.042 | Virtual Building Permitting Framework for the State of Florida: Data C | fauth2022conceptual r | redundant zu `messaoudi2020virtual` (gleiche Gruppe, Florida) |
| 25 | – | Building regulations in Europe Part I: A comparison of the systems of  | fauth2022conceptual r | redundant: Bericht Meijer/Visscher 2002 ohne DOI; Argument durch `meijer2006deregulation` getragen |
| 26 | – | Comparison of building permit procedures in European Union countries | fauth2022conceptual r | redundant: Vergleich EU-Genehmigungsverfahren 2011 ohne DOI; Argument durch `fauth2024pace`, `meijer2017quality` getragen |
| 28 | – | Automatisierungspotenziale in der Verwaltung | fauth2022conceptual r | nicht verifiziert: ohne DOI, nicht geprüft; Thema Verwaltungsautomatisierung, FF4 möglicherweise 1-2, **nachprüfen** |
| 30 | 10.36253/979-12-215-0289-3.51 | Integrated GeBIM Requirements Definition for Digital Building Permit | fauth2022conceptual v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 31 | 10.36680/j.itcon.2026.033 | Ecosystem-based servitization assessment for the use case of building  | fauth2022conceptual v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 32 | 10.1108/jsfe-11-2025-0054 | A systematic review of BIM-based approaches for fire safety and automa | fauth2022conceptual v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 33 | 10.3389/fbuil.2022.834671 | Digital Twins in the Construction Industry: A Perspective of Practitio | fischer2023automation r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 34 | 10.36680/j.itcon.2021.024 | Potentials of Augmented Reality in a BIM based building submission pro | fischer2023automation r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 35 | 10.3390/buildings13061462 | Augmented Reality for Building Authorities: A Use Case Study in Austri | fischer2023automation r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 36 | 10.1061/(asce)0887-3801(1998)12:4(181) | Client/Server Framework for On-Line Building Code Checking | fischer2023automation r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 37 | – | Building environment rule and analysis (BERA) language and its applica | fischer2023automation r | nicht verifiziert: Dissertation ohne DOI; Zeitschriftenfassung (10.1007/s10846-014-0117-7) geprüft, Relevanz < 2 |
| 38 | 10.3390/buildings15173228 | Augmented Reality in Review Processes for Building Authorities: A Case | fischer2023automation v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 39 | 10.2139/ssrn.6329621 | SmartNorms4BIM: Automated Code Compliance based on Semantic Reasoning | fischer2023automation v | SSRN-Preprint |
| 40 | 10.1007/978-3-032-02376-6_21-1 | Automated Compliance Checking: Mathematics, Computing, and the Assessm | fischer2023automation v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 41 | 10.1016/j.autcon.2013.12.005 | Development of BIM-based evacuation regulation checking system for hig | ilal2022integrating r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 42 | 10.1007/978-3-319-91638-5_16 | Digital Construction Permit: A Round Trip Between GIS and IFC | ilal2022integrating r | redundant zu `noardo2020opportunities` (GIS-IFC-Genehmigung) |
| 43 | 10.2495/bim170151 | Building permits as proof of concepts in merging GIS and BIM informati | ilal2022integrating r | redundant zu `noardo2020opportunities` |
| 44 | 10.1061/(asce)0887-3801(1998)12:3(129) | Standards Modeling Language | ilal2022integrating r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 45 | 10.1201/b11647-6 | Towards a 3D geographic information system for the exploration of urba | ilal2022integrating r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 46 | 10.1068/b250617 | The Deregulation of Building Controls: A Comparison of Dutch and other | meijer2006deregulation r | redundant: Vorläufer von `meijer2006deregulation` (gleiche Autoren, 1998), redundant |
| 47 | 10.22004/ag.econ.30609 | Comparing Regulatory Systems: Institutions, Processes and Legal Forms  | meijer2006deregulation r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 48 | 10.1016/j.compenvurbsys.2018.03.006 | A building permit system for smart cities: A cloud-based framework | messaoudi2020virtual r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 49 | 10.1061/9780784482889.143 | Standardizing Ontario's Permitting Process for E-Permitting Implementa | messaoudi2020virtual r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 50 | 10.1068/b34120 | Towards a Better Understanding of Building Regulation | meijer2006deregulation v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 51 | 10.1108/02630800710772881 | Problems in enforcing Dutch building regulations | meijer2006deregulation v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 52 | 10.1111/j.1754-7121.2010.00138.x | One task, a few approaches, many impacts: Private-sector involvement i | meijer2006deregulation v | redundant: Parallelstudie Kanada zu `vanderheijden2010peanuts`, redundant |
| 54 | 10.1068/b34036 | Organisational Change in Systems of Building Regulation and Control: I | meijer2006deregulation v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 55 | 10.1068/b34038 | Quality Assurance in Construction by Independent Experts: A Case Study | meijer2006deregulation v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 56 | – | Building Regulatory Enforcement Regimes - Comparative Analysis of Priv | meijer2006deregulation v | redundant: Dissertation van der Heijden 2009 ohne DOI; Argument durch `vanderheijden2010peanuts` getragen |
| 57 | 10.1108/17561451311312793 | Regulating sustainable construction in Europe | meijer2006deregulation v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 58 | – | Measuring the evolution of online handling of building permits in Euro | meijer2006deregulation v | nicht verifiziert: ohne DOI, nicht geprüft |
| 59 | 10.3846/jcem.2023.18460 | Integration of structural information within a BIM-based environment f | ciotta2021structural v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 60 | 10.1007/978-3-031-57800-7_63 | Sustainability in the Context of BIM-Enabled Digital Building Permits | krischmann2020entwicklung v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 61 | 10.1007/978-3-032-18712-3_47 | A Mutli-agent AI System (MAS) for Roof Design | krischmann2020entwicklung v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 62 | 10.1007/978-981-97-5315-4_25 | Optimization of Time for the Revision of Norms in BIM Models of School | messaoudi2020virtual v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 63 | 10.1002/9781444393156 | Architectural Design and Regulation | meijer2017quality r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 64 | 10.1177/0042098009346068 | Regulating Design: The Practices of Architecture, Governance and Contr | meijer2017quality r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 65 | 10.1016/b978-193374207-6/50018-9 | Building Control Systems | meijer2017quality r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 66 | – | Building regulations in Europe: Part II - A comparison of technical re | meijer2017quality r | redundant: Bericht Meijer/Visscher 2003 (Teil II) ohne DOI, redundant |
| 67 | 10.1080/09613218.2016.1181955 | Comparative review of building commissioning regulation: a quality per | meijer2017quality r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 68 | 10.1080/01944369808975989 | Improving Compliance with Regulations: Choices and Outcomes for Local  | meijer2017quality r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 70 | 10.1016/j.ssci.2021.105337 | Roadmap for incorporating risk as a basis of performance objectives in | meijer2017quality v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 71 | 10.3351/ppp.2021.4964445474 | Housing quality and design standards in England: the driving forces fo | meijer2017quality v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 72 | 10.2478/admin-2018-0019 | Regulation of housing quality in Ireland: What can be learned from foo | meijer2017quality v | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 73 | 10.1016/j.aei.2008.06.005 | Specification and implementation of directional operators in a 3D spat | daum2014processing r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 74 | 10.1061/(asce)0887-3801(2009)23:1(34) | Implementing Metric Operators of a Spatial Query Language for 3D Build | daum2014processing r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 75 | 10.4018/978-1-60566-928-1.ch018 | Query Support for BIMs using Semantic and Spatial Conditions | daum2014processing r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 76 | 10.1016/j.autcon.2025.106034 | Releasing the power of graph for building information discovery | daum2014processing v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 77 | 10.3390/app10248794 | An Approach of Automatic SPARQL Generation for BIM Data Extraction | daum2014processing v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 78 | 10.3390/su151410901 | Compliance Checking on Topological Spatial Relationships of Building E | daum2014processing v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 79 | 10.26599/jic.2025.9180084 | Information Requirement Analysis for Establishing Intelligent Natural  | daum2014processing v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 80 | 10.2139/ssrn.6443038 | A large language model-based rule formalization framework for civil en | daum2014processing v | SSRN-Preprint |
| 81 | 10.48550/arxiv.1910.00334 | Towards French Smart Building Code: Compliance Checking Based on Seman | daum2014processing v | arXiv-Preprint |
| 82 | – | Automatic building information model query generation | daum2014processing v | nicht verifiziert: ohne DOI, nicht geprüft |
| 83 | 10.1016/j.autcon.2021.103834 | A deep neural network-based method for deep information extraction usi | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 84 | 10.1016/j.autcon.2022.104230 | Regulatory information transformation ruleset expansion to support aut | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 85 | 10.1016/j.autcon.2024.105730 | Question-answering framework for building codes using fine-tuned and d | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 86 | 10.1061/(asce)cp.1943-5487.0000583 | Semantic-Based Logic Representation and Reasoning for Automated Regula | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 87 | 10.1061/(asce)cp.1943-5487.0001002 | Model Validation Using Invariant Signatures and Logic-Based Inference  | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 88 | 10.1061/(asce)cp.1943-5487.0001000 | Semiautomated Generation of Logic Rules for Tabular Information in Bui | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 89 | 10.1061/(asce)cp.1943-5487.0000369 | Delivering the Infrastructure for Digital Building Regulations | yang2024promptbased r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 90 | 10.48550/arxiv.2201.11227 | Synchromesh: Reliable code generation from pre-trained language models | yang2024promptbased r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 91 | 10.1016/j.buildenv.2026.114260 | Ten questions concerning Large Language Models (LLMs) for building app | yang2024promptbased v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 92 | 10.1016/j.autcon.2026.106876 | Human-in-the-loop agent for product regulatory screening: Case study o | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 93 | 10.3390/buildings16112052 | Analysis of the Readiness of Regulatory Documents for Automation: A Co | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 94 | 10.2139/ssrn.6602381 | LLM-Based Structured Intermediate Representation for Building Regulati | yang2024promptbased v | SSRN-Preprint |
| 95 | 10.1061/jcemd4.coeng-18263 | RAG-for-CR: A Retrieval-Augmented Generation Framework for Efficient,  | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 96 | 10.1061/9780784486962.011 | Complex Building Code Interpretation Using Knowledge Graph-Based Large | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 97 | 10.1061/9780784486962.018 | Ontological Reasoning in the Built Environment: A Survey on Rule Const | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 98 | 10.1108/sasbe-03-2026-0231 | Automated formalization and verification of building code requirements | yang2024promptbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 99 | 10.1016/s0925-5273(98)00173-x | Introducing a platform strategy in product development | kruiper2024platformbased r | redundant zur Plattformliteratur im Bestand (`jensen2012configuration`, `zhou2023platforming`) |
| 100 | 10.1080/17452007.2026.2632098 | Graph-based rule representation for automated design checking | kruiper2024platformbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 101 | 10.1016/j.eswa.2026.131858 | A BERT-based intelligent framework for automated compliance checking o | kruiper2024platformbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 102 | 10.1007/978-3-032-15538-2_21 | Agentic Generation of Process Models from Regulatory Texts | kruiper2024platformbased v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 103 | 10.1016/j.aei.2021.101449 | Multi-ontology fusion and rule development to facilitate automated cod | hagedorn2025ontobpr r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 104 | 10.1016/j.aei.2024.102426 | Validation of technical requirements for a BIM model using semantic we | hagedorn2025ontobpr r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 105 | 10.3311/ccc2023-039 | Experiences of countries with the adoption of the BIM-based permit pro | hjelseth2015public v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 106 | 10.1007/978-3-032-18712-3_3 | Digital Verification of Construction Product Declarations: A Web-Based | hagedorn2025ontobpr v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 107 | 10.2139/ssrn.4556959 | Design Principles for Integrated Legislation Drafting Environment | hjelseth2015public v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 108 | 10.1061/9780784413982.ch02 | BIM-based Model Checking (BMC) | hjelseth2015public r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 109 | – | Foundations for BIM-based model checking systems: transforming regulat | hjelseth2015public r | nicht verifiziert: Dissertation ohne DOI, nicht geprüft; Argument durch `hjelseth2015public` getragen |
| 110 | 10.1596/978-0-8213-9984-2_topic_notes_2 | Dealing with construction permits | hjelseth2015public r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 111 | – | Configuration as Composite Constraint Satisfaction | gelle2003solving r | redundant: Tagungsbeitrag ohne DOI; Konfigurationsbegriff durch `sabin1998product`, `soininen1998general`, `felfernig2014knowledge` getragen |
| 112 | – | Dynamic constraint satisfaction problems | gelle2003solving r | redundant: wie oben (Mittal/Falkenhainer 1990), redundant |
| 113 | 10.1007/pl00007190 | Constraint Satisfaction Methods for Applications in Engineering | gelle2003solving r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 114 | 10.1007/978-3-642-38977-1_11 | Automated Analysis in Feature Modelling and Product Configuration | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 115 | 10.1109/mis.2007.6 | Configuration | gelle2003solving v | redundant zu `felfernig2014knowledge` |
| 116 | 10.3233/aic-2012-0545 | Beyond physical product configuration - Configuration in unusual domai | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 117 | 10.1080/00207543.2011.640714 | Domain-based production configuration with constraint satisfaction | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 118 | 10.1504/ijcat.2006.010085 | A constraint-based product configurator for mass customisation | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 119 | 10.1017/s0890060410000600 | Reasoning about conditional constraint specification problems and feat | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 120 | 10.1109/ieem.2007.4419409 | An approach to improve the efficiency of configurators | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 121 | 10.1080/00207543.2014.917216 | Attribute selection for product configurator design based on Gini inde | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 122 | 10.1017/s0890060410000624 | Adaptive attribute selection for configurator design via Shapley value | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 123 | 10.1007/978-3-540-24677-0_74 | A Systematic Search Strategy for Product Configuration | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 124 | 10.70675/3466dee1z32e5z4bb4z8964z4bf7e363bddf | Knowledge-based configuration: a contribution to generic modeling, eva | gelle2003solving v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 125 | 10.1109/access.2021.3108226 | A Semantic Approach for Automated Rule Compliance Checking in Construc | recski2024briseplandok r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 126 | 10.1016/j.aei.2020.101239 | Semantic information alignment of BIMs to computer-interpretable regul | zech2024bimreason r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 127 | 10.1061/9780784482421.045 | Automating Design Review with Artificial Intelligence and BIM: State o | zech2024bimreason r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 128 | – | Computerising the New Zealand Building Code for automated compliance a | recski2024briseplandok r | nicht verifiziert: Dissertation ohne DOI, nicht geprüft |
| 129 | 10.22260/isarc2019/0178 | Towards Rule-Based Model Checking of Building Information Models | zech2024bimreason r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 130 | 10.1007/s10506-018-9228-y | Semantic types of legal norms in German laws: classification and analy | recski2024briseplandok r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 131 | 10.1109/models67397.2025.00008 | An Ecosystem of DSMLs for Building Commissioning | zech2024bimreason v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 132 | 10.1068/b030037 | Synthesis and Optimization of Small Rectangular Floor Plans | lottaz1998constraint r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 133 | 10.1016/b978-0-12-660561-7.50020-x | WRIGHT: A constraint based spatial layout system | lottaz1998constraint r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 134 | 10.1007/978-94-011-0928-4_6 | A.S.A. An Interactive Assistant to Architectural Design | lottaz1998constraint r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 135 | 10.1007/978-3-642-11266-9_44 | How to Complete an Interactive Configuration Process? | lottaz1998constraint v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 136 | 10.1017/s0890060402164043 | Interactive constraint-aided conceptual design | lottaz1998constraint v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 137 | 10.52842/conf.caadria.2000.441 | A Constraint Based Generative System for Floor Layouts | lottaz1998constraint v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 138 | 10.5075/epfl-thesis-2119 | Collaborative design using solution spaces | lottaz1998constraint v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 139 | 10.1017/s0890060414000134 | Reuse of constraint knowledge bases and problem solvers explored in en | lottaz1998constraint v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 140 | 10.1016/s0926-5805(99)00020-5 | Parametric design: a review and some experiences | lee2006specifying r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 141 | 10.1016/s0957-4174(01)00030-6 | Knowledge-based parametric design of mechanical products based on conf | lee2006specifying r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 142 | 10.1016/0926-5805(95)00004-k | Towards integrated, intelligent, and compliant computer modeling of bu | lee2006specifying r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 143 | 10.1016/s0010-4485(02)00180-x | Selecting and parameterising components using knowledge based configur | lee2006specifying r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 144 | 10.1016/0926-5805(94)90017-5 | Knowledge-based computational support for architectural design | lee2006specifying r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 145 | 10.1016/j.proeng.2015.10.104 | Modular Coordination and BIM: Development of Rule Based Smart Building | lee2006specifying v | Tagungsfassung zu `singh2017integrating` (Bestand) |
| 146 | 10.1016/j.aei.2012.04.008 | Design Scenarios: Enabling transparent parametric design spaces | lee2006specifying v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 147 | 10.1016/j.autcon.2018.02.031 | BIM semantics for digital fabrication: A knowledge-based approach | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 148 | – | INFORMATION MANAGEMENT IN INDUSTRIAL HOUSING DESIGN AND MANUFACTURE | lee2006specifying v | nicht verifiziert: ohne DOI, nicht geprüft; Titel deutet auf FF1/FF2, **nachprüfen** |
| 149 | 10.1016/j.autcon.2018.12.024 | Integrating Building Information Modeling and Prefabrication Housing P | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 150 | 10.1061/9780784482421.040 | Schema for Automated Generation of CLT Framing and Panelization | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 151 | 10.1061/9780784485231.068 | Design Support Engine for Mass Engineered Timber Buildings | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 152 | 10.3233/atde200117 | Parametric Modelling of Steel Connectors in a Glulam Based Post and Be | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 153 | – | A Knowledge-based system framework for semantic enrichment and automat | lee2006specifying v | nicht verifiziert: ohne DOI, nicht geprüft |
| 154 | 10.52842/conf.caadria.2011.731 | Using domain specific languages in the Building Information Modelling  | lee2006specifying v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 155 | 10.1115/1.4031637 | Product Family Design With Solution Spaces | zimmermann2013computing v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 156 | 10.1017/pds.2023.287 | Optimizing requirements for maximum design freedom considering physica | zimmermann2013computing v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 157 | 10.1007/s10846-014-0117-7 | Implementation of a BIM Domain-specific Language for the Building Envi | lee2019efficient r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 158 | 10.1061/(asce)0887-3801(1995)9:2(141) | Automatic Fire-Code Checking Using Expert-System Technology | lee2019efficient r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 159 | 10.1016/j.autcon.2018.02.004 | Ontology- and freeware-based platform for rapid development of BIM app | lee2019efficient r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 160 | 10.1016/j.autcon.2020.103451 | Combining multi-criteria decision making (MCDM) methods with building  | lee2019efficient v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 161 | 10.1108/ecam-10-2023-1037 | Automated compliance checking for BIM models based on Chinese-NLP and  | lee2019efficient v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 162 | 10.36680/j.itcon.2024.037 | Exploring the use of parametric design in the AEC sector to improve an | lee2019efficient v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 163 | 10.1007/978-981-97-1949-5_113 | Transitioning to Intelligent Compliance Checking in Construction: A Re | lee2019efficient v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 164 | 10.1016/j.autcon.2015.05.008 | RDF-based signature algorithms for computing differences of IFC models | esser2022graphbased r | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 165 | 10.1016/j.aei.2010.12.001 | An approach to distributed building modeling on the basis of versions  | esser2022graphbased r | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 166 | 10.1016/j.dibe.2024.100418 | Automated generative design and prefabrication of precast buildings us | esser2022graphbased v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 167 | 10.1016/j.autcon.2023.104979 | Graph-based inter-domain consistency maintenance for BIM models | esser2022graphbased v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 168 | 10.1016/j.autcon.2023.105063 | Version control for asynchronous BIM collaboration: Model merging thro | esser2022graphbased v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 169 | 10.1016/j.autcon.2025.106670 | Decoupling IFC models for reliable modification of shared references | esser2022graphbased v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 170 | 10.1061/jccee5.cpeng-5487 | A Framework for Generic Semantic Enrichment of BIM Models | esser2022graphbased v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 171 | 10.1109/mipro70003.2026.11591903 | New Croatian Construction Act and Building Information Modelling (BIM) | urban2025augmented v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 172 | 10.1108/ecam-12-2020-1040 | Method for managing requirements in healthcare projects using building | solimanjunior2022designers r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 173 | 10.1061/9780784412848.082 | SmartCodes and BIM | solimanjunior2022designers r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 174 | 10.1016/0142-694x(88)90037-3 | Standards and the design process | solimanjunior2022designers r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 175 | 10.1080/0144619042000201411 | A framework for identification and representation of client requiremen | solimanjunior2022designers r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 176 | 10.1596/978-1-4648-0351-2 | Doing Business 2015: Going Beyond Efficiency | fauth2023process r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 177 | 10.1061/40513(279)143 | Document Management in Building Authorities with the Aid of a Workflow | fauth2023process r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 178 | 10.1145/2910019.2910028 | Bridging the Gaps Between Laws and their Application | fauth2023process r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 179 | 10.1061/9780784480502.072 | The Role of BIM in Simplifying Construction Permits in Kuwait | fauth2023process r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 180 | 10.1109/sims.2018.8355304 | The devil is in the detail: The link between building regulatory proce | sei2025understanding r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 181 | 10.1002/9780470759592.ch2 | The Building Regulations and Building Control | sei2025understanding r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 182 | 10.35490/ec3.2024.215 | Real-Time Assessment of Regulatory Compliance of Construction Sites | sei2025understanding r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 183 | 10.1111/padm.12534 | Public administration, public leadership and the construction of publi | sei2025understanding r | Relevanz < 2: Regulierungstheorie/-politik ohne Bezug zu Verfahren oder Entwurf |
| 184 | 10.1016/j.autcon.2024.105496 | A blockchain-based engineering design review service trading scheme fo | liu2025coordination r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 185 | 10.1016/j.autcon.2025.106369 | Semantic BIM enrichment using a hybrid ML and rule-based framework for | sei2025understanding v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 186 | 10.1016/j.autcon.2025.106268 | Ontology-based representation of quality assurance and inspection plan | sei2025understanding v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 187 | 10.1016/j.aei.2025.103650 | Reducing construction quality costs through ontology-based inspection  | sei2025understanding v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 188 | 10.35490/ec3.2023.207 | Automated generation of SPARQL queries from semantic mark-up | solimanjunior2022designers v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 190 | 10.1145/3736425.3770118 | A Vision-Language Model Agent for building code compliance | solimanjunior2022designers v | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 191 | 10.1061/9780784486962.048 | Reducing Demolition Regulatory Non-Compliance and Permitting Duration  | fauth2023process v | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 192 | 10.1007/978-3-031-61503-0_15 | Integrating Building Information Modeling (BIM), Universal Design (UD) | solimanjunior2022designers v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 193 | 10.1080/15623599.2024.2366727 | Moving automated compliance checking to the operational phase of the b | hartmann2026status r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 194 | 10.1007/978-3-658-21402-9_5 | E-Government in Deutschland: Ein Überblick | fauth2025baugenehmigungsv r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 195 | – | A Comparative Analysis of Building Permits Procedures in Slovenia and  | fauth2024pace r | nicht verifiziert: ohne DOI, nicht geprüft |
| 196 | 10.22260/isarc2015/0031 | An Approach to Translate Korea Building Act into Computer-Readable For | fauth2023requirements r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 197 | 10.1007/978-3-658-05606-3 | Building Information Modeling | fauth2025baugenehmigungsv r | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 198 | 10.1016/j.giq.2019.03.002 | Close encounters of the digital kind: A research agenda for the digita | akbas2025holistic r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 199 | 10.18178/ijimt.2022.13.3.921 | A Decision Support System for the Building Permit Review Process | weinkauf2024decision r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 200 | 10.24989/ocg.v338.8 | Usability of digitized citizens' services | akbas2025holistic r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 201 | 10.1145/3511889 | Consortium of Municipalities Co-tailoring a Governmental e-Service Pla | akbas2025holistic r | Relevanz < 2: Genehmigung/E-Permit außerhalb Deutschlands oder allgemeiner Verwaltungskontext (Einzelfall) |
| 202 | 10.1038/s41598-023-34342-1 | Automated code compliance checking research based on BIM and knowledge | yang2026llmpowered r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 203 | 10.3389/fbuil.2025.1575913 | Semantic and ontology-based analysis of regulatory documents for const | yang2026llmpowered r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 205 | 10.1016/j.jobe.2023.106701 | BIM product recommendation for intelligent design using style learning | feng2026bridging r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 206 | 10.1111/cgf.14844 | A Survey of Personalized Interior Design | feng2026bridging r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 207 | 10.46421/2706-6568.37.2020.paper018 | Semantic Web and Linked Data for Information Exchange between the Buil | vanberlo2019creating v | Relevanz < 2: BIM-Datenhaltung, Versionierung oder Bauteilschema ohne FF-Bezug |
| 208 | 10.1109/taslp.2020.2983593 | Out-of-Domain Detection for Natural Language Understanding in Dialog S | wang2022transfer r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 209 | 10.1016/j.aei.2020.101195 | A building regulation question answering system: A deep learning metho | wang2022transfer r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 210 | 10.1016/j.autcon.2023.105200 | Text mining and natural language processing in construction | wang2022transfer v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 211 | 10.3390/buildings14082511 | Utilizing Large Language Models to Illustrate Constraints for Construc | wang2022transfer v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 212 | 10.1016/j.buildenv.2025.113855 | BuildingGPT: Query building semantic data using large language models  | wang2022transfer v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 213 | 10.1016/j.autcon.2025.106738 | Enhancing LLM-based building data query with chain-of-thought, retriev | wang2022transfer v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 214 | 10.2139/ssrn.4791534 | Bridging Bim with Ai: A Gpt-Powered Assistant for Real-Time Modeling A | wang2022transfer v | SSRN-Vorfassung zu `fernandes2024gptassistant` (Bestand) |
| 215 | 10.2139/ssrn.5179919 | ArcBIM: Low-Prerequisite, High-Flexible, and Cost-Effective BIM Inform | wang2022transfer v | SSRN-Preprint (ArcBIM) |
| 216 | 10.1016/j.compind.2026.104462 | Learning to ask and answer in specialized documents: Exemplifying thro | wang2022transfer v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 217 | 10.1016/j.autcon.2022.104540 | Transformer-based approach for automated context-aware IFC-regulation  | yin2023twostage r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 218 | 10.1061/9780784483961.055 | Named Entity Recognition Algorithm for iBISDS Using Neural Network | yin2023twostage r | Relevanz < 2: ACC-/Regelextraktionsmethodik ohne Entwurfs- oder Konfiguratorbezug, Argument im Bestand getragen |
| 220 | 10.36680/j.itcon.2021.022 | Multi-scale Information Retrieval for BIM using Hierarchical Structure | guo2025advancing r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 223 | 10.1061/9780784486979.036 | Error Taxonomy and Failure Analysis of Large Language Models for BIM S | guo2025advancing v | Tagungsfassung zu `alwashah2026reliable` (aufgenommen) |
| 224 | 10.3390/buildings16163168 | A Metadata-Grounded LLM Framework for Conversational BIM Information R | guo2025advancing v | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 225 | 10.1016/j.autcon.2022.104234 | Automated modular housing design using a module configuration algorith | gao2025lifecycle r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 228 | 10.1016/j.autcon.2017.03.008 | Near optimum selection of module configuration for efficient modular c | gao2025lifecycle r | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 229 | 10.52842/conf.caadria.2018.2.071 | BIM-Based Model Checking in the Early Design Phases of Precast Concret | gao2025lifecycle r | redundant zu `an2020bimbased`, `cao2022ontologybased` (Fertigungsregeln im Frühentwurf; Betonfertigteile) |
| 231 | 10.3390/su12072804 | Using Building Information Modelling to Manage Client Requirements in  | bagasi2025bim r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 232 | 10.52842/conf.caadria.2021.2.071 | Facilitating Architect-Client Communication in the Pre-design Phase | bagasi2025bim r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 233 | 10.1016/j.autcon.2022.104483 | Intelligent question and answer system for building information modeli | bagasi2025bim r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 234 | 10.1080/17452007.2025.2456768 | Balancing performance and cost of LLMs in a multi-agent framework for  | dong2025bim r | Relevanz < 2: nur Informationsabfrage, keine Modelländerung |
| 235 | 10.2139/ssrn.5193679 | A Multi-Agent Large Language Model (LLM) Framework for Code-Complying  | dong2025bim r | SSRN-Preprint |
| 236 | 10.3390/buildings15152684 | Platform Approaches in the AEC Industry: Stakeholder Perspectives and  | dong2025bim v | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 237 | 10.1016/j.autcon.2026.106846 | Human-operational 3D indoor layout generation with LLM-driven anthropo | dong2025bim v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 238 | 10.1109/icicv68925.2026.11554740 | SmartFloor: AI-Powered Natural Language to 3D Architectural Visualizat | dong2025bim v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 239 | 10.3390/su18136386 | REGEN: A Regulation-Aware Generative Design Framework for BIM-Enabled  | dong2025bim v | redundant zu `niemeijer2014freedom` (Vorschriften als Constraints im Entwurf) |
| 240 | 10.3390/buildings16132502 | AI-Assisted Residential Layout Generation: A Comparative Study of Plan | dong2025bim v | Relevanz < 2: Layout-/Generativverfahren ohne Bezug zu Fertigungs- oder Genehmigungsregeln |
| 241 | 10.2139/ssrn.7347219 | Script-Mediated Semantic State Modeling for Highly Controllable Intera | dong2025bim v | SSRN-Preprint |
| 242 | 10.3390/buildings11120583 | Exploring Natural Language Processing in Construction and Integration  | jin2026evaluating r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 243 | 10.1609/aimag.v13i1.976 | Algorithms for constraint-satisfaction problems: a survey | mcdermott1982rulebased r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 244 | – | Towards a generic model of configuraton tasks | xie2005modelling r | redundant: wie oben (Mittal/Frayman 1989), redundant |
| 245 | – | An overview of knowledge-based configuration | xie2005modelling r | redundant: wie oben (Übersicht wissensbasierte Konfiguration), redundant |
| 246 | 10.3233/ica-2003-10207 | Mass customization and configuration: Requirement analysis and constra | xie2005modelling r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 247 | 10.1007/3-540-57292-9_68 | A generative constraint formalism for configuration problems | xie2005modelling r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 248 | 10.1609/aimag.v14i3.1055 | A Knowledge-Based Configurator that Supports Sales, Engineering, and M | mcdermott1982rulebased v | redundant: Konfiguratoranwendung, redundant zu `felfernig2014knowledge` |
| 249 | 10.3233/aic-2012-0547 | WeCoTin - A practical logic-based sales configurator | mcdermott1982rulebased v | redundant: wie 248 |
| 250 | 10.1017/s0890060498124046 | Generative constraint-based configuration of large technical systems | mcdermott1982rulebased v | redundant: wie 248 |
| 251 | 10.1017/s0890060410000570 | Modeling and solving technical product configuration problems | mcdermott1982rulebased v | redundant: wie 248 |
| 252 | 10.1609/aimag.v37i4.2688 | Twenty-Five Years of Successful Application of Constraint Technologies | mcdermott1982rulebased v | redundant zu `felfernig2014knowledge` (Siemens-Autoren dort beteiligt) |
| 253 | 10.1017/dsd.2020.129 | Integrating sales and design: applying CAD configurators in the produc | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 254 | 10.48550/arxiv.2102.08113 | Recommender Systems for Configuration Knowledge Engineering | mcdermott1982rulebased v | arXiv-Preprint |
| 256 | 10.1017/s0890060410000582 | Product configuration as decision support: The declarative paradigm in | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 257 | 10.3390/a15090318 | Joining Constraint Satisfaction Problems and Configurable CAD Product  | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 258 | 10.1007/bfb0025022 | The design of building parts by using knowledge based systems | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 259 | 10.1007/978-94-009-0279-4_21 | Explanatory Interface in Interactive Design Environments | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 260 | 10.1145/3468784.3468785 | Interactive Online Configurator via Boolean Satisfiability Modeling | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 262 | 10.1007/978-3-030-55789-8_12 | ConMerge - Arbitration of Constraint-Based Knowledge Bases | mcdermott1982rulebased v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 263 | 10.1016/j.procir.2019.04.124 | Relative preference-based product configurator design | wang2018mapping v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 264 | 10.1016/j.cad.2008.05.004 | Development of a product configuration system with an ontology-based a | xie2005modelling v | redundant zu `yang2012constraint` (gleiche Gruppe) |
| 265 | 10.1108/17410380810888120 | Automating knowledge acquisition for constraint-based product configur | xie2005modelling v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 266 | 10.1007/s10844-016-0431-6 | Building renovation adopts mass customization | xie2005modelling v | redundant zu `vareilles2013renovation` (gleiche Gruppe) |
| 267 | 10.1007/s10845-017-1333-3 | Applications of non-monotonic reasoning to automotive product configur | xie2005modelling v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 268 | 10.1007/978-3-319-58409-6_11 | Resolving Product Configuration Conflicts | xie2005modelling v | redundant zu `yang2012constraint`, `felfernig2011personalized` |
| 269 | 10.1007/s10601-025-09381-2 | Solutions and minimal conflict search for product configuration | xie2005modelling v | redundant zu `felfernig2011personalized`, `yang2012constraint` (Konfliktauflösung über Restriktionstabellen, Pumpen) |
| 271 | 10.1016/j.eswa.2005.06.026 | Applying case-based reasoning for product configuration in mass custom | rasmussen2020guidelines r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 272 | 10.1017/s0890060498124101 | A classification and constraint-based framework for configuration | rasmussen2020guidelines r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 273 | 10.1016/j.eswa.2008.05.026 | Product configuration knowledge modeling using ontology web language | rasmussen2020guidelines r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 274 | 10.1016/j.aei.2017.02.004 | The documentation of product configuration systems: A framework and an | rasmussen2020guidelines r | redundant zur Hvam-Gruppe im Bestand (`haug2012definition`, `kristjansdottir2018challenges`) |
| 275 | 10.5555/2666064.2666072 | Towards more reliable configurators: a re-engineering perspective | rasmussen2020guidelines r | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |
| 276 | 10.1016/j.compind.2020.103357 | Text mining tool for translating terms of contract into technical spec | dudek2023mass r | Relevanz < 2: fremde Domäne oder allgemeine NLP-/LLM-Übersicht (höchstens 1) |
| 277 | 10.1080/09544828.2024.2335136 | Design of product configuration systems supporting customer | rasmussen2020guidelines v | Relevanz < 2: allgemeine Konfigurations-/CSP-Methodik ohne Baubezug, Argument im Bestand (felfernig2014knowledge, sabin1998product) |

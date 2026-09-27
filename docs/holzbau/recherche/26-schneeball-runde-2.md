# Recherche 26: Schneeballverfahren Runde 2 (FF1–FF6)

Status: v0.1 (27.09.2026). Nicht committet. Gehört zu `../arbeit/02a-review-protokoll.md` (2a.3 Nr. 3, 2a.4, 2a.5, 2a.6 Schritt 4) und setzt Runde 1 fort (`24-schneeball-ff1-ff2-ff4.md`, `25-schneeball-ff3-ff5-ff6.md`).
Literaturdatei: `../arbeit/literatur/lit-J-schneeball-runde2.bib` (162 Einträge, alle [V]; 158 mit DOI, 4 ohne DOI).

**Verfahren:** Wohlin (2014), eine Iteration je Startquelle, rückwärts (Referenzen) und vorwärts (zitierende Arbeiten). Vorgehen, Werkzeuge und Einschränkungen wie in Runde 1. Screening gegen alle sechs Forschungsfragen nach `literatur/bewertung/AUFTRAG.md`. Aufgenommen wird nur, was in mindestens einer FF Relevanz ≥ 2 erreicht und bibliografisch verifiziert ist.

Die Maßstäbe für „Relevanz 2“ und „Relevanz 3“ sind dieselben wie in Runde 1:
- **2** stützt ein konkretes Argument der Arbeit.
- **3** trägt ein zentrales Argument oder liefert einen übernehmbaren Baustein.
- Generische Anwendungen in fremden Domänen erhalten höchstens 1. Das gilt etwa für NLP-Regelextraktion für chinesische Brandschutz- oder Tunnelnormen oder für Lärmmedizin ohne Entwurfsbezug.
- Funde, die nur ein Argument wiederholen, das eine Bestandsquelle schon trägt, werden als „redundant“ geführt und nicht aufgenommen.

## Ergebnis in Kürze

1. **Umfang:**
   - 47 Startquellen, 4 911 gesichtete Datensätze (rückwärts 2 385, vorwärts 2 526)
   - 411 Kandidaten zur Abstract-Prüfung, davon 72 Dubletten zum Bestand
   - **162 aufgenommen**, davon 3 mit Relevanz 3
2. **Aufnahmequote:**
   - Runde 2: 3,3 % (162 von 4 911)
   - Runde 1: 4,4 % (286 von 6 437, gleiche Zählweise ohne rundeninterne Bereinigung)
   - Die Quote sinkt damit relativ um 26 %.
   - Pro neuem Kandidat trifft Runde 2 seltener: 48 % gegenüber 53 % (Teil A) und 83 % (Teil B).
   - Unter den neuen Kandidaten sind 17 % bloße Wiederholungen oder Vorfassungen, in Runde 1 waren es 3,5 %.
3. **Drei neue Quellen mit Relevanz 3:**
   - `wei2025texttostructure` (TUM, FF3): Nutzeranfragen werden in Intent und Slots zerlegt und als Revit-Aktion ausgeführt. Das ist ein übernehmbarer Baustein für die Intent-Schicht.
   - `an2020bimbased` (Alberta, FF2): automatische Prüfung der Fertigbarkeit von Holzrahmen-Baugruppen gegen Maschinenrestriktionen, also Herstellerregeln als Prüfung im Entwurf.
   - `zhang2022bimbased` (Alberta, FF6): automatischer Entwurf der Entwässerung für Wohngebäude im Tafelbau.
4. **Stärkste neue Befunde je Forschungsfrage:**
   - **FF4:** zwei bundesweite deutsche Erhebungen zum Baugenehmigungsverfahren (`fauth2025baugenehmigungsv` mit 649 Teilnehmern, `hartmann2026status` bei Bauaufsichten) sowie die europäische Einordnung privater Bauaufsicht (`meijer2006deregulation`, `meijer2017quality`).
   - **FF3:** eine Linie von natürlicher Sprache über eine Zwischenrepräsentation zu deterministischem Code: `yin2023twostage` (Text-zu-BIMQL), `guo2025advancing` (LLM-DSL mit Code-Funktionen), `yang2026llmpowered` (natürliche Sprache zu IDS).
   - **FF1/FF2:** schwedische Plattformforschung zum Holzfertighaus (`johnsson2007ict`, `malmgren2010customization`, `lennartsson2021plm`, `vestin2023mitigating`).
   - **FF5:** Evaluationsbausteine (TAM, heuristische Evaluation, Applicability Checks, Erklärungsforschung).
   - **FF6:** Schlafraum, Fensterorientierung und ruhige Fassadenseite sowie melanopische Metrik (CIE S 026).
5. **Sättigung nach 2a.3:**
   - **Nicht erreicht.** Die Quote liegt unter Runde 1, aber nicht „deutlich“ (weniger als halbiert), und drei Quellen erreichen Relevanz 3.
   - **Empfehlung:** eine *gezielte* Runde 3, ausgehend von den drei R3-Funden und den beiden Clustern, die noch über dem Niveau von Runde 1 liefern (FF3 Sprache, FF2/FF4 Bauantrag). Für die übrigen Cluster ist keine weitere Runde nötig (Abschnitt 6).

## 1 Startmenge

Auswahlregel (Auftrag): `id ≥ Q531` (in Runde 1 neu gefunden) UND `kern = ja` UND `art = W`, ausgewertet auf `literatur/quellen-bewertung.csv` (811 Zeilen, Stand 27.09.2026). Ergebnis: **47 Startquellen**. Alle 47 sind in OpenAlex per DOI auffindbar.

| id | Key | ff1 | ff2 | ff3 | ff4 | ff5 | ff6 | P | OpenAlex-ID | Referenzen / Zitierende (OpenAlex) |
|---|---|---|---|---|---|---|---|---|---|---|
| Q537 | `bloch2023unbalanced` | 0 | 1 | 0 | 2 | 0 | 0 | 5.0 | W4387017062 | 51 / 30 |
| Q552 | `fischer2024extending` | 0 | 3 | 0 | 0 | 0 | 0 | 5.5 | W4403912815 | 36 / 18 |
| Q576 | `lee2026automated` | 0 | 2 | 0 | 0 | 0 | 0 | 5.0 | W7133562547 | 116 / 7 |
| Q592 | `narayanaswamy2019bim` | 1 | 3 | 0 | 0 | 0 | 0 | 5.5 | W2955625167 | 10 / 23 |
| Q596 | `niemeijer2014freedom` | 0 | 3 | 1 | 0 | 0 | 0 | 5.5 | W2162535319 | 46 / 15 |
| Q598 | `nuyts2024comparative` | 0 | 3 | 0 | 0 | 0 | 0 | 5.5 | W4392265030 | 32 / 34 |
| Q604 | `pinto2026exhaustive` | 0 | 3 | 0 | 1 | 0 | 0 | 5.5 | W7214018051 | 54 / 0 |
| Q611 | `senousy2026automated` | 0 | 2 | 1 | 1 | 0 | 0 | 5.0 | W7172460384 | 70 / 0 |
| Q621 | `urban2026development` | 0 | 3 | 0 | 2 | 0 | 0 | 5.5 | W7168152718 | 32 / 0 |
| Q623 | `vestin2022information` | 2 | 0 | 0 | 0 | 1 | 0 | 5.5 | W4224274985 | 41 / 3 |
| Q626 | `wu2025design` | 0 | 3 | 0 | 0 | 1 | 0 | 5.5 | W4406886975 | 103 / 9 |
| Q628 | `yin2019building` | 2 | 0 | 0 | 0 | 1 | 0 | 5.0 | W2911311605 | 247 / 422 |
| Q630 | `zentgraf2023concept` | 0 | 2 | 0 | 0 | 0 | 0 | 5.5 | W4392221391 | 18 / 1 |
| Q634 | `zhang2023rule` | 0 | 2 | 0 | 0 | 0 | 0 | 5.0 | W4384666463 | 77 / 11 |
| Q644 | `gregor1999explanations` | 0 | 2 | 1 | 1 | 0 | 2 | 6.0 | W1576620340 | 125 / 537 |
| Q655 | `park2026bimllm` | 0 | 0 | 2 | 0 | 1 | 0 | 5.0 | W7143448972 | 67 / 1 |
| Q660 | `wang2022natural` | 0 | 0 | 3 | 0 | 0 | 1 | 5.5 | W3189014113 | 53 / 35 |
| Q662 | `wu2026alterations` | 0 | 2 | 3 | 0 | 0 | 0 | 5.5 | W7169758746 | 18 / 0 |
| Q669 | `campogay2026quality` | 0 | 1 | 0 | 0 | 3 | 0 | 5.5 | W7212399974 | 55 / 0 |
| Q682 | `grenzfurtner2026failure` | 0 | 0 | 0 | 0 | 2 | 0 | 5.5 | W7140112933 | 41 / 0 |
| Q703 | `love2022rework` | 0 | 0 | 0 | 0 | 2 | 0 | 5.0 | W4282839789 | 93 / 48 |
| Q716 | `sonnenberg2012patterns` | 0 | 0 | 0 | 0 | 2 | 0 | 5.5 | W130008378 | 22 / 144 |
| Q721 | `trentin2011overcoming` | 0 | 0 | 0 | 0 | 3 | 0 | 5.5 | W2056765331 | 93 / 59 |
| Q724 | `virzi1992subjects` | 0 | 0 | 0 | 0 | 2 | 0 | 5.5 | W1596953637 | 11 / 1230 |
| Q726 | `vonhippel2001user` | 0 | 3 | 0 | 0 | 2 | 0 | 5.5 | W2000718498 | 34 / 521 |
| Q732 | `abualdenien2020consistent` | 2 | 0 | 0 | 0 | 0 | 2 | 5.5 | W3013281327 | 43 / 33 |
| Q735 | `ahn2013roofs` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2051964651 | 25 / 6 |
| Q736 | `aichholzer1996general` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W1887122289 | 14 / 172 |
| Q743 | `basner2010guidance` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2052731732 | 41 / 50 |
| Q744 | `biedl2015weighted` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2138168865 | 25 / 48 |
| Q747 | `bodin2015quiet` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2009952491 | 32 / 123 |
| Q749 | `brown2020melanopic` | 0 | 0 | 0 | 0 | 0 | 2 | 6.0 | W3014760713 | 57 / 251 |
| Q750 | `cain2020evening` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W3095576386 | 43 / 119 |
| Q751 | `cajochen2022evening` | 0 | 0 | 0 | 0 | 0 | 2 | 6.0 | W4290080716 | 66 / 39 |
| Q752 | `chateauvieuxhellwig2022timber` | 2 | 0 | 0 | 0 | 0 | 3 | 6.5 | W4283755222 | 51 / 3 |
| Q753 | `chateauvieuxhellwig2025schallschutz` | 2 | 0 | 0 | 0 | 0 | 3 | 6.0 | W4408375823 | 6 / 0 |
| Q761 | `dosen2013methodological` | 0 | 0 | 0 | 0 | 0 | 2 | 5.0 | W2049791344 | 33 / 24 |
| Q764 | `eder2018volume` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2939968013 | 7 / 0 |
| Q765 | `eder2021exact` | 0 | 0 | 0 | 0 | 0 | 3 | 6.5 | W3134191041 | 33 / 6 |
| Q766 | `emmitt2023bedroom` | 0 | 0 | 0 | 0 | 0 | 2 | 5.0 | W4385387143 | 43 / 13 |
| Q772 | `held2017roofs` | 0 | 0 | 0 | 0 | 0 | 3 | 6.5 | W2340286203 | 37 / 32 |
| Q783 | `locher2018windows` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W2788686826 | 30 / 89 |
| Q791 | `ohrstrom2006quietness` | 0 | 0 | 0 | 0 | 0 | 3 | 6.5 | W2043882265 | 23 / 345 |
| Q797 | `potter2025sleep` | 0 | 0 | 0 | 0 | 0 | 2 | 5.0 | W4414154390 | 203 / 0 |
| Q800 | `spitschan2021luox` | 0 | 0 | 0 | 0 | 0 | 2 | 5.5 | W3148041589 | 73 / 20 |
| Q808 | `wiener2007isovist` | 0 | 0 | 0 | 0 | 0 | 3 | 5.5 | W2048830551 | 49 / 83 |
| Q811 | `zhao2025mep` | 0 | 0 | 0 | 0 | 0 | 2 | 5.0 | W4406227355 | 142 / 2 |
**Befund zur Startmenge:**
- **Verteilung nach FF:** Die Startmenge ist nach FF6 verschoben. Nach Haupt-FF (höchster Wert, bei Gleichstand FF4 vor FF2 vor FF1 vor FF3 vor FF5 vor FF6) entfallen 21 der 47 Startquellen auf FF6 (Dach, Schall, Licht, Architekturpsychologie, TGA). Es folgen FF2 mit 13, FF5 mit 6, FF1 und FF3 mit je 3 und FF4 mit 1.
- **FF4:** Nur zwei Startquellen erreichen ff4 = 2 (`bloch2023unbalanced`, `urban2026development`). Keine erreicht ff4 = 3.
- **Kaum Vorwärtskanten:** Elf Startquellen haben 0 oder 1 zitierende Arbeit, meist weil sie aus 2025/2026 stammen. Sie tragen fast nur rückwärts bei.

## 2 Suchweg und Werkzeuge

Das Vorgehen entspricht Runde 1, mit folgenden Einschränkungen:

- **Gesperrte Dienste:** Semantic Scholar, OpenAlex und Crossref sind direkt per Proxy gesperrt (403, geprüft 27.09.2026). Auch doi.org, OpenCitations, DataCite, dblp und Europe PMC sind nicht erreichbar. Alle Abfragen laufen deshalb über `mcp__Exa__web_fetch_exa`.
- **Kanten aus OpenAlex:**
  - rückwärts: `works?filter=cited_by:<W-ID>`
  - vorwärts: `works?filter=cites:<W-ID>`
  - Bei mehr als 400 Zitierenden wird wie in Runde 1 gezielt vorgegangen: Volltextfilter (`search=`) mit Bau- und Wohnbegriffen, Filter in Tabelle 3.
  - Die Zuordnung der Kandidaten zu Startquellen ist maschinell über `referenced_works` beider Seiten geprüft. Eine Quelle zählt deshalb bei jeder Startquelle, die sie erreicht (29 der 158 DOI-Funde erreichen mehr als eine Startquelle).
- **Abstracts:**
  - über OpenAlex (`abstract_inverted_index`, rekonstruiert) für 124 der 158 DOI-Funde
  - für fünf zentrale Elsevier-Artikel ohne OpenAlex-Abstract über Verlags- oder Repositoriumsseiten (Exa-Suche)
  - 34 Funde sind nach Titel, Venue und Zitationskontext eingestuft. Das ist im `note`-Feld vermerkt.
- **Verifikation:**
  - 157 DOIs über Crossref (`api.crossref.org/works?filter=doi:…`, Exa-Fetch: Autoren, Venue, Band, Seiten, Jahr)
  - 1 DOI über OpenAlex (AI Magazine, nicht in Crossref)
  - 4 Quellen ohne DOI über UGent-Bibliografie, TU/e-Portal, Lund University Publications, ITC-SciX und IngentaConnect
- **Dubletten:**
  - gegen `quellen-master.csv` (811 Einträge; DOI exakt, Titel normalisiert auf 60 Zeichen und Präfixabgleich)
  - zusätzlich gegen DOI und Titel aller `lit-*.bib`
  - Keine Key-Kollision mit den vorhandenen Keys. Zwei bestehende Doppel-Keys in anderen Dateien (`du2026text2bim`, `mbo2bim2023`) sind unberührt.

## 3 Protokoll je Startquelle

**Zählweise:**
- „gesichtet“: Datensätze der OpenAlex-Liste (rückwärts nur die in OpenAlex auflösbaren Referenzen)
- „Kandidaten“: nach Titel-Screening zur Abstract-Prüfung vorgemerkt, einschließlich Bestandsdubletten, gezählt über alle Kanten
- „davon Bestand“: Dublette zu `quellen-master.csv`
- „aufgenommen“: in `lit-J-schneeball-runde2.bib`, gezählt über alle Kanten
- r = rückwärts, v = vorwärts

| Start | Referenzen gesichtet | Zitierende gesichtet | Kandidaten r / v | davon Bestand r / v | aufgenommen r / v | Anmerkung |
|---|---|---|---|---|---|---|
| Q537 `bloch2023unbalanced` | 46 | 30 | 21 / 15 | 4 / 1 | 8 / 10 | vollständig |
| Q552 `fischer2024extending` | 27 | 18 | 8 / 7 | 2 / 1 | 4 / 4 | vollständig |
| Q576 `lee2026automated` | 116 | 7 | 23 / 2 | 7 / 0 | 4 / 0 | vollständig |
| Q592 `narayanaswamy2019bim` | 9 | 23 | 3 / 7 | 1 / 0 | 0 / 2 | vollständig |
| Q596 `niemeijer2014freedom` | 42 | 14 | 8 / 5 | 1 / 1 | 3 / 2 | vollständig |
| Q598 `nuyts2024comparative` | 22 | 34 | 11 / 8 | 2 / 0 | 3 / 2 | vollständig |
| Q604 `pinto2026exhaustive` | 54 | 0 | 10 / 0 | 1 / 0 | 5 / 0 | 0 Zitierende (2026) |
| Q611 `senousy2026automated` | 70 | 0 | 20 / 0 | 4 / 0 | 5 / 0 | 0 Zitierende (2026) |
| Q621 `urban2026development` | 32 | 0 | 9 / 0 | 2 / 0 | 3 / 0 | 0 Zitierende (2026) |
| Q623 `vestin2022information` | 41 | 3 | 15 / 1 | 2 / 0 | 7 / 1 | vollständig |
| Q626 `wu2025design` | 66 | 9 | 12 / 2 | 0 / 1 | 8 / 1 | vollständig |
| Q628 `yin2019building` | 197 | 421 | 17 / 25 | 6 / 4 | 4 / 10 | vorwärts vollständig (421, drei Seiten); rückwärts 197 von 247 in OpenAlex auflösbar |
| Q630 `zentgraf2023concept` | 14 | 1 | 3 / 0 | 0 / 0 | 0 / 0 | vollständig |
| Q634 `zhang2023rule` | 77 | 11 | 12 / 5 | 0 / 0 | 0 / 1 | vollständig |
| Q644 `gregor1999explanations` | 120 | 174 | 7 / 9 | 0 / 0 | 5 / 5 | vorwärts gefiltert: 174 von 537 (Volltextfilter „building OR construction OR architectural OR configurator OR compliance OR BIM“) |
| Q655 `park2026bimllm` | 67 | 1 | 21 / 1 | 2 / 0 | 8 / 0 | vollständig |
| Q660 `wang2022natural` | 47 | 35 | 16 / 5 | 6 / 2 | 4 / 2 | vollständig |
| Q662 `wu2026alterations` | 17 | 0 | 6 / 0 | 0 / 0 | 2 / 0 | 0 Zitierende (2026) |
| Q669 `campogay2026quality` | 55 | 0 | 7 / 0 | 2 / 0 | 2 / 0 | 0 Zitierende (2026) |
| Q682 `grenzfurtner2026failure` | 41 | 0 | 9 / 0 | 2 / 0 | 3 / 0 | 0 Zitierende (2026) |
| Q703 `love2022rework` | 85 | 47 | 11 / 2 | 4 / 0 | 6 / 1 | vollständig |
| Q716 `sonnenberg2012patterns` | 20 | 143 | 3 / 0 | 0 / 0 | 2 / 0 | vorwärts vollständig (143), fast nur Wirtschaftsinformatik ohne Baubezug |
| Q721 `trentin2011overcoming` | 88 | 59 | 8 / 6 | 0 / 0 | 4 / 3 | vollständig |
| Q724 `virzi1992subjects` | 11 | 200 | 1 / 4 | 0 / 0 | 1 / 2 | vorwärts gefiltert: 200 von 328 Treffern (Filter „building OR housing OR BIM OR architectural OR configurator OR construction“) über 1 230 Zitierende |
| Q726 `vonhippel2001user` | 33 | 149 | 5 / 8 | 1 / 0 | 2 / 5 | vorwärts gefiltert: 149 von 521 (Filter „house OR housing OR building OR construction OR configurator OR architecture“) |
| Q732 `abualdenien2020consistent` | 42 | 33 | 6 / 2 | 1 / 1 | 1 / 0 | vollständig |
| Q735 `ahn2013roofs` | 17 | 6 | 4 / 1 | 1 / 0 | 2 / 0 | vollständig |
| Q736 `aichholzer1996general` | 13 | 172 | 0 / 8 | 0 / 1 | 0 / 1 | vorwärts vollständig (172) |
| Q743 `basner2010guidance` | 37 | 50 | 0 / 0 | 0 / 0 | 0 / 0 | Referenzen und Zitierende fast nur Schlaf-/Lärmmedizin ohne Entwurfsbezug |
| Q744 `biedl2015weighted` | 18 | 48 | 4 / 2 | 0 / 1 | 2 / 0 | vollständig |
| Q747 `bodin2015quiet` | 31 | 123 | 3 / 4 | 0 / 0 | 1 / 4 | vollständig |
| Q749 `brown2020melanopic` | 56 | 184 | 0 / 9 | 0 / 0 | 0 / 7 | vorwärts gefiltert: 184 von 251 (Filter „residential OR dwelling OR home OR housing OR architectural OR daylight OR building“) |
| Q750 `cain2020evening` | 43 | 77 | 0 / 2 | 0 / 0 | 0 / 1 | vorwärts gefiltert: 77 von 119 (Filter wie Q749) |
| Q751 `cajochen2022evening` | 66 | 39 | 0 / 2 | 0 / 0 | 0 / 2 | vollständig |
| Q752 `chateauvieuxhellwig2022timber` | 37 | 3 | 8 / 1 | 1 / 0 | 4 / 0 | vollständig |
| Q753 `chateauvieuxhellwig2025schallschutz` | 6 | 0 | 0 / 0 | 0 / 0 | 0 / 0 | Kalenderbeitrag, 6 Referenzen, 0 Zitierende |
| Q761 `dosen2013methodological` | 31 | 24 | 4 / 5 | 1 / 2 | 2 / 1 | vollständig |
| Q764 `eder2018volume` | 7 | 0 | 2 / 0 | 0 / 0 | 0 / 0 | 0 Zitierende |
| Q765 `eder2021exact` | 22 | 6 | 1 / 1 | 0 / 0 | 0 / 0 | vollständig |
| Q766 `emmitt2023bedroom` | 41 | 13 | 7 / 1 | 0 / 0 | 7 / 1 | vollständig |
| Q772 `held2017roofs` | 25 | 32 | 4 / 3 | 1 / 0 | 1 / 1 | vollständig |
| Q783 `locher2018windows` | 28 | 87 | 5 / 5 | 0 / 0 | 2 / 4 | vollständig |
| Q791 `ohrstrom2006quietness` | 23 | 145 | 0 / 7 | 0 / 0 | 0 / 3 | vorwärts gefiltert: 145 von 345 (Filter „dwelling OR facade OR bedroom OR floor plan OR layout OR building design“) |
| Q797 `potter2025sleep` | 202 | 0 | 3 / 0 | 0 / 0 | 1 / 0 | rückwärts 202 (zwei Seiten) |
| Q800 `spitschan2021luox` | 72 | 20 | 3 / 0 | 0 / 0 | 2 / 0 | vollständig |
| Q808 `wiener2007isovist` | 47 | 83 | 6 / 4 | 3 / 0 | 1 / 2 | vollständig |
| Q811 `zhao2025mep` | 124 | 2 | 6 / 0 | 0 / 0 | 5 / 0 | vollständig |
**Ertrag je Cluster** (gesichtet und aufgenommen; eine Quelle kann mehreren Clustern zugeordnet sein):

| Cluster | Startquellen | gesichtet | Bestand unter Kandidaten | aufgenommen (eindeutig) | Quote | Relevanz 3 |
|---|---|---|---|---|---|---|
| Regelprüfung/Bauantrag (FF2/FF4) | 12 | 722 | 28 | 48 | 6,6 % | – |
| Sprache/Konfiguration (FF3) | 3 | 167 | 10 | 16 | 9,6 % | `wei2025texttostructure` |
| Vorfertigung/Informationsmodell (FF1) | 2 | 662 | 12 | 21 | 3,2 % | `an2020bimbased`, `zhang2022bimbased` |
| Wirkung/Evaluation/Erklärung (FF5) | 8 | 1 225 | 9 | 39 | 3,2 % | – |
| TGA (FF6) | 1 | 126 | 0 | 5 | 4,0 % | – |
| Licht/Schlaf/Raumwahrnehmung (FF6) | 8 | 998 | 6 | 23 | 2,3 % | – |
| Schall/Lärm (FF6) | 6 | 570 | 1 | 13 | 2,3 % | – |
| Reifegrade/Dachgeometrie (FF6) | 7 | 441 | 6 | 5 | 1,1 % | – |

**Kurzbefund je Cluster:**

- **Regelprüfung/Bauantrag (FF2/FF4):** Ergiebig ist vor allem die Vorwärtssuche zu `bloch2023unbalanced`: 10 von 30 Zitierenden sind aufgenommen, darunter die deutschen Erhebungen, PACE-BP und Inspektionen.
  - Rückwärts bei den großen Reviews (`lee2026automated`, `senousy2026automated`, `zhang2023rule`) ist das Feld nahezu gesättigt. Die Referenzlisten bestehen zu großen Teilen aus Bestandsquellen oder generischer NLP-Regelextraktion (Relevanz 1).
  - Neu tragfähig sind:
    - OntoBPR (Bauantragsprüfung mit Informationscontainern)
    - Rules as Code
    - BRISE-Plandok (deutschsprachiges Regelkorpus Wien)
    - die IDS-Vorgeschichte (`vanberlo2019creating`)
    - LOIN und IDS integriert (`akbas2025holistic`)
    - Lösungsraum- und Constraint-Grundlagen aus dem Umfeld von `niemeijer2014freedom` (`lottaz1998constraint`, `gelle2003solving`, `zimmermann2013computing`)
- **Sprache (FF3):** `park2026bimllm` hat eine Referenzliste, aus der 8 von 67 Datensätzen aufgenommen sind. Sie erschließt die Linie „natürliche Sprache → strukturierte Zwischenform → deterministische Ausführung“, die im Bestand dünn war.
- **Vorfertigung (FF1):**
  - Rückwärts bei `vestin2022information` kommt die schwedische Plattformforschung zu Holz-Einfamilienhäusern (Jönköping, Luleå, Lund) hinzu.
  - Vorwärts bei `yin2019building` (421 Zitierende) liegt die Quote nur bei 2,4 %. Die Funde konzentrieren sich auf die Alberta-Linie (Fertigbarkeitsprüfung, Entwässerung im Tafelbau) und Design-to-Manufacturing.
- **Wirkung (FF5):**
  - Die Nacharbeits-Literatur (`love2022rework`) liefert vor allem Messmethoden (`fayek2004developing`, `davis1989measuring`, `love2026quantifying`).
  - Die Konfigurator-Literatur liefert Wirkungsbelege (XCON, `salvador2014product`, `bredahlrasmussen2021costs`).
  - Die Erklärungsforschung (Gregor-Umfeld) liefert Evaluationsrahmen.
  - Viele Kandidaten sind nur Wiederholungen von Bestandsargumenten.
- **FF6:**
  - Die Dachgeometrie ist weitgehend gesättigt (5 Aufnahmen aus 441 Datensätzen). Neu sind nur Implementierung (Bone) und Dacherzeugung aus Grundrissen.
  - Schall/Lärm und Licht liefern wohnbezogene Einzelstudien (ruhige Seite, Schlafzimmerfenster, Fassadendämmung, melanopische Metrik), aber keinen neuen Baustein mit Relevanz 3.
  - Die Referenzliste der TGA-Übersicht `zhao2025mep` bringt Modularisierung von Sanitär- und TGA-Systemen.

## 4 PRISMA-Zahlen Runde 2 im Vergleich zu Runde 1

| Schritt | Runde 1 Teil A (FF1/2/4) | Runde 1 Teil B (FF3/5/6) | Runde 1 gesamt | **Runde 2 (FF1–FF6)** |
|---|---|---|---|---|
| Startquellen | 23 | 38 | 61 (56 verschiedene) | **47** |
| Datensätze gesichtet (roh, rundenintern nicht bereinigt) | 2 800 | 3 637 | 6 437 | **4 911** (r 2 385, v 2 526) |
| Titel-Screening nach Bereinigung | 2 291 | – | – | – (nicht maschinell bereinigt) |
| Kandidaten zur Abstract-Prüfung | 211 | 257 | 468 | **411** |
| davon Dubletten zum Bestand | 99 (auf Listenebene) | 42 | – | **72** (17,5 % der Kandidaten) |
| neue Kandidaten | 211 | 212 | 423 | **339** (323 mit DOI, 16 ohne) |
| ausgeschlossen | 100 | 37 | 137 | **177** |
| davon Relevanz < 2 bzw. andere FF | 83 | 26 | 109 | 102 |
| davon redundant | – | 10 | 10 | 49 |
| davon Vorfassung/Tagungsfassung | 4 | 1 | 5 | 10 |
| davon nicht verifizierbar/ohne Abstract | 4 | – | 4 | 9 |
| davon Preprint | 8 | – | 8 | 4 |
| davon Hochschulschrift | 1 | – | 1 | 3 |
| **aufgenommen (Relevanz ≥ 2, verifiziert)** | 111 | 175 | 286 | **162** |
| davon Relevanz 3 | 10 | 19 | 29 (10,1 %) | **3 (1,9 %)** |
| **Aufnahmequote aufgenommen / gesichtet (roh)** | 4,0 % | 4,8 % | **4,4 %** | **3,3 %** |
| Aufnahmequote auf bereinigter Basis (nur Teil A verfügbar) | 4,8 % | – | – | – |
| Trefferquote aufgenommen / Kandidaten (einschließlich Bestand) | – | 68,1 % | – | **39,4 %** |
| Trefferquote aufgenommen / neue Kandidaten | 52,6 % | 82,5 % | 67,6 % | **47,8 %** |

**Schwerpunkt der 162 Aufnahmen:**
- nach Haupt-FF: FF1 12, FF2 37, FF3 13, FF4 20, FF5 33, FF6 47
- mit Relevanz ≥ 2 je FF: FF1 21, FF2 40, FF3 15, FF4 20, FF5 39, FF6 50

**Zur Vergleichbarkeit:**
- **Zählweise:** Runde 1 hat Teil A nach rundeninterner Bereinigung gezählt (2 291), Teil B roh (3 637). Runde 2 ist roh gezählt. Der faire Vergleich ist deshalb roh gegen roh: 4,4 % gegen 3,3 %.
- **Gefilterte Vorwärtssuche:** Sechs Startquellen wurden in Runde 2 gefiltert statt vollständig gesichtet. Das erhöht die Quote von Runde 2 eher, weil Filter den Anteil einschlägiger Titel steigern. Der Rückgang ist deshalb eher unterschätzt.

## 5 Aufgenommene Quellen

Einteilung nach Haupt-FF (höchste Relevanz; bei Gleichstand FF4 vor FF2 vor FF1 vor FF3 vor FF5 vor FF6). Jede Quelle erscheint einmal. Relevanz 3 ist **fett** markiert.

Die Werte ff1–ff6 sind vorläufig: Einzelbewertung nach Titel und Abstract, kein Volltext. Vor der Übernahme in `quellen-bewertung.csv` müssen `qualitaet`, `uebertragbarkeit` und P ergänzt werden. „Schneeball von“: Startquelle(n) mit Richtung.

#### FF4 – Verantwortung, Freigabe, Bauantrag (20)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `brkan2020legal` | 2020 | Legal and Technical Feasibility of the GDPR’s Quest for Explanation of Algorithmic Decisions: of Black Boxes, White Boxes and Fata Morganas | European Journal of Risk Regulation | gregor1999explanations (vorwärts) | 0/0/0/2/0/0 | DSGVO-Anforderungen an Erklärungen automatisierter Entscheidungen |
| `ciotta2021structural` | 2021 | Structural E-Permits: an OpenBIM, Model-Based Procedure for Permit Applications Pertaining to Structural Engineering | Journal of Civil Engineering and Management | bloch2023unbalanced (rückwärts) | 1/0/0/2/0/0 | IFC-basierte Einreichung statischer Nachweise bei Behörden (Structural e-permits) |
| `debruijn2022perils` | 2022 | The perils and pitfalls of explainable AI: Strategies for explaining algorithmic decision-making | Government Information Quarterly | gregor1999explanations (vorwärts) | 0/0/0/2/0/0 | Fallstricke erklärbarer KI in der Verwaltung |
| `esser2022graphbased` | 2022 | Graph-based version control for asynchronous BIM collaboration | Advanced Engineering Informatics | wu2025design (rückwärts) | 2/0/0/2/0/0 | graphbasierte Versionierung von BIM-Ständen (TUM): Änderungsnachweis zwischen Freigaben |
| `fauth2022conceptual` | 2022 | Conceptual Framework for Building Permit Process Modeling: Lessons Learned from a Comparison between Germany and the United States regarding the As-Is Building Permit Processes | Buildings | bloch2023unbalanced (rückwärts) | 0/0/0/2/0/0 | Prozessmodell Baugenehmigung Deutschland vs. USA: Schritte, Rollen, Zuständigkeiten |
| `fauth2023process` | 2023 | Process model for international building permit benchmarking and a validation example using the Israeli building permit process | Engineering, Construction and Architectural Management | bloch2023unbalanced (vorwärts) | 0/0/0/2/0/0 | Prozessmodell internationaler Baugenehmigungs-Benchmarks (Israel) |
| `fauth2023requirements` | 2023 | Requirements and framework for Gaia-x-based building permit processes | Computing in Construction | narayanaswamy2019bim (vorwärts) | 1/0/0/2/0/0 | Gaia-X-basierte Bauantragsprozesse (Datenraum) |
| `fauth2024pace` | 2024 | PACE–BP: Process Analysis and Comparative Evaluation of Building Permit Processes in a Global Perspective | Journal of Management in Engineering | bloch2023unbalanced (vorwärts) | 0/0/0/2/0/0 | PACE-BP: Vergleich von Genehmigungsprozessen weltweit |
| `fauth2025baugenehmigungsv` | 2025 | Das Baugenehmigungsverfahren und dessen Digitalisierung: eine Bestandserhebung | Bautechnik | bloch2023unbalanced (vorwärts) | 0/0/0/2/2/0 | Umfrage mit 649 Teilnehmern zu Aufwand und Digitalisierung der Baugenehmigung in Deutschland |
| `hagedorn2025ontobpr` | 2025 | OntoBPR: An ontology-based framework for performing building permit reviews using standardized information containers | Advanced Engineering Informatics | lee2026automated, pinto2026exhaustive, senousy2026automated (rückwärts); bloch2023unbalanced, nuyts2024comparative (vorwärts) | 0/2/0/2/0/0 | OntoBPR: Ontologie für Bauantragsprüfung mit Informationscontainern (ICDD) |
| `hartmann2026status` | 2026 | The status of digital and BIM-based building permitting in Germany: evidence from a nationwide survey of building authorities | International Journal of Construction Management | bloch2023unbalanced (vorwärts) | 1/0/0/2/0/0 | bundesweite Umfrage Bauaufsichten: Stand digitaler und BIM-basierter Bauantrag in Deutschland |
| `krischmann2020entwicklung` | 2020 | Entwicklung eines openBIM-Bewilligungsverfahrens/Development of an openBIM submission process | Bauingenieur | bloch2023unbalanced (rückwärts) | 0/2/0/2/0/0 | openBIM-Bewilligungsverfahren Wien (BRISE), deutschsprachig |
| `langer2021want` | 2021 | What do we want from Explainable Artificial Intelligence (XAI)? – A stakeholder perspective on XAI and a conceptual model guiding interdisciplinary XAI research | Artificial Intelligence | gregor1999explanations (vorwärts) | 0/0/0/2/1/0 | Stakeholder-Perspektive auf erklärbare KI |
| `liu2025coordination` | 2025 | Coordination mechanisms in digital building permitting: unravelling the dynamic tension between collaboration and complexity | Building Research & Information | bloch2023unbalanced, fischer2024extending (vorwärts) | 0/0/0/2/0/0 | Koordinationsmechanismen im digitalen Bauantrag |
| `meijer2006deregulation` | 2006 | Deregulation and Privatisation of European Building-Control Systems? | Environment and Planning B: Planning and Design | bloch2023unbalanced (rückwärts) | 0/0/0/2/0/0 | Deregulierung und Privatisierung der Bauaufsicht in Europa: Einordnung Prüfsachverständige/Freistellung |
| `meijer2017quality` | 2017 | Quality control of constructions: European trends and developments | International Journal of Law in the Built Environment | bloch2023unbalanced (rückwärts) | 0/0/0/2/0/0 | Qualitätskontrolle/Bauaufsicht in sieben EU-Ländern: private Prüfung, Haftung |
| `messaoudi2020virtual` | 2020 | Virtual Permitting Framework for Off-site Construction Case Study: A Case Study of the State of Florida | Lecture Notes in Civil Engineering | bloch2023unbalanced (rückwärts) | 0/0/0/2/0/0 | Genehmigungsrahmen für Vorfertigung (Florida): Zulassung werkseitig gefertigter Bauteile |
| `sei2025understanding` | 2025 | Understanding and conceptualizing inspections in the context of building permits | Smart and Sustainable Built Environment | bloch2023unbalanced (vorwärts) | 0/0/0/2/0/0 | Inspektionen im Baugenehmigungskontext: Bauüberwachung und Abnahmen |
| `urban2025augmented` | 2025 | Augmented reality supported hearings: a case study on the openBIM-based building permit process in Vienna, Austria | Building Research & Information | urban2026development (rückwärts); bloch2023unbalanced (vorwärts) | 0/0/0/2/0/0 | AR-gestützte Bauverhandlung im openBIM-Verfahren Wien (Beteiligung) |
| `weinkauf2024decision` | 2024 | Decision Support for Building Permit Application Preparation | Proceedings of the 17th International Conference on Theory and Practice of Electronic Governance | bloch2023unbalanced (vorwärts) | 0/2/0/2/0/0 | Entscheidungsunterstützung für Antragsteller bei der Bauantragsvorbereitung |

#### FF1 – Informationsmodell, Vorfertigung, Ableitungen (12)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `anane2023bimdriven` | 2023 | BIM-driven computational design for robotic manufacturing in off-site construction: an integrated Design-to-Manufacturing (DtM) approach | Automation in Construction | yin2019building (vorwärts) | 2/0/0/0/0/0 | Design-to-Manufacturing: BIM steuert robotische Fertigung in der Vorfertigung |
| `eriksson2019assessing` | 2019 | Assessing Digital Information Management Between Design and Production in Industrialised House-Building  A Case Study | Proceedings of the International Symposium on Automation and Robotics in Construction (IAARC) | vestin2022information (rückwärts) | 2/0/0/0/0/0 | digitales Informationsmanagement zwischen Entwurf und Produktion im industriellen Hausbau |
| `gbadamosi2020big` | 2020 | Big data for Design Options Repository: Towards a DFMA approach for offsite construction | Automation in Construction | yin2019building (vorwärts) | 2/1/0/0/0/0 | Varianten-Repository für DfMA in der Vorfertigung |
| `lachance2022automated` | 2022 | Automated and robotized processes in the timber-frame prefabrication construction industry: A state of the art | 2022 IEEE 6th International Conference on Logistics Operations Management (GOL) | yin2019building (vorwärts) | 2/0/0/0/0/0 | Stand der Automatisierung/Robotik in der Holzrahmen-Vorfertigung |
| `lennartsson2020framework` | 2020 | Framework for Digital Development in Industrialized Housebuilding | Advances in Transdisciplinary Engineering | vestin2022information (rückwärts) | 2/0/0/0/0/0 | Rahmen für digitale Entwicklung im industriellen Hausbau |
| `liu2017optimizing` | 2017 | Optimizing Multi-Wall Panel Configuration for Panelized Construction Using BIM | Proceedings of International Structural Engineering and Construction | yin2019building (rückwärts) | 2/0/0/0/0/0 | Optimierung der Wandtafel-Konfiguration im Tafelbau (BIM) |
| `mattern2018bimbased` | 2018 | BIM-based modeling and management of design options at early planning phases | Advanced Engineering Informatics | abualdenien2020consistent, wu2025design, wu2026alterations (rückwärts) | 2/0/0/0/0/0 | Management von Entwurfsvarianten in frühen Phasen im BIM |
| `mellenthinfilardo2023automated` | 2023 | Automated supplement of information requirements for tendering data | Computing in Construction | fischer2024extending (rückwärts) | 2/0/0/0/0/0 | deutsche Ausschreibungs-/Abrechnungsdaten automatisch aus Informationsanforderungen am Modell |
| `sacks2004parametric` | 2004 | Parametric 3D modeling in building construction with examples from precast concrete | Automation in Construction | wu2025design, yin2019building (rückwärts) | 2/0/0/0/0/0 | parametrische 3D-Modellierung in der Fertigteilindustrie |
| `vestin2020smart` | 2020 | Smart factories for single-family wooden houses – a practitioner’s perspective | Construction Innovation | vestin2022information (rückwärts) | 2/0/0/0/1/0 | Smart Factories für Holz-Einfamilienhäuser aus Praxissicht |
| `vestin2023mitigating` | 2023 | Mitigating product data management challenges in the wooden single-family house industry | Journal of Information Technology in Construction | vestin2022information, yin2019building (vorwärts) | 2/0/0/0/0/1 | Produktdatenmanagement Holz-EFH-Industrie: Anforderungen an ein Unterstützungssystem |
| `wu2025enhancing` | 2025 | Enhancing IFC models with reference grids by re-engineering building component placement logic | Automation in Construction | wu2025design (vorwärts) | 2/0/0/0/0/0 | Referenzraster und Platzierungslogik in IFC übertragen |

#### FF2 – Regelraum, Regelprüfung, Konfiguration (37)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| **`an2020bimbased`** | 2020 | BIM-based decision support system for automated manufacturability check of wood frame assemblies | Automation in Construction | yin2019building (vorwärts) | 2/3/0/0/0/0 | automatische Fertigbarkeitsprüfung von Holzrahmen-Baugruppen im BIM (Alberta) |
| `akbas2025holistic` | 2025 | A holistic approach to information requirements: Integration of level of information need and information delivery specification | Journal of Information Technology in Construction | fischer2024extending (vorwärts) | 2/2/0/0/0/2 | LOIN und IDS integriert: Informationsbedarf je Reifegrad |
| `andre2019exploring` | 2019 | Exploring the Design Platform in Industrialized Housing for Efficient Design and Production of Customized Houses | Advances in Transdisciplinary Engineering | vestin2022information (rückwärts) | 2/2/0/0/0/0 | Designplattform im industriellen Hausbau für kundenindividuelle Häuser |
| `banihashemi2018integration` | 2018 | Integration of parametric design into modular coordination: A construction waste reduction workflow | Automation in Construction | zhao2025mep (rückwärts) | 1/2/0/0/0/0 | parametrisches Entwerfen in modularer Maßordnung (Abfallreduktion) |
| `clancey1983epistemology` | 1983 | The epistemology of a rule-based expert system —a framework for explanation | Artificial Intelligence | gregor1999explanations (rückwärts) | 0/2/0/0/0/0 | Erklärungsstruktur regelbasierter Systeme (Clancey) |
| `daum2014processing` | 2014 | Processing of Topological BIM Queries using Boundary Representation Based Methods | Advanced Engineering Informatics | chateauvieuxhellwig2022timber, nuyts2024comparative (rückwärts) | 0/2/0/0/0/0 | topologische BIM-Abfragen (B-Rep) für Regelprüfung (TUM) |
| `felfernig2007standardized` | 2007 | Standardized Configuration Knowledge Representations as Technological Foundation for Mass Customization | IEEE Transactions on Engineering Management | trentin2011overcoming (rückwärts) | 0/2/0/0/0/0 | standardisierte Repräsentation von Konfigurationswissen |
| `fischer2023automation` | 2023 | Automation of escape route analysis for BIM-based building code checking | Automation in Construction | fischer2024extending, lee2026automated (rückwärts) | 0/2/0/0/0/0 | BIM-basierte Fluchtwegprüfung für Bauaufsichten |
| `gao2025lifecycle` | 2025 | Lifecycle framework for AI-driven parametric generative design in industrialized construction | Automation in Construction | park2026bimllm (rückwärts) | 0/2/0/0/0/0 | LLM/KGQA erfasst Anforderungen; dreistufige Priorität zur Konfliktauflösung (TUM) |
| `gelle2003solving` | 2003 | Solving Mixed and Conditional Constraint Satisfaction Problems | Constraints | niemeijer2014freedom (rückwärts) | 0/2/0/0/0/0 | bedingte/gemischte CSP: Optionen, die weitere Constraints aktivieren (Konfigurator) |
| `ghannad2019automated` | 2019 | Automated BIM data validation integrating open-standard schema with visual programming language | Advanced Engineering Informatics | fischer2024extending (rückwärts) | 1/2/0/0/0/0 | Validierung von BIM-Daten gegen offene Schemata per visueller Programmierung; Vorstufe der IDS-Prüfung |
| `hjelseth2015public` | 2015 | Public BIM-based model checking solutions: lessons learned from Singapore and Norway | WIT Transactions on The Built Environment | nuyts2024comparative, urban2026development (rückwärts) | 0/2/0/1/0/0 | öffentliche Model-Checking-Lösungen Singapur/Norwegen: Gründe des Scheiterns |
| `ilal2022integrating` | 2022 | Integrating building and context information for automated zoning code checking: a review | Journal of Information Technology in Construction | bloch2023unbalanced (rückwärts) | 0/2/0/0/0/0 | Review Prüfung gegen Bebauungsplan/Zoning mit Kontextinformation (BIM+GIS) |
| `johnsson2007ict` | 2007 | ICT Support for Industrial Production of Houses – The Swedish Case | Proceedings of the 24th CIB W78 Conference | vestin2022information (rückwärts) | 2/2/0/0/0/0 | vier Sichten; Fertigungsregeln begrenzen die Kundensicht (CIB W78 2007) |
| `kruiper2024platformbased` | 2024 | A platform-based Natural Language processing-driven strategy for digitalising regulatory compliance processes for the built environment | Advanced Engineering Informatics | lee2026automated, senousy2026automated (rückwärts); bloch2023unbalanced, niemeijer2014freedom, zhang2023rule (vorwärts) | 0/2/0/1/0/0 | Plattformstrategie zur Digitalisierung regulatorischer Compliance nach Grenfell (UK) |
| `lee2006specifying` | 2006 | Specifying parametric building object behavior (BOB) for a building information modeling system | Automation in Construction | wu2025design, yin2019building (rückwärts) | 2/2/0/0/0/0 | parametrisches Bauteilverhalten (BOB): Regeln im Objekt |
| `lee2019efficient` | 2019 | An Efficient Design Support System based on Automatic Rule Checking and Case-based Reasoning | KSCE Journal of Civil Engineering | wu2025design, wu2026alterations (rückwärts) | 0/2/0/0/0/0 | Regelprüfung plus fallbasierte Alternativen im Entwurf |
| `lennartsson2021plm` | 2021 | PLM support for design platforms in industrialized house-building | Construction Innovation | vestin2022information (rückwärts) | 2/2/0/0/0/0 | PLM für Designplattformen im industriellen Hausbau |
| `lottaz1998constraint` | 1998 | Constraint solving and preference activation for interactive 
design | Artificial Intelligence for Engineering Design, Analysis and Manufacturing | niemeijer2014freedom (rückwärts) | 0/2/0/0/0/0 | Constraint-Löser für vollständige Lösungsräume im interaktiven Entwurf |
| `luo2024ontologybased` | 2024 | Ontology-Based Design Features for Representing Constructability in Architectural Design: Toward BIM in Off-Site Construction | Journal of Construction Engineering and Management | yin2019building (vorwärts) | 2/2/0/0/0/0 | ontologiebasierte Konstruierbarkeitsmerkmale im Architekturentwurf für Vorfertigung |
| `malmgren2010customization` | 2010 | Customization of Buildings Using Configuration Systems – A Study of Conditions and Opportunities in the Swedish Timber House Manufacturing Industry | Lund University (Lizentiatsarbeit TVBK-1041) | vestin2022information (rückwärts) | 0/2/0/0/2/0 | Konfiguration im schwedischen Holzfertighausbau (Lizentiatsarbeit Lund) |
| `mcdermott1982rulebased` | 1982 | R1: A rule-based configurer of computer systems | Artificial Intelligence | wang2022natural (rückwärts) | 0/2/0/0/0/0 | R1/XCON: regelbasierter Konfigurator als Referenz |
| `mowbray2023representing` | 2023 | Representing legislative Rules as Code: Reducing the problems of ‘scaling up’ | Computer Law & Security Review | nuyts2024comparative (rückwärts) | 0/2/0/1/0/0 | Rules as Code: Rechtsnormen als ausführbaren Code skalieren (Rechtsinformatik) |
| `olsson2018automation` | 2018 | Automation of Building Permission by Integration of BIM and Geospatial Data | ISPRS International Journal of Geo-Information | bloch2023unbalanced, urban2026development (rückwärts) | 0/2/0/1/0/0 | Prototyp: Prüfung von BIM plus Geodaten gegen Bebauungsplan-Festsetzungen (Schweden) |
| `rasmussen2020guidelines` | 2020 | Guidelines for Structuring Object-Oriented Product Configuration Models in Standard Configuration Software | JUCS - Journal of Universal Computer Science | wang2022natural (rückwärts) | 0/2/0/0/0/0 | Leitlinien zur Strukturierung objektorientierter Konfigurationsmodelle |
| `recski2024briseplandok` | 2024 | BRISE-plandok: a German legal corpus of building regulations | Language Resources and Evaluation | senousy2026automated (rückwärts) | 0/2/2/0/0/0 | BRISE-Plandok: deutschsprachiges Korpus Bebauungsplan Wien mit formalen Regeln |
| `singh2017integrating` | 2017 | Integrating rules of modular coordination to improve model authoring in BIM | International Journal of Construction Management | yin2019building (rückwärts) | 0/2/0/0/0/0 | Regeln der Maßordnung als Skripte im BIM-Authoring |
| `soininen1998general` | 1998 | Towards a general ontology of configuration | Artificial Intelligence for Engineering Design, Analysis and Manufacturing | trentin2011overcoming (rückwärts) | 0/2/0/0/0/0 | allgemeine Ontologie der Produktkonfiguration |
| `solimanjunior2022designers` | 2022 | Designers’ perspective on the use of automation to support regulatory compliance in healthcare building projects | Construction Management and Economics | wu2025design (rückwärts) | 0/2/0/0/1/0 | Sicht der Planer auf automatisierte Regelprüfung (Interviews) |
| `vanberlo2019creating` | 2019 | Creating Information Delivery Specifications Using Linked Data | Proceedings of the 36th CIB W78 Conference | fischer2024extending (rückwärts) | 0/2/0/0/0/0 | IDS-Entstehung über Linked Data (CIB W78 2019) |
| `xie2005modelling` | 2005 | Modelling and solving engineering product configuration problems by constraint satisfaction | International Journal of Production Research | trentin2011overcoming, wang2022natural (rückwärts) | 0/2/0/0/0/0 | Produktkonfiguration als Constraint-Satisfaction modelliert und gelöst |
| `yang2012constraint` | 2012 | A constraint satisfaction approach to resolving product configuration conflicts | Advanced Engineering Informatics | trentin2011overcoming (vorwärts) | 0/2/0/0/0/0 | Auflösung von Konfigurationskonflikten mit Constraint-Methoden |
| `yang2024promptbased` | 2024 | Prompt-based automation of building code information transformation for compliance checking | Automation in Construction | lee2026automated, pinto2026exhaustive, senousy2026automated, wu2025design (rückwärts) | 0/2/0/0/0/0 | LLM übersetzt Bauvorschriften in Logikprogramme (IBC-Test); Abgrenzung KI/Regelmaschine |
| `yang2026llmpowered` | 2026 | LLM-Powered Structurer: Normalizing Natural Language to Information Delivery Specification for Industrial Data Exchange | Companion Proceedings of the ACM Web Conference 2026 | fischer2024extending (vorwärts) | 0/2/2/0/0/0 | LLM normalisiert natürliche Sprache in IDS |
| `ye1995impact` | 1995 | The Impact of Explanation Facilities on User Acceptance of Expert Systems Advice | MIS Quarterly | gregor1999explanations (rückwärts) | 0/2/0/0/2/0 | Wirkung von Erklärungskomponenten auf Akzeptanz von Expertensystem-Empfehlungen |
| `zech2024bimreason` | 2024 | BIMReason: Validating BIM model correctness | Bauphysik | senousy2026automated (rückwärts) | 0/2/0/0/0/0 | BIMReason: Regel-/Reasoning-Prüfung der Modellkorrektheit (Bauphysik) |
| `zimmermann2013computing` | 2013 | Computing solution spaces for robust design | International Journal for Numerical Methods in Engineering | wu2025design (rückwärts) | 0/2/0/0/0/0 | Lösungsräume für robustes Design: Regelraum als zulässiger Parameterraum |

#### FF3 – Sprachschnittstelle (13)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| **`wei2025texttostructure`** | 2025 | Text-to-structure interpretation of user requests in BIM interaction | Automation in Construction | park2026bimllm (rückwärts) | 0/0/3/0/0/0 | T2S4BIM (TUM): Nutzeranfragen in Intent und Slots, dann Revit-Aktion |
| `bagasi2025bim` | 2025 | BIM and AI in Early Design Stage: Advancing Architect–Client Communication | Buildings | park2026bimllm (rückwärts) | 0/0/2/0/1/0 | BIM+KI in der Architekt-Bauherr-Kommunikation früher Phasen |
| `dahlem2026comparing` | 2026 | Comparing Drag-and-Drop and Conversational Interfaces for Digital Psychometric Assessment Design: A Mixed-Methods Usability Study | Lecture Notes in Computer Science | virzi1992subjects (vorwärts) | 0/0/2/0/2/0 | Drag-and-Drop vs. Konversation: Usability-Vergleich für Entwurfsaufgaben |
| `dong2025bim` | 2025 | AI BIM coordinator for non-expert interaction in building design using LLM-driven multi-agent systems | Automation in Construction | park2026bimllm (rückwärts) | 0/0/2/0/0/0 | LLM-Multiagenten ermöglichen Nicht-Experten BIM-Operationen, Prüfagent sichert Code |
| `dudek2023mass` | 2023 | Towards mass customisation: automatic processing of orders for residential ship’s containers - A case study example | Bulletin of the Polish Academy of Sciences Technical Sciences | wang2022natural (vorwärts) | 0/1/2/0/1/0 | Spracherkennung und Schlüsselbegriffe wählen Varianten vorgefertigter Container-Häuser |
| `feng2026bridging` | 2026 | Bridging the Semantic Gap in BIM Interior Design: A Neuro-Symbolic Framework for Explainable Scene Completion | Applied Sciences | fischer2024extending, nuyts2024comparative (vorwärts) | 0/0/2/0/0/2 | neurosymbolische Innenraumvervollständigung mit expliziten Constraints |
| `guo2025advancing` | 2025 | Advancing BIM information retrieval with an LLM-based query-domain-specific language and library code function alignment system | Automation in Construction | park2026bimllm (rückwärts) | 0/0/2/0/0/0 | LLM-Abfrage-DSL mit Zuordnung zu Bibliotheksfunktionen |
| `jin2026evaluating` | 2026 | Evaluating large language models (LLMs) for semantic interpretation of IFC-based BIM data | Automation in Construction | park2026bimllm (rückwärts) | 0/0/2/0/0/0 | Evaluation von LLMs beim Verständnis von IFC-Daten |
| `stevens2020customers` | 2020 | Customers’ learning process during product customization: The case of online configuration tool kits | Information & Management | vonhippel2001user (vorwärts) | 0/0/2/0/2/0 | Lernprozess von Kunden in Online-Konfiguratoren |
| `vonhippel1994sticky` | 1994 | “Sticky Information” and the Locus of Problem Solving: Implications for Innovation | Management Science | vonhippel2001user (rückwärts) | 0/0/2/0/2/0 | Sticky Information: warum Problemlösung zum Nutzer verlagert wird |
| `wang2018mapping` | 2018 | Mapping customer needs to design parameters in the front end of product design by applying deep learning | CIRP Annals | wang2022natural (rückwärts) | 0/0/2/0/0/0 | Kundenbedürfnisse auf Designparameter abbilden (Deep Learning) |
| `wang2022transfer` | 2022 | Transfer learning-based query classification for intelligent building information spoken dialogue | Automation in Construction | park2026bimllm (rückwärts) | 0/0/2/0/0/0 | Klassifikation gesprochener Anfragen für BIM-Dialog |
| `yin2023twostage` | 2023 | Two-stage Text-to-BIMQL semantic parsing for building information model extraction using graph neural networks | Automation in Construction | park2026bimllm (rückwärts) | 0/0/2/0/0/0 | zweistufiges Text-zu-BIMQL-Parsing: Sprache in deterministische Abfragesprache |

#### FF5 – Wirkung und Evaluation (33)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `barr2015oracle` | 2015 | The Oracle Problem in Software Testing: A Survey | IEEE Transactions on Software Engineering | pinto2026exhaustive (rückwärts) | 0/1/0/0/2/0 | Testorakel-Problem: wie Korrektheit einer Regelmaschine geprüft wird |
| `bredahlrasmussen2021costs` | 2021 | The costs and benefits of multistage configuration: A framework and case study | Computers & Industrial Engineering | campogay2026quality (rückwärts); trentin2011overcoming (vorwärts) | 0/0/0/0/2/0 | Kosten und Nutzen mehrstufiger Konfiguration (Fallstudie) |
| `burati1992causes` | 1992 | Causes of Quality Deviations in Design and Construction | Journal of Construction Engineering and Management | love2022rework (rückwärts) | 0/0/0/0/2/0 | Ursachen von Qualitätsabweichungen in Planung und Ausführung |
| `campagna2025usercentered` | 2025 | User-Centered Perspectives in Prefabricated Timber Buildings: A Scoping Review | Buildings | yin2019building (vorwärts) | 0/0/0/0/2/2 | Scoping Review: Nutzerperspektive in vorgefertigten Holzgebäuden |
| `davis1989measuring` | 1989 | Measuring Design and Construction Quality Costs | Journal of Construction Engineering and Management | love2022rework (rückwärts) | 0/0/0/0/2/0 | Messung von Qualitätskosten in Planung und Ausführung |
| `davis1989perceived` | 1989 | Perceived Usefulness, Perceived Ease of Use, and User Acceptance of Information Technology | MIS Quarterly | gregor1999explanations (rückwärts) | 0/0/0/0/2/0 | TAM: Messskalen für wahrgenommenen Nutzen und Bedienbarkeit |
| `dhaliwal1996use` | 1996 | The Use and Effects of Knowledge-Based System Explanations: Theoretical Foundations and a Framework for Empirical Evaluation | Information Systems Research | gregor1999explanations (rückwärts) | 0/0/0/0/2/0 | Rahmen zur empirischen Evaluation von Erklärungen wissensbasierter Systeme |
| `fayek2004developing` | 2004 | Developing a standard methodology for measuring and classifying construction field rework | Canadian Journal of Civil Engineering | love2022rework (rückwärts) | 0/0/0/0/2/0 | Standardmethode zur Erfassung und Klassifikation von Nacharbeit |
| `franke2003satisfying` | 2003 | Satisfying heterogeneous user needs via innovation toolkits: the case of Apache security software | Research Policy | vonhippel2001user (rückwärts) | 0/0/0/0/2/0 | Toolkits für heterogene Nutzerbedürfnisse (empirisch) |
| `gann2003design` | 2003 | Design Quality Indicator as a tool for thinking | Building Research & Information | vonhippel2001user (vorwärts) | 0/0/0/0/2/0 | Design Quality Indicator als Werkzeug zur Bewertung der Entwurfsqualität |
| `halman2008modular` | 2008 | Modular Approaches in Dutch House Building: An Exploratory Survey | Housing Studies | niemeijer2014freedom (rückwärts) | 1/0/0/0/2/0 | modulare Ansätze im niederländischen Wohnungsbau mit Kundeneinfluss (Survey) |
| `hopkin2016detecting` | 2016 | Detecting defects in the UK new-build housing sector: a learning perspective | Construction Management and Economics | grenzfurtner2026failure (rückwärts) | 0/0/0/0/2/0 | Mängelerkennung im britischen Neubau (Lernperspektive) |
| `hwang2014investigating` | 2014 | Investigating the client-related rework in building projects: The case of Singapore | International Journal of Project Management | love2022rework (rückwärts) | 0/0/0/0/2/0 | bauherrenbedingte Nacharbeit (Singapur) |
| `jimenezmoreno2021mass` | 2021 | Mass Customisation for Zero-Energy Housing | Sustainability | vonhippel2001user (vorwärts) | 0/0/0/0/2/1 | Mass Customisation japanischer Hausbauer für Nullenergiehäuser |
| `josephson2002illustrative` | 2002 | Illustrative Benchmarking Rework and Rework Costs in Swedish Construction Industry | Journal of Management in Engineering | love2022rework (rückwärts) | 0/0/0/0/2/0 | Kosten von Nacharbeit, Benchmark Schweden |
| `larsen2019mass` | 2019 | Mass Customization in the House Building Industry: Literature Review and Research Directions | Frontiers in Built Environment | grenzfurtner2026failure (rückwärts) | 0/1/0/0/2/0 | Review Mass Customization im Hausbau |
| `lei2023measurement` | 2023 | Measurement of Information Loss and Transfer Impacts of Technology Systems in Offsite Construction Processes | Journal of Construction Engineering and Management | yin2019building (vorwärts) | 1/0/0/0/2/0 | Messung von Informationsverlust in Vorfertigungsprozessen |
| `lewis2018system` | 2018 | The System Usability Scale: Past, Present, and Future | International Journal of Human–Computer Interaction | pinto2026exhaustive (rückwärts) | 0/0/0/0/2/0 | SUS-Übersichtsarbeit: Normwerte und Auswertung |
| `love2011design` | 2011 | Design error reduction: toward the effective utilization of building information modeling | Research in Engineering Design | love2022rework (rückwärts) | 0/0/0/0/2/0 | Reduktion von Planungsfehlern durch BIM |
| `love2026quantifying` | 2026 | Quantifying the Costs of Field Rework in Construction | Journal of Construction Engineering and Management | love2022rework (vorwärts) | 0/0/0/0/2/0 | Quantifizierung der Kosten von Nacharbeit |
| `mohseni2021multidisciplinar` | 2021 | A Multidisciplinary Survey and Framework for Design and Evaluation of Explainable AI Systems | ACM Transactions on Interactive Intelligent Systems | gregor1999explanations (vorwärts) | 0/0/0/0/2/0 | Übersicht und Rahmen zu Entwurf und Evaluation erklärbarer KI |
| `nielsen1990heuristic` | 1990 | Heuristic evaluation of user interfaces | Proceedings of the SIGCHI conference on Human factors in computing systems Empowering people - CHI '90 | virzi1992subjects (rückwärts) | 0/0/0/0/2/0 | heuristische Evaluation (Nielsen/Molich): Expertenbewertung von Oberflächen |
| `rosemann2008improving` | 2008 | Toward Improving the Relevance of Information Systems Research to Practice: The Role of Applicability Checks1 | MIS Quarterly | sonnenberg2012patterns (rückwärts) | 0/0/0/0/2/0 | Applicability Checks mit Praktikern (Relevanz von DSR) |
| `salvador2014product` | 2014 | Product configuration, ambidexterity and firm performance in the context of industrial equipment manufacturing | Journal of Operations Management | trentin2011overcoming (vorwärts) | 0/0/0/0/2/0 | Produktkonfiguration und Unternehmensleistung (empirisch) |
| `saruhashi2026improving` | 2026 | Improving design operations for offsite construction: an empirical implementation of a generative design framework | Construction Innovation | yin2019building (vorwärts) | 1/0/0/0/2/0 | empirische Einführung generativer Entwurfswerkzeuge in der Vorfertigung |
| `schaper2023toolkits` | 2023 | Toolkits for innovation: how digital technologies empower users in new product development | R&D Management | vonhippel2001user (vorwärts) | 0/0/0/0/2/0 | Toolkits for Innovation unter digitalen Bedingungen (Review) |
| `segura2016survey` | 2016 | A Survey on Metamorphic Testing | IEEE Transactions on Software Engineering | pinto2026exhaustive (rückwärts) | 0/1/0/0/2/0 | Metamorphes Testen: Prüfung ohne Referenzlösung, übertragbar auf Regelmaschine |
| `stehn2023industrialized` | 2023 | Industrialized house building productivity growth | Construction Innovation | grenzfurtner2026failure (rückwärts) | 0/0/0/0/2/0 | Produktivitätsentwicklung im industriellen Hausbau |
| `sviokla1990examination` | 1990 | An Examination of the Impact of Expert Systems on the Firm: The Case of XCON | MIS Quarterly | campogay2026quality, trentin2011overcoming (rückwärts) | 0/0/0/0/2/0 | XCON: betriebliche Wirkung eines Konfigurator-Expertensystems |
| `wang2007recommendation` | 2007 | Recommendation Agents for Electronic Commerce: Effects of Explanation Facilities on Trusting Beliefs | Journal of Management Information Systems | gregor1999explanations (vorwärts) | 0/0/0/0/2/0 | Erklärungskomponenten und Vertrauen in Empfehlungsagenten |
| `zelkowitz1998experimental` | 1998 | Experimental models for validating technology | Computer | sonnenberg2012patterns (rückwärts) | 0/0/0/0/2/0 | experimentelle Validierungsmodelle für Technologie |
| `zhang2022developing` | 2022 | Developing separate or integrated configurators? A longitudinal case study | International Journal of Production Economics | wang2022natural (vorwärts) | 0/0/0/0/2/0 | getrennte oder integrierte Konfiguratoren (Längsschnitt) |
| `zhao2018evaluation` | 2018 | An Evaluation Model for Web-based 3D Mass Customization Toolkit Design | Springer Proceedings in Business and Economics | vonhippel2001user (vorwärts) | 0/0/0/0/2/0 | Evaluationsmodell für webbasierte 3D-Konfiguratoren |

#### FF6 – Detailtiefe (Reifegrade, Dach, Schall, Licht, Raum, TGA) (47)

| Key | Jahr | Titel | Venue | Schneeball von | ff1–ff6 | Kurzbegründung |
|---|---|---|---|---|---|---|
| **`zhang2022bimbased`** | 2022 | BIM-based automated design of drainage systems for panelized residential buildings | International Journal of Construction Management | yin2019building (vorwärts) | 2/0/0/0/0/3 | automatischer Entwurf der Entwässerung für Tafelbau-Wohngebäude im BIM |
| `abdalhamid2023quantifying` | 2023 | Quantifying window view quality: A review on view perception assessment and representation methods | Building and Environment | bodin2015quiet (vorwärts) | 0/0/0/0/0/2 | Qualität der Fensteraussicht quantifizieren (Review) |
| `amundsen2011norwegian` | 2011 | The Norwegian Façade Insulation Study: The efficacy of façade insulation in reducing noise annoyance due to road traffic | The Journal of the Acoustical Society of America | locher2018windows (rückwärts); ohrstrom2006quietness (vorwärts) | 0/0/0/0/0/2 | Wirkung von Fassadendämmung auf Lärmbelästigung (Vorher-Nachher) |
| `andersen2013interactive` | 2013 | Interactive expert support for early stage full-year daylighting design: A user's perspective on Lightsolve | Automation in Construction | virzi1992subjects (vorwärts) | 0/0/0/0/1/2 | interaktive Expertenunterstützung für Tageslichtentwurf aus Nutzersicht |
| `bartels2021impact` | 2021 | The impact of nocturnal road traffic noise, bedroom window orientation, and work-related stress on subjective sleep quality: results of a cross-sectional study among working women | International Archives of Occupational and Environmental Health | bodin2015quiet, locher2018windows, ohrstrom2006quietness (vorwärts) | 0/0/0/0/0/2 | Orientierung des Schlafzimmerfensters, Straßenlärm und Schlaf |
| `benedikt1979take` | 1979 | To Take Hold of Space: Isovists and Isovist Fields | Environment and Planning B: Planning and Design | wiener2007isovist (rückwärts) | 0/0/0/0/0/2 | Isovisten und Isovistenfelder (Benedikt): Grundlage rechenbarer Sichtmaße |
| `caddick2018review` | 2018 | A review of the environmental parameters necessary for an optimal sleep environment | Building and Environment | emmitt2023bedroom (rückwärts); bodin2015quiet (vorwärts) | 0/0/0/0/0/2 | Umweltparameter für optimalen Schlafraum (Review) |
| `caniato2017acoustic` | 2017 | Acoustic of lightweight timber buildings: A review | Renewable and Sustainable Energy Reviews | chateauvieuxhellwig2022timber (rückwärts) | 0/0/0/0/0/2 | Akustik leichter Holzbauten (Review) |
| `chen2024nonimageforming` | 2024 | The Non-Image-Forming Effects of Daylight: An Analysis for Design Practice Purposes | Buildings | brown2020melanopic (vorwärts) | 0/0/0/0/0/2 | nicht-visuelle Tageslichtwirkung für die Entwurfspraxis |
| `cie2018s026` | 2018 | CIE S 026/E:2018 CIE System for Metrology of Optical Radiation for ipRGC-Influenced Responses to Light |  | potter2025sleep, spitschan2021luox (rückwärts) | 0/0/0/0/0/2 | CIE S 026: Metrik für melanopische Wirkung (Norm) |
| `degeetere2014new` | 2014 | A New Building Acoustical Concept for Lightweight Timber Frame Constructions | INTER-NOISE 2014 | chateauvieuxhellwig2022timber (rückwärts) | 0/0/0/0/0/2 | akustisches Konzept für Holzrahmenbau (Inter-Noise 2014) |
| `dekluizenaar2013road` | 2013 | Road Traffic Noise and Annoyance: A Quantification of the Effect of Quiet Side Exposure at Dwellings | International Journal of Environmental Research and Public Health | bodin2015quiet (rückwärts); ohrstrom2006quietness (vorwärts) | 0/0/0/0/0/2 | Quantifizierung der ruhigen Seite an Wohnungen |
| `dincer2024sleep` | 2024 | Beyond Sleep: Investigating User Needs in Today’s Bedrooms | Buildings | emmitt2023bedroom (vorwärts) | 0/0/0/0/0/2 | Nutzerbedürfnisse im heutigen Schlafzimmer |
| `dosen2013prospect` | 2013 | Prospect and Refuge Theory: Constructing a Critical Definition for Architecture and Design | The International Journal of Design in Society | dosen2013methodological (rückwärts) | 0/0/0/0/0/2 | kritische Definition Prospect-Refuge für die Architektur |
| `fan2022field` | 2022 | A field intervention study of the effects of window and door opening on bedroom IAQ, sleep quality, and next-day cognitive performance | Building and Environment | emmitt2023bedroom (rückwärts) | 0/0/0/0/0/2 | Fenster-/Türöffnung, Luftqualität im Schlafzimmer und Schlaf (Intervention) |
| `gkaintatzimasouti2022simulations` | 2022 | Simulations of non-image-forming effects of light in building design: A literature review | Lighting Research & Technology | brown2020melanopic (vorwärts) | 0/0/0/0/0/2 | Simulation nicht-visueller Lichtwirkung im Gebäudeentwurf (Review) |
| `harvieclark2019assessing` | 2019 | Assessing noise with provisions for ventilation and overheating in dwellings | Building Services Engineering Research and Technology | locher2018windows (vorwärts) | 0/0/0/0/0/2 | Schall, Lüftung und Überhitzung in Wohnungen gemeinsam planen |
| `heshmati2026photoentrainment` | 2026 | Photoentrainment in the Built Environment: Daylight/Lighting Regulations, Limitations, and Proposed New Design Strategies | Leukos | brown2020melanopic (vorwärts) | 0/0/0/0/0/2 | Tageslicht-/Beleuchtungsregeln und circadiane Wirkung |
| `houser2020humancentric` | 2020 | Human-centric lighting: Myth, magic or metaphor? | Lighting Research & Technology | brown2020melanopic (vorwärts) | 0/0/0/0/0/2 | Human-Centric Lighting kritisch: Abgrenzung Marketing/Evidenz |
| `houser2021humancentric` | 2021 | Human-Centric Lighting: Foundational Considerations and a Five-Step Design Process | Frontiers in Neurology | spitschan2021luox (rückwärts); brown2020melanopic (vorwärts) | 0/0/0/0/0/2 | Human-Centric Lighting: fünfstufiger Entwurfsprozess |
| `huber2012fast` | 2012 | A Fast Straight-Skeleton Algorithm Based on Generalized Motorcycle Graphs | International Journal of Computational Geometry & Applications | ahn2013roofs, biedl2015weighted (rückwärts) | 0/0/0/0/0/2 | Bone: industriefeste Straight-Skeleton-Implementierung |
| `kazeem2024integration` | 2024 | Integration of Building Services in Modular Construction: A PRISMA Approach | Applied Sciences | zhao2025mep (rückwärts) | 0/0/0/0/0/2 | Integration der TGA in modulares Bauen (Review) |
| `kearns2022housing` | 2022 | Housing space and occupancy standards: developing evidence for policy from a health and wellbeing perspective in the UK context | Building Research & Information | emmitt2023bedroom (rückwärts) | 0/0/0/0/0/2 | Wohnflächen- und Belegungsstandards aus Gesundheitssicht |
| `kutzias2024recent` | 2024 | Recent Advances in Procedural Generation of Buildings: From Diversity to Integration | IEEE Transactions on Games | held2017roofs (vorwärts) | 0/0/0/0/0/2 | Review prozedurale Gebäudegenerierung |
| `lan2017thermal` | 2017 | Thermal environment and sleep quality: A review | Energy and Buildings | emmitt2023bedroom (rückwärts) | 0/0/0/0/0/2 | thermische Umgebung und Schlafqualität (Review) |
| `laycock2003generating` | 2003 | Automatically generating large urban environments based on the footprint data of buildings | Proceedings of the eighth ACM symposium on Solid modeling and applications | ahn2013roofs, biedl2015weighted, held2017roofs (rückwärts) | 0/0/0/0/0/2 | Dächer aus Grundrisspolygonen automatisch erzeugen |
| `ozer2022dwelling` | 2022 | Dwelling size and usability in London: a study of floor plan data using machine learning | Building Research & Information | emmitt2023bedroom (rückwärts) | 0/0/0/0/0/2 | Wohnungsgröße und Nutzbarkeit aus Grundrissdaten (London) |
| `pestana2024optimizing` | 2024 | Optimizing MEP design in early AEC projects through generative design | Automation in Construction | zhao2025mep (rückwärts) | 0/0/0/0/0/2 | generatives TGA-Design in frühen Phasen |
| `pirrera2014field` | 2014 | Field study on the impact of nocturnal road traffic noise on sleep: The importance of in- and outdoor noise assessment, the bedroom location and nighttime noise disturbances | Science of The Total Environment | locher2018windows (rückwärts) | 0/0/0/0/0/2 | Schlafzimmerlage und Nachtlärm (Feldstudie) |
| `rasmussen2010sound` | 2010 | Sound insulation between dwellings – Requirements in building regulations in Europe | Applied Acoustics | chateauvieuxhellwig2022timber (rückwärts) | 0/0/0/0/0/2 | Schallschutzanforderungen zwischen Wohnungen in Europa im Vergleich |
| `reid2026sound` | 2026 | Sound advice: associations between building design attributes and residents’ noise annoyance | Cities & Health | locher2018windows (vorwärts) | 0/0/0/0/0/2 | Gebäudegestalt und Lärmbelästigung der Bewohner |
| `rewatkar2026data` | 2026 | A data driven decision-making framework for architectural design quality: Enhancing well-being in multi-family housing | Building Services Engineering Research & Technology | niemeijer2014freedom (vorwärts) | 0/0/0/0/0/2 | datenbasierte Bewertung der Wohnqualität im Geschosswohnungsbau |
| `rostamiasl2024cloudbased` | 2024 | A cloud-based integration of Building Information Modeling and Virtual Reality through game engine to facilitate the design of Age-in-Place homes at the conceptual stage | Journal of Information Technology in Construction | narayanaswamy2019bim (vorwärts) | 0/0/0/0/1/2 | Konzeptentwurf altersgerechter Häuser mit BIM+VR und Universal-Design-Regeln |
| `roswall2020nighttime` | 2020 | Nighttime road traffic noise exposure at the least and most exposed façades and sleep medication prescription redemption—a Danish cohort study | Sleep | bodin2015quiet, locher2018windows (vorwärts) | 0/0/0/0/0/2 | Nachtlärm an lautester/leisester Fassade und Schlafmittel (Kohorte) |
| `sentopdumen2020enforcement` | 2020 | Enforcement of acoustic performance assessment in residential buildings and occupant satisfaction | Building Research & Information | emmitt2023bedroom (rückwärts) | 0/0/0/0/0/2 | akustische Klassifizierung von Wohngebäuden und Zufriedenheit |
| `shemesh2022emotional` | 2022 | The emotional influence of different geometries in virtual spaces: A neurocognitive examination | Journal of Environmental Psychology | dosen2013methodological (vorwärts) | 0/0/0/0/0/2 | emotionale Wirkung von Raumgeometrien (neurokognitiv) |
| `silverman1992expert` | 1992 | Expert critics in engineering design: lessons learned and research needs | AI Magazine | gregor1999explanations (rückwärts) | 0/0/0/0/0/2 | Expert Critics im Ingenieurentwurf: Lehren für Critiquing |
| `stamps2008some` | 2008 | Some Findings on Prospect and Refuge Theory: II | Perceptual and Motor Skills | dosen2013methodological (rückwärts) | 0/0/0/0/0/2 | Prospect-Refuge: Zusammenfassung von acht Studien (Stamps) |
| `stefani2024evidencebased` | 2024 | Towards an evidence-based integrative lighting score: a proposed multi-level approach | Annals of Medicine | brown2020melanopic, cajochen2022evening (vorwärts) | 0/0/0/0/0/2 | integrativer Beleuchtungsscore (mehrstufig) |
| `suarez2023optimizing` | 2023 | Optimizing Modularity of Prefabricated Residential Plumbing Systems for Construction in Remote Communities | Journal of Construction Engineering and Management | zhao2025mep (rückwärts) | 0/0/0/0/0/2 | Modularität vorgefertigter Sanitärinstallationen im Wohnbau |
| `sugihara2013automatic` | 2013 | Automatic Generation of 3D Building Models from Complicated Building Polygons | Journal of Computing in Civil Engineering | aichholzer1996general (vorwärts) | 0/0/0/0/0/2 | 3D-Gebäude mit Dächern aus komplexen Grundrissen |
| `ticleanu2021impacts` | 2021 | Impacts of home lighting on human health | Lighting Research & Technology | brown2020melanopic, cain2020evening (vorwärts) | 0/0/0/0/0/2 | Wirkung von Wohnbeleuchtung auf Gesundheit |
| `tserng2011modularization` | 2011 | Modularization and assembly algorithm for efficient MEP construction | Automation in Construction | zhao2025mep (rückwärts) | 0/0/0/0/0/2 | Modularisierung und Montagealgorithmus für TGA |
| `unlu2022exploring` | 2022 | Exploring perceived openness and spaciousness: the effects of semantic and physical aspects | Architectural Science Review | wiener2007isovist (vorwärts) | 0/0/0/0/0/2 | wahrgenommene Offenheit/Weite aus Sichtvolumen und Tageslicht |
| `voncastell2014effect` | 2014 | The Effect of Furnishing on Perceived Spatial Dimensions and Spaciousness of Interior Space | Plos One | wiener2007isovist (vorwärts) | 0/0/0/0/0/2 | Möblierung und wahrgenommene Raumgröße |
| `wang2025natural` | 2025 | Natural light control to improve awakening quality | Building and Environment | cajochen2022evening (vorwärts) | 0/0/0/0/0/2 | Tageslichtsteuerung im Schlafzimmer und Aufwachqualität |
| `west2004functional` | 2004 | Functional design? An analysis of new speculative house plans in the UK | Design Studies | emmitt2023bedroom (rückwärts) | 0/0/0/0/1/2 | Funktionalität von Grundrissen spekulativer Neubauhäuser (UK) |

**Ausgeschlossen, aber als Hinweis festgehalten** (nicht zitierfähig nach 2a.4; vollständige Liste in Anhang A):

- **SSRN-Preprints:**
  - Barcelos & Isatto 2026, „Operationalizing automated compliance checking in an openBIM environment“. Weiterhin nur Preprint; schon in Runde 1 vermerkt.
  - „Knowledge Engineering for AI Collaborative BIM“ (2026)
  - „A Closed-Loop Framework for Automated IFC Model Validation“ (2026)
  - „Cognitively Grounded Floorplan Optimization to Nudge Occupant Route Choices“ (2022)
- **Vorfassungen:**
  - Tagungsfassungen zu `alwisy2019bim`, `ramaji2017product`, `abualdenien2019metamodel` (zwei), `hwang2018window` und `ahn2013roofs`
  - EuroCG-Vorfassungen zu `eder2018volume` und `held2017roofs`
- **Hochschulschriften mit Inhalt an anderer Stelle:**
  - Vestin (2020, Lizentiatsarbeit; Inhalt in `vestin2020smart`, `vestin2023mitigating`)
  - Huber (2012, Dissertation Salzburg; Inhalt in `huber2012fast`)
- **Hinweis ohne Aufnahme:** Die Lizentiatsarbeit von Malmgren nennt „Product modeling of configurable building systems“ (ITcon 2010). Diese Arbeit steht bereits im Bestand (`malmgren2010product`).

## 6 Sättigungsbewertung

**Kriterium (Protokoll 2a.3, Auftrag):** Runde 2 gilt als gesättigt, wenn beide Bedingungen gelten:
- (a) Die Aufnahmequote liegt deutlich unter Runde 1.
- (b) Keine neue Quelle erreicht Relevanz 3.

Das strengere ursprüngliche Abbruchkriterium aus 2a.3 Nr. 3 („keine neue Quelle mit Relevanz ≥ 2“) ist mit 162 Aufnahmen klar verfehlt.

**Messung:**

| Kennzahl | Runde 1 | Runde 2 | Veränderung |
|---|---|---|---|
| Aufnahmequote aufgenommen / gesichtet (roh) | 4,4 % | 3,3 % | −1,1 Prozentpunkte (relativ −26 %) |
| Trefferquote aufgenommen / neue Kandidaten | 67,6 % | 47,8 % | −19,8 Prozentpunkte |
| Anteil redundanter Funde und Vorfassungen unter neuen Kandidaten | 3,5 % (15 von 423) | 17,4 % (59 von 339) | etwa verfünffacht |
| Bestandsdubletten unter Kandidaten | 16,3 % (Teil B) | 17,5 % | etwa gleich |
| neue Quellen mit Relevanz 3 | 29 | 3 | −90 % |

**Urteil:**
- **(a) Quote:** nur teilweise erfüllt. Die Quote sinkt, aber um ein Viertel, nicht auf die Hälfte oder weniger. „Deutlich“ ist das nicht. Bezogen auf die Trefferquote je Kandidat und auf den Anteil der Wiederholungen ist der Rückgang dagegen klar.
- **(b) Relevanz 3:** nicht erfüllt. Drei neue Quellen erreichen Relevanz 3 (`wei2025texttostructure`, `an2020bimbased`, `zhang2022bimbased`).
- **Gesamt:** **Runde 2 ist nicht gesättigt.** Der Ertrag an Relevanz-3-Funden ist aber gegenüber Runde 1 um 90 % eingebrochen. Er konzentriert sich auf zwei eng umrissene Linien: die TUM-Linie der natürlichsprachlichen BIM-Interaktion und die Alberta-Linie der regelbasierten Holzrahmen-Fertigung.

**Empfehlung: Runde 3 ja, aber gezielt statt flächig.**

1. **Startmenge Runde 3:**
   - die drei Relevanz-3-Funde `wei2025texttostructure`, `an2020bimbased` und `zhang2022bimbased`, jeweils rückwärts und vorwärts
   - aus den beiden Clustern, die noch über dem Niveau von Runde 1 liefern, die R2-Funde, die nach dem Einpflegen in `quellen-bewertung.csv` Kernbestand werden (P ≥ 5). Das sind Sprache/Konfiguration (9,6 %) und Regelprüfung/Bauantrag (6,6 %). Voraussichtlich gehören dazu `yin2023twostage`, `guo2025advancing`, `yang2026llmpowered`, `hagedorn2025ontobpr`, `fauth2025baugenehmigungsv`, `hartmann2026status` und `recski2024briseplandok`.
2. **Keine weitere Runde für:**
   - Dachgeometrie (Quote 1,1 %)
   - Schall/Lärm und Licht/Schlaf (je 2,3 %, fast nur Einzelstudien mit Relevanz 2, die bestehende Argumente bestätigen)
   - Wirkung/Evaluation (3,2 %, hoher Anteil redundanter Funde)
   - Informationsmodell allgemein (Quote bei `yin2019building` vorwärts 2,4 %)

   Diese Cluster gelten nach dem Muster von Runde 2 als praktisch gesättigt.
3. **Abbruchregel für Runde 3:** Sättigung ist erreicht, wenn keine neue Quelle mit Relevanz 3 hinzukommt und die Rohquote unter 2 % liegt, also unter der Hälfte von Runde 1. Kommt erneut Relevanz 3 hinzu, wird nur von diesen Quellen aus weitergesucht.
4. **FF4 bleibt eine Lücke des Schneeballs:** 20 FF4-Funde, keiner mit Relevanz 3. Die zwei deutschen Erhebungen sind die stärksten Kandidaten für eine Höherstufung nach Volltext. Juristische Quellen stehen nicht im Zitationsnetz, etwa Kommentare zu BayBO Art. 61/62, Haftung des Entwurfsverfassers und Rolle der Prüfsachverständigen. Die Zusatzrecherche aus Runde 1 (Abschnitt 6 Nr. 3 in Recherche 24) bleibt nötig und ersetzt für FF4 eine weitere Schneeballrunde.

## 7 Grenzen dieser Runde

- **Datenbasis OpenAlex:**
  - Referenzlisten sind unvollständig aufgelöst: rückwärts 2 385 von 2 621 gemeldeten `referenced_works`.
  - Tagungsbände ohne DOI fehlen häufig. Semantic Scholar war nicht nutzbar, ein Abgleich mit einer zweiten Zitationsdatenbank steht aus.
- **Gefilterte Vorwärtssuche** bei sechs Startquellen:
  - Q644 (174 von 537)
  - Q724 (200 von 328 Filtertreffern bei 1 230 Zitierenden)
  - Q726 (149 von 521)
  - Q749 (184 von 251)
  - Q750 (77 von 119)
  - Q791 (145 von 345)

  Zitierende außerhalb der Filterbegriffe sind nicht gesichtet.
- **Bestandsdubletten** sind nur auf Kandidatenebene vollständig gezählt, nicht auf Listenebene. Die Rohzahl „gesichtet“ ist nicht rundenintern bereinigt; das gilt ebenso für Teil B von Runde 1.
- **Einstufung ohne Abstract:** 34 der 158 DOI-Funde sind ohne Abstract eingestuft, vor allem Elsevier-Artikel ohne Abstract in OpenAlex. Bei der Zweitbewertung für κ sollten sie bevorzugt geprüft werden, ebenso die Grenzfälle mit Relevanz 2:
  - Software-Testmethoden (`barr2015oracle`, `segura2016survey`)
  - Lärm- und Lichtepidemiologie mit Wohnbezug
  - LLM-BIM-Einzelarbeiten
- **Redundanz als Ausschlussgrund** ist eine Ermessensentscheidung eines einzelnen Bewerters (2a.7). Die 49 so ausgeschlossenen Kandidaten stehen mit Begründung in Anhang A und lassen sich bei Bedarf nachholen.
- **Jahresangaben** folgen Crossref (Heftjahr). OpenAlex nennt teils das Online-Jahr, z. B. `an2020bimbased`: OpenAlex 2019, Crossref 2020.

## Anhang A: ausgeschlossene Kandidaten (177)

| DOI / Quelle | Grund | Anmerkung |
|---|---|---|
| 10.2139/ssrn.7327425 | Preprint ohne Begutachtung | SSRN-Preprint |
| 10.2139/ssrn.7428103 | Preprint ohne Begutachtung | SSRN-Preprint |
| 10.2139/ssrn.6251260 | Preprint ohne Begutachtung | SSRN-Preprint |
| 10.2139/ssrn.4003119 | Preprint ohne Begutachtung | SSRN-Preprint |
| 10.1201/9780203883327.ch52 | Vorfassung/Tagungsfassung | Tagungsfassung Constraint-Prüfung (niemeijer-Linie) |
| 10.1061/9780784412343.0028 | Vorfassung/Tagungsfassung | Tagungsfassung zu alwisy2019bim |
| 10.1061/9780784479070.002 | Vorfassung/Tagungsfassung | Tagungsfassung zu ramaji2017 |
| 10.1201/9780429506215-24 | Vorfassung/Tagungsfassung | Tagungsfassung zu abualdenien2019metamodel |
| 10.1061/9780784482421.032 | Vorfassung/Tagungsfassung | Tagungsfassung Abualdenien |
| 10.1007/978-3-642-25591-5_8 | Vorfassung/Tagungsfassung | Tagungsfassung zu ahn2013roofs |
| 10.52842/conf.caadria.2018.2.577 | Vorfassung/Tagungsfassung | Tagungsfassung zu hwang2018window |
| (ohne DOI) Managing Building Design Variants at Multiple Development Levels | Vorfassung/Tagungsfassung | Tagungsfassung Abualdenien |
| (ohne DOI) Bisector Graphs for Min-/Max-Volume Roofs over Simple Polygons | Vorfassung/Tagungsfassung | EuroCG-Vorfassung zu eder2018volume |
| (ohne DOI) Additive Weights for Straight Skeletons | Vorfassung/Tagungsfassung | EuroCG-Vorfassung zu held2017roofs |
| 10.1007/978-3-319-54660-5_40 | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | kein Abstract, Tagungsbeitrag |
| 10.1007/978-3-031-16538-2_30 | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | kein Abstract |
| 10.1016/j.aei.2026.105075 | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | kein Abstract auffindbar |
| 10.1016/j.compind.2021.103570 | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | kein Abstract |
| 10.1007/978-3-319-77556-2_35 | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | kein Abstract |
| (ohne DOI) USING 3D GEOMETRIC CONSTRAINTS IN ARCHITECTURAL DESIGN SUPPORT SYSTEMS | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | Tagungsbeitrag 2000, nicht verifiziert |
| (ohne DOI) A knowledge representation approach in BIM rule requirement analysis u | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | nicht verifiziert |
| (ohne DOI) Designing a Reference Model for Digital Product Configurators | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | nicht verifiziert |
| (ohne DOI) BIM-based framework for indoor acoustic conditioning in early stages o | nicht verifizierbar bzw. ohne Abstract nicht bewertbar | nicht verifiziert |
| (ohne DOI) Smart manufacturing for the wooden single-family house industry | Hochschulschrift, Inhalt anderweitig belegt | Lizentiatsarbeit, Inhalt in Nr. 133/109 |
| (ohne DOI) Design-for-empowerment-for-design: computational structures for design | Hochschulschrift, Inhalt anderweitig belegt | Hochschulschrift, nicht verifiziert |
| (ohne DOI) Computing Straight Skeletons and Motorcycle Graphs: Theory and Practic | Hochschulschrift, Inhalt anderweitig belegt | Dissertation, Inhalt in huber2012fast |
| 10.35490/ec3.2022.148 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Review Regelinterpretation; redundant zu zhang2023rule/lee2026automated |
| 10.5194/isprs-archives-xliii-b4-2022-529-2022 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | GeoBIM-Prüfungen; redundant zu noardo2022ifc |
| 10.36680/j.itcon.2025.002 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | ML-Review ACC; redundant zu senousy2026automated |
| 10.1186/s40327-017-0055-0 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | VPL-Abfragen; redundant zu preidel2016towards |
| 10.3390/app15010049 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Review Model Checking; redundant |
| 10.1007/s10462-025-11241-7 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | LLM-Review AEC; redundant zu park2026bimllm |
| 10.3390/info15120759 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | SHACL-ACC; redundant zu hagedorn2023semantic |
| 10.1061/9780784413616.067 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Kodierrichtlinien; redundant zu dimyadi2016computerizing |
| 10.1080/09613218.2026.2637965 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Review Regelinterpretation; redundant |
| 10.1007/s00158-016-1454-x | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Lösungsräume hochdimensional; redundant zu Nr. 64 |
| 10.1061/9780784480823.020 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | VCCL; redundant zu preidel2016towards |
| 10.1061/(asce)cp.1943-5487.0001019 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | NLP-QA BIM; redundant |
| 10.1016/j.promfg.2018.06.129 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Tagungsfassung; redundant zu Nr. 133 |
| 10.29173/mocs105 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 133/135 |
| 10.1016/j.procir.2021.11.251 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 133 |
| 10.1016/j.autcon.2015.07.010 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Validierung Austausch; redundant zu lee2019mechanism |
| 10.1139/cjce-2014-0078 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Änderungsverfolgung; redundant zu shi2018ifcdiff |
| 10.1007/s10845-011-0544-2 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 146 |
| 10.1017/s0890060498124022 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 205 |
| 10.3390/app15147647 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | LLM-BIM-Abfrage; redundant |
| 10.1016/j.autcon.2020.103287 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Stahlrahmen; redundant zu Nr. 168 |
| 10.1155/2020/8946530 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | IDM Vorfertigung; redundant zu rojaswettling2023idm |
| 10.1080/09537287.2018.1513177 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Nacharbeitskosten; redundant zu love2018unpacking/love2022rework |
| 10.1016/s0004-3702(83)80014-9 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 182 |
| 10.1016/0166-3615(94)00041-n | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 146/51 |
| 10.1016/b978-0-12-415817-7.00004-9 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Buchkapitel; redundant zu hvam2006quotation |
| 10.1145/62065.62067 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 188/140 |
| 10.1016/s0954-1810(01)00016-4 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 205 |
| 10.1109/ieem.2015.7385608 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Konferenzbeitrag; redundant zu kristjansdottir2018return |
| 10.24867/ijiem-2012-4-125 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 237 |
| 10.1016/j.jbi.2013.04.007 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Stichprobengröße; redundant zu faulkner2003beyond/virzi1992subjects |
| 10.1007/s10796-026-10716-4 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 221 |
| 10.4018/ij3dim.2018010103 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | LOD-Leitfäden; redundant zu abualdenien2022levels |
| 10.24132/csrn.2019.2901.1.12 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 249 |
| 10.1016/j.tcs.2017.02.013 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Fortsetzung ahn2013roofs |
| 10.3390/ijerph9124292 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 267 |
| 10.1121/1.3621180 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 267 |
| 10.1121/1.4802824 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 271 |
| 10.1177/1351010x251348672 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 294 |
| 10.1016/s0003-682x(01)00040-8 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu locher2018windows |
| 10.1016/j.apacoust.2008.01.007 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu locher2018windows |
| 10.3389/fphot.2023.1272934 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu brown2022recommendations |
| 10.2466/pms.106.1.147-162 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 292 |
| 10.1177/1477153518824147 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 296 |
| 10.3390/buildings13051357 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 286 |
| 10.1080/00038628.2016.1266597 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 303 |
| 10.1016/j.sleh.2023.02.010 | redundant (Argument bereits durch Bestand/anderen Fund getragen) | redundant zu Nr. 308 |
| (ohne DOI) Straight Skeleton for Automatic Generation of 3-D Building Models with | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Tagungsfassung Sugihara |
| (ohne DOI) Predicting experiential qualities of architecture by its spatial prope | redundant (Argument bereits durch Bestand/anderen Fund getragen) | Tagungsbeitrag; redundant zu wiener2007isovist |
| 10.1016/j.autcon.2017.08.006 | Relevanz < 2 | Auftraggeber-Informationsanforderungen allgemein |
| 10.1061/(asce)cp.1943-5487.0000922 | Relevanz < 2 | semantische Anreicherung für ACC, generisch |
| 10.3390/buildings12010045 | Relevanz < 2 | Adoptionsfaktoren in einer Behörde, Kontext |
| 10.1088/1755-1315/323/1/012102 | Relevanz < 2 | Grundlagenstudie Behörden-BIM ohne übertragbaren Baustein (Tagungsbeitrag) |
| 10.3846/ijspm.2020.13676 | Relevanz < 2 | BIM-Adoption in einer Genehmigungsbehörde, Kontext |
| 10.1108/eum0000000005831 | Relevanz < 2 | CORENET, historisch |
| 10.2749/newyork.2019.1560 | Relevanz < 2 | Standardisierung Bauantragsprozess, ohne Baustein |
| 10.1007/10929179_70 | Relevanz < 2 | E-Government Bauantrag 2003, historisch |
| 10.1016/j.autcon.2022.104524 | Relevanz < 2 | NLP-Regelinterpretation, generisch |
| 10.1016/j.compind.2022.103746 | Relevanz < 2 | NLP+Grammatik, generisch |
| 10.1016/j.aei.2023.102137 | Relevanz < 2 | GNN für Code-Checking |
| 10.1016/j.autcon.2009.07.008 | Relevanz < 2 | historische Ontologie Konformitätsanforderungen |
| 10.1016/j.autcon.2017.08.010 | Relevanz < 2 | Datenintegritätslogik, generisch |
| 10.1016/j.autcon.2020.103248 | Relevanz < 2 | Schema-Abfragen, generisch |
| 10.1016/j.aei.2015.05.006 | Relevanz < 2 | Ausschreibungsprüfung Korea |
| 10.1016/j.autcon.2025.106450 | Relevanz < 2 | LLM-Auslegung Bauvorschriften, generisch |
| 10.3390/civileng4020022 | Relevanz < 2 | Übersetzung Normtext (Russland), generisch |
| 10.1016/c2013-0-07627-x | Relevanz < 2 | Lehrbuch Constraint Satisfaction, Kontext |
| 10.1145/3344429.3372508 | Relevanz < 2 | Compiler-Fehlermeldungen, fremde Domäne |
| 10.1061/(asce)cp.1943-5487.0000427 | Relevanz < 2 | Informationstransformation ACC, generisch |
| 10.1016/j.autcon.2024.105369 | Relevanz < 2 | Ethik KI im Bau, allgemein |
| 10.1016/j.autcon.2025.106331 | Relevanz < 2 | LLM-Stahlbetonbemessung |
| 10.1016/j.aei.2022.101557 | Relevanz < 2 | NLG für Bauvorschriften |
| 10.3390/buildings12020154 | Relevanz < 2 | Check-Flow Italien |
| 10.22260/isarc2023/0011 | Relevanz < 2 | ChatGPT für ACC, explorativ |
| 10.1061/9780784412343.0036 | Relevanz < 2 | Nawari 2012, Kontext |
| 10.1061/9780784412367.084 | Relevanz < 2 | Model Checking allgemein |
| 10.3233/sw-180297 | Relevanz < 2 | SPARQL-Erweiterung |
| 10.1061/(asce)cp.1943-5487.0000331 | Relevanz < 2 | Graphmodell Topologie |
| 10.1061/(asce)ae.1943-5568.0000049 | Relevanz < 2 | Nawari, Kontext |
| 10.1061/(asce)ae.1943-5568.0000382 | Relevanz < 2 | Design-Review-Rahmen allgemein |
| 10.1016/j.dibe.2023.100174 | Relevanz < 2 | Korea ACC-Methoden |
| 10.1088/1755-1315/1101/9/092007 | Relevanz < 2 | Ontologie Normanforderungen |
| 10.1061/9780784483961.105 | Relevanz < 2 | Visualisierung verknüpfter Anforderungen |
| 10.1061/(asce)0887-3801(2005)19:1(1) | Relevanz < 2 | historisch |
| 10.1016/j.jclepro.2018.08.195 | Relevanz < 2 | Review Vorfertigung |
| 10.1016/j.jobe.2024.111515 | Relevanz < 2 | Digital Twin Genehmigung |
| 10.1016/j.aei.2025.103375 | Relevanz < 2 | LLM-Raumabfragen |
| 10.1016/j.aei.2025.104229 | Relevanz < 2 | IFC-Graph |
| 10.12688/openreseurope.18553.2 | Relevanz < 2 | Logbuch/Nachhaltigkeit |
| 10.1061/jladah.ladr-1310 | Relevanz < 2 | Stakeholder-Management Genehmigung |
| 10.1016/j.aei.2026.104735 | Relevanz < 2 | Normextraktion+ACC generisch |
| 10.1108/sasbe-01-2026-0077 | Relevanz < 2 | KPI-Rahmen |
| 10.1504/ijplm.2016.080502 | Relevanz < 2 | PLM/BIM-Vergleich |
| 10.1002/sys.70001 | Relevanz < 2 | Traceability MBSE, fremde Domäne |
| 10.18653/v1/2021.nllp-1.14 | Relevanz < 2 | Shallow Parsing Regeltexte |
| 10.1061/jcemd4.coeng-18122 | Relevanz < 2 | GenAI-Compliance |
| 10.1007/978-3-319-22786-3_38 | Relevanz < 2 | Graphgrammatik |
| 10.52842/conf.ecaade.2022.2.319 | Relevanz < 2 | ACC-Workflow |
| 10.36680/j.itcon.2026.025 | Relevanz < 2 | ML-Bauteilspezifikation |
| 10.1016/j.autcon.2026.107026 | Relevanz < 2 | Carbon Thread |
| 10.1016/j.autcon.2026.107038 | Relevanz < 2 | geometrieintensive ACC |
| 10.1016/j.aei.2026.105074 | Relevanz < 2 | Robotik-Review |
| 10.3390/s23062942 | Relevanz < 2 | Chatbot Bauleiter |
| 10.1016/j.compind.2023.104063 | Relevanz < 2 | semantisches Tagging |
| 10.1016/j.autcon.2025.106350 | Relevanz < 2 | Review generatives Design Vorfertigung |
| 10.1080/13467581.2024.2329351 | Relevanz < 2 | LLM-DfMA Freiform |
| 10.1207/s15516709cog1603_3 | Relevanz < 2 | Designproblemräume |
| 10.1016/j.autcon.2017.09.009 | Relevanz < 2 | Produktionsplanung Wandtafelwerk |
| 10.1016/j.autcon.2025.106174 | Relevanz < 2 | Review GenAI Architektur |
| 10.1109/tase.2020.2986774 | Relevanz < 2 | Multitask-Customization |
| 10.1061/9780784413517.170 | Relevanz < 2 | Montageplanung |
| 10.1061/9780784412343.0027 | Relevanz < 2 | IFC Fertigteil |
| 10.22260/isarc2016/0127 | Relevanz < 2 | MVD Fertigteil |
| 10.1108/ecam-11-2020-0986 | Relevanz < 2 | BIM-Lean Vorfertigungsplanung |
| 10.1061/(asce)co.1943-7862.0002369 | Relevanz < 2 | generatives Design Vorfertigung |
| 10.3390/su16052134 | Relevanz < 2 | Bibliometrie Holzvorfertigung |
| 10.1016/j.autcon.2024.105447 | Relevanz < 2 | Blockchain Produktion |
| 10.1061/jcemd4.coeng-13472 | Relevanz < 2 | Review DfMA |
| 10.1007/978-3-031-34821-1_12 | Relevanz < 2 | Konfigurator Umwelt |
| 10.1109/icrai62391.2024.10894593 | Relevanz < 2 | Paneloptimierung BSP |
| 10.1017/cbo9780511840005 | Relevanz < 2 | Argumentationstheorie, Kontext |
| 10.1080/09537287.2018.1485983 | Relevanz < 2 | MC-Leitlinien |
| 10.1080/01446193.2013.812227 | Relevanz < 2 | PDCA |
| 10.1108/ci-10-2019-0115 | Relevanz < 2 | KVP Auftragsabwicklung |
| 10.1108/ci-10-2013-0042 | Relevanz < 2 | Erfahrungsrückfluss Plattform |
| 10.1145/1555619.1555645 | Relevanz < 2 | DSR-Evaluationsalternativen |
| 10.1007/978-0-387-34930-5_7 | Relevanz < 2 | Konfigurationspraxis Finnland 1996 |
| 10.1016/j.jvlc.2011.11.005 | Relevanz < 2 | Endnutzer als Co-Designer |
| 10.1016/j.compind.2016.05.003 | Relevanz < 2 | Reifegradmodell ETO |
| 10.1108/ecam-06-2023-0645 | Relevanz < 2 | Nacharbeitsrisiko |
| 10.1287/mnsc.44.6.743 | Relevanz < 2 | Experimentieren in der Produktentwicklung |
| 10.1145/3479532 | Relevanz < 2 | Sprachassistent-Feedback, fremde Domäne |
| 10.1108/bpmj-05-2015-0067 | Relevanz < 2 | Prozess-Compliance |
| 10.1371/journal.pone.0321342 | Relevanz < 2 | Laienverständnis KI-Erklärungen Radiologie, fremde Domäne |
| 10.1016/j.jmsy.2025.06.013 | Relevanz < 2 | Konfigurationsempfehlung |
| 10.1016/j.dss.2017.03.003 | Relevanz < 2 | Guidance-Review |
| 10.1007/s00453-006-1229-7 | Relevanz < 2 | Motorcycle Graphs, Kontext |
| 10.1016/j.autcon.2019.103057 | Relevanz < 2 | Navigationsnetz |
| 10.1145/2898961 | Relevanz < 2 | SS-Algorithmus theoretisch |
| 10.1002/bate.202000090 | Relevanz < 2 | KI Tragwerk frühe Phase |
| 10.2312/conf/eg2013/short/085-088 | Relevanz < 2 | GPU-Dachgrammatik |
| 10.3390/acoustics2020016 | Relevanz < 2 | Performance-based Akustikentwurf |
| 10.1016/j.apacoust.2018.07.009 | Relevanz < 2 | BSP-Stoßstellen |
| 10.1016/j.jobe.2025.113216 | Relevanz < 2 | BSP-Beton-Decken |
| 10.1111/tgis.12970 | Relevanz < 2 | Parzellenmodell |
| 10.3390/ijerph7093359 | Relevanz < 2 | Innenhöfe |
| 10.1186/s12889-021-12069-w | Relevanz < 2 | Mehrfamilienhäuser Lärm |
| 10.3390/app14072945 | Relevanz < 2 | Krankenhausbeleuchtung |
| 10.1177/2399808320974533 | Relevanz < 2 | 3D-Isovisten |
| 10.1038/s41598-022-12408-w | Relevanz < 2 | Abendlicht REM |
| 10.1016/j.autcon.2019.102941 | Relevanz < 2 | Review MEP-Geometrie |
# Recherche 24: Schneeballverfahren Runde 1 zu FF1, FF2 und FF4

Status: v0.1 (27.09.2026). Nicht committet. Gehört zu `../arbeit/02a-review-protokoll.md` (2a.3 Nr. 3, 2a.4, 2a.5, 2a.6 Schritt 4).
Literaturdatei: `../arbeit/literatur/lit-I-schneeball-a.bib` (106 Einträge, alle [V], eine Teilangabe [U]). Fünf weitere aufgenommene Quellen (mit † markiert) stehen mit gleicher DOI bereits in der parallel entstandenen `lit-I-schneeball-b.bib` (Recherche 25) und werden dort unter dem angegebenen Key geführt, um doppelte Einträge zu vermeiden.

**Verfahren:** Wohlin (2014), eine Iteration, rückwärts (Referenzen der Startquelle) und vorwärts (Arbeiten, die die Startquelle zitieren).
Bewertung nach 2a.5: Relevanz 0–3 je Forschungsfrage, aufgenommen nur mit ff1, ff2 oder ff4 ≥ 2 und verifizierter Existenz.
„Relevanz 2“ heißt hier: Die Quelle stützt ein konkretes Argument der Arbeit (z. B. Aufteilung IDS/Regelmaschine, Prüfung im Entwurf, Freigabe-Gate, Ableitung von Maschinendaten). Generische ACC-Anwendungen in fremden Domänen (Brücken, Wasserbau, Arbeitsschutz auf der Baustelle, Krankenhaus ohne übertragbaren Baustein) erhalten höchstens 1.

## 1 Startmenge

Auswahlregel (Auftrag): `kern = ja` UND `art = W` UND [max(ff1, ff2, ff4) = 3 ODER (max(ff1, ff2, ff4) ≥ 2 UND P ≥ 6)], ausgewertet auf `literatur/quellen-bewertung.csv` (462 Zeilen). Ergebnis: **23 Startquellen**.

| id | Key | ff1 | ff2 | ff4 | P | OpenAlex-ID | Kante zur Startquelle |
|---|---|---|---|---|---|---|---|
| Q001 | `eastman2009automatic` | 1 | 3 | 0 | 6.0 | W2066023832 | OpenAlex |
| Q002 | `solihin2015classification` | 1 | 3 | 0 | 5.5 | W2053846395 | OpenAlex |
| Q009 | `hjelseth2011capturing` | 0 | 3 | 0 | 5.5 | W2101926299 | OpenAlex (ohne DOI, Titelsuche) |
| Q014 | `moult2020compliance` | 1 | 3 | 0 | 5.5 | W3084036425 | OpenAlex vorwärts; rückwärts Volltext (keine Referenzen in OpenAlex) |
| Q017 | `fischer2025bridging` | 0 | 3 | 0 | 5.5 | W4408773182 | OpenAlex |
| Q110 | `schoenwitz2017product` | 0 | 2 | 0 | 6.5 | W2533647958 | OpenAlex |
| Q207 | `duarte2001customizing` | 0 | 3 | 0 | 5.5 | W1492583075 | OpenAlex vorwärts; rückwärts nicht zugänglich |
| Q208 | `duarte2005discursive` | 0 | 3 | 0 | 5.5 | W2085346316 | OpenAlex |
| Q212 | `kwiecinski2016wood` | 0 | 3 | 0 | 5.5 | W2588886183 | OpenAlex |
| Q215 | `khalili2016development` | 0 | 3 | 0 | 5.5 | W2236051048 | OpenAlex |
| Q224 | `popovic2021configuration` | 3 | 2 | 0 | 5.5 | W3085083842 | OpenAlex |
| Q233 | `geier2018analysemodell` | 0 | 3 | 0 | 6.5 | W2890206135 | OpenAlex (0 Zitierende, 0 Referenzen); Volltext nicht abrufbar |
| Q234 | `chateauvieux2023bim` | 2 | 1 | 0 | 6.5 | – | nicht in OpenAlex; rückwärts über mediaTUM-Volltext |
| Q240 | `alwisy2019bim` | 3 | 2 | 0 | 5.5 | W2789648104 | OpenAlex |
| Q243 | `ramaji2017product` | 3 | 0 | 0 | 5.5 | W2587913078 | OpenAlex |
| Q247 | `rojaswettling2023idm` | 3 | 2 | 0 | 5.5 | W4366989908 | OpenAlex |
| Q248 | `shafiee2025enhancing` | 3 | 2 | 0 | 5.5 | W4404961726 | OpenAlex |
| Q260 | `sydora2020rulebased` | 0 | 3 | 0 | 5.5 | W3082354722 | OpenAlex |
| Q261 | `niemeijer2009checkmate` | 2 | 3 | 0 | 5.5 | W1540571331 | OpenAlex |
| Q262 | `niemeijer2011constraint` | 0 | 3 | 0 | 5.5 | W1552445635 | OpenAlex vorwärts; rückwärts nicht zugänglich |
| Q294 | `abualdenien2019metamodel` | 2 | 0 | 0 | 6.5 | W2936735866 | OpenAlex |
| Q295 | `abualdenien2022levels` | 2 | 0 | 0 | 6.0 | W4224314439 | OpenAlex |
| Q384 | `meseguer2006soft` | 0 | 3 | 0 | 6.5 | (W47957325 = Handbuch) | Kapitel nicht einzeln indexiert; vorwärts über das Handbuch mit Themenfilter |

**Befund zur Startmenge:** Keine Startquelle erreicht ff4 ≥ 2. Die einzigen W-Quellen mit ff4 = 2 (`fauth2024taxonomy`, `fauth2026digital`) haben P = 4,5 und sind nicht im Kernbestand. FF4 wird in dieser Runde deshalb nur indirekt erreicht (über zitierende Arbeiten zum digitalen Bauantrag).

## 2 Suchweg und Werkzeuge

- **Semantic Scholar** (`api.semanticscholar.org`): direkt per Proxy gesperrt (403); über Exa-Fetch nicht lesbar (`CRAWL_UNEXPECTED_CONTENT_TYPE`). Nicht genutzt.
- **OpenAlex** (`api.openalex.org`): direkt gesperrt (403), über `mcp__Exa__web_fetch_exa` lesbar. Primärquelle dieser Runde:
  - rückwärts: `works?filter=cited_by:<W-ID>` (aufgelöste `referenced_works`)
  - vorwärts: `works?filter=cites:<W-ID>` (vollständig, bei Q001 und Q002 seitenweise, 721 bzw. 301 Treffer)
  - Metadaten und Abstracts der Kandidaten: `works?filter=doi:…&select=…,abstract_inverted_index`
- **Crossref** (`api.crossref.org/works?filter=doi:…`, über Exa-Fetch): bibliografische Verifikation aller 108 aufgenommenen DOIs aus Crossref; zwei DataCite-DOIs über `api.datacite.org`; zwei ITcon-Artikel ohne DOI über die Verlagsseite `itcon.org`.
- **Volltexte** (Exa-Fetch): TU-Delft-Repositorium bzw. Exa-Bibliothek (Q014) und mediaTUM-PDF (Q234). Nicht abrufbar: mediaTUM-PDF von Q233 (`SOURCE_NOT_AVAILABLE`), TU/e-PDF von Q262 (`CRAWL_NOT_FOUND`), MIT-DSpace-Scan von Q207 (66 MB, nur Bildscan).
- **Dublettenprüfung:** gegen `quellen-master.csv` (530 Einträge, DOI exakt, Titel normalisiert auf 60 Zeichen) und zusätzlich gegen DOI und Titel aller `lit-*.bib`. Keine Key-Kollision mit den 533 vorhandenen Keys.

## 3 Protokoll je Startquelle

Zählweise: „gesichtet“ = Datensätze der OpenAlex-Liste bzw. Einträge des Literaturverzeichnisses; „Bestand“ = Dublette zu `quellen-master.csv`; „Kandidaten“ = nach Titel-Screening zur Abstract-Prüfung vorgemerkt (vor Abgleich zwischen den Startquellen); „aufgenommen“ = in `lit-I-schneeball-a.bib`. 32 der 111 aufgenommenen Quellen werden von mehr als einer Startquelle erreicht; sie zählen bei jeder Startquelle. r = rückwärts, v = vorwärts.

| Start | Referenzen gesichtet / davon Bestand | Zitierende gesichtet / davon Bestand | Kandidaten (Abstract) r / v | aufgenommen r / v | Beispiele aufgenommener Quellen |
|---|---|---|---|---|---|
| Q001 `eastman2009automatic` | 19 / 0 | 721 / 35 | 4 / 103 | 2 / 53 | `plume2007collaborative`, `le2020hitos`, `noardo2022ifc` |
| Q002 `solihin2015classification` | 30 / 3 | 301 / 9 | 9 / 41 | 1 / 22 | `borrmann2009topological`, `fuchs2025exploring`, `narayanaswamy2019bim` |
| Q009 `hjelseth2011capturing` | 13 / 0 | 79 / 8 | 1 / 26 | 0 / 7 | `noardo2022ifc`, `niemeijer2014freedom`, `zhang2023capabilities` |
| Q014 `moult2020compliance` | 9 (Volltext) / 3 | 5 / 1 | 1 / 0 | 1 / 0 | `pichler2012imperative` |
| Q017 `fischer2025bridging` | 16 / 1 | 6 / 0 | 8 / 3 | 8 / 3 | `fischer2024extending`, `nuyts2024comparative`, `tomczak2024requiring` |
| Q110 `schoenwitz2017product` | 75 / 4 | 69 / 1 | 0 / 1 | 0 / 0 | – |
| Q207 `duarte2001customizing` | – (nicht zugänglich) | 147 / 2 | 0 / 1 | 0 / 0 | – |
| Q208 `duarte2005discursive` | 7 / 0 | 153 / 5 | 0 / 3 | 0 / 1 | `jalaliyazdi2021clt`† |
| Q212 `kwiecinski2016wood` | 13 / 0 | 6 / 0 | 1 / 1 | 1 / 1 | `kwiecinski2014system`, `kwiecinski2018hopla` |
| Q215 `khalili2016development` | 21 / 4 | 29 / 1 | 0 / 1 | 0 / 1 | `kwiecinski2018hopla` |
| Q224 `popovic2021configuration` | 38 / 14 | 9 / 1 | 5 / 1 | 4 / 0 | `khaliliaraghi2020variability`, `ramaji2016product`, `jansson2019breakdown` |
| Q233 `geier2018analysemodell` | – (nicht zugänglich) | 0 | 0 / 0 | 0 / 0 | – |
| Q234 `chateauvieux2023bim` | ca. 235 (Volltext) / ≥ 12 | – (nicht in OpenAlex) | 6 / 0 | 4 / 0 | `darwish2022automated`, `day2019knowledge`, `liu2016ontology` |
| Q240 `alwisy2019bim` | 20 / 1 | 75 / 1 | 1 / 7 | 0 / 7 | `abushwereb2019framework`, `yin2019building`, `mtehrani2025streamlining` |
| Q243 `ramaji2017product` | 32 / 2 | 64 / 3 | 4 / 5 | 3 / 4 | `eastman2010exchange`, `nawari2012bim`, `laakso2012ifc` |
| Q247 `rojaswettling2023idm` | 19 / 2 | 5 / 0 | 6 / 1 | 5 / 1 | `yin2019building`, `he2021bim`, `venugopal2012semantics` |
| Q248 `shafiee2025enhancing` | 44 / 4 | 4 / 0 | 3 / 1 | 1 / 0 | `cao2021cross` |
| Q260 `sydora2020rulebased` | 49 / 10 | 116 / 3 | 11 / 17 | 3 / 11 | `lee2016translating`, `mazairac2013bimql`, `preidel2016towards` |
| Q261 `niemeijer2009checkmate` | 11 / 0 | 15 / 1 | 3 / 4 | 2 / 1 | `nassar2003building`, `donath2008constraint`, `benghi2019automated` |
| Q262 `niemeijer2011constraint` | – (nicht zugänglich) | 4 / 0 | 0 / 1 | 0 / 1 | `niemeijer2014freedom` |
| Q294 `abualdenien2019metamodel` | 49 / 2 | 70 / 2 | 2 / 4 | 0 / 3 | `zahedi2022bim`, `slepicka2022fabrication`, `piazzi2022graphical`† |
| Q295 `abualdenien2022levels` | 34 / 3 | 60 / 0 | 2 / 2 | 1 / 2 | `abualdenien2020consistent`†, `comai2026definition`, `mellenthinfilardo2026requirements`† |
| Q384 `meseguer2006soft` | – (Kapitel nicht indexiert) | 128 von 1498 (Handbuch, Themenfilter) / 0 | 0 / 3 | 0 / 2 | `bogaerts2021step`, `vareilles2013renovation`† |

Kurzbefund je Cluster:

- **Regelprüfung (Q001, Q002, Q009, Q260):** Das mit Abstand ergiebigste Cluster. `eastman2009automatic` hat 721 zitierende Arbeiten; davon tragen etwa 50 ein konkretes Argument. Neu sind vor allem:
  - Arbeiten zum digitalen Bauantrag (Wien, Südtirol, Portugal, EU-Strategien, OBPA, GeoBIM)
  - die Formalisierung an der Quelle (`fuchs2025exploring`, `mcgibbney2013intelligent`)
  - Transparenz und Verifikation von Prüfsoftware (`gade2021exploration`, `pinto2026exhaustive`, `purushotham2026automated`)
  - der Holzbaubezug (`narayanaswamy2019bim`, `kincelova2020fire`, `paskoff2023bim`)
- **IDS (Q017):** Die Referenz- und Zitationsliste von `fischer2025bridging` ist nahezu vollständig einschlägig (11 von 22 Datensätzen aufgenommen). Hinzu kommen `fischer2024extending` (IDS für den Bauantrag) und `nuyts2024comparative` (IDS, SHACL u. a. im direkten Vergleich).
- **Vorfertigung und Informationslieferung (Q240, Q243, Q247, Q248, Q224):**
  - Model-View- und Exchange-Model-Grundlagen (`eastman2010exchange`, `venugopal2012semantics`, `ramaji2016product`)
  - Ableitung von Fertigungsdaten (`darwish2022automated`, `mtehrani2025streamlining`, `abushwereb2019framework`, `liu2021bim` (BVBS-Bewehrungsdaten))
  - die Holz-Einfamilienhausindustrie (`vestin2022information`)
- **Mass Customization und Constraints (Q207, Q208, Q212, Q215, Q261, Q262, Q384):** Die zitierenden Arbeiten der Formgrammatik-Linie (Duarte) sind überwiegend generative Gestaltung ohne Regelprüfung (FF6-nah, ff2 ≤ 1). Tragfähig für FF2 sind:
  - `niemeijer2014freedom`
  - `khaliliaraghi2020variability`
  - `kwiecinski2018hopla`
  - `donath2008constraint`
  - `bogaerts2021step` (erklärbare Constraint-Lösung)
- **LOD/Konsistenz (Q294, Q295):** Wenig Neues für FF1. Neu sind `zahedi2022bim` (Entscheidungsdokumentation, FF4) und `mellenthinfilardo2026requirements`† (AIA in Deutschland).
- **Q110 (Lieferkette, Marketing)** liefert nichts für FF1, FF2 oder FF4.

## 4 PRISMA-Zahlen dieser Runde

| Schritt | Anzahl | Anmerkung |
|---|---|---|
| Datensätze gesichtet | **2 800** | OpenAlex rückwärts 490 + vorwärts 1 938; Volltext-Referenzlisten 244 (Q014: 9, Q234: ca. 235); Q384 vorwärts über Handbuch 128 |
| − Dubletten innerhalb der Runde | 410 | gleiche Arbeit von mehreren Startquellen/Richtungen (nur OpenAlex-Listen maschinell abgeglichen) |
| − Dubletten zum Bestand (`quellen-master.csv`) | 99 | OpenAlex 84 (DOI/Titel), Q014 3, Q234 ≥ 12 (Titelabgleich, Untergrenze) |
| = Titel-Screening | **2 291** | Titel (und Venue) gegen FF1, FF2, FF4 |
| → Abstract-Prüfung | **211** | 201 aus OpenAlex-Listen + 10 aus Volltext/Handbuch; Abstracts über OpenAlex, sonst Verlagsseite |
| − ausgeschlossen | 100 | Relevanz < 2: 83; Preprint ohne Begutachtung (SSRN): 8; Vorfassung oder Teil eines Bestandswerks: 4; Venue/Existenz nicht verifizierbar: 4; Hochschulschrift ohne Begutachtung: 1 |
| = **aufgenommen** | **111** (106 in Teil A, 5 † in Teil B) | davon ff1 ≥ 2: 43, ff2 ≥ 2: 77, ff4 ≥ 2: 19; Relevanz 3 in mindestens einer FF: 10 |

Verifikation der 111: 108 über Crossref (DOI, Autoren, Venue, Band, Seiten), 1 über DataCite (Hochschulschrift Alberta), 2 über die Verlagsseite ITcon (ohne DOI).

**Ausgeschlossen, aber als Hinweis festgehalten** (nicht zitierfähig nach 2a.4):

- *SSRN-Preprints* (nicht begutachtet), bei späterer Begutachtung erneut prüfen:
  - Barcelos & Isatto 2026, „Operationalizing automated compliance checking in an openBIM environment: a framework for planning approval in the public sector“ (FF2/FF4 potenziell 2)
  - Muniz, Granja & Azenha 2025 (Open-Source-Prüfanwendung für den digitalen Bauantrag)
  - Karmakar et al. 2025/2026 (Begründungen im Genehmigungsverfahren mit RAG und Human-in-the-Loop)
  - Dridi, Patlakas et al. 2024 (AEC3PO)
  - Huitzil et al. 2026 (SmartNorms4BIM)
  - Yamusa et al. 2024 (ACC-Review)
  - Borkowski & Michalak 2026 (IFC2COBie mit Provenienz)
- *Vorfassungen oder Teile von Bestandswerken:*
  - Kapitel „Prüfung der Einhaltung von Normen und Richtlinien mittels BIM“ (VDI-Buch 2021 = Kapitel von `borrmann2021bim`; Fassung 2015)
  - Zhang, Beetz & Weise 2014, ECPPM (Tagungsfassung zu `zhang2015interoperable`)
  - Kincelova et al. 2019 (Tagungsfassung zu `kincelova2020fire`)
- *Nicht verifizierbar:*
  - Dimyadi & Amor 2013, „Automated Building Code Compliance Checking – Where is it at?“: DOI nur bei ResearchGate, laut DataCite „Unpublished“, Tagungsband nicht bestätigt
  - Exner et al. 2019 (Entwurfsvarianten, mediaTUM, Tagung nicht bestätigt)
  - Veliz, Medjdoub & Kocatürk 2011 (Buchkapitel, Band nicht bestätigt)
  - „Methodologies for requirement checking on building models“ (2016, nicht auflösbar)
- *Graue Literatur:* Stocker 2021, TUM, „Erstellung von IFC-Datenmodellen für den Holzbau und darauf basierende automatisierte Überprüfung der Einhaltung von Schallschutzanforderungen“. Studienabschlussarbeit (Betreuung Châteauvieux-Hellwig, Abualdenien; mediaTUM 1633174). Für 8.2 als Art G nutzbar.

## 5 Aufgenommene Quellen

Einteilung nach Schwerpunkt: Jede Quelle erscheint einmal. Zuerst alle mit ff4 ≥ 2, dann FF1, dann FF2. Relevanzwerte sind vorläufig (Einzelbewertung nach Titel und Abstract, kein Volltext). Sie müssen vor Übernahme in `quellen-bewertung.csv` mit `qualitaet`, `uebertragbarkeit` und P ergänzt werden. „Schneeball von“: Startquelle, v = vorwärts, r = rückwärts.

#### FF4 – Verantwortung, Freigabe, Nachvollziehbarkeit (ff4 ≥ 2) (19)

| Key | Jahr | Titel | Venue | Schneeball von | ff1/ff2/ff4 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `urban2026development` | 2026 | Development of openBIM based building code compliance checks: Case study in the City of Vienna | Building Research & Information | Q001 v | 0/3/2 | Methodik zur Entwicklung und Validierung von Prüfregeln im realen Genehmigungsprozess (Wien) |
| `alhasan2026blockchain` | 2026 | Blockchain-Enhanced Construction Records: Transforming Evidentiary Standards and Dispute Resolution in International Arbitration | Journal of Legal Affairs and Dispute Resolution in Engineering and Construction | Q017 v | 0/0/2 | Blockchain-gestützte Bauaufzeichnungen und ihr Beweiswert im Streitfall |
| `benghi2019automated` | 2019 | Automated verification for collaborative workflows in a Digital Plan of Work | Automation in Construction | Q001 v, Q002 v, Q261 v | 2/0/2 | automatische Verifikation kollaborativer Workflows im Digital Plan of Work (Phasen und Gates) |
| `bloch2023unbalanced` | 2023 | The unbalanced research on digitalization and automation of the building permitting process | Advanced Engineering Informatics | Q001 v | 0/2/2 | Stakeholder, Zuständigkeiten und Forschungslücken im Genehmigungsprozess |
| `fauth2023ontology` | 2023 | Ontology for building permit authorities (OBPA) for advanced building permit processes | Advanced Engineering Informatics | Q001 v | 0/2/2 | Ontologie für Bauaufsichtsbehörden (OBPA) |
| `fauth2023understanding` | 2023 | Understanding processes on digital building permits – a case study in South Tyrol | Building Research & Information | Q001 v | 0/1/2 | Prozessanalyse digitaler Bauantrag (Südtirol): Schritte, Rollen und Verantwortungen der Behörde |
| `gade2021exploration` | 2021 | Exploration of practitioner experiences of flexibility and transparency to improve BIM-based model checking systems | Journal of Information Technology in Construction | Q001 v | 0/2/2 | Praxisstudie: Transparenz und Flexibilität als Bedingung für Akzeptanz von Model Checking |
| `garcia2026ifc` | 2026 | From IFC validation to publish/hold decisions: A tool-independent quality-gating framework for railway depots | Advanced Engineering Informatics | Q002 v | 1/2/2 | werkzeugunabhängiges Freigabe-Gate (publish/hold) nach IFC-Validierung |
| `li2020qualitative` | 2020 | Qualitative and Traceable Calculations for Building Codes | CIB W78 Proceedings | Q001 v, Q002 v | 0/2/2 | qualitative und nachvollziehbare Berechnungen für Bauvorschriften; Baustein für die Nachweisführung (7a) |
| `mastrolemboventura2025digital` | 2025 | Towards Digital Building Permits: a review of European strategies and relevant literature | TECHNE - Journal of Technology for Architecture and Environment | Q001 v | 0/2/2 | europäische Strategien zum digitalen Bauantrag (Horizon-Projekte) |
| `meda2024twinning` | 2024 | Twinning the path of digital building permits and digital building logbooks – Diagnosis and challenges | Developments in the Built Environment | Q001 v | 2/0/2 | Verknüpfung digitaler Bauantrag und digitales Gebäudelogbuch (EU-Kontext) |
| `mellenthinfilardo2026requirements`† | 2026 | Information requirements for BIM: Current practice and implementation in Germany | Journal of Information Technology in Construction | Q295 v | 2/0/2 | Informationsanforderungen (AIA) in Deutschland und ihre vertragliche Bindung |
| `pinto2026exhaustive` | 2026 | Exhaustive Differential Verification of Rule Execution in Building Compliance Software: A Method and Its Application to Seismic Provisions for Earthen Buildings | Buildings | Q001 v | 0/2/2 | differenzielle Verifikation der Regelausführung: prüft, ob Prüfsoftware richtig urteilt |
| `purushotham2026automated` | 2026 | Framework for automated building code compliance checking to improve transparency, trust, validation, and design interpretation | Automation in Construction | Q260 v | 0/2/2 | ACC mit Transparenz, Vertrauen und Validierung: nachvollziehbare Prüfergebnisse |
| `shahi2019automated` | 2019 | Framework for Automated Model-Based e-Permitting System for Municipal Jurisdictions | Journal of Management in Engineering | Q001 v, Q002 v | 0/2/2 | Rahmen für modellbasiertes e-Permitting in Kommunen |
| `shi2018ifcdiff` | 2018 | IFCdiff: A content-based automatic comparison approach for IFC files | Automation in Construction | Q001 v | 2/0/2 | IFCdiff: inhaltlicher Vergleich von IFC-Ständen; Änderungsnachweis zwischen Freigabeständen |
| `sobral2026challenges` | 2026 | Challenges of current regulations for building permits under digitalisation: a Portuguese case-based analysis | Building Research & Information | Q001 v, Q002 v | 0/2/2 | Auslegungsprobleme von Bauvorschriften im digitalen Bauantrag (Portugal) |
| `urban2024adapting` | 2024 | Adapting to an OpenBIM Building Permit Process: A Case Study Using the Example of the City of Vienna | Buildings | Q017 r | 0/2/2 | openBIM-Bauantragsprozess der Stadt Wien |
| `zahedi2022bim` | 2022 | BIM-based design decisions documentation using design episodes, explanation tags, and constraints | Journal of Information Technology in Construction | Q001 v, Q294 v | 1/0/2 | Dokumentation von Entwurfsentscheidungen mit Begründung und Constraints im BIM (TUM): Nachvollziehbarkeit |

#### FF1 – Informationsmodell, Vorfertigung, Ableitungen (37)

| Key | Jahr | Titel | Venue | Schneeball von | ff1/ff2/ff4 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `abushwereb2019framework` | 2019 | Framework for automated manufacturing-centric BIM for light wood frame buildings | University of Alberta (Hochschulschrift) | Q240 v | 3/1/0 | regelbasierte Fertigungsdetaillierung von Holzrahmenwänden nach Bauordnung, inkl. Transportregeln |
| `darwish2022automated` | 2022 | Automated BIM-based CNC file generator for wood panel framing machines in construction manufacturing | Modular and Offsite Construction (MOC) Summit Proceedings | Q234 r | 3/0/0 | CNC-Dateien für Wandtafel-Anlagen direkt aus BIM: Muster für WUP/BTLx als Ableitung |
| `vestin2022information` | 2022 | Information Management in the Wooden Single-Family House Industry – Challenges and Potential Solutions | SPS2022 | Q243 v | 3/0/0 | Informationsmanagement in der Holz-Einfamilienhausindustrie |
| `abualdenien2020consistent`† | 2020 | Consistent management and evaluation of building models in the early design stages | Journal of Information Technology in Construction | Q295 r | 2/0/0 | konsistentes Management früher Entwurfsvarianten |
| `cao2021cross` | 2021 | Cross-phase product configurator for modular buildings using kit-of-parts | Automation in Construction | Q248 r | 2/2/0 | phasenübergreifender Produktkonfigurator (Kit-of-parts) |
| `comai2026definition` | 2026 | Definition of standardized GeoBIM information requirements for digital building permits | Building Research & Information | Q002 v, Q295 v | 2/2/0 | standardisierte GeoBIM-Informationsanforderungen für den digitalen Bauantrag |
| `day2019knowledge` | 2019 | Knowledge-Based Design in Industrialised House Building: A Case-Study for Prefabricated Timber Walls | Digital Wood Design | Q234 r | 2/2/0 | wissensbasierter Entwurf vorgefertigter Holzwände im industriellen Hausbau |
| `eastman2010exchange` | 2010 | Exchange Model and Exchange Object Concepts for Implementation of National BIM Standards | Journal of Computing in Civil Engineering | Q243 r | 2/0/0 | Exchange Model und Exchange Object für nationale BIM-Standards |
| `gharaibeh2023digital` | 2023 | Digital transformation of the wood construction supply chain through building information modelling: current state of practice | Construction Innovation | Q240 v | 2/0/0 | BIM in der schwedischen Holzbau-Lieferkette |
| `hagedorn2023semantic` | 2023 | Semantic rule checking of cross-domain building data in information containers for linked document delivery using the shapes constraint language | Automation in Construction | Q001 v, Q002 v | 2/2/0 | SHACL-Prüfung domänenübergreifender Daten in ICDD-Containern: Dokumente neben IFC prüfbar verknüpfen |
| `he2021bim` | 2021 | BIM-enabled computerized design and digital fabrication of industrialized buildings: A case study | Journal of Cleaner Production | Q247 r | 2/0/0 | BIM-gestützter Entwurf und digitale Fertigung industrieller Gebäude |
| `jalaliyazdi2021clt`† | 2021 | Mass-customisation of cross-laminated timber wall systems at early design stages | Automation in Construction | Q208 v | 2/2/0 | Mass Customization von BSP-Wandsystemen mit Fertigungsregeln im Frühentwurf |
| `jansson2019breakdown` | 2019 | Breakdown Structure in the Digitalization of Design Work for Industrialized House-Building: A Case Study of Systems Building Using Predefinition Levels of Product Platforms | ICCREM 2019 | Q224 r | 2/0/0 | Produktstruktur und Vordefinitionsebenen in Plattformen des industriellen Hausbaus |
| `kim2024rule` | 2024 | Rule-based automation algorithm for generating 2D deliverables from BIM | Journal of Building Engineering | Q240 v | 2/0/0 | regelbasierte Erzeugung von 2D-Plänen aus BIM: Bauvorlagen als Ableitung |
| `laakso2012ifc` | 2012 | The IFC standard: a review of history, development, and standardization | ITcon 17 | Q243 r | 2/0/0 | Standardisierungsgeschichte von IFC und buildingSMART; Kontext für 5.1 und die Schemawahl |
| `le2020hitos` | 2020 | The HITOS project – A full scale IFC test | eWork and eBusiness in Architecture, Engineering and Construction | Q001 r | 2/1/0 | HITOS: vollständiger IFC-Pilot mit Regelprüfung |
| `lee2016modularized` | 2016 | Modularized rule-based validation of a BIM model pertaining to model views | Automation in Construction | Q001 v | 2/2/0 | modularisierte Validierung gegen Model Views |
| `lee2016ontology` | 2016 | An ontology-based approach for developing data exchange requirements and model views of building information modeling | Advanced Engineering Informatics | Q001 v | 2/0/0 | ontologiebasierte Entwicklung von Austauschanforderungen und Model Views |
| `lee2019mechanism` | 2019 | The Mechanism and Challenges of Validating a Building Information Model regarding data exchange standards | Automation in Construction | Q001 v | 2/2/0 | Mechanismen und Grenzen der Validierung gegen Austauschstandards |
| `liu2016ontology` | 2016 | Ontology-based semantic approach for construction-oriented quantity take-off from BIM models in the light-frame building industry | Advanced Engineering Informatics | Q234 r | 2/0/0 | ontologiebasierte Mengenermittlung aus BIM im Holzrahmenbau (Light-Frame) |
| `liu2021bim` | 2021 | BIM-BVBS integration with openBIM standards for automatic prefabrication of steel reinforcement | Automation in Construction | Q243 v | 2/0/0 | BVBS-Fertigungsdaten aus openBIM: Muster für BTLx/WUP als Ableitung |
| `liu2023definition` | 2023 | Definition of a container-based machine-readable IDM integrating level of information needs | Proceedings of the 2023 European Conference on Computing in Construction and the 40th International CIB W78 Conference | Q017 r | 2/2/0 | maschinenlesbares IDM mit Level of Information Need im Container |
| `loboscalquin2024implementation` | 2024 | Implementation of Building Information Modeling Technologies in Wood Construction: A Review of the State of the Art from a Multidisciplinary Approach | Buildings | Q240 v | 2/0/0 | Review BIM im Holzbau |
| `mtehrani2025streamlining` | 2025 | Streamlining design-to-manufacturing for assembly-based robotics in wood panel framing tasks of industrialized construction: Introducing a BIM-to-BoT (B2B) framework | Advanced Engineering Informatics | Q240 v | 2/0/0 | BIM-to-Bot für die Wandtafelfertigung im Holzrahmenbau: Ableitung von Maschinendaten |
| `nawari2012bim` | 2012 | BIM Standard in Off-Site Construction | Journal of Architectural Engineering | Q243 r | 2/0/0 | BIM-Standard in der Vorfertigung |
| `nawari2012standardization` | 2012 | BIM Standardization and Wood Structures | Computing in Civil Engineering (2012) | Q247 r | 2/0/0 | BIM-Standardisierung und Holzkonstruktionen |
| `paskoff2023bim` | 2023 | BIM-Based Checking Method for the Mass Timber Industry | Buildings | Q001 v | 2/2/0 | Prüfmethode für Holzmodelle mit Vorfertigungsbezug |
| `patlakas2015potential` | 2015 | The Potential, Requirements, and Limitations of BIM for Offsite Timber Construction | International Journal of 3-D Information Modeling | Q247 r | 2/0/0 | Potenzial und Grenzen von BIM für die Holz-Vorfertigung |
| `piazzi2022graphical`† | 2022 | An investigation of concepts for the specification of graphical exchange information requirements in building information modelling | Journal of Information Technology in Construction | Q294 v | 2/0/0 | Spezifikation grafischer Informationsanforderungen |
| `plume2007collaborative` | 2007 | Collaborative design using a shared IFC building model—Learning from experience | Automation in Construction | Q001 r | 2/0/0 | Erfahrungen mit einem gemeinsam genutzten IFC-Modell |
| `ramaji2016product` | 2016 | Product Architecture Model for Multistory Modular Buildings | Journal of Construction Engineering and Management | Q224 r | 2/0/0 | Produktarchitekturmodell modularer Mehrgeschosser |
| `ramaji2017extending` | 2017 | Extending the current model view definition standards to support multi-storey modular building projects | Architectural Engineering and Design Management | Q243 v | 2/0/0 | MVD-Erweiterung für modulare Mehrgeschosser |
| `rojas2025impact` | 2025 | Impact of Using an Exchange Model (EM) to Support the Early Assessment Process of Industrialized Timber Projects | Buildings | Q247 v | 2/0/0 | Exchange Model für die frühe Bewertung industrieller Holzbauprojekte (Folgearbeit zu Q247) |
| `slepicka2022fabrication` | 2022 | Fabrication information modeling: interfacing building information modeling with digital fabrication | Construction Robotics | Q294 v | 2/0/0 | Fabrication Information Modeling: BIM und digitale Fertigung |
| `venugopal2012semantics` | 2012 | Semantics of model views for information exchanges using the industry foundation class schema | Advanced Engineering Informatics | Q247 r | 2/0/0 | Semantik von Model Views für IFC-Austausch |
| `wongchong2021logic` | 2021 | Logic representation and reasoning for automated BIM analysis to support automation in offsite construction | Automation in Construction | Q240 v | 2/2/0 | Logik und Reasoning für automatisierte BIM-Analysen in der Vorfertigung |
| `yin2019building` | 2019 | Building information modelling for off-site construction: Review and future directions | Automation in Construction | Q240 v, Q243 v, Q247 r | 2/0/0 | Review BIM für die Vorfertigung |

#### FF2 – Regelformalisierung, ACC, IDS, digitaler Bauantrag (55)

| Key | Jahr | Titel | Venue | Schneeball von | ff1/ff2/ff4 | Kurzbegründung |
|---|---|---|---|---|---|---|
| `fischer2024extending` | 2024 | Extending Information Delivery Specifications for digital building permit requirements | Developments in the Built Environment | Q001 v, Q017 r | 0/3/0 | IDS-Erweiterung für Bauantragsanforderungen |
| `fuchs2025exploring` | 2025 | Exploring the potential of parallel drafting of building regulations | Advanced Engineering Informatics | Q001 v, Q002 v | 0/3/0 | paralleles Verfassen von Bauvorschriften in natürlicher und formaler Sprache: compliance-by-design an der Quelle |
| `narayanaswamy2019bim` | 2019 | BIM-based Automated Design Checking for Building Permit in the Light-Frame Building Industry | Proceedings of the 36th International Symposium on Automation and Robotics in Construction (ISARC) | Q002 v | 2/3/0 | BIM-basierte Bauantragsprüfung im Holzrahmenbau (Light-Frame) |
| `niemeijer2014freedom` | 2014 | Freedom through constraints: User-oriented architectural design | Advanced Engineering Informatics | Q001 v, Q009 v, Q262 v | 0/3/0 | Freedom through constraints: nutzerorientiertes Entwerfen im Regelraum |
| `noardo2022ifc` | 2022 | IFC models for semi-automating common planning checks for building permits | Automation in Construction | Q001 v, Q009 v | 2/3/1 | GeoBIM-Benchmark: halbautomatische Bauantragsprüfungen an realen Architektenmodellen; Modellqualität als Engpass |
| `nuyts2024comparative` | 2024 | Comparative analysis of approaches for automated compliance checking of construction data | Advanced Engineering Informatics | Q017 r | 0/3/0 | Vergleich von ACC-Ansätzen (u. a. IDS, SHACL) an denselben Anforderungen |
| `ataide2023digital` | 2023 | Digital Transformation of Building Permits: Current Status, Maturity, and Future Prospects | Buildings | Q001 v | 0/2/1 | Reifegrad der Digitalisierung von Baugenehmigungen |
| `battisti2022automatic` | 2022 | An Automatic Process for the Application of Building Permits | Buildings | Q001 v | 1/2/1 | deutscher Beitrag zu einem durchgängigen, medienbruchfreien Bauantragsprozess auf BIM-Basis |
| `beach2024digital` | 2024 | Digital approaches to construction compliance checking: Validating the suitability of an ecosystem approach to compliance checking | Advanced Engineering Informatics | Q260 v | 0/2/0 | Ökosystem-Ansatz für die Compliance-Prüfung |
| `bogaerts2021step` | 2021 | A framework for step-wise explaining how to solve constraint satisfaction problems | Artificial Intelligence | Q384 v | 0/2/1 | schrittweise Erklärung von Constraint-Lösungen: Baustein für "Ablehnen mit Begründung" (9.5) |
| `borrmann2009topological` | 2009 | Topological analysis of 3D building models using a spatial query language | Advanced Engineering Informatics | Q002 r | 0/2/0 | räumliche Anfragesprache für topologische Prüfungen |
| `cerovsek2025advancing` | 2025 | Advancing Semantic Enrichment Compliance in BIM: An Ontology-Based Framework and IDS Evaluation | Buildings | Q001 v, Q002 v, Q009 v, Q017 v | 0/2/0 | Evaluation von IDS für semantische Anreicherung |
| `demarco2024enriching` | 2024 | Enriching Building Information Modeling Models through Information Delivery Specification | Buildings | Q017 r | 1/2/0 | IDS zur Anreicherung von BIM-Modellen |
| `dimyadi2016computerizing` | 2016 | Computerizing Regulatory Knowledge for Building Engineering Design | Journal of Computing in Civil Engineering | Q001 v, Q009 v | 0/2/0 | Computerisierung regulatorischen Wissens für die Prüfung |
| `donath2008constraint` | 2008 | Constraint-Based Design in Participatory Housing Planning | International Journal of Architectural Computing | Q261 r | 0/2/0 | constraint-basiertes partizipatives Wohnungsentwerfen |
| `doukari2022object` | 2022 | Object-centred automated compliance checking: a novel, bottom-up approach | Journal of Information Technology in Construction | Q001 v, Q002 v, Q260 v | 1/2/0 | objektzentrierte, bottom-up Anforderungsprüfung; nah an der IDS-Logik (Anforderung je Objekt) |
| `fonsati2026leveraging` | 2026 | Leveraging OpenBIM standards and information delivery specification (IDS) for digital validation in circular construction: reusing hollow core slabs | Smart and Sustainable Built Environment | Q001 v | 1/2/0 | IDS-Validierung von IFC-Modellen in der Praxis (Wiederverwendung von Hohldielen) |
| `hosseinigourabpasi2025developing` | 2025 | Developing an openBIM Information Delivery Specifications Framework for Operational Carbon Impact Assessment of Building Projects | Sustainability | Q017 r | 0/2/0 | openBIM-IDS-Framework für Betriebs-CO2-Bewertung |
| `jedrzejewska2026eurocode` | 2026 | Eurocode Core Ontology: Building the semantic framework for structural design assistants | Advanced Engineering Informatics | Q260 v | 0/2/0 | Eurocode-Kernontologie: Grundlage für EC5-Regeln |
| `khaliliaraghi2020variability` | 2020 | Variability and validity: Flexibility of a dimensional customization system | Automation in Construction | Q224 r | 0/2/0 | Variabilität und Gültigkeit einer Maßanpassung (Folgearbeit zu Q215) |
| `kincelova2020fire` | 2020 | Fire Safety in Tall Timber Building: A BIM-Based Automated Code-Checking Approach | Buildings | Q001 v, Q002 v | 0/2/0 | BIM-basierte Brandschutzprüfung für Holzgebäude; direkter Holzbaubezug |
| `kremer2023extending` | 2023 | Extending - information delivery specification - for linking distributed model checking services | Proceedings of the 2023 European Conference on Computing in Construction and the 40th International CIB W78 Conference | Q017 r | 0/2/0 | IDS-Erweiterung für verteilte Prüfdienste |
| `kwiecinski2014system` | 2014 | System for customer participation in the design process of mass-customized houses | Proceedings of the 32nd International Conference on Education and Research in Computer Aided Architectural Design in Europe (eCAADe) [Volume 2] | Q212 r | 0/2/0 | Kundenbeteiligung am Entwurf vorgefertigter Häuser |
| `kwiecinski2018hopla` | 2018 | HOPLA - Interfacing Automation for Mass-customization | Proceedings of the 36th International Conference on Education and Research in Computer Aided Architectural Design in Europe (eCAADe) [Volume 2] | Q212 v, Q215 v | 0/2/0 | HOPLA: Kundenplanung innerhalb von Regeln |
| `lee2016translating` | 2016 | Translating building legislation into a computer-executable format for evaluating building permit requirements | Automation in Construction | Q260 r | 0/2/0 | Übersetzung von Baurecht in ausführbare Form für Bauantragsanforderungen |
| `lee2020comparative` | 2020 | A Comparative Analysis of Five Rule-Based Model Checking Platforms | Construction Research Congress 2020 | Q001 v | 0/2/0 | Vergleich von fünf regelbasierten Prüfplattformen |
| `lee2026automated` | 2026 | Automated compliance checking across the building lifecycle: Systematic and semantic review integrating PRISMA and deep search | Automation in Construction | Q001 v, Q260 v | 0/2/0 | systematischer Review ACC über den Lebenszyklus |
| `liu2022mvdlite` | 2022 | MVDLite: a Fast Validation Algorithm for Model View Definition Rules | Proceedings of the 29th EG-ICE International Workshop on Intelligent Computing in Engineering | Q001 v | 1/2/0 | MVDLite: schnelle Validierung von MVD-Regeln; Referenzpunkt für die IDS-Validierung |
| `macitilal2017computer` | 2017 | Computer representation of building codes for automated compliance checking | Automation in Construction | Q001 v, Q002 v | 0/2/0 | Repräsentation von Bauvorschriften für ACC |
| `malsane2015development` | 2015 | Development of an object model for automated compliance checking | Automation in Construction | Q001 v | 1/2/0 | Objektmodell für die automatisierte Konformitätsprüfung |
| `marcellino2026enhancing` | 2026 | Enhancing Computational Compliance Checking in Healthcare Facilities Through the IDS Standard | Buildings | Q001 v, Q002 v | 0/2/0 | IDS für regulatorische Anforderungen im Gesundheitsbau |
| `mazairac2013bimql` | 2013 | BIMQL – An open query language for building information models | Advanced Engineering Informatics | Q260 r | 0/2/0 | BIMQL: offene Anfragesprache für BIM |
| `mcgibbney2013intelligent` | 2013 | An intelligent authoring model for subsidiary legislation and regulatory instrument drafting within construction and engineering industry | Automation in Construction | Q001 v | 0/2/0 | Autorensystem für Verordnungstexte: Regeln bereits bei der Erstellung maschinenlesbar |
| `napps2026digitalizing` | 2026 | Digitalizing workplace safety regulations for rule-based validation of escape routes and movement areas in BIM | Automation in Construction | Q001 v | 0/2/0 | Digitalisierung der Arbeitsstättenregeln für die regelbasierte Fluchtwegprüfung (deutsche Regelwerke) |
| `nassar2003building` | 2003 | Building assembly detailing using constraint-based modeling | Automation in Construction | Q261 r | 1/2/0 | constraint-basierte Detaillierung von Bauteilanschlüssen |
| `patlakas2018automatic` | 2018 | Automatic code compliance with multi-dimensional data fitting in a BIM context | Advanced Engineering Informatics | Q234 r, Q001 v | 0/2/0 | automatische Normprüfung von Holzverbindungen (EC5) im BIM-Kontext |
| `pauwels2017performance` | 2017 | A performance benchmark over semantic rule checking approaches in construction industry | Advanced Engineering Informatics | Q001 v | 0/2/0 | Leistungsvergleich semantischer Regelprüfverfahren |
| `pichler2012imperative` | 2012 | Imperative versus Declarative Process Modeling Languages: An Empirical Investigation | Business Process Management Workshops | Q014 r | 0/2/0 | imperative vs. deklarative Modellierungssprachen (empirisch): Begründung für die Wahl der Regelsprache (IDS deklarativ, Regelmaschine imperativ) |
| `preidel2016towards` | 2016 | Towards code compliance checking on the basis of a visual programming language | ITcon 21 | Q260 r | 0/2/0 | transparente statt Black-Box-Regeln (VCCL, TUM); Zeitschriftenfassung zu Bestandsquellen |
| `senousy2026automated` | 2026 | Automated compliance checking in AEC in the era of AI and LLMs: A review (2022–2025) | Automation in Construction | Q001 v, Q002 v, Q260 v | 0/2/0 | Review ACC mit KI/LLM 2022-2025; aktueller Stand für Kap. 5.2 |
| `sobhkhiz2021framing` | 2021 | Framing and Evaluating the Best Practices of IFC-Based Automated Rule Checking: A Case Study | Buildings | Q001 v, Q002 v | 0/2/0 | kritisiert die Trennung von Entwurf und Prüfung; stützt Prüfung während des Entwurfs (Echtzeit-Begrenzung) |
| `sun2026global` | 2026 | Global advancements in BIM-based building e-permit system adoption: a review | Journal of Civil Engineering and Management | Q001 v | 0/2/1 | Review BIM-basierter e-Permit-Systeme weltweit |
| `tomczak2024requiring` | 2024 | Requiring Circularity Data in BIM With Information Delivery Specification | Journal of Circular Economy | Q017 r | 0/2/0 | IDS für Zirkularitätsdaten |
| `tonguc2026code` | 2026 | CODE-COMPANION: A Cross-Platform Computational Framework for Real-Time BIM Compliance Checking and Digital Building Permit Workflows | Buildings | Q001 v, Q002 v, Q017 v | 0/2/0 | Echtzeit-Prüfung im Entwurf, gekoppelt an den Bauantrags-Workflow |
| `vareilles2013renovation`† | 2013 | Configuration of high performance apartment buildings renovation: A constraint based approach | 2013 IEEE International Conference on Industrial Engineering and Engineering Management | Q384 v | 0/2/0 | Konfiguration von Sanierungselementen als Constraint-Problem (Soft/Hard Constraints im Gebäudekonfigurator) |
| `viking2015exploring` | 2015 | Exploring industrialized housebuilders’ interpretations of local requirements using institutional logics | Construction Management and Economics | Q224 r | 0/2/1 | Auslegung lokaler Anforderungen durch Industriehausbauer |
| `wu2025design` | 2025 | Design Healing framework for automated code compliance | Automation in Construction | Q001 v, Q260 v | 0/2/0 | Design Healing: automatische Korrekturvorschläge nach der Prüfung; stützt 9.5 Ablehnen mit Alternative |
| `wu2026revisiting` | 2026 | The Beginning, Not the End: Revisiting Automated Compliance Checking for BIM-Based Design Adaptation | Computing in Civil Engineering 2025 | Q001 v, Q002 v, Q260 v | 0/2/0 | ACC als Ausgangspunkt der Entwurfsanpassung (TUM) |
| `zentgraf2023concept` | 2023 | Concept for Enriching NISO-STS Standards with Machine-Readable Requirements and Validation Rules | CONVR 2023 - Proceedings of the 23rd International Conference on Construction Applications of Virtual Reality | Q001 v | 0/2/0 | maschinenlesbare Anforderungen und Prüfregeln in NISO-STS-Normen (DIN-Normformat): Brücke Norm zu Prüfregel |
| `zhang2017logic` | 2017 | A logic-based representation and tree-based visualization method for building regulatory requirements | Visualization in Engineering | Q001 v, Q009 v | 0/2/1 | verständliche, baumbasierte Darstellung von Regelanforderungen |
| `zhang2021clustering` | 2021 | Clustering-Based Approach for Building Code Computability Analysis | Journal of Computing in Civil Engineering | Q001 v, Q002 v | 0/2/0 | Clusteranalyse der Berechenbarkeit von Normanforderungen; stützt Aufteilung IDS / Regelmaschine / manuell |
| `zhang2023capabilities` | 2023 | Capabilities of rule representations for automated compliance checking in healthcare buildings | Automation in Construction | Q001 v, Q002 v, Q009 v | 0/2/0 | vergleicht Regelrepräsentationen nach Ausdrucksfähigkeit; Kriterien für die Wahl IDS vs. Regelsprache |
| `zhang2023rule` | 2023 | Rule capture of automated compliance checking of building requirements: a review | Proceedings of the Institution of Civil Engineers - Smart Infrastructure and Construction | Q001 v, Q002 v, Q260 v | 0/2/0 | Review der Regelerfassung für ACC |
| `zhang2023unpacking` | 2023 | Unpacking Ambiguity in Building Requirements to Support Automated Compliance Checking | Journal of Management in Engineering | Q001 v, Q009 v, Q260 v | 0/2/0 | Mehrdeutigkeit in Anforderungen als Hürde der Formalisierung |
| `zheng2026translating` | 2026 | Translating regulatory clauses into executable codes for building design checking via large language model driven function matching and composing | Engineering Applications of Artificial Intelligence | Q001 v, Q002 v, Q260 v | 0/2/0 | LLM übersetzt Klauseln in ausführbare Prüffunktionen; Abgrenzung zu "KI versteht, Code entscheidet" |

## 6 Sättigung: Ist eine zweite Runde nötig?

**Ja.** Nach 2a.3 Nr. 3 endet das Verfahren erst, wenn eine Runde keine neue Quelle mit Relevanz ≥ 2 mehr liefert. Runde 1 liefert 111 solche Quellen. Die Sättigung ist aber je Forschungsfrage verschieden:

- **FF2 (Regelformalisierung, ACC, IDS, digitaler Bauantrag): nicht gesättigt.** Der Ertrag stammt überwiegend aus den Jahren 2022 bis 2026 (IDS, digitaler Bauantrag, LLM-gestützte Formalisierung). Diese Arbeiten sind selbst noch wenig zitiert, ihr Umfeld wächst schnell. Klassische Referenzlisten (Eastman, Solihin) liefern dagegen fast nur Bekanntes oder Historisches (Relevanz 1). Rückwärts ist die ACC-Grundlagenliteratur weitgehend gesättigt, vorwärts nicht.
- **FF1 (durchgängiges Modell bis Fertigung/Bauantrag): teilweise gesättigt.** MVD-/Exchange-Model-Grundlagen und Reviews zur Vorfertigung wiederholen sich bereits über mehrere Startquellen (z. B. `yin2019building` über Q240, Q243 und Q247). Neu und dünn besetzt ist die Ableitung von Maschinendaten für Holzrahmen-Wandanlagen: `darwish2022automated`, `mtehrani2025streamlining`, `abushwereb2019framework`. Hier lohnt eine Runde, vor allem über das Alberta-Umfeld (Al-Hussein) und die schwedische Plattformforschung (Jönköping, Luleå).
- **FF4 (Verantwortung, Freigabe, Haftung, Nachvollziehbarkeit): strukturell unterversorgt.** Keine Startquelle hatte ff4 ≥ 2. Die 19 Funde mit ff4 = 2 kommen als Nebenertrag über die Bauantrags-Literatur, keine erreicht ff4 = 3. Das Zitationsnetz der technischen Literatur erreicht deutschsprachige juristische und berufsrechtliche Quellen kaum. Diese Quellen stehen in Kommentaren und Fachzeitschriften ohne DOI oder ohne OpenAlex-Kanten, etwa zu BayBO Art. 61, zur Haftung des Entwurfsverfassers und zur Rolle des Prüfsachverständigen.

**Vorschlag für Runde 2** (nach Einpflegen dieser Runde in `quellen-bewertung.csv`):

1. **Startmenge:** die 10 neuen Quellen mit Relevanz 3
   - `noardo2022ifc`, `urban2026development`, `fuchs2025exploring`, `fischer2024extending`
   - `nuyts2024comparative`, `niemeijer2014freedom`, `narayanaswamy2019bim`
   - `vestin2022information`, `darwish2022automated`, `abushwereb2019framework`

   Dazu die ff4-Funde mit dem stärksten Freigabebezug: `garcia2026ifc`, `benghi2019automated`, `zahedi2022bim`, `purushotham2026automated`, `bloch2023unbalanced`. Jeweils rückwärts und vorwärts.
2. **Nachholen:** rückwärts für Q207, Q233 und Q262 (Volltexte über Fernleihe oder direkte Repositoriumsanfrage); `fauth2024taxonomy` als FF4-Brücke zusätzlich in die Startmenge.
3. **FF4 zusätzlich außerhalb des Schneeballs:** gezielte Recherche in juris/beck-online-Fundstellen, DIBt-/ARGEBAU-Materialien und bei Kammern (Bayerische Architekten- und Ingenieurekammer) zu Freigabe, Unterschrift und digitaler Bauvorlage (Anschluss an Recherche 23).

Erwartung: Für FF1 dürfte Runde 2 nach dem Muster dieser Runde nur noch wenige neue Quellen liefern. Für FF2 ist ein weiterer größerer Ertrag im Bereich IDS/digitaler Bauantrag 2024–2026 zu erwarten, für FF4 nur mit der Zusatzrecherche nach Punkt 3.

## 7 Grenzen dieser Runde

- **Datenbasis OpenAlex:** Referenzlisten sind dort unvollständig aufgelöst (z. B. Q001: 26 `referenced_works`, 19 auflösbar). Tagungsbeiträge ohne DOI fehlen häufig. Semantic Scholar war nicht erreichbar. Der Abgleich mit einer zweiten Zitationsdatenbank steht aus.
- **Vorwärts bei Q384:** nur über das gesamte Handbuch mit Themenfilter (Bauwesen/Architektur). Zitierende des Kapitels „Soft Constraints“ sind darin nicht trennbar.
- **Volltext-Referenzen (Q014, Q234):** maschinell getrennt und von Hand gesichtet. Die Zahl für Q234 (ca. 235) ist über Jahresangaben geschätzt, die Bestandsdubletten (≥ 12) sind eine Untergrenze.
- **Bewertung durch einen Bewerter** (2a.7). Grenzfälle mit Relevanz 2 liegen vor allem bei IDS-Anwendungsstudien (`tomczak2024requiring`, `hosseinigourabpasi2025developing`, `fonsati2026leveraging`) und LLM-Arbeiten (`zheng2026translating`, `tonguc2026code`). Bei der Zweitbewertung für κ bevorzugt prüfen.
- **Crossref-Titel** sind unverändert übernommen, einschließlich Groß-/Kleinschreibung. Akronyme und Eigennamen sind in `{}` geschützt, der Rest nicht angeglichen.

# Recherche 12: Vergleichbare Arbeiten zu Design Automation, Compliance-by-Design, KI/NL, TGA, Dach und Detail

Stand: 27.09.2026. BibTeX: `arbeit/literatur/lit-E-vergleich-automation.bib`.

**Legende**
- **[V]**: Autor, Jahr, Titel und Venue an einer Primärquelle geprüft (Verlagsseite, Repositorium, mediaTUM, ITcon, arXiv-Abstract, GitHub/HF). Die DOI stand dort.
- **[V\*]**: Metadaten an der Primärquelle geprüft. Die DOI stammt aber aus einer Sekundärquelle (Suchzusammenfassung, Literaturliste) oder ist aus der Elsevier-Artikelnummer abgeleitet. Vor der Abgabe noch einmal auflösen.
- **[U]**: unsicher. Etwas Wesentliches ist offen: Venue, DOI, Seiten oder Lizenz.
- **(lit-A)/(lit-B)**: Die Arbeit ist dort schon mit diesem Key erfasst. Der Key wird wiederverwendet und steht nicht noch einmal in lit-E.

**Einschränkung bei der Verifikation:** In dieser Umgebung sind `api.crossref.org`, `api.openalex.org`, `doi.org` und `arxiv.org` (direkt) per Egress-Proxy gesperrt. Crossref- und OpenAlex-Abfragen waren deshalb nicht möglich. Geprüft wurde über Verlags- und Repositoriumsseiten, die per Exa-Suche und WebSearch gefunden wurden. Bei jedem Eintrag steht der Weg im `note`-Feld der .bib. Vor der Einreichung sollte einmal ein Crossref-Batch-Abgleich laufen, vor allem für alle [V\*].

---

## Ergebnis in 5 Punkten

1. **Niemand hat die ganze Kette gebaut.** Keine gefundene Arbeit verbindet Sprache, regelkonforme Erzeugung, ein durchgängiges IFC-Modell mit TGA, Dach und Bemusterung, IDS-Prüfung, Bauantrag und Maschinendaten. Es gibt starke Einzelbausteine:
   - Framing und CNC: Al-Hussein-Gruppe in Alberta
   - TGA-Routing: Medjdoub, Singh/Cheng, Baradaran-Noveiri
   - Dach: Straight Skeleton nach Aichholzer, Laycock, Kelly
   - Sprache zu BIM: Text2BIM, NADIA, MCP4IFC, Hellin
   - Regeln zugleich zum Prüfen und Erzeugen: Sydora & Stroulia
   Die Integrationslücke ist damit belegt und nicht nur behauptet.

2. **Compliance-by-Design gibt es, aber nur in schmalen Nischen.**
   - Sydora & Stroulia (2020) nutzen *eine* Regelsprache zum Prüfen und zum Generieren. Das betrifft aber nur die Innenraummöblierung.
   - FrameX (Abushwereb et al. 2019) erzeugt Holzrahmen „nach Code“, aber nur auf Bauteilebene.
   - Niemeijer (2009, 2011) wollte Kundenänderungen an Fertighäusern gegen Architekten- und Baurechtsregeln prüfen, Mass Customization also. Das ist unser Szenario 15 Jahre früher, nur ohne Generierung.
   - Neuere Arbeiten sind noch Preprints oder Konferenzbeiträge und nicht in Journalen publiziert: D-CodeWeaver 2026, Pang et al. 2026 (SSRN), Kodnongbua et al. 2024 (arXiv).

3. **Das wertvollste Muster für unsere Architektur: „LLM interpretiert, deterministischer Kern verifiziert/erzeugt“.** Es kommt unabhängig voneinander mehrfach vor:
   - Text2BIM: Checker-Feedback-Loop (lit-A/B)
   - Kodnongbua et al.: Gurobi mit IIS-Rückmeldung an das LLM
   - Mirhosseini et al. 2026: IfcOpenShell als „geometry kernel“, laut den Autoren „zero-hallucination“
   - Saluz et al. 2025: OWL-Reasoner
   Das stützt unseren Weg (Intent-Erkennung plus deterministischer Code) methodisch. Der wichtige Unterschied: Bei uns erzeugt das LLM **keinen Code**. Es wählt nur Intents und Parameter.

4. **Wiederverwendbare Assets:**
   - Code: compas_timber (MIT, BTLx), campskeleton (weighted straight skeleton, Java), IfcOpenShell-Voxelisierung für A*-Routing (Issue #6521)
   - Datensätze: **IFC-Bench** mit 1 027 QA-Paaren auf 51 IFC-Modellen, v1 unter CC0; die Frage-Kategorien folgen Solihin & Eastman
   - Evaluationsdesigns:
     - Zeitvergleich manuell gegen Tool (FrameX: −80 %)
     - Round-Trip-Diff über GUIDs (Ma et al. 2006)
     - Benchmark-Modell mit Export-Matrix (Jeong et al. 2009)
     - IoU gegen Ingenieurlösung (StructGAN)
     - pass@k für Codegeneratoren

5. **Warnungen aus der Literatur:**
   - IFC-Round-Trips verlieren nachweislich Semantik: GUIDs, Namen, `IfcRoof`→`IfcSlab`, fehlende Beams (Pazlar & Turk 2008; Ma et al. 2006; Jeong et al. 2009; Noardo et al. 2022). Das passt zu unserer „Single Source of Truth“-These: Das Modell muss *bei uns* führen, nicht in einem Autorentool.
   - Das Multi-LOD-Metamodell von Abualdenien liefert die formale Grundlage für unsere Reifegrade. Es ist aber nur an einem realen Projekt evaluiert und nicht im Fertighauskontext.
   - Holzbau-spezifisches TGA-Routing existiert praktisch nicht. Die einzige Panelbau-Arbeit ist Baradaran-Noveiri 2022, und sie behandelt Lüftungskanäle (GA). Das ist eine echte Forschungslücke.

---

## 1. Vergleichsmatrix

Spalten: Regeln bei Erzeugung? = Regeln wirken *während* der Generierung (nicht nur nachträglich). T/D/Det = TGA / Dach / Detail. Zeilen mit Key aus lit-A/B sind markiert.

| # | Arbeit (Key) | Jahr | Typ | Ansatz | Regeln bei Erzeugung? | IFC? | Sprache/NL? | T/D/Det | Evaluation | Code/Daten/Lizenz |
|---|---|---|---|---|---|---|---|---|---|---|
| 1 | Sydora & Stroulia (`sydora2020rulebased`) [V] | 2020 | Journal (AutCon) | DSL für Innenraumregeln, Checker und Greedy-Generator mit derselben Regelsprache | **ja** | ja (BIM/IFC-Objekte) | nein | Det (Möblierung) | Küchen gegen reale Beispiele, Wohnzimmer gegen Literaturregeln | REST-Toolkit beschrieben, Code nicht gefunden [U] |
| 2 | Niemeijer, de Vries, Beetz (`niemeijer2009checkmate`) [V] | 2009 | Konferenz (CIB W78) | Constraint-Checking auf IFC für Mass Customization im Wohnungsbau, „Puzzle“-DSL | nein (prüft Kundenänderung) | ja (ifcXML) | teilweise (kontrollierte Sprache) | – | Prototyp, Testwohnung | – |
| 3 | Niemeijer (`niemeijer2011constraint`) [V] | 2011 | Dissertation TU/e | NL-Parsing von Architekten-/Baurechts-Constraints (Dachgauben Rotterdam) | nein (explizit nur Checking) | ja | **ja** (NL-Constraint-Eingabe) | D (Gauben) | Usability-Test mit Architekten, Parse-Erfolgsquote | – |
| 4 | Abushwereb, Liu, Al-Hussein (`abushwereb2019knowledge`) [V] | 2019 | Konferenz (MOC Summit) | FrameX: regelbasiertes Wood-Framing als Revit-Add-on (Code, Transport, Best Practice) | **ja** | nein (Revit) | nein | Det (Framing) | Zeitvergleich 60-ft-Wand: −80 % | proprietär |
| 5 | Alwisy et al. (`alwisy2019bimbased`) [V] | 2019 | Journal (IJCM) | MCMPro: 2D-CAD → BIM → Werkstattpläne Holzrahmenpanel | ja (Platform Framing) | nein | nein | Det | Fallbeispiel | proprietär (VBA) |
| 6 | Manrique et al. (`manrique2015automated`) [V\*] | 2015 | Journal (AutCon) | parametrische Werkstattpläne Wood-Framing | ja | nein | nein | Det | Industriepartner | – |
| 7 | Liu, Singh, Lu, Bouferguène, Al-Hussein (`liu2018boarding`) [V\*] | 2018 | Journal (AutCon) | regelbasierte Beplankungs-Layouts und Plattenzuschnitt | **ja** | nein (Revit-API) | nein | Det (Beplankung) | Verschnitt gegen Praxis | – |
| 8 | Liu, Zhang, Lei, Li, Han (`liu2021panelization`) [V] | 2021 | Journal (ACE) | generative Wandpanelisierung plus DES-Produktivitätsbewertung | **ja** (Struktur-, Produktions-, Logistikregeln) | nein | nein | Det | Fallstudie Wohnhaus | – |
| 9 | Sandberg, Johnsson, Larsson (`sandberg2008knowledge`) [V] | 2008 | Journal (ITcon) | KBE im Vertrieb eines Holz-Volumenelement-Herstellers (Treppentool) | ja | nein | nein | Det (Treppe) | Fallstudie Hersteller | – |
| 10 | Jensen, Olofsson, Johnsson (`jensen2012configuration`) **(lit-B)** | 2012 | Journal (AutCon) | Parametrische Konfiguration von Bauteilen (Holzdecke) | ja | nein | nein | Det | Fallstudie | – |
| 11 | Retik & Warszawski (`retik1994automated`) [V] | 1994 | Journal (B&E) | frühes wissensbasiertes Auto-Design Fertigteilbau | ja | nein | nein | Det | Prototyp | – |
| 12 | Gan (`gan2022graph`) [V] | 2022 | Journal (AutCon) | Graph-Datenmodell plus generative Modulbau-Varianten | ja (Topologie-Constraints) | ja (BIM) | nein | – | Varianten/CO₂/Kosten | – |
| 13 | Liao et al. (`liao2021structgan`) [V] | 2021 | Journal (AutCon) | GAN für Wandscheiben-Layouts | nein (lernt aus Plänen) | nein (Bilder) | nein | Det (Tragwerk) | IoU/SWratio gegen Ingenieure | Datensatz nicht offen [U] |
| 14 | Medjdoub & Bi (`medjdoub2018parametric`) [V] | 2018 | Journal (AutCon) | CSP-basiertes Kanalrouting für Fan-Coil-Decken, parametrisch editierbar | **ja** | nein | nein | **T** | Industriepartner-Realfall | – |
| 15 | Singh & Cheng (`singh2021automating`) [V] | 2021 | Konferenz (ICCCBE/LNCE) | Mehrrohr-Routing: gewichteter Graph, Dijkstra / 3D-A\* / FOA plus Simulated Annealing | ja (Kollision, Installation) | ja (BIM) | nein | **T** | Technikraum, 9 Leitungen | – |
| 16 | Choi et al. (`choi2022modification`) [U] | 2022 | Journal (IEEE Access) | modifizierter A\* mit Knotenauswahl und Temp-Grid bei Kollision | ja | ja (BIM) | nein | **T** | 7 Beispielgebäude vs. manuell/kommerziell | – |
| 17 | Baradaran-Noveiri et al. (`baradaran2022parametric`) [V] | 2022 | Journal (JoBE) | GA-Luftkanal-Layout im **Panelbau** mit DfMA und ADPI | ja | nein (Dynamo/Revit) | nein | **T** | 4 Fälle: −23,9 % Kosten, −21,3 % Fertigungszeit | – |
| 18 | Korman, Fischer, Tatum (`korman2003knowledge`) [V] | 2003 | Journal (JCEM) | Wissensbasis MEP-Koordination (Stanford) | teilw. (Regeln für Koordination) | nein | nein | **T** | Expertenwissen, Prototyp | – |
| 19 | Blokland et al. (`blokland2023literature`) [V] | 2023 | Review (ORF) | Taxonomie Pipe Routing: Raum-, Routen-, Ziel-, Constraint-Modell | – | – | – | **T** | Synthesetabelle | Open Access |
| 20 | Aichholzer et al. (`aichholzer1995novel`) [V] | 1995 | Journal (J.UCS) | Straight Skeleton, „kanonisches Dach“ | ja (Geometrie) | – | – | **D** | theoretisch | – |
| 21 | Laycock & Day (`laycock2003automatically`) [V] | 2003 | Konferenz (WSCG) | Walm-, Mansard-, Krüppelwalm-, Satteldach aus Grundriss, rechtwinklige Zerlegung | ja | nein | nein | **D** | Stadtmodell | – |
| 22 | Kelly & Wonka (`kelly2011interactive`) [V] | 2011 | Journal (ACM TOG) | Procedural Extrusions = weighted Straight Skeleton, Gauben, Überstände | ja | nein | nein | **D** | 50 Gebäude, 6 000-Gebäude-Datensatz | campskeleton (Java) auf GitHub, Lizenz [U] |
| 23 | Kelly (`kelly2014unwritten`) [U] | 2014 | Dissertation (Glasgow) | Procedural Modeling mit Straight Skeleton | ja | nein | nein | **D** | – | LaTeX-Quelle auf GitHub |
| 24 | Apolinarska et al. (`apolinarska2016mastering`) [V] | 2016 | Konferenz (AAG) | Sequential Roof: Nagelbild-Algorithmus mit SIA-265-Abstandsellipsen, greedy Nachbemessung | **ja** (Norm im Algorithmus) | nein | nein | **D/Det** | 815 984 Nägel, Holz +13 % statt +59 % | – |
| 25 | Mork (`mork2020parametric`) [U] | 2020 | Masterarbeit | Reindeer: Grasshopper-Toolkit, JointSearch, BTLx-Export | ja | nein | nein | Det (Abbund) | Workflow-Demo | Open Source (Lizenz [U]) |
| 26 | compas_timber (`compastimber`) **(lit-B)** | 2020– | Software | Holzrahmen-Joints, BTLx | ja | nein | nein | Det | – | **MIT** [V, GitHub-API] |
| 27 | Upasani, Shekhawat, Sachdeva (`upasani2020dimensioned`) [V] | 2020 | Journal (AutCon) | Rechteck-Grundrisse per LP aus Rectangular Arrangement plus Min-Breite und Seitenverhältnis | **ja** | nein | nein | – | Laufzeit, Regeneration Palladio | MATLAB-Prototyp, Code [U] |
| 28 | Merrell et al. (`merrell2010computer`) **(lit-B)** | 2010 | Journal (TOG) | Bayes-Netz plus stochastische Optimierung | teilw. | nein | nein | – | Nutzerstudie | – |
| 29 | Laignel et al. (`laignel2021floor`) **(lit-B)** | 2021 | Journal (AutCon) | CP plus GA Grundrisse | **ja** | nein | nein | – | Industriefall | – |
| 30 | Weber et al. (`weber2022automated`) **(lit-B)** | 2022 | Review | Grundrissgenerierung | – | – | – | – | – | – |
| 31 | Kodnongbua, Curtis, Schulz (`kodnongbua2024zeroshot`) [V] | 2024 | Preprint (arXiv) | Neuro-symbolisch: GPT-4 erzeugt Constraints, Gurobi löst, **IIS-Feedback** | **ja** | nein | **ja** (LLM-Spezifikation) | – | Ablation, Vergleich mit realen Gebäuden | – |
| 32 | Text2BIM (`du2026text2bim`) **(lit-A/B)** | 2026 | Journal (JCCE) | Multi-Agent-LLM → Vectorworks-API, Solibri-Checker-Loop | nachträglich, iterativ | ja (Export) | **ja** | – | 3 LLMs, Testfälle | [U] |
| 33 | NADIA (`jang2024nadia`) **(lit-B)** | 2024 | Journal (AEI) | LLM-Detaillierung Außenwände | teilw. | ja | **ja** | Det | Fallstudien | – |
| 34 | Nithyanantham et al. (`nithyanantham2025mcp4ifc`) [V] | 2025 | Preprint (arXiv) | MCP-Server auf IfcOpenShell/Bonsai, Tools plus RAG-Codegenerierung | nein | **ja (nativ)** | **ja** | – | Demo-Aufgaben, kein Benchmark | Open Source (Lizenz [U]) |
| 35 | Hellin, Nousias, Borrmann (`hellin2025natural`) [V] | 2025 | Konferenz (EC3) | LLM-Agenten fragen IFC ohne Ontologie ab | – | **ja** | **ja** | T (MEP-Fragen) | 80 % Genauigkeit | **IFC-Bench v1, CC0** |
| 36 | Hellin et al. (`hellin2026bim`) [V] | 2026 | Preprint (arXiv) | Cobbie: dynamische Tool-Erzeugung für IFC-QA | – | **ja** | **ja** | – | IFC-Bench v2: 1 027 Fragen / 51 Modelle | GitHub `sylvainHellin/cobbie` (Lizenz: NOASSERTION), HF-Datensatz |
| 37 | Chen et al. CAADRIA (`chen2025agent`) **(lit-B)** | 2025 | Konferenz | Sprache/Text → Whisper → Intents → Parameter-Mapping → Grasshopper-PCG | teilw. (Logik-Checks) | nein | **ja (Sprache)** | – | Fallstudien | – |
| 38 | Kakadoo (`atakan2025kakadoo`) **(lit-B)** | 2025 | Konferenz (eCAADe) | Sprache → LLM → JSON → Grasshopper-Slider | nein | nein | **ja (Sprache)** | – | Workshop mit Profis | – |
| 39 | Shin & Issa (`shin2021bimasr`) [V\*] | 2021 | Journal (JCEM) | BIMASR: ASR plus NLP plus relationale DB, Abfrage und Manipulation in Revit | nein | bewusst ohne IFC | **ja (Sprache)** | – | Prototyp | – |
| 40 | Kou & Tan (`kou2008design`) [V] | 2008 | Journal (CAD&A) | Voice-CAD mit CAD-Grammatik und kontextbewusster Inferenz | nein | nein | **ja (Sprache)** | – | Erkennungsraten Grammatik vs. Diktat | – |
| 41 | Kou, Xue, Tan (`kou2010knowledge`) [V] | 2010 | Journal (CAD) | wissensgeleitete Semantik-Inferenz für Voice-CAD | nein | nein | **ja** | – | Prototyp | – |
| 42 | Saluz, Baimuratov, Geyer (`saluz2025semio`) [V] | 2025 | Konferenz (EG-ICE) | LLM-Alignment Kit-of-Parts-Modell → OWL, Reasoner prüft Brandschutz | nein (Alignment für ACC) | nein (semio/RDF) | ja (LLM) | – | 4 LLMs verglichen | semio (Open Source, Lizenz [U]) |
| 43 | Mirhosseini, Shojaei, Sabri (`mirhosseini2026ambiguity`) [U] | 2026 | Journal (Buildings) | Agent synthetisiert Logik, IfcOpenShell verifiziert deterministisch, Graph-Traversal O(K) | nein | **ja** | ja | – | NCC 2022, „zero hallucination“ (Selbstangabe) | – |
| 44 | Pang et al. (`pang2026natural`) [U] | 2026 | Preprint (SSRN) | NL → interoperables BIM, compliance-aware generativ | **ja** (laut Titel) | ja | **ja** | – | [U] | – |
| 45 | Erhan et al. (`erhan2026dcodeweaver`) [U] | 2026 | Konferenz (AHFE) | Priorisierte Code-Regeln als parametrische Regeln im Holzmodulbau (Rhino/GH) | **ja** | nein | nein | – | mit Perkins&Will | – |
| 46 | Wang & Chen (`wang2024cloud`) [V] | 2024 | Journal (Buildings) | Cloud-Konfigurator, Diffusions-Layout (PlanFinder), regelbasierter Recommender, Produktkatalog, IFC | teilw. (vorgenehmigte Blueprints) | ja | teilw. (SBERT-Textmatching) | Bemusterung | Fallstudie British Columbia | – |
| 47 | Abualdenien & Borrmann (`abualdenien2019metamodel`) [V] | 2019 | Journal (AEI) | Multi-LOD-Metamodell mit Fuzziness und `IsRefinedBy` | – (Konsistenzprüfung) | ja | nein | – | Realprojekt, Web-Prototyp | – |
| 48 | Abualdenien & Borrmann (`abualdenien2022levels`) [V] | 2022 | Review (ITcon) | LOD/LOI/LOIN-Begriffe | – | – | – | – | SLR | Open Access |
| 49 | Abualdenien (`abualdenien2023consistent`) [V] | 2023 | Dissertation TUM | Metamodell, Visualisierung von Unsicherheit, LOG-Klassifikation (83–85 %), Graph-Rewriting für Detailmuster | teilw. (Detailtransfer) | ja | NL-Links zu Regeln | Det | mehrere Realfälle | – |
| 50 | Preidel (`preidel2020konformitaet`) [V] | 2020 | Dissertation TUM | VCCL, visuelle Prüfsprache | nein | ja | nein | – | Fallbeispiele | – |
| 51 | Vilgertshofer & Borrmann (`vilgertshofer2017graph`) [V] | 2017 | Journal (AEI) | Graph-Rewriting (GrGen.NET) für schrittweise Detaillierung über LoDs | **ja** (Regeln = Rewrite-Regeln) | ja (IfcTunnel-Export) | nein | Det | Schildtunnel LoD 1–4 | GrGen.NET (Open Source) |
| 52 | Wagner et al. (`wagner2022building`) [V] | 2022 | Journal (AutCon) | Building Product Ontology (BPO), Linked Product Data | – | ergänzt IFC | nein | Bemusterung | Beispielprodukte | Ontologie online [U] |
| 53 | El Sibaii, Granja, Azenha (`elsibaii2025open`) [V] | 2025 | Journal (ITcon) | offene PDT-Plattform nach ISO 23386/23387, bSDD-Anbindung, API | – | ja (IfcProperty.Specification-URI) | nein | Bemusterung | Implementierung PT | Open Source |
| 54 | Jeong et al. (`jeong2009benchmark`) [V\*] | 2009 | Journal (AutCon) | Benchmark-Tests IFC-Austausch Fertigteil | – | **ja** | – | – | Benchmarkmodell, Round-Trips | – |
| 55 | Pazlar & Turk (`pazlar2008interoperability`) [V\*] | 2008 | Journal (ITcon) | Geometrie-Round-Trips IFC | – | **ja** | – | – | Entitäts- und Attributvergleich | – |
| 56 | Ma, Ha, Chung, Amor (`ma2006testing`) [V] | 2006 | Konferenz (ICCCBE) | semantischer Round-Trip-Diff über GUIDs (EVASYS) | – | **ja** | – | – | 3 Testmodelle | – |
| 57 | Lai & Deng (`lai2018interoperability`) **(lit-A)**, Noardo et al. (`noardo2022unveiling`) **(lit-A)** | 2018/22 | Journal | Interoperabilitätsexperimente | – | ja | – | – | – | GeoBIM-Daten offen |
| 58 | Boje et al. (`boje2020towards`) [V] | 2020 | Review (AutCon) | semantischer Construction Digital Twin | – | ja | – | – | 196 Publikationen | Open Access |
| 59 | Tomczak et al. (`tomczak2022review`) **(lit-A)** | 2022 | Review | Informationsanforderungen, IDS | – | ja | – | – | – | – |
| 60 | OpenBIMRL (`stepien2023openbimrl`), Häußler (`haeussler2021code`) **(lit-A)** | 2021/23 | Konferenz/Journal | Regelformat, BPMN/DMN | nein | ja | nein | – | – | – |

**Zählung:** 48 neue Einträge in lit-E, dazu 12 Querverweise auf lit-A/B.

---

## 2. Pro Arbeit: Gold und Warnung

### 2.1 Compliance-by-Design und Mass Customization

**Sydora & Stroulia 2020** [V]
- **Gold:** Dieselbe Regelsprache dient als Prüfer *und* als Generator (Greedy: platzieren → prüfen → behalten oder verwerfen). Das ist der sauberste veröffentlichte Beleg für unser Prinzip „eine Regelbasis, zwei Verwendungen“.
- **Gold:** Die Regeltypen „Eigenschaft“ und „Relation“ plus deren logische Komposition sind eine schlanke Vorlage für unsere Regelmaschine.
- **Warnung:** Nur Möblierung, nur Greedy. Die Autoren sagen selbst, der Algorithmus sei „not an important contribution“. Es gibt kein Baurecht, keine Tragwerks- und keine TGA-Regeln. Die Evaluation vergleicht optisch mit Beispielküchen und hat keine Nutzerstudie.

**Niemeijer, de Vries, Beetz 2009 und Niemeijer 2011 (Diss. TU/e)** [V]
- **Gold:** Das ist unser Szenario, Käufer ändern ein Serienhaus, fast wörtlich:
  - „the architect makes a design as usual, but … specifies the requirements … the buyers … are free to make changes, as long as these changes are not prohibited“.
  - Constraints werden als Funktion `Element → Bool` dargestellt.
  - Die Diss. evaluiert NL-Eingabe von Constraints mit Architekten und Baurechtsregeln zu Dachgauben (Rotterdam).
- **Gold:** Lessons learned zu IFC: Viele Parameter, die Architekten brauchen (Wandlänge und -höhe, Dauerhaftigkeitsklasse Holz, Gauben, Abstellräume), fehlen oder müssen abgeleitet werden. Das gehört direkt in unser IDS/Pset-Design.
- **Warnung:** Die Diss. schließt Generierung ausdrücklich aus („only the former is explored“). Die Puzzle-DSL war laut Nutzertest „too laborious“. Beides ist ein Argument für Sprache plus Intents statt DSL-Eingabe durch Laien.

**FrameX, MCMPro, Boarding, Panelization (Al-Hussein-Gruppe, Alberta)** [V]/[V\*]
- **Gold:** Das ist die einzige zusammenhängende Forschungslinie für automatisiertes **Light-Frame-Holzbau-Detailing mit Industriepartnern**:
  - Framing-Regeln: Ständerabstand, King-, Jack- und Cripple-Studs an Öffnungen, Shipping Walls
  - Beplankung: Plattenlayout mit minimalem Verschnitt
  - Panelisierung: zufällige Trennstud-Wahl außerhalb der Öffnungsstuds, dann DES-Produktivität
  - CNC-Dateien für die Framing-Maschine (siehe Algorithmen)
- **Gold:** Das Evaluationsdesign ist einfach und übertragbar: Zeitvergleich manuell gegen Tool an einer Referenzwand. FrameX spart 80 %.
- **Warnung:**
  - Alles läuft in Revit/AutoCAD-Add-ins, ohne IFC und ohne offenen Code.
  - Die Regeln folgen dem kanadischen NBC mit 16″ o. c. und sind nicht auf DIN/EC5 und den deutschen Holzrahmenbau übertragbar.
  - Kein Kunde entwirft selbst. Eingabe ist ein fertiger Architektenplan.
  - FrameX konnte „nicht durch Öffnungen framen“, also Vorsicht bei Sonderfällen.

**Sandberg et al. 2008; Jensen et al. 2012 (lit-B); Retik & Warszawski 1994** [V]
- **Gold:**
  - KBE und Konfiguration bei skandinavischen Holzhausherstellern.
  - Sandberg zeigt ein Treppen-Tool, das im Verkaufsgespräch Kosten und Herstellbarkeit berechnet. Das ist ein Vorläufer der „Bemusterung mit Regelprüfung“.
  - Retik 1994 zeigt: Die Idee ist 30 Jahre alt, gescheitert ist sie an Daten und Integration, nicht an der Logik.
- **Warnung:** Alle drei nur bis Prototyp oder Fallstudie. Es gibt keine offenen Artefakte.

**Wang & Chen 2024 (Buildings)** [V]
- **Gold:**
  - Konfigurator für Einfamilienhäuser mit **vorgenehmigten Blueprints** plus Diffusions-Layout.
  - Regelbasierter Filter („knowledge-based filtering“) auf zertifizierte BIM-Produkte, dazu SBERT-Textmatching auf Nutzerwünsche.
  - Ausgabe als IFC.
  - Das kommt unserer Bemusterung am nächsten.
- **Warnung:** Die Generierung ist ein Blackbox-Dienst (PlanFinder). Compliance kommt über Vorgenehmigung, nicht über Regeln. Evaluation nur als Fallstudie.

**D-CodeWeaver (Erhan et al. 2026), Pang et al. 2026** [U]
- **Gold:** Beide Arbeiten stellen „compliance as design parameter“ ausdrücklich gegen „post-design verification“. D-CodeWeaver zielt auf modularen *Holz*bau. Pang et al. heißt schon im Titel „From Natural Language to Interoperable BIM … Compliance-Aware Generative Design“ und zitiert Sydora und Laignel. Das ist der nächste direkte Konkurrent.
- **Warnung:** Beide sind noch nicht im Peer-Review-Journal (AHFE-Konferenz bzw. SSRN-Preprint). Vor dem Zitieren den Status prüfen. Pang et al. unbedingt im Volltext lesen, bevor wir „erstmals“ schreiben.

### 2.2 Neuro-symbolische KI und Sprache

**Kodnongbua, Curtis, Schulz 2024 (arXiv)** [V]
- **Gold:** Das LLM erzeugt Constraints und Zielfunktion, ein MILP-Solver (Gurobi) löst. Bei Unlösbarkeit geht das **Irreducible Inconsistent Subsystem (IIS)** an das LLM zurück, das einen widersprüchlichen Constraint streicht. In 10 von 13 unlösbaren Fällen hat das geholfen.
- **Gold:** Ablation zeigt, dass GPT-4-Selbstvalidierung Arithmetik falsch macht, etwa „3+3=6 liegt in 10–15“. Das ist ein starkes Argument, Rechnen nie dem LLM zu überlassen.
- **Warnung:** Mehrfamilienhaus, kein IFC, nur Preprint.

**Mirhosseini et al. 2026; Saluz et al. 2025** [U]/[V]
- **Gold:**
  - Mirhosseini: „AI interprets. Geometry verifies.“ IfcOpenShell ist der deterministische Kern. Ein Konnektivitätsgraph grenzt den Teilgraphen ein (O(K) statt O(N)) und umgeht damit Kontextgrenzen.
  - Saluz: Das LLM richtet ein Kit-of-Parts-Modell auf ein OWL-Regelmodell aus, ein Reasoner liefert eine erklärbare Inkonsistenz. Das Autorenformat vom Prüfformat zu trennen („Single Model“ vs. „Model Islands“) ist ein nützlicher Begriff für unsere Architekturdiskussion.
- **Warnung:** „Zero hallucination“ ist Selbstaussage. Beide prüfen nur und erzeugen nicht.

**Text2BIM (lit-A/B), NADIA (lit-B), MCP4IFC, Chen CAADRIA (lit-B), Kakadoo (lit-B)**
- **Gold:**
  - MCP4IFC ist der erste vollständige MCP-Server auf IfcOpenShell zum Abfragen, Erzeugen und Editieren, mit RAG über IfcOpenShell-Doku. Das ist die direkte Vorlage für eine „Werkzeug-Schicht“, falls wir später doch LLM-Tools zulassen.
  - Chen CAADRIA 2025 hat dieselbe Pipeline wie wir: Whisper → Intent-Analyse → Parameter-Mapping per Tool-Call → PCG-Module mit Logik-Checks. Allerdings nur Kubatur und Fassade.
- **Warnung:** Alle lassen das LLM Code oder API-Aufrufe erzeugen, außer Kakadoo und Chen (Parameter-Mapping). Reproduzierbarkeit und Haftung sind damit schwach. Keine Arbeit hat TGA, Dach oder Fertigung. MCP4IFC ausdrücklich „not intended as comprehensive benchmarks“.

**Hellin et al. 2025/2026 (TUM)** [V]
- **Gold:** **IFC-Bench** ist der einzige offene NL-BIM-Datensatz mit Referenz-IFCs:
  - v2 hat 1 027 QA-Paare auf 51 Modellen.
  - Die vier Kategorien folgen Solihin & Eastman, darunter eine Kategorie „incomplete information“.
  - v1 steht unter CC0.
  - Direkt nutzbar, um unsere Abfrage-Intents („Wie groß ist das Bad?“) zu testen.
- **Warnung:**
  - v2 und Cobbie haben eine Custom-Lizenz (GitHub: NOASSERTION), vor Nutzung lesen.
  - Die Modelle sind englischsprachig und nicht aus dem Holzbau.
  - Es geht nur um Retrieval, nicht um Generierung.

**Shin & Issa 2021; Kou & Tan 2008; Kou, Xue, Tan 2010** [V\*]/[V]
- **Gold:**
  - Kou: eine **CAD-spezifische Grammatik** erkennt deutlich besser als freies Diktat.
  - Kou: **kontextbewusste Inferenz**, also Kandidaten nach aktuellem Modellkontext (Selektion, Dimensionalität) filtern und bei Mehrdeutigkeit nachfragen („Meinen Sie …?“). Das entspricht unserem hierarchischen Intent-Katalog.
  - BIMASR: Sprache zur *Manipulation*, nicht nur zur Abfrage.
- **Warnung:** Vor-LLM-Technik (SAPI) und keine kontrollierten Nutzerstudien mit Laien. BIMASR umgeht IFC bewusst, das ist das Gegenteil unseres Ansatzes.

### 2.3 TGA-Routing

**Medjdoub & Bi 2018** [V]
- **Gold:** Constraint-basierte (CSP) Kanalführung, die ein **parametrisches** und damit nachträglich editierbares Modell erzeugt. Getestet mit Industriepartnern. Das passt zu unserem Anspruch, dass der Kunde nach dem Routing noch verschieben kann.
- **Warnung:** Nur Fan-Coil-Decken im Gewerbebau, keine Holzbalkenlage.

**Singh & Cheng 2021; Choi et al. 2022** [V]/[U]
- **Gold:**
  - Gerichteter gewichteter Graph mit Kosten für Länge, Bögen und Installationsregeln.
  - Dijkstra, 3D-A\* und FOA werden verglichen. Simulated Annealing optimiert die *Reihenfolge* mehrerer Leitungen (Ressourcenkonkurrenz).
  - Choi: temporäres Feingitter lokal bei Kollision, Post-Processing zur Bogenreduktion, Vergleich mit kommerziellem BIM-Routing an 7 Gebäuden.
- **Warnung:** Technikraum bzw. Massivbau. Durchdringungsregeln für Holzbauteile fehlen: Bohrungen in Balken, Schwächung, Brandschutz-Abschottung, Installationsebene.

**Baradaran-Noveiri et al. 2022** [V]
- **Gold:** Die **einzige** Routing-Arbeit für den **Panelbau**. Die Zielfunktion enthält „Anzahl Kreuzungen mit Tragwerk“ und „Überlappung mit anderen Gewerken“, dazu DfMA (Einbau im Werk). GA-Parameter sind dokumentiert: Population 50, 25 Eltern, 100 Generationen, Mutation 27 %.
- **Warnung:** Nur Luftkanäle, nur GA, kanadischer Panelbau, kein IFC.

**Korman et al. 2003; Blokland et al. 2023** [V]
- **Gold:**
  - Korman: Die Wissenskategorien für MEP-Koordination (Design, Montage, Betrieb, Wartung) eignen sich als Checkliste für unsere Routing-Kostenfunktion.
  - Blokland: Die Taxonomie (Raummodell, Routenmodell, Ziel, Constraints; Branching, Ressourcenkonkurrenz, Dimensionalität) liefert Begriffe und Gliederung für das TGA-Kapitel der Arbeit.
- **Warnung:** Blokland stammt überwiegend aus Schiffbau und Anlagenbau.

### 2.4 Dach und Detail

**Aichholzer et al. 1995; Laycock & Day 2003; Kelly & Wonka 2011; Kelly 2014** [V]/[U]
- **Gold:**
  - Das Straight Skeleton liefert laut Aichholzer das „kanonische“ Walmdach.
  - Laycock & Day geben ein vierschrittiges Walmdachverfahren und Varianten für Mansard, Gambrel und Krüppelwalm (Dutch Hip). Rechtwinklige Grundrisse werden in Rechtecke zerlegt, jedes bekommt ein eigenes Dach, dann werden die Dächer vereinigt.
  - Kelly & Wonka: **gewichtetes** Skeleton mit Neigung pro Kante. Kante auf 90° heißt Giebel. Dazu Gauben und Überstände. Sie weisen außerdem auf **Mehrdeutigkeiten im konkaven Fall** hin.
  - Mit campskeleton gibt es eine Implementierung (Java).
- **Warnung:**
  - Das sind reine Geometrieflächen: keine Sparren, Kehlbalken, Schifter, Pfetten, keine Statik.
  - Die Float-Heuristiken können versagen, etwa 2 falsche Dachflächen in 6 000 Gebäuden.
  - Die Lizenz von campskeleton ist noch ungeprüft [U].

**Apolinarska et al. 2016 (Sequential Roof)** [V]
- **Gold:**
  - Normregeln (SIA 265, Nagelabstände) wurden in **Ausschlussellipsen entlang der Faserrichtung** übersetzt. Ein randomisierter Algorithmus besetzt die Nagelpositionen, ein Greedy-Schritt passt Querschnitte an.
  - Unabhängiges Kontrollskript prüft das Ergebnis erneut.
  - Iterationen sind gezählt: 95 % weniger Probleme je Iteration.
  - Das ist Compliance-by-Design auf Verbindungsmittelebene.
- **Warnung:** Freiform-Unikat, nicht seriell.

**Reindeer (Mork 2020), compas_timber (lit-B)** [U]/[V]
- **Gold:**
  - JointSearch definiert den Lösungsraum eines Verbindungstyps über Suchkriterien.
  - TimberProcessingTools bilden Bearbeitungen nach und schreiben BTLx.
  - compas_timber steht unter **MIT** (GitHub-API geprüft).
- **Warnung:** Reindeer ist eine Masterarbeit mit ungeprüfter Institution und Lizenz.

**Vilgertshofer & Borrmann 2017; Abualdenien 2023** [V]
- **Gold:** Graph-Rewriting (GrGen.NET) formalisiert Detaillierungsschritte als Regeln, von LoD 1 bis LoD 4 ohne manuelles Modellieren. Abualdenien überträgt **Detailmuster** per Graph-Rewriting auf neue Projekte. Das ist eine Vorlage für unsere Dach- und Anschlussdetails („Traufdetail X in allen Häusern mit Bedingung Y“).
- **Warnung:** Tunnelbau bzw. frühe Phasen. Keine Fertigungsdaten.

**Liao et al. 2021 (StructGAN); Gan 2022** [V]
- **Gold:**
  - StructGAN evaluiert mit **IoU und Wandanteil gegenüber der Lösung erfahrener Ingenieure**. Das lässt sich direkt auf „Ständerraster und Aussteifungswände vs. Statiker“ übertragen.
  - Gan: Graphmodell für Modulbau mit 1 000–1 500 Varianten in 30 min.
- **Warnung:** Lernende Verfahren verletzen Normen ohne Garantie. Für uns nur als Vergleichsbaseline geeignet, nicht als Methode.

### 2.5 Reifegrad, Single Source of Truth, Produktdaten

**Abualdenien & Borrmann 2019/2022, Diss. 2023** [V]
- **Gold:**
  - Zwei Ebenen: Datenmodell-Ebene (Komponententyp × LOD → Geometrie- und Semantikanforderungen plus erlaubte Unschärfe) und Instanz-Ebene.
  - Die Relation `IsRefinedBy` erlaubt eine Konsistenzprüfung: Semantik und Geometrie bleiben im erlaubten Korridor, Topologie bleibt äquivalent.
  - LOG-Klassifikator erreicht 83–85 %.
  - Direkt nutzbar für „Entwurf → Bauantrag → Werkplanung“ in unserem Modell.
- **Warnung:** Das Metamodell ist nicht IDS-basiert. Wir müssen es auf IDS/LOIN (ISO 7817) abbilden.

**Jeong et al. 2009; Pazlar & Turk 2008; Ma et al. 2006; Lai & Deng 2018 (lit-A); Noardo et al. 2022 (lit-A)** [V]/[V\*]
- **Gold:** Round-Trip-Befunde, belegt:
  - GUIDs werden neu vergeben.
  - Name und Description werden überschrieben.
  - `IfcRoof` wird zu `IfcSlab`.
  - 16 % mehr Wände, Fenster verschwinden.
  - Nur ein Tool bildet 96 % der Features korrekt ab.
  - Ma et al.: Round-Trip-Diff über GUIDs als automatisierbares Prüfverfahren.
- **Warnung:** Die Befunde betreffen alte Tool-Versionen (IFC2x3). Für IFC 4.3 mit unseren Tools müssen wir sie neu messen. Genau das ist unser Beitrag.

**Boje et al. 2020** [V]
- **Gold:** Der dreistufige Construction Digital Twin (Stufen DT1 bis DT3) dient als Einordnungsrahmen für „Single Source of Truth“.
- **Warnung:** Bauphase, nicht Entwurf.

**Wagner et al. 2022 (BPO); El Sibaii et al. 2025 (PDT-Plattform)** [V]
- **Gold:**
  - BPO: modulare Produktbeschreibung als Linked Data, für multifunktionale Produkte, die starre Schemata wie VDI 3805 nicht abbilden.
  - El Sibaii: PDT-Datenmodell nach ISO 23387, bSDD-Anbindung. Die Property wird per `IfcProperty.Specification`-URI referenziert. Das ist das konkrete Muster, wie Bemusterungsmerkmale ins IFC kommen.
- **Warnung:**
  - ISO 23387:2020 ist laut ISO-Seite **zurückgezogen** (Nachfolger prüfen).
  - ETIM ist seit Release 10.0 (Jan. 2025) im bSDD, mit Links zu IFC 4.3 für bisher 491 von 5 799 Klassen (Herstellerangabe ETIM).

---

## 3. Algorithmen zum Übernehmen

Pseudocode als Kurzbeschreibung. Die Quelle steht jeweils dabei.

**A1. Eine Regelbasis für Prüfen und Erzeugen** (Sydora & Stroulia 2020)
```
rules := parse(DSL)                      # Eigenschafts-, Relations-, Komposit-Regeln
generate(space, catalog):
  for item in required_items(space) ordered by priority:
    best := argmax_{pose in candidates(item, space)} score(rules, model ∪ {item@pose})
    if violations(rules, model ∪ {item@best}) == ∅: model.add(item@best) else backtrack/skip
check(model) := [r for r in rules if not r.eval(model)]
```
Für uns: die IDS-Regeln bzw. die Regelmaschine auch als Filter im Kandidatengenerator nutzen. Nicht erst nach dem Intent prüfen.

**A2. LLM-Spezifikation, Solver und IIS-Rückkopplung** (Kodnongbua et al. 2024)
```
spec := LLM(intent, context)            # nur Constraints/Ziele, keine Geometrie
loop:
  sol := MILP.solve(spec)
  if feasible: return sol
  iis := MILP.computeIIS(spec)          # minimal widersprüchliche Teilmenge
  spec := LLM.drop_one(spec, iis)       # oder: Rückfrage an Kunden (bei uns!)
```
Für uns: Das IIS nicht an ein LLM geben, sondern **als Rückfrage an den Kunden**: „Bad 8 m² und Flurbreite 1,20 m passen nicht zusammen, was ist wichtiger?“

**A3. Rechteckgrundriss per LP** (Upasani et al. 2020)
```
input: rectangular arrangement RA (Adjazenz, dimensionslos), minWidth_i, aspect_i∈[a_min,a_max]
vars: x_i, y_i, w_i, h_i
constraints: Nachbarschaft aus RA als Gleichungen der Kanten; w_i,h_i ≥ minWidth_i;
             a_min·h_i ≤ w_i ≤ a_max·h_i (linearisiert); gemeinsame Wandlänge ≥ Türbreite
objective: min Gesamtfläche  (oder: min Abweichung von Wunschflächen)
```
Für uns: Das passt gut zu Raster-Holzrahmenbau mit 62,5-cm-Modul. Das Modul geht als Ganzzahligkeit in ein MILP.

**A4. Walm- und Satteldach per (gewichtetem) Straight Skeleton** (Aichholzer 1995; Laycock & Day 2003; Kelly & Wonka 2011)
```
S := straight_skeleton(footprint, weights)   # weight_e = tan(neigung_e); Giebel: weight=∞ (vertikal)
for vertex v in S: z(v) := dist(v, supporting_edge) · weight
faces := boundary_walk(S, least_interior_angle)   # je Kante eine Dachfläche
rechtwinklig/komplex: partition(footprint) → Rechtecke → je Dach → merge (Laycock Fig. 6)
Mansard: shrink bis 85 % des ersten Events, dann zweite Neigung
```
Danach folgt der eigene Schritt, den die Literatur nicht liefert: aus Grat-, Kehl- und Firstlinien die Sparren, Schifter und Gratsparren ableiten (siehe Abschnitt 4).

**A5. Holzrahmen-Framing und Panelisierung** (FrameX; Alwisy 2019; Liu et al. 2021)
```
studs := place_regular(wall, spacing)                  # bei uns 62,5 cm
for opening o: add king_studs, jack_studs, header, sill, cripples; remove conflicts
panelize(wall):
  repeat K times:
    L := random(target_panel_lengths ≤ transport_max)
    N := ceil(len(wall)/L)
    cuts := choose N−1 studs  ∉ {king, jack, cripple}   # Öffnungen nicht teilen
    if feasible(struct, transport, crane): candidates += cuts
  return argmax_{c in candidates} DES_productivity(c)   # oder: min Bauteilvarianz
```

**A6. Beplankung mit minimalem Verschnitt** (Liu et al. 2018)
```
for wall face: lay sheets from reference corner, snap joints to studs
cut list := sheets ∩ face − openings
optimize start offset/ orientation to min waste; reuse offcuts (1D/2D bin packing)
```

**A7. CNC-Operationen aus dem BIM** (Alberta-Framing-Maschine, MOC-Summit-Beitrag [U]; ISARC-2017-Beitrag [U])
```
nails  := intersections(stud, plate) × n_nails(code)   # z. B. ≥2 Nägel, ≥82 mm (NBC Alberta)
drills := routing_penetrations ∩ studs (Kollision prüfen)
for op in ops: x'_op := x_op − offset[station(op)]    # Stationsversatz Nagler/Säge/Bohrer
sort ops by x' → Maschinendatei
```
Für uns: dasselbe Prinzip Richtung BTLx und Maschinenformate für Nagelbrücke und Multifunktionsbrücke. Die Leitungsdurchbrüche kommen aus dem TGA-Routing (A8) und gehen als Bohrungen in die Maschinendaten. Diese Kopplung hat noch niemand publiziert.

**A8. TGA-Routing im Holzrahmenbau** (Kombination aus Singh & Cheng 2021, Choi 2022, Baradaran-Noveiri 2022, Medjdoub 2018)
```
G := orthogonal voxel/graph in Installationsebene + Balkenlage   # IfcOpenShell-Voxelisierung
cost(e) := len(e) + α·bend + β·cross_structural(e) + γ·(Bohrung in Balken nicht zulässig ? ∞ : 1)
         + δ·Brandabschnitt-Durchdringung + ε·Gefälle-Verletzung (Abwasser)
order := SA over permutations of runs (Abwasser zuerst, dann Lüftung, Wasser, Elektro)
for run in order: path := A*(G, run, cost); G.block(path ⊕ clearance)
post: merge colinear, reduce bends; emit IfcPipeSegment/IfcDuctSegment + IfcPipeFitting
```

**A9. Norm im Verbindungsmittel-Algorithmus** (Apolinarska et al. 2016)
```
for each connection: feasible := overlap_polygon − edge_offsets(fibre dir)
repeat: sample candidate nail p in feasible; accept if ∀q: p ∉ ellipse(q, fibre_i, fibre_j)
until required count; if not reached → greedy upsizing of member; iterate model
independent checker re-verifies all ellipses
```

**A10. Refinement-Konsistenz über Reifegrade** (Abualdenien & Borrmann 2019)
```
for element e with e_k IsRefinedBy e_{k+1}:
  assert semantics(e_{k+1}) ⊆ allowed_range(e_k)
  assert |geom(e_{k+1}) − geom(e_k)| ≤ fuzziness(type, LOD_k)
  assert topology(e_{k+1}) ≅ topology(e_k)
```

**A11. Detailmuster per Graph-Rewriting** (Vilgertshofer & Borrmann 2017; Abualdenien 2023)
```
rule Traufdetail_A: LHS = (Wand)-[trägt]->(Dach{neigung∈[25°,45°]}) ; RHS = LHS + Fußpfette + Sparrenanschluss + Luftdichtung
apply rules until fixpoint; evaluate graph → IFC elements
```

**A12. Round-Trip-Regressionstest** (Ma et al. 2006; Pazlar & Turk 2008)
```
B := import_export(tool, A)
match by GlobalId; report: missing types, missing instances, changed attributes, changed relations
Fail if Kern-Psets / IfcRoof / IfcCovering / Systemzuordnung verändert
```

**A13. Kontextbewusste Spracherkennung** (Kou & Tan 2008; Kou et al. 2010)
```
hyps := ASR(nbest) sorted by conf
for h in hyps: if valid_in_context(h, selection, dimensionality, phase): return h
ask("Meinten Sie …?")
```
Das deckt sich mit unserem hierarchischen Intent-Katalog und dem Kontextfilter (Recherche 03).

**A14. Deterministischer Kern plus LLM nur zur Interpretation** (Mirhosseini et al. 2026; Text2BIM; MCP4IFC)
Bei uns noch strenger: Das LLM bzw. Intent-Modell liefert nur `{intent, slots}`. Geometrie, Prüfung und Export laufen ausschließlich im Code. Das ist das stärkste Abgrenzungsargument gegenüber allen LLM-Codegeneratoren.

---

## 4. Was keine Arbeit bisher geschafft hat

1. **Eine Kette in einem IFC-4.3-Modell:** Laienentwurf per Sprache → regelkonforme Erzeugung → TGA → Dach → Bemusterung → IDS-Prüfung → Bauantrag → Maschinendaten. Es gibt keine einzige Arbeit mit mehr als drei dieser Glieder. Am nächsten kommen:
   - Wang & Chen 2024 (Konfigurator, IFC, Produkte)
   - Alberta (Framing, CNC)
   - Pang et al. 2026 (NL, compliance-aware, IFC; Preprint)
2. **TGA-Routing, das Holzbauregeln kennt:** Installationsebene, keine Bohrungen in bestimmten Balkenzonen, Durchbrüche als Maschinendaten, Brandschutz-Abschottungen in Holzbauteilen. Baradaran-Noveiri berücksichtigt nur Kreuzungen mit Tragwerk.
3. **Vom Straight-Skeleton-Dach zum Abbund:** Sparren, Grat- und Kehlsparren, Schifter und BTLx-Bearbeitungen automatisch aus der Dachgeometrie. Die Geometriearbeiten hören bei Flächen auf. Die Abbund-Tools (Reindeer, compas_timber) setzen eine fertige Stabgeometrie voraus.
4. **Compliance-by-Design mit echtem Baurecht (Landesbauordnung, GEG, Holzbaurichtlinie) *während* der Generierung.** Vorhanden ist nur:
   - Innenraum-Ergonomie (Sydora)
   - NBC-Framing (FrameX)
   - SIA-265-Nägel (Apolinarska)
   - Massing-Regeln (D-CodeWeaver)
5. **Kontrollierte Nutzerstudie mit echten Bauherren (Laien), die per Sprache ein ganzes Haus entwerfen.** Die Studien nutzen Profis und Studierende:
   - Kakadoo: Workshop mit Profis
   - MR-Parametrik: 27 Architekt:innen
   - Niemeijer: Architekturstudierende
6. **Messung der IFC-4.3-Round-Trip-Verluste für Holzbau-Entitäten** (`IfcMember`, `IfcCovering`, `IfcElementAssembly`, `IfcPipeSegment`). Die bisherigen Studien laufen auf IFC2x3 und Massivbau.
7. **Reifegrad-Konsistenz (Multi-LOD) in einem generativen System.** Abualdenien prüft von Hand gebaute Modelle. Niemand erzwingt `IsRefinedBy` bei automatischer Detaillierung.
8. **Deutschsprachige Intent-Erkennung für den Hausentwurf.** Alle NL-BIM-Arbeiten und -Datensätze sind englisch oder chinesisch.

---

## 5. Evaluationsdesigns zum Übernehmen

| Design | Quelle | Übertragung auf unser System |
|---|---|---|
| **Zeitvergleich manuell vs. Tool** an Referenzbauteil | FrameX (−80 %), Gan (30 min / 1 000 Varianten), Baradaran-Noveiri | Referenzhaus: Konstrukteur mit hsbcad/Dietrich's gegen unser System. Messen: Zeit bis Werkplan und Zeit bis BTLx |
| **Vergleich mit Expertenlösung per IoU/Überdeckung** | StructGAN (SIoU, WIoU, SWratio) | Ständer- und Aussteifungslayout, TGA-Trassen gegen die Lösung des Herstellers; IoU der Wandflächen |
| **Benchmark-Modell mit Tool-Matrix und Round-Trip** | Jeong et al. 2009; Noardo et al. 2022 (lit-A) | 3 Referenzhäuser als IFC 4.3 → Import/Export in 4–5 Tools → Diff nach A12 |
| **GUID-basierter Semantik-Diff** | Ma et al. 2006; Pazlar & Turk 2008 | als CI-Test im Repo |
| **QA-Benchmark mit Komplexitätskategorien** | IFC-Bench (Hellin); Kategorien nach Solihin & Eastman | eigene deutschsprachige Fragen an unsere Häuser; Kategorie 4 („unvollständige Information“) testet, ob das System Rückfragen stellt |
| **pass@k** für Code- bzw. Intent-Generatoren | CAADRIA-2025-Beitrag zum RKG-/IfcOpenShell-Codegenerator (pass@1 82 %) [U, Autoren offen] | pass@k ist für Codegeneratoren gedacht und für uns nicht passend. Stattdessen Intent-Accuracy@1/@3 plus Slot-F1 pro Intent-Ebene |
| **Ablation „mit/ohne symbolische Rückkopplung“** | Kodnongbua et al. (IIS-Loop 10/13); Text2BIM (Checker-Loop) | System mit und ohne Regelfilter bei der Kandidatengenerierung; messen: Regelverletzungen je Entwurf, Anzahl Rückfragen |
| **Mapping-Accuracy bestehender Regeln vs. Neuregel-Erfolgsquote, getrennt nach Regeltyp** | Alnuzha & Bloch 2026 [U]: 100 % Parameterregeln, 20–60 % räumliche Regeln | Regelmaschine nach Solihin-Klassen auswerten; räumliche Regeln getrennt berichten |
| **Usability-Test mit Nutzergruppen und Aufgaben mit Fehlern** | Niemeijer 2011 (Studierende formulieren Constraints zu fehlerhaften Entwürfen) | Laien bekommen Aufgabenkarten wie „Bad vergrößern, Dachgaube hinzufügen“. Messen: Erfolg, Zeit, SUS, Rückfragen, Abbruch |
| **Workshop-Studie mit Profis** | Kakadoo (eCAADe 2025), MCP-GH (NeurIPS-Workshop, 20 Teilnehmende) | ergänzend mit Vertriebsberatern des Herstellers; Achtung: homogene, digital affine Stichprobe als Limitation benennen (Kakadoo nennt das selbst) |
| **Produktivitätsbewertung per Diskreter Ereignissimulation (DES)** | Liu et al. 2021 | Panelisierungsvarianten gegen die Werkslinie des Herstellers simulieren |

---

## 6. Nicht verifizierte Hinweise (nicht in lit-E)

- **„Automated BIM-Based CNC File Generator for Wood Panel Framing Machines in Construction Manufacturing“** (Journal of Industrialized Construction / MOC Summit). Volltext gesehen, Autoren und Jahr nicht (Seite gesperrt). Methodisch wichtig für A7.
- **„Developing a BIM-based Integrated Model for CAD to CAM Building Production Automation“** (ISARC 2017, Paper 007). Nagel-, Bohr- und Schnittkoordinaten aus Revit. Autoren nicht geprüft.
- **Alnuzha & Bloch (2026), „Integrating large language models and knowledge graphs for adaptive design review“.** Venue offen.
- **CAADRIA 2025, Beitrag 348:** RKG plus IfcOpenShell-Codegenerator (GPT-2), pass@k. Autoren nicht geprüft.
- **MDPI Buildings 15(12):2093 (2025), Review zu Pfadoptimierung bei MEP** (ACO + A\*). Autoren nicht geprüft. Die Zahlen darin (−25–35 % Entwurfszeit) sind nicht belastbar.
- **„Text-to-Code Generation for Modular Building Layouts in BIM“** (arXiv 2509.23713) und **„Toward Platform-based Building Design“** (arXiv 2305.10949): nur als Suchtreffer gesehen, noch lesen.
- **Malmgren, Jensen, Olofsson, „Product modeling of configurable building systems – a case study“** (ITcon, 2010 oder 2011, Jahr widersprüchlich). Schwedischer Hausbauer, Produktstruktur.
- **Müller et al. (2006), „Procedural modeling of buildings“** (ACM TOG), wird von Kelly zitiert. Nicht selbst geprüft.
- **Zeitschriftenversion von Niemeijer et al., „Designing with constraints – towards mass customization in the housing industry“** (TU/e-Repositorium): Venue offen.

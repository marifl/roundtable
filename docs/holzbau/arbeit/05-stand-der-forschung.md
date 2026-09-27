# 5 Stand der Forschung und Technik

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle geprüft) oder [U] (unsicher); eigene Bewertungen sind als solche formuliert. Graue Literatur ist im Text als solche ausgewiesen.

## 5.0 Einordnung und Vorgehen

Die Arbeit verbindet sechs Forschungsfelder, die sich bisher weitgehend getrennt entwickelt haben:

- das Informationsmodell IFC mit seinen Prüf- und Liefermechanismen (Abschnitt 5.1)
- die automatisierte Regelprüfung und den digitalen Bauantrag (5.2)
- die digitale Prozesskette im vorgefertigten Holzbau (5.3)
- Mass Customization und Produktkonfiguration im Hausbau (5.4)
- generatives Design mit Grundriss- und Möblierungssolvern (5.5)
- Sprach- und Sprachmodellschnittstellen in Architektur, Ingenieurwesen und Bau (AEC) (5.6)

Abschnitt 5.7 stellt die Arbeiten gegenüber, die der Zielsetzung am nächsten kommen. Abschnitt 5.8 leitet daraus die Forschungslücken ab und grenzt den eigenen Beitrag ab.

Das Kapitel beantwortet für jedes Feld drei Fragen:

1. Was ist gesichert, und auf welcher Evidenz beruht es?
2. Was davon lässt sich für ein kundengesteuertes, regelbasiertes Entwurfssystem im Holzrahmenbau übernehmen?
3. Wo endet das Feld, und welche Annahme der Arbeit ist dort nicht gedeckt?

**Quellenbasis.** Die Literatur stammt aus der systematischen Recherche nach Kapitel 2 (Protokoll `02a-review-protokoll.md`). Sie umfasst die thematischen Recherchen 01 bis 28 in `../recherche/` und drei Runden Schneeballverfahren nach Wohlin. Runde 1 nahm 286 Quellen mit Relevanz ≥ 2 auf, Runde 2 weitere 162 (Recherchen 24 bis 26). Runde 3 wurde nach 3 von 53 Startquellen abgebrochen, weil die Zitationsdienste nicht mehr erreichbar waren. Sie lieferte 7 weitere Quellen (Recherche 28). Die Sättigung ist deshalb **nicht formal nachgewiesen**. Die steigenden Wiederholungsanteile (Bestandsdubletten von 17 % in Runde 2 auf 41 % in Runde 3) sprechen aber für eine nahe Sättigung. Jede Quelle ist einzeln nach ihrer Passung zu FF1 bis FF6 bewertet (`literatur/quellen-bewertung.csv`). Aussagen über Inhalte stützen sich auf Abstract, Einzelbewertung oder Recherchebefund. Wo nur Titel und Screening-Notiz vorliegen, ist das vermerkt.

**Maßstab der kritischen Würdigung.** Viele der gesichteten Arbeiten sind Demonstratoren. Um ihre Belastbarkeit vergleichbar zu machen, ordnet dieses Kapitel die Evaluation jeder Arbeit einer von fünf Stufen zu. Die Stufen sind eine eigene Einordnung, angelehnt an die Unterscheidung artifizieller und naturalistischer Evaluation in FEDS [@venable2016feds] und an die Evaluationsmuster von Sonnenberg und vom Brocke [@sonnenberg2012evaluations].

| Stufe | Bedeutung | typisches Beispiel |
|---|---|---|
| **E0** | konzeptionell, kein lauffähiges Artefakt oder keines berichtet | Rahmenwerk, Architekturvorschlag |
| **E1** | Demonstration an einem oder wenigen Fällen, ohne Vergleichsmaß | Proof of Concept, Fallstudie |
| **E2** | technische Messung gegen Referenz oder Baseline | Genauigkeit, Zeit, Verschnitt gegen manuelle Lösung |
| **E3** | Studie mit Zielnutzern | Usability-Test, Experiment mit Kontrollgruppe |
| **E4** | Einsatz im Betrieb mit Betriebsdaten | Live-Konfigurator mit Nutzungsprotokoll |

Die Stufen bewerten nicht die Idee, sondern wie weit ein Befund getragen ist.

## 5.1 BIM und IFC: Datenmodell, Lieferanforderungen und Validierung

### 5.1.1 Entwicklung und Standardisierung

Die maßgebliche deutschsprachige Darstellung der BIM-Grundlagen ist der Band von Borrmann, König, Koch und Beetz, von der Datenmodellierung über IFC bis zur Regelprüfung [@borrmann2021bim].

Laakso und Kiviniemi zeichnen die Standardisierung der Industry Foundation Classes von 1994 bis 2012 nach [@laakso2012ifc]. Sie beschreiben den Wandel vom Industriekonsortium zur offenen, hybriden Normung und stellen eine schwache Marktdurchdringung fest. Der Befund ist für die Arbeit nicht veraltet: Er erklärt, warum ein Standard, der im Schema reich ist, in der Werkzeugpraxis oft nur teilweise umgesetzt wird.

**Stand 2026 [V]:**

- IFC 4.3 ADD2 ist als ISO 16739-1:2024 genormt [@iso2024ifc]. Die zweite Ausgabe erweitert das Schema um Infrastrukturbauwerke.
- IFC4 ADD2 TC1 (ISO 16739-1:2018) ist daneben weiter gültig und hat in der Software derzeit die breitere Unterstützung. Laut Recherche 06 exportieren hsbcad und cadwork nur bis IFC4, und Archicad bietet kein IFC 4.3 an.
- Für den Holzrahmenbau relevante Änderungen gegenüber IFC4: `IfcBuildingElement` heißt nun `IfcBuiltElement`, und `IfcWallElementedCase` ist entfallen. Das Wandelement wird als `IfcWall` mit `IfcRelAggregates` abgebildet (Recherche 01, am Schema IFC4X3_ADD2 geprüft).

Das österreichische Projekt Sys.Wood bestätigt die Lücke zwischen Norm und Praxis (graue Literatur). Eine Umfrage bei 63 Holzbauunternehmen benennt Softwarekompatibilität, Datenformate und redundante Arbeit als Probleme [@tugraz2025syswood] (Recherche 21). Eine Projektveröffentlichung von 2026 empfiehlt IFC 4.3, findet in der Praxis aber zu 56 % IFC4 im Einsatz und vermisst Fertigungsmerkmale (Recherche 06).

### 5.1.2 Model View Definitions und ihre Grenzen

IFC ist ein breites Schema. Für einen konkreten Austausch muss festgelegt werden, welche Teilmenge mit welcher Detaillierung geliefert wird. Eastman et al. begründeten dafür die Konzepte Exchange Model und Exchange Object im Information Delivery Manual (IDM) [@eastman2010exchange]. Die Semantik von Model Views, ihre ontologiebasierte Entwicklung und die regelbasierte Validierung gegen sie sind ausgearbeitet [@venugopal2012semantics; @lee2016ontology; @lee2016modularized; @lee2019mechanism].

Die Model View Definition (MVD) war lange das Mittel der Wahl. Zhang, Beetz und Weise implementierten einen mvdXML-basierten Prüfer mit Berichten im BIM Collaboration Format (BCF). Sie zeigten, dass sich vor allem Existenz-, Werte-, Eindeutigkeits- und Wenn-dann-Regeln abbilden lassen, geometrische und berechnete Anforderungen dagegen nicht [@zhang2015interoperable]. Ramaji et al. zeigten, dass bestehende MVDs mehrgeschossige Modulbauten nicht abdecken, und erweiterten eine MVD in einer Fallstudie [@ramaji2017extending].

**Befund für IFC 4.3 [V]:** Offiziell sind nur zwei MVDs veröffentlicht, die Reference View und die Alignment-based View. Eine Design Transfer View für IFC 4.3 gibt es nicht [@bsiMvd43]. Die Reference View ist laut Dokumentation kein vollständiger Austausch der Entwurfsabsicht (Recherche 01 und 06). buildingSMART hat mvdXML zurückgezogen. Das EU-Projekt CHEK nennt das als einen Grund, IDS statt mvdXML zu verwenden [@chek2024d22].

**Konsequenz:** Für die hier verfolgte Breite von Entwurf bis Fertigung existiert keine offizielle MVD. „Standardkonform“ lässt sich deshalb nicht über die Erfüllung einer MVD definieren. Es muss über Schemavalidität, die normativen Regeln des Validation Service und projektspezifische Lieferanforderungen definiert werden (Abschnitt 5.1.4).

### 5.1.3 Information Delivery Specification (IDS)

Tomczak et al. verglichen die Methoden, mit denen Informationsanforderungen spezifiziert werden: bSDD und ISO 12006, IDM, Property Templates, IDS, Level of Information Need (LOIN), mvdXML, Product Data Templates und SHACL [@tomczak2022review]. Ihr Befund: Keine Methode deckt alle Aspekte ab. Die Vorgeschichte der IDS über Linked Data beschreiben van Berlo et al. [@vanberlo2019creating]. IDS 1.0 ist seit dem 1. Juni 2024 offizieller buildingSMART-Standard [@bsi2024ids]. IFC4X3_ADD2 ist als Zielschema zulässig (Recherche 06).

Die Anwendungsforschung zu IDS ist jung und wächst schnell:

- **Tabellarische Anforderungen.** Fischer et al. überführen die in der Praxis verbreiteten Merkmalslisten in eine erweiterte Tabellenstruktur, die IDS vollständig nutzt. Validiert wurde das unter anderem am openBIM-Bauantrag der Stadt Wien [@fischer2025bridging].
- **Bauantrag.** Dieselbe Gruppe zeigt, dass Bauaufsichten IDS bereits für Informationsanforderungen nutzen. Für Fluchtweg- und Feuerwiderstandsprüfungen fehlt aber eine Filterung nach Merkmalen verbundener Elemente. Eine kleine Schemaerweiterung macht IDS zu einer einfachen Regelsprache [@fischer2024extending].
- **Vergleich.** Nuyts et al. formulieren fünf Anforderungen der flämischen Barrierefreiheitsregeln in acht Ansätzen, darunter Solibri, IDS, JSON Schema, XSD, OWL, SWRL, SPARQL und SHACL. SHACL halten sie unter den Linked-Data-Ansätzen für am besten geeignet [@nuyts2024comparative].
- **Werkzeugqualität.** Cerovšek und Omar evaluieren IDS mit fünf Werkzeugen an einem realen Projekt. Sie finden Schwächen bei Klassifikationsfacetten, regulären Ausdrücken und Fehlerberichten [@cerovsek2025advancing].
- **Reifegrade.** Akbas et al. untersuchen die Integration von IDS mit dem LOIN-XML-Schema nach DIN EN ISO 7817-1 [@akbas2025holistic; @dineniso7817-1]. LOIN deckt mehr Aspekte ab, IDS vor allem alphanumerische Anforderungen. Eine vollständige Integration gelingt wegen der unterschiedlichen Reichweite nicht.
- **Erstellung per Sprache.** Yang et al. übersetzen natürlichsprachliche Anforderungen mit einem Sprachmodell in gültiges IDS-XML. Die Arbeit ist eine Demonstration ohne quantitative Evaluation [@yang2026llmpowered].

**Kritische Würdigung.** IDS ist für die Arbeit das richtige Werkzeug für Regelklasse R2 (Kapitel 4.1), und zwar aus drei Gründen: Es ist standardisiert, deklarativ und werkzeugunabhängig prüfbar. Die Literatur zeigt aber übereinstimmend seine Grenze. IDS prüft das Vorhandensein und die Werte von Merkmalen, nicht die Geometrie und nicht Beziehungen über mehrere Elemente hinweg [@fischer2024extending; @akbas2025holistic]. Die Evaluationen sind überwiegend Fallstudien der Stufe E1. Nur Nuyts et al. vergleichen Ansätze systematisch an denselben Anforderungen, allerdings an nur fünf Regeln [@nuyts2024comparative].

### 5.1.4 Validierung: buildingSMART Validation Service

Mit dem buildingSMART Validation Service existiert eine öffentliche Referenzinstanz für die Validierung von IFC-Dateien. Er prüft vier Dinge [@bsi2025validation; @bsiValidation]:

- Syntax
- Schemakonformität einschließlich der Where-Rules
- normative Regeln (Implementer Agreements und Informal Propositions, formuliert als Gherkin-Szenarien auf IfcOpenShell-Basis)
- bSDD-Bezüge

Industry Practices meldet er als Warnungen. Der Ansatz geht auf Moult und Krijnen zurück, die Prüfregeln im Stil des Behaviour-Driven Development formulierten und bei jeder Modellrevision ausführten [@moult2020compliance].

**Befund [V]:** Projekt- und Firmenregeln prüft der Validation Service nicht (Recherche 06). Er ist damit eine notwendige, aber keine hinreichende Bedingung für ein prüffähiges Modell. Für Firmenregeln braucht es IDS, für geometrische Regeln eine eigene Regelmaschine.

### 5.1.5 Interoperabilität und Informationsverlust

Dass der IFC-Austausch Information verliert, ist gut belegt:

- Pazlar und Turk zeigten an Geometrie-Round-Trips den Verlust von Entitäten und Attributen [@pazlar2008interoperability].
- Ma et al. schlugen einen semantischen Vergleich über GlobalIds als automatisierbares Prüfverfahren vor [@ma2006testing].
- Jeong et al. testeten den Austausch für den Fertigteilbau an einem Benchmark-Modell [@jeong2009benchmark].
- Lai und Deng dokumentierten Verluste und Verfälschungen bei Geometrie, Beziehungen und Eigenschaften zwischen heterogenen Programmen [@lai2018interoperability].

Für den Bauantrag besonders relevant sind zwei Befunde. Erstens ist die Georeferenzierung in Autorensoftware häufig fehlerhaft oder unvollständig [@jaud2020georeferencing; @jaud2022georeferencing]. Zweitens sind Raumbegrenzungen zweiter Ordnung, die für Flächen- und Energienachweise gebraucht werden, eigens zu erzeugen und zu validieren [@ying2021generating; @ying2021rulebased]. Noardo et al. prüften reale Architektenmodelle auf typische Bauantragskriterien. Sie fanden, dass die schwankende Modellqualität der eigentliche Engpass ist [@noardo2022ifc].

Für den Holzbau liefert das österreichische Projekt TIMBIM einen konkreten Warnbefund (graue Literatur) [@timbim2024]. Die Schichtaufbauten von dataholz.eu stehen dort als IFC und bSDD-Daten bereit. Die geplante Abbildung jeder Schicht als eigene Komponente über eine Aggregation wurde aber verworfen, weil die Autorensoftware sie nicht umsetzte. Die Schichten werden nur alphanumerisch transportiert (Recherche 11).

**Kritische Würdigung.** Die Round-Trip-Studien sind methodisch einfach und gut übertragbar, beziehen sich aber überwiegend auf IFC2x3 und Massivbau. Für IFC 4.3 und Holzbauentitäten wie `IfcMember`, `IfcBuildingElementPart` und `IfcMechanicalFastener` gibt es keine vergleichbare Messung. Aus der Literatur folgt vor allem ein Architekturargument: Wenn ein Modell programmatisch erzeugt wird, statt aus einem Autorenwerkzeug exportiert, entfallen typische Exportfehler. Dafür muss der Generator seine eigene Konformität nachweisen.

### 5.1.6 Reifegrade im Modell

Abualdenien und Borrmann legen mit einem Multi-LOD-Metamodell die formale Grundlage für Detaillierungsstufen in einem Modell [@abualdenien2019metamodel]. Für jeden Komponententyp und jede Stufe definieren sie Anforderungen an Geometrie und Semantik mit erlaubter Unschärfe. Die Relation `IsRefinedBy` macht die Konsistenz zwischen Stufen prüfbar. Ihre Übersicht ordnet die Begriffe LOD, LOI und LOIN [@abualdenien2022levels]. Das Metamodell ist an einem realen Projekt evaluiert und nicht auf IDS oder LOIN abgebildet (Recherche 12).

### 5.1.7 IFC 5 und IFCX

Die Weiterentwicklung zu IFC 5 zielt auf Modularisierung, Normalisierung der Objekt- und Beziehungsstrukturen, Unabhängigkeit von EXPRESS/STEP und ein „Late Binding“ fachlicher Inhalte [@vanberlo2021future]. Effiziente binäre Speicherformate bereiten das vor [@krijnen2020efficient]. Die Serialisierung IFCX befindet sich im Alpha-Stand. Ein Release-Termin ist nicht bekannt (Recherche 06, Stand 26.08.2026) [U].

**Konsequenz:** Die Arbeit kann nicht auf IFC 5 warten. Stabile GlobalIds, bSDD-Verweise und IDS erleichtern eine spätere Migration, ohne sie vorwegzunehmen.

### 5.1.8 Zwischenfazit 5.1

| Mechanismus | leistet | leistet nicht | Konsequenz für die Arbeit |
|---|---|---|---|
| Schema IFC4X3_ADD2 [@iso2024ifc] | Entitäten für nahezu alle Phasen von Entwurf bis Übergabe (Recherche 06) | keine Maschinendaten, keine Varianten in einer Datei | IFC als kanonisches Modell; BTLx/WUP und Varianten außerhalb |
| MVD [@bsiMvd43] | vereinbarte Teilmengen für Reference View und Alignment | keine offizielle MVD für Entwurf bis Fertigung | Konformität über Validierung statt MVD definieren |
| IDS [@bsi2024ids] | deklarative Merkmalsanforderungen, werkzeugunabhängig prüfbar | Geometrie, elementübergreifende Beziehungen [@fischer2024extending] | IDS für R2-Regeln, Regelmaschine für R1 |
| Validation Service [@bsi2025validation] | Syntax, Schema, normative Regeln, bSDD | Projekt- und Firmenregeln | Pflichtprüfung jeder Revision, ergänzt durch IDS |
| LOIN / Multi-LOD [@dineniso7817-1; @abualdenien2019metamodel] | Informationsbedarf je Stufe, Konsistenz über `IsRefinedBy` | Abbildung auf IDS nur teilweise [@akbas2025holistic] | Reifegrade P/R/A je Bauteilgruppe als IDS-Profile |

## 5.2 Automatisierte Regelprüfung und digitaler Bauantrag

### 5.2.1 Grundlegung und Taxonomien

Als Referenzpunkt der BIM-basierten Regelprüfung gilt die Übersicht von Eastman et al. [@eastman2009automatic]. Sie vergleicht fünf industrielle Prüfsysteme, darunter CORENET in Singapur, und zerlegt die Prüfung in vier Phasen:

1. Interpretation und logische Strukturierung der Regeln
2. Vorbereitung des Bauwerksmodells
3. Ausführung der Prüfung
4. Bericht

Diese Gliederung ist bis heute der gemeinsame Bezugsrahmen. Eine aktuelle Übersicht über die KI-gestützte Prüfung ergänzt sie um eine fünfte Stufe, die Entscheidungsunterstützung [@senousy2026automated]. Die Wirkung auf Zeit und Kosten wird bei Eastman et al. behauptet, aber nicht gemessen (Einzelbewertung).

Solihin und Eastman klassifizierten Prüfregeln nach Berechnungskomplexität [@solihin2015classification]. Die Klassen reichen von Regeln, die explizite Attributwerte abfragen, bis zu Regeln, die abgeleitete Geometrie, Topologie oder einen Lösungsnachweis brauchen. Die Klassifikation macht sichtbar, dass der Aufwand weniger in der Logik der Regel liegt als in der Frage, ob das Modell die geprüften Größen explizit enthält.

Amor und Dimyadi ziehen nach rund fünfzig Jahren Forschung eine nüchterne Bilanz: Das Versprechen der automatisierten Prüfung sei in der Praxis nur in Ansätzen eingelöst [@amor2021promise]. Sie benennen das „Black-Box“-Problem entkoppelter Regelkopien und fordern, Regeln an ihre Quelltexte zu koppeln. Hjelseth erklärt am Beispiel von CORENET und ByggSøk, warum sich staatliche Prüflösungen kaum verbreitet haben [@hjelseth2015public]. Fünf verbreitete Prüfplattformen folgen alle dem Ablauf „übersetzen, definieren, prüfen, berichten“ [@lee2020comparative].

### 5.2.2 Offene und transparente Regelsprachen

Die frühen kommerziellen Werkzeuge kodierten Regeln fest und intransparent. Die Folgeforschung zielt auf Repräsentationen, die Fachleute ohne Programmierkenntnisse lesen und pflegen können:

- **Visuelle Sprachen.** Preidel und Borrmann entwickelten die Visual Code Checking Language (VCCL), einen Datenflussgraphen aus Operatorknoten, erprobt an einer deutschen Brandschutzvorschrift [@preidel2015automated; @preidel2016towards; @preidel2020konformitaet].
- **Entscheidungstabellen.** Häußler, Esser und Borrmann prüften 943 Regeln aus Richtlinien der Deutschen Bahn auf Abbildbarkeit in BPMN und DMN. Je nach Teilbestand gelang das für 37 bis 75 %, bei modellrelevanten Regeln für 68 % [@haeussler2021code]. Das ist einer der wenigen quantitativen Befunde zur Formalisierbarkeit überhaupt.
- **Offene Formate.** OpenBIMRL kombiniert einen Vorberechnungsgraphen für geometrische und semantische Informationen mit aussagenlogischer Auswertung und wurde an der Musterbauordnung evaluiert [@stepien2023openbimrl].
- **Testfälle als Regeln.** Gherkin-Szenarien nach Moult und Krijnen machen Regeln zugleich zu ausführbaren Tests [@moult2020compliance].
- **Semantic Web.** Regeln und Modelle werden in RDF/OWL geprüft [@pauwels2011semantic]; Beach et al. trennen dabei Domänen-, Regel- und Datenformatsemantik [@beach2015rulebased]. Die Laufzeit semantischer Prüfverfahren streut stark [@pauwels2017performance], was für eine Prüfung in Echtzeit relevant ist.
- **Trennung von Wissen, Modell und Ablauf.** Dimyadi et al. beschreiben einen offenen, grafisch dokumentierten Prüfablauf, der vom Gebäudemodell und vom Regelwissen getrennt ist [@dimyadi2016computerizing].

**Kritische Würdigung.** Die Linie hat überzeugend begründet, warum Regeln transparent und von der Prüfmaschine getrennt sein müssen. Behörden und Planende müssen nachvollziehen können, warum eine Regel verletzt ist. Die Evaluationen bleiben aber meist bei Machbarkeitsbeispielen (E1). Die Ausnahme ist Häußler et al., deren Befund jedoch aus der Eisenbahninfrastruktur stammt.

### 5.2.3 Regelextraktion aus Normtext

Der Engpass jeder Prüfung ist die Übersetzung von Normtext in eine ausführbare Form:

- **Semantische Auszeichnung.** Hjelseth und Nisbet schlugen mit RASE (Requirement, Applicability, Selection, Exception) eine Annotation vor, aus der prüfbare Aussagen entstehen und sich zur Kontrolle in Prosa zurückführen lassen [@hjelseth2011capturing].
- **Regelbasiertes NLP.** Zhang und El-Gohary extrahierten quantitative Anforderungen aus dem International Building Code mit einer Präzision von 0,969 und einem Recall von 0,944 [@zhang2016semantic]. Später verbanden sie Extraktion, Logikklauseln und Schlussfolgern zu einem vollautomatischen System [@zhang2017integrating].
- **Neuronale Parser.** Die Gruppe um Amor übersetzte neuseeländische Vorschriften nach LegalRuleML. Die Qualität reichte nicht für vollautomatische Übersetzung, wohl aber für eine Autovervollständigung [@fuchs2022neural]. Zwischenrepräsentationen verbesserten das Parsing weiter [@fuchs2024intermediate].
- **Korpora.** CODE-ACCORD umfasst 862 annotierte Sätze englischer und finnischer Bauvorschriften [@hettiarachchi2025codeaccord]. BRISE-Plandok ist das einzige gefundene **deutschsprachige** Korpus. Es enthält über 7000 Sätze aus dem Flächenwidmungs- und Bebauungsplan der Stadt Wien, manuell mit formalen Regeln annotiert [@recski2024briseplandok].
- **Berechenbarkeit und Mehrdeutigkeit.** Zhang und El-Gohary analysieren per Clusterbildung, welche Normanforderungen überhaupt berechenbar sind [@zhang2021clustering]. Zhang, Ma und Nisbet zeigen, dass Mehrdeutigkeit eine eigene Hürde der Formalisierung ist [@zhang2023unpacking]. Eine Übersicht derselben Gruppe zur Regelerfassung hält fest, dass heutige Repräsentationen Unbekannte, Nebenwirkungen und mehrdeutige Regeln nicht abbilden [@zhang2023rule].

**Befund für die Arbeit.** Für die BayBO, die Bayerischen Technischen Baubestimmungen und die holzbaurelevanten DIN-Normen gibt es weder ein annotiertes Korpus noch eine Evaluation. BRISE-Plandok zeigt, dass ein deutschsprachiges Korpus möglich ist. Es betrifft aber Wiener Planungsrecht und nicht die Bauordnung. Hinzu kommt eine rechtliche Grenze: Normtexte sind urheberrechtlich geschützt (Kapitel 4.9). Eine maschinelle Extraktion aus DIN-Texten ist deshalb auch rechtlich nicht der naheliegende Weg.

### 5.2.4 Sprachmodelle in der Regelprüfung (2023 bis 2026)

Seit 2023 wächst die Zahl der Arbeiten, die große Sprachmodelle (Large Language Models, LLM) für die Regelprüfung einsetzen, sehr schnell. Zwei Übersichten nennen als offene Probleme Erklärbarkeit, Human-in-the-Loop, Rückverfolgbarkeit und Benchmarking [@senousy2026automated; @lee2026automated].

| Arbeit | Ansatz | berichtete Leistung | Evaluationsbasis | Stufe |
|---|---|---|---|---|
| Chen et al. 2024 [@chen2024automated] | LLM plus Deep Learning plus Ontologie zur Regelextraktion | Effizienzgewinn behauptet, kaum quantifiziert | Fallbeispiel | E1 |
| Yang & Zhang 2024 [@yang2024promptbased] | Prompt-basierte Übersetzung in Logikprogramme | Präzision 97,4 %, Recall 95,9 % | 51 Anforderungen des IBC 2015 | E2 |
| Madireddy et al. 2025 [@madireddy2025large] | LLM erzeugt Python-Prüfskripte in Revit | Zeitersparnis gegenüber manueller Prüfung | ein Einfamilienhaus, ein Bürogebäude | E1 |
| Shi et al. 2025 [@shi2025finetuning] | feinabgestimmtes Mistral 7B mit RAG erzeugt Skriptentwürfe, Fachleute verfeinern | Entwürfe für reale Regel-Skript-Paare | Singapur | E2 |
| Iversen & Huang 2026 [@iversen2026leveraging] | LLM interpretiert Vorschriften direkt, extrahiert Daten, prüft | F1 97 % (Klassifikation), 97,7 % Ausführung, besser als naive Baseline | DSR-Artefakt, eigene Testmenge | E2 |
| Zheng et al. 2026 [@zheng2026translating] | LLM ordnet Klauseln 66 atomaren Funktionen zu und komponiert Code | 19 % besser als Fine-Tuning beim Funktionsabgleich | eigene Klauseln, Fallstudie | E2 |
| Lin et al. 2026 [@lin2026defects] | LLM erkennt und korrigiert merkmalsbezogene Modellfehler | Halluzinationskontrolle hebt Genauigkeit von 64 % auf 85 % | eigene Testmodelle | E2 |
| Mirhosseini et al. 2026 [@mirhosseini2026ambiguity] | Agent übersetzt Vorschrift in Logik, IfcOpenShell prüft deterministisch | „zero hallucination“ als Selbstangabe | australischer NCC | E1–E2 [U] |
| Saluz et al. 2025 [@saluz2025semio] | LLM richtet Kit-of-Parts-Modell auf OWL-Regeln aus, Reasoner prüft | vier LLMs verglichen | kleiner Brandschutz-Testfall | E1 |

**Kritische Würdigung.** Die Tabelle zeigt ein einheitliches Muster:

1. **Die Zahlen sind hoch, die Basis ist schmal.** Genauigkeiten über 95 % beruhen auf wenigen Dutzend selbst gewählter Anforderungen, meist aus dem IBC. Ein unabhängiger Goldstandard fehlt fast immer. CODE-ACCORD ist der erste öffentliche Benchmark [@hettiarachchi2025codeaccord], deutschsprachige Regeln enthält er nicht.
2. **Ausführungstreue wird selten geprüft.** Pinto et al. zeigen den blinden Fleck des Feldes [@pinto2026exhaustive]. Sie prüften ein frei verbreitetes Prüfwerkzeug für Lehmbauvorschriften durch vollständige Aufzählung von über 292 Milliarden Eingabekonfigurationen. Dabei fanden sie drei Ausführungsfehler, und die Regelsätze wichen in 8,26 % des Definitionsbereichs voneinander ab. Die Forschung konzentriert sich darauf, ob eine Regel extrahiert werden kann, und kaum darauf, ob sie danach richtig ausgeführt wird.
3. **Für haftungsrelevante Freigaben reicht das nicht.** Eine Fehlerquote von 3 % oder 15 % ist für eine Forschungsarbeit ein gutes Ergebnis. Für eine Aussage „zulässig nach BayBO“, die eine bauvorlageberechtigte Person unterschreibt, ist sie es nicht (Kapitel 4.3.5).

Die Arbeiten, die ein LLM nur zur Interpretation einsetzen und die Prüfung einem deterministischen Kern überlassen [@mirhosseini2026ambiguity; @saluz2025semio; @shi2025finetuning], weisen deshalb in die Richtung dieser Arbeit. Keine von ihnen erzeugt aber einen Entwurf.

### 5.2.5 Von der Prüfung zur Entwurfsanpassung

Fast alle Arbeiten prüfen ein fertiges Modell nachträglich. Sobhkhiz et al. kritisieren diese Trennung von Entwurf und Prüfung ausdrücklich [@sobhkhiz2021framing]. Sie belaste die Planenden mit iterativen Korrekturen, und eine proaktive Prüfung setze stabile Datenstandards und Modellierungsrichtlinien voraus. Seit 2025 entsteht eine Linie, die die Prüfung als Ausgangspunkt der Anpassung versteht:

- Wu et al. schlagen mit „Design Healing“ vor, nicht konforme Entwürfe automatisch in konforme Alternativen zu überführen. Die Alternativen werden nach ihrer Nähe zum Ausgangsentwurf gewichtet [@wu2025design].
- Wu et al. analysieren am Beispiel der Barrierefreiheitsanforderungen des IBC, welche Regelmerkmale eine automatische Anpassung überhaupt erlauben [@wu2026revisiting].
- Wu et al. lassen ein LLM menschlich formulierte Verbesserungsstrategien in Bauteiloperationen übersetzen. Die Ausführung bleibt regelgebunden, der Änderungsumfang bleibt unter der Kontrolle des Planers [@wu2026alterations].
- CODE-COMPANION formalisiert ausgewählte Vorschriften als deterministische Regeln und gibt in Revit Rückmeldung während des Entwurfs. Validiert wurde es an zwei Entwürfen für ein Grundstück in Istanbul [@tonguc2026code].
- D-CodeWeaver integriert priorisierte Regeln als parametrische Regeln in den frühen Entwurf von modularem Holzwohnungsbau. Ausdrücklich wird dabei keine vollständige Prüfung angestrebt [@erhan2026dcodeweaver].

**Kritische Würdigung.** Die Linie ist die fachlich nächste Nachbarschaft der Arbeit. Sie verlagert die Regel vom Prüfer in den Entwurf. Drei Einschränkungen bleiben aber. Erstens sind die Nutzer Planende, nicht Laien. Zweitens betreffen die Regeln Barrierefreiheit, Raumgrößen oder Kubatur, nicht das Zusammenspiel von Bauordnung, Normen und Herstellerregeln. Drittens liegen die Evaluationen auf Stufe E1, und zwei der Arbeiten sind Tagungsbeiträge.

### 5.2.6 Digitaler Bauantrag

Die Anwendung der Regelprüfung im Genehmigungsverfahren wird unter dem Begriff Digital Building Permit (DBP) untersucht. Das europäische Netzwerk EUnet4DBP ordnete den Forschungsbedarf in die drei Säulen Prozess, Regeln und Technologie [@noardo2020integrating]. Die kritische Übersicht von Noardo et al. stellt fest, dass die Forschung technisch fragmentiert ist und selten Verwaltungsprozess, rechtliche Einbettung und Datenbereitstellung zugleich adressiert [@noardo2022unveiling]. Bloch et al. bestätigen das in einem systematischen Review: Die Forschung betrachtet fast nur die Regelprüfung, während Teilprozesse, Beteiligte und Zuständigkeiten kaum untersucht sind [@bloch2023unbalanced]. Eine Taxonomie des Genehmigungssystems und ein Sammelband bündeln den internationalen Stand [@fauth2024taxonomy; @fauth2026digital]. Laut Ataide et al. sind die meisten Behörden bei Portal und elektronischer Akte angekommen, die automatische Prüfung gibt es nur in Pilotstädten [@ataide2023digital].

**Europäische Projekte.** Das Horizon-Projekt CHEK legte für den digitalen Bauantrag eine IFC-Spezifikation fest [@chek2024d22]. Sie enthält IFC4 ADD2 TC1 mit Reference View und Raumbegrenzungen zweiter Ordnung, Anforderungen als IDS 1.0 und geometrische Prüfungen als Microservices. Fehlende Merkmale stehen in einem eigenen Property Set. Die Stadt Wien betreibt einen openBIM-Bauantrag (BRISE) [@krischmann2020entwicklung; @urban2024adapting]. Urban et al. beschreiben die Methodik der Regelentwicklung dort und erproben sie an 24 realen Bauvorhaben mit mehreren Autorenwerkzeugen [@urban2026development]. Ihr zentrales Artefakt ist eine Regulation Information Matrix. Sie dokumentiert Rechtsauslegung, Informationsbedarf, Umsetzungsentscheidung und Validierungsergebnis je Regel. Das ist unter den gesichteten Arbeiten die belastbarste Evaluation der Regelentwicklung im Behördenbetrieb (Stufe E4, Pilotbetrieb).

**Deutschland [V].** Drei Arbeitsstände sind maßgeblich:

- Das Zukunft-Bau-Projekt „BIM-basierter Bauantrag“ entwickelte eine Modellierungsrichtlinie auf Basis der MBO mit XBau-Datenübernahme, formaler Modellvorprüfung und BCF-Kommunikation [@bimbauantrag2020; @bimbauantrag2020abschluss].
- MBO2BIM formalisierte Vorgaben der Musterbauordnung. Formale Prüfregeln liegen in MVD und IDS, fachliche in OpenBIMRL; umgesetzt wurde vor allem die Gebäudeklasse [@mbo2bim2023; @stepien2023openbimrl].
- Die Machbarkeitsstudie NRW 2026 empfiehlt eine formale Vorprüfung per IDS und öffentliche IDS-Dateien [@nrw2026bimbauantrag].

In Bayern werden Bauvorlagen dagegen als PDF hochgeladen. Ein IFC-Modell kann nur als Anlage übermittelt werden [@dbauv2026] (Kapitel 4.3.6).

**Planungsrecht und Geodaten.** Olsson et al. inventarisierten, welche Festsetzungen schwedischer Bebauungspläne automatisch prüfbar sind, und prüften Gebäudehöhe und Grundfläche mit BIM und Geodaten [@olsson2018automation]. İlal ordnet in einer Übersicht die BIM-GIS-Integration für die Prüfung gegen Bebauungspläne [@ilal2022integrating]. Battisti et al. identifizierten mit Beteiligten einer österreichischen Baubehörde acht algorithmisch automatisierbare Prüfaufgaben [@battisti2022automatic].

**Holzrahmenbau.** Narayanaswamy et al. prüften kommunale Satzungsregeln und Wandrahmenregeln für Holzrahmen-Wohngebäude in Alberta [@narayanaswamy2019bim]. Die Regeln sind in drei Komplexitätsgruppen geordnet und an Bauobjekte gebunden. Das ist die nächste Vergleichsarbeit für eine Bauantragsprüfung im Holzrahmenbau. Sie folgt aber kanadischem Recht und arbeitet in Revit.

**Kritische Würdigung.** Die Bauantragsforschung ist in zwei Richtungen einseitig. Sie denkt die Prüfung von der Behörde her, nicht vom Entwurfsverfasser. Und sie setzt Modelle voraus, die von Architekten in Autorenwerkzeugen erstellt wurden; deren schwankende Qualität ist dann das Hauptproblem [@noardo2022ifc]. Ein Szenario, in dem der Hersteller das Modell regelbasiert erzeugt und die Konformität schon bei der Erzeugung sichert, kommt in dieser Literatur nicht vor. Für Bayern und die BayBO ist keine Modellierungsrichtlinie mit Prüfregeln dokumentiert.

### 5.2.7 Normen und Recht als maschinenlesbare Daten

Die Idee, Rechtsnormen als ausführbare Logik zu fassen, reicht bis zum British Nationality Act zurück [@sergot1986british]. Unter „Rules as Code“ sollen menschen- und maschinenlesbare Fassung gemeinsam entstehen, damit die maschinenlesbare autoritativ wird [@mohun2020cracking]; die Skalierungsprobleme sind beschrieben [@mowbray2023representing]. Catala modelliert Ausnahmen mit Default-Logik eng am Gesetzestext [@merigoux2021catala]. LegalRuleML bildet deontische Modalitäten, Defeasibility und zeitliche Geltung ab [@palmirani2011legalruleml] und wurde für die Bauwirtschaft als geeignet bewertet [@dimyadi2017evaluating]. Für Bauvorschriften untersuchten Fuchs et al. in Interviews mit Regelsetzern weltweit, ob Vorschriften parallel in natürlicher und formaler Sprache verfasst werden können [@fuchs2025exploring].

Aus der Normung kommt das Reifegradmodell der SMART Standards. Es reicht vom Papierdokument (Stufe 0) bis zu maschinensteuerbaren Inhalten (Stufe 5) [@idis2021szenarien]. Zentgraf et al. schlagen vor, Normen im Format NISO-STS um maschinenlesbare Anforderungen und Prüfregeln anzureichern [@zentgraf2023concept].

**Befund für die Arbeit.** Weder BayBO noch Technische Baubestimmungen noch holzbaurelevante DIN-Normen liegen als autoritative, maschineninterpretierbare Fassung vor. Jede Formalisierung ist derzeit eine nicht amtliche Interpretation. Sie braucht deshalb Quellenbezug, Version, Geltungszeitraum und Testfälle. Genau das verlangen auch Amor und Dimyadi [@amor2021promise] und die Regulation Information Matrix aus Wien [@urban2026development].

### 5.2.8 Zwischenfazit 5.2

| Linie | Stärke | Grenze | Evaluationsniveau | Übernahme |
|---|---|---|---|---|
| Taxonomien [@eastman2009automatic; @solihin2015classification] | gemeinsamer Bezugsrahmen, Komplexitätsklassen | keine Wirkungsmessung | E0–E1 | Gliederung der Prüfschicht; Trennung IDS vs. Regelmaschine |
| transparente Regelsprachen [@haeussler2021code; @stepien2023openbimrl; @moult2020compliance] | nachvollziehbar, pflegbar | selten Geometrie in Echtzeit | E1, vereinzelt E2 | Regeln als Daten mit Testfällen |
| NLP-Regelextraktion [@zhang2017integrating; @fuchs2022neural; @recski2024briseplandok] | senkt Formalisierungsaufwand | englische Korpora, Urheberrecht an Normen | E2 | nur als Hilfe bei der Regelpflege |
| LLM-Prüfung [@iversen2026leveraging; @lin2026defects] | hohe Werte an kleinen Mengen | kein Goldstandard, Ausführungstreue ungeprüft [@pinto2026exhaustive] | E2 | nicht zur Laufzeit; Rolle des LLM begrenzen |
| Prüfung im Entwurf [@wu2025design; @tonguc2026code; @erhan2026dcodeweaver] | Regel wirkt früh | Planer als Nutzer, schmale Regelbasis | E1 | Ablehnen mit Alternative (Kapitel 9.5) |
| digitaler Bauantrag [@chek2024d22; @urban2026development; @mbo2bim2023] | IDS plus Geometrie-Dienste, realer Behördenbetrieb | Behördensicht, fremde Autorenmodelle | E1–E4 | zweistufige Prüfung, Regulation Information Matrix |

## 5.3 Digitale Prozesskette im vorgefertigten Holzbau

### 5.3.1 Diagnose: frühe Festlegung und fragmentierte Modelle

Die Literatur stimmt in einer Diagnose überein: Vorfertigung verlangt, dass Entscheidungen früher fallen als im Massivbau. Das Handbuch von Kaufmann, Krötsch und Winter formuliert: Bauteilaufbauten, Elementierung, Installationsführung und Anschlussdetails müssen in frühen Leistungsphasen feststehen, weil sie später nur mit hohen Kosten zu ändern sind [@kaufmann2018manual]. Stehn und Bergström zeigten schon 2002 für den mehrgeschossigen Holzrahmenbau, dass kundenorientierte Entwurfsänderungen Störungen in der Produktion auslösen [@stehn2002integrated]. Johnsson und Meiling fanden bei zwei schwedischen Modulherstellern zwar eine bessere Produktqualität als im konventionellen Bau [@johnsson2009defects]; laut Recherche 11 stammen aber auch dort viele Mängel aus Planung und Informationsübergabe. In der Produktion industrieller Hausbauer werden Informationen noch oft manuell und auf Papier geführt [@eriksson2019assessing].

Die deutschsprachigen Forschungsprojekte bestätigen das (graue Literatur):

- **leanWOOD** entwickelte Prozess- und Kooperationsmodelle und holzbaugerechte Leistungsbilder [@kaufmann2018leanwood].
- **BIMwood** (TUM 2019 bis 2023; HSLU mit Partnern) stellt fest, dass BIM-Prozesse bisher auf mineralische Bauweisen abgestimmt sind [@tum2023bimwood; @geier2022bimwood; @schuster2022bimwood]. Der Luzerner Bericht diagnostiziert „überinformierte Modelle“ und widersprüchliche Daten an der Schnittstelle zum Holzbauunternehmen. Er schlägt eine Pull-Planung vom Fertigungsziel her vor [@geier2022bimwood].

Beide Projekte adressieren die Schnittstelle zwischen Planenden und Ausführenden. Die vorgelagerte Schnittstelle zwischen Bauherr und Planung ist nicht Gegenstand. Die Kette läuft bei BIMwood über verknüpfte Modelle und Dokumente, nicht über ein einziges IFC [@tum2023bimwood].

International ergänzen Übersichten dieses Bild [@yin2019building]. Abanda et al. nennen Interoperabilität und fehlende objektbezogene Fertigungsinformationen als wiederkehrende Hindernisse [@abanda2017bim]. Eine narrative Übersicht mit Softwaretests findet, dass BIM-Werkzeuge für Holz hinter Stahl und Beton zurückliegen [@loboscalquin2024implementation]. Das deutschsprachige Standardwerk zur Automatisierung im Holzbau beschreibt Fertigungsprinzipien und Automatisierungsstufen der Holzrahmenbau-Vorfertigung [@heinzmann2022automatisierung].

### 5.3.2 IFC im Holzbau

**Klassenmapping.** Ein Implementierungsleitfaden von buildingSMART für den Holzbau existiert nicht (Recherche 01). Die Fachgruppe „BIM im Holzbau“ von buildingSMART Deutschland arbeitet an einem Anwendungsfall mit IDS-Prüfregeln, der Stand ist aber nicht veröffentlicht (Recherche 01 und 06). Das in Recherche 01 am Schema geprüfte Mapping für die Holzrahmenwand nutzt `IfcWall` mit Aggregation, `IfcMember` (STUD, PLATE), `IfcPlate`, `IfcBuildingElementPart`, `IfcVoidingFeature` und `IfcMechanicalFastener`. Es ist schemakonform, aber in der Literatur nicht als Konvention beschrieben.

**Nachweise aus IFC.** Châteauvieux entwickelte an der TUM einen IFC-basierten Planungsprozess für den Schallschutz im Holzbau [@chateauvieux2023bim]. Eingangsmodelle werden zuerst geprüft und per „Model Healing“ korrigiert. Danach folgt eine Stoßstellenanalyse über semantische und geometrische Abfragen. Aus IFC-Modellen früher Phasen werden so 15 akustisch unterscheidbare Stoßstellentypen erkannt [@chateauvieuxhellwig2022timber]. Rojas Wettling et al. definierten ein IDM für die frühe Bewertung von Holzrahmenbauprojekten, validiert mit chilenischen Vorfertigern und abgeglichen mit IFC-Property-Sets [@rojaswettling2023idm]. Ramaji et al. erweiterten das IDM um ein Produktarchitekturmodell für vorgefertigte Bauten [@ramaji2017product]. Niemeijer et al. fanden, dass viele Parameter, die Architekten für Prüfungen brauchen, in IFC fehlen oder erst abgeleitet werden müssen, darunter Wandmaße, Dauerhaftigkeitsklassen von Holz und Gauben [@niemeijer2009checkmate].

**Gegenbefunde.** Drei Arbeiten zeigen, dass ein durchgängiges IFC bis zur Fertigung heute nicht Stand der Technik ist:

- Das Stuttgarter Co-Design mehrgeschossiger Holzbauten nutzte BHoM statt IFC als globales Gebäudemodell, weil ein interoperabler Standard fehle [@orozco2023codesign].
- Der Luzerner BIMwood-Bericht hält fest, dass sich Komponenten im IFC-Schema nicht parametrisieren lassen [@geier2022bimwood].
- Samarawickrama et al. schlagen für den vorgefertigten Holzbau eine „Parametric Geometry Governance“ vor. Die gemeinsame Quelle ist dort ein Grasshopper-Modell, aus dem Fachmodelle für Dlubal und Cadwork entstehen. Evaluiert ist das als Machbarkeitsnachweis in Australien [@samarawickrama2026digital].

**Kritische Würdigung.** Die Gegenbefunde sind ernst zu nehmen, aber sie widerlegen die These der Arbeit nicht. Sie zeigen, dass *Autorenwerkzeuge* den Austausch über IFC nicht tragen und dass eine *parametrische* Beschreibung im IFC-Schema fehlt. Beides betrifft ein Modell, das von Hand erzeugt und zwischen Programmen ausgetauscht wird. Ob ein Modell, das aus einem Parametermodell regelbasiert *generiert* wird, die Kette tragen kann, ist in der Literatur nicht untersucht. Die Parametrik liegt dann im Generator, nicht im IFC.

### 5.3.3 Regelbasiertes Framing und Ableitung von Fertigungsdaten

Die einzige zusammenhängende Forschungslinie zum automatisierten Detaillieren im Holzrahmenbau mit Industriepartnern stammt aus der Gruppe um Al-Hussein an der University of Alberta und ihrem Umfeld (Recherche 12). Sie deckt die Kette vom Wandumriss bis zur Maschine in Einzelschritten ab:

| Schritt | Arbeit | Befund | Stufe |
|---|---|---|---|
| Werkstattpläne | Manrique et al. 2015 [@manrique2015automated] | parametrische Werkstattpläne für Wood Framing in Revit | E1 |
| Paneel-Detaillierung | Alwisy et al. 2019 [@alwisy2019bim] | MCMPro: aus 2D-CAD entstehen BIM, fertigungsorientiertes BIM und Werkstattpläne nach Platform Framing | E1 |
| Beplankung | Liu et al. 2018 [@liu2018bim] | regelbasiertes Plattenlayout und Zuschnittplanung mit minimalem Verschnitt | E2 |
| Mengen | Liu et al. 2016 [@liu2016ontology] | ontologiebasierte Mengenermittlung im Holzrahmenbau | E1 |
| Stückliste | Wang et al. 2019 [@wang2019automatic] | BIM-zu-ERP-Stückliste; 7,9 % Abweichung über 5 Projekte, unter 1 min statt 20–30 min (Recherche 11) | E2 |
| Framing nach Regeln | Abushwereb et al. 2019 [@abushwereb2019knowledge; @abushwereb2019framework] | FrameX: Framing nach Bauordnung, Transportregeln und Best Practice; −80 % Zeit an einer Referenzwand (Recherche 12) | E2 |
| Bauantragsprüfung | Narayanaswamy et al. 2019 [@narayanaswamy2019bim] | Satzungs- und Wandrahmenregeln in drei Komplexitätsgruppen | E1 |
| Fertigbarkeit | An et al. 2020 [@an2020bimbased] | Prüfung der Fertigbarkeit von Holzrahmen-Baugruppen gegen Maschinenrestriktionen (nur nach Titel und Screening) | ? |
| Panelisierung | Liu et al. 2021 [@liu2021panelization] | generative Wandteilung unter Tragwerks-, Produktions- und Logistikregeln, bewertet per Simulation | E2 |
| Maschinendaten | Darwish et al. 2022 [@darwish2022automated] | Regelsatz erzeugt CNC-Datei für eine Wandfertigungsanlage direkt aus BIM | E1 |
| Robotik | M. Tehrani & Alwisy 2025 [@mtehrani2025streamlining] | BIM-to-Bot für robotergestützte Wandtafelfertigung (nach Recherche 24) | ? |

Außerhalb Albertas ergänzen einzelne Arbeiten die Linie. Wong Chong und Zhang übersetzen IFC-Instanzen in Logikfakten und leiten daraus Fertigungsinformationen ab [@wongchong2021logic]. Cao et al. verknüpfen Bauteilmerkmale, Produktionsfähigkeiten und Fertigungsregeln in einer Ontologie. Laut Kurzfassung meldet ein Reasoner Verstöße gegen die Fertigbarkeit in Echtzeit an den Planer, erprobt an einem Holztafelbauprojekt [@cao2022ontologybased]. Day et al. kodieren explizites und implizites Wissen für vorgefertigte Holzrahmen-Außenwände und verlagern damit Entwurfsaufwand nach vorn [@day2019knowledge]. Fisher et al. teilen Wände unter Fertigungsrestriktionen automatisch in Tafeln [@fisher2024paad]. Thajudeen et al. zeigen für ein schwedisches Holzskelettsystem, dass eine parametrische Designplattform Anschlüsse 20-mal schneller modelliert [@thajudeen2022supporting].

**Kritische Würdigung.** Die Alberta-Linie ist der wichtigste Beleg, dass Framing-Regeln formalisierbar sind und Maschinendaten sich automatisch ableiten lassen. Ihre Evaluationsdesigns sind einfach und übertragbar: Zeit gegen manuelle Arbeit, Verschnitt gegen Praxis, Stückliste gegen die Arbeitsvorbereitung. Vier Grenzen verhindern eine direkte Übernahme:

1. **Proprietäre Umgebung.** Alle Werkzeuge laufen als Add-ins in Revit oder AutoCAD. Offener Code und IFC fehlen.
2. **Fremdes Regelwerk.** Die Regeln folgen dem kanadischen National Building Code mit Ständerabständen von 16 Zoll. Auf DIN EN 1995 und den deutschen Holzrahmenbau sind sie nicht übertragbar (Recherche 12).
3. **Kein Laie.** Die Eingabe ist ein fertiger Architektenplan.
4. **Einzelne Glieder.** Jede Arbeit behandelt einen Schritt. Eine Kette vom Entwurf bis zur Maschinendatei in einem Modell ist nicht dokumentiert.

### 5.3.4 Offene Werkzeuge und Fertigungsformate

Auf der Werkzeugebene stehen quelloffene Bausteine bereit, die aber kein IFC erzeugen:

- **COMPAS Timber** (ETH Zürich, MIT-Lizenz) bietet Balken, Platten, Verbindungen und BTLx-Export [@compastimber]. Laut Recherche 01 umfasst Version 2.2.0 rund 28 Verbindungstypen und 18 BTLx-Bearbeitungen. Es ist Software ohne begutachtete Systembeschreibung.
- **Reindeer** ist ein Grasshopper-Werkzeugsatz für fertigungsreife Holzdetails mit Verbindungssuche und BTLx-Export. Es setzt eine fertige Stabgeometrie voraus [@mork2020parametric].
- **BTLx 2.3** ist als Schema und Spezifikation frei verfügbar. Die Version enthält Attribute für Nägel, Schrauben und Klammern [@btlx23].
- **WUP**, das Format der Weinmann-Wandanlagen, ist proprietär. Die Spezifikation muss beim Hersteller angefragt werden (Recherche 01) [U].
- **dataholz.eu** liefert rund 1.500 geprüfte Konstruktionen und Anschlüsse mit Schichtaufbauten als IFC nach Registrierung, als IDS und als bSDD-Daten, aber keine Ständer und keine API [@dataholz] (Recherche 01).

Die Forschung zur robotischen Holzfertigung zeigt, wie weit Fertigungsattribute im Modell reichen können. Adel et al. integrierten Architektur-, Tragwerks- und Fertigungsconstraints in den Rechenentwurf robotergefertigter Holzrahmenmodule, mit Greifebene, Endschnitten und Bohrungen je Balken [@adel2018design; @adel2020computational] (Recherche 11), demonstriert an der DFAB HOUSE [@graser2020dfab]. Die transportable Roboterplattform TIM lässt sich auch in normale Zimmereien integrieren [@wagner2020flexible]. Apolinarska et al. übersetzten die Nagelabstände der SIA 265 in Ausschlussellipsen entlang der Faserrichtung und besetzten damit 815.984 Nagelpositionen algorithmisch; ein unabhängiges Skript prüfte das Ergebnis (Recherche 12) [@apolinarska2016mastering]. Das ist ein seltenes Beispiel für eine Norm, die *im* Erzeugungsalgorithmus wirkt. Die ETH-Arbeiten und das Sequential Roof betreffen aber Unikate mit hohem Forschungsaufwand, keine Serienfertigung mit Abbund- und Wandanlagen.

### 5.3.5 Industrielle und regionale Praxis

Aus der Praxis sind drei Ansätze dokumentiert, alle als graue Literatur:

- **Haas Fertigbau** bietet einen Konfigurator, in dem Kunden Modell, Grundriss, Heiztechnik, Dach und Fassade wählen. Er warnt vor Fehlplanungen und übergibt laut Anbieter über ein Revit-Add-in an die Produktion [@np2025haas]. Beleg ist nur eine Pressemitteilung.
- **DesignChain** (Fraunhofer IPA mit Wood Pro) erzeugt aus standardisierten Eingangsparametern, die vom Kunden oder aus Revit kommen, ein vollständiges 3D-Wandelement bis zum Nagelbild [@fraunhoferipa0000designchain].
- **Digital Craft** (Hochschule München, Zukunft Bau 2023 bis 2026) entwickelt ein digital geplantes und gefertigtes Holzstecksystem, in dem Primärkonstruktion, Wandaufbau, Fassade und Öffnungen aus einem Modell entstehen [@krueger2026steckhaus].

Recherche 03 hat die Konfiguratoren von fünf deutschen Fertighausherstellern gesichtet. Alle arbeiten mit Formularen oder 3D-Oberflächen, keiner mit Sprache.

**Kritische Würdigung.** Die Praxis zeigt, dass die Kette Konfigurator → Werk bei einzelnen Herstellern technisch existiert. Sie läuft aber über proprietäre Werkzeuge ohne IFC, ohne dokumentierte Regelbasis und ohne Bezug zum Bauantrag. Wissenschaftlich überprüfbar ist davon nichts.

### 5.3.6 Zwischenfazit 5.3

| Glied der Kette | beste dokumentierte Arbeit | Datenformat | Lücke |
|---|---|---|---|
| Regelbasiertes Framing | FrameX [@abushwereb2019knowledge], MCMPro [@alwisy2019bim] | Revit, AutoCAD | kanadisches Regelwerk, proprietär |
| Fertigbarkeit im Entwurf | An et al. [@an2020bimbased], Cao et al. [@cao2022ontologybased] | BIM, Ontologie | kein Laie, kein Bauantrag |
| Maschinendaten | Darwish et al. [@darwish2022automated], COMPAS Timber [@compastimber] | CNC-Datei, BTLx | kein IFC als Quelle; kein WUP |
| Holzbau-Nachweise aus IFC | Châteauvieux [@chateauvieux2023bim] | IFC | Eingangsmodelle müssen „geheilt“ werden |
| Durchgängiges Modell | Samarawickrama et al. [@samarawickrama2026digital] | Grasshopper | Einheit im Parametermodell, nicht im Standard |
| Prozess und Rollen | BIMwood [@tum2023bimwood] | verknüpfte Modelle und Dokumente | Schnittstelle Bauherr–Planung fehlt |

## 5.4 Mass Customization und Produktkonfiguration im Hausbau

### 5.4.1 Konzept und Fähigkeiten

Pine prägte „Mass Customization“ als Wettbewerbsstrategie: kundenindividuelle Produkte zu Kosten nahe der Massenfertigung [@pine1993mass]. Da Silveira et al. systematisieren Stufen der Individualisierung von der reinen Präsentationsvarianz bis zur kundenindividuellen Konstruktion [@dasilveira2001mass]. Piller beschreibt Mass Customization als Fähigkeit mit drei Voraussetzungen [@piller2004mass]. Salvador et al. verdichten sie zu drei strategischen Fähigkeiten [@salvador2009cracking]:

- **Solution Space Development:** den Lösungsraum festlegen
- **Robust Process Design:** Varianten ohne Qualitätsverlust liefern
- **Choice Navigation:** Kunden durch den Lösungsraum führen

Von Hippel beschrieb Nutzer-Toolkits, die Entwurfsarbeit auf den Nutzer verlagern [@vonhippel2001user; @vonhippel2002shifting]. Ein Toolkit gibt Freiheit innerhalb eines begrenzten Lösungsraums und stellt sicher, dass der Entwurf ohne Änderung auf dem Produktionssystem gefertigt werden kann. Das ist die ökonomische Formulierung der Leitidee dieser Arbeit: Der Kunde entwirft im Regelraum des Herstellers.

Die Trias lässt sich unmittelbar zuordnen. Der Lösungsraum entspricht dem formalisierten Regelraum aus Recht, Norm und Herstellerregeln. Der robuste Prozess entspricht der Ableitung aller Unterlagen aus einem Modell. Die Choice Navigation ist die Aufgabe der Sprachschnittstelle.

### 5.4.2 Wissensbasierte Konfiguration

Die informationstechnische Umsetzung des Lösungsraums ist Gegenstand der Konfigurationsforschung. Ihr Referenzpunkt ist der regelbasierte Konfigurator R1/XCON für Computersysteme [@mcdermott1982rulebased]. Seine betriebliche Wirkung ist als Fallstudie belegt [@sviokla1990examination]. Sabin und Weigel unterscheiden regelbasierte, modellbasierte und fallbasierte Ansätze [@sabin1998product]. Felfernig et al. fassen die wissensbasierte Konfiguration zusammen [@felfernig2014knowledge]. Konfiguration wird dort als Constraint-Satisfaction-Problem über Komponenten, Attribute und Verbindungen formalisiert. Zum Repertoire gehören Konsistenzprüfung, Vervollständigung und die Diagnose widersprüchlicher Kundenanforderungen. Bedingte Constraint-Probleme bilden Optionen ab, die weitere Constraints aktivieren [@gelle2003solving]. Für Konfigurationskonflikte gibt es eigene Auflösungsverfahren [@yang2012constraint].

Vorgehensmodelle für Produktmodellierung und Konfiguratorentwicklung liegen vor [@forza2006product; @hvam2008product; @haug2012definition].

**Befund für die Arbeit.** Die Konfigurationsforschung liefert eine reife Theorie der *Gültigkeit* von Konfigurationen und der *Erklärung von Konflikten*. Beides fehlt rein generativen, lernbasierten Verfahren (Abschnitt 5.5). Für das Prinzip „Ablehnen mit Begründung und Alternative“ (Kapitel 9.5) ist die Konfliktdiagnose der direkte Baustein.

### 5.4.3 Empirische Wirkung von Konfiguratoren

Die Wirkung von Konfiguratoren ist außerhalb des Bauwesens großzahlig belegt:

- In 238 Werken aus drei Branchen und acht Ländern verbessert der Einsatz von Konfiguratoren die Zeitperformance bei kundenindividuellen Produkten, auch nach Kontrolle anderer Einflussgrößen [@trentin2011overcoming].
- In 14 technikorientierten Firmen sinkt die Angebotsdurchlaufzeit im Mittel um 85,5 % [@haug2011impact].
- Bei einem Pumpenhersteller sanken die Personalstunden über fünf Jahre um 75 % [@kristjansdottir2018return].
- Die Nutzung eines Konfigurators verbessert die Produktqualität, schwächer bei schwer bestimmbarem Kundenbedarf [@trentin2012product].

Die Gegenseite ist ebenso belegt. Kristjansdottir et al. ordnen die Hürden bei Einführung und Nutzung in sechs Kategorien, darunter Produktmodellierung, Organisation und Wissenserwerb [@kristjansdottir2018challenges]. Haug et al. zeigen an acht gescheiterten Konfiguratorprojekten, wie sich Fehlentscheidungen über die Projektphasen aufschaukeln [@haug2019causes]. Im industriellen Hausbau der USA sinkt die betriebliche Leistung mit steigender Individualisierung [@nahmens2011customization].

**Kritische Würdigung.** Die Zeitwirkung gilt für Angebot und Dokumentation in Industrien mit stabiler Produktarchitektur. Sie auf die Planungsschleifen eines Fertighauses zu übertragen, ist eine Hypothese und kein Befund. Die Arbeit von Nahmens und Bindroo zeigt zudem, dass Freiheit ohne begrenzenden Regelraum Kosten verursacht. Das stützt nicht die Individualisierung an sich, sondern ihre Bindung an einen formalisierten Lösungsraum.

### 5.4.4 Plattformen im industriellen Hausbau

Die skandinavische Forschung beschreibt den industriellen Hausbau als Bündel aus Prozessen, technischem System, Vorfertigung, Lieferbeziehungen und Kundenorientierung [@lessing2015industrialised]. Ihr Kern ist das Plattformdenken:

- Eine Plattform umfasst Komponenten, Prozesse, Wissen und Beziehungen. In der Praxis bleibt sie oft implizit [@jansson2014platform].
- Der Grad der Vorab-Festlegung (Engineer-, Modify-, Configure-to-Order) bestimmt die Informationsflüsse zwischen Vertrieb, Planung und Produktion [@johnsson2013production].
- Veenstra et al. entscheiden methodisch, welche Module standardisiert werden, und klassifizieren sie nach räumlicher Nutzung [@veenstra2006methodology].
- Malmgren et al. beschreiben ein Produkt in vier Sichten: Kunde, Engineering, Produktion und Montage. Der Informationsfluss stromaufwärts zum Kunden fehlt in der Praxis und führt zu Ad-hoc-Lösungen [@malmgren2010product; @malmgren2010customization].
- „Architektonische Objekte“ übersetzen Kundenanforderungen in die Fähigkeiten eines Plattformsystems [@wikberg2014design]. Konfiguration geschieht durch Parametrisierung von Bauteilen [@jensen2012configuration; @jensen2015product].
- Sandberg et al. testeten ein wissensbasiertes Treppenwerkzeug, mit dem ein Verkäufer im Gespräch mit dem Kunden Folgen für Balken und Kosten prüft [@sandberg2008knowledge].
- Popovic et al. kombinieren die Design Platform mit einem produktorientierten IDM. Die Exchange Requirement Specification ordnet jedem Plattformattribut je Austauschmodell einen Status zu: generiert, modifiziert, weitergereicht oder wiederverwendet [@popovic2021configuration; @popovic2020development].
- Lennartsson et al. untersuchten die technische Plattform in zwei Hausbauunternehmen mit mehr als 50 Praktikern [@lennartsson2022exploring]. Laut Recherche 11 erodieren starke Kunden die Plattform, wenn Komponenten ohne Wirkungsanalyse hinzukommen. Engineering-Assets liegen ungeordnet vor [@lennartsson2021plm; @andre2019exploring].
- Architekten erleben Plattformgrenzen als schwer verständlich [@jansson2018artistic].
- Zhou unterscheidet in neun Firmen Plattformen als Bausatz, mit Schnittstellen und mit Designregeln [@zhou2023platforming].

Den Referenzfall für Mass Customization im Hausbau liefern die japanischen Hersteller [@gann1996construction; @barlow2003choice; @barlow2005building; @linner2012evolution]. Die Auswahl erfolgt dort im Ausstellungszentrum mit Beratern, nicht durch den Kunden allein.

**Deutscher Markt.** Zwei Arbeiten betreffen deutsche Hersteller unmittelbar. Thuesen und Hvam beschreiben eine deutsche Hausplattform, die die Kosten um mehr als 30 % senkte [@thuesen2011efficient]. Schoenwitz et al. werteten 16 Projekte eines deutschen Hausbauers über 35 Jahre aus [@schoenwitz2012nature]. Die Zahl der Kundenänderungen gegenüber der Standardbaubeschreibung stieg deutlich, und die Kunden waren bereit, zunehmend mehr dafür zu zahlen. Eine Folgestudie fordert, Produktarchitektur, Lage des Kundenentkopplungspunkts und Kundenpräferenzen aufeinander abzustimmen [@schoenwitz2017product]. Darüber hinaus ist der deutsche Fertighausmarkt in der begutachteten Literatur kaum untersucht. Larsen et al. kommen in ihrer Übersicht zu Mass Customization im Hausbau zum selben Schluss: großes Potenzial, aber wenig Forschung, vor allem zum Lösungsraum und zu Werkzeugen der Choice Navigation [@larsen2019mass].

### 5.4.5 Der Laie als Nutzer

Aus der Marketingforschung stammen Befunde, die für eine Kundenschnittstelle zentral sind:

- **Bedarfs- statt Parameterorientierung.** Randall et al. zeigen experimentell, dass bei parameterbasierten Schnittstellen das Ergebnis mit der Expertise des Nutzers steigt. Für Laien liefert eine bedarfsbasierte Schnittstelle bessere Ergebnisse [@randall2007user; @randall2005principles]. Eine Sprachschnittstelle ist bedarfsorientiert.
- **Selbst entworfen.** Franke et al. weisen nach, dass selbst gestaltete Produkte höher bewertet werden [@franke2010designed].
- **Wahlüberlastung.** Iyengar und Lepper zeigten, dass große Auswahl Entscheidung und Zufriedenheit mindern kann [@iyengar2000choice]. Die Meta-Analyse von Scheibehenne et al. findet einen mittleren Effekt nahe null bei großer Heterogenität [@scheibehenne2010choice]. Chernev et al. nennen die Moderatoren: Komplexität des Auswahlsets, Schwierigkeit der Aufgabe, Präferenzunsicherheit und Entscheidungsziel [@chernev2015choice]. Der Hauskauf erfüllt nach eigener Einschätzung alle vier. Mehr konfigurierbare Module erhöhen den Nutzen, aber auch die wahrgenommene Komplexität [@dellaert2005marketing].
- **Fähigkeiten von Vertriebskonfiguratoren.** Trentin et al. validierten fünf Fähigkeiten: fokussierte und flexible Navigation, leichter Vergleich, Nutzen-Kosten-Kommunikation und benutzerfreundliche Produktraumbeschreibung [@trentin2013sales]. Sie erhöhen den wahrgenommenen Nutzen des Laien [@trentin2014increasing].

Im Hausbau selbst ist die Laienforschung schmal. Die wichtigsten Arbeiten:

- **Khalili-Araghi und Kolarevic** entwickelten einen Rahmen für die dimensionale Anpassung durch Kunden auf Basis eines constraintbasierten Parametermodells [@khalili2016development]. Sie formulieren das Problem, das diese Arbeit adressiert, ausdrücklich: Die Herausforderung der Kundenbeteiligung liege vor allem in der Validierung des Entwurfs, besonders in der Prüfung gegen die Bauvorschriften. Eine Folgearbeit untersucht das Verhältnis von Variabilität und Gültigkeit [@khaliliaraghi2020variability].
- **Kwieciński et al.** entwickelten mit HOPLA ein System, in dem Laien ein Haus innerhalb vorgegebener Architekturregeln konfigurieren [@kwiecinski2014system; @kwiecinski2018hopla]. In Nutzertests auf zwei Kontinenten verglichen sie die Modifikation eines Vorschlags mit dem Entwurf von Null [@kwiecinski2019customers]. Die Studie von 2023 prüft Nutzerentscheidungen mit formalisierten Regeln [@kwiecinski2023interactive]. Laut Recherche 11 wollen Laien vor allem den Grundriss steuern und wünschen sich als Ergebnis zuerst die Baukosten. Die Stichproben sind klein, die Interaktion lief über einen Multi-Touch-Tisch.
- **Puusepp et al.** analysierten einen Live-Konfigurator eines estnischen Fertighausherstellers mit Echtzeitkosten [@puusepp2017enabling]. Laut Recherche 11 bemerkten viele der 133 ausgewerteten Nutzer die Preisänderung nicht.
- **Swanenburg** verglich in einem randomisierten Online-Experiment mit Kaufinteressenten zwei Konfiguratorformen gegen eine Kontrollgruppe mit Standardhaus [@swanenburg2016towards]. „Process enjoyment“ und „design freedom“ erklärten den Kundennutzen. Die Arbeit ist eine nicht begutachtete Masterarbeit.
- **Raposo et al.** entwickelten und testeten eine grafische Oberfläche für Co-Design im Wohnungsbau [@raposo2024bridging]. **Hentschke et al.** legten einen Rahmen für die Kundenintegration in Mass-Customised-Housing-Projekten vor [@hentschke2020customer].
- **Niemeijer et al.** wollten Käufern erlauben, einen Serienentwurf zu ändern, solange Architekten- und Baurechtsregeln nicht verletzt sind [@niemeijer2009checkmate; @niemeijer2014freedom] (Abschnitte 5.6 und 5.7).

**Konfiguratoren mit Bausystembezug.** Mehrere Arbeiten koppeln die Konfiguration an ein Bausystem, aber jeweils nur teilweise:

- Cao et al. vereinen einen Konfigurator über ein fertigungsbereites Kit-of-Parts mit Produktionsregeln über Lageplan, Grundriss und 3D-Modell [@cao2021cross].
- Wang und Chen verknüpfen ein generatives Layout mit vorgenehmigten Grundrissen und einen wissensbasierten Recommender mit zertifizierten Materialkatalogen nach der Bauordnung von British Columbia [@wang2024cloud].
- Bakhshi et al. beteiligen Kunden an der Konfiguration von Offsite-Bauten, gesteuert über Montageinformationen im BIM-Modell (Revit/Dynamo, Proof of Concept) [@bakhshi2021dfma].
- Shafiee et al. führen einen Web-Konfigurator für eine Garage bis zu Anschlussdetails und Produktionsdokumenten [@shafiee2025enhancing] (Abschnitt 5.7).
- Das Zukunft-Bau-Projekt Variowohnen Kassel entwickelte einen wissensbasierten BIM-Wohnungskonfigurator mit Regeln in den Objekten serieller Elemente und open BIM über IFC [@eisfeld2022variowohnen]. Er ist ein Planerwerkzeug und nur über die Kurzfassung bekannt.
- Piroozfar et al. und Farr et al. nutzen BIM als Konfigurationsplattform [@piroozfar2019configuration; @farr2014bim]. BIM-Autorensysteme bleiben dabei Expertenwerkzeuge.

Die architekturtheoretische Grundlage liefert Habrakens Trennung von dauerhafter Tragstruktur („Support“) und individuell bestimmbarem Ausbau („Infill“) [@habraken2021supports], die das Open Building zu einem Ebenenmodell ausbaute [@kendall2000residential]. Sie passt zur Plattformlogik des Fertighauses: Raster und tragende Elementierung sind fest, Grundriss und Ausbau variabel.

### 5.4.6 Zwischenfazit 5.4

Die Mass-Customization-Forschung liefert den Begriffsrahmen und die formalen Mittel. Die Plattformforschung liefert die Datenmodelle. Die Marketingforschung liefert Gestaltungsregeln für Laien. Drei Befunde tragen die Arbeit:

1. Laien können in einem regelbegrenzten System Entwürfe erzeugen, die ihren Erwartungen entsprechen [@kwiecinski2019customers; @kwiecinski2023interactive]. Die Validierung gegen die Bauvorschriften ist dabei die Kernaufgabe [@khalili2016development].
2. Bedarfsorientierte Schnittstellen helfen Laien mehr als parameterorientierte [@randall2007user].
3. Bei einem deutschen Hausbauer änderten Kunden über 35 Jahre zunehmend mehr und zahlten dafür [@schoenwitz2012nature].

Keine der gefundenen Arbeiten verbindet diese Befunde mit einer natürlichsprachlichen Choice Navigation, einem vollständig formalisierten Holzrahmenbau-Regelraum und einer Übergabe an Fertigung und Genehmigung.

## 5.5 Generatives Design, Grundriss- und Möblierungssolver

### 5.5.1 Begriffe

Caetano, Santos und Leitão grenzen parametrisches, generatives und algorithmisches Design voneinander ab [@caetano2020computational]. In ihrer Terminologie ist das Vorgehen dieser Arbeit **regelbasiert-generativ**: Eine Regelbasis erzeugt aus Kundenanforderungen Entwurfsvarianten. Sie besteht aus Plattform, Normen und Fertigungsrestriktionen. Maschinelles Lernen übernimmt dabei die Übersetzung von Sprache in formale Anforderungen und nicht die Geometrieerzeugung.

Weber, Mueller und Reinhart gliedern die automatische Grundrissgenerierung in Bottom-up-, Top-down- und referenzielle Verfahren und schlagen ein hybrides Verfahren vor [@weber2022automated]. Eine Bindung an Bauordnung oder Fertigung stellt die Übersicht nicht her. Liggett zeichnet die frühe Linie der automatisierten Raumzuordnung nach [@liggett2000automated]. Die folgende Darstellung ordnet die Verfahren nach der Frage, die für die Arbeit entscheidend ist: Garantiert das Verfahren die Einhaltung harter Regeln, und ist es reproduzierbar?

### 5.5.2 Formgrammatiken

Formgrammatiken beschreiben einen Entwurfsraum durch Ersetzungsregeln. Die klassische Analyse der Prairie Houses von Frank Lloyd Wright zeigte, dass sich ein Stil generativ beschreiben lässt [@koning1981language]. Duarte entwickelte diese Linie ausdrücklich zur Mass Customization von Wohnungen [@duarte2001customizing; @duarte2005discursive; @duarte2005towards]. Seine „Discursive Grammar“ der Malagueira-Häuser von Álvaro Siza hat drei Teile:

1. Eine **Programming Grammar** erzeugt aus Nutzerangaben ein Raumprogramm.
2. Eine **Designing Grammar** enthält die Entwurfsregeln des Stils.
3. Eine **Description Grammar** enthält Regeln der portugiesischen Wohnungsbauvorschriften.

Heuristiken lenken die Suche. Duarte entschied sich laut Recherche 11 bewusst für eine deterministische Suche, weil stochastische Verfahren für Antwortzeiten im Web zu langsam seien. Validiert wurde die Grammatik durch einen Test, in dem Siza ein von der Grammatik erzeugtes Haus nicht als fremd erkannte. Benrós und Duarte koppelten ein solches Entwurfssystem konzeptionell mit einem Vorfertigungs-Bausystem [@benros2009integrated].

Für den Holzbau kodierten Kwieciński et al. Regeln des leichten Holzrahmenbaus in einer Formgrammatik [@kwiecinski2016wood]. Laut Recherche 11 sind das ein Achsraster von 60 cm, Räume als Vielfache von 60 × 60 cm und eine maximale Deckenspannweite von 6 m. Sie verglichen die Grammatik mit einem genetischen Algorithmus. Bei vielen Räumen wird die Grammatik kombinatorisch teuer. Sass zeigte, dass Grammatikregeln direkt CNC-Daten für Holzbauteile erzeugen können [@sass2006wood]. Knight und Sass fordern „visuell-physische“ Grammatiken, die vollständige Fertigungsdaten liefern [@knight2010looks].

**Kritische Würdigung.** Die Grammatiklinie ist der konzeptionell nächste Vorläufer eines regelbasierten, nutzergesteuerten Hausentwurfs. Duartes Dreiteilung entspricht fast genau der Architektur der Arbeit: Sprachschnittstelle zum Raumprogramm, Herstellerregelraum, Prüfung nach Bauordnung. Ihre Grenzen sind ebenso deutlich. Die Grammatik bildet einen Stil und einen Standort ab, eine Konstruktions- und Fertigungsebene fehlt. Laut Recherche 11 kostete das Extrahieren der nie niedergeschriebenen Regeln Jahre. Das gilt auch für den Regelraum eines Herstellers: Der Wissenserwerb ist der Engpass, nicht die Suche.

### 5.5.3 Optimierung und Constraint-Programmierung

Die optimierungsbasierte Linie formuliert Grundrisse als Zuordnungs- oder Optimierungsproblem:

- Michalek et al. kombinieren gradientenbasierte und evolutionäre Suche mit menschlichen Entscheidungen [@michalek2002architectural].
- Lottaz et al. bestimmen mit IDIOM vollständige Lösungsräume aus Constraints über kontinuierlichen Variablen und aktivieren bevorzugte Constraints interaktiv, erprobt am Wohnungsgrundriss [@lottaz1998constraint].
- Merrell et al. verbinden ein aus realen Grundrissen gelerntes Bayes'sches Netz für das Raumprogramm mit stochastischer Optimierung der Geometrie [@merrell2010computer].
- Laignel et al. rastern den Umriss nach architektonischen Constraints, weisen Zellen per Constraint-Programmierung zu und verfeinern per genetischem Algorithmus. Gültige Wohnungsgrundrisse entstehen meist in etwa einer Minute [@laignel2021floor].
- Upasani et al. erzeugen bemaßte Rechteckgrundrisse aus einer dimensionslosen Anordnung mit einem linearen Optimierungsmodell, das Mindestbreiten und Seitenverhältnisse einhält [@upasani2020dimensioned].
- Erculiani et al. lernen Präferenzen des Entwerfers im Dialog, während ein Constraint-Solver die Grundrisse erzeugt [@erculiani2019layout].

**Kritische Würdigung.** Diese Verfahren garantieren harte Constraints, soweit sie formuliert sind. Das ist ihr entscheidender Vorteil gegenüber lernenden Verfahren. Ihre Constraints sind aber architektonisch-funktional, nicht bauordnungsrechtlich oder konstruktiv. Kein gefundenes Verfahren kennt Abstandsflächen, Vollgeschossregeln, ein Holzrahmenraster mit Tragwänden und Elementstößen oder die Transportmaße vorgefertigter Elemente. Die Kombination mit stochastischer Suche (Merrell, Laignel) kostet zudem Reproduzierbarkeit.

### 5.5.4 Lernende Verfahren

Große Grundrissdatensätze haben eine lernende Linie ermöglicht:

- RPLAN, ein Datensatz realer Wohnungsgrundrisse, mit Raumaufteilung innerhalb einer vorgegebenen Hülle [@wu2019data]
- House-GAN erzeugt Layouts aus Blasendiagrammen [@nauata2020housegan], House-GAN++ verfeinert sie iterativ [@nauata2021housegan]
- HouseDiffusion überträgt Diffusionsmodelle auf Vektorgrundrisse [@shabani2023housediffusion]
- Tell2Design liefert über 80.000 Grundrisse mit Sprachanweisungen und zeigt, dass Text-zu-Bild-Modelle räumliche und relationale Vorgaben schlecht einhalten [@leng2023tell2design]
- StructGAN lernt Wandscheiben-Layouts aus Plänen und misst die Überdeckung mit Lösungen erfahrener Ingenieure [@liao2021structgan]
- ein GNN-Co-Pilot schlägt aus IFC-Graphen passende Bauteile vor [@renner2025copilot]
- ein Multiagenten-LLM erzeugt aus freien Anforderungen Blasendiagramme, die ein Diffusionsmodell in Grundrisse übersetzt, und schneidet auf Tell2Design besser ab als eine reine LLM-Baseline [@zhang2026multiagent]

Eine Übersicht über 71 Verfahren der prozeduralen Gebäudegenerierung nennt als typische Grenzen rechteckige Räume, manuelle Zwischenschritte und ungültige Ergebnisse [@kutzias2024recent].

**Kritische Würdigung.** Lernende Verfahren erzeugen plausibel aussehende Layouts. Sie garantieren aber weder Maßhaltigkeit noch Normkonformität noch einen Bezug zu einem Bausystem. Die Trainingsdaten stammen überwiegend aus ostasiatischem Geschosswohnungsbau. Hinzu kommt ein praktisches Hindernis: Laut Recherche 03 sind House-GAN++, HouseDiffusion und Graph2Plan nicht kommerziell oder ohne Lizenz veröffentlicht, RPLAN ist vermutlich nur nicht kommerziell nutzbar [U]. Für die Arbeit sind sie deshalb nur als Vergleichsbaseline geeignet, nicht als Methode.

### 5.5.5 Möblierung

Für die Möblierung zeigen zwei Arbeiten von 2011, wie sich Ergonomie- und Gestaltungsregeln als Kostenfunktionen fassen lassen. Yu et al. optimieren Möbelanordnungen per Simulated Annealing und prüfen die wahrgenommene Funktionalität in einer Wahrnehmungsstudie [@yu2011make]. Merrell et al. übersetzen Einrichtungsleitlinien in eine Dichtefunktion. Ihr interaktives Vorschlagssystem verbesserte messbar die Anordnungen von Teilnehmenden ohne Vorbildung [@merrell2011interactive].

Die für die Arbeit wichtigste Möblierungsarbeit ist die von Sydora und Stroulia [@sydora2020rulebased]. Sie entwickelten eine domänenspezifische Sprache für Innenraumregeln, die zweierlei leistet. Sie prüft ein BIM-Modell gegen die Regeln, und sie erzeugt mehrere gültige Alternativen, die denselben Regeln genügen. Evaluiert wurde das an Küchen mit realen Regeln eines Industriepartners und an Wohnzimmern mit Regeln aus der Literatur. Das ist der sauberste veröffentlichte Beleg für das Prinzip „eine Regelbasis, zwei Verwendungen“. Die Grenzen: nur Innenraum, ein einfacher Greedy-Algorithmus, keine Bauordnungs-, Tragwerks- oder TGA-Regeln und keine Nutzerstudie (Recherche 12).

Aus der Critiquing-Forschung stammen Systeme, die Laien nicht ersetzen, sondern kommentieren. JANUS verband in der Küchenplanung eine konstruktive Entwurfsumgebung mit regelbasierten Kritikern [@fischer1989environments; @fischer1991critiquing]. Der Furniture Design Critic wählt Art und Form der Kritik nach Wissensstand und Interaktionsgeschichte des Nutzers [@oh2010furniture]. Weiche Constraints bilden Präferenzen ab, die verletzt werden dürfen [@meseguer2006soft]. Bogaerts et al. erzeugen schrittweise, für Menschen leicht prüfbare Erklärungen, wie ein Constraint-Problem gelöst wurde [@bogaerts2021step]. Diese Linien sind der Unterbau für die Empfehlungsklasse R5 in Kapitel 9b.

### 5.5.6 Weitere generative Teilprobleme: Dach und Leitungsführung

Zwei Teilprobleme des Zielbilds sind eigenständig erforscht, enden aber vor der Konstruktion:

- **Dach.** Das Straight Skeleton liefert das „kanonische“ Walmdach über einem Grundriss [@aichholzer1995novel]. Kelly und Wonka verallgemeinern es mit gewichteten Kanten zu Giebeln, Gauben und Überständen und weisen auf Mehrdeutigkeiten im konkaven Fall hin [@kelly2011interactive]. Held und Palfrader erzeugen Dächer mit unterschiedlichen Neigungen und Traufhöhen [@held2017roofs], Eder et al. robuste Implementierungen mit exakter Arithmetik [@eder2021exact]. Alle Verfahren liefern Dachflächen, keine Sparren, Grat- und Kehlsparren oder Schifter (Recherche 12).
- **TGA-Routing.** Medjdoub und Bi führen Kanäle constraintbasiert und parametrisch editierbar [@medjdoub2018parametric]. Singh und Cheng vergleichen Graphverfahren für mehrere Leitungen [@singh2021automating]. Blokland et al. ordnen das Feld in einer Taxonomie [@blokland2023literature]. Für den Tafelbau fanden sich nur zwei Arbeiten. Baradaran-Noveiri et al. optimieren Luftkanäle mit einem genetischen Algorithmus und berücksichtigen Kreuzungen mit dem Tragwerk [@baradaran2022parametric]. Zhang et al. entwerfen die Entwässerung von Wohngebäuden im Tafelbau automatisch; diese Arbeit ist nur nach Titel und Screening eingeordnet [@zhang2022bimbased]. Bohrregeln für Holzbauteile und die Übergabe von Durchbrüchen als Fertigungsbearbeitung fehlen.

### 5.5.7 Zwischenfazit 5.5

| Verfahrensfamilie | harte Regeln garantiert? | reproduzierbar? | Bausystembezug | Beispiele | Eignung für die Arbeit |
|---|---|---|---|---|---|
| Formgrammatik | ja, soweit kodiert | ja (bei deterministischer Suche) | schwach; Raster bei [@kwiecinski2016wood] | [@duarte2001customizing; @kwiecinski2016wood] | Architekturvorbild; Wissenserwerb als Engpass |
| Constraint-Programmierung, lineare Optimierung | ja | ja | nicht vorhanden | [@lottaz1998constraint; @upasani2020dimensioned] | Kernverfahren für Grundriss mit Raster |
| hybride Optimierung (CP plus GA, Bayes plus Stochastik) | teilweise | nein | nicht vorhanden | [@laignel2021floor; @merrell2010computer] | nur CP-Anteil übernehmbar |
| lernende Generatoren | nein | nein | nicht vorhanden | [@nauata2021housegan; @shabani2023housediffusion; @zhang2026multiagent] | Baseline; Lizenzen oft nicht kommerziell |
| DSL für Prüfen und Erzeugen | ja | ja | Innenraum | [@sydora2020rulebased] | Prinzip „eine Regelbasis, zwei Verwendungen“ |
| Critiquing, weiche Constraints | nicht Ziel | ja | nicht vorhanden | [@fischer1991critiquing; @meseguer2006soft] | Empfehlungen mit Begründung |

## 5.6 Sprach- und Sprachmodellschnittstellen in AEC

### 5.6.1 Sprachverstehen: Intent, Slots und Spracherkennung

Unterhalb der LLM-Welle liegt eine etablierte Forschungstradition des Spoken Language Understanding (SLU). Tur und De Mori fassen sie zusammen: Eine Äußerung wird in Domäne, Absicht (Intent) und eine Menge von Attribut-Wert-Paaren (Slots) überführt [@tur2011spoken]. Der ATIS-Korpus prägte die Aufgabe als Benchmark [@hemphill1990atis]. Neuronale Verfahren lösten Slot Filling mit rekurrenten Netzen [@mesnil2015rnn] und später als gemeinsame Intent- und Slot-Modellierung mit vortrainierten Transformern [@chen2019bert]. Weld et al. geben eine Übersicht über gemeinsame Modelle [@weld2022survey].

Für die Arbeit ist diese Tradition methodisch wertvoll. Sie liefert ein formales Zielschema und etablierte Metriken, etwa Intent-Accuracy und Slot-F1. Damit lässt sich die sprachliche Komponente unabhängig von der Geometrieerzeugung evaluieren.

Die Spracherkennung hat mit großen, schwach überwachten Modellen wie Whisper eine hohe Robustheit erreicht [@radford2023whisper]. Für Fachvokabular ist Contextual Biasing das Standardverfahren, bei dem eine Liste kontextueller Phrasen zur Laufzeit begünstigt wird [@pundak2018deep]. Deutsche Sprachdatensätze aus dem Bauwesen wurden nicht gefunden (Recherche 03). Eine Evaluation für Begriffe wie „Kniestock“, „Pfette“ oder „Abstandsfläche“ fehlt.

**Stand der Technik (Recherche 03).** Typisierte Entscheidungsmodelle, die statt Text Wahrscheinlichkeiten für vorgegebene Antwortoptionen liefern, sind erst seit Mitte September 2026 öffentlich. Laut Model Card liegt das offene Modell Laya ohne Fine-Tuning mit einer Genauigkeit von 0,342 nahe am Zufallsniveau von 0,318 und wird unkalibriert ausgeliefert. Mit mehr als etwa 20 Auswahloptionen sinkt die Leistung deutlich [V]. Wissenschaftliche Evaluationen dieser Modelle gibt es noch nicht.

### 5.6.2 Frühe Sprachschnittstellen zu CAD und BIM

Sprachsteuerung im Entwurf ist älter als die Sprachmodelle:

- Kou und Tan steuerten CAD per Sprache. Laut Recherche 12 erkannte eine CAD-spezifische Grammatik deutlich besser als freies Diktat [@kou2008design]. Eine Folgearbeit filtert Kandidaten nach dem aktuellen Modellkontext und fragt bei Mehrdeutigkeit nach [@kou2010knowledge].
- BIMASR verbindet Spracherkennung, NLP und eine relationale Datenbank zur Abfrage und Änderung in Revit. Es verzichtet bewusst auf IFC, weil der Umweg über IFC die direkte Datenänderung verhindere [@shin2021bimasr].
- Elghaish et al. bauten mit Amazon Alexa einen Sprachassistenten für BIM-Daten, auch für Nutzer mit Behinderung [@elghaish2022voice].
- Niemeijer ließ Architekten Constraints in natürlicher Sprache formulieren, die ein Parser in prüfbare Regeln übersetzt [@niemeijer2011constraint; @niemeijer2014freedom]. Eine zuvor erprobte eigene Regelsprache war im Nutzertest laut Recherche 12 „zu mühsam“.

### 5.6.3 Sprachmodelle für die Informationsabfrage

Die Informationsabfrage ist mit 29,5 % das häufigste Anwendungsfeld der BIM-LLM-Forschung [@park2026bimllm]:

- BIMS-GPT klassifiziert natürlichsprachliche Abfragen mit 99,5 % Genauigkeit, wenn 2 % der Daten im Prompt stehen, erprobt an einem Krankenhausmodell [@zheng2023dynamic].
- Yin et al. übersetzen Text zweistufig in die Abfragesprache BIMQL [@yin2023twostage]. Guo et al. ordnen Anfragen Funktionen der Revit-API zu und erreichen an 80 Anfragen 78,75 % Genauigkeit [@guo2025advancing].
- Hellin et al. lassen LLM-Agenten IFC-Modelle ohne Ontologie abfragen, mit 80 % Genauigkeit, und veröffentlichen den Datensatz IFC-Bench [@hellin2025natural]. Die zweite Fassung umfasst 1.027 Aufgaben an 37 IFC-Modellen aus 21 Projekten. Ein Agent, der die Modellstruktur zur Laufzeit erkundet, übertrifft dort statische Abfragen [@hellin2026bim].

**Befund.** Abfragen lesen nur; ein Fehler verändert das Modell nicht. Für die Arbeit liefert die Linie vor allem ein Evaluationsvorbild: IFC-Bench ist der einzige offene Datensatz mit Referenz-IFCs, allerdings englischsprachig und nicht aus dem Holzbau (Recherche 12).

### 5.6.4 Sprachmodelle für die Erzeugung und Änderung von Modellen

Die für die Arbeit maßgebliche Frage ist, wer die Modelländerung ausführt. Die folgende Tabelle ordnet die gesichteten Systeme danach.

| System | Eingabe | Rolle des LLM | Ausführung | Prüfung | Nutzer | Stufe |
|---|---|---|---|---|---|---|
| NADIA [@jang2024interactivedesign; @jang2024nadia] | Text | spezifiziert Wandschichten, erzeugt geänderte XML-Daten | Revit über BIM2XML/XML2BIM | Einhaltung von Wärmeschutzanforderungen gemessen | Architekten | E2 |
| NADIA-S [@lee2024generalized] | Sprache | sechs Schritte: interpret, fill, match, structure, execute, check | Revit | Schritt „check“ | Architekten | E1, Preprint |
| Text2BIM [@du2026text2bim] | Text | Multi-Agenten erzeugen imperativen Code für die Vectorworks-API | Autorenwerkzeug | regelbasierter Modellprüfer in einer Rückkopplungsschleife | Entwerfende | E2 (drei LLMs) |
| Chen et al. [@chen2025agent] | Sprache oder Text | erkennt Änderungsabsicht, bildet sie auf Parameter ab | prozedurale Grasshopper-Module | keine Regelprüfung | Architekt und Bauherr | E2 (−78 % Modellierzeit) |
| Kakadoo [@atakan2025kakadoo] | Sprache | nur für unstrukturierte Befehle, Ausgabe als JSON-Reglerwerte | Grasshopper | keine | Fachleute im Workshop | E3 qualitativ |
| DAVE [@fernandes2024gptassistant] | Sprache oder Text | steuert Python-Skripte über die Revit-API | Revit | Fehleranalyse | Fachleute | E2 |
| MCP4IFC [@nithyanantham2025mcp4ifc] | Text | ruft vordefinierte Werkzeuge auf oder generiert Code per RAG | IfcOpenShell (IFC nativ) | keine | offen | E1, Preprint |
| T2S4BIM [@wei2025texttostructure] | Text | zerlegt Anfragen in Intent und Slots (nach Screening) | Revit | ? | ? | ? |
| Wu et al. [@wu2026alterations] | menschliche Strategie | formalisiert Strategien zu Bauteiloperationen | regelgebunden | Codeprüfung nach IBC | Planer | E1 |
| Kodnongbua et al. [@kodnongbua2024zeroshot] | Text | erzeugt Constraints und Zielfunktionen | symbolische Solver | Rückkopplung je Entwurfsstufe | Projektentwicklung | E2, Preprint |

Hinzu kommt ein Multiagentensystem, das Nicht-Experten BIM-Operationen im Entwurf ermöglichen soll. Es ist nur nach Titel und Screening-Notiz eingeordnet [@dong2025bim].

**Kritische Würdigung.** Vier Befunde ziehen sich durch die Tabelle:

1. **Das LLM erzeugt meist Code oder Daten.** Bei Text2BIM, DAVE, NADIA und MCP4IFC schreibt das Sprachmodell den Code oder die geänderten Daten selbst. Reproduzierbarkeit und Haftungszuordnung sind damit schwach, denn dieselbe Anweisung kann zu verschiedenen Modellen führen. Nur Kakadoo und Chen et al. beschränken das Modell auf die Abbildung auf Parameter. Kakadoo parst strukturierte Befehle sogar deterministisch und ruft das LLM nur für unscharfe Angaben wie „höher“ auf [@atakan2025kakadoo].
2. **Implizite Annahmen werden nicht offengelegt.** Chen et al. lassen fehlende Angaben vom Sprachmodell ergänzen, nach der Auswertung in `literatur/lit-B-vorfertigung-ki.md` nach „gesundem Menschenverstand“ [@chen2025agent]. Laut Einzelbewertung bevorzugen Nutzer dort bei Änderungen eines einzelnen Parameters den Schieberegler. Sprache lohnt sich also vor allem für zusammengesetzte Änderungen.
3. **Kein System kennt ein Bausystem, eine Bauordnung oder eine Fertigung.** Die erzeugten Modelle bleiben auf der Ebene eines frühen Entwurfs oder eines einzelnen Bauteils.
4. **Die Nutzer sind Fachleute.** Keine Arbeit evaluiert mit Bauherren. Das Review von Park et al. findet über 61 Studien eine technische Validierung in 70,5 %, eine industrielle nur in 44,3 % der Fälle [@park2026bimllm].

Die Stufenfolge von NADIA-S (interpret, fill, match, structure, execute, check) entspricht strukturell einer klassischen SLU-Pipeline mit Intent-Erkennung, Slot-Füllung, Abgleich mit Katalogobjekten, Ausführung und Prüfung [@lee2024generalized]. Sie ist der direkteste Vergleichsrahmen für die Sprachschnittstelle der Arbeit (Kapitel 10).

### 5.6.5 Konfiguration aus natürlicher Sprache

Außerhalb des Bauwesens ist eine Linie entstanden, die Produktkonfiguratoren direkt aus freiem Text bedient. Wang et al. bilden Kundenbeschreibungen über Text-Embeddings und ein mehrschichtiges Perzeptron auf Attributoptionen ab [@wang2022natural]. Weitere Arbeiten überbrücken die „semantische Lücke“ zwischen Kundenbedarf und Spezifikation mit Attention-Netzen, Domänenwissen oder Soft Prompts [@wang2021needsbased; @wang2021knowledge; @huang2024semanticgap]. Dudek wählt per Spracherkennung und Schlüsselbegriffen Varianten vorgefertigter Containerhäuser aus [@dudek2023mass].

**Befund.** Diese Linie verbindet die Befunde von Randall et al. zur Bedarfsorientierung (Abschnitt 5.4.5) mit Sprachtechnik. Sie arbeitet aber mit Konsumgütern und flachen Attributlisten, ohne Constraints und ohne Rückfrage bei Mehrdeutigkeit. Der Hausentwurf ist dagegen eine Konfiguration mit Geometrie, Abhängigkeiten und harten Rechtsgrenzen.

### 5.6.6 Risiken und neuro-symbolische Muster

Die Grenzen der Sprachmodelle sind gut dokumentiert. Halluzinationen, also flüssige, aber faktisch falsche Ausgaben, sind systematisch beschrieben [@ji2023hallucination]. Sprachmodelle bilden Text zuverlässig auf räumliche Relationen ab, scheitern aber an mehrstufigem räumlichem Schließen [@li2024spatial]. Übersichten zu GPT-Modellen und Konversations-KI im Bauwesen verorten das Feld zwischen hohen Erwartungen und deutlichen Grenzen [@saka2024gpt; @saka2023conversational].

Dem steht ein in der allgemeinen KI-Forschung gut belegtes Muster gegenüber: Das Sprachmodell zerlegt das Problem, und ein Interpreter oder Werkzeug rechnet [@gao2023pal; @schick2023toolformer; @yao2023react]. Garcez und Lamb beschreiben die Verbindung als neuro-symbolische KI: Lernverfahren übernehmen Wahrnehmung, symbolische Verfahren übernehmen Schlussfolgern, Garantien und Erklärbarkeit [@garcez2023neurosymbolic].

In der AEC-Literatur tritt das Muster unabhängig mehrfach auf:

- Text2BIM mit dem regelbasierten Prüfer [@du2026text2bim]
- Kodnongbua et al. mit Solvern, die Constraints des LLM lösen [@kodnongbua2024zeroshot]. Laut Recherche 12 half die Rückgabe des minimal widersprüchlichen Teilsystems an das LLM in 10 von 13 unlösbaren Fällen, und die Selbstprüfung von GPT-4 machte Rechenfehler.
- Mirhosseini et al. mit IfcOpenShell als deterministischem Kern [@mirhosseini2026ambiguity]
- Saluz et al. mit einem OWL-Reasoner [@saluz2025semio]

**Kritische Würdigung.** Die Aufgabenteilung ist in der Literatur angelegt, aber nicht zu Ende gedacht. In allen genannten Systemen darf das Sprachmodell noch Constraints, Code oder Daten erzeugen, die dann geprüft werden. Eine strengere Teilung, in der das Modell nur eine Absicht und typisierte Parameter aus einem geschlossenen Katalog wählt und Werte, Regeln und Geometrie ausschließlich im Code entstehen, ist nicht dokumentiert. Genau diese Teilung verlangt das Zielbild: „Die KI versteht, der Code entscheidet.“ Rechtlich stützt sie die Unterscheidung zwischen automatisierten Systemen mit festen, nachvollziehbaren Regeln und autonomen Systemen, bei denen Zurechnungslücken entstehen [@wilhelmi2020haftung] (Recherche 23).

## 5.7 Vergleichbare Arbeiten

### 5.7.1 Auswahl und Kriterien

Die Matrix führt die Arbeiten zusammen, die dem Zielbild in mindestens zwei Merkmalen nahekommen. Grundlage sind die Recherchen 11 und 12, ergänzt um die Schneeballrunden (Recherchen 24 bis 28) und die regionale Lückenrecherche (Recherche 21). Die sechs Merkmale entsprechen den Gliedern der Kette aus dem Zielbild.

**Legende.** ● ja · ◐ teilweise · ○ nein · ? am vorliegenden Material nicht prüfbar

| Spalte | ● | ◐ |
|---|---|---|
| Laie entwirft? | der Endkunde bedient das System selbst | Kunde nur mittelbar (mit Verkäufer, im Co-Design oder als geplante Zielgruppe) |
| Regeln bei Erzeugung? | Regeln begrenzen die Erzeugung selbst | Prüfung mit Rückkopplung oder nur Teilregeln |
| offener Standard/IFC? | IFC oder anderer offener Standard durchgängig | BIM in proprietärem Autorensystem oder IFC nur als Export |
| bis Fertigung? | Werkstattpläne oder Maschinendaten | Fertigungsregeln oder Fertigbarkeit ohne Fertigungsdaten |
| Bauantrag? | Genehmigungsunterlagen werden abgeleitet | bauordnungsrechtliche Regeln werden geprüft |
| Sprache? | natürliche Sprache (Text oder gesprochen) steuert | kontrollierte Sprache oder Textabgleich |

### 5.7.2 Vergleichsmatrix

| Nr. | Arbeit | Jahr | Laie entwirft? | Regeln bei Erzeugung? | offener Standard/IFC? | bis Fertigung? | Bauantrag? | Sprache? | Evaluation (Stufe) |
|---|---|---|---|---|---|---|---|---|---|
| 1 | Duarte, Discursive Grammar [@duarte2001customizing; @duarte2005discursive] | 2001/05 | ◐ | ● | ○ | ○ | ◐ | ○ | Experten-Blindtest mit dem Architekten (E1) |
| 2 | Benrós & Duarte [@benros2009integrated] | 2009 | ◐ | ● | ○ | ◐ | ○ | ○ | konzeptionelle Kopplung, Fallbeispiel (E0–E1) |
| 3 | Kwieciński et al., Holzrahmen-Grammatik [@kwiecinski2016wood] | 2016 | ◐ | ● | ○ | ○ | ○ | ○ | Laufzeitvergleich Grammatik gegen GA (E2) |
| 4 | Kwieciński & Duarte, HOPLA [@kwiecinski2018hopla; @kwiecinski2019customers] | 2019 | ● | ● | ○ | ○ | ○ | ○ | Nutzertests mit Laien auf zwei Kontinenten, kleine Stichproben (E3) |
| 5 | Kwieciński & Słyk [@kwiecinski2023interactive] | 2023 | ● | ● | ○ | ○ | ○ | ○ | Usability-Studien (E3) |
| 6 | Niemeijer et al., Check-mate [@niemeijer2009checkmate] | 2009 | ◐ | ○ | ● | ○ | ◐ | ◐ | Prototyp an einer Testwohnung (E1) |
| 7 | Niemeijer, Constraint Specification [@niemeijer2011constraint; @niemeijer2014freedom] | 2011/14 | ◐ | ○ | ● | ○ | ◐ | ● | Parse-Erfolg an Constraints von Architekturstudierenden (E2) |
| 8 | Khalili-Araghi & Kolarevic [@khalili2016development; @khaliliaraghi2020variability] | 2016/20 | ● | ● | ◐ | ○ | ◐ | ○ | konzeptioneller Rahmen, Folgearbeit zu Variabilität (E0–E1) |
| 9 | Sandberg et al., Treppenwerkzeug [@sandberg2008knowledge] | 2008 | ◐ | ● | ○ | ◐ | ○ | ○ | Demonstrator beim Hersteller (E1) |
| 10 | Popovic et al., Design Platform und IDM [@popovic2021configuration] | 2021 | ○ | ● | ◐ | ◐ | ○ | ○ | Fallstudie Einfamilienhaus (E1) |
| 11 | Puusepp et al. [@puusepp2017enabling] | 2017 | ● | ◐ | ◐ | ○ | ○ | ○ | Live-Betrieb, Web-Analytics mit n = 133 (E4, deskriptiv) |
| 12 | Swanenburg [@swanenburg2016towards] | 2016 | ● | ○ | ○ | ○ | ○ | ○ | randomisiertes Online-Experiment mit Kontrollgruppe (E3, MSc) |
| 13 | Alwisy et al., MCMPro [@alwisy2019bim] | 2019 | ○ | ● | ◐ | ● | ○ | ○ | Fallanwendung, Vorteile erwartet (E1) |
| 14 | Abushwereb et al., FrameX [@abushwereb2019knowledge] | 2019 | ○ | ● | ◐ | ● | ◐ | ○ | Zeitvergleich an einer Referenzwand, −80 % (E2) |
| 15 | Narayanaswamy et al. [@narayanaswamy2019bim] | 2019 | ○ | ○ | ◐ | ○ | ◐ | ○ | Prototyp, Vergleich mit manueller Prüfung (E1) |
| 16 | An et al. [@an2020bimbased] | 2020 | ○ | ◐ | ◐ | ◐ | ○ | ○ | ? (nur Titel und Screening) |
| 17 | Darwish et al. [@darwish2022automated] | 2022 | ○ | ◐ | ◐ | ● | ○ | ○ | Werkzeug für eine Wandfertigungsanlage (E1) |
| 18 | Cao et al., Fertigbarkeitsontologie [@cao2022ontologybased] | 2022 | ○ | ● | ? | ◐ | ○ | ○ | Holztafelbau-Projekt (E1, nur Kurzfassung) |
| 19 | Sydora & Stroulia [@sydora2020rulebased] | 2020 | ○ | ● | ◐ | ○ | ○ | ○ | Küchen mit Regeln eines Industriepartners, Wohnzimmer (E1–E2) |
| 20 | Cao et al., Kit-of-Parts-Konfigurator [@cao2021cross] | 2021 | ? | ● | ? | ◐ | ○ | ○ | Prototyp, Implementierung (E1) |
| 21 | Bakhshi et al. [@bakhshi2021dfma] | 2022 | ● | ● | ◐ | ◐ | ○ | ○ | Proof of Concept in Revit/Dynamo (E1) |
| 22 | Wang & Chen [@wang2024cloud] | 2024 | ◐ | ◐ | ● | ○ | ◐ | ◐ | Fallstudie British Columbia (E1) |
| 23 | Shafiee et al. [@shafiee2025enhancing] | 2025 | ● | ● | ○ | ● | ◐ | ○ | DSR-Fallstudie, Firmenbefragung (E1) |
| 24 | Eisfeld & Mons, Variowohnen [@eisfeld2022variowohnen] | 2022 | ○ | ● | ◐ | ◐ | ○ | ○ | Forschungsbericht, nur Kurzfassung bekannt (E1) |
| 25 | BIMwood [@tum2023bimwood; @geier2022bimwood] | 2022/23 | ○ | ○ | ◐ | ◐ | ○ | ○ | Referenzprozess, Fallstudie (E1) |
| 26 | Haas-Konfigurator [@np2025haas] | 2025 | ● | ◐ | ○ | ● | ○ | ○ | keine; Pressemitteilung |
| 27 | DesignChain [@fraunhoferipa0000designchain] | 2023 | ◐ | ● | ○ | ● | ○ | ○ | Referenzbericht (E1) |
| 28 | Digital Craft [@krueger2026steckhaus] | 2026 | ● | ◐ | ? | ● | ○ | ○ | Prototyp, laufend |
| 29 | Text2BIM [@du2026text2bim] | 2026 | ○ | ◐ | ◐ | ○ | ○ | ● | Vergleich dreier LLMs an Testfällen (E2) |
| 30 | NADIA, NADIA-S [@jang2024nadia; @lee2024generalized] | 2024 | ○ | ◐ | ◐ | ○ | ○ | ● | 240 und 1.920 Wanddetails (E2) |
| 31 | Chen et al. [@chen2025agent] | 2025 | ◐ | ○ | ○ | ○ | ○ | ● | Fallstudie, −78 % Modellierzeit (E2) |
| 32 | Wei et al., T2S4BIM [@wei2025texttostructure] | 2025 | ? | ? | ◐ | ○ | ○ | ● | ? (nur Titel und Screening) |
| 33 | Kodnongbua et al. [@kodnongbua2024zeroshot] | 2024 | ○ | ● | ○ | ○ | ○ | ● | Vergleich mit realen Gebäuden (E2, Preprint) |
| 34 | MCP4IFC [@nithyanantham2025mcp4ifc] | 2025 | ? | ○ | ● | ○ | ○ | ● | Demonstrationsaufgaben (E1, Preprint) |
| 35 | Erhan et al., D-CodeWeaver [@erhan2026dcodeweaver] | 2026 | ○ | ● | ○ | ○ | ◐ | ○ | mit Industriepartnern entwickelt (E1) |
| 36 | Pang et al. [@pang2026natural] | 2026 | ? | ● | ? | ? | ◐ | ● | Compliance-Rate, Intent-Treue, Zeit gegen manuelle Abläufe laut Abstract (E2?, Preprint, Volltext offen) |
| – | **diese Arbeit (Ziel)** | – | ● | ● | ● | ● | ● | ● | technisch E2, Laienstudie E3 geplant (Kapitel 20) |

### 5.7.3 Kritische Würdigung nach Gruppen

**Grammatiken und Laienentwurf (Nr. 1 bis 8, 11 und 12).** Diese Gruppe hat das Szenario am klarsten formuliert: Ein Laie ändert oder erzeugt einen Hausentwurf, und formalisierte Regeln sichern die Gültigkeit. Niemeijer beschreibt fast wörtlich den Fall dieser Arbeit, Käufer ändern ein Serienhaus innerhalb der Regeln von Architekt und Bauordnung (Recherche 12). Die Stärken liegen in der Architektur (Duartes Dreiteilung, Khalili-Araghis Trennung von Constraint Solving und Constraint Checking) und in übertragbaren Evaluationsdesigns (HOPLA, Recherche 11). Die Grenzen sind durchgängig: keine Konstruktions- und Fertigungsebene, kein offenes Datenmodell außer bei Niemeijer, keine Sprache außer bei Niemeijer, der aber nur prüft und Generierung ausdrücklich ausschließt. Die Stichproben der Nutzerstudien sind klein.

**Plattform und Konfiguration beim Hersteller (Nr. 9, 10, 20 bis 25).** Diese Gruppe liefert die Datenmodelle, mit denen ein Hersteller seinen Lösungsraum beschreibt. Shafiee et al. kommen der Kette am nächsten: Ein Laie konfiguriert im Web, und das System erzeugt Anschlussdetails und Produktionsdokumente [@shafiee2025enhancing]. Das Objekt ist aber ein Nebengebäude, das System ist proprietär, und die Wirkung beruht auf einer Firmenbefragung, nicht auf Messung (Recherche 11). Wang und Chen sichern die Konformität über vorgenehmigte Grundrisse statt über Regeln [@wang2024cloud]. Variowohnen ist der nächste deutsche Präzedenzfall, aber ein Planerwerkzeug [@eisfeld2022variowohnen].

**Framing und Fertigungsdaten (Nr. 13 bis 18).** Hier liegt der stärkste Beleg für formalisierte Holzbauregeln und abgeleitete Maschinendaten (Abschnitt 5.3.3). Kein Laie entwirft, und das Regelwerk ist kanadisch.

**Regeln in der Erzeugung (Nr. 19, 35, 36).** Drei Arbeiten lassen dieselben Regeln prüfen und erzeugen: für Innenräume [@sydora2020rulebased], für die Kubatur im modularen Holzbau [@erhan2026dcodeweaver] und, laut Abstract, für Grundrisse aus Vorschriften und Sprache [@pang2026natural]. Keine reicht bis zur Konstruktion.

**Industrielle Praxis (Nr. 26 bis 28).** Die Praxis zeigt, dass die Kette technisch machbar ist, aber nicht, wie sie gebaut ist. Keine der drei Lösungen ist wissenschaftlich evaluiert oder offen dokumentiert.

**Sprache und Sprachmodelle (Nr. 29 bis 34).** Diese Gruppe liefert die Sprachschnittstelle, aber ohne Bausystem, Bauordnung und Fertigung (Abschnitt 5.6.4). Nur Kodnongbua et al. lassen einen Solver die harten Constraints durchsetzen, und nur MCP4IFC arbeitet nativ auf IFC.

### 5.7.4 Einordnung von Pang et al. (2026): offen

Die Arbeit von Pang et al. ist nach Titel und Abstract der nächste direkte Konkurrent [@pang2026natural]. Laut Abstract integriert das Rahmenwerk Entwurfswissen aus Vorschriften und aus natürlichsprachlichen Entwurfsabsichten. Es stellt das Wissen als ontologiegestützte Constraints dar, wendet sie bei der Erzeugung der Raumtopologie an und übersetzt die erzeugten Layouts in interoperable BIM-Instanzmodelle. Validiert wird über verschiedene BIM-Umgebungen. Gemessen werden Compliance-Rate, Übereinstimmung mit der Absicht und Zeit gegenüber manuellen Abläufen.

Damit deckt die Arbeit nach eigener Beschreibung zwei Glieder ab, die sonst fehlen: Regeln *bei* der Erzeugung und natürliche Sprache. **Offen** ist, was davon am Volltext trägt:

- welche Vorschriften formalisiert sind und ob Bauordnungsrecht dazugehört
- ob „interoperabel“ IFC bedeutet und in welcher Detaillierung
- ob ein Bausystem, eine Konstruktion oder Fertigungsdaten vorkommen
- welche Rolle das Sprachmodell hat: Erzeugt es Constraints, oder wählt es aus einem Katalog?
- wer die Nutzer der Evaluation sind

Die Arbeit ist ein SSRN-Preprint ohne Begutachtung. Der Volltext wurde für dieses Kapitel **nicht gelesen** (Recherche 12). Die Einordnung in der Matrix beruht allein auf dem Abstract und ist vor jeder Aussage „erstmals“ am Volltext zu prüfen.

### 5.7.5 Was sich übernehmen lässt und was zu vermeiden ist

| übernehmen | Quelle | vermeiden | Quelle |
|---|---|---|---|
| Dreiteilung Raumprogramm, Herstellerregeln, Bauordnung; deterministische Suche | [@duarte2001customizing] | Regelraum ohne Konstruktions- und Fertigungsebene | [@duarte2005towards] |
| Trennung Constraint Solving und Constraint Checking | [@khalili2016development] | Bindung an ein Autorenwerkzeug | [@khalili2016development; @alwisy2019bim] |
| eine Regelbasis für Prüfen und Erzeugen | [@sydora2020rulebased] | Greedy-Suche ohne Rückfrage bei Konflikt | [@sydora2020rulebased] |
| Austauschanforderungen je Übergabe mit Status G/M/T/R, übertragbar auf IDS | [@popovic2021configuration] | Verkauf außerhalb der Plattform ohne Wirkungsanalyse | [@lennartsson2022exploring] |
| Framing-, Beplankungs- und Panelisierungsregeln als Startpunkt | [@abushwereb2019knowledge; @liu2018bim; @liu2021panelization] | fremdes Regelwerk ungeprüft übernehmen | Recherche 12 |
| Zeitvergleich und Stücklistenvergleich gegen die Arbeitsvorbereitung | [@abushwereb2019knowledge; @wang2019automatic] | Wirkung nur per Befragung belegen | [@shafiee2025enhancing] |
| Laientest mit Modus „Vorschlag ändern“ gegen „von Null“ | [@kwiecinski2019customers] | Zufriedenheit messen, Baubarkeit nicht | [@kwiecinski2023interactive] |
| Kosten in der Antwort aktiv nennen | [@puusepp2017enabling] (Recherche 11) | Preisänderung nur anzeigen | [@puusepp2017enabling] |
| SLU-Pipeline interpret–fill–match–structure–execute–check | [@lee2024generalized] | LLM erzeugt Code oder Modelldaten | [@du2026text2bim; @nithyanantham2025mcp4ifc] |
| deterministischer Parser für strukturierte Befehle | [@atakan2025kakadoo] | stilles Ergänzen fehlender Angaben | [@chen2025agent] |
| Solver setzt harte Constraints durch, Widerspruch wird zurückgemeldet | [@kodnongbua2024zeroshot] | Rechnen und Prüfen dem LLM überlassen | [@kodnongbua2024zeroshot; @gao2023pal] |

### 5.7.6 Evaluationsqualität im Vergleich

Von den 36 Arbeiten der Matrix erreichen nur vier die Stufe E3 oder E4, also eine Studie mit Zielnutzern oder einen Betrieb mit Nutzungsdaten (Nr. 4, 5, 11 und 12). Keine davon misst zugleich die Baubarkeit des Ergebnisses, und keine arbeitet mit Sprache. Die einzige Sprachstudie mit Nutzern, der Workshop zu Kakadoo, ist qualitativ und mit Fachleuten besetzt [@atakan2025kakadoo]. Umgekehrt messen die technischen Evaluationen der Framing-Linie Zeit, Verschnitt und Genauigkeit, aber ohne Laien. Recherche 11 hält das als Kernbefund fest: Laienevaluation und Messung der Baubarkeit kommen in keiner Arbeit zusammen. Bei den LLM-Arbeiten fehlen Vergleichsbaselines und Wiederholungsmessungen fast durchgängig. Das bestätigt die Übersicht von Park et al. [@park2026bimllm].

## 5.8 Forschungslücken und Abgrenzung der eigenen Arbeit

### 5.8.1 Forschungslücken

Aus den Abschnitten 5.1 bis 5.7 ergeben sich die folgenden Lücken. Jede ist mit den Belegen genannt, die sie tragen, und der Forschungsfrage zugeordnet, die sie adressiert.

**L1 Keine durchgängige Kette vom Laienentwurf bis zu Bauantrag und Maschinendaten (FF1).** Keine der 36 Arbeiten der Vergleichsmatrix erfüllt mehr als drei der sechs Merkmale vollständig, und keine leitet Genehmigungsunterlagen ab. Die vollständigste Kette endet bei einem Nebengebäude ohne IFC und ohne Bauantrag [@shafiee2025enhancing]. Die Framing-Linie beginnt beim Planer [@alwisy2019bim; @abushwereb2019knowledge]. BIMwood arbeitet mit verknüpften Modellen und Dokumenten und adressiert nicht die Schnittstelle zum Bauherrn [@tum2023bimwood]. Recherche 06 fand keinen Hersteller, der ein IFC von Entwurf bis Fertigung führt [U].

**L2 Compliance by Construction mit echtem Bauordnungsrecht fehlt (FF2).** Regeln wirken *während* der Erzeugung bisher nur in Nischen: Innenraum [@sydora2020rulebased], kanadisches Framing [@abushwereb2019knowledge], Nagelbilder nach SIA 265 [@apolinarska2016mastering], Kubatur im modularen Holzbau [@erhan2026dcodeweaver]. Die Prüfforschung prüft überwiegend nachträglich [@sobhkhiz2021framing; @noardo2022unveiling]. Die Linie der Entwurfsanpassung repariert nach der Prüfung [@wu2025design; @wu2026alterations]. Ob Pang et al. diese Lücke für Bauvorschriften schließen, ist offen [@pang2026natural].

**L3 Keine formalisierte BayBO und keine deutschsprachige Regelbasis für Wohngebäude (FF2).** Formalisierungen liegen für die MBO [@mbo2bim2023], für NRW [@nrw2026bimbauantrag] und für Wien [@urban2026development; @recski2024briseplandok] vor. Für die BayBO ist keine Modellierungsrichtlinie mit Prüfregeln dokumentiert. Die NLP- und LLM-Evaluationen stützen sich auf englische, finnische, neuseeländische oder chinesische Regelwerke [@hettiarachchi2025codeaccord; @yang2024promptbased]. Autoritative maschinenlesbare Fassungen deutscher Bauvorschriften gibt es nicht [@idis2021szenarien].

**L4 Holzrahmenbau-Semantik in IFC 4.3 ist nicht beschrieben (FF1).** Es gibt weder eine MVD noch einen Implementierungsleitfaden für den Holzbau [@bsiMvd43] (Recherche 01). Die Schichtaggregation wurde in der Praxis verworfen [@timbim2024]. Forschungsprojekte weichen auf BHoM oder Grasshopper aus [@orozco2023codesign; @samarawickrama2026digital]. Laut BIMwood lassen sich Komponenten im IFC-Schema nicht parametrisieren [@geier2022bimwood].

**L5 Validierung eines generierten IFC ist methodisch nicht beschrieben (FF1).** Die Interoperabilitäts- und Prüfliteratur untersucht exportierte Modelle und deren schwankende Qualität [@lai2018interoperability; @noardo2022ifc]. Holzbau-Nachweise aus IFC brauchen ein vorgeschaltetes „Model Healing“ [@chateauvieux2023bim]. Round-Trip-Messungen liegen für IFC2x3 und Massivbau vor [@pazlar2008interoperability; @jeong2009benchmark], nicht für IFC 4.3 und Holzbauentitäten. Wie Schema-, Normative-Rules-, IDS- und Fachprüfung als fester Teil einer Generierungspipeline nachgewiesen werden, ist offen.

**L6 Eine strenge Aufgabenteilung zwischen Sprachmodell und Code ist nicht ausgearbeitet (FF3).** In den AEC-Systemen erzeugt das Sprachmodell Code, Daten oder Constraints [@du2026text2bim; @nithyanantham2025mcp4ifc; @kodnongbua2024zeroshot]. LLM-gestützte Prüfungen erreichen an kleinen Mengen hohe Werte ohne Goldstandard [@iversen2026leveraging; @lin2026defects]. Selbst deterministische Prüfsoftware führt Regeln nicht immer richtig aus [@pinto2026exhaustive]. Eine Architektur, in der das Modell nur Absicht und typisierte Parameter aus einem geschlossenen Katalog wählt, ist nicht dokumentiert. Die Haftungsliteratur spricht für eine solche Auslegung als automatisiertes statt autonomes System [@wilhelmi2020haftung].

**L7 Keine deutschsprachige Intent-Erkennung und kein Korpus für den Hausentwurf (FF3).** Die NL-BIM-Datensätze sind englisch [@hellin2026bim; @leng2023tell2design]. Deutsche Sprachdaten aus dem Bauwesen wurden nicht gefunden, und Contextual Biasing ist für deutsches Bauvokabular nicht evaluiert [@pundak2018deep] (Recherche 03). Die etablierten SLU-Metriken [@tur2011spoken; @weld2022survey] werden in der AEC-Literatur kaum genutzt.

**L8 Keine Evaluation, die Laien und Baubarkeit zugleich erfasst (FF5).** Laienstudien messen Zufriedenheit und Bedienbarkeit [@kwiecinski2019customers; @swanenburg2016towards; @puusepp2017enabling]. Technische Studien messen Zeit und Genauigkeit ohne Laien [@abushwereb2019knowledge; @wang2019automatic]. Die Sprachsysteme sind mit Fachleuten evaluiert [@atakan2025kakadoo; @park2026bimllm]. Für den deutschen Fertighausvertrieb fehlen Ausgangswerte zu Planständen und Änderungsschleifen (Recherche 23).

**L9 Von der Geometrie zur Fertigungsbearbeitung bei Dach und TGA (FF6).** Dachverfahren enden bei Dachflächen [@kelly2011interactive; @held2017roofs]. Abbundwerkzeuge setzen eine fertige Stabgeometrie voraus [@mork2020parametric; @compastimber]. Die geprüften Arbeiten zum TGA-Routing kennen keine Bohrregeln im Holzbau und übergeben Durchbrüche nicht als Fertigungsbearbeitung [@baradaran2022parametric; @blokland2023literature]. Die Entwässerungsarbeit von Zhang et al. ist dafür nicht am Inhalt geprüft [@zhang2022bimbased].

**L10 Reifegrade in einem generativen System (FF6).** Das Multi-LOD-Metamodell ist an von Hand gebauten Modellen erprobt [@abualdenien2019metamodel]. Die Integration von IDS und LOIN gelingt nur teilweise [@akbas2025holistic]. Wie drei Reifegrade aus einem regelbasiert erzeugten Modell entstehen und je Stufe prüfbar sind, ist nicht untersucht.

**L11 Der deutsche Fertighausmarkt ist empirisch kaum erforscht (FF5).** Begutachtete Studien zu Plattformen und Mass Customization stammen überwiegend aus Schweden, Großbritannien und Japan [@lessing2015industrialised; @barlow2003choice]. Ausnahmen sind zwei Arbeiten zu deutschen Herstellern [@thuesen2011efficient; @schoenwitz2012nature]. Die regionale Recherche fand an der TH Rosenheim Forschung zu Robotik und Schallschutz, aber kein Projekt zu Kundenkonfiguration oder Laienentwurf (Recherche 21). Der Konfigurator eines bayerischen Herstellers ist nur über eine Pressemitteilung belegt [@np2025haas].

### 5.8.2 Abgrenzung

Die Arbeit beansprucht **keine** neue Grundlagentechnik (These 1). Im Einzelnen:

- **Keine neue Regelsprache.** Die Arbeit nutzt IDS für Informationsanforderungen und eine Regelmaschine für Geometrie. Sie folgt damit dem Muster von CHEK und MBO2BIM [@chek2024d22; @mbo2bim2023].
- **Kein neues Sprachmodell.** Das Intent-Modell wird ausgewählt, feinabgestimmt und kalibriert, nicht entwickelt.
- **Kein neuer Grundriss- oder Dachalgorithmus.** Constraint-Programmierung, lineare Optimierung und Straight Skeleton werden übernommen [@lottaz1998constraint; @upasani2020dimensioned; @aichholzer1995novel].
- **Keine automatische Regelextraktion aus Normtext.** Regeln werden von Hand mit Normverweis formalisiert. Das ist fachlich wegen L6 und rechtlich wegen des Urheberrechts an Normen geboten (Kapitel 4.9).
- **Keine Rechtsberatung und kein Ersatz der Freigabe.** Die bauvorlageberechtigte Person bleibt verantwortlich (Kapitel 4.3.5).

### 5.8.3 Beitrag

Der Beitrag ist die **Integration** vorhandener Bausteine in einem standardkonformen Informationsmodell. Er lässt sich in sechs Teilbeiträge gliedern:

| Beitrag | adressiert | FF | Kapitel |
|---|---|---|---|
| B1 Informationsmodell eines Holzrahmenbau-Fertighauses in IFC4X3_ADD2 bis zu Ständer und Verbindungsmittel, mit Phasenabdeckung und standardkonformer Überbrückung der Grenzen | L1, L4 | FF1 | 8 |
| B2 Validierung als Teil der Generierung: Validation Service, IDS je Übergabe und Reifegrad, Fachprüfung, Round-Trip-Messung in Fremdsoftware | L5, L10 | FF1, FF6 | 8, 11, 20 |
| B3 Regelraum aus BayBO, eingeführten Normen, Handwerks- und Herstellerregeln, der den Entwurf während der Erzeugung begrenzt und mit Begründung und Alternative ablehnt | L2, L3 | FF2 | 9, 9a |
| B4 neuro-symbolische Sprachschnittstelle für Deutsch, in der das Sprachmodell nur Absicht und typisierte Parameter wählt | L6, L7 | FF3 | 7, 10 |
| B5 Ableitung von Bauvorlagen und Maschinendaten (BTLx, WUP) aus demselben Modell, einschließlich Dach- und TGA-Bearbeitungen | L1, L9 | FF1, FF6 | 13, 14, 17, 18 |
| B6 Evaluationsdesign, das Laienstudie und Messung der Baubarkeit verbindet, mit Ausgangswerten eines deutschen Herstellers | L8, L11 | FF5 | 20 |

### 5.8.4 Belastbarkeit der Neuheitsbehauptung

Nach dem Stand dieser Recherche lautet die Neuheitsbehauptung: Keine bekannte Arbeit lässt Laien per Sprache in einem formalisierten Holzrahmenbau-Regelraum eines realen Herstellers deterministisch entwerfen, erzeugt daraus ein IFC-4.3-Modell bis zum Verbindungsmittel, prüft es gegen Bauordnung und Herstellerregeln und leitet daraus Bauvorlagen und Maschinendaten ab. Die Einzelteile haben Vorläufer, die Kette als Ganzes nicht (Recherche 11).

Die Behauptung steht unter drei Vorbehalten:

1. **Pang et al. (2026)** ist nicht im Volltext geprüft [@pang2026natural]. Bis dahin darf die Arbeit für die Kombination „Sprache plus Regeln bei der Erzeugung plus BIM“ nicht „erstmals“ beanspruchen.
2. **Die Sättigung ist nicht nachgewiesen.** Runde 3 des Schneeballverfahrens wurde nach 3 von 53 Startquellen abgebrochen, die Cluster Sprache und Bauantrag sind nicht gemessen (Recherche 28).
3. **Deutsche Hochschulschriften sind unvollständig erfasst.** DNB und GEPRIS waren nicht direkt abfragbar (Recherche 21). Eine Nachsuche vor der Abgabe ist nötig.

Die Vorbehalte betreffen die Formulierung der Neuheit, nicht die Lücken. Schließt eine Arbeit ein einzelnes Glied, bleibt die Integration über alle Glieder offen, und sie ist der Beitrag.

## Verwendete Schlüssel

Das Kapitel enthält 548 Zitatstellen zu 321 Schlüsseln. Ein Python-Abgleich aller `[@key]` im Text gegen `literatur/lit-*.bib` ergab am 27.09.2026 keine fehlenden Schlüssel. Die Schlüssel `du2026text2bim` und `mbo2bim2023` stehen in zwei Bib-Dateien (bekannte Dublette, siehe `literatur/KORREKTUREN.md`); zugeordnet ist jeweils die erste Datei.

**lit-A-acc-bim.bib** (48): `amor2021promise`, `beach2015rulebased`, `bimbauantrag2020abschluss`, `borrmann2021bim`, `bsi2024ids`, `bsi2025validation`, `chek2024d22`, `chen2024automated`, `dimyadi2017evaluating`, `du2026text2bim`, `eastman2009automatic`, `fauth2024taxonomy`, `fauth2026digital`, `fischer2025bridging`, `fuchs2022neural`, `fuchs2024intermediate`, `haeussler2021code`, `hettiarachchi2025codeaccord`, `hjelseth2011capturing`, `idis2021szenarien`, `iso2024ifc`, `iversen2026leveraging`, `jaud2020georeferencing`, `jaud2022georeferencing`, `krijnen2020efficient`, `lai2018interoperability`, `madireddy2025large`, `mbo2bim2023`, `merigoux2021catala`, `mohun2020cracking`, `moult2020compliance`, `noardo2020integrating`, `noardo2022unveiling`, `palmirani2011legalruleml`, `pauwels2011semantic`, `preidel2015automated`, `samarawickrama2026digital`, `sergot1986british`, `shi2025finetuning`, `solihin2015classification`, `stepien2023openbimrl`, `tomczak2022review`, `vanberlo2021future`, `ying2021generating`, `ying2021rulebased`, `zhang2015interoperable`, `zhang2016semantic`, `zhang2017integrating`

**lit-B-vorfertigung-ki.bib** (67): `abanda2017bim`, `atakan2025kakadoo`, `barlow2003choice`, `caetano2020computational`, `chen2019bert`, `chen2025agent`, `chernev2015choice`, `compastimber`, `dasilveira2001mass`, `duarte2005towards`, `felfernig2014knowledge`, `forza2006product`, `franke2010designed`, `gann1996construction`, `garcez2023neurosymbolic`, `geier2022bimwood`, `habraken2021supports`, `haug2012definition`, `hemphill1990atis`, `hvam2008product`, `iyengar2000choice`, `jang2024nadia`, `jansson2014platform`, `jensen2012configuration`, `jensen2015product`, `ji2023hallucination`, `johnsson2013production`, `kaufmann2018manual`, `kendall2000residential`, `koning1981language`, `laignel2021floor`, `lee2024generalized`, `leng2023tell2design`, `lessing2015industrialised`, `liggett2000automated`, `linner2012evolution`, `merrell2010computer`, `merrell2011interactive`, `mesnil2015rnn`, `michalek2002architectural`, `nahmens2011customization`, `nauata2020housegan`, `nauata2021housegan`, `piller2004mass`, `pine1993mass`, `pundak2018deep`, `radford2023whisper`, `randall2007user`, `sabin1998product`, `saka2024gpt`, `salvador2009cracking`, `scheibehenne2010choice`, `schoenwitz2012nature`, `schoenwitz2017product`, `shabani2023housediffusion`, `stehn2002integrated`, `thuesen2011efficient`, `trentin2013sales`, `tum2023bimwood`, `tur2011spoken`, `venable2016feds`, `weber2022automated`, `wikberg2014design`, `wu2019data`, `yao2023react`, `yu2011make`, `zheng2023dynamic`

**lit-C-recht-normen.bib** (7): `bimbauantrag2020`, `bsiMvd43`, `bsiValidation`, `btlx23`, `dataholz`, `dbauv2026`, `nrw2026bimbauantrag`

**lit-D-vergleich-vorfertigung.bib** (36): `adel2018design`, `adel2020computational`, `alwisy2019bim`, `barlow2005building`, `benros2009integrated`, `chateauvieux2023bim`, `duarte2001customizing`, `duarte2005discursive`, `farr2014bim`, `graser2020dfab`, `jansson2018artistic`, `johnsson2009defects`, `khalili2016development`, `knight2010looks`, `kwiecinski2016wood`, `kwiecinski2019customers`, `kwiecinski2023interactive`, `lennartsson2022exploring`, `liu2018bim`, `malmgren2010product`, `orozco2023codesign`, `piroozfar2019configuration`, `popovic2020development`, `popovic2021configuration`, `puusepp2017enabling`, `ramaji2017product`, `rojaswettling2023idm`, `sandberg2008knowledge`, `sass2006wood`, `shafiee2025enhancing`, `swanenburg2016towards`, `timbim2024`, `veenstra2006methodology`, `wagner2020flexible`, `wang2019automatic`, `zhou2023platforming`

**lit-E-vergleich-automation.bib** (34): `abualdenien2019metamodel`, `abualdenien2022levels`, `abushwereb2019knowledge`, `aichholzer1995novel`, `apolinarska2016mastering`, `baradaran2022parametric`, `blokland2023literature`, `erhan2026dcodeweaver`, `hellin2025natural`, `hellin2026bim`, `jeong2009benchmark`, `kelly2011interactive`, `kodnongbua2024zeroshot`, `kou2008design`, `kou2010knowledge`, `liao2021structgan`, `liu2021panelization`, `ma2006testing`, `manrique2015automated`, `medjdoub2018parametric`, `mirhosseini2026ambiguity`, `mork2020parametric`, `niemeijer2009checkmate`, `niemeijer2011constraint`, `nithyanantham2025mcp4ifc`, `pang2026natural`, `pazlar2008interoperability`, `preidel2020konformitaet`, `saluz2025semio`, `shin2021bimasr`, `singh2021automating`, `sydora2020rulebased`, `upasani2020dimensioned`, `wang2024cloud`

**lit-F-architekturpsychologie.bib** (2): `fischer1991critiquing`, `meseguer2006soft`

**lit-G-luecken.bib** (9): `eisfeld2022variowohnen`, `fraunhoferipa0000designchain`, `heinzmann2022automatisierung`, `kaufmann2018leanwood`, `krueger2026steckhaus`, `np2025haas`, `schuster2022bimwood`, `sonnenberg2012evaluations`, `tugraz2025syswood`

**lit-H-ff4-ff5.bib** (5): `haug2011impact`, `kristjansdottir2018return`, `thajudeen2022supporting`, `trentin2012product`, `wilhelmi2020haftung`

**lit-I-schneeball-a.bib** (48): `abushwereb2019framework`, `ataide2023digital`, `battisti2022automatic`, `bloch2023unbalanced`, `bogaerts2021step`, `cao2021cross`, `cerovsek2025advancing`, `darwish2022automated`, `day2019knowledge`, `dimyadi2016computerizing`, `eastman2010exchange`, `fischer2024extending`, `fuchs2025exploring`, `khaliliaraghi2020variability`, `kwiecinski2014system`, `kwiecinski2018hopla`, `laakso2012ifc`, `lee2016modularized`, `lee2016ontology`, `lee2019mechanism`, `lee2020comparative`, `lee2026automated`, `liu2016ontology`, `loboscalquin2024implementation`, `mtehrani2025streamlining`, `narayanaswamy2019bim`, `niemeijer2014freedom`, `noardo2022ifc`, `nuyts2024comparative`, `pauwels2017performance`, `pinto2026exhaustive`, `preidel2016towards`, `ramaji2017extending`, `senousy2026automated`, `sobhkhiz2021framing`, `tonguc2026code`, `urban2024adapting`, `urban2026development`, `venugopal2012semantics`, `wongchong2021logic`, `wu2025design`, `wu2026revisiting`, `yin2019building`, `zentgraf2023concept`, `zhang2021clustering`, `zhang2023rule`, `zhang2023unpacking`, `zheng2026translating`

**lit-I-schneeball-b.bib** (33): `bakhshi2021dfma`, `chateauvieuxhellwig2022timber`, `dellaert2005marketing`, `dineniso7817-1`, `eder2021exact`, `elghaish2022voice`, `erculiani2019layout`, `fernandes2024gptassistant`, `fischer1989environments`, `gao2023pal`, `haug2019causes`, `held2017roofs`, `hentschke2020customer`, `huang2024semanticgap`, `jang2024interactivedesign`, `kristjansdottir2018challenges`, `li2024spatial`, `lin2026defects`, `oh2010furniture`, `park2026bimllm`, `randall2005principles`, `raposo2024bridging`, `renner2025copilot`, `schick2023toolformer`, `trentin2011overcoming`, `trentin2014increasing`, `vonhippel2001user`, `vonhippel2002shifting`, `wang2021knowledge`, `wang2021needsbased`, `wang2022natural`, `wu2026alterations`, `zhang2026multiagent`

**lit-J-schneeball-runde2.bib** (28): `akbas2025holistic`, `an2020bimbased`, `andre2019exploring`, `dong2025bim`, `dudek2023mass`, `eriksson2019assessing`, `gelle2003solving`, `guo2025advancing`, `hjelseth2015public`, `ilal2022integrating`, `krischmann2020entwicklung`, `kutzias2024recent`, `larsen2019mass`, `lennartsson2021plm`, `lottaz1998constraint`, `malmgren2010customization`, `mcdermott1982rulebased`, `mowbray2023representing`, `olsson2018automation`, `recski2024briseplandok`, `sviokla1990examination`, `vanberlo2019creating`, `wei2025texttostructure`, `yang2012constraint`, `yang2024promptbased`, `yang2026llmpowered`, `yin2023twostage`, `zhang2022bimbased`

**lit-L-schneeball-runde3.bib** (4): `cao2022ontologybased`, `fisher2024paad`, `saka2023conversational`, `weld2022survey`

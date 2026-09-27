# 9b Entwurfsqualität: Architekturpsychologie und Kulturprofile

Status: Entwurf v0.1 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`, überwiegend auf `lit-F-architekturpsychologie.bib`. **[V]** = an Primärquelle, Abstract oder Verlagsseite geprüft, **[U]** = unsicher oder nicht erneut geprüft.

## 9b.0 Einordnung und Vorgehen

Die Kapitel 4, 9 und 9a beschreiben Regeln, die einen Entwurf zulassen oder verbieten. Ein Haus kann aber alle diese Regeln einhalten und trotzdem schlecht sein. Das Schlafzimmer kann an der lauten Straße liegen, die Küche drei Räume vom Essplatz entfernt, und das Kinderzimmer kann so geschnitten sein, dass kein Bett hineinpasst, ohne dass die Tür an das Bett schlägt. Architektinnen und Architekten vermeiden solche Fehler aus Erfahrung. Ein Laie, der mit dem System selbst entwirft, hat diese Erfahrung nicht.

Das Zielbild fasst die Antwort in Prinzip 8 zusammen: **Assistieren statt bevormunden.** Neben den harten Regeln gibt es Empfehlungen aus der Architektur- und Umweltpsychologie, jede mit Begründung und Evidenzgrad. Kulturprofile wie Feng Shui, Vastu oder Baubiologie kann der Kunde wählen. Sie sind als Tradition gekennzeichnet und werden nie als Wissenschaft ausgegeben. Dieses Kapitel macht das Prinzip formal und prüfbar. Es beantwortet vier Fragen:

1. Wie unterscheidet sich eine Empfehlung formal von einer Regel, und wie wird sie berechnet?
2. Welche Wirkfaktoren sind so gut belegt, dass das System sie als Empfehlung vertreten darf, und wie lassen sie sich am Grundrissmodell messen?
3. Wie werden Kulturprofile abgebildet, ohne dass Tradition als Wissen erscheint oder Kunden bevormundet werden?
4. Welche Form der Assistenz ist ethisch vertretbar, wenn die Wirksamkeit von Nudges selbst umstritten ist?

**Quellenbasis.** Grundlage sind die Recherchen 15 (Kern), 21 (deutschsprachige Architekturpsychologie, BBSR-Studie zum Homeoffice), 20 (Außenlärm) und 13 (Möblierung und Stellflächen). In der Quellenbewertung (`literatur/quellen-bewertung.csv`) tragen 180 Quellen einen Bezug zu Kapitel 9b. Davon sind 27 als „übernehmen“, 70 als „adaptieren“, 71 als „Kontext“, 10 als „abgrenzen“ und 2 als „verwerfen“ eingestuft. Für 72 dieser Quellen lag in der Bewertungsrunde kein Abstract vor. Aussagen über Studienergebnisse stehen im Text deshalb nur dort, wo Abstract, Einzelbewertung oder Recherche sie stützen. Wo nur der Titel bekannt ist, ist das vermerkt.

**Qualität der Einstufung.** Die Zweitbewertung einer Stichprobe von 80 Quellen ergab für die Relevanz zu FF6, der Forschungsfrage dieses Kapitels, ein quadratisch gewichtetes κ = 0,81 bei 66 % exakter Übereinstimmung. Für die Quellenqualität lag κ bei 0,95, für die Nutzungsart („übernehmen“, „adaptieren“ usw.) nur bei 0,45 [@cohen1960coefficient; @landis1977measurement]. Zwei der neun abweichenden Kernbestand-Entscheidungen betreffen dieses Kapitel (`bafna2003space`, `oswald2007housing`). Daraus folgt zweierlei. Erstens ist die Relevanz der Quellen reproduzierbar eingestuft. Zweitens ist die Frage, *wie* eine Quelle genutzt wird, eine Ermessensentscheidung. Das gilt erst recht für die Evidenzgrade der Empfehlungen, die aus diesen Quellen abgeleitet werden. Abschnitt 9b.2 zieht daraus die Konsequenz, dass die Grade selbst doppelt bewertet und versioniert werden.

**Abweichung von der Gliederung.** Das Evidenzgrad-Schema (Gliederungspunkt 6) steht hier als Abschnitt 9b.2 vorn, weil alle folgenden Abschnitte es verwenden. Die Ethik der Assistenz folgt in 9b.7. Die Gliederungspunkte 2 bis 5 entsprechen den Abschnitten 9b.3 bis 9b.6.

## 9b.1 Regelklasse R5 „Empfehlungen“

### 9b.1.1 Definition und Abgrenzung

Kapitel 4.1 unterscheidet vier Regelklassen nach ihrer Funktion im System: R1 Entwurfsgrenzen, R2 Informationsanforderungen, R3 Verantwortungsregeln und R4 Formregeln. Allen vier ist gemeinsam, dass ihre Verletzung einen Fortgang verhindert: Ein Entwurf außerhalb der Abstandsflächen ist unzulässig, ein Modell ohne Gebäudeklasse unvollständig, ein Bauantrag ohne Unterschrift nicht einreichbar. Die fünfte Klasse ist von anderer Art.

> **Definition 9b.1 (R5-Empfehlung).** Eine R5-Regel ist ein Prädikat über das Grundriss- und Gebäudemodell, das einen Grad der Erfüllung zwischen 0 und 1 liefert. Sie trägt einen Evidenzgrad, eine Evidenzart, Quellen und einen Erklärtext. Ihre Verletzung blockiert nichts. Sie erzeugt einen Hinweis und verändert ein Qualitätsprofil.

| Merkmal | R1–R4 (hart) | R5 (weich) |
|---|---|---|
| Wirkung einer Verletzung | blockiert Entwurf, Übergabe oder Freigabe | Hinweis, Profilwert sinkt |
| Wer kann abweichen? | niemand (R1, R2, R4) bzw. nur die berechtigte Person (R3) | der Kunde, ohne Begründungspflicht |
| Geltungsgrund | Recht, Norm, Herstellerregel (Status N) | Evidenz über Wirkung oder Präferenz, Planungswissen |
| Ergebnis | wahr/falsch mit Grenzwert und Ausnutzung | Erfüllungsgrad, Evidenzgrad, Begründung |
| Konflikte zwischen Regeln | nicht zulässig (Lösungsraum leer) | zulässig und sichtbar (Zielkonflikt) |
| Formalisierung | Constraint, IDS, Freigabe-Gate, Export | gewichteter Soft Constraint [@meseguer2006soft] |

Die Abgrenzung ist nicht immer eine Frage des Inhalts, sondern der Geltung. Dasselbe Thema kann in beiden Klassen vorkommen. Die Fensterfläche von einem Achtel der Netto-Grundfläche ist nach Art. 45 BayBO eine R1-Grenze [@baybo2026]. Der Tageslichtquotient nach DIN 5034-1 [@din5034-1] und die Stufen der DIN EN 17037 [@din2019tageslicht] sind für Einfamilienhäuser nicht bauaufsichtlich verlangt und erscheinen als R5-Hinweis (Beispiel 4.3). Beim Außenlärm ist der Nachweis nach DIN 4109 eine harte Regel (Recherche 20). Die Empfehlung, Schlafräume an die ruhige Fassade zu legen, ist dagegen R5, auch wenn sie den harten Nachweis erleichtert.

Deshalb führt das Schema einen **Status N** (Norm oder Recht), der vom Evidenzgrad unabhängig ist. Eine Norm kann verbindlich sein, auch wenn ihr Inhalt empirisch nur als Expertenkonsens (Grad C) gilt. Umgekehrt kann eine gut belegte Wirkung (Grad A) rechtlich unverbindlich sein, etwa die Schwellen der WHO-Lärmleitlinie [@who2018noise].

Zu R2 besteht eine Abhängigkeit. Viele R5-Prädikate brauchen Informationen, die nicht jeder Entwurfsstand enthält: Möblierung, Himmelsrichtung, Lärmpegel an der Fassade. Fehlt die Information, liefert die Regel den Wert „nicht bewertbar“ statt 0 (Designentscheidung). Sonst würde ein unvollständiges Modell als schlechtes Modell erscheinen.

### 9b.1.2 Der Regeldatensatz

Jede R5-Regel ist ein versionierter Datensatz mit folgenden Feldern (angelehnt an Recherche 15):

- `id` und Version, z. B. `R5-RUHE-02@1.1`
- Prädikat über Raumgraph und Geometrie, mit Parametern und Einheiten
- Dimension des Qualitätsprofils (9b.5)
- Evidenzgrad (A, B, C, D, X) und Evidenzart (Wirkung, Präferenz, Markt), s. 9b.2
- Quellen als BibTeX-Keys
- Laientext und Fachtext, getrennt formuliert
- bekannte Konfliktregeln, z. B. Vastu-Schlafzimmerlage gegen thermischen Komfort
- Zuständigkeit: allgemein, Nutzerprofil (z. B. „Homeoffice“, „barrierefrei vorbereitet“) oder Kulturprofil

Die Trennung von Laien- und Fachtext folgt einem Befund der deutschsprachigen Architekturpsychologie: Architekten und Laien nehmen Räume unterschiedlich wahr und bewerten sie unterschiedlich [@rambow2000expertenlaien]. Eine Befragung zu drei Grundrissvarianten einer Plattenbauwohnung zeigt systematische Unterschiede zwischen beiden Gruppen, vor allem bei Topologie, Privatheit und der Abgrenzung öffentlicher und privater Zonen [@boumova2016apartment]. Ein Erklärtext, den ein Architekt plausibel findet, erreicht den Laien also nicht ohne Weiteres.

Dass qualitative Begriffe formalisiert und bis zur Quelle rückverfolgbar gehalten werden können, zeigen Li et al. Sie führen Formulierungen wie „leicht zu sehen“ in einem Answer-Set-Programm über Abstraktionsebenen auf Befunde der Kognitionspsychologie zurück [@li2020qualitative]. Zahedi et al. binden Entwurfsentscheidungen mit Absicht und Begründung an Modellelemente [@zahedi2022bim]. Beide Arbeiten stützen den Ansatz, jede Empfehlung als Datensatz mit Quellenbezug im Modell zu führen.

### 9b.1.3 Berechnung als Soft Constraints

Die harten Regeln R1 bestimmen die Menge zulässiger Entwürfe $X$. Für einen Entwurf $x \in X$ liefert jede R5-Regel $i$ einen Erfüllungsgrad

$$s_i(x) \in [0,1] \cup \{\bot\},$$

wobei $\bot$ „nicht bewertbar“ bedeutet. Das Gewicht einer Regel ergibt sich aus ihrem Evidenzgrad $e_i$ und einer Gewichtung $u_d$ der Dimension $d$, die der Kunde ändern kann:

$$w_i = g(e_i)\cdot u_{d(i)}, \qquad g(\mathrm{A}) = 1{,}0;\ g(\mathrm{B}) = 0{,}7;\ g(\mathrm{C}) = 0{,}4;\ g(\mathrm{D}) = g(\mathrm{X}) = 0.$$

Die Werte von $g$ sind eine Designentscheidung und werden über die Bewohnerbefragung nach Einzug kalibriert (9b.5.4). Der Wert einer Dimension ist das gewichtete Mittel ihrer bewertbaren Regeln:

$$S_d(x) = \frac{\sum_{i \in I_d,\ s_i(x) \neq \bot} w_i\, s_i(x)}{\sum_{i \in I_d,\ s_i(x) \neq \bot} w_i}.$$

Ausgegeben wird der Profilvektor $\mathbf{S}(x) = (S_1(x), \dots, S_m(x))$, nicht seine Summe. Zu jeder Dimension gehört eine Abdeckung, also der Anteil der bewertbaren Regelgewichte. Kulturprofile erhalten einen eigenen Teilscore $K_p(x)$ gleicher Form, in dem alle Regeln des gewählten Profils das Gewicht 1 haben. Er fließt nie in $\mathbf{S}$ ein.

Formal ist das ein gewichtetes Constraint-Problem im Sinne von Meseguer, Rossi und Schiex [@meseguer2006soft]. Anders als dort wird aber nicht die Summe der Verletzungskosten minimiert. Die Aggregation über Dimensionen unterbleibt absichtlich, weil sie Zielkonflikte verdeckt (9b.5.3). Dasselbe Muster, weiche Präferenzen neben harten Regeln, verwenden Erculiani et al. in einem Grundrissgenerator, der Präferenzen im Dialog lernt [@erculiani2019layout]. Merrell et al. zeigen für die Möblierung, dass Gestaltungsleitlinien als Terme einer Bewertungsfunktion Laien zu messbar besseren Anordnungen führen [@merrell2011interactive]. Ihr stochastisches Sampling übernimmt die Arbeit nicht, weil die Kette deterministisch bleiben soll (Kapitel 7).

## 9b.2 Evidenzgrad-Schema

### 9b.2.1 Grade und Evidenzarten

Das Schema lehnt sich an GRADE an, das Evidenzqualität und Empfehlungsstärke trennt [@guyatt2008grade]. Die Übertragung von der Medizin auf Entwurfsregeln ist eine eigene Adaption. Sie unterscheidet zwei Achsen.

Die erste Achse ist der **Grad**:

| Grad | Definition | Beispiele | Darstellung für Laien |
|---|---|---|---|
| **A** | Systematisches Review oder Meta-Analyse mit konsistentem Befund zur *Wirkung*, oder evidenzbasierte Leitlinie nach GRADE | WHO-Lärmleitlinie 2018 [@who2018noise]; Radon-Referenzwert [@bfs2025radon] | „gut belegt“ |
| **B** | Kontrollierte Einzelstudien, konsistente Beobachtungsstudien, Konsensempfehlungen auf Laborbasis, oder Meta-Analysen, die nur *Präferenz* messen | Fensterblick im Crossover-Experiment [@ko2020window]; Bettposition [@spoerrle2010sleeping; @bonin2023goodnight]; Kurvenpräferenz [@chuquichambi2022curvature] | „belegt (Studien)“, bei Präferenz „Die meisten Menschen bevorzugen …“ |
| **C** | Expertenkonsens, Lehrbuch, Norm oder Bewertungssystem ohne direkte Wirkungsstudie | WBS [@bwo2015wbs]; Neufert [@neufert2022bauentwurfslehre]; Alexander-Muster [@alexander1977pattern]; Besonnungsdauer nach EN 17037 | „bewährte Planungsregel“ |
| **D** | Tradition oder Kulturlehre ohne empirische Prüfung | Bagua-Raster, Vastu-Mandala, harmonische Proportionen | „traditionelle Lehre, nicht wissenschaftlich belegt“ |
| **X** | Geprüft und ohne Befund oder widerlegt | Wünschelrute, „Wasseradern“ [@enright1995dowsing] | wird nicht angeboten, nur auf Nachfrage erklärt |

Die zweite Achse ist die **Evidenzart**:

- **Wirkung (W):** Gesundheit, Wohlbefinden, Leistung, Schlaf.
- **Präferenz (P):** was Menschen wählen oder schön finden.
- **Markt (M):** Zahlungsbereitschaft beim Kauf.

Grad und Art werden zusammen angegeben, z. B. „A-W“ für die Lärmschwellen der WHO oder „B-P“ für die Bettposition.

Drei Einstufungsregeln sind für die Konsistenz wichtig:

1. **Präferenz erreicht höchstens B.** Auch eine Meta-Analyse zur Präferenz belegt nur, was Menschen mögen, nicht, was ihnen guttut. Die Kurvenpräferenz ist meta-analytisch gut gesichert (Hedges' g = 0,39 aus 61 Studien), aber vom Reiz, von der Darbietungszeit, der Aufgabe und der Expertise abhängig [@chuquichambi2022curvature]. Sie wird deshalb als B-P geführt. Recherche 15 hatte sie für Objekte mit A eingestuft. Diese Einstufung wird hier korrigiert, weil sie der eigenen Definition widerspricht.
2. **Narrative Übersichten erreichen höchstens B.** Grad A verlangt ein systematisches Vorgehen. Die Übersichten von Evans zu Wohnen, Beengtheit und Kindesentwicklung sind wertvoll, aber nicht systematisch [@evans2003built; @evans2006child]. Crowding wird deshalb als B-W geführt, nicht wie in Recherche 15 als A/B.
3. **Neurowissenschaftliche Befunde erhöhen keinen Grad.** fMRI-Studien mit Bildreizen messen ästhetische Urteile, keine Langzeitwirkung. Der Schluss von der aktivierten Hirnregion auf einen psychischen Zustand ist schwach [@poldrack2006reverse]. Die Neuroarchitektur fordert selbst Studien mit Bewegung im Raum statt unbewegter Probanden [@wang2022embodiment; @coburn2017buildings; @higueratrujillo2021cognitive]. „Neuro“ ist deshalb kein Qualitätsmerkmal. Vartanians Befunde zu Raumhöhe und Kontur zählen als Präferenzstudien wie andere auch [@vartanian2015ceiling; @vartanian2013contour].

### 9b.2.2 Abgrenzung zur Quellenqualität

Die Quellenbewertung der Arbeit verwendet ebenfalls Buchstaben A bis D, aber mit anderer Bedeutung (Review-Protokoll, Kapitel 2a): Sie bewertet die *Quelle* (Übersichtsarbeit, Einzelstudie, graue Literatur, Tradition). Der Evidenzgrad bewertet die *Aussage einer Regel* über alle Quellen hinweg. Eine Quelle der Qualität A kann eine Regel des Grades C tragen. Die Meta-Analyse zu Prospect-Refuge etwa ist eine Übersichtsarbeit, ihr Befund für Innenräume bleibt aber inkonsistent [@dosen2016prospect]. Umgekehrt kann eine Einzelstudie der Qualität B zusammen mit einer Replikation eine B-Regel tragen. Im System und im Text wird deshalb immer „Evidenzgrad“ geschrieben, wenn die Regel gemeint ist.

### 9b.2.3 Sprachliche Trennung

Die Evidenzart bestimmt die Satzform. Das System erzeugt Erklärtexte aus Vorlagen, die an Grad und Art gebunden sind:

| Art und Grad | zulässige Formulierung | unzulässig |
|---|---|---|
| W, A | „… schadet nachweislich …“, „… senkt das Risiko …“ | – |
| W, B (Beobachtung) | „… hängt in Studien mit … zusammen“ | „… bewirkt …“ |
| P, B | „Die meisten Menschen bevorzugen …; eine Wirkung auf … ist nicht belegt.“ | „… ist gesünder“, „… schläft besser“ |
| C | „bewährte Planungsregel nach …“ | „wissenschaftlich erwiesen“ |
| M | „In Märkten mit … zahlen Käufer für … mehr bzw. weniger.“ | Ableitung einer Wirkung aus dem Preis |
| D | „Nach der Lehre des … gilt …“ | Indikativ als Tatsache („das Chi fließt ab“) |
| X | „wurde geprüft und nicht bestätigt“ | jede Bewertung am Grundriss |

Die Trennung ist keine Stilfrage. Querschnittsstudien, etwa aus dem Lockdown, zeigen Zusammenhänge, keine Ursachen [@amerio2020covid; @fornara2022space]. Eine Formulierung im Kausalmodus würde die Evidenz überhöhen.

### 9b.2.4 Pflege der Grade

Evidenzgrade sind zeitgebunden. Sie werden wie Regelwerk-Profile versioniert (Kapitel 9.3). Jede Änderung eines Grades erzeugt eine neue Regelversion, und der Nachweis nennt die Version (Prinzip 9 des Zielbilds). Wegen des mittelmäßigen κ bei der Nutzungsart (9b.0) wird jeder Grad von zwei Personen unabhängig vergeben. Die Übereinstimmung wird wie in der Quellenbewertung berichtet.

## 9b.3 Evidenzbasierte Wirkfaktoren

### 9b.3.1 Übersicht

Die folgende Tabelle führt die Faktoren, die das System als Empfehlung vertritt. Sie ist nach Evidenzgrad geordnet. Faktoren mit Präferenz-Evidenz sind als solche ausgewiesen.

| Faktor | Befund | Evidenzgrad | rechenbare Kennzahl / Entwurfsregel | Quelle |
|---|---|---|---|---|
| Verkehrslärm | Leitlinie nach GRADE: Straßenverkehr schadet ab 53 dB Lden bzw. 45 dB Lnight; Review zu Schlaf und Herz-Kreislauf | A-W | Lden/Lnight je Fassade aus der Lärmkarte (nur Screening); Hinweis bei Lden > 53 dB; Schlafräume an die Fassade mit dem geringsten Pegel | [@who2018noise; @basner2014noise] |
| Ruhige Seite | Zugang zur ruhigen Seite senkt Belästigung (OR 0,47); Schlafzimmerfenster dorthin senkt das Risiko schlechten Schlafs; Fensterorientierung sagt Schlaf besser vorher als der Pegel an der lautesten Fassade | B-W | Prädikat: jeder Schlafraum hat ≥ 1 Fenster an der leisesten Fassade; Kennzahl ΔL zwischen lautester und Schlafraumfassade | [@ohrstrom2006quietness; @bodin2015quiet; @bartels2021impact; @roswall2020nighttime] |
| Tageslicht | Review: begrenzte, aber für die Planung nutzbare Belege | B-W; Schwellen C | 1/8-Regel (N, R1); Tageslichtquotient (Hinweis); EN 17037 „gering“: 300 lx auf 50 %, 100 lx auf 95 % der Fläche | [@aries2015daylight; @din5034-1; @din2019tageslicht] |
| Zirkadianes Licht | Konsens: tags ≥ 250 lx mEDI am Auge, abends ≤ 10 lx; mEDI als bester Prädiktor | B-W | Tagesarbeitsplätze in der Fensterzone; Schlafraum vollständig verdunkelbar | [@brown2022recommendations; @brown2020melanopic; @cajochen2022evening] |
| Besonnung | Normempfehlung ohne direkte Wirkungsstudie | C | ≥ 1 Wohnraum mit ≥ 1,5 h Besonnung am Stichtag, Sonnenstandssimulation | [@din2019tageslicht] |
| Blick nach draußen / ins Grüne | Baumblick: kürzere Liegezeit (23 gegen 23 Patienten); Crossover-Experiment (n = 86): kühler empfunden, positivere Emotion, besseres Arbeitsgedächtnis; Review: gemischte Befunde | B-W | Sichtverbindung nach außen vom Nutzungsort jedes Hauptaufenthaltsraums; Anteil Grün im Sichtkegel aus dem Grundstücksmodell | [@ulrich1984view; @ko2020window; @ohly2016attention; @abdalhamid2023quantifying] |
| Beengtheit, Rückzug | Chronische Beengtheit hängt bei Kindern mit Schulproblemen, Hilflosigkeit und Blutdruck zusammen (einkommenskontrolliert); Wohnraum wirkte im Lockdown über die Wohnzufriedenheit auf Stress | B-W | Personen je Raum ≤ 1; ein abschließbarer Raum je Person ab Schulalter; ≥ 1 Rückzugsort außerhalb der Schlafräume | [@evans1998crowding; @evans2006child; @fornara2022space] |
| Thermischer Komfort im Schlafraum | Reviews: Überhitzung beeinträchtigt den Schlaf, Planungsevidenz lückenhaft | B-W; Nachweis N | Warnung bei großen West- und Südwestverglasungen in Schlafräumen; sommerlicher Wärmeschutz als R1 | [@emmitt2023bedroom; @lan2017thermal; @din4108-2] |
| Zugänglichkeit im Alter | Zugänglichkeit und Nutzbarkeit der Wohnung hängen mit Selbstständigkeit und Wohlbefinden sehr alter Menschen zusammen | B-W (korrelativ) | Profil „barrierefrei vorbereitet“: Schlafen und Bad im EG, Bewegungsflächen 120 × 120 bzw. 150 × 150 cm, schwellenlos | [@oswald2007housing; @kremerpreiss2011wohnenalter] |
| Bettposition | 138 Personen stellen das Bett so, dass sie die Tür sehen, möglichst weit von ihr entfernt, auf der Seite des Türaufschlags; Replikation in Frankreich und der Slowakei | B-P | Prädikat: Tür vom Kopfkissen sichtbar ∧ Bett außerhalb des Türschwenks ∧ Abstand zur Tür maximal | [@spoerrle2010sleeping; @bonin2023goodnight] |
| Raumhöhe | höhere Decken werden in Bildstudien eher als schön beurteilt; Priming-Effekt auf den Denkstil ist Einzelbefund | B-P | lichte Höhe ≥ 2,50 m im Wohnbereich als Standard; Überhöhung als Option; Mindesthöhe ist N | [@vartanian2015ceiling; @meyerslevy2007ceiling] |
| Kurven statt Kanten | Meta-Analyse: Kurvenpräferenz, moderiert; kurvige Räume schöner beurteilt, ohne Effekt auf Annäherung | B-P | nur Hinweis bei Möbeln und Öffnungen (im Holzrahmenbau teuer) | [@chuquichambi2022curvature; @vartanian2013contour; @bar2006curved] |
| Prospect-Refuge im Innenraum | Meta-Analyse: Prospect in Innen- und Stadtstudien gestützt, Refuge neutral, Gesamtlage inkonsistent; Zusammenfassung von acht Studien: Effekte von Prospect und Refuge nahe null | C-P | Sitzplatz: Zugang im Isovist sichtbar, Wand im Rücken; Kennzahl Isovistenfläche | [@dosen2016prospect; @stamps2008some; @stamps2006interior] |
| Privatheitsgradient, Zonierung | Theorie der Privatheitsregulation; Space-Syntax-Analysen von Wohnhäusern; Laien und Architekten uneins über Zonen | C (teils B-P) | Tiefe der Schlafräume > Tiefe des Wohnbereichs; kein Schlafraum als Durchgangsraum | [@altman1975environment; @hanson1998decoding; @boumova2016apartment] |
| Orientierung | Isovistenmaße korrelieren mit Navigation und Raumerleben (VR); bei Demenz wirkt die Grundrisstypologie stärker als Beschilderung | C (Wohlbefinden); B-W (Demenz) | mittlere Tiefe, Integration, Sichtachse Eingang → Treppe und Wohnen | [@wiener2007isovist; @marquardt2011wayfinding; @turner2001isovists] |
| Farbe | Befunde uneinheitlich, kleine Stichproben, kaum Feldstudien; Sättigung und Helligkeit wirken stärker auf die Erregung als der Farbton | C (keine Wirkungsregel) | keine Farbregel mit Gesundheitsbezug, nur Stilberatung | [@elliot2014color; @wilms2018color] |

### 9b.3.2 Wirkung: Lärm, Licht, Außenbezug, Beengtheit

**Lärm** ist der einzige Faktor, bei dem eine Leitlinie nach GRADE vorliegt [@who2018noise]. Für den Grundriss wichtiger ist aber, *wo* der Pegel ankommt. Mehrere Studien stützen die Regel „Schlafräume zur ruhigen Seite“. Öhrström et al. fanden bei 956 Befragten, dass der Zugang zu einer ruhigen Seite Störungen um 30 bis 50 % senkt. Das entspricht etwa 5 dB weniger an der lautesten Fassade [@ohrstrom2006quietness]. In Malmö (2.612 Befragte) senkte der Zugang zu einer ruhigen Seite das Risiko der Belästigung (OR 0,47) [@bodin2015quiet]. In einer Querschnittsstudie mit berufstätigen Frauen sagte der modellierte Nachtpegel an der lautesten Fassade schlechten Schlaf kaum vorher, die Orientierung des Schlafzimmerfensters dagegen eher [@bartels2021impact]. In einer dänischen Kohorte mit 44.438 Personen ging der Nachtlärm an der lautesten Fassade mit einer leicht erhöhten Einlösung von Schlafmittelrezepten einher (HR 1,05), an der leisesten Fassade nicht (HR 1,00) [@roswall2020nighttime].

Die Regel verbindet sich mit dem harten Nachweis. DIN 4109-2 erlaubt an der abgewandten Fassade ohne Einzelnachweis einen Abschlag von 5 dB bei offener Bebauung (Recherche 20) [V]. Im Prototyp B19 sinkt dadurch das erforderliche Schalldämmmaß im Schlafzimmer von 42 auf 36,8 dB, und die Fenster brauchen Schallschutzklasse 3 statt 5. Hier fallen Empfehlung und Kostenersparnis zusammen. Das System zeigt beides, trennt aber die Begründungen: Die Wirkung auf den Schlaf ist Evidenz (A-W bzw. B-W), der Abschlag ist Norm (N).

**Tageslicht und zirkadianes Licht.** Das Review von Aries et al. findet nur begrenzte, statistisch belastbare Belege für Gesundheitswirkungen von Tageslicht, aber genug für erste Planungskategorien [@aries2015daylight]. Das rechtfertigt Grad B, nicht A. Für die nicht-visuelle Wirkung gibt es seit 2022 quantitative Konsensempfehlungen in melanopischer äquivalenter Tageslicht-Beleuchtungsstärke (mEDI) [@brown2022recommendations]. Die Wahl der Größe stützt eine Reanalyse von 19 Laborstudien, in der mEDI der beste Prädiktor zirkadianer Lichtwirkungen war [@brown2020melanopic]. Die Meta-Analyse zum Abendlicht mahnt zur Vorsicht. Sie findet Dosis-Wirkungs-Beziehungen für Einschlaflatenz und Schlafeffizienz im Bereich von 100 bis 1.000 lx mEDI, aber Gesamteffekte, deren Konfidenzintervalle null einschließen [@cajochen2022evening]. Messungen in Wohnungen zeigen, dass fast die Hälfte der Haushalte abends hell genug beleuchtet ist, um Melatonin um 50 % zu unterdrücken, bei großer individueller Streuung [@cain2020evening].

Für den Grundriss folgen daraus nur zwei Regeln: Arbeitsplätze in die Fensterzone und Schlafräume vollständig verdunkelbar. Die Abendlichtempfehlung gehört in die Bemusterung der Beleuchtung (Kapitel 12). Dort ist auch die Warnung von Houser et al. zu beachten: Human-Centric Lighting ist gut begründet, aber durch irreführende Werbeversprechen belastet [@houser2020humancentric].

**Außenbezug.** Ulrichs Krankenhausstudie ist der meistzitierte Beleg, aber klein, retrospektiv und nicht auf Wohnen bezogen [@ulrich1984view]. Belastbarer ist das randomisierte Crossover-Experiment von Ko et al. (n = 86). Mit Fenster war das thermische Empfinden kühler (0,3 Skalenpunkte, entsprechend 0,74 °C), 12 % mehr Personen waren thermisch zufrieden, positive Emotionen und Arbeitsgedächtnis waren besser. Kurzzeitgedächtnis, Planung und Kreativität unterschieden sich nicht [@ko2020window]. Das systematische Review zur Aufmerksamkeitserholung findet gemischte Befunde [@ohly2016attention], und die zugrunde liegende Theorie ist umstritten [@joye2018broken; @kaplan1995restorative]. Die Empfehlung „Sichtverbindung nach außen“ ist deshalb B-W. Der Mechanismus wird nicht behauptet. Vom Biophilic Design übernimmt das System nur Muster, die einzeln belegt sind. Das kritische Review von Zhong et al. zeigt, dass die Rahmenwerke heterogen und die Belege je Muster sehr unterschiedlich sind [@zhong2022biophilic]. Die Sternebewertung im Musterkatalog von Terrapin stammt vom Herausgeber selbst [@browning2014patterns].

**Beengtheit.** Evans et al. fanden bei 10- bis 12-jährigen Kindern in Indien, dass chronische Wohnbeengtheit mit Schulproblemen, erlernter Hilflosigkeit und erhöhtem Blutdruck zusammenhängt, auch nach Kontrolle des Einkommens [@evans1998crowding]. Die dortigen Dichten liegen weit über denen eines deutschen Einfamilienhauses. Für den Neubau ist die Regel deshalb vor allem bei knappen Raumprogrammen und im Mehrfamilienhaus relevant (Kapitel 9a). Die Kennzahl „Personen je Raum“ ist trivial zu berechnen, sobald die Haushaltsgröße bekannt ist.

### 9b.3.3 Präferenz: Bettposition und Prospect-Refuge

An diesen Faktoren zeigt sich die Trennung von Wirkung und Präferenz am deutlichsten. Spörrle und Stich ließen 138 Personen Möbel auf experimentell variierten Grundrissen anordnen. Die Teilnehmenden stellten das Bett überwiegend so, dass sie die Tür sehen konnten, möglichst weit von ihr entfernt und auf der Seite, zu der die Tür aufschlägt [@spoerrle2010sleeping]. Bonin et al. replizierten den Befund mit 2D- und 3D-Plänen in Frankreich und der Slowakei. Eine unsichere Bettposition löste in der Vorstellung mehr Unbehagen aus [@bonin2023goodnight]. Beide Arbeiten belegen eine robuste *Vorliebe*. Dass Menschen in dieser Position besser schlafen, ist nicht untersucht.

Die Theorie dahinter, Appletons Prospect-Refuge-Theorie, stammt aus der Landschaftsästhetik [@appleton1975experience; @appleton1984prospects]. Hildebrand übertrug sie interpretierend auf Wohnhäuser [@hildebrand1999origins]. Die empirische Lage für Innenräume ist schwächer, als die Architekturliteratur nahelegt:

- Die Meta-Analyse von Dosen und Ostwald findet für Innen- und Stadträume Unterstützung für Prospect und neutrale Ergebnisse für Refuge. Die Autoren halten die quantitative Evidenz insgesamt für inkonsistent und kritisieren, dass die in der Architektur zitierten Befunde meist aus Landschaftsstudien stammen [@dosen2016prospect]. Eine methodische Analyse von 30 Studien derselben Autoren benennt deren Verzerrungen [@dosen2013methodological].
- Stamps fasste acht Studien mit 144 Personen und 80 Umgebungen zusammen. Nur der Faktor „venue“ (Art der Umgebung) wirkte deutlich (r = 0,42). Die Effekte von Prospect und Refuge lagen nahe null [@stamps2008some]. In zwei Innenraumexperimenten wirkte nur die Raumbreite deutlich auf den Komfort (r = 0,35) [@stamps2006interior].

Die Arbeit stuft Prospect-Refuge im Innenraum deshalb als **C-P** ein, strenger als Recherche 15 (B-P). Die spezifische Bettregel bleibt **B-P**, weil sie in einem eigenen Paradigma repliziert ist. Diese Unterscheidung ist für die Kulturprofile wichtig. Die Feng-Shui-„Kommandoposition“ deckt sich mit der gut replizierten Bettpräferenz, nicht mit einer allgemeinen Wirkungsaussage (9b.6.2).

Für Präferenzregeln gilt eine Besonderheit. Ein Präferenzbefund sagt, was die *meisten* Menschen bevorzugen. Äußert ein Kunde eine eigene, abweichende Vorliebe, ist diese Äußerung für ihn die bessere Evidenz. Das System übernimmt sie deshalb bei P-Regeln ohne Rückfrage und setzt die Regel für diesen Kunden aus. Bei W-Regeln bleibt der Hinweis bestehen, die Entscheidung liegt trotzdem beim Kunden (9b.7.3).

## 9b.4 Rechenbares Grundrisswissen

### 9b.4.1 Das Grundrissmodell als Graph und Geometrie

Die Prädikate der R5-Regeln arbeiten auf zwei Darstellungen, die aus dem IFC-Modell abgeleitet werden (Kapitel 8):

- **Raumgraph** $G = (V, E)$: Knoten sind Räume (`IfcSpace`) und der Außenraum, Kanten sind Türen und offene Durchgänge. Kanten tragen Attribute wie Türbreite und Aufschlagrichtung.
- **Geometrie:** Raumpolygone, Öffnungen mit Flügelgeometrie, Möblierung als Stell- und Bewegungsflächen, Himmelsrichtung über den Nordwinkel des Modellkontexts.

Aus dieser Grundlage stammen fünf Gruppen von Kennzahlen.

### 9b.4.2 Zonierung und Raumbeziehungen

Der Privatheitsgradient wird über den **Justified Graph** ab der Haustür geprüft [@hillier1984social; @hanson1998decoding]. Die Tiefe $d_{ij}$ ist die Zahl der Schritte zwischen Raum $i$ und $j$ im Raumgraphen. Die Kernregeln sind:

- $\bar d(\text{Schlafräume}) > \bar d(\text{Wohnbereich})$, gemessen ab dem Außenraumknoten (C, gestützt durch die Theorie der Privatheitsregulation [@altman1975environment] und Alexanders Muster #127 „Intimacy Gradient“ [@alexander1977pattern]).
- Kein Schlafraum liegt auf einem kürzesten Weg zwischen zwei anderen Räumen (kein Durchgangsraum).
- Das Gäste-WC ist vom Eingang erreichbar, ohne dass der Weg durch einen Schlafraum oder dessen Vorbereich führt.

Raumbeziehungen werden als Graph- und Abstandsprädikate formuliert. Das WBS gibt dafür rechenbare Schwellen (Kriterium K19): Kochen und Essen liegen Mitte zu Mitte weniger als 300 cm auseinander, der Durchgang ist breiter als 120 cm, der Kochbereich liegt an der Fassade mit einem öffenbaren Fenster [@bwo2015wbs]. Funktionsstudien zum Verhältnis von Küche, Essen und Wohnen im deutschen Wohngrundriss liefern den Kontext [@faller2002wohngrundriss].

Die **Anpassbarkeit** eines Grundrisses lässt sich ebenfalls am Graphen messen. SAGA quantifiziert mit gewichteten Graphen und fünf Kennzahlen, wie gut ein Grundriss Veränderungen trägt, ist aber nur an sechs Layouts illustriert [@herthogs2019saga]. Eine Studie an 313 von ihren Eigentümern umgebauten schwedischen Wohnungen fand, dass die Größe des Wohnraums und die Zersplitterung des Ausgangsgrundrisses mit Umbauten zusammenhängen [@femenias2020adaptable]. Beide stützen eine C-Regel zur Anpassbarkeit, etwa ein Kinderzimmer, das sich später teilen oder zusammenlegen lässt.

### 9b.4.3 Himmelsrichtung

Die Faustregel „Wohnen nach Süden und Westen, Schlafen nach Osten und Norden“ hat keine eigene Wirkungsstudie. Ihre Quellen sind Alexanders Muster #138 „Sleeping to the East“ [@alexander1977pattern], die Orientierungsschemata der Bauentwurfslehre [@neufert2022bauentwurfslehre] und die Besonnungsempfehlungen [@din2019tageslicht]. Mechanistisch plausibel ist sie über das Morgenlicht [@brown2022recommendations] und über die sommerliche Überhitzung westorientierter Räume [@emmitt2023bedroom]. Sie wird als **C, mechanistisch gestützt durch B** ausgewiesen.

Als harte Zählregel formuliert das WBS unter K24, dass mindestens 50 % der Fenster aller Zimmer nicht in einem Sektor von ±60° um Nord liegen (Recherche 15) [V]. Rechnerisch ist das ein Winkeltest auf der Fensternormalen:

$$\text{nordorientiert}(f) \iff |\,\alpha_f - 0^\circ\,| \le 60^\circ,$$

mit $\alpha_f$ als Azimut der Außennormalen des Fensters $f$, bezogen auf geografisch Nord. Die Regel setzt voraus, dass der Nordwinkel im Modell gesetzt ist. Fehlt er, ist sie „nicht bewertbar“ (9b.1.1).

### 9b.4.4 Möblierbarkeit und Stauraum

Möblierbarkeit ist der Faktor, bei dem Laien am häufigsten scheitern und der am besten rechenbar ist. Eine Analyse spekulativ gebauter Neubauhäuser in Großbritannien untersuchte deren Funktionalität bei Möblierung und Raumgrößen; sie ist nur nach Titel eingeordnet [@west2004functional]. Das WBS-Kriterium K18 liefert einen direkt implementierbaren Algorithmus [@bwo2015wbs] (Recherche 15) [V]:

1. Je Zimmer werden alle Stellungen eines Bettmoduls gesucht (Doppelbett ab 12 m², Einzelbett ab 10 m²), bei denen mindestens das Kopfende eine Wand berührt.
2. Eine Stellung ist gültig, wenn kein Tür- oder Fensterflügel bei 90° Öffnung in die Bettfläche ragt.
3. Die gültigen Stellungen werden je Zimmer gezählt und über alle Zimmer gemittelt.
4. Zusatzpunkte gibt es, wenn in allen Zimmern ein Doppelbett möglich ist, bei mindestens 5 m² zusätzlicher Fläche und bei einer Wendefläche von 140 × 170 cm am Bett.

Der Algorithmus ist eine diskrete Suche über Wandsegmente und Orientierungen. Für ein Zimmer mit $n$ Wandsegmenten und zwei Orientierungen je Segment ist der Aufwand linear in $n$ mal der Zahl der Kollisionsprüfungen mit Flügeln. Die Bettregel aus 9b.3.3 lässt sich auf dieselbe Menge der gültigen Stellungen anwenden. Das System sucht dann unter den möblierbaren Stellungen die, von denen aus die Tür sichtbar ist.

Für die übrigen Stell- und Bewegungsflächen gibt es in Deutschland keine geltende Norm mehr. DIN 18011 ist zurückgezogen und galt schon 1990 als ungeeignet für Mindestgrößen (Recherche 13) [V]. Ihre Werte dienen als Startheuristik: Bewegungsfläche zwischen Stellfläche und Wand mindestens 70 cm, Eingangsflur mindestens 130 cm, Nebenflur mindestens 90 cm. Präzisere Maße liefern die Bauentwurfslehre [@neufert2022bauentwurfslehre], für die Küche die Branchenempfehlung von mindestens 120 cm Bewegungsfläche vor der Zeile und für die Barrierefreiheit DIN 18040-2 (Recherche 13). Alle diese Werte sind Grad C. Der Constraint-basierte Möbelkritiker von Oh et al. zeigt, wie sich die Rückmeldung dazu nach dem Wissensstand des Nutzers abstufen lässt [@oh2010furniture].

Der **Stauraum** folgt WBS K21: Ein Schrankmodul von 60 × 60 × 180 cm braucht 90 cm Bedienfläche, im Kochbereich 120 cm. Zusatzpunkte gibt es für einen weiteren Einbauschrank von mindestens 120 cm Breite, einen separaten Abstellraum und Stauraum außen oder in der Zwischenzone [@bwo2015wbs]. Dass Stauraum für Bewohner zählt, zeigt eine explorative Studie, die ihn unter sechs gewünschten Raumatmosphären fand. Das ist ein Präferenzbefund [@graham2015psychology].

### 9b.4.5 Verkehrsfläche

Der Verkehrsflächenanteil ist nach DIN 277 als Verhältnis von Verkehrsfläche zu Nutzungsfläche definiert (Kapitel 9a). Einen belegten Zielwert für Einfamilienhäuser hat die Recherche nicht gefunden [U]. Das System weist den Anteil deshalb nicht als Grenzwert aus, sondern relativ: als Perzentil gegenüber einem Referenzsatz. Kalibriersätze sind die rund 160 Referenzgrundrisse des Grundrissatlas [@heckmann2017grundrissatlas], die überwiegend aus dem Geschosswohnungsbau stammen, und langfristig der Katalog des Herstellers. Ein Hinweis erscheint erst, wenn der Anteil über dem 90. Perzentil des Referenzsatzes liegt (Designentscheidung).

### 9b.4.6 Space Syntax und Isovisten

Für Zonierung und Orientierung stellt Space Syntax etablierte Konfigurationsmaße bereit [@hillier1984social; @bafna2003space]. Mit $k$ Knoten und der Tiefe $d_{ij}$ gilt für Raum $i$:

$$\mathrm{MD}_i = \frac{\sum_{j \neq i} d_{ij}}{k-1}, \qquad \mathrm{RA}_i = \frac{2(\mathrm{MD}_i - 1)}{k-2}, \qquad \mathrm{RRA}_i = \frac{\mathrm{RA}_i}{D_k}.$$

$D_k$ ist der Normierungswert eines rautenförmigen Referenzgraphen gleicher Knotenzahl. Die Integration ist der Kehrwert von $\mathrm{RRA}_i$. Ostwald hat die Definitionen mathematisch revidiert und die Methode kritisch aufgearbeitet [@ostwald2011mathematics]. Seine Fassung dient als Implementierungsgrundlage. Einfamilienhäuser haben nur etwa 8 bis 15 Knoten, und die Normierung reagiert bei so kleinen Graphen empfindlich. Das System zeigt deshalb vor allem Tiefe und Rangfolge der Räume und nutzt RRA nur zum Vergleich von Varianten mit gleicher Knotenzahl (Designentscheidung).

Das **Isovist** ist die Menge aller Punkte, die von einem Standpunkt aus sichtbar sind. Benedikt schlug dafür Größen- und Formmaße vor und nannte als Anwendungsfelder Blickkontrolle, Privatheit und Weite [@benedikt1979take]. Turner et al. bauten daraus den Sichtbarkeitsgraphen, dessen lokale und globale Kennzahlen Zugänglichkeit und Sichtbarkeit einer Konfiguration beschreiben [@turner2001isovists]. In 16 virtuellen Innenräumen korrelierten wenige Isovistenmaße stark mit Navigationsverhalten und Raumerleben [@wiener2007isovist]. Ob einfache Raumgefühle wie Enge und Offenheit mit Isovistenmaßen korrelieren, prüften Dosen und Ostwald mit 159 Personen an 24 virtuellen Innenräumen [@dosen2017lived]. Ihr Ergebnis ist im vorliegenden Abstract nicht enthalten. Die Arbeit stützt sich darauf deshalb nicht.

Im System werden zwei Isovistenmaße verwendet:

- **Isovistenfläche** $A(p)$ am Nutzungsort $p$ (Sofa, Essplatz, Schreibtisch) als Maß für Überblick.
- **Zugang sichtbar:** boolesch, ob die Türöffnung des Raums in $A(p)$ liegt.

Ein ähnliches Verfahren hat Hwang für Fensteralternativen vorgeschlagen, ohne Nutzerstudie [@hwang2018window]. Dawes und Ostwald analysierten mit Isovisten die Prospect-Refuge-Eigenschaften von Wohnhäusern Frank Lloyd Wrights (nach Titel eingeordnet) [@dawes2014wright]. Beide Arbeiten sind Methodenbeispiele, keine Wirkungsbelege. Die Isovistenmaße tragen deshalb C- und P-Regeln, keine W-Regeln.

### 9b.4.7 Alexander-Muster als Planungswissen

*A Pattern Language* ist eine reiche Quelle für Entwurfsregeln. Nur ein kleiner Teil der 253 Muster ist aber empirisch geprüft, und die Kritik bemängelt fehlende Prüfung und Überprüfbarkeit [@dawes2017pattern]. Die Muster werden deshalb einzeln bewertet und nur übernommen, wenn ein Prädikat möglich ist:

| Muster | Prädikat im System | Grad |
|---|---|---|
| #127 Intimacy Gradient | Tiefenordnung im Justified Graph | C, gestützt durch Privatheitstheorie |
| #138 Sleeping to the East | Azimut der Schlafraumfenster | C, mechanistisch B |
| #159 Light on Two Sides | Aufenthaltsräume mit Fenstern an zwei Fassaden | C [U] |
| #179 Alcoves, #180 Window Place | Nischen, Sitzplatz am Fenster mit Wand im Rücken | C-P (Prospect-Refuge) |
| #190 Ceiling Height Variety | Varianz der lichten Höhe im Wohnbereich | B-P [@vartanian2015ceiling] |
| #112 Entrance Transition | Windfang oder Zwischenzone vor dem Wohnbereich | C (≈ WBS K24) |

## 9b.5 Wohnqualitäts-Scoring: Profil statt Gesamtscore

### 9b.5.1 Das Schweizer Wohnungs-Bewertungs-System

Das Wohnungs-Bewertungs-System (WBS) des Schweizer Bundesamts für Wohnungswesen ist das einzige gefundene Bewertungssystem, das Wohnqualität weitgehend rechenbar macht [@bwo2015wbs]. Die Ausgabe 2015 hat 25 Kriterien in drei Bereichen: Wohnstandort, Wohnanlage und Wohnung. Jedes Kriterium bringt höchstens 4 Punkte, zusammen 100 Punkte, dazu höchstens 5 Innovationspunkte. Das Ergebnis wird als Netzdiagramm dargestellt. Das WBS setzt eine Grundausstattung je Wohnungsgröße voraus und bewertet Gebrauchswert und Nutzungsflexibilität, nicht Gesundheit. Seine Kriterien sind deshalb durchgehend Grad C.

Für Einfamilienhäuser sind die Wohnungskriterien übertragbar. Die Arbeit implementiert daraus ein **WBS-lite** und kennzeichnet es als eigene Adaption, nicht als offizielle WBS-Bewertung. Die Schweizer Verweise auf SIA 500 werden durch DIN 18040-2 ersetzt. Die Punktelogik der Kriterien K15 bis K17, K22 und K23 konnte am Original nicht vollständig nachgelesen werden (Recherche 15, offener Punkt 1) [U]. Für diese Kriterien steht in der folgenden Tabelle eine eigene Operationalisierung.

| WBS-Kriterium | geometrisch prüfbar als | Quelle der Prüflogik |
|---|---|---|
| K15 Nettowohnfläche | Fläche je Person gegen Haushaltsgröße | eigene Operationalisierung [U] |
| K16 Zimmergröße | Anteil der Zimmer ≥ 10 bzw. ≥ 12 m² | Schwellen aus K18; Rest [U] |
| K17 vielfältige Nutzbarkeit | Zahl der Zimmer mit ≥ 2 Möblierungsvarianten (Bett, Arbeitsplatz) | eigene Operationalisierung [U] |
| K18 Möblierbarkeit | Bettmodul-Algorithmus (9b.4.4) | WBS [V] |
| K19 Koch- und Essbereich | Abstand < 300 cm, Durchgang > 120 cm, Fenster am Kochbereich | WBS [V] |
| K20 Sanitär | Bewegungsflächen nach DIN 18040-2 statt SIA 500 | WBS [V], Ersatz eigene Adaption |
| K21 Abstellbereich | Schrankmodule, Reduit, Außenstauraum | WBS [V] |
| K22 Anpassungsfähigkeit | teilbare oder zusammenlegbare Räume, Graphmaße nach SAGA | eigene Operationalisierung [U] |
| K23 privater Außenbereich | Fläche und Direktzugang von Wohnraum oder Küche | eigene Operationalisierung [U] |
| K24 Übergänge innen/außen | Zwischenzone am Eingang, Öffentlichkeitsgrade, Nordanteil der Fenster ≤ 50 % | WBS [V] |

### 9b.5.2 Andere Bewertungssysteme

Drei deutsche und internationale Systeme ergänzen das WBS, ohne es zu ersetzen:

- **DGNB:** Die Kriterien SOC1.1 bis SOC1.6 decken thermischen, visuellen und akustischen Komfort, Innenraumluft und Aufenthaltsqualität ab [@dgnb2023soc]. Die Gewichtung von 4,2 % je Kriterium für Wohngebäude ist unsicher [U]. Die Zertifizierungslogik passt eher zum Mehrfamilienhaus.
- **QNG:** Anhang 313 der Anlage 3 regelt die Schadstoffvermeidung in Baumaterialien [@qng2023anlage3]. Er ist die evidenzbasierte Brücke zur Baubiologie (9b.6.4).
- **WELL v2:** Die Lichtmerkmale und die Mind-Features dienen nur als Ideengeber, weil das System auf Büros ausgelegt ist [@iwbi2020wellv2]. Die Nummern der Merkmale sind nicht geprüft [U].

International zeigt der Design Quality Indicator, wie wahrgenommene Entwurfsqualität mit Rahmen, Erhebungswerkzeug und Gewichtung erfasst werden kann [@gann2003design]. Ein neuer Rahmen für Wohnqualität im Mehrfamilienhausbau leitet aus 2.536 Indikatoren über Clusterung, eine AHP-Gewichtung durch 51 Architekten und eine Befragung von 411 Bewohnern sieben Kriterien mit 21 Indikatoren ab. Lüftung und Tageslicht erhielten die höchsten Gewichte [@rewatkar2026data]. Beide Arbeiten stammen aus anderen Kontexten und bestätigen vor allem, dass Tageslicht in der Gewichtung vorn liegt. Stefani und Cajochen schlagen einen mehrstufigen, evidenzbasierten Score für integrative Beleuchtung vor, der nicht validiert ist; das Abstract lag nicht vor [@stefani2024evidencebased].

### 9b.5.3 Profil und Pareto-Vergleich

Das System zeigt keinen Gesamtscore. Es gibt drei Gründe.

1. **Ein Gesamtwert verdeckt Zielkonflikte.** Ein Schlafzimmer mit großer Westverglasung zum Garten kann im Außenbezug gut und im Raumklima schlecht abschneiden. Eine Summe mittelt beides zu „durchschnittlich“ und nimmt dem Kunden die Information, die er für die Abwägung braucht.
2. **Ein Gesamtwert lädt dazu ein, auf die Kennzahl zu optimieren statt auf Qualität.** Das ist der aus der Ökonomie bekannte Goodhart-Effekt. Er ist hier Designbegründung, kein empirischer Befund dieser Arbeit.
3. **Die Gewichte sind nicht kalibriert.** Solange $g$ und $u_d$ Designentscheidungen sind (9b.1.3), wäre eine Summe eine Scheingenauigkeit.

Stattdessen gibt es ein **Profil mit sechs Dimensionen**, dargestellt wie das WBS-Netzdiagramm:

| Dimension | typische Regeln |
|---|---|
| Licht | Tageslicht, Besonnung, zirkadianes Licht, Verdunkelung |
| Ruhe und Privatheit | ruhige Seite, Privatheitsgradient, Rückzugsorte |
| Raumklima und Innenraumluft | sommerliche Überhitzung, schadstoffarme Materialien |
| Funktion und Möblierbarkeit | K18, K19, K21, Verkehrsfläche, Bettposition |
| Außenbezug | Sichtverbindung, Grün im Sichtkegel, privater Außenbereich |
| Anpassbarkeit und Barrierearmut | K22, Profil „barrierefrei vorbereitet“ |

Wenn der Kunde Varianten vergleicht, bestimmt das System die **Pareto-Menge**. Eine Variante $x$ dominiert $y$, wenn

$$x \succ y \iff \forall d:\ S_d(x) \ge S_d(y)\ \wedge\ \exists d:\ S_d(x) > S_d(y).$$

Dominierte Varianten werden ausgeblendet oder als solche markiert. Für die nicht dominierten zeigt das System eine Vergleichsmatrix. Häubl und Trifts zeigten in einem kontrollierten Experiment zum Onlinekauf, dass ein Empfehlungsagent zusammen mit einer Vergleichsmatrix den Suchaufwand senkt und die Entscheidungsqualität verbessert [@haubl2000decisionaids]. Der Kontext ist Konsumgüterkauf, nicht Hausentwurf. Die Übertragung ist deshalb eine Hypothese, die in Kapitel 20 geprüft wird.

### 9b.5.4 Kalibrierung durch Bewohnerbefragung

Die Gewichte sind die schwächste Stelle des Scorings. Preiser et al. unterscheiden für die Post-Occupancy Evaluation drei Ebenen: indikativ, investigativ und diagnostisch [@preiser1988poe]. Die Arbeit schlägt eine indikative Befragung 12 bis 24 Monate nach Einzug vor. Walden hat mit dem Koblenzer Architekturfragebogen ein deutschsprachiges Instrument für Schulen und Büros entwickelt, dessen Konstrukt „Umweltkontrolle“ übertragbar ist [@walden2008architekturpsychologie]. Die Befragung liefert zwei Ergebnisse. Sie kalibriert $g$ und $u_d$ am realen Bestand, und sie ist ein eigener empirischer Beitrag. Bis dahin gilt die Assistenz nicht als „bewiesen gut“.

## 9b.6 Kulturprofile

### 9b.6.1 Grundsatz

Kulturprofile sind **nur auf Wunsch aktiv**. Ein aktives Profil hat einen eigenen Teilscore $K_p$, der nie in das Wohnqualitätsprofil einfließt. Jede Regel trägt die Kennzeichnung „traditionelle Lehre“, und die Überschneidungen mit evidenzbasierten Faktoren werden ausgewiesen. So sieht der Kunde, wo Tradition und Forschung übereinstimmen und wo sie sich widersprechen.

Dass das Profil nur auf Wunsch erscheint, hat einen empirischen Grund. In einer Befragung von 246 Bewohnern Taipehs stieg die Sorge um Feng Shui mit dem Aberglauben und sank mit der Selbstwirksamkeit [@peng2012concern]. Ein ungefragt eingeblendetes Feng-Shui-Urteil würde also gerade die Menschen verunsichern, die dafür empfänglich sind. Flade führt Feng Shui in ihrer Wohnpsychologie als Trendthema [@flade2006wohnen].

### 9b.6.2 Feng Shui

Feng Shui hat zwei Hauptschulen. Die **Formschule** beurteilt Landschafts- und Gebäudeform, etwa das „Lehnstuhl“-Ideal mit Rückendeckung und offener Vorderseite. Die **Kompassschule** arbeitet mit Bagua, Luopan, der aus dem Geburtsdatum berechneten Kua-Zahl und den Fliegenden Sternen. Eine Befragung von Architekten in Hongkong ergab, dass sie Prinzipien der Formschule oft ohnehin befolgen und diese für eher rational analysierbar halten [@mak2005fengshui]. Das ist Wahrnehmungsforschung, keine Wirkungsforschung.

Geometrisch prüfbar sind vor allem Regeln der Formschule:

| Regel (nach der Lehre) | Prädikat | Grad | Überschneidung mit Evidenz |
|---|---|---|---|
| Bett in „Kommandoposition“, nicht mit den Füßen zur Tür | Tür vom Kopfkissen sichtbar, Bettachse nicht in Flucht mit der Türachse | D; Überschneidung B-P | Bettposition [@spoerrle2010sleeping; @bonin2023goodnight]; eine Diagonalstellung erfüllt beide |
| Schreibtisch mit Wand im Rücken, Blick zur Tür | Rückwandabstand ≤ Parameter, Tür im Isovist | D; Überschneidung C-P | Prospect-Refuge [@dosen2016prospect] |
| Haustür nicht in Flucht mit Hintertür oder großem Fenster | Gerade ab Haustür trifft ungehindert auf eine Außenöffnung | D | teilweise: Windfang, Einblick, Privatheit (C) |
| Treppe nicht direkt gegenüber der Haustür | Treppenantritt in der Sichtachse ab Eingang innerhalb eines Abstands | D | **Konflikt:** Space Syntax wertet die Sichtbarkeit der Treppe für die Orientierung positiv (C) |
| WC nicht im Zentrum, nicht gegenüber Küche oder Haustür | Hüllflächenzentrum nicht im WC; Sichtlinie WC–Küche bzw. Eingang | D | teilweise: Geruch, Privatheit (C) |
| Bagua-Raster, „fehlende Ecken“ | 3 × 3-Raster über dem umschreibenden Rechteck, Flächenanteil je Feld unter Schwelle | D | keine |
| keine „Giftpfeile“ auf Sitz- oder Schlafplatz | Außenecke zeigt in kurzem Abstand auf einen Nutzungsort | D | schwach: Kurvenpräferenz (B-P) [@chuquichambi2022curvature] |

Die Wirkung von Feng Shui ist **D**. Die Arbeit hat keine methodisch belastbare Studie gefunden, die Wirkungen über die genannten Überschneidungen hinaus zeigt. Eine Studie prüfte das direkt: In einer Befragung in Malaysia (N = 405) wurde ein nach der Formschule gestaltetes Schlafzimmer deutlich bevorzugt, aber es ging nicht mit besserer subjektiver Schlafqualität einher [@hong2016fengshui]. Das ist dasselbe Muster wie bei der Bettposition: Präferenz ja, Wirkung nicht belegt.

Belegt ist dagegen eine **Marktwirkung** (B-M) in Märkten mit hohem chinesischstämmigem Käuferanteil:

- Vancouver, rund 117.000 Verkäufe: Häuser mit einer 4 am Ende der Hausnummer wurden 2,2 % billiger, mit einer 8 um 2,5 % teurer verkauft, vor allem in Vierteln mit hohem chinesischem Bevölkerungsanteil [@fortin2014superstition].
- Auckland: Glückszahlen bei Hausnummern sind preiswirksam [@bourassa1999hedonic].
- Taiwan, 77.624 Beobachtungen: sechs Formen „schlechten Feng Shuis“ senken die Preise [@lin2012fengshui].
- Hongkong: frühe Studie zu Grundstücks- und Projektentwicklung [@tam1999fengshui]; 622 Transaktionen mit einem Abschlag von 6,45 % bei Ausrichtung auf „Sha Qi“ [@prpj2022fengshui].

Diese Studien zeigen Zahlungsbereitschaft, nicht Wirkung. Für Bayern sind sie nicht übertragbar, und Hausnummern sind kein Entwurfsgegenstand.

**Marktrelevanz in Deutschland.** Ein deutscher Fertighaushersteller bietet „Hausbau nach Feng Shui“ mit Referenzhaus an. Für Baufritz und Regnauer hat die Recherche kein Feng-Shui-Angebot gefunden, beide positionieren sich über Baubiologie und Wohngesundheit (Recherche 15) [V]. Freie Berater nennen für eine Komplettauswertung eines Neubaus etwa 3.750 € netto [V]. Zahlen zur Nachfrage fehlen [U]. Feng Shui ist in Deutschland eine Nische. Die Nachfrage wäre per Kundenbefragung bei den Herstellern zu erheben.

### 9b.6.3 Vastu Shastra

Vastu legt ein Vastu-Purusha-Mandala als Raster aus 8 × 8 oder 9 × 9 Feldern über Grundstück oder Haus. Das Zentrum (Brahmasthan) bleibt frei. Der Eingang liegt bevorzugt im Osten, Norden oder Nordosten, die Küche im Südosten, das Hauptschlafzimmer im Südwesten, der Andachtsraum im Nordosten, und im Nordosten liegt kein WC. Die Regelvarianten unterscheiden sich je Schule und Text. Die Zusammenfassung folgt der Sekundärliteratur [U].

Geometrisch ist Vastu so einfach prüfbar wie das Bagua: Rasterüberlagerung und Zuordnung von Raumtyp zu Himmelsrichtung. Die Evidenz ist **D**. Chakrabarti analysiert die heutige Vastu-Praxis und ihre Schulen kulturhistorisch [@chakrabarti1998vastu]. Patra argumentiert, Vastu sei mit nachhaltiger Entwicklung vereinbar, prüft das aber nicht empirisch [@patra2009vaastu].

Bei 48 bis 54° nördlicher Breite entsteht ein offener **Zielkonflikt**. Ein Schlafzimmer im Südwesten bekommt Nachmittags- und Abendsonne und damit ein Überhitzungsrisiko. Das widerspricht dem thermischen Komfort (B-W, Nachweis N nach DIN 4108-2 [@din4108-2]) und der Ost-Schlaf-Regel (C). Das System verschweigt diesen Konflikt nicht und löst ihn nicht selbst auf. Es zeigt ihn und schlägt Maßnahmen vor, die beiden Zielen dienen, etwa außenliegenden Sonnenschutz. Die Marktrelevanz in Deutschland ist eine Nische, Zahlen fehlen [U].

### 9b.6.4 Baubiologie

Die Baubiologie ist für den deutschen Holzfertighausmarkt das wichtigste Kulturprofil, weil Hersteller mit Wohngesundheit werben. Ihre Quellen sind die 25 Leitlinien des IBN in fünf Kategorien [@ibn2018leitlinien] und der Standard der baubiologischen Messtechnik SBM-2024 [@maes2024sbm]. Der Standard gliedert sich in Felder, Wellen und Strahlung (A1 bis A7), Wohngifte (B) sowie Pilze, Bakterien und Allergene (C). Seine Richtwerte für Schlafbereiche sind vorsorglich formuliert und nicht gesundheitsbasiert abgeleitet. Teil A7 führt „geologische Störungen“ einschließlich „Erdstrahlung“.

Anders als Feng Shui und Vastu zerfällt die Baubiologie in einen evidenzbasierten und einen nicht belegten Teil:

| baubiologischer Punkt | Grad | Behandlung im System |
|---|---|---|
| Radon | A-W, Status N | Referenzwert 300 Bq/m³ nach §§ 124, 126 StrlSchG [@bfs2025radon]; Grundstück im Radonvorsorgegebiet → radonsichere Bodenplatte als Regel, Messhinweis |
| Formaldehyd, VOC | A/B-W | Richtwert des Ausschusses für Innenraumrichtwerte für Formaldehyd 0,1 mg/m³ [@air2016formaldehyd]; Materialwahl nach QNG Anhang 313 [@qng2023anlage3] |
| Feuchte, Schimmel | Feuchteschutz N; Wirkungsgrad [U] | Feuchteschutz und Lüftungskonzept nach DIN 1946-6 [@din1946-6]; die WHO-Leitlinie zur Innenraumfeuchte ist nicht Teil der Literaturbasis |
| Tageslicht, Raumakustik, flimmerfreies Licht | B/C | deckungsgleich mit den Wirkfaktoren in 9b.3 |
| „harmonische Proportionen“, regionale Baukultur | C/D | nur Gestaltungshinweis |
| NF/HF-Felder unterhalb der Grenzwerte | C [U] | nur Komfortoption (Netzfreischalter, Leitungen nicht am Bett) mit dem Hinweis „vorsorglich, kein Gesundheitsnutzen belegt“; Werbeaussagen zu Elektrosmog-Schutz werden nicht übernommen |
| Erdstrahlen, Wasseradern, Globalgitter, Wünschelrute | **X** | nicht angeboten (9b.6.5) |

Das System bildet damit die evidenzbasierte Hälfte der Baubiologie über QNG und Strahlenschutzrecht ab, ohne die esoterische Hälfte zu übernehmen. Für Hersteller, die mit Wohngesundheit werben, ist das zugleich ein Schutz. Die belegten Punkte lassen sich mit Quelle vertreten, die unbelegten werden nicht als Leistung ausgewiesen.

### 9b.6.5 Ausschlussliste

Die Ausschlussliste enthält Aussagen, die geprüft wurden und ohne Befund blieben. Sie werden nicht bewertet und nicht als Regel angeboten. Fragt ein Kunde danach, erklärt das System, warum.

- **Wünschelrute, „Wasseradern“, „Erdstrahlen“, Globalgitter.** Die vom damaligen Bundesforschungsministerium finanzierten Scheunenversuche mit rund 500 Rutengängern ergaben in der Nachanalyse von Enright keinen Nachweis (Recherche 15) [@enright1995dowsing]. Ein Abstract lag nicht vor. Die Aussage stützt sich auf Recherche und Bewertung. Hinzu kommt ein hydrogeologisches Argument: Grundwasser fließt meist flächig, nicht in Adern. Dass SBM-2024 den Punkt unter A7 führt [@maes2024sbm], ändert die Einstufung nicht. Der Standard ist Gegenstand der Abgrenzung, kein Beleg.

Die Liste ist bewusst kurz. Grad X ist Aussagen vorbehalten, die empirisch geprüft wurden. Aussagen, die einfach nicht untersucht sind, bleiben D. So wird verhindert, dass die Ausschlussliste zu einem Werkzeug wird, mit dem Traditionen pauschal abgewertet werden.

### 9b.6.6 Stilprofile und Überschneidungen

Wabi-Sabi ist ein ästhetisches Leitbild aus Unvollkommenheit, Patina und natürlichen Materialien, kein Regelwerk [@koren1994wabisabi]. Hygge beschreibt die Anthropologie als soziale Praxis mit egalitären Normen und auch mit Ausgrenzung, nicht als Einrichtungsrezept [@linnet2011hygge]. Beide werden als **Stilprofile** geführt, die Materialien, Lichtfarben und Nischen vorschlagen, ohne Gesundheitsversprechen (D). Linnets Befund ist zugleich eine Warnung. Kulturprofile dürfen nicht auf Stilregeln aus Ratgeberbüchern reduziert werden.

Die Überschneidungen aller Kulturprofile mit den evidenzbasierten Faktoren fasst die folgende Matrix zusammen. Sie ist die Grundlage der Erklärtexte, wenn ein Profil aktiv ist.

| Kulturregel | evidenzbasierter Faktor | Verhältnis |
|---|---|---|
| Feng Shui: Kommandoposition des Betts | Bettposition (B-P) | Deckung |
| Feng Shui: Schreibtisch mit Rückendeckung | Prospect-Refuge (C-P) | Teildeckung |
| Feng Shui: keine Flucht Haustür–Hintertür | Windfang, Privatheit (C) | Teildeckung |
| Feng Shui: Treppe nicht gegenüber Haustür | Orientierung, Space Syntax (C) | Konflikt |
| Feng Shui: Bagua, fehlende Ecken | – | keine |
| Vastu: Hauptschlafzimmer im Südwesten | thermischer Komfort (B-W, N), Ost-Schlaf (C) | Konflikt |
| Vastu: Zentrum frei | – | keine |
| Baubiologie: Radon, Schadstoffe | StrlSchG, QNG (A, N) | Deckung |
| Baubiologie: Erdstrahlen | – | Ausschluss (X) |
| Hygge: warmes, schwaches Abendlicht | ≤ 10 lx mEDI am Abend (B-W) | Deckung |
| Hygge: Nischen, Ofenplatz | Refuge (C-P) | Teildeckung |

## 9b.7 Assistenz-Architektur und Ethik

### 9b.7.1 Schichten

Die Assistenz hat vier Schichten und eine Ausschlussliste:

1. **Harte Regeln (Status N):** Recht, Norm, Herstellerregel (R1–R4). Sie blockieren, der Kunde kann sie nicht übergehen.
2. **Evidenzbasierte Empfehlungen (A, B):** standardmäßig aktiv, hohes Gewicht.
3. **Planungswissen (C):** WBS-lite, Bauentwurfslehre, ausgewählte Alexander-Muster, Space Syntax. Standardmäßig aktiv, mittleres Gewicht.
4. **Kulturprofile (D):** nur auf Wunsch, eigener Teilscore, eigene Farbe.
5. **Ausschlussliste (X):** wird nicht bewertet, nur auf Nachfrage erklärt.

### 9b.7.2 Critiquing statt Autopilot

Das Muster der Assistenz ist **Critiquing**. Fischer et al. beschreiben kooperative Problemlösungssysteme, die Nutzern helfen, Lösungen selbst zu entwerfen, statt sie für sie zu entwerfen. Kritiker lassen das entstehende Artefakt „zurücksprechen“ und sind in eine Entwurfsumgebung mit argumentativem Hypertext, Spezifikation und Katalog eingebettet. Lernen entsteht als Nebenprodukt des Problemlösens [@fischer1991critiquing]. Das Vorbild war die Küchenplanung mit JANUS und dem Kritiker CRACK [@fischer1989environments]. Die von Fischer et al. genannten Teilprozesse lassen sich direkt auf Komponenten des Systems abbilden:

| Teilprozess nach Fischer et al. 1991 | Komponente im System |
|---|---|
| Zielerfassung (goal acquisition) | Nutzerprofile (Homeoffice, Kinder, barrierefrei vorbereitet), Kulturprofil, Umgewichtung $u_d$ |
| Produktanalyse | Auswertung der R5-Prädikate am Modell |
| Kritikstrategien | Zeitpunkt und Dichte der Hinweise (s. u.) |
| Anpassungsfähigkeit | Aussetzen von P-Regeln bei abweichender Vorliebe, Wissensstand des Nutzers |
| Erklärung und Argumentation | Laien- und Fachtext, Quelle, Evidenzgrad, Konflikte |
| Beratung (advisory capability) | Alternativvorschlag, der alle harten Regeln erfüllt |

Drei Befunde bestimmen die Kritikstrategie:

- **Zeitpunkt.** Silverman berichtet aus dem Ingenieurentwurf, dass nachträgliche Stapelkritik Nutzer frustriert. Kritik sollte während des Entwerfens kommen [@silverman1992expert; @silverman1992critiquing]. Fischer et al. betten Kritiker deshalb so ein, dass sie früh auf Probleme hinweisen [@fischer1993critics]. Der Hinweis erscheint an der Entscheidungsstelle: Wer ein Bett platziert, bekommt die Bettregel, nicht am Ende eine Mängelliste.
- **Form.** Oh et al. unterscheiden Arten der Kritik (Interpretation, Erinnerung, Beispiel, Demonstration, Bewertung) und Modalitäten (Text, grafische Annotation, Bild) und wählen sie nach Wissensstand und Interaktionsverlauf [@oh2010furniture; @oh2008critiquing]. Ali et al. ordnen solche Kritiker in einer Taxonomie [@ali2013critiquing]. Im System ist die Standardform eine grafische Annotation im Grundriss mit einem Satz Text. Die Begründung öffnet sich auf Nachfrage.
- **Dichte.** Höchstens zwei bis drei Hinweise je Entwurfsschritt, damit Nutzer nicht abstumpfen (Designentscheidung, in der Nutzerstudie zu prüfen).

Oxmans Modell des Entwerfens aus Präzedenzfällen ergänzt das [@oxman1990prior]. Das System zeigt Referenzgrundrisse aus dem Grundrissatlas als Beispiele, die eine Regel gut erfüllen. Dass dialogische Kritik mit Reparaturvorschlägen einem statischen Prüfer überlegen sein kann, zeigen zwei kontrollierte Studien (N = 48) mit LLM-Agenten im UI-Design [@chen2026critiquecrew]. Der Befund stammt aus einer anderen Domäne und stützt die Richtung, nicht die Übertragbarkeit.

### 9b.7.3 Erklärungen

Gute Erklärungen sind nach Millers Übersicht aus den Sozialwissenschaften kontrastiv, selektiv und sozial [@miller2019explanation]. Menschen fragen nicht „Warum Ost?“, sondern „Warum Ost und nicht West?“. Sie wollen wenige Gründe, nicht alle. Das System beantwortet deshalb Kontrastfragen und nennt höchstens drei Gründe, jeweils mit Quelle und Evidenzgrad. Gregor und Benbasat fanden in ihrer Übersicht, dass Erklärungen Leistung, Lernen und Vertrauen verbessern, wenn sie automatisch, kontextspezifisch und mit Begründung angeboten werden [@gregor1999explanations]. In einem Laborexperiment mit einem Empfehlungsagenten stärkten Wie-, Warum- und Abwägungserklärungen jeweils unterschiedliche Vertrauensüberzeugungen (Kompetenz, Wohlwollen, Integrität) [@wang2007recommendation]. Die Abwägungserklärung ist für R5 am wichtigsten, weil fast jede Empfehlung einen Preis hat: Fläche, Kosten oder einen anderen Wunsch.

Die Erklärtexte werden aus dem Regeldatensatz erzeugt, nicht frei von einem Sprachmodell formuliert. Das hat einen konkreten Grund. In einem Online-Experiment (N = 1.506) verschob ein meinungsgeprägter LLM-Schreibassistent nicht nur, was die Teilnehmenden schrieben, sondern auch ihre später erhobene Einstellung [@jakesch2023cowriting]. Ein Sprachmodell, das Empfehlungen frei formuliert, könnte Wertungen einführen, die weder in der Regel noch in der Evidenz stehen. Das entspricht dem Architekturprinzip der Arbeit: Die KI versteht, der Code entscheidet (Kapitel 7). Die Sprachschnittstelle erkennt die Absicht des Kunden. Die Empfehlung und ihre Begründung stammen aus dem versionierten Regelwerk.

### 9b.7.4 Nudging und seine Grenzen

Choice Architecture nach Thaler und Sunstein legitimiert sichtbare Voreinstellungen [@thaler2008nudge]. Johnson et al. katalogisieren die Werkzeuge: Voreinstellungen, Zahl und Struktur der Optionen, Beschreibung der Attribute [@johnson2012beyond]. Das System nutzt davon nur zwei: gute Voreinstellungen, etwa das Schlafzimmer im ersten Grundrissvorschlag an der ruhigen Fassade, und verständliche Beschreibungen.

Die Evidenz für die Wirksamkeit solcher Interventionen ist umstritten. Die Meta-Analyse von Mertens et al. berichtet einen mittleren Effekt von d = 0,45 (95 %-KI 0,39 bis 0,52). Interventionen an der Struktur der Entscheidung wirkten stärker als solche an der Information. Die Autoren selbst stellen einen moderaten Publikationsbias fest [@mertens2022nudging]. Maier et al. korrigierten die Daten für diesen Bias und fanden danach keine belastbare Evidenz mehr für einen Nudging-Effekt [@maier2022nudging]. Für die Arbeit folgen drei Konsequenzen:

1. Die Voreinstellungen werden mit dem Inhalt der Empfehlung begründet, nicht mit der Wirksamkeit von Nudges. Das Schlafzimmer liegt an der ruhigen Seite, weil Lärm den Schlaf stört, nicht weil Voreinstellungen Verhalten lenken.
2. Der Arbeit werden keine Wirkungsversprechen der Art „die Assistenz führt zu besseren Häusern“ zugeschrieben, bevor sie selbst evaluiert ist.
3. Die Evaluation vergleicht Entwürfe mit und ohne Assistenz und ergänzt sie um die Befragung nach Einzug (Kapitel 20).

### 9b.7.5 Transparenz, Autonomie und Protokoll

Aus den Befunden und dem Prinzip 8 ergeben sich verbindliche Gestaltungsregeln:

- **Sichtbarkeit.** Jede Voreinstellung ist als solche erkennbar und mit einem Klick änderbar.
- **Autonomie.** R5 blockiert nie. Der Kunde kann jede Empfehlung ohne Begründung übergehen. Ein zweiter Hinweis zur selben Regel erscheint nur, wenn sich die Lage wesentlich ändert.
- **Keine Dark Patterns und keine Angstappelle.** Hinweise nennen Befund und Grad, nicht Risiken in dramatisierender Sprache.
- **Gesundheitsaussagen nur bei Grad A oder B der Art W**, immer mit Quelle.
- **Protokoll.** Jede Empfehlung wird mit Regelversion, Quelle, angezeigtem Text und Kundenentscheidung protokolliert und über die IFC-GUID mit dem Modell verknüpft (Prinzip 9 des Zielbilds).
- **Haftungsgrenze.** Empfehlungen sind keine Planungsleistung und keine Zusicherung einer Eigenschaft. Für die Planung bleibt die Entwurfsverfasserin verantwortlich (Kapitel 4.3.5) [U: im Einzelnen rechtlich nicht geprüft]. Gesundheitsbezogene Werbeaussagen zu Kulturprofilen („Feng Shui fördert die Gesundheit“) sind lauterkeitsrechtlich riskant [U].
- **KI-Transparenz.** Wo der Kunde mit einem KI-System interagiert, gelten die Transparenzpflichten nach Art. 50 der KI-Verordnung [@aiact2024]. Kapitel 10 behandelt sie für die Sprachschnittstelle.

### 9b.7.6 Kulturelle Sensibilität und Datenschutz

Feng Shui und Vastu sind lebendige Traditionen mit mehreren Schulen. Daraus folgen vier Regeln:

1. Das System vermischt keine Schulen und gibt die Schule jedes Regelsatzes an.
2. Die Regelsätze werden mit Praktikern der jeweiligen Tradition abgestimmt.
3. Religiöse Bestandteile wie der Andachtsraum im Vastu werden abgebildet, aber nicht bewertet.
4. Kulturprofile sind gleichrangige Wahloptionen, kein exotisierendes Sonderangebot. Das System kommentiert sie nicht herablassend. Die Kennzeichnung als „traditionelle Lehre“ ist eine sachliche Auskunft, kein Urteil über die Tradition.

Die Kua-Zahl der Kompassschule braucht das Geburtsdatum. Sie wird nur auf ausdrücklichen Wunsch berechnet, und das Geburtsdatum wird nicht gespeichert. Ein aktives Vastu-Profil kann Rückschlüsse auf religiöse Überzeugungen zulassen. Ob es damit eine besondere Kategorie personenbezogener Daten nach Art. 9 DSGVO berührt, ist rechtlich zu prüfen [U].

## 9b.8 Beispieldialoge

Die folgenden Kästen zeigen, wie die Schichten im Dialog zusammenwirken. Die Regel-IDs sind illustrativ. Die Texte folgen den Vorlagen aus 9b.2.3.

> **Kasten 9b.1 – Schlafzimmer nach Westen mit Glasfront**
>
> **Kunde:** „Das Schlafzimmer soll nach Westen raus, mit großer Glasfront zum Garten.“
>
> **System:** „Das ist möglich. Zwei Hinweise dazu. Erstens: Große Westfenster heizen Schlafräume im Sommer abends auf. Der sommerliche Wärmeschutz wird ohnehin geprüft, das ist Pflicht. Studien zeigen außerdem, dass Hitze im Schlafraum den Schlaf beeinträchtigt. Zweitens: Morgenlicht unterstützt den Tag-Nacht-Rhythmus. ‚Schlafen nach Osten‘ ist deshalb eine bewährte Planungsregel. Mein Vorschlag: Sie behalten die Glasfront und bekommen außen Raffstores. Oder Sie tauschen Schlafzimmer und Arbeitszimmer. Sie entscheiden.“
>
> **Empfehlung, weil:** Überhitzung beeinträchtigt den Schlaf; Morgenlicht wirkt auf den zirkadianen Rhythmus. **Evidenz:** thermischer Komfort B-W, Nachweis N [@emmitt2023bedroom; @din4108-2]; Morgenlicht B-W [@brown2022recommendations]; Ost-Schlaf C [@alexander1977pattern]. **Profil:** Außenbezug steigt, Raumklima sinkt; beide Varianten sind Pareto-optimal.

> **Kasten 9b.2 – Bett gegenüber der Tür**
>
> **Kunde:** „Das Bett kommt gegenüber der Tür, Kopfende an die Fensterwand.“
>
> **System:** „Die meisten Menschen wählen einen Bettplatz, von dem aus sie die Tür sehen und der möglichst weit von ihr entfernt ist. Das ist eine gut belegte Vorliebe. Eine Wirkung auf den Schlaf ist nicht untersucht. Ihre Position erfüllt das. Aber: Der Fensterflügel ragt bei voller Öffnung in die Bettfläche. Wenn Sie das Bett 40 cm nach links rücken oder einen Kippflügel wählen, passt es.“
>
> **Empfehlung, weil:** Der Flügel kollidiert mit der Bettfläche (Möblierbarkeit); die Stellung selbst entspricht der verbreiteten Präferenz. **Evidenz:** Möblierbarkeit C [@bwo2015wbs]; Bettposition B-P [@spoerrle2010sleeping; @bonin2023goodnight].

> **Kasten 9b.3 – Schlafzimmer zur Straße**
>
> **Kunde:** „Die Schlafzimmer bitte nach vorne zur Straße, dann ist der Garten fürs Wohnzimmer frei.“
>
> **System:** „Die Straße ist laut Lärmkarte nachts deutlich über dem Wert, ab dem die WHO Gesundheitsschäden durch Straßenverkehr sieht. Das ist gut belegt. Studien zeigen außerdem, dass ein Schlafzimmerfenster zur ruhigen Seite schlechten Schlaf seltener macht. Wenn die Schlafzimmer zum Garten gehen, sinkt auch die Schallschutzanforderung an die Fenster, das spart Kosten. Wohnzimmer und Küche vertragen die Straßenseite besser. Möchten Sie die Variante sehen?“
>
> **Empfehlung, weil:** nächtlicher Verkehrslärm schadet; die Fensterorientierung zur ruhigen Seite schützt den Schlaf; der Normabschlag an der abgewandten Fassade senkt die Anforderung. **Evidenz:** A-W [@who2018noise]; B-W [@bodin2015quiet; @bartels2021impact; @ohrstrom2006quietness]; Abschlag N (DIN 4109-2, Recherche 20). Die Lärmkarte dient nur dem Screening, nicht dem Nachweis.

> **Kasten 9b.4 – Feng Shui und die fehlende Ecke**
>
> **Kunde:** „Bitte Feng Shui einschalten. Ist die fehlende Ecke im Nordosten schlimm?“
>
> **System:** „Das Feng-Shui-Profil ist aktiv. Vorab: Feng Shui ist eine traditionelle chinesische Lehre, ihre Wirkungen sind wissenschaftlich nicht belegt. Die Bewertung zählt deshalb getrennt und fließt nicht in die Wohnqualität ein. Nach dem Bagua-Raster fehlt im Nordosten etwa ein Drittel des Feldes. Die Lehre würde die Ecke mit einem Anbau, einer Terrasse oder einer Pergola schließen. Ein Punkt Ihres Entwurfs deckt sich mit der Forschung: Ihr Bett steht in der ‚Kommandoposition‘, und die meisten Menschen bevorzugen genau diesen Platz. Einen Widerspruch gibt es bei der Treppe gegenüber der Haustür. Feng Shui sieht sie als ungünstig, für die Orientierung im Haus ist sie dagegen günstig. Das wägen Sie ab.“
>
> **Empfehlung, weil:** Der Kunde hat das Profil gewählt; das System ordnet jede Regel ein und zeigt Deckung und Konflikt. **Evidenz:** Bagua D; Kommandoposition D mit Überschneidung B-P [@spoerrle2010sleeping; @hong2016fengshui]; Orientierung C [@hillier1984social].

> **Kasten 9b.5 – Erdstrahlen und Radon**
>
> **Kunde:** „Können Sie den Schlafplatz auf Wasseradern und Erdstrahlen prüfen?“
>
> **System:** „Das bieten wir nicht an. Eine große, vom Bund finanzierte Versuchsreihe mit rund 500 Rutengängern ergab in der unabhängigen Auswertung keinen Nachweis. Grundwasser fließt außerdem meist flächig, nicht in Adern. Was nachweislich zählt: Ihr Grundstück liegt in einem Radonvorsorgegebiet. Radon ist ein gut belegtes Gesundheitsrisiko, deshalb ist eine radonsichere Bodenplatte vorgesehen. Sie können außerdem Materialien wählen, die nach QNG schadstoffgeprüft sind. Auf Wunsch führen wir Leitungen nicht am Bett entlang. Das ist eine Komfortoption, ein Gesundheitsnutzen ist nach heutigem Wissen nicht belegt.“
>
> **Empfehlung, weil:** Die Frage betrifft einen Punkt der Ausschlussliste; das System lenkt auf die belegten Punkte derselben Sorge. **Evidenz:** Erdstrahlen X [@enright1995dowsing]; Radon A-W, N [@bfs2025radon]; Schadstoffe A/B-W [@air2016formaldehyd; @qng2023anlage3]; Felder unterhalb der Grenzwerte C [U].

## 9b.9 Homeoffice-Assistenz

Die Arbeit im eigenen Haus ist ein Wirkfaktor, der erst seit der Pandemie systematisch untersucht wird. Die wichtigste deutsche Quelle ist die BBSR-Studie „Funktionswandel des Wohnens“ [@wegener2024funktionswandel]. Sie beruht auf einer repräsentativen Bevölkerungsbefragung zu Krisenerfahrungen, Nutzungsprofilen, Wohnpraktiken und Wohnwünschen. Laut Recherche 21 nutzen 84 % der Befragten, die zu Hause arbeiten können, das Homeoffice. Nur die Hälfte hält die eigene Wohnung dafür für geeignet. Als Gründe werden fehlender Rückzugsraum, zu wenig Platz, Lärm und Dunkelheit genannt [V: BBSR-Seite]. Die vier Gründe entsprechen vier Dimensionen des Profils aus 9b.5.3: Ruhe und Privatheit, Funktion, Ruhe, Licht.

Weitere Studien ergänzen das Bild:

- Eine begutachtete deutsche Befragung fand keine klare Verschiebung der Standortpräferenzen durch das Homeoffice. Die Umzugsbereitschaft war aber höher, vor allem in als zu klein empfundenen Wohnungen, und die Unzufriedenheit war bei wenig Platz größer [@neumann2022homeoffice].
- Bei 988 Büroangestellten im Homeoffice hing das Wohlbefinden unter anderem mit der Einrichtung des Arbeitsplatzes, Kindern im Haushalt und Ablenkungen zusammen [@xiao2021wfh].
- Bei 8.177 Studierenden in Mailand ging Wohnen auf weniger als 60 m², schlechter Ausblick und geringe Innenraumqualität im Lockdown mit einem höheren Risiko depressiver Symptome einher [@amerio2020covid].
- Eine Pressemitteilung der LBS nennt, dass jeder Fünfte der 20- bis 45-Jährigen einen Heimarbeitsplatz eingerichtet hat. Ein Studienbericht fehlt, sie dient nur als Kontext [@lbs2020wohnwuensche].

Alle Befunde sind Querschnittsdaten, meist aus einer Ausnahmesituation und oft aus Wohnungen im Geschossbau. Sie tragen Grad **B-W** für den Zusammenhang und **C** für die konkreten Maße. Wählt der Kunde das Nutzerprofil „Homeoffice“ mit einer Zahl von Arbeitstagen, aktiviert das System folgende Regeln:

| Regel | Prädikat | Grad | Quelle |
|---|---|---|---|
| eigener Arbeitsplatz mit Fenster | Arbeitsplatz in der Fensterzone, Sichtverbindung nach außen | B-W | [@ko2020window; @amerio2020covid; @brown2022recommendations] |
| akustisch getrennt vom Wohn- und Kinderbereich | Arbeitsraum nicht offen zum Wohnbereich; Tür; keine gemeinsame Wand mit dem Kinderzimmer | B-W | [@xiao2021wfh; @wegener2024funktionswandel] |
| bevorzugt abschließbar | eigener Raum mit Tür, kein Durchgangsraum | C | [@wegener2024funktionswandel; @fornara2022space] |
| Mindestgröße | Planungswert ≈ 6 m² | C [U] | Recherche 15 |
| später umnutzbar | Arbeitsraum als Kinder- oder Gästezimmer möblierbar (K18) | C | [@bwo2015wbs; @herthogs2019saga] |
| Blick zur Tür | Tür im Isovist des Schreibtischs | C-P | [@dosen2016prospect] |

Beim Schallschutz ist eine Designentscheidung zu treffen. Ob ein Arbeitszimmer nach DIN 4109 als Tagraum oder wie ein Schlafraum einzustufen ist, hängt davon ab, ob es überwiegend zum Schlafen genutzt werden *kann* (Recherche 20). Das System stuft es deshalb standardmäßig wie einen Schlafraum ein. Das ist die sichere Seite, wenn das Zimmer später Gäste- oder Kinderzimmer wird.

> **Kasten 9b.6 – Schreibtisch in der Wohnzimmerecke**
>
> **Kunde:** „Küche, Essen und Wohnen in einem Raum, und mein Schreibtisch kommt in die Wohnzimmerecke. Ich arbeite drei Tage die Woche zu Hause.“
>
> **System:** „Küche und Essplatz liegen 2,40 m auseinander, das ist gut. Beim Arbeitsplatz ein Hinweis: In Studien hingen Ablenkung und Kinder im Haushalt mit schlechterem Befinden im Homeoffice zusammen. In einer großen deutschen Befragung hielt nur die Hälfte der Menschen ihre Wohnung fürs Homeoffice geeignet, oft wegen fehlenden Rückzugs und Lärm. Vorschlag: eine abtrennbare Nische mit Fenster und Schiebetür, oder das Gästezimmer im Obergeschoss als Arbeitszimmer mit Tür. Bei gleicher Wohnfläche wird der Wohnraum dann 5 m² kleiner.“
>
> **Empfehlung, weil:** fehlende Abgrenzung von Arbeit und Familie hängt mit schlechterem Befinden zusammen. **Evidenz:** Kochen–Essen C [@bwo2015wbs]; Homeoffice B-W (Querschnitt) [@xiao2021wfh; @wegener2024funktionswandel; @neumann2022homeoffice].

## 9b.10 Grenzen und Zwischenfazit

**Grenzen.** Vier Einschränkungen bestimmen die Reichweite des Kapitels.

1. **Übertragbarkeit.** Viele Studien beruhen auf kleinen Stichproben, auf Studierenden aus westlichen Industrieländern, auf Bildreizen statt gebauten Räumen und auf Wohnungen im Geschossbau. Für das bayerische Einfamilienhaus im Holzrahmenbau ist die Evidenz fast immer indirekt. Die Studienlage zu Nutzerperspektiven in vorgefertigten Holzgebäuden ist laut einem Scoping Review dünn [@campagna2025usercentered].
2. **Wirkung der Assistenz.** Ob die Assistenz zu besseren Häusern führt, ist nicht belegt und wegen der Nudging-Debatte auch nicht zu unterstellen. Die Arbeit prüft das in Kapitel 20 mit einem Vergleich von Entwürfen mit und ohne Assistenz und schlägt die Befragung nach Einzug vor.
3. **Offene Quellenpunkte.** Die WBS-Punktelogik für fünf Kriterien, die Aussichtsstufen der EN 17037 (Recherche 15 nennt 14°, 28° und 54° horizontal) [U] und die Einstufung von Feuchte und Feldern sind nicht abschließend geprüft.
4. **Einstufung als Urteil.** Evidenzgrade sind begründete Urteile, keine Messwerte. Das mittelmäßige κ bei der Nutzungsart zeigt, dass zwei sorgfältige Bewerter hier auseinanderliegen können. Die doppelte Vergabe und Versionierung der Grade (9b.2.4) ist die Antwort darauf.

**Zwischenfazit.** Das Kapitel präzisiert Prinzip 8 des Zielbilds in vier Punkten.

1. **Empfehlungen sind eine eigene Regelklasse.** R5 unterscheidet sich von R1–R4 nicht durch das Thema, sondern durch die Geltung: Sie blockiert nie, trägt einen Evidenzgrad und wird als gewichteter Soft Constraint berechnet. Status N und Evidenzgrad sind unabhängig.
2. **Belastbare Wirkungsevidenz gibt es nur für wenige Faktoren.** Lärm (A), Tageslicht und zirkadianes Licht, Außenbezug, Beengtheit, sommerliche Überhitzung und Zugänglichkeit im Alter (jeweils B) tragen die Assistenz. Bekannte Entwurfsregeln wie Bettposition, Raumhöhe und Kurven sind Präferenzbefunde. Prospect-Refuge ist im Innenraum schwächer belegt als in der Architekturliteratur angenommen (C-P). Das System trennt diese Arten sprachlich.
3. **Wohnqualität ist ein Profil, kein Wert.** Ein WBS-lite aus den Kriterien K15 bis K24, ergänzt um Space Syntax und Isovisten, macht Grundrissqualität rechenbar. Ausgegeben werden sechs Dimensionen und die Pareto-Menge der Varianten.
4. **Kulturprofile sind Wahl, nicht Wissen.** Feng Shui und Vastu sind Grad D mit ausgewiesenen Überschneidungen und Konflikten. Die Baubiologie wird geteilt: Radon und Schadstoffe sind über Strahlenschutzrecht und QNG evidenzbasiert abbildbar, Erdstrahlen stehen auf der Ausschlussliste.

Das Muster der Assistenz ist Critiquing. Der Kunde entwirft, das System kommentiert an der Entscheidungsstelle mit Begründung, Quelle und Grad, und der Kunde entscheidet. Kapitel 10 greift die Erklärungen für die Sprachschnittstelle auf, Kapitel 12 die Licht- und Materialempfehlungen für die Bemusterung, Kapitel 20 die Evaluation der Assistenz.

---

## Verwendete Keys

abdalhamid2023quantifying, aiact2024, air2016formaldehyd, alexander1977pattern, ali2013critiquing, altman1975environment, amerio2020covid, appleton1975experience, appleton1984prospects, aries2015daylight, bafna2003space, bar2006curved, bartels2021impact, basner2014noise, baybo2026, benedikt1979take, bfs2025radon, bodin2015quiet, bonin2023goodnight, boumova2016apartment, bourassa1999hedonic, brown2020melanopic, brown2022recommendations, browning2014patterns, bwo2015wbs, cain2020evening, cajochen2022evening, campagna2025usercentered, chakrabarti1998vastu, chen2026critiquecrew, chuquichambi2022curvature, coburn2017buildings, cohen1960coefficient, dawes2014wright, dawes2017pattern, dgnb2023soc, din1946-6, din2019tageslicht, din4108-2, din5034-1, dosen2013methodological, dosen2016prospect, dosen2017lived, elliot2014color, emmitt2023bedroom, enright1995dowsing, erculiani2019layout, evans1998crowding, evans2003built, evans2006child, faller2002wohngrundriss, femenias2020adaptable, fischer1989environments, fischer1991critiquing, fischer1993critics, flade2006wohnen, fornara2022space, fortin2014superstition, gann2003design, graham2015psychology, gregor1999explanations, guyatt2008grade, hanson1998decoding, haubl2000decisionaids, heckmann2017grundrissatlas, herthogs2019saga, higueratrujillo2021cognitive, hildebrand1999origins, hillier1984social, hong2016fengshui, houser2020humancentric, hwang2018window, ibn2018leitlinien, iwbi2020wellv2, jakesch2023cowriting, johnson2012beyond, joye2018broken, kaplan1995restorative, ko2020window, koren1994wabisabi, kremerpreiss2011wohnenalter, lan2017thermal, landis1977measurement, lbs2020wohnwuensche, li2020qualitative, lin2012fengshui, linnet2011hygge, maes2024sbm, maier2022nudging, mak2005fengshui, marquardt2011wayfinding, merrell2011interactive, mertens2022nudging, meseguer2006soft, meyerslevy2007ceiling, miller2019explanation, neufert2022bauentwurfslehre, neumann2022homeoffice, oh2008critiquing, oh2010furniture, ohly2016attention, ohrstrom2006quietness, ostwald2011mathematics, oswald2007housing, oxman1990prior, patra2009vaastu, peng2012concern, poldrack2006reverse, preiser1988poe, prpj2022fengshui, qng2023anlage3, rambow2000expertenlaien, rewatkar2026data, roswall2020nighttime, silverman1992critiquing, silverman1992expert, spoerrle2010sleeping, stamps2006interior, stamps2008some, stefani2024evidencebased, tam1999fengshui, thaler2008nudge, turner2001isovists, ulrich1984view, vartanian2013contour, vartanian2015ceiling, walden2008architekturpsychologie, wang2007recommendation, wang2022embodiment, wegener2024funktionswandel, west2004functional, wiener2007isovist, wilms2018color, xiao2021wfh, zahedi2022bim, zhong2022biophilic

**Key-Prüfung (Python, 27.09.2026):** siehe unten.

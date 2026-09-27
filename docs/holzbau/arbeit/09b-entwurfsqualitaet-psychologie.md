# 9b Entwurfsqualität: Architekturpsychologie und Kulturprofile

Status: Entwurf v0.2 (27.09.2026). Zitate beziehen sich auf `literatur/lit-*.bib`, überwiegend auf `lit-F-architekturpsychologie.bib`. **[V]** = an Primärquelle, Abstract oder Verlagsseite geprüft, **[U]** = unsicher oder nicht erneut geprüft. Maschinenlesbarer Katalog: `spezifikation/empfehlungen.yaml`.

## 9b.0 Einordnung und Vorgehen

Die Kapitel 4, 9 und 9a beschreiben Regeln, die einen Entwurf zulassen oder verbieten. Ein Haus kann alle diese Regeln einhalten und trotzdem schlecht sein: das Schlafzimmer an der lauten Straße, die Küche drei Räume vom Essplatz entfernt, ein Kinderzimmer, in das kein Bett passt, ohne dass die Tür dagegen schlägt. Architekten vermeiden solche Fehler aus Erfahrung. Ein Laie, der mit dem System selbst entwirft, hat diese Erfahrung nicht.

Das Zielbild fasst die Antwort in Prinzip 8 zusammen: **Assistieren statt bevormunden.** Empfehlungen aus Architektur- und Umweltpsychologie kommen mit Begründung und Evidenzgrad. Kulturprofile wie Feng Shui, Vastu oder Baubiologie kann der Kunde wählen; sie sind als Tradition gekennzeichnet und werden nie als Wissenschaft ausgegeben. Dieses Kapitel macht das Prinzip formal und prüfbar. Es beantwortet vier Fragen:

1. Wie unterscheidet sich eine Empfehlung formal von einer Regel, und wie wird sie berechnet?
2. Welche Wirkfaktoren sind so gut belegt, dass das System sie vertreten darf, und wie werden sie am Grundriss gemessen?
3. Wie werden Kulturprofile abgebildet, ohne dass Tradition als Wissen erscheint oder Kunden bevormundet werden?
4. Welche Form der Assistenz ist vertretbar, wenn die Wirksamkeit von Nudges selbst umstritten ist?

**Quellenbasis.** Grundlage sind die Recherchen 15 (Kern), 21 (deutschsprachige Architekturpsychologie, BBSR-Studie), 20 (Außenlärm) und 13 (Möblierung). In der Quellenbewertung tragen 180 Quellen einen Bezug zu Kapitel 9b: 27 „übernehmen“, 70 „adaptieren“, 71 „Kontext“, 10 „abgrenzen“, 2 „verwerfen“. Für 72 davon lag kein Abstract vor. Aussagen über Studienergebnisse stehen deshalb nur dort, wo Abstract, Einzelbewertung oder Recherche sie stützen.

**Qualität der Einstufung.** Die blinde Zweitbewertung von 80 Quellen ergab für die Relevanz zu FF6 ein quadratisch gewichtetes κ = 0,81 bei 66 % exakter Übereinstimmung, für die Quellenqualität κ = 0,95, für die Nutzungsart aber nur κ = 0,45 [@cohen1960coefficient; @landis1977measurement]. Zwei der neun abweichenden Kernbestand-Entscheidungen betreffen dieses Kapitel (`bafna2003space`, `oswald2007housing`). Die Relevanz ist also reproduzierbar eingestuft, die Frage, *wie* eine Quelle genutzt wird, ist dagegen Ermessen. Das gilt erst recht für die daraus abgeleiteten Evidenzgrade (Konsequenz in 9b.2.4).

**Aufbau.** Das Evidenzgrad-Schema (Gliederungspunkt 6) steht als 9b.2 vorn, weil alle folgenden Abschnitte es verwenden. Die Ethik folgt in 9b.7, die Umsetzungsvorgaben für die App in 9b.11.

## 9b.1 Regelklasse R5 „Empfehlungen“

### 9b.1.1 Definition und Abgrenzung

Kapitel 4.1 unterscheidet R1 Entwurfsgrenzen, R2 Informationsanforderungen, R3 Verantwortungsregeln und R4 Formregeln. Allen ist gemeinsam, dass ihre Verletzung einen Fortgang verhindert. Die fünfte Klasse ist von anderer Art.

> **Definition 9b.1 (R5-Empfehlung).** Eine R5-Regel ist ein Prädikat über das Grundriss- und Gebäudemodell, das einen Erfüllungsgrad zwischen 0 und 1 liefert. Sie trägt Evidenzgrad, Evidenzart, Quellen und Erklärtext. Ihre Verletzung blockiert nichts; sie erzeugt einen Hinweis und verändert ein Qualitätsprofil.

| Merkmal | R1–R4 (hart) | R5 (weich) |
|---|---|---|
| Wirkung einer Verletzung | blockiert Entwurf, Übergabe oder Freigabe | Hinweis, Profilwert sinkt |
| Abweichung | niemand (R1, R2, R4) bzw. berechtigte Person (R3) | der Kunde, ohne Begründungspflicht |
| Geltungsgrund | Recht, Norm, Herstellerregel (Status N) | Evidenz zu Wirkung oder Präferenz, Planungswissen |
| Ergebnis | wahr/falsch mit Grenzwert und Ausnutzung | Erfüllungsgrad, Evidenzgrad, Begründung |
| Konflikte | unzulässig (Lösungsraum leer) | zulässig und sichtbar (Zielkonflikt) |
| Formalisierung | Constraint, IDS, Freigabe-Gate, Export | gewichteter Soft Constraint [@meseguer2006soft] |

Die Abgrenzung betrifft die Geltung, nicht das Thema. Die Fensterfläche von einem Achtel der Netto-Grundfläche ist nach Art. 45 BayBO eine R1-Grenze [@baybo2026]. Tageslichtquotient nach DIN 5034-1 [@din5034-1] und Stufen der DIN EN 17037 [@din2019tageslicht] sind für Einfamilienhäuser nicht verlangt und erscheinen als R5-Hinweis (Beispiel 4.3). Der Schallschutznachweis gegen Außenlärm ist hart (Recherche 20), die Empfehlung, Schlafräume zur ruhigen Fassade zu legen, ist R5.

Deshalb gibt es einen **Status N** (Norm oder Recht), der vom Evidenzgrad unabhängig ist. Eine Norm kann verbindlich sein, obwohl ihr Inhalt nur Expertenkonsens ist (Grad C). Umgekehrt kann eine gut belegte Wirkung rechtlich unverbindlich sein, etwa die Schwellen der WHO-Lärmleitlinie [@who2018noise].

Zu R2 besteht eine Abhängigkeit. Viele Prädikate brauchen Informationen, die nicht jeder Entwurfsstand enthält: Möblierung, Nordwinkel, Fassadenpegel. Fehlt die Information, liefert die Regel „nicht bewertbar“ statt 0. Sonst erschiene ein unvollständiges Modell als schlechtes Modell.

### 9b.1.2 Der Regeldatensatz

Jede R5-Regel ist ein versionierter Datensatz (Schema in `empfehlungen.yaml`): `id` und Version, Dimension, Evidenzgrad und -art, Profil (evidenzbasiert oder Kulturprofil), Nutzerprofil, Kennzahl mit Berechnungsvorschrift und Einheit, Schwellen, Erfüllungsfunktion, Meldungstext, Quellen-Keys, Konflikte und Status V/U.

Der Meldungstext ist für Laien eigens formuliert. Architekten und Laien nehmen Räume unterschiedlich wahr und bewerten sie unterschiedlich [@rambow2000expertenlaien]. Bei drei Grundrissvarianten einer Plattenbauwohnung unterschieden sich beide Gruppen systematisch, vor allem bei Topologie, Privatheit und der Abgrenzung öffentlicher und privater Zonen [@boumova2016apartment]. Dass qualitative Begriffe bis zur Quelle rückverfolgbar formalisiert werden können, zeigen Li et al. mit einem Answer-Set-Programm, das Formulierungen wie „leicht zu sehen“ auf Befunde der Kognitionspsychologie zurückführt [@li2020qualitative]. Zahedi et al. binden Entwurfsentscheidungen mit Begründung an Modellelemente [@zahedi2022bim].

### 9b.1.3 Berechnung als Soft Constraints

Die R1-Regeln bestimmen die Menge zulässiger Entwürfe $X$. Für $x \in X$ liefert jede R5-Regel $i$ einen Erfüllungsgrad $s_i(x) \in [0,1] \cup \{\bot\}$, wobei $\bot$ „nicht bewertbar“ bedeutet. Das Gewicht ergibt sich aus dem Evidenzgrad $e_i$ und einer Gewichtung $u_d$ der Dimension, die der Kunde ändern kann:

$$w_i = g(e_i)\cdot u_{d(i)}, \qquad g(\mathrm{A}) = 1{,}0;\ g(\mathrm{B}) = 0{,}7;\ g(\mathrm{C}) = 0{,}4;\ g(\mathrm{D}) = 0.$$

Die Werte von $g$ sind eine Designentscheidung, die per Bewohnerbefragung kalibriert wird (9b.5.4). Der Wert einer Dimension ist das gewichtete Mittel ihrer bewertbaren Regeln:

$$S_d(x) = \frac{\sum_{i \in I_d,\ s_i(x) \neq \bot} w_i\, s_i(x)}{\sum_{i \in I_d,\ s_i(x) \neq \bot} w_i}.$$

Ausgegeben wird der Profilvektor $\mathbf{S}(x) = (S_1(x), \dots, S_m(x))$ mit der Abdeckung je Dimension, nicht seine Summe. Ein Kulturprofil $p$ erhält einen eigenen Teilscore $K_p(x)$ gleicher Form mit Gewicht 1 je Regel, der nie in $\mathbf{S}$ einfließt.

Formal ist das ein gewichtetes Constraint-Problem [@meseguer2006soft], nur ohne Aggregation über Dimensionen, weil diese Zielkonflikte verdeckt (9b.5.3). Dasselbe Muster, weiche Präferenzen neben harten Regeln, nutzen Erculiani et al. in einem Grundrissgenerator [@erculiani2019layout]. Merrell et al. zeigen, dass Einrichtungsleitlinien als Terme einer Bewertungsfunktion Laien zu messbar besseren Möblierungen führen [@merrell2011interactive]. Ihr stochastisches Sampling wird nicht übernommen, weil die Kette deterministisch bleibt (Kapitel 7).

## 9b.2 Evidenzgrad-Schema

### 9b.2.1 Grade und Evidenzarten

Das Schema lehnt sich an GRADE an, das Evidenzqualität und Empfehlungsstärke trennt [@guyatt2008grade]. Die Übertragung auf Entwurfsregeln ist eine eigene Adaption mit zwei Achsen. Die erste ist der **Grad**:

| Grad | Definition | Beispiele | Laientext |
|---|---|---|---|
| **A** | Systematisches Review oder Meta-Analyse mit konsistentem Befund zur *Wirkung*, oder Leitlinie nach GRADE | WHO-Lärmleitlinie [@who2018noise]; Radon [@bfs2025radon] | „gut belegt“ |
| **B** | Kontrollierte Einzelstudien, konsistente Beobachtungsstudien, Konsens auf Laborbasis, oder Meta-Analysen nur zur *Präferenz* | Fensterblick [@ko2020window]; Bettposition [@spoerrle2010sleeping; @bonin2023goodnight]; Kurvenpräferenz [@chuquichambi2022curvature] | „belegt (Studien)“; bei Präferenz „Die meisten Menschen bevorzugen …“ |
| **C** | Expertenkonsens, Lehrbuch, Norm oder Bewertungssystem ohne direkte Wirkungsstudie | WBS [@bwo2015wbs]; Neufert [@neufert2022bauentwurfslehre]; Alexander [@alexander1977pattern] | „bewährte Planungsregel“ |
| **D** | Tradition oder Kulturlehre ohne empirische Prüfung | Bagua, Vastu-Mandala | „traditionelle Lehre, nicht wissenschaftlich belegt“ |
| **X** | geprüft und ohne Befund | Wünschelrute, „Wasseradern“ [@enright1995dowsing] | nicht angeboten, nur auf Nachfrage erklärt |

Die zweite Achse ist die **Evidenzart**: Wirkung (W) auf Gesundheit, Wohlbefinden, Leistung oder Schlaf; Präferenz (P), also was Menschen wählen oder schön finden; Markt (M), also Zahlungsbereitschaft. Angegeben wird beides, etwa „A-W“ für die Lärmschwellen oder „B-P“ für die Bettposition.

Drei Einstufungsregeln sichern die Konsistenz:

1. **Präferenz erreicht höchstens B.** Auch eine Meta-Analyse zur Präferenz belegt nur, was Menschen mögen. Die Kurvenpräferenz ist meta-analytisch gesichert (Hedges' g = 0,39 aus 61 Studien), aber von Reiz, Darbietungszeit, Aufgabe und Expertise abhängig [@chuquichambi2022curvature]. Recherche 15 hatte sie für Objekte mit A eingestuft; das widerspricht der eigenen Definition und wird korrigiert.
2. **Narrative Übersichten erreichen höchstens B.** Die Übersichten von Evans zu Wohnen, Beengtheit und Kindesentwicklung sind nicht systematisch [@evans2003built; @evans2006child]. Crowding wird deshalb B-W, nicht wie in Recherche 15 A/B.
3. **Neurowissenschaftliche Befunde erhöhen keinen Grad.** fMRI-Studien mit Bildreizen messen ästhetische Urteile, keine Langzeitwirkung, und der Schluss von der Hirnaktivierung auf einen psychischen Zustand ist schwach [@poldrack2006reverse]. Die Neuroarchitektur fordert selbst Studien mit Bewegung im Raum [@wang2022embodiment; @coburn2017buildings; @higueratrujillo2021cognitive]. „Neuro“ ist kein Qualitätsmerkmal.

### 9b.2.2 Abgrenzung zur Quellenqualität

Die Quellenbewertung verwendet ebenfalls A bis D, bewertet aber die *Quelle* (Übersichtsarbeit, Einzelstudie, graue Literatur, Tradition; Kapitel 2a). Der Evidenzgrad bewertet die *Aussage einer Regel* über alle Quellen. Eine Übersichtsarbeit der Qualität A kann eine Regel des Grades C tragen: Die Meta-Analyse zu Prospect-Refuge findet für Innenräume inkonsistente Ergebnisse [@dosen2016prospect]. Im System heißt es deshalb stets „Evidenzgrad“, wenn die Regel gemeint ist.

### 9b.2.3 Sprachliche Trennung

Die Evidenzart bestimmt die Satzform. Meldungen entstehen aus Vorlagen, die an Grad und Art gebunden sind; verbotene Wendungen werden automatisch geprüft (`textregeln` im Katalog):

| Art und Grad | zulässig | unzulässig |
|---|---|---|
| W, A | „… schadet nachweislich …“ | – |
| W, B (Beobachtung) | „… hängt in Studien mit … zusammen“ | „… bewirkt …“ |
| P, B | „Die meisten Menschen bevorzugen …; eine Wirkung auf … ist nicht belegt.“ | „… ist gesünder“, „… schläft besser“ |
| C | „bewährte Planungsregel“ | „wissenschaftlich erwiesen“ |
| M | „In Märkten mit … zahlen Käufer … mehr.“ | Schluss vom Preis auf eine Wirkung |
| D | „Nach der Lehre des … gilt …“ | Indikativ als Tatsache („das Chi fließt ab“) |
| X | „geprüft, ohne Befund“ | jede Bewertung am Grundriss |

Das ist keine Stilfrage. Querschnittsstudien aus dem Lockdown zeigen Zusammenhänge, keine Ursachen [@amerio2020covid; @fornara2022space]; eine kausale Formulierung überhöhte die Evidenz.

### 9b.2.4 Pflege der Grade

Evidenzgrade sind zeitgebunden und werden wie Regelwerk-Profile versioniert (Kapitel 9.3). Jede Änderung eines Grades erzeugt eine neue Regelversion, die im Nachweis steht (Prinzip 9). Wegen des mittelmäßigen κ bei der Nutzungsart vergeben zwei Personen jeden Grad unabhängig; die Übereinstimmung wird berichtet.

## 9b.3 Evidenzbasierte Wirkfaktoren

### 9b.3.1 Übersicht

Die Tabelle führt die Faktoren, die das System vertritt, geordnet nach Evidenzgrad. Die rechte Spalte nennt die Katalog-IDs.

| Faktor | Befund | Evidenzgrad | rechenbare Kennzahl / Entwurfsregel | Quelle |
|---|---|---|---|---|
| Verkehrslärm | Leitlinie nach GRADE: Straßenverkehr schadet ab 53 dB Lden / 45 dB Lnight | A-W | Lnight vor dem Schlafraumfenster (Lärmkarte, Screening) · R5-RUHE-01 | [@who2018noise; @basner2014noise] |
| Ruhige Seite | Zugang zur ruhigen Seite senkt Belästigung (OR 0,47); Fensterorientierung sagt Schlaf besser vorher als der Pegel der lautesten Fassade | B-W | ΔL zwischen Schlafraumfassade und leisester Fassade ≤ 3 dB · R5-RUHE-02 | [@ohrstrom2006quietness; @bodin2015quiet; @bartels2021impact; @roswall2020nighttime] |
| Schadstoffe, Radon | Richtwert Formaldehyd 0,1 mg/m³; Radon-Referenzwert 300 Bq/m³ | A-W, Radon N | Anteil QNG-Produkte; radonsichere Bodenplatte im Vorsorgegebiet · R5-KLIMA-02/03 | [@air2016formaldehyd; @qng2023anlage3; @bfs2025radon] |
| Tageslicht | Review: begrenzte, für die Planung nutzbare Belege | B-W; Schwellen C | EN 17037 „gering“: 300 lx auf 50 %, 100 lx auf 95 % der Fläche · R5-LICHT-01 | [@aries2015daylight; @din2019tageslicht; @din5034-1] |
| Zirkadianes Licht | Konsens: tags ≥ 250 lx mEDI am Auge, abends ≤ 10 lx | B-W | Schlafraum verdunkelbar; Arbeitsplatz in der Fensterzone · R5-LICHT-03/04 | [@brown2022recommendations; @brown2020melanopic; @cajochen2022evening] |
| Außenbezug | Crossover-Experiment (n = 86): kühler empfunden, positivere Emotion, besseres Arbeitsgedächtnis; Review gemischt | B-W | Fenster im Isovist des Nutzungsorts · R5-AUSSEN-01 | [@ko2020window; @ulrich1984view; @ohly2016attention; @abdalhamid2023quantifying] |
| Beengtheit, Rückzug | chronische Beengtheit hängt bei Kindern mit Schulproblemen, Hilflosigkeit und Blutdruck zusammen | B-W | Personen je Raum ≤ 1; eigener Raum ab Schulalter · R5-RUHE-05 | [@evans1998crowding; @evans2006child; @fornara2022space] |
| Überhitzung Schlafraum | Reviews: Hitze stört den Schlaf, Planungsevidenz lückenhaft | B-W; Nachweis N | W/SW-Glas ohne außenliegenden Sonnenschutz · R5-KLIMA-01 | [@emmitt2023bedroom; @lan2017thermal; @din4108-2] |
| Zugänglichkeit im Alter | Nutzbarkeit der Wohnung hängt mit Selbstständigkeit sehr alter Menschen zusammen | B-W | Profil „barrierefrei vorbereitet“ · R5-ANPASS-01 | [@oswald2007housing; @kremerpreiss2011wohnenalter] |
| Bettposition | Bett mit Blick zur Tür, weit entfernt, auf der Seite des Aufschlags; repliziert | B-P | Tür im Isovist vom Kopfkissen ∧ außerhalb Türschwenk · R5-FUNKTION-02 | [@spoerrle2010sleeping; @bonin2023goodnight] |
| Raumhöhe | höhere Decken eher als schön beurteilt (Bildstudie) | B-P | lichte Höhe ≥ 2,50 m im Wohnbereich · R5-WIRKUNG-01 | [@vartanian2015ceiling; @meyerslevy2007ceiling] |
| Kurven | Meta-Analyse zur Kurvenpräferenz; Räume schöner, ohne Annäherungseffekt | B-P | nur Hinweis bei Möbeln (im Holzrahmenbau teuer) | [@chuquichambi2022curvature; @vartanian2013contour] |
| Prospect-Refuge | Meta-Analyse inkonsistent; acht Studien: Effekte nahe null | C-P | Zugang sichtbar, Wand im Rücken · R5-AUSSEN-04 | [@dosen2016prospect; @stamps2008some; @stamps2006interior] |
| Privatheit, Zonierung | Privatheitstheorie; Space Syntax von Wohnhäusern | C | Tiefe Schlafen > Tiefe Wohnen; kein Durchgangsschlafraum · R5-RUHE-03/04 | [@altman1975environment; @hanson1998decoding] |
| Orientierung | Isovistenmaße korrelieren mit Navigation (VR); Demenz: Grundrisstypologie wirkt stärker als Beschilderung | C; B-W (Demenz) | Sichtachse Eingang → Treppe/Wohnen · R5-FUNKTION-08 | [@wiener2007isovist; @marquardt2011wayfinding] |
| Farbe | Befunde uneinheitlich, kaum Feldstudien | C | keine Farbregel mit Gesundheitsbezug | [@elliot2014color; @wilms2018color] |

### 9b.3.2 Wirkung: Lärm, Licht, Außenbezug, Beengtheit

**Lärm.** Für den Grundriss zählt, *wo* der Pegel ankommt. Bei 956 Befragten senkte der Zugang zu einer ruhigen Seite Störungen um 30 bis 50 %, entsprechend etwa 5 dB weniger an der lautesten Fassade [@ohrstrom2006quietness]. In einer Querschnittsstudie mit berufstätigen Frauen sagte der modellierte Nachtpegel an der lautesten Fassade schlechten Schlaf kaum vorher; die ruhige Fassade wirkte in jeder Pegelklasse schützend [@bartels2021impact]. In einer dänischen Kohorte (44.438 Personen) ging Nachtlärm an der lautesten Fassade mit leicht erhöhter Einlösung von Schlafmittelrezepten einher (HR 1,05), an der leisesten nicht (HR 1,00) [@roswall2020nighttime]. Die Regel verbindet sich mit dem harten Nachweis: DIN 4109-2 erlaubt an der abgewandten Fassade 5 dB Abschlag bei offener Bebauung. Im Prototyp B19 sinkt die Anforderung im Schlafzimmer dadurch von 42 auf 36,8 dB, die Fenster brauchen Schallschutzklasse 3 statt 5 (Recherche 20). Das System zeigt beides, trennt aber die Begründungen: Schlaf ist Evidenz, der Abschlag ist Norm.

**Licht.** Das Review von Aries et al. findet nur begrenzte, statistisch belastbare Belege für Gesundheitswirkungen von Tageslicht, aber genug für erste Planungskategorien [@aries2015daylight]. Für die nicht-visuelle Wirkung gibt es quantitative Konsensempfehlungen in melanopischer EDI [@brown2022recommendations]; die Größe stützt eine Reanalyse von 19 Laborstudien [@brown2020melanopic]. Die Meta-Analyse zum Abendlicht findet Dosis-Wirkungs-Beziehungen für Einschlaflatenz und Schlafeffizienz bei 100 bis 1.000 lx mEDI, aber Gesamteffekte mit Konfidenzintervallen, die null einschließen [@cajochen2022evening]. Fast die Hälfte der untersuchten Wohnungen war abends hell genug, um Melatonin um 50 % zu unterdrücken [@cain2020evening]. Für den Grundriss folgen daraus nur zwei Regeln (Verdunkelung, Arbeitsplatz am Fenster). Die Abendlichtempfehlung gehört in die Bemusterung (Kapitel 12), wo auch die Warnung vor Werbeversprechen des Human-Centric Lighting gilt [@houser2020humancentric].

**Außenbezug.** Ulrichs Krankenhausstudie (23 gegen 23 Patienten) ist klein, retrospektiv und nicht auf Wohnen bezogen [@ulrich1984view]. Belastbarer ist das randomisierte Crossover-Experiment von Ko et al.: Mit Fenster war das thermische Empfinden um 0,3 Skalenpunkte kühler, 12 % mehr Personen waren thermisch zufrieden, Emotion und Arbeitsgedächtnis waren besser; Kurzzeitgedächtnis, Planung und Kreativität unterschieden sich nicht [@ko2020window]. Das systematische Review zur Aufmerksamkeitserholung findet gemischte Befunde [@ohly2016attention], die Theorie dahinter ist umstritten [@joye2018broken; @kaplan1995restorative]. Die Empfehlung ist deshalb B-W, ohne Mechanismusbehauptung. Vom Biophilic Design übernimmt das System nur einzeln belegte Muster, weil die Rahmenwerke heterogen sind [@zhong2022biophilic] und die Sternebewertung bei Terrapin eine Selbstbewertung ist [@browning2014patterns].

**Beengtheit.** Bei 10- bis 12-jährigen Kindern in Indien hing chronische Wohnbeengtheit mit Schulproblemen, erlernter Hilflosigkeit und Blutdruck zusammen, auch nach Kontrolle des Einkommens [@evans1998crowding]. Die Dichten liegen weit über denen eines deutschen Einfamilienhauses. Die Regel zählt deshalb vor allem bei knappen Raumprogrammen und im Mehrfamilienhaus (Kapitel 9a).

### 9b.3.3 Präferenz: Bettposition und Prospect-Refuge

Hier zeigt sich die Trennung von Wirkung und Präferenz am deutlichsten. Spörrle und Stich ließen 138 Personen Möbel auf variierten Grundrissen anordnen. Die Teilnehmenden stellten das Bett überwiegend so, dass sie die Tür sahen, möglichst weit von ihr entfernt und auf der Seite des Türaufschlags [@spoerrle2010sleeping]. Bonin et al. replizierten das mit 2D- und 3D-Plänen in Frankreich und der Slowakei [@bonin2023goodnight]. Belegt ist eine robuste *Vorliebe*; ob Menschen so besser schlafen, ist nicht untersucht.

Die Prospect-Refuge-Theorie stammt aus der Landschaftsästhetik [@appleton1975experience; @appleton1984prospects] und wurde interpretierend auf Wohnhäuser übertragen [@hildebrand1999origins]. Für Innenräume ist die Lage schwächer, als die Architekturliteratur nahelegt. Die Meta-Analyse von Dosen und Ostwald findet für Innen- und Stadträume Unterstützung für Prospect, neutrale Ergebnisse für Refuge und insgesamt inkonsistente Evidenz; die in der Architektur zitierten Befunde stammen meist aus Landschaftsstudien [@dosen2016prospect; @dosen2013methodological]. Stamps fasste acht Studien mit 144 Personen und 80 Umgebungen zusammen: Nur die Art der Umgebung wirkte deutlich (r = 0,42), Prospect und Refuge lagen nahe null [@stamps2008some]. Im Innenraumexperiment wirkte nur die Raumbreite (r = 0,35) [@stamps2006interior].

Die Arbeit stuft Prospect-Refuge im Innenraum deshalb als **C-P** ein, strenger als Recherche 15. Die Bettregel bleibt **B-P**, weil sie in einem eigenen Paradigma repliziert ist. Die Feng-Shui-„Kommandoposition“ deckt sich also mit einer replizierten Vorliebe, nicht mit einer Wirkungsaussage (9b.6.2).

Bei Präferenzregeln ist die eigene Äußerung des Kunden die bessere Evidenz für seine Vorliebe. P-Regeln sind deshalb vom Kunden aussetzbar (`aussetzbar_durch_kunde`). W-Regeln bleiben als Hinweis bestehen; entscheiden darf der Kunde trotzdem (9b.7.4).

## 9b.4 Rechenbares Grundrisswissen

### 9b.4.1 Graph und Geometrie

Die Prädikate arbeiten auf zwei Darstellungen aus dem IFC-Modell (Kapitel 8): einem **Raumgraphen** $G = (V, E)$ mit Räumen (`IfcSpace`) und Außenraum als Knoten und Türen bzw. Durchgängen als Kanten, und der **Geometrie** mit Raumpolygonen, Öffnungen samt Flügeln, Stell- und Bewegungsflächen und dem Nordwinkel des Modellkontexts.

### 9b.4.2 Zonierung und Raumbeziehungen

Der Privatheitsgradient wird über den **Justified Graph** ab der Haustür geprüft [@hillier1984social; @hanson1998decoding]. Mit $d_{ij}$ als Schrittzahl zwischen Raum $i$ und $j$ gilt: Die mittlere Tiefe der Schlafräume ist größer als die des Wohnbereichs (C, gestützt durch die Privatheitstheorie [@altman1975environment] und Alexanders Muster #127 [@alexander1977pattern]). Kein Schlafraum liegt als einziger Weg zwischen zwei anderen Räumen, und das Gäste-WC ist vom Eingang ohne Weg durch den privaten Bereich erreichbar.

Raumbeziehungen werden als Graph- und Abstandsprädikate formuliert. WBS K19 gibt Schwellen: Kochen und Essen Mitte zu Mitte unter 300 cm, Durchgang über 120 cm, Kochbereich an der Fassade mit öffenbarem Fenster [@bwo2015wbs]; Funktionsstudien zum deutschen Wohngrundriss liefern den Kontext [@faller2002wohngrundriss]. Auch **Anpassbarkeit** ist am Graphen messbar: SAGA quantifiziert sie mit gewichteten Graphen und fünf Kennzahlen, nur an sechs Layouts illustriert [@herthogs2019saga]; bei 313 von Eigentümern umgebauten Wohnungen hingen Wohnraumgröße und Zersplitterung des Ausgangsgrundrisses mit Umbauten zusammen [@femenias2020adaptable].

### 9b.4.3 Himmelsrichtung

„Wohnen nach Süden und Westen, Schlafen nach Osten“ hat keine eigene Wirkungsstudie. Quellen sind Alexanders Muster #138 [@alexander1977pattern], die Bauentwurfslehre [@neufert2022bauentwurfslehre] und die Besonnungsempfehlungen [@din2019tageslicht]. Mechanistisch plausibel ist die Regel über Morgenlicht [@brown2022recommendations] und die Überhitzung westorientierter Schlafräume [@emmitt2023bedroom]. Sie wird als **C, mechanistisch gestützt durch B** geführt. WBS K24 formuliert eine Zählregel: Mindestens 50 % der Zimmerfenster liegen nicht in einem Sektor von ±60° um Nord (Recherche 15) [V]. Mit $\alpha_f$ als Azimut der Außennormalen von Fenster $f$ gilt $\text{nord}(f) \iff |\alpha_f| \le 60^\circ$. Ohne Nordwinkel ist die Regel nicht bewertbar.

### 9b.4.4 Möblierbarkeit und Stauraum

Möblierbarkeit ist der Faktor, an dem Laien am häufigsten scheitern und der am besten rechenbar ist; eine britische Analyse spekulativ gebauter Neubauhäuser untersuchte genau diese Funktionalität (nach Titel eingeordnet) [@west2004functional]. WBS K18 liefert einen direkt implementierbaren Algorithmus [@bwo2015wbs]:

1. Je Zimmer werden alle Stellungen eines Bettmoduls gesucht (Doppelbett ab 12 m², Einzelbett ab 10 m²), bei denen mindestens das Kopfende eine Wand berührt.
2. Gültig ist eine Stellung, wenn kein Tür- oder Fensterflügel bei 90° Öffnung in die Bettfläche ragt.
3. Die gültigen Stellungen werden je Zimmer gezählt und über alle Zimmer gemittelt; Zusatzpunkte gibt es u. a. für eine Wendefläche von 140 × 170 cm am Bett.

Der Aufwand ist linear in der Zahl der Wandsegmente mal der Kollisionsprüfungen. Auf dieselbe Menge gültiger Stellungen wird die Bettpräferenz angewandt: Das System sucht unter den möblierbaren Stellungen jene mit Türsicht.

Für übrige Stell- und Bewegungsflächen gilt keine Norm mehr; DIN 18011 ist zurückgezogen und galt schon 1990 als ungeeignet für Mindestgrößen (Recherche 13) [V]. Ihre Werte dienen als Startheuristik (70 cm zwischen Stellfläche und Wand, Eingangsflur 130 cm, Nebenflur 90 cm), ergänzt um die Bauentwurfslehre [@neufert2022bauentwurfslehre], 120 cm Bewegungsfläche vor der Küchenzeile und DIN 18040-2 für die Barrierefreiheit (Recherche 13). Alle Werte sind Grad C. Wie sich Rückmeldung dazu nach dem Wissensstand abstufen lässt, zeigt ein constraint-basierter Möbelkritiker [@oh2010furniture].

**Stauraum** folgt WBS K21: Schrankmodul 60 × 60 × 180 cm mit 90 cm Bedienfläche (120 cm im Kochbereich), Zusatzpunkte für Einbauschrank, Abstellraum und Außenstauraum [@bwo2015wbs]. Eine explorative Studie fand Stauraum unter sechs gewünschten Raumatmosphären, ein Präferenzbefund [@graham2015psychology].

### 9b.4.5 Verkehrsfläche

Der Verkehrsflächenanteil folgt DIN 277 (Kapitel 9a). Einen belegten Zielwert für Einfamilienhäuser gibt es nicht [U]. Das System weist ihn deshalb relativ aus, als Perzentil gegen die rund 160 Referenzgrundrisse des Grundrissatlas [@heckmann2017grundrissatlas] und später gegen den Herstellerkatalog. Ein Hinweis erscheint über dem 90. Perzentil (Designentscheidung).

### 9b.4.6 Space Syntax und Isovisten

Space Syntax stellt Konfigurationsmaße bereit [@hillier1984social; @bafna2003space]. Mit $k$ Knoten gilt für Raum $i$:

$$\mathrm{MD}_i = \frac{\sum_{j \neq i} d_{ij}}{k-1}, \qquad \mathrm{RA}_i = \frac{2(\mathrm{MD}_i - 1)}{k-2}, \qquad \mathrm{RRA}_i = \frac{\mathrm{RA}_i}{D_k},$$

mit $D_k$ als Normierungswert eines rautenförmigen Referenzgraphen; die Integration ist $1/\mathrm{RRA}_i$. Ostwalds mathematische Revision dient als Implementierungsgrundlage [@ostwald2011mathematics]. Einfamilienhäuser haben nur etwa 8 bis 15 Knoten, und die Normierung reagiert bei kleinen Graphen empfindlich. Das System zeigt deshalb vor allem Tiefe und Rangfolge und vergleicht RRA nur zwischen Varianten gleicher Knotenzahl (Designentscheidung).

Das **Isovist** ist die Menge aller von einem Standpunkt sichtbaren Punkte; Benedikt schlug Größen- und Formmaße vor und nannte Blickkontrolle, Privatheit und Weite als Anwendungen [@benedikt1979take]. Turner et al. bauten daraus den Sichtbarkeitsgraphen [@turner2001isovists]. In 16 virtuellen Innenräumen korrelierten wenige Isovistenmaße stark mit Navigation und Raumerleben [@wiener2007isovist]. Das System nutzt die Isovistenfläche $A(p)$ am Nutzungsort und das Prädikat „Zugang sichtbar“. Hwangs parametrisches Verfahren für Fenster ist ein Methodenbeispiel ohne Nutzerstudie [@hwang2018window]. Isovistenmaße tragen deshalb C- und P-Regeln, keine W-Regeln.

### 9b.4.7 Alexander-Muster

Nur ein kleiner Teil der 253 Muster ist empirisch geprüft, die Kritik bemängelt fehlende Überprüfbarkeit [@dawes2017pattern]. Übernommen werden einzeln bewertete Muster mit Prädikat: #127 Intimacy Gradient (Tiefenordnung, C), #138 Sleeping to the East (Azimut, C, mechanistisch B), #159 Light on Two Sides (Fenster an zwei Fassaden, C [U]), #179/#180 Alcoves und Window Place (Sitzplatz mit Wand im Rücken, C-P), #190 Ceiling Height Variety (B-P [@vartanian2015ceiling]) und #112 Entrance Transition (Windfang, C).

## 9b.5 Wohnqualitäts-Scoring: Profil statt Gesamtscore

### 9b.5.1 Das Schweizer Wohnungs-Bewertungs-System

Das WBS des Schweizer Bundesamts für Wohnungswesen ist das einzige gefundene System, das Wohnqualität weitgehend rechenbar macht [@bwo2015wbs]. Die Ausgabe 2015 hat 25 Kriterien in den Bereichen Wohnstandort, Wohnanlage und Wohnung, je höchstens 4 Punkte, zusammen 100 plus höchstens 5 Innovationspunkte, dargestellt als Netzdiagramm. Es bewertet Gebrauchswert und Nutzungsflexibilität, nicht Gesundheit; seine Kriterien sind Grad C.

Die Arbeit implementiert ein **WBS-lite** aus den Wohnungskriterien und kennzeichnet es als eigene Adaption. SIA 500 wird durch DIN 18040-2 ersetzt. Die Punktelogik von K15 bis K17, K22 und K23 konnte am Original nicht vollständig nachgelesen werden [U]; dort steht eine eigene Operationalisierung.

| WBS-Kriterium | geometrisch prüfbar als | Prüflogik |
|---|---|---|
| K15 Nettowohnfläche | Fläche je Person | eigene Operationalisierung [U] |
| K16 Zimmergröße | Anteil der Zimmer ≥ 10 bzw. ≥ 12 m² | Schwellen aus K18, Rest [U] |
| K17 vielfältige Nutzbarkeit | Zimmer mit ≥ 2 Möblierungsvarianten | eigene Operationalisierung [U] |
| K18 Möblierbarkeit | Bettmodul-Algorithmus (9b.4.4) | WBS [V] |
| K19 Koch- und Essbereich | Abstand, Durchgang, Fenster | WBS [V] |
| K20 Sanitär | Bewegungsflächen nach DIN 18040-2 | WBS [V], Ersatz eigene Adaption |
| K21 Abstellbereich | Schrankmodule, Abstellraum | WBS [V] |
| K22 Anpassungsfähigkeit | umnutzbare Zimmer, SAGA-Maße | eigene Operationalisierung [U] |
| K23 privater Außenbereich | Fläche, Direktzugang von Wohnraum oder Küche | eigene Operationalisierung [U] |
| K24 Übergänge innen/außen | Zwischenzone, Öffentlichkeitsgrade, Nordanteil ≤ 50 % | WBS [V] |

### 9b.5.2 Andere Bewertungssysteme

DGNB deckt mit SOC1.1 bis SOC1.6 thermischen, visuellen und akustischen Komfort, Innenraumluft und Aufenthaltsqualität ab; die Gewichtung von 4,2 % für Wohngebäude ist unsicher [@dgnb2023soc] [U]. QNG regelt in Anhang 313 die Schadstoffvermeidung [@qng2023anlage3] und ist die Brücke zur Baubiologie. WELL v2 dient nur als Ideengeber, weil es auf Büros zielt [@iwbi2020wellv2]. Der Design Quality Indicator erfasst wahrgenommene Entwurfsqualität mit Rahmen, Erhebungswerkzeug und Gewichtung [@gann2003design]. Ein neuer Rahmen für Wohnqualität im Mehrfamilienhausbau gewichtet über Experten und 411 Bewohner Lüftung und Tageslicht am höchsten [@rewatkar2026data].

### 9b.5.3 Profil und Pareto-Vergleich

Das System zeigt keinen Gesamtscore, aus drei Gründen. Erstens verdeckt eine Summe Zielkonflikte: Ein Westschlafzimmer mit Glasfront kann im Außenbezug gut und im Raumklima schlecht sein, gemittelt „durchschnittlich“. Zweitens lädt ein Einzelwert dazu ein, auf die Kennzahl statt auf Qualität zu optimieren (Goodhart-Effekt, hier Designbegründung). Drittens wäre eine Summe mit unkalibrierten Gewichten Scheingenauigkeit.

Ausgegeben wird ein **Profil mit sieben Dimensionen**: Licht; Ruhe und Privatheit; Raumklima und Innenraumluft; Funktion und Möblierbarkeit; Außenbezug; Anpassbarkeit und Barrierearmut; Raumwirkung (Vorlieben). Die siebte Dimension sammelt reine Präferenzregeln wie Raumhöhe und Prospect, damit Vorlieben nicht mit Wirkungen verrechnet werden. Das Kulturprofil erscheint als separater Balken.

Bei mehreren Varianten bestimmt das System die **Pareto-Menge**:

$$x \succ y \iff \forall d:\ S_d(x) \ge S_d(y)\ \wedge\ \exists d:\ S_d(x) > S_d(y).$$

Dominierte Varianten werden markiert, die übrigen in einer Vergleichsmatrix gezeigt. Ein Empfehlungsagent mit Vergleichsmatrix senkte in einem Experiment zum Onlinekauf den Suchaufwand und verbesserte die Entscheidungsqualität [@haubl2000decisionaids]. Die Übertragung auf den Hausentwurf ist eine Hypothese für Kapitel 20.

### 9b.5.4 Kalibrierung durch Bewohnerbefragung

Die Gewichte sind die schwächste Stelle. Preiser et al. unterscheiden indikative, investigative und diagnostische Post-Occupancy Evaluation [@preiser1988poe]. Vorgeschlagen wird eine indikative Befragung 12 bis 24 Monate nach Einzug; Waldens Konstrukt „Umweltkontrolle“ aus dem Koblenzer Architekturfragebogen ist übertragbar [@walden2008architekturpsychologie]. Die Befragung kalibriert $g$ und $u_d$ und ist ein eigener empirischer Beitrag. Bis dahin gilt die Assistenz nicht als „bewiesen gut“.

## 9b.6 Kulturprofile

### 9b.6.1 Grundsatz

Kulturprofile sind **nur auf Wunsch aktiv**, haben einen eigenen Teilscore, der nie in das Wohnqualitätsprofil einfließt, und jede Regel trägt die Kennzeichnung „traditionelle Lehre“. Überschneidungen und Konflikte mit evidenzbasierten Regeln werden ausgewiesen. Dass das Profil nicht ungefragt erscheint, hat einen empirischen Grund: Bei 246 Bewohnern Taipehs stieg die Sorge um Feng Shui mit dem Aberglauben und sank mit der Selbstwirksamkeit [@peng2012concern]. Ein ungefragtes Feng-Shui-Urteil würde gerade die Empfänglichen verunsichern. Flade führt Feng Shui in ihrer Wohnpsychologie als Trendthema [@flade2006wohnen].

### 9b.6.2 Feng Shui

Die **Formschule** beurteilt Landschafts- und Gebäudeform, etwa das „Lehnstuhl“-Ideal mit Rückendeckung. Die **Kompassschule** arbeitet mit Bagua, Luopan, der aus dem Geburtsdatum berechneten Kua-Zahl und den Fliegenden Sternen. Architekten in Hongkong befolgen Prinzipien der Formschule oft ohnehin und halten sie für eher rational analysierbar [@mak2005fengshui]; das ist Wahrnehmungs-, nicht Wirkungsforschung. Prüfbar sind vor allem Regeln der Formschule:

| Regel (nach der Lehre) | Prädikat | Grad | Überschneidung |
|---|---|---|---|
| Bett in „Kommandoposition“ (FS-01) | Tür vom Kopfkissen sichtbar, Bettachse nicht in Türflucht | D | **Deckung** mit Bettposition B-P; eine Diagonalstellung erfüllt beide |
| Schreibtisch mit Rückendeckung (FS-02) | Rückwandabstand ≤ Parameter, Tür im Isovist | D | Teildeckung mit Prospect-Refuge C-P |
| Haustür nicht in Flucht mit Hintertür (FS-03) | Strahl ab Haustür trifft ungehindert auf Außenöffnung | D | Teildeckung: Windfang, Einblick (C) |
| Treppe nicht gegenüber Haustür (FS-04) | Treppenantritt in Sichtachse ab Eingang | D | **Konflikt:** Orientierung wertet Treppensicht positiv (C) |
| WC nicht im Zentrum, nicht gegenüber Küche (FS-05) | Hüllflächenschwerpunkt ∉ WC; Sichtlinien | D | Teildeckung: Geruch, Privatheit (C) |
| Bagua, „fehlende Ecken“ (FS-06) | 3 × 3-Raster, Flächenanteil je Feld | D | keine |
| keine „Giftpfeile“ (FS-07) | Außenecke zeigt auf Nutzungsort | D | schwach: Kurvenpräferenz B-P |

Die Wirkung ist **D**. Eine Befragung in Malaysia (N = 405) prüfte sie direkt: Ein nach der Formschule gestaltetes Schlafzimmer wurde deutlich bevorzugt, ging aber nicht mit besserer subjektiver Schlafqualität einher [@hong2016fengshui]. Das ist dasselbe Muster wie bei der Bettposition. Belegt ist dagegen eine **Marktwirkung (B-M)** in Märkten mit hohem chinesischstämmigem Käuferanteil: In Vancouver wurden Häuser mit einer 4 am Ende der Hausnummer 2,2 % billiger, mit einer 8 um 2,5 % teurer verkauft (rund 117.000 Verkäufe) [@fortin2014superstition]; ähnliche Effekte zeigen Studien aus Auckland, Taiwan und Hongkong [@bourassa1999hedonic; @lin2012fengshui; @tam1999fengshui; @prpj2022fengshui]. Das ist Zahlungsbereitschaft, keine Wirkung, und für Bayern nicht übertragbar.

**Marktrelevanz in Deutschland.** Ein deutscher Fertighaushersteller bietet „Hausbau nach Feng Shui“ an; bei Baufritz und Regnauer fand die Recherche kein solches Angebot, beide positionieren sich über Baubiologie (Recherche 15) [V]. Berater nennen für eine Komplettauswertung etwa 3.750 € netto [V]. Nachfragezahlen fehlen [U]; Feng Shui ist eine Nische, deren Größe per Kundenbefragung zu erheben ist.

### 9b.6.3 Vastu Shastra

Vastu legt ein Mandala aus 8 × 8 oder 9 × 9 Feldern über Grundstück oder Haus. Das Zentrum bleibt frei, der Eingang liegt bevorzugt im Osten, Norden oder Nordosten, die Küche im Südosten, das Hauptschlafzimmer im Südwesten, kein WC im Nordosten; die Varianten unterscheiden sich je Schule [U]. Geometrisch ist das eine Rasterüberlagerung mit Sektorzuordnung (VA-01 bis VA-04). Die Evidenz ist **D**: Chakrabarti analysiert die Praxis kulturhistorisch [@chakrabarti1998vastu], Patra argumentiert ohne empirische Prüfung für die Vereinbarkeit mit Nachhaltigkeit [@patra2009vaastu].

Bei 48 bis 54° nördlicher Breite entsteht ein **Zielkonflikt**: Ein Südwestschlafzimmer bekommt Abendsonne und ein Überhitzungsrisiko (B-W, Nachweis nach DIN 4108-2 [@din4108-2]) und widerspricht der Ost-Schlaf-Regel (C). Das System zeigt den Konflikt, löst ihn nicht selbst auf und schlägt Maßnahmen vor, die beiden Zielen dienen, etwa außenliegenden Sonnenschutz. Die Marktrelevanz ist eine Nische ohne Zahlen [U].

### 9b.6.4 Baubiologie

Die Baubiologie ist für den deutschen Holzfertighausmarkt das wichtigste Profil, weil Hersteller mit Wohngesundheit werben. Quellen sind die 25 Leitlinien des IBN in fünf Kategorien [@ibn2018leitlinien] und der Standard SBM-2024 mit den Teilen Felder und Strahlung (A1 bis A7), Wohngifte (B) sowie Pilze und Allergene (C) [@maes2024sbm]. Seine Richtwerte für Schlafbereiche sind vorsorglich, nicht gesundheitsbasiert abgeleitet; Teil A7 führt „geologische Störungen“ einschließlich „Erdstrahlung“. Anders als Feng Shui zerfällt die Baubiologie in zwei Teile:

| Punkt | Grad | Behandlung |
|---|---|---|
| Radon | A-W, N | Referenzwert 300 Bq/m³ (§§ 124, 126 StrlSchG) [@bfs2025radon]; radonsichere Bodenplatte im Vorsorgegebiet (R5-KLIMA-03) |
| Formaldehyd, VOC | A/B-W | Richtwert 0,1 mg/m³ [@air2016formaldehyd]; Materialwahl nach QNG Anhang 313 (R5-KLIMA-02) |
| Feuchte, Schimmel | N; Wirkungsgrad [U] | Feuchteschutz, Lüftungskonzept nach DIN 1946-6 [@din1946-6]; die WHO-Leitlinie zur Innenraumfeuchte ist nicht Teil der Literaturbasis |
| Tageslicht, Akustik | B/C | deckungsgleich mit 9b.3 |
| NF/HF-Felder unter den Grenzwerten | C [U] | nur Komfortoption „vorsorglich, kein Gesundheitsnutzen belegt“ (BB-03); Werbeaussagen zum Elektrosmog-Schutz werden nicht übernommen |
| Erdstrahlen, Wasseradern | **X** | nicht angeboten (9b.6.5) |

Das System bildet so die evidenzbasierte Hälfte über QNG und Strahlenschutzrecht ab, ohne die esoterische zu übernehmen. Für Hersteller ist das ein Schutz: Belegtes lässt sich mit Quelle vertreten, Unbelegtes wird nicht als Leistung ausgewiesen.

### 9b.6.5 Ausschlussliste

Die Ausschlussliste enthält Aussagen, die geprüft wurden und ohne Befund blieben. Sie werden nicht bewertet; fragt ein Kunde danach, erklärt das System, warum (X-01, X-02).

- **Wünschelrute, „Wasseradern“, „Erdstrahlen“, Globalgitter.** Die vom Bund finanzierten Scheunenversuche mit rund 500 Rutengängern ergaben in der Nachanalyse von Enright keinen Nachweis [@enright1995dowsing]. Ein Abstract lag nicht vor; die Aussage stützt sich auf Recherche 15 und die Einzelbewertung. Grundwasser fließt zudem meist flächig. Dass SBM-2024 den Punkt führt [@maes2024sbm], ändert die Einstufung nicht; der Standard ist Gegenstand der Abgrenzung, kein Beleg.

Die Liste ist bewusst kurz. Grad X ist Aussagen vorbehalten, die empirisch geprüft wurden; Ungeprüftes bleibt D. So wird die Ausschlussliste nicht zum Werkzeug, Traditionen pauschal abzuwerten.

### 9b.6.6 Stilprofile und weitere Überschneidungen

Wabi-Sabi ist ein ästhetisches Leitbild aus Unvollkommenheit, Patina und natürlichen Materialien [@koren1994wabisabi]. Hygge beschreibt die Anthropologie als soziale Praxis mit egalitären Normen und Ausgrenzung, nicht als Einrichtungsrezept [@linnet2011hygge]. Beide werden als **Stilprofile** ohne Gesundheitsversprechen geführt (D). Zwei Überschneidungen werden ausgewiesen: warmes, schwaches Abendlicht deckt sich mit ≤ 10 lx mEDI am Abend (B-W), Nischen und Ofenplatz decken sich teilweise mit Refuge (C-P, HY-01). Linnets Befund warnt zugleich davor, Kulturprofile auf Ratgeberregeln zu reduzieren.

## 9b.7 Assistenz-Architektur und Ethik

### 9b.7.1 Schichten

Die Assistenz hat vier Schichten und eine Ausschlussliste: (1) harte Regeln mit Status N, die blockieren; (2) evidenzbasierte Empfehlungen A und B, standardmäßig aktiv mit hohem Gewicht; (3) Planungswissen C, standardmäßig aktiv mit mittlerem Gewicht; (4) Kulturprofile D, nur auf Wunsch, mit eigenem Teilscore und eigener Farbe; (5) die Ausschlussliste X, die nur auf Nachfrage erklärt wird.

### 9b.7.2 Critiquing statt Autopilot

Das Muster ist **Critiquing**. Kooperative Problemlösungssysteme helfen Nutzern, Lösungen selbst zu entwerfen, statt sie für sie zu entwerfen; Kritiker lassen das Artefakt „zurücksprechen“, sind in eine Entwurfsumgebung mit argumentativem Hypertext, Spezifikation und Katalog eingebettet, und Lernen entsteht als Nebenprodukt [@fischer1991critiquing]. Vorbild war die Küchenplanung mit JANUS und dem Kritiker CRACK [@fischer1989environments]. Die Teilprozesse nach Fischer et al. bilden sich direkt auf das System ab:

| Teilprozess nach Fischer et al. 1991 | Komponente im System |
|---|---|
| Zielerfassung | Nutzerprofile (Homeoffice, Kinder, barrierefrei), Kulturprofil, Umgewichtung $u_d$ |
| Produktanalyse | Auswertung der R5-Prädikate am Modell |
| Kritikstrategie | Zeitpunkt und Dichte der Hinweise |
| Anpassung | Aussetzen von P-Regeln, Wissensstand des Nutzers |
| Erklärung und Argumentation | Meldung, Warum-Text, Quelle, Evidenzgrad, Konflikte |
| Beratung | Alternativvorschlag, der alle harten Regeln erfüllt |

Drei Befunde bestimmen die Kritikstrategie. **Zeitpunkt:** Nachträgliche Stapelkritik frustriert, Kritik sollte während des Entwerfens kommen [@silverman1992expert; @silverman1992critiquing; @fischer1993critics]. Wer ein Bett platziert, bekommt die Bettregel, nicht am Ende eine Mängelliste. **Form:** Kritik lässt sich nach Art (Interpretation, Erinnerung, Beispiel, Demonstration, Bewertung) und Modalität (Text, Annotation, Bild) wählen, abhängig von Wissensstand und Interaktionsverlauf [@oh2010furniture; @oh2008critiquing; @ali2013critiquing]. Standard ist eine grafische Annotation mit einem Satz Text; die Begründung öffnet sich auf Nachfrage. **Dichte:** höchstens drei Hinweise je Entwurfsschritt (Designentscheidung, in der Nutzerstudie zu prüfen). Referenzgrundrisse aus dem Grundrissatlas dienen als Beispiele im Sinne des Entwerfens aus Präzedenzfällen [@oxman1990prior]. Dass dialogische Kritik mit Reparaturvorschlägen einem statischen Prüfer überlegen sein kann, zeigen zwei kontrollierte Studien (N = 48) im UI-Design [@chen2026critiquecrew]; das stützt die Richtung, nicht die Übertragbarkeit.

### 9b.7.3 Erklärungen

Gute Erklärungen sind kontrastiv, selektiv und sozial [@miller2019explanation]. Menschen fragen „Warum Ost und nicht West?“ und wollen wenige Gründe. Das System beantwortet Kontrastfragen mit höchstens drei Gründen, jeweils mit Quelle und Grad. Erklärungen verbessern Leistung, Lernen und Vertrauen, wenn sie automatisch, kontextspezifisch und begründet angeboten werden [@gregor1999explanations]. Wie-, Warum- und Abwägungserklärungen stärken unterschiedliche Vertrauensüberzeugungen [@wang2007recommendation]. Für R5 ist die Abwägung am wichtigsten, weil fast jede Empfehlung einen Preis hat: Fläche, Kosten oder einen anderen Wunsch.

Meldungen werden aus dem Katalog erzeugt, nicht frei von einem Sprachmodell formuliert. In einem Experiment (N = 1.506) verschob ein meinungsgeprägter LLM-Schreibassistent nicht nur die Texte, sondern auch die später erhobene Einstellung der Teilnehmenden [@jakesch2023cowriting]. Ein frei formulierendes Modell könnte Wertungen einführen, die weder in der Regel noch in der Evidenz stehen. Das entspricht dem Architekturprinzip „Die KI versteht, der Code entscheidet“ (Kapitel 7).

### 9b.7.4 Nudging, Transparenz und Autonomie

Choice Architecture legitimiert sichtbare Voreinstellungen [@thaler2008nudge]; ihre Werkzeuge sind Voreinstellungen, Zahl und Struktur der Optionen und die Beschreibung der Attribute [@johnson2012beyond]. Das System nutzt nur gute Voreinstellungen (Schlafzimmer im ersten Vorschlag an der ruhigen Fassade) und verständliche Beschreibungen. Die Wirksamkeit ist umstritten. Mertens et al. berichten meta-analytisch d = 0,45 (95 %-KI 0,39 bis 0,52), stärkere Effekte für Interventionen an der Entscheidungsstruktur und selbst einen moderaten Publikationsbias [@mertens2022nudging]. Nach Korrektur dieses Bias fanden Maier et al. keine belastbare Evidenz mehr für einen Nudging-Effekt [@maier2022nudging]. Daraus folgt: Voreinstellungen werden mit dem Inhalt der Empfehlung begründet, nicht mit der Wirksamkeit von Nudges; der Assistenz werden keine Wirkungsversprechen zugeschrieben, bevor sie selbst evaluiert ist (Kapitel 20).

Aus Befunden und Prinzip 8 folgen Gestaltungsregeln, die in 9b.11 als Anforderungen stehen: jede Voreinstellung sichtbar und mit einem Klick änderbar; R5 blockiert nie, Abweichung ohne Begründung; keine Dark Patterns und keine Angstappelle; Gesundheitsaussagen nur bei A-W oder B-W mit Quelle; Protokoll jeder Empfehlung mit Regelversion, Text und Entscheidung, verknüpft über die IFC-GUID (Prinzip 9). Empfehlungen sind keine Planungsleistung und keine Zusicherung einer Eigenschaft; verantwortlich bleibt die Entwurfsverfasserin (Kapitel 4.3.5) [U: im Einzelnen rechtlich nicht geprüft]. Gesundheitsbezogene Werbeaussagen zu Kulturprofilen sind lauterkeitsrechtlich riskant [U]. Für die KI-Interaktion gelten die Transparenzpflichten nach Art. 50 der KI-Verordnung [@aiact2024] (Kapitel 10).

### 9b.7.5 Kulturelle Sensibilität und Datenschutz

Feng Shui und Vastu sind lebendige Traditionen mit mehreren Schulen. Das System vermischt keine Schulen und gibt sie an, stimmt die Regelsätze mit Praktikern ab, bildet religiöse Bestandteile wie den Andachtsraum im Vastu ab, ohne sie zu bewerten, und behandelt Kulturprofile als gleichrangige Wahl, nicht als exotisierendes Sonderangebot. Die Kennzeichnung „traditionelle Lehre“ ist Auskunft, kein Urteil. Die Kua-Zahl braucht das Geburtsdatum; sie wird nur auf ausdrücklichen Wunsch berechnet, das Datum nicht gespeichert. Ob ein aktives Vastu-Profil als Hinweis auf religiöse Überzeugungen unter Art. 9 DSGVO fällt, ist rechtlich zu prüfen [U].

## 9b.8 Beispieldialoge

Die Kästen sind als UI-Texte formuliert und können so übernommen werden. Platzhalter in geschweiften Klammern füllt die App aus dem Modell; die Beispielwerte stehen dahinter. Jede Meldung hat drei Teile: **Meldung** (sichtbar an der Entscheidungsstelle), **Aktionen** (Schaltflächen) und **Warum?** (aufklappbar, mit Evidenzhinweis und Quellen).

> **Kasten 9b.1 – UI-D1 Schlafzimmer nach Westen** · Regeln R5-KLIMA-01, R5-AUSSEN-03
>
> **Kunde:** „Das Schlafzimmer soll nach Westen raus, mit großer Glasfront zum Garten.“
>
> **Meldung:** „Gern. Ein Hinweis: Große Fenster nach Westen heizen das Schlafzimmer im Sommer abends auf. Hitze im Schlafzimmer stört in Studien den Schlaf.“
>
> **Aktionen:** [Raffstores außen ergänzen] · [Schlafzimmer mit {raum_ost} (Arbeitszimmer) tauschen] · [So lassen]
>
> **Warum?** „Hitze im Schlafzimmer stört den Schlaf (Studien). Morgenlicht unterstützt den Tag-Nacht-Rhythmus (Studien). ‚Schlafen nach Osten‘ ist deshalb eine bewährte Planungsregel. Den sommerlichen Wärmeschutz prüfen wir sowieso, er ist Pflicht. Sie entscheiden.“ · Quellen: [@emmitt2023bedroom; @brown2022recommendations; @alexander1977pattern; @din4108-2]

> **Kasten 9b.2 – UI-D2 Bett und Fensterflügel** · Regeln R5-FUNKTION-01, R5-FUNKTION-02
>
> **Kunde:** „Das Bett kommt gegenüber der Tür, Kopfende an die Fensterwand.“
>
> **Meldung:** „Der Fensterflügel stößt beim Öffnen ans Bett. Mit {verschiebung} (40 cm) nach links passt es.“
>
> **Aktionen:** [Bett {verschiebung} verschieben] · [Kippflügel wählen] · [So lassen]
>
> **Warum?** „Tür und Fenster sollen frei aufgehen (bewährte Planungsregel). Ihre Bettposition ist sonst gut: Die meisten Menschen stellen das Bett so, dass sie die Tür sehen und weit von ihr entfernt liegen. Das ist eine gut belegte Vorliebe. Ob man so besser schläft, ist nicht untersucht.“ · Quellen: [@bwo2015wbs; @spoerrle2010sleeping; @bonin2023goodnight]

> **Kasten 9b.3 – UI-D3 Schlafzimmer zur Straße** · Regeln R5-RUHE-01, R5-RUHE-02
>
> **Kunde:** „Die Schlafzimmer bitte nach vorne zur Straße, dann ist der Garten fürs Wohnzimmer frei.“
>
> **Meldung:** „An der Straßenseite ist es nachts laut, etwa {lnight} dB (59 dB). Das ist mehr, als für guten Schlaf empfohlen wird ({schwelle} dB, 45 dB).“
>
> **Aktionen:** [Variante mit Schlafzimmern zum Garten zeigen] · [Schallschutz-Details ansehen] · [So lassen]
>
> **Warum?** „Nächtlicher Verkehrslärm schadet der Gesundheit (gut belegt, WHO). Wer zur ruhigen Seite schläft, schläft seltener schlecht (Studien). Zum Garten hin sinkt auch die Schallschutzanforderung an die Fenster, das spart Kosten. Der Lärmwert ist eine Schätzung aus der Lärmkarte, der Nachweis folgt später.“ · Quellen: [@who2018noise; @bodin2015quiet; @bartels2021impact]

> **Kasten 9b.4 – UI-D4 Feng Shui** · Regeln FS-06, FS-01, FS-04, R5-FUNKTION-08
>
> **Kunde:** „Bitte Feng Shui einschalten. Ist die fehlende Ecke im Nordosten schlimm?“
>
> **Meldung beim Einschalten:** „Feng-Shui-Profil ist an. Feng Shui ist eine traditionelle chinesische Lehre. Ihre Wirkungen sind wissenschaftlich nicht belegt. Die Bewertung steht deshalb getrennt und zählt nicht zur Wohnqualität.“
>
> **Meldung:** „Nach dem Bagua-Raster fehlt im Feld {feld} (Nordosten) etwa {anteil} (30 %) der Fläche. Die Lehre würde die Ecke zum Beispiel mit Terrasse oder Pergola schließen.“
>
> **Aktionen:** [Terrasse ergänzen] · [Pergola ergänzen] · [So lassen] · [Profil ausschalten]
>
> **Warum?** „Das ist traditionelle Lehre, nicht wissenschaftlich belegt. Ihr Bett steht nach Feng Shui in der ‚Kommandoposition‘. Das passt zu Studien: Die meisten Menschen bevorzugen diesen Platz. Die Treppe gegenüber der Haustür gilt im Feng Shui als ungünstig, für die Orientierung im Haus ist sie aber günstig (bewährte Planungsregel). Das wägen Sie ab.“ · Quellen: [@mak2005fengshui; @spoerrle2010sleeping; @hong2016fengshui; @hillier1984social]

> **Kasten 9b.5 – UI-D5 Erdstrahlen** · Ausschluss X-01, X-02; Regeln R5-KLIMA-03, R5-KLIMA-02, BB-03
>
> **Kunde:** „Können Sie den Schlafplatz auf Wasseradern und Erdstrahlen prüfen?“
>
> **Meldung:** „Eine Prüfung auf Wasseradern und Erdstrahlen bieten wir nicht an. Was nachweislich zählt, prüfen wir: Ihr Grundstück liegt in einem Radonvorsorgegebiet, deshalb ist eine radonsichere Bodenplatte eingeplant.“
>
> **Aktionen:** [Schadstoffgeprüfte Materialien zeigen] · [Leitungen nicht am Bett führen (Komfortoption)] · [Warum keine Prüfung?]
>
> **Warum?** „In großen, vom Bund finanzierten Versuchen mit rund 500 Rutengängern ließ sich nicht nachweisen, dass sie Wasser zuverlässig finden. Grundwasser fließt außerdem meist flächig, nicht in Adern (geprüft, ohne Befund). Radon ist dagegen ein Gesundheitsrisiko (gut belegt). Leitungen abseits vom Bett sind eine Komfortoption; ein Gesundheitsnutzen ist nicht belegt.“ · Quellen: [@enright1995dowsing; @bfs2025radon; @qng2023anlage3]

## 9b.9 Homeoffice-Assistenz

Die wichtigste deutsche Quelle ist die BBSR-Studie „Funktionswandel des Wohnens“, eine repräsentative Befragung zu Krisenerfahrungen, Nutzungsprofilen und Wohnwünschen [@wegener2024funktionswandel]. Laut Recherche 21 nutzen 84 % der Befragten, die zu Hause arbeiten können, das Homeoffice; nur die Hälfte hält die Wohnung dafür für geeignet, wegen fehlenden Rückzugsraums, zu wenig Platz, Lärm und Dunkelheit [V: BBSR-Seite]. Das sind vier Dimensionen des Profils. Eine begutachtete deutsche Befragung fand keine klare Verschiebung der Standortpräferenzen, aber höhere Umzugsbereitschaft und Unzufriedenheit in als zu klein empfundenen Wohnungen [@neumann2022homeoffice]. Bei 988 Büroangestellten hing das Wohlbefinden im Homeoffice unter anderem mit Arbeitsplatz, Kindern im Haushalt und Ablenkung zusammen [@xiao2021wfh]. Bei 8.177 Studierenden in Mailand gingen Wohnungen unter 60 m², schlechter Ausblick und geringe Innenraumqualität mit höherem Risiko depressiver Symptome einher [@amerio2020covid]. Eine LBS-Pressemitteilung, nach der jeder Fünfte der 20- bis 45-Jährigen einen Heimarbeitsplatz eingerichtet hat, dient nur als Kontext [@lbs2020wohnwuensche].

Alle Befunde sind Querschnittsdaten aus einer Ausnahmesituation, oft aus Geschosswohnungen. Sie tragen B-W für den Zusammenhang und C für konkrete Maße. Wählt der Kunde das Nutzerprofil „Homeoffice“ mit der Zahl der Arbeitstage, aktiviert das System:

| Regel | Prädikat | Grad | Katalog |
|---|---|---|---|
| Arbeitsplatz mit Tageslicht | ≥ 300 lx Tageslicht am Schreibtisch (Analogie EN 17037) [U] | B-W | R5-LICHT-04 |
| akustisch getrennt | Raum mit Tür, nicht offen zum Wohnbereich, keine Wand mit Kinderzimmer | B-W | R5-HOME-01 |
| eigener Raum | ≈ 6 m² mit Tür und Fenster (Planungswert) | C [U] | R5-HOME-02 |
| später umnutzbar | als Kinder- oder Gästezimmer möblierbar | C | R5-ANPASS-02 |
| Blick zur Tür | Tür im Isovist des Schreibtischs | C-P | R5-AUSSEN-04 |

Beim Schallschutz stuft das System ein Arbeitszimmer standardmäßig wie einen Schlafraum ein, weil DIN 4109 darauf abstellt, ob ein Raum überwiegend zum Schlafen genutzt werden *kann* (Recherche 20). Das ist die sichere Seite, wenn das Zimmer später Kinder- oder Gästezimmer wird. Der typische Dialog („Schreibtisch in die Wohnzimmerecke, drei Tage Homeoffice“) folgt dem Muster von Kasten 9b.1: Meldung zur fehlenden Trennung, Aktionen [Nische mit Schiebetür] · [Gästezimmer als Arbeitszimmer] · [So lassen], Warum-Text mit B-W und dem Hinweis auf die Flächenfolge.

## 9b.10 Grenzen und Zwischenfazit

**Grenzen.** Erstens ist die Evidenz für das bayerische Einfamilienhaus im Holzrahmenbau fast immer indirekt: kleine Stichproben, Studierende, Bildreize, Geschosswohnungen; zu Nutzerperspektiven in vorgefertigten Holzgebäuden ist die Studienlage dünn [@campagna2025usercentered]. Zweitens ist nicht belegt, dass die Assistenz zu besseren Häusern führt; Kapitel 20 prüft das. Drittens sind die WBS-Punktelogik für fünf Kriterien, die Aussichtsstufen der EN 17037 (Recherche 15: 14°, 28°, 54°) und die Einstufung von Feuchte und Feldern offen [U]. Viertens sind Evidenzgrade begründete Urteile; die doppelte Vergabe (9b.2.4) ist die Antwort darauf.

**Zwischenfazit.** Das Kapitel präzisiert Prinzip 8 in vier Punkten:

1. **Empfehlungen sind eine eigene Regelklasse.** R5 unterscheidet sich von R1–R4 durch die Geltung: Sie blockiert nie, trägt einen Evidenzgrad und wird als gewichteter Soft Constraint berechnet. Status N und Evidenzgrad sind unabhängig.
2. **Belastbare Wirkungsevidenz gibt es nur für wenige Faktoren.** Lärm, Radon und Schadstoffe (A) sowie Tageslicht, zirkadianes Licht, Außenbezug, Beengtheit, Überhitzung und Zugänglichkeit (B) tragen die Assistenz. Bettposition, Raumhöhe und Kurven sind Präferenzen, Prospect-Refuge im Innenraum ist nur C-P.
3. **Wohnqualität ist ein Profil, kein Wert.** WBS-lite, Space Syntax und Isovisten machen Grundrissqualität rechenbar; ausgegeben werden sieben Dimensionen und die Pareto-Menge.
4. **Kulturprofile sind Wahl, nicht Wissen.** Feng Shui und Vastu sind D mit ausgewiesenen Überschneidungen und Konflikten; die Baubiologie wird geteilt, Erdstrahlen stehen auf der Ausschlussliste.

## 9b.11 Umsetzungsvorgaben für die App

### 9b.11.1 Anforderungen

| ID | Prio | Beschreibung | Beleg | Abnahmekriterium |
|---|---|---|---|---|
| ANF-09b-01 | Muss | R5-Regeln blockieren nie Speichern, Export oder Freigabe. | 9b.1.1 | Testmodell mit allen R5-Regeln bei $s_i = 0$ und erfüllten R1–R4 lässt sich speichern, exportieren und zur Freigabe senden. |
| ANF-09b-02 | Muss | Der Katalog wird aus `empfehlungen.yaml` geladen und beim Start validiert. | 9b.1.2 | Validator meldet bei fehlendem Pflichtfeld, unbekanntem Quellen-Key, unbekanntem Verweis oder P-Regel mit Grad A einen Fehler; der Katalog v0.1.0 besteht ohne Fehler. |
| ANF-09b-03 | Muss | Jede Meldung zeigt Evidenzhinweis in Laiensprache und im Warum-Teil mindestens eine Quelle. | 9b.2.1 | UI-Test über alle Regeln: Laientext des Grades sichtbar, ≥ 1 Quelle im Warum-Teil. |
| ANF-09b-04 | Muss | Fehlende Eingangsdaten ergeben „nicht bewertbar“, nicht 0; die Abdeckung je Dimension wird angezeigt. | 9b.1.1 | Modell ohne Nordwinkel: R5-AUSSEN-02 = nicht bewertbar, $S_d$ ohne diese Regel, Abdeckung < 100 %. |
| ANF-09b-05 | Muss | Ausgabe als Profil mit sieben Dimensionen; kein Gesamtscore in UI und API. | 9b.5.3 | API-Schema enthält kein aggregiertes Feld; UI zeigt Netzdiagramm mit sieben Achsen. |
| ANF-09b-06 | Muss | Pareto-Vergleich von bis zu fünf Varianten; dominierte Varianten werden markiert. | 9b.5.3 | Testfall mit drei Varianten und bekannter Pareto-Menge liefert genau diese Menge. |
| ANF-09b-07 | Muss | Kulturprofile sind standardmäßig aus; ihr Teilscore $K_p$ beeinflusst $\mathbf{S}$ nicht. | 9b.6.1 | Ein- und Ausschalten eines Profils lässt $\mathbf{S}(x)$ bitgleich. |
| ANF-09b-08 | Muss | Themen der Ausschlussliste werden nicht bewertet; auf Anfrage erscheint der Erklärtext. | 9b.6.5 | Intent „Erdstrahlen prüfen“ liefert Meldung X-02; keine Regel wird ausgeführt. |
| ANF-09b-09 | Muss | Meldungen stammen aus dem Katalog; verbotene Wendungen je Evidenzart sind ausgeschlossen. | 9b.2.3, 9b.7.3 | Automatischer Test über alle Meldungen gegen `textregeln`: 0 Treffer; kein Meldungstext wird zur Laufzeit von einem Sprachmodell erzeugt. |
| ANF-09b-10 | Muss | Jede angezeigte Empfehlung wird mit `id@version`, Text, Kundenentscheidung, Zeitstempel und IFC-GUID protokolliert. | 9b.7.4 | Protokollexport enthält für jeden angezeigten Hinweis einen vollständigen Eintrag. |
| ANF-09b-11 | Muss | Voreinstellungen aus R5 sind als solche gekennzeichnet und mit einem Klick änderbar. | 9b.7.4 | UI-Test: Kennzeichnung sichtbar, Änderung mit einer Aktion möglich. |
| ANF-09b-12 | Muss | Konflikte zwischen Regeln (auch Kulturregel gegen R5) werden gemeinsam angezeigt. | 9b.6.3 | Vastu-Profil mit Südwestschlafzimmer zeigt VA-04 zusammen mit R5-KLIMA-01. |
| ANF-09b-13 | Muss | Das Geburtsdatum für die Kua-Zahl wird nicht gespeichert. | 9b.7.5 | Nach Berechnung enthält keine Datenbanktabelle und kein Log das Datum. |
| ANF-09b-14 | Soll | Höchstens drei Hinweise je Entwurfsschritt, priorisiert nach $w_i (1 - s_i)$. | 9b.7.2 | Testschritt mit fünf verletzten Regeln zeigt die drei mit höchstem Produkt. |
| ANF-09b-15 | Soll | P-Regeln lassen sich vom Kunden aussetzen; W-Regeln bleiben als Hinweis. | 9b.3.3 | Aussetzen von R5-FUNKTION-02 entfernt sie aus $S_d$; R5-RUHE-01 ist nicht aussetzbar. |
| ANF-09b-16 | Soll | Kontrastfragen („Warum X und nicht Y?“) werden mit höchstens drei Gründen beantwortet. | 9b.7.3 | Frage „Warum Ost und nicht West?“ liefert ≤ 3 Gründe mit Grad und Quelle. |
| ANF-09b-17 | Soll | Nutzerprofile aktivieren ihre Regeln (Homeoffice, barrierefrei vorbereitet, Kinder). | 9b.9 | Profil „Homeoffice“ aktiviert R5-LICHT-04, R5-HOME-01, R5-HOME-02. |
| ANF-09b-18 | Soll | Gewichte $g$ und Schwellen sind Konfiguration, nicht Code; jede Änderung erhöht die Katalogversion. | 9b.2.4, 9b.5.4 | Änderung von $g(\mathrm{B})$ in der Datei wirkt ohne Neubau; Protokoll nennt die neue Version. |

### 9b.11.2 Empfehlungskatalog

Der Katalog `spezifikation/empfehlungen.yaml` enthält in Version 0.1.0 44 Regeln: 29 evidenzbasierte (3 × A-W, 9 × B-W, 2 × B-P, 14 × C-W, 1 × C-P) sowie 15 Regeln der Kulturprofile Feng Shui (7), Vastu (4), Baubiologie (3, davon zwei Verweise auf die evidenzbasierten Regeln zu Radon und Schadstoffen) und Hygge (1). Hinzu kommen die Ausschlussliste (X-01, X-02), die Gewichte $g$, die sieben Dimensionen plus Kultur, die Nutzerprofile und die `textregeln`. Jede Regel nennt Kennzahl mit Berechnungsvorschrift und Einheit, Schwellen, Erfüllungsfunktion, Meldungstext mit Evidenzhinweis und Quellen-Keys. Schwellen, die Designentscheidungen sind, tragen `status: U` und sind vor dem Produktivbetrieb zu bestätigen; das betrifft vor allem die Parameter der Kulturprofile, die mit Praktikern abzustimmen sind.

**YAML-Prüfung (Python, 27.09.2026):** Der Katalog wurde mit PyYAML geladen und geprüft auf Pflichtfelder, eindeutige IDs, Evidenzgrad A–D, Präferenz höchstens B, Profilmuster `evidenzbasiert` bzw. `kulturprofil:<name>`, gültige Dimensionen und Nutzerprofile, existierende Quellen-Keys in `lit-*.bib`, auflösbare Verweise und symmetrische Konflikte, verbotene Wendungen und vorhandenen Evidenzhinweis in jedem Meldungstext. Ergebnis: **0 Fehler**.

---

## Verwendete Keys

abdalhamid2023quantifying, aiact2024, air2016formaldehyd, alexander1977pattern, ali2013critiquing, altman1975environment, amerio2020covid, appleton1975experience, appleton1984prospects, aries2015daylight, bafna2003space, bartels2021impact, basner2014noise, baybo2026, benedikt1979take, bfs2025radon, bodin2015quiet, bonin2023goodnight, boumova2016apartment, bourassa1999hedonic, brown2020melanopic, brown2022recommendations, browning2014patterns, bwo2015wbs, cain2020evening, cajochen2022evening, campagna2025usercentered, chakrabarti1998vastu, chen2026critiquecrew, chuquichambi2022curvature, coburn2017buildings, cohen1960coefficient, dawes2017pattern, dgnb2023soc, din1946-6, din2019tageslicht, din4108-2, din5034-1, dosen2013methodological, dosen2016prospect, elliot2014color, emmitt2023bedroom, enright1995dowsing, erculiani2019layout, evans1998crowding, evans2003built, evans2006child, faller2002wohngrundriss, femenias2020adaptable, fischer1989environments, fischer1991critiquing, fischer1993critics, flade2006wohnen, fornara2022space, fortin2014superstition, gann2003design, graham2015psychology, gregor1999explanations, guyatt2008grade, hanson1998decoding, haubl2000decisionaids, heckmann2017grundrissatlas, herthogs2019saga, higueratrujillo2021cognitive, hildebrand1999origins, hillier1984social, hong2016fengshui, houser2020humancentric, hwang2018window, ibn2018leitlinien, iwbi2020wellv2, jakesch2023cowriting, johnson2012beyond, joye2018broken, kaplan1995restorative, ko2020window, koren1994wabisabi, kremerpreiss2011wohnenalter, lan2017thermal, landis1977measurement, lbs2020wohnwuensche, li2020qualitative, lin2012fengshui, linnet2011hygge, maes2024sbm, maier2022nudging, mak2005fengshui, marquardt2011wayfinding, merrell2011interactive, mertens2022nudging, meseguer2006soft, meyerslevy2007ceiling, miller2019explanation, neufert2022bauentwurfslehre, neumann2022homeoffice, oh2008critiquing, oh2010furniture, ohly2016attention, ohrstrom2006quietness, ostwald2011mathematics, oswald2007housing, oxman1990prior, patra2009vaastu, peng2012concern, poldrack2006reverse, preiser1988poe, prpj2022fengshui, qng2023anlage3, rambow2000expertenlaien, rewatkar2026data, roswall2020nighttime, silverman1992critiquing, silverman1992expert, spoerrle2010sleeping, stamps2006interior, stamps2008some, tam1999fengshui, thaler2008nudge, turner2001isovists, ulrich1984view, vartanian2013contour, vartanian2015ceiling, walden2008architekturpsychologie, wang2007recommendation, wang2022embodiment, wegener2024funktionswandel, west2004functional, who2018noise, wiener2007isovist, wilms2018color, xiao2021wfh, zahedi2022bim, zhong2022biophilic

**Key-Prüfung (Python, 27.09.2026):** Alle `[@key]`-Zitate im Text wurden per regulärem Ausdruck extrahiert und gegen die Keys aller `literatur/lit-*.bib` (1087 Keys) abgeglichen. Ergebnis: 204 Zitatstellen, 133 verschiedene Keys, **0 fehlende Keys**. Die 58 Quellen-Keys des Empfehlungskatalogs sind ebenfalls vollständig in `lit-*.bib` enthalten.

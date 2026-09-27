# 7a Nachweisführung: rechnerisch und grafisch

Status: Entwurf v0.1 (27.09.2026). Befunde tragen [V] (an der Primärquelle geprüft) oder [U] (nicht an der Primärquelle geprüft). Das lauffähige Artefakt ist `beispiele/nachweis.py`, beschrieben in `beispiele/NACHWEIS.md`. Keine Rechts- oder Normauskunft.

## 7a.0 Einordnung

Ein regelbasierter Hausplaner trifft laufend Entscheidungen der Form „zulässig“ oder „nicht zulässig“. Beispiele sind eine Abstandsfläche, ein U-Wert, ein Treppenmaß oder eine IDS-Anforderung. Solange diese Entscheidungen nur im Code stehen, kann sie niemand außerhalb des Entwicklerteams prüfen. Deshalb gilt für diese Arbeit ein Grundsatz: **Jede Regelprüfung und jede Berechnung muss rechnerisch und grafisch nachweisbar sein.** Ein Prüfingenieur, eine Behörde oder ein Gutachter soll den Nachweis nachvollziehen können, ohne den Code zu lesen.

Dieses Kapitel leitet die Anforderungen an einen solchen Nachweis aus Bauordnungsrecht, Metrologie und Softwarepraxis ab (7a.1–7a.2). Daraus entsteht ein Datenmodell (7a.3), eine Darstellung für Grafiken (7a.4) und ein Konzept für Nachweisheft und Rückverfolgbarkeit (7a.5). Abschnitt 7a.6 demonstriert das Konzept an den Beispielen B1–B5, Abschnitt 7a.7 benennt die Grenzen.

## 7a.1 Anforderungen an prüffähige Nachweise

### Was das Bauordnungsrecht verlangt

Das Bauordnungsrecht sagt nicht, *wie* ein Nachweis aussehen muss. Es sagt aber, *was* geprüft wird und *welche* Unterlagen dazu gehören. Drei Befunde sind für die Formalisierung entscheidend.

1. **Prüfmaßstab.** Nach der Muster-Verordnung über die Prüfingenieure und Prüfsachverständigen prüfen Prüfingenieure und Prüfsachverständige für Standsicherheit „die Vollständigkeit und Richtigkeit der Standsicherheitsnachweise“ [@mppvo2012]. Für den Brandschutz gilt dieselbe Formel. Beide Sätze stehen in den Vorschriften zur „Aufgabenerledigung“ [V, Wortlaut; Paragrafen- und Absatznummer je Fassung 2006, 2008 und 2012 U]. Für Bayern regelt das die BayPrüfVBau; ihr Primärtext war aus der Arbeitsumgebung nicht erreichbar [U]. „Vollständig“ und „richtig“ sind damit die beiden Kriterien, an denen sich ein maschinell erzeugter Nachweis messen lassen muss.
2. **Inhalt der Bauvorlage.** Die bayerische Bauvorlagenverordnung verlangt für den Standsicherheitsnachweis „eine Darstellung des gesamten statischen Systems sowie die erforderlichen Konstruktionszeichnungen, Berechnungen und Beschreibungen“ (§ 10 Abs. 1 BauVorlV) [@bauvorlv] [V]. Die Musterbauvorlagenverordnung enthält denselben Wortlaut [@mbauvorlv2020] [V]. Rechnung, Zeichnung und Beschreibung stehen also gleichrangig nebeneinander. Die ältere Musterfassung verlangte zusätzlich ausdrücklich: „Berechnungen und Zeichnungen müssen übereinstimmen und gleiche Positionsangaben haben“ [@mbauvorlv1996] [V, historische Fassung]. Heute übernimmt das Übereinstimmungsgebot in § 13 BauVorlV diese Rolle (vgl. Kapitel 4).
3. **Grafische Mindestinhalte.** Der Lageplan muss unter anderem „den Maßstab und die Nordrichtung“ sowie „die Abstandsflächen der geplanten baulichen Anlagen“ enthalten. Sein Maßstab darf nicht kleiner als 1 : 1000 sein (§ 7 Abs. 2 und 3 Nr. 1 und 13 BauVorlV) [@bauvorlv] [V]. Für einen grafischen Abstandsflächennachweis sind Maßstab, Nordpfeil und dargestellte Abstandsflächen damit keine Gestaltungsfrage, sondern Pflichtinhalt.

Eine allgemeine Legaldefinition von „prüffähig“ für bautechnische Nachweise wurde in den geprüften Texten nicht gefunden. Der Begriff wird in dieser Arbeit deshalb **operational** bestimmt: Ein Nachweis ist prüffähig, wenn ein fachkundiger Dritter Vollständigkeit und Richtigkeit allein anhand des Dokuments beurteilen kann.

### Was die Metrologie verlangt

Für den Bericht über ein Messergebnis gibt der Leitfaden zur Angabe der Messunsicherheit (GUM) einen Prüfstein, der sich auf Berechnungen übertragen lässt [@jcgm100] [V]. Nach Abschnitt 7.1.4 soll man:

- die Methoden klar beschreiben, mit denen Ergebnis und Unsicherheit berechnet werden,
- alle Unsicherheitskomponenten auflisten,
- die Analyse so darstellen, dass jeder wichtige Schritt verfolgt und die Rechnung unabhängig wiederholt werden kann,
- alle Korrekturen und Konstanten mit Quelle angeben.

Der Test dafür lautet: Habe ich genug Information so klar angegeben, dass das Ergebnis später aktualisiert werden kann, wenn neue Daten vorliegen? Abschnitt 7.2.7 ergänzt: Anzugeben sind jeder Eingangswert mit Herkunft, die Funktion *Y = f(X₁, …, X_N)* und, wo nützlich, die Sensitivitätskoeffizienten. Ist *f* nur als Programm vorhanden, muss klar sein, wie Ergebnis und Unsicherheit entstanden sind [V].

### Was die Softwarepraxis verlangt

Rechnet ein Programm, gehört das Programm selbst zur Nachweiskette. Die Software Citation Principles fordern unter „Specificity“, die *konkret verwendete Version* einer Software identifizierbar zu machen [@smith2016softwarecitation] [V]. Die FAIR-Prinzipien für Forschungssoftware übertragen Auffindbarkeit, Zugänglichkeit, Interoperabilität und Wiederverwendbarkeit auf Software [@barker2022fair4rs] [V].

### Anforderungskatalog

Aus den drei Quellen folgen acht Anforderungen an jeden Nachweis des Systems:

| Nr. | Anforderung | Herleitung |
|---|---|---|
| A1 | Regel mit Quelle, **Fassung** und Fundstelle | Vollständigkeit; Regeln sind zeitabhängig (Kap. 4) |
| A2 | Gegenstand eindeutig, mit IFC-GlobalId | „gleiche Positionsangaben“; Rückverfolgbarkeit ins Modell |
| A3 | jede Eingangsgröße mit Wert, Einheit, Quelle und Art (Eingabe, Annahme, Konstante, Grenzwert) | GUM 7.1.4 d, 7.2.7 a |
| A4 | jeder Rechenschritt mit Formel, eingesetzten Werten und Normverweis | GUM 7.1.4 c, 7.2.7 d |
| A5 | Vergleich mit dem Grenzwert, Ausnutzung und Status; Annahmen getrennt ausgewiesen | Richtigkeit, Nachvollziehbarkeit |
| A6 | Angaberegeln für Zahlen: Rundung, Einheiten, Unsicherheit | ISO 80000-1, DIN 1333, GUM |
| A7 | grafischer Nachweis mit Maßstab, Nordpfeil, Legende und Bemaßung, wo das Recht es verlangt | § 7, § 10 BauVorlV |
| A8 | Reproduzierbarkeit und Unverfälschtheit: Software-Version, deterministische Ausgabe, Prüfsumme | Software Citation, FAIR4RS |

## 7a.2 Größen, Einheiten, Rundung und Unsicherheit

### Größen und Einheiten

Eine physikalische Größe ist das Produkt aus Zahlenwert und Einheit (DIN 1313, ISO 80000-1) [@din1313; @iso80000-1] [U für DIN 1313]. Für einen Nachweis folgt daraus: Eine Zahl ohne Einheit ist kein Nachweiswert. Das Framework rechnet deshalb jeden Schritt mit Größen und nicht mit Zahlen. Die Bibliothek `pint` prüft die Dimensionen; fehlt sie, übernimmt eine eigene Prüfung mit den sieben Basisdimensionen des SI. Zwei typische Fehlerklassen werden dadurch vor dem Ergebnis erkannt:

- **Unverträgliche Operationen**, etwa die Addition einer Dicke in mm zu einer Wärmeleitfähigkeit.
- **Falsch deklarierte Ergebnisse**, etwa ein Wärmedurchlasswiderstand, der als U-Wert ausgegeben wird.

Ein Nebeneffekt ist fachlich wichtig: Die Umrechnung von mm in m geschieht nicht mehr von Hand. Im Rechenkern von B3 steht `d = s["dicke"] / 1000.0`. Im Nachweis steht `R = d/λ` mit *d* in mm, und das Ergebnis erscheint korrekt in m²·K/W. Bei Nachrechnungen ist die häufigste Fehlerquelle damit strukturell ausgeschlossen.

### Rundung: Rechnen ungerundet, Anzeigen gerundet

ISO 80000-1:2022 regelt das Runden im normativen Anhang B [@iso80000-1] [V]:

- Gerundet wird auf ein ganzzahliges Vielfaches eines gewählten Rundungsbereichs.
- Liegen zwei Vielfache gleich nahe, gibt es zwei Regeln. Regel A wählt das gerade Vielfache, Regel B das betragsmäßig größere. Regel A wird allgemein bevorzugt, Regel B ist in Rechnern verbreitet (B.3).
- Gerundet wird in **einem** Schritt: 12,254 wird zu 12,3 und nicht über 12,25 zu 12,2 (B.4).
- Wo Sicherheitsanforderungen oder Grenzwerte einzuhalten sind, ist nur in eine Richtung zu runden (B.5).
- Der Rundungsbereich ist stets anzugeben (B.6).

DIN 1333 behandelt das Runden in Abschnitt 4 und die Ergebniswerte mit Unsicherheit in Abschnitt 6 [@din1333] [V, Inhaltsverzeichnis]. Nach Sekundärquellen gilt: Die Rundestelle richtet sich nach der ersten von null verschiedenen Ziffer der Unsicherheit. Ist sie 3 bis 9, ist sie selbst die Rundestelle, bei 1 oder 2 die Stelle rechts daneben. Die Unsicherheit wird dort aufgerundet [U]. Der GUM empfiehlt ebenfalls höchstens zwei signifikante Stellen für die Unsicherheit und eine dazu passende Rundung des Ergebnisses (7.2.6). Zusätzliche Stellen erlaubt er, wenn Folgerechnungen sonst Rundungsfehler aufsammeln [@jcgm100] [V].

Für den Wärmeschutz gibt DIN EN ISO 6946 fachspezifische Angaberegeln vor [@iso6946_2017] [V]:

- Ein U-Wert als Endergebnis ist auf **zwei signifikante Stellen** zu runden, und die Eingangsdaten sind anzugeben (6.5.2).
- Ein Wärmedurchlasswiderstand als Endergebnis erhält zwei Dezimalstellen (6.6).
- Zwischenwerte von Wärmedurchlasswiderständen sind mit mindestens drei Dezimalstellen zu rechnen (6.7.1.1).

Das Framework setzt diese Regeln um. Jede Größe kann eine eigene Anzeigeregel tragen, bestehend aus Art, Stellenzahl, Verfahren (Regel A, Regel B, auf, ab) und Begründung. Gerechnet und verglichen wird ungerundet. Der Bericht nennt die Regel jeweils im Klartext. Außerdem prüft das Framework die **Rundungsempfindlichkeit**: Würde der gerundete Anzeigewert anders entscheiden als der ungerundete, erscheint ein Hinweis. Ein Beispiel ist U = 0,2049 W/(m²·K). Angezeigt als „0,20“, sähe der Wert gegenüber U_max = 0,20 erfüllt aus, ist es aber nicht. Der Fall ist als Test hinterlegt.

### Unsicherheit

Der GUM pflanzt Unsicherheiten linear fort: $u_c^2(y) = \sum_i (\partial f/\partial x_i)^2\,u^2(x_i)$ für unkorrelierte Eingänge (5.1.2, Gl. 10). Die partiellen Ableitungen heißen Sensitivitätskoeffizienten (5.1.3). Die erweiterte Unsicherheit ist U = k·u_c. Bei annähernd normalverteiltem Ergebnis ergibt k = 2 ein Intervall mit einem Vertrauensniveau von etwa 95 % (6.2.1, 6.3.3) [@jcgm100] [V]. Supplement 1 (JCGM 101:2008) ersetzt die Linearisierung durch eine Monte-Carlo-Fortpflanzung der Verteilungen [@jcgm101] [V].

Das Framework bildet die Ableitungen numerisch durch zentrale Differenzen, und zwar **über die gesamte Rechenkette** statt Schritt für Schritt. Der Unterschied ist nicht akademisch. Gehen oberer und unterer Grenzwert von R_T in B3 beide auf dasselbe λ zurück, sind sie korreliert. Eine schrittweise Fortpflanzung würde diese Korrelation übersehen. Ein Test belegt das Verhalten: Für y = z + x mit z = x liefert das Framework u(y) = 2·u(x) und nicht √2·u(x). Optional läuft eine Monte-Carlo-Fortpflanzung mit festem Seed. Der Bericht enthält das vollständige Unsicherheitsbudget mit Beitrag und Anteil jeder Eingangsgröße.

Liegt der Abstand zum Grenzwert innerhalb von U, gibt das Framework einen Hinweis aus: Die Konformitätsaussage ist dann unsicher. Die Regeln des JCGM 106:2012 zur Konformitätsbewertung sind nicht am Text geprüft [U]. Wichtig für die Einordnung: Bemessungswerte nach DIN EN ISO 10456 enthalten ihre Sicherheitsüberlegungen bereits. Die Unsicherheitsangabe ergänzt den Nachweis, sie ersetzt keine normative Sicherheitsregel. In B1 und B3 sind die Unsicherheiten ausdrücklich als Annahmen zur Demonstration gekennzeichnet.

## 7a.3 Datenmodell des Nachweises

Das Datenmodell bildet die Anforderungen A1–A8 direkt ab (Tabelle; JSON-Schema `nachweis.schema.json`, Draft 2020-12):

| Element | Inhalt | Anforderung |
|---|---|---|
| `regel` | Text, Quelle, Fassung, Fundstelle, [V]/[U], Regelwerk-Profil und Version | A1 |
| `gegenstand` | Bezeichnung, IFC-GlobalId, IFC-Klasse, IFC-Datei mit SHA-256, weitere GUIDs | A2 |
| `eingaben[]` | Größe mit Name, Symbol, Wert, Einheit, Dimension, Quelle, Art, Standardunsicherheit, Verteilung | A3 |
| `schritte[]` | Beschreibung, maschinenlesbarer Ausdruck, Formel in LaTeX, eingesetzte Werte, Normverweis, Ergebnis; alternativ Verfahren mit Werkzeug und Version | A4 |
| `kriterien[]` | Ist, Vergleich, Grenzwert, Toleranz, Ausnutzung η, erfüllt, Rundungsempfindlichkeit, Lage zur Unsicherheit | A5 |
| `status`, `ausnutzung` | erfüllt / nicht erfüllt / Hinweis; maßgebendes Kriterium | A5 |
| `annahmen[]`, `hinweise[]` | getrennt vom Rechengang | A5 |
| `unsicherheit`, `gegenrechnungen` | GUM-Budget, Monte-Carlo; Vergleich mit dem Rechenkern | A6, A8 |
| `grafiken[]` | SVG mit Prüfsumme, Art, Maßstab | A7 |
| `umgebung`, `hash`, `zeitstempel` | Software-Versionen, SHA-256, optionaler Zeitstempel | A8 |

Zwei Entwurfsentscheidungen verdienen eine Begründung.

**Ausdruck und Formel aus einer Quelle.** Jeder Rechenschritt trägt einen Ausdruck in einer sicheren Teilmenge von Python. Er erlaubt Grundrechenarten, Potenzen und wenige Funktionen wie `min`, `max`, `tan`, `ceil`. Das Framework wertet ihn über den Syntaxbaum aus, nicht mit `eval`. Aus demselben Syntaxbaum entstehen die LaTeX-Formel und die Zeile mit den eingesetzten Werten. Formel, Einsetzung und Ergebnis können deshalb nicht auseinanderlaufen, wie es bei handgeschriebenen Berichten vorkommt. Ein Dritter kann den Nachweis aus dem JSON ohne den Quellcode nachrechnen.

**Verfahrensschritte statt Scheinformeln.** Manche Schritte haben keine geschlossene Formel: die Verschneidung einer Abstandsfläche mit dem Grundstück, die vollständige Aufzählung von Treppenlösungen oder eine IDS-Prüfung. Das Framework erfindet dafür keine Formel. Es beschreibt das Verfahren mit Werkzeug und Version, zum Beispiel „shapely 2.1.2, Polygon.difference“ oder „ifctester 0.8.5“, und übernimmt dessen Ergebnis. Die Unsicherheitsrechnung weist aus, dass solche Schritte nicht fortgepflanzt sind.

**Gegenrechnung.** Die Nachweisschicht liegt über den bestehenden Rechenkernen. Sie rechnet die Formelkette aus den offengelegten Eingaben selbst und vergleicht das Ergebnis mit dem Rechenkern innerhalb einer angegebenen Toleranz. Das entspricht einer Vergleichsrechnung, wie sie ein Prüfingenieur stichprobenhaft ausführt. Hier läuft sie bei jedem Lauf vollständig.

## 7a.4 Grafische Nachweise

Grafiken erfüllen im Nachweis zwei Aufgaben: Sie zeigen den geometrischen Sachverhalt, etwa Lageplan, Schnitt oder Ansicht, und sie zeigen das Prüfergebnis, etwa Ist gegen Grenzwert. Für die Bauzeichnung gelten DIN 1356-1 (Bauzeichnungen) und die Normenreihe ISO 128 (technische Produktdokumentation, allgemeine Darstellungsregeln). Hinzu kommen die Regeln zur Maßeintragung (DIN 406) [@din1356-1; @iso128-1] [U, Normtexte nicht eingesehen]. Das Framework übernimmt davon, was sich ohne Normtext belastbar begründen lässt:

- **Maßstäblichkeit.** Technische Zeichnungen werden als reines SVG erzeugt. Breite und Höhe sind in Millimetern angegeben, Modellkoordinaten werden über den Maßstab auf Papier-Millimeter abgebildet. Beim Druck in 100 % ist die Zeichnung maßhaltig. Der Lageplan in B4 hat den Maßstab 1 : 200 und liegt damit innerhalb der Grenze des § 7 Abs. 2 BauVorlV.
- **Pflichtinhalte.** Der Lageplan enthält Maßstabsleiste, Nordpfeil, Legende und Schriftfeld, dazu Grenzabstände und Abstandsflächentiefen. Zulässige Abstandsflächen erscheinen grün, unzulässige rot. Die Unterscheidung hängt nie nur an der Farbe, denn Legende und Tabelle tragen denselben Befund.
- **Zeichenregeln.** Linienbreiten 0,25/0,35/0,5/0,7 mm und Schrifthöhen 2,5/3,5 mm; im Bauwesen als Schrägstrich ausgeführte Maßbegrenzung; Maßzahlen lesbar von unten oder rechts; Schraffuren je Baustoff im Schnitt. Diese Regeln sind an DIN 1356-1, ISO 128 und ISO 3098 angelehnt. Normtreue wird nicht behauptet [U].
- **Diagramme** entstehen mit matplotlib, wenn es installiert ist, sonst als reines SVG. Datum und Zufallskennungen sind aus der Ausgabe entfernt, die Achsen haben Dezimalkomma. Status wird nie nur durch Farbe codiert: Die Beschriftung „erfüllt“ oder „nicht erfüllt“ steht am Balken.

Jede Grafik geht über ihren SVG-Text in den Hash des Nachweises ein. Ändert sich eine Zeichnung, ändert sich der Hash.

## 7a.5 Nachweisheft, Hash und Rückverfolgbarkeit

Mehrere Nachweise werden zu einem **Nachweisheft** gebündelt. Es enthält:

- ein Deckblatt mit Projekt, Verfasser, Gesamtergebnis, Regelwerk-Profilen mit Versionen, Regelquellen mit [V]/[U] und Heft-Hash,
- ein Inhaltsverzeichnis mit Status, Ausnutzung und Hash-Anfang je Nachweis,
- die Nachweise selbst.

Das Heft wird als JSON, Markdown und HTML geschrieben. Das HTML hat ein Druck-Stylesheet für A4 mit einem Seitenumbruch je Nachweis.

**Rückverfolgbarkeit in drei Richtungen:**

1. **Zum Modell:** Der Gegenstand verweist auf die IFC-GlobalId und auf die SHA-256-Prüfsumme der IFC-Datei. Die deterministischen GUIDs aus B1 (Kapitel 7.3) machen den Verweis über Modelländerungen hinweg stabil. Ein Ständer behält seine GUID, wenn sich an anderer Stelle der Wand etwas ändert. Bei IDS-Nachweisen nennt der Befund jedes fehlerhafte Element mit GUID.
2. **Zur Regel:** Jede Regel nennt Quelle, Fassung, Fundstelle sowie Regelwerk-Profil und Version (Kapitel 4, Abschnitt Versionierung). Wie wichtig die Fassung ist, zeigt die eigene Literaturdatenbank. Das GModG verweist in § 20 Abs. 6 **datiert** auf DIN EN ISO 6946:2008-04, B3 rechnet dagegen nach der Ausgabe 2018-03 [@iso6946]. Ohne Fassungsangabe wäre nicht erkennbar, welche Ausgabe ein Nachweis anwendet. Dass die Angaberegel „zwei signifikante Stellen“ bereits in der Ausgabe 2008 steht, ist nicht geprüft [U].
3. **Zur Software:** Der Block `umgebung` nennt die Versionen von Python, Modul und Paketen sowie die Einheiten- und Grafik-Backends. Er erfüllt damit die Forderung nach Spezifität der Software Citation Principles.

**Hash.** Der Hash ist SHA-256 über das kanonische JSON des Nachweises: sortierte Schlüssel, keine Leerzeichen, UTF-8. Das Vorgehen ist an RFC 8785 angelehnt, ohne dessen Zahlenformat vollständig umzusetzen [U]. Zeitstempel und Umgebung sind ausgenommen. Der Hash identifiziert damit die **fachliche Aussage** und nicht den Zeitpunkt oder die Maschine. Ein Zeitstempel wird nur gesetzt, wenn er übergeben wird oder die Umgebungsvariable `SOURCE_DATE_EPOCH` gesetzt ist. Ohne diese Angaben ist jeder Lauf byte-identisch. Der Heft-Hash bildet sich aus Titel, Projekt und der geordneten Liste der Nachweis-Hashes.

**Befund zur Hash-Stabilität.** In einem Vergleich wurden alle 32 Nachweise B1–B5 einmal mit pint und einmal mit der eigenen Dimensionsprüfung erzeugt. Zunächst stimmten nur 27 von 32 Hashes überein, obwohl alle Werte bis auf 1,8 · 10⁻¹⁵ relativ gleich waren. Die Ursachen waren zweierlei:

- ungerundete Zwischenwerte in Anzeigetexten,
- Differenzen fast gleicher Zahlen in der Gegenrechnung (Auslöschung).

Nach zwei Korrekturen stimmen alle 32 Hashes überein: Gleitkommazahlen gehen mit 12 signifikanten Stellen in den Hash ein, und Abweichungen werden auf drei Stellen gespeichert. Die Lehre daraus: Ein Inhalts-Hash für numerische Nachweise braucht eine definierte **Zahlen-Normalform**. Sonst misst er Rechenreihenfolgen statt Inhalte.

Der Hash belegt Unverändertheit, aber keine Urheberschaft. Eine qualifizierte elektronische Signatur und der Prüfvermerk einer berechtigten Person sind eigene Schritte. Sie gehören zu den Verantwortungsregeln R3 (Kapitel 4) und sind nicht Teil des Frameworks.

## 7a.6 Demonstration an den Beispielen B1–B5

Das Framework wurde an die fünf vorhandenen Beispiele nachgerüstet, ohne deren Rechenkerne zu ändern. Die 48 bestehenden Tests bleiben grün, 50 neue Tests kommen hinzu. Es entstehen sieben Nachweishefte mit insgesamt 32 Nachweisen und 46 Grafiken (`beispiele/ausgabe/nachweise/`).

| Beispiel | Nachweis | Ergebnis | Grafik |
|---|---|---|---|
| B1 Wandelement | Flächen, Volumen, Massen je Baustoff; Volumen gleich IFC-Mengen (Abweichung ≤ 4,4 · 10⁻¹⁶ m³) | m = 650 ± 70 kg (k = 2), Monte-Carlo 95 %: 587–707 kg; Rohdichten als Annahmen | Wandansicht 1 : 50, Massendiagramm |
| B2 IDS | je Spezifikation: Kardinalität und Verstöße | bestanden 11/11; fehlerhaft genau HRB-01, 03, 05, 08, 09, 11, jeweils mit GUID; Status in 22 von 22 Fällen gleich ifctester | Anteilsbalken |
| B3 U-Wert | ISO 6946 in 16 Schritten, oberer und unterer Grenzwert, e = 4,0 % | U = 0,19 W/(m²·K) (Geometrie, verputzt); 0,187 ± 0,007 (k = 2); Monte-Carlo [0,180; 0,194]; η = 0,93 | Horizontalschnitt 1 : 5, Grenzwertdiagramm, U gegen U_max |
| B4 Abstandsflächen | H und T je Wand, T vorhanden, Fläche außerhalb | drei Szenarien zulässig; „zu_nah“: 15,20 m² außerhalb, T vorhanden 2,00 m < 3,27 m | Lageplan 1 : 200, Tiefendiagramm |
| B5 Treppe | n_min = 15, n_max = 20, 68 Lösungen, 17 × 170,6/290 | 2s + a = 631,2 mm, 7 Kriterien erfüllt, η = 0,97 | Schrittmaß-Diagramm, Treppenschnitt 1 : 50 |

Drei Beobachtungen gehen über die Einzelergebnisse hinaus.

**Angaberegeln decken Inkonsistenzen auf.** Im IFC-Modell steht der U-Wert als 0,187 W/(m²·K), also mit drei Stellen. Als Endergebnis nach ISO 6946 wäre 0,19 anzugeben. Beide Angaben sind vertretbar, wenn man sie einordnet. Der IFC-Wert ist ein Zwischenwert für Folgerechnungen; der GUM erlaubt dafür zusätzliche Stellen (7.2.6). Der Nachweis nennt die Norm-Angabe als Endergebnis und dokumentiert die Abweichung als Hinweis. Ohne explizite Rundungsregel wäre der Unterschied nicht aufgefallen.

**Das Unsicherheitsbudget zeigt, wo Genauigkeit zählt.** In B3 stammen 43 % der Varianz von U aus λ der Gefachdämmung, 21 % aus der Holzfaserdämmplatte, 17 % aus λ des Holzes und 13 % aus der Gefachdicke. Die Plattendicken tragen praktisch nichts bei. Die lineare Fortpflanzung (u_c = 0,0034 W/(m²·K)) und die Monte-Carlo-Rechnung (s = 0,0034) stimmen überein. Der Abstand zum Grenzwert von 0,20 ist größer als U, die Konformitätsaussage ist also robust. Für Kapitel 9 folgt daraus: Die Genauigkeit der Produktdaten für Dämmstoffe ist wichtiger als die der Plattendicken.

**Negative Nachweise sind gleichwertig.** Die absichtlich fehlerhaften Fälle aus B2 und B4 erzeugen vollständige Nachweise mit rotem Status, Befund, GUID und Zeichnung. Für die Ablehnung mit Begründung (Kapitel 9) ist das die Voraussetzung. Eine Ablehnung ist ebenso nachzuweisen wie eine Zustimmung.

## 7a.7 Grenzen und Zwischenfazit

Die Grenzen sind benannt:

- Die Primärtexte von BayPrüfVBau, DIN 1333, DIN 1313, DIN 1356-1, ISO 128 und JCGM 106 wurden nicht eingesehen [U].
- Die Zeichnungen folgen den Zeichenregeln sinngemäß. Nicht umgesetzt sind die Planzeichen nach Anlage 1 BauVorlV bzw. PlanZV sowie Katastergrundlage und Höhenbezug.
- Ein PDF entsteht nur über die Druckfunktion des Browsers. Eine PDF-Erzeugung ohne Systemabhängigkeiten hätte einen eigenen Formelsatz erfordert.
- Die Unsicherheitsfortpflanzung ist linear und nimmt unkorrelierte Eingänge an; Korrelationen entstehen nur über die Rechenkette.
- Für B4 und B5 fehlt noch ein IFC-Gebäudemodell und damit die GUID des Gegenstands.

Das Zwischenfazit hat drei Teile:

1. **Prüffähigkeit lässt sich operationalisieren.** Die Kriterien „Vollständigkeit und Richtigkeit“ der Prüfverordnungen und der Prüfstein des GUM ergeben einen Anforderungskatalog (A1–A8). Ein Datenmodell bildet ihn vollständig ab, und ein Schema prüft ihn maschinell.
2. **Nachweise lassen sich nachrüsten.** Eine Nachweisschicht über bestehenden Rechenkernen macht Ergebnisse prüffähig, ohne sie zu ändern. Die Gegenrechnung verbessert dabei die Qualität der Kerne, weil sie Abweichungen sofort sichtbar macht.
3. **Reproduzierbarkeit braucht Normalformen.** Byte-identische Ausgabe verlangt fünf Dinge: deterministische GUIDs, abschaltbare Zeitstempel, deterministische Grafiken, ein kanonisches JSON und eine definierte Zahlen-Normalform für den Hash. Erst dann ist die Aussage „zulässig nach Profil *P* in Version *v*“ aus Kapitel 4 mit einer Prüfsumme belegbar.

## Quellen

Schlüssel ohne Eintrag in `literatur/*.bib` sind zur Übernahme vorgesehen. [V] heißt: Wortlaut oder Inhalt wurde am 27.09.2026 an der Primärquelle oder einer amtlichen bzw. herausgebernahen Wiedergabe geprüft. [U] heißt: nicht an der Primärquelle geprüft.

- `@mppvo2012`: Bauministerkonferenz (ARGEBAU), Muster-Verordnung über die Prüfingenieure und Prüfsachverständigen nach § 85 Abs. 2 MBO (M-PPVO), Fassung Dezember 2012 mit Begründung; Fassungen März 2006 und August 2008. Wortlaut zu „Vollständigkeit und Richtigkeit“ geprüft über bvpi.de und is-argebau.de [V]. Absatzzählung je Fassung [U]. Bayerische Umsetzung BayPrüfVBau [U].
- `@bauvorlv`: Freistaat Bayern, Bauvorlagenverordnung (BauVorlV) vom 10.11.2007, §§ 7, 10, 13; gesetze-bayern.de, Text über Suchdienst-Cache abgerufen [V].
- `@mbauvorlv2020`: Bauministerkonferenz, Musterbauvorlagenverordnung (MBauVorlV), Fassung 2007, Begründung 2020, § 10 [V].
- `@mbauvorlv1996`: Bauministerkonferenz, Muster einer Verordnung über Bauvorlagen im bauaufsichtlichen Verfahren (ältere Fassung), § 5 Abs. 1 „Berechnungen und Zeichnungen müssen übereinstimmen“ [V, Jahr der Fassung U].
- `@jcgm100`: JCGM 100:2008, *Evaluation of measurement data – Guide to the expression of uncertainty in measurement* (GUM 1995 with minor corrections), BIPM; Abschnitte 5.1.2, 5.1.3, 6.2.1, 6.3.3, 7.1.4, 7.2.6, 7.2.7 [V].
- `@jcgm101`: JCGM 101:2008, *Supplement 1 to the GUM – Propagation of distributions using a Monte Carlo method*, BIPM [V, Titel und Gegenstand].
- JCGM 106:2012, *The role of measurement uncertainty in conformity assessment* [U].
- `@iso80000-1`: ISO 80000-1:2022, *Quantities and units – Part 1: General*, Anhang B „Rounding of numbers“, B.1–B.6 [V]; Abschnitt 7 zur Zifferngruppierung [U].
- `@din1333`: DIN 1333:1992-02, *Zahlenangaben*; Gliederung, Abschnitte 4 und 6 [V, Inhaltsverzeichnis]. Rundungsregel mit Unsicherheit nach Sekundärquellen (TU Chemnitz, Grundpraktikum; Wikipedia „DIN 1333“) [U].
- `@din1313`: DIN 1313:1998-12, *Größen* [U].
- `@iso6946_2017`: ISO 6946:2017 bzw. DIN EN ISO 6946:2018-03, *Bauteile – Wärmedurchlasswiderstand und Wärmedurchgangskoeffizient – Berechnungsverfahren*; 6.4, 6.5.2, 6.6, 6.7.1.1, 6.7.2.2 und Inhaltsverzeichnis über die Leseprobe des Normungsportals [V]; Absatznummern für oberen und unteren Grenzwert (6.7.2.3/6.7.2.4) [U].
- `@iso6946`: DIN EN ISO 6946:2008-04, datierter Verweis in § 20 Abs. 6 GModG (Literaturdatenbank der Arbeit) [V laut Datenbank]; Angaberegel in dieser Ausgabe [U].
- `@din1356-1`: DIN 1356-1:1995-02, *Bauzeichnungen – Teil 1: Arten, Inhalte und Grundregeln der Darstellung* [U].
- `@iso128-1`: ISO 128-1:2020 und ISO 128-2:2020, *Technical product documentation – General principles of representation*; DIN 406-11 (Maßeintragung); ISO 3098 (Schrift); DIN EN ISO 7200 (Schriftfeld) [U].
- `@smith2016softwarecitation`: Smith, A. M.; Katz, D. S.; Niemeyer, K. E.; FORCE11 Software Citation Working Group (2016): Software citation principles. *PeerJ Computer Science* 2:e86. doi:10.7717/peerj-cs.86 [V].
- `@barker2022fair4rs`: Barker, M.; Chue Hong, N. P.; Katz, D. S.; Lamprecht, A.-L.; Martinez-Ortiz, C.; Psomopoulos, F.; Harrow, J.; Castro, L. J.; Gruenpeter, M.; Martinez, P. A.; Honeyman, T. (2022): Introducing the FAIR Principles for research software. *Scientific Data* 9, 622. doi:10.1038/s41597-022-01710-x [V].
- RFC 8785, *JSON Canonicalization Scheme (JCS)*, 2020 [U]; `SOURCE_DATE_EPOCH`, reproducible-builds.org [U].
- `@ids2024`: buildingSMART International, Information Delivery Specification (IDS) 1.0 [V laut Datenbank].

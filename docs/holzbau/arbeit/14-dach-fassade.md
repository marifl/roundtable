# 14 Dach, Fassade und Einbauteile

Status: Entwurf v0.1 (27.09.2026). Befunde zu Regelwerk, Algorithmen und Datenlage; keine Ausführungsplanung. Grundlage sind Recherche 09 (`../recherche/09-dach-fassade-pv.md`), die Schneeballrunden 25 und 26 sowie die Prototypen B7, B17 und B18. Das Walmdach-Beispiel B21 ist geplant; die Zahlen dieses Kapitels zur Dachgeometrie sind eigene Rechnungen mit den Eingaben von B18 und als solche gekennzeichnet.

## 14.0 Einordnung und Vorgehen

Am Dach kreuzen sich im Entwurf eines Einfamilienhauses die meisten Regeln. Senkt der Kunde die Dachneigung von 35° auf 20°, ändern sich zugleich Abstandsfläche (Abschnitt 9.4.1), Vollgeschoss (9.4.2), Zusatzmaßnahme unter der Deckung (9.4.5), Photovoltaik (14.6) und die Dachelemente der Montage (Kapitel 14b).

Kapitel 9 hat die Dachneigung als R1-Regel formalisiert. Dieses Kapitel fragt, wie aus Grundriss, Neigung und Bemusterung ein **vollständiges Dach** mit Tragwerk, Deckung, Einbauteilen, Entwässerung und Photovoltaik entsteht, dazu die Fassade. Es beantwortet damit den Teil von FF6, der Dach und Fassade betrifft.

Drei Fragen leiten das Kapitel:

1. **Geometrie.** Welches Verfahren erzeugt aus einem beliebigen Grundrisspolygon mit Neigungen je Traufkante ein eindeutiges, entwässerndes und reproduzierbares Dach?
2. **Regelwerk.** Welche Regeln des Handwerks, des Bauordnungsrechts und der Hersteller bestimmen Deckung, Einbauteile, Photovoltaik und Fassade, und in welcher Form sind sie verfügbar?
3. **Daten.** Welche Herstellerdaten braucht ein Generator, damit Lattung, Formziegel und Einbauteile bestellbar werden, und wie werden sie maschinenlesbar?

Methodisch gilt Kapitel 4: Jede Aussage ist an der Primärquelle geprüft oder mit [U] markiert. Die ZVDH-Fachregel für Dachziegel und Dachsteine [@zvdh2024] ist kostenpflichtig. Ihre Kernwerte zu Regeldachneigung und Zusatzmaßnahmen sind über Herstellerbroschüren belegt [V]. Die Detailwerte zu First, Grat, Kehle, Ortgang und Traufe stammen aus dem Gelbdruck vom Juli 2023 (Einspruchsfassung); sie tragen [U, Gelbdruck] und sind gegen die Endfassung 04/2024 abzugleichen (Recherche 09).

## 14.1 Dachformen und Geometrie

### 14.1.1 Dachformen und ihre Abbildung in IFC

IFC 4.3 kennt für `IfcRoof` Aufzählungswerte für alle üblichen Wohnhausdächer [@iso2024ifc]. Das Testmodell aus Recherche 09 mit Walm-, Krüppelwalm-, Mansard-, Zelt- und Pultdach ist gegen IFC4X3_ADD2 mit 0 Fehlern validiert [V]. Tabelle 14.1 ordnet jeder Dachform den PredefinedType und die Parameter zu, mit denen der Generator sie erzeugt.

| Dachform | `IfcRoof` PredefinedType | Erzeugung (Abschnitt 14.1.3) | Kantenarten |
|---|---|---|---|
| Satteldach | GABLE_ROOF | Skelett, Giebelkanten mit Gewicht 0 | Traufe, Ortgang, First |
| Walmdach | HIP_ROOF | Skelett, alle Kanten mit Neigung | Traufe, Grat, First |
| Krüppelwalmdach | HIPPED_GABLE_ROOF | zwei Stufen: Satteldach und angehobener Walm | Traufe, Ortgang, Grat, First |
| Zeltdach | PAVILION_ROOF | Skelett über quadratischem oder regelmäßigem Grundriss | Traufe, Grat |
| Pultdach | SHED_ROOF | eine Traufkante mit Neigung, übrige Kanten als Wand | Traufe, Ortgang, Pultfirst |
| Mansarddach vierseitig | MANSARD_ROOF | zwei Stufen: steile Extrusion bis Knickhöhe, flache Extrusion der Offsetkontur | Traufe, Knick, Grat, First |
| Mansarddach mit Giebel | GAMBREL_ROOF | wie Mansarde, Giebelkanten mit Gewicht 0 | Traufe, Knick, Ortgang, First |
| Flachdach | FLAT_ROOF | keine Skelettrechnung, Gefälle als Schicht | Attika, Rand |
| Gaube | `IfcElementAssembly` USERDEFINED „DORMER“ | eigenes Kleindach, Verschnitt mit Hauptdach | Kehle, Wandanschluss, Traufe |

Jede Dachfläche ist ein `IfcSlab` ROOF, das über `IfcRelAggregates` am `IfcRoof` hängt und die Neigung in `Pset_SlabCommon.PitchAngle` trägt. Diese Abbildung steht in `spezifikation/ifc-mapping.csv`. Sie hat einen Montagegrund: Nur `Qto_SlabBaseQuantities` kennt ein Gewicht, `Qto_RoofBaseQuantities` nicht (Recherche 19).

### 14.1.2 Das Straight Skeleton als Dachmodell

Die Grundidee stammt aus der algorithmischen Geometrie. Aichholzer und Kollegen führten 1995 das Straight Skeleton ein, ein Gerüst aus Stücken von Winkelhalbierenden, das das Innere eines Polygons baumartig zerlegt. Sie zeigten, dass es „auf kanonische Weise“ ein polygonales Dach über einem beliebigen Grundriss liefert [@aichholzer1995novel]. Man stellt sich dazu vor, dass alle Kanten des Grundrisses mit gleicher Geschwindigkeit parallel nach innen wandern. Die Spuren der Ecken bilden Grate und Kehlen. Wo zwei Kanten zusammenstoßen, entsteht ein First. Hebt man jeden Punkt um die Zeit an, zu der die Wellenfront ihn erreicht, entsteht ein Dach mit einheitlicher Neigung.

Die Verallgemeinerung auf Grundrisse mit Löchern, wichtig für Innenhöfe, folgte 1996 [@aichholzer1996general]. Eppstein und Erickson verbesserten die Laufzeit [@eppstein1999raising], Huber und Held beschreiben mit Bone eine Implementierung auf Industrieniveau, gemessen an 22 300 Datensätzen [@huber2012fast]. In Stadtmodellen erzeugen Laycock und Day Dächer aus Grundrissen [@laycock2003generating; @laycock2003automatically], Sugihara kombiniert Rechteckzerlegung und Skelett [@sugihara2013automatic].

Für den Entwurf sind zwei Befunde aus dieser Linie wichtiger als die Laufzeit:

1. **Das Skelett-Dach ist nicht das einzige Dach.** Ahn und Kollegen zeigen für rechtwinklige Grundrisse, dass nach der schlichten Definition eines Daches Flächen ohne Verbindung zum Rand und lokale Tiefpunkte zulässig wären. Sie führen „realistische Dächer“ mit Zusatzbedingungen ein und zeigen, dass das Straight Skeleton unter ihnen das Dach größter Höhe liefert [@ahn2013roofs]. Eder und Kollegen konstruieren entwässernde Dächer minimalen und maximalen Volumens [@eder2018volume]. Die Dachlösung ist also mehrdeutig. Ein Generator muss eine Auswahlregel haben, und die naheliegende ist das Skelett, weil es entwässert, von jeder Fläche zu einer Traufkante führt und maximal hoch ist.
2. **Der Grundriss bestimmt die Güte des Daches.** Koźniewski und Banaszak zeigen an einer Fallstudie, dass die Analyse des Dachskeletts Planungsfehler im Gebäudeumriss aufdeckt, und fordern, die Form des Skeletts in die Mehrkriterienoptimierung aufzunehmen [@kozniewski2020roof]. Für die App folgt daraus eine Prüfregel: Ein Grundriss, der nur ein Dach mit sehr kurzen Firststücken, schmalen Restflächen oder vielen Kehlen zulässt, erhält eine Empfehlung zur Vereinfachung, bevor das Dach im Detail erzeugt wird.

### 14.1.3 Gewichtete Skelette: Neigung je Traufkante

Ein Wohnhausdach hat selten an allen Seiten dieselbe Neigung. Beim Satteldach stehen die Giebelseiten senkrecht, beim Krüppelwalm ist der Walm oft steiler als die Hauptfläche, und Bebauungspläne setzen Dachneigungen je Seite fest. Das ungewichtete Skelett reicht dafür nicht.

Im **multiplikativ gewichteten** Skelett wandert jede Kante mit eigener Geschwindigkeit. Die Geschwindigkeit entspricht dem Kehrwert von tan α der zugehörigen Dachfläche, sodass jede Fläche ihre eigene Neigung erhält. Kelly und Wonka nutzen dieses Prinzip in ihren prozeduralen Extrusionen und modellieren damit Überstände, Gauben, Giebel und gekrümmte Dächer [@kelly2011interactive]. Kellys Dissertation vertieft die Degenerationsfälle konkaver Grundrisse [@kelly2014unwritten]. Held und Palfrader führen zusätzlich **additive** Gewichte ein: Eine Kante beginnt erst zu einem späteren Zeitpunkt zu wandern. Damit lassen sich Dächer mit unterschiedlichen Traufhöhen erzeugen, was für Anbauten, versetzte Geschosse und Kniestöcke unterschiedlicher Höhe gebraucht wird [@held2017roofs].

Gewichtete Skelette haben aber eine Schattenseite. Biedl und Kollegen zeigen, dass schon das gewichtete Skelett eines einfachen Polygons nicht planar sein und Zyklen enthalten kann, und benennen Bedingungen an Gewichte und Grundriss, unter denen es sich gutartig verhält [@biedl2015weighted]. Für die App bedeutet das: Nicht jede Kombination von Neigungen, die der Kunde wünscht, ergibt ein Dach. Die Regelmaschine muss das Ergebnis der Skelettrechnung prüfen und eine unzulässige Neigungskombination ablehnen, statt eine fehlerhafte Geometrie weiterzureichen.

Für die Implementierung stehen zwei Wege offen [V, Recherche 09]:

- **CGAL** ab 5.6 mit gewichteten Skeletten und `extrude_skeleton()` (Winkel je Kante, maximale Höhe; Gewicht 0 ergibt einen Giebel). Die Python-Bindings enthalten das Modul nicht; Lizenz GPL oder kommerziell.
- **Surfer2** und **Monos**, CGAL-basiert mit exakter Arithmetik; Surfer2 verarbeitet multiplikativ gewichtete Streckengraphen und ist schneller als das CGAL-Paket [@eder2021exact].

polyskel, bpypolyskel und scikit-geometry rechnen nur ungewichtet; polyskel lieferte beim L-Grundriss nur im Uhrzeigersinn ein Ergebnis [V, Recherche 09]. Sie taugen als Referenz, nicht als Rechenkern.

**E14.1 – Die Dachgeometrie entsteht aus einem gewichteten Straight Skeleton mit exakter Arithmetik.** *Entscheidung.* Der Rechenkern ist ein multiplikativ und additiv gewichtetes Skelett, implementiert über CGAL oder Surfer2, mit exakten Zahlen im Kern und Rundung erst bei der Übergabe an das Parametermodell (auf 0,1 mm). Jede Traufkante trägt Neigung α und Traufhöhe; Giebel haben Gewicht 0. *Begründung.* Nur das gewichtete Skelett deckt Neigung je Seite und verschiedene Traufhöhen ab [@held2017roofs; @kelly2011interactive]; exakte Arithmetik sichert die Byte-Reproduzierbarkeit (E8.28), weil Gleitkommafehler an Skelettknoten die Topologie ändern können [@eder2021exact]. *Beleg.* Recherche 09 [V]; Lizenzfrage offen (Kapitel 7.4).

**E14.2 – Ausgewählt wird das Skelett-Dach; Plausibilität wird nach der Rechnung geprüft.** *Entscheidung.* Unter den möglichen Dächern über einem Grundriss wählt der Generator das Skelett-Dach. Nach der Rechnung prüft er: jede Dachfläche eben (Abweichung ≤ 0,1 mm), jede Dachfläche mit mindestens einer Traufkante, kein innerer Tiefpunkt, Skelett planar und zyklenfrei. Verletzt eine gewichtete Rechnung diese Bedingungen, wird die Neigungskombination mit Begründung abgelehnt. *Begründung.* Mehrdeutigkeit der Dachlösung [@ahn2013roofs; @eder2018volume] und mögliche Zyklen gewichteter Skelette [@biedl2015weighted]. *Beleg.* Eigene Festlegung.

> **Beispiel 14.1 (Walmdach über dem B18-Haus, eigene Rechnung).** Grundriss 12,00 × 10,00 m wie in B18, Dachüberstand 0,50 m, Traufumriss also 13,00 × 11,00 m. Dachneigung 35° an allen Seiten.
>
> - Firsthöhe über der Traufe: 5,50 m · tan 35° = 3,85 m.
> - Firstlänge: 13,00 − 11,00 = **2,00 m**.
> - Grat im Grundriss 5,50 m · √2 = 7,78 m, wahre Länge √(7,78² + 3,85²) = **8,68 m**.
> - Gratneigung aus tan β = tan α / √2: **β = 26,3°**.
>
> **Gewichtete Variante.** Der Kunde wünscht die Walmflächen mit 45°, die Hauptflächen bleiben bei 35°. Die Firsthöhe bleibt 3,85 m. Die Walmfläche reicht im Grundriss nur 3,85 m / tan 45° = 3,85 m tief, statt 5,50 m. Der First wird dadurch **5,30 m** lang.
>
> **Satteldach.** Gewicht 0 an den beiden Giebelkanten: Der First läuft über die ganze Länge von 13,00 m, die Sparrenlänge von der Traufe bis zum First ist 5,50 m / cos 35° = **6,71 m**. Das entspricht der Länge der Dachelemente in B18 (6,71 × 3,0 m, Kapitel 14b).
>
> Die Rechnung zeigt, warum die Neigung je Kante ein Entwurfsparameter mit Folgen ist: Ein um 10° steilerer Walm verlängert den First auf das 2,6-Fache und verändert Gratlänge, Formziegelbedarf und Dachfläche. Das Beispiel B21 soll diese Werte über den Rechenkern reproduzieren.

### 14.1.4 Zusammengesetzte Formen: Krüppelwalm, Mansarde und Gauben

Nicht jede Dachform ist ein einziges Skelett. Recherche 09 leitet aus den Quellen ein zweistufiges Vorgehen ab, das hier als Verfahren festgelegt wird [U, eigener Entwurf auf Basis der Quellen]:

1. **Krüppelwalm.** Bei konvexem Grundriss ist die Dachfläche die untere Hülle der Kantenebenen: z = min(Satteldachebenen, um die Krüppelhöhe angehobene Walmebene). Bei konkavem Grundriss werden die Skelettflächen mit einer Höhenschranke geschnitten. Das additiv gewichtete Skelett [@held2017roofs] ist die allgemeine Form dieses Vorgehens: Die Walmkante beginnt erst zu wandern, wenn die Wellenfront die Krüppelhöhe erreicht hat.
2. **Mansarde.** Stufe 1 ist eine steile Extrusion mit einer maximalen Höhe gleich der Knickhöhe. Sie liefert als Nebenprodukt die nach innen versetzte Kontur. Stufe 2 extrudiert diese Kontur mit der flachen Oberneigung. Die Knicklinie ist eine eigene Kantenart, weil sie ein eigenes Deckungsdetail hat (Mansardknick, Abschnitt 14.3.5).
3. **Gauben.** Schlepp-, Sattel-, Walm- und Flachgauben sind eigene Kleindächer. Ihr Verschnitt mit der Hauptdachfläche ergibt Kehlen und Anschlusslinien. Im IFC ist die Gaube ein `IfcElementAssembly` USERDEFINED mit ObjectType „DORMER“, das ein eigenes `IfcRoof`, die Gaubenwände und das Fenster bündelt. Die Hauptdachfläche erhält ein `IfcOpeningElement`.

Gauben, Überstände und Knicke lassen sich als Profile einer prozeduralen Extrusion darstellen [@kelly2011interactive]; zusammengesetzte Dächer auch aus Volumenprimitiven [@edelsbrunner2016roofs]. Ren und Kollegen kodieren die Dachtopologie als Graph und erzwingen ebene Flächen über eine Optimierung, flexibler als das Skelett [@ren2021roof]. Für einen reproduzierbaren Generator ist die Optimierung die schwächere Wahl, weil ihr Ergebnis vom Startwert abhängt; sie bleibt ein Kandidat für einen späteren Editiermodus.

Gauben sind zugleich eine Regelgrenze. Für sie gelten dieselben Neigungsgrenzen wie für das Hauptdach, und die letzte Ziegelreihe vor der Gaube soll durchgedeckt werden [U, Gelbdruck FR 4.12]. Über den Bebauungsplan und die Vollgeschossregel wirkt die Gaubenbreite auf das Planungsrecht (Abschnitt 9.4.2).

### 14.1.5 Kantenklassifikation, Grat- und Kehlneigung

Aus dem Skelett lässt sich jede Kante einer Dachfläche einer Kantenart zuordnen, und zwar allein aus der Lage ihrer Nachbarflächen:

- **Traufe:** Kante am Grundriss mit geneigter Nachbarfläche.
- **Ortgang:** Kante am Grundriss mit Gewicht 0 (Giebel).
- **First:** waagerechte Kante zwischen zwei Flächen, die voneinander wegfallen.
- **Grat:** geneigte Kante mit konvexem Flächenwinkel (vom Skelettknoten einer ausspringenden Ecke).
- **Kehle:** geneigte Kante mit konkavem Flächenwinkel (vom Skelettknoten einer einspringenden Ecke).
- **Knick:** waagerechte Kante zwischen zwei Flächen gleicher Richtung und verschiedener Neigung (Mansarde).
- **Pultfirst, Wandanschluss:** obere Kante einer Fläche gegen eine Wand.

Die Kantenart steuert alles Weitere: das Tragwerk (Grat- und Kehlsparren), die Deckungsdetails (Abschnitt 14.3.5) und die Formziegel. Für Grat und Kehle zweier gleich geneigter Flächen, die im Grundriss rechtwinklig aufeinandertreffen, gilt

$$\tan\beta = \frac{\tan\alpha}{\sqrt{2}},$$

wobei α die Dachneigung und β die Neigung der Grat- bzw. Kehllinie ist [U, eigene Herleitung in Recherche 09]. Bei ungleichen Neigungen oder schiefen Grundrisswinkeln folgt β direkt aus dem Skelett als Neigung der Kantenstrecke.

Die Kehlneigung ist für die Regelprüfung entscheidend, weil die Fachregel die Grenzen der Kehlarten an die **Kehlsparrenneigung** knüpft und nicht an die Dachneigung [U, Gelbdruck FR 4.6.1 Tab. 21]. Die Metall-Fachregel knüpft Blechstöße und Überdeckung ebenfalls an die Kehlneigung [U, ältere Fassung]. Weil β stets kleiner ist als α, ergibt sich aus jeder Kehlgrenze eine Mindest-Dachneigung.

| Kehlart | Grenze an der Kehle | Mindest-Dachneigung α bei 90°-Ecke | Status |
|---|---|---|---|
| Metallkehle (Dachneigung) | Dachneigung ≥ 10° | 10,0° | [U, Gelbdruck] |
| Metallkehle, Blech überlappt | Kehlneigung ≥ 15° | 20,8° | [U, eigene Rechnung] |
| Nockenkehle, Biberkehle eingebunden | Kehlsparren ≥ 25° | 33,4° | [U, eigene Rechnung] |
| Biberkehle überdeckt | Kehlsparren ≥ 30° | 39,2° | [U, eigene Rechnung] |
| Dreipfannen-, Formziegel-, Schwenkziegelkehle | Kehlsparren ≥ 35° | 44,7° | [U, eigene Rechnung] |

> **Beispiel 14.2 (Kehle am L-förmigen Haus).** Das B18-Haus erhält einen rechtwinkligen Anbau mit gleicher Dachneigung 35°. Am einspringenden Eck entsteht genau eine Kehle. Ihre Neigung ist wie die Gratneigung in Beispiel 14.1 β = 26,3°.
>
> - Nockenkehle (Kehlsparren ≥ 25°): zulässig, Reserve 1,3°.
> - überdeckte Biberkehle (≥ 30°): unzulässig.
> - Dreipfannenkehle (≥ 35°): unzulässig.
> - Metallkehle: zulässig; Blechstoß mit mindestens 100 mm Überdeckung, weil die Kehlneigung über 22° liegt [U].
>
> Senkt der Kunde die Dachneigung auf 30°, fällt β auf 22,2°, und auch die Nockenkehle wird unzulässig. Die App muss diese Folge vor der Änderung melden, als Vorab-Grenzwert nach ANF-09-19: „Ab einer Dachneigung unter 33,4° ist nur noch eine Metallkehle möglich.“

**E14.3 – Die Kantenart wird aus dem Skelett abgeleitet und ist ein Attribut jeder Kante.** *Entscheidung.* Jede Kante jeder Dachfläche trägt eine Kantenart aus der Liste oben, ihre wahre Länge, ihre Neigung β und die Flächenwinkel der Nachbarflächen. Deckungsdetail, Formziegelbedarf und Tragwerksglied werden aus der Kantenart abgeleitet, nie separat eingegeben. *Begründung.* Nur so bleiben Tragwerk, Deckung und Mengen bei jeder Änderung von Grundriss oder Neigung konsistent (Kapitel 8, E8.10). *Beleg.* Recherche 09, Abschnitt 4 [U, eigener Entwurf].

## 14.2 Dachtragwerk und Abbund

### 14.2.1 Tragwerkstypen und ihre Glieder

Das Tragwerk eines geneigten Holzdaches folgt einem von drei Grundtypen: dem Sparrendach, bei dem je zwei Sparren ein Dreieck bilden, dem Kehlbalkendach mit einem zusätzlichen waagerechten Riegel und dem Pfettendach, bei dem die Sparren auf Längsträgern (Pfetten) liegen. Regnauer beschreibt sein Thermo-Vitaldach als Pfettendach mit 280 mm Holzfaserdämmung und 16 mm Holzfaser-Unterdach [@regnauerBLB2024] (Kapitel 3). Ob die Dachelemente im Werk gedämmt und mit Unterdeckung vorgefertigt werden, ist nicht öffentlich (Recherche 09, Frage 2; DAT-06).

IFC 4.3 bildet die Glieder als `IfcMember` ab [V, Enum-Abfrage in Recherche 09]:

| Glied | `IfcMember` PredefinedType | Unterscheidung |
|---|---|---|
| Sparren, Gratsparren, Kehlsparren, Schifter | RAFTER | ObjectType „Gratsparren“, „Kehlsparren“, „Schifter“ |
| First-, Mittel-, Fußpfette | PURLIN | ObjectType |
| Kehlbalken | COLLAR | – |
| Stiel | POST | – |
| Strebe, Kopfband | STRUT | – |
| Traglatte, Konterlatte | USERDEFINED | ObjectType „BATTEN“ bzw. „COUNTERBATTEN“ |
| Wechsel | `IfcBeam` USERDEFINED | ObjectType „Wechsel“ (E8.15) |

Die Latten fehlen im Enum. Nach E8.15 werden sie als USERDEFINED mit kontrolliertem ObjectType geführt, nicht als `IfcBuildingElementProxy`. Die ObjectTypes „BATTEN“, „COUNTERBATTEN“, „Gratsparren“, „Kehlsparren“ und „Schifter“ sind in das Vokabular von Abschnitt 8.8.4 aufzunehmen; `ifc-mapping.csv` enthält sie noch nicht.

### 14.2.2 Ableitung aus der Geometrie

Das Tragwerk wird aus der Dachgeometrie abgeleitet, nicht getrennt entworfen. Die Ableitung folgt der Kantenart (E14.3):

1. **Sparren** liegen rechtwinklig zur Traufe im Achsraster des Herstellers, abgestimmt mit dem Wandraster (Kapitel 17).
2. **Grat- und Kehlsparren** liegen unter jeder Grat- bzw. Kehlkante mit der Neigung β.
3. **Schifter** sind die verkürzten Sparren zwischen Traufe oder First und Grat- bzw. Kehlsparren. Ihre Backenschmiege in der Dachebene beträgt bei einem Grat unter 45° im Grundriss θ = atan(cos α), also 39,3° bei 35°, 38,2° bei 38° und 35,3° bei 45° Dachneigung [U, eigene Herleitung in Recherche 09, gegen Zimmermannsliteratur zu prüfen].
4. **Wechsel** entstehen an jeder Öffnung, die breiter ist als das lichte Sparrenmaß, mit Lage aus Herstellertabellen (Abschnitt 14.4.1), bei Kaminen aus den Abständen zu brennbaren Bauteilen [U, Recherche 09].
5. **Pfetten, Stiele und Streben** folgen aus Tragwerkstyp und Spannweite; ihre Querschnitte bestimmt die Vorbemessung nach EC 5 (Abschnitt 15.2).

Die Bemessung bleibt beim Tragwerksplaner, dessen Nachweis bei Gebäudeklasse 1 und 2 weder geprüft noch bescheinigt wird (Abschnitt 4.3.5). Umso wichtiger ist eine vollständige, konsistente Übergabe der Geometrie.

**E14.4 – Der Generator erzeugt die Tragwerkstopologie, der Tragwerksplaner die Querschnitte.** *Entscheidung.* Lage, Achsen und Verbindungen entstehen aus der Dachgeometrie. Querschnitte sind Parameter mit Voreinstellung aus dem Herstellerkatalog (DAT-14-01), die der Tragwerksplaner bestätigt; eine Geometrieänderung setzt die betroffenen auf „unbestätigt“. *Begründung.* Die Verantwortung bleibt, wo das Recht sie verortet (R3), Topologie und Mengen kommen konsistent aus dem Modell. *Beleg.* Abschnitt 4.3.5; Kapitel 7a.

### 14.2.3 Abbundbearbeitungen und BTLx

Die Maschinendaten für den Abbund entstehen als BTLx (Kapitel 17), aktuell in der Spezifikation 2.3 vom 08.07.2025 [@btlx23]. Das Werkzeug compas_timber (MIT-Lizenz) exportiert BTLx [@compastimber] und kennt nach Recherche 09 in Version 2.2.0 die Bearbeitungen `BirdsMouth` (Kerve mit Nagelloch), `JackRafterCut` (Schifterschnitt), `DoubleCut`, `FrenchRidgeLap`, `Lap`, `StepJoint`, `Tenon`/`Mortise`, `Dovetail`, `Slot`, `Pocket`, `FreeContour` und `Drilling` [V]. Eine **Dachgenerierung** mit Grat, Kehle und Schifter enthält compas_timber nicht. Die Logik aus Abschnitt 14.2.2 muss also selbst gebaut werden; compas_timber übernimmt nur Bearbeitung und Export. Das Beispiel B7 zeigt den Weg an einem Wandelement: 18 Parts, `Material="KVH C24"`, die Kerve als `Lap` in Ständer R1 (StartX 990, Länge 40, Tiefe 25 mm), reproduzierbar mit SHA-256 `fc91a532…765ff24d` [V, `beispiele/ergebnisse.md`]. Nicht geprüft sind die XSD-Validität und der Import in eine Abbundsoftware.

Dass eine Norm unmittelbar im Fertigungsalgorithmus stecken kann, zeigt die Arbeit von Apolinarska und Kollegen: Ihr Nagelbildalgorithmus setzt die Abstandsregeln der SIA 265 direkt um [@apolinarska2016mastering]. Für den deutschen Kontext sind die Abstandsregeln aus EC 5 mit nationalem Anhang zu übernehmen (Kapitel 17.4).

### 14.2.4 Vorgefertigte Dachelemente

B18 rechnet Dachelemente mit Sparren 80/240, Holzfaser, Holzfaserdämmplatte 60 mm und OSB. Das ergibt ohne Eindeckung 43,4 kg/m² und je Element 0,873 t bei 6,71 × 3,0 m [V, Prototyp B18; Aufbau Annahme]. Die Elementgrenzen folgen den Sparrenachsen und dürfen weder Grat noch Kehle kreuzen. Öffnungen für Dachfenster und Durchgänge entstehen im Werk, der Eindeckrahmen erst nach der Deckung auf der Baustelle.

**E14.5 – Dachelemente sind Teilflächen eines `IfcSlab` ROOF und tragen ihr Gewicht.** *Entscheidung.* Ein vorgefertigtes Dachelement ist ein `IfcSlab` ROOF, das an der Dachfläche und über diese am `IfcRoof` hängt, mit `Qto_SlabBaseQuantities.GrossWeight`. Elementgrenzen liegen auf Sparrenachsen, kreuzen keine Grat- oder Kehlkante und halten die Transportgrenzen aus Kapitel 14b ein. *Begründung.* Das Gewicht ist nur am Slab-Qto standardkonform (Recherche 19); die Grenzbedingungen sichern Fertigung und Montage. *Beleg.* B18 (8 Dachelemente, 0,873 t) [V]; ANF-03-15.

## 14.3 Deckung

### 14.3.1 Regelwerk: Regeldachneigung, Mindestdachneigung, Zusatzmaßnahmen

Die Fachregel für Dachdeckungen mit Dachziegeln und Dachsteinen in der Ausgabe April 2024 [@zvdh2024] regelt die Deckung als anerkannte Regel der Technik, also werkvertraglich (Abschnitt 4.6). Ihr Kern ist das Paar aus Regeldachneigung (RDN) und Mindestdachneigung. Die RDN ist die untere Neigungsgrenze, bei der eine Deckung ohne Zusatzmaßnahme regensicher ist. Die Mindestdachneigung von 10° ist die Geltungsgrenze der Fachregel. Kapitel 9 hat daraus die Regel `DE.ZVDH.DZ.Dachneigung` gebildet (Abschnitt 9.4.5). Tabelle 14.3 fasst die Werte zusammen, die der Generator braucht.

| Regel | Kernwert | Status |
|---|---|---|
| Geltung | Dachneigung ≥ 10° | [V] |
| RDN 22° | Ringfalz: Flachdachziegel, Romanische | [U, Gelbdruck] |
| RDN 25° | Doppelmuldenfalz im Verband; Glatt-, Reform- und Verschiebeziegel mit besonderen Merkmalen | [U, Gelbdruck] |
| RDN 30° | Doppelmulden-, Reform-, Glatt- und Verschiebeziegel; Biber Doppel- und Kronendeckung | [U, Gelbdruck] |
| RDN 35° | Strangfalz, Krempziegel, Hohlpfanne in Aufschnittdeckung | [U, Gelbdruck] |
| RDN 40° | Hohlpfanne in Vorschnitt- oder Einfachdeckung, Mönch/Nonne, Biber-Einfachdeckung mit Spließen | [U, Gelbdruck] |
| Zusatzmaßnahme bei RDN 30° | ≥ 18° K2/K1; ≥ 22° K3/K2; ≥ 26° K4/K3; ≥ 30° K5/K4; unter 18° K1 (ohne/mit erhöhter Anforderung) | [V] |
| Klassen | K1 wasserdichtes Unterdach; K2 regensicheres Unterdach; K3 verklebte Unterdeck- oder Unterspannbahn oder Holzfaser-Unterdeckplatte; K4 verklebt; K5 überlappt | [V] |
| erhöhte Anforderungen | Sparrenlänge > 10 m (DN 10°) bis > 13 m (DN 40°); konzentrierter Wasserlauf; geschweifte Gauben; Schneelast ≥ 1,5 kN/m²; Windzone 4, Kamm- oder Gipfellage; werden **nicht aufaddiert** | [V] |
| Objektplanung | Sparrenlänge > 15 m, extreme Lagen | [U, Gelbdruck] |
| Traglattung | RDN um mehr als 12° unterschritten → Maßnahmen zum Schutz der Traglattung | [U, Gelbdruck] |

Zwei Korrekturen gegenüber verbreiteten Darstellungen sind für die Implementierung wesentlich [V, Recherche 09]:

1. Seit 04/2024 gibt es **fünf Klassen**, nicht sechs. Tabellen mit den alten Bezeichnungen UDB-A und USB-A sind veraltet.
2. **Hersteller-RDN und ZVDH-RDN unterscheiden sich.** Hersteller geben für einzelne Modelle Regeldachneigungen von 14° bis 16° an, deutlich unter den 22° der Fachregel. Wer die Hersteller-RDN nutzen will, muss sie nach Auffassung des ZVDH vertraglich vereinbaren. Nelskamp erklärt in seinen Unterlagen ausdrücklich, dass die Herstellervorschrift Vorrang vor der ZVDH-Regel habe [U, Recherche 09].

Der zweite Befund ist ein Schichtungsproblem im Sinne von Abschnitt 9.3.3. Die Herstellerregel (Schicht S5) darf die anerkannte Regel der Technik (S3) nicht lockern. Eine niedrigere Hersteller-RDN ist also keine strengere, sondern eine lockerere Regel und damit nur über eine ausdrückliche Vereinbarung zulässig.

**E14.6 – Der Generator rechnet mit der ZVDH-RDN; die Hersteller-RDN ist ein freigabepflichtiger Schichtwechsel.** *Entscheidung.* Jedes Ziegelmodell führt beide Werte. Die Klassenrechnung nach `DE.ZVDH.DZ.Dachneigung` verwendet die ZVDH-RDN. Liegt die Dachneigung zwischen Hersteller- und ZVDH-RDN, liefert die Regel `M.Hersteller.RDN-Vereinbarung` das Ergebnis `freigabepflichtig`. Aufgelöst wird es nur durch einen Freigabe-Datensatz der Firma mit der vertraglichen Vereinbarung als Dokument (E8.24). *Begründung.* Schichtungsregel aus Abschnitt 9.3.3; Befund ddh.de 2024 in Recherche 09 [V]. *Beleg.* Regel in `spezifikation/regelkatalog-14-dach.yaml`.

### 14.3.2 Ziegelformen, Oberflächen und Farben

Die Bemusterung wählt Form (Flachdach- und Flachziegel, Doppelmuldenfalz, Reformpfanne, Hohlfalz, Glatt- und Verschiebeziegel, Biber, Mönch/Nonne, Hohlpfanne), Material, Oberfläche (naturrot, engobiert, edelengobiert, glasiert; Dachsteine beschichtet) und Farbe [V, Recherche 09]. Drei Datenlücken sind relevant:

- **Farbwerte.** Die Hersteller veröffentlichen keine RGB- oder Spektralwerte [U]. Texturen für Reifegrad P müssen aus Mustern oder Fotos selbst erstellt werden; Hersteller-Visualisierungen sind keine Texturlizenz [U].
- **Produktdaten.** Eine ETIM-Klasse „Dachziegel“ mit Deckmaß-Merkmalen ließ sich nicht nachweisen [U]. Die Deckmaße stehen nur in PDF-Datenblättern.
- **BIM-Objekte** liegen meist als DWG oder RFA auf Portalen mit eigenen Nutzungsbedingungen [U]. Nach E8.22 liefern sie ohnehin nur Geometrie.

Die Bemusterungsoption „Dachziegel“ ist deshalb ein Typ der Projektbibliothek (E8.14), dessen Merkmale aus einem eigenen, versionierten Datenblatt stammen. Das Schema dieses Datenblatts ist `spezifikation/dachdeckung-herstellerdaten.schema.json` (Abschnitt 14.10).

### 14.3.3 Lattungsalgorithmus aus Herstellerdaten

Die Lattung ist das Bindeglied zwischen Geometrie und Deckung. Die Braas-Verlegeanleitung beschreibt die Einteilung einer Dachfläche über die Konstruktionslänge *L* von der Traufe bis zum First [V, Recherche 09]:

$$L = n \cdot LA + LAT + LAF$$

Darin ist *LA* die Lattweite, *LAT* das Traufenlattmaß (Abstand der untersten Latte von der Traufe), *LAF* das Firstlattmaß (Abstand der obersten Latte vom First) und *n* die Anzahl der Lattweiten. Das Datenblatt jedes Modells nennt einen zulässigen Bereich [LA_min, LA_max], der von der Dachneigung abhängen kann, sowie Bereiche oder Tabellen für LAT und LAF je Neigung. Die Einteilung ist dann eine kleine ganzzahlige Aufgabe:

```text
Rest = L − LAT − LAF
für n von ceil(Rest / LA_max) bis floor(Rest / LA_min):
    LA = Rest / n
    zulässig, wenn LA_min ≤ LA ≤ LA_max
wähle das kleinste zulässige n (größte Lattweite, geringste Stückzahl)
ohne Lösung: variiere LAT und LAF in ihren Bereichen (Raster 1 mm)
ohne Lösung: melde verletzt mit Alternativen (Überstand, Neigung, Modell)
```

Weil *n* ganzzahlig ist, hat die Aufgabe nicht immer eine Lösung. Das ist kein Randfall, wie das folgende Beispiel zeigt.

> **Beispiel 14.3 (Lattung Erlus Linea, eigene Rechnung).** Datenblatt nach Recherche 09: Lattweite 373–393 mm, LAT 370 mm; LAF 40 mm als Annahme [U].
>
> **Fall a (Recherche 09):** L = 6 000 mm. Rest = 5 590 mm. Mit n = 15 ist LA = 372,7 mm < 373 mm, mit n = 14 ist LA = 399,3 mm > 393 mm. **Keine Lösung** mit festem LAT.
>
> **Fall b (B18-Haus):** Satteldach 35°, Überstand 0,50 m, L = 6 714 mm (Beispiel 14.1). Rest = 6 304 mm. Mit n = 16 ist LA = 394,0 mm, mit n = 17 ist LA = 370,8 mm. **Wieder keine Lösung.**
>
> Die Suche über LAT ergibt für n = 16 eine Lösung ab LAT ≥ 386 mm und für n = 17 bis LAT ≤ 333 mm. Ob das Datenblatt diese Traufenlattmaße zulässt, ist offen (DAT-14-02). Bleibt LAT bei 370 mm, nennt die App als Alternative A1 den Dachüberstand: n = 16 passt bei einem waagerechten Überstand **≤ 0,486 m**, n = 17 bei **≥ 0,531 m**. Die Differenz zu 0,50 m beträgt 14 bzw. 31 mm.
>
> Das Beispiel zeigt zweierlei. Erstens gehören LAT- und LAF-Bereiche je Neigung in das Datenblatt, sonst ist die Einteilung nicht entscheidbar. Zweitens koppelt die Lattung die Deckung an einen Entwurfsparameter, den kein Laie mit dem Ziegel in Verbindung bringt: den Dachüberstand.

Liegt die Lösung fest, entstehen die Traglatten als `IfcMember` USERDEFINED „BATTEN“ mit Lage *LAT + i · LA*, die Konterlatten über jedem Sparren. Bei einer Unterschreitung der RDN um mehr als 12° verlangt die Fachregel Maßnahmen zum Schutz der Traglattung [U, Gelbdruck FR 1.2 (7)]. Die Lattung ist damit auch Gegenstand der Klassenrechnung und nicht nur der Geometrie.

**E14.7 – Die Lattung wird aus dem Datenblatt berechnet, nie geschätzt; eine unlösbare Einteilung ist ein Befund.** *Entscheidung.* Die Einteilung nutzt nur Datenblattwerte mit Quelle und Abrufdatum. Ohne Lösung liefert `M.Hersteller.Lattweite` das Ergebnis `verletzt` mit den Alternativen Überstand, Neigung und Modell; fehlt ein Datenblattwert (hier LAF), ist das Ergebnis `unbestimmt`. *Begründung.* Beispiel 14.3; keine erfundenen Zahlen. *Beleg.* Braas-Verlegeanleitung und Erlus-Produktblatt über Recherche 09 [V]; Rechnung [U].

### 14.3.4 Die Deckung als Musterausbreitung

Mit der Lattung liegt das Reihenraster fest. Die Spalten ergeben sich aus der Deckbreite, die ebenfalls in einem Bereich [DB_min, DB_max] liegt (Creaton etwa 260/262/263 mm für min, Mittel und max [V, Recherche 09]). Die Ausbreitung der Deckung ist dann ein Rasterproblem im lokalen (u, v)-System jeder Dachfläche [U, eigener Entwurf in Recherche 09]:

1. Ursprung am Ortgang oder an der Grat-Traufe-Ecke, u entlang der Traufe, v in Fallrichtung.
2. Reihen bei v_i = LAT + i · LA, Spalten mit zulässiger Deckbreite; Ortgangziegel mit eigenen Schnürmaßen (Erlus Linea 115 mm links, 210 mm rechts [V, Recherche 09]); im Verband jede zweite Reihe um DB/2 versetzt.
3. Jede Ziegelfläche wird mit Shapely gegen das Flächenpolygon geschnitten und klassifiziert: voll, geschnitten an Grat oder Kehle, Ortgang, Firstanschluss, Traufe, Einbauteil.
4. Aus der Klassifikation folgen Flächen-, Schnitt-, Form-, Lüfter- und Systemziegel.

Die Formziegel werden je laufenden Meter Kante gerechnet. Datenblätter nennen dafür Stückzahlen, etwa 2,7 Firstziegel je Meter bei Nelskamp D 15 Ü; allgemein liegen First und Grat bei 2,5 bis 2,9 Stück je Meter [U, Recherche 09]. Für den 13,00 m langen First des Satteldachs aus Beispiel 14.1 ergibt das mit dem Nelskamp-Wert 35,1, aufgerundet 36 Firstziegel.

Literatur speziell zur Musterausbreitung von Dachziegeln hat die Recherche nicht gefunden [U]; verwandt ist die Fliesenverlegung in B16 (Kapitel 12). Nach E8.12 folgt die Granularität dem Reifegrad: In P und R ist die Deckung ein `IfcCovering` ROOFING mit Verlegeparametern und Menge, erst in A entstehen Einzelstücke, und auch dann nur für Formziegel und Einbauteile, nicht für jeden Flächenziegel.

### 14.3.5 Details: Traufe, Ortgang, First, Grat, Kehle und Mansardknick

Jede Kantenart aus Abschnitt 14.1.5 hat ein Deckungsdetail. Die Detailwerte stammen aus dem Gelbdruck der Fachregel und sind entsprechend markiert.

| Kante | Detail und Kernwert | Fundstelle | Status |
|---|---|---|---|
| Traufe | Überstand der Deckung < 5 cm verlangt ein Traufblech. Die Traufreihe hat dieselbe Neigung wie die Fläche (Traufbohle oder Doppellatte). Die Lüftungsebene bleibt offen | FR 4.1 | [U, Gelbdruck] |
| Ortgang | Ortgangziegel: Innenkante des Lappens ≥ 1 cm von der Giebelwand. Flächenziegel oder Doppelwulst: Überstand ≥ 3 cm | FR 4.2 (4) | [U, Gelbdruck]; 1 cm von Creaton bestätigt [V] |
| First, Grat | trocken oder in Mörtel; konische Firstziegel ≥ 4 cm Überdeckung; jeder Formziegel mechanisch befestigt, **0,60 kN/m**; Schraube 4,5 mm mit Einschraubtiefe ≥ 24 mm; Mörtel zählt nicht als Windsogsicherung | FR 1.4, 4.3, 4.4 | [U, Gelbdruck] |
| Kehle | Neigungsgrenzen nach Kehlart (Tabelle in 14.1.5). Die Fläche überdeckt die Kehle ≥ 10 cm, rechtwinklig zur Kehllinie gemessen | FR 4.6.1 | [U, Gelbdruck] |
| Metallkehle | Blechstöße ≥ 100 mm (Kehlneigung > 22°), ≥ 150 mm (15–22°), unter 15° wasserdicht; Kehlzuschnitt ≥ 400 mm; Kehlschalung mit lichtem Abstand < 130 mm | Metall-Fachregel 7.2/7.3 | [U, ältere Fassung] |
| Mansard- und Schleppknick | Stirnbrett, Formziegel, Metall oder Fertigelement; die obere Reihe steht über; Unterdach objektspezifisch | FR 4.15 | [U, Gelbdruck] |
| Gaubenanschluss | gleiche Neigungsgrenzen wie das Hauptdach; letzte Reihe vor der Gaube durchdecken | FR 4.12 | [U, Gelbdruck] |
| Windsog | Klammerbedarf objektspezifisch nach „Hinweise zur Lastenermittlung“; über 65° jeden Ziegel klammern | FR 1.4 | [U, Gelbdruck] |

In der App wird jedes Detail zu einer Regel mit Eingaben aus der Kante. Die Kehlüberdeckung von 10 cm etwa ist eine Geometrieregel über die geschnittenen Ziegel entlang der Kehllinie. Die Befestigung der Formziegel ist eine R2-Anforderung: Jedes `IfcDiscreteAccessory` RIDGE oder HIP muss ein Befestigungsmittel mit Typ und Tragfähigkeit tragen, und die Summe je Meter muss 0,60 kN/m erreichen. Die objektspezifische Windsogberechnung nach den „Hinweisen zur Lastenermittlung“ liegt nur auf der kostenpflichtigen DVD vor [V, Recherche 09]. Bis zu ihrer Lizenzierung liefert die Regel für den Klammerbedarf das Ergebnis `unbestimmt`, außer über 65° Dachneigung, wo die Fachregel ohne Rechnung jeden Ziegel verlangt.

## 14.4 Einbauteile

### 14.4.1 Dachfenster, Eindeckrahmen und Rettungsweg

Dachfenster sind im IFC ein `IfcWindow` SKYLIGHT, das über `IfcRelFillsElement` ein `IfcOpeningElement` in der Dachfläche füllt. Der Eindeckrahmen ist ein `IfcDiscreteAccessory` FLASHING [V, Testmodell Recherche 09]. BIM-Objekte bieten Velux, Roto und Fakro über ihre eigenen Seiten und über BIMobject an [V].

Der Eindeckrahmen hängt von der Deckung ab. Velux unterscheidet EDW für profilierte Deckungen von 1,5 bis 12 cm Profilhöhe und 15° bis 90°, EDJ bis 9 cm und 20° bis 90° mit vertieftem Einbau, EDZ/EDN für flache Deckungen bis 16 mm sowie Kombirahmen; die Variante 2000 enthält Dämmrahmen BDX und Unterdachschürze BFX [V, Recherche 09]. Daraus folgt eine Kompatibilitätsregel der Bemusterung (Abschnitt 12.5): Der Ziegel bestimmt die Profilhöhe, diese den Rahmentyp, und die Dachneigung muss im Bereich des Rahmens liegen. Auf das Tragwerk wirkt das Fenster zweifach:

- **Sparrenabstand.** Ideal ist ein lichtes Sparrenmaß gleich der Blendrahmenbreite plus 6 cm, mit Dämmrahmen BDX plus 4 bis 5 cm. Kombinationen nebeneinander brauchen eine Mittelrinne von 10 bis 16 cm, übereinander 10 cm, mit Rollladen 25 cm [V, Recherche 09].
- **Wechsel.** Die Velux-Tabelle „Wechselabstände“ nennt Mindestabstände oben und unten je Dachdicke und Neigung, einschließlich 10 cm Sicherheit, etwa 21,1 cm oben und unten bei 20 cm Dachdicke und 45° [V].

Passt das Fenster nicht zwischen die Sparren, muss ein Sparren ausgewechselt werden. Der Generator prüft deshalb zuerst, ob eine Verschiebung des Fensters um weniger als eine halbe Sparrenteilung einen Wechsel vermeidet, und schlägt das als Alternative A1 vor.

**Rettungsweg.** Ein Dachfenster kann der zweite Rettungsweg eines Aufenthaltsraums im Dachgeschoss sein. Art. 35 Abs. 4 BayBO verlangt dafür in der ab 01.05.2026 geltenden Fassung [V, Recherche 09; @baybo2026]:

- eine lichte Breite von mindestens **0,60 m** und eine lichte Höhe von mindestens **1,00 m**,
- Öffnen von innen,
- eine Unterkante höchstens 1,20 m über dem Fußboden,
- in Dachschrägen eine Unterkante oder einen Austritt, der horizontal höchstens 1 m von der Traufkante entfernt ist.

Die in der Ausgangskonzeption dieser Arbeit genannten 0,90 × 1,20 m sind damit widerlegt. Ob die Maße erst mit der Novelle 2026 geändert wurden, hat die Recherche nicht geprüft [U]. Im IFC trägt das Rettungsfenster `Pset_WindowCommon.FireExit = TRUE`. Die Prüfung ist eine Geometrieregel über lichte Öffnungsmaße, Unterkante und den waagerechten Abstand zur Traufkante; die lichten Maße liefert der Hersteller am Typ (E8.22).

**Brandschutz.** Dachflächenfenster müssen mindestens 1,25 m von Brandwänden und Gebäudeabschlusswänden entfernt sein, sofern diese nicht mindestens 0,30 m über Dach geführt sind (Art. 30 Abs. 5 BayBO). Dachfenster von Wohngebäuden sind von der Anforderung einer harten Bedachung ausgenommen (Abs. 3 Nr. 3) [V, Recherche 09]. Bei Doppel- und Reihenhäusern wird die 1,25-m-Regel zu einer Sperrfläche entlang der Haustrennwand (Kapitel 9a, `BY.BayBO.28-2.Gebaeudeabschlusswand`).

### 14.4.2 Durchgänge: Sanitärlüfter, Solar, Antenne, Kamin

Jede Leitung, die das Dach durchdringt, erzeugt ein Einbauteil in der Deckung. Recherche 09 nennt aus dem Programm von Creaton und Koramic 2025 [V]:

- Solardurchgang Ø 70 mm, Antennendurchgang Ø 40–60 mm, Thermendurchführung Ø 110/125 mm für 7° bis 50°,
- Dunstrohr und Lüfter Ø 125/160 mm mit **offener Kappe für Fallleitungen** und geschlossener Kappe für Lüftungsleitungen.

Die Unterscheidung der Kappen entspricht DIN 1986-100:2016-12. Danach dürfen an der Mündung von Lüftungsleitungen über Dach keine Abdeckungen sitzen, und jede Fallleitung wird als Lüftung über Dach geführt; im Einfamilienhaus genügt eine Fallleitung über Dach, die übrigen dürfen Belüftungsventile haben [V, Recherche 09]. Für die Mündung nennt eine Sekundärquelle mindestens 15 cm über der Dachfläche sowie 1 m über oder 2 m neben Dachfenstern [U].

Kapitel 13 routet die Hauptlüftung, B15 führt sie als DN 100 mit Manschette durch Decke und Dach, dieses Kapitel setzt den Lüfterziegel in die Deckung. Im IFC ist die Mündung ein `IfcStackTerminal` COWL auf dem `IfcPipeSegment`, die Durchdringung ein `IfcOpeningElement` in der Dachfläche, der Lüfterziegel ein `IfcDiscreteAccessory`. Der Kamin ist ein `IfcChimney` mit USERDEFINED und `Pset_ChimneyCommon`; das Enum kennt keinen weiteren Wert [V].

### 14.4.3 Schneefang, Dachtritte und Sicherheitshaken

Art. 30 Abs. 8 BayBO verlangt Vorrichtungen für Arbeiten, die vom Dach aus vorzunehmen sind [V, Recherche 09]. Dazu gehören Sicherheitshaken und Dachtritte für den Schornsteinfeger und für die Wartung der Photovoltaik. Schneefanggitter hängen von der örtlichen Schneelast und der Lage über Verkehrsflächen ab; die Hersteller bieten Rechner an (Erlus-Schneesicherungsrechner [V, Recherche 09]).

Das IFC-Schema hat für diese Bauteile keinen Enum-Wert. Sie werden nach E8.15 als `IfcDiscreteAccessory` USERDEFINED mit den ObjectTypes SNOWGUARD, ROOFSTEP und SAFETYHOOK geführt, alternativ das Schneefanggitter als `IfcRailing` GUARDRAIL [V, Recherche 09].

**E14.8 – Jedes Einbauteil ist ein Tripel aus Produkt, Öffnung und Deckungsteil.** *Entscheidung.* Dachfenster, Durchgang oder Sicherheitshaken bestehen aus (1) dem Produkt mit Typ aus der Projektbibliothek, (2) der Öffnung oder Befestigung im Tragwerk und (3) dem Deckungsteil (Eindeckrahmen, Lüfterziegel, Systemziegel). Das Tripel wird gemeinsam erzeugt, verschoben und gelöscht; eine IDS-Regel prüft, dass kein Teil allein existiert. *Begründung.* Fehlt ein Teil, entsteht auf der Baustelle ein Mangel oder im Werk eine fehlende Bearbeitung. *Beleg.* Recherche 09 (Velux, Creaton) [V]; Muster der Abhängigkeitskette aus Kapitel 12.5 (Wand-WC → Vorwand → Ständer → Abwasser).

## 14.5 Dachentwässerung

Die Dachentwässerung ist das Bindeglied zur Grundstücksentwässerung in Kapitel 14a. Sie wird nach DIN 1986-100:2016-12 bemessen; der Entwurf E DIN 1986-100:2025-06 liegt vor [V, Recherche 09].

**Berechnungsregen.** Für Dachflächen gilt seit 2008 die fünfminütige Regenspende mit einer Wiederkehrzeit von fünf Jahren, r(5,5), zuvor r(5,2). Dach- und Notentwässerung zusammen müssen r(5,100) abführen. Für Grundstücksflächen gilt r(5,2) [V, DIN-FAQ in Recherche 09]. Fachaufsätze rechnen vorgehängte Rinnen nach Verbandspraxis weiter mit r(5,2), ein Herstellerrechner mit r(5,5) [V/U].

**Abfluss.** Der Regenwasserabfluss einer Dachfläche ist

$$Q = \frac{r \cdot C \cdot A}{10\,000}\quad[\mathrm{l/s}],$$

mit r in l/(s·ha), dem Abflussbeiwert C = 1,0 für Dachflächen und der projizierten Fläche A in m² [V, Recherche 09]. Für halbrunde Rinnen nennt DIN EN 12056-3 Q = 0,9 · 2,78 · 10⁻⁵ · A_W^1,25 · F_L. Eine Tabelle aus der Fachliteratur ordnet halbrunden Rinnen mit 250, 280, 333 und 400 mm Zuschnitt die Abflüsse 2,9, 4,1, 7,4 und 14,5 l/s zu; bei Winkeln gilt der Faktor 0,85; Fallrohre unter DN 75 werden nicht empfohlen [V Formel, U Tabellenwerte].

**Regendaten.** KOSTRA-DWD-2020 ist frei nutzbar (GeoNutzV), als 5-km-Raster in EPSG:3035 mit 22 Dauerstufen und Wiederkehrzeiten von 1 bis 100 Jahren, Rasterindex Zeile · 1000 + Spalte [V, Recherche 09]; München liegt unter anderem im Feld 202168 [V, Recherche 18]. Rasterfeld, Datensatzversion und Abrufdatum stehen im Nachweis (Kapitel 7a).

> **Beispiel 14.4 (Dachentwässerung des B18-Hauses).** Projizierte Dachfläche 13,00 × 11,00 m = 143 m², vier Fallrohre, je 35,75 m².
>
> - Mit r(5,2) = 290 l/(s·ha), dem Wert aus B17 für Grundstücksleitungen: Q = 290 · 1,0 · 35,75 / 10 000 = **1,04 l/s je Fallrohr**. Das ist genau der Zufluss, den B17 für die Regenfallrohre RF1 bis RF4 an der Grundleitung ansetzt [V, `ausgabe/b17_bericht.md`].
> - Mit r(5,5) nach DIN 1986-100 wird Q größer. Den Wert für das Grundstück liefert KOSTRA-DWD-2020 aus dem Rasterfeld des Standorts. Die in B17 verwendete Regenreihe stammt aus einer Sekundärquelle für Unterschleißheim und enthält r(5,5) nicht [V, Recherche 18].
>
> Eine halbrunde Rinne mit 250 mm Zuschnitt (2,9 l/s) hätte bei r(5,2) eine Reserve von 64 %; ob sie bei r(5,5) reicht, entscheidet erst der Standortwert. Deshalb gehören beide Werte in den Nachweis.

**E14.9 – Die Dachentwässerung rechnet mit r(5,5) aus KOSTRA-DWD-2020 und dokumentiert die Abweichung von der Rinnenpraxis.** *Entscheidung.* Der Rechenkern bemisst Rinne und Fallrohr mit r(5,5) für das KOSTRA-Rasterfeld des Grundstücks. Der Nachweis weist zusätzlich das Ergebnis mit r(5,2) aus und nennt die Norm-FAQ als Begründung. Die Grundleitungen in Kapitel 14a rechnen mit r(5,2). *Begründung.* DIN 1986-100 verlangt r(5,5) für Dachflächen; die abweichende Praxis ist belegt, aber nicht normgerecht [V/U]. *Beleg.* Recherche 09, Abschnitt 8; Beispiel 14.4.

Die IFC-Abbildung ist vollständig standardkonform [V]: Rinne als `IfcPipeSegment` GUTTER mit `Pset_PipeSegmentTypeGutter` (Slope, FlowRating), Fallrohr als RIGIDSEGMENT, Rinnenkessel als `IfcStackTerminal` RAINWATERHOPPER, Bögen als `IfcPipeFitting` BEND, alles in einem `IfcDistributionSystem` RAINWATER. Das Fallrohr endet an einem Standrohr mit Reinigungsöffnung und Laubfangkorb, und dort beginnt Kapitel 14a.

## 14.6 Photovoltaik

### 14.6.1 Rechtsrahmen

Für die Photovoltaik auf dem Wohnhausdach gelten fünf Regeln aus vier Rechtsquellen [V, Recherche 09]:

| Regel | Kernwert | Fundstelle | Klasse |
|---|---|---|---|
| Solarpflicht Wohngebäude | **Soll-Vorschrift** bei Bauantrag oder vollständiger Dacherneuerung ab 01.01.2025; angemessen ist eine Modulfläche von mindestens einem Drittel der geeigneten Dachfläche, dachparallel oder integriert | Art. 44a Abs. 4 mit Abs. 1 S. 2–4 BayBO | R1 weich |
| Vorrang örtlicher Bauvorschriften | Gestaltungssatzungen nach Art. 81 gehen der Solarpflicht vor | Art. 44a Abs. 5 Nr. 1 BayBO | R1 |
| Brandschutz Doppel- und Reihenhaus | Solaranlagen ≥ 0,50 m von Brandwänden und Wänden anstelle von Brandwänden, sofern diese sie nicht gegen Brandübertragung schützen | Art. 30 Abs. 5 S. 2 Nr. 2 BayBO | R1 hart |
| Einspeisung | Anlagen < 100 kW mit Inbetriebnahme ab 25.02.2025 und Einspeisevergütung: 60 % der Wirkleistung, bis Smart Meter und Steuerbox getestet sind | § 9 Abs. 2 EEG 2023 | R1 Hinweis |
| Registrierung | Marktstammdatenregister innerhalb eines Monats nach Inbetriebnahme | § 5 Abs. 5 MaStRV | R4 |

Dazu kommen der Netzanschluss nach VDE-AR-N 4105:2026-03 mit zwölf Monaten Übergang für die Fassung 2018 [V] und die Errichtung nach DIN VDE 0100-712, deren Ausgabe 2016-10 nur angenommen ist [U]. Die Muss-Pflicht des Art. 44a betrifft nur Nichtwohngebäude und staatliche Gebäude [V].

Die bayerische Solarpflicht ist für Wohngebäude also eine **Soll-Vorschrift** [V] und in der Taxonomie von Kapitel 9 eine weiche R1-Regel: Sie erzeugt einen Hinweis mit Begründung, verwirft aber keinen Entwurf.

### 14.6.2 Belegung

Die Belegung ist ein Packungsproblem auf einer ebenen Fläche mit Sperrflächen. Eine pauschale Randabstandsregel gibt es nicht; die Randabstände folgen aus der Auslegung des Montagesystems nach DIN EN 1991-1-4 mit Randzonen e = min(b; 2h) und aus der Herstellersoftware [V Prinzip, U Zonenmaße]. Das Verfahren:

1. **Fläche.** Flächenpolygon aus dem Skelett abzüglich Randzonen, 0,50-m-Streifen an Brandwänden, Dachfenster, Durchgänge, Kamin, Schneefang, Sicherheitshaken und Verschattung durch Gauben.
2. **Raster.** Module in beiden Orientierungen, Rasterursprung über eine Modulteilung verschoben; gewählt wird die größte Modulzahl, bei Gleichstand die geringste Zahl verschiedener Reihenlängen.
3. **Befestigung.** Dachhaken ab der RDN des Ziegels, Systemziegel mit Formschluss ab 10°, darunter Dachträgerpfannen [V, FR 4.10 (3) und K2 Systems in Recherche 09]. Die Haken sitzen auf Sparren und Lattreihen, sind also erst nach der Lattung bestimmbar.
4. **Statik des Montagesystems** rechnet die Herstellersoftware; ihr Ergebnis wird Nachweisdokument (E8.24).

**Indach oder Aufdach.** Bei der Aufdachanlage bleibt die Deckung durchgehend, die Haken sind `IfcDiscreteAccessory` BRACKET. Bei der Indachanlage ersetzen die Module die Deckung: Das `IfcCovering` ROOFING erhält eine Öffnung, die Module füllen sie, und die Anschlussbleche sind `IfcDiscreteAccessory` FLASHING [U, eigene Modellierung in Recherche 09].

### 14.6.3 Ertrag

Der Ertrag wird mit pvlib (Version 0.16.1, BSD-3) und PVGIS gerechnet [V, Recherche 09]. pvlib liest über `iotools.get_pvgis_hourly` bzw. `get_pvgis_tmy` die PVGIS-Daten und über `read_panond` die Kennlinien der Module und Wechselrichter aus PAN- und OND-Dateien. Die PVGIS-API 5.3 unter `re.jrc.ec.europa.eu/api/v5_3/PVcalc` erlaubt 30 Aufrufe je Sekunde und nimmt die Parameter `peakpower`, `loss`, `angle`, `aspect` (0 = Süd) und `mountingplace=building`. Für die Reproduzierbarkeit nach E8.28 speichert die App die Antwort mit Hash und rechnet bei gleicher Eingabe aus dem Speicher, statt die API erneut abzufragen.

> **Beispiel 14.5 (Solarpflicht-Fläche am B18-Haus, eigene Rechnung).** Satteldach 35°, Firstrichtung Ost–West, Südfläche 13,00 × 6,71 m = 87,3 m².
>
> - Wenn die ganze Südfläche als „geeignet“ gilt, verlangt Art. 44a Abs. 4 als angemessene Modulfläche mindestens **29,1 m²**.
> - Mit Dachfenster, Lüfterziegel und Randzonen sinkt die geeignete Fläche und mit ihr die Sollgröße. Was „geeignet“ bedeutet, legt das Gesetz nicht zahlenmäßig fest; die App führt es als Auslegungsparameter mit Status [U], den die bauvorlageberechtigte Person bestätigt (ANF-09-21).
> - Ob 29,1 m² eine bestimmte Modulzahl ergeben, hängt vom Moduldatenblatt ab (DAT-14-07). Die App rechnet die Zahl aus dem Datenblatt, nicht aus einem Standardmodul.
>
> Setzt ein Bebauungsplan des Standorts eine Gestaltungsvorschrift nach Art. 81 fest, die Solaranlagen auf der Straßenseite ausschließt, geht diese vor (Art. 44a Abs. 5 Nr. 1). Die Südfläche wäre dann nur geeignet, wenn sie nicht zur Straße weist.

### 14.6.4 Abbildung in IFC

Module sind `IfcSolarDevice` SOLARPANEL, Solarthermie SOLARCOLLECTOR, Wechselrichter `IfcTransformer` INVERTER und Speicher `IfcElectricFlowStorageDevice` BATTERY, alle in einem `IfcDistributionSystem` [V, Schemaabfrage in Recherche 09]. `IfcElectricGenerator` passt nicht; sein Enum kennt nur CHP, ENGINEGENERATOR und STANDALONE. `Pset_SolarDeviceTypeCommon` enthält nur Reference und Status. Leistungsdaten stehen deshalb in `Pset_ElectricalDeviceCommon` und in einem eigenen Pset mit den Kennwerten der PAN-Datei, nach E8.21 als `HRB_PVModul`.

**E14.10 – Photovoltaik: weiche Soll-Regel, harte Abstände, abgeleitete Belegung.** *Entscheidung.* Die Solar-Soll-Regel erzeugt einen Hinweis mit Sollfläche, nie eine Ablehnung. Brandschutzabstand, RDN-Grenze der Dachhaken und Sperrflächen sind harte Regeln der Belegung, die nach jeder Änderung von Geometrie, Lattung oder Einbauteil neu gerechnet wird. Die MaStR-Frist erscheint als Termin im Übergabepaket. *Begründung und Beleg.* Art. 44a Abs. 4 ist Soll-, Art. 30 Abs. 5 S. 2 Nr. 2 Muss-Vorschrift [V, Recherche 09].

## 14.7 Fassade

### 14.7.1 Holzschalung nach Fachregel 01

Die Fachregel 01 des Zimmererhandwerks „Außenwandbekleidungen aus Holz“ (3. korrigierte Auflage 03/2023 der Fassung 01/2020) ist nur gedruckt und kostenpflichtig erhältlich. Sie gilt bis **10 m Firsthöhe** für Vollholz, Dreischichtplatten und zementgebundene Spanplatten [V, Recherche 09]. Oberhalb dieser Geltungsgrenze, etwa bei Mehrfamilienhäusern (Kapitel 9a), wird der Brandschutz der Bekleidung nach Gebäudeklasse eigenständig maßgeblich. Die Schalungsarten folgen der Ausschreibungshilfe von Holzbau Deutschland 2021: Stülpschalung (parallel, konisch, mit Falz, mit Nut und Feder), Boden-Deckel-, Deckleisten- und Leisten-Deckel-Schalung sowie offene Bekleidung [V, Recherche 09].

Für die Bretter gelten eine Dicke von mindestens 18 mm und eine Breite von höchstens dem Elffachen der Dicke; ab 120 mm Breite wird zweifach befestigt [V]. Der Sockel hält typisch 300 mm Abstand zum Gelände, auf einem Kiesstreifen 16/32 bis 150 mm [V, BauNetz Wissen nach FR 01]. Hinterlüftung und Insektenschutz sind nach DIN 68800-2 und FR 01 zu planen; Querschnitte und Gitterweiten sind aus der Fachregel zu übernehmen, deren Volltext nicht eingesehen wurde [U].

Die Breitenregel koppelt zwei Bemusterungsparameter: Ein 20 mm dickes Brett darf höchstens 220 mm breit sein; für ein 240-mm-Profil bietet die App 22 mm Dicke an (Grenze 242 mm).

### 14.7.2 Putz auf Holzfaser

Die verputzte Holzfaserfassade ist ein Wärmedämm-Verbundsystem auf Holzfaser-Trägerplatten. Sie braucht je System eine allgemeine bauaufsichtliche Zulassung bzw. Bauartgenehmigung des DIBt, etwa für die Systeme von Gutex, Steico oder Pavatex; die Nummern je Regnauer-Wandtyp sind zu beschaffen [U, Recherche 09; DAT-14-08]. Beispiel 3.2 hat gezeigt, dass Putz und Putzträgerplatte in der Wanddicke des Herstellers Platz finden müssen und dass daraus ein Widerspruch in den veröffentlichten Aufbauten auffällt (Kapitel 3). Die Zulassungsnummer ist deshalb eine R2-Anforderung: Ohne sie ist der Nachweis der Außenwand im Reifegrad R `unbestimmt`.

### 14.7.3 Farben und Gestaltungssatzungen

RAL und NCS sind lizenzierte Farbsysteme. Frei nutzbare RGB-Näherungen sind nicht normativ [U, Recherche 09]. Die App speichert deshalb den Farbcode als Merkmal der Bemusterung und verwendet RGB-Werte nur für die Darstellung, mit dem Hinweis, dass Bildschirmfarbe und Musterfarbe abweichen.

Örtliche Bauvorschriften nach Art. 81 BayBO können Dachform, Dachneigung, Material und Farbe von Dach und Fassade festsetzen und gehen der Solarpflicht vor [V, Recherche 09]. XPlanung sieht dafür die Klasse `BP_Dachgestaltung` mit DNmin, DNmax und Dachform vor [@xplanung]. Wie in Abschnitt 4.2 gezeigt, liegen bayerische Bebauungspläne aber meist nur im Minimalstandard vor. Die Festsetzungen zur Gestaltung werden deshalb im Dialog bestätigt oder aus dem PDF-Plan extrahiert und von einem Menschen geprüft. Die Regel `BY.BayBO.81.Dachgestaltung` prüft dann Dachform, Neigung je Fläche, Deckungsfarbe und Fassadenfarbe gegen die bestätigten Festsetzungen.

### 14.7.4 Regelbasierte Fassadengliederung

Split- und Shape-Grammatiken teilen Fassaden rekursiv in Geschosse, Achsen und Felder [@wonka2003instant; @mueller2006procedural], zielen aber auf visuelle Modelle ohne Bauteilsemantik. Näher an der Bauproduktion liegen Konfigurationsansätze: eine vorgefertigte Hüllpaneel-Sanierung als Constraint-Problem mit Stückliste und Montageablauf [@vareilles2013renovation], BIM als Konfigurationsplattform für Fassadensysteme für Experten [@piroozfar2019configuration] und ein offenes Holzbausystem mit Öffnungsregeln und BIM-Bibliothek [@buildinwood2024]. Übernehmbar ist das Prinzip: Die Gliederung ist eine Aufgabe der Regelmaschine, nicht der Grafik. Fensterachsen hängen an Ständerlagen (Kapitel 17), Schalungsstöße an Lattenlagen, Fenstergrößen am Schallschutz gegen Außenlärm (Abschnitt 15.4, B19).

### 14.7.5 Abbildung in IFC und Darstellung

Die Fassadenbekleidung ist ein `IfcCovering` CLADDING, das über `IfcRelCoversBldgElements` an der `IfcWall` hängt. Das `IfcMaterialLayerSet` enthält die Luftschicht mit `IfcMaterialLayer.IsVentilated`. Für die Darstellung trägt das Material einen `IfcSurfaceStyle` mit `IfcSurfaceStyleRendering` (ReflectanceMethod PHYSICAL) und `IfcSurfaceStyleWithTextures` mit `IfcImageTexture`; die UV-Koordinaten stehen in einer `IfcIndexedTriangleTextureMap`. Das Testmodell in Recherche 09 ist damit valide [V].

Der glTF-Export von IfcOpenShell übernimmt nur Farben, keine Texturen und UV-Koordinaten [V, Test in Recherche 09]. Die Nachbearbeitung (etwa mit trimesh, MIT) nimmt die UV-Koordinaten aus dem (u, v)-System der Deckung bzw. Schalung, sodass die Textur dem Verlegeraster folgt (ANF-08-30, Kapitel 16).

**E14.11 – Fassade und Deckung teilen das (u, v)-System für Rechnung und Darstellung.** *Entscheidung.* Jede Dach- und Fassadenfläche hat genau ein lokales (u, v)-System. Lattung, Deckung, Schalung, Musterausbreitung und Texturkoordinaten beziehen sich darauf. *Begründung.* So stimmt das Bild in Reifegrad P mit Menge und Schnittplan in Reifegrad A überein, und eine Änderung des Rasters ändert beides zugleich. *Beleg.* Recherche 09, Abschnitte 4 und 7 [U, eigener Entwurf].

## 14.8 Reifegrade für Dach und Fassade

Nach den Reifegraden aus Kapitel 11, die dem Informationsbedarf der DIN EN ISO 7817-1 folgen [@dineniso7817-1], staffelt sich das Dach so: In P genügen Flächen, Farbe und Textur im Verlegeraster. R verlangt Neigungen, Traufhöhen, Kantenarten, Deckungsklasse, Rettungsweg, Brandschutzabstände, Solar-Soll-Regel, Bemessung der Entwässerung mit r(5,5) sowie Zulassungsnummer und Satzungsprüfung der Fassade. A ergänzt alle Tragwerksglieder mit Querschnitt und BTLx, Lattung, Formziegel je Kante, Einbauteile mit GTIN, Module mit Haken und Anmeldeterminen sowie den Schalungsplan.

## 14.9 Zwischenfazit

1. **Geometrie.** Das gewichtete Straight Skeleton mit exakter Arithmetik erzeugt aus Grundriss, Neigung und Traufhöhe je Kante ein eindeutiges, entwässerndes Dach [@aichholzer1995novel; @held2017roofs; @eder2021exact]. Neu ist nicht der Algorithmus, sondern seine Verbindung mit Tragwerk, Deckung und Regelwerk über die Kantenart.
2. **Regelwerk.** Die Regeln des Dachdeckerhandwerks lassen sich als Kennwerte fassen, liegen im Detail aber hinter einer Bezahlschranke und sind teils nur über den Gelbdruck belegt. Drei Annahmen der Ausgangskonzeption sind widerlegt: das Rettungsfenstermaß, die Solarpflicht als Muss-Regel und r(5,2) als Berechnungsregen für Dächer.
3. **Daten.** Die Herstellerdaten reichen für einen Lattungsalgorithmus nur, wenn Traufen- und Firstlattmaß je Neigung maschinenlesbar vorliegen. Beispiel 14.3 zeigt, dass sonst schon ein gewöhnliches Satteldach keine zulässige Einteilung hat.

Offen bleiben die Lizenzen der ZVDH-Fachregel, der Windsog-Rechenhilfen und von CGAL, der Abgleich der Gelbdruck-Werte und das Beispiel B21, das die Rechnungen dieses Kapitels über den Rechenkern reproduzieren soll.

## 14.10 Umsetzungsvorgaben für die App

Es gelten die Festlegungen aus Abschnitt 9.9: „Muss“ heißt, dass ohne die Anforderung ein Rechts-, Nachweis- oder Fertigungsfehler entstehen kann; „Soll“ heißt, dass sie Qualität oder Nutzen erhöht. Zahlen in den Abnahmekriterien sind eigene Rechnungen dieses Kapitels oder Werte aus B17 und B18; Herstellerwerte sind Beispielwerte aus Recherche 09 und durch die Datenlieferungen zu ersetzen.

### 14.10.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/regelkatalog-14-dach.yaml` | 26 Regeln zu Dachgeometrie, Kehle, Lattung, Deckungsdetails, Einbauteilen, Rettungsfenster, Brandschutzabständen, Dachentwässerung, Photovoltaik, Fassade und Gestaltungssatzung nach `regel.schema.json` |
| `spezifikation/dachdeckung-herstellerdaten.schema.json` | JSON-Schema (Draft 2020-12) des Datenblatts je Ziegel- oder Steinmodell: RDN nach ZVDH und Hersteller, Lattweite, Deckbreite, Traufen- und Firstlattmaß je Neigung, Schnürmaße, Zubehör mit Bedarf je Meter, Quelle und Status; mit zwei Beispieldatensätzen aus Recherche 09 |

Am 27.09.2026 geprüft: Die YAML-Datei ist mit PyYAML parsebar und validiert mit `jsonschema` 4.26 ohne Fehler gegen `regel.schema.json`. Das Datenblattschema ist nach Draft 2020-12 gültig, und seine Beispiele validieren gegen es. Die Profile `DE-Handwerk-Dach`, `BY-BayBO-2026-05`, `M-Firma` und `DE-aRdT-Sanitaer` sind in `regelprofile.yaml` registriert; neu verwendet werden `DE-EEG-2023`, `M-Hersteller-Dach` und `DE-Handwerk-Zimmerer`, die dort noch nachzutragen sind.

### 14.10.2 Anforderungen

**Geometrie und Tragwerk**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14-01 | Muss | Die Dachgeometrie entsteht aus einem gewichteten Straight Skeleton mit exakter Arithmetik; Neigung und Traufhöhe je Kante, Gewicht 0 für Giebel. | E14.1 | Traufumriss 13,00 × 11,00 m, alle Kanten 35°: First 2,000 m, Firsthöhe 3,851 m, Grat 8,679 m (± 1 mm); Walmkanten 45°: First 5,298 m; Giebelkanten Gewicht 0: First 13,000 m. |
| ANF-14-02 | Muss | Nach jeder Skelettrechnung werden Ebenheit, Traufanschluss jeder Fläche, Tiefpunktfreiheit und Planarität geprüft; eine unzulässige Neigungskombination wird mit Begründung abgelehnt. | E14.2 | Walmdach Rechteck: 4 Traufen, 4 Grate, 1 First, 0 Kehlen; Satteldach: 2 Traufen, 2 Ortgänge, 1 First. Jede Fläche hat eine Traufkante; Abweichung von der Ebene ≤ 0,1 mm. |
| ANF-14-03 | Muss | Krüppelwalm und Mansarde entstehen zweistufig; Gauben sind `IfcElementAssembly` DORMER mit eigenem `IfcRoof` und `IfcOpeningElement` im Hauptdach. | 14.1.4 | Mansarde: jede Knicklinie hat die Kantenart „Knick“. Gaube: genau eine Öffnung im Hauptdach, deren Rand aus Kehlen und Anschlusskanten besteht. |
| ANF-14-04 | Muss | Jede Kante trägt Kantenart, wahre Länge und Neigung β; die Kehlart wird gegen die Kehlneigung geprüft, und die Grenzneigung wird vor einer Änderung gemeldet. | E14.3, Bsp. 14.2 | L-Grundriss, 35°: genau 1 Kehle am einspringenden Eck, β = 26,34°; Nockenkehle `erfuellt`, überdeckte Biberkehle `verletzt`. Intent „Dachneigung 30°“: Vorab-Meldung „unter 33,4° nur Metallkehle“. |
| ANF-14-05 | Muss | Das Tragwerk wird aus der Geometrie abgeleitet (Sparren, Grat- und Kehlsparren, Schifter, Wechsel). Querschnitte sind bestätigungspflichtige Parameter des Tragwerksplaners. | E14.4 | Schifter-Backenschmiege bei 45°-Grat: 39,32° (DN 35°), 35,26° (DN 45°). Nach Änderung der Dachneigung haben alle betroffenen Querschnitte den Status „unbestätigt“. |
| ANF-14-06 | Muss | Abbundbearbeitungen werden als BTLx exportiert (Kerve, Schifterschnitt, Stoß, Bohrung), jede mit GlobalId der Quelle. | 14.2.3, ANF-08-22 | Jeder Schifter hat genau eine `JackRafterCut`-Bearbeitung je Gratseite; jede Bearbeitung trägt `UserAttribute Name="IfcGlobalId"`. |
| ANF-14-07 | Muss | Dachelemente sind `IfcSlab` ROOF mit `GrossWeight`; Elementgrenzen liegen auf Sparrenachsen und kreuzen weder Grat noch Kehle. | E14.5 | B18-Dachelement 6,71 × 3,0 m mit 43,35 kg/m²: GrossWeight 873 kg ± 1 kg. Eine Elementgrenze über einer Gratkante erzeugt einen Fehler. |

**Deckung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14-08 | Muss | Die Klasse der Zusatzmaßnahme wird mit erhöhten Anforderungen aus dem Modell (Sparrenlänge, Schneelast, Windzone) und dem Schutz der Traglattung ermittelt. | 14.3.1, ANF-09-25 | RDN 30°, DN 17°: Klasse K1 und Maßnahme Traglattung (Unterschreitung 13° > 12°). Schneelast 1,5 kN/m² gilt als erhöhte Anforderung; zwei erhöhte Anforderungen ergeben dieselbe Klasse wie eine. |
| ANF-14-09 | Muss | Eine Dachneigung zwischen Hersteller- und ZVDH-RDN ist `freigabepflichtig`; aufgelöst nur durch Freigabe der Firma mit Vereinbarung als Dokument. | E14.6 | ZVDH-RDN 22°, Hersteller-RDN 16°, DN 18°: `freigabepflichtig`; nach Freigabe `erfuellt` mit Nachweisstatus „abweichend freigegeben“ und Dokument-Hash. |
| ANF-14-10 | Muss | Die Lattung wird aus dem Datenblatt berechnet; ohne Lösung wird `verletzt` mit Alternativen gemeldet, ohne Datenblattwert `unbestimmt`. | E14.7, Bsp. 14.3 | Linea (LA 373–393, LAT 370, LAF 40): L = 6 000 mm → keine Lösung; L = 6 714 mm → keine Lösung, Alternativen „Überstand ≤ 0,486 m“ (n = 16) und „≥ 0,531 m“ (n = 17). LAF fehlt: `unbestimmt`. |
| ANF-14-11 | Muss | Die Deckung wird im (u, v)-System ausgebreitet; jede Ziegelposition hat genau eine Klasse; Formziegel werden je Meter Kante gerechnet. | 14.3.4 | First 13,00 m mit 2,7 St./m: 36 Firstziegel. Summe der Deckflächen = Flächeninhalt ± eine Ziegeldeckfläche. |
| ANF-14-12 | Muss | Traufe, Ortgang, Kehle, Mansardknick und Gaubenanschluss werden als Regeln der jeweiligen Kante geprüft. | 14.3.5 | Deckungsüberstand an der Traufe 4 cm: Traufblech gefordert. Kehlüberdeckung 9 cm: `verletzt`. Ortgangziegel mit Lappen 0,5 cm vor der Giebelwand: `verletzt`. |
| ANF-14-13 | Muss | Jeder First- und Gratziegel trägt ein Befestigungsmittel; Summe ≥ 0,60 kN/m. Klammerbedarf ist ohne Windsogrechnung `unbestimmt`, über 65° wird jeder Ziegel geklammert. | 14.3.5 | First ohne Befestigungsmittel: IDS-Befund. DN 50° ohne Windsogrechnung: `unbestimmt`; DN 70°: Klammer an jedem Ziegel. |

**Einbauteile und Entwässerung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14-14 | Muss | Rettungsfenster nach `BY.BayBO.35-4.Rettungsfenster`: lichte Maße, Unterkante über Fußboden, Abstand zur Traufkante; `FireExit = TRUE`. | 14.4.1 | Lichte 0,60 × 1,00 m, Unterkante 1,20 m, 1,00 m zur Traufkante: `erfuellt`. Lichte Breite 0,59 m: `verletzt`, Alternative „nächstgrößeres Fenster“. |
| ANF-14-15 | Muss | Brandschutzabstände: Dachfenster 1,25 m, Solaranlagen 0,50 m zu Brandwänden und Gebäudeabschlusswänden, soweit nicht über Dach geführt. | 14.4.1, 14.6.1 | Doppelhaus, Dachfenster 1,20 m von der Haustrennwand: `verletzt`; PV-Modul 0,45 m: `verletzt`; Wand 0,30 m über Dach geführt: beide `nicht_anwendbar`. |
| ANF-14-16 | Muss | Einbauteile sind Tripel aus Produkt, Öffnung und Deckungsteil; der Eindeckrahmen passt zu Profilhöhe und Neigung. | E14.8 | Löschen des Eindeckrahmens erzeugt einen IDS-Befund. Rahmen EDW bei DN 14°: `verletzt` (Bereich 15–90°). |
| ANF-14-17 | Muss | Wechsel werden aus Herstellertabellen gesetzt; vorher wird eine Verschiebung um weniger als eine halbe Sparrenteilung als Alternative geprüft. | 14.4.1 | 20 cm Dachdicke, 45°: Wechselabstand oben und unten 21,1 cm. Fenster, das nach Verschiebung zwischen die Sparren passt: Alternative A1 statt Wechsel. |
| ANF-14-18 | Muss | Die Fallleitung über Dach mündet ohne Abdeckung (offene Kappe); mindestens eine Fallleitung je Gebäude wird über Dach geführt. | 14.4.2 | Fallleitung mit geschlossener Kappe: `verletzt`. Zwei Fallleitungen, eine über Dach, eine mit Belüftungsventil: `erfuellt`. |
| ANF-14-19 | Muss | Die Dachentwässerung rechnet mit r(5,5) aus KOSTRA-DWD-2020 und weist r(5,2) als Vergleich aus; Rasterfeld, Version und Abrufdatum stehen im Nachweis. | E14.9, Bsp. 14.4 | 35,75 m², r = 290 l/(s·ha): Q = 1,04 l/s (wie B17 RF1–RF4). Ohne Regenspende r(5,5): `unbestimmt`. Fallrohr DN 70: `verletzt`. |

**Photovoltaik und Fassade**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14-20 | Muss | Die Solar-Soll-Regel ist weich: Sollfläche ≥ 1/3 der geeigneten Fläche als Hinweis; Gestaltungssatzungen gehen vor. | 14.6.1, Bsp. 14.5 | Südfläche 87,3 m², ohne Anlage: Hinweis „Sollfläche 29,1 m²“, Ergebnis nicht `verletzt`. Satzung schließt Anlagen aus: `nicht_anwendbar`. |
| ANF-14-21 | Muss | Die Belegung hält Sperrflächen und die RDN-Grenze der Dachhaken hart ein und wird nach Änderung von Geometrie, Lattung oder Einbauteil neu gerechnet. | E14.10 | Kein Modul im 0,50-m-Streifen. DN unter RDN mit Dachhaken: `verletzt`; mit Systemziegel und DN ≥ 10°: `erfuellt`. |
| ANF-14-22 | Soll | Der Ertrag wird mit pvlib und PVGIS gerechnet; die Antwort wird mit Hash gespeichert und bei gleicher Eingabe wiederverwendet. | 14.6.3 | Anfrage enthält `peakpower`, `loss`, `angle`, `aspect` (0 = Süd) und `mountingplace=building`; zweiter Lauf ohne Netz liefert dasselbe Ergebnis. |
| ANF-14-23 | Muss | Aus dem Inbetriebnahmedatum werden die Registrierfrist im Marktstammdatenregister und der Hinweis zur Einspeisegrenze erzeugt. | 14.6.1 | Inbetriebnahme 01.10.2026: Frist 01.11.2026; Anlage < 100 kW mit Einspeisevergütung: Hinweis „60 % Wirkleistung“. |
| ANF-14-24 | Muss | Holzschalung nach Fachregel 01: Geltung bis 10 m Firsthöhe, Brettdicke ≥ 18 mm, Breite ≤ 11 · Dicke, Sockelabstand. | 14.7.1 | Brett 20 × 240 mm: `verletzt`, Alternativen „22 mm Dicke“ oder „≤ 220 mm Breite“. Firsthöhe 10,5 m: `nicht_anwendbar` mit Hinweis. |
| ANF-14-25 | Muss | Eine verputzte Holzfaserfassade braucht die Zulassungs- oder Genehmigungsnummer des Systems als R2-Merkmal. | 14.7.2 | Ohne Nummer: Nachweis der Außenwand im Reifegrad R `unbestimmt`. |
| ANF-14-26 | Muss | Farben werden als Code gespeichert; RGB-Werte dienen nur der Darstellung. | 14.7.3 | Jede Farbwahl hat einen Farbcode mit System (RAL, NCS, Hersteller); die Bemusterungsausgabe enthält keinen RGB-Wert als Vertragsangabe. |
| ANF-14-27 | Muss | Dachform, Neigung und Farben werden gegen bestätigte Gestaltungsfestsetzungen (`BP_Dachgestaltung`) geprüft. | 14.7.3 | DNmin 30°, DNmax 40°, DN 28°: `verletzt`, Alternative A1 „30°“. Festsetzung nicht bestätigt: `unbestimmt`. |
| ANF-14-28 | Muss | Dach, Deckung, Einbauteile, PV und Fassade folgen `ifc-mapping.csv`; Latten und Sondersparren sind USERDEFINED mit Vokabular. | 14.2.1, E8.15 | 0 `IfcBuildingElementProxy`; jede Latte ist `IfcMember` USERDEFINED „BATTEN“; Validierung mit 0 Meldungen. |
| ANF-14-29 | Soll | Texturkoordinaten von Dach und Fassade folgen dem (u, v)-System des Verlegerasters. | E14.11, ANF-08-30 | Die Texturwiederholung in v entspricht der gewählten Lattweite; die GLB enthält `TEXCOORD_0` für jede Dach- und Fassadenfläche. |

### 14.10.3 Datenstrukturen und Parameter

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `dach.form` | enum | – | GABLE, HIP, HIPPED_GABLE, PAVILION, SHED, MANSARD, GAMBREL, FLAT | Tab. 14.1 |
| `dach.kante[i].neigung` | float | ° | 0 (Giebel) bis 90; Deckung 10–90 | E14.1 |
| `dach.kante[i].traufhoehe` | float | m | über OKFF EG | E14.1, [@held2017roofs] |
| `dach.ueberstand_traufe`, `dach.ueberstand_ortgang` | float | m | 0–1,5 | Parametermodell |
| `kante.art` | enum | – | TRAUFE, ORTGANG, FIRST, GRAT, KEHLE, KNICK, PULTFIRST, WANDANSCHLUSS | E14.3 |
| `kante.laenge_wahr`, `kante.neigung_beta` | float | m, ° | ≥ 0 | E14.3 |
| `tragwerk.sparrenraster` | int | mm | Herstellerwert | DAT-14-01 |
| `deckung.modell_id` | string | – | Schlüssel eines Datenblatts | Schema 14.10.1 |
| `deckung.rdn_zvdh`, `deckung.rdn_hersteller` | float | ° | 10–60 | E14.6 |
| `deckung.klasse` | int | – | 1–5 oder null | `DE.ZVDH.DZ.Dachneigung` |
| `lattung.LA`, `lattung.LAT`, `lattung.LAF` | float | mm | Datenblatt | E14.7 |
| `lattung.n` | int | – | ≥ 1 | E14.7 |
| `kehle.art` | enum | – | METALL, NOCKEN, BIBER_EINGEBUNDEN, BIBER_UEBERDECKT, DREIPFANNEN, FORMZIEGEL, SCHWENKZIEGEL | 14.1.5 |
| `einbauteil.tripel` | object | – | {produkt, oeffnung, deckungsteil} (GlobalIds) | E14.8 |
| `entwaesserung.r_5_5`, `entwaesserung.r_5_2` | float | l/(s·ha) | KOSTRA-Rasterfeld | E14.9 |
| `pv.system` | enum | – | AUFDACH, INDACH | 14.6.2 |
| `pv.sollflaeche` | float | m² | ≥ 0 | Art. 44a Abs. 4 |
| `fassade.art` | enum | – | STUELP, BODEN_DECKEL, DECKLEISTE, LEISTEN_DECKEL, OFFEN, PUTZ_HOLZFASER | 14.7.1–2 |
| `fassade.brett_dicke`, `fassade.brett_breite` | int | mm | ≥ 18; ≤ 11 · Dicke | 14.7.1 |
| `fassade.zulassung_nr` | string | – | DIBt-Nummer | 14.7.2 |
| `farbe.system`, `farbe.code` | string | – | RAL, NCS, Hersteller | 14.7.3 |

### 14.10.4 Datenlieferungen von Regnauer

| ID | Gegenstand | Format | Ersatzwert bis zur Lieferung | Anforderungen |
|---|---|---|---|---|
| DAT-14-01 | Dachformen, Neigungsbereiche, Gaubentypen, Tragwerkstyp, Sparrenraster und Standardquerschnitte; Umfang der Dachvorfertigung (präzisiert DAT-06) | Tabelle je Dachtyp | Thermo-Vitaldach als Pfettendach; Dachelemente wie B18 | ANF-14-01, -05, -07 |
| DAT-14-02 | Ziegel- und Steinmodelle der Lieferanten mit Datenblatt (LA, DB, LAT, LAF je Neigung, Schnürmaße, Zubehör), möglichst digital | JSON nach `dachdeckung-herstellerdaten.schema.json` oder Excel | Beispieldatensätze Erlus Linea und Braas Doppel-S, Status [U] | ANF-14-10, -11 |
| DAT-14-03 | Standard der Zusatzmaßnahme und ob Hersteller-RDN vertraglich vereinbart wird | Tabelle | ZVDH-RDN, Klasse nach Rechnung | ANF-14-08, -09 |
| DAT-14-04 | Standardausführung von First, Grat, Kehle und Ortgang, Befestigungssystem | Tabelle je Detail | Metallkehle, Trockenfirst | ANF-14-12, -13 |
| DAT-14-05 | Dachfenster: Hersteller, Typen mit lichten Maßen, Eindeckrahmen; Regel zur Festlegung von Rettungsfenstern | Typliste mit Datenblatt | Velux-Werte aus Recherche 09 | ANF-14-14, -16, -17 |
| DAT-14-06 | Lage und Durchmesser von Sanitärlüfter und Kamin, Lüfterziegelsystem, Vorbereitung im Werk | Tabelle | Lüfter Ø 125/160 mm mit offener Kappe | ANF-14-18 |
| DAT-14-07 | Photovoltaik: Indach oder Aufdach, Partnerfirma, Moduldatenblätter (PAN/OND), Montagesystem und Statiknachweis, Umgang mit der 0,50-m-Regel | Datenblätter, Nachweis | keine Modulzahl, nur Sollfläche | ANF-14-20, -21, -22 |
| DAT-14-08 | Fassadenvarianten: Schalungstypen, Putzsystem mit Zulassungsnummer je Wandtyp, Farbkollektionen | Tabelle, Zulassungsbescheide | Fachregel-Werte; Nachweis `unbestimmt` | ANF-14-24, -25, -26 |
| DAT-14-09 | Dachentwässerung: Material, Rinnengrößen, Zahl und Lage der Fallrohre, Zuständigkeit für die Bemessung | Tabelle | halbrunde Rinne, vier Fallrohre | ANF-14-19 |
| DAT-14-10 | Abbundsoftware und Import von BTLx für Sparren und Pfetten; gewünschter Detaillierungsgrad der Visualisierung | Beispieldateien, Angabe | BTLx 2.3 aus compas_timber | ANF-14-06, -29 |
| DAT-14-11 | Lizenz der ZVDH-Fachregel mit Merkblättern und „Hinweisen zur Lastenermittlung“ sowie der Fachregel 01 (über Regnauer als Mitgliedsbetrieb oder Kauf) | Lizenz, Volltext | Gelbdruck-Werte mit [U] | ANF-14-08, -12, -13, -24 |

## Verwendete Schlüssel

Das Kapitel enthält 44 Zitatstellen zu 31 Schlüsseln. Zugeordnet ist jeweils die Bib-Datei, in der der Schlüssel steht.

**lit-A-acc-bim.bib** (1): `iso2024ifc`

**lit-B-vorfertigung-ki.bib** (1): `compastimber`

**lit-C-recht-normen.bib** (5): `baybo2026`, `btlx23`, `regnauerBLB2024`, `xplanung`, `zvdh2024`

**lit-D-vergleich-vorfertigung.bib** (2): `buildinwood2024`, `piroozfar2019configuration`

**lit-E-vergleich-automation.bib** (5): `aichholzer1995novel`, `apolinarska2016mastering`, `kelly2011interactive`, `kelly2014unwritten`, `laycock2003automatically`

**lit-I-schneeball-b.bib** (14): `ahn2013roofs`, `aichholzer1996general`, `biedl2015weighted`, `dineniso7817-1`, `edelsbrunner2016roofs`, `eder2018volume`, `eder2021exact`, `eppstein1999raising`, `held2017roofs`, `kozniewski2020roof`, `mueller2006procedural`, `ren2021roof`, `vareilles2013renovation`, `wonka2003instant`

**lit-J-schneeball-runde2.bib** (3): `huber2012fast`, `laycock2003generating`, `sugihara2013automatic`

### Python-Key-Check

Am 27.09.2026 wurden alle `[@key]` im Text mit einem Python-Skript gegen die Schlüssel aus `literatur/lit-*.bib` abgeglichen, ebenso die 8 Schlüssel in den Feldern `bib` von `spezifikation/regelkatalog-14-dach.yaml`:

```text
Zitatstellen 44, Schlüssel 31, fehlend 0
YAML-Schlüssel 8, fehlend 0
```

Ergebnis: **0 fehlend.** Keiner der Schlüssel steht in mehr als einer Bib-Datei.

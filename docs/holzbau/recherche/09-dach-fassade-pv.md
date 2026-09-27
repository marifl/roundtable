# Recherche 09: Dach, Fassade, PV – präsentations-, prüf- und ausführungsfertig

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft oder maschinell nachvollzogen (IfcOpenShell 0.8.5 mit Schema IFC4X3_ADD2, Crossref-Abfrage, Testlauf). **[U]** = unsicher, Sekundärquelle oder eigene Herleitung. **[E]** = Wert aus dem ZVDH-Gelbdruck vom 01.07.2023. Die Endfassung 04/2024 konnte ich nicht im Volltext einsehen; Abweichungen sind möglich.

## Ergebnis in 5 Punkten

1. **Das Regelwerk lässt sich als Tabellen fassen, liegt aber hinter einer Bezahlschranke.** Die Kernwerte der ZVDH-Fachregel Dachziegel/Dachsteine (04/2024) sind über Herstellerbroschüren belegbar [V]:
   - RDN-Klassen 22/25/30/35/40°, Mindestdachneigung 10°,
   - Zusatzmaßnahmen Klasse 1–5 je RDN,
   - Kehlsparren-Neigungsgrenzen.

   **Wichtige Korrektur:** Seit 04/2024 gibt es nur noch die Klassen 1–5, nicht mehr 1–6. Der Volltext ist kostenpflichtig (Rudolf Müller). Deshalb gehört jeder Wert mit Fundstelle in eine eigene Regeltabelle.
2. **Die Herstellerdaten genügen für einen Lattweiten-Algorithmus.** Pro Modell veröffentlichen Creaton/Wienerberger, Braas, Erlus und Nelskamp Deckbreite und Lattweite als Min/Max, dazu LAT/LAF-Tabellen je Dachneigung [V]. Offen ist, ob diese Daten maschinenlesbar zu bekommen sind (kein BMEcat/ETIM für Dachziegel gefunden [U]). BIM-Objekte gibt es meist nur als DWG/RFA über Heinze/BIMobject, mit Nutzungsbedingungen der Portale.
3. **Die Dachgeometrie ist gelöst.** CGAL (ab 5.6) enthält gewichtete Straight Skeletons und `extrude_skeleton()` mit Winkel je Kante; Gewicht 0 ergibt eine senkrechte Giebelkante [V]. Damit sind Walm-, Zelt- und Satteldach abgedeckt, ebenso Pult (Traufwinkel an einer Kante, übrige Kanten als Wände [U]). Krüppelwalm und Mansarde entstehen in zwei Stufen. Die Python-Bausteine polyskel (LGPL-3), bpypolyskel (GPL-3) und skgeom (LGPL-3) taugen nur für ungewichtete Skelette.
4. **IFC 4.3 bildet Dach, Einbauteile und PV schemakonform ab.** Das Testmodell ist fehlerfrei validiert [V]: IfcRoof `HIPPED_GABLE_ROOF`/`MANSARD_ROOF`/`PAVILION_ROOF`/`SHED_ROOF`, IfcWindow `SKYLIGHT`, IfcSolarDevice `SOLARPANEL`, IfcStackTerminal `COWL`, IfcPipeSegment `GUTTER` und IfcCovering `ROOFING`/`CLADDING` mit Textur. **Aber:** Der glTF-Export von IfcOpenShell übernimmt nur Farben, keine Texturen [V]. Texturen brauchen einen eigenen Nachbearbeitungsschritt.
5. **Drei Rechtsannahmen im Auftrag sind falsch oder veraltet [V]:**
   - Das Rettungsfenster nach BayBO misst **0,60 × 1,00 m**, nicht 0,90 × 1,20 m (Art. 35 Abs. 4, Fassung ab 01.05.2026).
   - Die bayerische Solarpflicht ist für Wohngebäude nur eine **Soll-Vorschrift** (Art. 44a Abs. 4).
   - Aktuell gilt die **VDE-AR-N 4105:2026-03**.

   Dazu kommen die 60-%-Einspeisegrenze (§ 9 Abs. 2 EEG, seit 25.02.2025) und die Dachentwässerung mit **r(5,5)** statt r(5,2).

## 1. ZVDH-Regelwerk: Regel – Kernwert – Quelle – Status

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Geltung | Dachneigung ≥ 10° (Mindestdachneigung) | FR Dachziegel/-steine 04/2024, 1.1 (baunormenlexikon) | [V] |
| RDN 22° | Ringfalz: Flachdachziegel, Romanische | FR Tab. 3 | [E] |
| RDN 25° | Doppelmuldenfalz im Verband; Glatt-, Reform- und Verschiebeziegel „mit besonderen Merkmalen“ | FR Tab. 3 | [E] |
| RDN 30° | Doppelmulden-, Reform-, Glatt- und Verschiebeziegel; **Biber Doppel-/Kronendeckung** | FR Tab. 3 | [E] |
| RDN 35° | Strangfalz, Krempziegel, Hohlpfanne in Aufschnittdeckung | FR Tab. 3 | [E] |
| RDN 40° | Hohlpfanne in Vorschnitt- oder Einfachdeckung, Mönch/Nonne, Biber-Einfachdeckung mit Spließen | FR Tab. 3 | [E] |
| Zusatzmaßnahme RDN 22° | ≥10° K1; ≥14° K3; ≥18° K4; ≥22° K5. Mit erhöhter Anforderung: K1/K2/K3/K4 | proclima-/Pavatex-/Walther-Broschüren nach FR 04/2024 | [V] |
| RDN 25° | ≥13° K1; ≥17° K3/K2; ≥21° K4/K3; ≥25° K5/K4 | dto. | [V] |
| RDN 30° | ≥18° K2/K1; ≥22° K3/K2; ≥26° K4/K3; ≥30° K5/K4; unter 18° K1 | dto. | [V] |
| RDN 35° | ≥23° K2; ≥27° K3; ≥31° K4/K3; ≥35° K5/K4; unter 23° K1 | dto. | [V] |
| RDN 40° | ≥28° K2; ≥32° K3; ≥36° K4/K3; ≥40° K5/K4; unter 23° K1 | dto. | [V] |
| Erhöhte Anforderungen | Sparrenlänge > 10 m (DN 10°) bis > 13 m (DN 40°); konzentrierter Wasserlauf; geschweifte Gauben, Tonnen- und Kegeldächer; Schneelast ≥ 1,5 kN/m²; Windzone 4, Kamm- oder Gipfellage. **Sie werden nicht aufaddiert** | dto.; ddh.de 11.06.2024 | [V] |
| Objektplanung Pflicht | Sparrenlänge > 15 m, extreme Lagen | FR 1.2 (5) | [E] |
| Traglattung | Wird die RDN um mehr als 12° unterschritten, müssen Maßnahmen die Traglattung schützen | FR 1.2 (7) | [E] |
| Klassen (Merkblatt) | K1 wasserdichtes Unterdach oder UDB-eA mit eingebundener Konterlatte (≥10°); K2 regensicheres Unterdach oder UDB-eA mit Nageldichtung (≥14°); K3 verklebte UDB/USB mit Nageldichtung oder Holzfaser-UDP (≥14°); K4 verklebt (≥18°); K5 überlappt (≥22°) | Merkblatt Unterdächer 04/2024 (Mahler-Zusammenfassung) | [V] |
| Kehle, Neigungsgrenzen | Metallkehle: Dachneigung ≥10°. Nocken- und Biberkehle eingebunden: Kehlsparren ≥25°. Biberkehle überdeckt: ≥30°. Dreipfannen-, Formziegel- und Schwenkziegelkehle: ≥35° | FR 4.6.1 Tab. 21 | [E] |
| Kehle, Überdeckung | Die Fläche überdeckt die Kehle ≥ 10 cm, rechtwinklig zur Kehllinie gemessen | FR 4.6.1 (6) | [E] |
| Metallkehle (Metall-Fachregel) | Blechstöße: ≥100 mm (>22°), ≥150 mm (15–22°), unter 15° wasserdicht. Kehlzuschnitt ≥ 400 mm, Kehlschalung lichter Abstand < 130 mm | dach-holzbau.de 2020 (zitiert FR Metall 7.2/7.3) | [U, ältere Fassung] |
| First/Grat | Trocken oder Mörtel; konische Firstziegel ≥ 4 cm Überdeckung. Jeder Formziegel wird mechanisch befestigt, **0,60 kN/m**. Schraube 4,5 mm, Einschraubtiefe ≥ 24 mm. Mörtel zählt nicht als Windsogsicherung | FR 1.4, 4.3, 4.4 | [E] |
| Traufe | Überstand < 5 cm verlangt Traufblech. Traufreihe mit gleicher Neigung (Traufbohle/Doppellatte). Lüftungsebene offen | FR 4.1 | [E] |
| Ortgang | Ortgangziegel: Innenkante Lappen ≥ 1 cm von der Giebelwand. Flächenziegel/Doppelwulst: Überstand ≥ 3 cm | FR 4.2 (4) | [E], Creaton bestätigt 1 cm [V] |
| Mansard-/Schleppknick | Stirnbrett, Formziegel, Metall oder Fertigelement. Obere Reihe steht über. Unterdach objektspezifisch | FR 4.15 | [E] |
| Gauben | Gleiche Neigungsgrenzen wie das Hauptdach. Die letzte Reihe vor der Gaube sollte durchgedeckt werden | FR 4.12 | [E] |
| Windsog | Klammerbedarf objektspezifisch nach „Hinweise zur Lastenermittlung“ 4.2.2. Über 65° jeden Ziegel klammern | FR 1.4 | [E] |
| Solarhalter | Dachhaken ab RDN des Ziegels; Systemziegel (formschlüssig) ab 10° | FR 4.10 (3); K2-Systems 04/2024 | [V] |

**Öffentlich oder kostenpflichtig:**

- Öffentlich: Regelübersicht mit Ausgabedaten (dachdecker.org) [V], Inhaltsverzeichnis (baunormenlexikon) [V] und der Gelbdruck vom 07/2023 (Einspruchsfassung, frei im Netz) [V].
- Kostenpflichtig: Volltext von Fachregeln, Merkblättern und „Hinweise Lastenermittlung“ (Ordner, DVD, online, dachdecker-regelwerk.de). Die Windsog-Rechenhilfen stehen auf der DVD [V].

## 2. Dachziegel-Hersteller: Daten, Formate, Lizenz

| Hersteller | Beispiel-Datensatz [V] | Rechner/Tools | BIM/CAD | Lizenz |
|---|---|---|---|---|
| Creaton (seit 03/2024 Teil von **Wienerberger**, Marke bleibt; Koramic im selben Haus [V]) | „Technik kompakt 08/2025“: je Modell Deckbreite min/Mittel/max (z. B. 260/262/263 mm), Decklänge 380–420 mm, Stück/m², kg/Stück; **LAF/FLA-Tabelle je DN 10–60°**. Hersteller-RDN z. B. 16° | Visualisierung, Windsog- und Schneelastrechner | BIM-Bibliothek (2D/3D, Click2CAD), CAD je Formziegel (FLA, OGL, OGR, FALZ, LUEFTZ, SOLAR, ANTENNE …) | Herstellerbedingungen [U] |
| Braas (BMI) | Datenblatt Doppel-S: Decklänge 312–345 mm, Deckbreite 300 mm, LA je DN-Bereich, LAF 40 mm, PÜT/LAT 0–80/400–320 mm. Turmalin: LAF-Tabelle je Lattung 30/50 und 40/60 | Windsog-Service, CAD-Browser (DWG), 7GRAD-Dach | Heinze/ais: „BIM-Daten Download“ je Formstein (Mansard-, Knick-, Lüfter-, Antennen-, Abgasrohr-Durchgang) | Portalbedingungen [U] |
| Erlus (Neufahrn/Ergoldsbach, **Bayern**) | Linea: Lattweite 37,3–39,3 cm, Deckbreite 24,5 cm, **Lattweitengruppe 38,5 cm**, Schnürmaß Ortgang links/rechts, mittleres Traufenlattmaß, Pultziegel-Lattweite; RDN 25° (Verband)/30° (Reihe); Hagelwiderstandsklasse. 22 Formen, 31 Farben | Unterdach-Konfigurator, Schneesicherungsrechner, Profi-App | Download-Center (Produktblätter, Zeichnungen) | [U] |
| Nelskamp | D 15 Ü: Decklänge 34,4 cm ± 8 mm, Deckbreite 20,8 cm, RDN 30°, Zubehörbedarf je m (First 2,7 St./m, Trauflüftung 200 cm²/m); Herstellervorschrift hat ausdrücklich Vorrang vor der ZVDH-Regel | – | – | [U] |
| Jacobi Walther | „Bedachung nach Maß 04/2024“: RDN-Übersicht aller Modelle, Stylist 30° (Reihe)/25° (Verband), Lattweitenübersicht, Mindestlüftungsquerschnitte | – | – | [U] |
| Röben | nicht geprüft | – | – | [U] |

**Formen:**

- Flachdach- und Flachziegel, Doppelmuldenfalz, Reformpfanne,
- Hohlfalz, Glatt- und Verschiebeziegel, Biber (Segment-, Rund-, Geradschnitt), Mönch/Nonne, Hohlpfanne.

**Oberflächen:**

- Tonziegel: naturrot, engobiert, edelengobiert, glasiert.
- Dachsteine: beschichtet (z. B. Braas Protegon, Starmatt) [V, Datenblätter].
- Farbwerte (RGB) veröffentlichen die Hersteller nicht [U]. Farbwerte und Texturen müssen daher aus Fotos oder Mustern selbst erstellt werden.

**Datenformate:**

- BMEcat und ETIM sind im Baustoffhandel verbreitet. Eine ETIM-Klasse „Dachziegel“ mit Deckmaß-Merkmalen konnte ich nicht nachweisen [U].
- Praktikabler Weg: pro Modell ein eigenes JSON-Datenblatt, abgeleitet aus den PDFs und versioniert mit Quellen-PDF und Datum. Die Felder zeigt das Schema unten.

**Warnung:** Die Hersteller-RDN (Creaton/Wienerberger 14–16°, Erlus E58 RS 16°) liegen **unter** der ZVDH-RDN (22°). Wer sie nutzen will, muss das laut ZVDH/DDH vertraglich vereinbaren [V, ddh.de 2024]. Der Generator muss beide RDN führen und standardmäßig mit der ZVDH-RDN rechnen.

```json
{"modell":"Linea","hersteller":"Erlus","art":"Glattziegel","rdn_zvdh":30,"rdn_hersteller":{"verband":25,"reihe":30},
 "lattweite_mm":[373,393],"deckbreite_mm":{"mittel":245},"lat_mm":370,"laf_mm":{"10":..},"schnuermass_ortgang_mm":{"links":115,"rechts":210},
 "zubehoer":["FAL","OGL","OGR","Lüfter","Sanitärlüfter","Solar","Antenne","Firstziegel","Gratanfang"],"quelle":"erlus.com Produktblatt, abgerufen 2026-09-27"}
```

**Dachdurchdringungen (Beispiel Creaton/Koramic 2025):**

- Solardurchgang Ø 70 mm, Antenne Ø 40–60 mm, Thermendurchführung Ø 110/125 mm (7–50°).
- Dunstrohr/Lüfter Ø 125/160 mm mit **offener Kappe für Fallleitungen**, geschlossener Kappe für Lüftungsleitungen [V].
- Das passt zu DIN 1986-100:2016-12. Danach dürfen an der Mündung von Lüftungsleitungen über Dach **keine Abdeckungen** sitzen, und jede Fallleitung wird als Lüftung über Dach geführt (6.5.1). Im EFH genügt eine Fallleitung über Dach, die übrigen dürfen Belüftungsventile haben [V, baunormenlexikon/DIN-FAQ].
- Mündung ≥ 15 cm über der Dachfläche, 1 m über oder 2 m neben Dachfenstern [U, Sekundärquelle SBZ].

## 3. Dachfenster

| Thema | Befund | Status |
|---|---|---|
| BIM Velux | BIM-/3D-Objekte über velux.com, BIMobject und BIMsmith; Revit, ArchiCAD, SketchUp, DWG | [V] |
| BIM Roto | ArchiCAD- und Revit-Komplettpakete (186/149 MB), BIMobject-Einträge mit IFC-Klassifikation „Window“ | [V] |
| BIM Fakro | Archispace und BIMobject (AutoCAD, Revit, ArchiCAD, 3ds Max) | [V] |
| Eindeckrahmen Velux | **EDW** (profiliert, 1,5–12 cm, 15–90°, Standardeinbau). **EDJ** (bis 9 cm, 20–90°, vertieft −4 cm). **EDZ/EDN** (flach bis 16 mm). Kombi-Rahmen EKW/EKT/EKB/EKS/EKL. Variante 2000 enthält BDX-Dämmrahmen und BFX-Unterdachschürze | [V] |
| Sparrenabstand | Ideal: lichtes Sparrenmaß = Blendrahmenbreite + 6 cm (mit BDX ab +4/+5 cm). Kombi nebeneinander: Mittelrinne 10–16 cm. Übereinander: 10 cm, mit Rollladen 25 cm | [V] |
| Wechsel | Velux-Tabelle „Wechselabstände“: Mindestabstände oben/unten je Dachdicke und DN, inklusive ≥ 10 cm Sicherheit (z. B. 20 cm Dachdicke, 45°: 21,1/21,1 cm). Für waagerechtes Sturzbrett und senkrechtes Brüstungsfutter | [V] |
| Rettungsweg BayBO | **Art. 35 Abs. 4:** lichte Breite ≥ 0,60 m, Höhe ≥ 1,00 m, von innen zu öffnen, Unterkante ≤ 1,20 m über Fußboden. In Dachschrägen: Unterkante oder Austritt horizontal ≤ 1 m von der Traufkante | [V, gesetze-bayern.de, gilt ab 01.05.2026] |
| Brandschutz | Dachflächenfenster ≥ 1,25 m von Brandwänden bzw. Gebäudeabschlusswänden, sofern diese nicht ≥ 0,30 m über Dach geführt sind (Art. 30 Abs. 5). Dachfenster von Wohngebäuden sind von der harten Bedachung ausgenommen (Abs. 3 Nr. 3) | [V] |
| IFC | IfcWindow `SKYLIGHT`, `Pset_WindowCommon.FireExit=TRUE` für das Rettungsfenster, Eindeckrahmen als IfcDiscreteAccessory `FLASHING` | [V, Testmodell] |

## 4. Dachgeometrie-Algorithmen (Literatur per Crossref geprüft)

| Arbeit | DOI | Nutzen | Status |
|---|---|---|---|
| Aichholzer, Aurenhammer, Alberts, Gärtner: A Novel Type of Skeleton for Polygons (J.UCS 1995; Buchausgabe 1996) | 10.1007/978-3-642-80350-5_65 | Definition Straight Skeleton, Dachmodell | [V] |
| Aichholzer, Aurenhammer: Straight skeletons for general polygonal figures (COCOON 1996) | 10.1007/3-540-61332-3_144 | Verallgemeinerung | [V] |
| Eppstein, Erickson: Raising Roofs, Crashing Cycles, and Playing Pool (DCG 1999) | 10.1007/PL00009479 | Algorithmus, Komplexität | [V] |
| Felkel, Obdržálek: Straight Skeleton Implementation (SCCG 1998) | keine DOI gefunden | Grundlage von polyskel; in Sonderfällen fehlerhaft | [U] |
| Laycock, Day: Automatically generating large urban environments based on the footprint data of buildings (SM ’03) | 10.1145/781606.781663 | Dachgenerierung aus Grundrissen (von CGAL zitiert) | [V] |
| Huber, Held: A fast straight-skeleton algorithm based on generalized motorcycle graphs (IJCGA 2012) | 10.1142/S0218195912500124 | robuste Implementierung | [V] |
| Biedl et al.: Weighted straight skeletons in the plane (CGTA 2015) | 10.1016/j.comgeo.2014.08.006 | gewichtete Skelette: Theorie und Mehrdeutigkeiten | [V] |
| Held, Palfrader: Straight skeletons with additive and multiplicative weights … roofs and terrains (CAD 2017) | 10.1016/j.cad.2017.07.003 | **direkt Dachgenerierung mit Neigungen** | [V] |
| Kelly, Wonka: Interactive architectural modeling with procedural extrusions (TOG 2011) | 10.1145/1944846.1944854 | Mansarde, Gauben und Profile als gewichtete Extrusion | [V] |
| Müller et al.: Procedural modeling of buildings (SIGGRAPH 2006) | 10.1145/1179352.1141931 | CGA-Regeln (Dach, Fassade) | [V] |
| Sugihara: Straight Skeleton Computation Optimized for Roof Model Generation (2019) | 10.24132/CSRN.2019.2901.1.12 | Walm/Satteldach aus Grundriss | [V] |
| Kada, McKinley: 3D building reconstruction from LiDAR based on a cell decomposition approach (ISPRS Archives 2009) | keine Crossref-DOI | Zellzerlegung und Dachprimitive (eher Rekonstruktion) | [U] |

**Algorithmen für den Generator [U, eigener Entwurf auf Basis der Quellen]:**

1. **Walm und Zelt:** Grundrisspolygon mit einheitlichem Neigungswinkel an `CGAL::extrude_skeleton(angles=…)`.
2. **Satteldach:** Giebelkanten erhalten Gewicht 0 (senkrecht) [V, CGAL-Doku].
3. **Pult:** Nur die Traufkante bekommt einen Winkel; die übrigen Kanten sind Wände [U].
4. **Krüppelwalm:** Bei rechteckigem (konvexem) Grundriss ist die Dachfläche die untere Hülle der Kantenebenen. Also z = min(Satteldachebenen, Walmebene um die Krüppelhöhe angehoben). Bei konkavem Grundriss muss man die Skelettflächen mit einer Höhenschranke schneiden.
5. **Mansarde:** Stufe 1 ist eine steile Extrusion mit `maximum_height = Knickhöhe`. Das liefert die Offsetkontur (CGAL-Offset). Stufe 2 extrudiert diese Kontur flach. Die Knicklinie wird ein eigenes Detail („Mansardknick“, FR 4.15).
6. **Gauben:** Eigene Kleindächer (Schlepp-, Sattel-, Walm- oder Flachgaube). Verschnitt mit der Hauptdachfläche ergibt Kehlen und Anschlusslinien, im IFC als IfcOpeningElement in der Hauptdach-IfcSlab.
7. **Kanten klassifizieren:** Aus dem Skelett lassen sich jeder Kante Traufe, Ortgang, First, Grat, Kehle, Pultfirst, Knick oder Wandanschluss zuordnen, und zwar nach der Lage der Nachbarflächen (konvex = Grat, konkav = Kehle).
8. **Kehl- und Gratneigung:** Bei gleicher Dachneigung α und 90° Grundrisswinkel gilt tan β = tan α / √2. Daraus folgt eine Prüfregel für die Mindestdachneigung (eigene Rechnung [U]):

   | Kehlart (Grenze) | Mindest-α |
   |---|---|
   | Kehlsparren ≥ 25° (Nockenkehle) | 33,4° |
   | ≥ 30° (überdeckte Biberkehle) | 39,2° |
   | ≥ 35° (Dreipfannenkehle) | 44,7° |
   | Metallkehle, Kehlneigung ≥ 15° (Blech überlappt) | 20,8° |
9. **Lattung:** Konstruktionslänge L = n·LA + LAT + LAF (Braas-Verlegeanleitung [V]).

   ```text
   n  = ceil((L − LAT − LAF) / LA_max)
   LA = (L − LAT − LAF) / n
   ```

   Liegt LA unter LA_min, variiert man LAT im zulässigen Bereich (PÜT/LAT). Beispiel Erlus Linea mit L = 6,00 m, LAT = 370, LAF = 40 mm: Bei n = 15 ist LA = 372,7 < 373, bei n = 14 ist LA = 399,3 > 393. **Keine Lösung ohne LAT-Anpassung** [U, eigene Rechnung]. Das zeigt, warum die Tabellenwerte in das Datenblatt gehören.
10. **Deckung als Musterausbreitung:**
    - Im lokalen (u, v)-System jeder Dachfläche entsteht ein Raster aus Reihen v_i und Spalten u_j.
    - Die Spaltenbreite DB liegt zwischen DB_min und DB_max, Ortgangziegel haben eigene Schnürmaße; bei Verband wird jede zweite Reihe um DB/2 versetzt.
    - Jede Ziegelfläche wird mit Shapely gegen das Flächenpolygon geschnitten und nach Typ klassifiziert: voll, geschnitten an Grat oder Kehle, Ortgang, Firstanschluss, Traufe.
    - Als Mengen fallen Stückzahlen, Schnittziegel und Formziegel je lfm an (First und Grat ≈ 2,5–2,9 St./m laut Datenblatt).
    - Literatur speziell zur Ziegel-Musterausbreitung habe ich **nicht** gefunden [U].

## 5. Holz-Dachtragwerk

| Thema | Befund | Status |
|---|---|---|
| IFC | IfcMember `RAFTER` (auch Grat-, Kehl- und Schiftsparren, Unterscheidung über ObjectType oder eigenes Pset), `PURLIN`, `COLLAR` (Kehlbalken), `POST`, `STRUT`. Latten und Konterlatten: IfcMember `USERDEFINED`/„BATTEN“ | [V, Enum-Abfrage] |
| compas_timber 2.2.0 (MIT) | BTLx-Export (Version-Attribut 2.0.0) mit den Bearbeitungen `BirdsMouth` (Kerve, inklusive RafterNailHole), `JackRafterCut`, `DoubleCut`, `FrenchRidgeLap`, `Lap`, `StepJoint`/`StepJointNotch`, `Tenon`/`Mortise`, `Dovetail`, `Slot`, `Pocket`, `FreeContour`, `Drilling`. Verbindungen `TBirdsmouthJoint`, `TStepJoint`, `XLap`, `LMiter`. **Keine Dachgenerierung** (Grat, Kehle, Schifter) | [V, Quellcode] |
| Schifterschmiegen | Backenschmiege des Schifters in der Dachebene (Grat unter 45° im Grundriss) θ = atan(cos α), z. B. 35,3° bei 45° und 38,2° bei 38° Dachneigung. Die Gratsparrenneigung folgt aus der Formel oben | [U, eigene Herleitung, gegen Zimmermannsliteratur prüfen] |
| Wechsel | Maße aus Hersteller-Tabellen (Velux-Wechselabstände; Kaminabstand zu brennbaren Bauteilen nach Feuerungsverordnung und Schornsteinzulassung) | [V Velux / U Kamin] |
| Informationsdienst Holz | Zimmerer-Fachregeln erscheinen dort. Für Dachtragwerke: Bemessung nach EC 5, Details aus Musterzeichnungen | [U] |

## 6. Photovoltaik

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Solarpflicht Bayern, Wohngebäude | **Soll**: Bauantrag ab 01.01.2025 oder vollständige Dacherneuerung ab 01.01.2025. „Angemessen“ heißt Modulfläche ≥ ⅓ der geeigneten Dachfläche, dachparallel oder integriert | BayBO Art. 44a Abs. 4 mit Abs. 1 S. 2–4 | [V] |
| Pflicht (Muss) | nur Nichtwohngebäude (ab 01.03. bzw. 01.07.2023) und staatliche Gebäude. Ausgenommen: Garagen, Carports, Dächer ≤ 50 m² | Art. 44a Abs. 2, 3 | [V] |
| Brandschutz Doppel- und Reihenhaus | Solaranlagen ≥ **0,50 m** von Brandwänden und Wänden anstelle von Brandwänden, sofern diese sie nicht gegen Brandübertragung schützen. Traufseitig aneinandergebaute Dächer feuerhemmend, Öffnungen ≥ 1,25 m | BayBO Art. 30 Abs. 5 S. 2 Nr. 2; Abs. 6 | [V] (Art. 30, nicht Art. 30 Abs. 5 allein) |
| Netzanschluss | **VDE-AR-N 4105:2026-03** (TAR EZA NS). Übergang 12 Monate für die Fassung 2018. „Fastlane“ bis 7 kVA, Q(U) als Standard, ZEREZ-ID | DKE/VDE-Verlag; Netze BW | [V] |
| Einspeisegrenze | IBN ab 25.02.2025, < 100 kW, Einspeisevergütung: **60 % Wirkleistung** bis Smart-Meter und Steuerbox getestet sind | § 9 Abs. 2 EEG 2023; Clearingstelle | [V] |
| MaStR | Registrierung **innerhalb eines Monats** nach Inbetriebnahme | § 5 Abs. 5 MaStRV | [V] |
| Errichtung | DIN VDE 0100-712 (Ausgabe 2016-10 angenommen) | – | [U] |
| Randabstände/Wind | Keine pauschale Regel: statische Auslegung des Montagesystems nach DIN EN 1991-1-4 mit Randzonen (e = min(b; 2h)) und Herstellersoftware (z. B. Würth SolarTool, K2) | Zapfe; Würth | [V Prinzip / U Zonenmaße] |
| Befestigung | Dachhaken ab RDN; Systemziegel ab 10°. Unter der RDN Dachträgerpfannen (ZVDH-Empfehlung) | FR 4.10; K2 | [V] |
| Ertrag | pvlib 0.16.1 (BSD-3), `iotools.get_pvgis_hourly/tmy`, **`read_panond`** für PAN/OND-Dateien. PVGIS 5.3 API `re.jrc.ec.europa.eu/api/v5_3/PVcalc`, 30 Aufrufe/s, Parameter `peakpower, loss, angle, aspect (0 = Süd), mountingplace=building` | PyPI, JRC | [V] |
| Literatur | Holmgren et al. 2018 (JOSS) 10.21105/joss.00884; Jensen et al. 2023 (pvlib iotools) 10.1016/j.solener.2023.112092; Huld et al. 2012 10.1016/j.solener.2012.03.006; Šúri et al. 2005 10.1080/14786450512331329556 | Crossref | [V] |
| IFC | IfcSolarDevice `SOLARPANEL` (Solarthermie: `SOLARCOLLECTOR`), Wechselrichter IfcTransformer `INVERTER`, Speicher IfcElectricFlowStorageDevice `BATTERY`. **Nicht IfcElectricGenerator** (Enum nur CHP, ENGINEGENERATOR, STANDALONE). Pset_SolarDeviceTypeCommon enthält nur Reference/Status. Leistungsdaten über Pset_ElectricalDeviceCommon (gilt für IfcDistributionElement) und eigenes Pset mit PAN-Kennwerten | IfcOpenShell-Schema | [V] |
| Indach vs. Aufdach | Indach: Module ersetzen die Deckung; IfcCovering mit Öffnung, IfcSolarDevice als Füllung, Anschlussbleche als IfcDiscreteAccessory `FLASHING`. Aufdach: Deckung durchgehend, Haken als IfcDiscreteAccessory `BRACKET` | eigene Modellierung | [U] |

## 7. Fassade

| Thema | Befund | Status |
|---|---|---|
| Fachregel 01 Zimmerer | „Außenwandbekleidungen aus Holz“, 03/2023 (3. korrigierte Auflage der Fassung 01/2020), **nur kostenpflichtig im Druck**. Geltung bis **10 m Firsthöhe**. Vollholz, Dreischichtplatten, zementgebundene Spanplatten. Regeldetailkatalog als Ergänzung | [V] |
| Schalungsarten | Stülpschalung (parallel, konisch, mit Falz, mit Nut und Feder), Boden-Deckel, Deckleisten, Leisten-Deckel, offene Bekleidung (Rhombus). Brettdicke ≥ 18 mm, Breite ≤ 11·d; Befestigung ab 120 mm Breite zweifach | Holzbau-Deutschland-Ausschreibungshilfe 2021 | [V] |
| Sockel | Abstand zum Gelände typisch 300 mm, auf Kiesstreifen 16/32 bis 150 mm | BauNetz Wissen nach FR 01 | [V] |
| Hinterlüftung, Insektenschutz | hinterlüftet, belüftet oder unbelüftet nach DIN 68800-2 und FR 01. Querschnitte und Gitterweiten aus FR 01 übernehmen | [U, Volltext nicht eingesehen] |
| Putz auf Holzfaser | WDVS auf Holzfaser-Trägerplatten mit Systemzulassung bzw. Bauartgenehmigung des DIBt je System (z. B. Gutex, Steico, Pavatex). Nummern je Regnauer-Wandtyp beschaffen | [U] |
| Farben | RAL und NCS sind lizenzierte Farbsysteme. Frei nutzbare RGB-Näherungen sind nicht normativ. Deshalb Farbcode als Property, RGB nur für die Darstellung | [U] |
| Gestaltungssatzung | Örtliche Bauvorschriften nach **BayBO Art. 81** (Dachform, Neigung, Farbe, Material) gehen der Solarpflicht vor (Art. 44a Abs. 5 Nr. 1) | [V] |
| IFC | IfcCovering `CLADDING` an IfcWall über **IfcRelCoversBldgElements**. IfcMaterialLayerSet mit **IfcMaterialLayer.IsVentilated** für die Luftschicht. Style: IfcSurfaceStyle mit IfcSurfaceStyleRendering (ReflectanceMethod `PHYSICAL`) und IfcSurfaceStyleWithTextures/**IfcImageTexture** (URLReference, RepeatS/T, Mode „DIFFUSE“). UV über IfcIndexedTriangleTextureMap | [V, Testmodell valide] |
| glTF | IfcOpenShell-`GltfSerializer` exportiert Farben (baseColorFactor aus IfcSurfaceStyleRendering), **keine Texturen oder UVs** [V, Test]. Lösung: GLB mit pygltflib (Lizenz nicht geprüft [U]) oder trimesh (MIT) nachbearbeiten, UVs planar je Dachfläche aus dem (u, v)-System der Deckung | [V/U] |

## 8. Dachentwässerung

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Norm | DIN 1986-100:2016-12 gilt; **Entwurf E DIN 1986-100:2025-06** liegt vor | DIN | [V] |
| Berechnungsregen Dach | **r(5,5)** (seit 2008; zuvor r(5,2)). Dach- und Notentwässerung zusammen ≥ r(5,100). Grundstück r(5,2) | DIN-FAQ (NAW), IZEG | [V] |
| Konflikt | Fachaufsätze (SBZ, baumetall) rechnen vorgehängte Rinnen mit r(5,2) (ZVSHK-Praxis), der Rheinzink-Rechner mit r(5,5). **Der Generator nimmt r(5,5)**, die Abweichung ist zu dokumentieren | – | [V/U] |
| Abfluss | Q = r · C · A / 10 000 [l/s], C = 1,0 für Dachflächen, A = projizierte Fläche | DIN 1986-100 Tab. 9 (zitiert) | [V] |
| Rinne und Fallrohr | DIN EN 12056-3: halbrunde Rinne Q = 0,9 · 2,78·10⁻⁵ · A_W^1,25 · F_L. Stutzen-Tabelle (halbrund): 250/280/333/400 mm ↔ 2,9/4,1/7,4/14,5 l/s; bei Winkeln Faktor 0,85; Fallrohr unter DN 75 nicht empfohlen | SBZ, Berufsschul-Tabelle | [V Formel / U Tabellenwerte] |
| KOSTRA-DWD-2020 | **Frei** (GeoNutzV, Quellenvermerk). DOI 10.5676/DWD/KOSTRA-DWD-2020. Raster 5 km (EPSG:3035), CSV/ASC/Shape, 22 Dauerstufen, T = 1–100 a, INDEX_RC = Zeile·1000 + Spalte. opendata.dwd.de/…/KOSTRA_DWD_2020 | DWD-Anwenderhilfe | [V] |
| Hersteller | Rheinzink-Rinnenrechner online (dendrit), Grömo und Rheinzink BIM über Portale | – | [V Rechner / U BIM] |
| IFC | Rinne IfcPipeSegment `GUTTER` (Pset_PipeSegmentTypeGutter: Slope, FlowRating). Fallrohr `RIGIDSEGMENT`. Rinnenkessel IfcStackTerminal `RAINWATERHOPPER`. Bögen IfcPipeFitting `BEND` | Schema | [V] |

## 9. IFC-Mapping Dach (am Testmodell IFC4X3_ADD2 geprüft: 0 Fehler, inklusive EXPRESS-Regeln [V])

| Bauteil | IFC-Klasse / PredefinedType | Beziehung |
|---|---|---|
| Dach gesamt | IfcRoof: `GABLE_ROOF`, `HIP_ROOF` (Walm), `HIPPED_GABLE_ROOF` (Krüppelwalm), `PAVILION_ROOF` (Zelt), `SHED_ROOF` (Pult), `MANSARD_ROOF` (vierseitig), `GAMBREL_ROOF` (Mansarde mit Giebel), `BUTTERFLY_ROOF`, `FLAT_ROOF` | IfcRelContainedInSpatialStructure → Geschoss |
| Dachflächen | IfcSlab `ROOF` (Pset_SlabCommon.PitchAngle) | IfcRelAggregates ← IfcRoof |
| Sparren, Pfetten, Kehlbalken | IfcMember `RAFTER`/`PURLIN`/`COLLAR`/`POST`/`STRUT` | IfcRelAggregates ← IfcRoof |
| Deckung | IfcCovering `ROOFING` + IfcMaterialLayerSet (Ziegel, Trag-/Konterlatte, UDP) | **IfcRelCoversBldgElements** ← IfcSlab |
| Unterdeckbahn | IfcCovering `MEMBRANE` (Pset_CoveringTypeMembrane) | dto. |
| First, Grat, Ortgang, Kehlblech, Eindeckrahmen | IfcDiscreteAccessory `FLASHING` bzw. `USERDEFINED` („RIDGE“, „HIP“, „VERGE“) | IfcRelAggregates oder Nesting an der Covering |
| Schneefang, Dachtritt, Sicherheitshaken | IfcDiscreteAccessory `USERDEFINED` („SNOWGUARD“, „ROOFSTEP“, „SAFETYHOOK“); alternativ IfcRailing `GUARDRAIL` | BayBO Art. 30 Abs. 8 (Vorrichtungen für Arbeiten vom Dach aus) [V] |
| Dachfenster | IfcWindow `SKYLIGHT` in IfcOpeningElement | IfcRelVoidsElement + IfcRelFillsElement |
| Sanitärlüfter DN 100 | IfcPipeSegment `RIGIDSEGMENT` + IfcStackTerminal `COWL`; Durchdringung als IfcOpeningElement | Voids in IfcSlab |
| Antennen-/Solardurchgang | IfcDiscreteAccessory; Antenne IfcCommunicationsAppliance `ANTENNA` | – |
| Kamin | IfcChimney (nur USERDEFINED/NOTDEFINED), Pset_ChimneyCommon | Voids in IfcSlab |
| PV | IfcSolarDevice `SOLARPANEL`; IfcTransformer `INVERTER` | IfcDistributionSystem (elektrisch) |
| Gaube | eigene IfcRoof + IfcWall + IfcWindow, gebündelt als IfcElementAssembly `USERDEFINED`/„DORMER“ | Öffnung im Hauptdach [U] |

**Hinweis:** Die Enums haben keinen Wert für Latte, Schneefang oder Dachtritt. Hier ist USERDEFINED mit ObjectType erlaubt und nach Recherche 06 der saubere Weg, keine IfcBuildingElementProxy.

## Bausteine mit Urteil

| Baustein | Lizenz | Urteil |
|---|---|---|
| CGAL Straight Skeleton 2 (≥ 5.6, doc 6.2) | GPL/kommerziell | **Kern für die Dachgeometrie.** Gewichte, Winkel und maximum_height vorhanden. Python-Bindings (cgal-swig-bindings) enthalten das Modul **nicht** [V]. Deshalb eigenes pybind11-Wrapping oder CLI. GPL-Frage klären |
| scikit-geometry (skgeom) | LGPL-3 | Straight Skeleton über CGAL, ungewichtet, letzter Commit 12/2023, nicht auf PyPI [V]. Nur für Prototypen |
| polyskel | LGPL-3 | Felkel-Obdržálek, 2020 inaktiv. Test mit L-Grundriss funktioniert nur im Uhrzeigersinn, entgegen dem Uhrzeigersinn leer [V]. Nicht produktiv |
| bpypolyskel | GPL-3 | Auf 320 000 OSM-Walmdächer getestet (99,99 %), benötigt `mathutils` (bei mir kein Wheel baubar) [V]. Gute Referenz |
| Shapely 2.1 | BSD-3 | Ziegel- und Lattenraster gegen Flächen schneiden |
| compas_timber 2.2 | MIT | BTLx-Bearbeitungen für Sparren (Kerve, Klaue über StepJoint/JackRafterCut). Dachlogik muss man selbst bauen |
| IfcOpenShell 0.8.5 | LGPL-3 | IFC-Erzeugung, Validierung, glTF (ohne Texturen) |
| pvlib 0.16.1 | BSD-3 | Ertrag, PVGIS-Abruf, PAN/OND lesen |
| PVGIS 5.3 API | frei (EU JRC) | Ertrag pro Dachfläche, Horizont |
| KOSTRA-DWD-2020 | Open Data | Regenspenden standortgenau |
| trimesh | MIT | GLB-Nachbearbeitung (UV, Texturen) |

## Korrekturen und Warnungen

1. **BayBO-Rettungsfenster:** 0,60 × 1,00 m lichte Größe (Art. 35 Abs. 4 BayBO, gültig ab 01.05.2026), nicht 0,90 × 1,20 m. Unverändert gelten Unterkante ≤ 1,20 m und ≤ 1 m zur Traufkante [V]. Ob die Änderung aus der Novelle 2026 stammt, habe ich nicht geprüft [U].
2. **Art. 44a BayBO:** Für Wohngebäude nur eine Soll-Pflicht. Die Muss-Pflicht betrifft Nichtwohngebäude [V].
3. **Brandschutzabstand PV:** Er steht in Art. 30 Abs. 5 **Satz 2 Nr. 2** BayBO (0,50 m); Dachfenster brauchen 1,25 m [V].
4. **ZVDH-Merkblatt:** Klassen 1–5 statt 1–6. Die alte Tabelle mit „UDB-A/USB-A“ ist veraltet [V].
5. **Hersteller-RDN ≠ ZVDH-RDN:** Hersteller-RDN nur bei vertraglicher Vereinbarung nutzen [V].
6. **Metallkehle:** Die Mindestneigung bezieht sich laut Gelbdruck auf die **Dachneigung ≥ 10°**. Die Metall-Fachregel knüpft Stoßausbildung und Überdeckung an die **Kehlneigung**, die immer kleiner ist als die Dachneigung. Der Generator muss die Kehlneigung rechnen [E/V].
7. **Dachentwässerung:** r(5,5) statt r(5,2) [V]. Mit dem Entwurf 2025 kann sich das ändern.
8. **VDE-AR-N 4105:2026-03** ersetzt die Fassung 2018-11 (Übergangsfrist) [V].
9. **Sanitärlüfter:** Laut DIN 1986-100:2016 keine Abdeckung an der Mündung. Hauben oder geschlossene Kappen nur, wo Hersteller und Norm es zulassen [V/U].
10. **Gelbdruck ≠ Endfassung:** Werte mit [E] vor der Nutzung gegen die Fachregel 04/2024 abgleichen (Lizenz beschaffen).
11. **Texturen:** Beim glTF-Export aus IfcOpenShell gehen sie verloren [V]. Hersteller-Visualisierungen sind nicht als Textur-Lizenz zu verstehen [U].

## Offene Fragen an Regnauer

1. Welche Dachformen und Neigungsbereiche bietet Regnauer standardmäßig an (Katalog), und welche Gaubentypen sind vorgefertigt?
2. Fertigt Regnauer Dachelemente (gedämmt, mit Lattung und Unterdeckung) im Werk vor? Bis zu welcher Schicht wird im Werk gedeckt?
3. Mit welchen Ziegel- und Steinlieferanten und Modellen arbeitet Regnauer (Erlus, Creaton, Braas …)? Gibt es Lieferantendaten digital (Excel, BMEcat)?
4. Gilt die ZVDH- oder die Hersteller-RDN, und welche Zusatzmaßnahme ist Standard (Klasse 3 mit Holzfaser-UDP?)?
5. Welche Kehl-, Grat- und Firstausführung ist Standard (Metallkehle, Trockenfirst mit Firstrolle)?
6. Welche Dachfenster (Velux, Roto), welche Eindeckrahmen, und legt Regnauer Rettungsfenster nach Art. 35 Abs. 4 BayBO immer fest?
7. Wo verlaufen Sanitärentlüftung und Kamin (Lage, Durchmesser, Lüfterziegel-System), und wie wird die Durchdringung im Werk vorbereitet?
8. PV: Indach oder Aufdach, Partnerfirma, Belegungsplanung inklusive Statiknachweis, Umgang mit der 0,50-m-Regel bei Doppelhäusern?
9. Welche Fassadenvarianten gibt es (Putz auf Holzfaser mit Zulassungsnummer; Holzschalungstypen; Farbkollektionen RAL/NCS)?
10. Dachentwässerung: Material, Rinnengrößen, wer rechnet (Klempner oder Planung)?
11. Welche Abbundsoftware nutzt Regnauer (cadwork, hsbcad, Dietrich’s), und akzeptiert sie BTLx aus Fremdsystemen für Sparren und Pfetten?
12. Sollen Visualisierungen fotorealistisch sein (Texturen) oder reicht eine Farbdarstellung, und für welches Ausgabemedium (Web-Viewer, Bemusterung)?

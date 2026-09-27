# Recherche 13: Innenausbau und Interior – Regeln, Varianten, Datenquellen, IFC

Stand: 27.09.2026. **[V]** = an Primärquelle, Herstellerunterlage oder maschinell am Schema IFC4X3_ADD2 geprüft (IfcOpenShell 0.8.5), **[U]** = unsicher, Sekundärquelle oder eigene Bewertung. Normtexte sind geschützt: Kennwerte stehen hier mit Normverweis, Tabellen werden nicht kopiert (vgl. Zielbild, Harte Grenze 4). Produktdatenstandards (ETIM, ECLASS, BMEcat, PDT) und die glTF/PBR-Pipeline behandelt die Parallelrecherche; hier nur, wo es die Fachlogik braucht.

## Ergebnis in 5 Punkten

1. **Mehrere Annahmen im Auftrag sind überholt.** DIN 51130 und DIN 51097 gehen in DIN EN 16165:2023 auf. DIN 18534 gilt seit 10/2025 neu. VDI 6000 Blatt 1:2008 „Wohnungen“ ist ersetzt durch VDI 6000 Blatt 1 und Blatt 2 (2024-07). DIN EN 13300 ist 2023 neu erschienen (Klassen G, R, H10). Das ZDB-Merkblatt heißt seit 02/2026 „Groß- und Megaformate“. DIN 18065 nennt Verhältnis-, Winkel- und Kreisbogenmethode, keine „Abwicklungsmethode“. BayBO Art. 36 nennt **keine Zahlen** und nimmt Wohngebäude GK 1/2 von der Kleinkinder-Regel aus [V].
2. **IFC 4.3 trägt die Auswahl, aber nicht das Verlegemuster.** Es gibt IfcCovering mit FLOORING, CLADDING, SKIRTINGBOARD, MOLDING und CEILING, 15 Treppenformen, IfcRailing, IfcDoor und Pset_DoorLining/PanelProperties, 10 Sanitärtypen und Pset_FurnitureTypeCommon. Für Verlegemuster, Fugenfarbe, Versatz, Achsbezug und Stufenverziehung gibt es **weder Attribut noch Pset**. Das braucht ein eigenes Pset (ohne Präfix `Pset_`), bei A-Reife eine Verlegeplan-Geometrie [V].
3. **Achtung Türen:** IFC `SINGLE_SWING_LEFT` entspricht **DIN-rechts**. So steht es in der Mapping-Tabelle der IfcDoor-Doku. Ein Namensabgleich ohne Übersetzung führt zu falsch bestellten Zargen und Bändern [V].
4. **Möbel- und Küchendaten sind branchenintern.** Küche und Bad nutzen IDM 3.1.0 des DCC (gültig ab 01.08.2025), Wohnen IDM Living 4.1.0, Büro OFML 2.0 (IBA, Rechte bei EasternGraphics). Die Schemata sind öffentlich, die Katalogdaten laufen über Cat@web bzw. pCon und brauchen einen Vertrag. Kein Consumer-Planer exportiert IFC. Palette CAD exportiert IFC, Winner Flex ab 12.2a6 [V].
5. **Eine Festschreibung ist mehr als eine GTIN.** GTIN plus Farbe, Oberfläche und Format identifizieren den Artikel. Muster, Versatz, Fuge (Breite, Mörtel-GTIN, Farbe), Silikon, Achsbezug, Abdichtungsklasse, Ebenheitszeile und bei A-Reife Kaliber und Charge sind **Leistungs- und Einbaudaten**. Die GTIN bildet sie nicht ab. Das Schema unten trennt Artikel, Leistung und Kontext und verweist auf STLB-Bau 2026-04 (LB 024/028/034 …) [V/U].

---

## 1. Fliesen

### Regeln und Kernwerte

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Produktnorm | DIN EN 14411:2016 (= ISO 13006). Gruppen nach Formgebung A (stranggepresst), B (trockengepresst) und Wasseraufnahme E_b: BIa ≤ 0,5 % (Feinsteinzeug) bis BIII > 10 % (Steingut, nur Wand). Abrieb glasierter Bodenfliesen im informativen Anhang N (PEI-Klassen) | din.de Inhaltsverzeichnis EN 14411 | [V] |
| Maßtoleranz | ± 0,5 %, max. ± 2,0 mm für Maß, Rechtwinkligkeit und Kantengeradheit. Bei 120 cm sind laut Fachbeitrag bis 6 mm Wölbung zulässig | euroFEN MB 7; baunetzwissen | [V]/[U] |
| Rektifizierung | Kanten nach dem Brand geschliffen, dadurch erhöhte Maßhaltigkeit. **Die Wölbung bleibt** | euroFEN MB 7 | [V] |
| Großformat | ZDB: ab > 0,25 m² Grundfläche. Merkblatt gilt für 60–120 cm Kantenlänge, bei Riegelformaten bis 150 cm; Mindestdicke 7,5 mm Boden, 3,5 mm Wand. Über 120 cm gilt die Platte als Sonderkonstruktion mit schriftlicher Vereinbarung. **Neu: Merkblatt „Groß- und Megaformate“ 2026-02** (ISBN 978-3-481-05168-6), Inhalt nicht eingesehen | euroFEN MB 7; Botament; isbn.de | [V]/[U] |
| Versatz im Verband | Hersteller empfehlen Viertelverband und **höchstens Drittelverband**. Vom Halbverband wird bei Rechteckformaten abgeraten, weil sich Hoch- und Tiefpunkte treffen (Stolperkanten, „Lächeln“ der Fugen). Einen festen Grenzwert im ZDB-Merkblatt habe ich nicht belegt | Hornbach/Hersteller-Datenblatt; Innungshinweis | [V] Hersteller / [U] ZDB |
| Überzähne | ZDB-Merkblatt „Höhendifferenzen“ mit Formel. Beispiel laut Sekundärquelle: 30×60 mit Presskante 1,9 mm, rektifiziert 1,45 mm; Obergrenze ca. 2,0 bzw. 1,5 mm | baumigo.de | [U] |
| Rutschhemmung (Schuh) | R9 6–10°, R10 > 10–19°, R11 > 19–27°, R12 > 27–35°, R13 > 35°. **Prüfung heute nach DIN EN 16165:2023 Anhang B**; DIN 51130:2014 ist ersetzt. Gilt für Arbeitsstätten (ASR A1.5); im EFH nur eine Empfehlung | dinmedia; V&B TI 01/2025 | [V] |
| Rutschhemmung (barfuß) | A ≥ 12°, B ≥ 18°, C ≥ 24° (DGUV I 207-006; Prüfung nach DIN EN 16165) | V&B TI 01/2025 | [V] |
| Frost | nur außen relevant, EN ISO 10545-12 | EN 14411 | [U] |
| Fugenbreite | ATV DIN 18352:2019-09, 3.4.2: technisch notwendig **2–8 mm**, je nach Format und Toleranz mehr. Die Fassung vor 2019 staffelte nach Format (z. B. trockengepresst > 10 cm: 2–8 mm). **ZDB-Mindestfuge bei Großformat 3 mm**. Breite in mm-Schritten vereinbaren | baunormenlexikon; ZDB FI Zementäre Fugen 06/2015 | [V] |
| Verfugung | Regelfall: graue, hydraulisch abbindende Fugenmasse. Andere Farbe oder Reaktionsharz nur, wenn im LV beschrieben | ATV DIN 18352 3.4.3 | [V] |
| Abdichtung | DIN 18534-1 bis -6, **Ausgabe 2025-10**. W0-I gering (Wand außerhalb Dusche, Boden ohne Ablauf), W1-I mäßig (Wand an Wanne/Dusche, Boden mit Ablauf, Bad mit Duschabtrennung), W2-I hoch (Boden bodengleiche Dusche; ohne Abtrennung **ganzer Badboden**), W3-I sehr hoch (gewerblich). Ab W2-I nur feuchteunempfindliche Untergründe. **Neu:** In W2-I sind Spezialgipsplatten mit Herstellernachweis zulässig, in W3-I nur zementäre. AIV-B auch an W3-I-Wänden. Neu sind außerdem Schnittschutz unter Silikonfugen und Kapillarsperren an Türen | Schlüter; Knauf; Sopro 4x4 04/2025; dinmedia | [V] |
| Flansch Ablauf/Rinne | Klebeflansch ≥ 30 mm bis W2-I, ≥ 50 mm bei W3-I (bzw. werkseitige Manschette) | TECE; Dallmer | [V] |
| Ebenheit | DIN 18202:2019-07 Tab. 3 (Stichmaß in mm bei 0,1/1/4/10/15 m). Zeile 3 (flächenfertige Böden, Fliesenbeläge): 2/4/10/12/15. Zeile 4 (erhöht): 1/3/9/12/15. Zeile 6 (Wände): 3/5/10/20/25. Zeile 7 (erhöht): 2/3/8/15/20. Erhöhte Anforderungen sind gesondert zu vereinbaren | Haas-Fertigbau-Auszug; Fichtner | [V] |
| Bewegungsfugen | Estrichfugen in den Belag übernehmen, Randfugen, Feldbegrenzung im Heizestrich nach Fugenplan des Planers. Übliche Feldgrößen ≤ 40 m², Seite ≤ 8 m, Seitenverhältnis ≤ 1:2 | ZDB-MB „Bewegungsfugen“ (nicht eingesehen) | [U] |
| Belegreife | Zement unbeheizt ≤ 2,0 CM-%, beheizt ≤ 1,8 CM-%. Calciumsulfat ≤ 0,5 CM-%, beheizt ≤ 0,3 CM-%. DIN 18560-1:2021 lässt für beheiztes CA 0,5 zu, das Handwerk fordert 0,3. Für Schnellestriche gelten Herstellerwerte | TKB-MB 16 (12/2024); IBF 1/2021; BG Bau | [V] |

### Varianten-Taxonomie Fliese

`Material` (Feinsteinzeug BIa · Steinzeug · Steingut BIII · Naturstein EN 12058 · Glas-/Zementfliese) → `Format` (Nennmaß/Werkmaß, Dicke, Mosaik < 7 cm, Riegel, Groß-/Megaformat) → `Kante` (Presskante · rektifiziert · Fase) → `Oberfläche` (matt · poliert · lappato · strukturiert; R-Klasse; A/B/C) → `Dekor/Farbe` (Hersteller-Farbname, Farbvariation V1–V4 [U]) → `Verlegung` (Muster · Versatz · Richtung · Achsbezug · Fugenbreite · Fugenfarbe/-mörtel · Silikonfarbe) → `Formteile` (Sockel, Stufe, Kehle, Profil/Schiene) → `Aufbau` (Kleber C2/S1 [U], Entkopplung, AIV-Art, W-Klasse).

**Muster (Enum-Vorschlag):** Kreuzfuge · Halbverband · Drittelverband · Viertelverband · Wilder Verband · Diagonal 45° · Fischgrät · Chevron · Römischer Verband (Formatpaket) · Fliesenteppich/Bordüre. Verschnitt laut Ratgeber: gerade Muster 5–10 %, diagonal und Fischgrät 10–15 % [U].

**Fliesenspiegel und Schnitt [U, Handwerksregeln]:** Achse auf Sichtachse, Tür, Fenster oder Waschtischmitte legen. Symmetrische Randstücke, keine Randstreifen unter etwa ⅓ Fliese. Wand- und Bodenfuge durchlaufend führen. Höhen auf Objektkanten abstimmen (Waschtisch, Spiegel, Armatur). Wand- und Bodenraster verzahnen. Das ist ein 2D-Packungsproblem mit Zielfunktion, kein Regelwerk. Palette CAD bietet laut Hersteller Fliesentechnik und Schnittoptimierung als Referenz [V].

### Datenquellen und Lizenz

- **Hersteller-Stammdaten:** Villeroy & Boch (Technische Infos, frei) [V]. Palette-CAD-Katalog „Fliesen + Platten“ mit über 230.000 Oberflächen, lizenzpflichtig [V].
- **ZVSHK Open Data Pool** für Sanitär, nicht für Fliesen [V].
- **EPD:** EN 17160:2026 als PCR für keramische Fliesen; frei nutzbare EPDs z. B. von Confindustria Ceramica [V].
- **ZDB-Merkblätter:** kostenpflichtig (Rudolf Müller, ca. 16 € je Merkblatt), Sammlung Stand 04/2026 [V].

### IFC-Mapping [V Schema, U Konvention]

| Inhalt | IFC 4.3 |
|---|---|
| Fliesenbelag Boden/Wand | `IfcCoveringType` FLOORING/CLADDING → `IfcCovering`. Zuordnung per `IfcRelCoversSpaces` (Raum) oder `IfcRelCoversBldgElements` (Wandelement). Laut Doku: mit eigener Geometrie und Raumbegrenzung in den Raum enthalten |
| Schichten | `IfcMaterialLayerSetUsage` (Kleber, AIV, Fliese als Schichten). Kategorien laut Doku: Front, Fill, Back |
| Sockelfliese, Profil | `IfcCovering` SKIRTINGBOARD bzw. MOLDING mit `IfcMaterialProfileSet` (Kategorie „Trim“) |
| Artikel | `Pset_ManufacturerTypeInformation` (GlobalTradeItemNumber, ArticleNumber, ModelReference, Manufacturer) am Typ |
| Rutschhemmung | `Pset_CoveringFlooring.HasNonSkidSurface` ist **nur boolesch**. R-Klasse und A/B/C gehören in ein eigenes Pset |
| Oberfläche | `Pset_CoveringCommon.Finish` (Text). 3D-Stil über `IfcSurfaceStyle` + `IfcSurfaceStyleRendering` (ReflectanceMethod **PHYSICAL** existiert) + `IfcImageTexture`/`IfcIndexedPolygonalTextureMap` |
| Mengen | `Qto_CoveringBaseQuantities` (Width, GrossArea, NetArea) |
| Toleranz | `Pset_Tolerance` (PlanarFlatness …) für die DIN-18202-Zeile |
| Muster, Fuge, Achse | **fehlt.** Vorschlag: eigenes Pset `HP_Verlegung` (Muster-Enum, Versatzanteil, Winkel, Ursprung, Richtung, Fugenbreite, Fugenmörtel-GTIN, Fugenfarbe, Silikon-GTIN) am Occurrence. Bei A-Reife den Verlegeplan als Geometrie: `IfcCoveringType.RepresentationMaps` für die Einzelfliese, `IfcMappedItem`-Instanzen oder Kind-Coverings per `IfcRelAggregates`. Letzteres ist in der Doku **kein** dokumentiertes Konzept, deshalb mit dem Validation Service testen [U]. `IfcFillAreaStyleTiles` taugt nur für 2D-Schraffur |

Test: Ein `IfcCoveringType` FLOORING mit Hersteller-Pset, eigenem Pset `HP_Verlegung`, Schichtmaterial, STLB-Klassifikation und PHYSICAL-Stil bestand `ifcopenshell.validate` mit Express-Regeln ohne Befund [V].

### Abhängigkeiten
- Fliese → W-Klasse → Untergrund. Im Holzrahmenbau ist das die **Beplankung**: Gipsfaser/Gipskarton nur bis W1-I, W2-I nur mit Herstellernachweis, sonst zementgebundene Platte.
- Fliese → Estrichart und FBH → Belegreife und Entkopplung.
- Format → Ebenheit (Zeile 3 oder 4) → Aufpreis „erhöhte Anforderung“.
- Großformat → Mindestfuge 3 mm → Versatz ≤ ⅓.
- Achsbezug → Sanitärobjekte und Vorwand.

---

## 2. Böden

### Regeln und Kernwerte

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Massivparkett | DIN EN 13226:**2025-02** (Massivholz-Parkettelemente mit Nut/Feder), Sortierregeln je Holzart in Tabellen | din.de | [V] |
| Mehrschichtparkett | DIN EN 13489:**2023-09**. Nutzschicht ≥ 2,5 mm. Erscheinungsklassen ○ / △ / □; freie Herstellersortierung nach Anhang B (mittlere Brinellhärte ≥ 10 N/mm²). 3 % der Stäbe dürfen aus anderen Klassen stammen | dinmedia; dataholz | [V] |
| CE/Leistung | DIN EN 14342 (Holzfußböden; CE seit 2010). Brandverhalten Cfl-s1/Dfl-s1/Efl | dataholz | [V] |
| Laminat | DIN EN 13329 (aktuell 2023 [U]), Nutzungsklassen nach EN ISO 10874: 21/22/23 Wohnen, 31/32/33/34 gewerblich, Klasse 22+ abgeschafft (Amd 1:2020). Abrieb AC1–AC6. Nicht für Nassräume | dinmedia; normenportal; reschfloor | [V]/[U] |
| FBH-Eignung | Wärmedurchlasswiderstand des Belags inkl. Unterlage **R_λ,B ≤ 0,15 m²K/W**; Auslegung der FBH mit 0,10 (DIN EN 1264). Parkett verklebt, Richtwerte: Eiche 16 mm ≈ 0,085, 22 mm ≈ 0,105, Fertigparkett 10–15 mm 0,07–0,11 | BVF-Richtlinie 9; BVPF-MB 001; Reinlein | [V] |
| Oberflächentemperatur | FBH max. 29 °C (Randzone 35); für Parkett empfohlen 26 °C | BVPF/VdP MB 001 | [V] |
| Belegreife | siehe Fliesen. Parkett: Probe aus der unteren Estrichhälfte; Zement 2,0/1,8, CA 0,5/0,3 CM-%. Textil, elastisch und Laminat: Querschnitt 1,8/1,6 | TKB-MB 16 | [V] |
| Trittschall | DIN 4109 stellt innerhalb des eigenen EFH **keine** Anforderung [U]. Unterlagen mit ΔL_w nach Herstellerangabe; das ist Komfort, kein Nachweis | – | [U] |
| Schwelle | DIN 18040-2: untere Türanschläge/Schwellen vermeiden, technisch unabdingbar max. 2 cm. Im EFH nur verbindlich, wenn vereinbart | DIN 18040-2 (lizenzpflichtig) | [U] |
| Kapillarsperre Tür Bad | DIN 18534-1:2025-10, 8.5.5: kapillaren Feuchtetransport im Belagaufbau an Türen berücksichtigen (Parkett neben Bad) | dinmedia-Änderungsvermerk | [V] |

### Varianten-Taxonomie Boden

- **Parkett:** Konstruktion (Massiv-Stab, -Diele, Mosaik, Lamparkett, 2-/3-Schicht) · Holzart (Eiche, Esche, Buche, Ahorn, Nuss …) · Sortierung (○/△/□ oder Hersteller: „Natur“, „Rustikal“ …) · Oberfläche (geölt, hartwachsgeölt, lackiert matt/seidenmatt, gebürstet, geräuchert, weiß pigmentiert) · Kante (Fase 2-/4-seitig) · Verlegemuster (Schiffsboden/wilder Verband, Englischer Verband mit festem Versatz, Fischgrät, Chevron/Französisches Fischgrät, Würfel, Tafel) · Verlegeart (vollflächig verklebt, schwimmend, genagelt).
- **Fischgrät/Chevron** brauchen Links- und Rechtsstäbe, also zwei Artikel; Chevron dazu einen Gehrungswinkel (45°/60°) [U].
- **Designboden:** Rigid/SPC, Klebe-Vinyl, Klick-Vinyl; Nutzschicht mm; Klasse 23/33 [U].
- **Teppich:** Klassifikation EN 1307 [U].
- **Naturstein:** EN 12058 [V].
- **Sockelleisten:** keine Norm. Höhen typ. 40/60/80/100 mm; Material Echtholz, MDF foliert/lackiert, Alu, Fliesensockel; Profil (eckig, Viertelstab, Hamburger/Berliner Profil) [U]. **Übergangsprofile:** Anpassungs-, Übergangs-, Abschlussprofil, Dehnfugenprofil [U].

### Datenquellen
- Hersteller-Datenblätter mit R-Werten sind frei (Weitzer MB 021, Steigerwald/Reinlein) [V].
- dataholz.eu (Datenblätter frei) [V].
- EPDs über IBU oder Environdec.
- Muster und Holzbilder für PBR liefert der Hersteller; die Lizenz ist einzeln zu klären [U].

### IFC-Mapping
- `IfcCovering` FLOORING mit `IfcMaterialLayerSet`: Unterlage, Nutzschicht; `Pset_MaterialWood` (Species, AppearanceGrade = Sortierung, MoistureContent).
- Sockelleiste: `IfcCovering` SKIRTINGBOARD mit `IfcMaterialProfileSet`; die Raumsicht steht in `Pset_SpaceCoveringRequirements.SkirtingBoard/-Height`.
- Übergangsprofil: kein PredefinedType, also `USERDEFINED` + ObjectType „Übergangsprofil“ [U].
- R_λ,B ist kein Standard-Property (`ThermalTransmittance` in Pset_CoveringCommon ist ein U-Wert), deshalb ein eigenes Property [U].

### Abhängigkeiten
- Zielbild „gleiche Fertigfußbodenhöhe“: Belagdicke → Estrichhöhe je Raum → Türzarge (Bodenluft), Treppen-Antrittsstufe und Schwelle.
- Belag → R_λ,B → FBH-Vorlauftemperatur und Wärmepumpen-JAZ (Recherche 05).
- Fischgrät → Raumgeometrie und Fries.

---

## 3. Wände und Decken

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Gipsplatten Q1–Q4 | Merkblatt 2 (Stand 11/2017) der Industriegruppe Gipsplatten im Bundesverband der Gipsindustrie („Industrieverband Gips“ ist der alte Name). Q1 Grundverspachtelung (unter Fliesen: nur Fugen füllen). **Q2 Standard** (Raufaser mittel/grob, matte Anstriche). Q3 (matt, fein strukturiert; Oberputz ≤ 1 mm). Q4 (Vollflächenspachtelung > 1 mm; Glanz, Lack, Stuccolustro; Lichtverhältnisse ins LV). Ohne LV-Angabe gilt Q2. Q3/Q4 mit erhöhter Ebenheit nach DIN 18202 Zeile 7. Q3/Q4 sind Besondere Leistungen nach DIN 18340 | gips.de MB 2 | [V] |
| Innenputz | DIN EN 13914-2 (Planung Innenputz); Putzarten Gips, Kalk, Kalkzement, Lehm; Körnung und Struktur nach Hersteller | – | [U] |
| Keller feucht | massiver Keller: mineralisch, diffusionsoffen (Kalk/Silikat, ggf. WTA-Sanierputz). Keine dichten Dispersionen auf feuchtem Grund | – | [U] |
| Wandfarbe | DIN EN 13300, **Neuausgabe 2023**. Glanz G1 glänzend (≥ 60 bei 60°) … G4 stumpfmatt (< 5 bei 85°). Nassabrieb heute in **R-Klassen** mit neu geordneten Grenzwerten; klassisch Kl. 1 ≤ 5 µm/200 Zyklen, Kl. 2 ≤ 20, Kl. 3 ≤ 70, Kl. 4/5 bei 40 Zyklen. Deckvermögen heute **H10-Klassen**, klassisch Kl. 1 ≥ 99,5 %, Kl. 2 ≥ 98 %, Kl. 3 ≥ 95 % bei angegebener Ergiebigkeit (m²/l). Neu: Unsicherheitsprinzip | farbe.de 01/2023; Wikipedia; Baumit | [V] Struktur / [U] neue Grenzwerte |
| RAL | RAL CLASSIC, DESIGN SYSTEM plus, EFFECT: über 2.500 Töne; digital in RGB und **Lab**. Die Download-Bibliotheken sind laut RAL „nicht für farbmetrische Zwecke“ und je Nutzer lizenziert. **RAL-Codes in Online-Konfiguratoren sind lizenzpflichtig** | ral-farben.de | [V] |
| NCS | Lizenz bei NCS Colour AB; Hersteller-Farbfächer (Caparol, Brillux …) mit eigenen Lizenzen | – | [U] |
| Akustikdecke | Schallabsorberklasse A–E nach EN ISO 11654 | – | [U] |
| Einbauleuchten Holzbau | nur in Installationsebene bzw. abgehängter Decke, luftdichte Ebene und Brandschutzbekleidung nicht durchdringen | Praxis | [U] |

**Farbmetrik fürs Rendering [U]:** Die Farbe als CIELAB mit Lichtart und Beobachter speichern (D65/10° oder D50/2°). Für PBR daraus linear-sRGB `baseColor` ableiten. RAL-Lab aus der Digitalbibliothek reicht für P-Reife. Für eine farbverbindliche Bemusterung zählt immer das physische Muster. Das gehört als Hinweis in den Vertrag.

**Taxonomie Wand:**
- `Untergrund`: GK, GF, Putz, Beton
- `Spachtelqualität`: Q1–Q4
- `Beschichtung`: Produkt, Glanz, Nassabrieb, Deckvermögen, Farbsystem und Farbcode
- `Tapete`: Vlies, Raufaser, Glasgewebe; Musteransatz, Rapport
- `Wandfliese`: siehe Kapitel 1
- `Decke`: gespachtelt, Akustik, Holz; Leuchtenraster

**IFC:**
- Anstrich als `IfcCovering` CLADDING (Wand) bzw. CEILING (Decke) mit dünner Schicht, oder als Schicht „Front“ im Wand-`IfcMaterialLayerSet` [U, Konvention wählen].
- Q-Stufe, Farbcode und Farbsystem in ein eigenes Pset.
- Einbauleuchte: `IfcLightFixture` + `Pset_LightFixtureTypeCommon.LightFixtureMountingType = RECESSED` [V].

**Abhängigkeiten:**
- Glanzgrad → Q-Stufe → Ebenheit Zeile 7 → Preis.
- Streiflicht (Fenster, Leuchten) → Q4-Empfehlung.
- W-Klasse → Wandplatte.

---

## 4. Treppen

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Hauptmaße (≤ 2 WE) | Laufbreite ≥ 80 cm, Steigung 14–20 cm, Auftritt 23–37 cm, 2s + a = 59–65 cm. Für GK 1/2 bzw. innerhalb von Wohnungen **nicht bauaufsichtlich eingeführt** | Recherche 02 | [V] |
| Kopfhöhe | lichte Treppendurchgangshöhe ≥ 200 cm; bei ≤ 2 WE am Randstreifen einschränkbar | DIN 18065:2020 6.5 | [V] |
| Verziehung | Mindestauftritt Wendelstufe an der inneren Begrenzung: allgemein 100 mm, **≤ 2 WE: 50 mm**, Spindel ≤ 2 WE: 0 mm. Aus einer Wendelung heraus max. 3,5·a gewendelte Stufen im geraden Laufteil. Das gilt nicht bei „allgemein anerkannter handwerklicher Verziehungsregel, insbesondere **Verhältnis-, Winkel- oder Kreisbogenmethode**“. **Keine Mischung** der Methoden in einem Lauf. Auftritt in der Lauflinie als Sehne gemessen | DIN 18065 6.2 (2011/2020); trepedia | [V] |
| Gehbereich | Breite 2/10 der nutzbaren Laufbreite (bis 100 cm), sonst 20 cm; Lauflinie frei im Gehbereich, stetig, ohne Knick | DIN 18065 8 | [V] |
| Handlauf | BayBO Art. 32 Abs. 6: „fester und griffsicherer Handlauf“; beidseitig erst bei > 2 nicht stufenlos erreichbaren Wohnungen oder wenn es die Verkehrssicherheit erfordert. DIN 18065: Oberkante 80–115 cm, Ø 25–60 mm, ≥ 50 mm Wandabstand | gesetze-bayern (via Exa); trepedia | [V]/[U] |
| Umwehrung | BayBO Art. 36: umwehren bei > 0,50 m Absturzhöhe sowie an freien Seiten von Treppenläufen und Treppenaugen. „Ausreichend hoch und fest“, **ohne Zahl**. Die Kleinkinder-Regel (Über- und Durchklettern) gilt **nicht innerhalb von Wohngebäuden GK 1/2 und innerhalb von Wohnungen**. Der Kommentar hält die alten DVBayBO-Werte (0,90 m bis 12 m, 1,10 m darüber) für ausreichend | gesetze-bayern (via Exa); Rehm-Kommentar | [V] |
| Geländer DIN 18065 | Geländer ab > 100 cm Absturzhöhe; Mindesthöhen nach LBO/Arbeitsschutz (90 cm bis 12 m, 110 cm darüber). **12 cm** lichte Öffnung, Erschweren des Überkletterns und 12 cm lichter Stufenabstand nur für „Gebäude im Allgemeinen“. **Für ≤ 2 WE: keine Anforderung nach dieser Norm**. Waagerechter Abstand Geländer–Stufe ≤ 6 cm | DIN 18065:2020 6.8/6.9 | [V] |
| Bolzentreppe | DIN 18069 (Tragbolzentreppen), Mindestauftritt in der Bolzenkonstruktionslinie gemessen | DIN 18065 6.2.2 | [V] |

**Taxonomie:**
- `Form`: gerade · viertel-/halbgewendelt · zweimal viertelgewendelt · mit Podest (viertel/halb) · Wendel · Spindel
- `Bauart`: eingestemmte oder aufgesattelte Wange · Holm (Mittel-/Doppelholm) · Faltwerk · Bolzen · Kragstufen
- `Holzart/Sortierung`: Buche, Eiche, Esche, Ahorn; keilgezinkt oder durchgehende Lamelle [U]
- `Oberfläche`: Lack, Öl; R-Klasse bzw. Antirutsch-Einleger
- `Setzstufe`: offen oder geschlossen, Unterschneidung
- `Geländer`: senkrechte oder waagerechte Stäbe, Glas, Lochblech, Stababstand
- `Handlauf`: Holz oder Edelstahl, rund oder eckig, Höhe
- `Verziehungsmethode`: Verhältnis, Winkel, Kreisbogen
- `Drehrichtung` links/rechts nach DIN 107 bzw. DIN 18065 Abschnitt 5

**IFC [V]:**
- `IfcStairTypeEnum` hat 15 Formen (u. a. QUARTER_WINDING_STAIR, TWO_QUARTER_WINDING_STAIR, HALF_TURN_STAIR, SPIRAL_STAIR).
- `IfcStair` aggregiert per `IfcRelAggregates` `IfcStairFlight` (STRAIGHT, WINDER, SPIRAL, CURVED, FREEFORM), Podeste als `IfcSlab` LANDING und `IfcRailing` (HANDRAIL, GUARDRAIL, BALUSTRADE).
- `IfcStairFlight.NumberOfRisers/RiserHeight/TreadLength` sind seit IFC4 **deprecated**; die Werte gehören in `Pset_StairFlightCommon` (NumberOfRiser, RiserHeight, TreadLength, WalkingLineOffset, TreadLengthAtInnerSide, Headroom …).
- Die **Lauflinie** ist die „Axis“-Repräsentation, bei gewendelten Läufen als `IfcCompositeCurve`.
- `Pset_RailingCommon.Height`.
- Wange und Holm als `IfcMember` STRINGER.
- Für Trittstufen gibt es keine eigene Klasse, daher `IfcBuildingElementPart` bzw. `IfcPlate` USERDEFINED „Trittstufe“ [U].
- Die Verziehung (Auftritt je Stufe innen, Lauflinie, außen; Methode) braucht ein eigenes Pset.

**Abhängigkeiten:**
- Geschosshöhe und Fertigfußboden oben/unten → Steigungszahl.
- Deckenöffnung (Wechsel im Holzbalken = BTLx-Teil) → Kopfhöhe.
- Treppenauge → Umwehrung.
- Belag der Stufen → Nutzbarkeit, Übergang zum Parkett.

---

## 5. Innentüren, Fenster innen, Sonnenschutz

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Türmaße | DIN 18101:**2014-08** (ersetzt 1985). Baurichtmaß 625/750/875/1000/1125 (/1250) × 2000/2125/2250. Beispiel 875 × 2000: Zargenfalz 841 × 1983, lichter Durchgang 811 × 1968, Türblatt gefälzt 860 × 1985, stumpf 834 × 1972. Differenzregel Baunennmaß −44 (Falz), −25 (Blatt gefälzt), −51 (stumpf). Gilt nicht für Außen-, Brand-, Rauchschutz- und einbruchhemmende Türen | dinmedia; Westag-Handbuch | [V] |
| Zargen | Stahlzargen DIN 18111-1/-2/-3, Holzzargen DIN 68706-2 | DIN 18101 Anwendungsbereich | [V] |
| Drittes Band | Bandbezugslinie 350 mm unter dem oberen Band (DIN 18268) | normenportal (Entwurf) | [U] |
| Anschlag | DIN 107:1974: Blick auf die **Öffnungsfläche**; Drehachse links = DIN-links (L). Gilt auch für Zargen, Schlösser, Treppen, Wannen | din.de Inhaltsverz.; Wikipedia | [V] |
| **IFC-Mapping Anschlag** | IfcDoor-Doku, Tabelle 228: `SINGLE_SWING_LEFT` = **DIN-R**, `SINGLE_SWING_RIGHT` = **DIN-L**. Das Türblatt öffnet immer in +y der ObjectPlacement; eine Umkehr geht nur über die Placement | IFC4.3.x-development (GitHub) | [V] |
| Barrierefreiheit | DIN 18040-2:2011 gilt, Entwurf 2023-02. R-Standard 150×150 cm, sonst 120×120 cm Bewegungsfläche | din.de; ByAK | [V] |

**Taxonomie Tür:** Türblatt (Röhrenspan, Vollspan, Wabe; Oberfläche CPL, Lack, Furnier) · Kante (gefälzt, stumpf) · Höhe (2000/2125/raumhoch) · Glasausschnitt (LA, LA-Mitte, Ganzglas; Sicherheitsglas ESG/VSG) · Zarge (Umfassungs-, Block-, Stahl- oder verdeckte Zarge) · Bänder (2/3, verdeckt) · Schloss (BB, PZ, WC) · Drücker (Rosette oder Langschild; Form; Oberfläche) · Anschlag DIN L/R · Öffnung (Dreh, Schiebe vor der Wand, Schiebe in der Wand) · Bodenluft [U].

**Fenster innen und Sonnenschutz [U]:**
- Die Fensterbank innen hat keine eigene Klasse: `Pset_WindowCommon.HasSillInternal` plus `IfcCovering` USERDEFINED „Fensterbank innen“.
- Rollladen → `IfcShadingDevice` SHUTTER, Raffstore → JALOUSIE, Markise → AWNING [V Enum]. Insektenschutz → USERDEFINED.
- `Pset_ShadingDeviceCommon` (MechanicalOperated, SurfaceColour, SolarTransmittance) [V].

**IFC Tür [V]:**
- `IfcDoorType` mit OperationType (25 Werte).
- `Pset_DoorLiningProperties` und `Pset_DoorPanelProperties`: in 4.3 als Psets vorhanden, zusätzlich die Entitäten `IfcDoorLiningProperties`/`IfcDoorPanelProperties`.
- Materialkategorien „Lining“, „Framing“, „Glazing“.
- `Pset_DoorCommon` (AcousticRating, HandicapAccessible, SelfClosing).
- `Pset_DoorWindowGlazingType` (IsTempered, IsLaminated).
- Bodenluft in `ThresholdOffset` bzw. einem eigenen Property.

**Abhängigkeiten:**
- Fertigfußboden → Türhöhe und Bodenluft.
- Wanddicke im Holzrahmenbau → Zargenspiegel.
- Tür-Schwenkbereich → Möblierung und Bewegungsfläche.
- DIN-Anschlag → Lichtschalter-Position (TGA).

---

## 6. Sanitär

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Richtlinie | **VDI 6000 Blatt 1:2024-07 (Grundlagen)** + **Blatt 2:2024-07 (Wohnungen und Hotelzimmer)**; ersetzt VDI 6000 Bl. 1:2008 und Bl. 4:2006. Maße als Fertigmaße, Objekte als Außenmaße | vdi.de; baunormenlexikon | [V] |
| Bewegungsfläche | VDI-FAQ: vor dem WC 80 × 75 cm, vor der Dusche 90 × 75 cm. Bei Einzelnutzung dürfen sich Bewegungs- und Verkehrsflächen **überlagern**, aber nicht verkleinern | vdi.de FAQ | [V] |
| Barrierefrei | DIN 18040-2: vor WC, Waschtisch und in der Dusche 120 × 120 (R: 150 × 150). WT unterfahrbar ≥ 55 cm, Beinfreiraum 90 cm breit. Dusche niveaugleich, Absenkung ≤ 2 cm, Belag ≥ B. Duschsitz 46–48 cm | Heinze-Planungshilfe | [V] Sekundär |
| Abdichtung | siehe Kapitel 1 (W1-I/W2-I; Flansch) | – | [V] |
| Montagehöhen | WC-Sitz ca. 40–46 cm, WT-Oberkante 85–90 cm, Armatur/Brause nach Hersteller | – | [U] |
| Duschgefälle | planmäßig zum Ablauf, üblich 1–2 %; Rinne an der Wand oder im Feld | – | [U] |

**Taxonomie:** Objekt (WC wandhängend/spülrandlos, Waschtisch Einzel/Doppel/Aufsatz, Wanne Körperform/freistehend, Duschfläche gefliest/Duschwanne superflach, Rinne/Punktablauf) · Vorwand (Element, raumhoch/halbhoch, Ablage) · Armatur (Aufputz/Unterputz, Thermostat, Oberfläche) · Accessoires · Abtrennung (Glas ESG, Walk-in) · Farbe/Glasur.

**Datenquellen [V]:**
- ZVSHK Open Data Pool: Stammdaten, Zugang über Registrierung; angebunden an Palette CAD.
- Palette-CAD-Katalog: über 200.000 Sanitärobjekte inkl. ARGE-Daten.
- Villeroy & Boch BIM-Bibliothek; Duravit nur .rfa; Geberit als Revit-Plug-in (Recherche 04).
- Ausschreibung: LB 045 „Gas-, Wasser- und Entwässerungsanlagen – Ausstattung, Elemente, Fertigbäder“.

**IFC [V]:**
- `IfcSanitaryTerminalTypeEnum` (BATH, BIDET, CISTERN, SHOWER, SINK, TOILETPAN, WASHHANDBASIN, WCSEAT …) mit typspezifischen Psets, z. B. `…ToiletPan` (PanMounting WALLHUNG), `…WashHandBasin` (MountingOffset), `…Shower` (HasTray).
- `IfcWasteTerminal` FLOORTRAP mit `Pset_WasteTerminalTypeFloorTrap` (Rinne/Ablauf).
- Vorwand: `IfcWall`/`IfcElementAssembly` [U].
- Bewegungsflächen als `IfcSpatialZone` oder als eigene „Clearance“-Repräsentation [U].

**Abhängigkeiten:**
- Bodengleiche Dusche in der Holzbalkendecke: Aufbauhöhe für Rinne und Gefälle, Abdichtung W2-I am Holz (Recherche 01/05).
- Vorwand → Fliesenachse.
- WC-Position → Fallleitung (TGA-Recherche 08).

---

## 7. Küche

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Koordinationsmaße | DIN EN 1116:**2018-03**: Höhen (Arbeitsplatte, Unterbaugeräte, Sockel), Tiefen, Breiten, Einbaumaße der Geräte. Mit Kochfeld oder Spüle Plattentiefe **≥ 600 mm** | din.de Inhaltsverz.; AMK-MB 007 | [V] |
| Breitenraster | 10er- oder 15er-Teilung (20–120 cm bzw. 15–120 cm); Korpushöhen herstellerabhängig (68/72/80/86 cm), Sockel ab 10 cm | HEA | [V] |
| Bewegungsfläche | ≥ 120 cm vor der Zeile; Raumtiefe einzeilig ≥ 180 cm, zweizeilig ≥ 240 cm | HEA | [V] |
| AMK-Abstände | Kochfeld–seitlicher Hochschrank ≥ 300 mm; Spüle–Kochfeld ≥ 300 mm (Empfehlung), ergonomisch ≥ 900 mm (AMK-Ergonomiestudie 2011); Stege ≥ 50 mm; Einbauteil ≥ 300 mm von der Plattenverbindung | AMK-MB 007 | [V] |
| Induktion | AMK-MB 015 (2025-03): Korpustiefe 560 mm, Kochfeld max. 510 × 1180 mm, Ausschnitt max. 490 × 1160 mm, vertikaler Freiraum max. 64 mm, Wandabstand Ausschnitt ≥ 50 mm, Lüftung 100 cm² | AMK-MB 015 | [V] |
| Arbeitsdreieck | klassische Heuristik Kühlen–Spülen–Kochen; kein Normwert belegt | – | [U] |

**IDM (DCC) [V]:**
- Das Daten Competence Center e. V. (Herford, seit 1998) betreut das IDM seit 2002, entwickelt mit Softwarehäusern. Es vereint kaufmännische, funktionale und grafische Informationen.
- Versionen: **IDM Küche/Bad 3.1.0** (veröffentlicht 01.05.2025, gültig ab 01.08.2025, XSD + HTML-Doku frei downloadbar; Variante „Block“), IDM Living 4.1.0, IDM Polster.
- Dazu Bestellformate (ORDERS/ORDRSP, EUDR-Anpassung) und Web-Services für die Planungsprüfung.
- Datenverteilung über **Cat@web**; Katalogdaten nur mit Vertrag [U: Konditionen nicht eingesehen].
- Roomle importiert IDM Polster und IDM Wohnen.

**Datenquellen und IFC:**
- Planer CARAT, KPS und Winner nutzen IDM.
- Küchenmöbel als `IfcFurniture` (kein Küchen-Enum) mit USERDEFINED und `Pset_FurnitureTypeCommon.IsBuiltIn = TRUE`; Arbeitsplatte als `IfcSystemFurnitureElement` WORKSURFACE [U].
- Geräte als `IfcElectricAppliance` (DISHWASHER, ELECTRICCOOKER, FRIDGE_FREEZER, MICROWAVE …), Spüle als `IfcSanitaryTerminal` SINK [V].
- Anschlusspunkte (Wasser, Abwasser, E-Herd, Abluft/Umluft) als `IfcDistributionPort` [U].

**Abhängigkeiten:**
- Fensterbrüstung → Arbeitshöhe.
- Dunstabzug → Lüftungskonzept (Recherche 08).
- Insel → Bodenanschlüsse → Estrichaufbau.

---

## 8. Möblierung in 3D

| Quelle | Inhalt | Zugang/Lizenz | Status |
|---|---|---|---|
| OFML 2.0 (3. Aufl.) | Parts ODB (2D/3D-Geometrie), OCD (kaufmännisch, Konfiguration, Preis), OAS, OAM, OEX; Materialien OMATS 2.2. Ursprung BSO, heute IBA | Spezifikation frei als PDF. Urheberrecht am Objektmodell bei E. Beier, an ODB, EGM und Produktdatenmodell bei **EasternGraphics** (Verwertung zustimmungspflichtig). Daten über pCon | [V] |
| IDM Living/Polster | konfigurierbare Wohnmöbel | Schema frei, Daten über DCC | [V] |
| Roomle | Konfigurator-Plattform, IDM-Import | kommerziell | [V] |
| BIMobject (inkl. IKEA) | IFC kostenlos, Qualität und Klasse schwankend | Nutzungsbedingungen je Objekt, Weiterverteilung eingeschränkt | [V]/[U] |
| CC0-Modelle (z. B. Poly Haven) | PBR-Assets, wenige Möbel | CC0 | [U] |

**Stellflächen:** DIN 18011 (1967) ist zurückgezogen. Schon 1990 hieß es, sie sei für Mindestgrößen ungeeignet [V]. Alte Werte als Startheuristik: Bewegungsfläche zwischen Stellfläche und Wand ≥ 70 cm, Eingangsflur ≥ 130 cm, Nebenflur ≥ 90 cm, Kinderbett 55 × 110 cm; bei Einbauschränken kein Abstand [V, irbnet-Faksimile]. Ersatz: DIN 18040-2 (Barrierefreiheit), VDI 6000 (Sanitär), AMK/HEA (Küche) und eigene Firmenregeln [U].

**IFC [V]:**
- `IfcFurnitureTypeEnum`: BED, CHAIR, DESK, FILECABINET, SHELF, SOFA, TABLE, TECHNICALCABINET. **Schrank, Kommode und Küchenschrank fehlen**, daher USERDEFINED.
- `Pset_FurnitureTypeCommon`: Style, NominalHeight/Length/Depth, MainColour, IsBuiltIn.
- Chair- und Table-Psets.
- GTIN über `Pset_ManufacturerTypeInformation`.
- Geometrie als `IfcRepresentationMap` am Typ, damit Varianten die Geometrie teilen.

---

## 9. Sims-Analogie und Wettbewerb

### Werkzeuge im Vergleich

| Werkzeug | Zielgruppe | IFC-Export | Status |
|---|---|---|---|
| Planner 5D | Laien | nein. PRO exportiert DWG/DXF nur in 2D | [V] |
| RoomSketcher | Laien, Makler | nein, nur JPG/PNG/PDF | [V] |
| Coohom | Interior, Küche/Bad | nein, CAD/PDF/JPG, „kein Export des ganzen Modells“ | [V] |
| Floorplanner, Homestyler, IKEA Kreativ | Laien | nicht geprüft | [U] |
| Roomle | Handel, Konfigurator | nicht geprüft | [U] |
| **Palette CAD** | Bad, Fliese, Küche, Interior | **ja**, IFC-Import und -Export, dazu GLB/FBX/STEP | [V] |
| Winner Flex (Compusoft/Cyncly) | Küche | IFC-Import von Räumen (nur aus Revit), IFC-Export ab 12.2a6 | [V] |
| CARAT, KPS | Küche | IFC nicht belegt; Schnittstellen zu Warenwirtschaft | [U] |
| PYTHA | Tischler | IFC nicht belegt | [U] |
| Vectorworks interiorcad | Tischler/Innenausbau | Vectorworks exportiert IFC, Version nicht geprüft | [U] |

### Literatur

Die DOIs stammen von Verlagsseiten. Die **Crossref-API war aus dieser Umgebung gesperrt**, deshalb ist Crossref-Verifikation offen.

- Ilbeigi, Bairaktarova, Morteza (2022): Gamification in Construction Engineering Education: A Scoping Review. 103 Studien, fast nur Ausbildung. doi:10.1061/(ASCE)EI.2643-9115.0000077 [V Verlags-PDF]
- Khalili-Araghi, Kolarevic (2016): Dimensional customization system. J. Building Engineering 5. doi:10.1016/j.jobe.2016.01.001 [V]
- Cloud-based BIM configurator mit Materialkatalogen und Code-Konformität (2024). Buildings 14(7) 2084. doi:10.3390/buildings14072084 [V]
- Customer integration framework for mass customised housing (2020). Sustainability 12(21) 8901. doi:10.3390/su12218901 [V]
- Pantazis et al. (2025): Building configurator mit Kit-of-parts, IFC-Erweiterung. IOP EES 1554 012035. doi:10.1088/1755-1315/1554/1/012035 [V]
- Shafiee et al. (2024): Garagen-Konfigurator mit CNC-Kette. AEDM, doi:10.1080/17452007.2024.2434589 [V]
- Skates, Wood (2006): Lessons on Architectural Simulation Taken from Drawing and Gaming. Wright stützt sich auf Christopher Alexander; die Abstraktion sei Absicht („fill in the blanks“). DOI nicht gefunden [U]
- ECGBL-Beitrag „From Designing Houses to Studying Architecture … The Sims“, Umfrage N = 54 [V, ohne DOI]

### Was übernehmen, was nicht [eigene Bewertung, U]

| Sims-Prinzip | Übernehmen als |
|---|---|
| Getrennte Modi „Bauen“ und „Kaufen“ | Gewerke-Modi (Rohbau/Grundriss · Oberflächen · Ausstattung), gekoppelt an den Reifegrad |
| Raster-Snap | Snap auf Fliesenraster, Achsraster, DIN-18101-Maße und Küchenraster; freies Platzieren nur mit Prüfung |
| Rot/grün beim Platzieren | Regelmaschine live: Bewegungsflächen, Tür-Schwenkbereich, W-Klasse, Kopfhöhe. Ergebnis mit Regel-ID und Quelle |
| Preis-Ticker | Laufende Kosten ab R-Reife mit Gültigkeitsdatum (IfcCostValue); Material und Leistung getrennt |
| Pipette, Farbvarianten | Varianten-Taxonomie: gleiche Serie, andere Farbe oder Format, ohne neu zu suchen |
| Ganzer Raum mit einem Klick streichen | IfcCovering je Raum (IfcRelCoversSpaces) |
| Rückgängig, Galerie | Versionen in der CDE (Recherche 06); freigegebene Stände unveränderlich |

| **Nicht** übernehmen | Grund |
|---|---|
| Wände beliebig abreißen oder versetzen | tragende Holzrahmenwände, Aussteifung, Werkplanung |
| Unendlich dünne Wände, Böden ohne Aufbau | Fertigfußboden, Estrichhöhe und Türhöhe hängen zusammen |
| Textur ohne Maßstab und Fuge | Fliese und Parkett haben reale Formate, Muster und Achse |
| Objekte ohne Anschluss (Waschbecken „irgendwo“) | Vorwand, Fallleitung, Abdichtung |
| „Bewegen“-Cheat (Objekte überlappen) | Stellflächen, Normabstände |
| Farbe wie auf dem Bildschirm | Farbmetrik und physisches Muster sind vertragsrelevant |

---

## 10. Suchbarkeit und Festschreibung

**Prinzip [U, Vorschlag]:**
1. **Artikel:** GTIN, Hersteller und Artikelnummer. Farbe, Oberfläche und Format stecken meist in eigenen GTINs.
2. **Leistung:** Muster, Fuge, Aufbau, Ebenheit, W-Klasse, STLB-LB.
3. **Kontext:** Raum, Fläche, Achse, Anschlüsse.
4. **Charge (A-Reife):** Kaliber, Farbton-Charge, `Pset_ManufacturerOccurrence.BatchReference`.

Festschreiben heißt: den kanonischen JSON-Text hashen (z. B. SHA-256 über JCS/RFC 8785 [U]). Der Hash kommt ins IFC und in den Vertrag (vgl. Recherche 06, IfcDocumentReference). Suchbar wird die Auswahl über normalisierte Facetten (Klasse, Merkmale, Einheiten). Das Mapping auf ETIM und ECLASS liefert die Parallelrecherche. **ETIM-Klassennummern für Fliese, Parkett und Wandfarbe habe ich nicht verifiziert**: Das ETIM-Portal war gesperrt, ETIM deckt laut ITEK auch „Baustoffe“ ab [U]. Keine Nummern erfinden.

**STLB-Bau 2026-04 [V]:**
- LB 023 Putz/Stuck/WDVS
- LB 024 Fliesen- und Plattenarbeiten
- LB 025 Estrich
- LB 027 Tischler
- LB 028 Parkett-, Holzpflasterarbeiten
- LB 029 Beschlag
- LB 030 Rollladen
- LB 031 Metallbau (Geländer)
- LB 034 Maler- und Lackierarbeiten – Beschichtungen
- LB 036 Bodenbelag
- LB 037 Tapezier
- LB 039 Trockenbau
- LB 045 Sanitär-Ausstattung

### Beispiel Fliesenauswahl (Reife A)

```json
{
  "selection_id": "c3f1e0a2-…",
  "schema": "hp-selection/0.1",
  "maturity": "A",
  "status": "frozen",
  "frozen_at": "2026-09-27T10:00:00+02:00",
  "content_hash": "sha256:…",
  "context": { "space": "EG-Bad", "surface": "Boden", "ifc_space_guid": "…", "ifc_covering_guid": "…",
               "area_net_m2": 7.84, "water_exposure_class": "W2-I", "floor_heating": true },
  "article": {
    "gtin": "40xxxxxxxxxxxx", "manufacturer": "…", "article_no": "…", "series": "…",
    "colour_name": "sand", "surface": "matt", "slip": { "r_class": "R10", "barefoot": "B" },
    "format_nominal_mm": [600, 1200], "thickness_mm": 9, "edge": "rektifiziert",
    "en14411_group": "BIa", "shade_variation": "V2",
    "batch": { "caliber": "…", "shade_lot": "…" }
  },
  "laying": {
    "pattern": "Drittelverband", "offset_fraction": 0.333, "angle_deg": 0,
    "origin": { "ref": "Achse Tür EG-Bad", "xy_mm": [0, 0] }, "direction": [1, 0],
    "joint_width_mm": 3,
    "grout": { "gtin": "…", "type": "CG2WA", "colour": "zementgrau" },
    "sealant": { "gtin": "…", "colour": "zementgrau" },
    "movement_joints": ["Randfuge", "Fuge Duschbereich"],
    "cut_rules": { "min_edge_fraction": 0.33, "symmetric": true },
    "waste_factor": 0.10
  },
  "build_up": {
    "substrate": "Zementestrich CT beheizt", "cm_limit_pct": 1.8,
    "waterproofing": { "type": "AIV-F", "product_gtin": "…" },
    "flatness": "DIN 18202 Tab. 3 Zeile 4", "adhesive": "C2 S1"
  },
  "procurement": { "stlb_lb": "024", "unit": "m2", "qty": 8.62, "price_valid_until": "2026-12-31" },
  "checks": [
    { "rule": "HP-FL-007", "src": "Hersteller/ZDB Großformat", "text": "Versatz ≤ 1/3", "result": "pass" },
    { "rule": "HP-FL-012", "src": "ZDB FI Zementäre Fugen", "text": "Fuge ≥ 3 mm", "result": "pass" },
    { "rule": "HP-AB-002", "src": "DIN 18534-1:2025-10", "text": "W2-I: Untergrund feuchteunempfindlich", "result": "pass" }
  ],
  "ifc": { "type_class": "IfcCoveringType", "predefined": "FLOORING",
           "psets": ["Pset_ManufacturerTypeInformation", "Pset_CoveringCommon", "Pset_CoveringFlooring", "HP_Verlegung", "HP_Fliese"] }
}
```

### Beispiel Treppe (Reife R)

```json
{
  "selection_id": "7b9d…", "maturity": "R", "status": "approved",
  "context": { "from_storey": "EG", "to_storey": "DG", "ffl_bottom_mm": 0, "ffl_top_mm": 2860,
               "opening_ifc_guid": "…", "building_class": "GK1", "dwellings": 1 },
  "geometry": {
    "din18065_form": "viertelgewendelt", "ifc_stair_type": "QUARTER_WINDING_STAIR",
    "turn": "links (DIN 107)", "risers": 16, "riser_mm": 178.75, "going_walkline_mm": 260,
    "usable_width_mm": 900, "walkline_offset_mm": 450,
    "winder": { "method": "Winkelmethode", "min_tread_inner_mm": 95, "winders": 5 },
    "headroom_min_mm": 2030
  },
  "construction": { "type": "Wangentreppe eingestemmt", "species": "Eiche", "grade": "durchgehende Lamelle",
                    "finish": "Lack seidenmatt", "risers": "geschlossen", "nosing_mm": 30 },
  "railing": { "infill": "senkrechte Stäbe", "clear_gap_mm": 120, "height_mm": 900,
               "handrail": { "material": "Eiche", "profile": "rund", "diameter_mm": 45, "height_mm": 900 } },
  "checks": [
    { "rule": "HP-TR-001", "src": "DIN 18065:2020 (≤2 WE)", "text": "2s+a = 617.5 in 590–650", "result": "pass" },
    { "rule": "HP-TR-004", "src": "DIN 18065:2020 6.5", "text": "Kopfhöhe ≥ 2000", "result": "pass" },
    { "rule": "HP-TR-009", "src": "DIN 18065 6.2 / Verziehungsmethode", "text": "eine Methode je Lauf", "result": "pass" },
    { "rule": "HP-UM-001", "src": "BayBO Art. 36 Abs. 2 + Firmenregel", "text": "Stababstand 120 (freiwillig, GK1)", "result": "info" }
  ],
  "procurement": { "stlb_lb": ["027", "031"], "supplier_article": null },
  "ifc": { "aggregate": "IfcStair", "parts": ["IfcStairFlight WINDER", "IfcRailing HANDRAIL", "IfcRailing BALUSTRADE", "IfcMember STRINGER"],
           "psets": ["Pset_StairCommon", "Pset_StairFlightCommon", "Pset_RailingCommon", "HP_Verziehung"] }
}
```

---

## Korrekturen und Warnungen

1. **DIN 51130 und DIN 51097 sind als eigenständige Normen überholt.** Beide Verfahren stehen in DIN EN 16165:2023; die R- und A/B/C-Klassen bleiben. Das Bewertungsregelwerk kommt aus ASR A1.5 und DGUV I 207-006, im EFH ist es nicht verbindlich [V].
2. **DIN 18534 Ausgabe 2025-10.** Gipsplatten in W2-I nur mit Herstellernachweis, in W3-I nur zementär. Für Holzrahmen-Nassräume bestimmt das die Beplankung [V].
3. **VDI 6000 Blatt 1:2008 ist ersetzt** durch Bl. 1 (Grundlagen) und Bl. 2 (Wohnungen), beide 2024-07 [V].
4. **DIN EN 13300:2023:** Glanz G1–G4, Nassabrieb in R-Klassen, Deckvermögen in H10-Klassen. Alte Grenzwerte nicht ungeprüft übernehmen [V/U].
5. **Verziehung:** DIN 18065 nennt Verhältnis-, Winkel- und Kreisbogenmethode. „Abwicklungsmethode“ ist kein Normbegriff; die Methode ist fachsprachlich eventuell mit der Verhältnismethode verwandt [U]. Mischen in einem Lauf ist unzulässig [V].
6. **BayBO Art. 36 hat keine Zahlenwerte.** 0,90/1,10 m stammen aus der alten DVBayBO bzw. dem Kommentar. **12 cm sind im EFH (GK 1/2) weder nach BayBO noch nach DIN 18065 gefordert.** Das ist eine Firmen- oder Haftungsentscheidung [V].
7. **IFC-Türanschlag ist spiegelverkehrt benannt:** SINGLE_SWING_LEFT = DIN-R [V].
8. **Pset_CoveringFlooring kennt nur Boolesche Werte** (HasNonSkidSurface, HasAntiStaticSurface). R-Klasse, Muster und Fuge gehören in eigene Psets [V].
9. **IfcFurnitureTypeEnum hat keinen Schrank und keinen Küchenschrank** [V].
10. **IfcStairFlight-Attribute sind deprecated.** Die Werte stehen in Pset_StairFlightCommon [V].
11. **RAL im Konfigurator ist lizenzpflichtig.** Die Digitalbibliotheken sind laut RAL nicht farbmetrisch [V].
12. **ZDB-Merkblatt „Groß- und Megaformate“ 2026-02 ist neu.** Versatz- und Fugenregeln daraus noch prüfen, das Merkblatt ist kostenpflichtig [U].
13. **DIN 18011 als Norm zitieren ist unzulässig.** Die Werte taugen nur als Heuristik [V].
14. **Crossref, ETIM-Portal, gesetze-bayern.de und die IFC-4.3-Doku-Site** waren gesperrt. Ich habe über GitHub-Rohdaten (IFC), Exa-Auszüge (BayBO) und Verlagsseiten (DOIs) ausgewichen.

## Offene Fragen an Regnauer

1. **Werkfliesung:** Werden Bad- und WC-Wände im Werk gefliest? Dann bestimmen Elementstöße, Transport und Toleranz den Fliesenspiegel, und der Achsbezug muss in die Werkplanung.
2. **Nassraum-Beplankung:** Welche Platte steht in W1-I und W2-I (Gipsfaser, Spezialgips mit Nachweis, zementgebunden)? Gibt es Systemnachweise des Plattenherstellers?
3. **Estrich und FBH:** Zement, Calciumsulfat oder Trockenestrich? Standard-Fertigfußbodenhöhe, Belegreife-Messung (wer, wann)? Gibt es R_λ,B-Grenzen im Standard (Teppich)?
4. **Standard-Oberflächen:** Q2 oder Q3 als Serie? Welcher Farbhersteller und welches Farbsystem? Hat Regnauer RAL- oder NCS-Lizenzen?
5. **Bemusterungspartner** für Fliese, Parkett, Tür, Treppe und Sanitär: Liefern sie GTIN, Datenblätter und 3D (IFC/GLB)? Datenformate IDM, BMEcat, ZVSHK?
6. **Treppenbau:** eigener Bau oder Zulieferer? Verziehungsmethode, Standard-Stababstand (12 cm freiwillig?), Handlaufhöhe, Holzarten und Sortierung.
7. **Türen:** Standardhöhe (2000/2125/raumhoch), Zargenart für die Holzrahmen-Wanddicke, Anschlagskonvention in der Werkssoftware (DIN oder Software-eigen)?
8. **Bodengleiche Dusche:** Standard oder Aufpreis? Wie wird die Holzbalkendecke dafür ausgebildet (Absenkung, Rinne)?
9. **Barrierefreiheit:** Wird DIN 18040-2 als Option angeboten (Schwellen ≤ 2 cm, 120 × 120)?
10. **Küche:** eigene Küchenpartner oder Kundenküche? Bekommt Regnauer IDM-Daten oder nur Anschlusspläne?
11. **Mängel und Toleranzen:** Welche DIN-18202-Zeile ist vertraglich Standard? Wie werden „erhöhte Anforderungen“ bepreist?
12. **LV-Struktur:** Nutzt Regnauer STLB-Bau oder GAEB für die Ausbaugewerke, oder eigene Leistungstexte?

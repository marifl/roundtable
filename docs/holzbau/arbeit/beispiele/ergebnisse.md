# Ergebnisse der Beispiele B1–B7

Lauf am 27.09.2026 mit Python 3.11.15, IfcOpenShell/ifctester 0.8.5, shapely 2.1.2, compas_timber 2.2.0
(Linux, venv nach `requirements-lock.txt`). Die Zahlen stammen aus `ausgabe/kennzahlen.json`
(`python alle_ausfuehren.py`).

## Tests

`python -m pytest` meldet **48 passed** in 7,8 s:

| Datei | Tests | Inhalt |
|---|---:|---|
| `tests/test_b1_wandelement.py` | 13 | Byte-Identität (im Prozess und über Prozesse mit verschiedenem Hash-Seed), GUIDs, GUID-Stabilität bei Parameteränderung, Klassen-Mapping, Typ, Kerve, Layer-Set, Psets, Georeferenz, Folie als IfcCovering, Holzanteil, Volumen aus Geometrie = Qto, Schema-Validierung |
| `tests/test_b2_b3.py` | 6 | U-Wert gegen Handrechnung, Grenzwerte, U-Wert im IFC, IDS gegen XSD, IDS-Fall bestanden und fehlerhaft |
| `tests/test_b4_b5.py` | 6 | H und T, Giebelprofil, drei Szenarien, SVG deterministisch, Treppe 2,90 m, Randfälle |
| `tests/test_b6_b7.py` | 23 | 16 Parser-Fälle, mehrdeutige Maße, Raumreferenzen, Annahme mit Ausgleich, Ablehnung, Fläche und Rückfragen, Determinismus, BTLx |

## B1 – Wandelement nach IFC4X3_ADD2

| Kennzahl | Wert |
|---|---|
| Schema | IFC4X3_ADD2 |
| Dateigröße | 135 927 Bytes (2 402 Zeilen) |
| Entitäten gesamt / davon IfcRoot | 2 393 / 391 |
| IfcWall (ELEMENTEDWALL) | 1, mit IfcMaterialLayerSetUsage (5 Schichten, 287,7 mm) und IfcWallType |
| IfcMember STUD / PLATE | 15 / 3 (Rand-, Raster-, Königs-, Sturzauflager-, Füllständer, Sturz / Schwelle, Rähm, Brüstungsriegel) |
| IfcPlate SHEET | 10 (GKF 4, OSB 4, HFD 2), Fensterausschnitt als Profil mit Aussparung |
| IfcBuildingElementPart | 12 INSULATION (je Gefach) + 1 USERDEFINED/MEMBRANE (Dampfbremse) |
| IfcMechanicalFastener SCREW | 176, Typ „Spanplattenschraube 4,0x50“ (NominalDiameter 4,0, NominalLength 50), Geometrie als IfcMappedItem |
| IfcVoidingFeature NOTCH | 1 (Kerve 40 × 25 mm in Ständer R1, über IfcRelVoidsElement) |
| IfcOpeningElement | 1 (Fenster 1,26 × 1,385 m) |
| IfcPropertySet / IfcElementQuantity | 30 / 42 |
| Pset_WallCommon | IsExternal = TRUE, LoadBearing = TRUE, ThermalTransmittance = 0,187 (aus B3) |
| Klassifikation | DIN 276 (2018-12), 331 „Tragende Außenwände“ |
| Georeferenz | IfcMapConversion auf IfcProjectedCRS EPSG:25832, Scale 0,001 (mm → m), fiktiver Ursprung |
| SHA-256 | `5a796ea7b0f1d8c0b92002155819ddee4ca7bf6b0ddd6bfe619fcf38f8bb478b` |
| Zweiter Lauf byte-identisch | ja (auch über getrennte Prozesse mit `PYTHONHASHSEED` 1 und 4711) |
| `ifcopenshell.validate` (Schema + EXPRESS-Regeln) | 0 Meldungen |
| Volumenprobe | für alle 41 Teile ist das tesselierte Volumen gleich Qto NetVolume (Abweichung < 1e-9 m³), einschließlich Ständer R1 mit abgezogener Kerve (0,03150 statt 0,03156 m³) |

Befunde zur Reproduzierbarkeit:

1. Mit `ifcopenshell.api` entstanden zunächst **nicht** reproduzierbare Dateien. Die Funktionen
   `aggregate.assign_object`, `unit.assign_unit`, `type.assign_type` und `material.assign_material` iterieren über
   Python-Mengen. Mit vier Hash-Seeds entstanden vier verschiedene SHA-256-Werte. Die Beziehungen werden
   deshalb jetzt direkt und mit fester Listenreihenfolge angelegt. Danach war die Datei byte-identisch.
2. Die GUIDs sind stabil gegenüber Parameteränderungen: Bei geänderter Brüstungshöhe (900 → 850 mm)
   behalten Wand, Rasterständer, Schwelle, Rähm und Brüstungsriegel ihre GlobalId (Test).
3. Die Kerve braucht einen Überstand von 1 mm. Koplanare Flächen zwischen Abzugskörper und Ständer lieferten
   sonst keinen korrekten Booleschen Abzug.

## B2 – IDS-Prüfung

`holzrahmenbau.ids` hat 11 Spezifikationen und ist gegen die IDS-1.0-XSD valide.

| ID | Anforderung | anwendbar | Fall „bestanden“ | Fall „fehlerhaft“ | eingebauter Fehler |
|---|---|---:|---|---|---|
| HRB-01 | Außenwand: U ≤ 0,20 W/(m²K) | 1 | ✔ | ✘ | F1: U = 0,25 |
| HRB-02 | Wand: IsExternal, LoadBearing | 1 | ✔ | ✔ | – |
| HRB-03 | Wand: DIN 276, KG 33x | 1 | ✔ | ✘ | F2: Klassifikation entfernt |
| HRB-04 | Wand: Material | 1 | ✔ | ✔ | – |
| HRB-05 | STUD: Material „KVH C24…“ | 15 | ✔ | ✘ (1 von 15) | F3: Material an „Ständer R2“ entfernt |
| HRB-06 | Member: Qto Length, NetVolume | 18 | ✔ | ✔ | – |
| HRB-07 | Member/Plate/Part: Teil einer IfcWall | 41 | ✔ | ✔ | – |
| HRB-08 | FastenerType: NominalDiameter/-Length | 1 | ✔ | ✘ | F4: Durchmesser am Typ gelöscht |
| HRB-09 | Fastener: NominalDiameter 2–12 mm | 176 | ✔ | ✘ (1 von 176) | F5: 20 mm |
| HRB-10 | Dämmung: Material „insulation“ | 12 | ✔ | ✔ | – |
| HRB-11 | kein IfcBuildingElementProxy | 0 / 1 | ✔ | ✘ | F6: Proxy ergänzt |

Ergebnis: Der Fall „bestanden“ erfüllt 11 von 11 Spezifikationen. Der Fall „fehlerhaft“ scheitert an genau den
6 Spezifikationen mit eingebautem Fehler. Die Berichte liegen als JSON (ifctester), HTML (ifctester) und
Markdown (eigene Zusammenfassung) in `ausgabe/ids_bericht_*`.

Befunde: (a) ifctester 0.8.5 ignoriert das Spezifikationsattribut `identifier`. (b) Attribut-Facetten
werden nicht vom Typ geerbt, deshalb steht `NominalDiameter` redundant am Exemplar.

## B3 – U-Wert nach DIN EN ISO 6946

Aufbau von innen nach außen, λ in W/(mK) als Beispielwerte:

- GKF 12,5 mm (0,25)
- OSB 15 mm (0,13)
- Dampfbremse (thermisch vernachlässigt)
- Gefach 200 mm: KVH (0,13) und Holzfaser (0,038)
- HFD 60 mm (0,043)
- Rsi = 0,13 m²K/W

| Variante | Holzanteil | R′ (oben) | R″ (unten) | e | U [W/(m²K)] |
|---|---:|---:|---:|---:|---:|
| Raster, verputzt (Rse 0,04) | 9,6 % | 6,304 | 6,001 | 2,5 % | **0,163** |
| Raster, hinterlüftet (Rse 0,13) | 9,6 % | 6,402 | 6,091 | 2,5 % | 0,160 |
| Geometrie, verputzt | 22,5 % | 5,568 | 5,139 | 4,0 % | **0,187** → IFC |
| Geometrie, hinterlüftet | 22,5 % | 5,670 | 5,229 | 4,1 % | 0,183 |

Handrechnung (Raster, verputzt), im Test nachgeprüft:

- R_a = 3,26919
- R_b = 6,99389
- R′ = 1/(0,096/3,26919 + 0,904/6,99389) = 6,30436
- λ″ = 0,046832, daraus R″ = 6,00132
- R_T = 6,15284, U = 0,16253 W/(m²K)

Das Programm liefert 0,162527 W/(m²K). Die Abweichung ist kleiner als 5·10⁻⁵.

Der Holzanteil „Geometrie“ ist die Holzfläche in der Ansicht (2,5752 m²) bezogen auf die Wandfläche ohne Fenster
(11,4549 m²). Er enthält Schwelle, Rähm, Sturz und Öffnungshölzer und ist deshalb deutlich höher als b/e.

## B4 – Abstandsflächen BayBO Art. 6

Das Grundstück misst 20 × 30 m, im Süden liegt eine Straße mit 8 m Breite. Das Haus misst 10 × 12 m und hat
eine Wandhöhe von 6,50 m. Das Satteldach hat 45° Neigung und eine Dachhöhe von 5,00 m, der First liegt in y-Richtung.

| Szenario | Wand | H [m] | T erf. [m] | T vorh. [m] | außerhalb [m²] | ok |
|---|---|---:|---:|---:|---:|---|
| mittig (x=5, y=9) | West/Ost (Traufe) | 8,17 | 3,27 | 5,00 | 0 | ✔ |
| | Süd/Nord (Giebel, „drittel“) | 8,17 (First) | 3,00–3,27 | 13,0 / 9,0 | 0 | ✔ |
| zu_nah (x=2) | West (Traufe) | 8,17 | 3,27 | 2,00 | **15,20** | ✘ |
| an_strasse (y=1) | Süd (Giebel) | 8,17 | 3,27 | 5,00 (bis Straßenmitte) | 0 | ✔ |
| mittig, Lesart „voll“ | Süd/Nord (Giebel) | 11,50 | 3,00–4,60 | 13,0 / 9,0 | 0 | ✔ |

Giebelprofil „drittel“ (u in m, T in m): (0; 3,00) · (3,0; 3,00) · (5,0; 3,27) · (7,0; 3,00) · (10; 3,00).
Das ergibt die gestauchte Giebelform mit 30,53 m². In der Lesart „voll“ sind es 36,40 m².
SVG-Skizzen: `ausgabe/abstandsflaechen_*.svg`. Welche Lesart für den Giebel gilt, ist nicht am Gesetzestext geprüft [U].

## B5 – Treppe DIN 18065 (Geschosshöhe 2,90 m, Laufbreite 0,90 m)

| n | s [mm] | a zulässig [mm] (5-mm-Raster) | Lösungen |
|---:|---:|---|---:|
| 15 | 193,33 | 230–260 | 7 |
| 16 | 181,25 | 230–285 | 12 |
| 17 | 170,59 | 250–305 | 12 |
| 18 | 161,11 | 270–325 | 12 |
| 19 | 152,63 | 285–340 | 12 |
| 20 | 145,00 | 300–360 | 13 |

Es gibt **68 zulässige Lösungen**. Die beste hat **17 Steigungen à 170,6 mm und 16 Auftritte à 290 mm**:

- 2s + a = 631,2 mm (Ziel 630 ± 2,5 mm)
- a − s = 119,4 mm (Bequemlichkeitsregel 120)
- a + s = 460,6 mm (Sicherheitsregel 460)
- Lauflänge 4,64 m

Mit einer Lauflänge von höchstens 4,0 m ist die beste Lösung 16 × 181,25 / 265 mm. Eine Laufbreite von 0,75 m
ergibt keine Lösung. Ohne die Toleranz von 2,5 mm auf das Schrittmaß hätte die Rundung eine Treppe mit
20 Steigungen und 6,46 m Lauflänge auf Rang 1 gesetzt. Die Toleranz ist deshalb bewusst gesetzt.

## B6 – Deterministische Sprachpipeline (Intent-Modell = Stub)

| Äußerung | Intent (p, STUB) | Maß (Muster) | Ergebnis |
|---|---|---|---|
| Mach das Bad oben zwei Meter sechzig breit | raum_aendern 0,91 | 2,60 m (A) | angenommen: Bad 2,40 → 2,60; Kinderzimmer 1 3,50 → 3,30 |
| Das Bad oben bitte eins zwanzig breit | raum_aendern 0,91 | 1,20 m (C) | abgelehnt: 1,20 m < Mindestbreite 1,70 m |
| Das Bad soll zwanzig Zentimeter breiter werden | raum_aendern 0,91 | 0,20 m (B) | Rückfrage: „Bad“ mehrdeutig (EG/OG) |
| Mach das Kinderzimmer 2 auf 3,20 m | raum_aendern 0,78 | 3,20 m (B) | angenommen: 3,50 → 3,20; Kinderzimmer 1 → 3,80 |
| Das zweite Kinderzimmer soll zwölf Quadratmeter haben | raum_aendern 0,91 | 12 m² (B) | angenommen: 3,55 m (12,07 m², Raster 5 cm) |
| Mach das Kinderzimmer 1 einen Meter zwanzig schmaler | raum_aendern 0,91 | 1,20 m (A) | abgelehnt: 2,30 m < 2,60 m und 7,82 m² < 10 m² |
| Das Bad oben eins fünf breiter | raum_aendern 0,91 | 1,05 m (C, mehrdeutig) | Rückfrage: 1,05 oder 1,50 m? |
| Stell die Dachneigung auf 35 Grad | dach_aendern 0,88 | 35° (B) | erkannt, im PoC nicht umgesetzt |
| Kannst du das mal anders machen | sonstiges 0,46 | – | Rückfrage: Intent unsicher |

Die Raumreferenz „das Bad oben“ wird zu IfcSpace-GUID `1cRQfmv29HlfHiIPofgLWT` aufgelöst.
Alle Wahrscheinlichkeiten sind feste Stub-Werte und keine Modellausgaben.

## B7 – BTLx (optional, lauffähig)

`ausgabe/wandelement.btlx` hat 18 365 Bytes und enthält 18 Parts. Die Hölzer tragen `Material="KVH C24"` und
`TimberGrade="C24"`. Die Kerve steht als `Lap` in Ständer R1 (StartX 990, Länge 40, Tiefe 25 mm).
Die Datei ist reproduzierbar (SHA-256 `fc91a532…765ff24d`). Aufwand bis lauffähig: etwa 15 Minuten.
Nicht geprüft: XSD-Validität, weil design2machine.com gesperrt war, und der Import in eine Abbundsoftware.

## Nicht möglich in dieser Umgebung

- **buildingSMART Validation Service** (validate.buildingsmart.org): Das Netz ist gesperrt (Proxy 403). Geprüft
  wurde nur lokal mit `ifcopenshell.validate` (Schema und EXPRESS-WHERE-Regeln), ohne die Gherkin-Regeln des Service.
- **BayBO-Primärtext** (gesetze-bayern.de): gesperrt. B4 folgt der Regelzusammenfassung aus Recherche 02.
- **BTLx-XSD** (design2machine.com): gesperrt.
- **OR-Tools**: nicht installiert, weil unnötig. B5 zählt den Suchraum vollständig auf.

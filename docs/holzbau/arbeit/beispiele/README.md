# Lauffähige Beispiele: regelbasierter Holzrahmenbau-Entwurfsgenerator

Stand: 27.09.2026 · Python 3.11.15 · IfcOpenShell 0.8.5

## Zweck

Die Beispiele sind ein **Proof of Concept** für die technische Machbarkeit der Kette

```
Parametermodell (JSON) → deterministischer Code → IFC4X3_ADD2 (ISO 16739-1:2024) → IDS-Prüfung
```

und für die regelbasierten Bausteine daneben: Wärmeschutz, Abstandsflächen, Treppe
und den deterministischen Teil der Sprachsteuerung. Jedes Beispiel ist eine eigene,
kommentierte Datei mit pytest-Tests. Die Beispiele sind reproduzierbar: Bei gleicher
Eingabe und gleichen Paketversionen entstehen byte-identische IFC- und BTLx-Dateien.

| Nr. | Datei | Inhalt | Ausgabe (`ausgabe/`) |
|---|---|---|---|
| B1 | `b1_wandelement.py` | Holzrahmen-Wandelement 4,80 × 2,75 m aus `daten/wandelement.json` → IFC4X3_ADD2. Umfang: Ständer, Schwelle/Rähm, Fenster mit Sturz/Brüstung/Jack-Studs, Beplankung, Dämmung, Folie, Schrauben mit Typ, Kerve, Layer-Set, Psets/Qtos, DIN-276-Klassifikation, Georeferenz EPSG:25832, deterministische GUIDs | `wandelement.ifc` |
| B2 | `holzrahmenbau.ids`, `b2_ids_pruefung.py` | IDS 1.0 mit 11 Spezifikationen, Prüfung mit ifctester: ein Fall besteht, ein absichtlich fehlerhafter Fall scheitert | `ids_bericht_*.json/.html/.md`, `wandelement_fehlerhaft.ifc` |
| B3 | `b3_uwert_iso6946.py` | U-Wert nach DIN EN ISO 6946 mit inhomogener Schicht (oberer/unterer Grenzwert), Holzanteil aus dem Raster und aus der Geometrie, verputzt/hinterlüftet | `uwert.json` |
| B4 | `b4_abstandsflaechen.py` | Abstandsflächen nach BayBO Art. 6 für ein Satteldach mit gestauchter Giebelform, Prüfung gegen die Grundstücksgrenze (shapely), Tabelle und SVG | `abstandsflaechen.md/.json`, `*.svg` |
| B5 | `b5_treppe_din18065.py` | Treppenlauf-Solver nach DIN 18065 (Wohngebäude ≤ 2 WE): alle zulässigen Lösungen und die beste Lösung | `treppe.json` |
| B6 | `b6_intent_pipeline.py` | deutscher Zahlen- und Einheitenparser, Auflösung von Raumreferenzen gegen `daten/haus_state.json`, Intent `raum_aendern` mit Regelprüfung. **Das Intent-Modell (Laya/Jev) ist nur ein Stub** | `intent_protokoll.json` |
| B7 | `b7_btlx_export.py` | optional: BTLx-Export der 18 Hölzer mit compas_timber, mit der Kerve als `Lap` | `wandelement.btlx` |
| N | `nachweis.py`, `nachweise_b1_b5.py` | Nachweis-Framework: rechnerischer und grafischer Nachweis je Regelprüfung (Einheitenprüfung, Rundung, GUM-Unsicherheit, Hash, JSON/Markdown/HTML, maßstäbliche SVG), nachgerüstet für B1–B5 ohne Änderung der Rechenkerne; siehe [`NACHWEIS.md`](NACHWEIS.md) | `nachweise/*.json/.md/.html`, `nachweise/svg/` |
| – | `alle_ausfuehren.py` | führt B1–B7 und die Nachweishefte aus und sammelt die Kennzahlen | `kennzahlen.json` |

Die Ergebnisse und Kennzahlen stehen in [`ergebnisse.md`](ergebnisse.md).

## Installation

```bash
cd docs/holzbau/arbeit/beispiele
python3.11 -m venv .venv && . .venv/bin/activate
pip install --upgrade pip setuptools wheel   # nötig für odfpy (Abhängigkeit von ifctester)
pip install -r requirements.txt              # direkte Abhängigkeiten, gepinnt
# exakt reproduzierbar (alle transitiven Pakete):  pip install -r requirements-lock.txt
```

Hinweis: Auf Debian/Ubuntu scheitert `pip install ifctester` außerhalb einer venv am
Paket `odfpy` (setup.py-Build mit dem System-setuptools). In einer venv mit aktuellem
setuptools funktioniert es.

## Aufruf

```bash
python b1_wandelement.py            # → ausgabe/wandelement.ifc (+ Kennzahlen auf stdout)
python b3_uwert_iso6946.py          # → ausgabe/uwert.json
python b2_ids_pruefung.py           # → IDS-Berichte (bestanden/fehlerhaft)
python b4_abstandsflaechen.py [--giebel-modus drittel|voll]
python b5_treppe_din18065.py [--geschosshoehe 2.90] [--laufbreite 0.90] [--max-lauflaenge 4.0]
python b6_intent_pipeline.py ["Mach das Bad oben zwei Meter sechzig breit"]
python b7_btlx_export.py            # optional, benötigt compas_timber
python nachweise_b1_b5.py           # → ausgabe/nachweise/ (7 Nachweishefte, 32 Nachweise)
python alle_ausfuehren.py           # alles + ausgabe/kennzahlen.json
python -m pytest                    # 48 Tests
```

## Erwartete Ausgaben (Kurzfassung)

- **B1:** `wandelement.ifc`, 135 927 Bytes, 2 393 Entitäten. Klassen: 1 IfcWall, 18 IfcMember (15 STUD, 3 PLATE),
  10 IfcPlate, 13 IfcBuildingElementPart, 176 IfcMechanicalFastener, 1 IfcVoidingFeature.
  Ein zweiter Lauf erzeugt dieselbe Datei (SHA-256 `5a796ea7…b478b`). `ifcopenshell.validate`
  mit EXPRESS-Regeln meldet nichts.
- **B2:** Die erzeugte Datei besteht alle 11 Spezifikationen. Die fehlerhafte Datei scheitert an
  HRB-01, 03, 05, 08, 09 und 11, also genau an den sechs eingebauten Fehlern.
- **B3:** U = 0,163 W/(m²K) mit Holzanteil aus dem Raster (9,6 %) und U = 0,187 W/(m²K) mit Holzanteil
  aus der Geometrie (22,5 %, verputzt). Der zweite Wert steht in `Pset_WallCommon.ThermalTransmittance`.
- **B4:** Traufseite T = 3,27 m. Szenario „mittig“ und „an_strasse“ sind zulässig, „zu_nah“ ist
  unzulässig: 15,2 m² liegen außerhalb des Grundstücks.
- **B5:** 68 zulässige Lösungen. Die beste hat 17 Steigungen à 170,6 mm, einen Auftritt von 290 mm,
  2s + a = 631,2 mm und eine Lauflänge von 4,64 m.
- **B6:** Für 9 Beispielsätze entstehen: angenommen, abgelehnt (mit Begründung), Rückfrage und „nicht umgesetzt“.
- **B7:** `wandelement.btlx` mit 18 Parts und 1 Lap-Bearbeitung, reproduzierbar.

## Grenzen

- **Keine Rechts- oder Normauskunft.** Die Kennwerte stammen aus den Recherchedokumenten 02 und 05.
  Normtexte und DIN-Tabellen sind nicht übernommen. Die λ-Werte in `daten/wandelement.json` sind
  **Beispielwerte**. Die Projektregeln in B6 (Mindestbreiten, Mindestflächen) sind **Beispielwerte, keine Norm**.
- **B1:** Die Geometrie besteht aus einfachen Extrusionen (achsparallel). Nicht modelliert sind IfcWindow,
  Verbindungen (IfcRelConnects…), Nagel- und Klammerbilder sowie Schrauben in GKF und HFD.
  Die Schichtfolge ist fest: GKF | OSB | Folie | Gefach | HFD. Die inhomogene Gefachschicht trägt im Layer-Set
  das Dämmstoffmaterial; das Holz steht im Layer-Namen. Die Ständer haben ein IfcMaterial, kein Profil-Set.
  Getestet ist das nur mit IfcOpenShell. Der Import in Autorensoftware (Revit, ArchiCAD, cadwork) und der
  buildingSMART Validation Service sind nicht geprüft; der Service ist online, und das Netz war gesperrt.
- **B1, Determinismus:** Mehrere Funktionen von `ifcopenshell.api` erzeugen Beziehungen, Einheiten und
  Platzierungen in einer Reihenfolge, die vom Hash-Seed abhängt (Python-`set`). Mit `PYTHONHASHSEED=1/2/3/99`
  entstanden vier verschiedene Dateien. B1 legt Beziehungen und Einheiten deshalb direkt an; siehe
  `IfcWandBauer.beziehung`. Byte-Identität gilt nur bei derselben IfcOpenShell-Version, denn die Version
  steht im Header.
- **B2:** ifctester 0.8.5 liest das IDS-Attribut `identifier` nicht ein, deshalb wird die ID aus dem Namen
  gelesen. Attribut-Facetten werden nach IDS 1.0 nicht vom Typ geerbt. Deshalb stehen `NominalDiameter` und
  `NominalLength` redundant am Typ und am Exemplar. Die JSON- und HTML-Berichte enthalten die Prüfzeit und
  sind daher nicht byte-identisch.
- **B3:** Die Korrekturen ΔU sind nicht angesetzt (Luftspalte Stufe 0; die Befestigungen durchdringen die
  Dämmung nicht). Die Fensterfläche bleibt außen vor. Wärmebrücken an den Elementstößen fehlen.
- **B4:** Das Gelände ist eben. Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 sind nicht berücksichtigt.
  Welche Lesart für den Giebel gilt („drittel“, Standard nach Aufgabenstellung, oder „voll“), ist am
  Primärtext der BayBO 2026 **nicht geprüft** [U]: gesetze-bayern.de war aus der Build-Umgebung nicht erreichbar.
- **B5:** Nur eine gerade einläufige Treppe. Kopfhöhe, Podeste, Wendelung und Toleranzen fehlen.
  Die Bequemlichkeits- und die Sicherheitsregel sind Faustregeln und dienen nur der Rangfolge.
  Einen Constraint-Solver (OR-Tools) braucht es nicht, weil der Suchraum vollständig aufgezählt wird.
- **B6:** Das Intent-Modell ist ein **Stub mit festen, erfundenen Wahrscheinlichkeiten**. Die Werte sagen nichts
  über Laya oder Jev. Die Grammatik ist klein: Zahlen 0–999, „komma“, „anderthalb“. Räume werden
  nach Typ, Geschoss, Nummer und groß/klein aufgelöst, nicht nach „links/rechts“ oder „neben“.
  Nur die Breite ist änderbar. Der Ausgleich erfolgt beim Nachbarraum in derselben Raumzeile.
- **B7:** compas_timber 2.2.0 ist Beta und schreibt BTLx mit `Version="2.0.0"`. Die Datei ist nicht gegen
  die XSD geprüft, weil design2machine.com nicht erreichbar war. Verbindungen fehlen. Material, Datum und
  GUIDs werden nachträglich deterministisch gesetzt.

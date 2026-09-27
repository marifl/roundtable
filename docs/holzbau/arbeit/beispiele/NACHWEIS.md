# Nachweis-Framework (`nachweis.py`)

Stand: 27.09.2026 · Modul 1.0.0 · Schema 1.0 · Python 3.11.15, pint 0.25.3, matplotlib 3.11.2

Jede Regelprüfung und jede Berechnung des Hausplaners wird als **Nachweis** dokumentiert. Ein Nachweis ist
rechnerisch und grafisch nachvollziehbar, ohne dass man den Code lesen muss. Er entsteht in drei Formen:

- **JSON** für Maschinen, geprüft gegen [`nachweis.schema.json`](nachweis.schema.json)
- **Markdown** für Repository und Review
- **HTML** zum Lesen und Drucken, mit Formeln (MathJax), Ampel und eingebetteten SVG-Zeichnungen

Mehrere Nachweise bilden ein **Nachweisheft** mit Deckblatt, Inhaltsverzeichnis, Regelwerk-Versionen und Heft-Hash.
Die wissenschaftliche Begründung steht im Kapitelentwurf [`../07a-nachweisfuehrung.md`](../07a-nachweisfuehrung.md).

## Dateien

| Datei | Inhalt |
|---|---|
| `nachweis.py` | Datenklassen, Einheitenprüfung, Rundung, Unsicherheit, Hash, Markdown/HTML/JSON, Grafik-Helfer |
| `nachweis.schema.json` | JSON-Schema (Draft 2020-12) für Nachweis und Nachweisheft |
| `nachweise_b1_b5.py` | Nachrüstung der Beispiele B1–B5, ohne deren Rechenkerne zu ändern |
| `tests/test_nachweis.py` | 50 Tests (Einheiten, Rundung, Hash, Unsicherheit, Rendering, Schema, Nachrüstung, Determinismus) |
| `ausgabe/nachweise/` | erzeugte Nachweishefte (`*.json`, `*.md`, `*.html`), Grafiken in `svg/`, `uebersicht.json` |

```bash
python nachweise_b1_b5.py                 # → ausgabe/nachweise/ (etwa 4 s)
python nachweise_b1_b5.py --ausgabe /tmp/x
python -m pytest tests/test_nachweis.py   # 50 Tests
NACHWEIS_EINHEITEN=einfach python nachweise_b1_b5.py   # ohne pint (eigene Dimensionsprüfung)
```

## Aufbau eines Nachweises

```
Nachweis
├─ id, titel
├─ gegenstand      Bezeichnung, IFC-GlobalId, IFC-Klasse, IFC-Datei + SHA-256, weitere GUIDs
├─ regel           Text, Quelle, Fassung, Fundstelle, [V]/[U], Regelwerk-Profil + Version
├─ eingaben[]      Groesse: Name, Symbol, Wert, Einheit, Quelle, Art, u (k = 1), Verteilung, Bezug
├─ schritte[]      Schritt: Beschreibung, Ausdruck (Python-Teilmenge), Formel (LaTeX),
│                  eingesetzte Werte (LaTeX), Normverweis, Ergebnis-Groesse
│                  oder: Verfahren (Algorithmus, Werkzeug, Version) + übernommenes Ergebnis
├─ kriterien[]     Ist ⟂ Grenzwert (≤ ≥ < > =), Toleranz, Ausnutzung η, erfüllt,
│                  Rundungsempfindlichkeit, Entscheidung innerhalb von U
├─ ergebnis, grenzwert, vergleich, ausnutzung, status (erfüllt | nicht erfüllt | Hinweis)
├─ annahmen[], hinweise[]
├─ unsicherheit    GUM linear: u_c, U = k·u_c, Sensitivitäten, Beiträge; optional Monte-Carlo
├─ gegenrechnungen Vergleich mit dem Rechenkern (Zweitrechnung)
├─ grafiken[]      SVG + SHA-256, Art (diagramm | lageplan | schnitt | ansicht | grundriss), Maßstab
├─ umgebung        Python- und Paketversionen, Einheiten- und Grafik-Backend (nicht im Hash)
├─ zeitstempel     nur wenn übergeben oder SOURCE_DATE_EPOCH gesetzt (nicht im Hash)
└─ hash            SHA-256 über kanonisches JSON (ohne hash, zeitstempel, umgebung)
```

### Größen und Arten

`Groesse.art` kennzeichnet die Herkunft jedes Werts:

| Art | Bedeutung | Darstellung |
|---|---|---|
| `eingabe` | Wert aus Parametermodell, Modell oder Nutzereingabe | Quelle mit JSON-Pfad |
| `annahme` | Festlegung ohne Beleg, z. B. Rohdichte als Beispielwert | gelb hinterlegt, zusätzlich unter „Annahmen“ |
| `konstante` | normative Konstante, z. B. R_si = 0,13 m²·K/W | Normverweis |
| `grenzwert` | Anforderung der Regel | Normverweis |
| `zwischenergebnis`, `ergebnis` | berechnet | Anzeige gerundet, gerechnet ungerundet |

### Einheiten

Einheiten werden in Anzeige-Notation geschrieben (`W/(m²·K)`, `m²·K/W`, `kg/m³`, `°`, `%`, `Stk`). Jeder Schritt wird
mit Größen gerechnet, nicht mit Zahlen. Das Ergebnis wird in die deklarierte Einheit umgerechnet:

- `d/lam` mit d in mm und λ in W/(m·K) ergibt korrekt m²·K/W. Eine Umrechnung von Hand entfällt.
- `d + lam` bricht mit `EinheitenFehler` ab. Das gilt auch, wenn die Ergebniseinheit nicht passt oder ein Kriterium
  unverträgliche Größen vergleicht.

Backend: `pint`, falls installiert, sonst `EinheitenEinfach` mit sieben Basisdimensionen und einer kleinen
Einheitentabelle. Beide Backends liefern für alle 32 Nachweise B1–B5 **denselben Hash** (Test). Temperaturen gehen nur
als Differenzen in K ein; °C wird nicht unterstützt.

### Ausdrücke

Ausdrücke sind eine sichere Teilmenge von Python. Sie werden als AST geprüft und ausgewertet, nicht mit `eval`:

- Operatoren `+ − * / **` und Zahlen
- Symbole der Eingaben und früherer Schritte, dazu `pi`
- Funktionen `min, max, abs, sqrt, tan, sin, cos, atan, ceil, floor`

Aus demselben AST entstehen die Formel in LaTeX und die Zeile mit eingesetzten Werten und Einheiten, zum Beispiel
$R = \frac{200\ \mathrm{mm}}{0{,}038\ \mathrm{W/(m\cdot K)}} = 5{,}2632\ \mathrm{m^2\cdot K/W}$. Schritte ohne
geschlossene Formel werden als **Verfahren** beschrieben: Polygonverschneidung, vollständige Aufzählung, IDS-Prüfung.
Ihr Ergebnis übernimmt der Nachweis mit Werkzeug und Version.

### Rundung

Gerechnet wird ungerundet. Gerundet wird nur die Anzeige, und die Regel steht jeweils im Bericht:

```python
Rundung("signifikant", 2, "halb_auf", quelle="DIN EN ISO 6946:2018-03, 6.5.2")   # U-Wert → 0,19
Rundung("dezimalstellen", 2, "auf", quelle="sicherheitsgerichtet")               # erforderliche Tiefe → 3,27 m
```

- Verfahren: `halb_auf` (ISO 80000-1 Anh. B Regel B, DIN 1333), `halb_gerade` (Regel A), `auf` und `ab`
  (sicherheitsgerichtet, B.5). Gerundet wird in einem Schritt (B.4), auf Basis der Dezimaldarstellung (`repr`).
- `runde_mit_unsicherheit(y, U)` setzt die Rundestelle nach DIN 1333 aus U und rundet U auf, z. B. „650 ± 70 kg“.
- Ein Kriterium ist **rundungsempfindlich**, wenn der gerundete Anzeigewert anders entscheiden würde als der
  ungerundete, z. B. U = 0,2049 → „0,20“ ≤ 0,20. Das Framework meldet das als Hinweis.
- Zwischenwerte werden mit 5 signifikanten Stellen angezeigt, Zahlen mit Dezimalkomma. Ab fünf Stellen vor dem
  Komma wird in Dreiergruppen gegliedert. Sehr kleine Werte erscheinen als „1,1 · 10⁻¹⁶“.

### Unsicherheit

Erhält eine Eingangsgröße `unsicherheit=u` (Standardunsicherheit, k = 1), berechnet der Nachweis für das Ergebnis:

- die Sensitivitäten $c_i = \partial f/\partial x_i$ numerisch durch zentrale Differenzen **über die gesamte
  Rechenkette**, in SI-Zahlenwerten. Korrelationen über gemeinsame Zwischengrößen werden damit korrekt erfasst
  (Test: y = z + x mit z = x ergibt u = 2·u(x)).
- $u_c = \sqrt{\sum (c_i u_i)^2}$ und U = k·u_c mit k = 2 (JCGM 100:2008, 5.1.2 und 6.2.1).
- Beitrag und Anteil jeder Eingangsgröße (Unsicherheitsbudget).
- optional `monte_carlo=N`: Fortpflanzung der Verteilungen (normal oder Rechteck) nach JCGM 101:2008 mit festem Seed.

Verfahrensschritte gehen nicht in die Fortpflanzung ein; der Bericht weist darauf hin.

### Hash und Determinismus

- `hash` ist SHA-256 über das kanonische JSON: sortierte Schlüssel, keine Leerzeichen, UTF-8. Gleitkommazahlen sind
  auf 12 signifikante Stellen normiert.
- Ausgenommen sind `hash`, `zeitstempel` und `umgebung`.
- Grafiken gehen über ihren SVG-Text in den Hash ein. matplotlib läuft deterministisch: `svg.hashsalt`, keine
  Datums-Metadaten.
- Der **Heft-Hash** bildet sich aus Titel, Projekt und der geordneten Liste (ID, Status, η, Hash, GUID) aller Nachweise.
- Zwei Läufe in getrennten Prozessen mit `PYTHONHASHSEED` 1 und 4711 erzeugen byte-identische Dateien (Test).

## Grafik-Helfer

| Funktion | Zweck | Technik |
|---|---|---|
| `SvgZeichnung` | maßstäbliche Zeichnung: Modell → Papier-mm, `width`/`height` in mm | reines SVG |
| `lageplan_svg` | Grundstück, Gebäude, Abstandsflächen (grün/rot), Straße, Bemaßung, Maßstabsleiste, Nordpfeil, Legende, Schriftfeld | reines SVG, shapely-Polygone |
| `schnitt_svg` | Schichtaufbau mit Schraffuren, Einlagen (Ständer), Maßkette, Legende mit λ | reines SVG |
| `treppenschnitt_svg` | Stufenprofil, s/a, Gesamthöhe, Lauflänge | reines SVG |
| `diagramm_ist_grenzwert` | Ist-Balken gegen Grenzwert, Fehlerbalken U | matplotlib, sonst reines SVG |
| `diagramm_balken`, `diagramm_punkte` | Balken bzw. Streudiagramm mit zulässigem Bereich | matplotlib, sonst reines SVG |
| `balken_anteil_svg` | Anteil Elemente mit und ohne Verstoß (IDS) | reines SVG |

Die technischen Zeichnungen sind bewusst reines SVG. Nur so steuert der Code Maßstab, Linienbreiten
(0,25/0,35/0,5 mm), Schrifthöhen (2,5/3,5 mm) und Maßbegrenzung (Schrägstrich) exakt. Wird die Zeichnung mit 100 %
gedruckt, ist sie maßhaltig. Die Anlehnung an DIN 1356-1, ISO 128 und DIN 406 ist nicht am Normtext geprüft [U].

## Kurzbeispiel

```python
from nachweis import Nachweis, Gegenstand, Regel, Groesse as G, Schritt, Rundung

n = Nachweis(
    id="DEMO-01", titel="Wärmedurchlasswiderstand der Gefachdämmung",
    gegenstand=Gegenstand("Außenwand AW-01", "0gsiGQj_bG3wx8M0qwRA0U", "IfcWall"),
    regel=Regel("R = d/λ", "DIN EN ISO 6946:2018-03", "2018-03", "DE-Waermeschutz-Beispiel", "0.1.0",
                "6.7.1.1, Formel (3)", "[V]"),
    eingaben=[G("Dicke", "d", 200, "mm", "daten/wandelement.json", unsicherheit=2.0),
              G("Wärmeleitfähigkeit", "lambda_D", 0.038, "W/(m·K)", "Herstellerangabe (Beispiel)", unsicherheit=0.00114)],
    schritte=[Schritt("Wärmedurchlasswiderstand", G("Widerstand", "R", None, "m²·K/W"), "d/lambda_D")],
    ergebnis="R", grenzwert=G("Mindestwert", "R_min", 4.0, "m²·K/W", "Beispiel"), vergleich="≥",
    ergebnis_rundung=Rundung("dezimalstellen", 2, quelle="DIN EN ISO 6946:2018-03, 6.6"))
n.schreibe("ausgabe/demo")          # DEMO-01.json / .md / .html
print(n.status, n.ausnutzung, n.unsicherheit["anzeige"], n.hash)
# erfüllt 0.7599999999999999 5,3 ± 0,4 m²·K/W (k = 2) acedb1a5…
```

JSON-Ausschnitt (gekürzt):

```json
{
  "art": "nachweis", "schema_version": "1.0", "id": "DEMO-01",
  "gegenstand": {"bezeichnung": "Außenwand AW-01", "ifc_guid": "0gsiGQj_bG3wx8M0qwRA0U", "ifc_klasse": "IfcWall"},
  "regel": {"quelle": "DIN EN ISO 6946:2018-03", "fassung": "2018-03", "verifikation": "[V]",
            "regelwerk_profil": {"name": "DE-Waermeschutz-Beispiel", "version": "0.1.0"}},
  "schritte": [{"nr": 1, "ausdruck": "d/lambda_D", "formel_latex": "R = \\frac{d}{\\lambda_{\\mathrm{D}}}",
                "ergebnis": {"symbol": "R", "wert": 5.2631578947368425, "einheit": "m²·K/W", "dimension": "M^-1·T^3·Θ"}}],
  "kriterien": [{"ist": "R", "vergleich": "≥", "grenzwert": "R_min", "ausnutzung": 0.7599999999999999, "erfuellt": true}],
  "status": "erfüllt",
  "unsicherheit": {"k": 2.0, "u_c": 0.16643566632795925, "U": 0.3328713326559185, "anzeige": "5,3 ± 0,4 m²·K/W (k = 2)"},
  "hash": {"algorithmus": "SHA-256", "wert": "acedb1a555f2621f514cd671d41e1f723de039640c3f3be360fa6b5383518d73"}
}
```

## Nachrüstung B1–B5 (`nachweise_b1_b5.py`)

Die Nachweisschicht liegt **über** den Rechenkernen. Sie rechnet die Formelkette aus den offen gelegten Eingaben selbst
nach und vergleicht das Ergebnis mit dem Rechenkern („Gegenrechnung“). Die 48 bestehenden Tests bleiben grün.

| Heft | Nachweise | Status | Inhalt, Grafik |
|---|---:|---|---|
| `b1_wandelement` | 1 | erfüllt | Flächen, Volumen, Massen je Material (Rohdichten als Annahme, u = 5–15 %): m = 650 ± 70 kg (k = 2); Konsistenz der Volumen mit IFC-Qto; Wandansicht 1:50, Massendiagramm |
| `b2_ids_bestanden` | 11 | erfüllt | je IDS-Spezifikation: Kardinalität, Verstöße, GUIDs; Status = ifctester |
| `b2_ids_fehlerhaft` | 11 | 6 nicht erfüllt | HRB-01, 03, 05, 08, 09, 11 mit Befund und GUID |
| `b3_uwert` | 4 | erfüllt | ISO 6946 in 16 Schritten, R'_T/R''_T, U = 0,19 W/(m²·K) (2 sig. Stellen), U(k=2) = 0,007, Monte-Carlo; Horizontalschnitt 1:5, Grenzwert- und U-Diagramm |
| `b4_abstandsflaechen` | 4 | 1 nicht erfüllt (`zu_nah`) | H, T je Wand, Fläche außerhalb, T vorhanden; Lageplan 1:200, Tiefendiagramm |
| `b5_treppe` | 1 | erfüllt | n_min/n_max, 68 Lösungen, s, 2s + a, Lauflänge, 7 Kriterien; Schrittmaß-Diagramm, Treppenschnitt 1:50 |
| `gesamt` | 21 | nicht erfüllt (B4 `zu_nah`, absichtlich) | B1, B2 bestanden, B3, B4, B5 |

## Warum kein PDF

Ein PDF wird nicht erzeugt. Zur Wahl standen drei Wege:

- **WeasyPrint** braucht Pango und Cairo als Systembibliotheken. Das ist eine Systemabhängigkeit.
- **ReportLab** läuft ohne Systembibliotheken. Layout und Formelsatz müssten aber neu programmiert werden, und
  LaTeX-Formeln ließen sich nur über matplotlib-mathtext darstellen, nur als Teilmenge.
- **Headless-Browser** sind eine schwere Systemabhängigkeit.

Stattdessen hat das HTML ein Druck-Stylesheet: A4, Seitenumbruch je Nachweis, keine Trennung von Tabellen und
Abbildungen. „Drucken → Als PDF speichern“ im Browser ergibt ein PDF mit gesetzten Formeln. Voraussetzung ist, dass
MathJax geladen ist; sonst erscheint der LaTeX-Quelltext. Maßhaltig sind die Zeichnungen nur bei Druck in
„tatsächlicher Größe“.

## Grenzen

- MathJax kommt aus einem CDN (jsdelivr). Ohne Netz zeigt das HTML den LaTeX-Quelltext, der Inhalt bleibt vollständig.
- Die Unsicherheitsfortpflanzung ist linear und nimmt unkorrelierte Eingänge an. Die Unsicherheiten in B1 und B3 sind
  **Annahmen zur Demonstration**, keine ermittelten Werte.
- Die Zeichnungen folgen den Regeln technischer Zeichnungen nur sinngemäß. Nicht umgesetzt sind Planzeichen nach
  Anlage 1 BauVorlV / PlanZV, Katastergrundlage und Höhenangaben.
- B4 und B5 haben noch kein IFC-Gebäudemodell. Deshalb fehlt dort die GlobalId des Gegenstands; der Nachweis weist
  darauf hin.
- Der Hash weist Unverändertheit nach, nicht Urheberschaft. Eine Signatur, etwa nach eIDAS, oder ein Prüfvermerk ist
  nicht Teil des Frameworks.

# Recherche 02: Deutsche Regeln, Baurecht, Normen (maschinenlesbar?)

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft, **[U]** = unsicher.

## Ergebnis in 5 Punkten

1. **Eine fertige Regelprüfung für die BayBO gibt es nicht.** Aufbauen lässt sich auf MBO2BIM: IDS, OpenBimRL und eine Modellierungsrichtlinie.
2. **Bebauungspläne in Bayern sind nicht maschinenlesbar.** Meist gibt es nur den Umring plus PDF. GRZ, GFZ und Dachneigung erfasst deshalb der Nutzer im Dialog oder eine PDF-Extraktion.
3. **Der Gesetzestext der BayBO ist frei nutzbar.** Abstandsflächen, Vollgeschoss, Gebäudeklasse, Fensterfläche und Genehmigungsfreistellung sind klar implementierbar.
4. **Das GEG ist seit 29.07.2026 durch das GModG ersetzt.** DIN 4108-2 und EC 5 gibt es in neuen Ausgaben.
5. **DIN-Normen bleiben urheberrechtlich geschützt.** Kennwerte mit Normverweis darf man implementieren, Texte und Tabellen nicht kopieren. Für kommerzielle Nutzung eine Lizenz anfragen.

## 1. BIM-basierter Bauantrag und Regelprüfung

| Projekt | Was es liefert | Maschinenlesbar | Urteil |
|---|---|---|---|
| **MBO2BIM** (DIBt, Hamburg, RUB 2021–2023) [V] | Modellierungsrichtlinie MBO, IDS + MVD, Regeln in OpenBimRL, Objektvorlagen. Umgesetzt ist v. a. die Gebäudeklasse. Bericht: https://www.irbnet.de/daten/rswb/24049007645.pdf | ja | IDS übernehmen, Regeln adaptieren (MBO → BayBO) |
| **OpenBimRL** https://github.com/RUB-Informatik-im-Bauwesen/OpenBimRL [V] | Regelsprache; MIT (Code), CC-BY-4.0 (Schema). Engine hängt am proprietären Apstex-Framework | ja | Schema adaptieren, eigene Engine |
| **BIM-Bauantrag Hamburg/NRW 2020** [V] | Container aus XBau-Nachricht 200 + XPlanung + IFC + BCF. Prototypisch geprüft: Baugrenzen, GRZ, Geschossigkeit, Stellplätze, Gebäudeklasse, Abstandsflächen. PDF + mvdXML auf bimdeutschland.de | teilweise | als Referenz adaptieren |
| **BIM.GOV** (Hamburg + RUB) [U] | Piloten laufen, keine veröffentlichten Regeln gefunden | – | beobachten |
| **ACCORD** (EU, bis 08/2025) [V] | XPlanung + IFC als RDF, SPARQL. Kein produktives Tool veröffentlicht | – | Referenz |
| **Bayern, Landesbaudirektion** [U] | Modellierungsrichtlinie BayBO in Arbeit: IDS-Check, GK, Höhe, Brandschutz, Abstandsflächen mit BIM.permit. Nur für staatliche Bauten (Art. 73) | nicht öffentlich | Kontakt aufnehmen |

## 2. Bebauungsplan und Kataster Bayern

- **XPlanung** ist seit 08.02.2023 Pflicht [V]. Bayern führt B-Pläne meist im **Minimalstandard**: Umring plus Link auf PDF. Art und Maß der Nutzung sind nicht abfragbar [V].
- Das Landesportal geht am 31.10.2026 in **DiPlanung** über [V].
- **Datenmodell zum Übernehmen** [V]:
  - `BP_BaugebietsTeilFlaeche`, `BP_UeberbaubareGrundstuecksFlaeche`
  - `BP_BauGrenze`/`BP_BauLinie`
  - GRZ, Z
  - `BP_Dachgestaltung` mit DNmin, DNmax, DN, DNzwingend, dachform
- **Werkzeuge:** xPlanBox/XPlanValidator (AGPL-3.0, mit bayerischem Profil) unter gitlab.opencode.de/xleitstelle [V].
- **Kataster:**
  - ALKIS-Flurstücke sind **nicht frei**: etwa 2,90 € je Flurstück, mindestens 20 € [V].
  - Frei unter CC BY 4.0 (https://www.geodaten.bayern.de/opengeodata) [V]: Parzellarkarte als Raster ohne Nummern, Hausumringe, LoD2, DGM/DOM, Orthofotos.

## 3. BayBO: implementierbare Regeln (Fassung ab 01.05.2026) [V]

| Regel | Kern |
|---|---|
| Art. 6 Abstandsflächen | H = Wandhöhe + 1/3 Dachhöhe (Dachneigung ≤ 70°), voll bei > 70°. Tiefe **0,4 H, mindestens 3 m**; GE/GI 0,2 H. Giebel sind normale Wände (seit 2021). Abs. 5a: Gemeinden über 250.000 Einwohner abweichend. Abs. 6: Dachüberstände und Balkone unter Bedingungen unbeachtlich. Abs. 7: Grenzgaragen (Wandhöhe im Mittel ≤ 3 m, ≤ 9 m je Grenze, zusammen ≤ 15 m). Satzungen nach Art. 81 möglich |
| Vollgeschoss | über Art. 83 Abs. 6 → Art. 2 Abs. 5 in der Fassung bis 31.12.2007: vollständig über Gelände **und** ≥ 2,30 m Höhe auf ≥ 2/3 der Grundfläche. Keller zählt, wenn Deckenunterkante im Mittel ≥ 1,20 m über Gelände. Bei alten B-Plänen gilt die damalige Fassung |
| Gebäudeklasse 1 | freistehend, oberstes Aufenthaltsgeschoss ≤ 7 m über Gelände, ≤ 2 Nutzungseinheiten, zusammen ≤ 400 m² |
| Art. 45 | Fensterfläche ≥ 1/8 der Netto-Grundfläche. Mindestraumhöhe gilt nicht für Wohngebäude GK 1/2 |
| Art. 57 | verfahrensfrei u. a. Garagen ≤ 50 m², Terrassenüberdachungen ≤ 30 m² |
| Art. 58 | Genehmigungsfreistellung im qualifizierten B-Plan; Baubeginn 1 Monat nach Vorlage |
| Stellplätze (seit 01.10.2025) | Pflicht nur mit Gemeindesatzung; GaStellV nennt **Höchstwerte** (2 je Wohnung) |
| Holzbau | HolzBauRL 2024-09 in BayTB 11/2025 eingeführt; für GK 1/2 in der Regel nicht relevant |

- **Novellen seit 2025:** vier Modernisierungsgesetze und Art. 82c zum „Bauturbo“ (01.01.2026). Den Inhalt der Änderung vom 23.04.2026 habe ich nicht geprüft [U].

## 4. IDS und Merkmale

| Quelle | Inhalt | Lizenz | Urteil |
|---|---|---|---|
| **BIM-Portal des Bundes** https://via.bund.de/bim [V] | Katalog BIM.GOV mit MBO-Merkmalen LP4, IDS-Export, REST-API | **DL-DE-Zero-2.0** | übernehmen |
| buildingSMART Deutschland [U] | IDS QTo-Mengenermittlung, bSDD-Namespace `buildingsmart-de` | unklar, Registrierung nötig | prüfen |
| dataholz.eu [V] | IDS zu Holzbauaufbauten, synchron mit bSDD | Nutzungsbedingungen | adaptieren |
| BIMwood (TUM) [V] | Holzbau-Merkmallisten als PDF | – | adaptieren |

- **Nicht vorhanden:** eine fertige Holzbau-IDS, sowie IDS für GModG/GEG und Brandschutz [V]. Die Fachgruppen von bSD arbeiten daran. **Selbst bauen.**

## 5. Normen: aktueller Stand und Kernwerte

| Norm | Stand | Kernwert / Hinweis |
|---|---|---|
| DIN 18065 | 2020-08 [V] | Wohngebäude ≤ 2 WE: Laufbreite ≥ 80 cm, Steigung 14–20 cm, Auftritt 23–37 cm, 2s + a = 59–65 cm. Für GK 1/2 bzw. innerhalb von Wohnungen nicht bauaufsichtlich eingeführt |
| DIN 18011 | 1967, **zurückgezogen** [U] | nur als Heuristik: 65–70 cm zwischen Stellflächen, Flur 90 cm, Diele 130 cm |
| DIN 18040-2 | 2011-09, Entwurf 2023-02 [V/U] | barrierefreies Wohnen |
| DIN 68800-2 | 2022-02 [V] | Einbaufeuchte GK 0–3.1 **≤ 20 %** |
| DIN 4109-33 | 2016-07, Entwurf 2026-09 [V] | Schall-Bauteilkatalog Holzbau |
| DIN 4102-4 | 2016-05 [U] | Brandschutztabellen |
| DIN 1946-6 | 2019-12 + Beiblatt 2025-06 [V] | Lüftungskonzept, Feuchteschutzlüftung nutzerunabhängig |
| DIN 4108-2 | **2026-05 (neu)** [V] | Mindestwärmeschutz, sommerlicher Wärmeschutz |
| DIN EN 1995-1-1 | **2026-09 erschienen** [V] | eingeführt ist noch 2010-12 + A2:2014 (BayTB 11/2025); Rücknahme der alten Fassung bis etwa 03/2028 |
| DIN 5034-1 | 2021-08 [V] | Tageslichtquotient ≥ 0,9 % Mittel / ≥ 0,75 % ungünstigster Punkt; die 1/8-Regel ist notwendig, aber nicht hinreichend |

## 6. Regeln des Handwerks

- **Fachregeln Zimmererhandwerk:** Es gibt nur 01 Außenwandbekleidungen (03/2023) und 02 Balkone/Terrassen (12/2020). Eine „03“ existiert nicht [V]. Beide sind kostenpflichtig.
- **ZVDH Dachziegel/Dachsteine 04/2024** [V]:
  - Regeldachneigung 22–40° je nach Deckung, Mindestneigung 10°.
  - Unterschreitung der Regeldachneigung verlangt Zusatzmaßnahmen in 5 Klassen.
  - Erhöhte Anforderungen z. B. bei Sparrenlänge > 10 m, Schneelast ≥ 1,5 kN/m², Windzone 4.
  - Die Tabelle adaptieren, Lizenz des ZVDH beachten.
- **RAL-GZ 422 „Holzhausbau“** [V]: Holzfeuchte ≤ 18 %, technisch getrocknet, Holzwerkstoffe < 0,03 ppm Formaldehyd. GuP 2016: https://www.ghad.de/fileadmin/sites/ghad/Informationen_rechte_Seite/2016-03_GuP_RAL-GZ_422_Holzhausbau.pdf
- **QDF-Satzung:** 36 Qualitätsversprechen, Hausakte ist Pflicht [V].

## 7. Lizenz und Recht

- **EuGH C-588/21 P (05.03.2024)** [V]:
  - Harmonisierte Normen sind Teil des Unionsrechts. Deshalb besteht ein Anspruch auf **Zugang**.
  - Über das Urheberrecht hat der Gerichtshof nicht entschieden.
  - Die hier relevanten DIN-Normen sind national, nicht harmonisiert [U].
- **§ 5 Abs. 3 UrhG:** DIN-Normen bleiben geschützt, auch wenn Gesetze auf sie verweisen [V].
- **Empfehlung:**
  - Nur Kennwerte mit Normverweis implementieren.
  - Keine Texte oder Tabellen kopieren.
  - Für kommerzielle Nutzung eine Lizenz bei DIN Media anfragen.
  - Die Fragen rechtlich prüfen lassen [U].

## Korrekturen am Konzept

1. „18 % Holzfeuchte nach DIN 68800-2“ ist falsch. DIN 68800-2 nennt 20 %, die 18 % stammen aus RAL-GZ 422.
2. „GEG“ → **GModG** seit 29.07.2026 (BGBl. 2026 I Nr. 226). Die 65-%-EE-Pflicht entfällt. EPBD-Themen wie Ökobilanz und Nullemissionsgebäude ab 2030 kommen später.
3. DIN 4108-2 gilt jetzt in der Ausgabe 2026-05.
4. EC 5: Die neue Generation ist als DIN EN 1995-1-1:2026-09 erschienen, aber noch nicht eingeführt.
5. Stellplätze: Die GaStellV-Werte sind Höchstwerte; eine Pflicht entsteht nur durch eine Satzung.
6. Vollgeschoss: Die Definition kommt über Art. 83 Abs. 6 aus der BayBO-Fassung 2007.
7. B-Pläne Bayern: GRZ, GFZ und Dachneigung sind nicht automatisch abrufbar.
8. Flurstücke: in Bayern kein Open Data.
9. Fachregel 03 des Zimmererhandwerks existiert nicht.

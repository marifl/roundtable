# Recherche 04: Regnauer, Branchenstandards, Kataloge, Kosten

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft, **[U]** = unsicher.

## Ergebnis in 5 Punkten

1. **Regnauer veröffentlicht Startwerte:** 11 Bestseller mit Wohnfläche und Ab-Preis, dazu Wand-, Dach- und Deckenaufbauten mit U-Werten. Grundrisse gibt es nur als Bild.
2. **Die Werkssoftware ist nicht öffentlich.** Ein Indiz spricht für SEMA oder Dietrich's. Das muss Regnauer bestätigen.
3. **dataholz.eu und lignumdata.ch liefern IFC, IDS, bSDD bzw. eine API.** Sie sind die besten maschinenlesbaren Bauteilquellen.
4. **Kosten:** Der Destatis-Preisindex für Fertighäuser ist frei. BKI und STLB-Bau kosten Lizenz.
5. **Regnauers Konfigurator** ist ein Formular ohne 3D und Preis. Baufritz und Hanse Haus sind deutlich weiter. Das ist die Chance.

## 1. Regnauer

### Hauskatalog [V]
- Quellen: https://www.regnauer.de/hausbau/vitalhaus/bestseller und /haeusergalerie
- **11 Bestseller:**
  - Einfamilienhäuser: BS01 106 m², ab 377.646 € bis BS10 176 m², ab 552.874 €
  - Doppelhaushälften: BS04 140 m², BS11 146 m²
  - Bungalow: BS07 121 m², ab 452.689 €
- Galerie: rund 80 Häuser mit den Filtern Haustyp, Stil und Wohnfläche. Musterhäuser in Seebruck, Fellbach und Poing.
- Dachneigung und Geschosszahl stehen nur auf fertighaus-finder.de [U].

### Aufbauten [V]
Quellen: https://www.regnauer.de/hausbau/vitalhaus und die Bau- und Ausstattungsbeschreibung 10/2024: https://cms20683.livestep.de/hausbau/downloads/Regnauer_Bauleistungs-Ausstattungsbeschreibung_1024.pdf

| Bauteil | Aufbau (öffentlich) | Kennwerte |
|---|---|---|
| Vitalwand | Massivholz-Riegel, Holzfaserdämmung, 345(–381) mm, innen 25 mm Gips, Vlies-Dampfbremse, spanplattenfrei, ohne chemischen Holzschutz | U 0,128–0,153 W/m²K; „bis F 60 B“ |
| Passivhauswand | 240 mm Riegel | U 0,12 |
| Thermo-Vitaldach | Pfettendach, 280 mm Holzfaser, 16 mm Holzfaser-Unterdach; „Plus“ 330 mm | U 0,148 / 0,129 |
| Flachdach | – | U 0,117 |
| Silence-Decke | 240 mm Balken, 60 mm Jute, 30 mm entkoppelte Schalung, 25 mm Gipsfeuerschutz, Zementestrich | L'n,w 49 dB am Bau; „Deep Silence“ < 46 dB |
| Fenster KlimaPlus | Holz-Alu, eigene Fertigung | Ug 0,5 |

- **Widerspruch:** Die Riegelstärke der Vitalwand ist mal mit 200 mm, mal mit 300 mm angegeben.
- **Standard:** Effizienzhaus 40, Lüftung mit Wärmerückgewinnung (Proxon), QNG mit Energiepaket.
- **Siegel:** QDF, RAL (seit 1967), IBR, Sentinel Haus, PEFC.

### Werk und Software [U]
- Keine öffentliche Quelle nennt die Software.
- Indiz: ein anonymes Inserat eines Büros „am Chiemsee“ verlangt „SEMA, Dietrich's o. ä.“ (https://www.houseofconsultants.de/de/job.php?id=3052).
- Gesichert ist nur das CRM: CAS genesisWorld [V].

### Konfigurator [V]
- https://www.regnauer.de/hausbau/konfigurator: Wunschzettel mit Bildern und Formular.
- Kein 3D, kein Preis, keine Grundrissänderung.

## 2. Branchenstandards

- **RAL-GZ 422 „Holzhausbau“** [V]: https://www.ral.de/guetezeichen-von-a-z/guetezeichen-uebersicht/gz-422/
  - Träger: GDF, BMF, GHAD.
  - Überwachung zweimal jährlich im Werk, einmal jährlich auf der Baustelle.
  - Die Güte- und Prüfbestimmungen (2016) sind öffentlich.
- **QDF/BDF** [V]: https://www.fertigbau.de/qdf/ mit 36 Qualitätsversprechen. Die Richtlinien sind frei, z. B. C01 Bäder und Raumluft.
- **Baubeschreibung** [V]:
  - § 650j BGB mit Art. 249 § 2 EGBGB: 9 Pflichtpunkte plus Fertigstellungstermin.
  - Gliederung nach dem BSB-Leitfaden: https://www.bsb-ev.de/fileadmin/user_upload/1_Startseite/Leitfaden_Baubeschreibung_Webversion.pdf
- **Zulassungen** [V]:
  - Eine allgemein zugelassene Referenzwand gibt es nicht. Der Nachweis läuft über DIN 4102-4 Kap. 10 und die HolzBauRL.
  - Herstellernachweise, zum Beispiel:
    - GUTEX abP P-SAC-02/III-740 (bis REI 90)
    - STEICO Z-9.1-826 (Aussteifung)

## 3. Bauteilkataloge mit Kennwerten

| Quelle | Kennwerte | Maschinenlesbar | Urteil |
|---|---|---|---|
| **dataholz.eu** [V] | REI, U, Rw/Ln,w, Masse, ÖI3; 141 Außenwände | **IFC, IDS, bSDD**; PDF-Nachweise für DE nach Login | übernehmen |
| **lignumdata.ch** [V] | Brand, Schall | **API** (`/api/schema/getBauteil`) + IFC | übernehmen, Schweizer Normen für DE adaptieren |
| Informationsdienst Holz [V] | holzbau handbuch, Schallschutz-Katalog | PDF | adaptieren |
| DIN 4109-33 [V] | normativer Schallkatalog Holzbau | lizenzpflichtig | Lizenz |
| GUTEX, STEICO, Rigips [V] | Konstruktionskataloge (U, REI, Rw) | PDF und Web-Rechner | adaptieren |
| ubakus [V] | U-Wert, Feuchte | keine API, gewerbliche Nutzung kostenpflichtig | nur als Werkzeug |

## 4. Möbel und Ausstattung

- **BIMobject** [V]: IFC kostenlos, auch IKEA. Die Qualität schwankt, oft mit falscher Klasse.
- **Sanitär** [V]: Villeroy & Boch mit BIM-Bibliothek; Duravit nur .rfa; Geberit nur als Revit-Plug-in.
- **Bonsai** [V]: keine Möbelbibliothek. Das Addon „bonsai-ifc-product-library“ (MIT/CC BY) liefert nur Struktur.
- **DIN 18011** ist zurückgezogen [U]. Die Maße müssen wir selbst tabellieren, z. B. 70 cm Abstand, Flur 90 cm, Diele 130 cm, Bett 100×205 cm.
- **Barrierefreiheit:** DIN 18040-2 (lizenzpflichtig).

## 5. Kosten

| Quelle | Frei? | Nutzen |
|---|---|---|
| **Destatis GENESIS 61261** [V] | **frei**, API/Excel | Preisindex Einfamilienfertighäuser (61261-0015/-0016); Zimmer- und Holzbauarbeiten 2025 = 122,4 (2021 = 100). Übernehmen zur Fortschreibung |
| BKI Baukosten 2025 [V] | lizenzpflichtig | €/m² BGF nach DIN 276 für EFH Holzbau |
| STLB-Bau LB 016 [V] | lizenzpflichtig, GAEB-XML | Leistungstexte Zimmer- und Holzbau |
| Regnauer-Preise [V] | nur „ab“-Preise | Leistungsumfang unklar [U] |

## 6. Benchmark: Konfiguratoren anderer Hersteller [V]

| Hersteller | Stand |
|---|---|
| **Baufritz** „my smart green home“ | modulare Zonen, 94.000 Varianten, algorithmische Prüfung der Baubarkeit, sofortiger Preis. **Kommt uns am nächsten** |
| Hanse Haus | Live-Preis, Grundrissvarianten, QNG-Paket |
| Haas | freie Planung, 3D, AR auf dem Grundstück |
| WeberHaus | 3D-Designer, aktuell nur für das Minihaus OPTION |
| Bien-Zenker | Hausfinder + KI-Berater „CASAI“ |
| Regnauer | Formular ohne 3D und Preis |

## Fragen an Regnauer

1. Vitalwand: Riegelstärke 200 oder 300 mm? Vollständiger Schichtaufbau? Gibt es eine Installationsebene?
2. Alle Varianten von Wand, Dach und Decke mit U, Rw, REI, Masse, sd-Wert und den Nachweisen (abP/aBG/Prüfberichte).
3. Silence-Decke: Labor- und Baustellenwerte, maximale Spannweiten, Raster.
4. Werk: welches CAD/CAM (SEMA? Dietrich's?), welche Maschinen (Weinmann? Hundegger?), welche Formate (BTL/BTLx, WUP, IFC)?
5. Fertigungsregeln: maximale Elementmaße und -gewichte, Transport, Achsraster, Öffnungsregeln, Mindestmaße für Kniestock, Dachneigung und Gauben.
6. Bestseller als DWG oder IFC: Was ist im Ab-Preis enthalten? Gibt es eine Preislogik je Option?
7. Bemusterungskatalog (Sanitär, Böden, Türen) als Datenliste.
8. Nutzungsrechte an Bildern, Grundrissen und der BLB für unsere Wissensbasis.
9. Gewerbebau: Gibt es ein Rastersystem oder Standardmodule?

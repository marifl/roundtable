# B17 – Grundstücksentwässerung: Ergebnisse (Beispielrechnung, keine Bemessung im Rechtssinn)

## Szenario `bodenplatte` – EFH auf Bodenplatte (Regnauer-Standardfall angenommen), Gelände 2 % zur Straße

### Schmutzwasser-Haltungen

| von | nach | Lage | DN | L [m] | Gefälle [%] | min [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] | Kreuzung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FL1 | SW-W2 | Gebäude | 125 | 3.27 | 5.00 | 0.50 | 519.102 | 518.938 | 2.00 | 8.70 | – |
| FL2 | SW-W1 | Gebäude | 100 | 2.00 | 5.00 | 0.50 | 519.195 | 519.095 | 0.85 | 5.63 | – |
| SW-W1 | SW-S1 | Erdreich | 150 | 1.05 | 0.67 | 0.67 | 519.095 | 519.088 | 0.85 | 10.45 | – |
| SW-S1 | SW-S2 | Erdreich | 150 | 10.55 | 1.98 | 0.67 | 519.088 | 518.879 | 0.85 | 18.12 | – |
| SW-S2 | SW-S3 | Erdreich | 150 | 7.00 | 0.93 | 0.67 | 518.879 | 518.814 | 0.85 | 12.35 | HA Wasser/Strom/Telekom |
| SW-W2 | SW-S3 | Erdreich | 150 | 6.13 | 2.03 | 0.67 | 518.938 | 518.814 | 2.00 | 18.35 | – |
| SW-S3 | SW-RS | Erdreich | 150 | 3.64 | 0.93 | 0.67 | 518.814 | 518.780 | 2.00 | 12.36 | – |
| SW-RS | Kanal-Einlass | Anschlusskanal | 150 | 4.60 | 43.04 | 0.67 | 518.780 | 516.800 | – | 84.95 | – |

### Schächte und Reinigungsöffnungen

| Id | Bauwerk | Art | x | y | Deckel | Sohle | Tiefe | DN | Grund |
|---|---|---|---|---|---|---|---|---|---|
| FL1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 7.00 | 12.00 | 520.21 | 519.10 | 1.10 | – | Fuß der Fallleitung |
| FL2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 13.00 | 18.50 | 520.30 | 519.20 | 1.11 | – | Fuß der Fallleitung |
| SW-S1 | Schacht | Inspektionsöffnung | 16.05 | 18.50 | 520.29 | 519.09 | 1.20 | 600 | Richtungsänderung 90° > 45° |
| SW-S2 | Schacht | Inspektionsöffnung | 16.05 | 7.95 | 520.08 | 518.88 | 1.20 | 600 | Richtungsänderung 49° > 45° |
| SW-S3 | Schacht | Inspektionsöffnung | 10.75 | 3.38 | 520.01 | 518.81 | 1.20 | 600 | Zusammenführung |
| SW-RS | Revisionsschacht | Revisionsschacht (Übergabeschacht) | 8.00 | 1.00 | 519.98 | 518.78 | 1.20 | 1000 | Ende der Grundstücksentwässerungsanlage (EWS § 8 Abs. 4) |
| HA1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 10.00 | 24.30 | 520.44 | 519.22 | 1.21 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 9.40 | 520.16 | 519.37 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 20.60 | 520.39 | 519.17 | 1.22 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF3 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 9.40 | 520.11 | 519.31 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF4 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 20.60 | 520.34 | 519.23 | 1.10 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| NW-S1 | Schacht | Inspektionsöffnung | 15.96 | 20.39 | 520.33 | 519.20 | 1.13 | 400 | Zusammenführung |
| NW-S2 | Schacht | Inspektionsöffnung | 16.05 | 22.05 | 520.36 | 519.18 | 1.18 | 400 | Richtungsänderung 90° > 45° |
| NW-S3 | Schacht | Inspektionsöffnung | 10.06 | 22.31 | 520.40 | 519.12 | 1.27 | 600 | Zusammenführung |
| NW-S4 | Schacht | Inspektionsöffnung | 4.56 | 22.55 | 520.43 | 519.07 | 1.36 | 600 | Zusammenführung |
| NW-FS | Filterschacht | Filterschacht (Vorreinigung) | 3.40 | 22.60 | 520.43 | 519.06 | 1.38 | 600 | Vorreinigung vor der Rigole (NWFreiV § 3 Abs. 2) |

### Niederschlagswasser-Haltungen

| von | nach | DN | L [m] | Gefälle [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] |
|---|---|---|---|---|---|---|---|---|
| HA1 | NW-S3 | 100 | 1.99 | 5.00 | 519.224 | 519.124 | 0.63 | 9.43 |
| RF1 | NW-B1 | 100 | 2.99 | 1.00 | 519.365 | 519.335 | 1.04 | 4.18 |
| NW-B1 | NW-B2 | 100 | 10.10 | 2.25 | 519.335 | 519.107 | 1.04 | 6.31 |
| NW-B2 | NW-FS | 100 | 0.99 | 5.00 | 519.107 | 519.058 | 1.04 | 9.43 |
| RF2 | NW-S4 | 100 | 1.95 | 5.00 | 519.167 | 519.069 | 1.04 | 9.43 |
| RF3 | NW-S1 | 100 | 11.00 | 1.00 | 519.311 | 519.201 | 1.04 | 4.18 |
| RF4 | NW-S1 | 100 | 0.60 | 5.00 | 519.231 | 519.201 | 1.04 | 9.43 |
| NW-S1 | NW-S2 | 100 | 1.67 | 1.00 | 519.201 | 519.184 | 2.07 | 4.18 |
| NW-S2 | NW-S3 | 100 | 6.00 | 1.00 | 519.184 | 519.124 | 2.07 | 4.18 |
| NW-S3 | NW-S4 | 100 | 5.50 | 1.00 | 519.124 | 519.069 | 2.70 | 4.18 |
| NW-S4 | NW-FS | 100 | 1.16 | 1.00 | 519.069 | 519.058 | 3.74 | 4.18 |

### Rigole (DWA-A 138-1, einfaches Verfahren)

A_E,b = 167.0 m², A_C = 131.2 m² (C_m), k_i = 7.20e-06 m/s; 1 Reihe(n), b = 0.80 m, h = 0.66 m, L_erf = 9.29 m → L = 9.60 m (12 Elemente), D_maßg = 240 min; A_S,m = 14.54 m², Q_S = 0.105 l/s, V_erf = 4.61 m³ ≤ V_vorh = 4.82 m³; Entleerung 12.2 h; OK 519.01, Sohle 518.35, Sickerraum 3.35 m; Abstand Gebäude 1.20 m (erf. 1.20 m). Vergleich Mulde: A_S ≥ 17.1 m² (passt).

### Regelprüfung

| Id | Status | Regel | Quelle | Befund |
|---|---|---|---|---|
| SW-01 | erfüllt | Revisionsschacht am Ende der Anlage auf eigenem Grund | EWS § 8 Abs. 4 [V] | Revisionsschacht DN 1000 bei (8.00; 1.00), Außenkante 0.40 m innerhalb der Grenze |
| SW-02 | erfüllt | Außenliegender Revisionsschacht nur bei >= 5 m zwischen Grenze und Gebäudekante | MSE-Leitfaden 2.6 [V] | Abstand Straßengrenze-Gebäude 9.00 m |
| SW-03 | erfüllt | Frostfreie Tiefe 1,20 m (GOK bis Rohrsohle) für erdverlegte SW-Leitungen | MSE-Leitfaden 2.7, EWS § 8 Abs. 3 [V] | alle Knoten >= 1,20 m |
| SW-04 | erfüllt | Mindestgefälle Grundleitungen (0,5 % im Gebäude, 1:DN außerhalb) | DIN 1986-100 [V] | eingehalten |
| SW-05 | erfüllt | Höchstgefälle 1:20 (sonst Absturzbauwerk) | kommunale Merkblätter [U] | eingehalten |
| SW-06 | erfüllt | Anschlusskanal geradlinig, ohne Gefällewechsel, Gefälle 1:DN bis 1:1 | MSE-Leitfaden 2.6 [V] | L = 4.60 m, Gefälle 43.0 % (zulässig 0.67-100 %) |
| SW-07 | erfüllt | Nennweite in Fließrichtung nicht verringern | DIN 1986-100 6.1.8 [V] | eingehalten |
| SW-08 | erfüllt | Hydraulische Leistungsfähigkeit (Q_ww <= Q bei h/d 0,5 innen / 0,7 außen) | DIN 1986-100 14.1.5 [V/U] | max. Auslastung 0.23 |
| SW-09 | erfüllt | Reinigungsöffnungen an Fallleitungsfüßen, Zusammenführungen, Richtungsänderungen > 45°, Abstand <= 20/40 m | DIN 1986-100 6.6 [U] | 3 Schacht/Schächte außen, 2 Reinigungsöffnung(en), Revisionsschacht DN 1000 |
| SW-10 | erfüllt | Ablaufstellen unter der Rückstauebene gegen Rückstau sichern | EWS § 8 Abs. 6, MSE-Leitfaden 2.2 [V] | alle Ablaufstellen über RSE 519.95 m (FFB EG 520.55); keine Rückstausicherung nötig |
| SW-11 | erfüllt | Geschützte Gehölze <= 5 m zur Leitungsachse im Plan 1:100 darstellen, ggf. Stellungnahme Baumschutz | MSE-Genehmigungsantrag Ziff. 3, MSE-Leitfaden 3.2 [V] | keine geschützten Gehölze im 5-m-Bereich |
| SW-12 | Hinweis | Kreuzungen mit Versorgungsleitungen im Plan eintragen, Abstände mit Netzbetreiber klären | MSE-Leitfaden 3.2 (Sparten im Bereich von SW-Leitungen) [V], Abstandswerte [U] | SW-S2-SW-S3 x HA Wasser/Strom/Telekom |
| SW-13 | Hinweis | Grundleitungen innerhalb von Gebäuden vermeiden; in der Bodenplatte genehmigungspflichtig | DIN 1986-100 6.1.1, MSE-Leitfaden 2.1 [V] | 5.27 m Leitung im/unter dem Gebäude (Grundleitung unter Bodenplatte) |
| NW-01 | erfüllt | Durchlässigkeit im Bereich 1e-6 bis 1e-3 m/s | DWA-A 138-1, MSE-Leitfaden 3.2 [V] | k_f = 1.0e-05 m/s, k_i = 7.20e-06 m/s (f_k = 0.72) |
| NW-02 | erfüllt | Sickerraum >= 1 m (Sohle bis MHGW) | TRENGW Nr. 6, DWA-A 138-1 [V] | Sohle 518.35, MHGW 515.00 -> 3.35 m |
| NW-03 | erfüllt | Sohle der Versickerungsanlage <= 5 m unter GOK | TRENGW Nr. 6 [V] | 1.97 m |
| NW-04 | erfüllt | Angeschlossene befestigte Fläche je Anlage <= 1000 m² | NWFreiV § 3 Abs. 1 [V] | A_E,b = 167.0 m² |
| NW-05 | Hinweis | Rigole nur, wenn flächenhafte Versickerung (Mulde) nicht möglich ist | NWFreiV § 3 Abs. 2, TRENGW Nr. 4 [V] | Mulde mit A_S >= 17.1 m² (hydraulisch 17.1 m², TRENGW 1/15: 11.1 m²) passt auf das Grundstück -> Rigole begründen oder Mulde wählen |
| NW-06 | Hinweis | Vorreinigung vor unterirdischer Versickerung | TRENGW Tab. 2 [V]; DWA-A 138-1 Tab. 7 [U] | Dach: Laubfangkörbe/Grobstoffrückhalt; Terrasse: Hofablauf mit Schlammeimer; Filterschacht NW-FS vor der Rigole. Nach DWA-A 138-1 sind auch Dachabflüsse zu behandeln (Gesamtwirkungsgrad je Flächenkategorie) – Produkt mit Nachweis wählen |
| NW-07 | erfüllt | Unbeschichtete Cu/Zn/Pb-Flächen > 50 m² nur über zugelassenen Filter | NWFreiV § 3 Abs. 2 [V] | keine |
| NW-08 | erfüllt | Abstand Versickerungsanlage-Gebäude >= 1,5 x Baugruben-/Fundamenttiefe | DWA-A 138-1 5.3.2 [V (Sekundärquelle)] | vorhanden 1.20 m, erforderlich 1.20 m (Fundamenttiefe 0.80 m) |
| NW-09 | erfüllt | Abstand zur Grundstücksgrenze >= 2 m | kommunale Leitfäden [U] | 3.00 m |
| NW-10 | erfüllt | Kein Überlauf der Versickerungsanlage an den städtischen Kanal | MSE-Leitfaden 5.2 [V] | kein Notüberlauf zum Kanal vorgesehen |
| NW-11 | erfüllt | Überflutungsnachweis bei A_C > 800 m² | DIN 1986-100 14.9, DWA-A 138-1 5.3.4 [V] | A_C (C_s) = 164.6 m² -> nicht erforderlich; nach DWA-A 138-1 Überflutungsfolgen trotzdem qualitativ bewerten |
| NW-12 | erfüllt | Frosttiefe 0,80 m für NW-Leitungen zur Versickerung | MSE-Leitfaden 2.7 [V] | eingehalten |
| NW-13 | erfüllt | Erlaubnisfrei nur außerhalb von Wasserschutzgebieten und Altlastverdachtsflächen | NWFreiV § 1 [V] | laut Technischem Formblatt (hier Beispielangabe: nein/nein) |
| NW-14 | erfüllt | Niederschlagswasser nicht in den städtischen Kanal einleiten (kein Anspruch) | EWS § 4 Abs. 4, MSE-Leitfaden 2.4/5 [V] | vollständige Versickerung auf dem Grundstück |
| NW-15 | erfüllt | Speichernachweis der Rigole V_vorh >= V_erf | DWA-A 138-1 Gl. 8 [V (Sekundärquelle)] | V_vorh = 4.82 m³ >= V_erf = 4.61 m³ (D = 240 min), Entleerung 12.2 h |

Niederschlagswassergebühr pauschal 371.70 EUR/a (600 m² × 0.35 × 1,77 EUR/m²); bei Vollversickerung 0 EUR/a (Antrag EAS § 8 Abs. 5).

## Szenario `keller` – EFH mit Keller (UG-FFB 517,75 unter Rückstauebene)

### Schmutzwasser-Haltungen

| von | nach | Lage | DN | L [m] | Gefälle [%] | min [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] | Kreuzung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FL1 | SW-RÖ1 | Gebäude | 125 | 3.98 | 5.00 | 0.50 | 519.222 | 519.023 | 2.00 | 8.70 | – |
| FL2 | SW-RÖ1 | Gebäude | 100 | 8.00 | 5.00 | 0.50 | 519.423 | 519.023 | 0.85 | 5.63 | – |
| SW-RÖ1 | SW-W1 | Gebäude | 125 | 1.88 | 5.00 | 0.50 | 519.023 | 518.929 | 2.00 | 8.70 | – |
| SW-W1 | SW-RS | Erdreich | 150 | 8.32 | 1.79 | 0.67 | 518.929 | 518.780 | 2.00 | 17.19 | – |
| SW-RS | Kanal-Einlass | Anschlusskanal | 150 | 4.60 | 43.04 | 0.67 | 518.780 | 516.800 | – | 84.95 | – |

### Schächte und Reinigungsöffnungen

| Id | Bauwerk | Art | x | y | Deckel | Sohle | Tiefe | DN | Grund |
|---|---|---|---|---|---|---|---|---|---|
| FL1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 7.00 | 12.00 | 520.21 | 519.22 | 0.98 | – | Fuß der Fallleitung |
| FL2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 13.00 | 18.50 | 520.30 | 519.42 | 0.88 | – | Fuß der Fallleitung |
| SW-RÖ1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 10.80 | 10.81 | 520.16 | 519.02 | 1.14 | – | Zusammenführung (im Gebäude) |
| SW-RS | Revisionsschacht | Revisionsschacht (Übergabeschacht) | 8.00 | 1.00 | 519.98 | 518.78 | 1.20 | 1000 | Ende der Grundstücksentwässerungsanlage (EWS § 8 Abs. 4) |
| HA1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 10.00 | 24.30 | 520.44 | 519.18 | 1.25 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 9.40 | 520.16 | 519.37 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 20.60 | 520.39 | 519.28 | 1.10 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| NW-S1 | Schacht | Inspektionsöffnung | 4.04 | 20.39 | 520.39 | 519.25 | 1.13 | 400 | Zusammenführung |
| NW-S2 | Schacht | Inspektionsöffnung | 3.95 | 22.05 | 520.42 | 519.24 | 1.18 | 400 | Richtungsänderung 74° > 45° |
| NW-S3 | Schacht | Inspektionsöffnung | 10.11 | 24.14 | 520.43 | 519.17 | 1.26 | 600 | Zusammenführung |
| RF3 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 9.40 | 520.11 | 519.31 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF4 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 20.60 | 520.34 | 519.22 | 1.11 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| NW-S4 | Schacht | Inspektionsöffnung | 15.02 | 20.39 | 520.33 | 519.20 | 1.13 | 400 | Zusammenführung |
| NW-S5 | Schacht | Inspektionsöffnung | 14.84 | 25.75 | 520.44 | 519.12 | 1.32 | 600 | Zusammenführung |
| NW-FS | Filterschacht | Filterschacht (Vorreinigung) | 15.60 | 26.40 | 520.45 | 519.12 | 1.33 | 600 | Vorreinigung vor der Rigole (NWFreiV § 3 Abs. 2) |

### Niederschlagswasser-Haltungen

| von | nach | DN | L [m] | Gefälle [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] |
|---|---|---|---|---|---|---|---|---|
| HA1 | NW-S3 | 100 | 0.19 | 5.00 | 519.183 | 519.173 | 0.63 | 9.43 |
| RF1 | NW-S1 | 100 | 11.00 | 1.00 | 519.365 | 519.255 | 1.04 | 4.18 |
| RF2 | NW-S1 | 100 | 0.60 | 5.00 | 519.285 | 519.255 | 1.04 | 9.43 |
| NW-S1 | NW-S2 | 100 | 1.67 | 1.00 | 519.255 | 519.238 | 2.07 | 4.18 |
| NW-S2 | NW-S3 | 100 | 6.50 | 1.00 | 519.238 | 519.173 | 2.07 | 4.18 |
| NW-S3 | NW-S5 | 100 | 5.00 | 1.00 | 519.173 | 519.123 | 2.70 | 4.18 |
| RF3 | NW-S4 | 100 | 11.00 | 1.00 | 519.311 | 519.201 | 1.04 | 4.18 |
| RF4 | NW-S4 | 100 | 0.43 | 5.00 | 519.222 | 519.201 | 1.04 | 9.43 |
| NW-S4 | NW-S5 | 100 | 5.36 | 1.45 | 519.201 | 519.123 | 2.07 | 5.05 |
| NW-S5 | NW-B1 | 125 | 0.01 | 0.80 | 519.123 | 519.123 | 4.77 | 5.78 |
| NW-B1 | NW-FS | 125 | 0.99 | 0.80 | 519.123 | 519.115 | 4.77 | 5.78 |

### Rigole (DWA-A 138-1, einfaches Verfahren)

A_E,b = 167.0 m², A_C = 131.2 m² (C_m), k_i = 7.20e-06 m/s; 1 Reihe(n), b = 0.80 m, h = 0.66 m, L_erf = 9.29 m → L = 9.60 m (12 Elemente), D_maßg = 240 min; A_S,m = 14.54 m², Q_S = 0.105 l/s, V_erf = 4.61 m³ ≤ V_vorh = 4.82 m³; Entleerung 12.2 h; OK 519.07, Sohle 518.40, Sickerraum 3.40 m; Abstand Gebäude 5.00 m (erf. 4.95 m). Vergleich Mulde: A_S ≥ 17.1 m² (passt nicht).

### Regelprüfung

| Id | Status | Regel | Quelle | Befund |
|---|---|---|---|---|
| SW-01 | erfüllt | Revisionsschacht am Ende der Anlage auf eigenem Grund | EWS § 8 Abs. 4 [V] | Revisionsschacht DN 1000 bei (8.00; 1.00), Außenkante 0.40 m innerhalb der Grenze |
| SW-02 | erfüllt | Außenliegender Revisionsschacht nur bei >= 5 m zwischen Grenze und Gebäudekante | MSE-Leitfaden 2.6 [V] | Abstand Straßengrenze-Gebäude 9.00 m |
| SW-03 | erfüllt | Frostfreie Tiefe 1,20 m (GOK bis Rohrsohle) für erdverlegte SW-Leitungen | MSE-Leitfaden 2.7, EWS § 8 Abs. 3 [V] | alle Knoten >= 1,20 m |
| SW-04 | erfüllt | Mindestgefälle Grundleitungen (0,5 % im Gebäude, 1:DN außerhalb) | DIN 1986-100 [V] | eingehalten |
| SW-05 | erfüllt | Höchstgefälle 1:20 (sonst Absturzbauwerk) | kommunale Merkblätter [U] | eingehalten |
| SW-06 | erfüllt | Anschlusskanal geradlinig, ohne Gefällewechsel, Gefälle 1:DN bis 1:1 | MSE-Leitfaden 2.6 [V] | L = 4.60 m, Gefälle 43.0 % (zulässig 0.67-100 %) |
| SW-07 | erfüllt | Nennweite in Fließrichtung nicht verringern | DIN 1986-100 6.1.8 [V] | eingehalten |
| SW-08 | erfüllt | Hydraulische Leistungsfähigkeit (Q_ww <= Q bei h/d 0,5 innen / 0,7 außen) | DIN 1986-100 14.1.5 [V/U] | max. Auslastung 0.23 |
| SW-09 | erfüllt | Reinigungsöffnungen an Fallleitungsfüßen, Zusammenführungen, Richtungsänderungen > 45°, Abstand <= 20/40 m | DIN 1986-100 6.6 [U] | 0 Schacht/Schächte außen, 3 Reinigungsöffnung(en), Revisionsschacht DN 1000 |
| SW-10 | Auflage | Ablaufstellen unter der Rückstauebene gegen Rückstau sichern | EWS § 8 Abs. 6, MSE-Leitfaden 2.2/2.3, DIN EN 12056-4, DIN 1986-100 Abschn. 13 [V] | Rückstauebene 519.95 m (Straßenoberkante). Unter RSE: UG (FFB 517.75): UG-Dusche, UG-Waschmaschine, UG-Bodenablauf DN 70. Abwasserhebeanlage DIN EN 12050-2 (fäkalienfrei) mit Rückstauschleife über RSE; Rückstauverschluss (DIN EN 13564) nur bei Gefälle zum Kanal (ja), Räumen untergeordneter Nutzung, kleinem Benutzerkreis und WC über RSE (MSE-Merkblatt Kellerüberflutung) |
| SW-11 | erfüllt | Geschützte Gehölze <= 5 m zur Leitungsachse im Plan 1:100 darstellen, ggf. Stellungnahme Baumschutz | MSE-Genehmigungsantrag Ziff. 3, MSE-Leitfaden 3.2 [V] | keine geschützten Gehölze im 5-m-Bereich |
| SW-12 | erfüllt | Kreuzungen mit Versorgungsleitungen im Plan eintragen, Abstände mit Netzbetreiber klären | MSE-Leitfaden 3.2 (Sparten im Bereich von SW-Leitungen) [V], Abstandswerte [U] | keine Kreuzung |
| SW-13 | Hinweis | Grundleitungen innerhalb von Gebäuden vermeiden; in der Bodenplatte genehmigungspflichtig | DIN 1986-100 6.1.1, MSE-Leitfaden 2.1 [V] | 13.86 m Leitung im/unter dem Gebäude (Sammelleitung im Keller) |
| NW-01 | erfüllt | Durchlässigkeit im Bereich 1e-6 bis 1e-3 m/s | DWA-A 138-1, MSE-Leitfaden 3.2 [V] | k_f = 1.0e-05 m/s, k_i = 7.20e-06 m/s (f_k = 0.72) |
| NW-02 | erfüllt | Sickerraum >= 1 m (Sohle bis MHGW) | TRENGW Nr. 6, DWA-A 138-1 [V] | Sohle 518.41, MHGW 515.00 -> 3.41 m |
| NW-03 | erfüllt | Sohle der Versickerungsanlage <= 5 m unter GOK | TRENGW Nr. 6 [V] | 2.07 m |
| NW-04 | erfüllt | Angeschlossene befestigte Fläche je Anlage <= 1000 m² | NWFreiV § 3 Abs. 1 [V] | A_E,b = 167.0 m² |
| NW-05 | erfüllt | Rigole nur, wenn flächenhafte Versickerung (Mulde) nicht möglich ist | NWFreiV § 3 Abs. 2, TRENGW Nr. 4 [V] | Mulde mit 17.1 m² passt nicht; Rigole zulässig |
| NW-06 | Hinweis | Vorreinigung vor unterirdischer Versickerung | TRENGW Tab. 2 [V]; DWA-A 138-1 Tab. 7 [U] | Dach: Laubfangkörbe/Grobstoffrückhalt; Terrasse: Hofablauf mit Schlammeimer; Filterschacht NW-FS vor der Rigole. Nach DWA-A 138-1 sind auch Dachabflüsse zu behandeln (Gesamtwirkungsgrad je Flächenkategorie) – Produkt mit Nachweis wählen |
| NW-07 | erfüllt | Unbeschichtete Cu/Zn/Pb-Flächen > 50 m² nur über zugelassenen Filter | NWFreiV § 3 Abs. 2 [V] | keine |
| NW-08 | erfüllt | Abstand Versickerungsanlage-Gebäude >= 1,5 x Baugruben-/Fundamenttiefe | DWA-A 138-1 5.3.2 [V (Sekundärquelle)] | vorhanden 5.00 m, erforderlich 4.95 m (Kellertiefe 2.90 m) |
| NW-09 | erfüllt | Abstand zur Grundstücksgrenze >= 2 m | kommunale Leitfäden [U] | 3.20 m |
| NW-10 | erfüllt | Kein Überlauf der Versickerungsanlage an den städtischen Kanal | MSE-Leitfaden 5.2 [V] | kein Notüberlauf zum Kanal vorgesehen |
| NW-11 | erfüllt | Überflutungsnachweis bei A_C > 800 m² | DIN 1986-100 14.9, DWA-A 138-1 5.3.4 [V] | A_C (C_s) = 164.6 m² -> nicht erforderlich; nach DWA-A 138-1 Überflutungsfolgen trotzdem qualitativ bewerten |
| NW-12 | erfüllt | Frosttiefe 0,80 m für NW-Leitungen zur Versickerung | MSE-Leitfaden 2.7 [V] | eingehalten |
| NW-13 | erfüllt | Erlaubnisfrei nur außerhalb von Wasserschutzgebieten und Altlastverdachtsflächen | NWFreiV § 1 [V] | laut Technischem Formblatt (hier Beispielangabe: nein/nein) |
| NW-14 | erfüllt | Niederschlagswasser nicht in den städtischen Kanal einleiten (kein Anspruch) | EWS § 4 Abs. 4, MSE-Leitfaden 2.4/5 [V] | vollständige Versickerung auf dem Grundstück |
| NW-15 | erfüllt | Speichernachweis der Rigole V_vorh >= V_erf | DWA-A 138-1 Gl. 8 [V (Sekundärquelle)] | V_vorh = 4.82 m³ >= V_erf = 4.61 m³ (D = 240 min), Entleerung 12.2 h |

Niederschlagswassergebühr pauschal 371.70 EUR/a (600 m² × 0.35 × 1,77 EUR/m²); bei Vollversickerung 0 EUR/a (Antrag EAS § 8 Abs. 5).

## Szenario `kanal_hoch` – flacher Straßenkanal (Einlass-Sohle 518,90)

### Schmutzwasser-Haltungen

| von | nach | Lage | DN | L [m] | Gefälle [%] | min [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] | Kreuzung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FL1 | SW-W2 | Gebäude | 125 | 3.27 | 5.00 | 0.50 | 519.102 | 518.938 | 2.00 | 8.70 | – |
| FL2 | SW-W1 | Gebäude | 100 | 2.00 | 5.00 | 0.50 | 519.195 | 519.095 | 0.85 | 5.63 | – |
| SW-W1 | SW-S1 | Erdreich | 150 | 1.05 | 0.67 | 0.67 | 519.095 | 519.088 | 0.85 | 10.45 | – |
| SW-S1 | SW-S2 | Erdreich | 150 | 10.55 | 1.98 | 0.67 | 519.088 | 518.879 | 0.85 | 18.12 | – |
| SW-S2 | SW-S3 | Erdreich | 150 | 7.00 | 0.93 | 0.67 | 518.879 | 518.814 | 0.85 | 12.35 | HA Wasser/Strom/Telekom |
| SW-W2 | SW-S3 | Erdreich | 150 | 6.13 | 2.03 | 0.67 | 518.938 | 518.814 | 2.00 | 18.35 | – |
| SW-S3 | SW-RS | Erdreich | 150 | 3.64 | 0.93 | 0.67 | 518.814 | 518.780 | 2.00 | 12.36 | – |
| SW-RS | Kanal-Einlass | Anschlusskanal | 150 | 4.60 | -2.61 | 0.67 | 518.780 | 518.900 | – | 0.09 | – |

### Schächte und Reinigungsöffnungen

| Id | Bauwerk | Art | x | y | Deckel | Sohle | Tiefe | DN | Grund |
|---|---|---|---|---|---|---|---|---|---|
| FL1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 7.00 | 12.00 | 520.21 | 519.10 | 1.10 | – | Fuß der Fallleitung |
| FL2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 13.00 | 18.50 | 520.30 | 519.20 | 1.11 | – | Fuß der Fallleitung |
| SW-S1 | Schacht | Inspektionsöffnung | 16.05 | 18.50 | 520.29 | 519.09 | 1.20 | 600 | Richtungsänderung 90° > 45° |
| SW-S2 | Schacht | Inspektionsöffnung | 16.05 | 7.95 | 520.08 | 518.88 | 1.20 | 600 | Richtungsänderung 49° > 45° |
| SW-S3 | Schacht | Inspektionsöffnung | 10.75 | 3.38 | 520.01 | 518.81 | 1.20 | 600 | Zusammenführung |
| SW-RS | Revisionsschacht | Revisionsschacht (Übergabeschacht) | 8.00 | 1.00 | 519.98 | 518.78 | 1.20 | 1000 | Ende der Grundstücksentwässerungsanlage (EWS § 8 Abs. 4) |
| HA1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 10.00 | 24.30 | 520.44 | 519.22 | 1.21 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 9.40 | 520.16 | 519.37 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 20.60 | 520.39 | 519.17 | 1.22 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF3 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 9.40 | 520.11 | 519.31 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF4 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 20.60 | 520.34 | 519.23 | 1.10 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| NW-S1 | Schacht | Inspektionsöffnung | 15.96 | 20.39 | 520.33 | 519.20 | 1.13 | 400 | Zusammenführung |
| NW-S2 | Schacht | Inspektionsöffnung | 16.05 | 22.05 | 520.36 | 519.18 | 1.18 | 400 | Richtungsänderung 90° > 45° |
| NW-S3 | Schacht | Inspektionsöffnung | 10.06 | 22.31 | 520.40 | 519.12 | 1.27 | 600 | Zusammenführung |
| NW-S4 | Schacht | Inspektionsöffnung | 4.56 | 22.55 | 520.43 | 519.07 | 1.36 | 600 | Zusammenführung |
| NW-FS | Filterschacht | Filterschacht (Vorreinigung) | 3.40 | 22.60 | 520.43 | 519.06 | 1.38 | 600 | Vorreinigung vor der Rigole (NWFreiV § 3 Abs. 2) |

### Niederschlagswasser-Haltungen

| von | nach | DN | L [m] | Gefälle [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] |
|---|---|---|---|---|---|---|---|---|
| HA1 | NW-S3 | 100 | 1.99 | 5.00 | 519.224 | 519.124 | 0.63 | 9.43 |
| RF1 | NW-B1 | 100 | 2.99 | 1.00 | 519.365 | 519.335 | 1.04 | 4.18 |
| NW-B1 | NW-B2 | 100 | 10.10 | 2.25 | 519.335 | 519.107 | 1.04 | 6.31 |
| NW-B2 | NW-FS | 100 | 0.99 | 5.00 | 519.107 | 519.058 | 1.04 | 9.43 |
| RF2 | NW-S4 | 100 | 1.95 | 5.00 | 519.167 | 519.069 | 1.04 | 9.43 |
| RF3 | NW-S1 | 100 | 11.00 | 1.00 | 519.311 | 519.201 | 1.04 | 4.18 |
| RF4 | NW-S1 | 100 | 0.60 | 5.00 | 519.231 | 519.201 | 1.04 | 9.43 |
| NW-S1 | NW-S2 | 100 | 1.67 | 1.00 | 519.201 | 519.184 | 2.07 | 4.18 |
| NW-S2 | NW-S3 | 100 | 6.00 | 1.00 | 519.184 | 519.124 | 2.07 | 4.18 |
| NW-S3 | NW-S4 | 100 | 5.50 | 1.00 | 519.124 | 519.069 | 2.70 | 4.18 |
| NW-S4 | NW-FS | 100 | 1.16 | 1.00 | 519.069 | 519.058 | 3.74 | 4.18 |

### Rigole (DWA-A 138-1, einfaches Verfahren)

A_E,b = 167.0 m², A_C = 131.2 m² (C_m), k_i = 7.20e-06 m/s; 1 Reihe(n), b = 0.80 m, h = 0.66 m, L_erf = 9.29 m → L = 9.60 m (12 Elemente), D_maßg = 240 min; A_S,m = 14.54 m², Q_S = 0.105 l/s, V_erf = 4.61 m³ ≤ V_vorh = 4.82 m³; Entleerung 12.2 h; OK 519.01, Sohle 518.35, Sickerraum 3.35 m; Abstand Gebäude 1.20 m (erf. 1.20 m). Vergleich Mulde: A_S ≥ 17.1 m² (passt).

### Regelprüfung

| Id | Status | Regel | Quelle | Befund |
|---|---|---|---|---|
| SW-01 | erfüllt | Revisionsschacht am Ende der Anlage auf eigenem Grund | EWS § 8 Abs. 4 [V] | Revisionsschacht DN 1000 bei (8.00; 1.00), Außenkante 0.40 m innerhalb der Grenze |
| SW-02 | erfüllt | Außenliegender Revisionsschacht nur bei >= 5 m zwischen Grenze und Gebäudekante | MSE-Leitfaden 2.6 [V] | Abstand Straßengrenze-Gebäude 9.00 m |
| SW-03 | erfüllt | Frostfreie Tiefe 1,20 m (GOK bis Rohrsohle) für erdverlegte SW-Leitungen | MSE-Leitfaden 2.7, EWS § 8 Abs. 3 [V] | alle Knoten >= 1,20 m |
| SW-04 | erfüllt | Mindestgefälle Grundleitungen (0,5 % im Gebäude, 1:DN außerhalb) | DIN 1986-100 [V] | eingehalten |
| SW-05 | erfüllt | Höchstgefälle 1:20 (sonst Absturzbauwerk) | kommunale Merkblätter [U] | eingehalten |
| SW-06 | Verstoß | Anschlusskanal mit Mindestgefälle im Freispiegel | EWS § 8 Abs. 5, MSE-Leitfaden 2.6 [V] | Gefälle -2.61 % < 0.67 % (Sohle RS 518.780 / Einlass 518.900): Freispiegelentwässerung nicht möglich -> Abwasserhebeanlage (DIN EN 12050-1, DIN EN 12056-4) für das Gebäude erforderlich |
| SW-07 | erfüllt | Nennweite in Fließrichtung nicht verringern | DIN 1986-100 6.1.8 [V] | eingehalten |
| SW-08 | erfüllt | Hydraulische Leistungsfähigkeit (Q_ww <= Q bei h/d 0,5 innen / 0,7 außen) | DIN 1986-100 14.1.5 [V/U] | max. Auslastung 0.23 |
| SW-09 | erfüllt | Reinigungsöffnungen an Fallleitungsfüßen, Zusammenführungen, Richtungsänderungen > 45°, Abstand <= 20/40 m | DIN 1986-100 6.6 [U] | 3 Schacht/Schächte außen, 2 Reinigungsöffnung(en), Revisionsschacht DN 1000 |
| SW-10 | erfüllt | Ablaufstellen unter der Rückstauebene gegen Rückstau sichern | EWS § 8 Abs. 6, MSE-Leitfaden 2.2 [V] | alle Ablaufstellen über RSE 519.95 m (FFB EG 520.55); keine Rückstausicherung nötig |
| SW-11 | erfüllt | Geschützte Gehölze <= 5 m zur Leitungsachse im Plan 1:100 darstellen, ggf. Stellungnahme Baumschutz | MSE-Genehmigungsantrag Ziff. 3, MSE-Leitfaden 3.2 [V] | keine geschützten Gehölze im 5-m-Bereich |
| SW-12 | Hinweis | Kreuzungen mit Versorgungsleitungen im Plan eintragen, Abstände mit Netzbetreiber klären | MSE-Leitfaden 3.2 (Sparten im Bereich von SW-Leitungen) [V], Abstandswerte [U] | SW-S2-SW-S3 x HA Wasser/Strom/Telekom |
| SW-13 | Hinweis | Grundleitungen innerhalb von Gebäuden vermeiden; in der Bodenplatte genehmigungspflichtig | DIN 1986-100 6.1.1, MSE-Leitfaden 2.1 [V] | 5.27 m Leitung im/unter dem Gebäude (Grundleitung unter Bodenplatte) |
| NW-01 | erfüllt | Durchlässigkeit im Bereich 1e-6 bis 1e-3 m/s | DWA-A 138-1, MSE-Leitfaden 3.2 [V] | k_f = 1.0e-05 m/s, k_i = 7.20e-06 m/s (f_k = 0.72) |
| NW-02 | erfüllt | Sickerraum >= 1 m (Sohle bis MHGW) | TRENGW Nr. 6, DWA-A 138-1 [V] | Sohle 518.35, MHGW 515.00 -> 3.35 m |
| NW-03 | erfüllt | Sohle der Versickerungsanlage <= 5 m unter GOK | TRENGW Nr. 6 [V] | 1.97 m |
| NW-04 | erfüllt | Angeschlossene befestigte Fläche je Anlage <= 1000 m² | NWFreiV § 3 Abs. 1 [V] | A_E,b = 167.0 m² |
| NW-05 | Hinweis | Rigole nur, wenn flächenhafte Versickerung (Mulde) nicht möglich ist | NWFreiV § 3 Abs. 2, TRENGW Nr. 4 [V] | Mulde mit A_S >= 17.1 m² (hydraulisch 17.1 m², TRENGW 1/15: 11.1 m²) passt auf das Grundstück -> Rigole begründen oder Mulde wählen |
| NW-06 | Hinweis | Vorreinigung vor unterirdischer Versickerung | TRENGW Tab. 2 [V]; DWA-A 138-1 Tab. 7 [U] | Dach: Laubfangkörbe/Grobstoffrückhalt; Terrasse: Hofablauf mit Schlammeimer; Filterschacht NW-FS vor der Rigole. Nach DWA-A 138-1 sind auch Dachabflüsse zu behandeln (Gesamtwirkungsgrad je Flächenkategorie) – Produkt mit Nachweis wählen |
| NW-07 | erfüllt | Unbeschichtete Cu/Zn/Pb-Flächen > 50 m² nur über zugelassenen Filter | NWFreiV § 3 Abs. 2 [V] | keine |
| NW-08 | erfüllt | Abstand Versickerungsanlage-Gebäude >= 1,5 x Baugruben-/Fundamenttiefe | DWA-A 138-1 5.3.2 [V (Sekundärquelle)] | vorhanden 1.20 m, erforderlich 1.20 m (Fundamenttiefe 0.80 m) |
| NW-09 | erfüllt | Abstand zur Grundstücksgrenze >= 2 m | kommunale Leitfäden [U] | 3.00 m |
| NW-10 | erfüllt | Kein Überlauf der Versickerungsanlage an den städtischen Kanal | MSE-Leitfaden 5.2 [V] | kein Notüberlauf zum Kanal vorgesehen |
| NW-11 | erfüllt | Überflutungsnachweis bei A_C > 800 m² | DIN 1986-100 14.9, DWA-A 138-1 5.3.4 [V] | A_C (C_s) = 164.6 m² -> nicht erforderlich; nach DWA-A 138-1 Überflutungsfolgen trotzdem qualitativ bewerten |
| NW-12 | erfüllt | Frosttiefe 0,80 m für NW-Leitungen zur Versickerung | MSE-Leitfaden 2.7 [V] | eingehalten |
| NW-13 | erfüllt | Erlaubnisfrei nur außerhalb von Wasserschutzgebieten und Altlastverdachtsflächen | NWFreiV § 1 [V] | laut Technischem Formblatt (hier Beispielangabe: nein/nein) |
| NW-14 | erfüllt | Niederschlagswasser nicht in den städtischen Kanal einleiten (kein Anspruch) | EWS § 4 Abs. 4, MSE-Leitfaden 2.4/5 [V] | vollständige Versickerung auf dem Grundstück |
| NW-15 | erfüllt | Speichernachweis der Rigole V_vorh >= V_erf | DWA-A 138-1 Gl. 8 [V (Sekundärquelle)] | V_vorh = 4.82 m³ >= V_erf = 4.61 m³ (D = 240 min), Entleerung 12.2 h |

Niederschlagswassergebühr pauschal 371.70 EUR/a (600 m² × 0.35 × 1,77 EUR/m²); bei Vollversickerung 0 EUR/a (Antrag EAS § 8 Abs. 5).

## Szenario `grundwasser_hoch` – hoher Grundwasserstand (MHGW 518,40)

### Schmutzwasser-Haltungen

| von | nach | Lage | DN | L [m] | Gefälle [%] | min [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] | Kreuzung |
|---|---|---|---|---|---|---|---|---|---|---|---|
| FL1 | SW-W2 | Gebäude | 125 | 3.27 | 5.00 | 0.50 | 519.102 | 518.938 | 2.00 | 8.70 | – |
| FL2 | SW-W1 | Gebäude | 100 | 2.00 | 5.00 | 0.50 | 519.195 | 519.095 | 0.85 | 5.63 | – |
| SW-W1 | SW-S1 | Erdreich | 150 | 1.05 | 0.67 | 0.67 | 519.095 | 519.088 | 0.85 | 10.45 | – |
| SW-S1 | SW-S2 | Erdreich | 150 | 10.55 | 1.98 | 0.67 | 519.088 | 518.879 | 0.85 | 18.12 | – |
| SW-S2 | SW-S3 | Erdreich | 150 | 7.00 | 0.93 | 0.67 | 518.879 | 518.814 | 0.85 | 12.35 | HA Wasser/Strom/Telekom |
| SW-W2 | SW-S3 | Erdreich | 150 | 6.13 | 2.03 | 0.67 | 518.938 | 518.814 | 2.00 | 18.35 | – |
| SW-S3 | SW-RS | Erdreich | 150 | 3.64 | 0.93 | 0.67 | 518.814 | 518.780 | 2.00 | 12.36 | – |
| SW-RS | Kanal-Einlass | Anschlusskanal | 150 | 4.60 | 43.04 | 0.67 | 518.780 | 516.800 | – | 84.95 | – |

### Schächte und Reinigungsöffnungen

| Id | Bauwerk | Art | x | y | Deckel | Sohle | Tiefe | DN | Grund |
|---|---|---|---|---|---|---|---|---|---|
| FL1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 7.00 | 12.00 | 520.21 | 519.10 | 1.10 | – | Fuß der Fallleitung |
| FL2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 13.00 | 18.50 | 520.30 | 519.20 | 1.11 | – | Fuß der Fallleitung |
| SW-S1 | Schacht | Inspektionsöffnung | 16.05 | 18.50 | 520.29 | 519.09 | 1.20 | 600 | Richtungsänderung 90° > 45° |
| SW-S2 | Schacht | Inspektionsöffnung | 16.05 | 7.95 | 520.08 | 518.88 | 1.20 | 600 | Richtungsänderung 49° > 45° |
| SW-S3 | Schacht | Inspektionsöffnung | 10.75 | 3.38 | 520.01 | 518.81 | 1.20 | 600 | Zusammenführung |
| SW-RS | Revisionsschacht | Revisionsschacht (Übergabeschacht) | 8.00 | 1.00 | 519.98 | 518.78 | 1.20 | 1000 | Ende der Grundstücksentwässerungsanlage (EWS § 8 Abs. 4) |
| HA1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 10.00 | 24.30 | 520.44 | 519.22 | 1.21 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF1 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 9.40 | 520.16 | 519.37 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF2 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 4.60 | 20.60 | 520.39 | 519.17 | 1.22 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF3 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 9.40 | 520.11 | 519.31 | 0.80 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| RF4 | Reinigungsöffnung | Reinigungsrohr/-öffnung | 15.40 | 20.60 | 520.34 | 519.23 | 1.10 | – | Standrohr mit Laubfangkorb (TRENGW Tab. 2) |
| NW-S1 | Schacht | Inspektionsöffnung | 15.96 | 20.39 | 520.33 | 519.20 | 1.13 | 400 | Zusammenführung |
| NW-S2 | Schacht | Inspektionsöffnung | 16.05 | 22.05 | 520.36 | 519.18 | 1.18 | 400 | Richtungsänderung 90° > 45° |
| NW-S3 | Schacht | Inspektionsöffnung | 10.06 | 22.31 | 520.40 | 519.12 | 1.27 | 600 | Zusammenführung |
| NW-S4 | Schacht | Inspektionsöffnung | 4.56 | 22.55 | 520.43 | 519.07 | 1.36 | 600 | Zusammenführung |
| NW-FS | Filterschacht | Filterschacht (Vorreinigung) | 3.40 | 22.60 | 520.43 | 519.06 | 1.38 | 600 | Vorreinigung vor der Rigole (NWFreiV § 3 Abs. 2) |

### Niederschlagswasser-Haltungen

| von | nach | DN | L [m] | Gefälle [%] | Sohle oben | Sohle unten | Q [l/s] | Q_zul [l/s] |
|---|---|---|---|---|---|---|---|---|
| HA1 | NW-S3 | 100 | 1.99 | 5.00 | 519.224 | 519.124 | 0.63 | 9.43 |
| RF1 | NW-B1 | 100 | 2.99 | 1.00 | 519.365 | 519.335 | 1.04 | 4.18 |
| NW-B1 | NW-B2 | 100 | 10.10 | 2.25 | 519.335 | 519.107 | 1.04 | 6.31 |
| NW-B2 | NW-FS | 100 | 0.99 | 5.00 | 519.107 | 519.058 | 1.04 | 9.43 |
| RF2 | NW-S4 | 100 | 1.95 | 5.00 | 519.167 | 519.069 | 1.04 | 9.43 |
| RF3 | NW-S1 | 100 | 11.00 | 1.00 | 519.311 | 519.201 | 1.04 | 4.18 |
| RF4 | NW-S1 | 100 | 0.60 | 5.00 | 519.231 | 519.201 | 1.04 | 9.43 |
| NW-S1 | NW-S2 | 100 | 1.67 | 1.00 | 519.201 | 519.184 | 2.07 | 4.18 |
| NW-S2 | NW-S3 | 100 | 6.00 | 1.00 | 519.184 | 519.124 | 2.07 | 4.18 |
| NW-S3 | NW-S4 | 100 | 5.50 | 1.00 | 519.124 | 519.069 | 2.70 | 4.18 |
| NW-S4 | NW-FS | 100 | 1.16 | 1.00 | 519.069 | 519.058 | 3.74 | 4.18 |

### Rigole (DWA-A 138-1, einfaches Verfahren)

A_E,b = 167.0 m², A_C = 131.2 m² (C_m), k_i = 7.20e-06 m/s; 1 Reihe(n), b = 0.80 m, h = 0.66 m, L_erf = 9.29 m → L = 9.60 m (12 Elemente), D_maßg = 240 min; A_S,m = 14.54 m², Q_S = 0.105 l/s, V_erf = 4.61 m³ ≤ V_vorh = 4.82 m³; Entleerung 12.2 h; OK 519.01, Sohle 518.35, Sickerraum -0.05 m; Abstand Gebäude 1.20 m (erf. 1.20 m). Vergleich Mulde: A_S ≥ 17.1 m² (passt).

### Regelprüfung

| Id | Status | Regel | Quelle | Befund |
|---|---|---|---|---|
| SW-01 | erfüllt | Revisionsschacht am Ende der Anlage auf eigenem Grund | EWS § 8 Abs. 4 [V] | Revisionsschacht DN 1000 bei (8.00; 1.00), Außenkante 0.40 m innerhalb der Grenze |
| SW-02 | erfüllt | Außenliegender Revisionsschacht nur bei >= 5 m zwischen Grenze und Gebäudekante | MSE-Leitfaden 2.6 [V] | Abstand Straßengrenze-Gebäude 9.00 m |
| SW-03 | erfüllt | Frostfreie Tiefe 1,20 m (GOK bis Rohrsohle) für erdverlegte SW-Leitungen | MSE-Leitfaden 2.7, EWS § 8 Abs. 3 [V] | alle Knoten >= 1,20 m |
| SW-04 | erfüllt | Mindestgefälle Grundleitungen (0,5 % im Gebäude, 1:DN außerhalb) | DIN 1986-100 [V] | eingehalten |
| SW-05 | erfüllt | Höchstgefälle 1:20 (sonst Absturzbauwerk) | kommunale Merkblätter [U] | eingehalten |
| SW-06 | erfüllt | Anschlusskanal geradlinig, ohne Gefällewechsel, Gefälle 1:DN bis 1:1 | MSE-Leitfaden 2.6 [V] | L = 4.60 m, Gefälle 43.0 % (zulässig 0.67-100 %) |
| SW-07 | erfüllt | Nennweite in Fließrichtung nicht verringern | DIN 1986-100 6.1.8 [V] | eingehalten |
| SW-08 | erfüllt | Hydraulische Leistungsfähigkeit (Q_ww <= Q bei h/d 0,5 innen / 0,7 außen) | DIN 1986-100 14.1.5 [V/U] | max. Auslastung 0.23 |
| SW-09 | erfüllt | Reinigungsöffnungen an Fallleitungsfüßen, Zusammenführungen, Richtungsänderungen > 45°, Abstand <= 20/40 m | DIN 1986-100 6.6 [U] | 3 Schacht/Schächte außen, 2 Reinigungsöffnung(en), Revisionsschacht DN 1000 |
| SW-10 | erfüllt | Ablaufstellen unter der Rückstauebene gegen Rückstau sichern | EWS § 8 Abs. 6, MSE-Leitfaden 2.2 [V] | alle Ablaufstellen über RSE 519.95 m (FFB EG 520.55); keine Rückstausicherung nötig |
| SW-11 | erfüllt | Geschützte Gehölze <= 5 m zur Leitungsachse im Plan 1:100 darstellen, ggf. Stellungnahme Baumschutz | MSE-Genehmigungsantrag Ziff. 3, MSE-Leitfaden 3.2 [V] | keine geschützten Gehölze im 5-m-Bereich |
| SW-12 | Hinweis | Kreuzungen mit Versorgungsleitungen im Plan eintragen, Abstände mit Netzbetreiber klären | MSE-Leitfaden 3.2 (Sparten im Bereich von SW-Leitungen) [V], Abstandswerte [U] | SW-S2-SW-S3 x HA Wasser/Strom/Telekom |
| SW-13 | Hinweis | Grundleitungen innerhalb von Gebäuden vermeiden; in der Bodenplatte genehmigungspflichtig | DIN 1986-100 6.1.1, MSE-Leitfaden 2.1 [V] | 5.27 m Leitung im/unter dem Gebäude (Grundleitung unter Bodenplatte) |
| NW-01 | erfüllt | Durchlässigkeit im Bereich 1e-6 bis 1e-3 m/s | DWA-A 138-1, MSE-Leitfaden 3.2 [V] | k_f = 1.0e-05 m/s, k_i = 7.20e-06 m/s (f_k = 0.72) |
| NW-02 | Verstoß | Sickerraum >= 0,5 m (absolute Untergrenze) | MSE-Leitfaden 3.2 (WWA München) [V] | -0.05 m < 0,5 m: unzulässig; Mulde/Flächenversickerung oder andere Lösung erforderlich |
| NW-03 | erfüllt | Sohle der Versickerungsanlage <= 5 m unter GOK | TRENGW Nr. 6 [V] | 1.97 m |
| NW-04 | erfüllt | Angeschlossene befestigte Fläche je Anlage <= 1000 m² | NWFreiV § 3 Abs. 1 [V] | A_E,b = 167.0 m² |
| NW-05 | Hinweis | Rigole nur, wenn flächenhafte Versickerung (Mulde) nicht möglich ist | NWFreiV § 3 Abs. 2, TRENGW Nr. 4 [V] | Mulde mit A_S >= 17.1 m² (hydraulisch 17.1 m², TRENGW 1/15: 11.1 m²) passt auf das Grundstück -> Rigole begründen oder Mulde wählen |
| NW-06 | Hinweis | Vorreinigung vor unterirdischer Versickerung | TRENGW Tab. 2 [V]; DWA-A 138-1 Tab. 7 [U] | Dach: Laubfangkörbe/Grobstoffrückhalt; Terrasse: Hofablauf mit Schlammeimer; Filterschacht NW-FS vor der Rigole. Nach DWA-A 138-1 sind auch Dachabflüsse zu behandeln (Gesamtwirkungsgrad je Flächenkategorie) – Produkt mit Nachweis wählen |
| NW-07 | erfüllt | Unbeschichtete Cu/Zn/Pb-Flächen > 50 m² nur über zugelassenen Filter | NWFreiV § 3 Abs. 2 [V] | keine |
| NW-08 | erfüllt | Abstand Versickerungsanlage-Gebäude >= 1,5 x Baugruben-/Fundamenttiefe | DWA-A 138-1 5.3.2 [V (Sekundärquelle)] | vorhanden 1.20 m, erforderlich 1.20 m (Fundamenttiefe 0.80 m) |
| NW-09 | erfüllt | Abstand zur Grundstücksgrenze >= 2 m | kommunale Leitfäden [U] | 3.00 m |
| NW-10 | erfüllt | Kein Überlauf der Versickerungsanlage an den städtischen Kanal | MSE-Leitfaden 5.2 [V] | kein Notüberlauf zum Kanal vorgesehen |
| NW-11 | erfüllt | Überflutungsnachweis bei A_C > 800 m² | DIN 1986-100 14.9, DWA-A 138-1 5.3.4 [V] | A_C (C_s) = 164.6 m² -> nicht erforderlich; nach DWA-A 138-1 Überflutungsfolgen trotzdem qualitativ bewerten |
| NW-12 | erfüllt | Frosttiefe 0,80 m für NW-Leitungen zur Versickerung | MSE-Leitfaden 2.7 [V] | eingehalten |
| NW-13 | erfüllt | Erlaubnisfrei nur außerhalb von Wasserschutzgebieten und Altlastverdachtsflächen | NWFreiV § 1 [V] | laut Technischem Formblatt (hier Beispielangabe: nein/nein) |
| NW-14 | erfüllt | Niederschlagswasser nicht in den städtischen Kanal einleiten (kein Anspruch) | EWS § 4 Abs. 4, MSE-Leitfaden 2.4/5 [V] | vollständige Versickerung auf dem Grundstück |
| NW-15 | erfüllt | Speichernachweis der Rigole V_vorh >= V_erf | DWA-A 138-1 Gl. 8 [V (Sekundärquelle)] | V_vorh = 4.82 m³ >= V_erf = 4.61 m³ (D = 240 min), Entleerung 12.2 h |

Niederschlagswassergebühr pauschal 371.70 EUR/a (600 m² × 0.35 × 1,77 EUR/m²); bei Vollversickerung 0 EUR/a (Antrag EAS § 8 Abs. 5).

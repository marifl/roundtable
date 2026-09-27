# Recherche 22: Schallberechnung und optimale Aufstellung von Wärmepumpen-Außengeräten (Monoblock R290, Split)

Stand: 27.09.2026. Baut auf Recherche 08, Abschnitt 5 auf (LAI-Tabelle, BayBO Art. 6 Abs. 1). **[V]** = am Primärtext oder an einer amtlichen bzw. Verlagsquelle geprüft, oder maschinell nachgerechnet. **[U]** = unsicher, Sekundärquelle oder eigene Bewertung. Normtexte (DIN, EN) sind kostenpflichtig. DIN ISO 9613-2 ist hier am englischen Originaltext ISO 9613-2:1996 geprüft, der öffentlich als Behördenexponat vorliegt (siehe Literatur). Die TA Lärm ist am amtlichen Text auf verwaltungsvorschriften-im-internet.de geprüft. Crossref war in dieser Sitzung gesperrt. DOIs sind deshalb an den Verlagsseiten geprüft.

Prototyp: `docs/holzbau/arbeit/beispiele/b20_waermepumpe_schall.py`, Tests in `tests/test_b20.py`, Eingabe in `daten/b20_waermepumpe.json`. Ausgaben in `ausgabe/b20_*`: `b20_waermepumpe.json` (alle Nachweise), `b20_waermepumpe.md` (Tabellen), `b20_laermkarte.svg`, `b20_laermkarte_R1.svg` und `b20_standortkarte.svg`.

## Ergebnis in 5 Punkten

1. **Verbindlich ist die TA Lärm, nicht die LAI-Tabelle.** Maßgeblich ist nachts die lauteste volle Stunde. Im WA gilt nachts ein Richtwert von 40 dB(A). Zuschläge K_T und K_I betragen je 0, 3 oder 6 dB, Zwischenwerte sind nicht zulässig. Der Immissionsort liegt 0,5 m vor der Mitte des geöffneten Fensters (A.1.3 a). Bei unbebauter Nachbarfläche liegt er am Rand der überbaubaren Fläche (A.1.3 b). Das ist ein Fall, den der BWP-Rechner nicht abbildet [V]. Die LAI 2023 rechnet mit IRW − 6 dB (Irrelevanz nach Nr. 3.2.1). Sie ist eine Empfehlung, die in der Praxis wie ein Zielwert wirkt [V].
2. **Die LAI-Tabelle 5 ist ein Spezialfall von ISO 9613-2, und das lässt sich exakt nachrechnen.** Die LAI-Abstände ergeben sich aus A_div (Gl. 7), D_Ω (Gl. 11), A_gr (Gl. 10) und α = 2 dB/km mit h_s = 1,5 m und h_r = 2 m. Alle 41 Tabellenwerte werden auf höchstens 0,11 m getroffen [V, eigene Reproduktion, Test `test_lai_tabelle5_aus_iso9613_reproduziert`]. Damit sind LAI-Tabelle, BWP-Rechner und detaillierte Prognose methodisch vergleichbar.
3. **Im freien Schallfeld sind die drei Verfahren gleichwertig. Bei Abschirmung und Reflexion gehen sie um bis zu 10 dB auseinander.** Im Beispiel liegen BWP und LAI bei freier Sicht innerhalb von ±1 dB der detaillierten Rechnung. Hinter dem eigenen Haus weicht der Pauschalwert „abgewandte Seite 15 dB“ um **−6,7 bis +9,7 dB** ab. Er kann also auch **zu günstig** sein, weil Schall seitlich um kurze Häuser gebeugt wird. In der Gasse zwischen Hauswand und Gartenmauer liegen BWP und LAI um rund 6 dB zu hoch [V, Prototyp].
4. **Die Aufstellung wird vor allem von der Sicherheit und der Leitungsführung begrenzt, nicht vom Schall.** Von 2 304 Rasterpunkten (0,5 m) sind für die Monoblock-R290 nur 834 zulässig. Die meisten scheitern am R290-Schutzbereich, der über die Grenze ragt (564) oder Öffnungen und Einläufe enthält, und an der Leitungslänge (499). Die typische Installateurwahl „Ostseite vor dem HWR“ ist schalltechnisch in Ordnung, aber **unzulässig**, weil das HWR-Fenster im Schutzbereich liegt. Das Optimum liegt im Vorgarten bei (7,25 m / 1,75 m). Dort gilt L_r,N ≤ 27 dB(A) an allen Immissionsorten, die Reserve beträgt 12,9 dB, und das Irrelevanzkriterium ist überall erfüllt [V, Prototyp].
5. **Split-Geräte mit R32 dürfen ab 01.01.2027 nicht mehr in Verkehr gebracht werden** (Luft-Wasser-Split ≤ 12 kW mit GWP ≥ 150, VO (EU) 2024/573 Anhang IV Nr. 9 b). Ab 2035 gilt das für alle F-Gase (Nr. 9 d). Monoblock-Geräte ≤ 12 kW sind ab 2027 bei GWP ≥ 150 betroffen, ab 2032 bei jedem F-Gas (Nr. 8 b, c) [V]. Für Holzbau-Fertighäuser in Bayern ab 2027 heißt das praktisch: **Monoblock mit R290 und dem Schutzbereich als harter geometrischer Regel.**

## Regel-Tabelle mit Kernwerten

| Regel / Quelle | Kernwert | Umsetzung im Planer | Status |
|---|---|---|---|
| BImSchG § 22 Abs. 1 Nr. 1, 2 | nicht genehmigungsbedürftige Anlage: vermeidbare schädliche Umwelteinwirkungen verhindern, unvermeidbare auf ein Mindestmaß beschränken; Behörde kann nach §§ 24, 25 anordnen | Rechtsgrundlage des Nachweises | [V] (LAI 2023 Kap. 3.3; VG Düsseldorf 3 K 8968/22) |
| TA Lärm Nr. 6.1 | IRW außen tags/nachts: WR 50/35, WA und WS 55/40, MI, MD und MK 60/45, MU 63/45, GE 65/50, Kurgebiet 45/35 dB(A) | Konstante je Gebiet | [V] |
| TA Lärm Nr. 6.1 letzter Satz | Geräuschspitzen: tags ≤ IRW + 30, nachts ≤ IRW + 20 dB(A) | Nachweis mit L_WA,max (Abtauen, Anlauf) | [V] |
| TA Lärm Nr. 6.4 | tags 06–22 Uhr (T_r = 16 h), nachts 22–06 Uhr, maßgeblich die lauteste volle Nachtstunde | T_r,N = 1 h | [V] |
| TA Lärm Nr. 6.5 (mit Korrektur BMUB 07.07.2017) | K_R = 6 dB werktags 06–07 und 20–22 Uhr, sonn- und feiertags 06–09, 13–15 und 20–22 Uhr; gilt in WS, WA, WR und Kurgebiet (redaktionell „e bis g“) | Teilzeiten in G2 | [V] |
| TA Lärm Nr. 3.2.1 Abs. 2, Nr. 4.2 c | Zusatzbelastung ≥ 6 dB(A) unter IRW gilt als irrelevant, Vorbelastung ist dann entbehrlich | Zielwert IRW − 6 (LAI-Empfehlung) | [V] |
| TA Lärm A.1.3 | IO 0,5 m vor Mitte des geöffneten Fensters des am stärksten betroffenen schutzbedürftigen Raums (DIN 4109); unbebaut: Rand der Fläche, auf der schutzbedürftige Gebäude zulässig sind | IO-Konstruktion, Linien-IO an der Baugrenze | [V] |
| TA Lärm A.1.4 (G2) | L_r = 10 lg[(1/T_r) Σ T_j 10^(0,1(L_Aeq,j − C_met + K_T,j + K_I,j + K_R,j))] | Formel | [V] |
| TA Lärm A.2.3.4 / A.2.3.1 | Detaillierte Prognose nach DIN ISO 9613-2 in Oktaven 63–4000 Hz; nur bei A-bewerteten Daten gilt ISO 9613-2 Abschnitt 1 (500-Hz-Terme) | Standard: A/500 Hz, Vergleich Oktave | [V] |
| TA Lärm A.2.4.3 (G4) | Überschlägige Prognose: L_Aeq = L_WAeq + D_I + K0 − 20 lg s − 11 dB, nur Eigenabschirmung, Reflexionen über K0 (VDI 2714) | = BWP-Rechner | [V] |
| TA Lärm A.2.5.2 / A.3.3.5 | K_T 3 oder 6 dB je nach Auffälligkeit; messtechnisch DIN 45681 | Eingabe K_T | [V] |
| TA Lärm Nr. 7.3, A.1.5 | tieffrequent: < 90 Hz, L_Ceq − L_Aeq > 20 dB als Hinweis; DIN 45680:1997-03 und Beiblatt 1 | nur Warnhinweis (keine Prognose) | [V] |
| LAI-Hinweise TA Lärm (24.02.2023) | Zwischenwerte mit einer Nachkommastelle nicht runden, L_r in vollen dB nach DIN 1333; Genauigkeit ±3 dB, im Nahbereich ±1 dB | `runde_din1333` | [V] |
| LAI-Leitfaden 2023, Kap. 4 | L_E = L_WA − Sicht (0/5/15) + Reflexion (0/3/6) + Ton (0/3/6, unbekannt → 3); Tab. 5 Mindestabstände für IRW_N − 6; Mindestabstand 1,0 m | Vergleichsverfahren | [V] |
| LAI 2023 Kap. 4.1.3 | maßgeblich ist der höchste L_WA im Nachtbetrieb; der Label-Wert ist nicht immer der Maximalwert; Silent-Mode nur, wenn garantiert | Eingabe L_WA,Nacht | [V] |
| LAI 2023 Kap. 6 | Schirm nahe an der Quelle bis ca. 10 dB, Kapsel bis ca. 20 dB, Hecken ohne Wirkung; tonhaltige Geräte entsprechen nicht dem Stand der Technik | Maßnahmenkatalog | [V] |
| VO (EU) 813/2013 (über LAI Tab. 1) | L_WA-Grenzwert außen: ≤ 6 kW 65 dB, 6–12 kW 70 dB, 12–30 kW 78 dB, 30–70 kW 88 dB | Plausibilitätsgrenze | [V] (über LAI) |
| LfU Bayern (Luftwärmepumpen) | Empfehlung L_WA ≤ 50 dB(A) im EFH; Wand +3 dB, zwei Wände +6 dB; 6 dB unter IRW anstreben; abgewandte Fassade nutzen | Hinweis | [V] |
| BayBO Art. 6 Abs. 1 Satz 3 Nr. 4 (seit 01.01.2025) | WP und Einhausungen bis 2 m über Gelände lösen keine Abstandsflächen aus | Höhenprüfung ≤ 2 m | [V] |
| BayBO Art. 6 Abs. 7 Satz 1 Nr. 3 | geschlossene Einfriedungen außerhalb GE/GI bis 2 m ohne eigene Abstandsfläche | Gartenmauer 2,0 m | [V] |
| StMB-Rundschreiben 24.07.2023 | übliche Luft-WP ohne gebäudegleiche Wirkung; Lärm nicht über das Abstandsflächenrecht, sondern über das Rücksichtnahmegebot | Hinweis | [V] |
| BWP-Leitfaden Außenaufstellung A3-Kältemittel (2024) | Schutzbereich nach Herstellerangabe: keine Zündquellen, Gebäudeöffnungen, Lichtschächte, Einläufe oder Senken; darf nicht über die Grundstücksgrenze oder auf Verkehrsflächen reichen | Sperrzone (shapely) | [V] |
| Herstellerbeispiele R290 | typisch 1 m am Boden, 0,5 m an der Geräteoberkante; Trennwand kann auf 0,5 m reduzieren; Ansaug ≥ 200 mm zur Wand, Ausblas > 1 m frei, ≥ 3 m zu Gehweg und Terrasse | Beispielparameter | [V] je Anleitung, **herstellerspezifisch** |
| VO (EU) 2024/573 Anhang IV Nr. 8, 9 | Monoblock ≤ 12 kW: GWP ≥ 150 ab 2027, jedes F-Gas ab 2032; Luft-Wasser-Split ≤ 12 kW: GWP ≥ 150 ab 2027, jedes F-Gas ab 2035; Ausnahme bei Sicherheitsanforderungen am Standort | `f_gase_pruefung` | [V] |

## 1 Rechtsrahmen

**BImSchG und TA Lärm.** Eine Wärmepumpe ist eine nicht genehmigungsbedürftige Anlage nach § 22 BImSchG. Die TA Lärm konkretisiert die Betreiberpflichten. Nach der Rechtsprechung ist sie im Anwendungsbereich grundsätzlich abschließend bindend (VG Düsseldorf, Urt. v. 10.12.2024 – 3 K 8968/22, Leitsatz 3) [V]. Eine Regelfallprüfung nach Nr. 4.2 findet nur statt, wenn die WP Teil einer öffentlich-rechtlichen Zulassung ist (Bauantrag). Sonst bleibt nur das nachträgliche Einschreiten nach § 24 BImSchG [V, LAI 2023 Kap. 3.3.2]. Die LAI-Kurzfassung verlangt für baugenehmigungspflichtige Vorhaben mit WP als Hauptwärmequelle einen Nachweis mit Lageplan, IO, Abstand, L_WA und begründeten Zuschlägen [V]. Das ist genau das Datenmodell des Prototyps.

**Zuschläge.** K_T und K_I betragen je 3 oder 6 dB, es gibt keine Zwischenwerte (LAI-Hinweise zu A.2.5.2) [V]. Der Ruhezeitenzuschlag K_R gilt nach der Korrektur von 2017 in WS, WA, WR und Kurgebiet [V]. Er wirkt nur über die Teilzeiten: Ein Dauerpegel von 56 dB(A) ergibt L_r,T = 57,9 dB(A), nicht 62 dB(A) (Beispiel IZU/Umweltpakt Bayern, im Test nachgerechnet) [V]. Nachts gibt es kein K_R, deshalb ist die Nacht für WP maßgeblich.

**Irrelevanz und Vorbelastung.** Unterschreitet die Zusatzbelastung den IRW um mindestens 6 dB(A), ist sie irrelevant. Die Vorbelastung muss dann nicht ermittelt werden (Nr. 3.2.1 Abs. 2, Nr. 4.2 c) [V]. Die LAI legt ihre Tabelle bewusst auf IRW − 6 aus, weil künftig mehrere WP auf einen IO einwirken [V]. Die LAI-Hinweise warnen: Viele Anlagen, die einzeln je 6 dB unter dem IRW liegen, können zusammen eine Sonderfallprüfung (Nr. 3.2.2) auslösen [V].

**Bayern.** Seit 01.01.2025 lösen WP bis 2 m keine Abstandsflächen aus (BayBO Art. 6 Abs. 1 Satz 3 Nr. 4) [V]. Die früher strittige Frage war, ob Lärm eine „gebäudegleiche Wirkung“ ist. Das OLG Nürnberg bejahte das (30.01.2017 – 14 U 2612/15), das OLG München (11.04.2018 – 3 U 3538/17) und das OLG Bamberg (04.05.2021 – 5 U 176/20) verneinten es, ebenso das StMB-Rundschreiben vom 24.07.2023 [V, zitiert im Rundschreiben]. Die Frage ist damit gesetzlich erledigt. Das LfU Bayern empfiehlt L_WA ≤ 50 dB(A) und 6 dB Unterschreitung [V]. Gestaltungssatzungen nach Art. 81 BayBO können Standort und Einhausung zusätzlich regeln [U, gemeindespezifisch].

**Zivilrecht.** Nachbarn können über §§ 1004, 906 BGB auf Unterlassung klagen. Die TA-Lärm-Werte dienen dabei als Maßstab für die Wesentlichkeit [U, allgemeine Rechtslage]. Das LG Bielefeld wies eine solche Klage wegen tieffrequenter Brummtöne ab. Die Messungen erfolgten nach DIN 45680 im Schlafzimmer, eine Messung zeigte Überschreitungen in zwei Terzen, zwei weitere keine (Urt. v. 09.06.2026 – 1 O 310/24) [V].

**Rechtsprechung zur Tonhaltigkeit.** Im Fall VG Düsseldorf 3 K 8968/22 stand die WP im WR 7 m vor dem Schlafzimmerfenster. Die Behörde vergab tags einen Tonzuschlag von 6 dB(A). Der Kläger argumentierte mit der LAI-Aussage, tonhaltige Geräte seien nicht Stand der Technik. Die Klage auf Einschreiten wurde abgewiesen [V]. Im Fall OVG NRW, Beschl. v. 06.08.2026 – 8 A 134/25 ergab die Überwachungsmessung im faktischen WR 34 dB(A) tags und 19 dB(A) nachts. Das Gericht bestätigte den Maßstab TA Lärm [V; Tenor im Detail nicht gelesen, U]. Nach VGH BW, Beschl. v. 30.01.2019 – 5 S 1913/18 sind im Nachbarrechtsbehelf gegen eine Baugenehmigung auch Messungen nach Inbetriebnahme heranzuziehen [U, Abschrift auf einer Kanzleiseite]. **Folge für den Planer:** K_T ist die größte Stellschraube, die der Planer nicht selbst kontrolliert. Ohne Herstelleraussage ist K_T = 3 dB anzusetzen (LAI).

## 2 Rechenverfahren mit vollständigem Rechenweg

### 2.1 Emission

- **Schallleistungspegel.** Das ErP-Label nach VO (EU) 811/2013 zeigt den Außen-Schallleistungspegel. Er wird nach EN 12102-1 unter Normbedingungen gemessen [V: LAI 2023 Kap. 2.1; Messpunkt U]. Die Werte sind nicht zwingend der Maximalwert. Für die Nacht ist der höchste im Nachtbetrieb mögliche L_WA anzusetzen, ein Silent-Mode nur, wenn er garantiert ist (LAI 4.1.3) [V]. Das BWP-Verfahren verlangt ausdrücklich den maximalen L_WA für Tag und Nacht [V]. KEYMARK-Datenblätter enthalten ebenfalls Schallleistungen nach EN 12102-1 [U, nicht geprüft].
- **Oktavspektrum.** Hersteller müssen es nicht angeben. Tonhaltigkeit, tieffrequente Anteile und saisonale Änderungen (Abtauen) sind nicht kennzeichnungspflichtig (LAI 2.3) [V]. Im Prototyp ist ein Oktavspektrum nur ein klar gekennzeichnetes **Beispiel**.
- **Richtwirkung D_I.** Die Richtwirkung ist nicht angenommen (LAI 4.1.1) [V]. Die Ausblasrichtung wird als Aufstellregel geprüft (weg von den IO), nicht akustisch bewertet.

### 2.2 Ausbreitung nach DIN ISO 9613-2 (= ISO 9613-2:1996), je Pfad und A-bewertet mit den 500-Hz-Termen

| Schritt | Formel (Gl. in ISO 9613-2:1996) | Einheit | Status |
|---|---|---|---|
| Grundgleichung | L_AT(DW) = L_W + D_c − A, mit A = A_div + A_atm + A_gr + A_bar + A_misc (3), (4) | dB | [V] |
| Divergenz | A_div = 20 lg(d/1 m) + 11 (7) | dB | [V] |
| Luftabsorption | A_atm = α·d/1000 (8), α(500 Hz; 10 °C; 70 %) = 1,9 dB/km (Tab. 2). Bei d ≤ 35 m unter 0,07 dB, also **vernachlässigbar, aber mitgerechnet** | dB | [V] |
| Boden | A_gr = 4,8 − (2h_m/d)(17 + 300/d) ≥ 0 (10), alternatives Verfahren für A-Pegel und porösen Boden. Bei h_m ≈ 1,2–2,5 m ist der Wert erst ab etwa 20–30 m > 0 | dB | [V] |
| Bodenreflexion an der Quelle | D_Ω = 10 lg{1 + [d_p² + (h_s − h_r)²]/[d_p² + (h_s + h_r)²]} (11), Teil von D_c. Im Fernfeld → 3 dB. **Das ist der „Halbraum“** | dB | [V] |
| Abschirmung über die Kante | A_bar = D_z − A_gr > 0 (12); D_z = 10 lg[3 + (C2/λ)·C3·z·K_met] (14), C2 = 20, λ = 340/f | dB | [V] |
| Mehrfachkante | C3 = [1 + (5λ/e)²]/[1/3 + (5λ/e)²] (15); z = d_ss + d_sr + e − d (16, 17). Im Prototyp: Gummiband als obere konvexe Hülle im Vertikalschnitt des (entfalteten) Pfads | – , m | [V]; Gummiband-Konstruktion [U, entspricht ISO/TR 17534-3 bzw. ISO 9613-2:2024] |
| Meteorologie im Schirm | K_met = exp[−(1/2000)√(d_ss·d_sr·d/(2z))] für z > 0, sonst 1 (18); für d < 100 m ≈ 1 (Anm. 17) | – | [V] |
| Seitliche Beugung | A_bar = D_z > 0 mit K_met = 1 (13), Pfade quadratisch addiert (7.4). Im Prototyp nur relevant, wenn z_seitlich ≤ 8·z_oben | dB | Formel [V]; 8-fach-Kriterium [U] |
| Begrenzung | D_z ≤ 20 dB (Einfach-), ≤ 25 dB (Doppelbeugung) | dB | [V] |
| Sichtlinie knapp frei | z erhält negatives Vorzeichen, D_z fällt von 4,77 dB auf 0 bei z = −λ/10 | dB | [V] (Vorzeichenregel), Verlauf nachgerechnet |
| Reflexion | Spiegelquelle bei gültiger spiegelnder Reflexion, ρ > 0,2 und Mindestgröße 1/λ > [2/(l_min cos β)²]·[d_so d_or/(d_so + d_or)] (19); L_W,im = L_W + 10 lg ρ + D_Ir (20); ρ: ebene harte Wand 1, Gebäudewand mit Fenstern 0,8 (Tab. 4) | dB | [V] |
| Summe | L_AT = 10 lg Σ_i 10^(0,1 L_i) über Quelle und Spiegelquellen (5) | dB(A) | [V] |
| Langzeit | C_met = 0 für d_p ≤ 10(h_s + h_r), sonst C0[1 − 10(h_s + h_r)/d_p] (21, 22). Bei WP-Abständen fast immer 0 | dB | [V] |
| Genauigkeit | h < 5 m, d < 100 m: ±3 dB (Tab. 5; ohne Reflexion und Schirm). LAI-Hinweise: im Nahbereich ±1 dB zulässig | dB | [V] |

**Richtwirkung und Raumwinkelmaß: die Frage „+0 / +3 / +6“ geklärt.** Es gibt drei Konventionen, die alle dasselbe beschreiben:

| Aufstellung | BWP / TA Lärm G4 (K0, VDI 2714) | LAI 2023 (Reflexionswert, zusätzlich Bodenmodell D_Ω) | ISO 9613-2 detailliert |
|---|---|---|---|
| frei auf dem Boden | +3 dB (Halbraum) | 0 dB + D_Ω (≈ 1,9–3 dB, im Nahbereich < 3) | D_Ω nach Gl. (11) |
| vor einer Wand (< 3 m) | +6 dB (Viertelraum) | +3 dB + D_Ω | + Spiegelquelle: 10 lg(1 + ρ) = +3,0 dB (ρ = 1) bzw. +2,6 dB (ρ = 0,8) |
| Ecke, zwei Wände, Vordach | +9 dB (Achtelraum) | +6 dB + D_Ω | 3 Spiegelquellen (2 × 1., 1 × 2. Ordnung): +6,0 dB (ρ = 1) |

„Freistehend +0“ gilt also nur, wenn der Boden separat als Halbraum gerechnet wird. Die Tabellenwerte der Aufgabenstellung stimmen für die LAI-Konvention [V]. Die ISO-Werte sind im Test `test_reflexion_wand_plus_3_dB_und_ecke_plus_6_dB` nachgerechnet: Die Innenecke ergibt mit 2. Ordnung +6,0 dB und ohne sie nur +4,8 dB [V].

**Rekonstruktion der LAI-Tabelle 5 (neu, [V] durch Nachrechnung).** LAI 4.1.3 nennt die Formel L_E = L_IRW − 6 + K0 + A_div + A_atm + A_gr mit h_s = 1,5 m, h_r = 2 m und α = 2 dB/km. Setzt man K0 = D_Ω (Gl. 11) und A_gr nach Gl. (10) mit h_m = 1,75 m, reproduziert die Bisektion alle 41 WR-Werte (40–80 dB) auf ≤ 0,11 m. 36 von 41 Werten stimmen bei kaufmännischer Rundung exakt. Der Knick der Tabelle zwischen 64 und 65 dB (22,2 → 23,7 m) ist der Einsatz von A_gr ab ca. 23 m. Die WA-Spalte ist die WR-Spalte um 5 dB verschoben, MI/MD/MU/MK um 10 dB. Damit ist die Spaltenzuordnung aus Recherche 08 bestätigt ([U] → [V]).

### 2.3 Beurteilung nach TA Lärm

- Nacht: L_r,N = L_Aeq,N + K_T + K_I + 10 lg(T_E/60 min), mit T_E = 60 min (konservativ, Dauerlauf in der lautesten Stunde).
- Tag: L_r,T = 10 lg[(1/16 h)(1 h·10^0,1(L+K_T+6) + 13 h·10^0,1(L+K_T) + 2 h·10^0,1(L+K_T+6))]. Das entspricht **+1,9 dB** gegenüber L + K_T. Der BWP schlägt pauschal +6 dB auf den ganzen Tag [V, BWP-Leitfaden 4.1] und ist damit tags um 4,1 dB konservativer.
- Spitzen: L_AFmax = L_AT,N − L_WA,N + L_WA,max ≤ IRW_N + 20 dB.
- Rundung: intern ungerundet, Ausweisung 0,1 dB, Vergleich mit dem IRW in vollen dB nach DIN 1333 (40,5 → 41) [V].
- Unsicherheit: Prognose ±3 dB (ISO Tab. 5). L_WA nach EN 12102-1 hat eine zusätzliche Messunsicherheit (Größenordnung 1,5–2 dB [U]). Im Prototyp als Sensitivität ±1 dB L_WA ausgewiesen. Das wirkt **exakt linear** (Test `test_sensitivitaet_lwa_linear`), deshalb ändert sich die Rangfolge der Standorte nicht.

### 2.4 Tonhaltigkeit, tieffrequente Geräusche, Körperschall

- **Tonhaltigkeit** wird bei der Prognose als K_T 0/3/6 geschätzt (Erfahrungswerte, A.2.5.2). Gemessen wird sie nach DIN 45681; die TA Lärm verweist auf den Entwurf 05/1992, aktuell ist die Ausgabe 2005 [U]. Die LAI schreibt: „Ist über die Tonhaltigkeit nichts bekannt, soll zur Sicherheit 3 dB gewählt werden“ [V].
- **Tieffrequente Geräusche.** Die TA Lärm verweist auf DIN 45680:1997-03 mit Beiblatt 1 (Messung im Raum bei geschlossenem Fenster). **DIN 45680:2020-06 ist nur ein Norm-Entwurf.** Nach drei Entwürfen (2011, 2013, 2020) gab es keinen Konsens. Die Fassung 1997 bleibt gültig, die neuen Inhalte sollen als DIN/TS 45610-1 und DIN/TR 45610-2 erscheinen, „spätestens Anfang 2026“ [V: DIN-FAQ 18.11.2025; ob sie erschienen sind, ist U]. Ein genormtes Prognoseverfahren gibt es nicht (LAI 3.3.6) [V]. Der Planer kann nur warnen (Kompressor im Innengerät, keine Aufstellung vor Schlafraum-Außenwänden).
- **Körperschall im Holzbau.** Die TA Lärm gibt für Körperschall keine Rechenvorschrift (A.2.1) [V]. Für Körperschall in betriebsfremde Räume gilt Nr. 6.2 (35/25 dB(A) innen) [V]. Die LAI empfiehlt elastische Lagerung und keine Aufstellung auf schwimmendem Estrich. Rohre sollen flexibel angeschlossen werden (6.3.4) [V]. **Für Holzbau folgt daraus: keine Wandkonsole an der Holzrahmenwand eines Aufenthaltsraums.** Leichte Wände mit geringer Masse strahlen Körperschall stark ab [U, bauakustische Bewertung, nicht quantifiziert]. Bevorzugt wird eine Bodenkonsole auf separatem Fundament mit Fuge zur Bodenplatte.

## 3 Aufstellregeln

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| R290-Schutzbereich (Monoblock) | keine Zündquellen, Fenster, Türen, Lüftungsöffnungen, Lichtschächte, Fallrohre, Einläufe, Schächte oder Senken im Bereich; darf nicht auf Nachbargrund, Gehwege oder Parkplätze reichen; typisch 1 m am Boden, 0,5 m an der Oberkante, Fenster oberhalb mit Abstand erlaubt; eine gasdichte Trennwand reduziert einseitig auf 0,5 m | BWP-Leitfaden A3-Kältemittel 2024; Herstelleranleitungen | [V], Maße **herstellerspezifisch** |
| Normbezug Schutzbereich | EN 378-3 bzw. EN IEC 60335-2-40 | – | [U], nicht am Normtext geprüft |
| Servicearbeiten R290 | Sicherheitsbereich 3 m Radius bei Befüllen oder Rückgewinnen (Herstellerbeispiel) | Herstelleranleitung | [V] (eine Anleitung) |
| Luftführung | Ansaug ≥ 200 mm zur Wand, Ausblas > 1 m frei, ≥ 3 m zu Gehweg und Terrasse (Vereisung, Ausblas ca. 8 K kälter); nicht in Nischen (Luftkurzschluss, Reflexion) | Herstelleranleitung | [V] (Beispiel) |
| Schnee und Frost | Sockel ≥ 100 mm über Schneehöhe, Vordach, Kondensat frostfrei (Begleitheizung, Siphon) | Herstelleranleitung | [V] (Beispiel) |
| Split-Kältemittelleitung | maximale Länge und Höhenunterschied nach Hersteller (Beispiel 15 m einfach, 10 m Höhe); Installation, Befüllung und Dichtheitsprüfung nur durch zertifiziertes Personal | VO (EU) 2024/573; UBA-FAQ | Pflicht [V], Artikelnummer (Art. 10) [U] |
| F-Gase-Verbote | siehe Regel-Tabelle; R32 hat GWP 675 → Luft-Wasser-Split ≤ 12 kW ab 2027 verboten | Anhang IV | [V], GWP-Wert [U] |
| Abstandsflächen | WP ≤ 2 m ohne Abstandsfläche; Einhausung ebenfalls ≤ 2 m; Einfriedung ≤ 2 m ohne Abstandsfläche | BayBO Art. 6 Abs. 1 S. 3 Nr. 4, Abs. 7 Nr. 3 | [V] |
| Einhausung / Schallschutzhaube | Kapsel bis ca. 20 dB (nur mit innen absorbierender Oberfläche, abgedichtet und entkoppelt), Schirm nahe an der Quelle ca. 10 dB, Teilumschließung 5–10 dB, Vorsatzschale 5–10 dB; der Luftstrom darf nicht behindert werden | LAI 2023 Kap. 6.3; LfU 2011 | [V]; Einfügungsdämpfung eines konkreten Produkts nur nach Herstellerprüfbericht |

Im Prototyp sind die Regeln harte Constraints je Rasterpunkt, mit dem Grund im Tooltip der Standortkarte. Geprüft werden: Hüllkreis im Grundstück, Wandabstand, Höhe ≤ 2 m, Schutzbereich im Grundstück und frei von Öffnungen (Unterkante < Geräteoberkante + 0,5 m) und Senken, Leitungslänge und mindestens eine Ausblasrichtung mit 1 m Freiraum, die möglichst weit von den IO weg zeigt.

## 4 Abgrenzung zum BWP-Schallrechner

Der BWP-Rechner (waermepumpe.de/werkzeuge/schallrechner) nutzt nach eigener Angabe die **überschlägige Prognose der TA Lärm** (A.2.4.3, G4) [V]:

- L_r = L_W,Aeq + K_T + K0 − 20 lg s_m − 11 dB (+ K_R = 6 dB pauschal für den **ganzen** Tag). K0 beträgt 3/6/9 dB je nach Wandzahl unter 3 m oder Vordach unter 5 m. Die Abschirmung wird pauschal mit 0 (Sicht), 5 (keine Sicht) oder 15 dB (abgewandte Seite) angesetzt [V].
- Vereinfachungen: keine Bodendämpfung außer K0, keine Luftabsorption, C_met = 0, K_I „nicht relevant“, keine Richtwirkung D_I, keine geometrische Schirmberechnung, keine Reflexionen an fremden Fassaden, keine Linien-IO an der Baugrenze, keine Summe mehrerer Geräte oder der Vorbelastung. Die 6-dB-Irrelevanz muss man nach Angabe eines Landkreises selbst abziehen [V: BWP-Leitfaden 4.1; Landkreis Neunkirchen]. Das Beispiel im BWP-Leitfaden (59/51 dB, K_T 3, Wand, 6 m) ergibt L_r,T = 47,4 und L_r,N = 33,4 dB(A). Der Test `test_bwp_beispiel_leitfaden` reproduziert beide Werte [V].
- **Befund im Prototyp:** Bei freier Sicht und ohne nahe Wände weicht der BWP-Wert höchstens 0,9 dB von der detaillierten Rechnung ab (R3, Optimum IO1/2/5). An der Hauswand gegenüber dem Nachbarn liegt er 1,7–3,1 dB höher (R2). In der Gasse zwischen Haus und Mauer liegt er 5,9 dB höher (R1/IO5). Hinter dem eigenen Haus reicht die Abweichung von **−6,7 dB bis +9,7 dB**. Der Pauschalwert 15 dB ist also weder sicher konservativ noch präzise. Die LAI-Tabelle zeigt dasselbe Muster, weil sie dieselben Pauschalwerte verwendet.

## 5 Werkzeuge und Forschung

- **NoiseModelling** (Université Gustave Eiffel/Cerema, Java, **GPL v3**, v6.0.0 vom 20.05.2026) implementiert CNOSSOS-EU (Richtlinie 2015/996) für Straße und Schiene samt Ausbreitung. ISO 9613-2 ist nach README und Doku **nicht** das implementierte Verfahren [V: GitHub/readthedocs]. CNOSSOS unterscheidet sich im Bodenmodell und in der Meteorologie. Für die TA Lärm ist das Werkzeug daher nicht direkt verwendbar, aber als unabhängige Plausibilisierung nützlich.
- **openPSTD** (pseudospektrale Wellenrechnung) und kommerzielle Programme (CadnaA, SoundPLAN, IMMI) wurden nicht geprüft [U].
- **Eigene Implementierung** (B20) mit Deckung durch Normtext, Handrechnung und LAI-Reproduktion. Für die Arbeit ist die Konformitätsprüfung nach ISO/TR 17534-3 (Testfälle zu ISO 9613-2) der nächste Schritt [U, TR nicht gelesen].
- **ISO 9613-2:2024** (2. Ausgabe) überarbeitet unter anderem D_z/K_met bei niedrigen Schirmen, die Kombination vertikaler und seitlicher Beugung, die Mindestgröße reflektierender Flächen und Mehrfachreflexionen. Außerdem ist ein Korrekturglied im vereinfachten Bodenverfahren neu [V: Vorwort, iTeh-Leseprobe]. Die TA Lärm verweist weiter auf den Entwurf 1997, deshalb rechnet der Prototyp nach der Ausgabe 1996/1999. Ob eine DIN-Übernahme der Ausgabe 2024 erschienen ist, ist [U].
- **Forschung.** Es gibt Hörversuche zur Lästigkeit von WP-Geräuschen, auch zu Tonalität, Rauigkeit, Schaltvorgängen und mehreren Geräten (IEA HPT Annex 51 und 63; Acun et al. 2026; Stürenburg et al. 2026; Becker et al., Forum Acusticum 2026). Der A-Pegel erklärt die Lästigkeit ähnlich gut wie die Lautheit. Tonalität und Rauigkeit erhöhen die Lästigkeit darüber hinaus [V: Abstracts]. Das stützt einen strengen Umgang mit K_T.

## 6 IFC-4.3-Mapping (am Schema IFC4X3_ADD2 mit IfcOpenShell 0.8.5 geprüft)

| Objekt | IFC | Attribute / Property | Status |
|---|---|---|---|
| WP-Außengerät Monoblock | `IfcUnitaryEquipment`, PredefinedType `USERDEFINED`, ObjectType „AirToWaterHeatPump_Monoblock“ (es gibt kein IfcHeatPump) | `Pset_UnitaryEquipmentTypeCommon` (Reference, Status); Nennleistung als eigenes Pset | [V] Enum: AIRCONDITIONINGUNIT, AIRHANDLER, DEHUMIDIFIER, ROOFTOPUNIT, SPLITSYSTEM, USERDEFINED, NOTDEFINED |
| Split-Außeneinheit | `IfcUnitaryEquipment`, PredefinedType `SPLITSYSTEM` | dito | [V] |
| Schallleistung Oktave | `Pset_SoundGeneration.SoundCurve` als `IfcPropertyTableValue` (Frequenz `IfcFrequencyMeasure` → `IfcSoundPowerMeasure`) | Oktaven 63–8000 Hz. Die Beschreibung nennt „Dezibel re 1 pW“, der Messtyp ist aber Leistung. Die Vereinbarung ist im Projekt festzulegen | [V] (Template), Widerspruch Messtyp/Beschreibung [V] |
| A-bewertete Kennwerte | eigenes Pset, z. B. `Pset_Holzbau_WPSchall`: `LWA_Tag`, `LWA_Nacht`, `LWA_Max` (`IfcSoundPowerLevelMeasure`), `KT` (`IfcReal`), `Messnorm` (EN 12102-1), `Quelle` | es gibt kein Standard-Pset für L_WA | Typ [V], Pset-Name eigener Vorschlag |
| Kältemittel | eigenes Pset: `Kaeltemittel` (R290), `GWP`, `Fuellmenge_kg`, `Sicherheitsklasse` (A3) | Grundlage für die F-Gase-Prüfung | Vorschlag |
| R290-Schutzbereich | `IfcSpatialZone`, PredefinedType `USERDEFINED` („R290_Schutzbereich“), Geometrie = Hüllkörper, Zuordnung zum Gerät über `IfcRelAssignsToProduct` | IDS-Regel: keine `IfcWindow`/`IfcDoor`-Öffnung schneidet die Zone (Kollisionsprüfung) | Entitäten [V], Konvention eigener Vorschlag |
| Wartungs- und Luftführungsbereich | `IfcSpatialZone` PredefinedType `RESERVATION` | Ansaug- und Ausblasfreiraum | [V] Enum |
| Immissionsort | `IfcAnnotation` PredefinedType `USERDEFINED` („Immissionsort“) oder `IfcSpatialZone` (Punkt 0,5 m vor dem Fenster), Bezug auf das Fenster über `IfcRelInterferesElements`/Referenz | Nachbargebäude sind in der Regel nur als Kontextmodell vorhanden | Entitäten [V], Konvention [U] |
| Isolinien der Lärmkarte | `IfcAnnotation` PredefinedType `CONTOURLINE` | Pegelwert als Property | [V] Enum |
| Messwerte am IO | `Pset_SoundAttenuation` (nur an `IfcAnnotation`: SoundScale DBA, SoundFrequency, SoundPressure als `IfcTimeSeries`) | für Messprotokolle geeignet | [V] |

## 7 Prototyp B20: Aufbau und Ergebnisse (Beispieldaten)

**Szenario.** Grundstück 18 × 32 m im WA (IRW 55/40 dB(A)), Straße im Süden. Eigenes Haus 10 × 10 m (Traufe 6,2 m als wirksame Schirmhöhe). Nachbarhaus West mit IO1 (Schlafzimmer OG, 4,3 m) und IO2 (Wohnzimmer EG, 1,5 m). Nachbarhaus Nord mit IO3 (Kinderzimmer OG) und IO4 (Küche mit Essplatz EG). Im Osten ein unbebautes Grundstück mit IO5 als Linie an der Baugrenze, 11 Stützpunkte × 2 Höhen (TA Lärm A.1.3 b). Gartenmauer M1 im Osten, 18 m lang und 2,0 m hoch (ρ = 1). Das eigene Haus hat 8 Öffnungen und 3 Senken. Die WP ist ein **Beispiel**: Monoblock R290, 7 kW, L_WA Tag/Nacht/max = 60/55/63 dB, K_T = 3 dB (LAI-Standard bei unbekannter Tonhaltigkeit), h_s = 0,8 m, Hüllkreis r = 0,45 m, Schutzbereich 1,0/0,5 m, hydraulische Leitung ≤ 20 m. Split-Variante mit R32 und Kältemittelleitung ≤ 15 m.

**Optimierung.** Raster 0,5 m mit 2 304 Punkten, davon 834 zulässig. Die Gründe überlappen: Schutzbereich über der Grenze 564, Leitung zu lang 499, Wandabstand zum Haus 484, keine Ausblasrichtung 400, Öffnungen und Senken 442. Zielfunktion ist die größte kleinste Reserve IRW_N − L_r,N über alle IO. Bei Gleichstand entscheidet die kürzere Leitung, dann die Koordinate. Das Verfahren ist deterministisch, und die Ausgaben sind bei zwei Läufen byte-identisch (md5 geprüft). Laufzeit ca. 8,5 s.

**Ergebnis am Optimum (7,25 m / 1,75 m, Vorgarten), Nacht (L_WA,N = 55 dB):**

| IO | d m | A_div | A_gr | D_Ω | z m | A_bar | L_AT,N | L_r,N | gerundet | Reserve zum IRW 40 | irrelevant | L_r,T | L_AFmax | BWP | LAI |
|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|---:|---:|---:|---:|
| IO1 Schlafzimmer OG | 16,7 | 35,4 | 0,0 | 2,9 | – | 0,0 | 22,4 | 25,4 | 25 | 14,6 | ja | 32,4 | 30,4 | 25,6 | 25,6 |
| IO2 Wohnzimmer EG | 14,2 | 34,0 | 0,0 | 3,0 | – | 0,0 | 23,9 | 26,9 | 27 | 13,1 | ja | 33,8 | 31,9 | 27,0 | 26,8 |
| IO3 Kinderzimmer OG | 34,0 | 41,6 | 0,9 | 3,0 | 1,7 | 15,3 | 0,1 | 3,1 | 3 | 36,9 | ja | 10,0 | 8,1 | 4,4 | 2,2 |
| IO4 Küche EG | 33,9 | 41,6 | 3,0 | 3,0 | 2,4 | 16,2 | −2,9 | 0,1 | 0 | 39,9 | ja | 7,0 | 5,1 | 4,4 | 2,2 |
| IO5 Baugrenze Ost (lautester Stützpunkt) | 13,9 | 33,8 | 0,0 | 2,9 | – | 0,0 | 24,1 | 27,1 | 27 | 12,9 | ja | 34,0 | 32,1 | 27,2 | 27,0 |

A_atm liegt bei allen Pfaden ≤ 0,07 dB. Die Tabelle mit allen Termen (auch z, e, C3, K_met, seitliche Pfade und jede Spiegelquelle mit ρ und Reflexionshöhe) steht in `ausgabe/b20_waermepumpe.md` und `.json`.

**Referenzstandorte:**

| Standort | zulässig | kleinste Reserve zum IRW_N | Befund |
|---|---|---:|---|
| R1 Ostseite vor dem HWR (15/12) | **nein**: HWR-Fenster im R290-Schutzbereich | 6,9 dB | akustisch in Ordnung (IO5: 33,1 dB(A), irrelevant). BWP/LAI zeigen 39,0/39,7 dB(A), LAI Tab. 5 verlangt 12,3 m bei 6,1 m Ist-Abstand → „nicht eingehalten“ |
| R2 Westseite zum Nachbarn (2,5/14) | ja | 5,3 dB | IO2 34,7 → 35 dB(A): Richtwert eingehalten, aber **nicht irrelevant** |
| R3 Nordgarten Mitte (9/26) | ja | 9,4 dB | freie Sicht zu allen IO, BWP/LAI innerhalb ±1 dB |

**Teilraum-Optima (bester zulässiger Ort je Bereich):** Vorgarten 12,9 dB (342 zulässige Punkte), Garten Nord 11,8 dB bei (5,75/20,75) mit 376 Punkten, Westseite 7,3 dB (68 Punkte), Ostseite 7,1 dB bei (16,25/9,25) mit 48 Punkten und der kürzesten Leitung von 7,3 m. Zwischen Ostseite (kurze Leitung) und Vorgarten (+5,8 dB Reserve) besteht ein echter Zielkonflikt, den der Planer mit einer Gewichtung auflösen muss.

**Sensitivität (Reserve in dB):**

| Variante | Optimum | Ostseite (16,25/9,25) |
|---|---:|---:|
| Basis | 12,9 | 7,1 |
| L_WA ±1 dB | 11,9 / 13,9 (exakt linear) | 6,1 / 8,1 |
| K_T = 0 / 6 dB | 15,9 / 9,9 | 10,1 / 4,1 |
| ρ = 1,0 statt 0,8 | 12,9 | 6,5 |
| Wandkonsole h_s = 1,6 m | 13,0 | 6,1 |
| ohne Gartenmauer | 12,9 | **3,7 (Mauer bringt 3,5 dB)** |
| nur Reflexionen 1. Ordnung | 12,9 | 8,5 (die 2. Ordnung in der Gasse kostet 1,3 dB) |

**Oktav- gegen 500-Hz-Rechnung (Beispielspektrum):** Bei freien Pfaden ist die Differenz ≤ 0,2 dB. Hinter dem eigenen Haus ergibt die Oktavrechnung +1,2 dB (Ostseite/IO1) bis **+9,6 dB** (Optimum/IO4, allerdings bei −2,9 dB(A) absolut). Das liegt daran, dass 63/125 Hz kaum abgeschirmt werden. **Die A/500-Hz-Näherung ist bei Schirmwirkung nicht konservativ.** Wo die Abschirmung den Nachweis trägt, muss oktavweise gerechnet werden (TA Lärm A.2.3.1 verlangt das ohnehin).

**Split-Variante (R32):** 674 zulässige Punkte. Das Optimum liegt bei (8,25/3,75) mit 12,3 dB Reserve und 14,3 m Leitung. Die F-Gase-Prüfung ergibt: „zulässig bis 2026-12-31, danach Verbot des Inverkehrbringens“ (Anhang IV Nr. 9 b) [V].

**Grafiken:** `b20_laermkarte.svg` zeigt die Rasterlärmkarte L_r,N in 4,3 m Höhe (0,5-m-Raster) mit Isolinien 35/40/45 dB(A), IO, Gerät, Schutzbereich, Mauer, Öffnungen und Senken. `b20_laermkarte_R1.svg` ist dieselbe Karte für R1: Die 35-dB-Linie überschreitet die Mauer in OG-Höhe. `b20_standortkarte.svg` zeigt die Reserve zum Zielwert IRW − 6 je Rasterpunkt als divergierende Skala; unzulässige Punkte sind schraffiert und nennen den Grund im Tooltip. Die Farben stammen aus einer einheitlichen blauen (sequenziellen) bzw. blau-roten (divergierenden) Skala. Hell- und Dunkelmodus laufen über CSS-Variablen.

**Tests (`tests/test_b20.py`): 17 bestanden.** Geprüft werden: Handrechnung Freifeld (A_div 31,000 dB, D_Ω 2,926 dB, A_gr 0, L = 26,907 dB(A)); Handrechnung Mauer (z = 0,7879 m, C3 = 1,0033, K_met = 0,9934, D_z = 14,17 dB); Grenzwerte von D_z; Wand +3,0 dB und Ecke +6,0 dB bzw. +4,8 dB ohne 2. Ordnung; Monotonie mit dem Abstand samt exakter Differenz 8 → 16 m; Mauer senkt den Pegel um > 5 dB; LAI-Tabelle 5 reproduziert (41 Werte); BWP-Leitfadenbeispiel 47,4/33,4 dB(A); TA-Lärm-Tag 56 → 57,9 dB(A); Rundung nach DIN 1333; R290 schließt R1 aus; F-Gase-Stichtage; das Optimum erfüllt alle Richtwerte und Spitzenpegel und ist maximal; Sensitivität linear; Determinismus; Isolinien am Kreis. Die gesamte Beispiel-Suite ohne `test_b2_b3.py` läuft grün (152 bestanden, 1 übersprungen, einschließlich der 17 B20-Tests). `test_b2_b3.py` lässt sich im System-Python nicht sammeln, weil `ifctester` fehlt; das hängt nicht mit B20 zusammen.

**Nachweisformat:** Das Nachweis-Modul `nachweis.py` existierte beim Bau noch nicht. B20 schreibt deshalb je Regel ein JSON mit `regel, quelle, eingaben[{name, wert, einheit, quelle}], schritte[{formel, zwischenwert, zwischenwert_ungerundet, einheit, beschreibung}], ergebnis, grenzwert, ausnutzung, status`. Das Feld `ausnutzung` ist bei dB-Größen energetisch definiert: 10^(0,1(L − G)).

## 8 Literatur

**Recht und Regelwerke**
- TA Lärm vom 26.08.1998 (GMBl S. 503), geändert durch VwV vom 01.06.2017 (BAnz AT 08.06.2017 B5), mit Anhang; BMUB-Schreiben vom 07.07.2017 (Korrektur Nr. 6.5/7.4). verwaltungsvorschriften-im-internet.de [V].
- LAI: Leitfaden für die Verbesserung des Schutzes gegen Lärm beim Betrieb von stationären Geräten in Gebieten, die dem Wohnen dienen, 3. Aktualisierung, Lang- und Kurzfassung, Stand 28.08.2023, UMK-Umlaufbeschluss 47/2023. lai-immissionsschutz.de [V].
- LAI-Hinweise zur Auslegung der TA Lärm (Fragen und Antworten), Stand 24.02.2023 [V, Auszüge].
- VO (EU) 2024/573 über fluorierte Treibhausgase, Anhang IV. EUR-Lex; Übersicht der EU-Kommission und EHPA-Leitfaden 11/2024 [V].
- Bayerische Bauordnung, Art. 6 (Fassung ab 01.01.2025, GVBl. 2024 S. 619). gesetze-bayern.de; StMB-Rundschreiben „Abstandsflächen von Luftwärmepumpen“ vom 24.07.2023 [V].
- VO (EU) 811/2013 und 813/2013 (Label und Ökodesign), zitiert nach LAI 2023 Tab. 1 [V über LAI].

**Normen**
- ISO 9613-2:1996 / DIN ISO 9613-2:1999-10: Akustik – Dämpfung des Schalls bei der Ausbreitung im Freien – Teil 2. Englischer Originaltext als Exhibit KM-9 im Verfahren EL19-003 der South Dakota PUC (puc.sd.gov) [V]. ISO 9613-2:2024 (2. Ausgabe), Vorwort und Inhalt über die iTeh-Leseprobe [V].
- DIN 45680:1997-03 mit Beiblatt 1; Entwurf DIN 45680:2020-06 (DIN Media); DIN-FAQ zu DIN 45680 vom 18.11.2025 (DIN/TS 45610) [V].
- DIN 45681 (Tonhaltigkeit), EN 12102-1 (Schallleistung WP), EN 378, EN IEC 60335-2-40, DIN 1333 [U, nicht am Text geprüft; DIN 1333 über die LAI-Hinweise V].

**Leitfäden**
- BWP: Leitfaden Schall (Gl. 4.1/4.2, Beispiel 4.3) und Schallrechner (waermepumpe.de/werkzeuge/schallrechner) [V].
- BWP: Leitfaden Außenaufstellung von Wärmepumpen mit brennbarem Kältemittel (A3), 2024 [V].
- Bayerisches Landesamt für Umwelt: Lärmprobleme bei Luftwärmepumpen (Web), Tieffrequente Geräusche bei Biogasanlagen und Luftwärmepumpen, Teil 3 (2011) [V].
- IEA HPT Annex 51, Deliverable 6: Annoyance rating and psychoacoustical analysis of heat pump; Annex 63: Placement Impact on Heat Pump Acoustics [V, Berichte].
- UK DESNZ: Review of Air Source Heat Pump Noise Emissions, Permitted Development Guidance and Regulations (2023), Main Report und Technical Annex [V, nicht ausgewertet].

**Wissenschaftliche Arbeiten (DOI an der Verlagsseite geprüft)**
- Acun, V.; Graetzer, S.; Radivan, M.; Torija Martinez, A. J. (2026): Human response to air source heat pump noise: influence of background noise, operating conditions and acoustic characteristics. *Acta Acustica* 10, 36. DOI 10.1051/aacus/2026032 [V].
- Stürenburg, L.; Braren, H.; Aspöck, L.; Fels, J. (2026): Heat pump noise: Determination and modelling of preference-equivalent levels. *Acta Acustica* 10, 20. DOI 10.1051/aacus/2026016 [V].
- Schmidt, T. et al. (2025): Sound model of an acoustic improved air to water heat pump. *Acta Acustica*. DOI 10.1051/aacus/2025027 [V; Autorenliste U].
- Noise spectral characteristics and noise reduction schemes of screw air-source heat pump: a case study. *Building Simulation* (2023). DOI 10.1007/s12273-023-1085-2 [V].
- Stürenburg, L.; Braren, H.; Aspöck, L.; Fels, J. (2024): Recordings of an Air-to-Water Heat Pump [Datensatz]. Zenodo. DOI 10.5281/zenodo.13365535 [U, aus einer Literaturliste].
- Becker, J. et al. (2026): Sound character and annoyance of ASHP noise (IEA HPT Annex 63), Forum Acusticum 2026 [U, Proceedings-Vorabdruck].

**Rechtsprechung**
- VG Düsseldorf, Urt. v. 10.12.2024 – 3 K 8968/22, ECLI:DE:VGD:2024:1210.3K8968.22.00 [V].
- OVG NRW, Beschl. v. 06.08.2026 – 8 A 134/25 [V, Auszug].
- LG Bielefeld, Urt. v. 09.06.2026 – 1 O 310/24 [V].
- VGH Baden-Württemberg, Beschl. v. 30.01.2019 – 5 S 1913/18 [U].
- OLG Nürnberg 14 U 2612/15 (2017); OLG München 3 U 3538/17 (2018); OLG Bamberg 5 U 176/20 (2021), zitiert nach dem StMB-Rundschreiben 2023 [V über Sekundärzitat].

**Software**
- NoiseModelling, Universite-Gustave-Eiffel/NoiseModelling (GitHub), GPL v3, v6.0.0 (2026) [V].

## Warnungen

1. **Alle Geräte- und Geometriedaten in B20 sind Beispiele.** L_WA, K_T, Spektrum, Schutzbereichsmaße und Leitungslängen müssen aus dem konkreten Herstellerdatenblatt kommen. Das Ergebnis ist kein Schallgutachten und keine Rechtsauskunft.
2. **K_T ist die kritische Unbekannte.** 3 dB mehr (K_T 3 → 6) kosten so viel Reserve wie eine Verdopplung der Quelle. Bei Beschwerden wird gemessen, nicht gerechnet.
3. **Der Pauschalwert „abgewandte Seite 15 dB“ ist nicht sicher.** Um kurze Häuser (10 m) herum ergibt die seitliche Beugung bis zu 6,7 dB mehr als BWP/LAI annehmen. Ein Planer, der die Abschirmung durch das eigene Haus einrechnet, muss geometrisch rechnen, und zwar oktavweise.
4. **Die A/500-Hz-Näherung unterschätzt hinter Schirmen**, im Beispiel um bis zu 9,6 dB bei sehr niedrigen Pegeln. Tieffrequente Anteile (Kompressor, 50/100 Hz) lassen sich weder mit der LAI-Tabelle noch mit ISO 9613-2 sicher prognostizieren. DIN 45680 ist ein Messverfahren im Raum.
5. **Modellgrenzen des Prototyps:** Gebäude als Prismen mit Traufhöhe, konvexe Hindernisse, ebener Boden, seitliche Beugung nur am Direktpfad, Spiegelquellen bis 2. Ordnung (2. Ordnung nur mit Flächen im 6-m-Umkreis), keine Reflexion an der Fassade des Immissionsorts selbst (verbreitete Praxis [U]), Relevanzkriterium z_seitlich ≤ 8·z_oben [U], Boden in der Oktavrechnung weiter nach 7.3.2 (Hybrid) [U]. Keine Vorbelastung und keine weiteren WP in der Nachbarschaft. Die Irrelevanzlogik ersetzt diese Prüfung nur im Regelfall.
6. **Normstand:** Die TA Lärm verweist auf den ISO-9613-2-Entwurf 1997. ISO 9613-2:2024 ändert D_z/K_met und die Beugungskombination. Ein Wechsel kann Ergebnisse um einige dB verschieben und wäre juristisch erst mit einer Anpassung der TA Lärm oder einer Behördenpraxis gedeckt.
7. **F-Gase:** Die Verbote betreffen das **Inverkehrbringen**, nicht den Betrieb bestehender Anlagen. Die Ausnahme „Sicherheitsanforderungen am Standort“ ist eng. Ein R32-Split, der 2026 geplant und 2027 geliefert wird, ist ein Lieferrisiko.
8. **R290 und Holzbau:** Der Schutzbereich betrifft auch Durchführungen und Leerrohre in der Holzrahmenwand. Sie müssen gasdicht sein (Ringspalt), sonst kann Propan in die Installationsebene gelangen [V: Hinweis im BWP-Leitfaden bzw. in Fachquellen; Detaillösung U].
9. **Körperschall:** Wandkonsolen an leichten Holzrahmenwänden von Aufenthaltsräumen sind zu vermeiden. B20 rechnet keinen Körperschall.

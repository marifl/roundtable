# Recherche 16: Fußbodenaufbau mit Höhenausgleich und Durchdringungen an der richtigen Stelle

Stand: 27.09.2026. **[V]** = an Primärquelle, amtlichem Text, Normenverlag oder Herstellerdatenblatt gelesen bzw. maschinell geprüft (IfcOpenShell 0.8.5, `ifcopenshell.validate` mit EXPRESS-Regeln, Schema IFC4X3_ADD2); **[U]** = unsicher, Sekundärquelle, Beispielwert oder eigene Bewertung. DIN-Normen sind kostenpflichtig. Normwerte stehen deshalb hier und in den Beispieldaten nur als **einzelne Kennwerte mit Normverweis**, nicht als Tabellenkopie. Die Crossref-API war aus der Umgebung nicht erreichbar (Proxy: `connect_rejected`). Die DOIs unten sind auf den Verlagsseiten abgelesen. Recherche 08 (TGA, Routing, Licht) wird vorausgesetzt und nicht wiederholt.

Prototypen: `arbeit/beispiele/b14_fussbodenaufbau.py` und `arbeit/beispiele/b15_durchdringungen.py` mit Daten in `daten/b14_fussbodenaufbau.json` und `daten/b15_durchdringungen.json`, Tests in `tests/test_b14.py` und `tests/test_b15.py`. **28 Tests bestanden (15,1 s)**. Die Gesamtsuite ohne `test_b2_b3.py` meldet 69 bestanden und 1 übersprungen. `test_b2_b3.py` bricht ab, weil `ifctester` in dieser Umgebung fehlt; das hat mit B14/B15 nichts zu tun.

## Ergebnis in 5 Punkten

1. **Gleiche OKFF ist ein lösbares Optimierungsproblem, und es gibt eine exakte, schnelle Lösung.** Je Raum wird über die diskreten Wahlen aufgezählt (Handelsdicken der Platten, Wabe 30/60, bis zu 2 Dämmlagen, welche optionalen Schichten aktiv sind). Die stetigen, nivellierenden Schichten (Schüttung, Fließestrich, Mittelbett, Spachtel, Kleberbett) werden je Kombination exakt verteilt: lineares Teilproblem mit einer Gleichung, gelöst durch „Füllen nach Stückkosten“. Beide Beispielvarianten erreichen die Ziel-OKFF in allen vier Räumen auf den Millimeter. Die Toleranzkette über dem Nivellierhorizont bleibt ≤ 1,0 mm, die Übergänge sind kantenfrei (worst case ≤ 1,6 mm) [V Prototyp].
2. **Die Höhe bestimmt meist der Estrich, und dessen Mindestdicke hängt an wenigen Normkennwerten.** Nach DIN 18560-2:2022 gelten die Nenndicken **unabhängig vom Belag**; die frühere Sonderregel für Stein/Keramik (CAF 40, sonst 45 mm) ist gestrichen [V Knauf-Erläuterung]. Heizestrich Bauart A: Nenndicke + Rohr-Außendurchmesser, Rohrüberdeckung bei F4 ≥ 45 mm (CAF-F4 ≥ 40 mm) [V, Fassung 2004 im Wortlaut; 2022 laut Sekundärquellen unverändert U]. Daraus folgen **CAF 57 mm, CT 62 mm bei 17-mm-Rohr**. Die bodengleiche Dusche (2 % × 1 m = 20 mm) und die Rohdeckentoleranz kommen im Bad dazu. **Folge:** Im Bad auf der Bodenplatte fehlen bei 210 mm Aufbauhöhe 30 mm. Der Algorithmus erklärt das und schlägt eine Bodenplatten-Absenkung als Rohbauvorgabe vor [V Prototyp].
3. **Im Holzbau entscheiden Hersteller- und Firmenregeln, nicht die DIN.** Trockenestrich ist kein DIN-18560-Estrich. Die Aufbauten folgen den Systemregeln der Hersteller: Wabe direkt auf der Rohdecke, gebundene Schüttung nie über der Wabe, Leitungen ≤ 10 cm Breite in die Wabe einschneiden, Ausgleichsschüttung 10–60 mm, Gefälle nur mit feuchteunempfindlichem, zementgebundenem Element [V Fermacell; IGG-Merkblatt 5]. Nach dem IGG-Merkblatt sind Holz und Holzwerkstoffe als Untergrund für flüssige und bahnenförmige Verbundabdichtung ungeeignet [V]. Neu ist: Die **Toleranzkette** über dem letzten nivellierenden Layer (Dämmung + Systemplatte + TE + Kleber + Belag ≈ 2,6 mm, Beispielwerte) überschreitet ±2 mm. Der Solver setzt dann automatisch eine Spachtelung auf den Trockenestrich [V Prototyp, Toleranzwerte U].
4. **Durchdringungen scheitern im Holzrahmenbau am gemeinsamen 625-mm-Raster.** Eine DN-100-Fallleitung (da 110, Öffnung Ø 150) nahe einer Rasterachse trifft Deckenbalken *und* Wandständer gleichzeitig. Eine Querbohrung ist nach DIN EN 1995-1-1/NA NCI NA.6.7 unverstärkt nur bis **hd ≤ 0,15 h** zulässig (bei h = 240 mm also 36 mm), mit hro/hru ≥ 0,35 h, lA ≥ h/2 und lz ≥ max(1,5 h; 300 mm) [V BSH-Bemessungsbeispiel, Stucki/forum-holzbau]. Über 50 mm liegt schon ein „Durchbruch“ vor [V FRILO]. DN 50 (Ø 60) quer zur Balkenlage ist damit unzulässig, M25 (Ø 31) ist nur eine Querschnittsschwächung. B15 findet die nächste Achse, die in beiden Rastern frei ist. Liegt sie außerhalb des zulässigen Verschubs, plant B15 Wechsel bzw. Ständerauswechslung als IFC-Bauteile und gibt die Bohrungen mit Leitungs-GUID als BTLx-Bearbeitung aus [V Prototyp].
5. **IFC 4.3 bildet die Durchbruchsplanung vollständig ab, außer der Abschottung.** TGA-Vorschlag `IfcVirtualElement PROVISIONFORVOID` + `Pset_ProvisionForVoid` → freigegebene `IfcOpeningElement` + `IfcRelVoidsElement` + `IfcRelInterferesElements` → Füllung `IfcRelFillsElement` (Manschette) → Umhüllung `IfcCovering WRAPPING` (Dämmschlauch) validiert fehlerfrei [V]. Es gibt **keine `IfcSealing`** und **keinen Firestop-/Manschetten-Typ** in `IfcDiscreteAccessoryTypeEnum`, also USERDEFINED + ObjectType [V]. Rechtlich gilt: In GK 1/2 und innerhalb von Wohnungen ist nach MLAR/LAR 4.1.1 keine Abschottung nötig [V StMB-Text]. Im MFH aus Holz muss der Verwendbarkeitsnachweis die Holzbalkendecke abdecken, sonst wird ein Betonverguss als „Massivdecke“ eingebunden [V Fachartikel].

---

## Teil 1 – Fußbodenaufbau und Höhenausgleich

### 1.1 Beläge inklusive Verlegewerkstoff

| Belag | Belagdicke | Verlegewerkstoff (Dicke) | Summe typ. | R_λ,B-Richtwert | Untergrund-Hinweise | Quelle | Status |
|---|---|---|---|---|---|---|---|
| Feinsteinzeug | 8–20 mm (Standard 9–10; Großformat meist 6–12) | Dünnbett **1–5 mm** (DIN 18157), Kleberbett Handel ca. 4 mm | 13–15 mm | Keramik ≈ 0,01 m²K/W | Großformat: erhöhte Ebenheit (DIN 18202 Tab. 3 Z. 4) vereinbaren | Sopro-Planer, BauNetz Wissen; dielendealer (Handel) | Dünnbett [V], Formate/Summen [U] |
| Naturstein | 10–30 mm | Dünnbett 1–5 / **Mittelbett 5–20 mm** (Sopro MDM 5–30) / **Dickbett 10–30 mm** (DIN 18332; euroFEN Regel 10–20) | 20–60 mm | ≈ 0,01 | **Dickbett nicht auf Calciumsulfatestrich** (Feuchte/Gipstreiben), dort Dünn-/Mittelbett; Dickbett auf Dämmung ersetzt keinen Estrich | Sopro-Planer Kap. 6, euroFEN MB 4, MAPEI-Broschüre | [V] |
| Mehrschichtparkett | 10–15 mm (2-Schicht 10, 3-Schicht 13–15) | vollflächig geklebt ≈ 1 mm | 11–16 mm | 0,07–0,11 (10–15 mm, geklebt) | auf FBH vollflächig kleben; schwimmend „nur bedingt geeignet“ | Holz Reinlein Merkblatt FBH; Weitzer MB-020 | [V Hersteller] |
| Massivparkett | 8 (Mosaik) – 22 mm (Stab/Diele 16, 20, 22) | geklebt ≈ 1 mm | 9–23 mm | Eiche 16 mm 0,085; 20 mm 0,100; 22 mm 0,105 | Buche/Ahorn als Massivparkett auf FBH vom Hersteller nicht freigegeben | Holz Reinlein | [V Hersteller] |
| Parkett schwimmend | 14–15 mm | Trittschallunterlage 2–3 mm | 17 mm | Unterlage erhöht R | auf FBH ungünstig (Luftschicht, Knistern) | dielendealer, Weitzer | [U]/[V] |
| Vinyl geklebt | 2–2,5 (1,6–3) mm | Kleber ≈ 0,5 mm + ggf. Spachtel | 3 mm | gering | sehr ebener Untergrund nötig | dielendealer, bodenfuchs24 (Handel) | [U] |
| Klick-Vinyl (Rigid) | 4–6,5 mm | Unterlage 1–1,5 mm | 5–8 mm | gering | – | Handel | [U] |
| Laminat | 6–12 mm | Unterlage 2–3 mm | 9–12 mm | – | – | Handel | [U] |
| Beton Ciré / Mikrozement | **2–3 mm** (2 Lagen) | Grundierung/Grundierharz 0,5–1 mm, ggf. Armierungsgewebe | 3–4 mm | ≈ 0 | tragfähig, eben, trocken, rissfrei; Restfeuchte CT ≤ 2,3 / 1,5 (FBH), CA ≤ 0,5 / 0,3 CM-% (Beispiel Stoneage); FBH vorher aufheizen; **folgt Estrichfugen** (kann Bewegungsfugen nicht überbrücken); Nassbereich W2-I nur mit Abdichtung darunter | Stoneage-Datenblatt 2021; Artistic Color; Bodentrik | [V Hersteller] |
| Teppich | 5–15 mm | Filz/Unterlage 0–5 mm | – | kann **> 0,15** werden | Beispiel: 8 mm Velours + 5 mm Filz → 0,23 m²K/W (Beispielwerte) | eigene Rechnung | [U] |

**Übergänge:** Nach DIN 18040-2 sind untere Türanschläge und Schwellen unzulässig. Wo sie technisch unabdingbar sind, dürfen sie **höchstens 2 cm** hoch sein [V Bayerisches Staatsministerium, Planungsgrundlagen]. Als Stolperkante nennt das Institut für Fußboden- und Raumausstattung ab etwa 4 mm Höhenunterschied (zitiert beim Parkettverleger) [U]. Der Prototyp verlangt deshalb strenger ΔOKFF + Toleranzen ≤ 2 mm.

### 1.2 Estrich

| Regel | Kennwert (≤ 2 kN/m², Wohnbau) | Quelle | Status |
|---|---|---|---|
| DIN 18560-2:2022-08 Tab. 1, unbeheizt schwimmend | **CT-F4 ≥ 45, CT-F5 ≥ 40 mm; CAF-F4 ≥ 35 mm; CA-F4 45 / F5 40 / F7 35 mm; MA wie CA**, neu MA-F7 | Reschfloor-Normenlexikon, Wikipedia (Tabellenauszug), Knauf-Blog 06/2026, Thermolutz (Fassung 2004) | CT/CA [V]; CAF-F5/F7 in 2022 widersprüchlich (Wikipedia: 35 mm; Fassung 2004: 30 mm) [U] |
| Belagunabhängigkeit (neu 2022) | Die Sonderregel „unter Stein/Keramik CAF ≥ 40, sonst ≥ 45 mm“ ist **entfallen**. Geringere Herstellerdicken gelten als **Sonderkonstruktion** | Knauf-Blog „DIN 18560-2 Erklärung“ | [V] |
| Zusammendrückbarkeit c | c > 5 mm → Nenndicke + 5 mm; Heizestrich: c ≤ 5 mm | Reschfloor; Wico CAF-Hinweise | [V] |
| Heizestrich Bauart A | Nenndicke = Tabellenwert + **Rohr-Außendurchmesser d**; Rohrüberdeckung **F4 ≥ 45 mm, CAF-F4 ≥ 40 mm**; bei anderen Klassen ≥ 30 mm nur mit Eignungsnachweis, nicht nach VOB/C | DIN 18560-2:2004 (Wortlaut, stroy.it-Scan), Wico, Holcim, VDZ-Merkblatt B19, Forum-Verlag-Leseprobe | [V] (Fassung 2004); 2022 laut Reschfloor gleich [U] |
| Heizestrich Bauart B/C | Nenndicke wie unbeheizt (Rohre unter dem Estrich bzw. im Ausgleichsestrich) | VDZ B19, Forum-Verlag | [V] |
| Gussasphalt-Heizestrich | 35 mm (≤ 2 kN/m²), Rohrüberdeckung 15 mm, nur IC10 | Wikipedia, 18560-2:2004 | [V] |
| Beispiel Bezeichnung | „DIN 18560-CT-F4-S70 H45“ = CT-F4 schwimmend 70 mm, Rohrüberdeckung 45 mm | 18560-2:2004, Holcim | [V] |
| Rohrabstand zur Dämmung | Liegt das Rohr 10 mm über der Dämmung (Clips/Matte), soll dieses Maß zur Nenndicke addiert werden | IBF Troisdorf (Gutachterauffassung) | [V] Quelle / [U] normativ |
| Installationsebene (neu 5.1/5.2) | Leitungen auf dem tragenden Untergrund → **separate Installationsebene planen** und in der Konstruktionshöhe berücksichtigen; Ausgleich aus Estrichmörtel, Leichtausgleichsestrich, DEO-Dämmstoff, gebundener oder mechanisch gebundener Schüttung; Druckfestigkeit ≥ 200 kPa bzw. σ10 ≥ 100 kPa; **Dämmplatten als Rohrausgleich**: DEO ≥ 100 kPa, geradlinige Leitungen, **höchstens 2 Installationshöhen, bündig**; mechanisch gebundene Schüttungen nicht neben anderen Ausgleichsschichten | Knauf-Blog (Erläuterung der Änderungen) | [V] (Sekundär, Hersteller) |
| Rohrhülsen an Bewegungsfugen | Der Satz „Rohrhülsen ca. 0,3 m“ ist aus DIN 18560-2 gestrichen und steht weiter in DIN EN 1264 | Knauf-Blog | [V] |
| Randstreifen, Fugen | DIN 18560-2 6.2 Randstreifen, 6.3.3 Estrichfugen (Inhaltsverzeichnis) | DIN-Inhaltsverzeichnis | Existenz [V], Zahlen nicht eingesehen [U] |
| Trockenestrich Fermacell | 2E11 = 2 × 10 mm, 2E22 = 2 × 12,5 mm Gipsfaser; 2E31/32 mit 10 mm HF bzw. MW, 2E35 mit 20 mm MW; **AWB 1: Einzellast 1,0 kN, 1,5/2,0 kN/m²**; 2E22 bis AWB 3; F 60 (F 90 mit Zusatzschicht) auf Holzbalkendecke; W0-I/W1-I; FBH-tauglich (2E22 auf Wärmeleitblechen) | Fermacell-Produktdatenblatt 2E11/2E22, Verarbeitungsanleitung | [V] |
| Waben-Dämmsystem | Wabe 30/60 mm + Wabenschüttung (1,5 kg/l, ca. 45/90 kg/m²); Aufbau 60/90 mm mit ca. 70/115 kg/m²; **Wabe direkt auf der Rohdecke**; Leitungen ≤ 10 cm breit einschneidbar; max. 3 mm überschütten; weiterer Ausgleich darüber nur mit Ausgleichsschüttung; gebundene Schüttung nicht über der Wabe, bei großen Unebenheiten darunter | Fermacell-Datenblatt Estrich-Wabe | [V] |
| Ausgleichsschichten Fermacell | Nivelliermasse 0–20 mm, Ausgleichsschüttung 10–60 (100) mm, gebundene Schüttung 30–2000 mm | Verarbeitungsanleitung | [V] |
| Nassraum-Trockenestrich | Powerpanel TE 2 × 12,5 mm zementgebunden, A1; Gefälle-Set 2.0: 30 mm EPS DEO 200 + 25 mm Powerpanel, ca. 2 % Gefälle, Ablauftopf waagerecht 95 mm, **Einbauhöhe 150 mm auf Massivdecke**; Ablauftopf in der Holzbalkendecke tiefer setzbar; Bodenablauf-Element außen 35 mm | Fermacell/Baucenter-Datenblatt 2014 | [V] (Ausgabe alt) |
| Ebenheit DIN 18202 Tab. 3 | Stichmaße bei 0,1 / 1 / 4 / 10 / 15 m: **Z. 2** (Rohdecke für schwimmenden Estrich) 5 / 8 / 12 / 15 / 20 mm; **Z. 3** (flächenfertige Böden) 2 / 4 / 10 / 12 / 15 mm; **Z. 4** (erhöht) 1 / 3 / 9 / 12 / 15 mm | Bau-Index, Fichtner (erweiterte Tabelle) | [V] (2 Quellen übereinstimmend; 1 Ratgeberseite abweichend) |
| Belegreife (CM-%) [unbeheizt/beheizt] | CT **2,0 / 1,8**, CA **0,5 / 0,3** (Parkett, elastisch/textil); Keramik CT 2,0 / 2,0; CA laut DIN 18560-1 0,5, Handwerk 0,3; Probe aus der unteren Estrichhälfte | TKB-Merkblatt 16 (12/2024), BG BAU Bauportal, IVK-Stellungnahme 2013, Chemotechnik | [V]; Zeilenzuordnung TKB-16 im Auszug nicht eindeutig [U] |
| Schwellenfreiheit / Dusche | Duschplatz niveaugleich, **Absenkung ≤ 2 cm**, Übergang geneigt; Neigung ≤ 2 %, wenn die Dusche Teil der Bewegungsfläche ist; Fläche 120 × 120 (R: 150 × 150) cm | DIN 18040-2 via StMB, HEWI | [V] |
| Abdichtung DIN 18534 | Bodengleiche Dusche ohne wirksamen Spritzschutz = **W2-I**; am Boden **keine Dispersionsabdichtung** (18534-3); Holz/Holzwerkstoffe sind feuchteempfindlich und kein Untergrund für AIV-F/-B; Gefälleflächen mit feuchteunempfindlichem Estrich; Ablaufzone ≥ 1 m über Duschkopfachse, dann Rest W1-I; Rückstau nur 5–10 l aufnehmbar; Anstauhöhe max. 10 cm; **keine Zahl zum Gefälle** („ausreichend“), Vorschlag Fachliteratur ≥ 2 % | IGG-Merkblatt 5 (2018/2020), Oswald/irbnet „Dichter als vorher?“ | [V] |
| Duschrinnen (Hersteller) | Geberit CleanLine Rohbauset DN 40: Estrichhöhe am Einlauf **65–90 mm**, 0,4 l/s, 30 mm Sperrwasser; DN 50: **90–220 mm**, 0,8 l/s, 50 mm Sperrwasser; TECEdrainline h2: superflach 53 / flach 80 / Norm 105 / max 133 mm (0,5 / 0,8 / 0,9 / 1,4 l/s) | Geberit-Katalog, TECE-AT | [V] |

**Holzbau-Befund:** Ein Nassestrich (CAF/CT) auf der Holzbalkendecke bringt rund 120 kg/m² und viel Baufeuchte ein. Übliche Fertighaus-Trockenaufbauten liegen bei 60–115 kg/m² (Waben-System) [V Fermacell] und sind nach etwa einem Tag belegreif [V]. Der Prototyp führt die Masse als Nebenbedingung (Beispiel 180 kg/m², Statik) und die Beschwerung als Schallbedingung (Beispiel ≥ 45 kg/m², vertraglich).

### 1.3 Dämmschichten

| Thema | Kennwert | Quelle | Status |
|---|---|---|---|
| Trittschall Holzdecken, Nachweis | DIN 4109-33:2016 (Bauteilkatalog Holz-/Leicht-/Trockenbau) mit 27 Deckenaufbauten; L′n,w = Ln,w + K1 + K2 (Flanken); Wohnungstrenndecke L′n,w ≤ 50 dB, vorübergehend ≤ 53 dB für Leichtbaudecken nach 4109-33 (soll mit der Überarbeitung entfallen); erhöht (DIN 4109-5) ≤ 45 dB | DAGA 2018 (Rabold u. a.), DAGA 2022, Rigips TA, Forum Holzbau 2017 | [V] |
| Beschwerung | Splitt 80 → 60 mm: +3 dB, 80 → 40 mm: +6 dB; ohne Beschwerung +14 dB (Lattung) bzw. +20 dB (federnde Abhängung); Leitungstrassen < 200 mm mit Splitt verfüllt ohne Abschlag | Wolf Bavaria (Herstellerprüfungen) | [V Hersteller] |
| EFH | öffentlich-rechtlich keine Trittschallanforderung innerhalb der eigenen Wohnung (s. Recherche 08); Schallschutz ist Vertragsqualität (VDI 4100 / DEGA) | 08 | [V] |
| Wärmeschutz Bodenplatte | GModG Anlage 1 Referenzgebäude: U = **0,35 W/(m²K)** für Bodenplatte/Wände gegen Erdreich – das ist ein **Referenzwert**, kein Einzelgrenzwert; Bestand Anlage 7: 0,30 bzw. **0,50** bei Fußbodenaufbau auf der beheizten Seite | gesetze-im-internet (Anlage 1 GModG), GModG-Portal | [V] |
| U-Wert erdberührt | exakt nach DIN EN ISO 13370; im Prototyp vereinfacht mit Rsi 0,17, Rse 0 | eigene Vereinfachung | [U] |
| FBH-Dämmung nach unten | Mindest-R_λ,ins nach DIN EN 1264-4 (Richtwerte 0,75 m²K/W zu beheizt, 1,25 zu unbeheizt/Erdreich) | nicht an der Norm geprüft | [U] |
| Leitungen im Fußboden | Installationsebene planen (DIN 18560-2 5.1); Rohrausgleich s. 1.2; Mindestüberdeckung von Leitungen in Schüttungen **nicht gefunden** (Beispiel: 10 mm) | Knauf-Blog | [V]/[U] |
| Leitungshöhe | h = da + 2 × Dämmung + L × Gefälle (Schwerkraft); Beispiel DN 50, 1,2 m, 1 %: 50 + 12 = **62 mm** | eigene Formel | [U] |

### 1.4 Fußbodenheizung und Belag

| Regel | Kennwert | Quelle | Status |
|---|---|---|---|
| Wärmedurchlasswiderstand des Belags inkl. Unterlage | **R_λ,B ≤ 0,15 m²K/W**; Auslegung 0,10 (Bad 0,0, s. 08) | BVF-Richtlinie 9 (Thermolutz), Weitzer, Reinlein | [V] |
| DIN EN 1264 (2021) | Kennlinien für R_λ,B = 0 / 0,05 / 0,10 / 0,15 m²K/W; Teil 4 Installation 08/2021 (Randdämmung, Dämmschichten, Funktionsheizprotokoll Anhang B) | cci-dialog, FV Gebäudeenergie Dresden | [V] |
| Estrichtemperatur | Warmwasser-FBH: im Bereich der Heizelemente dauerhaft ≤ 55 °C (CT/CA), ≤ 45 °C (AS) | DIN 18560-2:2004 | [V] |
| Holzbelag auf FBH | ≤ 0,15 m²K/W für die ganze Oberbelagskonstruktion; ÖNORM: Holzbelag max. 24 mm; vollflächig kleben | Weitzer MB-020 | [V Hersteller] |

### 1.5 Algorithmus: raumweiser Aufbau als Constraint-Optimierung

**Modell.** Ein Geschoss hat die Ziel-Aufbauhöhe H (OKFF über OK Rohdecke). Je Raum r gibt es eine Rohdeckenabsenkung a_r (Rohbauvorgabe, meist 0), den Belag b_r (Dicke d_b, Verlegewerkstoff [nenn, max]), die Leitungen L_r im Aufbau, eine Dusche (Gefälle Δh) und die FBH (System, Rohr-da d). Der Aufbau ist eine Slot-Folge von unten nach oben, je Variante im JSON definiert, z. B. *Abdichtung – Installationsebene – Wärmedämmung – Trittschall/FBH-Träger – Estrich – [Spachtel] – [AIV] – Verlegewerkstoff – Belag*.

- Diskrete Variablen: Belegung jedes optionalen Slots (aus / Material / Handelsdicke, bis zu 2 Lagen).
- Stetige Variablen x_i ∈ [lo_i, hi_i] (ganze mm): nivellierende Schichten und Verlegewerkstoff. Die Grenzen lo_i hängen von den Regeln ab:
  - Estrich nass: lo = max(e_min + d; d + ü_min) + Δh (+ t_Rohdecke, falls kein anderer Layer ausgleicht); hi = lo_0 + Mehrdicke.
  - Installationsebene aus Schüttung: lo = max(Material-min, h_Leitung + Überdeckung); die tiefste nivellierende Schicht bekommt + t_Rohdecke (Toleranz nach DIN 18202 Z. 2).
- Gleichung: Σ fest + Σ x_i = H + a_r.
- Harte Nebenbedingungen: Dämmplatten bündig (0 ≤ d_Platte − h_Leitung ≤ 5 mm, ≤ 2 Höhen); Σc ≤ 5 mm (Heizestrich); U ≤ U_max; R_ins ≥ R_min; m′ ≤ m′_max; m′ unter Trittschall ≥ Beschwerung; Wabe auf Rohdecke; Trockenestrich nur über nivellierender Schicht; **Toleranzkette** Σ tol_j über dem obersten nivellierenden Layer ≤ 2 mm.
- Ziel: min w_m·m′ + w_k·Kosten + w_l·Lagenzahl. Gleichstand wird über die Textform der Kombination aufgelöst, das Ergebnis ist also deterministisch.
- Weiche Regeln (Meldung statt Ausschluss): Belag–Untergrund-Eignung (zulässig / Herstellerfreigabe / unzulässig), R_λ,B ≤ 0,15, Gefälle ≤ 20 mm (DIN 18040-2), Rinneneinbauhöhe, GModG-Dämmung der Leitungen, Belegreife, Übergänge (Fuge/Profil).

**Warum exakt:** Für feste diskrete Wahl ist das Restproblem ein lineares Programm mit einer Gleichung und Boxgrenzen. Das Optimum füllt die Resthöhe in der Reihenfolge der Kosten je mm (fraktionaler Rucksack). Die Aufzählung über die diskreten Wahlen ist klein: Variante A 405, Variante B 72 Kombinationen je Raum. Laufzeit: 3–4 s je Variante in reinem Python.

```text
für jeden Raum r:
    estrich ← Standard; wenn bodengleiche Dusche und Estrich feuchteempfindlich: estrich ← Gefällebereich-Estrich
    für jede Kombination k der diskreten Slots (Handelsdicken, an/aus):
        S ← Schichtfolge(k, estrich, Belag, AIV falls Dusche)
        setze Grenzen [lo, hi] der stetigen Schichten:
            Estrich: lo ← max(e_min + d, d + ü_min) + Δh
            Leitungsträger: bündig prüfen (Platte) oder lo ← h_Leitung + Überdeckung (Schüttung)
            tiefste nivellierende Schicht: lo ← lo + t_Rohdecke
        wenn harte Regel verletzt: verwerfe(k, Grund); weiter
        R ← H + a_r − Σ feste Dicken
        verteile R: alle x_i ← lo_i, Rest nach Stückkosten (w_m·ρ + w_k·€/mm) aufsteigend bis hi_i
        wenn Rest ≠ 0: verwerfe(k, "Höhe zu klein/groß"); weiter
        prüfe U, R_ins, m′, Beschwerung, Toleranzkette → sonst verwerfe
        merke k, falls Zielwert kleiner
    wenn kein k zulässig:
        [H_min, H_max] ← Spannweite der erreichbaren Höhen aller Kombinationen
        melde „fehlen H_min − H mm → Rohdecke absenken / H erhöhen / dünneres System“ + häufigste Gründe
    weiche Regeln prüfen, Hinweise sammeln
Geschoss: Nachweis |OKFF_r − H| + tol_r ≤ 2 mm; Übergänge: |ΔOKFF| + tol_a + tol_b ≤ 2 mm, Fuge/Profil
```

**Erweiterung [U]:** Sollen Räume gekoppelt werden, etwa durch ein gemeinsames Estrichfeld ohne Fuge, gleiche Dämmdicke im Flur und in den Zimmern oder gemeinsam bestellte Plattenmengen, wird das Problem ein kleines MILP. Dann lohnt ein Löser (OR-Tools CP-SAT, Apache-2.0, oder HiGHS über PuLP, MIT). Der Rechenweg bleibt derselbe, nur die Kopplungsgleichungen kommen hinzu.

### 1.6 Prototyp B14 – Ergebnisse (Beispielwerte)

**Variante A:** EG auf Stahlbeton-Bodenplatte, CAF-Heizestrich Bauart A (Rohr 17 mm), Ziel **210 mm**, Rohdeckentoleranz 8 mm, U_max 0,30 (Beispiel). Nachweis gleiche OKFF: **erfüllt**.

| Raum | Estrich | Schichten von unten nach oben [mm] | OKFF | m′ kg/m² | R_λ,B | R_ins | U | CM max |
|---|---|---|---|---|---|---|---|---|
| Wohnen (Parkett 14 geklebt) | CAF-F4 | Abdichtung 5 + EPS DEO 35 + EPS DEO 60 + EPS-T 30-2 (28) + CAF 67 + Kleber 1 + Parkett 14 | 210 ± 0,6 | 152 | 0,113 | 3,44 | 0,257 | 0,3 |
| Küche (Feinsteinzeug 10) | CAF-F4 | Abdichtung 5 + **DEO 35 bündig zu PWC/PWH 34 mm** + DEO 60 + EPS-T 28 + CAF 68 + Dünnbett 4 + Fliese 10 | 210 ± 1,0 | 173 | 0,013 | 3,44 | 0,264 | 0,3 |
| Bad (Naturstein 20, Mittelbett, Dusche) | **CT-F4** | (Rohdecke −30) Abdichtung 5 + DEO 25 + DEO 60 + EPS-T 28 + **CT 90** + AIV 2 + Mittelbett 10 + Naturstein 20 | 210 ± 0,5 | 263 | 0,019 | 3,16 | 0,284 | 2,0 |
| Flur (Beton Ciré 3) | CAF-F4 | Abdichtung 5 + **geb. Schüttung 46** (M25 + 10 + Toleranz 8) + DEO 20 + DEO 50 + EPS-T 28 + CAF 57 + Grundierung 1 + Mikrozement 3 | 210 ± 0,8 | 145 | 0,004 | 3,39 | 0,269 | 0,3 |

Handrechnungen, als Tests abgesichert:
- CAF-Heizestrich: max(35 + 17; 17 + 40) = **57 mm**.
- CT: max(45 + 17; 17 + 45) = **62 mm**.
- Bad: 62 + 20 (Gefälle 2 % × 1 m) + 8 (Toleranz) = **90 mm**, am Tiefpunkt 70 mm.
- Rinne DN 50: Estrichhöhe am Einlauf 188 mm, liegt in 90–220 ✓.
- Parkett: R = 0,014/0,13 + 0,001/0,20 = **0,1127 m²K/W**.

**Konfliktfall (Test):** Ohne Absenkung meldet B14 für das Bad: „Kein zulässiger Aufbau für H = 210 mm. Mindestens erreichbar: 240 mm (fehlen 30 mm) → Rohdecke im Raum um ≥ 30 mm absenken …“. Die Absenkung von 30 mm ist deshalb als Rohbauvorgabe im JSON gesetzt.
Im Flur nimmt die Schüttung die 8 mm Toleranz auf, und der Estrich bleibt auf 57 mm. Die Alternative mit einer bündigen DEO-Platte von 25 mm bräuchte 65 mm Estrich. Beide Lösungen wiegen etwa gleich viel (+16 kg/m² Schüttung gegenüber +16 kg/m² Estrich); die Schüttung gewinnt bei den Beispielgewichten über die Kosten.

**Variante B:** OG auf Holzbalkendecke (OSB 22 auf KVH 100/240), Trockenaufbau mit Beschwerung und FBH-Trockensystem, Ziel **160 mm**, Toleranz 4 mm, m′ ≤ 180 kg/m², Beschwerung ≥ 45 kg/m² (Beispiele). Nachweis: **erfüllt**.

| Raum | Estrich | Schichten von unten nach oben [mm] | OKFF | m′ | R_ins |
|---|---|---|---|---|---|
| Wohnen | TE Gipsfaser 25 | Wabe 30 + Ausgleichsschüttung 24 + HF-TSD 39 + FBH-Systemplatte 25 + TE 25 + **Spachtel 2** + Kleber 1 + Parkett 14 | 160 ± 0,6 | 109 | 1,89 |
| Küche | TE Gipsfaser 25 | **Wabe 60 (Leitungen 88 mm breit eingeschnitten)** + Ausgleichsschüttung 15 + HF 19 + Systemplatte 25 + TE 25 + Spachtel 2 + Dünnbett 4 + Fliese 10 | 160 ± 1,0 | 165 | 1,39 |
| Bad | **TE zementgebunden 25** | Wabe 30 + Ausgleichsschüttung 19 + HF 29 + Systemplatte 25 + TE-Z 25 + AIV 2 + Mittelbett 10 + Naturstein 20 | 160 ± 0,5 | 161 | 1,61 |
| Flur | TE Gipsfaser 25 | geb. Schüttung 45 (Leerrohr) + Wabe 30 + HF 29 + Systemplatte 25 + TE 25 + Spachtel 2 + Grundierung 1 + Mikrozement 3 | 160 ± 0,8 | 109 | 2,04 |

Hinweise aus B14 (Auszug): „Feinsteinzeug/Mikrozement auf Gipsfaser-TE nur mit Herstellerfreigabe“; „Rinnenablauf in die Balkenlage absenken → Durchbruch/Wechsel prüfen (B15)“; „Trockenestrich: keine CM-Belegreife“. Übergänge: ΔOKFF 0, worst case 1,3–1,6 mm, jeweils mit Fuge und höhengleichem Profil bei Mikrozement/Parkett/Fliese.
**Konfliktfall (Test):** Liegt die DN-50-Leitung der Rinne im Aufbau statt in der Balkenlage (62 mm Installationshöhe), ist im 160-mm-Trockenaufbau kein Aufbau zulässig („fehlen …“).

**IFC:** Je Variante 1 `IfcSlab` (BASESLAB bzw. FLOOR) mit Schicht-Usage, 4 `IfcSpace`, 4 `IfcCovering FLOORING` mit `IfcMaterialLayerSetUsage` (AXIS3, POSITIVE) und `IfcRelCoversSpaces`, dazu `Pset_SpaceCoveringRequirements`, `Pset_CoveringCommon`, eigenes Pset `B14_Fussbodenaufbau` sowie ein `IfcWasteTerminal FLOORTRAP` für die Rinne. `ifcopenshell.validate` mit EXPRESS-Regeln: **0 Fehler**. Die Dateien sind byte-identisch auch bei anderem `PYTHONHASHSEED` (Test).

---

## Teil 2 – Rohrdurchmesser und Durchdringungen

### 2.1 Nennweiten und Außendurchmesser

| Leitungsart | Bezeichnung → Außen-/Innendurchmesser | Quelle | Status |
|---|---|---|---|
| Trinkwasser Mehrschichtverbundrohr | 16×2 (di 12, 0,113 l/m), 20×2 (16; 0,201), 26×3 (20; 0,314), 32×3 (26; 0,531), 40×3,5 (33), 50×4 (42), 63×4,5 (54); Variante 20×2,25 (di 15,5) | Hornbach-Datenblatt (Hersteller-MSVR), Becker Plastics, Präsentation EN 806-3 | [V Hersteller] |
| 3-l-Regel (08) mit diesen Werten | 3 l ≈ 26 m 16×2 bzw. 15 m 20×2 | eigene Rechnung aus l/m | [V] Rechnung |
| FBH-Rohr | 14×2, 16×2, 17×2 (PE-Xa, PE-RT, PE-Xc/Al) | Becker Plastics (14×2, 16×2); 17×2 in Beispielen zu DIN 18560 | [V]/[U] |
| Abwasser HT / Schallschutzrohr | DN/OD 32, 40, 50, 75, 90, 110, 125, 160, 200 (DN 70 ≙ 75, DN 100 ≙ 110); z. B. RAUPIANO PLUS di 71,2 / 85,6 / **104,6** mm; Skolan dB DN 58/78/90/110/135 (Außendurchmesser!) mit di 50/69/81/99,4 | REHAU TI (Tab. 03-1), Ostendorf | [V] |
| Formel für die Dimension | Anschlusswerte/Qww = K·√ΣDU (s. 08); DN 90 als Fallleitung für Gebäude bis 3 WE (Herstellerhinweis, ÖNORM-Kontext) | REHAU AT | [V Hersteller] / [U] für DE |
| Lüftung flexibel | ComfoTube 75: da 75 / di 63, empfohlen max. **28 m³/h** (2,5 m/s), Nennluftmenge 30; ComfoTube 90: 90 / 74, 39 bzw. 50 m³/h; min. Biegeradius 1 × D; LVS 75: 30 m³/h je Strang, Biegeradius 200 mm, **Mindestabstand 120 mm zwischen Rohren in Betondecken**, Zuleitung DN 125/160 | Zehnder-Spezifikation, Heinze/Planungshandbuch | [V Hersteller] |
| Lüftung Flachkanal | 130 × 52 mm, 45 m³/h | Heinze | [V] |
| Elektro-Leerrohr | M-Bezeichnung = Außendurchmesser (DIN EN 61386): M20 innen 14,1 (flexibel) / 16,9 (starr); M25 18,3 / 21,4; Klassifizierung „3321“ = mittlere Druck-/Schlagfestigkeit | GEWISS-Daten (Sanos), EN-61386-Klassifizierung | [V Hersteller] |
| Netzwerk/Glasfaser | CAT6 ≈ 6,3 mm → M16; Glasfaser-Leerrohr nach GIA (s. 08) | Meteor-Tabelle (Handel) | [U] |

### 2.2 Leitungsdämmung nach GModG Anlage 8 (Prüfung aus 08)

Der Einzelnormtitel lautet jetzt „Anlage 8 GModG“ [V gesetze-im-internet]. Wortlaut Nr. 1 a, bezogen auf λ = 0,035 W/(m K) bei 40 °C Mitteltemperatur [V]:
- aa) di ≤ 22 mm: **20 mm**
- bb) di 22–35 mm: **30 mm**
- cc) di 35–100 mm: **gleich di**
- dd) di > 100 mm: **100 mm**
- ee) in Wand-/Deckendurchbrüchen, Kreuzungen, Verbindungsstellen und an zentralen Verteilern: **halber Wert**
- ff) Wärmeverteilleitungen zwischen beheizten Räumen **verschiedener** Nutzer: halber Wert; gg) davon im **Fußbodenaufbau: 6 mm**
- hh) an Außenluft: doppelter Wert

Ausnahmen: b) Wärmeverteilleitungen in beheizten Räumen eines Nutzers mit frei liegender Absperrung; c) **Warmwasser-Stichleitungen ≤ 3 l** ohne Zirkulation und Begleitheizung in beheizten Räumen. Kälte/Kaltwasser von RLT-/Klimaanlagen: 9 mm (di ≤ 22) bzw. 19 mm [V].

**Folge für den Fußboden:** Trinkwasser kalt und Abwasser haben keine GModG-Anforderung (Schutz nach DIN 1988-200 gegen Erwärmung und Tauwasser [U]). Die Warmwasser-Stichleitung im Beispiel ist ausgenommen. Umgesetzt ist das in `b14.gmodg_mindestdaemmung()` mit 10 Testfällen.

### 2.3 Durchdringungsregeln

| Bauteil / Fall | Regel mit Kennwert | Quelle | Status | Umsetzung B15 |
|---|---|---|---|---|
| Deckenbalken, Querbohrung ≤ 50 mm | „Querschnittsschwächung“, Nettoquerschnitt nachweisen | FRILO HO12 (zitiert NA) | [V] | ✓ M25 Ø 31 |
| Deckenbalken, Durchbruch > 50 mm, unverstärkt (NCI NA.6.7) | hd ≤ **0,15 h**; hro, hru ≥ **0,35 h**; lA ≥ **h/2**; lz ≥ **max(1,5 h; 300 mm)**; rechteckig a ≤ 0,4 h; Gruppen (lz < 1,5 h) unzulässig | Studiengemeinschaft Holzleimbau/IDH-Bemessungsbeispiel, Stucki (forum-holzwissen) | [V] | ✓ DN 50 Ø 60 > 36 → Verstoß |
| künftiger EC5 (prEN 1995-1-1) | unverstärkt d ≤ 0,3 h (e ≤ 0,1 h) bzw. 0,2 h; lz ≥ 1,5 h ≥ 300 mm; lA ≥ h/2; hru ≥ 0,15 h; **Vollholz verstärken** | forum-holzwissen (Entwurfsstand), Massaro/Malo WCTE | [V] Entwurf / [U] Endfassung | Warnung |
| Senkrechte Leitung durch Balkenlage | nie durch den Balken; Öffnung im Gefach mit Randabstand (Beispiel 20 mm); sonst **Wechsel**: Balken unterbrechen, 2 Wechsel auf die Nachbarbalken, Nachweis Stich-/Wechselbalken und Anschlüsse (Balkenschuhe) | mb AEC S295 (Modulbeschreibung), Praxis | [V] Prinzip / [U] Randabstand | ✓ |
| Ständer (Wandtafel) | EC5 ohne eigene Bohrregel (s. 08); **Firmenregel** (Platzhalter: Ø ≤ 25 % der Ständertiefe, mittig); sonst Ständer auswechseln (Riegel oben/unten) oder Vorwand | – | [U] → Regnauer | ✓ |
| Installationsebene/Vorwand | Leitungen vom Tragwerk trennen, zentrale Trasse/Schacht, zugänglich, Platzreserven | TU München „Holzbau der Zukunft“ (Zuschnitt 71); CLT_Plumbing_Design (FFG) | [V] | Hinweis |
| Luftdichtheitsebene (DIN 4108-7) | Systemmanschetten: pro clima KAFLEX 6–12 mm (Kabel), ROFLEX 20: Ø 15–30, **ROFLEX 100: Ø 100–120 mm**, ROFLEX SOLIDO, Dunstrohrmanschette ROFLEX exto; Leerrohre innen mit STOPPA (16–40 mm) abdichten | pro clima Datenblätter/Anwendungshinweise | [V Hersteller]; Siga/Ampack nicht geprüft [U] | ✓ ROFLEX 100 für da 110 |
| Strangentlüftung über Dach (DIN 1986-100 6.5) | jede Schmutzwasser-Fallleitung über Dach, in Anlagen ohne Fallleitung ≥ 1 Lüftung DN 70; Mündung nahe Aufenthaltsräumen **≥ 1 m über Fenstersturz oder ≥ 2 m seitlich**; Umlenkungen 45° | IZEG TI 2-1/2-5, tga-praxis (Ishorst) | [V] | ✓ Fensterprüfung |
| Mündung / Abdeckung | IZEG (2014): Abdeckungen zulässig, wenn ≤ 90° Umlenkung und Austritt ≥ 1,5 × Querschnitt; alwitra (zitiert ältere Fassung): „Abdeckungen dürfen nicht eingesetzt werden“, Mündung ≥ … cm über Dachfläche (im Auszug unvollständig) | IZEG, alwitra | [V] beide / Widerspruch → E DIN 1986-100:2025-06 prüfen | Warnung |
| Brandschutz MLAR/LAR (Bayern) | 4.1.1: keine Anforderung in **GK 1/2, innerhalb von Wohnungen**, NE ≤ 400 m² in ≤ 2 Geschossen; 4.1.2 Abschottung gleicher Feuerwiderstand oder Schacht; 4.1.3 Abstand nach Nachweis, sonst **≥ 50 mm**; 4.2 feuerhemmende Wände: Einzelkabel/-bündel ≤ 50 mm, nichtbrennbare Rohre, Spalt ≤ 50 mm; 4.3.1 nichtbrennbare Rohre ≤ **160 mm**, brennbare ≤ **32 mm**, Abstand 1 × bzw. 5 × d, Bauteildicke 80/70/60 mm, Mörtelverguss; 4.3.2 Spalt ≤ 50 mm (Mineralfaser) / ≤ 15 mm (Intumeszenz); 4.3.3 gedämmte Rohre 50 mm Abstand, 500 mm nichtbrennbare Dämmung beidseitig; 4.3.4 Rohre ≤ 110 mm in Schlitzen | StMB „Leitungsanlagen-Richtlinie MLAR“ (Fassung 10.02.2015, geändert 03.09.2020), ZVEI/VdS-Kommentar, Promat | [V] | ✓ Regel GK |
| Abschottung in Holzbalkendecken | keine allgemeingültige Lösung; Nachweis gilt nur für die geprüfte Deckenkonstruktion (Prüfung Brand von oben und unten); Alternative **Betonverguss** als Massivdecke des Nachweises, gegen Durchfallen gesichert; Abstand zur brennbaren Laibung ≥ 10 cm empfohlen (Nachweise F30 oft 50 mm) | tga-fachplaner.de (2020), IRB-Forschungsbericht „Leitungsdurchführungen im Holzbau“ | [V] Fachartikel | Text in Regel |
| MHolzBauRL | Neufassung Bauministerkonferenz 09/2024; in Bayern Vorabanwendung über Abweichung (Art. 63 BayBO), als Technische Baubestimmung gilt bis zur BayTB-Fortschreibung die Fassung 10/2020 | Bayerische Ingenieurekammer-Bau (Schreiben StMB 26.11.2024) | [V] | Hinweis |
| Schall in Durchführungen | körperschallentkoppelt (Dämmschlauch, Schellen mit Einlage, keine starre Verbindung, Gefach mit Mineralwolle stopfen); im EFH vertraglich | Hersteller (REHAU: Prüfung DIN EN 14366), 08 | [V]/[U] | ✓ IfcCovering WRAPPING |
| Vorwand (Geberit Duofix) | Fußbodenaufbau **0–25 cm**, WC-Montagehöhe 41–46 cm einstellbar, Anschlussmaße EN 33, Anschlussbogen **Ø 90** mit Übergang 90/110; Waschtisch Befestigungsabstand 5–38 cm, UP-Siphon ± 3 cm, Anschluss Ø 50; Duschelement Wandablauf: Estrichhöhe am Einlauf 65–90 / 90–250 mm, Fliesenaufbau Boden 2–26 mm | Geberit-Katalog DE/CH | [V] |
| WC-Anschlussachse über OKFF | im Beispiel 22 cm | nicht belegt | [U] → Hersteller-Montageanleitung | Eingabe |

### 2.4 IFC-Mapping (maschinell geprüft, IFC4X3_ADD2, IfcOpenShell 0.8.5)

| Konzept | IFC | Befund | Status |
|---|---|---|---|
| Aussparungswunsch TGA | `IfcVirtualElement` PROVISIONFORVOID + `Pset_ProvisionForVoid` (VoidShape, Width, Height, **Diameter**, Depth, System) | Enum und Pset im Schema vorhanden; ohne Material (s. 08) | [V] |
| Freigegebene Öffnung | `IfcOpeningElement` OPENING/RECESS, `IfcRelVoidsElement` je Bauteil (Platte, Balken) | 1 Öffnung je durchdrungenem Bauteil, im Holzbau je Schicht | [V] |
| Durchdringungsbeziehung | `IfcRelInterferesElements` (RelatingElement, RelatedElement, InterferenceGeometry, **InterferenceType**, **ImpliedOrder**, InterferenceSpace) | ImpliedOrder TRUE: Bauteil wird geschnitten; InterferenceType frei („Durchdringung“, „Clash“) | [V] |
| Manschette / Füllung | `IfcRelFillsElement` (RelatingOpeningElement → **RelatedBuildingElement: IfcElement**) | nimmt auch `IfcDiscreteAccessory` auf; semantisch für Türen/Fenster gedacht → Projektkonvention [U] | [V] Schema |
| Abschottung / Manschette als Typ | `IfcDiscreteAccessory` USERDEFINED, ObjectType „Brandschutzmanschette“ / „Luftdichtheitsmanschette“ | **kein** FIRESTOP/SLEEVE in `IfcDiscreteAccessoryTypeEnum`; **keine `IfcSealing`** | [V] |
| Dämmschlauch, Schutzrohr | `IfcCovering` **WRAPPING** bzw. **SLEEVING** (INSULATION, MEMBRANE vorhanden) + `IfcRelCoversBldgElements` am Rohr; Brandklasse in `Pset_CoveringCommon.FireRating` | Enum-Werte vorhanden | [V] |
| Rohrdurchmesser | `Pset_PipeSegmentTypeCommon`: **NominalDiameter, InnerDiameter, OuterDiameter**, WorkingPressure, PressureRange, TemperatureRange, Length; Occurrence: `Pset_PipeSegmentOccurrence` (**Gradient**, InvertElevation, Colour) | Typ-Pset muss über `HasPropertySets` am Typ hängen. Mit `IfcRelDefinesByProperties` meldet der Validator einen Regelverstoß (im Prototyp gefunden und behoben) | [V] |
| Kanaldurchmesser | `Pset_DuctSegmentTypeCommon`: CrossSectionShape, **NominalDiameterOrWidth, NominalHeight**, WorkingPressure, LongitudinalSeam, Reinforcement … | – | [V] |
| Port | `IfcDistributionPort` PIPE/DUCT/CABLE…, FlowDirection SOURCE/SINK/SOURCEANDSINK, SystemType; `Pset_DistributionPortTypePipe` (NominalDiameter, OuterDiameter, ConnectionType …), `Pset_DistributionPortTypeDuct` (NominalWidth/Height) | `util.system.get_connected_to` folgt der Fließrichtung und liefert nur die Abströmseite; für die Nachbarn `get_connected_from` ergänzen | [V] |
| Leerrohr | `IfcCableCarrierSegment` CONDUITSEGMENT + `Pset_CableCarrierSegmentTypeConduitSegment` (NominalDiameter, IsRigid …) | – | [V] |
| System | `IfcDistributionSystem` WASTEWATER / SEWAGE / VENT / DOMESTICCOLDWATER …, `IfcRelAssignsToGroup`, `IfcRelServicesBuildings` | – | [V] |
| Wechsel | `IfcBeam` JOIST für Balken; Wechsel = `IfcBeam` USERDEFINED/ObjectType „Wechsel“ | **kein TRIMMER** in `IfcBeamTypeEnum` | [V] |
| Formteil | `IfcPipeFitting` JUNCTION (Abzweig) mit 3 Ports | – | [V] |
| Koordination | Ablauf: TGA liefert PROVISIONFORVOID; der Holzbau prüft nach 2.3 und gibt als BCF-Topic mit Viewpoint und Komponenten-GUIDs zurück (Annahme, Verschiebung, Ablehnung). Bei Annahme erzeugt er `IfcOpeningElement` und Fertigungsbearbeitung. BCF ist das Kommunikations-, IFC das Modellformat | eigene Bewertung auf Basis 08 | [U] |

### 2.5 Werkseitige Umsetzung (BTLx, WUP) und Rückverfolgung

| Punkt | Befund | Quelle | Status |
|---|---|---|---|
| BTLx-Versionen | Doku BTLx 2.1 (29.06.2022), 2.2 (04.03.2024); XSD BTLx 1.1 enthält neben Stabbearbeitungen **CompositeElement/-Layer/-Module, MillContour, SawContour, NailContour, LockoutArea, GlueArea, PlasterArea** (Element-/Tafelbearbeitung) | design2machine.com (Suchindex; Seite aus der Umgebung gesperrt) | [V] Index / Details [U] |
| Drilling-Parameter | StartX, StartY, Angle, Inclination, **DepthLimited, Depth, Diameter** (+ ReferencePlaneID, UserAttributes) | compas_timber 2.2.0 (`fabrication/drilling.py`, MIT), BTLx-Schema-Auszug | [V] |
| Slot / Pocket | Slot: Orientation, StartX/Y, StartDepth, Angle, Inclination, Length, Depth, Thickness, AngleRefPoint …; Pocket: StartX/Y, StartDepth, Angle, Inclination, Slope, Length, Width, InternalAngle, TiltRef/Opp/Start/EndSide, MachiningLimits | compas_timber 2.2.0 | [V] |
| WUP (Weinmann) | cadwork-Export `*.wup` je Hülle; Bohrungen ab einem Grenzdurchmesser (z. B. ≥ 70 mm bei 68-mm-Dosenbohrer) werden gefräst; freie Bearbeitungen über Achsen mit Kennung (z. B. PAF = Ausfräsung); Sperrflächen für Säge/Fräse | cadwork „Manual Weinmann“ | [V] |
| Dietrich's | „Maximaler Durchmesser für Bohrungen“: größere Bohrungen werden als runde Fräsung übergeben; Wandbearbeitung über Materialfunktionen (Platte als Ausnehmung, Eckenrundung bis Kreis) | docs.dietrichs.com | [V] |
| Rückverfolgung | BTLx: Leitungs-GUID als `UserAttribute` an der Bearbeitung (B15 so umgesetzt); WUP: kein dokumentiertes Freitextfeld gefunden | eigene Umsetzung | [V] BTLx / [U] WUP |

### 2.6 Prototyp B15 – Ergebnisse (Beispielwerte)

Leitung SW-01: Schallschutzrohr DN 100 (da 110, di 104,6 mm), Achse x = 3150 / y = 2100 mm. Öffnung Decke/Wand **Ø 150 mm** (110 + 2 × (9 + 10) = 148 → 150), Dach **Ø 130 mm**.
- **Rasterkollision:** Die Achse liegt 25 mm neben der Balken- *und* Ständerachse 3125. Die nächste in beiden Rastern freie Achse ist 3270 mm; 120 mm Verschub sind mehr als die zulässigen 100 mm → Strategie **Wechsel**. Mit zulässigen 150 mm wählt B15 die Verschiebung ohne Wechsel (Test).
- **D1 Holzbalkendecke:** Balken 5 wird zwischen y = 1905 und 2295 unterbrochen. Zwei Wechsel 100/240 bei y = 1955/2245 laufen auf die Nachbarbalken, dazu Stichbalken [0–1905] und [2295–4500], Hinweis auf den statischen Nachweis. Keine Abschottung, weil GK 1.
- **D2 Ständerwand:** Ständer 5 trifft die Öffnung; 150 mm sind mehr als 25 % der Tiefe von 160 mm (Platzhalterregel) → Ständer auswechseln mit 2 Wechselriegeln, Alternative Vorwand.
- **D3 Dach:** Die Öffnung liegt zwischen den Sparren. Manschette **ROFLEX 100**. **Verstoß DIN 1986-100:** Das Dachfenster liegt 1,6 m seitlich und nur 0,3 m unter der Mündung. Vorschlag: Mündung auf 7,30 m (+0,70 m) oder Abstand ≥ 2 m (fehlen 0,4 m).
- **BD-1 DN 50 quer zu den Balken:** Ø 60 > 0,15 · 240 = 36 mm → unzulässig, parallel zu den Balken führen (Anschluss an B14 Variante B). **BD-2 M25:** Ø 31 ≤ 50 mm → Querschnittsschwächung, mittig, Drilling freigegeben.
- **IFC:** 4 PROVISIONFORVOID, 4 `IfcOpeningElement` + 4 `IfcRelVoidsElement` + 4 `IfcRelInterferesElements`, 1 `IfcRelFillsElement` mit Luftdichtheitsmanschette, 2 Wechsel, 2 Stichbalken, 2 Wechselriegel, 3 Rohrsegmente + Abzweig JUNCTION mit 3 Port-Verbindungen, Dämmschlauch als `IfcCovering WRAPPING`. `validate` mit EXPRESS-Regeln: **0 Fehler**. Zwei zunächst gefundene Regelverstöße sind behoben: Axis ohne RefDirection und Pset am Typ über RelDefines.
- **BTLx-artige Ausgabe:** 5 Parts mit `Drilling` (D1, D2 Süd/Nord, D3, BD-2), bauteillokale StartX/StartY, `UserAttribute LeitungGUID` = GlobalId der Fallleitung. Das BTLx-Schema ist **nicht validiert**, weil die XSD aus der Umgebung nicht erreichbar war.

---

## Korrekturen und Warnungen

1. **„Unter Fliese/Naturstein 45 mm“ ist seit DIN 18560-2:2022 falsch.** Die Nenndicken gelten belagunabhängig; dünnere Herstellersysteme sind Sonderkonstruktionen [V]. Viele Hersteller-PDFs (Sopro-Planer, VDZ) zitieren noch die alte Regel.
2. **Rohrüberdeckung CAF-F4 40 mm** steht im Wortlaut von 2004. Ob die Fassung 2022 den Wert unverändert führt, ist nur sekundär belegt [U]. Einige Ratgeber nennen für CA pauschal 30 mm; das gilt nur mit höherer Festigkeitsklasse und Nachweis und nicht nach VOB/C [V].
3. **Durmaz-Fußbodenbau verortet die Heizestrich-Regeln in DIN 18560-4.** Das ist falsch: Estrich auf Dämmschicht und Heizestrich regelt Teil 2 [V].
4. **U = 0,35 W/(m²K) für die Bodenplatte ist ein Referenzgebäudewert** (GModG Anlage 1), kein Bauteil-Grenzwert. Bauteilgrenzwerte gibt es nur im Bestand (Anlage 7) [V]. Förderstandards (KfW) liegen deutlich darunter [U].
5. **DIN 18202 Tab. 3 Z. 4:** Eine Ratgeberseite nennt 1 / 2 / 5 / 6 mm („Werte halbieren sich“). Zwei Quellen mit der Originaltabelle zeigen 1 / 3 / 9 / 12 / 15 mm [V].
6. **Fermacell-Waben-System:** Die Trittschallverbesserung wird einmal mit „bis 27 dB“ (Merkblatt) und einmal mit „bis 34 dB“ (Verarbeitungsanleitung) angegeben. Für den Nachweis zählen Prüfberichte bzw. DIN 4109-33 [V].
7. **Lüftungsmündung:** Zur Abdeckung widersprechen sich IZEG („zulässig bei ≤ 90° und 1,5 × Querschnitt“) und alwitra („nicht zulässig“). Vermutlich stammen die Aussagen aus verschiedenen Ausgaben von DIN 1986-100; vor dem Einbau E DIN 1986-100:2025-06 prüfen [V/U].
8. **Kein IFC-Typ für Abschottungen.** Der Generator muss eine Projektkonvention festlegen: `IfcDiscreteAccessory` USERDEFINED + ObjectType + Pset mit Nachweisnummer (abZ/aBG) [V].
9. **Typ-Psets nie über `IfcRelDefinesByProperties`.** Die EXPRESS-Regel meldet einen Fehler; nötig ist `HasPropertySets` am Typ [V]. Achsen mit Axis brauchen immer auch RefDirection [V].
10. **Der Holzrahmenbau erzeugt Konflikte systematisch.** Decken- und Wandraster sind gleich (625 mm). Eine Fallleitung nahe einer Rasterachse trifft deshalb Balken und Ständer zugleich. Im Grundriss sollten Fallleitungen und WC-Achsen auf Gefachmitten liegen; das ist eine Regel für den Entwurf, nicht erst für die Werkplanung [V Prototyp].
11. **Trockenestrich im Bad:** Gipsfaser-TE ist nur für W0-I/W1-I freigegeben [V Hersteller]. Die Gefälleflächen der bodengleichen Dusche brauchen ein zementgebundenes Element oder CT [V IGG]. Beton Ciré und Feinsteinzeug auf Gipsfaser-TE nur mit Systemfreigabe [U].
12. **Toleranzkette:** Mit Trockenelementen addieren sich die Plattentoleranzen über dem letzten Ausgleich. Für ±2 mm OKFF (Übergänge ohne Kante) ist eine Spachtelung auf dem TE einzuplanen, die B14 automatisch vorsieht. Die Toleranzwerte je Schicht sind Annahmen [U].
13. **DN 50 quer zur Balkenlage ist unzulässig** (0,15 h = 36 mm bei h = 240). Die Anschlussleitung der Rinne muss parallel zu den Balken oder unter der Decke laufen, oder es braucht einen Wechsel [V NA]. Recherche 08 formuliert die Regel richtig; neu ist hier die Konsequenz für die Rinnenleitung.
14. **Nicht erreichbar:** gesetze-im-internet.de, design2machine.com und api.crossref.org waren für direktes Abrufen gesperrt. Inhalte stammen aus Suchindex-Auszügen derselben Seiten [V Auszug].

## Offene Fragen an Regnauer

1. **Standard-Fußbodenaufbau je Geschoss:** Nassestrich (CAF/CT) oder Trockenestrich? Welche Aufbauhöhen (OK Rohdecke bis OKFF) gelten im EG (Bodenplatte/Keller) und im OG (Holzbalken-, Brettsperrholz- oder Hohlkastendecke)?
2. **Bad mit bodengleicher Dusche:** Wird die Rohdecke abgesenkt (Bodenplatte; im OG Balkenlage)? Welches Rinnen- und Gefällesystem ist Standard (Geberit, TECE, Fermacell-Gefälle-Set)? Wie wird W2-I auf Holz gelöst?
3. **FBH:** System (Tacker/Noppe nass, Trockensystem mit Wärmeleitblech), Rohrdimension, R_λ,B-Grenze in der Auslegung (0,10?), Belagfreigaben (Parkett geklebt, Teppich)?
4. **Schallschutz Holzbalkendecke:** vertragliche Zielwerte (L′n,w), Beschwerungsstandard (Splitt, Wabe, Masse in kg/m²), Unterdecke (Lattung oder federnd)?
5. **Toleranzen:** Ebenheit der Werksdecke (OSB/BSP), zugesicherte OKFF-Toleranz, Übergangsprofile als Standard?
6. **Firmenregeln Bohrungen:** größte Bohrung in Ständer, Schwelle, Rähm und Deckenbalken, Lage, Randabstände, Verstärkung (Vollgewindeschrauben, Laschen); BSH oder KVH für Deckenbalken?
7. **Fallleitungen:** Position im Grundriss (Gefachmitte, Schacht, Vorwand), wer plant Wechsel und Auswechslungen, werden Deckendurchbrüche im Werk gefräst?
8. **Luftdichtheit:** Welche Manschetten/Systeme (pro clima, Siga, Ampack) sind freigegeben? Wird die oberste Geschossdecke oder das Dach luftdicht ausgeführt?
9. **Strangentlüftung:** immer über Dach oder Belüftungsventil? Standardposition relativ zu Dachfenstern und Gauben?
10. **CAM:** Werden Durchbruchsbohrungen als WUP-Bearbeitung an die Multifunktionsbrücke übergeben (Grenzdurchmesser für Fräsen)? Gibt es ein Feld, um die Leitungs-GUID bis in die Fertigungsdaten mitzuführen?
11. **MFH (GK 3–5):** Welche Abschottungssysteme mit Nachweis für die eigenen Holzdecken gibt es, oder ist Betonverguss Standard? Wie weit wird die MHolzBauRL 2024 schon vorab angewendet?

---

*Quellen (Auswahl, abgerufen 27.09.2026):* DIN-Inhaltsverzeichnisse DIN 18560-2:2022-08, DIN 1986-100:2016-12, E DIN 1986-100:2025-06, E DIN 18040-2:2023-02, DIN EN 1995-1-1/NA:2013-08 (din.de); Knauf-Blog „DIN 18560-2 Erklärung & Prüfung“ (29.06.2026); Reschfloor-Normenlexikon DIN 18560-2; Wikipedia „DIN 18560“; DIN 18560-2:2004-04 (Scan stroy.it/silo.tips); Wico CAF-Planungshinweise; VDPM-Merkblatt Zementfließestrich 2021; Holcim-Leporello; VDZ-Merkblatt B19; IBF Troisdorf; Forum-Verlag-Leseprobe Heizestrich; Sopro-Planer Kap. 6/7; euroFEN MB 4; MAPEI-Natursteinbroschüre; BauNetz Wissen; Bau-Index „Toleranzen im Hochbau“; Fichtner-Estriche DIN 18202; TKB-Merkblatt 16 (12/2024), TKB-Bericht 11, IVK-Stellungnahme 2013; BG BAU Bauportal 4/2021; Chemotechnik; Stoneage-Datenblatt Beton Ciré; Artistic-Color-Datenblatt; Bodentrik-FAQ; Fermacell (Produktdatenblätter 2E11/2E22, Estrich-Wabe, Powerpanel TE, Verarbeitungsanleitung, Bodensysteme); IGG-Merkblatt 5 „Bäder, Feucht- und Nassräume im Holz- und Trockenbau“ (2018/2020); Oswald, „Dichter als vorher?“ (irbnet); Knauf „Trockenbauuntergründe in Nassräumen“; Geberit-Produktkatalog (CleanLine, Duofix); TECE (drainline); StMB „Planungsgrundlagen barrierefreies Bauen“; HEWI; FRELU; Holz Reinlein Merkblatt FBH; Weitzer MB-020; BVF-Richtlinie 9 (Thermolutz); cci-dialog DIN EN 1264-3; FV Gebäudeenergie Dresden 09/2021; DAGA 2018 (Rabold, Châteauvieux-Hellwig, Mecking), DAGA 2022 (Rabold, Bacher); Rigips TA Schall Holzbalkendecken; Forum Holzbau 2017 (Mayr, Einig, Rabold); Wolf Bavaria; GModG Anlage 1, 7, 8 (gesetze-im-internet, Suchauszug), geg-info.de, BBSR-Auslegung zu § 69; IZEG TI 2-1, 2-5; tga-praxis (Ishorst); alwitra; REHAU RAUPIANO PLUS TI; Ostendorf Skolan/HT; Zehnder ComfoTube; Heinze-Planungsunterlage Lüftung; GEWISS/Sanos, Meteor (Leerrohre); Hornbach-/Becker-Plastics-Datenblätter MSVR; pro clima (ROFLEX, KAFLEX, Anwendungshinweise); StMB „Leitungsanlagen-Richtlinie MLAR“ (2021); ZVEI/VdS-MLAR-Kommentar 2022; Promat; tga-fachplaner.de „Rohrabschottungen in Holzbalkendecken“ (2020); IRB „Leitungsdurchführungen im Holzbau“; bayika.de (MHolzBauRL 2024); Stucki, forum-holzwissen „Durchbrüche … neuer Eurocode 5“; Studiengemeinschaft Holzleimbau/IDH „Bemessung von BS-Holz-Bauteilen“; FRILO HO12; mb AEC S295.de; TU München/Zuschnitt 71; BSP-Wiki CLT_Plumbing_Design; cadwork „Manual Weinmann“; docs.dietrichs.com; design2machine (BTLx-Doku, Suchindex); compas_timber 2.2.0 (PyPI-Wheel, MIT).

*DOIs (Verlagsseite; Crossref nicht erreichbar):* Danielsson, Gustafsson (2014), Fracture analysis of glulam beams with a hole using a 3D cohesive zone model, Eng. Fract. Mech. 124–125, 10.1016/j.engfracmech.2014.04.020; Caniato u. a. (2024), Modelling the impact sound reduction of floating floors applied on CLT floors, J. Building Eng., 10.1016/j.jobe.2024.109679; Schiavi (2018), Improvement of impact sound insulation: a constitutive model for floating floors, Appl. Acoust. 129, 10.1016/j.apacoust.2017.07.013; Zhou, Zhao, Yang (2024), Apparent impact sound insulation of floating concrete toppings on mass timber floors, J. Archit. Eng. 30(4), 10.1061/JAEIED.AEENG-1838; Massaro, Malo (2023), Glulam beams with large round holes (WCTE), 10.52202/069179-0307 [U Jahr]; Danzer, Dietsch, Winter (2016), Reinforcement of round holes in glulam beams arranged eccentrically or in groups, WCTE 2016 (mediaTUM, ohne DOI).

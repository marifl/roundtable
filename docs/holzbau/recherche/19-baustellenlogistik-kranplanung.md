# Recherche 19: Baustellenlogistik und Montageplanung – Kran, Transport, Genehmigungen

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft (Hersteller, Gesetzestext, DGUV/BG BAU, Behörde, Urteil, Crossref) oder maschinell am Schema IFC4X3_ADD2 geprüft (IfcOpenShell 0.8.5). **[U]** = unsicher, nicht an der Primärquelle geprüft oder eigene Bewertung.

Baut auf [Recherche 06](06-ifc-phasenabdeckung.md) auf („Logistik, Montage: IfcTask LOGISTIC/MOVE/INSTALLATION, IfcVehicle; IfcTransportElement ist Kran/Aufzug“). Das Ergebnis dieser Recherche präzisiert diese Zeile (siehe IFC-Mapping).

Prototyp: [`arbeit/beispiele/b18_kranplanung.py`](../arbeit/beispiele/b18_kranplanung.py), Eingabe [`daten/b18_baustelle.json`](../arbeit/beispiele/daten/b18_baustelle.json), Tests [`tests/test_b18.py`](../arbeit/beispiele/tests/test_b18.py) (15 Tests, alle grün).

## Ergebnis in 5 Punkten

1. **Beim Holzfertighaus begrenzen Reichweite und Stellfläche den Kran, nicht das Gewicht.**
   - Die Elemente des Beispielhauses wiegen 0,65–1,23 t, die Hublast mit Anschlagmittel und Hakenflasche 1,15–1,73 t.
   - Die Radien liegen aber bei 20–30 m.
   - Im Prototyp reicht ein Kran der 35-t-Klasse in der Einfahrt (78 % Auslastung bei r = 20,0 m).
   - Ist die Einfahrt belegt, muss ein Kran der 60-t-Klasse von der Straße heben (72 % bei r = 29,6 m). Das kostet mit Beispielsätzen 62 % mehr und braucht zusätzliche Genehmigungen [V am Prototyp; Kranwerte Beispiel].
2. **Der Wind ist die versteckte Grenze.**
   - DIN EN 13000 rechnet mit 1,2 m² wirksamer Windfläche je t Last [V].
   - Holztafeln haben 14–20 m²/t.
   - Mit der Herstellerformel v_max = v_TAB · √(1,2 · m/A_W) ergeben sich für eine 9-m/s-Tabelle nur **2,9–4,1 m/s** (3-s-Böe in Hubhöhe) [V Formel]. Das ist konservativ: Die Formel ignoriert Traglastreserven [U].
   - Die Windgrenze gehört deshalb als harte Eingabe in die Hubplanung, gerechnet mit dem Hersteller-Windrechner.
3. **In München liegen die Genehmigungen auf dem kritischen Pfad.** Etwa 6 Wochen vor der Montage beginnen:
   - Haltverbot beim Mobilitätsreferat: ca. 10 Arbeitstage Bearbeitung, Schilder 3 volle Kalendertage vorher aufstellen [V].
   - Kran auf der Straße: Sondernutzung plus verkehrsrechtliche Anordnung, mehrere Wochen [V].
   - Überschwenken des Nachbargrundstücks, **auch ohne Last**: Anzeige nach Art. 46b Abs. 3 BayAGBGB mindestens 1 Monat vorher. Lehnt der Nachbar ab, hilft nur die Duldungsklage (OLG München 8 U 5531/20) [V].
4. **IFC 4.3 bildet die Montageplanung schemakonform ab.** Die generierte Datei meldet 0 Fehler bei `ifcopenshell.validate` mit EXPRESS-Regeln.
   - Kran = **IfcConstructionEquipmentResource ERECTING**. Die IFC-Doku nennt „tower crane or other mobile crane“ ausdrücklich [V].
   - Als Produkt optional **IfcTransportElement LIFTINGGEAR**. **CRANEWAY** ist die Kranbahn in der Halle und passt nicht zum Mobilkran [V]. Das korrigiert die Kurzform aus 06.
   - LKW = **IfcVehicle VEHICLEWHEELED** [V].
   - Flächen = IfcSpatialZone **CONSTRUCTION/TRANSPORT/RESERVATION** [V].
   - Montage = IfcTask INSTALLATION/MOVE mit IfcTaskTime und IfcRelSequence [V].
   - Gewicht = **GrossWeight in Qto_WallBaseQuantities und Qto_SlabBaseQuantities**. Qto_RoofBaseQuantities hat kein Gewicht, deshalb Dachelemente als IfcSlab ROOF [V].
5. **Herstellerdaten gibt es öffentlich nur als PDF-Tabellen.**
   - Die Liebherr-Datenblätter enthalten Traglast je Radius × Auslegerlänge × Ballast × Schwenkbereich [V].
   - Exakte Stützkräfte, Bodenpressung und Windwerte liefern nur LICCON-Einsatzplaner bzw. Crane Planner 2.0 (online, Import `.ifc`/`.dwg` in „Pro“, Export als Bericht/PDF) [V].
   - Eine offene maschinenlesbare Schnittstelle habe ich nicht gefunden [U].
   - Die Regelmaschine ist deshalb eine **Vorauswahl mit konservativen Hüllkurven**. Die Hubfreigabe bleibt beim Kranpartner.

## Regeln und Normen

| Thema | Regel (Kurzfassung) | Quelle | Status | In B18 |
|---|---|---|---|---|
| Mobilkrane, Wind auf Last | Mindestannahme A_P = 1,0 m²/t, c_W = 1,2 → **1,2 m²/t**; bei A·c_W > 1,2 m²/t Sonderprüfung; Windangabe = 3-s-Böe an der höchsten Stelle | EN 13000:2010/FprA1 (Wortlaut über iTeh-Leseprobe), FEM 5.016, Liebherr „Influence of wind“ | [V] | `wind_zulaessig()`, Warnung |
| Windformel | v_max = v_max_TAB · √(1,2 m²/t · m_H / A_W); größer als v_TAB → v_TAB | Liebherr Schulungsunterlage P403 (Beispiele 85 t/60 m² → 9 m/s; 65 t/280 m² → 5,9 m/s) | [V], Test | ja |
| Turmdreh-/Mobilbaukrane | DIN EN 14439; das MK-88-Datenblatt verweist auf EN 14439:2009 | Liebherr MK 88-4.1 Datenblatt | [V] Verweis, Inhalt [U] | – |
| Krane, Freileitung | Schutzabstand bis 1 kV **1 m**, 1–110 kV **3 m**, 110–220 kV **4 m**, 220–380 kV und unbekannt **5 m**; Ausschwingen von Seil und Last berücksichtigen | DGUV Vorschrift 52 § 39; DGUV Vorschrift 38 § 16; BG BAU C 412 | [V] | `schutzabstand_freileitung()` + 1 m Zuschlag (Annahme), 2D |
| Kap. 2.8 DGUV Regel 100-500 | **zurückgezogen** → DGUV Regel 109-017 „Lastaufnahme- und Anschlagmittel“: Neigungswinkel **≤ 60°**, T_β = T_0 · cos β, Kennzeichnung für 60° | DGUV Regel 100-500 Inhaltsverzeichnis; DGUV Regel 109-017 Abschn. 4.1.2.1, Anhang A | [V] | Anschlagmittel 0,30 t pauschal |
| Bodenpressung | **p = F_max / A ≤ p_zul**; immer die maximale Stützkraft; Beispiel 120 kN / 0,035 m² = 3 430 kN/m² → Platte 0,6 m² (80 × 80 cm) | DGUV Information 208-059 Abschn. 4 (Formel 4.3, Tab. 4.1 nach DIN 1054:1976-11) | [V] | `bodenpressung()`, Test |
| zul. Bodenpressung (Tabelle) | angeschüttet 0–100; nichtbindig fest 150–200; bindig weich 40 / steif 100 / halbfest 200 / fest 300; Fels 1 500–3 000 kN/m²; Wiese 100, Asphalt 200, Schotter verdichtet 250, Kies fest 400 | DGUV Information 208-059 Tab. 4.1; DGUV Information 208-019 Anh. 1 (aus DGUV Information 213-009) | [V] | Bodenzonen 150/250/200 |
| Stützteller | Randbereich trägt nicht: Liebherr rechnet mit 80 % der Tellerfläche (LTM 1230-5.1: 1 109 kN auf 0,6 × 0,6 m → 3 851 kN/m²) | Liebherr „Untergrund für sichere Kraneinsätze“ | [V] | Test; im Modell tragen die Platten voll [U] |
| Baugrube/Böschung | Abstand der Abstützung zur Böschungskante: bis 12 t Gesamtgewicht **≥ 1,00 m**, > 12–40 t **≥ 2,00 m**; ohne Nachweis Böschungswinkel 45° (nichtbindig), 60° (steif/halbfest), 80° (Fels); Schutzstreifen 0,60 m | DIN 4124 in der Wiedergabe BG BAU B 213 | [V] Wiedergabe, Normtext [U] | `abstand_baugrube()`; > 40 t: 3 m Beispiel + „Nachweis nötig“ [U] |
| bewegte Kranteile | ≥ 0,5 m Sicherheitsabstand zu Bauwerk, Gerüst, Stapeln (für TDK formuliert) | BG BAU B 213 | [V] | Heckradius + 0,5 m zu Haus und Baumkrone |
| Überschwenken | Eigentum erstreckt sich auf den Luftraum; Einwirkungen ohne Ausschließungsinteresse sind zu dulden | § 905 BGB | [V] | Warnung |
| Überschwenken Bayern | Überschwenken mit **und ohne** Last = „Übergreifen von Geräten“ (Art. 46b Abs. 1 BayAGBGB); Anzeige **≥ 1 Monat** vorher (Abs. 3); nach Ablehnung keine Selbsthilfe → Duldungsklage; Duldung nur, wenn anders nicht oder nur mit unverhältnismäßigen Kosten möglich | OLG München, Urt. v. 15.10.2020 – 8 U 5531/20 | [V] | Warnung „Nachbar“ |
| Gegenbeispiele | LG München II, 10.09.2020 – 13 O 3296/20: lastfrei in 17 m über First zu dulden (§ 905 S. 2); offenbar derselbe Streit, den das OLG München (8 U 5531/20) aufgehoben hat [U]. OLG Stuttgart 2022/23: Unterlassung auch lastfrei, weil die Anzeige nach § 7d NRG BW fehlte | lexika.de (BeckRS 2020, 27169); Pressemitteilung OLG Stuttgart | [V] | – |
| Baustellen-VO | Vorankündigung spätestens **2 Wochen** vorher bei > 30 AT und > 20 Beschäftigten gleichzeitig oder > 500 Personentagen; SiGe-Plan bei mehreren Arbeitgebern und Vorankündigung **oder** besonders gefährlichen Arbeiten; Koordinator bei mehreren Arbeitgebern | BaustellV §§ 2, 3 | [V] | Warnung |
| gefährliche Arbeiten | Anh. II Nr. 1 Absturz > 7 m; Nr. 4 < 5 m zu Hochspannungsleitungen; Nr. 10 Auf-/Abbau von **Massivbauelementen** mit kraftbetriebenen Hebezeugen | BaustellV Anhang II | [V] Text; ob Holztafeln „Massivbauelemente“ sind: [U] | Warnung |
| Maße | Breite **2,55 m**, Höhe **4,00 m**, Einzelfahrzeug 12,00 m, Sattelkfz 15,50 m bzw. 16,50 m, Zug 18,75 m; keine Toleranzen | § 32 StVZO | [V] | Transportprüfung |
| Gewichte | Einzelachse 10 t, angetrieben 11,5 t; Kombination > 4 Achsen **40 t** | § 34 StVZO | [V] | Nutzlast 24 t (Beispiel) |
| Ladung | Fahrzeug + Ladung ≤ 2,55 m breit, ≤ 4 m hoch; hinten bis 1,50 m (bis 100 km: 3 m); gesamt ≤ 20,75 m | § 22 Abs. 2–4 StVO | [V] | Stapelhöhe Plateau = 4,00 − 1,35 m |
| Übermaß | Erlaubnis für Verkehr über den Grenzen (§ 29 Abs. 3 StVO); Ausnahme von Maßen und Ladung (§ 46 Abs. 1 Nr. 5 StVO); Ausnahme von §§ 32, 34 StVZO durch höhere Verwaltungsbehörde (§ 70 StVZO) | StVO §§ 29, 46; StVZO § 70 | [V] | Hinweis bei Übermaß |
| Kran im Verkehr | LTM 1060-3.1: 36 t bei 12 t Achslast mit reduziertem Ballast; mit vollem Ballast ca. 15 t je Achse | Liebherr-Presse 2015, Datenblatt | [V] | – |

## Kran-Kenndaten (typisch; nur Orientierung, Quelle beachten)

| Modell | Typ | max. Traglast | Ausleger / Ausladung | Ballast, Achsen, Gewicht | Abstützung / Stützkraft | Quelle |
|---|---|---|---|---|---|---|
| Liebherr LTM 1030-2.1 | Autokran 2-Achser | 35 t bei 3 m | Tele 9,2–30 m, max. Radius 40 m, Hubhöhe 44 m; Tabelle (5,5 t Ballast, 360°): ca. 7,2–8,0 t bei 10 m, 2,4–2,5 t bei 20 m | 5,5 t (Variante 2,3 t), 2 Achsen | VarioBase; Stützkräfte im Datenblatt | liebherr.com (Produktseite); Datenblatt 2004 (liebherr-club) [V]; Tabellenwerte aus altem Blatt [U aktuell] |
| Liebherr LTM 1060-3.1 | 3-Achser | 60 t bei 2,1 m | Tele 10,3–48 m, Radius 48 m, Hubhöhe 63 m; Tabelle (12,8 t Ballast, 360°): ca. 13–16 t bei 10 m, 4,9–5,7 t bei 20 m je Auslegerlänge | 12,8 t, 3 Achsen, 36 t bei 12 t Achslast | max. Stützkräfte 280 kN (29 t) bzw. 445 kN (46 t) je nach Konfiguration | Datenblatt (Spiegel voutas.com), Presse 2015 [V]; Zuordnung der zwei Stützkräfte [U] |
| Liebherr LTM 1090-4.2 | 4-Achser | 90 t bei 3 m | Tele 11,4–60 m, Radius 62 m, Hubhöhe 76 m | 22,5 t, 4 Achsen | VarioBase/VarioBallast | liebherr.com [V] |
| Liebherr LTM 1160-5.2 | 5-Achser | 180 t bei 2,5 m | Tele 13,1–62 m, Radius 78 m, Hubhöhe 99 m | 54 t, 5 Achsen | – | liebherr.com [V] |
| Liebherr LTM 1230-5.1 | 5-Achser | – | – | – | max. Stützkraft 1 109 kN, Teller 0,6 × 0,6 m | Liebherr-Kundenmagazin [V] |
| Liebherr MK 88-4.1 (E) | Mobilbaukran | 8 000 kg | Ausladung 45 m, 1 850–2 200 kg an der Spitze (Zusatzballast/Plus), Hakenhöhe 17,9 m (horizontal) bis 59,1 m (45°); Traglasten gelten bis 14,1 m/s (6,5 Bft) | 2 t Zusatzballast; 4 Achsen, 8 × 6 × 8; Einsatzgewicht 48 t; Drehradius 3,55 m | Abstützweite 7,0 m (reduziert 5,75 m) × 7,3 m, Teller 0,6 × 0,6 m, „max. 37 t“ in der Draufsicht | liebherr.com; Datenblätter (hn-krane, kvn, liebherr-club) [V]; „37 t“ als Eckdruck gelesen [U] |
| Liebherr MK 140 | Mobilbaukran | – | – | – | – | nicht abgerufen [U] |
| Liebherr 81 K.1 | Schnelleinsatzkran (Untendreher) | 6 000 kg | Ausladung 48 m, 1 350 kg an der Spitze, 11 Hakenhöhen 17,4–40,4 m, 30°-Steilstellung | Ballastierradius 5 m | – | Datenblatt (sab-eitorf, bkl) [V] |
| Potain Igo, Tadano/Grove AT | – | – | – | – | – | keine Primärquelle abgerufen [U] |

**Datenformat [V]:** Die Traglasttabellen der Hersteller sind öffentlich als PDF-Datenblatt verfügbar. Gegliedert sind sie nach Auslegerlänge (Spalten), Radius (Zeilen), Ballast, Abstützbasis und Schwenkbereich (360° oder „nach hinten“). Die Tabellen gelten „netto“ oder mit Hakenflasche, je nach Blatt. Die Stützkraft steht im Datenblatt nur als Maximalwert. Den Wert für einen konkreten Hub rechnen der LICCON-Einsatzplaner und Crane Planner 2.0 aus derselben Logik wie die Lastmomentbegrenzung: „Free“ in 2D, „Pro“ mit 3D, `.ifc`/`.dwg`-Import und Export [V]. Ein dokumentierter Export der Planungsdaten als offene Datei ist mir nicht bekannt [U].

**Lastmoment-Prinzip [V, Liebherr/DGUV]:** Die Traglast fällt mit dem Radius, weil das Kippmoment (Last × Radius) und die Tragfähigkeit von Ausleger und Abstützung begrenzt sind. Die Stützkraft hängt deshalb von Schwenkwinkel, Radius und Last ab. Für die Bodenpressung ist ohne Einsatzplaner die maximale Stützkraft anzusetzen.

## Genehmigungen München (Mobilitätsreferat, Stand 2025/26)

| Vorgang | Zuständig / Verfahren | Vorlauf | Unterlagen | Quelle |
|---|---|---|---|---|
| Vorübergehendes Haltverbot (Abladezone, ggf. Kranstellung) | MOR-GB2.3 „Temporäre Anordnungen“, Implerstraße 9; verkehrsrechtliche Anordnung | Bearbeitung **10 Arbeitstage**; Schilder spätestens am 4. Tag vor Gültigkeit (**3 volle Kalendertage**); Baustellenbelieferung max. 365 Tage | Antrag, bemaßte Skizze, **Vornotierungsliste**; Schilder selbst beschaffen/aufstellen, 30 cm Schrammbord; alle 20–30 m Wiederholungsschild | stadt.muenchen.de (Leistung 1072585); Antrag HV Umzug/Baustelle (29.01.2025) [V] |
| Autokran/Baukran auf öffentlichem Grund | MOR: **Sondernutzungserlaubnis + verkehrsrechtliche Anordnung (§ 45 StVO)**; „Autokran (Anzahl)“ im Formular ankreuzen | aktuelle Bearbeitungsdauer online; länger bei Beteiligung von Baureferat, Signalabteilung oder MVG; 2018–19 im Mittel **3,2 Wochen** (klein) bzw. **5,3 Wochen** (mittel/groß), Spitzen 7 Wochen | Antrag „Baustelle privat“, **MVAS-Zertifikat** der verantwortlichen Person, **Verkehrszeichenplan** bzw. Regelplan nach RSA 21, bemaßter Plan; Angabe „vor benachbartem Anwesen“ | stadt.muenchen.de (1072250), Antragsformular, Antwort KVR an Stadtrat (muenchen-transparent) [V]; die Zahlen von 2020 sind veraltet [U aktuell] |
| Stillstands-Auflagen | eingerichtete Fläche nach 10 Werktagen ungenutzt → Absicherung abbauen; nach 20 Werktagen Stillstand räumen; 72 h Vorlauf bei Wiederaufnahme | – | – | MOR „Auflagen gegen Stillstand“ [V] |
| Übermaß-/Schwertransport | Erlaubnis § 29 Abs. 3 StVO, ggf. Ausnahme § 70 StVZO | – | – | Gesetzestext [V]; bayerisches Verfahren (VEMAGS, Behörde, Fristen) nicht geprüft [U] |
| Überschwenken Nachbar | Anzeige an Eigentümer **und** Nutzungsberechtigte (Art. 46b Abs. 3 BayAGBGB) | **≥ 1 Monat** | Art, Dauer und Umfang der Arbeiten, mit/ohne Last | OLG München 8 U 5531/20 [V] |
| Vorankündigung, SiGe | Gewerbeaufsicht (in Bayern bei den Regierungen [U]) | **≥ 2 Wochen** vor Einrichtung | Anhang I BaustellV | BaustellV § 2 [V] |
| Freileitung | Netzbetreiber informieren; bei > 1 kV auch EVU; ggf. Freischaltung/Abdeckung | – | – | DGUV Vorschrift 52 § 39; DGUV Information 214-002 [V]; Netzbetreiber in München (SWM) [U] |
| Baumschutz | BaumschutzV München, Wurzelbereich nach DIN 18920 | – | – | **nicht geprüft** [U]; B18 nimmt Kronentraufe + 1,5 m als Sperrfläche an |

**Zeitstrahl (abgeleitet [U]):** T − 6 Wochen Nachbar-Anzeige und Antrag Sondernutzung/Kran → T − 3 Wochen Antrag Haltverbot → T − 2 Wochen Vorankündigung (falls nötig) → T − 4 Tage Schilder und Vornotierung → T Montage.

## Holzbau-Montage: Elemente, Transport, Anschlag

- **Montagedauer:** Regnauer: „In 1–2 Tagen ist das Haus regendicht“, Rohbau „innerhalb von ein bis zwei Tagen“, eigene Montagekolonnen [V]. Fertighauswelt: Montage geschossweise mit Kolonne und Kran, meist 1–2 Tage; Außenwände EG in „nicht einmal einer Stunde“ [V, Branchenportal].
- **Werkvorlauf:** Regnauer-Bauleistungsbeschreibung (AT): Montagebeginn frühestens 12 Wochen nach Ausstattungsfestlegung bzw. Baugenehmigung im Original [V].
- **Innenlader:**
  - Faymonville PrefaMAX: Ladeschacht 7,1–10,2 m, Fahrzeugbreite 2,55 m, „keine Kosten für Begleitfahrzeuge und Sondergenehmigungen“ [V].
  - Langendorf: Ladehöhe „über 3 700 mm“, Aggregatlast 27 t; Be- und Entladen der Paletten ab Windstärke 5 verboten [V].
  - Das Gestellmaß für Holztafeln habe ich nicht gefunden [U]. B18 nimmt 1,5 m Stapelbreite an.
- **Anschlagpunkte:**
  - Schmid RAPID T-Lift (ETA-12/0373): Kugelkopfabheber 1,3 t (d = 12 mm) bzw. 2,5 t (d = 16 mm) × sin α, Schrauben nur einmal verwenden, dynamischer Beiwert φ = 1,10 (stationärer Kran ≤ 90 m/min) bis 2,00 (fahrbarer Kran, unebenes Gelände), Belastung ≤ 30 min [V].
  - Rothoblaas WASP/WASPL (ETA-11/0030): Bemessung mit k_mod = 1,0, γ_M = 1,3, γ_G = 1,35, φ₂ = 1,2; bei mehr als 3 Anschlagpunkten Traverse [V].
- **Wind beim Montieren:** Die Traglastangaben des MK 88 gelten bis 14,1 m/s [V]. Bei großer Windangriffsfläche gilt die Formel oben [V]. Eine Holzbau-spezifische Windgrenze aus DGUV oder Holzbau Deutschland habe ich nicht gefunden [U].
- **Elementgewichte (B18, aus Aufbauten):**
  - Außenwand B1 roh 49,2 kg/m², mit Putz (20) und Fensteranteil (5,25) 74,4 kg/m² [Zuschläge = Annahme].
  - Decke (Balken 60/220, GKF, OSB, Holzfaser) 36,6 kg/m² ohne Estrich/Schüttung.
  - Dach (Sparren 80/240, Holzfaser, HFD 60, OSB) 43,4 kg/m² ohne Eindeckung.

## Algorithmus (B18)

```
Eingabe: B1-IFC, Grundstück/Straße/Nachbarn/Baugrube/Hindernisse/Freileitung, Kranliste (Beispiel), Fahrzeuge
1  q_wand  ← Σ_Bauteile NetVolume × MassDensity(Material) / GrossSideArea        # aus B1-IFC
   q_decke, q_dach ← Σ_Schichten dicke × ρ × Holzanteil
2  E ← erzeuge_haus()                    # 12 Wand-/Giebel-, 6 Decken-, 8 Dachelemente mit Masse, Schwerpunkt, OK
3  E ← sortiere(E, Rang: EG-Wand < Decke < DG-Giebel < Dach)   # prüfe_reihenfolge(E) = ∅
4  LKW ← Next-Fit(E): Wand/Giebel/Dach stehend Innenlader (Σ Dicke ≤ Gestellbreite), Decke liegend Plateau
         (Σ Dicke ≤ 4,00 m − Ladeflächenhöhe), Σ Masse ≤ Nutzlast; Übermaß → § 29(3) StVO / § 70 StVZO
5  für jeden Kran K:
     tage_K ← Zeitplan(K)                                # Ladung nicht über Nacht teilen
     F_K ← (Grundstück ∪ Straße) − Abladezone − Haus⊕0,5 − Baugrube⊕d_4124(Gesamtgewicht_K)
           − Baum-Wurzelbereich − Schächte − Szenario-Sperrflächen
     für (x, y) im Raster (0,5 m), Orientierung ∈ {0°, 90°}:
       Platte ← kleinste p ∈ Platten mit Abstützrechteck(p) ⊂ F_K und F_max/p² ≤ min p_zul(Zonen unter Platte)
       verwerfe, falls keine Platte;  verwerfe, falls Kreis(Heckradius) ∩ (Haus⊕0,5 ∪ Krone⊕0,5) ≠ ∅
       für jedes Element e:  r = max(|Aufnahme − C|, |Schwerpunkt_e − C|)
            Last = m_e + Anschlagmittel + Hakenflasche;  verwerfe, falls Last > 0,8 · T_K(r) oder Hakenhöhe fehlt
       verwerfe, falls min Abstand(Hakenweg ⊕ ½ max(L,B), Ausleger, Heck; Freileitung) < Schutzabstand(kV) + Zuschlag
            (Mobilbaukran: fester Ausleger über den überstrichenen Drehwinkel)
       Kosten = tage_K · Tagessatz + Anfahrt (+ Straße) (+ große Platten)
       Schlüssel = (Kosten, #Lasthübe über Nachbar, auf Straße, max. Auslastung, Kran, x, y, ori)
6  Bester ← min Schlüssel;  Warnungen (Nachbar mit/ohne Last, Straße, Wind, Freileitung, DIN 4124, BaustellV, Übermaß)
7  Ausgaben: JSON, SVG-BE-Plan, IFC (IfcWorkSchedule/IfcTask/IfcTaskTime/IfcRelSequence, Ressourcen, Zonen)
```

Hakenweg: Der Kran schwenkt auf dem kürzeren Weg und fährt den Radius dabei linear über den Drehwinkel (25 Stützpunkte). Die Last kann sich drehen, deshalb wird der Weg um die halbe größte Elementabmessung aufgeweitet. Die Prüfung ist 2D, also konservativ, weil die Leitungshöhe nicht angerechnet wird.

## IFC-4.3-Mapping (geprüft gegen IFC4X3_ADD2, IfcOpenShell 0.8.5)

| Sachverhalt | IFC 4.3 | Status / Befund |
|---|---|---|
| Kran als Einsatzmittel | **IfcConstructionEquipmentResource**, PredefinedType **ERECTING** („Lifting, positioning, and placing elements“), zugeordnet zum Vorgang über IfcRelAssignsToProcess | [V] Doku nennt „tower crane or other mobile crane“ als Beispiel |
| Kran als Objekt | **IfcTransportElement LIFTINGGEAR** („device used for lifting or lowering heavy goods“) + Pset_TransportElementCommon.CapacityWeight; mit der Ressource verbunden über IfcRelAssignsToResource | [V] Enum; Wahl LIFTINGGEAR statt USERDEFINED ist eigene Bewertung [U]. **CRANEWAY** = „crane way system … in a factory“, also nicht für den Mobilkran [V] → Präzisierung zu 06 |
| LKW | **IfcVehicle VEHICLEWHEELED** („car, lorry, forklift“), Qto_VehicleBaseQuantities (nur Length/Width/Height, **kein Gewicht**), Ressource TRANSPORTING | [V] |
| Stellfläche, Abladezone, Schwenkbereich | **IfcSpatialZone** CONSTRUCTION / TRANSPORT / RESERVATION mit Body (extrudiertes Polygon), Qto_SpatialZoneBaseQuantities, IfcRelReferencedInSpatialStructure → IfcSite | [V] Enum und Validierung; Wahl RESERVATION für den Schwenkbereich [U] |
| Montage | IfcWorkSchedule (PLANNED) → IfcRelAssignsToControl → Sammel-IfcTask (CONSTRUCTION) → IfcRelNests → IfcTask **INSTALLATION** (26) + **MOVE** (6 Anlieferungen) + Rüsten | [V] |
| Zeiten | IfcTaskTime (ScheduleStart/Finish/Duration, DurationType WORKTIME bzw. ELAPSEDTIME); IfcRelSequence FINISH_START (Hubkette; LKW → erster Hub) | [V] |
| Element ↔ Vorgang | IfcRelAssignsToProduct (RelatingProduct = Element) | [V] |
| Verpackung/Beladung | **Pset_PackingInstructions** (nur für IfcTask/MOVE) → SpecialInstructions mit Beladereihenfolge | [V] |
| Elementgewicht | **Qto_WallBaseQuantities.GrossWeight/NetWeight**, Qto_SlabBaseQuantities, Qto_MemberBaseQuantities, Qto_PlateBaseQuantities; **Qto_RoofBaseQuantities hat kein Gewicht** → Dachelemente als IfcSlab ROOF; Pset_ElementAssemblyCommon kennt nur Reference/Status | [V] |
| Gewicht berechnen | B1 hat Pset_MaterialCommon.MassDensity je Material und NetVolume je Teil → Masse maschinell berechenbar; **B1 schreibt noch kein GrossWeight** (Vorschlag: im Wand-Qto ergänzen) | [V] |
| Hubdaten | eigenes Pset **HRB_Kranhub** am IfcTask (Hublast, Radien, Traglast, Auslastung, Windgrenze, Last über Nachbar) | eigene Konvention [U] |
| Prüfung | `b18_montage.ifc`: 1 134 Entitäten, `ifcopenshell.validate` (Schema + EXPRESS-Regeln) **0 Meldungen**, byte-identisch über Läufe und `PYTHONHASHSEED` (SHA-256 `e4d8de10…a7f6f5`) | [V] |

Offen: Ob der buildingSMART Validation Service Elemente ohne Geometrie als Industry-Practice-Warnung meldet, habe ich nicht geprüft [U]. 4D-Viewer lesen IfcTaskTime unterschiedlich gut [U].

## Prototyp-Ergebnisse (B18, Szenario „basis“ und „einfahrt_belegt“)

Lauf: `python b18_kranplanung.py` (Raster 0,5 m, 14 694 Stellungen je Kran, ca. 7 s je Szenario). Ausgaben: `ausgabe/b18_kranplanung.json`, `ausgabe/b18_be_plan_basis.svg`, `ausgabe/b18_be_plan_einfahrt_belegt.svg`, `ausgabe/b18_montage.ifc`.

**Gewicht B1 (4,80 × 2,75 m, 13,2 m² brutto):** 649,4 kg = 49,2 kg/m².

| Material | Teile | Volumen m³ | ρ kg/m³ | Masse kg |
|---|---:|---:|---:|---:|
| KVH C24 | 18 | 0,515 | 420 | 216,3 |
| Holzfaserdämmplatte | 2 | 0,687 | 180 | 123,7 |
| Gipsplatte GKF | 4 | 0,143 | 800 | 114,6 |
| OSB/3 | 4 | 0,172 | 600 | 103,1 |
| Holzfaser-Dämmmatte | 12 | 1,776 | 50 | 88,8 |
| Dampfbremse | 1 | 0,0023 | 900 (Annahme) | 2,1 |
| Schrauben | 176 | 0,00011 | 7 850 | 0,9 |

**Haus (12 × 10 m, 1,5-geschossig, Satteldach 35°):** 26 Elemente, zusammen 22,99 t.

| Gruppe | Anzahl | Maße | Masse je Element |
|---|---:|---|---:|
| EG-Außenwand | 8 | 6,0 bzw. 5,0 × 2,75 m | 1,228 / 1,024 t |
| Decke | 6 | 10,0 × 2,0 m | 0,732 t |
| DG-Giebel (Dreieck) | 4 | 5,0 × 3,50 m | 0,652 t |
| Dach | 8 | 6,71 × 3,0 m | 0,873 t |

**LKW (Next-Fit, Beispiel-Grenzen 24 t):** 6 Ladungen.

| LKW | Fahrzeug | Elemente | Masse | Ankunft |
|---:|---|---|---:|---|
| 1 | Innenlader | W-S1 bis W-O2 | 4,50 t | Tag 1, 07:30 |
| 2 | Innenlader | W-N1 bis W-W2 | 4,50 t | Tag 1, 08:42 |
| 3 | Plateau | D-1 bis D-6 (1,83 m Stapel) | 4,39 t | Tag 1, 09:54 |
| 4 | Innenlader | Giebel | 2,61 t | Tag 1, 11:54 |
| 5 | Innenlader | Dach Süd | 3,49 t | Tag 1, 12:54 |
| 6 | Innenlader | Dach Nord | 3,49 t | **Tag 2**, 06:30 |

Der Engpass ist das Volumen (Gestellbreite, Stapelhöhe), nicht die Nutzlast: Kein LKW ist zu mehr als 19 % ausgelastet.

**Kranwahl (Beispielkrane, Beispielsätze):**

| Szenario | AK-35 | AK-60 | AK-100 | MBK-8 | gewählt |
|---|---|---|---|---|---|
| basis | 40 zulässig, 2 650 € | 22 zulässig, 4 300 € | 0 (Abstützung inkl. Platten passt nirgends) | 64 zulässig, 4 950 € (22 Stellungen scheitern am festen 45-m-Ausleger gegen die Freileitung) | **AK-35** bei (18,5 \| 4,0), Einfahrt |
| einfahrt_belegt | 0 (von der Straße fehlt Reichweite) | 18 zulässig, 4 300 € | 0 | 64, 4 950 € | **AK-60** bei (23,0 \| −4,5), Straße vor Nachbar Ost |

**Gewählt, basis:**
- Aufstellung: AK-35, Orientierung 0°, Platten 1,0 × 1,0 m auf verdichtetem Schotter, p = 250 ≤ 250 kN/m² (genau an der Grenze).
- Auslastung: max. **78,4 %**, kritischer Hub **W-N2** (1,73 t bei r = 20,0 m, Beispiel-Traglast 2,21 t). Aufnahmeradius am LKW 9,8 m. Erforderliche Hakenhöhe max. 10,3 m (Dach), verfügbar ≥ 22,9 m.
- Wind: zulässige Böe **2,85–4,07 m/s** (Wand 2,9–3,0, Decke 4,1, Giebel 3,3, Dach 2,85). Alle 26 Hübe liegen unter der geplanten Böe von 7 m/s.
- Nachbar: 2 Hübe führen Last über Nachbargrund (D-1 mit 10 m Elementlänge; R-N1) → Anzeige nach Art. 46b BayAGBGB.
- Freileitung: Abstand ≥ 12,5 m (gefordert 4,0 m).
- Kosten und Zeit: 2 650 € (2 Einsatztage). Montage Tag 1 07:00–14:52, Tag 2 07:00–09:28 inkl. Abrüsten; 10,3 Einsatzstunden. Warnung: Kran über Nacht aufgebaut.

**Gewählt, einfahrt_belegt:**
- Aufstellung: AK-60 auf der Straße, Platten 1,5 × 1,5 m, p = 178 ≤ 200 kN/m².
- Auslastung: max. 71,9 % (W-N2 bei r = 29,6 m).
- Nachbar: 0 Lasthübe über Nachbargrund.
- Kosten: 4 300 €.
- Warnungen: Sondernutzung, verkehrsrechtliche Anordnung und „vor benachbartem Anwesen“.

**Rastersensitivität:**
- Mit 1,0-m-Raster findet die Suche den engen Einfahrt-Stellplatz nicht (7,0 m Abstützung inkl. Platten in 7,0 m Einfahrt). Sie wählt dann AK-35 teilweise auf der Straße für 3 200 €.
- 0,25 m liefert dasselbe Ergebnis wie 0,5 m (176 statt 40 zulässige AK-35-Stellungen).
- Folge: Raster ≤ 0,5 m oder eine exakte Randsuche.

**Tests:** `python -m pytest tests/test_b18.py` → **15 passed** (ca. 17 s). Geprüft werden:
- Normwerte (Freileitung, DIN 4124), die DGUV- und Liebherr-Beispiele zur Bodenpressung und die Windformel gegen drei Quellenbeispiele (Liebherr 9 / 5,9 m/s, FEM 7 m/s)
- Traglastkurve, B1-Gewicht und Aufbaugewicht
- Reihenfolge-Regel samt Gegenbeispiel, LKW-Ladungen samt Übermaß-Fall
- Kranwahl in beiden Szenarien, Rastersensitivität, harte Freileitungsregel
- Zeitplan (keine Ladung über Nacht geteilt)
- IFC valide und byte-identisch, SVG deterministisch

## Literatur (DOIs über Crossref geprüft [V])

Kranstandort und Kranwahl:
- Zhang, P.; Harris, F. C.; Olomolaiye, P. O.; Holt, G. D. (1999): Location Optimization for a Group of Tower Cranes. *J. Constr. Eng. Manage.* 125(2), 115–122. https://doi.org/10.1061/(ASCE)0733-9364(1999)125:2(115)
- Tam, C. M.; Tong, T. K. L.; Chan, W. K. W. (2001): Genetic Algorithm for Optimizing Supply Locations around Tower Crane. *J. Constr. Eng. Manage.* 127(4), 315–321. https://doi.org/10.1061/(ASCE)0733-9364(2001)127:4(315)
- Tam, C. M.; Tong, T. K. L. (2003): GA-ANN model for optimizing the locations of tower crane and supply points for high-rise public housing construction. *Constr. Manage. Econ.* 21(3), 257–266. https://doi.org/10.1080/0144619032000049665
- Al-Hussein, M.; Alkass, S.; Moselhi, O. (2005): Optimization Algorithm for Selection and on Site Location of Mobile Cranes. *J. Constr. Eng. Manage.* 131(5), 579–590. https://doi.org/10.1061/(ASCE)0733-9364(2005)131:5(579) – nächster Verwandter von B18 (Kranwahl + Stellplatz)
- Hasan, S.; Al-Hussein, M.; Hermann, U. H.; Safouhi, H. (2010): Interactive and Dynamic Integrated Module for Mobile Cranes Supporting System Design. *J. Constr. Eng. Manage.* 136(2), 179–186. https://doi.org/10.1061/(ASCE)CO.1943-7862.0000121 – Abstützung/Bodenpressung
- Safouhi, H.; Mouattamid, M.; Hermann, U.; Hendi, A. (2011): An algorithm for the calculation of feasible mobile crane position areas. *Autom. Constr.* 20(4), 360–367. https://doi.org/10.1016/j.autcon.2010.11.006 – analytische Alternative zur Rastersuche
- Lien, L.-C.; Cheng, M.-Y. (2014): Particle bee algorithm for tower crane layout with material quantity supply and demand optimization. *Autom. Constr.* 45, 25–32. https://doi.org/10.1016/j.autcon.2014.05.002
- Marzouk, M.; Abubakr, A. (2016): Decision support for tower crane selection with building information models and genetic algorithms. *Autom. Constr.* 61, 1–15. https://doi.org/10.1016/j.autcon.2015.09.008
- Wu, K.; García de Soto, B.; Zhang, F. (2020): Spatio-temporal planning for tower cranes in construction projects with simulated annealing. *Autom. Constr.* 111, 103060. https://doi.org/10.1016/j.autcon.2019.103060

Hubwege, Kollision, 3D-Planung:
- Zhang, C.; Hammad, A. (2012): Improving lifting motion planning and re-planning of cranes with consideration for safety and efficiency. *Adv. Eng. Inform.* 26(2), 396–410. https://doi.org/10.1016/j.aei.2012.01.003
- Lei, Z.; Taghaddos, H.; Olearczyk, J.; Al-Hussein, M.; Hermann, U. (2013): Automated Method for Checking Crane Paths for Heavy Lifts in Industrial Projects. *J. Constr. Eng. Manage.* 139(10). https://doi.org/10.1061/(ASCE)CO.1943-7862.0000740
- Olearczyk, J.; Al-Hussein, M.; Bouferguène, A. (2014): Evolution of the crane selection and on-site utilization process for modular construction multilifts. *Autom. Constr.* 43, 59–72. https://doi.org/10.1016/j.autcon.2014.03.015
- Han, S. H.; Hasan, S.; Bouferguène, A.; Al-Hussein, M.; Kosa, J. (2015): Utilization of 3D Visualization of Mobile Crane Operations for Modular Construction On-Site Assembly. *J. Manage. Eng.* 31(5). https://doi.org/10.1061/(ASCE)ME.1943-5479.0000317
- Hussein, M.; Zayed, T. (2021): Crane operations and planning in modular integrated construction: Mixed review of literature. *Autom. Constr.* 122, 103466. https://doi.org/10.1016/j.autcon.2020.103466

Offsite-Logistik, Just-in-time, Holzbau:
- Bataglin, F. S.; Viana, D. D.; Formoso, C. T.; Bulhões, I. R. (2020): Model for planning and controlling the delivery and assembly of engineer-to-order prefabricated building systems: exploring synergies between Lean and BIM. *Can. J. Civ. Eng.* 47(2), 165–177. https://doi.org/10.1139/cjce-2018-0462 – Fallstudie Betonfertigteile (ETO), übertragbar auf Holzelemente [U]
- Yi, W.; Wang, S.; Zhang, A. (2020): Optimal transportation planning for prefabricated products in construction. *Comput.-Aided Civ. Infrastruct. Eng.* 35(4), 342–353. https://doi.org/10.1111/mice.12504
- Hussein, M.; Zayed, T. (2021): Critical factors for successful implementation of just-in-time concept in modular integrated construction: A systematic review and meta-analysis. *J. Clean. Prod.* 284, 124716. https://doi.org/10.1016/j.jclepro.2020.124716
- Zhang, C. et al. (2024): Dual-objective optimization of prefabricated component logistics based on JIT strategy. *Sci. Rep.* 14. https://doi.org/10.1038/s41598-024-82689-w
- Lawani, K.; Okoro, C.; Tong, M.; Hare, B. (2020): Maximizing Construction of Timber Kit Homes Using Telescopic Crane to Improve Efficiency and Safety: A Case Study. *Sustainability* 12(24), 10238. https://doi.org/10.3390/su122410238 – Holzfertighaus mit Autokran, Wetter als Hauptursache für Stillstand

Primärquellen (Auswahl, URLs):
- Liebherr: LTM 1030-2.1/1060-3.1/1090-4.2/1160-5.2 (liebherr.com Produktseiten); MK 88-4.1E (liebherr.com/de-de/p/mk8841e-7387914); Crane Planner 2.0 (liebherr.com/en-int/mobile-and-crawler-cranes/service/crane-planner-2-0-5387400); „Influence of wind on crane operation“ (liebherr.com/shared/media/mobile-and-crawler-cranes/brochures/wind-influences/liebherr-influence-of-wind-p403-e04-2017.pdf); „Untergrund für sichere Kraneinsätze“ (Kundenmagazin)
- FEM 5.016 (fem-eur.com/wp-content/uploads/2016/03/CLE-5016-EN.pdf); EN 13000:2010/FprA1 (standards.iteh.ai)
- DGUV Information 208-059 (bgbau.de …/208-059_BGBAU_web.pdf); DGUV Information 208-019 Anh. 1; BG BAU B 213, C 412; DGUV Vorschrift 52 § 39; DGUV Vorschrift 38 § 16; DGUV Regel 109-017
- gesetze-im-internet.de: StVZO §§ 32, 34, 70; StVO §§ 22, 29, 46; BaustellV §§ 2, 3, Anhang II; BGB § 905
- OLG München 8 U 5531/20 (recht.nulegal.eu; juraforum.de); LG München II 13 O 3296/20 (lexika.de); OLG Stuttgart (Pressemitteilung)
- Landeshauptstadt München, Mobilitätsreferat: Leistungen 1072585 und 1072250, Antragsformulare, „Auflagen gegen Stillstand“; muenchen-transparent.de Dokument 6153813
- Schmid RAPID T-Lift (schmid-screw.com); Rothoblaas WASP (rothoblaas.com); Faymonville PrefaMAX; Langendorf Innenlader
- Regnauer: regnauer.de/hausbau/schluesselfertig, /ratgeber/fertighaus-kosten; Bauleistungsbeschreibung (AT)

## Warnungen

1. **Die Kranwerte in B18 sind erfunden** (gerundete Hüllkurven in der Größenordnung der Datenblätter). Sie sind nicht zur Einsatzplanung geeignet und zitieren keine Herstellertabellen. Echte Tabellen hängen von Auslegerlänge, Ballast, Abstützbasis (VarioBase) und Schwenkbereich ab.
2. **Die Stützkraft ist pauschal F_max.** Das ist nach DGUV korrekt konservativ [V]. Der Einsatzplaner liefert oft deutlich kleinere Werte (Liebherr-Beispiel 700 statt 1 109 kN) [V]. B18 überschätzt deshalb Plattengrößen.
3. **Die Windformel ist konservativ** und für Holztafeln drastisch (≈ 3 m/s). Ob Kranunternehmen für Holztafeln mit Auslastungsreserve höhere Werte freigeben, ist offen [U]. Keinesfalls mit dem 10-m-Mittelwind des Wetterdienstes rechnen: Die 3-s-Böe in Hubhöhe kann „um Faktor 2 und mehr“ höher sein [V FEM 5.016].
4. **Freileitung und Nachbar werden nur in 2D geprüft.** Leitungshöhe und Überschwenkhöhe gehen nicht ein (konservativ bzw. nur Hinweis). Die Last wird als Kreis mit halber Elementlänge angesetzt.
5. **Bodenzonen und Bodenkennwerte sind geschätzt** (DIN 1054:1976 über DGUV-Tabellen). Diese Werte sind historisch und kein Baugrundgutachten. Frisch verfüllte Arbeitsräume tragen weit weniger.
6. **Baumschutz München und DIN 18920** sind nicht geprüft. Die Sperrfläche „Krone + 1,5 m“ ist eine Annahme.
7. **Raster:** Enge Stellplätze erfordern ≤ 0,5 m oder eine exakte Randsuche. Ein Kran exakt an der Stellflächengrenze (hier 7,0 m in 7,0 m, p = p_zul) ist planerisch knapp und braucht Toleranzen [U].
8. **Rechtliches:** Die Aussagen zu BayAGBGB, Sondernutzung und BaustellV sind keine Rechtsauskunft. Art. 46b BayAGBGB habe ich nur über das Urteil zitiert, der Gesetzestext war nicht abrufbar [V mittelbar].
9. **Kapitel 2.8 der DGUV Regel 100-500 ist zurückgezogen.** Maßgeblich ist DGUV Regel 109-017; der Auftragstext nannte noch das alte Kapitel.

## Offene Fragen an Regnauer

1. **Kranpartner:** Welche Kranunternehmen und Krantypen (Autokran, Mobilbaukran) setzt Regnauer ein? Werden Einsatzplanungen mit LICCON oder Crane Planner bzw. Stützkraftberichte übergeben, und in welchem Format?
2. **Elementgewichte:** Wie viel wiegen die realen Wand-, Decken- und Dachelemente inkl. Fenster, Putz, Installation und Estrich? Steht das Gewicht im CAD/ERP (z. B. als Etikett)? Wie groß sind die maximalen Elementlängen und -höhen?
3. **Transportflotte:** Eigene Innenlader oder Spedition? Welche Gestelle bzw. A-Böcke, Stapelbreite, Ladehöhe, Nutzlast? Werden Übermaße (> 2,55 m) gefahren, mit Dauererlaubnis?
4. **Montagekolonnen:** Kolonnengröße, Tagesleistung (Elemente oder Hübe je Stunde), Arbeitszeitfenster, Montage an 1 oder 2 Tagen, Kran über Nacht?
5. **Wind:** Welche Windgrenze gilt intern für Holztafeln (Böe, Messort)? Wer entscheidet über Abbruch? Gibt es Erfahrungswerte für abgesagte Montagetage?
6. **Anschlagmittel:** Traverse, Hebebänder oder Schraubsysteme (RAPID T-Lift, WASP, Würth)? Welche Anschlagpunkte plant die Werkplanung, und stehen sie im Modell?
7. **Genehmigungen:** Wer beantragt Haltverbot, Sondernutzung und Nachbar-Anzeige (Regnauer, Kranpartner, Bauherr)? Welche Vorlaufzeiten gelten in München und im Landkreis?
8. **Just-in-time oder Zwischenlager:** Wird immer direkt vom LKW montiert? Wie lange steht ein LKW höchstens? Gibt es Abstellflächen oder Wechselbrücken?
9. **Baustellenaufnahme:** Welche Daten erhebt der Außendienst vor der Montage (Zufahrt, Freileitungen, Bäume, Bodenverhältnisse, Böschung)? Könnte das als strukturierte Checkliste bzw. GeoJSON in das Modell fließen?
10. **SiGe:** Bestellt Regnauer als GU einen SiGe-Koordinator? Wie wird Anh. II Nr. 10 BaustellV bei Holzelementen ausgelegt?

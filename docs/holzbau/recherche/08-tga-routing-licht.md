# Recherche 08: Gebäudetechnik (TGA), automatisches Routing und Licht im IFC-4.3-Modell

Stand: 27.09.2026. **[V]** = an Primärquelle, amtlicher Stelle, Normenverlag oder maschinell am Schema IFC4X3_ADD2 geprüft (IfcOpenShell 0.8.5, `ifcopenshell.validate` mit EXPRESS-Regeln); **[U]** = unsicher, Sekundärquelle oder eigene Bewertung. Normtexte (DIN/VDE) sind kostenpflichtig; Kernwerte stammen deshalb oft aus Inhaltsverzeichnissen des Verlags, Fachartikeln und Herstellerunterlagen. Das ist jeweils vermerkt. DOIs sind über die Crossref-API aufgelöst.

## Ergebnis in 5 Punkten

1. **Die Regeln gibt es fast überall schon, und sie sind geometrisch.** Installationszonen (DIN 18015-3), Bad-Schutzbereiche (DIN VDE 0100-701), 3-Liter-Regel (DVGW W 551), Gefälle und Lüftungsregeln (DIN 1986-100), Luftmengenformel (DIN 1946-6), Spitzendurchfluss (DIN 1988-300) und WP-Mindestabstände (LAI-Tabelle) lassen sich als Parameter, Sperrvolumen oder Formeln codieren [V]. Erfinden muss man fast nichts, wohl aber **abtippen**: Die DIN-Tabellen sind nicht maschinenlesbar und nicht frei lizenziert.
2. **IFC 4.3 trägt die ganze TGA.** Systeme, Kreise, Segmente, Formteile, Ports, Endgeräte, Verteiler und Aussparungen sind vorhanden. Ein Testmodell mit System, Rohren, Ports, Port-Verbindung und Aussparung validiert **fehlerfrei** gegen IFC4X3_ADD2 [V]. Es gibt Fallen: `IfcElectricDistributionBoard`, `IfcRelConnectsPortToElement` und die Proxy-PROVISIONFORVOID sind in 4.3 **deprecated**, und es gibt **keine `IfcHeatPump`** [V].
3. **Automatisches Routing ist in der Forschung gelöst, als Produkt nicht.** Den Stand geben A*/Dijkstra auf Voxel- oder Graphrastern mit Bogenstrafe, GA/Multi-Objective und regelbasierte Kanalführung (DOIs unten) [V]. Open Source gibt es nur Bausteine: IfcOpenShell `system`-API, ShapeBuilder-MEP-Formteile, IfcClash, voxelization_toolkit, networkx. In Bonsai ist ein A*-Router als Ausbaustufe erst geplant (Issue #6521, PR #8884) [V]. **Deshalb selbst bauen, als Graph-Suche mit Installationszonen als Kantenrestriktion.**
4. **Im Holzbau zählt die Wand, nicht der Raum.** Gerechnet wird der Durchbruch im Ständer oder Balken: nach DIN EN 1995-1-1/NA gelten Öffnungen über 50 mm als „Durchbruch“, kleinere als Querschnittsschwächung. Unverstärkte Durchbrüche sind nur eingeschränkt zulässig (≤ 0,15 h) [V/U]. Dazu kommen Luftdichtheit (luftdichte Dosen bzw. Installationsebene, DIN 18015-5/DIN 4108-7) und AFDD-Risikobewertung (VDE 0100-420) [V]. Die Router-Ergebnisse müssen als **BTLx/Maschinen-Bearbeitungen** (Dosenfräsung, Bohrung) in die Wandfertigung. Das können Dietrich's, cadwork und hsbcad, aber proprietär [V/U].
5. **Recht hat sich 2026 bewegt.** Das GEG heißt seit 29.07.2026 **Gebäudemodernisierungsgesetz (GModG)**, und die 65-%-EE-Pflicht ist entfallen [V]. Seit 12.02.2026 verlangt die EU-Gigabit-Infrastrukturverordnung (GIA, Art. 10) für neue Gebäude glasfaserfähige Infrastruktur **und** Glasfaserverkabelung [V]. Wohnlichtplanung bleibt **ohne verbindliche Norm**. Photometrie-Austausch über GLDF (XSD unter MIT-Lizenz), EULUMDAT/IES und `IfcLightSourceGoniometric` ist gelöst [V].

---

## 1 Elektro, Kommunikation, Smart Home

| Regel/Norm | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| DIN 18015-3:2016-09 Installationszonen Wand | **ZW-o** 15–45 cm unter Deckenbekleidung; **ZW-u** 15–45 cm über FFB; **ZW-m** 100–130 cm über FFB (nur Räume mit Arbeitsflächen); Breite max. 30 cm. **ZS-t/ZS-f/ZS-e** 10–30 cm neben Rohbaukanten (Türen an der Griffseite, Fenster beidseitig, Ecken); Breite max. 20 cm; über Türen min. 10 cm | als Rechtecke je Wandfläche erzeugbar (Parameter aus Öffnungen/Ecken) | [V] (Fachartikel elektro.net, Voltimum, JUNG) |
| DIN 18015-3 Decke/Boden | ZD-r: Breite max. 30 cm, Wandabstand min. 20 cm; ZD-t (Türdurchgang): Wandabstand min. 15 cm; 20 cm Abstand zu Zonen fremder Gewerke (Estrich) | Bänder auf Deckenfläche | [V] (elektro.net) |
| DIN 18015-3 Außenwand außen (AZW/AZS) | oben/unten 20–40 cm; an Türen/Fenstern 10–30 cm; an Wandkanten 50–70 cm | wie oben | [U] (nur JUNG-Übersicht) |
| DIN 18015-3 Vorzugshöhen | oberster Schalter/Steckdose neben Tür mittig **105 cm**; Steckdosen in ZW-u vorzugsweise Zonenmitte (30 cm); ZW-m-Mitte 115 cm | Konstanten | 105 cm [V], 30/115 cm abgeleitet [U] |
| DIN 18015-3 Ausnahme Leichtbau | In Fertigbauteilen/Leichtbauwänden darf von den Zonen abgewichen werden, wenn ≥ 6 cm Überdeckung **oder** Leitungen in unverfüllten Hohlräumen ausweichen können | Flag je Wandtyp; **gefüllte Gefache (Dämmung) erfüllen das nicht** [U] | Wortlaut [V] (elektro.net-Zitat) |
| DIN 18015-2:2021-10 Mindestausstattung | Stromkreise Steckdosen+Licht: ≤ 50 m² → 3; 50–75 → 4; 75–100 → 5; 100–125 → 6; > 125 m² → 7. Doppelsteckdose zählt als 2. Tabelle 2 mit Nutzungsbereichen (Küche < 20 m²: 3 allgemeine Steckdosen + je 1,20 m Arbeitsfläche …) | Tabelle abtippen | [V] (Hager, DIN-Presse) |
| RAL-RG 678 | Stern-Stufen: 1 = DIN 18015-2, 2 = Standard, 3 = Komfort, dazu „plus“-Stufen für Gebäudesystemtechnik nach DIN 18015-4 | HEA-PDF mit Tabellen je Raum | [V] (HEA) |
| DIN VDE 0100-701:2008-10 Bad | Bereich 0 = Wanneninneres; Bereich 1 bis **2,25 m** über FFB bzw. höchster fester Wasserauslass; Bereich 2 = **0,60 m** über Bereich 1 hinaus; bodengleiche Dusche: Bereich 1 mit **r = 1,20 m**; Fadenmaß 0,60 m um Abtrennungen; Steckdosen in Bereich 2 nur SELV/PELV/Rasiersteckdose; IPX4; Leitungen zu Bereich 1 senkrecht von oben/hinten; raumfremde Leitungen ≥ 6 cm Restwand oder RCD ≤ 30 mA | **Sperrvolumen (Extrusionen)** um IfcSanitaryTerminal | [V] (DIN Media Änderungsvermerk, elektro.net). Bereich 0 bei Dusche ohne Wanne (10 cm Höhe?) [U] |
| DIN VDE 0100-420:2019-10/2022-06 AFDD | Keine Pauschalpflicht. **Risiko- und Sicherheitsbewertung** für Schlafräume und für Räume aus Bauteilen mit brennbaren Baustoffen unter „feuerhemmend“. Holzrahmenbau mit Mineralwolle ist laut DKE nicht „überwiegend brennbar“. Praxishilfe BDF/DHV/ZDB/ZVEH | Regel: pro Raum Klassifikation → Bewertungsprotokoll | [V] (DKE-Erläuterung, BG BAU) |
| DIN VDE 0100-410/-520/-712 | RCD 30 mA für Steckdosen ≤ 32 A; Verlegearten; PV-Anlagen | Tabellen | [U] (Wortlaut nicht geprüft) |
| VDE-AR-N 4100:2019-04 (TAR NS) | Zählerplatz nach DIN VDE 0603: AAR 300 mm, Zählerfeld 450 mm (eHZ 300 + **RfZ 150 mm**); **APZ-Raum ≥ 300 mm** im Zählerschrank; Cat-5-Leitung APZ↔RfZ mit RJ45; Leerrohr **≥ 25 mm HÜP↔APZ**; freier Bedienbereich **1,2 m** tief, 2 m hoch; Kurzschlussfestigkeit 25/10/6 kA | Bauraum-Box vor dem Schrank = Clearance | [V] (VDE/FNN-Hinweis, Hager-Info); Neuausgabe? [U] |
| TAB Bayern (z. B. Bayernwerk) | ergänzt VDE-AR-N 4100 netzbetreiberspezifisch | nicht geprüft | [U] |
| DIN 18015-5 luftdicht | luftdichte Hohlwand- bzw. Massivholzdosen, Rohre an den Enden abdichten, Installationsebene bevorzugt; Zählerschrank/Verteiler an Innenwände | Wandschicht-Flag „luftdichte Ebene“ → Dosentyp | Inhalt [V] (ELEKTRO+, FLiB); Ausgabejahr [U] |
| BDF-Merkmal „Luftdichtheit“ | Installationsebene löst die Luftdichtheit im Holztafelbau **nicht generell**; bei Durchdringung der Beplankung luftdichte Dosen | Firmenregel | [V] (fertigbau.de) |
| **GIA (EU) 2024/1309 Art. 10** | Neue Gebäude, Bauantrag **ab 12.02.2026**: glasfaserfähige gebäudeinterne Infrastruktur **plus** Glasfaserverkabelung bis zum Netzabschlusspunkt (Zugangspunkt nur bei MFH Pflicht) | Pflicht-Teilsystem „FTTH“ | [V] (EUR-Lex, BMDS-FAQ) |
| § 145 Abs. 4 TKG | ältere Pflicht: passive Infrastruktur für „Netze mit sehr hoher Kapazität“ + Zugangspunkt | – | [V], wird durch GIA überlagert [V] |
| DIN EN 50173-4 / EN 50700 | Wohnungsverkabelung, Glasfaser-Heimnetz | nicht geprüft | [U] |
| KNX = EN 50090 / ISO/IEC 14543-3 | **kein offizielles KNX↔IFC-Mapping**. ETS 6 exportiert semantisch als JSON-LD/Turtle (KNX-Ontologie, Location-Modell „teilweise an IFC-Ontologie angelehnt“) | Brücke selbst bauen: IfcSensor/IfcActuator/IfcSwitchingDevice ↔ KNX-Device/Channel | [V] (KNX-Support) |
| Vorinstallation im Werk | Wandelemente werden im Werk mit Leerrohren und Dosen gefertigt; Wand-/Decken-Übergänge 90° (KAISER); Stecksysteme (Unicon); Freiblatt-Bearbeitungen und „Sperrflächen“ für Nagelbrücken in Dietrich's | Bearbeitung je Wandschicht | [V] (Herstellerunterlagen, Dietrich's-Forum) |

**Hinweis:** DIN 18015 ist eine Planungsnorm und gilt verbindlich nur bei vertraglicher Vereinbarung. Die VDE-Normen sind dagegen anerkannte Regeln der Technik (EnWG) [V, Voltimum]. Der Generator sollte das als Regelklasse „vertraglich“ bzw. „öffentlich-rechtlich/aaRdT“ führen.

## 2 Trinkwasser kalt und warm

| Regel/Norm | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| DIN 1988-300:2012-05 Spitzendurchfluss | **V̇S = a·(ΣV̇R)^b − c**, Wohngebäude a = 1,48, b = 0,19, c = 0,94; gültig 0,2 ≤ ΣV̇R ≤ 500 l/s; zweiter Waschtisch u. Ä. in derselben Sanitäreinheit zählt nicht | Formel | [V] (Herstellertabelle mit Zitat Tab. 3) |
| DIN 1988-300 Berechnungsdurchflüsse | V̇R je Armatur aus Tab. 2 oder Herstellerangabe; Start hinter dem Wasserzähler (pminWZ) | Tabelle abtippen | Tab. 2 nicht eingesehen [U] |
| DIN 1988-300 Geschwindigkeit | Hausanschluss ≤ 2 m/s; Verbrauchsleitungen je nach Einzelwiderständen bis 5 m/s (Begrenzung, nicht Dimensionierungsgröße) | Constraint | [V] (IKZ) |
| DIN EN 806-3 | vereinfachtes Belastungswertverfahren nur für Wohngebäude **≤ 6 Wohnungen** zulässig (Einschränkung durch DIN 1988-300) | Verfahrenswahl | [V] (IKZ) |
| DIN 1988-200 | Kaltwasser ≤ 25 °C (nach 30 s Zapfen); nicht planmäßig durchflossene Strecken ≤ 10 × DN | Constraints, Mindestabstand PWC zu Wärmequellen | [V] (irbnet-Fachartikel) |
| DVGW W 551 (2004) | **Kleinanlage**: EFH/ZFH immer. Speicher-Austritt ≥ 60 °C, Rücklauf Zirkulation ≥ 55 °C (Spreizung ≤ 5 K); ohne Zirkulation ≤ 3 l je Fließweg Speicher→Zapfstelle (Zirkulation zählt nicht mit) | **Rohrvolumen je Pfad = Σ π/4·di²·L ≤ 3 l** im Router als Constraint | [V] (DVGW-Artikel). Neufassung W 551-x? [U] |
| VDI/DVGW 6023:2013 | Stagnation vermeiden; Spülintervall 72 h (bis 7 d); 3-l-Richtwert | Prüfregel | [V] (irbnet) |
| Faustwert 3 l | ≈ 15 m DN15 bzw. ≈ 6 m DN25 | – | [V] (irbnet) |
| DIN 1988-100 / EN 1717 | Sicherungsarmaturen (Garten, Heizungsbefüllung) | Pflichtbauteil je Anschluss | [U] |

## 3 Abwasser und Regenwasser

| Regel/Norm | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| DIN 1986-100:2016-12 (Entwurf **E DIN 1986-100:2025-06**) | gültig zusammen mit DIN EN 12056-1…5 | – | [V] (DIN Media, DIN) |
| Anschlusswerte (System I) | Waschtisch 0,5; Dusche ohne Stöpsel 0,6 / mit 0,8; Badewanne 0,8; Küchenspüle 0,8; Geschirrspüler 0,8; Waschmaschine ≤ 6 kg 0,8; WC 6 l **2,0**, 4–4,5 l 1,8, 9 l 2,5; Bodenablauf DN 50/70/100 = 0,8/1,5/2,0 | Tabelle | [V] (mehrere Herstellerunterlagen übereinstimmend) |
| Abfluss | **Qww = K·√ΣDU**, K = 0,5 (Wohnhaus); Qww ≥ größter Einzel-DU | Formel | [V] |
| Unbelüftete Einzelanschlussleitung | Gefälle ≥ 1 %, L ≤ 4 m, ≤ 3 Umlenkungen à 90° (ohne Anschlussbogen), Höhendifferenz ≤ 1 m | Pfad-Constraints | [V] (IZEG, SBZ) |
| Mindestgefälle | unbelüftete Anschlussleitungen 1 %; belüftete 0,5 %; Sammel- und Grundleitungen im Gebäude 0,5 %; außerhalb 1:DN | Graph-Kantengewicht mit Höhenabnahme | [V] (SBZ) |
| Lüftung über Dach | **Jede Schmutzwasserfallleitung über Dach.** Belüftungsventile (DIN EN 12380) im EFH als Hauptlüftung **nur**, wenn mindestens die Fallleitung mit größter DN über Dach geht; ohne Fallleitungen ≥ 1 Lüftung DN 70 über Dach; keine Abdeckung auf der Mündung; Hauptlüftung in gleicher DN wie Fallleitung | Topologieregel | [V] (IZEG) |
| Durchdringung Dach | Lüftungsleitung durchdringt Luftdichtheits-, Dämm- und Dachebene → Manschette, IfcVirtualElement PROVISIONFORVOID | Aussparung erzeugen | [V/U] |
| Schallschutz DIN 4109-1:2018 | Anforderungen (LAF,max,n ≤ 30 dB(A) Wasser/Abwasser) gelten für **fremde** schutzbedürftige Räume. Im freistehenden EFH gibt es öffentlich-rechtlich keine Anforderung an Abwasserleitungen; Ausnahme: RLT im eigenen Wohnbereich (Tab. 10) | Regel „nur privatrechtlich“ (VDI 4100/DEGA) | [V] (DIN-Auslegungen, Normtext) |
| Regenwasser | Bemessung mit **KOSTRA-DWD-2020** (seit 01.01.2023; der Normenausschuss hält die Nutzung für zulässig) | Rasterdaten DWD frei | [V] (DIN NAW, DWD) |

## 4 Lüftung

| Regel/Norm | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| DIN 1946-6:2019-12 Lüftungskonzept | Notwendigkeit lüftungstechnischer Maßnahmen, wenn qv,Inf < qv,ges,NE,FL. Anhang A: normatives Ablaufschema | Entscheidungsbaum | [V] (DIN-FAQ, SBZ) |
| Luftvolumenstrom | **qv = f · (−0,002·A_NE² + 1,15·A_NE + 11)** m³/h; f = f_WS (FL) bzw. f_LSt: RL 0,7, NL 1,0, IL 1,3; A_NE < 20 m² → 20; > 210 m²: +0,4 m³/h je m² | Formel | [V]. Zahlenwert f_WS (typ. 0,3 bei Neubau) [U] |
| Auslegung ventilatorgestützt | mindestens Nennlüftung; qv,ges,NL = max(qv,NE,NL; min(Σ Abluft Räume; 1,2·qv,NE,NL)); Gleichzeitigkeit bei vielen Ablufträumen (Tab. 16) | Formel | [V] (DIN-FAQ) |
| Raumabluftwerte | Tab./Bild 8 der Norm; DIN-FAQ-Beispiel fensterloses Bad 40, WC 20 m³/h (DIN 18017-3) | Tabelle abtippen | Werte für 1946-6 selbst [U] |
| DIN 1946-6 Beiblatt 1:2025-06 | Beispielrechnungen → **Validierungsfälle für den Generator** | Testfälle | [V] (DIN Media) |
| Brandschutz Lüftung BayBO Art. 39 | Abs. 2–3 (nichtbrennbare Leitungen, Überbrückung feuerwiderstandsfähiger Bauteile) **gelten nicht in GK 1 und 2 und nicht innerhalb von Wohnungen** → M-LüAR im EFH praktisch nicht einschlägig; Abs. 4: Abluft ins Freie, nicht in Abgasanlagen | Regel | [V] (gesetze-bayern.de) |
| Leitungsanlagen BayBO/MLAR | Abschottungspflicht entfällt ebenso für GK 1/2 | Regel | [V] (StMB MLAR) |
| RLT-Schall eigene Wohnung | DIN 4109-1 Tab. 10: LAF,max,n ≤ 30 dB(A) Wohn/Schlaf (≤ 33 für Dauergeräusch-Fall) | Schalldämpfer-Pflichtprüfung | [U] (Tabellenlesung unscharf) |
| Kanalführung/Überströmung | Zuluft Wohn/Schlaf, Abluft Küche/Bad/WC, Überströmung Flur; Durchlassquerschnitte nach Norm | Raumrollen-Graph | Prinzip [V], Maße [U] |

## 5 Heizung und Wärmepumpe

| Regel/Norm | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| DIN EN 12831-1 + DIN/TS 12831-1:2020-04 | raumweise Norm-Heizlast; Norm-Innentemperatur Bad 24 °C, Wohnen 20 °C; Norm-Außentemperatur ortsabhängig | Rechenkern selbst oder Fremdtool | 24 °C Bad [V] (Musterberechnung); Ortswerte [U] |
| DIN EN 1264 Fußbodenheizung | θF,max: Aufenthaltszone **29 °C**, Randzone **35 °C**, Bad **33 °C** (ti + 9 K); Auslegung Rλ,B = 0,10 m²K/W (Bad 0,0); Spreizung 5 K im Auslegungsraum | Formel + Grenzkurven | [V] (Danfoss, Purmo) |
| Heizkreislänge | ≤ 100 m (Maximum 110, ideal 60); Druckverlust ≤ 300 mbar; Rohrlänge je m² = 100/VA[cm] (VA 10 → 10 m/m²) | Constraint im FBH-Mäandergenerator | [U] (Herstellerregel, keine Norm) |
| Hydraulischer Abgleich | VdZ-Formular Verfahren A/B; GModG/Förder-Kopplung | Formular-Export | [U] (Formular nicht geprüft) |
| **GModG** (GEG umbenannt, BGBl. 2026 I Nr. 226) | seit **29.07.2026**: 65-%-EE-Pflicht entfällt; Biotreppe für Gas/Öl ab 2029 (10/15/30/60 %) | Regel-Update im Regelwerk | [V] (Bundesregierung, gesetze-im-internet) |
| TA Lärm Immissionsrichtwerte | z. B. WA nachts 40 dB(A); Immissionsort 0,5 m vor geöffnetem Fenster | Konstante je Baugebiet | [V] (LAI-Langfassung) |
| **LAI-Leitfaden, 3. Aktualisierung 2023, Tab. 5** | Mindestabstand zum Immissionsort je Emissionspegel (L_WA + Reflexion + Tonzuschlag), z. B. 50 dB → WR 3,9 m / WA 1,9 m / MI 1,0 m; 55 dB → 7,6 / 3,9 / 1,9 m; 60 dB → 13,9 / 7,6 / 3,9 m; Toleranz 6 dB unter IRW eingerechnet | **Lookup-Tabelle** (40–80 dB) | Werte [V]; Spaltenzuordnung WR/WA/MI aus Randbedingungstext abgeleitet [U] |
| BayBO Art. 6 Abs. 1 S. 3 Nr. 4 | **Wärmepumpen und Einhausungen bis 2 m Höhe lösen keine Abstandsflächen aus** | Regel | [V] (gesetze-bayern.de) |

## 6 Licht

| Regel/Norm/Format | Kernwert | maschinenlesbar | Status |
|---|---|---|---|
| Wohnlichtplanung | **keine verbindliche Norm**; DIN EN 12464-1 nur Arbeitsstätten; DIN 18015-2 regelt nur **Anschlüsse** (Beleuchtungsauslässe je Raum, Flur je 6 m) | – | [V] (DIN 18015-2-Zusammenfassung); 12464-1-Umfang [U] |
| Tageslicht | DIN EN 17037 / DIN 5034-1 als Bezug | nicht geprüft | [U] |
| **GLDF** (DIAL + RELUX) | ZIP-Container (.gldf) mit product.xml, Photometrie aus EULUMDAT, IES LM-63 oder IES-XML (TM-33/UNI 11733), Geometrie L3D (OBJ); **XSD unter MIT-Lizenz**; .NET-Referenzbibliothek | XSD-validierbar | [V] (gldf.io, relux.com) |
| EULUMDAT / IES LM-63 | Lichtstärkeverteilung C/γ | Parser vorhanden (s. Bausteine) | [V] |
| IFC | `IfcLightFixture` (POINTSOURCE, DIRECTIONSOURCE, SECURITYLIGHTING), `IfcLamp` (LED …), `IfcLightSourceGoniometric` mit `LightDistributionDataSource` = **IfcExternalReference (EULUMDAT/IES-Datei)** oder `IfcLightIntensityDistribution` (TYPE_A/B/C + `IfcLightDistributionData`); `Pset_LightFixtureTypeCommon`, `Pset_SpaceLightingDesign` (Illuminance) | direkt | [V] (Schema + Doku) |
| Simulation | Radiance (Radiance Software License 2.0, BSD-artig), DIALux/Relux proprietär, liest GLDF | – | [V] |

## 7 IFC-4.3-Abbildung der TGA (maschinell geprüft, IFC4X3_ADD2)

| Konzept | Entität / PredefinedType [V] | Beziehung [V] | Bemerkung |
|---|---|---|---|
| Gewerk-System | `IfcDistributionSystem` (u. a. ELECTRICAL, LIGHTING, DOMESTICCOLDWATER, DOMESTICHOTWATER, SEWAGE, WASTEWATER, RAINWATER, VENT, VENTILATION, HEATING, DATA, COMMUNICATION, TV, EARTHING, POWERGENERATION, SECURITY) | `IfcRelAssignsToGroup`; `IfcRelServicesBuildings` → IfcBuilding/Storey/Space | Kanalentlüftung = VENT, Wohnungslüftung = VENTILATION |
| Stromkreis | `IfcDistributionCircuit` ELECTRICAL | Untersystem | ersetzt IfcElectricalCircuit seit IFC4 |
| Rohr / Kanal | `IfcPipeSegment` RIGIDSEGMENT/FLEXIBLESEGMENT; `IfcDuctSegment` | IfcRelContainedInSpatialStructure | `Pset_PipeSegmentTypeCommon` (NominalDiameter, InnerDiameter …) |
| Leerrohr / Kabel | `IfcCableCarrierSegment` **CONDUITSEGMENT**; `IfcCableSegment` CABLESEGMENT; `IfcCableFitting`, `IfcCableCarrierFitting` (BEND, TEE …) | – | Glasfaser: CABLESEGMENT/`OPTICALCABLESEGMENT` |
| Formteil | `IfcPipeFitting`/`IfcDuctFitting` (BEND, JUNCTION, TRANSITION, OBSTRUCTION …) | – | **kein „IfcElbow“** (Bonsai-Issue-Vorschlag irrt) |
| Dose | `IfcJunctionBox` POWER/DATA („enthält Kabel, Steckdosen und/oder Schalter“) | – | Hohlwanddose |
| Anschlusspunkt | `IfcDistributionPort` (PIPE, DUCT, CABLE, CABLECARRIER, WIRELESS), FlowDirection SOURCE/SINK, SystemType | **`IfcRelNests`** (Element→Ports), **`IfcRelConnectsPorts`** (Port↔Port, optional RealizingElement) | `IfcRelConnectsPortToElement` in 4.3 **deprecated** |
| Endgeräte | `IfcOutlet` (POWEROUTLET, DATAOUTLET, …), `IfcSanitaryTerminal` (WASHHANDBASIN, SHOWER, TOILETPAN, BATH …), `IfcWasteTerminal` (FLOORTRAP …), `IfcAirTerminal` (DIFFUSER, GRILLE …), `IfcSpaceHeater` (RADIATOR, CONVECTOR), `IfcLightFixture`, `IfcStackTerminal` (COWL = Dachhaube) | – | |
| Schalt-/Schutzgeräte | `IfcSwitchingDevice` (TOGGLESWITCH, DIMMERSWITCH, MOMENTARYSWITCH …), `IfcProtectiveDevice` (CIRCUITBREAKER, RESIDUALCURRENTCIRCUITBREAKER, …) | `IfcRelFlowControlElements` | AFDD: USERDEFINED [U] |
| Verteiler / Zähler | **`IfcDistributionBoard`** (CONSUMERUNIT, DISTRIBUTIONBOARD, DISTRIBUTIONFRAME …); `IfcFlowMeter` (ENERGYMETER, WATERMETER) | Ports laut Doku: SINK_Line, SINK_Ground, SOURCE_CircuitN | `IfcElectricDistributionBoard` **deprecated** in 4.3 |
| Wärmepumpe | **keine IfcHeatPump**; `IfcUnitaryEquipment` (Doku nennt Wärmepumpen als Beispiel; Enum ohne HEATPUMP → USERDEFINED/ObjectType) oder `IfcChiller` | – | [V] |
| Lüftungsgerät WRG | `IfcAirToAirHeatRecovery` (FIXEDPLATECOUNTERFLOWEXCHANGER …), `IfcFan`, `IfcDuctSilencer`, `IfcFilter` | Aggregat per IfcRelAggregates | Pset_DistributionSystemTypeVentilation |
| Speicher, Pumpe, Ventil | `IfcTank`, `IfcPump` CIRCULATOR, `IfcValve` (ISOLATING, CHECK, REGULATING, MIXING …) | – | |
| Smart Home | `IfcSensor` (TEMPERATURESENSOR, CO2SENSOR, MOVEMENTSENSOR …), `IfcActuator`, `IfcController`, `IfcCommunicationsAppliance` (ROUTER, OPTICALNETWORKUNIT, GATEWAY) | IfcRelFlowControlElements | ONT = OPTICALNETWORKUNIT |
| PV / Batterie | `IfcSolarDevice` SOLARPANEL, `IfcElectricFlowStorageDevice` BATTERY, `IfcTransformer` INVERTER | – | |
| Aussparungsvorschlag | **`IfcVirtualElement` PROVISIONFORVOID** + `Pset_ProvisionForVoid` (VoidShape, Width, Height, Diameter, Depth, System); **kein Material zulässig** | Tiefe ≥ Bauteildicke, Swept Solid | Proxy-Variante seit 4.3 deprecated |
| Freigegebene Öffnung | `IfcOpeningElement` OPENING/RECESS | `IfcRelVoidsElement` (Wand/Ständer/Platte), Leitung ↔ Bauteil: `IfcRelInterferesElements` (ImpliedOrder TRUE = aus RelatingElement abziehen) | im Holzbau pro Schicht/Teil (IfcMember, IfcPlate) |
| Kollisionsergebnis | `IfcRelInterferesElements` InterferenceType „Clash“ (ImpliedOrder FALSE) bzw. BCF | – | |

**Prüfprotokoll:** Skript im Scratchpad (`mep_test.py`) erzeugt IfcProject → Site → Building → Storey, `IfcDistributionSystem` DOMESTICCOLDWATER + `IfcRelServicesBuildings`, zwei `IfcPipeSegment` mit Profil-Extrusion, je zwei Ports (`system.add_port` → IfcRelNests), `system.connect_port` (→ IfcRelConnectsPorts), `IfcVirtualElement` PROVISIONFORVOID mit Pset und `IfcOpeningElement` via `feature.add_feature` (→ IfcRelVoidsElement). `ifcopenshell.validate(..., express_rules=True)` ergibt **0 Fehler**. Ohne ObjectPlacement meldet die Regel `IfcProduct.PlacementForShapeRepresentation` einen Fehler; Segmente brauchen also immer eine Platzierung [V]. `ifcopenshell.util.system.get_connected_to()` findet die Topologie wieder [V].

**Merkmale/Produktdaten:** VDI 3805 (Blatt 1 Entwurf 2020-10, Einspruchsfrist 31.03.2021; eigenes Satzformat mit Geometrie, Störräumen, Anschlüssen) ist Grundlage der **ISO 16757** (Teil 1+2 veröffentlicht, Geometrie auf STEP/IFC-Basis) [V]. VDI 3805 ist kein IFC, braucht also einen Konverter auf IfcTypeProduct + Ports [U]. Für Merkmale bSDD (IFC-4.3-Psets sind dort veröffentlicht) [U]. BIM-Portal des Bundes nicht geprüft [U].

## 8 Automatisches Routing

### 8.1 Literatur (DOI über Crossref aufgelöst)

| Arbeit | Methode | Relevanz | DOI |
|---|---|---|---|
| Choi, Kim, Heo, Na (2022), IEEE Access | modifizierter A* für MEP-Pfade (Bogenkosten) | Kernalgorithmus | 10.1109/ACCESS.2022.3184106 [V] |
| Singh, Cheng (2020), ICCCBE 2020, LNCE | 3D-Mehrrohr-Layout, BIM + heuristische Suche | Mehrleitungs-Sequenzierung | 10.1007/978-3-030-51295-8_6 [V] |
| Medjdoub, Bi (2018), Automation in Construction | parametrische, constraint-basierte Kanalführung | Regeln als Constraints | 10.1016/j.autcon.2018.02.006 [V] |
| Medjdoub, Chenini (2013), AEDM | Constraint-Modell für TGA-Entwurf | Hintergrund | 10.1080/17452007.2013.834812 [V] |
| Chen, Guan, Yuan, Xie, Xu (2022), Automation in Construction | **regelbasierte** HVAC-Kanalführung | Vorbild Regelbasis | 10.1016/j.autcon.2022.104264 [V] |
| Liang, Wang, Wang, Yoon (2023), J. Building Eng. | regelbasiertes automatisches Kanallayout | dito | 10.1016/j.jobe.2023.107946 [V] |
| (2024), Buildings 14(12) 3826 | GA-Längenoptimierung modularer MEP-Leitungen | Vorfertigung | 10.3390/buildings14123826 [V] |
| (2025), Buildings 15(12) 2093 | **Review** Pfadoptimierung für MEP-Rohre | Überblick | 10.3390/buildings15122093 [V] |
| Zhang, Zhu, Joneja (2026), Automation in Construction | multikriterielles Mehr-Rohr-Routing in Technikräumen | Stand 2026 | 10.1016/j.autcon.2026.107201 [V] |
| (2025), Trans. Inst. Measurement & Control (SAGE) | Deep RL (diskreter SAC) für Rohrlayout | RL-Variante, nicht gebäudespezifisch | 10.1177/01423312251326630 [V] |
| (2022), Automation in Construction | AR-gestützte automatische Leitungsplanung zur Konfliktlösung | Kollisionsbehebung | 10.1016/j.autcon.2022.104400 [V] |
| Zhang, Tian, Wang, Al-Hussein (2020), CRC 2020 | BIM-basiertes automatisches Entwässerungsdesign **in der Vorfertigung** | nah an Fertighaus | 10.1061/9780784482865.121 [V] |
| Shin et al. (2024), JCDE | CAD→BIM Sanitär-Entwässerung | Abwasser-Topologie | 10.1093/jcde/qwae021 [V] |
| (2022), Buildings 12(7) 934 | automatische Regelprüfung MEP (BIM + KBMS) | Prüffähigkeit | 10.3390/buildings12070934 [V] |
| Solihin, Eastman (2015), Automation in Construction | Klassifikation von Regeln für Rule Checking | Regeltaxonomie | 10.1016/j.autcon.2015.03.003 [V] (Autoren [U]) |
| (2022), Buildings 12(7) 1044 | Hindernisse bei Vorfertigung Holz + TGA | Kontext Holzbau | 10.3390/buildings12071044 [V] |

Einen Artikel zu **Routing speziell in Holzrahmen-Wandtafeln** unter Ständer- und Zonenregeln habe ich nicht gefunden [U]. Das ist eine echte Forschungslücke.

### 8.2 Übertragbares Verfahren (eigene Bewertung [U])

1. **Graph statt Voxel.** Knoten entstehen an Zonenkreuzungen (DIN 18015-3 ZW/ZS/ZD), an Gefachen zwischen Ständern (Rastermaß aus Wandaufbau), an Ports und an Wand-/Deckenübergängen. Kanten dürfen nur innerhalb erlaubter Zonen und Schichten liegen (Installationsebene oder Gefach). Gewicht = Länge + Bogenstrafe + Ständerbohrungs-Strafe + Durchdringung der Luftdichtebene (hoch) + Querung Bad-Schutzbereich (verboten). Rechnen mit A*/Dijkstra (networkx).
2. **Gewerkreihenfolge:** Abwasser zuerst (Gefälle, DN groß, Fallleitung über Dach als harte Topologie), dann Lüftung (Kanäle im Deckenfeld), Trinkwasser (3-l-Pfad-Constraint), Heizung (FBH-Mäander raumweise), Elektro zuletzt.
3. **Geometrie:** Segmente/Formteile mit ShapeBuilder (`mep_bend_shape`, `mep_transition_shape`). Ports verbinden. Pro Kreuzung Bauteil×Leitung ein `IfcVirtualElement` PROVISIONFORVOID. Nach Holzbau-Prüfung wird daraus `IfcOpeningElement` in IfcMember/IfcPlate und daraus BTLx-Drilling/Slot bzw. Dosenfräsung.
4. **Prüfung:** IfcClash (intersection/collision/clearance → BCF) plus Regelprüfer (Zonen, 701-Volumen, Gefälle, 3 l, Durchbruchsgeometrie) plus IDS für Merkmale.

### 8.3 Holzbau-Durchbrüche

| Regel | Kernwert | Status |
|---|---|---|
| DIN EN 1995-1-1/NA:2013-08, NCI NA.6.7 | Öffnungen **> 50 mm** lichtes Maß = Durchbruch; kleinere wie Querschnittsschwächung (Nettoquerschnitt) | [V] (pcae/FRILO-Handbücher zitieren NA.1/NA.3) |
| NA.6.7 Geometrie unverstärkt | hd ≤ 0,15 h; Gruppen (lz < 1,5 h) unzulässig; hro/hru ≥ 0,35 h | [V] (Fachbeitrag forum-holzwissen, Stucki) |
| Anwendungsbereich | FRILO: Durchbrüche nur für BSH berechnet; nach prEN 1995-1-1:2023 müssen Durchbrüche in KVH/Vollholz (ST/FST) **verstärkt** werden, unverstärkt nur GL/GST/LVL-P | [V] Entwurf / [U] Endfassung |
| Ständer (Druckstab) | EC5 hat keine eigene „Ständerbohr“-Regel: Nettoquerschnitt im Knick-/Druck-Nachweis; Firmenregel (Bohrung mittig, max. Anteil der Tiefe) **bei Regnauer erfragen** | [U] |
| Informationsdienst Holz | konkrete Bohrregeln für Ständer nicht als Primärquelle gefunden | [U] |

## 9 Bausteine und Urteil

| Baustein | Lizenz | Nutzen | Urteil |
|---|---|---|---|
| IfcOpenShell 0.8.5 (`api.system`: add_system/add_port/connect_port/assign_system; `util.system`; `validate`) | LGPL-3.0+ [V] | IFC-TGA schreiben, prüfen, Topologie lesen | **übernehmen** |
| ShapeBuilder `mep_bend_shape`, `mep_transition_shape` | LGPL-3.0+ [V] | Bögen, Reduzierungen | **übernehmen** |
| IfcClash 0.8.5 (PyPI, BCF/JSON-Export, clearance) | LGPL-3.0+ [V] | Kollision/Abstand | **übernehmen** |
| Bonsai (Blender-Extension) MEP-Werkzeuge | GPL-3.0 [U] | interaktive Nachbearbeitung, Viewer | **adaptieren** (nicht linken: GPL) |
| IfcOpenShell voxelization_toolkit | Lizenz [U] | Voxel + Dilatation für Abstände | **adaptieren** (optional) |
| networkx 3.7 | BSD-3 [V] | A*/Dijkstra auf Zonen-Graph | **übernehmen** |
| python-fcl / trimesh | BSD / MIT [V] | schnelle Kollisionsabfrage beim Routing | **übernehmen** |
| Router für Holzrahmen-Zonen | – | es gibt keinen | **selbst bauen** |
| Regelprüfer (Zonen, 701, Gefälle, 3 l, NA.6.7) | – | – | **selbst bauen** (Werte aus Normen abtippen, Lizenz beachten) |
| Radiance 6.x / pyradiance 1.3 | Radiance License 2.0 (BSD-artig) / BSD [V] | Lichtberechnung, Renderings | **übernehmen** |
| honeybee-radiance, ladybug-geometry | AGPL-3.0 [V] | Komfort-Wrapper | **meiden** (AGPL) oder nur als Dienst |
| `eulumdat` (PyPI 0.7.1) | AGPL-3.0+ [V] | LDT-Parser | **selbst bauen** (EULUMDAT ist ein einfaches Textformat) |
| GLDF-XSD, gldf.net | MIT [V] / Lizenz gldf.net [U] | Leuchtendaten-Container | **übernehmen** (XSD), Parser selbst in Python |
| pandapower | BSD [V] | Lastfluss/Spannungsfall (überdimensioniert fürs EFH) | optional |
| pvlib | BSD-3 [V] | PV-Ertrag | **übernehmen** |
| KNX ETS Semantic Export (JSON-LD) | KNX-Lizenzbedingungen [U] | Smart-Home-Brücke | **adaptieren** |
| **Achtung:** PyPI-Paket „bonsai“ | MIT | ist ein **LDAP-Client**, nicht Bonsai-BIM | nicht verwechseln [V] |

**Kommerzielle Referenzen (nur Vergleich):** Dietrich's (DICAM, HRB-Modul, Freiblatt-Bearbeitungen, Sperrflächen für Weinmann-Nagelbrücken) [V, Forum]; cadwork Elementfertigung/Multifunktionsbrücke (Bohren/Fräsen schichtweise, Weinmann WALLTEQ) [V]; hsbcad [U]; SEMA [U]; Weinmann-Anlagen als Empfänger [V]; DDS-CAD (Elektro/HKLS, IFC-Export mit „Provision for Void“, Leerrohre, Kabel; IFC-2x3-CV-2.0-zertifiziert 2014) [V]; Trimble Nova (ehem. Plancal nova, IFC-Import/Export, Schnittstellen DIALux/RELUX) [V]; liNear [U]. **Keiner davon generiert TGA regelbasiert aus dem Grundriss** [U].

## Korrekturen und Warnungen

1. **`IfcElectricDistributionBoard` nicht mehr verwenden.** In IFC 4.3 ist es deprecated; richtig ist `IfcDistributionBoard` [V].
2. **Ports über `IfcRelNests`, nicht `IfcRelConnectsPortToElement`**, das in 4.3 deprecated ist [V].
3. **Aussparungsvorschlag = `IfcVirtualElement` PROVISIONFORVOID**, ohne Material. `IfcBuildingElementProxy` PROVISIONFORVOID ist deprecated [V].
4. **Es gibt keine `IfcHeatPump` und kein `IfcElbow`** [V].
5. **Installationszonen gelten auch in Ständerwänden** (DIN 18015-3 4.2.1). Die Ausnahme für Leichtbau verlangt ≥ 6 cm Überdeckung oder **ausweichfähige Leitungen in unverfüllten Hohlräumen**. Gedämmte Gefache sind nicht unverfüllt [V Wortlaut / U Auslegung].
6. **DIN 4109 schützt im EFH nur gegen RLT-Geräusche im eigenen Bereich**, nicht gegen Abwasser. Schallschutz der Fallleitung ist dort nur Vertragsqualität [V].
7. **M-LüAR/MLAR sind im EFH (GK 1/2) nicht einschlägig** (BayBO Art. 39 Abs. 5, Art. 38 bzw. MLAR 4.1.1) [V]. Brandschutz im Holzbau bleibt über die AFDD-Risikobewertung und die Bauteilklassen relevant.
8. **AFDD ist keine Pauschalpflicht mehr** (seit VDE 0100-420:2019). Nötig ist eine dokumentierte Risikobewertung, die der Generator als Protokoll erzeugen sollte [V].
9. **„TKG § 145“ reicht nicht mehr aus.** Seit 12.02.2026 verlangt die GIA Art. 10 für Neubauten auch die Glasfaserverkabelung selbst [V].
10. **„GEG § 71 65 %“ ist Geschichte**, seit 29.07.2026 gilt das GModG. Das betrifft ältere Recherchen im Projekt (z. B. 02, 05) [V].
11. **LAI-Abstände sind Empfehlungen**, verbindlich ist die TA Lärm. Die Tabelle rechnet 6 dB Irrelevanz ein [V].
12. **DIN-Tabellenwerte sind urheberrechtlich geschützt.** Als eigene Datendateien nur mit Quellenangabe und im Rahmen der Lizenz nutzen [U].
13. **VDI 3805 ist kein IFC**, und ISO 16757 ist erst teilweise fertig [V].
14. **Routing im Holzbau ist ein Fertigungsproblem.** Jede Bohrung durch Ständer, Schwelle oder Rähm braucht eine NA.6.7-/Nettoquerschnittsprüfung und eine Maschinenbearbeitung [V/U].

## Offene Fragen an Regnauer

1. Welche **TGA-Gewerke** installiert Regnauer im Werk vor (Leerrohre, Dosen, Kabel, Wasser, Abwasser, Lüftungskanäle), und welche macht die Baustelle? Gibt es Steckverbinder an Wandstößen (z. B. Unicon)?
2. Gibt es eine **Installationsebene** (Vorsatzschale, Tiefe?) in Außen- und Innenwänden, und welche Schicht ist die **luftdichte Ebene** (OSB verklebt, Folie)? Welche Dosentypen (luftdicht, Massivholz, Brandschutz) sind Standard?
3. **Firmenregeln für Bohrungen** in Ständern, Schwellen, Rähmen und Deckenbalken: maximaler Durchmesser, Lage, Abstände, Verstärkung? Welches KVH/BSH wird verwendet?
4. Welche **CAD/CAM-Kette** (Dietrich's, hsbcad, cadwork, SEMA?) und welche **Anlage** (Weinmann, Homag) übernimmt Dosenfräsungen und Bohrungen, und in welchem Format (BTLx, WUP, herstellerspezifisch)?
5. **Standard-Ausstattungswert** Elektro (RAL-RG 678, 1–3 Sterne, plus?), KNX oder Funk-Smart-Home, Standard-Zählerschrank (Anzahl Zählerplätze für WP, PV, Wallbox) und Netzbetreiber-TAB (Bayernwerk o. a.)?
6. **Heizsystem-Standard:** Luft-WP innen oder außen, Split oder Monoblock, Fußbodenheizung (System, VA, Estrich nass oder trocken), Heizlast-Software? Wer macht hydraulischen Abgleich und LAI-Nachweis?
7. **Lüftung:** zentrale WRG oder dezentral? Kanalsystem (flexibel rund, Flachkanal), Verlegung in Decke oder Estrich, Gerätestandort?
8. **Sanitär:** Vorwandsystem (Hersteller), Fallleitung durch Deckenelemente, Schallschutzstandard (VDI 4100-Stufe vertraglich?), Belüftungsventil oder immer über Dach?
9. Welche **TGA-Planungssoftware** nutzen Fachplaner oder Partner (DDS-CAD, Trimble Nova, liNear), und wird IFC tatsächlich ausgetauscht?
10. Werden **Leuchten** geplant und geliefert (Hersteller mit GLDF/EULUMDAT?) oder nur Auslässe nach DIN 18015-2?
11. **Glasfaser (GIA):** Wer verlegt die Glasfaserverkabelung bis zum Netzabschluss (Werk, Baustelle, Netzbetreiber), und wo sitzen HÜP und APZ?

---

*Quellen (Auswahl, alle am 27.09.2026 abgerufen):* DIN Media und din.de (Norm-Inhaltsverzeichnisse und Änderungsvermerke zu DIN 18015-2/-3, DIN VDE 0100-701, DIN 1986-100, E DIN 1986-100:2025-06, DIN 1946-6, DIN 1946-6 Bbl 1:2025-06, DIN 4109-1, DIN EN 1995-1-1/NA); DKE-Erläuterung zu VDE 0100-420 Abschnitt 421.7; VDE FNN-Hinweis Zählerplätze; Hager-Tipp VDE-AR-N 4100; elektro.net (Installationszonen, Bad, Leichtbau); ELEKTRO+, FLiB, BDF-Merkblatt Luftdichtheit; DVGW-Artikel W 551; IKZ/irbnet zu DIN 1988-300/-200; IZEG-Info Lüftung Entwässerungsanlagen; DIN-FAQ DIN 1946-6; LAI-Leitfaden 3. Aktualisierung 2023 (lai-immissionsschutz.de); gesetze-bayern.de (BayBO Art. 6, 39); StMB MLAR und Rundschreiben Luftwärmepumpen; gesetze-im-internet.de (GModG, TKG § 145); bundesregierung.de, bundestag.de, bundesrat.de Drs. 409/26; EUR-Lex und BMDS-FAQ zur GIA; gldf.io, relux.com; KNX-Support; VDI/vdi3805.eu, ISO TC 59/SC 13 (ISO 16757); buildingSMART IFC4.3.x-development (Doku-Quelltexte); PyPI-Metadaten; Crossref-API für alle DOIs.

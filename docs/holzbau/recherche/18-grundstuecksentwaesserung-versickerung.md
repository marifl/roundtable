# Recherche 18: Grundstücksentwässerung und Versickerung – vom Gebäude bis zum Kanal (Referenz München)

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft (Satzungs- oder Verordnungstext, Behördenseite, Normenverlag) oder maschinell nachvollzogen (IfcOpenShell 0.8.5 gegen IFC4X3_ADD2, Nachrechnung veröffentlichter Bemessungen, PyPI-Metadaten). **[U]** = unsicher, Sekundärquelle oder eigene Bewertung. DIN- und DWA-Volltexte sind kostenpflichtig; ihre Werte stammen hier aus Inhaltsverzeichnissen, Fachartikeln (SBZ, BauNetz, IZEG, Haustec) und kommunalen Merkblättern und sind entsprechend markiert. Crossref und die DWD-Server waren aus der Arbeitsumgebung gesperrt. DOIs stammen deshalb aus den Verlagsseiten.

**Anschluss an frühere Recherchen (hier nicht wiederholt):**
- Recherche 08, Abschnitt 3: Abwasser im Gebäude, also Anschlusswerte DU, Q_ww = K·√ΣDU, Mindestgefälle innen/außen, Lüftung über Dach, KOSTRA-DWD-2020 für Regenwasser.
- Recherche 09, Abschnitt 8: Dachentwässerung mit r(5,5), Rinnen und Fallrohre, KOSTRA frei nach GeoNutzV, IFC `GUTTER`/`RAINWATERHOPPER`.

Diese Recherche beginnt am Fuß der Fallleitung bzw. am Standrohr und endet am Einlassstück des städtischen Kanals bzw. in der Versickerungsanlage.

## Ergebnis in 5 Punkten

1. **München regelt die Grundstücksentwässerung im Volltext und fast maschinenlesbar.** Maßgeblich sind die Entwässerungssatzung (EWS vom 28.08.2018, geändert 08.05.2024) und der *Leitfaden Grundstücksentwässerung* der MSE (7. Auflage, Stand 08.06.2026). Beide enthalten die Kernwerte eines Generators [V]:
   - Revisionsschacht am Ende der Anlage auf eigenem Grund; außenliegend, sobald zwischen Grenze und Gebäude ≥ 5 m frei sind.
   - Frostfreie Tiefe **1,20 m GOK bis Rohrsohle**; Niederschlagsleitungen zur Versickerung 0,80 m.
   - Anschlusskanal geradlinig und ohne Gefällewechsel, **Steilgefälle bis 1:1** erlaubt.
   - Rückstauebene = Straßenoberkante an der Anschlussstelle.
   - Plansatz: Lageplan 1:1000, Grundriss 1:100, Abwicklung 1:100 in wahrer Länge, Höhen in DHHN2016, **keine rote Farbe**.

   Nennweite, Zahl und Führung des Anschlusskanals sowie den Anschlusspunkt bestimmt die MSE (§ 9 Abs. 2). Das Technische Formblatt ist deshalb **Eingabedatum**, nicht Planungsergebnis.
2. **Niederschlagswasser gehört in München nicht in den Kanal.** Ein Benutzungsrecht besteht nicht, soweit Versickerung möglich ist (EWS § 4 Abs. 4). Versickerungsanlagen dürfen keinen Überlauf zum Kanal haben (Leitfaden 5.2) [V]. Erlaubnisfrei ist die Versickerung nach NWFreiV/TRENGW unter diesen Bedingungen [V]:
   - höchstens 1000 m² befestigte Fläche je Anlage,
   - vorrangig flächenhaft über ≥ 20 cm bewachsenen Oberboden, Fläche ≥ 1/15 der angeschlossenen Fläche,
   - Rigole/Sickerschacht **nur, wenn flächenhaft nicht möglich**, und nur mit Vorreinigung,
   - Sohle ≤ 5 m unter GOK und ≥ 1 m über dem MHGW.

   Der Prototyp zeigt, dass im Beispiel eine Mulde von 17 m² Platz fände. Die Rigole wäre also zu begründen, und genau diese Prüfung wird in der Praxis oft übersprungen.
3. **DWA-A 138-1 (10/2024) hat die Bemessung geändert, und die neuen Formeln sind ohne Normtext reproduzierbar.** Die Änderungen:
   - k_i = k_f · f_Ort · f_Methode ersetzt k_f/2.
   - Die Rigole versickert auch über die Stirnflächen: A_S,m = b·L + h·(L + b).
   - Einfaches Verfahren nach DWA-A 117 (T ≤ 10 a, t_f ≤ 15 min).
   - Vorbehandlung grundsätzlich auch für Dachflächen.

   Zwei veröffentlichte A-138-1-Rechnungen lassen sich exakt nachrechnen: V_erf = 40,52 m³ bzw. L = 27,45 m [V, Test]. Die Tabellen 9–11 (C_m, f_Ort, f_Methode) bleiben kostenpflichtig.
4. **Das Routing auf dem Grundstück ist ein kleines Steinerbaum-Problem mit Gefällebedingung.** Die Forschung löst Layout und Hydraulik öffentlicher Netze mit MILP, Spannbäumen, kürzesten Wegen und Metaheuristiken (DOIs unten). Fürs Einzelgrundstück genügt ein deterministisches Verfahren:
   - Sichtbarkeitsgraph,
   - Takahashi-Matsuyama-Heuristik,
   - zweistufiger Höhenplan: vorwärts Mindestgefälle und Frosttiefe, rückwärts Höchstgefälle.

   Der Prototyp **B17** rechnet vier Szenarien in 1,3 s. **20 Tests sind grün**, das IFC hat **0 Validierungsmeldungen** und ist über zwei Prozesse byte-identisch [V].
5. **IFC 4.3 bildet die Grundstücksentwässerung weitgehend ab, nur nicht die Versickerung** [V, Schemaabfrage]. Vorhanden sind:
   - `IfcDistributionSystem` SEWAGE/RAINWATER/STORMWATER,
   - `IfcPipeSegment` mit `Pset_PipeSegmentOccurrence.Gradient/InvertElevation`,
   - `IfcDistributionChamberElement` MANHOLE/INSPECTIONCHAMBER,
   - `IfcInterceptor`, `IfcTank` STORAGE (`StorageType` RAINWATER), `IfcGeographicElement` TERRAIN, `IfcGeotechnicalStratum` WATER.

   Es fehlt eine Klasse für Rigole, Mulde oder Sickerschacht und ein Pset für k_f/MHGW. Der saubere Weg ist USERDEFINED mit ObjectType und eigenem Pset.

---

## 1 Regelwerk: Regel – Kernwert – Quelle – Status

### 1.1 DIN 1986-100 und Europäische Normen

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Ausgabe | DIN 1986-100:2016-12. **E DIN 1986-100:2025-06** integriert DIN 1986-4, überarbeitet Abschnitt 13 Rückstau (Rückstauebene, Rückstauschleife, Rückstauverschlüsse) und 14.10 Überflutungsnachweise und ergänzt Anhang D Dichtheitsprüfung und Anhang F zeichnerische Darstellung; Tabelle 3 „Maße von Einsteigschächten und Inspektionsöffnungen“ | DIN Media, DIN-Inhaltsverzeichnis | [V] |
| Anschlusskanäle | „Anschlusskanäle werden in diesem Dokument nicht behandelt“ → kommunales Recht (EWS/MSE) | DIN Media, Anwendungsbereich | [V] |
| Grundleitung im Gebäude | Grundleitungen innerhalb von Gebäuden vermeiden, besser Sammelleitungen (6.1.1) | baunormenlexikon (Normtext-Auszug) | [V] |
| Mindestgefälle | im Gebäude 0,5 %; außerhalb **1:DN** (DN 150 → 0,67 %) | BauNetz Wissen, SBZ | [V, Sekundärquelle] |
| Füllungsgrad, Geschwindigkeit | h/d = 0,5 und v ≥ 0,5 m/s im Gebäude; h/d = 0,7 und v ≥ 0,7 m/s außerhalb | BauNetz Wissen | [V, Sekundärquelle] |
| Nennweiten | Grundleitung ≥ DN 100; bis zum nächsten Schacht außen DN 80 zulässig, wenn die Hydraulik es erlaubt; Nennweite in Fließrichtung nicht verringern (6.1.8) | Haustec (Ishorst 2020), BauNetz | [V, Sekundärquelle] |
| Innendurchmesser (Tab. A.3) | DN 100/125/150/200 → di 96/113/146/184 mm | baunormenlexikon (Tabellenkopf) | [V] |
| Reinigungsöffnungen | am Fuß jeder Fallleitung; in Grundleitungen ≤ 20 m (< DN 150) bzw. ≤ 40 m (≥ DN 150, geradlinig); bei Richtungsänderung > 45° (lokal auch > 30°); außen als Schacht mit offenem Gerinne, innen geschlossene Durchführung | kommunale Merkblätter (Weserbergland, „Schächte 2023/01“) | [U] (Wortlaut 6.6 nicht eingesehen) |
| Schachtgrößen nach Einbautiefe | Inspektionsöffnung DN 400 (≤ 1,2 m), DN 600 (≤ 1,6 m); Kontrollschacht DN 800 (≤ 1,8 m), DN 1000 (≤ 2,2 m, PE-HD nach DIN 19537-3); darüber Beton-Einsteigschacht DN 1000; Übergabeschacht „wenn möglich DN 1000“ | Merkblatt Grundstücksentwässerung „Schächte 2023/01“ | [U] (kommunal, nicht DIN) |
| Überflutungsnachweis | erforderlich, wenn A_C (mit C_s) > 800 m²; bei Versickerung Verweis auf DWA-A 138-1 | SBZ 07/2025, DIN Media Änderungsvermerk | [V] |
| Abflussbeiwerte Tab. 9 | seit 2016 getrennt in C_s (Spitze, für Leitungen) und C_m (Mittel, für Speicher/Versickerung). Gründach < 10 cm 0,5, ≥ 10 cm 0,3 in allen Regelwerken gleich; Pflaster DIN 0,7 vs. DWA 0,75 | IZEG, tga-praxis (König) | Struktur [V], Einzelwerte [U] |
| Frosttiefe | DIN 1986-100 5.6: 0,80 m (vom MSE-Leitfaden zitiert) | MSE-Leitfaden 2.7 | [V] |
| Rückstau | Ablaufstellen unter der Rückstauebene sichern. **Abwasserhebeanlage** nach DIN EN 12056-4 mit Rückstauschleife: DIN EN 12050-1 fäkalienhaltig, -2 fäkalienfrei. **Rückstauverschluss** nach DIN EN 13564 nur bei Gefälle zum Kanal, bei Räumen untergeordneter Nutzung, bei kleinem Benutzerkreis und wenn ein WC über der RSE verfügbar ist | MSE-Faltblatt „Lieber heute handeln …“ | [V] |
| Rückstausicherung, Ort | nie im Revisionsschacht vor dem Haus | Stadtentwässerung Düsseldorf | [V] (Düsseldorf, sinngemäß allgemein) |
| Verlegung/Prüfung | DIN EN 1610; Dichtheitsprüfung mit Wasser oder Luft vor dem Verfüllen, in München in Anwesenheit der MSE (EWS § 11 Abs. 3). Optische Inspektion genügt nicht. Wiederkehrend 30 Jahre nach der Erstprüfung, dann alle 20 Jahre (häusliches Abwasser, Regel der Technik nach DIN 1986-30) | MSE „Dichtheitsnachweis“, EWS | [V]; Prüfdrücke EN 1610 [U] |
| Regenwassernutzung | DIN 1989-1 (von E DIN 1986-100 referenziert); in München Zähler bei Grau- und Regenwassernutzung über das Gebührenbüro | DIN Media, MSE-Leitfaden 3.1 | [V]; Bemessung DIN 1989 [U] |
| Baumabstand | geschützte Gehölze ≤ 5 m zur Leitungsachse im Plan darstellen, ggf. Stellungnahme der Unteren Naturschutzbehörde (MSE). Wurzelbereich nach DIN 18920 = Kronentraufe + 1,5 m; Rigole mindestens halber Kronendurchmesser | MSE-Genehmigungsantrag Ziff. 3; Leitfaden Hohenwestedt | MSE [V], DIN 18920 [U] |
| Abstand zu Versorgungsleitungen | im Plan eintragen (MSE); Zahlenwerte (z. B. DVGW W 400-1) nicht geprüft | MSE-Leitfaden 3.2 | [V] / Werte [U] |

### 1.2 Niederschlagswasser Bayern: NWFreiV, TRENGW

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| NWFreiV § 1 | erlaubnisfrei nur außerhalb von Wasserschutz- und Heilquellenschutzgebieten sowie Altlast(verdachts)flächen, nur nicht verändertes und nicht vermischtes Niederschlagswasser | gesetze-bayern.de | [V] |
| NWFreiV § 2 | ausgeschlossen: Flächen mit regelmäßigem Umgang mit wassergefährdenden Stoffen (außer Kleingebinde ≤ 20 l), Straßen mit > 2 Fahrstreifen, planfestgestellte Straßen | dto. | [V] |
| NWFreiV § 3 Abs. 1 | flächenhaft über geeignete Oberbodenschicht; **≤ 1000 m² befestigte Fläche je Anlage** | dto. | [V] |
| NWFreiV § 3 Abs. 2 | Rigolen, Sickerrohre und -schächte **nur, wenn flächenhaft nicht möglich**, und nur **vorgereinigt**; Cu/Zn/Pb-Flächen > 50 m² nur über bauartzugelassene Anlage (Art. 41f BayWG) | dto. | [V] |
| TRENGW Nr. 2 | Nachweis durch pauschale Erhebung in Horizontalprojektion oder die maximal zulässige Befestigung nach B-Plan | gesetze-bayern.de (Bek. 17.12.2008) | [V] |
| TRENGW Tab. 1 (flächenhaft) | Dach/Terrasse/Wege: Oberboden bewachsen ≥ 20 cm, Versickerungsfläche ≥ **1/15** der angeschlossenen Fläche; Metalldächer ≥ 30 cm, pH 6–8; Karst ≥ 30 cm und 1/10 | dto. | [V] |
| TRENGW Nr. 4, Tab. 2 (unterirdisch) | linienförmig (Rigole) vor punktförmig (Schacht). Vorreinigung: Dach → Körbe zum Grobstoffrückhalt; Terrasse → Hof-/Straßenablauf mit Schlammeimer; Wege/Stellplätze → Nassschlamm-Straßenablauf, Absetzbecken ≥ 1/800 bzw. 1/200 oder DIBt-Anlage; Umschlagflächen → nicht erlaubnisfrei | dto. | [V] |
| TRENGW Nr. 5 | Bemessung, Bau, Betrieb nach DWA-A 138 „in der jeweils gültigen Fassung“ → heute A 138-1 | dto. | [V] |
| TRENGW Nr. 6 | stauende Deckschichten nicht durchstoßen; Sohle **≤ 5 m unter GOK**, **≥ 1 m über MHGW** | dto. | [V] |
| Hilfsmittel | kostenloses LfU-Programm „BEN“ (Beurteilung der Erlaubnisfreiheit) | MSE-Leitfaden 5 | [V] |
| Bundesrecht | eine Bundesverordnung nach § 46 i. V. m. § 23 WHG könnte die NWFreiV ablösen; bis dahin gilt die NWFreiV | LfU Bayern | [V] |

### 1.3 DWA-A 138-1 (Oktober 2024), DWA-A/M 102, KOSTRA

| Regel | Kernwert | Quelle | Status |
|---|---|---|---|
| Veröffentlichung | DWA-A 138-1 „Anlagen zur Versickerung von Niederschlagswasser – Teil 1: Planung, Bau, Betrieb“, 10/2024, 98 S., ersetzt A 138 (04/2005). Merkblatt DWA-M 138-2 (Erläuterungen, Beispiele) in Arbeit | DWA-Pressemitteilung 01.10.2024, SBZ 05/2025 | [V] |
| Einfaches Verfahren | nach DWA-A 117, wenn A_E ≤ 200 ha oder t_f ≤ 15 min, T_n ≤ 10 a und q_S ≥ 2 l/(s·ha) | SBZ 07/2025 (Ishorst) | [V, Sekundärquelle] |
| Zufluss | A_C = Σ A_i·C_m,i; Q_zu = r_D(n)·(A_C + A_VA)·10⁻⁴ | dto. | [V, Sekundärquelle] |
| Versickerungsleistung | Q_S = k_i·A_S·10³; **k_i = k·f_k, f_k = f_Ort·f_Methode ≤ 1**. f_Ort 0,3 bis < 1 (Anzahl und Verteilung der Versuche); f_Methode z. B. Open-End-Test 0,8. Bodenansprache allein genügt nicht mehr | SBZ 07/2025, Handbuch Versickerungs-Expert 2025, BauNetz | [V/U] |
| Speichervolumen | V = (Q_zu − Q_S − Q_Dr)·D·60·f_Z·f_A·10⁻³, Maximum über D = 5 … 4320 min; f_Z 1,1–1,2, f_A = 1 | SBZ 07/2025 | [V, Sekundärquelle] |
| Rigole (Kap. 6.4.2) | Sickerfläche Sohle + Seiten + **Stirn** bis zur mittleren Einstauhöhe h/2 → A_S,m = b·L + h·(L + b); Längenformel siehe Abschnitt 3 | nachgerechnete Bemessungen (uvp-verbund Hessen, Waldbrunn, Unterschleißheim) | [V, Nachrechnung] |
| Überflutung | V_Rück = [r_D(30)·(A_E,b,a·C_s + A_VA)·10⁻⁴ − (Q_S + Q_Dr)]·D·60·10⁻³ − V_VA; auch unter 800 m² Folgen bewerten | SBZ 07/2025, ebook-tipp | [V/U] |
| k_f-Bereich | Regelbereich 1·10⁻³ bis 1·10⁻⁶ m/s | SBZ 05/2025 | [V, Sekundärquelle] |
| Sickerraum | Sohle bis MHGW ≥ 1 m; bei geringer Belastung in Absprache mit der Behörde weniger, **nie < 0,5 m** | SBZ 05/2025; MSE-Leitfaden | [V] |
| Abstand zu Gebäuden | ohne wasserdruckhaltende Abdichtung ≥ **1,5 × Baugrubentiefe** ab Baugrubenfußpunkt; ohne Keller die Fundamenttiefe; ≥ 0,5 m zur Böschungsoberkante; mit wasserdruckhaltender Abdichtung unkritisch. Kommunale Pauschalwerte 6 m „ohne Nachweis“ | GGU-Glossar zu A 138-1; bfr-abwasser; Remscheid | [V, Sekundärquelle] / 6 m [U] |
| Abstand zur Grenze | kein fester Wert; Beeinträchtigung Nachbar ausschließen. Kommunal oft ≥ 2 m | SBZ 05/2025; Leitfäden Hohenwestedt, Remscheid | [V] / 2 m [U] |
| Behandlung | Belastungskategorien I/II/III (harmonisiert mit DWA-A 102), Mindestwirkungsgrade; Vorbehandlung vor Versickerung grundsätzlich auch für Dachflächen (Tab. 6/7) | BauNetz, SBZ 05/2025 | [V/U] |
| DWA-A/M 102 | Flächenkategorien I/II/III für Einleitung in Oberflächengewässer; A 138-1 übernimmt die Kategorien | DWA, bau.bi | [V]; Detailwerte [U] |
| Regenhäufigkeit | Dezentrale Rigolen und Mulden mit n = 0,2 (T = 5 a); Überflutung T = 30 a; Grundstücksleitungen r(5,2); Dach r(5,5) (Recherche 09) | Unterschleißheim B 166, Kirchheim B-Plan 104/H, Waldbrunn, Radtke | [V, Sekundärquelle] |
| KOSTRA-DWD-2020 | frei, 5-km-Raster, INDEX_RC = Zeile·1000 + Spalte; München u. a. Rasterfeld **202168** (München/Unterföhring/Ismaning); REST-API openko.de (API-Schlüssel) | DWD-Anwenderhilfe, openko.de | [V] |
| Speicherkoeffizient Füllkörper | 0,93–0,95 in veröffentlichten Bemessungen (Kunststoff-Blockrigolen); Kies 0,35 | Unterschleißheim, Kirchheim, GGU | [V, Sekundärquelle]; Herstellerdatenblätter Rehau/Graf/Wavin/ACO nicht einzeln geprüft [U] |
| Gründach München | begrünte Dächer ≥ 10 cm Aufbau, ≤ 15° gelten zu **30 % als befestigt** (Gebühr) | EAS § 8 Abs. 5 | [V] |
| MSE-Detail Sickerschacht | Absetzschacht + Versickerungsschacht Typ B nach DWA-A 138 (2024): max. Anschlussfläche 400 m², ein Zulauf, Filtersand k_f < 1,8·10⁻⁴ m/s, Abdeckung D 400 | MSE-Detailblatt „Absetzschacht_Versickerungsschacht“ | [V] |

## 2 München (MSE): Anforderungen und Verfahren

### 2.1 Technische Vorgaben

| Anforderung | Kernwert | Fundstelle | Status |
|---|---|---|---|
| Revisionsschacht | „Am Ende der Grundstücksentwässerungsanlage ist auf eigenem Grund ein Revisionsschacht zu errichten“. Revisionsschacht = Übergabeschacht (§ 3 Nr. 9); MSE kann Messschacht verlangen | EWS § 8 Abs. 4 | [V] |
| außenliegend | nur, wenn **≥ 5 m** zwischen Grundstücksgrenze und Gebäudekante frei sind (sonst Reinigungsöffnung im Gebäude) | Leitfaden 2.6 | [V] |
| Anschlusskanal | Teil der Grundstücksentwässerungsanlage und Eigentum der Anlieger (Anliegerregie), auch im öffentlichen Grund; geradlinig, ohne Gefällewechsel, **bis 1:1**; Material- oder DN-Wechsel nur am Kanal oder am Revisionsschacht; im öffentlichen Grund nur der Anschlusskanal | EWS § 9, Leitfaden 2.6, 3.2 | [V] |
| MSE bestimmt | Zahl, Art, Nennweite, Führung, Anschlusspunkt; vorhandene Einlassstücke verwenden; jedes Grundstück gesondert | EWS § 9 Abs. 2 | [V] |
| Anstich | nur durch den Kanalbetrieb der MSE; Absteckung von Kanalachse und Einlassstück mit der MSE | EWS § 9 Abs. 3, Leitfaden 4.5 | [V] |
| Frost | **1,20 m** GOK bis Rohrsohle; NW-Leitungen zur Versickerung 0,80 m | Leitfaden 2.7, EWS § 8 Abs. 3 | [V] |
| Rückstau | Rückstauebene = **Straßenoberkante an der Anschlussstelle**, ggf. höher festgelegt; Eigentümer sichert selbst; MSE haftet nicht | Leitfaden 2.2/2.3, EWS § 8 Abs. 6, § 18 | [V] |
| Hebeanlage | wenn zum Kanal kein ausreichendes Gefälle besteht | EWS § 8 Abs. 5 | [V] |
| Grundleitungen | mehrerer Gebäude (Reihenhäuser) außerhalb zusammenfassen | Leitfaden 2.5 | [V] |
| Schwimmbecken | Schmutzwasser | Leitfaden 2.8 | [V] |
| Einleiten | Schmutz- in Schmutzwasserkanal, Regen- in Regenwasserkanal, beides in Mischkanal | EWS § 14 | [V] |
| Niederschlagswasser | kein Benutzungsrecht, soweit Versickerung möglich; kein Bestandsschutz; Einleitung nur ausnahmsweise nach Vorabstimmung (Selbstauskunft, MSE-421), Ergebnis im Technischen Formblatt; **kein Überlauf** von Versickerungsanlagen zum Kanal | EWS § 4 Abs. 4, Leitfaden 2.4, 5, 5.1, 5.2 | [V] |
| Drosselabfluss | kein allgemeiner Drosselwert veröffentlicht, sondern Einzelfallentscheidung im Technischen Formblatt | Leitfaden 5.1 | [V] (Fehlen belegt) |
| Sonderfälle (WWA) | k_f ≥ 10⁻³ → 1 m Bodenaustausch im Sickerkegel; MHGW-Abstand zu klein → erst Oberbodenversickerung oder flachere Leitungen prüfen, sonst Absetzschacht mit Tauchwand; **< 0,5 m nie zulässig**; Flächen ab F5 → Oberbodenpassage, Retentionsbodenfilter (DWA-A 178) oder DIBt-Filter | Leitfaden 3.2 | [V] |
| Tiefgarage, Treppen | unüberdachte Abfahrten versickern oder rückstaufrei einleiten; kleine Treppenabgänge (≈ 10 m²) und Lichtschächte dürfen an den Kanal | Leitfaden 5.2 | [V] |
| Dichtheit | Luft- oder Wasserprüfung in Anwesenheit einer MSE-beauftragten Person, im offenen Graben, vor Inbetriebnahme | EWS § 11 Abs. 3, Leitfaden 4.4 | [V] |

### 2.2 Genehmigungsweg (Ablauf nach Leitfaden, Abb. 1)

1. **Technisches Formblatt** online beim Erschließungsbüro MSE-421 anfordern (mit Auszug Stadtgrundkarte 1:1000). Es enthält Anschlussmöglichkeit, Einlassstück mit Kanalkataster-Auszug (Höhen noch **DHHN12**, 2–5 cm über DHHN2016), Altlastverdacht, Wasserschutzgebiet und die Vorgabe zum Niederschlagswasser. Bei gewünschter Einleitung geht zuerst die *Selbstauskunft Niederschlagswasser* an MSE-421 [V].
2. **Entwässerungsantrag** je wirtschaftlicher Einheit (EFH oder DHH) bei der Planannahme MSE-422 einreichen [V]:
   - Genehmigungsantrag (1-fach) mit „Erklärung zur Niederschlagswasserversickerung“ (Checkliste NWFreiV),
   - Technisches Formblatt,
   - Pläne **3-fach**: Lageplan 1:1000, Grundriss 1:100, Abwicklungen 1:100,
   - ggf. Bemessung nach DWA-M 153 und A 138, Abscheider, Stellungnahmen RKU.

   Baukosten über 60 000 EUR sind anzugeben.
3. **Planinhalte** [V]:
   - Darstellung: Sinnbilder nach DIN 1986-100 Tab. 1, Ein-Strich-Darstellung mit DN und Werkstoff, Schächte und Verzweigungen nummeriert, Schrift ≥ 2,5 mm, **nicht rot**, auf A4 gefaltet.
   - Lageplan: Nordpfeil, Straßennamen, Fl.-Nr., städtischer Kanal mit Maßen, Gefälle und Fließrichtung.
   - Grundriss: Geschosse und Ablaufstellen unter der RSE, geschützte Bäume, Sparten im Bereich der SW-Leitungen, Grau- und Regenwassernutzung.
   - Abwicklung: wahre Länge (kein Strangschema), GOK, RSE auf jedem Plan, NHN-Höhen, HW 1940, Frosttiefe 1,20 m, Gefälle, Belastungswerte je Geschoss.
   - Versickerung: vollständig im Grundriss, Schnitt durch die Anlage, MHGW (Mittel der Jahreshöchststände, ≥ 10 Jahre, beim RKU kostenpflichtig) und k_f.
4. **Prüfung und Genehmigung**: Die Genehmigung **gilt als erteilt**, wenn die MSE sie nicht binnen 3 Monaten nach Vollständigkeit verweigert. Baubeginn erst danach (EWS § 10 Abs. 3–4). Die wasserrechtliche Erlaubnis zur Versickerung erteilt die MSE, im Wasserschutzgebiet Trudering das RKU [V].
5. **Arbeitsbeginnanzeige** ≥ 24 h vorher (§ 11 Abs. 1, online nach Firmenregistrierung). Aufgrabung im öffentlichen Grund: Sondernutzung und verkehrsrechtliche Anordnung beim Mobilitätsreferat, Anmeldung ≥ 5 Arbeitstage vorher, **20 EUR je Hausanschluss** [V].
6. **Bauüberwachung** MSE-423 mit Dichtheitsprotokoll, danach **Gebührenbescheid** [V].

Genehmigungspflichtig sind Anlagen **unterhalb der Rückstauebene, erdverlegt oder in der Bodenplatte**. Genehmigungsfrei sind z. B. das Abtrennen von Niederschlagswasser, zusätzliche Schächte und der Austausch genehmigter Anlagen (Leitfaden 2.1) [V]. Für das Fertighaus auf Bodenplatte ist damit **jede Grundleitung unter der Platte genehmigungspflichtig**.

### 2.3 Gebühren (EAS München)

| Gebühr | Wert | Fundstelle | Status |
|---|---|---|---|
| Schmutzwasser | **2,02 EUR/m³** Frischwasser (Zwischenzähler für Gartenwasser) | EAS § 9 a, MSE | [V] |
| Niederschlagswasser | **1,77 EUR/m² und Jahr** auf die reduzierte Fläche = Grundstücksfläche × Gebietsabflussbeiwert (0,35 Einzelhaus, 0,5, 0,6, 0,9; Karte 2000) | EAS § 8 Abs. 2–3, § 9 b | [V] |
| Widerlegung | wenn die tatsächliche Ableitungsfläche ≥ 25 % oder ≥ 400 m² kleiner ist; Gründach (≥ 10 cm, ≤ 15°) zu 30 % | EAS § 8 Abs. 5 | [V] |
| Kalkulationszeitraum | 01.01.2023 bis 31.12.2026; ab 2027 neue Sätze möglich | MSE-Infoschreiben 2023 | [V] |
| Beispiel 600 m², GAB 0,35 | 210 m² × 1,77 = **371,70 EUR/a**, bei Vollversickerung 0 EUR (Antrag) | eigene Rechnung | [V] |

## 3 Bemessungsformeln (im Prototyp umgesetzt)

**Schmutzwasser (Anschluss an Recherche 08):**
- Q_ww = K·√ΣDU mit K = 0,5, mindestens der größte Einzel-DU.
- Vollfüllung nach Prandtl-Colebrook: v = −2·lg(2,51ν/(d·√(2gdJ)) + k_b/(3,71d))·√(2gdJ), mit k_b = 1 mm [U] und ν = 1,31·10⁻⁶ m²/s.
- Teilfüllung über den Ansatz Q ~ A·R^(2/3): Q/Q_v = 0,500 bei h/d = 0,5 (exakt) und 0,837 bei h/d = 0,7 (Näherung) [U].

**Regenwasser in Leitungen:** Q = r·C_s·A/10 000 mit r(5,2) für Grundstücksleitungen (Recherche 09).

**Rigole nach DWA-A 138-1, einfaches Verfahren** (Formeln aus Fachartikeln und veröffentlichten Rechenblättern, [V] durch Nachrechnung):

```
k_i   = k_f · min(1, f_Ort · f_Methode)
A_C   = Σ A_E,i · C_m,i
A_S,m = b·L + h·(L + b)                                    (mittlere Sickerfläche)
Q_S   = k_i · A_S,m · 10³                                   [l/s]
L(D)  = [A_C·10⁻⁷·r_D(n) − b·h·k_i − Q_Dr·10⁻³ − V_Sch/(D·60·f_Z)]
        / [b·h·s_R/(D·60·f_Z) + (b + h)·k_i]
L_erf = max_D L(D)          (D = 5 … 4320 min, T = 5 a)
V_erf = max_D (r_D·A_C·10⁻⁴ − Q_S)·D·60·f_Z·10⁻³ ≤ V_vorh = s_R·b·h·L
t_E   = V_erf / Q_S
```

**Mulde (Vergleichsrechnung für NWFreiV § 3 Abs. 2):**

```
V(A_S)  = max_D (r_D·(A_C + A_S)·10⁻⁴ − k_i·A_S·10³)·D·60·f_Z·10⁻³
Bedingungen: V/A_S ≤ 0,30 m [U]  und  A_S ≥ A_E/15 (TRENGW)
```

**Nachrechnung (tests/test_b17.py):**
- Rigole „Wendeanlage Ludwigshöhstraße“: A_C 820 m², k_i 1,04·10⁻⁶, 8,0 × 0,66 × 8,80 m. Ergebnis A_S,m = 81,49 m², Q_S = 0,085 l/s, V_erf = **40,52 m³** bei D = 1440 min, V_vorh = 44,14 m³, Entleerung 133 h. Das stimmt mit der veröffentlichten Rechnung überein [V].
- Rigole B 166 Unterschleißheim: A_C 864 m², k_i = 5·10⁻⁶ · 0,75, 4,0 × 0,35 m, s_R 0,93. Ergebnis L = **27,45 m** bei D = 360 min, wie veröffentlicht [V].
- Waldbrunn: A_C 5592 m², 7,2 × 1,32 m. Die Nachrechnung ergibt 17,36 m statt 17,39 m; die Abweichung erklärt die Rundung von k_f in der Quelle [U].

## 4 Routing auf dem Grundstück

### 4.1 Verfahren im Prototyp (deterministisch)

1. **Geometrie.** Grundstück, Gebäude, Gelände als Ebene z(x, y) oder DGM1, geschützte Bäume, Sparten (Hausanschlüsse) und befestigte Flächen. Das DGM1 Bayern (1-m-Raster) ist **kostenfrei unter CC BY 4.0** (Gebühren- und Preisliste LDBV, Stand 01.07.2026) [V].
2. **Zuerst die Versickerungsanlage platzieren.** Zulässige Fläche = Grundstück minus 2 m Grenzabstand, minus Gebäude + 1,5·t, minus Baumkronen, minus befestigte Flächen + 0,5 m, minus Sparten + 1 m. Achsparallele Rechtecke auf einem 0,5-m-Raster, zwei Orientierungen. Ziel: kleinster Abstand zum Schwerpunkt der Zuläufe. Passt eine Reihe nicht, wird die Rigole breiter (2, 3 Reihen).
3. **Sichtbarkeitsgraph.** Knoten sind Quellen, Ziel, Ecken der Hindernisse (um 1,05 m versetzt), Achtecke um Wurzelbereiche und Austrittspunkte senkrecht zu den Außenwänden. Eine Kante ist zulässig, wenn sie innerhalb des Grundstücks (0,5 m Rand) liegt und kein hartes Hindernis schneidet (Wurzelbereich, Rigole + 1 m).

   Kosten = Länge + (f − 1)·Länge in Zonen + Strafe je Sparten-Kreuzung (5 m) + Strafe je Formstück (0,5 m):
   - im Gebäude f = 3 (DIN 1986-100 6.1.1), mit Keller 1,5,
   - im Fundamentstreifen 0–1 m f = 2,
   - bei NW-Leitungen 1,2 für den Fundamentstreifen und 2 im 0,5-m-Streifen um die SW-Leitungen.

   Alle Kostenwerte sind eigene Annahmen.
4. **Steiner-Heuristik (Takahashi-Matsuyama).** Die fernste Quelle wird zuerst zum Ziel geführt (Revisionsschacht an der Grenze in der Flucht des Einlassstücks bzw. Filterschacht vor der Rigole). Jede weitere Quelle wird per Dijkstra an den nächsten Punkt des bestehenden Baums angeschlossen (Knoten + Abtastpunkte alle 0,5 m). Der bestehende Baum ist für neue Kanten ein Hindernis (0,02-m-Puffer). So entstehen keine Kreuzungen und keine Doppelführungen im eigenen Netz.
5. **Topologie.**
   - Wanddurchführungen an den Schnitten mit der Außenwand einfügen, gerade Zwischenknoten entfernen.
   - Last aufsummieren (ΣDU bzw. Q), Nennweite wählen, in Fließrichtung nicht verringern.
6. **Höhenplan.**
   - Vorwärts: Sohle(v) = min(Sohle(u) − L·s_min, GOK(v) − Frosttiefe) für Knoten außerhalb des Gebäudes.
   - Rückwärts: Liegt das Gefälle über 5 %, wird der oberstromige Knoten tiefer gelegt.
   - Wiederholen bis stabil. Das Ergebnis ist die Mindesttiefe unter allen Randbedingungen.
7. **Schächte.**
   - Revisionsschacht am Ziel (mindestens DN 1000); Schacht bei Zusammenführung oder Richtungsänderung > 45° außerhalb des Gebäudes.
   - Im Gebäude Reinigungsöffnung, am Fallleitungsfuß Reinigungsrohr.
   - Zusatzschacht bei Überschreitung von 20/40 m; Größe aus der Einbautiefe.
8. **Anschlusskanal.** Gerade vom Revisionsschacht zum Einlassstück. Liegt das Gefälle unter 1/DN, ist Freispiegel nicht möglich, und das Werkzeug fordert eine Hebeanlage (EWS § 8 Abs. 5).

### 4.2 Literatur zur automatischen Kanalnetzplanung

| Arbeit | Methode | DOI | Status |
|---|---|---|---|
| Duque, Duque, Aguilar, Saldarriaga (2020), *Water* 12(12) 3337: Sewer Network Layout Selection and Hydraulic Design Using a Mathematical Optimization Framework | MILP-Layout (Baum) + kürzeste Wege für DN/Sohlhöhen, iteriert | 10.3390/w12123337 | [V] DOI, Autoren [U] |
| (2021), *Water* 13(18) 2491: Layout Selection … Based on Land Topography, Streets Network Topology, and Inflows | Layout aus Topografie und Straßennetz | 10.3390/w13182491 | [V] |
| Navin, Mathur (2016), *Water Resources Management* 30(10) | Spannbäume + modifizierte PSO | 10.1007/s11269-016-1378-7 | [V] |
| Steele, Mahoney, Karovic, Mays (2016), *WRM* 30(5) 1605–1620 | MINLP (GAMS) + Simulated Annealing | 10.1007/s11269-015-1191-8 | [V] |
| Alfaisal, Mays (2021), *WRM* 35(14) | 0-1-INLP für Layout und Rohrbemessung Regenwasser | 10.1007/s11269-021-02958-5 | [V] |
| (2019), Wiley/Hindawi: Feasible Sanitary Sewer Network Generation Using Graph Theory | zulässige Layouts graphentheoretisch | 10.1155/2019/8527180 | [V] DOI, Zeitschrift [U] |
| (2006), *J. Hydraulic Engineering* 132(9) 927: Optimal Layout of Sewer Systems: A Deterministic versus a Stochastic Model | mehrstufige dynamische Programmierung | 10.1061/(ASCE)0733-9429(2006)132:9(927) | [V] |
| (2024), *Eng. Proc.* 69(1) 143: Automated Pump Placement Algorithms for Optimal Sewer Network Design in Areas with Complex Terrain | Graph + Metaheuristik, Hebeanlagen im Netz | 10.3390/engproc2024069143 | [V] |
| Duque et al. (2016), *J. Hydroinformatics* 18(5) 757: series of pipes | Hydraulik einer Rohrreihe als kürzester Weg | nicht aufgelöst | [U] |
| Takahashi, Matsuyama (1980), *Math. Japonica* 24: Steiner problem in graphs | Steiner-Heuristik „nächster Anschluss“ | keine DOI | [U] |
| Zhang, Tian, Wang, Al-Hussein (2020), CRC | BIM-Entwässerung in der Vorfertigung (aus Recherche 08) | 10.1061/9780784482865.121 | [V] |

**Bewertung [U]:** Die Literatur optimiert öffentliche Netze mit Hunderten Haltungen nach Baukosten. Beim Einzelgrundstück dominieren harte Satzungsregeln (Revisionsschacht an der Grenze, Frosttiefe, RSE, Anschlusskanal gerade), und die Suchmenge ist winzig. Ein deterministisches Verfahren mit expliziter Regelprüfung ist dort besser erklärbar als eine Metaheuristik. Eine Arbeit, die **Grundstücksentwässerung automatisch aus einem Fertighaus-Grundriss nach kommunaler Satzung** plant, habe ich nicht gefunden. Das ist eine Forschungslücke.

## 5 Hydraulik-Werkzeuge: was ist frei nutzbar?

| Werkzeug | Lizenz | Nutzen | Urteil |
|---|---|---|---|
| EPA SWMM 5 | **Public Domain** (US-Bundeswerk; Quellcode C, GitHub USEPA) | Langzeit- und Ereignissimulation, Nachweisverfahren nach A 117, Überflutung | **übernehmen** (Nachweisverfahren, Starkregen) [V] |
| pyswmm 2.1.0 | BSD-2 | Python-Steuerung von SWMM | **übernehmen** [V, PyPI] |
| swmm-toolkit 0.17.0 | CC0-1.0 AND (MIT OR Apache-2.0) | SWMM-Bibliothek für Python | **übernehmen** [V, PyPI] |
| swmmio 0.8.6 | MIT | .inp lesen/schreiben, Visualisierung | **übernehmen** (Export des Netzes) [V, PyPI] |
| „urbs“ | – | nach meiner Kenntnis ein Energiesystem-Optimierungsmodell der TU München, **kein** Entwässerungswerkzeug | verwerfen [U] |
| DWA Versickerungs-Expert 6.0 | kommerziell | A-138-1-konforme Bemessung mit Behördenausgabe | Referenz für Validierung [V] |
| DWA-Datentool KOSTRA, itwh KOSTRA-DWD 2020 | kommerziell | Regenreihen aufbereitet | nicht nötig, DWD-Rohdaten frei [V] |
| KOSTRA-DWD-2020 (DWD) | frei (GeoNutzV) | Regenspenden je Rasterfeld | **übernehmen** (Recherche 09) [V] |
| DGM1 Bayern | CC BY 4.0, kostenfrei | Gelände für Tiefen und Gefälle | **übernehmen** [V] |
| DWA-A 138-1, DIN 1986-100 | kostenpflichtig (Normtext) | Tabellen C_m, f_Ort, f_Methode, Schachtmaße | **Lizenz beschaffen**, Werte als Datendatei mit Quelle [V] |
| B17 (dieser Prototyp) | Projektcode | Routing, Höhenplan, Rigole, Prüfung, SVG, IFC | **selbst gebaut** |

## 6 IFC-4.3-Abbildung (maschinell gegen IFC4X3_ADD2 geprüft)

| Bauteil | Entität / PredefinedType [V] | Merkmale [V] | Bemerkung |
|---|---|---|---|
| Systeme | `IfcDistributionSystem` **SEWAGE** (SW), **RAINWATER** (Niederschlag direkt auf die Parzelle), **STORMWATER** (Oberflächenabfluss), außerdem WASTEWATER, DRAINAGE | – | Dach = RAINWATER, Hof/Stellplatz = STORMWATER; Mischkanal nur als Randbedingung |
| Grund- und Anschlussleitung | `IfcPipeSegment` **RIGIDSEGMENT** | `Pset_PipeSegmentTypeCommon` (NominalDiameter, InnerDiameter, Length); **`Pset_PipeSegmentOccurrence` (Gradient: IfcPositiveRatioMeasure, InvertElevation: IfcLengthMeasure)** | Gefälle und Sohle sind Standardmerkmale; `CULVERT` ist ein Durchlass unter Straßen, nicht die Grundleitung |
| Formteile | `IfcPipeFitting` BEND, JUNCTION, CONNECTOR, TRANSITION | – | Abzweig im Gebäude = JUNCTION |
| Revisionsschacht, Einsteigschacht | `IfcDistributionChamberElement` **MANHOLE** | `Pset_DistributionChamberElementTypeManhole` (InvertLevel, IsShallow, HasSteps, AccessCoverLoadRating, …) | „permits the entry of a person“ |
| Kontrollschacht, Inspektionsöffnung | `IfcDistributionChamberElement` **INSPECTIONCHAMBER** | `…TypeInspectionChamber` (InspectionChamberInvertLevel, ChamberLengthOrRadius) | „permits visible inspection“ |
| Pumpenschacht/Hebeanlage | `IfcDistributionChamberElement` SUMP + `IfcPump` SUMPPUMP/SUBMERSIBLEPUMP; Rückstauverschluss `IfcValve` CHECK | – | Rückstauschleife als Leitung über RSE |
| Abscheider, Filterschacht | `IfcInterceptor` GREASE/OIL/PETROL; Sediment- oder Filterschacht **USERDEFINED** | `Pset_InterceptorTypeCommon` | Alternative `IfcFilter` WATERFILTER (Einsatz) |
| Zisterne | `IfcTank` **STORAGE** | `Pset_TankTypeCommon.StorageType` = **RAINWATER**, AccessType MANHOLE | Retentionszisterne: eigenes Pset für Drossel und Nutzvolumen |
| Rigole, Sickerschacht | **keine Klasse**: `IfcDistributionChamberElement` **USERDEFINED**, ObjectType „Versickerungsrigole“ (Prototyp); Alternative TRENCH („excavated chamber, length exceeds width“) | eigenes Pset `B17_Versickerung` (k_f, k_i, s_R, V_erf, V_vorh, MHGW, Sickerraum) | eigene Psets nicht mit „Pset_“ benennen |
| Mulde | `IfcGeographicElement` USERDEFINED („Versickerungsmulde“) oder Aushub `IfcEarthworksCut` | – | [U] Wahl offen |
| Gelände | `IfcGeographicElement` **TERRAIN** mit `IfcTriangulatedFaceSet` | – | DGM1 → Dreiecksnetz |
| Grundwasser | `IfcGeotechnicalStratum` **WATER** (Enum SOLID/VOID/WATER) | `Pset_GeotechnicalStratumCommon` | MHGW als Oberfläche; Bohrung `IfcBorehole` |
| Ports | `IfcDistributionPort` PIPE, FlowDirection SINK/SOURCE, SystemType; `IfcRelNests`, `IfcRelConnectsPorts` | – | wie Recherche 08; `util.system.get_connected_to` findet die Kette |

**Prüfprotokoll:** `b17_grundstuecksentwaesserung.py --ifc` erzeugt je Szenario eine Datei. Szenario *bodenplatte* enthält:
- 19 `IfcPipeSegment`, 9 `IfcDistributionChamberElement` (Schächte + Rigole), 1 `IfcInterceptor`, 2 `IfcPipeFitting`,
- 65 Ports, 29 `IfcRelConnectsPorts`, 2 Systeme, 1 TERRAIN.

`ifcopenshell.validate(..., express_rules=True)` meldet **0 Fehler**. SHA-256 `d548ea4835c2…` in zwei Prozessen gleich. `get_connected_to(SW-RS)` liefert den Anschlusskanal [V].

## 7 Prototyp B17: Ergebnisse

Dateien:
- `arbeit/beispiele/b17_grundstuecksentwaesserung.py`
- `arbeit/beispiele/tests/test_b17.py`
- `arbeit/beispiele/daten/b17_grundstuecksentwaesserung.json`

Ausgaben unter `arbeit/beispiele/ausgabe/b17_*` (JSON, Lageplan-SVG, Abwicklungs-SVG, Bericht MD, IFC).

**Eingabe (alles Beispielwerte):**
- Grundstück 20 × 30 m wie `grundstueck.json`. Das vorhandene `grundstueck.json` ist eben und ohne Kanal, deshalb gibt es eine eigene Datei.
- Gelände z = 520,00 − 0,005x + 0,02y (2 % zur Straße im Süden). Mischwasserkanal DN 600 in der Straßenachse, Einlassstück-Sohle 516,80, RSE 519,95.
- EFH 10 × 12 m (FFB 520,55) mit zwei Fallleitungen: FL1 ΣDU 6,4, FL2 ΣDU 2,9.
- Geschützter Baum, Hausanschlusstrasse, Terrasse 24 m², Rasengitter-Zufahrt.
- Dach 143 m² (C_m 0,8), Terrasse (C_m 0,7) → A_E,b = 167 m², **A_C = 131,2 m²**.
- k_f = 1·10⁻⁵ m/s, f_Ort·f_Methode = 0,9·0,8 → **k_i = 7,2·10⁻⁶ m/s**.
- Regenreihe KOSTRA-DWD-2020, T = 5 a, aus dem Entwässerungskonzept Unterschleißheim (Sekundärquelle, **nicht** das Münchner Rasterfeld). Blockrigole 0,8 × 0,66 m, s_R 0,95, f_Z 1,2.

**Ergebnisse (Szenario *bodenplatte*):**

| Größe | Wert |
|---|---|
| Rigole | L_erf = **9,29 m** (D = 240 min, r = 28,3 l/(s·ha)) → gewählt **9,60 m = 12 Elemente**, 0,80 × 0,66 m; A_S,m = 14,54 m²; Q_S = 0,105 l/s; V_erf = **4,61 m³** ≤ V_vorh = **4,82 m³** (brutto 5,07 m³); Entleerung 12,2 h |
| Lage und Höhen | Weststreifen x 3,0–3,8 / y 12,0–21,6; Abstand zum Gebäude **1,20 m = 1,5 × 0,80 m** Fundamenttiefe; OK 519,01, Sohle 518,35, Überdeckung 1,31 m, **Sickerraum 3,35 m** (MHGW 515,00) |
| Vergleich Mulde | hydraulisch A_S ≥ 17,1 m² (TRENGW-Minimum 11,1 m²) → **passt auf das Grundstück** → Befund NW-05 „Rigole begründen oder Mulde wählen“ |
| SW-Netz | 7 Haltungen + Anschlusskanal, gesamt **38,24 m**, davon 5,27 m unter der Bodenplatte. FL2 verlässt das Haus nach Osten, weil der Weststreifen durch die Rigole belegt ist, und kreuzt die Hausanschlusstrasse einmal (Hinweis SW-12) |
| Tiefen | Fallleitungsfüße 519,10/519,20 (1,45/1,35 m unter FFB), weil die Wanddurchführung schon 1,20 m frostfrei liegen muss. Innen 5 % (Höchstgefälle), außen 0,67–2,03 % |
| Schächte | 3 Inspektionsöffnungen DN 600 (Richtungsänderungen 90°/49°, Zusammenführung), **Revisionsschacht DN 1000** bei (8,0; 1,0), Sohle 518,78, Tiefe 1,20 m |
| Anschlusskanal | DN 150, L = 4,60 m, **Gefälle 43 %** (zulässig 0,67–100 %) |
| Hydraulik | Q_ww 2,0 l/s (WC maßgebend), maximale Auslastung 0,23 |
| NW-Netz | 11 Haltungen DN 100, 43,95 m, 4 Inspektionsöffnungen, Filterschacht DN 600 vor der Rigole, Q bis 3,74 l/s (r(5,2) = 290 l/(s·ha)) |
| Regelprüfung | 28 Prüfpunkte: **0 Verstöße**, 4 Hinweise (Sparten-Kreuzung, Grundleitung unter der Bodenplatte, NWFreiV § 3 Abs. 2, Vorreinigung nach A 138-1) |
| Gebühr | NW-Pauschale 371,70 EUR/a entfällt bei Vollversickerung |

**Szenarien im Vergleich:**

| Szenario | Befund | Zahlen |
|---|---|---|
| *keller* (UG-FFB 517,75 < RSE) | **Auflage SW-10**: Hebeanlage DIN EN 12050-2 (fäkalienfrei) mit Rückstauschleife. Ein Rückstauverschluss wäre nur unter MSE-Bedingungen denkbar (Gefälle vorhanden) | Rigole muss ≥ 0,6 + 1,5 × 2,90 = **4,95 m** vom Haus entfernt liegen → Nordgarten (5,00 m); Mulde passt nicht mehr, also ist die Rigole begründet. SW-Netz nur 26,8 m, weil die Sammelleitung im Keller zugänglich ist (Kostenfaktor 1,5), 1 Revisionsschacht |
| *kanal_hoch* (Einlass-Sohle 518,90) | **Verstoß SW-06**: Anschlusskanal −2,6 % → Freispiegel unmöglich, **Hebeanlage für das Gebäude** (EWS § 8 Abs. 5) | Revisionsschacht-Sohle 518,78 bei Frosttiefe 1,20 m |
| *grundwasser_hoch* (MHGW 518,40) | **Verstoß NW-02**: Sickerraum −0,05 m < 0,5 m → unzulässig; Mulde/Flächenversickerung prüfen | Rigolensohle 518,35 |

**Tests:** `python -m pytest tests/test_b17.py` → **20 passed** (5,8 s). Sie decken ab:
- Nachrechnung von zwei veröffentlichten A-138-1-Bemessungen, Konsistenz von Längenformel und Speicherbedingung,
- Mulden-Bisektion, Hydraulik,
- alle vier Szenarien, NWFreiV-1000-m²-Grenze,
- harte Hindernisse, keine Selbstkreuzung, Gebühr,
- JSON/SVG deterministisch, IFC valide und byte-identisch.

Die übrige Beispielsuite (ohne `test_b2_b3`, dem im System-Python `ifctester` fehlt) läuft weiter grün (136 passed, 1 skipped).

**Grenzen des Prototyps [U]:**
- Gelände als Ebene (DGM1-Anbindung fehlt); nur eine Sohlhöhe je Knoten (sohlgleich, keine Scheitelgleichheit, kein Absturz im Schacht).
- SW wird vor NW geroutet, NW weicht nur aus. Im Bodenplatten-Fall läuft die NW-Leitung RF3 an der Ostseite eng parallel zur SW-Leitung.
- Hausanschlussleitungen (Wasser, Strom) werden nicht mitgeplant; passt die Rigole nicht, bricht die Rechnung ab.
- Schachtmaße stammen aus einem kommunalen Merkblatt, nicht aus DIN 1986-100 Tab. 3. Abflussbeiwerte C_s/C_m sind Beispielwerte.
- UG-Ablaufstellen werden nur geprüft, nicht geroutet.

## Warnungen

1. **Die MSE verlangt 1,20 m Frosttiefe bis zur Rohrsohle**, nicht 0,80 m (DIN 1986-100 5.6 gilt in München nur für NW-Leitungen zur Versickerung). Das drückt beim Haus auf Bodenplatte die Fallleitungsfüße auf ca. 1,4 m unter FFB [V].
2. **„Kontrollschacht“ heißt in München „Revisionsschacht“ (= Übergabeschacht).** Er liegt auf eigenem Grund, außen nur bei ≥ 5 m Vorgarten [V].
3. **Der Anschlusskanal gehört dem Eigentümer, auch im öffentlichen Grund.** Herstellung in Anliegerregie, Anstich nur durch die MSE, Sondernutzung und 20 EUR je Hausanschluss [V].
4. **Niederschlagswasser hat kein Einleitungsrecht, und ein Notüberlauf zum Kanal ist unzulässig** (Leitfaden 5.2). Die Versickerungsanlage muss daher auch Überlast schadlos auf dem Grundstück halten [V].
5. **NWFreiV § 3 Abs. 2:** Rigole und Sickerschacht sind nur zulässig, wenn flächenhafte Versickerung nicht möglich ist. Die Begründung gehört in den Antrag [V].
6. **DWA-A 138-1 verlangt jetzt auch für Dachflächen eine Behandlung** vor unterirdischer Versickerung. Einfache Siebfilter reichen nach Fachkommentaren nicht mehr [V BauNetz / U Umfang].
7. **Die MSE fordert (Leitfaden 06/2026) weiterhin eine Bewertung nach DWA-M 153.** Die DWA hat die Qualitätsbewertung inzwischen nach A/M 102 und A 138-1 verlagert. Der Generator sollte beides ausgeben, bis die MSE umstellt [V Forderung / U Ablösung von M 153].
8. **Rot ist auf Münchner Entwässerungsplänen verboten.** Die SVG-Ausgabe verwendet deshalb Braun, Blau und Violett [V].
9. **Höhensystem:** Das Kanalkataster rechnet noch in DHHN12, das sind 2–5 cm über DHHN2016. Pläne müssen DHHN2016 zeigen [V].
10. **Die Regenreihe im Beispiel stammt nicht aus München-Stadt** (Unterschleißheim, Sekundärquelle). Für echte Planung das eigene KOSTRA-Rasterfeld verwenden, z. B. 202168 [V].
11. **Rückstausicherung:** Hebeanlage ist in München der empfohlene Standard. Ein Rückstauverschluss kommt nur unter den EN-12056-4-Bedingungen in Frage, nie im Revisionsschacht [V].
12. **Genehmigungsfiktion:** Die Genehmigung gilt nach 3 Monaten als erteilt. Das ersetzt keine Baugenehmigung und keine wasserrechtliche Erlaubnis (EWS § 10 Abs. 4) [V].
13. **Die Gebührensätze gelten bis 31.12.2026.** Die Wirtschaftlichkeitsrechnung (Vollversickerung spart 371,70 EUR/a) ist ab 2027 zu aktualisieren [V].
14. **Tabellenwerte (DIN 1986-100 Tab. 3 und 9, DWA-A 138-1 Tab. 9–11) nicht aus dem Normtext übernommen.** Vor produktiver Nutzung Lizenz beschaffen und die Datendatei gegen den Normtext prüfen [U].
15. **Die Dateien von B17 sind bereits in den Commits „Zwischenstand B17“ und „Zwischenstand laufender Recherchen …“ enthalten.** Die Commits kamen nicht aus dieser Bearbeitung. Der jetzige Stand der Arbeitskopie ist nicht committet.

## Offene Fragen an Regnauer

1. **Gründung:** Welcher Anteil der Häuser in Bayern/München steht auf Bodenplatte, welcher auf Keller? Wer liefert Bodenplatte bzw. Keller (Regnauer oder Partner), und wer verlegt die Grundleitungen darunter?
2. **Übergabepunkte:** Wo und auf welcher Höhe übergibt das Werk die Fallleitungen (Stutzen über oder unter OK Bodenplatte, festes Raster, Vorwand)? Gibt es Standardlagen für Bad, Küche und HWR, die sich als Quellen parametrieren lassen?
3. **Entwässerungsantrag:** Wer erstellt Lageplan, Grundriss und Abwicklung für die MSE: Regnauer, der Bauherr oder ein Fachplaner vor Ort? In welchem CAD, und würde ein generierter Planentwurf mit Regelprüfung helfen?
4. **Dachentwässerung:** Standardanzahl und -lage der Fallrohre, Standrohre mit Reinigungsöffnung, Laubfang?
5. **Versickerung:** Bietet Regnauer Rigole, Mulde oder Zisterne an, und welches System (Rehau, Graf, Wavin, ACO)? Wer beauftragt Sickertest und Bodengutachten, und wer beschafft den MHGW beim RKU?
6. **Regenwassernutzung und Retention:** Gibt es eine Zisterne (DIN 1989) im Angebot, eventuell mit Retentionsvolumen und Drossel?
7. **Gründach/Carport:** Werden begrünte Flachdächer (≥ 10 cm, ≤ 15°) angeboten? In München zählen sie für die Gebühr nur zu 30 %.
8. **Keller unter der Rückstauebene:** Standard-Hebeanlage (Hersteller, fäkalienfrei/-haltig), Lage und Rückstauschleife? Wird bewusst auf Ablaufstellen im Keller verzichtet?
9. **Fundamenttiefe/Frostschürze:** Welche Gründungstiefe gilt bei Bodenplatten? Sie bestimmt den Mindestabstand der Versickerung (1,5 × Tiefe).
10. **Sparten:** Wo liegt die Mehrsparten-Hauseinführung, und gibt es Mindestabstände des Netzbetreibers zu Abwasserleitungen?
11. **Leistungsgrenze:** Gehören Außenanlagen und Grundstücksentwässerung zum Regnauer-Leistungsumfang oder zum Bauherrn/GaLaBau? Davon hängt ab, ob der Generator sie planen oder nur prüfen soll.
12. **IFC-Austausch:** Braucht der Tiefbauer oder Fachplaner die Leitungen als IFC (IfcPipeSegment mit Sohlhöhen), oder reicht PDF/DWG?

---

*Quellen (Auswahl, alle am 27.09.2026 abgerufen):*
- **Landeshauptstadt München:** Entwässerungssatzung EWS (Stadtrecht 210, Fassung 08.05.2024); Entwässerungsabgabensatzung EAS (Stadtrecht 211); MSE „Leitfaden Grundstücksentwässerung – Planung und Bau in München“, 7. Aufl., Stand 08.06.2026; Genehmigungsantrag (Vordruck 2023); Datenerfassungsblatt Technisches Formblatt; MSE-Seiten Grundstücksentwässerung, Dichtheitsnachweis, Schutz gegen Rückstau, Entwässerungsgebühren, FAQ Niederschlagswassergebühr; Faltblatt „Lieber heute handeln als morgen pumpen!“; Detailblatt Absetzschacht/Versickerungsschacht; Infoschreiben Gebührenanpassung 2023.
- **Bayern:** gesetze-bayern.de (NWFreiV, TRENGW Bek. 17.12.2008); LfU Bayern (erlaubnisfreie Versickerung); LDBV Gebühren- und Preisliste Stand 01.07.2026 und OpenData DGM1.
- **DWA und Fachpresse:** DWA-Pressemitteilung A 138-1 (01.10.2024); DWA Versickerungs-Expert (Handbuch 2025); SBZ 05/2025 und 07/2025 (Ishorst, Teil 1/2); BauNetz Wissen (A 138-1; Abwasserleitungen); IZEG Tech-Info DIN 1986-100; tga-praxis (König) Abflussbeiwerte; Haustec (Ishorst 2020); GGU-Glossar A 138-1; ebook-tipp „Erfahrungen DWA-A 138-1“.
- **Normen:** DIN/DIN Media (DIN 1986-100:2016-12, E DIN 1986-100:2025-06, Inhaltsverzeichnisse); baunormenlexikon.
- **Kommunale Merkblätter:** Weserbergland, Hohenwestedt, Remscheid, Düsseldorf, Merkblatt Schächte 2023/01.
- **Veröffentlichte Bemessungen:** Radtke (uvp-verbund, Hessen), Waldbrunn (rö ingenieure), Unterschleißheim B 166, Kirchheim-Heimstetten B-Plan 104/H, München BP 2164.
- **Daten und Software:** DWD KOSTRA-Anwenderhilfe und Mustertabelle, openko.de (Rasterfeld 202168, REST-API); US EPA SWMM (epa.gov, GitHub USEPA); PyPI (pyswmm, swmm-toolkit, swmmio, networkx).
- **Verlagsseiten der Literatur:** MDPI, Springer/RePEc, ASCE, Wiley, IWA.

# Recherche 20: Schallschutz gegen Außenlärm – von der Lärmkarte bis zur Umplanung

Stand: 27.09.2026. Recherchebefund, keine Rechts- oder Normauskunft. **[V]** = Wortlaut an Primärquelle geprüft (Normtext DIN 4109-1/-2:2018-01 als von Gemeinden veröffentlichte Auslegungsexemplare, BayTB Ausgabe November 2025 und Februar 2025 im StMB-PDF, gesetze-im-internet.de, bverwg.de, Behörden-Metadaten). **[U]** = unsicher, Sekundärquelle oder eigene Auslegung.

Anschluss an frühere Recherchen, ohne sie zu wiederholen:
- **Recherche 14:** Schall *zwischen* Nutzungseinheiten (DIN 4109-1 Tab. 2/3), Nachweis nach § 12 BauVorlV ohne Prüfung.
- **Recherche 08:** Wärmepumpe (LAI-Abstände, TA-Lärm-Richtwerte), RLT-Schall im eigenen Bereich, DIN 1946-6.
- **Recherche 15:** WHO-Leitlinie 2018 als Evidenz Grad A, Regel „Schlafräume zur lärmabgewandten Fassade“.

Diese Recherche ergänzt die Lärmquelle *außen* und den Weg bis zur Bauteilwahl. Der Prototyp dazu ist `arbeit/beispiele/b19_aussenlaerm.py`.

## Ergebnis in 5 Punkten

1. **Die Kernregel ist einfach und vollständig codierbar.** Sie lautet erf R′w,ges = La − K_Raumart, für Wohnräume mit K = 30 dB und mindestens 30 dB (DIN 4109-1:2018, 7.1, Gl. 6).
   - Der Nachweis ist R′w,ges − 2 dB ≥ erf R′w,ges + K_AL. Dabei ist K_AL = 10 lg(S_S/(0,8·S_G)) (DIN 4109-2:2018, Gl. 32/33).
   - R′w,ges ist die energetische Summe aus Wand, Fenstern, Rollladenkästen und Lüftern. Kleine Elemente gehen mit D_n,e,w über A₀ = 10 m² ein (Gl. 35/37/38).
   - Im Holzbau zählt keine Flankenübertragung (4.4.3) [V].
2. **Schwierig ist nicht der Nachweis, sondern der Eingangspegel.** DIN 4109-2 schließt EU-Lärmkarten (Lden/Lnight) für den maßgeblichen Außenlärmpegel ausdrücklich aus (4.4.5.2, Anmerkung) [V].
   - Zulässig sind B-Plan-Angaben, Gutachten nach RLS-19, Schall 03 oder TA Lärm, das Diagramm aus DIN 18005 oder Messungen.
   - Die offenen Lärmkarten (LfU-WMS unter CC BY 4.0, EBA-WMS unter dl-de/by-2-0) taugen deshalb nur zum **Screening** und für den WHO-Hinweis.
3. **In Bayern ist der Nachweis Pflicht, wenn der B-Plan Vorkehrungen nach § 9 Abs. 1 Nr. 24 BauGB festsetzt oder La ≥ 61 dB(A) ist.** Bei Büros liegt die Schwelle bei 66 dB(A) (BayTB 11/2025, Anlage A 5.2/1 Nr. 5) [V].
   - Ab R′w,ges > 50 dB oder La > 80 dB legt die Bauaufsicht die Anforderung im Einzelfall fest. Nötig ist dann eine Messung durch eine VMPA-Prüfstelle (Nr. 1 und 3) [V].
   - An einer Autobahn in 150 m Abstand wird die 61-dB-Schwelle leicht überschritten.
4. **Die wirksamste Maßnahme kostet nichts: Schlafräume an die abgewandte Fassade legen.** DIN 4109-2 erlaubt dort ohne Nachweis −5 dB (offene Bebauung) bzw. −10 dB (geschlossene Bebauung/Innenhof) (4.4.5.1) [V].
   - Seitenfassaden mit Streifsicht werden **nicht** gemindert.
   - Im Prototyp sinkt so erf R′w,ges im Schlafzimmer von 42 auf 36,8 dB. Die Fenster brauchen SSK 3 statt SSK 5, und die Mehrkosten fallen von 5 958 € auf 3 250 € (Beispielpreise).
   - Der Abstand im Grundstück bringt dagegen nur 0,3 dB. Die Rechtsprechung trägt Grundrissorientierung als Lärmschutz (BVerwG 4 CN 2.06).
5. **Lüftung ist Teil des Schallschutzes.** Die Dämmung wirkt nur bei geschlossenem Fenster (DIN 4109-1, 7.3) [V].
   - Ab Nachtpegeln > 45 bzw. > 50 dB(A) empfehlen die Gutachterpraxis bzw. VDI 2719 eine fensterunabhängige, schallgedämmte Lüftung der Schlafräume [U, Sekundärzitate].
   - Die zentrale Lüftung mit WRG im Regnauer-Standard erledigt das und macht Außenwandluftdurchlässe (ALD) im Nachweis überflüssig. Im Beispiel spart das je nach Variante ca. 1 300–2 100 €.
   - Firmenseitig wichtig: Das KlimaPlus-Fenster gibt es laut Ausstattungsbeschreibung nur in SSK 3/4 und nur einflüglig. Nordschlafzimmer an einer Autobahn fallen damit aus dem Katalog.

---

## 1. Regel-Tabelle (Kernwerte, Quellen)

| Regel | Kernwert / Formel | Quelle | Status |
|---|---|---|---|
| Schutzbedürftige Räume | Wohnräume inkl. Wohndielen und Wohnküchen, Schlafräume, Büro, Unterricht. Bad, Flur und Arbeitsküche sind nicht schutzbedürftig | DIN 4109-1:2018, 3.16 | [V] |
| Anforderung | erf R′w,ges = La − K_Raumart. K = 25 (Bettenräume), 30 (Wohnen/Übernachten/Unterricht), 35 (Büro). Mindestens 35/30/30 dB | DIN 4109-1:2018, 7.1, Gl. (6) | [V] |
| Einzelfall | R′w,ges > 50 dB bzw. La > 80 dB: Bauaufsicht legt fest; Messung bei R′w,ges ≥ 50 dB oder La > 80 dB | DIN 4109-1, 7.1; BayTB 11/2025 A 5.2/1 Nr. 1, 3 | [V] |
| Lärmpegelbereiche | Nur wenn *ausschließlich* LPB vorliegen (alte B-Pläne): La = Obergrenze des LPB, I = 55 … VI = 80 dB, VII = Einzelfall. 2016 stand in Tab. 7 noch R′w,res je LPB in 5-dB-Stufen | DIN 4109-1:2018, 7.1, Tab. 7; DAGA 2023 (Meier/Moll) | [V] |
| La Straße | Lr,T + 3 dB; Schlafräume: Lr,N + 3 + 10 dB, wenn Lr,T − Lr,N < 10 dB. Maßgebend ist die Tageszeit mit der höheren Anforderung | DIN 4109-2:2018, 4.4.5.1–4.4.5.2 | [V] |
| La Schiene | wie Straße, zusätzlich Beurteilungspegel pauschal −5 dB | DIN 4109-2, 4.4.5.3 | [V] |
| La Wasser, Luft | +3 dB; Nachtregel gleich. Innerhalb der Schutzzonen nach FluLärmG gilt Gl. (6) nicht, dort gilt die 2. FlugLSV | DIN 4109-2, 4.4.5.4/4.4.5.5; DIN 4109-1, 7.1 | [V] |
| La Gewerbe | Regelfall: Tag-IRW der TA Lärm für die Gebietsart + 3 dB (WA: 55 + 3 = 58 dB). Bei vermuteter Überschreitung: Beurteilungspegel + 3 dB | DIN 4109-2, 4.4.5.6 | [V] |
| Mehrere Quellen | La,res = 10 lg Σ 10^(0,1·La,i). Die +3 dB nur einmal, auf den Summenpegel | DIN 4109-2, 4.4.5.7, Gl. (44) | [V] |
| Abgewandte Seite | −5 dB (offen) bzw. −10 dB (geschlossen/Innenhof) ohne besonderen Nachweis. Lärmschutzwand/-wall: Minderung mit Nachweis nach 16. BImSchV | DIN 4109-2, 4.4.5.1 | [V] |
| EU-Lärmkarten | dürfen für La nicht herangezogen werden | DIN 4109-2, 4.4.5.2, Anm. | [V] |
| Nachweisgleichung | R′w,ges − 2 dB ≥ erf R′w,ges + K_AL | DIN 4109-2, Gl. (32); 5.3.3 (u_prog = 2 dB) | [V] |
| K_AL | 10 lg(S_S / (0,8·S_G)). S_S = alle Außenflächen des Raums, von innen gesehen (auch Dach). S_G = Grundfläche | DIN 4109-2, Gl. (33) | [V] (Faktor 0,8 im OCR-Text unscharf, durch DAGA 2017 gestützt) |
| Summe | R′w,ges = −10 lg Σ 10^(−R_e,i,w/10); R_e,i,w = R_i,w + 10 lg(S_S/S_i) für Bauteile; R_e,i,w = D_n,e,w + 10 lg(S_S/A₀), A₀ = 10 m², für Elemente | DIN 4109-2, Gl. (35), (37), (38) | [V] |
| Unterschiedliche Fassaden | K_LPB = La,max − La,i wird auf alle R der leiseren Fassadenteile addiert | DIN 4109-2, 4.4.1 | [V] |
| Mehrere gleiche Elemente | D_n,e,w = D_n,e,lab,w − 10 lg n. Schlitzlüfter/Kästen über Längenverhältnis. Ungedämmte Öffnung ≈ 10 lg(10 m²/S_Öffnung) | DIN 4109-2, Gl. (39)–(41) | [V] |
| Holzbau | Flankenübertragung bei Holz-, Leicht- und Trockenbau-Außenbauteilen nicht berücksichtigt | DIN 4109-2, 4.4.3 | [V] |
| Fassadenstruktur | Balkone und Loggien werden im Nachweis nach DIN 4109 **nicht** angerechnet (nur Planung, DIN EN 12354-3) | DIN 4109-2, 4.4.1, Anm. 5 | [V] |
| Fenster/Einbaufuge | Kritische Einbausituation (Fenster in der Dämmebene, auch Holzbau): Fugenschalldämmung rechnen | DIN 4109-2, 4.4.4 | [V] |
| Lüftung/Rollladen | Temporäre Lüftungsöffnungen geschlossen, Dauerlüfter im Betriebszustand ansetzen. Schutz nur bei geschlossenem Fenster | DIN 4109-1, 7.3 | [V] |
| Rollladenkasten | Rw = D_n,e,w + 10 lg(S_R/10 m²), direkt in Gl. (37) einsetzbar. Rw nach DIN 4109-35 Tab. 6 oder Messung | BayTB, Anhang RokR, Abschn. 3 | [V] |
| Decke unter Dachraum | Dach und Decke gemeinsam. Erfüllt, wenn die Decke allein höchstens 10 dB unter erf R′w,ges liegt | DIN 4109-1, 7.2 | [V] |
| Nachweispflicht Bayern | B-Plan nach § 9 Abs. 1 Nr. 24 BauGB **oder** La ≥ 61 dB(A) (Aufenthalt, Betten) / ≥ 66 dB(A) (Büro), „auch nach den vorgesehenen Maßnahmen zur Lärmminderung“ | BayTB 11/2025, A 5.2/1 Nr. 5 | [V] |
| Bauteildaten | Nachweis mit DIN 4109-31 bis -36 (inkl. -34/A1, -35/A1). DIN 4109-2 Anh. B, C, D sind nicht anzuwenden. Prüfwerte außerhalb der Kataloge brauchen einen Nachweis nach Art. 15 BayBO (Bauart) | BayTB 11/2025, A 5.2/2, A 5.2/3 | [V] |
| Bautechnischer Nachweis | Schallschutz ist bautechnischer Nachweis (Art. 62 Abs. 1 BayBO). „Die Berechnungen müssen … nachweisen“ (§ 12 BauVorlV). Zu erstellen, auch wenn nicht einzureichen | BayBO Art. 62; BauVorlV § 12; BYAK Merkblatt 1 | [V] |
| Fenster-Schallschutzklassen | SSK 1–6 = 25–29 / 30–34 / 35–39 / 40–44 / 45–49 / ≥ 50 dB am Bau. Prüfstand ≥ 27/32/37/42/47/52 dB | VDI 2719:1987, Tab. 2 (über ift Rosenheim 2015, REHAU) | [V] Sekundär, Klassen konsistent |
| Innenpegel (Planung) | VDI 2719: Schlafräume nachts 25–30 dB(A), Wohnräume tags 30–35 dB(A) | VDI 2719, Tab. 6 (Zitate in B-Plan-Gutachten) | [U] |
| Lüftungsschwelle | > 45 dB(A) nachts: Schlaf bei Kippfenster oft gestört (DIN 18005 Bbl. 1). > 50 dB(A): fensterunabhängige Lüftung (VDI 2719) | Zitate in Gutachten Coesfeld, Bedburg-Hau, Schwerte | [U] |
| Städtebau | DIN 18005 Bbl. 1:2023: WA Verkehr 55/45, Gewerbe 55/40 dB (Orientierungswerte, keine Grenzwerte) | DIN 18005 Beiblatt 1:2023-07 | [V] |
| Straßen-/Schienenbau | 16. BImSchV § 2: WA 59/49 dB(A) (nur bei Bau oder wesentlicher Änderung des Verkehrswegs) | 16. BImSchV | [V] |
| Gewerbe | TA Lärm 6.1: WA 55/40 dB(A), MI 60/45 dB(A); Immissionsort 0,5 m vor dem geöffneten Fenster | TA Lärm (über LfU Bayern) | [V] |
| Fluglärm | Schutzzonen bestehender ziviler Flugplätze: Tag 1 > 65, Tag 2 > 60, Nacht > 55 dB(A) oder 6 × 57 dB(A) L_Amax. Neue/erweiterte: 60/55/50 und 6 × 53 | FluLärmG § 2 Abs. 2 | [V] |
| WHO (Assistenz) | Straße 53/45, Schiene 54/44, Flug 45/40 dB Lden/Lnight | WHO 2018 (über EEA SOER 2020); Recherche 15 | [V] |

## 2. Lärmdaten: Quellen, Zugang, Lizenz, Eignung

| Quelle | Inhalt | Zugang | Lizenz | Eignung für La |
|---|---|---|---|---|
| **LfU Bayern – Lärm an Hauptverkehrsstraßen** | Umgebungslärmkartierung 2017/2022. Autobahnen, Bundes- und Staatsstraßen > 3 Mio. Kfz/a (> 8 200 Kfz/24 h). Lden/Lnight, 10 m-Raster, 4 m Höhe, Methode BUB. Auch Lärmschutzeinrichtungen | WMS `https://www.lfu.bayern.de/gdi/wms/laerm/hauptverkehrsstrassen?`, WFS/Atom laut Metadaten, UmweltAtlas | **CC BY 4.0**, Datenquelle: Bayerisches Landesamt für Umwelt. Dienste geldleistungsfrei | **nein** (nur Screening/WHO) [V] |
| LfU – Ballungsräume (München, Nürnberg, Augsburg, Erlangen, Fürth, Regensburg, Würzburg, Ingolstadt) | Straße, Tram, oberirdische U-Bahn, IED-Anlagen und Häfen | UmweltAtlas; WMS-Übersicht des LfU | vermutlich CC BY 4.0 wie oben [U] | nein |
| LfU – Lärm an Flughäfen (München, Nürnberg) | Lden/Lnight 2022, 10 m-Raster | WMS (LfU-Übersicht) | wie oben [U] | nein (für Flug gilt FluLärmG) |
| **EBA – Umgebungslärmkartierung Schiene, Runde 4** | Juni 2022, Aktualisierung 1.6.2023. Isophonen Lden/Lnight, Rasterkarten, Schallschutzwände. Gesamtes bundeseigenes Netz: ca. 17 000 km pflichtig + 16 000 km erweitert | GeoPortal.EBA; WMS Isophonen, WFS LK 4, WMTS; PDF-Karten | WMS: **dl-de/by-2-0**, © Eisenbahn-Bundesamt. GovData-Shapefile/GeoJSON: „eingeschränkte Nutzung“ | nein [V] |
| **Schallgutachten zum B-Plan** | Beurteilungspegel nach RLS-19/Schall 03/TA Lärm, oft direkt als Karte der **maßgeblichen Außenlärmpegel** je Geschoss oder als LPB | Begründung/Anlage des B-Plans (Gemeinde-PDF) | amtliche Veröffentlichung, Urheberrecht beim Gutachter [U] | **ja**, ggf. an die konkrete Gebäudelage anpassen (Formulierung in Kottermair-Gutachten Peißenberg) [V] |
| DIN 18005 Diagramm | Beurteilungspegel aus Verkehrsmenge und Abstand. DIN 4109-2 verweist auf A.2 der Ausgabe 2002. In der Ausgabe 2023 ist es B.2 nach RLS-19; bis zur Anpassung von DIN 4109-2 gilt das alte Diagramm | DIN 18005-1:2002 / DIN 18005:2023 (kostenpflichtig) | Norm | **ja**, wenn nichts anderes festgelegt ist [V/U] |
| Eigene Berechnung RLS-19 / Schall 03 | Verkehrsmengen (SVZ, DTV, Lkw-Anteil), Deckschicht, Geschwindigkeit, Gelände | Straßenbauverwaltung, DB InfraGO (Zugzahlen) [U] | je Datenquelle | ja, durch Fachplaner |
| Flughafen München | Lärmschutzbereich nach **FluLärmMüV 1996** (Gauß-Krüger-Kurvenpunkte in Anlage 1). Ein Bereich nach dem FluLärmG 2007 ist noch nicht festgesetzt. Übergangsweise gelten regionalplanerische Lärmschutzbereiche (LEP § 3) bis 31.12.2026. Ein Verordnungsentwurf „FluLärmV M“ verlängert bis 31.12.2029 | gesetze-im-internet.de; Regierung von Oberbayern (Lärmaktionsplan); Gemeinde-Ratsinfo (Entwurf) | amtliches Werk | Schutzzonen: ja (FluLärmG) [V]; Stand des Entwurfs [U] |

**Umrechnung Lden/Lnight → Lr,T/Lr,N:** Für den Nachweis ist sie nicht zulässig [V]. Die Unterschiede sind:
- Zeitscheiben: Lden gewichtet den Abend mit 5 dB und die Nacht mit 10 dB [V].
- Rechenmethode: BUB statt RLS-19 [V].
- Rechenhöhe 4 m und Behandlung der Fassadenreflexion [U].

Zum **Screening** kann Lnight(EU) grob als Lr,N gelesen werden, mit einer Unsicherheit von ±3 dB [U, eigene Annahme]. Der Prototyp markiert eine Quelle mit `verfahren = "EU-Lärmkarte"` als `nachweis_tauglich = false`.

## 3. Rechenmodelle und Open Source

| Modell | Anwendung | Status |
|---|---|---|
| RLS-19 | Straße. Seit 1.3.2021 über § 3 der 16. BImSchV verbindlich (Abschn. 3 i. V. m. 1, Deckschichtkorrektur Tab. 4a/4b) | [V] |
| Schall 03 (2014) | Schiene, Anlage 2 zu § 4 der 16. BImSchV | [V] |
| DIN ISO 9613-2 | Ausbreitung im Freien, Gewerbe nach TA Lärm A.2; auch Wärmepumpen (→ B20). Die Neuausgabe ISO 9613-2:2024 ist für die TA Lärm noch nicht eingeführt | [U] |
| CNOSSOS-EU / BUB | Richtlinie (EU) 2015/996. In DE als BUB für die Lärmkartierung (34. BImSchV); Grundlage der LfU- und EBA-Karten | [V] (LfU-Metadaten) |
| AzB (1. FlugLSV) | Fluglärm für Lärmschutzbereiche | [V] (Lärmaktionsplan Obb.) |
| **NoiseModelling** (Univ. Gustave Eiffel/Cerema/CNRS) | Java-Bibliothek, CNOSSOS-EU für Straße und Schiene (Schiene mit französischen Emissionsdaten), H2GIS/PostGIS, WPS-GUI, Docker. Aktuelle Doku v6.0. **Lizenz GPL-3.0**. RLS-19 und Schall 03 sind nicht implementiert | [V] (GitHub, Read the Docs) |
| Weitere | QGIS-Plugin „opeNoise“ (ISO 9613-2) u. a. nicht geprüft | [U] |

**Machbarkeit einer vereinfachten Ausbreitung im Planer:** Für den Variantenvergleich reicht ein Fassadenmodell.
- Bezugspegel aus B-Plan oder Gutachten. Abstandsmaß einer langen Linienquelle 10 lg(d_ref/d).
- Eigenabschirmung über den **Sichtwinkelanteil**: shapely prüft die Sichtlinien gegen den eigenen Baukörper.
- Ergebnis Nordfassade 0 dB, Seitenfassaden ≈ −3 dB (halber Sichtwinkel), Südfassade ohne Sicht.

Für den **Nachweis** darf nur die Pauschale −5/−10 dB an Fassaden **ohne** Sicht angesetzt werden. Seitenfassaden bleiben ungemindert. Größere Minderungen an der Rückseite, physikalisch oft 10–20 dB, gibt es nur mit Gutachten [V Norm, U Physik]. GPL-Code wie NoiseModelling würde als Bibliothek den Planer-Code „infizieren“. Als getrennter Dienst (Prozessgrenze) ist das unkritisch [U, Lizenzauslegung].

## 4. Rechenweg (wie im Prototyp)

```
Eingang: Lr,T, Lr,N je Quelle (RLS-19/Schall 03/TA Lärm), Bezugspunkt, Quellachse
1  Fassadenpegel      Lr,f = Lr,ref + 10 lg(d_ref/d_f) + ΔL_o
                      ΔL_o = 0 (Sicht) | −5 (keine Sicht, offene Bebauung)        [Nachweis]
                      ΔL_o = max(10 lg Sichtanteil, −5)                            [Planung, ANNAHME]
2  La je Fassade      La,Tag   = 10 lg Σ 10^(0,1·(Lr,T,i − 5·[Schiene])) + 3
                      La,Schlaf = 10 lg Σ 10^(0,1·max(Lr,T,i', Lr,N,i' + 10·[ΔLr,i < 10])) + 3
3  Anforderung Raum   erf = max(La,max − K_Raumart, Mindestwert)   je Zeitraum (Tag; Schlaf)
                      K_AL = 10 lg(S_S/(0,8·S_G))
4  Nachweis           R'w,ges = −10 lg[ Σ S_i/S_S·10^(−(R_i+K_LPB,i)/10) + Σ A0/S_S·10^(−(D_n,e,w,j+K_LPB,j)/10) ]
                      erfüllt ⇔ R'w,ges − 2 ≥ erf + K_AL
5  Wahl               min Mehrkosten über {SSK je Fassade} × {Rollladen} × {ALD-Typ, ALD-Fassade};
                      Stufe 1 Firmenkatalog, Stufe 2 Fremdprodukte, sonst Regelverstoß
6  Assistenz          BayTB-Pflicht, Lüftung, Fensterverzicht laute Fassade, Grundrisstausch, WHO, Einzelfall > 50 dB
```

Ob die Nachtregel **je Quelle** vor der Summenbildung angewendet wird oder auf die Summe, regelt der Normtext nicht eindeutig. Der Prototyp wendet sie je Quelle an, wie das Beispiel des Instituts für Holzbau (2024) [U]. Schalltechnisch sind beide Wege gleich, wenn nur eine Quelle wirkt.

## 5. Planungsstrategien (von Bauteil bis Umplanung)

| Stufe | Maßnahme | Wirkung / Regel | Quelle |
|---|---|---|---|
| 1 Bauteil | Fensterklasse je Fassade, schallgedämmter Rollladenkasten oder Vorbau-Raffstore, ALD mit hohem D_n,e,w, ALD an der **leiseren** Fassade (K_LPB) | Nachweis nach DIN 4109-2 | [V] Norm |
| 2 Fenster | weniger oder kleinere Fenster an der lauten Fassade. Seitenwand ohne Fenster | geht über K_LPB ein. Belichtung (Art. 45 BayBO) und zweiten Rettungsweg prüfen | Prototyp |
| 3 Lüftung | KWL mit WRG oder schallgedämmte ALD. Lüftungskonzept nach DIN 1946-6 | DIN 4109-1, 7.3. Das BVerwG sieht das Schlafen bei gekipptem Fenster als Teil angemessenen Wohnens, sonst gibt es einen Anspruch auf Belüftungseinrichtung (Fluglärm) | BVerwG 4 C 4.05 [V] |
| 4 Grundriss | Schlaf- und Kinderzimmer an die abgewandte Seite. An die laute Fassade Bad, Flur, Treppe, Küche, HWR | −5/−10 dB nach DIN 4109-2, 4.4.5.1 | Hamburg-Broschüre [V]; Recherche 15 (Grad A) |
| 5 Puffer | verglaste Loggia, Wintergarten, Prallscheibe, Schallschutzerker vor dem zu öffnenden Fenster | im DIN-4109-Nachweis **nicht** anrechenbar (Fassadenstruktur), nur mit Gutachten/B-Plan-Regelung | DIN 4109-2, 4.4.1 Anm. 5 [V]; B-Plan-Texte Peißenberg [V] |
| 6 „HafenCity-Fenster“ | Kastenfenster mit versetzten Klappen, absorbierender Laibung, Öffnungsbegrenzer 40 mm. Ziel **≤ 30 dB(A) innen bei gekipptem Fenster** nachts. Gemessen R_w = 33 dB gekippt | Hamburger Leitfaden Lärm 2010 (Innenpegel-Festsetzung). In Bayern nicht als Standard eingeführt | hamburg.de [V]; Übertragbarkeit [U] |
| 7 Nicht öffenbare Fenster / Festverglasung | typische B-Plan-Festsetzung für Schlafräume an lauter Fassade, mit fensterunabhängiger Lüftung | **nicht** gegen Gewerbelärm nach TA Lärm (Immissionsort 0,5 m vor dem *geöffneten* Fenster). Passiver Schallschutz gegen Gewerbe ist unzulässig | BVerwG 4 C 8.11 [V]; B-Plan Giengen [V] |
| 8 Baukörper | Riegel: Garage oder Nebengebäude zur Quelle, geschlossene Nordfassade, Rücksprünge. Lärmschutzwand auf dem Grundstück | Minderung nur mit Nachweis (16. BImSchV/RLS-19). Abstandsgewinn im Grundstück ist klein (Linienquelle 3 dB je Verdopplung) | DIN 4109-2, 4.4.5.1 [V]; DIN 18005:2023 Abschn. „Abschirmung“, „Anordnung von Gebäuden“ [V TOC] |
| 9 B-Plan | Festsetzungen nach § 9 Abs. 1 Nr. 24 BauGB: Anordnung von Aufenthaltsräumen, LPB/La-Karten, Lüftung | Grundrissanordnung ist als passiver Schallschutz festsetzbar | BVerwG 4 BN 8.15 [V Sekundär]; BVerwG 4 BN 36.22 (Gemeinde muss Schutzniveau selbst bestimmen) [V Sekundär] |

**Rechtsprechung kurz:**
- **BVerwG 4 CN 2.06 (22.03.2007)** [V]: Bei Verkehrslärm über den Orientierungswerten der DIN 18005 kann eine Gemeinde auf aktiven Schallschutz verzichten. Zulässig ist dann eine Kombination aus passivem Schallschutz, Stellung und Gestaltung der Gebäude und **Anordnung der Wohn- und Schlafräume**.
- Eine spätere Nichtzulassungsentscheidung (2012, Az. nicht geprüft) nennt es für neu Einziehende „zumutbar, zur **architektonischen Selbsthilfe** zu greifen“ [U].
- **BVerwG 4 C 8.11 (29.11.2012)** [V]: Gegen die Überschreitung der Außen-IRW durch **Gewerbe** hilft passiver Lärmschutz nicht.
- Für Verkehrslärm bleibt der Weg über Grundriss und Bauteile offen. Das ist für Grundstücke neben Gewerbe entscheidend. Die **Wärmepumpe des Nachbarn** fällt unter die TA Lärm (→ Recherche 08, B20).

## 6. Erschütterungen nahe Bahn

- **DIN 4150-2** ist 2025-08 neu erschienen [V DIN Media]. Die Beurteilung von Schienenverkehrserschütterungen ist „vollständig geändert“ (6.5.3). Urbane Gebiete sind in Tab. 1 aufgenommen, der frühere Anhang A ist entfallen.
- Bewertet wird KB_F,max gegen A_u/A_o, dazu KB_FTr gegen A_r. Das LfU nennt die Werte der Ausgabe 1999 (WA nachts A_u 0,1 / A_o 0,2 / A_r 0,05) [V]. Die neuen Tabellenwerte sind nicht geprüft [U].
- **Sekundärer Luftschall** entsteht, wenn Decken und Wände abstrahlen. Nach den LAI-Hinweisen 2018 wird er nach den akustischen Regelwerken beurteilt (TA Lärm, bei tiefen Frequenzen DIN 45680) [V].
- **Holzbau:** Leichte Holzbalkendecken haben tiefe Eigenfrequenzen und wenig Masse. Liegen diese im Anregungsbereich des Bahnverkehrs, drohen Resonanzüberhöhung und abstrahlender Sekundärschall. Die LAI nennt „Resonanzen“ als Fall für Einzeluntersuchungen [V]. Belastbare Kennzahlen für Holzdecken neben Bahnstrecken fehlen in dieser Recherche [U].
- Regel für den Planer: Liegt eine Bahnlinie < 50–100 m entfernt [U, Faustbereich], ergeht ein Hinweis „Erschütterungsgutachten nach DIN 4150-2 prüfen“. Keine Rechnung.
- Die BayTB führen Erschütterungsschutz als bautechnischen Nachweis (Art. 62 BayBO, § 12 BauVorlV) [V].

## 7. Gesundheit (Assistenz, nicht bindend)

- Die WHO-Werte (Straße 53/45, Schiene 54/44, Flug 45/40 dB Lden/Lnight) sind für die Assistenz der richtige Maßstab für *Wirkung* (Recherche 15, Grad A).
- Die offenen EU-Lärmkarten liefern genau diese Größen. Der Planer kann sie deshalb ohne Gutachten anzeigen, mit dem Hinweis „nicht rechtlich bindend, kein Nachweis“.
- Laientext im Prototyp: „Das ist kein Bauverbot, aber ein Grund, Schlafräume ruhig zu legen.“

## 8. IFC-Mapping (geprüft gegen IFC4X3_ADD2 mit IfcOpenShell 0.8.5)

| Information | IFC-Träger | Befund |
|---|---|---|
| Rw Wand/Dach/Fenster/Tür als Text | `Pset_WallCommon.AcousticRating`, `Pset_RoofCommon`, `Pset_WindowCommon`, `Pset_DoorCommon`, `Pset_SlabCommon`, `Pset_CoveringCommon`, `Pset_CurtainWallCommon`, `Pset_PlateCommon`, `Pset_OpeningElementCommon` – jeweils **IfcLabel** | [V] Nur Text, deshalb Vokabular per IDS festlegen („Rw 42 dB (SSK 4 VDI 2719)“) |
| Rw, D_n,e,w als Zahl | eigenes Pset `HB_Schallschutz_Bauteil` (IfcReal, Klasse IfcInteger, Fassade) | [V] Kein Standard-Pset mit numerischem Rw. Präfix nicht „Pset_“ |
| Pegel | `IfcSoundPressureLevelMeasure` (existiert); `IfcDerivedUnitEnum.SOUNDPRESSURELEVELUNIT` | [V] |
| Raum schutzbedürftig / Schlafnutzung, La, erf R′w,ges, K_AL, Ergebnis | eigenes Pset `HB_Aussenlaerm_Raum` an `IfcSpace`. Nutzungsart über `Pset_SpaceOccupancyRequirements.OccupancyType` | [V] `Pset_SpaceCommon` hat keine Akustik-Property |
| Fassadenpegel / Immissionsort | `IfcAnnotation` (PredefinedType USERDEFINED, ObjectType „Immissionsort“) + `HB_Fassadenpegel` (Lr/La als IfcSoundPressureLevelMeasure, Verfahren, Annahme) | [V] validiert. `Pset_SoundAttenuation` (an IfcAnnotation) beschreibt Frequenz/Zeitreihe und passt nicht |
| Lärmquelle | `IfcAnnotation` mit Achse; bei Straße ggf. Verweis auf `IfcRoad`/`IfcAlignment` | [U] Entwurfsvorschlag |
| Lärmkarte (Raster) | außerhalb IFC (GeoTIFF/WMS), Verweis per `IfcDocumentReference` | [U] Vorschlag. `IfcGeographicElementTypeEnum` kennt nur SOIL_BORING_POINT, TERRAIN, VEGETATION [V] |
| Dachflächenfenster | `IfcWindow` PredefinedType SKYLIGHT | [V] |
| ALD | `IfcAirTerminal` (GRILLE/LOUVRE), `Pset_AirTerminalTypeCommon.HasSoundAttenuator` (IfcBoolean) + HB-Pset D_n,e,w | [V] |
| Rollladen | `IfcShadingDevice` (SHUTTER/JALOUSIE); Kasten als Element mit D_n,e,w im HB-Pset | [V] Enum; Kastenmodell [U] |
| Lärmschutzwand | `IfcWall` USERDEFINED („Laermschutzwand“). `IfcWallTypeEnum` hat kein NOISEBARRIER | [V] |

Der Prototyp schreibt `ausgabe/b19_aussenlaerm_A.ifc` und `_B.ifc`. Sie haben 253 bzw. 258 Entitäten und sind byte-identisch reproduzierbar. `ifcopenshell.validate` mit EXPRESS-Regeln meldet nichts.

## 9. Prototyp B19 – Ergebnisse

`python b19_aussenlaerm.py [--modus nachweis|planung] [--lueftung ALD|KWL] [--ifc]`, Tests: `python -m pytest tests/test_b19.py` → **16 passed** (0,6 s Laufzeit des Beispiels).

**Eingang (Beispiel):**
- Autobahn als 4 km lange Linienquelle, 150 m nördlich der Nordfassade.
- Lr,T = 66 / Lr,N = 59 dB(A) nach RLS-19 am Ort der Nordfassade, Freifeld. Die Differenz liegt unter 10 dB, deshalb greift die Nachtregel.
- EU-Karte Lden 68 / Lnight 59 dB (nur WHO-Hinweis).
- Haus 11 × 8 m, lichte Raumhöhe 2,5 m.
- Außenwand Holzrahmen + Holzfaser-WDVS mit Rw 47 dB (Beispiel nach ift-Prüfbericht).
- Fenster Rw = VDI-Prüfstandswert der Klasse. Regnauer-Katalog: SSK 2–4, SSK 3/4 nur einflüglig.
- Rollladen: Aufsatzkasten D_n,e,w 44/50 dB oder Vorbau-Raffstore. ALD mit D_n,e,w 36/44/52 dB.
- Preise sind frei gewählte Mehrpreise.

**Fassadenpegel (Modus Nachweis):**

| Fassade | Sichtanteil | ΔL | La,Tag | La,Schlaf |
|---|---|---|---|---|
| N | 1,00 | 0 | 69,0 | 72,0 |
| E / W | 0,50 | 0 (Streifsicht, keine Minderung) | 68,9 | 71,9 |
| S | 0,00 | −5 (DIN 4109-2, 4.4.5.1) | 63,8 | 66,8 |

**Obergeschoss, Lüftung ALD, Modus Nachweis:**

| Variante | Raum | Fassaden | La,max | erf R′w,ges | K_AL | Wahl | Mehrkosten |
|---|---|---|---|---|---|---|---|
| A | Schlafen | N, W | 72,0 | 42,0 | +1,7 | SSK N:5, W:4, Vorbau-Raffstore, ALD 52 dB | 2 174 € – **Fremdprodukt** |
| A | Kind | E, N | 72,0 | 42,0 | +1,9 | SSK 5/5, Vorbau-Raffstore, ALD 52 dB | 2 150 € – **Fremdprodukt** |
| A | Arbeiten (Tag) | S, W | 68,9 | 38,9 | +1,9 | SSK 3/3, AK schallgedämmt, ALD 44 dB (S) | 615 € |
| B | Schlafen | S | 66,8 | **36,8** | −1,1 | SSK 3, AK Standard, ALD 52 dB | 672 € |
| B | Kind (Westwand ohne Fenster) | S, W | 71,9 | 41,9 | +2,2 | SSK 4, AK schallgedämmt, ALD 44 dB (S) | 630 € |
| B | Arbeiten (Tag) | N, W | 69,0 | 39,0 | +1,7 | SSK 4/4, AK schallgedämmt, ALD 44 dB (W) | 930 € |

Das Wohnen im EG ist in beiden Varianten gleich: erf 39,0 dB, SSK N:3/W:3. Die Hebe-Schiebe-Tür im Süden bleibt bei SSK 2 (mehrflüglig), das K_LPB von +5 dB reicht. Mehrkosten 1 018 €.

**Vergleich:**

| Modus / Lüftung | Mehrkosten A → B | max. SSK A → B | Fenster ≥ SSK 4 A → B | Regelverstöße A → B |
|---|---|---|---|---|
| Nachweis / ALD | 5 958 € → 3 250 € | 5 → 4 | 4 → 3 | 2 → 0 |
| Nachweis / KWL | 3 827 € → 1 913 € | 5 → 4 | 4 → 1 | 2 → 0 |
| Planung / ALD | 3 865 € → 2 454 € | 4 → 4 | 5 → 2 | 0 → 0 |
| Planung / KWL | 2 256 € → 1 166 € | 4 → 4 | 3 → 2 | 0 → 0 |

**Befunde:**
1. Der Grundrisstausch senkt die Anforderung im Schlafzimmer um 5,2 dB und halbiert die Mehrkosten. Er beseitigt beide Regelverstöße, denn Variante A ist mit dem Firmenkatalog nicht nachweisbar.
2. Das Kinderzimmer SW (Variante B) profitiert im Nachweismodus kaum, nur 0,1 dB. Grund ist die fensterlose Westwand: Sie hat Streifsicht auf die Autobahn und bestimmt deshalb La,max, obwohl dort kein Fenster sitzt.
   - Die Norm rechnet mit dem höchsten La an *irgendeiner* Außenfläche des Raums.
   - Eine Minderung der Seitenfassade braucht ein Gutachten. Im Planungsmodus (−3 dB) sinkt die Anforderung auf 38,9 dB.
3. Der Optimierer setzt den ALD an die leisere Fassade. Dort wirkt K_LPB mit +5 dB, und ein billigerer ALD reicht (Kind B, Arbeiten A).
4. Fensterverzicht (Planungsmodus, Variante A): Ohne Nordfenster sinkt die Wahl im Schlafzimmer von 1 530 € auf 550 €, im Kinderzimmer von 1 345 € auf 594 €. Offen bleibt die Belichtung.
5. Assistenzausgaben: Nachweispflicht nach BayTB (La 69 ≥ 61), Lüftungskonzept (Lr,N 59 > 45/50), Abstand bringt nur 0,3 dB, Terrasse (Lr,T Süd 61 > OW 55), WHO-Hinweis (Lden 68 > 53).

**Grenzen des Prototyps:**
- Ein Geschoss als Fassadenpunkt, keine Höhenabhängigkeit (das OG ist real oft 1–2 dB lauter).
- Keine Reflexionen, kein Boden, keine Meteorologie.
- Dach/Decke (DIN 4109-1, 7.2) nicht gerechnet.
- Keine Einbaufugen (4.4.4).
- Rw der Fenster pauschal je Klasse.
- Kosten fiktiv.

## 10. Warnungen

1. **EU-Lärmkarten nie als La verwenden** (DIN 4109-2, 4.4.5.2, Anm.). Ein Planer, der „automatisch aus der Lärmkarte“ nachweist, produziert einen unzulässigen Nachweis.
2. **Seitenfassaden nicht mindern** ohne Gutachten. Die −5/−10 dB gelten nur für die *abgewandte* Seite.
3. **Kinderzimmer, Gästezimmer und Ein-Zimmer-Wohnräume** sind nach Gutachterpraxis wie Schlafräume zu behandeln. Die Norm sagt: „überwiegend zum Schlafen genutzt werden *können*“ [V Wortlaut; Einstufung U]. „Arbeiten“ als Tagraum einzustufen ist eine Designentscheidung mit Risiko.
4. **Schienenbonus −5 dB** gilt nur für La (DIN 4109-2, 4.4.5.3). Für Orientierungs- und Grenzwerte gilt er nicht, und die geplante Normrevision will ihn streichen (DAGA 2023) [V als Vorschlag].
5. **Normrevision läuft:** Vorgesehen sind (R′w + C/Ctr) mit La,T − 35 / La,N − 25 dB. Der Nachtzuschlag und die LPB-Anwendung sollen entfallen („ausdrücklich vorläufig“, DAGA 2023) [V als Vorschlag]. E DIN 4109-33:2026-09 liegt als Entwurf vor [V]. Die Regeln deshalb **versioniert** hinterlegen.
6. **Prüfwerte aus Prüfberichten** außerhalb der Kataloge DIN 4109-32 bis -35 brauchen in Bayern einen Nachweis nach Art. 15 BayBO (BayTB A 5.2/3) [V]. Ein ift-Prüfbericht allein genügt nicht; laut Prüfbericht ist in DE ein abP nötig [V].
7. **Holzfenster in der Dämmebene** sind nach DIN 4109-2, 4.4.4 eine kritische Einbausituation. Dann ist die Fugenschalldämmung zu rechnen, sonst ist der Nachweis zu optimistisch.
8. **Loggien, Balkone und Wintergärten** zählen im DIN-4109-Nachweis nicht (4.4.1, Anm. 5). Wer sie als Puffer verkauft, braucht einen gesonderten Nachweis oder eine B-Plan-Regel.
9. **Gewerbe:** Gegen TA-Lärm-Überschreitungen helfen Schallschutzfenster rechtlich nicht (BVerwG 4 C 8.11). Der Planer darf das nicht als „gelöst“ anzeigen.
10. **Flughafen München:** Der Lärmschutzbereich nach dem FluLärmG 2007 ist noch nicht festgesetzt. Der regionalplanerische Übergang endet am 31.12.2026. Die Verlängerung bis 2029 ist nur als Entwurf gefunden. Den Status vor jeder Nutzung prüfen.
11. **Regnauer-Ausstattungsbeschreibung** sagt „Schallschutznachweis, sofern von Behörde gefordert“. In Bayern ist er bei La ≥ 61 dB(A) als bautechnischer Nachweis **immer** zu erstellen, auch im Freistellungsverfahren und auch ohne Anforderung (Art. 62 BayBO, BYAK) [V]. Das ist ein Vertragsrisiko.
12. **Maximalpegel** (Bahn, Flug) bleiben in DIN 4109 außen vor (4.4.5.1, Anm.). Bei Güterverkehr nachts kann ein Gutachter L_AF,max-Ansätze wählen (Gutachten Gauting, nach DIN 4109-4:2016 C.2) [U]. Der Planer sollte dann nur warnen.

## 11. Offene Fragen an Regnauer

1. **Vitalwand:** Welches Rw (C; Ctr) hat sie, mit welchem Nachweis (DIN-4109-33-Zeile, abP, Prüfbericht)? Gilt der Wert je Fassadenvariante (Putz/Holzschalung, Holzfaser 80/100 mm, EPS-Option) und mit bzw. ohne Installationsebene? Die Ausstattungsbeschreibung nennt nur „Prüfzeugnisse für Schall-, Wärme- und Brandschutz“.
2. **KlimaPlus-Fenster:** Welches Rw hat die Standardausführung? Welche Rw-Werte und Prüfzeugnisse gibt es für SSK 3 und SSK 4? Warum gilt das nur einflüglig? Gibt es Stulp- oder Hebe-Schiebe-Elemente mit ≥ SSK 3? Welches Einbaudetail (Fuge in der Dämmebene, DIN 4109-2, 4.4.4)?
3. **Rollladen/Raffstore:** Welche Kastenbauarten (Aufsatz, Vorbau, integriert) gibt es, mit welchem D_n,e,w bzw. Rw nach RokR und Ü-Zeichen?
4. **Lüftung:** Wo liegen die Außen- und Fortluftdurchlässe der zentralen KWL (Proxon)? Welche Schalldämpfer werden verbaut? Wird für Häuser ohne KWL ein ALD-Typ mit D_n,e,w angeboten?
5. **Dachflächenfenster und Dach:** Welches Rw haben die Dachflächenfenster und die Dachaufbauten (Zwischen-/Aufsparrendämmung, Sichtdachstuhl)? Sichtsparrendächer gelten bei Außenlärm als nur bedingt geeignet (Meier, Forum Holzbau).
6. **Prozess:** Wer erstellt den Schallschutznachweis gegen Außenlärm, und ab welchem La? Gibt es Referenzprojekte an Autobahnen, Bahnlinien oder Flughäfen (Freising/Erding), die als Präzedenzfälle dienen können?
7. **Preise:** Welche Mehrpreise gelten für SSK 3/4 und für schallgedämmte Kästen? Nur dann werden die Kostenvergleiche des Planers belastbar.
8. **Erschütterungen:** Gibt es Erfahrungen mit der Silence-Decke neben Bahnstrecken (Resonanz, sekundärer Luftschall)?

## 12. Literatur und Quellen (abgerufen 27.09.2026)

- DIN 4109-1:2018-01 und DIN 4109-2:2018-01, Auslegungsexemplare in kommunalen B-Plan-Unterlagen (verwaltungsportal.de). Abschn. 3.16, 7.1–7.3; 4.4.1–4.4.5, 5.3.3 [V]
- DIN (NABau): Auslegungen zu DIN 4109 (din.de, Stand 2021): Beispiele La Tag/Schlaf, Sicherheitsbeiwert für Fenstertüren, Rundung [V]
- StMB: Bayerische Technische Baubestimmungen, Ausgabe November 2025 (BayMBl. 2025 Nr. 480) und Februar 2025, lfd. Nr. A 5.2.1, Anlagen A 5.2/1–3; Anhang RokR [V]
- BayBO Art. 13, Art. 62 (gesetze-bayern.de, lexmea.de); BauVorlV § 12; BYAK Merkblatt 1 „Checkliste Bauantrag“ [V]
- 16. BImSchV §§ 2–4 mit RLS-19, Schall 03 (gesetze-im-internet.de); BT-Drs. 19/18471 [V]
- FluLärmG § 2 (gesetze-im-internet.de); FluLärmMüV 1996; Regierung von Oberbayern: Lärmaktionsplan Flughafen München; Entwurf FluLärmV M (Ratsinfo Neufahrn) [V/U]
- DIN 18005 Beiblatt 1:2023-07, Tab. 1 (verwaltungsportal.de); DIN 18005:2023-07 (DIN Media); Gigla, bauen+ 6/2023 [V]
- LfU Bayern: Geodatendienst „Lärm an Hauptverkehrsstraßen – WMS“, Ergebnisse der Lärmkartierung, Anlagenlärm, Erschütterungen [V]
- Eisenbahn-Bundesamt: Lärmkartierung Runde 4, GeoPortal.EBA, INSPIRE-Metadaten „(WMS) Lärmaktionsplan Runde 4“ (dl-de/by-2-0); GovData-Datensatz Schienenstrecken Bund [V]
- Meier, A.; Moll, A.: Schallschutz gegen Außenlärm – Ergebnisse eines Forschungsvorhabens. DAGA 2023; Meier, A.: Stand der Regelung – Schallschutz gegen Außenlärm in DIN 4109. DAGA 2017 [V]
- Frey: Anwendungsbereich der DIN 4109 unter Berücksichtigung der spektralen Eigenschaften … (Masterarbeit 2019, sp-laermschutz.de) [V]
- Institut für Holzbau (Krause, M.): Berechnungsbeispiel Außenlärm nach DIN 4109:2018 (2024) [V]
- Stucki/Meier: Schallschutz gegen Außenlärm bei Holzbauweisen (Forum Holzbau) [V]
- ift Rosenheim, Saß, B.: Schalldämmung von Fenstern im eingebauten Zustand (Rosenheimer Fenstertage 2015); ift-Prüfbericht 17-002083-PR01 (Informationsdienst Holz), Holzständer-WDVS Rw 47 (−1; −7) dB [V]
- Holzfaser-WDVS Detailkatalog Holzrahmenbau 03-2025 (holzfaser.org): Rw ≥ 51 dB nach DIN 4109-33 [V Verbandsangabe]
- VDI 2719:1987-08 (Inhaltsverzeichnis Intertek; Klassen über ift/REHAU) [V/U]
- Hamburger Leitfaden Lärm in der Bauleitplanung 2010; Broschüre „Schallschutz bei teilgeöffneten Fenstern“ (hamburg.de) [V]
- BVerwG 4 CN 2.06 (22.03.2007); 4 C 8.11 (29.11.2012); 4 C 4.05 (21.09.2006) (bverwg.de) [V]; 4 BN 8.15 (26.05.2015, JuraForum), 4 BN 36.22 (18.01.2023, NWB), 4 BN 2.11 (31.03.2011) [V Sekundär/Volltext]
- DIN 4150-2:2025-08 (DIN Media, Auslegungen DIN 2025); LAI-Hinweise Erschütterungen 2018 [V]
- WHO Environmental Noise Guidelines 2018; EEA SOER 2020 Kap. 11 [V]
- NoiseModelling (GitHub Universite-Gustave-Eiffel/NoiseModelling, GPL-3.0; noisemodelling.readthedocs.io v6.0); Bocher et al. 2019, ISPRS IJGI 8(3):130 [V]
- Regnauer: Bauleistungs- und Ausstattungsbeschreibung 10/2024 (Abschn. 1.4, 5.3, 5.5, 5.6, Lüftung) [V]
- Schallgutachten in B-Plan-Verfahren (Kottermair/Peißenberg, Dinkelscherben; Büchlberg; Greiner/Gauting; Coesfeld; Bedburg-Hau; Schwerte; Giengen; Bad Segeberg) als Praxisbelege für BayTB-Zitate und Festsetzungstexte [V als Zitat, Inhalte U]

# Recherche 14: Gebäudetypen – Regel-Deltas gegenüber dem Einfamilienhaus

Stand: 27.09.2026. Recherchebefund, keine Rechtsberatung. **[V]** = Wortlaut an Primärquelle geprüft (BayBO-Fassung „gilt ab 01.05.2026“ auf gesetze-bayern.de, Bundesrecht auf gesetze-im-internet.de). **[U]** = unsicher, Sekundärquelle oder eigene Auslegung.

## Ergebnis in 5 Punkten

1. **Die Gebäudeklasse ist der Hauptschalter, aber nicht der einzige.** Sie folgt aus drei Größen: Höhe (Oberkante Fußboden des obersten Geschosses, in dem ein Aufenthaltsraum *möglich* ist), Zahl der Nutzungseinheiten und deren Fläche (BGF ohne Keller). Dazu kommt, ob das Gebäude freisteht (Art. 2 Abs. 3). Daneben gibt es eigene Schwellen: mehr als 2 Wohnungen (Barrierefreiheit), mehr als 3 Wohnungen (Bauvorlage), mehr als 5 Wohnungen (Spielplatz nur mit Satzung), Höhe über 13 m (Aufzug) und über 22 m (Hochhaus = Sonderbau). Diese Schwellen sind voneinander unabhängig [V].
2. **Die Bauvorlageberechtigung des Zimmerermeisters endet früher als gedacht.** Sie gilt nur für Wohngebäude der GK 1–3 mit höchstens 3 Wohnungen, die *freistehend oder nur einseitig angebaut* sind (Art. 61 Abs. 3 Nr. 1). Ein **Reihenmittelhaus** fällt heraus, ebenso jedes Mehrfamilienhaus ab 4 Wohnungen. Dafür braucht es Architekten oder Listen-Ingenieure [V].
3. **Holzbau ab GK 4 ist ein eigenes Regelwerk.** Bauteile müssen hochfeuerhemmend bzw. feuerbeständig sein. Gilt die HolzBauRL 2024-09 (BayTB 11/2025, lfd. Nr. A 2.2.1.4), sind das 2 × 15 mm bzw. 2 × 18 mm GKF/GF und **nichtbrennbare Dämmung mit Schmelzpunkt ≥ 1000 °C**. In GK 5 sind Treppenraumwände und Brandwände nicht in Holz möglich. Die Standsicherheit prüft ab GK 4 immer ein Prüfsachverständiger, den Brandschutz erst ab GK 5 [V].
4. **Schallschutz wird Pflicht, sobald es zwei Wohnungen gibt, also schon beim EFH mit Einliegerwohnung.** DIN 4109-1:2018 Tab. 2 verlangt für Wohnungstrenndecken R′w ≥ 54 dB und L′n,w ≤ 50 dB. Für Holzdecken nach DIN 4109-33 gilt ≤ 53 dB. Tab. 3 verlangt für Haustrennwände von Doppel- und Reihenhäusern R′w ≥ 59 dB bzw. **≥ 62 dB**, praktisch nur zweischalig erreichbar [V].
5. **Den Gebäudetyp darf die Regelmaschine nicht als Etikett wählen lassen.** Sie muss ihn als Merkmalsvektor aus dem IFC ableiten. Manche Merkmale sind nicht deterministisch entscheidbar: ob zwei Hälften ein „Doppelhaus“ sind (BVerwG 4 C 12.14: „weder abstrakt-generell noch mathematisch-prozentual“) oder ob ein Gebäude „Wohngebäude“ ist. Solche Merkmale brauchen eine menschliche Freigabe [V/U].

---

## 1. Matrix Gebäudetyp × Regelbereich

Referenz ist das bisherige Konzept: freistehendes EFH, GK 1, 1 Nutzungseinheit. „wie EFH“ heißt: kein Delta.

### 1a. Klasse, Verfahren, Brandschutz

| Typ | GK (typisch) | Bauvorlage (Art. 61) | Prüfpflicht Statik / Brand (Art. 62a/b) | Brandschutz-Kern (Art. 25–33) |
|---|---|---|---|---|
| **EFH** (Referenz) | 1 (freistehend, h ≤ 7 m, ≤ 400 m²) | Abs. 3: auch Zimmerermeister | keine / keine | keine Anforderungen an tragende Teile. Kellerwände und -decken feuerhemmend |
| **EFH > 400 m² BGF** | **3** | Abs. 3 (GK 3, 1 WE) | Kriterienkatalog / keine | tragende Teile, Decken feuerhemmend. Keller feuerbeständig. Notwendiger Treppenraum nötig |
| **Bungalow** | 1 | wie EFH | wie EFH | ebenerdig bis 400 m²: **ein** Rettungsweg genügt (Art. 31 Abs. 1 S. 2 Nr. 2) |
| **Tiny House / Modul** | 1 | wie EFH | keine; Typenprüfung möglich (Art. 62a Abs. 2 S. 3 Nr. 2) | wie EFH. „Ortsfest benutzt“ heißt bauliche Anlage (Art. 2 Abs. 1 S. 3) |
| **EFH + Einliegerwohnung / ZFH** | 1 (freistehend) oder 2 | Abs. 3 | keine / keine | innerhalb GK 1/2 keine Trennwand-Pflicht (Art. 27 Abs. 6). Decken in GK 2 feuerhemmend. 2 Rettungswege **je Wohnung** |
| **Doppelhaushälfte** | 2 (nicht freistehend) | Abs. 3 („einseitig angebaut“) | keine / keine | **Gebäudeabschlusswand**: in GK 1/2 gilt Art. 27 entsprechend, also mindestens feuerhemmend (Art. 28 Abs. 2 S. 2). Bis unter die Dachhaut (Abs. 5 S. 2) |
| **Reihenendhaus** | 2 (h > 7 m: **4**) | Abs. 3 | GK 2: keine. GK 4: PSV Statik | wie DHH. In GK 4: hochfeuerhemmend + mechanische Beanspruchung (Art. 28 Abs. 3 S. 2 Nr. 1) |
| **Reihenmittelhaus** | 2 (h > 7 m: **4**) | **nicht Abs. 3** (beidseitig angebaut) → Architekt/Ingenieur | wie Endhaus | zwei Abschlusswände. Bei traufseitiger Reihung Dach feuerhemmend von innen (Art. 30 Abs. 6) [U] |
| **MFH GK 3** (h ≤ 7 m) | 3 | ≤ 3 WE und freistehend: Abs. 3. **≥ 4 WE: Abs. 2** | Kriterienkatalog / keine | tragende Teile, Decken, Trennwände feuerhemmend. Treppenraum feuerhemmend. Treppe nichtbrennbar **oder** feuerhemmend |
| **MFH GK 4** (≤ 13 m, NE ≤ 400 m²) | 4 | Abs. 2 | **PSV Statik immer** / keine Prüfung, aber Bestätigung der Bauausführung (Art. 78) | alles hochfeuerhemmend (HolzBauRL). Treppe **nichtbrennbar**. Treppenraum hochfeuerhemmend + mechanisch |
| **Holz-Geschossbau GK 5** (≤ 22 m) | 5 | Abs. 2 | PSV Statik **und** PSV Brand / Bauaufsicht | feuerbeständig („abweichend feuerbeständig“ nach HolzBauRL). Treppenraum Bauart Brandwand, **nichtbrennbar** |
| **Wohn- und Geschäftshaus** | 3–5 | Abs. 2 (kein reines Wohngebäude) [U] | wie GK. Sonderbau: Prüfung durch Behörde/Prüfingenieur | zusätzlich Sonderbau-Schwellen (Art. 2 Abs. 4), notwendige Flure ab NE > 200 m², Türen zu Läden feuerhemmend + rauchdicht |

### 1b. Schall, Barrierefreiheit, Pflichten, Eigentum, TGA

| Typ | Schall (DIN 4109-1) | Barrierefreiheit / Aufzug | Spielplatz / Stellplätze | WEG | TGA-Besonderheiten |
|---|---|---|---|---|---|
| EFH | keine Anforderung im eigenen Bereich | – | Stellplatz nur per Satzung | – | – |
| EFH + ELW / ZFH | **Tab. 2**: Decke R′w 54 / L′n,w 53 (Holz), Wand 53 | – | Satzung je Wohnung | Aufteilung möglich | HeizkostenV gilt; Ausnahme nach § 2, wenn der Vermieter eine der ≤ 2 Wohnungen bewohnt. TrinkwV § 31 nicht (ZFH) |
| DHH / RH | **Tab. 3**: Haustrennwand 59 (unterstes Geschoss) / 62 dB; Decken L′n,w 41; Treppen 46 | – | Satzung | Realteilung oder WEG mit Sondereigentum/-nutzung | Anschlüsse je Haus. Bei gemeinsamer Anlage Gebäudenetz (GModG § 3 Nr. 9a) |
| MFH GK 3 | Tab. 2 inkl. Treppenraumwände 53, Wohnungstüren Rw 27/37 | **> 2 WE**: Wohnungen eines Geschosses barrierefrei erreichbar (DIN 18040-2 ohne „R“) | Spielplatz nur mit Satzung **> 5 WE**; Abstellräume für Kinderwagen/Fahrräder (Art. 46 Abs. 2) | Aufteilungsplan + Abgeschlossenheit | TrinkwV § 31 bei > 400 l / > 3 l und Vermietung. HeizkostenV fernablesbar. Hausanschlussraum ab > 5 NE [U] |
| MFH GK 4 | wie GK 3; Aufzugsschacht 57 dB | wie GK 3; **kein** Aufzugszwang (h ≤ 13 m) | wie GK 3 | wie GK 3 | Leitungsdurchführungen nach LAR, Abschottungen hochfeuerhemmend |
| GK 5 | wie GK 3 | **Aufzug Pflicht** (h > 13 m), Trage 1,10 × 2,10 m; **⅓** der Wohnungen barrierefrei erreichbar; Wohnungstüren 0,90 m | wie GK 3 | wie GK 3 | Sicherheitsbeleuchtung in fensterlosen Treppenräumen, Rauchabzug oben |
| Wohn-/Geschäftshaus | Tab. 2 „fremde Arbeitsräume“, Abschn. 8/9 (laute Räume, Gewerbe) | öffentlich zugängliche Teile barrierefrei (Art. 48 Abs. 2) | Satzung je Nutzung | Teileigentum | GModG § 106: Nichtwohnteil getrennt. Bayerische PV-Pflicht für Nichtwohngebäude (Art. 44a Abs. 2) [U, gemischt] |

---

## 2. Detailabschnitte

### 2.1 Gebäudeklassen und Nutzungseinheiten (BayBO Art. 2) [V]

- **GK 1**: freistehend, h ≤ 7 m, ≤ 2 NE mit zusammen ≤ 400 m². **GK 2**: wie GK 1, aber nicht freistehend. **GK 3**: sonstige mit h ≤ 7 m. **GK 4**: h ≤ 13 m und jede NE ≤ 400 m² (oder abgetrennte Teile mit eigenen Rettungswegen). **GK 5**: sonstige, auch unterirdische.
- **h** = OKFF des höchsten Geschosses, in dem ein Aufenthaltsraum *möglich* ist, über dem mittleren Gelände (Abs. 3 S. 2). Ein ausbaufähiger Dachraum zählt also schon mit.
- **Flächen**: BGF (Abs. 6), Kellergeschosse zählen nicht (Abs. 3 S. 3). Kellergeschoss heißt: Deckenoberkante im Mittel ≤ 1,40 m über Gelände (Abs. 7).
- **Sonderbau**, relevant für Wohn- und Geschäftshäuser (Abs. 4):
  - Hochhaus > 22 m
  - Verkaufsstätte > 800 m² (erdgeschossig > 2000 m²)
  - Büro/Verwaltung mit Einzelraum > 400 m²
  - Raum für > 100 Personen
  - Gaststätte > 60 Gastplätze (nur EG: > 100)
  - Beherbergung > 30 Betten
  - Pflege-Nutzungseinheiten > 6 Personen
  - Kita > 10 Personen
  - Wohngebäude sind vom Auffangtatbestand Nr. 21 ausgenommen.
- **Typische Kipppunkte**:
  - Reihen- oder Stadthaus mit ausgebautem Dachgeschoss: OKFF DG etwa 8 m, damit **GK 4**.
  - „Villa“ mit 1 WE und 450 m² oberirdischer BGF: **GK 3**.
  - Doppelhaushälfte: nie GK 1, da nicht freistehend.
  - Tiny House: fast immer GK 1.

### 2.2 Bauvorlageberechtigung und Prüfpflichten

- **Art. 61 Abs. 3** [V]:
  - Architektur-/Bauingenieure, staatlich geprüfte Techniker, Maurer-, Betonbauer- und Zimmerermeister dürfen nur für „freistehende oder nur einseitig angebaute oder anbaubare Wohngebäude der GK 1 bis 3 mit nicht mehr als drei Wohnungen“ Bauvorlagen machen.
  - Abs. 4 Nr. 6: Holzbau-Absolventen, beschränkt auf Holzbauweise.
  - Sonst gilt Abs. 2: Architekt oder Listen-Ingenieur.
  - Firmen dürfen Entwurfsverfasser sein, wenn eine berechtigte Person leitet (Abs. 6).
- **Standsicherheit, Art. 62a** [V]:
  - GK 1–3: Ersteller nach Abs. 1.
  - **Keine Prüfung** bei Wohngebäuden GK 1/2 (Abs. 2 S. 3 Nr. 1).
  - GK 3: Kriterienkatalog nach Anlage 2 BauVorlV. Ist nur ein Kriterium nicht erfüllt, bescheinigt ein Prüfsachverständiger.
  - **GK 4/5: immer Prüfsachverständiger.**
  - Sonderbau: Bauaufsicht, Prüfingenieur oder Prüfamt.
  - Typenprüfung ersetzt die Prüfung (Abs. 2 S. 3 Nr. 2).
- **Kriterienkatalog** (BauVorlV Anlage 2) [V]. Für den Holzbau kritisch sind:
  - Nr. 4: „rechnerischer Nachweis der Gebäudeaussteifung … nicht erforderlich“
  - Nr. 6: keine „besonderen … Schwingungsuntersuchungen“
  - Nr. 8: keine „besonderen Bauarten wie … **Leimholzbau**“
  - Ein Holztafel-MFH der GK 3 mit Scheibennachweis, Schwingungsnachweis nach EC 5 und BSH/BSP erfüllt den Katalog daher oft nicht [U, Auslegung]. Eine Prüfung ist dann wahrscheinlich.
- **Brandschutz, Art. 62b** [V]:
  - Ersteller: bauvorlageberechtigt oder Listen-Brandschutzplaner.
  - Geprüft wird nur bei Sonderbau, Mittel-/Großgarage und **GK 5**.
  - Bei GK 4 bestätigt der Nachweisersteller die übereinstimmende Bauausführung mit der Anzeige der Nutzungsaufnahme (StMB-Merkblatt „Bautechnische Nachweise“ 11/2024 zu Art. 78 Abs. 2 S. 2 Nr. 3).
- **Schallschutz**: Nachweis nach BauVorlV § 12, keine Prüfung [V].
- **Abweichungen**: Art. 63 Abs. 1 S. 3 – keine Zulassung nötig, wenn ein Prüfsachverständiger bescheinigt [V]. Das ist wichtig für Gebäudetyp-e-Ansätze ab GK 4.

### 2.3 Brandschutz je Gebäudeklasse

**Bauteilanforderungen** [V, BayBO Art. 25, 27–29, 32, 33, 37]:

| Bauteil | GK 1 | GK 2 | GK 3 | GK 4 | GK 5 |
|---|---|---|---|---|---|
| tragende Wände, Stützen, Decken | – | fh | fh | hfh | fb |
| Keller: tragende Teile, Decken | fh | fh | fb | fb | fb |
| Trennwände zwischen NE (Art. 27) | – (Wohngeb.) | – (Wohngeb.) | wie Tragwerk, mind. fh | hfh | fb |
| Gebäudeabschlusswand (Art. 28) | Art. 27 entspr. (fh) | Art. 27 entspr. (fh) | hfh **oder** fh innen→außen / fb außen→innen | hfh + mech. | Brandwand, nichtbrennbar |
| Wände notwendiger Treppenräume | – | – | fh | hfh + mech. | Bauart Brandwand (nichtbrennbar, Art. 24 Abs. 2 S. 5) |
| tragende Teile notwendiger Treppen | – | – | nb oder fh | nb | fh + nb |
| Fahrschachtwände | – | – | fh | hfh | fb + nb |

fh = feuerhemmend, hfh = hochfeuerhemmend, fb = feuerbeständig, nb = nichtbrennbar.

- **Doppel- und Reihenhaus, bayerische Besonderheit** [V]:
  - Art. 28 Abs. 2 S. 2: Für GK 1/2 gilt die Brandwandpflicht der Nr. 1 nicht; stattdessen gilt Art. 27 entsprechend.
  - Die Abschlusswand an der Grenze muss damit die Feuerwiderstandsfähigkeit der Tragkonstruktion haben, mindestens feuerhemmend. In Holztafelbauweise ist das zweischalig gut lösbar.
  - Offen ist, ob die Detailregeln in Abs. 4–10 (Überdachführung, Abs. 7 „Bauteile mit brennbaren Baustoffen … nicht hinweggeführt“) über Abs. 11 auch für diese Art-27-Wand gelten [U]. Dasselbe gilt für Art. 30 Abs. 5 (Dachfenster ≥ 1,25 m, PV ≥ 0,50 m von der Wand).
  - **Das nicht aus MBO-Quellen übernehmen.**
- **HolzBauRL 2024-09** [V: DIBt-Mitteilung 05/2025, StMB-Rundschreiben zu BayTB 11/2025, Erläuterungen RLP 02/2026]:
  - Das Kapselkriterium K₂60 entfällt. Maßstab ist jetzt der Entzündungsschutz t_ch:
    - hochfeuerhemmend: t_ch ≥ 60 min, z. B. 2 × 15 mm GKF oder GF
    - abweichend feuerbeständig: t_ch ≥ 90 min, 2 × 18 mm
  - Reduzierte Bekleidung (t_ch 30) ist möglich bei NE bzw. Raumgruppen ≤ 200 m²; die Grenze sonst liegt bei 400 m².
  - Dämmstoffe in und auf den Bauteilen: **nichtbrennbar, Schmelzpunkt ≥ 1000 °C**, gefachfüllend. Ausnahme: Fußbodenaufbau.
  - Holztafelbau ist jetzt auch in GK 5 zulässig.
  - Brandwände und Treppenraumwände in GK 5 bleiben nichtbrennbar.
  - Holzfassaden in GK 4/5: horizontale Brandsperren geschossweise, Abstand ≤ 4 m, Lüftungsspalt ≤ 60 mm.
  - Bayern verzichtet auf eine Bauartgenehmigung auch außerhalb des Anwendungsbereichs, z. B. in GK 3, wenn nach den Anhängen 1–3 nachgewiesen wird (Verzicht nach Art. 15 Abs. 4 BayBO).
- **Rettungswege** [V]:
  - Je NE und Geschoss 2 Rettungswege (Art. 31). Der erste führt über eine notwendige Treppe, der zweite über eine weitere Treppe oder über Rettungsgeräte der Feuerwehr.
  - Liegt die Brüstung der Anleiterstelle **> 8 m** hoch, braucht die Feuerwehr ein Hubrettungsfahrzeug (Art. 31 Abs. 3), plus Zufahrt und Aufstellflächen (Art. 5 Abs. 1).
  - Rettungsfenster: lichte Öffnung ≥ 0,60 × 1,00 m, Brüstung ≤ 1,20 m. Im Dach ≤ 1 m von der Traufe (Art. 35 Abs. 4).
  - Notwendiger Treppenraum ab GK 3 (Art. 33 Abs. 1).
  - Wege zum Treppenraum ≤ 35 m.
  - Treppenraum: in jedem Geschoss Fenster mit ≥ 0,50 m² freiem Querschnitt oder oben eine Rauchabzugsöffnung ≥ 1 m². Bei h > 13 m ist die Öffnung oben Pflicht.
  - Bekleidungen im Treppenraum nichtbrennbar, Holzwände dort nichtbrennbar bekleidet (Abs. 5).
- **Rauchwarnmelder** [V]: in jeder Wohnung (Schlafräume, Kinderzimmer, Flure), ohne Delta nach Typ (Art. 46 Abs. 4).
- **Leitungen** [V]:
  - Art. 38 Abs. 1: Anforderungen an Durchführungen gelten nicht in GK 1/2 und nicht innerhalb von Wohnungen, wohl aber an Wohnungstrenndecken ab GK 3.
  - Bayern hat die Muster-Leitungsanlagen-Richtlinie als LAR (StMB, 04/2021) eingeführt.
  - Erleichterung für einzelne Leitungen: Mindestbauteildicke 60/70/80 mm für fh/hfh/fb.
- **Abfall** [V]: Abfallräume in Gebäuden der GK 3–5 nur mit Trennwänden und Decken in der Feuerwiderstandsfähigkeit der tragenden Wände und direkter Entleerung von außen (Art. 43).

### 2.4 Schallschutz

DIN 4109-1:2018-01, als Mindestanforderung eingeführt [V für die Werte; Einführung in BayTB V/U]:

| Bauteil | R′w | L′n,w |
|---|---|---|
| Wohnungstrenndecke (auch Treppen), Tab. 2 Z. 2 | ≥ 54 | ≤ 50; **≤ 53 bei Decken nach DIN 4109-33 (Holz)**, Fußnote b |
| Decken über Keller, Hausfluren, Treppenräumen | ≥ 52 | ≤ 50 |
| Decken unter Bad/WC | ≥ 54 | ≤ 53 |
| Treppenläufe und Podeste (MFH) | – | ≤ 53 |
| Balkone / Laubengänge | – | ≤ 58 / ≤ 53 |
| Wohnungstrennwand, Treppenraumwand | ≥ 53 | – |
| Aufzugsschachtwand an Aufenthaltsraum | ≥ 57 | – |
| Wohnungseingangstür zum Flur / direkt in Aufenthaltsraum | Rw ≥ 27 / ≥ 37 | – |
| **RH/DH, Tab. 3**: Haustrennwand, unterstes Geschoss | ≥ 59 | – |
| **RH/DH**: Haustrennwand, darüber | **≥ 62** | – |
| RH/DH: Decken / Bodenplatte / Treppen | – | ≤ 41 / ≤ 46 / ≤ 46 |

- Leicht austauschbare Beläge, auch schwimmendes Parkett, dürfen nicht angerechnet werden [V].
- **Erhöhter Schallschutz, DIN 4109-5:2020-08** [U, Sekundärquellen]:
  - Decke R′w ≥ 57 / L′n,w ≤ 45
  - Wand ≥ 56
  - Treppen ≤ 47
  - Haustrennwand ≥ 67
  - Er ist nicht bauaufsichtlich gefordert, aber vertraglich riskant: Die bayerische Gebäudetyp-e-Begleitforschung nennt Urteile, die den erhöhten Schallschutz de facto zur Erwartung machen.
- **Folge für den Holzbau**:
  - Haustrennwände von DH/RH zweischalig mit durchgehender Fuge, auch im Fundament und im Dach [U, Stand der Technik].
  - Trenndecken im MFH mit Katalogaufbau aus DIN 4109-33 oder mit Prüfzeugnis. Regnauer nennt eine eigene „Silence-Decke“, Werte liegen nicht vor.

### 2.5 Barrierefreiheit und Aufzug [V]

- **Art. 48 Abs. 1**, mehr als 2 Wohnungen:
  - Die Wohnungen **eines** Geschosses müssen barrierefrei erreichbar sein; die Pflicht darf auf mehrere Geschosse verteilt werden.
  - Mit Aufzugspflicht: **⅓** der Wohnungen.
  - In diesen Wohnungen barrierefrei: Wohn- und Schlafräume, WC, Bad, Küche und Waschmaschinenplatz.
  - Grenze: unverhältnismäßiger Mehraufwand, ausdrücklich auch wegen „des Einbaus eines sonst nicht erforderlichen Aufzugs“ (Abs. 4).
- **DIN 18040-2** ist eingeführt (BayTB Anlage A 4.2/3Bay):
  - Ausgenommen sind Abschnitte 4.3.6, 4.4 und 5.6 sowie **alle „R“-Anforderungen**. Rollstuhlgerecht ist also nicht bauordnungsrechtlich gefordert.
  - Ein Fenster je Wohnung mit Durchblick im Sitzen; eine Brüstung von 70 cm ist zulässig.
  - Eine Badewanne ist zulässig, wenn die Dusche später nachgerüstet werden kann.
- **Aufzug, Art. 37 Abs. 4**:
  - Pflicht erst bei h > 13 m. Bei Wohnnutzung fällt das praktisch mit GK 5 zusammen.
  - Mindestens ein Aufzug muss Rollstuhl, Trage und Lasten aufnehmen können (Kabine 1,10 × 2,10 m, Tür 0,90 m) und hält in allen Geschossen.
  - Wohnungseingangstüren an der Aufzugsstrecke haben eine lichte Breite ≥ 0,90 m (Art. 35 Abs. 2).
- Handläufe beidseitig bei > 2 nicht stufenlos erreichbaren Wohnungen (Art. 32 Abs. 6).
- **Förderung** [V]: WFB 2023 Nr. 12.4 verlangt bei geförderten Neubauten *alle* Wohnungen nach DIN 18040-2; die „R“-Anforderungen gelten nur für rollstuhlgerechte Wohnungen. Das ist strenger als die BayBO.

### 2.6 Weitere Pflichten im Mehrfamilienhaus

- **Kinderspielplatz** [V]: Die Pflicht steht **nicht mehr in Art. 7**; Art. 7 regelt heute die Begrünung. Die Pflicht besteht nur, wenn die Gemeinde eine Satzung nach Art. 81 Abs. 1 Nr. 3 erlassen hat, und nur für Gebäude mit **mehr als fünf Wohnungen**. Die Satzung kann eine Ablöse vorsehen.
- **Abstellräume** [V]: In GK 3–5 braucht jede Wohnung einen Abstellraum. Liegen nicht alle Wohnungen zu ebener Erde, kommen gut zugängliche Abstellräume für Kinderwagen, Fahrräder und Mobilitätshilfen dazu (Art. 46 Abs. 2).
- **Stellplätze und Fahrradplätze** [V]:
  - Nur mit Gemeindesatzung (Art. 47, Art. 81 Abs. 1 Nr. 4).
  - Die Zahl legt das Ministerium per Verordnung fest (GaStellV); eine Satzung darf weniger festlegen.
  - Die Regelmaschine braucht deshalb eine Satzungsdatenbank je Gemeinde, keine Pauschale.
- **Raumhöhe** [V]: Aufenthaltsräume ≥ 2,40 m, im Dachgeschoss ≥ 2,20 m über der halben Fläche. Das gilt **nicht** für Wohngebäude GK 1/2, wohl aber ab GK 3, also für das Holz-MFH (Art. 45 Abs. 1).
- **Abstandsflächen** [V]:
  - In Gemeinden > 250 000 Einwohnern gilt 1 H, wenn die Umgebung von GK 1–3 geprägt ist (Art. 6 Abs. 5a).
  - An der Grenze keine Abstandsfläche, wenn planungsrechtlich angebaut werden muss oder darf (Abs. 1 S. 4). Das ist der Regelfall für DH und RH.
- **Hausanschlussraum**: nach DIN 18012:2018 erforderlich bei **mehr als fünf NE**, bis dahin genügt eine Hausanschlusswand. Die Nische ist nur für nicht unterkellerte EFH zulässig [U: Normzitat über baunormenlexikon und EWE; eine Netzbetreiberschrift nennt „> 4 WE“, das entspricht der alten Fassung 2008].
- **Briefkästen, Trockenraum, Keller**: keine bauordnungsrechtliche Pflicht gefunden [U]. Das ist eine Frage des Ausstattungsstandards bzw. des Gebäudetyps E.

### 2.7 Flächen, Planungsrecht, Wohnungseigentum

- **WoFlV § 4** [V]:
  - lichte Höhe ≥ 2 m: voll angerechnet
  - 1–2 m: zur Hälfte
  - unbeheizte Wintergärten: zur Hälfte
  - Balkone, Loggien, Terrassen: „in der Regel“ zu einem Viertel, höchstens zur Hälfte
  - Nicht zur Wohnfläche gehören Keller, Abstellräume außerhalb der Wohnung, Heizungsräume und Garagen (§ 2 Abs. 3).
- **DIN 277:2021**: BGF, NRF, NUF über IfcSpace/Qto; nicht separat geprüft [U].
- **Doppel- und Reihenhaus, Planungsrecht** [V]:
  - Ein Doppelhaus verlangt, dass beide Hälften „in wechselseitig verträglicher und abgestimmter Weise“ aneinandergebaut sind (BVerwG 4 C 12.98). Das lässt sich „weder abstrakt-generell noch mathematisch-prozentual“ bestimmen (4 C 12.14).
  - Die Regelmaschine kann also nur **Indikatoren** liefern (Höhen- und Tiefenversatz, Dachform, Firstrichtung) und keine Entscheidung.
  - GRZ/GFZ gelten je Baugrundstück: bei Realteilung je Flurstück, bei WEG für das Gesamtgrundstück.
- **Wohnungseigentum** [V]:
  - § 3 Abs. 3 WEG: Sondereigentum „soll“ nur an abgeschlossenen Räumen entstehen. Stellplätze gelten als Räume, Freiflächen sind möglich, wenn sie mit Maßangaben bestimmt sind.
  - § 7 Abs. 4: Der Eintragungsbewilligung liegen bei:
    - ein von der Baubehörde gesiegelter **Aufteilungsplan**; alle Teile einer Einheit tragen die gleiche Nummer
    - die **Abgeschlossenheitsbescheinigung**
  - Maßgeblich ist die **AVA vom 12.07.2021** (BAnz AT B2). Sie hat die AVV von 1974 abgelöst:
    - „ungeachtet bauordnungsrechtlicher Vorschriften“ zu erteilen
    - abgeschlossen heißt „baulich vollkommen abgetrennt“ und mit eigenem abschließbarem Zugang, nicht über anderes Sondereigentum
    - elektronisch mit qualifizierter Signatur möglich
  - gesetze-bayern.de führt noch die Bekanntmachung von 1974 (mit Wohnungstrennwand-Bezug und WC in der Wohnung). **Nicht mehr als Prüfmaßstab verwenden.**
  - Aus IFC ableitbar: Einheiten (IfcZone), Nummerierung, Zugänge (Graph über IfcDoor/IfcSpace), Stellplätze (IfcSpace PARKING), Freiflächen (IfcSpace EXTERNAL mit Maßen). Sondernutzungsrechte sind schuldrechtlich (Gemeinschaftsordnung). Das Modell kann sie nur als Attribut tragen, nicht prüfen.

### 2.8 Energie und TGA

- **Trinkwasser, TrinkwV § 31** [V]:
  - Legionellen-Untersuchungspflicht, wenn *alle* drei zutreffen:
    - Speicher bzw. zentraler Durchfluss-Trinkwassererwärmer > 400 l oder > 3 l in einer Leitung ohne Zirkulation
    - Duschen vorhanden
    - **kein EFH/ZFH**
  - Zusätzlich muss die Abgabe gewerblich sein; Vermietung gilt als gewerblich (§ 2 Nr. 8).
  - Intervall: alle 3 Jahre, erste Untersuchung 3–12 Monate nach Inbetriebnahme.
  - Dezentrale Wohnungsstationen unter 3 l vermeiden die Pflicht [U, Planungsfolgerung].
- **HeizkostenV** [V]:
  - Verbrauchserfassung je Nutzeinheit.
  - Neugeräte seit 01.12.2021 fernablesbar, seit 01.12.2022 smart-meter-gateway-fähig und interoperabel.
  - Altgeräte bis 31.12.2026 nachrüsten.
  - Vorrangausnahme bei ≤ 2 Wohnungen, von denen der Vermieter eine bewohnt (§ 2).
- **PV und Messkonzept** [V]:
  - Mieterstrom (EnWG § 42a): Preis ≤ 90 % des Grundversorgungstarifs, nicht Teil des Mietvertrags.
  - Alternative ist die **gemeinschaftliche Gebäudeversorgung** (§ 42b) ohne Vollversorgungspflicht, mit viertelstündlicher Messung.
  - Die Regelmaschine braucht ein Messkonzept-Attribut je Gebäude, nicht je Wohnung.
- **Solarpflicht** [V]:
  - Bayern: für Wohngebäude nur eine **Soll**-Vorschrift (Art. 44a Abs. 4). Für Nichtwohngebäude eine Pflicht (Abs. 2); das betrifft den Gewerbeteil gemischter Gebäude [U].
  - EPBD 2024/1275 Art. 10: neue Wohngebäude **ab 2030**; Umsetzungsfrist 29.05.2026.
  - Nach BBSR hat der Bundestag das GModG-Änderungsgesetz am 10.07.2026 beschlossen. Ob es die Wohngebäude-Solarpflicht schon konkretisiert, habe ich nicht geprüft [U].
- **Energiebilanz** [V]:
  - GModG § 106: Nichtwohnteile eines Wohngebäudes werden getrennt behandelt.
  - § 3 Abs. 1 Nr. 6 definiert „einseitig angebautes Wohngebäude“ über ≥ 80 % Anbaufläche; das braucht man für DHH und RH-Ende.
  - § 104: Für kleine Gebäude und Raumzellen genügen die Bauteil-U-Werte; relevant für Tiny House und Modul.

### 2.9 Neue Rechtsentwicklungen

- **Gebäudetyp E, Bund**:
  - Entwurf am 07.07.2026 als „fertig“ vorgestellt.
  - Stand 15.–21.09.2026: noch in der Frühkoordinierung zwischen den Ressorts, **kein Kabinettsbeschluss** (Handelsblatt, MeisCon) [V/U, Presse].
  - Ziel nach den Eckpunkten vom 20.11.2025: ein Gebäudetyp-E-*Vertrag*. Die Abweichung von den anerkannten Regeln der Technik soll kein Mangel sein, mit Aufklärung in Textform gegenüber Verbrauchern.
  - Der Entwurf von 2024 (BT-Drs. 20/13959) ist verfallen.
  - Folge: Profile brauchen einen Schalter „vertraglich vereinbarter Standard“ für Komfortnormen, nie für BayBO-Mindestanforderungen.
- **Bayern** [V]:
  - Rechtsgrundlage ist Art. 63 (Abweichungen, auch „zur Erprobung neuer Bau- und Wohnformen“).
  - 19 Pilotprojekte seit 12/2023. Das erste ist fertig („Haus fast ohne Heizung“, Ingolstadt, 15 WE, etwa 15 % unter den üblichen Kosten).
  - „Das große kleine Haus“ (München): Holzbau unter der Hochhausgrenze, reduzierter Schallschutz, HolzBauRL vorab angewendet, über 11 % Einsparung.
  - Die zweite Runde ab 09/2026 betrifft Bildungsbauten.
- **Typengenehmigung Art. 73a** [V]:
  - Die oberste Bauaufsichtsbehörde (StMB) erteilt sie, auch für ein „System aus Bauteilen“ mit festgelegter Veränderbarkeit.
  - Sie gilt als bautechnischer Nachweis für Standsicherheit, Brand- und Schallschutz, soweit sie diese regelt.
  - Typengenehmigungen anderer Länder gelten in Bayern (Abs. 4).
  - Sie ersetzt nicht das Genehmigungsverfahren (Abs. 5).
  - Gestaltungssatzungen gelten nicht (Abs. 6).
  - Muster ist MBO § 72a (BMK 2019); die BMK bekräftigte 09/2024 den „einheitlichen Rahmen“.
- **Wohnraumförderung** [V]:
  - WFB 2023 gilt bis 31.12.2026.
  - Nr. 12.2 nennt Wohnflächen-Obergrenzen: 1 Person 40/50 m², 2 Personen 55/65 m², 3–4 Personen 75 m², 4 Personen 90 m², je weitere Person + 15 m², rollstuhlgerecht + 15 m²; Mindestens 35 m².
  - 2026 gibt es EOF-orientierte Pakete, ab 2027 ein Jahresbauprogramm mit neuer Richtlinie [U].

### 2.10 Typologien und Referenzen

- **IWU / TABULA** [V]: Größenklassen EFH, RH, MFH, GMH und HH:
  - EFH: freistehende Ein- und Zweifamilienhäuser
  - RH: Doppelhaushälfte und Reihenhaus
  - MFH: 3–12 Wohnungen
  - GMH: ≥ 13 Wohnungen [U beim genauen Grenzwert]
  - Das eignet sich als Kategorie für Kosten- und Energie-Benchmarks, nicht für Rechtsregeln.
- **Spänner**: Zwei- und Dreispänner (Wohnungen je Treppenhaus und Geschoss) sind Grundrissmuster ohne eigene Rechtsfolge. Relevant ist nur, ob die Wege zum Treppenraum ≤ 35 m bleiben und die Anleiterbarkeit gesichert ist [U].
- **Prinz-Eugen-Park, München** [V]:
  - 566 Wohnungen, 8 Projekte, bis zu 7 Geschosse.
  - Vom Hybridbau bis zum Brettsperrholz mit Aufzugsschacht.
  - Viergeschossige Stadthäuser in GK 4, Kleinhäuser bis GK 3.
  - Wohnungstrennwand zweischalig aus Brettsperrholz.
  - Quelle: Informationsdienst Holz 2020, DBU-Bericht Q-PEP.
- **Regnauer Objektbau** [V, Firmenseiten]:
  - MFH Stephanskirchen: 16 WE, 3 Geschosse, Tiefgarage, 2023
  - Stadthäuser Uttenreuth: 4 Häuser, eines mit 2 Wohnungen
  - Zeiler, Regensburg: 4-geschossiges Wohn- und Geschäftshaus mit 14 Wohnungen, 2010
  - „Mehrparteienhaus“ Obermenzing: 3 WE, genau an der Grenze von Art. 61 Abs. 3

---

## 3. Folgen für die Regelmaschine (Profile)

1. **Merkmale statt Typ.** Das Profil ist ein Vektor, den die Maschine deterministisch aus dem IFC berechnet:
   - `anbau` ∈ {freistehend, einseitig, beidseitig}
   - `n_WE`, `n_NE_sonst` mit Nutzungsart und Fläche
   - `h_Art2` = OKFF des obersten *möglichen* Aufenthaltsgeschosses minus mittleres Gelände
   - `BGF_NE` oberirdisch je NE
   - `keller` (Art. 2 Abs. 7)
   - `eigentum` ∈ {allein, Realteilung, WEG}
   - `gemeinde` (Satzungen, > 250 000 Einwohner)
   - `förderung` (WFB)
   - `sonderbau_flags`

   Der vom Kunden gewählte „Haustyp“ ist nur der Startwert der Konfiguration.
2. **Abgeleitete Schalter.** Jeder Schalter ist eine Regel mit Quelle:
   - `GK`
   - `bauvorlage_rolle`: Abs. 3 oder Abs. 2
   - `prüfung_statik` ∈ {keine, Kriterienkatalog, PSV, Behörde}
   - `prüfung_brand`
   - `brand_stufe`: die Tabelle aus 2.3
   - `schall_tabelle` ∈ {keine, Tab2, Tab3}
   - `bf_pflicht`: n_WE > 2
   - `aufzug`: h > 13
   - `raumhöhe_240`: GK ≥ 3
   - `abstellraum`: GK ≥ 3
   - `spielplatz`: Satzung ∧ n_WE > 5
   - `trinkwv31`
   - `heizkostenv`
   - `hausanschlussraum`: NE > 5
   - `holzbaurl`: GK ∈ {4, 5}
   - `hubrettung`: Brüstung > 8 m
3. **Schwellen-Warnungen.** Bei |h − 7 m|, |h − 13 m| oder |h − 22 m| < 0,5 m, bei NE-Flächen nahe 200 bzw. 400 m² und bei n_WE ∈ {2, 3, 5} warnt die Maschine. Die Warnung nennt die Folgen („+1 Wohnung → Architekt erforderlich, barrierefreie Erreichbarkeit“). Die Folgen springen und sind teuer; das muss der Konfigurator vor der Entscheidung zeigen.
4. **Katalog je Profil.** Bauteilaufbauten tragen Eigenschaften (Feuerwiderstand, Kapselung/t_ch, Dämmstoff-Brennbarkeit, R′w/L′n,w nach DIN 4109-33). Die Regelmaschine filtert den Regnauer-Katalog nach dem Profil. In GK 4/5 fallen damit z. B. alle Aufbauten mit Holzfaser- oder Zellulosedämmung weg (HolzBauRL 3.3).
5. **Holzbau-GK 4/5 als eigenes Modul** mit Regelwerk-Version (HolzBauRL 2024-09 in BayTB 11/2025, Übergang nach Einleitungsdatum des Verfahrens). So bleibt der EFH-Kern schlank.
6. **Nicht deterministisch → Freigabe-Knoten**:
   - Doppelhaus-Eigenschaft
   - „Wohngebäude“ bei gemischter Nutzung
   - Abgrenzung der Nutzungseinheiten (z. B. Einliegerwohnung ohne eigenen Zugang)
   - Unverhältnismäßigkeit bei Art. 48 Abs. 4
   - Abweichungen nach Art. 63
   - Gebäudetyp-E-Vereinbarungen
7. **IDS bleibt Eigenschaftsprüfung** („jede tragende Wand hat FireRating aus der Liste …“), abhängig vom Profil. Beziehungsregeln (Rettungsweglänge, Anleiterhöhe, Abgeschlossenheit, Trennwand zwischen zwei Zonen) gehören in die Regelmaschine, nicht in IDS.

## 4. Folgen für Rollen und Freigaben

| Freigabe | EFH, ZFH, DHH, RH-Ende, ≤ 3 WE freistehend | RH-Mitte, MFH ≥ 4 WE, gemischt | GK 4 | GK 5 / Sonderbau |
|---|---|---|---|---|
| Entwurfsverfasser (Bauvorlagen) | Zimmerermeister/Techniker/Ingenieur (Abs. 3) möglich | **Architekt oder Listen-Ingenieur** (Abs. 2) | Abs. 2 | Abs. 2 |
| Standsicherheit erstellen | Art. 62a Abs. 1 (Zimmerermeister nur mit Zusatzqualifikation) | Abs. 1, Liste | Tragwerksplaner | Tragwerksplaner |
| Standsicherheit prüfen | keine (GK 1/2 Wohngebäude); GK 3 Kriterienkatalog | Kriterienkatalog | **PSV**, vom Bauherrn beauftragt | PSV bzw. Prüfingenieur/Behörde |
| Brandschutz erstellen | Entwurfsverfasser | Entwurfsverfasser oder Brandschutzplaner | dto. + **Bestätigung der Bauausführung** | Brandschutzkonzept |
| Brandschutz prüfen | – | – | – | **PSV Brandschutz** oder Bauaufsicht, mit Bauüberwachung |
| Schallschutz | – (bei 2 WE: Nachweis Tab. 2) | Nachweis § 12 BauVorlV | dto. | dto. |
| WEG | – | Aufteilungsplan → Bauaufsicht (AVA 2021) | dto. | dto. |

- Die Plattform muss jeder Person ihre **Berechtigungsreichweite** zuordnen: Rolle × Profil. Den Export „Bauvorlagen einreichen“ sperrt sie, wenn der benannte Entwurfsverfasser für das Profil nicht berechtigt ist.
- Neue externe Rollen: Prüfsachverständiger Standsicherheit, Prüfsachverständiger Brandschutz, Brandschutzplaner (Liste nach Art. 62 Abs. 3), Notar/Aufteiler (WEG), Messstellenbetreiber (PV-Konzept).
- Den Prüfsachverständigen beauftragt der **Bauherr**. Bei einem Kunden-Konfigurator muss der Vertrag das sichtbar machen (Kosten, Termine: Bescheinigung I mit der Baubeginnsanzeige, II mit der Nutzungsaufnahme).

## 5. IFC-Abbildung (geprüft mit IfcOpenShell 0.8.5 gegen IFC4X3_ADD2)

Ein Testmodell hat den Validator einschließlich der EXPRESS-Regeln mit **0 Befunden** durchlaufen [V]. Es enthielt:

- 1 IfcSite mit 2 Unter-Sites (Flurstücke)
- 4 IfcBuilding
- IfcZone „WE 01“ über IfcSpace
- IfcSpatialZone OCCUPANCY
- Referenz von Zone und Raumzone ins Geschoss über IfcRelReferencedInSpatialStructure
- Haustrennwand mit Pset_WallCommon
- Pset_PropertyAgreement an IfcSpace

| Rechtsbegriff | IFC-Abbildung | Hinweis |
|---|---|---|
| Baugrundstück / Flurstück | IfcSite, Flurstücke als aggregierte Unter-IfcSite | Realteilung beim RH; Pset_SiteCommon (BuildableArea, SiteCoverageRatio, FloorAreaRatio) für GRZ/GFZ |
| Gebäude i. S. d. BayBO | **ein IfcBuilding je DHH/RH-Einheit** | GK je IfcBuilding. `IfcBuilding` hat in 4X3 ADD2 **kein PredefinedType** (kein IfcBuildingTypeEnum). Typ daher in `ObjectType` bzw. bSDD-Klassifikation |
| GK, Geschosszahl | Pset_BuildingCommon.FireProtectionClass [U, Nutzung], NumberOfStoreys, OccupancyType | h nach Art. 2 aus dem Geschoss mit Aufenthaltsraum-Möglichkeit + DGM; eigene Property für h und Mittelgelände |
| Nutzungseinheit / Wohnung | **IfcZone** (`ObjectType`="Wohnung"/"Gewerbe") über IfcRelAssignsToGroup | Pset_ZoneCommon: GrossPlannedArea, NetPlannedArea, HandicapAccessible, PubliclyAccessible. Maisonette unproblematisch |
| Brand- und Rauchabschnitt | IfcSpatialZone FIRESAFETY | Pset_SpatialZoneCommon hat nur Reference und IsExternal; Anforderungen in eigenem Pset |
| Stellplatz / Freifläche (Sondereigentum) | IfcSpace PARKING / EXTERNAL + Qto_SpaceBaseQuantities | Pset_PropertyAgreement (AgreementType ASSIGNMENT/LEASE/TENANT) gilt nur für IfcSpatialStructureElement, also IfcSpace, nicht IfcZone |
| Wohnfläche WoFlV | IfcSpace + eigenes Qto (Anrechnungsfaktor 1 / 0,5 / 0,25) | nicht nativ in IFC |
| Trennwand, Abschlusswand | IfcWall + Pset_WallCommon: FireRating (IfcLabel), AcousticRating (IfcLabel), **Compartmentation** (IfcBoolean), Combustible, LoadBearing | Labels frei → per IDS auf Vokabular beschränken („REI 30“, „EI 60-M“ …). Rolle (Wohnungstrennwand, Gebäudeabschlusswand) in eigenem Pset |
| Trenndecke | IfcSlab + Pset_SlabCommon (dieselben Properties) | L′n,w getrennt von R′w führen |
| Türen | Pset_DoorCommon: FireRating, SmokeStop, SelfClosing, AcousticRating | Rw 27/37 dB, T30-RS |
| Treppe | Pset_StairCommon: FireRating, FireExit, HandicapAccessible | nichtbrennbar über Material |

## 6. Korrekturen und Warnungen zum bisherigen Konzept (EFH, GK 1–3)

1. **„GK 1–3 ≤ 3 WE“ reicht für den Zimmerermeister nicht.** Das Gebäude muss zusätzlich freistehend oder nur einseitig angebaut sein und ein Wohngebäude sein. Reihenmittelhaus und Wohn-/Geschäftshaus sind ausgeschlossen (zu korrigieren in 00-zielbild.md, 07-recht-rollen.md).
2. **GK 3 ist nicht „EFH-nah“.** Schon ein großes EFH (> 400 m²) oder ein 3-WE-Haus bringt feuerhemmende Bauteile, einen notwendigen Treppenraum, 2,40 m Raumhöhe, Abstellräume, den Kriterienkatalog und oft einen PSV wegen Leimholz und Aussteifung [U].
3. **Die Einliegerwohnung ist eine zweite Nutzungseinheit.** Sie bringt Schall nach Tab. 2, zwei Rettungswege je Wohnung, Rauchwarnmelder, die HeizkostenV und ggf. einen Stellplatz nach Satzung.
4. **Höhe misst sich am *möglichen* Aufenthaltsraum.** Ein „nicht ausgebauter“, aber ausbaufähiger Dachraum kann GK 4 auslösen.
5. **Kinderspielplatz**: Art. 7 Abs. 3 existiert nicht mehr. Maßgeblich ist Art. 81 Abs. 1 Nr. 3 (Satzung, > 5 WE).
6. **Abgeschlossenheit**: nach AVA 2021 prüfen, nicht nach der AVV 1974.
7. **HolzBauRL**: Die Aussage „für GK 1/2 nicht relevant“ stimmt. Die RL gilt aber auch nicht für GK 3; dort bleibt der Nachweis über DIN 4102-4 / EN 1995-1-2 mit dem bayerischen Verzicht auf Bauartgenehmigungen. In GK 4/5 kollidieren Holzfaser- und Zellulosedämmung mit der Pflicht zu nichtbrennbaren Dämmstoffen.
8. **Bayerische Abschlusswand-Regel** (Art. 28 Abs. 2 S. 2) weicht von der MBO ab. MBO-basierte Regelsätze wie MBO2BIM also nicht ungeprüft übernehmen.
9. **DIN 18012**: Die Schwelle liegt bei > 5 NE (Fassung 2018), nicht bei > 4 [U].
10. **Doppelhaus / Hausgruppe** ist planungsrechtlich keine Rechenregel. Ein Automatismus „GRZ ok → zulässig“ ist falsch.

## 7. Offene Fragen an Regnauer (Objektbau)

1. Welche Typen baut der Objektbau heute, mit welcher maximalen GK: DH, RH, MFH GK 3/4/5, Wohn- und Geschäftshaus? Wer ist Entwurfsverfasser (eigene Architekten, Listen-Ingenieure, externe Partner)?
2. Welche Wand- und Deckenaufbauten sind für **GK 4** (hfh, t_ch 60, nichtbrennbare Dämmung) und **GK 5** freigegeben? Welche Dämmung hat die „Vitalwand“, und ist sie in GK 4 zulässig?
3. Welche Werte erreicht die **Silence-Decke** (R′w, L′n,w)? Ist sie DIN 4109-33 zuzuordnen oder gibt es ein Prüfzeugnis? Wird der erhöhte Schallschutz (4109-5) vertraglich angeboten?
4. Wie ist die **Haustrennwand** für DH und RH aufgebaut (zweischalig, Fuge in Bodenplatte und Dach, Brandschutz nach Art. 28 Abs. 2 S. 2)? Gibt es Messwerte ≥ 62 dB?
5. Treppenhaus und Aufzugsschacht: Holz (GK 4) oder Stahlbetonkern (GK 5)? Wer liefert den Kern?
6. Mit welchen Prüfsachverständigen (Standsicherheit, Brandschutz) arbeitet Regnauer, und wie lang sind die Vorläufe? Wird bei GK 3 der Kriterienkatalog regelmäßig verfehlt (BSH, Aussteifung)?
7. Gibt es Interesse an einer **Typengenehmigung** (Art. 73a, System mit festgelegter Veränderbarkeit), z. B. für Stadthaus- und RH-Serien?
8. TGA im MFH: zentral mit Zirkulation (TrinkwV § 31) oder Wohnungsstationen? Lüftung je Wohnung? Messkonzept PV (§ 42a oder § 42b EnWG)?
9. Liefert Regnauer Aufteilungspläne (WEG) mit, und wer beantragt die Abgeschlossenheitsbescheinigung?
10. Welche Projekte (Stephanskirchen, Uttenreuth, Zeiler) dürfen anonymisiert als Testfälle in IFC nachmodelliert werden?

## Quellen (Auswahl)

- BayBO Art. 2, 5, 6, 7, 24–38, 43–48, 61–63, 73a, 81 (gilt ab 01.05.2026): gesetze-bayern.de/Content/Document/BayBO-{Nr}
- BauVorlV mit Anlage 2 (Kriterienkatalog): gesetze-bayern.de/Content/Document/BayBauVorlV2008/true
- StMB, „Bautechnische Nachweise“ (25.11.2024); Rundschreiben „Verzicht Bauartgenehmigung HolzBauRL 2024-09“; BayTB 11/2025 (BayMBl. 2025 Nr. 480); BayTB-Anlage A 4.2/3Bay (DIN 18040-2)
- MHolzBauRL 2024-09: DIBt-Meldung 13.05.2025; Text bau.bremen.de; Erläuterungen RLP (16.02.2026); Kampmeier (FNR 2026)
- DIN 4109-1:2018-01 Tab. 2/3 (Abdruck MBl. 2020, umwelt-online.de); DIN 4109-5 (gn-bauphysik 2020, Kellerer)
- WEG § 3, § 7; AVA 2021 (BAnz AT 12.07.2021 B2); WoFlV §§ 2, 4; TrinkwV §§ 2, 31; HeizkostenV §§ 2, 5; EnWG §§ 42a, 42b; GModG §§ 3, 104, 106 (gesetze-im-internet.de)
- BVerwG 4 C 12.98 (24.02.2000), 4 C 12.14 (19.03.2015)
- EPBD (EU) 2024/1275; BBSR GEG-Infoportal EPBD
- Gebäudetyp E: BT-Drs. 20/13959; Handelsblatt 15.09.2026; StMB-Pressemitteilungen 2025/112, 2026/23b, 2026/107; iTUBS-Kurzbericht Pilotphase I
- WFB 2023 Nr. 12 (gesetze-bayern.de); StMB-Förderübersicht 2026
- IWU, Deutsche Wohngebäudetypologie (2015); LH München / Informationsdienst Holz, Prinz-Eugen-Park; regnauer.de/objektbau

# 14b Baustellenlogistik und Montageplanung

Status: Entwurf v0.1 (27.09.2026). Befunde zu Regelwerk, Verfahren und Genehmigungen der Montage; keine Einsatzplanung und keine Hubfreigabe. Grundlage sind Recherche 19 (`../recherche/19-baustellenlogistik-kranplanung.md`), das Beispiel B18 (`beispiele/b18_kranplanung.py`, 15 Tests grün am 27.09.2026) und die Abschnitte 3.2.7 und 8.4. **Alle Kran-, Fahrzeug- und Kostenwerte in B18 sind Beispielwerte** in der Größenordnung öffentlicher Datenblätter, keine Herstellerdaten.

## 14b.0 Einordnung und Vorgehen

Ein Holzfertighaus wird in ein bis zwei Tagen montiert; Regnauer gibt an, das Haus sei in dieser Zeit regendicht, und montiert mit eigenen Kolonnen [V, Recherche 19]. Zwischen unterschriebener Ausstattungsfestlegung und Montagebeginn liegen mindestens zwölf Wochen [@regnauerBLB2024]; in dieser Zeit müssen Kran, Stellplatz, Transporte und Genehmigungen feststehen. Dieses Kapitel begründet die Rückwärtsterminierung aus Beispiel 3.5.

Für ein Entwurfssystem ist die Montageplanung aus zwei Gründen Gegenstand und nicht bloß Nachlauf:

1. **Sie hängt am Entwurf.** Die Elementierung bestimmt Gewichte, Maße und Ladungen; die Lage des Hauses auf dem Grundstück bestimmt Kranstellplatz, Radien und Genehmigungen. Wer die Garage an die Einfahrt rückt, verlegt den Kran unter Umständen auf die Straße.
2. **Sie ist regelbasiert.** Traglast nach Radius, Bodenpressung, Abstände zu Freileitung und Baugrube, Fahrzeugmaße und Genehmigungsfristen sind Regeln mit Kennwert und Quelle. Sie werden wie in Kapitel 9 formalisiert.

Die Grenze ist ebenso klar: Die App liefert eine **Vorauswahl** mit konservativen Hüllkurven. Die Hubfreigabe bleibt beim Kranunternehmen, das mit der Software des Herstellers und dem eigenen Einsatzplan arbeitet [V, Recherche 19]. Die Arbeitsvorbereitung ist damit eine R3-Frage im Sinne von Kapitel 4.

## 14b.1 Elementgewichte aus dem Modell

Das Gewicht jedes Elements ist Volumen × Rohdichte, summiert über alle Teile. Diese Rechnung setzt die doppelte Darstellung aus Kapitel 8 voraus: Das Einzelteilmodell trägt das Volumen jedes Stabs, jeder Platte und jeder Dämmlage, das Material trägt `Pset_MaterialCommon.MassDensity` (E8.11). B18 liest das Wandelement aus B1 und rechnet [V, `ausgabe/b18_kranplanung.json`]:

> **Beispiel 14b.1 (Gewicht des Wandelements B1).** Außenwand 4,80 × 2,75 m, 13,2 m² brutto, Dicke 0,288 m.
>
> | Material | Teile | Volumen [m³] | ρ [kg/m³] | Masse [kg] |
> |---|---:|---:|---:|---:|
> | KVH C24 | 18 | 0,515 | 420 | 216,3 |
> | Holzfaserdämmplatte | 2 | 0,687 | 180 | 123,7 |
> | Gipsplatte GKF | 4 | 0,143 | 800 | 114,6 |
> | OSB/3 | 4 | 0,172 | 600 | 103,1 |
> | Holzfaser-Dämmmatte | 12 | 1,776 | 50 | 88,8 |
> | Dampfbremse | 1 | 0,0023 | 900 (Annahme) | 2,1 |
> | Schrauben | 176 | 0,00011 | 7 850 | 0,9 |
> | **Summe** | | | | **649,4 kg = 49,2 kg/m²** |
>
> Mit Putz (20 kg/m²) und Fensteranteil (5,25 kg/m²) wird die Außenwand zu 74,4 kg/m²; beide Zuschläge sind Annahmen. Die Decke (Balken 60/220, GKF, OSB, Holzfaser) wiegt ohne Estrich 36,6 kg/m², das Dach (Sparren 80/240, Holzfaser, Holzfaserdämmplatte 60 mm, OSB) ohne Eindeckung 43,4 kg/m².

Für das Beispielhaus von B18, 12 × 10 m, eineinhalbgeschossig mit Satteldach 35°, ergeben sich 26 Elemente mit zusammen 22,99 t:

| Gruppe | Anzahl | Maße | Masse je Element |
|---|---:|---|---:|
| EG-Außenwand | 8 | 6,0 bzw. 5,0 × 2,75 m | 1,228 bzw. 1,024 t |
| Decke | 6 | 10,0 × 2,0 m | 0,732 t |
| DG-Giebel (Dreieck) | 4 | 5,0 × 3,50 m | 0,652 t |
| Dach | 8 | 6,71 × 3,0 m | 0,873 t |

Im IFC steht das Gewicht als `GrossWeight` in `Qto_WallBaseQuantities` bzw. `Qto_SlabBaseQuantities`. `Qto_RoofBaseQuantities` kennt kein Gewicht; Dachelemente sind deshalb `IfcSlab` ROOF (E14.5). B1 schreibt das Gewicht noch nicht; ANF-03-15 und ANF-08-12 verlangen es ab Reifegrad A [V, Recherche 19].

**E14b.1 – Das Hubgewicht ist eine abgeleitete Größe mit Zuschlägen, die als Annahmen gekennzeichnet sind.** *Entscheidung.* Das Elementgewicht wird aus dem Einzelteilmodell berechnet. Zuschläge für Bauteile, die im Einzelteilmodell noch fehlen (Putz, Fenster, Installation), sind Parameter mit Status [U] und Datenlieferung (DAT-14b-01). Die Hublast ist Elementgewicht plus Anschlagmittel plus Hakenflasche. *Begründung.* Nur so ist jede Tonne auf eine Quelle zurückführbar; reale Gewichte liefert das Werk. *Beleg.* B18: 649,4 kg ± 0,5 kg (`test_b1_gewicht`) [V].

## 14b.2 Kranwahl

### 14b.2.1 Krantypen

In Frage kommen Autokran, Mobilbaukran, Schnelleinsatzkran und, selten wirtschaftlich, der Turmdrehkran. Recherche 19 hat öffentliche Kenndaten erhoben:

| Modell | Typ | Kenndaten | Status |
|---|---|---|---|
| Liebherr LTM 1030-2.1 | Autokran, 2 Achsen | 35 t bei 3 m; Teleskop 9,2–30 m, Radius bis 40 m; ca. 2,4–2,5 t bei 20 m (5,5 t Ballast, 360°) | [V]; Tabellenwerte aus altem Blatt [U] |
| Liebherr LTM 1060-3.1 | Autokran, 3 Achsen | 60 t bei 2,1 m; Teleskop 10,3–48 m; ca. 4,9–5,7 t bei 20 m; 36 t bei 12 t Achslast mit reduziertem Ballast | [V]; Zuordnung Stützkräfte [U] |
| Liebherr LTM 1090-4.2 | Autokran, 4 Achsen | 90 t bei 3 m; Teleskop 11,4–60 m | [V] |
| Liebherr MK 88-4.1 | Mobilbaukran | 8 t; Ausladung 45 m mit 1,85–2,2 t an der Spitze; Traglasten gelten bis 14,1 m/s; Einsatzgewicht 48 t | [V] |
| Liebherr 81 K.1 | Schnelleinsatzkran | 6 t; Ausladung 48 m mit 1,35 t an der Spitze; Hakenhöhen 17,4–40,4 m | [V] |

Die Traglasttabellen liegen als PDF vor, gegliedert nach Auslegerlänge, Radius, Ballast, Abstützbasis und Schwenkbereich, netto oder mit Hakenflasche. Stützkräfte, Bodenpressung und Windwerte eines konkreten Hubs rechnen nur die Einsatzplaner der Hersteller (LICCON, Crane Planner 2.0 mit IFC-Import in der Pro-Version); eine offene Schnittstelle fehlt [U].

### 14b.2.2 Traglast und Lastmoment

Die Traglast fällt mit dem Radius, weil das Kippmoment aus Last und Radius und die Tragfähigkeit von Ausleger und Abstützung begrenzt sind [V, Liebherr/DGUV in Recherche 19]. Für jede Hubbewegung ist deshalb der größte Radius maßgebend, entweder am Aufnahmepunkt auf dem LKW oder am Absetzpunkt im Haus. B18 prüft je Element:

$$\text{Hublast} = m_e + m_\text{Anschlag} + m_\text{Flasche} \le \eta_\max \cdot T_K(r_\max)$$

mit der Auslastungsgrenze η_max = 0,8 als Firmenparameter [U, Annahme B18], dem Anschlagmittel mit pauschal 0,30 t (Traverse und Hebebänder) und der Hakenflasche des Krans. Die Traglastkurve T_K(r) interpoliert B18 stückweise linear zwischen Stützpunkten. Für echte Herstellertabellen ist das nicht zulässig: Zwischen zwei Radien gilt nach üblicher Praxis der Wert des nächstgrößeren Radius [U]. Das Schema `kran-traglast.schema.json` führt deshalb die Interpolationsregel als Pflichtfeld.

### 14b.2.3 Abstützung und Bodenpressung

Die Bodenpressung unter einer Stützplatte ist nach DGUV Information 208-059

$$p = \frac{F_\max}{A} \le p_\text{zul},$$

mit der **maximalen** Stützkraft, solange kein Einsatzplaner eine kleinere liefert. Das Beispiel der DGUV lautet 120 kN auf 0,035 m² = 3 430 kN/m²; eine Platte von 0,6 m² (80 × 80 cm) bringt die Pressung auf ein zulässiges Maß [V, Recherche 19]. Liebherr rechnet mit 80 % der Tellerfläche, weil der Randbereich nicht trägt, etwa 1 109 kN auf 0,6 × 0,6 m → 3 851 kN/m² [V]. Die zulässigen Pressungen stammen aus Tabellen der DGUV nach DIN 1054:1976-11:

| Untergrund | p_zul [kN/m²] |
|---|---:|
| angeschüttet, nicht verdichtet | 0–100 |
| nichtbindig, fest gelagert | 150–200 |
| bindig weich / steif / halbfest / fest | 40 / 100 / 200 / 300 |
| Wiese / Asphalt / Schotter verdichtet / Kies fest | 100 / 200 / 250 / 400 |
| Fels | 1 500–3 000 |

Diese Werte sind historisch und kein Baugrundgutachten; frisch verfüllte Arbeitsräume und Leitungsgräben (Kapitel 14a) tragen weit weniger [V Tabelle, Warnung Recherche 19]. Der Einsatzplaner liefert oft deutlich kleinere Stützkräfte als F_max, im Liebherr-Beispiel 700 statt 1 109 kN. B18 überschätzt deshalb die Plattengröße, und das ist gewollt.

### 14b.2.4 Wind je Hub

Der Wind ist bei Holztafeln die versteckte Grenze. DIN EN 13000 setzt für die Windangriffsfläche der Last eine Mindestannahme von 1,0 m² je Tonne mit dem Formbeiwert 1,2 an, also **1,2 m²/t**; liegt die tatsächliche wirksame Fläche darüber, ist eine Sonderbetrachtung nötig. Die Windangabe bezieht sich auf die 3-s-Böe an der höchsten Stelle [V, EN 13000 über Leseprobe; FEM 5.016]. Die Herstellerformel lautet

$$v_\max = v_{\max,\text{TAB}} \cdot \sqrt{\frac{1{,}2\ \mathrm{m^2/t} \cdot m_H}{A_W}},\qquad A_W = A_P \cdot c_W,$$

und ist durch die Tabellengeschwindigkeit nach oben begrenzt. B18 prüft sie gegen drei Quellenbeispiele (Liebherr: 85 t mit 60 m² → 9 m/s, 65 t mit 280 m² → 5,9 m/s; FEM: 7 m/s) [V, `test_windformel_gegen_quellen`].

> **Beispiel 14b.2 (Windgrenze der Holztafeln).** Holztafeln haben 14 bis 20 m² Windangriffsfläche je Tonne, mehr als das Zehnfache der Normannahme. Mit einer Tabellengeschwindigkeit von 9 m/s ergeben sich in B18 zulässige Böen von **2,85 bis 4,07 m/s**: Wand 2,9–3,0, Giebel 3,3, Decke 4,1, Dach 2,85 m/s [V, Prototyp].
>
> Das ist eine leichte Brise. Die Formel ist konservativ, weil sie Traglastreserven nicht anrechnet [U]; ob Kranunternehmen für Holztafeln mit Auslastungsreserve höhere Werte freigeben, ist offen. Mit dem 10-m-Mittelwind des Wetterdienstes darf keinesfalls gerechnet werden, weil die 3-s-Böe in Hubhöhe „um Faktor 2 und mehr“ höher sein kann [V, FEM 5.016].

Eine holzbauspezifische Windgrenze aus DGUV oder Holzbau Deutschland hat die Recherche nicht gefunden [U]. Für den Innenlader gilt: Be- und Entladen der Paletten ist ab Windstärke 5 verboten [V, Langendorf]. Die Windgrenze ist deshalb eine harte Eingabe der Hubplanung, gerechnet mit dem Windrechner des Herstellers und gemessen mit einem Windmesser am Kran.

### 14b.2.5 Anschlagmittel

Kapitel 2.8 der DGUV Regel 100-500 ist zurückgezogen; maßgeblich ist die DGUV Regel 109-017 „Lastaufnahme- und Anschlagmittel“ mit einem Neigungswinkel der Stränge von höchstens 60° und der Tragfähigkeit T_β = T_0 · cos β [V, Recherche 19]. Für Holzelemente gibt es Anschlagschrauben mit europäischer technischer Bewertung: Der Schmid RAPID T-Lift trägt je Kugelkopfabheber 1,3 t (d = 12 mm) bzw. 2,5 t (d = 16 mm) mal sin α, mit einem dynamischen Beiwert von 1,10 (stationärer Kran) bis 2,00 (fahrbarer Kran auf unebenem Gelände), jede Schraube nur einmal und höchstens 30 min belastet; das System Rothoblaas WASP wird mit k_mod = 1,0, γ_M = 1,3, γ_G = 1,35 und φ₂ = 1,2 bemessen und verlangt ab drei Anschlagpunkten eine Traverse [V]. Die Anschlagpunkte gehören in Werkplanung und Modell (DAT-14b-05).

**E14b.2 – Die Kranwahl ist eine Vorauswahl mit konservativen Hüllkurven; Wind, Stützkraft und Anschlag bleiben freigabepflichtig.** *Entscheidung.* Die App wählt Kran und Stellplatz mit Traglast × 0,8, maximaler Stützkraft und der Windformel nach DIN EN 13000. Jeder Hub trägt Hublast, Radien, Traglast, Auslastung, zulässige Böe und das Kennzeichen „Last über Nachbargrund“ im Pset `HRB_Kranhub`. Das Ergebnis hat den Status `freigabepflichtig`, bis das Kranunternehmen den Einsatzplan als Dokument liefert. *Begründung.* Herstellerdaten liegen nur als PDF vor, Einsatzplaner sind geschlossen [V]; die konservativen Annahmen machen die Vorauswahl sicher, aber nicht optimal. *Beleg.* Recherche 19; B18.

## 14b.3 Kranstellplatz, Abladezone und Abstände

### 14b.3.1 Abstandsregeln

Die Stellfläche des Krans muss drei Arten von Abständen einhalten [V, Recherche 19]:

| Regel | Kernwert | Quelle |
|---|---|---|
| Freileitung | bis 1 kV **1 m**; 1–110 kV **3 m**; 110–220 kV **4 m**; 220–380 kV und unbekannte Spannung **5 m**; Ausschwingen von Seil und Last berücksichtigen | DGUV Vorschrift 52 § 39; DGUV Vorschrift 38 § 16 |
| Baugrube, Böschung | Abstand der Abstützung zur Böschungskante: Gesamtgewicht bis 12 t ≥ 1,00 m, über 12 bis 40 t ≥ 2,00 m; darüber Nachweis | DIN 4124 in der Wiedergabe BG BAU B 213 |
| bewegte Kranteile | ≥ 0,5 m zu Bauwerk, Gerüst und Stapeln | BG BAU B 213 (für Turmdrehkrane formuliert) |

B18 rechnet die Freileitung mit einem Zuschlag von 1 m [U, Annahme] und in 2D, also ohne Anrechnung der Leitungshöhe, und über 40 t mit einem Beispielabstand von 3 m und dem Kennzeichen „Nachweis nötig“ [U]. Der Wurzelbereich von Bäumen (Kronentraufe + 1,5 m) ist eine Sperrfläche; die Baumschutzverordnung München und DIN 18920 sind nicht geprüft [U].

### 14b.3.2 Überschwenken des Nachbargrundstücks

Das Eigentum am Grundstück erstreckt sich auf den Luftraum; Einwirkungen, an deren Ausschließung der Eigentümer kein Interesse hat, muss er dulden (§ 905 BGB) [V, Recherche 19]. In Bayern ist das Überschwenken mit **und ohne** Last ein „Übergreifen von Geräten“ nach Art. 46b Abs. 1 BayAGBGB. Es ist dem Eigentümer und den Nutzungsberechtigten mindestens einen Monat vorher anzuzeigen (Abs. 3). Lehnt der Nachbar ab, gibt es keine Selbsthilfe, nur die Duldungsklage; geduldet werden muss nur, wenn die Arbeiten anders nicht oder nur mit unverhältnismäßigen Kosten möglich sind (OLG München, Urteil vom 15.10.2020, 8 U 5531/20) [V mittelbar; Gesetzestext nicht abgerufen]. Das Landgericht München II hatte im selben Streit das lastfreie Überschwenken in 17 m über dem First noch für duldungspflichtig gehalten [U]. Für die App folgt daraus: Jeder Hub, dessen Hakenweg das Nachbargrundstück berührt, erzeugt eine R4-Frist und eine Warnung, und die Zahl solcher Hübe ist ein Kriterium der Stellplatzwahl.

### 14b.3.3 Das Suchverfahren von B18

B18 sucht Kran und Stellplatz durch vollständige Rasteraufzählung [V, Recherche 19]:

```text
für jeden Kran K:
  F_K ← (Grundstück ∪ Straße) − Abladezone − Haus⊕0,5 m − Baugrube⊕d_4124(Gesamtgewicht_K)
        − Wurzelbereiche − Schächte − Sperrflächen des Szenarios
  für (x, y) im 0,5-m-Raster, Orientierung ∈ {0°, 90°}:
    kleinste Platte p mit Abstützrechteck ⊂ F_K und F_max/p² ≤ min p_zul unter der Platte
    verwerfen ohne Platte oder wenn der Heckradius Haus⊕0,5 oder Krone⊕0,5 schneidet
    je Element: r = max(|Aufnahme − C|, |Schwerpunkt − C|); verwerfen bei Hublast > 0,8·T_K(r)
    verwerfen bei Abstand(Hakenweg ⊕ ½ max(L, B), Ausleger, Heck; Freileitung) < Schutzabstand + Zuschlag
    Kosten = Einsatztage · Tagessatz + Anfahrt (+ Straße) (+ große Platten)
    Schlüssel = (Kosten, Lasthübe über Nachbar, auf Straße, max. Auslastung, Kran, x, y, Orientierung)
bester Stellplatz = kleinster Schlüssel
```

Der Hakenweg folgt dem kürzeren Schwenkweg mit linear über den Drehwinkel veränderlichem Radius, abgetastet an 25 Punkten und um die halbe größte Elementabmessung aufgeweitet, weil sich die Last drehen kann. Die lexikographische Ordnung des Schlüssels macht das Ergebnis eindeutig.

> **Beispiel 14b.3 (Kranwahl in B18).** Grundstück 22 × 30 m an einer Straße im Süden, Einfahrt 7,0 m breit, Freileitung und Nachbargrundstücke auf beiden Seiten. Vier Beispielkrane, je 14 694 geprüfte Stellungen [V, `ausgabe/b18_kranplanung.json`].
>
> | Szenario | AK-35 | AK-60 | AK-100 | MBK-8 | gewählt |
> |---|---|---|---|---|---|
> | basis | 40 zulässig, 2 650 € | 22 zulässig, 4 300 € | 0 (Abstützung mit Platten passt nirgends) | 64 zulässig, 4 950 € | AK-35 bei (18,5 \| 4,0) in der Einfahrt |
> | Einfahrt belegt | 0 (von der Straße fehlt Reichweite) | 18 zulässig, 4 300 € | 0 | 64 zulässig, 4 950 € | AK-60 bei (23,0 \| −4,5) auf der Straße |
>
> **basis:** Platten 1,0 × 1,0 m auf verdichtetem Schotter, p = 250 ≤ 250 kN/m², genau an der Grenze. Größte Auslastung 78,4 % beim Hub W-N2 (1,73 t bei r = 20,0 m, Beispieltraglast 2,21 t). Erforderliche Hakenhöhe höchstens 10,3 m. Zwei Hübe führen Last über Nachbargrund (D-1 mit 10 m Länge, R-N1). Abstand zur Freileitung ≥ 12,5 m (gefordert 4,0 m). Zwei Einsatztage.
>
> **Einfahrt belegt:** Platten 1,5 × 1,5 m, p = 178 ≤ 200 kN/m², größte Auslastung 71,9 % bei r = 29,6 m, kein Lasthub über Nachbargrund, aber Sondernutzung und verkehrsrechtliche Anordnung. Kosten +62 %.
>
> **Befund.** Das Gewicht begrenzt den Kran nicht: Die Hublasten liegen bei 1,15 bis 1,73 t. Es begrenzen Reichweite und Stellfläche. Beim 1,0-m-Raster findet die Suche den engen Einfahrtsplatz (7,0 m Abstützung mit Platten in 7,0 m Einfahrt) nicht und wählt für 3 200 € einen Platz teilweise auf der Straße; 0,25 m liefert dasselbe Ergebnis wie 0,5 m.

Das Verfahren ist verwandt mit der Literatur zur Kranstandortoptimierung. Recherche 19 hat 19 Arbeiten von 1999 bis 2024 über Crossref geprüft, darunter Verfahren zur Wahl und Aufstellung von Mobilkranen, zu zulässigen Aufstellflächen, zur Hubwegplanung im Modulbau und eine Fallstudie zu Holzfertighäusern mit Teleskopkran, die das Wetter als Hauptursache für Stillstand nennt; sie sind noch nicht in das Literaturverzeichnis übernommen. Nach Recherche 19 ist die analytische Berechnung zulässiger Aufstellflächen eine Alternative zur Rastersuche, die das Rasterproblem aus Beispiel 14b.3 vermeidet [U]. Dass Baustellenlogistik regelbasiert aus einem Hausmodell geplant werden kann, zeigen Løvset und Kollegen für Gerüste: Ihre Pipeline plant das Gerüst nach Vorschriften, erzeugt Stücklisten, Gewichte und Kosten und vergleicht das Ergebnis mit einer professionellen Planung [@lovset2013scaffold].

**E14b.3 – Die Stellplatzsuche ist vollständig und lexikographisch geordnet; das Raster ist höchstens 0,5 m.** *Entscheidung.* Die App zählt alle Stellungen im Raster ≤ 0,5 m in zwei Orientierungen auf und ordnet nach (Kosten, Lasthübe über Nachbar, Straße, Auslastung, Kran, x, y, Orientierung). Liegt der gewählte Platz an einer Grenze (Pressung = p_zul oder Abstützung = Stellflächenbreite), erzeugt sie einen Hinweis „ohne Reserve“. Eine exakte Randsuche ersetzt das Raster, sobald sie implementiert ist. *Begründung.* Rastersensitivität in B18 [V]; Erklärbarkeit und Reproduzierbarkeit (E8.28). *Beleg.* `test_raster_sensitiv`, `test_kranwahl_basis`, `test_kranwahl_einfahrt_belegt`.

## 14b.4 Transport

Straßenfahrzeuge dürfen samt Ladung höchstens **2,55 m breit** und **4,00 m hoch** sein, das Einzelfahrzeug 12,00 m, der Sattelzug 15,50 bzw. 16,50 m und der Zug 18,75 m lang, ohne Toleranz (§ 32 StVZO). Die Achslast beträgt 10 t, angetrieben 11,5 t, das Gesamtgewicht einer Kombination mit mehr als vier Achsen 40 t (§ 34 StVZO). Die Ladung darf hinten bis 1,50 m hinausragen, bei Fahrten bis 100 km bis 3 m, insgesamt höchstens 20,75 m (§ 22 Abs. 2–4 StVO) [V, Recherche 19]. Übermaß verlangt eine Erlaubnis nach § 29 Abs. 3 StVO oder eine Ausnahme nach § 46 Abs. 1 Nr. 5 StVO bzw. § 70 StVZO; das bayerische Verfahren ist nicht geprüft [U].

Holztafeln werden stehend im Innenlader transportiert. Der Faymonville PrefaMAX hat einen Ladeschacht von 7,1 bis 10,2 m bei 2,55 m Fahrzeugbreite und wirbt ausdrücklich damit, dass keine Begleitfahrzeuge und Sondergenehmigungen nötig sind; Langendorf nennt eine Ladehöhe über 3 700 mm und 27 t Aggregatlast [V]. Das Gestellmaß für Holztafeln hat die Recherche nicht gefunden; B18 nimmt 1,5 m Stapelbreite an [U].

> **Beispiel 14b.4 (Ladungen in B18).** Next-Fit-Beladung mit Beispielgrenzen (Nutzlast 24 t): Wände, Giebel und Dachelemente stehend im Innenlader (Summe der Dicken ≤ Gestellbreite), Decken liegend auf dem Plateau (Stapelhöhe ≤ 4,00 m − 1,35 m Ladeflächenhöhe).
>
> | LKW | Fahrzeug | Elemente | Masse | Ankunft |
> |---:|---|---|---:|---|
> | 1 | Innenlader | W-S1 bis W-O2 | 4,50 t | Tag 1, 07:30 |
> | 2 | Innenlader | W-N1 bis W-W2 | 4,50 t | Tag 1, 08:42 |
> | 3 | Plateau | D-1 bis D-6 (1,83 m Stapel) | 4,39 t | Tag 1, 09:54 |
> | 4 | Innenlader | Giebel | 2,61 t | Tag 1, 11:54 |
> | 5 | Innenlader | Dach Süd | 3,49 t | Tag 1, 12:54 |
> | 6 | Innenlader | Dach Nord | 3,49 t | Tag 2, 06:30 |
>
> Der Engpass ist das Volumen, nicht die Nutzlast: Kein LKW ist zu mehr als 19 % ausgelastet. Die Beladereihenfolge ist die Umkehrung der Montagereihenfolge; sie steht als `Pset_PackingInstructions.SpecialInstructions` am Vorgang MOVE [V, Recherche 19].

Die Elementierung wird damit auch von der Transportgrenze begrenzt: Ein Element, das stehend höher als die Ladehöhe oder liegend breiter als 2,55 m ist, macht aus einem Normaltransport einen Übermaßtransport mit Genehmigung. Generative Panelisierungsverfahren beziehen Logistikregeln deshalb in die Elementierung ein [@liu2021panelization], und Leitlinien für bauorientiertes Design for Manufacture and Assembly führen die Logistikoptimierung als einen von fünf Aspekten [@tan2020construction]. Die Elementgrenzen sind in Kapitel 17 Gegenstand der Fertigungsregeln.

## 14b.5 Genehmigungen

In München liegen die Genehmigungen auf dem kritischen Pfad der Montage. Recherche 19 hat die Verfahren des Mobilitätsreferats und die Fristen aus Zivil- und Arbeitsschutzrecht erhoben [V, soweit nicht anders markiert]:

| Vorgang | Zuständig, Verfahren | Frist | Unterlagen |
|---|---|---|---|
| Haltverbot für Abladezone | Mobilitätsreferat, verkehrsrechtliche Anordnung | Bearbeitung ca. 10 Arbeitstage; Schilder spätestens am 4. Tag vor Gültigkeit (3 volle Kalendertage); Baustellenbelieferung bis 365 Tage | Antrag, bemaßte Skizze, Vornotierungsliste; Schilder selbst aufstellen, Wiederholung alle 20–30 m |
| Kran auf öffentlichem Grund | Mobilitätsreferat: Sondernutzungserlaubnis und verkehrsrechtliche Anordnung (§ 45 StVO) | mehrere Wochen; 2018/19 im Mittel 3,2 Wochen (klein) bzw. 5,3 Wochen (mittel/groß), Spitzen 7 Wochen [U aktuell] | Antrag „Baustelle privat“, MVAS-Zertifikat, Verkehrszeichenplan nach RSA 21, Angabe „vor benachbartem Anwesen“ |
| Stillstand | Auflage des Mobilitätsreferats | nach 10 Werktagen ungenutzt Absicherung abbauen, nach 20 räumen | – |
| Überschwenken des Nachbarn | Anzeige an Eigentümer und Nutzungsberechtigte (Art. 46b Abs. 3 BayAGBGB) | ≥ 1 Monat | Art, Dauer und Umfang, mit oder ohne Last |
| Vorankündigung | zuständige Arbeitsschutzbehörde (BaustellV § 2) | ≥ 2 Wochen vor Einrichtung | Anhang I BaustellV |
| Freileitung | Netzbetreiber, bei über 1 kV auch das Versorgungsunternehmen | vor Montage | ggf. Freischaltung oder Abdeckung |

Die Baustellenverordnung verlangt eine Vorankündigung, wenn die Baustelle länger als 30 Arbeitstage mit mehr als 20 gleichzeitig Beschäftigten dauert oder mehr als 500 Personentage umfasst, und einen Sicherheits- und Gesundheitsschutzplan (SiGe-Plan), wenn mehrere Arbeitgeber tätig sind und eine Vorankündigung nötig ist **oder** besonders gefährliche Arbeiten ausgeführt werden [V]. Zu den besonders gefährlichen Arbeiten zählen Absturzgefahr über 7 m, Arbeiten näher als 5 m an Hochspannungsleitungen und der Auf- und Abbau von **Massivbauelementen** mit kraftbetriebenen Hebezeugen (Anhang II Nr. 1, 4, 10). Ob vorgefertigte Holzelemente Massivbauelemente in diesem Sinn sind, ist ungeklärt [U]; B18 empfiehlt im Zweifel einen SiGe-Plan.

> **Beispiel 14b.5 (Fristen für die Montage am 12.10.2026).** Montagetag T aus den Eingabedaten von B18; die Fristen folgen der Tabelle oben, der Zeitstrahl ist abgeleitet [U].
>
> | spätestens | Vorgang | Grundlage |
> |---|---|---|
> | 20.07.2026 (T − 12 Wochen) | Ausstattungsfestlegung unterschrieben | [@regnauerBLB2024], Beispiel 3.5 |
> | 31.08.2026 (T − 6 Wochen) | Anzeige des Überschwenkens (gesetzliche Mindestfrist 1 Monat: 12.09.2026); Antrag Sondernutzung, falls Kran auf der Straße | Art. 46b BayAGBGB; Mobilitätsreferat |
> | 21.09.2026 (T − 3 Wochen) | Antrag Haltverbot (10 Arbeitstage vor dem 08.10. wäre der 24.09.) | Mobilitätsreferat |
> | 28.09.2026 (T − 2 Wochen) | Vorankündigung, falls erforderlich | BaustellV § 2 |
> | 08.10.2026 (T − 4 Tage) | Haltverbotsschilder stehen | Mobilitätsreferat |
>
> Im Szenario „basis“ ist die Nachbar-Anzeige wegen zweier Lasthübe über Nachbargrund Pflicht, ein Sondernutzungsantrag nicht; im Szenario „Einfahrt belegt“ ist es umgekehrt. Die Stellplatzwahl verschiebt also den kritischen Pfad.

**E14b.4 – Genehmigungen sind R4-Regeln mit Frist relativ zum Montagetermin.** *Entscheidung.* Jeder Genehmigungsvorgang ist eine Regel mit Auslöser (Kran auf Straße, Lasthub über Nachbar, Abladezone im öffentlichen Raum, Vorankündigungsschwelle), Frist relativ zu T und Unterlagenliste. Aus dem `IfcWorkSchedule` berechnet die App die spätesten Termine und warnt bei Unterschreitung. Ändert sich der Stellplatz, werden die Auslöser neu ausgewertet. *Begründung.* Die Fristen sind gesetzlich oder behördlich festgelegt [V]; ihre Auslöser hängen an Größen, die das Modell kennt. *Beleg.* Recherche 19; Beispiel 3.5; ANF-03-20.

## 14b.6 Montagereihenfolge, Zeitplan und Baustelleneinrichtung

### 14b.6.1 Reihenfolge und Zeitplan

Die Montage folgt einer Rangordnung, die aus der Statik und der Zugänglichkeit kommt: Erdgeschosswände vor Decke, Decke vor Dachgeschoss-Giebeln, Giebel vor Dachelementen. B18 prüft diese Ordnung mit einer eigenen Funktion; ein vertauschtes Gegenbeispiel wird erkannt [V, `test_haus_und_reihenfolge`]. Die Hubzeiten sind Beispielwerte (Wand 18, Decke 20, Giebel 15, Dach 22 min). Im Szenario „basis“ ergibt sich: Kran rüsten Tag 1 ab 07:00, erster Hub 08:00, Ende Tag 1 um 14:52, Tag 2 von 07:00 bis 09:28 einschließlich Abrüsten, 10,3 Kraneinsatzstunden. Eine Ladung wird nicht über Nacht geteilt; der Kran bleibt über Nacht aufgebaut, was B18 als Warnung ausgibt (Sicherung nach Betriebsanleitung) [V, `test_zeitplan`].

Die Literatur überführt die Stückliste vom Werk zur Baustelle [@hussamadin2020conceptual] oder synchronisiert Fertigung, Logistik und Montage im Innenausbau [@ding2025fitout], jeweils ohne Holzrahmenbau-Evaluation. Hier ist die Montagereihenfolge schlicht eine Eigenschaft des Modells, aus der Beladereihenfolge, Lieferzeiten und Kranzeit folgen.

### 14b.6.2 Abbildung in IFC

IFC 4.3 bildet die Montageplanung schemakonform ab [@iso2024ifc]; die Datei `b18_montage.ifc` hat 1 134 Entitäten, besteht die Validierung mit EXPRESS-Regeln mit 0 Meldungen und ist byte-identisch über Läufe und Hash-Seeds [V, Recherche 19]:

| Sachverhalt | IFC 4.3 |
|---|---|
| Montageplan | `IfcWorkSchedule` PLANNED → `IfcRelAssignsToControl` → Sammel-`IfcTask` CONSTRUCTION |
| Vorgänge | `IfcTask` INSTALLATION (26 Hübe), MOVE (6 Anlieferungen), Rüsten; `IfcRelNests` |
| Zeiten | `IfcTaskTime` (ScheduleStart, ScheduleFinish, ScheduleDuration); `IfcRelSequence` FINISH_START |
| Element ↔ Vorgang | `IfcRelAssignsToProduct` |
| Kran | `IfcConstructionEquipmentResource` ERECTING und `IfcTransportElement` LIFTINGGEAR (E8.18) |
| LKW | `IfcVehicle` VEHICLEWHEELED mit Ressource TRANSPORTING |
| Stellfläche, Abladezone, Schwenkbereich | `IfcSpatialZone` CONSTRUCTION, TRANSPORT, RESERVATION |
| Beladung | `Pset_PackingInstructions` am `IfcTask` MOVE |
| Hubdaten | `HRB_Kranhub` am `IfcTask` |

`CRANEWAY` ist eine Kranbahn in einer Halle und passt nicht zum Mobilkran; LIFTINGGEAR ist eigene Wahl [V Enum, U Wahl]. Ob 4D-Viewer `IfcTaskTime` einheitlich lesen und ob der Validation Service Elemente ohne Geometrie bemängelt, ist offen [U]. Dass Terminpläne im 4D-BIM per Sprache geändert werden können, zeigt VISA4D mit 71 von 80 richtig klassifizierten Befehlen [@jaff2025visa4d]; für die Sprachschnittstelle (Kapitel 10) ist der Montagetermin damit ein möglicher Intent.

### 14b.6.3 Baustelleneinrichtungsplan und SiGe-Plan

B18 erzeugt je Szenario einen Baustelleneinrichtungsplan als SVG mit Grundstück, Haus, Kranstellung, Abstützung, Schwenkbereich, Abladezone, Freileitung, Bäumen und den Hakenwegen über Nachbargrund (`ausgabe/b18_be_plan_basis.svg`, `…_einfahrt_belegt.svg`); die Ausgabe ist deterministisch [V, `test_svg_deterministisch`]. Der Plan ist Grundlage für den Antrag beim Mobilitätsreferat und für die Unterweisung der Kolonne. Den SiGe-Plan selbst erstellt der Koordinator; die App liefert ihm die gefährlichen Arbeiten nach Anhang II BaustellV mit Ort und Zeit als strukturierte Eingabe.

Werk- und Montagepläne prüft der Architekt nach einem Merkblatt der Bayerischen Architektenkammer nur auf offenkundige, mit zu erwartender Fachkenntnis erkennbare Fehler, und der Prüfvermerk kann ein Eintrag im digitalen Arbeitsablauf sein [@byak2021montageplaene]. Für den Montageplan heißt das: Er ist ein `IfcApproval` mit Prüfumfang, Prüfer, Datum und Vorbehalt (Kapitel 18), nicht eine Unterschrift auf Papier.

**E14b.5 – Der Montageplan ist Teil des Modells und wird wie jede Ableitung reproduzierbar erzeugt.** *Entscheidung.* `IfcWorkSchedule`, Vorgänge, Ressourcen, Zonen und BE-Plan entstehen aus Parametermodell, Elementierung und Baustellendaten. Die Freigabe durch Kranunternehmen, Bauleitung und gegebenenfalls SiGe-Koordinator ist ein `IfcApproval` am Montageplan. *Begründung.* Kapitel 8 (E8.18, E8.26); Merkblatt 13 der Byak. *Beleg.* B18: 35 Vorgänge, 33 Reihenfolgebeziehungen, 3 Zonen, 0 Meldungen [V].

## 14b.7 Zwischenfazit

1. **Reichweite und Stellfläche begrenzen den Kran, nicht das Gewicht.** Die Elemente wiegen 0,65 bis 1,23 t, die Radien liegen bei 20 bis 30 m. Die Lage des Hauses und die Einfahrt entscheiden über Krangröße, Kosten und Genehmigungen.
2. **Der Wind ist die versteckte Grenze.** Holztafeln haben mehr als die zehnfache Windangriffsfläche der Normannahme; die zulässige Böe liegt nach der Herstellerformel bei 3 bis 4 m/s.
3. **Beim LKW begrenzt das Volumen.** Kein Transport ist zu mehr als 19 % der Nutzlast ausgelastet.
4. **Genehmigungen bestimmen den kritischen Pfad.** Nachbar-Anzeige, Sondernutzung und Haltverbot brauchen drei bis sechs Wochen Vorlauf und hängen an der Stellplatzwahl.
5. **Die Vorauswahl ist sicher, die Freigabe bleibt beim Menschen.** Die Herstellerdaten liegen nur als PDF vor, die Einsatzplaner sind geschlossen. Das Schema `kran-traglast.schema.json` macht die Tabellen maschinenlesbar, ohne die Hubfreigabe zu ersetzen.

## 14b.8 Umsetzungsvorgaben für die App

### 14b.8.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/regelkatalog-14b-logistik.yaml` | 15 Regeln zu Hublast, Wind, Bodenpressung, Freileitung, Böschung, Heckabstand, Anschlagmitteln, Fahrzeugmaßen, Ladung, Überschwenken, Haltverbot, Sondernutzung, Vorankündigung und SiGe-Plan, Montagereihenfolge und Kranfreigabe nach `regel.schema.json` |
| `spezifikation/kran-traglast.schema.json` | JSON-Schema (Draft 2020-12) eines Krandatensatzes: Traglast je Konfiguration (Auslegerlänge, Ballast, Abstützbasis, Schwenkbereich) als Radius-Traglast-Tabelle mit Interpolationsregel, Geometrie, Abstützung mit Stützkraft und tragendem Tellerteil, Fahrzeugdaten, Windangaben, Quelle und Status; mit dem Beispielkran AK-35 aus B18 |

Am 27.09.2026 geprüft: Die YAML-Datei ist parsebar und validiert ohne Fehler gegen `regel.schema.json`; das Kranschema ist nach Draft 2020-12 gültig, und sein Beispiel validiert. **Schemabefund:** Das Muster für Anforderungskennungen in `regel.schema.json` (`^ANF-[0-9]{2}a?-[0-9]{2}$`) lässt `ANF-14b-…` nicht zu. Die Regeln dieses Katalogs nennen ihre Anforderungen deshalb im Feld `hinweis`; das Muster ist bei der nächsten Schemaversion auf `[a-z]?` zu erweitern. Neu verwendete Profile, in `regelprofile.yaml` nachzutragen: `DE-Arbeitsschutz-Bau` (S1), `DE-StVO-StVZO` (S1), `BY-AGBGB` (S1), `BY-M-Mobilitaetsreferat` (S1) und `DE-Normen-Krane` (S3, DIN EN 13000, DIN 4124, DGUV-Informationen und -Regeln); daneben `M-Firma` (registriert).

### 14b.8.2 Anforderungen

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14b-01 | Muss | Elementgewicht = Σ Volumen × Rohdichte aus dem Einzelteilmodell; Zuschläge sind Parameter mit Status [U]; `GrossWeight` ab Reifegrad A. | E14b.1 | B1: 649,4 kg ± 0,5 kg, 49,2 kg/m² (`test_b1_gewicht`); Decke 36,6 kg/m², Dach 43,4 kg/m² (`test_aufbau_flaechengewicht`). |
| ANF-14b-02 | Muss | Hublast = Elementmasse + Anschlagmittel + Hakenflasche; zulässig bis 0,8 · T_K(r_max), r_max aus Aufnahme- und Absetzpunkt. | 14b.2.2 | B18 basis: größte Auslastung 78,4 % bei W-N2 (1,73 t, r = 20,0 m). Hub mit 0,81 · T_K: `verletzt`. |
| ANF-14b-03 | Muss | Krandaten nach `kran-traglast.schema.json`; zwischen Tabellenradien gilt die Interpolationsregel des Datensatzes, für Herstellertabellen „nächstgrößerer Radius“. | 14b.2.2 | Datensatz ohne Interpolationsregel wird abgewiesen. Tabelle (20 m; 2,2 t), (22 m; 1,8 t): bei 21 m linear 2,0 t, nach Regel „nächstgrößer“ 1,8 t. |
| ANF-14b-04 | Muss | Bodenpressung p = F_max/A ≤ p_zul der ungünstigsten Zone unter der Platte; kleinste passende Platte aus der Plattenliste. | 14b.2.3 | DGUV-Beispiel: 120 kN / 0,035 m² = 3 430 kN/m² (`test_bodenpressung_beispiele`). B18 basis: Platte 1,0 m, 250 ≤ 250 kN/m² mit Hinweis „ohne Reserve“. |
| ANF-14b-05 | Muss | Windgrenze je Hub nach DIN EN 13000 und Herstellerformel mit A_W aus der Elementfläche; Ergebnis im Pset `HRB_Kranhub`. | 14b.2.4 | Formel trifft 9,0 und 5,9 m/s (Liebherr) und 7 m/s (FEM) (`test_windformel_gegen_quellen`); B18: Dach 2,85 m/s, Decke 4,1 m/s. |
| ANF-14b-06 | Muss | Schutzabstand zur Freileitung nach Spannung plus Ausschwingzuschlag; unbekannte Spannung 5 m. Prüfung über Hakenweg, Ausleger und Heck. | 14b.3.1 | 0,4/1/20/110/220/380 kV und unbekannt: 1/1/3/3/4/5/5 m (`test_schutzabstand_und_baugrube`). Bei (18,5; 4,0) verletzt MBK-8 mit festem 45-m-Ausleger den Abstand, AK-35 nicht (`test_freileitung_harte_regel`). |
| ANF-14b-07 | Muss | Abstand der Abstützung zur Böschung nach Gesamtgewicht; über 40 t Kennzeichen „Nachweis nötig“. | 14b.3.1 | 10 t: 1,00 m; 36 t: 2,00 m; 48 t: Kennzeichen „Nachweis nötig“ (`test_schutzabstand_und_baugrube`). |
| ANF-14b-08 | Muss | Heckradius + 0,5 m frei von Haus und Baumkrone. | 14b.3.1 | Heckradius 3,5 m: Abstand Drehmitte–Haus 4,1 m zulässig, 3,9 m verworfen (3,5 + 0,5 = 4,0 m). |
| ANF-14b-09 | Muss | Stellplatzsuche vollständig im Raster ≤ 0,5 m mit lexikographischem Schlüssel. | E14b.3 | basis: AK-35 bei (18,5; 4,0), 2 650 €; Einfahrt belegt: AK-60 bei (23,0; −4,5), 4 300 € (`test_kranwahl_basis`, `test_kranwahl_einfahrt_belegt`); Raster 1,0 m weicht ab (`test_raster_sensitiv`). |
| ANF-14b-10 | Muss | Jeder Hub mit Hakenweg über Nachbargrund erzeugt die Frist nach Art. 46b BayAGBGB; die Zahl solcher Hübe geht in die Stellplatzwahl ein. | 14b.3.2 | basis: 2 Hübe (D-1, R-N1), Warnung mit Frist T − 1 Monat; Einfahrt belegt: 0 Hübe. |
| ANF-14b-11 | Muss | Transport nach § 32, § 34 StVZO und § 22 StVO; Übermaß erzeugt den Genehmigungshinweis. | 14b.4 | B18: 6 Ladungen, keine über 19 % Nutzlast (`test_lkw_ladungen`); Element 2,60 m liegend breit: Übermaß mit Hinweis § 29 Abs. 3 StVO. |
| ANF-14b-12 | Muss | Beladereihenfolge = Umkehrung der Montagereihenfolge, als `Pset_PackingInstructions` am Vorgang MOVE. | 14b.4 | LKW 1: Beladung W-O2, W-O1, W-S2, W-S1 für Montage W-S1 … W-O2. |
| ANF-14b-13 | Muss | Montagereihenfolge EG-Wand < Decke < DG-Giebel < Dach wird geprüft. | 14b.6.1 | B18: 0 Verstöße; vertauschtes Gegenbeispiel wird erkannt (`test_haus_und_reihenfolge`). |
| ANF-14b-14 | Muss | Zeitplan aus Hubzeiten, Rüstzeit und Arbeitszeitfenster; keine Ladung über Nacht geteilt. | 14b.6.1 | basis: Tag 1 07:00–14:52, Tag 2 07:00–09:28, 10,3 h (`test_zeitplan`). |
| ANF-14b-15 | Muss | Genehmigungsfristen relativ zum Montagetermin mit Auslösern aus der Stellplatzwahl. | E14b.4, Bsp. 14b.5 | T = 12.10.2026: Nachbar-Anzeige spätestens 12.09.2026 (Plan 31.08.), Haltverbot-Antrag 21.09., Schilder 08.10.; Kran auf Straße löst Sondernutzung aus. |
| ANF-14b-16 | Muss | Vorankündigung und SiGe-Plan nach BaustellV; Anhang II Nr. 10 bei Holzelementen als `unbestimmt` mit Empfehlung. | 14b.5 | 25 Arbeitstage, 12 Beschäftigte, 2 Arbeitgeber: keine Vorankündigung; Kranmontage: Hinweis „SiGe-Plan im Zweifel“. |
| ANF-14b-17 | Muss | IFC der Montage nach 14b.6.2; Hubdaten in `HRB_Kranhub`. | E14b.5, E8.18 | `b18_montage.ifc`: 1 134 Entitäten, 0 Validierungsmeldungen, byte-identisch (`test_ifc_valide_und_deterministisch`). |
| ANF-14b-18 | Muss | BE-Plan als SVG mit Kran, Abstützung, Schwenkbereich, Abladezone, Freileitung und Hakenwegen über Nachbargrund. | 14b.6.3 | SVG deterministisch (`test_svg_deterministisch`); jede Warnung „Nachbar“ hat einen gezeichneten Hakenweg. |
| ANF-14b-19 | Muss | Kranwahl und Hubplanung sind `freigabepflichtig` bis zum Einsatzplan des Kranunternehmens; alle Beispielwerte sind als solche gekennzeichnet. | E14b.2 | Ohne Einsatzplan-Dokument: Gate „Montage“ gesperrt; Datensatz mit `beispielwerte = true` erzeugt im Bericht den Vermerk „keine Einsatzfreigabe“. |
| ANF-14b-20 | Soll | Anschlagpunkte und -system werden aus der Werkplanung übernommen; Neigungswinkel ≤ 60°, Tragfähigkeit T_β = T_0 · cos β. | 14b.2.5 | Strang mit 65° Neigung: `verletzt`; ab 4 Anschlagpunkten mit WASP ohne Traverse: `verletzt`. |
| ANF-14b-21 | Soll | Der Montagetermin ist per Sprache änderbar; die Fristen werden sofort neu berechnet. | 14b.6.2, Kap. 10 | Intent „Montage eine Woche später“: alle Fristen aus ANF-14b-15 um 7 Tage verschoben, Warnungen neu bewertet. |

### 14b.8.3 Datenstrukturen und Parameter

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `element.masse` | float | kg | > 0 | E14b.1 |
| `element.zuschlag_putz`, `element.zuschlag_fenster` | float | kg/m² | 20; 5,25 (Annahme) | B18, DAT-14b-01 |
| `element.windflaeche` | float | m² | Elementansicht | 14b.2.4 |
| `hub.anschlagmittel` | float | t | 0,30 (Beispiel) | B18 |
| `hub.auslastung_max` | float | – | 0,8 (Firmenparameter [U]) | 14b.2.2 |
| `hub.wind_tabelle`, `hub.wind_plan_boe` | float | m/s | 9,0; 7,0 (Beispiel) | B18 |
| `hub.referenz_windflaeche` | float | m²/t | 1,2 | DIN EN 13000 |
| `hub.r_aufnahme`, `hub.r_absetzen` | float | m | ≥ r_min | 14b.2.2 |
| `kran` | object | – | nach `kran-traglast.schema.json` | 14b.8.1 |
| `boden.zone[i].p_zul` | float | kN/m² | Tabelle DGUV 208-059 | 14b.2.3 |
| `platten` | list | m | 0,6; 0,8; 1,0; 1,2; 1,5; 2,0 (Beispiel) | B18 |
| `freileitung.spannung` | float oder null | kV | null = unbekannt | 14b.3.1 |
| `freileitung.zuschlag` | float | m | 1,0 (Annahme) | B18 |
| `baugrube.boeschungskante` | Polylinie | m | – | DIN 4124 |
| `fahrzeug.art` | enum | – | INNENLADER, PLATEAU, SATTEL | 14b.4 |
| `fahrzeug.gestellbreite`, `fahrzeug.nutzlast`, `fahrzeug.ladehoehe` | float | m, t | 1,5; 24; 3,6 (Beispiel) | B18, DAT-11 |
| `suche.raster` | float | m | ≤ 0,5 | E14b.3 |
| `montage.termin` | date | – | – | IfcWorkSchedule |
| `montage.hubzeit[typ]` | int | min | Wand 18, Decke 20, Giebel 15, Dach 22 (Beispiel) | B18 |
| `genehmigung[i]` | object | – | {art, ausloeser, frist_tage, unterlagen, status} | E14b.4 |

### 14b.8.4 Datenlieferungen von Regnauer

Die Datenlieferungen präzisieren DAT-11 aus Kapitel 3.

| ID | Gegenstand | Format | Ersatzwert | Anforderungen |
|---|---|---|---|---|
| DAT-14b-01 | Reale Elementgewichte einschließlich Fenster, Putz, Installation; größte Elementlängen und -höhen; Gewicht im CAD/ERP | Tabelle je Elementtyp | B18-Flächengewichte und Zuschläge | ANF-14b-01, -02 |
| DAT-14b-02 | Kranpartner und Krantypen; Einsatzpläne (LICCON, Crane Planner) und Stützkraftberichte mit Format | Liste, Beispiel-Einsatzplan | Beispielkrane AK-35 bis MBK-8 | ANF-14b-03, -19 |
| DAT-14b-03 | Transportflotte: Innenlader oder Spedition, Gestelle, Stapelbreite, Ladehöhe, Nutzlast, Dauererlaubnis für Übermaß | Tabelle | Innenlader 1,5 m, 24 t | ANF-14b-11, -12 |
| DAT-14b-04 | Kolonnengröße, Hubzeiten, Arbeitszeitfenster, Montage an einem oder zwei Tagen, Kran über Nacht | Tabelle | B18-Hubzeiten | ANF-14b-14 |
| DAT-14b-05 | Anschlagsystem (Traverse, Bänder, Schrauben) und Anschlagpunkte in der Werkplanung | Datenblatt, Werkplan | Traverse 0,30 t | ANF-14b-20 |
| DAT-14b-06 | Interne Windgrenze für Holztafeln (Böe, Messort) und Entscheidungsbefugnis; Erfahrungswerte abgesagter Montagetage | Angabe | Herstellerformel | ANF-14b-05 |
| DAT-14b-07 | Zuständigkeit für Haltverbot, Sondernutzung und Nachbar-Anzeige; Vorlaufzeiten in München und im Landkreis | Angabe | Fristen aus 14b.5 | ANF-14b-10, -15 |
| DAT-14b-08 | Just-in-time oder Zwischenlager; höchste Standzeit eines LKW; Wechselbrücken | Angabe | direkt vom LKW | ANF-14b-14 |
| DAT-14b-09 | Baustellenaufnahme: Zufahrt, Freileitungen, Bäume, Boden, Böschung als Checkliste oder GeoJSON | Formular, GeoJSON | Eingabe im Dialog | ANF-14b-04, -06, -07 |
| DAT-14b-10 | SiGe-Koordination und Auslegung von Anhang II Nr. 10 BaustellV für Holzelemente | Angabe | SiGe-Plan im Zweifel | ANF-14b-16 |

## Verwendete Schlüssel

Das Kapitel enthält 10 Zitatstellen zu 9 Schlüsseln. Die Rechts- und Regelquellen (StVO, StVZO, BaustellV, BayAGBGB, DGUV, DIN EN 13000, DIN 4124) und die 19 in Recherche 19 geprüften Arbeiten zur Kranplanung haben noch keine Einträge im Literaturverzeichnis; sie sind über Recherche 19 belegt und vor Abgabe nachzutragen.

**lit-A-acc-bim.bib** (1): `iso2024ifc`

**lit-B-vorfertigung-ki.bib** (1): `tan2020construction`

**lit-C-recht-normen.bib** (1): `regnauerBLB2024`

**lit-D-vergleich-vorfertigung.bib** (1): `hussamadin2020conceptual`

**lit-E-vergleich-automation.bib** (1): `liu2021panelization`

**lit-I-schneeball-b.bib** (3): `ding2025fitout`, `jaff2025visa4d`, `lovset2013scaffold`

**lit-K-ff4-jur.bib** (1): `byak2021montageplaene`

### Python-Key-Check

Am 27.09.2026 wurden alle `[@key]` im Text mit einem Python-Skript gegen die Schlüssel aus `literatur/lit-*.bib` abgeglichen; `spezifikation/regelkatalog-14b-logistik.yaml` enthält keine Bib-Schlüssel:

```text
Zitatstellen 10, Schlüssel 9, fehlend 0
YAML-Schlüssel 0, fehlend 0
```

Ergebnis: **0 fehlend.**

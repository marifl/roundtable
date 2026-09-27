# 14a Grundstücksentwässerung und Außenanlagen

Status: Entwurf v0.1 (27.09.2026). Befunde zu Regelwerk, Verfahren und Genehmigung; keine Entwässerungsplanung im Rechtssinn. Grundlage sind Recherche 18 (`../recherche/18-grundstuecksentwaesserung-versickerung.md`), das Beispiel B17 (`beispiele/b17_grundstuecksentwaesserung.py`, 20 Tests grün am 27.09.2026) und die Abschnitte 13.3 und 14.5. Referenzkommune ist München.

## 14a.0 Einordnung und Vorgehen

Das Fertighaus endet nicht an der Bodenplatte. Jede Fallleitung, jedes Regenfallrohr und jede Terrasse muss an einen Kanal oder an eine Versickerungsanlage angeschlossen werden. Dieses Kapitel beginnt dort, wo Abschnitt 13.3 (Abwasser im Gebäude) und Abschnitt 14.5 (Dachentwässerung) enden, am Fuß der Fallleitung und am Standrohr, und es endet am Einlassstück des öffentlichen Kanals oder in der Versickerungsanlage.

Für ein Entwurfssystem ist dieser Abschnitt aus drei Gründen wichtig:

1. **Er ist genehmigungspflichtig.** In München sind Anlagen unterhalb der Rückstauebene, erdverlegt oder in der Bodenplatte genehmigungspflichtig. Für das Fertighaus auf Bodenplatte ist damit jede Grundleitung unter der Platte Gegenstand eines Entwässerungsantrags [V, Recherche 18].
2. **Er koppelt an den Entwurf.** Lage der Nassräume, Gründung, Keller, Terrasse und Garagenzufahrt bestimmen Leitungswege, Tiefen, Hebeanlagen und die Fläche der Versickerung. Ein Keller unter der Rückstauebene erzwingt eine Hebeanlage; eine Rigole muss vom Keller weiter entfernt liegen als von einer Bodenplatte.
3. **Er ist kommunal geregelt.** DIN 1986-100 behandelt Anschlusskanäle ausdrücklich nicht [V, Recherche 18]. Nennweite, Führung und Anschlusspunkt bestimmt der Kanalnetzbetreiber, in München die Münchner Stadtentwässerung (MSE) nach § 9 Abs. 2 der Entwässerungssatzung (EWS).

Ob Außenanlagen und Grundstücksentwässerung zum Leistungsumfang von Regnauer gehören oder beim Bauherrn liegen, ist offen (Recherche 18, Frage 11; DAT-14a-01). Davon hängt ab, ob die App diese Anlagen **planen** oder nur **prüfen** soll. Das Kapitel spezifiziert beides, weil die Prüfung dieselben Regeln braucht wie die Planung.

## 14a.1 Schmutzwasser

### 14a.1.1 Regelwerk

Maßgeblich ist DIN 1986-100:2016-12; der Entwurf E DIN 1986-100:2025-06 integriert DIN 1986-4, überarbeitet den Abschnitt zum Rückstau und ergänzt Anhänge zur Dichtheitsprüfung und zur zeichnerischen Darstellung [V, Recherche 18]. Verlegung und Prüfung folgen DIN EN 1610, die Planung außerhalb von Gebäuden DIN EN 752. Die Normtexte sind kostenpflichtig; die folgenden Kernwerte stammen aus Inhaltsverzeichnissen, Fachartikeln und kommunalen Merkblättern und sind entsprechend markiert.

| Regel | Kernwert | Status |
|---|---|---|
| Grundleitung im Gebäude | vermeiden, besser Sammelleitungen (6.1.1) | [V] |
| Mindestgefälle | im Gebäude 0,5 %; außerhalb 1:DN (DN 150 → 0,67 %) | [V, Sekundärquelle] |
| Füllungsgrad und Geschwindigkeit | h/d = 0,5 und v ≥ 0,5 m/s im Gebäude; h/d = 0,7 und v ≥ 0,7 m/s außerhalb | [V, Sekundärquelle] |
| Nennweite | Grundleitung ≥ DN 100; in Fließrichtung nicht verringern (6.1.8) | [V, Sekundärquelle] |
| Innendurchmesser | DN 100/125/150/200 → d_i 96/113/146/184 mm (Tab. A.3) | [V] |
| Reinigungsöffnungen | am Fuß jeder Fallleitung; in Grundleitungen alle ≤ 20 m (< DN 150) bzw. ≤ 40 m (≥ DN 150); bei Richtungsänderung > 45° | [U, kommunale Merkblätter] |
| Schachtgröße nach Einbautiefe | Inspektionsöffnung DN 400 (≤ 1,2 m), DN 600 (≤ 1,6 m); Kontrollschacht DN 800 (≤ 1,8 m), DN 1000 (≤ 2,2 m); darüber Einsteigschacht DN 1000 | [U, kommunal, nicht DIN] |
| Rückstau | Ablaufstellen unter der Rückstauebene sichern; Hebeanlage nach DIN EN 12056-4 mit Rückstauschleife; Rückstauverschluss nach DIN EN 13564 nur bei Gefälle zum Kanal, untergeordneter Nutzung, kleinem Benutzerkreis und WC über der Rückstauebene | [V, MSE-Faltblatt] |
| Dichtheit | Prüfung mit Wasser oder Luft vor dem Verfüllen; wiederkehrend nach 30, dann alle 20 Jahre | [V]; Prüfdrücke [U] |

Die Bemessung der Schmutzwasserleitungen schließt an Recherche 08 an. Der Schmutzwasserabfluss ist Q_ww = K · √ΣDU mit K = 0,5, mindestens der größte Einzelanschlusswert. Die Leistungsfähigkeit bei Vollfüllung folgt aus Prandtl-Colebrook mit einer Betriebsrauheit k_b = 1 mm [U] und der kinematischen Zähigkeit 1,31 · 10⁻⁶ m²/s; die Teilfüllung wird über Q ~ A · R^(2/3) angenähert, mit Q/Q_v = 0,500 bei h/d = 0,5 und 0,837 bei h/d = 0,7 [U, Recherche 18].

### 14a.1.2 Frosttiefe und Höhensystem

Die Frosttiefe ist in München **1,20 m von der Geländeoberkante bis zur Rohrsohle** (Leitfaden 2.7, EWS § 8 Abs. 3). Die 0,80 m aus DIN 1986-100 5.6 gelten dort nur für Niederschlagsleitungen zur Versickerung [V, Recherche 18]. Der Unterschied ist für das Fertighaus auf Bodenplatte erheblich: Weil schon die Wanddurchführung frostfrei liegen muss, sinken die Fallleitungsfüße in B17 auf 1,45 und 1,35 m unter Fertigfußboden. Der Wert ist deshalb kein Normkennwert, sondern ein Parameter des kommunalen Regelprofils.

Die Höhen des Münchner Kanalkatasters liegen noch in DHHN12, das 2 bis 5 cm über DHHN2016 liegt; Pläne müssen DHHN2016 zeigen [V, Recherche 18]. Der Lageplan zum Bauantrag verlangt Höhen im amtlichen Höhenbezugssystem (§ 7 BauVorlV) [@bauvorlv]. Das Höhensystem ist damit ein Pflichtmerkmal jeder Höhenangabe, und das Modell hängt über seine Georeferenz an einem amtlichen Bezugssystem; wann dessen Verzerrung vernachlässigt werden darf, beantwortet ein Entscheidungsdiagramm von Jaud und Kollegen [@jaud2020georeferencing] (Abschnitt 8.4).

**E14a.1 – Das Technische Formblatt ist Eingabe, nicht Planungsergebnis.** *Entscheidung.* Anschlusspunkt, Einlassstück mit Sohle, Nennweite und Art des Kanals, Rückstauebene, Wasserschutzgebiet, Altlastverdacht und die Vorgabe zum Niederschlagswasser werden aus dem Technischen Formblatt des Netzbetreibers übernommen und mit Dokument-Hash gespeichert (E8.24). Fehlt es, sind alle davon abhängigen Regeln `unbestimmt`. *Begründung.* Die MSE bestimmt Zahl, Art, Nennweite, Führung und Anschlusspunkt (EWS § 9 Abs. 2) [V]. *Beleg.* Recherche 18, Abschnitt 2.

**E14a.2 – Frosttiefe, Rückstauebene und Höhensystem sind Parameter des kommunalen Profils.** *Entscheidung.* Das Profil `BY-M-EWS-2024-05` setzt die Frosttiefe auf 1,20 m (Schmutzwasser) und 0,80 m (Niederschlagsleitungen zur Versickerung), die Rückstauebene auf die Straßenoberkante an der Anschlussstelle, sofern das Formblatt nichts anderes nennt, und den Umrechnungsbetrag DHHN12 → DHHN2016 aus dem Formblatt. Andere Kommunen erhalten eigene Profile. *Begründung.* Diese Werte weichen von DIN 1986-100 ab und sind Satzungsrecht [V]. *Beleg.* EWS § 8, Leitfaden 2.2, 2.7 (Recherche 18).

### 14a.1.3 Schächte, Revisionsschacht und Anschlusskanal

Die EWS verlangt am Ende der Grundstücksentwässerungsanlage auf eigenem Grund einen **Revisionsschacht**, der zugleich Übergabeschacht ist (§ 8 Abs. 4, § 3 Nr. 9). Außen liegt er nur, wenn zwischen Grundstücksgrenze und Gebäude mindestens 5 m frei sind; sonst tritt eine Reinigungsöffnung im Gebäude an seine Stelle (Leitfaden 2.6). Was andernorts „Kontrollschacht“ heißt, heißt in München „Revisionsschacht“ [V, Recherche 18].

Der **Anschlusskanal** vom Revisionsschacht zum Einlassstück ist Teil der Grundstücksentwässerungsanlage und Eigentum der Anlieger, auch im öffentlichen Grund. Er verläuft geradlinig und ohne Gefällewechsel, mit Steilgefälle bis 1:1; Material- oder Nennweitenwechsel sind nur am Kanal oder am Revisionsschacht zulässig. Den Anstich nimmt nur der Kanalbetrieb der MSE vor. Besteht zum Kanal kein ausreichendes Gefälle, ist eine Hebeanlage vorgeschrieben (EWS § 8 Abs. 5) [V, Recherche 18].

> **Beispiel 14a.1 (B17, Szenario „bodenplatte“).** EFH 10 × 12 m auf Bodenplatte, Fertigfußboden 520,55 m, Grundstück 20 × 30 m mit 2 % Gefälle zur Straße, Mischwasserkanal DN 600 mit Einlass-Sohle 516,80 m, Rückstauebene 519,95 m. Zwei Fallleitungen mit ΣDU 6,4 und 2,9 [V, `ausgabe/b17_bericht.md`; Eingaben Beispielwerte].
>
> - **Netz:** 7 Haltungen und Anschlusskanal, zusammen 38,24 m, davon 5,27 m unter der Bodenplatte. DN 125 und 100 im Gebäude mit 5 %, DN 150 außen mit 0,67 bis 2,03 %.
> - **Tiefen:** Fallleitungsfüße 519,10 und 519,20 m; alle Knoten außen mindestens 1,20 m unter Gelände.
> - **Schächte:** 3 Inspektionsöffnungen DN 600 (Richtungsänderungen 90° und 49°, Zusammenführung) und der Revisionsschacht DN 1000 bei (8,00; 1,00) mit Sohle 518,78 m, Tiefe 1,20 m, 0,40 m innerhalb der Grenze. Der Vorgarten ist 9,00 m tief, der Schacht darf also außen liegen.
> - **Anschlusskanal:** DN 150, 4,60 m, Gefälle 43 %, zulässig 0,67 bis 100 %.
> - **Hydraulik:** Q_ww = 2,0 l/s (WC maßgebend), größte Auslastung 0,23.
> - **Prüfung:** 13 Schmutzwasser-Prüfpunkte, 0 Verstöße; Hinweise zur Kreuzung mit der Hausanschlusstrasse (SW-12) und zur genehmigungspflichtigen Grundleitung unter der Bodenplatte (SW-13).

Zwei weitere Szenarien von B17 zeigen die harten Grenzen. Im Szenario „keller“ liegt der Kellerfußboden mit 517,75 m unter der Rückstauebene; das Werkzeug verlangt eine fäkalienfreie Hebeanlage nach DIN EN 12050-2 mit Rückstauschleife (Auflage SW-10). Im Szenario „kanal_hoch“ liegt die Einlass-Sohle bei 518,90 m über der Sohle des Revisionsschachts (518,78 m); der Anschlusskanal hätte −2,6 % Gefälle, und das Gebäude braucht eine Hebeanlage (Verstoß SW-06) [V, Recherche 18].

## 14a.2 Niederschlagswasser

### 14a.2.1 Einleitungsverbot und erlaubnisfreie Versickerung

In München besteht für Niederschlagswasser **kein Benutzungsrecht** am Kanal, soweit Versickerung möglich ist (EWS § 4 Abs. 4). Eine Einleitung ist nur ausnahmsweise nach Vorabstimmung zulässig. Versickerungsanlagen dürfen **keinen Überlauf** zum Kanal haben (Leitfaden 5.2) [V, Recherche 18]. Die Anlage muss also auch Überlast schadlos auf dem Grundstück halten.

Ob die Versickerung eine wasserrechtliche Erlaubnis braucht, regeln in Bayern die Niederschlagswasserfreistellungsverordnung (NWFreiV) und die Technischen Regeln TRENGW [V, Recherche 18]:

| Regel | Kernwert | Fundstelle |
|---|---|---|
| Ausschluss | Wasserschutz- und Heilquellenschutzgebiete, Altlast(verdachts)flächen; nur nicht verändertes, nicht vermischtes Niederschlagswasser | NWFreiV § 1 |
| Flächen | keine Flächen mit regelmäßigem Umgang mit wassergefährdenden Stoffen (außer Kleingebinde ≤ 20 l) | NWFreiV § 2 |
| Größe | ≤ 1 000 m² befestigte Fläche je Anlage | NWFreiV § 3 Abs. 1 |
| Vorrang | flächenhaft über geeignete Oberbodenschicht; Rigole, Sickerrohr und -schacht **nur, wenn flächenhaft nicht möglich**, und nur vorgereinigt | NWFreiV § 3 Abs. 2 |
| Metalldächer | Cu-, Zn-, Pb-Flächen > 50 m² nur über bauartzugelassene Anlage | NWFreiV § 3 Abs. 2 |
| Mulde | bewachsener Oberboden ≥ 20 cm, Versickerungsfläche ≥ 1/15 der angeschlossenen Fläche; Metalldächer ≥ 30 cm | TRENGW Tab. 1 |
| Vorreinigung | Dach: Körbe zum Grobstoffrückhalt; Terrasse: Hofablauf mit Schlammeimer | TRENGW Tab. 2 |
| Lage | stauende Deckschichten nicht durchstoßen; Sohle ≤ 5 m unter Gelände und ≥ 1 m über dem mittleren höchsten Grundwasserstand (MHGW) | TRENGW Nr. 6 |
| Bemessung | nach DWA-A 138 in der jeweils gültigen Fassung, heute A 138-1 | TRENGW Nr. 5 |

Der Vorrang der Flächenversickerung ist die Regel, die in der Praxis am häufigsten übergangen wird. Die Rigole ist bequemer, weil sie keine Gartenfläche verbraucht. Rechtlich ist sie aber nur zulässig, wenn eine Mulde nicht möglich ist, und diese Begründung gehört in den Antrag [V, Recherche 18].

### 14a.2.2 Bemessung nach DWA-A 138-1

Das Arbeitsblatt DWA-A 138-1 vom Oktober 2024 ersetzt A 138 von 2005 [V, Recherche 18]. Vier Änderungen sind für den Rechenkern wesentlich:

1. Die infiltrationswirksame Durchlässigkeit ist k_i = k_f · f_k mit f_k = f_Ort · f_Methode ≤ 1. Sie ersetzt den pauschalen Ansatz k_f/2. f_Ort hängt von Zahl und Verteilung der Versuche ab, f_Methode vom Versuchsverfahren; eine Bodenansprache allein genügt nicht mehr.
2. Die Rigole versickert auch über die Stirnflächen bis zur mittleren Einstauhöhe.
3. Für kleine Anlagen gilt ein einfaches Verfahren nach DWA-A 117, wenn unter anderem die Wiederkehrzeit höchstens 10 Jahre beträgt.
4. Vor unterirdischer Versickerung ist grundsätzlich auch Dachabfluss zu behandeln.

Die Formeln des einfachen Verfahrens lassen sich ohne Normtext aus veröffentlichten Rechenblättern reproduzieren [V, Nachrechnung in Recherche 18]:

```text
k_i   = k_f · min(1, f_Ort · f_Methode)
A_C   = Σ A_E,i · C_m,i
A_S,m = b·L + h·(L + b)                                   mittlere Sickerfläche
Q_S   = k_i · A_S,m · 10³                                  [l/s]
L(D)  = [A_C·10⁻⁷·r_D(n) − b·h·k_i − Q_Dr·10⁻³ − V_Sch/(D·60·f_Z)]
        / [b·h·s_R/(D·60·f_Z) + (b + h)·k_i]
L_erf = max_D L(D),   D = 5 … 4320 min,  T = 5 a
V_erf = max_D (r_D·A_C·10⁻⁴ − Q_S)·D·60·f_Z·10⁻³  ≤  V_vorh = s_R·b·h·L
```

Die Tabellen der Abflussbeiwerte C_m und der Faktoren f_Ort und f_Methode bleiben kostenpflichtig [V]. B17 prüft den Rechenkern an drei veröffentlichten Bemessungen [V, `tests/test_b17.py`]:

| Bemessung | Eingabe | Ergebnis B17 | veröffentlicht |
|---|---|---|---|
| Rigole Wendeanlage Ludwigshöhstraße | A_C 820 m², k_i 1,04 · 10⁻⁶ m/s, 8,0 × 0,66 × 8,80 m | V_erf = 40,52 m³ bei D = 1 440 min | 40,52 m³ |
| Rigole B 166 Unterschleißheim | A_C 864 m², k_i = 5 · 10⁻⁶ · 0,75, 4,0 × 0,35 m, s_R 0,93 | L = 27,45 m bei D = 360 min | 27,45 m |
| Waldbrunn | A_C 5 592 m², 7,2 × 1,32 m | 17,36 m | 17,39 m [U, Rundung von k_f in der Quelle] |

Die Nachrechnung ist mehr als eine Plausibilitätsprobe. Sie belegt, dass der Rechenkern das Verfahren trifft, obwohl die Arbeit den Normtext nicht wiedergibt, und sie liefert Regressionswerte für jede spätere Änderung.

### 14a.2.3 Mulde vor Rigole

Für den Vergleich mit der Flächenversickerung rechnet B17 die Mulde mit dem Speicheransatz V(A_S) = max_D (r_D · (A_C + A_S) · 10⁻⁴ − k_i · A_S · 10³) · D · 60 · f_Z · 10⁻³ unter den Bedingungen V/A_S ≤ 0,30 m [U] und A_S ≥ A_E/15 (TRENGW). Die kleinste zulässige Muldenfläche ergibt sich durch Bisektion.

> **Beispiel 14a.2 (B17, Rigole und Mulde).** Dach 143 m² (C_m 0,8) und Terrasse 24 m² (C_m 0,7): A_E,b = 167 m², A_C = 131,2 m². k_f = 1 · 10⁻⁵ m/s, f_Ort · f_Methode = 0,9 · 0,8, also k_i = 7,2 · 10⁻⁶ m/s. Regenreihe T = 5 a aus einer Sekundärquelle für Unterschleißheim, nicht aus dem Münchner Rasterfeld [V, Recherche 18].
>
> | Größe | Wert |
> |---|---|
> | Rigole | L_erf = 9,29 m (D = 240 min, r = 28,3 l/(s·ha)) → gewählt 9,60 m = 12 Elemente, 0,80 × 0,66 m |
> | Speicher | V_erf = 4,61 m³ ≤ V_vorh = 4,82 m³; Entleerung 12,2 h |
> | Lage | Weststreifen, 1,20 m vom Gebäude (= 1,5 × 0,80 m Fundamenttiefe), Sohle 518,35 m |
> | Sickerraum | 3,35 m bis MHGW 515,00 m |
> | Mulde | hydraulisch A_S ≥ 17,1 m², TRENGW-Minimum 11,1 m² → passt auf das Grundstück |
>
> Befund NW-05: „Rigole begründen oder Mulde wählen“. Im Szenario „keller“ muss die Rigole 0,6 + 1,5 · 2,90 = 4,95 m vom Haus entfernt liegen; sie rückt in den Nordgarten auf 5,00 m, und die Mulde passt nicht mehr. Dort ist die Rigole begründet. Im Szenario „grundwasser_hoch“ (MHGW 518,40 m) ist der Sickerraum −0,05 m; die Anlage ist unzulässig (NW-02).

Der Abstand zum Gebäude folgt der Regel „ohne wasserdruckhaltende Abdichtung mindestens 1,5 × Baugrubentiefe ab Baugrubenfußpunkt, ohne Keller die Fundamenttiefe“ [V, Sekundärquelle]. Kommunale Pauschalwerte von 6 m „ohne Nachweis“ und 2 m zur Grundstücksgrenze sind nicht allgemein belegt [U].

### 14a.2.4 Zisterne, Gründach, Drossel und Vorbehandlung

- **Zisterne.** Regenwassernutzung richtet sich nach DIN 1989-1; in München ist bei Grau- und Regenwassernutzung ein Zähler über das Gebührenbüro vorzusehen [V; Bemessung DIN 1989 U]. Im IFC ist die Zisterne ein `IfcTank` STORAGE mit `StorageType` RAINWATER [V].
- **Gründach.** Begrünte Dächer mit mindestens 10 cm Aufbau und höchstens 15° Neigung gelten in München für die Gebühr zu 30 % als befestigt (EAS § 8 Abs. 5) [V]. Die Abflussbeiwerte 0,5 (< 10 cm) und 0,3 (≥ 10 cm) sind in allen Regelwerken gleich [U].
- **Drosselabfluss.** Einen allgemeinen Drosselwert veröffentlicht die MSE nicht; er ist Einzelfallentscheidung im Technischen Formblatt [V, Fehlen belegt].
- **Vorbehandlung.** Die MSE verlangt weiterhin eine Bewertung nach DWA-M 153, während die DWA die Qualitätsbewertung nach A/M 102 und A 138-1 verlagert hat [V Forderung, U Ablösung]. Der Generator gibt beides aus, bis die MSE umstellt.

**E14a.3 – Die Versickerung wird in der Reihenfolge Mulde, Rigole, Schacht geplant; die Wahl wird begründet.** *Entscheidung.* Der Generator bemisst zuerst die Mulde. Passt sie auf die zulässige Fläche, ist sie der Vorschlag; eine Rigole erzeugt dann den Hinweis NW-05 mit Begründungspflicht. Erst wenn keine Mulde passt, wird die Rigole geplant, erst wenn keine Rigole passt, ein Sickerschacht. Überlast bleibt auf dem Grundstück; ein Überlauf zum Kanal wird in München nie erzeugt. *Begründung.* NWFreiV § 3 Abs. 2, TRENGW Nr. 4, Leitfaden 5.2 [V]. *Beleg.* B17, Szenarien „bodenplatte“ und „keller“.

## 14a.3 Kommunale Anforderungen am Beispiel München

### 14a.3.1 Genehmigungsweg

Der Weg zum genehmigten Entwässerungsplan hat in München sechs Schritte [V, Recherche 18]:

1. **Technisches Formblatt** beim Erschließungsbüro MSE-421 anfordern. Es enthält Anschlussmöglichkeit, Einlassstück mit Auszug aus dem Kanalkataster, Altlastverdacht, Wasserschutzgebiet und die Vorgabe zum Niederschlagswasser. Soll Niederschlagswasser eingeleitet werden, geht zuerst die Selbstauskunft Niederschlagswasser an MSE-421.
2. **Entwässerungsantrag** je wirtschaftlicher Einheit (EFH oder Doppelhaushälfte) bei der Planannahme MSE-422: Genehmigungsantrag mit Erklärung zur Niederschlagswasserversickerung, Technisches Formblatt, Pläne dreifach, gegebenenfalls Bemessungen nach DWA-M 153 und A 138. Baukosten über 60 000 EUR sind anzugeben.
3. **Planinhalte.** Sinnbilder nach DIN 1986-100, Ein-Strich-Darstellung mit Nennweite und Werkstoff, nummerierte Schächte, Schrift ≥ 2,5 mm, **keine rote Farbe**, auf A4 gefaltet. Lageplan 1:1 000 mit Nordpfeil, Flurnummer und städtischem Kanal; Grundriss 1:100 mit Ablaufstellen unter der Rückstauebene, geschützten Bäumen und Sparten; Abwicklung 1:100 **in wahrer Länge** (kein Strangschema) mit Geländeoberkante, Rückstauebene, NHN-Höhen, Frosttiefe 1,20 m und Gefälle; Versickerung vollständig mit Schnitt, MHGW und k_f.
4. **Genehmigung.** Sie gilt als erteilt, wenn die MSE sie nicht binnen drei Monaten nach Vollständigkeit verweigert (EWS § 10 Abs. 3–4). Die Fiktion ersetzt weder Baugenehmigung noch wasserrechtliche Erlaubnis.
5. **Arbeitsbeginnanzeige** mindestens 24 Stunden vorher (§ 11 Abs. 1). Aufgrabung im öffentlichen Grund: Sondernutzung und verkehrsrechtliche Anordnung beim Mobilitätsreferat, Anmeldung mindestens 5 Arbeitstage vorher, 20 EUR je Hausanschluss.
6. **Bauüberwachung** durch MSE-423 mit Dichtheitsprüfung in Anwesenheit einer von der MSE beauftragten Person, im offenen Graben, vor Inbetriebnahme (EWS § 11 Abs. 3); danach Gebührenbescheid.

Genehmigungsfrei sind etwa das Abtrennen von Niederschlagswasser, zusätzliche Schächte und der Austausch genehmigter Anlagen (Leitfaden 2.1) [V].

**E14a.4 – Der Entwässerungsantrag ist eine abgeleitete Sicht mit kommunalen Darstellungsregeln.** *Entscheidung.* Lageplan, Grundriss und Abwicklung entstehen aus dem Modell als R4-Ausgaben mit einer Vollständigkeitsprüfung gegen die Planinhalte oben. Die Darstellungsregeln des Profils (Farbverbot Rot, Schriftgröße, Maßstäbe, Höhensystem, Abwicklung in wahrer Länge) sind Daten, nicht Code. *Begründung.* Dieselbe Logik wie bei den Bauvorlagen (Abschnitt 4.3.6): Die Übereinstimmung aller Pläne folgt aus der einen Quelle. B17 verwendet deshalb Braun, Blau und Violett [V]. *Beleg.* Recherche 18, Abschnitt 2.2; `ausgabe/b17_*_lageplan.svg` und `*_abwicklung.svg`.

Die Dichtheitsprüfung ist eine R3-Regel im Sinne von Kapitel 4: Sie verlangt die Handlung einer berechtigten Person. Im Modell wird sie als `IfcApproval` am Entwässerungssystem mit Protokoll als Dokument abgebildet und sperrt den Vorgang „Verfüllen“ im Bauablauf (Kapitel 14b, Kapitel 18).

### 14a.3.2 Gebühren

Die Niederschlagswassergebühr beträgt in München 1,77 EUR je m² reduzierter Fläche und Jahr; die reduzierte Fläche ist die Grundstücksfläche mal Gebietsabflussbeiwert, für Einzelhausgebiete 0,35. Die Schmutzwassergebühr beträgt 2,02 EUR je m³ Frischwasser. Beide Sätze gelten für den Kalkulationszeitraum bis 31.12.2026 [V, Recherche 18]. Für das Grundstück von B17 mit 600 m² ergibt sich 210 m² × 1,77 EUR = 371,70 EUR im Jahr. Bei Vollversickerung entfällt die Gebühr auf Antrag, wenn die tatsächliche Ableitungsfläche mindestens 25 % oder 400 m² kleiner ist (EAS § 8 Abs. 5). Die App weist diese Ersparnis als Folge der Versickerung aus, mit dem Hinweis auf den Kalkulationszeitraum.

## 14a.4 Routing auf dem Grundstück

### 14a.4.1 Das Problem und der Stand der Forschung

Aus Sicht der Informatik ist die Grundstücksentwässerung ein kleines Steinerbaum-Problem mit Gefällebedingung: Mehrere Quellen (Fallleitungsfüße, Standrohre, Hofabläufe) sind mit einem Ziel (Revisionsschacht oder Filterschacht vor der Versickerung) zu verbinden, sodass der Baum kurz ist, Hindernisse meidet und überall Mindestgefälle und Frosttiefe einhält.

Die Forschung zur automatischen Kanalnetzplanung löst Layout und Hydraulik **öffentlicher** Netze mit gemischt-ganzzahliger Optimierung, Spannbäumen, kürzesten Wegen, dynamischer Programmierung und Metaheuristiken. Recherche 18 hat acht solche Arbeiten aus den Jahren 2006 bis 2024 über die Verlagsseiten geprüft; sie sind noch nicht in das Literaturverzeichnis übernommen. Für den Holztafelbau am nächsten liegt eine Arbeit von Zhang und Kollegen aus der Forschungslinie zu BIM in der Vorfertigung [@yin2019building]. Sie entwerfen die Entwässerung von Wohngebäuden im Tafelbau automatisch im BIM, führen die Leitungen regelbasiert, teilen das Rohrnetz an den Tafelgrenzen und erzeugen Stücklisten je Tafel [@zhang2022bimbased]. Ihr Gegenstand endet aber am Gebäude, und sie arbeiten mit nordamerikanischen Regeln in Revit.

Eine Arbeit, die die Grundstücksentwässerung automatisch aus einem Fertighaus-Grundriss nach kommunaler Satzung plant, hat die Recherche nicht gefunden [U]. Das ist eine Forschungslücke. Die Bewertung aus Recherche 18 lautet: Die Literatur optimiert Netze mit Hunderten Haltungen nach Baukosten; beim Einzelgrundstück dominieren harte Satzungsregeln, und die Suchmenge ist winzig. Ein deterministisches Verfahren mit expliziter Regelprüfung ist hier besser erklärbar als eine Metaheuristik [U, eigene Bewertung].

### 14a.4.2 Das Verfahren von B17

B17 setzt das Routing deterministisch in acht Schritten um [V, Recherche 18]:

1. **Geometrie.** Grundstück, Gebäude, Gelände, geschützte Bäume, Sparten und befestigte Flächen. Das DGM1 Bayern im 1-m-Raster ist kostenfrei unter CC BY 4.0 verfügbar [@opengeodataBY; V, Recherche 18]; B17 rechnet noch mit einer Ebene.
2. **Versickerung zuerst.** Zulässige Fläche = Grundstück minus 2 m Grenzabstand, minus Gebäude + 1,5 · t, minus Baumkronen, minus befestigte Flächen + 0,5 m, minus Sparten + 1 m. Rechtecke auf einem 0,5-m-Raster in zwei Orientierungen; Ziel ist der kleinste Abstand zum Schwerpunkt der Zuläufe.
3. **Sichtbarkeitsgraph.** Knoten sind Quellen, Ziel, um 1,05 m versetzte Hindernisecken, Achtecke um Wurzelbereiche und Austrittspunkte senkrecht zu den Außenwänden. Kanten dürfen kein hartes Hindernis schneiden. Die Kosten sind Länge plus Zuschläge: Faktor 3 im Gebäude (1,5 mit Keller), 2 im Fundamentstreifen, 5 m je Spartenkreuzung, 0,5 m je Formstück. Alle Kostenwerte sind eigene Annahmen.
4. **Steiner-Heuristik nach Takahashi und Matsuyama.** Die fernste Quelle wird zuerst zum Ziel geführt; jede weitere wird per Dijkstra an den nächsten Punkt des bestehenden Baums angeschlossen. Der bestehende Baum ist für neue Kanten ein Hindernis. So entstehen weder Kreuzungen noch Doppelführungen.
5. **Topologie.** Wanddurchführungen einfügen, gerade Zwischenknoten entfernen, Last aufsummieren (ΣDU bzw. Q), Nennweite wählen und in Fließrichtung nicht verringern.
6. **Höhenplan.** Vorwärts: Sohle(v) = min(Sohle(u) − L · s_min, Gelände(v) − Frosttiefe). Rückwärts: liegt das Gefälle über 5 %, wird der oberstromige Knoten tiefer gelegt. Wiederholen bis stabil. Das Ergebnis ist die Mindesttiefe unter allen Randbedingungen.
7. **Schächte.** Revisionsschacht am Ziel, Schacht bei Zusammenführung und Richtungsänderung über 45° außerhalb des Gebäudes, Reinigungsöffnung im Gebäude, Zusatzschacht bei Überschreitung von 20 bzw. 40 m, Größe aus der Einbautiefe.
8. **Anschlusskanal.** Gerade zum Einlassstück. Liegt das Gefälle unter 1:DN, ist Freispiegelabfluss unmöglich, und das Werkzeug fordert eine Hebeanlage.

Alle vier Szenarien rechnen zusammen in 1,3 s. Die 20 Tests decken die Nachrechnungen, die Mulden-Bisektion, die Hydraulik, alle Szenarien, die 1 000-m²-Grenze der NWFreiV, harte Hindernisse, Kreuzungsfreiheit, Gebühr sowie deterministische JSON-, SVG- und IFC-Ausgaben ab [V, Recherche 18; Lauf am 27.09.2026: 20 passed].

**E14a.5 – Das Routing ist deterministisch und regelgeführt; Optimierungsverfahren sind Werkzeuge für große Netze.** *Entscheidung.* Für Einzel-, Doppel- und Reihenhausgrundstücke plant die App mit dem Verfahren aus 14a.4.2. Die Reihenfolge der Quellen ist festgelegt, Gleichstände werden über Koordinaten entschieden, und die Ausgabe ist byte-identisch. Metaheuristiken sind erst für Anlagen mit mehreren Gebäuden (Mehrfamilienhaus, Reihenhauszeile) zu prüfen. *Begründung.* Erklärbarkeit jeder Leitungsführung gegenüber MSE und Bauherrn; Reproduzierbarkeit nach E8.28. *Beleg.* B17: SHA-256 der IFC-Datei in zwei Prozessen gleich [V].

### 14a.4.3 Hydraulische Nachweise mit SWMM

Für Überflutungsbewertung und Langzeitsimulation ist EPA SWMM 5 das naheliegende Werkzeug. Es ist als Werk der US-Bundesverwaltung gemeinfrei; pyswmm 2.1.0 (BSD-2), swmm-toolkit 0.17.0 (CC0 und MIT/Apache) und swmmio 0.8.6 (MIT) erlauben Steuerung, Bibliotheksnutzung sowie Lesen und Schreiben von `.inp`-Dateien aus Python [V, PyPI in Recherche 18]. Die App exportiert das geroutete Netz als `.inp`, damit ein Fachplaner Überflutung und Starkregen nachweisen kann. Ein Überflutungsnachweis ist nach DIN 1986-100 erst ab einer abflusswirksamen Fläche von 800 m² erforderlich; DWA-A 138-1 verlangt, die Folgen auch darunter zu bewerten [V]. Für die kommerzielle Bemessung nach A 138-1 mit Behördenausgabe ist DWA Versickerungs-Expert die Referenz zur Validierung [V].

### 14a.4.4 Grenzen des Prototyps

Recherche 18 nennt fünf Grenzen von B17 [U]: Das Gelände ist eine Ebene; jeder Knoten hat nur eine Sohlhöhe, ohne Scheitelgleichheit und Absturz; Schmutzwasser wird vor Niederschlagswasser geroutet, und die Niederschlagsleitung weicht nur aus; Hausanschlussleitungen werden nicht mitgeplant; Schachtmaße und Abflussbeiwerte sind Beispielwerte aus kommunalen Merkblättern. Die Tabellen aus DIN 1986-100 und DWA-A 138-1 sind vor der produktiven Nutzung zu lizenzieren und als Datendatei mit Fundstelle zu führen.

## 14a.5 Abbildung in IFC

IFC 4.3 bildet die Grundstücksentwässerung weitgehend ab, nur die Versickerung nicht [@iso2024ifc; V, Schemaabfrage in Recherche 18]. Die Zuordnung steht in `spezifikation/ifc-mapping.csv` (Kapitel 8):

| Bauteil | IFC 4.3 | Bemerkung |
|---|---|---|
| Systeme | `IfcDistributionSystem` SEWAGE, RAINWATER, STORMWATER | Dach = RAINWATER, Hof und Stellplatz = STORMWATER |
| Grund- und Anschlussleitung | `IfcPipeSegment` RIGIDSEGMENT mit `Pset_PipeSegmentOccurrence.Gradient` und `.InvertElevation` | Gefälle und Sohle sind Standardmerkmale |
| Revisions- und Einsteigschacht | `IfcDistributionChamberElement` MANHOLE | „permits the entry of a person“ |
| Inspektionsöffnung, Kontrollschacht | `IfcDistributionChamberElement` INSPECTIONCHAMBER | „permits visible inspection“ |
| Hebeanlage | `IfcDistributionChamberElement` SUMP mit `IfcPump` und `IfcValve` CHECK | Rückstauschleife als Leitung über der Rückstauebene |
| Filterschacht, Abscheider | `IfcInterceptor` bzw. USERDEFINED | – |
| Zisterne | `IfcTank` STORAGE, `StorageType` RAINWATER | – |
| Rigole, Sickerschacht | **keine Klasse**: `IfcDistributionChamberElement` USERDEFINED „Versickerungsrigole“ | eigenes Pset für k_f, k_i, s_R, V_erf, V_vorh, MHGW |
| Mulde | `IfcGeographicElement` USERDEFINED „Versickerungsmulde“ | Wahl offen [U] |
| Gelände, Grundwasser | `IfcGeographicElement` TERRAIN, `IfcGeotechnicalStratum` WATER | MHGW als Fläche |

Das IFC des Szenarios „bodenplatte“ enthält 19 `IfcPipeSegment`, 9 `IfcDistributionChamberElement`, 1 `IfcInterceptor`, 2 `IfcPipeFitting`, 65 Ports und 29 `IfcRelConnectsPorts` in 2 Systemen und besteht die Validierung mit EXPRESS-Regeln mit 0 Fehlern [V, Recherche 18]. Die Psets heißen in B17 noch `B17_Entwaesserung` und `B17_Versickerung`; nach E8.21 werden sie zu `HRB_Entwaesserung` und `HRB_Versickerung`, wie in `ifc-mapping.csv` bereits vorgesehen.

## 14a.6 Außenanlagen

Die Außenanlagen sind für das Entwurfssystem vor allem als **Randbedingungen** der Entwässerung und der Montage relevant:

- **Befestigte Flächen** (Terrasse, Zufahrt, Stellplatz) bestimmen über ihren Abflussbeiwert die angeschlossene Fläche und über ihre Nutzung die Vorreinigung. B17 führt die Terrasse mit 24 m² und C_m 0,7, die Rasengitter-Zufahrt als befestigte Fläche.
- **Bäume.** Geschützte Gehölze bis 5 m zur Leitungsachse sind im Plan darzustellen, gegebenenfalls mit Stellungnahme der Unteren Naturschutzbehörde [V, MSE]. Den Wurzelbereich setzt B17 mit Kronentraufe plus 1,5 m nach DIN 18920 an [U]; die Baumschutzverordnung München ist nicht geprüft [U].
- **Sparten.** Kreuzungen mit Wasser, Strom und Telekommunikation sind im Plan einzutragen; Mindestabstände legt der Netzbetreiber fest [V Pflicht, U Werte].
- **Gelände.** Das DGM1 liefert Höhen für Tiefen und Gefälle [@opengeodataBY]. Eine Geländemodellierung (Aufschüttung, Abgrabung) ist nicht Gegenstand dieses Kapitels.

Die Außenanlagen koppeln auch an die Montage (Kapitel 14b): Schächte und die Rigole sind Sperrflächen für die Kranabstützung, frisch verfüllte Leitungsgräben tragen weit weniger als gewachsener Boden, und die Reihenfolge von Tiefbau und Montage muss das berücksichtigen. Der Schallschutz gegen Außenlärm, der ebenfalls vom Grundstück ausgeht, ist Gegenstand von Abschnitt 15.4 und B19.

## 14a.7 Zwischenfazit

1. **Die Grundstücksentwässerung ist kommunales Recht mit normativem Kern.** DIN 1986-100 und DWA-A 138-1 liefern die Rechenverfahren, die Satzung des Netzbetreibers die entscheidenden Kennwerte: Frosttiefe, Revisionsschacht, Anschlusskanal, Einleitungsverbot. Das verlangt kommunale Regelprofile.
2. **Die Versickerung hat eine Rangfolge.** Mulde vor Rigole vor Schacht, ohne Überlauf zum Kanal. B17 zeigt, dass die Mulde im Standardfall passt und die Rigole deshalb zu begründen ist.
3. **Die Bemessung ist reproduzierbar ohne Normtext.** Zwei veröffentlichte A-138-1-Rechnungen werden exakt nachgerechnet; die Tabellenwerte bleiben lizenzpflichtig.
4. **Das Routing ist klein und erklärbar.** Ein deterministischer Steinerbaum mit Höhenplan löst das Einzelgrundstück in Sekunden; die Literatur zu öffentlichen Netzen ist für diesen Fall überdimensioniert, und eine direkt vergleichbare Arbeit fehlt.

## 14a.8 Umsetzungsvorgaben für die App

### 14a.8.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/regelkatalog-14a-entwaesserung.yaml` | 21 Regeln zu Schmutzwasser (Frosttiefe, Gefälle, Nennweite, Schächte, Revisionsschacht, Anschlusskanal, Rückstau), Niederschlagswasser (NWFreiV, TRENGW, DWA-A 138-1, Einleitungsverbot) und Verfahren (Formblatt, Antrag, Dichtheit, Plandarstellung) nach `regel.schema.json`; Zuordnung zu den Prüfpunkten SW-01 bis NW-15 von B17 |

Am 27.09.2026 geprüft: parsebar mit PyYAML, 0 Fehler gegen `regel.schema.json` mit `jsonschema` 4.26. Neu verwendete Profile, in `regelprofile.yaml` nachzutragen: `BY-M-EWS-2024-05` (S1, Satzungsrecht München), `BY-Wasserrecht-NWFreiV` (S1) und `DE-aRdT-Entwaesserung` (S3, DWA). Für DIN 1986-100 wird das registrierte Profil `DE-aRdT-Sanitaer` verwendet.

### 14a.8.2 Anforderungen

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-14a-01 | Muss | Das Technische Formblatt ist Eingabe mit Dokument-Hash; fehlt es, sind die abhängigen Regeln `unbestimmt`. | E14a.1 | Ohne Formblatt: SW-01, SW-06, SW-10, NW-13 `unbestimmt`. Mit Formblatt von B17: `erfuellt`. |
| ANF-14a-02 | Muss | Alle Höhen tragen das Höhensystem; Katasterhöhen in DHHN12 werden mit dem Betrag aus dem Formblatt nach DHHN2016 umgerechnet. | 14a.1.2 | Einlass-Sohle 516,83 m DHHN12 mit Betrag 0,03 m ergibt 516,80 m DHHN2016; eine Höhe ohne System wird abgewiesen. |
| ANF-14a-03 | Muss | Frosttiefe aus dem Profil: München 1,20 m (SW), 0,80 m (NW zur Versickerung). | E14a.2 | B17 „bodenplatte“: alle SW-Knoten außen ≥ 1,20 m unter Gelände; Fallleitungsfüße 519,10 und 519,20 m. |
| ANF-14a-04 | Muss | Gefälle im Gebäude ≥ 0,5 %, außen ≥ 1:DN, höchstens 5 %. | 14a.1.1 | DN 150 außen: Mindestgefälle 0,67 %; alle Haltungen von B17 liegen zwischen Mindest- und Höchstgefälle, Nennweite monoton (`test_hoehenplan_regeln`). |
| ANF-14a-05 | Muss | Nennweite in Fließrichtung nicht verringern; Leistungsfähigkeit bei h/d 0,5 innen und 0,7 außen nachweisen. | 14a.1.1 | B17: Q_ww = 2,0 l/s, größte Auslastung 0,23; Nennweitenfolge monoton. |
| ANF-14a-06 | Muss | Schächte und Reinigungsöffnungen an Fallleitungsfuß, Zusammenführung, Richtungsänderung > 45° und nach 20/40 m; Größe aus Einbautiefe. | 14a.1.1 | B17: 3 Inspektionsöffnungen DN 600, Revisionsschacht DN 1000 bei (8,00; 1,00), Sohle 518,78 m (`test_schaechte`). |
| ANF-14a-07 | Muss | Revisionsschacht auf eigenem Grund; außen nur bei ≥ 5 m zwischen Grenze und Gebäude. | 14a.1.3 | Vorgarten 9,00 m: außen `erfuellt`. Vorgarten 4,00 m: Reinigungsöffnung im Gebäude statt Außenschacht. |
| ANF-14a-08 | Muss | Anschlusskanal gerade mit Gefälle 1:DN bis 1:1; sonst `verletzt` mit Auflage Hebeanlage. | 14a.1.3 | B17: 4,60 m, 43 % `erfuellt`. „kanal_hoch“: −2,6 %, `verletzt`, Hebeanlage (`test_kanal_zu_hoch_hebeanlage`). |
| ANF-14a-09 | Muss | Ablaufstellen unter der Rückstauebene erhalten eine Hebeanlage mit Rückstauschleife; ein Rückstauverschluss nur unter den Bedingungen von DIN EN 12056-4, nie im Revisionsschacht. | 14a.1.1 | „keller“ (UG 517,75 < RSE 519,95): Auflage Hebeanlage DIN EN 12050-2 (`test_keller_rueckstau_und_abstand`). |
| ANF-14a-10 | Muss | In München wird Niederschlagswasser nicht in den Kanal geleitet, außer das Formblatt erlaubt es; ein Überlauf zum Kanal wird nie erzeugt. | E14a.3 | Netz mit Notüberlauf zum Kanal: `verletzt` (NW-10). |
| ANF-14a-11 | Muss | Erlaubnisfreiheit nach NWFreiV § 1–3 wird geprüft. | 14a.2.1 | B17: 167 m² `erfuellt`; befestigte Fläche 1 100 m²: NW-04 `verletzt` (`test_nwfreiv_flaechengrenze`). Kupferdach 60 m² ohne zugelassene Anlage: `verletzt`. |
| ANF-14a-12 | Muss | Mulde vor Rigole vor Schacht; eine Rigole bei passender Mulde erzeugt einen Hinweis mit Begründungspflicht. | E14a.3, Bsp. 14a.2 | „bodenplatte“: Mulde A_S ≥ 17,1 m² passt, Hinweis NW-05. „keller“: Mulde passt nicht, Rigole ohne Hinweis. |
| ANF-14a-13 | Muss | Rigole nach DWA-A 138-1, einfaches Verfahren. | 14a.2.2 | Nachrechnung: V_erf = 40,52 m³; L = 27,45 m. B17: L_erf = 9,29 m → 9,60 m, V_erf 4,61 ≤ V_vorh 4,82 m³. |
| ANF-14a-14 | Muss | Sickerraum ≥ 1 m (nie < 0,5 m), Sohle ≤ 5 m unter Gelände. | 14a.2.1 | „grundwasser_hoch“: Sickerraum −0,05 m, `verletzt` (`test_grundwasser_hoch`). |
| ANF-14a-15 | Muss | Abstand der Versickerung zum Gebäude ≥ 1,5 × Baugruben- bzw. Fundamenttiefe; Grenzabstand als Parameter [U]. | 14a.2.3 | „bodenplatte“: 1,20 m gefordert und vorhanden; „keller“: 4,95 m gefordert, 5,00 m vorhanden. |
| ANF-14a-16 | Muss | Vorreinigung vor unterirdischer Versickerung (Filterschacht, Laubfang); Bewertung nach DWA-M 153 und A 138-1 werden beide ausgegeben. | 14a.2.4 | B17: Filterschacht NW-FS vor der Rigole, Hinweis NW-06; Bericht enthält beide Bewertungsabschnitte. |
| ANF-14a-17 | Muss | Das Routing ist deterministisch, kreuzungsfrei und meidet harte Hindernisse. | E14a.5 | `test_routing_meidet_harte_hindernisse`, `test_determinismus`: zwei Läufe ergeben byte-identische JSON-, SVG- und IFC-Dateien. |
| ANF-14a-18 | Muss | Lageplan, Grundriss und Abwicklung werden als Entwässerungsantrag nach den Darstellungsregeln des Profils erzeugt. | E14a.4 | SVG enthält keine Farbe mit überwiegendem Rotanteil; Abwicklung in wahrer Länge mit GOK, RSE, NHN-Höhen und Frosttiefe; Schrift ≥ 2,5 mm im Maßstab. |
| ANF-14a-19 | Muss | IFC nach 14a.5 mit Gefälle und Sohle in `Pset_PipeSegmentOccurrence`; eigene Psets mit Präfix `HRB_`. | 14a.5 | „bodenplatte“: 19 `IfcPipeSegment`, 9 Schächte, 65 Ports, 29 `IfcRelConnectsPorts`, 0 Validierungsfehler. |
| ANF-14a-20 | Muss | Die Dichtheitsprüfung ist eine Freigabe (`IfcApproval`) und sperrt den Vorgang „Verfüllen“. | 14a.3.1 | Ohne Protokoll ist der Vorgang „Verfüllen“ gesperrt; mit Protokoll und Prüfer freigegeben. |
| ANF-14a-21 | Muss | Aus dem Montagetermin werden die Fristen der Genehmigung berechnet (Fiktion 3 Monate, Arbeitsbeginnanzeige 24 h, Aufgrabung 5 Arbeitstage). | 14a.3.1 | Antrag vollständig am 01.06.2026: Fristende der Genehmigungsfiktion 01.09.2026; ein Tiefbaubeginn bis zu diesem Tag erzeugt eine Warnung. |
| ANF-14a-22 | Soll | Das Netz wird als SWMM-`.inp` exportiert. | 14a.4.3 | swmmio liest die Datei; Zahl der Knoten und Haltungen gleich dem Modell. |
| ANF-14a-23 | Soll | Die Gebührenfolge der Versickerung wird ausgewiesen. | 14a.3.2 | 600 m², GAB 0,35: 371,70 EUR/a; bei Vollversickerung 0 EUR/a mit Hinweis auf den Kalkulationszeitraum (`test_gebuehr`). |

### 14a.8.3 Datenstrukturen und Parameter

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `formblatt.einlass_sohle` | float | m NHN | Höhensystem Pflicht | Technisches Formblatt |
| `formblatt.kanal_art` | enum | – | SCHMUTZ, REGEN, MISCH | EWS § 14 |
| `formblatt.dn_anschluss` | int | mm | ≥ 150 | EWS § 9 Abs. 2 |
| `formblatt.rse` | float | m NHN | Straßenoberkante oder Vorgabe | Leitfaden 2.2 |
| `formblatt.nw_vorgabe` | enum | – | VERSICKERN, EINLEITEN_GEDROSSELT, EINLEITEN | Leitfaden 5 |
| `formblatt.wsg`, `formblatt.altlast` | bool | – | – | NWFreiV § 1 |
| `hoehensystem` | enum | – | DHHN2016, DHHN12 | 14a.1.2 |
| `profil.frosttiefe_sw`, `profil.frosttiefe_nw` | float | m | 0,80–1,50 | E14a.2 |
| `haltung.dn`, `haltung.gefaelle`, `haltung.sohle_oben`, `haltung.sohle_unten` | int, float | mm, %, m | DN ≥ 100 | 14a.1.1 |
| `knoten.art` | enum | – | FALLLEITUNG, STANDROHR, REINIGUNG, INSPEKTION, REVISION, FILTER, WANDDURCHFUEHRUNG | 14a.4.2 |
| `boden.k_f` | float | m/s | 10⁻⁶–10⁻³ | Sickertest |
| `boden.f_ort`, `boden.f_methode` | float | – | 0,3–1 bzw. ≤ 1 | DWA-A 138-1 |
| `grundwasser.mhgw` | float | m NHN | Mittel der Jahreshöchststände ≥ 10 a | RKU |
| `flaeche.a_e`, `flaeche.c_m`, `flaeche.c_s` | float | m², – | C 0–1 | DWA-A 138-1, DIN 1986-100 |
| `regen.kostra_feld`, `regen.reihe` | int, Tabelle | –, l/(s·ha) | D 5–4 320 min, T 1–100 a | KOSTRA-DWD-2020 |
| `rigole.b`, `rigole.h`, `rigole.L`, `rigole.s_r`, `rigole.f_z` | float | m, – | s_R 0,35 (Kies) bis 0,95 | 14a.2.2 |
| `mulde.a_s`, `mulde.einstau` | float | m², m | Einstau ≤ 0,30 m [U] | 14a.2.3 |
| `kosten.faktor_gebaeude`, `kosten.strafe_kreuzung` | float | –, m | 3; 5 (Annahme) | 14a.4.2 |

### 14a.8.4 Datenlieferungen von Regnauer

| ID | Gegenstand | Format | Ersatzwert | Anforderungen |
|---|---|---|---|---|
| DAT-14a-01 | Leistungsgrenze: gehören Grundstücksentwässerung und Außenanlagen zum Leistungsumfang (planen oder nur prüfen)? | Angabe | nur prüfen | alle |
| DAT-14a-02 | Anteil Bodenplatte/Keller, Lieferant der Gründung, Gründungstiefe bzw. Frostschürze | Tabelle | Bodenplatte, Fundamenttiefe 0,80 m | ANF-14a-03, -15 |
| DAT-14a-03 | Übergabepunkte der Fallleitungen (Lage, Höhe, Raster, Stutzen über oder unter Platte) | Tabelle je Haustyp | Lagen aus B17 | ANF-14a-03, -17 |
| DAT-14a-04 | Wer erstellt den Entwässerungsantrag, in welchem CAD; Nutzen eines generierten Plans | Angabe | App erzeugt Planentwurf | ANF-14a-18 |
| DAT-14a-05 | Dachentwässerung: Zahl und Lage der Fallrohre, Standrohre, Laubfang | Tabelle | vier Fallrohre (B17) | ANF-14a-16 |
| DAT-14a-06 | Versickerungs- und Zisternensysteme im Angebot, Hersteller, Speicherkoeffizient | Datenblatt | Blockrigole s_R 0,95 | ANF-14a-12, -13 |
| DAT-14a-07 | Zuständigkeit für Sickertest, Bodengutachten und MHGW-Auskunft | Angabe | Eingabe durch Bauherrn | ANF-14a-13, -14 |
| DAT-14a-08 | Standard-Hebeanlage (Hersteller, fäkalienfrei oder -haltig), Rückstauschleife | Datenblatt | DIN EN 12050-2 | ANF-14a-09 |
| DAT-14a-09 | Mehrsparten-Hauseinführung, Abstandsvorgaben der Netzbetreiber | Tabelle | Kreuzungshinweis ohne Abstandswert | ANF-14a-17 |
| DAT-14a-10 | Bedarf an IFC der Grundleitungen beim Tiefbauer (IFC oder PDF/DWG) | Angabe | IFC und PDF | ANF-14a-19 |

## Verwendete Schlüssel

Das Kapitel enthält 7 Zitatstellen zu 6 Schlüsseln. Die geringe Zahl ist ein Befund: Die Rechtsquellen (EWS, NWFreiV, TRENGW), Normen (DIN 1986-100, DWA-A 138-1) und die acht in Recherche 18 geprüften Arbeiten zur Kanalnetzoptimierung haben noch keine Einträge im Literaturverzeichnis; sie sind über Recherche 18 belegt und vor Abgabe als Bib-Einträge nachzutragen.

**lit-A-acc-bim.bib** (2): `iso2024ifc`, `jaud2020georeferencing`

**lit-C-recht-normen.bib** (2): `bauvorlv`, `opengeodataBY`

**lit-I-schneeball-a.bib** (1): `yin2019building`

**lit-J-schneeball-runde2.bib** (1): `zhang2022bimbased`

### Python-Key-Check

Am 27.09.2026 wurden alle `[@key]` im Text mit einem Python-Skript gegen die Schlüssel aus `literatur/lit-*.bib` abgeglichen; `spezifikation/regelkatalog-14a-entwaesserung.yaml` enthält keine Bib-Schlüssel:

```text
Zitatstellen 7, Schlüssel 6, fehlend 0
YAML-Schlüssel 0, fehlend 0
```

Ergebnis: **0 fehlend.**

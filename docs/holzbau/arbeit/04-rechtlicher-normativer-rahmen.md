# 4 Rechtlicher und normativer Rahmen

Status: Entwurf v0.1 (27.09.2026). Befunde zur Rechtslage, keine Rechtsberatung. Zitate beziehen sich auf `literatur/lit-C-recht-normen.bib`.

## 4.0 Einordnung und Vorgehen

Ein System, mit dem Laien Gebäude entwerfen, bewegt sich in einem dicht geregelten Feld. Die Regeln kommen aus sechs Quellen mit unterschiedlicher Verbindlichkeit:

- öffentliches Baurecht des Bundes (Bauplanungsrecht) und des Landes (Bauordnungsrecht)
- eingeführte Technische Baubestimmungen
- private Normen
- Regeln des Handwerks und der Gütesicherung
- Verbrauchervertragsrecht
- Querschnittsregelungen zu Haftung, künstlicher Intelligenz, Datenschutz und Barrierefreiheit

Dieses Kapitel ordnet die Quellen danach, **welche Funktion sie im System übernehmen**. Es beantwortet drei Fragen:

1. Welche Regeln begrenzen den Entwurfsraum?
2. Welche Regeln verlangen eine menschliche Verantwortung?
3. Welche Regeln bestimmen die Form, in der Ergebnisse übergeben werden müssen?

Räumlich beschränkt sich die Untersuchung auf Bayern und sachlich auf Wohngebäude der Gebäudeklassen 1 bis 3 mit höchstens drei Wohnungen in Holzrahmenbauweise. Die Rechtslage ist auf den 27.09.2026 datiert.

Methodisch wurde jede Aussage an der Primärquelle geprüft: Gesetzes- und Verordnungstext, amtliche Veröffentlichung oder Normausgabe. Aussagen, die sich nur auf Sekundärquellen stützen, sind mit [U] markiert. Die Recherchedokumentation liegt in `../recherche/02-regeln-recht-normen.md` und `../recherche/07-recht-rollen.md`.

## 4.1 Eine Taxonomie der Regeln nach Systemfunktion

Aus Sicht der Informatik ist nicht die juristische Rangordnung entscheidend, sondern die Rolle, die eine Regel im System spielt. Wir unterscheiden vier Klassen.

| Klasse | Funktion im System | Beispiele | Formalisierung |
|---|---|---|---|
| **R1 Entwurfsgrenzen** | schränken den Lösungsraum ein; müssen *während* des Entwurfs geprüft werden | Abstandsflächen, Vollgeschoss, GRZ/GFZ, Treppengeometrie, Fensterfläche, Dachneigung | ausführbare Geometrie- und Rechenregeln |
| **R2 Informationsanforderungen** | verlangen, dass bestimmte Informationen im Modell vorhanden sind | Gebäudeklasse, U-Werte, Materialien, Beteiligte, Georeferenz | IDS 1.0 [@ids2024] |
| **R3 Verantwortungsregeln** | verlangen eine Handlung einer berechtigten Person | Bauvorlageberechtigung, Standsicherheitsnachweis, Unterschrift | Freigabe-Gates mit `IfcApproval` |
| **R4 Formregeln** | bestimmen Form und Zeitpunkt der Übergabe | Bauvorlagen 1:100 als PDF, Baubeschreibung in Textform vor Vertragsschluss | abgeleitete Exporte mit Vollständigkeitsprüfung |

Diese Taxonomie erklärt, warum eine einzelne Prüftechnik nicht genügt:

- **IDS** beschreibt Informationsanforderungen (R2). Geometrische Beziehungen wie den Abstand einer Wand zur Grundstücksgrenze kann IDS nicht ausdrücken.
- **R1** braucht deshalb eine eigene Regelmaschine.
- **R3 und R4** sind keine Prüfregeln, sondern Prozessregeln.

Diese Unterscheidung prägt die Architektur in Kapitel 7.

## 4.2 Bauplanungsrecht: der Bebauungsplan als Quelle von R1-Regeln

Das Maß der baulichen Nutzung setzt der Bebauungsplan nach der BauNVO fest [@baunvo]. Für ein Einfamilienhaus zählen vor allem:

- Grundflächenzahl (GRZ) und Geschossflächenzahl (GFZ)
- Zahl der Vollgeschosse
- überbaubare Grundstücksfläche mit Baugrenzen und Baulinien
- örtliche Bauvorschriften zur Dachgestaltung

Seit dem 08.02.2023 sind Bauleitpläne im Standard XPlanung bereitzustellen [@xplanung]. Das Datenmodell XPlanGML enthält alle Festsetzungen, die ein Entwurfssystem braucht:

- `BP_BaugebietsTeilFlaeche` mit GRZ und Z
- `BP_UeberbaubareGrundstuecksFlaeche`
- `BP_BauGrenze`
- `BP_Dachgestaltung` mit DNmin, DNmax und Dachform

**Befund für Bayern [V]:** Die Pläne liegen überwiegend im sogenannten Minimalstandard vor, also als Umring des Geltungsbereichs mit Verweis auf den PDF-Plan. Sachauskünfte zu Art und Maß der Nutzung sind maschinell nicht abrufbar. Damit ist die naheliegende Annahme widerlegt, ein Entwurfssystem könne die Festsetzungen automatisch laden.

**Konsequenz:** Das System übernimmt das Datenmodell von XPlanGML als internes Schema. Befüllt wird es aber zunächst über eine Bestätigung im Dialog oder über eine PDF-Extraktion, die ein Mensch prüft. Sobald Gemeinden vollvektorielle Pläne liefern, entfällt dieser Schritt, ohne dass sich das Schema ändert.

Das Grundstück selbst ist ebenfalls nur teilweise frei verfügbar [@opengeodataBY]:

- **Frei (CC BY 4.0):** Hausumringe, Geländemodell, Luftbilder und die Parzellarkarte als Raster ohne Flurstücksnummern.
- **Kostenpflichtig:** Flurstücksgeometrie aus ALKIS, etwa 2,90 € je Flurstück.

## 4.3 Bauordnungsrecht Bayern

### 4.3.1 Abstandsflächen (Art. 6 BayBO)

Die Abstandsflächen sind die geometrisch anspruchsvollste R1-Regel. Nach Art. 6 Abs. 4 BayBO [@baybo2026] gilt:

- Die Wandhöhe wird von der Geländeoberfläche bis zum Schnittpunkt der Wand mit der Dachhaut gemessen.
- Die Höhe von Dächern mit einer Neigung bis 70° wird zu einem Drittel hinzugerechnet, bei steilerer Neigung voll.
- Das Ergebnis ist das Maß *H*.

Für die Tiefe der Abstandsfläche gilt nach Abs. 5 außerhalb von Gewerbe- und Industriegebieten:

$$T = \max(0{,}4\,H;\ 3\,\mathrm{m})$$

Seit der Novelle 2021 sind Giebelflächen normale Wände. Ihre Abstandsfläche ist die um den Faktor 0,4 gestauchte Giebelform, wobei das Mindestmaß von 3 m gilt.

Weitere Absätze regeln Sonderfälle:

- **Abs. 5a:** Gemeinden mit mehr als 250.000 Einwohnern.
- **Abs. 6:** Dachüberstände und Balkone bleiben unter Bedingungen außer Betracht.
- **Abs. 7:** Grenzgaragen.
- **Art. 81:** Gemeindliche Satzungen können abweichen.

> **Beispiel 4.1 (Traufseite).** Satteldach, Hausbreite 10,00 m, Dachneigung 35°, Traufwandhöhe 6,00 m.
>
> - Dachhöhe: 5,00 m · tan 35° = 3,50 m.
> - *H* = 6,00 m + 3,50 m / 3 = 7,17 m.
> - 0,4 · *H* = 2,87 m < 3 m, maßgeblich ist also **T = 3,00 m**.
>
> **Giebelseite:** Die Abstandsfläche folgt der Giebelform. Ihre Tiefe liegt bei 3,00 m an den Traufen (Mindestmaß, weil 0,4 · 6,00 m = 2,40 m) und bei 0,4 · 9,50 m = 3,80 m am First.
>
> Das lauffähige Beispiel B4 (`beispiele/b4_abstandsflaechen.py`) prüft diese Flächen gegen ein Beispielgrundstück von 20 × 30 m.

Das Beispiel zeigt, warum die Regel nicht als Tabellenwert, sondern als Geometrieoperation umgesetzt werden muss. Die Abstandsfläche hängt über die Dachgeometrie von Parametern ab, die der Kunde per Sprache ändert: Dachneigung, Kniestock und Gebäudebreite. Jede dieser Änderungen löst eine neue Prüfung aus.

### 4.3.2 Vollgeschoss

Das Vollgeschoss bestimmt, ob ein Entwurf die im Bebauungsplan festgesetzte Geschosszahl einhält. Die BauNVO verweist dafür auf das Landesrecht [@baunvo]. In Bayern gilt über Art. 83 Abs. 6 BayBO die Definition des Art. 2 Abs. 5 BayBO in der **bis 31.12.2007** geltenden Fassung fort [V]. Ein Geschoss ist danach Vollgeschoss, wenn zwei Bedingungen gelten:

1. Es liegt vollständig über der Geländeoberfläche.
2. Es hat über mindestens zwei Dritteln seiner Grundfläche eine lichte Höhe von mindestens 2,30 m.

Ein Kellergeschoss zählt, wenn seine Deckenunterkante im Mittel mindestens 1,20 m über der Geländeoberfläche liegt.

> **Beispiel 4.2.** Ein Dachgeschoss hat 100 m² Grundfläche. Davon haben 60 m² eine lichte Höhe von mindestens 2,30 m. Weil 60 % < 66,7 %, ist es **kein Vollgeschoss**.
>
> Wünscht der Kunde einen höheren Kniestock, wächst die Fläche mit mindestens 2,30 m. Ab 66,7 m² wird das Dachgeschoss zum Vollgeschoss. In einem Baugebiet mit der Festsetzung „II“ wäre das Haus dann dreigeschossig und damit unzulässig.
>
> Das System muss diese Schwelle beim Intent `kniestock_aendern` vorab berechnen und dem Kunden den Grenzwert nennen.

Weil die fortgeltende Fassung auf das Jahr 2007 zurückgeht, gilt für die Formalisierung: Das Regelwerk-Profil muss den **Zeitpunkt des Bebauungsplans** kennen. Ältere Pläne können auf noch ältere Fassungen verweisen.

### 4.3.3 Gebäudeklassen, Aufenthaltsräume, Fenster

Die Gebäudeklasse steuert Brandschutzanforderungen, Nachweispflichten und die Bauvorlageberechtigung. Gebäudeklasse 1 hat vier Merkmale [V]:

- freistehend
- Fußbodenoberkante des obersten Aufenthaltsgeschosses höchstens 7 m über Gelände
- höchstens zwei Nutzungseinheiten
- zusammen höchstens 400 m²

Die Fensterfläche von Aufenthaltsräumen muss nach Art. 45 BayBO mindestens ein Achtel der Netto-Grundfläche betragen. Für Wohngebäude der Gebäudeklassen 1 und 2 gilt die Mindestraumhöhe nicht [V].

> **Beispiel 4.3.** Ein Kinderzimmer mit 14,0 m² Netto-Grundfläche braucht mindestens 1,75 m² Fensterfläche.
>
> Die 1/8-Regel ist bauordnungsrechtlich notwendig, nach DIN 5034-1 aber nicht hinreichend für eine gute Tageslichtversorgung. DIN 5034-1 verlangt einen mittleren Tageslichtquotienten von mindestens 0,9 % [@din5034-1].
>
> Das System prüft die 1/8-Regel als R1-Grenze. Den Tageslichtquotienten zeigt es als Qualitätshinweis an.

### 4.3.4 Verfahren: Freistellung, vereinfachtes Verfahren, Typengenehmigung

Für Einfamilienhäuser im Geltungsbereich eines qualifizierten Bebauungsplans ist die **Genehmigungsfreistellung** (Art. 58 BayBO) der Regelfall [V]:

- Voraussetzung ist, dass das Vorhaben den Festsetzungen nicht widerspricht und die Erschließung gesichert ist.
- Die Unterlagen gehen an die Gemeinde.
- Nach einem Monat darf gebaut werden, wenn die Gemeinde kein Verfahren verlangt.
- Die bautechnischen Nachweise bleiben unberührt.

Weil die Freistellung genau an die Übereinstimmung mit dem Bebauungsplan gebunden ist, hängt der Nutzen des Systems unmittelbar von der Güte der R1-Regeln ab.

Für die Architektur ist eine weitere Vorschrift wichtig. Die **Typengenehmigung** nach Art. 73a BayBO kann für ein „System aus Bauteilen“ mit festgelegter zulässiger Veränderbarkeit erteilt werden. Sie gilt als bautechnischer Nachweis, ersetzt aber nicht das Verfahren [V].

Hier schließt sich ein Kreis zum Konzept des Regelraums: Ein Hersteller, dessen Bauteilsystem typengenehmigt ist, kann den Konfigurationsraum der App deckungsgleich mit dem genehmigten Veränderungsspielraum definieren. Diese Option wird in Kapitel 9 als eigenes Regelwerk-Profil aufgegriffen.

### 4.3.5 Verantwortung: Entwurfsverfasser und Bauvorlageberechtigung (R3)

**Befund:** Ein Laie kann nicht Entwurfsverfasser sein. Nach Art. 61 Abs. 6 BayBO kann aber ein **Unternehmen** Entwurfsverfasser sein, wenn die Bauvorlagen unter der Leitung einer bauvorlageberechtigten Person entstehen, deren Name auf den Bauvorlagen steht [V].

Bauvorlageberechtigt sind:

- **Allgemein** (Abs. 2): Architekten und in die Liste eingetragene Ingenieure.
- **Für freistehende oder einseitig angebaute Wohngebäude der Gebäudeklassen 1 bis 3 mit höchstens drei Wohnungen** (Abs. 3) zusätzlich:
  - Ingenieure der Fachrichtungen Architektur, Hochbau und Bauingenieurwesen
  - staatlich geprüfte Techniker der Fachrichtung Bautechnik
  - Maurer-, Betonbauer- und **Zimmerermeister**
- **Für Holzbauweise** (Abs. 4 Nr. 6): Absolventen eines anerkannten Studiengangs Holzbau und Ausbau.

Die Nachweise sind getrennt geregelt [V]:

- **Standsicherheit** (Art. 62, 62a): Bei Gebäudeklasse 1 bis 3 erstellen ihn gelistete Tragwerksplaner. Für Wohngebäude der Gebäudeklassen 1 und 2 wird er **weder geprüft noch bescheinigt**. Die Erklärung des Nachweiserstellers ist spätestens mit der Baubeginnsanzeige vorzulegen (§ 15 BauVorlV).
- **Brandschutz** (Art. 62b): Ihn stellt eine bauvorlageberechtigte Person auf; geprüft wird er erst bei Sonderbauten und Gebäudeklasse 5.

Diese Rechtslage entscheidet die Rollenfrage aus dem Zielbild:

- Der **Kunde** erstellt eine Vorplanung.
- Die **Firma** wird durch die Freigabe der bauvorlageberechtigten Person zur Entwurfsverfasserin.
- Der **Architekt** oder Zimmermeister prüft und verantwortet. Er zeichnet nicht mehr selbst.
- Für Wohngebäude der Gebäudeklassen 1 und 2 entfällt die Prüfung der Standsicherheit durch Dritte. Der **Tragwerksplaner** verantwortet den Nachweis deshalb allein. Umso wichtiger ist, dass seine Eingangsdaten aus dem Modell stammen und nicht abgetippt werden.

### 4.3.6 Form der Einreichung (R4)

Die Bauvorlagenverordnung verlangt [@bauvorlv]:

- **Lageplan** mindestens im Maßstab 1:1000, mit Abstandsflächen und Höhen im amtlichen Höhenbezugssystem (§ 7).
- **Bauzeichnungen** im Maßstab 1:100 (§ 8), mit der Wandhöhe nach Art. 6 Abs. 4, den lichten Raumhöhen und den Rohbaumaßen der Fenster.
- **Baubeschreibung** mit Gebäudeklasse und Baukosten (§ 9).
- **Übereinstimmung** aller Bauvorlagen untereinander (§ 13).

Der digitale Bauantrag in Bayern beruht auf der DBauV [@dbauv2026]. Die Authentifizierung über BayernID oder das Unternehmenskonto ersetzt die Unterschrift. **Die Bauvorlagen werden jedoch als PDF hochgeladen** [V]. Ein IFC-Modell ist keine anerkannte Bauvorlage und kann über XBau nur als Anlage übermittelt werden.

Die modellbasierte Genehmigung existiert in Deutschland als Richtlinie und in Pilotprojekten:

- Modellierungsrichtlinie BIM-basierter Bauantrag, 2020 [@bimbauantrag2020]
- MBO2BIM [@mbo2bim2023]
- Machbarkeitsstudie NRW 2026 [@nrw2026bimbauantrag]

Die Studie aus NRW empfiehlt eine formale Vorprüfung per IDS. Bayern plant mit dem Gesetzentwurf vom 21.07.2026 die ausschließlich digitale Einreichung [@bayDigitalisierungEntwurf2026], nach Stand der Recherche aber nicht die modellbasierte.

**Konsequenz:** § 13 BauVorlV verlangt die Übereinstimmung aller Bauvorlagen untereinander. Diese Forderung erfüllt ein System, das alle Vorlagen aus *einem* Modell ableitet, gleichsam konstruktionsbedingt. Das IFC ist damit nicht die Bauvorlage, aber die Quelle, die ihre Konsistenz garantiert.

## 4.4 Technische Baubestimmungen und Normen

Private Normen werden bauaufsichtlich verbindlich, wenn sie in die Bayerischen Technischen Baubestimmungen eingeführt sind [@baytb2025]. Für das Vorhaben relevant sind die Normen der folgenden Tabelle.

| Gebiet | Norm, Ausgabe | Kernaussage für das System | Status |
|---|---|---|---|
| Tragwerk | DIN EN 1995-1-1:2026-09 [@en1995-2026] | neue EC-5-Generation erschienen; eingeführt ist weiter 2010-12 + A2:2014 | [V] |
| Brandschutz Holzbau | HolzBauRL 2024-09 [@holzbaurl2024] | in BayTB 11/2025 eingeführt, für GK 1/2 meist nicht maßgeblich | [V] |
| Holzschutz | DIN 68800-2:2022-02 [@din68800-2] | Einbaufeuchte in GK 0 bis 3.1 **≤ 20 %** | [V] |
| Wärmeschutz | DIN 4108-2:2026-05 [@din4108-2] | neue Ausgabe; Mindestwärmeschutz, sommerlicher Wärmeschutz | [V] |
| Schallschutz | DIN 4109-33:2016-07 [@din4109-33] | Bauteilkatalog Holzbau; Entwurf 2026-09 | [V] |
| Brandschutz Bauteile | DIN 4102-4:2016-05 [@din4102-4] | Tabellen für Holztafelbauteile | [U] |
| Treppen | DIN 18065:2020-08 [@din18065] | Wohngebäude ≤ 2 WE: Laufbreite ≥ 80 cm, Steigung 14–20 cm, Auftritt 23–37 cm | [V] |
| Lüftung | DIN 1946-6:2019-12 [@din1946-6] | Lüftungskonzept, Feuchteschutzlüftung nutzerunabhängig | [V] |
| Tageslicht | DIN 5034-1:2021-08 [@din5034-1] | Tageslichtquotient ≥ 0,9 % im Mittel | [V] |

Zwei Befunde korrigieren die Ausgangskonzeption dieser Arbeit:

1. **Holzfeuchte.** Die dort genannten 18 % stammen nicht aus DIN 68800-2, die 20 % nennt. Sie stammen aus den Güte- und Prüfbestimmungen RAL-GZ 422 [@ral422]. Der Unterschied ist systematisch bedeutsam: Die 20 % sind eine normative Mindestanforderung, die 18 % eine privatrechtlich vereinbarte Qualitätsanforderung. Im Regelwerk erscheinen beide Werte, aber in unterschiedlichen Profilen (Abschnitt 4.6).
2. **Treppen.** DIN 18065 ist für Treppen innerhalb von Wohnungen und für Gebäudeklasse 1/2 in der Regel nicht bauaufsichtlich eingeführt [U]. Das Schrittmaß 2s + a = 59–65 cm ist dennoch anerkannte Regel der Technik und damit werkvertraglich geschuldet.

> **Beispiel 4.4 (Treppe).** Geschosshöhe von Fertigfußboden zu Fertigfußboden 2,90 m:
>
> | Steigungen | Steigung *s* | Auftritt *a* | 2s + a |
> |---|---|---|---|
> | 16 | 18,1 cm | 26,8 cm | 63 cm |
> | 15 | 19,3 cm | 24,3 cm | 63 cm |
>
> Beide Lösungen liegen in den Grenzen. Die Lösung mit 16 Steigungen braucht eine längere Lauflänge (15 · 26,8 cm = 4,01 m gegenüber 14 · 24,3 cm = 3,40 m). Damit berührt die Wahl den Grundriss.
>
> Beispiel B5 (`beispiele/b5_treppe_din18065.py`) listet alle zulässigen Lösungen auf und rangiert sie nach Zielschrittmaß und Platzbedarf.

## 4.5 Energierecht: vom GEG zum GModG

Seit dem 29.07.2026 gilt das Gebäudemodernisierungsgesetz (GModG) [@gmodg2026]. Für Neubauten von Wohngebäuden gelten danach [V]:

- **Primärenergie** höchstens 0,55 × Referenzgebäude (§ 15).
- **Spezifischer Transmissionswärmeverlust** H'T höchstens 1,0 × Referenzgebäude (§ 16).
- **Nachweis** nach DIN V 18599:2018-09 (§ 20) [@din18599].
- **U-Werte** nach DIN 4108-4:2017-03 und DIN EN ISO 6946:2008-04 (§ 20 Abs. 6) [@din4108-4; @iso6946].
- Das **Modellgebäudeverfahren** nach § 31 mit Anlage 5 bleibt als vereinfachter Nachweis erhalten.

Die Umsetzung der EU-Gebäuderichtlinie (EPBD) folgt in einer zweiten Stufe:

- neue Referenzgebäude
- DIN/TS 18599:2025-10
- Bilanzbezugsfläche nach DIN SPEC 91606
- Pflicht zur Lebenszyklus-Ökobilanz
- Nullemissionsgebäude ab 2030

**Folge für die Architektur:** Rechenkerne müssen **versioniert** sein. Ein Entwurf, der heute nach dem Referenzgebäude des GModG geprüft wird, kann in sechs Monaten gegen ein anderes Referenzgebäude laufen. Das System speichert deshalb zu jeder Prüfung das angewandte Regelwerk-Profil samt Version. Die Frage, ob ein Entwurf zulässig ist, hat damit immer die Form „zulässig nach Profil *P* in Version *v*“.

## 4.6 Regeln des Handwerks und der Gütesicherung

Die Regeln des Handwerks gelten nicht bauaufsichtlich, sondern **werkvertraglich**. Sie konkretisieren die „anerkannten Regeln der Technik“ und damit den geschuldeten Erfolg.

**Zimmererhandwerk [V]:** Es gibt zwei Fachregeln:
- 01 Außenwandbekleidungen (03/2023)
- 02 Balkone und Terrassen (12/2020)

Eine Fachregel 03 existiert nicht.

**Dachdeckerhandwerk [V]:** Die Fachregel des ZVDH für Dachziegel und Dachsteine (04/2024) [@zvdh2024] enthält eine R1-Regel, die für den Entwurf zentral ist:
- **Regeldachneigung:** 22° bis 40°, je nach Deckung.
- **Mindestdachneigung:** 10°.
- Wer die Regeldachneigung unterschreitet, braucht Zusatzmaßnahmen in fünf Klassen.
- Weitere erhöhte Anforderungen, etwa bei Sparrenlängen über 10 m oder Schneelasten ab 1,5 kN/m², verschieben die Klasse.

Senkt der Kunde die Dachneigung per Sprache von 35° auf 20°, ändert das also nicht nur die Abstandsfläche, sondern auch Unterdach, Kosten und Deckmaterial.

**Gütesicherung und Qualitätsgemeinschaft [V]:**
- **RAL-GZ 422** „Holzhausbau“ [@ral422]: Überwachung zweimal jährlich im Werk und einmal jährlich auf der Baustelle; unter anderem Holzfeuchte ≤ 18 % und Holzwerkstoffe unter 0,03 ppm Formaldehyd.
- **QDF** [@qdf2022]: 36 Qualitätsversprechen, eine Hausakte ist Pflicht.

Die Pflicht zur Hausakte ist für das Zielbild besonders relevant. Das Modell, das der Kunde zur Übergabe erhält, erfüllt diese Pflicht unmittelbar.

**Folge für die Formalisierung:** Die Regeln lassen sich in Profile schichten, die aufeinander aufbauen und sich verschärfen:

1. öffentliches Recht
2. eingeführte Technische Baubestimmungen
3. anerkannte Regeln der Technik
4. Gütesicherung
5. Herstellerregeln

Die Herstellerregeln haben dabei Vorrang, soweit sie strenger sind. Nie darf eine höhere Schicht eine niedrigere lockern. Diese Eigenschaft lässt sich maschinell prüfen: Jede Regel einer höheren Schicht muss zu einem Lösungsraum führen, der eine Teilmenge des Lösungsraums der tieferen Schicht ist.

## 4.7 Verbrauchervertragsrecht

Der Vertrag über ein Fertighaus ist in der Regel ein **Verbraucherbauvertrag** nach § 650i BGB [@bgb]. Daraus folgen R4-Regeln mit harten zeitlichen Bedingungen.

**Baubeschreibung [V]:** Sie ist dem Verbraucher rechtzeitig **vor** Abgabe seiner Vertragserklärung in Textform zu übergeben (§ 650j BGB). Art. 249 § 2 EGBGB [@egbgb249] verlangt neun Mindestinhalte:

1. Gebäude, Haustyp und Bauweise
2. Leistungsumfang einschließlich Planung und Bauleitung
3. Pläne mit Raum- und Flächenangaben, Ansichten, Grundrisse, Schnitte
4. Energie-, Brand- und Schallschutzstandard sowie Bauphysik
5. Konstruktion aller wesentlichen Gewerke
6. Innenausbau
7. Gebäudetechnik
8. Qualitätsmerkmale
9. Sanitär, Elektro, IT und Außenanlagen

Dazu kommt ein verbindlicher Fertigstellungstermin oder die Bauzeit. Die Baubeschreibung wird Vertragsinhalt; Unklarheiten gehen zulasten des Unternehmers (§ 650k BGB).

**Widerruf [V]:** Der Verbraucher kann 14 Tage widerrufen (§ 650l BGB). Die Frist beginnt erst mit ordnungsgemäßer Belehrung.

Ob die Pflicht zur Baubeschreibung entfällt, wenn der Verbraucher „die wesentlichen Planungsvorgaben“ macht, ist für einen Entwurf innerhalb der Regeln der Firma ungeklärt [U]. Ein verantwortungsvolles System stützt sich auf diese Ausnahme nicht.

**Konsequenz:** Das Modell enthält alle neun Inhalte, weil sie genau die Informationen sind, die ohnehin für Bauantrag und Fertigung gebraucht werden. Die Baubeschreibung ist deshalb eine *Sicht* auf das Modell. Zu dieser Sicht gehören:

- eine Vollständigkeitsprüfung gegen Art. 249 § 2 EGBGB als R2-Regel
- ein Hash des eingefrorenen Vertragsstands
- die Sperre der Produktion bis zum Ablauf der Widerrufsfrist

## 4.8 Querschnittsregelungen

### 4.8.1 Produkthaftung

Mit dem modernisierten Produkthaftungsrecht ist Software einschließlich KI-Systemen ab dem 09.12.2026 ein Produkt [@prodhaftg2026]. Für ein Entwurfssystem folgen daraus drei Anforderungen:

- Die angewandten Regelwerke sind zu versionieren.
- Jede Entscheidung, auch jede Ablehnung, ist in einem Audit-Trail nachvollziehbar zu speichern.
- Die Grenze zwischen Vorschlag der Maschine und Freigabe des Menschen muss dokumentiert sein.

### 4.8.2 KI-Verordnung

Gebäudeentwurf gehört nicht zu den Hochrisiko-Anwendungen nach Anhang III der KI-Verordnung [@aiact2024]. Seit dem 02.08.2026 gelten jedoch die Transparenzpflichten des Art. 50: Nutzer müssen erkennen können, dass sie mit einem KI-System interagieren.

Die hier gewählte Trennung von Absichtserkennung (KI) und Berechnung (Code) erleichtert die Erfüllung dieser Pflicht. Die KI erzeugt keine Planinhalte, sondern wählt nur zwischen typisierten Optionen. Jeder Wert im Modell ist auf eine deterministische Regel zurückführbar.

### 4.8.3 Datenschutz und Barrierefreiheit

**Datenschutz:** Sprachaufnahmen sind personenbezogene Daten. Eine lokale Verarbeitung der Spracherkennung unterstützt Datenschutz durch Technikgestaltung. Gespräche mit Verkaufsberatern dürfen nur mit Einwilligung aller Beteiligten aufgezeichnet werden (§ 201 StGB) [U].

**Barrierefreiheit:** Führt die App zum Abschluss eines Verbrauchervertrags, fällt sie sehr wahrscheinlich unter das Barrierefreiheitsstärkungsgesetz [@bfsg] [U]. Für einen 3D-Editor ist das eine eigene Gestaltungsaufgabe. Die Sprachsteuerung selbst kann hier zu einem Mittel der Barrierefreiheit werden.

## 4.9 Urheberrecht an Normen und die Implementierbarkeit von Regeln

Das Ziel, „nichts zu erfinden“, stößt beim Normenrecht an eine Grenze. Nach § 5 Abs. 3 UrhG bleiben private Normwerke urheberrechtlich geschützt, auch wenn Gesetze auf sie verweisen [@urhg5; @wd2020normen].

Der EuGH hat 2024 entschieden, dass **harmonisierte** Normen Teil des Unionsrechts sind und ein überwiegendes öffentliches Interesse am *Zugang* besteht [@eugh2024publicresource]. Die Frage des Urheberrechts hat er nicht entschieden. Die hier relevanten Normen (DIN 18065, DIN 4108, DIN 4109, DIN 68800) sind zudem nationale und keine harmonisierten Normen [U].

**Befund:** Einzelne Zahlenwerte wie das Schrittmaß von 59 bis 65 cm dürften als technische Fakten kaum schutzfähig sein. Tabellen, Texte und Bilder sind dagegen geschützt [U].

**Folge für die Umsetzung:**

1. Implementiert werden Regeln und Kennwerte mit Normverweis, nicht Normtexte oder Tabellen.
2. Bauteilkennwerte stammen aus frei nutzbaren oder lizenzierten Katalogen (dataholz.eu, Herstellernachweise), nicht aus Normtabellen.
3. Für den kommerziellen Betrieb ist eine Lizenz bei DIN Media und eine rechtliche Prüfung einzuholen.

Die Grenze zeigt, dass „alles ist schon da“ nicht mit „alles ist frei verfügbar“ gleichzusetzen ist. Existenz und Nutzbarkeit einer Regel sind getrennt zu prüfen. Kapitel 7 führt deshalb für jeden Baustein eine Lizenzanalyse.

## 4.10 Zwischenfazit

Der Rechtsrahmen bestätigt das Zielbild in seinem Kern und präzisiert es in drei Punkten:

1. **Der Kunde kann entwerfen, aber nicht verantworten.** Die Verantwortung liegt bei der Firma als Entwurfsverfasserin unter Leitung einer bauvorlageberechtigten Person (Art. 61 Abs. 6 BayBO). Für Gebäudeklasse 1 bis 3 kann das auch ein Zimmerermeister sein. Das System muss diese Freigabe als R3-Gate abbilden.
2. **Das Modell ist nicht die Bauvorlage, aber ihr Garant.** Bayern verlangt PDF-Bauvorlagen. Die Konsistenzforderung des § 13 BauVorlV erfüllt ein System mit einer einzigen Quelle konstruktionsbedingt.
3. **Regeln sind zeitabhängig und geschichtet.** Vollgeschoss nach der Fassung von 2007, GEG → GModG und EC 5 in zwei Generationen: Das Regelwerk braucht Profile mit Version und Geltungszeitraum. Außerdem braucht es eine Schichtung vom öffentlichen Recht bis zur Herstellerregel, in der höhere Schichten nur verschärfen dürfen.

Die in Abschnitt 4.1 eingeführte Taxonomie R1–R4 dient in Kapitel 9 als Gliederung für die Formalisierung.

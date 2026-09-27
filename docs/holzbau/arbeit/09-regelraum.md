# 9 Regelraum

Status: Entwurf v0.1 (27.09.2026). Befunde zur Rechtslage, keine Rechtsberatung. Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle geprüft) oder [U] (unsicher); eigene Bewertungen sind als solche formuliert. Zahlen aus den Beispielen stammen aus `beispiele/ausgabe/` und `beispiele/ergebnisse.md` und sind, wo die Eingaben Beispielwerte sind, als Beispielwerte zu lesen.

## 9.0 Einordnung und Vorgehen

Kapitel 4 hat den Rechtsrahmen nach der Funktion geordnet, die eine Regel im System übernimmt. Daraus entstanden vier Regelklassen: Entwurfsgrenzen (R1), Informationsanforderungen (R2), Verantwortungsregeln (R3) und Formregeln (R4). Kapitel 5 hat gezeigt, dass die Forschung zur automatisierten Regelprüfung fast ausschließlich *nachträglich* prüft und dass eine Regelbasis für deutsches, versioniertes Bauordnungsrecht fehlt (Lücken L2 und L3). Dieses Kapitel schließt an beide Befunde an. Es beantwortet die Forschungsfrage FF2:

> Wie lassen sich öffentlich-rechtliche Regeln, Normen, Handwerksregeln und Herstellerregeln so formalisieren, dass sie einen Laienentwurf in Echtzeit begrenzen und das Ergebnis maschinell prüfbar machen?

Die Antwort hat fünf Teile:

1. **Taxonomie** (9.1): Die Regeln werden nach Quelle und Klasse geordnet. Die Quelle bestimmt Verbindlichkeit und Vorrang, die Klasse bestimmt die Prüftechnik.
2. **Formalisierung** (9.2): R2 wird als IDS formuliert, R1 als ausführbare Regel nach einem einheitlichen Regelschema.
3. **Profile** (9.3): Regeln werden zu versionierten Regelwerk-Profilen mit Geltungszeitraum gebündelt und in Schichten geordnet. Für die Schichtung wird eine formale Eigenschaft angegeben, die Monotonie, mit einem Prüfverfahren.
4. **Beispiele und Ablehnung** (9.4, 9.5): Neun R1-Regeln werden als Listing ausgeführt. Jede Ablehnung trägt eine Begründung und eine Alternative.
5. **Wirkungsweise** (9.6, 9.7): Die Regeln wirken während der Erzeugung (*compliance by construction*) und werden danach unabhängig nachgeprüft. Normwerte werden dabei nur so genutzt, wie es das Urheberrecht erlaubt.

Die Empfehlungsregeln der Klasse R5 (Qualität, Evidenzgrad, Score) behandelt Kapitel 9b. Sie werden hier nur dort erwähnt, wo sie von den harten Regeln abzugrenzen sind. Die Typabhängigkeit der Profile vom Einfamilienhaus bis zum Geschosswohnungsbau folgt in Kapitel 9a.

## 9.1 Taxonomie der Regeln: Quelle und Klasse

### 9.1.1 Sechs Regelquellen

Kapitel 4 unterscheidet die Regeln nach ihrer rechtlichen Herkunft. Für die Formalisierung genügt eine gröbere Einteilung in sechs Quellen. Maßgeblich ist, **warum** eine Regel verbindlich ist, denn davon hängen Vorrang, Abweichungsmöglichkeit und Verantwortung ab.

| Quelle | Beispiele | Geltungsgrund | Abweichung möglich durch |
|---|---|---|---|
| **G Gesetz** (Bund, Land, Ortsrecht) | BayBO, BauNVO, Bebauungsplan, Satzungen nach Art. 81 BayBO, GModG, BGB, TA Lärm als normkonkretisierende Verwaltungsvorschrift | öffentliches Recht bzw. zwingendes Vertragsrecht | nur Behörde (z. B. Abweichung nach Art. 63 BayBO) |
| **N Norm** | eingeführte Technische Baubestimmungen (BayTB), DIN-Normen, VDI-Richtlinien, EC 5 | bauaufsichtlich über die Einführung, sonst als anerkannte Regel der Technik werkvertraglich | eingeführt: wie G; nicht eingeführt: Vereinbarung |
| **H Handwerk** | Fachregeln des Zimmerer- und Dachdeckerhandwerks, Merkblätter, Verlegeregeln | anerkannte Regel der Technik, werkvertraglich geschuldet [@bgb] | Vereinbarung mit Aufklärung |
| **Q Güte** | RAL-GZ 422, QDF-Satzung | privatrechtliche Selbstverpflichtung als Mitglied bzw. Zeichennehmer [@ral422; @qdf2022] | Verband, nicht Kunde |
| **M Hersteller** | Produkt- und Systemregeln (Trockenestrich, R290-Schutzbereich), Firmenregeln (Katalog, Raster, Mindestmaße) | Verwendbarkeit des Produkts; unternehmerische Festlegung | Hersteller bzw. Firma |
| **K Kunde** | vereinbarter Standard (z. B. erhöhter Schallschutz), Budget, Raumprogramm | Vertrag, Baubeschreibung als Vertragsinhalt [@egbgb249] | Kunde, mit Nachtrag |

Zwei Zuordnungen sind nicht selbstverständlich:

- **Satzungen und Bebauungspläne** gehören zu G, sind aber gemeindlich verschieden. Die Regelmaschine braucht deshalb eine Satzungsdatenbank je Gemeinde und keine Pauschale. Das gilt etwa für Stellplätze, die nur mit Satzung geschuldet sind (Recherche 02, 14) [V].
- **Zurückgezogene Normen** leben oft als Firmenregel fort. B6 prüft Mindestbreiten und Mindestflächen je Raumtyp, die der Sache nach aus der zurückgezogenen DIN 18011 stammen. Im Regelwerk stehen sie korrekt als *Projektregel* der Quelle M (`daten/haus_state.json`). Wer sie mit „DIN 18011“ belegen würde, würde eine Verbindlichkeit behaupten, die nicht besteht.

### 9.1.2 Quelle × Klasse

Die Klassen R1–R4 aus Abschnitt 4.1 sind orthogonal zu den Quellen. Jede Quelle kann Regeln jeder Klasse liefern. Die Matrix zeigt je Zelle ein belegtes Beispiel aus den Recherchen.

**Tabelle 9.1: Regelquelle × Regelklasse (Beispiele)**

| Quelle | R1 Entwurfsgrenze | R2 Informationsanforderung | R3 Verantwortung | R4 Form |
|---|---|---|---|---|
| G Gesetz | Abstandsfläche (Art. 6 BayBO), Vollgeschoss, Fensterfläche 1/8 (Art. 45) [@baybo2026] | Gebäudeklasse und Baukosten in der Baubeschreibung (§ 9 BauVorlV) [@bauvorlv] | Bauvorlageberechtigung (Art. 61), Prüfsachverständige (Art. 62a/b) | Bauzeichnungen 1:100 (§ 8 BauVorlV), Baubeschreibung vor Vertragsschluss [@egbgb249] |
| N Norm | Treppe [@din18065], Durchbruch nach EC 5/NA, erf R′w,ges nach DIN 4109-1 | U-Wert als Merkmal nach DIN EN ISO 6946 [@iso6946] | Schallschutznachweis als bautechnischer Nachweis (Art. 62 BayBO, § 12 BauVorlV) | Rundung von L_r in vollen dB nach DIN 1333 [@din1333] |
| H Handwerk | Regeldachneigung und Mindestdachneigung [@zvdh2024], Kleinstück-Regel beim Fliesen | Deckungsart und Unterdachklasse | – | Abrechnung nach ATV DIN 18352 |
| Q Güte | Holzfeuchte ≤ 18 % [@ral422] | Hausakte [@qdf2022] | Fremdüberwachung | – |
| M Hersteller | Mindestbreite Bad 1,70 m (B6), Katalogfenster nur SSK 3/4 (B19), R290-Schutzbereich (B20) | Material „KVH C24“ an jedem Ständer (B2, HRB-05) | Werkfreigabe | BTLx-Export |
| K Kunde | Budget, Raumprogramm, vereinbarter erhöhter Schallschutz | Bemusterungsauswahl | Unterschrift, Widerruf | Textform |

Die Matrix macht zwei Dinge sichtbar. Erstens liegt der Formalisierungsaufwand nicht gleichmäßig. R1-Regeln aus G und N sind wenige, aber geometrisch anspruchsvoll. R1-Regeln aus M sind zahlreich, aber meist einfach. Zweitens ist die Zeile K keine Nebensache. Der Kunde setzt Regeln, die den Lösungsraum oft stärker einschränken als das Baurecht, zum Beispiel ein Budget. Diese Regeln sind aber nicht verbindlich im öffentlich-rechtlichen Sinn und dürfen bei der Freigabe nie mit G oder N verwechselt werden.

### 9.1.3 Folgerung für die Prüftechnik

Die Klasse bestimmt die Technik, die Quelle bestimmt den Umgang mit dem Ergebnis:

- **R1** braucht eine Regelmaschine mit Geometrie- und Rechenfunktionen (9.2.3).
- **R2** lässt sich deklarativ als IDS formulieren (9.2.2).
- **R3 und R4** sind Prozessregeln. Sie werden als Freigabe-Gates und als abgeleitete Exporte mit Vollständigkeitsprüfung umgesetzt (Kapitel 18). Hier interessiert nur ihre Kopplung an R1 und R2.
- Die **Quelle** entscheidet, wer eine Verletzung auflösen darf: bei G und eingeführten N nur eine Behörde, bei H eine aufgeklärte Vereinbarung, bei M die Firma, bei K der Kunde.

## 9.2 Formalisierung

### 9.2.1 Grundbegriffe

Die Formalisierung benutzt wenige Begriffe. Sie sind so gewählt, dass sie sich unmittelbar in Code und in das Nachweisdatenmodell aus Kapitel 7a übersetzen lassen.

- **Entwurfsraum X.** Ein Entwurf ist ein Parametervektor *x* ∈ *X* des Parametermodells (Kapitel 7): Grundriss, Geschosshöhen, Dachform und -neigung, Bauteilaufbauten, Bemusterung.
- **Modell.** Der Generator erzeugt daraus deterministisch ein IFC-Modell *M* = gen(*x*) (Kapitel 8).
- **Kontext c.** Zum Entwurf gehören Daten, die nicht der Kunde bestimmt: Grundstück und Gelände, Bebauungsplan, Gemeinde, Lärmquellen, Stichtage.
- **Regel r.** Eine Regel ist eine Prüffunktion *f_r*(*M*, *c*) mit Ergebnis in einer fünfwertigen Menge.

| Ergebnis | Bedeutung | Folge im System |
|---|---|---|
| **erfüllt** | Die Bedingung gilt. | Entwurf zulässig bezüglich *r* |
| **verletzt** | Die Bedingung gilt nicht. | Ablehnung mit Begründung und Alternative (9.5) |
| **unbestimmt** | Eine Eingangsinformation fehlt. | R2-Befund, Rückfrage oder Nachtrag der Information |
| **nicht anwendbar** | Die Regel gilt für diesen Fall nicht. | keine Folge, aber protokolliert |
| **freigabepflichtig** | Die Frage ist nicht deterministisch entscheidbar. | Freigabe-Knoten für eine berechtigte Person (R3) |

Der Wert **unbestimmt** ist die wichtigste Unterscheidung gegenüber einer zweiwertigen Prüfung. Fehlt etwa das Geländemodell, ist eine Abstandsfläche weder erfüllt noch verletzt. Eine zweiwertige Prüfung müsste sich für eines entscheiden und würde damit entweder einen unzulässigen Entwurf durchlassen oder einen zulässigen ablehnen. Die fünfwertige Logik koppelt R1 an R2: Jede R1-Regel nennt die R2-Anforderungen, deren Erfüllung sie voraussetzt. Der Wert **freigabepflichtig** koppelt R1 an R3. Er ist für Rechtsbegriffe reserviert, die sich einer Rechenregel entziehen, etwa die Doppelhaus-Eigenschaft (Kapitel 9a.2).

Der **Lösungsraum** einer Regel ist die Menge der Entwürfe, für die sie nicht verletzt und nicht unbestimmt ist:

$$L(r) = \{\, x \in X \mid f_r(\mathrm{gen}(x), c) \in \{\text{erfüllt}, \text{nicht anwendbar}\} \,\}$$

Für eine Regelmenge *R* ist $L(R) = \bigcap_{r \in R} L(r)$. Ein Entwurf ist **zulässig nach Profil P**, wenn *x* ∈ *L*(*P*). Diese Schreibweise trägt bis zur Monotonie (9.3.3) und zur Ablehnung (9.5).

### 9.2.2 R2: Informationsanforderungen als IDS

IDS 1.0 ist seit Juni 2024 buildingSMART-Standard [@bsi2024ids; @ids2024]. Eine Spezifikation besteht aus einer Anwendbarkeit (*applicability*) und Anforderungen (*requirements*). Beide werden aus Facetten zusammengesetzt: Entität, Attribut, Merkmal, Klassifikation, Material und Teil-von-Beziehung. Das Beispiel B2 enthält 11 Spezifikationen für ein Holzrahmen-Wandelement (`beispiele/holzrahmenbau.ids`). Listing 9.1 zeigt die erste im Auszug.

**Listing 9.1: IDS-Spezifikation HRB-01 aus B2 (Auszug, gekürzt)**

```xml
<ids:specification name="HRB-01 Außenwand: U-Wert höchstens 0,20 W/(m²K)"
                   ifcVersion="IFC4X3_ADD2" identifier="HRB-01">
  <ids:applicability minOccurs="1" maxOccurs="unbounded">
    <ids:entity><ids:name><ids:simpleValue>IFCWALL</ids:simpleValue></ids:name></ids:entity>
    <ids:property dataType="IFCBOOLEAN">
      <ids:propertySet><ids:simpleValue>Pset_WallCommon</ids:simpleValue></ids:propertySet>
      <ids:baseName><ids:simpleValue>IsExternal</ids:simpleValue></ids:baseName>
      <ids:value><ids:simpleValue>TRUE</ids:simpleValue></ids:value>
    </ids:property>
  </ids:applicability>
  <ids:requirements>
    <ids:property dataType="IFCTHERMALTRANSMITTANCEMEASURE" cardinality="required">
      <ids:propertySet><ids:simpleValue>Pset_WallCommon</ids:simpleValue></ids:propertySet>
      <ids:baseName><ids:simpleValue>ThermalTransmittance</ids:simpleValue></ids:baseName>
      <ids:value>
        <xs:restriction base="xs:double">
          <xs:minExclusive value="0"/><xs:maxInclusive value="0.20"/>
        </xs:restriction>
      </ids:value>
    </ids:property>
  </ids:requirements>
</ids:specification>
```

Das Beispiel zeigt die Arbeitsteilung genau. IDS prüft, **dass** der U-Wert im Modell steht und **dass** er einen Grenzwert einhält. IDS rechnet ihn aber nicht aus. Die Berechnung nach DIN EN ISO 6946 ist eine R1-Rechenregel (B3), deren Ergebnis in `Pset_WallCommon.ThermalTransmittance` geschrieben wird. Die IDS prüft dann die Übergabe.

**Befunde aus B2 [V].** Die Datei „bestanden“ erfüllt alle 11 Spezifikationen. Die absichtlich fehlerhafte Datei scheitert an genau den 6 Spezifikationen mit eingebautem Fehler (HRB-01, 03, 05, 08, 09, 11). Zwei Werkzeugbefunde betreffen die Formalisierung unmittelbar:

1. ifctester 0.8.5 ignoriert das Attribut `identifier`. Die Zuordnung von Befund zu Regel muss deshalb über den Namen laufen, bis das Werkzeug korrigiert ist.
2. Attribut-Facetten werden nicht vom Typ geerbt, Merkmals-Facetten schon. `NominalDiameter` steht deshalb redundant am Exemplar (HRB-08 prüft den Typ, HRB-09 das Exemplar).

Beide Befunde decken sich mit der Werkzeugkritik von Cerovšek und Omar [@cerovsek2025advancing]. Sie zeigen, dass auch eine deklarative Anforderung von der Implementierung des Prüfwerkzeugs abhängt. Das Regelwerk speichert deshalb zu jeder IDS-Prüfung die Werkzeugversion (Kapitel 7a.3).

**Grenze der IDS.** IDS prüft Merkmale einzelner Elemente. Es prüft keine Geometrie und keine Beziehungen, deren Bedingung an einem verbundenen Element hängt [@fischer2024extending; @akbas2025holistic]. Die Anforderung „Die Gefachdämmung jeder *tragenden* Wand ist nichtbrennbar“ lässt sich mit der Teil-von-Facette nur halb ausdrücken: Die Anwendbarkeit kann verlangen, dass die Dämmung Teil einer `IfcWall` ist, aber nicht, dass diese Wand `LoadBearing = TRUE` trägt. Für solche Fälle gibt es zwei Wege. Entweder trägt das Teil das Merkmal selbst, dann wird die Beziehung beim Generieren aufgelöst. Oder die Regel wandert in die Regelmaschine. Kapitel 9a.6 zeigt den Fall an der HolzBauRL.

**Profilabhängige IDS.** Eine IDS-Datei gehört zu einem Regelwerk-Profil und zu einem Reifegrad (Kapitel 11). Für ein Einfamilienhaus der Gebäudeklasse 1 verlangt sie kein `FireRating` an Innenwänden, für ein Mehrfamilienhaus der Gebäudeklasse 4 schon, und zwar aus einem kontrollierten Vokabular (Recherche 14, Abschnitt 5). Die IDS ist damit eine Ableitung des Profils und keine handgepflegte Einzeldatei.

### 9.2.3 R1: ausführbare Regeln und das Regelschema

R1-Regeln brauchen Geometrie und Rechnung. Nach der Klassifikation von Solihin und Eastman liegen sie überwiegend in den oberen Komplexitätsklassen: Sie fragen nicht nur explizite Werte ab, sondern brauchen abgeleitete Geometrie, Topologie oder einen Lösungsnachweis [@solihin2015classification]. Aus der Literatur folgen drei Anforderungen an ihre Darstellung:

- Regeln müssen von der Prüfmaschine getrennt und für Fachleute lesbar sein [@dimyadi2016computerizing; @haeussler2021code].
- Sie müssen an ihre Quelltexte gekoppelt sein, sonst entsteht das „Black-Box“-Problem entkoppelter Regelkopien [@amor2021promise].
- Sie müssen Quellenbezug, Version, Geltungszeitraum und Testfälle tragen, weil es keine autoritative maschinenlesbare Fassung der BayBO gibt (Kapitel 5.2.7) [@idis2021szenarien].

Die Arbeit entwickelt dafür **keine neue Regelsprache** (Kapitel 5.8.2). Sie legt ein **Regelschema** fest: Jede R1-Regel ist ein Datensatz mit acht Feldern. Die Prüffunktion selbst ist versionierter, getesteter Code.

**Tabelle 9.2: Felder des Regelschemas**

| Feld | Inhalt | Bezug |
|---|---|---|
| `id` | stabile Kennung, unabhängig von der Fassung (z. B. `BY.BayBO.6.T`) | Rückverfolgung über Versionen |
| `quelle` | Quelle (G/N/H/Q/M/K), Werk, Fundstelle, **Fassung**, Status [V]/[U] | Feld `regel` in `nachweis.schema.json` (7a.3) |
| `geltung` | Regelwerk-Profil, räumlicher und sachlicher Geltungsbereich, Geltungszeitraum mit Stichtagsregel | 9.3 |
| `vorbedingung` | Anwendbarkeit, Auswahl der geprüften Objekte, Ausnahmen, vorausgesetzte R2-Spezifikationen | RASE [@hjelseth2011capturing] |
| `pruefung` | Typ (Attribut, Rechnung, Geometrie, Topologie, Aufzählung), Funktion mit Version, Parameter mit Normverweis, Auslegungsparameter | [@solihin2015classification] |
| `ergebnis` | fünfwertiger Status, Ist, Grenzwert, Ausnutzung η, maßgebendes Kriterium | Nachweis nach 7a.3 |
| `begruendung` | Textvorlage mit eingesetzten Werten und Quelle | 9.5 |
| `alternative` | Generatoren für Alternativen: Grenzwert, Kompensation, Variante, Schichtwechsel, Freigabeweg | 9.5 |

Das Schema übernimmt bewährte Elemente, ohne sie neu zu erfinden:

- Die Felder `vorbedingung` und `pruefung` entsprechen der RASE-Auszeichnung von Hjelseth und Nisbet. *Applicability* und *Selection* stehen in der Vorbedingung, *Requirement* in der Prüffunktion, *Exception* als Ausnahme in der Vorbedingung [@hjelseth2011capturing].
- Das Feld `geltung` bildet die zeitliche Geltung ab, die LegalRuleML für Rechtsnormen vorsieht [@palmirani2011legalruleml].
- Ausnahmen innerhalb einer Vorschrift werden als Vorrangregeln *innerhalb* einer Regel modelliert, ähnlich der Default-Logik von Catala [@merigoux2021catala]. Ein Beispiel ist Art. 6 Abs. 6 BayBO, nach dem Dachüberstände unter Bedingungen außer Betracht bleiben.
- Die Kombination aus Vorberechnung und Auswertung folgt OpenBIMRL, das MBO2BIM für die Musterbauordnung verwendet [@stepien2023openbimrl; @mbo2bim2023].
- Die Dokumentation von Rechtsauslegung, Informationsbedarf und Umsetzungsentscheidung je Regel entspricht der Regulation Information Matrix aus Wien [@urban2026development].

Neu ist die Verbindung zweier Felder mit der Regel selbst: `begruendung` und `alternative`. Sie machen aus einer Prüfregel eine Regel, die einen Laienentwurf *führen* kann (9.5). Listing 9.2 zeigt das Schema an der Abstandsfläche.

**Listing 9.2: Regelschema am Beispiel der Abstandsfläche (YAML)**

```yaml
id: BY.BayBO.6.T                      # stabil über Fassungen hinweg
version: 0.1.0                        # Version der Implementierung
quelle:
  art: G                              # G | N | H | Q | M | K
  werk: BayBO
  fundstelle: Art. 6 Abs. 4 und 5
  fassung: "ab 2026-05-01"
  status: "[U]"                       # B4: Primärtext nicht abrufbar, Regel nach Recherche 02
klasse: R1
geltung:
  profil: BY-BayBO-2026-05
  raum: Bayern; außerhalb GE/GI; Gemeinde <= 250 000 Einwohner (sonst Abs. 5a)
  zeit: {von: 2026-05-01, bis: null, stichtag: eingang_bauvorlagen}
vorbedingung:
  auswahl: IfcWall mit Pset_WallCommon.IsExternal = TRUE
  ausnahmen: [satzung_art81, dachueberstand_abs6, grenzgarage_abs7]
  r2_voraussetzung: [BY-R2-Gelaende-DGM, BY-R2-Grundstuecksgrenze]
pruefung:
  typ: geometrie
  funktion: abstandsflaeche@1.2       # Code mit Tests, B4
  parameter: {faktor: 0.4, mindesttiefe_m: 3.0, grenzneigung_grad: 70, dachanteil: 1/3}
  auslegung: {giebel_modus: drittel}  # [U] Alternative: voll
ergebnis: nachweis                    # Datenmodell 7a.3
begruendung: >
  Die Abstandsfläche der {wand} ist {T:.2f} m tief (0,4 · H = 0,4 · {H:.2f} m).
  {A:.2f} m² liegen außerhalb des Grundstücks.
alternative:
  - {art: grenzwert,    frei: [haus.x, haus.y]}             # Verschieben
  - {art: kompensation, frei: [dach.neigung, wand.hoehe]}   # H verkleinern
  - {art: freigabe,     weg: "Abweichung Art. 63 BayBO (Behörde)"}
```

Drei Einzelheiten des Listings verdienen eine Begründung.

**Auslegungsparameter statt verdeckter Entscheidung.** Wie die Giebelfläche nach der Novelle 2021 genau zu bemessen ist, konnte in B4 nicht am Gesetzestext geprüft werden [U]. B4 rechnet deshalb beide Lesarten. In der Lesart „drittel“ ergibt sich die gestauchte Giebelform mit 30,53 m², in der Lesart „voll“ sind es 36,40 m². Das Schema macht diese Unsicherheit zu einem sichtbaren Parameter mit Status [U]. Die bauvorlageberechtigte Person legt ihn im Profil fest und verantwortet damit die Auslegung, statt dass sie im Code verborgen bleibt.

**Parameter als Daten, Funktion als Code.** Die Kennwerte 0,4, 3 m und 70° stehen im Datensatz, nicht im Code. Ändert eine Novelle nur einen Kennwert, entsteht eine neue Profilversion ohne neue Funktion. Ändert sie das Verfahren, entsteht eine neue Funktionsversion (`abstandsflaeche@1.2`). Beides bleibt unterscheidbar.

**Vorausgesetzte R2-Spezifikationen.** Fehlt das Geländemodell, liefert die Regel **unbestimmt**, nicht verletzt. Der Kunde erfährt, welche Information fehlt. Die Regelmaschine erfindet keinen Ersatzwert.

### 9.2.4 R3 und R4 im Regelschema

R3- und R4-Regeln sind keine Prüffunktionen über das Modell, aber sie hängen an R1- und R2-Ergebnissen. Das Regelschema bildet diese Kopplung über zwei Mechanismen ab:

- **Freigabepflichtiges Ergebnis.** Eine R1-Regel kann statt *erfüllt* oder *verletzt* **freigabepflichtig** liefern. Dann entsteht ein Freigabe-Knoten mit der Rolle, die ihn auflösen darf. Welche Rolle das ist, hängt vom Gebäudetyp ab (Kapitel 9a.4). Im IFC wird er als `IfcApproval` abgebildet (Kapitel 18).
- **Vollständigkeitsprüfung als R2.** R4-Regeln verlangen Inhalte in einer Form. Die Inhalte prüft eine R2-Spezifikation, etwa die neun Mindestinhalte der Baubeschreibung nach Art. 249 § 2 EGBGB [@egbgb249]. Die Form entsteht als Ableitung (Kapitel 4.7, 18).

## 9.3 Regelwerk-Profile: Version, Geltungszeitraum und Schichtung

### 9.3.1 Der Begriff des Profils

Kapitel 4 hat festgestellt, dass die Frage nach der Zulässigkeit immer die Form „zulässig nach Profil *P* in Version *v*“ hat. Ein **Regelwerk-Profil** ist ein Tupel

$$P = (\mathit{id},\ v,\ [t_\text{von}, t_\text{bis}),\ \sigma,\ (S_1, \dots, S_n),\ \Theta)$$

mit Kennung, Version, Geltungszeitraum, Stichtagsregel σ, einer geordneten Folge von Schichten *S_k* (Regelmengen) und den Parametern Θ der Regeln. Profile sind unveränderlich. Jede Änderung erzeugt eine neue Version. Die Nachweise tragen Profilname und Version bereits heute, zum Beispiel `BY-BayBO-2026-05` in Version 0.1.0 für B4 und `DE-DIN18065-WG2WE` für B5 (`ausgabe/nachweise/`).

Die **Stichtagsregel σ** ist der unterschätzte Teil. Sie legt fest, welches Datum über die anzuwendende Fassung entscheidet. Die Beispiele zeigen, dass es nicht ein Stichtag ist, sondern mehrere:

| Regelbereich | maßgeblicher Stichtag | Beleg |
|---|---|---|
| Festsetzungen des Bebauungsplans, Vollgeschoss | Fassung, auf die der Bebauungsplan verweist | Art. 83 Abs. 6 BayBO; Recherche 02 [V] |
| Bauordnungsrecht, Technische Baubestimmungen | Einleitung des Verfahrens bzw. Eingang der Bauvorlagen; Übergangsregeln der Einführung | HolzBauRL: Übergang nach Einleitungsdatum (Recherche 14) [V] |
| Energierecht | Antrag bzw. Bauanzeige nach den Übergangsregeln des GModG | [@gmodg2026] [U für die Einzelheiten] |
| anerkannte Regeln der Technik | Abnahme, nicht Vertragsschluss | werkvertragliche Rechtsprechung [U] |
| Vertrag, Baubeschreibung | Vertragsschluss (eingefrorener Stand mit Hash) | Kapitel 4.7 |

Der Stichtag der anerkannten Regeln der Technik ist mit [U] markiert, weil er hier nicht an der Rechtsprechung geprüft wurde. Er ist für die Architektur trotzdem bedeutsam: Wenn er bei der Abnahme liegt, muss ein Profil, das bei Vertragsschluss eingefroren wurde, gegen spätere Fassungen *nachgeprüft* werden können. Das Profil wird dann nicht getauscht, sondern ein Delta-Bericht erzeugt.

### 9.3.2 Versionierung an fünf Fällen

Fünf Fälle aus den Recherchen zeigen, warum Profile Version und Geltungszeitraum brauchen. Jeder Fall steht für ein anderes Muster.

**Fall 1: Ersetzung eines Gesetzes (GEG → GModG).** Seit dem 29.07.2026 gilt das Gebäudemodernisierungsgesetz [@gmodg2026]. Die 65-%-Pflicht für erneuerbare Energien ist entfallen (Recherche 02, 08) [V]. Für die Regelmaschine ist das ein **harter Schnitt mit Übergang**: Ein Profil `DE-GEG` endet, ein Profil `DE-GModG-2026-07` beginnt. Die EPBD-Umsetzung mit neuen Referenzgebäuden folgt in einer zweiten Stufe (Kapitel 4.5). Deshalb ist schon jetzt ein drittes Profil absehbar.

**Fall 2: Datierter Verweis auf eine ältere Normausgabe (ISO 6946).** § 20 Abs. 6 GModG verweist **datiert** auf DIN EN ISO 6946:2008-04 [@iso6946]. Die aktuelle Ausgabe ist DIN EN ISO 6946:2018-03 auf Grundlage der ISO 6946:2017 [@iso6946_2017]. B3 rechnet nach der Ausgabe 2018-03, und der Nachweis nennt sie korrekt (Kapitel 7a.5). Für einen öffentlich-rechtlichen Nachweis nach GModG wäre aber die Ausgabe 2008-04 maßgeblich. **Die neueste Fassung ist nicht die geltende Fassung.** Ein Profil muss deshalb je Zweck eine Fassung wählen können: 2008-04 für den GModG-Nachweis, 2018-03 für den werkvertraglichen Stand der Technik. Ob sich die Ergebnisse für den Holzrahmenbau unterscheiden, ist in dieser Arbeit nicht quantifiziert [U]. Die Architektur muss den Unterschied aber abbilden können, bevor man weiß, ob er zählt.

**Fall 3: Zwei Normgenerationen nebeneinander (EC 5).** DIN EN 1995-1-1:2026-09 ist erschienen [@en1995-2026]. Bauaufsichtlich eingeführt ist weiter die Fassung 2010-12 mit A2:2014 und nationalem Anhang (BayTB 11/2025) [@baytb2025]. Die Rücknahme der alten Fassung wird für etwa 03/2028 erwartet (Recherche 02) [V]. Für mindestens eineinhalb Jahre existieren also **zwei gültige Profile parallel**. B15 zeigt die praktische Folge: Nach dem nationalen Anhang sind unverstärkte Durchbrüche bis *h_d* ≤ 0,15 *h* zulässig. Nach dem Entwurf der neuen Generation müssen Durchbrüche in Vollholz und KVH verstärkt werden, unverstärkt nur in BSH und LVL [V Entwurf, U Endfassung]. B15 prüft nach dem eingeführten Profil und gibt die neue Regel als Hinweis aus. Das ist die richtige Form: Das eingeführte Profil entscheidet, das kommende Profil warnt.

**Fall 4: Novellen einer Landesbauordnung (BayBO).** Die BayBO wurde seit 2021 mehrfach geändert. Die Recherchen belegen unter anderem:

- Seit der Novelle 2021 gelten Giebelflächen als normale Wände (Abstandsfläche, Kapitel 4.3.1).
- Seit 01.01.2025 lösen Wärmepumpen und ihre Einhausungen bis 2 m Höhe keine Abstandsflächen aus (Art. 6 Abs. 1 Satz 3 Nr. 4) (Recherche 22) [V].
- Seit 01.10.2025 sind Stellplätze nur mit Gemeindesatzung geschuldet (Recherche 02) [V].
- Die Fassung ab 01.05.2026 liegt den Recherchen zugrunde [@baybo2026]. Den Inhalt der Änderung vom 23.04.2026 hat Recherche 02 nicht geprüft [U].

Jede dieser Änderungen betrifft eine andere Regel. Das Muster ist die **regelweise Änderung** innerhalb eines fortbestehenden Gesetzes. Das Profil versioniert deshalb nicht das Gesetz als Ganzes, sondern jede Regel mit eigenem Geltungszeitraum.

**Fall 5: Fortgeltung einer historischen Fassung (Vollgeschoss 2007).** Die BauNVO verweist für das Vollgeschoss auf das Landesrecht [@baunvo]. In Bayern gilt über Art. 83 Abs. 6 BayBO die Definition des Art. 2 Abs. 5 in der bis 31.12.2007 geltenden Fassung fort [@baybo2026] [V]. Für ältere Bebauungspläne kann eine noch ältere Fassung maßgeblich sein (Kapitel 4.3.2). Das Muster ist die **Bindung an das Datum eines anderen Rechtsakts**. Die Stichtagsregel σ lautet hier nicht „heute“, sondern „Datum des Bebauungsplans“. Das Profil braucht deshalb das Datum des Bebauungsplans als Eingabe, und das XPlanung-Schema trägt es [@xplanung].

Ein sechster Fall zeigt, dass Versionierung auch Kennwerte in Datensätzen betrifft. B14 verwendet für die Rohrüberdeckung von Calciumsulfat-Fließestrich CAF-F4 den Wert ≥ 40 mm. Er ist im Eingabedatensatz mit „Fassung 2004, von Herstellern 2023 weiter genannt“ belegt. Ob DIN 18560-2:2022-08 ihn unverändert übernimmt, ist nur über Sekundärquellen belegt [U] (Recherche 16). Der Kennwert trägt damit seine eigene Fassung, auch wenn das Profil die Norm in der Ausgabe 2022 führt. Ohne diese Angabe wäre die Abweichung unsichtbar.

**Tabelle 9.3: Muster der Versionierung**

| Muster | Fall | Umsetzung im Profil |
|---|---|---|
| Ersetzung mit Übergang | GEG → GModG | Profil endet, Nachfolgeprofil beginnt; Stichtagsregel nach Übergangsvorschrift |
| datierter Verweis | ISO 6946:2008 im GModG | Fassungswahl je Zweck (öffentlich-rechtlich / werkvertraglich) |
| Parallelgeltung | EC 5 2010 + A2 / 2026 | eingeführtes Profil entscheidet, kommendes Profil warnt |
| regelweise Änderung | BayBO-Novellen | Geltungszeitraum je Regel statt je Gesetz |
| Bindung an fremdes Datum | Vollgeschoss 2007 | Stichtag = Datum des Bebauungsplans |
| Kennwert mit eigener Fassung | Rohrüberdeckung CAF-F4 | Fassung und Status am Kennwert |

Aus den Mustern folgt eine technische Regel: Das Ergebnis einer Prüfung ist nur mit Profil-ID, Profilversion, Funktionsversion und Hash des geprüften Modells reproduzierbar. Kapitel 7a.5 speichert genau diese Angaben im Nachweisheft. Wird ein eingefrorener Entwurf später gegen ein neues Profil geprüft, entsteht ein **Delta-Bericht**: welche Regeln neu verletzt sind, welche nicht mehr, und welche nur ihren Kennwert geändert haben.

### 9.3.3 Schichtung und Monotonie

Kapitel 4.6 hat eine Schichtung der Regeln vom öffentlichen Recht bis zur Herstellerregel eingeführt und gefordert, dass eine höhere Schicht eine niedrigere nie lockern darf. Dieser Abschnitt macht die Forderung präzise und gibt ein Prüfverfahren an.

**Schichten.** Ein Profil ordnet seine Regeln in sechs Schichten:

1. *S*₁ öffentliches Recht (G)
2. *S*₂ eingeführte Technische Baubestimmungen (N, eingeführt)
3. *S*₃ anerkannte Regeln der Technik (N nicht eingeführt, H)
4. *S*₄ Gütesicherung (Q)
5. *S*₅ Hersteller und Firma (M)
6. *S*₆ Kundenvereinbarung (K)

Der Lösungsraum bis zur Schicht *k* ist $L_k = \bigcap_{j \le k} L(S_j)$.

**Definition 9.1 (Monotonie).** Ein Profil ist *monoton*, wenn für alle *k* > 1 gilt: $L_k \subseteq L_{k-1}$.

Wertet die Maschine alle Schichten konjunktiv aus, ist die Monotonie trivial erfüllt, denn ein Schnitt kann nicht größer werden. Die Eigenschaft wird erst dann zu einer echten Forderung, wenn eine höhere Schicht eine Regel der tieferen Schicht **überschreibt**, statt sie zu ergänzen. Das ist in der Praxis der Normalfall. Die Holzfeuchte ist das Standardbeispiel: DIN 68800-2 nennt ≤ 20 % [@din68800-2], RAL-GZ 422 ≤ 18 % [@ral422]. Implementiert wird sinnvollerweise *ein* Parameter `holzfeuchte_max`, den die Güteschicht auf 18 % setzt. Genau an dieser Stelle kann eine Lockerung entstehen. Setzt eine Firmenregel versehentlich 22 %, würde sie bei überschreibender Auswertung die Norm aufheben.

**Definition 9.2 (Regelfamilie mit Richtung).** Eine *Regelfamilie* ρ ist eine Regel mit Parameter θ aus einer geordneten Menge (Θ, ⪯), sodass aus θ ⪯ θ′ stets $L(\rho_\theta) \subseteq L(\rho_{\theta'})$ folgt. θ ⪯ θ′ heißt „θ ist mindestens so streng wie θ′“. Für eine Obergrenze ist ⪯ die Ordnung ≤, für eine Untergrenze ≥, für ein zulässiges Intervall die Inklusion ⊆, für eine zulässige Menge ebenfalls ⊆.

**Satz 9.1.** Jede Schicht *S_k* enthalte (a) neue Regeln, die konjunktiv hinzukommen, und (b) Überschreibungen von Parametern θ_k bestehender Regelfamilien. Gilt für jede Überschreibung θ_k ⪯ θ_{k−1}, so ist das Profil monoton.

*Beweis.* Für (a) folgt die Inklusion aus der Schnittbildung. Für (b) folgt aus θ_k ⪯ θ_{k−1} nach Definition 9.2, dass $L(\rho_{\theta_k}) \subseteq L(\rho_{\theta_{k-1}})$. Da alle übrigen Regeln der Schicht *k* − 1 unverändert bleiben oder weiter eingeschränkt werden, gilt $L_k \subseteq L_{k-1}$. Induktion über *k* liefert die Aussage für alle Schichten. □

Der Satz ist einfach. Sein Wert liegt darin, dass er die Prüfung von einer Aussage über unendliche Lösungsräume auf eine Aussage über **endlich viele Parametervergleiche** zurückführt. Daraus ergibt sich ein dreistufiges Prüfverfahren.

**Stufe 1: Parametervergleich beim Laden des Profils.** Jede Regelfamilie trägt im Schema ihre Richtung (`max`, `min`, `intervall`, `menge`). Beim Laden prüft das System für jede Überschreibung θ_k ⪯ θ_{k−1}. Ein Verstoß ist ein Ladefehler des Profils, kein Befund am Entwurf. Listing 9.3 zeigt den Kern.

**Listing 9.3: Monotonieprüfung beim Laden eines Profils (Pseudocode)**

```python
STRENGER = {
    "max":       lambda neu, alt: neu <= alt,
    "min":       lambda neu, alt: neu >= alt,
    "intervall": lambda neu, alt: alt.lo <= neu.lo and neu.hi <= alt.hi,
    "menge":     lambda neu, alt: set(neu) <= set(alt),
}

def pruefe_monotonie(profil):
    befunde = []
    for k, schicht in enumerate(profil.schichten[1:], start=1):
        for ueb in schicht.ueberschreibungen:          # (familie, parameter, wert)
            alt = profil.parameter_bis(k - 1, ueb.familie, ueb.parameter)
            richtung = profil.familie(ueb.familie).richtung[ueb.parameter]
            if not STRENGER[richtung](ueb.wert, alt):
                befunde.append((schicht.name, ueb, alt))   # Lockerung
    return befunde    # leer ⇒ monoton nach Satz 9.1

# Beispiel: holzfeuchte_max  N: 20 %  →  Q: 18 %  ✓ ;  M: 22 %  ✗ (Ladefehler)
```

**Stufe 2: Aufzählung für Regeln ohne gemeinsamen Parameter.** Manche Regeln einer höheren Schicht sind keine Parameterüberschreibung, sondern eine andere Funktion über denselben Gegenstand. Beispiele sind eine Firmenregel „nur geradläufige Treppen mit 16 bis 18 Steigungen“ gegenüber DIN 18065 oder die Kleinstück-Regel beim Fliesen. Hier ist die Inklusion nicht syntaktisch prüfbar. Für diskrete, kleine Suchräume lässt sie sich aber durch vollständige Aufzählung zeigen. B5 zählt für eine Geschosshöhe von 2,90 m und eine Laufbreite von 0,90 m alle 68 zulässigen Treppenlösungen nach DIN 18065 auf. Jede Firmenregel über denselben Suchraum lässt sich gegen diese Menge prüfen. Pinto et al. haben gezeigt, dass eine vollständige Aufzählung auch bei sehr großen Räumen praktikabel ist und Fehler findet, die Stichproben übersehen: Sie prüften über 292 Milliarden Eingabekonfigurationen eines Prüfwerkzeugs und fanden Abweichungen in 8,26 % des Definitionsbereichs [@pinto2026exhaustive]. Für kontinuierliche Räume ersetzt eine Rasterung mit Randfällen die Aufzählung. Sie liefert dann keinen Beweis, sondern einen Test.

**Stufe 3: konjunktive Auswertung zur Laufzeit.** Unabhängig von Stufe 1 und 2 wertet die Prüfschicht jeden Entwurf gegen **alle** Schichten aus, nicht nur gegen die strengste. Damit ist ein zugelassener Entwurf auch dann zulässig nach *S*₁ und *S*₂, wenn Stufe 1 oder 2 einen Fehler übersehen hat. Die Stufen 1 und 2 sichern dann nicht die Zulässigkeit, sondern die **Richtigkeit der Begründung**: Ohne Monotonie könnte die Ablehnung auf eine Firmenregel verweisen, obwohl in Wahrheit die Bauordnung verletzt ist, oder umgekehrt.

**Kontrollierte Nicht-Monotonie.** Drei Mechanismen durchbrechen die Monotonie absichtlich. Sie sind gerade deshalb explizit zu modellieren:

| Mechanismus | betroffene Schichten | Wer entscheidet | Abbildung |
|---|---|---|---|
| Abweichung nach Art. 63 BayBO | *S*₁, *S*₂ | Bauaufsicht, bei Bescheinigung durch Prüfsachverständige ohne Zulassung (Art. 63 Abs. 1 Satz 3) | Freigabe-Knoten; Regel bleibt, Status „abweichend zugelassen“ |
| vertraglich vereinbarter Standard (Gebäudetyp E, Kapitel 9a.7) | nur *S*₃ | Kunde nach Aufklärung in Textform | Schalter im Profil; nie für *S*₁, *S*₂ |
| Aufhebung einer eigenen Firmenregel | *S*₅ | Firma | Freigabe-Knoten; z. B. Fremdprodukt statt Katalogfenster (B19) |

Formal wird dafür eine Menge *W* ausgesetzter Regeln eingeführt, jede mit Freigabe-Datensatz. Der wirksame Lösungsraum ist $L^W = \bigcap_{r \notin W} L(r)$. Die Nebenbedingung lautet: *W* ∩ (*S*₁ ∪ *S*₂) = ∅, außer die Freigabe stammt von einer Behörde. Diese Bedingung ist maschinell prüfbar. Sie verhindert, dass ein Kundenwunsch oder eine Vertriebsentscheidung stillschweigend eine Mindestanforderung der Bauordnung aufhebt.

## 9.4 Beispiele: neun R1-Regeln

Die folgenden Listings zeigen neun R1-Regeln aus fünf Quellen. Jedes Listing nennt Vorbedingung, Prüffunktion, Ergebnis und die Art der Alternative. Die Kennwerte stammen aus den Recherchen und den Beispielen. Normwerte sind als Einzelkennwerte mit Verweis angegeben (9.7). Tabelle 9.4 ordnet die Regeln vorab ein.

**Tabelle 9.4: Übersicht der Beispielregeln**

| Nr. | Regel | Quelle | Prüftyp | Beleg | Status |
|---|---|---|---|---|---|
| 1 | Abstandsfläche | G: BayBO Art. 6 | Geometrie | B4 | lauffähig |
| 2 | Vollgeschoss | G: BayBO Art. 2 Abs. 5 a. F. | Geometrie, Fläche | – | Regel spezifiziert |
| 3 | Treppe | N: DIN 18065 | Aufzählung | B5 | lauffähig |
| 4 | Fensterfläche | G: BayBO Art. 45 | Rechnung | – | Regel spezifiziert |
| 5 | Dachneigung | H: ZVDH-Fachregel | Tabelle, Rechnung | – | Regel spezifiziert |
| 6 | Fußbodenaufbau | N, M: DIN 18560-2, Systemregeln | Optimierung | B14 | lauffähig |
| 7 | Durchbruch | N: EC 5 mit NA | Geometrie, Rechnung | B15 | lauffähig |
| 8 | Außenlärm | N: DIN 4109-1/-2, BayTB | Rechnung, Auswahl | B19 | lauffähig |
| 9 | Wärmepumpe | G, N, M: TA Lärm, ISO 9613-2, Herstellerangaben | Geometrie, Rechnung, Raster | B20 | lauffähig |

### 9.4.1 Abstandsfläche (BayBO Art. 6)

```text
REGEL BY.BayBO.6.T                               [G, R1, Profil BY-BayBO-2026-05, U]
FÜR   jede Außenwand w
H(w)  := Wandhöhe(w) + a · Dachhöhe(w),  a = 1/3 bei Dachneigung ≤ 70°, sonst 1
T(w)  := max(0,4 · H(w); 3,00 m)                  # Giebel: T(u) entlang der Giebelform
AF(w) := Rechteck bzw. gestauchte Giebelform der Tiefe T vor w
ZUL   := Grundstück ∪ halbe Breite angrenzender öffentlicher Verkehrsflächen
PRÜFE Fläche(AF(w) \ ZUL) = 0
ALTERNATIVE  grenzwert: Verschiebung, bis Fläche = 0;  kompensation: Dachneigung, Wandhöhe
```

> **Beispiel 9.1.** B4: Haus 10 × 12 m auf einem Grundstück von 20 × 30 m, Wandhöhe 6,50 m, Satteldach 45°, Dachhöhe 5,00 m. Es ergibt sich *H* = 6,50 + 5,00/3 = 8,17 m und *T* = 3,27 m. In der Lage „mittig“ ist der Entwurf zulässig. In der Lage „zu nah“ (Abstand 2,00 m zur Westgrenze) liegen **15,20 m²** der Abstandsfläche außerhalb des Grundstücks. Die Grenzwert-Alternative ist unmittelbar ablesbar: Das Haus muss um 1,27 m nach Osten rücken.

### 9.4.2 Vollgeschoss (BayBO Art. 2 Abs. 5 in der Fassung bis 31.12.2007)

```text
REGEL BY.BayBO.2-5.a.F.2007.Vollgeschoss         [G, R1, Stichtag = Datum B-Plan, V]
FÜR   jedes Geschoss g
VOLL(g) := g liegt vollständig über der Geländeoberfläche
           ∧ Fläche{p ∈ g | lichte_höhe(p) ≥ 2,30 m} ≥ 2/3 · Grundfläche(g)
KELLER(g) zählt, wenn mittel(UK Decke − Gelände) ≥ 1,20 m
PRÜFE Anzahl{g | VOLL(g)} ≤ Z                      # Z aus dem Bebauungsplan
VORAB bei Intent kniestock_aendern:
      k* := kleinster Kniestock mit Fläche(h ≥ 2,30) = 2/3 · Grundfläche   # monoton, Bisektion
      melde k* als Grenzwert, bevor die Änderung angewandt wird
ALTERNATIVE  grenzwert: Kniestock < k*;  variante: Dachneigung, Gaubenbreite
```

Die Regel ist in B6 noch nicht implementiert. Sie ist hier vollständig spezifiziert, weil sie die Kopplung zwischen Dachgeometrie und Planungsrecht am deutlichsten zeigt (Beispiel 4.2). Weil die lichte Höhe mit dem Kniestock monoton wächst, existiert der Grenzwert *k** eindeutig und ist durch Bisektion schnell zu finden.

### 9.4.3 Treppe (DIN 18065, Wohngebäude mit höchstens zwei Wohnungen)

```text
REGEL DE.DIN18065.WG2WE                          [N, R1, nicht bauaufsichtlich eingeführt, V]
SUCHRAUM n ∈ ℕ Steigungen, s = Geschosshöhe / n,  a ∈ Raster 5 mm
ZULÄSSIG ⇔ 140 ≤ s ≤ 200 mm ∧ 230 ≤ a ≤ 370 mm ∧ 590 ≤ 2s + a ≤ 650 mm
           ∧ Laufbreite ≥ 800 mm ∧ Lauflänge (n − 1) · a ≤ verfügbar
LÖSUNG   vollständige Aufzählung, lexikografisch sortiert:
         |2s + a − 630| (Toleranz 2,5 mm) → |a − s − 120| → |a + s − 460| → Lauflänge
ALTERNATIVE  grenzwert: kleinste zulässige Laufbreite; variante: nächstbeste Lösung
```

> **Beispiel 9.2.** B5, Geschosshöhe 2,90 m, Laufbreite 0,90 m: 68 zulässige Lösungen. Die beste hat 17 Steigungen à 170,6 mm und Auftritte von 290 mm (2*s* + *a* = 631,2 mm, Lauflänge 4,64 m). Ist die Lauflänge auf 4,0 m begrenzt, wird 16 × 181,25 mm / 265 mm gewählt. Bei 0,75 m Laufbreite gibt es **keine** Lösung. Die Ablehnung nennt dann den Grenzwert 0,80 m.

Die Toleranz von 2,5 mm auf das Zielschrittmaß ist eine bewusste Entwurfsentscheidung. Ohne sie hätten Rundungsreste eine Treppe mit 20 Steigungen und 6,46 m Lauflänge auf Rang 1 gesetzt (`ergebnisse.md`). Das zeigt, dass auch die *Auswahl* unter zulässigen Lösungen eine Regel ist. Sie gehört aber zu R5 bzw. zur Zielfunktion, nicht zu R1.

### 9.4.4 Fensterfläche (BayBO Art. 45)

```text
REGEL BY.BayBO.45.Fensterflaeche                  [G, R1, V; Maßbezug U]
FÜR   jeden Aufenthaltsraum r (IfcSpace mit Nutzung Aufenthalt)
PRÜFE Σ Fensterfläche(r) ≥ Netto-Grundfläche(r) / 8
AUSLEGUNG fenstermass ∈ {rohbaumass, lichtes_mass}      # im Profil festgelegt [U]
HINWEIS (R5, Kap. 9b): Tageslichtquotient ≥ 0,9 % im Mittel nach DIN 5034-1
ALTERNATIVE  grenzwert: fehlende Fensterfläche in m²; variante: zweites Fenster, Dachfenster
```

> **Beispiel 9.3.** Ein Kinderzimmer mit 14,0 m² braucht mindestens 1,75 m² Fensterfläche (Beispiel 4.3). Die Regel ist notwendig, aber nicht hinreichend für gute Tageslichtversorgung [@din5034-1]. Die Trennung in R1 (Art. 45) und R5 (Tageslichtquotient) verhindert, dass eine Qualitätsempfehlung als Rechtsgrenze erscheint.

### 9.4.5 Dachneigung (Fachregel des ZVDH für Dachziegel und Dachsteine, 04/2024)

```text
REGEL DE.ZVDH.DZ.2024-04.Dachneigung               [H, R1, Kennwerte V über Herstellerbroschüren]
EINGABE Deckung d → Regeldachneigung RDN(d) ∈ {22°, 25°, 30°, 35°, 40°}
        erhöhte_anforderung := Sparrenlänge > Grenze(DN) ∨ Schneelast ≥ 1,5 kN/m² ∨ Windzone 4 ∨ …
PRÜFE  DN ≥ 10°                                    # Mindestdachneigung, sonst verletzt
FALLS  DN < RDN(d):  Zusatzmaßnahme K := Klasse(RDN(d), DN, erhöhte_anforderung)
       # z. B. RDN 30°: DN ≥ 18° → K2 (ohne) / K1 (mit erhöhter Anforderung)
       #                DN ≥ 22° → K3/K2;  ≥ 26° → K4/K3;  ≥ 30° → K5/K4
FOLGE  Unterdach nach Klasse K, Kosten, Materialliste (Kopplung an Kap. 14)
ALTERNATIVE  variante: Deckung mit kleinerer RDN;  grenzwert: DN für nächstschwächere Klasse
```

> **Beispiel 9.4.** Der Kunde senkt die Dachneigung eines Doppelmuldenfalzziegels (RDN 30°) von 35° auf 20° (Kapitel 4.6). Die Regel liefert nicht *verletzt*, sondern *erfüllt mit Zusatzmaßnahme* der Klasse K2, bei erhöhten Anforderungen K1. Erst unter 10° wäre die Deckung unzulässig. Zugleich ändern sich Abstandsfläche (9.4.1) und Vollgeschoss (9.4.2).

Die Klassen gelten seit 04/2024 nur noch von 1 bis 5; die frühere Klasse 6 ist entfallen (Recherche 09) [V]. Der Volltext der Fachregel ist kostenpflichtig [@zvdh2024]. Die Regeltabelle trägt deshalb je Wert eine Fundstelle und die Herkunft des Belegs (9.7).

### 9.4.6 Fußbodenaufbau mit gleicher Fertigfußbodenhöhe (B14)

```text
REGEL DE.Fussboden.OKFF-gleich                   [N + M, R1, Kennwerte mit Normverweis]
GEGEBEN je Raum: Rohdecke, Ziel-Aufbauhöhe H (gleich je Geschoss), Belag, Leitungen, FBH
DISKRET   Handelsdicken, Wabe 30/60 mm, bis zu 2 Dämmlagen, optionale Schichten → Kombinationen
STETIG    nivellierende Schichten in [lo, hi]; Σ = Resthöhe  ⇒  exakt: „Füllen nach Stückkosten“
HART      Estrich-Mindestdicke + Rohrüberdeckung (DIN 18560-2: CT-F4 ≥ 45, CAF-F4 ≥ 40 mm [U])
          ∧ Leitungen überdeckt ∧ Zusammendrückbarkeit ∧ U-Wert ∧ Flächenmasse ∧ Beschwerung
          ∧ Toleranzkette über Nivellierhorizont ≤ ±2 mm ∧ Trockenestrich nur mit Ausgleich
WEICH     R_λ,B ≤ 0,15 m²K/W, Belag-Untergrund-Eignung, Belegreife, Übergänge → Hinweis
ZIEL      min w_m · Masse + w_k · Kosten + w_l · Lagen  (deterministischer Gleichstand)
SONST     Konflikt erklären: erreichbares [H_min, H_max], häufigste Ausschlussgründe
```

> **Beispiel 9.5.** B14 erreicht in beiden Varianten (Bodenplatte 210 mm nass, Holzbalkendecke 160 mm trocken) die Ziel-OKFF in allen vier Räumen auf den Millimeter. Die Übergänge sind kantenfrei (ungünstigster Fall 1,6 mm). Im Raum „Wohnen“ der Variante A wurden 361 Kandidaten verworfen: 318 wegen zu großer Höhe, 27 wegen zu kleiner Höhe, 16 wegen des U-Werts. Ohne Absenkung der Bodenplatte gibt es für das Bad **keinen** zulässigen Aufbau (9.5).

B14 zeigt, dass eine R1-Regel nicht immer ein Prädikat über einem fertigen Entwurf ist. Sie kann ein Lösungsverfahren sein, das den Entwurf erst erzeugt (9.6). Die harten Regeln stammen aus zwei Schichten: die Estrichdicken aus der Norm (*S*₃), die Trockenbauregeln aus den Systemregeln der Hersteller (*S*₅). Nach Recherche 16 entscheiden im Holzbau die Hersteller- und Firmenregeln, nicht die DIN.

### 9.4.7 Durchbruch in Holzbalken (DIN EN 1995-1-1 mit NA, B15)

```text
REGEL DE.EC5-NA.NA67.Durchbruch                  [N, R1, Profil EC5-2010+A2 eingeführt, V Sekundär]
FÜR   jede Leitung l, die einen Balken der Höhe h kreuzt, Öffnungsmaß d
FALLS d ≤ 50 mm:  Querschnittsschwächung → Nettoquerschnitt nachweisen
SONST Durchbruch, unverstärkt zulässig nur wenn
      h_d ≤ 0,15 h ∧ h_ro ≥ 0,35 h ∧ h_ru ≥ 0,35 h ∧ l_A ≥ h/2 ∧ l_z ≥ max(1,5 h; 300 mm)
HINWEIS Profil EC5-2026 (Entwurf): Vollholz/KVH nur verstärkt; unverstärkt nur GL, LVL  [U]
ALTERNATIVE  variante: Leitung parallel zur Balkenlage;  kompensation: Wechsel mit Nachweis;
             grenzwert: nächste Achse, die in Decken- und Wandraster frei ist
```

> **Beispiel 9.6.** B15, Balkenhöhe *h* = 240 mm: Die Anschlussleitung DN 50 der Duschrinne (Ø 60 mm) quer zur Balkenlage verletzt die Regel, denn 60 mm > 0,15 · 240 mm = 36 mm. Das Elektro-Leerrohr M25 (Ø 31 mm) ist nur eine Querschnittsschwächung. Für die Fallleitung DN 100 liegt die nächste in Decke und Wand freie Achse 120 mm entfernt, zulässig sind 100 mm. B15 plant deshalb einen Wechsel als IFC-Bauteil und gibt die Bohrungen als BTLx-Bearbeitung aus.

Die Ständerbohrung prüft B15 gegen einen **Firmenregel-Platzhalter**, eine Bohrung von höchstens 25 % der Ständertiefe. Für Ständer als Druckstäbe enthält EC 5 keine eigene Bohrregel, und eine Primärquelle für eine Bohrregel wurde nicht gefunden (Recherche 08) [U]. Das Regelschema zwingt hier zur Ehrlichkeit: Die Quelle ist M, der Status ist [U], und der Wert ist beim Hersteller zu erfragen.

### 9.4.8 Schallschutz gegen Außenlärm (DIN 4109-1/-2, BayTB, B19)

```text
REGEL DE.DIN4109.Aussenlaerm                     [N eingeführt, R1, V]
VORBEDINGUNG Nachweispflicht: B-Plan-Festsetzung nach § 9 Abs. 1 Nr. 24 BauGB ∨ L_a ≥ 61 dB(A)
             (BayTB 11/2025 A 5.2/1 Nr. 5); EU-Lärmkarten als Eingang unzulässig → unbestimmt
L_a(f)   := Beurteilungspegel + 3 dB; Schlafräume nachts + 10 dB, wenn L_r,T − L_r,N < 10 dB
            abgewandte Seite ohne Nachweis − 5 dB (offen) bzw. − 10 dB (geschlossen)
erf(r)   := max(L_a,max(r) − 30 dB; 30 dB)       # Wohnräume
K_AL(r)  := 10 lg(S_S / (0,8 · S_G))
PRÜFE    R′w,ges(r) − 2 dB ≥ erf(r) + K_AL(r),  R′w,ges = energetische Summe der Bauteile
WAHL     min Mehrkosten über {Fensterklasse je Fassade} × {Rollladen} × {Lüfter}
         Stufe 1 Firmenkatalog, Stufe 2 Fremdprodukt, sonst verletzt
ALTERNATIVE  variante: Grundriss mit Schlafräumen zur abgewandten Seite
```

> **Beispiel 9.7.** B19, Autobahn im Norden: Die Nordfassade hat nachts *L_a* = 72,0 dB. In der Ausgangsvariante braucht das Schlafzimmer erf *R′_w,ges* = 42,0 dB und damit Fenster der Schallschutzklasse 5. Die Katalogfenster der Firma gibt es nur in SSK 3 und 4. Die Regel ist deshalb zweimal verletzt (Schlafen, Kind). Die Variante mit Schlafräumen nach Süden senkt erf *R′_w,ges* im Schlafzimmer auf 36,8 dB (9.5).

### 9.4.9 Wärmepumpe: Schall und Aufstellung (TA Lärm, DIN ISO 9613-2, B20)

```text
REGEL DE.TALaerm.WP-Aufstellung                  [G + N + M, R1, V]
FÜR   jeden Kandidatenort p im Raster 0,5 m und jeden Immissionsort IO (0,5 m vor Fenster;
      unbebautes Nachbargrundstück: Rand der überbaubaren Fläche, TA Lärm A.1.3 b)
L_r,N(p, IO) := L_WA,Nacht − A_div − A_atm − A_gr − A_bar + D_Ω + Reflexion + K_T + K_I
                (DIN ISO 9613-2, A-bewertet; K_T, K_I ∈ {0, 3, 6} dB; lauteste Nachtstunde)
PRÜFE  runde_DIN1333(L_r,N) ≤ IRW_N(Gebiet)                 # S1: WA 40 dB(A)
       ∧ Schutzbereich_R290(p) ∩ (Öffnungen ∪ Senken ∪ Einläufe) = ∅   # S5: Herstellerangabe
       ∧ Schutzbereich_R290(p) ⊂ Grundstück ∧ Leitungslänge(p) ≤ max ∧ Ausblas frei ≥ 1 m
ZIEL   max min_IO (IRW_N − L_r,N)  ∧  Ziel IRW_N − 6 dB (Irrelevanz, Firmenziel)
ALTERNATIVE  grenzwert: bester zulässiger Ort mit Reserve;  kompensation: Schirm, Silent-Mode
```

> **Beispiel 9.8.** B20: Von 2 304 Rasterpunkten sind 834 zulässig. Die häufigsten Ausschlussgründe sind der R290-Schutzbereich, der über die Grundstücksgrenze ragt (564), und die Leitungslänge (499). Die typische Installateurwahl „Ostseite vor dem Hauswirtschaftsraum“ ist **unzulässig**, weil das HWR-Fenster im Schutzbereich liegt. Das Optimum bei (7,25 m; 1,75 m) hat eine kleinste Reserve von 12,9 dB zum Nachtrichtwert. Die Westseite ist nach TA Lärm zulässig (35 dB(A) ≤ 40 dB(A)). Sie verfehlt aber am Wohnzimmer das Irrelevanzziel von 34 dB(A).

Das Beispiel zeigt die Schichtung an einer einzigen Regel. Der Richtwert von 40 dB(A) ist Recht (*S*₁). Der R290-Schutzbereich ist eine Herstellerangabe (*S*₅). Das Ziel IRW − 6 dB ist in der TA Lärm ein Kriterium für die Irrelevanz einer Zusatzbelastung. Die LAI empfiehlt es als Planungsziel (Recherche 22) [V]. Als Firmenziel verschärft es die Rechtsgrenze monoton (9.3.3), ist selbst aber keine Rechtsgrenze.

**Bewegungsflächen.** Für die in der Gliederung genannten Bewegungsflächen gilt dasselbe Schema mit anderer Quelle: VDI 6000 Blatt 2 nennt vor dem WC 80 × 75 cm und vor der Dusche 90 × 75 cm als Bewegungsfläche, DIN 18040-2 für barrierefreie Wohnungen 120 × 120 cm (Recherche 13) [V]. Die VDI-Werte sind anerkannte Regel der Technik (*S*₃). Die Werte der DIN 18040-2 werden nur dann bauordnungsrechtlich verbindlich, wenn das Profil die Barrierefreiheit einschaltet (Kapitel 9a.3). Die Prüffunktion ist eine Geometrieregel: Die Bewegungsfläche als Rechteck vor dem Objekt darf sich mit anderen Bewegungsflächen überlagern, aber nicht mit Bauteilen oder Möbeln.

## 9.5 Ablehnen mit Begründung und Alternative

### 9.5.1 Das Prinzip

Ein Laie kennt die Regeln nicht. Eine Ablehnung ohne Begründung lässt ihn raten, eine Begründung ohne Alternative lässt ihn suchen. Beides widerspricht dem Zielbild, nach dem der Kunde „Kosten und Folgen sofort“ sieht. Das Prinzip lautet deshalb:

> **Jede Ablehnung nennt die verletzte Regel mit Quelle, die Werte, an denen sie scheitert, und mindestens eine zulässige Alternative oder den Weg zu einer Freigabe.**

Formal ist eine Ablehnung die Antwort auf einen Kundenwunsch *w*, dessen Umsetzung *x_w* nicht in *L*(*P*) liegt. Die Antwort hat drei Teile:

1. **Konfliktmenge.** Die Menge der verletzten Regeln, möglichst minimal: Keine echte Teilmenge erklärt die Ablehnung ebenfalls. Die Konfigurationsforschung stellt dafür Diagnoseverfahren bereit, die auch personalisierte Diagnosen für unvereinbare Nutzeranforderungen liefern [@felfernig2014knowledge; @felfernig2011personalized; @yang2012constraint].
2. **Begründung.** Ein Text aus dem Feld `begruendung` mit eingesetzten Werten und Quelle. Er ist kontrastiv formuliert, also als Antwort auf „warum dies und nicht das“. Das entspricht dem Befund, dass Menschen Erklärungen kontrastiv verstehen [@miller2019explanation]. Die Forschung zu Erklärungskomponenten wissensbasierter Systeme hat zudem gezeigt, dass Erklärungen die Akzeptanz beeinflussen und dass sie aus der Struktur des Regelwissens entstehen müssen, nicht nachträglich [@gregor1999explanations; @clancey1983epistemology].
3. **Alternative.** Ein Entwurf *x′* ∈ *L*(*P*), der dem Wunsch möglichst nahe kommt, oder ein Freigabeweg. Die Nähe zum Ausgangsentwurf ist das Kriterium, das auch Wu et al. für „Design Healing“ verwenden [@wu2025design].

Die dritte Komponente lässt sich als **Projektion des Wunsches auf den Lösungsraum** verstehen: $x' = \arg\min_{x \in L(P)} d(x, x_w)$. Ist die kleinste Distanz null, wird der Wunsch angenommen. Ist sie positiv, wird er mit Anpassung angenommen oder abgelehnt, je nachdem, ob die Anpassung den Kern des Wunsches erhält. Ist *L*(*P*) in der Umgebung leer, bleibt nur der Freigabeweg.

### 9.5.2 Arten der Alternative

Aus den Beispielen ergeben sich fünf Arten. Sie entsprechen den Einträgen im Feld `alternative` des Regelschemas.

| Art | Bedeutung | Beispiel |
|---|---|---|
| **A1 Grenzwert** | nächster zulässiger Wert desselben Parameters | Bad mindestens 1,70 m breit (B6); Laufbreite 0,80 m (B5) |
| **A2 Kompensation** | andere Parameter ändern, Wunsch bleibt | Bodenplatte im Bad 30 mm absenken (B14); Wechsel statt Bohrung (B15) |
| **A3 Variante** | strukturell anderer Entwurf | Schlafräume nach Süden (B19); Leitung parallel zur Balkenlage (B15) |
| **A4 Schichtwechsel** | eigene Firmenregel aussetzen, mit Freigabe | Fremdfenster SSK 5 statt Katalogfenster (B19) |
| **A5 Freigabeweg** | Entscheidung einer berechtigten Stelle | Abweichung nach Art. 63 BayBO; Architekt statt Zimmerermeister (Kapitel 9a.4) |

Die Reihenfolge ist zugleich eine Präferenz. A1 und A2 lassen den Entwurf im Kern unverändert, A3 ändert ihn, A4 und A5 verlassen den automatischen Entscheidungsraum. Das System bietet deshalb zuerst A1 und A2 an. A4 und A5 erscheinen nur, wenn A1 bis A3 nicht existieren oder der Kunde sie ablehnt. So vermeidet das System, dass eine Abweichung wie ein normaler Ausweg wirkt.

### 9.5.3 Drei Fälle aus den Beispielen

**Fall B6: Begründung ohne Alternative.** Die Sprachpipeline lehnt zwei von neun Äußerungen ab (`ausgabe/intent_protokoll.json`):

- „Das Bad oben bitte eins zwanzig breit“: *Bad: Breite 1,20 m < Mindestbreite 1,70 m (Projektregel bad).*
- „Mach das Kinderzimmer 1 einen Meter zwanzig schmaler“: *Kinderzimmer 1: Breite 2,30 m < Mindestbreite 2,60 m; Fläche 7,82 m² < Mindestfläche 10,00 m² (Projektregel kind).*

Beide Ablehnungen nennen Regel, Werte und Quelle. Eine Alternative erzeugt der Prototyp aber **nicht**. Das ist eine Lücke des Prototyps, die sich an dieser Stelle beziffern lässt. Für das Bad ist die Alternative A1 trivial (1,70 m). Für das Kinderzimmer ist sie es nicht, und genau das macht den Fall lehrreich. Die Konfliktmenge enthält zwei Regeln. Die zuerst genannte Mindestbreite ist aber nicht die bindende. Aus 7,82 m² bei 2,30 m Breite folgt eine Raumtiefe von 3,40 m. Bei der Mindestbreite von 2,60 m ergäben sich nur 8,84 m², also weiterhin zu wenig. Bindend ist die Mindestfläche: Die Breite muss mindestens 10,00 m² / 3,40 m = 2,94 m betragen, im 5-cm-Raster 2,95 m (10,03 m²). Die richtige Alternative lautet also: „höchstens 55 cm schmaler“, nicht „höchstens 90 cm schmaler“. Diese Nachrechnung ist eine eigene Rechnung, im Prototyp noch nicht implementiert. Sie zeigt, dass die Alternative nicht aus der ersten verletzten Regel, sondern nur aus der **gemeinsamen Projektion auf alle Regeln** folgt.

B6 unterscheidet außerdem Ablehnung von **Rückfrage**. „Das Bad soll zwanzig Zentimeter breiter werden“ führt zur Rückfrage, weil zwei Bäder in Frage kommen. „Das Bad oben eins fünf breiter“ führt zur Rückfrage, weil „eins fünf“ 1,05 m oder 1,50 m bedeuten kann. Eine Rückfrage betrifft die Absicht, eine Ablehnung die Regel. Beides darf die Oberfläche nicht vermischen (Kapitel 10).

**Fall B14: Konflikterklärung mit Kompensation.** Ohne Absenkung der Bodenplatte findet der Fußboden-Solver für das Bad keinen zulässigen Aufbau. Die Meldung lautet sinngemäß: *Kein zulässiger Aufbau für H = 210 mm. Mindestens erreichbar: 240 mm (fehlen 30 mm) → Rohdecke im Raum um ≥ 30 mm absenken (Rohbauvorgabe), Ziel-Aufbauhöhe erhöhen oder dünneres System.* Dazu nennt sie die häufigsten Ausschlussgründe (Test `test_konflikt_bad_ohne_absenkung`). Die Ursache ist die Summe aus Estrich-Mindestdicke mit Rohrüberdeckung, bodengleicher Dusche und Rohdeckentoleranz (Recherche 16). Die Alternative ist eine Kompensation (A2): Die Rohbauvorgabe „Bodenplatte im Bad 30 mm tiefer“ steht seitdem im Eingabedatensatz. Das zeigt einen zweiten Nutzen der Alternative: Sie wird zur **Vorgabe für ein anderes Gewerk**. Ein zweiter Konfliktfall ist die Abwasserleitung DN 50 im 160-mm-Trockenaufbau. Sie braucht bei 1 % Gefälle über 1,2 m eine Installationsebene von 62 mm und ist nicht unterzubringen. Die Alternative ist eine Variante (A3), nämlich die Führung in der Balkenlage mit Durchbruchprüfung nach B15.

**Fall B19: Variante statt teurerem Bauteil.** In der Ausgangsvariante sind zwei Räume nur mit Fremdprodukten nachweisbar. Das System bietet drei Wege an: A4 (Fremdfenster, Firmenregel aussetzen), A2 (schallgedämmte Lüftung, kein Kippfenster) und A3 (Grundrisstausch). Die Variante A3 legt Schlaf- und Kinderzimmer nach Süden:

| Kennzahl | Variante A (Ursprung) | Variante B (Tausch) |
|---|---|---|
| erf *R′_w,ges* Schlafzimmer | 42,0 dB | 36,8 dB |
| höchste Fensterklasse | SSK 5 | SSK 4 |
| Regelverstöße | 2 | 0 |
| Mehrkosten Schallschutz (Beispielpreise) | 5 958 € | 3 250 € |

Die Alternative ist hier nicht nur zulässig, sondern auch billiger und schalltechnisch besser. Sie ist ein Beispiel dafür, dass eine gute Ablehnung den Entwurf verbessert, statt ihn nur zu begrenzen. Die Empfehlung nennt ihre Quelle: DIN 4109-2, 4.4.5.1, mit −5 dB für die abgewandte Seite. Andere Empfehlungen aus B19, etwa der Hinweis auf die WHO-Leitlinien [@who2018noise], sind keine R1-Regeln, sondern Empfehlungen der Klasse R5 und gehören zu Kapitel 9b.

### 9.5.4 Ablehnungen sind nachzuweisen

Kapitel 7a hat gezeigt, dass negative Nachweise gleichwertig sind. Die absichtlich fehlerhaften Fälle aus B2 und B4 erzeugen vollständige Nachweise mit rotem Status, Befund, GUID und Zeichnung (7a.6). Für die Ablehnung folgt daraus eine Pflicht: Jede Ablehnung erzeugt einen Nachweis mit Regel, Fassung, Werten und angebotener Alternative. Der Audit-Trail enthält damit auch die Entwürfe, die das System *nicht* zugelassen hat. Das ist für die Produkthaftung relevant, weil Software ab dem 09.12.2026 ein Produkt ist und jede Entscheidung, auch eine Ablehnung, nachvollziehbar sein muss (Kapitel 4.8.1) [@prodhaftg2026]. Es ist auch für das Werkvertragsrecht relevant: Der Architekt schuldet eine dauerhaft genehmigungsfähige Planung [@bgh2002genehmigungsplanung]. Eine dokumentierte Ablehnung belegt, dass eine nicht genehmigungsfähige Variante erkannt und nicht weiterverfolgt wurde.

## 9.6 Compliance by construction und nachträgliche Prüfung

### 9.6.1 Zwei Wirkungsweisen

Regeln können auf zwei Weisen auf einen Entwurf wirken.

- **Nachträgliche Prüfung (generate and test).** Der Entwurf entsteht, dann prüft die Regelmaschine. Das ist das Vierphasenmodell von Eastman et al. [@eastman2009automatic] und das Muster fast aller Arbeiten zur automatisierten Prüfung. Sobhkhiz et al. kritisieren, dass diese Trennung Planende mit iterativen Korrekturen belastet [@sobhkhiz2021framing].
- **Konformität durch Konstruktion (compliance by construction).** Die Regeln sind Nebenbedingungen des Verfahrens, das den Entwurf erzeugt. Ein Solver erzeugt nur Entwürfe aus *L*(*P*), oder jede Änderung wird vor ihrer Anwendung auf *L*(*P*) projiziert (9.5.1).

Für Laien ist die zweite Wirkungsweise die einzig brauchbare. Ein Laie kann mit einer Liste von Verstößen nichts anfangen, wohl aber mit einem Entwurf, der gültig bleibt, und mit einer Rückmeldung, warum eine Änderung anders ausfiel als gewünscht. Kapitel 5 hat gezeigt, dass Regeln während der Erzeugung bisher nur in Nischen wirken: im Innenraum [@sydora2020rulebased], beim kanadischen Framing [@abushwereb2019knowledge] und bei der Kubatur im modularen Holzbau [@erhan2026dcodeweaver]. Echtzeit-Rückmeldung im Entwurf gibt es mit CODE-COMPANION für Planende [@tonguc2026code]. Die Idee, dass Nutzerfreiheit durch gut formulierte Constraints entsteht, hat Niemeijer für die nutzerorientierte Mass Customization ausgearbeitet [@niemeijer2014freedom].

### 9.6.2 Die Beispiele als Solver

Sechs der Beispiele setzen R1-Regeln bereits als Nebenbedingungen eines Lösungsverfahrens um. Tabelle 9.5 ordnet sie ein.

**Tabelle 9.5: Solver-Muster in den Beispielen**

| Beispiel | Suchraum | Verfahren | Eigenschaft |
|---|---|---|---|
| B5 Treppe | *n* × Auftritt im 5-mm-Raster | vollständige Aufzählung (68 Lösungen) | vollständig; Unlösbarkeit beweisbar |
| B14 Fußboden | diskrete Kombinationen × stetige Dicken | Aufzählung + exaktes lineares Teilproblem | optimal bezüglich Zielfunktion; Konflikterklärung |
| B15 Durchdringung | Leitungsachsen im 625-mm-Raster | Suche nach freier Achse, sonst Wechsel | deterministisch; erzeugt Bauteile und BTLx |
| B16 Fliesen | Rasterursprung × Muster × Entwässerung | Aufzählung, Clipping, Reststückverwertung | harte Regel (Stücke < 6 mm werden verfugt) + weiche Regel als Malus |
| B19 Außenlärm | Fensterklasse × Rollladen × Lüfter je Fassade | Minimierung der Mehrkosten unter Nachweis | Stufe Katalog → Fremdprodukt → Verstoß |
| B20 Wärmepumpe | Raster 0,5 m (2 304 Punkte) | Aufzählung, Maximierung der kleinsten Reserve | vollständig im Raster; Ausschlussgründe gezählt |

Drei Eigenschaften dieser Verfahren sind für die Argumentation wichtig.

**Vollständigkeit ermöglicht Erklärung.** B5 und B20 zählen ihren Suchraum vollständig auf, B14 zählt den diskreten Teil vollständig auf und löst den stetigen exakt. Deshalb können sie nicht nur „keine Lösung gefunden“ melden, sondern „es gibt keine Lösung“. Mit den gezählten Ausschlussgründen können sie außerdem sagen, *warum*. Eine stochastische Suche könnte das nicht. Kapitel 5.5.3 hat festgehalten, dass die Kombination mit stochastischer Suche Reproduzierbarkeit kostet [@lottaz1998constraint].

**Harte und weiche Regeln sind getrennt.** B14 und B16 unterscheiden harte Nebenbedingungen, die einen Kandidaten verwerfen, von weichen Regeln, die als Hinweis oder Strafterm eingehen. In B16 ist die Handwerksregel „kein Randstück unter einem Drittel der Fliese“ ein Malus in der Zielfunktion und keine Grenze. Stücke unter 6 mm werden dagegen gar nicht verlegt, sondern verfugt. Das entspricht der Unterscheidung harter und weicher Constraints in der Constraint-Programmierung [@meseguer2006soft]. Ob eine Handwerksregel hart oder weich ist, entscheidet das Profil, nicht der Solver.

**Bedingte Regeln aktivieren weitere Regeln.** Wählt der Kunde eine Wärmepumpe mit R290, wird der Schutzbereich zur harten geometrischen Regel. Legt er eine Dusche bodengleich an, greifen Abdichtungsklasse W2-I und Estrichwechsel. Die Konfigurationsforschung bildet solche Abhängigkeiten als bedingte Constraint-Probleme ab [@gelle2003solving].

### 9.6.3 Warum trotzdem nachträglich geprüft wird

Konformität durch Konstruktion garantiert nur, was der Solver kennt. Sie garantiert nicht, dass der Solver richtig rechnet, dass der Generator das Ergebnis richtig ins IFC schreibt und dass die Regeln richtig formalisiert sind. Pinto et al. haben selbst bei deterministischer Prüfsoftware Ausführungsfehler gefunden [@pinto2026exhaustive]. Die Arbeit verbindet deshalb beide Wirkungsweisen zu einem **zweikanaligen** Verfahren:

1. **Kanal 1, Erzeugung.** Der Solver arbeitet auf dem Parametermodell und nutzt die Regeln als Nebenbedingungen.
2. **Kanal 2, Nachprüfung.** Nach der Erzeugung prüft eine davon getrennte Prüfschicht das **IFC-Modell**, nicht das Parametermodell. Sie verwendet dieselbe Regeldefinition, aber eine eigene Auswertung: IDS für R2 (B2), die Nachweisschicht mit Gegenrechnung für R1 (Kapitel 7a.3).

Weichen die Kanäle voneinander ab, liegt ein Fehler im Generator, im Solver oder in der Regel vor. Der Entwurf wird dann nicht freigegeben. Das Verfahren entspricht der Vergleichsrechnung eines Prüfingenieurs, läuft aber bei jedem Lauf vollständig. Es ist die technische Antwort auf die Frage, wie „Validierung als Teil der Generierung“ nachgewiesen werden kann (Lücke L5, Kapitel 5.8.1).

**Welche Regel in welchen Kanal?** Nicht jede Regel kann in Echtzeit im Solver laufen. Als Arbeitsregel gilt:

- In den **Solver** gehören lokale R1-Regeln mit kleinem Suchraum und kurzer Rechenzeit: Raummaße, Treppe, Abstandsfläche, Fensterfläche, Dachneigungsklasse, Bohrungen.
- In die **Hintergrundprüfung** gehören Regeln, deren Auswertung das ganze Gebäude braucht: Energiebilanz, vollständiger Schallnachweis, Tragwerksvorbemessung. Ihr Ergebnis erscheint mit Verzögerung und markiert den Entwurf bis dahin als **unbestimmt**.
- **Vorab-Grenzwerte** schließen die Lücke. Für kritische Schwellen berechnet das System den Grenzwert, bevor der Kunde ihn überschreitet, etwa den Kniestock, ab dem das Dachgeschoss Vollgeschoss wird (9.4.2), oder die Höhe, ab der die Gebäudeklasse springt (Kapitel 9a.2).

Die Abhängigkeiten zwischen Regeln und Parametern bilden einen Graphen. Eine Änderung der Dachneigung betrifft Abstandsfläche, Vollgeschoss, Deckungsklasse, Gebäudeklasse und Photovoltaik. Die Prüfschicht wertet deshalb nur die Regeln neu aus, deren Eingaben sich geändert haben. Das entspricht dem Vorberechnungsgraphen von OpenBIMRL [@stepien2023openbimrl].

## 9.7 Rechtliche Nutzung von Normwerten

Kapitel 4.9 hat die urheberrechtliche Lage beschrieben: Private Normwerke bleiben nach § 5 Abs. 3 UrhG geschützt, auch wenn Gesetze auf sie verweisen [@urhg5; @wd2020normen]. Der EuGH hat 2024 einen Anspruch auf Zugang zu harmonisierten Normen anerkannt, die Frage des Urheberrechts aber nicht entschieden [@eugh2024publicresource]. Die hier relevanten Normen sind national [U]. Einzelne Zahlenwerte dürften als technische Fakten kaum schutzfähig sein, Tabellen, Texte und Bilder dagegen schon [U].

Für den Regelraum folgen daraus vier Umsetzungsregeln. Sie sind in den Beispielen bereits angewendet.

1. **Kennwert mit Verweis statt Tabelle.** Der Datensatz enthält einzelne Kennwerte mit Fundstelle, nicht die Tabelle. Der Eingabedatensatz von B14 hält das ausdrücklich fest: „Normwerte sind nur als einzelne Kennwerte mit Normverweis eingetragen (keine Tabellenkopie)“ (`daten/b14_fussbodenaufbau.json`).
2. **Formel statt Tabelle, wo möglich.** Die Mindestabstände der LAI-Tabelle 5 für Wärmepumpen ergeben sich aus den Gleichungen der ISO 9613-2. Recherche 22 hat alle 41 Tabellenwerte aus den Formeln auf höchstens 0,11 m reproduziert [V]. Die Bemessung nach DWA-A 138-1 lässt sich ebenfalls ohne Normtext nachrechnen, nur die Beiwerttabellen bleiben kostenpflichtig (Recherche 18). Wer rechnet, statt abzuschreiben, braucht die Tabelle nicht.
3. **Lizenz für Tabellenwerke.** Wo eine Regel nur als Tabelle existiert, etwa die Zusatzmaßnahmen der ZVDH-Fachregel [@zvdh2024], stammen die Werte aus öffentlich zugänglichen Herstellerbroschüren mit Fundstelle. Für den kommerziellen Betrieb ist eine Lizenz des Regelsetzers einzuholen.
4. **Bauteilkennwerte aus Katalogen mit Nutzungsrecht.** Kennwerte für Bauteile stammen aus frei nutzbaren oder lizenzierten Katalogen wie dataholz.eu [@dataholz] oder aus Herstellernachweisen, nicht aus Normtabellen (Kapitel 4.9).

Das Regelschema unterstützt diese Regeln strukturell. Das Feld `quelle` trägt Fundstelle und Fassung, nicht den Text. Das Feld `parameter` trägt Werte mit Herkunft. Der Status [V]/[U] zeigt, ob der Wert an der Primärquelle geprüft ist. Eine automatische Extraktion von Regeln aus Normtexten schließt die Arbeit aus fachlichen und rechtlichen Gründen aus (Kapitel 5.8.2).

## 9.8 Zwischenfazit

Das Kapitel beantwortet FF2 in fünf Punkten:

1. **Zwei Techniken, eine Regeldefinition.** R2 wird als IDS formuliert und werkzeugunabhängig geprüft. R1 wird als ausführbare Regel nach einem Regelschema mit acht Feldern formuliert: Kennung, Quelle mit Fassung, Geltung, Vorbedingung, Prüffunktion, Ergebnis, Begründung und Alternative. Die fünfwertige Ergebnismenge koppelt R1 an R2 (unbestimmt) und an R3 (freigabepflichtig).
2. **Regeln sind zeitabhängig.** Sechs Versionierungsmuster (Tabelle 9.3) verlangen Profile mit Version, Geltungszeitraum und Stichtagsregel. Der Fall ISO 6946 zeigt, dass die neueste Fassung nicht die geltende sein muss.
3. **Schichtung ist prüfbar.** Monotonie lässt sich nach Satz 9.1 auf endlich viele Parametervergleiche zurückführen. Wo das nicht geht, prüft eine vollständige Aufzählung. Zur Laufzeit wertet die Prüfschicht ohnehin alle Schichten aus. Absichtliche Lockerungen sind als ausgesetzte Regeln mit Freigabe modelliert, und die Bauordnung ist gegen Lockerung durch Kunde oder Vertrieb geschützt.
4. **Ablehnen heißt projizieren.** Eine Ablehnung nennt die Konfliktmenge, eine kontrastive Begründung und eine Alternative. Die Alternative folgt aus der gemeinsamen Projektion auf alle Regeln, nicht aus der ersten verletzten Regel (Fall B6). Die Beispiele B14 und B19 zeigen, dass die Alternative zur Vorgabe für ein anderes Gewerk werden oder den Entwurf verbessern kann.
5. **Konform durch Konstruktion, belegt durch Nachprüfung.** Sechs Beispiele setzen R1-Regeln als Nebenbedingungen vollständiger oder exakter Verfahren um. Eine davon getrennte Prüfung am IFC-Modell sichert das Ergebnis zweikanalig ab.

Offen bleiben drei Punkte. Die Alternativen-Generierung ist in B6 noch nicht implementiert. Vollgeschoss, Fensterfläche und Dachneigung sind spezifiziert, aber nicht lauffähig. Die Auslegungsparameter mit Status [U] (Giebelfläche, Fenstermaß) muss eine bauvorlageberechtigte Person festlegen. Kapitel 9a zeigt, wie das Profil vom Gebäudetyp abhängt und welche Freigaben daraus folgen.

## 9.9 Umsetzungsvorgaben für die App

Die Arbeit ist die fachliche Grundlage einer App, die am Ende voll funktionieren soll. Dieser Abschnitt übersetzt das Kapitel deshalb in Anforderungen und maschinenlesbare Vorgaben. Es gelten die Regeln aus Kapitel 3.7: „Muss“ heißt, dass ohne die Anforderung ein Rechts-, Nachweis- oder Fertigungsfehler entstehen kann. „Soll“ heißt, dass sie Qualität oder Nutzen erhöht. Jedes Abnahmekriterium ist ein Testfall mit Eingabe und erwartetem Ergebnis. Wo ein Beispiel die Referenz liefert, sind dessen gemessene Werte die Sollwerte.

### 9.9.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/regel.schema.json` | JSON-Schema (Draft 2020-12) des Regelkatalogs; das Schema einer Regel ist `#/$defs/regel` mit den acht Feldern aus Tabelle 9.2 und den Zusatzfeldern Klasse, Härte, Schicht, Eingaben mit Einheit, Grenzwerte mit Richtung, Status, Beispiel, Anforderungen und Tests |
| `spezifikation/regelkatalog.yaml` | initialer Katalog mit 40 Regeln aus Kapitel 9 und 9a (R1–R4), darunter die neun Regeln aus 9.4, die Holzfeuchte-Familie aus 9.3.3, die IDS-Spezifikationen aus B2 und die typabhängigen Regeln aus 9a |
| `spezifikation/regelprofile.yaml` | Profilregister (Version, Schicht, Geltung, Stichtag), Merkmalsvektor, Schalter, Schwellenwarnungen, Brandschutz je GK, Matrix Gebäudetyp × Regelbereich, Freigabe-Gates (Kapitel 9a) |

Am 27.09.2026 geprüft: Beide YAML-Dateien und das Schema sind mit Python parsebar. Das Schema ist nach Draft 2020-12 gültig. Der Katalog validiert mit `jsonschema` 4 ohne Fehler gegen das Schema. Ein Konsistenzabgleich ergab, dass jede in `regelprofile.yaml` genannte Regel im Katalog steht, jedes Profil des Katalogs registriert ist und die Schicht jeder Regel mit der ihres Profils übereinstimmt.

### 9.9.2 Anforderungen

**Regeldaten und Prüfkern**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09-01 | Muss | Regeln sind Daten nach `regel.schema.json`; die Prüffunktion ist versionierter Code. Der Katalog wird nur geladen, wenn er schema-valide ist. | 9.2.3 | `regelkatalog.yaml` lädt ohne Fehler. Eine Kopie, in der bei `BY.BayBO.6.T` das Feld `quelle.fassung` fehlt, wird mit Ladefehler „fassung fehlt“ abgewiesen. |
| ANF-09-02 | Muss | Jede Prüfung liefert einen von fünf Werten. Fehlt eine R2-Voraussetzung, ist das Ergebnis `unbestimmt`, nie `erfuellt` oder `verletzt`. | 9.2.1 | B4 „mittig“ ohne Geländemodell: `unbestimmt`, Meldung nennt `BY-R2-Gelaende-DGM`. Mit Geländemodell: `erfuellt`. |
| ANF-09-03 | Muss | R2-Anforderungen werden je Profil und Reifegrad als IDS 1.0 erzeugt und geprüft. Der Nachweis speichert Werkzeug und Version. | 9.2.2 | B2: Datei „bestanden“ erfüllt 11 von 11 Spezifikationen; Datei „fehlerhaft“ scheitert an genau HRB-01, 03, 05, 08, 09, 11. Nachweis enthält „ifctester 0.8.5“. |
| ANF-09-04 | Muss | Befunde werden über den Spezifikationsnamen einer Regel-ID zugeordnet, solange das Prüfwerkzeug `identifier` ignoriert. | 9.2.2 | B2 fehlerhaft: Jeder der 6 Befunde trägt die Regel-ID `IDS.HRB-01` bzw. `IDS.HRB-02-11` und den Namen der Spezifikation. |
| ANF-09-05 | Muss | Profile sind unveränderlich und versioniert. Jeder Nachweis trägt Profil-ID, Profilversion, Funktionsversion und SHA-256 des geprüften Modells. | 9.3.1, 7a.5 | Nachweis B4 enthält `BY-BayBO-2026-05`, `0.1.0`, `abstandsflaeche@1.2` und den Modell-Hash. Eine Änderung eines Kennwerts im Profil ohne neue Version wird abgewiesen. |
| ANF-09-06 | Muss | Das Profil wählt die Normfassung je Zweck. Für den GModG-Nachweis gilt die datiert in Bezug genommene Fassung. | 9.3.2, Fall 2 | Profil `DE-GModG-2026-07`: U-Wert-Nachweis nennt DIN EN ISO 6946:2008-04. Werkvertragliches Profil: 2018-03. Laden eines GModG-Profils mit Ausgabe 2018-03 erzeugt Warnung „datierter Verweis § 20 Abs. 6 GModG“. |
| ANF-09-07 | Muss | Bei parallel gültigen Normgenerationen entscheidet das eingeführte Profil; das kommende Profil erzeugt Hinweise. | 9.3.2, Fall 3 | B15, Durchbruch BD-1: Verstoß nach `DE-EC5-2010-A2` (60 mm > 36 mm); zusätzlich Hinweis aus `DE-EC5-2026` „Vollholz/KVH nur verstärkt“. Keine Entscheidung aus dem kommenden Profil. |
| ANF-09-08 | Muss | Die Vollgeschossregel verwendet die Fassung zum Datum des Bebauungsplans (Stichtagsregel). | 9.3.2, Fall 5; 9.4.2 | DG 100 m², davon 60 m² mit ≥ 2,30 m: kein Vollgeschoss; 67 m²: Vollgeschoss. Bei Z = II und drei Vollgeschossen: `verletzt`. Ohne B-Plan-Datum: `unbestimmt`. |
| ANF-09-09 | Muss | Prüfung eines eingefrorenen Entwurfs gegen eine neue Profilversion erzeugt einen Delta-Bericht. | 9.3.2 | B4 gegen `BY-BayBO-2026-05` 0.1.0 und eine Testversion 0.2.0 mit `mindesttiefe_m` = 3,5: Bericht listet genau `BY.BayBO.6.T` als „Kennwert geändert“, Status Traufseite weiter `erfuellt` (5,00 m ≥ 3,50 m). |

**Schichtung und Monotonie**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09-10 | Muss | Beim Laden eines Profils prüft die App jede Parameterüberschreibung nach Satz 9.1 (Listing 9.3). Eine Lockerung ist ein Ladefehler. | 9.3.3 | `holzfeuchte_max`: N 20 % → Q 18 %: geladen. Testprofil M mit 22 %: Ladefehler mit Nennung von Schicht, Regel und altem Wert. |
| ANF-09-11 | Muss | Zur Laufzeit werden alle Schichten konjunktiv ausgewertet; die Meldung nennt die strengste verletzte Quelle. | 9.3.3 | Holz mit 19 %: `DE.DIN68800-2.Holzfeuchte` erfüllt, `Q.RAL-GZ422.Holzfeuchte` verletzt; Meldung nennt RAL-GZ 422 (vgl. ANF-03-07). |
| ANF-09-12 | Muss | Regeln dürfen nur mit Freigabe-Datensatz ausgesetzt werden. Für Regeln der Schichten S1/S2 ist nur eine Behördenentscheidung zulässig. | 9.3.3 | Rolle „Vertrieb“ setzt `BY.BayBO.6.T` aus: abgewiesen. Rolle „Firma“ setzt `M.Katalog.Fenster-SSK` aus: zulässig, Nachweis mit Status „abweichend freigegeben“. |

**Ablehnung, Begründung, Alternative**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09-13 | Muss | Jede Ablehnung enthält Konfliktmenge, Begründung mit Werten und Quelle sowie mindestens eine Alternative A1–A5. Die Alternative ist die gemeinsame Projektion auf alle Regeln. | 9.5.1, 9.5.3 | B6 „Kinderzimmer 1 einen Meter zwanzig schmaler“: Konfliktmenge {Mindestbreite, Mindestfläche}; Alternative „höchstens 0,55 m schmaler (2,95 m; 10,03 m²)“. B6 „Bad eins zwanzig breit“: Alternative „mindestens 1,70 m“. |
| ANF-09-14 | Soll | Alternativen werden in der Reihenfolge A1 → A5 angeboten; A4 und A5 nur, wenn A1–A3 fehlen oder abgelehnt werden. | 9.5.2 | B19 Variante A: erste Alternative ist A3 „Schlafräume nach Süden“ (Verstöße 2 → 0, Mehrkosten 5 958 € → 3 250 €); A4 „Fremdfenster“ erscheint danach. |
| ANF-09-15 | Muss | Rückfragen zur Absicht werden von Ablehnungen nach Regeln getrennt. | 9.5.3 | B6 „Das Bad soll zwanzig Zentimeter breiter werden“: Status `rueckfrage` (zwei Bäder); „eins fünf breiter“: `rueckfrage` (1,05 oder 1,50 m). Kein Regelnachweis. |
| ANF-09-16 | Muss | Jede Ablehnung erzeugt einen Nachweis nach Kapitel 7a mit rotem Status. | 9.5.4 | B4 „zu nah“: Nachweis Status „nicht erfüllt“, 15,20 m² außerhalb, SVG vorhanden, Hash gesetzt. |

**Wirkungsweise und Normwerte**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09-17 | Muss | Solver für R1-Regeln sind vollständig oder exakt und melden Unlösbarkeit mit Diagnose. | 9.6.2 | B5, Laufbreite 0,75 m: „keine Lösung“, Grenzwert 0,80 m. B14 Bad ohne Absenkung: „mindestens erreichbar 240 mm (fehlen 30 mm)“ mit Ausschlussgründen. |
| ANF-09-18 | Muss | Nach der Erzeugung prüft eine vom Solver getrennte Prüfschicht das IFC-Modell. Abweichung zwischen den Kanälen sperrt jede Freigabe. | 9.6.3 | IFC nach Generierung manipuliert (U = 0,25): IDS HRB-01 scheitert, Gate „Bauvorlage“ gesperrt, Meldung „Kanalabweichung“. |
| ANF-09-19 | Soll | Änderungen lösen nur die abhängigen Regeln neu aus; kritische Schwellen werden vorab als Grenzwert gemeldet. | 9.6.3 | Dachneigung 35° → 20°: neu ausgewertet genau Abstandsfläche, Vollgeschoss, Dachneigung, Gebäudeklasse. Intent „Kniestock ändern“: Grenzwert *k** wird vor Anwendung gemeldet. |
| ANF-09-20 | Muss | Normwerte stehen als Einzelkennwerte mit Fundstelle im Katalog; wo möglich wird aus Formeln gerechnet statt aus Tabellen gelesen. | 9.7 | Lint: Jeder Grenzwert mit Quelle N oder H hat eine Fundstelle. B20: Test `test_lai_tabelle5_aus_iso9613_reproduziert` trifft alle 41 LAI-Werte auf ≤ 0,11 m. |
| ANF-09-21 | Muss | Auslegungsparameter mit Status U sind vor dem Gate „Bauvorlage“ durch die bauvorlageberechtigte Person festzulegen. | 9.2.3 | `giebel_modus` nicht gesetzt: Gate gesperrt. Gesetzt auf „drittel“: Nachweis nennt 30,53 m² und die Person; „voll“: 36,40 m². |

**Einzelregeln (Referenzwerte)**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09-22 | Muss | Abstandsflächen nach `BY.BayBO.6.T`. | 9.4.1, B4 | Haus 10 × 12 m, Wandhöhe 6,50 m, 45°, Dachhöhe 5,00 m: *H* = 8,17 m, *T* = 3,27 m; „zu nah“ (x = 2 m): 15,20 m² außerhalb, Alternative „1,27 m nach Osten“. |
| ANF-09-23 | Muss | Treppen nach `DE.DIN18065.WG2WE` durch vollständige Aufzählung. | 9.4.3, B5 | 2,90 m, 0,90 m: 68 Lösungen; beste 17 × 170,6 mm / 290 mm, 2s + a = 631,2 mm, Lauflänge 4,64 m; mit max. 4,0 m: 16 × 181,25 / 265 mm. |
| ANF-09-24 | Muss | Fensterfläche nach `BY.BayBO.45.Fensterflaeche`. | 9.4.4 | Raum 14,0 m²: Soll 1,75 m²; Fenster 1,70 m²: `verletzt`, Alternative „+0,05 m²“. |
| ANF-09-25 | Muss | Dachneigung nach `DE.ZVDH.DZ.Dachneigung`. | 9.4.5 | Doppelmuldenfalz (RDN 30°), DN 20°: `erfuellt` mit Klasse K2 (ohne erhöhte Anforderung) bzw. K1 (mit); DN 9°: `verletzt`. |
| ANF-09-26 | Muss | Fußbodenaufbau nach `DE.Fussboden.OKFF-gleich`. | 9.4.6, B14 | Variante A (210 mm) und B (160 mm): alle Räume OKFF auf ±2 mm; Übergänge ≤ 1,6 mm; Teppich auf FBH: R_λ,B = 0,233 > 0,15 als weiche Meldung. |
| ANF-09-27 | Muss | Außenlärm nach `DE.DIN4109.Aussenlaerm`; EU-Lärmkarten sind als Eingang unzulässig. | 9.4.8, B19 | Variante A: Schlafzimmer erf R′w,ges = 42,0 dB, SSK 5, 2 Verstöße; Variante B: 36,8 dB, 0 Verstöße. Eingang EU-Lärmkarte: `unbestimmt`. |
| ANF-09-28 | Muss | Wärmepumpen-Aufstellung nach `DE.TALaerm.WP-Richtwert`, `M.Hersteller.R290-Schutzbereich` und `M.Firma.WP-Irrelevanzziel`. | 9.4.9, B20 | 2 304 Rasterpunkte, 834 zulässig; Ostseite vor HWR `verletzt` (Schutzbereich); Optimum (7,25 m; 1,75 m) mit Reserve 12,9 dB; Westseite erfüllt 40 dB(A), verfehlt 34 dB(A) am Wohnzimmer. |
| ANF-09-29 | Soll | Bewegungsflächen nach `DE.VDI6000.Bewegungsflaeche`; Überlagerung mit anderen Bewegungsflächen zulässig, mit Bauteilen nicht. | 9.4 | WC-Bewegungsfläche 0,80 × 0,75 m schneidet Waschtisch: `verletzt`. Überlagert nur die Bewegungsfläche der Dusche: `erfuellt`. |

## Verwendete Schlüssel

Das Kapitel enthält 74 Zitatstellen zu 59 Schlüsseln. Ein Python-Abgleich aller `[@key]` im Text gegen `literatur/lit-*.bib` ergab am 27.09.2026 keine fehlenden Schlüssel. Der Schlüssel `mbo2bim2023` steht in zwei Bib-Dateien (bekannte Dublette, siehe `literatur/KORREKTUREN.md`); zugeordnet ist die erste Datei.

**lit-A-acc-bim.bib** (11): `amor2021promise`, `bsi2024ids`, `eastman2009automatic`, `haeussler2021code`, `hjelseth2011capturing`, `idis2021szenarien`, `mbo2bim2023`, `merigoux2021catala`, `palmirani2011legalruleml`, `solihin2015classification`, `stepien2023openbimrl`

**lit-B-vorfertigung-ki.bib** (1): `felfernig2014knowledge`

**lit-C-recht-normen.bib** (22): `baunvo`, `bauvorlv`, `baybo2026`, `baytb2025`, `bgb`, `dataholz`, `din18065`, `din5034-1`, `din68800-2`, `egbgb249`, `en1995-2026`, `eugh2024publicresource`, `gmodg2026`, `ids2024`, `iso6946`, `prodhaftg2026`, `qdf2022`, `ral422`, `urhg5`, `wd2020normen`, `xplanung`, `zvdh2024`

**lit-E-vergleich-automation.bib** (3): `abushwereb2019knowledge`, `erhan2026dcodeweaver`, `sydora2020rulebased`

**lit-F-architekturpsychologie.bib** (3): `meseguer2006soft`, `miller2019explanation`, `who2018noise`

**lit-H-ff4-ff5.bib** (1): `bgh2002genehmigungsplanung`

**lit-I-schneeball-a.bib** (9): `cerovsek2025advancing`, `dimyadi2016computerizing`, `fischer2024extending`, `niemeijer2014freedom`, `pinto2026exhaustive`, `sobhkhiz2021framing`, `tonguc2026code`, `urban2026development`, `wu2025design`

**lit-I-schneeball-b.bib** (1): `gregor1999explanations`

**lit-J-schneeball-runde2.bib** (5): `akbas2025holistic`, `clancey1983epistemology`, `gelle2003solving`, `lottaz1998constraint`, `yang2012constraint`

**lit-L-schneeball-runde3.bib** (1): `felfernig2011personalized`

**lit-M-nachweis.bib** (2): `din1333`, `iso6946_2017`

Die Schlüssel in den Feldern `bib` von `spezifikation/regelkatalog.yaml` und `spezifikation/regelprofile.yaml` (23 Schlüssel) sind mit demselben Abgleich geprüft; es fehlt keiner.

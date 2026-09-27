# 9a Gebäudetypen und typabhängige Regelprofile

Status: Entwurf v0.1 (27.09.2026). Befunde zur Rechtslage, keine Rechtsberatung. Zitate beziehen sich auf `literatur/lit-*.bib`. Die Befunde stützen sich vor allem auf Recherche 14 (BayBO in der Fassung ab 01.05.2026, Bundesrecht auf gesetze-im-internet.de). [V] heißt am Wortlaut der Primärquelle geprüft, [U] unsicher.

## 9a.0 Einordnung

Kapitel 4 hat den Rechtsrahmen am Referenzfall behandelt: Wohngebäude der Gebäudeklassen 1 bis 3 mit höchstens drei Wohnungen. Die Arbeit umfasst aber alle Wohngebäudetypen vom Einfamilienhaus bis zum Geschosswohnungsbau in Holz (Kapitel 1.4). Dieses Kapitel zeigt, wie der Regelraum aus Kapitel 9 vom Gebäudetyp abhängt. Es vertritt drei Thesen:

1. **Der Gebäudetyp ist kein Etikett, sondern eine Ableitung.** Das Regelprofil folgt aus einem Merkmalsvektor, den das System aus dem Modell berechnet. Der vom Kunden gewählte Haustyp ist nur der Startwert der Konfiguration.
2. **Die Deltas springen.** Eine Wohnung mehr, ein ausbaufähiger Dachraum oder ein zweiter Nachbar an der Grenze kann Gebäudeklasse, Brandschutz, Schallschutz, Barrierefreiheit und die berechtigte Person zugleich ändern. Das System muss diese Schwellen zeigen, bevor der Kunde sie überschreitet.
3. **Die Freigabe-Gates hängen am Profil.** Wer Bauvorlagen verantworten darf und wer prüfen muss, ist eine Funktion desselben Merkmalsvektors.

## 9a.1 Typologie

Die Gliederung nennt sieben Typen. Für die Regelableitung sind drei Randfälle zu ergänzen, weil sie typische Kipppunkte zeigen. Tabelle 9a.1 ordnet sie nach den drei Größen, aus denen die Gebäudeklasse folgt.

**Tabelle 9a.1: Typologie und typische Einordnung**

| Typ | Anbau | Nutzungseinheiten | typische GK | Kipppunkt |
|---|---|---|---|---|
| Einfamilienhaus (EFH) | freistehend | 1 | 1 | über 400 m² BGF → GK 3 |
| EFH mit Einliegerwohnung | freistehend | 2 | 1 | zweite Nutzungseinheit |
| Zweifamilienhaus (ZFH) | freistehend | 2 | 1 oder 2 | wie ELW |
| Doppelhaushälfte (DHH) | einseitig | 1 je Haus | 2 | nie GK 1, da nicht freistehend |
| Reihenendhaus | einseitig | 1 je Haus | 2 | *h* > 7 m → GK 4 |
| Reihenmittelhaus | beidseitig | 1 je Haus | 2 | Bauvorlageberechtigung (9a.4) |
| Mehrfamilienhaus (MFH) | frei oder angebaut | 3 bis ≥ 4 | 3 oder 4 | ≥ 4 Wohnungen, *h* > 7 m |
| Geschosswohnungsbau in Holz | beliebig | viele | 4 oder 5 | *h* > 13 m (Aufzug), > 22 m (Hochhaus) |
| Randfall Bungalow | freistehend | 1 | 1 | ein Rettungsweg genügt |
| Randfall Tiny House, Modul | freistehend | 1 | 1 | „ortsfest benutzt“ = bauliche Anlage |
| Randfall Wohn- und Geschäftshaus | beliebig | gemischt | 3 bis 5 | kein reines Wohngebäude, Sonderbau-Schwellen |

Die Einordnung ist typisierend. Im Einzelfall folgt die Gebäudeklasse aus Art. 2 Abs. 3 BayBO [@baybo2026] [V]:

- **GK 1**: freistehend, *h* ≤ 7 m, höchstens zwei Nutzungseinheiten mit zusammen höchstens 400 m².
- **GK 2**: wie GK 1, aber nicht freistehend.
- **GK 3**: sonstige Gebäude mit *h* ≤ 7 m.
- **GK 4**: *h* ≤ 13 m und jede Nutzungseinheit höchstens 400 m².
- **GK 5**: sonstige Gebäude.

Dabei ist *h* die Höhe der Fußbodenoberkante des höchstgelegenen Geschosses, in dem ein Aufenthaltsraum **möglich** ist, über dem Mittel der Geländeoberfläche. Die Flächen sind Brutto-Grundflächen ohne Kellergeschosse (Recherche 14, Abschnitt 2.1) [V].

Die bekannte Typologie von IWU und TABULA unterscheidet EFH, RH, MFH, GMH und HH. Sie eignet sich für Kosten- und Energie-Benchmarks, nicht für Rechtsregeln (Recherche 14, Abschnitt 2.10) [V]. Ihre Grenze für das MFH (3 bis 12 Wohnungen) fällt mit keiner Rechtsschwelle zusammen. Die Arbeit übernimmt sie deshalb nur als Anzeigekategorie.

## 9a.2 Merkmalbasierte Profilableitung

### 9a.2.1 Warum der Typ nicht gewählt werden darf

Ein naheliegender Entwurf wäre ein Auswahlmenü „Haustyp“ mit einem Regelprofil je Eintrag. Recherche 14 zeigt an mehreren Kipppunkten, warum das falsch ist [V]:

- Ein Reihen- oder Stadthaus mit ausgebautem Dachgeschoss hat eine Fußbodenoberkante im Dachgeschoss von etwa 8 m und ist damit **GK 4**, obwohl der Kunde „Reihenhaus“ gewählt hat.
- Eine „Villa“ mit einer Wohnung und 450 m² oberirdischer Brutto-Grundfläche ist **GK 3**.
- Eine Einliegerwohnung ist eine **zweite Nutzungseinheit**. Sie bringt Schallschutz nach DIN 4109-1 Tabelle 2, zwei Rettungswege je Wohnung, die Heizkostenverordnung und gegebenenfalls einen Stellplatz nach Satzung.
- Die Höhe misst sich am **möglichen** Aufenthaltsraum. Ein nicht ausgebauter, aber ausbaufähiger Dachraum kann GK 4 auslösen.

Jeder dieser Fälle entsteht durch eine Änderung, die der Kunde im Entwurf vornimmt, ohne den Typ zu wechseln. Ein gewähltes Etikett würde veralten, ohne dass es jemand bemerkt. Das Profil muss deshalb aus dem Modell **abgeleitet** werden und bei jeder relevanten Änderung neu entstehen.

### 9a.2.2 Der Merkmalsvektor

Das Profil ist eine Funktion eines Merkmalsvektors *m*, den die Maschine deterministisch aus dem IFC-Modell und dem Kontext berechnet (Recherche 14, Abschnitt 3):

| Merkmal | Wertebereich | Ableitung aus dem Modell |
|---|---|---|
| `anbau` | freistehend, einseitig, beidseitig | Gebäudeabschlusswände an der Grenze; ein `IfcBuilding` je DHH bzw. RH-Einheit |
| `n_WE`, `n_NE_sonst` | ℕ, mit Nutzungsart und Fläche | `IfcZone` mit `ObjectType` „Wohnung“ bzw. „Gewerbe“ |
| `h_Art2` | m | OKFF des obersten Geschosses mit möglichem Aufenthaltsraum minus mittleres Gelände (DGM) |
| `BGF_NE` | m² je Nutzungseinheit | Flächen der Zone, oberirdisch, ohne Kellergeschosse |
| `keller` | ja/nein je Geschoss | Deckenoberkante im Mittel ≤ 1,40 m über Gelände (Art. 2 Abs. 7) |
| `eigentum` | allein, Realteilung, WEG | Eingabe; Flurstücke als Unter-`IfcSite` |
| `gemeinde` | Gemeindeschlüssel | Satzungen, Einwohnerzahl (> 250 000 für Art. 6 Abs. 5a) |
| `foerderung` | keine, WFB | Eingabe |
| `sonderbau` | Menge von Kennzeichen | Nutzungen nach Art. 2 Abs. 4 bei gemischten Gebäuden |

Aus *m* folgen die Schalter des Profils. Listing 9a.1 zeigt die Ableitung der Gebäudeklasse und der wichtigsten Schalter. Jeder Schalter ist eine Regel mit Quelle im Sinne des Regelschemas aus Kapitel 9.2.3.

**Listing 9a.1: Profilableitung aus dem Merkmalsvektor (Pseudocode)**

```python
def gebaeudeklasse(m) -> int:                       # BayBO Art. 2 Abs. 3 [V]
    summe = sum(m.BGF_NE)                            # oberirdisch, ohne Keller
    n_ne = m.n_WE + m.n_NE_sonst
    if m.h_Art2 <= 7.0 and n_ne <= 2 and summe <= 400.0:
        return 1 if m.anbau == "freistehend" else 2
    if m.h_Art2 <= 7.0:
        return 3
    if m.h_Art2 <= 13.0 and max(m.BGF_NE) <= 400.0:
        return 4
    return 5

def pruefung_statik(m, gk) -> str:                 # Art. 62a [V]
    if m.sonderbau:           return "behoerde_oder_pruefingenieur"
    if gk >= 4:               return "PSV"
    if gk == 3:               return "kriterienkatalog"      # Anlage 2 BauVorlV
    return "keine" if m.wohngebaeude else "kriterienkatalog"  # GK 1/2 Nichtwohnbau [U]

def schalter(m) -> dict:
    gk = gebaeudeklasse(m)
    return {
        "GK": gk,
        "bauvorlage": "Art61_Abs3" if (m.wohngebaeude and gk <= 3 and m.n_WE <= 3
                                       and m.anbau in ("freistehend", "einseitig"))
                      else "Art61_Abs2",
        "pruefung_statik": pruefung_statik(m, gk),
        "pruefung_brand": "PSV_oder_behoerde" if gk == 5 or m.sonderbau else
                          ("bestaetigung_ausfuehrung" if gk == 4 else "keine"),
        "schall_tabellen": ({"Tab3"} if m.haustrennwand else set())      # DIN 4109-1
                           | ({"Tab2"} if m.n_WE + m.n_NE_sonst >= 2 else set()),
        "barrierefrei": m.n_WE > 2,                   # Art. 48 Abs. 1
        "aufzug": m.h_Art2 > 13.0,                    # Art. 37 Abs. 4
        "raumhoehe_240": gk >= 3,                     # Art. 45 Abs. 1
        "abstellraum": gk >= 3,                       # Art. 46 Abs. 2
        "spielplatz": m.gemeinde.satzung_spielplatz and m.n_WE > 5,   # Art. 81 Abs. 1 Nr. 3
        "holzbaurl": gk in (4, 5),                    # BayTB 11/2025, A 2.2.1.4
        "hubrettung": m.bruestung_anleiterstelle > 8.0,               # Art. 31 Abs. 3
    }

SCHWELLEN = [("h_Art2", 7.0, 0.5), ("h_Art2", 13.0, 0.5), ("h_Art2", 22.0, 0.5)]
WE_SCHWELLEN = {2, 3, 5}          # nächste Wohnung ändert Tab2/Bf., Bauvorlage, Spielplatz
```

Das Listing ist eine Verdichtung. Die Detailregeln stehen in Recherche 14, Abschnitt 2, und sind in `spezifikation/regelprofile.yaml` mit Fundstelle hinterlegt. Zwei Einzelheiten sind hervorzuheben.

**Schwellenwarnungen.** Liegt *h* weniger als 0,5 m unter 7, 13 oder 22 m, liegt eine Nutzungseinheit nahe 200 oder 400 m² oder hat das Gebäude 2, 3 oder 5 Wohnungen, warnt das System, bevor die Schwelle überschritten ist. Die Warnung nennt die Folgen, zum Beispiel „+1 Wohnung → Architekt erforderlich, barrierefreie Erreichbarkeit“. Das ist die Anwendung der Vorab-Grenzwerte aus Kapitel 9.6.3 auf den Gebäudetyp. Die Folgen springen und sind teuer. Deshalb muss der Kunde sie vor der Entscheidung sehen.

**Profil ist nicht monoton im Merkmalsvektor.** Mehr Wohnungen oder mehr Höhe bringen fast immer mehr Regeln. Es gibt aber Gegenbeispiele. Der ebenerdige Bungalow bis 400 m² braucht nur einen Rettungsweg (Art. 31 Abs. 1 Satz 2 Nr. 2), und ein Geschoss, das zum Kellergeschoss wird, fällt aus der Flächensumme. Die Monotonie aus Kapitel 9.3.3 gilt zwischen den Schichten eines Profils, nicht zwischen Profilen verschiedener Typen. Wechselt der Typ, wertet das System deshalb **alle** Regeln neu aus und erzeugt einen Delta-Bericht. Das geplante Beispiel B12 (Wechsel EFH → ZFH) soll genau das zeigen.

### 9a.2.3 Nicht deterministische Merkmale

Manche Merkmale lassen sich nicht berechnen. Das deutlichste Beispiel ist das **Doppelhaus**. Planungsrechtlich verlangt es, dass beide Hälften „in wechselseitig verträglicher und abgestimmter Weise“ aneinandergebaut sind. Das Bundesverwaltungsgericht hat 2015 festgehalten, dass sich dies „weder abstrakt-generell noch mathematisch-prozentual“ bestimmen lässt (BVerwG 4 C 12.14, im Anschluss an 4 C 12.98; Recherche 14, Abschnitt 2.7) [V]. Ein Automatismus „GRZ eingehalten → zulässig“ wäre deshalb falsch.

Die Regelmaschine liefert in solchen Fällen **Indikatoren** und das Ergebnis **freigabepflichtig** (Kapitel 9.2.1). Für das Doppelhaus sind die Indikatoren Höhen- und Tiefenversatz, Dachform, Dachneigung und Firstrichtung beider Hälften. Weitere nicht deterministische Merkmale sind:

- ob ein Gebäude mit gemischter Nutzung „Wohngebäude“ ist,
- wie Nutzungseinheiten abzugrenzen sind, etwa bei einer Einliegerwohnung ohne eigenen Zugang,
- ob der Mehraufwand für Barrierefreiheit unverhältnismäßig ist (Art. 48 Abs. 4),
- Abweichungen nach Art. 63 und Vereinbarungen nach dem Modell des Gebäudetyps E (9a.7).

Jeder dieser Fälle erzeugt einen Freigabe-Knoten mit der Rolle, die ihn auflösen darf. Das ist der Punkt, an dem der Regelraum bewusst endet: Wo die Rechtsprechung eine Wertung verlangt, ersetzt das System sie nicht, sondern bereitet sie mit Daten vor.

Ein verwandtes Problem ist die **Begriffsgleichheit bei verschiedener Bedeutung**. „Einseitig angebaut“ steht in Art. 61 Abs. 3 BayBO als Voraussetzung der kleinen Bauvorlageberechtigung. Das GModG definiert „einseitig angebautes Wohngebäude“ dagegen über einen Anbauanteil von mindestens 80 % (§ 3 Abs. 1 Nr. 6) [@gmodg2026] (Recherche 14, Abschnitt 2.8) [V]. Eine numerische Definition in der BayBO wurde nicht gefunden [U]. Das Regelschema verwendet deshalb **quellengebundene Merkmale** (`BayBO.anbau`, `GModG.einseitig_angebaut`) statt eines gemeinsamen Begriffs. Andernfalls würde eine energierechtliche Definition stillschweigend über die Bauvorlageberechtigung entscheiden.

## 9a.3 Matrix Gebäudetyp × Regelbereich

Die folgende Matrix verdichtet Recherche 14. Referenz ist das freistehende EFH der GK 1. „wie EFH“ heißt: kein Delta. Die vollständige, maschinenlesbare Fassung mit Fundstellen steht in `spezifikation/regelprofile.yaml`.

**Tabelle 9a.2: Klasse, Verfahren und Brandschutz**

| Typ | GK | Bauvorlage (Art. 61) | Prüfung Statik / Brand | Brandschutz-Kern |
|---|---|---|---|---|
| EFH | 1 | Abs. 3 möglich | keine / keine | keine Anforderung an tragende Teile; Keller feuerhemmend |
| EFH > 400 m² BGF | 3 | Abs. 3 | Kriterienkatalog / keine | tragende Teile und Decken feuerhemmend; notwendiger Treppenraum |
| EFH + ELW, ZFH | 1 oder 2 | Abs. 3 | keine / keine | zwei Rettungswege **je Wohnung**; Decken in GK 2 feuerhemmend |
| DHH, Reihenendhaus | 2 (Endhaus > 7 m: 4) | Abs. 3 | GK 2 keine; GK 4 PSV Statik | Gebäudeabschlusswand mindestens feuerhemmend (Art. 28 Abs. 2 Satz 2), bis unter die Dachhaut |
| Reihenmittelhaus | 2 (> 7 m: 4) | **nicht Abs. 3** | wie Endhaus | zwei Abschlusswände |
| MFH GK 3 | 3 | ≤ 3 WE und frei/einseitig: Abs. 3; **≥ 4 WE: Abs. 2** | Kriterienkatalog / keine | tragende Teile, Decken, Trennwände, Treppenraum feuerhemmend |
| MFH GK 4 | 4 | Abs. 2 | **PSV Statik immer** / Bestätigung der Bauausführung | hochfeuerhemmend nach HolzBauRL; Treppe nichtbrennbar |
| Holz-Geschossbau GK 5 | 5 | Abs. 2 | PSV Statik **und** PSV Brand bzw. Bauaufsicht | feuerbeständig („abweichend feuerbeständig“ nach HolzBauRL); Treppenraum in Bauart Brandwand, nichtbrennbar |

**Tabelle 9a.3: Schall, Barrierefreiheit und weitere Pflichten**

| Typ | Schallschutz (DIN 4109-1) | Barrierefreiheit, Aufzug | weitere Deltas |
|---|---|---|---|
| EFH | keine Anforderung im eigenen Bereich | – | Stellplatz nur per Satzung |
| EFH + ELW, ZFH | **Tab. 2**: Decke R′w ≥ 54 dB, L′n,w ≤ 53 dB bei Holzdecken nach DIN 4109-33; Wand ≥ 53 dB | – | Heizkostenverordnung (Ausnahme, wenn der Vermieter eine der ≤ 2 Wohnungen bewohnt) |
| DHH, RH | **Tab. 3**: Haustrennwand ≥ 59 dB im untersten Geschoss, darüber **≥ 62 dB**; Decken L′n,w ≤ 41 dB | – | Realteilung oder WEG; GRZ je Baugrundstück |
| MFH GK 3 | Tab. 2 einschließlich Treppenraumwände 53 dB; Wohnungstüren Rw 27 bzw. 37 dB | **> 2 WE**: Wohnungen eines Geschosses barrierefrei erreichbar (DIN 18040-2 ohne „R“) | Raumhöhe ≥ 2,40 m; Abstellräume; Spielplatz nur mit Satzung und > 5 WE; Aufteilungsplan |
| MFH GK 4 | wie GK 3; Aufzugsschachtwand ≥ 57 dB | wie GK 3; kein Aufzugszwang (*h* ≤ 13 m) | Leitungsabschottungen hochfeuerhemmend (LAR) |
| GK 5 | wie GK 3 | **Aufzug** (*h* > 13 m), Kabine 1,10 × 2,10 m; **⅓** der Wohnungen barrierefrei erreichbar; Wohnungstüren 0,90 m | Sicherheitsbeleuchtung in fensterlosen Treppenräumen; Rauchabzug oben |

Die Werte der DIN 4109-1:2018-01 sind an einem Abdruck der Norm geprüft, ihre Einführung in die BayTB nur teilweise [V für die Werte, V/U für die Einführung] (Recherche 14, Abschnitt 2.4). Die Haustrennwand von 62 dB ist im Holzbau praktisch nur zweischalig mit durchgehender Fuge erreichbar, auch in Fundament und Dach [U, Stand der Technik]. Der Bauteilkatalog DIN 4109-33 enthält Holzbauteile [@din4109-33]. Die Übertragbarkeit der Anforderungen zwischen europäischen Ländern ist gering, wie der Vergleich von Rasmussen zeigt [@rasmussen2010sound]. Für die BIM-gestützte Schallberechnung im Holzbau liegt eine deutsche Vorarbeit vor [@chateauvieux2023bim].

Zwei Befunde der Matrix korrigieren verbreitete Annahmen:

- **GK 3 ist nicht „EFH-nah“.** Schon ein großes EFH über 400 m² oder ein Haus mit drei Wohnungen bringt feuerhemmende Bauteile, einen notwendigen Treppenraum, die Raumhöhe von 2,40 m, Abstellräume und den Kriterienkatalog (9a.4).
- **Die bayerische Abschlusswand-Regel weicht von der MBO ab.** Nach Art. 28 Abs. 2 Satz 2 BayBO gilt für GK 1 und 2 statt der Brandwandpflicht Art. 27 entsprechend [V]. Regelsätze, die auf der Musterbauordnung beruhen wie MBO2BIM [@mbo2bim2023; @bmk2024mbo], dürfen deshalb nicht ungeprüft übernommen werden.

## 9a.4 Folgen für die Freigabe-Gates

### 9a.4.1 Berechtigungsreichweite

Das Zielbild setzt voraus, dass die Firma Entwurfsverfasserin ist und eine bauvorlageberechtigte Person die Vorlagen verantwortet (Art. 61 Abs. 6 BayBO; Kapitel 4.3.5). Kapitel 4 hat für den Referenzfall festgestellt, dass dafür auch ein Zimmerermeister genügen kann. Die Typologie zeigt die Grenze dieser Aussage. Nach Art. 61 Abs. 3 Nr. 1 BayBO dürfen Ingenieure der Fachrichtungen Architektur, Hochbau und Bauingenieurwesen, staatlich geprüfte Techniker sowie Maurer-, Betonbauer- und Zimmerermeister nur für „freistehende oder nur einseitig angebaute oder anbaubare Wohngebäude der Gebäudeklassen 1 bis 3 mit nicht mehr als drei Wohnungen“ Bauvorlagen erstellen [@baybo2026] [V]. Der Bayerische Verfassungsgerichtshof hat diese kleine Bauvorlageberechtigung als verfassungsgemäß bestätigt [@bayverfgh1999vf4vii97] [U, nur sekundär belegt]. Die Architektenkammer erläutert die Rechtslage im Merkblatt 7, allerdings noch ohne die Novellen ab 2021 [@byak2019merkblatt7] [U].

Daraus folgt:

- **Reihenmittelhaus** und **Mehrfamilienhaus ab vier Wohnungen** fallen heraus. Für sie braucht es Architekten oder Listen-Ingenieure nach Abs. 2.
- **Wohn- und Geschäftshäuser** sind keine reinen Wohngebäude und fallen ebenfalls heraus [U].
- **Absolventen eines Studiengangs Holzbau und Ausbau** sind nach Abs. 4 Nr. 6 für die Holzbauweise berechtigt. Die Reichweite im Übrigen ist hier nicht geprüft [U].

Die App ordnet deshalb jeder Person eine **Berechtigungsreichweite** zu, also eine Menge von Profilen. Das Gate „Bauvorlage“ ist nur freigebbar, wenn das aktuelle Profil in der Reichweite der benannten Person liegt. Ändert der Kunde den Entwurf so, dass das Profil die Reichweite verlässt, wird eine bereits erteilte Freigabe ungültig. Beispiel: Aus einem Endhaus wird durch Anbau eines weiteren Hauses ein Mittelhaus.

### 9a.4.2 Prüfpflichten

Die Prüfpflichten hängen an der Gebäudeklasse (Recherche 14, Abschnitt 2.2) [V]:

| GK | Standsicherheit (Art. 62a) | Brandschutz (Art. 62b) |
|---|---|---|
| 1, 2 (Wohngebäude) | keine Prüfung; Erklärung des Nachweiserstellers | keine Prüfung |
| 3 | Kriterienkatalog nach Anlage 2 BauVorlV; ist ein Kriterium nicht erfüllt, bescheinigt ein Prüfsachverständiger | keine Prüfung |
| 4 | **immer Prüfsachverständiger** | keine Prüfung, aber Bestätigung der übereinstimmenden Bauausführung durch den Nachweisersteller |
| 5 | immer Prüfsachverständiger | **Prüfsachverständiger** oder Bauaufsicht, mit Bauüberwachung |

Das Prüfwesen beruht auf dem Muster der M-PPVO [@mppvo2012]. Für den Holzbau ist der **Kriterienkatalog** der GK 3 kritisch. Er verlangt unter anderem, dass ein rechnerischer Nachweis der Gebäudeaussteifung nicht erforderlich ist (Nr. 4), dass keine besonderen Schwingungsuntersuchungen nötig sind (Nr. 6) und dass keine besonderen Bauarten wie Leimholzbau vorliegen (Nr. 8) [@bauvorlv] [V]. Ein Holztafel-MFH der GK 3 mit Scheibennachweis, Schwingungsnachweis nach EC 5 und Brettschichtholz erfüllt den Katalog deshalb oft nicht [U, Auslegung].

Ein Teil des Katalogs ist aus dem Modell auswertbar. Enthält das Modell Bauteile aus Brettschichtholz (Material GL), liefert die Regel für Nr. 8 **verletzt**, und das Gate Statik verlangt einen Prüfsachverständigen. Andere Kriterien sind Ingenieurentscheidungen und bleiben **freigabepflichtig**. Die Typenprüfung ersetzt die Prüfung (Art. 62a Abs. 2 Satz 3 Nr. 2). Meacham weist darauf hin, dass vorgefertigte Bauteile und Module andere Nachweis- und Prüfwege brauchen als Aufsichtsmodelle, die auf Kontrollen an vielen Punkten der Bauausführung beruhen [@meacham2022fire]. Für ein Fertighaussystem spricht das für Prüfungen am System statt am Einzelbau (9a.8).

### 9a.4.3 Neue Rollen und Vertragsfolgen

Mit dem Profil ändern sich die Beteiligten. Ab GK 4 kommen Prüfsachverständige für Standsicherheit, ab GK 5 für Brandschutz hinzu, außerdem Brandschutzplaner, bei WEG Notar und Aufteiler und bei Photovoltaik im MFH der Messstellenbetreiber. Den Prüfsachverständigen beauftragt der **Bauherr** (Recherche 14, Abschnitt 4) [V]. Ein Kundenkonfigurator muss das im Vertrag sichtbar machen, mit Kosten und Terminen: Bescheinigung I mit der Baubeginnsanzeige, Bescheinigung II mit der Anzeige der Nutzungsaufnahme. Für die Baubeschreibung nach Art. 249 EGBGB ist das eine Pflichtangabe zum Leistungsumfang [@egbgb249].

## 9a.5 Flächen und Wohnungseigentum

### 9a.5.1 Wohnfläche und Grundflächen

Zwei Flächenbegriffe sind zu trennen, weil sie verschiedenen Regeln dienen:

- Die **Brutto-Grundfläche** nach DIN 277 bestimmt über Art. 2 Abs. 6 BayBO die Gebäudeklasse. Sie ist eine R1-Eingangsgröße. Die Arbeit berechnet sie aus `IfcSpace` und den Mengen `Qto_SpaceBaseQuantities`. Eine eigene Prüfung gegen DIN 277:2021 fand nicht statt [U].
- Die **Wohnfläche** nach der Wohnflächenverordnung ist eine Vertrags- und Förderungsgröße. Nach § 4 WoFlV werden Flächen mit einer lichten Höhe von mindestens 2 m voll angerechnet, zwischen 1 und 2 m zur Hälfte, unbeheizte Wintergärten zur Hälfte und Balkone, Loggien und Terrassen in der Regel zu einem Viertel, höchstens zur Hälfte [V]. Keller, Abstellräume außerhalb der Wohnung, Heizungsräume und Garagen gehören nicht dazu (§ 2 Abs. 3).

Die Wohnfläche ist in IFC nicht nativ vorgesehen. Die Arbeit führt sie als eigene Mengenangabe je `IfcSpace` mit dem Anrechnungsfaktor 1, 0,5 oder 0,25 (Recherche 14, Abschnitt 5). Regelklasse ist R2 (die Angabe muss vorhanden sein) mit R4-Folge (sie erscheint in der Baubeschreibung nach Art. 249 § 2 Nr. 3 EGBGB). Bei Förderung schaltet das Profil zusätzlich die Wohnflächenobergrenzen der Wohnraumförderungsbestimmungen ein, zum Beispiel 55 bzw. 65 m² für zwei Personen (WFB 2023 Nr. 12.2) [V]. Damit wird aus einer Rechengröße eine R1-Grenze.

### 9a.5.2 Wohnungseigentum: Aufteilungsplan und Abgeschlossenheit

Soll ein Mehrfamilienhaus oder ein Doppelhaus nach dem Wohnungseigentumsgesetz aufgeteilt werden, gelten zwei Regeln (Recherche 14, Abschnitt 2.7) [V]:

- Sondereigentum „soll“ nur an **abgeschlossenen** Räumen entstehen (§ 3 Abs. 3 WEG). Stellplätze gelten als Räume. Freiflächen sind möglich, wenn sie mit Maßangaben bestimmt sind.
- Der Eintragungsbewilligung liegen ein von der Baubehörde gesiegelter **Aufteilungsplan**, in dem alle Teile einer Einheit dieselbe Nummer tragen, und die **Abgeschlossenheitsbescheinigung** bei (§ 7 Abs. 4 WEG).

Maßstab ist die Allgemeine Verwaltungsvorschrift vom 12.07.2021, nicht mehr die Bekanntmachung von 1974. Nach der neuen Vorschrift ist die Bescheinigung „ungeachtet bauordnungsrechtlicher Vorschriften“ zu erteilen. Abgeschlossen heißt „baulich vollkommen abgetrennt“ mit eigenem abschließbarem Zugang, der nicht über anderes Sondereigentum führt [V]. Das Landesportal führt noch die Bekanntmachung von 1974. Sie darf nicht als Prüfmaßstab verwendet werden. Das ist ein weiterer Versionierungsfall im Sinne von Kapitel 9.3.2.

Die Abgeschlossenheit ist eine **topologische R1-Regel**. Sie lässt sich als Graphregel über Räume und Türen formulieren (Listing 9a.2).

**Listing 9a.2: Abgeschlossenheit als Graphregel (Pseudocode)**

```text
REGEL DE.WEG.3-3.Abgeschlossenheit              [G, R1, Maßstab AVA 2021, V]
GRAPH  Knoten: IfcSpace; Kanten: IfcDoor bzw. Öffnung zwischen zwei Räumen
       Zuordnung se(raum) ∈ {Einheit 1 … n, Gemeinschaft}
FÜR    jede Einheit E
PRÜFE  (1) es gibt einen Weg von einem Raum in E zu Gemeinschaft oder außen,
           der nur Räume aus E oder Gemeinschaft berührt       # eigener Zugang
       (2) die Tür an der Grenze E → Gemeinschaft ist abschließbar
       (3) keine offene Verbindung zwischen E und einer anderen Einheit
ERGEBNIS  verletzt → Begründung nennt Raum, Tür und fremde Einheit
FOLGE  Aufteilungsplan (R4) = Ableitung mit Nummer je Einheit; Siegel = R3 (Bauaufsicht)
```

Nicht prüfbar sind **Sondernutzungsrechte**. Sie sind schuldrechtlich und stehen in der Gemeinschaftsordnung. Das Modell kann sie als Attribut tragen (`Pset_PropertyAgreement` an `IfcSpace`), aber nicht prüfen. Das Planungsrecht bleibt davon getrennt: GRZ und GFZ gelten je Baugrundstück, bei Realteilung also je Flurstück, bei WEG für das Gesamtgrundstück.

## 9a.6 Holzbau in den Gebäudeklassen 4 und 5

Ab GK 4 wird der Holzbau ein eigenes Regelwerk. Die Muster-Holzbaurichtlinie in der Fassung 2024-09 ist in Bayern mit den BayTB 11/2025 unter der laufenden Nummer A 2.2.1.4 eingeführt [@holzbaurl2024; @baytb2025] [V]. Recherche 14 hat ihre Kernwerte zusammengestellt (Abschnitt 2.3) [V]:

- Das Kapselkriterium K₂60 entfällt. Maßstab ist der **Entzündungsschutz** *t_ch*: hochfeuerhemmend *t_ch* ≥ 60 min, zum Beispiel 2 × 15 mm GKF oder GF; abweichend feuerbeständig *t_ch* ≥ 90 min mit 2 × 18 mm.
- Eine reduzierte Bekleidung (*t_ch* 30) ist bei Nutzungseinheiten bzw. Raumgruppen bis 200 m² möglich.
- Dämmstoffe in und auf den Bauteilen müssen **nichtbrennbar** sein, einen **Schmelzpunkt ≥ 1000 °C** haben und das Gefach füllen. Ausgenommen ist der Fußbodenaufbau.
- Holztafelbau ist jetzt auch in GK 5 zulässig. Brandwände und Treppenraumwände bleiben in GK 5 nichtbrennbar.
- Holzfassaden in GK 4 und 5 brauchen horizontale Brandsperren geschossweise mit höchstens 4 m Abstand.
- Bayern verzichtet auf eine Bauartgenehmigung auch außerhalb des Anwendungsbereichs, etwa in GK 3, wenn nach den Anhängen der Richtlinie nachgewiesen wird.

Für den Regelraum hat das drei Folgen.

**Katalogfilter statt Einzelprüfung.** Die Bauteilaufbauten des Herstellers tragen Merkmale wie Feuerwiderstand, *t_ch*, Brennbarkeit und Schmelzpunkt der Dämmung sowie R′w und L′n,w. Das Profil filtert den Katalog, bevor der Kunde wählt. In GK 4 und 5 fallen damit alle Wandaufbauten mit Holzfaser- oder Zellulosedämmung weg. Die Wand aus B1 und B3 mit 200 mm Holzfaser im Gefach wäre in GK 4 nicht wählbar. Der Kunde sieht sie gar nicht erst, statt sie zu wählen und abgelehnt zu werden. Das ist Konformität durch Konstruktion (Kapitel 9.6) auf der Ebene des Katalogs. Kapitel 3 formuliert dieselbe Folge als Anforderung ANF-03-08.

**Die Ausnahme für den Fußbodenaufbau ist eine Vorbedingung.** Die Holzfaser-Trittschalldämmplatte im Trockenaufbau der Holzbalkendecke aus B14 (Variante B) liegt im Fußbodenaufbau. Nach der Ausnahme der Richtlinie bleibt sie in GK 4 zulässig. Im Regelschema steht diese Ausnahme im Feld `vorbedingung.ausnahmen`, nicht in der Prüffunktion. So bleibt sie als Rechtsauslegung sichtbar und kann einzeln bestätigt werden.

**Die IDS-Grenze wird praktisch.** Die Anforderung „nichtbrennbare Dämmung in hochfeuerhemmenden Bauteilen“ hängt an einem Merkmal des umgebenden Bauteils. IDS kann das nicht in der Anwendbarkeit ausdrücken (Kapitel 9.2.2). Der Generator schreibt die Anforderung deshalb beim Erzeugen an das Dämmteil. Die IDS prüft dann das Merkmal am Teil, und die Regelmaschine prüft die Beziehung. Das ist dieselbe Arbeitsteilung wie beim U-Wert, nur mit umgekehrter Richtung.

Für das Brandschutzmodul ab GK 4 gibt es internationale Vorarbeiten zur automatisierten Prüfung, etwa für hohe Holzgebäude [@kincelova2020fire]. Konstruktive Grundlagen des mehrgeschossigen Holzbaus fasst das Handbuch von Kaufmann et al. zusammen [@kaufmann2018manual]. Keine dieser Arbeiten bildet die HolzBauRL 2024 ab. Die Arbeit führt den Holzbau in GK 4 und 5 deshalb als **eigenes Modul** mit eigener Regelwerk-Version. So bleibt der Kern für das Einfamilienhaus schlank, und der Übergang nach dem Einleitungsdatum des Verfahrens lässt sich im Modul selbst abbilden (Kapitel 9.3.2).

## 9a.7 Gebäudetyp E (Stand 27.09.2026)

Der Gebäudetyp E soll das Bauen einfacher und billiger machen, indem von Komfortstandards abgewichen werden darf. Dass Ausstattungsstandards im Wohnungsbau ein Kostenfaktor sind, untersucht das BBSR [@eisele2024standards]. Der Rechtsstand ist unfertig (Recherche 14, Abschnitt 2.9):

- **Bund [V/U, Presse].** Ein Entwurf wurde am 07.07.2026 als „fertig“ vorgestellt. Nach Stand 15. bis 21.09.2026 ist er noch in der Frühkoordinierung zwischen den Ressorts, ein Kabinettsbeschluss liegt nicht vor. Ziel nach den Eckpunkten vom 20.11.2025 ist ein **Gebäudetyp-E-Vertrag**: Die Abweichung von den anerkannten Regeln der Technik soll kein Mangel sein, wenn der Verbraucher in Textform aufgeklärt wurde. Der Entwurf von 2024 (BT-Drs. 20/13959) ist verfallen.
- **Bayern [V].** Rechtsgrundlage ist Art. 63 BayBO, der Abweichungen auch „zur Erprobung neuer Bau- und Wohnformen“ erlaubt. Seit 12/2023 laufen 19 Pilotprojekte. Das erste fertige Projekt in Ingolstadt hat 15 Wohnungen und liegt etwa 15 % unter den üblichen Kosten. Ein Münchner Projekt in Holzbau unterhalb der Hochhausgrenze wendet die HolzBauRL vorab an, reduziert den Schallschutz und spart über 11 %.

Für das Regelwerk-Profil folgt daraus eine klare Grenze. Der Gebäudetyp E ist ein Schalter „vertraglich vereinbarter Standard“, der **nur Regeln der Schicht *S*₃** aussetzen kann, also anerkannte Regeln der Technik wie den erhöhten Schallschutz nach DIN 4109-5 oder Komfortwerte, die nicht bauaufsichtlich eingeführt sind. Er kann nie Regeln der Schichten *S*₁ und *S*₂ aussetzen, also BayBO-Mindestanforderungen und eingeführte Technische Baubestimmungen. Das ist genau die kontrollierte Nicht-Monotonie aus Kapitel 9.3.3 mit der Nebenbedingung *W* ∩ (*S*₁ ∪ *S*₂) = ∅. Für Abweichungen von *S*₁ bleibt der Weg über Art. 63. Ab GK 4 ist dafür keine Zulassung nötig, wenn ein Prüfsachverständiger bescheinigt (Art. 63 Abs. 1 Satz 3) [V].

Weil der Bundesentwurf nicht beschlossen ist, implementiert die Arbeit den Schalter als **Profilvariante ohne Rechtswirkung**. Sie zeigt, welche Regeln betroffen wären, und erzeugt die Aufklärung in Textform als R4-Dokument. Rechtsverbindlich wird sie erst mit Inkrafttreten, und dann mit Geltungszeitraum und Stichtagsregel nach Kapitel 9.3.1. Ein Risiko bleibt bestehen: Die bayerische Begleitforschung nennt Urteile, nach denen der erhöhte Schallschutz faktisch erwartet wird (Recherche 14, Abschnitt 2.4) [U]. Eine Absenkung unter diese Erwartung ist deshalb auch mit Gebäudetyp-E-Vertrag vertraglich riskant.

## 9a.8 Typengenehmigung für serielles Bauen (Art. 73a BayBO)

Die Typengenehmigung nach Art. 73a BayBO ist für ein System aus vorgefertigten Bauteilen die rechtlich interessanteste Option. Sie wurde mit der Novelle 2020 eingeführt. Die Begründung versteht sie ausdrücklich als Baukastensystem und verlangt, dass sich „die Reichweite der Veränderbarkeit … zweifelsfrei ergeben“ muss [@landtagby2020baybonovelle] [V]. Mit dem Ersten Modernisierungsgesetz 2024 entfiel die Befristung. Seitdem gelten Ortsgestaltungssatzungen nicht, Festsetzungen des Bebauungsplans aber schon [@landtagby2024modernisierung] [V]. Die weiteren Eigenschaften nach Recherche 14 [V]:

- Die oberste Bauaufsichtsbehörde erteilt sie, auch für ein „System aus Bauteilen“ mit festgelegter Veränderbarkeit.
- Sie gilt als bautechnischer Nachweis für Standsicherheit, Brand- und Schallschutz, soweit sie diese regelt.
- Sie ersetzt nicht das Genehmigungsverfahren.
- Typengenehmigungen anderer Länder gelten in Bayern.

Muster ist § 72a MBO, seit dem Beschluss der Bauministerkonferenz vom 22.02.2019 [@bmk2024mbo]. Die erste bayerische Typengenehmigung für Wohngebäude erhielt 2025 ein System mit Holzmassivwänden für vier bis acht Obergeschosse [@stmb2025typengenehmigung]. Die Bewertung der Praxis ist gespalten. Die Verbände HDB und GdW sahen 2023 „im Moment keinen Vorteil“ [@hdbgdw2023typengenehmigung]. Der ZIA fordert, § 72a MBO nach bayerischem Vorbild zu einem gebundenen Anspruch zu stärken [@zia2023seriell]. Beide sind Interessenverbände. Die Stellungnahme des baden-württembergischen Ministeriums gibt eine amtliche Auskunft zur Anwendungspraxis [@landtagbw2023typengenehmigung].

**Formalisierung.** Im Regelraum ist eine Typengenehmigung ein eigenes Profil *T* mit Lösungsraum *L*(*T*). Er ist der genehmigte Veränderungsspielraum. Die Forderung der Begründung, dass sich die Reichweite der Veränderbarkeit „zweifelsfrei“ ergeben muss, ist die Forderung nach einem **formal spezifizierten** Lösungsraum. Genau das leistet das Regelschema aus Kapitel 9.2.3. Für einen Entwurf *x* gilt dann:

- **x ∈ L(T):** Die typengeregelten bautechnischen Nachweise gelten als erbracht. Für die Standsicherheit entfällt die Prüfung als Typenprüfung (Art. 62a Abs. 2 Satz 3 Nr. 2). Die übrigen Regeln des Profils, insbesondere der Bebauungsplan, gelten weiter.
- **x ∉ L(T):** Der Entwurf verlässt die Typengenehmigung. Die Nachweise sind einzeln zu führen, und das Gate Statik folgt wieder der Tabelle in 9a.4.2.

Für die App ist das mehr als eine Rechtsoption. Deckt sich der Konfigurationsraum des Kunden mit *L*(*T*), dann ist jede Konfiguration, die das System zulässt, auch typengenehmigt. Die Grenze der Typengenehmigung wird zur **R1-Regel mit eigener Quelle**, und die Ablehnung eines Kundenwunsches nennt sie als Grund: „Diese Änderung verlässt die Typengenehmigung; Statik und Brandschutz müssen dann einzeln nachgewiesen werden (Mehrkosten, Prüfsachverständiger).“ Kapitel 4.3.4 hat diese Option angekündigt. Sie ist im Zielbild die stärkste Form der Konformität durch Konstruktion, weil die Behörde den Lösungsraum einmal prüft und nicht jeden Entwurf.

## 9a.9 Zwischenfazit

Die Typologie ergänzt den Regelraum aus Kapitel 9 in vier Punkten:

1. **Profil aus Merkmalen.** Das Regelprofil ist eine Funktion eines Merkmalsvektors aus Anbau, Zahl und Fläche der Nutzungseinheiten, Höhe nach Art. 2, Kellereigenschaft, Eigentum, Gemeinde und Förderung. Der Haustyp ist nur Startwert. Schwellenwarnungen zeigen die springenden Folgen vor der Entscheidung.
2. **Grenzen der Berechenbarkeit.** Doppelhaus-Eigenschaft, Wohngebäude-Eigenschaft bei gemischter Nutzung und Unverhältnismäßigkeit sind freigabepflichtig. Gleichlautende Begriffe verschiedener Quellen werden quellengebunden geführt.
3. **Gates am Profil.** Die kleine Bauvorlageberechtigung endet bei freistehenden oder einseitig angebauten Wohngebäuden der GK 1 bis 3 mit höchstens drei Wohnungen. Ab GK 4 prüft immer ein Prüfsachverständiger die Standsicherheit, ab GK 5 auch den Brandschutz. Die App prüft die Berechtigungsreichweite bei jeder Änderung neu.
4. **Holzbau ab GK 4 als Modul, Typengenehmigung als Profil.** Die HolzBauRL 2024 wirkt als Katalogfilter. Der Gebäudetyp E darf nur Schicht *S*₃ aussetzen und ist bis zum Inkrafttreten eine Profilvariante ohne Rechtswirkung. Eine Typengenehmigung nach Art. 73a ist ein Profil, dessen Lösungsraum die Behörde einmal prüft.

## 9a.10 Umsetzungsvorgaben für die App

Es gelten die Regeln aus Kapitel 3.7 und 9.9. Die Matrix aus 9a.3, der Merkmalsvektor, die Schalter und die Gates stehen maschinenlesbar in `spezifikation/regelprofile.yaml`. Die typabhängigen Regeln stehen in `spezifikation/regelkatalog.yaml` (Kennungen unten). Die Referenzfälle sind Testfälle mit konstruierten Merkmalsvektoren, weil ein lauffähiges Beispiel für die Typumschaltung (B12) noch aussteht.

### 9a.10.1 Anforderungen

**Profilableitung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09a-01 | Muss | Das Profil wird aus dem Merkmalsvektor abgeleitet und bei jeder relevanten Modelländerung neu berechnet; der gewählte Haustyp ist nur Startwert. | 9a.2.1 | Start „Reihenhaus“, DG ausgebaut, `h_Art2` = 8,0 m: GK 4, Schalter `holzbaurl` aktiv. Start „EFH“, 1 WE, 450 m² BGF: GK 3, `raumhoehe_240` aktiv. |
| ANF-09a-02 | Muss | Gebäudeklasse nach `BY.BayBO.2-3.Gebaeudeklasse`; *h* bezieht sich auf das oberste Geschoss mit **möglichem** Aufenthaltsraum. | 9a.1, Listing 9a.1 | (frei, 6,5 m, 2 NE, 380 m²) → 1; (einseitig, 6,5 m, 1 NE, 150 m²) → 2; (frei, 6,9 m, 3 NE, 300 m²) → 3; (12,5 m, max. NE 380 m²) → 4; (12,5 m, eine NE 420 m²) → 5. Nicht ausgebauter, ausbaufähiger Dachraum auf 7,6 m: zählt für *h*. |
| ANF-09a-03 | Muss | Schwellenwarnungen nach `BY.Profil.Schwellenwarnung` nennen die Folgen vor der Überschreitung. | 9a.2.2 | `h_Art2` = 6,6 m: Warnung „GK-Sprung bei > 7 m“. 3 WE: Warnung „+1 Wohnung → Architekt oder Listen-Ingenieur (Art. 61 Abs. 2)“. 2 WE: Warnung „+1 Wohnung → barrierefreie Erreichbarkeit“. |
| ANF-09a-04 | Muss | Ein Profilwechsel löst die vollständige Neuauswertung und einen Delta-Bericht aus (B12). | 9a.2.2 | EFH → EFH mit ELW: Bericht nennt neu aktiv `DE.DIN4109-1.Tab2-Trennbauteile`, Rettungswege je Wohnung, HeizkostenV; keine neue Anforderung an die Bauvorlageberechtigung. |
| ANF-09a-05 | Muss | Nicht deterministische Merkmale liefern `freigabepflichtig` mit Indikatoren, nie `erfuellt`. | 9a.2.3 | Zwei Hälften mit verschiedener Firstrichtung und 1,5 m Höhenversatz: `BY.BauNR.Doppelhaus` = `freigabepflichtig`, Indikatoren gelistet, Gate „Bauvorlage“ wartet auf Freigabe. |
| ANF-09a-06 | Muss | Merkmale sind quellengebunden; gleichlautende Begriffe verschiedener Gesetze werden getrennt geführt. | 9a.2.3 | Anbauanteil 70 %: `GModG.einseitig_angebaut` = nein; `BayBO.anbau` = einseitig bleibt; Schalter `bauvorlage` = `Art61_Abs3` unverändert. |

**Gates und Rollen**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09a-07 | Muss | Jede Person hat eine Berechtigungsreichweite; das Gate „Bauvorlage“ ist nur frei, wenn das Profil darin liegt. Eine Freigabe verfällt, wenn das Profil die Reichweite verlässt. | 9a.4.1 | Zimmerermeister, Reihenendhaus GK 2: Gate frei. Anbau eines weiteren Hauses (Mittelhaus): Freigabe ungültig, Meldung „Architekt oder Listen-Ingenieur (Art. 61 Abs. 2)“. MFH mit 4 WE: Gate gesperrt. |
| ANF-09a-08 | Muss | Prüfpflichten nach `BY.BayBO.62a-62b.Pruefpflichten`; Kriterium Nr. 8 des Kriterienkatalogs wird aus dem Modell ausgewertet. | 9a.4.2 | GK 3 mit einem Bauteil aus Brettschichtholz: „PSV Standsicherheit erforderlich“. GK 4: PSV Statik + Bestätigung Bauausführung Brandschutz. GK 5: zusätzlich PSV Brandschutz. GK 2 Wohngebäude: keine Prüfung. |
| ANF-09a-09 | Muss | Wird ein Prüfsachverständiger erforderlich, nennt die Baubeschreibung Beauftragung durch den Bauherrn, Kosten und Termine der Bescheinigungen. | 9a.4.3 | Profil GK 4: Baubeschreibung enthält Abschnitt „Prüfsachverständiger“ mit „Bescheinigung I mit Baubeginnsanzeige“ und „Bescheinigung II mit Nutzungsaufnahme“; GK 2: Abschnitt fehlt. |
| ANF-09a-10 | Muss | Die Matrix Gebäudetyp × Regelbereich wird aus `regelprofile.yaml` geladen, nicht im Code gepflegt. | 9a.3 | Ladeprüfung: jede in `regelprofile.yaml` genannte Regel-ID existiert im Katalog; jedes Profil des Katalogs ist registriert (Stand 27.09.2026: 0 Abweichungen). |

**Typabhängige Regeln**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-09a-11 | Muss | Schallschutz nach Tab. 2 bzw. Tab. 3 je Schalter `schall_tabellen`; der Bauteilkatalog wird vorab gefiltert. | 9a.3 | DHH, Haustrennwand OG mit R′w = 60 dB: `verletzt` (≥ 62 dB); im untersten Geschoss 60 dB: `erfuellt` (≥ 59 dB). ZFH, Holzdecke L′n,w = 52 dB: `erfuellt` (≤ 53 dB). |
| ANF-09a-12 | Muss | Wohnfläche nach `DE.WoFlV.Wohnflaeche` je `IfcSpace` mit Anrechnungsfaktor; Ausgabe in der Baubeschreibung. | 9a.5.1 | DG-Raum 10 m², davon 6 m² mit ≥ 2 m und 4 m² mit 1–2 m: 8,0 m². Balkon 8 m²: 2,0 m². Kellerraum: 0 m². |
| ANF-09a-13 | Muss | Abgeschlossenheit nach `DE.WEG.3-3.Abgeschlossenheit` mit Maßstab AVA 2021. | 9a.5.2 | MFH, Wohnung 2 nur durch Wohnung 1 erreichbar: `verletzt`, Meldung nennt Tür und fremde Einheit. Profil mit Maßstab „AVV 1974“: Ladefehler. |
| ANF-09a-14 | Muss | HolzBauRL-Dämmstoffregel als Katalogfilter in GK 4/5, mit Ausnahme Fußbodenaufbau (vgl. ANF-03-08). | 9a.6 | GK 4: Wandaufbau B1/B3 (Holzfaser im Gefach) nicht wählbar; Aufbau B14 Variante B (Holzfaser-Trittschall im Fußboden) wählbar. GK 2: beide wählbar. |
| ANF-09a-15 | Muss | Entzündungsschutz *t_ch* nach `DE.HolzBauRL.Entzuendungsschutz`. | 9a.6 | GK 4, tragende Wand mit Katalogwert *t_ch* = 30 min und NE 350 m²: `verletzt` (≥ 60 min); gleiche Wand bei NE 180 m²: `erfuellt` (reduziert, ≤ 200 m²). |
| ANF-09a-16 | Muss | Gebäudetyp E ist eine Profilvariante ohne Rechtswirkung; sie kann nur Regeln der Schicht S3 aussetzen und erzeugt die Aufklärung in Textform. | 9a.7 | Variante aktiv, Aussetzung einer S3-Regel (erhöhter Schallschutz): zulässig, Aufklärungsdokument erzeugt, Nachweis „vertraglich abweichend, ohne Rechtswirkung“. Aussetzung von `DE.DIN4109-1.Tab2-Trennbauteile` (S2): abgewiesen. |
| ANF-09a-17 | Soll | Eine Typengenehmigung ist ein Profil *T*; ein Entwurf außerhalb *L*(*T*) wird gemeldet und das Gate Statik neu bestimmt. | 9a.8 | Testprofil *T* mit 4–8 Obergeschossen: Entwurf mit 9 OG → Meldung „verlässt Typengenehmigung“, Gate Statik = PSV. Entwurf mit 6 OG: Typenprüfung ersetzt Prüfung. |
| ANF-09a-18 | Muss | Schalter `barrierefrei`, `aufzug`, `raumhoehe_240`, `abstellraum` aktivieren die zugehörigen Regeln. | 9a.3 | 3 WE, GK 3: Barrierefreiheit (ein Geschoss), Raumhöhe 2,40 m, Abstellraum aktiv; Raum mit 2,35 m: `verletzt`. *h* = 13,5 m: Aufzug mit Kabine 1,10 × 2,10 m gefordert. |
| ANF-09a-19 | Muss | Stellplatz- und Spielplatzpflicht nur über eine Satzungsdatenbank je Gemeinde. | 9a.3 | Gemeinde ohne Satzung: keine Stellplatzpflicht. Testsatzung mit 2 Stellplätzen je Wohnung und 1 geplantem bei 1 WE: `verletzt`. 6 WE mit Spielplatzsatzung: Spielplatz gefordert; 5 WE: nicht. |

## Verwendete Schlüssel

Das Kapitel enthält 26 Zitatstellen zu 24 Schlüsseln. Ein Python-Abgleich aller `[@key]` im Text gegen `literatur/lit-*.bib` ergab am 27.09.2026 keine fehlenden Schlüssel. Der Schlüssel `mbo2bim2023` steht in zwei Bib-Dateien (bekannte Dublette, siehe `literatur/KORREKTUREN.md`); zugeordnet ist die erste Datei. Rechtsprechung (BVerwG 4 C 12.98, 4 C 12.14), WEG, WoFlV, AVA 2021, DIN 4109-1 und der Stand zum Gebäudetyp E haben keinen Schlüssel im Literaturverzeichnis; sie sind über Recherche 14 belegt und im Text so ausgewiesen.

**lit-A-acc-bim.bib** (1): `mbo2bim2023`

**lit-B-vorfertigung-ki.bib** (1): `kaufmann2018manual`

**lit-C-recht-normen.bib** (7): `bauvorlv`, `baybo2026`, `baytb2025`, `din4109-33`, `egbgb249`, `gmodg2026`, `holzbaurl2024`

**lit-D-vergleich-vorfertigung.bib** (1): `chateauvieux2023bim`

**lit-G-luecken.bib** (1): `eisele2024standards`

**lit-H-ff4-ff5.bib** (1): `landtagbw2023typengenehmigung`

**lit-I-schneeball-a.bib** (1): `kincelova2020fire`

**lit-J-schneeball-runde2.bib** (1): `rasmussen2010sound`

**lit-K-ff4-jur.bib** (8): `bayverfgh1999vf4vii97`, `bmk2024mbo`, `byak2019merkblatt7`, `hdbgdw2023typengenehmigung`, `landtagby2020baybonovelle`, `landtagby2024modernisierung`, `stmb2025typengenehmigung`, `zia2023seriell`

**lit-L-schneeball-runde3.bib** (1): `meacham2022fire`

**lit-M-nachweis.bib** (1): `mppvo2012`

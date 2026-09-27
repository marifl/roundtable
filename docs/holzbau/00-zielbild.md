# Zielbild: Vom Kundenwunsch bis ins Werk in einer IFC-Datei

Status: Entwurf v0.1 (27.09.2026). Aussagen mit **[prüfen]** hängen an laufender Recherche.

Aufbau nach Simon Sineks Golden Circle: erst Why, dann How, dann What.

---

## 1. Why

**Fertighauskunden entwerfen ihr Haus selbst, innerhalb der Regeln der Firma.**

Damit kann sich jede Rolle wieder auf ihre eigentliche Arbeit konzentrieren:

| Rolle | Heute | Im Zielbild |
|---|---|---|
| Kunde | wartet auf Planstände, formuliert Wünsche über Dritte | entwirft selbst, sieht Kosten und Folgen sofort |
| Vertrieb | zeichnet, rechnet nach, trägt Änderungen hin und her | berät und verkauft |
| Architekt | setzt Kundenwünsche in Pläne um, wiederholt Standardarbeit | gestaltet Hausmodelle und Regelraum, prüft Sonderwünsche, unterschreibt den Bauantrag |
| Ingenieur | tippt Geometrie für Statik und Energie ab | definiert Bemessungsregeln, prüft und unterschreibt Nachweise |
| Werk | bekommt Pläne, modelliert für die Fertigung neu | bekommt eine freigegebene Datei, leitet Maschinendaten ab |

Kurz: **Niemand tippt etwas ab, was schon im Modell steht.**

---

## 2. How (Prinzipien)

1. **Eine Datei ist die Wahrheit.** Pro Projektstand gibt es genau ein IFC. Alles, was für die Baupraxis relevant ist, steht darin: Geometrie, Aufbauten, Mengen, Kosten, Freigaben, Bauantragsdaten, Fertigungsteile.
2. **Nur der Standard, keine Eigenbauten.** IFC 4.3 (ISO 16739-1:2024) **[prüfen]** ohne proprietäre Erweiterungen, die andere Programme nicht lesen. Jede Version muss den buildingSMART Validation Service bestehen **[prüfen: was er genau prüft]**.
3. **Programme interpretieren, sie besitzen nichts.** CAD, Statik, Energie, Kalkulation und Werk lesen die Datei. Was sie zurückliefern, fließt über das Parametermodell wieder ins IFC.
4. **Andere Formate sind nur Ableitungen.** BTLx (Abbund), Maschinendaten für Wandanlagen **[prüfen: WUP?]**, GAEB, XBau und PDF-Pläne werden aus dem IFC erzeugt und nie von Hand bearbeitet.
5. **Die Regeln der Firma sind Daten, kein Code.** Katalog, Aufbauten, Preise und Grenzen liegen als prüfbare Dateien vor (IDS plus Katalog) **[prüfen: IfcProjectLibrary vs. separate Dateien]**. Die Firma ändert Regeln, ohne dass jemand programmiert.
6. **Nichts erfinden, alles übernehmen.** Deutsche Gesetze, Normen, Fachregeln des Handwerks und vorhandene Open-Source-Bausteine werden zusammengeführt. Eigenentwicklung nur dort, wo nachweislich nichts existiert.
7. **Die KI versteht, der Code entscheidet.** Das Sprachmodell erkennt nur die Absicht. Maße, Regeln, Statik und Kosten berechnet deterministischer Code. So ist jedes Ergebnis nachvollziehbar und reproduzierbar.
8. **Menschen unterschreiben, was das Gesetz verlangt.** Bauvorlageberechtigte und Nachweisberechtigte geben frei **[prüfen: BayBO Art. 61, 62]**. Ihre Freigabe steht als Freigabe-Eintrag im IFC **[prüfen: IfcApproval]**.

---

## 3. What (der Endzustand)

### 3.1 Ein Durchlauf, wie er am Ende aussehen soll

1. **Idee.** Familie H. öffnet die App, wählt ein Regnauer-Hausmodell und ihr Grundstück. Flurstück und Bebauungsplan werden geladen **[prüfen: ALKIS, XPlanung Bayern]**.
2. **Entwurf.** Sie sagt: „Das Bad oben einen Meter größer, Richtung Süden.“ Das Modell ändert sich, Kosten, Wohnfläche, Energiewert und Abstandsflächen aktualisieren sich sofort. Unzulässiges lehnt die App mit Grund und Alternative ab.
3. **Angebot und Vertrag.** Aus der Datei entstehen Angebot und Baubeschreibung nach BGB §650j **[prüfen: Mindestinhalte]**.
4. **Bemusterung.** Fliesen, Fenster, Treppe, Sanitär werden als Produkttypen aus dem Katalog gewählt und stehen im IFC.
5. **Freigabe durch Fachleute.** Architekt und Ingenieur sehen nur Abweichungen vom Regelraum und bestätigen. Ihre Freigabe wird in der Datei vermerkt.
6. **Bauantrag.** Aus derselben Datei werden Bauvorlagen erzeugt: IFC, Pläne als PDF, Formulare, XBau-Nachricht **[prüfen: was Bayern digital akzeptiert]**.
7. **Werkplanung und Fertigung.** Die freigegebene Datei enthält jedes Wandelement mit Ständern, Beplankung, Dämmung, Folie und Verbindungsmitteln. Daraus entstehen die Maschinendaten.
8. **Montage und Übergabe.** Montagereihenfolge und Elementnummern stehen im IFC. Der Kunde bekommt bei der Übergabe dieselbe Datei als Hausakte.

### 3.2 Was in der Datei lebt, Phase für Phase

| Phase | Inhalt im IFC (vorläufig) | Freigabe durch | Abgeleitete Exporte |
|---|---|---|---|
| Entwurf | Geschosse, Räume, Wände, Dach, Fenster, Möbel | Kunde | Visualisierung |
| Angebot | Mengen, Kostenpositionen nach DIN 276 **[prüfen]** | Vertrieb | Angebots-PDF |
| Vertrag | Baubeschreibung als Dokumentverweis, Variantenstand | Kunde + Firma | Vertrag, Baubeschreibung |
| Bemusterung | Produkttypen mit Hersteller und Artikel | Kunde | Bemusterungsprotokoll |
| Bauantrag | Grundstück georeferenziert, Beteiligte, Genehmigungsdaten **[prüfen: IfcPermit]** | Bauvorlageberechtigte | PDF-Pläne, XBau |
| Nachweise | Aufbauten mit U-Wert, Brand- und Schallklasse, Raumbegrenzungen, Lasten | Ingenieur | Eingangsdaten Statik und GEG |
| Fertigung | Elemente mit allen Teilen, Bearbeitungen, Verbindungsmitteln | Werkplanung | BTLx, Maschinendaten |
| Montage | Elementreihenfolge, Transport **[prüfen: IfcTask]** | Bauleitung | Montageplan |
| Übergabe | Produkte, Wartungsdaten **[prüfen: COBie]** | Firma | Hausakte |

---

## 4. Erfolgskriterien (Vorschlag, messbar)

1. Ein Kunde erreicht ohne Mitarbeiter einen zulässigen, kalkulierten Entwurf.
2. Zwischen Vertrag und Werk wird **null Mal** neu modelliert oder abgetippt.
3. Jede IFC-Version besteht die Standardprüfung und alle Firmen-IDS.
4. Bauantragsunterlagen entstehen vollständig aus der Datei.
5. Maschinendaten entstehen vollständig aus der Datei.
6. Die Durchlaufzeit Vertrag → Produktionsfreigabe sinkt messbar. Den Ausgangswert liefert Regnauer.

---

## 5. Bekannte harte Grenzen (vorläufig)

1. **Unterschriften bleiben menschlich.** Bauantrag, Statik und GEG-Nachweis unterschreiben Berechtigte.
2. **Maschinen lesen kein IFC.** Maschinendaten sind immer ein Export.
3. **Normtexte sind geschützt.** Normwerte und Regeln lassen sich umsetzen, Texte nicht übernehmen **[prüfen: EuGH C-588/21 P]**.
4. **Regnauers interne Daten** (Bauteilkatalog, Preise, Fertigungssoftware) sind nicht öffentlich.

---

## 6. Offene Entscheidungen

1. Zielkunde der ersten Version: nur Regnauer oder von Anfang an mehrere Hersteller?
2. Erste Ausbaustufe: bis Vertrag, bis Bauantrag oder bis Werk?
3. Wo liegen die Firmenregeln: im IFC selbst oder als IDS-Dateien neben dem IFC?

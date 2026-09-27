# 27 Juristische Lückenrecherche FF4 (Verantwortung): frei zugängliche Quellen

Status: v0.1 (27.09.2026). Diese Recherche schließt die in `23-lueckenrecherche-ff4-ff5.md` („Was nicht gefunden wurde“, Nr. 1, 2, 4, 8) offen gebliebenen juristischen Fragen, soweit das ohne beck-online und juris möglich ist. Die 74 neuen Einträge stehen in `../arbeit/literatur/lit-K-ff4-jur.bib`. Dubletten zu `quellen-master.csv` und allen `lit-*.bib` sind ausgeschlossen (Abgleich über Key, DOI, Aktenzeichen und Drucksachennummer). Quellen, die schon vorhanden sind, werden mit ihrem Key genannt, zum Beispiel `baybo2026`, `aiact2024`, `eu2014eidas`, `bgh2002genehmigungsplanung`, `bayika2026ki` und `bayDigitalisierungEntwurf2026`.

Recherchebefund, keine Rechtsberatung.

**Prüfweg.**
- **Rechtsprechung:** Gericht, Datum, Aktenzeichen und Fundstellen stammen von der dejure.org-Vernetzungsseite. Wo verfügbar, wurde der Volltext gelesen: BGH-PDF, NRWE, gesetze-bayern.de, EUR-Lex oder ein Kanzleiabdruck (dann als solcher genannt).
- **Gesetzesmaterialien:** Sie wurden an der Drucksache selbst geprüft (dserver.bundestag.de, bayern.landtag.de). Gelesen wurden jeweils die Begründung zur einschlägigen Vorschrift.
- **Aufsätze:** Die Metadaten stammen aus Crossref (`api.crossref.org/works/{DOI}/transform/application/x-bibtex`). Alle Aufsätze sind Open Access, die Kernaussage wurde am Abstract oder Volltext geprüft.
- **Zugriff:** Der Direktzugriff (curl) auf bayern.landtag.de, crossref.org und dejure.org wird vom Proxy abgewiesen. Alle Abrufe liefen deshalb über den Exa-Fetch.

**Legende.**
- **Typ:** N = Norm, Gesetzesmaterial oder Rechtsprechung; W = Wissenschaft; G = graue Literatur (Kammer, Verband, Behörde ohne Normcharakter, Expertenbericht, Leitlinie).
- **Passung FF4:** Skala 0–3 nach 2a.5.
- **Status:** [V] = an der Fundstelle geprüft; [U] = Teilangabe unsicher, der Grund steht in der Zeile und im `note`-Feld.

---

## Ergebnis in 5 Punkten

1. **Wer freigibt, übernimmt die Planung. Der Kundenentwurf ist eine Vorleistung und entlastet die Firma nicht.**
   - Wer eine fremde Planung fortführt, muss sie im Rahmen des Zumutbaren selbst prüfen und Bedenken dem Besteller mitteilen (BGH, 15.01.2026, VII ZR 119/24). Wer sie umfassend übernimmt, macht sie sich zu eigen (OLG Karlsruhe 19 U 100/09).
   - Wer als Unternehmer Planung übernimmt, kann sich nicht auf fehlende Fachkenntnis berufen (OLG Köln 19 U 23/20, NZB zurückgewiesen, BGH VII ZR 289/21).
   - Ein Mitverschulden des Bestellers wegen fehlerhafter Vorgaben entlastet nur, wenn er die Planung einem Dritten übertragen hat. Im Zielbild stellt die Firma selbst den Regelraum. Dieser Einwand trägt deshalb kaum.
   - Aus demselben Grund greift auch die Ausnahme von der Baubeschreibungspflicht nicht. Die Begründung nennt als Beispiel den vom Verbraucher beauftragten Architekten (BT-Drs. 18/8486 zu § 650i BGB-E).
   - Die Firma haftet schon vor Vertragsschluss für die Planung durch den Vertrieb, einschließlich 3D-Darstellung und Grundstückseinbindung (OLG Nürnberg 2 U 1369/10, Fertighaus).
2. **„Unter der Leitung“ (Art. 61 Abs. 6 BayBO) verlangt eine nachweisbare Einflussmöglichkeit, nicht nur eine Unterschrift. Automation Bias hat bereits einen haftungsrechtlichen Maßstab.**
   - Kammern werten es als Berufspflichtverstoß, einen fertig vorgelegten Entwurf ohne rechtlich abgesicherte Weisungs-, Organisations- und Überwachungsbefugnis zu unterzeichnen, selbst wenn er vorher geprüft wurde (IK-Bau NRW 2024; Byak-Berufsordnung Nr. 5.1).
   - Für die Software gilt: Wer ein übliches Rechenprogramm verwendet, handelt sorgfaltsgemäß. Sobald Warnsignale vorliegen, braucht es eine Plausibilitäts- oder Gegenrechnung (OLG Köln 16 U 98/16).
   - Das Genehmigungsfreistellungsverfahren und das vereinfachte Verfahren verstärken die Verantwortung der Beteiligten bewusst (BGH VII ZR 391/99; Begründung BayBO 2008, Drs. 15/7161). Für Wohngebäude der GK 1/2 gibt es bei der Standsicherheit kein Vier-Augen-Prinzip.
3. **Automatische Prüfberichte sind Parteidokumentation, kein Verwaltungsakt und keine Urkunde mit besonderer Beweiskraft. Ihr Wert entsteht durch die Beweisarchitektur.**
   - Vor Gericht ist ein privater Prüfbericht qualifizierter Parteivortrag in freier Beweiswürdigung (BGH VI ZR 243/92; OLG Nürnberg 8 U 1139/21).
   - Besondere Beweiskraft hat nur ein privates Dokument mit qualifizierter elektronischer Signatur (QES) einer natürlichen Person (§ 371a Abs. 1 ZPO).
   - Das qualifizierte Siegel der Firma begründet die unionsrechtliche Vermutung von Integrität und Herkunft (Art. 35 Abs. 2 eIDAS). Qualifizierte Zeitstempel, Archive und Ledger haben eigene Vermutungen (Art. 41, 45i, 45k eIDAS).
   - Die Kommission hat „logging by design“ vorgeschlagen. Fehlen die Aufzeichnungen, kehrt sich danach die Beweislast um (Expert Group 2019, Key Finding [22]). Die Produkthaftungsrichtlinie sieht die Offenlegung von Beweismitteln vor.
   - Bayern will für Bauvorlagen weder Unterschrift noch QES verlangen (Entwurf 2026, Begründung zu Art. 51 und 64). Der Nachweis der Person läuft dort über das Nutzerkonto und den Namen im Plankopf.
4. **Die Typengenehmigung passt zum Regelraum. Sie ist aber ein Nachweis- und kein Verfahrensersatz, und die Praxis ist dünn.**
   - Art. 73a BayBO wurde 2020 ausdrücklich für Baukastensysteme eingeführt. Die „Reichweite der Veränderbarkeit“ muss sich „zweifelsfrei“ aus der Genehmigung ergeben (Drs. 18/8547).
   - Seit 2024 gilt sie unbefristet, und Ortsgestaltungssatzungen gelten für typengenehmigte Gebäude nicht mehr. Bebauungsplan, Abstandsflächen und das Verfahren bleiben (Drs. 19/3023).
   - Die erste bayerische Typengenehmigung für ein Wohngebäude wurde im Oktober 2025 erteilt (StMB 106/2025). Verbände halten den Nutzen derzeit für gering (HDB/GdW 2023; ZIA 2023).
5. **Es haftet vor allem die Firma aus Werkvertrag. Produkthaftung und KI-VO ergänzen das nur.**
   - Der Fertighausvertrag ist ein Werkvertrag (BGHZ 87, 112). Die Firma schuldet eine dauerhaft genehmigungsfähige Planung, eine Risikoübernahme durch den Kunden setzt Aufklärung voraus (BGH VII ZR 8/10).
   - Die EU-Richtlinie zur KI-Haftung ist zurückgezogen (ABl. C/2025/5423). Außerhalb der Produkthaftung gibt es damit keine KI-spezifische Beweiserleichterung.
   - Die Leitlinien der Kommission nehmen Systeme mit rein menschlich definierten Regeln aus der Definition des KI-Systems aus, logik- und wissensbasierte Inferenz aber nicht. Die Regelmaschine ist deshalb nur „voraussichtlich“ kein KI-System, das Intent-Modell ist eines.
   - Hochrisiko liegt nicht vor: Weder Anhang III noch Anhang I (ohne Bauprodukteverordnung) erfassen die Anwendung. Es bleiben Art. 50 und der durch die Omnibus-Verordnung 2026/1744 abgeschwächte Art. 4.
   - Datenschutz: Die DSK verlangt „keine automatisierte Letztentscheidung“. Eine automatische Ablehnung, von der der Vertrag maßgeblich abhängt, kann nach EuGH C-634/21 eine Entscheidung im Sinne von Art. 22 DSGVO sein. Das spricht für ein menschliches Gate bei jeder Ablehnung.

---

## 1 Verantwortung und Haftung: Laie entwirft, berechtigte Person gibt frei

### 1a Übernahme fremder Planung, Prüf- und Hinweispflicht

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| BGH, Urteil 15.01.2026 | N | VII ZR 119/24, ECLI:DE:BGH:2026:150126UVIIZR119.24.0 | Die Übergabe einer mangelhaften fremden Entwurfsplanung entbindet den Ausführungsplaner nicht. Er muss die Ergebnisse der vorangehenden Leistungsphasen im Rahmen der Zumutbarkeit prüfen, notfalls nachfragen und dem **Besteller** (nicht nur einem anderen Beteiligten) klar Bedenken mitteilen. Das Mitverschulden des Bestellers wird ihm über § 254 Abs. 2 S. 2, § 278 BGB zugerechnet, wenn er die Pläne durch einen Dritten erstellen ließ. Im Fall lag es bei insgesamt 80 %. | **3** – genauester Maßstab für die Freigabe eines Kundenentwurfs: eigene Prüfung, Bedenkenhinweis an den Kunden. Der Zurechnungsweg setzt einen vom Besteller beauftragten Planer voraus. Den gibt es im Zielbild nicht, weil die Firma selbst den Regelraum stellt. | [V] BGH-PDF |
| BGH, Urteil 10.02.2011 | N | VII ZR 8/10, BauR 2011, 869 = NZBau 2011, 360 | Geschuldet ist eine dauerhaft genehmigungsfähige Planung. Eine Risikoübernahme durch den Auftraggeber setzt voraus, dass er Bedeutung und Tragweite erkannt hat, in der Regel also eine umfassende Aufklärung. Hätte ein Laie das Risiko erkennen können, trägt er ein Mitverschulden (§ 254 BGB). | **3** – begründet ein eigenes „Abweichungs-Gate“: Wünscht der Kunde etwas außerhalb des Regelraums, muss die Aufklärung dokumentiert werden, bevor er das Risiko trägt. Ergänzt `bgh2002genehmigungsplanung`. | [V] dejure, NWB (Rn. 22, 27, 46 f.) |
| BGH, Urteil 08.11.2007 | N | VII ZR 183/05, BGHZ 174, 110 | Geschuldet ist die Funktionstauglichkeit. Wer auf fehlerhafte Vorleistungen aufbaut, wird nur frei, wenn er seine Prüf- und Hinweispflicht erfüllt hat. | **2** – Grundsatz hinter VII ZR 119/24; überträgt die Pflicht auf den Fall „Werk baut auf Planung auf“. | [V] dejure |
| BGH, Urteil 27.11.2008 | N | VII ZR 206/06, BGHZ 179, 55 | Glasfassade: Der Bauherr muss dem Bauüberwacher mangelfreie Pläne übergeben. Außerdem geht es um Organisationsverschulden bei arbeitsteiliger Überwachung. | **2** – Pflicht einer arbeitsteiligen Firma, Prüfungen zu organisieren. Das spricht dafür, Gates als Organisationspflicht zu verstehen. | [V] dejure |
| BGH, Urteil 15.05.2013 | N | VII ZR 257/11, BGHZ 197, 252 | Der Tragwerksplaner muss sich die nötigen Kenntnisse selbst verschaffen, etwa zu Baugrund und Grundwasser. Ob er auf übermittelte Angaben vertrauen darf, betrifft nur das Verschulden. Bei falschen Angaben des Auftraggebers haftet dieser mit. | **2** – Grundstücksdaten vom Kunden (Höhen, Baugrund) sind „Angaben des Auftraggebers“. Ihre Herkunft muss im Nachweis stehen (Herkunftsfeld). | [V] dejure, nu:legal |
| OLG Karlsruhe, Urteil 09.03.2010 | N | 19 U 100/09, IBR 2010, 281 | Der umfassend beauftragte Zweitarchitekt macht sich übernommene Pläne „planerisch zu eigen“ und haftet voll. | **2** – Leitbild für „Übernahme“ des Kundenentwurfs durch die Firma. | [V] dejure; Leitsatz über AKNW-Besprechung |
| OLG Köln, Beschluss 09.03.2021; BGH, Beschluss 10.05.2023 | N | 19 U 23/20; VII ZR 289/21 (NZB zurückgewiesen); IBR 2023, 618 | „Wer planen will, muss auch planen können“: Wer als Bauunternehmer Planung übernimmt, schuldet sie mangelfrei. Er kann sich nicht auf fehlende Fachkenntnis berufen, muss notfalls Sonderfachleute einsetzen und mindestens die einschlägigen DIN kennen. | **3** – unmittelbar auf die Fertighausfirma als Entwurfsverfasserin übertragbar. Ersetzt die Kurzangabe in Recherche 07. | [V] dejure (Verfahrensgang); Leitsätze über Besprechung |
| OLG Nürnberg, Urteil 17.06.2011 | N | 2 U 1369/10, IBR 2013, 16 | Fertighaushersteller: Eine Vertriebsmitarbeiterin plant auf Angaben der Kunden (Hang „ca. 3 m“) und zeigt eine 3D-Animation. Die Eingabeplanung stammt von einer externen Architektin, die als Entwurfsverfasserin zeichnet. Der Hersteller haftet wegen Verletzung vorvertraglicher Aufklärungs- und Beratungspflichten. | **3** – bayerischer Präzedenzfall genau zur Konstellation „Kunde und Vertrieb entwerfen, eine Berechtigte zeichnet“: Die 3D-Darstellung begründet Vertrauen, die Geländeeinbindung gehört zur Beratungspflicht. | [V] dejure; Volltext Kanzleiabdruck |
| BGH, Urteil 27.09.2001 | N | VII ZR 391/99, BauR 2002, 114 | Aus dem eingeschränkten Prüfprogramm eines vereinfachten Verfahrens folgt keine eingeschränkte Planungspflicht. Das Verfahren bedeutet einen Abbau staatlicher Aufsicht bei **bewusster Verstärkung der Verantwortlichkeit** der Beteiligten. | **3** – In Bayern ist die Genehmigungsfreistellung (Art. 58) der Regelfall für das Einfamilienhaus. Das System muss deshalb auch das prüfen, was keine Behörde prüft. | [V] dejure; Leitsätze über BauNetz |
| BGH, Beschluss 19.07.2023 (zu KG 27 U 82/22) | N | VII ZR 216/22, IBR 2024, 134 | Verlangt der Bauherr eine Abweichung vom Bebauungsplan in der Erwartung einer Befreiung, kann er das Genehmigungsrisiko übernehmen. Dann ist die Planung nicht mangelhaft. | **2** – Gegenstück zu VII ZR 8/10 für bewusste Kundenwünsche außerhalb der Regeln. | [V] Verfahrensgang dejure; [U] Inhalt nur über BauNetz |
| BVerfG, Beschluss 27.05.1970 | N | 2 BvR 117/65, BVerfGE 28, 364 | Die Bauvorlageberechtigung ist verfassungsgemäß. Der Gesetzgeber darf verlangen, dass Vorlagen von Fachleuten angefertigt **und verantwortet** werden, weil die Bauaufsicht nicht jeden Antrag bis ins Detail prüfen kann. | **2** – Normzweck: Die Berechtigung sichert Sachkunde im Entstehungsprozess, nicht nur die Unterschrift. Das stützt die Auslegung von „unter der Leitung“ als Einfluss. | [V] BVerfG-Verzeichnis, dejure-Auszüge |
| BayVerfGH, 14.04.1999 | N | Vf. 4-VII-97, BayVBl. 1999, 493 | Die „kleine“ Bauvorlageberechtigung für Meister und Techniker ist nicht willkürlich. | **1** – Rechtfertigung der Zimmerermeister-Stufe in Art. 61 Abs. 3. | [U] nur sekundär (Begründung eines Berliner Gesetzentwurfs) |
| BT-Drs. 18/8486 (Reform Bauvertragsrecht) | N | Drs. 18/8486 vom 18.05.2016, Begr. zu § 650i und § 650m BGB-E | Die Baubeschreibungspflicht entfällt, „wenn der Besteller oder ein von ihm Beauftragter, beispielsweise ein Architekt, die wesentlichen Planungsvorgaben macht“. Die Herausgabepflicht für Unterlagen zielt auf den Schlüsselfertigbau, in dem die Planung nicht vom Besteller stammt. | **3** – klärt den in 07 offenen Punkt: Ein Laienentwurf im Regelraum der Firma ist kein Fall der Ausnahme. Baubeschreibung und Unterlagenpflicht bleiben (heute §§ 650j, 650n BGB). | [V] dserver |
| BT-Drs. 18/11437 | N | Beschlussempfehlung Rechtsausschuss, 08.03.2017 | Endfassung mit neuer Nummerierung. | **1** – Zitierhilfe zur Normfolge. | [V] dserver |
| Bay. Landtag Drs. 15/7161 (BayBO 2008) | N | 15.01.2007, Begr. zu Art. 57 und 68a a. F. | Entwurfsverfasser ist, wer die Bauvorlagen fertigt **und/oder verantwortlich zeichnet**; nacheinander können mehrere mitwirken. Die BayBO kompensiert entfallende Prüfungen dreistufig: allgemeine Bauvorlageberechtigung, besondere Qualifikation, Vier-Augen-Prinzip nur bei Risiko. | **3** – amtliche Grundlage dafür, dass die freigebende Person Entwurfsverfasserin im Rechtssinn ist, auch wenn sie nicht zeichnet. Außerdem Begründung für gestufte Gates. | [V] Landtag-Volltext |
| OLG München, Beschluss 29.07.2021 | N | 9 U 3342/20 Bau | Planungsleistungen im Generalunternehmer-Vertrag werden nicht nach HOAI abgerechnet. | **1** – präzisiert Recherche 07 (dort: „Paketanbieter“). Betrifft das Honorar, nicht die Haftung. | [V] gesetze-bayern.de |
| BGH, Urteile 10.03.1983; 22.12.2005; 27.04.2006 | N | VII ZR 302/82 (BGHZ 87, 112); VII ZR 183/04; VII ZR 175/05 | Fertig- und Ausbauhausvertrag mit Errichtung ist ein Werkvertrag. Eine Kündigungspauschale von 10 % ist in AGB wirksam. | **1** – ordnet den Vertragstyp ein. Die Pauschale ist für FF4 nur am Rand relevant, eher für das Vertrags-Gate. | [V] dejure, Doctrine |
| LG Kiel, Urteil 29.02.2024 | N | 6 O 151/23, GRUR-RS 2024, 29599 | Der Betreiber haftet für KI-generierte Falschinformationen, die er sich erkennbar zu eigen macht. | **1** – Zurechnung von KI-Ausgaben an den Verwender. Kein Baurecht. | [V] dejure, WD 7-004/25 |
| IK-Bau NRW: Unterzeichnung fremder Entwürfe | G | Kammermeldung 23.02.2024 | Unterzeichnen darf nur, wer die Planung selbst oder „unter seiner Leitung“ erstellt hat. Leitung heißt tatsächliche **und rechtlich abgesicherte** Einflussmöglichkeit, etwa ein Weisungsrecht gegenüber Angestellten. Die bloße Vorlage eines fertigen Entwurfs genügt auch nach eigener Prüfung nicht. Bestätigt vom Berufsgericht beim VG Düsseldorf. | **3** – schärfster verfügbarer Maßstab für Art. 61 Abs. 6. Die benannte Person muss den Regelraum mitgestalten, freigeben und Abweichungen entscheiden. Ein reiner Stempel am Ende reicht nicht. Für Bayern nur analog anwendbar (NRW-Kammerrecht). | [V] Kammerseite; [U] Az. des Berufsgerichts nicht genannt |
| AKNW: Angestellter Entwurfsverfasser | G | Rechtstipp 25.03.2019 | In NRW ist die unterzeichnende Person höchstpersönlich verantwortlich, nicht das Büro. Wer unterzeichnen darf, soll intern schriftlich geregelt werden. Die zivile Haftung trägt der Arbeitgeber, das Bußgeldrisiko trifft die Person. | **2** – Gegenmodell zur bayerischen Unternehmenslösung (Art. 61 Abs. 6). Stützt eine schriftliche Freigabeordnung. | [V] Kammerseite |
| Byak: Berufsordnung 2020 | N | Neubekanntmachung 27.11.2020 | Nr. 4.4: Berufshaftpflicht mindestens 1,5 Mio. € Personen- und 200.000 € sonstige Schäden. Nr. 5.1: Urheberschaft nur für Leistungen unter eigener oder persönlicher Leitung. Nr. 7.2: Die Tätigkeitsform ist offenzulegen, wenn geschäftliche Interessen die Entscheidungsfreiheit einschränken können. | **2** – In Bayern gilt die persönliche Leitung auch berufsrechtlich. Arbeitet ein angestellter Architekt in einer Fertighausfirma, muss die gewerbliche Einbindung offengelegt werden. | [V] Kammer-PDF |
| Byak: Merkblatt 7 Bauvorlageberechtigung | G | Stand 01/2019 | Erläutert Art. 61, 62, 62a, 62b BayBO und die Listen. | **1** – Hintergrund; veraltet gegenüber `baybo2026`. | [V]; [U] Stand 2019 |
| Byak: Merkblatt 13 Prüfung Werkstatt- und Montageplanung | G | Stand 11/2021 | Geprüft wird auf offenkundige und mit zu erwartender Fachkenntnis feststellbare Fehler. Der Prüfvermerk kann ein Eintrag im digitalen Workflow sein, mit Prüfer und Datum. Ein Mustervermerk ist enthalten. | **2** – Vorlage für die Semantik eines `IfcApproval`: Prüfumfang, Prüfer, Datum, Vorbehalt. | [V] Kammer-PDF |
| BAK: KI-FAQ Nr. 8 | G | 25.04.2024 | Es gelten die allgemeinen Haftungsregeln. Wegen der Black Box droht die Alleinhaftung der Architektin. Die neue Produkthaftungsrichtlinie soll den Rückgriff auf den Hersteller erleichtern. | **2** – Sicht der Berufsvertretung; ergänzt `bayika2026ki`. | [V] BAK-Seite |
| AKNW: KI und Berufsbild | G | Positionspapier 03.12.2025 (Vorfassung 04.10.2024) | Architekten müssen „Systemführer“ bleiben, KI-Ergebnisse kritisch prüfen und Haftung vertraglich regeln. | **2** – Rollenbild für die freigebende Person. | [V] Kammer-PDF |
| WD 7 – 3000 – 004/25 | G | Sachstand, Abschluss 04.03.2025 | „Verantwortlich für KI-generierte Inhalte ist im Zweifel der Anwender, der … sich die Ergebnisse einer KI zu eigen macht.“ Überblick über Produkt- und Produzentenhaftung. | **2** – amtlicher Überblick ohne Baurechtsbezug. | [V] Volltext |

### 1b Automation Bias und wirksame menschliche Aufsicht (rechtlicher Maßstab)

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| OLG Köln, Urteil 31.05.2017 | N | 16 U 98/16, IBR 2017, 564 | Wer ein übliches Statikprogramm mit richtigen Eingaben nutzt, handelt zunächst sorgfaltsgemäß; eine Doppelrechnung ist nicht geschuldet. Bei Warnsignalen (hier sechs Schreiben des Prüfstatikers) darf er dem Programm nicht mehr vertrauen, sondern muss plausibilisieren oder gegenrechnen. Das Unterlassen war fahrlässig. | **3** – der deutsche Rechtsmaßstab für Automation Bias: Vertrauen ist erlaubt, bis ein Warnsignal kommt. Das Gate muss Warnsignale (Grenzwertnähe, gelbe Ergebnisse, Widersprüche) sichtbar machen und die Reaktion dokumentieren. | [V] NRWE-Volltext |
| OLG Oldenburg, Urteil 17.01.2017 | N | 2 U 68/16, IBR 2017, 509 | Der Ingenieur haftet für Fehler des beigezogenen Tragwerksplaners, wenn sie für ihn mit dem zu erwartenden Fachwissen erkennbar waren. Eine „mindestens gebotene oberflächliche Durchsicht“ ist geschuldet. | **2** – Prüfpflicht der freigebenden Person gegenüber Fachbeiträgen (Statik, Energie). | [V] dejure, voris |
| Green: Flaws of human oversight policies | W | CLSR 45 (2022) 105681 | Menschliche Aufsicht über Algorithmen ist oft nur eine Scheinsicherung: Menschen erkennen Fehler schlecht, und die Aufsicht verschleiert die Verantwortung. Green empfiehlt, erst nachzuweisen, dass die Aufsicht wirksam ist. | **3** – Gegenargument zum reinen Klick-Gate. Die Arbeit muss die Wirksamkeit der Freigabe messen (M9 in Recherche 23). | [V] Crossref, CC BY |
| Laux: Institutionalised distrust | W | AI & Society 39 (2024), 2853–2866 | Menschliche Aufsicht nach der KI-VO sollte als institutionalisiertes Misstrauen gestaltet werden, mit Rechenschaft, Befugnis und Kompetenz der Aufsichtspersonen. | **2** – Leitbild für die Rolle „Prüfer“ statt „Unterzeichner“. | [V] Crossref |
| Enqvist: Human oversight in the AI Act | W | Law, Innovation and Technology 15 (2023), 508–535 | Rechtsdogmatisch: Was bedeutet Aufsicht, wann und durch wen (Anbieter oder Betreiber)? | **2** – ordnet Art. 14 KI-VO ein. Gilt nur für Hochrisiko-Systeme, taugt aber als Vorbild. | [V] Crossref |
| Sterz et al.: Effectiveness in human oversight | W | FAccT 2024, 2495–2507 | Wirksam ist Aufsicht nur, wenn vier Bedingungen erfüllt sind: kausaler Einfluss, epistemischer Zugang, Selbstkontrolle und passende Absichten. | **3** – prüfbare Kriterien für jedes Gate: Die Person kann eingreifen, sieht Begründung und Daten, hat Zeit und ist befugt. | [V] Crossref |
| Alon-Barkat & Busuioc: Automation bias and selective adherence | W | JPART 33 (2023), 153–169 | Drei Experimente (N = 605, 904 und ein drittes) in der niederländischen Verwaltung. Kein Nachweis von Automation Bias gegenüber menschlichen Experten, wohl aber „selektive Befolgung“, wenn der Rat Stereotypen bestätigt. | **2** – relativiert die Annahme, dass Automation Bias stets auftritt. Die Evaluation sollte beide Effekte messen. | [V] Crossref mit Abstract |
| KI-VO Art. 14 Abs. 4 Buchst. b (`aiact2024`) | N | VO (EU) 2024/1689 | Aufsichtspersonen müssen sich der Neigung zum übermäßigen Vertrauen auf die Ausgabe bewusst bleiben („automation bias“). | **2** – der Begriff ist jetzt normiert, gilt aber nur für Hochrisiko-Systeme. Hier ist er Gestaltungsmaßstab, keine Pflicht. | [V] EUR-Lex (vorhanden) |

---

## 2 Rechtscharakter automatischer Prüfberichte, Beweiswert, elektronische Signatur

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| § 371a ZPO | N | gesetze-im-internet.de | Private elektronische Dokumente mit **QES** gelten beweisrechtlich wie Privaturkunden (Anscheinsbeweis der Echtheit). Öffentliche Dokumente können auch ein qualifiziertes Siegel tragen. | **3** – Der Prüfbericht der Firma bekommt besondere Beweiskraft nur mit der QES der freigebenden Person, nicht mit einem Firmensiegel. | [V] |
| eIDAS Art. 25, 35, 41, 45i, 45k (`eu2014eidas`) | N | konsolidierte Fassung 18.10.2024 | QES ist der Handschrift gleichgestellt (Art. 25). Qualifiziertes Siegel: Vermutung von Integrität und Herkunft (Art. 35 Abs. 2). Qualifizierter Zeitstempel: Vermutung von Datum und Integrität (Art. 41). Qualifiziertes Archiv: Vermutung von Integrität und Herkunft (Art. 45i). Qualifiziertes Ledger: Vermutung der Reihenfolge und Integrität (Art. 45k). | **3** – Baukasten für die Nachweiskette: Siegel der Firma auf jedem Prüfbericht, QES der Person auf dem Gate, qualifizierter Zeitstempel auf dem Hash. Ein Ledger wäre die unionsrechtliche Alternative zur Blockchain (vgl. Hunhevicz & Hall in 23). | [V] EUR-Lex (vorhanden, Artikel neu geprüft) |
| Vertrauensdienstegesetz (VDG), § 15 | N | BGBl. I 2017 S. 2745 | Regelt die langfristige Beweiserhaltung qualifiziert signierter Daten durch Erneuerung von Signaturen, Siegeln und Zeitstempeln. | **2** – Der Nachweis muss über 30 Jahre Hausakte prüfbar bleiben. | [V]; [U] BGBl.-Seite |
| BT-Drs. 18/12494 (eIDAS-Durchführungsgesetz) | N | 24.05.2017 | Gesetzesmaterialien zum VDG. | **1** – Hintergrund. | [V] |
| BSI TR-03125 (TR-ESOR) V1.3 | G | 31.03.2022 | Ohne Erneuerung entfällt nur die besondere Beweiskraft nach § 371a ZPO, nicht jeder Beweiswert (§ 286 ZPO). Evidence Records (RFC 4998) über Hashbäume. Seit V1.2.2 auch auf DLT anwendbar. | **3** – technische Norm für „Nachweis mit Hash“: Hashbaum und Evidence Record statt eigener Kette. | [V] Hauptdokument |
| BGH, Urteil 11.05.1993 | N | VI ZR 243/92, NJW 1993, 2382 | Ein Privatgutachten ist kein Beweismittel nach §§ 355 ff. ZPO, sondern qualifizierter Parteivortrag. Als Sachverständigengutachten gilt es nur, wenn beide Parteien zustimmen. | **2** – Rechtscharakter des automatischen Prüfberichts im Streit mit dem Kunden. | [V] dejure |
| OLG Nürnberg, Endurteil 19.08.2021 | N | 8 U 1139/21 | Privatgutachten sind qualifizierter, urkundlich belegter Parteivortrag (§ 416 ZPO). Bei Bestreiten ist ein gerichtliches Gutachten einzuholen. | **2** – bayerische Bestätigung. Nachvollziehbarkeit ohne Code (Prinzip 9) ist die Voraussetzung dafür, dass ein Gerichtsgutachter den Bericht prüfen kann. | [V] gesetze-bayern.de |
| § 35a VwVfG | N | gesetze-im-internet.de | Ein vollautomatischer Verwaltungsakt braucht eine Rechtsvorschrift und darf weder Ermessen noch Beurteilungsspielraum enthalten. | **2** – Abgrenzung: Der Prüfbericht der Firma ist kein Verwaltungsakt. Eine behördliche Prüfung per ACC bräuchte eine eigene Rechtsgrundlage. | [V]; [U] Art. 35a BayVwVfG nicht separat |
| Gesetzentwurf Digitalisierung bauaufsichtlicher Verfahren (`bayDigitalisierungEntwurf2026`) | N | Ministerrat 21.07.2026, Begr. zu Art. 51, 56, 64 | „Digital only“. Die Unterschriften von Entwurfsverfasser und Fachplanern entfallen. Es genügt, dass Bauvorlagen die Person erkennen lassen (Name im Beschriftungsfeld); die Authentifizierung läuft über Nutzerkonten. Ausdrücklich „ohne Schriftformersatz wie etwa eine qualifizierte elektronische Signatur“. | **3** – schließt Lücke 8 aus Recherche 23: Behördlich ist keine QES nötig. Die QES bleibt eine Frage der zivilrechtlichen Beweisvorsorge. | [V] (vorhanden; Begründung jetzt gelesen) |
| DBauV § 11 Abs. 4 (`dbauv2026`) | N | Fassung 15.05.2026 | Standsicherheits- und Brandschutznachweis werden als elektronisches Abbild des **unterschriebenen Originals** eingereicht. Das Original kann nachgefordert werden. | **2** – Solange die DBauV gilt, braucht das Statik-Gate ein unterschriebenes Original. | [V] (vorhanden) |
| Bay. Landtag Drs. 19/9992 „Digital Only“ | N | Antrag 12.02.2026, Beschluss 15.04.2026 | Parlamentarischer Auftrag für das digitale Regelverfahren. | **1** – Einordnung des Entwurfs. | [V] |
| TAB-Bericht BT-Drs. 20/3651 | G | 26.09.2022 | KI und DLT in der öffentlichen Verwaltung, internationale Beispiele (u. a. Grundbuch in Schweden). | **1** – Kontext zur Frage „Ledger oder vertrauenswürdige Instanz“. | [V] |

---

## 3 Typengenehmigung Art. 73a BayBO und serielle Planung

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Bay. Landtag Drs. 18/8547 | N | 23.06.2020, Begr. zu Nr. 29 (Art. 73a); GVBl. 2020 S. 663 | Eingeführt „auf Wunsch der Wohnungswirtschaft“, um serielles Bauen zu erleichtern. Gilt auch für ein „Baukastensystem oder andere Varianten serieller Bauweise“. „Die jeweilige Reichweite der Veränderbarkeit eines Systems muss sich aus der Genehmigung allerdings zweifelsfrei ergeben.“ Die Genehmigung wirkt als bautechnischer Nachweis. | **3** – genau die Brücke zum Regelraum: Der maschinenlesbare Regelraum könnte die „zweifelsfreie“ Beschreibung der Veränderbarkeit sein. | [V] Volltext |
| Bay. Landtag Drs. 19/3023 (Erstes Modernisierungsgesetz) | N | 31.07.2024, § 12 Nr. 13 | Die Pflicht zur Befristung entfällt (Nebenbestimmung nach Art. 36 BayVwVfG möglich). Neu Abs. 6: Ortsgestaltungssatzungen gelten für typengenehmigte Gebäude nicht, Festsetzungen im Bebauungsplan weiterhin. | **3** – bestimmt, was das System trotz Typengenehmigung prüfen muss: Bebauungsplan, Abstandsflächen, Verfahren. | [V] Volltext |
| StMB: Erste Typengenehmigung für Wohngebäude | G | Pressemitteilung 106/2025 (10/2025) | Erste Erteilung an B&O Bau: Holzmassivwände, mit oder ohne Keller und Balkone, 4 bis 8 Obergeschosse. Im Einzelverfahren bleiben die ortsabhängigen Aspekte zu prüfen. | **2** – belegt, dass Varianten genehmigungsfähig sind. Einfamilienhaus-Serien sind noch nicht belegt. | [V]; [U] Tagesdatum |
| MBO, zuletzt geändert 26./27.09.2024 | N | Bauministerkonferenz; § 72a seit 22.02.2019 | Mustervorschrift zur Typengenehmigung (Typen- und Systembauten), gilt länderübergreifend. | **1** – nicht verbindlich. Das bayerische Recht geht vor. | [V] Fassungsangabe; [U] Wortlaut § 72a nicht geprüft |
| ZIA: Serielles/modulares Bauen | G | Kurzgutachten 02/2023 | Fordert, § 72a MBO zu stärken, und nennt Bayern als Vorbild für einen gebundenen Anspruch. Außerdem Anerkennung ohne Vergleichbarkeitsvorbehalt, Genehmigungsfreistellung oder -fiktion für serielle Vorhaben und die referentielle Baugenehmigung nach NRW-Vorbild. | **2** – rechtspolitische Optionen, Interessenverband. | [V]; [U] Verfasser |
| HDB/GdW: Spannungsfeld Typengenehmigung | G | Positionspapier 26.05.2023 | Praxisurteil: „Typengenehmigung bringen im Moment keinen Vorteil“, weil das Verfahren vor Ort bleibt. Schlanke Bebauungspläne und die Genehmigungsfreistellung seien wichtiger. | **2** – dämpft die Erwartung. Stützt die Entscheidung, die Typengenehmigung als Option und nicht als Kern zu führen. | [V] |
| Art. 62a Abs. 2 S. 3 Nr. 2 BayBO (`baybo2026`) | N | Fassung 01.05.2026 | Die Typenprüfung der Standsicherheit durch ein Prüfamt ersetzt Bescheinigung und Prüfung. Ein Zimmerermeister darf den Standsicherheitsnachweis nur mit Zusatzqualifikation und drei Jahren Berufserfahrung erstellen (Abs. 1 Nr. 2 a). | **2** – Die Typenprüfung ist die leichtere Alternative für Wandelemente. Das Statik-Gate muss prüfen, ob der Zimmerermeister die Zusatzqualifikation hat. | [V] gesetze-bayern (vorhanden) |

---

## 4 Produkthaftung und Werkmangel bei Planungssoftware

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Expert Group „Liability for AI and other emerging digital technologies“ | G | Europäische Kommission 2019, DOI 10.2838/573689 | Gefährdungshaftung des Betreibers, der das Risiko kontrolliert (Front- und Backend-Operator, [9]–[12]). „Logging by design“ als Herstellerpflicht ([20]). Fehlen die Aufzeichnungen, soll die Beweislast umgekehrt werden ([22]). Keine eigene Rechtspersönlichkeit ([8]). | **3** – rechtspolitische Begründung für Nachweise mit Hash und Regelwerk-Version. Sie sind Beweisvorsorge und kein Selbstzweck. | [V] Volltext |
| Bertolini & Episcopo: Kritik des Expertenberichts | W | EJRR 12 (2021), 644–659 | Kritisiert den Vorrang von Beweisregeln vor materiellen Regeln und die unklare Abgrenzung von hohem und niedrigem Risiko. | **1** – Gegenstimme. | [V] Crossref |
| ELI: Guiding Principles PLD | G | Twigg-Flesner, ELI Innovation Paper 01/2021 | Zehn Grundsätze: Software als Produkt, dynamischer Fehlerbegriff bei Updates, Beweislast. | **1** – Vorgeschichte der Richtlinie 2024/2853. | [V] |
| KI-Haftungsrichtlinie (Entwurf) | N | COM(2022) 496, 28.09.2022 | Vermutung der Kausalität und Offenlegung bei Hochrisiko-KI. | **1** – nur als Vorgeschichte. | [V] |
| Rücknahme der KI-Haftungsrichtlinie | N | ABl. C/2025/5423, 06.10.2025 | Am 16.07.2025 zurückgezogen. | **2** – Folge: Für reine Vermögensschäden aus Planungsfehlern bleibt es beim Werkvertragsrecht (vgl. `bayika2026ki`). | [V] |
| Hacker: EPRS Complementary Impact Assessment | G | PE 762.861, 09/2024, DOI 10.2861/1723734 | Empfiehlt, die Haftungsrichtlinie zu einer allgemeinen Verordnung über Softwarehaftung auszubauen. | **2** – zeigt die offene Lücke „Software ohne KI“, in die die Regelmaschine fällt. | [V] |
| Hacker: EU AI liability directives | W | CLSR 51 (2023) 105871 | Kritik: Das Konzept stützt sich auf Offenlegung und eng gefasste Vermutungen. Vorschlag: Gefährdungshaftung nur für bestimmte Hochrisiko-Systeme, sichere Häfen. | **2** – dogmatische Einordnung, Open Access. | [V] Crossref |
| Wendehorst: Stellungnahme ProdHaftG | G | Ausschussdrucksache 21(6)74d, 10.04.2026 | Zweifel an § 8 ProdHaftG-E: Die „Kontrolle des Herstellers“ ist ein Schwachpunkt. Klarstellung gefordert, dass „digitale Produkte“ im Sinne des § 327 BGB Software sind. Daten mit gemischter Nutzung nach dem überwiegenden Zweck. | **2** – Die Firma behält über Updates die Kontrolle über den Planer. Der Beurteilungszeitpunkt für einen Fehler verschiebt sich damit nach hinten. | [V] |
| ProdHaftG-E (`prodhaftg2026`) und RL 2024/2853 (`eu2024produkthaftungsrl`) | N | BT-Drs. 21/4297 | Neu: Auch **digitale Konstruktionsunterlagen** gelten als Produkt, ebenso Updates und verbundene Dienste. Ersatz nur für Personen-, Sach- (nicht beruflich) und Datenschäden. | **2** – BTLx- und WUP-Dateien für die Maschinen könnten „digitale Konstruktionsunterlagen“ sein; ob das zutrifft, ist ungeklärt. Stand 09/2026: in Ausschussberatung, Inkrafttreten geplant zum 09.12.2026. | [V] (vorhanden); [U] Stand des Gesetzgebungsverfahrens |
| BGH, Urteil 04.03.2010 | N | III ZR 79/09 | Der „Internet-System-Vertrag“ (Erstellung und Betrieb einer Website) ist ein Werkvertrag. | **1** – Werkvertrag bei individuell erstellten Softwareleistungen. | [V] dejure |
| BGH, Urteil 15.11.2006 | N | XII ZR 120/04 | Ein ASP-Vertrag ist ein Mietvertrag. Verkörperte Standardsoftware ist eine bewegliche Sache. | **1** – Mängelrechte der Firma gegenüber einem Anbieter von Software als Dienst. | [V] dejure |
| BGH, Urteil 04.11.1987 | N | VIII ZR 314/86 | Auf Standardsoftware ist Kaufrecht zumindest analog anwendbar. | **1** – Hintergrund. | [V] dejure |
| Zech: Risiken digitaler Systeme | W | Weizenbaum Series 2 (2020), DOI 10.34669/wi.ws/2 | Unterscheidet symbolische Repräsentation (logisches Schließen, klassische Programmierung) von impliziter (neuronale Netze). Das Autonomierisiko liegt in eingeschränkter Vorhersehbarkeit und Erklärbarkeit. | **2** – juristische Begründung für die Trennung „KI versteht, Code entscheidet“, ergänzt `wilhelmi2020haftung`. | [V] Volltext |
| Datenethikkommission: Gutachten | G | 23.10.2019 | Fünfstufige Kritikalitätspyramide, klare Rechenschaftsstrukturen. Kap. 8: Haftung für algorithmische Systeme. | **2** – Stufung der Gates nach Schadenspotenzial. | [V] |
| Enquete-Kommission KI: Bericht | G | BT-Drs. 19/23700 (28.10.2020) | Gesamtbericht, u. a. zu Haftung und Verantwortung. | **1** – Kontext. | [V]; [U] Haftungskapitel nicht im Einzelnen |

---

## 5 Pflichten nach der KI-VO für Anbieter und Betreiber im Bauwesen

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Leitlinien der Kommission zur Definition des KI-Systems | G | C(2025) 924, 06.02.2025, Rn. 40–49 | Nicht erfasst sind Systeme mit ausschließlich von Menschen definierten Regeln, „basic data processing“, klassische Heuristiken und einfache Vorhersage. Logik- und wissensbasierte Inferenz ist aber nach Erwägungsgrund 12 grundsätzlich ein KI-Verfahren. Die Leitlinien sind nicht verbindlich. | **3** – Die deterministische Regelmaschine (IDS, Geometrieprüfung) fällt voraussichtlich heraus, das Intent-Modell sicher hinein. Wird die Regelmaschine zu einem Inferenzsystem mit Regelschluss ausgebaut, kann sie hineinfallen. Die Architektur muss die Grenze dokumentieren. | [V] Leitlinien-PDF |
| KI-VO (`aiact2024`): Art. 6, Anhang I und III, Art. 50 | N | VO (EU) 2024/1689 | Anhang III enthält keinen Gebäudeentwurf. Anhang I Abschnitt A nennt die Bauprodukteverordnung nicht (sie erscheint nur in einer Fußnote zur Marktüberwachung). Art. 50 Abs. 1 verlangt den Hinweis, dass eine KI beteiligt ist. | **2** – bestätigt „kein Hochrisiko“ auch über den Produktweg. | [V] EUR-Lex (vorhanden, neu geprüft) |
| Digital Omnibus on AI | N | VO (EU) 2026/1744 vom 08.07.2026, ABl. L 24.07.2026 | Art. 4 neu: Anbieter und Betreiber müssen nur noch „Maßnahmen … unterstützen“; ein bestimmtes Niveau ist nicht garantiert. Art. 50 Abs. 2 (Kennzeichnung) gilt für Altsysteme ab 02.12.2026. Hochrisiko nach Anhang III ab 02.12.2027, nach Anhang I ab 02.08.2028. | **3** – ändert den Stand in Kap. 4.8.2 und Recherche 07: Die Pflicht zur KI-Kompetenz ist abgeschwächt, die Kennzeichnung erst ab Dezember 2026 zwingend. | [V] EUR-Lex |
| KI-MIG | N | BGBl. 2026 I Nr. 223, in Kraft 29.07.2026 | Die Bundesnetzagentur ist Marktüberwachungsbehörde. Sie berät zum Status als KI-System nur öffentliche Stellen (§ 12 Nr. 2). | **2** – Zuständigkeit bei Beschwerden. Private Firmen erhalten keine amtliche Einstufung und müssen selbst dokumentieren. | [V] |
| BT-Drs. 21/6407 (Beschlussempfehlung KI-Durchführungsgesetz) | N | Beschluss 11.06.2026 | Gesetzgebungsmaterial zum KI-MIG (Entwurf Drs. 21/4594, 21/5143). | **1** – Materialien. | [V]; [U] Datum der Beschlussempfehlung |

---

## 6 Datenschutz bei Sprachaufnahmen und automatisierter Ablehnung

| Quelle | Typ | Fundstelle | Kernaussage | Passung FF4 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| DSK: OH Künstliche Intelligenz und Datenschutz | G | 06.05.2024, V1.0 | Nr. 1.6: keine automatisierte Letztentscheidung. Nr. 2.3: Datenschutz-Folgenabschätzung. Nr. 2.5: datenschutzfreundliche Voreinstellungen (kein Training mit Eingaben, keine Eingabehistorie). Nr. 3.3: Ergebnisse auf Richtigkeit prüfen. | **3** – Aus Sicht der Aufsicht muss jede Ablehnung und jede Freigabe menschlich sein. Die Protokollierung der Sprachdaten ist zu minimieren. | [V] |
| DSK: OH TOM bei Entwicklung und Betrieb von KI-Systemen | G | Juni 2025, V1.0 | Maßnahmen je Lebensphase (Design, Entwicklung, Einführung, Betrieb) nach den Gewährleistungszielen des Standard-Datenschutzmodells (SDM). | **2** – Checkliste für den Betrieb des Intent-Modells (Laya lokal, Jev als Fallback). | [V] |
| EDPB: Guidelines 02/2021 on virtual voice assistants | G | V2.0, 07.07.2021 | Für den Zugriff auf das Endgerät ist die Einwilligung nach Art. 5 Abs. 3 ePrivacy-RL entbehrlich, wenn er für den angefragten Dienst unbedingt erforderlich ist. Die Speicherung ist zu begrenzen, versehentliche Aufnahmen sind zu löschen. Stimmdaten sind nur bei Verarbeitung zur Identifizierung biometrisch (Abschn. 3.8.2). Lokale Verarbeitung (Edge) erfordert eine neue Bewertung. | **3** – direkt anwendbar auf die Spracheingabe: ohne Sprechererkennung keine Daten nach Art. 9 DSGVO. Keine Aufnahmen für Training ohne Einwilligung. | [V] Volltext |
| § 25 TDDDG | N | gesetze-im-internet.de | Deutsche Umsetzung von Art. 5 Abs. 3 ePrivacy-RL (Mikrofonzugriff über App und Browser). | **2** – Rechtsgrundlage der Einwilligung in der App. | [V] |
| § 201 StGB | N | gesetze-im-internet.de | Strafbar ist die unbefugte Aufnahme des nichtöffentlich gesprochenen Wortes. | **2** – Beratungsgespräche mit dem Vertrieb dürfen nur mit Einwilligung aller Beteiligten aufgezeichnet werden. Stützt die [U]-Angabe in Recherche 07, die damit an der Norm geprüft ist. | [V] |
| EuGH, Urteil 07.12.2023, SCHUFA (Scoring) | N | C-634/21 | Eine automatisierte Bewertung ist schon dann eine „Entscheidung“ im Sinne von Art. 22 DSGVO, wenn der Vertragsschluss eines Dritten maßgeblich von ihr abhängt. Rn. 66: Verantwortliche müssen Fehlerrisiken minimieren und das Eingreifen einer Person ermöglichen. | **2** – Lehnt die App einen Entwurf automatisch ab und hängt der Vertrag davon ab, kann Art. 22 DSGVO greifen. Menschliches Eingreifen und Anfechtungsweg müssen daher vorgesehen sein. | [V] EUR-Lex |

---

## Folgen für Freigabe-Gates und Nachweise

1. **Gate „Regelraum“ (neu, vor allen Projekt-Gates).**
   - Die benannte bauvorlageberechtigte Person gibt jede Regelwerk-Version frei. Dazu gehören Hausmodelle, IDS, Geometrieregeln und Schwellenwarnungen.
   - Die Freigabe wird mit QES und einem `IfcApproval` an der `IfcProjectLibrary` festgehalten.
   - So wird „unter der Leitung“ belegbar: Die Person hat die rechtlich abgesicherte Einflussmöglichkeit (IK-Bau NRW 2024; Byak-BO 5.1; BVerfGE 28, 364; Drs. 15/7161).
2. **Das Gate „Bauvorlage“ ist eine Übernahmeprüfung, keine Unterschrift.**
   - Der Kundenentwurf ist eine Vorleistung. Die Prüfung umfasst Grundstücksdaten und deren Herkunft, alle Abweichungen vom Regelraum und alle Ergebnisse nahe am Grenzwert (BGH VII ZR 119/24; OLG Köln 19 U 23/20).
   - Ein Mitverschulden des Kunden ist nicht einzuplanen.
   - Das Gate prüft ausdrücklich auch, was im Freistellungsverfahren keine Behörde prüft (BGH VII ZR 391/99).
3. **Abweichungs-Gate mit dokumentierter Aufklärung.**
   - Wünscht der Kunde etwas außerhalb des Regelraums, etwa eine Befreiung vom Bebauungsplan, trägt er das Risiko nur nach umfassender, dokumentierter Aufklärung (BGH VII ZR 8/10; VII ZR 216/22).
   - Die Aufklärung wird als eigenes signiertes Dokument (`IfcDocumentReference`) im Modell hinterlegt.
4. **Warnsignale als Pflichtanzeige im Gate.**
   - Das Gate zeigt Grenzwertnähe, „gelbe“ Ergebnisse, widersprüchliche Nachweise und Hinweise Dritter wie Prüfstatiker oder Gemeinde als eigene Liste.
   - Zu jedem Warnsignal wird die Reaktion festgehalten: plausibilisiert, gegengerechnet oder verworfen. Sonst ist das Gate nicht abschließbar (OLG Köln 16 U 98/16).
   - Dieses Protokoll ist zugleich die Messgröße M9 aus Recherche 23 und erfüllt die Kriterien nach Sterz et al.: Eingriffsmacht, Einsicht, Zeit.
5. **Keine automatische Letztentscheidung gegenüber dem Kunden.**
   - Die App darf warnen und Alternativen vorschlagen.
   - Eine endgültige Ablehnung, die den Vertrag verhindert, braucht einen menschlichen Anfechtungsweg (DSK-OH 1.6; EuGH C-634/21).
6. **Nachweis-Paket je Prüfung.**
   - Inhalt: Regel-ID mit Fassung, Eingangsdaten mit Herkunft (Kunde, Amt, Firma), Hash, Ergebnis und Software-Build.
   - Gesichert wird es mit einem qualifizierten Zeitstempel und dem qualifizierten Siegel der Firma, das Integrität und Herkunft vermuten lässt (Art. 35, 41 eIDAS).
   - Die QES der Person gehört an das Gate und nicht an jeden Bericht. Nur sie bringt § 371a ZPO ins Spiel.
   - Für die Langzeitaufbewahrung (Hausakte) dienen Evidence Records nach TR-ESOR oder ein qualifiziertes Archiv (Art. 45i). Eine Blockchain ist nicht nötig.
7. **Nachweise so schreiben, dass ein Gerichtsgutachter sie ohne Code prüfen kann.**
   - Rechtlich ist der Bericht Parteivortrag (BGH VI ZR 243/92; OLG Nürnberg 8 U 1139/21). Sein Wert hängt an der Prüfbarkeit durch Dritte.
   - Das bestätigt Prinzip 9 des Zielbilds als Beweisvorsorge. Ergänzt wird es um „logging by design“ (Expert Group [20]–[22]).
8. **Einreichung nach bayerischem Stand.**
   - Bauvorlagen tragen künftig den Namen der Person im Plankopf, eine Unterschrift entfällt (Entwurf 2026).
   - Statik- und Brandschutznachweis bleiben unter der DBauV ein Abbild des unterschriebenen Originals.
   - Das Statik-Gate prüft die Qualifikation nach Art. 62a Abs. 1: Zimmerermeister nur mit Zusatzqualifikation.
9. **Typengenehmigung als Profil, nicht als Voraussetzung.**
   - Die Regelwerk-Version kann als „zweifelsfreie“ Beschreibung der Veränderbarkeit dienen (Drs. 18/8547).
   - Auch bei Typengenehmigung prüft das System Bebauungsplan, Abstandsflächen und Verfahren (Drs. 19/3023). Die Gestaltungssatzung entfällt.
10. **KI-VO-Grenze dokumentieren.**
    - In der Architektur wird festgehalten, dass die Regelmaschine ohne Inferenz arbeitet und nur das Intent-Modell ein KI-System ist (Leitlinien C(2025) 924).
    - Pflichten: Art. 50 Abs. 1 und Maßnahmen zur KI-Kompetenz nach Art. 4 in der Fassung von 2026/1744. Hochrisiko-Pflichten entstehen nicht.
11. **Sprache.**
    - Lokale Verarbeitung, keine Sprechererkennung und keine Speicherung von Rohaudio über die Sitzung hinaus (EDPB VVA; DSK-OH 2.5).
    - Gespräche mit dem Vertrieb werden nur mit Einwilligung aller Beteiligten aufgezeichnet (§ 201 StGB).

---

## Was ohne Datenbankzugang nicht erreichbar war

1. **Kommentarliteratur zu Art. 61 Abs. 6 BayBO.** Gemeint sind Simon/Busse und Jäde/Dirnberger/Bauer, dazu die Rechtsprechung der bayerischen Verwaltungsgerichte zur Frage, was „unter der Leitung“ im Unternehmen verlangt. Auch die Entstehungsgeschichte der Unternehmensregel vor 2008 (Art. 68 a. F. BayBO) ließ sich frei nicht ermitteln. Die Auslegung in dieser Recherche stützt sich deshalb auf das NRW-Kammerrecht (analog), BVerfGE 28, 364 und die Begründung von 2007. **Vor der Abgabe in beck-online prüfen.**
2. **Aufsätze in BauR, NZBau, IBR, ZfBR und NJW** zu KI oder Konfigurator in der Planung, zur Haftung des Entwurfsverfassers bei Kundenentwürfen und zur Typengenehmigung. Nur die IBR-Fundstellen der Urteile sind bekannt, die Anmerkungen nicht.
3. **Volltexte einzelner Entscheidungen.** Nicht im Volltext gelesen wurden OLG Karlsruhe 19 U 100/09, OLG Köln 19 U 23/20, BGH VII ZR 391/99, KG 27 U 82/22 und BayVerfGH Vf. 4-VII-97. Hier stammen die Kernaussagen aus Leitsätzen, Besprechungen oder Sekundärzitaten; die Zeilen sind entsprechend markiert.
4. **Keine veröffentlichte Entscheidung zu einem Laien, der mit Planungssoftware oder Konfigurator entwirft**, und keine zu KI in der Bauplanung. Der nächste Fall ist OLG Nürnberg 2 U 1369/10: Vertriebsplanung mit 3D-Animation beim Fertighaus.
5. **Versicherer-Merkblätter** zu KI oder Software in der Berufshaftpflicht der Architekten und Ingenieure waren frei nicht auffindbar. Offen bleibt, ob die Planungsleistung einer gewerblichen Fertighausfirma unter der Leitung einer Kammerangehörigen von deren Berufshaftpflicht gedeckt ist oder eine Betriebshaftpflicht braucht (vgl. AKNW 2019).
6. **Byak-Stellungnahme zu KI** wurde nicht gefunden. Die Merkblätter der Byak zur BayBO sind nach eigener Angabe nicht auf dem Stand der Novellen ab 2025.
7. **Stand des ProdHaftG.** Eine Beschlussempfehlung oder ein Gesetzesbeschluss zu BT-Drs. 21/4297 wurde bis 27.09.2026 nicht gefunden. Das Verfahren muss vor der Abgabe erneut geprüft werden.
8. **Keine eigene DSK-Orientierungshilfe zu Sprachassistenten oder Sprachaufnahmen.** Sie wird durch die EDPB-Leitlinien 02/2021 ersetzt. Ob Art. 35a BayVwVfG wortgleich mit § 35a VwVfG ist, wurde nicht separat abgerufen.
9. **Wortlaut von § 72a MBO** nicht am MBO-PDF geprüft; die Fassungsangabe stammt vom DIBt.

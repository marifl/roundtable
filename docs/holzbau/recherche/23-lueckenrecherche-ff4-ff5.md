# 23 Lückenrecherche FF4 (Verantwortung) und FF5 (Wirkung)

Status: v0.1 (27.09.2026). Diese Recherche setzt Protokoll 2a.3 Nr. 4 um (`../arbeit/02a-review-protokoll.md`). Anlass ist die Einzelbewertung (`../arbeit/literatur/bewertung/STATISTIK.md`): Nur 12 Quellen tragen FF4 mit Relevanz ≥ 2, nur 24 tragen FF5. Die 40 neuen Quellen stehen in `../arbeit/literatur/lit-H-ff4-ff5.bib`. Dubletten zu `quellen-master.csv` wurden über DOI und Titel ausgeschlossen. Vorhandene Quellen, auf die hier verwiesen wird, sind mit ihrem Key genannt, zum Beispiel `prodhaftg2026`, `haug2012definition` oder `brooke1996sus`.

**Prüfweg.** Direkte Abfragen an Crossref weist der Proxy mit 403 ab. Die Metadaten stammen deshalb aus der Crossref-REST-API, abgerufen über den Exa-Fetch (`api.crossref.org/works?filter=doi:…`); in den Tabellen heißt dieser Weg „Crossref“. Kernbefunde und Zahlen sind am Abstract geprüft, bei Open-Access-Fassungen am Volltext. Rechtsquellen sind an der amtlichen Fundstelle geprüft (EUR-Lex, Landtagsdrucksache), das BGH-Urteil über dejure.org.

**Legende.** Typ: W = Wissenschaft, N = Norm/Gesetz/Rechtsprechung, G = graue Literatur (siehe 2a.2). Passung: 0–3 je FF nach 2a.5; genannt sind nur FF ≥ 1. Status: [V] = verifiziert, [U] = Teilangabe unsicher (Grund in der Zeile und im `note`-Feld).

---

## Ergebnis in 5 Punkten

1. **Die Verantwortung bleibt beim Menschen. Das System muss sie deshalb an eine Person binden, nicht verteilen.**
   - Der BGH verlangt vom Architekten eine *dauerhaft genehmigungsfähige* Planung, und zwar unabhängig vom Verschulden (VII ZR 290/01).
   - Die neue Produkthaftungsrichtlinie 2024/2853 erfasst Software. Sie deckt aber weder reine Vermögensschäden noch Sachen, die ausschließlich beruflich genutzt werden. Der typische Planungsfehler (falscher Nachweis, Verzug, Mehrkosten) bleibt damit in der werkvertraglichen Haftung (`bgb`, `prodhaftg2026`). So ordnet es auch der Leitfaden der Bayerischen Ingenieurekammer-Bau vom 09/2026 ein.
   - Wilhelmi (2020) trennt *automatisierte* Systeme (feste, ex ante und ex post nachvollziehbare Regeln) von *autonomen* Systemen. Nur bei den autonomen entstehen echte Zurechnungslücken. Das stützt These 2: Maßgeblich ist der Regelraum, nicht das Sprachmodell.
2. **Nachvollziehbarkeit ist eine Frage der Beweisarchitektur, nicht der Blockchain.**
   - Cheung et al. (2026) haben ACC-Einführungen in Europa verglichen. Prüfergebnisse sind dort am besten erklärbar, wo die Darstellung der Nachweise und die Prüfmaschine strukturell zusammenpassen. Herkunftsnachweis (Provenance) und eine klare Zuordnung der Verantwortung wirken als Governance-Mechanismen.
   - Regulierer verlangen menschliche Aufsicht über algorithmische Entscheidungen (Fuchs et al. 2025; Beach et al. 2020).
   - Blockchain-Audit-Trails für BIM sind machbar (Celik et al. 2023). Nach dem Entscheidungsrahmen von Hunhevicz & Hall (2020) sind sie aber nur nötig, wenn sich die Beteiligten gegenseitig nicht vertrauen und keine vertrauenswürdige Instanz existiert. Für einen Hersteller mit eigener CDE genügen Hashwerte, CDE-Status und eine qualifizierte elektronische Signatur nach eIDAS.
   - Signaturen auf Objektebene in IFC sind noch unausgereift (Fakour et al. 2025). Auf Dateiebene läuft die Signatur mit QES bereits im Prototyp (CHEK D4.5).
3. **Das Hauptrisiko bei der Freigabe ist der Automation Bias, nicht der Modellfehler.**
   - Complacency und Automation Bias treten bei Laien wie bei Experten auf (Parasuraman & Manzey 2010).
   - Im Feldexperiment von Dell'Acqua et al. (2026) mit 758 Beratern lagen die Teilnehmer mit KI bei einer Aufgabe außerhalb der Fähigkeitsgrenze („Frontier“) im Mittel 19 Prozentpunkte seltener richtig.
   - Die BayIka nennt die unkritische Übernahme als größtes von Planenden selbst genanntes Risiko. Sie verlangt einen Dokumentationsbogen und eine Kontrollrechnung.
   - Folge für das Modell: Freigaben sind abgestufte Automatisierungsstufen (Parasuraman et al. 2000). Wie streng die Schutzmechanismen sind, richtet sich nach dem Anteil der Maschine (Naser 2026).
4. **Die Wirkung ist gut belegt für Angebot und Dokumentation, schlecht belegt für Änderungsschleifen im Fertighaus.**
   - Konfiguratoren verkürzen die Angebotsdurchlaufzeit im Mittel um 85,5 % (14 Firmen, Haug et al. 2011). Bei Grundfos sank sie von 9,5 auf 3,4 Tage (−64 %), die Personalstunden sanken um 75 % (Kristjansdottir et al. 2018).
   - 3D-Parametrik spart 15–41 % der Zeichenstunden (Sacks & Barak 2008). Im schwedischen Holzbau modelliert eine parametrische Plattform ETO-Bauteile 20-mal schneller (Thajudeen et al. 2022).
   - Für Nacharbeit gibt es nur allgemeine Baudaten: Die direkten Kosten liegen oft bei rund 5 % der Baukosten (359 Projekte, Hwang et al. 2009). Späte Änderungen stören am meisten (162 Projekte, Ibbs 2005).
   - Belastbare Zahlen zur Änderungsquote nach Vertragsschluss im deutschen Fertighaus fehlen. Die Ausgangswerte muss die Arbeit selbst erheben (siehe Messgrößen).
5. **Das Evaluationsdesign muss nach Nutzergruppen trennen und Aufgaben außerhalb der Systemgrenze enthalten.**
   - Generative KI hilft Unerfahrenen am meisten: Bei Brynjolfsson et al. (2025) steigt die Produktivität im Mittel um 15 %, bei weniger Erfahrenen um 30 %, bei den Besten sinkt die Qualität leicht. Noy & Zhang (2023) messen 40 % weniger Zeit und 18 % mehr Qualität.
   - Für die Arbeitsteilung heißt das: Laie, Vertrieb und Planer müssen getrennt ausgewertet werden.
   - Methodisch reichen die Taxonomie von Prat et al. (2015), Fokusgruppen nach Tremblay et al. (2010) und Stichproben von mindestens 10, besser 20 Personen je Gruppe. Mit 5 Personen fanden einzelne Stichproben nur 55 % der Probleme (Faulkner 2003).

---

## A FF4 Verantwortung: Recht, Freigabe, Nachvollziehbarkeit

### A1 Haftung und Verantwortung bei automatisierter und KI-gestützter Planung

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| BGH, VII ZR 290/01 (BauR 2002, 1872) | 2002 | N | Wer eine Genehmigungsplanung übernimmt, schuldet als Werkerfolg eine dauerhaft genehmigungsfähige Planung. Ist sie das nicht, ist das Werk mangelhaft, auch ohne Verschulden. Eine Risikoübernahme durch den Bauherrn muss vereinbart sein; bloße Kenntnis des Risikos genügt nicht. | **FF4: 3** – Maßstab für „prüffertig“: Das System entlastet den Entwurfsverfasser nicht, das Ergebnis muss genehmigungsfähig sein. FF2: 1. | [V] dejure.org |
| Wilhelmi: Haftung beim Einsatz von KI | 2020 | W | Unterscheidet automatisierte Systeme (feste, nachvollziehbare Regeln), autonome Systeme im weiteren Sinn und selbstlernende autonome Systeme. Das geltende Recht reicht über die Verkehrspflichten (§ 823 BGB) und die Produzentenhaftung aus. Mit zunehmender Autonomie verschiebt sich die Haftung zum Hersteller. | **FF4: 3** – liefert die juristische Begründung, das System als *automatisiert* (deterministischer Regelraum) auszulegen und nicht als autonom. | [V] KOPS-Volltext |
| EU-Produkthaftungsrichtlinie 2024/2853 | 2024 | N | Software ist ein Produkt. Das Gericht kann die Offenlegung von Beweismitteln anordnen, dazu kommen Vermutungen für Fehler und Kausalität. Ersatzfähig sind Tod, Körperverletzung, Sachschäden (ohne Sachen, die ausschließlich beruflich genutzt werden) und Datenverlust, reine Vermögensschäden nicht. Umsetzung bis 09.12.2026. | **FF4: 3** – bestimmt die Rolle des Werkzeugherstellers; unionsrechtliche Grundlage zu `prodhaftg2026`. FF3: 1. | [V] EUR-Lex |
| BayIka: KI in der Planung (Leitfaden) | 2026 | G | Die Verantwortung bleibt voll beim Ingenieur („Mit der Unterschrift … bürgen Sie“). Eine ungeprüfte Übernahme ist unzulässig. Die Kontrollrechnung hat 5 Schritte. Der Nachweis muss „aus sich heraus prüfbar“ bleiben. Anhang B verteilt die Verantwortung auf die Leistungsphasen, Anhang D ist ein Dokumentationsbogen für den KI-Einsatz. Die Einstufung von Statiksoftware nach dem AI Act ist offen. | **FF4: 3** – bayerisch, aktuell, direkt übernehmbar für das Freigabe- und Dokumentationsschema. FF5: 1 (Berufseinstieg, Kompetenz). | [V] Kammer-PDF |
| Naser: Engineers' Professional Responsibility in Using ML | 2026 | W | Grenzt die Opazität von ML von der Undurchsichtigkeit klassischer Rechenwerkzeuge (FE-Löser) ab. Schlägt ein dreistufiges Sicherungsprotokoll entlang der Schwellen der Sorgfaltspflicht vor. Die Offenlegungspflicht soll mit dem Anteil der ML am Ergebnis wachsen. Warnt vor einer Erosion ingenieurlicher Tugenden durch kognitives Auslagern. | **FF4: 3** – Vorlage für gestufte Freigaben nach Automatisierungsanteil. FF5: 1 (Rollenwandel). | [V] Crossref + ASCE |
| Jiang et al.: Liability Framework for GenAI in AEC | 2026 | W | Rechtsdogmatischer und rechtsvergleichender Rahmen mit proportionaler Haftung zwischen Entwickler, Betreiber und Fachnutzer. Kriterien: technische Kontrolle, Vorhersehbarkeit, Prüfmöglichkeit, Kausalbeitrag, Beweissicherung. Zwei Schadenspfade: Halluzination in sicherheitsrelevanter Planung und manipulierte Eingangsdaten. Ausdrücklich keine empirisch kalibrierte Formel. | **FF4: 2** – systematisiert die Rollen; bleibt international und qualitativ, das deutsche Werkvertragsrecht fehlt. | [V] Crossref + MDPI |
| Ng, Hall & Hsieh: Liability Factors for Design for Digital Fabrication | 2023 | W | Delphi-Studie mit 14 Beteiligten eines Projekts. 163 Haftungsfaktoren in 8 Kategorien, 85 davon wichtig. Am höchsten gewichtet: Managementfähigkeit (4,45) und BIM-Kompetenz (4,43). Vier Vertragsbausteine A–D für DBB, CM, DB und IPD. | **FF4: 2** – nächster Fall zur Kette Digitalplanung → Werk; Einzelfall aus Taiwan. FF5: 1. | [V] Crossref + ETH-Volltext |
| Parasuraman, Sheridan & Wickens: Types and levels of automation | 2000 | W | Vier Funktionen (Information erfassen, analysieren, entscheiden, handeln) mit je eigener Automatisierungsstufe von 1 bis 10. | **FF4: 2** – Gerüst, um Freigaben im Modell als Stufe je Funktion abzubilden. FF5: 1. | [V] Crossref |
| Parasuraman & Manzey: Complacency and Bias | 2010 | W | Complacency und Automation Bias treten bei Laien und Experten auf. Übung allein beseitigt sie nicht. Sie verstärken sich unter Mehrfachbelastung. | **FF4: 3** – begründet, warum eine reine Bestätigung per Klick keine Freigabe ist. FF5: 2 (Fehlerquote bei Freigabe messen). | [V] Crossref |

### A2 Freigabe-Workflows, CDE, Signatur und Audit-Trail

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Jaskula et al.: Common data environments | 2024 | W | Systematischer Review nach PRISMA über 46 Dokumente plus 15 Experteninterviews. Hauptproblem ist die parallele Nutzung mehrerer CDEs. Sie führt zu Problemen bei Zurechenbarkeit, Transparenz und Verlässlichkeit. | **FF4: 2** – belegt, dass Status und Freigabe in *einer* Quelle der Wahrheit liegen müssen. FF5: 1. | [V] Crossref (mit Abstract) |
| Hunhevicz & Hall: Do you need a blockchain in construction? | 2020 | W | Anwendungsfallkategorien und Entscheidungsbaum für DLT-Varianten. Eine Blockchain ist nur sinnvoll, wenn mehrere Schreibende einander misstrauen und keine vertrauenswürdige dritte Instanz vorhanden ist. | **FF4: 2** – kritisches Gegengewicht. Für den Herstellerfall ist die Antwort in der Regel „nein“. | [V] Crossref |
| Celik, Petri & Barati: Blockchain supported BIM data provenance | 2023 | W | Herkunftsnachweis für BIM-Objekte (Disziplin, Version, Verantwortung) über Smart Contracts im Ethereum-Testnetz, erprobt an einem Brückenprojekt. Die Kosten steigen mit der Zahl der Disziplinen und der Datenmenge. | **FF4: 2** – zeigt, welche Metadaten ein Audit-Trail braucht; Nutzen gegenüber CDE und Hash nicht belegt. | [V] Crossref + ORCA-Volltext |
| Fakour, Jaud & Poirier: Digital signatures in IFC at object level | 2025 | W | Untersucht, ob sich digitale Signaturen auf Objektebene ins IFC-Schema einbetten lassen. Offen sind die IFC-Struktur, die Langzeitprüfbarkeit und der Umgang mit Teiländerungen. | **FF4: 2** – Grenze der Nachvollziehbarkeit im Modell: Signaturen auf Objektebene sind Forschungsstand, nicht Praxis. | [V] Crossref (EC3) |
| Alfaro: CHEK D4.5 IFC digital signature module | 2025 | G | DSign signiert IFC-Dateien im Browser mit qualifizierter elektronischer Signatur (QES) nach eIDAS. Ablauf: Hash der Datei, Signatur über einen Vertrauensdiensteanbieter, Zeitstempel, eingebetteter Umschlag, ausdrücklicher Bestätigungsschritt. | **FF4: 2** – funktionierender Prototyp für die Signatur der Bauvorlage auf Dateiebene. FF1: 1. | [V] Projekt-PDF |
| eIDAS-VO 910/2014 i. d. F. 2024/1183 | 2014/2024 | N | Die qualifizierte elektronische Signatur ist der handschriftlichen gleichgestellt. 2024/1183 ergänzt die EUDI-Wallet. | **FF4: 2** – rechtlicher Rahmen für die digitale Unterschrift des Entwurfsverfassers; das Formerfordernis regelt das Landesrecht (`bayDigitalisierungEntwurf2026`). | [V] EUR-Lex; [U] Seitenangabe ABl. 2014 |

### A3 Erklärbarkeit und Rechtswirkung automatisierter Prüfergebnisse

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Cheung et al.: Institutionalizing ACC in Europe | 2026 | W | Vergleichende Mehrfallstudie mit Rekonstruktion von Modellen, Regeln und Ausführungsprotokollen. Prüfungen sind am besten erklärbar, wenn die Darstellung der Nachweise und die Prüfmaschine übereinstimmen. Datenreife und Provenance wirken als Governance-Mechanismen. Akzeptanz entsteht bei klarer Zuordnung der Verantwortung. | **FF4: 3** – der direkteste Beleg, wie ein Prüfbericht zum Nachweis wird: mit Regel-ID, Eingangsdaten und Protokoll. FF2: 2. | [V] Crossref + VTT-Abstract |
| Fuchs, Fauth, Boden & Amor: ACC – a regulatory view | 2025 | W | Experteninterviews mit Regulierern und ACC-Fachleuten weltweit. Hürden: mehrdeutige Begriffe, Widersprüche im Regelwerk, Balance zwischen menschlicher Aufsicht und algorithmischer Entscheidung. Vorschlag: Ampel oder Heatmap statt binärem bestanden/nicht bestanden. Mensch-Maschine-Zusammenarbeit über IFC-Viewer. | **FF4: 3** – TUM-Gruppe, Sicht der Behörden; stützt ein dreiwertiges Prüfergebnis mit menschlicher Entscheidung. FF2: 2. | [V] Crossref + mediaTUM |
| Beach, Hippolyte & Rezgui: Towards the adoption of ACC | 2020 | W | Hindernisse für die Einführung und eine Roadmap für Großbritannien. Die Industrie hält Automatisierung für machbar und erwünscht, *unter der Bedingung, dass die menschliche Aufsicht bleibt*. | **FF4: 2** – Akzeptanzbedingung für den Human-in-the-loop. FF2: 1. | [V] Crossref + Abstract |
| Zou et al.: Lessons learned on adopting ACC – a global study | 2023 | W | 18 Interviews mit 20 Experten aus 8 Ländern. 12 bestimmende Variablen, 3 Pfadmodelle, 10 Propositionen. Der Staat soll über Förderung, Vorgaben und digitalen Prüfpfad treiben. | **FF4: 2** – Rahmenbedingungen für einen Prüfpfad, den die Behörde anerkennt. FF5: 1. | [V] Crossref + UCL |
| Zou et al.: NZ off-site manufacturing readiness for ACC | 2022 | W | 44 Fragebögen, 16 Experteninterviews, 1 Fokusgruppe mit 9 Beteiligten. Der Bedarf ist hoch, aber die Vorfertigung, besonders KMU, ist nicht bereit. Fünf Handlungsfelder, darunter Schulung in BIM und ACC. | **FF4: 2**, **FF5: 2** – einzige gefundene Studie zu ACC *in der Vorfertigung*; Messinstrument für Bereitschaft übertragbar. | [V] Crossref + UCL |
| Love et al.: Explainable AI in construction | 2023 | W | Narratives Review mit Taxonomie aus Erklärbarkeit und Interpretierbarkeit, transparenten und opaken Modellen sowie Post-hoc-Verfahren. Katalog von Anforderungen der Beteiligten, darunter Rechenschaft, Verantwortung, Verifikation und rechtliche Konformität. | **FF4: 2** – liefert Begriffe; bestätigt, dass regelbasierte Modelle von sich aus transparent sind. FF2: 1. | [V] Crossref + arXiv |
| Landtag BW, Drs. 17/4637 (Typengenehmigung) | 2023 | N | Amtliche Stellungnahme: Die Typengenehmigung nach § 72a MBO wurde in den anderen Ländern „bislang nur in Einzelfällen“ angewandt, weil Freistellungsverfahren genügen. BW, Berlin, Bremen und das Saarland hatten 2023 keine Regelung. BW nutzt stattdessen die Typenprüfung für Standsicherheit, Schall- und Brandschutz. | **FF4: 2** – dämpft die Erwartung an die Typengenehmigung für serielle Einfamilienhäuser; Art. 73a BayBO steht in `baybo2026`. FF1: 1. | [V] Drucksache |

---

## B FF5 Wirkung: Durchlaufzeit, Schleifen, Fehler, Arbeitsteilung

### B1 Wirkung von Produktkonfiguratoren

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Haug, Hvam & Mortensen: Impact of configurators on lead times | 2011 | W | 14 technikorientierte Firmen. Die Angebotsdurchlaufzeit sinkt um bis zu 99,9 %, im Mittel um 85,5 %. Die Literatur enthielt davor nur 6 Fälle mit Zahlen. | **FF5: 3** – wichtigste Vergleichsgröße für die Zeit von der Anfrage zum Angebot bzw. Entwurf. FF1: 1. | [V] Crossref + Cambridge |
| Kristjansdottir et al.: ROI from product configuration systems | 2018 | W | Grundfos, 5 Jahre: 453.419 Personalstunden eingespart (−75 %). Angebotszeit von 9,5 auf 3,4 Tage (−64 %). ROI 316 % nach 1 Jahr und 842 % nach 5 Jahren bei 2,41 Mio. € Gesamtkosten; über Konfigurator 3,94-facher Absatz. | **FF5: 3** – vollständiges Kosten-Nutzen-Schema mit Entwicklung, Einführung und Pflege, übertragbar auf die Evaluation. | [V] Crossref + DTU-Volltext |
| Forza & Salvador: Managing for variety in the order process | 2002 | W | Fall eines Transformatorenherstellers. Der Konfigurator erhöht Wirksamkeit und Effizienz bei der Übersetzung des Kundenwunsches in die Produktdokumentation, sichert Produktwissen und erfordert anfangs hohen Aufwand und Umorganisation. Laut Sekundärzitat sinkt die Angebotszeit von 5–6 Tagen auf 1 Tag, die Stücklisten sind nahezu fehlerfrei. | **FF5: 2** – Mechanismus hinter der Fehlerreduktion; Arbeitsteilung zwischen Vertrieb und Technik. | [V] Crossref; [U] Zahlen nur sekundär |
| Trentin, Perin & Forza: Configurator impact on product quality | 2012 | W | Hypothesentest an einer Stichprobe von Fertigungsbetrieben: Die Nutzung eines Konfigurators verbessert die Produktqualität. Der Effekt ist schwächer, wenn der Marktbedarf schwer bestimmbar ist. | **FF5: 2** – quantitativer Beleg für die Qualitätswirkung; Moderator „unklarer Kundenbedarf“ ist im EFH-Laiengeschäft relevant. | [V] Crossref |

### B2 Nacharbeit, Änderungen und Durchlaufzeit in Bau und Vorfertigung

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Hwang et al.: Measuring the impact of rework | 2009 | W | 359 Projekte aus der CII-Datenbank. Die direkten Nacharbeitskosten liegen „oft bei 5 %“ der Baukosten. Die Wirkung hängt vom Projekttyp ab; die Hauptquellen (auftraggeberseitige Änderungen, Planungsfehler) sind über die Kategorien gleich. | **FF5: 2** – Ausgangswert für Nacharbeit; kein Fertighaus. | [V] Crossref + ASCE |
| Love & Edwards: Determinants of rework | 2004 | W | 161 australische Projekte, Gesamtkosten der Nacharbeit aus direkten und indirekten Kosten. Signifikant sind vom Auftraggeber veranlasste Änderungen und unwirksamer IT-Einsatz der Planer. Auch das Einfrieren des Planungsumfangs („design scope freezing“) erhöht die Nacharbeit, entgegen der Erwartung. | **FF5: 2** – nennt genau die Hebel, die ein Konfigurator adressiert: Kundenänderung und IT-Einsatz. | [V] Crossref |
| Love & Smith: Unpacking the ambiguity of rework | 2018 | W | Die berichteten Nacharbeitskosten reichen je nach Definition von unter 1 % bis über 20 %. Ohne Planungsänderungen und Auslassungen liegen sie meist unter 1 %. Es gibt keinen empirischen Beleg, dass BIM die Nacharbeit auf der Baustelle senkt; Kritik an Herstellerzahlen. | **FF5: 3** – methodisch zentral: Die Arbeit muss definieren, ob Änderungen des Kunden als Nacharbeit zählen. Warnt vor Werbezahlen. | [V] Crossref |
| Ibbs: Impact of change's timing on labor productivity | 2005 | W | 162 Projekte, drei Kurven für frühe, normale und späte Änderungen. Späte Änderungen senken die Produktivität stärker als frühe. | **FF5: 2** – begründet die Messgröße „Zeitpunkt der Änderung relativ zum Planungsfreeze bzw. Fertigungsstart“. | [V] Crossref + ASCE |
| Mubashar et al.: Variation orders in SMEs using MMC | 2026 | W | Britische KMU mit modernen Baumethoden: Befragung und Fallstudie. Eine Änderung zum Brandschutz 13 Wochen nach Fertigungsbeginn kostete 4 Wochen Verzug („Flaschenhals“ in der Linie). Am höchsten bewertet: Budgetabweichung (4,00), Verzug durch Kundenfreigaben (4,00), Nacharbeit (4,00). | **FF5: 2** – einziger aktueller Beleg zu späten Änderungen in der Vorfertigung mit Zeitangabe. FF4: 1 (Freigabe durch den Kunden als Engpass). | [V] Crossref |
| da Rocha, Kemmer & Meneses: Customization strategies and workflow variation | 2016 | W | Kundenänderungen im Wohnungsbau: Fehlende Kundeninformation stört den ersten und alle folgenden Arbeitsschritte. Leitlinien zu Informationsfluss und Individualisierungsumfang, dazu ein visueller Indikator für die Schwankung im Arbeitsfluss. | **FF5: 2** – Messidee für die Stabilität des Arbeitsflusses bei individualisierten Häusern; Brasilien. FF6: 1. | [V] Crossref |

### B3 Wirkung von BIM und Automatisierung auf die Planungszeit

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Sacks & Barak: 3D parametric modeling and productivity | 2008 | W | Benchmark und zwei Modellierexperimente: 15–41 % weniger Projektstunden allein durch die Zeichnungserstellung. Erwartet: weniger Zeichner im Verhältnis zu Ingenieuren und eine neue Rolle, der „structural modeler“. | **FF5: 3** – belegt Zeitgewinn *und* Rollenwandel; Stahlbeton, nicht Holz. | [V] Crossref + Technion |
| Thajudeen, Elgh & Lennartsson: Reuse of design assets in ETO components | 2022 | W | Schwedischer Hersteller von mehrgeschossigen Holzskelettbauten: Parametrische Design-Plattform für ETO-Anschlüsse (Konsolen). Der Modellierprozess wird 20-mal schneller; ETO-Bauteile werden konfigurierbar. | **FF5: 2** – Holzbau-Beleg mit Zahl; Einzelfall eines Bauteils. FF1: 1, FF6: 1. | [V] Crossref + MDPI |

### B4 Evaluationsdesign für Design-Science-Artefakte

| Quelle | Jahr | Typ | Kernbefund (mit Zahlen) | Passung FF (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Prat, Comyn-Wattiau & Akoka: Taxonomy of evaluation methods | 2015 | W | Taxonomie der Evaluation von IS-Artefakten nach Systemdimensionen (Ziel, Umgebung, Struktur, Aktivität, Entwicklung) mit Kriterien und generischen Methoden. | **FF5: 3** – Raster für die Wahl der Messgrößen; ergänzt `venable2016feds` und `sonnenberg2012evaluations`. | [V] Crossref |
| Tremblay, Hevner & Berndt: Focus groups in design research | 2010 | W | Explorative Fokusgruppen zur Verfeinerung und konfirmatorische Fokusgruppen zur Bewertung eines Artefakts, jeweils mit Ablaufvorgaben. | **FF5: 2** – Design für die Expertenbewertung mit Architekt, Tragwerksplaner und Prüfsachverständigem. | [V] Crossref |
| Faulkner: Beyond the five-user assumption | 2003 | W | 60 Nutzer, je 100 Zufallsstichproben. Stichproben mit 5 Personen fanden im Mittel 85 % der Probleme, einzelne nur 55 %. Mit 10 Personen mindestens 82 % (Mittel 95 %), mit 20 mindestens 95 % (Mittel 98 %). | **FF5: 3** – begründet die Stichprobengröße der Laien- und Vertriebsstudie. | [V] Crossref + Volltext |
| Noy & Zhang: Productivity effects of generative AI | 2023 | W | Präregistriertes Experiment mit 453 Akademikern bei Schreibaufgaben: 40 % weniger Zeit, 18 % höhere Qualität. Die Ungleichheit zwischen den Teilnehmern sinkt. | **FF5: 2** – Vorlage für das Design mit Kontrollgruppe und Zeit- und Qualitätsmaß; kein Bauwesen. | [V] Crossref + Science |
| Brynjolfsson, Li & Raymond: Generative AI at Work | 2025 | W | 5.172 Support-Agenten, gestaffelte Einführung. Die Produktivität steigt im Mittel um 15 % (Fälle je Stunde), bei weniger Erfahrenen um 30 %. Bei den Erfahrensten sinkt die Qualität leicht. Neue Agenten erreichen nach 2 Monaten das Niveau von 6 Monaten. | **FF5: 3** – erwartete Wirkung auf die Arbeitsteilung: Das System hebt den Vertrieb bzw. Laien, nicht den Experten. FF4: 1. | [V] Crossref + OUP |
| Dell'Acqua et al.: Navigating the jagged technological frontier | 2026 | W | 758 BCG-Berater, randomisiert. Innerhalb der KI-Fähigkeitsgrenze: 12,2 % mehr Aufgaben, 25,1 % schneller, deutlich höhere Qualität. Außerhalb: 19 Prozentpunkte seltener korrekt (84,5 % gegenüber 60 bzw. 70,6 %). | **FF5: 3**, **FF4: 2** – zwingt das Evaluationsdesign, Aufgaben außerhalb des Regelraums zu testen; misst den Automation Bias. | [V] Crossref + INFORMS |

---

## Messgrößen und Zielwerte für die Evaluation

Die Zielwerte sind aus der Literatur *abgeleitet*, nicht übernommen. Sie gelten als Hypothesen für Kapitel 17/19 und müssen gegen eine eigene Baseline beim Praxispartner gemessen werden. Belastbare Ausgangswerte für das deutsche Fertighaus fehlen (siehe unten).

| Nr. | Messgröße | Operationalisierung | Literaturanker | abgeleiteter Zielwert / Prüfkriterium |
|---|---|---|---|---|
| M1 | Durchlaufzeit Anfrage → Angebot/Vorentwurf | Kalendertage und Personalstunden je Projekt, vorher/nachher | Haug 2011 (−85,5 % im Mittel); Kristjansdottir 2018 (9,5 → 3,4 d, −75 % Stunden) | ≥ 50 % kürzer (konservativ unter den Literaturwerten, weil Bauvorhaben mehr Standortbezug haben) |
| M2 | Durchlaufzeit Vertrag → prüffähige Bauvorlage | Kalendertage; Stunden Architekt/Ingenieur | Sacks & Barak 2008 (−15–41 % Zeichenstunden); Thajudeen 2022 (20× bei ETO-Bauteil) | Stunden −30 %; Kalenderzeit nur berichten, weil Behördenwartezeit dominiert |
| M3 | Planungsschleifen | Anzahl der Planstände (Revisionen) zwischen Vorentwurf und Freigabe; Anzahl der Rückfragen Werk ↔ Planung | da Rocha 2016 (Schwankung im Arbeitsfluss); Love & Edwards 2004 | Median −1 Schleife je Projekt; Streuung berichten |
| M4 | Änderungsquote und Zeitpunkt | Änderungen je Projekt nach Vertrag, klassifiziert *vor/nach* Planungsfreeze und Fertigungsstart | Ibbs 2005 (späte Änderungen am schädlichsten); Mubashar 2026 (13 Wochen → 4 Wochen Verzug) | Anteil der Änderungen nach Fertigungsstart ≤ 5 % der Änderungen |
| M5 | Nacharbeitskosten | Direkte Kosten als % der Auftragssumme, *getrennt* mit und ohne Kundenänderungen | Hwang 2009 (≈ 5 % direkt); Love & Smith 2018 (< 1 % bis > 20 %, definitionsabhängig) | Definition vorab festlegen; Ziel < 1 % ohne Kundenänderungen |
| M6 | Fehlerquote der Spezifikation | Fehler in Stückliste und Bauteilliste je 100 Positionen, die das Werk findet | Forza & Salvador 2002 (nahezu fehlerfrei) [U]; Trentin 2012 | 0 Fehler bei Regeln, die das System abdeckt; Fehler außerhalb getrennt zählen |
| M7 | Güte der Regelprüfung | Richtig-positiv- und Falsch-positiv-Rate gegen Expertenurteil; Anteil „gelb“ (unklar) | Fuchs 2025 (Ampel statt binär); Cheung 2026 (Erklärbarkeit) | Falsch-negativ bei Muss-Regeln = 0; Anteil „gelb“ berichten |
| M8 | Nachvollziehbarkeit (FF4) | Anteil der Prüfergebnisse mit Regel-ID, Norm- und Fassungsangabe, Eingangsdaten-Hash; Test: erneute Ausführung liefert dasselbe Ergebnis | Cheung 2026; Celik 2023; BayIka 2026 (Dokumentationsbogen) | 100 % der Ergebnisse vollständig; Reproduktion 100 % |
| M9 | Freigabequalität und Automation Bias (FF4) | Eingestreute fehlerhafte Vorschläge: Anteil, den der Freigebende erkennt; Zeit je Freigabe | Parasuraman & Manzey 2010; Dell'Acqua 2026 (−19 pp außerhalb der Grenze) | Erkennungsrate berichten; Ziel: nicht schlechter als die Kontrollgruppe ohne System |
| M10 | Aufgabenerfolg und Zeit Laie/Vertrieb | Anteil gelöster Konfigurationsaufgaben; Zeit je Aufgabe | Noy & Zhang 2023; Brynjolfsson 2025 | Erfolg ≥ 80 %; Wirkung je Gruppe getrennt ausweisen |
| M11 | Gebrauchstauglichkeit und Beanspruchung | SUS; NASA-TLX | `brooke1996sus`, `bangor2008empirical`, `hart2006tlx` (vorhanden) | SUS ≥ 68 (Durchschnitt), Ziel ≥ 80 |
| M12 | Stichprobe | Personen je Nutzergruppe | Faulkner 2003 | ≥ 10 je Gruppe (mindestens 82 % der Probleme), Ziel 20 (≥ 95 %) |
| M13 | Arbeitsteilung | Stundenanteile je Rolle (Kunde, Vertrieb, Architekt, Ingenieur, Werk) vorher/nachher; neue Rollen | Sacks & Barak 2008 (Zeichner → Modellierer); Brynjolfsson 2025 | Verschiebung beschreiben, kein Zielwert; qualitativ über Experteninterviews (`bogner2014interviews`) |
| M14 | Wirtschaftlichkeit | ROI nach 1 und 5 Jahren mit Entwicklung, Einführung und Regelpflege | Kristjansdottir 2018 (Schema) | Schema übernehmen; die Regelpflege ausdrücklich einrechnen |

**Design-Hinweise.** (1) Die Evaluation muss Aufgaben innerhalb *und* außerhalb des Regelraums enthalten (Dell'Acqua), sonst ist M9 nicht messbar. (2) Die Nutzergruppen sind getrennt auszuwerten, weil die Effekte heterogen sind (Brynjolfsson). (3) Die Expertenbewertung erfolgt als explorative und konfirmatorische Fokusgruppe (Tremblay). Die Kriterien stammen aus der Taxonomie von Prat, die Strategie aus FEDS (`venable2016feds`). (4) Nacharbeit wird nach Love & Smith definiert, bevor gemessen wird.

---

## Geprüft, aber zurückgestellt (verifiziert, nicht in der Bib-Datei)

Um bei 40 Quellen zu bleiben, wurden folgende verifizierte Arbeiten nicht aufgenommen. Sie können bei Bedarf ergänzt werden:
- Love & Li 2000, *CME* 18(4), 10.1080/01446190050024897: zwei Fälle, Nacharbeit 3,15 % und 2,40 % der Auftragssumme.
- Love 2002, *JCEM* 128(1), 10.1061/(ASCE)0733-9364(2002)128:1(18).
- Love, Edwards & Irani 2008, *IEEE TEM* 55(2), 10.1109/TEM.2008.919677: Planungsbedingte Nacharbeit macht über 70 % der gesamten Nacharbeit aus.
- Josephson & Hammarlund 1999, *AutCon* 8(6), 10.1016/S0926-5805(98)00114-9. Zahlen nicht am Abstract geprüft.
- Thomas & Napolitan 1995, *JCEM* 121(3), 10.1061/(ASCE)0733-9364(1995)121:3(290).
- Myrodia, Kristjansdottir & Hvam 2017, *Comput. Ind.* 88, 10.1016/j.compind.2017.03.001: Projekte mit mehr als 10 % Kostenabweichung sanken von 14,6 % auf 2,2 %; Zahl aus der Konferenzfassung.
- Forza & Salvador 2002b, *Comput. Ind.* 49(1), 10.1016/S0166-3615(02)00057-X.
- Zhang 2014, *IJPR* 52(21), 10.1080/00207543.2014.942012: Review.
- Wuni, Shen & Mahmud 2019/2022, *IJCM* 22(2), 10.1080/15623599.2019.1613212: „fehlerhafte Planung und Änderungen“ auf Rang 7 von 30 Risiken im Modulbau.
- Abdul Nabi & El-adaway 2022, *JCEM* 148(7), 10.1061/(ASCE)CO.1943-7862.0002311: 68 Modulbauprojekte; Zahlen zur Zeitersparnis nicht geprüft.
- Lopez & Froese 2016, *Procedia Eng.* 145, 10.1016/j.proeng.2016.04.166.
- Li, Greenwood & Kassem 2019, *AutCon* 102, 10.1016/j.autcon.2019.02.005.
- Arensman & Ozbek 2012, *IJCER* 8(2), 10.1080/15578771.2011.617808.
- Alwash, Love & Olatunji 2017, *JLADR* 9(3), 10.1061/(ASCE)LA.1943-4170.0000219.
- Ittmann et al. 2018, *JLADR* 10(3), 10.1061/(ASCE)LA.1943-4170.0000265: Sorgfaltsmaßstab des Tragwerksplaners, US-Recht.
- Plevris & Hosamo 2025, *Front. Built Environ.* 11, 10.3389/fbuil.2025.1612575.
- Matthias 2004, 10.1007/s10676-004-3422-1; Santoni de Sio & Mecacci 2021, 10.1007/s13347-021-00450-x: Verantwortungslücken, philosophisch.
- Bainbridge 1983, 10.1016/0005-1098(83)90046-8.
- Kim et al. 2020 (K-BIM e-Submission), *JCEM (VGTU)* 26(8), 10.3846/jcem.2020.13756.
- Agri, Le & Phung 2025, *AEDM* 22(1), 10.1080/17452007.2025.2548911: 23 Interviews, 83 % nutzen KI im Alltag; genannte Hürde: rechtliche Unsicherheit.
- Bloch et al. 2026, *AEDM* 22(4), 10.1080/17452007.2026.2632103.
- Elrawy & Wagdy 2025, *AI & Society* 40(6), 10.1007/s00146-025-02193-1.
- Voordijk 2009, *CME* 27(8), 10.1080/01446190903117777.
- Nielsen & Landauer 1993, 10.1145/169059.169166.
- Frey & Osborne 2017, 10.1016/j.techfore.2016.08.019; Autor 2015, 10.1257/jep.29.3.3.
- Kaner et al. 2008, ITcon 13, 303–323: ohne Zahlen im Abstract.

**Nicht verifizierte Hinweise (nur Herstellerangaben, nicht zitierfähig, [U]):**
- Elecosoft/F.R.E.D.S. Timberframe: Werkplanung von 8–10 Wochen auf 1 Woche.
- PTC/Reframe Systems: Wandmodellierung 3–4-mal schneller.
- HOMAG/B&O Bau: Arbeitsvorbereitung von rund 30 auf 2 Tage je Gebäude (−95 %).
- Nordic BIM/Tene: 50 % weniger Zeit je Haus.

Diese Zahlen zeigen die Größenordnung, die der Markt behauptet. Nach Love & Smith (2018) sind sie ausdrücklich nicht als Beleg zu verwenden.

---

## Was nicht gefunden wurde

1. **Keine frei zugänglichen juristischen Aufsätze in BauR, NZBau oder ZfBR zu KI- oder algorithmischer Planung und Haftung des Entwurfsverfassers.** Die Zeitschriften liegen hinter beck-online bzw. juris und waren nicht einsehbar. Gefunden wurden nur:
   - berufsständische Stellungnahmen (BayIka 2026; BAK-FAQ „Wer haftet für Fehler beim KI-Einsatz“, 2024; AKNW-Positionspapier 2025),
   - ein allgemeiner zivilrechtlicher Beitrag (Wilhelmi 2020),
   - BGH-Rechtsprechung zur Genehmigungsplanung.

   Vor der Abgabe ist eine Recherche in beck-online nötig (Suchbegriffe: „KI Architektenhaftung“, „Planungssoftware Mangel“, „Typengenehmigung serielles Bauen“).
2. **Keine wissenschaftliche Untersuchung der Bauvorlageberechtigung bei serieller oder algorithmischer Planung.** Offen bleibt, wer bei einem vom System erzeugten Plan „Entwurfsverfasser“ im Sinne der BayBO ist. Dazu fanden sich nur Verbandspapiere (ZIA-Kurzgutachten 2023, HDB/GdW-Positionspapier 2023) und die Drucksache aus Baden-Württemberg.
3. **Keine empirische Studie zur Nutzung von IfcApproval** und keine wissenschaftliche Bewertung der Status-Codes S0–S4/A/B. Diese Codes stammen aus dem britischen Nationalen Anhang zu BS EN ISO 19650-2, nicht aus dem ISO-Kern. Dazu gibt es nur den UK-BIM-Framework-Leitfaden Teil C (grau, nicht aufgenommen). Das Schema selbst steht in `iso2024ifc` und `iso19650`.
4. **Keine Aussage zur Rechtsverbindlichkeit automatisierter Prüfberichte im deutschen Bauordnungsrecht.** Die internationale Literatur (Cheung 2026, Fuchs 2025, Beach 2020) behandelt ACC-Ergebnisse durchweg als Entscheidungs*grundlage*, nicht als Verwaltungsakt.
5. **Keine veröffentlichten Durchlaufzeiten und Änderungsquoten deutscher Fertighaushersteller.** Gesucht wurde nach Zeit vom Vertrag über Bemusterung und Bauantrag bis zur Fertigung sowie nach Kundenänderungen nach Vertrag. Einzige Quelle mit Herstellerdaten bleibt `schoenwitz2012nature` (16 Projekte eines deutschen Herstellers, vorhanden). Die Ausgangswerte M1–M5 müssen beim Praxispartner erhoben werden.
6. **Keine begutachtete Fallstudie mit Zahlen zur Planungszeit im Holzrahmenbau nach BIM-Einführung.** Die Zahlen stammen nur von Anbietern (siehe oben). Die nächsten Belege sind Holzskelettbau (Thajudeen 2022) und Betonfertigteile (Sacks & Barak 2008). Für die Rollen liegen leanWOOD und Holz&BIM bereits in `lit-G-luecken.bib`.
7. **Keine Studie zu Deskilling oder Upskilling speziell bei deutschen Architekten oder Tragwerksplanern.** Die BayIka warnt qualitativ, dass früher KI-Einsatz bei Berufseinsteigern die Urteilsfähigkeit untergräbt. Die belastbaren Daten zur Heterogenität der Effekte stammen aus anderen Branchen (Brynjolfsson, Noy & Zhang, Dell'Acqua).
8. **Keine Klärung, ob Bauvorlagen in Bayern eine qualifizierte elektronische Signatur brauchen.** Das regelt der Digitalisierungsentwurf (`bayDigitalisierungEntwurf2026`, vorhanden). Er muss nach Inkrafttreten nochmals geprüft werden.

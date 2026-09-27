# 21 Lückenrecherche: regionale Holzbauforschung, deutschsprachige Architekturpsychologie, Methodenstandards

Status: v0.1 (27.09.2026). Diese Recherche setzt Protokoll 2a.3 Nr. 4 um (`../arbeit/02a-review-protokoll.md`). Die neuen Quellen stehen in `../arbeit/literatur/lit-G-luecken.bib`. Dubletten zu `quellen-master.csv` sind mit ihrer Q-Nummer gekennzeichnet und wurden nicht neu aufgenommen.

**Prüfweg und Grenzen.** Direkte Abfragen an Crossref, OpenAlex, DNB (Portal und SRU) und GEPRIS werden vom Egress-Proxy mit 403 abgewiesen, per curl ebenso wie per WebFetch. Crossref-Metadaten wurden deshalb über den Exa-Fetch der Crossref-REST-API abgerufen (`api.crossref.org/works/<DOI>`); in der Tabelle heißt dieser Weg „Crossref“. GEPRIS und DNB waren nur indirekt über den Exa-Suchindex erreichbar. Alles andere ist über die Primärquelle geprüft: Verlagsseite, Projektseite der Hochschule, Förderdatenbank (Zukunft Bau, FNR, FFG) oder Repositorium (mediaTUM, HSBI, reposiTUm).

**Legende.** Typ: W = Wissenschaft, N = Norm, G = graue Literatur, T = Technik (siehe 2a.2). Passung: 0–3 je FF nach 2a.5. Aufgeführt sind nur FF mit einem Wert ≥ 1; alle übrigen stehen auf 0. Status: [V] = bibliografisch verifiziert, [U] = unsicher (Grund in der Tabelle und im `note`-Feld der Bib-Datei).

---

## Ergebnis in 5 Punkten

1. **Rosenheim hat einschlägige Forschung, aber keinen Konfigurator.** Die TH Rosenheim forscht zu Robotik in der Wandfertigung (RoWaPla 2024–2026: KI-Bahnplanung aus CAD-Daten, digitaler Zwilling) und zu BIM-gestützten Schallschutzprognosen. Gemeinsam mit dem ift Rosenheim liefert sie Planungsdaten für DIN 4109 (Holzmodulbau, Fugenschalldämmung beim Fenstereinbau). Das deutschsprachige Standardwerk zur Holzbau-Automatisierung stammt ebenfalls aus Rosenheim: Heinzmann & Karatza 2022 (Springer Vieweg). Ein Projekt zu Kundenkonfiguration, Laienentwurf oder zur Kette Entwurf → Bauantrag wurde nicht gefunden. Das ist die Forschungslücke, die die Arbeit besetzt.
2. **Die nächsten Vergleichsarbeiten für FF1/FF2 sind deutsche Zukunft-Bau-Projekte.**
   - „Variowohnen Kassel“ (Eisfeld & Mons 2022): wissensbasierter BIM-Wohnungskonfigurator mit Regeln in BIM-Objekten und open BIM über IFC.
   - „Digital Craft“ der HM München (2023–2026): parametrisches Hausmodell, aus dem alle Bauteile automatisch erzeugt werden.
   - DesignChain von Fraunhofer IPA und Wood Pro: regelbasierte Wandelement-Generierung bis zum Nagelbild.
   - Dazu kommen leanWOOD und Holz&BIM (TUM) als Grundlage für Leistungsbilder und Rollen (FF4/FF5).
3. **Bei den Herstellern gibt es kaum öffentlich dokumentierte Forschung.**
   - Regnauer gibt 2–4 wissenschaftliche Arbeiten pro Jahr mit der TH Rosenheim an und sitzt im Fachbeirat Holztechnik. Die Arbeiten selbst sind nicht öffentlich.
   - Haas Fertigbau hat einen Konfigurator mit Revit-Anbindung. Beleg ist nur eine Anbieter-Pressemitteilung.
   - Baufritz hat einen Dämmstoff mit der FH Rosenheim, der TUM und Fraunhofer entwickelt.
   - Für Huf Haus, WeberHaus, Schwörer und Bien-Zenker ist keine Hochschulkooperation zu Digitalisierung dokumentiert.
4. **Die deutschsprachige Architekturpsychologie ist vorhanden und prüfbar.**
   - Standardwerke von Flade: 2006, 2008 und zwei Bände 2020, davon einer zum Wohnen.
   - Hellbrück & Kals 2012, Walden 2008, Häußermann & Siebel 1996, Schneider & Spellerberg 1999, Handbuch Wohnsoziologie 2021.
   - Richter 2016, Rambow 2000 und Vollmer 2010 sind Dubletten.
   - Für 9b am wertvollsten ist die BBSR-Studie „Funktionswandel des Wohnens“ (Wegener et al. 2024). Sie ist die größte repräsentative Befragung zu Wohnwünschen nach Corona. 84 % der Befragten, die zu Hause arbeiten können, nutzen das Homeoffice. Nur die Hälfte hält die eigene Wohnung dafür für geeignet; genannt werden fehlender Rückzugsraum, zu wenig Platz, Lärm und Dunkelheit. Das sind direkt übersetzbare R5-Empfehlungen.
5. **Alle geforderten Methodenstandards sind verifiziert.**
   - Kitchenham & Charters 2007, Wohlin 2014, PRISMA 2020, Cohen 1960 (dazu Landis & Koch 1977 für die κ-Interpretation) und Sonnenberg & vom Brocke 2012.
   - Mayring 2022 (13. Aufl.), Kuckartz & Rädiker 2024 (6. Aufl.), Bogner/Littig/Menz 2014 und Gläser & Laudel 2010.
   - SUS nach Brooke 1996 (dazu Bangor et al. 2008 für Normwerte) und NASA-TLX nach Hart & Staveland 1988 (dazu Hart 2006).
   - ISO 9241-11:2018 und ISO 9241-110:2020, beide 2023 bzw. 2025 bestätigt.
   - Die DSR-Grundlagen (Hevner, Peffers, Gregor & Hevner, Venable) sind Dubletten.

---

## A Regionale und holzbaunahe Forschung

| Quelle | Typ | Jahr | Inhalt kurz | Passung FF1–FF6 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Heinzmann & Karatza: *Automatisierung und Digitalisierung im Holzbau*, Springer Vieweg, DOI 10.1007/978-3-658-38763-1 | W (Fachbuch) | 2022 | Fertigungsprinzipien (Takt, Linie, Zelle), Automatisierungsstufen der Holzrahmenbau-Vorfertigung; Kap. 5 „Digitaler Prozess und Informationsfluss“; Mass Customization. Autor: TH Rosenheim | FF1 2 · FF5 2 · FF6 1. Belegt, welche Daten die Werkautomatisierung aus der Planung braucht (FF1). Liefert Vergleichsraster für den Automatisierungsgrad (FF5). Regionaler Kernbeleg für Kap. 3.2 | [V] Crossref |
| Riß et al. (TH Rosenheim): *RoWaPla – Roboterbasierte Wandbeplankung unterstützt durch KI* | G (Projekt) | 2024–2026 | Roboterzelle für die Beplankung von Holzrahmenwänden. CAD-Analyse-Algorithmus extrahiert Kernkonstruktion und Beplankung; digitaler Zwilling; KMU-Fokus. Partner: holzbau.tech, innFactory, SAFELOG | FF1 2 · FF5 1 · FF6 1. Zeigt, dass Ständer und Beplankung als Einzelteile im Modell stehen müssen, damit Maschinendaten ableitbar sind. Stützt das Klassenmapping in 8.2 | [V] Projektseite TH Rosenheim |
| Schanda et al. (TH Rosenheim): *Prognoseverfahren zum Schall- und Schwingungsschutz für BIM-basierte Gebäudeplanung* | G (Projekt) | 2018–2022 | Prognosemodelle der Bauakustik im Holzbau, BIM- und KI-Einbindung, Normungsarbeit. Verwandt mit Châteauvieux 2023 (Q234) | FF2 2 · FF6 2 · FF1 1. Schallschutz-Nachweis als modellbasierte Regel. Eingangsdaten für die Prüfschicht | [V] Projektseite TH Rosenheim |
| Rabold et al. (TH Rosenheim / ift): *Schallschutz von Gebäuden in Holzmodulbauweise*, Zukunft Bau SWD-10.08.18.7-22.29 | G (Forschungsbericht) | 2022–2024 | Planungsdaten Luft- und Trittschall für Trennbauteile im Modulbau, Bauteilkatalog zur Integration in DIN 4109-33 (Q183) | FF2 2 · FF6 2. Tabellierte Kennwerte als Datenbasis für das MFH-Regelprofil (9a) und Schallschutz zwischen Nutzungseinheiten | [V] Projektseite TH Rosenheim, Fachartikel magazin-quartier.de |
| Rabold, Châteauvieux-Hellwig & Schramm (ift): *Vibroakustik im Planungsprozess für Holzbauten – Teilprojekt 4*, IGF 18725 N | G (Kurzbericht) | o. J. | SEA-Prognosetool „VBAcoustic“ mit **IFC-Schnittstelle**; Stoßstellendämm-Maße; Validierung an Baumessungen | FF1 2 · FF2 2 · FF6 1. Präzedenzfall für eine Nachweisrechnung, die direkt aus dem IFC gespeist wird („Programme interpretieren“) | [U] Jahr nicht angegeben; Existenz über iVTH-PDF |
| Saß (ift Rosenheim): *Nachweis des Fugenschalldämm-Maßes für kritische Einbausituationen*, Zukunft Bau 10.08.18.7-23.23 | G (Projekt) | 2023–2026 | Planungsdaten für den Fenstereinbau in der Dämmebene, Ergänzung DIN 4109-35 | FF2 2 · FF6 2. Regel für die Einbausituation von Fenstern; betrifft Bemusterung und Wandaufbau | [V] zukunftbau.de |
| Kaufmann, Huß, Schuster & Stieglmeier (TUM): *leanWOOD*, Schlussbericht FKZ 22004214 | G (Forschungsbericht) | 2018 | Prozess- und Kooperationsmodelle für den vorgefertigten Holzbau; holzbaugerechte Leistungsbilder nach HOAI; Holzbauingenieur nach Schweizer Vorbild | FF4 2 · FF5 2. Rollen, Schnittstellen und Zeitpunkt der Holzbaukompetenz; Grundlage für Freigabe-Gates und Arbeitsteilung | [V] mediaTUM |
| Kaufmann, Schuster & Stieglmeier (TUM): *Holz&BIM*, Schlussbericht FKZ 22001818 | G (Forschungsbericht) | 2019 | Standortbestimmung: Anforderungen und Hemmnisse von BIM im Holzbau; Vorstudie zu BIMwood | FF5 2 · FF1 1. Empirische Hemmnisse; Ausgangslage für 1.1 und 5.3 | [V] mediaTUM |
| Schuster, Arnold & Behm: *BIM und vorgefertigter Holzbau – Der BIMwood Referenzprozess*, Forum Bauinformatik 33 | W (Konferenz) | 2022 | Referenzprozess mit deskriptiver und prozessualer Ebene. Ergänzt BIMwood (Q091 TUM, Q092 HSLU, **Dubletten**) | FF1 2 · FF4 1. Begutachtete Kurzfassung des BIMwood-Prozesses; zitierfähiger als der Bericht | [V] mediaTUM |
| BFH/HSLU: *DeepWood* (Innosuisse) | G (Projektnotiz) | 2022 | Echtzeit-kollaborative Planung auf einer Industrieplattform; Performancematrix für den vorgefertigten Holzbau | FF1 1 · FF5 1. Gegenposition zu IFC-Dateiaustausch (Plattform statt Datei); Lock-in-Befund | [V] BFH-News 12.10.2022 |
| Standtke & von Gunten (BFH): *Plattform Wald & Holz 4.0, TP 2.4 Systematisierte digitale Bausteine und Schnittstellen* | G (Projekt) | 2023–2024 | Material- und Produktdaten nach ETIM/BMEcat für CAD und ERP im Holzbau; Abgrenzung zu IFC offen | FF6 1 · FF1 1. Produktdatenstandard für die Bemusterung neben bSDD | [V] wh40.ch |
| Standtke & Jack (BFH IDBH): *Businessintegrations-Plattform für die Holzbranche* (Innosuisse) | G (Projekt) | 2024–2025 | Firmenübergreifende Integration von ERP, CAD/CAM und CNC ohne proprietäre Schnittstellen | FF1 1. Kontext „andere Formate sind Ableitungen“ | [V] bfh.ch |
| TU Graz u. a.: *Sys.Wood – Systemoptimierung im österreichischen Holzbau* (FFG) | G (Projekt, Zwischenbericht) | 2023–2026 | Umfrage bei 63 Unternehmen: Softwarekompatibilität, Datenformate, redundante Arbeit; BIM-BIM- und BIM-CAM-Tests; Lean | FF5 2 · FF1 1. Aktuelle empirische Schnittstellenbefunde für die Problemstellung | [V] TUGRAZonline, Zwischenbericht 2025 |
| Holz.Kompetenzzentrum (Österreich): *Fertighausbau 4.0* (FFG) | G (Projekt) | 2018–2021 | Industrie 4.0 in der Variantenfließfertigung von Fertighäusern, RAMI 4.0, agentenbasierte Simulation | FF5 2 · FF1 1. Einzige gefundene Forschung explizit zum Fertighauswerk | [V] FFG-Projektdatenbank |
| Kyjanek, Krieg, Schwinn & Menges (Uni Stuttgart ICD): *Mensch-Roboter-Kooperation im Holzbau*, Zukunft Bau 16.56, Fraunhofer IRB, ISBN 978-3-7388-0461-4 | G (Forschungsbericht) | 2020 | MRK-Strategien für die Holzbau-Vorfertigung mit Müllerblaustein und KUKA | FF5 1 · FF6 1. Kontext Werk; Menges-Gruppe schon mit Q081, Q235, Q236 vertreten | [V] Zukunft-Bau-PDF |
| ICD Uni Stuttgart: *Prädiktive Modellierung zur Inkorporation des Menschen in der automatisierten Vorfabrikation*, Zukunft Bau 10.08.18.7-25.12 | G (Projekt) | 2026–2027 | Physiologische Daten und ML für die Mensch-Maschine-Kooperation in der Vorfertigung | FF5 1. Laufend; nur Ausblick | [V] zukunftbau.de |
| Eisfeld & Mons: *Variowohnen Kassel, Endbericht* (Zukunft Bau, Variowohnungen) | G (Forschungsbericht) | 2022 | Big open BIM über IFC; **wissensbasierter BIM-Wohnungskonfigurator**: Regeln der seriellen Elemente in BIM-Objekten, Konfiguration des Rohbaus; Kosten- und Bauzeitauswertung | FF2 3 · FF1 2 · FF5 2. Nächster deutscher Präzedenzfall für regelbegrenzte Konfiguration im Wohnungsbau; Pflicht in der Vergleichsmatrix 5.7. Unterschied: Planerwerkzeug statt Laienentwurf, ArchiCAD-Regeln statt IDS | [V] HSBI-Publikationsserver, zukunftbau.de |
| Krüger et al. (HM München): *Digital gefertigter Hausprototyp auf Basis eines Holzbaustecksystems*, Zukunft Bau 10.08.18.7-23.32 | G (Projekt) | 2023–2026 | Parametrisches Gittermodell (Grundriss, Kubatur, Dachform, Fenster frei konfigurierbar) → alle Bauteile automatisch erzeugt → direkte Fertigung; Partner Hundegger, Egger, Steico | FF6 2 · FF2 1 · FF1 1. Regional vergleichbare Arbeit zu „Modell → Maschinendaten“. Behauptung „Leistungsphasen entfallen“ ist zu FF4 abzugrenzen | [V] zukunftbau.de, HM-Projektseite |
| Robeller et al. (TH Augsburg DTC): *Timber Structures Interface (TSI)*, FNR 2220HV001X | G (Abschlussbericht) | 2024 | Datenschnittstelle für automatisierte Statik digital vorgefertigter Holztragwerke (mit Dlubal) | FF1 1 · FF6 1. Bayerischer Beleg für Statik-Ableitung aus Fertigungsgeometrie | [V] FNR-Projektdatenbank |
| Fraunhofer IPA: *DesignChain nachhaltiger Wandelemente* (Referenzprojekt mit Wood Pro IBS / Rhomberg) | G (Referenzbericht) | o. J. | Regelwerk erzeugt aus Eingangsparametern das vollständige 3D-Wandelement inkl. Nagelbild; Anbindung Revit | FF1 2 · FF6 2 · FF2 1. Industrieller Beleg für die regelbasierte Ableitung von Werkplanung | [U] Jahr fehlt auf der Seite; Existenz [V] ipa.fraunhofer.de |
| TU Berlin / Fraunhofer IPK und WKI: *DiKieHo – Digitale Wertschöpfungskette für den kieferbasierten Holzbau* | G (Projekt) | 2022 | Referenzmodell zur Vernetzung der Akteure im urbanen Holzbau Berlin-Brandenburg | FF1 1. Kontext Wertschöpfungskette | [V] wki.fraunhofer.de |
| Prochiner: *Homes 24 – Zukunftsorientierte Fertigungs- und Montagekonzepte im industriellen Wohnungsbau*, Diss. TUM | W (Dissertation) | 2006 | Vorfertigung und Fertighaus, Gewerkeintegration „Plug & Play“, Schnellverbinder, Robotik | FF6 2 · FF5 1. Historische Referenz für vorinstallierte TGA im Element (FF6) | [V] mediaTUM |
| Hoch: *BIM im Kleinprojektbereich – Einfamilienhausbau*, Diplomarbeit TU Wien | W (Abschlussarbeit) | 2026 | BIM-Template für Planung und Ausführung eines EFH in einem Kleinunternehmen; Nutzen für Planer, Poliere, Bauherren | FF5 1 · FF1 1. Abschlussarbeit, Massivbau; nur Kontext | [V] reposiTUm |
| Kuhl: *Robotik im Holzbau: Untersuchung grundlegender Fragen der Vorfertigung*, Bachelorarbeit HTWK Leipzig | W (Abschlussarbeit) | 2023 | Vorfertigung Wand/Decke, Robotik, Experteninterviews | FF5 1. Nur Kontext; zitiert Heinzmann & Karatza | [U] nur über Exa-Bibliothekseintrag, kein Repositorium gefunden |
| N+P Informationssysteme: *Durchgängige digitale Prozesse im Holzfertigbau* (Haas Fertigbau Haus-Konfigurator) | G (Pressemitteilung) | 2025 | Konfigurator mit Revit-Add-in zur automatischen Modellgenerierung, Übergabe an Fertigung, ACC/BIM 360 | FF1 2 · FF5 1 · FF2 1. Stand der Praxis beim niederbayerischen Wettbewerber: proprietäre Kette ohne IFC. Qualität C | [V] Pressemitteilung news-research.net |
| Regnauer Fertigbau: *Qualität* (Unternehmensseite) | G (Herstellerangabe) | abgerufen 2026 | 2–4 wissenschaftliche Arbeiten pro Jahr mit der TH Rosenheim; Mitglied im Fachbeirat Holztechnik; Austausch mit ift, DGfH, Holzforschung Austria, Holzforschung TUM | FF5 1. Kontext für das Fallbeispiel 3.5 und den Feldzugang | [V] regnauer.at/hausbau/qualitaet |
| Bayerische Staatszeitung: *Steuererleichterungen und weniger Bürokratie* (BDF-Tour Baufritz und Regnauer) | G (Presse) | o. J. | Baufritz-Dämmstoff mit FH Rosenheim, TUM (Holzforschung), MPA NRW, FIW München, Fraunhofer entwickelt; Regnauer Barrierefrei-Paket mit Robotik | FF6 1. Kontext Herstellerkooperationen | [U] Erscheinungsdatum nicht angegeben |
| TH Rosenheim, Fakultät HTB: *Jahresbericht 2023/2024* | G (Bericht) | 2024 | Promotionszentrum „Advanced Building Technologies“ (Vorfertigung, Digitalisierung, Automatisierung), neues Labor für Digitales Planen und Bauen | FF5 1. Institutioneller Kontext und Betreuungsweg | [V] th-rosenheim.de (PDF) |
| *Hinweis ohne Primärquelle:* ift / TH Rosenheim / HFT Stuttgart, Projekt zum Beitrag von Rollläden und Läden zum nächtlichen Schallschutz | G | 2026 | Bis 16 dB Verbesserung; Bauteilkatalog, Integration in DIN 4109 angestrebt | FF6 1 · FF2 1 | [U] nur LinkedIn-Beitrag; nicht zitieren, nicht in der Bib-Datei |

**Dubletten (nicht neu aufgenommen):** Q091 `tum2023bimwood`, Q092 `geier2022bimwood` (HSLU/BFH), Q233 `geier2018analysemodell` (Diss. TUM), Q234 `chateauvieux2023bim` (Diss. TUM, heute TH Rosenheim), Q232 `linner2013automated`, Q083 `bock2015robot`, Q081 `knippers2021integrative` (IntCDC Stuttgart), Q235/Q236 (Menges-Gruppe), Q259 `timbim2024` (Holzforschung Austria), Q204 `dataholz`, Q183 `din4109-33`, Q206 `regnauerBLB2024`.

### Kontaktmöglichkeiten und Ansprechpartner-Institutionen (nur Institutionen)

| Institution | Einheit | Anknüpfung an die Arbeit |
|---|---|---|
| TH Rosenheim, Fakultät für Holztechnik und Bau | Labor für Digitales Planen und Bauen (BIM, digitale Zwillinge) | IFC/IDS-Prüfung, Validierung FF1 |
| TH Rosenheim | Forschungsschwerpunkt Akustik im Bauwesen | Schallschutzregeln (DIN 4109) für FF2/FF6, Gebäudetypen 9a |
| TH Rosenheim | Robotik und Automatisierung im Holzbau (RoWaPla-Zelle bleibt an der Hochschule) | Ableitung Maschinendaten (Kap. 12/FF1), Experteninterviews Werk |
| TH Rosenheim | Promotionszentrum „Advanced Building Technologies“ | Institutioneller Rahmen für eine kooperative Promotion |
| TH Rosenheim | Studiengang Holzbau und Ausbau, Praxispartner-Netzwerk (Regnauer ist Verbundstudium-Partner) | Feldzugang, Abschlussarbeiten als Teilstudien |
| ift Rosenheim | Abteilung F+E, Labor Bauakustik, Montage (Montageplaner) | Fenstereinbau-Regeln, Bemusterung Fenster, Schallschutzkennwerte |
| TU München | Lehrstuhl für Architektur und Holzbau; Lehrstuhl für Architekturinformatik; Holzforschung München | BIMwood, leanWOOD, Holz&BIM; Holzbaukompetenz in Leistungsbildern (FF4) |
| Hochschule München, Fakultät für Architektur | Projekt Digital Craft | Vergleichsarbeit „parametrisches Haus → Fertigung“ |
| TH Augsburg | Digital Timber Construction (DTC) | Statikschnittstelle aus Fertigungsdaten |
| Universität Stuttgart | ICD / Exzellenzcluster IntCDC | Mensch-Roboter-Kooperation in der Vorfertigung |
| Berner Fachhochschule, Biel | Institut für digitale Bau- und Holzwirtschaft (IDBH) | Produktdaten (ETIM), Schnittstellen |
| Hochschule Luzern | Kompetenzzentrum Typologie & Planung in Architektur (CCTP) | BIMwood Schweiz, Pull-Planung |
| TU Graz | Institut für Architekturtechnologie; holz.bau forschungs gmbh | Sys.Wood-Befunde zu Datenaustausch |
| Fraunhofer IPA / Fraunhofer WKI | Referenzprojekt DesignChain / DiKieHo | Regelbasierte Wandelement-Generierung |
| buildingSMART Deutschland | Fachgruppe „BIM und Holzbau“ | IFC/IDS-Anwendungsfall Holzrahmenbau, Rückkopplung in Standards |
| Bundesverband Deutscher Fertigbau (BDF) | Verband der Hersteller | Zugang zu weiteren Herstellern für Interviews |
| BBSR, Referat WB 3 „Forschung und Innovation im Bauwesen“ | Zukunft Bau Forschungsförderung | Fördermöglichkeit für Demonstrator oder Nutzerstudie |
| Fachagentur Nachwachsende Rohstoffe (FNR) | Förderprogramm Nachwachsende Rohstoffe | Fördergeber von BIMwood, Holz&BIM, leanWOOD, TSI |

---

## B Deutschsprachige Architektur- und Umweltpsychologie, Wohnforschung

| Quelle | Typ | Jahr | Inhalt kurz | Passung FF1–FF6 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Flade: *Architektur – psychologisch betrachtet*, Huber, Bern (unter Mitarbeit von Dieckmann und Röhrbein), ISBN 978-3-456-84612-5 | W (Lehrbuch) | 2008 | Deutschsprachiges Standardwerk der Architekturpsychologie | FF6 2 · FF2 1. Grundlage für die Wirkfaktoren von R5 in 9b.2 | [V] mehrere Literaturverzeichnisse, Berliner Mieterverein 2009; ISBN nur über Wikipedia [U] |
| Flade: *Wohnen psychologisch betrachtet*, 2. Aufl., Huber, ISBN 978-3-456-84304-9 | W (Lehrbuch) | 2006 | Wohnbedürfnisse, Wohnzufriedenheit, Privatheit, Dichte, Lärm, Wohnen von Familien und Älteren, nutzerorientierte Wohnbauplanung; Feng Shui als Trendthema | FF6 2 · FF2 1. Deutschsprachige Primärquelle für Wohnbedürfnisse; Brücke zu Kulturprofilen (9b.5) | [V] Deutsche Digitale Bibliothek |
| Flade: *Kompendium der Architekturpsychologie*, Springer, DOI 10.1007/978-3-658-31338-8 | W (Lehrbuch) | 2020 | Aktuelle Gesamtdarstellung, u. a. Zielgruppen. Engl. Ausgabe 2021, DOI 10.1007/978-3-658-34917-2 | FF6 2. Aktuellster deutschsprachiger Überblick; Zitat für 9b.2 | [V] Crossref |
| Flade: *Wohnen in der individualisierten Gesellschaft*, Springer, DOI 10.1007/978-3-658-29836-4 | W (Monografie) | 2020 | Psychologie des Wohnens unter Individualisierung | FF6 2. Begründet Konfigurierbarkeit statt Standardgrundriss | [V] Crossref |
| Hellbrück & Kals: *Umweltpsychologie*, VS, DOI 10.1007/978-3-531-93246-0 | W (Lehrbuch) | 2012 | Grundlagen; Kapitel „Professionalisierung, Gestaltung und Evaluation“ | FF6 1 · FF5 1. Basis für Lärm, Crowding, Evaluation | [V] Crossref |
| Hellbrück & Fischer: *Umweltpsychologie. Ein Lehrbuch*, Hogrefe, ISBN 3-8017-0621-4 | W (Lehrbuch) | 1999 | Vorgängerwerk | FF6 1. Nur historisch; 2012 bevorzugen | [V] Bibliotheksbestand CUREM (UZH) |
| Walden: *Architekturpsychologie: Schule, Hochschule und Bürogebäude der Zukunft*, Pabst, ISBN 978-3-89967-426-2 | W (Monografie, Habil.-Basis) | 2008 | Umweltkontrolle als zentrales Kriterium; Koblenzer Architekturfragebogen; Building Performance Evaluation | FF6 1 · FF5 1. Keine Wohnbauten, aber übertragbares Konstrukt „Umweltkontrolle“ und Fragebogenmethodik | [V] Verlags- und E-Book-Seite, Publikationsliste Uni Koblenz |
| Dieckmann, Flade, Schuemer, Ströhlein & Walden: *Psychologie und gebaute Umwelt*, Institut Wohnen und Umwelt, Darmstadt, ISBN 3-932074-23-8 | W (Sammelband) | 1998 | Konzepte, Methoden, Anwendungsbeispiele. Einzige gefundene Schuemer-Quelle | FF6 1 · FF5 1. Methodische Frühquelle | [U] nur über die Publikationsliste R. Walden, kein Katalogabgleich |
| Häußermann & Siebel: *Soziologie des Wohnens*, Juventa, ISBN 3-7799-0395-4 (2. Aufl. 2000) | W (Lehrbuch) | 1996 | Wandel und Ausdifferenzierung des Wohnens, Trennung von Arbeit und Wohnen | FF6 1. Soziologischer Rahmen für veränderte Raumprogramme | [V] Deutsche Digitale Bibliothek, dandelon-Inhaltsverzeichnis |
| Harlander (Hrsg.): *Villa und Eigenheim. Suburbaner Städtebau in Deutschland*, DVA / Wüstenrot Stiftung, ISBN 3-421-03299-8 | W (Sammelband) | 2001 | Geschichte des Eigenheims in Deutschland | FF6 1. Kontext 3.3 und 1.1 | [V] Wüstenrot Stiftung, hbz (lobid) |
| Schneider & Spellerberg: *Lebensstile, Wohnbedürfnisse und räumliche Mobilität*, DOI 10.1007/978-3-322-97430-3 | W (Monografie) | 1999 | Neun Lebensstiltypen und ihre Wohnorientierungen (Wüstenrot-Studie) | FF6 2. Nutzerprofile als Voreinstellungen für R5-Empfehlungen | [V] Crossref |
| Eckardt & Meier (Hrsg.): *Handbuch Wohnsoziologie*, Springer VS, DOI 10.1007/978-3-658-24724-9 | W (Handbuch) | 2021 | Aktueller Stand der Wohnsoziologie, u. a. Spellerberg: Gemeinschaftliches Wohnen | FF6 1. Überblickszitat | [V] Crossref |
| Wegener, Fedkenheuer, Drexler & Schupp: *Funktionswandel des Wohnens*, BBSR-Online-Publikation 15/2024, DOI 10.58007/2s3m-6h29 | G (Ressortforschung) | 2024 | Repräsentative Befragung zu Wohnpraxis und Wohnwünschen nach Corona; Homeoffice von 84 % genutzt (Basis: alle, die zu Hause arbeiten können), nur die Hälfte hält die Wohnung für geeignet | FF6 3 · FF2 2. Liefert direkt übernehmbare R5-Regeln (Arbeitsplatz, Rückzugsraum, Tageslicht, Akustik) mit deutscher Datenbasis | [V] BBSR-Seite |
| Neumann, Spellerberg & Eichholz: *Veränderungen beim Wohnen und von Standortpräferenzen durch Homeoffice in der Covid-19-Pandemie?*, RuR 80(4), 434–450, DOI 10.14512/rur.133 | W (Artikel) | 2022 | Homeoffice-Befragung 2020 (vor allem Rheinland-Pfalz); Umzugswunsch vor allem bei beengtem Wohnen; „Zimmer mehr“ als Arbeitszimmer | FF6 2. Begutachtete deutsche Homeoffice-Studie; ergänzt Xiao 2021 (Q351) | [V] Crossref |
| Eisele & Albus: *Standards im Wohnungsbau als Kostenfaktor*, BBSR-Online 86/2024, DOI 10.58007/jwz9-ze04 | G (Ressortforschung) | 2024 | 2.408 Mieterhaushalte; Ausstattungsmerkmale mit Zahlungsbereitschaft, Kategorien Basis / Potenzial / Bonus / Nische | FF6 2. Raster für Bemusterungs-Voreinstellungen; Mieter, daher nur mit Anpassung übertragbar | [V] BBSR-Seite |
| Ammann & Müther: *Wohneigentumsbildung und Wohnflächenverbrauch*, BBSR-Analysen KOMPAKT 14/2022, DOI 10.58007/cqa5-jm26 | G | 2022 | Wohnwunsch Eigenheim, Wohnflächennachfrage | FF6 1. Kontext 3.3 | [V] BBSR-Seite |
| Ammann: *Wohneigentumsbildung – Faktencheck 2.0*, BBSR-Analysen KOMPAKT 08/2023, DOI 10.58007/cyqq-1a27 | G | 2023 | Erwerb 2018–2021: 45 % freistehende EFH, 21 % Neubau, Familien dominieren | FF6 1. Marktkontext Zielgruppe Familie | [V] BBSR-Seite |
| Kremer-Preiß, Mehnert & Stolarz (KDA): *Wohnen im Alter*, BMVBS-Forschungen 147, ISBN 978-3-87994-479-8 | G (Ressortforschung) | 2011 | 1.000 Seniorenhaushalte; Barrieren vor allem im Bad; Bedarf an altersgerechten Wohnungen | FF6 2 · FF2 1. Empfehlungen für Barrierearmut im EFH (Bad, Schwellen) über die Pflicht hinaus | [V] BBSR-Seite |
| Dürr, Heitkötter, Kuhn, Lien & Abraham: *Familien in gemeinschaftlichen Wohnformen*, BBSR-Online-Publikation (lt. DJI 5/2021) | G | 2021 | 400 Haushalte, 12 Fallstudien; Optionsräume, Anpassbarkeit über Lebensphasen | FF6 1. Anpassbarkeit als Entwurfsziel | [U] Heftnummer widersprüchlich: BBSR-Online 05/2021 ist laut BBSR ein anderer Titel (Leichtbeton-3D-Druck) |
| Wüstenrot Stiftung (Hrsg.), Dürr & Kuhn: *Wohnoptionen. gemeinschaftsorientiert – produktiv – adaptiv*, ISBN 978-3-96075-021-5 | G (Stiftungsstudie) | 2022 | Zwölf Projekte, Verbindung von Wohnen und Arbeiten, Anpassbarkeit | FF6 1 | [V] wuestenrot-stiftung.de |
| Wüstenrot Stiftung (Hrsg.): *Das zukunftsfähige Einfamilienhaus?*, ISBN 978-3-96075-026-0 | G (Dokumentation) | 2023 | 13. Gestaltungspreis, 15 prämierte EFH aus DE, AT, CH | FF6 1. Qualitätsbeispiele für Hausmodelle | [V] wuestenrot-stiftung.de |
| Schader-Stiftung (Hrsg.): *wohn:wandel. Szenarien, Prognosen, Optionen zur Zukunft des Wohnens*, ISBN 3-932736-07-9 | G (Tagungsband) | 2001 | Wandel von Funktionen und Formen des Wohnens | FF6 1. Kontext | [V] schader-stiftung.de |
| Schader-Stiftung / Heinze et al.: *Neue Wohnung auch im Alter*, ISBN 3-932736-00-1 | G (Forschungsbericht) | 1997 | Umzugswünsche Älterer, Ansprüche an altersgerechte Wohnungen | FF6 1. Historisch; 2011 bevorzugen | [V] Schader-PDF (Impressum) |
| LBS Research / LBS West: *Corona: Neue Wohnwünsche nach Pandemie-Erfahrung* (Pressemitteilung) | G (Presse) | 2020 | Befragung 20- bis 45-Jähriger; 60 % haben das Zuhause umgestaltet, jeder Fünfte einen Heimarbeitsplatz eingerichtet | FF6 1. Nur Pressemitteilung, kein Studienbericht; Qualität C | [V] presseportal.de |
| Verband der Sparda-Banken (IW Köln, IfD Allensbach): *Studie Wohnen in Deutschland 2025* | G | 2025 | Allensbach-Umfrage n = 1.234; Wohneigentumswunsch, Zufriedenheit | FF6 1. Kontext | [V] PDF des Herausgebers |

**Dubletten:** Q305 `richter2016architekturpsychologie` (Pabst, 4. Aufl.; eine Aufl. 2019 nicht gefunden), Q308 `rambow2000expertenlaien`, Q309 `vollmer2010erkrankung`, Q356 `faller2002wohngrundriss` (Wüstenrot), Q349 `oswald2007housing` (Ältere), Q350/Q351 (Covid, Homeoffice international), Q357 `bwo2015wbs`.

---

## C Methodische Standards

| Quelle | Typ | Jahr | Inhalt kurz | Passung FF1–FF6 (0–3) mit Begründung | Status |
|---|---|---|---|---|---|
| Kitchenham & Charters: *Guidelines for performing Systematic Literature Reviews in Software Engineering*, EBSE-2007-01, Vers. 2.3, Keele/Durham | G (Tech. Report) | 2007 | Planung, Durchführung und Bericht eines SLR; Protokoll, Qualitätschecklisten | Methodisch für FF1–FF6 je 1 (Recherche 2a); trägt keine Inhaltsaussage | [V] Original-PDF (9. Juli 2007) und EBSE-Bibliographie Durham; kein DOI |
| Wohlin: *Guidelines for snowballing in systematic literature studies…*, EASE 2014, DOI 10.1145/2601248.2601268 | W (Konferenz) | 2014 | Vorwärts- und Rückwärts-Schneeball, Abbruchkriterium | Methodisch FF1–FF6 je 1 (2a.3 Nr. 3) | [V] Crossref |
| Page et al.: *The PRISMA 2020 statement*, BMJ 372:n71, DOI 10.1136/bmj.n71 | W (Artikel) | 2021 | Berichtsstandard, Flussdiagramm | Methodisch FF1–FF6 je 1 (2a.6 Nr. 5) | [V] Crossref |
| Cohen: *A Coefficient of Agreement for Nominal Scales*, EPM 20(1), 37–46, DOI 10.1177/001316446002000104 | W (Artikel) | 1960 | Cohens κ | FF5 1, methodisch für 2a.7 (Zweitbewertung Kernbestand) | [V] Crossref |
| Landis & Koch: *The Measurement of Observer Agreement for Categorical Data*, Biometrics 33(1), 159–174, DOI 10.2307/2529310 | W (Artikel) | 1977 | Interpretationsstufen für κ | FF5 1, ergänzend zu Cohen | [V] Crossref |
| Sonnenberg & vom Brocke: *Evaluations in the Science of the Artificial*, DESRIST 2012, LNCS 7286, 381–397, DOI 10.1007/978-3-642-29863-9_28 | W (Konferenz) | 2012 | Ex-ante- und Ex-post-Evaluation in vier Aktivitäten (Eval 1–4) | FF5 3. Strukturiert die Evaluation in Kap. 20 zusammen mit FEDS (Q156) | [V] Crossref |
| Mayring: *Qualitative Inhaltsanalyse. Grundlagen und Techniken*, 13. Aufl., Beltz, ISBN 978-3-407-25898-4 | W (Methodenbuch) | 2022 | Zusammenfassung, Explikation, Strukturierung; QCAmap | FF5 3 · FF4 1. Auswertung der Experteninterviews (6–10 Personen) | [V] Beltz-Verlagsseite, SLUB-Katalog |
| Kuckartz & Rädiker: *Qualitative Inhaltsanalyse. Methoden, Praxis, Umsetzung mit Software und künstlicher Intelligenz*, 6. Aufl., Beltz Juventa, ISBN 978-3-7799-7912-8 | W (Methodenbuch) | 2024 | Inhaltlich strukturierende, evaluative, typenbildende QIA; neu: KI im Analyseprozess | FF5 3. Alternative zu Mayring; das KI-Kapitel ist für die Offenlegung der LLM-Nutzung relevant. 5. Aufl. 2022: ISBN 978-3-7799-6231-1 | [V] Beltz-Verlagsseite, Fachportal Pädagogik (5. Aufl.) |
| Bogner, Littig & Menz: *Interviews mit Experten. Eine praxisorientierte Einführung*, Springer VS, DOI 10.1007/978-3-531-19416-5 | W (Methodenbuch) | 2014 | Expertenbegriff, Leitfaden, Auswertung | FF5 3 · FF4 1. Design der Experteninterviews | [V] Crossref |
| Gläser & Laudel: *Experteninterviews und qualitative Inhaltsanalyse*, 4. Aufl., VS, DOI 10.1007/978-3-531-91538-8 | W (Methodenbuch) | 2010 | Rekonstruktive Untersuchung, Extraktion | FF5 2. Ergänzend zu Bogner et al. | [V] Crossref |
| Brooke: *SUS: A „quick and dirty“ usability scale*, in: Jordan et al. (Hrsg.), *Usability Evaluation in Industry*, DOI 10.1201/9781498710411-35 | W (Buchkapitel) | 1996 | System Usability Scale, zehn Items | FF5 3 · FF3 2. Zufriedenheitsmaß der Nutzerstudie, auch für die Sprachschnittstelle | [V] Crossref (Seiten 207–212 in der CRC-Neuausgabe) |
| Bangor, Kortum & Miller: *An Empirical Evaluation of the System Usability Scale*, IJHCI, DOI 10.1080/10447310802205776 | W (Artikel) | 2008 | Normwerte, Adjektivskala für SUS | FF5 2. Interpretation der SUS-Werte | [V] Crossref |
| Hart & Staveland: *Development of NASA-TLX*, in: *Human Mental Workload* (Advances in Psychology 52), 139–183, DOI 10.1016/S0166-4115(08)62386-9 | W (Buchkapitel) | 1988 | Sechs Dimensionen subjektiver Beanspruchung | FF5 3 · FF3 1. Beanspruchung der Laien beim Entwerfen | [V] Crossref; Herausgeber (Hancock & Meshkati) nach Standardzitation, von Crossref nicht angezeigt |
| Hart: *NASA-Task Load Index (NASA-TLX); 20 Years Later*, Proc. HFES 50(9), DOI 10.1177/154193120605000909 | W (Konferenz) | 2006 | Übersicht über 550 Studien, Raw TLX | FF5 2. Begründung für Raw TLX ohne Gewichtung | [V] Crossref |
| ISO 9241-11:2018 *Usability: Definitions and concepts* (DIN EN ISO 9241-11:2018-11) | N | 2018 | Gebrauchstauglichkeit = Effektivität, Effizienz, Zufriedenheit im Nutzungskontext | FF5 3. Operationalisiert Aufgabenerfolg, Zeit und Zufriedenheit der Nutzerstudie | [V] iso.org (2023 bestätigt) |
| ISO 9241-110:2020 *Interaction principles* (DIN EN ISO 9241-110:2020-10) | N | 2020 | Sieben Interaktionsprinzipien, u. a. Steuerbarkeit, Robustheit gegen Benutzungsfehler, Nutzerbindung | FF3 2 · FF5 2. Prüfkriterien für Dialog, Rückfragen und Ablehnung mit Begründung (10.4, 9.5) | [V] iso.org (2025 bestätigt) |

**Dubletten:** Q152 `hevner2004design`, Q153 `peffers2007design`, Q154 `gregor2013positioning`, Q156 `venable2016feds`.

---

## Was nicht gefunden wurde

- **GEPRIS (DFG):** Direkter Zugriff war gesperrt, daher nur Suche über den Exa-Index. Kein DFG-Projekt zu Fertighaus, Hauskonfigurator oder Holzbau-BIM gefunden. Treffer sind Grundlagenprojekte (z. B. 436451184 „Additive robotische Fabrikationstechniken für den Holzbau“, 514175549 CT-Labor HNE Eberswalde) ohne Bezug zu FF1–FF6. Eine Nachsuche direkt in GEPRIS ist vor der Abgabe nötig.
- **DNB-Dissertationsdatenbank:** nicht erreichbar (403). Dissertationen wurden nur über mediaTUM gefunden (Prochiner 2006, neu; Geier 2018, Châteauvieux 2023, Linner 2013 als Dubletten). Keine Dissertation zu kundengesteuertem Fertighausentwurf mit Regelprüfung gefunden. Das stützt die Lückenbehauptung, ist aber ohne DNB-Abfrage nicht abschließend.
- **TH Rosenheim:**
  - Kein Projekt zu Konfigurator, Kundenentwurf, IFC-Kette bis zum Bauantrag oder Sprachschnittstelle gefunden.
  - Abschlussarbeiten mit Regnauer sind laut Hersteller vorhanden, aber nicht öffentlich gelistet.
  - Eine Anfrage bei der Fakultät bzw. dem Promotionszentrum ist der einzige Weg.
- **Hersteller:**
  - Für Huf Haus, WeberHaus, SchwörerHaus und Bien-Zenker keine dokumentierte Hochschulkooperation zu Digitalisierung gefunden, nur BDF- und FertighausWelt-Pressetexte.
  - Haas und Baufritz nur über Presse bzw. Anbietertexte, nicht über Forschungsberichte.
- **ift Rosenheim:**
  - Prüfberichte sind auftraggebergebunden und nicht öffentlich.
  - Kein ift-Forschungsbericht zu BIM- oder Produktdaten für Fenster gefunden.
  - Beim Flachdach-Bericht fehlt das Jahr; er ist deshalb nicht aufgenommen.
- **HNE Eberswalde:** kein Projekt zu Digitalisierung oder Vorfertigung im Holzbau; nur Material- und Alterungsforschung (WAVE 2025–2027, CT-Labor).
- **Fraunhofer WKI:** nur Material- und Wertschöpfungsprojekte (DiKieHo, SafeTeCC). Das inhaltlich passende Projekt (DesignChain) stammt vom Fraunhofer IPA.
- **IRB / Zukunft Bau:** Suche nach „Fertighaus“ ergab keinen eigenen Treffer. Relevant sind Variowohnen Kassel, Digital Craft, MRK und die ift-Projekte.
- **LBS-Wohnwünsche-Studie:** kein Studienbericht, nur Pressemitteilungen 2020. Eine LBS-Kurzstudie des Verbands der Privaten Bausparkassen (bausparkassen.de) wurde nicht geprüft.
- **Schuemer:** keine eigene Monografie gefunden, nur Mitautorschaft 1998.
- **Richter (Hrsg.):** eine Auflage nach 2016 nicht gefunden (wie im Master vermerkt).
- **Offene [U]-Punkte:**
  - ISBN Flade 2008 (nur Wikipedia)
  - Heftnummer Dürr et al. 2021
  - Jahr IGF 18725 N
  - Jahr DesignChain
  - Datum Bayerische Staatszeitung
  - Repositorium Kuhl 2023
  - Katalogabgleich Dieckmann et al. 1998

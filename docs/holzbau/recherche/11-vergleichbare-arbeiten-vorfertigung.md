# Recherche 11: Vergleichbare Arbeiten zu Vorfertigung, Plattformen, Konfiguration und Design Automation

Stand: 27.09.2026. Schwerpunkt: industrialisierter Hausbau, Produktplattformen, Konfiguration, Mass Customization, Design Automation. Ziel: Gold (übernehmbare Methoden, Datenmodelle, Regeln, Evaluationsdesigns) und Warnungen für die Arbeit „Sprachgesteuerter, regelbasierter Entwurf von Holzrahmenbau-Fertighäusern durch Laien, mit IFC 4.3 bis Ständer und Schraube, IDS-Prüfung, Bauantrag Bayern und BTLx/WUP“.

**Kennzeichnung:** **[V]** = Autor, Jahr, Titel und Venue an einer Primärquelle geprüft (Verlags-, Proceedings-, Repositorien- oder Institutsseite). **[U]** = Existenz belegt, aber einzelne Metadaten (Seiten, DOI, Band) nicht geprüft. **[G]** = graue Literatur (Bericht, Fallstudie, Kommentar, Projektseite).

**Verifikationsweg:** Die Crossref-, OpenAlex-, doi.org- und mediaTUM-Endpunkte waren in dieser Sitzung vom Egress-Proxy gesperrt. Deshalb wurden die Metadaten über die Exa-Suche an den Primärseiten geprüft, etwa ScienceDirect, Taylor & Francis, Emerald, ASCE Library, Cambridge Core, ITcon, CumInCAD, IOS Press, DiVA, der mediaTUM-Katalogseite, Pure/Orbit und PUMA Stuttgart. In der `.bib` steht zu jedem Eintrag der Verifikationsweg. Vor der Abgabe sollten alle DOIs noch einmal über Crossref gegengeprüft werden.

**Abgleich mit Vorbestand:** 29 einschlägige Arbeiten stehen schon in `lit-B-vorfertigung-ki.bib`, zum Beispiel `jensen2012configuration`, `wikberg2014design`, `jansson2014platform`, `duarte2005towards`, `barlow2003choice` und `tum2023bimwood`. Sie werden hier mit ihrem Key zitiert und **nicht** noch einmal angelegt, damit keine Key-Dubletten entstehen. `lit-D-vergleich-vorfertigung.bib` enthält nur neue Einträge.

---

## Ergebnis in 5 Punkten

1. **Keine gefundene Arbeit schließt die Kette „Laie → formalisierter Herstellerregelraum → offenes Modell bis Ständer/Schraube → Normprüfung → Bauantrag → Maschinendaten“.** Am nächsten kommen drei Arbeiten, denen jeweils zentrale Glieder fehlen. Shafiee et al. (2025) führen einen Laien-Konfigurator für eine Garage bis zu Pre-cut-Produktionsdaten, aber ohne IFC und ohne Bauantrag. Benrós & Duarte (2009) verbinden eine Grammatik mit einem Vorfertigungssystem, aber ohne offenes Datenmodell und ohne Maschinendaten. Alwisy et al. (2019) erzeugen aus 2D-CAD automatisch Werkstattpläne für Holzrahmen-Paneele, dort entwirft aber kein Laie. Diese Lücke ist die Neuheit der Arbeit.
2. **Das wichtigste methodische Gold ist die Trennung von Regeln und Suche.** Duarte (2001, 2005) trennt Formgrammatik, Beschreibungsgrammatik (Regelwerk der Bauordnung) und Heuristiken. Er sucht **bewusst deterministisch**, damit Antwortzeiten für Web-Laien möglich werden. Khalili-Araghi & Kolarevic (2016) unterscheiden Constraint-*Solving* (generativ, der Kunde hat keinen Einfluss) von Constraint-*Checking* (der Kunde wirkt mit, das System prüft). Beides begründet direkt das deterministische, sprachgesteuerte Design mit einem Prüfkern.
3. **Für Plattformen gibt es reife, übernehmbare Modellierungsmethoden.** Dazu gehören die Vierfachsicht Kunde/Engineering/Produktion/Montage (Malmgren et al. 2010) und die Indizes GVI/CI zur Frage, was standardisiert und was variabel wird (Veenstra et al. 2006). Hinzu kommen Popovics Kombination aus Design Platform, IDM und Exchange-Requirement-Matrix mit den Status G/M/T/**R**(euse) (Popovic et al. 2021) und die „Product Architecture Model“-Erweiterung des IDM für Vorfertigung (Ramaji et al. 2017). Diese Artefakte lassen sich fast 1:1 auf IDS-Spezifikationen je Prozessschritt abbilden.
4. **Die Laien-Evaluation ist in der Literatur dünn, es gibt aber drei kopierbare Designs.** Kwieciński & Duarte (2019) und Kwieciński & Słyk (2023) testen HOPLA mit 15-Minuten-Aufgabe, Modus „Modifizieren“ gegen „von Null“ und Likert-Skala, auf zwei Kontinenten mit Mann-Whitney-Test. Swanenburg (2016) vergleicht randomisiert „Starting Solutions“, „Attribute-by-Attribute“ und eine Standard-Kontrollgruppe mit Preference Fit und Kaufwahrscheinlichkeit. Puusepp et al. (2017) messen mit Web-Analytics und n=133 an einem Live-Konfigurator. Befund quer über diese Studien: Laien wollen **Grundriss und Kosten** steuern, nicht Oberflächen.
5. **Die Warnungen sind konsistent.** (a) Kunden- und Vertriebsdruck erodiert den Regelraum, wenn „außerhalb der Plattform“ verkauft wird (Lennartsson et al. 2022; Popovic et al. 2019). (b) Konfigurator, CAD und ERP sind in der Praxis nicht durchgängig verbunden (Popovic et al. 2019). (c) IFC-Implementierungslücken bei Mehrschichtaufbauten zwingen zu Workarounds (TIMBIM). Stuttgart wich deshalb auf BHoM statt IFC aus (Orozco et al. 2023). (d) Katerra zeigt, dass Vertikalintegration ohne stabile Plattform scheitert. (e) KBE-Werkzeuge sind nur so gut wie ihre Pflege, und Standardisierung ist Vorbedingung, nicht Ergebnis (Sandberg et al. 2008).

---

## Vergleichsmatrix

Legende: ● ja, ◐ teilweise, ○ nein. „Laie entwirft“ = Endkunde ohne Planungsausbildung bedient das System selbst.

| Arbeit | Jahr | Typ | Ansatz | Holzbau? | Laie entwirft? | Regeln formalisiert? | IFC/offener Standard? | bis Fertigung? | Evaluation | Code/Daten |
|---|---|---|---|---|---|---|---|---|---|---|
| Duarte, MIT-Diss. [V] | 2001 | Diss. | Discursive Grammar (Form-, Beschreibungsgrammatik, Heuristik), deterministische Suche, Web-Prototyp | ○ (Mauerwerk) | ◐ Web-Prototyp | ● | ○ | ○ | Experimente mit Entwerfern; „Siza-Test“ | ○ |
| Duarte, AutCon [V] | 2005 | Journal | Designing Grammar als Teil der Discursive Grammar | ○ | ◐ | ● | ○ | ○ | Beispielableitungen | ○ |
| `duarte2005towards` (lit-B) | 2005 | Journal | Formgrammatik Malagueira (35 Häuser) | ○ | ○ | ● | ○ | ○ | Rekonstruktion bestehender Häuser | ○ |
| Benrós & Duarte [V] | 2009 | Journal | Grammatik plus Vorfertigungssystem als integriertes MC-System | ◐ | ◐ | ● | ○ | ◐ konzeptionell | Fallbeispiel | ○ |
| Sass, Wood Frame Grammar [V] | 2006 | Journal | Grammatik, die CNC-Holzbauteile erzeugt | ● (Sperrholz) | ○ | ● | ○ | ● CNC | Prototypbau | ○ |
| Knight & Sass [V] | 2010 | Journal | Visuell-physische Grammatiken, CNC-Steckbausysteme | ● | ○ | ● | ○ | ● | Pilotstudien | ○ |
| Kwieciński et al. [V] | 2016 | Konferenz | Formgrammatik mit Leichtbau-Holzrahmenregeln (60-cm-Raster, 6 m Spannweite), Grammatik gegen GA | ● | ◐ geplant | ● | ○ | ○ | Laufzeitvergleich | ○ |
| Kwieciński & Duarte [V] | 2019 | Konferenz | HOPLA, Nutzertests mit Laien (USA/PL) | ○ | ● | ● | ○ | ○ | 15-min-Aufgabe, Likert, Mann-Whitney, n=40 | ○ |
| Kwieciński & Słyk [V] | 2023 | Journal | Interaktives generatives System für partizipativen Hausentwurf | ○ | ● | ● | ○ | ○ | Usability-Studien E01–E03 | ○ |
| Khalili-Araghi & Kolarevic [V] | 2016 | Journal | Constraint-basierte dimensionale Anpassung in Revit (PDS/UCS) | ◐ Fertighaus CA | ● | ● | ◐ Revit | ○ | Diss.: formativ/summativ, Experten gegen Laien | ○ |
| Puusepp et al. [V] | 2017 | Konferenz | Web-Hauskonfigurator mit Echtzeitkosten | ● (EE-Fertighaus) | ● | ◐ | ◐ BIM-Plugins | ○ | Web-Analytics, n=133 | ○ |
| Swanenburg (MSc Twente) [V] | 2016 | MSc | Online-Experiment Konfiguratordesign (CvSS gegen AbA) | ○ | ● | ○ | ○ | ○ | Randomisiert mit Kontrollgruppe | ○ |
| Shafiee et al. [V] | 2025 | Journal | Garagenkonfigurator (Grasshopper/ShapeDiver) bis Pre-cut-Produktionsdaten, CO₂, Kosten | ● | ● | ● | ○ | ● | DSR-Fallstudie, Firmenbefragung | ○ proprietär |
| Piroozfar et al. [V] | 2019 | Journal | BIM als Konfigurationsplattform für Fassaden | ○ | ○ | ◐ | ◐ Revit | ◐ | Universal-Fallmodell | ○ |
| Farr et al. [V] | 2014 | Journal | BIM als generischer Konfigurator | ○ | ◐ | ◐ | ◐ | ○ | Demonstrator | ○ |
| `jensen2012configuration` (lit-B) | 2012 | Journal | Parametrisierung von Bauteilen, Raumelemente | ● | ○ | ● | ○ | ◐ | Fallstudie | ○ |
| Malmgren et al. [V] | 2010 | Journal | Produktmodell mit 4 Sichten (Kunde, Engineering, Produktion, Montage) | ● | ○ | ◐ | ○ | ◐ | Fallstudie | ○ |
| Sandberg et al. [V] | 2008 | Journal | KBE-Demonstrator Treppe: Verkäufer-Tool für Kosten und Fertigbarkeit | ● | ◐ mit Verkäufer | ● | ○ | ○ | Workshop, Demonstrator | ○ |
| `wikberg2014design` (lit-B) | 2014 | Journal | Architektonische Objekte verbinden Kundenanforderung und Systemfähigkeit | ● | ○ | ◐ | ○ | ○ | Fallstudie | ○ |
| Veenstra et al. [V] | 2006 | Journal | Plattform-Methodik mit GVI/CI (Design for Variety), räumliche Klassifikation | ○ | ○ | ◐ | ○ | ○ | 1 Jahr Fallstudie, 31 Sitzungen | ○ |
| Jansson et al. [V] | 2018 | Journal | Architektenarbeit unter Plattform-Constraints | ● | ○ | ○ | ○ | ○ | Interviews | ○ |
| Popovic et al. [V] | 2021 | Journal | Design Platform, IDM und ERS für flexible Raumelemente | ● | ○ | ● | ◐ IDM | ◐ | Fallstudie Einfamilienhaus | ○ |
| Popovic, Diss. Jönköping [V] | 2020 | Diss. | Plattformen im Einfamilien-Fertighausbau (DRM) | ● | ○ | ● | ◐ | ◐ | Mehrfachfallstudien | ○ |
| Popovic et al., MOC [U] | 2019 | Konferenz | Smart Manufacturing und Plattformen, 14 Interviews | ● | ○ | ○ | ○ | ◐ | Interviews | ○ |
| Lennartsson et al. [V] | 2022 | Konferenz | Technische Plattform in 2 Fertighausfirmen | ● | ◐ Konfigurator L2 | ◐ | ○ | ○ | Interaktive Forschung, >50 Praktiker | ○ |
| Ramaji et al. [V] | 2017 | Journal | Produktorientiertes IDM mit Product Architecture Model | ○ (Modulbau) | ○ | ◐ | ● IDM/IFC | ○ | Abgleich mit US-Projekt | ○ |
| Khalili & Chua [V] | 2013 | Journal | IFC → Graph → Konfigurationen von Fertigteilgruppen, Constructability-Regeln | ○ (Beton) | ○ | ● | ● IFC | ◐ | Beispiel: −15 % Kosten | ○ |
| Isaac et al. [V] | 2016 | Journal | Graph- und Cluster-Modularisierung aus BIM-Daten | ○ | ○ | ● | ◐ | ○ | Realprojekt LISA | ○ |
| Yuan et al. [V] | 2018 | Journal | DfMA-orientiertes parametrisches Design (Revit-Familien) | ○ | ○ | ◐ | ◐ | ◐ | Beispiele | ○ |
| Alwisy et al. [V] | 2019 | Journal | MCMPro: 2D-CAD → BIM → Werkstattpläne Holzrahmen-Paneele (Platform Framing) | ● | ○ | ● | ○ | ● Werkstattplan | Fallanwendung | ○ |
| Liu et al. [V] | 2018 | Journal | Automatisches Beplankungslayout (OSB/Gips) im Leichtbau | ● | ○ | ● | ◐ BIM | ● Zuschnitt | Fallprojekt, Verschnitt | ○ |
| Wang et al. [V] | 2019 | Konferenz | BIM → ERP-Stückliste (Stud, OSB) Paneelbau | ● | ○ | ● | ○ | ◐ | 5 Projekte, 7,9 % Fehler | ○ |
| Adel et al. [V] | 2018 | Konferenz | Rechnerischer Entwurf robotergefertigter Holzrahmenmodule (DFAB HOUSE) | ● | ○ | ● | ○ | ● Roboter/CNC | 1:1-Bau | ◐ COMPAS |
| Adel, ETH-Diss. [V] | 2020 | Diss. | Wie oben, vertieft | ● | ○ | ● | ○ | ● | 1:1-Bau | ◐ |
| Graser et al. [V] | 2020 | Buchbeitrag | DFAB HOUSE als Gesamtdemonstrator | ● teilw. | ○ | ◐ | ○ | ● | Lessons Learned | ○ |
| Wagner et al. [V] | 2020 | Journal | Transportable Roboterplattform TIM für Zimmereien | ● | ○ | ○ | ○ | ● | Leistungsparameter BUGA | ○ |
| Orozco et al. [V] | 2023 | Journal | Co-Design mehrgeschossiger Holzbau, BHoM statt IFC | ● | ○ | ● | ◐ BHoM | ● | Prototyp 37 m² | ◐ |
| Granello et al. (WikiHouse) [V] | 2022 | Journal | WikiHouse Skylark: Bauteilbibliothek, Balkentests | ● | ◐ Selbstbau | ◐ | ◐ offene Dateien | ● CNC | 5 Balken 4-Punkt-Biegung | ● CC BY-SA |
| Priavolou & Niaros [V] | 2019 | Journal | Offenheit und Konvivialität von WikiHouse (Open-O-Meter) | ● | ◐ | ○ | ◐ | ● | Feldstudie, Interviews | ● |
| Geier, TUM-Diss. [V] | 2018 | Diss. | Kriterienkatalog und Analysemodell Komplexität vorgefertigter Holzbau | ● | ◐ Laienkommunikation | ◐ | ○ | ○ | leanWOOD-Fälle | ○ |
| Châteauvieux, TUM-Diss. [V] | 2023 | Diss. | IFC-Schallschutz Holzbau, Model Healing, Stoßstellenanalyse | ● | ○ | ● | ● IFC | ○ | Fallmodelle | ○ |
| Rojas Wettling et al. [V] | 2023 | Journal | IDM für Konzeptbewertung Holzrahmenbau, Abgleich mit IFC-Psets | ● | ○ | ◐ | ● IDM/IFC | ○ | Validierung mit Fertigern | ○ |
| Vakaj et al. [V] | 2023 | Journal | Ontologie OHO und KBE-Kostenschätzung Offsite | ○ | ○ | ● | ◐ OWL/LBD | ○ | Realszenario | ◐ Ontologie |
| Johnsson & Meiling [V] | 2009 | Journal | Mängelstatistik Raummodulfertigung | ● | ○ | ○ | ○ | ● | Audits 3 Phasen, 2 Firmen | ○ |
| Bonev et al. [V] | 2015 | Journal | Plattformen im ETO-Fertigteilbau (Hvam-Modellierung) | ○ | ○ | ◐ | ○ | ◐ | Längsschnitt-Fallstudie | ○ |
| Barlow & Ozaki [V] | 2005 | Journal | Japan: Pfadabhängigkeit, MC-Produktionssystem | ◐ | ◐ Showroom | ○ | ○ | ● | Fallstudien | ○ |
| Zhou [V] | 2023 | Journal | 3 Plattformtypen (Kit / + Interfaces / + Designregeln) | ◐ | ○ | ◐ | ◐ | ◐ | 9 Firmen | ○ |
| Build-in-Wood (H2020) [G] | 2024 | Projekt | Offenes Holzbausystem, Connector Matrix, BIM-Bibliothek | ● | ○ | ◐ | ◐ BIM-Bibliothek | ◐ | Demonstrator DTI | ● Zenodo |
| BIMwood (TUM/HSLU) `tum2023bimwood`, `geier2022bimwood` [G] | 2022/23 | Projekt | Holzbau-BIM-Referenzprozess, BAP | ● | ○ | ◐ | ● | ◐ | Case Study Studhalde | ◐ Templates |
| TIMBIM (AT) [G] | 2023/24 | Projekt | dataholz-Aufbauten als IFC, bSDD, ISO 23387 | ● | ○ | ◐ | ● IFC/bSDD | ○ | Praxistest ArchiCAD | ● Download |
| Bryden Wood/CDBB [G] | 2018 | Bericht | P-DfMA-Plattformen | ○ | ○ | ◐ | ○ | ◐ | ○ | ○ |
| Katerra (Rabeneck; HBS-Fall) [G] | 2021 | Kommentar/Fall | Scheitern Vertikalintegration | ◐ | ○ | ○ | ○ | ● | Fallanalyse | ○ |

---

## Gold und Warnungen je Arbeit

### A. Grammatiken und Laienentwurf (Portugal/USA/Polen)

**Duarte (2001), MIT-Dissertation „Customizing Mass Housing“ [V]; Duarte (2005), Automation in Construction [V]; `duarte2005towards` (lit-B)**
- *Gold:* Die Architektur der **Discursive Grammar** ist genau die Dreiteilung, die die Arbeit braucht. (1) Eine *Programming Grammar* erzeugt aus Nutzerangaben ein Programm (Brief). Das entspricht dem Sprach-Frontend, das Absichten in strukturierte Anforderungen übersetzt. (2) Eine *Designing Grammar* ist der Regelraum des Herstellers. (3) Die *Description Grammar* enthält Regeln der portugiesischen Wohnungsbauvorschriften. Das entspricht der BayBO- und DIN-Prüfung. Heuristiken lenken die Suche. Duarte entschied sich **ausdrücklich für deterministische Suche statt stochastischer Verfahren**, weil diese „mehrere Stunden“ brauchen können und für Web-Kunden unbrauchbar sind. Das liefert eine direkte historische Begründung für den deterministischen Kern. Seine Validierung war ein Turing-artiger Test: Siza erkannte ein grammatikerzeugtes Haus nicht als fremd.
- *Warnung:* Die Grammatik bildet nur einen Stil und einen Standort ab und hat keine Konstruktions- oder Fertigungsebene. Sizas Regeln waren „nie explizit niedergelegt“, das Extrahieren kostete Jahre. Das gilt auch für den Regelraum eines Fertighausherstellers: Der Wissenserwerb ist der Engpass.

**Benrós & Duarte (2009), „An integrated system for providing mass customized housing“, Automation in Construction 18(3) [V]**
- *Gold:* Die Arbeit koppelt ausdrücklich ein Entwurfssystem (Regeln) mit einem Vorfertigungs-Bausystem. Das ist die konzeptionelle Blaupause für „Regelraum ↔ Produktionssystem“.
- *Warnung:* Die Kopplung bleibt konzeptionell. Es gibt kein offenes Datenmodell und keine Maschinendaten. Genau hier setzt die Arbeit an.

**Sass (2006), „A Wood Frame Grammar“, IJAC 4(1) [V]; Knight & Sass (2010), AI EDAM 24(3) [V]**
- *Gold:* Die Regeln erzeugen **direkt CAD/CAM-Daten** für Holzbauteile. Das ist ein früher Beleg, dass Grammatikregeln bis zur Fertigung reichen können. Knight & Sass verlangen „visual–physical grammars“, die *vollständige* Fertigungsdaten erzeugen. Die IFC-bis-Schraube-Forderung formuliert das gleiche Ziel.
- *Warnung:* Das System arbeitet mit Sperrholz-Stecksystemen und 3-Achs-CNC, nicht mit Holzrahmenbau nach DIN/EC5 und nicht mit Abbundmaschinen. Es gibt keine Statik und keinen Brandschutz. Die Anwendung in New Orleans erforderte Eingriffe in letzter Minute wegen der Topografie (Wikipedia-Quelle, nur Hinweis, [U]).

**Kwieciński, Santos, de Almeida, Taborda, Eloy (2016), eCAADe [V]**
- *Gold:* Die Formgrammatik kodiert **Holzrahmenbauregeln**: Achsraster 60 cm, Räume als Vielfache von 60×60 cm, maximale Deckenspannweite 6 m. Diese Randbedingung bestimmt Tragwand-Lage und Gebäudebreite. Die Regeln haben einen Form- und einen Bedingungsteil und sind in Phasen gruppiert (Raster, Eingang, halböffentlich, privat). Das entspricht einer Regelstruktur, wie sie ein Hersteller-Regelraum braucht. Bei kleinen Häusern war die prozedurale Grammatik schneller als der GA.
- *Warnung:* Die kombinatorische Explosion wächst mit der Raumzahl. Die Autoren weichen auf einen GA aus und verlieren damit Determinismus und Nachvollziehbarkeit. Für die Arbeit heißt das: Der Suchraum wird über den Herstellerregelraum eng gehalten, statt ihn stochastisch zu durchsuchen.

**Kwieciński & Duarte (2019), eCAADe/SIGraDi [V]; Kwieciński & Słyk (2023), Automation in Construction 145 [V]**
- *Gold:* Das **Evaluationsdesign** ist direkt übernehmbar (siehe unten). Die Nutzer lösen eine Aufgabe für eine vorgegebene Familie (2 Erwachsene, Kinder 10 und 14 Jahre), ein Grundstück und eine Orientierung. Zwei Modi werden verglichen: Modifikation eines Vorschlags (M) und Entwurf von Null (S). Die Aufgabe dauert 15 min, danach folgen ein Likert-Fragebogen und offene Fragen. Architekten werden nachträglich aus der Stichprobe ausgeschlossen. Kernbefund: Laien wollen vor allem den **Grundriss** ändern, Möbel und Oberflächen sind ihnen am wenigsten wichtig. Als Ergebnis wünschen sie sich zuerst die **Baukosten**. Die Arbeit 2023 formuliert den Anspruch, den das Vorhaben einlösen soll: Das Werkzeug trägt die „Korrektheitsgarantie“ und entlastet den Architekten.
- *Warnung:* Die Stichproben sind klein (je Modus 7–13 Personen). Die Interaktion lief über einen Multi-Touch-Tisch mit Markern, nicht über Sprache. Es gibt keine Konstruktion und keine Kostenberechnung. Die Studie misst Zufriedenheit, nicht Baubarkeit.

**Khalili-Araghi & Kolarevic (2016), Journal of Building Engineering 5 [V]; Folgearbeiten und Dissertation Calgary [U]**
- *Gold:* Die begriffliche Trennung **Constraint Solving** (generativ, der Kunde hat keinen Einfluss) gegen **Constraint Checking** (der Kunde gestaltet, das System prüft automatisch) passt zur Arbeit, die beides kombiniert: deterministisch ableiten und per IDS prüfen. Die Architektur besteht aus einem Parametric Design System (Maßketten, Constraints, Zonen) und einem User Configuration System, das Designer und Kunden trennt. Der Architekt entwirft ein **„Meta-Haus“**, einen Lösungsraum statt eines Hauses. Die Dissertation zeigt, dass mangelndes Fachwissen Laien **nicht** daran hindert, befriedigende Lösungen zu finden. Experten gehen aber gewandter mit der Konfiguration um.
- *Warnung:* Das System ist an Revit gebunden, arbeitet ohne offenes Format und nur mit Maß-Constraints, ohne Konstruktion und ohne Fertigung. Die Autoren nennen als Grund für die Zurückhaltung der Hersteller: „The challenge of customer participation lies mostly in design validation, especially the code compliance checking“. Genau das adressiert die IDS- und Regelprüfung.

**Puusepp, Lõoke, Kivi (2017), CAADRIA [V]**
- *Gold:* Ein Live-Konfigurator eines estnischen Fertighausherstellers zeigt Echtzeitkosten zu jeder Entscheidung. Architekten erstellen das konfigurierbare Modell mit BIM-Plugins, der Kunde konfiguriert im Web, und die Wahl fließt zurück ins Autorensystem. Befunde aus einer qualitativen Studie und einer quantitativen mit n=133: Laien beherrschen die 3D-Navigation. Viele **bemerkten die Preisänderung nicht**. Optionen, die im Interface vom 3D-Modell getrennt sind, verwirren. Bei zu wenig Wahlmöglichkeiten langweilen sich die Nutzer schnell. Für die Arbeit heißt das: Kostenänderungen muss das System in der Sprachantwort aktiv benennen und nicht nur anzeigen.
- *Warnung:* Das Datenmodell ist nur partiell, weil BIM-Viewer keine Geometriemanipulation erlauben. Die Konfiguration muss im Autorensystem nachgebaut werden, der Medienbruch bleibt.

**Swanenburg (2016), MSc-Arbeit Universität Twente [V]**
- *Gold:* Online-Experiment mit echten Kaufinteressenten aus einer Datenbank. Randomisiert werden „Customization via Starting Solutions“ (CvSS), „Attribute-by-Attribute“ (AbA) und eine Kontrollgruppe mit Standardhaus verglichen. Abhängige Variablen sind *Preference Fit* und *Kaufwahrscheinlichkeit*, Prädiktoren nach dem MOA-Rahmen „process enjoyment“, „design freedom“ und „ease of use“. „Design freedom“ sagt Preference Fit voraus, „process enjoyment“ beide Zielgrößen.
- *Warnung:* Es handelt sich um eine Masterarbeit, nicht begutachtet. Das MOA-Modell erklärt nur teilweise.

### B. Schweden: Plattformen, Konfiguration, KBE

**Jensen, Olofsson, Johnsson (2012) `jensen2012configuration`; Jensen, Lidelöw, Olofsson (2015) `jensen2015product` (beide lit-B)**
- *Gold:* Konfiguration durch **Parametrisierung** von Bauteilen statt durch Auswahl fester Varianten, im Raumelement-Holzbau. Das ist die direkte Begründung, warum Wände im Regelraum parametrisch sind (Länge, Öffnungen) und nicht katalogisiert.
- *Warnung:* Der Kunde ist nicht Nutzer, und ein offenes Austauschformat fehlt.

**Malmgren, Jensen, Olofsson (2010), ITcon 15 [V]**
- *Gold:* **Vier Sichten auf dasselbe Produkt**: Kunde, Engineering, Produktion, Montage. Die Informationsflüsse **stromaufwärts** zum Kunden fehlen in der Praxis und führen zu Ad-hoc-Lösungen. Für die Arbeit folgt: Fertigungs- und Montagerestriktionen müssen in der Kundensicht in Laiensprache sichtbar werden, etwa „diese Fensterbreite geht, weil …“.
- *Hinweis:* ITcon führt denselben Titel 2011 in Band 16 (S. 697–712) ein zweites Mal. Zitiert wird die Erstveröffentlichung.

**Sandberg, Johnsson, Larsson (2008), ITcon 13 [V]**
- *Gold:* KBE heißt, dass die Geometrie-Engine an eine Regelbasis gekoppelt ist. Der Demonstrator: Ein **Verkäufer ändert mit dem Kunden die Treppe**, das Tool rechnet die Folgen für Deckenbalken und Kosten und warnt bei nicht fertigbaren oder zu weichen Varianten mit Änderungsvorschlag. Das ist der Urtyp des Kunden-Dialogs der Arbeit.
- *Warnung:* Informationsmanagement im frühen Entwurf ist „ad hoc und personenabhängig“, dazu kommt eine „Unikat-Mentalität“. Standardisierung ist *Vorbedingung*, weil das Wissen begrenzt und gut beschrieben sein muss. Das Tool muss regelmäßig gepflegt werden, sonst veraltet es. Für die Arbeit heißt das: Regelpflege, Versionierung und Governance gehören zur Methode.

**Veenstra, Halman, Voordijk (2006), Research in Engineering Design 17(3) [V]** (Niederlande, aber Grundlagenwerk der Plattformforschung)
- *Gold:* Die **GVI/CI-Indizes** (Generational Variety Index, Coupling Index nach Martin & Ishii) entscheiden, welche Module standardisiert und welche variabel werden. Die Schwelle legen die Autoren am Mittelwert fest. Außerdem schlagen sie vor, Module nach **räumlicher Nutzung** statt nach Bauelementen zu klassifizieren, weil das der Kundensicht entspricht. Das ist hilfreich für die Frage, auf welcher Ebene der Laie spricht: Räume, nicht Wände.
- *Warnung:* Es handelt sich um eine Einzelfallstudie (Plegt-Vos). Die Indexwerte beruhen auf Expertenschätzungen.

**Jansson, Viklund, Olofsson (2018), Buildings 8(2):34 [V]**
- *Gold:* **Offene Layout-Parameter** sind Schlüssel zur Kreativität, Vordefinition ist Schlüssel zur Effizienz. Architekten durchlaufen divergente und konvergente Phasen und brauchen Divergenz, um die Plattformgrenzen auszuloten. Das begründet eine Rolle für den Architekten oder Entwurfsverfasser nach Art. 61 BayBO „über“ dem Laien.
- *Warnung:* „Understanding platform constraints is often difficult“, besonders unter Zeitdruck. Das trifft auf Laien noch stärker zu, deshalb muss das System Grenzen erklären und nicht nur verbieten.

**Popovic, Raudberget, Elgh (2020), SPS/IOS Press [V]; Popovic, Elgh, Heikkinen (2021), Automation in Construction 126 [V]; Popovic (2020), Dissertation Jönköping [V]**
- *Gold:* Die Methode ist das stärkste übernehmbare Datenmodellierungsmuster. **Design Platform** (Produktstruktur plus Design Assets: Lösungs-, Geometrie-, Bewertungsressource, Constraints) wird mit dem **IDM** kombiniert: BPMN-Prozesskarte plus **Exchange Requirement Specification**. Die ERS ist eine Matrix mit Austauschmodellen als Spalten und Plattformobjekt-Attributen als Zeilen. Jede Zelle trägt einen Status: **G** (generiert), **M** (modifiziert), **T** (weitergereicht) und neu **R** (Reuse). Für die Arbeit heißt das: Jede Spalte der ERS wird eine IDS-Datei, der Status steuert, welche Facetten geprüft werden. Das Konstrukt „Design Module“ beschreibt flexible Raumelemente, die in Configure-, Modify- oder Engineer-to-Order spezifiziert werden. Das passt zur Unterscheidung zwischen dem, was der Laie konfiguriert, und dem, was die Firma nachplant.
- *Warnung:* Validierung an nur einem Fall. Laut Popovic et al. (MOC 2019, Interviews in 2 schwedischen Holzhausfirmen) sind Vertriebskonfiguratoren **nicht vertikal mit CAD und ERP integriert**, und der Vertrieb akzeptiert Wünsche **außerhalb** des Bausystems, was die Planung belastet.

**Lennartsson, Raudberget, Elgh, Koroth (2022), TE2022/IOS Press [V]**
- *Gold:* Eine Firma mit drei Produktlinien (Paneel frei, Raumzelle mit Konfigurator, Raumzelle fix) lenkt hartnäckige Kunden in die flexible Linie und schützt so den Regelraum der Standardlinien. Das ist ein Muster, wie ein Laiensystem Anfragen „außerhalb des Regelraums“ behandelt: als Übergabe an die Planung statt als Verbot.
- *Warnung:* **Starke Kunden erodieren die technische Plattform.** Komponenten kommen ohne Wirkungsanalyse hinzu, und Wissen sitzt „in einzelnen Mitarbeitern“.

**Wikberg, Olofsson, Ekholm (2014) `wikberg2014design`; Jansson, Johnsson, Engström (2014) `jansson2014platform`; Johnsson (2013) `johnsson2013production` (lit-B)**: Plattformbegriffe (technische Plattform, Prozessplattform, Wissens- und Beziehungsplattform) sowie architektonische Objekte als Brücke zwischen Kundenwunsch und Systemfähigkeit. Sie dienen als Terminologiebasis für Kapitel 2.

**Johnsson & Meiling (2009), Construction Management and Economics 27(7) [V]**
- *Gold:* Mängel werden über Qualitätsaudits in drei Phasen erfasst und kategorisiert, in zwei schwedischen Raummodulfirmen. Diese Kategorisierung ist als Messgröße für eine spätere Feldevaluation übernehmbar: Welche Mängel hätte eine IDS- oder Regelprüfung verhindert?
- *Warnung:* Auch im Fertigbau stammen viele Mängel aus Planung und Informationsübergabe, nicht aus der Werkstatt.

**Lindbäcks (Firmendarstellung) [G]:** Lindbäcks betont, dass die Volumengeometrie projektweise veränderbar bleibt, ist also Plattform, kein Katalog. Das größte Projekt hatte 37 000 Elementzeichnungen. Diese Größenordnung zeigt, warum Plan- und Maschinendaten automatisch entstehen müssen. Jansson (2009, Luleå-Bericht) fand, dass Projektleitung und Koordination über 40 % der Planungszeit beanspruchten [U, schwedischer Bericht].

### C. Japan und Plattformökonomie

**`barlow2003choice` (lit-B); Barlow & Ozaki (2005), Environment and Planning A 37 [V]; `noguchi2003effect`, `linner2012evolution`, `bock2015robot` (lit-B)**
- *Gold:* Sekisui Heim steht für **„customized standardization“**: assemble-to-order aus Standardkomponenten, etwa 20 000 Häuser pro Jahr. Die Auswahl findet im Showroom mit Beratern statt, die Fertigung ist qualitätsorientiert. Barlow & Ozaki erklären den Erfolg über Pfadabhängigkeit, also Marktstruktur und Grundstücksbesitz beim Kunden. Das trifft auch auf den deutschen Fertighausmarkt zu, in dem der Kunde meist selbst ein Grundstück hat.
- *Warnung:* Das Modell lässt sich nur begrenzt übertragen, weil die UK-Spekulationsbauweise strukturell anders funktioniert. Deshalb gilt auch für die Arbeit: den Kontext Bayern und Fertighaus ausdrücklich machen.

**Linner (2013), TUM-Dissertation [V]:** vergleichende Analyse von 140 Einzelaufgaben-Baurobotern und 30 automatisierten Feldfabriken. Sie ist nützlich als Systematik für das Fertigungsende, aber ohne Laienentwurf.

### D. Deutschland, Schweiz, Österreich

**Geier (2018), TUM-Dissertation „Analysemodell für das vorgefertigte Bauen mit Holz“ (Betreuer Kaufmann) [V]**
- *Gold:* Ein **Kriterienkatalog** ordnet architektonische, funktionale und konstruktive Aspekte nach Komplexitätsgrad und trennt *verhandelbare* von *nicht verhandelbaren* Vorgaben. Das ist ein direktes Vorbild für die Klassifikation der Regeln im Regelraum als hart, weich oder Firmenpolitik. Das Analysemodell ist ausdrücklich auch für die **Laienkommunikation mit dem Bauherrn** gedacht. Als Perspektive nennt Geier die Kostenschätzung in frühen Phasen über eine Verknüpfung mit Elementkatalogen.
- *Warnung:* Das Modell ist qualitativ und nicht maschinenlesbar. Die isolierte Übertragung von Lean aus der Produktion ist laut Geier die Ursache des Scheiterns in der Baupraxis.

**BIMwood (TUM 2019–2023; HSLU/BFH Innosuisse) `tum2023bimwood`, `geier2022bimwood` (lit-B) [G]**
- *Gold:* Referenzprozess für holzbauspezifisches BIM, BAP-Vorlage, „Planung der Planung“ nach dem Pull-Prinzip und Informationsbereitstellungsplan nach ISO 19650. Im Holzbau fallen Entscheidungen früher als im Massivbau. Das ist ein Argument, warum der Laie *schon im Entwurf* in einem fertigungsnahen Regelraum arbeiten sollte.
- *Warnung:* Der Holz&BIM-Vorbericht nennt fehlende Standards, uneinheitliche Bearbeitungstiefe und unklare Verantwortlichkeiten. Viele Schnittstellenprobleme entstehen aus fehlenden Festlegungen und nicht aus der Technik.

**Châteauvieux (2023), TUM-Dissertation (Betreuer Borrmann) [V]**
- *Gold:* Die Eingangsmodelle werden zuerst geprüft und per **Model Healing** korrigiert. Danach folgt eine Stoßstellenanalyse über semantische und geometrische Abfragen auf IFC. Die Ergebnisse landen in einem akustischen Fachmodell. Das ist ein Muster für DIN-4109-Nachweise aus dem IFC der Arbeit und eine Begründung, warum ein **selbst erzeugtes** IFC (statt eines importierten) das Healing überflüssig macht.
- *Warnung:* Reale Autoren-IFCs sind für Holzbau-Nachweise oft unzureichend, das Healing ist nötig.

**TIMBIM I–III (Holzforschung Austria, buildingSMART Austria, FV Holzindustrie, VIE Build) [G]**
- *Gold:* dataholz-Aufbauten stehen als IFC-Download und mit Datenvorlagen nach ISO 23387 im bSDD. Damit gibt es eine geprüfte Bauteilaufbau-Quelle mit Brand-, Schall- und Wärmeschutz- sowie Ökodaten (vgl. `dataholz` im Vorbestand).
- *Warnung:* Die geplante Variante, jede Schicht als eigene Komponente über IfcAggregat abzubilden, wurde **verworfen**, weil die Design-Transfer-MVD in Autorensoftware nicht implementiert war. Die Schichten werden nur alphanumerisch transportiert. Das ist ein konkretes Risiko für „IFC bis Ständer“, wenn Fremdsoftware das Modell öffnen soll. Zielviewer müssen daher früh getestet werden.

**Wagner, Alvarez, Kyjanek, Bhiri, Buck, Menges (2020), Automation in Construction 120 [V]; Orozco et al. (2023), Sustainability 15(23) [V]; Treml et al. (2025), WCTE [U]**
- *Gold:* TIM ist eine transportable Roboterplattform, die sich in normale Zimmereien integrieren lässt. Das zeigt, dass Automatisierung nicht Großfabrik bedeuten muss. Das Co-Design in Stuttgart koppelt Entwurf, Engineering und Fertigung über direktes und „kuratiertes“ Feedback.
- *Warnung:* Orozco et al. schreiben ausdrücklich, dass ein interoperabler Datenstandard fehle. Sie nutzten deshalb BHoM statt IFC als globales Gebäudemodell. Das stützt die Behauptung, dass ein durchgängiges IFC bis zur Fertigung eben *nicht* Stand der Technik ist, und ist zugleich ein Risiko.

**ETH/Gramazio Kohler: Adel et al. (2018), ACADIA [V]; Adel (2020), ETH-Dissertation [V]; Graser et al. (2020), Fabricate [V]**
- *Gold:* Ein fertigungsbewusster Rechenentwurf integriert Architektur-, Geometrie-, Statik- und Fertigungsconstraints. Fertigungsattribute sind je Balken festgelegt: Greifebene, Endschnittebenen, Bohrvektoren und -anker. Daraus entsteht CNC-Säge-Code. Die **Attributliste je Stab** ist eine gute Vorlage für die BTLx-Bearbeitungen je `IfcMember`. Die Werkzeugkette lebt als COMPAS-Ökosystem weiter (vgl. `compastimber`).
- *Warnung:* Es handelt sich um Nonstandard-Einzelbauten mit Roboterzelle. Das Ergebnis lässt sich nicht auf Serienfertigung mit Abbundanlage und Wandfertigungsstraße übertragen. Die DFAB HOUSE war ein Demonstrator mit hohem Forschungsaufwand.

### E. Nordamerika: Holzrahmen-Automatisierung

**Alwisy, Bu Hamdan, Barkokébas, Bouferguène, Al-Hussein (2019), IJCM 19(3) [V]; Alwisy (2012) ASCE-Konferenz und MSc Alberta [V]**
- *Gold:* **MCMPro** automatisiert Design und Drafting von Holzrahmen-Paneelen nach der Platform-Framing-Methode. Aus 2D-CAD entstehen ein BIM und ein „Construction Manufacturing BIM“, daraus Werkstattpläne. Das ist das nächstliegende Vorbild für die Ableitung Wand → Ständer/Rähm/Schwelle → Werkstattplan. Die Regeln für Ständerraster, Öffnungen, Stürze und Aufdopplungen sind im Code formalisiert.
- *Warnung:* VBA in AutoCAD ist proprietär und nicht offen. Das System startet vom 2D-Plan eines Planers, nicht vom Laien. Es gibt keine Maschinenschnittstelle nach BTL/WUP.

**Liu, Singh, Lu, Bouferguène, Al-Hussein (2018), Automation in Construction 89 [V]; Wang et al. (2019), MOC Summit [V]**
- *Gold:* Liu et al. optimieren Beplankung und Gipslayout automatisch, mit Plattenformaten, Stoßregeln und Verschnittminimierung. Das ist die gleiche Klasse von Regel wie die WUP-Plattenaufteilung. Wang et al. messen die BIM→ERP-Stücklistenumsetzung **gegen manuelle Referenzwerte** (7,9 % Fehler über 5 Projekte, unter 1 min gegenüber 20–30 min manuell). Dieses Evaluationsmuster ist direkt übernehmbar: Automatisch erzeugte Stückliste und Maschinendaten werden gegen die Arbeitsvorbereitung des Herstellers verglichen.
- *Warnung:* Die Genauigkeit sinkt bei großen Häusern, weil Daten fehlen. Die Regeln müssen an echten Projekten des Herstellers kalibriert werden.

### F. IFC/IDM für Vorfertigung

**Ramaji, Memari, Messner (2017), J. Comput. Civ. Eng. 31(4) [V]; Ramaji & Memari (2016), JCEM [U]**
- *Gold:* Das IDM wird um ein **Product Architecture Model** erweitert. Damit lässt sich die Bauteilhierarchie des vorgefertigten Produkts abbilden. Die Autoren sehen darin die Basis, um IFC für Modulbau zu erweitern. Für die Arbeit heißt das: Die PAM-Hierarchie Haus → Element → Wand → Ständer → Verbindungsmittel wird auf `IfcElementAssembly` und `IfcRelAggregates` gemappt.
- *Warnung:* Der Fokus liegt auf mehrgeschossigem Stahl- und Modulbau, IFC-Erweiterungen bleiben Vorschlag.

**Khalili & Chua (2013), J. Comput. Civ. Eng. 27(3) [V]**
- *Gold:* Aus IFC werden Geometrie und Topologie gelesen und als **Graphmodell** abgebildet. Alle Gruppierungen werden enumeriert und dann mit **Constructability-Regeln** gefiltert. Im Beispiel sanken die Kosten um bis zu 15 %. Das ist ein Muster für die Elementierung (Wandteilung nach Transport- und Tischmaß) als Graph plus Regeln.
- *Warnung:* Es handelt sich um Betonfertigteile, und die vollständige Enumeration skaliert schlecht.

**Rojas Wettling, Mourgues, Guindos (2023), Advances in Civil Engineering [V]**
- *Gold:* IDM für die **Konzeptbewertung von Holzrahmenbau-Projekten**, also die Informationsparameter, die Fertiger früh brauchen. Sie wurden mit chilenischen Vorfertigern validiert und mit IFC-Property-Sets abgeglichen. Das ist eine fertige Parameterliste als Startpunkt für die IDS der frühen Phase.
- *Warnung:* Der Kontext ist Chile, deutsche Normbezüge fehlen.

**Isaac, Bock, Stoliar (2016), Automation in Construction 65 [V]; Yuan, Sun, Wang (2018), Automation in Construction 88 [V]**: Graph- und Clusterbildung für Module aus BIM (Isaac) sowie DfMA-Familienvorlagen in Revit (Yuan). Beide sind Belege für regelbasierte Fertigungsgerechtheit, aber ohne Laien und ohne offenes Format.

### G. Konfiguratoren (Hvam/Forza-Schule) und Kosten

**Shafiee, Piroozfar, Forberg, Hansen, Farr (2025), AEDM 21(3) [V]**
- *Gold:* **Die vollständigste Kette in der Literatur.** Ein Laie konfiguriert im Web eine Garage mit Echtzeit-Mengen, Kosten und CO₂. Daraus entstehen automatisch Anschlussdetails, Arbeitszeichnungen und Pre-cut-Produktionsdateien. Die Architektur hat drei Schichten: Product Family Master Plan und Produktstruktur als JSON, Grasshopper, ShapeDiver und WordPress. Methodisch folgt die Arbeit dem Dreischritt von Shafiee et al. (2018): Scope, Wissenserwerb und -modellierung, Umsetzung. Die Regeln prüfen gültige Kombinationen nach Baubarkeit, Montage, **Bauvorschriften**, Entwurfsprinzipien und Vertriebsstrategie.
- *Warnung:* Es ist nur ein Nebengebäude. Das System ist proprietär, ohne IFC und ohne Normprüfung im Sinne einer Baugenehmigung. Die Evaluation beruht auf einer Firmenbefragung (56,6 % sagen „spart Ressourcen“), nicht auf Messung.

**Piroozfar, Farr, Hvam, Robinson, Shafiee (2019), Automation in Construction 106 [V]; Farr, Piroozfar, Robinson (2014), Automation in Construction 45 [V]; `haug2012definition`, `trentin2013sales`, `hvam2008product`, `forza2006product` (lit-B)**: BIM als Konfigurator, Configurator-Capabilities (Solution Space Development, Choice Navigation) und Produktvariantenmaster. Gold ist die Terminologie für die Konfigurator-Anforderungen. Die Warnung: BIM-Autorensysteme als Konfigurator bleiben Expertenwerkzeuge.

**Bonev, Wörösch, Hvam (2015), Construction Innovation 15(1) [V]**
- *Gold:* Mehrere Plattformschichten (Produkt, Prozess, Logistik) und Kostenverlauf je Produktfamilie über das Projekt. Das ist ein Muster, um den Kostenvorteil des Regelraums darzustellen.
- *Warnung:* Betonfertigteile, Einzelfall.

**Vakaj, Cheung, Cao, Tawil, Patlakas (2023), ITcon 28 [V]**
- *Gold:* Die Ontologie **OHO** (Core, Produktion, Kosten) ermöglicht eine **aktivitätsbasierte** Kostenschätzung für DfMA-Häuser mit den Phasen Design, Offsite-Produktion, Transport, Onsite, Nutzung. Implementiert ist sie als REST-KBE-Tool. Das ist ein Vorbild für die frühe Kostenschätzung aus dem IFC. Kosten entstehen dann aus Fertigungsschritten (Abbund, Wandstraße, Montage) statt aus €/m² BGF.
- *Warnung:* Es gibt nur ein Demonstrationsszenario, eine Genauigkeitsmessung gegen Nachkalkulation fehlt.

**Montali, Overend, Pelken, Sauchelli (2017 online), AEDM [U: Band/Seiten]**
- *Gold:* Das KBE-Werkzeug wirkt als **„interim product configurator“**: Es verschiebt ETO-Produkte Richtung Make-to-Order, indem Fertigungswissen des Herstellers in Regeln gegossen wird. Die Methodik verwendet MOKA/ICARE-Formulare, UML und DSM zur Wissensstrukturierung. Die ICARE-Formulare sind eine erprobte Vorlage für die Dokumentation einzelner Herstellerregeln.
- *Warnung:* KBE-Entwicklung ist zeitaufwendig, das nennen die Autoren als Hauptgrenze.

### H. Open Source und Open Building

**Granello, Reynolds, Prest (2022), Engineering Structures 252 [V]; Priavolou & Niaros (2019), Sustainability 11(17) [V]**
- *Gold:* WikiHouse Skylark bietet eine Bibliothek standardisierter Subassemblies. 3D-Modelle, CNC-Dateien und Montageanleitungen stehen unter **CC BY-SA** offen. Balken wurden im Versuch geprüft (5 Stück, 4-Punkt-Biegung nach ISO 22389-1) und analytisch mit Drehfedern modelliert. Das **Open-O-Meter** mit 8 Kriterien (Designdateien, Anleitung, Stückliste, editierbar, Beitragsleitfaden, kommerzielle Lizenz …) eignet sich als Checkliste, wenn Teile der Arbeit als Open Artefact veröffentlicht werden.
- *Warnung:* Die Dateien auf GitHub sind „uncategorized and not engineered“, Statikdaten werden nicht geteilt, und Montageanleitungen sind nicht editierbar. Bestehende Designs anzupassen dauert oft länger als neu zu zeichnen. Offenheit ohne Datenmodell und Regeln skaliert nicht.

**`habraken2021supports`, `kendall2000residential` (lit-B):** Die Trennung Support/Infill ist die theoretische Grundlage, warum der Laie im Infill (Grundriss) frei und im Support (Tragwerk, Raster) gebunden ist.

### I. Graue Literatur zu Plattform-Hypes [G]

- **Bryden Wood/CDBB (2018), „Platforms: Bridging the gap between construction and manufacturing“:** P-DfMA mit wenigen Plattformen, die über Spannweite und Höhe definiert sind. Das ist ein Narrativ für Politik und Firmenstrategie und nicht wissenschaftlich begutachtet.
- **Katerra:** Rabeneck (2021, Buildings & Cities, Kommentar) und der HBS-Fall Katerra (A/B) (Hyde, Eisenmann, Quinn 2021) beschreiben mehr als 2 Mrd. USD Kapital, Übernahmen von Architektur- und Baufirmen, eigene Software und Holzpaneelfabriken, Konkurs 2021. *Warnung:* Das Unternehmen setzte auf Vertikalintegration statt auf eine stabile Produktplattform, verkannte, „warum Bauen so ist, wie es ist“, und hatte Qualitätsprobleme. Für die Arbeit heißt das: Sie sollte sich als Werkzeug im Regelraum *eines bestehenden* Herstellers positionieren, nicht als Neuerfindung der Branche.
- **Build-in-Wood (H2020, GA 862820, bis 08/2024):** offenes Holzbausystem (Pfosten-Riegel und vorgefertigte Holzrahmen-Fassade) mit „Regeln“ für Öffnungen, Connector Matrix und BIM-Bibliothek (hsbcad, Bimetica). Die Ergebnisse liegen auf Zenodo. Das ist Gold als offene Quelle für Fassadenöffnungsregeln.

---

## Was keine Arbeit bisher geschafft hat (Abgrenzung und Neuheit)

| Glied der Kette | Beste gefundene Arbeit | Lücke |
|---|---|---|
| Laie entwirft selbst | Kwieciński & Słyk 2023; Khalili-Araghi & Kolarevic 2016; Puusepp et al. 2017; Shafiee et al. 2025 | Keine Sprachsteuerung, keine Tragwerks- oder Fertigungsebene (außer Shafiee) |
| Herstellerregelraum formalisiert | Sandberg et al. 2008; Jensen et al. 2012; Popovic et al. 2021; Kwieciński et al. 2016 | Einzelausschnitte (Treppe, Raumelemente, Raster), kein vollständiger Holzrahmenbau-Regelraum |
| Regeln der Bauordnung | Duarte 2001 (portug. Wohnungsbaurecht als Description Grammar) | Keine deutsche/bayerische Landesbauordnung, keine Verknüpfung mit Bauantrag |
| Durchgängiges offenes Modell bis Ständer/Schraube | Ramaji et al. 2017 (Konzept); Alwisy 2019 (proprietär bis Ständer) | **Kein IFC-4.3-Modell bis Verbindungsmittel.** Orozco 2023 und TIMBIM belegen, dass IFC hier heute umgangen wird |
| Maschinendaten | Alwisy 2019 (Werkstattplan); Adel 2018 (Roboter/CNC); Shafiee 2025 (Pre-cut) | Kein BTLx/WUP aus einem Laienentwurf |
| Prüfung per IDS | Rojas Wettling 2023 (IDM, Psets); Popovic 2021 (ERS) | Kein IDS-basiertes Gate zwischen Konfiguration, Bauantrag und Fertigung |
| Bauantrag | – | Keine gefundene Arbeit leitet Bauvorlagen aus einem Konfigurator ab |
| Evaluation mit Laien **und** Messung der Baubarkeit | Kwieciński 2019 (Zufriedenheit); Wang 2019 (Genauigkeit) | Nirgends beides zusammen |

**Neuheitsbehauptung, belastbar formuliert:** Nach dieser Recherche mit 53 neuen Einträgen in lit-D (davon 5 graue Literatur) und 29 aus lit-B übernommenen Arbeiten ist keine Arbeit bekannt, die (1) Laien per Sprache (2) in einem vollständig formalisierten Holzrahmenbau-Regelraum eines realen Herstellers entwerfen lässt, deterministisch, und daraus (3) ein IFC-4.3-Modell bis zu Ständer und Verbindungsmittel erzeugt. Dieses Modell wird (4) per IDS gegen Bauordnung und Herstellerregeln geprüft, und (5) aus ihm werden sowohl Bauvorlagen als auch BTLx/WUP abgeleitet. Die Einzelteile haben jeweils Vorläufer, die Kette als Ganzes nicht.

---

## Evaluationsdesigns zum Übernehmen

1. **Laien-Usability nach Kwieciński & Duarte (2019):** Die Aufgabe ist standardisiert (Familie, Grundstück, Orientierung). Zwei Bedingungen werden randomisiert: „Vorschlag modifizieren“ gegen „von Null“. Übertragen auf die Arbeit: vorbelegter Hausentwurf gegen freie Sprachbeschreibung. Zeitlimit 15 min, danach Likert-Skalen zu Usability, Effektivität und Zufriedenheit sowie offene Fragen. Fachleute werden nachträglich ausgeschlossen. Die Bedingungen werden mit Mann-Whitney verglichen. **Ergänzung für die Arbeit:** SUS, NASA-TLX sowie die Zahl der Regelverletzungen und Rückfragen je Sitzung.
2. **Konfigurator-A/B-Experiment nach Swanenburg (2016):** Randomisierte Gruppen, eine Kontrollgruppe mit Standardhaus, abhängige Variablen *Preference Fit* und *Kaufwahrscheinlichkeit*, Prädiktoren nach MOA. Für die Arbeit: Sprachdialog, grafischer Konfigurator und Katalog-Kontrollgruppe im Vergleich.
3. **Live-Analytics nach Puusepp et al. (2017):** Protokoll der Entscheidungsgraphen realer Nutzer. Gemessen wird, welche Optionen gewählt werden, wo abgebrochen wird und ob Preisänderungen wahrgenommen werden (Probe-Frage).
4. **Ground-Truth-Vergleich nach Wang et al. (2019):** Automatisch erzeugte Stückliste und BTLx werden gegen die manuelle Arbeitsvorbereitung des Herstellers an N realen Projekten verglichen. Gemessen werden Fehlerquote je Positionstyp und Zeitbedarf.
5. **Turing-artiger Experten-Blindtest nach Duarte (2001):** Planer des Herstellers bekommen gemischt systemerzeugte und von Hand geplante Entwürfe und sollen sie zuordnen. Ergänzend wird die Freigabequote ohne Änderung erfasst.
6. **Mängel- und Nacharbeitsaudit nach Johnsson & Meiling (2009):** Mängelkategorien in Planung, Werk und Montage. Retrospektiv wird geprüft, welcher Anteil durch IDS- oder Regelprüfung abgefangen worden wäre.
7. **Plattform-Robustheitsanalyse nach Veenstra et al. (2006) / Lennartsson et al. (2022):** GVI/CI je Modul und Anteil der Kundenanfragen außerhalb des Regelraums. Das ist eine Kennzahl für die Frage, wie gut der Regelraum den Markt abdeckt.
8. **Formativ/summativ mit Experten und Laien nach Khalili-Araghi (Diss. Calgary) [U]:** Zuerst testen Experten den Prototyp, dann bewertet eine gemischte Stichprobe die Nutzungsbereitschaft. Die Fähigkeit wird über Vorwissen gemessen (Architekturbezug, CAD-Erfahrung).
9. **Offenheitsbewertung nach Priavolou & Niaros (2019):** Das Open-O-Meter mit 8 Kriterien wird auf alle veröffentlichten Artefakte angewandt (Regeln, IDS, Beispiel-IFC).

---

## Konkrete Übernahmen in die Arbeit (Kurzliste)

- **Architekturbegründung:** Programming Grammar (Sprache → Brief), Designing Grammar (Herstellerregelraum), Description Grammar (BayBO/DIN), deterministische Heuristik (Duarte). Constraint-Checking mit automatischer Validierung (Khalili-Araghi & Kolarevic).
- **Datenmodell:** Die PAM-Hierarchie (Ramaji) wird auf IfcElementAssembly abgebildet. Die Design Platform mit Design Assets (Popovic/André) wird zum Regelraum-Schema. Die ERS mit G/M/T/R (Popovic) wird zur IDS je Übergabe.
- **Regeldokumentation:** ICARE-Formulare und DSM (Montali), Klassifikation verhandelbar/nicht verhandelbar (Geier), Vier-Sichten-Modell (Malmgren).
- **Holzrahmenbau-Regeln als Startpunkt:** 60-cm-Raster und Spannweiten (Kwieciński 2016), Platform-Framing-Regeln (Alwisy), Beplankungsoptimierung (Liu), Öffnungsregeln (Build-in-Wood), Bauteilaufbauten (dataholz/TIMBIM).
- **Kosten:** aktivitätsbasiert nach Fertigungsschritt (Vakaj OHO) und in der Sprachantwort aktiv benannt (Puusepp).

---

## Nicht verifizierte Hinweise (nicht in der .bib)

- Raposo, Eloy, Dias (2023): Definition und Evaluation einer GUI für ein Housing-Co-Design-System (Iscte). Venue ungeprüft.
- Khalili-Araghi (ca. 2020), Dissertation University of Calgary, Experimente zur Nutzungsbereitschaft. Titel und Jahr nicht an der Katalogseite geprüft.
- Treml et al. (2025), WCTE, DOI 10.52202/080513-0012. Nur über die IntCDC-Seite gesehen.
- Popovic, Thajudeen, Vestin (2019), „Smart Manufacturing Support to Product Platforms in Industrialized House Building“, MOC Summit. Jahr nicht geprüft.
- André, Lennartsson, Elgh (2019), „Exploring the design platform in industrialized housing …“, ATDE 10, S. 125–134. Nur als Zitat gesehen.
- Mendonça, Passaro, Castro Henriques (2018), SIGraDi, WikiHouse-Generativwerkzeug. Nur als Zitat gesehen.

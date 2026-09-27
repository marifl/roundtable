# 6 Anforderungen

Status: Entwurf v0.1 (27.09.2026). Befunde tragen [V] (an der Primärquelle geprüft) oder [U] (nicht an der Primärquelle geprüft oder eigene Bewertung). Keine Rechtsberatung. Der maschinenlesbare Anforderungskatalog liegt in `spezifikation/anforderungen.csv`, die Datenlieferungen in `spezifikation/datenlieferungen.csv`, die Verantwortungs- und Formregeln dieses Kapitels in `spezifikation/regelkatalog-06.yaml`.

## 6.0 Einordnung und Vorgehen

Im Prozessmodell der Design Science Research folgt auf die Identifikation des Problems die Festlegung der **Ziele einer Lösung** [@peffers2007design]. Diese Ziele müssen so formuliert sein, dass sich das Artefakt später an ihnen messen lässt [@hevner2004design]. Für diese Arbeit heißt das: Aus dem Zielbild, dem Stand der Praxis (Kapitel 3), dem Rechtsrahmen (Kapitel 4) und dem Stand der Forschung (Kapitel 5) entstehen Anforderungen, deren Abnahmekriterium ein Test ist. Kapitel 20 prüft das Artefakt gegen genau diese Tests.

Das Kapitel beginnt nicht auf einem leeren Blatt. Die bereits fertigen Kapitel 3, 8, 9, 9a und 9b enthalten zusammen **122 Anforderungen** (104 Muss, 18 Soll). Kapitel 7a enthält acht Anforderungen A1–A8 an jeden Nachweis, aber keine ANF-Nummern. Kapitel 6 hat deshalb drei Aufgaben:

1. **Ordnen.** Es führt Stakeholder und Rollen ein (6.1) und ordnet jede vorhandene Anforderung einer Phase der Kette von der Idee bis zur Übergabe zu (6.2).
2. **Ergänzen.** Es schließt die Lücken, die in keinem Fachkapitel liegen: Rollen und Rechte, die Phasen Idee, Vertrag, Bauantrag und Übergabe, die nichtfunktionalen Anforderungen (6.3) und die harten Grenzen aus Recht und Norm (6.4). Neue Anforderungen erhalten die Kennung `ANF-06-*`.
3. **Konsolidieren.** Es prüft die vorhandenen Anforderungen auf Überschneidungen und Widersprüche (6.5). Vorhandene Kennungen werden **nicht neu nummeriert**, sondern referenziert.

**E6.1 – Eine Anforderung hat genau eine Kennung und genau einen Ursprung.** *Entscheidung.* Jede Anforderung behält die Kennung des Kapitels, in dem sie begründet ist. Überschneiden sich zwei Anforderungen, bleiben beide bestehen; die strengere gilt, und die Konsolidierungstabelle in 6.5 verweist auf beide. *Begründung.* Eine Neunummerierung würde die Querverweise in den Regel- und Mappingdateien brechen, etwa `anforderungen: [ANF-09a-07]` in `regelkatalog.yaml`. Rückverfolgbarkeit vom Test zur Begründung ist das Ziel der Matrix in Kapitel 23. *Beleg.* Zielbild, „Rückverfolgbarkeitsmatrix“.

Für die Verbindlichkeit gelten die Regeln aus Abschnitt 3.7 und 8.8: **Muss** heißt, dass ohne die Anforderung ein Rechts-, Nachweis- oder Fertigungsfehler entstehen kann oder die Kette bricht. **Soll** heißt, dass sie Qualität oder Nutzen erhöht; eine Abweichung ist schriftlich zu begründen.

## 6.1 Stakeholder und Rollen

### 6.1.1 Rollen statt Personen

Ein Stakeholder ist eine Partei mit einem Interesse am System. Eine **Rolle** ist dagegen eine Menge von Rechten und Pflichten im System. Dieselbe Person kann mehrere Rollen haben: Ein angestellter Zimmerermeister kann Werkplaner und zugleich bauvorlageberechtigte Person sein. Umgekehrt kann eine Rolle wechselnde Personen haben. Das System muss deshalb Rollen modellieren und sie Personen mit **nachgewiesener Qualifikation** zuordnen. Diese Unterscheidung ist keine Formalie. Sie folgt aus drei Befunden der vorangehenden Kapitel.

- **Der Kunde entwirft, verantwortet aber nicht.** Ein Laie kann nicht Entwurfsverfasser sein. Die Firma wird es durch die Leitung einer namentlich benannten bauvorlageberechtigten Person (Art. 61 Abs. 6 BayBO) [@baybo2026] [V]; Abschnitt 4.3.5.
- **Die Reichweite einer Berechtigung hängt am Gebäude.** Ein Zimmerermeister ist nur für freistehende oder einseitig angebaute Wohngebäude der Gebäudeklassen 1 bis 3 mit höchstens drei Wohnungen bauvorlageberechtigt. Wird aus dem Endhaus ein Mittelhaus, verfällt seine Freigabe (Abschnitt 9a.4.1, ANF-09a-07).
- **„Unter der Leitung“ verlangt Einfluss, nicht nur eine Unterschrift.** Die Ingenieurkammer-Bau NRW wertet es als Berufspflichtverstoß, einen fertig vorgelegten Entwurf ohne rechtlich abgesicherte Einflussmöglichkeit zu unterzeichnen, selbst nach eigener Prüfung [@ikbaunrw2024unterzeichnung] [V; für Bayern nur analog]. Die bayerische Berufsordnung erlaubt die Urheberschaft nur für Leistungen unter eigener oder persönlicher Leitung [@byak2020berufsordnung] [V]. Das Bundesverfassungsgericht sieht den Zweck der Bauvorlageberechtigung darin, dass Vorlagen von Fachleuten angefertigt **und verantwortet** werden [@bverfg1970bvr11765] [V]. Die Begründung der BayBO 2008 nennt als Entwurfsverfasser, wer die Bauvorlagen fertigt und/oder verantwortlich zeichnet [@landtagby2007baybo] [V].

Aus dem dritten Befund folgt eine Rolle, die im Zielbild nur angedeutet ist: Die bauvorlageberechtigte Person gestaltet den **Regelraum** mit und gibt jede seiner Versionen frei, bevor ein Kundenentwurf dagegen geprüft wird (Recherche 27, „Folgen für Freigabe-Gates“, Nr. 1). Erst dadurch hat sie die Einflussmöglichkeit, die „unter der Leitung“ verlangt.

### 6.1.2 Rollenkatalog

Tabelle 6.1 führt die Rollen, ihre Rechtsstellung und ihre Aufgabe im Zielbild zusammen.

**Tabelle 6.1: Rollen im System**

| Kürzel | Rolle | Rechtsstellung | Aufgabe im Zielbild | Beleg |
|---|---|---|---|---|
| KU | Kunde (Bauherr) | Verbraucher im Verbraucherbauvertrag (§ 650i BGB); beauftragt Prüfsachverständige | entwirft im Regelraum, bemustert, erhält Baubeschreibung, schließt Vertrag, kann widerrufen, erhält Hausakte | [@bgb; @egbgb249]; Kap. 4.7, 9a.4.3 |
| VT | Vertrieb | Erfüllungsgehilfe der Firma; vorvertragliche Beratungspflicht | berät, erklärt Ablehnungen, bearbeitet Anfechtungen, erstellt Angebot | [@olgnuernberg2011u136910] |
| FR | Firma als Regelverantwortliche | Herstellerin, Entwurfsverfasserin nach Art. 61 Abs. 6 BayBO | pflegt Hausmodelle, Katalog, Herstellerregeln (Schicht S5) | [@baybo2026]; Kap. 9.3.3 |
| BV | bauvorlageberechtigte Person (Architekt, Listen-Ingenieur oder Zimmerermeister) | leitet die Entwurfsverfassung, Name auf den Bauvorlagen | gibt Regelraum und Bauvorlage frei, entscheidet Auslegungsparameter und freigabepflichtige Ergebnisse | Art. 61 BayBO; Kap. 9.2.3, 9a.4.1 |
| TW | Tragwerksplaner (Nachweisersteller Standsicherheit) | gelistet; Zimmerermeister nur mit Zusatzqualifikation und drei Jahren Berufserfahrung | erstellt und erklärt den Standsicherheitsnachweis | Art. 62, 62a BayBO; Recherche 27, Abschnitt 3 |
| FP | weitere Fachplaner (Energie, Schall, Brandschutz) | nachweisberechtigt je Fachgebiet | erstellen Fachnachweise aus dem Modell | Kap. 4.3.5, 4.5 |
| PS | Prüfsachverständiger | vom Bauherrn beauftragt; ab GK 4 für Standsicherheit, ab GK 5 für Brandschutz | prüft und bescheinigt | Kap. 9a.4.2, 9a.4.3 |
| WP | Werkplanung | Organisationseinheit der Firma | ergänzt ausführungsfertige Informationen, gibt Produktion frei | Kap. 3.4.1 |
| WK | Werk | Fertigung | erhält Fertigungspaket, meldet Fertigungsstand zurück | Kap. 3.2, 17 |
| MO | Montage und Bauleitung | Ausführung auf der Baustelle | Montagereihenfolge, Ist-Termine, Übergabe | Kap. 3.2.7, 14b |
| BA | Bauaufsichtsbehörde | Genehmigungsbehörde | erhält Bauvorlagen (PDF, IFC als Anlage) | [@bauvorlv; @dbauv2026] |
| GE | Gemeinde | Adressat der Freistellung (Art. 58 BayBO); Satzungsgeberin | erhält Unterlagen, kann Verfahren verlangen; liefert Satzungen und Bebauungsplan | Kap. 4.2, 4.3.4, 9a.3 |

Zwei Rollen fehlen in der Tabelle bewusst. Der **Nachbar** ist Betroffener, aber kein Nutzer: Er wird bei der Freistellung benachrichtigt und bei überschwenkendem Kran angezeigt (Beispiel 3.5). Das **System selbst** ist keine Rolle. Es schlägt vor, prüft und protokolliert, entscheidet aber nichts, was eine Rolle entscheiden muss. Diese Grenze ist Gegenstand von 6.4 und von Abschnitt 7.1.

### 6.1.3 Berechtigungsmatrix

Tabelle 6.2 ordnet den Rollen die wichtigsten Aktionen zu. „F“ bedeutet Freigabe mit Signatur, „Ä“ Ändern, „L“ Lesen, „–“ kein Zugriff. Die vollständige Matrix ist Konfiguration im Modul `freigabe` (Abschnitt 7.5).

**Tabelle 6.2: Berechtigungsmatrix (Ausschnitt)**

| Aktion | KU | VT | FR | BV | TW | WP | WK | BA/GE |
|---|---|---|---|---|---|---|---|---|
| Entwurf im Regelraum ändern | Ä | Ä | – | Ä | – | – | – | – |
| Regel der Schicht S1/S2 aussetzen | – | – | – | – | – | – | – | Behördenentscheidung |
| Herstellerregel (S5) aussetzen | – | – | F | F | – | – | – | – |
| Regelraum-Version freigeben (Gate G0) | – | – | Ä | F | – | – | – | – |
| Auslegungsparameter [U] festlegen | – | – | – | F | – | – | – | – |
| Baubeschreibung übergeben, Vertrag schließen (G1) | F | F | – | – | – | – | – | – |
| Ausstattungsfestlegung unterschreiben (G2) | F | L | – | – | – | L | – | – |
| Bauvorlage freigeben (G4) | L | L | – | F | L | – | – | – |
| Standsicherheitsnachweis erklären (G5) | L | – | – | L | F | L | – | – |
| Produktion freigeben (G7) | – | – | – | L | L | F | L | – |
| Fertigungspaket abrufen | – | – | – | – | – | L | L | – |
| Bauvorlagen empfangen | – | – | – | – | – | – | – | L |

Die Matrix setzt ANF-09-12 um: Weder Kunde noch Vertrieb können Regeln der Bauordnung aussetzen. Sie ergänzt ANF-09a-07, das die Reichweite nach dem Profil bestimmt, um die Reichweite nach der Qualifikation.

### 6.1.4 Wirksame Aufsicht statt Klick-Gate

Eine Freigabe, die nur aus einem Klick besteht, erfüllt die Form, aber nicht den Zweck. Green zeigt, dass menschliche Aufsicht über Algorithmen oft eine Scheinsicherung ist: Menschen erkennen Fehler schlecht, und die Aufsicht verschleiert die Verantwortung [@green2022flaws]. Sterz et al. nennen vier Bedingungen wirksamer Aufsicht: kausaler Einfluss, epistemischer Zugang, Selbstkontrolle und passende Absichten [@sterz2024quest]. Bainbridge hat schon 1983 beschrieben, dass Automatisierung dem Menschen gerade die schwierigen Ausnahmen überlässt, die er ohne Übung schlechter beherrscht [@bainbridge1983ironies].

Das deutsche Haftungsrecht hat dafür einen Maßstab. Wer ein übliches Rechenprogramm mit richtigen Eingaben nutzt, handelt zunächst sorgfaltsgemäß. Sobald Warnsignale vorliegen, muss er plausibilisieren oder gegenrechnen [@olgkoeln2017u9816] [V]. Wer eine fremde Planung fortführt, muss sie im Rahmen des Zumutbaren prüfen und dem Besteller Bedenken mitteilen [@bgh2026viizr11924] [V]. Wer als Unternehmer Planung übernimmt, kann sich nicht auf fehlende Fachkenntnis berufen [@olgkoeln2021u2320] [V, Leitsätze].

Das Gate „Bauvorlage“ ist deshalb eine **Übernahmeprüfung**. Es zeigt der freigebenden Person nicht den ganzen Entwurf, sondern eine Liste von Warnsignalen, und es ist erst abschließbar, wenn zu jedem Signal eine Reaktion protokolliert ist. Die Einteilung der Automatisierung in vier Funktionsklassen nach Parasuraman et al. liefert dafür das Raster [@parasuraman2000model]: Informationsaufnahme und Analyse übernimmt das System vollständig, die Entscheidung bleibt bei der Person, die Ausführung (Export, Einreichung) folgt ihr.

> **Beispiel 6.1 (Warnsignale im Gate „Bauvorlage“).** Das System markiert ein Ergebnis als grenzwertnah, wenn seine Ausnutzung η mindestens 0,95 beträgt (Designentscheidung E6.2). Die Nachweise der Beispiele liefern echte Werte:
>
> | Nachweis | Ergebnis | Ausnutzung η | Warnsignal |
> |---|---|---:|---|
> | B3 U-Wert, Geometrie verputzt | U = 0,187 W/(m²K) ≤ 0,20 | 0,93 | nein |
> | B5 Treppe, beste Lösung | 7 Kriterien erfüllt | 0,97 | **ja** |
> | B4 Abstandsfläche, Szenario „mittig“, Traufseite | T erforderlich 3,27 m, vorhanden 5,00 m | 0,65 | nein |
> | B4 Giebel, Lesart des Auslegungsparameters | „drittel“ 30,53 m² oder „voll“ 36,40 m² | – | **ja** (Status U, ANF-09-21) |
>
> Die Person sieht zwei Signale. Zur Treppe protokolliert sie etwa „plausibilisiert: Steigungsverhältnis 170,6/290 mm nachgerechnet“, zum Giebel legt sie die Lesart fest. Erst danach ist das Gate abschließbar. Das Protokoll dient zugleich der Evaluation der Gate-Wirksamkeit (Kapitel 20).

**E6.2 – Grenzwertnähe ab η ≥ 0,95 ist ein Pflicht-Warnsignal.** *Entscheidung.* Jedes Ergebnis mit Ausnutzung η ≥ 0,95, jedes Ergebnis mit Status [U], jedes freigabepflichtige Ergebnis, jede Angabe mit Herkunft „Kunde“ und jede Meldung Dritter erscheint im Gate als Warnsignal. Der Schwellwert ist Konfiguration. *Begründung.* Das OLG Köln knüpft die Pflicht zur Gegenrechnung an Warnsignale [@olgkoeln2017u9816]; der BGH sieht Grundstücksangaben des Auftraggebers als Angaben, auf deren Richtigkeit der Planer nur eingeschränkt vertrauen darf [@bgh2013viizr25711]. Nachweise, deren Abstand zum Grenzwert innerhalb der Unsicherheit liegt, markiert Abschnitt 7a.2 bereits als unsicher. *Beleg.* Der Wert 0,95 ist eine eigene Festlegung [U] und in der Nutzerstudie zu prüfen.

## 6.2 Funktionale Anforderungen je Phase

### 6.2.1 Phasenmodell

Die Prozesskette aus Abschnitt 3.4.1 hat neun Phasen. Für das System kommt eine vorgelagerte Phase hinzu: die Pflege des Regelraums, ohne die kein Kundenentwurf geprüft werden kann. Tabelle 6.3 ordnet jeder Phase ihr Freigabe-Gate, die vorhandenen Anforderungen und die neuen Anforderungen dieses Kapitels zu. Die Gates sind in Abschnitt 7.4 als Zustandsautomat beschrieben.

**Tabelle 6.3: Phasen, Gates und Anforderungen**

| Phase | Gate | vorhandene Anforderungen (Auswahl) | neu in Kapitel 6 |
|---|---|---|---|
| 0 Regelraum | G0 Regelraum | ANF-09-01, -05, -06, -10, -20; ANF-09a-10; ANF-09b-02, -18; ANF-03-05, -06; ANF-08-31 | ANF-06-02 |
| 1 Idee | – | ANF-08-26; ANF-09-02 | ANF-06-08, -09 |
| 2 Entwurf | – | ANF-09-13 bis -19, -22 bis -29; ANF-09a-01 bis -06, -11 bis -15, -18, -19; ANF-09b-01 bis -17; ANF-03-24 | ANF-06-10, -11 |
| 3 Angebot und Vertrag | G1 Vertrag | ANF-09a-09, -16; ANF-03-18 (Widerruf) | ANF-06-12, -13, -14 |
| 4 Bemusterung | G2 Ausstattung | ANF-03-19, -21, -22; ANF-08-16, -17; ANF-09-26 | ANF-06-15 |
| 5 Fachfreigabe | G3 Abweichung, G4 Bauvorlage, G5 Statik, G6 Brandschutz | ANF-09-18, -21; ANF-09a-05, -07, -08, -17; ANF-08-19 | ANF-06-01, -03 bis -07 |
| 6 Bauantrag oder Freistellung | – (Einreichung) | ANF-08-26 | ANF-06-16 bis -19 |
| 7 Werkplanung | – | ANF-03-01 bis -11, -15; ANF-08-07 bis -12, -21, -25, -29 | ANF-06-20 |
| 8 Fertigung | G7 Produktion | ANF-03-12 bis -14, -18; ANF-08-22 | ANF-06-21 |
| 9 Transport und Montage | – | ANF-03-16, -17, -20 | ANF-06-22 |
| 10 Übergabe | G8 Übergabe | – | ANF-06-23, -24 |

Die Tabelle zeigt ein deutliches Ungleichgewicht. Entwurf, Regelraum und Werkplanung sind dicht spezifiziert, weil die Fachkapitel dort ansetzen. Idee, Vertrag, Bauantrag und Übergabe hatten bisher fast keine eigenen Anforderungen, obwohl gerade dort die harten rechtlichen Bedingungen liegen. Die folgenden Abschnitte schließen diese Lücken.

### 6.2.2 Phase 0: Regelraum

Die Firma pflegt Hausmodelle, Bauteilkatalog und Herstellerregeln als Daten (Zielbild, Prinzip 5). Die Fachkapitel haben dafür das Nötige festgelegt: schema-valide Regeln (ANF-09-01), unveränderliche Profile mit Version (ANF-09-05), Monotonieprüfung beim Laden (ANF-09-10), Herstellerkennwerte mit Quelle und Konfliktstatus (ANF-03-05) und ein Mapping, das Konfiguration statt Code ist (ANF-08-31). Es fehlt die Verknüpfung mit der Verantwortung. Eine neue Version des Regelraums darf erst dann gegen Kundenentwürfe laufen, wenn die bauvorlageberechtigte Person sie freigegeben hat (**ANF-06-02**). Die Freigabe steht als `IfcApproval` an der `IfcProjectLibrary` und trägt eine qualifizierte elektronische Signatur (Recherche 27).

Diese Anforderung hat eine zweite Wirkung. Ist der Regelraum einmal freigegeben, sieht die Person im Gate „Bauvorlage“ nur noch die **Abweichungen** vom Regelraum (Zielbild 3.1, Schritt 5). Ohne G0 müsste sie jeden Entwurf vollständig prüfen, und die Arbeitsteilung des Zielbilds würde nicht entstehen.

### 6.2.3 Phase 1: Idee

Familie H. wählt ein Hausmodell und ihr Grundstück (Zielbild 3.1). Abschnitt 4.2 hat gezeigt, dass Hausumringe, Geländemodell und Luftbilder frei (CC BY 4.0) verfügbar sind, das Flurstück aus ALKIS aber etwa 2,90 € kostet und der Bebauungsplan in Bayern meist nur als PDF vorliegt [@opengeodataBY; @xplanung] [V]. Daraus folgen zwei Anforderungen:

- **ANF-06-08** verlangt, dass das Grundstück aus den freien Daten automatisch aufgebaut wird, das Flurstück mit Kostenhinweis abgerufen wird und die Festsetzungen des Bebauungsplans im Schema von XPlanGML stehen, auch wenn sie per Dialog oder PDF-Extraktion mit menschlicher Bestätigung befüllt werden. Fehlt eine Festsetzung, liefern die abhängigen Regeln **unbestimmt** (ANF-09-02).
- **ANF-06-09** verlangt, dass jede Angabe eine **Herkunft** trägt: Kunde, Amt oder Firma. Der BGH sieht Angaben des Auftraggebers zu Baugrund und Grundwasser als Angaben, deren Herkunft das Verschulden des Planers bestimmt [@bgh2013viizr25711] [V]. Das OLG Nürnberg hat einen Fertighaushersteller haften lassen, dessen Vertrieb auf die Angabe „Hang ca. 3 m“ geplant hatte [@olgnuernberg2011u136910] [V]. Angaben mit Herkunft „Kunde“ erscheinen deshalb im Gate als Warnsignal (E6.2).

### 6.2.4 Phase 2: Entwurf

Der Entwurf ist die am dichtesten spezifizierte Phase. Kapitel 9 legt die Regelprüfung, die Ablehnung mit Begründung und Alternative und die Solver fest, Kapitel 9a die Profilableitung, Kapitel 9b die Assistenz. Zwei Anforderungen fehlen noch.

**Eine Schnittstelle für alle Eingabewege (ANF-06-10).** Jede Änderung, ob gesprochen, getippt oder geklickt, wird zu demselben typisierten Intent und demselben Ereignis im Parametermodell (Abschnitt 7.3). Sprache ist nie der einzige Weg zu einer Funktion. Das hat drei Gründe. Erstens bevorzugen Nutzer bei Änderungen eines einzelnen Parameters den Schieberegler, Sprache lohnt sich vor allem für zusammengesetzte Änderungen [@chen2025agent]. Zweitens verlangt die Barrierefreiheit gleichwertige Zugänge (6.3.5). Drittens wird die Prüfung nur dann für alle Eingabewege gleich, wenn sie hinter einer gemeinsamen Schnittstelle liegt.

**Sofortige Rückmeldung der Folgen (ANF-06-11).** Das Zielbild verlangt, dass sich Kosten, Wohnfläche, H'T und Abstandsflächen nach jeder Änderung „sofort“ aktualisieren. Das ist nur für einen Teil der Kennwerte in Echtzeit möglich (6.3.3). Die Anforderung lautet deshalb: Jede Kennzahl trägt einen Status „aktuell“, „wird berechnet“ oder „unbestimmt“, und kein Wert wird angezeigt, der zu einem älteren Entwurfsstand gehört, ohne dass das sichtbar ist. Die Kosten nennt die Antwort aktiv, nicht nur in einer Anzeige; das übernimmt die Arbeit aus der Laienstudie von Puusepp et al. [@puusepp2017enabling] (Abschnitt 5.7.5).

> **Beispiel 6.2 (eine Änderung, vier Folgen).** Beispiel B6 verarbeitet den Satz „Mach das Bad oben zwei Meter sechzig breit“. Der Parser liest 2,60 m (Muster A), die Referenzauflösung findet das Bad im Obergeschoss (IfcSpace-GUID `1cRQfmv29HlfHiIPofgLWT`), die Regelprüfung nimmt die Änderung an und gleicht das Kinderzimmer 1 von 3,50 m auf 3,30 m aus. Der Satz „Mach das Kinderzimmer 1 einen Meter zwanzig schmaler“ wird dagegen abgelehnt, weil 2,30 m < 2,60 m und 7,82 m² < 10 m² wären. Nach ANF-06-11 zeigt die Antwort in beiden Fällen die Wohnfläche als „aktuell“, die Kosten als „aktuell“ oder „wird berechnet“ und H'T als „wird berechnet“, bis die Hintergrundprüfung fertig ist.

### 6.2.5 Phase 3: Angebot und Vertrag

Abschnitt 4.7 hat die harten Bedingungen des Verbraucherbauvertrags herausgearbeitet: Baubeschreibung mit neun Mindestinhalten nach Art. 249 § 2 EGBGB, Übergabe in Textform **vor** der Vertragserklärung, verbindlicher Fertigstellungstermin oder Bauzeit, 14 Tage Widerruf ab ordnungsgemäßer Belehrung [@bgb; @egbgb249] [V]. Offen war, ob die Pflicht zur Baubeschreibung entfällt, wenn der Kunde selbst entwirft. Die Gesetzesbegründung beantwortet das: Die Pflicht entfällt, wenn der Besteller oder ein von ihm Beauftragter, „beispielsweise ein Architekt“, die wesentlichen Planungsvorgaben macht [@bundestag2016bauvertrag] [V]. Ein Laienentwurf im Regelraum der Firma ist kein solcher Fall, denn den Regelraum stellt die Firma (Recherche 27). Die Pflicht bleibt.

Daraus folgen drei neue Anforderungen:

- **ANF-06-12**: Die Baubeschreibung ist eine Sicht auf das Modell. Sie wird gegen die Regel `DE.EGBGB249.Baubeschreibung` geprüft. Das Gate G1 lässt die Vertragserklärung erst zu, wenn die Übergabe in Textform mit Zeitstempel protokolliert ist.
- **ANF-06-13**: Mit der Vertragserklärung wird ein Vertragsstand eingefroren: IFC-Revision, Baubeschreibung und Preis mit SHA-256. Jede spätere Änderung ist eine neue Revision und ein Nachtrag. Die Widerrufsfrist berechnet ANF-03-18 bereits.
- **ANF-06-14** (Soll): Das Angebot entsteht aus `IfcCostSchedule` mit Preisgültigkeit und wird als GAEB exportiert (Zielbild 3.2).

Wird ein Prüfsachverständiger erforderlich, nennt die Baubeschreibung Beauftragung, Kosten und Termine (ANF-09a-09). Bei aktivem Gebäudetyp E entsteht die Aufklärung in Textform (ANF-09a-16).

### 6.2.6 Phase 4: Bemusterung

Die Bemusterung ist ein Fertigungs-Gate (Abschnitt 3.4.2). Die Freeze-Kategorien, der Nachtrag nach dem Freeze und die Mehrpreisformel sind in ANF-03-19 bis -22 festgelegt, die Typzuordnung in der Projektbibliothek in ANF-08-17. Es fehlt das Gate selbst als Datensatz. **ANF-06-15** verlangt, dass die Ausstattungsfestlegung als eigenes Dokument mit Hash und Unterschrift des Kunden entsteht (G2) und dass ihr Datum den Termin „Montage frühestens 12 Wochen danach“ auslöst [@regnauerBLB2024] [V], den ANF-03-20 rückwärts rechnet.

### 6.2.7 Phase 5: Fachfreigabe

Die Fachfreigabe ist der Kern der Verantwortungsfrage (FF4). Fünf neue Anforderungen setzen die Befunde aus 6.1 um:

- **ANF-06-01** führt das Rollenmodell mit Qualifikationsnachweis ein (Tabelle 6.1 und 6.2).
- **ANF-06-03** macht das Gate „Bauvorlage“ zur Übernahmeprüfung mit Pflichtliste der Warnsignale (E6.2). Es prüft ausdrücklich auch, was im Freistellungsverfahren keine Behörde prüft. Der BGH sieht im vereinfachten Verfahren einen Abbau staatlicher Aufsicht bei „bewusster Verstärkung der Verantwortlichkeit“ der Beteiligten [@bgh2001viizr39199] [V].
- **ANF-06-04** prüft im Gate „Statik“ die Qualifikation des Nachweiserstellers. Ein Zimmerermeister darf den Standsicherheitsnachweis nur mit Zusatzqualifikation und drei Jahren Berufserfahrung erstellen (Art. 62a Abs. 1 Nr. 2 a BayBO) [@baybo2026] [V, Recherche 27].
- **ANF-06-05** führt ein **Abweichungs-Gate** ein. Wünscht der Kunde etwas außerhalb des Regelraums, etwa eine Befreiung vom Bebauungsplan, trägt er das Risiko nur nach umfassender, dokumentierter Aufklärung [@bgh2011viizr810; @bgh2023viizr21622] [V].
- **ANF-06-06** verbietet die automatische Letztentscheidung. Die Datenschutzkonferenz verlangt „keine automatisierte Letztentscheidung“ [@dsk2024ki] [V]. Nach dem EuGH ist eine automatisierte Bewertung schon dann eine Entscheidung im Sinne von Art. 22 DSGVO, wenn ein Vertragsschluss maßgeblich von ihr abhängt [@eugh2023schufa] [V]. Jede Ablehnung, die den Vertrag verhindert, bietet deshalb einen menschlichen Prüfweg.
- **ANF-06-07** (Soll) macht die Wirksamkeit der Aufsicht messbar: Verweildauer, geöffnete Nachweise und Reaktionen je Warnsignal.

### 6.2.8 Phase 6: Bauantrag oder Freistellung

Abschnitt 4.3.6 hat die Form der Einreichung festgelegt: Lageplan mindestens 1 : 1000 mit Abstandsflächen, Bauzeichnungen 1 : 100, Baubeschreibung mit Gebäudeklasse und Baukosten, Übereinstimmung aller Vorlagen untereinander (§§ 7–9, 13 BauVorlV) [@bauvorlv] [V]. Eingereicht wird als PDF über das BayernPortal; das IFC geht nur als Anlage mit [@dbauv2026] [V]. Nach dem Gesetzentwurf vom 21.07.2026 genügt künftig der Name der Person im Beschriftungsfeld, ausdrücklich „ohne Schriftformersatz wie etwa eine qualifizierte elektronische Signatur“ [@bayDigitalisierungEntwurf2026] [V, Entwurf]. Standsicherheits- und Brandschutznachweis bleiben unter der DBauV ein elektronisches Abbild des unterschriebenen Originals (§ 11 Abs. 4 DBauV) [@dbauv2026] [V].

Die neuen Anforderungen:

- **ANF-06-16**: Die Bauvorlagen entstehen vollständig aus einer freigegebenen Revision. Der Name der bauvorlageberechtigten Person steht automatisch im Plankopf, übernommen aus dem `IfcApproval` des Gates G4. Wird die Freigabe ungültig, sperrt der Export.
- **ANF-06-17**: Die Übereinstimmung nach § 13 BauVorlV wird maschinell belegt: Jede Vorlage trägt den Hash derselben Revision. Kapitel 4 hat gezeigt, dass ein System mit einer einzigen Quelle diese Forderung konstruktionsbedingt erfüllt. Die Anforderung macht daraus einen Test.
- **ANF-06-18**: Das System bestimmt Verfahren und Adressaten (Gemeinde bei Freistellung, Bauaufsicht sonst) und führt die Fristen: Freistellung ein Monat, Erklärung zur Standsicherheit spätestens mit der Baubeginnsanzeige (§ 15 BauVorlV).
- **ANF-06-19** (Soll): Die Formulardaten für BayernPortal bzw. XBau werden erzeugt, das IFC als Anlage beigefügt.

### 6.2.9 Phasen 7 bis 10: Werkplanung, Fertigung, Montage, Übergabe

Werkplanung und Fertigung sind in Kapitel 3 und 8 dicht spezifiziert. Drei Lücken bleiben.

**Keine Neumodellierung (ANF-06-20).** Erfolgskriterium 2 des Zielbilds lautet: „Zwischen Vertrag und Werk wird null Mal neu modelliert oder abgetippt.“ Das ist nur prüfbar, wenn die Werkplanung auf demselben Parametermodell arbeitet und ihre Ergänzungen als Ereignisse mit der Rolle WP einbringt. Jede IFC-Revision nach Vertrag muss aus gen(*x*) entstehen (Abschnitt 9.2.1). Ein Import fremder Geometrie ist nur für Produktgeometrie der Hersteller zulässig (E8.22).

**Fertigungspaket (ANF-06-21).** Die Produktionsfreigabe (ANF-03-18) erzeugt ein unveränderliches Paket: IFC-Revision, BTLx, WUP oder dessen Adapter-Meldung (ANF-03-14), `export_guid.csv` (ANF-08-22) und Stückliste, mit Hash und dem qualifizierten Siegel der Firma. Das Werk nimmt nur Pakete mit gültiger Freigabe an.

**Montage und Übergabe (ANF-06-22 bis -24).** Montage-Ist-Termine und Abweichungen fließen als Ereignisse zurück (Soll). Die Hausakte, nach QDF Pflicht [@qdf2022] [V], ist die letzte freigegebene Revision mit allen Nachweisheften, Dokumenten und einem Auszug des Audit-Trails. Sie muss ohne die App prüfbar sein, also in offenen Formaten (IFC, PDF, JSON) und mit einem Beweiswerterhaltungsnachweis (6.3.7). `IfcAsset` und `Pset_Warranty` tragen Wartung und Gewährleistung (Soll, Zielbild 3.2).

## 6.3 Nichtfunktionale Anforderungen

Nichtfunktionale Anforderungen beschreiben Eigenschaften des ganzen Systems, nicht einzelner Funktionen. Für diese Arbeit sind neun maßgeblich. Sie treiben die Architektur in Kapitel 7 stärker als jede einzelne Funktion.

### 6.3.1 Standardkonformität

„Standardkonform“ ist in Kapitel 8 als Prüfkette definiert, nicht als Erfüllung einer MVD (E8.2): Schema und EXPRESS-Regeln (K1), buildingSMART Validation Service (K2), IDS je Gate und Reifegrad (K3) und die Regelmaschine mit Nachweisen (K4) [@bsi2025validation; @bsi2024ids; @iso2024ifc]. ANF-08-01 bis -06 und ANF-09-18 legen die Stufen fest. Neu ist nur eine Verknüpfung: **ANF-06-25** verlangt, dass das Prüfprotokoll zu genau der Revision gehört, die freigegeben wird. Ein Protokoll mit anderem Hash gilt nicht. Der Grund ist trivial und wird trotzdem oft verletzt: Zwischen Prüfung und Freigabe darf sich nichts ändern.

### 6.3.2 Determinismus und Reproduzierbarkeit

Der Generator ist bereits deterministisch spezifiziert: byte-identische Dateien bei gleicher Eingabe, auch unter verschiedenen Hash-Seeds (ANF-08-24, E8.28), stabile GlobalIds (ANF-08-23). B1 erfüllt das mit SHA-256 `5a796ea7…f8bb478b` [V]. Kapitel 7a hat dasselbe für Nachweise gezeigt, sofern eine Zahlen-Normalform gilt: 32 von 32 Nachweis-Hashes stimmen nach der Korrektur überein [V].

Zwei Lücken bleiben. Erstens ist bisher nur der Generator deterministisch, nicht der ganze Durchlauf. Ein Projekt besteht aus einer Folge von Ereignissen: Intents, Bemusterungsentscheidungen, Freigaben. **ANF-06-26** verlangt, dass die Wiederholung dieser Folge dieselben IFC-Revisionen, Nachweise und Exporte ergibt. Die Intent-Erkennung ist dabei ausgenommen, weil ihr Ergebnis als Ereignis gespeichert und beim Wiederholen nicht neu berechnet wird (Abschnitt 7.3).

Zweitens ist Reproduzierbarkeit eine Frage der Zeit. Ein Nachweis, der in zehn Jahren im Streit geprüft wird, muss mit der damaligen Software nachrechenbar sein. Die Software Citation Principles verlangen, die konkret verwendete Version identifizierbar zu machen [@smith2016softwarecitation]; die FAIR-Prinzipien für Forschungssoftware übertragen Auffindbarkeit und Wiederverwendbarkeit auf Software [@barker2022fair4rs]. **ANF-06-27** verlangt deshalb, dass jede Revision die Kennung einer archivierten Laufzeitumgebung trägt, aus der sie byte-identisch neu erzeugt werden kann.

### 6.3.3 Latenz der Sprachschleife

Die Sprachschleife ist die Zeit vom Ende einer Äußerung bis zur sichtbaren Antwort des Systems. Die Literatur liefert Teilwerte, aber kein Gesamtbudget für diesen Anwendungsfall. Die folgende Rechnung setzt es aus gemessenen und veröffentlichten Werten zusammen.

> **Beispiel 6.3 (Latenzbudget der Sprachschleife).** Werte je Stufe, gemessen oder aus Recherche 03:
>
> | Stufe | Wert | Herkunft | Budget (p95) |
> |---|---|---|---:|
> | Spracherkennung Voxtral Mini 4B Realtime | Wortfehlerrate Deutsch 6,19 % bei 480 ms Verzögerung | Model Card, Recherche 03 [V] | 500 ms |
> | Intent-Modell Laya | etwa 7 ms je Frage bei 10 Fragen auf einer T4 | Model Card, Recherche 03 [V] | 150 ms (zwei Hierarchiestufen) |
> | Werteparser, Referenzauflösung, Raumregeln (B6) | Median 0,125 ms, p95 0,229 ms, Maximum 0,972 ms bei 450 Aufrufen | eigene Messung, 27.09.2026 [V] | 50 ms |
> | lokale R1-Regeln: Abstandsflächen (B4), Treppe (B5) | 0,60 ms je Szenario bzw. 0,56 ms für 68 Lösungen (Median) | eigene Messung [V] | 300 ms |
> | IFC-Neuerzeugung eines Wandelements (B1) | Median 0,131 s (n = 5; 0,118–0,323 s) | eigene Messung [V] | 200 ms |
> | Darstellung im Browser | nicht gemessen | – [U] | 300 ms |
> | **Summe** | | | **1 500 ms** |
>
> Messumgebung: Python 3.11.15, IfcOpenShell 0.8.5, x86_64 mit 4 Kernen, ohne GPU. Nicht im Budget liegt die Schemaprüfung: `ifcopenshell.validate` mit EXPRESS-Regeln brauchte für das Wandelement B1 3,66 s bei 0 Meldungen [V]. Für ein ganzes Haus mit vielen Elementen ist ein Vielfaches zu erwarten [U].

Aus der Rechnung folgen zwei Anforderungen und eine Entscheidung.

**E6.3 – Das Latenzbudget der Sprachschleife beträgt 1,5 s im 95. Perzentil für lokale Änderungen.** *Entscheidung.* Vom Ende der Äußerung bis zur Antwort mit Annahme, Ablehnung oder Rückfrage vergehen höchstens 1,5 s (p95), gemessen an einem festen Satz von Referenzäußerungen. Die Teilbudgets der Tabelle sind Richtwerte. *Begründung.* Die deterministischen Teile liegen um drei Größenordnungen unter ihrem Budget, die IFC-Erzeugung eines Elements knapp darunter. Das Budget wird also von Spracherkennung und Darstellung bestimmt, nicht von Regelprüfung und Rechnung. Kritik während des Entwerfens statt nachträglicher Stapelkritik setzt eine solche Rückmeldung voraus [@silverman1992critiquing] (Abschnitt 9b.7.2). *Beleg.* Der Wert 1,5 s ist eine eigene Festlegung [U]; die Nutzerstudie in Kapitel 20 prüft, ob er für Laien genügt.

**ANF-06-28** macht das Budget zur Abnahme. **ANF-06-29** trennt den synchronen vom asynchronen Pfad: Prüfungen, die das Budget sprengen, laufen im Hintergrund, und ihr Ergebnis ist bis dahin **unbestimmt**. Das entspricht der Arbeitsregel aus Abschnitt 9.6.3, nach der Energiebilanz, vollständiger Schallnachweis und Tragwerksvorbemessung in die Hintergrundprüfung gehören. Eine Freigabe ist erst möglich, wenn alle Hintergrundprüfungen der Revision abgeschlossen sind.

### 6.3.4 Datenschutz

Sprachaufnahmen sind personenbezogene Daten (Abschnitt 4.8.3). Drei Quellen konkretisieren, was daraus folgt. Nach den Leitlinien des Europäischen Datenschutzausschusses zu Sprachassistenten ist die Speicherung zu begrenzen, versehentliche Aufnahmen sind zu löschen, und Stimmdaten sind nur dann biometrisch, wenn sie zur Identifizierung verarbeitet werden [@edpb2021vva] [V]. Die Datenschutzkonferenz verlangt datenschutzfreundliche Voreinstellungen ohne Training mit Eingaben und ohne Eingabehistorie sowie eine Datenschutz-Folgenabschätzung [@dsk2024ki] [V]; ihre Orientierungshilfe zu technischen und organisatorischen Maßnahmen gibt eine Checkliste je Lebensphase eines KI-Systems [@dsk2025kitom]. Der Zugriff auf das Mikrofon über App und Browser richtet sich nach § 25 TDDDG [@tdddg25] [V].

Die Anforderungen:

- **ANF-06-30**: Die Spracherkennung läuft standardmäßig lokal. Rohaudio wird nicht über die Sitzung hinaus gespeichert. Es gibt keine Sprechererkennung, damit keine biometrischen Daten entstehen. Ein Cloud-Fallback (Jev, Abschnitt 7.7) ist nur nach Einwilligung und nur mit Zero Data Retention zulässig. Ins Audit gehen Intent, Parameter und Ergebnis, nicht das Transkript.
- **ANF-06-31**: Beratungsgespräche mit dem Vertrieb werden nur mit Einwilligung aller Beteiligten aufgezeichnet. Die unbefugte Aufnahme des nichtöffentlich gesprochenen Wortes ist strafbar (§ 201 StGB) [@stgb201] [V].
- **ANF-06-32**: Vor dem Betrieb liegen Datenschutz-Folgenabschätzung und Verarbeitungsverzeichnis vor.

Hinzu kommen die bereits festgelegten Anforderungen: Das Geburtsdatum für die Kua-Zahl wird nicht gespeichert (ANF-09b-13), und ob ein aktives Vastu-Profil ein Hinweis auf religiöse Überzeugungen im Sinne von Art. 9 DSGVO ist, bleibt rechtlich zu prüfen (Abschnitt 9b.7.5) [U].

### 6.3.5 Barrierefreiheit

Das Barrierefreiheitsstärkungsgesetz ist seit dem 28.06.2025 anwendbar [@bfsg] [V]. Es erfasst Dienstleistungen im elektronischen Geschäftsverkehr, die zum Abschluss eines Verbrauchervertrags führen. Führt die App zum Vertragsschluss, fällt sie sehr wahrscheinlich darunter (Abschnitt 4.8.3) [U]. Als Prüfmaßstab nennt Recherche 07 die EN 301 549 [U, Normtext nicht eingesehen].

Für einen 3D-Editor ist das eine eigene Gestaltungsaufgabe. Ein Grundriss, der nur als Bild existiert, ist für blinde Nutzer nicht zugänglich. Das Informationsmodell hilft hier: Jeder Raum ist ein `IfcSpace` mit Name, Fläche und Nachbarschaft, jede Regelprüfung ein Nachweis mit Text. Daraus lässt sich eine gleichwertige nicht-visuelle Sicht erzeugen: Raumliste, Nachbarschaftstabelle, Kennzahlen, Meldungen. Die Sprachsteuerung selbst kann zum Mittel der Barrierefreiheit werden. Elghaish et al. haben einen Sprachassistenten für BIM-Daten ausdrücklich für Nutzer mit Behinderung gebaut [@elghaish2022voice]. Sprache darf aber nicht der einzige Weg sein, denn sie schließt Nutzer mit Sprech- oder Hörbeeinträchtigung aus. Die Interaktionsprinzipien der ISO 9241-110, darunter Steuerbarkeit, Erwartungskonformität und Robustheit gegen Benutzungsfehler, geben die Prüfkriterien für Dialog, Rückfrage und Ablehnung [@iso2020interaction].

**ANF-06-33** verlangt deshalb: Alle Funktionen, die zum Vertragsschluss führen, sind nach EN 301 549 barrierefrei; der 3D-Editor hat eine gleichwertige nicht-visuelle Sicht; jede Funktion ist per Tastatur, per Sprache und per Zeigegerät erreichbar (vgl. ANF-06-10); Status wird nie nur durch Farbe codiert (Abschnitt 7a.4).

### 6.3.6 KI-Transparenz nach Art. 50 KI-VO

Gebäudeentwurf ist keine Hochrisiko-Anwendung. Weder Anhang III noch Anhang I der KI-Verordnung erfassen ihn; die Bauprodukteverordnung steht nicht in Anhang I Abschnitt A [@aiact2024] [V, Recherche 27]. Es bleiben die Transparenzpflicht nach Art. 50 und die Pflicht zu Maßnahmen der KI-Kompetenz nach Art. 4, die der Digital Omnibus abgeschwächt hat [@eu2026omnibus] [V]. Nach derselben Verordnung gilt die Kennzeichnungspflicht des Art. 50 Abs. 2 für bestehende Systeme ab dem 02.12.2026 [V].

Wichtiger als die Pflicht selbst ist die Frage, **welche Komponente** ein KI-System ist. Die Leitlinien der Kommission nehmen Systeme mit ausschließlich von Menschen definierten Regeln aus der Definition aus, nicht aber logik- und wissensbasierte Inferenz [@eu2025aidefinition] [V]. Recherche 27 folgert: Die deterministische Regelmaschine ist voraussichtlich kein KI-System, das Intent-Modell sicher eines. Private Anbieter erhalten von der Bundesnetzagentur keine amtliche Einstufung [@kimig2026] [V] und müssen die Grenze selbst dokumentieren.

Die Anforderungen:

- **ANF-06-34**: Vor der ersten Spracheingabe und dauerhaft sichtbar weist die App darauf hin, dass ein KI-System die Absicht erkennt. Jede Antwort zeigt, welcher Teil vom Intent-Modell stammt (erkannte Absicht mit Wahrscheinlichkeit) und welcher vom Code (Werte, Regeln, Kosten).
- **ANF-06-35**: Die Architektur dokumentiert, welche Komponenten KI-Systeme sind. Ein automatischer Test stellt sicher, dass kein Ausgabewert des Intent-Modells ohne deterministischen Parser und Regelprüfung in das Parametermodell gelangt. Diese Anforderung ist das technische Gegenstück zu „Die KI versteht, der Code entscheidet“ (Abschnitt 7.1).

### 6.3.7 Audit-Trail, Produkthaftung und Beweisvorsorge

Mit der Umsetzung der Produkthaftungsrichtlinie wird Software ab dem 09.12.2026 ein Produkt [@prodhaftg2026; @eu2024produkthaftungsrl] [V für die Richtlinie; U für die Verkündung des Gesetzes]. Nach Recherche 27 haftet die Firma aber vor allem aus Werkvertrag. Die Produkthaftung ersetzt nur Personen-, Sach- und Datenschäden, nicht den typischen reinen Vermögensschaden eines Planungsfehlers [@eu2024produkthaftungsrl]. Für den Audit-Trail ist die Frage deshalb weniger, welches Haftungsregime gilt, als wie die Firma im Streit beweist, was geschehen ist.

Ein automatischer Prüfbericht ist vor Gericht qualifizierter Parteivortrag in freier Beweiswürdigung [@bgh1993vizr24392; @olgnuernberg2021u113921] [V]. Besondere Beweiskraft hat nur ein privates Dokument mit qualifizierter elektronischer Signatur einer natürlichen Person (§ 371a ZPO) [@zpo371a] [V]. Das qualifizierte Siegel der Firma begründet die Vermutung von Integrität und Herkunft, der qualifizierte Zeitstempel die Vermutung von Datum und Integrität (Art. 35, 41 eIDAS) [@eu2014eidas] [V]. Die Expertengruppe der Kommission hat „logging by design“ als Herstellerpflicht vorgeschlagen; fehlen die Aufzeichnungen, soll sich die Beweislast umkehren [@expertgroup2019liability] [V]. Für die Langzeitaufbewahrung beschreibt die Technische Richtlinie TR-ESOR Evidence Records über Hashbäume; ohne Erneuerung entfällt nur die besondere Beweiskraft nach § 371a ZPO, nicht jeder Beweiswert [@bsi2022tresor] [V]. Das Vertrauensdienstegesetz regelt die Erneuerung von Signaturen, Siegeln und Zeitstempeln (§ 15 VDG) [@vdg2017] [V].

Die Anforderungen:

- **ANF-06-36**: Jedes Ereignis (Änderung, Prüfung, Ablehnung, Empfehlung, Freigabe, Export) wird in einem nur anhängbaren, hashverketteten Protokoll gespeichert. Jede nachträgliche Änderung eines Eintrags ist erkennbar.
- **ANF-06-37**: Nachweishefte und Freigaben tragen ein qualifiziertes Siegel der Firma und einen qualifizierten Zeitstempel. Die qualifizierte elektronische Signatur der Person gehört an das Gate, nicht an jeden Bericht. Die Hausakte erhält einen Beweiswerterhaltungsnachweis nach TR-ESOR.

Eine Blockchain ist dafür nicht nötig. Der Entscheidungsrahmen von Hunhevicz und Hall koppelt die Wahl verteilter Ledger an Merkmale des Anwendungsfalls [@hunhevicz2020need]. Hat ein Hersteller eine eigene, vertrauenswürdige Datenhaltung, genügen Hashkette, Zeitstempel und Signatur (Abschnitt 7.3).

### 6.3.8 Offline-Fähigkeit

Beratung findet im Musterhaus, im Bauherrenzentrum und auf dem Grundstück statt. Nicht überall ist eine Netzverbindung verlässlich [U, von Regnauer zu bestätigen: DAT-06-07]. Die Architektur des Zielbilds kommt dem entgegen: Laya läuft lokal, Jev ist nur Fallback, und das Vorbild Shapeshift nutzt offline einen Stichwort-Klassifikator (Recherche 03) [V].

**E6.4 – Der Entwurfskern ist offline-fähig, die Verantwortungskette nicht.** *Entscheidung.* Ohne Netz funktionieren Entwurf, Sprachschleife, lokale R1-Regeln, Nachweise, Schemaprüfung (K1) und IDS (K3). Nicht offline verfügbar sind Abrufe amtlicher Daten (ALKIS, PVGIS, Lärmkarten), der Validation Service als externer Dienst (K2), der Cloud-Fallback und alle Signaturen. Freigaben sind nur online möglich. *Begründung.* Eine Freigabe ohne Zeitstempel und Signatur hätte nicht den Beweiswert, den 6.3.7 verlangt. Der Entwurf dagegen ist eine Vorleistung ohne Rechtswirkung und kann später synchronisiert und vollständig nachgeprüft werden. Den Validation Service kann die Firma lokal aus dem offenen Quellcode betreiben (ANF-08-03) [@bsi2025validation]. *Beleg.* Recherche 03 [V] für die lokalen Modelle; Offline-Bedarf beim Praxispartner [U].

**ANF-06-38** setzt E6.4 als Testfall um.

### 6.3.9 Nachweisbarkeit und Gebrauchstauglichkeit

Kapitel 7a hat acht Anforderungen A1–A8 an jeden Nachweis hergeleitet, aber nicht als ANF nummeriert. **ANF-06-40** führt sie in den Katalog: Jeder Nachweis validiert gegen `nachweis.schema.json` und erfüllt A1–A8. **ANF-06-39** (Soll) macht Erfolgskriterium 1 des Zielbilds messbar. Gebrauchstauglichkeit ist nach ISO 9241-11 das Ausmaß, in dem Nutzer ihre Ziele effektiv, effizient und zufriedenstellend erreichen [@iso2018usability]. Die Nutzerstudie misst deshalb Aufgabenerfolg („zulässiger, kalkulierter Entwurf ohne Mitarbeiter“), Zeit und Zufriedenheit, und zusätzlich die Baubarkeit des Ergebnisses. Abschnitt 5.7.6 hat gezeigt, dass keine vergleichbare Arbeit Laienevaluation und Baubarkeit zusammen misst.

## 6.4 Harte Grenzen aus Recht und Norm

Harte Grenzen sind Bedingungen, die das System nicht durch bessere Technik überwinden kann. Sie unterscheiden sich von R1-Regeln: Eine R1-Regel begrenzt den Entwurf, eine harte Grenze begrenzt das **System**. Tabelle 6.4 führt sie aus Zielbild (Abschnitt 5), Kapitel 4, Kapitel 9a und den Recherchen 07 und 27 zusammen.

**Tabelle 6.4: Harte Grenzen**

| Nr. | Grenze | Grundlage | Wirkung im System | Anforderung | Status |
|---|---|---|---|---|---|
| HG-1 | Ohne namentlich benannte bauvorlageberechtigte Person kein Bauantrag | Art. 61 Abs. 6, Art. 64 BayBO [@baybo2026] | Gate G4 sperrt Export der Bauvorlagen | ANF-06-16, ANF-09a-07 | [V] |
| HG-2 | „Unter der Leitung“ verlangt Einflussmöglichkeit | [@ikbaunrw2024unterzeichnung; @byak2020berufsordnung; @bverfg1970bvr11765] | Gate G0: die Person gibt jede Regelraum-Version frei | ANF-06-02 | [V]; in Bayern nicht kommentiert geprüft [U] |
| HG-3 | Kleine Bauvorlageberechtigung nur für freistehende oder einseitig angebaute Wohngebäude GK 1–3 mit höchstens drei Wohnungen | Art. 61 Abs. 3 BayBO | Berechtigungsreichweite je Profil | ANF-09a-07 | [V] |
| HG-4 | Standsicherheitsnachweis nur durch gelistete Personen; Zimmerermeister nur mit Zusatzqualifikation | Art. 62, 62a BayBO | Gate G5 prüft Qualifikation | ANF-06-04 | [V] |
| HG-5 | Prüfsachverständige ab GK 4 (Standsicherheit) bzw. GK 5 (Brandschutz); Beauftragung durch den Bauherrn | Art. 62a, 62b BayBO | Gate G5/G6 nach Profil; Pflichtangabe in der Baubeschreibung | ANF-09a-08, -09 | [V] |
| HG-6 | Bauvorlagen als PDF, IFC nur Anlage; Nachweise als Abbild des unterschriebenen Originals | [@bauvorlv; @dbauv2026] | Bauvorlagen sind Ableitungen; Statik-Gate braucht Original | ANF-06-16, -19 | [V] |
| HG-7 | Baubeschreibung mit neun Mindestinhalten in Textform vor der Vertragserklärung; Ausnahme greift beim Laienentwurf nicht | § 650j BGB, Art. 249 § 2 EGBGB [@bgb; @egbgb249; @bundestag2016bauvertrag] | Gate G1 | ANF-06-12 | [V] |
| HG-8 | 14 Tage Widerruf ab ordnungsgemäßer Belehrung | § 650l BGB | Produktion erst nach Fristablauf | ANF-03-18, ANF-06-13 | [V] |
| HG-9 | Produktion erst nach Genehmigung bzw. Ablauf der Freistellungsfrist | Art. 58 BayBO | Gate G7 | ANF-03-18 | [V] |
| HG-10 | Keine automatisierte Letztentscheidung, wenn der Vertrag davon abhängt | Art. 22 DSGVO [@eugh2023schufa; @dsk2024ki] | menschlicher Prüfweg bei jeder Ablehnung | ANF-06-06 | [V] |
| HG-11 | Abweichung vom Regelraum nur nach dokumentierter Aufklärung | [@bgh2011viizr810; @bgh2023viizr21622] | Abweichungs-Gate G3 | ANF-06-05 | [V] |
| HG-12 | Bauordnungsrecht nicht durch Kunde oder Vertrieb lockerbar | Schichtung S1/S2, Kap. 9.3.3 | Aussetzen nur durch Behördenentscheidung | ANF-09-12 | [V] |
| HG-13 | Normtexte und Tabellen sind geschützt | § 5 Abs. 3 UrhG [@urhg5] | nur Einzelkennwerte mit Fundstelle; Lizenz DIN Media für Betrieb | ANF-09-20 | [V] Norm; [U] Reichweite |
| HG-14 | Maschinen lesen kein IFC; WUP ist proprietär | Recherche 01; [@btlx23] | BTLx, WUP als Ableitung; WUP-Adapter bricht ohne Spezifikation ab | ANF-03-14 | [V] |
| HG-15 | Interne Daten des Herstellers sind nicht öffentlich | Kap. 3.5.4 | Platzhalter mit Status [U] bis zur Lieferung | ANF-03-23; DAT-01 bis -15 | [V] |
| HG-16 | Hinweis auf KI-Interaktion | Art. 50 KI-VO [@aiact2024; @eu2026omnibus] | Hinweis und Kennzeichnung | ANF-06-34 | [V] |
| HG-17 | Aufzeichnung von Gesprächen nur mit Einwilligung aller | § 201 StGB [@stgb201] | Mehrpersonen-Einwilligung | ANF-06-31 | [V] |
| HG-18 | Barrierefreiheit bei Diensten zum Verbrauchervertrag | [@bfsg] | nicht-visuelle Sicht, mehrere Eingabewege | ANF-06-33 | [V] Gesetz; [U] Anwendbarkeit |
| HG-19 | Typengenehmigung ersetzt den bautechnischen Nachweis, nicht das Verfahren; Bebauungsplan und Abstandsflächen bleiben | Art. 73a BayBO [@landtagby2020baybonovelle; @landtagby2024modernisierung] | Profil *T*, Regeln des Bebauungsplans bleiben aktiv | ANF-09a-17 | [V] |
| HG-20 | Brennbare Dämmstoffe in GK 4/5 nur nach HolzBauRL | [@holzbaurl2024] | Katalogfilter | ANF-09a-14, ANF-03-08 | [V] |

Aus der Tabelle lässt sich eine kurze Liste dessen ableiten, was das System **nie** tut. Sie ist als Negativtest in der Prüfsuite zu führen:

1. Es reicht keinen Bauantrag ohne gültige Freigabe G4 ein.
2. Es gibt keine Produktion frei, solange Widerrufsfrist, Freistellungsfrist oder Genehmigung ausstehen.
3. Es lässt keinen Vertragsschluss zu, bevor die vollständige Baubeschreibung in Textform übergeben ist.
4. Es setzt keine Regel der Schichten S1 oder S2 aus.
5. Es trifft keine endgültige Ablehnung ohne menschlichen Prüfweg.
6. Es schreibt keinen Wert in das Modell, den nur ein Sprachmodell erzeugt hat.
7. Es kopiert keinen Normtext und keine Normtabelle.
8. Es speichert kein Rohaudio über die Sitzung hinaus.

Die Punkte 1, 2, 3 und 5 sind zusammen mit den Gates G0 und G3 als R3- und R4-Regeln in `spezifikation/regelkatalog-06.yaml` formalisiert. Punkt 4 setzt ANF-09-12 um, Punkt 6 ist Gegenstand von Abschnitt 7.1, Punkt 7 von Abschnitt 9.7, Punkt 8 von 6.3.4.

## 6.5 Konsolidierung des Anforderungskatalogs

### 6.5.1 Umfang

Der konsolidierte Katalog umfasst die 122 vorhandenen Anforderungen, 40 neue Anforderungen aus diesem Kapitel und 23 aus Kapitel 7, zusammen 185. Ein Skript extrahiert sie aus den Markdown-Tabellen der Kapitel und schreibt `spezifikation/anforderungen.csv` (6.7.4). Die Spalten Modul und Test sind vorläufig. Sie werden in Kapitel 23 zur Rückverfolgbarkeitsmatrix ausgebaut.

**Tabelle 6.5: Anforderungen nach Kapitel**

| Kapitel | Muss | Soll | Summe | Schwerpunkt |
|---|---:|---:|---:|---|
| 3 Holzrahmenbau | 20 | 5 | 25 | Bauteilmodell, Fertigung, Transport, Prozess |
| 6 Anforderungen | 34 | 6 | 40 | Rollen, Phasen, nichtfunktionale Anforderungen |
| 7 Systemarchitektur | 21 | 2 | 23 | Schnittstellen, Versionierung, Lizenzen |
| 8 Informationsmodell | 27 | 4 | 31 | Schema, Mapping, GUID, Reproduzierbarkeit |
| 9 Regelraum | 26 | 3 | 29 | Regeldaten, Profile, Ablehnung, Solver |
| 9a Gebäudetypen | 18 | 1 | 19 | Profilableitung, Gates, typabhängige Regeln |
| 9b Entwurfsqualität | 13 | 5 | 18 | Empfehlungen, Evidenz, Ethik |
| **Summe** | **159** | **26** | **185** | |

### 6.5.2 Überschneidungen und Widersprüche

Die Durchsicht aller 122 vorhandenen Anforderungen ergab keine unvereinbaren Widersprüche, aber sieben Paare mit Überschneidung oder abweichender Schärfe. Tabelle 6.6 nennt sie mit der Auflösung nach E6.1.

**Tabelle 6.6: Konsolidierungsbefunde**

| Paar | Befund | Auflösung |
|---|---|---|
| ANF-03-02 / ANF-08-23, -24 | beide verlangen Determinismus; 08-24 zusätzlich Zeitstempel aus Eingabe | 08-24 ist strenger und gilt; gemeinsamer Test |
| ANF-03-04 / ANF-08-12 | U-Wert-Toleranz ± 0,0005 bzw. ± 0,001 W/(m²K) | strengere Toleranz ± 0,0005 für den Referenzfall B1 |
| ANF-03-07 / ANF-09-11 | derselbe Fall (19 % Holzfeuchte) aus zwei Blickwinkeln | 09-11 regelt die Meldung, 03-07 den Referenzwert; ein Test |
| ANF-03-08 / ANF-09a-14 | 03-08 lehnt nachträglich ab, 09a-14 filtert vorab und nimmt Fußbodenaufbauten aus | 09a-14 wirkt im Kanal 1, 03-08 im Kanal 2 (Abschnitt 9.6.3); die Ausnahme gilt für beide |
| ANF-03-12 / ANF-08-22 | 03-12 schreibt die GUID des **verursachenden** Objekts (`LeitungGUID`), 08-22 die GUID des **Teils selbst** (`IfcGlobalId`) | beide Attribute; siehe Beispiel 6.4 |
| ANF-09-02 / ANF-09b-04 | „unbestimmt“ bei R1 und „nicht bewertbar“ bei R5 | gleiche Semantik, getrennte Begriffe bleiben, weil R5 nie blockiert |
| ANF-09-16 / Kap. 7a A1–A8 | Ablehnungen sind nachzuweisen; A1–A8 hatten keine Kennung | ANF-06-40 führt A1–A8 in den Katalog |

> **Beispiel 6.4 (zwei GUIDs an einer Bohrung).** In B15 bohrt die Fallleitung SW-01 durch Ständer und Balken. Die BTLx-Datei trägt an jeder `Drilling`-Bearbeitung `UserAttribute LeitungGUID` mit der GlobalId der Leitung (ANF-03-12). ANF-08-22 verlangt zusätzlich `UserAttribute Name="IfcGlobalId"` mit der GlobalId des Holzes und `Transformation GUID` = UUID des IFC-Objekts. Die beiden Forderungen beantworten verschiedene Fragen: „Welches Holz ist das?“ und „Warum ist hier ein Loch?“. Die Auflösung ist, beide Attribute zu schreiben. Der Name `LeitungGUID` wird dabei auf `UrsacheGUID` verallgemeinert, weil auch Kerven für Leerrohre und Durchbrüche für Lüftungskanäle eine Ursache haben (ANF-07-20).

### 6.5.3 Verteilung auf die Phasen

Die Zuordnung zu Phasen in `anforderungen.csv` zeigt, wo das Artefakt dicht und wo es dünn spezifiziert ist. Nach der Ergänzung durch dieses Kapitel hat jede Phase mindestens zwei Anforderungen. Die meisten Anforderungen sind querschnittlich (Schema, Determinismus, Audit) oder betreffen den Entwurf. Die Phasen Montage und Übergabe bleiben dünn. Das ist ein Befund, keine Nachlässigkeit: Die Kapitel 14b und 17 werden dort weitere Anforderungen liefern.

## 6.6 Zwischenfazit

Das Kapitel präzisiert die Anforderungen in vier Punkten:

1. **Rollen sind Rechte mit Qualifikation.** Zwölf Rollen und eine Berechtigungsmatrix bilden die Rechtslage ab. Die bauvorlageberechtigte Person erhält mit dem Gate „Regelraum“ die Einflussmöglichkeit, die „unter der Leitung“ verlangt. Ihre Freigabe eines Entwurfs ist eine Übernahmeprüfung mit Pflichtliste der Warnsignale, kein Klick.
2. **Die Kette hat jetzt Anforderungen in jeder Phase.** Idee, Vertrag, Bauantrag und Übergabe, bisher fast unspezifiziert, erhalten elf neue Anforderungen. Sie setzen harte zeitliche und formale Bedingungen um: Baubeschreibung vor Vertragserklärung, Übereinstimmung der Bauvorlagen, Name im Plankopf, Hausakte ohne App prüfbar.
3. **Die nichtfunktionalen Anforderungen treiben die Architektur.** Das Latenzbudget von 1,5 s wird von Spracherkennung und Darstellung bestimmt, nicht von der Regelprüfung, die in den Beispielen unter einer Millisekunde bleibt. Die Schemaprüfung braucht dagegen Sekunden und gehört in den Hintergrund. Datenschutz, KI-Transparenz und Beweisvorsorge verlangen eine klare Grenze zwischen Sprachmodell und Code, einen hashverketteten Audit-Trail und Signaturen am Gate.
4. **Das System hat Grenzen, die keine Technik überwindet.** Zwanzig harte Grenzen und acht Negativtests legen fest, was das System nie tut.

Kapitel 7 übersetzt diese Anforderungen in Module, Schnittstellen und eine Bausteinwahl.

## 6.7 Umsetzungsvorgaben für die App

Es gelten die Regeln aus Abschnitt 3.7 und 8.8. Jedes Abnahmekriterium ist ein automatisierbarer Testfall. Wo ein Beispiel die Referenz liefert, sind dessen gemessene Werte die Sollwerte.

### 6.7.1 Anforderungen

**Rollen, Rechte und Gates**

| ID | Muss/Soll | Beschreibung | Beleg im Kapitel | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-06-01 | Muss | Das System führt die zwölf Rollen der Tabelle 6.1. Jede Aktion prüft das Recht nach der Berechtigungsmatrix (Tabelle 6.2). Rollen sind Personen mit Qualifikationsnachweis zugeordnet (Kammer- oder Listeneintrag, Meisterbrief, Zusatzqualifikation). | 6.1.2, 6.1.3 | Testmatrix Rolle × Aktion aus Tabelle 6.2: jede Zelle „–“ wird mit Fehler „keine Berechtigung“ abgewiesen, jede Zelle „F“/„Ä“ gelingt. Person mit Rolle BV ohne hinterlegten Nachweis: Freigabe abgewiesen. |
| ANF-06-02 | Muss | Gate G0 „Regelraum“: Jede Version von Regelkatalog, Profil, Hausmodell und IDS wird von einer benannten bauvorlageberechtigten Person freigegeben (`IfcApproval` an der `IfcProjectLibrary`, QES), bevor Entwürfe dagegen geprüft werden. | 6.1.1, 6.2.2 | Katalog 0.2.0 ohne Freigabe geladen: Entwurfsprüfung verwendet weiter 0.1.0, Meldung „Regelraum 0.2.0 nicht freigegeben“. Nach Freigabe: Prüfung mit 0.2.0, Nachweis nennt Version und freigebende Person. |
| ANF-06-03 | Muss | Gate G4 „Bauvorlage“ ist eine Übernahmeprüfung: Es listet Abweichungen vom Regelraum, Angaben mit Herkunft „Kunde“, Ergebnisse mit η ≥ 0,95, Ergebnisse mit Status [U], freigabepflichtige Ergebnisse und Meldungen Dritter. Es ist erst abschließbar, wenn zu jedem Signal eine Reaktion (plausibilisiert, gegengerechnet, verworfen mit Begründung) protokolliert ist. | 6.1.4, 6.2.7, E6.2 | Testprojekt mit B3, B4 „mittig“ und B5: Liste enthält genau B5 (η = 0,97) und den Auslegungsparameter `giebel_modus`; B3 (η = 0,93) und B4 (η = 0,65) fehlen. Abschluss ohne Reaktion zu B5: abgewiesen. |
| ANF-06-04 | Muss | Gate G5 „Statik“ prüft die Qualifikation des Nachweiserstellers nach Art. 62a Abs. 1 BayBO. | 6.2.7 | Zimmerermeister ohne Zusatzqualifikation als Nachweisersteller: Gate gesperrt, Meldung nennt Art. 62a Abs. 1 Nr. 2 a. Mit Zusatzqualifikation und drei Jahren Berufserfahrung: frei. |
| ANF-06-05 | Muss | Gate G3 „Abweichung“: Ein Kundenwunsch außerhalb des Regelraums wird nur nach dokumentierter Aufklärung übernommen. Die Aufklärung ist ein signiertes Dokument (`IfcDocumentReference` mit SHA-256) mit Zustimmung des Kunden. | 6.2.7; HG-11 | Wunsch „Firstrichtung abweichend vom Bebauungsplan“: Status `freigabepflichtig`, Gate G3 offen. Ohne Aufklärungsdokument: Übernahme abgewiesen. Mit Dokument und Zustimmung: Übernahme, Nachweis „abweichend auf Wunsch, Aufklärung vom <Datum>“. |
| ANF-06-06 | Muss | Keine automatische Letztentscheidung: Jede Ablehnung, die einen Vertragsschluss verhindern kann, bietet „menschliche Prüfung anfordern“. Die Anfrage erzeugt einen Vorgang für VT oder BV mit Frist. | 6.2.7; HG-10 | B4 „zu_nah“ (15,20 m² außerhalb): Ablehnung enthält Prüfweg. Aufruf erzeugt Vorgang mit Rolle, Frist und Audit-Eintrag. Ein Test ohne Prüfweg in der Ablehnungsantwort schlägt fehl. |
| ANF-06-07 | Soll | Das Gate protokolliert Verweildauer, geöffnete Nachweise und die Reaktion je Warnsignal für die Evaluation der Aufsichtswirksamkeit. | 6.1.4 | Nach einer Testfreigabe enthält das Protokoll je Warnsignal Reaktion, Zeitstempel und die Liste geöffneter Nachweis-Hashes. |

**Funktionale Anforderungen je Phase**

| ID | Muss/Soll | Beschreibung | Beleg im Kapitel | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-06-08 | Muss | Projektstart aus Hausmodell und Grundstück: freie Geodaten (DGM, Hausumringe, Luftbild) automatisch; Flurstück (ALKIS) mit Kostenhinweis; Festsetzungen im Schema von XPlanGML, befüllt per Dialog oder PDF-Extraktion mit Bestätigung. | 6.2.3 | Grundstück ohne bestätigte GRZ: alle GRZ-abhängigen Regeln `unbestimmt`. Nach Bestätigung GRZ = 0,35: Regeln ausgewertet, Herkunft „Kunde“ bzw. „Amt“ im Nachweis. Abruf ALKIS ohne Kostenbestätigung: kein Abruf. |
| ANF-06-09 | Muss | Jede Eingangsangabe trägt eine Herkunft (Kunde, Amt, Firma) mit Zeitpunkt. Angaben mit Herkunft „Kunde“ sind im Gate G4 Warnsignale. | 6.2.3 | Geländehöhe vom Kunden eingegeben: Nachweis B4 nennt Herkunft „Kunde“; Gate G4 listet den Wert. Ersetzt durch DGM: Herkunft „Amt“, Warnsignal entfällt. |
| ANF-06-10 | Muss | Alle Eingabewege (Sprache, Text, Zeigegerät, Tastatur) erzeugen denselben typisierten Intent und dasselbe Ereignis. Keine Funktion ist nur per Sprache erreichbar. | 6.2.4, 6.3.5 | Für jeden Intent des Katalogs existiert ein UI-Pfad; derselbe Intent per Sprache und per Formular erzeugt ein Ereignis mit gleichem Inhalt (bis auf `eingabeweg`) und denselben IFC-Hash. |
| ANF-06-11 | Muss | Nach jeder angenommenen Änderung zeigt die App Kosten, Wohnfläche, H'T und Abstandsflächen mit Status „aktuell“, „wird berechnet“ oder „unbestimmt“; kein Wert eines älteren Standes erscheint ohne Kennzeichnung. Die Antwort nennt die Kostenänderung aktiv. | 6.2.4 | B6 „Bad oben 2,60 m“: Antwort enthält Kostenänderung und Wohnfläche „aktuell“; H'T „wird berechnet“ bis zum Ende der Hintergrundprüfung, danach „aktuell“ mit Revisions-Hash. |
| ANF-06-12 | Muss | Gate G1 „Vertrag“: Die Baubeschreibung ist eine Sicht auf das Modell und besteht `DE.EGBGB249.Baubeschreibung`. Die Vertragserklärung ist erst möglich, wenn die Übergabe in Textform mit Zeitstempel protokolliert ist. | 6.2.5; HG-7 | Baubeschreibung ohne Abschnitt 7 (Gebäudetechnik): Gate gesperrt, Meldung „Art. 249 § 2 Nr. 7 EGBGB“. Vollständig, Übergabe protokolliert am T: Vertragserklärung ab T möglich, vor T abgewiesen. |
| ANF-06-13 | Muss | Mit der Vertragserklärung wird der Vertragsstand eingefroren (IFC-Revision, Baubeschreibung, Preis, SHA-256). Jede spätere Änderung ist eine neue Revision und ein Nachtrag. | 6.2.5 | Änderung nach Vertrag: neue Revision, Nachtrag mit Bezug auf den eingefrorenen Hash; der eingefrorene Stand ist unverändert abrufbar und hat denselben Hash. |
| ANF-06-14 | Soll | Das Angebot entsteht aus `IfcCostSchedule` mit Preisgültigkeit (`ApplicableDate`, `FixedUntilDate`) und wird als GAEB DA XML exportiert. | 6.2.5 | GAEB-Export ist gegen die XSD valide; Summe der Positionen = Summe des `IfcCostSchedule` ± 0,01 €. |
| ANF-06-15 | Muss | Gate G2 „Ausstattung“: Die Ausstattungsfestlegung ist ein Dokument mit Hash und Unterschrift des Kunden; ihr Datum löst den Termin „Montage frühestens 12 Wochen danach“ aus. | 6.2.6 | Festlegung am 20.07.2026: frühester Montagetermin 12.10.2026 (vgl. ANF-03-20). Montagetermin 05.10.2026: Warnung. |
| ANF-06-16 | Muss | Bauvorlagen nach BauVorlV entstehen aus einer freigegebenen Revision; der Name der bauvorlageberechtigten Person steht automatisch im Plankopf (aus `IfcApproval` G4). Wird die Freigabe ungültig, ist der Export gesperrt. | 6.2.8; HG-1, HG-6 | Plankopf-Name = `IfcApproval.RequestingApproval` bzw. Akteur der Freigabe G4. Profilwechsel Endhaus → Mittelhaus nach Freigabe: Export gesperrt (vgl. ANF-09a-07). |
| ANF-06-17 | Muss | Jede Bauvorlage trägt den Hash derselben Revision (Übereinstimmung nach § 13 BauVorlV). | 6.2.8 | Paket aus Lageplan der Revision r1 und Grundriss der Revision r2: Export verweigert, Meldung „§ 13 BauVorlV: Revisionen verschieden“. |
| ANF-06-18 | Muss | Das System bestimmt das Verfahren (Freistellung, vereinfacht, regulär) und den Adressaten (Gemeinde oder Bauaufsicht) und führt die Fristen (Freistellung 1 Monat; Erklärung Standsicherheit spätestens mit der Baubeginnsanzeige). | 6.2.8 | Qualifizierter Bebauungsplan, keine Abweichung: Verfahren „Freistellung“, Adressat Gemeinde; Eingang 01.09.2026: frühester Baubeginn 01.10.2026. Baubeginnsanzeige ohne Erklärung: Warnung „§ 15 BauVorlV“. |
| ANF-06-19 | Soll | Formulardaten für BayernPortal bzw. XBau werden erzeugt; das IFC geht als Anlage mit. | 6.2.8 | Formulardaten enthalten Gebäudeklasse, Baukosten und Entwurfsverfasser aus dem Modell; Anlage-IFC hat den Revisions-Hash. |
| ANF-06-20 | Muss | Werkplanung arbeitet auf demselben Parametermodell; ihre Ergänzungen sind Ereignisse mit Rolle WP. Jede Revision nach Vertrag entsteht aus gen(*x*). Import fremder Geometrie nur als Produktgeometrie am Typ. | 6.2.9 | Für jede Revision nach Vertrag gilt: gen(Ereignisfolge) ergibt denselben Hash. Anzahl der Revisionen mit manuell importierter Bauteilgeometrie = 0. |
| ANF-06-21 | Muss | Die Produktionsfreigabe (G7) erzeugt ein unveränderliches Fertigungspaket (IFC, BTLx, WUP oder Adapter-Meldung, `export_guid.csv`, Stückliste) mit Hash und Siegel. Das Werk nimmt nur Pakete mit gültiger Freigabe an. | 6.2.9 | Paket ohne Freigabe G7: Abruf durch Rolle WK abgewiesen. Paket mit Freigabe: Hash des Pakets = Hash im Freigabedatensatz; nachträgliche Änderung einer Datei macht das Siegel ungültig. |
| ANF-06-22 | Soll | Montage-Ist-Termine und Abweichungen fließen als Ereignisse in `IfcWorkSchedule`/`IfcTask` zurück. | 6.2.9 | Ist-Termin für Element W-03 gemeldet: `IfcTask` trägt Ist-Datum; Abweichung > 1 Tag erzeugt Hinweis. |
| ANF-06-23 | Muss | Gate G8 „Übergabe“: Die Hausakte enthält die letzte freigegebene Revision, alle Nachweishefte, alle Dokumente und einen Auszug des Audit-Trails in offenen Formaten (IFC, PDF, JSON) mit Beweiswerterhaltungsnachweis und ist ohne die App prüfbar. | 6.2.9, 6.3.7 | Offline-Prüfskript ohne App-Code: alle Hashes der Hausakte stimmen; Entfernen eines Nachweishefts wird erkannt. |
| ANF-06-24 | Soll | Wartung und Gewährleistung stehen als `IfcAsset` mit `Pset_Warranty` im Übergabemodell. | 6.2.9 | Jedes Bauteil mit Gewährleistungsangabe im Katalog hat im Übergabemodell ein `Pset_Warranty` mit Beginn = Abnahmedatum. |

**Nichtfunktionale Anforderungen**

| ID | Muss/Soll | Beschreibung | Beleg im Kapitel | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-06-25 | Muss | Das Prüfprotokoll K1–K4 gehört zu genau der Revision, die freigegeben wird (gleicher SHA-256). | 6.3.1 | Freigabe mit Protokoll einer anderen Revision: abgewiesen, Meldung nennt beide Hashes. |
| ANF-06-26 | Muss | Die Wiederholung der Ereignisfolge eines Projekts ergibt byte-identische IFC-Revisionen, Nachweise und Exporte. Intent-Ergebnisse werden aus dem Ereignis gelesen, nicht neu berechnet. | 6.3.2 | Replay der neun Äußerungen von B6 gegen `haus_state.json`: gleiches Protokoll (Status, Maße, GUIDs) und gleicher Hash des Endzustands, in zwei Prozessen mit `PYTHONHASHSEED` 1 und 4711. |
| ANF-06-27 | Muss | Jede Revision trägt die Kennung einer archivierten Laufzeitumgebung (Generator-, Katalog-, Profilversion, Hash der Paketliste, Kennung des Container-Abbilds), aus der sie byte-identisch neu erzeugt werden kann. | 6.3.2 | Neuerzeugung von B1 im archivierten Abbild: SHA-256 `5a796ea7…f8bb478b`. Abbild mit anderer IfcOpenShell-Version: Abweichung wird gemeldet, nicht verschwiegen. |
| ANF-06-28 | Muss | Latenz der Sprachschleife vom Ende der Äußerung bis zur Antwort (Annahme, Ablehnung, Rückfrage) ≤ 1,5 s im 95. Perzentil für lokale Änderungen; der deterministische Anteil (Parser, Referenz, lokale Regeln) ≤ 50 ms. | 6.3.3, E6.3 | Lasttest mit den neun B6-Äußerungen × 50 auf der Zielhardware: p95 gesamt ≤ 1 500 ms; deterministischer Anteil p95 ≤ 50 ms (Referenz 27.09.2026: 0,229 ms). |
| ANF-06-29 | Muss | Prüfungen außerhalb des Latenzbudgets laufen asynchron; ihr Ergebnis ist bis zum Abschluss `unbestimmt`. Eine Freigabe ist erst nach Abschluss aller Hintergrundprüfungen der Revision möglich. | 6.3.3 | `ifcopenshell.validate` (B1: 3,66 s) läuft nicht im synchronen Pfad; Status „wird berechnet“, danach Ergebnis mit Revisions-Hash. Freigabeversuch vor Abschluss: abgewiesen. |
| ANF-06-30 | Muss | Spracherkennung standardmäßig lokal; kein Rohaudio über die Sitzung hinaus; keine Sprechererkennung; Cloud-Fallback nur nach Einwilligung und mit Zero Data Retention; ins Audit gehen Intent, Parameter und Ergebnis, nicht das Transkript. | 6.3.4 | Nach Sitzungsende enthält kein Speicherort Audio. Fallback ohne Einwilligung: nicht aufgerufen. Audit-Eintrag einer Spracheingabe enthält kein Feld mit Transkript. |
| ANF-06-31 | Muss | Aufzeichnung von Beratungsgesprächen nur mit Einwilligung aller Beteiligten. | 6.3.4; HG-17 | Mehrpersonen-Modus mit zwei Teilnehmern, eine Einwilligung fehlt: Mikrofon bleibt aus. |
| ANF-06-32 | Muss | Vor Produktivbetrieb liegen Datenschutz-Folgenabschätzung und Verarbeitungsverzeichnis vor. | 6.3.4 | Betriebsfreigabe prüft das Vorhandensein beider Dokumente mit Datum und Version; fehlt eines, startet der Produktivmodus nicht. |
| ANF-06-33 | Muss | Funktionen, die zum Vertragsschluss führen, sind nach EN 301 549 barrierefrei; der 3D-Editor hat eine gleichwertige nicht-visuelle Sicht (Raumliste, Nachbarschaften, Kennzahlen, Meldungen); Status nie nur durch Farbe. | 6.3.5; HG-18 | Automatisierte Prüfung der vertragsrelevanten Seiten: 0 Verstöße. Aufgabe „Bad um 20 cm verbreitern“ ist ohne 3D-Ansicht per Tastatur lösbar. |
| ANF-06-34 | Muss | Hinweis auf KI-Interaktion vor der ersten Spracheingabe und dauerhaft sichtbar; jede Antwort trennt erkannte Absicht (mit Wahrscheinlichkeit) von berechneten Werten. | 6.3.6; HG-16 | UI-Test: Hinweis vor erster Eingabe; Antwort auf B6 „Bad oben 2,60 m“ zeigt „erkannt: raum_aendern“ getrennt von „berechnet: Bad 2,40 → 2,60 m; Kinderzimmer 1 3,50 → 3,30 m“. |
| ANF-06-35 | Muss | Die KI-Grenze ist dokumentiert und getestet: Kein Ausgabewert von Intent- oder Sprachmodell gelangt ohne deterministischen Parser und Regelprüfung in das Parametermodell. | 6.3.6 | Datenflusstest: Ereignis mit Wert aus Feld `intent.antwort` ohne Parser-Beleg wird abgewiesen; Architekturdokument listet `sprache-asr` und `intent` als KI-Systeme, `regelmaschine` nicht. |
| ANF-06-36 | Muss | Jedes Ereignis (Änderung, Prüfung, Ablehnung, Empfehlung, Freigabe, Export) steht in einem nur anhängbaren, hashverketteten Protokoll. | 6.3.7 | Veränderung eines Eintrags n: Kettenprüfung schlägt ab n fehl und nennt n. Löschung eines Eintrags wird erkannt. |
| ANF-06-37 | Muss | Nachweishefte und Freigaben tragen qualifiziertes Siegel und qualifizierten Zeitstempel; die QES der Person steht am Gate; die Hausakte erhält einen Beweiswerterhaltungsnachweis nach TR-ESOR. | 6.3.7 | Signaturprüfung mit dem Prüfwerkzeug des Vertrauensdiensteanbieters: gültig. Nachweisheft nach der Signatur geändert: Prüfung ungültig. |
| ANF-06-38 | Muss | Offline funktionieren Entwurf, Sprachschleife, lokale R1-Regeln, Nachweise, K1 und K3; Freigaben, Signaturen, amtliche Abrufe und Cloud-Fallback nicht. Offline erzeugte Ereignisse werden nach Verbindung synchronisiert und nachgeprüft. | 6.3.8, E6.4 | Test ohne Netz: B6-Äußerungen werden verarbeitet, B4 und B5 geprüft, Freigabeversuch zeigt „nur online“. Nach Verbindung: Ereignisse synchronisiert, Kanal 2 läuft, Ergebnis gleich. |
| ANF-06-39 | Soll | Die Nutzerstudie misst Gebrauchstauglichkeit nach ISO 9241-11 (Aufgabenerfolg, Zeit, Zufriedenheit) und die Baubarkeit des Ergebnisses. | 6.3.9 | Studienprotokoll enthält je Teilnehmer Erfolg (zulässiger, kalkulierter Entwurf ohne Mitarbeiter), Zeit, Zufriedenheit und die Zahl der R1-Verstöße im Ergebnis. |
| ANF-06-40 | Muss | Jeder Nachweis validiert gegen `nachweis.schema.json` und erfüllt A1–A8 aus Kapitel 7a. | 6.3.9, 6.5.2 | Die 32 Nachweise B1–B5 validieren. Kopie ohne `regel.fassung`: ungültig mit Meldung „A1: Fassung fehlt“. |

### 6.7.2 Datenstrukturen und Parameter

**A Person und Qualifikation**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `person_id` | UUID | – | eindeutig | ANF-06-01 |
| `name` | string | – | Klarname für Plankopf | ANF-06-16 |
| `rollen` | list[enum] | – | KU, VT, FR, BV, TW, FP, PS, WP, WK, MO, BA, GE | Tabelle 6.1 |
| `qualifikation` | list[object] | – | Art (Architekt, Listen-Ingenieur, Zimmerermeister, Zusatzqualifikation 62a, Tragwerksplaner-Liste), Nummer, Stelle, gültig bis | Art. 61, 62a BayBO; DAT-06-01 |
| `berufserfahrung_jahre` | int | a | 0–60 | Art. 62a Abs. 1 BayBO |
| `reichweite` | list[Profil-ID] | – | abgeleitet aus Qualifikation | ANF-09a-07 |

**B Freigabe (Gate-Datensatz)**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `gate` | enum | – | G0 Regelraum, G1 Vertrag, G2 Ausstattung, G3 Abweichung, G4 Bauvorlage, G5 Statik, G6 Brandschutz, G7 Produktion, G8 Übergabe | 6.2, Kap. 7.4 |
| `revision_sha256` | string | – | 64 Hex-Zeichen | ANF-06-25 |
| `person_id`, `rolle` | UUID, enum | – | – | A |
| `warnsignale` | list[object] | – | Art, Nachweis-Hash, Reaktion ∈ {plausibilisiert, gegengerechnet, verworfen}, Begründung, Zeitstempel | ANF-06-03 |
| `signatur` | object | – | Art ∈ {QES, Siegel}, Anbieter, Zertifikat, Zeitstempel (qualifiziert) | ANF-06-37 |
| `ifc_approval_guid` | GlobalId | – | 22 Zeichen | ANF-08-19 |
| `gueltig` | bool | – | ungültig bei Hash- oder Profilwechsel | ANF-09a-07 |

**C Herkunft einer Angabe**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `herkunft` | enum | – | kunde, amt, firma, berechnet | ANF-06-09 |
| `quelle` | string | – | z. B. „DGM1 Bayern“, „Eingabe Kunde“ | ANF-06-08 |
| `zeitpunkt` | datetime | – | ISO 8601 | ANF-06-09 |
| `lizenz` | string | – | z. B. CC BY 4.0 | [@opengeodataBY] |

**D Audit-Ereignis**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `nr` | int | – | fortlaufend ab 1 | ANF-06-36 |
| `art` | enum | – | aenderung, pruefung, ablehnung, empfehlung, rueckfrage, freigabe, export, anfechtung | ANF-06-36 |
| `rolle`, `eingabeweg` | enum | – | Tabelle 6.1; sprache, text, zeiger, tastatur | ANF-06-10 |
| `intent`, `parameter` | object | – | ohne Transkript | ANF-06-30 |
| `versionen` | object | – | Generator, Katalog, Profile, Intent-Modell, ASR | ANF-06-27, ANF-07-22 |
| `ergebnis_hash` | string | – | SHA-256 von Revision oder Nachweis | ANF-06-26 |
| `vorgaenger_hash` | string | – | SHA-256 des Eintrags nr − 1 | ANF-06-36 |

**E Latenzmessung**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `t_asr_ende`, `t_intent`, `t_parser`, `t_regeln`, `t_gen`, `t_anzeige` | float | ms | ≥ 0 | E6.3 |
| `budget_p95_ms` | int | ms | 1 500 | ANF-06-28 |
| `umgebung` | object | – | CPU, GPU, Modellversionen | 6.3.3 |

**F Einwilligung**

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `zweck` | enum | – | mikrofon, cloud_fallback, aufzeichnung_beratung, kua_berechnung | ANF-06-30, -31; ANF-09b-13 |
| `personen` | list[UUID] | – | alle Anwesenden bei Aufzeichnung | § 201 StGB |
| `erteilt_am`, `widerrufen_am` | datetime | – | – | § 25 TDDDG |

### 6.7.3 Datenlieferungen von Regnauer

| ID | Inhalt | gewünschtes Format | Ersatz bis zur Lieferung | blockiert |
|---|---|---|---|---|
| DAT-06-01 | Personen mit Freigaberechten: Qualifikation, Listen- oder Kammereintrag, Zusatzqualifikation nach Art. 62a, interne schriftliche Freigabeordnung | Tabelle A, Dokument | Testpersonen, Gates nur im Testmodus | ANF-06-01, -02, -04 |
| DAT-06-02 | Organisationsrollen: Vertrieb, Projektleitung, Werkplanung, Vertretungen, Zuständigkeit für Anfechtungen | Organigramm, Tabelle | Rollen aus Tabelle 6.1 | ANF-06-06 |
| DAT-06-03 | Vertragsprozess: aktuelle AGB, Muster der Widerrufsbelehrung, Form der Vertragserklärung, bisherige Übergabe der Baubeschreibung | PDF, Prozessbeschreibung | AGB 10/2024 [@regnauerBLB2024] | ANF-06-12, -13 |
| DAT-06-04 | Inhalt und Aufbewahrungsdauer der Hausakte, gewünschte Dauer der Beweiswerterhaltung | Liste, Frist in Jahren | QDF-Satzung, Dauer offen | ANF-06-23, -37 |
| DAT-06-05 | Vertrauensdienste: vorhandene QES-Karten, Firmensiegel, Zeitstempeldienst | Anbieter, Verfahren | Signatur-Adapter im Testmodus ohne Rechtswirkung | ANF-06-37 |
| DAT-06-06 | Datenschutz: Verarbeitungsverzeichnis, Datenschutzbeauftragter, Einwilligungstexte, Hosting-Vorgaben | Dokumente | Muster der Arbeit, nicht produktiv | ANF-06-30 bis -32 |
| DAT-06-07 | Einsatzorte und Geräte: Musterhäuser, Bauherrenzentrum, Netzabdeckung, Offline-Bedarf | Liste | Offline-Kern nach E6.4 | ANF-06-38 |
| DAT-06-08 | Barrierefreiheit: vorhandene Erklärung zur Barrierefreiheit, Zielgruppen, Beratung vor Ort | Dokument | Prüfung nach EN 301 549 ohne Firmenbezug | ANF-06-33 |
| DAT-06-09 | Prüfumfang und Vermerk der bisherigen Freigabe von Kundenplänen (wer prüft was, mit welchem Vermerk) | Checkliste, Beispielvermerk | Warnsignale nach E6.2 | ANF-06-03 |

Voraussetzung für den Produktivbetrieb und deshalb mit Priorität „Muss“ geführt sind DAT-06-01, -03, -05 und -06. Ohne sie läuft die App, aber Gates, Vertrag und Signaturen nur im Testmodus ohne Rechtswirkung.

### 6.7.4 Maschinenlesbare Dateien

| Datei | Inhalt | Prüfung |
|---|---|---|
| `spezifikation/anforderungen.csv` | alle 185 `ANF-*` aus den Kapiteln 3, 6, 7, 8, 9, 9a, 9b mit Spalten `id`, `prioritaet`, `phase`, `rolle`, `beschreibung`, `abnahmekriterium`, `kapitel`, `quelle_keys`, `modul`, `test`, `status` | per Skript aus den Markdown-Tabellen extrahiert (`spezifikation/anforderungen_extrahieren.py`); Module aus `module.yaml` |
| `spezifikation/datenlieferungen.csv` | alle 29 `DAT-*` (Kapitel 3, 6, 7) mit `id`, `beschreibung`, `benoetigt_fuer`, `kapitel`, `prioritaet` | ebenfalls aus den Tabellen extrahiert |
| `spezifikation/regelkatalog-06.yaml` | sechs R3- und R4-Regeln zu den harten Grenzen HG-1, HG-2 und HG-6 bis HG-11 | validiert gegen `regel.schema.json` |

**Prüfung (Python, 27.09.2026).** Beide CSV-Dateien wurden mit `csv.DictReader` geladen und geprüft auf: eindeutige IDs, Priorität ∈ {Muss, Soll}, nichtleeres Abnahmekriterium, Modul ∈ `module.yaml`, jede ANF genau einem Modul zugeordnet, jeder Quellen-Key in `literatur/lit-*.bib`. `regelkatalog-06.yaml` wurde mit PyYAML geladen und mit `jsonschema` 4.26 gegen `regel.schema.json` validiert. Ergebnis: **0 Fehler**; 185 Anforderungen (159 Muss, 26 Soll), 29 Datenlieferungen (12 Muss), 6 Regeln.

---

## Verwendete Keys

aiact2024, bainbridge1983ironies, barker2022fair4rs, bauvorlv, baybo2026, bayDigitalisierungEntwurf2026, bfsg, bgb, bgh1993vizr24392, bgh2001viizr39199, bgh2011viizr810, bgh2013viizr25711, bgh2023viizr21622, bgh2026viizr11924, bsi2022tresor, bsi2024ids, bsi2025validation, btlx23, bundestag2016bauvertrag, bverfg1970bvr11765, byak2020berufsordnung, chen2025agent, dbauv2026, dsk2024ki, dsk2025kitom, edpb2021vva, egbgb249, elghaish2022voice, eu2014eidas, eu2024produkthaftungsrl, eu2025aidefinition, eu2026omnibus, eugh2023schufa, expertgroup2019liability, green2022flaws, hevner2004design, holzbaurl2024, hunhevicz2020need, ikbaunrw2024unterzeichnung, iso2018usability, iso2020interaction, iso2024ifc, kimig2026, landtagby2007baybo, landtagby2020baybonovelle, landtagby2024modernisierung, olgkoeln2017u9816, olgkoeln2021u2320, olgnuernberg2011u136910, olgnuernberg2021u113921, opengeodataBY, parasuraman2000model, peffers2007design, prodhaftg2026, puusepp2017enabling, qdf2022, regnauerBLB2024, silverman1992critiquing, smith2016softwarecitation, sterz2024quest, stgb201, tdddg25, urhg5, vdg2017, xplanung, zpo371a

### Key-Check

Der folgende Test extrahiert alle Pandoc-Zitate `[@key]` aus diesem Kapitel und prüft sie gegen die Einträge in `literatur/lit-*.bib`. Aufruf aus `arbeit/`:

```python
#!/usr/bin/env python3
"""Prüft, dass jeder [@key] in Kapitel 6 in literatur/lit-*.bib definiert ist."""
import glob
import re
from pathlib import Path

text = Path("06-anforderungen.md").read_text(encoding="utf-8").split("## Verwendete Keys")[0]
zitate = set()
for block in re.findall(r"\[(@[^\]]+)\]", text):
    zitate.update(re.findall(r"@([A-Za-z0-9_:\-]+)", block))
bib = set()
for datei in glob.glob("literatur/lit-*.bib"):
    bib.update(re.findall(r"^@\w+\{([^,\s]+),", Path(datei).read_text(encoding="utf-8"), re.M))
fehlend = sorted(zitate - bib)
print(f"{len(zitate)} Schlüssel zitiert, {len(bib)} Schlüssel in lit-*.bib, {len(fehlend)} fehlend")
print("fehlend:", fehlend if fehlend else "keine")
```

Ausgabe am 27.09.2026:

```
66 Schlüssel zitiert, 1087 Schlüssel in lit-*.bib, 0 fehlend
fehlend: keine
```

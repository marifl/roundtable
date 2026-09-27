# 13 Technische Gebäudeausrüstung und automatisches Routing

Status: Entwurf v0.1 (27.09.2026). Befunde zur Rechts- und Normenlage, keine Rechts- oder Fachplanungsberatung. Zitate beziehen sich auf `literatur/lit-*.bib`. Befunde tragen [V] (an Primärquelle, Normenverlag, Herstellerdatenblatt, am Schema IFC4X3_ADD2 oder im Prototyp geprüft) oder [U] (unsicher); eigene Bewertungen sind als solche formuliert. Normtexte (DIN, VDE, DVGW) sind kostenpflichtig; ihre Kennwerte stammen aus den Recherchen 08, 14, 16 und 22 und werden nach Kapitel 9.7 nur als Einzelkennwerte mit Fundstelle geführt. Zahlen aus den Beispielen stammen aus `beispiele/ausgabe/` und sind, wo die Eingaben Beispielwerte sind, als Beispielwerte zu lesen.

## 13.0 Einordnung und Vorgehen

Die Forschungsfrage FF6 verlangt, die Technische Gebäudeausrüstung (TGA) mit allen Details und Einbauteilen regelbasiert zu erzeugen, und zwar in den drei Reifegraden P, R und A aus demselben Modell. Kapitel 5 hat die zugehörige Lücke L9 benannt: Die Arbeiten zum TGA-Routing kennen keine Bohrregeln des Holzbaus und übergeben Durchbrüche nicht als Fertigungsbearbeitung [@baradaran2022parametric; @blokland2023literature]. Dieses Kapitel schließt die Lücke in vier Schritten:

1. **Regeln je Gewerk** (13.1 bis 13.7) mit Kernwert, Verbindlichkeit und IFC-Abbildung.
2. **IFC-Abbildung** (13.8) von Systemen, Segmenten, Ports, Verbindungen und Durchbrüchen.
3. **Dimensionierung und Durchdringungen** (13.9) bis zur Übergabe als BTLx-Bearbeitung.
4. **Routing unter Regeln** (13.10) auf einem Graphen über den konstruktiven Zellen, der Regeln während der Erzeugung einhält und Kreuzungen als Fertigungsdaten ausgibt.

Es folgen Vorinstallation (13.11), Gebäudetyp-Deltas (13.12) und die Umsetzungsvorgaben (13.14). Maschinenlesbar sind `spezifikation/regelkatalog-13-tga.yaml` (42 Regeln im Schema aus Kapitel 9.2.3), `spezifikation/tga-dimensionierung.yaml` (20 Formeln, 33 Testfälle) und `spezifikation/routing-graph.md` (formale Definition des Routing-Graphen).

Zwei Befunde prägen das Kapitel. Erstens existieren fast alle TGA-Regeln bereits, und sie sind überwiegend **geometrisch**: Zonen, Schutzbereiche, 3-Liter-Regel, Gefälle, Luftmengen, Spitzendurchfluss und Wärmepumpen-Abstände lassen sich als Parameter, Sperrvolumen oder Formeln codieren. Die DIN-Tabellen sind aber weder maschinenlesbar noch frei lizenziert (Recherche 08) [V]. Zweitens ist Routing in der Forschung gelöst, als Produkt nicht; für den Holzrahmenbau fehlt ein Router, der Ständer, Balken, Zonen und Luftdichtheit zugleich beachtet (Recherchen 08 und 12) [V].

**Verbindlichkeit.** DIN 18015 ist eine Planungsnorm und gilt nur bei vertraglicher Vereinbarung, die VDE-Normen sind anerkannte Regeln der Technik (Recherche 08) [V]. Das Regelschema bildet diese Geltung über Quelle und Schicht ab (Kapitel 9.3.3).

**E13.1 – Planungsnormen der TGA stehen im Firmenprofil, Sicherheitsnormen im Profil der anerkannten Regeln.** *Entscheidung.* DIN 18015-2 und -3 stehen als Normquelle im Profil `M-Firma` (*S*₅) und gelten, soweit die Bau- und Leistungsbeschreibung sie vereinbart (DAT-13-10). Sicherheits- und Hygieneregeln (DIN VDE 0100-701, DIN 4108-7, DIN EN 1264, DIN 1946-6) stehen im neuen Profil `DE-aRdT-TGA` (*S*₃), Sanitärregeln in `DE-aRdT-Sanitaer`, öffentliches Recht in *S*₁ und eingeführte Baubestimmungen in *S*₂. *Begründung.* So kann die Firma eine Planungsnorm vertraglich abwandeln, ohne eine Sicherheitsregel zu berühren; die Monotonieprüfung (Kapitel 9.3.3) verhindert Lockerungen. *Beleg.* Recherche 08 [V]; `regelkatalog-13-tga.yaml`.

## 13.1 Elektro und Netzwerk

### 13.1.1 Installationszonen nach DIN 18015-3

DIN 18015-3 legt fest, wo Leitungen in Wänden, Decken und Böden verlaufen dürfen. Die Zonen sind Rechtecke auf der Wandfläche, deren Lage sich aus Decke, Fußboden, Öffnungen und Ecken ergibt (Recherche 08) [V]:

| Zone | Lage | Breite |
|---|---|---|
| ZW-o | 15–45 cm unter der Deckenbekleidung | ≤ 30 cm |
| ZW-u | 15–45 cm über dem Fertigfußboden | ≤ 30 cm |
| ZW-m | 100–130 cm über dem Fertigfußboden, nur in Räumen mit Arbeitsflächen | ≤ 30 cm |
| ZS-t, ZS-f, ZS-e | 10–30 cm neben Rohbaukanten: an Türen auf der Griffseite, an Fenstern beidseitig, an Wandecken | ≤ 20 cm |
| ZD-r (Decke, Boden) | Wandabstand ≥ 20 cm; am Türdurchgang (ZD-t) ≥ 15 cm; 20 cm Abstand zu Zonen fremder Gewerke | ≤ 30 cm |

Waagerechte Leitungen liegen in ZW-Zonen, senkrechte in ZS-Zonen. Über Türen gilt ein Mindestabstand von 10 cm. Der oberste Schalter neben einer Tür sitzt mittig auf 105 cm [V]. Die Vorzugshöhen von 30 cm in ZW-u und 115 cm in ZW-m sind abgeleitet [U].

Für den Holzbau ist die **Ausnahme für Leichtbau** entscheidend. In Fertigbauteilen und Leichtbauwänden darf von den Zonen abgewichen werden, wenn die Leitung mindestens 6 cm überdeckt ist oder in unverfüllten Hohlräumen ausweichen kann [V, Wortlaut nach Fachartikel]. Recherche 08 folgert daraus, dass gedämmte Gefache nicht unverfüllt sind [U, Auslegung]. Kapitel 3.1.6 hat gezeigt, dass Regnauer in Innenwänden eine Installationsebene von 40 mm vorsieht und für die Außenwand keine beschreibt [@regnauerBLB2024].

**E13.2 – Installationszonen sind in Holzständerwänden hart; die Ausnahme wird aus dem Schichtmodell berechnet.** *Entscheidung.* Die Regel `DE.DIN18015-3.Installationszonen-Wand` entfernt im Routing-Graphen jede Wandkante außerhalb einer Zone. Die Ausnahme gilt nur, wenn die Überdeckung *ü* = Σ der Schichtdicken raumseitig vor der Leitung mindestens 60 mm beträgt, oder wenn der Auslegungsparameter `gedaemmtes_gefach_unverfuellt` durch die verantwortliche Person auf *wahr* gesetzt wird. Voreinstellung ist *falsch*. *Begründung.* Die Zone schützt Dritte, die später in die Wand bohren. Diese Schutzfunktion ist im Holzbau nicht schwächer als im Massivbau. Die Überdeckung ist eine Modellgröße und kein Ermessen. *Beleg.* Recherche 08 [V Wortlaut, U Auslegung]; Kapitel 9.2.3 zum Umgang mit Auslegungsparametern.

> **Beispiel 13.1 (Überdeckung).** Eine Leitung im Kern hinter einer Installationsebene von 40 mm und einer Beplankung von 15 mm hat *ü* = 55 mm < 60 mm. Die Ausnahme greift nicht, die Zonen gelten. Mit einer Gipslage von 25 mm, wie sie die Außenwand des Praxispartners trägt [@regnauerBLB2024], ergäbe sich bei gleicher Installationsebene *ü* = 65 mm. Die Außenwand hat nach der öffentlichen Beschreibung aber keine Installationsebene (Kapitel 3.1.6). Die Werte sind Beispielwerte; der Schichtaufbau ist Datenlieferung DAT-01 aus Kapitel 3.

### 13.1.2 Mindestausstattung, Bad-Schutzbereiche, Fehlerlichtbogenschutz

**Mindestausstattung.** DIN 18015-2:2021-10 bestimmt die Zahl der Steckdosen- und Beleuchtungsstromkreise nach der Wohnfläche: bis 50 m² drei, bis 75 m² vier, bis 100 m² fünf, bis 125 m² sechs, darüber sieben. Eine Doppelsteckdose zählt als zwei Steckdosen [V]. RAL-RG 678 staffelt die Ausstattung in Sterne-Stufen, deren Stufe 1 DIN 18015-2 entspricht [V]; eine vereinbarte Stufe erhöht die Mindestwerte, senkt sie nie. Eine Wohnung mit 140 m² braucht also mindestens sieben Stromkreise.

**Bad-Schutzbereiche.** DIN VDE 0100-701:2008-10 definiert drei Bereiche. Bereich 0 ist das Wanneninnere. Bereich 1 reicht bis 2,25 m über dem Fertigfußboden oder bis zum höchsten festen Wasserauslass. Bereich 2 reicht 0,60 m darüber hinaus. Bei der bodengleichen Dusche hat Bereich 1 einen Radius von 1,20 m. In Bereich 2 sind Steckdosen nur als SELV, PELV oder Rasiersteckdose zulässig. Betriebsmittel brauchen mindestens IPX4, und Leitungen zu Bereich 1 führen senkrecht von oben oder hinten. Raumfremde Leitungen brauchen 6 cm Restwand oder eine RCD mit höchstens 30 mA [V]. Offen ist Bereich 0 bei der Dusche ohne Wanne [U]. Die Regel wird als **Sperrvolumen** umgesetzt: eine Extrusion um jedes `IfcSanitaryTerminal` BATH bzw. SHOWER, gegen die jedes Betriebsmittel und jede Leitungskante geprüft wird (Constraint K9 in `routing-graph.md`).

**Fehlerlichtbogen-Schutzeinrichtungen.** Seit DIN VDE 0100-420:2019 gibt es keine Pauschalpflicht mehr. Verlangt ist eine Risiko- und Sicherheitsbewertung für Schlafräume und für Räume aus Bauteilen mit brennbaren Baustoffen unter „feuerhemmend“. Holzrahmenbau mit Mineralwolle ist laut DKE nicht „überwiegend brennbar“ [V]. Die R3-Regel `DE.VDE0100-420.AFDD-Bewertung` liefert deshalb *freigabepflichtig*, bis eine Elektrofachkraft je Raum ein Protokoll bestätigt.

### 13.1.3 Zählerschrank, Luftdichtheit und Netzwerk

**Zählerplatz.** Nach VDE-AR-N 4100:2019-04 umfasst ein Zählerfeld 450 mm, davon 300 mm für den elektronischen Haushaltszähler und 150 mm Raum für Zusatzanwendungen. Hinzu kommen der obere Anschlussraum von 300 mm und ein APZ-Raum von mindestens 300 mm. Zwischen Hausübergabepunkt und APZ liegt ein Leerrohr von mindestens 25 mm, und vor dem Schrank ist ein Bedienbereich von 1,2 m Tiefe und 2 m Höhe frei zu halten [V]. Eine Neuausgabe und die bayerischen Netzbetreiber-TAB sind nicht geprüft [U]. Der Bedienbereich ist eine `IfcSpatialZone` RESERVATION und für Möbel und Leitungen gesperrt (K14).

**Luftdichtheit.** DIN 18015-5 verlangt luftdichte Hohlwand- oder Massivholzdosen, an den Enden abgedichtete Rohre und bevorzugt eine Installationsebene. Zählerschrank und Verteiler gehören an Innenwände [V Inhalt, U Ausgabejahr]. Das BDF-Merkmal hält fest, dass die Installationsebene die Luftdichtheit im Holztafelbau nicht generell löst; wo die Beplankung durchdrungen wird, braucht es luftdichte Dosen [V]. Die Regel `DE.DIN4108-7.Luftdichte-Durchdringung` fasst Dosen und Manschetten zusammen: Jede Öffnung in einer Schicht mit `luftdicht = true` braucht eine Füllung, die als `IfcRelFillsElement` im Modell steht. Das entspricht ANF-03-09.

**Glasfaser.** Für Neubauten mit Bauantrag ab dem 12.02.2026 verlangt Art. 10 der Gigabit-Infrastrukturverordnung (EU) 2024/1309 eine glasfaserfähige gebäudeinterne Infrastruktur **und** die Glasfaserverkabelung bis zum Netzabschlusspunkt. Einen Zugangspunkt verlangt sie nur bei Mehrparteiengebäuden. Die ältere Pflicht nach § 145 Abs. 4 TKG wird überlagert [V]. Die App behandelt das als R2-Regel `EU.GIA.10.Glasfaser`: Ein Teilsystem mit Leerrohr, `IfcCableSegment` OPTICALCABLESEGMENT und `IfcCommunicationsAppliance` OPTICALNETWORKUNIT muss vorhanden sein.

**Smart Home.** KNX hat kein offizielles Mapping auf IFC; ETS 6 exportiert ein semantisches Modell als JSON-LD [V]. Die Brücke zu `IfcSensor`, `IfcActuator` und `IfcSwitchingDevice` ist selbst zu bauen und nicht Gegenstand dieses Kapitels. Für Beleuchtungsstromkreise im Wohnbau ist eine Leitungsführung als ganzzahlige Netzflussoptimierung vorgeschlagen worden; die Arbeit ist nur nach Titel und Referenzen eingeordnet, ob sie Zonen und Ständerwände kennt, ist ungeprüft [@huang2026bimintegrated] [U].

## 13.2 Trinkwasser kalt und warm, Zirkulation, Hygiene

**Spitzendurchfluss.** DIN 1988-300:2012-05 bestimmt für Wohngebäude den Spitzendurchfluss aus der Summe der Berechnungsdurchflüsse:

$$\dot V_S = 1{,}48 \cdot \left(\textstyle\sum \dot V_R\right)^{0{,}19} - 0{,}94 \quad [\mathrm{l/s}], \qquad 0{,}2 \le \textstyle\sum \dot V_R \le 500\ \mathrm{l/s}$$

Ein zweiter Waschtisch in derselben Sanitäreinheit zählt nicht mit (Recherche 08) [V]. Die Berechnungsdurchflüsse je Armatur stehen in Tabelle 2 der Norm oder beim Hersteller; die Tabelle wurde nicht eingesehen [U]. Sie sind deshalb Datenlieferung DAT-13-04. Die Geschwindigkeit ist eine Begrenzung, keine Dimensionierungsgröße: Am Hausanschluss gelten höchstens 2 m/s, in Verbrauchsleitungen je nach Einzelwiderständen bis 5 m/s [V]. Das vereinfachte Verfahren nach DIN EN 806-3 ist nur für Wohngebäude bis sechs Wohnungen zulässig [V].

> **Beispiel 13.2 (Vorbemessung).** Mit ΣV̇_R = 2,0 l/s ergibt sich V̇_S = 1,48 · 2,0^0,19 − 0,94 = 0,748 l/s. Bei 2 m/s ist der kleinste Innendurchmesser 21,8 mm. Das Mehrschichtverbundrohr 26 × 3 (*d*_i 20 mm) ergäbe 2,38 m/s und ist zu klein, 32 × 3 (*d*_i 26 mm) ergibt 1,41 m/s. Die Rechnung steht als Testfall in `tga-dimensionierung.yaml` (`TW.Spitzendurchfluss`, `TW.Innendurchmesser-Vorbemessung`). Sie ist eine Vorbemessung; der Druckverlustnachweis bleibt beim Fachplaner (E13.10).

**Hygiene.** Die Hygieneregeln wirken im Router als Pfad- und Kantenbedingungen:

- **DVGW W 551 (2004).** Einfamilien- und Zweifamilienhäuser sind immer Kleinanlagen. Der Speicheraustritt liegt bei mindestens 60 °C, der Zirkulationsrücklauf bei mindestens 55 °C. Ohne Zirkulation darf jeder Fließweg vom Speicher zur Zapfstelle höchstens 3 l enthalten; die Zirkulation zählt nicht mit [V].
- **3-Liter-Regel als Ressource.** Der Wasserinhalt ist Σ π/4 · *d*_i² · *L*. Mit den Herstellerwerten 0,113 l/m (16 × 2) und 0,201 l/m (20 × 2) entspricht 3 l etwa 26,5 m bzw. 14,9 m Leitung (Recherche 16) [V Rechnung]. B14 führt die Warmwasser-Stichleitung 16 × 2 in der Küche mit 1,2 l ohne Zirkulation; sie ist damit auch von der Dämmpflicht nach GModG ausgenommen (13.9.2) [V Prototyp].
- **DIN 1988-200 und VDI/DVGW 6023.** Kaltwasser soll nach 30 s Zapfen höchstens 25 °C haben, nicht planmäßig durchflossene Strecken sind auf 10 × DN zu begrenzen, und Stagnation ist zu vermeiden [V]. Ein Mindestabstand zu Wärmequellen als Zahl ist nicht belegt. Die Parallelführung von Kaltwasser mit Warmwasser, Heizung oder Heizkreisen der Fußbodenheizung wird deshalb nur als Strafterm im Router geführt, nicht als harte Grenze [U].

Die Lage des Speichers wird so zur Entwurfsentscheidung mit hygienischer Folge: Eine Stichleitung 20 × 2 von 15,5 m enthält 3,12 l und verletzt die Regel (Testfall T5 in `routing-graph.md`). Alternativen sind Zirkulation, anderer Speicherort oder kleinere Nennweite im Rahmen der Geschwindigkeitsgrenze.

## 13.3 Abwasser mit Lüftung über Dach

**Anschlusswerte und Abfluss.** DIN 1986-100:2016-12 gilt zusammen mit DIN EN 12056; ein Entwurf E DIN 1986-100:2025-06 liegt vor (Recherche 08) [V]. Für System I sind die Anschlusswerte in mehreren Herstellerunterlagen übereinstimmend angegeben, unter anderem Waschtisch 0,5, Dusche ohne Stöpsel 0,6, Küchenspüle, Geschirrspüler und Waschmaschine je 0,8 sowie WC mit 6 l Spülung 2,0 l/s [V]. Der Schmutzwasserabfluss ist

$$Q_{ww} = \max\left(K \cdot \sqrt{\textstyle\sum DU};\ \max_i DU_i\right), \qquad K = 0{,}5 \text{ (Wohnhaus)}$$

> **Beispiel 13.3 (Bad).** WC 2,0, Dusche 0,6, Waschtisch 0,5 l/s: ΣDU = 3,1 l/s, 0,5 · √3,1 = 0,88 l/s. Maßgeblich ist aber der größte Einzelwert, also *Q*_ww = 2,0 l/s. Eine Leitung ohne WC mit Küche, Geschirrspüler, Waschmaschine, Dusche und Waschtisch (ΣDU = 3,5 l/s) ergibt dagegen 0,935 l/s, weil hier die Wurzelformel über dem größten Einzelwert von 0,8 l/s liegt. Beide Fälle stehen als Testfälle in `AW.Schmutzwasserabfluss`.

Die Nennweite folgt aus der hydraulischen Leistungsfähigkeit der Leitungsart. Für die WC-Anschlussleitung bestimmt das Vorwandsystem den Anschlussbogen: Das Vorwandelement eines Herstellers führt einen Anschlussbogen Ø 90 mit Übergang auf 110 mm (Recherche 16) [V].

**Gefälle und unbelüftete Anschlussleitungen.** Unbelüftete Anschlussleitungen brauchen mindestens 1 %, belüftete 0,5 %, Sammel- und Grundleitungen im Gebäude 0,5 %; außerhalb des Gebäudes gilt 1 : DN (Kapitel 14a) [V]. Eine unbelüftete Einzelanschlussleitung darf höchstens 4 m lang sein, höchstens drei 90°-Umlenkungen ohne den Anschlussbogen haben und höchstens 1 m Höhendifferenz überwinden [V]. Diese vier Grenzen sind **Ressourcen eines Pfades**, nicht Eigenschaften einer Kante. Der Router trägt sie deshalb im Suchzustand mit (13.10.4).

Das Gefälle kostet Aufbauhöhe. B14 rechnet die benötigte Höhe einer Leitung im Fußbodenaufbau als Außendurchmesser plus zweimal Dämmung plus Gefällehöhe [V Prototyp]. Eine Anschlussleitung DN 50 von 2,45 m mit 1 % braucht 50 + 24,5 = 74,5 mm (Testfall `AW.Gefaellehoehe`). Im Trockenaufbau der Variante B von B14 führt der Prototyp die Rinnenleitung deshalb in der Balkenlage parallel zu den Balken [V Prototyp].

**Lüftung über Dach.** Jede Schmutzwasserfallleitung wird über Dach entlüftet, und zwar in der Nennweite der Fallleitung. Belüftungsventile nach DIN EN 12380 sind im Einfamilienhaus als Hauptlüftung nur zulässig, wenn mindestens die Fallleitung mit der größten Nennweite über Dach geht. Anlagen ohne Fallleitung brauchen mindestens eine Lüftung DN 70 über Dach [V]. Die Mündung muss nahe Aufenthaltsräumen mindestens 1 m über dem Fenstersturz oder mindestens 2 m seitlich davon liegen (Recherche 16) [V].

> **Beispiel 13.4 (B15, Mündung).** Die Hauptlüftung DN 100 der Fallleitung SW-01 mündet 1,6 m seitlich und nur 0,3 m über dem Sturz des Dachfensters DF-01. B15 meldet einen Verstoß und schlägt zwei Alternativen vor: die Mündung auf 7,30 m anheben (+0,70 m) oder den seitlichen Abstand auf 2 m vergrößern (es fehlen 0,4 m) [V Prototyp, `ausgabe/b15_bericht.txt`]. Die Regel steht als `DE.DIN1986-100.Muendungsabstand` im Katalog.

Ob die Mündung abgedeckt werden darf, ist widersprüchlich belegt; vor dem Einbau ist der Entwurf 2025-06 zu prüfen (Recherche 16) [U].

**Schallschutz.** DIN 4109-1:2018 schützt nur **fremde** schutzbedürftige Räume. Im freistehenden Einfamilienhaus gibt es deshalb öffentlich-rechtlich keine Anforderung an Abwasserleitungen; der Schallschutz der Fallleitung ist dort Vertragsqualität (Recherche 08) [V]. Die körperschallentkoppelte Durchführung mit Dämmschlauch, Schellen mit Einlage und gestopftem Gefach bleibt trotzdem Standard der Konstruktion (13.9). Im Mehrfamilienhaus ändert sich die Lage (13.12).

## 13.4 Lüftung nach DIN 1946-6 mit Kanalnetz

**Lüftungskonzept.** DIN 1946-6:2019-12 verlangt ein Lüftungskonzept. Lüftungstechnische Maßnahmen sind notwendig, wenn der Luftvolumenstrom durch Infiltration kleiner ist als der zum Feuchteschutz nötige Volumenstrom der Nutzungseinheit. Anhang A enthält dafür ein normatives Ablaufschema [@din1946-6] (Recherche 08) [V]. Die App bildet das Ablaufschema als Entscheidungsbaum ab (`DE.DIN1946-6.Lueftungskonzept`). Beiblatt 1:2025-06 enthält Beispielrechnungen; sie sind als Validierungsfälle zu übernehmen [V].

**Luftvolumenstrom.** Der Gesamt-Außenluftvolumenstrom der Nutzungseinheit ist

$$q_v = f \cdot \left(-0{,}002 \cdot A_{NE}^2 + 1{,}15 \cdot A_{NE} + 11\right)\ \mathrm{m^3/h}$$

mit *f* = 0,7 für reduzierte Lüftung, 1,0 für Nennlüftung und 1,3 für Intensivlüftung. Unter 20 m² wird mit 20 m² gerechnet, über 210 m² mit einem Zuschlag von 0,4 m³/h je m² [V]. Der Faktor für die Lüftung zum Feuchteschutz (typisch 0,3 im Neubau) und die genaue Lesart der Fortschreibung über 210 m² sind unsicher [U]. Ventilatorgestützte Systeme werden mindestens für Nennlüftung ausgelegt:

$$q_{v,ges,NL} = \max\left(q_{v,NE,NL};\ \min\left(\textstyle\sum q_{v,Abluft};\ 1{,}2 \cdot q_{v,NE,NL}\right)\right)$$

Bei vielen Ablufträumen wird eine Gleichzeitigkeit angesetzt [V].

> **Beispiel 13.5 (140 m²).** Für *A*_NE = 140 m² ergibt die Formel 92,96 m³/h (reduziert), 132,8 m³/h (Nennlüftung) und 172,64 m³/h (intensiv). Ein fensterloses Bad mit 40 m³/h und ein WC mit 20 m³/h (Beispielwerte aus einer DIN-Auslegung zu DIN 18017-3) [U für DIN 1946-6] ergeben Σ Abluft = 60 m³/h. Maßgeblich bleibt die Nennlüftung mit 132,8 m³/h. Ein Zuluftraum mit 60 m³/h braucht bei einem Flexrohr da 75 mit höchstens 28 m³/h je Strang drei Stränge (Herstellerwert) [V Hersteller]. Alle Werte stehen als Testfälle in `tga-dimensionierung.yaml`.

**Kanalnetz.** Die Raumrollen bestimmen die Topologie: Zuluft in Wohn- und Schlafräume, Abluft aus Küche, Bad und WC, Überströmung über den Flur (Recherche 08) [V Prinzip, U Durchlassmaße]. Für Rohre gelten Herstellerwerte (da 75 bis 28 m³/h, da 90 bis 39 m³/h, Flachkanal 130 × 52 mm bis 45 m³/h, Biegeradius ≥ 1 × D) (Recherche 16) [V Hersteller]. Das Netz ist ein Baum vom Gerät zu den Durchlässen, also ein Fall für die Steiner-Näherung in 13.10.

**Brandschutz und Schall.** Art. 39 Abs. 2 und 3 BayBO regeln nichtbrennbare Lüftungsleitungen und die Überbrückung feuerwiderstandsfähiger Bauteile. Diese Absätze gelten nicht in Gebäudeklasse 1 und 2 und nicht innerhalb von Wohnungen [@baybo2026] (Recherche 08) [V]. Im Einfamilienhaus ist die Lüftungsanlagen-Richtlinie deshalb praktisch nicht einschlägig. Abs. 4 bleibt: Abluft wird ins Freie geführt, nicht in Abgasanlagen [V]. Für Geräusche der eigenen Lüftungsanlage nennt DIN 4109-1 in Tabelle 10 einen Höchstwert von 30 dB(A) in Wohn- und Schlafräumen; die Tabellenlesung ist unscharf [U]. Die Regel `DE.DIN4109-1.RLT-eigene-Wohnung` ist deshalb nur weich.

Lüftung und Schallschutz gegen Außenlärm hängen zusammen: Wer für den Schallschutz geschlossene Fenster annimmt, muss die Lüftung anders sicherstellen [@harvieclark2019assessing]. B19 nutzt diese Kopplung bereits als Kompensation (Kapitel 9.4.8).

## 13.5 Heizung: Heizlast, Fußbodenheizung, hydraulischer Abgleich

**Heizlast.** Die Norm-Heizlast wird raumweise nach DIN EN 12831-1 mit DIN/TS 12831-1:2020-04 bestimmt. Die Norm-Innentemperatur beträgt im Bad 24 °C, in Wohnräumen 20 °C. Die Norm-Außentemperatur ist ortsabhängig (Recherche 08) [V für 24 °C, U für Ortswerte]. Ob die App einen eigenen Rechenkern erhält oder ein Fremdwerkzeug anbindet, ist offen. Die Regel `DE.DINEN12831.Heizlast-raumweise` ist deshalb eine R2-Regel: Sie prüft, dass für jeden beheizten Raum eine Heizlast mit Temperaturen, Werkzeug und Version im Modell steht. Ohne sie kann die Fußbodenheizung nicht ausgelegt werden.

**Fußbodenheizung.** Nach DIN EN 1264 darf die Oberflächentemperatur in der Aufenthaltszone höchstens 29 °C, in der Randzone 35 °C und im Bad 33 °C betragen, also *θ*_i + 9 K. Ausgelegt wird mit einem Wärmedurchlasswiderstand des Belags von 0,10 m²K/W, im Bad mit 0, und einer Spreizung von 5 K im Auslegungsraum [V]. Die Grenze des Belagwiderstands liegt bei 0,15 m²K/W (Recherche 16) [V]. B14 wendet sie an: Teppich auf Fußbodenheizung ergibt *R*_λ,B = 0,233 m²K/W und wird als weiche Meldung ausgegeben (ANF-09-26) [V Prototyp]. Für die Heizkreise gelten Herstellerregeln: höchstens 100 m Kreislänge (Maximum 110 m, ideal 60 m), höchstens 300 mbar Druckverlust und eine Rohrlänge je m² von 100 / VA in cm [U, keine Norm].

> **Beispiel 13.6 (Heizkreise).** Ein Raum mit 20 m² Heizfläche und 15 cm Verlegeabstand braucht 20 · 100 / 15 = 133,3 m Rohr. Das überschreitet die Kreislänge von 100 m; der Raum wird in zwei Kreise geteilt. Bei 12 m² und 10 cm ergeben sich 120 m, ebenfalls zwei Kreise. Die Zuleitung zum Verteiler kommt hinzu (Testfälle in `HZ.FBH-Rohrlaenge`).

**Hydraulischer Abgleich und Recht.** Für den hydraulischen Abgleich gibt es das VdZ-Formular mit den Verfahren A und B; das Formular wurde nicht geprüft [U]. Die App exportiert die Voreinstellwerte je Kreis und prüft ihre Vollständigkeit (R4-Regel `DE.VdZ.Hydraulischer-Abgleich`). Seit dem 29.07.2026 heißt das Gebäudeenergiegesetz Gebäudemodernisierungsgesetz, und die 65-%-Pflicht für erneuerbare Energie ist entfallen [@gmodg2026] (Recherche 08) [V]. Die Wahl des Wärmeerzeugers wird damit zur Frage von Kosten, Schall und Aufstellung (13.6).

## 13.6 Wärmepumpe: Aufstellung als Optimierung

### 13.6.1 Rechtsrahmen und Rechenverfahren

Eine Luft-Wasser-Wärmepumpe ist eine nicht genehmigungsbedürftige Anlage nach § 22 BImSchG. Verbindlich ist die TA Lärm, nicht die LAI-Tabelle (Recherche 22) [V]. Im allgemeinen Wohngebiet gilt nachts ein Richtwert von 40 dB(A), maßgeblich ist die lauteste volle Nachtstunde. Die Zuschläge für Ton- und Impulshaltigkeit betragen 0, 3 oder 6 dB, Zwischenwerte gibt es nicht. Ohne Herstelleraussage ist *K*_T = 3 dB anzusetzen [V]. Der Immissionsort liegt 0,5 m vor der Mitte des geöffneten Fensters; bei unbebautem Nachbargrundstück liegt er am Rand der überbaubaren Fläche (A.1.3 b) [V]. Geräuschspitzen dürfen nachts den Richtwert um höchstens 20 dB überschreiten [V]. Der Beurteilungspegel wird intern ungerundet gerechnet und in vollen dB nach DIN 1333 mit dem Richtwert verglichen [@din1333] [V].

Die Ausbreitung rechnet B20 nach DIN ISO 9613-2 mit Divergenz, Luftabsorption, Bodeneffekt, Abschirmung und Spiegelquellen bis zur zweiten Ordnung; die LAI-Tabelle 5 reproduziert B20 in allen 41 Werten auf höchstens 0,11 m (Recherche 22) [V]. Bei freier Sicht liegen detaillierte Rechnung, LAI und BWP-Rechner innerhalb von ±1 dB. Hinter dem eigenen Haus weicht der Pauschalwert „abgewandte Seite 15 dB“ um −6,7 bis +9,7 dB ab, und die 500-Hz-Näherung unterschätzt hinter Schirmen um bis zu 9,6 dB [V Prototyp]. Einzelheiten stehen in Kapitel 9.4.9.

### 13.6.2 Aufstellregeln

Neben dem Schall begrenzen Sicherheit, Luftführung, Baurecht und Leitungsführung den Aufstellort (Recherche 22) [V, Maße herstellerspezifisch]:

- **R290-Schutzbereich.** Im Schutzbereich dürfen keine Zündquellen, Fenster, Türen, Lüftungsöffnungen, Lichtschächte, Einläufe oder Senken liegen. Er darf nicht auf Nachbargrund oder Verkehrsflächen reichen; typisch sind 1 m am Boden und 0,5 m an der Oberkante. Im Holzbau müssen Durchführungen und Leerrohre im Schutzbereich gasdicht sein [V Hinweis, U Detail].
- **Luftführung.** Ansaugung mindestens 200 mm zur Wand, Ausblas mit mehr als 1 m Freiraum, mindestens 3 m zu Gehweg und Terrasse, keine Nischen, Sockel mindestens 100 mm über der Schneehöhe, Kondensat frostfrei [V Beispiel].
- **Abstandsflächen.** Wärmepumpen und Einhausungen bis 2 m Höhe lösen in Bayern keine Abstandsflächen aus (Art. 6 Abs. 1 Satz 3 Nr. 4 BayBO) [@baybo2026] [V].
- **Körperschall.** Leichte Holzrahmenwände strahlen Körperschall stark ab [U, nicht quantifiziert]. Die LAI empfiehlt elastische Lagerung und flexible Rohranschlüsse [V]. Daraus folgt die weiche Firmenregel `M.Firma.WP-Koerperschall`: keine Wandkonsole an der Holzrahmenwand eines Aufenthaltsraums, bevorzugt eine Bodenkonsole auf eigenem Fundament.
- **F-Gase.** Luft-Wasser-Split-Geräte bis 12 kW mit einem Treibhauspotenzial von mindestens 150 dürfen ab dem 01.01.2027 nicht mehr in Verkehr gebracht werden, ab 2035 gilt das für jedes F-Gas. Monoblock-Geräte bis 12 kW sind ab 2027 bei GWP ≥ 150 und ab 2032 bei jedem F-Gas betroffen (VO (EU) 2024/573, Anhang IV) [V]. Die Verbote betreffen das Inverkehrbringen, nicht den Betrieb [V].

**E13.7 – Standard ist ab 2027 die Monoblock-Wärmepumpe mit R290; der Schutzbereich ist eine harte geometrische Regel.** *Entscheidung.* Die Bemusterung bietet Split-Geräte mit F-Gasen nur an, wenn der Liefertermin vor dem Stichtag liegt; die Regel `EU.FGas.2024-573.Inverkehrbringen` prüft gegen den Liefertermin, nicht gegen das Planungsdatum. *Begründung.* Ein R32-Split, der 2026 geplant und 2027 geliefert wird, ist ein Lieferrisiko (Recherche 22) [V]. *Beleg.* B20 gibt für die Split-Variante „zulässig bis 2026-12-31, danach Verbot des Inverkehrbringens“ aus [V, Test `test_f_gase_split_r32_ab_2027_verboten`].

### 13.6.3 Das Optimierungsproblem

Die Aufstellung ist ein Optimierungsproblem über einer Kandidatenmenge *P* (Raster 0,5 m auf dem Grundstück) mit Immissionsorten *I*:

$$\max_{p \in P_{zul}}\ \min_{i \in I}\ \big(\mathrm{IRW}_N(i) - L_{r,N}(p, i)\big)$$

$$P_{zul} = \{p : \text{Schutzbereich}(p) \cap (\text{Öffnungen} \cup \text{Senken}) = \emptyset,\ \text{Schutzbereich}(p) \subset \text{Grundstück},\ L_{Leitung}(p) \le L_{max},\ \text{Ausblas frei},\ h \le 2\,\mathrm{m}\}$$

Die harten Bedingungen stammen aus fünf Regeln (`M.Hersteller.R290-Schutzbereich`, `M.Hersteller.WP-Luftfuehrung`, `BY.BayBO.6.WP-Hoehe`, `DE.TALaerm.WP-Richtwert`, `DE.TALaerm.WP-Spitzenpegel`). B20 löst das Problem durch vollständige Aufzählung. Bei Gleichstand entscheidet die kürzere Leitung, dann die Koordinate; das Verfahren ist deterministisch [V Prototyp].

> **Beispiel 13.7 (B20).** Grundstück 18 × 32 m im allgemeinen Wohngebiet, eigenes Haus 10 × 10 m, zwei Nachbarhäuser mit vier Immissionsorten, ein unbebautes Grundstück im Osten mit Linien-Immissionsort, Gartenmauer 2,0 m. Beispielgerät: Monoblock R290, 7 kW, *L*_WA Tag/Nacht/max = 60/55/63 dB, *K*_T = 3 dB. Von 2 304 Rasterpunkten sind 834 zulässig. Die häufigsten Ausschlussgründe sind der Schutzbereich über der Grenze (564), die Leitungslänge (499) und der Wandabstand zum Haus (484). Das Optimum liegt im Vorgarten bei (7,25 m; 1,75 m) mit 12,9 dB kleinster Reserve und 17,3 m Leitung; am Schlafzimmer des Nachbarn ergibt sich *L*_r,N = 25,4 dB(A), der Spitzenpegel beträgt 30,4 dB(A) und liegt weit unter 60 dB(A). Die typische Installateurwahl „Ostseite vor dem Hauswirtschaftsraum“ ist akustisch in Ordnung, aber unzulässig: Das HWR-Fenster liegt im Schutzbereich [V, `ausgabe/b20_waermepumpe.md`].

Die lexikografische Zielfunktion von B20 verdeckt einen Zielkonflikt. Recherche 22 hat ihn an zwei Teilräumen gezeigt: Die Ostseite hat die kürzeste Leitung ihres Teilraums (7,3 m) bei 7,1 dB Reserve, der Vorgarten 5,8 dB mehr Reserve bei längerer Leitung [V]. Für dieses Kapitel wurde die zulässige Menge von B20 mit den Funktionen des Prototyps (`optimiere`) neu ausgewertet, ohne dessen Ausgaben zu ändern (Nachrechnung am 27.09.2026) [V]:

| Formulierung | Ergebnis |
|---|---|
| Pareto-Front (Reserve maximieren, Leitungslänge minimieren) | 21 nicht dominierte Punkte von 4,3 m / 6,98 dB bis 17,3 m / 12,92 dB |
| kürzeste Leitung überhaupt | (15,75 m; 12,25 m): 4,3 m, 6,98 dB; am Linien-Immissionsort 33,0 dB(A) |
| ε-Bedingung Reserve ≥ 6 dB (Irrelevanzziel) | 720 von 834 zulässigen Punkten; kürzeste Leitung wie oben, 4,3 m |
| ε-Bedingung Reserve ≥ 10 dB | (11,75 m; 6,75 m): 7,8 m, 10,19 dB |
| ε-Bedingung Reserve ≥ 12 dB | (8,25 m; 3,75 m): 14,3 m, 12,26 dB |

Der Befund ist für die Praxis bemerkenswert. Nur 0,75 m östlich und 0,25 m nördlich der unzulässigen Installateurwahl liegt ein Punkt, der den Schutzbereich einhält, das Irrelevanzziel an allen Immissionsorten erfüllt und die kürzeste Leitung des ganzen Grundstücks hat. Nach eigener Einschätzung findet ein Planer ihn ohne Rechnung kaum, eine vollständige Rastersuche findet ihn sicher. Der Punkt liegt allerdings dicht an der Grenze des Schutzbereichs, dessen Maße hier Beispielwerte sind. Mit den realen Herstellerdaten (DAT-13-08) kann er entfallen.

**E13.6 – Die Wärmepumpe wird mehrkriteriell aufgestellt; Voreinstellung ist die kürzeste Leitung unter dem Irrelevanzziel.** *Entscheidung.* Die App berechnet die zulässige Menge und die Pareto-Front aus Reserve und Leitungslänge. Voreingestellt ist die ε-Formulierung „kürzeste Leitung unter der Bedingung Reserve ≥ 6 dB“. Sie entspricht dem Firmenziel `M.Firma.WP-Irrelevanzziel`, das die Rechtsgrenze monoton verschärft (Kapitel 9.4.9). Der Kunde sieht die Front als Karte und kann einen anderen Punkt wählen, solange er zulässig ist. *Begründung.* Die maximale Reserve ist kein Wert an sich, sobald die Zusatzbelastung irrelevant ist. Eine kürzere Leitung spart Kosten und Wärmeverluste. Die Gewichtung ist eine Wertentscheidung, die offengelegt werden muss. *Beleg.* Nachrechnung oben [V]; B20 und Recherche 22 [V].

**Abgrenzung zum BWP-Schallrechner.** Der Rechner bildet Linien-Immissionsorte an der Baugrenze, Reflexionen an fremden Fassaden, geometrische Schirme, mehrere Geräte und die Vorbelastung nicht ab. Er schlägt den Ruhezeitenzuschlag pauschal auf den ganzen Tag und ist dort um 4,1 dB konservativer als die TA Lärm (Recherche 22) [V]. Für den Bauantrag genügt er in einfachen Fällen. Für die Aufstellungsoptimierung ist er ungeeignet, weil er die Abschirmung durch das eigene Haus nur pauschal kennt.

## 13.7 Lichtplanung: Leuchtendaten, Tageslicht, Empfehlungen

**Normlage.** Für die Lichtplanung in Wohnungen gibt es **keine verbindliche Norm**. DIN EN 12464-1 gilt für Arbeitsstätten [U Umfang]. DIN 18015-2 regelt nur die Anschlüsse: Beleuchtungsauslässe je Raum, im Flur nach Länge (Recherche 08) [V; Flurregel je 6 m U]. Für Tageslicht sind DIN EN 17037 und DIN 5034-1 Bezugsnormen [@din2019tageslicht; @din5034-1]. Ihre Stufen sind im Einfamilienhaus nicht verlangt und erscheinen als Empfehlung R5 (Kapitel 9b, R5-LICHT-01 und -02).

**Leuchtendaten.** Der Austausch photometrischer Daten ist dagegen gelöst (Recherche 08) [V]:

- GLDF ist ein ZIP-Container von DIAL und RELUX mit `product.xml`, Photometrie aus EULUMDAT, IES LM-63 oder IES-XML und Geometrie im Format L3D. Das XSD steht unter MIT-Lizenz.
- EULUMDAT und IES beschreiben die Lichtstärkeverteilung im C-γ-System.
- IFC 4.3 bildet Leuchten als `IfcLightFixture` (POINTSOURCE, DIRECTIONSOURCE, SECURITYLIGHTING) mit `IfcLamp` ab. `IfcLightSourceGoniometric` verweist über `LightDistributionDataSource` auf eine externe EULUMDAT- oder IES-Datei oder trägt die Verteilung selbst als `IfcLightIntensityDistribution`. Dazu kommen `Pset_LightFixtureTypeCommon` und `Pset_SpaceLightingDesign` mit der Beleuchtungsstärke [@iso2024ifc].
- Simuliert wird mit Radiance (BSD-artige Lizenz); DIALux und Relux sind proprietär und lesen GLDF. Der PyPI-Parser für EULUMDAT steht unter AGPL und wird gemieden; das Format ist einfach genug für einen eigenen Parser [V].

**E13.8 – Licht wird in drei Klassen geregelt: Anschlüsse hart, Leuchtendaten als Informationsanforderung, Lichtqualität als Empfehlung.** *Entscheidung.* `DE.DIN18015-2.Beleuchtungsauslaesse` ist eine R1-Regel im Firmenprofil. `M.Firma.Leuchtendaten` ist eine R2-Regel ab Reifegrad A: Jede gelieferte Leuchte trägt photometrische Daten, und ein GLDF-Container besteht die XSD-Prüfung. Beleuchtungsstärken, Farbtemperatur und melanopische Wirkung sind R5-Empfehlungen ohne Sperrwirkung. *Begründung.* Ohne Norm gibt es keine Grundlage für eine harte Grenze. Eine Beleuchtungsstärke „für Küchen“ aus einer Arbeitsstättennorm zu übernehmen, wäre eine erfundene Regel. *Beleg.* Recherche 08 [V]; Kapitel 9b zur Klasse R5.

**Nicht-visuelle Wirkung.** Für die Wirkung von Licht auf den Tag-Nacht-Rhythmus gibt es quantitative Konsensempfehlungen in melanopischer tageslichtäquivalenter Beleuchtungsstärke (mEDI) am Auge: tagsüber mindestens 250 lx, abends höchstens 10 lx [@brown2022recommendations]. Die Größe stützt eine Reanalyse von Laborstudien [@brown2020melanopic], die Metrik ist in CIE S 026 genormt [@cie2018s026]. Die Meta-Analyse zum Abendlicht findet Dosis-Wirkungs-Beziehungen für Einschlaflatenz und Schlafeffizienz, aber Gesamteffekte mit Konfidenzintervallen, die null einschließen [@cajochen2022evening]. Fast die Hälfte der untersuchten Haushalte war abends hell genug, um Melatonin um die Hälfte zu unterdrücken [@cain2020evening]. Die mEDI einer Leuchte ist das Produkt aus photopischer Beleuchtungsstärke und dem melanopischen Wirkungsverhältnis (mDER) ihres Spektrums; für dessen Bestimmung gibt es Rechenmodelle [@trinh2023medi] und ein quelloffenes Werkzeug unter GPL-3.0 [@spitschan2021luox]. Ein Review zur Simulation nicht-visueller Lichtwirkung im Gebäudeentwurf findet keine gemeinsame Methode [@gkaintatzimasouti2022simulations]. Im Modell ist die melanopische Bewertung deshalb nur vereinfacht möglich.

Kritisch ist die Nähe zum Marketing: „Human-Centric Lighting“ ist durch irreführende Werbeversprechen belastet [@houser2020humancentric], ein fünfstufiger Entwurfsprozess trennt Wissen von Werbung [@houser2021humancentric], und eine Übersicht zur Wohnbeleuchtung nennt keine quantifizierten Schwellen [@ticleanu2021impacts]. Die App empfiehlt deshalb nur, wo eine Quelle die Schwelle trägt, und nennt den Evidenzgrad.

**Tabelle 13.1: Vorgeschlagene Licht-Empfehlungen R5 (Ergänzung zu `empfehlungen.yaml`)**

| ID | Empfehlung | Kennzahl, Schwelle | Evidenz | Quelle |
|---|---|---|---|---|
| R5-LICHT-05 | Abendlicht in Wohn- und Schlafräumen dimmbar und warm | mEDI am Auge ≤ 10 lx in der Abendszene; Nachweis über mDER der gewählten Leuchte | B-W (Konsens, Laborevidenz), Effektgröße unsicher | [@brown2022recommendations; @cajochen2022evening; @cain2020evening] |
| R5-LICHT-06 | Tagesaufenthaltsplatz mit hoher melanopischer Wirkung | mEDI am Auge ≥ 250 lx tagsüber aus Tages- und Kunstlicht | B-W | [@brown2022recommendations; @brown2020melanopic] |
| R5-LICHT-07 | Leuchtendaten mit Spektrum für die Bewertung | mDER oder Spektrum in GLDF vorhanden | C (Methode) | [@cie2018s026; @trinh2023medi] |

Die Empfehlungen ergänzen R5-LICHT-03 (Verdunkelung) und R5-LICHT-04 (Arbeitsplatz am Fenster) aus Kapitel 9b. Sie gehören in die Bemusterung von Leuchten und Schalterprogramm (Kapitel 12). Photopische Mindestbeleuchtungsstärken für Wohnräume werden nicht vorgegeben; die Firma kann sie als eigene Planungswerte in ihrem Profil hinterlegen (DAT-13-09).

## 13.8 IFC-Abbildung: Systeme, Segmente, Ports, Verbindungen, Durchbrüche

IFC 4.3 trägt die gesamte TGA: Ein Testmodell mit System, Rohren, Ports, Port-Verbindung und Aussparung validiert mit EXPRESS-Regeln fehlerfrei (Recherche 08), B15 ebenso [V]. Tabelle 13.2 ergänzt das Mapping aus Kapitel 8 (`ifc-mapping.csv`) um die TGA-Beziehungen.

**Tabelle 13.2: TGA in IFC 4.3**

| Konzept | IFC-Klasse, PredefinedType | Beziehung | Befund |
|---|---|---|---|
| Gewerk-System | `IfcDistributionSystem` ELECTRICAL, LIGHTING, DOMESTICCOLDWATER, DOMESTICHOTWATER, SEWAGE, WASTEWATER, RAINWATER, VENT, VENTILATION, HEATING, DATA, COMMUNICATION | `IfcRelAssignsToGroup`, `IfcRelServicesBuildings` | Kanalentlüftung VENT, Wohnungslüftung VENTILATION [V] |
| Stromkreis | `IfcDistributionCircuit` | Untersystem | ersetzt IfcElectricalCircuit [V] |
| Rohr, Kanal, Leerrohr, Kabel | `IfcPipeSegment`, `IfcDuctSegment`, `IfcCableCarrierSegment` CONDUITSEGMENT, `IfcCableSegment` | Ports über `IfcRelNests` | Segment braucht immer eine Platzierung [V] |
| Formteil | `IfcPipeFitting`, `IfcDuctFitting`, `IfcCableCarrierFitting` (BEND, JUNCTION, TRANSITION) | 2–3 Ports | kein „IfcElbow“ [V] |
| Anschlusspunkt | `IfcDistributionPort` (PIPE, DUCT, CABLE, CABLECARRIER), FlowDirection SOURCE/SINK | `IfcRelNests`, `IfcRelConnectsPorts` | `IfcRelConnectsPortToElement` deprecated [V] |
| Verteiler | `IfcDistributionBoard` CONSUMERUNIT, DISTRIBUTIONBOARD | Ports | `IfcElectricDistributionBoard` deprecated [V] |
| Dose, Endgeräte | `IfcJunctionBox`, `IfcOutlet`, `IfcSanitaryTerminal`, `IfcWasteTerminal`, `IfcAirTerminal`, `IfcSpaceHeater`, `IfcLightFixture`, `IfcStackTerminal` COWL | Zuordnung zum System | [V] |
| Wärmepumpe | `IfcUnitaryEquipment` USERDEFINED (ObjectType `AirToWaterHeatPump_Monoblock`) bzw. SPLITSYSTEM | System HEATING | keine IfcHeatPump [V]; Schutzbereich `IfcSpatialZone` USERDEFINED (Kapitel 8) |
| Aussparungsvorschlag | `IfcVirtualElement` PROVISIONFORVOID + `Pset_ProvisionForVoid` | ohne Material, Tiefe ≥ Bauteildicke | Proxy-Variante deprecated [V] |
| freigegebene Öffnung | `IfcOpeningElement` OPENING | `IfcRelVoidsElement` je Teil, `IfcRelInterferesElements` (ImpliedOrder TRUE) | im Holzbau je Schicht bzw. Stab [V] |
| Manschette, Abschottung | `IfcDiscreteAccessory` USERDEFINED | `IfcRelFillsElement` | keine IfcSealing, kein Firestop-Typ [V] |
| Dämmschlauch | `IfcCovering` WRAPPING bzw. SLEEVING | `IfcRelCoversBldgElements` | [V] |

Drei Fallen fängt nur die Validierung jeder Revision ab (E8.2): Typ-Psets hängen über `HasPropertySets` am Typ, nicht über `IfcRelDefinesByProperties`; jede Achse mit Axis braucht eine RefDirection; und `ifcopenshell.util.system.get_connected_to` folgt der Fließrichtung, sodass für die Nachbarn `get_connected_from` zu ergänzen ist (Recherche 16) [V]. Produktdaten der TGA liefert VDI 3805, die Grundlage der ISO 16757 ist. VDI 3805 ist kein IFC und braucht einen Konverter auf Typobjekt und Ports [V/U].

**Reifegrade.** Nach E8.12 genügen in Reifegrad P Endgeräte mit Lage und Aussehen; in R kommen Systeme, Segmente mit Nennweite, Ports und Aussparungsvorschläge hinzu, weil die Regeln aus 13.1 bis 13.6 sie brauchen; erst in A entstehen Öffnungen, Manschetten, Wechsel und Bearbeitungen. Dass TGA-Modelle über Detaillierungsstufen vom Vorentwurf bis zum Vorfertigungsmodell geführt werden können, zeigt ein BIM-Rahmen mit fünf Stufen; er zeigt aber auch, dass 78 % der automatisch gefundenen Kollisionen unwirksam waren [@wang2016building]. Das stützt eine Erzeugung, die Kollisionen vermeidet, statt sie nachträglich zu sortieren.

## 13.9 Dimensionierung und Durchdringungen

### 13.9.1 Nennweiten

Nennweiten sind Herstellerdaten, keine Normtabellen. `tga-dimensionierung.yaml` führt die in Recherche 16 geprüften Werte als Einzelkennwerte [V Hersteller]:

- **Trinkwasser.** Mehrschichtverbundrohr 16 × 2 (*d*_i 12 mm, 0,113 l/m), 20 × 2 (16 mm, 0,201 l/m), 26 × 3 (20 mm), 32 × 3 (26 mm) bis 63 × 4,5.
- **Abwasser.** Schallschutzrohr DN/OD 110 mit *d*_i 104,6 mm für DN 100 und DN/OD 75 mit *d*_i 71,2 mm für DN 70.
- **Elektro.** Die M-Bezeichnung des Leerrohrs ist der Außendurchmesser nach DIN EN 61386. M20 hat innen 14,1 mm (flexibel) bzw. 16,9 mm (starr), M25 18,3 bzw. 21,4 mm.

**E13.11 – Normtabellen werden nicht kopiert.** *Entscheidung.* Anschlusswerte, Nennweiten und Zonenmaße stehen als Einzelwerte mit Fundstelle in `tga-dimensionierung.yaml`, nicht als Tabelle. Wo eine Formel existiert, rechnet die App, statt eine Tabelle zu lesen. *Begründung.* Einzelne Zahlenwerte dürften als technische Fakten kaum schutzfähig sein, Tabellen dagegen schon (Kapitel 4.9, 9.7) [U]. *Beleg.* Recherche 08, Warnung 12.

### 13.9.2 Dämmung nach GModG Anlage 8

Die Mindestdämmung von Wärmeverteilungs- und Warmwasserleitungen steht jetzt in Anlage 8 des GModG [@gmodg2026]. Bezogen auf λ = 0,035 W/(m K) gilt (Recherche 16) [V]:

- bei *d*_i ≤ 22 mm 20 mm, bei 22 < *d*_i ≤ 35 mm 30 mm, bis 100 mm Dämmdicke gleich *d*_i, darüber 100 mm;
- in Wand- und Deckendurchbrüchen, an Kreuzungen und Verteilern der halbe Wert;
- zwischen beheizten Räumen verschiedener Nutzer der halbe Wert, im Fußbodenaufbau dort 6 mm;
- an Außenluft der doppelte Wert.

Ausgenommen sind Wärmeverteilungsleitungen mit frei liegender Absperrung in beheizten Räumen eines Nutzers und Warmwasser-Stichleitungen bis 3 l ohne Zirkulation. Kaltwasser und Abwasser haben keine Anforderung nach dem GModG [V]. B14 setzt die Regel in `gmodg_mindestdaemmung()` mit zehn Testfällen um [V Prototyp]. Für den Router ist die Dämmung eine Eigenschaft der **Lage**: Dieselbe Leitung 26 × 3 braucht frei verlegt 30 mm, im Deckendurchbruch aber nur 15 mm. Deshalb berechnet die App die Dämmung nach dem Routing je Segment, nicht vorher je Leitung.

### 13.9.3 Bohrungen und Durchbrüche in Holzbauteilen

Im Holzrahmenbau wird der Durchbruch nicht im Raum gerechnet, sondern im Ständer, im Balken und in der Platte. Drei Fälle sind zu unterscheiden:

- **Deckenbalken, Querbohrung.** Nach DIN EN 1995-1-1/NA, NCI NA.6.7, gilt eine Öffnung bis 50 mm als Querschnittsschwächung mit Nettoquerschnittsnachweis. Darüber liegt ein Durchbruch vor, der unverstärkt nur zulässig ist, wenn *h*_d ≤ 0,15 *h*, *h*_ro und *h*_ru ≥ 0,35 *h*, *l*_A ≥ *h*/2 und *l*_z ≥ max(1,5 *h*; 300 mm) gelten (Recherche 16) [V]. Nach dem neuen Eurocode 5, der als DIN EN 1995-1-1:2026-09 erschienen, aber nicht eingeführt ist [@en1995-2026], sind Durchbrüche in Vollholz und KVH zu verstärken; das Profil `DE-EC5-2026` gibt dazu nur Hinweise (Kapitel 9.3.2) [V Entwurfsstand, U Endfassung].
- **Senkrechte Leitung durch die Balkenlage.** Sie führt nie durch den Balken, sondern durch das Balkenfeld mit Randabstand. Sonst wird der Balken unterbrochen und über zwei Wechsel auf die Nachbarbalken abgefangen; Stich- und Wechselbalken sind nachzuweisen [V Prinzip, U Randabstand].
- **Ständer.** EC 5 hat keine eigene Bohrregel für Ständer; maßgeblich ist der Nettoquerschnitt im Druck- und Knicknachweis. Eine Primärquelle für eine Bohrregel wurde nicht gefunden (Recherche 08) [U]. B15 prüft gegen einen Firmenregel-Platzhalter von 25 % der Ständertiefe, mittig.

> **Beispiel 13.8 (B15).** Fallleitung SW-01, Schallschutzrohr DN 100 (*d*_a 110 mm) bei *x* = 3 150 mm, *y* = 2 100 mm. Die Öffnung ergibt sich aus Rohr, Dämmschlauch 9 mm und Ringspalt 10 mm: 110 + 2 · (9 + 10) = 148 mm, gerundet **Ø 150 mm**; im Dach mit luftdichter Ebene 110 + 2 · 10 = **Ø 130 mm**. Die Achse liegt 25 mm neben der Balken- *und* der Ständerachse 3 125 mm, weil Decke und Wand dasselbe 625-mm-Raster haben. Die nächste in beiden Rastern freie Achse liegt bei 3 270 mm, also 120 mm entfernt; der Platzhalter erlaubt 100 mm. B15 plant deshalb in der Decke einen Wechsel: Balken 5 wird zwischen *y* = 1 905 und 2 295 mm unterbrochen, zwei Wechsel 100/240 laufen auf die Nachbarbalken. In der Wand wird Ständer 5 ausgewechselt, weil 150 mm mehr als 25 % der Ständertiefe von 160 mm sind; die Riegel liegen bei *z* = 3 092 und 3 332 mm. Die Anschlussleitung DN 50 der Duschrinne (Ø 60 mm) quer zur Balkenlage verletzt NA.6.7, denn 60 mm > 0,15 · 240 mm = 36 mm. Das Leerrohr M25 (Ø 31 mm) ist nur eine Querschnittsschwächung [V, `ausgabe/b15_durchdringungen.json`].

Der Konflikt ist systematisch: Bei gleichem Decken- und Wandraster trifft eine Fallleitung nahe einer Achse Balken und Ständer zugleich (Recherche 16) [V Prototyp].

**E13.9 – Fallleitungen und WC-Achsen liegen auf Gefachmitte; das ist eine Entwurfsregel, keine Werkplanungsregel.** *Entscheidung.* Die weiche Regel `M.Firma.Fallleitung-Gefachmitte` wirkt schon beim Platzieren des Sanitärobjekts in Reifegrad P. Sie schlägt eine Verschiebung auf die nächste Gefachmitte vor, bevor der Kunde das Bad festlegt. Wird die Verschiebung abgelehnt, plant die App den Wechsel als IFC-Bauteil. *Begründung.* Eine Verschiebung von 120 mm im Grundriss kostet fast nichts, ein Wechsel kostet Holz, Anschlüsse und einen Nachweis. *Beleg.* B15: Mit zulässigen 150 mm wählt der Prototyp die Verschiebung ohne Wechsel [V, Test `test_verschiebung_statt_wechsel`].

### 13.9.4 Manschetten, Brand- und Schallschutz

**Luftdichtheit.** Für die luftdichte Ebene nach DIN 4108-7 gibt es Systemmanschetten, zum Beispiel für Kabel von 6 bis 12 mm, für Rohre von 15 bis 30 mm und von 100 bis 120 mm; Leerrohre werden innen mit einem Stopfen für 16 bis 40 mm abgedichtet (Recherche 16) [V Hersteller]. B15 wählt für *d*_a 110 mm im Dach die Manschette für 100 bis 120 mm und schreibt sie als `IfcRelFillsElement` ins Modell [V Prototyp]. Liegt kein freigegebenes System im Durchmesserbereich, ist das Ergebnis *unbestimmt*, nicht *erfüllt*. Die freigegebenen Systeme sind Datenlieferung DAT-13-05.

**Brandschutz.** Nach MLAR/LAR 4.1.1 ist in Gebäudeklasse 1 und 2, innerhalb von Wohnungen und für Nutzungseinheiten bis 400 m² in höchstens zwei Geschossen keine Abschottung nötig (Recherche 16) [V]. Darüber gelten Abschottungen mit gleichem Feuerwiderstand oder Erleichterungen: brennbare Rohre bis 32 mm, nichtbrennbare bis 160 mm, Abstände von 1 × bzw. 5 × *d*, Spalte bis 50 mm mit Mineralfaser oder 15 mm mit intumeszierendem Baustoff [V]. Für Holzbalkendecken gibt es keine allgemeingültige Lösung. Ein Nachweis gilt nur für die geprüfte Deckenkonstruktion; die Alternative ist ein Betonverguss als „Massivdecke“ des Nachweises, gegen Durchfallen gesichert [V Fachartikel]. Für Holzbauteile der Gebäudeklassen 4 und 5 kommt die über die BayTB 11/2025 eingeführte MHolzBauRL 2024 hinzu [@holzbaurl2024; @baytb2025] (Kapitel 9a.6). Die Regel `BY.MLAR.Abschottung` gilt ab Gebäudeklasse 3 und liefert *freigabepflichtig*, solange kein Nachweis für die eigene Decke vorliegt. Der Einführungsstatus der MLAR in Bayern ist vor dem Produktivbetrieb zu bestätigen [U].

**Schallschutz.** Durchführungen sind körperschallentkoppelt (Dämmschlauch als `IfcCovering` WRAPPING, Schellen mit Einlage, gestopftes Gefach) (Recherche 16) [V/U].

### 13.9.5 Übergabe an die Fertigung

Jede freigegebene Öffnung wird zu einer Bearbeitung des Bauteils, das sie durchdringt. BTLx beschreibt Bohrungen als `Drilling` mit StartX, StartY, Angle, Inclination, DepthLimited, Depth und Diameter; `Slot` und `Pocket` beschreiben Schlitze und Taschen [@btlx23; @compastimber] (Recherche 16) [V]. Wandanlagen lesen meist WUP; dort werden Bohrungen ab einem Grenzdurchmesser gefräst, im dokumentierten Beispiel ab 70 mm [V], und ein Freitextfeld für eine Leitungs-GUID wurde nicht gefunden [U]. Die Grenze ist ein Firmenparameter (`M.Firma.Fraesgrenze`).

> **Beispiel 13.9 (B15, BTLx).** B15 gibt fünf Bohrungen als `Drilling` aus: D1 durch die OSB-Platte des Deckenelements (Ø 150 mm), D2 durch beide Gipsfaserplatten der Wandtafel (je Ø 150 mm), D3 durch die luftdichte OSB-Ebene des Dachs (Ø 130 mm) und BD-2 durch Deckenbalken 6 (Ø 31 mm). Jede Bohrung trägt die GlobalId der Fallleitung als `UserAttribute LeitungGUID` [V, `ausgabe/b15_bearbeitungen.btlx`]. Die BTLx-Ausgabe ist nicht gegen das XSD validiert, weil es aus der Umgebung nicht erreichbar war (Recherche 16) [U]. ANF-08-22 verlangt zusätzlich das Attribut `IfcGlobalId` an jedem Part.

## 13.10 Routing-Algorithmen unter Regeln

### 13.10.1 Stand der Forschung

Die Übersicht von Blokland et al. ordnet das Leitungsrouting nach Raummodell, Routenmodell, Ziel und Constraints und unterscheidet Verzweigung, Ressourcenkonkurrenz und Dimensionalität; sie stammt überwiegend aus Schiff- und Anlagenbau [@blokland2023literature]. Für Gebäude sind vier Ansätze einschlägig:

1. **Constraint-basierte Kanalführung**, parametrisch editierbar und mit einem Industriepartner getestet [@medjdoub2018parametric]. Das passt zum Anspruch, dass der Kunde nach dem Routing noch verschieben kann.
2. **Graphsuche** mit Dijkstra, 3D-A\* und Metaheuristik für mehrere Rohre, deren Reihenfolge gesondert optimiert wird [@singh2021automating], sowie ein modifizierter A\* mit lokalem Feingitter bei Kollision, verglichen an sieben Gebäuden [@choi2022modification].
3. **Genetischer Algorithmus im Panelbau** für Luftkanäle mit Kreuzungen des Tragwerks und Fertigung im Werk in der Zielfunktion, aber ohne Bohrregeln [@baradaran2022parametric].
4. **Regelbasierte Entwässerung im Tafelbau** mit Teilung des Rohrnetzes an Tafelgrenzen und Stücklisten je Tafel, nach nordamerikanischen Regeln in Revit [@zhang2022bimbased].

Hinzu kommen Wissenskategorien der TGA-Koordination als Checkliste für eine Kostenfunktion [@korman2003knowledge] und generatives TGA-Design in frühen Phasen, das nur nach Titel eingeordnet ist [@pestana2024optimizing] [U]. Routing-Regeln liegen in den oberen Klassen der Einteilung von Solihin und Eastman, weil sie abgeleitete Geometrie und Topologie brauchen [@solihin2015classification].

**Kritische Würdigung.** Keine der Arbeiten verbindet Installationszonen, Bohrgrenzen in Ständern und Balken, Luftdichtheit und die Übergabe als Fertigungsbearbeitung. Die Arbeiten aus dem Tafelbau optimieren Kreuzungen mit dem Tragwerk als Anzahl, prüfen aber nicht, ob eine Kreuzung zulässig ist. Die Graphverfahren stammen aus Technikräumen und Massivbau. Recherche 08 hat keinen Artikel zu Routing in Holzrahmen-Wandtafeln unter Ständer- und Zonenregeln gefunden [U]. Das ist die Lücke, die dieser Abschnitt füllt. In Bonsai ist ein A\*-Router erst als Ausbaustufe geplant (Recherche 08) [V].

### 13.10.2 Das Graphmodell

**E13.3 – Geroutet wird auf einem Graphen über den konstruktiven Zellen, nicht auf einem Voxelraster.** *Entscheidung.* Knoten sind Gefache, Installationszonen, Vorwände, Schächte, Decken- und Dachfelder sowie Ports. Kanten verbinden benachbarte Zellen und tragen die Menge der Bauteile, die sie kreuzen. *Begründung.* Im Holzrahmenbau ist die Zelle zwischen zwei Ständern die natürliche Einheit: Innerhalb der Zelle ist eine Leitung frei, zwischen Zellen kostet sie eine Bohrung. Ein Voxelraster müsste diese Information aus der Geometrie zurückgewinnen und wäre deutlich größer. Der Graph macht jede Regel zu einer Eigenschaft einer Kante oder eines Pfades und jede Kreuzung unmittelbar zu einer Fertigungsbearbeitung. *Beleg.* Recherche 08, 8.2 (Verfahrensvorschlag) [U, eigene Bewertung]; Blokland et al. zur Wahl des Raummodells [@blokland2023literature].

Formal ist *G* = (*V*, *E*) mit acht Knotentypen (GEFACH, ZONE, VORWAND, SCHACHT, DECKENFELD, DACHFELD, UEBERGANG, PORT) und zehn Kantentypen, darunter LAENGS, QUER_STAENDER, QUER_BALKEN, DURCH_LUFTDICHT, DURCH_BRAND und ELEMENTSTOSS; die vollständige Definition steht in `spezifikation/routing-graph.md`. Die Kosten einer Kante *e* für ein Netz des Gewerks *g* sind

$$c_g(e) = w_{L,g}\,L(e) + w_{B,g}\,n_{Bogen}(e) + \sum_{x \in X(e)} w_{x,g} + w_{H,g}\,\max(0, H_{erf} - H_{frei}) + w_{P,g}\,p(e)$$

mit der Länge, der Zahl der 90°-Bögen, einer Strafe je gekreuztem Bauteiltyp, einer Strafe für fehlende Aufbauhöhe in weichen Fällen und einem Präferenzterm, etwa für Vorfertigung im Werk. Alle Gewichte sind nicht negativ. Deshalb ist der mit *w*_L gewichtete Manhattan-Abstand eine zulässige Heuristik für A\*. Die Gewichte sind Platzhalter [U] und werden gegen Werkplanungen des Herstellers kalibriert (Kapitel 20).

Harte Regeln sind **Constraints**, weiche Regeln sind **Kosten**. Die Constraints K1 bis K15 in `routing-graph.md` entfernen Kanten oder Pfade und protokollieren dabei die Regel-ID, damit jede Ablehnung ihre Begründung nennen kann (Kapitel 9.5):

| Constraint | Wirkung | Regel |
|---|---|---|
| K1, K2 Zonen | Elektrokanten in Wand und Decke nur innerhalb der Zonen | `DE.DIN18015-3.Installationszonen-Wand`, `-Decke` |
| K3 Ständer | Bohrung nur bis *p* · *t*, mittig | `M.Firma.Staenderbohrung` |
| K4, K5 Balken | Querbohrung nach NA.6.7; senkrecht nie durch den Balken | `DE.EC5-NA.NA67.Durchbruch` |
| K6 Luftdichtheit | Durchdringung nur mit passender Manschette oder Dose | `DE.DIN4108-7.Luftdichte-Durchdringung` |
| K7 Kollision | Kapazität je Zelle und Mindestabstände | `M.Firma.Routing-Kollisionsfreiheit` |
| K8 Brandschutz | Durchführung nur mit Abschottungssystem (ab GK 3) | `BY.MLAR.Abschottung` |
| K9 Schutzbereiche | Kanten in Bereich 1 nur zu dessen Betriebsmitteln | `DE.VDE0100-701.Schutzbereiche` |
| K10, K11 Gefälle | fallendes *z*, Höhenbudget; *L* ≤ 4 m, ≤ 3 Bögen, Δ*h* ≤ 1 m | `DE.DIN1986-100.Gefaelle`, `-Einzelanschluss-unbelueftet` |
| K12 3 Liter | Wasserinhalt je Fließweg | `DE.DVGW-W551.3-Liter` |
| K13 Lüftung | Biegeradius, Volumenstrom je Strang | `M.Hersteller.Lueftungsstrang` |
| K14 Sperrvolumen | Bedienbereich, R290-Schutzbereich | `DE.VDE-AR-N4100.Zaehlerplatz`, `M.Hersteller.R290-Schutzbereich` |
| K15 Elementstoß | Übergang nur an freigegebenen Kupplungsstellen | `M.Firma.Routing-Kollisionsfreiheit` |

### 13.10.3 Ein Rechenbeispiel: Zone gegen Bohrung

> **Beispiel 13.10 (Rechenbeispiel, mit networkx nachgerechnet).** Eine Innenwand von 5,00 m mit Ständern 60 mm im Raster 625 mm; das Balkenfeld darüber läuft parallel zur Wand. Die Einspeisung kommt im Deckenfeld über der Wandecke an. Die Steckdose sitzt in einer Küche bei *x* = 3,45 m in ZW-m (*z* = 1,15 m). Gewichte (Platzhalter): *w*_L = 1 KE/m, *w*_B = 0,5 KE je Bogen, Ständer- und Rähmbohrung je 0,4 KE.
>
> - **Pfad A, zonenkonform:** 0,20 m im Deckenfeld, Rähmbohrung bei *x* = 0,20 m in die Eckzone ZS-e, 1,35 m senkrecht, dann 3,25 m waagerecht in ZW-m bis zur Dose. Länge 4,80 m, 2 Bögen, 5 Ständerbohrungen, 1 Rähmbohrung: **8,20 KE**.
> - **Pfad B, im Gefach:** 3,45 m im Deckenfeld, Rähmbohrung bei *x* = 3,45 m, 1,35 m senkrecht im Gefach zwischen den Ständern 3,125 und 3,75 m. Länge 4,80 m, 1 Bogen, 0 Ständerbohrungen: **5,70 KE**.
>
> Ohne Zonenregel wählt A\* Pfad B. Mit Zonenregel ist B unzulässig, weil die senkrechte Führung außerhalb einer ZS-Zone liegt, und A\* findet A. Die Zonenregel kostet hier 2,50 KE und fünf Ständerbohrungen bei gleicher Länge. Nur die Leichtbau-Ausnahme mit *ü* ≥ 60 mm (E13.2) lässt B zu. Der Fall steht als Testfall T1 in `routing-graph.md`.

Das Beispiel zeigt einen Zielkonflikt, den die geprüfte Literatur nicht behandelt: Für die Fertigung ist die Führung im Gefach optimal, für die Planungsnorm unzulässig, weil niemand eine senkrechte Leitung über der Dose vermutet. Die Regelmaschine macht den Konflikt sichtbar und bietet an, die Dose in eine Zone zu verschieben, etwa neben die Tür.

### 13.10.4 Algorithmus

Das Verfahren hat drei Ebenen: die Reihenfolge der Netze, die Suche je Netz und die Auflösung von Konflikten.

**E13.4 – Gewerke werden in fester Reihenfolge geroutet; Konflikte werden durch Aufreißen und Neuverlegen gelöst.** *Entscheidung.* Die Reihenfolge ist Abwasser, Lüftung, Trinkwasser kalt und warm, Heizung, Elektro, Daten. Innerhalb eines Gewerks gehen große Nennweiten vor kleinen. Bei einem Konflikt wird das Netz mit dem höheren Rang aufgerissen, seine Konfliktkanten werden verteuert, und beide Netze werden neu verlegt. Abwasser wird nie verdrängt. *Begründung.* Abwasser hat die härtesten Bedingungen (Gefälle, große Nennweite, Fallleitung über Dach), Elektroleitungen sind biegsam und klein. Die Reihenfolge folgt dieser Flexibilität und dem Verfahrensvorschlag aus Recherche 08; Singh und Cheng optimieren die Reihenfolge mehrerer Leitungen eigens [@singh2021automating]. *Beleg.* Recherche 08, 8.2; Recherche 12, Baustein A8 [U, eigene Bewertung].

```text
ROUTE_ALL(G, N):
  for n in sortiere(N, (rang(gewerk), −nennweite, id)):
    P[n] := ROUTE_NET(G, n)
    if P[n] = ∅:
      k := KONFLIKT(G, n)                       # belegte Kanten, die n blockieren
      if k ≠ ∅: RIP_UP_REROUTE(n, k)            # höchstens k_max = 5 Runden [U]
      else: MELDE(n, Regeln der entfernten Kanten, Alternativen A1–A5)
    BELEGE(G, P[n] ⊕ clearance)                 # Kapazität mindern
  PRUEFE_ALLE(P)                                # Regelmaschine, IfcClash, IDS
  return P

ROUTE_NET(G, n):                                # Steiner-Näherung über kürzeste Wege
  T := {quelle(n)};  R := terminals(n) sortiert nach id
  while R ≠ ∅:
    (t, weg) := argmin_{t ∈ R} A*(G_n, t → T, c_g, h)   # G_n: ohne verletzende Kanten;
    if weg = ∅: return ∅                        # Zustand (Knoten, L, n_Bogen, V_Liter, z)
    T := T ∪ knoten(weg);  R := R \ {t}
  return NACHBEARBEITUNG(T)                     # Segmente zusammenfassen, Formteile setzen
```

**Suche.** Ein Netz mit einem Terminal ist ein Kürzeste-Wege-Problem, das A\* mit der zulässigen Heuristik exakt löst. Ein Netz mit mehreren Terminals ist ein Steiner-Baum-Problem: ein Stromkreis mit mehreren Dosen, ein Lüftungsnetz mit mehreren Durchlässen, eine Trinkwasser-Reiheninstallation. Das Verfahren verbindet schrittweise das nächste Terminal mit dem bereits gebauten Baum. Es ist eine Näherung, deren Güte gegenüber der Handplanung in Kapitel 20 zu messen ist. Für kleine Netze mit wenigen Terminals ist eine exakte Aufzählung möglich.

**Ressourcen.** Die Grenzen der unbelüfteten Anschlussleitung und die 3-Liter-Regel hängen am ganzen Pfad. Sie werden als Etiketten im Suchzustand geführt: Ein Zustand ist dominiert, wenn ein anderer im selben Knoten geringere Kosten und nicht mehr Ressourcen verbraucht hat. Das Gefälle wird als monoton fallende Höhe *z* in Fließrichtung geführt; jede Kante prüft ihr Höhenbudget.

**Determinismus.** Bei Gleichstand entscheiden geringere Kosten, dann weniger Kreuzungen, dann die lexikografisch kleinere Folge der Knoten-IDs. Die Knoten-IDs sind uuid5-Werte aus dem Pfad im Modell (Regel 8.8.3). Gleiche Eingabe ergibt deshalb gleiche Leitungen und gleiche GlobalIds (ANF-08-24).

**Nachgelagerte Prüfung.** Der Router erzeugt Leitungen, die nach Konstruktion regelkonform sind (Kapitel 9.6). Trotzdem prüft eine getrennte Schicht das fertige IFC mit Regelmaschine, IfcClash und IDS; eine Abweichung sperrt jede Freigabe (ANF-09-18). Das ist hier besonders wichtig, weil der Router mit Heuristiken arbeitet.

**Bausteine.** networkx (BSD-3) für A\*, IfcOpenShell mit `api.system` und ShapeBuilder (LGPL-3.0+) für IFC, Ports und Formteile, IfcClash für die Kollisionsprüfung und python-fcl oder trimesh für Abfragen während der Suche (Recherche 08) [V]. Bonsai (GPL-3.0) wird nicht gelinkt [U]. Der Router selbst ist neu zu bauen.

### 13.10.5 Ausgabe: vom Pfad zur Bearbeitung

Aus jedem Pfad entstehen drei Ergebnisse:

1. **Leitungen.** Segmente und Formteile mit Ports über `IfcRelNests`, verbunden mit `IfcRelConnectsPorts` und dem System zugeordnet (13.8).
2. **Aussparungsvorschläge.** Je Kreuzung einer Leitung mit einer Bauteilschicht oder einem Stab entsteht ein `IfcVirtualElement` PROVISIONFORVOID mit `Pset_ProvisionForVoid`.
3. **Freigabe und Fertigung.** Nach Prüfung und Freigabe entstehen die Öffnungen, Füllungen, Umhüllungen und Konstruktionsänderungen und daraus die BTLx-Bearbeitungen.

**E13.5 – Der Router erzeugt Aussparungsvorschläge je Bauteilschicht; die Öffnung entsteht erst nach der Holzbauprüfung.** *Entscheidung.* Der Ablauf aus E8.16 gilt unverändert: Vorschlag, Prüfung, Freigabe. Neu ist, dass der Router den Vorschlag nicht je Wand, sondern je gekreuztem Teil erzeugt, also je Ständer, Balken und Platte. Nach Freigabe entstehen je Teil ein `IfcOpeningElement` mit `IfcRelVoidsElement`, eine `IfcRelInterferesElements` zwischen Leitung und Teil und eine Bearbeitung mit der GlobalId der Leitung. Abgelehnte oder verschobene Vorschläge gehen als BCF-Thema zurück (E8.25). *Begründung.* Die Bohrregel hängt am Stab, nicht an der Wand, und die Maschine bearbeitet den Stab oder die Platte. *Beleg.* B15: 4 Vorschläge, 4 Öffnungen, 4 `IfcRelVoidsElement`, 4 `IfcRelInterferesElements`, 1 `IfcRelFillsElement`, 5 BTLx-Bohrungen, 0 Validierungsfehler [V Prototyp].

Damit schließt sich die Lücke L9: Die Kopplung der Durchbrüche aus dem Routing mit den Bohrungen in den Maschinendaten ist nach Recherche 12 bisher nicht publiziert [U]. Kapitel 17 führt die Fertigungsseite aus.

## 13.11 Werkseitige Vorinstallation

Im Holzfertigbau beginnt der Innenausbau im Werk. Nach der Bau- und Leistungsbeschreibung des Praxispartners werden bereits bei der Wandproduktion Dosenbohrungen und Zugdrähte vorbereitet sowie Sanitäranschlüsse, Tragkonstruktionen für Hänge-WCs, Unterputz-Spülkästen und Unterputz-Armaturen eingebaut [@regnauerBLB2024] (Kapitel 3.2.6) [V]. Die Idee der Gewerkeintegration im vorgefertigten Element ist alt [@prochiner2006homes24]. Herstellerunterlagen beschreiben Wandelemente mit Leerrohren und Dosen, rechtwinklige Übergänge zwischen Wand und Decke und Stecksysteme an den Stößen (Recherche 08) [V].

Die Vorinstallation ist vor allem ein Koordinationsproblem: 40 Interviews mit Bauunternehmen und Zulieferern benennen CAD/BIM, Koordination und Risiko als Hürden [@lopez2022mep]. Reviews ordnen Methoden der Modulteilung von TGA-Systemen [@zhao2025mep] und empfehlen BIM über den Lebenszyklus [@kazeem2024integration]; beide stammen aus dem Modulbau und enthalten keine Holzrahmenbau-Regeln. Arbeiten zur Modularisierung vorgefertigter Sanitär- und TGA-Installationen sind nur nach Titel eingeordnet [@suarez2023optimizing; @tserng2011modularization] [U].

Für das Modell folgen daraus drei Vorgaben:

1. **Elementgrenzen sind Graphkanten.** Die Stöße der Wand- und Deckenelemente sind Knoten vom Typ UEBERGANG. Eine Leitung darf eine Elementgrenze nur an einer freigegebenen Kupplungsstelle überqueren (K15), etwa an einem Leerrohrstoß, einem Steckverbinder oder einer Montageöffnung. Der Router teilt die Leitung dort in einen Werks- und einen Baustellenabschnitt. Dieselbe Teilung an Tafelgrenzen verwenden Zhang et al. für die Entwässerung [@zhang2022bimbased].
2. **Jedes Segment trägt einen Ausführungsort.** Das Merkmal `HRB_TGA.Ausfuehrung` ∈ {Werk, Baustelle} steuert Stückliste und Montagereihenfolge. Welche Gewerke Regnauer im Werk vorinstalliert, ist offen (DAT-13-01).
3. **Die Vorinstallation erzwingt einen frühen Freeze.** Dosenlagen, Sanitärobjekte und Montageelemente bestimmen Bohrungen und Ständerlagen. Recherche 10 ordnet Elektro, Sanitär, Smart Home und Heizung dem Freeze vor der Werkplanung zu (Kapitel 3.4.2).

**E13.12 – TGA-Bemusterung und Routing werden vor der Werkplanung eingefroren; danach sind nur noch Änderungen ohne Wirkung auf Bearbeitungen frei.** *Entscheidung.* Das Gate „Werkplanung“ verlangt ein vollständiges Routing aller Gewerke mit freigegebenen Aussparungen. Eine spätere Änderung, die eine Bearbeitung hinzufügt, verschiebt oder entfernt, löst die Änderungskosten nach DAT-08 aus Kapitel 3 aus. *Begründung.* Eine Dose, die nach dem Bohren verschoben wird, ist eine zweite Bohrung und eine beschädigte Platte. *Beleg.* Kapitel 3.2.6 und 3.4.2 [V]; Bau- und Leistungsbeschreibung [@regnauerBLB2024].

## 13.12 Deltas vom Einfamilienhaus bis zum Geschosswohnungsbau

Die TGA-Regeln hängen vom Gebäudetyp ab. Kapitel 9a leitet den Typ aus einem Merkmalsvektor ab und schaltet die Regeln über Schalter (`regelprofile.yaml`). Für die TGA sind fünf Deltas maßgeblich (Recherche 14) [V]:

- **Trinkwasser.** Die Untersuchungspflicht auf Legionellen nach § 31 TrinkwV greift, wenn ein Speicher mit mehr als 400 l oder eine Leitung mit mehr als 3 l ohne Zirkulation vorhanden ist, Duschen vorhanden sind, kein Ein- oder Zweifamilienhaus vorliegt und die Abgabe gewerblich ist; Vermietung gilt als gewerblich. Erste Untersuchung 3 bis 12 Monate nach Inbetriebnahme, dann alle drei Jahre. Dezentrale Wohnungsstationen unter 3 l vermeiden die Pflicht [U, Planungsfolgerung]. Schalter: `trinkwv31`.
- **Heizkosten.** Nach der HeizkostenV wird der Verbrauch je Nutzungseinheit erfasst; neue Geräte sind fernablesbar. Ausgenommen sind Gebäude mit höchstens zwei Wohnungen, von denen der Vermieter eine bewohnt (Schalter `heizkostenv`).
- **Schallschutz.** Ab der zweiten Nutzungseinheit schützt DIN 4109-1 fremde Räume. Dann gelten die Anforderungen an Wasser- und Abwassergeräusche aus fremden Bereichen (*L*_AF,max,n ≤ 30 dB(A), Recherche 08) [V], und die Entkopplung der Fallleitung wird öffentlich-rechtlich.
- **Brandschutz.** Ab Gebäudeklasse 3 und zwischen Nutzungseinheiten greift die MLAR (13.9.4); in Gebäudeklasse 4 sind Abschottungen hochfeuerhemmend auszuführen.
- **Messkonzept und Hausanschluss.** Photovoltaik im Mehrfamilienhaus braucht ein Messkonzept je Gebäude; ein Hausanschlussraum wird ab mehr als fünf Nutzungseinheiten verlangt [U].

Der Router wird im Mehrfamilienhaus nicht komplizierter, aber strenger: Kanten DURCH_BRAND zwischen Nutzungseinheiten werden teuer oder gesperrt.

## 13.13 Zwischenfazit

Das Kapitel beantwortet den TGA-Teil von FF6 in fünf Punkten:

1. **Die Regeln existieren und sind rechenbar.** Die 42 Regeln stammen fast vollständig aus Gesetz, Norm und Herstellerangabe. Nur die Firmenregeln (Ständerbohrung, Öffnungsmaß, Verschub, Fräsgrenze, Routing-Gewichte) sind Platzhalter mit Status [U].
2. **Die Wand ist die Rechenebene.** Das Graphmodell über konstruktiven Zellen macht jede Kreuzung zu einer prüfbaren Bohrung und jede Bohrung zu einer Bearbeitung.
3. **Norm und Fertigung stehen im Konflikt.** Die Zonen erzwingen fünf Bohrungen, wo die Fertigung keine bräuchte (Beispiel 13.10), und das gemeinsame Raster erzeugt Kollisionen systematisch (Beispiel 13.8). Eine Entwurfsregel löst beides früher und billiger als die Werkplanung.
4. **Die Wärmepumpe ist ein Standortproblem.** Neben der unzulässigen Installateurwahl liegt ein Punkt mit kürzester Leitung und irrelevanter Zusatzbelastung.
5. **Licht ist Empfehlung.** Hart sind nur Anschlüsse, Pflicht sind Leuchtendaten; die melanopische Wirkung bleibt R5.

Offen sind vor allem die Firmenwerte (DAT-13-01 bis DAT-13-03), die Kalibrierung der Routing-Gewichte, die Validierung von BTLx gegen das XSD und ein lauffähiger Router als Beispiel B8.

## 13.14 Umsetzungsvorgaben für die App

Es gelten die Regeln aus Kapitel 3.7: „Muss“ heißt, dass ohne die Anforderung ein Rechts-, Nachweis- oder Fertigungsfehler entstehen kann; „Soll“ heißt, dass sie Qualität oder Nutzen erhöht. Referenzwerte sind die gemessenen Werte der Beispiele B14, B15 und B20 sowie die Testfälle in `tga-dimensionierung.yaml` und `routing-graph.md`.

**E13.10 – TGA-Dimensionierung in der App ist Vorbemessung; die Ausführungsplanung gibt ein Fachplaner frei.** *Entscheidung.* Die Rechnungen aus 13.2 bis 13.5 laufen in Reifegrad R und liefern Nennweiten, Kreise und Volumenströme. Vor dem Gate „Werkplanung“ bestätigt ein TGA-Fachplaner Heizlast, Druckverlust und Abgleich (R3, `IfcApproval`, Kapitel 18). *Begründung.* Druckverlustnachweis, Heizlast und hydraulischer Abgleich brauchen Daten und Verfahren, die hier nur teilweise geprüft sind [U]. *Beleg.* 13.2, 13.5.

### 13.14.1 Maschinenlesbare Spezifikation

| Datei | Inhalt |
|---|---|
| `spezifikation/regelkatalog-13-tga.yaml` | 42 Regeln im Schema `regel.schema.json` (R1: 34, R2: 4, R3: 1, R4: 3); ergänzt `regelkatalog.yaml`, dessen fünf TGA-Regeln (NA.6.7, Ständerbohrung, TA Lärm, R290, Irrelevanzziel) nur referenziert werden |
| `spezifikation/tga-dimensionierung.yaml` | 20 Formeln mit Variablen, Einheiten, Normverweis, Status und 33 Testfällen; Kennwerttabellen für Nennweiten, Anschlusswerte, Manschetten, Zonen, Schutzbereiche, Stromkreise, Zählerplatz und WP-Aufstellung |
| `spezifikation/routing-graph.md` | formale Definition von Knoten, Kanten, Kosten, Constraints K1–K15, Algorithmus, Ausgabe, Austauschformat und fünf Testfällen T1–T5 in acht YAML-Blöcken |

**Neue Profile.** Der Katalog verwendet vier Profile, die in `regelprofile.yaml` noch nicht registriert sind: `DE-aRdT-TGA` (*S*₃), `EU-FGas-2024` (*S*₁), `EU-GIA-2024` (*S*₁) und `DE-TrinkwV` (*S*₁). Ihre Registrierung ist Voraussetzung für den Konsistenzabgleich nach Kapitel 9.9.1 und gehört in die Pflege dieser gemeinsamen Datei. Alle übrigen Profile sind registriert, und die Schicht jeder Regel stimmt mit der ihres Profils überein.

### 13.14.2 Anforderungen

**Regeldaten und Elektro**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-13-01 | Muss | Die TGA-Regeln werden aus `regelkatalog-13-tga.yaml` geladen, gegen `regel.schema.json` validiert und zusammen mit `regelkatalog.yaml` ausgewertet; die vier neuen Profile sind registriert. | 13.14.1, E13.1 | Laden ergibt 42 Regeln und 0 Schemafehler; jede Regel-ID ist über beide Kataloge eindeutig; eine Regel mit einem nicht registrierten Testprofil `DE-X` wird mit „Profil nicht registriert“ abgewiesen. |
| ANF-13-02 | Muss | Installationszonen werden je Wand- und Deckenfläche aus Decke, Fußboden, Öffnungen und Ecken erzeugt; Elektrokanten außerhalb der Zonen sind gesperrt. | 13.1.1, E13.2 | Testfall T1: ohne Ausnahme Pfad A mit 4,80 m, 2 Bögen, 5 Ständerbohrungen, 8,20 KE; Pfad B wird mit Regel-ID `DE.DIN18015-3.Installationszonen-Wand` abgelehnt. |
| ANF-13-03 | Muss | Die Leichtbau-Ausnahme wird aus dem Schichtmodell berechnet; gedämmte Gefache gelten nur als unverfüllt, wenn die verantwortliche Person den Auslegungsparameter setzt. | 13.1.1, E13.2 | Überdeckung 40 + 15 mm = 55 mm: Zonen gelten. 40 + 25 mm = 65 mm: T1 liefert Pfad B mit 5,70 KE. Parameter nicht gesetzt: Voreinstellung `false`, im Nachweis protokolliert. |
| ANF-13-04 | Muss | Bad-Schutzbereiche sind Sperrvolumen um Wanne und Dusche. | 13.1.2 | Bodengleiche Dusche: Steckdose 1,00 m vom Ablauf auf 1,05 m Höhe → `verletzt` (Bereich 1, *r* = 1,20 m); 1,50 m Abstand als Rasiersteckdose → `erfuellt` (Bereich 2 bis 1,80 m); Standardsteckdose bei 1,50 m → `verletzt`; bei 1,90 m → `erfuellt`. |
| ANF-13-05 | Muss | Die Zahl der Stromkreise folgt der Wohnfläche; eine vereinbarte RAL-Stufe erhöht, senkt aber nie. | 13.1.2 | Wohnfläche 140 m²: `n_min` = 7; 6 Stromkreise → `verletzt`; 48 m² → 3. |
| ANF-13-06 | Muss | Vor dem Zählerschrank ist ein Bedienbereich 1,2 m × 2,0 m als `IfcSpatialZone` RESERVATION gesperrt; Leerrohr HÜP–APZ ≥ 25 mm. | 13.1.3 | Schrank mit Möbel 0,9 m davor → `verletzt`, Meldung nennt 0,9 < 1,2 m; Leerrohr M20 → `verletzt`; M25 → `erfuellt`. |
| ANF-13-07 | Muss | Für Bauanträge ab 12.02.2026 enthält das Modell ein Glasfaser-Teilsystem bis zum Netzabschlusspunkt. | 13.1.3 | Bauantrag 2026-03-01 ohne `OPTICALCABLESEGMENT`: `verletzt`; Bauantrag 2026-01-15: `nicht_anwendbar`; mit Teilsystem: `erfuellt`. |
| ANF-13-08 | Muss | Schlafräume und Räume mit brennbaren Bauteilen unter „feuerhemmend“ erhalten ein Protokoll zur AFDD-Bewertung. | 13.1.2 | Schlafraum ohne Protokoll: `freigabepflichtig`, Rolle „Elektrofachkraft“; nach Bestätigung `erfuellt` mit Name und Datum. |
| ANF-13-09 | Muss | Jede Öffnung in einer luftdichten Schicht hat eine Manschette im Durchmesserbereich oder eine luftdichte Dose. | 13.1.3, 13.9.4 | B15 D3 (*d*_a 110 mm): Manschette 100–120 mm gewählt, `IfcRelFillsElement` vorhanden; *d*_a 140 mm ohne System: `unbestimmt`, Hinweis DAT-13-05. |

**Wasser, Abwasser, Lüftung, Heizung**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-13-10 | Muss | Trinkwasserleitungen werden über Spitzendurchfluss und Geschwindigkeitsgrenze vorbemessen. | 13.2, Beispiel 13.2 | ΣV̇_R = 2,0 l/s → V̇_S = 0,748 ± 0,001 l/s; *d*_i,min = 21,8 mm; Auswahl 32 × 3 mit 1,41 m/s; 26 × 3 → `verletzt` (2,38 m/s). |
| ANF-13-11 | Muss | Jeder Warmwasser-Fließweg ohne Zirkulation enthält höchstens 3 l; die Prüfung läuft als Pfadressource im Router. | 13.2 | T5: 20 × 2, 15,5 m → 3,12 l, `verletzt`, Alternativen „Zirkulation“ und „Speicher näher“; B14 Küche 16 × 2 mit 1,2 l → `erfuellt`. |
| ANF-13-12 | Muss | Speicher und Zirkulation tragen Solltemperaturen (≥ 60 °C, Rücklauf ≥ 55 °C). | 13.2 | Speicher mit 55 °C → `verletzt`; 60 °C mit Rücklauf 55 °C → `erfuellt`. |
| ANF-13-13 | Muss | Der Schmutzwasserabfluss wird als max(0,5 · √ΣDU; max DU) berechnet. | 13.3, Beispiel 13.3 | Bad (2,0; 0,6; 0,5) → 2,0 l/s; Leitung (0,8; 0,8; 0,8; 0,6; 0,5) → 0,935 ± 0,001 l/s. |
| ANF-13-14 | Muss | Gefälle und die Grenzen unbelüfteter Anschlussleitungen werden im Router als Pfadressourcen geführt. | 13.3, K10/K11 | Anschlussleitung 4,2 m → `verletzt`, Alternative „belüften“; 4 Umlenkungen → `verletzt`; DN 50, 2,45 m, 1 % → Höhenbedarf 74,5 mm. |
| ANF-13-15 | Muss | Jede Fallleitung ist über Dach entlüftet; die Mündung hält den Fensterabstand ein. | 13.3, Beispiel 13.4 | B15 D3: `verletzt`, Alternativen „+700 mm“ und „fehlen 400 mm“; Fallleitung ohne `IfcStackTerminal` → `verletzt`. |
| ANF-13-16 | Muss | Die Lüftung wird nach DIN 1946-6 bemessen; Abluft endet im Freien. | 13.4, Beispiel 13.5 | 140 m²: 92,96 / 132,8 / 172,64 m³/h (± 0,05); Σ Abluft 60 → Auslegung 132,8; Fortluft in eine Abgasanlage → `verletzt` (BayBO Art. 39 Abs. 4). Validierungsfälle aus Beiblatt 1 bestehen, sobald DAT-13-06 vorliegt. |
| ANF-13-17 | Soll | Das Kanalnetz wird mit Strangzahlen und Biegeradien nach Herstellersystem erzeugt. | 13.4 | Raum 60 m³/h mit Flexrohr da 75 → 3 Stränge; Biegeradius < 1 × D → Kante gesperrt. |
| ANF-13-18 | Muss | Jeder beheizte Raum hat eine Norm-Heizlast; die FBH hält Oberflächentemperatur, Belagwiderstand und Kreislänge ein. | 13.5, Beispiel 13.6 | Raum ohne Heizlast → `verletzt` (R2); 20 m², VA 15 cm → 133,3 m, 2 Kreise; Teppich R_λ,B = 0,233 → weiche Meldung; Bad *θ*_F,max = 33 °C. |

**Wärmepumpe und Licht**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-13-19 | Muss | Die WP-Aufstellung berechnet die zulässige Menge, die Pareto-Front aus Reserve und Leitungslänge und wählt voreingestellt die kürzeste Leitung mit Reserve ≥ 6 dB. | 13.6.3, E13.6 | B20-Daten: 834 zulässige Punkte, Pareto-Front 21 Punkte; Voreinstellung (15,75 m; 12,25 m) mit 4,3 m und 6,98 dB; ε = 10 dB → (11,75 m; 6,75 m); Modus „max. Reserve“ → (7,25 m; 1,75 m), 12,9 dB (ANF-09-28). |
| ANF-13-20 | Muss | Spitzenpegel werden je Immissionsort geprüft. | 13.6.1 | B20 Optimum, Schlafzimmer OG: *L*_AFmax = 30,4 dB(A) ≤ 60 dB(A) → `erfuellt`. |
| ANF-13-21 | Muss | F-Gase werden gegen den Liefertermin geprüft; Split-Kältemittelleitungen gegen Herstellergrenzen. | 13.6.2, E13.7 | Split R32, 7 kW, Lieferung 2027-01-15 → `verletzt`; Lieferung 2026-12-01 → `erfuellt` mit Warnung; Monoblock R290 → `erfuellt`; Kältemittelleitung 16 m bei Grenze 15 m → `verletzt`. |
| ANF-13-22 | Soll | Eine Wandkonsole an einer Holzrahmenwand eines Aufenthaltsraums erzeugt eine Warnung mit Alternative. | 13.6.2 | Konsole an Wohnzimmer-Außenwand → Warnung „Bodenkonsole empfohlen“; an Garagenwand → keine Meldung. |
| ANF-13-23 | Muss | Jeder Raum hat Beleuchtungsauslässe nach DIN 18015-2; gelieferte Leuchten tragen ab Reifegrad A photometrische Daten, GLDF wird gegen das XSD geprüft. | 13.7, E13.8 | Raum ohne Auslass → `verletzt`; Leuchte ohne `IfcLightSourceGoniometric` in Reifegrad A → IDS-Befund `HRB-TGA-Leuchte`; GLDF mit fehlendem Pflichtelement → `verletzt` mit XSD-Meldung. |
| ANF-13-24 | Soll | Licht-Empfehlungen R5-LICHT-05 bis -07 erscheinen mit Evidenzgrad und blockieren nie. | 13.7, Tabelle 13.1 | Schlafzimmer mit nicht dimmbarer Leuchte: Empfehlung R5-LICHT-05 mit „B“; Ablehnung ohne Begründung möglich; Gate unverändert. |

**IFC, Durchdringungen, Routing, Vorinstallation**

| ID | M/S | Beschreibung | Beleg | Abnahmekriterium (Testfall) |
|---|---|---|---|---|
| ANF-13-25 | Muss | TGA wird nach Tabelle 13.2 geschrieben; jedes Endgerät ist über Ports mit der Quelle seines Systems verbunden. | 13.8 | `validate` mit EXPRESS-Regeln: 0 Meldungen; Anzahl deprecated Klassen = 0; für jedes `IfcFlowTerminal` findet `get_connected_to`/`get_connected_from` einen Pfad zur Quelle; B15: Abzweig JUNCTION mit 3 Nachbarn und 3 `IfcRelConnectsPorts` (Test `test_ifc_rohr_merkmale_und_topologie`). |
| ANF-13-26 | Muss | Öffnungsmaße folgen aus Rohr, Entkopplung und Ringspalt; Vorschlag, Prüfung und Öffnung laufen nach E8.16 und E13.5 je gekreuztem Teil. | 13.9.3, E13.5 | *d*_a 110 → Ø 150 mm, luftdicht Ø 130 mm; B15: 4 PROVISIONFORVOID, 4 Öffnungen, 4 Voids, 4 Interferes, 1 Fills (ANF-08-21). |
| ANF-13-27 | Muss | Dämmdicken werden nach dem Routing je Segment und Lage nach GModG Anlage 8 bestimmt. | 13.9.2 | *d*_i 26 frei → 30 mm, im Durchbruch → 15 mm; Heizung *d*_i 20 im Fußboden zwischen Nutzern → 6 mm; Stichleitung 1,2 l → ausgenommen (B14). |
| ANF-13-28 | Muss | Abschottungen werden ab GK 3 zwischen Nutzungseinheiten verlangt und sind ohne Nachweis für die eigene Decke freigabepflichtig. | 13.9.4 | B15 (GK 1): keine Abschottung, Begründung MLAR 4.1.1; gleiche Durchdringung in GK 4 zwischen zwei Wohnungen: `freigabepflichtig`, Rolle „Brandschutzplaner“. |
| ANF-13-29 | Muss | Der Routing-Graph wird nach `routing-graph.md` aus dem Schichtmodell erzeugt; das Routing ist deterministisch. | 13.10.2, E13.3 | T4: zwei Läufe mit `PYTHONHASHSEED` 1 und 4711 ergeben identische Pfade und GlobalIds; jeder Knoten hat einen Typ aus den acht Knotentypen. |
| ANF-13-30 | Muss | Netze werden in der Reihenfolge nach E13.4 geroutet; Konflikte werden durch Aufreißen und Neuverlegen gelöst; das Ergebnis ist kollisionsfrei. | 13.10.4, E13.4 | Zwei sich kreuzende Netze (Abwasser, Elektro) in derselben Zelle: Elektro wird verlegt, Abwasser bleibt; IfcClash mit Clearance meldet 0 Konflikte; nach 5 erfolglosen Runden Meldung mit Konfliktkanten. |
| ANF-13-31 | Muss | Jede freigegebene Kreuzung wird eine BTLx-Bearbeitung mit `LeitungGUID` und `IfcGlobalId`. | 13.9.5, 13.10.5 | B15: 5 `Drilling` (D1, D2 Süd/Nord, D3, BD-2), jede mit der GlobalId der Fallleitung; `f.by_guid()` findet die Leitung. |
| ANF-13-32 | Muss | Fallleitungen und WC-Achsen werden beim Platzieren auf Gefachmitte geprüft; sonst Verschiebung oder Wechsel. | 13.9.3, E13.9 | B15: Verschub 120 mm > 100 mm → Wechsel und Ständerauswechslung als IFC-Bauteile; mit Grenze 150 mm → Verschiebung ohne Wechsel. |
| ANF-13-33 | Soll | Bohrungen ab der Fräsgrenze werden als Fräsung übergeben. | 13.9.5 | Grenze 70 mm: Ø 150 → Fräsung, Ø 31 → Bohrung; Grenze fehlt: Platzhalter 70 mm mit Status U im Protokoll. |
| ANF-13-34 | Muss | Elementgrenzen sind nur an Kupplungsstellen passierbar; jedes Segment trägt den Ausführungsort; TGA-Änderungen nach dem Freeze mit Wirkung auf Bearbeitungen lösen Änderungskosten aus. | 13.11, E13.12 | Leerrohr über einen Wandstoß ohne Kupplung → Kante gesperrt; mit Kupplung → zwei Segmente (Werk, Baustelle); Dose nach Freeze um 0,3 m verschoben → Änderungsmeldung mit Kosten nach DAT-08. |
| ANF-13-35 | Muss | TGA-Deltas werden über die Schalter `trinkwv31`, `heizkostenv` und die Gebäudeklasse aktiviert. | 13.12 | EFH → MFH mit 4 vermieteten WE, Speicher 500 l: `DE.TrinkwV.31.Legionellen` aktiv, Hinweis Probenahmestellen; EFH: `nicht_anwendbar`. |
| ANF-13-36 | Muss | Heizlast, Druckverlust und hydraulischer Abgleich sind vor dem Gate „Werkplanung“ durch einen Fachplaner freigegeben. | E13.10 | Gate „Werkplanung“ ohne `IfcApproval` der Rolle TGA-Fachplaner: gesperrt; mit Freigabe: frei, Nachweis nennt Werkzeug und Version. |

### 13.14.3 Datenstrukturen und Parameter

| Feld | Typ | Einheit | Wertebereich | Quelle |
|---|---|---|---|---|
| `netz.id`, `netz.gewerk` | string, enum | – | abwasser, lueftung, trinkwasser_kalt, trinkwasser_warm, heizung, elektro, daten | routing-graph.md 2, E13.4 |
| `netz.quelle`, `netz.terminals` | ref Port-GUID, list | – | ≥ 1 Terminal | 13.10.4 |
| `netz.d_a_mm`, `netz.d_i_mm` | float | mm | 6–200 | tga-dimensionierung.yaml#nennweiten |
| `knoten.typ` | enum | – | GEFACH, ZONE, VORWAND, SCHACHT, DECKENFELD, DACHFELD, UEBERGANG, PORT | routing-graph.md 3 |
| `kante.typ`, `kante.kreuzt`, `kante.laenge_m`, `kante.boegen_90` | enum, list, float, int | –, –, m, – | zehn Kantentypen; GUIDs; ≥ 0; 0–4 | routing-graph.md 4 |
| `gewichte.<gewerk>.<term>` | float | KE bzw. KE/m | ≥ 0 | routing-graph.md 5 (Platzhalter U) |
| `zone.id`, `zone.rechteck` | enum, float[4] | –, mm | ZW-o, ZW-u, ZW-m, ZS-t, ZS-f, ZS-e, ZD-r, ZD-t | 13.1.1 |
| `schicht.ueberdeckung_mm` | float | mm | 0–200; Ausnahme ab 60 | E13.2 |
| `auslegung.gedaemmtes_gefach_unverfuellt` | bool | – | Voreinstellung false | E13.2 |
| `kreuzung.d_oeffnung_mm`, `kreuzung.art` | int, enum | mm | Raster 10; Querschnittsschwaechung, Durchbruch, Bohrung, Fraesung | 13.9.3, `DD.Oeffnungsmass` |
| `kreuzung.status` | enum | – | vorschlag, angenommen, verschoben, abgelehnt | E8.16, E13.5 |
| `kreuzung.fuellung` | enum | – | keine, Luftdichtheitsmanschette, Brandschutzmanschette, Dose_luftdicht | 13.9.4 |
| `segment.lage_gmodg` | enum | – | frei, durchbruch, fussboden_ein_nutzer, fussboden_verschiedene_nutzer, aussenluft | 13.9.2 |
| `segment.daemmung_mm`, `segment.gradient` | float | mm, – | 0–100; 0–0,1 | GModG Anl. 8; DIN 1986-100 |
| `HRB_TGA.Ausfuehrung` | enum | – | Werk, Baustelle | 13.11 |
| `tw.sum_V_R_ls`, `tw.V_S_ls` | float | l/s | 0,2–500 | DIN 1988-300 |
| `tw.V_weg_l` | float | l | 0–3 ohne Zirkulation | DVGW W 551 |
| `aw.DU_ls`, `aw.Q_ww_ls` | float | l/s | 0,5–2,5 je Gegenstand | DIN 1986-100 |
| `lu.A_NE_m2`, `lu.q_v_m3h`, `lu.f` | float | m², m³/h, – | ≥ 20; f ∈ {0,3; 0,7; 1,0; 1,3} | DIN 1946-6 |
| `hz.phi_HL_W`, `hz.theta_int_C` | float | W, °C | > 0; 20 bzw. 24 | DIN EN 12831-1 |
| `hz.VA_cm`, `hz.L_kreis_m` | int, float | cm, m | 5–30; ≤ 100 | Herstellerregel (U) |
| `wp.xy`, `wp.reserve_dB`, `wp.leitung_m` | float[2], float, float | m, dB, m | Raster 0,5 m | B20 |
| `wp.eps_reserve_dB` | float | dB | Voreinstellung 6 | E13.6 |
| `wp.kaeltemittel`, `wp.gwp`, `wp.liefertermin` | string, int, date | –, –, – | R290, R32; GWP aus Datenblatt | VO (EU) 2024/573 |
| `leuchte.gldf`, `leuchte.mDER` | URI, float | –, – | XSD-gültig; > 0 | 13.7, DAT-13-09 |

### 13.14.4 Datenlieferungen von Regnauer

| ID | Inhalt | gewünschtes Format | Ersatz bis zur Lieferung | blockiert |
|---|---|---|---|---|
| DAT-13-01 | Umfang der Vorinstallation im Werk je Gewerk; Kupplungsstellen an Element- und Wandstößen (Steckverbinder, Leerrohrstöße) | Tabelle Gewerk × Werk/Baustelle, Systemdatenblatt | Elektro-Leerrohre und Dosen im Werk, Rest Baustelle [U] | ANF-13-34 |
| DAT-13-02 | Installationsebene in Außen- und Innenwand, luftdichte Ebene, Standard-Dosentypen | Schichtaufbau als JSON (vgl. DAT-01) | Innenwand 40 mm, Außenwand ohne; Dose luftdicht | ANF-13-03, -09 |
| DAT-13-03 | Bohrregeln für Ständer, Schwelle, Rähm und Balken, zulässiger Verschub, KVH oder BSH | Tabelle mit Grenzwerten und Quelle | 25 % der Ständertiefe, Verschub 100 mm (B15) | ANF-13-32; K3 |
| DAT-13-04 | Sanitärobjekte und Armaturen mit Berechnungsdurchfluss, Anschlusswert, Anschlusshöhen; Vorwandsystem | Katalog mit Artikel und Kennwerten | Herstellerwerte aus Recherche 16 | ANF-13-10, -13 |
| DAT-13-05 | freigegebene Manschetten und Abschottungssysteme mit Durchmesserbereich und Nachweis (auch Holzbalkendecke GK 4) | Liste mit abZ/aBG-Nummer | vier Systeme aus Recherche 16; MFH gesperrt | ANF-13-09, -28 |
| DAT-13-06 | Lüftungsstandard: Gerät, Kanalsystem, Verlegung (Decke oder Estrich), Raumabluftwerte, Schalldaten | Datenblatt, Tabelle | Flexrohr da 75; Bad 40, WC 20 m³/h [U] | ANF-13-16, -17 |
| DAT-13-07 | Heizungsstandard: WP innen/außen, Monoblock/Split, FBH-System und VA, Heizlast-Software, Zuständigkeit für Abgleich | Tabelle | Monoblock R290 außen, Tacker nass, VA 15 cm [U] | ANF-13-18, -36 |
| DAT-13-08 | WP-Herstellerdaten: *L*_WA Tag/Nacht/max, Oktavspektrum, Tonhaltigkeit, Schutzbereichsmaße, Leitungsgrenzen | Datenblatt je Gerät | B20-Beispielgerät, *K*_T = 3 dB | ANF-13-19 bis -21 |
| DAT-13-09 | Leuchtenprogramm: Hersteller, GLDF oder EULUMDAT, Spektrum bzw. mDER; firmeneigene Planungswerte | GLDF-Container | nur Auslässe nach DIN 18015-2 | ANF-13-23, -24 |
| DAT-13-10 | Elektro-Standard: RAL-RG-678-Stufe, KNX oder Funk, Zählerschrank mit Plätzen für WP, PV, Wallbox; Netzbetreiber-TAB | Tabelle, TAB-Dokument | Stufe 1 (DIN 18015-2) | ANF-13-05, -06 |
| DAT-13-11 | CAD/CAM-Kette für Bohrungen und Fräsungen, Fräsgrenze, GUID-Feld in WUP (ergänzt DAT-04 aus Kapitel 3) | Spezifikation, Beispieldateien | BTLx mit UserAttribute, Fräsgrenze 70 mm | ANF-13-31, -33 |
| DAT-13-12 | Zuständigkeit für TGA-Fachplanung und Glasfaser (Werk, Baustelle, Netzbetreiber), Lage von HÜP und APZ, genutzte TGA-Software | Beschreibung, IFC-Beispiel | App plant, Fachplaner gibt frei | ANF-13-07, -36 |

### 13.14.5 Prüfung der Spezifikationsdateien

Am 27.09.2026 mit Python 3.11, PyYAML und jsonschema 4 geprüft:

- `regelkatalog-13-tga.yaml`: parsebar; 42 Regeln, 0 Schemafehler (Draft 2020-12); keine doppelte ID und keine Kollision mit `regelkatalog.yaml`; alle acht `bib`-Schlüssel und der Schalter `trinkwv31` existieren; die Schicht jeder Regel mit registriertem Profil stimmt.
- `tga-dimensionierung.yaml`: parsebar; 20 Formeln; alle 33 Testfälle nachgerechnet und bestanden; jede Formel verweist auf eine vorhandene Regel oder auf R5-LICHT-05.
- `routing-graph.md`: acht YAML-Blöcke parsebar; T1 mit networkx 3.6.1 nachgerechnet (8,20 bzw. 5,70 KE).

## Verwendete Schlüssel

Das Kapitel enthält 59 Zitatstellen zu 42 Schlüsseln aus `literatur/lit-*.bib`; zugeordnet ist jeweils die erste Datei, in der ein Schlüssel steht.

**lit-A-acc-bim.bib** (2): `iso2024ifc`, `solihin2015classification`

**lit-B-vorfertigung-ki.bib** (1): `compastimber`

**lit-C-recht-normen.bib** (9): `baybo2026`, `baytb2025`, `btlx23`, `din1946-6`, `din5034-1`, `en1995-2026`, `gmodg2026`, `holzbaurl2024`, `regnauerBLB2024`

**lit-E-vergleich-automation.bib** (6): `baradaran2022parametric`, `blokland2023literature`, `choi2022modification`, `korman2003knowledge`, `medjdoub2018parametric`, `singh2021automating`

**lit-F-architekturpsychologie.bib** (2): `brown2022recommendations`, `din2019tageslicht`

**lit-G-luecken.bib** (1): `prochiner2006homes24`

**lit-I-schneeball-b.bib** (7): `brown2020melanopic`, `cain2020evening`, `cajochen2022evening`, `lopez2022mep`, `spitschan2021luox`, `trinh2023medi`, `zhao2025mep`

**lit-J-schneeball-runde2.bib** (11): `cie2018s026`, `gkaintatzimasouti2022simulations`, `harvieclark2019assessing`, `houser2020humancentric`, `houser2021humancentric`, `kazeem2024integration`, `pestana2024optimizing`, `suarez2023optimizing`, `ticleanu2021impacts`, `tserng2011modularization`, `zhang2022bimbased`

**lit-L-schneeball-runde3.bib** (2): `huang2026bimintegrated`, `wang2016building`

**lit-M-nachweis.bib** (1): `din1333`

Die `bib`-Felder in `spezifikation/regelkatalog-13-tga.yaml` (acht Schlüssel) sind mit demselben Abgleich geprüft; es fehlt keiner.

### Python-Key-Check

```python
import re, glob, pathlib
text = pathlib.Path("13-tga-routing.md").read_text(encoding="utf-8")
body = text.split("## Verwendete Schlüssel")[0]
cited = {k.strip().lstrip("@") for grp in re.findall(r"\[(@[^\]]+)\]", body) for k in grp.split(";")}
bib = set()
for f in glob.glob("literatur/lit-*.bib"):
    bib |= set(re.findall(r"^@\w+\{([^,\s]+),", open(f, encoding="utf-8").read(), re.M))
print(len(cited), "zitiert;", "fehlend:", sorted(cited - bib) or "keine")
```

Ergebnis (27.09.2026, aus `arbeit/` ausgeführt): `42 zitiert; fehlend: keine` – 0 fehlend.

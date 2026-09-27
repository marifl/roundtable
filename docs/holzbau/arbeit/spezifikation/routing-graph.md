# Routing-Graph: formale Definition (Spezifikation zu Kapitel 13.10)

Stand: 27.09.2026, Version 0.1.0. Status: Entwurf; Gewichte und Firmenwerte sind Platzhalter [U] bis zur Datenlieferung (DAT-13-01 bis DAT-13-03, DAT-13-11). Die YAML-Blöcke dieser Datei sind maschinenlesbar und werden mit Python geparst (Kapitel 13.14.4). Regel-IDs verweisen auf `regelkatalog-13-tga.yaml` und `regelkatalog.yaml`, Formeln auf `tga-dimensionierung.yaml`.

## 1 Zweck und Geltung

Der Routing-Graph ist das Suchmodell, in dem die App Leitungen aller Gewerke vom Endgerät zur Quelle führt. Er ist kein Voxelraster, sondern ein Graph über den **konstruktiven Zellen** des Holzrahmenbaus (E13.3): Gefache, Installationszonen, Vorwände, Schächte, Decken- und Dachfelder. Jede Kante trägt die Bauteile, die sie durchdringt. Deshalb lässt sich aus jedem Pfad unmittelbar ableiten, welche Bohrung, welcher Durchbruch, welche Manschette und welche Abschottung nötig ist.

Geltung: alle Gewerke nach Kapitel 13.1 bis 13.6 im Gebäude, vom Hausanschluss bzw. von der Fallleitung bis zum Endgerät. Grundleitungen außerhalb der Bodenplatte routet Kapitel 14a.

## 2 Grundmengen

- *B*: Menge der Bauteilschichten mit GlobalId, Material, Dicke, Rolle (`beplankung`, `gefach`, `folie`, `daemmung_aussen`, `installationsebene`, `putz`, Kapitel 3) und den Flags `luftdicht`, `feuerwiderstand`, `tragend`.
- *S*: Menge der Stäbe (Ständer, Schwelle, Rähm, Riegel, Balken, Sparren) mit Querschnitt *b* × *h* und Achse.
- *Z*: Menge der Installationszonen nach DIN 18015-3 je Wandfläche und Deckenfläche (`installationszonen_DIN18015-3` in `tga-dimensionierung.yaml`).
- *V*: Menge der Sperrvolumen: Schutzbereiche 0/1/2 nach VDE 0100-701, R290-Schutzbereich, Bedienbereich vor dem Zählerschrank, Bewegungsflächen, Fenster- und Türöffnungen.
- *N*: Menge der Netze. Ein Netz *n* = (Gewerk *g*, System, Quelle *q*, Terminals *T*, Nennweite *d*, Ressourcen). Terminals sind Ports (`IfcDistributionPort`) von Endgeräten.

## 3 Knoten

Ein Knoten ist eine konvexe Zelle, in der eine Leitung ohne weitere Durchdringung geführt werden kann, oder ein Port.

```yaml
knotentypen:
  GEFACH:        {zelle: "Raum zwischen zwei Ständern i, i+1 einer Wandtafel, je Schicht (Kern, Installationsebene)", attribute: [wand_guid, schicht, x_von, x_bis, z_von, z_bis, frei_querschnitt_mm2, gedaemmt]}
  ZONE:          {zelle: "Schnitt Gefach × Installationszone (ZW-o, ZW-u, ZW-m, ZS-t, ZS-f, ZS-e)", attribute: [zone_id, richtung_erlaubt]}
  VORWAND:       {zelle: "Installationsvorwand oder Vorsatzschale", attribute: [tiefe_mm, system, zugaenglich]}
  SCHACHT:       {zelle: "senkrechter Schacht bzw. Trasse über Geschosse", attribute: [querschnitt_mm, feuerwiderstand]}
  DECKENFELD:    {zelle: "Raum zwischen zwei Balken, je Lage (Fussbodenaufbau, Balkenlage, Unterdecke)", attribute: [decke_guid, lage, hoehe_frei_mm, richtung_balken]}
  DACHFELD:      {zelle: "Raum zwischen zwei Sparren", attribute: [dach_guid, luftdicht_ebene]}
  UEBERGANG:     {zelle: "Wand/Decke, Wand/Wand oder Elementstoß (Kopplungsstelle der Vorfertigung)", attribute: [element_a, element_b, kupplung]}
  PORT:          {zelle: "Anschlusspunkt eines Endgeräts, Verteilers, Speichers oder einer Fallleitung", attribute: [port_guid, flow_direction, system_type, nenndurchmesser]}
knotenregeln:
  - "Zellen werden aus dem Schichtmodell erzeugt; eine Zelle wird geteilt, wo eine Zonengrenze, ein Riegel oder ein Sperrvolumen sie schneidet."
  - "Knotenkoordinate ist der Schwerpunkt der Zelle; die Zelle behält ihre Box für Kapazität und Kollision."
  - "Knoten-ID = uuid5(Namensraum, Pfad), Pfad aus Element-GUID, Schicht und Index (Regel 8.8.3); daraus folgt eine deterministische Reihenfolge."
```

## 4 Kanten

Eine Kante *e* = (*u*, *v*, Typ, Geometrie) verbindet benachbarte Zellen. Sie trägt die Menge *X*(*e*) der gekreuzten Stäbe und Schichten.

```yaml
kantentypen:
  LAENGS:            {bedeutung: "innerhalb einer Zelle entlang erlaubter Richtung", kreuzt: []}
  QUER_STAENDER:     {bedeutung: "waagerecht durch einen Ständer in das Nachbargefach", kreuzt: [staender], bearbeitung: Drilling}
  QUER_RIEGEL:       {bedeutung: "senkrecht durch Schwelle, Rähm oder Riegel", kreuzt: [schwelle_raehm_riegel], bearbeitung: Drilling}
  QUER_BALKEN:       {bedeutung: "waagerecht durch einen Deckenbalken", kreuzt: [balken], bearbeitung: Drilling}
  SENKRECHT_DECKE:   {bedeutung: "senkrecht durch die Deckenbeplankung in einem Balkenfeld", kreuzt: [beplankung], bearbeitung: Drilling}
  DURCH_PLATTE:      {bedeutung: "durch eine Beplankung zum Raum oder zur Vorwand (Dose, Anschluss)", kreuzt: [beplankung], bearbeitung: "Drilling bzw. Dosenfräsung"}
  DURCH_LUFTDICHT:   {bedeutung: "durch eine Schicht mit luftdicht = true", kreuzt: [luftdichte_schicht], fuellung: "Manschette oder luftdichte Dose"}
  DURCH_BRAND:       {bedeutung: "durch ein Bauteil mit Feuerwiderstandsanforderung", kreuzt: [feuerwiderstandsfaehiges_bauteil], fuellung: "Abschottung mit Nachweis"}
  ELEMENTSTOSS:      {bedeutung: "über die Grenze zweier Fertigteile", kreuzt: [], kupplung: "Leerrohrstoß, Steckverbinder, Montageöffnung"}
  ANSCHLUSS:         {bedeutung: "Port zu Zelle", kreuzt: []}
kantenattribute: [laenge_m, richtung, boegen_90, dz_m, kreuzt, gewerk_maske, kapazitaet_mm2, element_guid]
```

## 5 Kosten

Die Kosten einer Kante *e* für ein Netz des Gewerks *g* sind

    c_g(e) = w_L,g · L(e) + w_B,g · n_Bogen(e) + Σ_{x ∈ X(e)} w_x,g + w_H,g · max(0, H_erf − H_frei) + w_P,g · p(e)

mit Länge *L*, Zahl der 90°-Bögen, einer Strafe je gekreuztem Bauteiltyp *x*, einer Strafe für fehlende Aufbauhöhe (nur weiche Fälle) und einem Präferenzterm *p* (zum Beispiel Vorfertigung im Werk bevorzugt, Parallelführung PWC/PWH vermeiden). Alle Gewichte sind ≥ 0; deshalb ist *h*(*v*) = min_g w_L,g · Manhattan(*v*, Ziel) eine zulässige Heuristik für A*.

```yaml
gewichte:            # Platzhalter [U]; Einheit: Kosteneinheiten (KE); w_L in KE/m
  status: U
  default:           {w_L: 1.0, w_B: 0.5, staender: 0.4, schwelle_raehm_riegel: 0.4, balken: 0.6, beplankung: 0.1, luftdichte_schicht: 5.0, feuerwiderstandsfaehiges_bauteil: 8.0, elementstoss: 1.0, w_H: 0.05, w_P: 1.0}
  abwasser:          {w_L: 1.0, w_B: 1.0, balken: 2.0}
  lueftung:          {w_L: 1.0, w_B: 0.8}
  trinkwasser:       {w_L: 1.2, w_B: 0.3}
  heizung:           {w_L: 1.0, w_B: 0.3}
  elektro:           {w_L: 1.0, w_B: 0.5}
  daten:             {w_L: 1.0, w_B: 0.5}
kalibrierung: "Gewichte werden gegen Werkplanungen des Herstellers kalibriert (Kapitel 20); Zielgrößen: Zahl der Bohrungen, Länge, Montagezeit."
```

## 6 Constraints

Harte Constraints entfernen Kanten oder Pfade (Kosten ∞). Jede Entfernung wird mit Regel-ID protokolliert, damit eine Ablehnung ihre Begründung nennen kann (Kapitel 9.5).

```yaml
constraints:
  K1_zone:          {regel: DE.DIN18015-3.Installationszonen-Wand, gewerk: [elektro, daten], art: kante, wirkung: "Wandkanten nur innerhalb Z; waagerecht nur ZW-*, senkrecht nur ZS-*; Ausnahme Überdeckung >= 60 mm oder unverfüllter Hohlraum"}
  K2_zone_decke:    {regel: DE.DIN18015-3.Installationszonen-Decke, gewerk: [elektro, daten], art: kante, wirkung: "Deckenkanten mit Wandabstand >= 20 cm (ZD-r) bzw. 15 cm (ZD-t)"}
  K3_staender:      {regel: M.Firma.Staenderbohrung, gewerk: alle, art: kante, wirkung: "QUER_STAENDER nur wenn d <= p · t (p = 0,25 Platzhalter), mittig; sonst Kante entfernt, Alternative Ständerauswechslung als Konstruktionsänderung"}
  K4_balken:        {regel: DE.EC5-NA.NA67.Durchbruch, gewerk: alle, art: kante, wirkung: "QUER_BALKEN: d <= 50 mm Querschnittsschwächung (erlaubt, Kosten); sonst nur wenn h_d <= 0,15 h ∧ h_ro, h_ru >= 0,35 h ∧ l_A >= h/2 ∧ l_z >= max(1,5 h; 300 mm)"}
  K5_senkrecht_balken: {regel: DE.EC5-NA.NA67.Durchbruch, gewerk: alle, art: kante, wirkung: "senkrecht nie durch den Balken selbst; nur im Balkenfeld mit Randabstand; sonst Wechsel (M.Firma.Fallleitung-Gefachmitte)"}
  K6_luftdicht:     {regel: DE.DIN4108-7.Luftdichte-Durchdringung, gewerk: alle, art: kante, wirkung: "DURCH_LUFTDICHT nur wenn eine freigegebene Manschette mit d_min <= d_a <= d_max bzw. eine luftdichte Dose existiert"}
  K7_kollision:     {regel: M.Firma.Routing-Kollisionsfreiheit, gewerk: alle, art: ressource, wirkung: "Querschnittskapazität je Zelle; Abstand >= clearance(g_i, g_j) zu belegten Trassen"}
  K8_brand:         {regel: BY.MLAR.Abschottung, gewerk: alle, art: kante, wirkung: "DURCH_BRAND nur mit Abschottungssystem mit Nachweis für das Bauteil; GK 1/2 und innerhalb von Wohnungen: keine Anforderung"}
  K9_schutzbereich: {regel: DE.VDE0100-701.Schutzbereiche, gewerk: [elektro], art: kante, wirkung: "Kanten durch Bereich 1 nur senkrecht von oben/hinten zu Betriebsmitteln dieses Bereichs; raumfremde Leitungen mit >= 6 cm Restwand"}
  K10_gefaelle:     {regel: DE.DIN1986-100.Gefaelle, gewerk: [abwasser], art: pfad, wirkung: "z monoton fallend in Fließrichtung; H_erf = d_a + 2 s + J · L <= H_frei der Lage"}
  K11_unbelueftet:  {regel: DE.DIN1986-100.Einzelanschluss-unbelueftet, gewerk: [abwasser], art: pfad, wirkung: "Ressourcen L <= 4 m, Bögen <= 3, Δh <= 1 m"}
  K12_3liter:       {regel: DE.DVGW-W551.3-Liter, gewerk: [trinkwasser_warm], art: pfad, wirkung: "Ressource Σ π/4 d_i² L <= 3 l je Fließweg ohne Zirkulation"}
  K13_lueftung:     {regel: M.Hersteller.Lueftungsstrang, gewerk: [lueftung], art: kante, wirkung: "Biegeradius >= Herstellerwert; Strang q <= q_max; keine Kanten durch Fortluft-/Außenluftfremde Zonen"}
  K14_sperrvolumen: {regel: [DE.VDE-AR-N4100.Zaehlerplatz, M.Hersteller.R290-Schutzbereich], gewerk: alle, art: knoten, wirkung: "Zellen, die Bedienbereiche oder Schutzbereiche schneiden, sind für Leitungen gesperrt; R290: Durchführungen gasdicht"}
  K15_elementstoss: {regel: M.Firma.Routing-Kollisionsfreiheit, gewerk: alle, art: kante, wirkung: "ELEMENTSTOSS nur an freigegebenen Kupplungsstellen (DAT-13-01)"}
```

## 7 Algorithmus

**Eingabe:** Graph *G*, Netze *N*, Gewichte, Constraints. **Ausgabe:** je Netz ein Baum *P*(*n*) mit Segmenten, Formteilen, Kreuzungen und Protokoll.

```text
ROUTE_ALL(G, N):
  order := sort N by (rang(g), −d, id)                  # rang: Abwasser 1, Lüftung 2, Trinkwasser 3,
                                                        # Heizung 4, Elektro 5, Daten 6 (E13.4)
  for n in order:
    P[n] := ROUTE_NET(G, n)
    if P[n] = ∅: konflikt := CONFLICT(G, n); if konflikt: RIP_UP_REROUTE(konflikt) else REPORT(n, unlösbar)
    BLOCK(G, P[n] ⊕ clearance)                          # K7: Kapazität reduzieren, Nachbarkanten verteuern
  CHECK_ALL(P)                                          # unabhängige Prüfung: Regeln, IfcClash, IDS
  return P

ROUTE_NET(G, n):                                        # Steiner-Näherung über kürzeste Wege
  T := {q_n}; R := terminals(n) sorted by id
  while R ≠ ∅:
    (t, path) := argmin_{t ∈ R} A*(G_n, t → T, c_g, h)  # G_n: G ohne Kanten mit K(e, n) = verletzt
                                                        # Ressourcen (K10–K12) als Labels im A*-Zustand
    if path = ∅: return ∅
    T := T ∪ nodes(path); R := R \ {t}
  return POSTPROCESS(T)                                 # kollineare Segmente zusammenfassen, Bögen
                                                        # reduzieren, Formteile (BEND, JUNCTION) setzen

RIP_UP_REROUTE(konflikt):                               # höchstens k_max Runden (Platzhalter 5)
  opfer := Netz mit höherem rang im Konflikt            # Abwasser wird nie verdrängt
  UNBLOCK(P[opfer]); erhöhe Kosten der Konfliktkanten für opfer um Faktor 2
  P[n] := ROUTE_NET(G, n); P[opfer] := ROUTE_NET(G, opfer)
  bleibt Konflikt nach k_max: REPORT(n, opfer, konfliktkanten) mit Alternativen A1–A5
```

```yaml
algorithmus:
  suche: "A* mit h = w_L · Manhattan-Abstand (zulässig, da alle Kosten >= w_L · L)"
  mehrere_terminals: "iterative Kürzeste-Wege-Näherung des Steiner-Baums (ROUTE_NET); Alternative für kleine Netze: exakte Aufzählung"
  ressourcen: "Label-Setting: Zustand = (Knoten, L_unbelueftet, n_Bogen, V_Liter, z); Dominanz nach Kosten und Ressourcen"
  reihenfolge: [abwasser, lueftung, trinkwasser_kalt, trinkwasser_warm, heizung, elektro, daten]
  konflikt: "Rip-up and Reroute mit Kostenerhöhung, k_max = 5 (Platzhalter U)"
  determinismus: "Gleichstand: kleinere Kosten, dann weniger Kreuzungen, dann lexikografisch kleinere Knoten-ID-Folge"
  bibliothek: "networkx (BSD-3) für A*; IfcOpenShell (LGPL-3.0+) für IFC und Ports; IfcClash für die nachgelagerte Prüfung"
```

## 8 Ausgabe

```yaml
ausgabe:
  segmente:       {pfadabschnitt: "IfcPipeSegment | IfcDuctSegment | IfcCableCarrierSegment CONDUITSEGMENT | IfcCableSegment", ports: "IfcDistributionPort über IfcRelNests, verbunden mit IfcRelConnectsPorts", system: "IfcRelAssignsToGroup → IfcDistributionSystem"}
  formteile:      {bogen: "IfcPipeFitting/IfcDuctFitting/IfcCableCarrierFitting BEND", abzweig: "JUNCTION", reduzierung: "TRANSITION"}
  kreuzung:       {vorschlag: "je Kreuzung Leitung × Bauteilschicht ein IfcVirtualElement PROVISIONFORVOID mit Pset_ProvisionForVoid (VoidShape, Diameter bzw. Width/Height, Depth, System); ohne Material"}
  nach_freigabe:  {oeffnung: "IfcOpeningElement OPENING je durchdrungenem Teil + IfcRelVoidsElement", beziehung: "IfcRelInterferesElements Leitung ↔ Bauteil (ImpliedOrder TRUE)", fuellung: "IfcRelFillsElement → IfcDiscreteAccessory USERDEFINED (Luftdichtheitsmanschette | Brandschutzmanschette)", umhuellung: "IfcCovering WRAPPING (Dämmschlauch) über IfcRelCoversBldgElements", konstruktion: "Wechsel/Stichbalken IfcBeam USERDEFINED; Ständerauswechslung IfcMember mit Riegeln"}
  fertigung:      {btlx: "Drilling (StartX, StartY, Angle, Inclination, DepthLimited, Depth, Diameter) je Part; Slot/Pocket für Kerven und Rechtecköffnungen; UserAttribute LeitungGUID und IfcGlobalId", wup: "Adapter nach DAT-04/DAT-13-11; Fräsung ab d_Fräs (M.Firma.Fraesgrenze); Zuordnung über export_guid.csv", koordinaten: "bauteillokal (Referenzfläche ReferencePlaneID)"}
  bericht:        {bcf: "je abgelehnte oder verschobene Kreuzung ein BCF-Thema mit Viewpoint und GUIDs (E8.25)", nachweis: "je Regelprüfung ein Nachweis nach Kapitel 7a"}
```

## 9 Austauschformat für Tests

```yaml
graph_json:
  knoten: [{id: string, typ: "GEFACH|ZONE|VORWAND|SCHACHT|DECKENFELD|DACHFELD|UEBERGANG|PORT", element_guid: string, box_mm: [xmin, ymin, zmin, xmax, ymax, zmax], attribute: object}]
  kanten: [{von: string, nach: string, typ: string, laenge_m: number, boegen_90: integer, dz_m: number, kreuzt: [string], gewerk_maske: [string]}]
  netze:  [{id: string, gewerk: string, quelle: string, terminals: [string], d_a_mm: number, ressourcen: object}]
```

## 10 Testfälle

```yaml
testfaelle:
  - id: T1_zone_gegen_bohrung
    beschreibung: "Innenwand 5,00 m, Ständer 60 mm im Raster 625 mm, Balkenfeld parallel zur Wand; Einspeisung V im Deckenfeld über der Ecke; Steckdose S bei x = 3,45 m, z = 1,15 m (ZW-m, Küche); Gewichte default"
    erwartet_ohne_ausnahme: {pfad: "V → Decke 0,20 m → Rähm bei x = 0,20 (ZS-e) → senkrecht 1,35 m → ZW-m waagerecht 3,25 m → S", laenge_m: 4.80, boegen: 2, staenderbohrungen: 5, kosten_KE: 8.20}
    erwartet_mit_ausnahme: {pfad: "V → Decke 3,45 m → Rähm bei x = 3,45 → senkrecht im Gefach 1,35 m → S", laenge_m: 4.80, boegen: 1, staenderbohrungen: 0, kosten_KE: 5.70}
    quelle: "Rechenbeispiel Kapitel 13.10 (mit networkx nachgerechnet)"
  - id: T2_dn50_quer_balken
    beschreibung: "Anschlussleitung DN 50 (Öffnung Ø 60 mm) quer zu Balken h = 240 mm"
    erwartet: {kante_QUER_BALKEN: entfernt, grund: "DE.EC5-NA.NA67.Durchbruch: 60 mm > 36 mm", alternative: "Führung parallel zu den Balken (B14 Variante B)"}
    quelle: B15 BD-1
  - id: T3_b15_regression
    beschreibung: "Fallleitung SW-01 DN 100 bei x = 3150 mm, y = 2100 mm"
    erwartet: {oeffnung_decke_wand_mm: 150, oeffnung_dach_mm: 130, strategie: Wechsel, provisionforvoid: 4, opening: 4, voids: 4, interferes: 4, fills: 1, btlx_drilling: 5, verstoesse: ["D3 Mündungsabstand", "BD-1 NA.6.7"]}
    quelle: "B15 (ausgabe/b15_durchdringungen.json)"
  - id: T4_determinismus
    beschreibung: "zwei Läufe mit PYTHONHASHSEED 1 und 4711"
    erwartet: {pfade: identisch, globalids: identisch}
  - id: T5_3liter
    beschreibung: "PWH 20×2 (0,201 l/m) von 15,5 m ohne Zirkulation"
    erwartet: {V_Weg_l: 3.12, ergebnis: verletzt, alternative: "Zirkulation oder Speicher näher"}
```

# Nachweisheft B2 – IDS-Prüfung, Fall „bestanden“

## Deckblatt

| Merkmal | Wert |
|---|---|
| Projekt | Beispielhaus Holzrahmenbau |
| Gebäude | Einfamilienhaus (fiktiv) |
| Geschoss | EG |
| Parametermodell | daten/wandelement.json (SHA-256 dcdbed63cc3d9ae5…) |
| Grundstück | daten/grundstueck.json (SHA-256 a60954d2a172493d…) |
| Rechtsstand der Beispiele | 27.09.2026 |
| Hinweis | Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis. |
| Verfasser | Entwurfsgenerator (Beispiel), ohne Prüfvermerk |
| Gesamtergebnis | **[ERFÜLLT]** (11 erfüllt, 0 nicht erfüllt, 0 Hinweis) |
| Heft-Hash (SHA-256) | `110675e58e78712267822b30fed5f19413fd9722003213ab26a9be507133fb82` |
| Zeitstempel | nicht gesetzt (deterministischer Lauf) |

Regelwerk-Profile:

- `HRB-IDS-Wandelement` Version `0.1.0`

Regelquellen:

- holzrahmenbau.ids (Information Delivery Specification, IDS 1.0), Fassung IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… [V]

## Inhaltsverzeichnis

| Nr. | ID | Titel | Status | η | Hash (Anfang) |
|---:|---|---|---|---:|---|
| 1 | [N-B2-bestanden-HRB-01](#n-n-b2-bestanden-hrb-01) | IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (bestanden) | erfüllt | – | `efed7f97dd13` |
| 2 | [N-B2-bestanden-HRB-02](#n-n-b2-bestanden-hrb-02) | IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (bestanden) | erfüllt | – | `167f8e89385b` |
| 3 | [N-B2-bestanden-HRB-03](#n-n-b2-bestanden-hrb-03) | IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (bestanden) | erfüllt | – | `dca3a7c3689f` |
| 4 | [N-B2-bestanden-HRB-04](#n-n-b2-bestanden-hrb-04) | IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (bestanden) | erfüllt | – | `2a8caea35af4` |
| 5 | [N-B2-bestanden-HRB-05](#n-n-b2-bestanden-hrb-05) | IDS HRB-05: Ständer: Material KVH C24 (bestanden) | erfüllt | – | `197e7910e0fe` |
| 6 | [N-B2-bestanden-HRB-06](#n-n-b2-bestanden-hrb-06) | IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (bestanden) | erfüllt | – | `e240b9ed033d` |
| 7 | [N-B2-bestanden-HRB-07](#n-n-b2-bestanden-hrb-07) | IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (bestanden) | erfüllt | – | `f41548dac89c` |
| 8 | [N-B2-bestanden-HRB-08](#n-n-b2-bestanden-hrb-08) | IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (bestanden) | erfüllt | – | `7fd66bfde091` |
| 9 | [N-B2-bestanden-HRB-09](#n-n-b2-bestanden-hrb-09) | IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (bestanden) | erfüllt | – | `bb036b74c9bd` |
| 10 | [N-B2-bestanden-HRB-10](#n-n-b2-bestanden-hrb-10) | IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (bestanden) | erfüllt | – | `c8b9bb7cc9b7` |
| 11 | [N-B2-bestanden-HRB-11](#n-n-b2-bestanden-hrb-11) | IDS HRB-11: Keine unklassifizierten Proxy-Elemente (bestanden) | erfüllt | – | `3410340e7df5` |

<a id="n-n-b2-bestanden-hrb-01"></a>

## N-B2-bestanden-HRB-01 – IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 1 anwendbare Elemente (All IFCWALL data; Elements with IsExternal data of TRUE in the dataset Pset_WallCommon) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |

### Regel

> Jede Außenwand trägt Pset_WallCommon.ThermalTransmittance mit U <= 0,20 W/(m²K) (Projektanforderung, Beispiel). Anwendbarkeit: All IFCWALL data; Elements with IsExternal data of TRUE in the dataset Pset_WallCommon. Anforderung: ThermalTransmittance data shall be {'minExclusive': '0', 'maxInclusive': '0.20'} and in the dataset Pset_WallCommon.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-01 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-01: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 0\ \mathrm{Stk} = 1\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-01 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-01/anteil: HRB-01: Elemente mit und ohne Verstoß**

![HRB-01: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-01_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `efed7f97dd138c1d58173416a5a62fa17194f13c1702cc5f2ea4e41db2cbca12`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-02"></a>

## N-B2-bestanden-HRB-02 – IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |

### Regel

> Jede Wand gibt Pset_WallCommon.IsExternal und LoadBearing an. Anwendbarkeit: All IFCWALL data. Anforderung: IsExternal data shall be provided in the dataset Pset_WallCommon; LoadBearing data shall be provided in the dataset Pset_WallCommon.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-02 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-02: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 0\ \mathrm{Stk} = 1\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-02 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-02 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-02/anteil: HRB-02: Elemente mit und ohne Verstoß**

![HRB-02: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-02_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `167f8e89385be0bbd87db5e9c33f539d3c9bd1841084964cdba198522ca9f219`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-03"></a>

## N-B2-bestanden-HRB-03 – IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |

### Regel

> Jede Wand ist nach DIN 276 in eine Kostengruppe 330–339 (Außenwände) klassifiziert. Anwendbarkeit: All IFCWALL data. Anforderung: Shall have a DIN 276 reference of {'pattern': '33[0-9]'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-03 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-03: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 0\ \mathrm{Stk} = 1\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-03 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-03 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-03/anteil: HRB-03: Elemente mit und ohne Verstoß**

![HRB-03: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-03_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `dca3a7c3689f91270da609581540c5d3d1aae8f2c1e8f01da9bed67f33ef17e9`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-04"></a>

## N-B2-bestanden-HRB-04 – IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |

### Regel

> Jede Wand hat ein Material; im Generator ist das eine IfcMaterialLayerSetUsage. Anwendbarkeit: All IFCWALL data. Anforderung: Shall have a material.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-04 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-04: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 0\ \mathrm{Stk} = 1\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-04 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-04 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-04/anteil: HRB-04: Elemente mit und ohne Verstoß**

![HRB-04: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-04_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `2a8caea35af427c7e80386a2a5f4daef976bf04fc1cd167cdeacb92e972f307a`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-05"></a>

## N-B2-bestanden-HRB-05 – IDS HRB-05: Ständer: Material KVH C24 (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 15 anwendbare Elemente (All IFCMEMBER data of type STUD) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `0ruebnGhrPUPaN5fsim6Vf`, `26xC9QsMnO6BHuxmSviBaF`, `254V3I5NrHxx6g9J9WAbEp`, `3ZVVDbGwDO7x2vg7I4UXpp`, `3BO1mSw7HO89jMsBG9Jb7H`, `1Shh7ZI39PQgxArHuFCIxO`, `2rWYAdwuXR2upUkdv7j_IN`, `18vNpgLaTOYgpLpdvN0aeA`, `02QVWAdt9VqxV8$c1qnuss`, `2D$QiiYtvNEfIXBRFteHwH`, `34BO68Wo1LCuqY8xgHmwWu`, `3AhW$EEQvKugecqAFgh9u9` … |

### Regel

> Jeder Ständer (IfcMember STUD) hat ein Material, dessen Name mit 'KVH C24' beginnt. Anwendbarkeit: All IFCMEMBER data of type STUD. Anforderung: Shall have a material of {'pattern': 'KVH C24.*'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-05 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 15 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-05: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 15\ \mathrm{Stk} - 0\ \mathrm{Stk} = 15\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 15 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-05 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-05 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-05/anteil: HRB-05: Elemente mit und ohne Verstoß**

![HRB-05: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-05_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `197e7910e0fe0d78e9450b604fa28ed9c9d10edf23a72206ef2690e543651799`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-06"></a>

## N-B2-bestanden-HRB-06 – IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 18 anwendbare Elemente (All IFCMEMBER data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `3N9BxbmVjJqfMasIm6VCTu`, `1TymEnbXzHcunnMbwZo5Cm`, `0ruebnGhrPUPaN5fsim6Vf`, `26xC9QsMnO6BHuxmSviBaF`, `254V3I5NrHxx6g9J9WAbEp`, `3ZVVDbGwDO7x2vg7I4UXpp`, `3BO1mSw7HO89jMsBG9Jb7H`, `1Shh7ZI39PQgxArHuFCIxO`, `2rWYAdwuXR2upUkdv7j_IN`, `0AkqIXRtnLZxJbnMw9nqYO`, `18vNpgLaTOYgpLpdvN0aeA`, `02QVWAdt9VqxV8$c1qnuss` … |

### Regel

> Jedes IfcMember hat Qto_MemberBaseQuantities.Length und NetVolume (für Abbundliste/Kalkulation). Anwendbarkeit: All IFCMEMBER data. Anforderung: Length data shall be provided in the dataset Qto_MemberBaseQuantities; NetVolume data shall be provided in the dataset Qto_MemberBaseQuantities.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-06 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 18 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-06: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 18\ \mathrm{Stk} - 0\ \mathrm{Stk} = 18\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 18 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-06 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-06 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-06/anteil: HRB-06: Elemente mit und ohne Verstoß**

![HRB-06: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-06_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `e240b9ed033dfbb76f200836b1ea67bd955f2d56985b59d7414da7bb67bbc8a9`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-07"></a>

## N-B2-bestanden-HRB-07 – IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 41 anwendbare Elemente (All {'enumeration': ['IFCMEMBER', 'IFCPLATE', 'IFCBUILDINGELEMENTPART']} data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `3lvMev6E9LueSQsQL9SyqJ`, `1ywZMKJxHHBwmNn$0DLcPP`, `2kOR3SNJLRhvgIkZqCD35O`, `0VAqV5cMTKoxFvJZ1sRPIh`, `1tGyPqPTzVWAaP6qdMPAhC`, `0sFfeJ3pvQ$eLlaJ2G66F8`, `1smMtnPdLGAwZZZIO4b8b3`, `3rhw57K3fGLOwjuPbWNuIt`, `32e_GlraTGcPYRh18u2qEF`, `1Do_$HborOExVic9UwPLxq`, `2lwpYyXkHJi9POHX6FZxkn`, `3lsRC1LKzOzeO81ZbRUvP3` … |

### Regel

> Jedes IfcMember, IfcPlate und IfcBuildingElementPart ist über IfcRelAggregates Teil einer IfcWall. Anwendbarkeit: All {'enumeration': ['IFCMEMBER', 'IFCPLATE', 'IFCBUILDINGELEMENTPART']} data. Anforderung: An element must have an IFCRELAGGREGATES relationship with an IFCWALL.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-07 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 41 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-07: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 41\ \mathrm{Stk} - 0\ \mathrm{Stk} = 41\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 41 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-07 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-07 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-07/anteil: HRB-07: Elemente mit und ohne Verstoß**

![HRB-07: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-07_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `f41548dac89c9d9a0dbeb8ba9c75327bfb9895f0045de01b1f8ecdb5eeebdc32`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-08"></a>

## N-B2-bestanden-HRB-08 – IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 1 anwendbare Elemente (All IFCMECHANICALFASTENERTYPE data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `10kcZK2DzMauPxIfg5Yrjt` |

### Regel

> Jeder IfcMechanicalFastenerType gibt NominalDiameter und NominalLength an. Anwendbarkeit: All IFCMECHANICALFASTENERTYPE data. Anforderung: The NominalDiameter shall be provided; The NominalLength shall be provided.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-08 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-08: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 0\ \mathrm{Stk} = 1\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-08 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-08 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-08/anteil: HRB-08: Elemente mit und ohne Verstoß**

![HRB-08: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-08_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `7fd66bfde0917bf9428a56db4d67880bd95d640f7c1a12077905038af3c5eed7`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-09"></a>

## N-B2-bestanden-HRB-09 – IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 176 anwendbare Elemente (All IFCMECHANICALFASTENER data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `39T8Vw55TT3BNaXCjVnHka`, `2LK0D15qDLIeeLmQIUpDKF`, `03p5SdiZHRCOt6vnISiQTU`, `34qH3t$EnVNw_5m_ScCw8W`, `1bIh0GI91UqOR6WrOOk916`, `3A7FgnPFbPVf127Vh8zJ5l`, `2QWW7utA9QC8KEdBDl7ZUD`, `2$Z16YAuDTjB3KIHN4kjFe`, `2istCiW8LPHO8exuLlTSRF`, `0C5DVI2hLJuRjcCk1h99cE`, `0iKI3vu2PJkeduptESFlTQ`, `02jeHreGLMD9_yczVveoz4` … |

### Regel

> Jedes IfcMechanicalFastener gibt NominalDiameter an (zwischen 2 und 12 mm, Projekteinheit mm). Anwendbarkeit: All IFCMECHANICALFASTENER data. Anforderung: The NominalDiameter shall be {'minInclusive': '2', 'maxInclusive': '12'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-09 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 176 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-09: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 176\ \mathrm{Stk} - 0\ \mathrm{Stk} = 176\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 176 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-09 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-09 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-09/anteil: HRB-09: Elemente mit und ohne Verstoß**

![HRB-09: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-09_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `bb036b74c9bd2c3416f17788a337b91806420d1928a4e6cb4c11081eb67fd76c`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-10"></a>

## N-B2-bestanden-HRB-10 – IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 12 anwendbare Elemente (All IFCBUILDINGELEMENTPART data of type INSULATION) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `1ywZMKJxHHBwmNn$0DLcPP`, `2kOR3SNJLRhvgIkZqCD35O`, `0VAqV5cMTKoxFvJZ1sRPIh`, `1tGyPqPTzVWAaP6qdMPAhC`, `0sFfeJ3pvQ$eLlaJ2G66F8`, `1smMtnPdLGAwZZZIO4b8b3`, `3rhw57K3fGLOwjuPbWNuIt`, `32e_GlraTGcPYRh18u2qEF`, `1Do_$HborOExVic9UwPLxq`, `2lwpYyXkHJi9POHX6FZxkn`, `3lsRC1LKzOzeO81ZbRUvP3`, `3Ea167a$bV2f_2XSF35CFa` |

### Regel

> Jedes IfcBuildingElementPart INSULATION hat ein Material der Kategorie 'insulation'. Anwendbarkeit: All IFCBUILDINGELEMENTPART data of type INSULATION. Anforderung: Shall have a material of insulation.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-10 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 12 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-10: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 12\ \mathrm{Stk} - 0\ \mathrm{Stk} = 12\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 12 Stk | ≥ | 1 Stk | – | erfüllt | holzrahmenbau.ids, HRB-10 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-10 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-10/anteil: HRB-10: Elemente mit und ohne Verstoß**

![HRB-10: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-10_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `c8b9bb7cc9b77c9812484c5a74d7994476e0c8804dc9cc198090ef34822dd575`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-11"></a>

## N-B2-bestanden-HRB-11 – IDS HRB-11: Keine unklassifizierten Proxy-Elemente (bestanden)

**Ergebnis: [ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement.ifc: 0 anwendbare Elemente (Shall not be IFCBUILDINGELEMENTPROXY data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement.ifc (`5a796ea7b0f1d8c0…`) |

### Regel

> Das Modell enthält kein IfcBuildingElementProxy (jedes Bauteil hat eine fachliche IFC-Klasse). Anwendbarkeit: Shall not be IFCBUILDINGELEMENTPROXY data. Anforderung: –.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-11 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| höchstzulässige Anzahl | $n_{\mathrm{max}}$ | 0 Stk | – | grenzwert | IDS HRB-11: maxOccurs = 0 (verboten) |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement.ifc, SHA-256 5a796ea7b0f1d8c0…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = ja

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 0\ \mathrm{Stk} - 0\ \mathrm{Stk} = 0\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| keine anwendbaren Elemente (verboten) | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-11 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-11/anteil: HRB-11: Elemente mit und ohne Verstoß**

![HRB-11: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-11_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `3410340e7df5b335174d534341395a7880f7dda47ea1daf6ab51d2ec3c367410`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung; Gleitkommazahlen auf 12 signifikante Stellen normiert
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


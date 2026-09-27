# Nachweisheft B2 – IDS-Prüfung, Fall „fehlerhaft“

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
| Gesamtergebnis | **[NICHT ERFÜLLT]** (5 erfüllt, 6 nicht erfüllt, 0 Hinweis) |
| Heft-Hash (SHA-256) | `c8f247dd98509cee6f17049a14ceacbea4845eec713f8c747269936f9bf62f3b` |
| Zeitstempel | nicht gesetzt (deterministischer Lauf) |

Die Datei enthält sechs absichtlich eingebaute Fehler (F1–F6, siehe b2_ids_pruefung.py); die zugehörigen Nachweise müssen scheitern.

Regelwerk-Profile:

- `HRB-IDS-Wandelement` Version `0.1.0`

Regelquellen:

- holzrahmenbau.ids (Information Delivery Specification, IDS 1.0), Fassung IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… [V]

## Inhaltsverzeichnis

| Nr. | ID | Titel | Status | η | Hash (Anfang) |
|---:|---|---|---|---:|---|
| 1 | [N-B2-fehlerhaft-HRB-01](#n-n-b2-fehlerhaft-hrb-01) | IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (fehlerhaft) | nicht erfüllt | – | `bf12eefe06ac` |
| 2 | [N-B2-fehlerhaft-HRB-02](#n-n-b2-fehlerhaft-hrb-02) | IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (fehlerhaft) | erfüllt | 1,000 | `04871a656dde` |
| 3 | [N-B2-fehlerhaft-HRB-03](#n-n-b2-fehlerhaft-hrb-03) | IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (fehlerhaft) | nicht erfüllt | – | `b6e972fbf219` |
| 4 | [N-B2-fehlerhaft-HRB-04](#n-n-b2-fehlerhaft-hrb-04) | IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (fehlerhaft) | erfüllt | 1,000 | `f17eac599b12` |
| 5 | [N-B2-fehlerhaft-HRB-05](#n-n-b2-fehlerhaft-hrb-05) | IDS HRB-05: Ständer: Material KVH C24 (fehlerhaft) | nicht erfüllt | – | `966c1ff4ef61` |
| 6 | [N-B2-fehlerhaft-HRB-06](#n-n-b2-fehlerhaft-hrb-06) | IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (fehlerhaft) | erfüllt | 0,056 | `b29de8bd3acd` |
| 7 | [N-B2-fehlerhaft-HRB-07](#n-n-b2-fehlerhaft-hrb-07) | IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (fehlerhaft) | erfüllt | 0,025 | `35231a0b0ea2` |
| 8 | [N-B2-fehlerhaft-HRB-08](#n-n-b2-fehlerhaft-hrb-08) | IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (fehlerhaft) | nicht erfüllt | – | `1dcf3fb0ce29` |
| 9 | [N-B2-fehlerhaft-HRB-09](#n-n-b2-fehlerhaft-hrb-09) | IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (fehlerhaft) | nicht erfüllt | – | `b388a1a2858a` |
| 10 | [N-B2-fehlerhaft-HRB-10](#n-n-b2-fehlerhaft-hrb-10) | IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (fehlerhaft) | erfüllt | 0,084 | `6fec51100a6f` |
| 11 | [N-B2-fehlerhaft-HRB-11](#n-n-b2-fehlerhaft-hrb-11) | IDS HRB-11: Keine unklassifizierten Proxy-Elemente (fehlerhaft) | nicht erfüllt | – | `1873cbe47177` |

<a id="n-n-b2-fehlerhaft-hrb-01"></a>

## N-B2-fehlerhaft-HRB-01 – IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (All IFCWALL data; Elements with IsExternal data of TRUE in the dataset Pset_WallCommon) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |

### Regel

> Jede Außenwand trägt Pset_WallCommon.ThermalTransmittance mit U <= 0,20 W/(m²K) (Projektanforderung, Beispiel). Anwendbarkeit: All IFCWALL data; Elements with IsExternal data of TRUE in the dataset Pset_WallCommon. Anforderung: ThermalTransmittance data shall be {'minExclusive': '0', 'maxInclusive': '0.20'} and in the dataset Pset_WallCommon.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-01 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-01: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 1\ \mathrm{Stk} = 0\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-01 |
| alle Anforderungen erfüllt | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: IfcWall „Außenwand Nord, Element 1“ GUID 0gsiGQj_bG3wx8M0qwRA0U: The property value "0.25" does not match the requirements
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-01/anteil: HRB-01: Elemente mit und ohne Verstoß**

![HRB-01: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-01_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `bf12eefe06ac119137a9171a8b1664d24f31c0dec7f2fa90403e048f7d31108d`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-02"></a>

## N-B2-fehlerhaft-HRB-02 – IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (fehlerhaft)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |

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

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-02 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-02 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-02/anteil: HRB-02: Elemente mit und ohne Verstoß**

![HRB-02: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-02_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `04871a656ddeb2f402bcb8f0e6249371f0cdbad28e949b36b40555b59ee83491`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-03"></a>

## N-B2-fehlerhaft-HRB-03 – IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |

### Regel

> Jede Wand ist nach DIN 276 in eine Kostengruppe 330–339 (Außenwände) klassifiziert. Anwendbarkeit: All IFCWALL data. Anforderung: Shall have a DIN 276 reference of {'pattern': '33[0-9]'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-03 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-03: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 1\ \mathrm{Stk} = 0\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-03 |
| alle Anforderungen erfüllt | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-03 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: IfcWall „Außenwand Nord, Element 1“ GUID 0gsiGQj_bG3wx8M0qwRA0U: The entity has no classification
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-03/anteil: HRB-03: Elemente mit und ohne Verstoß**

![HRB-03: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-03_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `b6e972fbf21970df62d6c7766406a1d477fc8c9ab76600c5d75f332e1d2c867c`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-04"></a>

## N-B2-fehlerhaft-HRB-04 – IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (fehlerhaft)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (All IFCWALL data) |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |

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

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-04 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-04 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-04/anteil: HRB-04: Elemente mit und ohne Verstoß**

![HRB-04: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-04_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `f17eac599b129fbefb8e36d9af67b76372d62cd21c02aeec11d28ad355967182`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-05"></a>

## N-B2-fehlerhaft-HRB-05 – IDS HRB-05: Ständer: Material KVH C24 (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 15 anwendbare Elemente (All IFCMEMBER data of type STUD) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
| weitere GUIDs | `0ruebnGhrPUPaN5fsim6Vf`, `26xC9QsMnO6BHuxmSviBaF`, `254V3I5NrHxx6g9J9WAbEp`, `3ZVVDbGwDO7x2vg7I4UXpp`, `3BO1mSw7HO89jMsBG9Jb7H`, `1Shh7ZI39PQgxArHuFCIxO`, `2rWYAdwuXR2upUkdv7j_IN`, `18vNpgLaTOYgpLpdvN0aeA`, `02QVWAdt9VqxV8$c1qnuss`, `2D$QiiYtvNEfIXBRFteHwH`, `34BO68Wo1LCuqY8xgHmwWu`, `3AhW$EEQvKugecqAFgh9u9` … |

### Regel

> Jeder Ständer (IfcMember STUD) hat ein Material, dessen Name mit 'KVH C24' beginnt. Anwendbarkeit: All IFCMEMBER data of type STUD. Anforderung: Shall have a material of {'pattern': 'KVH C24.*'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-05 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 15 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-05: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 15\ \mathrm{Stk} - 1\ \mathrm{Stk} = 14\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 15 Stk | ≥ | 1 Stk | 0,067 | erfüllt | holzrahmenbau.ids, HRB-05 |
| alle Anforderungen erfüllt | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-05 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: IfcMember „Ständer R2“ GUID 02QVWAdt9VqxV8$c1qnuss: The entity has no material
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-05/anteil: HRB-05: Elemente mit und ohne Verstoß**

![HRB-05: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-05_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `966c1ff4ef6129d2633fd62255774ff92e19abf728c97c340e95749470878c29`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-06"></a>

## N-B2-fehlerhaft-HRB-06 – IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (fehlerhaft)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,056

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 18 anwendbare Elemente (All IFCMEMBER data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
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

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

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
| Anwendbarkeit (Kardinalität) | 18 Stk | ≥ | 1 Stk | 0,056 | erfüllt | holzrahmenbau.ids, HRB-06 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-06 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-06/anteil: HRB-06: Elemente mit und ohne Verstoß**

![HRB-06: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-06_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `b29de8bd3acd29c03cc0cb103faca0f9b4d2dc8847d5bcdf4f1b7b1709eecf99`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-07"></a>

## N-B2-fehlerhaft-HRB-07 – IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (fehlerhaft)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,025

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 41 anwendbare Elemente (All {'enumeration': ['IFCMEMBER', 'IFCPLATE', 'IFCBUILDINGELEMENTPART']} data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
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

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

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
| Anwendbarkeit (Kardinalität) | 41 Stk | ≥ | 1 Stk | 0,025 | erfüllt | holzrahmenbau.ids, HRB-07 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-07 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-07/anteil: HRB-07: Elemente mit und ohne Verstoß**

![HRB-07: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-07_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `35231a0b0ea217d594196676c6425308297cc737ed0746acd6a7f3b2e7fcc79d`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-08"></a>

## N-B2-fehlerhaft-HRB-08 – IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (All IFCMECHANICALFASTENERTYPE data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
| weitere GUIDs | `10kcZK2DzMauPxIfg5Yrjt` |

### Regel

> Jeder IfcMechanicalFastenerType gibt NominalDiameter und NominalLength an. Anwendbarkeit: All IFCMECHANICALFASTENERTYPE data. Anforderung: The NominalDiameter shall be provided; The NominalLength shall be provided.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-08 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-08: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 1\ \mathrm{Stk} - 1\ \mathrm{Stk} = 0\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-08 |
| alle Anforderungen erfüllt | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-08 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: IfcMechanicalFastenerType „Spanplattenschraube 4,0x50“ GUID 10kcZK2DzMauPxIfg5Yrjt: The attribute value "None" is empty
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-08/anteil: HRB-08: Elemente mit und ohne Verstoß**

![HRB-08: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-08_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `1dcf3fb0ce29cb793b0f728101d78914b7257f00d1da2914d67e4a3629291c06`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-09"></a>

## N-B2-fehlerhaft-HRB-09 – IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 176 anwendbare Elemente (All IFCMECHANICALFASTENER data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
| weitere GUIDs | `39T8Vw55TT3BNaXCjVnHka`, `2LK0D15qDLIeeLmQIUpDKF`, `03p5SdiZHRCOt6vnISiQTU`, `34qH3t$EnVNw_5m_ScCw8W`, `1bIh0GI91UqOR6WrOOk916`, `3A7FgnPFbPVf127Vh8zJ5l`, `2QWW7utA9QC8KEdBDl7ZUD`, `2$Z16YAuDTjB3KIHN4kjFe`, `2istCiW8LPHO8exuLlTSRF`, `0C5DVI2hLJuRjcCk1h99cE`, `0iKI3vu2PJkeduptESFlTQ`, `02jeHreGLMD9_yczVveoz4` … |

### Regel

> Jedes IfcMechanicalFastener gibt NominalDiameter an (zwischen 2 und 12 mm, Projekteinheit mm). Anwendbarkeit: All IFCMECHANICALFASTENER data. Anforderung: The NominalDiameter shall be {'minInclusive': '2', 'maxInclusive': '12'}.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-09 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 176 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| Mindestanzahl anwendbarer Elemente | $n_{\mathrm{min}}$ | 1 Stk | – | grenzwert | IDS HRB-09: minOccurs = 1 |
| zulässige Verstöße | $n_{\mathrm{zul}}$ | 0 Stk | – | grenzwert | IDS 1.0: jede Anforderung gilt für jedes anwendbare Element |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

**Schritt 2: Elemente ohne Verstoß**

$$
n_{\mathrm{ok}} = n_{\mathrm{anw}} - n_{\mathrm{fehl}}
$$

$$
n_{\mathrm{ok}} = 176\ \mathrm{Stk} - 1\ \mathrm{Stk} = 175\ \mathrm{Stk}
$$

Ausdruck (maschinenlesbar): `n_anw - n_fehl`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Anwendbarkeit (Kardinalität) | 176 Stk | ≥ | 1 Stk | 0,006 | erfüllt | holzrahmenbau.ids, HRB-09 |
| alle Anforderungen erfüllt | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-09 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: IfcMechanicalFastener „Spanplattenschraube 4,0x50 #1“ GUID 39T8Vw55TT3BNaXCjVnHka: The attribute value "20.0" does not match the requirement
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-09/anteil: HRB-09: Elemente mit und ohne Verstoß**

![HRB-09: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-09_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `b388a1a2858a5cdc3a8468cf5a281375dacacf715b4972d8fff8bbd2833bdb4b`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-10"></a>

## N-B2-fehlerhaft-HRB-10 – IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (fehlerhaft)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,084

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 12 anwendbare Elemente (All IFCBUILDINGELEMENTPART data of type INSULATION) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
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

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

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
| Anwendbarkeit (Kardinalität) | 12 Stk | ≥ | 1 Stk | 0,084 | erfüllt | holzrahmenbau.ids, HRB-10 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-10 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-10/anteil: HRB-10: Elemente mit und ohne Verstoß**

![HRB-10: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-10_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `6fec51100a6f117525f19fcd05e2ace233bca66938d24fb9dabc076d4d590596`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-fehlerhaft-hrb-11"></a>

## N-B2-fehlerhaft-HRB-11 – IDS HRB-11: Keine unklassifizierten Proxy-Elemente (fehlerhaft)

**Ergebnis: [NICHT ERFÜLLT]**

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | wandelement_fehlerhaft.ifc: 1 anwendbare Elemente (Shall not be IFCBUILDINGELEMENTPROXY data) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | wandelement_fehlerhaft.ifc (`bc366788e43bc4ae…`) |
| weitere GUIDs | `0000000000000000000001` |

### Regel

> Das Modell enthält kein IfcBuildingElementProxy (jedes Bauteil hat eine fachliche IFC-Klasse). Anwendbarkeit: Shall not be IFCBUILDINGELEMENTPROXY data. Anforderung: –.

Quelle: holzrahmenbau.ids (Information Delivery Specification, IDS 1.0) · Fassung: IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… · Fundstelle: HRB-11 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-IDS-Wandelement` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| anwendbare Elemente | $n_{\mathrm{anw}}$ | 1 Stk | – | eingabe | ifctester 0.8.5: Specification.applicable_entities |
| Elemente mit Verstoß | $n_{\mathrm{fehl}}$ | 0 Stk | – | eingabe | ifctester 0.8.5: Specification.failed_entities |
| höchstzulässige Anzahl | $n_{\mathrm{max}}$ | 0 Stk | – | grenzwert | IDS HRB-11: maxOccurs = 0 (verboten) |

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: IDS-Prüfung des Modells**

Verfahren: ifctester 0.8.5: ids.open(validate=True) gegen die IDS-1.0-XSD, Specification.validate(IFC); Modell wandelement_fehlerhaft.ifc, SHA-256 bc366788e43bc4ae…

Ergebnis: $\mathrm{status}_{\mathrm{ifctester}}$ = nein

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
| keine anwendbaren Elemente (verboten) | 1 Stk | ≤ | 0 Stk | – | **nicht erfüllt** | holzrahmenbau.ids, HRB-11 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Befund: verbotenes Element IfcBuildingElementProxy „Unbekanntes Bauteil“ GUID 0000000000000000000001
- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-fehlerhaft-HRB-11/anteil: HRB-11: Elemente mit und ohne Verstoß**

![HRB-11: Elemente mit und ohne Verstoß](svg/N-B2-fehlerhaft-HRB-11_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `1873cbe4717710591c74ccd5b57d9cd513c858c5ed3396fcabbaeb53bbadc98f`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


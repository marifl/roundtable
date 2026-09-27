# Nachweisheft B1–B5 – Beispielhaus Holzrahmenbau (Proof of Concept)

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
| Gesamtergebnis | **[NICHT ERFÜLLT]** (20 erfüllt, 1 nicht erfüllt, 0 Hinweis) |
| Heft-Hash (SHA-256) | `6942614b079912cd9099e9b9ed1f3e8c76edf752a3eec1745f0d2a34226e501f` |
| Zeitstempel | nicht gesetzt (deterministischer Lauf) |

Das Heft bündelt die Nachweise der Beispiele B1–B5. Szenario „zu_nah“ (B4) ist absichtlich unzulässig; der IDS-Fall „fehlerhaft“ steht im eigenen Heft b2_ids_fehlerhaft.

Regelwerk-Profile:

- `BY-BayBO-2026-05` Version `0.1.0`
- `DE-DIN18065-WG2WE` Version `0.1.0`
- `DE-Waermeschutz-Beispiel` Version `0.1.0`
- `HRB-IDS-Wandelement` Version `0.1.0`
- `HRB-Mengen` Version `0.1.0`

Regelquellen:

- BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Fassung ab 01.05.2026 [U]
- DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02), Fassung 2020-08 [U]
- DIN EN ISO 6946:2018-03 (ISO 6946:2017); Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung), Fassung 2018-03 [V]
- Projektregel Mengenermittlung (eigene Festlegung), Fassung 2026-09 [V]
- holzrahmenbau.ids (Information Delivery Specification, IDS 1.0), Fassung IDS-Datei Version 0.1.0 vom 2026-01-01, SHA-256 31003d3f5117b785… [V]

## Inhaltsverzeichnis

| Nr. | ID | Titel | Status | η | Hash (Anfang) |
|---:|---|---|---|---:|---|
| 1 | [N-B1-01](#n-n-b1-01) | Mengen- und Massenermittlung Wandelement AW-01 (Außenwand Nord, Element 1) | erfüllt | 0,001 | `3984bfb486b3` |
| 2 | [N-B2-bestanden-HRB-01](#n-n-b2-bestanden-hrb-01) | IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (bestanden) | erfüllt | 1,000 | `6761c4520bc5` |
| 3 | [N-B2-bestanden-HRB-02](#n-n-b2-bestanden-hrb-02) | IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (bestanden) | erfüllt | 1,000 | `1569a8eec950` |
| 4 | [N-B2-bestanden-HRB-03](#n-n-b2-bestanden-hrb-03) | IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (bestanden) | erfüllt | 1,000 | `4d05e970d8fc` |
| 5 | [N-B2-bestanden-HRB-04](#n-n-b2-bestanden-hrb-04) | IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (bestanden) | erfüllt | 1,000 | `e117934af800` |
| 6 | [N-B2-bestanden-HRB-05](#n-n-b2-bestanden-hrb-05) | IDS HRB-05: Ständer: Material KVH C24 (bestanden) | erfüllt | 0,067 | `d4dea59fe39f` |
| 7 | [N-B2-bestanden-HRB-06](#n-n-b2-bestanden-hrb-06) | IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (bestanden) | erfüllt | 0,056 | `1ad6cb8a87d3` |
| 8 | [N-B2-bestanden-HRB-07](#n-n-b2-bestanden-hrb-07) | IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (bestanden) | erfüllt | 0,025 | `88c4b7bae0f0` |
| 9 | [N-B2-bestanden-HRB-08](#n-n-b2-bestanden-hrb-08) | IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (bestanden) | erfüllt | 1,000 | `3496ad701b0b` |
| 10 | [N-B2-bestanden-HRB-09](#n-n-b2-bestanden-hrb-09) | IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (bestanden) | erfüllt | 0,006 | `94a1ed6f892c` |
| 11 | [N-B2-bestanden-HRB-10](#n-n-b2-bestanden-hrb-10) | IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (bestanden) | erfüllt | 0,084 | `014c8a9805ed` |
| 12 | [N-B2-bestanden-HRB-11](#n-n-b2-bestanden-hrb-11) | IDS HRB-11: Keine unklassifizierten Proxy-Elemente (bestanden) | erfüllt | – | `68f2d76b3e98` |
| 13 | [N-B3-geometrie-verputzt](#n-n-b3-geometrie-verputzt) | U-Wert Außenwand AW-01 (Holzanteil aus der Elementgeometrie, verputzt) | erfüllt | 0,934 | `46b1a54c5c98` |
| 14 | [N-B3-geometrie-hinterlueftet](#n-n-b3-geometrie-hinterlueftet) | U-Wert Außenwand AW-01 (Holzanteil aus der Elementgeometrie, hinterlueftet) | erfüllt | 0,918 | `8a2c26bee9cd` |
| 15 | [N-B3-raster-verputzt](#n-n-b3-raster-verputzt) | U-Wert Außenwand AW-01 (Holzanteil aus dem Raster, verputzt) | erfüllt | 0,813 | `d83c1467a650` |
| 16 | [N-B3-raster-hinterlueftet](#n-n-b3-raster-hinterlueftet) | U-Wert Außenwand AW-01 (Holzanteil aus dem Raster, hinterlueftet) | erfüllt | 0,801 | `15589a73043a` |
| 17 | [N-B4-mittig-drittel](#n-n-b4-mittig-drittel) | Abstandsflächen Szenario „mittig“ (Haus mittig, 5 m zu den seitlichen Grenzen, Giebel: drittel) | erfüllt | 0,654 | `0676e9b04fab` |
| 18 | [N-B4-zu_nah-drittel](#n-n-b4-zu-nah-drittel) | Abstandsflächen Szenario „zu_nah“ (Haus 2 m an die westliche Grenze gerückt, Giebel: drittel) | nicht erfüllt | 1,634 | `833f7f6c74c3` |
| 19 | [N-B4-an_strasse-drittel](#n-n-b4-an-strasse-drittel) | Abstandsflächen Szenario „an_strasse“ (Haus 1 m hinter der Straßengrenze (Süd), Giebel: drittel) | erfüllt | 0,654 | `c39ad8abf914` |
| 20 | [N-B4-mittig-voll](#n-n-b4-mittig-voll) | Abstandsflächen Szenario „mittig“ (Haus mittig, 5 m zu den seitlichen Grenzen, Giebel: voll) | erfüllt | 0,654 | `e31acb476e7d` |
| 21 | [N-B5-01](#n-n-b5-01) | Treppenlauf gerade einläufig, Geschosshöhe 2,90 m | erfüllt | 0,972 | `0c03e40e3563` |

<a id="n-n-b1-01"></a>

## N-B1-01 – Mengen- und Massenermittlung Wandelement AW-01 (Außenwand Nord, Element 1)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,001

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Wandelement AW-01 mit 18 Hölzern |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (aus B1) (`5a796ea7b0f1d8c0…`) |
| weitere GUIDs | `3N9BxbmVjJqfMasIm6VCTu`, `1TymEnbXzHcunnMbwZo5Cm`, `0ruebnGhrPUPaN5fsim6Vf`, `26xC9QsMnO6BHuxmSviBaF`, `254V3I5NrHxx6g9J9WAbEp`, `3ZVVDbGwDO7x2vg7I4UXpp`, `3BO1mSw7HO89jMsBG9Jb7H`, `1Shh7ZI39PQgxArHuFCIxO`, `2rWYAdwuXR2upUkdv7j_IN`, `0AkqIXRtnLZxJbnMw9nqYO`, `18vNpgLaTOYgpLpdvN0aeA`, `02QVWAdt9VqxV8$c1qnuss` … |

### Regel

> Mengen und Massen des vorgefertigten Wandelements aus dem Parametermodell ermitteln; die Mengen müssen mit den Mengenangaben (Qto) des IFC-Modells übereinstimmen.

Quelle: Projektregel Mengenermittlung (eigene Festlegung) · Fassung: 2026-09 · Fundstelle: vgl. Qto_MemberBaseQuantities, Qto_PlateBaseQuantities (IFC 4.3) · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `HRB-Mengen` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Wandlänge | $L$ | 4800 mm | – | eingabe | daten/wandelement.json /wand/laenge |
| Wandhöhe | $H$ | 2750 mm | – | eingabe | daten/wandelement.json /wand/hoehe |
| Fensterbreite (Rohbau) | $b_{\mathrm{F}}$ | 1260 mm | – | eingabe | daten/wandelement.json /wand/oeffnungen/0/breite |
| Fensterhöhe (Rohbau) | $h_{\mathrm{F}}$ | 1385 mm | – | eingabe | daten/wandelement.json /wand/oeffnungen/0/hoehe |
| Holzquerschnittstiefe | $t_{\mathrm{H}}$ | 200 mm | – | eingabe | daten/wandelement.json /wand/staender/tiefe |
| Kervenbreite (= Ständerbreite) | $b_{\mathrm{K}}$ | 60 mm | – | eingabe | daten/wandelement.json /wand/staender/breite |
| Kerventiefe | $t_{\mathrm{K}}$ | 25 mm | – | eingabe | daten/wandelement.json /wand/kerven/0/tiefe |
| Kervenhöhe | $h_{\mathrm{K}}$ | 40 mm | – | eingabe | daten/wandelement.json /wand/kerven/0/hoehe |
| Dicke GKF | $d_{\mathrm{GKF}}$ | 12,5 mm | – | eingabe | daten/wandelement.json Schicht gkf |
| Dicke OSB/3 | $d_{\mathrm{OSB}}$ | 15 mm | – | eingabe | daten/wandelement.json Schicht osb |
| Dicke Gefach | $d_{\mathrm{G}}$ | 200 mm | – | eingabe | daten/wandelement.json Schicht gefach |
| Dicke Holzfaserdämmplatte | $d_{\mathrm{HFD}}$ | 60 mm | – | eingabe | daten/wandelement.json Schicht hfd |
| Schraubendurchmesser | $d_{\mathrm{S}}$ | 4 mm | – | eingabe | daten/wandelement.json /wand/verbindungsmittel/0/durchmesser |
| Schraubenlänge | $l_{\mathrm{S}}$ | 50 mm | – | eingabe | daten/wandelement.json /wand/verbindungsmittel/0/laenge |
| Rohdichte KVH C24 (Nadelholz) | $\rho_{\mathrm{kvh},\mathrm{c24}}$ | 420 kg/m³ | 42 kg/m³ | annahme | daten/wandelement.json /materialien/kvh_c24/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen |
| Rohdichte Gipsplatte Typ DF (GKF) | $\rho_{\mathrm{gkf}}$ | 800 kg/m³ | 40 kg/m³ | annahme | daten/wandelement.json /materialien/gkf/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 5 % angenommen |
| Rohdichte OSB/3 | $\rho_{\mathrm{osb3}}$ | 600 kg/m³ | 60 kg/m³ | annahme | daten/wandelement.json /materialien/osb3/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen |
| Rohdichte Holzfaser-Dämmmatte (flexibel) | $\rho_{\mathrm{holzfaser},\mathrm{flex}}$ | 50 kg/m³ | 7,5 kg/m³ | annahme | daten/wandelement.json /materialien/holzfaser_flex/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 15 % angenommen |
| Rohdichte Holzfaserdämmplatte (Putzträger) | $\rho_{\mathrm{holzfaserplatte}}$ | 180 kg/m³ | 18 kg/m³ | annahme | daten/wandelement.json /materialien/holzfaserplatte/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen |
| Rohdichte Stahl | $\rho_{\mathrm{St}}$ | 7850 kg/m³ | – | annahme | daten/wandelement.json /materialien/stahl_verzinkt/rho |
| zulässige Mengenabweichung Modell/IFC | $\mathrm{dV}_{\mathrm{zul}}$ | 1 · 10⁻⁸ m³ | – | grenzwert | Projektregel: Qto-Werte sind auf 1e-9 m³ gerundet; Summe über ≤ 18 Teile ergibt höchstens 9e-9 m³ |

### Annahmen

- **Annahme:** Die Dampfbremse (0,2 mm) hat im Parametermodell keine Rohdichte und bleibt in der Masse unberücksichtigt.
- **Annahme:** Schrauben als Zylinder d × l (Kopf und Gewinde nicht modelliert), wie die IFC-Geometrie.
- **Annahme:** Die Unsicherheiten der Rohdichten sind Annahmen zur Demonstration der Unsicherheitsfortpflanzung.
- **Annahme:** Rohdichte KVH C24 (Nadelholz) (rho_kvh_c24) = 420 kg/m³: daten/wandelement.json /materialien/kvh_c24/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen
- **Annahme:** Rohdichte Gipsplatte Typ DF (GKF) (rho_gkf) = 800 kg/m³: daten/wandelement.json /materialien/gkf/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 5 % angenommen
- **Annahme:** Rohdichte OSB/3 (rho_osb3) = 600 kg/m³: daten/wandelement.json /materialien/osb3/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen
- **Annahme:** Rohdichte Holzfaser-Dämmmatte (flexibel) (rho_holzfaser_flex) = 50 kg/m³: daten/wandelement.json /materialien/holzfaser_flex/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 15 % angenommen
- **Annahme:** Rohdichte Holzfaserdämmplatte (Putzträger) (rho_holzfaserplatte) = 180 kg/m³: daten/wandelement.json /materialien/holzfaserplatte/rho: Beispielwert (Mittelwert), keine Wichte nach DIN EN 1991-1-1; u = 10 % angenommen
- **Annahme:** Rohdichte Stahl (rho_St) = 7850 kg/m³: daten/wandelement.json /materialien/stahl_verzinkt/rho

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Bruttowandfläche**

$$
A_{\mathrm{b}} = L \cdot H
$$

$$
A_{\mathrm{b}} = 4800\ \mathrm{mm} \cdot 2750\ \mathrm{mm} = 13{,}200\ \mathrm{m^{2}}
$$

Ausdruck (maschinenlesbar): `L*H`

**Schritt 2: Öffnungsfläche Fenster F1**

$$
A_{\mathrm{F}} = b_{\mathrm{F}} \cdot h_{\mathrm{F}}
$$

$$
A_{\mathrm{F}} = 1260\ \mathrm{mm} \cdot 1385\ \mathrm{mm} = 1{,}7451\ \mathrm{m^{2}}
$$

Ausdruck (maschinenlesbar): `b_F*h_F`

**Schritt 3: Nettowandfläche**

$$
A_{\mathrm{n}} = A_{\mathrm{b}} - A_{\mathrm{F}}
$$

$$
A_{\mathrm{n}} = 13{,}200\ \mathrm{m^{2}} - 1{,}7451\ \mathrm{m^{2}} = 11{,}455\ \mathrm{m^{2}}
$$

Ausdruck (maschinenlesbar): `A_b - A_F`

**Schritt 4: Ansichtsfläche aller Hölzer**

Verfahren: Summe der 18 achsparallelen Holzrechtecke aus b1_wandelement.rahmenlayout; Überlappungsfreiheit per shapely-Vereinigung geprüft (Differenz < 1e-6 mm²)

Ergebnis: $A_{\mathrm{H}}$ = 2,5752 m²

**Schritt 5: Gefachfläche (Dämmung)**

$$
A_{\mathrm{G}} = A_{\mathrm{n}} - A_{\mathrm{H}}
$$

$$
A_{\mathrm{G}} = 11{,}455\ \mathrm{m^{2}} - 2{,}5752\ \mathrm{m^{2}} = 8{,}8797\ \mathrm{m^{2}}
$$

Ausdruck (maschinenlesbar): `A_n - A_H`

**Schritt 6: Volumen der Kerve K1**

$$
V_{\mathrm{K}} = b_{\mathrm{K}} \cdot t_{\mathrm{K}} \cdot h_{\mathrm{K}}
$$

$$
V_{\mathrm{K}} = 60\ \mathrm{mm} \cdot 25\ \mathrm{mm} \cdot 40\ \mathrm{mm} = 0{,}000060000\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `b_K*t_K*h_K`

**Schritt 7: Holzvolumen netto**

$$
V_{\mathrm{H}} = A_{\mathrm{H}} \cdot t_{\mathrm{H}} - V_{\mathrm{K}}
$$

$$
V_{\mathrm{H}} = 2{,}5752\ \mathrm{m^{2}} \cdot 200\ \mathrm{mm} - 0{,}000060000\ \mathrm{m^{3}} = 0{,}51498\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `A_H*t_H - V_K`

**Schritt 8: Volumen GKF** (Platten decken A_n vollständig)

$$
V_{\mathrm{GKF}} = A_{\mathrm{n}} \cdot d_{\mathrm{GKF}}
$$

$$
V_{\mathrm{GKF}} = 11{,}455\ \mathrm{m^{2}} \cdot 12{,}5\ \mathrm{mm} = 0{,}14319\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `A_n*d_GKF`

**Schritt 9: Volumen OSB/3**

$$
V_{\mathrm{OSB}} = A_{\mathrm{n}} \cdot d_{\mathrm{OSB}}
$$

$$
V_{\mathrm{OSB}} = 11{,}455\ \mathrm{m^{2}} \cdot 15\ \mathrm{mm} = 0{,}17182\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `A_n*d_OSB`

**Schritt 10: Volumen Holzfaserdämmplatte**

$$
V_{\mathrm{HFD}} = A_{\mathrm{n}} \cdot d_{\mathrm{HFD}}
$$

$$
V_{\mathrm{HFD}} = 11{,}455\ \mathrm{m^{2}} \cdot 60\ \mathrm{mm} = 0{,}68729\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `A_n*d_HFD`

**Schritt 11: Volumen Gefachdämmung**

$$
V_{\mathrm{D}} = A_{\mathrm{G}} \cdot d_{\mathrm{G}}
$$

$$
V_{\mathrm{D}} = 8{,}8797\ \mathrm{m^{2}} \cdot 200\ \mathrm{mm} = 1{,}7759\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `A_G*d_G`

**Schritt 12: Anzahl Schrauben (aus dem IFC-Modell)**

Verfahren: Zählung der IfcMechanicalFastener im Modell (Raster 150 mm, Randabstand 75 mm, Plattenrand ≥ 10 mm)

Ergebnis: $n_{\mathrm{S}}$ = 176 Stk

**Schritt 13: Masse Holz**

$$
m_{\mathrm{H}} = \rho_{\mathrm{kvh},\mathrm{c24}} \cdot V_{\mathrm{H}}
$$

$$
m_{\mathrm{H}} = 420\ \mathrm{kg/m^{3}} \cdot 0{,}51498\ \mathrm{m^{3}} = 216{,}29\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `rho_kvh_c24*V_H`

**Schritt 14: Masse GKF**

$$
m_{\mathrm{GKF}} = \rho_{\mathrm{gkf}} \cdot V_{\mathrm{GKF}}
$$

$$
m_{\mathrm{GKF}} = 800\ \mathrm{kg/m^{3}} \cdot 0{,}14319\ \mathrm{m^{3}} = 114{,}55\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `rho_gkf*V_GKF`

**Schritt 15: Masse OSB/3**

$$
m_{\mathrm{OSB}} = \rho_{\mathrm{osb3}} \cdot V_{\mathrm{OSB}}
$$

$$
m_{\mathrm{OSB}} = 600\ \mathrm{kg/m^{3}} \cdot 0{,}17182\ \mathrm{m^{3}} = 103{,}09\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `rho_osb3*V_OSB`

**Schritt 16: Masse Holzfaserdämmplatte**

$$
m_{\mathrm{HFD}} = \rho_{\mathrm{holzfaserplatte}} \cdot V_{\mathrm{HFD}}
$$

$$
m_{\mathrm{HFD}} = 180\ \mathrm{kg/m^{3}} \cdot 0{,}68729\ \mathrm{m^{3}} = 123{,}71\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `rho_holzfaserplatte*V_HFD`

**Schritt 17: Masse Gefachdämmung**

$$
m_{\mathrm{D}} = \rho_{\mathrm{holzfaser},\mathrm{flex}} \cdot V_{\mathrm{D}}
$$

$$
m_{\mathrm{D}} = 50\ \mathrm{kg/m^{3}} \cdot 1{,}7759\ \mathrm{m^{3}} = 88{,}797\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `rho_holzfaser_flex*V_D`

**Schritt 18: Masse Schrauben (Schaft als Zylinder, wie Modellgeometrie)**

$$
m_{\mathrm{S}} = n_{\mathrm{S}} \cdot \rho_{\mathrm{St}} \cdot \pi \cdot {\frac{d_{\mathrm{S}}}{2}}^{2} \cdot l_{\mathrm{S}}
$$

$$
m_{\mathrm{S}} = 176\ \mathrm{Stk} \cdot 7850\ \mathrm{kg/m^{3}} \cdot \pi \cdot {\frac{4\ \mathrm{mm}}{2}}^{2} \cdot 50\ \mathrm{mm} = 0{,}86808\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `n_S*rho_St*pi*(d_S/2)**2*l_S`

**Schritt 19: Gesamtmasse des Wandelements**

$$
m_{\mathrm{ges}} = m_{\mathrm{H}} + m_{\mathrm{GKF}} + m_{\mathrm{OSB}} + m_{\mathrm{HFD}} + m_{\mathrm{D}} + m_{\mathrm{S}}
$$

$$
m_{\mathrm{ges}} = 216{,}29\ \mathrm{kg} + 114{,}55\ \mathrm{kg} + 103{,}09\ \mathrm{kg} + 123{,}71\ \mathrm{kg} + 88{,}797\ \mathrm{kg} + 0{,}86808\ \mathrm{kg} = 647{,}31\ \mathrm{kg}
$$

Ausdruck (maschinenlesbar): `m_H + m_GKF + m_OSB + m_HFD + m_D + m_S`

**Schritt 20: flächenbezogene Masse**

$$
m_{\mathrm{A}} = \frac{m_{\mathrm{ges}}}{A_{\mathrm{n}}}
$$

$$
m_{\mathrm{A}} = \frac{647{,}31\ \mathrm{kg}}{11{,}455\ \mathrm{m^{2}}} = 56{,}510\ \mathrm{kg/m^{2}}
$$

Ausdruck (maschinenlesbar): `m_ges/A_n`

**Schritt 21: Holzvolumen laut IFC (Summe Qto_MemberBaseQuantities.NetVolume)**

Verfahren: Summe NetVolume über 18 IfcMember (GUIDs im Gegenstand)

Ergebnis: $V_{\mathrm{H},\mathrm{IFC}}$ = 0,51498 m³

**Schritt 22: Beplankungsvolumen laut IFC (Summe Qto_PlateBaseQuantities.NetVolume)**

Verfahren: Summe NetVolume über 10 IfcPlate

Ergebnis: $V_{\mathrm{P},\mathrm{IFC}}$ = 1,00230375 m³

**Schritt 23: Dämmvolumen laut IFC (Summe Qto_BodyGeometryValidation.NetVolume)**

Verfahren: Summe NetVolume über 12 IfcBuildingElementPart INSULATION

Ergebnis: $V_{\mathrm{D},\mathrm{IFC}}$ = 1,77594 m³

**Schritt 24: Abweichung Holzvolumen Nachweis/IFC**

$$
\mathrm{dV}_{\mathrm{H}} = \left|V_{\mathrm{H}} - V_{\mathrm{H},\mathrm{IFC}}\right|
$$

$$
\mathrm{dV}_{\mathrm{H}} = \left|0{,}51498\ \mathrm{m^{3}} - 0{,}51498\ \mathrm{m^{3}}\right| = 0{,}00000000000000011102\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `abs(V_H - V_H_IFC)`

**Schritt 25: Abweichung Beplankung Nachweis/IFC**

$$
\mathrm{dV}_{\mathrm{P}} = \left|V_{\mathrm{GKF}} + V_{\mathrm{OSB}} + V_{\mathrm{HFD}} - V_{\mathrm{P},\mathrm{IFC}}\right|
$$

$$
\mathrm{dV}_{\mathrm{P}} = \left|0{,}14319\ \mathrm{m^{3}} + 0{,}17182\ \mathrm{m^{3}} + 0{,}68729\ \mathrm{m^{3}} - 1{,}0023\ \mathrm{m^{3}}\right| = 0{,}00000000000000022204\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `abs(V_GKF + V_OSB + V_HFD - V_P_IFC)`

**Schritt 26: Abweichung Dämmung Nachweis/IFC**

$$
\mathrm{dV}_{\mathrm{D}} = \left|V_{\mathrm{D}} - V_{\mathrm{D},\mathrm{IFC}}\right|
$$

$$
\mathrm{dV}_{\mathrm{D}} = \left|1{,}7759\ \mathrm{m^{3}} - 1{,}7759\ \mathrm{m^{3}}\right| = 0{,}00000000000000044409\ \mathrm{m^{3}}
$$

Ausdruck (maschinenlesbar): `abs(V_D - V_D_IFC)`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Holzvolumen: Nachweis = IFC | 1,1102 · 10⁻¹⁶ m³ | ≤ | 1 · 10⁻⁸ m³ | 0,001 | erfüllt | Konsistenz Modell/IFC |
| Beplankung: Nachweis = IFC | 2,2204 · 10⁻¹⁶ m³ | ≤ | 1 · 10⁻⁸ m³ | 0,001 | erfüllt | Konsistenz Modell/IFC |
| Dämmung: Nachweis = IFC | 4,4409 · 10⁻¹⁶ m³ | ≤ | 1 · 10⁻⁸ m³ | 0,001 | erfüllt | Konsistenz Modell/IFC |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 3 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Massen für Transport- und Montageplanung; drei Stellen genügen.

### Messunsicherheit

Methode: lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette.

Ergebnis: **650 ± 70 kg (k = 2)**, kombinierte Standardunsicherheit u_c = 31 kg.

| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \|c\|·u | Anteil an u_c² |
|---|---:|---:|---|---:|---:|
| rho_kvh_c24 | 42 kg/m³ | 0,515 | (kg)/(kg/m³) | 22 | 49,9 % |
| rho_gkf | 40 kg/m³ | 0,143 | (kg)/(kg/m³) | 5,7 | 3,5 % |
| rho_osb3 | 60 kg/m³ | 0,172 | (kg)/(kg/m³) | 10 | 11,3 % |
| rho_holzfaser_flex | 7,5 kg/m³ | 1,78 | (kg)/(kg/m³) | 13 | 18,9 % |
| rho_holzfaserplatte | 18 kg/m³ | 0,687 | (kg)/(kg/m³) | 12 | 16,3 % |

Monte-Carlo (Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64); 50 000 Versuche, Seed 20260927): Mittelwert 647,4, s = 31, 95-%-Intervall [587,3; 707,1] kg.

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.
- Unsicherheitsbeiträge der Verfahrensschritte A_H, n_S, V_H_IFC, V_P_IFC, V_D_IFC sind nicht fortgepflanzt.

### Grafischer Nachweis

**Abbildung N-B1-01/ansicht: Wandansicht AW-01 von innen (Holzgerüst, Öffnung, Kerve)** (Maßstab 1:50)

![Wandansicht AW-01 von innen (Holzgerüst, Öffnung, Kerve)](svg/N-B1-01_ansicht.svg)

Bemaßung in mm. Hölzer schraffiert, Öffnung mit Kreuz, Kerve rot.

**Abbildung N-B1-01/massen: Massen je Bestandteil**

![Massen je Bestandteil](svg/N-B1-01_massen.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `3984bfb486b36ef8f82b34a4a028415fee791610c21254d31ce814a329987bfb`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-01"></a>

## N-B2-bestanden-HRB-01 – IDS HRB-01: Außenwand: U-Wert höchstens 0,20 W/(m²K) (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-01 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-01/anteil: HRB-01: Elemente mit und ohne Verstoß**

![HRB-01: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-01_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `6761c4520bc52f1bea4faae71dd71498ac2297ec4f665eb28c8d65cfc61b28a6`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-02"></a>

## N-B2-bestanden-HRB-02 – IDS HRB-02: Wand: Außen/Innen und Tragwirkung angegeben (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-02 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-02 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-02/anteil: HRB-02: Elemente mit und ohne Verstoß**

![HRB-02: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-02_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `1569a8eec950338fbf289e7649fdf0ac3b00aa981d97c009f0ca0dccfc5fc65b`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-03"></a>

## N-B2-bestanden-HRB-03 – IDS HRB-03: Wand: Klassifikation nach DIN 276 (KG 33x) (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-03 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-03 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-03/anteil: HRB-03: Elemente mit und ohne Verstoß**

![HRB-03: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-03_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `4d05e970d8fc2cea98acc8d37f54fced3e2ac9c65618efac2654cf74a6a8ac9e`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-04"></a>

## N-B2-bestanden-HRB-04 – IDS HRB-04: Wand: Material (Schichtaufbau) zugeordnet (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-04 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-04 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-04/anteil: HRB-04: Elemente mit und ohne Verstoß**

![HRB-04: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-04_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `e117934af800e935f1d43da9b6a8b09e9fc872ac65be405103cecd20cca0af3e`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-05"></a>

## N-B2-bestanden-HRB-05 – IDS HRB-05: Ständer: Material KVH C24 (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,067

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
| Anwendbarkeit (Kardinalität) | 15 Stk | ≥ | 1 Stk | 0,067 | erfüllt | holzrahmenbau.ids, HRB-05 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-05 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-05/anteil: HRB-05: Elemente mit und ohne Verstoß**

![HRB-05: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-05_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `d4dea59fe39f3eb8a5d081d18dbcb49652be17a0f9f71824c2b07ecd08cdd242`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-06"></a>

## N-B2-bestanden-HRB-06 – IDS HRB-06: Hölzer: Länge und Nettovolumen als Menge (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,056

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
| Anwendbarkeit (Kardinalität) | 18 Stk | ≥ | 1 Stk | 0,056 | erfüllt | holzrahmenbau.ids, HRB-06 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-06 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-06/anteil: HRB-06: Elemente mit und ohne Verstoß**

![HRB-06: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-06_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `1ad6cb8a87d3b6b98204a96d43db76635301864a987e43e31c1cb503bd4f37b0`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-07"></a>

## N-B2-bestanden-HRB-07 – IDS HRB-07: Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,025

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
| Anwendbarkeit (Kardinalität) | 41 Stk | ≥ | 1 Stk | 0,025 | erfüllt | holzrahmenbau.ids, HRB-07 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-07 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-07/anteil: HRB-07: Elemente mit und ohne Verstoß**

![HRB-07: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-07_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `88c4b7bae0f0d29cf5e4d8edc686d645e79521d5df65a23665524166a05f21dd`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-08"></a>

## N-B2-bestanden-HRB-08 – IDS HRB-08: Verbindungsmitteltyp: Nenndurchmesser und Nennlänge (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 1,000

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
| Anwendbarkeit (Kardinalität) | 1 Stk | ≥ | 1 Stk | 1,000 | erfüllt | holzrahmenbau.ids, HRB-08 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-08 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-08/anteil: HRB-08: Elemente mit und ohne Verstoß**

![HRB-08: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-08_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `3496ad701b0b304d057717c4d7cbdc909eacbd9c59299679422818020963032b`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-09"></a>

## N-B2-bestanden-HRB-09 – IDS HRB-09: Verbindungsmittel: Nenndurchmesser am Exemplar (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,006

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
| Anwendbarkeit (Kardinalität) | 176 Stk | ≥ | 1 Stk | 0,006 | erfüllt | holzrahmenbau.ids, HRB-09 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-09 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-09/anteil: HRB-09: Elemente mit und ohne Verstoß**

![HRB-09: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-09_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `94a1ed6f892c679b92d8d40ca9a9a8bf61f4599741d07a8e8971f1afec9e936f`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b2-bestanden-hrb-10"></a>

## N-B2-bestanden-HRB-10 – IDS HRB-10: Gefachdämmung: Dämmstoff zugeordnet (bestanden)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,084

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
| Anwendbarkeit (Kardinalität) | 12 Stk | ≥ | 1 Stk | 0,084 | erfüllt | holzrahmenbau.ids, HRB-10 |
| alle Anforderungen erfüllt | 0 Stk | ≤ | 0 Stk | – | erfüllt | holzrahmenbau.ids, HRB-10 |

Der Vergleich erfolgt mit ungerundeten Werten.

### Hinweise

- Der Nachweisstatus stimmt mit dem Status von ifctester überein (Gegenprüfung).

### Grafischer Nachweis

**Abbildung N-B2-bestanden-HRB-10/anteil: HRB-10: Elemente mit und ohne Verstoß**

![HRB-10: Elemente mit und ohne Verstoß](svg/N-B2-bestanden-HRB-10_anteil.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `014c8a9805edb4a75ae218a58e2721407ece6a71d8aa4f110c1fdc3508421047`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
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

- Hash (SHA-256): `68f2d76b3e98449d0504bafc4b4b27eee86326a29070963f0629ef5c245d5f9f`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b3-geometrie-verputzt"></a>

## N-B3-geometrie-verputzt – U-Wert Außenwand AW-01 (Holzanteil aus der Elementgeometrie, verputzt)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,934

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Außenwand AW-01, Typ AW-HRB-01, Variante geometrie/verputzt |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (aus B1) (`5a796ea7b0f1d8c0…`) |

### Regel

> Der Wärmedurchgangskoeffizient der Außenwand darf 0,20 W/(m²·K) nicht überschreiten. Berechnung nach dem vereinfachten Verfahren für Bauteile aus homogenen und inhomogenen Schichten (oberer und unterer Grenzwert).

Quelle: DIN EN ISO 6946:2018-03 (ISO 6946:2017); Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung) · Fassung: 2018-03 · Fundstelle: 6.5.2, 6.6, 6.7.1.1, 6.7.2, 6.8 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `DE-Waermeschutz-Beispiel` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Wärmeübergangswiderstand innen | $R_{\mathrm{si}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8, horizontaler Wärmestrom |
| Wärmeübergangswiderstand außen | $R_{\mathrm{se}}$ | 0,04 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8 (Fassade verputzt) |
| Dicke GKF | $d_{\mathrm{GKF}}$ | 12,5 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht gkf |
| Dicke OSB/3 | $d_{\mathrm{OSB}}$ | 15 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht osb |
| Dicke Gefach | $d_{\mathrm{G}}$ | 200 mm | 2 mm | eingabe | daten/wandelement.json Schicht gefach |
| Dicke Holzfaserdämmplatte | $d_{\mathrm{HFD}}$ | 60 mm | 1 mm | eingabe | daten/wandelement.json Schicht hfd |
| Bemessungswert λ GKF | $\lambda_{\mathrm{GKF}}$ | 0,25 W/(m·K) | 0,0075 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe (Beispielwert) |
| Bemessungswert λ OSB/3 | $\lambda_{\mathrm{OSB}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe / DIN EN 13986 (Beispielwert) |
| Bemessungswert λ Holz (KVH C24) | $\lambda_{\mathrm{H}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typischer Wert Nadelholz, vgl. DIN EN ISO 10456 (Beispielwert) |
| Bemessungswert λ Gefachdämmung | $\lambda_{\mathrm{D}}$ | 0,038 W/(m·K) | 0,00114 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Bemessungswert λ Holzfaserdämmplatte | $\lambda_{\mathrm{HFD}}$ | 0,043 W/(m·K) | 0,00129 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Ansichtsfläche aller Hölzer | $A_{\mathrm{H}}$ | 2 575 200 mm² | – | eingabe | b1_wandelement.rahmenlayout: Summe der Holzrechtecke |
| Nettowandfläche (ohne Öffnungen) | $A_{\mathrm{n}}$ | 11 454 900 mm² | – | eingabe | b1_wandelement.rahmenlayout: Wandfläche minus Öffnungen |
| Höchstwert des U-Werts | $U_{\mathrm{max}}$ | 0,20 W/(m²·K) | – | grenzwert | holzrahmenbau.ids, HRB-01 (Projektanforderung, Beispielwert) |

### Annahmen

- **Annahme:** Korrekturen ΔU nach Anhang F nicht angesetzt: Luftspalte Stufe 0 (Dämmung passgenau), Befestigungen durchdringen die Dämmschicht nicht (6.4 d: Korrektur nur bei > 3 % von U).
- **Annahme:** Die Dampfbremse (0,2 mm) ist thermisch vernachlässigt.
- **Annahme:** λ-Werte sind Beispielwerte aus dem Parametermodell, keine Tabellenwerte der DIN 4108-4.
- **Annahme:** Unsicherheiten der Dicken (Rechteckverteilung) und der λ-Werte (3 %, normal): Annahme zur Demonstration der Unsicherheitsfortpflanzung.

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Holzanteil aus der Elementgeometrie** (Flächenanteil Abschnitt a)

$$
f_{\mathrm{a}} = \frac{A_{\mathrm{H}}}{A_{\mathrm{n}}}
$$

$$
f_{\mathrm{a}} = \frac{2\,575\,200\ \mathrm{mm^{2}}}{11\,454\,900\ \mathrm{mm^{2}}} = 0{,}22481
$$

Ausdruck (maschinenlesbar): `A_H/A_n`

**Schritt 2: Wärmedurchlasswiderstand GKF** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.7.1.1, Formel (3))

$$
R_{\mathrm{GKF}} = \frac{d_{\mathrm{GKF}}}{\lambda_{\mathrm{GKF}}}
$$

$$
R_{\mathrm{GKF}} = \frac{12{,}5\ \mathrm{mm}}{0{,}25\ \mathrm{W/(m\cdot K)}} = 0{,}050000\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_GKF/lambda_GKF`

**Schritt 3: Wärmedurchlasswiderstand OSB/3** (6.7.1.1, Formel (3))

$$
R_{\mathrm{OSB}} = \frac{d_{\mathrm{OSB}}}{\lambda_{\mathrm{OSB}}}
$$

$$
R_{\mathrm{OSB}} = \frac{15\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 0{,}11538\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_OSB/lambda_OSB`

**Schritt 4: Wärmedurchlasswiderstand Holzfaserdämmplatte** (6.7.1.1, Formel (3))

$$
R_{\mathrm{HFD}} = \frac{d_{\mathrm{HFD}}}{\lambda_{\mathrm{HFD}}}
$$

$$
R_{\mathrm{HFD}} = \frac{60\ \mathrm{mm}}{0{,}043\ \mathrm{W/(m\cdot K)}} = 1{,}3953\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_HFD/lambda_HFD`

**Schritt 5: Gefachschicht, Abschnitt a (Holz)** (6.7.1.1)

$$
R_{\mathrm{Ga}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{H}}}
$$

$$
R_{\mathrm{Ga}} = \frac{200\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 1{,}5385\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_H`

**Schritt 6: Gefachschicht, Abschnitt b (Dämmung)** (6.7.1.1)

$$
R_{\mathrm{Gb}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{D}}}
$$

$$
R_{\mathrm{Gb}} = \frac{200\ \mathrm{mm}}{0{,}038\ \mathrm{W/(m\cdot K)}} = 5{,}2632\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_D`

**Schritt 7: Gesamtwiderstand Abschnitt a (innen bis außen)** (6.7.2 (oberer Grenzwert, Abschnittswiderstände))

$$
R_{\mathrm{T},a} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Ga}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},a} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 1{,}5385\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 3{,}2692\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Ga + R_HFD + R_se`

**Schritt 8: Gesamtwiderstand Abschnitt b** (6.7.2)

$$
R_{\mathrm{T},b} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Gb}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},b} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 5{,}2632\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 6{,}9939\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Gb + R_HFD + R_se`

**Schritt 9: Flächenanteil Abschnitt b**

$$
f_{\mathrm{b}} = 1 - f_{\mathrm{a}}
$$

$$
f_{\mathrm{b}} = 1 - 0{,}22481 = 0{,}77519
$$

Ausdruck (maschinenlesbar): `1 - f_a`

**Schritt 10: oberer Grenzwert R'_T (parallele Wärmeströme)** (6.7.2, oberer Grenzwert [Absatznummer U])

$$
R'_{\mathrm{T}} = \frac{1}{\frac{f_{\mathrm{a}}}{R_{\mathrm{T},a}} + \frac{f_{\mathrm{b}}}{R_{\mathrm{T},b}}}
$$

$$
R'_{\mathrm{T}} = \frac{1}{\frac{0{,}22481}{3{,}2692\ \mathrm{m^{2}\cdot K/W}} + \frac{0{,}77519}{6{,}9939\ \mathrm{m^{2}\cdot K/W}}} = 5{,}5678\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `1/(f_a/R_Ta + f_b/R_Tb)`

**Schritt 11: äquivalente Wärmeleitfähigkeit der Gefachschicht** (6.7.2, unterer Grenzwert)

$$
\lambda'' = f_{\mathrm{a}} \cdot \lambda_{\mathrm{H}} + f_{\mathrm{b}} \cdot \lambda_{\mathrm{D}}
$$

$$
\lambda'' = 0{,}22481 \cdot 0{,}13\ \mathrm{W/(m\cdot K)} + 0{,}77519 \cdot 0{,}038\ \mathrm{W/(m\cdot K)} = 0{,}058683\ \mathrm{W/(m\cdot K)}
$$

Ausdruck (maschinenlesbar): `f_a*lambda_H + f_b*lambda_D`

**Schritt 12: Wärmedurchlasswiderstand Gefach mit λ''** (6.7.2, unterer Grenzwert)

$$
R''_{\mathrm{G}} = \frac{d_{\mathrm{G}}}{\lambda''}
$$

$$
R''_{\mathrm{G}} = \frac{200\ \mathrm{mm}}{0{,}058683\ \mathrm{W/(m\cdot K)}} = 3{,}4082\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_eq`

**Schritt 13: unterer Grenzwert R''_T (isotherme Ebenen)** (6.7.2, unterer Grenzwert [Absatznummer U])

$$
R''_{\mathrm{T}} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R''_{\mathrm{G}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R''_{\mathrm{T}} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 3{,}4082\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 5{,}1389\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Geq + R_HFD + R_se`

**Schritt 14: Wärmedurchgangswiderstand als arithmetisches Mittel** (6.7.2.2 [V])

$$
R_{\mathrm{T}} = \frac{R'_{\mathrm{T}} + R''_{\mathrm{T}}}{2}
$$

$$
R_{\mathrm{T}} = \frac{5{,}5678\ \mathrm{m^{2}\cdot K/W} + 5{,}1389\ \mathrm{m^{2}\cdot K/W}}{2} = 5{,}3533\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `(R_o + R_u)/2`

**Schritt 15: maximaler relativer Fehler** (6.7.2, Abschätzung des Fehlers)

$$
e_{\mathrm{rel}} = \frac{R'_{\mathrm{T}} - R''_{\mathrm{T}}}{2 \cdot R_{\mathrm{T}}}
$$

$$
e_{\mathrm{rel}} = \frac{5{,}5678\ \mathrm{m^{2}\cdot K/W} - 5{,}1389\ \mathrm{m^{2}\cdot K/W}}{2 \cdot 5{,}3533\ \mathrm{m^{2}\cdot K/W}} = 4{,}0058\ \mathrm{\%}
$$

Ausdruck (maschinenlesbar): `(R_o - R_u)/(2*R_T)`

**Schritt 16: Wärmedurchgangskoeffizient** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2, Formel (1))

$$
U = \frac{1}{R_{\mathrm{T}}}
$$

$$
U = \frac{1}{5{,}3533\ \mathrm{m^{2}\cdot K/W}} = 0{,}18680\ \mathrm{W/(m^{2}\cdot K)}
$$

Ausdruck (maschinenlesbar): `1/R_T`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| U ≤ U_max | 0,19 W/(m²·K) | ≤ | 0,20 W/(m²·K) | 0,934 | erfüllt | holzrahmenbau.ids HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 2 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2: Endergebnis auf zwei signifikante Stellen [V].

### Messunsicherheit

Methode: lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette.

Ergebnis: **0,187 ± 0,007 W/(m²·K) (k = 2)**, kombinierte Standardunsicherheit u_c = 0,0034 W/(m²·K).

| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \|c\|·u | Anteil an u_c² |
|---|---:|---:|---|---:|---:|
| d_GKF | 0,3 mm | −0,000150 | (W/(m²·K))/(mm) | 0,000045 | 0,0 % |
| d_OSB | 0,3 mm | −0,000288 | (W/(m²·K))/(mm) | 0,000086 | 0,1 % |
| d_G | 2 mm | −0,000610 | (W/(m²·K))/(mm) | 0,0012 | 12,6 % |
| d_HFD | 1 mm | −0,000870 | (W/(m²·K))/(mm) | 0,00087 | 6,4 % |
| lambda_GKF | 0,0075 W/(m·K) | 0,00748 | (W/(m²·K))/(W/(m·K)) | 0,000056 | 0,0 % |
| lambda_OSB | 0,0039 W/(m·K) | 0,0332 | (W/(m²·K))/(W/(m·K)) | 0,00013 | 0,1 % |
| lambda_H | 0,0039 W/(m·K) | 0,362 | (W/(m²·K))/(W/(m·K)) | 0,0014 | 17,0 % |
| lambda_D | 0,00114 W/(m·K) | 1,97 | (W/(m²·K))/(W/(m·K)) | 0,0022 | 42,9 % |
| lambda_HFD | 0,00129 W/(m·K) | 1,21 | (W/(m²·K))/(W/(m·K)) | 0,0016 | 20,8 % |

Monte-Carlo (Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64); 100 000 Versuche, Seed 20260927): Mittelwert 0,1867, s = 0,0034, 95-%-Intervall [0,1801; 0,1935] W/(m²·K).

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| U | `b3_uwert_iso6946.berechne_uwert → u_wert (6 Dezimalstellen)` = 0,186799 | 0,18679932937799024 | 3,3 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_o | `b3_uwert_iso6946.berechne_uwert → r_oben` = 5,567784 | 5,567784334633171 | 3,3 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_u | `b3_uwert_iso6946.berechne_uwert → r_unten` = 5,138892 | 5,138892218541071 | 2,2 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| U | `IFC Pset_WallCommon.ThermalTransmittance (3 Dezimalstellen)` = 0,187 | 0,18679932937799024 | 2,0 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.
- Im IFC-Modell (Pset_WallCommon.ThermalTransmittance) steht der U-Wert mit drei Dezimalstellen. Das ist ein Zwischenwert für Folgerechnungen (vgl. JCGM 100:2008, 7.2.6); als Endergebnis gilt die Angabe mit zwei signifikanten Stellen.

### Grafischer Nachweis

**Abbildung N-B3-geometrie-verputzt/schnitt: Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)** (Maßstab 1:5)

![Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)](svg/N-B3-geometrie-verputzt_schnitt.svg)

Abschnitt a = Holz (Ständer), Abschnitt b = Dämmung. Maße in mm.

**Abbildung N-B3-geometrie-verputzt/grenzwerte: Grenzwerte des Wärmedurchgangswiderstands**

![Grenzwerte des Wärmedurchgangswiderstands](svg/N-B3-geometrie-verputzt_grenzwerte.svg)

**Abbildung N-B3-geometrie-verputzt/uwert: U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)**

![U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)](svg/N-B3-geometrie-verputzt_uwert.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `46b1a54c5c98f27ee4029c5ebdf124c1b682f70f88fc2bd5c5dab6bfa35c3bd1`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b3-geometrie-hinterlueftet"></a>

## N-B3-geometrie-hinterlueftet – U-Wert Außenwand AW-01 (Holzanteil aus der Elementgeometrie, hinterlueftet)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,918

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Außenwand AW-01, Typ AW-HRB-01, Variante geometrie/hinterlueftet |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (aus B1) (`5a796ea7b0f1d8c0…`) |

### Regel

> Der Wärmedurchgangskoeffizient der Außenwand darf 0,20 W/(m²·K) nicht überschreiten. Berechnung nach dem vereinfachten Verfahren für Bauteile aus homogenen und inhomogenen Schichten (oberer und unterer Grenzwert).

Quelle: DIN EN ISO 6946:2018-03 (ISO 6946:2017); Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung) · Fassung: 2018-03 · Fundstelle: 6.5.2, 6.6, 6.7.1.1, 6.7.2, 6.8 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `DE-Waermeschutz-Beispiel` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Wärmeübergangswiderstand innen | $R_{\mathrm{si}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8, horizontaler Wärmestrom |
| Wärmeübergangswiderstand außen | $R_{\mathrm{se}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8; stark belüftete Luftschicht: R_se = R_si (6.9.4) |
| Dicke GKF | $d_{\mathrm{GKF}}$ | 12,5 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht gkf |
| Dicke OSB/3 | $d_{\mathrm{OSB}}$ | 15 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht osb |
| Dicke Gefach | $d_{\mathrm{G}}$ | 200 mm | 2 mm | eingabe | daten/wandelement.json Schicht gefach |
| Dicke Holzfaserdämmplatte | $d_{\mathrm{HFD}}$ | 60 mm | 1 mm | eingabe | daten/wandelement.json Schicht hfd |
| Bemessungswert λ GKF | $\lambda_{\mathrm{GKF}}$ | 0,25 W/(m·K) | 0,0075 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe (Beispielwert) |
| Bemessungswert λ OSB/3 | $\lambda_{\mathrm{OSB}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe / DIN EN 13986 (Beispielwert) |
| Bemessungswert λ Holz (KVH C24) | $\lambda_{\mathrm{H}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typischer Wert Nadelholz, vgl. DIN EN ISO 10456 (Beispielwert) |
| Bemessungswert λ Gefachdämmung | $\lambda_{\mathrm{D}}$ | 0,038 W/(m·K) | 0,00114 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Bemessungswert λ Holzfaserdämmplatte | $\lambda_{\mathrm{HFD}}$ | 0,043 W/(m·K) | 0,00129 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Ansichtsfläche aller Hölzer | $A_{\mathrm{H}}$ | 2 575 200 mm² | – | eingabe | b1_wandelement.rahmenlayout: Summe der Holzrechtecke |
| Nettowandfläche (ohne Öffnungen) | $A_{\mathrm{n}}$ | 11 454 900 mm² | – | eingabe | b1_wandelement.rahmenlayout: Wandfläche minus Öffnungen |
| Höchstwert des U-Werts | $U_{\mathrm{max}}$ | 0,20 W/(m²·K) | – | grenzwert | holzrahmenbau.ids, HRB-01 (Projektanforderung, Beispielwert) |

### Annahmen

- **Annahme:** Korrekturen ΔU nach Anhang F nicht angesetzt: Luftspalte Stufe 0 (Dämmung passgenau), Befestigungen durchdringen die Dämmschicht nicht (6.4 d: Korrektur nur bei > 3 % von U).
- **Annahme:** Die Dampfbremse (0,2 mm) ist thermisch vernachlässigt.
- **Annahme:** λ-Werte sind Beispielwerte aus dem Parametermodell, keine Tabellenwerte der DIN 4108-4.
- **Annahme:** Unsicherheiten der Dicken (Rechteckverteilung) und der λ-Werte (3 %, normal): Annahme zur Demonstration der Unsicherheitsfortpflanzung.

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Holzanteil aus der Elementgeometrie** (Flächenanteil Abschnitt a)

$$
f_{\mathrm{a}} = \frac{A_{\mathrm{H}}}{A_{\mathrm{n}}}
$$

$$
f_{\mathrm{a}} = \frac{2\,575\,200\ \mathrm{mm^{2}}}{11\,454\,900\ \mathrm{mm^{2}}} = 0{,}22481
$$

Ausdruck (maschinenlesbar): `A_H/A_n`

**Schritt 2: Wärmedurchlasswiderstand GKF** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.7.1.1, Formel (3))

$$
R_{\mathrm{GKF}} = \frac{d_{\mathrm{GKF}}}{\lambda_{\mathrm{GKF}}}
$$

$$
R_{\mathrm{GKF}} = \frac{12{,}5\ \mathrm{mm}}{0{,}25\ \mathrm{W/(m\cdot K)}} = 0{,}050000\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_GKF/lambda_GKF`

**Schritt 3: Wärmedurchlasswiderstand OSB/3** (6.7.1.1, Formel (3))

$$
R_{\mathrm{OSB}} = \frac{d_{\mathrm{OSB}}}{\lambda_{\mathrm{OSB}}}
$$

$$
R_{\mathrm{OSB}} = \frac{15\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 0{,}11538\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_OSB/lambda_OSB`

**Schritt 4: Wärmedurchlasswiderstand Holzfaserdämmplatte** (6.7.1.1, Formel (3))

$$
R_{\mathrm{HFD}} = \frac{d_{\mathrm{HFD}}}{\lambda_{\mathrm{HFD}}}
$$

$$
R_{\mathrm{HFD}} = \frac{60\ \mathrm{mm}}{0{,}043\ \mathrm{W/(m\cdot K)}} = 1{,}3953\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_HFD/lambda_HFD`

**Schritt 5: Gefachschicht, Abschnitt a (Holz)** (6.7.1.1)

$$
R_{\mathrm{Ga}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{H}}}
$$

$$
R_{\mathrm{Ga}} = \frac{200\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 1{,}5385\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_H`

**Schritt 6: Gefachschicht, Abschnitt b (Dämmung)** (6.7.1.1)

$$
R_{\mathrm{Gb}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{D}}}
$$

$$
R_{\mathrm{Gb}} = \frac{200\ \mathrm{mm}}{0{,}038\ \mathrm{W/(m\cdot K)}} = 5{,}2632\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_D`

**Schritt 7: Gesamtwiderstand Abschnitt a (innen bis außen)** (6.7.2 (oberer Grenzwert, Abschnittswiderstände))

$$
R_{\mathrm{T},a} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Ga}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},a} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 1{,}5385\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 3{,}3592\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Ga + R_HFD + R_se`

**Schritt 8: Gesamtwiderstand Abschnitt b** (6.7.2)

$$
R_{\mathrm{T},b} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Gb}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},b} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 5{,}2632\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 7{,}0839\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Gb + R_HFD + R_se`

**Schritt 9: Flächenanteil Abschnitt b**

$$
f_{\mathrm{b}} = 1 - f_{\mathrm{a}}
$$

$$
f_{\mathrm{b}} = 1 - 0{,}22481 = 0{,}77519
$$

Ausdruck (maschinenlesbar): `1 - f_a`

**Schritt 10: oberer Grenzwert R'_T (parallele Wärmeströme)** (6.7.2, oberer Grenzwert [Absatznummer U])

$$
R'_{\mathrm{T}} = \frac{1}{\frac{f_{\mathrm{a}}}{R_{\mathrm{T},a}} + \frac{f_{\mathrm{b}}}{R_{\mathrm{T},b}}}
$$

$$
R'_{\mathrm{T}} = \frac{1}{\frac{0{,}22481}{3{,}3592\ \mathrm{m^{2}\cdot K/W}} + \frac{0{,}77519}{7{,}0839\ \mathrm{m^{2}\cdot K/W}}} = 5{,}6704\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `1/(f_a/R_Ta + f_b/R_Tb)`

**Schritt 11: äquivalente Wärmeleitfähigkeit der Gefachschicht** (6.7.2, unterer Grenzwert)

$$
\lambda'' = f_{\mathrm{a}} \cdot \lambda_{\mathrm{H}} + f_{\mathrm{b}} \cdot \lambda_{\mathrm{D}}
$$

$$
\lambda'' = 0{,}22481 \cdot 0{,}13\ \mathrm{W/(m\cdot K)} + 0{,}77519 \cdot 0{,}038\ \mathrm{W/(m\cdot K)} = 0{,}058683\ \mathrm{W/(m\cdot K)}
$$

Ausdruck (maschinenlesbar): `f_a*lambda_H + f_b*lambda_D`

**Schritt 12: Wärmedurchlasswiderstand Gefach mit λ''** (6.7.2, unterer Grenzwert)

$$
R''_{\mathrm{G}} = \frac{d_{\mathrm{G}}}{\lambda''}
$$

$$
R''_{\mathrm{G}} = \frac{200\ \mathrm{mm}}{0{,}058683\ \mathrm{W/(m\cdot K)}} = 3{,}4082\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_eq`

**Schritt 13: unterer Grenzwert R''_T (isotherme Ebenen)** (6.7.2, unterer Grenzwert [Absatznummer U])

$$
R''_{\mathrm{T}} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R''_{\mathrm{G}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R''_{\mathrm{T}} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 3{,}4082\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 5{,}2289\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Geq + R_HFD + R_se`

**Schritt 14: Wärmedurchgangswiderstand als arithmetisches Mittel** (6.7.2.2 [V])

$$
R_{\mathrm{T}} = \frac{R'_{\mathrm{T}} + R''_{\mathrm{T}}}{2}
$$

$$
R_{\mathrm{T}} = \frac{5{,}6704\ \mathrm{m^{2}\cdot K/W} + 5{,}2289\ \mathrm{m^{2}\cdot K/W}}{2} = 5{,}4497\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `(R_o + R_u)/2`

**Schritt 15: maximaler relativer Fehler** (6.7.2, Abschätzung des Fehlers)

$$
e_{\mathrm{rel}} = \frac{R'_{\mathrm{T}} - R''_{\mathrm{T}}}{2 \cdot R_{\mathrm{T}}}
$$

$$
e_{\mathrm{rel}} = \frac{5{,}6704\ \mathrm{m^{2}\cdot K/W} - 5{,}2289\ \mathrm{m^{2}\cdot K/W}}{2 \cdot 5{,}4497\ \mathrm{m^{2}\cdot K/W}} = 4{,}0509\ \mathrm{\%}
$$

Ausdruck (maschinenlesbar): `(R_o - R_u)/(2*R_T)`

**Schritt 16: Wärmedurchgangskoeffizient** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2, Formel (1))

$$
U = \frac{1}{R_{\mathrm{T}}}
$$

$$
U = \frac{1}{5{,}4497\ \mathrm{m^{2}\cdot K/W}} = 0{,}18350\ \mathrm{W/(m^{2}\cdot K)}
$$

Ausdruck (maschinenlesbar): `1/R_T`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| U ≤ U_max | 0,18 W/(m²·K) | ≤ | 0,20 W/(m²·K) | 0,918 | erfüllt | holzrahmenbau.ids HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 2 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2: Endergebnis auf zwei signifikante Stellen [V].

### Messunsicherheit

Methode: lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette.

Ergebnis: **0,183 ± 0,007 W/(m²·K) (k = 2)**, kombinierte Standardunsicherheit u_c = 0,0033 W/(m²·K).

| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \|c\|·u | Anteil an u_c² |
|---|---:|---:|---|---:|---:|
| d_GKF | 0,3 mm | −0,000144 | (W/(m²·K))/(mm) | 0,000043 | 0,0 % |
| d_OSB | 0,3 mm | −0,000277 | (W/(m²·K))/(mm) | 0,000083 | 0,1 % |
| d_G | 2 mm | −0,000590 | (W/(m²·K))/(mm) | 0,0012 | 12,7 % |
| d_HFD | 1 mm | −0,000837 | (W/(m²·K))/(mm) | 0,00084 | 6,4 % |
| lambda_GKF | 0,0075 W/(m·K) | 0,00720 | (W/(m²·K))/(W/(m·K)) | 0,000054 | 0,0 % |
| lambda_OSB | 0,0039 W/(m·K) | 0,0319 | (W/(m²·K))/(W/(m·K)) | 0,00012 | 0,1 % |
| lambda_H | 0,0039 W/(m·K) | 0,347 | (W/(m²·K))/(W/(m·K)) | 0,0014 | 16,7 % |
| lambda_D | 0,00114 W/(m·K) | 1,92 | (W/(m²·K))/(W/(m·K)) | 0,0022 | 43,4 % |
| lambda_HFD | 0,00129 W/(m·K) | 1,17 | (W/(m²·K))/(W/(m·K)) | 0,0015 | 20,6 % |

Monte-Carlo (Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64); 100 000 Versuche, Seed 20260927): Mittelwert 0,1834, s = 0,0033, 95-%-Intervall [0,1770; 0,1900] W/(m²·K).

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| U | `b3_uwert_iso6946.berechne_uwert → u_wert (6 Dezimalstellen)` = 0,183498 | 0,18349797236470997 | 2,8 · 10⁻⁸ | ja (Toleranz 5 · 10⁻⁷) |
| R_o | `b3_uwert_iso6946.berechne_uwert → r_oben` = 5,670411 | 5,670410777706296 | 2,2 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_u | `b3_uwert_iso6946.berechne_uwert → r_unten` = 5,228892 | 5,228892218541071 | 2,2 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.
- Im IFC-Modell (Pset_WallCommon.ThermalTransmittance) steht der U-Wert mit drei Dezimalstellen. Das ist ein Zwischenwert für Folgerechnungen (vgl. JCGM 100:2008, 7.2.6); als Endergebnis gilt die Angabe mit zwei signifikanten Stellen.

### Grafischer Nachweis

**Abbildung N-B3-geometrie-hinterlueftet/schnitt: Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)** (Maßstab 1:5)

![Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)](svg/N-B3-geometrie-hinterlueftet_schnitt.svg)

Abschnitt a = Holz (Ständer), Abschnitt b = Dämmung. Maße in mm.

**Abbildung N-B3-geometrie-hinterlueftet/grenzwerte: Grenzwerte des Wärmedurchgangswiderstands**

![Grenzwerte des Wärmedurchgangswiderstands](svg/N-B3-geometrie-hinterlueftet_grenzwerte.svg)

**Abbildung N-B3-geometrie-hinterlueftet/uwert: U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)**

![U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)](svg/N-B3-geometrie-hinterlueftet_uwert.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `8a2c26bee9cd9276c43f328a5a12e03e06932a9952445521a5593a5d43056cb3`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b3-raster-verputzt"></a>

## N-B3-raster-verputzt – U-Wert Außenwand AW-01 (Holzanteil aus dem Raster, verputzt)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,813

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Außenwand AW-01, Typ AW-HRB-01, Variante raster/verputzt |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (aus B1) (`5a796ea7b0f1d8c0…`) |

### Regel

> Der Wärmedurchgangskoeffizient der Außenwand darf 0,20 W/(m²·K) nicht überschreiten. Berechnung nach dem vereinfachten Verfahren für Bauteile aus homogenen und inhomogenen Schichten (oberer und unterer Grenzwert).

Quelle: DIN EN ISO 6946:2018-03 (ISO 6946:2017); Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung) · Fassung: 2018-03 · Fundstelle: 6.5.2, 6.6, 6.7.1.1, 6.7.2, 6.8 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `DE-Waermeschutz-Beispiel` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Wärmeübergangswiderstand innen | $R_{\mathrm{si}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8, horizontaler Wärmestrom |
| Wärmeübergangswiderstand außen | $R_{\mathrm{se}}$ | 0,04 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8 (Fassade verputzt) |
| Dicke GKF | $d_{\mathrm{GKF}}$ | 12,5 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht gkf |
| Dicke OSB/3 | $d_{\mathrm{OSB}}$ | 15 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht osb |
| Dicke Gefach | $d_{\mathrm{G}}$ | 200 mm | 2 mm | eingabe | daten/wandelement.json Schicht gefach |
| Dicke Holzfaserdämmplatte | $d_{\mathrm{HFD}}$ | 60 mm | 1 mm | eingabe | daten/wandelement.json Schicht hfd |
| Bemessungswert λ GKF | $\lambda_{\mathrm{GKF}}$ | 0,25 W/(m·K) | 0,0075 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe (Beispielwert) |
| Bemessungswert λ OSB/3 | $\lambda_{\mathrm{OSB}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe / DIN EN 13986 (Beispielwert) |
| Bemessungswert λ Holz (KVH C24) | $\lambda_{\mathrm{H}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typischer Wert Nadelholz, vgl. DIN EN ISO 10456 (Beispielwert) |
| Bemessungswert λ Gefachdämmung | $\lambda_{\mathrm{D}}$ | 0,038 W/(m·K) | 0,00114 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Bemessungswert λ Holzfaserdämmplatte | $\lambda_{\mathrm{HFD}}$ | 0,043 W/(m·K) | 0,00129 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Ständerbreite | $b_{\mathrm{St}}$ | 60 mm | – | eingabe | daten/wandelement.json /wand/staender/breite |
| Achsmaß der Ständer | $e_{\mathrm{St}}$ | 625 mm | – | eingabe | daten/wandelement.json /wand/staender/raster |
| Höchstwert des U-Werts | $U_{\mathrm{max}}$ | 0,20 W/(m²·K) | – | grenzwert | holzrahmenbau.ids, HRB-01 (Projektanforderung, Beispielwert) |

### Annahmen

- **Annahme:** Korrekturen ΔU nach Anhang F nicht angesetzt: Luftspalte Stufe 0 (Dämmung passgenau), Befestigungen durchdringen die Dämmschicht nicht (6.4 d: Korrektur nur bei > 3 % von U).
- **Annahme:** Die Dampfbremse (0,2 mm) ist thermisch vernachlässigt.
- **Annahme:** λ-Werte sind Beispielwerte aus dem Parametermodell, keine Tabellenwerte der DIN 4108-4.
- **Annahme:** Unsicherheiten der Dicken (Rechteckverteilung) und der λ-Werte (3 %, normal): Annahme zur Demonstration der Unsicherheitsfortpflanzung.

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Holzanteil aus dem Raster** (Flächenanteil Abschnitt a)

$$
f_{\mathrm{a}} = \frac{b_{\mathrm{St}}}{e_{\mathrm{St}}}
$$

$$
f_{\mathrm{a}} = \frac{60\ \mathrm{mm}}{625\ \mathrm{mm}} = 0{,}096000
$$

Ausdruck (maschinenlesbar): `b_St/e_St`

**Schritt 2: Wärmedurchlasswiderstand GKF** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.7.1.1, Formel (3))

$$
R_{\mathrm{GKF}} = \frac{d_{\mathrm{GKF}}}{\lambda_{\mathrm{GKF}}}
$$

$$
R_{\mathrm{GKF}} = \frac{12{,}5\ \mathrm{mm}}{0{,}25\ \mathrm{W/(m\cdot K)}} = 0{,}050000\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_GKF/lambda_GKF`

**Schritt 3: Wärmedurchlasswiderstand OSB/3** (6.7.1.1, Formel (3))

$$
R_{\mathrm{OSB}} = \frac{d_{\mathrm{OSB}}}{\lambda_{\mathrm{OSB}}}
$$

$$
R_{\mathrm{OSB}} = \frac{15\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 0{,}11538\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_OSB/lambda_OSB`

**Schritt 4: Wärmedurchlasswiderstand Holzfaserdämmplatte** (6.7.1.1, Formel (3))

$$
R_{\mathrm{HFD}} = \frac{d_{\mathrm{HFD}}}{\lambda_{\mathrm{HFD}}}
$$

$$
R_{\mathrm{HFD}} = \frac{60\ \mathrm{mm}}{0{,}043\ \mathrm{W/(m\cdot K)}} = 1{,}3953\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_HFD/lambda_HFD`

**Schritt 5: Gefachschicht, Abschnitt a (Holz)** (6.7.1.1)

$$
R_{\mathrm{Ga}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{H}}}
$$

$$
R_{\mathrm{Ga}} = \frac{200\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 1{,}5385\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_H`

**Schritt 6: Gefachschicht, Abschnitt b (Dämmung)** (6.7.1.1)

$$
R_{\mathrm{Gb}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{D}}}
$$

$$
R_{\mathrm{Gb}} = \frac{200\ \mathrm{mm}}{0{,}038\ \mathrm{W/(m\cdot K)}} = 5{,}2632\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_D`

**Schritt 7: Gesamtwiderstand Abschnitt a (innen bis außen)** (6.7.2 (oberer Grenzwert, Abschnittswiderstände))

$$
R_{\mathrm{T},a} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Ga}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},a} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 1{,}5385\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 3{,}2692\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Ga + R_HFD + R_se`

**Schritt 8: Gesamtwiderstand Abschnitt b** (6.7.2)

$$
R_{\mathrm{T},b} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Gb}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},b} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 5{,}2632\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 6{,}9939\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Gb + R_HFD + R_se`

**Schritt 9: Flächenanteil Abschnitt b**

$$
f_{\mathrm{b}} = 1 - f_{\mathrm{a}}
$$

$$
f_{\mathrm{b}} = 1 - 0{,}096000 = 0{,}90400
$$

Ausdruck (maschinenlesbar): `1 - f_a`

**Schritt 10: oberer Grenzwert R'_T (parallele Wärmeströme)** (6.7.2, oberer Grenzwert [Absatznummer U])

$$
R'_{\mathrm{T}} = \frac{1}{\frac{f_{\mathrm{a}}}{R_{\mathrm{T},a}} + \frac{f_{\mathrm{b}}}{R_{\mathrm{T},b}}}
$$

$$
R'_{\mathrm{T}} = \frac{1}{\frac{0{,}096000}{3{,}2692\ \mathrm{m^{2}\cdot K/W}} + \frac{0{,}90400}{6{,}9939\ \mathrm{m^{2}\cdot K/W}}} = 6{,}3043\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `1/(f_a/R_Ta + f_b/R_Tb)`

**Schritt 11: äquivalente Wärmeleitfähigkeit der Gefachschicht** (6.7.2, unterer Grenzwert)

$$
\lambda'' = f_{\mathrm{a}} \cdot \lambda_{\mathrm{H}} + f_{\mathrm{b}} \cdot \lambda_{\mathrm{D}}
$$

$$
\lambda'' = 0{,}096000 \cdot 0{,}13\ \mathrm{W/(m\cdot K)} + 0{,}90400 \cdot 0{,}038\ \mathrm{W/(m\cdot K)} = 0{,}046832\ \mathrm{W/(m\cdot K)}
$$

Ausdruck (maschinenlesbar): `f_a*lambda_H + f_b*lambda_D`

**Schritt 12: Wärmedurchlasswiderstand Gefach mit λ''** (6.7.2, unterer Grenzwert)

$$
R''_{\mathrm{G}} = \frac{d_{\mathrm{G}}}{\lambda''}
$$

$$
R''_{\mathrm{G}} = \frac{200\ \mathrm{mm}}{0{,}046832\ \mathrm{W/(m\cdot K)}} = 4{,}2706\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_eq`

**Schritt 13: unterer Grenzwert R''_T (isotherme Ebenen)** (6.7.2, unterer Grenzwert [Absatznummer U])

$$
R''_{\mathrm{T}} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R''_{\mathrm{G}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R''_{\mathrm{T}} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 4{,}2706\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}04\ \mathrm{m^{2}\cdot K/W} = 6{,}0013\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Geq + R_HFD + R_se`

**Schritt 14: Wärmedurchgangswiderstand als arithmetisches Mittel** (6.7.2.2 [V])

$$
R_{\mathrm{T}} = \frac{R'_{\mathrm{T}} + R''_{\mathrm{T}}}{2}
$$

$$
R_{\mathrm{T}} = \frac{6{,}3043\ \mathrm{m^{2}\cdot K/W} + 6{,}0013\ \mathrm{m^{2}\cdot K/W}}{2} = 6{,}1528\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `(R_o + R_u)/2`

**Schritt 15: maximaler relativer Fehler** (6.7.2, Abschätzung des Fehlers)

$$
e_{\mathrm{rel}} = \frac{R'_{\mathrm{T}} - R''_{\mathrm{T}}}{2 \cdot R_{\mathrm{T}}}
$$

$$
e_{\mathrm{rel}} = \frac{6{,}3043\ \mathrm{m^{2}\cdot K/W} - 6{,}0013\ \mathrm{m^{2}\cdot K/W}}{2 \cdot 6{,}1528\ \mathrm{m^{2}\cdot K/W}} = 2{,}4625\ \mathrm{\%}
$$

Ausdruck (maschinenlesbar): `(R_o - R_u)/(2*R_T)`

**Schritt 16: Wärmedurchgangskoeffizient** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2, Formel (1))

$$
U = \frac{1}{R_{\mathrm{T}}}
$$

$$
U = \frac{1}{6{,}1528\ \mathrm{m^{2}\cdot K/W}} = 0{,}16253\ \mathrm{W/(m^{2}\cdot K)}
$$

Ausdruck (maschinenlesbar): `1/R_T`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| U ≤ U_max | 0,16 W/(m²·K) | ≤ | 0,20 W/(m²·K) | 0,813 | erfüllt | holzrahmenbau.ids HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 2 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2: Endergebnis auf zwei signifikante Stellen [V].

### Messunsicherheit

Methode: lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette.

Ergebnis: **0,163 ± 0,007 W/(m²·K) (k = 2)**, kombinierte Standardunsicherheit u_c = 0,0033 W/(m²·K).

| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \|c\|·u | Anteil an u_c² |
|---|---:|---:|---|---:|---:|
| d_GKF | 0,3 mm | −0,000110 | (W/(m²·K))/(mm) | 0,000033 | 0,0 % |
| d_OSB | 0,3 mm | −0,000212 | (W/(m²·K))/(mm) | 0,000064 | 0,0 % |
| d_G | 2 mm | −0,000574 | (W/(m²·K))/(mm) | 0,0011 | 11,7 % |
| d_HFD | 1 mm | −0,000642 | (W/(m²·K))/(mm) | 0,00064 | 3,7 % |
| lambda_GKF | 0,0075 W/(m·K) | 0,00552 | (W/(m²·K))/(W/(m·K)) | 0,000041 | 0,0 % |
| lambda_OSB | 0,0039 W/(m·K) | 0,0245 | (W/(m²·K))/(W/(m·K)) | 0,000096 | 0,1 % |
| lambda_H | 0,0039 W/(m·K) | 0,171 | (W/(m²·K))/(W/(m·K)) | 0,00067 | 4,0 % |
| lambda_D | 0,00114 W/(m·K) | 2,43 | (W/(m²·K))/(W/(m·K)) | 0,0028 | 68,5 % |
| lambda_HFD | 0,00129 W/(m·K) | 0,896 | (W/(m²·K))/(W/(m·K)) | 0,0012 | 11,9 % |

Monte-Carlo (Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64); 100 000 Versuche, Seed 20260927): Mittelwert 0,1625, s = 0,0034, 95-%-Intervall [0,1559; 0,1691] W/(m²·K).

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| U | `b3_uwert_iso6946.berechne_uwert → u_wert (6 Dezimalstellen)` = 0,162527 | 0,1625267602545588 | 2,4 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_o | `b3_uwert_iso6946.berechne_uwert → r_oben` = 6,304348 | 6,304348160715462 | 1,6 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_u | `b3_uwert_iso6946.berechne_uwert → r_unten` = 6,001318 | 6,001317668514656 | 3,3 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.
- Im IFC-Modell (Pset_WallCommon.ThermalTransmittance) steht der U-Wert mit drei Dezimalstellen. Das ist ein Zwischenwert für Folgerechnungen (vgl. JCGM 100:2008, 7.2.6); als Endergebnis gilt die Angabe mit zwei signifikanten Stellen.

### Grafischer Nachweis

**Abbildung N-B3-raster-verputzt/schnitt: Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)** (Maßstab 1:5)

![Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)](svg/N-B3-raster-verputzt_schnitt.svg)

Abschnitt a = Holz (Ständer), Abschnitt b = Dämmung. Maße in mm.

**Abbildung N-B3-raster-verputzt/grenzwerte: Grenzwerte des Wärmedurchgangswiderstands**

![Grenzwerte des Wärmedurchgangswiderstands](svg/N-B3-raster-verputzt_grenzwerte.svg)

**Abbildung N-B3-raster-verputzt/uwert: U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)**

![U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)](svg/N-B3-raster-verputzt_uwert.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `d83c1467a6507169db1402f90ad691d747392a18284991720d3da732d0a26ac4`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b3-raster-hinterlueftet"></a>

## N-B3-raster-hinterlueftet – U-Wert Außenwand AW-01 (Holzanteil aus dem Raster, hinterlueftet)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,801

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Außenwand AW-01, Typ AW-HRB-01, Variante raster/hinterlueftet |
| IFC-GlobalId | `0gsiGQj_bG3wx8M0qwRA0U` |
| IFC-Klasse | IfcWall |
| IFC-Datei (SHA-256) | wandelement.ifc (aus B1) (`5a796ea7b0f1d8c0…`) |

### Regel

> Der Wärmedurchgangskoeffizient der Außenwand darf 0,20 W/(m²·K) nicht überschreiten. Berechnung nach dem vereinfachten Verfahren für Bauteile aus homogenen und inhomogenen Schichten (oberer und unterer Grenzwert).

Quelle: DIN EN ISO 6946:2018-03 (ISO 6946:2017); Grenzwert: holzrahmenbau.ids HRB-01 (Projektanforderung) · Fassung: 2018-03 · Fundstelle: 6.5.2, 6.6, 6.7.1.1, 6.7.2, 6.8 · Prüfung am Primärtext: [V]  
Regelwerk-Profil: `DE-Waermeschutz-Beispiel` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Wärmeübergangswiderstand innen | $R_{\mathrm{si}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8, horizontaler Wärmestrom |
| Wärmeübergangswiderstand außen | $R_{\mathrm{se}}$ | 0,13 m²·K/W | – | konstante | DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.8; stark belüftete Luftschicht: R_se = R_si (6.9.4) |
| Dicke GKF | $d_{\mathrm{GKF}}$ | 12,5 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht gkf |
| Dicke OSB/3 | $d_{\mathrm{OSB}}$ | 15 mm | 0,3 mm | eingabe | daten/wandelement.json Schicht osb |
| Dicke Gefach | $d_{\mathrm{G}}$ | 200 mm | 2 mm | eingabe | daten/wandelement.json Schicht gefach |
| Dicke Holzfaserdämmplatte | $d_{\mathrm{HFD}}$ | 60 mm | 1 mm | eingabe | daten/wandelement.json Schicht hfd |
| Bemessungswert λ GKF | $\lambda_{\mathrm{GKF}}$ | 0,25 W/(m·K) | 0,0075 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe (Beispielwert) |
| Bemessungswert λ OSB/3 | $\lambda_{\mathrm{OSB}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typische Herstellerangabe / DIN EN 13986 (Beispielwert) |
| Bemessungswert λ Holz (KVH C24) | $\lambda_{\mathrm{H}}$ | 0,13 W/(m·K) | 0,0039 W/(m·K) | eingabe | daten/wandelement.json: typischer Wert Nadelholz, vgl. DIN EN ISO 10456 (Beispielwert) |
| Bemessungswert λ Gefachdämmung | $\lambda_{\mathrm{D}}$ | 0,038 W/(m·K) | 0,00114 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Bemessungswert λ Holzfaserdämmplatte | $\lambda_{\mathrm{HFD}}$ | 0,043 W/(m·K) | 0,00129 W/(m·K) | eingabe | daten/wandelement.json: Beispielwert Herstellerangabe (Bemessungswert) |
| Ständerbreite | $b_{\mathrm{St}}$ | 60 mm | – | eingabe | daten/wandelement.json /wand/staender/breite |
| Achsmaß der Ständer | $e_{\mathrm{St}}$ | 625 mm | – | eingabe | daten/wandelement.json /wand/staender/raster |
| Höchstwert des U-Werts | $U_{\mathrm{max}}$ | 0,20 W/(m²·K) | – | grenzwert | holzrahmenbau.ids, HRB-01 (Projektanforderung, Beispielwert) |

### Annahmen

- **Annahme:** Korrekturen ΔU nach Anhang F nicht angesetzt: Luftspalte Stufe 0 (Dämmung passgenau), Befestigungen durchdringen die Dämmschicht nicht (6.4 d: Korrektur nur bei > 3 % von U).
- **Annahme:** Die Dampfbremse (0,2 mm) ist thermisch vernachlässigt.
- **Annahme:** λ-Werte sind Beispielwerte aus dem Parametermodell, keine Tabellenwerte der DIN 4108-4.
- **Annahme:** Unsicherheiten der Dicken (Rechteckverteilung) und der λ-Werte (3 %, normal): Annahme zur Demonstration der Unsicherheitsfortpflanzung.

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Holzanteil aus dem Raster** (Flächenanteil Abschnitt a)

$$
f_{\mathrm{a}} = \frac{b_{\mathrm{St}}}{e_{\mathrm{St}}}
$$

$$
f_{\mathrm{a}} = \frac{60\ \mathrm{mm}}{625\ \mathrm{mm}} = 0{,}096000
$$

Ausdruck (maschinenlesbar): `b_St/e_St`

**Schritt 2: Wärmedurchlasswiderstand GKF** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.7.1.1, Formel (3))

$$
R_{\mathrm{GKF}} = \frac{d_{\mathrm{GKF}}}{\lambda_{\mathrm{GKF}}}
$$

$$
R_{\mathrm{GKF}} = \frac{12{,}5\ \mathrm{mm}}{0{,}25\ \mathrm{W/(m\cdot K)}} = 0{,}050000\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_GKF/lambda_GKF`

**Schritt 3: Wärmedurchlasswiderstand OSB/3** (6.7.1.1, Formel (3))

$$
R_{\mathrm{OSB}} = \frac{d_{\mathrm{OSB}}}{\lambda_{\mathrm{OSB}}}
$$

$$
R_{\mathrm{OSB}} = \frac{15\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 0{,}11538\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_OSB/lambda_OSB`

**Schritt 4: Wärmedurchlasswiderstand Holzfaserdämmplatte** (6.7.1.1, Formel (3))

$$
R_{\mathrm{HFD}} = \frac{d_{\mathrm{HFD}}}{\lambda_{\mathrm{HFD}}}
$$

$$
R_{\mathrm{HFD}} = \frac{60\ \mathrm{mm}}{0{,}043\ \mathrm{W/(m\cdot K)}} = 1{,}3953\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_HFD/lambda_HFD`

**Schritt 5: Gefachschicht, Abschnitt a (Holz)** (6.7.1.1)

$$
R_{\mathrm{Ga}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{H}}}
$$

$$
R_{\mathrm{Ga}} = \frac{200\ \mathrm{mm}}{0{,}13\ \mathrm{W/(m\cdot K)}} = 1{,}5385\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_H`

**Schritt 6: Gefachschicht, Abschnitt b (Dämmung)** (6.7.1.1)

$$
R_{\mathrm{Gb}} = \frac{d_{\mathrm{G}}}{\lambda_{\mathrm{D}}}
$$

$$
R_{\mathrm{Gb}} = \frac{200\ \mathrm{mm}}{0{,}038\ \mathrm{W/(m\cdot K)}} = 5{,}2632\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_D`

**Schritt 7: Gesamtwiderstand Abschnitt a (innen bis außen)** (6.7.2 (oberer Grenzwert, Abschnittswiderstände))

$$
R_{\mathrm{T},a} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Ga}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},a} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 1{,}5385\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 3{,}3592\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Ga + R_HFD + R_se`

**Schritt 8: Gesamtwiderstand Abschnitt b** (6.7.2)

$$
R_{\mathrm{T},b} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R_{\mathrm{Gb}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R_{\mathrm{T},b} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 5{,}2632\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 7{,}0839\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Gb + R_HFD + R_se`

**Schritt 9: Flächenanteil Abschnitt b**

$$
f_{\mathrm{b}} = 1 - f_{\mathrm{a}}
$$

$$
f_{\mathrm{b}} = 1 - 0{,}096000 = 0{,}90400
$$

Ausdruck (maschinenlesbar): `1 - f_a`

**Schritt 10: oberer Grenzwert R'_T (parallele Wärmeströme)** (6.7.2, oberer Grenzwert [Absatznummer U])

$$
R'_{\mathrm{T}} = \frac{1}{\frac{f_{\mathrm{a}}}{R_{\mathrm{T},a}} + \frac{f_{\mathrm{b}}}{R_{\mathrm{T},b}}}
$$

$$
R'_{\mathrm{T}} = \frac{1}{\frac{0{,}096000}{3{,}3592\ \mathrm{m^{2}\cdot K/W}} + \frac{0{,}90400}{7{,}0839\ \mathrm{m^{2}\cdot K/W}}} = 6{,}4024\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `1/(f_a/R_Ta + f_b/R_Tb)`

**Schritt 11: äquivalente Wärmeleitfähigkeit der Gefachschicht** (6.7.2, unterer Grenzwert)

$$
\lambda'' = f_{\mathrm{a}} \cdot \lambda_{\mathrm{H}} + f_{\mathrm{b}} \cdot \lambda_{\mathrm{D}}
$$

$$
\lambda'' = 0{,}096000 \cdot 0{,}13\ \mathrm{W/(m\cdot K)} + 0{,}90400 \cdot 0{,}038\ \mathrm{W/(m\cdot K)} = 0{,}046832\ \mathrm{W/(m\cdot K)}
$$

Ausdruck (maschinenlesbar): `f_a*lambda_H + f_b*lambda_D`

**Schritt 12: Wärmedurchlasswiderstand Gefach mit λ''** (6.7.2, unterer Grenzwert)

$$
R''_{\mathrm{G}} = \frac{d_{\mathrm{G}}}{\lambda''}
$$

$$
R''_{\mathrm{G}} = \frac{200\ \mathrm{mm}}{0{,}046832\ \mathrm{W/(m\cdot K)}} = 4{,}2706\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `d_G/lambda_eq`

**Schritt 13: unterer Grenzwert R''_T (isotherme Ebenen)** (6.7.2, unterer Grenzwert [Absatznummer U])

$$
R''_{\mathrm{T}} = R_{\mathrm{si}} + R_{\mathrm{GKF}} + R_{\mathrm{OSB}} + R''_{\mathrm{G}} + R_{\mathrm{HFD}} + R_{\mathrm{se}}
$$

$$
R''_{\mathrm{T}} = 0{,}13\ \mathrm{m^{2}\cdot K/W} + 0{,}050000\ \mathrm{m^{2}\cdot K/W} + 0{,}11538\ \mathrm{m^{2}\cdot K/W} + 4{,}2706\ \mathrm{m^{2}\cdot K/W} + 1{,}3953\ \mathrm{m^{2}\cdot K/W} + 0{,}13\ \mathrm{m^{2}\cdot K/W} = 6{,}0913\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `R_si + R_GKF + R_OSB + R_Geq + R_HFD + R_se`

**Schritt 14: Wärmedurchgangswiderstand als arithmetisches Mittel** (6.7.2.2 [V])

$$
R_{\mathrm{T}} = \frac{R'_{\mathrm{T}} + R''_{\mathrm{T}}}{2}
$$

$$
R_{\mathrm{T}} = \frac{6{,}4024\ \mathrm{m^{2}\cdot K/W} + 6{,}0913\ \mathrm{m^{2}\cdot K/W}}{2} = 6{,}2469\ \mathrm{m^{2}\cdot K/W}
$$

Ausdruck (maschinenlesbar): `(R_o + R_u)/2`

**Schritt 15: maximaler relativer Fehler** (6.7.2, Abschätzung des Fehlers)

$$
e_{\mathrm{rel}} = \frac{R'_{\mathrm{T}} - R''_{\mathrm{T}}}{2 \cdot R_{\mathrm{T}}}
$$

$$
e_{\mathrm{rel}} = \frac{6{,}4024\ \mathrm{m^{2}\cdot K/W} - 6{,}0913\ \mathrm{m^{2}\cdot K/W}}{2 \cdot 6{,}2469\ \mathrm{m^{2}\cdot K/W}} = 2{,}4898\ \mathrm{\%}
$$

Ausdruck (maschinenlesbar): `(R_o - R_u)/(2*R_T)`

**Schritt 16: Wärmedurchgangskoeffizient** (DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2, Formel (1))

$$
U = \frac{1}{R_{\mathrm{T}}}
$$

$$
U = \frac{1}{6{,}2469\ \mathrm{m^{2}\cdot K/W}} = 0{,}16008\ \mathrm{W/(m^{2}\cdot K)}
$$

Ausdruck (maschinenlesbar): `1/R_T`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| U ≤ U_max | 0,16 W/(m²·K) | ≤ | 0,20 W/(m²·K) | 0,801 | erfüllt | holzrahmenbau.ids HRB-01 |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 2 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: DIN EN ISO 6946:2018-03 (ISO 6946:2017), 6.5.2: Endergebnis auf zwei signifikante Stellen [V].

### Messunsicherheit

Methode: lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette.

Ergebnis: **0,160 ± 0,007 W/(m²·K) (k = 2)**, kombinierte Standardunsicherheit u_c = 0,0033 W/(m²·K).

| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \|c\|·u | Anteil an u_c² |
|---|---:|---:|---|---:|---:|
| d_GKF | 0,3 mm | −0,000107 | (W/(m²·K))/(mm) | 0,000032 | 0,0 % |
| d_OSB | 0,3 mm | −0,000206 | (W/(m²·K))/(mm) | 0,000062 | 0,0 % |
| d_G | 2 mm | −0,000557 | (W/(m²·K))/(mm) | 0,0011 | 11,7 % |
| d_HFD | 1 mm | −0,000622 | (W/(m²·K))/(mm) | 0,00062 | 3,7 % |
| lambda_GKF | 0,0075 W/(m·K) | 0,00535 | (W/(m²·K))/(W/(m·K)) | 0,000040 | 0,0 % |
| lambda_OSB | 0,0039 W/(m·K) | 0,0237 | (W/(m²·K))/(W/(m·K)) | 0,000093 | 0,1 % |
| lambda_H | 0,0039 W/(m·K) | 0,165 | (W/(m²·K))/(W/(m·K)) | 0,00064 | 3,9 % |
| lambda_D | 0,00114 W/(m·K) | 2,37 | (W/(m²·K))/(W/(m·K)) | 0,0027 | 68,7 % |
| lambda_HFD | 0,00129 W/(m·K) | 0,868 | (W/(m²·K))/(W/(m·K)) | 0,0011 | 11,8 % |

Monte-Carlo (Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64); 100 000 Versuche, Seed 20260927): Mittelwert 0,1600, s = 0,0033, 95-%-Intervall [0,1537; 0,1664] W/(m²·K).

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| U | `b3_uwert_iso6946.berechne_uwert → u_wert (6 Dezimalstellen)` = 0,160081 | 0,16008062419998384 | 3,8 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_o | `b3_uwert_iso6946.berechne_uwert → r_oben` = 6,402387 | 6,402386738218921 | 2,6 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |
| R_u | `b3_uwert_iso6946.berechne_uwert → r_unten` = 6,091318 | 6,091317668514656 | 3,3 · 10⁻⁷ | ja (Toleranz 5 · 10⁻⁷) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.
- Im IFC-Modell (Pset_WallCommon.ThermalTransmittance) steht der U-Wert mit drei Dezimalstellen. Das ist ein Zwischenwert für Folgerechnungen (vgl. JCGM 100:2008, 7.2.6); als Endergebnis gilt die Angabe mit zwei signifikanten Stellen.

### Grafischer Nachweis

**Abbildung N-B3-raster-hinterlueftet/schnitt: Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)** (Maßstab 1:5)

![Horizontalschnitt Außenwand AW-01 (ein Ständerfeld, e = 625 mm)](svg/N-B3-raster-hinterlueftet_schnitt.svg)

Abschnitt a = Holz (Ständer), Abschnitt b = Dämmung. Maße in mm.

**Abbildung N-B3-raster-hinterlueftet/grenzwerte: Grenzwerte des Wärmedurchgangswiderstands**

![Grenzwerte des Wärmedurchgangswiderstands](svg/N-B3-raster-hinterlueftet_grenzwerte.svg)

**Abbildung N-B3-raster-hinterlueftet/uwert: U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)**

![U-Wert gegen Höchstwert (mit erweiterter Unsicherheit U, k = 2)](svg/N-B3-raster-hinterlueftet_uwert.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `15589a73043acae3c88e3fb2219289b0b6b020dd05be5f72f5eaf9a7ff2e5761`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b4-mittig-drittel"></a>

## N-B4-mittig-drittel – Abstandsflächen Szenario „mittig“ (Haus mittig, 5 m zu den seitlichen Grenzen, Giebel: drittel)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,654

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Gebäudevorlage Satteldach 10 × 12 m, Szenario mittig (kein IFC-Gebäudemodell in B4; GUID folgt mit dem Gebäudegenerator) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | – (–) |

### Regel

> Vor den Außenwänden sind Abstandsflächen der Tiefe T = 0,4 H, mindestens 3 m, einzuhalten; sie müssen auf dem Grundstück selbst liegen und dürfen bis zur Mitte öffentlicher Verkehrsflächen reichen. H = Wandhöhe + 1/3 der Dachhöhe bei Dachneigung ≤ 70°.

Quelle: BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft · Fassung: ab 01.05.2026 · Fundstelle: Art. 6 Abs. 2, 4, 5 · Prüfung am Primärtext: [U]  
Regelwerk-Profil: `BY-BayBO-2026-05` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Giebelbreite (quer zum First) | $b$ | 10 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/breite |
| Trauflänge | $l$ | 12 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/laenge |
| Wandhöhe bis Schnitt Wand/Dachhaut | $h_{\mathrm{w}}$ | 6,5 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/wandhoehe |
| Dachneigung | $\alpha$ | 45 ° | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/dachneigung_grad |
| Lage Südwestecke x | $x_{\mathrm{0}}$ | 5 m | – | eingabe | daten/grundstueck.json Szenario mittig |
| Lage Südwestecke y | $y_{\mathrm{0}}$ | 9 m | – | eingabe | daten/grundstueck.json Szenario mittig |
| Anrechnung Dachhöhe (Neigung ≤ 70°) | $f_{\mathrm{D}}$ | 0,3333333333333333 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4 |
| Anrechnung Giebeldreieck | $f_{\mathrm{Gi}}$ | 0,3333333333333333 | – | annahme | Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U]) |
| Faktor Tiefe | $c_{\mathrm{T}}$ | 0,4 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| Mindesttiefe | $T_{\mathrm{min}}$ | 3 m | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| zulässige Fläche außerhalb | $A_{\mathrm{zul}}$ | 0 m² | – | grenzwert | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 2 Satz 1: Abstandsflächen auf dem Grundstück selbst |

### Annahmen

- **Annahme:** Gelände eben; Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 BayBO nicht berücksichtigt.
- **Annahme:** Giebelwand: Tiefe punktweise entlang der Wand (gestauchte Giebelform), unten auf die Mindesttiefe begrenzt.
- **Annahme:** Anrechnung Giebeldreieck (f_Gi) = 0,3333333333333333: Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U])

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Dachhöhe über Traufe**

$$
h_{\mathrm{D}} = \frac{b}{2} \cdot \tan\left(\alpha\right)
$$

$$
h_{\mathrm{D}} = \frac{10\ \mathrm{m}}{2} \cdot \tan\left(45\ \mathrm{^{\circ}}\right) = 5{,}0000\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `b/2*tan(alpha)`

**Schritt 2: Maß H der Traufwände** (BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4)

$$
H_{\mathrm{T}} = h_{\mathrm{w}} + f_{\mathrm{D}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{T}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_D*h_D`

**Schritt 3: Tiefe der Abstandsfläche Traufe** (Abs. 5)

$$
T_{\mathrm{T}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{T}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{T}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_T, T_min)`

**Schritt 4: Maß H der Giebelwände am First** (Abs. 4)

$$
H_{\mathrm{G}} = h_{\mathrm{w}} + f_{\mathrm{Gi}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{G}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_Gi*h_D`

**Schritt 5: Tiefe der Abstandsfläche Giebel (First)** (Abs. 5)

$$
T_{\mathrm{G}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{G}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{G}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_G, T_min)`

**Schritt 6: vorhandene Tiefe vor Wand West (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{W}}$ = 5 m

**Schritt 7: Fläche der Abstandsfläche West (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{W}}$ = 0 m²

**Schritt 8: vorhandene Tiefe vor Wand Ost (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{O}}$ = 5 m

**Schritt 9: Fläche der Abstandsfläche Ost (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{O}}$ = 0 m²

**Schritt 10: vorhandene Tiefe vor Wand Süd (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{S}}$ = 13 m

**Schritt 11: Fläche der Abstandsfläche Süd (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{S}}$ = 0 m²

**Schritt 12: vorhandene Tiefe vor Wand Nord (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{N}}$ = 9 m

**Schritt 13: Fläche der Abstandsfläche Nord (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{N}}$ = 0 m²

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| West (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| West (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Ost (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Ost (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Süd (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Süd (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 13,000 m | ≥ | 3,2667 m | 0,252 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Nord (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Nord (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 9,0000 m | ≥ | 3,2667 m | 0,363 | erfüllt | BayBO Art. 6 Abs. 5 [U] |

Der Vergleich erfolgt mit ungerundeten Werten, Toleranzen siehe JSON.

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| T_T | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| T_G | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| h_D | `b4_abstandsflaechen.pruefe_szenario → dachhoehe (3 Dez.)` = 5 | 4,999999999999999 | 8,9 · 10⁻¹⁶ | ja (Toleranz 5 · 10⁻⁴) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.

### Grafischer Nachweis

**Abbildung N-B4-mittig-drittel/lageplan: Lageplan mit Abstandsflächen, Szenario mittig (drittel)** (Maßstab 1:200)

![Lageplan mit Abstandsflächen, Szenario mittig (drittel)](svg/N-B4-mittig-drittel_lageplan.svg)

Nordrichtung = +y. Grün: Abstandsfläche innerhalb von Grundstück und halber Straße; rot: außerhalb. Die Straße (schraffiert) ist bis zur Mitte anrechenbar.

**Abbildung N-B4-mittig-drittel/tiefen: Vorhandene gegen erforderliche Tiefe je Wand**

![Vorhandene gegen erforderliche Tiefe je Wand](svg/N-B4-mittig-drittel_tiefen.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `0676e9b04fab03b8c0b5acf3cf846624738cd66c6998281ff6318090aa58a3fd`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b4-zu-nah-drittel"></a>

## N-B4-zu_nah-drittel – Abstandsflächen Szenario „zu_nah“ (Haus 2 m an die westliche Grenze gerückt, Giebel: drittel)

**Ergebnis: [NICHT ERFÜLLT]** · maßgebende Ausnutzung η = 1,634

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Gebäudevorlage Satteldach 10 × 12 m, Szenario zu_nah (kein IFC-Gebäudemodell in B4; GUID folgt mit dem Gebäudegenerator) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | – (–) |

### Regel

> Vor den Außenwänden sind Abstandsflächen der Tiefe T = 0,4 H, mindestens 3 m, einzuhalten; sie müssen auf dem Grundstück selbst liegen und dürfen bis zur Mitte öffentlicher Verkehrsflächen reichen. H = Wandhöhe + 1/3 der Dachhöhe bei Dachneigung ≤ 70°.

Quelle: BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft · Fassung: ab 01.05.2026 · Fundstelle: Art. 6 Abs. 2, 4, 5 · Prüfung am Primärtext: [U]  
Regelwerk-Profil: `BY-BayBO-2026-05` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Giebelbreite (quer zum First) | $b$ | 10 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/breite |
| Trauflänge | $l$ | 12 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/laenge |
| Wandhöhe bis Schnitt Wand/Dachhaut | $h_{\mathrm{w}}$ | 6,5 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/wandhoehe |
| Dachneigung | $\alpha$ | 45 ° | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/dachneigung_grad |
| Lage Südwestecke x | $x_{\mathrm{0}}$ | 2 m | – | eingabe | daten/grundstueck.json Szenario zu_nah |
| Lage Südwestecke y | $y_{\mathrm{0}}$ | 9 m | – | eingabe | daten/grundstueck.json Szenario zu_nah |
| Anrechnung Dachhöhe (Neigung ≤ 70°) | $f_{\mathrm{D}}$ | 0,3333333333333333 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4 |
| Anrechnung Giebeldreieck | $f_{\mathrm{Gi}}$ | 0,3333333333333333 | – | annahme | Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U]) |
| Faktor Tiefe | $c_{\mathrm{T}}$ | 0,4 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| Mindesttiefe | $T_{\mathrm{min}}$ | 3 m | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| zulässige Fläche außerhalb | $A_{\mathrm{zul}}$ | 0 m² | – | grenzwert | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 2 Satz 1: Abstandsflächen auf dem Grundstück selbst |

### Annahmen

- **Annahme:** Gelände eben; Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 BayBO nicht berücksichtigt.
- **Annahme:** Giebelwand: Tiefe punktweise entlang der Wand (gestauchte Giebelform), unten auf die Mindesttiefe begrenzt.
- **Annahme:** Anrechnung Giebeldreieck (f_Gi) = 0,3333333333333333: Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U])

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Dachhöhe über Traufe**

$$
h_{\mathrm{D}} = \frac{b}{2} \cdot \tan\left(\alpha\right)
$$

$$
h_{\mathrm{D}} = \frac{10\ \mathrm{m}}{2} \cdot \tan\left(45\ \mathrm{^{\circ}}\right) = 5{,}0000\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `b/2*tan(alpha)`

**Schritt 2: Maß H der Traufwände** (BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4)

$$
H_{\mathrm{T}} = h_{\mathrm{w}} + f_{\mathrm{D}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{T}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_D*h_D`

**Schritt 3: Tiefe der Abstandsfläche Traufe** (Abs. 5)

$$
T_{\mathrm{T}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{T}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{T}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_T, T_min)`

**Schritt 4: Maß H der Giebelwände am First** (Abs. 4)

$$
H_{\mathrm{G}} = h_{\mathrm{w}} + f_{\mathrm{Gi}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{G}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_Gi*h_D`

**Schritt 5: Tiefe der Abstandsfläche Giebel (First)** (Abs. 5)

$$
T_{\mathrm{G}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{G}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{G}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_G, T_min)`

**Schritt 6: vorhandene Tiefe vor Wand West (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{W}}$ = 2 m

**Schritt 7: Fläche der Abstandsfläche West (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{W}}$ = 15,2 m²

**Schritt 8: vorhandene Tiefe vor Wand Ost (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{O}}$ = 8 m

**Schritt 9: Fläche der Abstandsfläche Ost (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{O}}$ = 0 m²

**Schritt 10: vorhandene Tiefe vor Wand Süd (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{S}}$ = 13 m

**Schritt 11: Fläche der Abstandsfläche Süd (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{S}}$ = 0 m²

**Schritt 12: vorhandene Tiefe vor Wand Nord (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{N}}$ = 9 m

**Schritt 13: Fläche der Abstandsfläche Nord (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{N}}$ = 0 m²

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| West (Traufe): Abstandsfläche auf dem Grundstück | 15,200 m² | ≤ | 0 m² | – | **nicht erfüllt** | BayBO Art. 6 Abs. 2 [U] |
| West (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 2,0000 m | ≥ | 3,2667 m | 1,634 | **nicht erfüllt** | BayBO Art. 6 Abs. 5 [U] |
| Ost (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Ost (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 8,0000 m | ≥ | 3,2667 m | 0,409 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Süd (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Süd (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 13,000 m | ≥ | 3,2667 m | 0,252 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Nord (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Nord (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 9,0000 m | ≥ | 3,2667 m | 0,363 | erfüllt | BayBO Art. 6 Abs. 5 [U] |

Der Vergleich erfolgt mit ungerundeten Werten, Toleranzen siehe JSON.

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| T_T | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| T_G | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| h_D | `b4_abstandsflaechen.pruefe_szenario → dachhoehe (3 Dez.)` = 5 | 4,999999999999999 | 8,9 · 10⁻¹⁶ | ja (Toleranz 5 · 10⁻⁴) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.

### Grafischer Nachweis

**Abbildung N-B4-zu_nah-drittel/lageplan: Lageplan mit Abstandsflächen, Szenario zu_nah (drittel)** (Maßstab 1:200)

![Lageplan mit Abstandsflächen, Szenario zu_nah (drittel)](svg/N-B4-zu_nah-drittel_lageplan.svg)

Nordrichtung = +y. Grün: Abstandsfläche innerhalb von Grundstück und halber Straße; rot: außerhalb. Die Straße (schraffiert) ist bis zur Mitte anrechenbar.

**Abbildung N-B4-zu_nah-drittel/tiefen: Vorhandene gegen erforderliche Tiefe je Wand**

![Vorhandene gegen erforderliche Tiefe je Wand](svg/N-B4-zu_nah-drittel_tiefen.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `833f7f6c74c3cf0985677c59306e212739de06c9f67f557c5a6ef8c459eff957`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b4-an-strasse-drittel"></a>

## N-B4-an_strasse-drittel – Abstandsflächen Szenario „an_strasse“ (Haus 1 m hinter der Straßengrenze (Süd), Giebel: drittel)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,654

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Gebäudevorlage Satteldach 10 × 12 m, Szenario an_strasse (kein IFC-Gebäudemodell in B4; GUID folgt mit dem Gebäudegenerator) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | – (–) |

### Regel

> Vor den Außenwänden sind Abstandsflächen der Tiefe T = 0,4 H, mindestens 3 m, einzuhalten; sie müssen auf dem Grundstück selbst liegen und dürfen bis zur Mitte öffentlicher Verkehrsflächen reichen. H = Wandhöhe + 1/3 der Dachhöhe bei Dachneigung ≤ 70°.

Quelle: BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft · Fassung: ab 01.05.2026 · Fundstelle: Art. 6 Abs. 2, 4, 5 · Prüfung am Primärtext: [U]  
Regelwerk-Profil: `BY-BayBO-2026-05` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Giebelbreite (quer zum First) | $b$ | 10 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/breite |
| Trauflänge | $l$ | 12 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/laenge |
| Wandhöhe bis Schnitt Wand/Dachhaut | $h_{\mathrm{w}}$ | 6,5 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/wandhoehe |
| Dachneigung | $\alpha$ | 45 ° | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/dachneigung_grad |
| Lage Südwestecke x | $x_{\mathrm{0}}$ | 5 m | – | eingabe | daten/grundstueck.json Szenario an_strasse |
| Lage Südwestecke y | $y_{\mathrm{0}}$ | 1 m | – | eingabe | daten/grundstueck.json Szenario an_strasse |
| Anrechnung Dachhöhe (Neigung ≤ 70°) | $f_{\mathrm{D}}$ | 0,3333333333333333 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4 |
| Anrechnung Giebeldreieck | $f_{\mathrm{Gi}}$ | 0,3333333333333333 | – | annahme | Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U]) |
| Faktor Tiefe | $c_{\mathrm{T}}$ | 0,4 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| Mindesttiefe | $T_{\mathrm{min}}$ | 3 m | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| zulässige Fläche außerhalb | $A_{\mathrm{zul}}$ | 0 m² | – | grenzwert | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 2 Satz 1: Abstandsflächen auf dem Grundstück selbst |

### Annahmen

- **Annahme:** Gelände eben; Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 BayBO nicht berücksichtigt.
- **Annahme:** Giebelwand: Tiefe punktweise entlang der Wand (gestauchte Giebelform), unten auf die Mindesttiefe begrenzt.
- **Annahme:** Anrechnung Giebeldreieck (f_Gi) = 0,3333333333333333: Lesart „drittel“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U])

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Dachhöhe über Traufe**

$$
h_{\mathrm{D}} = \frac{b}{2} \cdot \tan\left(\alpha\right)
$$

$$
h_{\mathrm{D}} = \frac{10\ \mathrm{m}}{2} \cdot \tan\left(45\ \mathrm{^{\circ}}\right) = 5{,}0000\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `b/2*tan(alpha)`

**Schritt 2: Maß H der Traufwände** (BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4)

$$
H_{\mathrm{T}} = h_{\mathrm{w}} + f_{\mathrm{D}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{T}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_D*h_D`

**Schritt 3: Tiefe der Abstandsfläche Traufe** (Abs. 5)

$$
T_{\mathrm{T}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{T}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{T}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_T, T_min)`

**Schritt 4: Maß H der Giebelwände am First** (Abs. 4)

$$
H_{\mathrm{G}} = h_{\mathrm{w}} + f_{\mathrm{Gi}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{G}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_Gi*h_D`

**Schritt 5: Tiefe der Abstandsfläche Giebel (First)** (Abs. 5)

$$
T_{\mathrm{G}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{G}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{G}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_G, T_min)`

**Schritt 6: vorhandene Tiefe vor Wand West (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{W}}$ = 5 m

**Schritt 7: Fläche der Abstandsfläche West (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{W}}$ = 0 m²

**Schritt 8: vorhandene Tiefe vor Wand Ost (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{O}}$ = 5 m

**Schritt 9: Fläche der Abstandsfläche Ost (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{O}}$ = 0 m²

**Schritt 10: vorhandene Tiefe vor Wand Süd (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{S}}$ = 5 m

**Schritt 11: Fläche der Abstandsfläche Süd (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{S}}$ = 0 m²

**Schritt 12: vorhandene Tiefe vor Wand Nord (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{N}}$ = 17 m

**Schritt 13: Fläche der Abstandsfläche Nord (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{N}}$ = 0 m²

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| West (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| West (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Ost (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Ost (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Süd (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Süd (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Nord (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Nord (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 17,000 m | ≥ | 3,2667 m | 0,193 | erfüllt | BayBO Art. 6 Abs. 5 [U] |

Der Vergleich erfolgt mit ungerundeten Werten, Toleranzen siehe JSON.

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| T_T | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| T_G | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| h_D | `b4_abstandsflaechen.pruefe_szenario → dachhoehe (3 Dez.)` = 5 | 4,999999999999999 | 8,9 · 10⁻¹⁶ | ja (Toleranz 5 · 10⁻⁴) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.

### Grafischer Nachweis

**Abbildung N-B4-an_strasse-drittel/lageplan: Lageplan mit Abstandsflächen, Szenario an_strasse (drittel)** (Maßstab 1:200)

![Lageplan mit Abstandsflächen, Szenario an_strasse (drittel)](svg/N-B4-an_strasse-drittel_lageplan.svg)

Nordrichtung = +y. Grün: Abstandsfläche innerhalb von Grundstück und halber Straße; rot: außerhalb. Die Straße (schraffiert) ist bis zur Mitte anrechenbar.

**Abbildung N-B4-an_strasse-drittel/tiefen: Vorhandene gegen erforderliche Tiefe je Wand**

![Vorhandene gegen erforderliche Tiefe je Wand](svg/N-B4-an_strasse-drittel_tiefen.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `c39ad8abf9142906532b856ac0879f409da4205932b8a834a4116ec05a287670`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b4-mittig-voll"></a>

## N-B4-mittig-voll – Abstandsflächen Szenario „mittig“ (Haus mittig, 5 m zu den seitlichen Grenzen, Giebel: voll)

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,654

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | Gebäudevorlage Satteldach 10 × 12 m, Szenario mittig (kein IFC-Gebäudemodell in B4; GUID folgt mit dem Gebäudegenerator) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | – (–) |

### Regel

> Vor den Außenwänden sind Abstandsflächen der Tiefe T = 0,4 H, mindestens 3 m, einzuhalten; sie müssen auf dem Grundstück selbst liegen und dürfen bis zur Mitte öffentlicher Verkehrsflächen reichen. H = Wandhöhe + 1/3 der Dachhöhe bei Dachneigung ≤ 70°.

Quelle: BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft · Fassung: ab 01.05.2026 · Fundstelle: Art. 6 Abs. 2, 4, 5 · Prüfung am Primärtext: [U]  
Regelwerk-Profil: `BY-BayBO-2026-05` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Giebelbreite (quer zum First) | $b$ | 10 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/breite |
| Trauflänge | $l$ | 12 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/laenge |
| Wandhöhe bis Schnitt Wand/Dachhaut | $h_{\mathrm{w}}$ | 6,5 m | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/wandhoehe |
| Dachneigung | $\alpha$ | 45 ° | – | eingabe | daten/grundstueck.json /gebaeude_vorlage/dachneigung_grad |
| Lage Südwestecke x | $x_{\mathrm{0}}$ | 5 m | – | eingabe | daten/grundstueck.json Szenario mittig |
| Lage Südwestecke y | $y_{\mathrm{0}}$ | 9 m | – | eingabe | daten/grundstueck.json Szenario mittig |
| Anrechnung Dachhöhe (Neigung ≤ 70°) | $f_{\mathrm{D}}$ | 0,3333333333333333 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4 |
| Anrechnung Giebeldreieck | $f_{\mathrm{Gi}}$ | 1 | – | annahme | Lesart „voll“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U]) |
| Faktor Tiefe | $c_{\mathrm{T}}$ | 0,4 | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| Mindesttiefe | $T_{\mathrm{min}}$ | 3 m | – | konstante | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 5 Satz 1 |
| zulässige Fläche außerhalb | $A_{\mathrm{zul}}$ | 0 m² | – | grenzwert | BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 2 Satz 1: Abstandsflächen auf dem Grundstück selbst |

### Annahmen

- **Annahme:** Gelände eben; Abs. 5a, 6 und 7 sowie Satzungen nach Art. 81 BayBO nicht berücksichtigt.
- **Annahme:** Giebelwand: Tiefe punktweise entlang der Wand (gestauchte Giebelform), unten auf die Mindesttiefe begrenzt.
- **Annahme:** Anrechnung Giebeldreieck (f_Gi) = 1: Lesart „voll“ (umschaltbar; welche Lesart dem Wortlaut entspricht, ist offen [U])

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: Dachhöhe über Traufe**

$$
h_{\mathrm{D}} = \frac{b}{2} \cdot \tan\left(\alpha\right)
$$

$$
h_{\mathrm{D}} = \frac{10\ \mathrm{m}}{2} \cdot \tan\left(45\ \mathrm{^{\circ}}\right) = 5{,}0000\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `b/2*tan(alpha)`

**Schritt 2: Maß H der Traufwände** (BayBO Art. 6 (Fassung ab 01.05.2026) nach Recherche 02; Primärtext nicht geprüft, Abs. 4)

$$
H_{\mathrm{T}} = h_{\mathrm{w}} + f_{\mathrm{D}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{T}} = 6{,}5\ \mathrm{m} + 0{,}3333333333333333 \cdot 5{,}0000\ \mathrm{m} = 8{,}1667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_D*h_D`

**Schritt 3: Tiefe der Abstandsfläche Traufe** (Abs. 5)

$$
T_{\mathrm{T}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{T}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{T}} = \max\left(0{,}4 \cdot 8{,}1667\ \mathrm{m},\ 3\ \mathrm{m}\right) = 3{,}2667\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_T, T_min)`

**Schritt 4: Maß H der Giebelwände am First** (Abs. 4)

$$
H_{\mathrm{G}} = h_{\mathrm{w}} + f_{\mathrm{Gi}} \cdot h_{\mathrm{D}}
$$

$$
H_{\mathrm{G}} = 6{,}5\ \mathrm{m} + 1 \cdot 5{,}0000\ \mathrm{m} = 11{,}500\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `h_w + f_Gi*h_D`

**Schritt 5: Tiefe der Abstandsfläche Giebel (First)** (Abs. 5)

$$
T_{\mathrm{G}} = \max\left(c_{\mathrm{T}} \cdot H_{\mathrm{G}},\ T_{\mathrm{min}}\right)
$$

$$
T_{\mathrm{G}} = \max\left(0{,}4 \cdot 11{,}500\ \mathrm{m},\ 3\ \mathrm{m}\right) = 4{,}6000\ \mathrm{m}
$$

Ausdruck (maschinenlesbar): `max(c_T*H_G, T_min)`

**Schritt 6: vorhandene Tiefe vor Wand West (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{W}}$ = 5 m

**Schritt 7: Fläche der Abstandsfläche West (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{W}}$ = 0 m²

**Schritt 8: vorhandene Tiefe vor Wand Ost (Traufe) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{O}}$ = 5 m

**Schritt 9: Fläche der Abstandsfläche Ost (Traufe) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{O}}$ = 0 m²

**Schritt 10: vorhandene Tiefe vor Wand Süd (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{S}}$ = 13 m

**Schritt 11: Fläche der Abstandsfläche Süd (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{S}}$ = 0 m²

**Schritt 12: vorhandene Tiefe vor Wand Nord (Giebel) (Wandmitte bis Grenze der zulässigen Fläche)**

Verfahren: Strahl von der Wandmitte in Richtung der Außennormalen, Schnitt mit dem Rand von Grundstück ∪ halber Straßenbreite (b4_abstandsflaechen.vorhandene_tiefe)

Ergebnis: $T_{\mathrm{v},\mathrm{N}}$ = 9 m

**Schritt 13: Fläche der Abstandsfläche Nord (Giebel) außerhalb der zulässigen Fläche**

Verfahren: Polygon der Abstandsfläche minus (Grundstück ∪ halbe öffentliche Verkehrsfläche), Flächeninhalt (b4_abstandsflaechen.abstandsflaechen, Polygon.difference)

Ergebnis: $A_{\mathrm{a},\mathrm{N}}$ = 0 m²

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| West (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| West (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Ost (Traufe): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Ost (Traufe): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 5,0000 m | ≥ | 3,2667 m | 0,654 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Süd (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Süd (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 13,000 m | ≥ | 4,6000 m | 0,354 | erfüllt | BayBO Art. 6 Abs. 5 [U] |
| Nord (Giebel): Abstandsfläche auf dem Grundstück | 0,0000 m² | ≤ | 0 m² | – | erfüllt | BayBO Art. 6 Abs. 2 [U] |
| Nord (Giebel): vorhandene ≥ erforderliche Tiefe (Wandmitte) | 9,0000 m | ≥ | 4,6000 m | 0,512 | erfüllt | BayBO Art. 6 Abs. 5 [U] |

Der Vergleich erfolgt mit ungerundeten Werten, Toleranzen siehe JSON.

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| T_T | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 3,267 | 3,2666666666666666 | 3,3 · 10⁻⁴ | ja (Toleranz 5 · 10⁻⁴) |
| T_G | `b4_abstandsflaechen.pruefe_szenario → T_erforderlich (3 Dez.)` = 4,6 | 4,6000000000000005 | 8,9 · 10⁻¹⁶ | ja (Toleranz 5 · 10⁻⁴) |
| h_D | `b4_abstandsflaechen.pruefe_szenario → dachhoehe (3 Dez.)` = 5 | 4,999999999999999 | 8,9 · 10⁻¹⁶ | ja (Toleranz 5 · 10⁻⁴) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.

### Grafischer Nachweis

**Abbildung N-B4-mittig-voll/lageplan: Lageplan mit Abstandsflächen, Szenario mittig (voll)** (Maßstab 1:200)

![Lageplan mit Abstandsflächen, Szenario mittig (voll)](svg/N-B4-mittig-voll_lageplan.svg)

Nordrichtung = +y. Grün: Abstandsfläche innerhalb von Grundstück und halber Straße; rot: außerhalb. Die Straße (schraffiert) ist bis zur Mitte anrechenbar.

**Abbildung N-B4-mittig-voll/tiefen: Vorhandene gegen erforderliche Tiefe je Wand**

![Vorhandene gegen erforderliche Tiefe je Wand](svg/N-B4-mittig-voll_tiefen.svg)


### Rückverfolgbarkeit

- Hash (SHA-256): `e31acb476e7d2515ac33ffab98f9068cc2ae820e791e47f0f0f94d5aa10f017e`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


<a id="n-n-b5-01"></a>

## N-B5-01 – Treppenlauf gerade einläufig, Geschosshöhe 2,90 m

**Ergebnis: [ERFÜLLT]** · maßgebende Ausnutzung η = 0,972

### Gegenstand

| Merkmal | Wert |
|---|---|
| Bezeichnung | notwendige Treppe EG–OG, gerade einläufig (kein IFC-Modell in B5; IfcStair folgt mit dem Gebäudegenerator) |
| IFC-GlobalId | `–` |
| IFC-Klasse | – |
| IFC-Datei (SHA-256) | – (–) |

### Regel

> Baurechtlich notwendige Treppe in Wohngebäuden mit höchstens zwei Wohnungen: Steigung 140 … 200 mm, Auftritt 230 … 370 mm, Schrittmaß 2s + a = 590 … 650 mm, nutzbare Laufbreite ≥ 800 mm.

Quelle: DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) · Fassung: 2020-08 · Fundstelle: Tabelle der Grenzmaße (Tabellen nicht übernommen) · Prüfung am Primärtext: [U]  
Regelwerk-Profil: `DE-DIN18065-WG2WE` Version `0.1.0`

### Eingangsgrößen

| Größe | Symbol | Wert | u (k=1) | Art | Quelle |
|---|---|---:|---:|---|---|
| Geschosshöhe (OKFF bis OKFF) | $h_{\mathrm{G}}$ | 2900 mm | – | eingabe | Eingabe (Kommandozeile B5, Standard 2,90 m) |
| nutzbare Laufbreite | $b_{\mathrm{L}}$ | 900 mm | – | eingabe | Eingabe (Kommandozeile B5) |
| Fertigungsraster Auftritt | $r_{\mathrm{a}}$ | 5 mm | – | annahme | Annahme B5: übliches Raster im Treppenbau |
| Steigung min. | $s_{\mathrm{min}}$ | 140 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Steigung max. | $s_{\mathrm{max}}$ | 200 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Auftritt min. | $a_{\mathrm{min}}$ | 230 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Auftritt max. | $a_{\mathrm{max}}$ | 370 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Schrittmaß min. | $S_{\mathrm{min}}$ | 590 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Schrittmaß max. | $S_{\mathrm{max}}$ | 650 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Laufbreite min. | $b_{\mathrm{min}}$ | 800 mm | – | grenzwert | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02); b5_treppe_din18065.GRENZEN |
| Zielwert Schrittmaß | $S_{\mathrm{Z}}$ | 630 mm | – | annahme | Vorgabe der Aufgabe (Rangfolge, keine Normanforderung) |

### Annahmen

- **Annahme:** Nur gerade einläufige Treppe; Kopfhöhe, Podeste, Wendelung und Maßtoleranzen sind nicht geprüft.
- **Annahme:** Bequemlichkeits- und Sicherheitsregel sind Faustregeln und dienen nur der Rangfolge.
- **Annahme:** Fertigungsraster Auftritt (r_a) = 5 mm: Annahme B5: übliches Raster im Treppenbau
- **Annahme:** Zielwert Schrittmaß (S_Z) = 630 mm: Vorgabe der Aufgabe (Rangfolge, keine Normanforderung)

### Rechengang

Gerechnet wird ungerundet. Angezeigte Zwischenwerte: 5 signifikante Stellen, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02; Begründung: Anzeige von Zwischenwerten; gerechnet wird ungerundet (vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen).

**Schritt 1: kleinste Steigungszahl**

$$
n_{\mathrm{min}} = \left\lceil \frac{h_{\mathrm{G}}}{s_{\mathrm{max}}} \right\rceil
$$

$$
n_{\mathrm{min}} = \left\lceil \frac{2900\ \mathrm{mm}}{200\ \mathrm{mm}} \right\rceil = 15
$$

Ausdruck (maschinenlesbar): `ceil(h_G/s_max)`

**Schritt 2: größte Steigungszahl**

$$
n_{\mathrm{max}} = \left\lfloor \frac{h_{\mathrm{G}}}{s_{\mathrm{min}}} \right\rfloor
$$

$$
n_{\mathrm{max}} = \left\lfloor \frac{2900\ \mathrm{mm}}{140\ \mathrm{mm}} \right\rfloor = 20
$$

Ausdruck (maschinenlesbar): `floor(h_G/s_min)`

**Schritt 3: zulässige Lösungen im Suchraum**

Verfahren: vollständige Aufzählung n = n_min … n_max, a im Raster 5 mm, Filter nach allen Grenzwerten (exakte Arithmetik mit fractions.Fraction)

Ergebnis: $N_{\mathrm{L}}$ = 68

**Schritt 4: gewählte Steigungszahl**

Verfahren: lexikografische Rangfolge: |2s+a−630| (Toleranz ≤ halbe Rasterweite), |a−s−120|, |a+s−460|, Lauflänge

Ergebnis: $n$ = 17

**Schritt 5: gewählter Auftritt**

Verfahren: wie vor

Ergebnis: $a$ = 290 mm

**Schritt 6: Steigung (alle gleich)**

$$
s = \frac{h_{\mathrm{G}}}{n}
$$

$$
s = \frac{2900\ \mathrm{mm}}{17} = 170{,}59\ \mathrm{mm}
$$

Ausdruck (maschinenlesbar): `h_G/n`

**Schritt 7: Schrittmaß** (Schrittmaßregel 2s + a)

$$
S = 2 \cdot s + a
$$

$$
S = 2 \cdot 170{,}59\ \mathrm{mm} + 290\ \mathrm{mm} = 631{,}18\ \mathrm{mm}
$$

Ausdruck (maschinenlesbar): `2*s + a`

**Schritt 8: Lauflänge (n − 1 Auftritte)**

$$
l_{\mathrm{L}} = \left(n - 1\right) \cdot a
$$

$$
l_{\mathrm{L}} = \left(17 - 1\right) \cdot 290\ \mathrm{mm} = 4640\ \mathrm{mm}
$$

Ausdruck (maschinenlesbar): `(n - 1)*a`

**Schritt 9: Abweichung vom Zielschrittmaß**

$$
\mathrm{dS} = \left|S - S_{\mathrm{Z}}\right|
$$

$$
\mathrm{dS} = \left|631{,}18\ \mathrm{mm} - 630\ \mathrm{mm}\right| = 1{,}1765\ \mathrm{mm}
$$

Ausdruck (maschinenlesbar): `abs(S - S_Z)`

### Nachweis

| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |
|---|---:|:---:|---:|---:|---|---|
| Steigung ≥ min. | 170,6 mm | ≥ | 140 mm | 0,821 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Steigung ≤ max. | 170,6 mm | ≤ | 200 mm | 0,853 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Auftritt ≥ min. | 290 mm | ≥ | 230 mm | 0,794 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Auftritt ≤ max. | 290 mm | ≤ | 370 mm | 0,784 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Schrittmaß ≥ min. | 631,2 mm | ≥ | 590 mm | 0,935 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Schrittmaß ≤ max. | 631,2 mm | ≤ | 650 mm | 0,972 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |
| Laufbreite ≥ min. | 900 mm | ≥ | 800 mm | 0,889 | erfüllt | DIN 18065:2020-08, Grenzwerte für Wohngebäude mit höchstens zwei Wohnungen (nach Recherche 02) |

Der Vergleich erfolgt mit ungerundeten Werten.

Rundung des Ergebnisses: 1 Dezimalstelle, Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02.

### Gegenrechnung mit dem Rechenkern

| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |
|---|---|---:|---:|---|
| s | `b5_treppe_din18065.loese → s_mm (2 Dez.)` = 170,59 | 170,58823529411765 | 0,0018 | ja (Toleranz 0,005) |
| S | `b5_treppe_din18065.loese → schrittmass_mm (2 Dez.)` = 631,18 | 631,1764705882354 | 0,0035 | ja (Toleranz 0,005) |
| l_L | `b5_treppe_din18065.loese → lauflaenge_mm` = 4640 | 4640 | 0 | ja (Toleranz 1 · 10⁻⁹) |
| N_L | `ergebnisse.md: 68 Lösungen` = 68 | 68 | 0 | ja (Toleranz 0) |

### Hinweise

- Beispielrechnung für eine wissenschaftliche Arbeit; keine Rechts- oder Normauskunft, kein geprüfter bautechnischer Nachweis.

### Grafischer Nachweis

**Abbildung N-B5-01/schrittmass: Schrittmaß-Diagramm: alle zulässigen Lösungen**

![Schrittmaß-Diagramm: alle zulässigen Lösungen](svg/N-B5-01_schrittmass.svg)

Jede Spalte gehört zu einer Steigungszahl n (s = h/n); innerhalb der Spalte variiert a im Raster.

**Abbildung N-B5-01/schnitt: Treppenschnitt der gewählten Lösung (17 Steigungen)** (Maßstab 1:50)

![Treppenschnitt der gewählten Lösung (17 Steigungen)](svg/N-B5-01_schnitt.svg)

Stufenprofil schematisch; Laufplatte und Stufenstärke nicht bemessen.


### Rückverfolgbarkeit

- Hash (SHA-256): `0c03e40e3563f5590db3af9ee7411b3d205adb916f08fa4196497d3d0a8fbedb`
- Umfang: kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung
- Umgebung: Python 3.11.15, Modul nachweis 1.0.0, Einheiten: pint, Grafik: matplotlib, numpy 2.4.6, pint 0.25.3, matplotlib 3.11.2, shapely 2.1.2, ifcopenshell 0.8.5, ifctester 0.8.5
- Zeitstempel: nicht gesetzt (deterministischer Lauf)


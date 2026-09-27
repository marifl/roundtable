# IDS-Prüfbericht: wandelement_fehlerhaft.ifc (Fall: fehlerhaft)

IDS: `holzrahmenbau.ids` · Ergebnis: **nicht bestanden**

| ID | Spezifikation | anwendbar | fehlerhaft | Status |
|---|---|---:|---:|---|
| HRB-01 | HRB-01 Außenwand: U-Wert höchstens 0,20 W/(m²K) | 1 | 1 | ✘ |
| HRB-02 | HRB-02 Wand: Außen/Innen und Tragwirkung angegeben | 1 | 0 | ✔ |
| HRB-03 | HRB-03 Wand: Klassifikation nach DIN 276 (KG 33x) | 1 | 1 | ✘ |
| HRB-04 | HRB-04 Wand: Material (Schichtaufbau) zugeordnet | 1 | 0 | ✔ |
| HRB-05 | HRB-05 Ständer: Material KVH C24 | 15 | 1 | ✘ |
| HRB-06 | HRB-06 Hölzer: Länge und Nettovolumen als Menge | 18 | 0 | ✔ |
| HRB-07 | HRB-07 Hölzer, Platten, Dämmung: Teil einer Wand (IfcRelAggregates) | 41 | 0 | ✔ |
| HRB-08 | HRB-08 Verbindungsmitteltyp: Nenndurchmesser und Nennlänge | 1 | 1 | ✘ |
| HRB-09 | HRB-09 Verbindungsmittel: Nenndurchmesser am Exemplar | 176 | 1 | ✘ |
| HRB-10 | HRB-10 Gefachdämmung: Dämmstoff zugeordnet | 12 | 0 | ✔ |
| HRB-11 | HRB-11 Keine unklassifizierten Proxy-Elemente | 1 | 0 | ✘ |

## Fehlerdetails (max. 3 je Anforderung)

- HRB-01: IfcWall „Außenwand Nord, Element 1“ – The property value "0.25" does not match the requirements
- HRB-03: IfcWall „Außenwand Nord, Element 1“ – The entity has no classification
- HRB-05: IfcMember „Ständer R2“ – The entity has no material
- HRB-08: IfcMechanicalFastenerType „Spanplattenschraube 4,0x50“ – The attribute value "None" is empty
- HRB-09: IfcMechanicalFastener „Spanplattenschraube 4,0x50 #1“ – The attribute value "20.0" does not match the requirement
- HRB-11: Das Modell enthält kein IfcBuildingElementProxy (jedes Bauteil hat eine fachliche IFC-Klasse). (Anwendbarkeit verletzt: 1 Elemente gefunden)

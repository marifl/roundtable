# Recherche 05: Energie, Statik, Brand/Schall, Kosten, Viewer

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft, **[U]** = unsicher.

## Ergebnis in 5 Punkten

1. **Das GEG ist jetzt das GModG** (BGBl. 2026 I Nr. 226). Die EPBD-Stufe mit neuen Referenzgebäuden und Ökobilanzpflicht folgt. Rechenkerne brauchen deshalb **Regelwerk-Profile**.
2. **Einen offenen Rechenkern für DIN V 18599 gibt es nicht.** Live laufen H'T (exakt) plus Modellgebäudeverfahren plus Monatsbilanz-Näherung. Für den Nachweis wird der Fraunhofer-IBP-Kern lizenziert oder an eine Nachweissoftware exportiert.
3. **Statik:** PyNite (MIT) als FE-Kern, eurocodepy (LGPL) für EC5. Der deutsche Nationale Anhang muss ergänzt werden, keine Bibliothek hat ihn.
4. **Kosten:** Übernehmen lassen sich IfcOpenShell `ifc5d`/`api.cost`, `gaeb` (MIT) und ÖKOBAUDAT (frei, API).
5. **Viewer:** web-ifc (MPL) + @thatopen/components (MIT) + ifctester. xeokit ist AGPL, deshalb meiden.

## GModG: was gilt, was kommt

- **Gilt** [V]:
  - § 15: Primärenergie ≤ 0,55 × Referenzgebäude.
  - § 16: H'T ≤ 1,0 × Referenzgebäude.
  - § 20: DIN V 18599:2018-09.
  - § 31 mit Anlage 5: Modellgebäudeverfahren.
  - U-Werte nach DIN 4108-4:2017-03 und DIN EN ISO 6946:2008-04.
  - DIN V 4108-6/4701-10 ist für Wohngebäude seit 31.12.2023 nicht mehr zulässig.
- **Kommt** (EPBD-Teil, etwa 6 Monate nach Verkündung [U]):
  - DIN/TS 18599:2025-10
  - neue Referenzgebäude und Primärenergiefaktoren
  - Bilanzbezugsfläche nach DIN SPEC 91606:2026-07
  - Pflicht zur Ökobilanz nach § 7
  - Nullemissionsgebäude ab 2030

## 1. Energie

| Baustein | Liefert | IFC | Lizenz | Urteil |
|---|---|---|---|---|
| Fraunhofer IBP18599kernel | validierter 18599-Kern | nein | kommerziell [V] | für den Nachweis lizenzieren |
| **Modellgebäudeverfahren** (§ 31, Anl. 5) | Nachweis ohne Rechnung. Nur für Wohngebäude ohne Klimaanlage, 115–2.300 m² beheizte BGF, ≤ 6 Geschosse | – | Gesetz | **übernehmen** als Schnellcheck |
| bim2sim https://github.com/BIM2SIM/bim2sim | IFC → TEASER/Modelica/EnergyPlus; braucht Space Boundaries 2nd Level | ja | LGPL-3.0 [V] | später für Detailsimulation |
| IFC2SB (RWTH-E3D) | erzeugt Space Boundaries aus Geometrie | ja | GPL-3.0 [V] | nur als Vorlage |
| pyBuildingEnergy (EURAC) | ISO 52016-1 | nein | BSD-3 [V] | Referenz für eine Monatsbilanz |
| DIBS (IWU) | ISO 13790 5R1C, für Nichtwohngebäude | nein | MIT [V] | Vorlage |
| Honeybee-energy | EnergyPlus-Wrapper | nein | **AGPL** [V] | meiden |
| glaser (anssilaukkarinen) | Tauwasser nach ISO 13788 | – | MIT [V] | adaptieren (bekannter Bug) |
| ifc_hygrothermal | Glaser direkt aus IfcMaterialLayerSetUsage | ja | GPL-3.0 [V] | Vorlage |

- **U-Wert inhomogen nach ISO 6946:** Mittelwert aus R_upper und R_lower mit Holzanteil. Selbst bauen, etwa 1–2 Tage.
- **Materialkennwerte:** DIN 4108-4 und ISO 10456 sind kostenpflichtig. Freier Ersatz:
  - dataholz.eu mit λ, μ, ρ, c je Baustoff [V]
  - Leistungserklärungen der Hersteller

## 2. Statik

| Baustein | Lizenz | Urteil |
|---|---|---|
| **PyNite** (3D-FE) | MIT [V] | übernehmen |
| **eurocodepy** (EC5: kmod, GZT, Schwingung) | LGPL-3.0 [V] | adaptieren, DE-NA ergänzen |
| Ourocode (EC0/1/5, Brand, frz. NA) | Apache-2.0 [V] | adaptieren, NA austauschen |
| anaStruct (2D-FE) | LGPL-3.0 [V] | Alternative |
| OpenSees | nur nichtkommerziell [V] | ausschließen |
| compas_timber | MIT [V] | nur Geometrie und BTLx, keine Bemessung |

- **Vorbemessungstabellen zur Validierung**, frei als PDF oder Tool [V]:
  - Informationsdienst Holz „KVH und Balkenschichtholz“ (Deckenbalken, Stützen, Sparren)
  - Vorbemessung auf kvh.eu
  - van Roje XWORKS (BSP, DIN-NA)
  - STEICO-XPRESS, Finnwood, Stora Enso Calculatis
- Die Tabellenwerte sind geschützt [U]. Deshalb nur zur Validierung verwenden und selbst rechnen.

## 3. Brand- und Schallschutz

- **dataholz.eu:** REI (für DE: F nach DIN 4102-4), U, Rw, Ln,w, Masse und Öko-Kennwerte je Aufbau, z. B. awrhhi01a mit REI 45/30, U 0,22, Rw 50 dB [V]. Adaptieren, die Lizenz vorher anfragen.
- DIN 4102-4 und DIN 4109-33 sind kostenpflichtig. Ein Open-Source-Tool gibt es nicht; regelbasiert selbst bauen.
- **EFH-Einordnung** [U]:
  - GK 1: keine Brandschutzanforderung an tragende Wände.
  - GK 2/3: feuerhemmend.
  - DIN 4109-1 gilt nicht innerhalb der eigenen Wohnung.
  - Relevant sind Außenlärm und die Trennbauteile bei Doppel- und Reihenhäusern.

## 4. Kosten, Mengen, Ökobilanz

| Baustein | Lizenz | Urteil |
|---|---|---|
| **IfcOpenShell `ifc5d` / `api.cost`**: IfcCostSchedule, verknüpft mit Qto_*BaseQuantities | LGPL-3.0 [V] | übernehmen |
| **gaeb** (PyPI): DA XML 2.0–3.3, XSD-Validierung | MIT [V] | übernehmen |
| pyGAEB, openbim-gaeb (Rust) | MIT [V] | Alternativen |
| **ÖKOBAUDAT**: soda4LCA-API `https://www.oekobaudat.de/OEKOBAU.DAT/resource`, CSV, EN 15804+A2 | frei mit Quellenangabe [V] | übernehmen |
| eLCA (BBSR) | AGPL-3.0 [V] | nur Referenz |
| BKI | kostenpflichtig [V] | lizenzieren oder eigene Kennwerte |
| QNG-Zielwerte: PLUS ≤ 24, PREMIUM ≤ 20 kg CO₂e/(m²a) | [U] | als Zielwerte, Zertifizierung bleibt extern |

## 5. Viewer und IDS

| Baustein | Lizenz | Urteil |
|---|---|---|
| **web-ifc** | MPL-2.0 [V] | übernehmen |
| **@thatopen/components** | MIT [V] | übernehmen |
| **ifctester** (IfcOpenShell) | LGPL [V] | übernehmen |
| IfcOpenShell WASM + `ifcopenshell-ids` | LGPL [V] | adaptieren, in einem Web Worker laden |
| IDS-Audit-tool (buildingSMART, .NET) | MIT [V] | serverseitig übernehmen |
| xeokit-sdk | **AGPL** [V] | meiden |

- **IDS 1.0** ist seit 01.06.2024 offizieller Standard von buildingSMART [V].

## Lizenzfallen auf einen Blick

- **AGPL:** xeokit, Honeybee, eLCA; außerdem FloorPlan6 und xPlanBox (siehe Recherchen 02 und 03).
- **GPL:** IFC2SB, ifc_hygrothermal.
- **Nichtkommerziell:** OpenSees.
- **Kostenpflichtige Normen und Tabellen:** DIN 4108-4, ISO 10456, DIN 4102-4, DIN 4109-33, BKI.

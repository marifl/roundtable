# Spezifikation der App

Maschinenlesbare Vorgaben, die aus den Kapiteln der Arbeit abgeleitet sind. Sie sind die verbindliche Grundlage für die Implementierung.

| Datei | Inhalt | Quelle |
|---|---|---|
| `ifc-mapping.csv` | Bauteil → IFC-Klasse, PredefinedType, Psets, Pflicht je Reifegrad P/R/A | Kap. 8 |
| `regel.schema.json` | Schema einer Regel (R1–R4) | Kap. 9 |
| `regelkatalog.yaml` | formalisierte Regeln mit Quelle, Fassung, Profil, Prüffunktion | Kap. 9, 9a, 13–18 |
| `regelprofile.yaml` | Gebäudetyp × Regelbereich | Kap. 9a |
| `empfehlungen.yaml` | Empfehlungen R5 mit Evidenzgrad, Kulturprofile, Ausschlussliste | Kap. 9b |
| `module.yaml` | 21 Module mit Zweck, Schnittstellen, Bausteinen und Lizenz, zugeordnete ANF | Kap. 7 |
| `regelkatalog-<kapitel>.yaml` | kapitelbezogene Regelkataloge im selben Schema | Kap. 6, 13, 14, 14a, 14b |
| `anforderungen_extrahieren.py` | erzeugt `anforderungen.csv` aus den ANF-Tabellen aller Kapitel | Kap. 6 |
| `anforderungen.csv` | alle `ANF-*` mit Priorität, Abnahmekriterium, Modul, Test | alle Kapitel, Kap. 23 |
| `datenlieferungen.csv` | alle `DAT-*` (von Regnauer benötigt) | alle Kapitel |

Regeln: Jede Zeile nennt ihre Quelle (Kapitel, Key im Literaturverzeichnis). Werte mit Status `U` sind vor dem Produktivbetrieb zu bestätigen.

# Referenzdatenbank

Automatisch erzeugt von `../referenzdatenbank.py`. Nicht von Hand bearbeiten; Änderungen in den Quelldateien vornehmen und das Skript neu ausführen.

## Stand

| Inhalt | Anzahl |
|---|---|
| Quellen | 811 |
| einzeln bewertet | 811 |
| zweitbewertet (blind) | 0 |
| Abstract-Datensätze | 734 |
| davon mit Originalabstract | 535 |

Open-Access-Status: closed: 314, green: 109, gold: 98, hybrid: 73, bronze: 61, frei (amtlich): 39, unbekannt: 36, diamond: 4

## Dateien

- `referenzdatenbank.sqlite`: Tabellen `quellen`, `bewertung`, `zweitbewertung`, `abstract`; Sichten `kernbestand`, `ohne_abstract`.
  Beispiel: `sqlite3 referenzdatenbank.sqlite "SELECT id,key,P FROM kernbestand LIMIT 20"`
- `referenzdatenbank.bib`: für Zotero, JabRef oder Citavi. Enthält `abstract`, `keywords` (Q-ID, Relevanz je Forschungsfrage, Nutzung, Qualität, Kernbestand) und `annote` (Begründung der Passung).
- `referenzdatenbank.json`: CSL-JSON für Zotero und Pandoc.

## Import in Zotero

1. Datei → Importieren → `referenzdatenbank.bib`
2. Alle Einträge markieren → Rechtsklick → „Verfügbare PDFs suchen“. Zotero lädt frei zugängliche Volltexte legal über Unpaywall.
3. Schlagwort `Kernbestand` filtert die 1–2 Dutzend Quellen je Kapitel, die zuerst gelesen werden sollten.

## Rechtlicher Hinweis

Abstracts sind urheberrechtlich geschützte Texte der Verlage bzw. Autoren. Sie liegen hier zur wissenschaftlichen Arbeit vor, mit Herkunft je Datensatz (`abstract_quelle`, `abstract_url`). Das Repository privat halten. Volltexte werden nicht im Repository gespeichert, sondern nur als Link (`oa_url`) bei frei zugänglichen Fassungen.

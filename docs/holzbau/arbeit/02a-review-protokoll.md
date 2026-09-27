# 2a Protokoll der systematischen Literatur- und Quellenrecherche

Status: v0.1 (27.09.2026). Dieses Protokoll gehört zu Kapitel 2 (Forschungsdesign) und macht die Recherche nachvollziehbar und wiederholbar.

## 2a.1 Ausgangslage und Anspruch

Die Arbeit setzt keine Vorkenntnis bestimmter Autoren oder Schulen voraus. Daraus folgen zwei Anforderungen:

- Die Literatur ist **vollständig systematisch zu erschließen**. Das gilt ausdrücklich auch für die Architekturpsychologie und für Forschung aus dem regionalen Umfeld (Rosenheim, Holzbau in Bayern).
- **Jede Quelle ist einzeln auf ihre Passung zur Fragestellung zu bewerten.** Eine Quelle zählt nicht deshalb, weil sie gefunden wurde, sondern weil ihr Beitrag zu einer Forschungsfrage begründet ist.

Das Vorgehen folgt drei Anleitungen:

- Richtlinien für systematische Reviews in der Softwaretechnik (Kitchenham & Charters 2007)
- Schneeballverfahren (Wohlin 2014)
- Berichtsstandard PRISMA 2020 (Page et al. 2021), sinngemäß angewandt auf ein Feld, das Wissenschaft, Normen, Gesetze und Technik verbindet

## 2a.2 Quellenarten

| Art | Beispiele | Prüfweg |
|---|---|---|
| W – Wissenschaft, begutachtet | Journal, Konferenz, Dissertation | DOI über Crossref bzw. Verlag oder Repositorium |
| N – Norm, Gesetz, Richtlinie | BayBO, DIN, VDI, DWA, ZVDH | amtliche Fundstelle bzw. Ausgabe beim Normgeber |
| G – graue Literatur | Forschungsberichte, Leitfäden, Herstellerunterlagen | Primärquelle beim Herausgeber |
| T – Technik | Software, Datenstandards, Datensätze | Repository, Lizenzdatei, Spezifikation |

## 2a.3 Recherchestrategie

1. **Themenfelder:** abgeleitet aus den Forschungsfragen FF1–FF6. Die Recherchen 01–20 decken sie ab (`../recherche/`).
2. **Suchräume:**
   - Crossref, OpenAlex
   - Verlagsportale: Elsevier, Springer, Taylor & Francis, ASCE, MDPI
   - Repositorien: mediaTUM, ETH Research Collection, DiVA, arXiv
   - amtliche Portale: gesetze-bayern.de, gesetze-im-internet.de, EUR-Lex
   - Normgeber, Verbände, Hersteller
3. **Schneeballverfahren:** vorwärts (Zitierende) und rückwärts (Zitierte), ausgehend von den am höchsten bewerteten Quellen (Abschnitt 2a.6). Es endet, wenn eine Runde keine neue Quelle mit Relevanz ≥ 2 mehr liefert.
4. **Lücken ohne Vorwissen:** Gezielt durchsucht werden:
   - die Architekturpsychologie, auch deutschsprachig
   - Forschung an der TH Rosenheim, am ift Rosenheim und an Hochschulen mit Holzbauschwerpunkt
   - Forschung mit Bezug zu bayerischen Fertighausherstellern

## 2a.4 Ein- und Ausschlusskriterien

**Eingeschlossen werden Quellen, die:**
- mindestens eine Forschungsfrage mit Relevanz ≥ 1 berühren (Abschnitt 2a.5),
- existent und prüfbar sind (Autor, Jahr, Titel, Fundstelle),
- bei Normen und Gesetzen in der zum 27.09.2026 geltenden Fassung vorliegen oder historisch begründet sind (z. B. Vollgeschoss nach BayBO 2007).

**Ausgeschlossen werden Quellen:**
- die nicht verifizierbar sind; sie werden als „nicht verifizierte Hinweise“ geführt, aber nie zitiert,
- ohne Primärquelle, wenn eine Primärquelle existiert.

Pseudowissenschaftliche Aussagen, etwa zu Erdstrahlen, werden nicht als Beleg zitiert. Sie erscheinen nur als Gegenstand der Abgrenzung.

## 2a.5 Schema für die Bewertung der Passung

Jede Quelle erhält eine Zeile in `literatur/quellen-bewertung.csv` mit folgenden Feldern:

| Feld | Werte | Bedeutung |
|---|---|---|
| `id`, `key` | Q001 …, BibTeX-Key | Verweis auf `quellen-master.csv` |
| `art` | W / N / G / T | Quellenart |
| `ff1` … `ff6` | 0–3 | Relevanz je Forschungsfrage: 0 = keine, 1 = Kontext, 2 = stützt ein Argument, 3 = trägt ein zentrales Argument oder liefert einen übernehmbaren Baustein |
| `beitrag` | Methode / Regel / Daten / Werkzeug / Evaluation / Befund / Kontext | Art des Beitrags |
| `qualitaet` | A / B / C / D | A: begutachtete Übersichtsarbeit, Meta-Analyse oder geltendes Recht bzw. Norm; B: begutachtete Einzelstudie oder Dissertation; C: graue Literatur, Herstellerangabe; D: Tradition oder Meinung ohne empirische Prüfung |
| `uebertragbarkeit` | 0–2 | auf Deutschland/Bayern, Holzbau und Fertighaus: 0 = nicht, 1 = mit Anpassung, 2 = direkt |
| `nutzung` | übernehmen / adaptieren / abgrenzen / Kontext / verwerfen | Rolle in der Arbeit |
| `kapitel` | z. B. 5.2; 9b | Verwendungsort |
| `begruendung` | 1–3 Sätze | Warum diese Quelle für diese Fragestellung passt oder nicht |
| `verifiziert` | V / U | Status der bibliografischen Prüfung |

**Gesamtrelevanz:** `R = max(ff1 … ff6)`.

**Priorität:** `P = R + uebertragbarkeit + Qualitätspunkte`. Dabei ergibt die Qualität A 2 Punkte, B 1,5, C 1 und D 0.

Quellen mit P ≥ 5 bilden den Kernbestand. Sie sind Ausgangspunkt des Schneeballverfahrens und werden im Text vertieft diskutiert.

## 2a.6 Ablauf

1. Alle Literaturlisten zusammenführen und Dubletten entfernen → `quellen-master.csv`. Stand heute: 393 eindeutige Einträge.
2. Jede Quelle einzeln nach 2a.5 bewerten, nach Möglichkeit anhand von Abstract oder Volltext → `quellen-bewertung.csv`.
3. Lückenrecherche nach 2a.3 Nr. 4.
4. Schneeballverfahren ab dem Kernbestand.
5. Flussdiagramm nach PRISMA: gefunden → geprüft → eingeschlossen → Kernbestand, mit Zahlen je Schritt.
6. Kapitel 5 wird aus dem Kernbestand geschrieben, weitere Kapitel beziehen ihre Quellen über das Feld `kapitel`.

## 2a.7 Grenzen

- **Proxy-Sperren:** Einige Recherchen konnten Crossref nicht direkt erreichen. Solche DOIs sind über Verlagsseiten geprüft und mit ihrem Prüfweg im Feld `note` markiert. Vor der Abgabe läuft ein zentraler Abgleich mit Crossref.
- **Kostenpflichtige Normen:** DIN-, VDI- und DWA-Volltexte liegen nicht vor. Kennwerte stammen aus amtlichen Verweisen, Entwürfen oder Sekundärquellen und sind entsprechend markiert.
- **Bewertung durch einen einzelnen Bewerter:** Die Passung wird zunächst von einer Instanz bewertet. Für den Kernbestand ist eine zweite, unabhängige Bewertung vorgesehen. Die Übereinstimmung wird mit Cohens κ gemessen.

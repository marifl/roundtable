# Gemeinsamer Auftrag für das Schreiben eines Kapitels

Gilt für jedes Kapitel der Arbeit. Das jeweilige Kapitel und sein Material nennt der Einzelauftrag.

## Zweck

Die Arbeit ist die **fachliche Grundlage einer App, die am Ende voll funktionieren soll**. Sie ist keine rein wissenschaftliche Auseinandersetzung. Jedes Kapitel liefert deshalb:

1. **Den Fachteil:** Deutsch, wissenschaftlicher Stil auf Doktorarbeitsniveau, jede Aussage belegt, kritisch gewürdigt.
2. **Einen Abschnitt „Umsetzungsvorgaben für die App“** am Ende mit:
   - **Anforderungen** `ANF-<Kapitel>-<Nr>` in einer Tabelle mit den Spalten ID, Muss/Soll, Beschreibung, Beleg im Kapitel, Abnahmekriterium. Das Abnahmekriterium ist prüfbar und möglichst als Testfall formuliert, zum Beispiel „Eingabe X ⇒ Ausgabe Y ± Toleranz“.
   - **Datenstrukturen/Parameter** in einer Tabelle mit den Spalten Feld, Typ, Einheit, Wertebereich, Quelle.
   - **Datenlieferungen von Regnauer** `DAT-<Kapitel>-<Nr>`.
   - **Maschinenlesbare Dateien** in `spezifikation/`, soweit der Einzelauftrag sie nennt. Jede Datei wird mit Python auf Parsebarkeit geprüft.

## Stil und Form

- Stilreferenz ist `04-rechtlicher-normativer-rahmen.md`. Übernommen werden:
  - Ton
  - Zitierweise `[@key]`
  - Beispielkästen mit echten Zahlen
  - Tabellen
  - nummerierte Entscheidungen `E<Kap>.<Nr>`, wo Designentscheidungen fallen
- Echte Zahlen aus den Prototypen in `beispiele/` verwenden (`ergebnisse.md`, `ausgabe/*.json`, Tests). Keine Zahlen erfinden.
- Status erhalten: [V] für verifiziert, [U] für unsicher.
- Zitieren nur mit Keys, die in `literatur/lit-*.bib` existieren (per grep prüfen).
- Aussagen über eine Quelle nur, wenn Abstract (`literatur/referenzdatenbank/referenzdatenbank.sqlite`, Tabelle `abstract`), Bewertung (`literatur/quellen-bewertung.csv`, Spalte `begruendung`) oder Recherche (`../recherche/*.md`) sie stützen.
- Querverweise auf andere Kapitel in der Form „Kapitel 9“ bzw. „Abschnitt 8.4“.
- Am Ende der Datei stehen die Liste der verwendeten Keys und das Ergebnis eines Python-Key-Checks. Das Ergebnis muss „0 fehlend“ lauten.

## Material, das immer gilt

- `../00-zielbild.md`
- `00-gliederung.md`
- die fertigen Kapitel: 01, 02, 03, 04, 05, 07a, 08, 09, 09a, 09b; nur lesen, nicht ändern
- `spezifikation/*`: IFC-Mapping, Regelkatalog, Regelprofile, Empfehlungen. Konsistent bleiben: IDs weiterverwenden, neue Regeln im selben Schema anlegen, `regel.schema.json` einhalten.

## Arbeitsweise

- Netzrecherche ist nicht nötig. Wenn doch, dann nur sparsam über das via ToolSearch geladene `mcp__Exa__web_fetch_exa`, höchstens 10 Abrufe.
- Andere Agenten schreiben parallel. Nur die eigenen Dateien anlegen oder ändern. Zusätzliche Regeln kommen in eine eigene Datei `spezifikation/regelkatalog-<kapitel>.yaml`, nicht in den gemeinsamen `regelkatalog.yaml`.
- NICHT committen.
- Rückmeldung an den Auftraggeber mit höchstens 100 Wörtern: Wortzahl, Anzahl ANF/DAT, Key-Check, erzeugte Spezifikationsdateien, wichtigste Lücken.

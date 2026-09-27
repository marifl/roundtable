# Auftrag: Abstracts und Open-Access-Status erfassen

Ziel: echte Referenzdatenbank. Für jede Quelle aus `../quellen-master.csv` im zugewiesenen ID-Bereich eine Zeile JSON (JSON Lines, UTF-8) in `teil-<N>.jsonl`:

{"id":"Q001","key":"...","abstract":"<Originaltext des Abstracts, unverändert, in Originalsprache>","abstract_quelle":"openalex|crossref|verlag|pubmed|arxiv|repositorium|amtlich|keine","abstract_url":"<URL, von der der Text stammt>","sprache":"en|de|...","oa_status":"gold|green|hybrid|bronze|closed|unbekannt|frei (amtlich)","oa_url":"<URL zu frei zugänglichem Volltext oder leer>","oa_lizenz":"cc-by|cc-by-nc|...|unbekannt|amtliches Werk","keywords":["<Autoren-Keywords falls vorhanden>"],"abgerufen":"2026-09-27","hinweis":"<optional>"}

Regeln:
- Abstract NIE selbst formulieren oder zusammenfassen. Nur Originaltext. Wenn keiner existiert (Norm, Gesetz, Buch): "abstract":"" und "abstract_quelle":"keine"; bei Normen/Gesetzen optional den amtlichen Kurzinhalt/Anwendungsbereich wörtlich mit Quelle, sonst leer.
- OpenAlex liefert abstract_inverted_index: in Klartext zurückwandeln (Wörter nach Positionen sortieren).
- Direkte API-Zugriffe (api.openalex.org, api.crossref.org, api.unpaywall.org) sind im Netz gesperrt: über via ToolSearch geladenes mcp__Exa__web_fetch_exa abrufen (z. B. https://api.openalex.org/works/doi:<doi>), sonst Verlagsseite/PubMed/arXiv.
- OA-Status aus OpenAlex (open_access.oa_status, best_oa_location.pdf_url/landing_page_url, license).
- Jede Zeile valide JSON; am Ende mit Python prüfen: Anzahl Zeilen = Anzahl IDs im Bereich, jede ID genau einmal.

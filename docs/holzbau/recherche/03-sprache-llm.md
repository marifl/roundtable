# Recherche 03: Sprache, Intent-Modell, Text-to-BIM

Stand: 27.09.2026. **[V]** = an Primärquelle geprüft, **[U]** = unsicher.

## Ergebnis in 5 Punkten

1. **Laya, Jev, Noul und Shapeshift gibt es.** Alle sind seit etwa Mitte September 2026 öffentlich und damit sehr jung [V].
2. **Lücke im Konzept:** Jev und Laya beantworten typisierte Fragen, liefern aber keine Werte wie „1,20 m“ oder „35 Grad“. Diese Werte liest ein deutscher Parser für Zahlen und Einheiten aus, oder ein LLM mit JSON-Schema.
3. **Laya braucht Fine-Tuning und Kalibrierung.** Ohne beides liegt die Genauigkeit fast auf Zufallsniveau.
4. **Spracherkennung:** Voxtral Realtime (Streaming) oder Parakeet v3 (Fachbegriff-Boosting) passen besser als Whisper.
5. **IFC und Holzbau:** IfcMCP/IfcOpenShell und compas_timber (mit BTLx) übernehmen, nicht selbst schreiben.

## 1. Intent-Schicht

### Jev [V]
- „System One“-Entscheidungsmodell von TypeSafe AI.
  - **Eingabe:** `state` plus typisierte Fragen.
  - **Ausgabe:** typisierte Antworten mit Wahrscheinlichkeiten. Jev erzeugt keinen Text.
- **Fragetypen:** `choice` (1–255 Optionen), `score` (Rubrik mit 2–10 Stufen) und `boolean`/`noul`. Alle Fragen eines Calls laufen parallel.
- **Vercel AI Gateway:**
  - Modell-ID `typesafe-ai/jev`, Aufruf über `experimental_evaluate` ab AI SDK 7.0.105.
  - Alternativ per HTTP `/v1/evaluate`.
- **Kosten:** 0,042 $ pro 1 Mio. Input-Tokens, Output ist kostenlos. Zero Data Retention ist pro Request wählbar.
- **Quellen:**
  - https://vercel.com/changelog/typesafe-ai-jev-now-available-on-ai-gateway
  - https://vercel.com/kb/guide/typesafe-jev-and-ai-sdk
- **Grenzen:**
  - Englisch ist die Hauptsprache, andere Sprachen muss man selbst testen [U].
  - Early Access mit Warteliste [U].
  - Kein eigenes Fine-Tuning [U].
  - Jev läuft nur in der Cloud.

### Noul [V]
- Der Ja/Nein-Fragetyp von Jev. Er liefert **P(true) zwischen 0 und 1**, keinen Boolean.
- Den Schwellwert legt der eigene Code fest, pro Frage passend dazu, wie teuer ein Fehler ist.

### Laya [V]
- Convai Innovations, Apache 2.0: https://huggingface.co/convaiinnovations/laya-multilingual
- **Modell:**
  - Nicht-autoregressiv auf Basis von mmBERT-base, 322 Mio. Parameter.
  - 100+ Sprachen inkl. Deutsch. Kontext 1024 Tokens, bis 8192 möglich.
- **Tempo:** etwa 7 ms pro Frage bei 10 Fragen auf einer T4.
- **Fine-Tuning:** Kaggle-Notebook für 2×T4, Dauer etwa 4–5 h. Installation mit `pip install laya`.
- **Jev-kompatibel:** Ein selbst gehosteter HTTP-Server spricht das Jev-Protokoll.
- **Grenzen laut Model Card:**
  - Ohne Fine-Tuning: Genauigkeit 0,342, Zufall wäre 0,318.
  - Wird unkalibriert ausgeliefert.
  - `noul` meldet „true“ teils zu selten.
  - Mehr als etwa 20 `choice`-Optionen machen es deutlich schlechter.
- **Folge für den Intent-Katalog:** Intents hierarchisch aufteilen, erst die Gruppe wählen, dann den Intent. So bleibt jede Frage unter 20 Optionen.

### Shapeshift [V]
- MIT-Lizenz, Bun/Next.js: https://github.com/anishfn/shapeshift. Es gibt viele Forks; welches das Original ist, ist [U].
- Ein Jev-Call beantwortet 14 Fragen. Deterministischer Code berechnet die Werte.
- Offline übernimmt ein Keyword-Klassifikator als Fallback.

### Etablierte Alternativen für die Werte-Extraktion
- Structured Outputs mit JSON Schema.
- Constrained Decoding:
  - llama.cpp mit GBNF/JSON-Schema
  - XGrammar/Outlines in vLLM
  - Ollama `format`
- Bibliotheken: Instructor, BAML, Pydantic AI, AI SDK.

## 2. Lokale LLMs (Deutsch, Tool-Calling)

| Modell | Lizenz | VRAM Q4 (ca.) | Hinweis |
|---|---|---|---|
| Qwen3.5 9B / 27B / 35B-A3B [V] | Apache 2.0 | 6–8 / 16–20 GB [U] | 201 Sprachen, starkes Tool-Calling |
| Gemma 4 E4B / 26B-A4B / 31B [V] | Apache 2.0 [U] | 5–6 / 14–18 GB [U] | E2B/E4B nehmen auch Audio |
| Ministral 3 (3B/8B/14B) [V] | Apache 2.0 [U] | 8B: ca. 6 GB [U] | EU-Anbieter |
| Teuken-7B v0.4 [V] | Commercial/Research | ca. 5 GB | kaum Tool-Calling [U] |

- **Im Vercel AI Gateway** [V]:
  - Gemma 4 26B/31B
  - Ministral 3B/8B/14B, Mistral Small
  - `alibaba/qwen3.5-flash`
  - `typesafe-ai/jev`
- Laya läuft nicht über das Gateway.

## 3. Spracherkennung Deutsch

| Modell | Lizenz | Streaming | Fachbegriffe | Urteil |
|---|---|---|---|---|
| Voxtral Mini 4B Realtime 2602 [V] | Apache 2.0 | ja, 80–2400 ms; DE-WER 6,19 % bei 480 ms | [U] | übernehmen (Favorit) |
| Parakeet-TDT-0.6b-v3 [V] | CC-BY-4.0 | ja | Phrase Boosting per Liste | übernehmen, wenn Fachbegriffe entscheiden |
| Canary-1b-v2 [V] | [U] | ja | Boosting | Alternative |
| Qwen3-ASR 0.6B/1.7B [V] | [U] | über vLLM | [U] | Alternative |
| Whisper large-v3-turbo (+ primeline German) [V] | MIT | nur in Stücken | `hotwords`, `initial_prompt` | Fallback |
| Kyutai STT, Moonshine [V] | – | – | – | ungeeignet (kein Deutsch) |

- **Deutsche Bau-Sprachdatensätze:** keine gefunden.
- **Stattdessen selbst bauen:**
  - eigenes Testset aus Aufnahmen plus TTS-Synthese
  - Fachbegriff-Liste für Boosting: Kniestock, Gaube, Pfette, Sparren, OSB, Schwelle
  - unscharfe Nachkorrektur gegen diese Liste

## 4. Vorbilder Text/Sprache → BIM

| Projekt | Lizenz | Kern | Urteil |
|---|---|---|---|
| Text2BIM, TUM [V] https://github.com/dcy0577/Text2BIM | MIT | LLM-Agenten plus Regelprüf-Schleife (Solibri/BCF) | Muster adaptieren |
| NADIA-S, arXiv 2409.18345 [V] | kein Code | Speech-to-BIM auf Revit | Referenz |
| CAADRIA 2025, caadria2025_420 [V] | – | Whisper → Intent → Parameter → Grasshopper, 78 % weniger Modellierzeit | nächster Präzedenzfall |
| IfcMCP / `ifcopenshell-mcp` 0.8.5 [V] https://docs.ifcopenshell.org/ifcmcp.html | LGPL-3.0 | IFC lesen, schreiben, prüfen | übernehmen |
| bonsai-mcp (Show2Instruct) [V] | MIT | Bonsai-Steuerung | adaptieren |
| compas_timber, ETH [V] | MIT | Balken, Platten, Verbindungen, BTLx-Export | übernehmen |

- **Holzbau-Konfiguratoren mit KI oder Sprache:** keine gefunden. Geprüft wurden myWeberHaus, Hanse, Haas, FingerHaus und Regnauer; alle arbeiten mit Formularen oder 3D. **Das ist die Marktlücke.**

## 5. Grundriss- und Möblierungs-Solver

- **Neuronale Generatoren:** wegen ihrer Lizenzen nicht nutzbar.
  - House-GAN++, HouseDiffusion und Graph2Plan sind nicht kommerziell oder ohne Lizenz.
  - RPLAN ist vermutlich nur nicht-kommerziell nutzbar [U].
- **FloorPlan6** [V]: AGPL-3.0, CP-SAT plus ArchiCAD. Nur als Referenz nutzen.
- **Möblierung:** AI2 Holodeck (Apache 2.0) [V] und Infinigen Indoors (BSD-3) [V]. Das Muster: LLM oder Regeln geben Constraints vor, ein Solver platziert.
- **Urteil: selbst bauen mit OR-Tools CP-SAT** (`add_no_overlap_2d`).

## Korrekturen am Konzept

1. Laya: Fine-Tuning und Kalibrierung sind Pflicht, `choice` unter 20 Optionen halten.
2. Jev: Englisch ist Hauptsprache, läuft nur in der Cloud, kein Fine-Tuning.
3. Noul: liefert eine Wahrscheinlichkeit, keinen Boolean. Schwellwerte legt der Code fest.
4. Neu im Konzept: ein deutscher Parser für Zahlen und Einheiten („eins zwanzig“, „einsdreißig“).
5. Spracherkennung auf Voxtral Realtime oder Parakeet v3 umstellen.
6. Für IFC IfcOpenShell/IfcMCP nutzen, für die Holzbauschicht compas_timber.
7. Für Grundriss und Möblierung einen regelbasierten Solver mit CP-SAT verwenden.

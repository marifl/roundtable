#!/usr/bin/env python3
"""Prüft intents.yaml, sprach-testset.jsonl und werteparser-grammatik.md (Kapitel 10)
und misst den B6-Prototyp am Testset. Aufruf:  python spezifikation/pruefe_sprache.py"""
import collections
import json
import re
import sys
import unicodedata
from pathlib import Path

import yaml

ARBEIT = Path(__file__).resolve().parent.parent
SPEZ = ARBEIT / "spezifikation"
sys.path.insert(0, str(ARBEIT / "beispiele"))
import b6_intent_pipeline as b6  # noqa: E402

fehler = []
kat = yaml.safe_load((SPEZ / "intents.yaml").read_text(encoding="utf-8"))
regeln = {r["id"] for r in yaml.safe_load((SPEZ / "regelkatalog.yaml").read_text(encoding="utf-8"))["regeln"]}
emp = yaml.safe_load((SPEZ / "empfehlungen.yaml").read_text(encoding="utf-8"))
regeln |= {r["id"] for r in emp["empfehlungen"]} | {r["id"] for r in emp["ausschlussliste"]}
slot_typen = set(kat["slot_typen"])
rk = set(kat["risikoklassen"])

# --- intents.yaml ----------------------------------------------------------------------
gruppen = kat["gruppen"]
if len(gruppen) > 19:
    fehler.append("mehr als 19 Gruppen")
q_gruppe = next(f for f in kat["globale_fragen"] if f["id"] == "q.gruppe")
if q_gruppe["optionen"] != [g["gruppe"] for g in gruppen]:
    fehler.append("q.gruppe passt nicht zu gruppen")
intents = {}
n_fragen = collections.Counter()
max_opt = 0
for g in gruppen:
    gf = g.get("frage", {})
    if gf.get("typ") != "choice" or gf.get("optionen") != [i["intent"] for i in g["intents"]]:
        fehler.append(f"{g['gruppe']}: Intent-Frage fehlt oder passt nicht")
    else:
        n_fragen["choice"] += 1
    if len(g["intents"]) > 19:
        fehler.append(f"{g['gruppe']}: mehr als 19 Intents")
    max_opt = max(max_opt, len(g["intents"]))
    for i in g["intents"]:
        iid = i["intent"]
        if iid in intents:
            fehler.append(f"doppelter Intent {iid}")
        intents[iid] = (g["gruppe"], i)
        if len(i["beispielsaetze"]) < 3:
            fehler.append(f"{iid}: < 3 Beispielsätze")
        if i["risikoklasse"] not in rk:
            fehler.append(f"{iid}: Risikoklasse")
        for r in i["regeln"]:
            if r not in regeln:
                fehler.append(f"{iid}: unbekannte Regel {r}")
        ids = [f["id"] for f in i["fragen"]]
        if len(ids) != len(set(ids)):
            fehler.append(f"{iid}: doppelte Frage-ID")
        for f in i["fragen"]:
            n_fragen[f["typ"]] += 1
            if not 0 < f["schwelle"] < 1:
                fehler.append(f"{iid}/{f['id']}: Schwelle")
            if f["typ"] == "choice":
                max_opt = max(max_opt, len(f["optionen"]))
                if len(f["optionen"]) > 19:
                    fehler.append(f"{iid}/{f['id']}: > 19 Optionen")
            if f["typ"] == "score" and not 2 <= len(f["stufen"]) <= 10:
                fehler.append(f"{iid}/{f['id']}: Stufen")
        for s in i["slots"]:
            for t in s["typ"].split("|"):
                if t not in slot_typen:
                    fehler.append(f"{iid}/{s['name']}: Slottyp {t}")
            if s["typ"] == "enum" and s.get("quelle") == "modell" and s.get("frage") not in ids:
                fehler.append(f"{iid}/{s['name']}: enum ohne choice-Frage")
            if "wertebereich" in s:
                wb = s["wertebereich"]
                for bereich in (wb.values() if isinstance(wb, dict) else [wb]):
                    if not (len(bereich) == 2 and bereich[0] < bereich[1]):
                        fehler.append(f"{iid}/{s['name']}: Wertebereich")
        if not i["rueckfrage"]:
            fehler.append(f"{iid}: Rückfragetext fehlt")
for f in kat["globale_fragen"]:
    n_fragen[f["typ"]] += 1
beispiele = {unicodedata.normalize("NFC", b).lower().strip(" .?!") for _, i in intents.values() for b in i["beispielsaetze"]}

# --- Testset ----------------------------------------------------------------------------
zeilen = (SPEZ / "sprach-testset.jsonl").read_text(encoding="utf-8").splitlines()
tests = [json.loads(z) for z in zeilen if z.strip()]
if len(tests) < 150:
    fehler.append("Testset < 150")
ids = [t["id"] for t in tests]
if len(ids) != len(set(ids)):
    fehler.append("doppelte Test-IDs")
for t in tests:
    if t["intent"] not in intents:
        fehler.append(f"{t['id']}: Intent {t['intent']} unbekannt")
        continue
    g, i = intents[t["intent"]]
    if t["gruppe"] != g:
        fehler.append(f"{t['id']}: Gruppe")
    namen = {s["name"] for s in i["slots"]}
    for s in t["slots"]:
        if s not in namen:
            fehler.append(f"{t['id']}: Slot {s} nicht im Intent {t['intent']}")
    if unicodedata.normalize("NFC", t["satz"]).lower().strip(" .?!") in beispiele:
        fehler.append(f"{t['id']}: Satz ist Beispielsatz (Leckage)")

# --- Messung B6 am Testset --------------------------------------------------------------
state = b6.lade_state()
DIM = {"m": "laenge", "m²": "flaeche", "°": "winkel"}
mass = collections.Counter()
mass_kat = collections.defaultdict(lambda: [0, 0])
for t in tests:
    for sname, v in t["slots"].items():
        if not isinstance(v, dict) or "einheit" not in v or v.get("aus_kontext"):
            continue
        mass["alle_zahlslots"] += 1
        erkannt = b6.parse_masse(t["satz"])
        if "mehrdeutig" in v:
            ok = any(m.mehrdeutig for m in erkannt)
        elif v["einheit"] in DIM:
            mass["b6_dimension_unterstuetzt"] += 1
            ok = any(m.dim == DIM[v["einheit"]] and abs(m.wert - v["wert"]) < 1e-6 and not m.mehrdeutig for m in erkannt)
        else:
            ok = False
        mass["b6_richtig"] += ok
        for k in t["kategorien"]:
            mass_kat[k][0] += 1
            mass_kat[k][1] += ok
ref = collections.Counter()
ref_fehl = []
for t in tests:
    if "kontext_pflicht" in t["kategorien"]:
        continue
    for sname in ("raum", "objekt"):
        v = t["slots"].get(sname)
        if not isinstance(v, dict) or "aufloesung" not in v:
            continue
        ref["raumslots"] += 1
        a = b6.loese_raum(t["satz"], state)
        if v["aufloesung"] == "eindeutig":
            ok = a.status == "eindeutig" and a.raum_id == v["raum_id"]
        elif v["aufloesung"] == "mehrdeutig":
            ok = a.status == "mehrdeutig"
        else:
            ok = False
        ref["b6_richtig"] += ok
        if not ok:
            ref_fehl.append((t["id"], t["satz"], a.status, a.raum_id))

# --- EBNF in werteparser-grammatik.md ------------------------------------------------
md = (SPEZ / "werteparser-grammatik.md").read_text(encoding="utf-8")
bloecke = re.findall(r"```ebnf\n(.*?)```", md, re.S)
ebnf = re.sub(r"\(\*.*?\*\)", " ", "\n".join(bloecke), flags=re.S)
regeln_ebnf, verwendet = {}, set()
rest = ebnf
for teil in re.split(r";\s*(?=\n|$)", ebnf):
    teil = teil.strip()
    if not teil:
        continue
    if "=" not in teil:
        fehler.append(f"EBNF: keine Regel: {teil[:40]}")
        continue
    name, rumpf = teil.split("=", 1)
    name = name.strip()
    if not re.fullmatch(r"[a-z_0-9]+", name):
        fehler.append(f"EBNF: Regelname {name!r}")
    if name in regeln_ebnf:
        fehler.append(f"EBNF: {name} doppelt definiert")
    regeln_ebnf[name] = rumpf
    ohne = re.sub(r'"[^"]*"', " ", rumpf)
    ohne = re.sub(r"\?[^?]*\?", " ", ohne)
    if ohne.count("(") != ohne.count(")") or ohne.count("[") != ohne.count("]") or ohne.count("{") != ohne.count("}"):
        fehler.append(f"EBNF: Klammern in {name}")
    if rumpf.count('"') % 2:
        fehler.append(f"EBNF: Anführungszeichen in {name}")
    verwendet |= set(re.findall(r"\b[a-z_][a-z_0-9]*\b", ohne))
for v in sorted(verwendet - set(regeln_ebnf)):
    fehler.append(f"EBNF: {v} verwendet, nicht definiert")

# --- Ausgabe ----------------------------------------------------------------------------
print(f"intents.yaml: {len(gruppen)} Gruppen, {len(intents)} Intents, "
      f"{sum(len(i['beispielsaetze']) for _, i in intents.values())} Beispielsätze, "
      f"{sum(len(i['slots']) for _, i in intents.values())} Slots, Fragen {dict(n_fragen)}, max. Optionen je choice {max_opt}, "
      f"{len(kat['fachbegriffe']['begriffe'])} Fachbegriffe")
print("Risikoklassen:", dict(collections.Counter(i["risikoklasse"] for _, i in intents.values())))
print(f"Testset: {len(tests)} Sätze, {len({t['intent'] for t in tests})} Intents abgedeckt, "
      f"Gruppen {dict(collections.Counter(t['gruppe'] for t in tests))}")
print("erwartet:", dict(collections.Counter(t["erwartet"] for t in tests)))
kc = collections.Counter(k for t in tests for k in t["kategorien"])
print("Kategorien (Auswahl):", {k: kc[k] for k in ("fachbegriff", "zahlwort", "umgangssprache", "mehrdeutig_referenz", "mehrdeutig_wert", "dialekt", "asr_artefakt", "korrektur", "anapher", "vage", "abfrage", "b6")})
print(f"B6-Werteparser: {mass['b6_richtig']} von {mass['alle_zahlslots']} Zahlslots richtig "
      f"(Dimension von B6 unterstützt, m, m², °: {mass['b6_dimension_unterstuetzt']} Slots)")
for k in ("zusammenschreibung", "tausenderpunkt", "einheit_fehlt", "dialekt", "einheit_neu", "zahlwort_gross", "mal_ausdruck", "umgangssprache", "komma", "asr_artefakt", "mehrdeutig_wert"):
    if k in mass_kat:
        print(f"   {k}: {mass_kat[k][1]}/{mass_kat[k][0]}")
print(f"B6-Raumreferenz: {ref['b6_richtig']} von {ref['raumslots']} Raumslots richtig (ohne Kontextfälle)")
for f in ref_fehl:
    print("   falsch:", f)
print(f"EBNF: {len(bloecke)} Blöcke, {len(regeln_ebnf)} Regeln, {len(verwendet)} verwendete Nichtterminale")
print("Fehler:", len(fehler))
for f in fehler:
    print("  -", f)
sys.exit(1 if fehler else 0)

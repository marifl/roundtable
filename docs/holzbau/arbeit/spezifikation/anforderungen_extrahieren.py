#!/usr/bin/env python3
"""Extrahiert alle ANF-* und DAT-* aus den Markdown-Tabellen der Kapitel und schreibt
spezifikation/anforderungen.csv und spezifikation/datenlieferungen.csv (Kapitel 6.7.4).

Aufruf aus arbeit/:  python3 spezifikation/anforderungen_extrahieren.py

- Anforderungen: Zeilen `| ANF-… | Muss/Soll | Beschreibung | Beleg | Abnahmekriterium |`
- Modul:        aus spezifikation/module.yaml (jede ANF genau einem Modul zugeordnet)
- quelle_keys:  alle [@key] in den Abschnitten bzw. Entscheidungen (E…), die die Spalte
                „Beleg“ nennt; nur Keys, die in literatur/lit-*.bib stehen
- phase, rolle: Zuordnung unten (Kapitel 6.2, Tabelle 6.1), vorläufig
- test:         vorläufiger Pfad tests/<modul>/test_<id>.py
- status:       wartet_auf_DAT (…) | referenz_prototyp (B…) | spezifiziert
"""
from __future__ import annotations

import csv
import glob
import re
import sys
from pathlib import Path

import yaml

ARBEIT = Path(__file__).resolve().parent.parent
SPEZ = ARBEIT / "spezifikation"

KAPITEL = {
    "3": "03-holzrahmenbau-fertighaus.md",
    "4": "04-rechtlicher-normativer-rahmen.md",
    "5": "05-stand-der-forschung.md",
    "6": "06-anforderungen.md",
    "7": "07-systemarchitektur.md",
    "7a": "07a-nachweisfuehrung.md",
    "8": "08-informationsmodell.md",
    "9": "09-regelraum.md",
    "9a": "09a-gebaeudetypen-regelprofile.md",
    "9b": "09b-entwurfsqualitaet-psychologie.md",
}
ANF_KAPITEL = ["3", "6", "7", "8", "9", "9a", "9b"]
DAT_KAPITEL = ["3", "6", "7"]

# ---------------------------------------------------------------------------
# Phase und Rolle (vorläufig). Phasen nach Tabelle 6.3, Rollen nach Tabelle 6.1.
# ---------------------------------------------------------------------------
Q = ("querschnittlich", "alle")
PHASE_ROLLE: dict[str, tuple[str, str]] = {}


def setze(ids: str, phase: str, rolle: str) -> None:
    for i in ids.split():
        PHASE_ROLLE[i] = (phase, rolle)


# Kapitel 3
setze("ANF-03-01 ANF-03-03 ANF-03-09 ANF-03-10 ANF-03-11", "Werkplanung", "WP")
setze("ANF-03-02 ANF-03-23", *Q)
setze("ANF-03-04 ANF-03-08 ANF-03-24", "Entwurf", "KU")
setze("ANF-03-05 ANF-03-06", "Regelraum", "FR")
setze("ANF-03-07 ANF-03-12 ANF-03-13 ANF-03-14 ANF-03-18", "Fertigung", "WK")
setze("ANF-03-15 ANF-03-16 ANF-03-17 ANF-03-20", "Montage", "MO")
setze("ANF-03-19 ANF-03-21 ANF-03-22", "Bemusterung", "KU")
setze("ANF-03-25", "querschnittlich", "VT")
# Kapitel 8
setze("ANF-08-01 ANF-08-02 ANF-08-03 ANF-08-04 ANF-08-05 ANF-08-06 ANF-08-13 ANF-08-14 "
      "ANF-08-15 ANF-08-18 ANF-08-23 ANF-08-24 ANF-08-25 ANF-08-27 ANF-08-28", *Q)
setze("ANF-08-07 ANF-08-08 ANF-08-09 ANF-08-10 ANF-08-11 ANF-08-12 ANF-08-21 ANF-08-29", "Werkplanung", "WP")
setze("ANF-08-16 ANF-08-17", "Bemusterung", "KU")
setze("ANF-08-19 ANF-08-20", "Fachfreigabe", "BV")
setze("ANF-08-22", "Fertigung", "WK")
setze("ANF-08-26", "Idee", "KU")
setze("ANF-08-30", "Entwurf", "KU")
setze("ANF-08-31", "Regelraum", "FR")
# Kapitel 9
setze("ANF-09-01 ANF-09-03 ANF-09-04 ANF-09-05 ANF-09-06 ANF-09-07 ANF-09-09 ANF-09-10 "
      "ANF-09-20", "Regelraum", "FR")
setze("ANF-09-02 ANF-09-08 ANF-09-11 ANF-09-13 ANF-09-14 ANF-09-15 ANF-09-16 ANF-09-17 "
      "ANF-09-19 ANF-09-22 ANF-09-23 ANF-09-24 ANF-09-25 ANF-09-27 ANF-09-28 ANF-09-29", "Entwurf", "KU")
setze("ANF-09-12 ANF-09-18 ANF-09-21", "Fachfreigabe", "BV")
setze("ANF-09-26", "Bemusterung", "KU")
# Kapitel 9a
setze("ANF-09a-01 ANF-09a-02 ANF-09a-03 ANF-09a-04 ANF-09a-11 ANF-09a-12 ANF-09a-13 "
      "ANF-09a-14 ANF-09a-15 ANF-09a-18", "Entwurf", "KU")
setze("ANF-09a-05 ANF-09a-07 ANF-09a-17", "Fachfreigabe", "BV")
setze("ANF-09a-06 ANF-09a-10", "Regelraum", "FR")
setze("ANF-09a-08", "Fachfreigabe", "TW")
setze("ANF-09a-09 ANF-09a-16", "Angebot und Vertrag", "VT")
setze("ANF-09a-19", "Entwurf", "GE")
# Kapitel 9b
setze(" ".join(f"ANF-09b-{i:02d}" for i in range(1, 19)), "Entwurf", "KU")
setze("ANF-09b-02 ANF-09b-09 ANF-09b-18", "Regelraum", "FR")
setze("ANF-09b-10 ANF-09b-13", *Q)
# Kapitel 6
setze("ANF-06-01 ANF-06-03 ANF-06-05 ANF-06-07", "Fachfreigabe", "BV")
setze("ANF-06-02", "Regelraum", "BV")
setze("ANF-06-04", "Fachfreigabe", "TW")
setze("ANF-06-06", "Entwurf", "VT")
setze("ANF-06-08 ANF-06-09", "Idee", "KU")
setze("ANF-06-10 ANF-06-11", "Entwurf", "KU")
setze("ANF-06-12 ANF-06-13 ANF-06-14", "Angebot und Vertrag", "VT")
setze("ANF-06-15", "Bemusterung", "KU")
setze("ANF-06-16 ANF-06-17 ANF-06-18 ANF-06-19", "Bauantrag", "BV")
setze("ANF-06-20", "Werkplanung", "WP")
setze("ANF-06-21", "Fertigung", "WK")
setze("ANF-06-22", "Montage", "MO")
setze("ANF-06-23 ANF-06-24", "Übergabe", "KU")
setze("ANF-06-25 ANF-06-26 ANF-06-27 ANF-06-29 ANF-06-32 ANF-06-35 ANF-06-36 ANF-06-37 "
      "ANF-06-38 ANF-06-40", *Q)
setze("ANF-06-28 ANF-06-30 ANF-06-31 ANF-06-33 ANF-06-34 ANF-06-39", "Entwurf", "KU")
# Kapitel 7
setze("ANF-07-01 ANF-07-02 ANF-07-03 ANF-07-04 ANF-07-05 ANF-07-06 ANF-07-21 ANF-07-23", "Entwurf", "KU")
setze("ANF-07-07 ANF-07-08 ANF-07-09 ANF-07-10 ANF-07-11 ANF-07-14 ANF-07-15 ANF-07-16 "
      "ANF-07-17 ANF-07-18 ANF-07-19 ANF-07-22", *Q)
setze("ANF-07-12 ANF-07-13", "Fachfreigabe", "BV")
setze("ANF-07-20", "Fertigung", "WK")

# Priorität der Datenlieferungen: Kapitel 3.7.3 (Voraussetzung der Demonstration),
# Kapitel 6.7.3 und 7.9.3 (Voraussetzung des Produktivbetriebs).
DAT_MUSS = {"DAT-01", "DAT-04", "DAT-05", "DAT-07", "DAT-08",
            "DAT-06-01", "DAT-06-03", "DAT-06-05", "DAT-06-06",
            "DAT-07-02", "DAT-07-03", "DAT-07-04"}


# ---------------------------------------------------------------------------
def tabellenzeilen(text: str, praefix: str) -> list[list[str]]:
    zeilen = []
    for z in text.splitlines():
        if z.startswith(f"| {praefix}-"):
            z = z.replace("\\|", "│")  # maskierte Pipes (Kapitel 8) erhalten
            zellen = [c.strip().replace("│", "|") for c in z.strip().strip("|").split("|")]
            # nur echte Anforderungs- bzw. Lieferzeilen, keine Verweise wie „ANF-03-02 / ANF-08-23“
            if re.fullmatch(rf"{praefix}-\d{{2}}[ab]?(?:-\d{{2}})?", zellen[0]):
                zeilen.append(zellen)
    return zeilen


def bereinige(s: str) -> str:
    return s.replace("**", "").strip()


def abschnitte(kap: str) -> tuple[dict[str, str], dict[str, str]]:
    """Abschnittstexte je Nummer und Entscheidungstexte je E-Nummer eines Kapitels."""
    zeilen = (ARBEIT / KAPITEL[kap]).read_text(encoding="utf-8").splitlines()
    koepfe = []
    for i, z in enumerate(zeilen):
        m = re.match(r"^(#{2,4}) (\d+[ab]?(?:\.\d+)*) ", z)
        if m:
            koepfe.append((i, len(m.group(1)), m.group(2)))
    ab = {}
    for k, (i, ebene, nr) in enumerate(koepfe):
        ende = len(zeilen)
        for j, e2, _ in koepfe[k + 1:]:
            if e2 <= ebene:
                ende = j
                break
        ab[nr] = "\n".join(zeilen[i:ende])
    text = "\n".join(zeilen)
    ents = {}
    for m in re.finditer(r"\*\*(E\d+[ab]?\.\d+) ", text):
        rest = text[m.start():]
        n = re.search(r"\n\*\*E\d+[ab]?\.\d+ |\n#", rest[3:])
        ents[m.group(1)] = rest[: n.start() + 3 if n else len(rest)]
    return ab, ents


def keys_in(text: str) -> set[str]:
    ks = set()
    for block in re.findall(r"\[(@[^\]]+)\]", text):
        ks.update(re.findall(r"@([A-Za-z0-9_:\-]+)", block))
    return ks


def bib_keys() -> set[str]:
    ks = set()
    for d in glob.glob(str(ARBEIT / "literatur" / "lit-*.bib")):
        ks.update(re.findall(r"^@\w+\{([^,\s]+),", Path(d).read_text(encoding="utf-8"), re.M))
    return ks


def main() -> int:
    fehler: list[str] = []
    bib = bib_keys()
    index = {k: abschnitte(k) for k in KAPITEL}

    module = yaml.safe_load((SPEZ / "module.yaml").read_text(encoding="utf-8"))["module"]
    modul_von: dict[str, str] = {}
    for m in module:
        for a in m.get("anforderungen", []):
            if a in modul_von:
                fehler.append(f"{a} mehrfach zugeordnet ({modul_von[a]}, {m['name']})")
            modul_von[a] = m["name"]

    anf = []
    for kap in ANF_KAPITEL:
        text = (ARBEIT / KAPITEL[kap]).read_text(encoding="utf-8")
        for z in tabellenzeilen(text, "ANF"):
            if len(z) != 5:
                fehler.append(f"{z[0]}: {len(z)} Spalten statt 5")
                continue
            aid, prio, beschr, beleg, abn = (bereinige(c) for c in z)
            # Quellen-Keys aus den im Beleg genannten Abschnitten und Entscheidungen
            ks = set(keys_in(beschr + " " + beleg))
            for tok in re.finditer(r"(Beispiel |Listing |Tabelle |Abbildung |Satz )?\b(E\d+[ab]?\.\d+|\d+[ab]?(?:\.\d+)+)\b", beleg):
                if tok.group(1):
                    continue
                t = tok.group(2)
                if t.startswith("E"):
                    kap_e = re.match(r"E(\d+[ab]?)", t).group(1)
                    if kap_e in index:
                        ks |= keys_in(index[kap_e][1].get(t, ""))
                else:
                    kap_s = t.split(".")[0]
                    if kap_s in index:
                        ks |= keys_in(index[kap_s][0].get(t, ""))
            ks &= bib
            modul = modul_von.get(aid, "")
            if not modul:
                fehler.append(f"{aid} keinem Modul zugeordnet")
            phase, rolle = PHASE_ROLLE.get(aid, ("", ""))
            if not phase:
                fehler.append(f"{aid} ohne Phase/Rolle")
            dats = sorted(set(re.findall(r"DAT-\d{2}(?:-\d{2})?", beschr + " " + abn)))
            beisp = sorted(set(re.findall(r"\bB\d{1,2}\b", beleg + " " + abn)), key=lambda b: int(b[1:]))
            if dats:
                status = f"wartet_auf_DAT ({', '.join(dats)})"
            elif beisp:
                status = f"referenz_prototyp ({', '.join(beisp)})"
            else:
                status = "spezifiziert"
            anf.append({
                "id": aid, "prioritaet": prio, "phase": phase, "rolle": rolle,
                "beschreibung": beschr, "abnahmekriterium": abn, "kapitel": kap,
                "quelle_keys": ";".join(sorted(ks, key=str.lower)), "modul": modul,
                "test": f"tests/{modul}/test_{aid.lower().replace('-', '_')}.py" if modul else "",
                "status": status,
            })

    ids = [a["id"] for a in anf]
    for i in set(ids):
        if ids.count(i) > 1:
            fehler.append(f"{i} doppelt in den Kapiteln")
    for a in anf:
        if a["prioritaet"] not in ("Muss", "Soll"):
            fehler.append(f"{a['id']}: Priorität {a['prioritaet']!r}")
        if not a["abnahmekriterium"]:
            fehler.append(f"{a['id']}: Abnahmekriterium fehlt")
    for a in modul_von:
        if a not in ids:
            fehler.append(f"{a} in module.yaml, aber in keinem Kapitel")

    def sortkey(i: str):
        k, n = i.split("-")[1], int(i.split("-")[2])
        return (int(re.match(r"\d+", k).group()), k, n)

    anf.sort(key=lambda a: sortkey(a["id"]))
    felder = ["id", "prioritaet", "phase", "rolle", "beschreibung", "abnahmekriterium",
              "kapitel", "quelle_keys", "modul", "test", "status"]
    with open(SPEZ / "anforderungen.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=felder)
        w.writeheader()
        w.writerows(anf)

    # Datenlieferungen
    dat = []
    for kap in DAT_KAPITEL:
        text = (ARBEIT / KAPITEL[kap]).read_text(encoding="utf-8")
        for z in tabellenzeilen(text, "DAT"):
            z = [bereinige(c) for c in z]
            if kap == "3":      # ID | Frage | Inhalt | Format | Ersatz | blockiert
                did, inhalt, blockiert = z[0], f"{z[2]} (Frage {z[1]}; Format: {z[3]}; Ersatz: {z[4]})", z[5]
            else:               # ID | Inhalt | Format | Ersatz | blockiert
                did, inhalt, blockiert = z[0], f"{z[1]} (Format: {z[2]}; Ersatz: {z[3]})", z[4]
            dat.append({"id": did, "beschreibung": inhalt, "benoetigt_fuer": blockiert,
                        "kapitel": kap, "prioritaet": "Muss" if did in DAT_MUSS else "Soll"})
    dids = [d["id"] for d in dat]
    for i in set(dids):
        if dids.count(i) > 1:
            fehler.append(f"{i} doppelt")
    with open(SPEZ / "datenlieferungen.csv", "w", encoding="utf-8", newline="") as f:
        w = csv.DictWriter(f, fieldnames=["id", "beschreibung", "benoetigt_fuer", "kapitel", "prioritaet"])
        w.writeheader()
        w.writerows(dat)

    # Rückprüfung der geschriebenen Dateien
    rueck = list(csv.DictReader(open(SPEZ / "anforderungen.csv", encoding="utf-8")))
    modulnamen = {m["name"] for m in module}
    for r in rueck:
        if r["modul"] not in modulnamen:
            fehler.append(f"{r['id']}: Modul {r['modul']!r} unbekannt")
        for k in filter(None, r["quelle_keys"].split(";")):
            if k not in bib:
                fehler.append(f"{r['id']}: Key {k} fehlt")
    rueck_d = list(csv.DictReader(open(SPEZ / "datenlieferungen.csv", encoding="utf-8")))

    muss = sum(r["prioritaet"] == "Muss" for r in rueck)
    je_kap = {k: sum(r["kapitel"] == k for r in rueck) for k in ANF_KAPITEL}
    je_phase: dict[str, int] = {}
    for r in rueck:
        je_phase[r["phase"]] = je_phase.get(r["phase"], 0) + 1
    print(f"{len(rueck)} Anforderungen ({muss} Muss, {len(rueck) - muss} Soll); je Kapitel {je_kap}")
    print(f"je Phase {je_phase}")
    print(f"{sum(bool(r['quelle_keys']) for r in rueck)} mit Quellen-Keys; "
          f"{len(rueck_d)} Datenlieferungen ({sum(d['prioritaet'] == 'Muss' for d in rueck_d)} Muss)")
    print(f"{len(fehler)} Fehler")
    for e in fehler:
        print("  -", e)
    return 1 if fehler else 0


if __name__ == "__main__":
    sys.exit(main())

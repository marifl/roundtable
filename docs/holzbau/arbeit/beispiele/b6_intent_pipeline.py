#!/usr/bin/env python3
"""
B6 – Deterministischer Teil der Sprachpipeline.

    Äußerung ──► [Intent-Modell: STUB] ──► Intent + Wahrscheinlichkeit
        │                                        │
        ├──► Zahlen-/Einheitenparser (deterministisch)
        ├──► Raumreferenz-Auflösung gegen State-JSON (deterministisch)
        └──► Anwendung auf das Parametermodell + Regelprüfung (deterministisch)
                 └──► angenommen (neuer Zustand, Änderungsliste)
                      oder abgelehnt / Rückfrage (mit Begründung)

WICHTIG – Kennzeichnung: Das Intent-Modell (Laya bzw. Jev, siehe Recherche 03)
wird hier NICHT aufgerufen. `IntentModellStub` simuliert dessen Schnittstelle
(typisierte Frage → Antwortoptionen mit Wahrscheinlichkeiten) über eine feste
Schlüsselworttabelle mit FESTEN, ERFUNDENEN Wahrscheinlichkeiten. Die Werte
sind keine Messergebnisse und sagen nichts über die Güte der echten Modelle.
Laut Recherche 03 liefern Jev/Laya keine Werte wie „1,20 m“; diese liest der
deterministische Parser. Genau diese Arbeitsteilung zeigt das Beispiel.

Eingabe:  daten/haus_state.json
Ausgabe:  ausgabe/intent_protokoll.json

Aufruf:   python b6_intent_pipeline.py                 (Beispielsätze)
          python b6_intent_pipeline.py "Mach das Bad oben zwei Meter sechzig breit"
"""
from __future__ import annotations

import copy
import json
import re
import sys
import unicodedata
from dataclasses import dataclass, field, asdict
from pathlib import Path

HIER = Path(__file__).resolve().parent
STANDARD_STATE = HIER / "daten" / "haus_state.json"

# ---------------------------------------------------------------------------
# 1. Deutscher Zahlen- und Einheitenparser
# ---------------------------------------------------------------------------

EINER = {"null": 0, "ein": 1, "eins": 1, "eine": 1, "einen": 1, "einem": 1, "einer": 1, "zwei": 2, "zwo": 2,
         "drei": 3, "vier": 4, "fuenf": 5, "sechs": 6, "sieben": 7, "acht": 8, "neun": 9}
ZEHNER_BIS_19 = {"zehn": 10, "elf": 11, "zwoelf": 12, "dreizehn": 13, "vierzehn": 14, "fuenfzehn": 15,
                 "sechzehn": 16, "siebzehn": 17, "achtzehn": 18, "neunzehn": 19}
ZEHNER = {"zwanzig": 20, "dreissig": 30, "vierzig": 40, "fuenfzig": 50, "sechzig": 60, "siebzig": 70,
          "achtzig": 80, "neunzig": 90}
BRUECHE = {"halb": 0.5, "halbe": 0.5, "halben": 0.5, "anderthalb": 1.5, "eineinhalb": 1.5, "zweieinhalb": 2.5,
           "dreieinhalb": 3.5}
# Einheit → (Dimension, Faktor auf SI-Basis m / m² / Grad)
EINHEITEN = {
    "m": ("laenge", 1.0), "meter": ("laenge", 1.0), "metern": ("laenge", 1.0),
    "cm": ("laenge", 0.01), "zentimeter": ("laenge", 0.01), "zentimetern": ("laenge", 0.01),
    "mm": ("laenge", 0.001), "millimeter": ("laenge", 0.001),
    "m2": ("flaeche", 1.0), "m²": ("flaeche", 1.0), "qm": ("flaeche", 1.0), "quadratmeter": ("flaeche", 1.0),
    "quadratmetern": ("flaeche", 1.0),
    "grad": ("winkel", 1.0), "°": ("winkel", 1.0),
}


def normalisiere(text: str) -> str:
    """Kleinschreibung, Umlaute/ß ausschreiben, Satzzeichen (außer , . °) trennen."""
    t = unicodedata.normalize("NFC", text.lower())
    for a, b in (("ä", "ae"), ("ö", "oe"), ("ü", "ue"), ("ß", "ss")):
        t = t.replace(a, b)
    t = re.sub(r"(\d)\s*(m²|m2|°)", r"\1 \2", t)          # „12m²“ → „12 m²“
    t = re.sub(r"(\d)(cm|mm|m|qm)\b", r"\1 \2", t)          # „120cm“ → „120 cm“
    t = re.sub(r"[!?;:\"()]", " ", t)
    t = re.sub(r"(?<!\d)[.,](?!\d)", " ", t)                # Satzzeichen, aber nicht „1,20“
    return re.sub(r"\s+", " ", t).strip()


def zahlwort(wort: str) -> int | None:
    """Deutsches Zahlwort 0…999 als ganze Zahl, sonst None.
    Beispiele: 'fuenfunddreissig' → 35, 'zweihundertzwanzig' → 220."""
    if wort in EINER:
        return EINER[wort]
    if wort in ZEHNER_BIS_19:
        return ZEHNER_BIS_19[wort]
    if wort in ZEHNER:
        return ZEHNER[wort]
    if "hundert" in wort:
        vor, _, nach = wort.partition("hundert")
        h = 1 if vor in ("", "ein", "eins") else EINER.get(vor)
        if h is None:
            return None
        if nach == "":
            return 100 * h
        rest = zahlwort(nach[3:] if nach.startswith("und") else nach)
        return None if rest is None or rest >= 100 else 100 * h + rest
    if "und" in wort:
        e, _, z = wort.partition("und")
        if e in EINER and z in ZEHNER and EINER[e] > 0:
            return EINER[e] + ZEHNER[z]
    return None


@dataclass
class Token:
    art: str            # "zahl" | "einheit" | "wort"
    text: str
    wert: float | None = None
    ganz: bool = False  # ganze Zahl (für „eins zwanzig“)
    dim: str | None = None
    faktor: float = 1.0


def tokenisiere(text: str) -> list[Token]:
    roh = normalisiere(text).split(" ")
    out: list[Token] = []
    i = 0
    while i < len(roh):
        w = roh[i]
        if re.fullmatch(r"\d+([.,]\d+)?", w):
            v = float(w.replace(",", "."))
            out.append(Token("zahl", w, v, ganz=("," not in w and "." not in w)))
        elif w in BRUECHE:
            out.append(Token("zahl", w, BRUECHE[w]))
        elif (z := zahlwort(w)) is not None and w not in ("ein", "eine", "einen", "einem", "einer") or \
                (w in ("ein", "eine", "einen", "einem", "einer") and i + 1 < len(roh) and
                 (roh[i + 1] in EINHEITEN or roh[i + 1] in BRUECHE)):
            z = zahlwort(w)
            # „drei komma fuenf“ / „zwei komma fuenf null“
            if i + 2 < len(roh) and roh[i + 1] == "komma":
                ziffern, j = "", i + 2
                while j < len(roh) and roh[j] in EINER and EINER[roh[j]] <= 9 and roh[j] not in ("ein", "eine", "einen"):
                    ziffern += str(EINER[roh[j]])
                    j += 1
                if ziffern:
                    out.append(Token("zahl", " ".join(roh[i:j]), float(f"{z}.{ziffern}")))
                    i = j
                    continue
            out.append(Token("zahl", w, float(z), ganz=True))
        elif w in EINHEITEN:
            d, f = EINHEITEN[w]
            out.append(Token("einheit", w, dim=d, faktor=f))
        else:
            out.append(Token("wort", w))
        i += 1
    # „einen halben Meter“ → 0,5 m: Artikel + Bruch zusammenfassen
    zus: list[Token] = []
    for t in out:
        if zus and t.art == "zahl" and t.text in BRUECHE and zus[-1].art == "zahl" and zus[-1].text in ("ein", "eine", "einen", "einem", "einer"):
            zus[-1] = t
        else:
            zus.append(t)
    return zus


@dataclass
class Messwert:
    wert: float          # in SI-Basis (m, m², Grad)
    dim: str             # laenge | flaeche | winkel | ohne
    quelle: str          # erkannter Textausschnitt
    muster: str          # welches Muster gegriffen hat
    mehrdeutig: bool = False


def parse_masse(text: str) -> list[Messwert]:
    """Alle Maßangaben eines Satzes. Muster (in dieser Reihenfolge):
      A  Zahl Einheit(Länge) Zahl<100      „einen Meter zwanzig“ → 1,20 m
      B  Zahl Einheit                      „1,20 m“, „35 Grad“, „zwölf Quadratmeter“
      C  Zahl(≤9) Zahl(10…99) ohne Einheit „eins zwanzig“ → 1,20 m (Umgangssprache)
         Zahl(≤9) Zahl(1…9)   ohne Einheit „eins fünf“ → mehrdeutig (1,05 oder 1,50?)
      D  Zahl allein                       ohne Einheit
    """
    tok = tokenisiere(text)
    erg: list[Messwert] = []
    i = 0
    while i < len(tok):
        t = tok[i]
        if t.art != "zahl":
            i += 1
            continue
        n1 = tok[i + 1] if i + 1 < len(tok) else None
        n2 = tok[i + 2] if i + 2 < len(tok) else None
        n3 = tok[i + 3] if i + 3 < len(tok) else None
        # A
        if (n1 and n1.art == "einheit" and n1.dim == "laenge" and n1.faktor == 1.0 and n2 and n2.art == "zahl"
                and n2.ganz and n2.wert < 100 and not (n3 and n3.art == "einheit")):
            erg.append(Messwert(round(t.wert + n2.wert / 100, 4), "laenge", f"{t.text} {n1.text} {n2.text}", "A"))
            i += 3
            continue
        # B
        if n1 and n1.art == "einheit":
            erg.append(Messwert(round(t.wert * n1.faktor, 4), n1.dim, f"{t.text} {n1.text}", "B"))
            i += 2
            continue
        # C
        if (t.ganz and t.wert <= 9 and n1 and n1.art == "zahl" and n1.ganz and n1.wert < 100
                and not (n2 and n2.art == "einheit")):
            mehrdeutig = n1.wert < 10
            erg.append(Messwert(round(t.wert + n1.wert / 100, 4), "laenge", f"{t.text} {n1.text}", "C", mehrdeutig))
            i += 2
            continue
        # D
        erg.append(Messwert(t.wert, "ohne", t.text, "D"))
        i += 1
    return erg


# ---------------------------------------------------------------------------
# 2. Raumreferenz-Auflösung gegen das kompakte State-JSON
# ---------------------------------------------------------------------------

RAUMTYP_SYNONYME = {
    "bad": ["bad", "badezimmer", "duschbad", "dusche"],
    "kind": ["kinderzimmer", "kind", "kinderzimmers"],
    "kueche": ["kueche"],
    "wohnen": ["wohnzimmer", "wohnen", "wohnbereich", "essen"],
    "schlafen": ["schlafzimmer", "elternschlafzimmer", "schlafen"],
    "flur": ["flur", "diele", "gang"],
    "hwr": ["hauswirtschaftsraum", "hauswirtschaft", "hwr", "technikraum"],
    "ankleide": ["ankleide", "ankleidezimmer"],
}
GESCHOSS_WOERTER = {
    "oben": "hoechstes", "obere": "hoechstes", "oberen": "hoechstes", "unten": "niedrigstes", "untere": "niedrigstes",
    "unteren": "niedrigstes", "og": "OG", "obergeschoss": "OG", "eg": "EG", "erdgeschoss": "EG",
}
ORDINALE = {"erste": 1, "ersten": 1, "zweite": 2, "zweiten": 2, "dritte": 3, "dritten": 3}


@dataclass
class Aufloesung:
    status: str                      # eindeutig | mehrdeutig | keine
    guid: str | None = None
    raum_id: str | None = None
    kandidaten: list = field(default_factory=list)
    begruendung: str = ""


def loese_raum(text: str, state: dict) -> Aufloesung:
    woerter = normalisiere(text).split(" ")
    typ = next((t for t, syn in RAUMTYP_SYNONYME.items() if any(w in syn for w in woerter)), None)
    if typ is None:
        return Aufloesung("keine", begruendung="kein Raumtyp erkannt")
    kand = [r for r in state["raeume"] if r["typ"] == typ]
    kriterien = [f"Typ={typ}"]
    ordnung = {g["id"]: g["ordnung"] for g in state["geschosse"]}
    for w in woerter:
        if w in GESCHOSS_WOERTER:
            ziel = GESCHOSS_WOERTER[w]
            if ziel == "hoechstes":
                ziel = max((r["geschoss"] for r in kand), key=lambda g: ordnung[g], default=None)
            elif ziel == "niedrigstes":
                ziel = min((r["geschoss"] for r in kand), key=lambda g: ordnung[g], default=None)
            kand = [r for r in kand if r["geschoss"] == ziel]
            kriterien.append(f"Geschoss={ziel} („{w}“)")
            break
    # Nummer: „Kinderzimmer 2“, „das zweite Kinderzimmer“
    nummer = None
    for j, w in enumerate(woerter):
        if w in ORDINALE:
            nummer = ORDINALE[w]
        elif re.fullmatch(r"\d", w) and j > 0 and any(woerter[j - 1] in syn for syn in RAUMTYP_SYNONYME.values()):
            nummer = int(w)
    if nummer is not None:
        kand = [r for r in kand if r["name"].endswith(f" {nummer}")]
        kriterien.append(f"Nummer={nummer}")
    # Größenattribut
    if any(w.startswith(("gross", "groess")) for w in woerter) and len(kand) > 1:
        m = max(r["breite"] * r["tiefe"] for r in kand)
        kand = [r for r in kand if r["breite"] * r["tiefe"] == m]
        kriterien.append("größter")
    elif any(w.startswith("klein") for w in woerter) and len(kand) > 1:
        m = min(r["breite"] * r["tiefe"] for r in kand)
        kand = [r for r in kand if r["breite"] * r["tiefe"] == m]
        kriterien.append("kleinster")
    liste = [{"guid": r["guid"], "name": r["name"], "geschoss": r["geschoss"]} for r in kand]
    if len(kand) == 1:
        return Aufloesung("eindeutig", kand[0]["guid"], kand[0]["id"], liste, ", ".join(kriterien))
    if not kand:
        return Aufloesung("keine", kandidaten=[], begruendung=", ".join(kriterien) + " → kein Raum")
    return Aufloesung("mehrdeutig", kandidaten=liste, begruendung=", ".join(kriterien) + f" → {len(kand)} Räume")


# ---------------------------------------------------------------------------
# 3. STUB des Intent-Modells (simuliert Laya/Jev – KEIN echtes Modell)
# ---------------------------------------------------------------------------

class IntentModellStub:
    """SIMULATION. Schnittstelle wie ein typisiertes Intent-Modell: eine Frage
    vom Typ 'choice' mit festen Optionen → Wahrscheinlichkeit je Option.
    Die Wahrscheinlichkeiten sind FEST und ERFUNDEN (Tabelle unten)."""

    OPTIONEN = ["raum_aendern", "dach_aendern", "fenster_einfuegen", "rueckgaengig", "sonstiges"]
    # Schlüsselwort → feste Verteilung (Summe 1). Erste passende Zeile gewinnt.
    TABELLE = [
        (("rueckgaengig", "zurueck"), {"rueckgaengig": 0.93, "raum_aendern": 0.02, "dach_aendern": 0.01, "fenster_einfuegen": 0.01, "sonstiges": 0.03}),
        (("dach", "dachneigung", "first"), {"dach_aendern": 0.88, "raum_aendern": 0.05, "fenster_einfuegen": 0.02, "rueckgaengig": 0.01, "sonstiges": 0.04}),
        (("fenster",), {"fenster_einfuegen": 0.84, "raum_aendern": 0.08, "dach_aendern": 0.02, "rueckgaengig": 0.01, "sonstiges": 0.05}),
        (("breit", "breiter", "schmaler", "tief", "tiefer", "laenger", "kuerzer", "quadratmeter", "qm", "groesser", "kleiner"),
         {"raum_aendern": 0.91, "fenster_einfuegen": 0.03, "dach_aendern": 0.02, "rueckgaengig": 0.01, "sonstiges": 0.03}),
        # nur ein Raumwort, kein Änderungsverb: geringere, aber ausreichende Sicherheit
        (tuple(w for syn in RAUMTYP_SYNONYME.values() for w in syn),
         {"raum_aendern": 0.78, "sonstiges": 0.12, "fenster_einfuegen": 0.05, "dach_aendern": 0.03, "rueckgaengig": 0.02}),
    ]
    STANDARD = {"sonstiges": 0.46, "raum_aendern": 0.31, "fenster_einfuegen": 0.10, "dach_aendern": 0.08, "rueckgaengig": 0.05}

    def frage(self, state: dict, aeusserung: str) -> dict:
        woerter = set(normalisiere(aeusserung).split(" "))
        for schluessel, vert in self.TABELLE:
            if any(s in woerter for s in schluessel):
                return {"frage": "Welche Aktion ist gemeint?", "typ": "choice", "antworten": dict(vert), "quelle": "STUB"}
        return {"frage": "Welche Aktion ist gemeint?", "typ": "choice", "antworten": dict(self.STANDARD), "quelle": "STUB"}


# ---------------------------------------------------------------------------
# 4. Intent raum_aendern anwenden + Regelprüfung
# ---------------------------------------------------------------------------

SCHWELLE = 0.70       # Mindestwahrscheinlichkeit des besten Intents
ABSTAND = 0.20        # Mindestabstand zum zweitbesten Intent


def _cm(x: float) -> int:
    return int(round(x * 100))


def erkenne_aenderung(text: str, masse: list[Messwert]) -> dict:
    """Welche Größe (breite/tiefe/flaeche) und ob absolut oder relativ."""
    w = normalisiere(text).split(" ")
    if any(x in w for x in ("breiter", "tiefer", "laenger", "groesser")):
        richtung = +1
    elif any(x in w for x in ("schmaler", "kuerzer", "kleiner")):
        richtung = -1
    else:
        richtung = 0
    groesse = "breite"
    if any(x.startswith(("tief", "lang", "laeng", "kuerz")) for x in w):
        groesse = "tiefe"
    laengen = [m for m in masse if m.dim in ("laenge", "flaeche")]
    if laengen and laengen[0].dim == "flaeche":
        groesse = "flaeche"
    return {"groesse": groesse, "relativ": richtung != 0, "richtung": richtung,
            "mass": asdict(laengen[0]) if laengen else None}


def pruefe_regeln(state: dict, raeume_neu: dict, geaendert: list[str]) -> list[str]:
    regeln = state["projektregeln"]
    verstoesse = []
    for rid in geaendert:
        r = raeume_neu[rid]
        mb = regeln["mindestbreite"].get(r["typ"])
        if mb is not None and r["breite_cm"] < _cm(mb):
            verstoesse.append(f"{r['name']}: Breite {r['breite_cm'] / 100:.2f} m < Mindestbreite {mb:.2f} m (Projektregel {r['typ']})")
        mf = regeln["mindestflaeche"].get(r["typ"])
        a = r["breite_cm"] * r["tiefe_cm"] / 1e4
        if mf is not None and a < mf - 1e-9:
            verstoesse.append(f"{r['name']}: Fläche {a:.2f} m² < Mindestfläche {mf:.2f} m² (Projektregel {r['typ']})")
        if r["breite_cm"] <= 0:
            verstoesse.append(f"{r['name']}: Breite ≤ 0")
    return verstoesse


def wende_raum_aendern(state: dict, raum_id: str, aenderung: dict) -> dict:
    """Setzt die neue Breite (bzw. Tiefe/Fläche) und gleicht in derselben
    Raumzeile beim rechten, sonst linken Nachbarn aus (Außenmaß bleibt)."""
    raeume = {r["id"]: dict(r, breite_cm=_cm(r["breite"]), tiefe_cm=_cm(r["tiefe"])) for r in state["raeume"]}
    r = raeume[raum_id]
    m = aenderung["mass"]
    raster_cm = _cm(state["projektregeln"]["raster"])
    if m is None:
        return {"status": "rueckfrage", "begruendung": "kein Maß erkannt – bitte Wert mit Einheit nennen"}
    if m["mehrdeutig"]:
        return {"status": "rueckfrage", "begruendung": f"Maß „{m['quelle']}“ mehrdeutig (z. B. 1,05 m oder 1,50 m?)"}
    if aenderung["groesse"] == "tiefe":
        return {"status": "abgelehnt", "begruendung": "Tiefenänderung verschiebt eine Achse über mehrere Räume; im PoC nicht umgesetzt"}
    alt = r["breite_cm"]
    if aenderung["groesse"] == "flaeche":
        # Zielfläche → Breite bei gleicher Tiefe, aufgerundet auf das Raster
        roh = m["wert"] * 1e4 / r["tiefe_cm"]
        neu = int(-(-roh // raster_cm) * raster_cm)
    elif aenderung["relativ"]:
        neu = alt + aenderung["richtung"] * _cm(m["wert"])
    else:
        neu = _cm(m["wert"])
    if neu % raster_cm:
        return {"status": "abgelehnt", "begruendung": f"{neu / 100:.2f} m liegt nicht im Raster {raster_cm} cm"}
    zeile = next(z for z, ids in state["zeilen"].items() if raum_id in ids)
    ids = state["zeilen"][zeile]
    k = ids.index(raum_id)
    nachbar = ids[k + 1] if k + 1 < len(ids) else (ids[k - 1] if k > 0 else None)
    if nachbar is None and neu != alt:
        return {"status": "abgelehnt", "begruendung": f"{r['name']} füllt die Zeile {zeile} allein; Außenmaß ist fest"}
    delta = neu - alt
    r["breite_cm"] = neu
    geaendert = [raum_id]
    if nachbar and delta:
        raeume[nachbar]["breite_cm"] -= delta
        geaendert.append(nachbar)
    verstoesse = pruefe_regeln(state, raeume, geaendert)
    aenderungen = [{"guid": raeume[i]["guid"], "raum": raeume[i]["name"], "breite_alt": _cm(next(x["breite"] for x in state["raeume"] if x["id"] == i)) / 100,
                    "breite_neu": raeume[i]["breite_cm"] / 100} for i in geaendert]
    if verstoesse:
        return {"status": "abgelehnt", "begruendung": "; ".join(verstoesse), "vorschlag_verworfen": aenderungen}
    neuer_state = copy.deepcopy(state)
    for x in neuer_state["raeume"]:
        if x["id"] in geaendert:
            x["breite"] = raeume[x["id"]]["breite_cm"] / 100
    return {"status": "angenommen", "aenderungen": aenderungen, "state": neuer_state}


def verarbeite(aeusserung: str, state: dict, modell: IntentModellStub | None = None) -> tuple[dict, dict | None]:
    """Ganze Pipeline. Rückgabe: (Protokoll, neuer Zustand oder None)."""
    modell = modell or IntentModellStub()
    antwort = modell.frage(state, aeusserung)
    rang = sorted(antwort["antworten"].items(), key=lambda kv: (-kv[1], kv[0]))
    (intent, p), (_, p2) = rang[0], rang[1]
    masse = parse_masse(aeusserung)
    protokoll = {"aeusserung": aeusserung, "intent": intent, "p": p, "p_zweiter": p2, "intent_quelle": antwort["quelle"],
                 "masse": [asdict(m) for m in masse]}
    if p < SCHWELLE or p - p2 < ABSTAND:
        return dict(protokoll, status="rueckfrage", begruendung=f"Intent unsicher (p={p:.2f}, Abstand {p - p2:.2f})"), None
    if intent != "raum_aendern":
        return dict(protokoll, status="nicht_umgesetzt", begruendung=f"Intent „{intent}“ erkannt; im PoC nur raum_aendern umgesetzt"), None
    ref = loese_raum(aeusserung, state)
    protokoll["raumreferenz"] = asdict(ref)
    if ref.status != "eindeutig":
        return dict(protokoll, status="rueckfrage", begruendung=f"Raumreferenz {ref.status}: {ref.begruendung}"), None
    aend = erkenne_aenderung(aeusserung, masse)
    protokoll["aenderung"] = aend
    erg = wende_raum_aendern(state, ref.raum_id, aend)
    return dict(protokoll, **{k: v for k, v in erg.items() if k != "state"}), erg.get("state")


BEISPIELE = [
    "Mach das Bad oben zwei Meter sechzig breit",
    "Das Bad oben bitte eins zwanzig breit",
    "Das Bad soll zwanzig Zentimeter breiter werden",
    "Mach das Kinderzimmer 2 auf 3,20 m",
    "Das zweite Kinderzimmer soll zwölf Quadratmeter haben",
    "Mach das Kinderzimmer 1 einen Meter zwanzig schmaler",
    "Das Bad oben eins fünf breiter",
    "Stell die Dachneigung auf 35 Grad",
    "Kannst du das mal anders machen",
]


def lade_state(pfad: Path | str = STANDARD_STATE) -> dict:
    with open(pfad, encoding="utf-8") as f:
        return json.load(f)


def verarbeite_einfach(aeusserung: str, state: dict) -> dict:
    """Wie verarbeite(), liefert aber nur das Protokoll (ohne neuen Zustand)."""
    return verarbeite(aeusserung, state)[0]


def main() -> None:
    state = lade_state()
    saetze = sys.argv[1:] or BEISPIELE
    protokolle = []
    for s in saetze:
        p = verarbeite_einfach(s, state)
        protokolle.append(p)
        print(f"» {s}\n  Intent {p['intent']} (p={p['p']:.2f}, {p['intent_quelle']}) → {p['status'].upper()}")
        if p.get("masse"):
            print("  Maße: " + ", ".join(f"{m['quelle']} = {m['wert']:g} [{m['dim']}, Muster {m['muster']}]" for m in p["masse"]))
        if p.get("raumreferenz"):
            rr = p["raumreferenz"]
            print(f"  Raum: {rr['status']} {rr.get('guid') or ''} ({rr['begruendung']})")
        for a in p.get("aenderungen", []):
            print(f"  ✔ {a['raum']} [{a['guid']}]: {a['breite_alt']:.2f} → {a['breite_neu']:.2f} m")
        if p.get("begruendung"):
            print(f"  Begründung: {p['begruendung']}")
    if not sys.argv[1:]:
        (HIER / "ausgabe").mkdir(exist_ok=True)
        (HIER / "ausgabe" / "intent_protokoll.json").write_text(json.dumps(protokolle, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")


if __name__ == "__main__":
    main()

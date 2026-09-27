#!/usr/bin/env python3
"""
Führt B1–B7 nacheinander aus und schreibt die Kennzahlen nach
ausgabe/kennzahlen.json (Grundlage für ergebnisse.md).

Aufruf:   python alle_ausfuehren.py
"""
from __future__ import annotations

import hashlib
import json
import platform
import subprocess
import sys
import time
from pathlib import Path

HIER = Path(__file__).resolve().parent
AUS = HIER / "ausgabe"


def lauf(skript: str, *args: str) -> str:
    t = time.perf_counter()
    r = subprocess.run([sys.executable, str(HIER / skript), *args], cwd=HIER, capture_output=True, text=True, check=True)
    print(f"✔ {skript} ({time.perf_counter() - t:.2f} s)")
    return r.stdout


def sha(p: Path) -> str:
    return hashlib.sha256(p.read_bytes()).hexdigest()


def main() -> None:
    AUS.mkdir(exist_ok=True)
    import ifcopenshell
    import ifcopenshell.validate

    kz: dict = {"umgebung": {"python": platform.python_version(), "ifcopenshell": ifcopenshell.version}}

    # B1 zweimal: Byte-Identität über zwei Prozesse
    kz["b1"] = json.loads(lauf("b1_wandelement.py"))
    h1 = sha(AUS / "wandelement.ifc")
    lauf("b1_wandelement.py")
    kz["b1"]["zweiter_lauf_byte_identisch"] = sha(AUS / "wandelement.ifc") == h1
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(AUS / "wandelement.ifc"), log, express_rules=True)
    kz["b1"]["validate_meldungen"] = len(log.statements)

    lauf("b3_uwert_iso6946.py")
    kz["b3"] = {k: {"holzanteil": v["holzanteil"], "u_wert": v["u_wert"], "r_oben": v["r_oben"],
                    "r_unten": v["r_unten"], "relativer_fehler": v["relativer_fehler"]}
                for k, v in json.loads((AUS / "uwert.json").read_text(encoding="utf-8")).items()}

    b2 = json.loads(lauf("b2_ids_pruefung.py"))
    kz["b2"] = {"bestanden": {"ergebnis": b2["bestanden"]["bestanden"],
                              "spezifikationen": len(b2["bestanden"]["spezifikationen"])},
                "fehlerhaft": {"ergebnis": b2["fehlerhaft"]["bestanden"], "fehlgeschlagen": b2["fehlerhaft"]["fehlgeschlagen"]},
                "eingebaute_fehler": b2["eingebaute_fehler"]}

    lauf("b4_abstandsflaechen.py")
    kz["b4"] = [{"szenario": e["szenario"], "giebel_modus": e["giebel_modus"], "zulaessig": e["zulaessig"],
                 "waende": {w["wand"]: {"T": w["T_erforderlich"], "vorh": w["T_vorhanden_mitte"], "ok": w["zulaessig"]} for w in e["waende"]}}
                for e in json.loads((AUS / "abstandsflaechen.json").read_text(encoding="utf-8"))]

    lauf("b5_treppe_din18065.py")
    t = json.loads((AUS / "treppe.json").read_text(encoding="utf-8"))
    kz["b5"] = {"anzahl_loesungen": t["anzahl_loesungen"], "beste": t["beste"], "uebersicht_je_n": t["uebersicht_je_n"]}

    lauf("b6_intent_pipeline.py")
    kz["b6"] = [{"aeusserung": p["aeusserung"], "intent": p["intent"], "p": p["p"], "status": p["status"]}
                for p in json.loads((AUS / "intent_protokoll.json").read_text(encoding="utf-8"))]

    try:
        import compas_timber  # noqa: F401
        kz["b7"] = lauf("b7_btlx_export.py").strip()
        kz["b7_sha256"] = sha(AUS / "wandelement.btlx")
    except ImportError:
        kz["b7"] = "übersprungen (compas_timber nicht installiert)"

    (AUS / "kennzahlen.json").write_text(json.dumps(kz, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"→ {AUS / 'kennzahlen.json'}")


if __name__ == "__main__":
    main()

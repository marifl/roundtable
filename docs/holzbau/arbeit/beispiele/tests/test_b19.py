"""Tests zu B19 (Schallschutz gegen Außenlärm, DIN 4109-1/-2:2018-01)."""
import copy
import json
import math
import os
import subprocess
import sys

import pytest

import b19_aussenlaerm as b19


@pytest.fixture(scope="module")
def erg():
    return b19.berechne()


def _raum(erg, variante, name):
    return next(z for z in erg["varianten"][variante]["raeume"] if z["raum"] == name and z["geschoss"] == "OG")


# --- energetische Addition (Handrechnung) --------------------------------------

def test_energetische_addition_handrechnung():
    # Wand 10 m² Rw 50, Fenster 2 m² Rw 35, S_S = 12 m²:
    # τ = 10/12·10^-5,0 + 2/12·10^-3,5 = 6,1038e-5  →  R'w,ges = 42,14 dB
    bt = [{"flaeche": 10.0, "rw": 50.0}, {"flaeche": 2.0, "rw": 35.0}]
    assert b19.rw_ges(bt, []) == pytest.approx(42.144, abs=0.001)
    # + ALD mit D_n,e,w = 40 dB: τ += A0/S_S·10^-4 = 10/12·10^-4  →  38,41 dB
    assert b19.rw_ges(bt, [{"dnew": 40.0}]) == pytest.approx(38.405, abs=0.001)
    # K_LPB = 5 dB auf dem Fenster (leisere Fassade): wie Rw 40  →  46,02 dB
    bt2 = [{"flaeche": 10.0, "rw": 50.0}, {"flaeche": 2.0, "rw": 35.0, "k_lpb": 5.0}]
    assert b19.rw_ges(bt2, []) == pytest.approx(46.021, abs=0.001)
    # Kastenfläche (rw=None) zählt nur zu S_S: gleiches Ergebnis wie Element allein mit S_S = 12 m²
    bt3 = [{"flaeche": 9.7, "rw": 50.0}, {"flaeche": 2.0, "rw": 35.0}, {"flaeche": 0.3, "rw": None}]
    tau = 9.7 / 12 * 1e-5 + 2 / 12 * 10 ** -3.5 + 10 / 12 * 10 ** -4.4
    assert b19.rw_ges(bt3, [{"dnew": 44.0}]) == pytest.approx(-10 * math.log10(tau), abs=1e-9)
    # schwächstes Bauteil dominiert: Gesamtwert liegt unter dem Fenster + 10 lg(S_S/S_F)
    assert b19.rw_ges(bt, []) < 35.0 + 10 * math.log10(12 / 2)


def test_pegelsumme_und_kal():
    assert b19.pegel_summe([60.0, 60.0]) == pytest.approx(63.01, abs=0.01)
    assert b19.k_al(0.8 * 20.0, 20.0) == pytest.approx(0.0)          # S_S = 0,8·S_G → 0 dB
    assert b19.k_al(20.0, 12.5) == pytest.approx(10 * math.log10(2.0))


# --- maßgeblicher Außenlärmpegel (DIN 4109-2, 4.4.5) ---------------------------

@pytest.mark.parametrize("tag,nacht,la_tag,la_schlaf", [
    (59, 50, 62, 63),   # DIN-Auslegung zu 4.4.5.1, Beispiel 1
    (59, 61, 62, 74),   # Beispiel 2
    (59, 45, 62, 62),   # Beispiel 3 (Differenz ≥ 10 dB: Tag maßgebend)
])
def test_la_din_auslegungsbeispiele(tag, nacht, la_tag, la_schlaf):
    la = b19.massgeblicher_aussenlaermpegel([{"art": "strasse", "lr_tag": tag, "lr_nacht": nacht}])
    assert la["la_tag"] == pytest.approx(la_tag)
    assert la["la_schlaf"] == pytest.approx(la_schlaf)


def test_la_schiene_und_mehrere_quellen():
    # Schiene: Beurteilungspegel −5 dB (4.4.5.3), dann +3 dB → 72 − 5 + 3 = 70
    s = b19.massgeblicher_aussenlaermpegel([{"art": "schiene", "lr_tag": 72, "lr_nacht": 59}])
    assert s["la_tag"] == pytest.approx(70.0)
    # Straße 63/55 (Nachtregel → 65) + Schiene 72/59 (→ 67): 10 lg(10^6,5 + 10^6,7) + 3 dB, +3 dB nur einmal
    m = b19.massgeblicher_aussenlaermpegel([{"art": "strasse", "lr_tag": 63, "lr_nacht": 55},
                                            {"art": "schiene", "lr_tag": 72, "lr_nacht": 59}])
    assert m["la_schlaf"] == pytest.approx(72.124, abs=0.001)


def test_lpb_und_baytb_schwelle():
    assert b19.la_aus_lpb("I") == 55.0 and b19.la_aus_lpb("III") == 65.0 and b19.la_aus_lpb("VI") == 80.0
    assert b19.la_aus_lpb("VII") is None
    assert b19.baytb_nachweis_erforderlich([("wohnen", 60.9)], False)[0] is False
    assert b19.baytb_nachweis_erforderlich([("wohnen", 61.0)], False)[0] is True
    assert b19.baytb_nachweis_erforderlich([("buero", 65.0)], False)[0] is False
    assert b19.baytb_nachweis_erforderlich([("wohnen", 50.0)], True)[0] is True


# --- Fassadenpegel und Eigenabschirmung ----------------------------------------

def test_fassadenpegel_nachweis_und_planung():
    e = b19.beispiel_eingabe()
    p = b19.fassadenpegel(e, "nachweis")
    assert p["N"]["quellen"][0]["sichtanteil"] == pytest.approx(1.0)
    assert p["S"]["quellen"][0]["sichtanteil"] == pytest.approx(0.0)
    assert p["S"]["quellen"][0]["dL_orientierung"] == pytest.approx(-5.0)     # DIN 4109-2, 4.4.5.1
    assert p["E"]["quellen"][0]["dL_orientierung"] == 0.0                     # Streifsicht: keine Minderung
    assert p["E"]["quellen"][0]["sichtanteil"] == pytest.approx(0.5, abs=0.01)
    pp = b19.fassadenpegel(e, "planung")
    assert pp["E"]["quellen"][0]["dL_orientierung"] == pytest.approx(-3.0, abs=0.1)
    assert all(v["nachweis_tauglich"] for v in p.values())


def test_eu_laermkarte_nicht_nachweistauglich():
    e = b19.beispiel_eingabe()
    e["quellen"][0]["verfahren"] = "EU-Lärmkarte (BUB)"
    p = b19.fassadenpegel(e, "nachweis")
    assert not any(v["nachweis_tauglich"] for v in p.values())


# --- Nachweis und Wahl der kleinsten ausreichenden Klasse ----------------------

def _einfacher_raum():
    raum = {"name": "T", "geschoss": "OG", "nutzung": "wohnen", "schlafen": True, "schutzbeduerftig": True,
            "polygon": [[0, 0], [4, 0], [4, 3], [0, 3]],
            "fenster": {"N": [{"b": 1.5, "h": 1.4, "mehrfluegelig": False, "rollladen": False}]}}
    pegel = {"N": {"la_tag": 68.0, "la_schlaf": 71.0}}
    return raum, {"N": 4.0}, 12.0, 2.5, pegel


def test_wahl_minimaler_klasse():
    raum, laengen, s_g, h, pegel = _einfacher_raum()
    kat = b19.katalog_beispiel()
    res = b19.waehle_bauteile(raum, laengen, s_g, h, pegel, kat, "KWL")
    assert res["gefunden"] and res["wahl"]["klasse"] == {"N": 4}
    # Handrechnung: erf = 71 − 30 = 41; K_AL = 10 lg(10/9,6) = 0,18; SSK 3 (37 dB) → 42,4 − 2 < 41,18
    w3 = copy.deepcopy(res["wahl"]); w3["klasse"]["N"] = 3
    assert not b19.pruefe_raum(raum, laengen, s_g, h, pegel, kat, w3, "KWL")["erfuellt"]
    assert b19.pruefe_raum(raum, laengen, s_g, h, pegel, kat, res["wahl"], "KWL")["erfuellt"]
    # Mindestwert: bei La 55 dB ist erf R'w,ges = 30 dB, nicht 25 dB
    pr = b19.pruefe_raum(raum, laengen, s_g, h, {"N": {"la_tag": 55.0, "la_schlaf": 55.0}}, kat, res["wahl"], "KWL")
    assert pr["zeitraeume"]["tag"]["erf_rw_ges"] == 30.0


def test_wahl_ist_optimal_je_raum(erg):
    """Für jeden gewählten Raum: eine Klasse weniger an irgendeiner Fassade
    (sonst gleiche Wahl) besteht nicht oder ist nicht billiger."""
    e = b19.beispiel_eingabe()
    from shapely.geometry import Polygon
    fp = Polygon(e["haus"]["footprint"])
    pegel = erg["fassadenpegel"]
    for vname, raeume in e["varianten"].items():
        for raum in raeume:
            if not raum["schutzbeduerftig"]:
                continue
            z = next(x for x in erg["varianten"][vname]["raeume"] if x["raum"] == raum["name"] and x["geschoss"] == raum["geschoss"])
            laengen = b19.raum_fassaden(raum, fp, 2.5)
            s_g = Polygon(raum["polygon"]).area
            for r, k in z["wahl"]["klasse"].items():
                if k <= 2:
                    continue
                w = copy.deepcopy(z["wahl"]); w["klasse"][r] = k - 1
                zul = b19.zulaessige_klassen(raum, r, e["katalog"], z["stufe"] == "Regnauer-Katalog")
                if k - 1 in zul:
                    assert not b19.pruefe_raum(raum, laengen, s_g, 2.5, pegel, e["katalog"], w, erg["lueftung"])["erfuellt"]


def test_regnauer_mehrfluegelig_nur_ssk2():
    raum = {"fenster": {"S": [{"b": 3.0, "h": 2.2, "mehrfluegelig": True, "rollladen": True}]}}
    assert b19.zulaessige_klassen(raum, "S", b19.katalog_beispiel(), True) == [2]
    assert b19.zulaessige_klassen(raum, "S", b19.katalog_beispiel(), False) == [2, 3, 4, 5, 6]  # Fremdprodukte


# --- Grundrisstausch -------------------------------------------------------------

def test_grundrisstausch_reduziert_anforderungen(erg):
    a, b = erg["varianten"]["A_ursprung"], erg["varianten"]["B_tausch"]
    sa, sb = _raum(erg, "A_ursprung", "Schlafen"), _raum(erg, "B_tausch", "Schlafen")
    assert sb["erf_rw_ges"] < sa["erf_rw_ges"] - 4.9                 # −5 dB abgewandte Seite
    assert sb["max_klasse"] < sa["max_klasse"]
    assert b["summe_mehrkosten_eur"] < a["summe_mehrkosten_eur"]
    assert b["max_klasse"] <= a["max_klasse"]
    assert len(a["regelverstoesse"]) > 0 and len(b["regelverstoesse"]) == 0
    assert erg["vergleich"]["empfehlung_anders_planen"] is True
    assert erg["empfehlungen"][0]["id"] in {"E1-grundriss-tausch", "E2-lueftung"}


def test_lueftung_und_nachweispflicht(erg):
    ids = {e["id"] for e in erg["empfehlungen"]}
    assert {"E2-lueftung", "E3-nachweispflicht", "E6-who"} <= ids
    assert erg["varianten"]["A_ursprung"]["baytb_nachweis_erforderlich"] is True


# --- Determinismus und IFC ---------------------------------------------------------

def test_determinismus():
    j1 = json.dumps(b19.berechne(), sort_keys=True)
    j2 = json.dumps(b19.berechne(), sort_keys=True)
    assert j1 == j2
    code = "import json, b19_aussenlaerm as b; print(json.dumps(b.berechne(), sort_keys=True))"
    aus = []
    for seed in ("1", "77"):
        env = dict(os.environ, PYTHONHASHSEED=seed)
        r = subprocess.run([sys.executable, "-c", code], cwd=os.path.dirname(b19.__file__), env=env,
                           capture_output=True, text=True, check=True)
        aus.append(r.stdout.strip())
    assert aus[0] == aus[1] == j1


def test_ifc_export(tmp_path, erg):
    ifcopenshell = pytest.importorskip("ifcopenshell")
    import ifcopenshell.util.element as el
    import ifcopenshell.validate
    e = b19.beispiel_eingabe()
    p = b19.exportiere_ifc(erg, e, "B_tausch", tmp_path / "b19.ifc")
    f = ifcopenshell.open(str(p))
    assert f.schema_identifier == "IFC4X3_ADD2"
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(p), log, express_rules=True)
    assert log.statements == []
    fenster = f.by_type("IfcWindow")
    assert fenster and all("AcousticRating" in el.get_psets(w)["Pset_WindowCommon"] for w in fenster)
    schlafen = next(s for s in f.by_type("IfcSpace") if s.Name == "Schlafen")
    ps = el.get_psets(schlafen)["HB_Aussenlaerm_Raum"]
    assert ps["NachweisErfuellt"] is True and ps["Schlafnutzung"] is True
    assert len(f.by_type("IfcAnnotation")) == 4
    p2 = b19.exportiere_ifc(erg, e, "B_tausch", tmp_path / "b19b.ifc")
    assert p.read_bytes().replace(b"b19.ifc", b"") == p2.read_bytes().replace(b"b19b.ifc", b"")

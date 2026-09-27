"""Tests zu B14: Fußbodenaufbau, gleiche OKFF, Konflikterklärung, IFC."""
import copy
import os
import subprocess
import sys

import ifcopenshell
import ifcopenshell.validate
import pytest

import b14_fussbodenaufbau as b14
from conftest import BEISPIELE

A, B = "A_bodenplatte_nass", "B_holzbalkendecke_trocken"


@pytest.fixture(scope="module")
def daten():
    return b14.lade_eingabe()


@pytest.fixture(scope="module")
def erg(daten):
    return {v: b14.berechne_variante(daten, v) for v in (A, B)}


def raum(e, name):
    return next(r for r in e["raeume"] if r["name"] == name)


def lage(r, rolle):
    return [s for s in r["schichten"] if s["rolle"] == rolle]


# --- Nachweis gleiche OKFF ------------------------------------------------

@pytest.mark.parametrize("v", [A, B])
def test_gleiche_okff_und_schichtsumme(erg, daten, v):
    e = erg[v]
    assert e["nachweis_gleiche_okff"]
    H = daten["varianten"][v]["ziel_aufbauhoehe_mm"]
    for r in e["raeume"]:
        assert r["zulaessig"] and r["verstoesse"] == []
        assert r["okff_mm"] == H
        dicke = sum(s["dicke_mm"] for s in r["schichten"])
        assert dicke == H + r["rohdecke_absenkung_mm"]
        assert r["okff_toleranz_mm"] <= daten["okff_toleranz_mm"]
        # Schichten lückenlos übereinander
        for s1, s2 in zip(r["schichten"], r["schichten"][1:]):
            assert s1["ok_mm"] == s2["uk_mm"]


@pytest.mark.parametrize("v", [A, B])
def test_uebergaenge_ohne_kante(erg, daten, v):
    for u in erg[v]["uebergaenge"]:
        assert u["verstoesse"] == []
        assert u["delta_okff_mm"] == 0
        assert u["kante_worst_case_mm"] <= daten["okff_toleranz_mm"]
    flur_bad = erg[v]["uebergaenge"][2]
    assert any("Mikrozement" in h and "Fugenprofil" in h for h in flur_bad["hinweise"])
    assert any("DIN 18040-2" in h for h in flur_bad["hinweise"])


# --- Handrechnungen Variante A (Bodenplatte, Heizestrich Bauart A) ---------

def test_heizestrich_mindestdicken_handrechnung(erg):
    """CAF-F4: max(35 + 17; 17 + 40) = 57 mm; CT-F4: max(45 + 17; 17 + 45) = 62 mm.
    Bad (Gefälle 2 % × 1,0 m = 20 mm, Rohdeckentoleranz 8 mm im Estrich): 62 + 20 + 8 = 90 mm,
    am Tiefpunkt 70 mm."""
    e = erg[A]
    assert raum(e, "Wohnen")["kennwerte"]["estrich_nenndicke_min_mm"] == 57
    bad = raum(e, "Bad")
    assert bad["estrich"] == "CT_F4"
    assert bad["kennwerte"]["estrich_nenndicke_min_mm"] == 62
    assert lage(bad, "estrich")[0]["dicke_mm"] == 90
    assert bad["kennwerte"]["estrich_tiefpunkt_mm"] == 70
    assert bad["kennwerte"]["gefaelle_mm"] == 20
    assert bad["rohdecke_absenkung_mm"] == 30
    assert 90 <= bad["kennwerte"]["estrichhoehe_am_einlauf_mm"] <= 220


def test_toleranz_wird_von_schuettung_aufgenommen(erg):
    """Flur: gebundene Schüttung über dem Leerrohr (25 + 10 mm Überdeckung + 8 mm Toleranz)
    nimmt die Rohdeckentoleranz auf; der Estrich bleibt auf 57 mm."""
    flur = raum(erg[A], "Flur")
    ie = lage(flur, "installationsebene")[0]
    assert ie["material"] == "gebundene_schuettung" and ie["dicke_mm"] >= 25 + 10 + 8
    assert lage(flur, "estrich")[0]["dicke_mm"] == 57


def test_kueche_daemmplatte_buendig_zu_leitungen(erg):
    """PWC/PWH 16 mm + 2 × 9 mm Dämmung = 34 mm → DEO-Platte 35 mm bündig (DIN 18560-2:2022 5.2)."""
    k = raum(erg[A], "Kueche")
    ie = lage(k, "installationsebene")[0]
    assert ie["material"] == "eps_deo_035" and ie["dicke_mm"] == 35
    assert k["kennwerte"]["leitungshoehe_mm"] == 34


def test_u_wert_und_r_ins(erg, daten):
    for r in erg[A]["raeume"]:
        assert r["kennwerte"]["U_W_m2K"] <= daten["varianten"][A]["grenzen"]["u_wert_max"]
        assert r["kennwerte"]["R_ins"] >= 1.25


def test_r_lambda_b_parkett_handrechnung(erg):
    """14 mm / 0,13 + 1 mm / 0,20 = 0,10769 + 0,005 = 0,1127 m²K/W ≤ 0,15."""
    assert raum(erg[A], "Wohnen")["kennwerte"]["R_lambda_B"] == pytest.approx(0.1127, abs=1e-4)


def test_teppich_auf_fbh_verstoss(daten):
    """Teppich 8 mm (λ 0,06) + Filz 5 mm (λ 0,05): 0,133 + 0,100 = 0,233 > 0,15."""
    d = copy.deepcopy(daten)
    d["raeume"][0]["belag"] = "teppich_8_filz"
    r = b14.optimiere_raum(d["raeume"][0], d["varianten"][A], d)
    assert r.kennwerte["R_lambda_B"] == pytest.approx(0.2333, abs=1e-4)
    assert any("R_λ,B" in v for v in r.verstoesse)


def test_belegreife(erg):
    assert raum(erg[A], "Wohnen")["kennwerte"]["belegreife_cm_max"] == 0.3   # CAF beheizt, Parkett
    assert raum(erg[A], "Bad")["kennwerte"]["belegreife_cm_max"] == 2.0      # CT beheizt, Naturstein
    assert raum(erg[B], "Wohnen")["kennwerte"]["belegreife_cm_max"] is None  # Trockenestrich


# --- Konflikterklärung ----------------------------------------------------

def test_konflikt_bad_ohne_absenkung(daten):
    d = copy.deepcopy(daten)
    d["varianten"][A]["absenkungen_mm"] = {}
    r = b14.optimiere_raum(d["raeume"][2], d["varianten"][A], d)
    assert not r.zulaessig
    assert "fehlen 30 mm" in r.verstoesse[0] and "absenken" in r.verstoesse[0]
    assert r.diagnose["h_erreichbar_mm"][0] == 240


def test_konflikt_abwasser_im_trockenaufbau(daten):
    """DN 50 mit 1 % über 1,2 m braucht 62 mm Installationsebene – im 160-mm-Trockenaufbau nicht unterzubringen."""
    d = copy.deepcopy(daten)
    d["raeume"][2]["leitungen"][0]["fuehrung"] = "im_aufbau"
    r = b14.optimiere_raum(d["raeume"][2], d["varianten"][B], d)
    assert not r.zulaessig and "fehlen" in r.verstoesse[0]


# --- Variante B: Holzbau-Regeln -------------------------------------------

def test_trockenaufbau_regeln(erg):
    e = erg[B]
    wohnen = raum(e, "Wohnen")
    assert wohnen["schichten"][0]["material"] == "wabe_schuettung"          # Wabe direkt auf Rohdecke
    assert wohnen["kennwerte"]["beschwerung_kg_m2"] >= 45
    for r in e["raeume"]:
        # Toleranzkette über Trockenestrich > 2 mm → Spachtelung (oder Mittelbett) wird gewählt
        assert r["kennwerte"]["nivellierhorizont"] in ("spachtelung", "verlegewerkstoff")
        assert r["kennwerte"]["flaechenmasse_kg_m2"] <= 180
    kueche = raum(e, "Kueche")
    assert kueche["schichten"][0]["material"] == "wabe_schuettung" and kueche["schichten"][0]["dicke_mm"] == 60
    assert raum(e, "Bad")["estrich"] == "TE_ZEM_25"
    assert any("Herstellerfreigabe" in h for h in raum(e, "Flur")["hinweise"])


def test_gmodg_anlage8():
    g = b14.gmodg_mindestdaemmung
    assert g({"medium": "heizung", "di_mm": 16})[0] == 20
    assert g({"medium": "heizung", "di_mm": 28})[0] == 30
    assert g({"medium": "heizung", "di_mm": 50})[0] == 50
    assert g({"medium": "heizung", "di_mm": 125})[0] == 100
    assert g({"medium": "heizung", "di_mm": 16}, "durchbruch")[0] == 10
    assert g({"medium": "heizung", "di_mm": 16}, "fussboden_verschiedene_nutzer")[0] == 6
    assert g({"medium": "trinkwasser_warm", "di_mm": 12, "stichleitung_volumen_l": 1.2})[0] == 0
    assert g({"medium": "trinkwasser_warm", "di_mm": 12, "zirkulation": True})[0] == 20
    assert g({"medium": "trinkwasser_kalt", "di_mm": 12})[0] is None
    assert g({"medium": "abwasser", "di_mm": 99})[0] is None


# --- IFC ------------------------------------------------------------------

@pytest.mark.parametrize("v", [A, B])
def test_ifc_valide_und_schichten(erg, daten, v, tmp_path):
    pfad = b14.erzeuge_ifc(daten, erg[v]).schreibe(tmp_path / f"{v}.ifc")
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(pfad), log, express_rules=True)
    assert log.statements == []
    f = ifcopenshell.open(str(pfad))
    covs = [c for c in f.by_type("IfcCovering") if c.PredefinedType == "FLOORING"]
    assert len(covs) == 4 and len(f.by_type("IfcRelCoversSpaces")) == 4 and len(f.by_type("IfcSlab")) == 1
    for c in covs:
        use = c.HasAssociations[0].RelatingMaterial
        assert use.is_a("IfcMaterialLayerSetUsage") and use.LayerSetDirection == "AXIS3"
        rid = c.CoversSpaces[0].RelatingSpace.Name
        r = next(x for x in erg[v]["raeume"] if x["id"] == rid)
        assert sum(l.LayerThickness for l in use.ForLayerSet.MaterialLayers) == pytest.approx(sum(s["dicke_mm"] for s in r["schichten"]))


def test_ifc_deterministisch(erg, daten, tmp_path):
    p1 = b14.erzeuge_ifc(daten, erg[B]).schreibe(tmp_path / "a.ifc")
    env = dict(os.environ, PYTHONHASHSEED="7")
    subprocess.run([sys.executable, "b14_fussbodenaufbau.py", "--variante", B, "--ifc"], cwd=BEISPIELE, env=env,
                   check=True, capture_output=True)
    p2 = BEISPIELE / "ausgabe" / f"b14_{B}.ifc"
    assert p1.read_bytes() == p2.read_bytes()

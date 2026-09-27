"""Tests zu B2 (IDS-Prüfung) und B3 (U-Wert nach DIN EN ISO 6946)."""
import pytest
from ifctester import ids

import b1_wandelement as b1
import b2_ids_pruefung as b2
import b3_uwert_iso6946 as b3


# --- B3: U-Wert ------------------------------------------------------------

@pytest.fixture(scope="module")
def param():
    return b3.lade_parameter()


def test_uwert_handrechnung_raster(param):
    """Handrechnung (4–5 Stellen, λ-Beispielwerte aus dem JSON):
        Holzanteil f = 60/625 = 0,096
        R_a (Holzpfad)   = 0,13 + 0,0125/0,25 + 0,015/0,13 + 0,2/0,13  + 0,06/0,043 + 0,04 = 3,26919
        R_b (Gefachpfad) = 0,13 + 0,05      + 0,11538    + 0,2/0,038 + 1,39535    + 0,04 = 6,99389
        R'  = 1 / (0,096/3,26919 + 0,904/6,99389) = 1 / 0,158622 = 6,30436
        λ'' = 0,096·0,13 + 0,904·0,038 = 0,046832  →  R_Gefach = 0,2/0,046832 = 4,27059
        R'' = 0,13 + 0,05 + 0,11538 + 4,27059 + 1,39535 + 0,04 = 6,00132
        R_T = (6,30436 + 6,00132)/2 = 6,15284  →  U = 0,16253 W/(m²K)
        e   = (6,30436 − 6,00132)/(2·6,15284) = 2,46 %"""
    e = b3.berechne_uwert(param, b3.holzanteil_raster(param), "verputzt")
    assert e.holzanteil == pytest.approx(0.096)
    assert e.r_t_holz == pytest.approx(3.26919, abs=1e-4)
    assert e.r_t_gefach == pytest.approx(6.99389, abs=1e-4)
    assert e.r_oben == pytest.approx(6.30436, abs=1e-4)
    assert e.r_unten == pytest.approx(6.00132, abs=1e-4)
    assert e.u_wert == pytest.approx(0.16253, abs=5e-5)
    assert e.relativer_fehler == pytest.approx(0.0246, abs=1e-4)


def test_uwert_grenzwerte_ordnung_und_hinterlueftung(param):
    f = b3.holzanteil_geometrie(param)
    v = b3.berechne_uwert(param, f, "verputzt")
    h = b3.berechne_uwert(param, f, "hinterlueftet")
    assert v.r_unten < v.r_t < v.r_oben
    assert h.rse == 0.13 and v.rse == 0.04
    assert h.u_wert < v.u_wert  # größeres Rse → kleineres U
    assert f == pytest.approx(2_575_200 / (4800 * 2750 - 1260 * 1385))


def test_uwert_steht_im_ifc(param):
    f = b1.erzeuge_ifc(b1.lade_parameter())
    import ifcopenshell.util.element as ue
    u = ue.get_psets(f.by_type("IfcWall")[0])["Pset_WallCommon"]["ThermalTransmittance"]
    assert u == b3.uwert_fuer_ifc(param) == pytest.approx(0.187, abs=1e-3)


# --- B2: IDS -----------------------------------------------------------------

def test_ids_datei_ist_schema_valide():
    spez = ids.open(str(b2.IDS_DATEI), validate=True)  # wirft bei XSD-Fehlern
    assert len(spez.specifications) == 11


@pytest.fixture(scope="module")
def ifc_dateien(tmp_path_factory):
    d = tmp_path_factory.mktemp("b2")
    ok = b1.schreibe_ifc(b1.lade_parameter(), d / "wandelement.ifc")
    nok = d / "wandelement_fehlerhaft.ifc"
    b2.baue_fehlerhaft(ok, nok)
    return ok, nok


def test_ids_bestanden(ifc_dateien, monkeypatch, tmp_path):
    monkeypatch.setattr(b2, "AUSGABE", tmp_path)
    erg = b2.pruefe(ifc_dateien[0], "bestanden")
    assert erg["bestanden"], erg["fehlgeschlagen"]
    assert all(s["anwendbar"] >= 1 for s in erg["spezifikationen"] if s["id"] != "HRB-11")
    assert (tmp_path / "ids_bericht_bestanden.html").exists()
    assert (tmp_path / "ids_bericht_bestanden.md").read_text(encoding="utf-8").count("✔") == 11


def test_ids_fehlerhaft(ifc_dateien, monkeypatch, tmp_path):
    monkeypatch.setattr(b2, "AUSGABE", tmp_path)
    erg = b2.pruefe(ifc_dateien[1], "fehlerhaft")
    assert not erg["bestanden"]
    assert set(erg["fehlgeschlagen"]) == b2.ERWARTET_FEHLERHAFT

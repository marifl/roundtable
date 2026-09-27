"""Tests zu B4 (Abstandsflächen BayBO Art. 6) und B5 (Treppe DIN 18065)."""
import copy
import json
import math

import pytest

import b4_abstandsflaechen as b4
import b5_treppe_din18065 as b5


# --- B4 ------------------------------------------------------------------------

@pytest.fixture(scope="module")
def param():
    return json.loads(b4.STANDARD_PARAMETER.read_text(encoding="utf-8"))


def test_mass_h_und_tiefe(param):
    r = param["regel"]
    dh = b4.dachhoehe(10, 45)
    assert dh == pytest.approx(5.0)
    assert b4.mass_h(6.5, dh, 45, r) == pytest.approx(6.5 + 5 / 3)
    assert b4.tiefe(b4.mass_h(6.5, dh, 45, r), r) == pytest.approx(0.4 * (6.5 + 5 / 3))
    assert b4.mass_h(6.5, dh, 75, r) == pytest.approx(11.5)          # > 70°: voll
    assert b4.tiefe(5.0, r) == 3.0                                    # Mindesttiefe


def test_giebelprofil_gestaucht(param):
    r, g = param["regel"], param["gebaeude_vorlage"]
    prof = b4.giebelprofil(g, r, "drittel")
    # Übergang zur Mindesttiefe bei 0,4·(6,5 + 5/3·u/5) = 3 → u = 3,0 m
    assert prof == [(0.0, 3.0), (3.0, 3.0), (5.0, pytest.approx(3.266667, abs=1e-6)), (7.0, 3.0), (10.0, 3.0)]
    voll = b4.giebelprofil(g, r, "voll")
    assert max(t for _, t in voll) == pytest.approx(0.4 * 11.5)


def test_szenarien(param):
    erg = {sz["id"]: b4.pruefe_szenario(param, sz, "drittel") for sz in param["szenarien"]}
    assert erg["mittig"]["zulaessig"]
    assert erg["an_strasse"]["zulaessig"]          # darf bis Straßenmitte reichen
    assert not erg["zu_nah"]["zulaessig"]
    west = next(w for w in erg["zu_nah"]["waende"] if w["wand"].startswith("West"))
    assert not west["zulaessig"]
    assert west["ueberschreitung_m2"] == pytest.approx((0.4 * (6.5 + 5 / 3) - 2.0) * 12, abs=1e-3)
    sued = next(w for w in erg["mittig"]["waende"] if w["wand"].startswith("Süd"))
    assert sued["flaeche_m2"] == pytest.approx(30 + 0.5 * 4 * (0.4 * (6.5 + 5 / 3) - 3), abs=1e-3)


def test_svg_deterministisch(param):
    sz = param["szenarien"][1]
    a = b4.svg(param, b4.pruefe_szenario(param, sz, "drittel"))
    b = b4.svg(copy.deepcopy(param), b4.pruefe_szenario(param, sz, "drittel"))
    assert a == b and a.startswith("<svg") and "#c0392b" in a


# --- B5 ------------------------------------------------------------------------

def test_treppe_290():
    loesungen, hinweise = b5.loese(2900, 900)
    assert hinweise == []
    assert {l.n_steigungen for l in loesungen} == set(range(15, 21))
    assert len(loesungen) == 68
    for l in loesungen:
        assert 140 <= l.s_mm <= 200 and 230 <= l.a_mm <= 370
        assert 590 <= l.schrittmass_mm <= 650
        assert l.lauflaenge_mm == (l.n_steigungen - 1) * l.a_mm
    beste = loesungen[0]
    assert (beste.n_steigungen, beste.a_mm) == (17, 290)
    assert beste.s_mm == pytest.approx(2900 / 17, abs=0.01)
    assert beste.schrittmass_mm == pytest.approx(2 * 2900 / 17 + 290, abs=0.01)


def test_treppe_randfaelle():
    assert b5.loese(2900, 750)[0] == []                      # Laufbreite < 80 cm
    kurz, _ = b5.loese(2900, 900, max_lauflaenge_mm=4000)
    assert all(l.lauflaenge_mm <= 4000 for l in kurz) and kurz[0].n_steigungen == 16
    assert math.ceil(2900 / 200) == 15 and math.floor(2900 / 140) == 20

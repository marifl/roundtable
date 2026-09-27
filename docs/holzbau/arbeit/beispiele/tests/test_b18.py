"""Tests zu B18 (Kranwahl, Kranstellplatz, Transport, Montagezeitplan, IFC)."""
import copy
import math

import numpy as np
import pytest

import b18_kranplanung as b18


@pytest.fixture(scope="module")
def daten():
    return b18.lade_eingabe()


@pytest.fixture(scope="module")
def b1():
    return b18.b1_gewicht()


@pytest.fixture(scope="module")
def basis(daten, b1):
    return b18.plane(copy.deepcopy(daten), "basis", 0.5, b1)


@pytest.fixture(scope="module")
def einfahrt(daten, b1):
    return b18.plane(copy.deepcopy(daten), "einfahrt_belegt", 0.5, b1)


# --- Normwerte und Formeln ----------------------------------------------------

def test_schutzabstand_und_baugrube(daten):
    assert [b18.schutzabstand_freileitung(u) for u in (0.4, 1.0, 20, 110, 220, 380, None)] == [1, 1, 3, 3, 4, 5, 5]
    bg = daten["gelaende"]["baugrube"]
    assert b18.abstand_baugrube(10, bg) == (1.0, False)
    assert b18.abstand_baugrube(36, bg) == (2.0, False)
    assert b18.abstand_baugrube(48, bg) == (3.0, True)          # > 40 t: Nachweis nötig


def test_bodenpressung_beispiele():
    # DGUV Information 208-059, Beispiele 1 und 2
    assert b18.bodenpressung(120, 0.035) == pytest.approx(3428.6, abs=0.1)
    assert b18.mindestflaeche(120, 200) == pytest.approx(0.6)
    # Liebherr-Beispiel: 1 109 kN auf 0,6 × 0,6 m, 20 % Randabzug
    assert b18.bodenpressung(1109, 0.36 * 0.8) == pytest.approx(3851, abs=1)


def test_windformel_gegen_quellen():
    # Liebherr: 85 t, A_W = 60 m², 9 m/s → rechnerisch 11,73 m/s, gilt 9 m/s
    assert 9 * math.sqrt(1.2 * 85 / 60) == pytest.approx(11.73, abs=0.01)
    assert b18.wind_zulaessig(9, 85, 60) == 9
    # Liebherr: 65 t, A_W = 280 m², Tabelle 11,1 m/s → 5,9 m/s
    assert b18.wind_zulaessig(11.1, 65, 280) == pytest.approx(5.9, abs=0.05)
    # FEM 5.016: 50 t, A_W = 100 m², 9 m/s → 7 m/s
    assert b18.wind_zulaessig(9, 50, 100) == pytest.approx(7.0, abs=0.05)


def test_traglastkurve(daten):
    ak35 = next(k for k in daten["krane"] if k["id"] == "AK-35")
    assert b18.traglast(ak35, 11.0) == pytest.approx(6.5)
    assert b18.traglast(ak35, 2.0) == 0.0 and b18.traglast(ak35, 27.0) == 0.0
    r = np.linspace(3, 26, 50)
    assert np.all(np.diff(b18.traglast(ak35, r)) <= 0)          # monoton fallend


# --- Gewichte -----------------------------------------------------------------

def test_b1_gewicht(b1):
    assert b1["bruttoflaeche_m2"] == pytest.approx(13.2)
    assert b1["masse_kg"] == pytest.approx(sum(m["masse_kg"] for m in b1["je_material"].values()), abs=0.05)
    assert b1["je_material"]["KVH C24 (Nadelholz)"]["anzahl"] == 18
    assert b1["je_material"]["Stahl, verzinkt"]["anzahl"] == 176
    assert 600 < b1["masse_kg"] < 700 and b1["flaechengewicht_kg_m2"] == pytest.approx(b1["masse_kg"] / 13.2, abs=1e-3)


def test_aufbau_flaechengewicht(daten):
    q, d = b18.flaechengewicht_aufbau(daten["aufbauten"]["decke"], daten["materialdichten_kg_m3"])
    assert q == pytest.approx(0.0125 * 800 + 0.22 * 420 * 0.096 + 0.1 * 50 * 0.904 + 0.022 * 600)
    assert d == pytest.approx(0.2545)


# --- Haus, Reihenfolge, LKW ---------------------------------------------------

def test_haus_und_reihenfolge(basis):
    el = basis["elemente"]
    arten = [e.art for e in el]
    assert (arten.count("wand") + arten.count("giebel"), arten.count("decke"), arten.count("dach")) == (12, 6, 8)
    assert b18.pruefe_reihenfolge(el) == []
    assert [e.art for e in el[:8]] == ["wand"] * 8 and el[-1].art == "dach"
    falsch = [copy.copy(e) for e in el]
    falsch[0].reihenfolge, falsch[-1].reihenfolge = falsch[-1].reihenfolge, falsch[0].reihenfolge
    assert b18.pruefe_reihenfolge(falsch)                        # Dach vor Wand wird erkannt


def test_lkw_ladungen(basis, daten):
    lkws = basis["lkws"]
    assert len(lkws) == 6
    assert [k["art"] for k in lkws] == ["innenlader", "innenlader", "plateau", "innenlader", "innenlader", "innenlader"]
    assert all(k["masse_t"] <= 24.0 and k["belegung_m"] <= k["grenze_m"] + 1e-9 for k in lkws)
    assert sum(len(k["elemente"]) for k in lkws) == 26
    assert not any(k["uebermass"] for k in lkws)
    # Übermaß: Deckenelement 3,0 m breit → Erlaubnis nach § 29 Abs. 3 StVO
    e = copy.copy(next(e for e in basis["elemente"] if e.art == "decke"))
    e.hoehe = 3.0
    art, hinw = b18.transportart(e, daten["fahrzeuge"])
    assert art == "plateau_uebermass" and "§ 29 Abs. 3 StVO" in hinw[0]


# --- Kranwahl -----------------------------------------------------------------

def test_kranwahl_basis(basis, daten):
    k = basis["beste"]
    assert (k.kran, k.x, k.y, k.ori) == ("AK-35", 18.5, 4.0, 0)
    assert k.kosten_eur == 2650 and not k.auf_strasse and k.einsatztage == 2
    assert all(u.auslastung <= daten["hub"]["auslastung_max"] for u in k.huebe)
    assert max(k.huebe, key=lambda u: u.auslastung).element == "W-N2"
    assert k.max_auslastung == pytest.approx(0.7839, abs=1e-4)
    assert k.p_kn_m2 <= k.p_zul_kn_m2
    st = basis["suche"]["statistik"]
    assert st["AK-100"]["zulaessig"] == 0                       # passt nicht auf die Stellflächen
    assert st["MBK-8"]["traglast_ok"] > st["MBK-8"]["freileitung_ok"]   # fester 45-m-Ausleger vs. Freileitung
    assert any(w["kategorie"] == "Nachbar" and "46b" in w["text"] for w in basis["warnungen"])
    assert any(w["kategorie"] == "Wind" for w in basis["warnungen"])


def test_kranwahl_einfahrt_belegt(einfahrt):
    k = einfahrt["beste"]
    assert k.kran == "AK-60" and k.auf_strasse
    assert einfahrt["suche"]["statistik"]["AK-35"]["zulaessig"] == 0
    texte = " ".join(w["text"] for w in einfahrt["warnungen"])
    assert "Sondernutzungserlaubnis" in texte and "benachbartes Anwesen" in texte


def test_raster_sensitiv(daten, b1):
    """Grobes Raster (1 m) findet den engen Stellplatz in der Einfahrt nicht."""
    k = b18.plane(copy.deepcopy(daten), "basis", 1.0, b1)["beste"]
    assert k.kran == "AK-35" and k.kosten_eur > 2650


def test_freileitung_harte_regel(basis, daten):
    mbk = next(k for k in daten["krane"] if k["id"] == "MBK-8")
    ge = basis["gelaende"]
    ok, dmin = b18.freileitung_ok(mbk, np.array([18.5, 4.0]), basis["elemente"], ge, genau=True)
    assert not ok and dmin < ge.leitung_abstand
    ak = next(k for k in daten["krane"] if k["id"] == "AK-35")
    ok, dmin = b18.freileitung_ok(ak, np.array([18.5, 4.0]), basis["elemente"], ge, genau=True)
    assert ok and dmin >= ge.leitung_abstand


# --- Zeitplan, Ausgaben --------------------------------------------------------

def test_zeitplan(basis):
    zp = basis["zeitplan"]
    assert zp["montagetage"] == 2
    tag = {v["id"]: v["beginn"][:10] for v in zp["vorgaenge"]}
    for k in basis["lkws"]:                                       # keine Ladung über Nacht geteilt
        assert len({tag[e] for e in k["elemente"]}) == 1
    assert zp["lkw"][-1]["ankunft"] == "2026-10-13T06:30:00"
    assert all(a["standzeit_min"] < 9 * 60 for a in zp["lkw"])


def test_ifc_valide_und_deterministisch(basis, daten, tmp_path):
    import ifcopenshell
    import ifcopenshell.validate
    pfade = []
    for i in range(2):
        w = b18.erzeuge_ifc(daten, basis["elemente"], basis["lkws"], basis["gelaende"], basis["beste"], basis["zeitplan"])
        p = tmp_path / f"m{i}.ifc"
        w.schreibe(p)
        pfade.append(p)
    assert pfade[0].read_bytes() == pfade[1].read_bytes()
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(pfade[0]), log, express_rules=True)
    assert log.statements == []
    f = ifcopenshell.open(str(pfade[0]))
    tasks = f.by_type("IfcTask")
    assert sum(t.PredefinedType == "INSTALLATION" for t in tasks) == 26
    assert sum(t.PredefinedType == "MOVE" for t in tasks) == 6
    assert {z.PredefinedType for z in f.by_type("IfcSpatialZone")} == {"CONSTRUCTION", "TRANSPORT", "RESERVATION"}
    assert f.by_type("IfcTransportElement")[0].PredefinedType == "LIFTINGGEAR"
    assert f.by_type("IfcConstructionEquipmentResource")[0].PredefinedType == "ERECTING"
    import ifcopenshell.util.element as ue
    w = next(x for x in f.by_type("IfcWall") if x.Name == "W-N2")
    assert ue.get_psets(w)["Qto_WallBaseQuantities"]["GrossWeight"] == pytest.approx(1228, abs=1)


def test_svg_deterministisch(basis, daten):
    a = b18.svg_be_plan(daten, basis["elemente"], basis["gelaende"], basis["beste"], "basis")
    b = b18.svg_be_plan(copy.deepcopy(daten), basis["elemente"], basis["gelaende"], basis["beste"], "basis")
    assert a == b and a.startswith("<svg") and "AK-35" in a

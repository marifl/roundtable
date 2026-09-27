"""Tests zu B17 (Grundstücksentwässerung, Rigole nach DWA-A 138-1, Routing, Regelprüfung)."""
import copy
import json
import math

import pytest
from shapely.geometry import LineString, Point

import b17_grundstuecksentwaesserung as b17


@pytest.fixture(scope="module")
def basis():
    return b17.lade()


@pytest.fixture(scope="module")
def ergebnisse(basis):
    return {s["id"]: b17.berechne(b17.szenario_daten(basis, s["id"])) for s in basis["szenarien"]}


def befund(e, pid):
    return next(p for p in e["pruefung"] if p["id"] == pid)


# --- Bemessungsformeln gegen veröffentlichte Rechnungen ------------------------

def test_rigole_speicher_gegen_veroeffentlichte_rechnung():
    """Rigole Wendeanlage Ludwigshöhstraße (uvp-verbund.de, 'Bemessung der Rigole nach
    DWA-A 138-1, Kap. 6.4.2'): A_C = 820 m², k_i = 1,04e-6 m/s, b = 8,0, h = 0,66,
    L = 8,80 m, s_R = 0,95, f_Z = 1,2 -> A_S,m = 81,49 m², Q_S = 0,08 l/s,
    V_erf = 40,52 m³ bei D = 1440 min, V_vorh = 44,1 m³, Entleerung 133 h."""
    serie = {5: 393.3, 10: 251.7, 15: 190.0, 20: 154.2, 30: 114.4, 45: 84.4, 60: 68.1, 90: 49.8, 120: 40.0,
             180: 29.3, 240: 23.4, 360: 17.1, 540: 12.5, 720: 10.0, 1080: 7.3, 1440: 5.8, 2880: 3.4,
             4320: 2.5, 5760: 2.0, 7200: 1.7}
    ki = b17.k_i(1.30e-6, 1.0, 0.80)
    assert ki == pytest.approx(1.04e-6)
    sp = b17.rigole_speicher(820.0, serie, 8.0, 0.66, 8.80, 0.95, ki, 1.2)
    assert sp["a_s"] == pytest.approx(81.49, abs=0.01)
    assert sp["q_s"] == pytest.approx(0.0847, abs=5e-4)
    assert sp["d_mass"] == 1440
    assert sp["v_erf"] == pytest.approx(40.52, abs=0.02)
    assert sp["v_vorh"] == pytest.approx(44.14, abs=0.01)
    assert sp["entleerung_h"] == pytest.approx(133, abs=1)


def test_rigolenlaenge_gegen_veroeffentlichte_rechnung():
    """Entwässerungskonzept B 166 Unterschleißheim, Anhang 1.3: A_C = 864 m², k_f = 5e-6,
    f_Ort = 0,75, b = 4,0, h = 0,35, s_R = 0,93, f_Z = 1,2 -> L = 27,45 m bei D = 360 min."""
    basis = b17.lade()
    serie = {int(k): v for k, v in basis["regen"]["t5"].items()}   # dieselbe Reihe
    ki = b17.k_i(5.0e-6, 0.75, 1.0)
    L, dd, tab = b17.rigole_laenge(864.0, serie, 4.0, 0.35, 0.93, ki, 1.2)
    assert dd == 360
    assert L == pytest.approx(27.45, abs=0.01)
    assert dict((d, l) for d, _, l in tab)[15] == pytest.approx(13.7, abs=0.05)   # Tabellenwert Quelle


def test_laenge_und_speicher_konsistent():
    """Die Längenformel ist die nach L aufgelöste Speicherbedingung: bei L_erf gilt V_erf = V_vorh."""
    serie = {5: 370.0, 60: 75.6, 240: 28.3, 1440: 7.8}
    ki = 7.2e-6
    L, _, _ = b17.rigole_laenge(131.2, serie, 0.8, 0.66, 0.95, ki, 1.2)
    sp = b17.rigole_speicher(131.2, serie, 0.8, 0.66, L, 0.95, ki, 1.2)
    assert sp["v_erf"] == pytest.approx(sp["v_vorh"], rel=1e-9)


def test_korrekturfaktor_hoechstens_eins():
    assert b17.k_i(1e-5, 1.2, 1.0) == 1e-5
    assert b17.k_i(1e-5, 0.9, 0.8) == pytest.approx(7.2e-6)


def test_mulde_einstau_und_monotonie():
    serie = {int(k): v for k, v in b17.lade()["regen"]["t5"].items()}
    a1 = b17.mulde_flaeche(131.2, serie, 7.2e-6, 1.2, 0.30)
    a2 = b17.mulde_flaeche(262.4, serie, 7.2e-6, 1.2, 0.30)
    assert 5 < a1 < a2
    v = max((r * (131.2 + a1) * 1e-4 - 7.2e-6 * a1 * 1e3) * dd * 60 * 1.2 * 1e-3 for dd, r in serie.items())
    assert v / a1 == pytest.approx(0.30, abs=1e-3)


# --- Hydraulik ------------------------------------------------------------------

def test_schmutzwasserabfluss():
    assert b17.q_ww(6.4, 0.5, 2.0) == 2.0                      # größter Einzel-DU maßgebend
    assert b17.q_ww(36.0, 0.5, 2.0) == pytest.approx(3.0)
    assert b17.q_ww(0.0, 0.5, 0.0) == 0.0


def test_teilfuellung_und_prandtl_colebrook():
    assert b17.teilfuellungsfaktor(0.5) == pytest.approx(0.5, abs=1e-12)
    assert b17.teilfuellungsfaktor(0.7) == pytest.approx(0.837, abs=0.002)
    q1 = b17.q_voll(0.146, 1 / 150, 1.0)
    q2 = b17.q_voll(0.146, 0.02, 1.0)
    assert 8.0 < q1 < 14.0 and q2 > q1                          # Größenordnung DN 150
    assert b17.q_voll(0.184, 1 / 150, 1.0) > q1


def test_regenabfluss():
    assert b17.q_regen(290.0, 1.0, 143.0) == pytest.approx(4.147, abs=1e-3)


# --- Szenarien -------------------------------------------------------------------

def test_standardfall_ohne_verstoss(ergebnisse):
    e = ergebnisse["bodenplatte"]
    stati = {p["id"]: p["status"] for p in e["pruefung"]}
    assert "Verstoß" not in stati.values() and "Erlaubnispflicht" not in stati.values()
    for p in ("SW-01", "SW-03", "SW-04", "SW-06", "SW-08", "NW-02", "NW-04", "NW-08", "NW-12", "NW-15"):
        assert stati[p] == "erfüllt", p
    assert stati["NW-05"] == "Hinweis"                          # Mulde wäre möglich -> Rigole begründen


def test_hoehenplan_regeln(ergebnisse, basis):
    e = ergebnisse["bodenplatte"]
    for h in e["schmutzwasser"]["haltungen"]:
        assert h["gefaelle"] >= h["gefaelle_min"] - 1e-5
        assert h["gefaelle"] <= basis["regeln"]["gefaelle_max"]["wert"] + 1e-5
        if h["lage"] == "Erdreich":
            assert h["gok_unten"] - h["sohle_unten"] >= 1.20 - 1e-3
    ak = e["schmutzwasser"]["anschlusskanal"]
    assert 1 / 150 <= ak["gefaelle"] <= 1.0
    # Nennweite in Fließrichtung nicht kleiner
    dn = {(h["von"], h["nach"]): h["dn"] for h in e["schmutzwasser"]["haltungen"]}
    for (a, b), n in dn.items():
        for (c, dd), m in dn.items():
            if dd == a:
                assert n >= m


def test_schaechte(ergebnisse):
    e = ergebnisse["bodenplatte"]
    s = {x["id"]: x for x in e["schmutzwasser"]["schaechte"]}
    rs = s["SW-RS"]
    assert rs["dn"] == 1000 and rs["y"] == pytest.approx(1.0) and rs["x"] == pytest.approx(8.0)
    assert all(x["bauwerk"] == "Reinigungsöffnung" for k, x in s.items() if k.startswith("FL"))
    for x in e["schmutzwasser"]["schaechte"]:
        if x["bauwerk"] == "Schacht":
            assert not x["im_gebaeude"]


def test_routing_meidet_harte_hindernisse(ergebnisse, basis):
    e = ergebnisse["bodenplatte"]
    N = e["_netze"]
    b = basis["hindernisse"]["baeume"][0]
    wurzel = Point(b["x"], b["y"]).buffer(b["kronenradius"] + basis["regeln"]["baum_wurzelzuschlag"]["wert"] - 0.01)
    rig = N["rigole"]
    for ln in N["sw"].linien():
        assert not ln.intersects(wurzel)
        assert ln.distance(rig) >= 1.0 - 1e-6
    for ln in N["nw"].linien():
        assert not ln.intersects(wurzel)
        assert not ln.crosses(N["gebaeude"])
    # jede Leitung eines Netzes kreuzt keine andere desselben Netzes
    for netz in (N["sw"], N["nw"]):
        ls = netz.linien()
        for i in range(len(ls)):
            for j in range(i + 1, len(ls)):
                x = ls[i].intersection(ls[j])
                assert x.is_empty or x.geom_type == "Point"


def test_rigole_bemessung_standard(ergebnisse):
    r = ergebnisse["bodenplatte"]["niederschlagswasser"]["rigole"]
    assert 8.0 < r["l_erforderlich"] < 11.0
    assert r["l_gewaehlt"] >= r["l_erforderlich"]
    assert r["v_vorh"] >= r["v_erf"]
    assert r["sickerraum"] >= 1.0
    assert r["abstand_gebaeude"] >= r["abstand_gebaeude_erf"] - 1e-6


def test_keller_rueckstau_und_abstand(ergebnisse):
    e = ergebnisse["keller"]
    p = befund(e, "SW-10")
    assert p["status"] == "Auflage" and "hebeanlage" in p["text"].lower() and "12050-2" in p["text"]
    r = e["niederschlagswasser"]["rigole"]
    assert r["abstand_gebaeude_erf"] > 4.5 and r["abstand_gebaeude"] >= r["abstand_gebaeude_erf"] - 1e-6
    assert befund(ergebnisse["bodenplatte"], "SW-10")["status"] == "erfüllt"


def test_kanal_zu_hoch_hebeanlage(ergebnisse):
    p = befund(ergebnisse["kanal_hoch"], "SW-06")
    assert p["status"] == "Verstoß" and "hebeanlage" in p["text"].lower()


def test_grundwasser_hoch(ergebnisse):
    e = ergebnisse["grundwasser_hoch"]
    p = befund(e, "NW-02")
    assert p["status"] == "Verstoß" and e["niederschlagswasser"]["rigole"]["sickerraum"] < 0.5


def test_nwfreiv_flaechengrenze(basis):
    d = b17.szenario_daten(basis, "bodenplatte")
    d["flaechen"][0]["flaeche"] = 1100.0              # horizontale befestigte Fläche > 1000 m²
    d["abflussbeiwerte"]["schraegdach_ziegel"]["cm"] = 0.1   # nur damit die Rigole noch auf das Grundstück passt
    e = b17.berechne(d)
    assert befund(e, "NW-04")["status"] == "Verstoß"


def test_gebuehr(ergebnisse):
    g = ergebnisse["bodenplatte"]["gebuehren"]
    assert g["nw_gebuehr_pauschal_eur_a"] == pytest.approx(600 * 0.35 * 1.77)


def test_determinismus(basis, tmp_path):
    a = b17.berechne(b17.szenario_daten(basis, "bodenplatte"))
    b = b17.berechne(b17.szenario_daten(basis, "bodenplatte"))
    ja = json.dumps(b17.export_json(a), sort_keys=True)
    assert ja == json.dumps(b17.export_json(b), sort_keys=True)
    d = b17.szenario_daten(basis, "bodenplatte")
    assert b17.svg_lageplan(d, a) == b17.svg_lageplan(d, b)


def test_ifc_valide_und_reproduzierbar(basis, tmp_path):
    ifcopenshell = pytest.importorskip("ifcopenshell")
    import ifcopenshell.validate
    import ifcopenshell.util.system as S
    d = b17.szenario_daten(basis, "bodenplatte")
    e = b17.berechne(d)
    p1 = b17.erzeuge_ifc(d, e, tmp_path / "a.ifc")
    p2 = b17.erzeuge_ifc(b17.szenario_daten(basis, "bodenplatte"), b17.berechne(b17.szenario_daten(basis, "bodenplatte")), tmp_path / "b.ifc")
    assert p1.read_bytes().replace(b"a.ifc", b"x") == p2.read_bytes().replace(b"b.ifc", b"x")
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(p1), log, express_rules=True)
    assert log.statements == []
    f = ifcopenshell.open(str(p1))
    n_halt = len(e["schmutzwasser"]["haltungen"]) + len(e["niederschlagswasser"]["haltungen"]) + 1
    assert len(f.by_type("IfcPipeSegment")) == n_halt
    assert {s.PredefinedType for s in f.by_type("IfcDistributionSystem")} == {"SEWAGE", "RAINWATER"}
    rs = next(x for x in f.by_type("IfcDistributionChamberElement") if x.Name == "SW-RS")
    assert rs.PredefinedType == "MANHOLE"
    assert [x.Name for x in S.get_connected_to(rs)] == ["Anschlusskanal SW-RS → Kanal"]
    rig = next(x for x in f.by_type("IfcDistributionChamberElement") if x.PredefinedType == "USERDEFINED")
    assert rig.ObjectType == "Versickerungsrigole"
    assert f.by_type("IfcGeographicElement")[0].PredefinedType == "TERRAIN"

"""Tests zu B15: Durchdringungen DN 100 durch Holzbalkendecke, Ständerwand, Dach."""
import copy
import xml.etree.ElementTree as ET

import ifcopenshell
import ifcopenshell.util.element as ue
import ifcopenshell.util.system as usys
import ifcopenshell.validate
import pytest

import b15_durchdringungen as b15


@pytest.fixture(scope="module")
def daten():
    return b15.lade_eingabe()


@pytest.fixture(scope="module")
def erg(daten):
    return b15.plane(daten)


def dd(erg, i):
    return next(d for d in erg["durchdringungen"] if d["id"] == i)


def test_oeffnungsdurchmesser(erg):
    """110 + 2 · (9 + 10) = 148 → 150 mm; Dach 110 + 2 · 10 = 130 mm."""
    assert erg["oeffnung_decke_wand_mm"] == 150 and erg["oeffnung_dach_mm"] == 130


def test_rasterkollision_fuehrt_zu_wechsel(erg):
    """x = 3150 liegt 25 mm neben der Balken- und Ständerachse 3125 (625er Raster);
    nächste freie Lage 3270 mm (120 mm) > zulässige 100 mm → Wechsel."""
    assert erg["strategie"] == "Wechsel"
    w = dd(erg, "D1")["wechsel"]
    assert w["balken_index"] == 5 and w["wechsel_y"] == [1955, 2245]
    assert w["stichbalken"] == [[0, 1905], [2295, 4500]]
    a = dd(erg, "D2")["auswechslung"]
    assert a["staender_index"] == 5
    assert any("3270" in h for h in erg["hinweise"])


def test_verschiebung_statt_wechsel(daten):
    d = copy.deepcopy(daten)
    d["leitung"]["verschiebung_max_mm"] = 150
    e = b15.plane(d)
    assert e["strategie"] == "Verschiebung" and e["achse_x_mm"] == 3270
    assert "wechsel" not in dd(e, "D1") and "auswechslung" not in dd(e, "D2")


def test_querbohrungen_na_6_7(erg):
    bd1, bd2 = dd(erg, "BD-1"), dd(erg, "BD-2")
    assert bd1["einstufung"].startswith("Durchbruch") and any("0,15·h" in v for v in bd1["verstoesse"])
    assert bd2["einstufung"].startswith("Querschnittsschwächung") and bd2["verstoesse"] == []
    f = b15.pruefe_balkendurchbruch
    assert f(240, 100, 36, 2000, 2680, 2600, [0, 4500])["verstoesse"] == []   # <= 50 mm: nur Querschnittsschwächung
    assert f(400, 100, 60, 2000, 2800, 2600, [0, 4500])["verstoesse"] == []   # hd = 0,15 h, mittig
    assert any("hru" in v for v in f(400, 100, 60, 2000, 2700, 2600, [0, 4500])["verstoesse"])
    assert any("lA" in v for v in f(400, 100, 60, 100, 2800, 2600, [0, 4500])["verstoesse"])


def test_fensterabstand_din1986(erg, daten):
    fe = dd(erg, "D3")["fensterabstand"][0]
    assert not fe["ok"] and fe["seitlich_mm"] == 1600 and fe["ueber_sturz_mm"] == 300
    L = {**daten["leitung"], "z_muendung": 7300}
    assert b15.pruefe_fenster(L, daten["dach"]["fenster"])[0]["ok"]
    assert b15.pruefe_fenster(daten["leitung"], [{**daten["dach"]["fenster"][0], "x_kante": 5150}])[0]["ok"]


def test_manschette_und_brandschutz(erg, daten):
    assert dd(erg, "D3")["manschette"]["id"] == "ROFLEX_100"
    assert b15.manschette(daten["manschetten"], 60) is None
    assert not dd(erg, "D1")["brandschutz"]["abschottung"]
    gk3 = b15.brandschutz({"gebaeudeklasse": 3, "nutzungseinheiten": 2}, {"feuerwiderstand": "REI 30"}, daten["leitung"])
    assert gk3["abschottung"] and "Brandschutzmanschette" in gk3["grund"]


@pytest.fixture(scope="module")
def ifc(daten, erg, tmp_path_factory):
    pfad = b15.erzeuge_ifc(daten, erg).schreibe(tmp_path_factory.mktemp("b15") / "b15.ifc")
    return ifcopenshell.open(str(pfad)), pfad


def test_ifc_valide(ifc):
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(ifc[1]), log, express_rules=True)
    assert log.statements == []


def test_ifc_durchbruchsplanung(ifc):
    f, _ = ifc
    prov = f.by_type("IfcVirtualElement")
    assert len(prov) == 4 and all(p.PredefinedType == "PROVISIONFORVOID" for p in prov)
    assert ue.get_psets(prov[0])["Pset_ProvisionForVoid"]["Diameter"] == 150
    assert len(f.by_type("IfcOpeningElement")) == 4 and len(f.by_type("IfcRelVoidsElement")) == 4
    assert len(f.by_type("IfcRelInterferesElements")) == 4
    fills = f.by_type("IfcRelFillsElement")
    assert len(fills) == 1 and fills[0].RelatedBuildingElement.ObjectType == "Luftdichtheitsmanschette"
    wechsel = [b for b in f.by_type("IfcBeam") if b.ObjectType == "Wechsel"]
    assert len(wechsel) == 2
    assert len([m for m in f.by_type("IfcMember") if m.Name.startswith("Wechselriegel")]) == 2


def test_ifc_rohr_merkmale_und_topologie(ifc):
    f, _ = ifc
    t = f.by_type("IfcPipeSegmentType")[0]
    ps = ue.get_psets(t)["Pset_PipeSegmentTypeCommon"]
    assert (ps["NominalDiameter"], ps["OuterDiameter"], ps["InnerDiameter"]) == (100, 110, 104.6)
    abzw = f.by_type("IfcPipeFitting")[0]
    assert abzw.PredefinedType == "JUNCTION"
    nachbarn = set(usys.get_connected_to(abzw)) | set(usys.get_connected_from(abzw))
    assert len(nachbarn) == 3 and len(f.by_type("IfcRelConnectsPorts")) == 3
    assert f.by_type("IfcDistributionSystem")[0].PredefinedType == "WASTEWATER"
    assert f.by_type("IfcCovering")[0].PredefinedType == "WRAPPING"


def test_btlx_rueckverfolgung(daten, erg, ifc, tmp_path):
    f, _ = ifc
    guid = f.by_type("IfcPipeSegment")[0].GlobalId
    pfad = b15.schreibe_btlx(daten, erg, tmp_path / "b.btlx", guid)
    ns = {"b": b15.NS_BTLX}
    root = ET.parse(pfad).getroot()
    teile = root.findall(".//b:Part", ns)
    assert len(teile) == 5   # D1, D2 (2 Platten), D3, BD-2 (BD-1 unzulässig → keine Bearbeitung)
    for t in teile:
        dr = t.find(".//b:Drilling", ns)
        attr = {u.get("Name"): u.text for u in dr.findall(".//b:UserAttribute", ns)}
        assert attr["LeitungGUID"] == guid
    d1 = teile[0].find(".//b:Drilling", ns)
    assert float(d1.find("b:Diameter", ns).text) == 150 and float(d1.find("b:StartX", ns).text) == 3200

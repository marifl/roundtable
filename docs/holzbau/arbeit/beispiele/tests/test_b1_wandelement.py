"""Tests zu B1: Klassen-Mapping, Mengen, Determinismus, Schema-Validierung."""
import copy
import hashlib
import os
import subprocess
import sys
import uuid

import ifcopenshell
import ifcopenshell.geom
import ifcopenshell.guid
import ifcopenshell.util.element as ue
import ifcopenshell.util.shape as us
import ifcopenshell.validate
import pytest

import b1_wandelement as b1
from conftest import BEISPIELE


@pytest.fixture(scope="module")
def param():
    return b1.lade_parameter()


@pytest.fixture(scope="module")
def ifc(param, tmp_path_factory):
    pfad = tmp_path_factory.mktemp("b1") / "wandelement.ifc"
    b1.schreibe_ifc(param, pfad)
    return ifcopenshell.open(str(pfad)), pfad


def sha(p):
    return hashlib.sha256(p.read_bytes()).hexdigest()


# --- Determinismus -------------------------------------------------------

def test_zwei_laeufe_byte_identisch(param, tmp_path):
    a, b = tmp_path / "a.ifc", tmp_path / "b.ifc"
    b1.schreibe_ifc(param, a)
    b1.schreibe_ifc(copy.deepcopy(param), b)
    assert a.read_bytes() == b.read_bytes()


def test_byte_identisch_ueber_prozesse_und_hash_seeds(tmp_path):
    """Zwei getrennte Prozesse mit verschiedenem PYTHONHASHSEED. Vor der
    Umstellung auf explizite Beziehungen (siehe IfcWandBauer.beziehung) lieferte
    dieser Test vier verschiedene Prüfsummen."""
    hashes = set()
    for seed in ("1", "4711"):
        ziel = tmp_path / f"w{seed}.ifc"
        env = dict(os.environ, PYTHONHASHSEED=seed)
        subprocess.run([sys.executable, str(BEISPIELE / "b1_wandelement.py"), "--ausgabe", str(ziel)],
                       check=True, env=env, capture_output=True, cwd=BEISPIELE)
        hashes.add(sha(ziel))
    assert len(hashes) == 1


def test_guids_eindeutig_und_aus_pfad(ifc):
    f, _ = ifc
    guids = [e.GlobalId for e in f.by_type("IfcRoot")]
    assert len(guids) == len(set(guids))
    wand = f.by_type("IfcWall")[0]
    assert wand.GlobalId == ifcopenshell.guid.compress(uuid.uuid5(b1.GUID_NAMENSRAUM, "/wand").hex)
    assert all(ifcopenshell.guid.expand(g) for g in guids)  # gültige 22-Zeichen-GUIDs


def test_guids_stabil_bei_parameteraenderung(param, ifc):
    """Brüstungshöhe ändern: Wand und Ständer außerhalb der Öffnung behalten
    ihre GlobalId, der Brüstungsriegel ebenfalls (gleicher Pfad), nur Geometrie
    und Werte ändern sich."""
    f, _ = ifc
    p2 = copy.deepcopy(param)
    p2["wand"]["oeffnungen"][0]["bruestungshoehe"] = 850
    f2 = b1.erzeuge_ifc(p2)
    alt = {e.Name: e.GlobalId for e in f.by_type("IfcMember")}
    neu = {e.Name: e.GlobalId for e in f2.by_type("IfcMember")}
    for name in ("Ständer R1", "Ständer R2", "Ständer R6", "Ständer R7", "Schwelle", "Rähm", "Brüstungsriegel F1"):
        assert alt[name] == neu[name]
    assert f.by_type("IfcWall")[0].GlobalId == f2.by_type("IfcWall")[0].GlobalId


# --- Klassen-Mapping ------------------------------------------------------

def test_klassen_und_predefined_types(ifc):
    f, _ = ifc
    assert f.schema_identifier == "IFC4X3_ADD2"
    wand = f.by_type("IfcWall")[0]
    assert wand.PredefinedType == "ELEMENTEDWALL"
    teile = [o for r in wand.IsDecomposedBy for o in r.RelatedObjects]
    klassen = {}
    for t in teile:
        klassen.setdefault((t.is_a(), t.PredefinedType), 0)
        klassen[(t.is_a(), t.PredefinedType)] += 1
    assert klassen[("IfcMember", "STUD")] == 15
    assert klassen[("IfcMember", "PLATE")] == 3
    assert klassen[("IfcPlate", "SHEET")] == 10
    assert klassen[("IfcBuildingElementPart", "INSULATION")] == 12
    assert klassen[("IfcBuildingElementPart", "USERDEFINED")] == 1
    assert klassen[("IfcMechanicalFastener", "SCREW")] == 176
    folie = next(t for t in teile if t.PredefinedType == "USERDEFINED")
    assert folie.ObjectType == "MEMBRANE"


def test_verbindungsmitteltyp(ifc):
    f, _ = ifc
    typ = f.by_type("IfcMechanicalFastenerType")[0]
    assert (typ.PredefinedType, typ.NominalDiameter, typ.NominalLength) == ("SCREW", 4.0, 50.0)
    schrauben = f.by_type("IfcMechanicalFastener")
    assert all(ue.get_type(s) == typ for s in schrauben)
    assert all(s.Representation.Representations[0].Items[0].is_a("IfcMappedItem") for s in schrauben)


def test_kerve_als_voidingfeature(ifc):
    f, _ = ifc
    vf = f.by_type("IfcVoidingFeature")
    assert len(vf) == 1 and vf[0].PredefinedType == "NOTCH"
    rel = vf[0].VoidsElements[0]
    assert rel.RelatingBuildingElement.Name == "Ständer R1"


def test_schichtaufbau_und_psets(ifc):
    f, _ = ifc
    wand = f.by_type("IfcWall")[0]
    usage = ue.get_material(wand, should_skip_usage=False)
    assert usage.is_a("IfcMaterialLayerSetUsage")
    dicken = [l.LayerThickness for l in usage.ForLayerSet.MaterialLayers]
    assert dicken == [12.5, 15.0, 0.2, 200.0, 60.0]
    ps = ue.get_psets(wand)
    assert ps["Pset_WallCommon"]["IsExternal"] is True
    assert ps["Pset_WallCommon"]["LoadBearing"] is True
    assert 0.18 < ps["Pset_WallCommon"]["ThermalTransmittance"] <= 0.20
    q = ps["Qto_WallBaseQuantities"]
    assert q["Length"] == 4800 and q["Height"] == 2750 and q["Width"] == pytest.approx(287.7)
    assert q["NetSideArea"] == pytest.approx(13.2 - 1.26 * 1.385)
    klass = [r.RelatingClassification for r in wand.HasAssociations if r.is_a("IfcRelAssociatesClassification")]
    assert klass[0].Identification == "331" and klass[0].ReferencedSource.Name == "DIN 276"


def test_georeferenz(ifc):
    f, _ = ifc
    mc = f.by_type("IfcMapConversion")[0]
    assert mc.TargetCRS.Name == "EPSG:25832"
    assert mc.Scale == 0.001  # Projekt in mm, Karte in m


def test_folie_als_ifccovering(param):
    p2 = copy.deepcopy(param)
    p2["wand"]["folie_als"] = "IfcCovering"
    f2 = b1.erzeuge_ifc(p2)
    cov = f2.by_type("IfcCovering")
    assert len(cov) == 1 and cov[0].PredefinedType == "MEMBRANE"


# --- Geometrie und Mengen ------------------------------------------------

def test_layout_holzanteil(param):
    lay = b1.rahmenlayout(param["wand"])
    assert len(lay["hoelzer"]) == 18
    assert lay["holzflaeche_mm2"] == 2_575_200
    assert lay["nettoflaeche_mm2"] == pytest.approx(4800 * 2750 - 1260 * 1385)
    # Gefache + Hölzer + Öffnung = Wandfläche
    gefache = sum(p.area for p in lay["gefache"])
    assert gefache + lay["holzflaeche_mm2"] + 1260 * 1385 == pytest.approx(4800 * 2750)


def test_nettovolumen_aus_geometrie_gleich_qto(ifc):
    """Tesselierte Geometrie (inkl. abgezogener Kerve) gegen Qto_*.NetVolume."""
    f, _ = ifc
    s = ifcopenshell.geom.settings()
    geprueft = 0
    for e in f.by_type("IfcMember") + f.by_type("IfcPlate") + f.by_type("IfcBuildingElementPart"):
        form = ifcopenshell.geom.create_shape(s, e)  # Referenz halten (sonst ungültiger Speicher)
        v = us.get_volume(form.geometry)
        qv = next(d["NetVolume"] for d in ue.get_psets(e, qtos_only=True).values() if "NetVolume" in d)
        assert v == pytest.approx(qv, abs=1e-9), e.Name
        geprueft += 1
    assert geprueft == 41
    r1 = next(m for m in f.by_type("IfcMember") if m.Name == "Ständer R1")
    assert ue.get_psets(r1)["Qto_MemberBaseQuantities"]["NetVolume"] == pytest.approx((60 * 200 * 2630 - 60 * 25 * 40) / 1e9)


def test_schema_und_regeln_valide(ifc):
    _, pfad = ifc
    log = ifcopenshell.validate.json_logger()
    ifcopenshell.validate.validate(str(pfad), log, express_rules=True)
    assert log.statements == []

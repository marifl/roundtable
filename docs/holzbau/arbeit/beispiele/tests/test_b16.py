"""Tests zu B16 (Fliesen/Parkett als 3D-Einzelobjekte, Verschnitt auf Gefälle)."""
import hashlib
import json
import math

import pytest
from shapely.geometry import box
from shapely.ops import unary_union

import b16_fliesen_verlegung as b16


@pytest.fixture(scope="module")
def daten():
    return b16.lade()


@pytest.fixture(scope="module")
def raeume(daten):
    return {e: b16.baue_raum(daten, e) for e in ("punkt", "zwei_rinnen", "eben")}


def _muster(daten, name):
    return b16.muster_bauen(name, daten["muster"][name], daten["fliesen"], daten["fuge_mm"])


@pytest.fixture(scope="module")
def faelle(daten, raeume):
    """Alle Muster × Entwässerung bei festem Rasterursprung (u, v) = (0, 0)."""
    out = {}
    for ent in ("punkt", "zwei_rinnen"):
        for mn in daten["muster"]:
            erg = b16.verlege(raeume[ent], _muster(daten, mn), 0.0, 0.0, daten["regeln"])
            out[(mn, ent)] = (erg, b16.auswerten(raeume[ent], erg, daten))
    return out


# --- Raum und Gefälle -----------------------------------------------------------

def test_achteck_und_facetten(daten, raeume):
    r_i = daten["raum"]["innenkreis_durchmesser_mm"] / 2
    a_soll = 8 * r_i ** 2 * math.tan(math.radians(22.5))          # Fläche regelmäßiges Achteck
    for r in raeume.values():
        assert r.flaeche == pytest.approx(a_soll, rel=1e-9)
        assert sum(f.poly.area for f in r.facetten) == pytest.approx(a_soll, rel=1e-9)
    punkt = raeume["punkt"]
    assert len(punkt.facetten) == 8 and len(punkt.knicke) == 8
    assert all(k.art == "kehle" for k in punkt.knicke)              # Trichter: Kehlen zur Mitte
    s = daten["gefaelle_prozent"] / 100
    for f in punkt.facetten:                                          # Wand hoch, Ablauf tief
        (x, y) = f.poly.exterior.coords[1]
        assert f.z(0, 0) == pytest.approx(0.0)
        assert f.z(x, y) == pytest.approx(s * r_i, rel=1e-9)
        assert math.hypot(f.ebene[0], f.ebene[1]) == pytest.approx(s)
    rinnen = raeume["zwei_rinnen"]
    arten = sorted(k.art for k in rinnen.knicke)
    assert arten == ["grat", "kehle", "kehle"]                      # Grat Mitte, Kehlen an den Rinnen


# --- Flächenbilanz --------------------------------------------------------------

def test_flaechenbilanz(daten, raeume, faelle):
    """Summe Fliesenflächen + Fugen = Raumfläche, ohne Überlappung, innerhalb des Raums;
    Fliesenanteil in der Verlegefläche ≈ Füllgrad des Musters."""
    for (mn, ent), (erg, kz) in faelle.items():
        raum = raeume[ent]
        polys = [s.poly for s in erg["stuecke"]]
        summe = sum(p.area for p in polys)
        vereinigt = unary_union(polys)
        assert summe == pytest.approx(vereinigt.area, abs=1.0), (mn, ent)          # keine Überlappung (mm²)
        assert vereinigt.difference(raum.raum).area < 1.0
        fugen = raum.raum.difference(vereinigt).area
        assert summe + fugen == pytest.approx(raum.flaeche, rel=1e-9)
        assert kz["verlegt_m2"] + kz["fugen_m2"] == pytest.approx(kz["raumflaeche_m2"], rel=1e-9)
        # Füllgrad: Musterfläche ohne Fugen / Zellfläche
        m = erg["muster"]
        zelle = abs(m.t1[0] * m.t2[1] - m.t1[1] * m.t2[0])
        fuell = sum(mot.soll.area for mot in m.motive) / zelle
        verlegeflaeche = sum(v.area for v in raum.verlegeflaechen)
        assert summe / verlegeflaeche == pytest.approx(fuell, abs=0.012), (mn, ent)
        assert 0.01 < fugen / raum.flaeche < 0.08


def test_fuellgrad_formeln(daten):
    f = daten["fuge_mm"]
    g = _muster(daten, "gerade_60x60")
    assert abs(g.t1[0] * g.t2[1] - g.t1[1] * g.t2[0]) == pytest.approx((600 + f) ** 2)
    fg = _muster(daten, "fischgraet_60x10")
    assert abs(fg.t1[0] * fg.t2[1] - fg.t1[1] * fg.t2[0]) == pytest.approx(2 * (600 + f) * (100 + f))
    ch = _muster(daten, "chevron_60x10")
    assert ch.motive[0].soll.area == pytest.approx((600 - 100) * 100)       # Gehrung 45°: −W² je Stab


# --- 3D und Knicklinien ----------------------------------------------------------

def test_stuecke_eben_und_nicht_ueber_knick(raeume, faelle):
    """Jedes Stück liegt in genau einer Gefälleebene; keine Fliese überbrückt eine Knicklinie."""
    for (mn, ent), (erg, _) in faelle.items():
        raum = raeume[ent]
        for s in erg["stuecke"]:
            assert raum.facetten[s.facette].poly.buffer(1e-6).contains(s.poly)
            for k in raum.knicke:
                assert s.poly.intersection(k.linie).length < 1e-6
            p3 = b16.stueck_3d(raum, s)
            a, b, c = raum.facetten[s.facette].ebene
            assert all(abs(z - (a * x + b * y + c)) < 2e-3 for x, y, z in p3)
            assert all(z >= -1e-6 for _, _, z in p3)


def test_gratschnitte_nur_mit_gefaelle(daten, raeume):
    eben = b16.verlege(raeume["eben"], _muster(daten, "fischgraet_60x10"), 0, 0, daten["regeln"])
    kz = b16.auswerten(raeume["eben"], eben, daten, mit_greedy=False)
    assert kz["schnitte_anzahl"]["gratschnitt"] == 0
    punkt = b16.verlege(raeume["punkt"], _muster(daten, "fischgraet_60x10"), 0, 0, daten["regeln"])
    kz_p = b16.auswerten(raeume["punkt"], punkt, daten, mit_greedy=False)
    assert kz_p["schnitte_anzahl"]["gratschnitt"] > 50
    assert kz_p["schnitte_gesamt"] > kz["schnitte_gesamt"]


def test_keine_unklassifizierten_schnitte(faelle):
    for key, (_, kz) in faelle.items():
        assert kz["schnitte_anzahl"]["sonstig"] == 0, key


# --- Determinismus ---------------------------------------------------------------

def test_determinismus(daten):
    def lauf():
        raum = b16.baue_raum(daten, "punkt")
        erg = b16.verlege(raum, _muster(daten, "chevron_60x10"), 0.25, 0.5, daten["regeln"])
        kz = b16.oeffentlich(b16.auswerten(raum, erg, daten))
        stueck = [(s.rohling_id, s.facette, b16.stueck_3d(raum, s), s.schnitte) for s in erg["stuecke"]]
        return json.dumps([kz, stueck], sort_keys=True)
    assert lauf() == lauf()


def test_ifc_deterministisch_und_vollstaendig(daten, tmp_path):
    import ifcopenshell
    raum = b16.baue_raum(daten, "punkt")
    erg = b16.verlege(raum, _muster(daten, "gerade_60x60"), 0, 0, daten["regeln"])
    kz = b16.auswerten(raum, erg, daten)
    hashes = {}
    for modus in ("einzeln", "aggregiert"):
        for lauf in (1, 2):
            p = tmp_path / str(lauf) / f"{modus}.ifc"          # gleicher Name → gleicher Header
            info = b16.erzeuge_ifc(daten, raum, erg, kz, modus, p)
            hashes.setdefault(modus, set()).add(hashlib.sha256(p.read_bytes()).hexdigest())
        f = ifcopenshell.open(str(p))
        cov = f.by_type("IfcCovering")
        guids = [e.GlobalId for e in f.by_type("IfcRoot")]
        assert len(guids) == len(set(guids))
        if modus == "einzeln":
            assert len(cov) == len(erg["stuecke"]) + 1
            teile = [r for r in f.by_type("IfcRelAggregates") if r.RelatingObject.is_a("IfcCovering")]
            assert len(teile) == 1 and len(teile[0].RelatedObjects) == len(erg["stuecke"])
            assert len(f.by_type("IfcPolygonalFaceSet")) == len(erg["stuecke"])
        else:
            assert len(cov) == 1
            assert len(f.by_type("IfcMappedItem")) == len(erg["stuecke"])
        qto = [q for q in f.by_type("IfcElementQuantity") if q.Name == "Qto_CoveringBaseQuantities"]
        assert qto
        gtin = [p for p in f.by_type("IfcPropertySingleValue") if p.Name == "GlobalTradeItemNumber"]
        assert gtin and gtin[0].NominalValue.wrappedValue == daten["fliesen"]["F60x60"]["gtin"]
        assert info["bytes"] > 0
    assert all(len(h) == 1 for h in hashes.values())                 # byte-identisch


# --- Verschnitt, Muster, Wiederverwendung ------------------------------------------

def test_chevron_verschnitt_groesser_als_gerade(faelle):
    for ent in ("punkt", "zwei_rinnen"):
        ch = faelle[("chevron_60x10", ent)][1]
        for gerade in ("gerade_60x10", "gerade_60x60"):
            g = faelle[(gerade, ent)][1]
            assert ch["verschnitt_nach_wiederverwendung"] > g["verschnitt_nach_wiederverwendung"], (ent, gerade)
            assert ch["verschnitt_je_position"] > g["verschnitt_je_position"], (ent, gerade)
            assert ch["schnittlaenge_gesamt_m"] > g["schnittlaenge_gesamt_m"]
        # Gehrung aus Rechteck kostet mindestens W/L = 1/6 jedes Stabs; Formteil spart das
        assert ch["verschnitt_je_position"] > 1 / 6
        ft = faelle[("chevron_60x10_formteil", ent)][1]
        assert ft["verschnitt_nach_wiederverwendung"] < ch["verschnitt_nach_wiederverwendung"] - 0.08
        assert ch["schnitte_anzahl"]["gehrung"] >= 2 * ch["anzahl_sollform_ganz"]


def test_wiederverwendung_senkt_bedarf(faelle):
    for key, (_, kz) in faelle.items():
        n_pos = sum(kz["rohlinge_je_position"].values())
        n_wv = sum(kz["rohlinge_nach_wiederverwendung"].values())
        n_naiv = sum(kz["rohlinge_naiv"].values())
        assert n_wv <= n_pos <= n_naiv, key
        assert kz["verschnitt_nach_wiederverwendung"] <= kz["verschnitt_je_position"] + 1e-12
        n_theor = kz["verlegt_m2"] * 1e6 / min(r.area for r in [m.rohling for m in faelle[key][0]["muster"].motive])
        assert n_wv >= math.floor(n_theor)                            # nicht besser als ohne Verschnitt


def test_greedy_reststueck_mit_drehung():
    """Linkes Randstück 300 mm und linkes Randstück 280 mm (andere Rasterposition):
    das zweite kommt um 180° gedreht aus dem Rest des ersten (Fabrikkante bleibt Fabrikkante)."""
    roh = box(0, 0, 600, 100)
    m = b16.np.eye(3)
    s1 = b16.Stueck("Q/0/0", "Q", "A", 0, box(0, 0, 300, 100), box(0, 0, 300, 100), m, False, False, 100.0)
    s2 = b16.Stueck("Q/5/0", "Q", "A", 0, box(0, 0, 280, 100), box(0, 0, 280, 100), m, False, False, 100.0)
    s3 = b16.Stueck("Q/9/0", "Q", "A", 0, box(0, 0, 400, 100), box(0, 0, 400, 100), m, False, False, 100.0)
    wv = b16.wiederverwendung([s1, s2, s3], {"A": roh}, 1.5, 1000)
    # s3 (400) neu, s1 (300) neu, s2 (280) aus dem 180°-gedrehten Rest von s1 (299,25 mm frei)
    assert wv["neu"]["A"] == 2
    assert wv["herkunft"][id(s2)][1] == "reststueck"
    assert wv["herkunft"][id(s2)][0] == wv["herkunft"][id(s1)][0]


def test_keine_spiegelung_bei_rechteck():
    """Symmetrien eines Rechtecks: nur 0° und 180° (keine Spiegelung, kein 90°)."""
    assert len(b16.symmetrien(box(0, 0, 600, 100))) == 2
    assert len(b16.symmetrien(box(0, 0, 600, 600))) == 4


# --- Kleinstücke und Rasteroptimierung ---------------------------------------------

def test_kleinstueck_regel(daten):
    r = daten["regeln"]
    soll = 600 * 100
    assert b16.kleinstueck(box(0, 0, 600, 100), soll, r) == \
        {"unter_flaechenanteil": False, "unter_mindestbreite": False, "verlegbar": True}
    k = b16.kleinstueck(box(0, 0, 150, 100), soll, r)                # 1/4 Stab
    assert k["unter_flaechenanteil"] and not k["unter_mindestbreite"]
    k = b16.kleinstueck(box(0, 0, 600, 15), soll, r)                 # 15 mm Streifen
    assert k["unter_mindestbreite"] and k["verlegbar"]
    assert not b16.kleinstueck(box(0, 0, 600, 4), soll, r)["verlegbar"]   # < 2 Fugen: verfugen
    dreieck = b16.Polygon([(0, 0), (100, 0), (0, 100)])
    d = b16.kleinstueck(dreieck, soll, r)
    assert b16.inkreis_durchmesser(dreieck) == pytest.approx(2 * 100 * 100 / (200 + 100 * math.sqrt(2)), abs=0.6)
    assert d["unter_flaechenanteil"] and not d["unter_mindestbreite"]


def test_rasteroptimierung(daten, raeume):
    """Grid-Search: bester Ursprung ist nie schlechter als die Mitte; es gibt eine Spanne."""
    m = _muster(daten, "gerade_60x60")
    opt = b16.optimiere(raeume["punkt"], m, daten, 4)
    assert opt["anzahl_kandidaten"] == 16
    assert opt["bester"]["zielwert_eur"] <= opt["mitte"]["zielwert_eur"]
    assert opt["bester"]["zielwert_eur"] <= opt["schlechtester"]["zielwert_eur"]
    assert opt["spanne_zielwert_eur"] > 0
    klein_bester = opt["bester"]["kleinstuecke_unter_flaechenanteil"] + opt["bester"]["kleinstuecke_unter_mindestbreite"]
    klein_schlecht = (opt["schlechtester"]["kleinstuecke_unter_flaechenanteil"]
                      + opt["schlechtester"]["kleinstuecke_unter_mindestbreite"])
    assert klein_bester <= klein_schlecht


def test_pakete(faelle, daten):
    kz = faelle[("chevron_60x10_formteil", "punkt")][1]
    assert set(kz["pakete"]) == {"C60x10_formteil_R", "C60x10_formteil_L"}   # L und R getrennt bestellen
    p = daten["fliesen"]["S60x10"]["paket_stueck"]
    kz = faelle[("fischgraet_60x10", "punkt")][1]
    n = kz["rohlinge_nach_wiederverwendung"]["S60x10"]
    assert kz["pakete"]["S60x10"] == math.ceil(n / p)

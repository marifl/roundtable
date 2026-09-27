"""Tests zum Nachweis-Framework (nachweis.py) und zur Nachrüstung B1–B5 (nachweise_b1_b5.py)."""
import html.parser
import json
import math
import re
from decimal import Decimal

import pytest

import nachweis as nw
from nachweis import (EinheitenFehler, Gegenstand, Grafik, Groesse as G, Kriterium, Nachweis, NachweisFehler, Nachweisheft,
                      Regel, Rundung, Schritt)


def regel():
    return Regel("Testregel", "Testquelle", "2026-09", "TEST", "0.0.1", "§ 1", "[V]")


def nachweis_r(d=200, lam=0.038, u_d=None, u_l=None, einheit_erg="m²·K/W", ausdruck="d/lam", nid="T-01", **kw):
    return Nachweis(
        id=nid, titel="Wärmedurchlasswiderstand", gegenstand=Gegenstand("Schicht", "0gsiGQj_bG3wx8M0qwRA0U", "IfcWall"),
        regel=regel(),
        eingaben=[G("Dicke", "d", d, "mm", "Planung", u_d), G("Wärmeleitfähigkeit", "lam", lam, "W/(m·K)", "Hersteller", u_l)],
        schritte=[Schritt("R", G("Widerstand", "R", None, einheit_erg), ausdruck)],
        ergebnis="R", grenzwert=G("Mindestwert", "R_min", 4.0, "m²·K/W", "Test"), vergleich="≥", **kw)


@pytest.fixture(params=["pint", "einfach"])
def backend(request):
    alt = nw.EINHEITEN
    nw.setze_einheiten_backend(request.param)
    yield request.param
    nw.EINHEITEN = alt


# --- Einheiten -----------------------------------------------------------------

def test_einheiten_umrechnung_korrekt(backend):
    n = nachweis_r().rechne()
    assert n.groessen()["R"].wert == pytest.approx(0.2 / 0.038, rel=1e-12)   # mm → m automatisch
    assert n.status == "erfüllt"


def test_einheitenfehler_addition_wird_erkannt(backend):
    n = nachweis_r(ausdruck="d + lam")                                        # mm + W/(m·K)
    with pytest.raises(EinheitenFehler):
        n.rechne()


def test_einheitenfehler_falsche_ergebniseinheit(backend):
    n = nachweis_r(einheit_erg="W/(m²·K)")                                    # R als U deklariert
    with pytest.raises(EinheitenFehler):
        n.rechne()


def test_einheitenfehler_im_kriterium(backend):
    n = nachweis_r()
    n.kriterien.append(Kriterium("falsch", "d", "≤", "R_min"))                 # mm gegen m²·K/W
    with pytest.raises(EinheitenFehler):
        n.rechne()


def test_winkelfunktion_braucht_dimensionslos(backend):
    ok = Nachweis("W", "t", Gegenstand("x"), regel(), [G("Neigung", "alpha", 45, "°"), G("b", "b", 10, "m")],
                  [Schritt("h", G("h", "h", None, "m"), "b/2*tan(alpha)")]).rechne()
    assert ok.groessen()["h"].wert == pytest.approx(5.0)
    falsch = Nachweis("W", "t", Gegenstand("x"), regel(), [G("b", "b", 10, "m")], [Schritt("h", G("h", "h", None, "m"), "tan(b)")])
    with pytest.raises(EinheitenFehler):
        falsch.rechne()


def test_einfache_dimensionspruefung_parser():
    e = nw.EinheitenEinfach()
    assert e.si("W/(m²·K)")[1] == e.si("kg/(s³·K)")[1]
    assert e.si("mm")[0] == pytest.approx(1e-3)
    assert e.si("m²·K/W")[0] == pytest.approx(1.0)
    with pytest.raises(EinheitenFehler):
        e.si("Furlong")


def test_auswerter_lehnt_code_ab():
    for boese in ("__import__('os')", "d.__class__", "[d]", "d if d else lam", "open('x')"):
        with pytest.raises(NachweisFehler):
            nw.parse_ausdruck(boese)
    with pytest.raises(NachweisFehler):
        Nachweis("X", "t", Gegenstand("x"), regel(), [G("a", "a", 1, "m")], [Schritt("s", G("b", "b", None, "m"), "a + c")]).rechne()


# --- Rundung --------------------------------------------------------------------

@pytest.mark.parametrize("wert, regel_, erwartet", [
    (0.18679932937799024, Rundung("signifikant", 2), "0.19"),               # ISO 6946, 6.5.2
    (0.16253, Rundung("signifikant", 2), "0.16"),
    (5.35334, Rundung("dezimalstellen", 2), "5.35"),                         # ISO 6946, 6.6
    (12.25, Rundung("dezimalstellen", 1, "halb_gerade"), "12.2"),             # ISO 80000-1 B.3 Regel A
    (12.35, Rundung("dezimalstellen", 1, "halb_gerade"), "12.4"),
    (12.25, Rundung("dezimalstellen", 1, "halb_auf"), "12.3"),                # Regel B / DIN 1333
    (-12.25, Rundung("dezimalstellen", 1, "halb_auf"), "-12.3"),
    (1225.0, Rundung("dezimalstellen", -1, "halb_gerade"), "1.22E+3"),        # Rundungsbereich 10
    (12.254, Rundung("dezimalstellen", 1), "12.3"),                           # B.4: in einem Schritt
    (9.96, Rundung("signifikant", 2), "10"),
    (0.1861, Rundung("dezimalstellen", 2, "auf"), "0.19"),
    (0.1899, Rundung("dezimalstellen", 2, "ab"), "0.18"),
    (0.0, Rundung("signifikant", 3), "0.00"),
])
def test_rundung(wert, regel_, erwartet):
    assert regel_.runde(wert) == Decimal(erwartet)


def test_rundung_nutzt_dezimaldarstellung_nicht_binaer():
    # 2.675 ist binär 2.67499999…; gerundet wird die angezeigte Dezimalzahl (repr)
    assert Rundung("dezimalstellen", 2).runde(2.675) == Decimal("2.68")


def test_rundestelle_aus_unsicherheit_din1333():
    assert nw.runde_mit_unsicherheit(8.579617, 0.0632) == ("8,58", "0,07")    # erste Ziffer 6 → Rundestelle 0,01
    assert nw.runde_mit_unsicherheit(8.579617, 0.0152) == ("8,580", "0,016")  # erste Ziffer 1 → eine Stelle weiter
    assert nw.runde_mit_unsicherheit(633.235, 1.425) == ("633,2", "1,5")
    assert nw.runde_mit_unsicherheit(530.15, 3.5) == ("530", "4")


def test_zahlformat_deutsch():
    assert nw.zahl_de(Decimal("12345.6")) == "12 345,6"
    assert nw.zahl_de(Decimal("-0.5")) == "−0,5"
    assert nw.zahl_roh(1e-8) == "1 · 10⁻⁸"
    assert nw.zahl_roh(0.2) == "0,2" and nw.zahl_roh(200.0) == "200"


def test_rechnen_ungerundet_anzeige_gerundet():
    n = nachweis_r(ergebnis_rundung=Rundung("dezimalstellen", 2)).rechne()
    assert n.groessen()["R"].wert == pytest.approx(5.2631578947)
    d = n.als_dict()
    assert d["ergebnis"]["anzeige"] == "5,26 m²·K/W"
    assert "2 Dezimalstellen" in d["ergebnis"]["rundung"]["text"]


def test_rundungsempfindlichkeit_wird_gemeldet():
    n = Nachweis("RU", "t", Gegenstand("x"), regel(), [G("R_T", "R_T", 1 / 0.2049, "m²·K/W")],
                 [Schritt("U", G("U", "U", None, "W/(m²·K)"), "1/R_T")], ergebnis="U",
                 grenzwert=G("U_max", "U_max", 0.20, "W/(m²·K)"), vergleich="≤",
                 ergebnis_rundung=Rundung("signifikant", 2)).rechne()
    k = n.kriterien[0]
    assert n.status == "nicht erfüllt" and k.rundungsempfindlich        # 0,2049 → „0,20“ sähe erfüllt aus
    assert any("gerundete Anzeigewert" in h for h in n.als_dict()["hinweise"])


# --- Hash und Determinismus -----------------------------------------------------------

def test_hash_deterministisch_und_inhaltsbezogen(monkeypatch):
    h1 = nachweis_r().hash
    h2 = nachweis_r().hash
    assert h1 == h2 and re.fullmatch(r"[0-9a-f]{64}", h1)
    assert nachweis_r(zeitstempel="2026-09-27T12:00:00+00:00").hash == h1   # Zeitstempel nicht im Hash
    monkeypatch.setenv("SOURCE_DATE_EPOCH", "1790000000")
    n = nachweis_r()
    assert n.zeitstempel.startswith("2026-") and n.hash == h1
    assert nachweis_r(d=201).hash != h1                                  # Inhalt ändert den Hash
    assert nw.inhalts_hash(nachweis_r().als_dict()) == h1                # nachprüfbar aus dem JSON


def test_json_byte_identisch_und_heft_hash():
    a = nachweis_r(u_d=2.0, u_l=0.001, monte_carlo=2000).json()
    b = nachweis_r(u_d=2.0, u_l=0.001, monte_carlo=2000).json()
    assert a == b
    h1 = Nachweisheft("Heft", {"Projekt": "Test"}, [nachweis_r()]).als_dict()["hash"]["wert"]
    h2 = Nachweisheft("Heft", {"Projekt": "Test"}, [nachweis_r()]).als_dict()["hash"]["wert"]
    assert h1 == h2


# --- Unsicherheit -------------------------------------------------------------------------

def test_unsicherheit_produkt_analytisch():
    a, b, ua, ub = 4.8, 2.75, 0.01, 0.02
    n = Nachweis("U1", "Fläche", Gegenstand("x"), regel(),
                 [G("a", "a", a, "m", "", ua), G("b", "b", b, "m", "", ub)],
                 [Schritt("A", G("A", "A", None, "m²"), "a*b")], ergebnis="A").rechne()
    u = n.unsicherheit
    assert u["u_c"] == pytest.approx(math.hypot(b * ua, a * ub), rel=1e-6)
    assert u["U"] == pytest.approx(2 * u["u_c"])
    sens = {x["symbol"]: x["sensitivitaet"] for x in u["beitraege"]}
    assert sens == pytest.approx({"a": b, "b": a}, rel=1e-6)
    assert sum(x["anteil"] for x in u["beitraege"]) == pytest.approx(1.0)


def test_unsicherheit_quotient_mit_einheiten(backend):
    n = nachweis_r(u_d=2.0, u_l=0.001).rechne()
    R = 0.2 / 0.038
    erwartet = R * math.hypot(2.0 / 200, 0.001 / 0.038)                 # relative Unsicherheiten addieren quadratisch
    assert n.unsicherheit["u_c"] == pytest.approx(erwartet, rel=1e-6)
    assert n.unsicherheit["beitraege"][0]["sensitivitaet"] == pytest.approx(R / 200, rel=1e-6)  # (m²K/W)/mm


def test_unsicherheit_korrelation_ueber_kette():
    """y = z + x mit z = x: volle Korrelation → u(y) = 2·u(x), nicht √2·u(x)."""
    n = Nachweis("U2", "Korrelation", Gegenstand("x"), regel(), [G("x", "x", 3.0, "m", "", 0.1)],
                 [Schritt("z", G("z", "z", None, "m"), "x"), Schritt("y", G("y", "y", None, "m"), "z + x")],
                 ergebnis="y").rechne()
    assert n.unsicherheit["u_c"] == pytest.approx(0.2, rel=1e-6)


def test_monte_carlo_stimmt_bei_linearem_modell():
    n = Nachweis("U3", "MC", Gegenstand("x"), regel(), [G("a", "a", 10.0, "m", "", 0.3), G("b", "b", 5.0, "m", "", 0.4, verteilung="rechteck")],
                 [Schritt("s", G("s", "s", None, "m"), "a + 2*b")], ergebnis="s", monte_carlo=200_000).rechne()
    mc = n.unsicherheit["monte_carlo"]
    assert mc["mittelwert"] == pytest.approx(20.0, abs=0.01)
    assert mc["standardabweichung"] == pytest.approx(math.hypot(0.3, 0.8), rel=0.01)
    assert n.unsicherheit["u_c"] == pytest.approx(math.hypot(0.3, 0.8), rel=1e-6)


def test_entscheidung_innerhalb_unsicherheit_wird_gemeldet():
    n = Nachweis("U4", "knapp", Gegenstand("x"), regel(), [G("R", "R_T", 5.1, "m²·K/W", "", 0.1)],
                 [Schritt("U", G("U", "U", None, "W/(m²·K)"), "1/R_T")], ergebnis="U",
                 grenzwert=G("U_max", "U_max", 0.20, "W/(m²·K)"), vergleich="≤").rechne()
    assert n.status == "erfüllt" and n.kriterien[0].innerhalb_unsicherheit


# --- Rendering ---------------------------------------------------------------------------

class _Tagbilanz(html.parser.HTMLParser):
    LEER = {"meta", "br", "img", "input", "link", "hr", "path", "rect", "line", "circle", "polygon", "polyline", "use", "stop"}

    def __init__(self):
        super().__init__()
        self.stapel, self.fehler = [], []

    def handle_starttag(self, tag, attrs):
        if tag not in self.LEER:
            self.stapel.append(tag)

    def handle_startendtag(self, tag, attrs):
        pass

    def handle_endtag(self, tag):
        if tag in self.LEER:
            return
        if not self.stapel or self.stapel[-1] != tag:
            self.fehler.append((tag, self.stapel[-3:]))
        else:
            self.stapel.pop()


def pruefe_html(text: str) -> None:
    assert text.startswith("<!DOCTYPE html>") and '<html lang="de">' in text
    p = _Tagbilanz()
    p.feed(text)
    assert not p.fehler and not p.stapel, (p.fehler[:3], p.stapel)
    for svg in re.findall(r"<svg.*?</svg>", text, flags=re.S):
        assert nw.svg_ist_valide(svg)


@pytest.fixture(params=["matplotlib", "svg"])
def grafik_backend(request, monkeypatch):
    if request.param == "svg":
        monkeypatch.setattr(nw, "_mpl", lambda: None)
    return request.param


def test_svg_grafiken_valide(grafik_backend):
    from shapely.geometry import box
    svgs = [
        nw.diagramm_ist_grenzwert([{"label": "U", "ist": 0.187, "grenz": 0.2, "vergleich": "≤", "U": 0.007}], "W/(m²·K)", "U"),
        nw.diagramm_balken([{"label": "a", "wert": 3.0}, {"label": "b", "wert": 5.0, "U": 0.5}], "kg", "Massen"),
        nw.diagramm_punkte([{"x": 1, "y": 2, "gruppe": "g"}, {"x": 2, "y": 3, "gruppe": "g"}], "x", "y", "Punkte",
                           bereich=[(0, 0), (3, 0), (3, 4)], hervorgehoben={"x": 1, "y": 2, "label": "h"}),
        nw.lageplan_svg(box(0, 0, 20, 30), box(5, 9, 15, 21), [{"polygon": box(1, 9, 5, 21), "ok": True, "label": "W"}],
                        strasse=box(0, -4, 20, 0), bemassungen=[{"a": (0, 15), "b": (5, 15)}], schriftfeld=["Test", "M 1:200"]),
        nw.schnitt_svg([{"name": "A", "dicke_mm": 12.5, "muster": "gips"}, {"name": "B", "dicke_mm": 200, "muster": "daemmung"}], 625,
                       einlagen=[{"schicht_index": 1, "x0_mm": 282.5, "breite_mm": 60}]),
        nw.treppenschnitt_svg(17, 2900 / 17, 290),
        nw.balken_anteil_svg([("ok", 5, "#0ca30c"), ("fehler", 1, "#d03b3b")], "Anteil"),
    ]
    for s in svgs:
        assert nw.svg_ist_valide(s), s[:200]
        assert "Date" not in s and "<dc:date>" not in s                       # keine Zeitangaben
    # technische Zeichnungen sind maßstäblich: Breite in mm
    assert re.search(r'width="[\d.]+mm"', svgs[3]) and re.search(r'viewBox="0 0 [\d.]+ [\d.]+"', svgs[3])


def test_svg_deterministisch():
    a = nw.diagramm_balken([{"label": "a", "wert": 3.0}], "kg", "M")
    b = nw.diagramm_balken([{"label": "a", "wert": 3.0}], "kg", "M")
    assert a == b


def test_html_markdown_json_schema(tmp_path):
    n = nachweis_r(u_d=2.0, u_l=0.001)
    n.grafiken.append(Grafik("g1", "Test", nw.balken_anteil_svg([("ok", 1, "#0ca30c")], "t")))
    pruefe_html(n.html())
    md = n.markdown()
    assert "$$" in md and "| Größe | Symbol |" in md and "[ERFÜLLT]" in md and "U(k" not in md
    d = json.loads(n.json())
    nw.pruefe_schema(d)
    heft = Nachweisheft("Heft", {"Projekt": "Test"}, [n, nachweis_r(d=100, nid="T-02")])
    pfade = heft.schreibe(tmp_path, "heft")
    nw.pruefe_schema(json.loads(pfade["json"].read_text(encoding="utf-8")))
    pruefe_html(pfade["html"].read_text(encoding="utf-8"))
    assert (tmp_path / "svg" / "T-01_g1.svg").exists()
    assert json.loads(pfade["json"].read_text(encoding="utf-8"))["status"] == "nicht erfüllt"   # d = 100 mm reicht nicht


def test_schema_lehnt_fehlerhaftes_dokument_ab():
    import jsonschema
    d = nachweis_r().als_dict()
    d["status"] = "vielleicht"
    with pytest.raises(jsonschema.ValidationError):
        nw.pruefe_schema(d)


# --- Nachrüstung B1–B5 ------------------------------------------------------------------------

@pytest.fixture(scope="module")
def alle():
    import nachweise_b1_b5 as nb
    return nb.alle_nachweise()


def test_retrofit_b2_stimmt_mit_ifctester(alle):
    import b2_ids_pruefung as b2
    assert all(n.status == "erfüllt" for n in alle["b2_bestanden"]) and len(alle["b2_bestanden"]) == 11
    fehl = {n.id.rsplit("-", 2)[-2] + "-" + n.id.rsplit("-", 1)[-1] for n in alle["b2_fehlerhaft"] if n.status != "erfüllt"}
    assert fehl == b2.ERWARTET_FEHLERHAFT


def test_retrofit_b3_ergebnisse_unveraendert(alle):
    import b3_uwert_iso6946 as b3
    p = b3.lade_parameter()
    werte = {n.id: n.groessen()["U"].wert for n in alle["b3"]}
    assert werte["N-B3-raster-verputzt"] == pytest.approx(b3.berechne_uwert(p, b3.holzanteil_raster(p), "verputzt").u_wert, abs=5e-7)
    assert werte["N-B3-geometrie-verputzt"] == pytest.approx(b3.uwert_fuer_ifc(p), abs=5e-4)
    geo = next(n for n in alle["b3"] if n.id == "N-B3-geometrie-verputzt").als_dict()
    assert geo["ergebnis"]["anzeige"] == "0,19 W/(m²·K)"                   # ISO 6946, 6.5.2: zwei signifikante Stellen
    assert all(g["uebereinstimmung"] for n in alle["b3"] for g in n.gegenrechnungen)
    assert geo["unsicherheit"]["monte_carlo"]["intervall_95"][1] < 0.20


def test_retrofit_b4_b5(alle):
    st = {n.id: n.status for n in alle["b4"]}
    assert st == {"N-B4-mittig-drittel": "erfüllt", "N-B4-zu_nah-drittel": "nicht erfüllt",
                  "N-B4-an_strasse-drittel": "erfüllt", "N-B4-mittig-voll": "erfüllt"}
    b5 = alle["b5"][0].groessen()
    assert (b5["n"].wert, b5["a"].wert, b5["N_L"].wert, b5["l_L"].wert) == (17, 290, 68, 4640)
    assert b5["S"].wert == pytest.approx(2 * 2900 / 17 + 290)


def test_retrofit_b1_konsistent_mit_ifc(alle):
    n = alle["b1"][0]
    assert n.status == "erfüllt" and n.gegenstand.ifc_guid == "0gsiGQj_bG3wx8M0qwRA0U"
    assert n.groessen()["V_H"].wert == pytest.approx(0.51498, abs=1e-9)
    assert len(n.gegenstand.weitere_guids) == 18


def test_retrofit_hefte_schema_und_html(alle, tmp_path):
    for key, liste in alle.items():
        heft = Nachweisheft(key, {"Projekt": "Test"}, liste)
        d = heft.als_dict()
        nw.pruefe_schema(d)
        for n in d["nachweise"]:
            assert n["grafiken"], n["id"]                                   # jeder Nachweis hat einen grafischen Teil
            assert all(nw.svg_ist_valide(g["svg"]) for g in n["grafiken"])
    pruefe_html(Nachweisheft("B3", {"Projekt": "Test"}, alle["b3"]).html())


def test_hash_unabhaengig_vom_einheiten_backend():
    alt = nw.EINHEITEN
    try:
        nw.setze_einheiten_backend("einfach")
        a = nachweis_r(u_d=2.0, u_l=0.001).hash
        nw.setze_einheiten_backend("pint")
        b = nachweis_r(u_d=2.0, u_l=0.001).hash
    finally:
        nw.EINHEITEN = alt
    assert a == b


def test_nachweishefte_byte_identisch_ueber_prozesse(tmp_path):
    """Zwei Läufe in getrennten Prozessen mit verschiedenem PYTHONHASHSEED → identische Dateien."""
    import hashlib
    import os
    import subprocess
    import sys
    from pathlib import Path
    hier = Path(nw.__file__).parent
    stände = []
    for seed in ("1", "4711"):
        ziel = tmp_path / seed
        env = dict(os.environ, PYTHONHASHSEED=seed)
        env.pop("SOURCE_DATE_EPOCH", None)
        subprocess.run([sys.executable, str(hier / "nachweise_b1_b5.py"), "--ausgabe", str(ziel)], cwd=hier, env=env,
                       check=True, capture_output=True)
        stände.append({p.relative_to(ziel).as_posix(): hashlib.sha256(p.read_bytes()).hexdigest()
                       for p in sorted(ziel.rglob("*")) if p.is_file()})
    assert stände[0] == stände[1] and len(stände[0]) > 60

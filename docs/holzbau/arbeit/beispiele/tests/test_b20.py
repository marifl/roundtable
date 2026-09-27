"""Tests zu B20: Schallprognose DIN ISO 9613-2 / TA Lärm und Aufstelloptimierung Wärmepumpe.

Die Handrechnungen rechnen die Normformeln hier im Test unabhängig nach (eigene Zeilen,
nicht über die Modulfunktionen), damit ein Fehler im Modul nicht in beide Seiten eingeht.
"""
import copy
import json
import math

import pytest

import b20_waermepumpe_schall as b20

LAM = 340.0 / 500.0          # ISO 9613-2 Gl. (19), 500 Hz
ALPHA = 1.9                   # ISO 9613-2 Tab. 2, 500 Hz, 10 °C, 70 %


def leere_daten(gebaeude=(), mauern=(), ordnung=2):
    """Minimale Szene ohne Hindernisse (für Handrechnungen)."""
    return {"gebaeude": list(gebaeude), "mauern": list(mauern),
            "berechnung": {"frequenz_Hz": 500.0, "alpha_dB_km": ALPHA, "C0_dB": 0.0,
                           "reflexion_ordnung_max": ordnung, "reflexion_radius_2_ordnung_m": 6.0,
                           "eigene_fassade_io_ignorieren": True}}


@pytest.fixture(scope="module")
def daten():
    return b20.lade_eingabe()


@pytest.fixture(scope="module")
def erg(daten):
    return b20.rechne(daten, mit_karte=False)


# ---------------------------------------------------------------- Handrechnungen ISO 9613-2
def test_handrechnung_freifeld_adiv_domega_agr():
    """S und R in 1 m Höhe, d = 10 m, kein Hindernis:
    A_div = 20 lg 10 + 11 = 31,000 dB; D_Ω = 10 lg(1 + 100/104) = 2,926 dB;
    A_gr = max(0; 4,8 − 0,2·(17 + 30)) = 0; A_atm = 1,9·10/1000 = 0,019 dB
    → L = 55 + 2,926 − 31 − 0,019 = 26,907 dB(A)."""
    sz = b20.Szene(leere_daten())
    adiv = 20 * math.log10(10.0) + 11
    dom = 10 * math.log10(1 + 100 / 104)
    agr = max(0.0, 4.8 - (2 * 1.0 / 10) * (17 + 300 / 10))
    soll = 55.0 + dom - adiv - ALPHA * 10 / 1000 - agr
    assert adiv == pytest.approx(31.0, abs=1e-12)
    assert dom == pytest.approx(2.9259, abs=1e-4) and agr == 0.0
    assert sz.pegel((0.0, 0.0), 1.0, (10.0, 0.0), 1.0, 55.0) == pytest.approx(soll, abs=1e-9)
    assert soll == pytest.approx(26.907, abs=1e-3)


def test_bodeneffekt_alternativ_ab_etwa_25_m():
    """Gl. (10) mit h_m = 1,75 m wird erst ab rund 22–25 m positiv (LAI: „ab etwa 25 m wirksam")."""
    assert b20.a_gr_alternativ(20.0, 1.75) == 0.0
    assert b20.a_gr_alternativ(30.0, 1.75) == pytest.approx(4.8 - (3.5 / 30) * (17 + 10), abs=1e-12)


def test_handrechnung_abschirmung_mauer():
    """Mauer h = 3 m, Dicke 0,24 m, sehr lang (seitliche Pfade irrelevant), mittig zwischen
    S (0/0, 1 m) und R (10/0, 1 m): Doppelkante e = 0,24 m in 3 m Höhe.
    d_ss = d_sr = √(4,88² + 2²) = 5,2739 m; z = 2·5,2739 + 0,24 − 10 = 0,7879 m;
    C3 = [1 + (5λ/e)²]/[1/3 + (5λ/e)²] = 1,0033; K_met = exp(−√(d_ss d_sr d/(2z))/2000) = 0,9934;
    D_z = 10 lg(3 + 20/λ · C3 · z · K_met) = 14,17 dB; A_gr = 0 → A_bar = D_z."""
    dss = math.hypot(4.88, 2.0)
    z = 2 * dss + 0.24 - 10.0
    q = (5 * LAM / 0.24) ** 2
    c3 = (1 + q) / (1 / 3 + q)
    km = math.exp(-(1 / 2000) * math.sqrt(dss * dss * 10.0 / (2 * z)))
    dz = 10 * math.log10(3 + (20 / LAM) * c3 * z * km)
    assert z == pytest.approx(0.7879, abs=1e-4) and c3 == pytest.approx(1.0033, abs=1e-4)
    assert km == pytest.approx(0.9934, abs=1e-4) and dz == pytest.approx(14.17, abs=0.01)
    mauer = {"id": "M", "name": "Testmauer", "achse": [[5.0, -500.0], [5.0, 500.0]], "dicke_m": 0.24,
             "hoehe_m": 3.0, "rho": 0.0}   # ρ = 0: keine Reflexion, nur Abschirmung
    ohne = b20.Szene(leere_daten()).pegel((0.0, 0.0), 1.0, (10.0, 0.0), 1.0, 55.0)
    mit, det = b20.Szene(leere_daten(mauern=[mauer])).pegel((0.0, 0.0), 1.0, (10.0, 0.0), 1.0, 55.0, mit_details=True)
    assert det["direkt"]["oben"]["z_m"] == pytest.approx(z, abs=1e-9)
    assert ohne - mit == pytest.approx(dz, abs=1e-6)
    assert all(not p["relevant"] for p in det["direkt"]["seitlich"])


def test_dz_negativer_umweg_stetig_und_begrenzt():
    """ISO 9613-2:1996: z < 0 → D_z < 4,77 dB, bei z = −λ/10 genau 0; Kappung 20/25 dB."""
    assert b20.d_z(0.0, LAM, 1.0, 1.0, 20.0) == pytest.approx(10 * math.log10(3), abs=1e-12)
    assert b20.d_z(-LAM / 10, LAM, 1.0, 1.0, 20.0) == 0.0
    assert b20.d_z(100.0, LAM, 1.0, 1.0, 20.0) == 20.0
    assert b20.d_z(100.0, LAM, 3.0, 1.0, 25.0) == 25.0


def test_reflexion_wand_plus_3_dB_und_ecke_plus_6_dB():
    """Spiegelquelle ρ = 1 direkt hinter der Quelle: +10 lg 2 = +3,0 dB (LAI „vor einer Hauswand");
    Innenecke aus zwei Wänden: 3 Spiegelquellen (2× 1., 1× 2. Ordnung) → +10 lg 4 = +6,0 dB."""
    wand_y = {"id": "W1", "name": "Wand", "achse": [[-0.24, -0.12], [60.0, -0.12]], "dicke_m": 0.24, "hoehe_m": 20.0, "rho": 1.0}
    wand_x = {"id": "W2", "name": "Wand", "achse": [[-0.12, -0.24], [-0.12, 60.0]], "dicke_m": 0.24, "hoehe_m": 20.0, "rho": 1.0}
    S, R, h = (0.02, 0.01), (30.0, 20.0), 1.0   # nicht diagonal: Pfad 2. Ordnung nicht durch die Ecke
    frei = b20.Szene(leere_daten()).pegel(S, h, R, h, 55.0)
    eine = b20.Szene(leere_daten(mauern=[wand_y])).pegel(S, h, R, h, 55.0)
    ecke = b20.Szene(leere_daten(mauern=[wand_y, wand_x])).pegel(S, h, R, h, 55.0)
    assert eine - frei == pytest.approx(10 * math.log10(2), abs=0.02)
    assert ecke - frei == pytest.approx(10 * math.log10(4), abs=0.05)
    ecke_1 = b20.Szene(leere_daten(mauern=[wand_y, wand_x], ordnung=1)).pegel(S, h, R, h, 55.0)
    assert ecke_1 - frei == pytest.approx(10 * math.log10(3), abs=0.05)   # ohne 2. Ordnung nur +4,8 dB


def test_monotonie_mit_abstand():
    sz = b20.Szene(leere_daten())
    werte = [sz.pegel((0.0, 0.0), 0.8, (d, 0.0), 4.3, 55.0) for d in (1, 2, 4, 8, 16, 32, 64, 128)]
    assert all(a > b for a, b in zip(werte, werte[1:]))
    gleich_hoch = [sz.pegel((0.0, 0.0), 2.0, (d, 0.0), 2.0, 55.0) for d in (8.0, 16.0)]
    # gleiche Höhen, A_gr = 0: Differenz = 6,02 dB (A_div) − ΔD_Ω − ΔA_atm
    soll = 20 * math.log10(2) - (10 * math.log10(1 + 64 / 80) - 10 * math.log10(1 + 256 / 272)) + ALPHA * 8 / 1000
    assert gleich_hoch[0] - gleich_hoch[1] == pytest.approx(soll, abs=1e-9)


def test_gartenmauer_senkt_pegel(daten):
    """Ostseite hinter der Mauer M1, IO5-Stützpunkt Baugrenze in 2 m Höhe: Mauer mindert."""
    S, R = (16.25, 15.25), (21.0, 15.5)
    mit = b20.Szene(daten).pegel(S, 0.8, R, 2.0, 55.0)
    ohne = b20.Szene(daten, mit_mauer=False).pegel(S, 0.8, R, 2.0, 55.0)
    assert ohne - mit > 5.0


# ---------------------------------------------------------------- vereinfachte Verfahren
def test_lai_tabelle5_aus_iso9613_reproduziert():
    """LAI 2023 Tab. 5 ist ISO 9613-2 Gl. (7), (8), (10), (11) mit h_s = 1,5 m, h_r = 2 m, α = 2 dB/km
    und Ziel IRW − 6 dB: alle 41 WR-Werte auf ≤ 0,11 m getroffen; WA/MI sind um 5/10 dB versetzt."""
    for i, soll in enumerate(b20.LAI_TAB5_WR):
        assert b20.lai_mindestabstand(40.0 + i, "WR") == pytest.approx(soll, abs=0.11)
    assert b20.lai_mindestabstand(55.0, "WA") == pytest.approx(3.9, abs=0.11)
    assert b20.lai_mindestabstand(60.0, "MI") == pytest.approx(3.9, abs=0.11)
    # LAI Kap. 4.2: nächsthöherer Emissionspegel → 52,4 dB wird 53 dB, Spalte WA: 3,0 m
    assert b20.lai_tabelle5(52.4, "WA") == 3.0

def test_bwp_beispiel_leitfaden():
    """BWP-Leitfaden Schall Kap. 4.3: L_W 59/51 dB, K_T 3, K0 6 (Wand), s = 6 m, K_R 6:
    L_r,T = 47,4 dB(A), L_r,N = 33,4 dB(A)."""
    assert b20.bwp_lr(59, 3, 6, 6.0, KR=6) == pytest.approx(47.4, abs=0.05)
    assert b20.bwp_lr(51, 3, 6, 6.0) == pytest.approx(33.4, abs=0.05)


# ---------------------------------------------------------------- TA Lärm
def test_beurteilungspegel_tag_mit_ruhezeitenzuschlag():
    """Beispiel IZU/Umweltpakt Bayern: konstant 56 dB(A) 06–22 Uhr im WA → L_r,T = 57,9 dB(A)."""
    wp = {"KT_dB": 0.0, "KI_dB": 0.0, "einwirkzeit_nacht_min": 60, "LWA_max_dB": 0.0, "LWA_nacht_dB": 0.0,
          "quelle_KT": "", "quelle_KI": "", "quelle_LWA": ""}
    be = b20.beurteilung(30.0, 56.0, 40.0, wp, "WA", "T")
    assert be["L_r_T"] == pytest.approx(57.9, abs=0.05)
    assert be["L_r_N"] == pytest.approx(30.0, abs=1e-12)


def test_rundung_din1333():
    assert b20.runde_din1333(40.5) == 41 and b20.runde_din1333(40.49) == 40
    assert b20.runde_din1333(1.499) == 1 and b20.runde_din1333(2.5) == 3
    assert b20.runde_din1333(-2.5) == -3


# ---------------------------------------------------------------- Aufstellregeln
def test_r290_schutzbereich_schliesst_hwr_fenster_aus(daten):
    sz = b20.Szene(daten)
    ok, gruende, _ = b20.pruefe_standort((15.0, 12.0), daten, sz, daten["waermepumpe"], [(21.0, 15.0)])
    assert not ok and any("HWR" in g for g in gruende)


def test_f_gase_split_r32_ab_2027_verboten(daten):
    sp = copy.deepcopy(daten["waermepumpe"])
    sp.update(daten["variante_split"])
    assert b20.f_gase_pruefung(sp, "2026-09-27")["status"].startswith("zulässig bis 2026-12-31")
    assert b20.f_gase_pruefung(sp, "2027-01-01")["status"].startswith("verboten")
    assert b20.f_gase_pruefung(daten["waermepumpe"], "2033-01-01")["status"] == "zulässig"   # R290


# ---------------------------------------------------------------- Optimierung
def test_optimum_erfuellt_richtwert_und_ist_maximal(erg, daten):
    opt = erg["optimum"]
    for z in opt["tabelle"]:
        assert z["L_r_N_gerundet"] <= z["IRW_N"] and z["L_r_T_gerundet"] <= z["IRW_T"]
        assert z["L_AFmax_N"] <= z["IRW_N"] + 20
    zul = [k for k in erg["_intern"]["kandidaten"] if k["zulaessig"]]
    assert opt["reserve_min_N_dB"] >= max(k["reserve_min"] for k in zul) - 1e-12
    ok, gruende, _ = b20.pruefe_standort(tuple(opt["xy"]), daten, erg["_intern"]["szene"], daten["waermepumpe"],
                                         [io["xy"] for io in erg["_intern"]["ios"]])
    assert ok, gruende


def test_sensitivitaet_lwa_linear(erg):
    for ort, s in erg["sensitivitaet_reserve_min_N_dB"].items():
        if isinstance(s, dict):
            assert s["LWA_+1dB"] == pytest.approx(s["basis"] - 1.0, abs=1e-9)
            assert s["LWA_-1dB"] == pytest.approx(s["basis"] + 1.0, abs=1e-9)


def test_determinismus(daten, erg):
    zweit = b20.rechne(copy.deepcopy(daten), mit_karte=False)
    assert json.dumps(b20._json_sicher(erg), sort_keys=True) == json.dumps(b20._json_sicher(zweit), sort_keys=True)


def test_isolinien_marching_squares():
    """Radialsymmetrisches Feld: Isolinie 40 liegt auf dem Kreis r = 5 (Pegel 45 − r)."""
    import numpy as np
    xs = ys = np.arange(-10.0, 10.01, 0.5)
    Z = np.array([[45.0 - math.hypot(x, y) for x in xs] for y in ys])
    seg = b20.marching_squares(xs, ys, Z, 40.0)
    assert seg and all(abs(math.hypot(a, b) - 5.0) < 0.05 for a, b, _, _ in seg)

"""Tests zu B6 (deterministische Sprachpipeline) und B7 (BTLx, optional)."""
import copy
import hashlib

import pytest

import b6_intent_pipeline as b6


@pytest.mark.parametrize("text, wert, dim, muster", [
    ("eins zwanzig", 1.20, "laenge", "C"),
    ("einen Meter zwanzig", 1.20, "laenge", "A"),
    ("1,20 m", 1.20, "laenge", "B"),
    ("1.20m", 1.20, "laenge", "B"),
    ("120 cm", 1.20, "laenge", "B"),
    ("35 Grad", 35.0, "winkel", "B"),
    ("35°", 35.0, "winkel", "B"),
    ("fünfunddreißig Grad", 35.0, "winkel", "B"),
    ("zwölf Quadratmeter", 12.0, "flaeche", "B"),
    ("12 m²", 12.0, "flaeche", "B"),
    ("zwei Meter fünfzig", 2.50, "laenge", "A"),
    ("drei komma fünf Meter", 3.5, "laenge", "B"),
    ("achtzig Zentimeter", 0.80, "laenge", "B"),
    ("anderthalb Meter", 1.5, "laenge", "B"),
    ("einen halben Meter", 0.5, "laenge", "B"),
    ("zweihundertzwanzig Zentimeter", 2.20, "laenge", "B"),
])
def test_parser(text, wert, dim, muster):
    m = b6.parse_masse(text)
    assert len(m) == 1, m
    assert m[0].wert == pytest.approx(wert) and m[0].dim == dim and m[0].muster == muster


def test_parser_mehrdeutig_und_zahlwoerter():
    m = b6.parse_masse("eins fünf")
    assert m[0].mehrdeutig
    assert b6.zahlwort("einundneunzig") == 91
    assert b6.zahlwort("hundertfuenf") == 105
    assert b6.zahlwort("kein") is None
    assert b6.parse_masse("Mach ein Fenster") == []   # unbestimmter Artikel ist keine Zahl


@pytest.fixture(scope="module")
def state():
    return b6.lade_state()


def test_raumreferenz(state):
    r = b6.loese_raum("das Bad oben", state)
    assert r.status == "eindeutig" and r.raum_id == "og_bad"
    assert r.guid == next(x["guid"] for x in state["raeume"] if x["id"] == "og_bad")
    assert b6.loese_raum("das Bad unten", state).raum_id == "eg_dusche"
    assert b6.loese_raum("das Bad", state).status == "mehrdeutig"
    assert b6.loese_raum("das zweite Kinderzimmer", state).raum_id == "og_kind2"
    assert b6.loese_raum("die Sauna", state).status == "keine"


def test_intent_angenommen_mit_ausgleich(state):
    prot, neu = b6.verarbeite("Mach das Bad oben zwei Meter sechzig breit", state)
    assert prot["status"] == "angenommen" and prot["intent_quelle"] == "STUB"
    breiten = {r["id"]: r["breite"] for r in neu["raeume"]}
    assert breiten["og_bad"] == 2.60 and breiten["og_kind1"] == 3.30
    zeile = neu["zeilen"]["OG-Nord"]
    assert sum(breiten[i] for i in zeile) == pytest.approx(9.40)   # Außenmaß unverändert
    assert state["raeume"][5]["breite"] == 2.40                    # Eingangszustand unverändert


def test_intent_abgelehnt_mit_begruendung(state):
    prot, neu = b6.verarbeite("Das Bad oben bitte eins zwanzig breit", state)
    assert prot["status"] == "abgelehnt" and neu is None
    assert "Mindestbreite 1.70" in prot["begruendung"]


def test_intent_flaeche_und_rueckfragen(state):
    prot, neu = b6.verarbeite("Das zweite Kinderzimmer soll zwölf Quadratmeter haben", state)
    assert prot["status"] == "angenommen"
    k2 = next(r for r in neu["raeume"] if r["id"] == "og_kind2")
    assert k2["breite"] == 3.55 and k2["breite"] * k2["tiefe"] >= 12.0
    assert b6.verarbeite("Das Bad soll zwanzig Zentimeter breiter werden", state)[0]["status"] == "rueckfrage"
    assert b6.verarbeite("Das Bad oben eins fünf breiter", state)[0]["status"] == "rueckfrage"
    assert b6.verarbeite("Stell die Dachneigung auf 35 Grad", state)[0]["status"] == "nicht_umgesetzt"
    assert b6.verarbeite("Kannst du das mal anders machen", state)[0]["status"] == "rueckfrage"


def test_pipeline_deterministisch(state):
    a = [b6.verarbeite_einfach(s, state) for s in b6.BEISPIELE]
    b = [b6.verarbeite_einfach(s, copy.deepcopy(state)) for s in b6.BEISPIELE]
    assert a == b


# --- B7 (optional) ---------------------------------------------------------------

def test_btlx_export(tmp_path):
    pytest.importorskip("compas_timber")
    import b1_wandelement as b1
    import b7_btlx_export as b7
    p = b1.lade_parameter()
    a = b7.exportiere(p, tmp_path / "1" / "wand.btlx")   # gleicher Dateiname: er steht im Header
    b = b7.exportiere(p, tmp_path / "2" / "wand.btlx")
    assert hashlib.sha256(a.read_bytes()).digest() == hashlib.sha256(b.read_bytes()).digest()
    text = a.read_text(encoding="utf-8")
    assert text.count("<Part ") == 18 and text.count("<Lap ") == 1
    assert 'Material="KVH C24"' in text and 'Date="2026-01-01"' in text

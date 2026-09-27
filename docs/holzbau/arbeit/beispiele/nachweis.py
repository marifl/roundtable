#!/usr/bin/env python3
"""
nachweis.py – Einheitliches Nachweis-Framework für den regelbasierten
Holzrahmenbau-Hausplaner (rechnerischer UND grafischer Nachweis).

Grundsatz: Jede Regelprüfung und jede Berechnung wird als *Nachweis*
dokumentiert, den ein Prüfingenieur, eine Behörde oder ein Gutachter ohne
Zugriff auf den Code nachvollziehen kann:

  * Regel mit Quelle, Fassung/Ausgabe, Regelwerk-Profil und Version,
  * Gegenstand mit IFC-GlobalId (Rückverfolgbarkeit ins Modell),
  * Eingangsgrößen mit Einheit, Quelle und Art (Eingabe, Annahme, Konstante,
    Grenzwert), optional mit Standardunsicherheit,
  * Rechenschritte mit Formel (LaTeX), ausführbarem Ausdruck, eingesetzten
    Zahlenwerten und Normverweis,
  * Kriterien (Ist ≤/≥ Grenzwert), Ausnutzung η, Status mit Ampel,
  * Unsicherheit nach GUM (JCGM 100:2008, lineare Fortpflanzung, U = k·u_c)
    und optional Monte-Carlo nach JCGM 101:2008,
  * Grafiken (SVG, maßstäblich), Hash über den kanonischen Inhalt.

Rechnen ungerundet, Anzeige gerundet mit Angabe der Rundungsregel
(ISO 80000-1:2022 Anhang B, DIN 1333:1992-02). Einheiten werden bei jedem
Rechenschritt dimensionsgeprüft: mit `pint`, falls installiert, sonst mit
einer eigenen minimalistischen Dimensionsprüfung (`EinheitenEinfach`).

Ausgabe: JSON (Schema `nachweis.schema.json`), Markdown, HTML (MathJax,
eingebettete SVG). PDF wird bewusst nicht erzeugt (siehe NACHWEIS.md).

Das Modul ist deterministisch: gleiche Eingabe und gleiche Paketversionen
ergeben byte-identische JSON-, Markdown-, HTML- und SVG-Dateien. Ein
Zeitstempel wird nur gesetzt, wenn er ausdrücklich übergeben wird oder
SOURCE_DATE_EPOCH gesetzt ist; er geht nicht in den Hash ein.
"""
from __future__ import annotations

import ast
import hashlib
import html as _html
import io
import json
import math
import os
import platform
import re
from dataclasses import dataclass, field
from datetime import datetime, timezone
from decimal import ROUND_CEILING, ROUND_FLOOR, ROUND_HALF_EVEN, ROUND_HALF_UP, Decimal
from fractions import Fraction
from pathlib import Path
from typing import Any, Callable, Iterable, Sequence

import numpy as np

__version__ = "1.0.0"
SCHEMA_VERSION = "1.0"
HIER = Path(__file__).resolve().parent
SCHEMA_DATEI = HIER / "nachweis.schema.json"


class NachweisFehler(Exception):
    """Allgemeiner Fehler im Nachweis (fehlendes Symbol, unzulässiger Ausdruck …)."""


class EinheitenFehler(NachweisFehler):
    """Dimensionen passen nicht zusammen (z. B. m + m² oder Ergebnis in falscher Einheit)."""


# ===========================================================================
# 1. Einheiten
# ===========================================================================

_HOCH = {"⁰": "0", "¹": "1", "²": "2", "³": "3", "⁴": "4", "⁵": "5", "⁶": "6", "⁷": "7", "⁸": "8", "⁹": "9", "⁻": "-"}


def normiere_einheit(einheit: str | None) -> str:
    """Anzeige-Notation → maschinenlesbare Notation (pint-kompatibel).

    „W/(m²·K)“ → „W/(m**2*K)“, „%“ → „percent“, „°“ → „degree“,
    „1“, „–“, „Stk“ und leer → „dimensionless“."""
    s = (einheit or "").strip()
    if s in ("", "1", "-", "–", "Stk", "Stk.", "dimensionless"):
        return "dimensionless"
    s = s.replace("·", "*").replace("⋅", "*").replace(" ", "*")
    s = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)", lambda m: "**" + "".join(_HOCH[c] for c in m.group(1)), s)
    s = s.replace("%", "percent").replace("°", "degree").replace("Stk", "dimensionless")
    return s


def einheit_latex(einheit: str | None) -> str:
    """„W/(m²·K)“ → „\\mathrm{W/(m^{2}\\cdot K)}“ (leer bei dimensionslos)."""
    s = (einheit or "").strip()
    if s in ("", "1", "-", "–", "dimensionless"):
        return ""
    s = re.sub(r"([⁰¹²³⁴⁵⁶⁷⁸⁹⁻]+)", lambda m: "^{" + "".join(_HOCH[c] for c in m.group(1)) + "}", s)
    s = s.replace("·", r"\cdot ").replace("%", r"\%").replace("°", r"^{\circ}")
    return r"\mathrm{" + s + "}"


# --- 1a. Eigene minimalistische Dimensionsprüfung (ohne pint) ---------------

_DIMS = ("L", "M", "T", "Θ", "I", "N", "J")


def _dim(**exp) -> tuple:
    return tuple(Fraction(exp.get(d, 0)) for d in _DIMS)


_D0 = _dim()
_EINFACH_TABELLE: dict[str, tuple[float, tuple]] = {
    "dimensionless": (1.0, _D0), "percent": (0.01, _D0), "rad": (1.0, _D0), "radian": (1.0, _D0),
    "degree": (math.pi / 180.0, _D0),
    "m": (1.0, _dim(L=1)), "mm": (1e-3, _dim(L=1)), "cm": (1e-2, _dim(L=1)), "dm": (0.1, _dim(L=1)), "km": (1e3, _dim(L=1)),
    "g": (1e-3, _dim(M=1)), "kg": (1.0, _dim(M=1)), "t": (1e3, _dim(M=1)),
    "s": (1.0, _dim(T=1)), "min": (60.0, _dim(T=1)), "h": (3600.0, _dim(T=1)),
    "K": (1.0, _dim(Θ=1)),
    "N": (1.0, _dim(L=1, M=1, T=-2)), "kN": (1e3, _dim(L=1, M=1, T=-2)),
    "Pa": (1.0, _dim(L=-1, M=1, T=-2)), "kPa": (1e3, _dim(L=-1, M=1, T=-2)), "MPa": (1e6, _dim(L=-1, M=1, T=-2)),
    "J": (1.0, _dim(L=2, M=1, T=-2)), "kJ": (1e3, _dim(L=2, M=1, T=-2)), "kWh": (3.6e6, _dim(L=2, M=1, T=-2)),
    "W": (1.0, _dim(L=2, M=1, T=-3)), "kW": (1e3, _dim(L=2, M=1, T=-3)),
}


def _parse_einfach(norm: str) -> tuple[float, tuple]:
    """Rekursiver Abstieg über * / ** ( ) für die normierte Einheitennotation."""
    tok = re.findall(r"\*\*|[A-Za-zΩµ_]+|\d+(?:\.\d+)?|[*/()\-]", norm)
    pos = 0

    def peek():
        return tok[pos] if pos < len(tok) else None

    def nimm():
        nonlocal pos
        pos += 1
        return tok[pos - 1]

    def atom():
        t = nimm()
        if t == "(":
            v = ausdruck()
            if nimm() != ")":
                raise EinheitenFehler(f"Klammer fehlt in Einheit '{norm}'")
        elif t in _EINFACH_TABELLE:
            v = _EINFACH_TABELLE[t]
        elif t is not None and re.fullmatch(r"\d+(?:\.\d+)?", t):
            v = (float(t), _D0)
        else:
            raise EinheitenFehler(f"Unbekannte Einheit '{t}' in '{norm}'")
        if peek() == "**":
            nimm()
            neg = False
            if peek() == "-":
                nimm()
                neg = True
            e = Fraction(nimm()) * (-1 if neg else 1)
            v = (v[0] ** float(e), tuple(x * e for x in v[1]))
        return v

    def ausdruck():
        v = atom()
        while peek() in ("*", "/"):
            op = nimm()
            w = atom()
            v = (v[0] * w[0], tuple(a + b for a, b in zip(v[1], w[1]))) if op == "*" else \
                (v[0] / w[0], tuple(a - b for a, b in zip(v[1], w[1])))
        return v

    erg = ausdruck()
    if pos != len(tok):
        raise EinheitenFehler(f"Einheit nicht lesbar: '{norm}'")
    return erg


def _dim_text(d: tuple) -> str:
    t = [f"{n}^{e}" if e != 1 else n for n, e in zip(_DIMS, d) if e != 0]
    return "·".join(t) or "1"


class DimWert:
    """Zahlenwert in SI-Basiseinheiten mit Dimensionsvektor (eigene Einheitenprüfung)."""
    __slots__ = ("si", "dim")

    def __init__(self, si, dim):
        self.si, self.dim = si, dim

    def _pruef(self, o, op):
        o = o if isinstance(o, DimWert) else DimWert(o, _D0)
        if o.dim != self.dim:
            raise EinheitenFehler(f"Operation '{op}' mit unverträglichen Dimensionen {_dim_text(self.dim)} und {_dim_text(o.dim)}")
        return o

    def __add__(self, o):
        o = self._pruef(o, "+"); return DimWert(self.si + o.si, self.dim)

    __radd__ = __add__

    def __sub__(self, o):
        o = self._pruef(o, "−"); return DimWert(self.si - o.si, self.dim)

    def __rsub__(self, o):
        o = self._pruef(o, "−"); return DimWert(o.si - self.si, self.dim)

    def __mul__(self, o):
        o = o if isinstance(o, DimWert) else DimWert(o, _D0)
        return DimWert(self.si * o.si, tuple(a + b for a, b in zip(self.dim, o.dim)))

    __rmul__ = __mul__

    def __truediv__(self, o):
        o = o if isinstance(o, DimWert) else DimWert(o, _D0)
        return DimWert(self.si / o.si, tuple(a - b for a, b in zip(self.dim, o.dim)))

    def __rtruediv__(self, o):
        return DimWert(o, _D0) / self

    def __pow__(self, e):
        if isinstance(e, DimWert):
            if e.dim != _D0:
                raise EinheitenFehler("Exponent muss dimensionslos sein")
            e = e.si
        fe = Fraction(e).limit_denominator(12)
        return DimWert(self.si ** e, tuple(x * fe for x in self.dim))

    def __neg__(self):
        return DimWert(-self.si, self.dim)

    def __pos__(self):
        return self

    def __abs__(self):
        return DimWert(abs(self.si), self.dim)

    def __lt__(self, o):
        return self.si < self._pruef(o, "<").si

    def __le__(self, o):
        return self.si <= self._pruef(o, "≤").si

    def __gt__(self, o):
        return self.si > self._pruef(o, ">").si

    def __ge__(self, o):
        return self.si >= self._pruef(o, "≥").si

    def __repr__(self):
        return f"DimWert({self.si!r}, {_dim_text(self.dim)})"


class EinheitenEinfach:
    """Eigene Dimensionsprüfung ohne Fremdpaket (Fallback, wenn pint fehlt)."""
    name = "einfach"

    def si(self, einheit: str) -> tuple[float, tuple]:
        return _parse_einfach(normiere_einheit(einheit))

    def groesse(self, wert: float, einheit: str) -> DimWert:
        f, d = self.si(einheit)
        return DimWert(wert * f, d)

    def in_einheit(self, q, einheit: str) -> float:
        f, d = self.si(einheit)
        q = q if isinstance(q, DimWert) else DimWert(q, _D0)
        if q.dim != d:
            raise EinheitenFehler(f"Ergebnis hat Dimension {_dim_text(q.dim)}, erwartet {_dim_text(d)} ({einheit})")
        return q.si / f

    def dimension(self, einheit: str) -> str:
        return _dim_text(self.si(einheit)[1])

    def si_faktor(self, einheit: str) -> float:
        return self.si(einheit)[0]

    def dimensionslos(self, q) -> float:
        if isinstance(q, DimWert):
            if q.dim != _D0:
                raise EinheitenFehler(f"Argument muss dimensionslos sein, hat {_dim_text(q.dim)}")
            return q.si
        return q

    # Funktionen für den Auswerter
    def funktionen(self) -> dict[str, Callable]:
        dl = self.dimensionslos

        def _minmax(f):
            def g(*a):
                if len(a) < 2:
                    raise NachweisFehler("min/max brauchen mindestens zwei Argumente")
                r = a[0]
                for x in a[1:]:
                    r = x if f(x, r) else r
                return r
            return g

        return {
            "min": _minmax(lambda x, r: x < r), "max": _minmax(lambda x, r: x > r),
            "abs": abs, "sqrt": lambda x: x ** 0.5,
            "tan": lambda x: math.tan(dl(x)), "sin": lambda x: math.sin(dl(x)), "cos": lambda x: math.cos(dl(x)),
            "atan": lambda x: DimWert(math.atan(dl(x)), _D0),
            "ceil": lambda x: math.ceil(dl(x)), "floor": lambda x: math.floor(dl(x)),
        }


# --- 1b. pint als Standard, falls installiert --------------------------------

class EinheitenPint:
    """Einheitenprüfung mit pint (https://pint.readthedocs.io)."""
    name = "pint"

    def __init__(self):
        import pint
        self.pint = pint
        self.ureg = pint.UnitRegistry(autoconvert_offset_to_baseunit=True)
        self._cache: dict[str, Any] = {}

    def einheit(self, einheit: str):
        n = normiere_einheit(einheit)
        if n not in self._cache:
            try:
                self._cache[n] = self.ureg.parse_units(n)
            except Exception as e:  # noqa: BLE001 – pint wirft verschiedene Typen
                raise EinheitenFehler(f"Unbekannte Einheit '{einheit}': {e}") from e
        return self._cache[n]

    def groesse(self, wert, einheit: str):
        return self.ureg.Quantity(wert, self.einheit(einheit))

    def in_einheit(self, q, einheit: str) -> float:
        ziel = self.einheit(einheit)
        if not isinstance(q, self.ureg.Quantity):
            q = self.ureg.Quantity(q, "dimensionless")
        try:
            return float(q.to(ziel).magnitude)
        except self.pint.DimensionalityError as e:
            raise EinheitenFehler(f"Ergebnis hat Dimension {q.dimensionality}, erwartet {ziel.dimensionality} ({einheit})") from e

    def dimension(self, einheit: str) -> str:
        return str(self.groesse(1.0, einheit).dimensionality)

    def si_faktor(self, einheit: str) -> float:
        return float(self.groesse(1.0, einheit).to_base_units().magnitude)

    def dimensionslos(self, q) -> float:
        if isinstance(q, self.ureg.Quantity):
            try:
                return float(q.to("radian").magnitude) if q.dimensionless else float(q.to("dimensionless").magnitude)
            except self.pint.DimensionalityError as e:
                raise EinheitenFehler(f"Argument muss dimensionslos sein, hat {q.dimensionality}") from e
        return q

    def funktionen(self) -> dict[str, Callable]:
        dl = self.dimensionslos

        def _minmax(f):
            def g(*a):
                if len(a) < 2:
                    raise NachweisFehler("min/max brauchen mindestens zwei Argumente")
                r = a[0]
                for x in a[1:]:
                    r = x if f(x, r) else r
                return r
            return g

        return {
            "min": _minmax(lambda x, r: x < r), "max": _minmax(lambda x, r: x > r),
            "abs": abs, "sqrt": lambda x: x ** 0.5,
            "tan": lambda x: math.tan(dl(x)), "sin": lambda x: math.sin(dl(x)), "cos": lambda x: math.cos(dl(x)),
            "atan": lambda x: math.atan(dl(x)),
            "ceil": lambda x: math.ceil(dl(x)), "floor": lambda x: math.floor(dl(x)),
        }


def _waehle_backend(name: str | None = None):
    name = name or os.environ.get("NACHWEIS_EINHEITEN", "auto")
    if name in ("auto", "pint"):
        try:
            return EinheitenPint()
        except ImportError:
            if name == "pint":
                raise
    return EinheitenEinfach()


EINHEITEN = _waehle_backend()


def setze_einheiten_backend(name: str) -> None:
    """'pint' oder 'einfach' (für Tests und Umgebungen ohne pint)."""
    global EINHEITEN
    EINHEITEN = EinheitenPint() if name == "pint" else EinheitenEinfach()


# ===========================================================================
# 2. Rundung und Zahlendarstellung
# ===========================================================================

_VERFAHREN = {
    "halb_auf": (ROUND_HALF_UP, "Regel B (bei 5 betragsmäßig aufrunden) nach ISO 80000-1:2022 Anh. B.3; entspricht DIN 1333:1992-02"),
    "halb_gerade": (ROUND_HALF_EVEN, "Regel A (bei 5 zur geraden Ziffer) nach ISO 80000-1:2022 Anh. B.3"),
    "auf": (ROUND_CEILING, "Aufrunden (Richtung +∞), sicherheitsgerichtet nach ISO 80000-1:2022 Anh. B.5"),
    "ab": (ROUND_FLOOR, "Abrunden (Richtung −∞), sicherheitsgerichtet nach ISO 80000-1:2022 Anh. B.5"),
}


@dataclass(frozen=True)
class Rundung:
    """Rundungsregel für die ANZEIGE. Gerechnet wird immer ungerundet.

    art:       "signifikant" (Anzahl wertanzeigender Ziffern) oder "dezimalstellen"
    stellen:   Anzahl
    verfahren: halb_auf | halb_gerade | auf | ab
    quelle:    fachliche Begründung, z. B. „DIN EN ISO 6946:2018-03, 6.5.2“
    Die Rundung erfolgt in einem Schritt (ISO 80000-1 Anh. B.4)."""
    art: str = "signifikant"
    stellen: int = 3
    verfahren: str = "halb_auf"
    quelle: str = ""

    def __post_init__(self):
        if self.art not in ("signifikant", "dezimalstellen"):
            raise ValueError(f"Rundungsart {self.art!r}")
        if self.verfahren not in _VERFAHREN:
            raise ValueError(f"Rundungsverfahren {self.verfahren!r}")
        if self.art == "signifikant" and self.stellen < 1:
            raise ValueError("mindestens eine signifikante Stelle")

    def runde(self, x: float | int | Decimal) -> Decimal:
        d = x if isinstance(x, Decimal) else Decimal(repr(float(x))) if not isinstance(x, int) else Decimal(x)
        modus = _VERFAHREN[self.verfahren][0]
        if self.art == "dezimalstellen":
            return d.quantize(Decimal(1).scaleb(-self.stellen), rounding=modus)
        if d == 0:
            return Decimal(0).quantize(Decimal(1).scaleb(-(self.stellen - 1)))
        exp = d.adjusted() - (self.stellen - 1)
        r = d.quantize(Decimal(1).scaleb(exp), rounding=modus)
        if r != 0 and r.adjusted() > d.adjusted():  # 9,96 → 10,0: eine Stelle zu viel
            r = r.quantize(Decimal(1).scaleb(exp + 1), rounding=modus)
        return r

    def text(self) -> str:
        was = f"{self.stellen} signifikante Stelle{'n' if self.stellen != 1 else ''}" if self.art == "signifikant" \
            else f"{self.stellen} Dezimalstelle{'n' if self.stellen != 1 else ''}"
        t = f"{was}, {_VERFAHREN[self.verfahren][1]}"
        return f"{t}; Begründung: {self.quelle}" if self.quelle else t

    def als_dict(self) -> dict:
        return {"art": self.art, "stellen": self.stellen, "verfahren": self.verfahren, "quelle": self.quelle, "text": self.text()}


ZWISCHENWERT = Rundung("signifikant", 5, "halb_auf", "Anzeige von Zwischenwerten; gerechnet wird ungerundet "
                       "(vgl. DIN EN ISO 6946:2018-03, 6.7.1.1: mindestens drei Dezimalstellen)")
AUSNUTZUNG = Rundung("dezimalstellen", 3, "auf", "Ausnutzung sicherheitsgerichtet aufgerundet")


def zahl_de(d: Decimal | float | int, gruppieren: bool = True) -> str:
    """Dezimalzahl mit Komma; ganzzahliger Teil ab fünf Stellen in Dreiergruppen
    mit schmalem Leerzeichen (ISO 80000-1:2022, 7.3.1; DIN 1333)."""
    if isinstance(d, bool):
        return "ja" if d else "nein"
    if isinstance(d, float):
        if math.isnan(d) or math.isinf(d):
            return str(d)
        d = Decimal(repr(d))
    elif isinstance(d, int):
        d = Decimal(d)
    s = format(d, "f")
    neg = s.startswith("-")
    s = s.lstrip("-")
    ganz, _, bruch = s.partition(".")
    if gruppieren and len(ganz) >= 5:
        ganz = " ".join(ganz[max(0, i - 3):i] for i in range(len(ganz), 0, -3)[::-1])
    return ("−" if neg else "") + ganz + ("," + bruch if bruch else "")


def zahl_roh(x: float | int) -> str:
    """Wert ohne Rundung (kürzeste exakte Darstellung der Gleitkommazahl)."""
    if isinstance(x, bool):
        return "ja" if x else "nein"
    if isinstance(x, int):
        return zahl_de(x)
    d = Decimal(repr(float(x)))
    if d == d.to_integral_value() and abs(d) < Decimal(10) ** 15:
        d = d.quantize(Decimal(1))
    return zahl_de(d)


def rundung_aus_unsicherheit(U: float) -> Rundung:
    """Rundestelle aus der Unsicherheit nach DIN 1333:1992-02, Abschn. 6.1:
    Ist die erste von null verschiedene Ziffer von U eine 3 … 9, ist sie die
    Rundestelle, bei 1 oder 2 die Stelle rechts daneben (→ höchstens zwei
    signifikante Stellen der Unsicherheit, vgl. JCGM 100:2008, 7.2.6).
    Negative Dezimalstellen bedeuten Rundung auf Zehner, Hunderter …"""
    if not U or U <= 0 or math.isnan(U):
        raise ValueError("Unsicherheit muss positiv sein")
    d = Decimal(repr(float(U)))
    e = d.adjusted()
    erste = int(format(d.scaleb(-e), "f")[0])
    p = e - 1 if erste in (1, 2) else e
    return Rundung("dezimalstellen", -p, "halb_auf", "Rundestelle aus der Unsicherheit nach DIN 1333:1992-02, 6.1")


def runde_mit_unsicherheit(y: float, U: float) -> tuple[str, str]:
    """y und U an derselben Stelle runden; U stets aufrunden (DIN 1333, 6.1)."""
    r = rundung_aus_unsicherheit(U)
    ry = r.runde(y)
    rU = Rundung(r.art, r.stellen, "auf").runde(U)
    return zahl_de(ry), zahl_de(rU)


# ===========================================================================
# 3. Datenklassen
# ===========================================================================

_GRIECH = {"alpha": r"\alpha", "beta": r"\beta", "gamma": r"\gamma", "delta": r"\delta", "Delta": r"\Delta",
           "eta": r"\eta", "lambda": r"\lambda", "rho": r"\rho", "mu": r"\mu", "sigma": r"\sigma", "phi": r"\varphi",
           "theta": r"\vartheta", "psi": r"\psi", "chi": r"\chi", "tau": r"\tau", "pi": r"\pi", "epsilon": r"\varepsilon"}

ARTEN = ("eingabe", "annahme", "konstante", "grenzwert", "zwischenergebnis", "ergebnis")


def symbol_latex(symbol: str) -> str:
    """„R_si“ → „R_{\\mathrm{si}}“, „lambda_D“ → „\\lambda_{\\mathrm{D}}“."""
    basis, _, index = symbol.partition("_")
    b = _GRIECH.get(basis, basis if len(basis) == 1 else r"\mathrm{" + basis + "}")
    if not index:
        return b
    teile = [(_GRIECH.get(t, r"\mathrm{" + t + "}")) for t in index.split("_")]
    return f"{b}_{{{','.join(teile)}}}"


@dataclass
class Groesse:
    """Physikalische Größe (DIN 1313: Größenwert = Zahlenwert · Einheit).

    `symbol` ist ein Python-Bezeichner und dient als Variable in Ausdrücken.
    `unsicherheit` ist die Standardunsicherheit u (k = 1) in derselben Einheit.
    `art` kennzeichnet die Herkunft: eingabe | annahme | konstante | grenzwert |
    zwischenergebnis | ergebnis. Annahmen werden im Bericht hervorgehoben."""
    name: str
    symbol: str
    wert: float | int | bool | str | None = None
    einheit: str = "1"
    quelle: str = ""
    unsicherheit: float | None = None
    art: str = "eingabe"
    latex: str | None = None
    rundung: Rundung | None = None
    verteilung: str = "normal"   # normal | rechteck (für Monte-Carlo; u ist immer die Standardunsicherheit)
    bezug: str | None = None     # z. B. IFC-GUID oder „Pset_WallCommon.ThermalTransmittance“

    def __post_init__(self):
        if not self.symbol.isidentifier():
            raise NachweisFehler(f"Symbol {self.symbol!r} ist kein gültiger Bezeichner")
        if self.art not in ARTEN:
            raise NachweisFehler(f"Art {self.art!r} unbekannt")
        if self.verteilung not in ("normal", "rechteck"):
            raise NachweisFehler(f"Verteilung {self.verteilung!r} unbekannt")

    @property
    def numerisch(self) -> bool:
        return isinstance(self.wert, (int, float)) and not isinstance(self.wert, bool)

    @property
    def tex(self) -> str:
        return self.latex or symbol_latex(self.symbol)

    def anzeige(self, rundung: Rundung | None = None) -> str:
        r = rundung or self.rundung
        if self.wert is None:
            return "–"
        if not self.numerisch:
            return zahl_roh(self.wert) if isinstance(self.wert, bool) else str(self.wert)
        z = zahl_de(r.runde(self.wert)) if r else zahl_roh(self.wert)
        e = self.einheit if self.einheit not in ("1", "", "-", "–") else ""
        return f"{z} {e}".strip()

    def als_dict(self) -> dict:
        d = {"name": self.name, "symbol": self.symbol, "latex": self.tex, "wert": self.wert, "einheit": self.einheit,
             "quelle": self.quelle, "art": self.art, "unsicherheit": self.unsicherheit, "verteilung": self.verteilung,
             "bezug": self.bezug, "anzeige": self.anzeige(),
             "rundung": self.rundung.als_dict() if self.rundung else None}
        if self.numerisch:
            try:
                d["dimension"] = EINHEITEN.dimension(self.einheit)
            except EinheitenFehler:
                d["dimension"] = None
        return d


@dataclass
class Schritt:
    """Ein Rechenschritt. Mit `ausdruck` wird das Ergebnis vom Framework
    berechnet und dimensionsgeprüft; ohne `ausdruck` beschreibt `verfahren`
    einen algorithmischen Schritt (z. B. Polygonverschneidung), dessen
    Ergebnis vom Rechenkern übernommen und als solches gekennzeichnet wird."""
    beschreibung: str
    ergebnis: Groesse
    ausdruck: str | None = None
    formel_latex: str | None = None
    eingaben: list[str] = field(default_factory=list)
    norm_verweis: str = ""
    verfahren: str | None = None
    einsetzen_latex: str | None = None   # wird von rechne() gefüllt

    def __post_init__(self):
        if self.ausdruck is None and self.verfahren is None:
            raise NachweisFehler(f"Schritt '{self.beschreibung}': Ausdruck oder Verfahren angeben")
        if self.ergebnis.art in ("eingabe", "annahme", "konstante", "grenzwert"):
            self.ergebnis.art = "zwischenergebnis"


@dataclass
class Regel:
    """Die angewandte Regel mit Fundstelle und Versionsangaben."""
    text: str
    quelle: str
    fassung: str
    profil: str
    profil_version: str
    fundstelle: str = ""
    verifikation: str = "[U]"   # [V] am Primärtext geprüft, [U] nicht geprüft

    def als_dict(self) -> dict:
        return {"text": self.text, "quelle": self.quelle, "fassung": self.fassung, "fundstelle": self.fundstelle,
                "verifikation": self.verifikation,
                "regelwerk_profil": {"name": self.profil, "version": self.profil_version}}


@dataclass
class Gegenstand:
    """Nachweisgegenstand; `ifc_guid` verweist auf IfcRoot.GlobalId im Modell."""
    bezeichnung: str
    ifc_guid: str | None = None
    ifc_klasse: str | None = None
    ifc_datei: str | None = None
    ifc_sha256: str | None = None
    weitere_guids: list[str] = field(default_factory=list)

    def als_dict(self) -> dict:
        return {"bezeichnung": self.bezeichnung, "ifc_guid": self.ifc_guid, "ifc_klasse": self.ifc_klasse,
                "ifc_datei": self.ifc_datei, "ifc_sha256": self.ifc_sha256, "weitere_guids": list(self.weitere_guids)}


@dataclass
class Kriterium:
    """Vergleich Ist ⟂ Grenzwert. `ist` und `grenzwert` sind Symbole des Nachweises."""
    bezeichnung: str
    ist: str
    vergleich: str
    grenzwert: str
    norm_verweis: str = ""
    toleranz: float = 0.0          # numerische Toleranz in der Einheit des Grenzwerts
    # von rechne() gefüllt
    ist_wert: float | None = None
    grenz_wert: float | None = None
    einheit: str = "1"
    ausnutzung: float | None = None
    erfuellt: bool | None = None
    rundungsempfindlich: bool = False
    innerhalb_unsicherheit: bool | None = None

    def __post_init__(self):
        if self.vergleich not in ("≤", "≥", "<", ">", "="):
            raise NachweisFehler(f"Vergleich {self.vergleich!r} unbekannt")

    def als_dict(self) -> dict:
        return {k: getattr(self, k) for k in ("bezeichnung", "ist", "vergleich", "grenzwert", "norm_verweis", "toleranz",
                                              "ist_wert", "grenz_wert", "einheit", "ausnutzung", "erfuellt",
                                              "rundungsempfindlich", "innerhalb_unsicherheit")}


@dataclass
class Grafik:
    """Grafischer Nachweis als SVG-Text (deterministisch erzeugt)."""
    id: str
    titel: str
    svg: str
    art: str = "diagramm"          # diagramm | lageplan | schnitt | ansicht | grundriss
    beschreibung: str = ""
    massstab: str | None = None

    def __post_init__(self):
        if not re.fullmatch(r"[A-Za-z0-9_\-]+", self.id):
            raise NachweisFehler(f"Grafik-ID {self.id!r}: nur Buchstaben, Ziffern, _ und -")

    @property
    def sha256(self) -> str:
        return hashlib.sha256(self.svg.encode("utf-8")).hexdigest()

    def als_dict(self) -> dict:
        return {"id": self.id, "titel": self.titel, "art": self.art, "beschreibung": self.beschreibung,
                "massstab": self.massstab, "sha256": self.sha256, "svg": self.svg}


# ===========================================================================
# 4. Sicherer Auswerter für Ausdrücke (AST, kein eval)
# ===========================================================================

_FUNKTIONEN = ("min", "max", "abs", "sqrt", "tan", "sin", "cos", "atan", "ceil", "floor")
_KONSTANTEN = {"pi": math.pi}


def _pruefe_ast(knoten: ast.AST, ausdruck: str) -> None:
    erlaubt = (ast.Expression, ast.BinOp, ast.UnaryOp, ast.Constant, ast.Name, ast.Call, ast.Load,
               ast.Add, ast.Sub, ast.Mult, ast.Div, ast.Pow, ast.USub, ast.UAdd)
    for k in ast.walk(knoten):
        if not isinstance(k, erlaubt):
            raise NachweisFehler(f"Unzulässiges Element {type(k).__name__} in Ausdruck '{ausdruck}'")
        if isinstance(k, ast.Constant) and not (isinstance(k.value, (int, float)) and not isinstance(k.value, bool)):
            raise NachweisFehler(f"Nur Zahlen als Konstanten erlaubt: '{ausdruck}'")
        if isinstance(k, ast.Call):
            if not isinstance(k.func, ast.Name) or k.func.id not in _FUNKTIONEN or k.keywords:
                raise NachweisFehler(f"Unzulässiger Funktionsaufruf in '{ausdruck}' (erlaubt: {', '.join(_FUNKTIONEN)})")


def parse_ausdruck(ausdruck: str) -> ast.Expression:
    try:
        baum = ast.parse(ausdruck, mode="eval")
    except SyntaxError as e:
        raise NachweisFehler(f"Syntaxfehler in '{ausdruck}': {e.msg}") from e
    _pruefe_ast(baum, ausdruck)
    return baum


def namen_in(ausdruck: str) -> list[str]:
    """Verwendete Symbole in Reihenfolge des ersten Auftretens (ohne Funktionen/Konstanten)."""
    baum = parse_ausdruck(ausdruck)
    fn = {k.func.id for k in ast.walk(baum) if isinstance(k, ast.Call)}
    gesehen: list[str] = []
    for k in ast.walk(baum):
        if isinstance(k, ast.Name) and k.id not in fn and k.id not in _KONSTANTEN and k.id not in gesehen:
            gesehen.append(k.id)
    return gesehen


def werte_aus(baum: ast.Expression, namen: dict[str, Any], funktionen: dict[str, Callable]):
    def ev(k):
        if isinstance(k, ast.Expression):
            return ev(k.body)
        if isinstance(k, ast.Constant):
            return k.value
        if isinstance(k, ast.Name):
            if k.id in namen:
                return namen[k.id]
            if k.id in _KONSTANTEN:
                return _KONSTANTEN[k.id]
            raise NachweisFehler(f"Symbol '{k.id}' ist nicht definiert")
        if isinstance(k, ast.UnaryOp):
            v = ev(k.operand)
            return -v if isinstance(k.op, ast.USub) else +v
        if isinstance(k, ast.BinOp):
            a, b = ev(k.left), ev(k.right)
            op = type(k.op)
            if op is ast.Add:
                return a + b
            if op is ast.Sub:
                return a - b
            if op is ast.Mult:
                return a * b
            if op is ast.Div:
                return a / b
            if op is ast.Pow:
                return a ** b
        if isinstance(k, ast.Call):
            return funktionen[k.func.id](*[ev(a) for a in k.args])
        raise NachweisFehler(f"Unzulässiger Knoten {type(k).__name__}")

    return ev(baum)


def _np_funktionen() -> dict[str, Callable]:
    """Vektorisierte Funktionen für das Rechnen in SI-Zahlenwerten (Monte-Carlo, Ableitungen)."""
    def _red(f):
        def g(*a):
            r = a[0]
            for x in a[1:]:
                r = f(r, x)
            return r
        return g
    return {"min": _red(np.minimum), "max": _red(np.maximum), "abs": np.abs, "sqrt": np.sqrt, "tan": np.tan,
            "sin": np.sin, "cos": np.cos, "atan": np.arctan, "ceil": np.ceil, "floor": np.floor}


# --- LaTeX aus dem AST --------------------------------------------------------

_PREC = {ast.Add: 1, ast.Sub: 1, ast.Mult: 2, ast.Div: 2, ast.Pow: 4}


def zahl_latex(x: float | int | Decimal) -> str:
    s = zahl_de(x) if isinstance(x, Decimal) else zahl_roh(x)
    return s.replace(",", "{,}").replace("−", "-").replace(" ", r"\,")


def ausdruck_latex(ausdruck: str, sym: Callable[[str], str]) -> str:
    """Python-Ausdruck → LaTeX. `sym(name)` liefert die Darstellung eines Namens."""
    baum = parse_ausdruck(ausdruck)

    def prec(k):
        if isinstance(k, ast.BinOp):
            return 2.5 if isinstance(k.op, ast.Div) else _PREC[type(k.op)]
        if isinstance(k, ast.UnaryOp):
            return 3
        return 5

    def lx(k, eltern_prec=0, rechts=False):
        if isinstance(k, ast.Expression):
            return lx(k.body)
        if isinstance(k, ast.Constant):
            s = zahl_latex(k.value)
        elif isinstance(k, ast.Name):
            s = r"\pi" if k.id == "pi" and k.id in _KONSTANTEN else sym(k.id)
        elif isinstance(k, ast.UnaryOp):
            s = ("-" if isinstance(k.op, ast.USub) else "+") + lx(k.operand, 3)
        elif isinstance(k, ast.BinOp):
            op = type(k.op)
            if op is ast.Div:
                return r"\frac{" + lx(k.left) + "}{" + lx(k.right) + "}"
            if op is ast.Pow:
                s = "{" + lx(k.left, 5) + "}^{" + lx(k.right) + "}"
            else:
                p = _PREC[op]
                zeichen = {ast.Add: " + ", ast.Sub: " - ", ast.Mult: r" \cdot "}[op]
                s = lx(k.left, p) + zeichen + lx(k.right, p + (0.5 if op is ast.Sub else 0), rechts=True)
        elif isinstance(k, ast.Call):
            f = k.func.id
            a = [lx(x) for x in k.args]
            s = {"sqrt": lambda: r"\sqrt{" + a[0] + "}", "abs": lambda: r"\left|" + a[0] + r"\right|",
                 "ceil": lambda: r"\left\lceil " + a[0] + r" \right\rceil", "floor": lambda: r"\left\lfloor " + a[0] + r" \right\rfloor",
                 }.get(f, lambda: "\\" + ("arctan" if f == "atan" else f) + r"\left(" + r",\ ".join(a) + r"\right)")()
            return s
        else:
            raise NachweisFehler(type(k).__name__)
        if prec(k) < eltern_prec:
            return r"\left(" + s + r"\right)"
        return s

    return lx(baum)


# ===========================================================================
# 5. Der Nachweis
# ===========================================================================

STATUS = ("erfüllt", "nicht erfüllt", "Hinweis")


def _vergleiche(ist: float, grenz: float, vergleich: str, tol: float) -> bool:
    if vergleich == "≤":
        return ist <= grenz + tol
    if vergleich == "<":
        return ist < grenz + tol
    if vergleich == "≥":
        return ist >= grenz - tol
    if vergleich == ">":
        return ist > grenz - tol
    return abs(ist - grenz) <= tol


def _ausnutzung(ist: float, grenz: float, vergleich: str) -> float | None:
    if vergleich in ("≤", "<"):
        return ist / grenz if grenz > 0 and ist >= 0 else None
    if vergleich in ("≥", ">"):
        return grenz / ist if ist > 0 and grenz >= 0 else None
    return None


def kanonisch_json(obj: Any) -> str:
    """Kanonisches JSON für den Hash: sortierte Schlüssel, keine Leerzeichen,
    UTF-8, Gleitkommazahlen in Pythons kürzester Rundlauf-Darstellung
    (angelehnt an RFC 8785, ohne dessen Zahlenformat vollständig umzusetzen)."""
    return json.dumps(obj, sort_keys=True, ensure_ascii=False, separators=(",", ":"), allow_nan=False)


def _zeitstempel(wert: str | None) -> str | None:
    if wert == "jetzt":
        return datetime.now(timezone.utc).replace(microsecond=0).isoformat()
    if wert is None and os.environ.get("SOURCE_DATE_EPOCH"):
        return datetime.fromtimestamp(int(os.environ["SOURCE_DATE_EPOCH"]), timezone.utc).isoformat()
    return wert


def umgebung() -> dict:
    """Software-Umgebung (Software Citation Principles: Specificity)."""
    pakete = {}
    for name in ("numpy", "pint", "matplotlib", "shapely", "ifcopenshell", "ifctester"):
        try:
            mod = __import__(name)
            pakete[name] = getattr(mod, "__version__", None) or getattr(mod, "version", None)
        except ImportError:
            continue
    return {"nachweis_modul": __version__, "schema_version": SCHEMA_VERSION, "python": platform.python_version(),
            "einheiten_backend": EINHEITEN.name, "grafik_backend": "matplotlib" if _mpl() else "svg", "pakete": pakete}


@dataclass
class Nachweis:
    """Ein Nachweis. Nach dem Anlegen `rechne()` aufrufen (erfolgt auch implizit
    beim Export). Einzelkriterium über `ergebnis`/`grenzwert`/`vergleich`,
    weitere über `kriterien`."""
    id: str
    titel: str
    gegenstand: Gegenstand
    regel: Regel
    eingaben: list[Groesse] = field(default_factory=list)
    schritte: list[Schritt] = field(default_factory=list)
    ergebnis: str | None = None                  # Symbol der maßgebenden Ergebnisgröße
    grenzwert: Groesse | str | None = None       # Größe (wird Eingabe) oder Symbol
    vergleich: str | None = None
    kriterien: list[Kriterium] = field(default_factory=list)
    ergebnis_rundung: Rundung | None = None
    annahmen: list[str] = field(default_factory=list)
    hinweise: list[str] = field(default_factory=list)
    grafiken: list[Grafik] = field(default_factory=list)
    k: float = 2.0
    monte_carlo: int = 0                          # Anzahl Versuche (0 = aus)
    monte_carlo_seed: int = 20260927
    zeitstempel: str | None = None
    kriterium_norm_verweis: str = ""
    kriterium_toleranz: float = 0.0
    # Ergebnisse
    status: str | None = None
    ausnutzung: float | None = None
    unsicherheit: dict | None = None
    gegenrechnungen: list[dict] = field(default_factory=list)
    _gerechnet: bool = field(default=False, repr=False)

    # --- Aufbau -------------------------------------------------------------
    def __post_init__(self):
        if not re.fullmatch(r"[A-Za-z0-9_.\-]+", self.id):
            raise NachweisFehler(f"Nachweis-ID {self.id!r}")
        if isinstance(self.grenzwert, Groesse):
            g = self.grenzwert
            g.art = "grenzwert"
            if all(e.symbol != g.symbol for e in self.eingaben):
                self.eingaben.append(g)
            self.grenzwert = g.symbol
        if self.ergebnis and self.grenzwert and self.vergleich:
            self.kriterien.insert(0, Kriterium(f"{self.ergebnis} {self.vergleich} {self.grenzwert}", self.ergebnis,
                                               self.vergleich, self.grenzwert, self.kriterium_norm_verweis,
                                               self.kriterium_toleranz))
        self.zeitstempel = _zeitstempel(self.zeitstempel)

    def groessen(self) -> dict[str, Groesse]:
        alle: dict[str, Groesse] = {}
        for g in list(self.eingaben) + [s.ergebnis for s in self.schritte]:
            if g.symbol in alle:
                raise NachweisFehler(f"{self.id}: Symbol '{g.symbol}' doppelt definiert")
            alle[g.symbol] = g
        return alle

    def gegenrechnung(self, symbol: str, wert: float, rechenkern: str, toleranz_abs: float = 1e-9) -> "Nachweis":
        """Vergleich mit dem unabhängig laufenden Rechenkern (Zweitrechnung)."""
        self.gegenrechnungen.append({"symbol": symbol, "rechenkern": rechenkern, "wert_rechenkern": wert,
                                     "toleranz_abs": toleranz_abs})
        self._gerechnet = False
        return self

    # --- Rechnen ------------------------------------------------------------
    def rechne(self) -> "Nachweis":
        G = self.groessen()
        fn = EINHEITEN.funktionen()
        ns: dict[str, Any] = {}
        for g in self.eingaben:
            if g.numerisch:
                ns[g.symbol] = EINHEITEN.groesse(g.wert, g.einheit)
        for i, s in enumerate(self.schritte, 1):
            erg = s.ergebnis
            if s.ausdruck is not None:
                baum = parse_ausdruck(s.ausdruck)
                s.eingaben = namen_in(s.ausdruck)
                fehlend = [n for n in s.eingaben if n not in ns]
                if fehlend:
                    raise NachweisFehler(f"{self.id}, Schritt {i}: Symbol(e) {', '.join(fehlend)} vorher nicht definiert")
                try:
                    q = werte_aus(baum, ns, fn)
                    erg.wert = EINHEITEN.in_einheit(q, erg.einheit)
                except EinheitenFehler as e:
                    raise EinheitenFehler(f"{self.id}, Schritt {i} ({s.beschreibung}): {e}") from e
                if s.formel_latex is None:
                    s.formel_latex = f"{erg.tex} = " + ausdruck_latex(s.ausdruck, lambda n: G[n].tex)
                s.einsetzen_latex = self._einsetzen(s, G)
            elif not erg.numerisch and not isinstance(erg.wert, (bool, str)):
                raise NachweisFehler(f"{self.id}, Schritt {i}: Verfahrensschritt ohne Ergebniswert")
            if erg.numerisch:
                ns[erg.symbol] = EINHEITEN.groesse(erg.wert, erg.einheit)
        if self.ergebnis:
            if G[self.ergebnis].art == "zwischenergebnis":
                G[self.ergebnis].art = "ergebnis"
            if self.ergebnis_rundung:
                G[self.ergebnis].rundung = self.ergebnis_rundung
        self._unsicherheit(G)
        self._kriterien(G)
        self._gegenrechnen(G)
        self._gerechnet = True
        return self

    def _einsetzen(self, s: Schritt, G: dict[str, Groesse]) -> str:
        def wert(n):
            g = G[n]
            zwischen = g.art in ("zwischenergebnis", "ergebnis") and isinstance(g.wert, float)
            z = zahl_latex(ZWISCHENWERT.runde(g.wert)) if zwischen else zahl_latex(g.wert)
            e = einheit_latex(g.einheit)
            t = z + (r"\ " + e if e else "")
            return r"\left(" + t + r"\right)" if (isinstance(g.wert, (int, float)) and g.wert < 0) else t
        rechts = ausdruck_latex(s.ausdruck, wert)
        e = einheit_latex(s.ergebnis.einheit)
        z = zahl_latex(ZWISCHENWERT.runde(s.ergebnis.wert)) if isinstance(s.ergebnis.wert, float) else zahl_latex(s.ergebnis.wert)
        return f"{s.ergebnis.tex} = {rechts} = {z}" + (r"\ " + e if e else "")

    # SI-Kette für Ableitungen und Monte-Carlo --------------------------------
    def _si_kette(self, x: dict[str, Any]) -> dict[str, Any]:
        """Rechnet alle Ausdrucks-Schritte in SI-Zahlenwerten (Einheiten wurden
        bereits im Größenlauf geprüft; kohärente SI-Einheiten machen die
        Zahlenwertgleichungen einheitenrichtig)."""
        fn = _np_funktionen()
        ns = dict(x)
        for s in self.schritte:
            if s.ausdruck is not None:
                ns[s.ergebnis.symbol] = werte_aus(parse_ausdruck(s.ausdruck), ns, fn)
        return ns

    def _si_start(self, G) -> dict[str, float]:
        x = {}
        for g in self.eingaben:
            if g.numerisch:
                x[g.symbol] = g.wert * EINHEITEN.si_faktor(g.einheit)
        for s in self.schritte:
            if s.ausdruck is None and s.ergebnis.numerisch:
                x[s.ergebnis.symbol] = s.ergebnis.wert * EINHEITEN.si_faktor(s.ergebnis.einheit)
        return x

    def _unsicherheit(self, G: dict[str, Groesse]) -> None:
        unsicher = [g for g in self.eingaben if g.numerisch and g.unsicherheit]
        if not unsicher or not self.ergebnis or G[self.ergebnis].wert is None:
            self.unsicherheit = None
            return
        ziel = G[self.ergebnis]
        x0 = self._si_start(G)
        y0 = self._si_kette(x0)
        # Selbstkontrolle: SI-Kette = Größenlauf
        ys = y0[ziel.symbol] / EINHEITEN.si_faktor(ziel.einheit)
        if not math.isclose(ys, ziel.wert, rel_tol=1e-9, abs_tol=1e-12):
            raise NachweisFehler(f"{self.id}: SI-Kette weicht vom Größenlauf ab ({ys} ≠ {ziel.wert})")
        fy = EINHEITEN.si_faktor(ziel.einheit)
        beitraege, summe = [], 0.0
        for g in unsicher:
            fx = EINHEITEN.si_faktor(g.einheit)
            h = max(abs(x0[g.symbol]), 1e-12) * 1e-6
            xp, xm = dict(x0), dict(x0)
            xp[g.symbol] += h
            xm[g.symbol] -= h
            c_si = (self._si_kette(xp)[ziel.symbol] - self._si_kette(xm)[ziel.symbol]) / (2 * h)
            c = float(c_si * fx / fy)            # in Einheit(Ergebnis)/Einheit(Eingang)
            ui = abs(c) * g.unsicherheit
            summe += ui ** 2
            beitraege.append({"symbol": g.symbol, "u": g.unsicherheit, "einheit": g.einheit,
                              "sensitivitaet": c, "sensitivitaet_einheit": f"({ziel.einheit})/({g.einheit})", "beitrag": ui})
        uc = math.sqrt(summe)
        for b in beitraege:
            b["anteil"] = (b["beitrag"] ** 2 / summe) if summe > 0 else 0.0
        U = self.k * uc
        d = {"methode": "lineare Fortpflanzung erster Ordnung, unkorrelierte Eingangsgrößen (JCGM 100:2008, 5.1.2, Gl. 10); "
                        "Sensitivitäten numerisch durch zentrale Differenzen über die gesamte Rechenkette",
             "k": self.k, "u_c": uc, "U": U, "einheit": ziel.einheit, "beitraege": beitraege,
             "nicht_fortgepflanzt": [s.ergebnis.symbol for s in self.schritte if s.ausdruck is None and s.ergebnis.numerisch]}
        y_txt, U_txt = runde_mit_unsicherheit(ziel.wert, U) if U > 0 else (zahl_roh(ziel.wert), "0")
        d["anzeige"] = f"{y_txt} ± {U_txt} {ziel.einheit} (k = {zahl_roh(self.k)})".replace(" 1 (", " (")
        if self.monte_carlo:
            d["monte_carlo"] = self._monte_carlo(G, x0, unsicher, ziel)
        self.unsicherheit = d

    def _monte_carlo(self, G, x0, unsicher, ziel) -> dict:
        rng = np.random.default_rng(self.monte_carlo_seed)
        n = int(self.monte_carlo)
        x = dict(x0)
        for g in unsicher:
            f = EINHEITEN.si_faktor(g.einheit)
            mu, u = g.wert * f, g.unsicherheit * f
            if g.verteilung == "rechteck":
                a = u * math.sqrt(3.0)
                x[g.symbol] = rng.uniform(mu - a, mu + a, n)
            else:
                x[g.symbol] = rng.normal(mu, u, n)
        y = np.asarray(self._si_kette(x)[ziel.symbol], dtype=float) / EINHEITEN.si_faktor(ziel.einheit)
        lo, hi = np.quantile(y, [0.025, 0.975])
        return {"methode": "Monte-Carlo-Fortpflanzung der Verteilungen (JCGM 101:2008), numpy.random.default_rng (PCG64)",
                "versuche": n, "seed": self.monte_carlo_seed, "mittelwert": float(np.mean(y)),
                "standardabweichung": float(np.std(y, ddof=1)), "intervall_95": [float(lo), float(hi)]}

    def _kriterien(self, G: dict[str, Groesse]) -> None:
        maßgebend = None
        for kr in self.kriterien:
            for s in (kr.ist, kr.grenzwert):
                if s not in G:
                    raise NachweisFehler(f"{self.id}: Kriterium '{kr.bezeichnung}' verweist auf unbekanntes Symbol '{s}'")
            gi, gg = G[kr.ist], G[kr.grenzwert]
            if not (gi.numerisch and gg.numerisch):
                raise NachweisFehler(f"{self.id}: Kriterium '{kr.bezeichnung}' braucht numerische Werte")
            try:
                ist = EINHEITEN.in_einheit(EINHEITEN.groesse(gi.wert, gi.einheit), gg.einheit)
            except EinheitenFehler as e:
                raise EinheitenFehler(f"{self.id}: Kriterium '{kr.bezeichnung}': {e}") from e
            kr.ist_wert, kr.grenz_wert, kr.einheit = ist, float(gg.wert), gg.einheit
            kr.erfuellt = _vergleiche(ist, kr.grenz_wert, kr.vergleich, kr.toleranz)
            kr.ausnutzung = _ausnutzung(ist, kr.grenz_wert, kr.vergleich)
            r = gi.rundung or self.ergebnis_rundung if kr.ist == self.ergebnis else gi.rundung
            if r is not None:
                gerundet = float(r.runde(gi.wert)) * (ist / gi.wert if gi.wert else 1.0)
                kr.rundungsempfindlich = _vergleiche(gerundet, kr.grenz_wert, kr.vergleich, kr.toleranz) != kr.erfuellt
            if self.unsicherheit and kr.ist == self.ergebnis and kr.vergleich != "=":
                U = self.unsicherheit["U"] * (ist / gi.wert if gi.wert else 1.0)
                kr.innerhalb_unsicherheit = abs(ist - kr.grenz_wert) <= U
            if maßgebend is None or (not kr.erfuellt and maßgebend.erfuellt) or (
                    kr.erfuellt == maßgebend.erfuellt and (kr.ausnutzung or 0) > (maßgebend.ausnutzung or 0)):
                maßgebend = kr
        if not self.kriterien:
            self.status, self.ausnutzung = "Hinweis", None
            return
        self.status = "erfüllt" if all(k.erfuellt for k in self.kriterien) else "nicht erfüllt"
        werte = [k.ausnutzung for k in self.kriterien if k.ausnutzung is not None]
        self.ausnutzung = max(werte) if werte else None
        self._maßgebend = maßgebend

    def _gegenrechnen(self, G: dict[str, Groesse]) -> None:
        for gr in self.gegenrechnungen:
            g = G.get(gr["symbol"])
            if g is None or not g.numerisch:
                raise NachweisFehler(f"{self.id}: Gegenrechnung für unbekanntes Symbol {gr['symbol']}")
            gr["wert_nachweis"] = g.wert
            gr["abweichung"] = abs(g.wert - gr["wert_rechenkern"])
            gr["uebereinstimmung"] = gr["abweichung"] <= gr["toleranz_abs"]

    # --- Export -------------------------------------------------------------
    def _sicher(self):
        if not self._gerechnet:
            self.rechne()

    def maßgebendes_kriterium(self) -> Kriterium | None:
        self._sicher()
        return getattr(self, "_maßgebend", None)

    def als_dict(self, mit_hash: bool = True) -> dict:
        self._sicher()
        G = self.groessen()
        mk = self.maßgebendes_kriterium()
        erg = G.get(self.ergebnis) if self.ergebnis else None
        grenz = G.get(mk.grenzwert) if mk else None
        d = {
            "art": "nachweis", "schema_version": SCHEMA_VERSION, "id": self.id, "titel": self.titel,
            "gegenstand": self.gegenstand.als_dict(), "regel": self.regel.als_dict(),
            "eingaben": [g.als_dict() for g in self.eingaben],
            "schritte": [{"nr": i, "beschreibung": s.beschreibung, "ausdruck": s.ausdruck, "formel_latex": s.formel_latex,
                          "einsetzen_latex": s.einsetzen_latex, "eingaben": list(s.eingaben), "verfahren": s.verfahren,
                          "norm_verweis": s.norm_verweis, "ergebnis": s.ergebnis.als_dict()}
                         for i, s in enumerate(self.schritte, 1)],
            "kriterien": [k.als_dict() for k in self.kriterien],
            "ergebnis": erg.als_dict() if erg else None,
            "grenzwert": grenz.als_dict() if grenz else None,
            "vergleich": mk.vergleich if mk else None,
            "ausnutzung": self.ausnutzung, "status": self.status,
            "annahmen": list(self.annahmen) + [f"{g.name} ({g.symbol}) = {g.anzeige()}: {g.quelle}"
                                               for g in self.eingaben if g.art == "annahme"],
            "hinweise": self._alle_hinweise(),
            "unsicherheit": self.unsicherheit, "gegenrechnungen": self.gegenrechnungen,
            "grafiken": [g.als_dict() for g in self.grafiken],
            "rundung_zwischenwerte": ZWISCHENWERT.als_dict(),
            "umgebung": umgebung(), "zeitstempel": self.zeitstempel,
        }
        if mit_hash:
            d["hash"] = {"algorithmus": "SHA-256", "wert": inhalts_hash(d),
                         "umfang": "kanonisches JSON des Nachweises ohne die Felder hash, zeitstempel und umgebung"}
        return d

    def _alle_hinweise(self) -> list[str]:
        h = list(self.hinweise)
        for k in self.kriterien:
            if k.rundungsempfindlich:
                h.append(f"Kriterium '{k.bezeichnung}': Der gerundete Anzeigewert führt zu einer anderen Entscheidung als der "
                         "ungerundete Wert. Maßgebend ist der ungerundete Wert.")
            if k.innerhalb_unsicherheit:
                h.append(f"Kriterium '{k.bezeichnung}': Der Abstand zum Grenzwert ist kleiner als die erweiterte Unsicherheit U "
                         "(Konformitätsaussage unsicher, vgl. JCGM 106:2012).")
        if self.unsicherheit and self.unsicherheit.get("nicht_fortgepflanzt"):
            h.append("Unsicherheitsbeiträge der Verfahrensschritte " + ", ".join(self.unsicherheit["nicht_fortgepflanzt"])
                     + " sind nicht fortgepflanzt.")
        for gr in self.gegenrechnungen:
            if not gr.get("uebereinstimmung", True):
                h.append(f"Gegenrechnung {gr['symbol']}: Abweichung zum Rechenkern {gr['abweichung']:.3g} > Toleranz.")
        return h

    @property
    def hash(self) -> str:
        return self.als_dict()["hash"]["wert"]

    def json(self) -> str:
        return json.dumps(self.als_dict(), ensure_ascii=False, indent=2, sort_keys=False) + "\n"

    def markdown(self, svg_pfad: Callable[[Grafik], str] | None = None, ebene: int = 1) -> str:
        return _md_nachweis(self.als_dict(), svg_pfad, ebene)

    def html(self) -> str:
        d = self.als_dict()
        return _html_seite(d["titel"], _html_nachweis(d, 1))

    def schreibe(self, ordner: Path | str, basis: str | None = None) -> dict[str, Path]:
        return _schreibe([self], ordner, basis or self.id, heft=None)


def inhalts_hash(d: dict) -> str:
    kern = {k: v for k, v in d.items() if k not in ("hash", "zeitstempel", "umgebung")}
    return hashlib.sha256(kanonisch_json(kern).encode("utf-8")).hexdigest()


# ===========================================================================
# 6. Nachweisheft
# ===========================================================================

@dataclass
class Nachweisheft:
    """Bündel mehrerer Nachweise mit Deckblatt, Inhaltsverzeichnis und Heft-Hash."""
    titel: str
    projekt: dict
    nachweise: list[Nachweis]
    verfasser: str = "Entwurfsgenerator (Beispiel), ohne Prüfvermerk"
    zeitstempel: str | None = None
    vorbemerkung: str = ""

    def __post_init__(self):
        self.zeitstempel = _zeitstempel(self.zeitstempel)
        ids = [n.id for n in self.nachweise]
        if len(set(ids)) != len(ids):
            raise NachweisFehler("Nachweis-IDs im Heft nicht eindeutig")

    def als_dict(self) -> dict:
        nd = [n.als_dict() for n in self.nachweise]
        profile = sorted({(x["regel"]["regelwerk_profil"]["name"], x["regel"]["regelwerk_profil"]["version"]) for x in nd})
        quellen = sorted({(x["regel"]["quelle"], x["regel"]["fassung"], x["regel"]["verifikation"]) for x in nd})
        zaehl = {s: sum(1 for x in nd if x["status"] == s) for s in STATUS}
        d = {"art": "nachweisheft", "schema_version": SCHEMA_VERSION, "titel": self.titel, "projekt": self.projekt,
             "verfasser": self.verfasser, "vorbemerkung": self.vorbemerkung,
             "regelwerk_profile": [{"name": a, "version": b} for a, b in profile],
             "regelquellen": [{"quelle": a, "fassung": b, "verifikation": c} for a, b, c in quellen],
             "zusammenfassung": zaehl,
             "status": "nicht erfüllt" if zaehl["nicht erfüllt"] else ("erfüllt" if zaehl["erfüllt"] else "Hinweis"),
             "inhalt": [{"id": x["id"], "titel": x["titel"], "status": x["status"], "ausnutzung": x["ausnutzung"],
                         "hash": x["hash"]["wert"], "gegenstand": x["gegenstand"]["ifc_guid"]} for x in nd],
             "nachweise": nd, "umgebung": umgebung(), "zeitstempel": self.zeitstempel}
        kern = {"titel": self.titel, "projekt": self.projekt, "inhalt": d["inhalt"]}
        d["hash"] = {"algorithmus": "SHA-256", "wert": hashlib.sha256(kanonisch_json(kern).encode("utf-8")).hexdigest(),
                     "umfang": "kanonisches JSON aus Titel, Projekt und der geordneten Liste (ID, Status, Ausnutzung, "
                               "Hash, GUID) aller Nachweise"}
        return d

    def json(self) -> str:
        return json.dumps(self.als_dict(), ensure_ascii=False, indent=2) + "\n"

    def markdown(self, svg_pfad: Callable[[Grafik], str] | None = None) -> str:
        return _md_heft(self.als_dict(), svg_pfad)

    def html(self) -> str:
        return _html_heft(self.als_dict())

    def schreibe(self, ordner: Path | str, basis: str) -> dict[str, Path]:
        return _schreibe(self.nachweise, ordner, basis, heft=self)


def _schreibe(nachweise: list[Nachweis], ordner, basis: str, heft: Nachweisheft | None) -> dict[str, Path]:
    """JSON, Markdown und HTML schreiben; SVG-Grafiken zusätzlich als Dateien unter svg/."""
    ordner = Path(ordner)
    (ordner / "svg").mkdir(parents=True, exist_ok=True)
    for n in nachweise:
        for g in n.grafiken:
            (ordner / "svg" / f"{n.id}_{g.id}.svg").write_text(g.svg, encoding="utf-8")

    def svg_pfad(nid: str, gid: str) -> str:
        return f"svg/{nid}_{gid}.svg"

    obj = heft if heft is not None else nachweise[0]
    d = obj.als_dict()
    pfade = {"json": ordner / f"{basis}.json", "md": ordner / f"{basis}.md", "html": ordner / f"{basis}.html"}
    pfade["json"].write_text(json.dumps(d, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    if heft is not None:
        pfade["md"].write_text(_md_heft(d, svg_pfad), encoding="utf-8")
        pfade["html"].write_text(_html_heft(d), encoding="utf-8")
    else:
        pfade["md"].write_text(_md_nachweis(d, svg_pfad, 1), encoding="utf-8")
        pfade["html"].write_text(_html_seite(d["titel"], _html_nachweis(d, 1)), encoding="utf-8")
    return pfade


# ===========================================================================
# 7. Markdown
# ===========================================================================

_STATUS_TEXT = {"erfüllt": "ERFÜLLT", "nicht erfüllt": "NICHT ERFÜLLT", "Hinweis": "HINWEIS"}


def _md_esc(s: Any) -> str:
    return str(s if s is not None else "–").replace("|", "\\|").replace("\n", " ")


def _eta(v: float | None) -> str:
    return "–" if v is None else zahl_de(AUSNUTZUNG.runde(v))


def _anz(wert, einheit, rundung: dict | None = None) -> str:
    if wert is None:
        return "–"
    if isinstance(wert, bool) or not isinstance(wert, (int, float)):
        return zahl_roh(wert) if isinstance(wert, bool) else str(wert)
    if rundung:
        z = zahl_de(Rundung(rundung["art"], rundung["stellen"], rundung["verfahren"]).runde(wert))
    else:
        z = zahl_roh(wert)
    e = einheit if einheit not in ("1", "", "-", "–") else ""
    return f"{z} {e}".strip()


def _md_nachweis(d: dict, svg_pfad, ebene: int = 1) -> str:
    h = "#" * ebene
    z = [f"{h} {d['id']} – {d['titel']}", "",
         f"**Ergebnis: [{_STATUS_TEXT[d['status']]}]**" + (f" · maßgebende Ausnutzung η = {_eta(d['ausnutzung'])}" if d["ausnutzung"] is not None else ""), ""]
    g, r = d["gegenstand"], d["regel"]
    z += [f"{h}# Gegenstand", "", "| Merkmal | Wert |", "|---|---|", f"| Bezeichnung | {_md_esc(g['bezeichnung'])} |",
          f"| IFC-GlobalId | `{g['ifc_guid'] or '–'}` |", f"| IFC-Klasse | {_md_esc(g['ifc_klasse'])} |",
          f"| IFC-Datei (SHA-256) | {_md_esc(g['ifc_datei'])} ({'`' + g['ifc_sha256'][:16] + '…`' if g['ifc_sha256'] else '–'}) |"]
    if g["weitere_guids"]:
        z.append(f"| weitere GUIDs | {', '.join('`' + x + '`' for x in g['weitere_guids'][:12])}{' …' if len(g['weitere_guids']) > 12 else ''} |")
    z += ["", f"{h}# Regel", "", f"> {r['text']}", "",
          f"Quelle: {r['quelle']} · Fassung: {r['fassung']} · Fundstelle: {r['fundstelle'] or '–'} · Prüfung am Primärtext: {r['verifikation']}  ",
          f"Regelwerk-Profil: `{r['regelwerk_profil']['name']}` Version `{r['regelwerk_profil']['version']}`", ""]
    z += [f"{h}# Eingangsgrößen", "", "| Größe | Symbol | Wert | u (k=1) | Art | Quelle |", "|---|---|---:|---:|---|---|"]
    for e in d["eingaben"]:
        u = _anz(e["unsicherheit"], e["einheit"]) if e["unsicherheit"] else "–"
        z.append(f"| {_md_esc(e['name'])} | ${e['latex']}$ | {_md_esc(e['anzeige'])} | {u} | {e['art']} | {_md_esc(e['quelle'])} |")
    if d["annahmen"]:
        z += ["", f"{h}# Annahmen", ""] + [f"- **Annahme:** {a}" for a in d["annahmen"]]
    z += ["", f"{h}# Rechengang", "", f"Gerechnet wird ungerundet. Angezeigte Zwischenwerte: {d['rundung_zwischenwerte']['text']}.", ""]
    for s in d["schritte"]:
        z.append(f"**Schritt {s['nr']}: {s['beschreibung']}**" + (f" ({s['norm_verweis']})" if s["norm_verweis"] else ""))
        z.append("")
        if s["formel_latex"]:
            z += ["$$", s["formel_latex"], "$$", ""]
        if s["einsetzen_latex"]:
            z += ["$$", s["einsetzen_latex"], "$$", ""]
        if s["verfahren"]:
            z += [f"Verfahren: {s['verfahren']}", "", f"Ergebnis: ${s['ergebnis']['latex']}$ = {s['ergebnis']['anzeige']}", ""]
        if s["ausdruck"]:
            z += [f"Ausdruck (maschinenlesbar): `{s['ausdruck']}`", ""]
    z += [f"{h}# Nachweis", ""]
    if d["kriterien"]:
        z += ["| Kriterium | Ist | Vergleich | Grenzwert | η | Ergebnis | Normverweis |", "|---|---:|:---:|---:|---:|---|---|"]
        for k in d["kriterien"]:
            z.append(f"| {_md_esc(k['bezeichnung'])} | {_anz(k['ist_wert'], k['einheit'], _rund_von(d, k['ist']))} | {k['vergleich']} | "
                     f"{_anz(k['grenz_wert'], k['einheit'])} | {_eta(k['ausnutzung'])} | "
                     f"{'erfüllt' if k['erfuellt'] else '**nicht erfüllt**'} | {_md_esc(k['norm_verweis'])} |")
        z.append("")
        z.append("Der Vergleich erfolgt mit ungerundeten Werten" + (", Toleranzen siehe JSON." if any(k["toleranz"] for k in d["kriterien"]) else "."))
    else:
        z.append("Kein Grenzwertvergleich (informativer Nachweis, Status „Hinweis“).")
    if d["ergebnis"] and d["ergebnis"]["rundung"]:
        z += ["", f"Rundung des Ergebnisses: {d['ergebnis']['rundung']['text']}."]
    u = d["unsicherheit"]
    if u:
        z += ["", f"{h}# Messunsicherheit", "", f"Methode: {u['methode']}.", "",
              f"Ergebnis: **{u['anzeige']}**, kombinierte Standardunsicherheit u_c = {zahl_de(Rundung('signifikant', 2).runde(u['u_c']))} {u['einheit']}.", "",
              "| Eingang | u(x) | Sensitivität c | Einheit von c | Beitrag \\|c\\|·u | Anteil an u_c² |", "|---|---:|---:|---|---:|---:|"]
        for b in u["beitraege"]:
            z.append(f"| {b['symbol']} | {_anz(b['u'], b['einheit'])} | {zahl_de(Rundung('signifikant', 3).runde(b['sensitivitaet']))} | {b['sensitivitaet_einheit']} | "
                     f"{zahl_de(Rundung('signifikant', 2).runde(b['beitrag']))} | {zahl_de(Rundung('dezimalstellen', 1).runde(100 * b['anteil']))} % |")
        mc = u.get("monte_carlo")
        if mc:
            z += ["", f"Monte-Carlo ({mc['methode']}; {zahl_de(mc['versuche'])} Versuche, Seed {mc['seed']}): Mittelwert "
                      f"{zahl_de(Rundung('signifikant', 4).runde(mc['mittelwert']))}, s = {zahl_de(Rundung('signifikant', 2).runde(mc['standardabweichung']))}, "
                      f"95-%-Intervall [{zahl_de(Rundung('signifikant', 4).runde(mc['intervall_95'][0]))}; "
                      f"{zahl_de(Rundung('signifikant', 4).runde(mc['intervall_95'][1]))}] {u['einheit']}."]
    if d["gegenrechnungen"]:
        z += ["", f"{h}# Gegenrechnung mit dem Rechenkern", "", "| Größe | Rechenkern | Nachweis | Abweichung | Übereinstimmung |", "|---|---|---:|---:|---|"]
        for gr in d["gegenrechnungen"]:
            z.append(f"| {gr['symbol']} | `{gr['rechenkern']}` = {zahl_roh(gr['wert_rechenkern'])} | {zahl_roh(gr['wert_nachweis'])} | "
                     f"{gr['abweichung']:.2e} | {'ja' if gr['uebereinstimmung'] else '**nein**'} (Toleranz {gr['toleranz_abs']:.0e}) |")
    if d["hinweise"]:
        z += ["", f"{h}# Hinweise", ""] + [f"- {x}" for x in d["hinweise"]]
    if d["grafiken"]:
        z += ["", f"{h}# Grafischer Nachweis", ""]
        for gr in d["grafiken"]:
            pfad = svg_pfad(d["id"], gr["id"]) if svg_pfad else f"svg/{d['id']}_{gr['id']}.svg"
            z += [f"**Abbildung {d['id']}/{gr['id']}: {gr['titel']}**" + (f" (Maßstab {gr['massstab']})" if gr["massstab"] else ""), "",
                  f"![{gr['titel']}]({pfad})", ""]
            if gr["beschreibung"]:
                z += [gr["beschreibung"], ""]
    z += ["", f"{h}# Rückverfolgbarkeit", "", f"- Hash ({d['hash']['algorithmus']}): `{d['hash']['wert']}`",
          f"- Umfang: {d['hash']['umfang']}",
          f"- Umgebung: Python {d['umgebung']['python']}, Modul nachweis {d['umgebung']['nachweis_modul']}, "
          f"Einheiten: {d['umgebung']['einheiten_backend']}, Grafik: {d['umgebung']['grafik_backend']}, "
          + ", ".join(f"{k} {v}" for k, v in d["umgebung"]["pakete"].items()),
          f"- Zeitstempel: {d['zeitstempel'] or 'nicht gesetzt (deterministischer Lauf)'}", ""]
    return "\n".join(z) + "\n"


def _rund_von(d: dict, symbol: str) -> dict | None:
    for e in d["eingaben"] + [s["ergebnis"] for s in d["schritte"]]:
        if e["symbol"] == symbol:
            return e["rundung"]
    return None


def _md_heft(d: dict, svg_pfad) -> str:
    z = [f"# {d['titel']}", "", "## Deckblatt", "", "| Merkmal | Wert |", "|---|---|"]
    for k, v in d["projekt"].items():
        z.append(f"| {_md_esc(k)} | {_md_esc(v)} |")
    z += [f"| Verfasser | {_md_esc(d['verfasser'])} |",
          f"| Gesamtergebnis | **[{_STATUS_TEXT[d['status']]}]** ({d['zusammenfassung']['erfüllt']} erfüllt, "
          f"{d['zusammenfassung']['nicht erfüllt']} nicht erfüllt, {d['zusammenfassung']['Hinweis']} Hinweis) |",
          f"| Heft-Hash (SHA-256) | `{d['hash']['wert']}` |", f"| Zeitstempel | {d['zeitstempel'] or 'nicht gesetzt (deterministischer Lauf)'} |", ""]
    if d["vorbemerkung"]:
        z += [d["vorbemerkung"], ""]
    z += ["Regelwerk-Profile:", ""] + [f"- `{p['name']}` Version `{p['version']}`" for p in d["regelwerk_profile"]]
    z += ["", "Regelquellen:", ""] + [f"- {q['quelle']}, Fassung {q['fassung']} {q['verifikation']}" for q in d["regelquellen"]]
    z += ["", "## Inhaltsverzeichnis", "", "| Nr. | ID | Titel | Status | η | Hash (Anfang) |", "|---:|---|---|---|---:|---|"]
    for i, x in enumerate(d["inhalt"], 1):
        z.append(f"| {i} | [{x['id']}](#{_anker(x['id'])}) | {_md_esc(x['titel'])} | {x['status']} | {_eta(x['ausnutzung'])} | `{x['hash'][:12]}` |")
    z.append("")
    for n in d["nachweise"]:
        z += [f'<a id="{_anker(n["id"])}"></a>', "", _md_nachweis(n, svg_pfad, 2)]
    return "\n".join(z)


def _anker(s: str) -> str:
    return "n-" + re.sub(r"[^a-z0-9]+", "-", s.lower()).strip("-")


# ===========================================================================
# 8. HTML
# ===========================================================================

_CSS = """
:root{--flaeche:#fcfcfb;--seite:#f9f9f7;--tinte:#0b0b0b;--tinte2:#52514e;--leise:#898781;--linie:#e1e0d9;
--gut:#0ca30c;--gut-text:#006300;--warn:#fab219;--krit:#d03b3b;--akzent:#2a78d6;color-scheme:light}
body{background:var(--seite);color:var(--tinte);font:15px/1.5 system-ui,-apple-system,"Segoe UI",sans-serif;margin:0}
main{max-width:980px;margin:0 auto;padding:24px 16px;background:var(--flaeche)}
h1{font-size:1.6em;margin:.2em 0}h2{font-size:1.3em;border-bottom:1px solid var(--linie);padding-bottom:.2em;margin-top:1.6em}
h3{font-size:1.1em;margin-top:1.3em}h4{font-size:1em}
table{border-collapse:collapse;width:100%;margin:.5em 0;font-size:.92em}
th,td{border:1px solid var(--linie);padding:4px 6px;vertical-align:top;text-align:left}
th{background:#f0efec;font-weight:600}td.z{text-align:right;font-variant-numeric:tabular-nums;white-space:nowrap}
code{font-size:.88em;word-break:break-all}.leise{color:var(--tinte2);font-size:.9em}
.ampel{display:inline-flex;align-items:center;gap:.45em;font-weight:700;padding:.25em .7em;border-radius:4px;border:1px solid var(--linie)}
.ampel i{width:.9em;height:.9em;border-radius:50%;display:inline-block}
.s-erfuellt i{background:var(--gut)}.s-nicht i{background:var(--krit)}.s-hinweis i{background:var(--warn)}
.s-erfuellt{color:var(--gut-text)}.s-nicht{color:var(--krit)}.s-hinweis{color:#7a5500}
.regel{border-left:4px solid var(--akzent);background:#f3f7fd;padding:.5em .9em;margin:.5em 0}
.annahme{background:#fff7e0;border-left:4px solid var(--warn);padding:.3em .8em;margin:.2em 0}
.schritt{border:1px solid var(--linie);border-radius:4px;padding:.4em .8em;margin:.6em 0;overflow-x:auto}
.formel{overflow-x:auto}figure{margin:1em 0;overflow-x:auto}figcaption{font-size:.9em;color:var(--tinte2)}
figure svg{max-width:100%;height:auto;background:#fff}
.deckblatt{border:2px solid var(--tinte);padding:1em 1.2em;margin-bottom:2em}
section.nachweis{margin-top:2.5em}
@media print{body{background:#fff}main{max-width:none;padding:0}section.nachweis{break-before:page}
figure,table,.schritt{break-inside:avoid}a{color:inherit;text-decoration:none}}
@page{size:A4;margin:18mm 15mm}
"""

_MATHJAX = ('<script>window.MathJax={tex:{inlineMath:[["$","$"],["\\\\(","\\\\)"]]},svg:{fontCache:"global"}};</script>\n'
            '<script defer src="https://cdn.jsdelivr.net/npm/mathjax@3.2.2/es5/tex-svg.js"></script>')


def _e(s: Any) -> str:
    return _html.escape("–" if s is None else str(s), quote=True)


def _ampel(status: str) -> str:
    k = {"erfüllt": "s-erfuellt", "nicht erfüllt": "s-nicht", "Hinweis": "s-hinweis"}[status]
    return f'<span class="ampel {k}" role="status"><i aria-hidden="true"></i>{_e(_STATUS_TEXT[status])}</span>'


def _html_seite(titel: str, inhalt: str) -> str:
    return ("<!DOCTYPE html>\n<html lang=\"de\">\n<head>\n<meta charset=\"utf-8\">\n"
            "<meta name=\"viewport\" content=\"width=device-width, initial-scale=1\">\n"
            f"<title>{_e(titel)}</title>\n<style>{_CSS}</style>\n{_MATHJAX}\n</head>\n<body>\n<main>\n{inhalt}\n</main>\n</body>\n</html>\n")


def _svg_inline(svg: str) -> str:
    return re.sub(r"^<\?xml[^>]*\?>\s*", "", re.sub(r"<!DOCTYPE[^>]*>\s*", "", svg)).strip()


def _html_nachweis(d: dict, ebene: int = 1) -> str:
    h1, h2 = f"h{ebene}", f"h{ebene + 1}"
    g, r = d["gegenstand"], d["regel"]
    t = [f'<section class="nachweis" id="{_anker(d["id"])}">',
         f"<{h1}>{_e(d['id'])} – {_e(d['titel'])}</{h1}>",
         f"<p>{_ampel(d['status'])}" + (f" &nbsp;maßgebende Ausnutzung η = <b>{_e(_eta(d['ausnutzung']))}</b>" if d["ausnutzung"] is not None else "") + "</p>",
         f"<{h2}>Gegenstand</{h2}><table>",
         f"<tr><th>Bezeichnung</th><td>{_e(g['bezeichnung'])}</td></tr>",
         f"<tr><th>IFC-GlobalId</th><td><code>{_e(g['ifc_guid'])}</code> ({_e(g['ifc_klasse'])})</td></tr>",
         f"<tr><th>IFC-Datei</th><td>{_e(g['ifc_datei'])}<br><span class=\"leise\">SHA-256 <code>{_e(g['ifc_sha256'])}</code></span></td></tr>"]
    if g["weitere_guids"]:
        t.append(f"<tr><th>weitere GUIDs</th><td>{' '.join('<code>' + _e(x) + '</code>' for x in g['weitere_guids'])}</td></tr>")
    t += ["</table>", f"<{h2}>Regel</{h2}>", f'<div class="regel"><p>{_e(r["text"])}</p>',
          f"<p class=\"leise\">Quelle: {_e(r['quelle'])} · Fassung: {_e(r['fassung'])} · Fundstelle: {_e(r['fundstelle'] or '–')} · "
          f"Prüfung am Primärtext: {_e(r['verifikation'])}<br>Regelwerk-Profil <code>{_e(r['regelwerk_profil']['name'])}</code> "
          f"Version <code>{_e(r['regelwerk_profil']['version'])}</code></p></div>",
          f"<{h2}>Eingangsgrößen</{h2}>",
          "<table><thead><tr><th>Größe</th><th>Symbol</th><th>Wert</th><th>u (k=1)</th><th>Art</th><th>Quelle</th></tr></thead><tbody>"]
    for e in d["eingaben"]:
        u = _anz(e["unsicherheit"], e["einheit"]) if e["unsicherheit"] else "–"
        stil = ' class="annahme"' if e["art"] == "annahme" else ""
        t.append(f"<tr{stil}><td>{_e(e['name'])}</td><td>${_e(e['latex'])}$</td><td class=\"z\">{_e(e['anzeige'])}</td>"
                 f"<td class=\"z\">{_e(u)}</td><td>{_e(e['art'])}</td><td>{_e(e['quelle'])}</td></tr>")
    t.append("</tbody></table>")
    if d["annahmen"]:
        t += [f"<{h2}>Annahmen</{h2}>"] + [f'<p class="annahme"><b>Annahme:</b> {_e(a)}</p>' for a in d["annahmen"]]
    t += [f"<{h2}>Rechengang</{h2}>", f"<p class=\"leise\">Gerechnet wird ungerundet. Angezeigte Zwischenwerte: {_e(d['rundung_zwischenwerte']['text'])}.</p>"]
    for s in d["schritte"]:
        t.append(f'<div class="schritt"><p><b>Schritt {s["nr"]}: {_e(s["beschreibung"])}</b>'
                 + (f' <span class="leise">({_e(s["norm_verweis"])})</span>' if s["norm_verweis"] else "") + "</p>")
        if s["formel_latex"]:
            t.append(f'<div class="formel">$$ {_e(s["formel_latex"])} $$</div>')
        if s["einsetzen_latex"]:
            t.append(f'<div class="formel">$$ {_e(s["einsetzen_latex"])} $$</div>')
        if s["verfahren"]:
            t.append(f"<p>Verfahren: {_e(s['verfahren'])}<br>Ergebnis: ${_e(s['ergebnis']['latex'])}$ = {_e(s['ergebnis']['anzeige'])}</p>")
        if s["ausdruck"]:
            t.append(f'<p class="leise">Ausdruck: <code>{_e(s["ausdruck"])}</code></p>')
        t.append("</div>")
    t.append(f"<{h2}>Nachweis</{h2}>")
    if d["kriterien"]:
        t.append("<table><thead><tr><th>Kriterium</th><th>Ist</th><th></th><th>Grenzwert</th><th>η</th><th>Ergebnis</th><th>Normverweis</th></tr></thead><tbody>")
        for k in d["kriterien"]:
            t.append(f"<tr><td>{_e(k['bezeichnung'])}</td><td class=\"z\">{_e(_anz(k['ist_wert'], k['einheit'], _rund_von(d, k['ist'])))}</td>"
                     f"<td>{_e(k['vergleich'])}</td><td class=\"z\">{_e(_anz(k['grenz_wert'], k['einheit']))}</td>"
                     f"<td class=\"z\">{_e(_eta(k['ausnutzung']))}</td><td>{_ampel('erfüllt' if k['erfuellt'] else 'nicht erfüllt')}</td>"
                     f"<td>{_e(k['norm_verweis'])}</td></tr>")
        t.append("</tbody></table><p class=\"leise\">Der Vergleich erfolgt mit ungerundeten Werten.</p>")
    else:
        t.append("<p>Kein Grenzwertvergleich (informativer Nachweis).</p>")
    if d["ergebnis"] and d["ergebnis"]["rundung"]:
        t.append(f"<p class=\"leise\">Rundung des Ergebnisses: {_e(d['ergebnis']['rundung']['text'])}.</p>")
    u = d["unsicherheit"]
    if u:
        t += [f"<{h2}>Messunsicherheit</{h2}>", f"<p>Ergebnis: <b>{_e(u['anzeige'])}</b>; u<sub>c</sub> = "
              f"{_e(zahl_de(Rundung('signifikant', 2).runde(u['u_c'])))} {_e(u['einheit'])}.</p><p class=\"leise\">{_e(u['methode'])}.</p>",
              "<table><thead><tr><th>Eingang</th><th>u(x)</th><th>Sensitivität c</th><th>Einheit von c</th><th>|c|·u</th><th>Anteil an u<sub>c</sub>²</th></tr></thead><tbody>"]
        for b in u["beitraege"]:
            t.append(f"<tr><td>{_e(b['symbol'])}</td><td class=\"z\">{_e(_anz(b['u'], b['einheit']))}</td>"
                     f"<td class=\"z\">{_e(zahl_de(Rundung('signifikant', 3).runde(b['sensitivitaet'])))}</td><td>{_e(b['sensitivitaet_einheit'])}</td>"
                     f"<td class=\"z\">{_e(zahl_de(Rundung('signifikant', 2).runde(b['beitrag'])))}</td>"
                     f"<td class=\"z\">{_e(zahl_de(Rundung('dezimalstellen', 1).runde(100 * b['anteil'])))} %</td></tr>")
        t.append("</tbody></table>")
        mc = u.get("monte_carlo")
        if mc:
            t.append(f"<p>Monte-Carlo: {zahl_de(mc['versuche'])} Versuche (Seed {mc['seed']}), Mittelwert "
                     f"{_e(zahl_de(Rundung('signifikant', 4).runde(mc['mittelwert'])))}, s = {_e(zahl_de(Rundung('signifikant', 2).runde(mc['standardabweichung'])))}, "
                     f"95-%-Intervall [{_e(zahl_de(Rundung('signifikant', 4).runde(mc['intervall_95'][0])))}; "
                     f"{_e(zahl_de(Rundung('signifikant', 4).runde(mc['intervall_95'][1])))}] {_e(u['einheit'])}. "
                     f"<span class=\"leise\">{_e(mc['methode'])}</span></p>")
    if d["gegenrechnungen"]:
        t += [f"<{h2}>Gegenrechnung mit dem Rechenkern</{h2}>",
              "<table><thead><tr><th>Größe</th><th>Rechenkern</th><th>Wert Rechenkern</th><th>Wert Nachweis</th><th>Abweichung</th><th>Übereinstimmung</th></tr></thead><tbody>"]
        for gr in d["gegenrechnungen"]:
            t.append(f"<tr><td>{_e(gr['symbol'])}</td><td><code>{_e(gr['rechenkern'])}</code></td><td class=\"z\">{_e(zahl_roh(gr['wert_rechenkern']))}</td>"
                     f"<td class=\"z\">{_e(zahl_roh(gr['wert_nachweis']))}</td><td class=\"z\">{gr['abweichung']:.2e}</td>"
                     f"<td>{'ja' if gr['uebereinstimmung'] else '<b>nein</b>'} (Toleranz {gr['toleranz_abs']:.0e})</td></tr>")
        t.append("</tbody></table>")
    if d["hinweise"]:
        t += [f"<{h2}>Hinweise</{h2}>", "<ul>"] + [f"<li>{_e(x)}</li>" for x in d["hinweise"]] + ["</ul>"]
    if d["grafiken"]:
        t.append(f"<{h2}>Grafischer Nachweis</{h2}>")
        for gr in d["grafiken"]:
            t.append(f"<figure>{_svg_inline(gr['svg'])}<figcaption>Abbildung {_e(d['id'])}/{_e(gr['id'])}: {_e(gr['titel'])}"
                     + (f" (Maßstab {_e(gr['massstab'])}, bei Druck in 100 %)" if gr["massstab"] else "")
                     + (f". {_e(gr['beschreibung'])}" if gr["beschreibung"] else "") + f"<br><span class=\"leise\">SHA-256 <code>{gr['sha256']}</code></span></figcaption></figure>")
    um = d["umgebung"]
    t += [f"<{h2}>Rückverfolgbarkeit</{h2}>", "<table>",
          f"<tr><th>Hash ({_e(d['hash']['algorithmus'])})</th><td><code>{_e(d['hash']['wert'])}</code><br><span class=\"leise\">{_e(d['hash']['umfang'])}</span></td></tr>",
          f"<tr><th>Umgebung</th><td>Python {_e(um['python'])}, Modul nachweis {_e(um['nachweis_modul'])}, Einheiten: {_e(um['einheiten_backend'])}, "
          f"Grafik: {_e(um['grafik_backend'])}; " + _e(", ".join(f"{k} {v}" for k, v in um["pakete"].items())) + "</td></tr>",
          f"<tr><th>Zeitstempel</th><td>{_e(d['zeitstempel'] or 'nicht gesetzt (deterministischer Lauf)')}</td></tr></table>",
          "</section>"]
    return "\n".join(t)


def _html_heft(d: dict) -> str:
    z = d["zusammenfassung"]
    t = ['<section class="deckblatt">', f"<h1>{_e(d['titel'])}</h1>", f"<p>{_ampel(d['status'])} &nbsp;"
         f"{z['erfüllt']} erfüllt · {z['nicht erfüllt']} nicht erfüllt · {z['Hinweis']} Hinweis</p>", "<table>"]
    for k, v in d["projekt"].items():
        t.append(f"<tr><th>{_e(k)}</th><td>{_e(v)}</td></tr>")
    t += [f"<tr><th>Verfasser</th><td>{_e(d['verfasser'])}</td></tr>",
          "<tr><th>Regelwerk-Profile</th><td>" + "<br>".join(f"<code>{_e(p['name'])}</code> Version <code>{_e(p['version'])}</code>" for p in d["regelwerk_profile"]) + "</td></tr>",
          "<tr><th>Regelquellen</th><td>" + "<br>".join(f"{_e(q['quelle'])}, Fassung {_e(q['fassung'])} {_e(q['verifikation'])}" for q in d["regelquellen"]) + "</td></tr>",
          f"<tr><th>Heft-Hash (SHA-256)</th><td><code>{_e(d['hash']['wert'])}</code><br><span class=\"leise\">{_e(d['hash']['umfang'])}</span></td></tr>",
          f"<tr><th>Zeitstempel</th><td>{_e(d['zeitstempel'] or 'nicht gesetzt (deterministischer Lauf)')}</td></tr></table>"]
    if d["vorbemerkung"]:
        t.append(f"<p>{_e(d['vorbemerkung'])}</p>")
    t += ["</section>", "<h2>Inhaltsverzeichnis</h2>",
          "<table><thead><tr><th>Nr.</th><th>ID</th><th>Titel</th><th>Status</th><th>η</th><th>Hash</th></tr></thead><tbody>"]
    for i, x in enumerate(d["inhalt"], 1):
        t.append(f"<tr><td class=\"z\">{i}</td><td><a href=\"#{_anker(x['id'])}\">{_e(x['id'])}</a></td><td>{_e(x['titel'])}</td>"
                 f"<td>{_ampel(x['status'])}</td><td class=\"z\">{_e(_eta(x['ausnutzung']))}</td><td><code>{_e(x['hash'][:12])}…</code></td></tr>")
    t.append("</tbody></table>")
    for n in d["nachweise"]:
        t.append(_html_nachweis(n, 2))
    return _html_seite(d["titel"], "\n".join(t))


# ===========================================================================
# 9. Grafik
# ===========================================================================

FARBE = {"tinte": "#0b0b0b", "tinte2": "#52514e", "leise": "#898781", "gitter": "#e1e0d9", "achse": "#c3c2b7",
         "flaeche": "#ffffff", "gut": "#0ca30c", "krit": "#d03b3b", "warn": "#fab219", "s1": "#2a78d6", "s2": "#eb6834",
         "s3": "#1baf7a"}


def _mpl():
    try:
        import matplotlib
        return matplotlib
    except ImportError:
        return None


def _f(x: float) -> str:
    """Koordinate mit fester Genauigkeit (deterministisch, 0,01 mm)."""
    s = f"{x:.2f}".rstrip("0").rstrip(".")
    return "0" if s in ("-0", "") else s


class SvgZeichnung:
    """Maßstäbliche technische Zeichnung als SVG.

    Modellkoordinaten (x nach rechts/Osten, y nach oben/Norden) in der
    Einheit `modell_m` (1.0 = Meter, 0.001 = Millimeter) werden im Maßstab
    1:`massstab` auf Papier-Millimeter abgebildet. Das SVG hat width/height
    in mm und viewBox in mm: Bei Druck in 100 % ist die Zeichnung maßhaltig.
    Linienbreiten 0,25/0,35/0,5/0,7 mm (Liniengruppe nach ISO 128-2),
    Schrifthöhen 2,5/3,5/5 mm (ISO 3098), Maßbegrenzung als Schrägstrich
    (Bauzeichnungen, DIN 1356-1 / DIN 406-11)."""

    def __init__(self, bereich: tuple[float, float, float, float], massstab: float, modell_m: float = 1.0,
                 rand_mm: float = 12.0, unten_mm: float = 0.0, titel: str = ""):
        self.minx, self.miny, self.maxx, self.maxy = bereich
        self.massstab, self.modell_m, self.rand, self.titel = massstab, modell_m, rand_mm, titel
        self.k = modell_m * 1000.0 / massstab                     # Papier-mm je Modelleinheit
        self.b = 2 * rand_mm + (self.maxx - self.minx) * self.k
        self.h_zeichnung = 2 * rand_mm + (self.maxy - self.miny) * self.k
        self.h = self.h_zeichnung + unten_mm
        self.teile: list[str] = []
        self.defs: list[str] = []
        self._muster: set[str] = set()

    # Transformation
    def p(self, x: float, y: float) -> tuple[float, float]:
        return self.rand + (x - self.minx) * self.k, self.rand + (self.maxy - y) * self.k

    def _pts(self, coords) -> str:
        return " ".join(f"{_f(a)},{_f(b)}" for a, b in (self.p(x, y) for x, y in coords))

    @staticmethod
    def _attr(**a) -> str:
        return " ".join(f'{k.rstrip("_").replace("_", "-")}="{_html.escape(str(v), quote=True)}"' for k, v in a.items() if v is not None)

    def muster(self, name: str) -> str:
        """Schraffuren (angelehnt an DIN 1356-1; ohne Anspruch auf Normtreue)."""
        if name not in self._muster:
            self._muster.add(name)
            m = {
                "holz": '<pattern id="m-holz" patternUnits="userSpaceOnUse" width="2" height="2" patternTransform="rotate(45)">'
                        '<rect width="2" height="2" fill="#f3e3c7"/><line x1="0" y1="0" x2="0" y2="2" stroke="#8d6e63" stroke-width="0.25"/></pattern>',
                "daemmung": '<pattern id="m-daemmung" patternUnits="userSpaceOnUse" width="3" height="3">'
                            '<rect width="3" height="3" fill="#fdf6d8"/><path d="M0,1.5 L0.75,0.3 L1.5,1.5 L2.25,2.7 L3,1.5" fill="none" stroke="#b08900" stroke-width="0.2"/></pattern>',
                "gips": '<pattern id="m-gips" patternUnits="userSpaceOnUse" width="1.5" height="1.5">'
                        '<rect width="1.5" height="1.5" fill="#eeeeee"/><circle cx="0.75" cy="0.75" r="0.18" fill="#777777"/></pattern>',
                "holzwerkstoff": '<pattern id="m-holzwerkstoff" patternUnits="userSpaceOnUse" width="2" height="2" patternTransform="rotate(-45)">'
                                 '<rect width="2" height="2" fill="#e8d2a6"/><line x1="0" y1="0" x2="0" y2="2" stroke="#8d6e63" stroke-width="0.25"/></pattern>',
                "strasse": '<pattern id="m-strasse" patternUnits="userSpaceOnUse" width="3" height="3" patternTransform="rotate(45)">'
                           '<rect width="3" height="3" fill="#ececec"/><line x1="0" y1="0" x2="0" y2="3" stroke="#bdbdbd" stroke-width="0.3"/></pattern>',
            }[name]
            self.defs.append(m)
        return f"url(#m-{name})"

    def polygon(self, coords, fill="none", stroke=FARBE["tinte"], lw=0.35, titel: str | None = None, **extra) -> None:
        t = f"<title>{_html.escape(titel)}</title>" if titel else ""
        self.teile.append(f'<polygon points="{self._pts(coords)}" {self._attr(fill=fill, stroke=stroke, stroke_width=lw, **extra)}>{t}</polygon>')

    def rechteck(self, x0, y0, x1, y1, **kw) -> None:
        self.polygon([(x0, y0), (x1, y0), (x1, y1), (x0, y1)], **kw)

    def linie(self, a, b, stroke=FARBE["tinte"], lw=0.35, **extra) -> None:
        (x1, y1), (x2, y2) = self.p(*a), self.p(*b)
        self.teile.append(f'<line x1="{_f(x1)}" y1="{_f(y1)}" x2="{_f(x2)}" y2="{_f(y2)}" {self._attr(stroke=stroke, stroke_width=lw, **extra)}/>')

    def polylinie(self, coords, stroke=FARBE["tinte"], lw=0.35, **extra) -> None:
        self.teile.append(f'<polyline points="{self._pts(coords)}" {self._attr(fill="none", stroke=stroke, stroke_width=lw, **extra)}/>')

    def text_papier(self, x_mm, y_mm, s, groesse=2.5, anker="start", fett=False, farbe=FARBE["tinte"], drehung=0.0) -> None:
        tr = f' transform="rotate({_f(drehung)} {_f(x_mm)} {_f(y_mm)})"' if drehung else ""
        w = ' font-weight="bold"' if fett else ""
        self.teile.append(f'<text x="{_f(x_mm)}" y="{_f(y_mm)}" font-size="{_f(groesse)}" text-anchor="{anker}" fill="{farbe}"{w}{tr}>{_html.escape(s)}</text>')

    def text(self, pos, s, groesse=2.5, anker="middle", **kw) -> None:
        x, y = self.p(*pos)
        self.text_papier(x, y, s, groesse, anker, **kw)

    def bemassung(self, a, b, abstand_mm: float = 6.0, text: str | None = None, groesse=2.5, stellen: int = 2,
                  einheit_faktor: float = 1.0) -> None:
        """Maßlinie parallel zu a–b, um `abstand_mm` (Papier) nach links der Richtung a→b versetzt.
        Text: Länge in Modelleinheiten·einheit_faktor, `stellen` Dezimalstellen, Komma."""
        (xa, ya), (xb, yb) = self.p(*a), self.p(*b)
        dx, dy = xb - xa, yb - ya
        L = math.hypot(dx, dy)
        if L < 1e-9:
            return
        ux, uy = dx / L, dy / L
        nx, ny = uy, -ux                                       # links der Richtung (Papier, y nach unten)
        ax, ay, bx, by = xa + nx * abstand_mm, ya + ny * abstand_mm, xb + nx * abstand_mm, yb + ny * abstand_mm
        s = self.teile.append
        vz = 1 if abstand_mm >= 0 else -1
        for (px, py), (qx, qy) in (((xa, ya), (ax, ay)), ((xb, yb), (bx, by))):
            s(f'<line x1="{_f(px + nx * vz * 1.0)}" y1="{_f(py + ny * vz * 1.0)}" x2="{_f(qx + nx * vz * 1.5)}" y2="{_f(qy + ny * vz * 1.5)}" stroke="{FARBE["tinte"]}" stroke-width="0.18"/>')
        s(f'<line x1="{_f(ax - ux * 1.5)}" y1="{_f(ay - uy * 1.5)}" x2="{_f(bx + ux * 1.5)}" y2="{_f(by + uy * 1.5)}" stroke="{FARBE["tinte"]}" stroke-width="0.25"/>')
        for qx, qy in ((ax, ay), (bx, by)):                     # Schrägstrich 45°
            tx, ty = (ux + nx) * 1.1, (uy + ny) * 1.1
            s(f'<line x1="{_f(qx - tx)}" y1="{_f(qy - ty)}" x2="{_f(qx + tx)}" y2="{_f(qy + ty)}" stroke="{FARBE["tinte"]}" stroke-width="0.5"/>')
        if text is None:
            laenge = math.hypot(b[0] - a[0], b[1] - a[1]) * einheit_faktor
            text = zahl_de(Rundung("dezimalstellen", stellen).runde(laenge))
        winkel = math.degrees(math.atan2(dy, dx))
        if winkel > 90 or winkel <= -90:                        # lesbar von unten bzw. rechts
            winkel -= 180 if winkel > 90 else -180
        if text == "":
            return
        mx, my = (ax + bx) / 2, (ay + by) / 2
        off = 0.8
        rx, ry = math.sin(math.radians(winkel)) * off, -math.cos(math.radians(winkel)) * off
        self.text_papier(mx + rx, my + ry, text, groesse, "middle", drehung=winkel)

    def massstabsleiste(self, x_mm, y_mm, laenge_modell: float, teile: int = 2, einheit: str = "m") -> None:
        seg = laenge_modell / teile * self.k
        for i in range(teile):
            f = FARBE["tinte"] if i % 2 == 0 else "#ffffff"
            self.teiles_rect(x_mm + i * seg, y_mm, seg, 1.5, f)
        for i in range(teile + 1):
            t = zahl_roh(laenge_modell / teile * i) + (f" {einheit}" if i == teile else "")
            self.text_papier(x_mm + i * seg, y_mm + 4.5, t, 2.2, "middle")
        self.text_papier(x_mm + teile * seg + 8, y_mm + 1.6, f"M 1:{zahl_roh(self.massstab)}", 2.5, "start", fett=True)

    def teiles_rect(self, x, y, w, h, fill) -> None:
        self.teile.append(f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(w)}" height="{_f(h)}" fill="{fill}" stroke="{FARBE["tinte"]}" stroke-width="0.25"/>')

    def nordpfeil(self, x_mm, y_mm, drehung_grad: float = 0.0, r: float = 5.0) -> None:
        self.teile.append(f'<g transform="rotate({_f(-drehung_grad)} {_f(x_mm)} {_f(y_mm)})">'
                          f'<circle cx="{_f(x_mm)}" cy="{_f(y_mm)}" r="{_f(r)}" fill="none" stroke="{FARBE["tinte"]}" stroke-width="0.25"/>'
                          f'<polygon points="{_f(x_mm)},{_f(y_mm - r)} {_f(x_mm + r * 0.35)},{_f(y_mm + r * 0.6)} {_f(x_mm)},{_f(y_mm + r * 0.3)}" fill="{FARBE["tinte"]}"/>'
                          f'<polygon points="{_f(x_mm)},{_f(y_mm - r)} {_f(x_mm - r * 0.35)},{_f(y_mm + r * 0.6)} {_f(x_mm)},{_f(y_mm + r * 0.3)}" fill="#ffffff" stroke="{FARBE["tinte"]}" stroke-width="0.25"/>'
                          f'<text x="{_f(x_mm)}" y="{_f(y_mm - r - 1.2)}" font-size="3.5" text-anchor="middle" font-weight="bold">N</text></g>')

    def legende(self, x_mm, y_mm, eintraege: Sequence[tuple[dict, str]], spalten: int = 1, spaltenbreite: float = 60.0) -> float:
        """eintraege: [(stil, text)], stil = dict(fill=…, stroke=…, linie=True). Rückgabe: Höhe in mm."""
        zeilen = math.ceil(len(eintraege) / spalten)
        for i, (stil, txt) in enumerate(eintraege):
            sx, sy = x_mm + (i // zeilen) * spaltenbreite, y_mm + (i % zeilen) * 5.0
            if stil.get("linie"):
                self.teile.append(f'<line x1="{_f(sx)}" y1="{_f(sy + 1.5)}" x2="{_f(sx + 6)}" y2="{_f(sy + 1.5)}" stroke="{stil.get("stroke", FARBE["tinte"])}" '
                                  f'stroke-width="{stil.get("lw", 0.5)}"' + (f' stroke-dasharray="{stil["dash"]}"' if stil.get("dash") else "") + "/>")
            else:
                self.teile.append(f'<rect x="{_f(sx)}" y="{_f(sy)}" width="6" height="3" fill="{stil.get("fill", "none")}" '
                                  f'fill-opacity="{stil.get("opacity", 1)}" stroke="{stil.get("stroke", FARBE["tinte"])}" stroke-width="0.25"/>')
            self.text_papier(sx + 8, sy + 2.6, txt, 2.5)
        return zeilen * 5.0

    def schriftfeld(self, zeilen: Sequence[str], breite: float = 70.0) -> None:
        """Einfaches Schriftfeld unten rechts (angelehnt an DIN EN ISO 7200)."""
        h = 4.5 * len(zeilen) + 2
        x, y = self.b - self.rand - breite, self.h - 4 - h
        self.teile.append(f'<rect x="{_f(x)}" y="{_f(y)}" width="{_f(breite)}" height="{_f(h)}" fill="#ffffff" stroke="{FARBE["tinte"]}" stroke-width="0.5"/>')
        for i, z in enumerate(zeilen):
            self.text_papier(x + 2, y + 4.5 + i * 4.5, z, 3.0 if i == 0 else 2.5, fett=(i == 0))

    def svg(self) -> str:
        kopf = (f'<svg xmlns="http://www.w3.org/2000/svg" width="{_f(self.b)}mm" height="{_f(self.h)}mm" '
                f'viewBox="0 0 {_f(self.b)} {_f(self.h)}" font-family="DejaVu Sans, Arial, sans-serif" role="img"'
                + (f' aria-label="{_html.escape(self.titel, quote=True)}"' if self.titel else "") + ">")
        t = [kopf]
        if self.titel:
            t.append(f"<title>{_html.escape(self.titel)}</title>")
        t.append(f'<rect width="{_f(self.b)}" height="{_f(self.h)}" fill="#ffffff"/>')
        if self.defs:
            t.append("<defs>" + "".join(self.defs) + "</defs>")
        t += self.teile
        t.append("</svg>")
        return "\n".join(t) + "\n"


# --- Diagramme --------------------------------------------------------------

def _mpl_svg(fig) -> str:
    import matplotlib.pyplot as plt
    buf = io.StringIO()
    fig.savefig(buf, format="svg", metadata={"Date": None, "Creator": None}, bbox_inches="tight")
    plt.close(fig)
    s = buf.getvalue()
    return re.sub(r"<!-- Created with matplotlib.*?-->\s*", "", s)


def _mpl_vorbereiten():
    mpl = _mpl()
    mpl.use("Agg", force=True)
    import matplotlib.pyplot as plt
    mpl.rcParams.update({"svg.hashsalt": "nachweis", "svg.fonttype": "none", "font.family": "DejaVu Sans",
                         "font.size": 9, "axes.edgecolor": FARBE["achse"], "axes.labelcolor": FARBE["tinte2"],
                         "xtick.color": FARBE["tinte2"], "ytick.color": FARBE["tinte2"], "axes.grid": True,
                         "grid.color": FARBE["gitter"], "grid.linewidth": 0.6, "axes.spines.top": False,
                         "axes.spines.right": False, "path.simplify": False, "figure.dpi": 100})
    return plt


def _de_achsen(ax, y: bool = False) -> None:
    """Achsbeschriftung mit Dezimalkomma (DIN 1333 / ISO 80000-1)."""
    from matplotlib.ticker import FuncFormatter

    def fmt(v, _p):
        return zahl_de(int(round(v))) if abs(v - round(v)) < 1e-9 else zahl_de(Decimal(repr(round(float(v), 10))).normalize())
    ax.xaxis.set_major_formatter(FuncFormatter(fmt))
    if y:
        ax.yaxis.set_major_formatter(FuncFormatter(fmt))


def diagramm_ist_grenzwert(zeilen: Sequence[dict], einheit: str, titel: str) -> str:
    """Ist-Wert gegen Grenzwert je Zeile: dict(label, ist, grenz, vergleich, U=None).
    Balken = Ist (grün erfüllt / rot nicht erfüllt), senkrechter Strich = Grenzwert,
    Fehlerbalken = erweiterte Unsicherheit U. Beschriftung direkt am Balken."""
    if _mpl():
        plt = _mpl_vorbereiten()
        n = len(zeilen)
        fig, ax = plt.subplots(figsize=(6.4, 0.55 * n + 1.2))
        for i, z in enumerate(zeilen):
            ok = _vergleiche(z["ist"], z["grenz"], z["vergleich"], z.get("tol", 0.0))
            f = FARBE["gut"] if ok else FARBE["krit"]
            y = n - 1 - i
            ax.barh(y, z["ist"], height=0.5, color=f, alpha=0.85, zorder=2)
            if z.get("U"):
                ax.errorbar(z["ist"], y, xerr=z["U"], fmt="none", ecolor=FARBE["tinte"], elinewidth=1, capsize=3, zorder=3)
            ax.plot([z["grenz"], z["grenz"]], [y - 0.38, y + 0.38], color=FARBE["tinte"], lw=2, zorder=4)
            ax.annotate(f"{z['vergleich']} {zahl_de(Rundung('signifikant', 3).runde(z['grenz']))}", (z["grenz"], y + 0.38),
                        xytext=(3, 1), textcoords="offset points", fontsize=8, color=FARBE["tinte"])
            ax.annotate(f"{zahl_de(Rundung('signifikant', 3).runde(z['ist']))} ({'erfüllt' if ok else 'nicht erfüllt'})",
                        (0, y), xytext=(4, -3), textcoords="offset points", fontsize=8, color="#ffffff" if z["ist"] > 0.25 * max(zz["grenz"] for zz in zeilen) else FARBE["tinte"])
        ax.set_yticks(range(n))
        ax.set_yticklabels([z["label"] for z in reversed(zeilen)])
        ax.set_xlabel(einheit)
        ax.set_xlim(0, max(max(z["ist"] + (z.get("U") or 0) for z in zeilen), max(z["grenz"] for z in zeilen)) * 1.18)
        ax.set_title(titel, fontsize=10, loc="left", color=FARBE["tinte"])
        ax.grid(axis="y", visible=False)
        _de_achsen(ax)
        return _mpl_svg(fig)
    return _svg_balken_fallback(zeilen, einheit, titel)


def _svg_balken_fallback(zeilen, einheit, titel) -> str:
    B, zh, links = 160.0, 9.0, 55.0
    H = 18 + zh * len(zeilen) + 12
    xmax = max(max(z["ist"] + (z.get("U") or 0) for z in zeilen), max(z["grenz"] for z in zeilen)) * 1.18
    sx = (B - links - 5) / xmax
    t = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{_f(B)}mm" height="{_f(H)}mm" viewBox="0 0 {_f(B)} {_f(H)}" font-family="DejaVu Sans, Arial, sans-serif" font-size="3">',
         f"<title>{_html.escape(titel)}</title>", f'<rect width="{_f(B)}" height="{_f(H)}" fill="#ffffff"/>',
         f'<text x="2" y="6" font-size="3.5">{_html.escape(titel)}</text>']
    for i, z in enumerate(zeilen):
        y = 12 + i * zh
        ok = _vergleiche(z["ist"], z["grenz"], z["vergleich"], z.get("tol", 0.0))
        t.append(f'<text x="{_f(links - 2)}" y="{_f(y + 4)}" text-anchor="end">{_html.escape(z["label"])}</text>')
        t.append(f'<rect x="{_f(links)}" y="{_f(y + 1)}" width="{_f(z["ist"] * sx)}" height="4.5" fill="{FARBE["gut"] if ok else FARBE["krit"]}"><title>{_html.escape(zahl_roh(z["ist"]))}</title></rect>')
        gx = links + z["grenz"] * sx
        t.append(f'<line x1="{_f(gx)}" y1="{_f(y)}" x2="{_f(gx)}" y2="{_f(y + 6.5)}" stroke="{FARBE["tinte"]}" stroke-width="0.6"/>')
        t.append(f'<text x="{_f(gx + 1)}" y="{_f(y + 1)}" font-size="2.5">{z["vergleich"]} {zahl_de(Rundung("signifikant", 3).runde(z["grenz"]))}</text>')
    t.append(f'<text x="{_f(B - 5)}" y="{_f(H - 3)}" text-anchor="end">{_html.escape(einheit)}</text></svg>')
    return "\n".join(t) + "\n"


def diagramm_punkte(punkte: Sequence[dict], x_label: str, y_label: str, titel: str,
                    bereich: Sequence[tuple[float, float]] | None = None,
                    linien: Sequence[dict] = (), hervorgehoben: dict | None = None,
                    beschriftungen: Sequence[tuple[float, float, str]] = ()) -> str:
    """Streudiagramm. punkte: dict(x, y, gruppe); bereich: Polygon des zulässigen
    Bereichs; linien: dict(punkte=[(x,y),…], label, stil='--'); hervorgehoben:
    dict(x, y, label). Gruppen erhalten Kategorienfarben in fester Reihenfolge."""
    gruppen = sorted({p["gruppe"] for p in punkte}, key=lambda g: (str(type(g)), g))
    if _mpl():
        plt = _mpl_vorbereiten()
        from matplotlib.patches import Polygon as MPoly
        fig, ax = plt.subplots(figsize=(6.4, 4.4))
        if bereich:
            ax.add_patch(MPoly(list(bereich), closed=True, facecolor="#e8f4e8", edgecolor=FARBE["gut"], lw=1, zorder=0,
                               label="zulässiger Bereich"))
        for li in linien:
            xs, ys = zip(*li["punkte"])
            ax.plot(xs, ys, li.get("stil", "--"), color=li.get("farbe", FARBE["tinte2"]), lw=1, label=li.get("label"), zorder=1)
        palette = ["#2a78d6", "#eb6834", "#1baf7a", "#eda100", "#e87ba4", "#008300", "#4a3aa7", "#e34948"]
        for i, g in enumerate(gruppen):
            pp = [p for p in punkte if p["gruppe"] == g]
            ax.scatter([p["x"] for p in pp], [p["y"] for p in pp], s=16, color=palette[i % len(palette)], label=str(g),
                       zorder=3, edgecolors="#ffffff", linewidths=0.5)
        for bx, by, bt in beschriftungen:
            ax.annotate(bt, (bx, by), ha="center", va="bottom", fontsize=7.5, color=FARBE["tinte2"])
        if hervorgehoben:
            ax.scatter([hervorgehoben["x"]], [hervorgehoben["y"]], s=110, facecolors="none", edgecolors=FARBE["tinte"], lw=1.6, zorder=4,
                       label=hervorgehoben.get("label"))
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(titel, fontsize=10, loc="left", color=FARBE["tinte"])
        ax.legend(fontsize=7, loc="upper right", frameon=False, ncol=2)
        _de_achsen(ax, y=True)
        return _mpl_svg(fig)
    # Fallback: reines SVG
    xs = [p["x"] for p in punkte] + [x for x, _ in (bereich or [])]
    ys = [p["y"] for p in punkte] + [y for _, y in (bereich or [])]
    x0, x1, y0, y1 = min(xs), max(xs), min(ys), max(ys)
    z = SvgZeichnung((x0, y0, x1, y1), massstab=1.0, modell_m=1.0 / max(x1 - x0, y1 - y0) * 0.12, titel=titel)
    if bereich:
        z.polygon(list(bereich), fill="#e8f4e8", stroke=FARBE["gut"], lw=0.3)
    for p in punkte:
        cx, cy = z.p(p["x"], p["y"])
        z.teile.append(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="0.8" fill="{FARBE["s1"]}"/>')
    if hervorgehoben:
        cx, cy = z.p(hervorgehoben["x"], hervorgehoben["y"])
        z.teile.append(f'<circle cx="{_f(cx)}" cy="{_f(cy)}" r="2" fill="none" stroke="{FARBE["tinte"]}" stroke-width="0.4"/>')
    z.text_papier(2, 5, titel, 3)
    return z.svg()


def diagramm_balken(werte: Sequence[dict], einheit: str, titel: str) -> str:
    """Einfarbiges waagerechtes Balkendiagramm: dict(label, wert, U=None). Wert direkt am Balken."""
    if _mpl():
        plt = _mpl_vorbereiten()
        n = len(werte)
        fig, ax = plt.subplots(figsize=(6.4, 0.42 * n + 1.1))
        vmax = max(w["wert"] + (w.get("U") or 0) for w in werte)
        for i, w in enumerate(werte):
            y = n - 1 - i
            ax.barh(y, w["wert"], height=0.55, color=FARBE["s1"], zorder=2)
            if w.get("U"):
                ax.errorbar(w["wert"], y, xerr=w["U"], fmt="none", ecolor=FARBE["tinte"], elinewidth=1, capsize=3, zorder=3)
            ax.annotate(zahl_de(Rundung("signifikant", 3).runde(w["wert"])), (w["wert"] + (w.get("U") or 0), y),
                        xytext=(4, -3), textcoords="offset points", fontsize=8, color=FARBE["tinte"])
        ax.set_yticks(range(n))
        ax.set_yticklabels([w["label"] for w in reversed(werte)])
        ax.set_xlim(0, vmax * 1.2)
        ax.set_xlabel(einheit)
        ax.set_title(titel, fontsize=10, loc="left", color=FARBE["tinte"])
        ax.grid(axis="y", visible=False)
        _de_achsen(ax)
        return _mpl_svg(fig)
    return _svg_balken_fallback([{"label": w["label"], "ist": w["wert"], "grenz": w["wert"], "vergleich": "="} for w in werte], einheit, titel)


def balken_anteil_svg(teile: Sequence[tuple[str, int, str]], titel: str, breite_mm: float = 150.0) -> str:
    """Gestapelter Anteilsbalken in reinem SVG, z. B. [("bestanden", 175, FARBE['gut']), ("fehlerhaft", 1, FARBE['krit'])].
    Klein und deterministisch; für viele gleichartige Nachweise (IDS) gedacht."""
    gesamt = sum(n for _, n, _ in teile)
    H = 22.0
    t = [f'<svg xmlns="http://www.w3.org/2000/svg" width="{_f(breite_mm)}mm" height="{_f(H)}mm" viewBox="0 0 {_f(breite_mm)} {_f(H)}" '
         f'font-family="DejaVu Sans, Arial, sans-serif" role="img" aria-label="{_html.escape(titel, quote=True)}">',
         f"<title>{_html.escape(titel)}</title>", f'<rect width="{_f(breite_mm)}" height="{_f(H)}" fill="#ffffff"/>',
         f'<text x="2" y="5" font-size="3.2" fill="{FARBE["tinte"]}">{_html.escape(titel)}</text>']
    x, w = 2.0, breite_mm - 4.0
    if gesamt == 0:
        t.append(f'<rect x="2" y="8" width="{_f(w)}" height="6" fill="#ffffff" stroke="{FARBE["achse"]}" stroke-width="0.3"/>')
        t.append(f'<text x="{_f(breite_mm / 2)}" y="12.3" font-size="3" text-anchor="middle" fill="{FARBE["tinte2"]}">keine anwendbaren Elemente</text>')
    for i, (name, n, farbe) in enumerate(teile):
        if gesamt == 0 or n == 0:
            continue
        b = w * n / gesamt
        t.append(f'<rect x="{_f(x)}" y="8" width="{_f(b)}" height="6" fill="{farbe}"><title>{_html.escape(name)}: {n}</title></rect>')
        x += b
    leg = "   ".join(f"{name}: {n}" for name, n, _ in teile)
    t.append(f'<text x="2" y="19.5" font-size="3" fill="{FARBE["tinte2"]}">{_html.escape(leg)} (von {gesamt} anwendbaren Elementen)</text>')
    t.append("</svg>")
    return "\n".join(t) + "\n"


# --- Fachgrafiken -------------------------------------------------------------

def lageplan_svg(grundstueck, gebaeude, abstandsflaechen: Sequence[dict], massstab: int = 200,
                 strasse=None, bemassungen: Sequence[dict] = (), titel: str = "Lageplan", schriftfeld: Sequence[str] = (),
                 nord_grad: float = 0.0, puffer: float = 4.0) -> str:
    """Lageplan mit Abstandsflächen (shapely-Polygone oder Koordinatenlisten).

    abstandsflaechen: dict(polygon, ok: bool, label) → grün (zulässig) / rot (unzulässig)
    bemassungen: dict(a=(x,y), b=(x,y), abstand_mm, text=None)"""
    from shapely.geometry import Polygon as SPoly
    from shapely.ops import unary_union

    def coords(g):
        return list(g.exterior.coords) if hasattr(g, "exterior") else list(g)

    alle = [SPoly(coords(grundstueck)), SPoly(coords(gebaeude))] + [SPoly(coords(a["polygon"])) for a in abstandsflaechen]
    if strasse is not None:
        alle.append(SPoly(coords(strasse)))
    minx, miny, maxx, maxy = unary_union(alle).buffer(puffer).bounds
    leg_h = 40.0
    z = SvgZeichnung((minx, miny, maxx, maxy), massstab, 1.0, rand_mm=10.0, unten_mm=leg_h, titel=titel)
    if strasse is not None:
        z.polygon(coords(strasse), fill=z.muster("strasse"), stroke=FARBE["leise"], lw=0.25, stroke_dasharray="2 1.2",
                  titel="öffentliche Verkehrsfläche (bis Mitte anrechenbar)")
    z.polygon(coords(grundstueck), fill="none", stroke=FARBE["tinte"], lw=0.7, titel="Grundstücksgrenze")
    for a in abstandsflaechen:
        f = FARBE["gut"] if a["ok"] else FARBE["krit"]
        z.polygon(coords(a["polygon"]), fill=f, fill_opacity="0.28", stroke=f, lw=0.35, titel=a.get("label"))
    z.polygon(coords(gebaeude), fill="#8d6e63", stroke="#3e2723", lw=0.5, titel="geplantes Gebäude")
    for bm in bemassungen:
        z.bemassung(bm["a"], bm["b"], bm.get("abstand_mm", 5.0), bm.get("text"))
    # Nordpfeil und Maßstabsleiste oben rechts/unten
    z.nordpfeil(z.b - 12, 16, nord_grad)
    y0 = z.h_zeichnung + 2
    z.massstabsleiste(z.rand, y0, 10.0, 2)
    z.legende(z.rand, y0 + 9, [({"fill": "none", "stroke": FARBE["tinte"]}, "Grundstücksgrenze"),
                                ({"fill": "#8d6e63", "stroke": "#3e2723"}, "geplantes Gebäude"),
                                ({"fill": FARBE["gut"], "opacity": 0.28, "stroke": FARBE["gut"]}, "Abstandsfläche zulässig"),
                                ({"fill": FARBE["krit"], "opacity": 0.28, "stroke": FARBE["krit"]}, "Abstandsfläche außerhalb"),
                                ({"fill": "url(#m-strasse)", "stroke": FARBE["leise"]}, "öffentliche Verkehrsfläche")],
              spalten=1)
    if schriftfeld:
        z.schriftfeld(list(schriftfeld), breite=66.0)
    return z.svg()


def schnitt_svg(schichten: Sequence[dict], breite_mm: float, massstab: int = 5, titel: str = "Schnitt",
                einlagen: Sequence[dict] = (), innen: str = "innen", aussen: str = "außen",
                schriftfeld: Sequence[str] = ()) -> str:
    """Horizontalschnitt eines Aufbaus. schichten (innen → außen): dict(name, dicke_mm, muster, text);
    einlagen: dict(schicht_index, x0_mm, breite_mm, muster, name) – z. B. Ständer im Gefach.
    Darstellung: innen unten, außen oben, Maßkette rechts, Beschriftung links."""
    gesamt = sum(s["dicke_mm"] for s in schichten)
    n = len(schichten)
    leg_h = 5.0 * (n + 1) + 22
    z = SvgZeichnung((-0.0, 0.0, breite_mm, gesamt), massstab, 0.001, rand_mm=14.0, unten_mm=leg_h, titel=titel)
    z.b += 38                                                  # Platz für die Maßkette rechts
    y = 0.0
    lagen = []
    for s in schichten:
        y1 = y + s["dicke_mm"]
        fill = z.muster(s["muster"]) if s.get("muster") else "#ffffff"
        if s["dicke_mm"] * z.k < 0.6:
            z.linie((0, y1), (breite_mm, y1), stroke="#1565c0", lw=0.35, stroke_dasharray="1.5 0.8")
        else:
            z.rechteck(0, y, breite_mm, y1, fill=fill, stroke=FARBE["tinte"], lw=0.35, titel=s["name"])
        lagen.append((y, y1))
        y = y1
    for e in einlagen:
        y0, y1 = lagen[e["schicht_index"]]
        z.rechteck(e["x0_mm"], y0, e["x0_mm"] + e["breite_mm"], y1, fill=z.muster(e.get("muster", "holz")), stroke=FARBE["tinte"], lw=0.5,
                   titel=e.get("name"))
        z.linie((e["x0_mm"], y0), (e["x0_mm"] + e["breite_mm"], y1), stroke=FARBE["tinte"], lw=0.18)
        z.linie((e["x0_mm"], y1), (e["x0_mm"] + e["breite_mm"], y0), stroke=FARBE["tinte"], lw=0.18)
    # Maßkette rechts (Schichtdicken), außen Gesamtmaß. Schmale Schichten (< 8 mm auf Papier):
    # Maßzahl waagerecht neben der Kette, gegen Überdeckung nach unten versetzt (von außen nach innen).
    xr = breite_mm
    xk, _ = z.p(xr, 0)
    klein = []
    for (y0, y1), s in zip(lagen, schichten):
        hp = (y1 - y0) * z.k
        if hp >= 8.0:
            z.bemassung((xr, y1), (xr, y0), 6.0, zahl_roh(s["dicke_mm"]), groesse=2.2)
        else:
            if hp >= 0.6:
                z.bemassung((xr, y1), (xr, y0), 6.0, "", groesse=2.2)
            klein.append(((y0 + y1) / 2, zahl_roh(s["dicke_mm"]) + (" (Folie)" if hp < 0.6 else "")))
    letzte = -1e9
    for ym_mod, txt in sorted(klein, key=lambda t: -t[0]):
        _, yp = z.p(0, ym_mod)
        yp = max(yp + 0.8, letzte + 2.9)
        z.text_papier(xk + 7.5, yp, txt, 2.2, "start")
        letzte = yp
    z.bemassung((xr, gesamt), (xr, 0), 22.0, zahl_roh(round(gesamt, 3)), groesse=2.5)
    for e in einlagen[:1]:
        z.bemassung((e["x0_mm"], 0), (e["x0_mm"] + e["breite_mm"], 0), -6.0, zahl_roh(e["breite_mm"]), groesse=2.2)
    z.bemassung((0, 0), (breite_mm, 0), -12.0, zahl_roh(breite_mm), groesse=2.5)
    xm, ym = z.p(breite_mm / 2, gesamt)
    z.text_papier(xm, ym - 2.0, aussen, 3.0, "middle")
    xm, ym = z.p(breite_mm / 2, 0)
    z.text_papier(xm, ym + 18.0, innen, 3.0, "middle")
    # Legende unten
    yl = ym + 23.0
    eintr = [({"fill": z.muster(s["muster"]) if s.get("muster") else "#ffffff"} if s["dicke_mm"] * z.k >= 0.6
              else {"linie": True, "stroke": "#1565c0", "dash": "1.5 0.8", "lw": 0.35}, f"{i + 1}  {s.get('text', s['name'])}")
             for i, s in enumerate(schichten)]
    eintr += [({"fill": z.muster(e.get("muster", "holz"))}, e.get("name", "Einlage")) for e in einlagen]
    z.legende(z.rand, yl, eintr)
    z.text_papier(z.b - 4, yl + 2.6, f"Maße in mm   M 1:{zahl_roh(massstab)}", 2.5, "end")
    # Nummern an den Schichten links, schmale Schichten versetzt
    letzte = -1e9
    for i, (y0, y1) in reversed(list(enumerate(lagen))):
        px, py = z.p(0, (y0 + y1) / 2)
        py = max(py + 0.9, letzte + 2.7)
        z.text_papier(px - 2, py, str(i + 1), 2.3, "end")
        letzte = py
    if schriftfeld:
        z.schriftfeld(list(schriftfeld), breite=64)
    return z.svg()


def treppenschnitt_svg(n_steigungen: int, s_mm: float, a_mm: float, massstab: int = 50,
                       titel: str = "Treppenschnitt", schriftfeld: Sequence[str] = ()) -> str:
    """Vertikalschnitt einer geraden einläufigen Treppe mit n Steigungen und n−1 Auftritten
    (Stufenprofil schematisch, Maße in mm)."""
    h = n_steigungen * s_mm
    L = (n_steigungen - 1) * a_mm
    z = SvgZeichnung((-400.0, -150.0, L + 600.0, h + 150.0), massstab, 0.001, rand_mm=16.0, unten_mm=36.0, titel=titel)
    pts = [(-400.0, 0.0), (0.0, 0.0)]
    x, y = 0.0, 0.0
    for i in range(n_steigungen):
        y += s_mm
        pts.append((x, y))
        if i < n_steigungen - 1:
            x += a_mm
            pts.append((x, y))
    pts.append((L + 600.0, h))
    z.polygon(pts + [(L + 600.0, h - 60.0), (L, h - 60.0), (0.0, -60.0), (-400.0, -60.0)], fill=z.muster("holz"),
              stroke=FARBE["tinte"], lw=0.5, titel="Stufenprofil (schematisch)")
    z.linie((-400.0, 0.0), (L + 600.0, 0.0), stroke=FARBE["leise"], lw=0.18, stroke_dasharray="3 1.5")
    z.linie((-400.0, h), (L + 600.0, h), stroke=FARBE["leise"], lw=0.18, stroke_dasharray="3 1.5")
    z.text((-380.0, 40.0), "OKFF unten ±0,00", 2.2, "start")
    z.text((L + 580.0, h + 40.0), f"OKFF oben +{zahl_de(Rundung('dezimalstellen', 2).runde(h / 1000))}", 2.2, "end")
    z.bemassung((L + 600.0, 0.0), (L + 600.0, h), -8.0,
                f"{n_steigungen} × {zahl_de(Rundung('dezimalstellen', 1).runde(s_mm))} = {zahl_roh(round(h, 3))}", groesse=2.2)
    z.bemassung((0.0, 0.0), (L, 0.0), -9.0, f"Lauflänge {n_steigungen - 1} × {zahl_roh(a_mm)} = {zahl_roh(round(L, 3))}", groesse=2.2)
    # eine Stufe herausgehoben: Maßlinien ohne Zahl, Maßzahlen daneben
    k = n_steigungen // 2
    x0, y0 = (k - 1) * a_mm, k * s_mm
    z.bemassung((x0, y0), (x0 + a_mm, y0), 2.5, "", groesse=2.0)
    z.bemassung((x0 + a_mm, y0), (x0 + a_mm, y0 + s_mm), -2.5, "", groesse=2.0)
    px, py = z.p(x0 + a_mm / 2, y0)
    z.text_papier(px - 1.0, py - 4.5, f"a = {zahl_roh(a_mm)}", 2.2, "end")
    px, py = z.p(x0 + a_mm, y0 + s_mm / 2)
    z.text_papier(px + 4.5, py + 0.8, f"s = {zahl_de(Rundung('dezimalstellen', 1).runde(s_mm))}", 2.2, "start")
    # Maßstabsleiste in m (Modell in mm: 1 m = 1000 Modelleinheiten)
    y_ml = z.h_zeichnung + 4
    seg = 1000.0 * z.k
    for i in range(2):
        z.teiles_rect(z.rand + i * seg, y_ml, seg, 1.5, FARBE["tinte"] if i % 2 == 0 else "#ffffff")
    for i, t in enumerate(("0", "1", "2 m")):
        z.text_papier(z.rand + i * seg, y_ml + 4.5, t, 2.2, "middle")
    z.text_papier(z.rand, y_ml + 11, f"M 1:{massstab}, Maße in mm", 2.5, "start", fett=True)
    if schriftfeld:
        z.schriftfeld(list(schriftfeld), breite=64)
    return z.svg()


def svg_ist_valide(svg: str) -> bool:
    """Wohlgeformtes XML mit SVG-Wurzelelement."""
    import xml.etree.ElementTree as ET
    try:
        wurzel = ET.fromstring(_svg_inline(svg))
    except ET.ParseError:
        return False
    return wurzel.tag == "{http://www.w3.org/2000/svg}svg"


# ===========================================================================
# 10. Schema-Prüfung
# ===========================================================================

def pruefe_schema(d: dict) -> None:
    """Validiert ein Nachweis- oder Heft-Dictionary gegen nachweis.schema.json (jsonschema)."""
    import jsonschema
    schema = json.loads(SCHEMA_DATEI.read_text(encoding="utf-8"))
    jsonschema.Draft202012Validator(schema).validate(d)


if __name__ == "__main__":  # kleine Selbstdemonstration
    n = Nachweis(
        id="DEMO-01", titel="Wärmedurchlasswiderstand einer Schicht",
        gegenstand=Gegenstand("Demo-Schicht"),
        regel=Regel("R = d/λ", "DIN EN ISO 6946:2018-03", "2018-03", "DEMO", "0.1", "6.7.1.1, Formel (3)", "[V]"),
        eingaben=[Groesse("Dicke", "d", 200, "mm", "Planung", 3.0),
                  Groesse("Wärmeleitfähigkeit", "lambda_D", 0.038, "W/(m·K)", "Herstellerangabe (Beispiel)", 0.001)],
        schritte=[Schritt("Wärmedurchlasswiderstand", Groesse("Wärmedurchlasswiderstand", "R", None, "m²·K/W"), "d/lambda_D")],
        ergebnis="R", grenzwert=Groesse("Mindestwert", "R_min", 4.0, "m²·K/W", "Beispiel"), vergleich="≥",
        ergebnis_rundung=Rundung("dezimalstellen", 2, quelle="DIN EN ISO 6946:2018-03, 6.6"))
    print(n.markdown())

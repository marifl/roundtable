#!/usr/bin/env python3
"""Kapitel 11 und 12: Erzeugung und Prüfung der Spezifikationsdateien.

Aufruf (aus arbeit/spezifikation/, mit ifcopenshell 0.8.5, ifctester 0.8.5, jsonschema, xmlschema, PyYAML):
  python pruefe_kap11_12.py erzeugen   # ids/*.ids und regelkatalog-11.yaml aus reifegrade.yaml erzeugen
  python pruefe_kap11_12.py pruefen    # Parsebarkeit, Schemata, Beispiele, Hashes, Referenzen, IDS, Monotonie
  python pruefe_kap11_12.py modelle    # IDS gegen B1, B14, B16 (unverändert und migriert) und synthetische Modelle
"""
import sys, re, json, glob, copy, uuid, hashlib, pathlib
import yaml, jsonschema, xmlschema
import ifcopenshell, ifcopenshell.api as api, ifcopenshell.util.element as ue, ifcopenshell.util.pset as P
from ifctester import ids
from ifctester.facet import Restriction

SPEZ = SP = pathlib.Path(__file__).resolve().parent
AUS = SPEZ.parent / "beispiele" / "ausgabe"
Y = yaml.safe_load(open(SPEZ / "reifegrade.yaml", encoding="utf-8"))

# ---------- typisierte Psets ----------
def pset(f, obj, name, props):
    """props: {Name: (IfcTyp, Wert)}; Typ-Objekte über HasPropertySets, Exemplare über IfcRelDefinesByProperties."""
    vals = [f.createIfcPropertySingleValue(k, None, f.create_entity(t, v), None) for k, (t, v) in props.items()]
    ps = f.createIfcPropertySet(ifcopenshell.guid.new(), None, name, None, vals)
    if obj.is_a("IfcTypeObject"):
        obj.HasPropertySets = list(obj.HasPropertySets or []) + [ps]
    else:
        f.createIfcRelDefinesByProperties(ifcopenshell.guid.new(), None, None, None, [obj], ps)
    return ps
def retype(f, obj_psets, psname, prop, typ):
    for ps in obj_psets:
        if ps.Name == psname:
            for p in ps.HasProperties:
                if p.Name == prop: p.NominalValue = f.create_entity(typ, p.NominalValue.wrappedValue)

# ---------- IDS-Erzeugung ----------
"""Erzeugt spezifikation/ids/<gruppe>-<P|R|A>.ids aus spezifikation/reifegrade.yaml und prüft sie."""

schema = ifcopenshell.ifcopenshell_wrapper.schema_by_name("IFC4X3_ADD2")
tmpl = P.get_template("IFC4X3")
XSD = xmlschema.XMLSchema(str(pathlib.Path(ids.__file__).parent/"ids.xsd"))
fehler = []

def val(d, base="string"):
    if "wert" in d: return str(d["wert"])
    if "enum" in d: return Restriction(options={"enumeration": [str(x) for x in d["enum"]]}, base="string")
    if "muster" in d: return Restriction(options={"pattern": d["muster"]}, base="string")
    opts = {}
    if "min" in d: opts["minInclusive"] = d["min"]
    if "max" in d: opts["maxInclusive"] = d["max"]
    if "min_excl" in d: opts["minExclusive"] = d["min_excl"]
    if opts: return Restriction(options=opts, base="double" if not d.get("typ","").endswith(("INTEGER","COUNTMEASURE")) else "integer")
    return None

def check_entity(name, pdt=None):
    names = name if isinstance(name, list) else [name]
    for n in names:
        try:
            decl = schema.declaration_by_name(n)
        except Exception:
            fehler.append(f"Klasse {n} fehlt"); continue
        if pdt:
            pdts = pdt if isinstance(pdt, list) else [pdt]
            attrs = {a.name(): a for a in decl.all_attributes()}
            if "PredefinedType" not in attrs: fehler.append(f"{n} ohne PredefinedType"); continue
            enum = attrs["PredefinedType"].type_of_attribute().declared_type().enumeration_items()
            for p_ in pdts:
                if p_ not in enum: fehler.append(f"{n}.{p_} kein Enum-Wert")

def check_prop(ps, name):
    if ps.startswith(("Pset_", "Qto_")):
        t = tmpl.get_by_name(ps)
        if not t: fehler.append(f"{ps} fehlt im Template"); return
        if name not in [p.Name for p in t.HasPropertyTemplates]: fehler.append(f"{ps}.{name} fehlt im Template")
    elif ps.startswith("HRB_"):
        if ps not in Y["hrb_psets"] or name not in [m["name"] for m in Y["hrb_psets"][ps]["merkmale"]]:
            fehler.append(f"{ps}.{name} nicht in hrb_psets definiert")
    else:
        fehler.append(f"Präfix unzulässig: {ps}")

def facet(fd, anforderung):
    (k, d), = fd.items()
    card = {} if not anforderung else {"cardinality": d.get("kardinalitaet", "required")}
    if k == "entitaet":
        check_entity(d["name"], d.get("vordefiniert"))
        n = d["name"]; n = Restriction(options={"enumeration": n}) if isinstance(n, list) else n
        p_ = d.get("vordefiniert"); p_ = Restriction(options={"enumeration": p_}) if isinstance(p_, list) else p_
        return ids.Entity(name=n, predefinedType=p_)
    if k == "merkmal":
        check_prop(d["pset"], d["name"])
        return ids.Property(propertySet=d["pset"], baseName=d["name"], dataType=d.get("typ"), value=val(d), **card)
    if k == "attribut":
        return ids.Attribute(name=d["name"], value=val(d), **card)
    if k == "klassifikation":
        return ids.Classification(system=d["system"], value=val(d), **card)
    if k == "material":
        return ids.Material(value=val(d) if d else None, **card)
    if k == "teil_von":
        check_entity(d["entitaet"])
        return ids.PartOf(name=d["entitaet"], relation=d["beziehung"], **card)
    raise ValueError(k)

def spec(s, verbot=False):
    mn = 0 if verbot else s.get("min_vorkommen", 0 if s.get("min_vorkommen") == 0 else 1)
    if verbot:
        sp = ids.Specification(name=f'{s["id"]} {s["titel"]}', ifcVersion=["IFC4X3_ADD2"], minOccurs=0, maxOccurs=0, identifier=s["id"])
    else:
        sp = ids.Specification(name=f'{s["id"]} {s["titel"]}', ifcVersion=["IFC4X3_ADD2"], minOccurs=mn, maxOccurs="unbounded", identifier=s["id"])
    sp.applicability = [facet(f, False) for f in s["anwendbarkeit"]]
    sp.requirements = [facet(f, True) for f in s.get("anforderungen", [])]
    return sp

def sammeln(g, lvl):
    stufe = g[lvl]; specs = []
    if stufe.get("erbt"): specs += sammeln(g, stufe["erbt"])[0]
    specs += stufe.get("pflichtmerkmale", [])
    return specs, stufe.get("verbote", []), stufe.get("lieferdaten", [])

def erzeugen_ids():
    erzeugt = []
    
    for gname, g in Y["bauteilgruppen"].items():
        for lvl in ("P", "R", "A"):
            if not g.get(lvl, {}).get("ids"): continue
            specs, verbote, liefer = sammeln(g, lvl)
            rg = Y["reifegrade"][lvl]
            I = ids.Ids(title=f"HRB Reifegrad {lvl} ({rg['name']}) – {g['titel']}",
                        copyright="Arbeit Holzrahmenbau, Kapitel 11", version=Y["meta"]["version"],
                        description=f"Pflichtmerkmale der Bauteilgruppe '{gname}' im Reifegrad {lvl} nach spezifikation/reifegrade.yaml (LOIN nach DIN EN ISO 7817-1:2024-11). Merkmale kumulativ (R erbt P, A erbt R); Granularitätsverbote nur für diesen Reifegrad.",
                        author="reifegrade@example.org", date=Y["meta"]["stand"], purpose=rg["zweck"], milestone=rg["meilenstein"])
            for s in specs: I.specifications.append(spec(s))
            for s in verbote: I.specifications.append(spec(s, verbot=True))
            if liefer:
                base = g["anwendbarkeit_gruppe"]
                s = {"id": f"{gname.upper()[:3]}-{lvl}-L01", "titel": "Lieferdaten (optional bis Gate G7; Wert geprüft, wenn vorhanden)",
                     "anwendbarkeit": base, "anforderungen": [{"merkmal": dict(l, kardinalitaet="optional")} for l in liefer], "min_vorkommen": 0}
                I.specifications.append(spec(s))
            out = SPEZ/g[lvl]["ids"]; out.parent.mkdir(exist_ok=True)
            I.to_xml(str(out))
            XSD.validate(str(out))            # wirft bei Schemafehler
            again = ids.open(str(out))        # ifctester parst die Datei
            erzeugt.append((out.name, len(again.specifications)))
    
    for n, k in erzeugt: print(f"{n}: {k} Spezifikationen, XSD gültig, ifctester parst")
    print("Schema-/Template-Fehler:", fehler or "keine")
    return not fehler

# ---------- Regelkatalog 11 ----------
def erzeugen_rk11():
    regeln = []
    anf = {"P": ["ANF-11-02", "ANF-11-04"], "R": ["ANF-11-02", "ANF-11-03", "ANF-11-04"], "A": ["ANF-11-02", "ANF-11-03", "ANF-11-09"]}
    bsp = {"wandelement": ["B1"], "belag": ["B14", "B16"], "sanitaer": ["keins"], "treppe": ["B5"]}
    for g, d in Y["bauteilgruppen"].items():
        for lvl in "PRA":
            s = d.get(lvl, {})
            if not s.get("ids"): continue
            ids_ = []
            def coll(l):
                st = d[l]; out = []
                if st.get("erbt"): out += coll(st["erbt"])
                return out + [x["id"] for x in st.get("pflichtmerkmale", [])]
            pflicht = coll(lvl); verb = [x["id"] for x in s.get("verbote", [])]
            regeln.append({
                "id": f"IDS.RG-{g}-{lvl}", "version": "0.1.0",
                "titel": f"Reifegrad {lvl} ({Y['reifegrade'][lvl]['name']}): {d['titel']}",
                "klasse": "R2", "haerte": "hart",
                "quelle": {"art": "M", "werk": f"spezifikation/{s['ids']}", "fundstelle": ", ".join(pflicht + verb),
                           "fassung": "IDS 1.0; reifegrade.yaml 0.1.0 (2026-09-27)", "status": "V", "bib": ["bsi2024ids", "dineniso7817-1"]},
                "profil": {"name": "HRB-IDS-Reifegrad", "version": "0.1.0"}, "schicht": "S5",
                "geltung": {"gebaeudetypen": ["alle"], "zeit": {"von": None, "bis": None, "stichtag": "pruefzeitpunkt"}},
                "eingaben": [], 
                "pruefung": {"typ": "ids", "formel": f"alle Pflichtspezifikationen ({len(pflicht)}) bestanden und alle Verbote ({len(verb)}) ohne Treffer; Merkmale kumulativ aus {'/'.join(['P','R','A'][:'PRA'.index(lvl)+1])}", "ids": f"spezifikation/{s['ids']}"},
                "grenzwerte": [], "meldung": "{spezifikation}: {anzahl_fehler} von {anwendbar} Elementen verfehlen die Anforderung (Reifegrad " + lvl + " nicht erreicht).",
                "alternative": [{"art": "A3_variante", "beschreibung": "fehlende Merkmale nachtragen oder Objekt im niedrigeren Reifegrad führen"}],
                "status": "V", "beispiel": bsp[g], "kapitel": "11.5", "anforderungen": anf[lvl],
                "hinweis": "Zahlenwerte der Facetten in SI-Einheiten; Befundzuordnung über das ID-Präfix im Spezifikationsnamen (ANF-09-04)."})
    extra = [
     {"id": "M.Reifegrad.Gate", "version": "0.1.0", "titel": "Mindestreifegrad je Bauteilgruppe an einem Freigabe-Gate",
      "klasse": "R3", "haerte": "hart",
      "quelle": {"art": "M", "werk": "spezifikation/reifegrade.yaml#phasen_matrix", "fundstelle": "phasen_matrix, gates", "fassung": "0.1.0 (2026-09-27)", "status": "U", "bib": ["dineniso7817-1"], "recherche": ["10"]},
      "profil": {"name": "HRB-IDS-Reifegrad", "version": "0.1.0"}, "schicht": "S5",
      "geltung": {"gebaeudetypen": ["alle"], "zeit": {"von": None, "bis": None, "stichtag": "pruefzeitpunkt"}},
      "eingaben": [{"name": "reifegradvektor", "einheit": "-", "quelle": "IDS-Ergebnisse je Gruppe"}, {"name": "gate", "einheit": "-", "quelle": "Prozess"}],
      "pruefung": {"typ": "freigabe", "formel": "Gate g öffnet ⇔ ∀ Gruppe k: ist(k) ≥ soll(k, g) in der Ordnung - < P < R < A; ist(k) = höchste Stufe, deren IDS-Pflichtspezifikationen bestanden sind"},
      "grenzwerte": [], "meldung": "Gate {gate} gesperrt: {gruppe} hat Reifegrad {ist}, verlangt ist {soll}.",
      "alternative": [{"art": "A5_freigabeweg", "beschreibung": "fehlende Auswahl oder Merkmale nachtragen; Gate erneut prüfen"}],
      "status": "U", "beispiel": ["keins"], "kapitel": "11.5", "anforderungen": ["ANF-11-05", "ANF-11-06"]},
     {"id": "M.Regnauer.Ausstattung-vor-Montage", "version": "0.1.0", "titel": "Montage frühestens 12 Wochen nach vollständiger Ausstattungsfestlegung",
      "klasse": "R4", "haerte": "hart",
      "quelle": {"art": "M", "werk": "Bau- und Leistungsbeschreibung Vitalhaus 10/2024, AGB", "fundstelle": "AGB § 5 und § 6", "fassung": "10/2024", "status": "V", "bib": ["regnauerBLB2024"], "recherche": ["10"]},
      "profil": {"name": "M-Firma", "version": "0.1.0"}, "schicht": "S5",
      "geltung": {"gebaeudetypen": ["alle"], "zeit": {"von": None, "bis": None, "stichtag": "vertragsschluss"}},
      "eingaben": [{"name": "ausstattung_unterschrieben_am", "einheit": "d", "quelle": "IfcApproval G4"}, {"name": "montage_termin", "einheit": "d", "quelle": "Terminplan"}],
      "pruefung": {"typ": "rechnung", "formel": "montage_termin − ausstattung_unterschrieben_am ≥ 84 d ∧ alle Bemusterungsgruppen an G4 im Reifegrad A (Herstellerprofil M-Regnauer)", "parameter": {"min_tage": 84}},
      "grenzwerte": [{"name": "min_tage", "wert": 84, "einheit": "d", "richtung": "min", "fundstelle": "AGB § 5/§ 6", "status": "V"}],
      "meldung": "Montage am {montage} liegt {tage} Tage nach der Ausstattungsfestlegung; verlangt sind 84 Tage.",
      "alternative": [{"art": "A1_grenzwert", "beschreibung": "spätester Termin der Ausstattungsfestlegung = Montage − 84 Tage"}],
      "status": "V", "beispiel": ["keins"], "kapitel": "11.5", "anforderungen": ["ANF-11-07"]},
     {"id": "M.Reifegrad.Lieferdaten", "version": "0.1.0", "titel": "Lieferdaten (Charge, Seriennummer, Garantie) an der Übergabe",
      "klasse": "R2", "haerte": "hart",
      "quelle": {"art": "M", "werk": "spezifikation/reifegrade.yaml#lieferdaten", "fundstelle": "lieferdaten je Gruppe", "fassung": "0.1.0 (2026-09-27)", "status": "U", "bib": ["bsi2024ids"]},
      "profil": {"name": "HRB-IDS-Reifegrad", "version": "0.1.0"}, "schicht": "S5",
      "geltung": {"gebaeudetypen": ["alle"], "zeit": {"von": None, "bis": None, "stichtag": "abnahme"}},
      "eingaben": [], "pruefung": {"typ": "ids", "formel": "A-IDS mit Lieferdaten als cardinality=required (Variante G7); vor G7 optional mit Wertprüfung"},
      "grenzwerte": [], "meldung": "{objekt}: Lieferdatum {merkmal} fehlt für die Hausakte.",
      "alternative": [{"art": "A5_freigabeweg", "beschreibung": "Lieferschein erfassen (Barcode/GTIN + Charge)"}],
      "status": "U", "beispiel": ["B16"], "kapitel": "11.4", "anforderungen": ["ANF-11-11"]},
    ]
    kat = {"katalog": {"name": "HRB-Regelkatalog Kapitel 11 (Reifegrade)", "version": "0.1.0", "stand": "2026-09-27", "kapitel": ["11"],
           "hinweis": "Erzeugt aus spezifikation/reifegrade.yaml. Neues Profil HRB-IDS-Reifegrad (S5) ist in regelprofile.yaml zu registrieren."},
           "regeln": regeln + extra}
    head = "# Regelkatalog Kapitel 11: Reifegrade P/R/A als IDS-Regeln (R2) und Gate-Regeln (R3/R4).\n# Schema: regel.schema.json. Erzeugt aus reifegrade.yaml (Kapitel 11.5); nicht von Hand pflegen.\n\n"
    open(SPEZ/"regelkatalog-11.yaml", "w", encoding="utf-8").write(head + yaml.safe_dump(kat, sort_keys=False, allow_unicode=True, width=160))
    print(len(regeln) + len(extra), "Regeln")

# ---------- Prüfung ----------
def pruefen():
    ok = lambda m: print("OK  ", m)
    # 1 Parsebarkeit
    for p in ["reifegrade.yaml", "regelkatalog-11.yaml", "regelkatalog-12.yaml", "bemusterung-abhaengigkeiten.yaml"]:
        yaml.safe_load(open(SP/p, encoding="utf-8")); ok(f"YAML parsebar: {p}")
    S = json.load(open(SP/"bemusterung-katalog.schema.json", encoding="utf-8"))
    jsonschema.Draft202012Validator.check_schema(S); ok("JSON-Schema gültig nach Draft 2020-12")
    V = jsonschema.Draft202012Validator(S, format_checker=jsonschema.FormatChecker())
    # 2 Beispiele
    bsp = sorted(glob.glob(str(SP/"beispiele/*.json")))
    for b in bsp:
        d = json.load(open(b, encoding="utf-8")); e = list(V.iter_errors(d))
        assert not e, (b, [x.message for x in e][:3]); ok(f"valide: {pathlib.Path(b).name}")
        if d.get("inhaltshash"):
            k = json.dumps({x: y for x, y in d.items() if x not in ("inhaltshash", "lieferdaten")}, sort_keys=True, separators=(",", ":"), ensure_ascii=False)
            assert d["inhaltshash"] == "sha256:" + hashlib.sha256(k.encode()).hexdigest(); ok(f"  Inhaltshash reproduziert: {d['inhaltshash'][:19]}…")
    def gtin_ok(g):
        s = sum(int(c) * (3 if (len(g) - 1 - i) % 2 else 1) for i, c in enumerate(g[:-1])); return (10 - s % 10) % 10 == int(g[-1])
    gt = set(re.findall(r'"gtin": "([0-9]+)"', "".join(open(b, encoding="utf-8").read() for b in bsp)))
    assert all(gtin_ok(g) for g in gt); ok(f"{len(gt)} GTINs mit gültiger Prüfziffer")
    assert not gtin_ok("2000000000016"); ok("Negativtest GTIN 2000000000016 ungültig")
    # 3 Negativtests Schema
    fl = json.load(open(SP/"beispiele/bemusterung-auswahl-fliese-fischgraet.json", encoding="utf-8"))
    neg = {}
    x = copy.deepcopy(fl); del x["inhaltshash"]; neg["A festgeschrieben ohne inhaltshash"] = x
    x = copy.deepcopy(fl); del x["leistung"]["verlegung"]["fuge"]; neg["Fliese ohne Fugenfarbe/-mörtel"] = x
    x = copy.deepcopy(fl); del x["artikel"]["hersteller"]["gtin"]; neg["A ohne GTIN (keine Einzelanfertigung)"] = x
    x = copy.deepcopy(fl); x["reifegrad"] = "R"; neg["festgeschrieben mit Reifegrad R"] = x
    x = copy.deepcopy(fl); x["leistung"]["verlegung"]["muster"] = "Drittelverband"; neg["Muster außerhalb des Vokabulars"] = x
    x = json.load(open(SP/"beispiele/bemusterung-artikel-fliese-s60x10.json", encoding="utf-8")); del x["freeze"]; neg["Katalogartikel ohne freeze"] = x
    x = json.load(open(SP/"beispiele/bemusterung-artikel-fliese-s60x10.json", encoding="utf-8")); x["darstellung"] = {"modus": "herstellertextur"}; neg["Herstellertextur ohne Lizenz"] = x
    for n, d in neg.items():
        assert list(V.iter_errors(d)), n; ok(f"Negativtest abgewiesen: {n}")
    # 4 Regelkataloge und Referenzen
    RS = json.load(open(SP/"regel.schema.json", encoding="utf-8"))
    alle = set()
    for p in ["regelkatalog.yaml", "regelkatalog-11.yaml", "regelkatalog-12.yaml"]:
        d = yaml.safe_load(open(SP/p, encoding="utf-8")); jsonschema.Draft202012Validator(RS).validate(d); alle |= {r["id"] for r in d["regeln"]}
        ok(f"regel.schema.json: {p} ({len(d['regeln'])} Regeln)")
    A = yaml.safe_load(open(SP/"bemusterung-abhaengigkeiten.yaml", encoding="utf-8"))
    refs = {k["regel"] for k in A["kanten"]} | {r for o in A["optionen"] for r in o["regeln"]} | {f["regel"] for o in A["optionen"] for fs in o["folgen"].values() for f in fs}
    refs |= {p["regel"] for b in bsp for p in json.load(open(b, encoding="utf-8")).get("pruefungen", [])}
    refs |= {r for b in bsp for r in json.load(open(b, encoding="utf-8")).get("kompatibilitaet", {}).get("regeln", [])}
    fehl = refs - alle; assert not fehl, fehl; ok(f"{len(refs)} referenzierte Regel-IDs, alle definiert")
    kat = {k["id"] for k in A["kategorien"]}; enum = set(S["$defs"]["kategorie"]["enum"]); assert kat == enum, kat ^ enum; ok(f"{len(kat)} Kategorien = Schema-Enum")
    dom = set(A["domaenen"]) | kat; assert all(k["von"] in dom and k["nach"] in dom for k in A["kanten"]); ok(f"{len(A['kanten'])} Kanten mit gültigen Knoten")
    opt = {o["id"] for o in A["optionen"]}; used = {f["option"] for b in bsp for f in json.load(open(b, encoding="utf-8")).get("folgen", [])}
    assert used <= opt; ok(f"{len(opt)} Optionen; Beispielfolgen verweisen auf vorhandene Optionen")
    # Zyklen im Teilgraph 'erfordert'
    g = {}
    for k in A["kanten"]:
        if k["art"] == "erfordert": g.setdefault(k["von"], set()).add(k["nach"])
    def zyklus(n, weg):
        if n in weg: return True
        return any(zyklus(m, weg | {n}) for m in g.get(n, ()))
    assert not any(zyklus(n, set()) for n in g); ok("Teilgraph 'erfordert' ist azyklisch")
    # 5 IDS
    XSD = xmlschema.XMLSchema(str(pathlib.Path(ids.__file__).parent/"ids.xsd"))
    for p in sorted(glob.glob(str(SP/"ids/*.ids"))):
        XSD.validate(p); n = len(ids.open(p).specifications); ok(f"IDS XSD-gültig und von ifctester geparst: {pathlib.Path(p).name} ({n})")
    # 6 Monotonie der Pflichtmerkmale
    for gname, gg in Y["bauteilgruppen"].items():
        if not gg["P"].get("ids"): continue
        s = {l: {x.name.split()[0] for x in ids.open(str(SP/gg[l]["ids"])).specifications if x.maxOccurs != 0 and "-L01" not in x.name} for l in "PRA"}
        assert s["P"] <= s["R"] <= s["A"]; ok(f"Monotonie {gname}: |P| = {len(s['P'])} ⊆ |R| = {len(s['R'])} ⊆ |A| = {len(s['A'])}")
    # 7 Phasenmatrix monoton je Zeile
    o = {"-": 0, "P": 1, "R": 2, "A": 3}
    for k, row in Y["phasen_matrix"]["gruppen"].items():
        assert all(o[a] <= o[b] for a, b in zip(row, row[1:])), k
    ok(f"Phasenmatrix: {len(Y['phasen_matrix']['gruppen'])} Gruppen, jede Zeile monoton")

# ---------- Modelltests ----------
def modelle():
    res = {}
    def run(model, gruppe, lvl):
        I = ids.open(str(SPEZ/"ids"/f"{gruppe}-{lvl}.ids")); I.validate(model)
        failed = [s.name.split()[0] for s in I.specifications if not s.status]
        return {"spez": len(I.specifications), "bestanden": len(I.specifications)-len(failed), "verfehlt": failed}
    def report(name, model, gruppe):
        for lvl in "PRA":
            r = run(model, gruppe, lvl); res[f"{name}|{gruppe}-{lvl}"] = r
            print(f"{name:34s} {gruppe}-{lvl}: {r['bestanden']}/{r['spez']}  verfehlt: {', '.join(r['verfehlt']) or '–'}")
    
    # 1) B1 real
    report("B1 wandelement.ifc", ifcopenshell.open(str(AUS/"wandelement.ifc")), "wandelement")
    report("B1 wandelement_fehlerhaft.ifc", ifcopenshell.open(str(AUS/"wandelement_fehlerhaft.ifc")), "wandelement")
    
    # 2) B16/B14 real, unverändert
    for fn in ["b16_chevron_60x10__punkt_einzeln.ifc", "b16_gerade_60x60__punkt_aggregiert.ifc", "b14_A_bodenplatte_nass.ifc"]:
        report(fn, ifcopenshell.open(str(AUS/fn)), "belag")
    
    # 3) B16 migriert: Präfix HRB_, HRB_Auswahl, HRB_Belag, STLB-Klassifikation ergänzt (GTIN bleibt 'BEISPIEL-GTIN-…')
    def migrate(fn, kat="Fliese", status="festgeschrieben", gtin=None):
        f = ifcopenshell.open(str(AUS/fn))
        for ps in f.by_type("IfcPropertySet"):
            if ps.Name.startswith("HP_"): ps.Name = "HRB_" + ps.Name[3:]
            if ps.Name.startswith("B14_"): ps.Name = "HRB_" + ps.Name[4:]
        stlb = api.run("classification.add_classification", f, classification="STLB-Bau")
        for c in f.by_type("IfcCovering"):
            if c.Decomposes: continue
            pv = ue.get_psets(c)
            if "HRB_Verlegung" not in pv and "HRB_Fussbodenaufbau" not in pv: continue
            ps = api.run("pset.add_pset", f, product=c, name="HRB_Auswahl")
            api.run("pset.edit_pset", f, pset=ps, properties={"AuswahlID": str(uuid.UUID(int=c.id())), "OptionID": "K-FLI-0001", "Kategorie": kat,
                "Reifegrad": "A", "Status": status, "Darstellung": "aehnlich", "Inhaltshash": "sha256:" + "0"*64})
            pb = api.run("pset.add_pset", f, product=c, name="HRB_Belag")
            api.run("pset.edit_pset", f, pset=pb, properties={"Belagart": kat, "FormatLaenge": 600.0, "FormatBreite": 600.0, "Dicke": 10.0,
                "Rutschhemmung": "R10", "Wassereinwirkungsklasse": "W2-I", "Holzart": "Eiche", "Sortierung": "Natur", "Oberflaeche": "geoelt", "Verlegeart": "verklebt"})
            if "HRB_Verlegung" not in pv:
                pvl = api.run("pset.add_pset", f, product=c, name="HRB_Verlegung")
                api.run("pset.edit_pset", f, pset=pvl, properties={"Muster": "gerade", "Fugenbreite": 3.0, "Fugenfarbe": "zementgrau"})
            else:
                api.run("pset.edit_pset", f, pset=f.by_id(pv["HRB_Verlegung"]["id"]), properties={"Fugenfarbe": "zementgrau"})
            api.run("classification.add_reference", f, products=[c], identification="024", name="Fliesen- und Plattenarbeiten", classification=stlb)
        for t in f.by_type("IfcCoveringType"):
            pm = ue.get_psets(t).get("Pset_ManufacturerTypeInformation")
            if pm:
                props = {"ModelReference": "Serie Beispiel"}
                if gtin: props["GlobalTradeItemNumber"] = gtin
                api.run("pset.edit_pset", f, pset=f.by_id(pm["id"]), properties=props)
        return f
    report("B16 chevron einzeln, migriert", migrate("b16_chevron_60x10__punkt_einzeln.ifc"), "belag")
    report("B16 chevron einzeln, migriert+GTIN", migrate("b16_chevron_60x10__punkt_einzeln.ifc", gtin="2000000000015"), "belag")
    report("B16 gerade aggr., migriert+GTIN", migrate("b16_gerade_60x60__punkt_aggregiert.ifc", gtin="2000000000015"), "belag")
    
    
    
    def migrate_typed(fn, fussboden=True):
        f = ifcopenshell.open(str(AUS/fn))
        for ps in f.by_type("IfcPropertySet"):
            if ps.Name.startswith("HP_"): ps.Name = "HRB_" + ps.Name[3:]
        # Messtypen korrigieren
        for ps in f.by_type("IfcPropertySet"):
            for p in ps.HasProperties:
                if not p.is_a("IfcPropertySingleValue") or p.NominalValue is None: continue
                key = (ps.Name, p.Name)
                m = {("Pset_ManufacturerTypeInformation","GlobalTradeItemNumber"):"IfcIdentifier", ("Pset_ManufacturerTypeInformation","ArticleNumber"):"IfcIdentifier",
                     ("Pset_ManufacturerOccurrence","BatchReference"):"IfcIdentifier", ("HRB_Verlegung","Verschnitt"):"IfcNormalisedRatioMeasure",
                     ("HRB_Verlegung","Rasterursprung_u"):"IfcNormalisedRatioMeasure", ("HRB_Verlegung","Rasterursprung_v"):"IfcNormalisedRatioMeasure",
                     ("HRB_Verlegung","Fugenbreite"):"IfcPositiveLengthMeasure", ("HRB_Verlegung","RohlingeBedarf"):"IfcInteger", ("HRB_Verlegung","Pakete"):"IfcInteger"}
                if key in m: p.NominalValue = f.create_entity(m[key], p.NominalValue.wrappedValue)
                if key == ("Pset_ManufacturerTypeInformation","GlobalTradeItemNumber"): p.NominalValue = f.create_entity("IfcIdentifier", "2000000000015")
                if key == ("Pset_ManufacturerTypeInformation","ArticleNumber"): pass
        stlb = api.run("classification.add_classification", f, classification="STLB-Bau")
        mat = api.run("material.add_material", f, name="Feinsteinzeug (Beispiel)", category="ceramic")
        for t in f.by_type("IfcCoveringType"):
            pm = [ps for ps in t.HasPropertySets if ps.Name == "Pset_ManufacturerTypeInformation"][0]
            pm.HasProperties = list(pm.HasProperties) + [f.createIfcPropertySingleValue("ModelReference", None, f.createIfcLabel("Serie Beispiel"), None)]
        for c in f.by_type("IfcCovering"):
            if c.Decomposes: continue
            api.run("material.assign_material", f, products=[c], material=mat)
            pset(f, c, "HRB_Auswahl", {"AuswahlID": ("IfcIdentifier", str(uuid.UUID(int=c.id()))), "OptionID": ("IfcIdentifier", "K-FLI-0001"),
                 "Kategorie": ("IfcLabel", "Fliese"), "Reifegrad": ("IfcLabel", "A"), "Status": ("IfcLabel", "festgeschrieben"),
                 "Darstellung": ("IfcLabel", "aehnlich"), "Inhaltshash": ("IfcIdentifier", "sha256:" + "0"*64)})
            pset(f, c, "HRB_Belag", {"Belagart": ("IfcLabel", "Fliese"), "FormatLaenge": ("IfcPositiveLengthMeasure", 600.0),
                 "FormatBreite": ("IfcPositiveLengthMeasure", 600.0 if "60x60" in fn else 100.0), "Dicke": ("IfcPositiveLengthMeasure", 10.0),
                 "Rutschhemmung": ("IfcLabel", "R10"), "Barfuss": ("IfcLabel", "B"), "Wassereinwirkungsklasse": ("IfcLabel", "W2-I")})
            pv = [r.RelatingPropertyDefinition for r in c.IsDefinedBy if r.RelatingPropertyDefinition.Name == "HRB_Verlegung"][0]
            pv.HasProperties = list(pv.HasProperties) + [f.createIfcPropertySingleValue("Fugenfarbe", None, f.createIfcLabel("zementgrau"), None)]
            if fussboden:  # Werte aus B14 Variante A, Bad (Beispiel): OKFF 210 mm, CT-F4, R_lambda_B 0,0187
                pset(f, c, "HRB_Fussbodenaufbau", {"OKFF": ("IfcLengthMeasure", 210.0), "Estrich": ("IfcLabel", "CT_F4"),
                     "R_lambda_B": ("IfcThermalResistanceMeasure", 0.0187), "NachweisOKFF": ("IfcBoolean", True)})
            api.run("classification.add_reference", f, products=[c], identification="024", name="Fliesen- und Plattenarbeiten", classification=stlb)
        return f
    for fn, name in [("b16_gerade_60x60__punkt_aggregiert.ifc", "B16 gerade 60x60 aggr., migriert typisiert"),
                     ("b16_chevron_60x10__punkt_einzeln.ifc", "B16 chevron einzeln, migriert typisiert")]:
        report(name, migrate_typed(fn), "belag")
    f = migrate_typed("b16_chevron_60x10__punkt_einzeln.ifc")   # Korrektur: Typ (Artikel) auch am Belag
    f.createIfcRelDefinesByType(ifcopenshell.guid.new(), None, None, None, [c for c in f.by_type("IfcCovering") if not c.Decomposes], f.by_type("IfcCoveringType")[0])
    report("B16 chevron einzeln, migriert, Typ am Belag", f, "belag")
    
    # ---------- synthetische Modelle Sanitär und Treppe je Reifegrad ----------
    def basis():
        f = ifcopenshell.file(schema="IFC4X3_ADD2")
        p = api.run("root.create_entity", f, ifc_class="IfcProject", name="Test"); api.run("unit.assign_unit", f)
        api.run("context.add_context", f, context_type="Model")
        site = api.run("root.create_entity", f, ifc_class="IfcSite", name="S"); api.run("aggregate.assign_object", f, products=[site], relating_object=p)
        b = api.run("root.create_entity", f, ifc_class="IfcBuilding", name="B"); api.run("aggregate.assign_object", f, products=[b], relating_object=site)
        st = api.run("root.create_entity", f, ifc_class="IfcBuildingStorey", name="OG"); api.run("aggregate.assign_object", f, products=[st], relating_object=b)
        sp = api.run("root.create_entity", f, ifc_class="IfcSpace", name="OG-Bad"); api.run("aggregate.assign_object", f, products=[sp], relating_object=st)
        return f, st, sp
    def auswahl(f, obj, lvl, opt, kat):
        d = {"OptionID": ("IfcIdentifier", opt), "Kategorie": ("IfcLabel", kat), "Reifegrad": ("IfcLabel", lvl), "Darstellung": ("IfcLabel", "generisch")}
        if lvl in "RA": d["Status"] = ("IfcLabel", "festgeschrieben" if lvl == "A" else "geprueft")
        if lvl == "A": d.update({"AuswahlID": ("IfcIdentifier", "7b9d0c3e-1f2a-4b5c-8d6e-0123456789ab"), "Inhaltshash": ("IfcIdentifier", "sha256:" + "a"*64)})
        pset(f, obj, "HRB_Auswahl", d)
    def sanitaer(lvl):
        f, st, sp = basis(); stlb = api.run("classification.add_classification", f, classification="STLB-Bau")
        mat = api.run("material.add_material", f, name="Sanitärkeramik weiß", category="ceramic")
        t = api.run("root.create_entity", f, ifc_class="IfcSanitaryTerminalType", predefined_type="TOILETPAN", name="Wand-WC Beispiel")
        wc = api.run("root.create_entity", f, ifc_class="IfcSanitaryTerminal", predefined_type="TOILETPAN", name="WC OG-Bad")
        api.run("type.assign_type", f, related_objects=[wc], relating_type=t); api.run("spatial.assign_container", f, products=[wc], relating_structure=sp)
        api.run("material.assign_material", f, products=[wc], material=mat); auswahl(f, wc, lvl, "K-SAN-0001", "Sanitaer")
        if lvl in "RA":
            mti = {"Manufacturer": ("IfcLabel", "Beispielhersteller"), "ModelReference": ("IfcLabel", "Serie Beispiel")}
            if lvl == "A": mti.update({"GlobalTradeItemNumber": ("IfcIdentifier", "2000000000022"), "ArticleNumber": ("IfcIdentifier", "WC-0001")})
            pset(f, t, "Pset_ManufacturerTypeInformation", mti)
            pset(f, t, "Pset_SanitaryTerminalTypeCommon", {"NominalLength": ("IfcNonNegativeLengthMeasure", 540.0), "NominalWidth": ("IfcNonNegativeLengthMeasure", 360.0)})
            pset(f, t, "Pset_SanitaryTerminalTypeToiletPan", {"PanMounting": ("IfcLabel", "WALLHUNG")})
            s = {"Vorwandsystem": ("IfcLabel", "Montageelement Holzständer (Beispiel)"), "Stromanschluss": ("IfcBoolean", False),
                 "BewegungsflaecheBreite": ("IfcPositiveLengthMeasure", 800.0), "BewegungsflaecheTiefe": ("IfcPositiveLengthMeasure", 750.0)}
            if lvl == "A": s["Montagehoehe"] = ("IfcPositiveLengthMeasure", 420.0)
            pset(f, wc, "HRB_Sanitaer", s)
            api.run("classification.add_reference", f, products=[wc], identification="045", name="Sanitär-Ausstattung", classification=stlb)
            port = api.run("system.add_port", f, element=wc); port.PredefinedType = "PIPE"
            pset(f, port, "Pset_DistributionPortTypePipe", {"NominalDiameter": ("IfcPositiveLengthMeasure", 100.0)})
        return f
    def treppe(lvl):
        f, st, sp = basis(); stlb = api.run("classification.add_classification", f, classification="STLB-Bau")
        mat = api.run("material.add_material", f, name="Buche keilgezinkt", category="wood")
        tr = api.run("root.create_entity", f, ifc_class="IfcStair", predefined_type="STRAIGHT_RUN_STAIR", name="Treppe EG-OG")
        api.run("spatial.assign_container", f, products=[tr], relating_structure=st); api.run("material.assign_material", f, products=[tr], material=mat)
        auswahl(f, tr, lvl, "K-TRE-0001", "Treppe")
        fl = api.run("root.create_entity", f, ifc_class="IfcStairFlight", predefined_type="STRAIGHT", name="Lauf 1")
        api.run("aggregate.assign_object", f, products=[fl], relating_object=tr)
        if lvl in "RA":   # Werte aus B5: 17 Steigungen à 170,59 mm, Auftritt 290 mm, Laufbreite 900 mm
            pset(f, fl, "Pset_StairFlightCommon", {"NumberOfRiser": ("IfcCountMeasure", 17), "RiserHeight": ("IfcPositiveLengthMeasure", 170.59),
                 "TreadLength": ("IfcPositiveLengthMeasure", 290.0), "WalkingLineOffset": ("IfcPositiveLengthMeasure", 450.0), "Headroom": ("IfcPositiveLengthMeasure", 2000.0)})
            pset(f, tr, "HRB_Verziehung", {"Methode": ("IfcLabel", "keine"), "Laufrichtung": ("IfcLabel", "rechts"), "Schrittmass": ("IfcPositiveLengthMeasure", 631.18)})
            api.run("classification.add_reference", f, products=[tr], identification="027", name="Tischlerarbeiten", classification=stlb)
            rl = api.run("root.create_entity", f, ifc_class="IfcRailing", predefined_type="HANDRAIL", name="Handlauf")
            api.run("aggregate.assign_object", f, products=[rl], relating_object=tr)
            pset(f, rl, "Pset_RailingCommon", {"Height": ("IfcPositiveLengthMeasure", 900.0)})
        if lvl == "A":
            pset(f, tr, "Pset_ManufacturerTypeInformation", {"Manufacturer": ("IfcLabel", "Beispiel-Treppenbau"), "ArticleNumber": ("IfcIdentifier", "AUF-2026-0815")})
            for n in ("Wange links", "Wange rechts"):
                w = api.run("root.create_entity", f, ifc_class="IfcMember", predefined_type="STRINGER", name=n)
                api.run("aggregate.assign_object", f, products=[w], relating_object=tr); api.run("material.assign_material", f, products=[w], material=mat)
        return f
    for gruppe, bau in [("sanitaer", sanitaer), ("treppe", treppe)]:
        for mlvl in "PRA":
            report(f"synth. {gruppe}, Modell {mlvl}", bau(mlvl), gruppe)

if __name__ == "__main__":
    cmd = sys.argv[1] if len(sys.argv) > 1 else "pruefen"
    if cmd == "erzeugen":
        ok_ = erzeugen_ids(); erzeugen_rk11(); sys.exit(0 if ok_ else 1)
    elif cmd == "pruefen":
        pruefen()
    elif cmd == "modelle":
        modelle()

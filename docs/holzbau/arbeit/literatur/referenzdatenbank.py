"""Baut die Referenzdatenbank der Arbeit aus allen Teilquellen.

Eingaben (alle in diesem Ordner):
  lit-*.bib                    vollständige bibliografische Einträge
  quellen-master.csv           stabile IDs Q001 … (aus bibmerge.py)
  quellen-bewertung.csv        Einzelbewertung nach Protokoll 2a.5
  bewertung/zweitbewertung.csv blinde Zweitbewertung (optional)
  abstracts/teil-*.jsonl       Originalabstracts, OA-Status, Volltext-URL (optional)

Ausgaben (Ordner referenzdatenbank/):
  referenzdatenbank.sqlite     Abfragen per SQL (Tabellen quellen, bewertung, zweitbewertung, abstract)
  referenzdatenbank.bib        Import in Zotero/JabRef/Citavi: mit abstract, keywords (FF, Nutzung), annote (Begründung), url
  referenzdatenbank.json       CSL-JSON (Zotero, Pandoc)
  README.md                    Aufbau, Import, Statistik

Deterministisch: gleiche Eingaben ergeben byte-identische Text-Ausgaben.
"""
import csv, glob, json, os, re, sqlite3, sys

HERE = os.path.dirname(os.path.abspath(__file__))
OUT = os.path.join(HERE, 'referenzdatenbank')
sys.path.insert(0, HERE)
from bibmerge import parse, fld  # noqa: E402  (gleicher Parser wie bei der Masterliste)

BIBFELDER = ['author', 'editor', 'title', 'year', 'journal', 'booktitle', 'volume', 'number', 'pages',
             'publisher', 'institution', 'organization', 'school', 'type', 'edition', 'address',
             'doi', 'isbn', 'url', 'note', 'howpublished']


def lade_bib():
    eintraege = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'lit-*.bib'))):
        for typ, key, body in parse(open(f, encoding='utf-8').read()):
            if typ.lower() in ('comment', 'preamble', 'string') or key in eintraege:
                continue
            e = {'typ': typ.lower(), 'datei': os.path.basename(f)}
            for n in BIBFELDER:
                e[n] = fld(body, n)
            eintraege[key] = e
    return eintraege


def lade_csv(p):
    return list(csv.DictReader(open(p, encoding='utf-8'))) if os.path.exists(p) else []


def lade_abstracts():
    ab = {}
    for f in sorted(glob.glob(os.path.join(HERE, 'abstracts', 'teil-*.jsonl'))):
        for zeile in open(f, encoding='utf-8'):
            zeile = zeile.strip()
            if zeile:
                d = json.loads(zeile)
                ab[d['id']] = d
    return ab


def bibtex_escape(s):
    return s.replace('{', '(').replace('}', ')') if s else s


def main():
    os.makedirs(OUT, exist_ok=True)
    bib = lade_bib()
    master = lade_csv(os.path.join(HERE, 'quellen-master.csv'))
    bew = {r['id']: r for r in lade_csv(os.path.join(HERE, 'quellen-bewertung.csv'))}
    zweit = {r['id']: r for r in lade_csv(os.path.join(HERE, 'bewertung', 'zweitbewertung.csv'))}
    ab = lade_abstracts()

    db_pfad = os.path.join(OUT, 'referenzdatenbank.sqlite')
    if os.path.exists(db_pfad):
        os.remove(db_pfad)
    con = sqlite3.connect(db_pfad)
    c = con.cursor()
    c.execute('CREATE TABLE quellen (id TEXT PRIMARY KEY, key TEXT, alias TEXT, typ TEXT, datei TEXT, '
              + ', '.join(f'"{n}" TEXT' for n in BIBFELDER) + ')')
    bewfelder = ['art', 'ff1', 'ff2', 'ff3', 'ff4', 'ff5', 'ff6', 'R', 'beitrag', 'qualitaet', 'uebertragbarkeit',
                 'P', 'kern', 'nutzung', 'kapitel', 'begruendung', 'verifiziert', 'pruefweg']
    c.execute('CREATE TABLE bewertung (id TEXT PRIMARY KEY, ' + ', '.join(f'"{n}" TEXT' for n in bewfelder) + ')')
    c.execute('CREATE TABLE zweitbewertung (id TEXT PRIMARY KEY, ' + ', '.join(f'"{n}" TEXT' for n in bewfelder) + ')')
    abfelder = ['abstract', 'abstract_quelle', 'abstract_url', 'sprache', 'oa_status', 'oa_url', 'oa_lizenz',
                'keywords', 'abgerufen', 'hinweis']
    c.execute('CREATE TABLE abstract (id TEXT PRIMARY KEY, ' + ', '.join(f'"{n}" TEXT' for n in abfelder) + ')')

    csl, bibout = [], []
    for m in master:
        qid, key = m['id'], m['key']
        e = bib.get(key, {})
        c.execute('INSERT INTO quellen VALUES (' + ','.join('?' * (5 + len(BIBFELDER))) + ')',
                  [qid, key, m.get('alias', ''), e.get('typ', m['typ']), e.get('datei', '')] + [e.get(n, '') for n in BIBFELDER])
        b = bew.get(qid)
        if b:
            c.execute('INSERT INTO bewertung VALUES (' + ','.join('?' * (1 + len(bewfelder))) + ')',
                      [qid] + [str(b.get(n, '')) for n in bewfelder])
        z = zweit.get(qid)
        if z:
            c.execute('INSERT INTO zweitbewertung VALUES (' + ','.join('?' * (1 + len(bewfelder))) + ')',
                      [qid] + [str(z.get(n, '')) for n in bewfelder])
        a = ab.get(qid, {})
        if a:
            c.execute('INSERT INTO abstract VALUES (' + ','.join('?' * (1 + len(abfelder))) + ')',
                      [qid] + [json.dumps(a.get(n), ensure_ascii=False) if isinstance(a.get(n), list) else (a.get(n) or '') for n in abfelder])

        # Schlagworte für Literaturverwaltung: Q-ID, FF-Relevanz, Nutzung, Kernbestand
        kw = [qid]
        if b:
            kw += [f'FF{i}={b[f"ff{i}"]}' for i in range(1, 7) if str(b.get(f'ff{i}', '0')) not in ('0', '')]
            kw += [f'Nutzung:{b["nutzung"]}', f'Qualitaet:{b["qualitaet"]}', 'Kernbestand' if b.get('kern') == 'ja' else 'Peripherie']
        kw += a.get('keywords') or []
        felder = {n: e.get(n, '') for n in BIBFELDER}
        felder['abstract'] = a.get('abstract', '')
        felder['keywords'] = ', '.join(kw)
        felder['annote'] = (b or {}).get('begruendung', '')
        if a.get('oa_url') and not felder['url']:
            felder['url'] = a['oa_url']
        zeilen = [f'@{e.get("typ", m["typ"]).lower()}{{{key},']
        for n, v in felder.items():
            if v:
                zeilen.append(f'  {n} = {{{bibtex_escape(v) if n in ("abstract", "annote") else v}}},')
        zeilen.append('}')
        bibout.append('\n'.join(zeilen))

        autoren = [x.strip() for x in re.split(r'\s+and\s+', e.get('author', '')) if x.strip()]
        item = {'id': key, 'type': {'article': 'article-journal', 'inproceedings': 'paper-conference', 'book': 'book',
                                    'phdthesis': 'thesis', 'mastersthesis': 'thesis', 'techreport': 'report',
                                    'incollection': 'chapter', 'standard': 'standard'}.get(e.get('typ', ''), 'document'),
                'title': e.get('title', m['titel']), 'note': qid}
        if autoren:
            item['author'] = [{'family': x.split(',')[0].strip(), 'given': x.split(',', 1)[1].strip()} if ',' in x
                              else {'literal': x} for x in autoren]
        if e.get('year', '').strip()[:4].isdigit():
            item['issued'] = {'date-parts': [[int(e['year'].strip()[:4])]]}
        for src, dst in [('doi', 'DOI'), ('url', 'URL'), ('journal', 'container-title'), ('booktitle', 'container-title'),
                         ('volume', 'volume'), ('number', 'issue'), ('pages', 'page'), ('publisher', 'publisher'), ('isbn', 'ISBN')]:
            if e.get(src) and dst not in item:
                item[dst] = e[src]
        if a.get('abstract'):
            item['abstract'] = a['abstract']
        item['keyword'] = ', '.join(kw)
        csl.append(item)
    con.commit()

    # Sichten für häufige Abfragen
    c.executescript('''
      CREATE VIEW kernbestand AS SELECT q.id, q.key, q.title, q.year, b.P, b.nutzung, b.kapitel, b.begruendung
        FROM quellen q JOIN bewertung b USING(id) WHERE b.kern = 'ja' ORDER BY CAST(b.P AS REAL) DESC, q.id;
      CREATE VIEW ohne_abstract AS SELECT q.id, q.key, q.title FROM quellen q LEFT JOIN abstract a USING(id)
        WHERE a.abstract IS NULL OR a.abstract = '';
    ''')
    con.commit()
    n = {t: c.execute(f'SELECT COUNT(*) FROM {t}').fetchone()[0] for t in ('quellen', 'bewertung', 'zweitbewertung', 'abstract')}
    mit_abs = c.execute("SELECT COUNT(*) FROM abstract WHERE abstract <> ''").fetchone()[0]
    oa = c.execute("SELECT oa_status, COUNT(*) FROM abstract GROUP BY oa_status ORDER BY 2 DESC").fetchall()
    con.close()

    open(os.path.join(OUT, 'referenzdatenbank.bib'), 'w', encoding='utf-8').write('\n\n'.join(bibout) + '\n')
    json.dump(csl, open(os.path.join(OUT, 'referenzdatenbank.json'), 'w', encoding='utf-8'), ensure_ascii=False, indent=1)

    readme = f"""# Referenzdatenbank

Automatisch erzeugt von `../referenzdatenbank.py`. Nicht von Hand bearbeiten; Änderungen in den Quelldateien vornehmen und das Skript neu ausführen.

## Stand

| Inhalt | Anzahl |
|---|---|
| Quellen | {n['quellen']} |
| einzeln bewertet | {n['bewertung']} |
| zweitbewertet (blind) | {n['zweitbewertung']} |
| Abstract-Datensätze | {n['abstract']} |
| davon mit Originalabstract | {mit_abs} |

Open-Access-Status: {', '.join(f'{k or "–"}: {v}' for k, v in oa) or 'noch nicht erfasst'}

## Dateien

- `referenzdatenbank.sqlite`: Tabellen `quellen`, `bewertung`, `zweitbewertung`, `abstract`; Sichten `kernbestand`, `ohne_abstract`.
  Beispiel: `sqlite3 referenzdatenbank.sqlite "SELECT id,key,P FROM kernbestand LIMIT 20"`
- `referenzdatenbank.bib`: für Zotero, JabRef oder Citavi. Enthält `abstract`, `keywords` (Q-ID, Relevanz je Forschungsfrage, Nutzung, Qualität, Kernbestand) und `annote` (Begründung der Passung).
- `referenzdatenbank.json`: CSL-JSON für Zotero und Pandoc.

## Import in Zotero

1. Datei → Importieren → `referenzdatenbank.bib`
2. Alle Einträge markieren → Rechtsklick → „Verfügbare PDFs suchen“. Zotero lädt frei zugängliche Volltexte legal über Unpaywall.
3. Schlagwort `Kernbestand` filtert die 1–2 Dutzend Quellen je Kapitel, die zuerst gelesen werden sollten.

## Rechtlicher Hinweis

Abstracts sind urheberrechtlich geschützte Texte der Verlage bzw. Autoren. Sie liegen hier zur wissenschaftlichen Arbeit vor, mit Herkunft je Datensatz (`abstract_quelle`, `abstract_url`). Das Repository privat halten. Volltexte werden nicht im Repository gespeichert, sondern nur als Link (`oa_url`) bei frei zugänglichen Fassungen.
"""
    open(os.path.join(OUT, 'README.md'), 'w', encoding='utf-8').write(readme)
    print(json.dumps({'quellen': n['quellen'], 'bewertet': n['bewertung'], 'zweit': n['zweitbewertung'],
                      'abstract_datensaetze': n['abstract'], 'mit_abstract': mit_abs}, ensure_ascii=False))


if __name__ == '__main__':
    main()

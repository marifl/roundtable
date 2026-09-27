"""Führt die Teilbewertungen zusammen, berechnet R und P nach Protokoll 2a.5 und schreibt quellen-bewertung.csv + Statistik."""
import csv, glob, collections, os
HERE = os.path.dirname(os.path.abspath(__file__))
master = {r['id']: r for r in csv.DictReader(open(os.path.join(HERE, '..', 'quellen-master.csv'), encoding='utf-8'))}
QP = {'A': 2.0, 'B': 1.5, 'C': 1.0, 'D': 0.0}
rows = []
for f in sorted(glob.glob(os.path.join(HERE, 'teil-*.csv'))):
    rows += list(csv.DictReader(open(f, encoding='utf-8')))
seen = set(); out = []
for r in rows:
    if r['id'] in seen: continue
    seen.add(r['id'])
    ff = [int(float(r[f'ff{i}'] or 0)) for i in range(1, 7)]
    R = max(ff)
    q = (r['qualitaet'] or '').strip()[:1].upper()
    u = int(float(r['uebertragbarkeit'] or 0))
    P = R + u + QP.get(q, 0)
    r['R'] = R; r['P'] = P; r['kern'] = 'ja' if P >= 5 else 'nein'
    r['titel'] = master.get(r['id'], {}).get('titel', ''); r['jahr'] = master.get(r['id'], {}).get('jahr', '')
    out.append(r)
out.sort(key=lambda r: r['id'])
fields = ['id','key','jahr','titel','art','ff1','ff2','ff3','ff4','ff5','ff6','R','beitrag','qualitaet','uebertragbarkeit','P','kern','nutzung','kapitel','begruendung','verifiziert','pruefweg']
with open(os.path.join(HERE, '..', 'quellen-bewertung.csv'), 'w', newline='', encoding='utf-8') as fh:
    w = csv.DictWriter(fh, fieldnames=fields, extrasaction='ignore'); w.writeheader(); w.writerows(out)
fehlend = sorted(set(master) - seen)
st = collections.Counter(r['nutzung'].strip() for r in out)
lines = ['# Statistik der Quellenbewertung', '', f'- Quellen in der Masterliste: {len(master)}', f'- bewertet: {len(out)}', f'- noch nicht bewertet: {len(fehlend)}' + (f' ({fehlend[0]}–{fehlend[-1]})' if fehlend else ''),
         f'- Kernbestand (P ≥ 5): {sum(r["kern"]=="ja" for r in out)}', f'- verifiziert V: {sum(r["verifiziert"].strip()=="V" for r in out)}, U: {sum(r["verifiziert"].strip()=="U" for r in out)}', '',
         '## Nutzung', ''] + [f'- {k}: {v}' for k, v in st.most_common()] + ['', '## Relevanz je Forschungsfrage (Anzahl Quellen mit Wert ≥ 2)', '']
for i in range(1, 7):
    lines.append(f'- FF{i}: {sum(int(float(r[f"ff{i}"] or 0))>=2 for r in out)} (davon 3: {sum(int(float(r[f"ff{i}"] or 0))==3 for r in out)})')
lines += ['', '## Qualität', ''] + [f'- {k}: {v}' for k, v in sorted(collections.Counter(r['qualitaet'].strip()[:1] for r in out).items())]
lines += ['', '## Kernbestand, sortiert nach P', '', '| id | Key | Jahr | P | FF mit 3 | Nutzung | Kapitel |', '|---|---|---|---|---|---|---|']
for r in sorted([r for r in out if r['kern']=='ja'], key=lambda r: (-r['P'], r['id'])):
    ff3 = ','.join(f'FF{i}' for i in range(1,7) if int(float(r[f'ff{i}'] or 0))==3) or '–'
    lines.append(f"| {r['id']} | {r['key']} | {r['jahr']} | {r['P']:g} | {ff3} | {r['nutzung']} | {r['kapitel']} |")
open(os.path.join(HERE, 'STATISTIK.md'), 'w', encoding='utf-8').write('\n'.join(lines) + '\n')
print('\n'.join(lines[:30]))

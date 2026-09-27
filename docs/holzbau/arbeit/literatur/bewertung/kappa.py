"""Beurteilerübereinstimmung zwischen Erst- und blinder Zweitbewertung (Protokoll 2a.7).

Cohens κ für nominale Merkmale (Kernbestand ja/nein, Nutzung, Qualität), gewichtetes κ (quadratische Gewichte)
für ordinale Merkmale (FF1–FF6, R, Übertragbarkeit). Einordnung nach Landis & Koch (1977).
"""
import csv, os, collections
HERE = os.path.dirname(os.path.abspath(__file__))
QP = {'A': 2.0, 'B': 1.5, 'C': 1.0, 'D': 0.0}

def kappa(a, b, gewicht=None):
    kats = sorted(set(a) | set(b))
    n = len(a); idx = {k: i for i, k in enumerate(kats)}; m = len(kats)
    if m == 1: return 1.0
    O = [[0]*m for _ in range(m)]
    for x, y in zip(a, b): O[idx[x]][idx[y]] += 1
    ra = [sum(r) for r in O]; cb = [sum(O[i][j] for i in range(m)) for j in range(m)]
    w = lambda i, j: 0.0 if i == j else 1.0 if gewicht is None else ((i-j)/(m-1))**2
    po = sum(w(i, j)*O[i][j] for i in range(m) for j in range(m))/n
    pe = sum(w(i, j)*ra[i]*cb[j] for i in range(m) for j in range(m))/(n*n)
    return 1 - po/pe if pe else 1.0

def stufe(k):
    for g, t in [(0.8, 'fast vollkommen'), (0.6, 'erheblich'), (0.4, 'mittelmäßig'), (0.2, 'ausreichend'), (0.0, 'gering')]:
        if k > g: return t
    return 'schlecht'

def P(r):
    R = max(int(float(r[f'ff{i}'] or 0)) for i in range(1, 7))
    return R + int(float(r['uebertragbarkeit'] or 0)) + QP.get((r['qualitaet'] or ' ')[0].upper(), 0), R

erst = {r['id']: r for r in csv.DictReader(open(os.path.join(HERE, '..', 'quellen-bewertung.csv'), encoding='utf-8'))}
zweit = list(csv.DictReader(open(os.path.join(HERE, 'zweitbewertung.csv'), encoding='utf-8')))
paare = [(erst[z['id']], z) for z in zweit if z['id'] in erst]
zeilen = ['# Beurteilerübereinstimmung (Cohens κ)', '', f'Stichprobe: {len(paare)} Quellen (50 Kernbestand, 30 Peripherie, Zufallsauswahl mit festem Seed). Zweitbewertung blind, ohne Einsicht in die Erstbewertung.', '',
          '| Merkmal | Skala | κ | Übereinstimmung (Landis & Koch) | exakt gleich |', '|---|---|---|---|---|']
def zeile(name, skala, a, b, gew=None):
    k = kappa(a, b, gew); gleich = sum(x == y for x, y in zip(a, b))/len(a)
    zeilen.append(f'| {name} | {skala} | {k:.2f} | {stufe(k)} | {gleich:.0%} |')
    return k
ka = [('ja' if P(e)[0] >= 5 else 'nein') for e, z in paare]; kb = [('ja' if P(z)[0] >= 5 else 'nein') for e, z in paare]
zeile('Kernbestand (P ≥ 5)', 'nominal', ka, kb)
zeile('Nutzung', 'nominal', [e['nutzung'].strip() for e, z in paare], [z['nutzung'].strip() for e, z in paare])
zeile('Qualität', 'nominal', [e['qualitaet'].strip()[:1] for e, z in paare], [z['qualitaet'].strip()[:1] for e, z in paare])
zeile('Gesamtrelevanz R', 'ordinal, quadratisch gewichtet', [P(e)[1] for e, z in paare], [P(z)[1] for e, z in paare], 'q')
for i in range(1, 7):
    zeile(f'FF{i}', 'ordinal, quadratisch gewichtet', [int(float(e[f'ff{i}'] or 0)) for e, z in paare], [int(float(z[f'ff{i}'] or 0)) for e, z in paare], 'q')
zeile('Übertragbarkeit', 'ordinal, quadratisch gewichtet', [int(float(e['uebertragbarkeit'] or 0)) for e, z in paare], [int(float(z['uebertragbarkeit'] or 0)) for e, z in paare], 'q')
abw = [(e['id'], e['key'], P(e)[0], P(z)[0]) for e, z in paare if (P(e)[0] >= 5) != (P(z)[0] >= 5)]
zeilen += ['', f'## Abweichende Kernbestand-Entscheidungen ({len(abw)})', '', '| id | Key | P Erst | P Zweit |', '|---|---|---|---|'] + [f'| {a} | {b} | {c:g} | {d:g} |' for a, b, c, d in abw]
zeilen += ['', 'Vorgehen bei Abweichungen: Konsensgespräch bzw. Drittbewertung; Ergebnis in quellen-bewertung.csv übernehmen und hier dokumentieren.']
open(os.path.join(HERE, 'KAPPA.md'), 'w', encoding='utf-8').write('\n'.join(zeilen) + '\n')
print('\n'.join(zeilen))

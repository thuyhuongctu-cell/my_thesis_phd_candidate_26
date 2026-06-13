#!/usr/bin/env python3
"""JED paper — income (GNI/capita) x digital-adoption axis.

The cloud container blocks the World Bank API (same 403 as Crossref/WoS), so
run this on a networked machine to add the income-development axis to the paper.
For each of the 50 economies it pulls GNI per capita (Atlas, NY.GNP.PCAP.CD),
merges with the firm-weighted web-adoption rate from the WBES frame, and reports
the cross-economy correlation between income and adoption.

Run (networked machine):  python3 jed_ai_digital/replication/jed_gni_axis.py
Deps: stdlib urllib + the project's p7_full_ladder build.
"""
import sys, json, warnings, urllib.request, numpy as np, pandas as pd
sys.path.insert(0, 'scripts'); warnings.filterwarnings('ignore')
from p7_full_ladder import build

# economy label -> ISO3 (extend as needed to cover all 50)
ISO = {'Japan': 'JPN', 'Korea': 'KOR', 'Singapore': 'SGP', 'Taiwan': 'TWN',
       'HongKong': 'HKG', 'Israel': 'ISR', 'SaudiArabia': 'SAU',
       'Qatar': 'QAT', 'China': 'CHN', 'Malaysia': 'MYS', 'Vietnam': 'VNM',
       'India': 'IND', 'Indonesia': 'IDN', 'Nepal': 'NPL', 'Cambodia': 'KHM',
       'Fiji': 'FJI', 'SolomonIslands': 'SLB', 'PapuaNewGuinea': 'PNG'}


def gni(iso):
    url = (f'https://api.worldbank.org/v2/country/{iso}/indicator/'
           f'NY.GNP.PCAP.CD?format=json&per_page=100')
    with urllib.request.urlopen(url, timeout=30) as r:
        js = json.load(r)
    for row in js[1]:
        if row['value'] is not None:
            return row['value'], row['date']
    return None, None


df, _ = build()
adopt = df.groupby('economy').dai.mean() * 100
rows = []
for econ, a in adopt.items():
    iso = ISO.get(econ)
    if not iso:
        continue
    try:
        v, yr = gni(iso)
        if v:
            rows.append((econ, a, v, yr))
    except Exception as e:
        print(f'  {econ}: {e}')
t = pd.DataFrame(rows, columns=['economy', 'adoption_pct', 'gni_pc', 'year'])
t['ln_gni'] = np.log(t.gni_pc)
r = t.adoption_pct.corr(t.ln_gni)
print(t.sort_values('gni_pc').to_string(index=False))
print(f'\nCorrelation(adoption %, ln GNI/capita) = {r:+.3f}  (n={len(t)} economies)')
print('Expected: strong positive -> the digital divide tracks income.')

#!/usr/bin/env python3
"""JED paper — robustness battery + saturation test + margins. Reproducible."""
import sys, warnings, numpy as np, pandas as pd
sys.path.insert(0,'scripts'); warnings.filterwarnings('ignore')
from p7_full_ladder import build
import pyfixest as pf
from scipy import stats
df,_=build()
df['lnlp_raw']=df['lp_z']  # already z; for winsor variant we re-derive below not needed
out=['# JED paper — robustness, saturation test, margins (computed)','']

def coef(fml,d,k='dai'):
    d=d.dropna(subset=['lp_z']+[t.strip() for t in fml.split('~')[1].split('|')[0].split('+')])
    f=pf.feols(fml,data=d,vcov={'CRV1':'economy'}); 
    return f.coef()[k],f.pvalue()[k],int(f._N)

out+=['## Robustness: pooled DAI premium under alternative specs','',
      '| spec | DAI premium | p | N |','|---|--:|--:|--:|']
specs=[('baseline (DAI only)','lp_z ~ dai | economy + year'),
       ('+ TCI','lp_z ~ dai + tci_z | economy + year'),
       ('+ size, age, FDI','lp_z ~ dai + tci_z + ln_size + ln_age + fdi10 | economy + year'),
       ('domestic-owned only','lp_z ~ dai + tci_z + ln_size + ln_age | economy + year')]
for name,fml in specs:
    d=df[df.fdi10==0] if 'domestic' in name else df
    b,p,n=coef(fml,d); out.append(f'| {name} | {b:+.3f} | {p:.3f} | {n} |')

# DAI x size interaction
d=df.dropna(subset=['lp_z','dai','ln_size','tci_z']).copy()
d['lnsz_z']=(d.ln_size-d.ln_size.mean())/d.ln_size.std(); d['dXs']=d.dai*d.lnsz_z
f=pf.feols('lp_z ~ dai + lnsz_z + dXs + tci_z | economy + year',data=d,vcov={'CRV1':'economy'})
out+=['','## Does the digital dividend differ by firm size? (DAI x ln size)','',
      f"- DAI main = {f.coef()['dai']:+.3f} (p={f.pvalue()['dai']:.3f})",
      f"- DAI x size = {f.coef()['dXs']:+.3f} (p={f.pvalue()['dXs']:.3f})  "
      f"({'smaller firms gain more' if f.coef()['dXs']<0 else 'larger firms gain more'})"]

# Saturation test: regime adoption vs regime premium (6 points)
GRP={1:'I',2:'II',3:'III',4:'IV',5:'V',6:'VI'}
ad,pr=[],[]
for g in sorted(df.grp.dropna().unique()):
    s=df[df.grp==g]; ad.append(100*s.dai.mean())
    sd=s.dropna(subset=['lp_z','dai'])
    pr.append(pf.feols('lp_z ~ dai | economy + year',data=sd,vcov={'CRV1':'economy'}).coef()['dai'])
r,p=stats.pearsonr(ad,pr)
out+=['','## Digital-saturation test (regime adoption vs regime premium, k=6)','',
      f'- adoption %: {[round(x,1) for x in ad]}',
      f'- premium  : {[round(x,3) for x in pr]}',
      f'- Pearson r(adoption, premium) = {r:+.3f} (p={p:.3f}); negative => '
      f'saturation (higher adoption, smaller marginal premium)']

# Adoption over time
df['period']=pd.cut(df.year,[2002,2009,2015,2025],labels=['2003-09','2010-15','2016-25'])
out+=['','## Web adoption over time (all 50 economies)','',
      '| period | adoption % | N |','|---|--:|--:|']
for per,s in df.groupby('period'):
    out.append(f'| {per} | {100*s.dai.mean():.1f} | {int(s.dai.notna().sum())} |')
open('jed_ai_digital/replication/jed_robustness_results.md','w').write('\n'.join(out)+'\n')
print('\n'.join(out))

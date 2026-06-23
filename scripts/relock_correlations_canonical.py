#!/usr/bin/env python3
"""Canonical re-lock of the ICRV Pearson-correlation table (CD1 Bang 2.3.8.1 /
thesis section 4.1.6): Pearson r of LP-z (z-scored ln(d2/l1) within economy-year)
vs FDI>=10% (b2b), FSTS (d3b+d3c), TCI (mean of R&D h8 + ISO b8), DAI (website
c22b), by ICRV group, on the same 50-economy raw frame as
relock_descriptives_canonical.py (includes China-2012 + all four Azerbaijan waves).
Out: data_wbes/analysis/correlations_canonical_50econ.csv
"""
import sys, glob; sys.path.insert(0,'scripts')
import numpy as np, pandas as pd, warnings; warnings.filterwarnings('ignore')
from wbes_canon import parse
from cd1_descriptives_pipeline import icrv_map
try: from scipy.stats import pearsonr; HAVE_SP=True
except Exception: HAVE_SP=False
icrv=icrv_map()
ORDER=["Advanced_innovation","Advanced_resource","Upper_mid","Lower_mid_transition","Emerging","SIDS_small"]
COLS=['d2','l1','b2b','d3b','d3c','h8','b8','c22b']; MISSING=[-9,-8,-7,-6,-5,-4]
def read(p):
    try:
        import pyreadstat; d,_=pyreadstat.read_dta(p,usecols=COLS); return d.apply(pd.to_numeric,errors='coerce')
    except Exception:
        try: d=pd.read_stata(p,convert_categoricals=False); return d[[c for c in COLS if c in d]].apply(pd.to_numeric,errors='coerce')
        except Exception: return None
chosen={}
for f in glob.glob('data_wbes/raw_dta/*.dta'):
    m=parse(f)
    if m is None or not m['standard'] or m['panel'] or icrv.get(m['country']) is None: continue
    chosen.setdefault((m['country'],m['year']),f)
rows=[]
for (c,y),f in chosen.items():
    d=read(f)
    if d is None or 'd2' not in d or 'l1' not in d: continue
    d=d.where(~d.isin(MISSING))
    lp=np.log(d['d2'].where(d['d2']>0)/d['l1'].where(d['l1']>0))
    lo,hi=lp.quantile([0.01,0.99]); lp=lp.clip(lo,hi)
    fsts=(d.get('d3b',pd.Series(index=d.index,dtype=float)).where(lambda s:s.between(0,100)).fillna(0)
          +d.get('d3c',pd.Series(index=d.index,dtype=float)).where(lambda s:s.between(0,100)).fillna(0))
    b=d.get('d3b'); cc=d.get('d3c')
    fsts=fsts.where((b.between(0,100) if b is not None else False)|(cc.between(0,100) if cc is not None else False))
    fo=d['b2b'].where(d['b2b'].between(0,100)) if 'b2b' in d else pd.Series(index=d.index,dtype=float)
    fdi=(fo>=10).astype(float).where(fo.notna())
    rd=(d['h8']==1).astype(float).where(d['h8'].isin([1,2])) if 'h8' in d else pd.Series(index=d.index,dtype=float)
    iso=(d['b8']==1).astype(float).where(d['b8'].isin([1,2])) if 'b8' in d else pd.Series(index=d.index,dtype=float)
    tci=pd.concat([rd,iso],axis=1).mean(axis=1)
    dai=(d['c22b']==1).astype(float).where(d['c22b'].isin([1,2])) if 'c22b' in d else pd.Series(index=d.index,dtype=float)
    rec=pd.DataFrame({'g':icrv[c],'ey':f'{c}-{y}','lp':lp,'FDI':fdi,'FSTS':fsts,'TCI':tci,'DAI':dai})
    rows.append(rec)
df=pd.concat(rows,ignore_index=True)
# LP-z within economy-year
def z(s):
    sd=s.std(); return (s-s.mean())/sd if sd and sd>0 else s*np.nan
df['lpz']=df.groupby('ey')['lp'].transform(z)
def star(p):
    return '**' if p<0.01 else ('*' if p<0.05 else ' ns')
def corr(a,b):
    m=a.notna()&b.notna(); n=int(m.sum())
    if n<3 or b[m].std()==0: return (np.nan,1.0,n)
    if HAVE_SP: r,p=pearsonr(a[m],b[m])
    else:
        r=np.corrcoef(a[m],b[m])[0,1]; t=r*np.sqrt((n-2)/max(1e-12,1-r*r))
        from math import erf; p=2*(1-0.5*(1+erf(abs(t)/np.sqrt(2))))
    return (r,p,n)
print(f"{'group':22s}  nLPz   FDI        FSTS       TCI        DAI")
for g in ORDER:
    s=df[df.g==g]; nlpz=int(s['lpz'].notna().sum())
    cells=[]
    for col in ['FDI','FSTS','TCI','DAI']:
        r,p,n=corr(s['lpz'],s[col]); cells.append(f"{r:+.3f}{star(p)}")
    print(f"{g:22s} {nlpz:6d}  "+"  ".join(f"{c:9s}" for c in cells))

recs=[]
for g in ORDER:
    s=df[df.g==g]; row={'group':g,'n_lpz':int(s['lpz'].notna().sum())}
    for col in ['FDI','FSTS','TCI','DAI']:
        r,p,n=corr(s['lpz'],s[col]); row[col+'_r']=round(r,3); row[col+'_p']=round(p,4)
    recs.append(row)
pd.DataFrame(recs).to_csv('data_wbes/analysis/correlations_canonical_50econ.csv',index=False)
print('saved -> data_wbes/analysis/correlations_canonical_50econ.csv')

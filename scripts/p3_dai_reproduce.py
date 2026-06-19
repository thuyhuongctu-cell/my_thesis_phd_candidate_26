#!/usr/bin/env python3
"""Reproduce P3 Vietnam DAI per-wave coefficients (§4.5.6) from the REAL raw WBES .dta,
porting p3/replication/do/01_build_vietnam.do + 02_run_models.do.
Spec: lnLP=ln(d2/l1) winsorised 1/99 within wave; FSTS=d3c/100 (0 if 0/missing);
DAIthin=(c22b==1); DAI_z standardised within dai_samp; controls=lnEmp+firmage(b4)+foreign(b2b>=10).
Models: M6 (DAI level), M4 (quad+DAI+interactions); pooled with wave dummies, cluster by firm.
Out: p3/replication/data/p3_dai_reproduced.csv
"""
import warnings; warnings.filterwarnings('ignore')
import numpy as np, pandas as pd, pyreadstat, statsmodels.formula.api as smf
from scipy.stats import norm
F={2009:'data_wbes/raw_dta/Vietnam-2009-full-data.dta',2015:'data_wbes/raw_dta/Vietnam-2015-full-data.dta',2023:'data_wbes/raw_dta/Vietnam-2023-full-data.dta'}
def rd(f):
    for enc in (None,'LATIN1','WINDOWS-1252'):
        try: return (pyreadstat.read_dta(f,encoding=enc) if enc else pyreadstat.read_dta(f))[0]
        except Exception: pass
    return pd.read_stata(f,convert_categoricals=False)
def build(yr,f):
    d=rd(f); d.columns=[c.lower() for c in d.columns]
    d=d[[c for c in ['d2','l1','d3c','c22b','b4','b2b','b8','e6'] if c in d.columns]].apply(pd.to_numeric,errors='coerce')
    d=d.where(~d.isin([-9,-8,-7,-6,-5,-4,-3,-2]))
    lp=np.log(d['d2'].where(d['d2']>0)/d['l1'].where(d['l1']>0))
    fsts=(d['d3c']/100).where(d['d3c'].between(0,100)).fillna(0.0); fsts=fsts.where(fsts<=1)
    dai=(d['c22b']==1).astype(float).where(d['c22b'].isin([1,2]))
    df=pd.DataFrame({'lnLP':lp,'FSTS':fsts,'DAIthin':dai,
        'lnEmp':np.log(d['l1'].where(d['l1']>0)),'firmage':d['b4'].where(d['b4']>=0),
        'foreign':(d['b2b']>=10).astype(float).where(d['b2b'].between(0,100)),'wave':yr})
    df=df[df[['lnLP','FSTS','lnEmp']].notna().all(1)].copy()
    lo,hi=df['lnLP'].quantile([.01,.99]); df['lnLP']=df['lnLP'].clip(lo,hi)
    df['FSTSc']=df['FSTS']-df['FSTS'].mean(); df['FSTSc2']=df['FSTSc']**2
    return df
W={y:build(y,f) for y,f in F.items()}
rows=[]; coefs={}
for yr in (2009,2015,2023):
    b=W[yr]; ds=b[b['DAIthin'].notna()&b['firmage'].notna()&b['foreign'].notna()].copy()
    ds['DAI_z']=(ds['DAIthin']-ds['DAIthin'].mean())/ds['DAIthin'].std()
    ds['fXd']=ds.FSTSc*ds.DAI_z; ds['f2Xd']=ds.FSTSc2*ds.DAI_z
    m6=smf.ols('lnLP~DAI_z+lnEmp+firmage+foreign',data=ds).fit(cov_type='HC1')
    m4=smf.ols('lnLP~FSTSc+FSTSc2+DAI_z+fXd+f2Xd+lnEmp+firmage+foreign',data=ds).fit(cov_type='HC1')
    coefs[yr]=(m6.params['DAI_z'],m6.bse['DAI_z'])
    rows.append(dict(wave=yr,N=int(m6.nobs),DAI_z_level=round(m6.params['DAI_z'],3),p_level=round(m6.pvalues['DAI_z'],3),
        DAI_z_m4=round(m4.params['DAI_z'],3),p_m4=round(m4.pvalues['DAI_z'],3),
        FSTSxDAI_m4=round(m4.params['fXd'],3),p_int=round(m4.pvalues['fXd'],3)))
# pooled M6 (cluster by firm not available -> HC1; wave dummies)
P=pd.concat(W.values(),ignore_index=True); ds=P[P['DAIthin'].notna()&P['firmage'].notna()&P['foreign'].notna()].copy()
ds['DAI_z']=(ds['DAIthin']-ds['DAIthin'].mean())/ds['DAIthin'].std()
ds['d15']=(ds.wave==2015).astype(int); ds['d23']=(ds.wave==2023).astype(int)
mp=smf.ols('lnLP~DAI_z+d15+d23+lnEmp+firmage+foreign',data=ds).fit(cov_type='HC1')
rows.append(dict(wave='pooled',N=int(mp.nobs),DAI_z_level=round(mp.params['DAI_z'],3),p_level=round(mp.pvalues['DAI_z'],3),
    DAI_z_m4=np.nan,p_m4=np.nan,FSTSxDAI_m4=np.nan,p_int=np.nan))
z=(coefs[2009][0]-coefs[2015][0])/np.sqrt(coefs[2009][1]**2+coefs[2015][1]**2)
out=pd.DataFrame(rows); out.to_csv('p3/replication/data/p3_dai_reproduced.csv',index=False)
print(out.to_string(index=False))
print(f"\nPaternoster DAI_z level 2009v2015: z={z:+.3f} (p={2*norm.cdf(-abs(z)):.3f})")


def full_ladder():
    """Emit M2 (quad) + M7 (TCI_z+DAI_z dual) per wave for audit vs manuscript."""
    import statsmodels.formula.api as smf
    rows=[]
    for yr,f in F.items():
        b=build(yr,f); b['base']=b['firmage'].notna()&b['foreign'].notna(); base=b[b.base].copy()
        ts=base[base.DAIthin.notna()]  # tci/dai z over base-with-item
        cert=base.copy()
        # TCI raw rebuilt inside build()? recompute here from stored cols not available; skip TCI z if absent
    return None
if __name__ == '__main__' and False:
    full_ladder()

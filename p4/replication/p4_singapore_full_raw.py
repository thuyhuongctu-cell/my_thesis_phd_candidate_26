#!/usr/bin/env python3
"""P4 Singapore — FULL canonical re-derivation from raw WBES .dta (no winsor).
Single source of truth for every reported number in the P4 manuscripts:
Table 2 (M0-M8 ladder), M2 turning point + delta CI + bootstrap, Table 4 DAI
marginal effects, Cohen's f2, Heckman IMR, exporters-only R5, Lind-Mehlum.
Run:  python3 p4/replication/p4_singapore_full_raw.py
"""
import pyreadstat, pandas as pd, numpy as np, warnings, os
from statsmodels.formula.api import ols, probit
from scipy.stats import norm
warnings.filterwarnings('ignore'); rng=np.random.default_rng(20260624)

RAW=os.environ.get('WBES_RAW', os.path.join(os.path.dirname(os.path.abspath(__file__)),'..','..','data_wbes','raw_dta'))
df,_=pyreadstat.read_dta(os.path.join(RAW,'Singapore-2023-full-data.dta')); df=df.copy()
for c in df.columns:
    if pd.api.types.is_numeric_dtype(df[c]): df[c]=df[c].replace([-9,-8,-7,-6],np.nan)
df['lnLP']=np.where((df['d2']>0)&(df['l1']>0),np.log(df['d2']/df['l1']),np.nan)
df['FSTS']=np.where(df['d3c'].notna(),df['d3c']/100,np.nan)
df['lnEmp']=np.where(df['l1']>0,np.log(df['l1']),np.nan)
df['firmage']=np.where((df['b5']>1900)&(df['b5']<=2023),2023-df['b5'],np.nan)
df['foreigndum']=np.where(df['b2b'].notna(),(df['b2b']>0).astype(float),np.nan)
df['sec_mfg']=(df['a4a']==1).astype(float); df['sec_constr']=(df['a4a']==2).astype(float)
for it in ['b8','e6','h1']: df[f'{it}_bin']=np.where(df[it]==1,1.0,np.where(df[it]==2,0.0,np.nan))
mat=pd.DataFrame({it:df[f'{it}_bin'] for it in ['b8','e6','h1']})
for c in mat: m,s=mat[c].mean(),mat[c].std(); mat[c]=(mat[c]-m)/s if s>0 else 0.0
comp=mat.mean(axis=1); comp[mat.notna().sum(axis=1)<2]=np.nan
m,s=comp.mean(),comp.std(); df['TCI_z']=(comp-m)/s
df['c22b_bin']=np.where(df['c22b']==1,1.0,np.where(df['c22b']==2,0.0,np.nan))
matd=pd.DataFrame({it:df[it] for it in ['c22b_bin','k33','k38']})
for c in matd: m,s=matd[c].mean(),matd[c].std(); matd[c]=(matd[c]-m)/s if s>0 else matd[c]
compd=matd.mean(axis=1); compd[matd.notna().sum(axis=1)<2]=np.nan
m,s=compd.mean(),compd.std(); df['DAI_z']=(compd-m)/s
fm=df.loc[df['FSTS'].notna(),'FSTS'].mean()
df['FSTS_c']=df['FSTS']-fm; df['FSTSsq_c']=df['FSTS_c']**2
CTRL='lnEmp + firmage + foreigndum + sec_mfg + sec_constr'
BASE=['lnLP','FSTS_c','FSTSsq_c','lnEmp','firmage','foreigndum','sec_mfg','sec_constr']
def star(p): return '\\*\\*\\*' if p<.001 else '\\*\\*' if p<.01 else '\\*' if p<.05 else '†' if p<.10 else ''
def samp(extra): return df[df[BASE+extra].notna().all(axis=1)].copy()
def fit(f,extra): return ols(f,samp(extra)).fit(cov_type='HC1')

LADDER=[('M0Ctrl',f'lnLP ~ {CTRL}',[]),
 ('M2Inv-U',f'lnLP ~ FSTS_c + FSTSsq_c + {CTRL}',[]),
 ('M5+TCI',f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + {CTRL}',['TCI_z']),
 ('M6+DAI',f'lnLP ~ FSTS_c + FSTSsq_c + DAI_z + {CTRL}',['DAI_z']),
 ('M7T+D',f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + {CTRL}',['TCI_z','DAI_z']),
 ('M4DAI×',f'lnLP ~ FSTS_c + FSTSsq_c + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL}',['DAI_z']),
 ('M8Full',f'lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + {CTRL}',['TCI_z','DAI_z'])]
F={lab:fit(f,e) for lab,f,e in LADDER}; labs=[l for l,_,_ in LADDER]

print("="*72,"\nTABLE 2 (markdown, raw)\n","="*72,sep="")
print("| Variable | "+" | ".join(labs)+" |"); print("|"+"---|"*(len(labs)+1))
def cl(l,t): m=F[l]; return f"{m.params[t]:+.3f}{star(m.pvalues[t])}" if t in m.params else ' '
def se(l,t): m=F[l]; return f"({m.bse[t]:.3f})" if t in m.params else ' '
for nm,t in [('FSTS','FSTS_c'),('FSTS²','FSTSsq_c'),('TCI (z)','TCI_z'),('DAI (z)','DAI_z'),
             ('FSTS × DAI','FSTS_c:DAI_z'),('FSTS² × DAI','FSTSsq_c:DAI_z'),
             ('Firm size (ln)','lnEmp'),('Firm age','firmage'),('Foreign-owned','foreigndum'),('Constant','Intercept')]:
    print(f"| {nm} | "+" | ".join(cl(l,t) for l in labs)+" |")
    if t in ('FSTS_c','FSTSsq_c','TCI_z','DAI_z','FSTS_c:DAI_z','FSTSsq_c:DAI_z'):
        print(f"|  | "+" | ".join(se(l,t) for l in labs)+" |")
print("| Sector FE | "+" | ".join('Yes' for _ in labs)+" |")
print("| N | "+" | ".join(str(int(F[l].nobs)) for l in labs)+" |")
print("| R² | "+" | ".join(f"{F[l].rsquared:.3f}" for l in labs)+" |")
print("| Adj. R² | "+" | ".join(f"{F[l].rsquared_adj:.3f}" for l in labs)+" |")

# M2 turning point + delta CI + bootstrap
m2=F['M2Inv-U']; b1,b2=m2.params['FSTS_c'],m2.params['FSTSsq_c']
tpc=-b1/(2*b2); tp=tpc+fm; cov=m2.cov_params(); g1=-1/(2*b2); g2=b1/(2*b2**2)
seTP=np.sqrt(g1**2*m2.bse['FSTS_c']**2+g2**2*m2.bse['FSTSsq_c']**2+2*g1*g2*cov.loc['FSTS_c','FSTSsq_c'])
print("\n"+"="*72,"\nM2 TURNING POINT\n","="*72,sep="")
print(f"  b1={b1:+.4f} (p={m2.pvalues['FSTS_c']:.4f}), b2={b2:+.4f} (p={m2.pvalues['FSTSsq_c']:.4f})")
print(f"  centered TP = {tpc:.3f}; + mean {fm:.3f} => TP = {tp*100:.1f}%")
print(f"  delta-method 95% CI = [{(tp-1.96*seTP)*100:.1f}%, {(tp+1.96*seTP)*100:.1f}%]")
db=samp([]).reset_index(drop=True); n=len(db); Fm='lnLP ~ FSTS_c + FSTSsq_c + '+CTRL
tps=[]; invU=0; B=5000
for _ in range(B):
    s=db.iloc[rng.integers(0,n,n)]; mb=ols(Fm,s).fit(); bb1,bb2=mb.params['FSTS_c'],mb.params['FSTSsq_c']
    if bb2<0: invU+=1; tps.append((-bb1/(2*bb2))+fm)
tps=np.array(tps); p25,p975=np.percentile(tps,[2.5,97.5]); q1,q3=np.percentile(tps,[25,75])
print(f"  bootstrap B={B}: inverted-U(b2<0) {invU/B*100:.1f}%; median {np.median(tps)*100:.0f}%, IQR [{q1*100:.0f}%, {q3*100:.0f}%]")
print(f"  bootstrap percentile CI [2.5,97.5] = [{p25*100:.0f}%, {p975*100:.0f}%]")
# Lind-Mehlum (Sasabuchi intersection-union)
xL,xH=db['FSTS_c'].min(),db['FSTS_c'].max()
def slope_se(x):
    s=b1+2*b2*x; v=m2.bse['FSTS_c']**2+(2*x)**2*m2.bse['FSTSsq_c']**2+2*(2*x)*cov.loc['FSTS_c','FSTSsq_c']; return s,np.sqrt(v)
sL,seL=slope_se(xL); sH,seH=slope_se(xH)
pL=1-norm.cdf(sL/seL); pH=norm.cdf(sH/seH); pLM=max(pL,pH)
print(f"  Lind-Mehlum: slope@min {sL:+.3f}(p_pos={pL:.3f}), slope@max {sH:+.3f}(p_neg={pH:.3f}) -> inverted-U p={pLM:.3f}")

# Table 4: M8 DAI marginal effects
m8=F['M8Full']; c8=m8.cov_params(); idx=list(m8.params.index)
iD,i1,i2=idx.index('DAI_z'),idx.index('FSTS_c:DAI_z'),idx.index('FSTSsq_c:DAI_z')
print("\n"+"="*72,"\nTABLE 4: M8 marginal effect of DAI across FSTS\n","="*72,sep="")
print("| FSTS level | ME | SE | p | 95% CI |"); print("|---|---|---|---|---|")
for lv in [0,5,10,15,20,30,50,70,100]:
    xc=lv/100-fm; me=m8.params['DAI_z']+m8.params['FSTS_c:DAI_z']*xc+m8.params['FSTSsq_c:DAI_z']*xc**2
    v=c8.iloc[iD,iD]+xc**2*c8.iloc[i1,i1]+xc**4*c8.iloc[i2,i2]+2*xc*c8.iloc[iD,i1]+2*xc**2*c8.iloc[iD,i2]+2*xc**3*c8.iloc[i1,i2]
    s=np.sqrt(v); p=2*(1-norm.cdf(abs(me/s)))
    st='\\*\\*\\*' if p<.001 else '\\*\\*' if p<.01 else '\\*' if p<.05 else ''
    print(f"| FSTS = {lv}% | {me:+.3f} | {s:.3f} | {p:.3f}{st} | [{me-1.96*s:+.3f}, {me+1.96*s:+.3f}] |")

# Cohen's f2
def r2(l): return F[l].rsquared
f2_tci=(r2('M5+TCI')-r2('M2Inv-U'))/(1-r2('M5+TCI'))
f2_dai=(r2('M8Full')-r2('M7T+D'))/(1-r2('M8Full'))
print("\n"+"="*72,"\nEFFECT SIZES / DIAGNOSTICS\n","="*72,sep="")
print(f"  Cohen f2 TCI (M2->M5+TCI) = {f2_tci:.3f}")
print(f"  Cohen f2 DAI block (M7->M8) = {f2_dai:.3f}")
# Heckman IMR (extensive-margin export participation)
dpr=samp([]).copy(); dpr['exp_pos']=(dpr['FSTS']>0).astype(int)
pm=probit('exp_pos ~ lnEmp + firmage + sec_mfg + sec_constr',dpr).fit(disp=0)
xb=pm.fittedvalues; dpr['IMR']=norm.pdf(xb)/norm.cdf(xb)
dh=dpr[dpr[['TCI_z','DAI_z']].notna().all(axis=1)].copy()
mh=ols('lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + IMR + '+CTRL,dh).fit(cov_type='HC1')
print(f"  Heckman IMR coef = {mh.params['IMR']:+.3f} (SE {mh.bse['IMR']:.3f}, p={mh.pvalues['IMR']:.3f})")
print(f"    delta on FSTS²×DAI: {m8.params['FSTSsq_c:DAI_z']:.3f} -> {mh.params['FSTSsq_c:DAI_z']:.3f} (|Δ|={abs(m8.params['FSTSsq_c:DAI_z']-mh.params['FSTSsq_c:DAI_z']):.3f})")
print(f"    delta on TCI:       {m8.params['TCI_z']:.3f} -> {mh.params['TCI_z']:.3f} (|Δ|={abs(m8.params['TCI_z']-mh.params['TCI_z']):.3f})")
# Exporters-only R5
de=samp(['TCI_z','DAI_z']); de=de[de['FSTS']>0].copy()
mr=ols('lnLP ~ FSTS_c + FSTSsq_c + TCI_z + DAI_z + FSTS_c:DAI_z + FSTSsq_c:DAI_z + '+CTRL,de).fit(cov_type='HC1')
ft=mr.f_test('FSTS_c:DAI_z = 0, FSTSsq_c:DAI_z = 0')
print(f"  Exporters-only R5: N={int(mr.nobs)}; FSTS²×DAI={mr.params['FSTSsq_c:DAI_z']:+.3f}; joint F={float(ft.fvalue):.2f}, p={float(ft.pvalue):.3f}")
print(f"\nfsts_mean={fm*100:.2f}%  |  done.")

# ── Extra specs cited in prose ──
print("\n"+"="*72,"\nEXTRA SPECS\n","="*72,sep="")
# (a) M8 DAI-block joint F (canonical "4.56")
jf=m8.f_test('FSTS_c:DAI_z = 0, FSTSsq_c:DAI_z = 0')
print(f"  M8 DAI-block joint F (full N=617) = {float(jf.fvalue):.2f}, p={float(jf.pvalue):.3f}")
# (b) TCI-moderation supplementary model (M3): FSTS+FSTS^2+TCI + TCI interactions
mt=ols('lnLP ~ FSTS_c + FSTSsq_c + TCI_z + FSTS_c:TCI_z + FSTSsq_c:TCI_z + '+CTRL,samp(['TCI_z'])).fit(cov_type='HC1')
jft=mt.f_test('FSTS_c:TCI_z = 0, FSTSsq_c:TCI_z = 0')
print(f"  TCI-moderation: TCI direct β={mt.params['TCI_z']:+.3f} (p={mt.pvalues['TCI_z']:.3f}); TCI-interaction joint F={float(jft.fvalue):.2f}, p={float(jft.pvalue):.3f}")
# (c) Item-swap falsification: move c22b from DAI to TCI; rebuild composites; M8 DAI-block joint F
d2=df.copy()
# TCI* = b8,e6,h1,c22b ; DAI* = k33,k38
def zcomp(cols, src):
    M=pd.DataFrame({c:src[c] for c in cols})
    for c in M: m_,s_=M[c].mean(),M[c].std(); M[c]=(M[c]-m_)/s_ if s_>0 else M[c]
    comp=M.mean(axis=1); comp[M.notna().sum(axis=1)<max(2,len(cols)-1)]=np.nan
    m_,s_=comp.mean(),comp.std(); return (comp-m_)/s_
d2['TCI_s']=zcomp(['b8_bin','e6_bin','h1_bin','c22b_bin'],d2)
d2['DAI_s']=zcomp(['k33','k38'],d2)
d2['FSTS_c']=d2['FSTS']-fm; d2['FSTSsq_c']=d2['FSTS_c']**2
need=BASE+['TCI_s','DAI_s']; ds=d2[d2[need].notna().all(axis=1)].copy()
ms=ols('lnLP ~ FSTS_c + FSTSsq_c + TCI_s + DAI_s + FSTS_c:DAI_s + FSTSsq_c:DAI_s + '+CTRL,ds).fit(cov_type='HC1')
jfs=ms.f_test('FSTS_c:DAI_s = 0, FSTSsq_c:DAI_s = 0')
print(f"  Item-swap (c22b->TCI): DAI*-block joint F={float(jfs.fvalue):.2f}, p={float(jfs.pvalue):.3f}  (N={int(ms.nobs)})")

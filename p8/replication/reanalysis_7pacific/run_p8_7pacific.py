"""P8 re-analysis: 7 genuine Pacific SIDS (drops Comoros [Indian Ocean] and
Timor-Leste [SE Asia]) from the SIDS_small pool. OLS + country/year FE + HC1.
Validated: reproduces the original 9-economy R baseline (M1 beta=-0.403826) exactly.
"""
import pandas as pd, numpy as np
from math import erf, sqrt
DATA="data_wbes/p7/p7_pooled_clean.csv"
PACIFIC7=["Fiji","Kiribati","PapuaNewGuinea","Samoa","SolomonIslands","Tonga","Vanuatu"]
ctrl=["ln_size","firm_age","foreign_own_pct"]
def P(z): return 2*(1-0.5*(1+erf(abs(z)/sqrt(2))))
def run(d,cols,need,fe_country=True):
    d=d.dropna(subset=["ln_labor_prod","fsts"]+need).copy()
    d["fsts_c"]=d.fsts-d.fsts.mean(); d["fsts_c2"]=d["fsts_c"]**2
    parts=[pd.Series(1.0,index=d.index,name="const"),d[cols]]
    if fe_country: parts.append(pd.get_dummies(d.country,prefix="c",drop_first=True).astype(float))
    parts.append(pd.get_dummies(d.year,prefix="y",drop_first=True).astype(float))
    X=pd.concat(parts,axis=1).astype(float); X=X.loc[:,(X.nunique()>1)|(X.columns=="const")]
    y=d["ln_labor_prod"].astype(float).values; Xv=X.values
    inv=np.linalg.pinv(Xv.T@Xv); b=inv@Xv.T@y; e=y-Xv@b; n,k=Xv.shape
    r2=1-(e@e)/(((y-y.mean())**2).sum()); ar2=1-(1-r2)*(n-1)/(n-k)
    V=inv@(Xv.T@(Xv*(e**2)[:,None]))@inv*(n/(n-k)); se=np.sqrt(np.diag(V))
    return {nm:(bb,ss,bb/ss,P(bb/ss)) for nm,bb,ss in zip(X.columns,b,se) if nm in cols},n,r2,ar2
def main():
    df=pd.read_csv(DATA,low_memory=False)
    S=df[df.icrv_label=="SIDS_small"]; S=S[S.country.isin(PACIFIC7)].copy()
    A=S.dropna(subset=["ln_labor_prod","fsts"])
    print("7 Pacific SIDS:",PACIFIC7)
    print(f"analysis N={len(A)} exporters={int((A.fsts>0).sum())} ({100*(A.fsts>0).mean():.1f}%)")
    rows=[]
    for lbl,cols,need,fe in [("M1",["fsts_c"]+ctrl,ctrl,True),
                             ("M2",["fsts_c","fsts_c2"]+ctrl,ctrl,True),
                             ("M3",["fsts_c","fsts_c2","tci_z","dai_z"]+ctrl,ctrl+["tci_z","dai_z"],True),
                             ("YearFE_only",["fsts"]+ctrl,ctrl,False),
                             ("Bivariate",["fsts"],[],False)]:
        r,n,r2,ar2=run(S,cols,need,fe)
        for t,(b,se,tt,p) in r.items():
            rows.append({"model":lbl,"term":t,"beta":round(b,6),"se":round(se,6),"p":round(p,6),"N":n,"R2":round(r2,4)})
    E=S[S.fsts>0]; r,n,_,_=run(E,["fsts_c"]+ctrl,ctrl)
    for t,(b,se,tt,p) in r.items():
        rows.append({"model":"Exporters_only","term":t,"beta":round(b,6),"se":round(se,6),"p":round(p,6),"N":n,"R2":None})
    out=pd.DataFrame(rows); out.to_csv("p8/replication/reanalysis_7pacific/p8_7pacific_coefs.csv",index=False)
    print(out.to_string(index=False))
if __name__=="__main__": main()

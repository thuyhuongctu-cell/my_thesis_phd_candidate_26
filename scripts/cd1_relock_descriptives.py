#!/usr/bin/env python3
"""
CĐ1 descriptive re-lock pipeline (DEDICATED — not P7's pipeline).

Reproduces Chuyên đề 1's firm-performance landscape descriptive tables from raw
WBES .dta files, using CĐ1's documented methodology:
  - Labour productivity  LP = ln(annual sales / permanent full-time workers)
  - Winsorize ln(LP) at 1/99 within each country×year cluster
  - Innovation/capability rates: R&D (h8), ISO cert (b8), product innovation (h1),
    process innovation (h5), website (c22b) — % of firms = Yes
  - Internationalisation: FSTS = d3b + d3c (% export intensity); exporter = FSTS>0
  - FDI≥10% via foreign-ownership share (b6a)
  - Aggregated by the 6-group ICRV scheme (DATA labels: IV=Lower_mid_transition,
    V=Emerging, VI=SIDS_small)

Note on PPP: sd(log LP) within country×year is invariant to a country-level PPP
multiplier (a constant shift in logs), so the dispersion statistic is faithful
without PPP conversion factors. Cross-country LP *levels* would need PPP and are
NOT pooled here.

Usage:
  python3 scripts/cd1_relock_descriptives.py --raw-dir data_wbes/raw_dta \
      --out reviews/cd1_relock_output.csv
"""
from __future__ import annotations
import argparse, logging, re
from pathlib import Path
import numpy as np
import pandas as pd

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger("cd1_relock")

# Variable aliases (priority order) — extends P7's VAR_MAP with innovation vars.
VAR_MAP = {
    "sales":        ["n3", "d2"],
    "workers":      ["l1"],
    "exp_indirect": ["d3b"],
    "exp_direct":   ["d3c"],
    "website":      ["c22b", "e1"],
    "iso":          ["b8"],
    "rd":           ["h8"],          # R&D spending (Yes/No)
    "prod_innov":   ["h1"],          # introduced new/improved product
    "proc_innov":   ["h5"],          # introduced new/improved process
    "foreign_own":  ["b6a"],         # % foreign ownership
}
NEG_CODES = set(range(-9, 0))

ICRV_MAP = {
    "Singapore": 1, "Korea": 1, "Taiwan": 1, "Israel": 1, "HongKong": 1,
    "Bahrain": 2, "Kuwait": 2, "Qatar": 2, "Oman": 2, "SaudiArabia": 2, "Brunei": 2,
    "China": 3, "Malaysia": 3, "Thailand": 3, "Kazakhstan": 3, "Armenia": 3, "Georgia": 3,
    "Vietnam": 4, "Philippines": 4, "Indonesia": 4, "India": 4,
    "Bangladesh": 4, "Pakistan": 4, "Mongolia": 4,
    "Cambodia": 5, "Laos": 5, "Myanmar": 5, "Nepal": 5, "SriLanka": 5,
    "Bhutan": 5, "Maldives": 5, "Afghanistan": 5, "Tajikistan": 5,
    "KyrgyzRepublic": 5, "Uzbekistan": 5, "Turkmenistan": 5,
    "Iraq": 5, "Yemen": 5, "Jordan": 5, "Lebanon": 5, "Azerbaijan": 5,
    "Fiji": 6, "Samoa": 6, "Kiribati": 6, "Tonga": 6,
    "SolomonIslands": 6, "Vanuatu": 6, "PapuaNewGuinea": 6, "TimorLeste": 6,
}
ICRV_LABEL = {1: "Advanced_innovation", 2: "Advanced_resource", 3: "Upper_mid",
              4: "Lower_mid_transition", 5: "Emerging", 6: "SIDS_small"}

def canon_country(stem: str) -> str | None:
    s = re.sub(r"^[0-9a-f]{8}-", "", stem)
    s = re.split(r"[-_]?20[0-9]{2}", s)[0]
    s = re.sub(r"[^A-Za-z]", "", s)
    aliases = {
        "LaoPDR": "Laos", "Lao": "Laos", "LaoInformal": "Laos",
        "KyrgyzRepublic": "KyrgyzRepublic", "Kyrgyzrepublic": "KyrgyzRepublic",
        "KoreaRepublic": "Korea", "KoreaRep": "Korea",
        "TaiwanChina": "Taiwan", "HongKongSARChina": "HongKong",
        "BruneiDarussalam": "Brunei", "TimorLeste": "TimorLeste",
        "SriLanka": "SriLanka", "Turkiye": "Turkey", "Turkey": "Turkey",
        "VietNam": "Vietnam",
    }
    return aliases.get(s, s) if s else None

def extract(df: pd.DataFrame, names: list[str]) -> pd.Series | None:
    low = {c.lower(): c for c in df.columns}
    for n in names:
        if n in low:
            s = pd.to_numeric(df[low[n]], errors="coerce")
            return s.mask(s.isin(NEG_CODES))
    return None

def yes_rate(s: pd.Series | None) -> tuple[float, int]:
    """% Yes for a WBES binary (1=Yes, 2=No) or 0/1 indicator."""
    if s is None:
        return (np.nan, 0)
    s = s.dropna()
    vals = set(s.unique())
    if vals <= {1.0, 2.0}:
        yes = (s == 1)
    elif vals <= {0.0, 1.0}:
        yes = (s == 1)
    else:                      # mixed coding: treat 1 as Yes, 2 as No, drop rest
        s = s[s.isin([1, 2])]; yes = (s == 1)
    return (float(yes.mean()) * 100, int(s.shape[0])) if len(s) else (np.nan, 0)

def process_file(path: Path) -> pd.DataFrame | None:
    country = canon_country(path.stem)
    if country is None or country not in ICRV_MAP:
        log.info(f"  skip (outside ICRV frame): {path.name} -> {country}")
        return None
    m = re.search(r"(20[0-9]{2})", path.stem)
    year = int(m.group(1)) if m else 0
    try:
        df = pd.read_stata(path, convert_categoricals=False)
    except Exception as e:
        log.warning(f"  READ FAIL {path.name}: {str(e)[:80]}")
        return None
    sales, workers = extract(df, VAR_MAP["sales"]), extract(df, VAR_MAP["workers"])
    if sales is None or workers is None:
        log.info(f"  no LP vars (schema {path.name}); innovation-only")
    out = pd.DataFrame(index=df.index)
    if sales is not None and workers is not None:
        w = workers.where(workers > 0); s = sales.where(sales > 0)
        out["ln_lp"] = np.log(s / w)
    di, dd = extract(df, VAR_MAP["exp_indirect"]), extract(df, VAR_MAP["exp_direct"])
    fsts = (di.fillna(0) if di is not None else 0) + (dd.fillna(0) if dd is not None else 0)
    out["fsts"] = pd.to_numeric(fsts, errors="coerce").clip(0, 100) if (di is not None or dd is not None) else np.nan
    fo = extract(df, VAR_MAP["foreign_own"])
    out["fdi10"] = (fo >= 10).astype(float) if fo is not None else np.nan
    out["country"], out["year"] = country, year
    for k in ("website", "iso", "rd", "prod_innov", "proc_innov"):
        out[k] = extract(df, VAR_MAP[k])
    # winsorize ln_lp at 1/99 within this country×year
    if "ln_lp" in out and out["ln_lp"].notna().any():
        lo, hi = out["ln_lp"].quantile([0.01, 0.99])
        out["ln_lp"] = out["ln_lp"].clip(lo, hi)
    return out

def aggregate(frames: list[pd.DataFrame]) -> pd.DataFrame:
    df = pd.concat(frames, ignore_index=True)
    df["icrv_group"] = df["country"].map(ICRV_MAP)
    df["icrv_label"] = df["icrv_group"].map(ICRV_LABEL)
    rows = []
    for g in sorted(df["icrv_group"].dropna().unique()):
        sub = df[df["icrv_group"] == g]
        row = {"group": int(g), "label": ICRV_LABEL[int(g)], "n_firms": len(sub),
               "n_econ": sub["country"].nunique(),
               "sd_log_lp": round(sub["ln_lp"].std(), 3) if sub["ln_lp"].notna().any() else np.nan,
               "fsts_mean": round(sub["fsts"].mean(), 1) if sub["fsts"].notna().any() else np.nan,
               "exporter_pct": round((sub["fsts"] > 0).mean() * 100, 1) if sub["fsts"].notna().any() else np.nan,
               "fdi10_pct": round(sub["fdi10"].mean() * 100, 1) if sub["fdi10"].notna().any() else np.nan}
        for k, lbl in [("rd", "rd_pct"), ("iso", "iso_pct"), ("prod_innov", "prod_innov_pct"),
                       ("proc_innov", "proc_innov_pct"), ("website", "website_pct")]:
            row[lbl] = round(yes_rate(sub[k])[0], 1)
        rows.append(row)
    return pd.DataFrame(rows)

def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--raw-dir", default="data_wbes/raw_dta")
    ap.add_argument("--out", default="reviews/cd1_relock_output.csv")
    a = ap.parse_args()
    files = sorted(Path(a.raw_dir).rglob("*.dta"))
    log.info(f"Found {len(files)} .dta in {a.raw_dir}")
    frames = [f for f in (process_file(p) for p in files) if f is not None]
    if not frames:
        log.error("No usable files."); return
    tbl = aggregate(frames)
    Path(a.out).parent.mkdir(parents=True, exist_ok=True)
    tbl.to_csv(a.out, index=False)
    econ = sorted({c for fr in frames for c in fr["country"].unique()})
    print("\n=== CĐ1 descriptive re-lock (reproducible) ===")
    print(tbl.to_string(index=False))
    print(f"\nEconomies processed ({len(econ)}): {', '.join(econ)}")
    missing = sorted(set(ICRV_MAP) - set(econ))
    print(f"\nEconomies still needed for full re-lock ({len(missing)}): {', '.join(missing)}")
    print(f"\nWritten: {a.out}")

if __name__ == "__main__":
    main()

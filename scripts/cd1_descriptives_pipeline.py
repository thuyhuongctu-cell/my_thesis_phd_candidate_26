#!/usr/bin/env python3
"""CD1 descriptive-table pipeline: multi-variable per-ICRV stats from raw WBES .dta.

Recomputes the CĐ1 §2.3.3–2.3.8 descriptive dimensions (innovation, R&D, ISO,
digital adoption, bribery/corruption, firm structure, FSTS/exporter) on the
canonical 49-economy frame, from the 119 raw country .dta files.

Variables (WBES core, yes=1/no=2 unless noted):
  h1  product innovation (3 yrs)      h5  process innovation (3 yrs)
  h8  R&D spending last FY            b8  internationally-recognized cert (ISO)
  c22b own website                    j7a  % sales paid in informal payments
  j30f corruption obstacle (0-4)      b5   year began operations (age)
  b7a female top manager              b4   any female owners
  d3b/d3c indirect/direct export %    l1   permanent workers

Population: main cross-sections only (panels / Informal / ISBS / ISES / Micro /
TGS excluded). ICRV mapping from data_wbes/p7/p7_pooled_clean.csv.
Outputs:
  data_wbes/analysis/cd1_pipeline_by_icrv.csv      (per-group stats)
  data_wbes/analysis/cd1_pipeline_coverage.csv     (economy coverage per group)
"""
from __future__ import annotations
import glob
import os
import re
import warnings

import numpy as np
import pandas as pd

warnings.filterwarnings("ignore")
try:
    import pyreadstat
    HAVE = True
except Exception:
    HAVE = False

MASTER = "data_wbes/p7/p7_pooled_clean.csv"
RAW = "data_wbes/raw_dta"
DROP_LABELS = ["Philippines_panel", "Nepal_panel", "Mongolia_panel",
               "Comoros", "Cyprus", "Turkey"]
ORDER = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
         "Lower_mid_transition", "Emerging", "SIDS_small"]
GROUP_SIZE = {"Advanced_innovation": 5, "Advanced_resource": 6, "Upper_mid": 6,
              "Lower_mid_transition": 7, "Emerging": 17, "SIDS_small": 8}
COUNTRY_MAP = {
    "HongKong": "HongKong", "Korea": "Korea", "Taiwan": "Taiwan",
    "Lao": "Laos", "Laos": "Laos", "Kyrgyz": "KyrgyzRepublic",
    "Brunei": "Brunei", "Timor": "TimorLeste", "Sri": "SriLanka",
    "Papua": "PapuaNewGuinea", "Solomon": "SolomonIslands",
    "Viet": "Vietnam", "VietNam": "Vietnam", "Turkiye": "Turkey",
}
YESNO = ["h1", "h5", "h8", "b8", "c22b", "b7a", "b4"]
NEED = YESNO + ["j7a", "j30f", "b5", "d3b", "d3c", "l1", "l2", "b2b"]


def icrv_map():
    df = pd.read_csv(MASTER, usecols=["country", "icrv_label"], low_memory=False)
    df = df[~df["country"].isin(DROP_LABELS)]
    return dict(df.dropna().groupby("country")["icrv_label"].first())


def file_country(fn):
    token = re.split(r"[-_0-9]", re.sub(r"\.dta$", "", os.path.basename(fn)))[0]
    return COUNTRY_MAP.get(token, token)


def file_year(fn):
    m = re.search(r"(20\d{2})", os.path.basename(fn))
    return int(m.group(1)) if m else np.nan


def is_main_cross_section(fn):
    b = os.path.basename(fn)
    return not re.search(
        r"_\d{4}_\d{4}|Informal|ISBS|ISES|Micro|TGS|expansion|LongForm", b, re.I)


def read_cols(path, cols):
    if HAVE:
        try:
            df, _ = pyreadstat.read_dta(path, usecols=cols)
            return df
        except Exception:
            pass
    try:
        df = pd.read_stata(path, convert_categoricals=False)
        return df[[c for c in cols if c in df.columns]]
    except Exception:
        return None


def extract(path):
    # probe available columns first
    try:
        if HAVE:
            try:
                _, m = pyreadstat.read_dta(path, metadataonly=True)
                avail = set(m.column_names)
            except Exception:
                with pd.read_stata(path, iterator=True,
                                   convert_categoricals=False) as r:
                    avail = set(r.variable_labels().keys())
        else:
            with pd.read_stata(path, iterator=True,
                               convert_categoricals=False) as r:
                avail = set(r.variable_labels().keys())
    except Exception:
        return None
    cols = [c for c in NEED if c in avail]
    if not cols:
        return None
    df = read_cols(path, cols)
    if df is None or df.empty:
        return None
    d = df.apply(pd.to_numeric, errors="coerce")
    out = pd.DataFrame(index=d.index)
    for v in YESNO:                       # 1=yes, 2=no; negatives = missing
        if v in d:
            out[v] = d[v].where(d[v].isin([1, 2])).map({1: 1.0, 2: 0.0})
    if "j7a" in d:                        # % sales informal payments (0-100)
        out["bribe_pct"] = d["j7a"].where((d["j7a"] >= 0) & (d["j7a"] <= 100))
    if "j30f" in d:                       # obstacle 0-4; major+ = >=3
        ok = d["j30f"].where(d["j30f"].between(0, 4))
        out["corr_major"] = (ok >= 3).astype(float).where(ok.notna())
    if "b5" in d:
        yr = file_year(path)
        age = yr - d["b5"].where(d["b5"].between(1800, yr))
        out["firm_age"] = age.where((age >= 0) & (age <= 200))
    if "b2b" in d:                        # % owned by foreign private entities
        fo = d["b2b"].where(d["b2b"].between(0, 100))
        out["fdi10"] = (fo >= 10).astype(float).where(fo.notna())
    if "l1" in d:                         # SME = <100 permanent workers
        w = d["l1"].where(d["l1"] > 0)
        out["sme"] = (w < 100).astype(float).where(w.notna())
        if "l2" in d:                     # employment CAGR over 3 fiscal years
            w0 = d["l2"].where(d["l2"] > 0)
            cagr = ((w / w0) ** (1 / 3) - 1) * 100
            out["emp_cagr"] = cagr.where(cagr.between(-50, 100))
    if "d3b" in d or "d3c" in d:
        parts = [d[v].where(d[v].between(0, 100)) for v in ("d3b", "d3c") if v in d]
        fsts = parts[0].fillna(0)
        for p in parts[1:]:
            fsts = fsts + p.fillna(0)
        valid = pd.concat(parts, axis=1).notna().any(axis=1)
        fsts = fsts.where(valid & fsts.between(0, 100))
        out["fsts"] = fsts
        out["exporter"] = (fsts > 0).astype(float).where(fsts.notna())
    return out


def main():
    icrv = icrv_map()
    files = [f for f in sorted(glob.glob(f"{RAW}/*.dta"))
             if is_main_cross_section(f)]
    frames = {g: [] for g in ORDER}
    econs = {g: set() for g in ORDER}
    used = 0
    for f in files:
        c = file_country(f)
        g = icrv.get(c)
        if g is None:
            continue
        e = extract(f)
        if e is None or e.empty:
            continue
        frames[g].append(e)
        econs[g].add(c)
        used += 1

    stats, cover = [], []
    for g in ORDER:
        if not frames[g]:
            continue
        d = pd.concat(frames[g], ignore_index=True)
        row = {"group": g, "n_firms": len(d)}
        for v, name in [("h1", "product_innov_pct"), ("h5", "process_innov_pct"),
                        ("h8", "rd_pct"), ("b8", "iso_cert_pct"),
                        ("c22b", "website_pct"), ("b7a", "female_topmgr_pct"),
                        ("b4", "female_owner_pct"), ("exporter", "exporter_pct"), ("fdi10", "fdi10_pct"), ("sme", "sme_pct"),
                        ("corr_major", "corruption_major_pct")]:
            if v in d:
                row[name] = round(100 * d[v].mean(), 1)
        for v, name in [("fsts", "fsts_mean"), ("bribe_pct", "bribe_pct_sales_mean"),
                        ("firm_age", "firm_age_mean"), ("emp_cagr", "emp_cagr_mean")]:
            if v in d:
                row[name] = round(d[v].mean(), 1)
        stats.append(row)
        cover.append({"group": g, "economies_covered": len(econs[g]),
                      "economies_total": GROUP_SIZE[g],
                      "coverage": f"{len(econs[g])}/{GROUP_SIZE[g]}",
                      "list": ", ".join(sorted(econs[g]))})

    s, c = pd.DataFrame(stats), pd.DataFrame(cover)
    print(f"files used: {used}\n")
    print("=== Per-ICRV descriptives (raw pipeline, main cross-sections) ===")
    print(s.to_string(index=False))
    print("\n=== Coverage ===")
    print(c[["group", "coverage", "list"]].to_string(index=False))
    os.makedirs("data_wbes/analysis", exist_ok=True)
    s.to_csv("data_wbes/analysis/cd1_pipeline_by_icrv.csv", index=False)
    c.to_csv("data_wbes/analysis/cd1_pipeline_coverage.csv", index=False)
    print("\nsaved -> data_wbes/analysis/cd1_pipeline_by_icrv.csv, cd1_pipeline_coverage.csv")


if __name__ == "__main__":
    main()

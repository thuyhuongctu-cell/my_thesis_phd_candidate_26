#!/usr/bin/env python3
"""Compute ROS (return on sales) by ICRV group from raw WBES .dta.

ROS = (d2_sales - operating_costs) / d2_sales, a unit-free ratio that is
comparable across countries without currency conversion. Operating costs =
n2a labour + n2b electricity + n2e raw materials + n2f fuel + n2i resale goods.

Population: main cross-section files only (excludes *_panel, Informal/ISBS/
ISES/Micro/TGS special samples) to avoid double counting and population mixing.
ICRV group is mapped per country from data_wbes/p7/p7_pooled_clean.csv.

Output: data_wbes/analysis/cd1_relock_ros_by_icrv.csv
"""
from __future__ import annotations
import glob
import os
import re
import numpy as np
import pandas as pd

try:
    import pyreadstat
    HAVE = True
except Exception:
    HAVE = False

MASTER = "data_wbes/p7/p7_pooled_clean.csv"
RAW = "data_wbes/raw_dta"
COST_VARS = ["n2a", "n2b", "n2e", "n2f", "n2i"]
DROP_LABELS = ["Philippines_panel", "Nepal_panel", "Mongolia_panel",
               "Comoros", "Cyprus", "Turkey"]
ORDER = ["Advanced_innovation", "Advanced_resource", "Upper_mid",
         "Lower_mid_transition", "Emerging", "SIDS_small"]

# filename country token -> master country label
COUNTRY_MAP = {
    "HongKong": "HongKong", "Korea": "Korea", "Taiwan": "Taiwan",
    "Lao": "Laos", "Laos": "Laos", "Kyrgyz": "KyrgyzRepublic",
    "Brunei": "Brunei", "Timor": "TimorLeste", "Sri": "SriLanka",
    "Papua": "PapuaNewGuinea", "Solomon": "SolomonIslands",
    "Viet": "Vietnam", "VietNam": "Vietnam",
}


def master_icrv_map():
    df = pd.read_csv(MASTER, usecols=["country", "icrv_label"], low_memory=False)
    df = df[~df["country"].isin(DROP_LABELS)]
    return dict(df.dropna().groupby("country")["icrv_label"].first())


def file_country(fn):
    base = re.sub(r"\.dta$", "", os.path.basename(fn))
    token = re.split(r"[-_0-9]", base)[0]
    return COUNTRY_MAP.get(token, token)


def is_main_cross_section(fn):
    b = os.path.basename(fn)
    if re.search(r"_\d{4}_\d{4}", b):           # panel (underscore multi-year)
        return False
    if re.search(r"Informal|ISBS|ISES|Micro|TGS|expansion|LongForm", b, re.I):
        return False
    return True


def read_cols(path, cols):
    if HAVE:
        try:
            df, _ = pyreadstat.read_dta(path, usecols=[c for c in cols])
            return df
        except Exception:
            pass
    try:
        return pd.read_stata(path, columns=cols, convert_categoricals=False)
    except Exception:
        return pd.read_stata(path, convert_categoricals=False)[
            [c for c in cols if c]]


def firm_ros(path):
    need = ["d2"] + COST_VARS
    try:
        df = read_cols(path, need)
    except Exception:
        # fall back: read all, subset
        try:
            df = pd.read_stata(path, convert_categoricals=False)
        except Exception:
            return None
    have = [c for c in need if c in df.columns]
    if "d2" not in have or "n2a" not in have or "n2e" not in have:
        return None                              # need sales + core costs
    d = df[have].apply(pd.to_numeric, errors="coerce")
    d = d.mask(d < 0)                            # WBES missing codes (-9/-8/...)
    sales = d["d2"]
    costs = d[[c for c in COST_VARS if c in d.columns]].sum(axis=1, min_count=2)
    ros = (sales - costs) / sales
    ros = ros[(sales > 0) & (costs > 0)]
    return ros.dropna()


def main():
    icrv = master_icrv_map()
    files = [f for f in sorted(glob.glob(f"{RAW}/*.dta")) if is_main_cross_section(f)]
    by_group = {lab: [] for lab in ORDER}
    used = skipped = 0
    for f in files:
        c = file_country(f)
        lab = icrv.get(c)
        if lab is None:
            skipped += 1
            continue
        r = firm_ros(f)
        if r is None or len(r) == 0:
            skipped += 1
            continue
        by_group[lab].append(r)
        used += 1
    rows = []
    allvals = []
    for lab in ORDER:
        if not by_group[lab]:
            continue
        v = pd.concat(by_group[lab])
        lo, hi = v.quantile([0.01, 0.99])
        vw = v.clip(lo, hi)                       # winsorize 1/99
        allvals.append(vw)
        rows.append({"group": lab, "n_firms": len(vw),
                     "ros_mean": round(vw.mean(), 4),
                     "ros_median": round(vw.median(), 4),
                     "ros_sd": round(vw.std(), 4)})
    out = pd.DataFrame(rows)
    print(f"files used: {used}, skipped: {skipped}\n")
    print("=== ROS (winsorized 1/99) by ICRV group, main cross-sections ===")
    print(out.to_string(index=False))
    os.makedirs("data_wbes/analysis", exist_ok=True)
    out.to_csv("data_wbes/analysis/cd1_relock_ros_by_icrv.csv", index=False)
    print("\nsaved -> data_wbes/analysis/cd1_relock_ros_by_icrv.csv")


if __name__ == "__main__":
    main()

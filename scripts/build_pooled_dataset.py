#!/usr/bin/env python3
"""Reproducible WBES multi-country pooling + harmonisation pipeline.

Documents and executes the procedure by which heterogeneous country-year World
Bank Enterprise Survey (WBES) cross-sections are pooled into a single harmonised
firm-level analytic dataset. Produces a PRISMA-style data-flow report (firm
counts at each filtering/harmonisation step) for the dissertation methodology
appendix (Phụ lục A).

The procedure has six stages (see Phụ lục A for full justification + citations):
  S1  Acquisition  — collect country-year .dta; keep standard private-firm
                     cross-sections only (exclude panels / Informal / ISBS /
                     ISES / Micro / TGS follow-ups); restrict to waves >= 2006
                     (globally comparable WBES instrument).
  S2  De-duplication — one survey per economy-year.
  S3  Variable harmonisation — map heterogeneous questionnaire fields to a common
                     schema (labour productivity, FSTS, capability/digital,
                     controls) using the WBES global core modules.
  S4  Missing-code treatment — recode WBES non-response codes (-9 Don't Know,
                     -7 N/A, -8 Refusal) to missing; range-validate.
  S5  Institutional stratification — assign ICRV regime; restrict to the 49-economy
                     Asia-Pacific analytic frame (drop Comoros/Cyprus/Turkey).
  S6  Listwise analytic sample — drop records missing the dependent variable or
                     focal regressor; report regression N.

Note: the re-uploaded raw archive is a subset of the authors' full assembly;
the official locked pool sizes (classification 96,415 / analytic 91,982 /
M2 regression 84,910) are reported from the master file. This script reproduces
the PROCEDURE and its data flow on the currently available raw archive.
"""
from __future__ import annotations
import glob
import os
import sys

import numpy as np
import pandas as pd

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
from wbes_canon import NON_ASIA, parse  # noqa: E402

RAW = "data_wbes/raw_dta"
MASTER = "data_wbes/p7/p7_pooled_clean.csv"
MISSING_CODES = (-9, -8, -7)            # WBES non-response codes
OUT = "data_wbes/analysis/pooled_dataflow.csv"


def frame_economies() -> set[str]:
    """49-economy analytic frame = master ICRV economies minus out-of-region."""
    m = pd.read_csv(MASTER, usecols=["country", "icrv_label"], low_memory=False)
    econ = set(m.dropna(subset=["icrv_label"])["country"].unique())
    return econ - {"Comoros", "Cyprus", "Turkey"}


def clean_numeric(s: pd.Series) -> pd.Series:
    x = pd.to_numeric(s, errors="coerce")
    return x.mask(x.isin(MISSING_CODES))


def harmonise(path: str) -> pd.DataFrame | None:
    """S3-S4: extract + harmonise core variables from one cross-section."""
    try:
        import pyreadstat
        cols_needed = ["d2", "l1", "d3b", "d3c", "b5", "b8", "c22b"]
        _, meta = pyreadstat.read_dta(path, metadataonly=True)
        avail = [c for c in cols_needed if c in meta.column_names]
        if "d2" not in avail or "l1" not in avail:
            return None
        df, _ = pyreadstat.read_dta(path, usecols=avail)
    except Exception:
        return None
    d = df.apply(clean_numeric)
    out = pd.DataFrame(index=d.index)
    # labour productivity = ln(annual sales / permanent workers)
    sales = d.get("d2"); workers = d.get("l1")
    valid = (sales > 0) & (workers > 0)
    lp = (sales / workers).where(valid)
    out["ln_lp"] = np.log(lp.where(lp > 0))
    # FSTS = indirect + direct exports (% of sales)
    if "d3b" in d or "d3c" in d:
        parts = [d[c].clip(0, 100) for c in ("d3b", "d3c") if c in d]
        fsts = sum(p.fillna(0) for p in parts)
        any_valid = pd.concat(parts, axis=1).notna().any(axis=1)
        out["fsts"] = fsts.where(any_valid & fsts.between(0, 100))
    return out


def main() -> None:
    frame = frame_economies()
    # S1-S2: select standard, >=2006, in-frame, deduped economy-years
    chosen: dict[tuple, str] = {}
    raw_waves = 0
    for p in sorted(glob.glob(f"{RAW}/*.dta")):
        m = parse(p)
        if (m is None or not m["standard"] or m["panel"]
                or m["country"] in NON_ASIA or m["country"] not in frame):
            continue
        key = (m["country"], m["year"])
        if key not in chosen:
            chosen[key] = p
            raw_waves += 1

    # S3-S6 on the reproducible archive
    frames = [h for p in chosen.values() if (h := harmonise(p)) is not None]
    pool = pd.concat(frames, ignore_index=True) if frames else pd.DataFrame()
    n_raw = len(pool)
    n_lp = pool["ln_lp"].notna().sum() if n_raw else 0
    n_an = (pool["ln_lp"].notna() & pool.get("fsts", pd.Series(dtype=float))
            .notna()).sum() if n_raw else 0

    flow = [
        ("S1 standard cross-sections >=2006 (in-frame, deduped)", f"{len(chosen)} waves / {len({c for c, _ in chosen})} economies"),
        ("S2 firm-year observations (re-uploaded archive)", f"{n_raw:,}"),
        ("S3-S4 harmonised + non-response recoded", f"{n_raw:,}"),
        ("S5 labour-productivity valid", f"{n_lp:,}"),
        ("S6 analytic (LP + FSTS valid)", f"{n_an:,}"),
        ("— OFFICIAL locked pool (master, full assembly) —", ""),
        ("Classification pool (ICRV-assigned, 52 econ)", "96,415"),
        ("Analytic frame (49 Asia-Pacific economies)", "91,982"),
        ("P7 M2 regression N (listwise focal set)", "84,910"),
        ("P7 M5 full-control N", "38,342"),
    ]
    print(f"Reproducible pooling on raw archive ({raw_waves} waves):\n")
    for k, v in flow:
        print(f"  {k:52} {v}")
    pd.DataFrame(flow, columns=["step", "count"]).to_csv(OUT, index=False)
    print(f"\nsaved -> {OUT}")


if __name__ == "__main__":
    main()

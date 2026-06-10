#!/usr/bin/env python3
"""
05 — Extract innovation columns (h1/h5/h8) from raw WBES .dta files available
in `data_wbes/raw_dta/`. Produces a firm-year delta CSV that can be merged
into p7_pooled_clean.dta (step 06).

Outputs:
  data_wbes/p7/p7_innovation_delta.csv  — long-format with country,year,firm_id,
                                          product_innov, process_innov, rd_spending
  data_wbes/p7/p7_innovation_coverage.csv — country-year level coverage report
"""
from __future__ import annotations

import re
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat

REPO = Path(__file__).resolve().parent.parent.parent
RAW_DIR = REPO / "data_wbes/raw_dta"
OUT_DELTA = REPO / "data_wbes/p7/p7_innovation_delta.csv"
OUT_COVER = REPO / "data_wbes/p7/p7_innovation_coverage.csv"

NEG_CODES = {-9, -8, -7, -6, -5, -4, -3, -2, -1}

NAME_MAP = {
    "Turkiye": "Turkey", "Turkey": "Turkey",
    "Korea-Republic": "Korea", "Korea--Rep.": "Korea", "Korea": "Korea",
    "Lao-PDR": "Laos", "Laos": "Laos",
    "Taiwan-China": "Taiwan", "Taiwan": "Taiwan",
    "Cambodia": "Cambodia", "Cyprus": "Cyprus", "Comoros": "Comoros",
    "Azerbaijan": "Azerbaijan", "India": "India",
}

SKIP_KEYWORDS = ("ISBS", "ISES", "Informal", "Documentation", "Notes")


def parse_country_year(fpath: Path) -> list[tuple[str, int]]:
    """Return list of (country, year) tuples implied by filename."""
    stem = fpath.stem
    m = re.match(r"^([A-Za-z][A-Za-z\-_.]+?)[-_\s]+(\d{4})", stem)
    if not m:
        return []
    raw_country = re.sub(r"[-_.]+$", "", m.group(1))
    country = NAME_MAP.get(raw_country, raw_country)
    years = [int(y) for y in re.findall(r"\d{4}", stem)]
    if not years:
        return []
    return [(country, y) for y in years]


def recode_binary_yn(s: pd.Series) -> pd.Series:
    out = s.copy().astype(float)
    out[out.isin(NEG_CODES)] = np.nan
    out[out == 2] = 0
    out[(out != 0) & (out != 1) & out.notna()] = np.nan
    return out


def read_dta(path: Path) -> pd.DataFrame | None:
    for enc in (None, "latin1", "cp1252"):
        try:
            kw = {"apply_value_formats": False}
            if enc:
                kw["encoding"] = enc
            df, _ = pyreadstat.read_dta(str(path), **kw)
            return df
        except Exception:
            continue
    return None


def detect_year_column(df: pd.DataFrame, candidate_years: list[int]) -> str | None:
    """For panel files: locate a 'year' column matching expected wave years."""
    for cand in ("year", "wave", "panelyear", "syear"):
        if cand in df.columns:
            vals = pd.to_numeric(df[cand], errors="coerce").dropna().unique()
            if any(y in candidate_years for y in vals.astype(int)):
                return cand
    return None


def extract_one_file(fpath: Path) -> list[pd.DataFrame]:
    """Return one or more (country, year)-stamped innov frames per file."""
    if any(kw in fpath.name for kw in SKIP_KEYWORDS):
        return []
    parsed = parse_country_year(fpath)
    if not parsed:
        return []
    df = read_dta(fpath)
    if df is None:
        return []

    h1 = df["h1"] if "h1" in df.columns else None
    h5 = df["h5"] if "h5" in df.columns else None
    h8 = df["h8"] if "h8" in df.columns else None
    if h1 is None and h5 is None and h8 is None:
        return []

    base = pd.DataFrame(index=df.index)
    base["firm_id"] = df["idstd"].astype(str) if "idstd" in df.columns else df.index.astype(str)
    base["product_innov"] = recode_binary_yn(h1) if h1 is not None else np.nan
    base["process_innov"] = recode_binary_yn(h5) if h5 is not None else np.nan
    base["rd_spending"] = recode_binary_yn(h8) if h8 is not None else np.nan

    # Multi-year (panel) file: split by year column if present
    if len(parsed) > 1:
        years_in_name = [y for _, y in parsed]
        ycol = detect_year_column(df, years_in_name)
        if ycol is None:
            # Cannot split — emit single concatenation tagged by smallest year
            country, year = parsed[0]
            base.insert(0, "country", country)
            base.insert(1, "year", year)
            return [base]
        frames = []
        for country, year in parsed:
            mask = pd.to_numeric(df[ycol], errors="coerce").fillna(-1).astype(int) == year
            sub = base.loc[mask].copy()
            sub.insert(0, "country", country)
            sub.insert(1, "year", year)
            frames.append(sub)
        return frames

    country, year = parsed[0]
    base.insert(0, "country", country)
    base.insert(1, "year", year)
    return [base]


def main() -> None:
    files = sorted(RAW_DIR.glob("*.dta"))
    frames: list[pd.DataFrame] = []
    coverage_rows: list[dict] = []
    for fpath in files:
        try:
            sub_frames = extract_one_file(fpath)
        except Exception as e:
            print(f"SKIP {fpath.name}: {e}")
            continue
        for frame in sub_frames:
            country = frame["country"].iloc[0]
            year = int(frame["year"].iloc[0])
            n = len(frame)
            n_h1 = frame["product_innov"].notna().sum()
            n_h5 = frame["process_innov"].notna().sum()
            n_h8 = frame["rd_spending"].notna().sum()
            coverage_rows.append({
                "country": country, "year": year, "source_file": fpath.name,
                "n_firms": n,
                "n_product_innov": int(n_h1),
                "n_process_innov": int(n_h5),
                "n_rd_spending": int(n_h8),
            })
            frames.append(frame)
            print(f"  {country} {year} (n={n}) ← {fpath.name}")

    if not frames:
        print("No innovation data extracted from any file.")
        return

    delta = pd.concat(frames, ignore_index=True)
    delta = delta.dropna(subset=["product_innov", "process_innov", "rd_spending"], how="all")
    delta.to_csv(OUT_DELTA, index=False)
    print(f"\nWrote {OUT_DELTA.relative_to(REPO)} — {len(delta):,} rows, "
          f"{delta['country'].nunique()} countries, "
          f"{delta.groupby(['country','year']).ngroups} country-years")

    pd.DataFrame(coverage_rows).to_csv(OUT_COVER, index=False)
    print(f"Wrote {OUT_COVER.relative_to(REPO)} — {len(coverage_rows)} country-year rows")


if __name__ == "__main__":
    main()

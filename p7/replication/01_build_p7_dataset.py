#!/usr/bin/env python3
"""
P7 Dataset Builder — Harmonize WBES raw .dta files into a pooled analytical file.

Usage:
  python3 01_build_p7_dataset.py [--raw-dir PATH] [--out-dir PATH]

Defaults:
  --raw-dir  data_wbes/raw/           (root of Country/Country_year.dta tree)
  --out-dir  data_wbes/p7/

The script reads each .dta in raw-dir, extracts P7-relevant variables, harmonizes
coding, and writes:
  - p7_pooled_clean.csv    (analytical file, one row per firm)
  - p7_manifest.csv        (country-year coverage + N per wave)
  - p7_variable_log.csv    (per-file variable availability)
"""
import argparse
import csv
import logging
import sys
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat
import warnings
warnings.filterwarnings("ignore")

logging.basicConfig(level=logging.INFO, format="%(levelname)s %(message)s")
log = logging.getLogger(__name__)

# ---------------------------------------------------------------------------
# Variable extraction plan
# ---------------------------------------------------------------------------
# For each target variable, list candidate raw WBES variable names in priority order.
# The first one found in the file is used.
VAR_MAP = {
    # Outcome
    "n3_sales":       ["n3", "d2"],           # total sales last fiscal year
    "l1_workers":     ["l1"],                  # permanent full-time employees

    # Export intensity (FSTS = (d3b+d3c)/100)
    "d3a_domestic":   ["d3a"],                 # % domestic sales
    "d3b_indirect":   ["d3b"],                 # % indirect exports
    "d3c_direct":     ["d3c"],                 # % direct exports

    # DAI components
    "c22b_website":   ["c22b", "e1"],          # has own website
    "k33_epay":       ["k33"],                 # % payments via e-payment

    # TCI components
    "b8_cert":        ["b8"],                  # quality certification
    "e6_foreign_tech":["e6"],                  # uses foreign-licensed technology

    # Top manager
    "b7_mgr_exp":     ["b7"],                  # years experience in sector
    "b7a_mgr_female": ["b7a"],                 # top manager is female

    # Controls
    "b4_female_owner":["b4"],                  # female among owners
    "b6a_foreign_own":["b6a"],                 # % foreign ownership
    "b2a_private_dom":["b2a"],                 # % private domestic ownership
    "b5_year_est":    ["b5"],                  # year established
    "a4a_size_strata":["a4a"],                 # size strata (1=small 2=med 3=large)
    "a6a_isic":       ["a6a", "a6b"],          # ISIC sector
    "b2b_sector":     ["b2b", "b2a"],          # sub-sector detail
    "b1_legal":       ["b1"],                  # legal status
    "wstrict":        ["wstrict"],             # survey weight (strict)
    "wmedian":        ["wmedian"],             # survey weight (median)
}

# WBES negative codes = missing (-9 don't know, -8 other, -6 refuse, -7 only 1 establishment)
NEG_CODES = {-9, -8, -7, -6, -5, -4, -3, -2, -1}

# Country → ICRV regime mapping (from thesis CD1/CD2 ICRV classification)
# Group I=5 advanced-innovation, II=5 advanced-resource, III=6 upper-mid,
# IV=7 lower-mid, V=17 emerging, VI=7 SIDS/small
ICRV_MAP = {
    # Group I — Advanced innovation
    "Singapore": 1, "Korea": 1, "Taiwan": 1, "Israel": 1, "Cyprus": 1,
    "HongKong": 1,   # HK SAR — per dissertation ICRV framework (WGI >+0.80)
    # Group II — Advanced resource
    "Bahrain": 2, "Kuwait": 2, "Qatar": 2, "Oman": 2, "SaudiArabia": 2,
    "Brunei": 2,     # Brunei — advanced resource-driven (oil sultanate, high WGI)
    # Group III — Upper-middle capability
    "China": 3, "Malaysia": 3, "Thailand": 3, "Kazakhstan": 3,
    "Armenia": 3, "Georgia": 3,
    # Group IV — Lower-middle transition
    "Vietnam": 4, "Philippines": 4, "Indonesia": 4, "India": 4,
    "Bangladesh": 4, "Pakistan": 4, "Mongolia": 4,
    # Group V — Emerging/developing
    "Cambodia": 5, "Laos": 5, "Myanmar": 5, "Nepal": 5, "SriLanka": 5,
    "Bhutan": 5, "Maldives": 5, "Afghanistan": 5, "Tajikistan": 5,
    "KyrgyzRepublic": 5, "Uzbekistan": 5, "Turkmenistan": 5,
    "Iraq": 5, "Yemen": 5, "Jordan": 5, "Lebanon": 5,
    # Group VI — Pacific/SIDS/small open economies
    "Fiji": 6, "Samoa": 6, "Kiribati": 6, "Tonga": 6,
    "SolomonIslands": 6, "Vanuatu": 6, "PapuaNewGuinea": 6,
    "TimorLeste": 6,
}

ICRV_LABEL = {
    1: "Advanced_innovation", 2: "Advanced_resource",
    3: "Upper_mid", 4: "Lower_mid_transition",
    5: "Emerging", 6: "SIDS_small",
}

NAME_MAP = {
    # Vietnam
    "VietNam": "Vietnam", "Vietnam": "Vietnam",
    # East Asia
    "HongKongSARChina": "HongKong", "HongKong": "HongKong",
    "TaiwanChina": "Taiwan", "Taiwan": "Taiwan",
    "KoreaRepublic": "Korea", "Korea": "Korea",
    "China": "China",
    # Southeast Asia
    "Singapore": "Singapore",
    "Indonesia": "Indonesia",
    "Philippines": "Philippines",
    "Thailand": "Thailand",
    "Malaysia": "Malaysia",
    "Myanmar": "Myanmar",
    "Cambodia": "Cambodia",
    "BruneiDarussalam": "Brunei", "Brunei": "Brunei",
    "LaoPDR": "Laos", "Laos": "Laos",
    "TimorLeste": "TimorLeste",
    # South Asia
    "India": "India",
    "Bangladesh": "Bangladesh",
    "Pakistan": "Pakistan",
    "SriLanka": "SriLanka",
    "Nepal": "Nepal",
    "Bhutan": "Bhutan",
    "Maldives": "Maldives",
    "Afghanistan": "Afghanistan",
    # Central Asia
    "Kazakhstan": "Kazakhstan",
    "Kyrgyzrepublic": "KyrgyzRepublic", "KyrgyzRepublic": "KyrgyzRepublic",
    "Tajikistan": "Tajikistan",
    "Uzbekistan": "Uzbekistan",
    "Turkmenistan": "Turkmenistan",
    # West Asia / Middle East
    "Armenia": "Armenia",
    "Georgia": "Georgia",
    "Bahrain": "Bahrain",
    "Kuwait": "Kuwait",
    "Qatar": "Qatar",
    "Oman": "Oman",
    "SaudiArabia": "SaudiArabia",
    "Israel": "Israel",
    "Jordan": "Jordan",
    "Lebanon": "Lebanon",
    "Iraq": "Iraq",
    "Yemen": "Yemen",
    "Cyprus": "Cyprus",
    "Republic_of_Cyprus": "Cyprus",
    # Pacific / SIDS
    "Fiji": "Fiji",
    "Samoa": "Samoa",
    "Kiribati": "Kiribati",
    "Tonga": "Tonga",
    "SolomonIslands": "SolomonIslands",
    "Vanuatu": "Vanuatu",
    "PapuaNewGuinea": "PapuaNewGuinea",
    "Mongolia": "Mongolia",
}


def read_dta_robust(path: Path) -> tuple[pd.DataFrame, object]:
    for enc in (None, "latin1", "cp1252", "utf-8"):
        try:
            kw = {"apply_value_formats": False}
            if enc:
                kw["encoding"] = enc
            return pyreadstat.read_dta(str(path), **kw)
        except Exception as e:
            last = e
    raise last


def extract_var(df: pd.DataFrame, candidates: list[str]) -> pd.Series | None:
    for cname in candidates:
        if cname in df.columns:
            return df[cname].copy()
    return None


def recode_binary_yn(s: pd.Series) -> pd.Series:
    """Recode WBES 1=yes 2=no to 1/0; negative codes → NaN."""
    out = s.copy().astype(float)
    out[out.isin(NEG_CODES)] = np.nan
    out[out == 2] = 0  # 2=no → 0
    # 1=yes stays 1
    out[(out != 0) & (out != 1) & out.notna()] = np.nan  # unexpected values
    return out


def recode_pct(s: pd.Series) -> pd.Series:
    """Recode percentage variables; negative codes → NaN."""
    out = s.copy().astype(float)
    out[out.isin(NEG_CODES)] = np.nan
    out[out < 0] = np.nan
    return out


def build_firm_record(df: pd.DataFrame, country: str, year: int, region: str) -> pd.DataFrame:
    """Extract and harmonize P7 variables from a single country-year file."""
    rows = pd.DataFrame(index=df.index)

    # Metadata
    rows["country"] = country
    rows["year"] = year
    rows["region"] = region
    rows["icrv_group"] = ICRV_MAP.get(country, np.nan)
    rows["icrv_label"] = rows["icrv_group"].map(ICRV_LABEL)

    # Firm ID
    for id_var in ("idstd", "id"):
        if id_var in df.columns:
            rows["firm_id"] = df[id_var].astype(str)
            break

    # Sales and employment → ln_labor_prod
    n3 = extract_var(df, ["n3", "d2"])
    l1 = extract_var(df, ["l1"])
    if n3 is not None:
        n3 = recode_pct(n3)
    if l1 is not None:
        l1 = recode_pct(l1)
        l1[l1 <= 0] = np.nan
    if n3 is not None and l1 is not None:
        with np.errstate(divide="ignore", invalid="ignore"):
            rows["ln_labor_prod"] = np.log(n3 / l1)
        rows["ln_labor_prod"] = rows["ln_labor_prod"].replace([np.inf, -np.inf], np.nan)
    else:
        rows["ln_labor_prod"] = np.nan
    rows["n3_sales_raw"] = n3
    rows["l1_workers_raw"] = l1

    # FSTS = (d3b + d3c) / 100  [total export intensity]
    d3a = recode_pct(extract_var(df, ["d3a"])) if "d3a" in df.columns else None
    d3b = recode_pct(extract_var(df, ["d3b"])) if "d3b" in df.columns else None
    d3c = recode_pct(extract_var(df, ["d3c"])) if "d3c" in df.columns else None

    if d3c is not None and d3b is not None:
        rows["fsts"] = (d3b.fillna(0) + d3c.fillna(0)) / 100
        # Flag: firm is an exporter (fsts > 0)
        rows["exporter"] = (rows["fsts"] > 0).astype(int)
    elif d3a is not None:
        # Fallback: fsts = 1 - d3a/100 (total foreign = 1 - domestic)
        rows["fsts"] = 1 - d3a / 100
        rows["exporter"] = (rows["fsts"] > 0).astype(int)
    else:
        rows["fsts"] = np.nan
        rows["exporter"] = np.nan
    rows["fsts_pct"] = rows["fsts"] * 100  # 0–100 scale for reporting

    # DAI
    c22b = extract_var(df, ["c22b", "e1"])
    if c22b is not None:
        rows["dai_website"] = recode_binary_yn(c22b)
    else:
        rows["dai_website"] = np.nan

    k33 = extract_var(df, ["k33"])
    if k33 is not None:
        k33 = recode_pct(k33)
        rows["dai_epay"] = (k33 > 0).astype(float)
        rows["dai_epay"][k33.isna()] = np.nan
        rows["dai_epay_pct"] = k33
    else:
        rows["dai_epay"] = np.nan
        rows["dai_epay_pct"] = np.nan

    # DAI composite (standardized mean of available components)
    dai_components = [c for c in ["dai_website", "dai_epay"] if rows[c].notna().any()]
    if dai_components:
        dai_stack = rows[dai_components]
        dai_means = (dai_stack - dai_stack.mean()) / dai_stack.std()
        rows["dai_z"] = dai_means.mean(axis=1)
    else:
        rows["dai_z"] = np.nan

    # TCI
    b8 = extract_var(df, ["b8"])
    if b8 is not None:
        rows["tci_cert"] = recode_binary_yn(b8)
    else:
        rows["tci_cert"] = np.nan

    e6 = extract_var(df, ["e6"])
    if e6 is not None:
        rows["tci_foreign_tech"] = recode_binary_yn(e6)
    else:
        rows["tci_foreign_tech"] = np.nan

    # TCI composite (standardized mean)
    tci_components = [c for c in ["tci_cert", "tci_foreign_tech"] if rows[c].notna().any()]
    if tci_components:
        tci_stack = rows[tci_components]
        tci_means = (tci_stack - tci_stack.mean()) / tci_stack.std()
        rows["tci_z"] = tci_means.mean(axis=1)
    else:
        rows["tci_z"] = np.nan

    # Innovation module (WBES Section H) — needed for CĐ1 Bảng 2.3.4.1
    # h1 = introduced new/improved product (binary)
    # h5 = introduced new/improved process (binary)
    # h8 = spent on R&D activities last 3 yrs (binary)
    h1 = extract_var(df, ["h1"])
    rows["product_innov"] = recode_binary_yn(h1) if h1 is not None else np.nan
    h5 = extract_var(df, ["h5"])
    rows["process_innov"] = recode_binary_yn(h5) if h5 is not None else np.nan
    h8 = extract_var(df, ["h8"])
    rows["rd_spending"] = recode_binary_yn(h8) if h8 is not None else np.nan

    # Top manager
    b7 = extract_var(df, ["b7"])
    if b7 is not None:
        b7_clean = b7.astype(float)
        b7_clean[b7_clean.isin(NEG_CODES)] = np.nan
        b7_clean[b7_clean < 0] = np.nan
        rows["mgr_experience"] = b7_clean
    else:
        rows["mgr_experience"] = np.nan

    b7a = extract_var(df, ["b7a"])
    if b7a is not None:
        rows["mgr_female"] = recode_binary_yn(b7a)
    else:
        rows["mgr_female"] = np.nan

    # Controls
    b4 = extract_var(df, ["b4"])
    rows["female_owner"] = recode_binary_yn(b4) if b4 is not None else np.nan

    b6a = extract_var(df, ["b6a"])
    if b6a is not None:
        rows["foreign_own_pct"] = recode_pct(b6a)
    else:
        rows["foreign_own_pct"] = np.nan

    b5 = extract_var(df, ["b5"])
    if b5 is not None:
        b5_clean = b5.astype(float)
        b5_clean[b5_clean.isin(NEG_CODES)] = np.nan
        b5_clean[b5_clean < 1800] = np.nan
        rows["firm_age"] = year - b5_clean
    else:
        rows["firm_age"] = np.nan

    a4a = extract_var(df, ["a4a"])
    if a4a is not None:
        a4a_clean = a4a.astype(float)
        a4a_clean[a4a_clean.isin(NEG_CODES)] = np.nan
        rows["size_strata"] = a4a_clean  # 1=small 2=medium 3=large
        rows["ln_size"] = np.log(rows["l1_workers_raw"].clip(lower=1))
    else:
        rows["size_strata"] = np.nan
        rows["ln_size"] = np.nan

    a6a = extract_var(df, ["a6a", "a6b"])
    rows["isic_sector"] = a6a if a6a is not None else np.nan

    b1 = extract_var(df, ["b1"])
    rows["legal_status"] = b1 if b1 is not None else np.nan

    # Weights
    rows["wstrict"] = df["wstrict"] if "wstrict" in df.columns else np.nan
    rows["wmedian"] = df["wmedian"] if "wmedian" in df.columns else np.nan

    return rows.reset_index(drop=True)


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--raw-dir", default="data_wbes/raw",
                        help="Root of Country/Country_year.dta tree")
    parser.add_argument("--out-dir", default="data_wbes/p7",
                        help="Output directory")
    parser.add_argument("--manifest", default=None,
                        help="Path to manifest.csv (if raw-dir not available)")
    args = parser.parse_args()

    repo_root = Path(__file__).parent.parent.parent
    raw_dir = repo_root / args.raw_dir
    out_dir = repo_root / args.out_dir
    out_dir.mkdir(parents=True, exist_ok=True)

    import re
    from collections import defaultdict

    # Keywords that mark files to exclude from single-year processing
    SKIP_KEYWORDS = ["ISBS", "ISES", "expansion", "Informal", "LongForm",
                     "ESIS", "Documentation", "paneldata", "Micro", "micro"]

    def parse_stem(fpath: Path) -> tuple[str, int] | None:
        """Return (canonical_country, year) or None if unparseable."""
        stem = re.sub(r"^[0-9a-f]{8}-", "", fpath.stem)
        # Allow underscores inside country name (e.g. Republic_of_Cyprus)
        m = re.match(r"^([A-Za-z][A-Za-z_]+?)[\s_-]*(\d{4})", stem)
        if not m:
            return None
        return NAME_MAP.get(m.group(1), m.group(1)), int(m.group(2))

    def is_panel_filename(fpath: Path) -> bool:
        """True when stem contains two separate 4-digit years."""
        stem = re.sub(r"^[0-9a-f]{8}-", "", fpath.stem)
        years = re.findall(r"\d{4}", stem)
        return len(years) >= 2

    # Find all .dta files
    dta_files = sorted(raw_dir.rglob("*.dta"))
    if not dta_files:
        uploads = list(Path("/root/.claude/uploads").rglob("*.dta"))
        uploads = [p for p in uploads
                   if not any(kw in p.name for kw in SKIP_KEYWORDS)]
        log.info(f"raw-dir empty — {len(uploads)} .dta from uploads (before dedup)")

        # Separate panel files (two years in name) from single-year files
        panel_files = [p for p in uploads if is_panel_filename(p)]
        single_files = [p for p in uploads if not is_panel_filename(p)]
        log.info(f"  Single-year files: {len(single_files)}, "
                 f"Panel files (will split): {len(panel_files)}")

        # Deduplicate single-year files: per (country, year), keep largest
        cy_single: dict = defaultdict(list)
        for fpath in single_files:
            parsed = parse_stem(fpath)
            if parsed:
                cy_single[parsed].append(fpath)
        dta_files = [
            sorted(files, key=lambda p: p.stat().st_size, reverse=True)[0]
            for files in cy_single.values()
        ]

        # For panel files, only keep if the (country, year) pair has no single file
        panel_to_process = []
        for fpath in panel_files:
            stem = re.sub(r"^[0-9a-f]{8}-", "", fpath.stem)
            m = re.match(r"^([A-Za-z][A-Za-z_]+?)[\s_-]*(\d{4})", stem)
            if not m:
                continue
            country = NAME_MAP.get(m.group(1), m.group(1))
            years_in_name = [int(y) for y in re.findall(r"\d{4}", stem)]
            # Include panel if any of its years lacks a single-year file
            needs_panel = any((country, yr) not in cy_single for yr in years_in_name)
            if needs_panel:
                panel_to_process.append(fpath)

        log.info(f"After dedup: {len(dta_files)} single-year + "
                 f"{len(panel_to_process)} panel files")
    else:
        panel_to_process = []

    log.info(f"Found {len(dta_files)} single-year + "
             f"{len(panel_to_process)} panel files to process")

    REGION_MAP = {
        "China": "East Asia", "HongKong": "East Asia", "Korea": "East Asia",
        "Taiwan": "East Asia", "Mongolia": "East Asia",
        "Vietnam": "Southeast Asia", "Singapore": "Southeast Asia",
        "Thailand": "Southeast Asia", "Malaysia": "Southeast Asia",
        "Indonesia": "Southeast Asia", "Philippines": "Southeast Asia",
        "Cambodia": "Southeast Asia", "Laos": "Southeast Asia",
        "Myanmar": "Southeast Asia", "Brunei": "Southeast Asia",
        "TimorLeste": "Southeast Asia",
        "India": "South Asia", "Bangladesh": "South Asia",
        "Pakistan": "South Asia", "SriLanka": "South Asia",
        "Nepal": "South Asia", "Bhutan": "South Asia",
        "Maldives": "South Asia", "Afghanistan": "South Asia",
        "Kazakhstan": "Central Asia", "KyrgyzRepublic": "Central Asia",
        "Tajikistan": "Central Asia", "Uzbekistan": "Central Asia",
        "Turkmenistan": "Central Asia",
        "Armenia": "West Asia", "Georgia": "West Asia",
        "Bahrain": "West Asia", "Kuwait": "West Asia",
        "Qatar": "West Asia", "Oman": "West Asia",
        "SaudiArabia": "West Asia", "Israel": "West Asia",
        "Jordan": "West Asia", "Lebanon": "West Asia",
        "Iraq": "West Asia", "Yemen": "West Asia", "Cyprus": "West Asia",
        "Fiji": "Pacific", "Samoa": "Pacific", "Kiribati": "Pacific",
        "Tonga": "Pacific", "SolomonIslands": "Pacific",
        "Vanuatu": "Pacific", "PapuaNewGuinea": "Pacific",
    }

    def process_file(fpath: Path, country: str, year: int) -> None:
        """Read one .dta, harmonize, append to all_frames/manifest_rows/var_log_rows."""
        region = REGION_MAP.get(country, "Unknown")
        log.info(f"Processing {country} {year} ({fpath.name})")
        try:
            df, _ = read_dta_robust(fpath)
        except Exception as e:
            log.error(f"  READ ERROR: {e}")
            return

        var_avail = {v: (v in df.columns) for v in
                     ["c22b", "k33", "b8", "e6", "d3a", "d3b", "d3c",
                      "n3", "d2", "l1", "b7", "b7a", "b4", "b6a", "b5", "a4a"]}
        var_log_rows.append({"country": country, "year": year, "n_obs": len(df),
                             "n_vars": len(df.columns), **var_avail})
        try:
            frame = build_firm_record(df, country, year, region)
            all_frames.append(frame)
            n_complete = frame[["ln_labor_prod", "fsts", "tci_z", "dai_z"]].dropna().shape[0]
            manifest_rows.append({
                "country": country, "year": year, "region": region,
                "icrv_group": ICRV_MAP.get(country, ""),
                "n_raw": len(df), "n_complete_core": n_complete,
                "has_website": var_avail["c22b"],
                "has_epay": var_avail["k33"],
                "has_cert": var_avail["b8"],
                "has_foreign_tech": var_avail["e6"],
            })
        except Exception as e:
            log.error(f"  HARMONIZE ERROR: {e}")
            import traceback; traceback.print_exc()

    all_frames = []
    manifest_rows = []
    var_log_rows = []

    # --- Single-year files ---
    for fpath in dta_files:
        stem = re.sub(r"^[0-9a-f]{8}-", "", fpath.stem)
        m = re.match(r"^([A-Za-z][A-Za-z_]+?)[\s_-]*(\d{4})", stem)
        if not m:
            log.warning(f"Cannot parse country/year from {stem} — skipping")
            continue
        country = NAME_MAP.get(m.group(1), m.group(1))
        year = int(m.group(2))
        process_file(fpath, country, year)

    # --- Panel files: split by 'year' column ---
    for fpath in panel_to_process:
        stem = re.sub(r"^[0-9a-f]{8}-", "", fpath.stem)
        m = re.match(r"^([A-Za-z][A-Za-z_]+?)[\s_-]*(\d{4})", stem)
        if not m:
            continue
        country = NAME_MAP.get(m.group(1), m.group(1))
        log.info(f"Reading panel file {fpath.name} ({country})")
        try:
            df_panel, _ = read_dta_robust(fpath)
        except Exception as e:
            log.error(f"  PANEL READ ERROR: {e}")
            continue
        if "year" not in df_panel.columns:
            log.warning(f"  No 'year' column in panel — skipping")
            continue
        for yr_val, grp in df_panel.groupby("year"):
            yr = int(yr_val)
            log.info(f"  Panel split: {country} {yr} ({len(grp)} rows)")
            region = REGION_MAP.get(country, "Unknown")
            var_avail = {v: (v in grp.columns) for v in
                         ["c22b", "k33", "b8", "e6", "d3a", "d3b", "d3c",
                          "n3", "d2", "l1", "b7", "b7a", "b4", "b6a", "b5", "a4a"]}
            var_log_rows.append({"country": country, "year": yr, "n_obs": len(grp),
                                 "n_vars": len(grp.columns), **var_avail})
            try:
                frame = build_firm_record(grp.reset_index(drop=True), country, yr, region)
                all_frames.append(frame)
                n_complete = frame[["ln_labor_prod", "fsts", "tci_z", "dai_z"]].dropna().shape[0]
                manifest_rows.append({
                    "country": country, "year": yr, "region": region,
                    "icrv_group": ICRV_MAP.get(country, ""),
                    "n_raw": len(grp), "n_complete_core": n_complete,
                    "has_website": var_avail["c22b"],
                    "has_epay": var_avail["k33"],
                    "has_cert": var_avail["b8"],
                    "has_foreign_tech": var_avail["e6"],
                })
            except Exception as e:
                log.error(f"  HARMONIZE ERROR ({country} {yr}): {e}")

    if not all_frames:
        log.error("No data extracted — check raw-dir or uploads")
        sys.exit(1)

    # Combine
    pooled = pd.concat(all_frames, ignore_index=True, sort=False)
    log.info(f"\nPooled shape: {pooled.shape}")
    log.info(f"Countries: {pooled['country'].nunique()}")
    log.info(f"Country-years: {pooled.groupby(['country','year']).ngroups}")

    # Save
    pooled_csv = out_dir / "p7_pooled_clean.csv"
    pooled.to_csv(pooled_csv, index=False)
    log.info(f"Saved {pooled_csv} ({pooled_csv.stat().st_size/1024:.0f} KB)")

    manifest_path = out_dir / "p7_manifest.csv"
    pd.DataFrame(manifest_rows).to_csv(manifest_path, index=False)
    log.info(f"Saved {manifest_path}")

    var_log_path = out_dir / "p7_variable_log.csv"
    pd.DataFrame(var_log_rows).to_csv(var_log_path, index=False)
    log.info(f"Saved {var_log_path}")

    # Coverage summary
    print("\n=== COVERAGE SUMMARY ===")
    print(pooled[["country", "year", "region", "icrv_group",
                  "ln_labor_prod", "fsts", "tci_z", "dai_z",
                  "mgr_experience", "mgr_female"]].groupby(
        ["country", "year"]
    ).agg({"ln_labor_prod": "count", "fsts": "count", "tci_z": "count",
           "dai_z": "count", "mgr_experience": "count"}).rename(
        columns={"ln_labor_prod": "N_y", "fsts": "N_fsts",
                 "tci_z": "N_tci", "dai_z": "N_dai",
                 "mgr_experience": "N_mgr"}
    ).to_string())


if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
04 — Consolidate p7_pooled_clean.csv (52 Asian economies) into a single Stata .dta,
merging in innovation columns (product_innov, process_innov, rd_spending) from
the delta produced by step 05.

Source:  data_wbes/p7/p7_pooled_clean.csv             (harmonized firm-year output of step 01)
         data_wbes/p7/p7_innovation_delta.csv         (innov vars from available raw .dta — step 05)
Output:  data_wbes/p7/p7_pooled_clean.dta             (Stata 14, 33 cols including innov)
         data_wbes/p7/p7_pooled_summary.csv           (per country-wave firm + innov counts)

Drops 3 `*_panel` country tags (Mongolia_panel, Nepal_panel, Philippines_panel) —
duplicates of the single-year files.

Innovation columns are LEFT-MERGED on (country, year, firm_id_norm). Country-years
without a raw .dta in `data_wbes/raw_dta/` retain NaN for innov cols — populate
later by re-uploading the missing .dta and re-running steps 05 + 04.
"""
from pathlib import Path

import numpy as np
import pandas as pd
import pyreadstat


VAR_LABELS = {
    "country": "Country (harmonized name)",
    "year": "Survey wave year",
    "region": "WBES region",
    "icrv_group": "ICRV regime group (1-6)",
    "icrv_label": "ICRV regime label",
    "firm_id": "Firm identifier (idstd)",
    "ln_labor_prod": "ln(sales/workers) - labor productivity",
    "n3_sales_raw": "Raw sales (n3, last fiscal year)",
    "l1_workers_raw": "Permanent FT employees (l1)",
    "fsts": "Foreign sales / total sales (0-1)",
    "exporter": "Exporter indicator (fsts > 0)",
    "fsts_pct": "Export intensity (0-100)",
    "dai_website": "DAI: own website (c22b)",
    "dai_epay": "DAI: customer e-payment (k33>0)",
    "dai_epay_pct": "DAI: % e-payments (k33)",
    "dai_z": "DAI composite (z-score mean)",
    "tci_cert": "TCI: quality certification (b8)",
    "tci_foreign_tech": "TCI: foreign-licensed tech (e6)",
    "tci_z": "TCI composite (z-score mean)",
    "mgr_experience": "Top manager experience (yrs)",
    "mgr_female": "Top manager is female",
    "female_owner": "Female among owners",
    "foreign_own_pct": "Foreign ownership %",
    "firm_age": "Firm age (year - b5)",
    "size_strata": "Size strata (1=S 2=M 3=L)",
    "ln_size": "ln(workers)",
    "isic_sector": "ISIC sector code",
    "legal_status": "Legal status (b1)",
    "wstrict": "WBES weight (strict)",
    "wmedian": "WBES weight (median)",
    "product_innov": "Product innovation (h1, 0/1)",
    "process_innov": "Process innovation (h5, 0/1)",
    "rd_spending": "R&D spending last 3y (h8, 0/1)",
}


def normalize_firm_id(series: pd.Series) -> pd.Series:
    """Coerce firm_id to a stable string form ('123' for both 123 and 123.0)."""
    s = series.astype(str).str.strip()
    s = s.str.replace(r"\.0+$", "", regex=True)
    return s


def main() -> None:
    repo = Path(__file__).resolve().parent.parent.parent
    src_pooled = repo / "data_wbes/p7/p7_pooled_clean.csv"
    src_delta = repo / "data_wbes/p7/p7_innovation_delta.csv"
    dst_dta = repo / "data_wbes/p7/p7_pooled_clean.dta"
    dst_sum = repo / "data_wbes/p7/p7_pooled_summary.csv"

    df = pd.read_csv(src_pooled, low_memory=False)
    n_raw = len(df)

    panel_mask = df["country"].str.endswith("_panel", na=False)
    df = df.loc[~panel_mask].reset_index(drop=True)
    print(f"Dropped {panel_mask.sum():,} _panel rows ({n_raw:,} -> {len(df):,}).")

    n_countries = df["country"].nunique()
    if n_countries != 52:
        raise AssertionError(f"Expected 52 countries, got {n_countries}")

    # Merge innovation delta
    if src_delta.exists():
        delta = pd.read_csv(src_delta, low_memory=False)
        delta["firm_id_norm"] = normalize_firm_id(delta["firm_id"])
        delta = delta.drop_duplicates(subset=["country", "year", "firm_id_norm"], keep="first")

        df["firm_id_norm"] = normalize_firm_id(df["firm_id"])
        merged = df.merge(
            delta[["country", "year", "firm_id_norm",
                   "product_innov", "process_innov", "rd_spending"]],
            on=["country", "year", "firm_id_norm"], how="left",
        )
        merged = merged.drop(columns=["firm_id_norm"])
        df = merged
        print(f"Merged innovation delta: "
              f"{df['product_innov'].notna().sum():,} product_innov, "
              f"{df['process_innov'].notna().sum():,} process_innov, "
              f"{df['rd_spending'].notna().sum():,} rd_spending values populated.")
    else:
        print(f"WARN: {src_delta.name} not found — innovation columns will be all NaN.")
        df["product_innov"] = np.nan
        df["process_innov"] = np.nan
        df["rd_spending"] = np.nan

    # Stata cleanup
    for col in df.columns:
        if df[col].dtype == "object":
            df[col] = df[col].astype("string").fillna("")
    for col in df.columns:
        if df[col].dtype == "string":
            max_len = df[col].str.len().max()
            if max_len and max_len > 244:
                df[col] = df[col].str.slice(0, 244)

    pyreadstat.write_dta(
        df,
        str(dst_dta),
        column_labels=[VAR_LABELS.get(c, c) for c in df.columns],
        file_label="WBES P7 pooled - 52 Asian economies + innov delta (CTU PhD 2026)",
    )
    size_mb = dst_dta.stat().st_size / (1024 * 1024)
    print(f"Wrote {dst_dta.name} = {size_mb:.2f} MB, {len(df):,} rows, "
          f"{n_countries} countries, {len(df.columns)} columns.")

    # Per country-year summary
    agg = df.groupby(["country", "year"], as_index=False).agg(
        n_firms=("firm_id", "size"),
        region=("region", "first"),
        icrv_group=("icrv_group", "first"),
        icrv_label=("icrv_label", "first"),
        n_product_innov=("product_innov", lambda s: int(s.notna().sum())),
        n_process_innov=("process_innov", lambda s: int(s.notna().sum())),
        n_rd_spending=("rd_spending", lambda s: int(s.notna().sum())),
    )
    agg = agg.sort_values(["region", "country", "year"])
    agg.to_csv(dst_sum, index=False)
    print(f"Wrote {dst_sum.name} = {len(agg)} country-year rows.")

    print("\nInnovation column coverage by ICRV group:")
    by_group = df.groupby("icrv_label").agg(
        n_total=("firm_id", "size"),
        n_product_innov=("product_innov", lambda s: int(s.notna().sum())),
        n_process_innov=("process_innov", lambda s: int(s.notna().sum())),
        n_rd_spending=("rd_spending", lambda s: int(s.notna().sum())),
    )
    by_group["pct_innov_populated"] = (
        by_group["n_product_innov"] / by_group["n_total"] * 100
    ).round(1)
    print(by_group.to_string())


if __name__ == "__main__":
    main()

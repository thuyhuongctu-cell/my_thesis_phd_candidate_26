#!/usr/bin/env python3
"""
04 — Consolidate p7_pooled_clean.csv (52 Asian economies) into a single Stata .dta.

Source:  data_wbes/p7/p7_pooled_clean.csv  (harmonized firm-year output of step 01)
Output:  data_wbes/p7/p7_pooled_clean.dta  (Stata 14 format, ≤32-char varnames)
         data_wbes/p7/p7_pooled_summary.csv (per-country firm/year counts)

Drops 3 `*_panel` country tags (Mongolia_panel, Nepal_panel, Philippines_panel) —
these rows duplicate the single-year files already present.
"""
from pathlib import Path

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
}


def main() -> None:
    repo = Path(__file__).resolve().parent.parent.parent
    src = repo / "data_wbes/p7/p7_pooled_clean.csv"
    dst_dta = repo / "data_wbes/p7/p7_pooled_clean.dta"
    dst_sum = repo / "data_wbes/p7/p7_pooled_summary.csv"

    df = pd.read_csv(src, low_memory=False)
    n_raw = len(df)

    panel_mask = df["country"].str.endswith("_panel", na=False)
    df = df.loc[~panel_mask].reset_index(drop=True)
    print(f"Dropped {panel_mask.sum():,} _panel rows ({n_raw:,} -> {len(df):,}).")

    n_countries = df["country"].nunique()
    if n_countries != 52:
        raise AssertionError(f"Expected 52 countries, got {n_countries}")

    for col in df.select_dtypes(include="object").columns:
        df[col] = df[col].astype("string").fillna("")
    for col in df.select_dtypes(include="string").columns:
        max_len = df[col].str.len().max()
        if max_len and max_len > 244:
            df[col] = df[col].str.slice(0, 244)

    pyreadstat.write_dta(
        df,
        str(dst_dta),
        column_labels=[VAR_LABELS.get(c, c) for c in df.columns],
        file_label="WBES P7 pooled - 52 Asian economies (CTU PhD 2026)",
    )
    size_mb = dst_dta.stat().st_size / (1024 * 1024)
    print(f"Wrote {dst_dta.name} = {size_mb:.2f} MB, {len(df):,} rows, {n_countries} countries.")

    summary = (
        df.groupby(["country", "year"], as_index=False)
        .agg(n_firms=("firm_id", "size"),
             region=("region", "first"),
             icrv_group=("icrv_group", "first"),
             icrv_label=("icrv_label", "first"))
        .sort_values(["region", "country", "year"])
    )
    summary.to_csv(dst_sum, index=False)
    print(f"Wrote {dst_sum.name} = {len(summary)} country-year rows.")


if __name__ == "__main__":
    main()

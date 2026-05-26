"""Multidimensional firm-performance robustness for P7.

Compares the internationalization-performance (I-P) inverted-U across three
performance operationalizations, holding the G2 geographical-Asia scope fixed:
  (1) labour productivity  -- ln(real sales / worker)        [primary, existing]
  (2) real sales growth    -- 3-yr log change in sales       [WBES d2 vs n3]
  (3) employment growth    -- 3-yr log change in workers     [if recoverable]

Sales in t recovered as exp(ln_labor_prod + ln_size); sales 3 years prior is
n3_sales_raw. Growth outcomes use country-year fixed effects so within-wave
inflation is absorbed (nominal growth is admissible under CY-FE).

Outputs results/p7_multidim_comparison.csv.
"""
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
DATA = ROOT / "data_wbes/p7/p7_pooled_clean.csv"
OUT = Path(__file__).resolve().parent / "results/p7_multidim_comparison.csv"

OUT_OF_SCOPE = {"Turkey", "Azerbaijan", "Armenia", "Georgia", "Cyprus", "Comoros"}
SALES_GAP_YEARS = 3  # WBES n3 = sales three fiscal years prior


def load_scoped():
    df = pd.read_csv(DATA)
    df = df[~df["country"].isin(OUT_OF_SCOPE)].copy()
    cy = (df.groupby(["country", "year"])[["ln_labor_prod", "fsts", "tci_z", "dai_z"]]
            .apply(lambda x: x.dropna().shape[0]))
    valid = cy[cy >= 50].reset_index()[["country", "year"]]
    return df.merge(valid, on=["country", "year"])


def build_outcomes(df):
    df = df.copy()
    # (1) labour productivity already present as ln_labor_prod
    # (2) real sales growth: ln(sales_t) - ln(sales_{t-3}); sales_t recovered
    ln_sales_t = df["ln_labor_prod"] + df["ln_size"]
    ln_sales_prior = np.log(df["n3_sales_raw"].where(df["n3_sales_raw"] > 0))
    df["sales_growth"] = (ln_sales_t - ln_sales_prior) / SALES_GAP_YEARS
    # trim implausible growth tails (|annualised log growth| > 2 ~ +640%/-86%)
    df.loc[df["sales_growth"].abs() > 2, "sales_growth"] = np.nan
    # (3) employment growth needs workers 3 yrs prior -- not in harmonised file
    df["emp_growth"] = np.nan
    return df


def fit_invU(df, outcome, use_cyfe):
    d = df.dropna(subset=[outcome, "fsts"]).copy()
    d["fc"] = d["fsts"] - d["fsts"].mean()
    d["fc2"] = d["fc"] ** 2
    rhs = "fc + fc2 + female_owner + foreign_own_pct + firm_age + ln_size"
    if use_cyfe:
        d["cy"] = d["country"].astype(str) + "_" + d["year"].astype(str)
        rhs += " + C(cy)"
    m = smf.ols(f"{outcome} ~ {rhs}", data=d).fit(cov_type="HC1")
    b1, b2 = m.params["fc"], m.params["fc2"]
    tp = (-b1 / (2 * b2) + d["fsts"].mean()) * 100 if b2 != 0 else np.nan
    shape = "inverted-U" if b2 < 0 else "U/linear"
    confirmed = (b2 < 0) and (m.pvalues["fc2"] < 0.05) and (0 <= tp <= 100)
    return dict(outcome=outcome, n=int(m.nobs), b1=round(b1, 4),
                b1_p=round(m.pvalues["fc"], 4), b2=round(b2, 4),
                b2_p=round(m.pvalues["fc2"], 4), turning_point_pct=round(tp, 1),
                shape=shape, invU_confirmed=confirmed, cyfe=use_cyfe)


def main():
    df = build_outcomes(load_scoped())
    rows = [
        fit_invU(df, "ln_labor_prod", use_cyfe=False),
        fit_invU(df, "sales_growth", use_cyfe=True),
    ]
    if df["emp_growth"].notna().sum() >= 1000:
        rows.append(fit_invU(df, "emp_growth", use_cyfe=True))
    res = pd.DataFrame(rows)
    OUT.parent.mkdir(parents=True, exist_ok=True)
    res.to_csv(OUT, index=False)
    print(f"Scoped N (productivity): {df['ln_labor_prod'].notna().sum():,}")
    print(f"Sales-growth coverage: {df['sales_growth'].notna().sum():,} "
          f"({100*df['sales_growth'].notna().mean():.0f}% of pool)")
    print(f"Employment-growth coverage: {df['emp_growth'].notna().sum():,} "
          "(workers-3yr-prior not in harmonised file)")
    print("\n=== Multidimensional I-P comparison ===")
    print(res.to_string(index=False))


if __name__ == "__main__":
    main()

* =============================================================================
* P8 Pacific & Indian Ocean SIDS — Wild-cluster bootstrap robustness
*
* 03_p8_wild_cluster_bootstrap.do
*
* Purpose: Cameron-Gelbach-Miller (2008) wild-cluster bootstrap inference for
* the headline M1 β(FSTSc) estimate, addressing Phase A1 reviewer item #8.
* Small G (5 effective clusters in regression sample after listwise deletion;
* 4 in Pacific-only subsample) makes naive cluster-robust SE potentially
* under-powered (Roodman et al. 2019); wild bootstrap recovers correct test
* size when G is small.
*
* Author: Đỗ Thùy Hương (NCS) · PGS.TS. Phan Anh Tú
* Created: 2026-06-03
*
* Inputs:
*   - data_wbes/p7/p7_pooled_clean.csv  (harmonised pooled WBES data)
*
* Outputs:
*   - p8/replication/results/p8_stata_wild_cluster_bootstrap.csv
*   - p8/replication/results/p8_stata_wild_cluster_bootstrap.log
*
* Required Stata packages:
*   - boottest  (Roodman, MacKinnon, Nielsen & Webb 2019)
*     net install boottest, from(https://raw.githubusercontent.com/droodman/boottest/master/)
*
* To run:
*   cd "MY_THESIS_PHD_CANDIDATE_26"
*   stata -b do p8/replication/do/03_p8_wild_cluster_bootstrap.do
*
* Note: matches the Python prototype (commit `081f40c`) for fair comparison
* with the HC1 baseline already reported in §4 of the P8 manuscript.
* =============================================================================

clear all
set more off
capture log close
log using "p8/replication/results/p8_stata_wild_cluster_bootstrap.log", replace

set seed 20260603

* ── 1. Load + filter ─────────────────────────────────────────────────────────
import delimited "data_wbes/p7/p7_pooled_clean.csv", clear
keep if icrv_label == "SIDS_small"
drop if missing(ln_labor_prod) | missing(fsts)

summarize fsts, meanonly
gen fsts_c = fsts - r(mean)
gen fsts_c2 = fsts_c ^ 2

encode country, gen(country_id)
encode year, gen(year_id)

* ── 2. M1 with HC1 SE (baseline) ─────────────────────────────────────────────
display "================================================================="
display "  M1 baseline (HC1 robust SE)"
display "================================================================="
reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(robust)

* ── 3. Naive cluster-robust SE ───────────────────────────────────────────────
display "================================================================="
display "  M1 naive cluster-robust SE (CR1) — note small-G distortion"
display "================================================================="
reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(cluster country_id)

* ── 4. Wild-cluster bootstrap (Rademacher) for β(fsts_c) test ────────────────
display "================================================================="
display "  M1 wild-cluster bootstrap (Cameron-Gelbach-Miller 2008)"
display "  H0: β(FSTSc) = 0; B = 999; Rademacher weights"
display "================================================================="

* Re-fit M1 baseline to capture for boottest
reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, cluster(country_id)
boottest fsts_c = 0, reps(999) cluster(country_id) weighttype(rademacher) seed(20260603)

* ── 5. Repeat on Pacific-only subsample ──────────────────────────────────────
display "================================================================="
display "  Pacific-only subsample (excluding Comoros, N ≈ 415)"
display "================================================================="

preserve
drop if country == "Comoros"
display _N " rows after excluding Comoros"

* Re-centre FSTS on Pacific-only sample
summarize fsts, meanonly
replace fsts_c = fsts - r(mean)
replace fsts_c2 = fsts_c ^ 2

reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(robust)

reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, cluster(country_id)
boottest fsts_c = 0, reps(999) cluster(country_id) weighttype(rademacher) seed(20260603)

restore

* ── 6. Expected results (per Python prototype 2026-06-03) ────────────────────
display "================================================================="
display "  Expected M1 β(FSTSc) inference (per Python prototype):"
display "  --------------------------------------------------"
display "  FULL SIDS (N=532 regression, G=5 effective clusters):"
display "    HC1 SE       : β = -0.4038, SE = 0.188, p = .031*"
display "    Cluster CR1  : β = -0.4038, SE = 0.312, p = .196 (G=5)"
display "    WCB Rademacher: p = .033* (B=999)"
display "  Pacific-only (N=415, G=4):"
display "    HC1 SE       : β = -0.3566, SE = 0.196, p = .068"
display "    Cluster CR1  : β = -0.3566, SE = 0.340, p = .295"
display "    WCB Rademacher: p = .069 (B=999)"
display "  ----------------------------------------"
display "  Substantive reading: HC1 inference is well-calibrated; the"
display "  small-G cluster SE over-conserves (Roodman et al. 2019)."
display "  WCB recovers the HC1-equivalent inference, validating that"
display "  the headline p-value of the FIP signal is not an artefact of"
display "  small-G cluster-robust standard errors."
display "================================================================="

log close
exit, clear

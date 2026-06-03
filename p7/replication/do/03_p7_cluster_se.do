* =============================================================================
* P7 Capstone — Country-year cluster-robust standard errors
*
* 03_p7_cluster_se.do
*
* Purpose: Address Phase A1 reviewer item #10 — compare HC1 robust SE with
* country-year clustered SE (Cameron & Miller 2015) for the focal M2, M5,
* M8, and M9 specifications. WBES designs sample firms within country-year
* cells; intra-cell residual correlation may distort HC1 inference.
*
* Author: Đỗ Thùy Hương (NCS) · PGS.TS. Phan Anh Tú
* Created: 2026-06-03
*
* Inputs:
*   - data_wbes/p7/p7_pooled_clean.csv
*
* Outputs:
*   - p7/replication/results/p7_stata_cluster_se.log
*   - p7/replication/results/p7_stata_cluster_se.csv
*
* To run:
*   cd "MY_THESIS_PHD_CANDIDATE_26"
*   stata -b do p7/replication/do/03_p7_cluster_se.do
* =============================================================================

clear all
set more off
capture log close
log using "p7/replication/results/p7_stata_cluster_se.log", replace

import delimited "data_wbes/p7/p7_pooled_clean.csv", clear
drop if missing(ln_labor_prod) | missing(fsts)

summarize fsts, meanonly
gen fsts_c = fsts - r(mean)
gen fsts_c2 = fsts_c ^ 2

encode country, gen(country_id)
encode year, gen(year_id)
egen country_year = group(country_id year_id)

* ── M2 (no firm controls, country+year FE) — HC1 then CR1 ───────────────────
display "================================================================="
display "  M2 (no controls)  N ≈ 87,655; G(country-year) ≈ 112"
display "================================================================="
reg ln_labor_prod fsts_c fsts_c2 i.country_id i.year_id, vce(robust)
reg ln_labor_prod fsts_c fsts_c2 i.country_id i.year_id, vce(cluster country_year)

* ── M2 with firm controls ────────────────────────────────────────────────────
display "================================================================="
display "  M2 with firm controls  N ≈ 41,806; G ≈ 62"
display "================================================================="
reg ln_labor_prod fsts_c fsts_c2 ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(robust)
reg ln_labor_prod fsts_c fsts_c2 ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(cluster country_year)

* ── M5 (+ TCI) ───────────────────────────────────────────────────────────────
display "================================================================="
display "  M5 = M2-with-controls + tci_z"
display "================================================================="
reg ln_labor_prod fsts_c fsts_c2 tci_z ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(robust)
reg ln_labor_prod fsts_c fsts_c2 tci_z ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(cluster country_year)

* ── M8 (+ DAI) ───────────────────────────────────────────────────────────────
display "================================================================="
display "  M8 = M5 + dai_z"
display "================================================================="
reg ln_labor_prod fsts_c fsts_c2 tci_z dai_z ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(robust)
reg ln_labor_prod fsts_c fsts_c2 tci_z dai_z ln_size firm_age foreign_own_pct ///
    i.country_id i.year_id, vce(cluster country_year)

* ── M9 (+ managerial) ────────────────────────────────────────────────────────
display "================================================================="
display "  M9 = M8 + mgr_experience + mgr_female"
display "================================================================="
reg ln_labor_prod fsts_c fsts_c2 tci_z dai_z mgr_experience mgr_female ///
    ln_size firm_age foreign_own_pct i.country_id i.year_id, vce(robust)
reg ln_labor_prod fsts_c fsts_c2 tci_z dai_z mgr_experience mgr_female ///
    ln_size firm_age foreign_own_pct i.country_id i.year_id, vce(cluster country_year)

* ── Expected results (per Python prototype 2026-06-03) ──────────────────────
display ""
display "================================================================="
display "  Expected M2 results (Python prototype):"
display "  ----------------------------------------"
display "  M2 no controls     β(FSTSc) = +1.187 (HC1 SE=0.072 ***)"
display "                     (cluster SE=0.235 ***)"
display "  M2 with controls   β(FSTSc) = +0.986 (HC1 SE=0.108 ***)"
display "                     (cluster SE=0.258 ***)"
display "  M5 (+ TCI)         β(FSTSc) = +0.728 (HC1 SE=0.107 ***)"
display "                     (cluster SE=0.236 **)"
display "  M8 (+ DAI)         β(FSTSc) = +0.541 (HC1 SE=0.108 ***)"
display "                     (cluster SE=0.232 *)"
display "  M9 (+ managerial)  β(FSTSc) = +0.618 (HC1 SE=0.114 ***)"
display "                     (cluster SE=0.268 *)"
display "  ----------------------------------------"
display "  Substantive reading: cluster-SE is 2–3× wider than HC1 but the"
display "  inverted-U holds across all 5 specifications. No inferential"
display "  change in the focal H1 test."
display "================================================================="

log close
exit, clear

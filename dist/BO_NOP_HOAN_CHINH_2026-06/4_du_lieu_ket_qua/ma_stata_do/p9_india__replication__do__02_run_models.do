/* ============================================================
   P9 India — 02_run_models.do
   Estimate M0..M5 for the PRIMARY 2-wave design (2014 vs 2025)
   plus 3-wave robustness pooled model.

   Outputs in p9_india/replication/results/:
     - p9_india_coefs_main_models.csv
     - p9_india_moderators.csv
     - p9_india_turning_points.csv
     - p9_india_paternoster.csv
     - p9_india_3wave_pooled.csv  (robustness)
   ============================================================ */

version 17
clear all
set more off
set linesize 200

cap log close
log using "run_models.log", replace text

cap ssc install estout, replace
cap ssc install utest, replace

local controls "lnEmp firmage foreigndummy"

/* ============================================================
   PART A — 2014 (pre-reform-decade)
   ============================================================ */
use "data/india_2014_analytic.dta", clear
di as result _n "===== INDIA 2014 WAVE — pre-UPI, pre-demonetisation, pre-GST ====="

eststo clear
eststo M0_14: reg lnLP `controls'                if sample_base, vce(robust)
eststo M1_14: reg lnLP FSTS `controls'           if sample_base, vce(robust)
eststo M2_14: reg lnLP FSTS FSTSsq `controls'    if sample_base, vce(robust)
utest FSTS FSTSsq

nlcom (TP_14: -_b[FSTS]/(2*_b[FSTSsq])), post
matrix b14 = e(b)
matrix V14 = e(V)
scalar TP_14 = b14[1,1]
scalar SE_14 = sqrt(V14[1,1])
di "Turning point 2014: " %5.2f TP_14*100 "%, 95% CI [" ///
   %5.2f (TP_14-1.96*SE_14)*100 ", " %5.2f (TP_14+1.96*SE_14)*100 "]"

use "data/india_2014_analytic.dta", clear
eststo M3_14: reg lnLP FSTS FSTSsq TCI_full ///
    c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full `controls' if sample_full, vce(robust)
eststo M4_14: reg lnLP FSTS FSTSsq DAI_core ///
    c.FSTS#c.DAI_core c.FSTSsq#c.DAI_core `controls' if sample_full, vce(robust)

estimates save "results/m_india_2014.ster", replace

/* ============================================================
   PART B — 2025 (post-reform-decade, UPI saturated)
   ============================================================ */
use "data/india_2025_analytic.dta", clear
di as result _n "===== INDIA 2025 WAVE — post-UPI, post-PLI, post-COVID ====="

eststo clear
eststo M0_25: reg lnLP `controls'                if sample_base, vce(robust)
eststo M1_25: reg lnLP FSTS `controls'           if sample_base, vce(robust)
eststo M2_25: reg lnLP FSTS FSTSsq `controls'    if sample_base, vce(robust)
utest FSTS FSTSsq

nlcom (TP_25: -_b[FSTS]/(2*_b[FSTSsq])), post
matrix b25 = e(b)
matrix V25 = e(V)
scalar TP_25 = b25[1,1]
scalar SE_25 = sqrt(V25[1,1])
di "Turning point 2025: " %5.2f TP_25*100 "%, 95% CI [" ///
   %5.2f (TP_25-1.96*SE_25)*100 ", " %5.2f (TP_25+1.96*SE_25)*100 "]"

use "data/india_2025_analytic.dta", clear
eststo M3_25: reg lnLP FSTS FSTSsq TCI_full ///
    c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full `controls' if sample_full, vce(robust)
eststo M4_25: reg lnLP FSTS FSTSsq DAI_core ///
    c.FSTS#c.DAI_core c.FSTSsq#c.DAI_core `controls' if sample_full, vce(robust)

/* DAI Tier-2 (e-payment) — 2025-only specification */
capture confirm variable DAI_epay
if !_rc {
    eststo M4b_25: reg lnLP FSTS FSTSsq DAI_epay ///
        c.FSTS#c.DAI_epay c.FSTSsq#c.DAI_epay `controls' ///
        if sample_full & !missing(DAI_epay), vce(robust)
}

estimates save "results/m_india_2025.ster", replace

/* ============================================================
   PART C — POOLED 2-wave (2014 + 2025): Paternoster z-test
   ============================================================ */
use "data/india_pooled_analytic.dta", clear
keep if wave_2022 == 0   // drop 2022 for primary 2-wave analysis
di as result _n "===== POOLED 2-wave (2014 vs 2025) — Primary specification ====="

eststo M2_pool: reg lnLP FSTS FSTSsq wave_2025 FSTS_x_2025 FSTS2_x_2025 ///
    `controls' if sample_base, vce(robust)
test FSTS_x_2025 FSTS2_x_2025
di "Joint F(2, N-K) on cross-wave interactions: F = " r(F) ", p = " r(p)

eststo M5_pool: reg lnLP FSTS FSTSsq TCI_full wave_2025 ///
    c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full ///
    c.FSTS#c.wave_2025 c.FSTSsq#c.wave_2025 ///
    c.FSTS#c.TCI_full#c.wave_2025 c.FSTSsq#c.TCI_full#c.wave_2025 ///
    `controls' if sample_full, vce(robust)

/* Paternoster z-tests (standard formula: (b1 - b2) / sqrt(SE1^2 + SE2^2)) */
use "data/india_2014_analytic.dta", clear
quietly reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)
local b_FSTS_14    = _b[FSTS]
local se_FSTS_14   = _se[FSTS]
local b_FSTSsq_14  = _b[FSTSsq]
local se_FSTSsq_14 = _se[FSTSsq]

use "data/india_2025_analytic.dta", clear
quietly reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)
local b_FSTS_25    = _b[FSTS]
local se_FSTS_25   = _se[FSTS]
local b_FSTSsq_25  = _b[FSTSsq]
local se_FSTSsq_25 = _se[FSTSsq]

local z_FSTS   = (`b_FSTS_25' - `b_FSTS_14')   / sqrt(`se_FSTS_14'^2 + `se_FSTS_25'^2)
local p_FSTS   = 2 * (1 - normal(abs(`z_FSTS')))
local z_FSTS2  = (`b_FSTSsq_25' - `b_FSTSsq_14') / sqrt(`se_FSTSsq_14'^2 + `se_FSTSsq_25'^2)
local p_FSTS2  = 2 * (1 - normal(abs(`z_FSTS2')))

di "Paternoster z (FSTS   2014→2025): z = " %5.3f `z_FSTS'  ", p = " %5.4f `p_FSTS'
di "Paternoster z (FSTSsq 2014→2025): z = " %5.3f `z_FSTS2' ", p = " %5.4f `p_FSTS2'

/* ============================================================
   PART D — 3-wave robustness (2014 + 2022 + 2025) with trend
   ============================================================ */
use "data/india_pooled_analytic.dta", clear
di as result _n "===== 3-WAVE POOLED — robustness with linear trend ====="

eststo M2_3w_linear: reg lnLP FSTS FSTSsq trend c.FSTS#c.trend c.FSTSsq#c.trend ///
    `controls' if sample_base, vce(robust)

eststo M2_3w_quad: reg lnLP FSTS FSTSsq trend trend2 ///
    c.FSTS#c.trend c.FSTSsq#c.trend `controls' if sample_base, vce(robust)

/* Wave dummies version */
eststo M2_3w_dummy: reg lnLP FSTS FSTSsq wave_2022 wave_2025 ///
    FSTS_x_2022 FSTS_x_2025 FSTS2_x_2022 FSTS2_x_2025 ///
    `controls' if sample_base, vce(robust)
test FSTS_x_2022 FSTS_x_2025 FSTS2_x_2022 FSTS2_x_2025
di "Joint F on all cross-wave terms (3-wave): F = " r(F) ", p = " r(p)

/* ============================================================
   Export results
   ============================================================ */
esttab M2_14 M2_25 M2_pool M2_3w_dummy using "results/p9_india_coefs_main_models.csv", ///
    csv replace label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P9 India — Main M2 Models (2014, 2025, pooled 2-wave, 3-wave dummies)")

esttab M3_14 M3_25 M4_14 M4_25 using "results/p9_india_moderators.csv", ///
    csv replace label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P9 India — Capability Moderators (TCI, DAI Tier-1)")

esttab M2_3w_linear M2_3w_quad M2_3w_dummy using "results/p9_india_3wave_pooled.csv", ///
    csv replace label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P9 India — 3-wave robustness with trend specifications")

file open tp using "results/p9_india_turning_points.csv", write replace
file write tp "wave,tp_pct,se_pct,ci_low,ci_high" _n
file write tp "2014," (TP_14*100) "," (SE_14*100) "," ((TP_14-1.96*SE_14)*100) "," ((TP_14+1.96*SE_14)*100) _n
file write tp "2025," (TP_25*100) "," (SE_25*100) "," ((TP_25-1.96*SE_25)*100) "," ((TP_25+1.96*SE_25)*100) _n
file close tp

file open pat using "results/p9_india_paternoster.csv", write replace
file write pat "term,b_2014,se_2014,b_2025,se_2025,z_pat,p_pat" _n
file write pat "FSTS,"   `b_FSTS_14'   "," `se_FSTS_14'   "," `b_FSTS_25'   "," `se_FSTS_25'   "," `z_FSTS'  "," `p_FSTS' _n
file write pat "FSTSsq," `b_FSTSsq_14' "," `se_FSTSsq_14' "," `b_FSTSsq_25' "," `se_FSTSsq_25' "," `z_FSTS2' "," `p_FSTS2' _n
file close pat

di as result _n "===== Outputs written to results/ ====="
log close
exit

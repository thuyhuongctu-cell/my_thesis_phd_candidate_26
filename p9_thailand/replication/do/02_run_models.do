/* ============================================================
   P9 Thailand — 02_run_models.do
   Estimate M0..M5 on 2016, 2025, and pooled samples
   + Lind-Mehlum U-test, delta-method turning-point CI,
     Paternoster cross-wave z-test

   Required:  thailand_2016_analytic.dta, thailand_2025_analytic.dta,
              thailand_pooled_analytic.dta  (from 01_build_thailand.do)
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
   PART A — Thailand 2016 (pre-COVID, pre-RCEP)
   ============================================================ */
use "data/thailand_2016_analytic.dta", clear
di as result _n "===== THAILAND 2016 WAVE (pre-COVID, pre-RCEP) ====="

eststo clear
eststo M0_2016: reg lnLP `controls'           if sample_base, vce(robust)
eststo M1_2016: reg lnLP FSTS `controls'      if sample_base, vce(robust)
eststo M2_2016: reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)

/* Lind-Mehlum U-test for inverted-U */
utest FSTS FSTSsq

/* Turning point + delta-method CI */
nlcom (TP_2016: -_b[FSTS]/(2*_b[FSTSsq])), post
matrix b_2016 = e(b)
matrix V_2016 = e(V)
scalar TP_2016 = b_2016[1,1]
scalar SE_2016 = sqrt(V_2016[1,1])
di "Turning point 2016: " %4.2f TP_2016*100 "%, 95% CI [" ///
   %4.2f (TP_2016-1.96*SE_2016)*100 ", " %4.2f (TP_2016+1.96*SE_2016)*100 "]"

/* M3 with TCI moderation (full sample only) */
use "data/thailand_2016_analytic.dta", clear
eststo M3_2016: reg lnLP FSTS FSTSsq TCI_full c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full `controls' ///
    if sample_full, vce(robust)

/* M4 with DAI moderation */
eststo M4_2016: reg lnLP FSTS FSTSsq DAI_core c.FSTS#c.DAI_core c.FSTSsq#c.DAI_core `controls' ///
    if sample_full, vce(robust)

/* Save 2016 estimates */
estimates save "results/m_2016.ster", replace

/* ============================================================
   PART B — Thailand 2025 (post-COVID, post-RCEP)
   ============================================================ */
use "data/thailand_2025_analytic.dta", clear
di as result _n "===== THAILAND 2025 WAVE (post-COVID, post-RCEP) ====="

eststo clear
eststo M0_2025: reg lnLP `controls'           if sample_base, vce(robust)
eststo M1_2025: reg lnLP FSTS `controls'      if sample_base, vce(robust)
eststo M2_2025: reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)
utest FSTS FSTSsq

nlcom (TP_2025: -_b[FSTS]/(2*_b[FSTSsq])), post
matrix b_2025 = e(b)
matrix V_2025 = e(V)
scalar TP_2025 = b_2025[1,1]
scalar SE_2025 = sqrt(V_2025[1,1])
di "Turning point 2025: " %4.2f TP_2025*100 "%, 95% CI [" ///
   %4.2f (TP_2025-1.96*SE_2025)*100 ", " %4.2f (TP_2025+1.96*SE_2025)*100 "]"

use "data/thailand_2025_analytic.dta", clear
eststo M3_2025: reg lnLP FSTS FSTSsq TCI_full c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full `controls' ///
    if sample_full, vce(robust)
eststo M4_2025: reg lnLP FSTS FSTSsq DAI_core c.FSTS#c.DAI_core c.FSTSsq#c.DAI_core `controls' ///
    if sample_full, vce(robust)

estimates save "results/m_2025.ster", replace

/* ============================================================
   PART C — POOLED + Cross-wave Paternoster z-test
   ============================================================ */
use "data/thailand_pooled_analytic.dta", clear
di as result _n "===== POOLED (Thailand 2016 + 2025) ====="

eststo M2_pool: reg lnLP FSTS FSTSsq wave_2025 FSTS_x_2025 FSTS2_x_2025 `controls' ///
    if sample_base, vce(robust)

/* Joint F-test on cross-wave interactions */
test FSTS_x_2025 FSTS2_x_2025
di "Joint F(2, N-K) on cross-wave interactions: F = " r(F) ", p = " r(p)

/* Three-way (TCI moderation by wave) */
eststo M5_pool: reg lnLP FSTS FSTSsq TCI_full wave_2025 ///
    c.FSTS#c.TCI_full c.FSTSsq#c.TCI_full ///
    c.FSTS#c.wave_2025 c.FSTSsq#c.wave_2025 ///
    c.FSTS#c.TCI_full#c.wave_2025 c.FSTSsq#c.TCI_full#c.wave_2025 ///
    `controls' if sample_full, vce(robust)

/* Paternoster z-test on FSTS, FSTSsq, TCI (cross-wave) */
use "data/thailand_2016_analytic.dta", clear
quietly reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)
local b_FSTS_2016 = _b[FSTS]
local se_FSTS_2016 = _se[FSTS]
local b_FSTSsq_2016 = _b[FSTSsq]
local se_FSTSsq_2016 = _se[FSTSsq]

use "data/thailand_2025_analytic.dta", clear
quietly reg lnLP FSTS FSTSsq `controls' if sample_base, vce(robust)
local b_FSTS_2025 = _b[FSTS]
local se_FSTS_2025 = _se[FSTS]
local b_FSTSsq_2025 = _b[FSTSsq]
local se_FSTSsq_2025 = _se[FSTSsq]

local z_FSTS = (`b_FSTS_2025' - `b_FSTS_2016') / sqrt(`se_FSTS_2016'^2 + `se_FSTS_2025'^2)
local p_FSTS = 2 * (1 - normal(abs(`z_FSTS')))
di "Paternoster z (FSTS 2016 vs 2025):  z = " %4.3f `z_FSTS' ", p = " %5.4f `p_FSTS'

local z_FSTSsq = (`b_FSTSsq_2025' - `b_FSTSsq_2016') / sqrt(`se_FSTSsq_2016'^2 + `se_FSTSsq_2025'^2)
local p_FSTSsq = 2 * (1 - normal(abs(`z_FSTSsq')))
di "Paternoster z (FSTSsq 2016 vs 2025): z = " %4.3f `z_FSTSsq' ", p = " %5.4f `p_FSTSsq'

/* Export coefficients to CSV for figure generation */
esttab M2_2016 M2_2025 M2_pool using "results/p9_coefs_main_models.csv", ///
    csv replace label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P9 Thailand — Main M2 Models")

esttab M3_2016 M3_2025 M4_2016 M4_2025 using "results/p9_moderators.csv", ///
    csv replace label se p drop(_cons) star(* 0.10 ** 0.05 *** 0.01) ///
    title("P9 Thailand — Capability Moderators")

/* Save turning points */
file open tp using "results/p9_turning_points.csv", write replace
file write tp "wave,tp,se,ci_low,ci_high" _n
file write tp "2016," (TP_2016*100) "," (SE_2016*100) "," ((TP_2016-1.96*SE_2016)*100) "," ((TP_2016+1.96*SE_2016)*100) _n
file write tp "2025," (TP_2025*100) "," (SE_2025*100) "," ((TP_2025-1.96*SE_2025)*100) "," ((TP_2025+1.96*SE_2025)*100) _n
file close tp

/* Save Paternoster z-tests */
file open pat using "results/p9_paternoster.csv", write replace
file write pat "term,b_2016,se_2016,b_2025,se_2025,z_pat,p_pat" _n
file write pat "FSTS," `b_FSTS_2016' "," `se_FSTS_2016' "," `b_FSTS_2025' "," `se_FSTS_2025' "," `z_FSTS' "," `p_FSTS' _n
file write pat "FSTSsq," `b_FSTSsq_2016' "," `se_FSTSsq_2016' "," `b_FSTSsq_2025' "," `se_FSTSsq_2025' "," `z_FSTSsq' "," `p_FSTSsq' _n
file close pat

di as result _n "===== Outputs written to results/ ====="
log close
exit

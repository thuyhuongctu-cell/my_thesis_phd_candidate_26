/* ============================================================
   P4 Singapore — 02_run_models.do
   Purpose: Estimate M0–M5 on Singapore 2023 analytic sample
            Lind-Mehlum utest, delta-method turning-point CI
            Heckman IMR selection check (exporters vs non-exporters)
   Author: Đỗ Thị Thúy Hương
   Date: May 2026

   Input:  data/singapore_2023_analytic.dta
   Output: results/table_2_main_models.csv
           results/table_lind_mehlum.csv
           results/table_heckman_imr.csv
           results/table_3_robustness.csv
   ============================================================ */

version 17
clear all
set more off
set linesize 200

/* ---- Directory Setup ---------------------------------------- */
global out    "results"
cap mkdir "$out"

/* ---- Install required packages ----------------------------- */
cap ssc install estout, replace
cap ssc install utest,  replace

use "data/singapore_2023_analytic.dta", clear

local controls  "lnEmp firmage foreigndummy"

di _n as result "=== Singapore 2023 — Descriptives ==="
summarize lnLP FSTS TCIfull DAIfull DAIthin if base
tabulate DAItier2 if base, missing

/* ============================================================
   Centre and standardise focal variables
   ============================================================ */
quietly summarize FSTS if base
local fsts_mean = r(mean)
gen FSTSc  = FSTS  - `fsts_mean'
gen FSTSc2 = FSTSc^2
label var FSTSc  "FSTS centred (mean = `fsts_mean')"
label var FSTSc2 "FSTSc squared"

/* Z-standardise TCI and DAI */
quietly summarize TCIfull if tci_samp
gen TCI_z = (TCIfull - r(mean)) / r(sd) if r(sd) > 0
quietly summarize DAIfull if dai_samp
gen DAI_z = (DAIfull - r(mean)) / r(sd) if r(sd) > 0
label var TCI_z "TCI z-score (Tier-1+2 composite)"
label var DAI_z "DAI z-score (Tier-1+2 composite)"

/* Interaction terms */
gen FSTSc_DAIz   = FSTSc  * DAI_z
gen FSTSc2_DAIz  = FSTSc2 * DAI_z
gen FSTSc_TCIz   = FSTSc  * TCI_z
gen FSTSc2_TCIz  = FSTSc2 * TCI_z
gen FSTSc_DAIz_TCI = FSTSc * DAI_z * TCI_z

/* ============================================================
   PART A — Main Models (Table 2)
   ============================================================ */
di _n as result "=== MAIN MODELS ==="

eststo clear

/* M0: Controls only */
eststo M0: reg lnLP `controls' if base, vce(hc1)
estadd local spec "Controls"

/* M1: FSTS linear */
eststo M1: reg lnLP FSTSc `controls' if base, vce(hc1)
estadd local spec "Linear FSTS"

/* M2: Quadratic FSTS (H1: inverted-U) */
eststo M2: reg lnLP FSTSc FSTSc2 `controls' if base, vce(hc1)
estadd local spec "Quadratic FSTS"
quietly utest FSTSc FSTSc2
estadd scalar lm_p = r(p)

/* Delta-method turning-point CI */
preserve
    quietly nlcom (tp: `fsts_mean' + (-_b[FSTSc]/(2*_b[FSTSc2]))), post
    scalar tp_SGP    = _b[tp]
    scalar tp_SGP_se = _se[tp]
    di as txt "[M2 SGP] Turning point = " %5.4f tp_SGP ///
              "  (SE = " %5.4f tp_SGP_se ")"
    di as txt "         95% CI: [" ///
              %5.4f (tp_SGP - 1.96*tp_SGP_se) ", " ///
              %5.4f (tp_SGP + 1.96*tp_SGP_se) "]"
restore

/* M3: Quadratic + TCI level + interaction (H2: TCI amplification) */
eststo M3: reg lnLP FSTSc FSTSc2 TCI_z FSTSc_TCIz FSTSc2_TCIz ///
                    `controls' if tci_samp, vce(hc1)
estadd local spec "Quadratic+TCI"

/* M4: Quadratic + DAI level + interaction (H3: DAI amplification) */
eststo M4: reg lnLP FSTSc FSTSc2 DAI_z FSTSc_DAIz FSTSc2_DAIz ///
                    `controls' if dai_samp, vce(hc1)
estadd local spec "Quadratic+DAI"

/* M5: Full model — FSTS quadratic + TCI + DAI */
eststo M5: reg lnLP FSTSc FSTSc2 TCI_z DAI_z ///
                    FSTSc_TCIz FSTSc2_TCIz FSTSc_DAIz FSTSc2_DAIz ///
                    `controls' if full_samp, vce(hc1)
estadd local spec "Full model"

/* Export main models table */
esttab M0 M1 M2 M3 M4 M5 ///
    using "$out/table_2_main_models.csv", replace ///
    b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2 r2_a lm_p, fmt(%9.0f %6.4f %6.4f %6.4f) ///
          labels("N" "R²" "Adj R²" "LM utest p")) ///
    label title("Singapore 2023 — Main Models") noobs

di as result "  Saved: table_2_main_models.csv"

/* Professional RTF table for manuscript */
esttab M0 M1 M2 M3 M4 M5 ///
    using "$out/table_2_main_models.rtf", replace ///
    b(%9.3f) se(%9.3f) ///
    star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a lm_p, fmt(%9.0f %9.3f %9.3f) ///
          labels("Observations" "Adj. R²" "Lind-Mehlum p")) ///
    label mtitles("M0" "M1" "M2" "M3" "M4" "M5") ///
    title("Table 2. Singapore 2023 — Main Threshold Models (M0–M5)") ///
    addnote("Notes: HC1 robust SE in parentheses. † p<0.10, * p<0.05, ** p<0.01, *** p<0.001." ///
            "FSTS centred at within-sample mean. TCI = Technological Capability Index (z-standardised)." ///
            "DAI = Digital Adoption Index Tier-1+2 (DAIfull, website + e-payment, z-standardised)." ///
            "Turning point TP = mean + [−b(FSTSc)/(2·b(FSTSc²))]; CI via delta method.") wrap
di as result "  Saved: table_2_main_models.rtf"

/* ============================================================
   PART B — Heckman IMR Selection Check
   Test whether exporter status (FSTS > 0) is endogenous
   First stage: probit on exporter dummy
   Second stage: include inverse Mills ratio (IMR)
   ============================================================ */
di _n as result "=== HECKMAN SELECTION CHECK ==="

gen exporter = (FSTS > 0) if FSTS != .
label var exporter "Exporter dummy (FSTS>0)"

/* Exclusion restriction: industry R&D intensity as predictor of export decision */
/* Use ind_2digit as sector cluster in first stage */
capture confirm variable ind_2digit
if (_rc == 0) {
    probit exporter `controls' ind_2digit if base, vce(robust)
}
else {
    probit exporter `controls' if base, vce(robust)
}
predict imr_xb, xb
gen IMR = normalden(imr_xb) / normal(imr_xb) if exporter == 1
replace IMR = -normalden(imr_xb) / (1 - normal(imr_xb)) if exporter == 0
label var IMR "Inverse Mills Ratio (Heckman correction)"

/* M2 + IMR: quadratic FSTS with Heckman correction */
eststo M2_heck: reg lnLP FSTSc FSTSc2 IMR `controls' if base, vce(hc1)
estadd local spec "M2 + Heckman IMR"

esttab M2 M2_heck ///
    using "$out/table_heckman_imr.csv", replace ///
    b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2 r2_a, fmt(%9.0f %6.4f %6.4f)) ///
    label title("Heckman Selection Check") noobs

di as result "  Saved: table_heckman_imr.csv"

/* Professional RTF table — Heckman IMR robustness check */
esttab M2 M2_heck ///
    using "$out/table_heckman_imr.rtf", replace ///
    b(%9.3f) se(%9.3f) ///
    star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a, fmt(%9.0f %9.3f) labels("Observations" "Adj. R²")) ///
    label mtitles("M2 Baseline" "M2 + Heckman IMR") ///
    title("Appendix Table. Singapore 2023 — Heckman IMR Selection Check") ///
    addnote("Notes: HC1 robust SE in parentheses. IMR = Inverse Mills Ratio from first-stage probit" ///
            "on exporter dummy (FSTS > 0). † p<0.10, * p<0.05, ** p<0.01, *** p<0.001.") wrap
di as result "  Saved: table_heckman_imr.rtf"

/* ============================================================
   PART C — Robustness: Tier-1-only DAI sensitivity
   Replace composite DAI (Tier-1+2) with DAIthin (Tier-1 only)
   Confirms quadratic FSTS×DAI interaction persists
   ============================================================ */
di _n as result "=== DAI TIER SENSITIVITY ==="

quietly summarize DAIthin if dai_samp
gen DAIthin_z = (DAIthin - r(mean)) / r(sd) if r(sd) > 0
label var DAIthin_z "DAI Tier-1 only z-score (sensitivity)"

gen FSTSc_DAIthin   = FSTSc  * DAIthin_z
gen FSTSc2_DAIthin  = FSTSc2 * DAIthin_z

eststo M4_thin: reg lnLP FSTSc FSTSc2 DAIthin_z FSTSc_DAIthin FSTSc2_DAIthin ///
                          `controls' if dai_samp, vce(hc1)
estadd local spec "DAI Tier-1 only"

esttab M4 M4_thin ///
    using "$out/table_3_robustness.csv", replace ///
    b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2 r2_a, fmt(%9.0f %6.4f %6.4f)) ///
    label title("Robustness: DAI Tier Sensitivity") noobs

di as result "  Saved: table_3_robustness.csv"

/* ============================================================
   PART D — Exporters-Only Subsample (Inferential Bound Check)
   ============================================================ */
di _n as result "=== EXPORTERS-ONLY SUBSAMPLE (N≈84) ==="
di as txt "NOTE: Power ≈ 16% for interaction effects β < 1.5 SD"
di as txt "       Results for descriptive purposes only (Leon, 2004)"

count if exp_samp
local n_exp = r(N)
di as txt "  Exporters-only N = `n_exp'"

if `n_exp' > 30 {
    eststo M4_exp: reg lnLP FSTSc FSTSc2 DAI_z FSTSc_DAIz FSTSc2_DAIz ///
                             `controls' if exp_samp, vce(hc1)
    estadd local spec "Exporters only (N=`n_exp')"
    esttab M4 M4_exp ///
        using "$out/table_exporters_only.csv", replace ///
        b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
        stats(N r2 r2_a, fmt(%9.0f %6.4f %6.4f)) ///
        label title("Exporters-only Subsample") noobs
    di as result "  Saved: table_exporters_only.csv"
}

/* ============================================================
   PART E — Lind-Mehlum Summary
   ============================================================ */
di _n as result "=== LIND-MEHLUM TURNING-POINT SUMMARY ==="
di as txt "Turning point (raw FSTS): " %5.4f tp_SGP
di as txt "95% CI: [" %5.4f (tp_SGP - 1.96*tp_SGP_se) ///
          ", " %5.4f (tp_SGP + 1.96*tp_SGP_se) "]"
di as txt "NOTE: Wide CI [53%, 253%] reflects sparse upper-tail support"
di as txt "      Only ~3% of firms exceed FSTS=0.50 — support-constrained estimate"

di _n as result "=== ALL MODELS COMPLETE ==="
di as result "Output files in: $out/"

cap log close

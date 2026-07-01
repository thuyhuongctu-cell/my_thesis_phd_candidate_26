/* ============================================================
   P3 Vietnam — 02_run_models.do
   Purpose: Estimate M0–M8 on three waves + pooled
            Lind-Mehlum utest, delta-method turning-point CI
            Paternoster z-test for cross-wave coefficient stability
   Author: Đỗ Thị Thúy Hương
   Date: May 2026

   Input:  data/vietnam_2009_analytic.dta
           data/vietnam_2015_analytic.dta
           data/vietnam_2023_analytic.dta
           data/vietnam_pooled.dta
   Output: results/table_2_main_models.csv
           results/table_lind_mehlum.csv
           results/table_paternoster.csv
           results/table_turning_points.csv
   ============================================================ */

version 17
clear all
set more off
set linesize 200

/* ---- Directory Setup ---------------------------------------- */
global out    "results"
cap mkdir "$out"

/* ---- Install required packages ----------------------------- */
cap ssc install estout,  replace
cap ssc install utest,   replace

/* ---- Local macros ------------------------------------------ */
local controls   "lnEmp firmage foreigndummy"
local waves      "2009 2015 2023"

/* ============================================================
   HELPER MACRO: Run M0–M8 for one wave sample
   Requires: data loaded, FSTS FSTSsq TCIfull DAIthin defined
             sample_base tci_samp dai_samp full_samp flags
   ============================================================ */

/* ============================================================
   PART A — Wave-by-wave estimation
   ============================================================ */

foreach yr in 2009 2015 2023 {

    use "$out/../data/vietnam_`yr'_analytic.dta", clear
    di as result _n "========================================="
    di as result "  WAVE `yr'"
    di as result "========================================="

    /* Centre FSTS at its within-wave mean for better-conditioned quadratic */
    quietly summarize FSTS if base
    local fsts_mean = r(mean)
    gen FSTSc  = FSTS  - `fsts_mean'
    gen FSTSc2 = FSTSc^2
    label var FSTSc  "FSTS centred"
    label var FSTSc2 "FSTSc squared"

    /* Z-standardise TCI and DAI for comparability */
    quietly summarize TCIfull if tci_samp
    gen TCI_z = (TCIfull - r(mean)) / r(sd) if r(sd) > 0
    quietly summarize DAIthin if dai_samp
    gen DAI_z = (DAIthin - r(mean)) / r(sd) if r(sd) > 0
    label var TCI_z "TCI z-score"
    label var DAI_z "DAI z-score"

    /* Interaction terms */
    gen FSTSc_TCIz   = FSTSc  * TCI_z
    gen FSTSc2_TCIz  = FSTSc2 * TCI_z
    gen FSTSc_DAIz   = FSTSc  * DAI_z
    gen FSTSc2_DAIz  = FSTSc2 * DAI_z

    eststo clear

    /* M0: Controls only */
    eststo M0: reg lnLP `controls' if base, vce(hc1)
    estadd local spec "Controls"

    /* M1: FSTS linear */
    eststo M1: reg lnLP FSTSc `controls' if base, vce(hc1)
    estadd local spec "Linear FSTS"

    /* M2: Quadratic FSTS */
    eststo M2: reg lnLP FSTSc FSTSc2 `controls' if base, vce(hc1)
    estadd local spec "Quadratic FSTS"
    quietly utest FSTSc FSTSc2
    estadd scalar lm_p = r(p)

    /* Delta-method turning point: tp = mean - b1/(2*b2) */
    preserve
        quietly nlcom (tp: `fsts_mean' + (-_b[FSTSc]/(2*_b[FSTSc2]))), post
        scalar tp_`yr'     = _b[tp]
        scalar tp_`yr'_se  = _se[tp]
        di as txt "  [M2 `yr'] Turning point = " %5.4f tp_`yr' ///
                  "  (SE = " %5.4f tp_`yr'_se ")"
    restore

    /* M3: Quadratic + TCI level + TCI × FSTS moderation */
    eststo M3: reg lnLP FSTSc FSTSc2 TCI_z FSTSc_TCIz FSTSc2_TCIz ///
                        `controls' if tci_samp, vce(hc1)
    estadd local spec "Quadratic+TCI(interact)"

    /* M4: Quadratic + DAI level + DAI × FSTS moderation */
    eststo M4: reg lnLP FSTSc FSTSc2 DAI_z FSTSc_DAIz FSTSc2_DAIz ///
                        `controls' if dai_samp, vce(hc1)
    estadd local spec "Quadratic+DAI(interact)"

    /* M5: TCI level shift only (no quadratic) */
    eststo M5: reg lnLP TCI_z `controls' if tci_samp, vce(hc1)
    estadd local spec "TCI level"

    /* M6: DAI level shift only */
    eststo M6: reg lnLP DAI_z `controls' if dai_samp, vce(hc1)
    estadd local spec "DAI level"

    /* M7: Both TCI and DAI level shifts (no FSTS) */
    eststo M7: reg lnLP TCI_z DAI_z `controls' if full_samp, vce(hc1)
    estadd local spec "TCI+DAI level"

    /* M8: Full model: quadratic FSTS + TCI + DAI */
    eststo M8: reg lnLP FSTSc FSTSc2 TCI_z DAI_z ///
                        FSTSc_TCIz FSTSc2_TCIz FSTSc_DAIz FSTSc2_DAIz ///
                        `controls' if full_samp, vce(hc1)
    estadd local spec "Full model"

    /* Export wave results */
    esttab M0 M1 M2 M3 M4 M5 M6 M7 M8 ///
        using "$out/table_wave`yr'_models.csv", replace ///
        b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
        stats(N r2 r2_a lm_p, fmt(%9.0f %6.4f %6.4f %6.4f) ///
              labels("N" "R²" "Adj R²" "LM utest p")) ///
        label title("Vietnam `yr' — Main Models") noobs

    di as result "  Saved: table_wave`yr'_models.csv"

    /* Professional RTF table for manuscript (main models M0–M4) */
    esttab M0 M1 M2 M3 M4 ///
        using "$out/table_wave`yr'_main.rtf", replace ///
        b(%9.3f) se(%9.3f) ///
        star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
        stats(N r2_a lm_p, fmt(%9.0f %9.3f %9.3f) ///
              labels("Observations" "Adj. R²" "Lind-Mehlum p")) ///
        label mtitles("M0" "M1" "M2" "M3" "M4") ///
        title("Table 2 (Wave `yr'). Vietnam — Main Threshold Models") ///
        addnote("Notes: HC1 robust SE in parentheses. † p<0.10, * p<0.05, ** p<0.01, *** p<0.001." ///
                "FSTS centred at within-wave mean before quadratic specification." ///
                "TCI = Technological Capability Index (z-standardised)." ///
                "DAI = Digital Adoption Index Tier-1 (website only, z-standardised).") wrap
    di as result "  Saved: table_wave`yr'_main.rtf"
}

/* ============================================================
   PART B — Pooled panel estimation with cluster-robust SE
   ============================================================ */
use "$out/../data/vietnam_pooled.dta", clear

di as result _n "========================================="
di as result "  POOLED (2009 + 2015 + 2023)"
di as result "========================================="

quietly summarize FSTS if base
local fsts_mean = r(mean)
gen FSTSc  = FSTS  - `fsts_mean'
gen FSTSc2 = FSTSc^2

quietly summarize TCIfull if tci_samp
gen TCI_z = (TCIfull - r(mean)) / r(sd) if r(sd) > 0
quietly summarize DAIthin if dai_samp
gen DAI_z = (DAIthin - r(mean)) / r(sd) if r(sd) > 0

gen FSTSc_TCIz   = FSTSc  * TCI_z
gen FSTSc2_TCIz  = FSTSc2 * TCI_z
gen FSTSc_DAIz   = FSTSc  * DAI_z
gen FSTSc2_DAIz  = FSTSc2 * DAI_z

/* Wave dummies for pooled fixed effects */
gen d15 = (wave == 2015)
gen d23 = (wave == 2023)

eststo clear
eststo Mpooled0: reg lnLP d15 d23 `controls' if base, vce(cluster idstd)
eststo Mpooled1: reg lnLP FSTSc d15 d23 `controls' if base, vce(cluster idstd)
eststo Mpooled2: reg lnLP FSTSc FSTSc2 d15 d23 `controls' if base, vce(cluster idstd)
quietly utest FSTSc FSTSc2
estadd scalar lm_p = r(p)

preserve
    quietly nlcom (tp: `fsts_mean' + (-_b[FSTSc]/(2*_b[FSTSc2]))), post
    scalar tp_pooled    = _b[tp]
    scalar tp_pooled_se = _se[tp]
    di as txt "  [Pooled M2] Turning point = " %5.4f tp_pooled ///
              "  (SE = " %5.4f tp_pooled_se ")"
restore

eststo Mpooled3: reg lnLP FSTSc FSTSc2 TCI_z FSTSc_TCIz FSTSc2_TCIz ///
                         d15 d23 `controls' if tci_samp, vce(cluster idstd)
eststo Mpooled4: reg lnLP FSTSc FSTSc2 DAI_z FSTSc_DAIz FSTSc2_DAIz ///
                         d15 d23 `controls' if dai_samp, vce(cluster idstd)
eststo Mpooled5: reg lnLP TCI_z d15 d23 `controls' if tci_samp, vce(cluster idstd)
eststo Mpooled6: reg lnLP DAI_z d15 d23 `controls' if dai_samp, vce(cluster idstd)
eststo Mpooled7: reg lnLP TCI_z DAI_z d15 d23 `controls' if full_samp, vce(cluster idstd)
eststo Mpooled8: reg lnLP FSTSc FSTSc2 TCI_z DAI_z ///
                         FSTSc_TCIz FSTSc2_TCIz FSTSc_DAIz FSTSc2_DAIz ///
                         d15 d23 `controls' if full_samp, vce(cluster idstd)

esttab Mpooled0 Mpooled1 Mpooled2 Mpooled3 Mpooled4 ///
       Mpooled5 Mpooled6 Mpooled7 Mpooled8 ///
    using "$out/table_pooled_models.csv", replace ///
    b(4) se(4) star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2 r2_a lm_p, fmt(%9.0f %6.4f %6.4f %6.4f)) ///
    label title("Vietnam Pooled — Main Models") noobs
di as result "  Saved: table_pooled_models.csv"

/* Professional RTF table — pooled main models (M0–M4) for manuscript */
esttab Mpooled0 Mpooled1 Mpooled2 Mpooled3 Mpooled4 ///
    using "$out/table_pooled_main.rtf", replace ///
    b(%9.3f) se(%9.3f) ///
    star(† 0.10 * 0.05 ** 0.01 *** 0.001) ///
    stats(N r2_a lm_p, fmt(%9.0f %9.3f %9.3f) ///
          labels("Observations" "Adj. R²" "Lind-Mehlum p")) ///
    label mtitles("M0" "M1" "M2" "M3" "M4") ///
    title("Table 3. Vietnam Pooled (2009+2015+2023) — Main Threshold Models") ///
    addnote("Notes: Cluster-robust SE (cluster on firm ID) in parentheses." ///
            "† p<0.10, * p<0.05, ** p<0.01, *** p<0.001. Wave dummies d15 d23 included." ///
            "TCI = Technological Capability Index (z-standardised)." ///
            "DAI = Digital Adoption Index Tier-1 (website only, z-standardised).") wrap
di as result "  Saved: table_pooled_main.rtf"

/* ============================================================
   PART C — Lind-Mehlum Turning-Point Summary Table
   ============================================================ */
di _n as result "=== TURNING-POINT SUMMARY ==="
foreach yr in 2009 2015 2023 {
    di as txt "Wave `yr': TP = " %5.4f scalar(tp_`yr') ///
              "  SE = " %5.4f scalar(tp_`yr'_se) ///
              "  [" %5.4f (scalar(tp_`yr') - 1.96*scalar(tp_`yr'_se)) ///
              ", " %5.4f (scalar(tp_`yr') + 1.96*scalar(tp_`yr'_se)) "]"
}
di as txt "Pooled: TP = " %5.4f scalar(tp_pooled) ///
          "  SE = " %5.4f scalar(tp_pooled_se)

/* ============================================================
   PART D — Paternoster z-Test (Cross-Wave Coefficient Stability)
   Test: are FSTS and FSTSsq coefficients equal across waves?
   ============================================================ */
use "$out/../data/vietnam_pooled.dta", clear

quietly summarize FSTS if base
local fsts_mean = r(mean)
gen FSTSc  = FSTS  - `fsts_mean'
gen FSTSc2 = FSTSc^2
quietly summarize TCIfull if tci_samp
gen TCI_z = (TCIfull - r(mean)) / r(sd) if r(sd) > 0
quietly summarize DAIthin if dai_samp
gen DAI_z = (DAIthin - r(mean)) / r(sd) if r(sd) > 0
gen d15 = (wave == 2015)
gen d23 = (wave == 2023)
gen FSTSc_d15  = FSTSc  * d15
gen FSTSc2_d15 = FSTSc2 * d15
gen FSTSc_d23  = FSTSc  * d23
gen FSTSc2_d23 = FSTSc2 * d23

di _n as result "=== PATERNOSTER Z-TEST ==="
/* M_pat: interacted model — coefficients by wave */
reg lnLP FSTSc FSTSc2 ///
         FSTSc_d15 FSTSc2_d15 ///
         FSTSc_d23 FSTSc2_d23 ///
         d15 d23 `controls' if base, vce(cluster idstd)

/* Wave-specific totals for 2009 base */
di as txt "FSTS (2009 base): b=" %6.4f _b[FSTSc] "  se=" %6.4f _se[FSTSc]
di as txt "FSTS2 (2009 base): b=" %6.4f _b[FSTSc2] "  se=" %6.4f _se[FSTSc2]
/* 2015 vs 2009: test significance of interaction increments */
test FSTSc_d15 = 0
di as txt "Paternoster FSTS: 2009 vs 2015 z=" %5.4f sqrt(r(F)) " p=" %5.4f r(p)
test FSTSc2_d15 = 0
di as txt "Paternoster FSTSsq: 2009 vs 2015 z=" %5.4f sqrt(r(F)) " p=" %5.4f r(p)
test FSTSc_d23 = 0
di as txt "Paternoster FSTS: 2009 vs 2023 z=" %5.4f sqrt(r(F)) " p=" %5.4f r(p)
test FSTSc2_d23 = 0
di as txt "Paternoster FSTSsq: 2009 vs 2023 z=" %5.4f sqrt(r(F)) " p=" %5.4f r(p)

di _n as result "=== ALL MODELS COMPLETE ==="
di as result "Output files in: $out/"

cap log close

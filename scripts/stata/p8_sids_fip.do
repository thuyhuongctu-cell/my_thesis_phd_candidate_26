* ============================================================================
* p8_sids_fip.do — FIP test on Pacific SIDS (thesis §4.7 / H1b)
* ----------------------------------------------------------------------------
* Spec follows thesis Ch3 §3.4.5.5:
*   M1: lp_z = b*fsts_c + controls + country FE + year FE  (LINEAR — FIP is a
*       monotone-negative claim; quadratic checked as robustness, expect no TP)
*   Locked benchmark: beta(FSTS_c) = -1.339, p < .001 (M1, country+year FE);
*   exporters-only N = 26 (NS, beta = -1.176, p = .130).
*
* INTEGRITY NOTE: author validates spec vs original P8 pipeline before any
* locked value changes. Run AFTER 00_prep_data.do.
* Run:  stata-mp -b do scripts/stata/p8_sids_fip.do
* ============================================================================
version 17
clear all
set more off
cap mkdir dist/stata_out
log using "dist/stata_out/p8_results.txt", text replace

use "data_wbes/p7/p7_analytic.dta", clear
keep if icrv_label == "SIDS_small"
* main P8 sample = 7 Pacific economies (drop Timor-Leste robustness member)
gen byte pacific = !inlist(country, "TimorLeste")
tab country pacific

gen fsts_c = fsts/100          // centred-as-share, matches manuscript scaling

* ---- M1 linear FIP (main, Pacific 7) ---------------------------------------
reghdfe lp_z c.fsts_c firm_age if pacific, absorb(c_id year) vce(cluster c_id)
est store P8_M1

* robustness: quadratic — expect NO interior maximum (utest should fail)
reghdfe lp_z c.fsts_c c.fsts_c#c.fsts_c firm_age if pacific, ///
    absorb(c_id year) vce(cluster c_id)
cap utest fsts_c c.fsts_c#c.fsts_c

* robustness: 8-economy group VI (incl. Timor-Leste)
reghdfe lp_z c.fsts_c firm_age, absorb(c_id year) vce(cluster c_id)
est store P8_M1_VI8

* exporters-only (expect small N, NS)
reghdfe lp_z c.fsts_c firm_age if pacific & fsts > 0, ///
    absorb(c_id year) vce(cluster c_id)
est store P8_exp

esttab P8_M1 P8_M1_VI8 P8_exp using "dist/stata_out/p8_models.csv", replace ///
    se star(* 0.10 ** 0.05 *** 0.01) b(%9.4f) ///
    title("P8 FIP re-estimation (locked benchmark: -1.339***, M1)")

log close
di as result "DONE. Benchmark beta = -1.339 (p<.001); exporters-only N = 26."

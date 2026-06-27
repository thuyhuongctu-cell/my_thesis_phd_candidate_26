* ============================================================================
* p7_reestimate.do — P7 quadratic I–P models on the 49-economy frame
* ----------------------------------------------------------------------------
* Spec follows thesis Ch3 §3.4.5.4 / Appendix A §A.6:
*   M2: lp_z = b1*fsts + b2*fsts2 + country FE + year FE
*   M5: + firm_age, ln(size), foreign ownership, tci_z, dai_z
*   TP  = -b1/(2*b2); existence test: Lind–Mehlum (utest)
*   SE clustered by country.
* Per-ICRV turning points estimated by group for the gradient (Bảng/§4.6.2).
*
* INTEGRITY NOTE: this re-implements the *described* specification. Before any
* number replaces a locked thesis value, the AUTHOR must confirm this spec
* matches the original P7 pipeline (PPP handling, weights, trimming) — see
* data_wbes/analysis/P7_REESTIMATION_NOTE.md. New waves + Japan can be added
* by re-running scripts/build_pooled_dataset.py upstream first.
*
* Requires: ssc install reghdfe ftools utest estout  (one-time)
* Run:      stata-mp -b do scripts/stata/p7_reestimate.do
* Output:   dist/stata_out/p7_results.txt + p7_models.ster
* ============================================================================
version 17
clear all
set more off
cap mkdir dist
cap mkdir dist/stata_out
log using "dist/stata_out/p7_results.txt", text replace

use "data_wbes/p7/p7_analytic.dta", clear

* ---- controls ---------------------------------------------------------------
destring l1_workers_raw, replace force
gen ln_size = ln(l1_workers_raw) if l1_workers_raw > 0
gen fown    = foreign_own_pct

* ============================ M2 (baseline) ==================================
reghdfe lp_z c.fsts c.fsts2, absorb(c_id year) vce(cluster c_id)
est store M2
nlcom TP_M2: -_b[fsts]/(2*_b[fsts2])
utest fsts fsts2

* ============================ M5 (full controls) =============================
reghdfe lp_z c.fsts c.fsts2 firm_age ln_size fown tci_z dai_z, ///
    absorb(c_id year) vce(cluster c_id)
est store M5
nlcom TP_M5: -_b[fsts]/(2*_b[fsts2])
utest fsts fsts2

* ===================== Per-ICRV turning-point gradient =======================
levelsof icrv_id, local(groups)
foreach g of local groups {
    di as result _n "===== ICRV group `g' ====="
    qui count if icrv_id == `g'
    if r(N) > 500 {
        reghdfe lp_z c.fsts c.fsts2 firm_age, ///
            absorb(c_id year) vce(cluster c_id), if icrv_id == `g'
        cap nlcom TP: -_b[fsts]/(2*_b[fsts2])
        cap utest fsts fsts2
    }
    else di as txt "  (skipped: N too small)"
}

* ===================== Moderation (M11-style, 3-way) =========================
reghdfe lp_z c.fsts##c.fsts##(c.tci_z c.dai_z) firm_age ln_size, ///
    absorb(c_id year) vce(cluster c_id)
est store M11

esttab M2 M5 M11 using "dist/stata_out/p7_models.csv", replace ///
    se star(* 0.10 ** 0.05 *** 0.01) b(%9.4f) ///
    title("P7 re-estimation — 49-economy frame (author to validate vs locked)")

log close
di as result "DONE. Compare TP_M5 with locked thesis value 40.0% before any update."

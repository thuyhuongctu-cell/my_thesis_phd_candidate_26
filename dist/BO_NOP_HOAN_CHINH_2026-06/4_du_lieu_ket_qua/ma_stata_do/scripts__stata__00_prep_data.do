* ============================================================================
* 00_prep_data.do — Build Stata analytic dataset from the pooled master CSV
* ----------------------------------------------------------------------------
* Input : data_wbes/p7/p7_pooled_clean.csv  (106,765 firm-year records)
* Output: data_wbes/p7/p7_analytic.dta      (49-economy analytic frame)
*
* Implements Appendix A steps S5–S6 + the currency-artifact correction:
*   - drop out-of-region economies (Comoros, Cyprus, Turkey) and panel labels
*   - keep ICRV-classified records
*   - lp_z = z-standardised ln(labour productivity) WITHIN country-year
*   - fsts in [0,100]; fsts2 = fsts^2
*
* Run:  stata-mp -b do scripts/stata/00_prep_data.do   (from repo root)
* ============================================================================
version 17
clear all
set more off

import delimited "data_wbes/p7/p7_pooled_clean.csv", varnames(1) bindquote(strict) encoding(utf8) clear

* ---- S5: frame restriction -------------------------------------------------
drop if inlist(country, "Philippines_panel", "Nepal_panel", "Mongolia_panel")
drop if inlist(country, "Comoros", "Cyprus", "Turkey")
drop if missing(icrv_label)

* ---- focal variables ---------------------------------------------------------
destring ln_labor_prod fsts_pct firm_age tci_z dai_z foreign_own_pct, replace force
keep if !missing(ln_labor_prod) & !missing(fsts_pct)
gen fsts  = fsts_pct
replace fsts = . if fsts < 0 | fsts > 100
gen fsts2 = fsts^2

* ---- currency-artifact correction: z within country-year -------------------
egen cy = group(country year)
bysort cy: egen lp_mu = mean(ln_labor_prod)
bysort cy: egen lp_sd = sd(ln_labor_prod)
gen lp_z = (ln_labor_prod - lp_mu) / lp_sd if lp_sd > 0
drop lp_mu lp_sd

* ---- encode FE dimensions ----------------------------------------------------
encode country,    gen(c_id)
encode icrv_label, gen(icrv_id)

label data "WBES 49-economy analytic frame (Appendix A S1-S6)"
compress
save "data_wbes/p7/p7_analytic.dta", replace

di as result "Saved p7_analytic.dta — N = " _N

/* ============================================================
   P8 — Wild-cluster bootstrap for the FIP coefficient (7 Pacific SIDS)
   Official few-cluster inference for the World Development submission.
   Run in YOUR authoritative Stata environment on the P8 analytic data
   that reproduces M1 β(fsts_c) = −1.339 (the version used in the paper).

   Requires: ssc install boottest   (Roodman et al. 2019)
   With only 7 clusters, Webb 6-point weights are recommended over
   Rademacher (Cameron, Gelbach & Miller 2008; Roodman et al. 2019).
   ============================================================ */
version 17
clear all
set more off

* ---- 1. Load the P8 analytic dataset (the build that gives β=−1.339) ----
*    Adjust the path to your authoritative P8 estimation sample.
use "p8/replication/data/p8_pacific7_analytic.dta", clear   // <-- set to your file

* keep the 7 genuine Pacific SIDS (drop Comoros, Timor-Leste) if not already
* keep if inlist(country,"Fiji","Kiribati","PapuaNewGuinea","Samoa","SolomonIslands","Tonga","Vanuatu")

* centred FSTS (as in the paper)
quietly summarize fsts
gen fsts_c = fsts - r(mean)

* ---- 2. M1: FIP baseline (country + year FE, cluster by economy) ----
reg ln_labor_prod fsts_c ln_size firm_age foreign_own_pct i.country i.year, ///
    vce(cluster country)
* sanity check: the fsts_c coefficient should be ≈ −1.339
di "M1 FIP coefficient (should be ~ -1.339): " _b[fsts_c]

* ---- 3. Wild-cluster bootstrap on the FIP coefficient ----
* Webb 6-point weights (recommended for <12 clusters); 9999 reps; bootstrap CI.
boottest fsts_c, reps(9999) weighttype(webb) cluster(country) ///
    boottype(wild) nograph seed(42)
* boottest reports: wild-cluster p-value + 95% confidence interval for β(fsts_c).

* ---- 4. (optional) Rademacher enumeration is exact at 2^7 = 128 draws ----
* boottest fsts_c, reps(127) weighttype(rademacher) cluster(country) nograph

/* Report in the manuscript §4.4:
   "A wild-cluster restricted bootstrap (Webb weights, 9,999 replications,
    clustered by economy; Roodman et al. 2019) yields p = [__] for the FIP
    coefficient, with a 95% bootstrap CI of [__ , __]."
   Few-cluster inference is anchored on this bootstrap together with the
   sign-consistency of the FSTS coefficient across all five specifications. */

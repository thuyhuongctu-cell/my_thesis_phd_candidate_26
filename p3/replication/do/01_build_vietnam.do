/* ============================================================
   P3 Vietnam WBES Build Script
   Purpose: Build analytic dataset from WBES Vietnam 2009/2015/2023
   Author: Đỗ Thị Thúy Hương
   Date: May 2026

   Output: vietnam_2009_analytic.dta
           vietnam_2015_analytic.dta
           vietnam_2023_analytic.dta
   ============================================================ */

version 17
clear all
set more off
set linesize 120

/* ---- Directory Setup ---------------------------------------- */
global data   "../../../data_wbes"
global out    "data"

/* ============================================================
   WAVE 1: WBES Vietnam 2009 (PICS3 schema)
   ============================================================ */
use "$data/Vietnam_2009.dta", clear

/* -- Outcome: Labour Productivity -- */
gen lnLP = ln(d2 / b1_d)           // ln(annual sales / number of workers)
replace lnLP = . if lnLP == .
label var lnLP "ln(Labour Productivity) — annual sales per worker"

/* -- Export intensity (FSTS) -- */
gen FSTS = d3b / 100                // foreign sales share (0–1 scale)
replace FSTS = 0 if d3b == 0 | d3b == .
replace FSTS = . if FSTS < 0 | FSTS > 1
label var FSTS "Export intensity (Foreign Sales / Total Sales)"
gen FSTSsq = FSTS^2
label var FSTSsq "FSTS squared (nonlinear term)"

/* -- Technological Capability Index (TCI) -- */
// Items: quality certification (b8), foreign technology license (e6)
// TCI = z-standardised mean of available items
gen tci_cert  = (b8 == 1) if b8 != .
gen tci_tech  = (e6 == 1) if e6 != .
egen TCI_raw  = rowmean(tci_cert tci_tech)
egen TCI_mean = mean(TCI_raw)
egen TCI_sd   = sd(TCI_raw)
gen  TCIfull  = (TCI_raw - TCI_mean) / TCI_sd if TCI_sd > 0
label var TCIfull "TCI — z-standardised (certification + foreign tech license)"

/* -- Digital Adoption Index (DAI) — Tier 1 only for 2009 -- */
gen DAIthin = (c22b == 1) if c22b != .     // website presence only
label var DAIthin "DAI Tier-1 — website presence (Spec 1; 2009 wave)"

/* -- Controls -- */
gen lnEmp   = ln(b1_d) if b1_d > 0
gen firmage = b4       if b4 >= 0
gen foreigndummy = (b2b >= 10) if b2b != .
label var lnEmp      "ln(Number of employees)"
label var firmage    "Firm age (years since establishment)"
label var foreigndummy "Foreign ownership ≥10% dummy"

/* -- Sample Flags -- */
gen analytic = (!missing(lnLP, FSTS, lnEmp))
gen base     = analytic & !missing(firmage, foreigndummy)
gen tci_samp = base & !missing(TCIfull)
gen dai_samp = base & !missing(DAIthin)
gen full_samp = base & !missing(TCIfull, DAIthin)

gen wave = 2009
label var wave "Survey wave year"

/* -- Winsorize lnLP at 1/99 within wave -- */
quietly summarize lnLP if analytic, detail
replace lnLP = r(p1)  if lnLP < r(p1)  & analytic
replace lnLP = r(p99) if lnLP > r(p99) & analytic

di "Wave 2009 — Analytic N = " _N " full_samp N = " as result `=sum(full_samp)'

/* -- Audit -- */
count if analytic
count if base
count if full_samp

keep if analytic
save "$out/vietnam_2009_analytic.dta", replace

/* ============================================================
   WAVE 2: WBES Vietnam 2015 (Standardized schema)
   ============================================================ */
use "$data/Vietnam_2015.dta", clear

gen lnLP    = ln(d2 / b1_d) if b1_d > 0
gen FSTS    = d3b / 100
replace FSTS = 0 if d3b == 0 | d3b == .
replace FSTS = . if FSTS < 0 | FSTS > 1
gen FSTSsq  = FSTS^2

gen tci_cert = (b8 == 1) if b8 != .
gen tci_tech = (e6 == 1) if e6 != .
egen TCI_raw = rowmean(tci_cert tci_tech)
egen TCI_mean = mean(TCI_raw)
egen TCI_sd   = sd(TCI_raw)
gen  TCIfull  = (TCI_raw - TCI_mean) / TCI_sd if TCI_sd > 0

// 2015: website only (c22b variable present but BREADY modules not in 2015)
gen DAIthin = (c22b == 1) if c22b != .

gen lnEmp      = ln(b1_d) if b1_d > 0
gen firmage    = b4       if b4 >= 0
gen foreigndummy = (b2b >= 10) if b2b != .

gen analytic = (!missing(lnLP, FSTS, lnEmp))
gen base     = analytic & !missing(firmage, foreigndummy)
gen tci_samp = base & !missing(TCIfull)
gen dai_samp = base & !missing(DAIthin)
gen full_samp = base & !missing(TCIfull, DAIthin)

gen wave = 2015
quietly summarize lnLP if analytic, detail
replace lnLP = r(p1)  if lnLP < r(p1)  & analytic
replace lnLP = r(p99) if lnLP > r(p99) & analytic

di "Wave 2015 — Analytic N = " _N " full_samp N = " as result `=sum(full_samp)'
keep if analytic
save "$out/vietnam_2015_analytic.dta", replace

/* ============================================================
   WAVE 3: WBES Vietnam 2023 (BREADY schema)
   ============================================================ */
use "$data/Vietnam_2023.dta", clear

gen lnLP    = ln(d2 / b1_d) if b1_d > 0
gen FSTS    = d3b / 100
replace FSTS = 0 if d3b == 0 | d3b == .
replace FSTS = . if FSTS < 0 | FSTS > 1
gen FSTSsq  = FSTS^2

gen tci_cert  = (b8 == 1) if b8 != .
gen tci_tech  = (e6 == 1) if e6 != .
// 2023: also try h8 (imported machinery) if available
capture gen tci_mach = (h8 == 1) if h8 != .
capture gen tci_iso  = (h1 == 1) if h1 != .
quietly: capture confirm variable tci_mach tci_iso
if (_rc == 0) {
    egen TCI_raw = rowmean(tci_cert tci_tech tci_mach tci_iso)
}
else {
    egen TCI_raw = rowmean(tci_cert tci_tech)
}
egen TCI_mean = mean(TCI_raw)
egen TCI_sd   = sd(TCI_raw)
gen  TCIfull  = (TCI_raw - TCI_mean) / TCI_sd if TCI_sd > 0

// 2023 BREADY: Tier 1 (website c22b) + Tier 2 (e-payment k33/k38)
gen dai_web  = (c22b == 1) if c22b != .
capture gen dai_pay = (k33 == 1 | k38 == 1) if (k33 != . | k38 != .)
capture confirm variable dai_pay
if (_rc == 0) {
    egen DAI_raw = rowmean(dai_web dai_pay)
    gen  DAItier2 = dai_pay
    label var DAItier2 "DAI Tier-2 — e-payment (k33/k38)"
}
else {
    gen DAI_raw = dai_web
}
gen DAIthin = dai_web
label var DAIthin "DAI Tier-1 — website presence"

gen lnEmp      = ln(b1_d) if b1_d > 0
gen firmage    = b4       if b4 >= 0
gen foreigndummy = (b2b >= 10) if b2b != .

gen analytic = (!missing(lnLP, FSTS, lnEmp))
gen base     = analytic & !missing(firmage, foreigndummy)
gen tci_samp = base & !missing(TCIfull)
gen dai_samp = base & !missing(DAIthin)
gen full_samp = base & !missing(TCIfull, DAIthin)

gen wave = 2023
quietly summarize lnLP if analytic, detail
replace lnLP = r(p1)  if lnLP < r(p1)  & analytic
replace lnLP = r(p99) if lnLP > r(p99) & analytic

di "Wave 2023 — Analytic N = " _N " full_samp N = " as result `=sum(full_samp)'
keep if analytic
save "$out/vietnam_2023_analytic.dta", replace

/* ============================================================
   BUILD POOLED DATASET
   ============================================================ */
use "$out/vietnam_2009_analytic.dta", clear
append using "$out/vietnam_2015_analytic.dta"
append using "$out/vietnam_2023_analytic.dta"

// Cross-wave interaction for Paternoster test
gen FSTS_w15  = FSTS    * (wave == 2015)
gen FSTSsq_w15= FSTSsq  * (wave == 2015)
gen FSTS_w23  = FSTS    * (wave == 2023)
gen FSTSsq_w23= FSTSsq  * (wave == 2023)

// Industry fixed effects (ISIC 2-digit groups)
gen ind_fe = int(isic / 10) if isic != .

di "Pooled Vietnam — Total N = " _N

save "$out/vietnam_pooled.dta", replace
di "Saved: vietnam_pooled.dta"

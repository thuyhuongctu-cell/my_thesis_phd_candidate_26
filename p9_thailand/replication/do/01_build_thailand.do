/* ============================================================
   P9 Thailand WBES — 01_build_thailand.do
   Purpose: Build analytic dataset from WBES Thailand 2016 + 2025
   Author: Đỗ Thùy Hương (NCS) · PGS.TS. Phan Anh Tú
   Date: June 2026

   Input:  $data/Thailand_2016.dta  (WBES Standardized schema)
           $data/Thailand_2025.dta  (WBES BREADY/BEE schema)
   Output: thailand_2016_analytic.dta
           thailand_2025_analytic.dta
           thailand_pooled_analytic.dta

   Sample:  Thailand 2016: N_raw = 1,000;  N_complete_core = 705
            Thailand 2025: N_raw =   813;  N_complete_core = 766
            Pooled:        N = 1,471 firms

   Theoretical window: pre-COVID, pre-RCEP (2016) vs post-COVID, post-RCEP
                       (2025, RCEP into force Jan 2022)
   ============================================================ */

version 17
clear all
set more off
set linesize 120

/* ---- Directory Setup ---------------------------------------- */
global data   "../../../data_wbes/raw_dta"
global out    "data"
cap mkdir "$out"

cap log close
log using "build_thailand.log", replace text

/* ============================================================
   WAVE 1: WBES Thailand 2016 (Standardized schema, PICS3 / pre-BREADY)
   ============================================================ */
use "$data/Thailand_2016.dta", clear

/* -- Outcome: Labour Productivity -- */
gen lnLP = ln(d2 / l1)              // ln(annual sales / number of workers)
replace lnLP = . if d2 <= 0 | l1 <= 0
label var lnLP "ln(Labour Productivity) — annual sales per worker"

/* -- Export intensity (FSTS = direct + indirect exports) -- */
gen FSTS = (d3b + d3c) / 100
replace FSTS = 0 if d3b == 0 & d3c == 0
replace FSTS = . if FSTS < 0 | FSTS > 1
label var FSTS "Export intensity (Direct + Indirect Exports / Total Sales)"
gen FSTSsq = FSTS^2
label var FSTSsq "FSTS squared (nonlinear term)"
gen FSTS_c = FSTS - 0.10            // mean-centered (Thailand FSTS mean ~ 0.10)
gen FSTS_c2 = FSTS_c^2

/* -- Technological Capability Index (TCI) -- */
// Items: quality certification (b8), foreign technology license (e6),
//        product innovation (h1), R&D activity (h8)
gen tci_cert = (b8 == 1) if b8 != .
gen tci_tech = (e6 == 1) if e6 != .
gen tci_inno = (h1 == 1) if h1 != .
gen tci_rd   = (h8 == 1) if h8 != .
egen TCI_raw = rowmean(tci_cert tci_tech tci_inno tci_rd)
egen n_tci_items = rowtotal(tci_cert tci_tech tci_inno tci_rd), missing
egen TCI_mean = mean(TCI_raw) if n_tci_items >= 3
egen TCI_sd   = sd(TCI_raw) if n_tci_items >= 3
gen TCI_full  = (TCI_raw - TCI_mean) / TCI_sd if n_tci_items >= 3
label var TCI_full "TCI — z-standardised (cert + foreign tech + innov + R&D), ≥3 items"

/* -- Digital Adoption Index (DAI) — Tier 1: website only for 2016 -- */
gen DAI_core = (c22b == 1) if c22b != .
label var DAI_core "DAI Tier-1 (own-website binary)"

/* -- Controls -- */
gen lnEmp = ln(l1)
replace lnEmp = . if l1 <= 0
label var lnEmp "ln(permanent full-time employees)"

gen firmage = (2016 - b5) if b5 != .
label var firmage "Firm age in years"

gen foreigndummy = (b2b >= 10) if b2b != .
label var foreigndummy "Foreign-owned (≥10% foreign ownership)"

/* -- ISIC sector code (a4a — 2-digit) -- */
gen isic2 = floor(a4a)
label var isic2 "ISIC 2-digit sector"

/* -- Wave indicator -- */
gen wave_2025 = 0
gen wave = "2016"

/* -- Sample flag for focal-variable complete cases -- */
gen sample_base = !missing(lnLP, FSTS, lnEmp, firmage, foreigndummy)
gen sample_full = sample_base & !missing(TCI_full, DAI_core)

/* -- Verify sample sizes match manifest -- */
count if sample_base
* expect N ≈ 1,000 raw; 705 complete-core

/* -- Save -- */
keep if sample_base
order country year_lab wave wave_2025 lnLP FSTS FSTSsq FSTS_c FSTS_c2 TCI_full DAI_core ///
      lnEmp firmage foreigndummy isic2 sample_base sample_full
save "$out/thailand_2016_analytic.dta", replace
display "Thailand 2016 saved: " _N " firms (sample_base)"

/* ============================================================
   WAVE 2: WBES Thailand 2025 (BREADY/BEE schema)
   ============================================================ */
use "$data/Thailand_2025.dta", clear

/* -- Outcome: Labour Productivity (BREADY uses n3, l1) -- */
gen lnLP = ln(n3 / l1)              // n3 = total sales (BREADY); l1 = workers
replace lnLP = . if n3 <= 0 | l1 <= 0
label var lnLP "ln(Labour Productivity)"

/* -- Export intensity (BREADY uses d3a, d3b, d3c with -7 / -8 / -9 codes) -- */
foreach v in d3a d3b d3c {
    replace `v' = . if `v' < 0           // recode -7/-8/-9 as missing
}
gen FSTS = (d3b + d3c) / 100
replace FSTS = 0 if d3b == 0 & d3c == 0
replace FSTS = . if FSTS < 0 | FSTS > 1
label var FSTS "Export intensity (Direct + Indirect Exports / Total Sales)"
gen FSTSsq = FSTS^2
gen FSTS_c = FSTS - 0.10
gen FSTS_c2 = FSTS_c^2

/* -- TCI (same items, BREADY-compatible) -- */
gen tci_cert = (b8 == 1) if b8 != .
gen tci_tech = (e6 == 1) if e6 != .
gen tci_inno = (h1 == 1) if h1 != .
gen tci_rd   = (h8 == 1) if h8 != .
egen TCI_raw = rowmean(tci_cert tci_tech tci_inno tci_rd)
egen n_tci_items = rowtotal(tci_cert tci_tech tci_inno tci_rd), missing
egen TCI_mean = mean(TCI_raw) if n_tci_items >= 3
egen TCI_sd   = sd(TCI_raw) if n_tci_items >= 3
gen TCI_full  = (TCI_raw - TCI_mean) / TCI_sd if n_tci_items >= 3
label var TCI_full "TCI — z-standardised within 2025 wave"

/* -- DAI core (Tier-1 website) + extended Tier-2 (BREADY adds e-payment) -- */
gen DAI_core = (c22b == 1) if c22b != .
label var DAI_core "DAI Tier-1 (own-website binary)"

gen DAI_epay = .
capture confirm variable k33
if !_rc {
    replace k33 = . if k33 < 0
    replace DAI_epay = k33 / 100 if k33 != .
    label var DAI_epay "DAI Tier-2 (% e-payment from customers, 2025 BREADY only)"
}

/* -- Controls (use 2025 codes) -- */
gen lnEmp = ln(l1)
replace lnEmp = . if l1 <= 0

gen firmage = (2025 - b5) if b5 != .
gen foreigndummy = (b2b >= 10) if b2b != .

gen isic2 = floor(d1a2_v4)            // BREADY uses d1a2_v4 for 2-digit ISIC Rev 4
replace isic2 = floor(a4a) if missing(isic2)

gen wave_2025 = 1
gen wave = "2025"

gen sample_base = !missing(lnLP, FSTS, lnEmp, firmage, foreigndummy)
gen sample_full = sample_base & !missing(TCI_full, DAI_core)

count if sample_base
* expect N ≈ 813 raw; 766 complete-core

keep if sample_base
order country year_lab wave wave_2025 lnLP FSTS FSTSsq FSTS_c FSTS_c2 TCI_full DAI_core DAI_epay ///
      lnEmp firmage foreigndummy isic2 sample_base sample_full
save "$out/thailand_2025_analytic.dta", replace
display "Thailand 2025 saved: " _N " firms (sample_base)"

/* ============================================================
   POOLED: stack 2016 + 2025 for cross-wave Paternoster z-test
   ============================================================ */
use "$out/thailand_2016_analytic.dta", clear
append using "$out/thailand_2025_analytic.dta", force

label var wave_2025 "1 if wave = 2025, else 0 (2016 baseline)"

* Cross-wave interactions
gen FSTS_x_2025  = FSTS * wave_2025
gen FSTS2_x_2025 = FSTSsq * wave_2025
gen TCI_x_2025   = TCI_full * wave_2025
gen DAI_x_2025   = DAI_core * wave_2025

save "$out/thailand_pooled_analytic.dta", replace
display "Pooled Thailand 2016+2025 saved: " _N " firm-year obs"

count if wave_2025 == 0
display "  2016 wave: " r(N) " firms"
count if wave_2025 == 1
display "  2025 wave: " r(N) " firms"

log close
exit

/* ============================================================
   P9 India WBES — 01_build_india.do  (3-wave design)
   Purpose: Build analytic dataset from WBES India 2014 + 2022 + 2025
   Authors: Đỗ Thùy Hương (NCS) · PGS.TS. Phan Anh Tú
   Date: June 2026

   Input:  $data/India-2014-full-data.dta  (PICS3 schema, N=9,281)
           $data/India-2022-full-data.dta  (BEE intermediate, N=9,376)
           $data/India-2025-full-data.dta  (BREADY full, N=10,479)
   Output: india_{2014,2022,2025}_analytic.dta
           india_pooled_analytic.dta  (~29,000 firm-year obs)

   Design — Two complementary specifications:
   (1) PRIMARY: 2-wave (2014 vs 2025), 11-year max window, full DAI Tier-1+2
   (2) ROBUST:  3-wave pooled with linear/non-linear time trend

   Theoretical window 2014 → 2025:
   - Pre-UPI (Apr 2016)         → Post-UPI saturation (12 B txn/month)
   - Pre-demonetisation (2016)  → Post (cashless transition complete)
   - Pre-GST (Jul 2017)         → Post-GST decade
   - Pre-IBC (May 2016)         → Post-IBC bankruptcy reform
   - Pre-PLI scheme (2020)      → Post-PLI manufacturing rollout
   - Pre-COVID                  → Post-COVID recovery (2025)
   - Pre-Atmanirbhar Bharat     → Post-self-reliance policy

   Differentiation from book chapter (Do & Phan 2025, IntechOpen,
   DOI 10.5772/intechopen.1011012):
   ┌───────────────────┬──────────────────────┬──────────────────────┐
   │ Dimension         │ Book Chapter         │ THIS PAPER (P9'')    │
   ├───────────────────┼──────────────────────┼──────────────────────┤
   │ DV                │ ROS (returns/sales)  │ lnLP (productivity)  │
   │ IV specification  │ Linear DOI           │ Quadratic FSTS       │
   │ Theoretical frame │ Uppsala + UE Theory  │ CDCM framework       │
   │ Moderators        │ TMT exp + gender     │ TCI + DAI capability │
   │ Method            │ FGLS                 │ OLS-HC1 + Lind-Mehlum│
   │                   │                      │     + Paternoster z  │
   │ Sample            │ N=760 matched panel  │ N≈18,000-29,000      │
   │ Waves             │ 2 unspecified waves  │ 2014/2022/2025 full  │
   │ Key claim         │ Negative linear I-P  │ Inverted-U threshold │
   │                   │                      │  stability over 11y  │
   └───────────────────┴──────────────────────┴──────────────────────┘
   ============================================================ */

version 17
clear all
set more off
set linesize 120

global data   "../../../data_wbes/raw_dta"
global out    "data"
cap mkdir "$out"

cap log close
log using "build_india.log", replace text

/* ============================================================
   Helper program — common variable construction across waves
   ============================================================ */
program define build_india_wave
    args wave_year
    di as result _n "===== INDIA " `wave_year' " =====" _n

    /* -- Outcome: ln(labour productivity) -- */
    capture confirm variable d2
    if _rc gen d2 = n3
    gen lnLP = ln(d2 / l1)
    replace lnLP = . if d2 <= 0 | l1 <= 0
    label var lnLP "ln(Labour Productivity)"

    /* -- Export intensity (handle -7/-8/-9 codes) -- */
    foreach v in d3a d3b d3c {
        replace `v' = . if `v' < 0
    }
    gen FSTS = (d3b + d3c) / 100
    replace FSTS = 0 if d3b == 0 & d3c == 0
    replace FSTS = . if FSTS < 0 | FSTS > 1
    label var FSTS "Export intensity (Direct + Indirect / Total Sales)"
    gen FSTSsq = FSTS^2
    gen FSTS_c = FSTS - 0.10
    gen FSTS_c2 = FSTS_c^2

    /* -- TCI: certification + foreign tech + product innov + R&D -- */
    gen tci_cert = (b8 == 1) if b8 != .
    gen tci_tech = (e6 == 1) if e6 != .
    gen tci_inno = (h1 == 1) if h1 != .
    gen tci_rd   = (h8 == 1) if h8 != .
    egen TCI_raw = rowmean(tci_cert tci_tech tci_inno tci_rd)
    egen n_tci_items = rowtotal(tci_cert tci_tech tci_inno tci_rd), missing
    egen TCI_mean = mean(TCI_raw) if n_tci_items >= 3
    egen TCI_sd   = sd(TCI_raw) if n_tci_items >= 3
    gen TCI_full  = (TCI_raw - TCI_mean) / TCI_sd if n_tci_items >= 3
    label var TCI_full "TCI — z-standardised within wave (>=3 items)"

    /* -- DAI Tier-1: website binary (available all waves) -- */
    gen DAI_core = (c22b == 1) if c22b != .
    label var DAI_core "DAI Tier-1 (own-website binary)"

    /* -- DAI Tier-2: e-payment from customers (k33, BREADY 2025 only) -- */
    gen DAI_epay = .
    capture confirm variable k33
    if !_rc {
        replace k33 = . if k33 < 0
        replace DAI_epay = k33 / 100 if k33 != .
        label var DAI_epay "DAI Tier-2 (% e-payment from customers, BREADY 2025 only)"
    }

    /* -- Controls -- */
    gen lnEmp = ln(l1)
    replace lnEmp = . if l1 <= 0
    gen firmage = (`wave_year' - b5) if b5 != .
    gen foreigndummy = (b2b >= 10) if b2b != .

    /* -- ISIC sector (PICS3 uses a4a; BEE/BREADY use d1a2_v4) -- */
    capture confirm variable d1a2_v4
    if !_rc {
        gen isic2 = floor(d1a2_v4)
        replace isic2 = floor(a4a) if missing(isic2)
    }
    else {
        gen isic2 = floor(a4a)
    }

    /* -- Wave indicators -- */
    gen wave = "`wave_year'"
    gen year_num = `wave_year'

    gen sample_base = !missing(lnLP, FSTS, lnEmp, firmage, foreigndummy)
    gen sample_full = sample_base & !missing(TCI_full, DAI_core)

    count if sample_base
end

/* ============================================================
   WAVE 1: 2014 (PICS3, pre-reform-decade)
   ============================================================ */
use "$data/India-2014-full-data.dta", clear
build_india_wave 2014
gen wave_2022 = 0
gen wave_2025 = 0
keep if sample_base
order country year wave year_num wave_2022 wave_2025 lnLP FSTS FSTSsq FSTS_c FSTS_c2 ///
      TCI_full DAI_core DAI_epay lnEmp firmage foreigndummy isic2 sample_base sample_full
save "$out/india_2014_analytic.dta", replace
display "India 2014 saved: " _N " firms (sample_base)"

/* ============================================================
   WAVE 2: 2022 (BEE intermediate, post-COVID, post-major-reforms)
   ============================================================ */
use "$data/India-2022-full-data.dta", clear
build_india_wave 2022
gen wave_2022 = 1
gen wave_2025 = 0
keep if sample_base
order country year wave year_num wave_2022 wave_2025 lnLP FSTS FSTSsq FSTS_c FSTS_c2 ///
      TCI_full DAI_core DAI_epay lnEmp firmage foreigndummy isic2 sample_base sample_full
save "$out/india_2022_analytic.dta", replace
display "India 2022 saved: " _N " firms (sample_base)"

/* ============================================================
   WAVE 3: 2025 (BREADY, post-PLI maturation, UPI saturated)
   ============================================================ */
use "$data/India-2025-full-data.dta", clear
build_india_wave 2025
gen wave_2022 = 0
gen wave_2025 = 1
keep if sample_base
order country year wave year_num wave_2022 wave_2025 lnLP FSTS FSTSsq FSTS_c FSTS_c2 ///
      TCI_full DAI_core DAI_epay lnEmp firmage foreigndummy isic2 sample_base sample_full
save "$out/india_2025_analytic.dta", replace
display "India 2025 saved: " _N " firms (sample_base)"

/* ============================================================
   POOLED: stack all 3 waves + wave dummies + interactions
   ============================================================ */
use "$out/india_2014_analytic.dta", clear
append using "$out/india_2022_analytic.dta", force
append using "$out/india_2025_analytic.dta", force

/* Trend variable (years since 2014) */
gen trend = year_num - 2014
gen trend2 = trend^2

/* Cross-wave interactions */
gen FSTS_x_2022  = FSTS * wave_2022
gen FSTS_x_2025  = FSTS * wave_2025
gen FSTS2_x_2022 = FSTSsq * wave_2022
gen FSTS2_x_2025 = FSTSsq * wave_2025
gen TCI_x_2025   = TCI_full * wave_2025
gen DAI_x_2025   = DAI_core * wave_2025

save "$out/india_pooled_analytic.dta", replace
display _n "Pooled India 2014+2022+2025: " _N " firm-year obs"

forval y = 2014(8)2025 {
    count if year_num == `y'
    display "  " `y' " wave: " r(N) " firms"
}
count if year_num == 2022
display "  2022 wave: " r(N) " firms"

log close
exit

/* ============================================================
   P4 Singapore — 01_build_singapore.do
   Purpose: Build analytic dataset from WBES Singapore 2023
   Author: Đỗ Thị Thúy Hương
   Date: May 2026

   Input:  $data/Singapore_2023.dta  (WBES BREADY schema)
   Output: data/singapore_2023_analytic.dta
   ============================================================ */

version 17
clear all
set more off
set linesize 120

/* ---- Directory Setup ---------------------------------------- */
global data   "../../../data_wbes"
global out    "data"
cap mkdir "$out"

/* ============================================================
   WBES Singapore 2023 (BREADY schema)
   N_raw ≈ 500 private non-agricultural firms
   ============================================================ */
use "$data/Singapore_2023.dta", clear

/* -- Recode WBES nonresponse codes -- */
foreach v of varlist _all {
    capture confirm numeric variable `v'
    if _rc == 0 {
        replace `v' = . if `v' == -9 | `v' == -8 | `v' == -7 | `v' == -6
    }
}

/* -- Outcome: Labour Productivity -- */
gen lnLP = ln(d2 / b1_d) if b1_d > 0 & d2 > 0
label var lnLP "ln(Labour Productivity) — annual sales per worker"

/* -- Export intensity (FSTS) -- */
/* BREADY 2023 variable: d3b (% direct exports). Verify name vs. d3c in earlier waves. */
/* Non-exporters report d3b = 0; missing d3b (no response) stays missing. */
gen FSTS = d3b / 100 if !mi(d3b) & d3b >= 0
replace FSTS = . if FSTS > 1   // flag any invalid values > 100%
label var FSTS "Export intensity (Foreign Sales / Total Sales)"
gen FSTSsq = FSTS^2
label var FSTSsq "FSTS squared"

/* -- Technological Capability Index (TCI) -- */
// Items: ISO quality cert (b8), foreign technology license (e6)
// 2023 BREADY: also imported machinery (h8), additional ISO (h1)
gen tci_cert = (b8 == 1) if b8 != .
gen tci_tech = (e6 == 1) if e6 != .
capture gen tci_mach = (h8 == 1) if h8 != .
capture gen tci_iso2 = (h1 == 1) if h1 != .

quietly: capture confirm variable tci_mach tci_iso2
if (_rc == 0) {
    // z-standardize each component before averaging
    foreach item in tci_cert tci_tech tci_mach tci_iso2 {
        quietly summarize `item'
        if r(sd) > 0 gen `item'_z = (`item' - r(mean)) / r(sd)
        else         gen `item'_z = 0
    }
    egen TCI_raw = rowmean(tci_cert_z tci_tech_z tci_mach_z tci_iso2_z)
}
else {
    foreach item in tci_cert tci_tech {
        quietly summarize `item'
        if r(sd) > 0 gen `item'_z = (`item' - r(mean)) / r(sd)
        else         gen `item'_z = 0
    }
    egen TCI_raw = rowmean(tci_cert_z tci_tech_z)
}
// Re-standardize composite
quietly summarize TCI_raw
gen TCIfull = (TCI_raw - r(mean)) / r(sd) if r(sd) > 0
label var TCIfull "TCI — z-standardised composite"

/* -- Digital Adoption Index (DAI) — Tier 1 + Tier 2 for 2023 -- */
// Tier 1: website presence (c22b)
gen dai_web = (c22b == 1) if c22b != .
label var dai_web "DAI Tier-1 — website presence"

// Tier 2: e-payment acceptance (k33 or k38)
capture gen dai_pay = (k33 == 1 | k38 == 1) if (k33 != . | k38 != .)

capture confirm variable dai_pay
if (_rc == 0) {
    // z-standardize each tier before averaging
    quietly summarize dai_web
    local mw = r(mean)
    local sw = r(sd)
    quietly summarize dai_pay
    local mp = r(mean)
    local sp = r(sd)
    gen dai_web_z = (dai_web - `mw') / `sw' if `sw' > 0
    gen dai_pay_z = (dai_pay - `mp') / `sp' if `sp' > 0
    egen DAI_raw = rowmean(dai_web_z dai_pay_z)
    quietly summarize DAI_raw
    gen DAIfull = (DAI_raw - r(mean)) / r(sd) if r(sd) > 0
    label var DAIfull "DAI Tier-1+2 — z-standardised composite"
    gen DAItier2 = dai_pay
    label var DAItier2 "DAI Tier-2 — e-payment (k33/k38)"
}
else {
    quietly summarize dai_web
    gen DAIfull = (dai_web - r(mean)) / r(sd) if r(sd) > 0
    label var DAIfull "DAI Tier-1 only — z-standardised"
}
gen DAIthin = dai_web
label var DAIthin "DAI Tier-1 — website presence (thin measure)"

/* -- Controls -- */
gen lnEmp   = ln(b1_d) if b1_d > 0
gen firmage = b4       if b4 >= 0
gen foreigndummy = (b2b >= 10) if b2b != .
label var lnEmp        "ln(Number of employees)"
label var firmage      "Firm age (years)"
label var foreigndummy "Foreign ownership ≥10% dummy"

/* -- Sector Classification (WBES BREADY 2023 Singapore) --
   Manuscript §3.2.4: Manufacturing ~31%, Retail/Other services ~50%, Other ~19%
   BREADY 2023 a4a codes (verify against Singapore_2023.dta labels):
     1 = Manufacturing;  2 = Retail/Wholesale;  3+ = Services/Other
   Fallback: uses ISIC divisional codes if a4a uses ISIC scheme (a4a > 10) */
quietly summarize a4a if analytic
local a4a_max = r(max)

if `a4a_max' > 10 {
    /* ISIC-based sector coding */
    gen byte sec_mfg    = (a4a >= 10 & a4a <= 39) if !mi(a4a)
    gen byte sec_retail = (a4a >= 45 & a4a <= 56) if !mi(a4a)
}
else {
    /* BREADY 2023 numeric coding (1=Mfg, 2=Retail, 3+=Other) */
    gen byte sec_mfg    = (a4a == 1) if !mi(a4a)
    gen byte sec_retail = (a4a == 2 | a4a == 3) if !mi(a4a)
}
gen byte sec_other = (sec_mfg == 0 & sec_retail == 0) if (!mi(sec_mfg) & !mi(sec_retail))

label var sec_mfg    "Manufacturing sector (BREADY a4a)"
label var sec_retail "Retail/wholesale sector (BREADY a4a)"
label var sec_other  "Other services sector (reference omitted in regressions)"

/* Audit: sector shares should approximate 31% / 50% / 19% per §3.1 */
foreach s in mfg retail other {
    quietly count if sec_`s' == 1 & analytic
    di as txt "[AUDIT] sec_`s' firms = " r(N) " (" %5.1f r(N)/_N*100 "%)"
}

/* -- Sample Flags -- */
gen analytic   = (!missing(lnLP, FSTS, lnEmp))
gen base       = analytic & !missing(firmage, foreigndummy)
gen tci_samp   = base & !missing(TCIfull)
gen dai_samp   = base & !missing(DAIfull)
gen full_samp  = base & !missing(TCIfull, DAIfull)
gen exp_samp   = full_samp & FSTS > 0     // exporters-only subsample

gen wave = 2023
label var wave "Survey wave year"

/* -- Winsorize lnLP at 1/99 -- */
quietly summarize lnLP if analytic, detail
replace lnLP = r(p1)  if lnLP < r(p1)  & analytic
replace lnLP = r(p99) if lnLP > r(p99) & analytic

/* -- Audit: report each sample count before keep -- */
di "Singapore 2023 — Raw N = " _N
count if analytic;   local n_analytic = r(N)
count if base;       local n_base     = r(N)
count if full_samp;  local n_full     = r(N)
count if exp_samp;   local n_exp      = r(N)
di "Analytic N   = `n_analytic'"
di "Base N       = `n_base'"
di "Full-samp N  = `n_full'  (expect ~617 per manuscript)"
di "Exporters N  = `n_exp'   (expect ~84 per manuscript)"

keep if analytic
save "$out/singapore_2023_analytic.dta", replace
di "Saved: $out/singapore_2023_analytic.dta (N = `n_analytic')"

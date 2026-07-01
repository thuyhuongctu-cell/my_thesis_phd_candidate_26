*===============================================================*
* P3 (Vietnam) — 03_make_figures.do
* Regenerates Figure 2 (inverted-U by wave + pooled) and
* Figure 3 (TCI / DAI moderator marginals) directly in Stata
* from the built analytic data sets.
*
* Run AFTER:
*   01_build_vietnam.do   -> data/vietnam_2009_analytic.dta, _2015_, _2023_,
*                            data/vietnam_pooled.dta
*   (02_run_models.do is not required; this file re-estimates M2 / M8.)
*
* Output: figures/figure_2a..2d.png and figures/figure_3a/3b.png
* Requires: -utest- optional (not needed here); base Stata graphics only.
*===============================================================*
version 15
clear all
set more off

* ---- paths (edit $root if needed) --------------------------------
global root  "`c(pwd)'"
global data  "$root/data"
global fig   "$root/figures"
cap mkdir "$fig"

local controls lnEmp firmage foreigndummy

*==================================================================*
* FIGURE 2 — Predicted ln(LP) vs FSTS (quadratic M2), by wave
*==================================================================*
* program: estimate M2 on the current data and plot predicted curve
capture program drop _f2
program define _f2
    args yr panel
    quietly summarize FSTS if base
    local m = r(mean)
    capture drop FSTSc FSTSc2
    gen double FSTSc  = FSTS - `m'
    gen double FSTSc2 = FSTSc^2
    quietly reg lnLP FSTSc FSTSc2 `0' if base, vce(hc1)
    * turning point on the original FSTS scale (%)
    local tp = 100*(`m' - _b[FSTSc]/(2*_b[FSTSc2]))
    twoway (function y = _b[_cons] ///
              + _b[FSTSc]*(x/100 - `m') ///
              + _b[FSTSc2]*(x/100 - `m')^2, range(0 100) lwidth(medthick)), ///
        xtitle("FSTS (%)") ytitle("Predicted ln(labour productivity)") ///
        title("`panel'. Wave `yr'") ///
        xline(`tp', lpattern(dash) lcolor(gs8)) ///
        note("Turning point ~ " + string(`tp',"%4.1f") + "% FSTS") ///
        graphregion(color(white)) plotregion(color(white))
    graph export "$fig/figure_2`=lower("`panel'")'.png", replace width(1800)
end

local controls lnEmp firmage foreigndummy
use "$data/vietnam_2009_analytic.dta", clear
_f2 2009 A `controls'
use "$data/vietnam_2015_analytic.dta", clear
_f2 2015 B `controls'
use "$data/vietnam_2023_analytic.dta", clear
_f2 2023 C `controls'

* pooled (add wave dummies d15 d23 if present)
use "$data/vietnam_pooled.dta", clear
capture confirm variable d15
if _rc {
    quietly tab wave, gen(_wv)
    capture gen d15 = (wave==2015)
    capture gen d23 = (wave==2023)
}
_f2 Pooled D `controls' d15 d23

*==================================================================*
* FIGURE 3 — Moderator marginals (pooled M8): DAI_z and TCI_z
*==================================================================*
use "$data/vietnam_pooled.dta", clear
capture gen d15 = (wave==2015)
capture gen d23 = (wave==2023)
quietly summarize FSTS if base
local m = r(mean)
foreach v in FSTSc FSTSc2 TCI_z DAI_z {
    capture drop `v'
}
gen double FSTSc  = FSTS - `m'
gen double FSTSc2 = FSTSc^2
quietly summarize TCIfull if full_samp
gen double TCI_z = (TCIfull - r(mean))/r(sd)
quietly summarize DAIthin if full_samp
gen double DAI_z = (DAIthin - r(mean))/r(sd)
gen double FSTSc_TCIz  = FSTSc*TCI_z
gen double FSTSc2_TCIz = FSTSc2*TCI_z
gen double FSTSc_DAIz  = FSTSc*DAI_z
gen double FSTSc2_DAIz = FSTSc2*DAI_z

quietly reg lnLP FSTSc FSTSc2 TCI_z DAI_z ///
    FSTSc_TCIz FSTSc2_TCIz FSTSc_DAIz FSTSc2_DAIz ///
    lnEmp firmage foreigndummy d15 d23 if full_samp, vce(cluster idstd)

* quantiles of the moderators
quietly summarize DAI_z if full_samp, detail
local daiLo = r(p25)
local daiHi = r(p75)
quietly summarize TCI_z if full_samp, detail
local tciLo = r(p25)
local tciHi = r(p75)

* Panel 3a — DAI_z low vs high (TCI_z at mean = 0)
twoway ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[DAI_z]*`daiLo' + _b[FSTSc_DAIz]*(x/100-`m')*`daiLo' + _b[FSTSc2_DAIz]*(x/100-`m')^2*`daiLo', ///
    range(0 100) lpattern(dash)) ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[DAI_z]*`daiHi' + _b[FSTSc_DAIz]*(x/100-`m')*`daiHi' + _b[FSTSc2_DAIz]*(x/100-`m')^2*`daiHi', ///
    range(0 100) lwidth(medthick)), ///
 legend(order(1 "Low DAI_z (p25)" 2 "High DAI_z (p75)") rows(1)) ///
 xtitle("FSTS (%)") ytitle("Predicted ln(labour productivity)") ///
 title("3a. Website-presence (DAI_z) moderation") ///
 graphregion(color(white)) plotregion(color(white))
graph export "$fig/figure_3a.png", replace width(1800)

* Panel 3b — TCI_z low vs high (DAI_z at mean = 0)
twoway ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[TCI_z]*`tciLo' + _b[FSTSc_TCIz]*(x/100-`m')*`tciLo' + _b[FSTSc2_TCIz]*(x/100-`m')^2*`tciLo', ///
    range(0 100) lpattern(dash)) ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[TCI_z]*`tciHi' + _b[FSTSc_TCIz]*(x/100-`m')*`tciHi' + _b[FSTSc2_TCIz]*(x/100-`m')^2*`tciHi', ///
    range(0 100) lwidth(medthick)), ///
 legend(order(1 "Low TCI_z (p25)" 2 "High TCI_z (p75)") rows(1)) ///
 xtitle("FSTS (%)") ytitle("Predicted ln(labour productivity)") ///
 title("3b. Technological-capability (TCI_z) moderation") ///
 graphregion(color(white)) plotregion(color(white))
graph export "$fig/figure_3b.png", replace width(1800)

di as result "Figures 2a-2d and 3a-3b exported to $fig"
*=================== end of file ==================================*

*===============================================================*
* P5 (China) — 05_make_figures.do
* Regenerates the predicted inverted-U I–P curves by wave (M2)
* showing temporal threshold stability (~47–48% FSTS).
* Run AFTER 01_build_2012.do / 02_build_2024.do / 03_build_pooled.do.
* Output: figures/figure_3_predicted_curves.png
*===============================================================*
version 15
clear all
set more off
global root "`c(pwd)'"
global data "$root"
global fig  "$root/figures"
cap mkdir "$fig"
local controls lnEmp firmage foreign

capture program drop _tp
program define _tp
    args dta yr
    use "`dta'", clear
    quietly reg lnLP FSTS FSTSsq `0' if sample_base, vce(robust)
    local tp = 100*(-_b[FSTS]/(2*_b[FSTSsq]))
    twoway (function y = _b[FSTS]*(x/100) + _b[FSTSsq]*(x/100)^2, range(0 100) lwidth(medthick)), ///
        xtitle("FSTS (%)") ytitle("Relative predicted ln(LP)") ///
        title("China `yr' — inverted-U (TP ~ " + string(`tp',"%4.1f") + "%)") ///
        xline(`tp', lpattern(dash) lcolor(gs9)) ///
        graphregion(color(white)) plotregion(color(white)) name(g`yr', replace)
end

local controls lnEmp firmage foreign
_tp "china2012_analytic.dta" 2012 `controls'
_tp "china2024_analytic.dta" 2024 `controls'
graph combine g2012 g2024, cols(2) graphregion(color(white))
graph export "$fig/figure_3_predicted_curves.png", replace width(2200)
di as result "P5 figure exported to $fig"

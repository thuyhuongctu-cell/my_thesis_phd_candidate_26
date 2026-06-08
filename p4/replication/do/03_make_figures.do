*===============================================================*
* P4 (Singapore) — 03_make_figures.do
* Regenerates Figure 2 (DAI_z moderation of the I–P curve, M8/M3)
* and Figure 3 (predicted I–P curve, M2) directly in Stata.
*
* Run AFTER:
*   01_build_singapore.do  -> data/singapore_2023_analytic.dta
*   (re-creates centred/standardised terms; does not require 02.)
* Output: figures/figure_2_dai_marginal.png, figure_3_predicted_ip_curve.png
*===============================================================*
version 15
clear all
set more off
global root "`c(pwd)'"
global data "$root/data"
global fig  "$root/figures"
cap mkdir "$fig"

use "$data/singapore_2023_analytic.dta", clear

quietly summarize FSTS if base
local m = r(mean)
gen double FSTSc  = FSTS - `m'
gen double FSTSc2 = FSTSc^2
quietly summarize TCIfull if !mi(TCIfull)
gen double TCI_z = (TCIfull - r(mean))/r(sd)
quietly summarize DAIfull if !mi(DAIfull)
gen double DAI_z = (DAIfull - r(mean))/r(sd)
gen double FSTSc_DAIz  = FSTSc*DAI_z
gen double FSTSc2_DAIz = FSTSc2*DAI_z
local controls lnEmp firmage foreign

* ---- Figure 3: predicted I–P curve (M2) ----
quietly reg lnLP FSTSc FSTSc2 `controls' if base, vce(hc1)
local tp = 100*(`m' - _b[FSTSc]/(2*_b[FSTSc2]))
twoway (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2, ///
        range(0 100) lwidth(medthick)), ///
   xtitle("FSTS (%)") ytitle("Predicted ln(labour productivity)") ///
   title("Predicted internationalization–performance curve (Singapore, M2)") ///
   xline(`tp', lpattern(dash) lcolor(gs9)) ///
   note("Turning point ~ " + string(`tp',"%4.1f") + "% FSTS (sparse upper tail)") ///
   graphregion(color(white)) plotregion(color(white))
graph export "$fig/figure_3_predicted_ip_curve.png", replace width(1800)

* ---- Figure 2: DAI_z moderation (M8 with TCI_z + DAI interactions) ----
gen double FSTSc_TCIz  = FSTSc*TCI_z
gen double FSTSc2_TCIz = FSTSc2*TCI_z
quietly reg lnLP FSTSc FSTSc2 TCI_z DAI_z FSTSc_DAIz FSTSc2_DAIz `controls' if base, vce(hc1)
twoway ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[DAI_z]*(-1) + _b[FSTSc_DAIz]*(x/100-`m')*(-1) + _b[FSTSc2_DAIz]*(x/100-`m')^2*(-1), ///
    range(0 100) lpattern(dash)) ///
 (function y = _b[_cons] + _b[FSTSc]*(x/100-`m') + _b[FSTSc2]*(x/100-`m')^2 ///
    + _b[DAI_z]*(1) + _b[FSTSc_DAIz]*(x/100-`m')*(1) + _b[FSTSc2_DAIz]*(x/100-`m')^2*(1), ///
    range(0 100) lwidth(medthick)), ///
 legend(order(1 "Low DAI_z (-1 SD)" 2 "High DAI_z (+1 SD)") rows(1)) ///
 xtitle("FSTS (%)") ytitle("Predicted ln(labour productivity)") ///
 title("Digital-adoption (DAI_z) moderation of the I–P curve (Singapore)") ///
 graphregion(color(white)) plotregion(color(white))
graph export "$fig/figure_2_dai_marginal_effect.png", replace width(1800)

di as result "P4 figures exported to $fig"
*=================== end of file ==================================*

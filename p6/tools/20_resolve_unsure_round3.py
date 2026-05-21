#!/usr/bin/env python3
"""
Script 20: Third-pass title resolution for 204 still-UNSURE papers.

After inspecting all 204 titles, the residual UNSURE pool splits into:
  - Papers whose title clearly signals I→P performance relationship (Y)
  - Papers whose title clearly signals non-performance DV or pure antecedent (N)
  - Papers that are genuinely ambiguous (need abstract)

New patterns added in this pass:
  HARD_EXCL: innovation-as-DV, employment-as-DV, emissions/environmental DV,
             born-global theory, pricing strategies, strategy-of-intl, FDI antecedents
  INCL: survival, growth, OFDI→parent performance, LBE variants,
        acquisition performance, export-efficiency, trade-off language
"""

import csv, re, pathlib, unicodedata

BASE  = pathlib.Path(__file__).parent
RES   = BASE / "results"
TODAY = "20260518"

INPUT   = RES / f"unsure_still_round2_{TODAY}.csv"
OUT_Y   = RES / f"unsure_resolved_round3_Y_{TODAY}.csv"
OUT_N   = RES / f"unsure_resolved_round3_N_{TODAY}.csv"
OUT_UNK = RES / f"unsure_still_round3_{TODAY}.csv"
OUT_ALL = RES / f"unsure_round3_all_{TODAY}.csv"


# ─── TIER 1: HARD exclusions ──────────────────────────────────────────────────

HARD_EXCL = [
    # Innovation as explicit DV (internationalization → innovation, not → performance)
    (r"\binternation\w+.*to innovation\b",         "DV:intl_to_innov"),
    (r"\bfrom internationali\w+.*innovation\b",    "DV:from_intl_to_innov"),
    (r"\bexport.*interplay.*innov",                "DV:export_innov_interplay"),
    (r"\binnov.*interplay.*export",                "DV:innov_export_interplay"),
    (r"\binternationaliz.*innov.*intensit",        "DV:intl_innov_intensity"),
    (r"\binnov.*strategy.*internationali",         "strat:innov_strategy"),
    (r"\binternationaliz.*innovation.*strategy",   "strat:intl_innov_strategy"),
    (r"\binternationali\w+.*new product development", "DV:intl_NPD"),
    # Employment / labour as DV (not financial performance)
    (r"\bemployment generation\b",                 "DV:emp_gen"),
    (r"\bwage premi\w+\b",                         "DV:wage_prem"),
    (r"\bwage prem\b",                             "DV:wage_prem2"),
    (r"\bdemand for skills\b",                     "DV:skills_demand"),
    (r"\blabour share\b",                          "DV:labour_share"),
    (r"\blabor share\b",                           "DV:labor_share"),
    (r"\bemployee income share\b",                 "DV:income_share"),
    (r"\bdownstream offshoring\b",                 "DV:offshoring_emp"),
    (r"\bimpact on employment\b",                  "DV:emp_impact"),
    # Emissions / environmental as DV
    (r"\bco2 emission\b",                          "DV:co2_emission"),
    (r"\bco<sub>2</sub>\b",                        "DV:co2_sub"),
    (r"\bcarbon emission\b",                       "DV:carbon"),
    (r"\bgreenhouse\b",                            "DV:greenhouse"),
    (r"\beco.innovation\b",                        "DV:eco_innov"),
    # Pure strategies / process papers (not performance outcome)
    (r"\binternationali\w+ strateg",               "strat:intl_strategy"),
    (r"\bstrateg.*internationali",                 "strat:strategy_intl"),
    (r"\bpricing strateg",                         "strat:pricing"),
    (r"\bleadership in internationali",            "strat:leadership"),
    (r"\bborn.global.*theory\b",                   "theory:born_global"),
    (r"\bborn local.*theory\b",                    "theory:born_local"),
    (r"\bborn local.*toward a theory\b",           "theory:born_local2"),
    (r"\billusion.*born global\b",                 "theory:born_illusion"),
    (r"\bborn global illusion\b",                  "theory:born_illusion2"),
    (r"\bresource.based view.*review\b",           "theory:RBV_review"),
    (r"\busing the resource.based view\b",         "theory:RBV_using"),
    (r"\bentrepreneurial orientation.*process\b",  "theory:EO_process"),
    (r"\bfoundations.*internationaliz\b",          "theory:foundation"),
    # FDI antecedents (what causes FDI, not FDI→performance)
    (r"\brent.seeking.*outward fdi\b",             "ant:rent_OFDI"),
    (r"\borganizational goals.*overseas fdi\b",    "ant:goals_OFDI"),
    (r"\bforeign bank entry.*outward fdi\b",       "ant:bank_OFDI"),
    (r"\bdoes policy reform promote fdi\b",        "ant:policy_FDI"),
    # Macro/spillover (not firm-level I→P)
    (r"\bspillover effect.*fdi\b",                 "macro:spillover_FDI"),
    (r"\bspillover.*manufacturing export\b",       "macro:spillover_exp"),
    (r"\bfdi.*green growth.*industr",              "macro:fdi_green_industry"),
    (r"\bfdi.*trade.driven.*green growth\b",       "macro:fdi_trade_green"),
    # CSR / sustainability as DV
    (r"\binternationalization.*corporate sustainability\b", "DV:corp_sustain"),
    (r"\bsustainable development.*internationali",  "DV:SDG"),
    (r"\bproactive environmental.*level of internationali", "DV:env_intl_level"),
    (r"\benvironmental sustainability.*export\b",   "DV:env_sustain_exp"),
    (r"\benvironmental sustainability.*offshoring\b","DV:env_sustain_off"),
    # Entry/expansion as DV (not performance)
    (r"\bdigital platforms.*sme expansion\b",      "ant:platform_expansion"),
    (r"\bstart.up export\b",                       "ant:startup_export"),
    (r"\bearly foreign listing\b",                 "ant:foreign_listing"),
    (r"\bventure internationalization.*entry\b",   "ant:vc_entry"),
    # Absorptive capacity as outcome (not firm performance)
    (r"\babsorptive capacity from fdi\b",          "DV:abs_capacity"),
    (r"\bknowledge assets.*strategy\b",            "ant:knowledge_strategy"),
]

# ─── TIER 2: INCLUDE patterns ─────────────────────────────────────────────────

INTL_RE = re.compile(
    r"\b(internationaliz\w+|internationaliz|multinationalit|multinational\b|"
    r"globali[sz]\w+|globaliz\w+|export\b|outward fdi\b|ofdi\b|"
    r"cross.border acqui|foreign sales\b|foreign direct invest\w+|"
    r"degree of internation|overseas expan|"
    r"internationali[zs]ation.+performance)\b"
)

PERF_RE = re.compile(
    r"\b(financial performance|firm performance|business performance|"
    r"corporate performance|economic performance|operating performance|"
    r"export performance|mne performance|subsidiary performance|"
    r"profitabilit\w+|profitab\w+|return on assets|return on equity|"
    r"roa\b|roe\b|ros\b|tobin'?s? ?q\b|market value\b|firm value\b|"
    r"productivity\b|labour productivity|labor productivity|"
    r"total factor productivity|tfp\b|"
    r"sales growth|revenue growth|earnings quality|"
    r"financial result|economic result|value creation\b|"
    r"financial effect|economic effect|performance implication|"
    r"technical efficiency|efficiency\b|firm growth\b|"
    r"survival\b|growth\b|risk.return\b|corporate value\b)\b"
)

STRONG_INCL = [
    # Existing patterns
    (r"performance.*internationaliz",              "SI:perf_intl"),
    (r"internationaliz.*performance",              "SI:intl_perf"),
    (r"multinationalit.*performance",              "SI:multi_perf"),
    (r"performance.*multinationalit",              "SI:perf_multi"),
    (r"globali[sz].*financial performance",        "SI:glob_finperf"),
    (r"financial performance.*globali[sz]",        "SI:finperf_glob"),
    (r"export.*productivit",                       "SI:exp_prod"),
    (r"productivit.*export",                       "SI:prod_exp"),
    (r"learning.by.export",                        "SI:LBE"),
    (r"which.*firms.*learn.*export\b",             "SI:which_LBE"),
    (r"self.selection.*export",                    "SI:self_sel"),
    (r"cross.border acqui.*perform",               "SI:xb_acq_perf"),
    (r"perform.*cross.border acqui",               "SI:perf_xb_acq"),
    (r"post.acquisition perform",                  "SI:post_acq_perf"),
    (r"acquisition perform",                       "SI:acq_perf"),
    (r"\bmne\b.*perform",                          "SI:mne_perf"),
    (r"outward fdi.*productiv",                    "SI:ofdi_prod"),
    (r"outward fdi.*parent firm",                  "SI:ofdi_parent"),
    (r"ofdi.*impact.*parent\b",                    "SI:ofdi_parent2"),
    (r"impact.*outward fdi.*parent",               "SI:impact_ofdi_parent"),
    (r"fdi.*productiv",                            "SI:fdi_prod"),
    (r"export.*profit",                            "SI:exp_profit"),
    (r"profit.*export",                            "SI:profit_exp"),
    (r"internationali\w+.*firm value",             "SI:intl_fv"),
    (r"impact of.*internation.*on.*perform",       "SI:impact_intl_perf"),
    (r"effect of.*internation.*on.*perform",       "SI:effect_intl_perf"),
    (r"internation.*and.*perform",                 "SI:intl_and_perf"),
    (r"globali\w+.*perform",                       "SI:glob_perf"),
    (r"perform.*globali",                          "SI:perf_glob"),
    (r"export.*perform",                           "SI:exp_perf"),
    (r"perform.*export",                           "SI:perf_exp"),
    (r"fdi.*and.*firm perform",                    "SI:fdi_firmperf"),
    (r"firm.*productiv.*export",                   "SI:firm_prod_exp"),
    (r"manufacturing.*export.*productiv",          "SI:mfg_exp_prod"),
    (r"internationali\w+.*financial",              "SI:intl_financial"),
    (r"financial.*internationali",                 "SI:financial_intl"),
    (r"impact of.*export.*on.*perform",            "SI:imp_exp_perf"),
    (r"e.commerce.*perform",                       "SI:ecom_perf"),
    (r"perform.*outcome\b",                        "SI:perf_outcome"),
    (r"mne.*perform.*outcome\|perform.*outcome.*mne", "SI:mne_perf_outcome"),
    # New patterns — survival
    (r"\bfirm.*survival\b.*export",                "SI:firm_surv_exp"),
    (r"\bexport.*firm.*survival\b",                "SI:exp_firm_surv"),
    (r"\binternationaliz.*survival\b",             "SI:intl_surv"),
    (r"\bsurvival.*internationaliz\b",             "SI:surv_intl"),
    (r"\bsurvival analys.*internationaliz\b",      "SI:surv_anal_intl"),
    (r"\bimproving firm survival\b",               "SI:improving_surv"),
    (r"\bfailure risk\b.*export",                  "SI:fail_risk_exp"),
    (r"\bexport.*failure risk\b",                  "SI:exp_fail_risk"),
    # New patterns — growth
    (r"\bhow internationalization affects.*growth\b", "SI:intl_growth"),
    (r"\binternationaliz.*and.*growth\b",          "SI:intl_and_growth"),
    (r"\bgrowth.*internationaliz\b",               "SI:growth_intl"),
    (r"\binternationaliz.*growth.*new venture\b",  "SI:intl_growth_nv"),
    (r"\bgrowth.*new venture.*internation\b",      "SI:growth_nv_intl"),
    (r"\binternationali\w+.*growth\b",             "SI:intl_growth2"),
    (r"\bexport.growth relationship\b",            "SI:exp_growth_rel"),
    (r"\bexport.*economic.*growth\b",              "SI:exp_econ_growth"),
    (r"\bimproving.*export.*fdi\b",                "SI:improving_exp_fdi"),
    # New patterns — efficiency
    (r"\btechnical efficiency.*export\b",          "SI:tech_eff_exp"),
    (r"\bexport.*technical efficiency\b",          "SI:exp_tech_eff"),
    (r"\befficiency.*export\b",                    "SI:eff_exp"),
    (r"\bexport.*efficiency\b",                    "SI:exp_eff"),
    # New patterns — M&A performance
    (r"\bpost.acquisition.*cross.border\b",        "SI:post_acq_xb"),
    (r"\bcross.border.*acqui.*financial\b",        "SI:xb_acq_fin"),
    (r"\bacquirer.*perform\b",                     "SI:acquirer_perf"),
    (r"\bshareholder wealth.*cross.border\b",      "SI:shareholder_xb"),
    (r"\bgains from.*cross.border.*acqui\b",       "SI:gains_xb_acq"),
    # New patterns — risk-return / corporate value
    (r"\brisk.return.*multinational\b",            "SI:risk_return_multi"),
    (r"\bmultinational.*risk.return\b",            "SI:multi_risk_return"),
    (r"\bdiversification.*risk.return\b",          "SI:div_risk_return"),
    (r"\bforeign sales.*corporate value\b",        "SI:fsales_corp_val"),
    (r"\bcorporate value.*foreign sales\b",        "SI:corp_val_fsales"),
    (r"\boptimal multinationalit\b",               "SI:optimal_multi"),
    (r"\bmisfits.*multinationalit\b",              "SI:misfits_multi"),
    # New patterns — FDI productivity
    (r"\bproductivit.*multinational\b",            "SI:prod_multi"),
    (r"\bmultinational.*productivit\b",            "SI:multi_prod"),
    (r"\bfdi.*productivit\b",                      "SI:fdi_prod2"),
    (r"\bproductivit.*fdi\b",                      "SI:prod_fdi"),
    (r"\bproductivity gap.*fdi\b",                 "SI:prod_gap_fdi"),
    (r"\bfdi.*productivity gap\b",                 "SI:fdi_prod_gap"),
    (r"\brole of fdi.*productiv\b",                "SI:role_fdi_prod"),
    # New patterns — in search of (performance)
    (r"\bin search of.*cross.border.*productiv\b", "SI:search_xb_prod"),
    (r"\bcross.border knowledge.*domestic productiv\b", "SI:xb_know_prod"),
    # New patterns — blessing/curse
    (r"\bblessing or curse\b",                     "SI:blessing_curse"),
    # New patterns — FDI in R&D on performance
    (r"\bimpact of.*fdi.*r.d.*on.*firm\b",         "SI:fdi_rd_firm"),
    (r"\bfdi.*research.*development.*firm\b",      "SI:fdi_rd_firm2"),
    # New patterns — internationalizing business group + performance
    (r"\binternationaliz.*business group.*perform\b", "SI:intl_bg_perf"),
    (r"\bbusiness group.*perform.*internationaliz\b", "SI:bg_perf_intl"),
    (r"\bdo internationaliz.*affiliates perform\b", "SI:affiliates_perf"),
    (r"\bdo internationaliz.*better\b",            "SI:intl_better"),
    # New patterns — pro-market reform + performance
    (r"\bpro.market reform.*multinational\b",      "SI:promarket_multi"),
    (r"\bpro.market reform.*performance\b",        "SI:promarket_perf"),
    (r"\bpromarket.*perform\b",                    "SI:promarket_perf2"),
    # New patterns — export and economic performance / competitiveness
    (r"\bcompetitiveness.*export.*Africa\b",       "SI:comp_exp_africa"),
    (r"\binternational competitiveness.*sme.*cross\b", "SI:intl_comp_sme"),
    # New patterns — adverse shocks + M&A performance
    (r"\bpolitical shock.*cross.border.*financial\b", "SI:shock_xb_fin"),
    (r"\bcross.border.*acquisition.*financial perform\b", "SI:xb_acq_finperf"),
    (r"\badverse.*shock.*mergers.*acquisition.*financial\b", "SI:shock_ma_fin"),
    # FDI impact on firm-level performance
    (r"\bis the effect.*large.*firm.level.*fdi\b", "SI:fdi_effect_firm"),
    (r"\bfirm.level evidence.*fdi.*transition\b",  "SI:fdi_firm_trans"),
    # General "affect firms' growth" pattern
    (r"\baffect.*firms.*growth\b",                 "SI:affect_firm_growth"),
    (r"\bfirms.*growth.*quantile\b",               "SI:firms_growth_quant"),
    # New: EMPLOYEE productivity in cross-border acquisitions
    (r"\bemployee productivit.*cross.border\b",    "SI:emp_prod_xb"),
    (r"\bproductivit.*cross.border acqui\b",       "SI:prod_xb_acq"),
]

# ─── TIER 3: SOFT exclusions ──────────────────────────────────────────────────

SOFT_EXCL = [
    (r"\bcorporate social responsibility\b",       "csr:CSR"),
    (r"\besg rating\b",                            "csr:ESG"),
    (r"\bgreen internationali",                    "csr:green_intl"),
    (r"\bgreen technology\b",                      "csr:green_tech"),
    (r"\bborn global.*characteristic\b",           "theory:BG_char"),
    (r"\bborn global.*insight\b",                  "theory:BG_insight"),
    (r"\bborn global.*closer look\b",              "theory:BG_look"),
    (r"\bcapabilit.*develop\b",                    "ant:cap_develop"),
    (r"\bstrategic agility.*internationali\b",     "ant:agility"),
    (r"\borganizational learning.*internationali\b", "ant:org_learn"),
    (r"\bsme.*entry.*foreign markets\b",           "ant:sme_entry"),
    (r"\bfirm.*location.*strateg\b",               "ant:location_strat"),
    (r"\binternationalization.*failure risk\b",    "ant:intl_fail"),
]


def classify_title(title: str) -> tuple[str, str]:
    tl = title.lower()

    for pat, reason in HARD_EXCL:
        if re.search(pat, tl):
            return "N", f"HARD:{reason}"

    for pat, reason in STRONG_INCL:
        if re.search(pat, tl):
            return "Y", reason

    if INTL_RE.search(tl) and PERF_RE.search(tl):
        return "Y", "COMP:intl+perf"

    for pat, reason in SOFT_EXCL:
        if re.search(pat, tl):
            return "N", f"SOFT:{reason}"

    return "UNSURE", "still_ambiguous"


def main():
    with open(INPUT, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys()) + ["round3_decision", "round3_reason"]

    y_rows, n_rows, unk_rows, all_rows = [], [], [], []

    for r in rows:
        dec, reason = classify_title(r["title"])
        r2 = dict(r, round3_decision=dec, round3_reason=reason)
        all_rows.append(r2)
        if dec == "Y":   y_rows.append(r2)
        elif dec == "N": n_rows.append(r2)
        else:            unk_rows.append(r2)

    def write_csv(path, data):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=fieldnames)
            w.writeheader()
            w.writerows(data)
        print(f"  Wrote {len(data):3d} rows → {path.name}")

    write_csv(OUT_Y,   y_rows)
    write_csv(OUT_N,   n_rows)
    write_csv(OUT_UNK, unk_rows)
    write_csv(OUT_ALL, all_rows)

    print(f"\nRound-3 resolution of {len(rows)} still-UNSURE papers:")
    print(f"  Y  (newly confirmed):   {len(y_rows):3d}")
    print(f"  N  (newly excluded):    {len(n_rows):3d}")
    print(f"  UNSURE (still pending): {len(unk_rows):3d}")

    print("\nTop Y reasons:")
    yr = {}
    for r in y_rows: yr[r['round3_reason']] = yr.get(r['round3_reason'],0) + 1
    for k, v in sorted(yr.items(), key=lambda x: -x[1])[:12]:
        print(f"  {v:3d}  {k}")

    print("\nTop N reasons:")
    nr = {}
    for r in n_rows: nr[r['round3_reason']] = nr.get(r['round3_reason'],0) + 1
    for k, v in sorted(nr.items(), key=lambda x: -x[1])[:15]:
        print(f"  {v:3d}  {k}")

    if unk_rows:
        print(f"\nFirst 10 remaining UNSURE titles:")
        for r in unk_rows[:10]:
            print(f"  [{r['year']}] {r['title'][:85]}")

if __name__ == "__main__":
    main()

#!/usr/bin/env python3
"""
Script 22: Fourth-pass title resolution for 136 still-UNSURE papers.

After inspecting all 136 titles, the residual pool contains:
  - Capital structure papers (intl as context, not performance DV)
  - Antecedent/determinant studies (what drives exports/FDI)
  - Innovation-as-DV papers not caught by R3 patterns
  - Location strategy / alliance portfolio papers
  - Papers with explicit "performance consequences" language → Y

New patterns added in this pass:
  HARD_EXCL:
    - Capital structure topic
    - Export antecedent language (cost competitiveness, driving force, motivators)
    - Eco-innovation / CDM / sustainability as DV (residual cases)
    - Location strategy MNE decisions
    - Network embeddedness → intl (antecedent direction)
    - Strategy diffusion papers
    - Quality management → globalization
    - Financial constraints → export entry decisions
    - Corporate social performance / CSP as DV
    - Servicification structural analysis
  STRONG_INCL:
    - "performance consequences" explicit in title
    - Optimal multinationality → subsequent market outcomes
    - OFDI investing-abroad → home transformation
    - Over-internationalization → reduction (I→P at upper bound)
    - From domestic to exporter (pre-post performance)
    - Crisis resilience + internationalization
    - Performance outcomes (fix plural form)
"""

import csv, re, pathlib

BASE  = pathlib.Path(__file__).parent
RES   = BASE / "results"
TODAY = "20260518"

INPUT   = RES / f"unsure_still_round3_{TODAY}.csv"
OUT_Y   = RES / f"unsure_resolved_round4_Y_{TODAY}.csv"
OUT_N   = RES / f"unsure_resolved_round4_N_{TODAY}.csv"
OUT_UNK = RES / f"unsure_still_round4_{TODAY}.csv"
OUT_ALL = RES / f"unsure_round4_all_{TODAY}.csv"


# ─── TIER 1: HARD exclusions (unambiguously NOT I→P performance) ─────────────

HARD_EXCL = [
    # Capital structure as topic (not performance DV)
    (r"\bcapital structure\b",                          "HARD:fin:capital_structure"),
    # Antecedent: what drives exports/FDI (export/FDI as DV, not performance DV)
    (r"cost competitiveness.*(?:export|driving force)",  "HARD:ant:cost_comp_export"),
    (r"driving force.*export",                           "HARD:ant:driving_force_exp"),
    (r"motivators.*(?:export|sme.*export)",              "HARD:ant:motivators_export"),
    (r"\binitial export choice\b",                       "HARD:ant:initial_exp_choice"),
    (r"financial constraint.*export.*firm",              "HARD:ant:fin_constraint_exp"),
    (r"financial constraint.*internation",               "HARD:ant:fin_constraint_intl"),
    (r"credit constraint.*(?:entry|internation)",        "HARD:ant:credit_constraint"),
    (r"determinants.*domestic value added",              "HARD:ant:dva_determinants"),
    (r"domestic value added.*export",                    "HARD:ant:dva_export"),
    (r"\bfirm heterogen\w+.*export activit",             "HARD:ant:firm_het_exp_act"),
    (r"presence of foreign capital.*internation",        "HARD:ant:for_cap_intl"),
    (r"how does manufacturing.*export",                  "HARD:ant:mfg_output_export"),
    # Innovation / R&D as DV (not caught by R3)
    (r"\br&d.*domestic.*entrepreneur",                   "HARD:DV:rd_entrepreneur"),
    (r"foreign multinationals.*domestic innovation",     "HARD:DV:for_mn_dom_innov"),
    (r"absorptive capacity from fdi",                    "HARD:DV:absorptive_fdi"),
    (r"r&d.*intensit.*overseas subsid",                  "HARD:DV:rd_subsidiary"),
    (r"drivers.*impacts.*globalization.*r&d",            "HARD:DV:rd_globalization"),
    # Environmental / sustainability (residual)
    (r"\beco.innovation\b",                              "HARD:DV:eco_innov"),
    (r"participation.*cdm\b",                            "HARD:DV:cdm_participation"),
    (r"\bco<sub>2</sub>.*export",                        "HARD:DV:co2_export"),
    (r"environmental sustainability.*export",            "HARD:DV:env_sust_export"),
    (r"corporate social performance.*multinational",     "HARD:DV:csp_mnc"),
    # Location strategy (not performance)
    (r"\blocation strateg",                              "HARD:strat:location"),
    (r"global cities.*multinational.*location",          "HARD:strat:global_cities"),
    (r"institutional influence.*location",               "HARD:strat:inst_location"),
    # Alliance / network (antecedent direction)
    (r"network embeddedness.*(?:new.venture|internation)", "HARD:ant:network_intl"),
    (r"alliance portfolio.*(?:development|driver)",       "HARD:ant:alliance_dev"),
    (r"network analysis.*(?:strategies|fdi)",             "HARD:ant:network_strat"),
    # Strategy diffusion / methodology
    (r"modeling.*diffusion.*strateg.*export",            "HARD:method:diffusion"),
    (r"quality management.*(?:globali|internation)",     "HARD:ant:quality_globali"),
    # Servicification / structural
    (r"servicification.*(?:export|manufactur)",          "HARD:macro:servicification"),
    # Information acquisition (antecedent/process)
    (r"information acquisition.*(?:export|global start)",  "HARD:ant:info_acquisition"),
    # R&D organization / knowledge (not performance-focused)
    (r"\borganization of knowledge.*multinational",      "HARD:strat:knowledge_org"),
    # Ownership transitions where intl is DV
    (r"(?:family to non.family|non.family.*controlled).*internation", "HARD:ant:ownership_intl"),
    # Political / institutional action (not performance)
    (r"(?:vanguards|political action).*(?:pro.trade|globali)", "HARD:DV:political_action"),
    # University-industry cross-border collaboration
    (r"university.industry.*collabor.*(?:cross.border|iberian)", "HARD:DV:uni_ind_collab"),
    # Technological diversification → innovation DV
    (r"technological diversification.*r&d.*internation.*innov", "HARD:DV:td_rd_innov"),
    # Global start-up / born-global with no performance DV
    (r"global start.up.*export.*compan",                 "HARD:ant:global_startup_exp"),
    # Employer-employee perspectives on turnover (HR DV)
    (r"employer.employee.*turnover",                     "HARD:DV:turnover"),
    # Corporate diversification with globalization
    (r"corporate diversification.*impact.*(?:foreign competition|industry globali)", "HARD:ant:corp_div_glob"),
]

# ─── TIER 2: STRONG inclusions (clearly I→P performance relationship) ────────

STRONG_INCL = [
    # Explicit "performance consequences" in title
    (r"performance consequences",                         "SI:perf_consequences"),
    # Optimal DOI / misfits → subsequent market/performance outcomes
    (r"(?:deviations|misfits).*optimal.*multinational",   "SI:optimal_doi_deviations"),
    (r"optimal multinational.*subsequent",                 "SI:optimal_doi_subseq"),
    # Over-internationalization → reduction (studying upper bound of I→P)
    (r"over.internationaliz.*reduc",                       "SI:over_intl_reduce"),
    (r"reduc.*international.*footprint",                   "SI:intl_footprint_reduce"),
    # OFDI investing abroad → home country transformation/performance
    (r"investing abroad.*transforming at home",            "SI:ofdi_home_transform"),
    (r"transforming at home.*(?:outward|foreign direct)",  "SI:ofdi_home_transform2"),
    # Pre-post exporter comparison
    (r"from domestic to exporter.*what happens",           "SI:dom_to_exp"),
    (r"what happens.*(?:domestic.*exporter|exporter.*manufacturing)", "SI:exp_entry_effect"),
    # Crisis resilience + internationalization
    (r"internationalization.*resilience.*(?:crisis|covid)", "SI:intl_resilience_crisis"),
    (r"resilience.*(?:crisis|covid).*internationali",      "SI:crisis_resilience_intl"),
    # MNC strategy + performance outcomes (plural fix)
    (r"mnc.*strateg.*perform.*outcomes?",                  "SI:mnc_strategy_perf"),
    (r"perform.*outcomes?.*(?:mnc|multinational|exogenous shock)", "SI:perf_outcomes_mnc"),
    # SME survival + FDI
    (r"survival.*(?:fdi|korean sme|sme.*fdi)",             "SI:sme_fdi_survival"),
    # Unlisted firms acquired by MNCs → post-acquisition performance
    (r"performance.*unlisted.*(?:multinational|acquired)",  "SI:unlisted_acq_perf"),
    # Analyst earnings forecast as performance proxy
    (r"corporate internation.*analyst.*forecast",           "SI:analyst_forecast"),
    (r"analyst.*forecast.*corporate internation",           "SI:analyst_forecast2"),
    # Foreign exchange risk + performance
    (r"internationaliz.*foreign exchange.*(?:firm|perform)", "SI:fx_exposure_perf"),
    # Speed of FDI + performance outcomes
    (r"speed.*fdi.*(?:survival|performance|sme)",           "SI:fdi_speed_perf"),
    # Knowledge assets growth in multinationals
    (r"multilocalisation.*growth.*knowledge.*medium",       "SI:multiloc_knowledge"),
    # Export leaning + performance
    (r"learn.*export.*manufactur.*evidence",                "SI:learn_export_mfg"),
]

# ─── TIER 3: SOFT exclusions (applied only if NO strong INCL match) ──────────

SOFT_EXCL = [
    (r"\bcorporate social responsibilit",                  "SOFT:csr"),
    (r"\besg\b",                                           "SOFT:esg"),
    (r"\bboard.*internation|internation.*board\b",         "SOFT:board"),
    (r"\bcountry.level\b|\bnational.level\b",              "SOFT:country_level"),
    (r"\bsustainability\b",                                "SOFT:sustainability"),
    (r"\binnovation\b.*\boutcome\b|\boutcome.*innovation\b", "SOFT:innov_outcome"),
]

# ─── Composite INTL + PERF signal ─────────────────────────────────────────────

INTL_PAT = [
    r"\bexport\b", r"\bfdi\b", r"\binternational", r"\bmultinational",
    r"\bofdi\b", r"\bforeign sales\b", r"\bfsts\b", r"\bdoi\b",
    r"\bforeign direct invest", r"\boutward invest",
]
PERF_PAT = [
    r"\bperform", r"\bproductiv", r"\bprofitab", r"\befficienc",
    r"\broa\b", r"\broe\b", r"\btobin", r"\bsales growth",
    r"\bfirm value\b", r"\bmarket value\b", r"\bcompetitiv",
    r"\bgrowth\b", r"\bsurviv", r"\bwelfare\b", r"\boutcome\b",
]


def classify_title(title: str) -> tuple[str, str]:
    tl = title.lower()

    # Tier 1: HARD exclusion
    for pat, reason in HARD_EXCL:
        if re.search(pat, tl):
            return "N", reason

    # Tier 2: Strong inclusion signals
    for pat, reason in STRONG_INCL:
        if re.search(pat, tl):
            return "Y", reason

    # Tier 2b: Composite INTL × PERF
    has_intl = any(re.search(p, tl) for p in INTL_PAT)
    has_perf = any(re.search(p, tl) for p in PERF_PAT)
    if has_intl and has_perf:
        # Check soft exclusions first
        for pat, reason in SOFT_EXCL:
            if re.search(pat, tl):
                return "UNSURE", f"SOFT:{reason}"
        return "Y", "composite_intl_perf"

    # Tier 3: Soft exclusion (only if no INCL match)
    for pat, reason in SOFT_EXCL:
        if re.search(pat, tl):
            return "N", f"SOFT:{reason}_no_incl"

    return "UNSURE", "insufficient_title_signal"


# ─── Process ──────────────────────────────────────────────────────────────────

with open(INPUT, newline="", encoding="utf-8") as f:
    rows = list(csv.DictReader(f))

fieldnames = list(rows[0].keys()) + ["round4_decision", "round4_reason"]

y_rows, n_rows, unk_rows, all_rows = [], [], [], []

for r in rows:
    decision, reason = classify_title(r.get("title", ""))
    r["round4_decision"] = decision
    r["round4_reason"]   = reason
    all_rows.append(r)
    if decision == "Y":
        y_rows.append(r)
    elif decision == "N":
        n_rows.append(r)
    else:
        unk_rows.append(r)

def write_csv(path, data):
    with open(path, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(data)

write_csv(OUT_Y,   y_rows)
write_csv(OUT_N,   n_rows)
write_csv(OUT_UNK, unk_rows)
write_csv(OUT_ALL, all_rows)

print(f"  Wrote {len(y_rows):3d} rows → {OUT_Y.name}")
print(f"  Wrote {len(n_rows):3d} rows → {OUT_N.name}")
print(f"  Wrote {len(unk_rows):3d} rows → {OUT_UNK.name}")
print(f"  Wrote {len(all_rows):3d} rows → {OUT_ALL.name}")

print(f"\nRound-4 resolution of {len(rows)} still-UNSURE papers:")
print(f"  Y  (newly confirmed):    {len(y_rows)}")
print(f"  N  (newly excluded):     {len(n_rows)}")
print(f"  UNSURE (still pending): {len(unk_rows)}")

from collections import Counter
y_reasons = Counter(r["round4_reason"] for r in y_rows)
n_reasons = Counter(r["round4_reason"] for r in n_rows)

print("\nTop Y reasons:")
for reason, cnt in y_reasons.most_common(12):
    print(f"  {cnt:3d}  {reason}")

print("\nTop N reasons:")
for reason, cnt in n_reasons.most_common(15):
    print(f"  {cnt:3d}  {reason}")

print("\nFirst 10 remaining UNSURE titles:")
for r in unk_rows[:10]:
    print(f"  [{r['year']}] {r['title'][:90]}")

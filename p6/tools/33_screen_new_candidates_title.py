#!/usr/bin/env python3
"""
33_screen_new_candidates_title.py

Title-only L1/L2 pre-screening for the 2,032 new candidates added to
tracker v3 (rows 436–2467).  Applies ALL accumulated HARD_EXCL and
STRONG_INCL patterns from screening rounds 1-8 (scripts 14, 18, 20, 22)
plus the INTL_RE × PERF_RE dual-signal heuristic.

Decision logic (priority order):
  1. HARD_EXCL match → N  (definitely not I→P performance paper)
  2. STRONG_INCL match → Y (clearly I→P performance paper)
  3. INTL_RE + PERF_RE both match → Y
  4. Otherwise → UNSURE (needs abstract / full-text)

Outputs:
  results/new_candidates_screened_YYYYMMDD.csv   — all 2032 rows with decision
  results/screen_new_summary_YYYYMMDD.txt        — stats

Usage:
  python3 p6/tools/33_screen_new_candidates_title.py
"""

import csv, re
from collections import Counter
from datetime import date
from pathlib import Path

BASE   = Path("/home/user/PAPERS_IN_PHD_2026")
INDIR  = BASE / "p6/tools/results"
TODAY  = date.today().strftime("%Y%m%d")

TRACKER_V3 = INDIR / "fulltext_to_extraction_tracker_v3.csv"
OUT_CSV    = INDIR / f"new_candidates_screened_{TODAY}.csv"
OUT_TXT    = INDIR / f"screen_new_summary_{TODAY}.txt"

# ─── HARD EXCLUSION patterns (unambiguously NOT I→P performance) ─────────────
# Compiled from all 8 previous screening rounds.

HARD_EXCL_RAW = [
    # ── Governance / board structure ──
    (r"\bboard composition\b",                    "gov:board_composition"),
    (r"\bboard structure\b",                      "gov:board_structure"),
    (r"\bcorporate governance\b",                 "gov:corp_gov"),
    (r"\bgender diversity\b.*\bboard\b",          "gov:gender_board"),
    # ── Pure antecedents of internationalization (I as DV) ──
    (r"\bentry mode\b",                           "ant:entry_mode"),
    (r"\blocation choice\b",                      "ant:location_choice"),
    (r"\binternationalization speed\b",           "ant:intl_speed"),
    (r"\binternationa\w* decision\b",             "ant:intl_decision"),
    (r"\bdrivers of.*internation",                "ant:drivers_intl"),
    (r"\bdeterminants of.*(?:internation|export|fdi)",  "ant:determinants"),
    (r"\bpropensity to export\b",                 "ant:propensity_exp"),
    (r"\bexport initiat\w+\b",                    "ant:export_init"),
    (r"\bhow.*digital.*facilitat.*internation",   "ant:dig_facilitates"),
    (r"\bdigital transformat\w+.*facilitat.*internation", "ant:digtr_intl"),
    (r"\binstitutional void\b",                   "ant:inst_void"),
    (r"\binstitutional distance\b",               "ant:inst_dist"),
    (r"cost competitiveness.*(?:export|driving force)", "ant:cost_comp"),
    (r"driving force.*export",                    "ant:driving_force_exp"),
    (r"motivators.*(?:export|sme.*export)",       "ant:motivators_export"),
    (r"\binitial export choice\b",                "ant:initial_exp_choice"),
    (r"financial constraint.*export.*firm",       "ant:fin_constraint_exp"),
    (r"financial constraint.*internation",        "ant:fin_constraint_intl"),
    (r"credit constraint.*(?:entry|internation)", "ant:credit_constraint"),
    (r"determinants.*domestic value added",       "ant:dva_determinants"),
    (r"domestic value added.*export",             "ant:dva_export"),
    (r"\bfirm heterogen\w+.*export activit",      "ant:firm_het_exp_act"),
    (r"presence of foreign capital.*internation", "ant:for_cap_intl"),
    (r"how does manufacturing.*export",           "ant:mfg_output_export"),
    (r"network embeddedness.*(?:new.venture|internation)", "ant:network_intl"),
    (r"alliance portfolio.*(?:development|driver)","ant:alliance_dev"),
    (r"network analysis.*(?:strategies|fdi)",     "ant:network_strat"),
    (r"information acquisition.*(?:export|global start)", "ant:info_acquisition"),
    (r"(?:family to non.family|non.family.*controlled).*internation", "ant:ownership_intl"),
    (r"(?:vanguards|political action).*(?:pro.trade|globali)", "ant:political_action"),
    (r"corporate political activit\w+.*internation", "ant:CPA_intl"),
    (r"leadership orientation.*export",           "ant:leadership_orient"),
    (r"quality management.*(?:globali|internation)", "ant:quality_globali"),
    # ── Process / strategy (not performance outcome) ──
    (r"\bstrategic change\b",                     "proc:strategic_change"),
    (r"\binternationalization process\b",         "proc:intl_process"),
    (r"\btemporal misalignment",                  "proc:temporal"),
    (r"\bglobal value chain\b",                   "proc:GVC"),
    (r"\bsupply chain\b",                         "proc:supply_chain"),
    (r"\bknowledge transfer\b",                   "proc:knowledge_transfer"),
    (r"\bknowledge spillover\b",                  "proc:spillover"),
    (r"\blocation strateg",                       "strat:location_strat"),
    (r"global cities.*multinational.*location",   "strat:global_cities"),
    (r"institutional influence.*location",        "strat:inst_location"),
    (r"modeling.*diffusion.*strateg.*export",     "meth:diffusion"),
    (r"servicification.*(?:export|manufactur)",   "macro:servicification"),
    (r"\boffshoring\b.*\bbackshoring\b",          "strat:offshoring"),
    (r"\borganization of knowledge.*multinational", "strat:knowledge_org"),
    # ── Innovation / R&D as DV (not performance DV) ──
    (r"\br&d.*domestic.*entrepreneur",            "DV:rd_entrepreneur"),
    (r"foreign multinationals.*domestic innovation", "DV:for_mn_dom_innov"),
    (r"absorptive capacity from fdi",             "DV:absorptive_fdi"),
    (r"r&d.*intensit.*overseas subsid",           "DV:rd_subsidiary"),
    (r"drivers.*impacts.*globalization.*r&d",     "DV:rd_globalization"),
    (r"\beco.innovation\b",                       "DV:eco_innov"),
    (r"participation.*cdm\b",                     "DV:cdm_participation"),
    (r"environmental sustainability.*export",     "DV:env_sust_export"),
    (r"corporate social performance.*multinational", "DV:csp_mnc"),
    (r"technological diversification.*r&d.*internation.*innov", "DV:td_rd_innov"),
    # ── Financial structure (not performance DV) ──
    (r"\bcapital structure\b",                    "fin:capital_structure"),
    (r"\btrade credit\b",                         "fin:trade_credit"),
    # ── Behavioral / psychological (not performance) ──
    (r"\baffect.enacted\b",                       "beh:affect"),
    (r"\bceo narcissism\b",                       "beh:narcissism"),
    (r"\btmt faultlines\b",                       "beh:faultlines"),
    # ── Theory / method papers (not empirical I→P) ──
    (r"\bbibliometric\b",                         "meth:bibliometric"),
    (r"\bsystematic review\b",                    "meth:sys_review"),
    (r"\bliterature review\b",                    "meth:lit_review"),
    (r"\bconceptual framework\b",                 "meth:conceptual"),
    (r"\bpenrose'?s? theory\b",                   "theory:penrose"),
    (r"\bborn global theory\b",                   "theory:born_global"),
    (r"\buppsala model\b",                        "theory:uppsala"),
    # ── M&A / alliance formation strategy (not performance) ──
    (r"\bjoint venture formation\b",              "strat:jv_form"),
    (r"\bacquisition strategy\b",                 "strat:acq_strat"),
    # ── Macro / country level (not firm level) ──
    (r"\bpublic funding\b",                       "macro:pub_fund"),
    (r"\beconomic growth of\b",                   "macro:econ_growth"),
    (r"country.level\s+analysis",                 "macro:country_analysis"),
    (r"national.level",                           "macro:national_level"),
    (r"cross.country.*(?:comparison|analysis)",   "macro:cross_country"),
    # ── Qualitative / review ──
    (r"case study|case-study",                    "qual:case_study"),
    (r"grounded theory",                          "qual:grounded"),
    (r"content analysis",                         "qual:content_analysis"),
    # ── Health / medical / education ──
    (r"health|hospital|medical|patient|clinical|nursing|pharmaceutical", "oob:health"),
    (r"consumer behav|purchase intent|buyer behav|buying behav", "oob:consumer"),
    (r"language learn|education\s+system|academic\s+performance", "oob:education"),
    (r"sports?\s+performance|athlete|tournament", "oob:sports"),
    # ── Born-global / EO-as-DV (from R5) ──
    (r"born.global.*develop\w+",                  "ant:born_global_dev"),
    (r"entrepreneurial orientat.*internation",    "ant:eo_intl"),
    (r"determinants.*born.global",                "ant:det_born_global"),
    # ── Export as DV explicitly ──
    (r"export(?:ing)? participation",             "ant:export_participation"),
    (r"export(?:ing)? decision",                  "ant:export_decision"),
    (r"going.*international.*decision",           "ant:going_intl_dec"),
    # ── University-industry ──
    (r"university.industry.*collabor.*(?:cross.border|iberian)", "DV:uni_ind_collab"),
    # ── HR as DV ──
    (r"employer.employee.*turnover",              "DV:turnover"),
]

HARD_EXCL = [(re.compile(p, re.IGNORECASE), tag) for p, tag in HARD_EXCL_RAW]

# ─── STRONG INCLUSION patterns (clearly I→P performance) ─────────────────────

STRONG_INCL_RAW = [
    # Direct performance-internationalization linkage
    (r"performance.*internationaliz",             "SI:perf_intl"),
    (r"internationaliz.*performance",             "SI:intl_perf"),
    (r"multinationalit.*performance",             "SI:multi_perf"),
    (r"performance.*multinationalit",             "SI:perf_multi"),
    (r"globali[sz].*financial performance",       "SI:glob_finperf"),
    (r"financial performance.*globali[sz]",       "SI:finperf_glob"),
    (r"performance.*globali[sz]",                 "SI:perf_glob"),
    (r"globali[sz].*performance",                 "SI:glob_perf"),
    # Export & productivity
    (r"export.*productivit",                      "SI:exp_prod"),
    (r"productivit.*export",                      "SI:prod_exp"),
    (r"learning.by.export",                       "SI:LBE"),
    (r"self.selection.*export",                   "SI:self_sel_exp"),
    (r"export.*profit",                           "SI:exp_profit"),
    (r"profit.*export",                           "SI:profit_exp"),
    (r"export.*perform",                          "SI:exp_perf"),
    (r"perform.*export",                          "SI:perf_exp"),
    # Cross-border & MNE performance
    (r"cross.border acqui.*performance",          "SI:xborder_perf"),
    (r"performance.*cross.border acqui",          "SI:perf_xborder"),
    (r"\bmne\b.*performance",                     "SI:mne_perf"),
    (r"performance.*\bmne\b",                     "SI:perf_mne"),
    # FDI & productivity
    (r"outward fdi.*productiv",                   "SI:ofdi_prod"),
    (r"fdi.*productiv",                           "SI:fdi_prod"),
    (r"fdi.*firm.*performance",                   "SI:fdi_firmperf"),
    (r"outward.*fdi.*firm.*performance",          "SI:ofdi_firmperf"),
    (r"impact of.*fdi.*on.*firm",                 "SI:fdi_firm"),
    (r"fdi.*and.*firm performance",               "SI:fdi_firmperf2"),
    # Firm value & financial
    (r"internationali\w+.*firm value",            "SI:intl_fv"),
    (r"internationali\w+.*financial",             "SI:intl_financial"),
    (r"financial.*internationali",                "SI:financial_intl"),
    # Digital & e-commerce I→P
    (r"e.commerce.*performance",                  "SI:ecom_perf"),
    (r"cross.border e.commerce.*perform",         "SI:xb_ecom_perf"),
    (r"digitali[zs].*cross.border.*perform",      "SI:dig_xb_perf"),
    # ESG + globalization → financial performance
    (r"globali[sz]\w*.*esg.*financial performance","SI:glob_esg_finperf"),
    # Explicit impact/effect phrases
    (r"impact of.*internation.*on.*perform",      "SI:impact_intl_perf"),
    (r"effect of.*internation.*on.*perform",      "SI:effect_intl_perf"),
    (r"internation.*and.*perform",                "SI:intl_and_perf"),
    (r"impact of.*export.*on.*performance",       "SI:imp_exp_perf"),
    # Performance consequences
    (r"performance consequences",                 "SI:perf_consequences"),
    # Optimal DOI / deviations
    (r"(?:deviations|misfits).*optimal.*multinational",  "SI:optimal_doi_dev"),
    (r"optimal multinational.*subsequent",        "SI:optimal_doi_subseq"),
    # Over-internationalization
    (r"over.internationaliz.*reduc",              "SI:over_intl_reduce"),
    (r"reduc.*international.*footprint",          "SI:intl_footprint_reduce"),
    # Domestic-to-exporter performance
    (r"transition.*export.*productiv",            "SI:transition_exp_prod"),
    (r"becoming.*exporter.*perform",              "SI:become_exporter_perf"),
    (r"crisis.*resili.*internation",              "SI:crisis_resil_intl"),
    # OFDI home transformation → performance
    (r"investing abroad.*transform.*home",        "SI:ofdi_home_transform"),
    (r"outward.*fdi.*home.*firm",                 "SI:ofdi_home_firm"),
    # Manufacturing/firm productivity + exports
    (r"firm.*productiv.*export",                  "SI:firm_prod_exp"),
    (r"manufacturing.*export.*productiv",         "SI:mfg_exp_prod"),
    # Common I→P measure patterns
    (r"\bfsts\b.*(?:perform|productiv|value)",    "SI:fsts_perf"),
    (r"\bdegree of internationalization\b",       "SI:doi_explicit"),
    (r"foreign sales.*(?:ratio|share).*perform",  "SI:fs_ratio_perf"),
    # SME internationalization → performance
    (r"sme.*internation.*perform",                "SI:sme_intl_perf"),
    (r"internation.*sme.*perform",                "SI:intl_sme_perf"),
    # Learning/experience effects on performance
    (r"international experience.*performance",    "SI:intl_exp_perf"),
    (r"performance.*international experience",    "SI:perf_intl_exp"),
    # Multinationality → market value
    (r"multinationalit.*value",                   "SI:multi_value"),
    (r"multinational.*corporate.*performance",    "SI:mn_corp_perf"),
    # Regional vs global → performance
    (r"regional.*global.*performance",            "SI:regional_glob_perf"),
    (r"regiona\w+.*internation.*performance",     "SI:regional_intl_perf"),
    # Curvilinear / nonlinear I→P
    (r"(?:curvilinear|inverted.u|u.shaped|nonlinear).*(?:internation|export).*performance",
                                                  "SI:curvilinear_intl_perf"),
    (r"(?:internation|export).*(?:curvilinear|inverted.u|u.shaped|nonlinear).*performance",
                                                  "SI:intl_curvilinear_perf"),
    # Exporter vs non-exporter premium
    (r"exporter.*non.exporter.*productiv",        "SI:exp_nonexp_prod"),
    (r"(?:premium|wage|productiv).*exporter",     "SI:exporter_premium"),
    # Liability of foreignness / home country advantage + performance
    (r"liability.*foreig\w+.*performance",        "SI:lof_perf"),
    (r"home.*advantage.*internation.*performance","SI:home_adv_perf"),
    # Performance outcomes (explicit)
    (r"performance outcomes.*(?:internation|multinational|global)", "SI:perf_outcomes"),
    (r"(?:internation|multinational|global).*performance outcomes", "SI:intl_perf_outcomes"),
]

STRONG_INCL = [(re.compile(p, re.IGNORECASE), tag) for p, tag in STRONG_INCL_RAW]

# ─── DUAL-SIGNAL: INTL × PERF heuristic ──────────────────────────────────────

INTL_RE = re.compile(
    r"\b(internationaliz\w+|multinationalit\w*|multinational\b|"
    r"globali[sz]\w+|export\b|outward fdi\b|foreign sales\b|"
    r"ofdi\b|cross.border acqui|overseas expan\w*|"
    r"foreign direct invest\w*|degree of internation|"
    r"fdi.*firm|internationali[zs]ation)\b",
    re.IGNORECASE
)

PERF_RE = re.compile(
    r"\b(financial performance|firm performance|business performance|"
    r"corporate performance|economic performance|operating performance|"
    r"export performance|mne performance|subsidiary performance|"
    r"profitabilit\w+|profitab\w+|return on assets|return on equity|"
    r"roa\b|roe\b|ros\b|tobin'?s? ?q\b|market value\b|firm value\b|"
    r"productivity\b|labour productivity|labor productivity|"
    r"total factor productivity|tfp\b|"
    r"sales growth|revenue growth|earnings qualit\w+|"
    r"financial result|economic result|value creation\b|"
    r"competitiveness\b|financial effect|economic effect|"
    r"performance implication|performance outcome)\b",
    re.IGNORECASE
)


def screen_title(title: str) -> tuple[str, str]:
    """Return (decision, reason)."""
    t = title.strip()

    # 1. HARD exclusion
    for pat, tag in HARD_EXCL:
        if pat.search(t):
            return "N", f"HARD:{tag}"

    # 2. Strong inclusion
    for pat, tag in STRONG_INCL:
        if pat.search(t):
            return "Y", f"STRONG:{tag}"

    # 3. Dual-signal heuristic
    if INTL_RE.search(t) and PERF_RE.search(t):
        return "Y", "DUAL:intl+perf"

    return "UNSURE", "title_insufficient"


# ─── Main ─────────────────────────────────────────────────────────────────────

with open(TRACKER_V3) as f:
    all_rows = list(csv.DictReader(f))
    cols = list(all_rows[0].keys())

# New candidates are rows after the original 435 (seq > 435 max_seq_original)
# The original tracker had 435 rows; new rows have seq >= 436
EXISTING_SEQ_CUTOFF = 435
new_rows = [r for r in all_rows if int(r.get('seq', '0') or 0) > EXISTING_SEQ_CUTOFF]
print(f"New rows to screen: {len(new_rows)}")

decisions = Counter()
results = []
for row in new_rows:
    title = row.get('title', '')
    decision, reason = screen_title(title)
    decisions[decision] += 1
    results.append({
        'seq': row['seq'],
        'title': title[:120],
        'year': row.get('year', ''),
        'journal': row.get('journal', ''),
        'doi': row.get('doi', ''),
        'extraction_priority': row.get('extraction_priority', ''),
        'decision': decision,
        'reason': reason,
    })

# Write output CSV
outcols = ['seq','title','year','journal','doi','extraction_priority','decision','reason']
with open(OUT_CSV, 'w', newline='', encoding='utf-8') as f:
    w = csv.DictWriter(f, fieldnames=outcols)
    w.writeheader()
    w.writerows(results)

# Summary
lines = [
    f"Title screening of {len(new_rows)} new candidates — {TODAY}",
    f"",
    f"  Y      (include):  {decisions['Y']:5d}  ({decisions['Y']/len(new_rows)*100:.1f}%)",
    f"  N      (exclude):  {decisions['N']:5d}  ({decisions['N']/len(new_rows)*100:.1f}%)",
    f"  UNSURE (abstract): {decisions['UNSURE']:5d}  ({decisions['UNSURE']/len(new_rows)*100:.1f}%)",
    f"",
    f"Top exclusion reasons:",
]
n_reasons = Counter(r['reason'] for r in results if r['decision']=='N')
for tag, cnt in n_reasons.most_common(15):
    lines.append(f"  {cnt:4d}  {tag}")
lines.append("")
lines.append("Top inclusion reasons:")
y_reasons = Counter(r['reason'] for r in results if r['decision']=='Y')
for tag, cnt in y_reasons.most_common(15):
    lines.append(f"  {cnt:4d}  {tag}")

summary = "\n".join(lines)
print(summary)
with open(OUT_TXT, 'w') as f:
    f.write(summary + "\n")

print(f"\nOutput: {OUT_CSV}")
print(f"Summary: {OUT_TXT}")

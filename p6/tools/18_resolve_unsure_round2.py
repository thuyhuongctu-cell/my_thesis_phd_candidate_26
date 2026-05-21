#!/usr/bin/env python3
"""
Script 18: Second-pass title-pattern resolution for 263 still-UNSURE papers.

Classification hierarchy:
  1. HARD_EXCL  — pure antecedents/process/theory/methodology; apply first
  2. INCL        — strong I→P performance signal present; overrides SOFT_EXCL
  3. SOFT_EXCL  — CSR/ESG as main topic (only if no INCL match)
  4. UNSURE     — default; needs abstract/full-text

Key fix from inspection: "Globalization + ESG rating → Financial Performance" papers
are I→P (financial perf as DV) and must be caught by INCL before SOFT_EXCL fires.
"""

import csv, re, pathlib

BASE = pathlib.Path(__file__).parent
RES  = BASE / "results"
TODAY = "20260518"

INPUT   = RES / f"unsure_still_{TODAY}.csv"
OUT_Y   = RES / f"unsure_resolved_round2_Y_{TODAY}.csv"
OUT_N   = RES / f"unsure_resolved_round2_N_{TODAY}.csv"
OUT_UNK = RES / f"unsure_still_round2_{TODAY}.csv"
OUT_ALL = RES / f"unsure_round2_all_{TODAY}.csv"


# ─── TIER 1: HARD exclusions (apply before INCL check) ───────────────────────
# Only patterns that are unambiguously NOT I→P outcome papers

HARD_EXCL = [
    # Governance / board structure
    (r"\bboard composition\b",                    "gov:board_composition"),
    (r"\bboard structure\b",                      "gov:board_structure"),
    (r"\bcorporate governance\b",                 "gov:corp_gov"),
    (r"\bgender diversity\b.*\bboard\b",          "gov:gender_board"),
    # Antecedents of internationalization (not outcome papers)
    (r"\bentry mode\b",                           "ant:entry_mode"),
    (r"\blocation choice\b",                      "ant:location"),
    (r"\binternationalization speed\b",           "ant:speed"),
    (r"\binternationa\w* decision\b",             "ant:decision"),
    (r"\bdrivers of.*internation",                "ant:drivers"),
    (r"\bdeterminants of.*internation",           "ant:determinants"),
    (r"\bpropensity to export\b",                 "ant:propensity"),
    (r"\bexport initiat\w+\b",                    "ant:export_init"),
    (r"\bhow.*digital.*facilitat.*internation",   "ant:dig_facilitates"),
    (r"\bdigital transformat\w+.*facilitat.*internation", "ant:digtr_intl"),
    (r"\binstitutional void\b",                   "ant:inst_void"),
    (r"\binstitutional distance\b",               "ant:inst_dist"),
    # Pure process / strategy (not performance outcome)
    (r"\bstrategic change\b",                     "proc:strategic_change"),
    (r"\binternationalization process\b",         "proc:process"),
    (r"\btemporal misalignment",                  "proc:temporal"),
    (r"\bglobal value chain\b",                   "proc:GVC"),
    (r"\bsupply chain\b",                         "proc:supply_chain"),
    (r"\bknowledge transfer\b",                   "proc:knowledge_transfer"),
    (r"\bknowledge spillover\b",                  "proc:spillover"),
    # Behavioral / psychological
    (r"\baffect.enacted\b",                       "beh:affect"),
    (r"\bceo narcissism\b",                       "beh:narcissism"),
    (r"\btmt faultlines\b",                       "beh:faultlines"),
    # Theory / methodology papers
    (r"\bbibliometric\b",                         "meth:bibliometric"),
    (r"\bsystematic review\b",                    "meth:sys_review"),
    (r"\bliterature review\b",                    "meth:lit_review"),
    (r"\bconceptual framework\b",                 "meth:conceptual"),
    (r"\bpenrose'?s? theory\b",                   "theory:penrose"),
    (r"\bborn global theory\b",                   "theory:born_global"),
    (r"\buppsala model\b",                        "theory:uppsala"),
    # M&A / alliance formation strategy (not performance)
    (r"\bjoint venture formation\b",              "strat:jv_form"),
    (r"\bacquisition strategy\b",                 "strat:acq_strat"),
    # Macro / country level
    (r"\bpublic funding\b",                       "macro:pub_fund"),
    (r"\beconomic growth of\b",                   "macro:econ_growth"),
    # Trade credit (finance antecedent)
    (r"\btrade credit\b",                         "fin:trade_credit"),
    # Leadership / orientation toward internationalization (antecedent)
    (r"\bleadership orientation\b.*export",       "ant:leadership_orient"),
    (r"\boffshoring\b.*\bbackshoring\b",          "strat:offshoring"),
    (r"\bcorporate political activit\w+.*internation", "ant:CPA_intl"),
]

# ─── TIER 2: INCLUDE signals ──────────────────────────────────────────────────

INTL_RE = re.compile(
    r"\b(internationaliz\w+|internationaliz|multinationalit|multinational\b|"
    r"globali[sz]\w+|globaliz\w+|export\b|outward fdi\b|foreign sales\b|"
    r"ofdi\b|cross.border acqui|overseas expan|foreign direct invest\w+|"
    r"degree of internation|fdi.*firm|"
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
    r"competitiveness\b.*export|export.*competitiveness\b|"
    r"financial effect|economic effect|performance implication)\b"
)

STRONG_INCL = [
    (r"performance.*internationaliz",             "SI:perf_intl"),
    (r"internationaliz.*performance",             "SI:intl_perf"),
    (r"multinationalit.*performance",             "SI:multi_perf"),
    (r"performance.*multinationalit",             "SI:perf_multi"),
    (r"globali[sz].*financial performance",       "SI:glob_finperf"),
    (r"financial performance.*globali[sz]",       "SI:finperf_glob"),
    (r"export.*productivit",                      "SI:exp_prod"),
    (r"productivit.*export",                      "SI:prod_exp"),
    (r"learning.by.export",                       "SI:LBE"),
    (r"self.selection.*export",                   "SI:self_sel_exp"),
    (r"cross.border acqui.*performance",          "SI:xborder_perf"),
    (r"performance.*cross.border acqui",          "SI:perf_xborder"),
    (r"\bmne\b.*performance",                     "SI:mne_perf"),
    (r"outward fdi.*productiv",                   "SI:ofdi_prod"),
    (r"fdi.*productiv",                           "SI:fdi_prod"),
    (r"export.*profit",                           "SI:exp_profit"),
    (r"profit.*export",                           "SI:profit_exp"),
    (r"internationali\w+.*firm value",            "SI:intl_fv"),
    (r"impact of.*internation.*on.*perform",      "SI:impact_intl_perf"),
    (r"effect of.*internation.*on.*perform",      "SI:effect_intl_perf"),
    (r"internation.*and.*perform",                "SI:intl_and_perf"),
    (r"globali\w+.*perform",                      "SI:glob_perf"),
    (r"perform.*globali",                         "SI:perf_glob"),
    (r"export.*perform",                          "SI:exp_perf"),
    (r"perform.*export",                          "SI:perf_exp"),
    (r"impact of.*fdi.*on.*firm",                 "SI:fdi_firm"),
    (r"fdi.*and.*firm performance",               "SI:fdi_firmperf"),
    (r"firm.*productiv.*export",                  "SI:firm_prod_exp"),
    (r"manufacturing.*export.*productiv",         "SI:mfg_exp_prod"),
    (r"outward.*fdi.*firm.*performance",          "SI:ofdi_firmperf"),
    (r"internationali\w+.*financial",             "SI:intl_financial"),
    (r"financial.*internationali",                "SI:financial_intl"),
    (r"impact of.*export.*on.*performance",       "SI:imp_exp_perf"),
    (r"e.commerce.*performance",                  "SI:ecom_perf"),
    (r"cross.border e.commerce.*perform",         "SI:xb_ecom_perf"),
    (r"digitali[zs].*cross.border.*perform",      "SI:dig_xb_perf"),
    # ESG/globalization → financial performance (I→P with ESG moderator)
    (r"globali[sz]\w*.*esg.*financial performance",  "SI:glob_esg_finperf"),
    (r"globali[sz]\w*.*financial performance",        "SI:glob_finperf2"),
]

# ─── TIER 3: SOFT exclusions (apply only if no INCL match) ───────────────────

SOFT_EXCL = [
    # CSR/ESG as main topic (not as moderator of I→P)
    (r"\bcorporate social responsibility\b",      "csr:CSR"),
    (r"\bcsr\b",                                  "csr:CSR_abbrev"),
    (r"\besg rating\b",                           "csr:ESG_rating"),
    (r"\besg performance\b",                      "csr:ESG_perf"),
    (r"\bgreen internationali",                   "csr:green_intl"),
    (r"\bgreen technology\b",                     "csr:green_tech"),
    (r"\boutward fdi.*green\b",                   "csr:ofdi_green"),
    (r"\bcarbon emission",                        "csr:carbon"),
    (r"\bsustainable development goals\b",        "csr:SDG"),
    # Board internationalization (governance, not performance)
    (r"\bboard internationali",                   "gov:board_intl"),
    # Pure macro / country level
    (r"\bcountry.level\b",                        "macro:country_level"),
    # SME participation as entry mode (antecedent)
    (r"\bentry mode to foreign markets\b",        "ant:sme_entry"),
    # Alliance/partnership role in internationalization
    (r"\bstrategic alliance\b.*internationali",   "strat:alliance"),
    (r"\brole of.*alliance\b",                    "strat:role_alliance"),
]


def classify_title(title: str) -> tuple[str, str]:
    tl = title.lower()

    # Tier 1: Hard exclusions
    for pat, reason in HARD_EXCL:
        if re.search(pat, tl):
            return "N", f"HARD:{reason}"

    # Tier 2: Strong include
    for pat, reason in STRONG_INCL:
        if re.search(pat, tl):
            return "Y", reason

    # Tier 2b: Composite intl+perf signal
    if INTL_RE.search(tl) and PERF_RE.search(tl):
        return "Y", "COMP:intl+perf"

    # Tier 3: Soft exclusions (only if no INCL match)
    for pat, reason in SOFT_EXCL:
        if re.search(pat, tl):
            return "N", f"SOFT:{reason}"

    return "UNSURE", "still_ambiguous_needs_abstract"


def main():
    with open(INPUT, encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f))
    fieldnames = list(rows[0].keys()) + ["round2_decision", "round2_reason"]

    y_rows, n_rows, unk_rows, all_rows = [], [], [], []

    for r in rows:
        dec, reason = classify_title(r["title"])
        r2 = dict(r, round2_decision=dec, round2_reason=reason)
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

    print(f"\nRound-2 resolution of {len(rows)} still-UNSURE papers:")
    print(f"  Y  (newly confirmed):   {len(y_rows):3d}")
    print(f"  N  (newly excluded):    {len(n_rows):3d}")
    print(f"  UNSURE (still pending): {len(unk_rows):3d}")

    print("\nTop Y reasons:")
    yr = {}
    for r in y_rows: yr[r['round2_reason']] = yr.get(r['round2_reason'],0) + 1
    for k, v in sorted(yr.items(), key=lambda x: -x[1])[:10]:
        print(f"  {v:3d}  {k}")

    print("\nTop N reasons:")
    nr = {}
    for r in n_rows: nr[r['round2_reason']] = nr.get(r['round2_reason'],0) + 1
    for k, v in sorted(nr.items(), key=lambda x: -x[1])[:15]:
        print(f"  {v:3d}  {k}")

if __name__ == "__main__":
    main()

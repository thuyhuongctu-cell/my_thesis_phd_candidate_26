#!/usr/bin/env python3
"""
Script 25: Round-5 UNSURE resolution using OpenAlex-fetched abstracts.

Input (normal mode):    openalex_unsure_r4_abstracts_20260519.csv  (from script 24)
Input (--title-only):   unsure_still_round4_20260518.csv           (direct fallback)

Output: unsure_resolved_round5_Y_YYYYMMDD.csv
        unsure_resolved_round5_N_YYYYMMDD.csv
        unsure_still_round5_YYYYMMDD.csv          ← need manual review
        unsure_round5_all_YYYYMMDD.csv

Resolution logic (applied to title+abstract combined):
  1. HARD_EXCL (→ N) — checked first; takes priority over everything
  2. STRONG_INCL (→ Y)
  3. Composite: INTL_SIGNAL + PERF_SIGNAL + UNIT_SIGNAL → Y (only if abstract available)
  4. SOFT_EXCL (→ N) — only if no INCL match and abstract available
  5. Else → still UNSURE (need manual full-text review)

Abstract text enables much finer discrimination than title alone.

--title-only flag: skip OpenAlex input requirement; run on round-4 UNSURE
  titles only (abstract = '').  Resolves title-conclusive cases now; leaves
  abstract-ambiguous papers as UNSURE for the full abstract pass later.
  Overwrites the same output files so a full re-run supersedes title-only results.
"""

import argparse, csv, re, pathlib
from collections import defaultdict

BASE  = pathlib.Path(__file__).parent
RES   = BASE / "results"
TODAY = "20260519"

INPUT   = RES / f"openalex_unsure_r4_abstracts_{TODAY}.csv"
OUT_Y   = RES / f"unsure_resolved_round5_Y_{TODAY}.csv"
OUT_N   = RES / f"unsure_resolved_round5_N_{TODAY}.csv"
OUT_UNK = RES / f"unsure_still_round5_{TODAY}.csv"
OUT_ALL = RES / f"unsure_round5_all_{TODAY}.csv"


# ─── pattern lists ────────────────────────────────────────────────────────────
# Each entry: (compiled_regex, label)

HARD_EXCL = [
    # ── antecedent / determinant studies (X → internationalisation) ────────────
    (re.compile(r"\b(?:determinants?|drivers?|predictors?|antecedents?|motivations?|barriers?|obstacles?|intentions?)\s+of\s+(?:export|internation\w*|fdi|outward)\b", re.I), "HARD:ant:of_internationalisation"),
    (re.compile(r"\b(?:what|why|how|factors?)\s+(?:drives?|explain|determine|predict|lead\s+to)\s+(?:export|internation\w*|fdi)\b", re.I), "HARD:ant:what_drives"),
    (re.compile(r"\bexport\s+propensity\b|\bexport\s+participation\b|\bexport\s+entry\b|\bexport\s+decision\b", re.I), "HARD:ant:export_propensity_entry"),
    (re.compile(r"\bfirm\s+(?:size|age|experience)\s+and\s+(?:export|internation)\b", re.I), "HARD:ant:size_age_export"),
    (re.compile(r"\bselection\s+into\s+(?:export|global|international)\b", re.I), "HARD:ant:selection_into"),
    (re.compile(r"\bself.selection\b.{0,60}export", re.I), "HARD:ant:self_selection_export"),
    (re.compile(r"\blearning.by.exporting\b|\blearning\s+to\s+export\b|\blearn\w*\s+by\s+exporting\b", re.I), "HARD:ant:learning_by_exporting"),
    # ── DV = innovation ────────────────────────────────────────────────────────
    (re.compile(r"\binnovation\s+(?:performance|output|activity|capability|behavior)\b", re.I), "HARD:DV:innov_perf"),
    (re.compile(r"\bpatent(?:s|ing)?\s+(?:output|count|application|intensity)\b", re.I), "HARD:DV:patents"),
    (re.compile(r"\bproduct\s+innovation\s+and\s+(?:export|internation)\b", re.I), "HARD:DV:product_innov"),
    (re.compile(r"\bR&D\s+(?:spending|expenditure|intensity)\s+(?:and|of)\s+(?:export|multinational)\b", re.I), "HARD:DV:rd_intensity"),
    # ── DV = employment / wages / labour ──────────────────────────────────────
    (re.compile(r"\b(?:employment|job|wage|worker|labour|labor)\s+(?:effect|impact|consequence|growth|creation)\b", re.I), "HARD:DV:employment"),
    (re.compile(r"\b(?:labour|labor)\s+(?:productivity)\s+(?:and|of)\s+(?:export|internation|trade)\b", re.I), "HARD:DV:labour_prod_antecedent"),
    # ── DV = ESG / CSR / sustainability ───────────────────────────────────────
    (re.compile(r"\b(?:esg|environmental|social\s+responsibility|corporate\s+social)\s+(?:perform|score|report|rating)\b", re.I), "HARD:DV:esg_csr"),
    (re.compile(r"\bcarbon\s+(?:emission|footprint|intensity)\b|\bco2\s+emission\b", re.I), "HARD:DV:carbon"),
    # ── country-level / macro ─────────────────────────────────────────────────
    (re.compile(r"\b(?:gdp|gnp|national\s+income|economic\s+growth)\s+(?:and|of)\s+(?:export|trade|fdi)\b", re.I), "HARD:macro:gdp_trade"),
    (re.compile(r"\bcountry.level\s+(?:data|analysis|study|evidence)\b", re.I), "HARD:macro:country_level"),
    (re.compile(r"\b(?:industry|sector).level\s+(?:data|analysis)\b.{0,50}(?:export|trade|fdi)\b", re.I), "HARD:macro:industry_level"),
    (re.compile(r"\bspillover\s+effects?\s+of\s+(?:fdi|foreign\s+direct\s+invest)", re.I), "HARD:macro:fdi_spillover"),
    (re.compile(r"\btrade\s+openness\s+and\s+(?:gdp|growth|develop)\b", re.I), "HARD:macro:trade_openness_gdp"),
    # ── qualitative / conceptual ──────────────────────────────────────────────
    (re.compile(r"\b(?:qualitative|case\s+study|interview|grounded\s+theory|narrative)\s+(?:research|approach|method|study)\b", re.I), "HARD:method:qualitative"),
    (re.compile(r"\bconceptual\s+(?:paper|framework|model|contribution|article)\b", re.I), "HARD:method:conceptual"),
    (re.compile(r"\b(?:systematic\s+review|meta.analysis|literature\s+review)\s+of\s+(?:export|internation\w*|fdi)\b", re.I), "HARD:method:review_of_export"),
    # ── capital structure ─────────────────────────────────────────────────────
    (re.compile(r"\bcapital\s+structure\b.{0,80}(?:export|multinational|internation)\b", re.I), "HARD:fin:capital_structure"),
    (re.compile(r"\bdebt\s+(?:ratio|financing|maturity)\b.{0,60}(?:export|internation)\b", re.I), "HARD:fin:debt_export"),
    # ── location / entry mode strategy ───────────────────────────────────────
    (re.compile(r"\blocation\s+(?:choice|selection|decision)\s+of\s+(?:fdi|mne|subsidiary|offshore)\b", re.I), "HARD:strat:location_choice"),
    (re.compile(r"\bentry\s+mode\s+(?:choice|selection|decision)\b", re.I), "HARD:strat:entry_mode"),
    (re.compile(r"\bwholly.owned\s+subsidiary\s+vs\s+joint\s+venture\b", re.I), "HARD:strat:ownership_structure"),
    # ── eco-innovation plural form (singular already in R4; plural missed) ───
    (re.compile(r"\beco.innovation(?:s|al)?\b", re.I), "HARD:DV:eco_innov_plural"),
    # ── proactive environmental strategy as DV ────────────────────────────────
    (re.compile(r"\bproactive\s+environmental\s+strateg", re.I), "HARD:DV:proactive_env_strat"),
    # ── effects of internationalisation ON innovation (explicit innovation DV)
    (re.compile(r"\beffects?\s+of\s+internation\w*\s+on\s+innovation", re.I), "HARD:DV:intl_on_innovation"),
    # ── absorptive capacity FROM FDI (capability DV, not financial performance)
    (re.compile(r"\babsorptive\s+capacity\s+from\s+(?:fdi|foreign\s+direct)", re.I), "HARD:DV:absorptive_cap_fdi"),
    # ── export + financial constraints (antecedent: constraints → export) ────
    (re.compile(r"exports?\b.{0,80}financial\s+constraints?|financial\s+constraints?.{0,80}\bexports?\b", re.I), "HARD:ant:export_financial_constraints"),
    # ── internationalisation AND innovation intensities (dual-DV, not I→P) ───
    (re.compile(r"\binternation\w+\s+and\s+innovation\s+intensit", re.I), "HARD:DV:intl_innov_intensity"),
    # ── innovation management of internationalised firms (innovation DV) ─────
    (re.compile(r"\binnovation\s+management\s+of\s+internation", re.I), "HARD:DV:innov_mgmt_intl"),
    # ── innovation activities + learning processes (non-financial DVs) ───────
    (re.compile(r"\binnovation\s+activities\b.{0,80}\blearning\s+processes?", re.I), "HARD:DV:innov_activities_learning"),
]

STRONG_INCL = [
    # ── explicit I→P quantitative claim ──────────────────────────────────────
    (re.compile(r"(?:effect|impact|relation(?:ship)?|influence)\s+of\s+(?:internationaliz\w*|exports?|fdi|doi|degree\s+of\s+internation)\s+on\s+(?:firm\s+)?(?:performance|profitab|productiv|tobin|roa|roe|roa)\b", re.I), "SI:effect_of_I_on_P"),
    (re.compile(r"(?:internationaliz\w*|export\s+intensity|degree\s+of\s+internation|doi\b).{0,60}(?:firm\s+perform|financial\s+perform|profitab|tobin|roa|labour\s+productiv)\b", re.I), "SI:I_and_P_linked"),
    (re.compile(r"(?:roa|roe|tobin.s\s+q|return\s+on\s+(?:assets|equity)|profitab).{0,60}(?:internationaliz\w*|export\s+intensit|fdi|multinational|doi\b)\b", re.I), "SI:P_and_I_linked"),
    # ── curvilinear / nonlinear ───────────────────────────────────────────────
    (re.compile(r"(?:inverted.?u|u.shaped|curvilinear|nonlinear|quadratic)\s+(?:relation|effect|link).{0,60}(?:internationaliz\w*|export|doi|multinational)\b", re.I), "SI:curvilinear_I_P"),
    (re.compile(r"turning\s+point.{0,60}(?:internationaliz\w*|export|doi)\b", re.I), "SI:turning_point"),
    # ── moderation of I→P ────────────────────────────────────────────────────
    (re.compile(r"modera(?:te|tion|tor)\b.{0,80}(?:internationaliz\w*|export\s+intensit|doi\b|fsts\b)\b", re.I), "SI:moderation_I_P"),
    (re.compile(r"(?:technology|digital|institutional).{0,40}modera.{0,40}(?:internationaliz\w*|export)\b", re.I), "SI:tech_digital_modera"),
    # ── WBES / survey firm data ───────────────────────────────────────────────
    (re.compile(r"\b(?:world\s+bank\s+enterprise\s+survey|enterprise\s+survey|firm.level\s+survey\s+data)\b", re.I), "SI:wbes_data"),
    (re.compile(r"\bfirm.level\s+(?:panel\s+)?data.{0,50}(?:export|internation|multinational)\b", re.I), "SI:firm_level_panel"),
    # ── survival / resilience / crisis ────────────────────────────────────────
    (re.compile(r"\b(?:survival|hazard|exit\s+rate|firm\s+exit)\b.{0,80}(?:export|internation\w*|fdi)\b", re.I), "SI:survival_export"),
    (re.compile(r"\b(?:resilience|crisis\s+(?:performance|survival))\b.{0,80}(?:export|internation|multinational)\b", re.I), "SI:resilience_intl"),
    # ── productivity ──────────────────────────────────────────────────────────
    (re.compile(r"\b(?:labour\s+productiv|total\s+factor\s+productiv|tfp|output\s+per\s+worker)\b.{0,60}(?:export|internation|multinational|fdi)\b", re.I), "SI:productivity_export"),
    # ── over-internationalisation ─────────────────────────────────────────────
    (re.compile(r"\bover.?internationaliz\b|\bbeyond\s+optimal.{0,30}internationaliz\b", re.I), "SI:over_intl"),
    # ── explicit r/beta/coefficient reported ─────────────────────────────────
    (re.compile(r"\b(?:pearson\s+r|effect\s+size|regression\s+coefficient|standardized\s+beta|path\s+coefficient)\s*=\s*[-0-9.]", re.I), "SI:effect_size_reported"),
    (re.compile(r"\bcorrelation\s+matrix\b|\bpath\s+analysis\b.{0,40}(?:export|internation)\b", re.I), "SI:correlation_matrix"),
    # ── born-global + performance (title alone is decisive) ──────────────────
    (re.compile(r"\bborn.global\w*.{0,60}\bperform\w*\b", re.I), "SI:born_global_perf"),
    # ── efficiency and exports (I→P: export status/intensity → efficiency) ───
    (re.compile(r"\befficiency\s+and\s+exports?\b|\bexports?\s+and\s+(?:firm\s+)?efficienc", re.I), "SI:efficiency_exports"),
    # ── effects on (SME) growth with export/internation context ─────────────
    (re.compile(r"(?:exports?|internation\w*|trade).{0,60}effects?\s+on\s+(?:sme\s+)?(?:growth|perform)\b|effects?\s+on\s+(?:sme\s+)?(?:growth|perform)\b.{0,60}(?:exports?|internation\w*|trade)", re.I), "SI:effects_on_growth_exports"),
]

# Composite signals (need INTL + PERF + UNIT to → Y)
INTL_SIGNAL = re.compile(
    r"\b(?:export(?:er|ing|s)?|internationaliz\w*|internationalise\w*|fdi\b|multinational|"
    r"doi\b|fsts\b|foreign\s+sales?|cross.border|overseas|outward\s+fdi|global\s+reach)\b",
    re.I)

PERF_SIGNAL = re.compile(
    r"\b(?:perform(?:ance)?|profitab|tobin|roa\b|roe\b|ros\b|return\s+on\s+(?:asset|equity)|"
    r"productiv|sales\s+growth|revenue\s+growth|survival\b|firm\s+(?:value|exit)|"
    r"market\s+value|hazard\s+rate|exit\s+rate|resilience)\b", re.I)

UNIT_SIGNAL = re.compile(
    r"\b(?:firm.level|company.level|enterprise.level|firm\s+data|"
    r"(?:\d[\d,]+\s+firms?)|survey\s+of\s+(?:firms?|enterprises?|smes?)|"
    r"panel\s+(?:data|of\s+firms?))\b", re.I)

# Soft-exclude patterns: applied only if NO INCL matches
SOFT_EXCL = [
    (re.compile(r"\b(?:country|aggregate|economy|national|macro).level\b", re.I), "SOFT:macro_level"),
    (re.compile(r"\bimport(?:er|s|ing)\s+(?:firm|country|market)\b", re.I), "SOFT:importer_focus"),
    (re.compile(r"\btechnology\s+transfer\s+(?:from|between)\s+(?:multinational|fdi)\b", re.I), "SOFT:tech_transfer_direction"),
]


def check_patterns(text: str, patterns: list) -> str:
    """Return label of first matching pattern, or '' if none."""
    for pat, label in patterns:
        if pat.search(text):
            return label
    return ""


def resolve(title: str, abstract: str) -> tuple[str, str]:
    """
    Returns (decision, reason):
      decision = 'Y' | 'N' | 'UNSURE'
    """
    combined = f"{title} {abstract}".lower()
    full_txt = f"{title} {abstract}"   # keep case for some patterns

    # 1. Hard-exclude wins
    hard = check_patterns(full_txt, HARD_EXCL)
    if hard:
        return "N", hard

    # 2. Strong-include wins
    strong = check_patterns(full_txt, STRONG_INCL)
    if strong:
        return "Y", strong

    # 3. Composite signal (only if abstract available)
    if abstract.strip():
        has_intl = bool(INTL_SIGNAL.search(full_txt))
        has_perf = bool(PERF_SIGNAL.search(full_txt))
        has_unit = bool(UNIT_SIGNAL.search(full_txt))
        if has_intl and has_perf and has_unit:
            return "Y", "COMPOSITE:intl+perf+unit_in_abstract"
        if has_intl and has_perf and not has_unit:
            # abstract available but unit not confirmed → UNSURE (prefer over N)
            return "UNSURE", "COMP_partial:intl+perf_no_unit_signal"

    # 4. Soft-exclude (only if abstract available and no INCL)
    if abstract.strip():
        soft = check_patterns(full_txt, SOFT_EXCL)
        if soft:
            return "N", soft

    # 5. No abstract and no decisive signal → still UNSURE
    if not abstract.strip():
        return "UNSURE", "NO_ABSTRACT:unresolved"
    return "UNSURE", "ABSTRACT:no_decisive_pattern"


# ─── main ─────────────────────────────────────────────────────────────────────

def main() -> None:
    parser = argparse.ArgumentParser(description="Script 25 — Round-5 UNSURE resolution")
    parser.add_argument("--title-only", action="store_true",
                        help="Use round-4 UNSURE file directly (no abstract needed). "
                             "Resolves title-conclusive cases; leaves the rest for the "
                             "full abstract pass after running script 24.")
    args = parser.parse_args()

    title_only = args.title_only
    mode_label = "TITLE-ONLY" if title_only else "ABSTRACT"
    print(f"Script 25 — Round-5 UNSURE resolution [{mode_label} mode]")

    if title_only:
        fallback_input = RES / f"unsure_still_round4_20260518.csv"
        if not fallback_input.exists():
            raise SystemExit(f"Fallback input not found: {fallback_input}")
        with open(fallback_input, newline="", encoding="utf-8") as f:
            base_rows = list(csv.DictReader(f))
        rows = []
        for r in base_rows:
            rows.append({**r, "abstract": "", "openalex_id": "", "pdf_url": ""})
        print(f"  Input (title-only fallback): {fallback_input.name}")
        print(f"  Input rows : {len(rows)}")
        print(f"  Note: abstract='' for all rows; composite (step 3) will be skipped.")
    else:
        if not INPUT.exists():
            raise SystemExit(f"Input not found: {INPUT}\nRun script 24 first, "
                             "or use --title-only for partial title-based resolution.")
        with open(INPUT, newline="", encoding="utf-8") as f:
            rows = list(csv.DictReader(f))
        print(f"  Input rows : {len(rows)}")

    has_abstract = sum(1 for r in rows if str(r.get("abstract","") or "").strip())
    if not title_only:
        print(f"  With abstract: {has_abstract}/{len(rows)}")

    y_rows = []
    n_rows = []
    u_rows = []

    for r in rows:
        title    = str(r.get("title",    "") or "")
        abstract = str(r.get("abstract", "") or "")
        decision, reason = resolve(title, abstract)
        r["round5_decision"] = decision
        # Tag title-only decisions so the full abstract pass can overwrite them
        r["round5_reason"]   = (reason + ":TITLE_ONLY") if (title_only and reason) else reason

    for r in rows:
        d = r["round5_decision"]
        if   d == "Y":      y_rows.append(r)
        elif d == "N":      n_rows.append(r)
        else:               u_rows.append(r)

    print(f"\n  Results:")
    print(f"    Y (include)    : {len(y_rows)}")
    print(f"    N (exclude)    : {len(n_rows)}")
    print(f"    Still UNSURE   : {len(u_rows)}")

    # ── write outputs ─────────────────────────────────────────────────────────
    all_rows = rows
    base_cols = list(rows[0].keys())
    add_cols  = [c for c in ["round5_decision","round5_reason"] if c not in base_cols]
    out_cols  = base_cols + add_cols

    def write_csv(path, data):
        with open(path, "w", newline="", encoding="utf-8") as f:
            w = csv.DictWriter(f, fieldnames=out_cols, extrasaction="ignore")
            w.writeheader()
            for r in data:
                w.writerow(r)

    write_csv(OUT_Y,   y_rows)
    write_csv(OUT_N,   n_rows)
    write_csv(OUT_UNK, u_rows)
    write_csv(OUT_ALL, all_rows)

    print(f"\n  Wrote → {OUT_Y.name}   ({len(y_rows)} rows)")
    print(f"  Wrote → {OUT_N.name}   ({len(n_rows)} rows)")
    print(f"  Wrote → {OUT_UNK.name} ({len(u_rows)} rows)")
    print(f"  Wrote → {OUT_ALL.name} ({len(rows)} rows)")

    # ── top patterns summary ───────────────────────────────────────────────────
    from collections import Counter
    y_reasons = Counter(r["round5_reason"] for r in y_rows)
    n_reasons = Counter(r["round5_reason"] for r in n_rows)
    print("\n  Top Y reasons:")
    for reason, cnt in y_reasons.most_common(8):
        print(f"    {cnt:3d}  {reason}")
    print("  Top N reasons:")
    for reason, cnt in n_reasons.most_common(8):
        print(f"    {cnt:3d}  {reason}")

    if u_rows:
        print(f"\n  Still-UNSURE titles (need manual full-text review):")
        for r in u_rows[:15]:
            print(f"    [{r.get('id','')}] {r.get('title','')[:75]}")
            print(f"         reason: {r.get('round5_reason','')}")

    print("\nNext step: run script 26 to merge R5-Y papers into v7 pool.")


if __name__ == "__main__":
    main()

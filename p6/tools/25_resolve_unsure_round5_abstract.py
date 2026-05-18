#!/usr/bin/env python3
"""
Script 25: Round-5 UNSURE resolution using OpenAlex-fetched abstracts.

Input : openalex_unsure_r4_abstracts_20260519.csv (87 rows, from script 24)
Output: unsure_resolved_round5_Y_YYYYMMDD.csv
        unsure_resolved_round5_N_YYYYMMDD.csv
        unsure_still_round5_YYYYMMDD.csv          ← need manual review
        unsure_round5_all_YYYYMMDD.csv

Resolution logic (applied to title+abstract combined):
  1. HARD_EXCL (→ N) — checked first; takes priority over everything
  2. STRONG_INCL (→ Y)
  3. Composite: INTL_SIGNAL + PERF_SIGNAL + UNIT_SIGNAL → Y
  4. SOFT_EXCL (→ N) — only if no INCL match
  5. Else → still UNSURE (need manual full-text review)

Abstract text enables much finer discrimination than title alone.
"""

import csv, re, pathlib
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
    (re.compile(r"\blearning.by.exporting\b|\blearning\s+to\s+export\b", re.I), "HARD:ant:learning_by_exporting"),
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
    (re.compile(r"\bspillover\s+effect\s+of\s+fdi\b", re.I), "HARD:macro:fdi_spillover"),
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
    print("Script 25 — Round-5 abstract-level UNSURE resolution")

    if not INPUT.exists():
        raise SystemExit(f"Input not found: {INPUT}\nRun script 24 first.")

    with open(INPUT, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    print(f"  Input rows : {len(rows)}")

    has_abstract = sum(1 for r in rows if str(r.get("abstract","") or "").strip())
    print(f"  With abstract: {has_abstract}/{len(rows)}")

    y_rows = []
    n_rows = []
    u_rows = []

    for r in rows:
        title    = str(r.get("title",    "") or "")
        abstract = str(r.get("abstract", "") or "")
        decision, reason = resolve(title, abstract)
        r["round5_decision"] = decision
        r["round5_reason"]   = reason

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

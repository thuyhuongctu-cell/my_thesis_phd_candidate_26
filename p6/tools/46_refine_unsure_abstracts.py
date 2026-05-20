#!/usr/bin/env python3
"""
46_refine_unsure_abstracts.py — Second-pass refinement for UNSURE papers with abstracts.

The first-pass auto-screen (44) required ≥2 abstract signals to auto-Y.
This script targets the 678 UNSURE papers that have an abstract and applies:

  - Additional EXCLUDE patterns (macro, wrong outcome, qualitative)
  - Stronger INCLUDE: explicit I→P quantitative study confirmed by abstract
  - REMAIN UNSURE: anything ambiguous

Conservative: only auto-decide when evidence is clear. UNSURE = human review.

Output: updates tracker in-place; writes refinement log.
"""
import csv, re, sys
from datetime import date
from pathlib import Path

DEFAULT_TRACKER   = "p6/tools/results/fulltext_to_extraction_tracker_v3.csv"
DEFAULT_ABSTRACTS = "p6/tools/results/abstracts_20260520.csv"
LOG_OUT = f"p6/tools/results/refine_unsure_log_{date.today().strftime('%Y%m%d')}.csv"

# ── STRONG EXCLUSION patterns (on full abstract text) ─────────────────────────
# Only exclude if the abstract CLEARLY indicates out-of-scope

STRONG_EXCLUDE = [
    # Qualitative only
    (r'\b(grounded theory|discourse analysis|ethnograph|case.stud(y|ies))\b', "qualitative"),
    (r'\b(semi.structured interview|in.depth interview|focus group|interview.based)\b', "qualitative"),
    (r'\bqualitative (approach|method|study|analysis|research)\b', "qualitative"),
    # Macro / country-level (explicit)
    (r'\bcountry.level (regression|panel|analysis|sample|data)\b', "macro_country"),
    (r'\bour (country|cross.country|bilateral) (sample|dataset|analysis)\b', "macro_country"),
    (r'\b(GDP|GNP|national income|trade balance|current account)\b.*\b(dependent variable|outcome)\b', "macro_outcome"),
    # Wrong subject: individuals / workers / managers / students
    (r'\b(employee|worker|manager|staff|student).{1,20}(performance|productivity|outcome)\b', "individual_level"),
    (r'\b(job satisfaction|work engagement|organizational commitment)\b', "individual_level"),
    # Wrong field (non-business performance)
    (r'\b(environmental performance|carbon emission|CO2|greenhouse gas|sustainability performance)\b', "wrong_outcome"),
    (r'\b(social performance|CSR|corporate social responsibility|ESG)\b.*\bperformance\b', "wrong_outcome"),
    (r'\b(hospital|clinic|patient|medical|health care|public health)\b', "health_field"),
    (r'\b(school|university|education|academic achievement)\b', "education_field"),
    # Pure theoretical/conceptual
    (r'\bwe (propose|develop|present) (a )?(framework|model|theory|typology)\b(?!.*empiric)', "conceptual"),
    (r'\bconceptual (paper|study|framework|model|contribution)\b(?!.*empiric)', "conceptual"),
    # Reverse direction: antecedents of internationalization
    (r'\b(determinants?|antecedents?|drivers?) of (firm |SME |company )?internationali', "antecedent"),
    (r'\bwhy (firms?|companies|SMEs?) internationali', "antecedent"),
    (r'\b(propensity|likelihood|decision) to (export|internationali|go abroad)\b', "antecedent"),
    # Meta-analysis / review (should have been caught in title, belt-and-suspenders)
    (r'\b(meta.anal|systematic review|literature review)\b', "review_type"),
]

# ── STRONG INCLUSION patterns (on full abstract text) ─────────────────────────
# Auto-Y only when BOTH a performance outcome AND an internationalization measure
# are clearly firm-level and quantitative in the abstract.

IP_PERFORMANCE = [
    r'\b(ROA|return on assets)\b',
    r'\b(ROE|return on equity)\b',
    r'\b(ROS|return on sales)\b',
    r'\b(Tobin.s Q|market.to.book|firm value)\b',
    r'\b(labor productivity|labour productivity|total factor productivity|TFP)\b',
    r'\b(sales growth|revenue growth|profit(ability)?)\b',
    r'\bfirm.{0,10}(financial )?performance\b',
    r'\bcorporate (financial )?performance\b',
    r'\boperating performance\b',
]

IP_INTERNATIONALIZ = [
    r'\b(FSTS|foreign sales (ratio|intensity|to total))\b',
    r'\b(export intensity|export.to.sales|export.sales ratio)\b',
    r'\b(degree of internationali[sz]ation|DOI)\b',
    r'\b(multinationality|transnationality)\b',
    r'\b(foreign (direct )?investment|FDI|outward FDI|OFDI)\b',
    r'\b(export (propensity|participation|status|behavior|behaviour))\b',
    r'\b(number of (foreign |host )?countries|geographic (scope|diversification|spread))\b',
    r'\bforeign (market|subsidiary|operation|affiliate)\b',
    r'\binternational(i[sz]ation)? (breadth|depth|scope|extent|expansion)\b',
]

QUANTITATIVE_METHOD = [
    r'\b(OLS|panel (data|regression)|fixed.effects?|random.effects?|GMM|2SLS|IV|HAC)\b',
    r'\b(regression|ordinary least squares|instrumental variable|difference.in.differences)\b',
    r'\b(hierarchical regression|multilevel|SEM|structural equation)\b',
    r'\b(longitudinal (data|study)|panel of (firm|company|enterprise)s?)\b',
    r'\b(cross.sectional (data|study)|survey.based)\b',
    r'\b(WBES|World Bank Enterprise Survey|Orbis|Compustat|Amadeus)\b',
]

FIRM_LEVEL = [
    r'\b(firm.level|company.level|enterprise.level)\b',
    r'\b(sample of (firms?|companies|SMEs?|MNEs?|enterprises?))\b',
    r'\b(\d{2,5} (firms?|companies|SMEs?|MNEs?|enterprises?))\b',
    r'\bfirm (size|age|characteristics?)\b',
    r'\bpanel of (\d+ )?firms?\b',
]


def count_hits(text: str, patterns: list) -> int:
    """Count how many distinct patterns match in text."""
    t = text.lower()
    return sum(1 for p in patterns if re.search(p, t, re.IGNORECASE))


def refine(title: str, abstract: str) -> tuple[str, str]:
    """
    Returns (decision, reason).
    decision: 'Y'|'N'|'UNSURE' — only changes if evidence is clear.
    """
    full = f"{title} {abstract}"

    # ─ Strong Excludes ─
    for pattern, reason in STRONG_EXCLUDE:
        if re.search(pattern, full, re.IGNORECASE):
            return "N", f"refine_abs:{reason}"

    # ─ Strong Include: need performance + internationalization + quantitative + firm-level ─
    perf_hits   = count_hits(full, IP_PERFORMANCE)
    intl_hits   = count_hits(full, IP_INTERNATIONALIZ)
    quant_hits  = count_hits(full, QUANTITATIVE_METHOD)
    firm_hits   = count_hits(full, FIRM_LEVEL)

    if perf_hits >= 1 and intl_hits >= 1 and quant_hits >= 1 and firm_hits >= 1:
        return "Y", f"refine_abs:perf={perf_hits},intl={intl_hits},quant={quant_hits},firm={firm_hits}"

    # ─ Partial evidence: performance + internationalization (no method/firm confirm) ─
    if perf_hits >= 1 and intl_hits >= 1:
        return "Y_WEAK", f"refine_abs:perf_intl_only(needs_verify)"

    return "UNSURE", "refine_abs:insufficient"


def main():
    tracker_path = DEFAULT_TRACKER

    # Load abstracts
    abs_map: dict[str, str] = {}
    if Path(DEFAULT_ABSTRACTS).exists():
        with open(DEFAULT_ABSTRACTS, newline="", encoding="utf-8") as f:
            for r in csv.DictReader(f):
                seq = r.get("seq", "").strip()
                ab  = r.get("abstract", "").strip()
                if seq and ab:
                    abs_map[seq] = ab

    with open(tracker_path, newline="", encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    cols = list(rows[0].keys())

    unsure = [r for r in rows if r.get("fulltext_screening_decision", "").strip() == "UNSURE"]
    unsure_with_abs = [r for r in unsure if abs_map.get(r.get("seq", "").strip(), "").strip()]

    print(f"UNSURE total:      {len(unsure)}")
    print(f"UNSURE with abs:   {len(unsure_with_abs)}")

    log_rows = []
    changed = {"Y": 0, "N": 0, "Y_WEAK": 0, "UNSURE": 0}

    row_by_seq = {r["seq"]: r for r in rows}

    for row in unsure_with_abs:
        seq     = row.get("seq", "").strip()
        title   = row.get("title", "")
        abstract = abs_map.get(seq, "")

        decision, reason = refine(title, abstract)
        changed[decision] = changed.get(decision, 0) + 1

        if decision in ("Y", "N"):
            row_by_seq[seq]["fulltext_screening_decision"] = decision
            # Only write reason column if it exists in the tracker
            if "fulltext_screening_reason" in cols:
                row_by_seq[seq]["fulltext_screening_reason"] = reason

        log_rows.append({
            "seq": seq,
            "title": title[:80],
            "old_decision": "UNSURE",
            "new_decision": decision,
            "reason": reason,
            "has_abstract": "Y",
        })

    print(f"\n=== REFINEMENT RESULTS ===")
    print(f"  → Y (auto-include):       {changed.get('Y', 0)}")
    print(f"  → Y_WEAK (perf+intl only): {changed.get('Y_WEAK', 0)}  [not committed — review manually]")
    print(f"  → N (auto-exclude):       {changed.get('N', 0)}")
    print(f"  → remain UNSURE:          {changed.get('UNSURE', 0)}")

    # Atomic write — write to temp then rename to avoid partial-write corruption
    import tempfile, os
    tmp = tracker_path + ".tmp"
    with open(tmp, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=cols, extrasaction="ignore")
        w.writeheader()
        w.writerows(rows)
    os.replace(tmp, tracker_path)

    # Write log
    with open(LOG_OUT, "w", newline="", encoding="utf-8") as f:
        w = csv.DictWriter(f, fieldnames=["seq","title","old_decision","new_decision","reason","has_abstract"])
        w.writeheader()
        w.writerows(log_rows)
    print(f"\nLog: {LOG_OUT}")
    print(f"Tracker updated: {tracker_path}")


if __name__ == "__main__":
    main()

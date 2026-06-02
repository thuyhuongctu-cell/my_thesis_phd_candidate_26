#!/usr/bin/env python3
"""
Unified humanization script for portfolio papers (P3, P4, P5, P6, P7, P8).

Applies the same transformations developed for P9' India:
- Voice transfer (we/our → this study, the analysis, the results)
- Em-dash removal (with title-preservation)
- Mid-sentence emphasis removal
- Negative parallelism cleanup
- Copula avoidance fixes
- Inline-header vertical list conversion
- Filler phrase removal

Idempotent: safe to re-run.

Usage:
    python3 scripts/humanize_portfolio.py --paper p3
    python3 scripts/humanize_portfolio.py --paper all
    python3 scripts/humanize_portfolio.py --paper all --dry-run  # report only
"""

from __future__ import annotations
import argparse
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Map of paper folder → main manuscript filename
PAPERS = {
    "p3": "p3/p3_vietnam_en_clean.md",
    "p4": "p4/p4_singapore_en_clean.md",
    "p5": "p5/p5_china_en_clean.md",
    "p6": "p6/p6_meta_manuscript_en.md",
    "p7": "p7/p7_capstone_en_clean.md",
    "p8": "p8/p8_pacific_sids_en_clean.md",
}


# ============================================================
# TRANSFORMATIONS
# ============================================================

WE_OUR_REPLACEMENTS = [
    # Subject "we" → this study / the analysis
    (r'\bWe exploit\b', 'This study employs'),
    (r'\bwe exploit\b', 'this study employs'),
    (r'\bWe provide\b', 'This study provides'),
    (r'\bwe provide\b', 'this study provides'),
    (r'\bWe examine\b', 'This study examines'),
    (r'\bwe examine\b', 'this study examines'),
    (r'\bWe estimate\b', 'The analysis estimates'),
    (r'\bwe estimate\b', 'the analysis estimates'),
    (r'\bWe test\b', 'This study tests'),
    (r'\bwe test\b', 'this study tests'),
    (r'\bWe document\b', 'This study documents'),
    (r'\bwe document\b', 'this study documents'),
    (r'\bWe propose\b', 'This study proposes'),
    (r'\bwe propose\b', 'this study proposes'),
    (r'\bWe argue\b', 'This study argues'),
    (r'\bwe argue\b', 'this study argues'),
    (r'\bWe find\b', 'The results show'),
    (r'\bwe find\b', 'the results show'),
    (r'\bWe show\b', 'The analysis shows'),
    (r'\bwe show\b', 'the analysis shows'),
    (r'\bWe present\b', 'This study presents'),
    (r'\bwe present\b', 'this study presents'),
    (r'\bWe believe\b', ''),  # often "what we believe to be"
    (r'\bwe believe\b', ''),
    (r'\bWe report\b', 'The analysis reports'),
    (r'\bwe report\b', 'the analysis reports'),
    (r'\bWe acknowledge\b', 'The authors acknowledge'),
    (r'\bwe acknowledge\b', 'the authors acknowledge'),
    (r'\bWe thank\b', 'The authors thank'),
    (r'\bwe thank\b', 'the authors thank'),
    (r'\bWe treat\b', 'This study treats'),
    (r'\bwe treat\b', 'this study treats'),
    (r'\bWe use\b', 'This study uses'),
    (r'\bwe use\b', 'this study uses'),
    (r'\bWe retain\b', 'This study retains'),
    (r'\bwe retain\b', 'this study retains'),
    (r'\bWe refrain\b', 'The analysis refrains'),
    (r'\bwe refrain\b', 'the analysis refrains'),
    (r'\bWe position\b', 'This study positions'),
    (r'\bwe position\b', 'this study positions'),
    (r'\bWe term\b', 'This study terms'),
    (r'\bwe term\b', 'this study terms'),
    (r'\bWe distinguish\b', 'This study distinguishes'),
    (r'\bwe distinguish\b', 'this study distinguishes'),
    (r'\bWe integrate\b', 'This study integrates'),
    (r'\bwe integrate\b', 'this study integrates'),
    (r'\bWe develop\b', 'This study develops'),
    (r'\bwe develop\b', 'this study develops'),
    (r'\bWe pool\b', 'This study pools'),
    (r'\bwe pool\b', 'this study pools'),
    (r'\bWe theorise\b', 'This study theorises'),
    (r'\bwe theorise\b', 'this study theorises'),
    (r'\bWe formalise\b', 'This study formalises'),
    (r'\bwe formalise\b', 'this study formalises'),
    (r'\bWe draw\b', 'This study draws'),
    (r'\bwe draw\b', 'this study draws'),
    (r'\bWe control\b', 'The analysis controls'),
    (r'\bwe control\b', 'the analysis controls'),
    (r'\bWe have verified\b', 'The authors have verified'),
    (r'\bwe have verified\b', 'the authors have verified'),
    (r'\bWe address\b', 'This study addresses'),
    (r'\bwe address\b', 'this study addresses'),
    (r'\bWe advance\b', 'This study advances'),
    (r'\bwe advance\b', 'this study advances'),
    (r'\bWe define\b', 'This study defines'),
    (r'\bwe define\b', 'this study defines'),
    (r'\bWe construct\b', 'This study constructs'),
    (r'\bwe construct\b', 'this study constructs'),
    (r'\bWe focus\b', 'This study focuses'),
    (r'\bwe focus\b', 'this study focuses'),
    (r'\bWe consider\b', 'This study considers'),
    (r'\bwe consider\b', 'this study considers'),
    (r'\bWe expect\b', 'This study expects'),
    (r'\bwe expect\b', 'this study expects'),
    (r'\bWe note\b', 'This study notes'),
    (r'\bwe note\b', 'this study notes'),
    (r'\bWe interpret\b', 'The analysis interprets'),
    (r'\bwe interpret\b', 'the analysis interprets'),
    (r'\bWe characterise\b', 'This study characterises'),
    (r'\bwe characterise\b', 'this study characterises'),
    (r'\bWe offer\b', 'This study offers'),
    (r'\bwe offer\b', 'this study offers'),
    (r'\bWe flag\b', 'This study flags'),
    (r'\bwe flag\b', 'this study flags'),
    (r'\bWe state\b', 'This study states'),
    (r'\bwe state\b', 'this study states'),
    (r'\bWe operationalise\b', 'This study operationalises'),
    (r'\bwe operationalise\b', 'this study operationalises'),
    (r'\bWe adopt\b', 'This study adopts'),
    (r'\bwe adopt\b', 'this study adopts'),
    (r'\bWe do\b', 'This study does'),
    (r'\bwe do\b', 'this study does'),
    (r'\bWe follow\b', 'This study follows'),
    (r'\bwe follow\b', 'this study follows'),
    (r'\bWe augment\b', 'This study augments'),
    (r'\bwe augment\b', 'this study augments'),
    (r'\bWe anchor\b', 'This study anchors'),
    (r'\bwe anchor\b', 'this study anchors'),
    (r'\bWe read\b', 'This study reads'),
    (r'\bwe read\b', 'this study reads'),
    (r'\bWe disclose\b', 'This study discloses'),
    (r'\bwe disclose\b', 'this study discloses'),
    (r'\bWe also\b', 'This study also'),
    (r'\bwe also\b', 'this study also'),
    (r'\bWe make\b', 'This study makes'),
    (r'\bwe make\b', 'this study makes'),
    (r'\bWe frame\b', 'This study frames'),
    (r'\bwe frame\b', 'this study frames'),
    (r'\bWe include\b', 'This study includes'),
    (r'\bwe include\b', 'this study includes'),
    (r'\bWe exclude\b', 'This study excludes'),
    (r'\bwe exclude\b', 'this study excludes'),
    (r'\bWe return\b', 'This study returns'),
    (r'\bwe return\b', 'this study returns'),
    (r'\bWe record\b', 'This study records'),
    (r'\bwe record\b', 'this study records'),
    (r'\bWe re-fit\b', 'The analysis re-fits'),
    (r'\bwe re-fit\b', 'the analysis re-fits'),
    (r'\bWe therefore\b', 'This study therefore'),
    (r'\bwe therefore\b', 'this study therefore'),
    (r'\bour own\b', "the present study's own"),
    (r'\bOur own\b', "The present study's own"),
    (r'\bour largest\b', 'the largest'),
    (r'\bOur largest\b', 'The largest'),
    (r'\bour substantive\b', 'the substantive'),
    (r'\bOur substantive\b', 'The substantive'),
    (r'\bour earlier\b', 'the earlier'),
    (r'\bOur earlier\b', 'The earlier'),
    (r'\bour discussion\b', 'the discussion'),
    (r'\bOur discussion\b', 'The discussion'),
    # "Our contribution(s)" → "The contribution(s)"
    (r'\bOur contributions are\b', 'The contributions of this study are'),
    (r'\bour contributions are\b', 'the contributions of this study are'),
    (r'\bOur contribution\b', 'The contribution of this study'),
    (r'\bour contribution\b', 'the contribution of this study'),
    (r'\bOur central\b', 'The central'),
    (r'\bour central\b', 'the central'),
    (r'\bOur DAI\b', 'The DAI'),
    (r'\bour DAI\b', 'the DAI'),
    (r'\bour TCI\b', 'the TCI'),
    (r'\bOur TCI\b', 'The TCI'),
    (r'\bour empirical\b', 'the present empirical'),
    (r'\bOur empirical\b', 'The present empirical'),
    (r'\bour design\b', 'the present design'),
    (r'\bOur design\b', 'The present design'),
    # "our" → "the present" / "this study's"
    (r'\bour analysis\b', 'the present analysis'),
    (r'\bOur analysis\b', 'The present analysis'),
    (r'\bour findings\b', 'the present findings'),
    (r'\bOur findings\b', 'The present findings'),
    (r'\bour study\b', 'this study'),
    (r'\bOur study\b', 'This study'),
    (r'\bour results\b', 'the results'),
    (r'\bOur results\b', 'The results'),
    (r'\bour estimation\b', 'the present estimation'),
    (r'\bOur estimation\b', 'The present estimation'),
    (r'\bour interpretation\b', 'the present interpretation'),
    (r'\bOur interpretation\b', 'The present interpretation'),
    (r'\bour model\b', 'the model'),
    (r'\bOur model\b', 'The model'),
    (r'\bour specification\b', 'the specification'),
    (r'\bOur specification\b', 'The specification'),
    (r'\bour sample\b', 'the sample'),
    (r'\bOur sample\b', 'The sample'),
    (r'\bour paper\b', 'this paper'),
    (r'\bOur paper\b', 'This paper'),
    (r'\bour finding\b', 'the present finding'),
    (r'\bOur finding\b', 'The present finding'),
    (r'\bour data\b', 'the data'),
    (r'\bOur data\b', 'The data'),
    (r'\bour focal\b', 'the focal'),
    (r'\bOur focal\b', 'The focal'),
    (r'\bour primary\b', 'the primary'),
    (r'\bOur primary\b', 'The primary'),
    (r'\bour cross-wave\b', 'the cross-wave'),
    (r'\bOur cross-wave\b', 'The cross-wave'),
    # Recursive hedging
    (r'what we believe to be the\b', 'the'),
    (r'What we believe to be the\b', 'The'),
    (r'to our knowledge,\s*', ''),
    (r'To our knowledge,\s*', ''),
    (r"to the authors' knowledge,\s*", ''),
    (r"To the authors' knowledge,\s*", ''),
]

NEGATIVE_PARALLELISM = [
    (r'\bnot only ([\w\s,]+?) but also\b', r'both \1 and'),
    (r'\bNot only ([\w\s,]+?) but also\b', r'Both \1 and'),
    (r'\bnot merely shift it\b', 'rather than relocate it'),
    (r'\bnot merely shifted\b', 'rather than relocated'),
    (r'\bnot just\s', 'beyond '),
]

COPULA_FIXES = [
    # "represents a" overuse — context-sensitive, only fix obvious ones
    (r'This represents a ', 'This is a '),
    (r'this represents a ', 'this is a '),
    # "operates as a level-shifter" is technical idiom — keep
    # "serves as" → "is"
    (r'\bserves as a\b', 'is a'),
    (r'\bServes as a\b', 'Is a'),
]

PERSUASIVE_AUTHORITY = [
    (r'\bfundamentally different\b', 'distinct'),
    (r'\bAt its core,\s*', ''),
    (r'\bat its core,\s*', ''),
    (r'\bIn reality,\s*', ''),
    (r'\bin reality,\s*', ''),
    (r'\bThe real question is\b', 'The question is'),
    (r'\bthe real question is\b', 'the question is'),
]

FILLER_PHRASES = [
    (r'\bIn order to\b', 'To'),
    (r'\bin order to\b', 'to'),
    (r'\bDue to the fact that\b', 'Because'),
    (r'\bdue to the fact that\b', 'because'),
    (r'\bIt is important to note that\b', ''),
    (r'\bIt should be noted that\b', ''),
    (r'\bIt is worth noting that\b', ''),
    (r'\bAt this point in time\b', 'Now'),
    (r'\bat this point in time\b', 'now'),
    (r'\bhas the ability to\b', 'can'),
    (r'\bHas the ability to\b', 'Can'),
]


def is_in_reference(line: str) -> bool:
    """Detect if line is inside References / Bibliography section."""
    return False  # handled in apply_em_dash by paragraph context


def is_in_title_quote(text: str, position: int) -> bool:
    """Check if position is inside a quoted title (Harvard reference)."""
    # Look 100 chars before to find opening quote
    before = text[max(0, position - 200):position]
    # Count straight quotes
    open_quotes = before.count('"') - before.count('""')
    return open_quotes % 2 == 1


def remove_em_dashes(text: str) -> tuple[str, int]:
    """
    Remove prose em-dashes while preserving:
    - Em-dashes inside published titles (within quotes)
    - Em-dashes in figure/table captions
    - En-dashes (–) in ranges
    """
    count = 0
    result = []
    in_references = False
    in_code_block = False

    lines = text.split('\n')
    for i, line in enumerate(lines):
        # Detect References section start
        if re.match(r'^##+\s*References\b', line):
            in_references = True
        elif re.match(r'^##+ ', line) and in_references:
            # Next section after References
            in_references = False

        # Skip code blocks
        if line.startswith('```'):
            in_code_block = not in_code_block
        if in_code_block:
            result.append(line)
            continue

        # Skip table/figure caption lines (Figure X., Table X., Source:)
        if re.match(r'^\s*(Figure|Table|Source:|\*Figure|\*Table|\*Source)', line, re.IGNORECASE):
            result.append(line)
            continue

        # Skip lines that are entirely heading
        if line.startswith('#'):
            result.append(line)
            continue

        # If in references, preserve em-dashes inside quoted titles
        if in_references:
            # Only replace em-dashes OUTSIDE quoted titles
            new_line = ""
            j = 0
            in_quote = False
            while j < len(line):
                c = line[j]
                if c == '"':
                    in_quote = not in_quote
                if c == '—' and not in_quote:
                    # Replace with comma
                    new_line += ','
                    count += 1
                else:
                    new_line += c
                j += 1
            result.append(new_line)
            continue

        # Prose lines: replace em-dash with comma
        # Pattern: spaced em-dash " — " → ", "
        new_line = line
        spaced_count = new_line.count(' — ')
        new_line = new_line.replace(' — ', ', ')
        count += spaced_count
        # Unspaced em-dash "—" → ", " (rare in our manuscripts)
        unspaced_count = new_line.count('—')
        new_line = new_line.replace('—', ', ')
        count += unspaced_count

        result.append(new_line)

    return '\n'.join(result), count


def apply_pattern_replacements(text: str, patterns: list[tuple[str, str]]) -> tuple[str, int]:
    """Apply regex substitutions, return (text, total_replacements)."""
    count = 0
    for pat, repl in patterns:
        new_text, n = re.subn(pat, repl, text)
        if n > 0:
            count += n
            text = new_text
    return text, count


def remove_mid_sentence_boldface(text: str) -> tuple[str, int]:
    """
    Remove **boldface** that's mid-sentence (not legitimate label).
    Legitimate: H1/H2/H3 hypothesis labels, (R1)/(R2) spec labels,
    section-emphasis sub-headers (end with period), Abstract structured
    labels (Purpose./Findings./etc.), [Insert ...] markers.
    """
    count = 0
    legit_patterns = [
        r'^Purpose\.?$', r'^Findings\.?$', r'^Design/methodology/approach\.?$',
        r'^Research limitations/implications\.?$', r'^Practical implications\.?$',
        r'^Social implications\.?$', r'^Originality/value\.?$',
        r'^Keywords:?$', r'^JEL classification:?$', r'^Paper type:?$',
        r'^Manuscript classification:?$',
        r'^H(ypothesis )?\d[ab]?\b',
        r'^\(R\d',
        r'^\[Insert',
        # Section emphasis sub-headers (end with period, short)
        r'^.{1,80}\.$',
    ]
    legit_re = re.compile('|'.join(legit_patterns))

    def fix_bold(m: re.Match) -> str:
        nonlocal count
        inner = m.group(1)
        if legit_re.match(inner):
            return m.group(0)  # keep
        count += 1
        return inner  # strip ** markers

    new_text = re.sub(r'\*\*([^*]+?)\*\*', fix_bold, text)
    return new_text, count


# ============================================================
# MAIN PROCESSING
# ============================================================

def humanize_file(path: Path, dry_run: bool = False) -> dict:
    """Apply humanization to a single manuscript file."""
    text = path.read_text()
    original = text
    stats = {
        "file": str(path.relative_to(ROOT)),
        "original_words": len(text.split()),
        "original_em_dashes": text.count(' — '),
        "original_we_our": len(re.findall(r"\b(we|our|We|Our)\b", text)),
    }

    # 1. We/Our replacements (but skip Acknowledgements + Disclaimer sections)
    # Find boundaries of Acknowledgements section
    ack_match = re.search(r'^## Acknowledgements?\s*$', text, re.MULTILINE)
    cof_match = re.search(r'^## Conflict of Interest\s*$', text, re.MULTILINE | re.IGNORECASE)
    da_match = re.search(r'^## Data availability', text, re.MULTILINE | re.IGNORECASE)
    ai_match = re.search(r'^## Use of [Gg]enerative', text, re.MULTILINE)
    refs_match = re.search(r'^## References\s*$', text, re.MULTILINE)

    # Apply we/our replacements only to main body (before Acknowledgements)
    if ack_match:
        body_end = ack_match.start()
        body = text[:body_end]
        rest = text[body_end:]
        body, n_we = apply_pattern_replacements(body, WE_OUR_REPLACEMENTS)
        text = body + rest
    else:
        text, n_we = apply_pattern_replacements(text, WE_OUR_REPLACEMENTS)
    stats["we_our_replaced"] = n_we

    # 2. Negative parallelism
    text, n_neg = apply_pattern_replacements(text, NEGATIVE_PARALLELISM)
    stats["negative_parallelism_fixed"] = n_neg

    # 3. Copula avoidance
    text, n_cop = apply_pattern_replacements(text, COPULA_FIXES)
    stats["copula_fixed"] = n_cop

    # 4. Persuasive authority
    text, n_pa = apply_pattern_replacements(text, PERSUASIVE_AUTHORITY)
    stats["persuasive_authority_fixed"] = n_pa

    # 5. Filler phrases
    text, n_fp = apply_pattern_replacements(text, FILLER_PHRASES)
    stats["filler_phrases_fixed"] = n_fp

    # 6. Em-dash removal
    text, n_em = remove_em_dashes(text)
    stats["em_dashes_removed"] = n_em

    # 7. Mid-sentence boldface DISABLED in batch mode
    # (Per-paper boldface audit required; batch stripping too aggressive,
    # would damage author names, model labels M0/M1, table cell content,
    # research question labels, figure callouts. Manual review per paper.)
    stats["boldface_stripped"] = 0

    # Cleanup: collapse double spaces, fix punctuation around removed text
    text = re.sub(r'  +', ' ', text)
    text = re.sub(r' ,', ',', text)
    text = re.sub(r' \.', '.', text)
    text = re.sub(r',,+', ',', text)

    stats["final_words"] = len(text.split())
    stats["final_em_dashes"] = text.count(' — ')
    stats["final_we_our"] = len(re.findall(r"\b(we|our|We|Our)\b", text))
    stats["text_changed"] = (text != original)

    if not dry_run and stats["text_changed"]:
        path.write_text(text)

    return stats


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True,
                        choices=list(PAPERS.keys()) + ["all"])
    parser.add_argument("--dry-run", action="store_true",
                        help="Report changes without writing")
    args = parser.parse_args()

    targets = list(PAPERS.keys()) if args.paper == "all" else [args.paper]

    print(f"{'=' * 76}")
    print(f"  Portfolio humanization {'(DRY RUN)' if args.dry_run else ''}")
    print(f"{'=' * 76}")

    all_stats = []
    for p in targets:
        path = ROOT / PAPERS[p]
        if not path.exists():
            print(f"\n  ⚠ Skip {p}: {path} not found")
            continue
        print(f"\n→ {p}: {PAPERS[p]}")
        stats = humanize_file(path, dry_run=args.dry_run)
        all_stats.append(stats)
        print(f"   Words:    {stats['original_words']:,} → {stats['final_words']:,}")
        print(f"   Em-dash:  {stats['original_em_dashes']} → {stats['final_em_dashes']}")
        print(f"   we/our:   {stats['original_we_our']} → {stats['final_we_our']}")
        print(f"   Replacements: we/our={stats['we_our_replaced']}, neg={stats['negative_parallelism_fixed']}, copula={stats['copula_fixed']}, pers-auth={stats['persuasive_authority_fixed']}, filler={stats['filler_phrases_fixed']}, em-dash={stats['em_dashes_removed']}, bold={stats['boldface_stripped']}")
        print(f"   Modified: {stats['text_changed']}")

    print(f"\n{'=' * 76}")
    print(f"  Summary: {len(all_stats)} paper(s) processed")
    print(f"{'=' * 76}")
    total_em = sum(s["original_em_dashes"] - s["final_em_dashes"] for s in all_stats)
    total_we = sum(s["original_we_our"] - s["final_we_our"] for s in all_stats)
    print(f"  Total em-dashes removed: {total_em}")
    print(f"  Total we/our eliminated: {total_we}")


if __name__ == "__main__":
    main()

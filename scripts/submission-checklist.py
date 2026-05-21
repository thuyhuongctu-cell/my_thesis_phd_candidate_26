#!/usr/bin/env python3
"""
submission-checklist.py — validate academic manuscripts against journal
submission requirements before submission.

Implements the spec from .claude/skills/academic-manuscript-submission-checker
(see /tmp/skills_extract/academicmanuscriptsubmissionchecker/SKILL.md).

Checks: word count main text, abstract structure & length, keyword count,
blind review (regex scan for author / institution identifiers), section
presence, reference count, data availability statement.

Usage:
    python3 scripts/submission-checklist.py \
        --manuscript manuscripts/p3_vietnam_en_clean.md --journal APJM

Exit code: 0 if all required checks pass (warnings allowed), 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import sys
from dataclasses import dataclass, field
from pathlib import Path


# ----------------------------------------------------------------------------
# Journal profiles
# ----------------------------------------------------------------------------

@dataclass
class JournalProfile:
    name: str
    main_word_min: int
    main_word_max: int
    abstract_word_min: int
    abstract_word_max: int
    keyword_min: int
    keyword_max: int
    blind_review: bool
    require_data_availability: bool
    abstract_structured: bool = False  # Purpose / Design / Findings / Originality
    require_jel: bool = False
    notes: str = ""


PROFILES: dict[str, JournalProfile] = {
    "APJM": JournalProfile(
        name="Asia Pacific Journal of Management",
        main_word_min=6000,
        main_word_max=12000,
        abstract_word_min=150,
        abstract_word_max=250,
        keyword_min=4,
        keyword_max=6,
        blind_review=True,
        require_data_availability=False,  # Springer encourages, not required
        notes="Self-cites should be anonymised as 'Author Citation'.",
    ),
    "MIR": JournalProfile(
        name="Management International Review",
        main_word_min=5000,
        main_word_max=10000,
        abstract_word_min=120,
        abstract_word_max=200,
        keyword_min=4,
        keyword_max=6,
        blind_review=True,
        require_data_availability=False,
        require_jel=True,
        notes="JEL classification codes recommended.",
    ),
    "IJOEM": JournalProfile(
        name="International Journal of Emerging Markets",
        main_word_min=4000,
        main_word_max=8000,
        abstract_word_min=150,
        abstract_word_max=250,
        keyword_min=4,
        keyword_max=8,
        blind_review=True,
        require_data_availability=True,
        abstract_structured=True,  # Emerald structured abstract
    ),
    "JIBS": JournalProfile(
        name="Journal of International Business Studies",
        main_word_min=8000,
        main_word_max=14000,
        abstract_word_min=150,
        abstract_word_max=250,
        keyword_min=4,
        keyword_max=6,
        blind_review=True,
        require_data_availability=True,
    ),
    "GSJ": JournalProfile(
        name="Global Strategy Journal",
        main_word_min=6000,
        main_word_max=12000,
        abstract_word_min=150,
        abstract_word_max=200,
        keyword_min=4,
        keyword_max=6,
        blind_review=True,
        require_data_availability=False,
    ),
}


# Blind-review leak patterns. Whitelist tokens are matched against the same
# regex and excluded from the leak count.
BLIND_PATTERNS = [
    r"Phan Anh Tu",
    r"Do Thuy Huong",
    r"Đỗ Thúy Hương",
    r"thuyhuongctu",
    r"Can Tho University",
    r"Đại học Cần Thơ",
    r"huongctu",
    r"Class-AI-Agent",
]
BLIND_WHITELIST = [
    "Author Citation",
    "Author details withheld",
    "Publisher details withheld",
]


@dataclass
class CheckResult:
    name: str
    status: str  # "PASS", "WARN", "FAIL"
    detail: str = ""


@dataclass
class Report:
    manuscript: Path
    journal: JournalProfile
    results: list[CheckResult] = field(default_factory=list)

    def add(self, name: str, status: str, detail: str = ""):
        self.results.append(CheckResult(name, status, detail))

    def has_failures(self) -> bool:
        return any(r.status == "FAIL" for r in self.results)

    def render(self) -> str:
        lines = [
            f"\n=== Submission readiness — {self.manuscript.name} -> {self.journal.name} ===\n"
        ]
        for r in self.results:
            mark = {"PASS": "✓", "WARN": "⚠", "FAIL": "✗"}[r.status]
            line = f"  [{mark}] {r.name}"
            if r.detail:
                line += f" — {r.detail}"
            lines.append(line)
        n_pass = sum(1 for r in self.results if r.status == "PASS")
        n_warn = sum(1 for r in self.results if r.status == "WARN")
        n_fail = sum(1 for r in self.results if r.status == "FAIL")
        lines.append(
            f"\n  Summary: {n_pass} pass / {n_warn} warn / {n_fail} fail"
        )
        return "\n".join(lines)


# ----------------------------------------------------------------------------
# Section extraction helpers
# ----------------------------------------------------------------------------

SECTION_RE = re.compile(r"^(#{1,6})\s+(.+?)\s*$", re.MULTILINE)


def find_section(text: str, names: list[str]) -> tuple[int, int] | None:
    """Find the first section whose heading contains any of `names`.

    Returns (start, end) byte offsets where end is the next heading at the
    same level or shallower.
    """
    matches = list(SECTION_RE.finditer(text))
    for i, m in enumerate(matches):
        title = m.group(2).strip().lower()
        if any(n.lower() in title for n in names):
            level = len(m.group(1))
            # find end: next heading with level <= current
            end = len(text)
            for n in matches[i + 1 :]:
                if len(n.group(1)) <= level:
                    end = n.start()
                    break
            return m.end(), end
    return None


def word_count(text: str) -> int:
    return len(text.split())


def count_words_excluding_tables(text: str) -> int:
    """Word count excluding markdown table rows (lines starting with `|`)."""
    lines = [ln for ln in text.split("\n") if not ln.lstrip().startswith("|")]
    return word_count("\n".join(lines))


# ----------------------------------------------------------------------------
# Checks
# ----------------------------------------------------------------------------

def check_section_presence(text: str, report: Report) -> None:
    required = [
        ("Abstract", ["abstract"]),
        ("Introduction", ["introduction", "1. introduction"]),
        ("Methods/Data", ["methods", "method", "data and methods", "data, variables"]),
        ("Results", ["results"]),
        ("Discussion", ["discussion"]),
        ("References", ["references"]),
    ]
    for label, aliases in required:
        present = find_section(text, aliases) is not None
        report.add(
            f"Section: {label}",
            "PASS" if present else "FAIL",
            "" if present else f"no heading matching {aliases}",
        )


def check_word_count(text: str, report: Report, profile: JournalProfile) -> None:
    ref_section = find_section(text, ["references"])
    if ref_section is None:
        main_text = text
    else:
        main_text = text[: ref_section[0] - len("\n## References\n")]

    # Exclude abstract from main text count (journal convention)
    abs_section = find_section(main_text, ["abstract"])
    if abs_section:
        # main text starts after the abstract section ends
        main_text = main_text[abs_section[1]:]

    n_words = count_words_excluding_tables(main_text)
    if profile.main_word_min <= n_words <= profile.main_word_max:
        status = "PASS"
    elif n_words < profile.main_word_min:
        status = "WARN"
    else:
        status = "FAIL" if n_words > profile.main_word_max * 1.15 else "WARN"
    report.add(
        "Main-text word count",
        status,
        f"{n_words:,} words (target {profile.main_word_min:,}–{profile.main_word_max:,})",
    )


def check_abstract(text: str, report: Report, profile: JournalProfile) -> None:
    sec = find_section(text, ["abstract"])
    if sec is None:
        report.add("Abstract length", "FAIL", "no Abstract section")
        return
    abstract_text = text[sec[0]:sec[1]]
    n_words = word_count(abstract_text)
    if profile.abstract_word_min <= n_words <= profile.abstract_word_max:
        status = "PASS"
    elif n_words < profile.abstract_word_min:
        status = "WARN"
    else:
        status = "WARN"
    report.add(
        "Abstract word count",
        status,
        f"{n_words} words (target {profile.abstract_word_min}–{profile.abstract_word_max})",
    )

    if profile.abstract_structured:
        required_labels = ["purpose", "design", "findings", "originality"]
        lower = abstract_text.lower()
        missing = [lab for lab in required_labels if lab not in lower]
        if missing:
            report.add(
                "Abstract structure (Emerald)",
                "WARN",
                f"missing labels: {', '.join(missing)}",
            )
        else:
            report.add("Abstract structure (Emerald)", "PASS")


def check_keywords(text: str, report: Report, profile: JournalProfile) -> None:
    # Look for "Keywords:" or "**Keywords**" line
    m = re.search(r"(?:^|\n)\s*\**Keywords?\**\s*[:：]\s*(.+)", text, re.IGNORECASE)
    if not m:
        report.add("Keywords presence", "FAIL", "no Keywords: line found")
        return
    kw_line = m.group(1).split("\n")[0]
    # Split on comma, semicolon, or bullet
    parts = [p.strip() for p in re.split(r"[,;•]", kw_line) if p.strip()]
    parts = [re.sub(r"[*_]", "", p) for p in parts]  # strip markdown
    n = len(parts)
    if profile.keyword_min <= n <= profile.keyword_max:
        status = "PASS"
    else:
        status = "WARN"
    report.add(
        "Keyword count",
        status,
        f"{n} keywords (target {profile.keyword_min}–{profile.keyword_max})",
    )


def check_blind_review(text: str, report: Report, profile: JournalProfile) -> None:
    if not profile.blind_review:
        report.add("Blind-review compliance", "PASS", "journal does not require")
        return

    leaks: list[str] = []
    for pat in BLIND_PATTERNS:
        for m in re.finditer(pat, text):
            start = max(0, m.start() - 40)
            end = min(len(text), m.end() + 40)
            context = text[start:end].replace("\n", " ")
            # whitelist check
            if any(w in context for w in BLIND_WHITELIST):
                continue
            leaks.append(f"{pat}: ...{context}...")
            if len(leaks) >= 5:
                break
    if leaks:
        report.add(
            "Blind-review compliance",
            "FAIL",
            f"{len(leaks)} potential leak(s); first: {leaks[0][:140]}",
        )
    else:
        report.add("Blind-review compliance", "PASS")


def check_references(text: str, report: Report) -> None:
    sec = find_section(text, ["references"])
    if sec is None:
        report.add("References section", "FAIL", "no References section")
        return
    ref_text = text[sec[0]:sec[1]]
    # Count entries by looking for lines starting with a capital letter and
    # containing a (YYYY) pattern.
    entries = re.findall(r"^[A-Z][^\n]*\((?:19|20)\d{2}", ref_text, re.MULTILINE)
    n = len(entries)
    if n < 5:
        report.add("Reference count", "FAIL", f"only {n} entries (expect >=5)")
    elif n < 15:
        report.add("Reference count", "WARN", f"{n} entries (typical paper has 20+)")
    else:
        report.add("Reference count", "PASS", f"{n} entries")


def check_data_availability(text: str, report: Report, profile: JournalProfile) -> None:
    has_statement = bool(
        re.search(
            r"data\s+availability|publicly\s+available|enterprisesurveys\.org|"
            r"available\s+upon\s+request|replication\s+package",
            text,
            re.IGNORECASE,
        )
    )
    if profile.require_data_availability:
        report.add(
            "Data availability statement",
            "PASS" if has_statement else "FAIL",
            "" if has_statement else "required by journal but not found",
        )
    else:
        report.add(
            "Data availability statement",
            "PASS" if has_statement else "WARN",
            "" if has_statement else "encouraged but not required",
        )


def check_jel(text: str, report: Report, profile: JournalProfile) -> None:
    if not profile.require_jel:
        return
    has_jel = bool(re.search(r"\bJEL\b.{0,20}[:：]", text))
    report.add(
        "JEL classification",
        "PASS" if has_jel else "WARN",
        "" if has_jel else "JEL codes recommended for this journal",
    )


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manuscript", required=True, type=Path)
    p.add_argument(
        "--journal",
        required=True,
        choices=sorted(PROFILES.keys()),
        help="Target journal code (APJM, MIR, IJOEM, JIBS, GSJ)",
    )
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Suppress per-check output, only print summary line",
    )
    args = p.parse_args(argv)

    if not args.manuscript.is_file():
        print(f"error: file not found: {args.manuscript}", file=sys.stderr)
        return 2

    text = args.manuscript.read_text(encoding="utf-8")
    profile = PROFILES[args.journal]
    report = Report(manuscript=args.manuscript, journal=profile)

    check_section_presence(text, report)
    check_word_count(text, report, profile)
    check_abstract(text, report, profile)
    check_keywords(text, report, profile)
    check_blind_review(text, report, profile)
    check_references(text, report)
    check_data_availability(text, report, profile)
    check_jel(text, report, profile)

    if not args.quiet:
        print(report.render())
    else:
        n_pass = sum(1 for r in report.results if r.status == "PASS")
        n_warn = sum(1 for r in report.results if r.status == "WARN")
        n_fail = sum(1 for r in report.results if r.status == "FAIL")
        print(
            f"{args.manuscript.name} -> {profile.name}: "
            f"{n_pass} pass / {n_warn} warn / {n_fail} fail"
        )

    return 1 if report.has_failures() else 0


if __name__ == "__main__":
    sys.exit(main())

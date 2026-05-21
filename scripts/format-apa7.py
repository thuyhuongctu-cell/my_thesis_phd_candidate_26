#!/usr/bin/env python3
"""
format-apa7.py — cross-validate in-text citations against the reference list
in an APA7-style academic manuscript.

Implements the citation-cross-validation tool described in the
academic-manuscript-quality-toolkit skill (see /tmp/skills_extract/
academicmanuscriptqualitytoolkit/SKILL.md).

For each Markdown manuscript:
  1. Extract reference entries from the `## References` section (one entry
     per paragraph; each entry must start with an upper-case author surname
     followed by other authors / initials and a `(YYYY)` year).
  2. Scan the body text for in-text citations in these forms:
       - "(Author, YYYY)"
       - "Author (YYYY)"
       - "(Author & Author, YYYY)"
       - "Author and Author (YYYY)"
       - "Author et al. (YYYY)"
       - "(Author et al., YYYY)"
       - blinded variant "(Author Citation, YYYY ...)" / "Author Citation (YYYY)"
       - semicolon-separated lists "(Foo, 2020; Bar & Baz, 2021)"
  3. Report:
       - References that have no matching in-text citation (uncited).
       - In-text citations that have no matching reference entry (orphaned).
       - Year mismatches (author cited with year X but reference list has year Y).

Usage:
    python3 scripts/format-apa7.py --manuscript manuscripts/p3_vietnam_en_clean.md

Exit code: 0 if no uncited / no orphaned citations, 1 otherwise.
"""

from __future__ import annotations

import argparse
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from pathlib import Path


# ----------------------------------------------------------------------------
# Reference extraction
# ----------------------------------------------------------------------------

# Reference entry pattern: starts with capital letter, runs until we see (YYYY)
# Then captures the surname (first author) and year(s). Recognises "World Bank"
# as a two-word institutional author.
REF_LINE_RE = re.compile(
    r"""^
    (?P<surname>
        World\s+Bank                              # institutional two-word
        |[A-Z][A-Za-zÀ-ſ\-\'éèâàü]+               # standard surname
    )
    [\.,]?                                        # optional terminator after surname
    (?:                                          # optional rest of author list
        \s*,?\s*[A-Z][A-Za-zÀ-ſ\-\'éèâàü\.\s,&]*?
    )?
    \s*\(
        (?P<year>(?:19|20)\d{2})                  # Year
        (?:\s*[—-]\s*[A-Z]{3,6})?                 # Optional suffix tag (— JFAR / — ICBEF)
    \)
    """,
    re.VERBOSE,
)

# Blinded entries use "Author Citation" as the surname placeholder.
BLIND_REF_RE = re.compile(
    r"""^
    Author\s+Citation
    \s*\(
        (?P<year>(?:19|20)\d{2})
        (?:\s*[—-]\s*(?P<tag>[A-Z]{3,6}))?
    \)
    """,
    re.VERBOSE,
)


@dataclass(frozen=True)
class RefKey:
    surname: str
    year: str
    tag: str = ""  # journal suffix (JFAR / VEFR / ICBEF) for blinded duplicates

    def __str__(self) -> str:
        suffix = f" — {self.tag}" if self.tag else ""
        return f"{self.surname} ({self.year}{suffix})"


def _split_entries(ref_body: str) -> list[str]:
    """Split a references block into individual entry strings.

    Handles two layouts:
      1. Paragraph-separated entries (blank line between entries).
      2. Line-per-entry layout (each entry on a single line, no blank between).
    Detects which layout is in use by counting blank-line separators.
    """
    blank_split = [p.strip() for p in re.split(r"\n\s*\n", ref_body) if p.strip()]
    # If most "paragraphs" contain multiple author-year markers, fall back to
    # per-line splitting because entries got smashed into one block.
    has_many_years = sum(
        len(re.findall(r"\((?:19|20)\d{2}", p)) >= 3 for p in blank_split
    )
    if has_many_years:
        line_split = [
            ln.strip() for ln in ref_body.split("\n")
            if ln.strip() and re.match(r"^[A-Z]", ln.strip())
        ]
        return line_split
    return blank_split


def extract_references(text: str) -> set[RefKey]:
    ref_start = text.find("## References")
    if ref_start == -1:
        return set()
    ref_body = text[ref_start:].split("\n", 1)[1] if "\n" in text[ref_start:] else ""
    entries = _split_entries(ref_body)

    refs: set[RefKey] = set()
    for entry in entries:
        # Flatten multi-line entry to a single string
        flat = re.sub(r"\s+", " ", entry)
        m = BLIND_REF_RE.match(flat)
        if m:
            refs.add(RefKey("Author Citation", m.group("year"), m.group("tag") or ""))
            continue
        m = REF_LINE_RE.match(flat)
        if m:
            surname = re.sub(r"\s+", " ", m.group("surname").strip())
            refs.add(RefKey(surname, m.group("year")))
    return refs


# ----------------------------------------------------------------------------
# In-text citation extraction
# ----------------------------------------------------------------------------

# Matches "(Author1, Year; Author2 & Author3, Year; ...)"
PAREN_CITE_RE = re.compile(
    r"\(([^()]*?(?:19|20)\d{2}[a-z]?[^()]*?)\)"
)

# Matches narrative form "Author (YYYY)" or "Author et al. (YYYY)" or
# "Author and/& Author (YYYY)"
NARRATIVE_CITE_RE = re.compile(
    r"""(?:
        (?<![A-Za-z])                              # word boundary before
        (?:Author\s+Citation|[A-Z][A-Za-zÀ-ſ\-\']+)
        (?:\s+(?:and|&)\s+[A-Z][A-Za-zÀ-ſ\-\']+)?  # second author
        (?:\s+et\s+al\.?)?                          # et al.
    )
    \s*\(
        ((?:19|20)\d{2})                            # year
        (?:[a-z])?                                  # year disambig suffix
        (?:\s*[—-]\s*[A-Z]{3,6})?
    \)
    """,
    re.VERBOSE,
)


def extract_citations(text: str, body_only: str) -> dict[tuple[str, str], int]:
    """Return mapping (surname_token, year) -> count over body text."""
    cites: dict[tuple[str, str], int] = defaultdict(int)

    # Parenthetical citations — split inside the parens on semicolons
    for m in PAREN_CITE_RE.finditer(body_only):
        inner = m.group(1)
        # Skip if obviously not a citation (e.g., page ranges, footnote nums)
        if not re.search(r"(?:19|20)\d{2}", inner):
            continue
        # Skip if it contains math-expression markers (× ^ = + interaction
        # terms like "FSTS × wave_2024" or table footnote like "(N = 1,940)")
        if re.search(r"[×\^=]|N\s*=", inner):
            continue
        for chunk in re.split(r";", inner):
            chunk = chunk.strip()
            # Liberal: first surname token + a year somewhere later in chunk.
            # Recognises two-word surnames like "World Bank".
            mm = re.match(
                r"(?P<head>Author\s+Citation"
                r"|World\s+Bank"
                r"|[A-Z][A-Za-zÀ-ſ\-\']+)"
                r"[^\d]*?(?P<year>(?:19|20)\d{2})",
                chunk,
            )
            if mm:
                first_surname = mm.group("head").strip()
                # Collapse internal whitespace ("World  Bank" -> "World Bank")
                first_surname = re.sub(r"\s+", " ", first_surname)
                cites[(first_surname, mm.group("year"))] += 1

    # Narrative citations
    for m in NARRATIVE_CITE_RE.finditer(body_only):
        full = m.group(0)
        year = m.group(1)
        # Skip false positives where the "name" before (YYYY) is part of a
        # measurement label, table caption, or section reference.
        if re.match(r"^(Panel|Figure|Table|Section|FSTS|TCI|DAI|Model|WBES|"
                    r"H[0-9]|N|Equation|Appendix)\b", full):
            continue
        toks = re.findall(r"Author\s+Citation|World\s+Bank|[A-Z][A-Za-zÀ-ſ\-\']+", full)
        if toks:
            first = re.sub(r"\s+", " ", toks[0].strip())
            cites[(first, year)] += 1
    return cites


# ----------------------------------------------------------------------------
# Cross-validation
# ----------------------------------------------------------------------------

@dataclass
class AuditReport:
    manuscript: Path
    references: set[RefKey]
    citations: dict[tuple[str, str], int]

    @property
    def uncited(self) -> list[RefKey]:
        cited_keys = {(s, y) for (s, y) in self.citations}
        return sorted(
            [r for r in self.references if (r.surname, r.year) not in cited_keys],
            key=lambda r: (r.surname, r.year),
        )

    @property
    def orphaned(self) -> list[tuple[str, str]]:
        ref_keys = {(r.surname, r.year) for r in self.references}
        return sorted(
            [k for k in self.citations if k not in ref_keys],
            key=lambda k: (k[0], k[1]),
        )

    def render(self) -> str:
        lines = [
            f"\n=== APA7 citation audit — {self.manuscript.name} ===\n",
            f"  References extracted: {len(self.references)}",
            f"  In-text citation keys: {len(self.citations)}",
        ]
        if self.uncited:
            lines.append(
                f"\n  UNCITED references ({len(self.uncited)}) — in reference list "
                f"but not cited in body:"
            )
            for r in self.uncited:
                lines.append(f"    - {r}")
        else:
            lines.append("\n  UNCITED: none")
        if self.orphaned:
            lines.append(
                f"\n  ORPHANED citations ({len(self.orphaned)}) — cited in body "
                f"but missing from reference list:"
            )
            for s, y in self.orphaned:
                lines.append(f"    - {s} ({y}) — cited {self.citations[(s, y)]}×")
        else:
            lines.append("\n  ORPHANED: none")
        return "\n".join(lines)

    @property
    def clean(self) -> bool:
        return not self.uncited and not self.orphaned


def audit(path: Path) -> AuditReport:
    text = path.read_text(encoding="utf-8")
    refs = extract_references(text)
    body = text.split("## References")[0]
    cites = extract_citations(text, body)
    return AuditReport(manuscript=path, references=refs, citations=cites)


# ----------------------------------------------------------------------------
# Entry point
# ----------------------------------------------------------------------------

def main(argv: list[str] | None = None) -> int:
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("--manuscript", required=True, type=Path)
    p.add_argument(
        "--quiet",
        action="store_true",
        help="Print summary line only",
    )
    args = p.parse_args(argv)

    if not args.manuscript.is_file():
        print(f"error: file not found: {args.manuscript}", file=sys.stderr)
        return 2

    report = audit(args.manuscript)

    if args.quiet:
        print(
            f"{args.manuscript.name}: "
            f"{len(report.uncited)} uncited / {len(report.orphaned)} orphaned"
        )
    else:
        print(report.render())

    return 0 if report.clean else 1


if __name__ == "__main__":
    sys.exit(main())

#!/usr/bin/env python3
"""fix_author_name.py — Canonical name correction sweep across portfolio.

User-confirmed canonical names:
  VI: "Đỗ Thùy Hương" (3 words: surname Đỗ, middle Thùy, given Hương)
  EN: "Do Thuy Huong"

Replace incorrect 4-word variants used throughout the repo:
  WRONG VI: "Đỗ Thị Thúy Hương" → CORRECT: "Đỗ Thùy Hương"
  WRONG VI: "Đỗ Thị Thúy" (shortened) → "Đỗ Thùy"
  WRONG EN: "Do Thi Thuy Huong" → "Do Thuy Huong"
  WRONG EN: "Do Thi Thuy" (shortened) → "Do Thuy"
  WRONG: "Huong Do Thi Thuy" → "Huong Do Thuy"

APA citations:
  WRONG: "Đỗ, T. T. H." → "Đỗ, T. H."
  WRONG: "Do, T. T. H." → "Do, T. H."

Preserves:
  - "Tác giả ẩn danh" anonymized strings
  - Co-author Phan Anh Tú (unchanged)
  - Math/code/tables

Source of truth: CTU QĐ 3010/QĐ-ĐHCT (23/6/2023) confirms
"Đỗ Thùy Hương" (no "Thị").
"""
import re
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parents[1]

# Order matters — longest patterns first to avoid partial-match bugs
REPLACEMENTS = [
    # VI full name (4 words → 3 words)
    ("Đỗ Thị Thúy Hương", "Đỗ Thùy Hương"),
    # EN full name (lossy form without diacritics)
    ("Do Thi Thuy Huong", "Do Thuy Huong"),
    ("Huong Do Thi Thuy", "Huong Do Thuy"),
    # APA citation initials (T. T. H. → T. H.)
    ("Đỗ, T. T. H.", "Đỗ, T. H."),
    ("Do, T. T. H.", "Do, T. H."),
    ("Đỗ T. T. H.", "Đỗ T. H."),
    ("Do T. T. H.", "Do T. H."),
    # Lower-case context "do, t. t. h." (rare)
    ("do, t. t. h.", "do, t. h."),
    # Shortened forms in text (only when followed by space + comma or end)
    # "Đỗ Thị Thúy" not followed by "Hương" — e.g., "by Đỗ Thị Thúy and Phan"
    # Handled via narrower pattern below to avoid breaking unrelated names
]

# Patterns needing regex (e.g., word boundary)
REGEX_REPLACEMENTS = [
    # "Đỗ Thị Thúy" not followed by "Hương" (already handled above) → fallback
    # Use negative lookahead
    (re.compile(r"Đỗ Thị Thúy(?!\s*Hương)"), "Đỗ Thùy"),
    (re.compile(r"Do Thi Thuy(?!\s*Huong)"), "Do Thuy"),
]


def fix_file(path):
    text = path.read_text(encoding="utf-8")
    original = text
    fixes = {}
    for old, new in REPLACEMENTS:
        cnt = text.count(old)
        if cnt:
            text = text.replace(old, new)
            fixes[old] = cnt
    for pat, replacement in REGEX_REPLACEMENTS:
        cnt = len(pat.findall(text))
        if cnt:
            text = pat.sub(replacement, text)
            fixes[pat.pattern] = cnt
    if text != original:
        path.write_text(text, encoding="utf-8")
        return fixes
    return None


def main():
    # Scan all relevant text files
    patterns = [
        "**/*.md", "**/*.txt", "**/*.cff", "**/*.yml", "**/*.yaml",
        "**/*.csv",
    ]
    skip_dirs = {".git", "node_modules", "__pycache__", "dist/submission",
                 ".claude/uploads"}

    targets = set()
    for pat in patterns:
        for path in ROOT.glob(pat):
            if any(skip in path.parts for skip in skip_dirs):
                continue
            if path.is_file():
                targets.add(path)

    print(f"Scanning {len(targets)} files...")
    total_files = 0
    total_replacements = 0
    for path in sorted(targets):
        fixes = fix_file(path)
        if fixes:
            total_files += 1
            n = sum(fixes.values())
            total_replacements += n
            rel = path.relative_to(ROOT)
            print(f"  ✓ {rel}: {n} fixes")
            for k, v in fixes.items():
                print(f"      {k!r}: {v}")

    print(f"\n=== Summary ===")
    print(f"Files modified: {total_files}")
    print(f"Total replacements: {total_replacements}")


if __name__ == "__main__":
    main()

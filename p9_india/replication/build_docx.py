#!/usr/bin/env python3
"""
P9' India — Build submission DOCX via pandoc

Pipeline:
1. Read main manuscript p9_india_en_clean.md
2. Read each table .md file
3. Inline figures + tables at insertion markers
4. Compile to a single source markdown
5. Convert to DOCX via pandoc

Output:
- p9_india/submission/mir_package/01_manuscript_blinded.docx
- p9_india/submission/mir_package/01_manuscript_blinded_full.md  (source build)
"""

from __future__ import annotations
import re
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
P9 = ROOT / "p9_india"
SRC_MD = P9 / "p9_india_en_clean.md"
TABLES_DIR = P9 / "replication" / "tables"
FIGURES_DIR = P9 / "replication" / "figures"
OUT_DIR = P9 / "submission" / "mir_package"
OUT_DIR.mkdir(parents=True, exist_ok=True)

# Insertion mapping (marker pattern → replacement)
INSERTIONS = {
    "[Insert Figure 1 about here.]": [
        ("FIGURE", FIGURES_DIR / "figure_1_conceptual_model.png",
         "Figure 1. Conceptual model: conditional inverted-U with capability moderation under institutional scope condition."),
    ],
    "[Insert Table 1 about here.]": [
        ("TABLE", TABLES_DIR / "table_1_descriptives.md", None),
    ],
    "[Insert Table 2 and Figure 2 about here.]": [
        ("TABLE", TABLES_DIR / "table_2_main_m2.md", None),
        ("FIGURE", FIGURES_DIR / "figure_2_predicted_curves.png",
         "Figure 2. Wave-specific predicted I-P relationship: India 2014, 2022, 2025."),
    ],
    "[Insert Figure 3 about here.]": [
        ("FIGURE", FIGURES_DIR / "figure_3_turning_points.png",
         "Figure 3. Turning-point estimates and 2025 threshold collapse."),
    ],
    "[Insert Table 4 and Figure 4 about here.]": [
        ("TABLE", TABLES_DIR / "table_4_moderators.md", None),
        ("FIGURE", FIGURES_DIR / "figure_4_upi_timeline.png",
         "Figure 4. UPI rollout and Indian institutional shocks, 2014-2025."),
    ],
    "[Insert Table 5 about here.]": [
        ("TABLE", TABLES_DIR / "table_5_robustness.md", None),
    ],
}


def build_replacement(items: list[tuple]) -> str:
    """Build the markdown block that replaces a marker."""
    parts = []
    for kind, path, caption in items:
        if kind == "FIGURE":
            # Pandoc markdown image: ![caption](path)
            rel_path = path.resolve()
            parts.append(f"\n![{caption}]({rel_path}){{width=6.5in}}\n")
        elif kind == "TABLE":
            content = path.read_text().strip()
            parts.append(f"\n{content}\n")
    return "\n".join(parts)


def main():
    src = SRC_MD.read_text()
    print(f"Source manuscript: {len(src.split())} words, {len(src)} chars")

    # Apply insertions
    replaced_count = 0
    for marker, items in INSERTIONS.items():
        marker_bold = f"**{marker}**"
        replacement = build_replacement(items)
        if marker_bold in src:
            src = src.replace(marker_bold, replacement)
            replaced_count += 1
            print(f"  ✓ Inserted: {marker}")
        elif marker in src:
            src = src.replace(marker, replacement)
            replaced_count += 1
            print(f"  ✓ Inserted (no bold): {marker}")
        else:
            print(f"  ⚠ Marker not found: {marker}")

    print(f"\n{replaced_count} of {len(INSERTIONS)} markers replaced.")

    # Write source build (markdown with inlined content)
    full_md = OUT_DIR / "01_manuscript_blinded_full.md"
    full_md.write_text(src)
    print(f"\nSource build → {full_md}")

    # Convert to DOCX via pandoc
    docx_path = OUT_DIR / "01_manuscript_blinded.docx"
    print(f"\nRunning pandoc → {docx_path}")
    cmd = [
        "pandoc",
        str(full_md),
        "-o", str(docx_path),
        "--standalone",
        "--from", "markdown+pipe_tables+tex_math_dollars+raw_html",
        "--to", "docx",
        "--toc",
        "--toc-depth=2",
    ]

    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        size_kb = docx_path.stat().st_size / 1024
        print(f"\n✓ DOCX built successfully: {docx_path} ({size_kb:.0f} KB)")
    else:
        print(f"\n✗ Pandoc failed:")
        print(result.stderr)
        return 1

    return 0


if __name__ == "__main__":
    raise SystemExit(main())

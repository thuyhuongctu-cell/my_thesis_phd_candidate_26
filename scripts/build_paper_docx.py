#!/usr/bin/env python3
"""
Generic pandoc DOCX builder for portfolio papers.

Usage:
    python3 scripts/build_paper_docx.py --paper p5
    python3 scripts/build_paper_docx.py --paper all
"""
from __future__ import annotations
import argparse
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

# Map: paper → (manuscript path, output DOCX path)
PAPERS = {
    "p3": ("p3/p3_vietnam_en_clean.md",   "p3/submission/jed_package/01_manuscript_blinded.docx"),
    "p4": ("p4/p4_singapore_en_clean.md", "p4/submission/jabes_package/01_manuscript_blinded.docx"),
    "p5": ("p5/p5_china_en_clean.md",     "p5/submission/ijoem_package/01_manuscript_blinded.docx"),
    "p6": ("p6/p6_meta_manuscript_en.md", "p6/submission/mir_package/01_manuscript_blinded.docx"),
    "p7": ("p7/p7_capstone_en_clean.md",  "p7/submission/jibs_package/01_manuscript_blinded.docx"),
    "p8": ("p8/p8_pacific_sids_en_clean.md","p8/submission/jed_package/01_manuscript_blinded.docx"),
    "p9_india": ("p9_india/p9_india_en_clean.md","p9_india/submission/mir_package/01_manuscript_blinded.docx"),
}


def build_one(paper: str) -> bool:
    src_rel, out_rel = PAPERS[paper]
    src = ROOT / src_rel
    out = ROOT / out_rel
    resource = ROOT / paper.split("_")[0]  # p5 root for p5; p9_india root for p9_india

    if paper.startswith("p9_india"):
        resource = ROOT / "p9_india"
    else:
        resource = ROOT / paper

    print(f"\n→ {paper}: {src_rel}")
    if not src.exists():
        print(f"   ⚠ Source not found: {src}")
        return False

    # Preprocess: --- → *** to avoid YAML interpretation
    text = src.read_text(encoding="utf-8")
    lines = text.splitlines()
    pre_lines = []
    stripped_blind = 0
    for l in lines:
        # Blind-redaction: drop lines that bear author-identifier patterns.
        # Matches lines containing email-like patterns + ORCID or affiliation
        # markers. Keeps the line if it is only a title or a section header.
        lower = l.lower()
        is_author_block_line = (
            ("orcid:" in lower)
            or ("@" in l and ("university" in lower or "school of" in lower or "viện" in lower))
            or l.strip().startswith("**Do Thuy Huong**")
            or l.strip().startswith("**Phan Anh Tu**")
            or l.strip().startswith("**Đỗ Thùy Hương**")
            or l.strip().startswith("**Phan Anh Tú**")
        )
        if is_author_block_line:
            stripped_blind += 1
            continue
        pre_lines.append("***" if l.strip() == "---" else l)
    if stripped_blind:
        print(f"   ↪ Stripped {stripped_blind} author-identifier line(s) for blinded output.")
    pre = "\n".join(pre_lines)

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp.write(pre)
        tmp_path = tmp.name

    cmd = [
        "pandoc", tmp_path,
        "-o", str(out),
        "--standalone",
        "--from", "markdown+pipe_tables+tex_math_dollars",
        "--to", "docx",
        "--toc", "--toc-depth=2",
        "--resource-path", str(resource),
    ]
    out.parent.mkdir(parents=True, exist_ok=True)
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        size_kb = out.stat().st_size // 1024
        print(f"   ✓ Built {out_rel} ({size_kb} KB)")
        return True
    else:
        print(f"   ✗ Failed: {result.stderr[:200]}")
        return False


def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--paper", required=True, choices=list(PAPERS.keys()) + ["all"])
    args = parser.parse_args()

    targets = list(PAPERS.keys()) if args.paper == "all" else [args.paper]
    print(f"Building {len(targets)} paper DOCX(s)...")
    ok = sum(1 for p in targets if build_one(p))
    print(f"\n✓ {ok}/{len(targets)} successful")


if __name__ == "__main__":
    main()

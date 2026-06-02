#!/usr/bin/env python3
"""
P5 China — Build submission DOCX via pandoc.

Usage:
    python3 p5/replication/build_docx.py

Outputs:
    p5/submission/ijoem_package/01_manuscript_blinded.docx
"""
import re
import subprocess
import tempfile
from pathlib import Path

ROOT = Path(__file__).resolve().parents[2]
SRC = ROOT / "p5" / "p5_china_en_clean.md"
OUT = ROOT / "p5" / "submission" / "ijoem_package" / "01_manuscript_blinded.docx"
RESOURCE = ROOT / "p5"

def main():
    src = SRC.read_text(encoding="utf-8")
    # Convert standalone --- separators to *** to avoid YAML interpretation
    pre = "\n".join(("***" if l.strip() == "---" else l) for l in src.splitlines())

    with tempfile.NamedTemporaryFile("w", suffix=".md", delete=False, encoding="utf-8") as tmp:
        tmp.write(pre)
        tmp_path = tmp.name

    cmd = [
        "pandoc", tmp_path,
        "-o", str(OUT),
        "--standalone",
        "--from", "markdown+pipe_tables+tex_math_dollars",
        "--to", "docx",
        "--toc", "--toc-depth=2",
        "--resource-path", str(RESOURCE),
    ]
    result = subprocess.run(cmd, capture_output=True, text=True)
    if result.returncode == 0:
        size_kb = OUT.stat().st_size // 1024
        print(f"✓ Built: {OUT} ({size_kb} KB)")
    else:
        print("✗ Failed:", result.stderr)
        raise SystemExit(1)

if __name__ == "__main__":
    main()

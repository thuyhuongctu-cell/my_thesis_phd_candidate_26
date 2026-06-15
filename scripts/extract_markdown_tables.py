"""
General Markdown-table -> Excel extractor.

Parses every Markdown table in a source .md file and writes each to its own sheet,
naming the sheet from the nearest bold caption (**...**) above the table. Pure
parse of author-written tables — no recomputation or fabrication.

Usage:
    python3 scripts/extract_markdown_tables.py <input.md> <output.xlsx> [SheetPrefix]
"""
import os
import re
import sys
import pandas as pd


def extract(src_path, out_path, prefix="T"):
    lines = open(src_path, encoding="utf-8").read().split("\n")
    bold_re = re.compile(r"\*\*(.+?)\*\*")

    def cells(row):
        return [c.strip() for c in row.strip().strip("|").split("|")]

    tables, i, seen = [], 0, {}
    while i < len(lines):
        if not lines[i].lstrip().startswith("|"):
            i += 1
            continue
        block = []
        while i < len(lines) and lines[i].lstrip().startswith("|"):
            block.append(lines[i].strip())
            i += 1
        if len(block) < 2:
            continue
        # nearest caption above the table: bold **...**, a "Bảng X.N ..." line,
        # or a "## Heading". Look back up to 8 lines; stop at another table.
        caption = ""
        first_row = i - len(block)
        for k in range(1, 9):
            j = first_row - k
            if j < 0:
                break
            ln = lines[j].strip()
            if not ln:
                continue
            if ln.startswith("|"):
                break
            mb = bold_re.search(ln)
            if mb and mb.group(1).strip():
                caption = mb.group(1).strip().rstrip(":").strip()
                break
            mt = re.match(r"^(Bảng\s+[\w.]+[.\s].*)$", ln)
            if mt:
                caption = mt.group(1).strip().rstrip(".").strip()
                break
            mh = re.match(r"^#{1,4}\s+(.+)$", ln)
            if mh:
                caption = mh.group(1).strip()
                break
        header = cells(block[0])
        body = [cells(r) for r in block[2:] if any(c for c in cells(r))]
        body = [(r + [""] * len(header))[:len(header)] for r in body]
        df = pd.DataFrame(body, columns=header)
        base = re.sub(r"[^0-9A-Za-zÀ-ỹ ]", "", caption)[:24].strip()
        if not base:  # fall back to the first header cells when no caption found
            base = re.sub(r"[^0-9A-Za-zÀ-ỹ ]", "", " ".join(header[:2]))[:24].strip()
        name = f"{prefix}{len(tables)+1}_{base or prefix}".replace(" ", "_")[:31]
        seen[name] = seen.get(name, 0) + 1
        if seen[name] > 1:
            name = f"{name[:28]}_{seen[name]}"
        tables.append((name, caption, df))

    with pd.ExcelWriter(out_path, engine="openpyxl") as xw:
        readme = pd.DataFrame([{"Sheet": n, "Caption (nguyên văn)": c, "Số dòng": len(d)}
                               for n, c, d in tables])
        readme.to_excel(xw, sheet_name="README", index=False)
        for name, _cap, df in tables:
            df.to_excel(xw, sheet_name=name, index=False)
    print(f"Saved: {os.path.relpath(out_path)}  ({len(tables)} tables + README)")
    for n, c, d in tables:
        print(f"  {n}: {d.shape[0]}×{d.shape[1]}  «{c[:50]}»")


if __name__ == "__main__":
    if len(sys.argv) < 3:
        print(__doc__); sys.exit(1)
    extract(sys.argv[1], sys.argv[2], sys.argv[3] if len(sys.argv) > 3 else "T")

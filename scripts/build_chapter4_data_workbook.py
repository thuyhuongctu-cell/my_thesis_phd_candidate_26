"""
Extract the result tables of dissertation Chapter 4 (Bảng 4.1 … 4.7) verbatim
from thesis/chuong_4_ket_qua_vi.md into an Excel workbook for submission/review.

This is a pure parse of the Markdown tables the author already wrote and verified;
no values are recomputed or fabricated. Each Bảng becomes one sheet, with its
caption preserved on a README sheet.

Output: dist/figure_data/chuong4_ket_qua_data.xlsx
Run from project root: python3 scripts/build_chapter4_data_workbook.py
"""
import os
import re
import pandas as pd

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
SRC = os.path.join(ROOT, "thesis", "chuong_4_ket_qua_vi.md")
OUT = os.path.join(ROOT, "dist", "figure_data", "chuong4_ket_qua_data.xlsx")

lines = open(SRC, encoding="utf-8").read().split("\n")
cap_re = re.compile(r"\*\*Bảng (4\.\d+)\.\*\*\s*\*?(.*)")

tables = []   # (id, caption, dataframe)
i = 0
while i < len(lines):
    m = cap_re.search(lines[i])
    if not m:
        i += 1
        continue
    tid, caption = m.group(1), m.group(2).strip().rstrip("*")
    # find the next markdown table (contiguous lines starting with '|')
    j = i + 1
    while j < len(lines) and not lines[j].lstrip().startswith("|"):
        if lines[j].strip() and lines[j].lstrip().startswith("**Bảng"):
            break
        j += 1
    block = []
    while j < len(lines) and lines[j].lstrip().startswith("|"):
        block.append(lines[j].strip())
        j += 1
    if len(block) >= 2:
        def cells(row):
            return [c.strip() for c in row.strip().strip("|").split("|")]
        header = cells(block[0])
        body = [cells(r) for r in block[2:]]   # block[1] is the |---| separator
        body = [r for r in body if any(c for c in r)]
        # pad/truncate rows to header width
        body = [(r + [""] * len(header))[:len(header)] for r in body]
        df = pd.DataFrame(body, columns=header)
        tables.append((tid, caption, df))
        print(f"Bảng {tid}: {df.shape[0]} rows × {df.shape[1]} cols")
    i = j

with pd.ExcelWriter(OUT, engine="openpyxl") as xw:
    readme = pd.DataFrame(
        [{"Sheet": f"Bang_{t.replace('.', '_')}", "Bảng": t, "Tiêu đề": cap}
         for t, cap, _ in tables]
    )
    readme.to_excel(xw, sheet_name="README", index=False)
    for tid, cap, df in tables:
        df.to_excel(xw, sheet_name=f"Bang_{tid.replace('.', '_')}"[:31], index=False)

print(f"\nSaved: {os.path.relpath(OUT, ROOT)}  ({len(tables)} tables + README)")

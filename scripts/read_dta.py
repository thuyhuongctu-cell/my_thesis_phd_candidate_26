#!/usr/bin/env python3
"""Read and inspect Stata .dta files (WBES raw data).

Backend: pyreadstat (preferred — exposes variable & value labels) with a
pandas.read_stata fallback. Designed for the WBES re-lock pipeline where each
country .dta carries ~340 columns with Stata variable/value labels.

Usage:
  python3 scripts/read_dta.py info     <file.dta>
  python3 scripts/read_dta.py cols     <file.dta> [--grep REGEX]
  python3 scripts/read_dta.py head     <file.dta> [-n 10] [--cols c1,c2,...]
  python3 scripts/read_dta.py labels   <file.dta> <column>      # value labels
  python3 scripts/read_dta.py describe <file.dta> [--cols c1,c2,...]
  python3 scripts/read_dta.py find     <dir> --grep REGEX       # search a column across files

Examples:
  python3 scripts/read_dta.py info data_wbes/raw_dta/Lao-PDR-2024-full-data.dta
  python3 scripts/read_dta.py cols data_wbes/raw_dta/*.dta --grep '^d3'   # FSTS export vars
  python3 scripts/read_dta.py labels data_wbes/raw_dta/Cambodia-2024-ISBS-full-data.dta b1
"""
from __future__ import annotations
import argparse
import glob
import os
import re
import sys

try:
    import pyreadstat  # noqa
    HAVE_PYREADSTAT = True
except Exception:
    HAVE_PYREADSTAT = False

import pandas as pd


def _meta_only(path: str):
    """Return (column_names, column_labels dict, value_labels dict, n_rows)."""
    if HAVE_PYREADSTAT:
        _, meta = pyreadstat.read_dta(path, metadataonly=True)
        labels = dict(zip(meta.column_names, meta.column_labels))
        return meta.column_names, labels, meta.variable_value_labels, meta.number_rows
    # pandas fallback: read variable labels via StataReader, no value labels
    with pd.io.stata.StataReader(path) as r:
        cols = list(r.varlist)
        labels = dict(zip(r.varlist, r.variable_labels().values())) \
            if hasattr(r, "variable_labels") else {c: "" for c in cols}
        nrows = r.nobs
    return cols, labels, {}, nrows


def cmd_info(args):
    for path in _expand(args.file):
        cols, labels, vlabels, nrows = _meta_only(path)
        size = os.path.getsize(path) / 1e6
        print(f"\n📄 {os.path.basename(path)}  ({size:.1f} MB)")
        print(f"   rows={nrows}  cols={len(cols)}  value-labelled vars={len(vlabels)}")
        print(f"   backend={'pyreadstat' if HAVE_PYREADSTAT else 'pandas'}")


def cmd_cols(args):
    pat = re.compile(args.grep, re.I) if args.grep else None
    for path in _expand(args.file):
        cols, labels, _, _ = _meta_only(path)
        sel = [c for c in cols if not pat or pat.search(c)]
        print(f"\n📄 {os.path.basename(path)}  ({len(sel)}/{len(cols)} cols)")
        for c in sel:
            lab = (labels.get(c) or "").strip()
            print(f"   {c:<14} {lab[:80]}")


def cmd_head(args):
    cols = args.cols.split(",") if args.cols else None
    for path in _expand(args.file):
        if HAVE_PYREADSTAT:
            df, _ = pyreadstat.read_dta(path, usecols=cols, row_limit=args.n)
        else:
            df = pd.read_stata(path, columns=cols).head(args.n)
        print(f"\n📄 {os.path.basename(path)}")
        with pd.option_context("display.max_columns", None, "display.width", 200):
            print(df.head(args.n).to_string())


def cmd_labels(args):
    path = _expand(args.file)[0]
    cols, clabels, vlabels, _ = _meta_only(path)
    col = args.column
    if col not in cols:
        sys.exit(f"Column '{col}' not in {os.path.basename(path)}")
    print(f"{col}  —  {(clabels.get(col) or '').strip()}")
    vl = vlabels.get(col)
    if not vl:
        print("  (no value labels — likely continuous/string)")
        return
    for k, v in sorted(vl.items(), key=lambda x: (isinstance(x[0], str), x[0])):
        print(f"  {k!r:>8} = {v}")


def cmd_describe(args):
    cols = args.cols.split(",") if args.cols else None
    for path in _expand(args.file):
        if HAVE_PYREADSTAT:
            df, _ = pyreadstat.read_dta(path, usecols=cols)
        else:
            df = pd.read_stata(path, columns=cols)
        print(f"\n📄 {os.path.basename(path)}  (n={len(df)})")
        with pd.option_context("display.max_columns", None, "display.width", 200):
            print(df.describe(include="all").to_string())


def cmd_find(args):
    pat = re.compile(args.grep, re.I)
    files = sorted(glob.glob(os.path.join(args.dir, "*.dta")))
    print(f"Searching {len(files)} .dta in {args.dir} for column /{args.grep}/\n")
    for path in files:
        try:
            cols, labels, _, _ = _meta_only(path)
        except Exception as e:
            print(f"  ⚠ {os.path.basename(path)}: {type(e).__name__}")
            continue
        hits = [c for c in cols if pat.search(c)]
        if hits:
            print(f"  ✓ {os.path.basename(path):<45} {', '.join(hits)}")


def _expand(patterns):
    out = []
    for p in (patterns if isinstance(patterns, list) else [patterns]):
        m = glob.glob(p)
        out.extend(sorted(m) if m else [p])
    if not out:
        sys.exit("No files matched.")
    return out


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = ap.add_subparsers(dest="cmd", required=True)

    p = sub.add_parser("info"); p.add_argument("file", nargs="+"); p.set_defaults(fn=cmd_info)
    p = sub.add_parser("cols"); p.add_argument("file", nargs="+"); p.add_argument("--grep"); p.set_defaults(fn=cmd_cols)
    p = sub.add_parser("head"); p.add_argument("file", nargs="+"); p.add_argument("-n", type=int, default=10); p.add_argument("--cols"); p.set_defaults(fn=cmd_head)
    p = sub.add_parser("labels"); p.add_argument("file"); p.add_argument("column"); p.set_defaults(fn=cmd_labels)
    p = sub.add_parser("describe"); p.add_argument("file", nargs="+"); p.add_argument("--cols"); p.set_defaults(fn=cmd_describe)
    p = sub.add_parser("find"); p.add_argument("dir"); p.add_argument("--grep", required=True); p.set_defaults(fn=cmd_find)

    args = ap.parse_args()
    args.fn(args)


if __name__ == "__main__":
    main()

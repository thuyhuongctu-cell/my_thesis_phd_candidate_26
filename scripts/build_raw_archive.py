#!/usr/bin/env python3
"""Build a deduplicated, Asia-Pacific-only raw WBES .dta archive.

Sources: existing data_wbes/raw_dta/*.dta + loose uploaded *.dta. Each file is
parsed to a canonical (country, year) key; standard private-firm cross-sections
only (panels / Informal / ISBS / ISES / Micro / expansion excluded). One file per
economy-year survives (existing raw file preferred, else largest upload). Files
for NON_ASIA economies are removed. Idempotent: safe to re-run after new uploads.

Usage: python3 scripts/build_raw_archive.py [UPLOAD_DIR]
"""
from __future__ import annotations
import glob
import os
import shutil
import sys

from wbes_canon import NON_ASIA, parse

RAW = "data_wbes/raw_dta"
DEFAULT_UPLOADS = "/root/.claude/uploads/8e33d986-57ea-5213-85e4-ad328f348bd2"


def main():
    apply = "--apply" in sys.argv
    args = [a for a in sys.argv[1:] if not a.startswith("--")]
    up = args[0] if args else DEFAULT_UPLOADS
    cands = []  # (path, source, meta, size)
    for p in glob.glob(f"{RAW}/*.dta"):
        m = parse(p)
        if m:
            cands.append((p, "raw", m, os.path.getsize(p)))
    for p in glob.glob(f"{up}/*.dta"):
        m = parse(p)
        if m:
            cands.append((p, "upload", m, os.path.getsize(p)))

    # keep only standard, non-panel, Asia-Pacific candidates
    elig = [(p, s, m, sz) for (p, s, m, sz) in cands
            if m["standard"] and not m["panel"] and m["country"] not in NON_ASIA]

    # winner per (country, year): prefer an existing raw file, else largest upload
    winners: dict[tuple, tuple] = {}
    for p, s, m, sz in elig:
        k = (m["country"], m["year"])
        cur = winners.get(k)
        if cur is None:
            winners[k] = (p, s, sz)
            continue
        cp, cs, csz = cur
        better = (s == "raw" and cs != "raw") or \
                 (s == cs and sz > csz)
        if better:
            winners[k] = (p, s, sz)

    keep_raw_paths = {w[0] for w in winners.values() if w[1] == "raw"}

    # 1) raw files to delete: non-Asia, or duplicate of a kept economy-year
    removed_nonasia, removed_dup = [], []
    for p in glob.glob(f"{RAW}/*.dta"):
        m = parse(p)
        if m is None:
            continue
        if m["country"] in NON_ASIA:
            removed_nonasia.append(p); continue
        if (not m["standard"]) or m["panel"]:
            continue  # leave non-standard originals untouched
        if p not in keep_raw_paths:
            removed_dup.append(p)

    # 2) upload winners to copy in (economy-years not already in raw)
    added = []
    for (country, year), (p, s, sz) in sorted(winners.items()):
        if s != "upload":
            continue
        dest = f"{RAW}/{country}-{year}-full-data.dta"
        if os.path.exists(dest):
            continue
        added.append((p, dest))

    if apply:
        for p in removed_nonasia + removed_dup:
            os.remove(p)
        for src, dest in added:
            shutil.copy2(src, dest)
    else:
        print(">>> DRY-RUN (no filesystem changes). Re-run with --apply to execute.\n")

    print(f"ADD {len(added)} | REMOVE dup {len(removed_dup)} | "
          f"REMOVE non-Asia {len(removed_nonasia)}")
    if added:
        print("\n+ add (from uploads):")
        [print("   ", os.path.basename(d)) for _, d in sorted(added)]
    if removed_nonasia:
        print("\n- remove non-Asia:")
        [print("   ", os.path.basename(p)) for p in sorted(removed_nonasia)]
    if removed_dup:
        print("\n- remove duplicate economy-year:")
        [print("   ", os.path.basename(p)) for p in sorted(removed_dup)]


if __name__ == "__main__":
    sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))
    main()

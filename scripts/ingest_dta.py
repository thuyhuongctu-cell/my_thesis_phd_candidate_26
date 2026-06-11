#!/usr/bin/env python3
"""Ingest uploaded WBES .dta files into data_wbes/raw_dta/ with clean names.

Scans a source directory for *.dta files and *panel*data*.zip archives, derives
a tidy `Country-YEAR(S)-suffix.dta` filename, and copies them into the raw_dta
folder. Idempotent — safe to re-run as more upload batches arrive.

Usage:
  python3 scripts/ingest_dta.py <source_dir> [--dest data_wbes/raw_dta] [--dry-run]
"""
from __future__ import annotations
import argparse
import glob
import os
import re
import shutil
import tempfile
import zipfile

# CamelCase / known multi-word country tokens -> hyphenated
COUNTRY_FIX = {
    "TimorLeste": "Timor-Leste",
    "Timor": "Timor-Leste",
    "SriLanka": "Sri-Lanka",
    "TaiwanChina": "Taiwan-China",
    "HongKongSARChina": "HongKong-SAR-China",
    "KoreaRepublic": "Korea-Republic",
    "Korearepublic": "Korea-Republic",
    "KyrgyzRepublic": "Kyrgyz-Republic",
    "Kyrgyzrepublic": "Kyrgyz-Republic",
    "BruneiDarussalam": "Brunei-Darussalam",
    "LaoPDR": "Lao-PDR",
    "LaoInformal": "Lao-Informal",
    "CambodiaInformal": "Cambodia-Informal",
}
# suffix token normalisation (applied after the year block)
SUFFIX_FIX = [
    ("fulldataLongForm", "full-data-LongForm"),
    ("ISBSfulldata", "ISBS-full-data"),
    ("ESISfulldata", "ESIS-full-data"),
    ("ISESfulldata", "ISES-full-data"),
    ("Microfulldata", "Micro-full-data"),
    ("fulldata", "full-data"),
    ("full_data", "full-data"),
    ("fullESN2700data", "full-ESN2700-data"),
    ("paneldata", "panel-data"),
    ("panel_data", "panel-data"),
]
HASH_RE = re.compile(r"^[0-9a-f]{6,}-")
YEAR_RE = re.compile(r"((?:19|20)\d{2})")


def clean_name(raw: str, panel: bool = False) -> str:
    base = HASH_RE.sub("", raw).replace(" ", "")
    base = re.sub(r"\.dta$", "", base, flags=re.I)
    m = re.match(r"^([A-Za-z]+)(.*)$", base)          # leading letters = country
    country_raw, rest = (m.group(1), m.group(2)) if m else (base, "")
    country = COUNTRY_FIX.get(country_raw, country_raw)
    years = YEAR_RE.findall(rest)
    year_part = "_".join(years) if years else "NA"
    if panel:                                          # underscore style (matches existing panels)
        return f"{country}_{year_part}.dta"
    suffix = YEAR_RE.sub("", rest).strip("_-")         # dash style for cross-sections
    for a, b in SUFFIX_FIX:
        suffix = suffix.replace(a, b)
    suffix = suffix.strip("_-") or "full-data"
    return f"{country}-{year_part}-{suffix}.dta"


def ingest(src: str, dest: str, dry: bool) -> None:
    os.makedirs(dest, exist_ok=True)
    seen = {}
    # plain .dta
    for f in sorted(glob.glob(os.path.join(src, "*.dta"))):
        _place(f, clean_name(os.path.basename(f)), dest, dry, seen)
    # panel zips
    for z in sorted(glob.glob(os.path.join(src, "*.zip"))):
        if not re.search(r"panel", os.path.basename(z), re.I):
            continue
        with tempfile.TemporaryDirectory() as tmp:
            try:
                with zipfile.ZipFile(z) as zf:
                    zf.extractall(tmp)
            except Exception as e:
                print(f"  ⚠ zip {os.path.basename(z)}: {e}")
                continue
            for f in glob.glob(os.path.join(tmp, "**", "*.dta"), recursive=True):
                _place(f, clean_name(os.path.basename(f), panel=True), dest, dry, seen)


def _place(src_path, name, dest, dry, seen):
    dst = os.path.join(dest, name)
    tag = "DRY" if dry else ("dup→skip" if name in seen else "ok")
    if name in seen:
        print(f"  · {name:<46} (duplicate in batch, skipped)")
        return
    seen[name] = src_path
    if not dry:
        shutil.copy2(src_path, dst)
    print(f"  ✓ {name:<46} [{tag}]")


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("src")
    ap.add_argument("--dest", default="data_wbes/raw_dta")
    ap.add_argument("--dry-run", action="store_true")
    a = ap.parse_args()
    print(f"Ingesting from {a.src} -> {a.dest}\n")
    ingest(a.src, a.dest, a.dry_run)


if __name__ == "__main__":
    main()

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

# Canonical country names, keyed by lowercased string with separators removed.
COUNTRY_NORM = {
    "timorleste": "Timor-Leste", "timor": "Timor-Leste",
    "srilanka": "Sri-Lanka",
    "taiwanchina": "Taiwan-China", "taiwan": "Taiwan-China",
    "hongkongsarchina": "HongKong-SAR-China", "hongkong": "HongKong-SAR-China",
    "korearepublic": "Korea-Republic", "korea": "Korea-Republic", "korearep": "Korea-Republic",
    "kyrgyzrepublic": "Kyrgyz-Republic", "kyrgyz": "Kyrgyz-Republic",
    "bruneidarussalam": "Brunei-Darussalam", "brunei": "Brunei-Darussalam",
    "laopdr": "Lao-PDR", "lao": "Lao-PDR", "laos": "Lao-PDR",
    "laoinformal": "Lao-Informal",
    "cambodiainformal": "Cambodia-Informal",
    "indiamicro": "India-Micro",
    "vietnam": "Vietnam", "vietnam-": "Vietnam",
    "republicofcyprus": "Cyprus", "cyprus": "Cyprus",
}
SUFFIX_FIX = [("fulldata", "full-data"), ("full data", "full-data"),
              ("paneldata", "panel-data"), ("esn2700", "ES-N2700")]
HASH_RE = re.compile(r"^[0-9a-f]{6,}-")
YEAR_RE = re.compile(r"((?:19|20)\d{2})")


def _country(raw: str) -> str:
    key = re.sub(r"[ _\-]", "", raw).lower()
    if key in COUNTRY_NORM:
        return COUNTRY_NORM[key]
    # unknown: collapse separators to single dash, keep capitalisation
    return re.sub(r"[ _]+", "-", raw.strip(" _-")) or "Unknown"


def clean_name(raw: str, panel: bool = False) -> str:
    base = HASH_RE.sub("", raw)
    base = re.sub(r"\.dta$", "", base, flags=re.I).strip()
    ym = YEAR_RE.search(base)
    if ym:
        country = _country(base[:ym.start()])
        years = YEAR_RE.findall(base)
        suffix = YEAR_RE.sub("", base[ym.start():])
    else:
        country, years, suffix = _country(base), [], ""
    year_part = "_".join(years) if years else "NA"
    # Auto-detect panel: 2+ year tokens and no descriptive suffix
    suffix_clean = re.sub(r"[ _\-]+", "-", suffix).strip("-")
    for a, b in SUFFIX_FIX:
        suffix_clean = re.sub(re.escape(a), b, suffix_clean, flags=re.I)
    suffix_clean = re.sub(r"-{2,}", "-", suffix_clean).strip("-")
    is_panel = panel or (len(years) >= 2 and suffix_clean in ("", "data", "panel-data"))
    if is_panel:
        return f"{country}_{year_part}.dta"
    return f"{country}-{year_part}-{suffix_clean or 'full-data'}.dta"


def ingest(src: str, dest: str, dry: bool) -> None:
    os.makedirs(dest, exist_ok=True)
    seen = {}
    # plain .dta
    for f in sorted(glob.glob(os.path.join(src, "*.dta"))):
        _place(f, clean_name(os.path.basename(f)), dest, dry, seen)
    # every zip that holds .dta members (panel archives + bundles)
    for z in sorted(glob.glob(os.path.join(src, "*.zip"))):
        try:
            zf = zipfile.ZipFile(z)
        except Exception as e:
            print(f"  ⚠ zip {os.path.basename(z)}: {e}")
            continue
        members = [m for m in zf.namelist() if m.lower().endswith(".dta")]
        for m in members:
            with tempfile.TemporaryDirectory() as tmp:
                try:                       # extract each member alone — skip bad CRC
                    zf.extract(m, tmp)
                except Exception as e:
                    print(f"  ⚠ {os.path.basename(z)}::{os.path.basename(m)}: {type(e).__name__}")
                    continue
                _place(os.path.join(tmp, m), clean_name(os.path.basename(m)), dest, dry, seen)
        zf.close()


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

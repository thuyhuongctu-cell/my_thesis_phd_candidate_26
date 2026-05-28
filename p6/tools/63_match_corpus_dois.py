#!/usr/bin/env python3
"""
63_match_corpus_dois.py — Match the k=238 study database against an OpenAlex
"works" CSV export (the user's curated corpus) to recover real DOIs, offline.

For each study we find corpus works whose author list contains the study's
first-author surname and whose year is within +/-1, then classify the best
candidate by confidence:

  confirmed_title    APA title present and token-overlap >= 0.60  -> trustworthy
  confirmed_openalex corpus DOI == the OpenAlex-verified DOI       -> trustworthy
  candidate_unique   exactly one corpus candidate, no title check  -> suggest
  candidate_multi    several candidates, cannot disambiguate       -> suggest
  no_corpus_match    nothing in the corpus                         -> -

Only the confirmed_* tiers are safe to publish; the rest are suggestions a human
confirms. Reuses fold/surname/title_overlap/author_matches from script 60.

Usage:
  python3 63_match_corpus_dois.py \
      --db       ../data/p6_study_database.csv \
      --apa      ../p6_primary_studies_apa7.md \
      --corpus   works.csv \
      --enriched ../data/p6_openalex_enriched.csv \
      --out      ../data/p6_corpus_matches.csv
"""

import argparse
import csv
import importlib.util
import re
from pathlib import Path

CONFIRM_OVERLAP = 0.60
TRUSTED_ENRICH = {"verified", "title_match", "title_corrected"}
OUT_FIELDS = [
    "study_id", "author", "year", "enrich_status", "enrich_doi",
    "corpus_doi", "corpus_title", "corpus_journal", "corpus_year",
    "n_candidates", "title_overlap", "match_confidence", "agrees_enrich",
]


def load_mod(path: Path):
    spec = importlib.util.spec_from_file_location("enrich60", path)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def to_int(y):
    try:
        return int(str(y).strip())
    except (ValueError, TypeError):
        return None


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--apa", default="")
    ap.add_argument("--corpus", required=True, nargs="+",
                    help="one or more OpenAlex works CSV exports")
    ap.add_argument("--enriched", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--module", default=str(Path(__file__).with_name("60_enrich_openalex_metadata.py")))
    args = ap.parse_args()

    mod = load_mod(Path(args.module))
    fold, surname, overlap = mod.fold, mod.surname, mod.title_overlap

    apa = mod.parse_apa(Path(args.apa)) if args.apa else {}

    enrich = {}
    if args.enriched and Path(args.enriched).exists():
        for r in csv.DictReader(open(args.enriched, encoding="utf-8")):
            enrich[r["study_id"]] = r

    def load_csv(cf):
        rows = []
        with open(cf, encoding="utf-8") as fh:
            for r in csv.DictReader(fh):
                doi = (r.get("doi") or "").replace("https://doi.org/", "").strip().lower()
                if not doi:
                    continue
                rows.append({
                    "doi": doi,
                    "title": r.get("display_name") or "",
                    "authors_folded": fold(r.get("authorships.author.display_name") or ""),
                    "year": to_int(r.get("publication_year")),
                    "journal": r.get("primary_location.source.display_name") or "",
                })
        return rows

    def load_ris(cf):
        rows, cur = [], None
        def flush(c):
            if c and (c["doi"] or c["title"]):
                rows.append({
                    "doi": c["doi"].replace("https://doi.org/", "").strip().lower(),
                    "title": c["title"],
                    "authors_folded": fold(" | ".join(c["authors"])),
                    "year": c["year"],
                    "journal": c["journal"],
                })
        for line in open(cf, encoding="utf-8", errors="replace"):
            tag, val = line[:6], line[6:].strip()
            if tag == "TY  -":
                flush(cur); cur = {"authors": [], "title": "", "year": None, "doi": "", "journal": ""}
            elif cur is None:
                continue
            elif tag in ("TI  -", "T1  -"):
                cur["title"] = val
            elif tag == "AU  -":
                cur["authors"].append(val)
            elif tag in ("PY  -", "Y1  -"):
                m = re.search(r"\d{4}", val); cur["year"] = int(m.group()) if m else None
            elif tag == "DO  -":
                cur["doi"] = val
            elif tag in ("T2  -", "JO  -", "JF  -") and not cur["journal"]:
                cur["journal"] = val
            elif tag == "ER  -":
                flush(cur); cur = None
        flush(cur)
        return rows

    corpus, seen_doi = [], set()
    for cf in args.corpus:
        rows = load_ris(cf) if cf.lower().endswith(".ris") else load_csv(cf)
        for r in rows:
            if r["doi"] and r["doi"] not in seen_doi:
                seen_doi.add(r["doi"])
                corpus.append(r)

    seen, studies = set(), []
    for r in csv.DictReader(open(args.db, encoding="utf-8")):
        sid = (r.get("study_id") or "").strip()
        if sid and sid not in seen:
            seen.add(sid)
            studies.append(r)

    out_rows, tally = [], {}
    for s in studies:
        sid = s["study_id"].strip()
        sn = fold(surname(s.get("author", "")))
        sy = to_int(s.get("year"))
        e = enrich.get(sid, {})
        apa_title = apa.get(int("".join(c for c in sid if c.isdigit()) or 0), {}).get("title", "")

        cands = [c for c in corpus if sn and sn in c["authors_folded"]
                 and c["year"] is not None and sy is not None and abs(c["year"] - sy) <= 1]

        enrich_doi = (e.get("oa_doi") or "").strip().lower()
        distinct_dois = {c["doi"] for c in cands}
        agrees = "yes" if enrich_doi and enrich_doi in distinct_dois else "no"

        best, best_ov = None, -1.0
        for c in cands:
            ov = overlap(apa_title, c["title"]) if apa_title else 0.0
            if ov > best_ov:
                best, best_ov = c, ov
        # a corpus candidate that equals the OpenAlex-resolved DOI is the safe pick
        if agrees == "yes" and (not best or best["doi"] != enrich_doi):
            best = next(c for c in cands if c["doi"] == enrich_doi)

        if not cands:
            conf = "no_corpus_match"
        elif apa_title and best_ov >= CONFIRM_OVERLAP:
            conf = "confirmed_title"
        elif agrees == "yes" and e.get("verify_status") in TRUSTED_ENRICH:
            conf = "confirmed_openalex"
        elif agrees == "yes":
            # corpus DOI == OpenAlex author+year DOI: two different queries agree
            conf = "confirmed_crosscheck"
        elif len(distinct_dois) == 1:
            conf = "candidate_unique"
        else:
            conf = "candidate_multi"

        tally[conf] = tally.get(conf, 0) + 1
        out_rows.append({
            "study_id": sid, "author": s.get("author", ""), "year": s.get("year", ""),
            "enrich_status": e.get("verify_status", ""), "enrich_doi": enrich_doi,
            "corpus_doi": best["doi"] if best else "",
            "corpus_title": best["title"] if best else "",
            "corpus_journal": best["journal"] if best else "",
            "corpus_year": best["year"] if best else "",
            "n_candidates": len(distinct_dois),
            "title_overlap": round(best_ov, 2) if best_ov >= 0 else "",
            "match_confidence": conf,
            "agrees_enrich": agrees,
        })

    out_path = Path(args.out)
    out_path.parent.mkdir(parents=True, exist_ok=True)
    with open(out_path, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=OUT_FIELDS)
        w.writeheader()
        w.writerows(out_rows)

    print(f"Corpus match written: {out_path}")
    for k in ("confirmed_title", "confirmed_openalex", "confirmed_crosscheck",
              "candidate_unique", "candidate_multi", "no_corpus_match"):
        print(f"  {k:20}: {tally.get(k, 0)}")
    trusted = sum(tally.get(k, 0) for k in
                  ("confirmed_title", "confirmed_openalex", "confirmed_crosscheck"))
    print(f"\n  NEW trustworthy DOIs from corpus (confirmed_*): {trusted}")
    print("  candidate_* are suggestions to confirm; no_corpus_match needs another source.")


if __name__ == "__main__":
    main()

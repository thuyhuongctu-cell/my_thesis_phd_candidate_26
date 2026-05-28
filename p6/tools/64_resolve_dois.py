#!/usr/bin/env python3
"""
64_resolve_dois.py — Resolve a final DOI per study by combining three sources
and cross-validating them:

  1. references  the thesis's own APA reference list (authoritative bibliography)
  2. openalex    the OpenAlex enrichment output (verified / title_match / title_corrected)
  3. corpus      DOIs confirmed against the OpenAlex works exports (script 63)

Matching to the reference list uses EXACT first-author surname + year +/-1
(substring matching falsely links short names like "Li" to "Williamson").

Confidence:
  high     >= 2 independent sources agree on the same DOI
  medium   only one source (a unique reference, or an OpenAlex-verified DOI)
  review   sources disagree, or the reference match is ambiguous (>1 DOI)
  none     no DOI from any source

Output: p6_doi_resolved.csv (study_id, final_doi, source, confidence, ...).

Usage:
  python3 64_resolve_dois.py \
      --db ../data/p6_study_database.csv \
      --references ../data/thesis_references_apa7.md \
      --enriched ../data/p6_openalex_enriched.csv \
      --corpus-matches ../data/p6_corpus_matches.csv \
      --apa ../p6_primary_studies_apa7.md \
      --out ../data/p6_doi_resolved.csv
"""

import argparse
import csv
import importlib.util
import re
from pathlib import Path

TRUSTED_ENRICH = {"verified", "title_match", "title_corrected"}
OUT_FIELDS = [
    "study_id", "author", "year", "final_doi", "source", "confidence",
    "ref_doi", "openalex_doi", "openalex_status", "corpus_doi", "n_sources_agree",
]


def load_mod(p):
    s = importlib.util.spec_from_file_location("e60", p)
    mod = importlib.util.module_from_spec(s)
    s.loader.exec_module(mod)
    return mod


def to_int(y):
    try:
        return int(str(y).strip())
    except (ValueError, TypeError):
        return None


def parse_references(path: Path, fold):
    """One record per DOI-bearing line: (surname, year, doi, title)."""
    refs = []
    if not path.exists():
        return refs
    for raw in path.read_text(encoding="utf-8").splitlines():
        line = raw.strip()
        dm = re.search(r"doi\.org/(\S+)", line)
        ym = re.search(r"\((\d{4})[a-z]?\)", line)
        if not dm or not ym:
            continue
        head = re.sub(r"^[\*\s>\-]+", "", line)
        first = re.split(r"[,(]", head)[0].strip()
        surname = fold(first.split()[-1]) if first.split() else ""
        refs.append({
            "surname": surname,
            "year": int(ym.group(1)),
            "doi": dm.group(1).rstrip(").,*").lower(),
        })
    return refs


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("--db", required=True)
    ap.add_argument("--references", required=True)
    ap.add_argument("--enriched", default="")
    ap.add_argument("--corpus-matches", default="")
    ap.add_argument("--apa", default="")
    ap.add_argument("--out", required=True)
    ap.add_argument("--module", default=str(Path(__file__).with_name("60_enrich_openalex_metadata.py")))
    args = ap.parse_args()

    mod = load_mod(Path(args.module))
    fold, surname = mod.fold, mod.surname

    refs = parse_references(Path(args.references), fold)

    enrich = {}
    if args.enriched and Path(args.enriched).exists():
        for r in csv.DictReader(open(args.enriched, encoding="utf-8")):
            enrich[r["study_id"]] = r

    corpus = {}
    if args.corpus_matches and Path(args.corpus_matches).exists():
        for r in csv.DictReader(open(args.corpus_matches, encoding="utf-8")):
            corpus[r["study_id"]] = r

    seen, studies = set(), []
    for r in csv.DictReader(open(args.db, encoding="utf-8")):
        sid = (r.get("study_id") or "").strip()
        if sid and sid not in seen:
            seen.add(sid)
            studies.append(r)

    rows, tally = [], {}
    for s in studies:
        sid = s["study_id"].strip()
        sn = fold(surname(s.get("author", "")))
        sy = to_int(s.get("year"))

        ref_dois = {r["doi"] for r in refs
                    if sn and r["surname"] == sn and sy and abs(r["year"] - sy) <= 1}
        ref_doi = next(iter(ref_dois)) if len(ref_dois) == 1 else ""

        e = enrich.get(sid, {})
        oa_status = e.get("verify_status", "")
        oa_doi = (e.get("oa_doi") or "").strip().lower() if oa_status in TRUSTED_ENRICH else ""

        cm = corpus.get(sid, {})
        cm_conf = cm.get("match_confidence", "")
        corpus_doi = (cm.get("corpus_doi") or "").strip().lower() if cm_conf.startswith("confirmed") else ""
        corpus_cand = (cm.get("corpus_doi") or "").strip().lower() if cm_conf == "candidate_unique" else ""

        votes = {}
        for d in (ref_doi, oa_doi, corpus_doi):
            if d:
                votes[d] = votes.get(d, 0) + 1
        trusted_set = {ref_doi, oa_doi, corpus_doi} - {""}
        final_doi, source, confidence, n_agree = "", "", "none", 0
        if votes:
            if len(trusted_set) > 1:
                # sources disagree -> prefer the thesis reference list (authoritative)
                final_doi = ref_doi or oa_doi or corpus_doi
                confidence, n_agree = "review", votes.get(final_doi, 1)
            else:
                final_doi, n_agree = max(votes.items(), key=lambda kv: kv[1])
                confidence = "high" if n_agree >= 2 else "medium"
            source = "+".join(name for name, d in
                              (("references", ref_doi), ("openalex", oa_doi), ("corpus", corpus_doi))
                              if d == final_doi)
        elif corpus_cand:
            final_doi, source, confidence, n_agree = corpus_cand, "corpus_suggested", "suggested", 1
        elif len(ref_dois) > 1:
            confidence, source = "review", "references_ambiguous"

        tally[confidence] = tally.get(confidence, 0) + 1
        rows.append({
            "study_id": sid, "author": s.get("author", ""), "year": s.get("year", ""),
            "final_doi": final_doi, "source": source, "confidence": confidence,
            "ref_doi": ref_doi, "openalex_doi": oa_doi, "openalex_status": oa_status,
            "corpus_doi": corpus_doi, "n_sources_agree": n_agree,
        })

    out = Path(args.out)
    out.parent.mkdir(parents=True, exist_ok=True)
    with open(out, "w", newline="", encoding="utf-8") as fh:
        w = csv.DictWriter(fh, fieldnames=OUT_FIELDS)
        w.writeheader()
        w.writerows(rows)

    resolved = sum(1 for r in rows if r["final_doi"])
    print(f"DOI resolution written: {out}")
    print(f"  studies: {len(rows)} | resolved with a DOI: {resolved}")
    for c in ("high", "medium", "review", "suggested", "none"):
        print(f"    {c:9}: {tally.get(c, 0)}")
    print(f"  reference list parsed: {len(refs)} DOI lines")


if __name__ == "__main__":
    main()

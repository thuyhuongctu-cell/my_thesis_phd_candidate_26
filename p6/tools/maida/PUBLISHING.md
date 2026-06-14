# Publishing M-AIDA: GitHub repository + Zenodo DOI

A step-by-step guide to turn this source tree into a public, citable,
archived repository — the public evidence of the author's software-engineering
capability behind the dissertation's meta-analysis (P6).

## Why a standalone repo

Keep M-AIDA in its **own** public repository, separate from the dissertation
repo. The git commit history (small, dated, explained commits, with bugs found
and fixed) is the strongest provenance evidence that the software was developed
by a person over time, not generated in one pass.

## Step 1 — create the repository

```bash
# from this directory (p6/tools/maida), with a clean copy
git init
git add .
git commit -m "M-AIDA v7.0.0: initial public release"
gh repo create maida-core --public --source=. --remote=origin --push
```

Fill `thuyhuongctu-cell` is already set in `CITATION.cff` (repository-code) with the GitHub account.

## Step 2 — tag a release

```bash
git tag -a v7.0.0 -m "M-AIDA v7.0.0 — meta-analysis effect-size assistant"
git push origin v7.0.0
```
Then on GitHub: **Releases → Draft a new release → choose tag v7.0.0 → Publish.**

## Step 3 — connect Zenodo for a permanent DOI

1. Sign in to https://zenodo.org with the GitHub account.
2. Zenodo → **GitHub** tab → toggle the `maida-core` repository **ON**.
3. Back on GitHub, publish the v7.0.0 release (Step 2). Zenodo automatically
   archives it and mints a DOI from `.zenodo.json` + `CITATION.cff`.
4. Copy the DOI badge Markdown from Zenodo into `README.md` (see badge slot).

## Step 4 — cite it in the dissertation and papers

- Add to the front-matter "Danh mục công trình": the M-AIDA software with its
  Zenodo DOI and COV copyright certificate number (once issued).
- In the P6 manuscript's data-availability statement, cite the Zenodo DOI.

## Step 5 — repository hygiene that signals quality

- [ ] `README.md` with architecture diagram, quick start, and a "Cite" section (done).
- [ ] `CITATION.cff` (done) → GitHub shows a "Cite this repository" button.
- [ ] `LICENSE` (done) → rights preserved + academic use permitted.
- [ ] `CHANGELOG.md` (done) → version history.
- [ ] `.env.example` committed, real secrets never committed (verify `.gitignore`).
- [ ] A short `demo/` with one sample PDF and the resulting CSV row (optional but
      powerful: a visitor reproduces an extraction end-to-end).

## Anti-AI-suspicion checklist (ties to REPRODUCIBILITY.md)

- Public commit history showing iterative development.
- Zenodo DOI + COV copyright certificate (independent authorship attestation).
- `CITATION.cff` linking the software to the author's ORCID.
- The author can open any module (`extractor.py`, `models.py`, `notion_sync.py`)
  and explain it — the decisive provenance check at the defense.

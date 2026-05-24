# ⚠️ DEPRECATED — DO NOT SUBMIT THESE FILES

**Status:** Superseded legacy track (24/05/2026). **Contains stale/incorrect data.**

These `dist/submission/` artifacts (`p3_vietnam_APJM`, `p4_singapore_MIR`,
`p5_china_APJM` — docx/tex/pdf) were built from the **older manuscript versions**
in the top-level `manuscripts/` directory, which target a legacy journal set
(APJM) and differ structurally from the current papers (fewer words, different
section organisation). They still carry **outdated results** — e.g. P4 Singapore
turning point 88.6% (corrected to **82%** after raw-`.dta` verification: N=623,
β₁=2.652/β₂=−1.705 → TP=82.3%, raw-data M2 → 78.6%), P3 missing five reference
entries, P5 pre-fix M6 equation.

## ✅ Use these CANONICAL, data-correct deliverables instead

| Purpose | Location |
|---------|----------|
| **Journal submission packages** (blinded ms + title page + cover letter) | `p{3,4,5,6,7,8}/submission/<journal>_package/` |
| **Current full manuscripts (DOCX)** | `dist/manuscripts/en/` and `dist/manuscripts/vi/` |
| **Canonical Markdown sources** | `p{3..8}/p{N}_*_en_clean.md`, `p{N}/submission/p{N}_*_vi.md` |

Current journal targets: P3→JABS, P4→MIR, P5→IJOEM, P6→IBR, P7→JIBS, P8→World Development.

PDF regeneration of any LaTeX track requires `pdflatex` (texlive), which is not
installed in this environment.

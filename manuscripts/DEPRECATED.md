# ⚠️ DEPRECATED — older manuscript versions (not canonical)

**Status:** Superseded legacy sources (24/05/2026).

The `manuscripts/*.md` files here are an **earlier version** of papers P3–P5
(legacy APJM-targeted, different section structure, fewer words) and carry
**outdated results** (e.g. P4 turning point 88.6% — corrected to 82% after
raw-`.dta` verification). They are NOT the editing path.

## ✅ Canonical sources (edit these)

- **Papers:** `p{3..8}/p{N}_*_en_clean.md`
- **VI manuscripts:** `p{N}/submission/p{N}_*_vi.md`
- **Submission packages:** `p{N}/submission/<journal>_package/`
- **Built dossier DOCX:** `dist/manuscripts/`, `dist/luan_an*/`, `dist/chuyen_de_1/`

`build_submission_package.sh` still reads from this directory and therefore
produces the legacy `dist/submission/` track — see `dist/submission/DEPRECATED.md`.
Do not submit its output; use the `p{N}/submission/` packages.

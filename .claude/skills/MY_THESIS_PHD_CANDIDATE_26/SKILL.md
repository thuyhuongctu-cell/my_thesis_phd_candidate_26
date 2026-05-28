```markdown
# MY_THESIS_PHD_CANDIDATE_26 Development Patterns

> Auto-generated skill from repository analysis

## Overview

This skill teaches the development and manuscript preparation patterns used in the `MY_THESIS_PHD_CANDIDATE_26` repository. The codebase supports the preparation of a PhD thesis and related manuscripts in both English and Vietnamese, focusing on academic writing consistency, terminology standardization, statistical notation normalization, and automated deliverable generation. The repository is primarily Python-based (no framework), with supporting scripts and build tools for document processing.

## Coding Conventions

- **File Naming:**  
  All files use `snake_case` for consistency.  
  *Example:*  
  ```
  fix_stat_notation.py
  00_cd1_ctu_final_vi.md
  04_references_apa7.md
  ```

- **Import Style:**  
  Relative imports are used within Python scripts.  
  *Example:*  
  ```python
  from .utils import normalize_notation
  ```

- **Export Style:**  
  Named exports are preferred.  
  *Example:*  
  ```python
  def fix_stat_notation(...):
      ...
  ```

- **Commit Messages:**  
  Follows [Conventional Commits](https://www.conventionalcommits.org/) with prefixes: `style`, `build`, `fix`, `docs`, `chore`.  
  *Example:*  
  ```
  fix: correct p-value formatting in Vietnamese manuscripts
  ```

## Workflows

### Deep Author Voice Transformation
**Trigger:** When preparing a manuscript or thesis chapter for submission or review, to ensure consistent authorial style and academic register.  
**Command:** `/transform-author-voice`

1. Apply the author-voice transformation skill to relevant manuscript files (English and/or Vietnamese).
2. Normalize variable notation and Scopus/WoS symbols as needed.
3. Update both source manuscripts and distribution copies.
4. Regenerate deliverables (`.docx`/`.pdf`) if required.

*Files involved:*  
- `dist/manuscripts/en/source_md/*_en_clean.md`
- `dist/manuscripts/vi/source_md/*_vi.md`
- `manuscripts/*_en_clean.md`
- `manuscripts/*_vi_clean.md`
- `p*/p*_en_clean.md`
- `p*/submission/p*_vi.md`
- `chuyen_de/cd1/00_cd1_ctu_final_vi.md`
- `chuyen_de/cd2/00_cd2_ctu_final_vi.md`
- `thesis/chuong_*_vi.md`

*Example usage:*  
```bash
/transform-author-voice
```

---

### Terminology and Glossary Standardization
**Trigger:** When inconsistent or awkward terminology is detected in manuscripts, or after reviewer feedback.  
**Command:** `/standardize-terminology`

1. Identify non-standard or literal translations in manuscript files.
2. Replace with standardized terms as per the glossary or terminology skill.
3. Add or update glossary entries to reflect new or corrected terms.
4. Regenerate affected deliverables (`.docx`/`.pdf`) if needed.

*Files involved:*  
- `p3/submission/p3_vietnam_vi.md`
- `thesis/09b_vn_term_glossary.md`
- `chuyen_de/cd1/00_cd1_ctu_final_vi.md`
- `chuyen_de/cd2/00_cd2_ctu_final_vi.md`

*Example usage:*  
```bash
/standardize-terminology
```

---

### Statistical Notation and Math Normalization
**Trigger:** When preparing documents for submission or after a standards review to ensure statistical notation consistency.  
**Command:** `/normalize-stat-notation`

1. Run scripts to harmonize statistical notation (e.g., p-values, betas, decimal separators).
2. Convert Unicode math operators and inline coefficients/exponents to LaTeX math.
3. Replace non-standard symbols (arrows, en-dashes, etc.) with standard equivalents.
4. Regenerate deliverables (`.docx`/`.pdf`) as needed.

*Files involved:*  
- `chuyen_de/cd1/00_cd1_ctu_final_vi.md`
- `chuyen_de/cd2/00_cd2_ctu_final_vi.md`
- `thesis/chuong_*_vi.md`
- `scripts/fix_stat_notation.py`
- `scripts/fix_math_operators.py`
- `scripts/fix_inline_math.py`

*Example usage:*  
```bash
python scripts/fix_stat_notation.py thesis/chuong_3_vi.md
/normalize-stat-notation
```

---

### Build and Distribute DOCX/PDF Deliverables
**Trigger:** When manuscript or thesis source files are updated, or after major formatting/notation/voice passes.  
**Command:** `/build-deliverables`

1. Run the build script (`build_ctu_docx.sh`) to generate `.docx` and `.pdf` files from markdown sources.
2. Ensure LaTeX math renders as native equations in Word and PDF.
3. Place deliverables in `dist/downloads/` and relevant `dist/` subfolders.
4. Verify output for errors or missing glyphs.

*Files involved:*  
- `build_ctu_docx.sh`
- `dist/downloads/*.docx`
- `dist/downloads/*.pdf`
- `dist/chuyen_de_1/*.docx`
- `dist/luan_an_ctu/*.docx`

*Example usage:*  
```bash
sh build_ctu_docx.sh
/build-deliverables
```

---

### Reference List and Glossary Corrections
**Trigger:** When references are cited but missing from the reference list, or glossary metadata errors are found.  
**Command:** `/fix-references`

1. Identify missing or incorrect references/glossary entries.
2. Add or correct entries in the reference list and glossary.
3. Regenerate reference deliverables (`.docx`/`.pdf`) if needed.

*Files involved:*  
- `thesis/04_references_apa7.md`
- `thesis/09b_vn_term_glossary.md`
- `dist/downloads/04_references_apa7.docx`
- `dist/downloads/04_references_apa7.pdf`

*Example usage:*  
```bash
/fix-references
```

## Testing Patterns

- **Framework:** Unknown (not detected)
- **Test File Pattern:** Files matching `*.test.*`
- **Typical Structure:**  
  Test scripts are named using snake_case and include `.test.` in the filename.  
  *Example:*  
  ```
  fix_stat_notation.test.py
  ```

## Commands

| Command                    | Purpose                                                               |
|----------------------------|-----------------------------------------------------------------------|
| /transform-author-voice    | Apply deep author voice transformation to manuscripts                 |
| /standardize-terminology   | Standardize terminology and update glossary entries                   |
| /normalize-stat-notation   | Normalize statistical notation and math symbols                       |
| /build-deliverables        | Build and distribute DOCX/PDF deliverables from source manuscripts    |
| /fix-references            | Add/correct references and glossary entries, regenerate deliverables  |
```
# Changelog

All notable changes to this fork are documented here.

The format follows [Keep a Changelog](https://keepachangelog.com/en/1.0.0/).  
This project adheres to [Semantic Versioning](https://semver.org/).

---

## [5.1.0] — 2026-01-15

### Added
- `gui_app.py`: Full desktop GUI with progress bars, log output, and per-step controls
- `launch_app.py`: GUI launcher with automatic dependency installation
- `plot_citations.py`: Annual publication and citation trend charts
- `plot_types.py`: Document type distribution charts
- `advanced_search_engine.py`: Advanced keyword/field search across merged datasets
- `fix_for_vosviewer.py`: Post-processing step to ensure VOSviewer citation network compatibility (CR field reformatting, CRLF line endings)

### Changed
- `workflow.py` (`AIWorkflow`): Added `enable_plot` and `progress_callback` parameters; GUI progress integration
- Year filtering now applied at source (Step 1 & 2) before conversion — "year-filtering-first architecture"

### Fixed
- `enrichment.py`: Corrected C1 country extraction — country is now always the last independent comma-separated segment
- `wos_standardizer.py` / `batch.py`: Rate limit handling improved; 5-thread concurrency with 1.5 s inter-request delay to prevent 429 errors

---

## [5.0.0] — 2026-01-15 (Stable Release)

### Added
- `retraction_filter.py`: Automatic detection and removal of retracted publications via title keywords, document type, and optional CrossRef API
- `institutions.py` (`InstitutionCleaner`): Rule-based institution name normalization — merges parent/child names, removes noise, reduces unique institution count by ~20%
- `year.py` (`YearFilter`): Year range filtering for both WOS and Scopus files; generates per-year distribution report
- `records.py` (`RecordAnalyzer`): Statistical analysis — country, institution, author, year distribution with international collaboration mapping
- `config/institution_cleaning_rules_ultimate.json`: 200+ institution cleaning rules for common research institutions

### Changed
- Default model updated to `gemini-2.5-flash`
- Workflow report now includes year-filtering statistics and retraction count

---

## [4.5.2] — 2025-11-13

### Added
- `batch.py` (`EnhancedConverterBatchV2`): Batch concurrent Scopus→WOS converter with 5-thread pool and 20-item batch size
- `wos.py` (`WOSStandardizerBatch`): Batch variant of WOS standardizer with concurrent AI calls; separate methods for authors, countries, journals
- Exponential backoff in Gemini API calls: fast retries (5 s × 5) then slow retries (120 s × 7)

### Changed
- Author names now processed by rule-based algorithm only (no AI calls) — accuracy 97%+, zero API cost
- Batch processing reduces API calls from 7,000+ to ~297 for 660 records (95% reduction)

### Performance
- Processing time: 3 min vs. 70–80 min (20–30× speedup)
- Cost: ¥0.01–0.02 per 1,000 papers vs. ¥0.14

---

## [4.4.0] — 2025-11-11

### Added
- `merge_with_repair.py`: WOS format alignment step — Scopus-unique records automatically aligned to WOS standard formats for institutions, journals, countries, and authors
- Strict C1 country validation: `_is_valid_country()` excludes person names and state codes from country field

### Changed
- Merge priority: WOS records take full precedence; Scopus supplements only completely missing fields
- C1/C3 fields: strictly use WOS format when available

---

## [4.3.0] — 2025-11-11

### Added
- `wos_standardizer.py` (`WOSStandardizer`): AI-driven single-record standardizer for countries, journals, and author diacritics
- `enhanced_converter.py` (`EnhancedConverter`): Wraps base converter with WOS standardization pass
- `gemini_config.py` (`GeminiConfig`): Centralized Gemini API configuration with `from_params()`, `from_file()`, `is_enabled()`, `validate()`
- Persistent JSON cache for WOS standards (`config/wos_standard_cache.json`) and institution enrichment (`config/institution_ai_cache.json`)

### Changed
- Country standardization: 60 WOS-specific rules (e.g., `Peoples R China`, `Turkiye`, `England` vs. `UK`)
- Journal standardization: standard WOS abbreviation rules (237 journals cached after first run)

---

## [4.0.0] — 2025-11-10

### Added
- `gemini.py` (`GeminiEnricherV2`): Gemini AI institution enrichment with persistent database caching; batch mode processes 10 institutions per API call
- `enrichment.py` (`InstitutionEnricherV2`): Adapter class connecting GUI/workflow to GeminiEnricherV2
- `InstitutionDatabase`: JSON-based persistent cache with automatic backup on save
- Institution enrichment fields: state/province code, ZIP/postal code, department names, WOS-standard abbreviations

### Performance
- Cache hit rate: 0% (first run) → 98%+ (subsequent runs)
- First-run cost: ~¥0.14 per 1,000 papers
- Repeat-run cost: ~¥0 (fully cached)

---

## [3.0.0] — 2025-11-04 *(Base fork point)*

> This version corresponds to the state of the original upstream repository at fork time.  
> See [LeoMengTCM/Bibliometric-Data-Consolidation-Tool](https://github.com/LeoMengTCM/Bibliometric-Data-Consolidation-Tool) for the original changelog.

### Inherited from upstream
- `scopus.py`: Scopus CSV → WOS plain text conversion (44 fields)
- `language.py`: Language filtering with distribution report
- `merge_with_repair.py` (base): DOI + title/year/author deduplication
- `run_complete_workflow.py`: One-command pipeline
- `config/`: country_mapping.json, journal_abbrev.json, institution_config.json

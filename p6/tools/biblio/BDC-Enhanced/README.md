# Bibliometric Data Consolidation Tool — Enhanced Edition

> **Built upon** [LeoMengTCM/Bibliometric-Data-Consolidation-Tool](https://github.com/LeoMengTCM/Bibliometric-Data-Consolidation-Tool) (MIT License)

A comprehensive toolkit for researchers to merge, clean, and standardize bibliometric data from **Web of Science (WOS)** and **Scopus** into a unified, analysis-ready dataset compatible with VOSviewer, CiteSpace, and Bibliometrix.

---

## ✨ What's New in This Fork

This fork significantly extends the original tool with:

| Feature | Description |
|---|---|
| 🤖 **AI Institution Enrichment** | Gemini-powered completion of state/province codes, ZIP codes, and department info |
| ⚡ **Batch Concurrent Processing** | 5-thread concurrent API calls — 3 min for 660 records vs. 70+ min |
| 🌍 **WOS Format Standardization** | Country names (`China → Peoples R China`), journal abbreviations (`Journal of XXX → J XXX`) |
| 📅 **Year Range Filtering** | Filter records by custom year range (e.g., 2015–2024) |
| 🏛️ **Institution Name Cleaning** | Merge parent/child institutions, remove noise, standardize variants |
| 🖥️ **GUI Application** | Full desktop GUI (`gui_app.py`) for non-command-line users |
| 🔁 **Retraction Detection** | Automatic detection and removal of retracted publications |
| 📊 **Auto Chart Generation** | Publication trend and document-type charts via matplotlib |
| 💾 **Persistent AI Cache** | JSON-based database memory — zero cost on repeat runs |

---

## 📋 Overview

**Primary Use Case**: Combine Scopus and WOS exports for comprehensive bibliometric analysis.

**Processing Pipeline**:

```
wos.txt + scopus.csv
        ↓
[1] Year Range Filter (optional)        — Remove out-of-range records at source
        ↓
[2] Format Conversion + WOS Standardization  — Scopus CSV → WOS plain text
        ↓
[3] AI Institution Enrichment (optional) — Complete state/ZIP/department fields
        ↓
[4] Merge & Deduplicate                 — DOI-first, then title+year+author
        ↓
[5] Retraction Filter                   — Remove retracted publications
        ↓
[6] Language Filter                     — e.g., English-only
        ↓
[7] Institution Cleaning (optional)     — Normalize institution names
        ↓
[8] Statistical Analysis + Charts       — Reports for paper Methods section
        ↓
Final_Version.txt  +  analysis_report.txt
```

---

## 🚀 Quick Start

### 1. Install dependencies

```bash
pip install requests customtkinter pandas openpyxl matplotlib
```

> For macOS with system Python: add `--break-system-packages`

### 2. Configure your API key

Set your Gemini API key as an environment variable (required for AI features):

```bash
export GEMINI_API_KEY="your_api_key_here"
```

Or create a `.env` file:

```
GEMINI_API_KEY=your_api_key_here
```

### 3. Prepare your data

Place these two files in a folder (e.g., `data/`):
- `wos.txt` — exported from Web of Science
- `scopus.csv` — exported from Scopus (with all fields)

### 4. Run

**Option A — One-click GUI:**
```bash
python launch_app.py
```

**Option B — Full AI workflow (command line):**
```bash
python run_complete_workflow.py --data-dir "/path/to/data"
```

**Option C — With year filtering:**
```bash
python run_complete_workflow.py --data-dir "/path/to/data" --year-range 2015-2024
```

**Option D — Step by step:**
```bash
# Convert Scopus to WOS format
python enhanced_converter.py scopus.csv scopus_converted.txt

# Merge and deduplicate
python merge_with_repair.py wos.txt scopus_converted.txt merged.txt

# Filter language
python language.py merged.txt english_only.txt --language English

# Analyze
python records.py english_only.txt
```

---

## 📁 Project Structure

```
├── gui_app.py                    # Desktop GUI application
├── launch_app.py                 # GUI launcher with dependency check
├── run_complete_workflow.py      # One-click command-line workflow
│
├── src/bibliometrics/
│   ├── converters/
│   │   ├── scopus.py             # Scopus CSV → WOS format converter
│   │   └── batch.py              # Batch concurrent converter (v2, recommended)
│   ├── standardizers/
│   │   ├── wos.py                # WOS batch standardizer (countries, journals)
│   │   ├── gemini.py             # Gemini AI institution enricher
│   │   ├── enrichment.py         # Institution enrichment adapter
│   │   └── institutions.py       # Institution name cleaner
│   ├── filters/
│   │   ├── language.py           # Language filter
│   │   ├── year.py               # Year range filter
│   │   └── retraction_filter.py  # Retraction detector
│   ├── analysis/
│   │   ├── records.py            # Statistical analysis
│   │   ├── plot_types.py         # Document type charts
│   │   └── plot_citations.py     # Citation trend charts
│   ├── workflow.py               # AI-enhanced workflow orchestrator
│   └── gemini_config.py          # Gemini API configuration
│
├── enhanced_converter.py         # Standalone enhanced converter
├── wos_standardizer.py           # Standalone WOS standardizer
├── merge_with_repair.py          # Merge with format repair
├── fix_for_vosviewer.py          # Fix output for VOSviewer compatibility
├── advanced_search_engine.py     # Advanced search/filter tool
│
├── config/                       # Configuration files (JSON)
│   ├── wos_standard_cache.json   # AI cache: WOS format standards
│   ├── institution_ai_cache.json # AI cache: enriched institutions
│   ├── country_mapping.json      # Country name normalization rules
│   └── institution_cleaning_rules_ultimate.json
│
└── data/                         # Your data goes here
    ├── wos.txt
    └── scopus.csv
```

---

## ⚙️ Key Features

### AI-Powered WOS Standardization

Ensures full WOS format compliance across merged data:

- **Country names**: `China → Peoples R China`, `UK → England`, `Turkey → Turkiye`
- **Journal abbreviations**: `Journal of Clinical Oncology → J CLIN ONCOL`
- **Author diacritics**: `Pénault-Llorca → Penault-Llorca`
- **Persistent cache**: Results stored in `config/wos_standard_cache.json` — reused across runs at zero cost

### Batch Concurrent Processing

| Metric | v1 (sequential) | This fork (batch concurrent) |
|---|---|---|
| Time (660 records) | ~70–80 min | ~3 min |
| API calls | 7,000+ | ~297 |
| Cost | ¥0.14/1000 papers | ¥0.01–0.02/1000 papers |

### Intelligent Deduplication

1. **Primary**: DOI exact match (100% accuracy)
2. **Fallback**: Normalized title + publication year + first author

WOS records take priority in all merge conflicts; Scopus supplements missing fields only.

### Retraction Detection

Automatically identifies and removes retracted publications via:
- Title keyword detection (`retraction`, `withdrawn`, `erratum`, etc.)
- Document type field (`DT`) inspection
- Optional CrossRef API verification (`--online` flag)

---

## 🖥️ GUI Application

Launch the desktop interface for a point-and-click experience:

```bash
python launch_app.py
```

The GUI supports the full processing pipeline with progress indicators, log output, and configurable options for all major steps.

---

## 🔧 Configuration

### API Key

```bash
export GEMINI_API_KEY="your_key"
export GEMINI_API_URL="https://generativelanguage.googleapis.com/v1beta"  # optional override
```

### Gemini Model

Edit `gemini_config.py` to change the model:
```python
self.model = "gemini-2.5-flash"   # default
```

### Custom Institution Cleaning Rules

Edit `config/institution_cleaning_rules_ultimate.json` to add your own merge/normalize rules.

### Country Mapping

Edit `config/country_mapping.json` to add or override country name normalization.

---

## 📊 Output Files

| File | Description |
|---|---|
| `scopus_converted_to_wos.txt` | Scopus data converted to WOS format |
| `scopus_enriched.txt` | After AI institution enrichment |
| `merged_deduplicated.txt` | Full merged and deduplicated dataset |
| `english_only.txt` | Language-filtered dataset |
| `Final_Version.txt` | Final cleaned dataset (after institution cleaning) |
| `*_analysis_report.txt` | Statistical analysis report |
| `*_retraction_report.json` | Detected retracted records |
| `ai_workflow_report.txt` | Full workflow run summary |

---

## 🔬 Compatibility

Output files are compatible with:
- **VOSviewer** — use `fix_for_vosviewer.py` for optimal citation network parsing
- **CiteSpace**
- **Bibliometrix** (R package)
- Any tool accepting standard WOS plain text format

---

## 📦 Dependencies

| Package | Purpose | Required |
|---|---|---|
| `requests` | Gemini API calls | For AI features |
| `customtkinter` | GUI application | For GUI only |
| `pandas` | CSV processing | Recommended |
| `openpyxl` | Excel export | Optional |
| `matplotlib` | Chart generation | Optional |

Core processing (format conversion, merge, filter) runs on Python standard library only.

---

## 🙏 Credits & License

This project is built upon **[Bibliometric Data Consolidation Tool](https://github.com/LeoMengTCM/Bibliometric-Data-Consolidation-Tool)** by [LeoMengTCM](https://github.com/LeoMengTCM), released under the [MIT License](LICENSE).

This fork adds AI enrichment, batch processing, GUI, year filtering, retraction detection, and additional standardization capabilities.

**License**: MIT — see [LICENSE](LICENSE) for details.

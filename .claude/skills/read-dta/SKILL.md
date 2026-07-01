---
name: read-dta
description: Read, inspect, and extract data from Stata .dta files (including WBES raw survey data with ~340 variables and Stata variable/value labels). Use whenever you need to open a .dta file, list its columns and labels, preview rows, decode categorical value labels, compute descriptive statistics, or search for a variable across many .dta files. Backend is pyreadstat (preferred) with a pandas.read_stata fallback. Triggers: read dta, open dta, inspect dta, Stata file, .dta, WBES raw data, variable labels, value labels, đọc file dta, đọc dữ liệu Stata.
---

# Read .dta (Stata) files

Inspect and extract data from Stata `.dta` files. Optimised for World Bank
Enterprise Survey (WBES) raw country files used in the ICRV re-lock pipeline,
where each file carries ~340 columns plus Stata variable and value labels.

## Setup (once per session)

The helper prefers `pyreadstat` (exposes variable + value labels). If a fresh
container lacks it, install it — it falls back to `pandas.read_stata` otherwise:

```bash
pip install pyreadstat          # optional but recommended
python3 -c "import pandas; print(pandas.__version__)"   # pandas read_stata is the fallback
```

> Containers on Claude Code web are ephemeral. To make `pyreadstat` persist
> across web sessions, add `pip install pyreadstat` to the SessionStart hook
> (see the `session-start-hook` skill) or to `requirements.txt`.

## CLI — `scripts/read_dta.py`

| Command | What it does |
|---|---|
| `info <file...>` | rows × cols, file size, # value-labelled vars, backend |
| `cols <file...> [--grep REGEX]` | list columns + their Stata variable labels |
| `head <file...> [-n N] [--cols a,b]` | preview first N rows (optionally selected cols) |
| `labels <file> <column>` | decode value labels of a categorical column |
| `describe <file...> [--cols a,b]` | summary statistics |
| `find <dir> --grep REGEX` | locate a variable across every .dta in a folder |

File args accept globs (e.g. `data_wbes/raw_dta/*.dta`).

### Examples

```bash
# Schema overview of one country file
python3 scripts/read_dta.py info data_wbes/raw_dta/Lao-PDR-2024-full-data.dta

# Which files carry the FSTS export-share variables d3a/d3b?
python3 scripts/read_dta.py find data_wbes/raw_dta --grep '^d3[ab]?$'

# List all labour/employment vars with their labels
python3 scripts/read_dta.py cols data_wbes/raw_dta/Lao-PDR-2024-full-data.dta --grep '^l'

# Decode a categorical (e.g. legal status b1)
python3 scripts/read_dta.py labels data_wbes/raw_dta/Cambodia-2024-ISBS-full-data.dta b1

# Quick stats on selected variables
python3 scripts/read_dta.py describe data_wbes/raw_dta/*.dta --cols d3a,d3b,l1
```

## Reading inside a Python script

```python
import pyreadstat
df, meta = pyreadstat.read_dta("data_wbes/raw_dta/Lao-PDR-2024-full-data.dta")
meta.column_labels            # variable labels
meta.variable_value_labels    # {col: {code: label}}
# Fast schema-only (no data load):
_, meta = pyreadstat.read_dta(path, metadataonly=True)
# Memory-light column subset:
df, meta = pyreadstat.read_dta(path, usecols=["d3a", "d3b", "l1"])
```

Pandas fallback (no pyreadstat):

```python
import pandas as pd
df = pd.read_stata(path, columns=["d3a", "d3b"])          # column subset
chunks = pd.read_stata(path, iterator=True); first = chunks.read(1000)  # large files
```

## WBES notes (schema gotchas)

- **Schema generations differ.** PICS3 (2009-2013), Standardized (2014-2018),
  and BREADY/BEE (2019-2025) rename/move variables. A variable present in one
  wave may be absent or renamed in another — always `find` before assuming.
- **ISBS / informal-sector files** (e.g. `Cambodia-2024-ISBS`) and very old
  waves (e.g. `Korea-2005`) use reduced schemas and may lack `d3a/d3b`.
- **Core WBES variables**: `idstd` (firm id), `d3a/d3b` (direct/indirect export
  share → FSTS), `l1` (permanent workers), `d2` (sales), sampling weight `wt`.
- **Missing codes**: `-9` Don't know, `-7` N/A, `-8`/`-4` refusal/other — filter
  these before computing means.
- Do not commit raw `.dta` to git if they are restricted; keep them under
  `data_wbes/raw_dta/` (check `.gitignore`).

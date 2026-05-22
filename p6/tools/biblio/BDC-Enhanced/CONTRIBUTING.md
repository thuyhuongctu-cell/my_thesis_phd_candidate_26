# Contributing

Thank you for your interest in contributing! This project is a research tool used by bibliometricians and academics — contributions that improve reliability, accuracy, and usability are very welcome.

---

## Ways to Contribute

- **Bug reports** — especially edge cases in WOS/Scopus format parsing
- **Institution cleaning rules** — additions to `config/institution_cleaning_rules_ultimate.json`
- **Country / journal mappings** — corrections or additions to standardization tables
- **Performance improvements** — especially around API rate limiting and caching
- **Documentation** — clearer usage examples, translated guides

---

## Getting Started

```bash
# 1. Fork the repository on GitHub

# 2. Clone your fork
git clone https://github.com/YOUR_USERNAME/Bibliometric-Data-Consolidation-Tool.git
cd Bibliometric-Data-Consolidation-Tool

# 3. Install dependencies
pip install requests customtkinter pandas openpyxl matplotlib

# 4. Create a feature branch
git checkout -b feature/your-feature-name
```

---

## Code Style

- Python 3.6+ compatible
- Follow existing file structure: parsers, converters, standardizers, filters, analysis
- Add logging via the standard `logging` module — no bare `print()` in library code (CLI scripts are fine)
- Handle encoding explicitly: WOS files must be `utf-8-sig`
- Wrap API calls in try/except with appropriate retry logic (see `gemini.py` for the pattern)

---

## Submitting a Pull Request

1. Keep PRs focused — one feature or fix per PR
2. Update `CHANGELOG.md` under `[Unreleased]`
3. If adding new config options, include an `.example.json` template
4. Do not commit real API keys, user data files, or AI cache files (`.gitignore` covers these)

---

## Reporting Bugs

Please open an issue and include:
- Python version and OS
- A minimal sample of the input file that triggers the bug (anonymize if needed)
- The full error traceback
- What you expected vs. what happened

---

## License

By contributing, you agree that your contributions will be licensed under the [MIT License](LICENSE).

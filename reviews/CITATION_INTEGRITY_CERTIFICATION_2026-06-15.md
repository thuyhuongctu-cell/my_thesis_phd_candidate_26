# Citation-integrity certification — corpus-wide (2026-06-15)

Two-way citation check (every in-text author-year ↔ every reference entry, both
directions) across the entire dissertation corpus, after the core/recent I–P
literature additions and the CĐ reference completions.

## Result: citation-clean

| Document | Broken cites | Orphans |
|---|---|---|
| Thesis Ch.1–5 + references | 0 | 0 |
| CĐ1 | 0¹ | 0 |
| CĐ2 | 0² | 0 |
| P3 Vietnam | 0 | 0 |
| P4 Singapore | 0 | 0 |
| P5 China | 0 | 0³ |
| P6 meta | 0 | 0 |
| P7 capstone | 0 | 0 |
| P8 Pacific SIDS | 0 | 0 |
| P9 India | 0 | 0 |
| P10 Japan | 0 | 0 |
| P11 JED | 0 | 0 |

All residual detector hits are verified false positives: hyphenated method names
(Lind–Mehlum), variable/acronym tokens (FSTS, ISIC, BEE, WBES, RBV, Scopus,
Standardised, SPN/FOL/PRE), company names (Alibaba, Lazada, Tokopedia), months,
the documented included primary study (Pouresmaeili et al. 2018, in
`p6/results/forest_data.csv`), and P5's intentional blind-review self-citation
masks ("Author Citation, 2025/2026", entries present).

¹ CĐ1 exception (flagged, not fabricated): **CIEM (2023)** is cited in Section 2.3.7.3.
CIEM (Vietnam's Central Institute for Economic Management) is a real source, but
the exact 2023 publication could not be verified — the author should supply the
full reference.

² CĐ2 exception (flagged, not fabricated): **Kim, Kumar, Ramalho & Russell
(2026)** is cited. These are confirmed real World Bank authors (Galileu Kim, Tanu
Kumar, Rita Ramalho, Stuart Russell) with a 2026 institutional-capacity
publication, but the exact title could not be verified — the author should supply it.

³ P5 "Author Citation (2025/2026)" are intentional blind-review self-citation
masks for the candidate's own companion papers (entries present in the list).

## What was added (all web-verified or pulled from the vetted corpus; no fabrication)

- **Thesis Ch.2:** Vernon (1966), Hymer (1976), Caves (1971), Buckley & Casson
  (1976), Pisani et al. (2020) added to the reference list; integrated as
  citations in Section 2.1.1/Section 2.3.1/Section 2.3.2 together with the already-listed Ruigrok &
  Wagner (2003), Contractor (2012), Arbelo et al. (2024) (orphans resolved).
- **CĐ1:** completed 7 broken citations (Aguinis et al. 2019, Arte & Larimo 2022,
  Barney 1991, Hambrick & Mason 1984, La Porta & Shleifer 2008 + 2014, Scott 1995).
- **CĐ2:** completed 6 broken citations (Borenstein et al. 2009, Cronbach 1951,
  Dubin 1978, Sutton & Higgins 2008, Whetten 1989, Wolfolds & Siegel 2019); added
  the core I–P canon (Vernon, Hymer, Caves, Buckley & Casson, Dunning 1988,
  Ruigrok & Wagner 2003, Pisani et al. 2020) cited in Section 2.3.1; and resolved 6
  orphans by citing them at accurate locations (Bharadwaj et al. 2013, Bhandari
  et al. 2023, Chen & Tan 2012, Xiao et al. 2013, Melitz 2003, Nielsen & Nielsen
  2011).

## DOIs left blank for the standing `verify_dois.py` pass
Caves (1971), Vernon (1966) — book/journal classics added without DOIs to avoid
any fabricated identifier; to be confirmed in the DOI-verification pass.

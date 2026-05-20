#!/usr/bin/env python3
"""
36_l2_batch_screen_and_prefill.py
L2 batch screening + metadata pre-fill for auto-Y records.

For each auto-Y row (fulltext_screening_decision == 'Y'):
  1. Apply 5-question L2 inclusion check (title+abstract)
  2. Pre-fill icrv from country/region keywords
  3. Pre-fill dpl from study year
  4. Pre-fill fp_type from performance keywords
  5. Pre-fill internationalization_measure_guess
  6. Pre-fill model_type guess
  7. Downgrade to 'UNSURE_L2' if any hard L2 red flag found
"""

import csv, re
from datetime import datetime
from pathlib import Path
from collections import Counter

TODAY = datetime.now().strftime("%Y%m%d")

# ── L2 RED FLAGS (auto-downgrade from auto-Y to UNSURE_L2) ──────────────────
L2_RED_FLAGS = [
    (r"\b(country[- ]level|national[- ]level|macro[- ]level|aggregate[- ]level|"
     r"economy[- ]wide|sector[- ]level|industry[- ]level analysis)\b", "country_level"),
    (r"\b(qualitative|case study|grounded theory|interview|ethnograph)\b", "qualitative"),
    (r"\b(meta[- ]analy|systematic review|bibliometric)\b", "is_meta"),
    (r"\b(antecedents? of (export|internationali|FDI)|"
     r"determinants? of (export|internationali|FDI)|"
     r"drivers? of (export|FDI)|"
     r"what (determines?|drives?|explains?) (export|internationali))\b", "wrong_direction"),
    (r"\b(dissertation|thesis|working paper|conference paper|book chapter)\b", "not_peer_reviewed"),
    (r"\b(health|clinical|patient|medical|environmental compliance|carbon emission|"
     r"pollution abatement)\b", "oob"),
]

# ── ICRV MAPPING ────────────────────────────────────────────────────────────
ICRV_PATTERNS = [
    (r"\b(USA|United States|US firm|American firm|UK|Britain|Germany|Japan|Korea|"
     r"Singapore|Australia|Taiwan|Canada|France|Netherlands|Sweden|Switzerland|"
     r"Denmark|Finland|Norway|Austria|Belgium|OECD)\b", "1"),
    (r"\b(China|Chinese firm|Malaysia|Thailand|Brazil|Turkey|Mexico|South Africa|"
     r"Colombia|Peru|Argentina|Poland|Hungary|Czech|Russia|Romania)\b", "2"),
    (r"\b(Vietnam|India|Indonesia|Philippines|Pakistan|Bangladesh|Egypt|"
     r"Sri Lanka|Nigeria|Ghana|Kenya|Tanzania|Uganda|Ethiopia)\b", "3"),
    (r"\b(Saudi Arabia|UAE|Qatar|Kuwait|Bahrain|Oman|Nigeria|Kazakhstan|"
     r"Azerbaijan|Angola|Iraq)\b", "4"),
    (r"\b(Fiji|Samoa|Tonga|Vanuatu|Malta|Mauritius|Maldives|Barbados|"
     r"Trinidad|Jamaica)\b", "5"),
    (r"\b(Cambodia|Myanmar|Laos|Nepal|Mozambique|Mali|Niger|Burkina)\b", "6"),
    (r"\b(Asia.?Pacific|emerging (market|economy|economies)|"
     r"(developing|transition) (countr|econom)|cross.?country|multi.?country|"
     r"several countries|ASEAN|BRICS|BRICs)\b", "0"),
]

# ── FP_TYPE MAPPING ──────────────────────────────────────────────────────────
FP_PATTERNS = [
    (r"\b(return on asset|ROA)\b", "roa"),
    (r"\b(return on equity|ROE)\b", "roe"),
    (r"\b(return on sale|ROS|profit margin)\b", "ros"),
    (r"\b(Tobin.s Q|market.to.book|market value|stock return|shareholder)\b", "tobin_q"),
    (r"\b(sales growth|revenue growth|turnover growth)\b", "sales_growth"),
    (r"\b(productiv|efficiency|TFP|total factor)\b", "productivity"),
    (r"\b(market return|abnormal return|stock price|CAR)\b", "market_return"),
    (r"\b(performance|profitabilit|firm value)\b", "composite"),
]

# ── DOI_TYPE (internationalization measure) ──────────────────────────────────
DOI_PATTERNS = [
    (r"\b(FSTS|foreign sales|export (intensity|ratio)|export.to.sales)\b", "fsts"),
    (r"\b(entropy|transnationality index|TNI)\b", "entropy"),
    (r"\b(number of (countries|markets|nations)|geographic spread|breadth)\b", "n_countries"),
    (r"\b(FDI (stock|flow)|foreign direct investment (stock|flow))\b", "fdi_stock"),
    (r"\b(export dummy|export (status|participation)|exporter|"
     r"export.vs.non.export)\b", "export_dummy"),
    (r"\b(DOI|degree of internationali)\b", "composite"),
]

# ── MODEL TYPE ───────────────────────────────────────────────────────────────
MODEL_PATTERNS = [
    (r"\b(panel (data|regression)|fixed effect|random effect|GLS|GMM)\b", "panel"),
    (r"\b(OLS|ordinary least square|cross.sectional)\b", "ols"),
    (r"\b(logit|probit|binary|discrete choice)\b", "logit_probit"),
    (r"\b(structural equation|SEM|path analysis)\b", "sem"),
    (r"\b(hierarchical regression|moderated regression)\b", "hierarchical"),
]

def match_first(text, patterns, default=""):
    for pat, val in patterns:
        if re.search(pat, text, re.I):
            return val
    return default

def check_l2_red_flags(text):
    for pat, tag in L2_RED_FLAGS:
        if re.search(pat, text, re.I):
            return tag
    return None

def dpl_from_year(year_str):
    try:
        y = int(year_str)
        if y < 2000: return "1"
        if y <= 2009: return "2"
        return "3"
    except:
        return ""

def run():
    # Load tracker v3
    tracker_path = Path("p6/tools/results/fulltext_to_extraction_tracker_v3.csv")
    with open(tracker_path) as f:
        reader = csv.DictReader(f)
        fieldnames = reader.fieldnames
        rows = list(reader)

    # Load abstract map (seq → abstract text)
    ab_map = {}
    ab_path = Path("p6/tools/results/abstracts_20260520.csv")
    if ab_path.exists():
        with open(ab_path) as f:
            for r in csv.DictReader(f):
                ab_map[int(r['seq'])] = r.get('abstract', '').strip()

    # Process auto-Y new candidates
    stats = Counter()
    downgraded = []

    for row in rows:
        seq = int(row.get('seq', 0))
        if seq <= 435:
            continue
        if row.get('fulltext_screening_decision') != 'Y':
            continue

        title = row.get('title', '')
        abstract = ab_map.get(seq, '')
        year = row.get('year', '')
        text = f"{title} {abstract}"

        # 1. L2 red flag check
        flag = check_l2_red_flags(text)
        if flag:
            row['fulltext_screening_decision'] = 'UNSURE_L2'
            row['exclusion_reason'] = f"L2_redflag:{flag}"
            downgraded.append((seq, flag))
            stats['downgraded'] += 1
            continue

        # 2. Pre-fill ICRV (only if blank)
        if not row.get('icrv', '').strip():
            row['icrv'] = match_first(text, ICRV_PATTERNS, "")

        # 3. Pre-fill DPL (only if blank)
        if not row.get('dpl', '').strip():
            row['dpl'] = dpl_from_year(year)

        # 4. Pre-fill fp_type
        if not row.get('fp_type', '').strip():
            row['fp_type'] = match_first(text, FP_PATTERNS, "")

        # 5. Pre-fill internationalization_measure_guess
        if not row.get('internationalization_measure_guess', '').strip():
            row['internationalization_measure_guess'] = match_first(text, DOI_PATTERNS, "")

        # 6. Pre-fill model_type
        if not row.get('model_type', '').strip():
            row['model_type'] = match_first(text, MODEL_PATTERNS, "")

        # 7. Mark ready_for_r=0 until full-text confirmed
        if not row.get('ready_for_r', '').strip():
            row['ready_for_r'] = '0'

        stats['prefilled'] += 1

    # Write updated tracker
    with open(tracker_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        writer.writerows(rows)

    # Summary
    print(f"Auto-Y pre-fill complete — {TODAY}")
    print(f"  Processed (pre-filled):  {stats['prefilled']}")
    print(f"  Downgraded to UNSURE_L2: {stats['downgraded']}")
    if downgraded:
        print(f"\n  Top downgrade reasons:")
        rc = Counter(flag for _, flag in downgraded)
        for flag, cnt in rc.most_common(10):
            print(f"    {cnt:>4}  {flag}")

    # Final Y count
    y_final = sum(1 for r in rows if int(r.get('seq',0))>435
                  and r['fulltext_screening_decision']=='Y')
    unsure_l2 = sum(1 for r in rows if int(r.get('seq',0))>435
                    and r['fulltext_screening_decision']=='UNSURE_L2')
    manual = sum(1 for r in rows if int(r.get('seq',0))>435
                 and not r['fulltext_screening_decision'])

    print(f"\nUpdated tracker counts (new candidates only):")
    print(f"  Y (confirmed auto-include): {y_final}")
    print(f"  UNSURE_L2 (downgraded):     {unsure_l2}")
    print(f"  N_title + N_abstract:       {sum(1 for r in rows if int(r.get('seq',0))>435 and r['fulltext_screening_decision'] in ('N_title','N_abstract'))}")
    print(f"  Manual review needed:       {manual}")

    # ICRV fill stats
    y_rows = [r for r in rows if int(r.get('seq',0))>435 and r['fulltext_screening_decision']=='Y']
    icrv_filled = sum(1 for r in y_rows if r.get('icrv','').strip())
    dpl_filled  = sum(1 for r in y_rows if r.get('dpl','').strip())
    fp_filled   = sum(1 for r in y_rows if r.get('fp_type','').strip())
    print(f"\nPre-fill coverage on Y records ({len(y_rows)} rows):")
    print(f"  icrv filled:   {icrv_filled} ({icrv_filled/max(len(y_rows),1)*100:.0f}%)")
    print(f"  dpl filled:    {dpl_filled}  ({dpl_filled/max(len(y_rows),1)*100:.0f}%)")
    print(f"  fp_type filled:{fp_filled}  ({fp_filled/max(len(y_rows),1)*100:.0f}%)")

if __name__ == "__main__":
    run()

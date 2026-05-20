#!/usr/bin/env python3
"""
37_generate_extraction_queue.py
Generate a lean extraction queue for the 538 confirmed-Y papers.
Sorted: 1_DOI_FIRST then 2_NO_DOI_MANUAL, then by year desc.
Shows only the columns needed for manual extraction work.
"""

import csv
from datetime import datetime
from pathlib import Path

TODAY = datetime.now().strftime("%Y%m%d")

# Columns for the extraction queue (in display order)
QUEUE_COLS = [
    'seq', 'extraction_priority', 'icrv', 'dpl', 'fp_type',
    'internationalization_measure_guess', 'model_type',
    'title', 'authors', 'year', 'journal', 'doi', 'doi_link',
    'google_scholar', 'fulltext_screening_decision',
    'sample_size_n', 'reported_coefficient', 't_value', 'df_for_t',
    'p_value', 'converted_r', 'conversion_formula',
    'performance_measure_guess', 'country_guess', 'region_guess',
    'study_period_start', 'study_period_end', 'curve_type',
    'ready_for_r', 'notes_for_extractor', 'extracted_by',
]

def run():
    with open('p6/tools/results/fulltext_to_extraction_tracker_v3.csv') as f:
        reader = csv.DictReader(f)
        all_rows = list(reader)

    # Filter: new candidates that are confirmed Y
    y_rows = [r for r in all_rows
              if int(r.get('seq', 0)) > 435
              and r['fulltext_screening_decision'] == 'Y']

    # Sort: DOI_FIRST first, then year descending
    priority_order = {'1_DOI_FIRST': 0, '2_NO_DOI_MANUAL': 1, '': 2}
    y_rows.sort(key=lambda r: (
        priority_order.get(r.get('extraction_priority', ''), 2),
        -int(r.get('year', '0') or '0')
    ))

    # Write queue CSV
    out_path = Path(f'p6/tools/results/extraction_queue_{TODAY}.csv')
    with open(out_path, 'w', newline='', encoding='utf-8') as f:
        writer = csv.DictWriter(f, fieldnames=QUEUE_COLS, extrasaction='ignore')
        writer.writeheader()
        writer.writerows(y_rows)

    # Stats
    doi_first = sum(1 for r in y_rows if r.get('extraction_priority') == '1_DOI_FIRST')
    no_doi    = sum(1 for r in y_rows if r.get('extraction_priority') == '2_NO_DOI_MANUAL')
    icrv_filled = sum(1 for r in y_rows if r.get('icrv', '').strip())
    dpl_filled  = sum(1 for r in y_rows if r.get('dpl', '').strip())
    fp_filled   = sum(1 for r in y_rows if r.get('fp_type', '').strip())
    doi_meas    = sum(1 for r in y_rows if r.get('internationalization_measure_guess', '').strip())
    model_filled= sum(1 for r in y_rows if r.get('model_type', '').strip())

    print(f"Extraction queue generated: {out_path}")
    print(f"  Total Y papers: {len(y_rows)}")
    print(f"    1_DOI_FIRST:  {doi_first}")
    print(f"    2_NO_DOI_MANUAL: {no_doi}")
    print(f"")
    print(f"  Pre-filled metadata coverage:")
    print(f"    icrv:          {icrv_filled:>3}/{len(y_rows)} ({icrv_filled/len(y_rows)*100:.0f}%)")
    print(f"    dpl:           {dpl_filled:>3}/{len(y_rows)} ({dpl_filled/len(y_rows)*100:.0f}%)")
    print(f"    fp_type:       {fp_filled:>3}/{len(y_rows)} ({fp_filled/len(y_rows)*100:.0f}%)")
    print(f"    intl_measure:  {doi_meas:>3}/{len(y_rows)} ({doi_meas/len(y_rows)*100:.0f}%)")
    print(f"    model_type:    {model_filled:>3}/{len(y_rows)} ({model_filled/len(y_rows)*100:.0f}%)")
    print()

    # Show first 5 for review
    print("Top 5 extraction queue entries (DOI_FIRST):")
    for i, r in enumerate(y_rows[:5], 1):
        print(f"  [{i}] {r.get('title','')[:70]}")
        print(f"       year={r.get('year')} | icrv={r.get('icrv')} | dpl={r.get('dpl')} | fp={r.get('fp_type')} | doi={r.get('doi','')[:40]}")

if __name__ == "__main__":
    run()

#!/usr/bin/env bash
# assemble_submission_folder.sh
#
# Consolidate ALL final deliverables into one self-contained submission folder
# (dist/HO_SO_NOP/) organised by document type, plus a manifest (00_DANH_MUC.md)
# and a zip for handoff. Sources are the already-built DOCX/PDF in dist/downloads
# (rebuild those first via build_ctu_docx.sh) and the P6 OSF data/results.
#
# Usage: bash scripts/assemble_submission_folder.sh
set -euo pipefail
cd "$(dirname "$0")/.."
B="dist/HO_SO_NOP"; DL="dist/downloads"

# Rebuild content subfolders but preserve the hand-maintained manifest.
rm -rf "$B"/0[1-6]_*
mkdir -p "$B/01_LUAN_AN" "$B/02_TOM_TAT" "$B/03_CHUYEN_DE" \
         "$B/04_BAI_BAO_VI" "$B/05_BAI_BAO_EN" "$B/06_DU_LIEU_OSF_P6"

# 01 — dissertation (full + 5 chapters + references)
cp "$DL/LUAN_AN_FULL_vi.docx" "$B/01_LUAN_AN/"
for c in chuong_1_gioi_thieu chuong_2_tong_quan_tai_lieu chuong_3_phuong_phap \
         chuong_4_ket_qua chuong_5_ket_luan_de_xuat 04_references_apa7; do
  cp "$DL/$c.docx" "$DL/$c.pdf" "$B/01_LUAN_AN/"
done

# 02 — abstract (docx only)
cp "$DL/TOM_TAT_LUAN_AN_vi.docx" "$B/02_TOM_TAT/"

# 03 — chuyên đề
cp "$DL"/CD1_chuyen_de_1.{docx,pdf} "$DL"/CD2_chuyen_de_2.{docx,pdf} "$B/03_CHUYEN_DE/"

# 04 / 05 — component papers P3-P8 (VI + EN)
cp "$DL"/manuscripts_vi/*.docx "$DL"/manuscripts_vi/*.pdf "$B/04_BAI_BAO_VI/"
cp "$DL"/manuscripts_en/*.docx "$DL"/manuscripts_en/*.pdf "$B/05_BAI_BAO_EN/"

# 06 — P6 OSF publication data + results
cp p6/data/p6_study_database_osf.csv p6/data/p6_osf_dataset_README.md \
   p6/data/p6_doi_resolved.csv "$B/06_DU_LIEU_OSF_P6/"
cp p6/results/table1_baseline.csv p6/results/table2_icrv.csv p6/results/table3_cdai.csv \
   p6/results/table4_dpl.csv p6/results/table5_sensitivity.csv \
   p6/results/table_icrv_dropFR_sensitivity.csv p6/results/forest_data.csv \
   p6/results/p6_reproduction_validation.md "$B/06_DU_LIEU_OSF_P6/"

# NOTE: 00_DANH_MUC.md (manifest) is maintained by hand and not overwritten here.
echo "Assembled $(find "$B" -type f | wc -l) files into $B/ ($(du -sh "$B" | cut -f1))"

# zip for handoff (gitignored)
( cd dist && rm -f HO_SO_NOP.zip && zip -qr HO_SO_NOP.zip HO_SO_NOP )
echo "Zip: dist/HO_SO_NOP.zip ($(du -h dist/HO_SO_NOP.zip | cut -f1))"

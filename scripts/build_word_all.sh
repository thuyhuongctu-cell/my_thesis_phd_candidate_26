#!/usr/bin/env bash
# build_word_all.sh — Xuất bản Word (.docx) cho luận án + CĐ1 + CĐ2.
#
# Vì bìa/trang hội đồng/mục lục trong .md là raw-LaTeX (chỉ dành cho PDF),
# pandoc bỏ qua khi xuất .docx. Script này CHÈN bìa bằng openxml (canh giữa,
# in đậm) cho bản Word, dùng mẫu CTU templates/ctu_paper_reference.docx.
#
# Dùng:  bash scripts/build_word_all.sh
set -euo pipefail
cd "$(dirname "$0")/.."
TPL="templates/ctu_paper_reference.docx"
REF=(); [[ -f "$TPL" ]] && REF=(--reference-doc="$TPL")
mkdir -p dist/word

# Sinh một đoạn openxml canh giữa, in đậm. $1=text $2=half-point-size
ctr() { printf '<w:p><w:pPr><w:jc w:val="center"/><w:spacing w:after="120"/></w:pPr><w:r><w:rPr><w:b/><w:sz w:val="%s"/></w:rPr><w:t xml:space="preserve">%s</w:t></w:r></w:p>' "$2" "$1"; }
gap() { printf '<w:p><w:pPr><w:jc w:val="center"/></w:pPr><w:r><w:t> </w:t></w:r></w:p>'; }
pb()  { printf '<w:p><w:r><w:br w:type="page"/></w:r></w:p>'; }

build() {
  local name="$1"; shift
  local out="$1"; shift
  local cover="$1"; shift   # openxml cover string
  local TMP; TMP="$(mktemp -d)"; local M="$TMP/m.md"
  : > "$M"
  printf '```{=openxml}\n%s\n```\n\n' "$cover" >> "$M"
  for p in "$@"; do
    [[ -f "$p" ]] || { echo "WARN missing $p" >&2; continue; }
    cat "$p" >> "$M"
    printf '\n\n```{=openxml}\n%s\n```\n\n' "$(pb)" >> "$M"
  done
  pandoc -f markdown-yaml_metadata_block "${REF[@]}" --toc --toc-depth=3 \
    --resource-path=thesis:chuyen_de/cd1:chuyen_de/cd2:. "$M" -o "$out"
  echo "Built $out ($(stat -c%s "$out") bytes)"
  rm -rf "$TMP"
}

# ---------- Luận án ----------
LA_COVER="$(ctr 'BỘ GIÁO DỤC VÀ ĐÀO TẠO' 28)$(ctr 'TRƯỜNG ĐẠI HỌC CẦN THƠ' 28)$(gap)$(gap)$(ctr 'ĐỖ THÙY HƯƠNG' 28)$(gap)$(gap)$(ctr 'QUỐC TẾ HÓA VÀ HIỆU QUẢ HOẠT ĐỘNG KINH DOANH CỦA CÁC DOANH NGHIỆP Ở CHÂU Á' 40)$(gap)$(gap)$(ctr 'LUẬN ÁN TIẾN SĨ' 28)$(ctr 'NGÀNH QUẢN TRỊ KINH DOANH' 28)$(ctr 'MÃ SỐ: 9340101' 28)$(gap)$(gap)$(ctr 'CẦN THƠ, NĂM 2026' 28)$(pb)$(ctr 'BỘ GIÁO DỤC VÀ ĐÀO TẠO' 28)$(ctr 'TRƯỜNG ĐẠI HỌC CẦN THƠ' 28)$(gap)$(ctr 'ĐỖ THÙY HƯƠNG' 28)$(ctr 'MÃ SỐ NGHIÊN CỨU SINH: P1323001' 26)$(gap)$(ctr 'QUỐC TẾ HÓA VÀ HIỆU QUẢ HOẠT ĐỘNG KINH DOANH CỦA CÁC DOANH NGHIỆP Ở CHÂU Á' 40)$(gap)$(ctr 'LUẬN ÁN TIẾN SĨ' 28)$(ctr 'NGÀNH QUẢN TRỊ KINH DOANH' 28)$(ctr 'MÃ SỐ: 9340101' 28)$(gap)$(ctr 'NGƯỜI HƯỚNG DẪN KHOA HỌC' 26)$(ctr 'PGS.TS. PHAN ANH TÚ' 26)$(gap)$(ctr 'CẦN THƠ, NĂM 2026' 28)$(pb)"
build "Luận án" "dist/word/LUAN_AN_vi.docx" "$LA_COVER" \
  thesis/00_phan_dau_vi.md thesis/chuong_1_gioi_thieu_vi.md thesis/chuong_2_tong_quan_tai_lieu_vi.md \
  thesis/chuong_3_phuong_phap_vi.md thesis/chuong_4_ket_qua_vi.md thesis/chuong_5_ket_luan_de_xuat_vi.md \
  thesis/04_references_apa7.md thesis/phu_luc_A_hop_nhat_du_lieu_vi.md

# ---------- Chuyên đề 1 ----------
CD1_COVER="$(ctr 'BỘ GIÁO DỤC VÀ ĐÀO TẠO' 28)$(ctr 'TRƯỜNG ĐẠI HỌC CẦN THƠ' 28)$(ctr 'TRƯỜNG KINH TẾ' 28)$(gap)$(gap)$(ctr 'ĐỖ THÙY HƯƠNG' 28)$(ctr 'MÃ SỐ NGHIÊN CỨU SINH: P1323001' 26)$(gap)$(ctr 'CHUYÊN ĐỀ TIẾN SĨ SỐ 1' 28)$(gap)$(ctr 'THỰC TRẠNG VỀ HIỆU QUẢ HOẠT ĐỘNG KINH DOANH CỦA CÁC DOANH NGHIỆP Ở CHÂU Á' 36)$(gap)$(gap)$(ctr 'NGÀNH QUẢN TRỊ KINH DOANH' 28)$(ctr 'MÃ NGÀNH: 9340101' 28)$(gap)$(ctr 'NGƯỜI HƯỚNG DẪN KHOA HỌC' 26)$(ctr 'TS. NGUYỄN MINH CẢNH' 26)$(gap)$(ctr 'CẦN THƠ, NĂM 2026' 28)$(pb)"
build "Chuyên đề 1" "dist/word/CHUYEN_DE_1_vi.docx" "$CD1_COVER" chuyen_de/cd1/00_cd1_ctu_final_vi.md

# ---------- Chuyên đề 2 ----------
CD2_COVER="$(ctr 'BỘ GIÁO DỤC VÀ ĐÀO TẠO' 28)$(ctr 'TRƯỜNG ĐẠI HỌC CẦN THƠ' 28)$(ctr 'TRƯỜNG KINH TẾ' 28)$(gap)$(gap)$(ctr 'ĐỖ THÙY HƯƠNG' 28)$(ctr 'MÃ SỐ NGHIÊN CỨU SINH: P1323001' 26)$(gap)$(ctr 'CHUYÊN ĐỀ TIẾN SĨ SỐ 2' 28)$(gap)$(ctr 'XÂY DỰNG MÔ HÌNH NGHIÊN CỨU VỀ ẢNH HƯỞNG CỦA QUỐC TẾ HÓA ĐẾN HIỆU QUẢ HOẠT ĐỘNG KINH DOANH CỦA CÁC DOANH NGHIỆP Ở CHÂU Á' 34)$(gap)$(gap)$(ctr 'NGÀNH QUẢN TRỊ KINH DOANH' 28)$(ctr 'MÃ NGÀNH: 9340101' 28)$(gap)$(ctr 'NGƯỜI HƯỚNG DẪN KHOA HỌC' 26)$(ctr 'PGS.TS. PHAN ANH TÚ' 26)$(gap)$(ctr 'CẦN THƠ, NĂM 2026' 28)$(pb)"
build "Chuyên đề 2" "dist/word/CHUYEN_DE_2_vi.docx" "$CD2_COVER" chuyen_de/cd2/00_cd2_ctu_final_vi.md

echo "== Done. Word files in dist/word/ =="

# IMPLEMENTATION LOG — Luận án "Quốc tế hóa và hiệu quả doanh nghiệp ở Châu Á"

> Nhật ký quyết định triển khai (decision log). Cập nhật mỗi khi có thay đổi lớn về
> nội dung/số liệu. Mục đích: ghi nhớ **đã làm gì, vì sao, ở đâu** — để người duyệt
> và các session sau truy vết nhanh. Không thay cho `CANONICAL_NUMBERS.md` (số) hay
> `REPLICATION_STATUS.md` (trạng thái script).
>
> NCS: Đỗ Thùy Hương · GVHD: PGS.TS. Phan Anh Tú · Nhánh: `claude/phd-thesis-review-L9Gml` · PR #17

---

## 2026-06-19 — Loại Timor-Leste khỏi nhóm SIDS Thái Bình Dương

**Vấn đề.** `icrv_map()` xếp nhầm `TimorLeste → SIDS_small`, khiến P7 và bản P8 redesign
ước lượng nhóm SIDS có Timor (chiếm ~23% mẫu SIDS, cụm lớn nhất).

**Cơ sở loại (uy quyền).**
- **World Bank**: 11 Pacific Island Countries (FSM, Fiji, Kiribati, Marshall, Nauru, Palau,
  Samoa, Solomon, Tonga, Tuvalu, Vanuatu) — **không có Timor-Leste**.
- **UN Pacific SIDS (PSIDS)**: 14 nước (gồm PNG) — **không có Timor-Leste**.
- Timor-Leste là nền kinh tế Đông Á–Thái Bình Dương riêng (biển Timor/Đông Nam Á).

**Đã làm.**
- Sửa `scripts/cd1_descriptives_pipeline.py` → `DROP_LABELS` thêm `TimorLeste`; `GROUP_SIZE` SIDS 8→7.
- Chạy lại P7 từ raw `.dta` (`p7_run_50econ.py`, `p7_full_ladder.py`): khung **50→49 nền**,
  Nhóm VI = **7 nền Pacific** (Fiji, Kiribati, PNG, Samoa, Solomon, Tonga, Vanuatu).
- Dựng lại P8 từ raw: `p8/replication/build_and_run_p8_7pacific.py` → pin
  `p8/replication/data/p8_7pacific_pinned.csv` (N=1.450, 7 cụm).
- Propagate khắp luận án (VN+EN), slides, CANONICAL_NUMBERS, manuscript P8 + gói World
  Development, CD1/CD2. Rebuild PDF/docx.

**Số đã sửa (tái lập từ raw, loại Timor).**
| | Cũ (gồm Timor) | Mới |
|---|---|---|
| Khung | 50 nền, 88.869, 103 cặp | 49 nền, 87.987, 99 cặp |
| P7 M2 | N=81.022, β₁=1,189, β₂=−1,398, TP 51,5% | N=80.373, β₁=1,194, β₂=−1,404, TP 51,5% |
| P7 M5 | N=79.080, β₁=0,500, β₂=−0,721, TP 43,6% | N=78.445, β₁=0,503, β₂=−0,727, TP 43,5% |
| P8 SIDS | 8 nền, N=1.916 | 7 nền, N=1.450 |
| Lục địa Nhóm IV β₂ | −1,012 | −1,012 (không đổi) |

**Còn lại (cần NCS).** Tổng locked 96.415 (pool phân loại) và các **bảng mô tả 7 nền**
(Bảng 4.1/4.2 luận án + 2.3.x CD) chưa re-lock — ba pipeline cho ba số SIDS xung đột
(2.038 / 2.295 / 1.781 / 2.809). Tỷ lệ mô tả Nhóm VI để nguyên vintage + ghi chú; cần NCS
chỉ định pipeline chuẩn rồi regenerate đồng loạt.

---

## 2026-06-19 — Tái khung P8: "When the Inverted-U Dissolves" (dissolution thay vì đảo chiều)

**Quyết định.** Bỏ khung "đảo chiều chữ U xuôi/inversion" (over-claim). Headline **vững** =
**chữ U ngược TAN RÃ** (độ dốc null, độ cong không có ý nghĩa dưới wild-bootstrap). Độ cong
dương có điều kiện chỉ là **dấu hiệu gợi ý ở mức biên** (p_wild≈.06–.08), KHÔNG khẳng định
đảo chiều. **FIP = trường hợp giới hạn lý thuyết**, không phải hiệu ứng đo được vững.

**Cơ sở số (7 Pacific, lp_z, FE nền+năm, wild-cluster G=7).** M1 độ dốc −0,085 (p_wild=,66);
M2 độ cong +0,696 (,082); M3 +1,051 (,056); TCI +0,064 (,036). Hệ số −1,339 chỉ ở bản dựng
hạn chế 3 cụm (Fiji 2009, PNG 2015, Vanuatu 2009; N=209) — minh họa, nhạy cảm phiên bản dữ liệu.

**Đã propagate.** thesis §4.7 + abstract + Ch1/Ch5; manuscript `p8/p8_pacific_sids_redesigned_en.md`;
gói `p8/submission/world_development_redesign/`; hình `scripts/render_p8_dissolution_fig.py`;
slides + Q&A.

**Còn lại (cần NCS/GVHD).** Xác nhận khối tác giả/đơn vị + metadata nộp World Development;
GVHD duyệt định vị dissolution; các gói P8 cũ (ejdr/jid/world_development_package) đã bị
superseded bởi bản redesign.

---

## Tham chiếu nhanh

- **Số chuẩn (single source of truth):** `data_wbes/analysis/CANONICAL_NUMBERS.md`
- **Trạng thái script tái lập:** `REPLICATION_STATUS.md`
- **Pipeline P7 (raw→kết quả):** `dist/osf/P7_capstone/code/p7_run_50econ.py`, `scripts/p7_full_ladder.py`
- **Pipeline P8 7-Pacific:** `p8/replication/build_and_run_p8_7pacific.py`
- **Phân loại ICRV:** `scripts/cd1_descriptives_pipeline.py` (`icrv_map`, `DROP_LABELS`, `GROUP_SIZE`)
- **Raw `.dta`:** `data_wbes/raw_dta/` (override bằng env `WBES_RAW`)

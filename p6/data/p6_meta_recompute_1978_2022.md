# P6 Meta-Analysis — Strict 1978–2022 Recompute (Audit Trail)

**Ngày:** 2026-05-30
**Trigger:** User chỉ ra meta-analysis cover 1978–2022, không phải 1978–2026.
**Tình trạng:** Xấp xỉ 2-level (R không có trong môi trường remote); cần re-run full 3-level (`metafor::rma.mv`) trước khi propagate vào chương/tóm tắt/CĐ.

## Mâu thuẫn cần làm rõ

Header script `p6/scripts/p6_three_level_mara.R` ghi:
> "P6 UPDATED target: k=235 studies, K≈385 effect sizes (extended backward scan + 2022–2026 + scite.ai/Consensus screen)"

⇒ Design ban đầu **chủ ý** mở rộng 2022–2026; nay user revise về strict 1978–2022. Cần confirm policy trước khi propagate.

## So sánh số liệu

| Statistic | DB hiện tại (k=238) | Strict 1978–2022 (k=221) | Δ |
|---|---|---|---|
| k (studies) | 238 | **221** | −17 |
| K (effect sizes) | 288 | **271** | −17 |
| N (firm-obs cộng gộp) | 258,557 | **245,794** | −12,763 |
| I² (heterogeneity) | 87,8% | **≈ 85,2%** (xấp xỉ) | −2,6 pp |
| τ² | — | ≈ 0,0081 | — |
| Pooled r (random-effects) | — | ≈ 0,0728 | — |

> **Lưu ý quan trọng:** I² ≈ 85,2% là **xấp xỉ 2-level** (Fisher z + DerSimonian-Laird trên K=271 effect sizes, bỏ qua phân rã giữa-/trong-nghiên cứu). Full 3-level metafor `rma.mv(yi, vi, random=~1|study/effect)` sẽ cho I² level-2/level-3 chính xác + τ²_within/τ²_between + CI. Số 85,2% chỉ dùng để **ước lượng impact**, không dùng cho công bố.

## 17 entries bị loại (post-2022)

```
S127 (2 effects), S128, S183, S184, S185, S187, S188, S189,
S193, S194, S202, S207, S208, S213, S225, S230, S238
```

Đáng chú ý: **S188 (Do & Phan, 2025)**, **S189 (Do & Phan, 2026)** — kiểm tra xem có phải placeholder/forthcoming/own work.

## Filtered dataset

- `p6/data/p6_study_database_1978_2022.csv` — đã lọc, gồm tất cả rows có `year ≤ 2022` (271 rows).
- Schema giữ nguyên 18 cột gốc.
- Sẵn sàng cho R: `Rscript p6/scripts/p6_three_level_mara.R p6/data/p6_study_database_1978_2022.csv`

## Phạm vi propagation (chỉ thực hiện sau khi R cho con số chính xác)

**8 file, 38 chỗ trích cần update** sau khi có số mới:
- `thesis/chuong_1_gioi_thieu_vi.md`
- `thesis/chuong_2_tong_quan_tai_lieu_vi.md`
- `thesis/chuong_3_phuong_phap_vi.md`
- `thesis/chuong_4_ket_qua_vi.md`
- `thesis/chuong_5_ket_luan_de_xuat_vi.md`
- `thesis/tom_tat_noi_dung_vi.md`
- `chuyen_de/cd2/00_cd2_ctu_final_vi.md`
- `p6/21_p6_meta_vi.md`

Sau khi propagate phải rebuild tất cả deliverable (docx+pdf): chuong_1–5, tom_tat, cd2, LUAN_AN_FULL, p6_meta_vi → cập nhật `dist/HO_SO_NOP/`, `dist/downloads/`, `dist/luan_an_ctu/`, `dist/chuyen_de_1/`, `dist/submission/`.

## Next steps cần user quyết

1. **Xác nhận policy:** strict 1978–2022 (loại 17 entries) hay revise khác?
2. **R re-run:** chạy local `p6_three_level_mara.R` trên filtered CSV → trả về k/K/N/I²/τ²/pooled r/CI/moderator tests chính xác.
3. **Propagation:** Khi có số chính xác, tôi sẽ cập nhật 38 chỗ trích + rebuild deliverable.
4. **Đối chiếu kết quả moderation:** H1–H6 (ICRV, DAI, CDAI) có thể đổi sign/significance khi loại entries — cần kiểm tra cẩn thận.

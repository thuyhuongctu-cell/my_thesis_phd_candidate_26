# Ghi chú: thử ước lượng lại P7 với Japan — kết quả & quyết định

> Ngày 2026-06-11. Phản hồi yêu cầu "chạy lại data có Japan, chỉ đổi P7 nếu có".
> Script: `scripts/p7_reestimate_check.py` (tái lập được).

## 1. Việc đã thử
Tái lập gradient turning-point của P7 từ master pool (`p7_pooled_clean.csv`):
- DV = năng suất lao động **z-chuẩn hóa within country-year** (`lp_z`) — loại artifact tiền tệ (ln_labor_prod thô dao động -4,2 → 29,7 do nội tệ trộn).
- Mô hình: bậc hai FSTS + FSTS² + firm_age + **country FE + year FE**, theo từng nhóm ICRV và pooled.
- Turning point = −β₁/(2β₂).

## 2. Kết quả tái lập (KHÔNG khớp P7 đã công bố)

| Nhóm ICRV | TP tái lập (script) | TP P7 công bố (Ch4 §4.6) |
|---|--:|--:|
| Advanced innovation (I) | 79–84% | **≈28%** |
| Lower-mid transition (IV) | 36–50% | (trong dải) |
| Emerging (V) | 56–65% | ≈55% |
| SIDS (VI) | dạng ∪ (b₂>0) | âm đơn điệu (FIP) |
| **Pooled** | **52%** | **40,0% (M5)** |

→ Gradient **ngược chiều** (P7: tăng I→V; tái lập: I cao nhất) và SIDS sai dạng. Sai lệch lớn & có hệ thống.

## 3. Kết luận (ranh giới liêm chính)
Master pool + spec hợp lý **không tái lập** được P7. P7 gốc dùng các yếu tố tôi không có: hiệu chỉnh PPP, trọng số mẫu WBES, bộ biến kiểm soát/đặc tả tương tác, và quy ước turning-point riêng (trong do-file của nhóm tác giả). 

**Do đó KHÔNG thể tạo ra số "P7 + Japan" đáng tin** — bất kỳ hệ số nào tôi sinh ra sẽ mâu thuẫn với P7 thật trong luận án. **Không bịa số.** Việc cập nhật định lượng P7 phải do nhóm nghiên cứu chạy lại do-file gốc trên mẫu mở rộng.

## 4. Việc ĐÃ làm thay thế (trung thực)
- **Tác động đếm (chắc chắn)**: thêm Japan-2025 → khung phân loại 49 nền (91.864 DN) thành **50 nền (94.032 DN)**; Nhóm I 4.222 → 6.390.
- **Hồ sơ mô tả Japan** (xem `DATA_UPDATE_MANIFEST.md` §3): website 83,8%, DN ~50 tuổi, FSTS 4,1% (quốc tế hóa thấp).
- **Footnote minh bạch** đã thêm vào: Chương 4 §4.6.1 + CĐ1 (§2.3.2 ghi chú) — nêu rõ Japan + sóng mới lưu trữ cho vòng ước lượng lại; **kết quả P7 báo cáo giữ trên mẫu 49 nền đã khóa**.
- **Lập luận định tính** (do P7 dùng country FE): thêm Japan — một nền có biến thiên FSTS thấp — dự kiến không đổi turning point các nhóm khác, chỉ tinh chỉnh Nhóm I.

## 5. Khi nào số P7 mới đáng tin?
Khi nhóm tác giả chạy `do`-file P7 gốc trên bộ raw mở rộng (49 nền + Japan + sóng ≥2024 trong `data_wbes/raw_dta/`), rồi thay turning point/hệ số mới vào §4.6. Cho tới lúc đó, luận án giữ số P7 đã khóa.

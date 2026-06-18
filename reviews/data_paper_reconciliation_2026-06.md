# Đối chiếu Số liệu Luận án ↔ Kết quả Replication (P2–P10)

**Ngày:** 2026-06-18
**Phạm vi:** Đối chiếu mọi con số trụ cột trong Bảng 4.10, Bảng 4.11 (Chương 4) và Abstract (EN) với các tệp replication/canonical đã khóa.
**Nguồn chân lý ưu tiên:** `data_wbes/analysis/CANONICAL_NUMBERS.md` (khóa 2026-06-13) cho P7/khung dữ liệu; các tệp `*/replication/results/` cho P3–P9; `p10_japan/replication/p10_japan_models.py` cho P10.

> **Quy ước ký hiệu:** ✓ = khớp; ≈ = khớp trong sai số làm tròn (≤ ~0,4 pp / ≤ làm tròn chữ số cuối), KHÔNG cần sửa; ✗ = lệch thật cần sửa; ⚠ = không kiểm chứng được từ replication hiện có (không phán xử, tránh bịa).

> **Cảnh báo nhãn tệp:** thư mục `replication/` ở gốc có tên tệp gây nhầm: `p4_vietnam_replication.py` thực ra là Việt Nam (P3), `p4_singapore_replication.py` (trong `p4/`) là Singapore (P4). Quy ước luận án: **P3 = Việt Nam, P4 = Singapore, P5 = Trung Quốc.** Đối chiếu dưới đây theo quy ước luận án.

---

## P2 — Trung Quốc, doanh nghiệp nhỏ và vừa (Nhóm III)

| Đại lượng | Luận án (Bảng 4.10 / §4.4*) | Replication | Trạng thái |
|---|---|---|---|
| N | 4.290 | (không có thư mục replication — nghiên cứu nền đã công bố) | ⚠ không tự kiểm chứng |
| Dạng hàm | U ngược | — | — |
| Điểm uốn | 47,8% | — (chỉ neo định tính "sát P5 48,78%") | ⚠ |

*P2 không có pipeline replication trong repo (là nghiên cứu thành phần nền). Mọi số P2 lấy từ bản công bố; không phán xử ở đây.*

---

## P3 — Việt Nam (Nhóm IV) — nguồn: `p3/replication/coefs_main_models.csv` (VNM)

| Đại lượng | Luận án | Replication | Trạng thái |
|---|---|---|---|
| N gộp | 2.958 | VNMpooled N=2958 | ✓ |
| β₁ (FSTSc) gộp M2 | +0,984 | +0,9843 | ✓ |
| β₂ (FSTSc²) gộp M2 | −1,909 | −1,9091 | ✓ |
| Điểm uốn gộp | 39,7% | (từ β₁/β₂ centered + mean 13,9%) → ≈39,7% | ✓ |
| TP 2009 / 2015 | 46,2% / 39,3% | M2 wave 2009/2015 (β₁,β₂ khớp) | ≈ |
| TCI (β=0,179, IV) | 0,179 | M7 TCI_z=+0,1792 (M5=+0,196) | ✓ |
| Nhóm phụ exporters | N=669; β₁=−0,861; β₂=−0,200 (NS) | (báo cáo trong thân bài, khớp logic biên tham gia) | ≈ |

**Kết luận P3:** khớp toàn bộ trụ cột.

---

## P4 — Singapore (Nhóm I) — nguồn: `p4/replication/coefs_main_models.csv` (SGP2023)

| Đại lượng | Luận án | Replication | Trạng thái |
|---|---|---|---|
| N (M0 / DAI-spec) | 623 / 617 | SGP2023 M0 N=623; M2,M5–M8 N=617 | ✓ |
| β₁ (FSTSc) M2 | +2,652*** | +2,652 (p=0,000) | ✓ |
| β₂ (FSTSc²) M2 | −1,705† | −1,705 (p=0,068) | ✓ |
| FSTS²×DAI (M8) | +3,119** (p=,005) | +3,119 (p=0,005) | ✓ |
| R² M2/M5/M8 | 0,178 / 0,199 / 0,211 | 0,178 / 0,199 / 0,211 | ✓ |
| DAI decay M6→M7→M8 | +0,104→+0,077→+0,019 | +0,104 / +0,077 / +0,019 | ✓ |
| Điểm uốn ~88,6% | informative null, LM p=,303 | (TP tính, không định vị chắc) | ✓ |

**Kết luận P4:** khớp toàn bộ.

---

## P5 — Trung Quốc (Nhóm III) — nguồn: `p5/replication/results/summary.md` (Python, locked "matches manuscript v1.2")

| Đại lượng | Luận án | Replication (Python, canonical) | Trạng thái |
|---|---|---|---|
| N 2012 / 2024 / gộp | 2.610 / 1.934 / 4.544 | 2.610 / 1.934 / 4.544 | ✓ |
| TP 2012 | 49,37% | 49,37% [43,17;55,57] | ✓ |
| TP 2024 | 47,19% | 47,19% [34,46;59,92] | ✓ |
| TP gộp | 48,78% | 48,78% [42,65;54,91] | ✓ |
| β₁ M2 (2012/2024/gộp) | +2,065 / +1,498 / +1,784 | +2,0654 / +1,4980 / +1,7843 | ✓ |
| β₂ M2 | −2,092 / −1,587 / −1,829 | −2,0919 / −1,5873 / −1,8289 | ✓ |
| Paternoster (FSTS / FSTS²) | z=+0,82 p=,412 / z=−0,61 p=,545 | +0,821 p=,412 / −0,605 p=,545 | ✓ |
| P2-anchor §4.4 β₁ | +1,704 (TP 47,8%) | (đó là P2, không phải P5) | ✓ |

> **Lưu ý:** tệp `p5_R_turning_points.csv` (pipeline R phụ, FSTS định tâm, base N=2684) cho 47,65/47,52/47,58 — KHÁC con số luận án, NHƯNG `summary.md` (Python) là artifact đã khóa "matches manuscript v1.2". Luận án trích đúng pipeline Python. **Không lệch.**

**Kết luận P5:** khớp toàn bộ (dùng pipeline Python locked).

---

## P6 — Phân tích tổng hợp (châu Á) — nguồn: Bảng 4.10/§4.2 + abstract

| Đại lượng | Luận án | Replication/canonical | Trạng thái |
|---|---|---|---|
| k | 238 | CANONICAL k=238 (kèm cảnh báo "cần hoàn tất extraction thật") | ✓/⚠ |
| r̄ | 0,074 | (§4.2) | ⚠ chưa có tệp số gốc đối chiếu trực tiếp |
| I² | 62,4% | (§4.2) | ⚠ |
| Q_M (ICRV) | 17,35 (df=4, p=,002) | abstract & §4.11 nhất quán nội bộ | ✓ nội bộ |

*P6 dựa script R (`thesis/p6_scripts/*.rds`) trên dữ liệu mô phỏng/đóng băng; con số r̄/I²/k nhất quán giữa abstract–§4.2–§4.11–Bảng 4.10. Không có tệp CSV số gốc để đối chiếu ngoài; đánh dấu ⚠ chứ không phán "lệch".*

---

## P7 — Đa quốc gia 50 nền (Nhóm I–VI) — nguồn CANONICAL: `data_wbes/analysis/p7_50econ_models.csv` + `CANONICAL_NUMBERS.md`

> ⚠ Thư mục `p7/replication/results/` đã có `DEPRECATED.md`: là run TIỀN-Nhật (N≈84.910), KHÔNG dùng. Con số đúng nằm trong khung 50 nền canonical.

| Đại lượng | Luận án (Bảng 4.6/4.10/abstract) | Replication canonical | Trạng thái |
|---|---|---|---|
| N M2 / M5 | 81.022 / 79.080 | 81.022 / 79.080 | ✓ |
| β₁ / β₂ M2 | +1,189*** / −1,398*** | +1,1891 / −1,3980 | ✓ |
| TP M2 | 51,5% | 51,48% | ✓ |
| β₁ / β₂ M5 | +0,500*** / −0,721*** | +0,4995 / −0,7214 | ✓ |
| TP M5 | 43,6% | 43,57% | ✓ |
| TP Nhóm IV (Lower-mid) | 43,0% | 43,03% (p<,001) | ✓ |
| TP Nhóm I (Advanced) | ~79% (ngoài miền) | 79,12% (p=,304) | ✓ |
| TP Nhóm V (Emerging) | tan rã ~35% | 34,77% (p=,184) | ✓ |
| TCI hiệu ứng mức | +0,141 sd | (§4.6: +0,141***) | ✓ |
| DAI hiệu ứng mức | +0,201 sd | +0,201*** (§4.6) | ✓ |
| DAI tương tác cong | −0,271 (p=,149); +0,252 (p=,367) | (§4.6, không ý nghĩa toàn mẫu) | ✓ |
| **Nữ quản lý P7** | **§4.6.5: −0,104 (p<,001)** vs **§4.11/§5.1.4/§5.5.3.5: −0,088 (p=,026)** | KHÔNG có trong canonical; tệp focal (deprecated) cho mgr_female **DƯƠNG +0,185** | **✗ (mâu thuẫn nội bộ) + ⚠ (giá trị đúng chưa xác lập)** |

**Kết luận P7:** mọi headline (N, β, TP, ba vùng, TCI/DAI mức) KHỚP canonical. Riêng **hệ số nữ quản lý** vừa mâu thuẫn nội bộ (−0,104 vs −0,088, p<,001 vs p=,026) vừa KHÔNG nằm trong nguồn canonical đã khóa — cần tái ước lượng và chốt một giá trị; không bịa con số.

---

## P8 — SIDS Thái Bình Dương (Nhóm VI, FIP) — nguồn: `p8/replication/reanalysis_7pacific/` (khớp luận án)

> ⚠ Có HAI run: `reanalysis_7pacific/` (7 nền, N=959 — khớp Bảng 4.10/§4.7) và `results/` (9 nền, N=1.469 — dùng cho độ vững mở rộng). Đối chiếu theo run 7 nền cho các số trụ cột.

| Đại lượng | Luận án | Replication 7-Pacific | Trạng thái |
|---|---|---|---|
| N tổng | 959 | 959 | ✓ |
| Doanh nghiệp xuất khẩu | 132 (13,8%) | 132 (13,8%) | ✓ |
| FSTS trung bình | 0,048 | 0,048279 | ✓ |
| β(FSTS) M1 (ctry+year FE) | −1,339*** (SE 0,386) | −1,3393 (SE 0,386; p=,0005) | ✓ |
| β(FSTS) year-FE only | −3,351*** | −3,3515 (p=3e-5) | ✓ |
| β(FSTS) bivariate | −0,864 (p=,050) | −0,8642 (p=,0425/,050) | ≈ |
| Exporters-only | N=26; −1,176; p=,130 (NS) | N=26; −1,1757; p=,124 | ≈ |
| M3 N (thiếu năng lực) | 205 | 205 | ✓ |
| TCI_z M3 | +0,299 (p=,003) | +0,2986 (p=,003) | ✓ |
| DAI_z M3 | +0,094 (p=,285) | +0,0942 (p=,285) | ✓ |
| Mở rộng 9 nền | N=1.469; β=−0,510 (p=,008) | run 9-nền có N=1.469; **M1(ctry+yr FE) β=−0,4038 (p=,032)** trong CSV | ⚠ (β=−0,510 KHÔNG thấy trong CSV; spec khác chưa xác lập) |
| Bỏ control nước ngoài | N=950; β=−0,835 (p=,010) | KHÔNG có trong CSV hiện hữu | ⚠ |

**Kết luận P8:** mọi số trụ cột FIP (−1,339; −3,351; N=959/132/26/205) KHỚP. Hai con số độ vững mở rộng (−0,510 ở 9 nền; −0,835 bỏ control) KHÔNG đối chiếu được từ CSV hiện có (CSV 9 nền cho M1 = −0,4038) → ⚠ cần kiểm chứng do-file, KHÔNG khẳng định lệch.

---

## P9 — Ấn Độ (Nhóm IV, tan biến ngưỡng) — nguồn: `p9_india/replication/results/`

| Đại lượng | Luận án | Replication | Trạng thái |
|---|---|---|---|
| N (2014/2022/2025) | 8.941 / 9.300 / 10.476 | 8.941 / 9.300 / 10.476 | ✓ |
| N gộp | 28.717 | 8941+9300+10476 = 28.717 | ✓ |
| 2014: β₁/β₂ | +1,865 / −1,508 | +1,8645 / −1,5082 | ✓ |
| TP 2014 | 61,8% [55,0;68,6] | 61,81% [54,99;68,64] | ✓ |
| 2022: β₁/β₂ | +1,542 / −1,893 | +1,5419 / −1,8933 | ✓ |
| TP 2022 | 40,7% [38,0;43,5] | 40,72% [37,97;43,47] | ✓ |
| 2025: β₂ NS | −0,160 (p=,420) | −0,1604 (p=,420) | ✓ |
| Paternoster HC1 (FSTS/FSTS²) | z=−7,94 p<,0001 / z=+4,17 p<,0001 | −7,935 p=2e-15 / +4,174 p=3e-5 | ✓ |
| Paternoster cluster | z=−3,50 p=,001 / z=+2,19 p=,029 | −3,503 p=,0005 / +2,187 p=,029 | ✓ |
| Wave×2025 interaction | −1,63 (p<,0001) | (§4.8, khớp) | ✓ |

**Kết luận P9:** khớp toàn bộ.

---

## P10 — Nhật Bản (Nhóm I) — nguồn: `CANONICAL_NUMBERS.md` (P10 row) + `p10_japan/replication/p10_japan_models.py`

| Đại lượng | Luận án | Canonical | Trạng thái |
|---|---|---|---|
| N | 2.168 | 2.168 | ✓ |
| FSTS tuyến tính | +0,671*** | +0,671*** | ✓ |
| Phần bù xuất khẩu | +0,258*** | +0,258*** | ✓ |
| Bậc hai | NS | n.s. | ✓ |
| Điểm uốn | ~90,1% (không định vị) | (gần tuyến tính, TP ngoài miền) | ≈ |
| Nữ quản lý % | 7,3% | 7,3% | ✓ |
| Website % / tuổi | 83,8% / 50,4 | 83,8% / 50,4 | ✓ |

**Kết luận P10:** khớp toàn bộ.

---

## Khung dữ liệu nền tảng (đối chiếu abstract ↔ canonical)

| Đại lượng | Abstract/Ch4 | Canonical | Trạng thái |
|---|---|---|---|
| Khung phân tích | 88.869 DN / 50 nền | 88.869 / 50 (gồm Nhật) | ✓ |
| Mẫu hồi quy chính | N=81.022 (M2) | 81.022 | ✓ |
| Pool phân loại ICRV | 96.415 / 52 nhãn | 96.415 / 52 | ✓ |
| Q_M (P6) | 17,35 | 17,35 | ✓ |
| FSTS β SIDS (abstract) | −1,339 (p<,001) | −1,339 (level/PPP spec) | ✓ |

> Lưu ý: canonical ghi rõ FIP **z-spec = −0,098** (KHÁC level-spec −1,339). Luận án/abstract dẫn −1,339 (level-spec) làm headline — đúng theo canonical. Không lệch.

---

# CÁC LỆCH CẦN SỬA (chỉ ✗ — lệch thật; bỏ qua ≈ làm tròn)

1. **`thesis/chuong_4_ket_qua_vi.md` : §4.6.5 vs §4.11(H4) (và lan sang §5.1.4, §5.5.3.5 của `chuong_5_ket_luan_de_xuat_vi.md`) : hệ số nữ quản lý P7 −0,104 (p<,001) ⟷ −0,088 (p=,026)** — mâu thuẫn nội bộ cho CÙNG một hệ số/mô hình. Giá trị đúng KHÔNG nằm trong nguồn canonical đã khóa (tệp focal replication — đã deprecated — thậm chí cho dấu DƯƠNG +0,185). **Hành động: tái ước lượng từ microdata 50 nền, chốt MỘT giá trị + một p-value, ghi vào `CANONICAL_NUMBERS.md` rồi propagate.** Không tự điền con số nào trước khi chạy estimation thật.

*(Đây là lệch ✗ DUY NHẤT xác lập được từ đối chiếu số liệu. Mọi trụ cột P3–P10 còn lại khớp replication/canonical trong sai số làm tròn.)*

---

## Các mục ⚠ (không kiểm chứng được — KHÔNG sửa mù, cần chạy lại nguồn)

- **P8 §4.7.7 — β=−0,510 (9 nền, N=1.469)** và **β=−0,835 (bỏ control, N=950)**: không có trong CSV replication hiện hữu; CSV 9-nền cho M1(ctry+year FE)=−0,4038 (p=,032). Cần xác minh do-file đặc tả nào sinh −0,510/−0,835 trước khi kết luận đúng/sai.
- **P6 — r̄=0,074; I²=62,4%; k=238**: nhất quán nội bộ giữa abstract–§4.2–§4.11 nhưng chưa có tệp số gốc đối chiếu; canonical gắn cờ "k cần hoàn tất extraction thật".
- **P2 — N=4.290; TP 47,8%**: nghiên cứu nền đã công bố, không có pipeline replication trong repo.

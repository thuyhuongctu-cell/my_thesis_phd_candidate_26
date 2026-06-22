# Rà soát nội dung luận án — Báo cáo nhất quán nội tại (2026-06-22)

**Phạm vi:** `thesis/chuong_1..5`, phụ lục A/B, `11_dissertation_positioning`, `00_phan_dau`,
đối chiếu chéo với các nghiên cứu thành phần P1–P10 và các tệp khóa số canonical.
**Phương pháp:** ba lượt quét song song — (i) điểm uốn & hệ số, (ii) cỡ mẫu/N & số học cộng dồn,
(iii) hệ giả thuyết & tham chiếu chéo/đánh số bảng-hình.

---

## 0. Tóm tắt điều hành

| # | Hạng mục | Mức độ | Trạng thái |
|---|----------|--------|-----------|
| 1 | Bảng 4.1/4.2 drift (cũ: cộng 98.097 ≠ 96.415; lệch CSV; thiếu China-2012) | 🔴→🟢 | ✅ **Đã tái lập Bảng 4.1+4.2 từ script canonical** (gồm China-2012); n = LP-valid 84.045/49 nền. Còn: **sync CĐ1** (xem §11) |
| 2 | Nhãn năm hội nghị: "ICBEF 2025" (ch3 ×2) vs "ICBEF 2024" (ch4/ch5/DMTL) | 🟡 Nhẹ | ✅ **Đã sửa → 2024** |
| 3 | TCI Trung Quốc 2012: thân luận án ghi "+0,26" vs bài P5 "+0,28" | 🟡 Nhẹ | ✅ **Đã sửa → +0,28** (ch4:668, ch5:139) |
| 4 | ~~H1c vắng trong Bảng 2.2~~ → **KHÔNG phải lỗi**: H1c là giả thuyết con (lồng dưới H1/H6), cố ý không nằm trong Bảng 2.2 theo ghi chú `ch2:314` | ⚪ Bác bỏ flag | ✅ Đã rà lại — đúng thiết kế |
| 5 | Tiêu đề ch5 §5.1.2 "Xác nhận H2" mâu thuẫn chính thân bài ("một phần") và ch4 §4.11 | 🟠 Trung bình | ✅ **Đã sửa → "Xác nhận một phần H2"** |
| 5b | Tiêu đề ch5 §5.1.1 "Xác nhận H5" vs ch4 §4.11 "Xác nhận một phần" | 🟠 Trung bình | ✅ **Đã sửa → "một phần"** (rà soát kết quả thực P6/P7, xem §10) |
| 6 | H6 chỉ kết luận ở ch4 §4.11, không nhắc lại trong ch5 | 🟡 Nhẹ | ✅ **Đã thêm đoạn H6 vào ch5 §5.1.6** |
| 7 | Bảng 2.1 / Bảng 2.2 đánh số ngược thứ tự xuất hiện (ch2 §2.5.8–2.5.9) | 🟡 Nhẹ | ✅ **Đã hoán đổi** (2.1=giả thuyết, 2.2=ánh xạ) |
| 8 | **4 trích dẫn mồ côi** (ch1–3 có trong văn nhưng thiếu mục tài liệu): Contractor et al. 2003, Hitt et al. 2006, Hunter & Schmidt 2004, Peng 2001 | 🟠 Trung bình | ✅ **Đã bổ sung 4 mục vào `04_references_apa7.md`** |

**Kết luận chung:** Bộ số kinh tế lượng cốt lõi (điểm uốn P3/P4/P5/P7/P9/P10, hệ số TCI/DAI,
meta P6) **nhất quán** xuyên năm chương và khớp tệp khóa canonical. Phân biệt 43,6% (toàn mẫu M5)
vs 43,0% (Nhóm IV) là **đúng**, không phải lỗi. Mọi tham chiếu chéo `Mục/Bảng/Hình` đều phân giải
được (không có tham chiếu treo). Vấn đề số liệu lớn nhất (**Bảng 4.1/4.2**) **đã được tái lập theo
data canonical** ở §11 (gồm China-2012); việc còn lại chỉ là đồng bộ CĐ1.

---

## 1. 🔴→🟢 Bảng 4.1 — n các nhóm ICRV không cộng về tổng, và lệch CSV canonical

> **✅ ĐÃ XỬ LÝ ở §11** (lượt 2: tái lập Bảng 4.1+4.2 từ script canonical, gồm China-2012). Phần
> §1.1–§1.4 dưới đây giữ lại làm **chẩn đoán gốc** để truy vết, không còn là vấn đề mở.

**Vị trí:** `thesis/chuong_4_ket_qua_vi.md:25–31` (và caption :21, :35).

### 1.1 Lỗi cộng dồn nội tại
```
Nhóm I 6.390 + II 2.269 + III 17.905 + IV 50.926 + V 18.569 + VI 2.038 = 98.097
Tổng ghi trong bảng (:31) ................................................ 96.415
Lệch ..................................................................... +1.682
```
Hàng "Tổng (phân loại ICRV) = 96.415" tự mâu thuẫn với chính cột n của bảng.

### 1.2 So với nguồn canonical `data_wbes/analysis/cd1_relock_descriptives_by_icrv.csv`
| Nhóm | Bảng 4.1 | CSV canonical | Chênh | Ghi chú |
|------|---------:|--------------:|------:|---------|
| I (Adv. đổi mới) | 6.390 | 4.222 | +2.168 | = đúng Nhật Bản 2025 (4.222 + 2.168) → bản **gồm Nhật** |
| II (Adv. tài nguyên) | 2.269 | 2.269 | 0 | khớp |
| III (Trung bình cao) | 17.905 | 13.993 | **+3.912** | **không giải thích được** (nghi vấn vintage cũ/khác) |
| IV (Chuyển đổi TB-thấp) | 50.926 | 50.926 | 0 | khớp |
| V (Đang nổi) | 18.569 | 18.569 | 0 | khớp |
| VI (SIDS) | 2.038 | 1.885 | +153 | lệch |
| **Tổng** | **98.097** | **91.864** | | cả hai ≠ 96.415 |

**Chẩn đoán:** Bảng 4.1 là bản **trộn nhiều vintage** — ba nhóm (II, IV, V) khớp CSV; nhóm I đã
cập nhật gồm Nhật Bản; nhóm III và VI mang số khác (drift). Tổng ghi 96.415 là **pool khóa canonical**
(xuất hiện ở `scripts/build_pooled_dataset.py:118`, `check-consistency.py`, phụ lục, slide) nhưng
**không** bằng tổng cột (98.097) lẫn tổng CSV (91.864).

**Vì sao KHÔNG tự sửa:** Bản phân rã per-nhóm đúng cộng về 96.415 nằm trong **master file** mà NCS
giữ (xem `scripts/build_pooled_dataset.py:26–28`: "official locked pool sizes ... reported from the
master file"; script không tái lập được từ raw subset trong repo). Sửa tay = bịa số. Hơn nữa hạng mục
này **gắn với lần rebuild P7 China-2012 authoritative** mà NCS đã giữ lại cho mình
(`p7/P7_CHINA2012_REBUILD_HANDOFF.md`) — nhóm III (gồm Trung Quốc) chính là nhóm lệch lớn nhất.

### 1.3 Lớp mô tả ICRV tồn tại ở BA vintage không hòa giải (mở rộng từ rà soát CĐ1)

Đối chiếu thêm với Chuyên đề 1 (`chuyen_de/cd1/00_cd1_ctu_final_vi.md:412–418`, lặp ở `:1091–1097`)
cho thấy bảng phân rã ICRV xuất hiện ở **ba phiên bản số khác nhau, và mỗi phiên bản đều không tự
cộng về tổng của chính nó**:

| Nhóm | CĐ1 (Bảng 2.3.2.1) | Thesis Bảng 4.1 | CSV canonical |
|------|-------------------:|----------------:|--------------:|
| I | 6.390 | 6.390 | 4.222 |
| II | 2.231 | 2.269 | 2.269 |
| III | 13.993 | 17.905 | 13.993 |
| IV | 45.003 | 50.926 | 50.926 |
| V | 18.589 | 18.569 | 18.569 |
| VI | 1.781 | 2.038 | 1.885 |
| **Cộng cột** | **87.987** | **98.097** | **91.864** |
| **Tổng ghi** | **88.869** | **96.415** | (— không ghi) |
| **Lệch** | **−882** | **+1.682** | — |

- CĐ1 chỉ khớp thesis ở Nhóm I (6.390); chỉ khớp CSV ở Nhóm III (13.993); mọi nhóm khác lệch cả hai.
- **CĐ1 cũng tự mâu thuẫn**: cột cộng 87.987 ≠ tổng ghi 88.869 (−882).
- Thêm: CĐ1 đếm SIDS theo **ba số** thay nhau cho cùng một dòng — 2.295 (8 nền mở rộng), 1.781
  (7 nền chính), còn CSV ghi 1.885 (`cd1:404,417`; CSV).

**Hệ quả:** đây không phải một lỗi cộng đơn lẻ ở Bảng 4.1 mà là **drift toàn lớp mô tả ICRV** — ba
nguồn (CĐ1, thesis, CSV) phản ánh ba lần cắt dữ liệu khác nhau (khác khung 50/52 nền, khác có/không
Nhật Bản, khác đợt China). Cần **một lần tính lại authoritative duy nhất** rồi đồng bộ ngược ra cả
CĐ1 lẫn thesis.

### 1.4 Bảng 4.2 (%) — CĐ1 ↔ thesis khớp tuyệt đối, nhưng cột website lệch CSV

Bảng 4.2 (`chuong_4:63–68`) trùng khít CĐ1 Bảng 2.3.4.1 (`cd1:519–524`) trên cả 6 nhóm × 5 cột ✅.
Tuy nhiên **cột website** của cặp CĐ1↔thesis lệch CSV canonical ở hai nhóm rõ nhất: Nhóm I 69,2 vs
CSV 61,7; Nhóm VI 41,5 vs CSV 45,6 (các nhóm còn lại ≈). Tức Bảng 4.2 nhất quán nội bộ nhưng thuộc
**cùng một vintage cũ** với phần n ở §1.3 — củng cố chẩn đoán cần tính lại đồng bộ.

**Khuyến nghị:** Trong lần rebuild canonical, xuất lại **đồng thời** (i) bảng phân rã n per-nhóm và
(ii) bảng % Bảng 4.2 trên **đúng khung pool 96.415 (gồm Nhật Bản)**, kiểm tra cộng cột = 96.415,
rồi thay cả Bảng 4.1 + 4.2 trong thesis **và** Bảng 2.3.2.1 + 2.3.4.1 trong CĐ1 cho khớp một vintage.

---

## 2–3. ✅ Đã sửa trong lượt này

- **ICBEF 2025 → 2024** (`chuong_3:35`, `chuong_3:37`): danh mục công bố (`00_phan_dau:216`,
  "Sixth ICBEF 2024") và ch4/ch5 đều ghi 2024 cho cùng bản nền k=113/K=200 → ch3 là chỗ sai năm.
- **TCI Trung Quốc 2012 +0,26 → +0,28** (`chuong_4:668`, `chuong_5:139`): bài P5
  (`p5/p5_china_en_clean.md:26,42`) ghi β_z = +0,28 (2012) → +0,43 (2024). Cận trên +0,43 đã đúng;
  chỉ cận dưới lệch. Không ảnh hưởng kết luận.

---

## 4. ⚪ H1c — flag ban đầu đã RÚT (đúng thiết kế, không phải lỗi)

- Lượt rà soát đầu nghi H1c "vắng trong Bảng 2.2". Đọc lại ghi chú `ch2:314` cho thấy đây là **cố ý**:
  hệ giả thuyết trọng tâm gồm H1–H6 + điều kiện biên H1b; H1c (cùng H2b, H4a–H4b, E1a–E1b) là
  **giả thuyết con** (sub-hypothesis) "lồng dưới H1 và H6", nên **không** liệt kê trong Bảng 2.2.
- H1c vẫn được phát biểu (`ch2:238`) và kết luận có nhãn (`ch4:688`). Việc `ch5 §5.1.6` bàn hiện
  tượng P9 không gắn nhãn "H1c" là chấp nhận được. **Tùy chọn (rất nhẹ):** thêm "(kiểm định H1c)"
  vào §5.1.6 cho dễ truy vết — không bắt buộc. **KHÔNG** thêm dòng H1c vào Bảng 2.2.

## 5. Tiêu đề "Xác nhận H2 / H5" (ch5) vs "Xác nhận một phần" (ch4 §4.11)

- **H2 — ✅ đã sửa:** tiêu đề `ch5 §5.1.2` đổi "Xác nhận H2" → "**Xác nhận một phần H2**". Đây là
  sửa an toàn vì chính thân bài §5.1.2 đã viết "H2 được xác nhận một phần", và khớp `ch4:682`.
- **H5 — ⏳ cần NCS quyết (5b):** tiêu đề `ch5 §5.1.1` ghi "Xác nhận H5" còn `ch4:685` ghi "Xác nhận
  **một phần**" (vì định hướng phổ thể chế E1a/E1b chưa xác nhận do *k*=3 ở bin Frontier). Khác H2,
  ở đây **thân bài ch5 cũng khẳng định mạnh** ("xác nhận H5… theo cách thuyết phục nhất"), nên đây là
  **mâu thuẫn liên chương về lập trường**, không phải lệch tiêu đề–thân bài. Hai lựa chọn:
  - (a) Hạ tiêu đề + một mệnh đề ở §5.1.1 xuống "một phần" để khớp ch4 (nhất quán, thận trọng); hoặc
  - (b) Giữ "Xác nhận H5" nhưng sửa `ch4:685` & Bảng 4.11 cho khớp, kèm chú thích rằng phần "một
    phần" chỉ là do E1a/E1b thiếu lực kiểm định, còn lõi H5 (Q_M + phổ điểm uốn P7) đã xác nhận.
  → Cần NCS chọn (a) hay (b); em không tự đổi vì là tuyên bố lập trường học thuật.

## 6. 🟡 H6 chỉ kết luận ở ch4

H6 (dị biệt thời gian) có verdict ở `ch4:686` ("không xác nhận tại TQ F=1,83 p=,176; TP dịch chuyển
tại VN") nhưng không được nhắc lại trong phần bàn luận ch5. **Đề xuất:** thêm một câu về H6 vào §5.1
hoặc §5.4 hạn chế.

## 7. 🟡 Bảng 2.1 / Bảng 2.2 đánh số ngược (ch2 §2.5.8)

Bảng 2.2 (tổng hợp giả thuyết) định nghĩa trước ở `ch2:278`, Bảng 2.1 (ánh xạ nghiên cứu thành phần)
sau ở `ch2:298`. Người đọc gặp "Bảng 2.2" trước "Bảng 2.1". **Đề xuất:** hoán đổi số hai bảng (cập
nhật mọi tham chiếu `ch2:296,302–312`). *(Thay đổi lan tỏa — để NCS quyết.)*

---

## 8. ✅ Các hạng mục đã kiểm tra và NHẤT QUÁN

- **Điểm uốn:** P7 M2 51,5% → M5 43,6% (toàn mẫu) vs Nhóm IV 43,0% — đúng và phân biệt rõ.
  VN 39–46% (pooled 39,7%), TQ 47–49% (48,78%), Singapore ~88,6% (kèm cảnh báo CI), Ấn Độ
  61,8%→40,7%→tan biến, Nhật điểm uốn ngoài miền. Khớp `CANONICAL_NUMBERS.md`.
- **Hệ số:** TCI +0,141 / DAI +0,201 (toàn mẫu); Nhật +0,671 (tuyến tính), premium 25,8%;
  FIP −1,339 (chỉ bản 3-cụm N=209, có cảnh báo). Nhất quán.
- **Meta P6:** k=238, K=288, r=0,074, I²=62,4% (54,1%/8,4%), Q_M=17,35 df=4 p=,002; 5-regime
  (P6) vs 6-nhóm (P7) đã được hòa giải tường minh ở `ch4:179`.
- **Cỡ mẫu:** pool 96.415/52; khung 88.869/50; P7 M2 81.022 / M5 79.080; Nhật 2.168; P1 40.633
  (5.251+12.068+23.314 ✅); P8 1.450/7 nền. 91.982/84.910 là **khung pre-Japan** (ghi rõ ở
  `appendix_A:83`) — không phải mâu thuẫn.
- **Tham chiếu chéo:** mọi `Mục X.Y`, `Bảng X.Y`, `Hình X.Y` đều phân giải; không có tham chiếu treo.
  Mọi `Hình 4.x` đều có tệp trong `thesis/figures/`.

---

*Người rà soát: trợ lý AI (3 lượt quét song song có kiểm chứng số học). Hạng mục 1, 4–7 chờ quyết
định/ rebuild của NCS; hạng mục 2–3 đã áp dụng.*

---

## 9. ✅ Trích dẫn mồ côi trong Chương 1–3 — đã sửa

Rà soát đối chiếu mọi trích dẫn trong văn của ch1/ch2/ch3 với `04_references_apa7.md` phát hiện
**4 trích dẫn không có mục tài liệu tương ứng**. Đã bổ sung đủ 4 mục (APA7, đúng vị trí chữ cái):

| Trích dẫn | Vị trí trong văn | Xử lý |
|-----------|------------------|-------|
| **Contractor et al., 2003** (đường cong chữ S ba giai đoạn — neo H1) | ch1:11; ch2:53,133,226; ch3:92,224; ch5:81,83,149 | ✅ Thêm Contractor, Kundu & Hsu (2003), *JIBS* 34(1) — trước đó danh mục chỉ có Contractor (2012) |
| **Hitt et al., 2006** (đa dạng hóa quốc tế — RBV) | ch2:11,63; ch3:92 | ✅ Thêm Hitt, Tihanyi, Miller & Connelly (2006), *J. Management* 32(6) — trước đó chỉ có Hitt et al. (1997) |
| **Hunter & Schmidt, 2004** (nền phương pháp meta-analysis) | ch1:97; ch3:15,31,706 | ✅ Thêm Hunter & Schmidt (2004), *Methods of meta-analysis* (2nd ed.), Sage |
| **Peng, 2001** (RBV trong kinh doanh quốc tế) | ch2:63 | ✅ Thêm Peng (2001), *J. Management* 27(6) — **không phải lỗi gõ** "Peng 2003"; ngữ cảnh RBV-IB khớp đúng bài Peng (2001) |

*Lưu ý Peng:* agent rà soát ban đầu nghi "Peng 2001" là lỗi gõ của "Peng 2003", nhưng ngữ cảnh
`ch2:63` (RBV giải thích vì sao cùng FSTS doanh nghiệp đạt hiệu quả khác nhau, giảm gánh nặng người
nước ngoài) khớp chính xác bài *"The resource-based view and international business"* (Peng, 2001),
khác hẳn Peng (2003) *"Institutional transitions"*. Do đó **bổ sung** Peng (2001) thay vì sửa năm.

**Đã kiểm tra và đầy đủ:** 15 trích dẫn trụ cột còn lại (Lu & Beamish 2004, Marano 2016, Kirca 2012,
Berry & Kaul 2016, Hsieh & Klenow 2009, North 1990, Khanna & Palepu 2010, Barney 1991, Hambrick &
Mason 1984, Teece 1997, Johanson & Vahlne 1977, Haans 2016, Pisani 2020, Kafouros 2023, Karna 2016)
đều có mục đúng năm. Định nghĩa biến (FSTS=d3b+d3c đa quốc gia / d3c đơn quốc gia; DAI Tầng 1/2;
ICRV 6 chế độ), đặc tả mô hình P7 (M1–M10, M2 N=81.022 / M5 N=79.080) và mọi số xem trước ở Chương 1
đều **nhất quán** với Chương 4–5.

---

## 10. ✅ H5 — chốt verdict bằng rà soát kết quả thực (P6 MARA + P7)

Theo yêu cầu "rà soát kết quả .dta thực tế trước khi quyết", đã đối chiếu trực tiếp output thật:

**P6 MARA** (`p6/p6_meta_manuscript_en.md:328,344–346,434,470`):
- Lõi H5 — **xác nhận**: $Q_M = 17{,}35$, $df=4$, $p={,}002$ → cỡ ảnh hưởng khác nhau giữa các chế độ.
- Định hướng E1a/E1b — **KHÔNG xác nhận**: ý nghĩa $Q_M$ do **nhóm Frontier $k=3$** (chi phối bởi
  1 nghiên cứu ngoại lai Pouresmaeili 2018, $r=0{,}69$). Tương phản giữa các nhóm đông (I, II, III,
  MX) **đều không có ý nghĩa**; khoảng cách Advanced–Emerging 0,079 vs 0,069 không ý nghĩa. Manuscript
  còn khuyến cáo chính sách rằng gradient thể chế "không được xác nhận meta-analytically".

**P7** (`p7/replication/results/p7_R_turning_points.csv`): gradient điểm uốn theo ICRV là **ba vùng
phi đơn điệu** (chữ U ngược sắc ở vùng giữa → duỗi thẳng biên trên → mất cấu trúc/U ở SIDS), không
phải dốc đơn điệu "mạnh ở yếu → giảm ở tiên tiến" như H5 phát biểu.

**→ Kết luận:** bằng chứng thực ủng hộ **Phương án (a)** — verdict đúng là **"Xác nhận một phần H5"**.
Phương án (b) (nâng lên "Xác nhận" đầy đủ) sẽ **mâu thuẫn chính kết luận của bài P6**, nên bị loại.
Đã sửa ch5 §5.1.1 (tiêu đề + đoạn mở) xuống "một phần" kèm giải thích E1a/E1b & ba-vùng, khớp ch4 §4.11.

*Ghi chú phụ phát hiện khi rà:* `p7_R_turning_points.csv` (v1 không-FE) và `_v2` (FE theo nhóm) cho
điểm uốn per-ICRV **lệch nhau khá lớn** (vd Upper_mid 5,5% vs 42,9%; Emerging 43,9% vs 59,2%;
Advanced_innovation 56,6% vs 73,9%). Thân luận án dùng các con số đã chốt riêng (Nhóm IV 43,0%,
Nhóm I ngoài miền); nên khi rebuild authoritative, cần nêu rõ **đặc tả nào** (FE hay không) là nguồn
chính cho phổ điểm uốn per-nhóm để tránh người đọc đối chiếu nhầm sang bản v1/v2.

---

## 11. ✅ Điều chỉnh Bảng 4.1 + 4.2 theo kết quả data thực (2026-06-22, lượt 2)

Theo chỉ đạo "điều chỉnh theo kết quả data", đã **chạy lại script canonical**
`scripts/relock_descriptives_canonical.py` trên dữ liệu thô (`data_wbes/raw_dta/`, 139 tệp .dta) —
đây là "single source of truth" được thiết kế cho chính Bảng 4.1/4.2. Lần chạy lại **nay đã gồm
China-2012** nhờ bản vá parser `31b7895` (trước đây token `N####` làm rớt đợt này).

**Thay đổi cốt lõi (so committed CSV cũ):** chỉ **Nhóm III (Upper_mid)** đổi — đợt khảo sát 17→18,
LP-valid 12.481→15.174, sd 1,334→1,297, ISO 25,4→31,4%, website 53,9→56,9% — đúng là hiệu ứng nạp
thêm China-2012. Các nhóm khác không đổi.

**Đã căn lại trong `thesis/chuong_4`:**
- **Bảng 4.1**: cột n đổi sang **LP-valid** (5.688 / 2.082 / 15.174 / 42.798 / 16.387 / 1.916;
  **tổng 84.045**, cộng đúng), cùng sd log LP, FSTS%, xuất khẩu%, FDI% theo script. Đã giải quyết
  triệt để lỗi "98.097 ≠ 96.415": bảng nay là khung **LP-valid 49 nền** tái lập được, không còn trộn
  vintage. Note làm rõ thứ bậc: pool phân loại 96.415/52 ⊇ khung phân tích 88.869/50 ⊇ **LP-valid
  84.045/49** ⊇ P7 M2 81.022.
- **Bảng 4.2**: Nhóm III ISO 25,4→31,4%, website 53,9→56,9%; Nhóm V đổi mới quy trình 16,3→16,4%,
  ISO 12,7→12,6%, website 40,9→40,6%. Các nhóm khác giữ nguyên.
- **Văn xuôi §4.1** căn theo data: phân tán sd 1,04→0,96 (Nhóm I) & 1,24–1,37 (III–V); P90/P10
  ~11→~27 lần; P75/P25 3,2→5,5 (§4.1.6); FSTS khu vực 6,7–10,6% (~9%); tham gia xuất khẩu ~12–24%;
  exporter Nhóm I 24,3% / II 11,6%; SIDS website ngang Đang nổi 40,6%.
- CSV `data_wbes/analysis/descriptives_canonical_49econ.csv` đã được regenerate & commit.

**Còn lại (đề xuất lượt sau):**
1. **Sync CĐ1** (`chuyen_de/cd1/00_cd1_ctu_final_vi.md` Bảng 2.3.2.1 & 2.3.4.1) sang **cùng** output
   script canonical — hiện CĐ1 vẫn mang vintage cũ (87.987≠88.869). Script docstring nêu rõ nó là
   nguồn cho cả "CĐ1 Bảng 2.3.3.1–2.3.6", nên đồng bộ là bước trực tiếp.
2. **49 vs 50 nền**: khung LP-valid tái lập là 49 nền (một nền của khung 50 không có doanh nghiệp
   năng suất hợp lệ); docstring script tự mâu thuẫn về Timor — NCS nên xác nhận xử lý Timor để chốt
   49/50 trên toàn luận án.
3. Headline pool **96.415/52** vẫn là số master-file (không tái lập từ script LP-valid) — giữ làm
   pool phân loại, nhưng nếu cần con số tái lập được thì phải chạy bước phân loại trên master file.

---

## 12. ✅ Đồng bộ CĐ1 + chốt quy ước Timor (2026-06-22, lượt 3)

Theo chỉ đạo "triển khai đồng bộ; P7 giữ Timor, P8 bỏ Timor":

**Quy ước Timor đã chốt & ghi rõ:** khung mô tả/P7 **GIỮ** Timor-Leste trong Nhóm VI (SIDS = 8 nền,
LP-valid 1.916); nghiên cứu chuyên sâu **P8 LOẠI** Timor (7 nền Pacific, n=1.781). Đây đúng là cách
script canonical đã chạy; đã sửa docstring `relock_descriptives_canonical.py` (trước ghi nhầm "Timor
excluded") cho khớp thực tế.

**Đã đồng bộ CĐ1** (`chuyen_de/cd1/00_cd1_ctu_final_vi.md`) sang **cùng vintage** với thesis Bảng
4.1/4.2:
- **Bảng 2.3.2.1** (chính) + **Bảng A.1** (phụ lục): cột N → LP-valid (5.688 / 2.082 / 15.174 /
  42.798 / 16.387 / 1.916; tổng **84.045**); Nhóm VI bổ sung **Timor-Leste** (trước thiếu ở bảng
  chính); đợt khảo sát Nhóm III 17→18 (China-2012), Nhóm V 40→39 (Azerbaijan không dữ liệu).
- **Bảng 2.3.4.1** (%): Nhóm III ISO 25,4→31,4 / website 53,9→56,9; Nhóm V đổi mới quy trình
  16,3→16,4 / ISO 12,7→12,6 / website 40,9→40,6 — khớp thesis Bảng 4.2.
- Văn xuôi phân bố (§2.3.3) + caption hình + ghi chú SIDS (2.295→1.916) căn theo LP-valid.
- Note bảng nêu rõ thứ bậc khung (96.415/52 ⊇ 88.869/50 ⊇ 84.045/49 ⊇ 81.022) + quy ước Timor.

**Trạng thái:** thesis ↔ CĐ1 ↔ CSV canonical nay **cùng MỘT vintage** (gồm China-2012), tái lập được
từ `scripts/relock_descriptives_canonical.py`. "88.869/50" giữ vai trò **pool mô tả/khung phân tích**
(narrative), còn các bảng phân rã per-nhóm dùng **LP-valid 84.045/49** (tái lập được) — quan hệ tập
con đã ghi chú minh bạch.

**Lưu ý còn mở (nhẹ):** nếu cần con số phân rã đúng cho khung 88.869/50 (không phải LP-valid) hoặc
bổ sung Azerbaijan, phải có lát cắt thô Azerbaijan + chạy bước phân loại trên master file — nằm ngoài
subset committed.

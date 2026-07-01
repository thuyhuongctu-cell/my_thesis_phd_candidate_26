# A1 — Cross-validation bằng phần mềm tương đương (Python), 2026-06-23

> Đối chiếu headline của từng nghiên cứu thành phần bằng **công cụ tương đương Stata**
> (Python: `statsmodels`/`pyreadstat` + wild-cluster bootstrap thuần Python), chạy trực tiếp
> trên dữ liệu thô committed `data_wbes/raw_dta/`. Đây là phần **A1** trong luật liêm chính.
> *Lưu ý:* đây là phần mềm **tương đương**, không phải Stata; nếu hội đồng/tạp chí yêu cầu đích danh
> Stata, NCS chạy lại các `.do` đã có (`scripts/stata/`, `p5/replication/do/`, `p4/replication/do/`,
> `p9_india/replication/do/`) trên máy có license — kết quả Python dưới đây dùng để **đối chiếu chéo**.

## Bảng đối chiếu (chạy 2026-06-23)

| NC | Runner Python (tái lập) | Headline chạy ra | Số khóa trong bản thảo | Khớp? |
|----|--------------------------|------------------|------------------------|-------|
| **P4** Singapore | `p4/replication/p4_singapore_figs_from_raw.py` | chữ U ngược M2: FSTS_c **+3,08**/FSTS²_c **−1,90**; TCI mức **+0,21**; DAI mức **+0,17**; **FSTS²×DAI +3,22** (p=,020); điểm uốn ~**86%** (CI 31–141% → không định vị chắc); N=623/617 | FSTS²×DAI **+3,119**; TP ~88,6% (không định vị) | ✅ (tương tác +3,22 ≈ +3,119) |
| **P5** Trung Quốc | `p5/replication/python/build_and_run.py` | TP mfg **42,31%**(2012)/**29,65%**(2024); pooled all-frame **48,78%** | 49,37/47,19/48,78; mfg 42,31/29,65; N=4.544 | ✅ khớp |
| **P7** 50 nền | `dist/osf/P7_capstone/code/p7_run_50econ.py` | 50 nền/107 cặp; M2 TP **51,40%**; M5 TP **43,83%**; Nhóm IV (Lower_mid) TP **43,03%**; SIDS β₂>0 (FIP U-shape) | M2 51,5%/M5 43,6% | ✅ TP + ba-vùng (xem ghi chú N) |
| **P8** SIDS | `p8/replication/build_and_run_p8_7pacific.py` | N=**1.450**/7 cụm; tuyến tính **−0,085** (p_wild=,656); bậc hai fsts_c **−0,567**/fsts_c² **+0,696** (p_wild ,088/,082) | trùng khít | ✅ khớp |
| **P9** Ấn Độ | `p9_india/replication/run_pipeline.py` | TP **61,81%**(2014)/**40,72%**(2022)/**tan biến** (−112%, β₂ ns); Paternoster z=**−7,94** | 61,8/40,7/tan biến; z=−7,94 | ✅ khớp |
| **P10** Nhật Bản | `p10_japan/replication/p10_japan_models.py` | phần bù xuất khẩu **+0,258**; FSTS 4,1%; 16,5% xuất khẩu; battery gần-tuyến-tính | premium 25,8%; FSTS 4,1% | ✅ khớp |
| **P3** Việt Nam | `p3/replication/do/01_build_vietnam.do` (Stata) + `scripts/p3_dai_reproduce.py` | Python tái lập **đúng mẫu hình** (chữ U ngược, TP 39–46%) | TP 39–46% | ⚠️ độ lớn chính xác cần Stata (mẫu số `b1_d`) |
| **Lớp mô tả** (CĐ1/thesis) | `scripts/relock_descriptives_canonical.py` + `relock_correlations_canonical.py` | 50 nền/107 cặp/84.998 LP-valid; bảng % + tương quan | khớp Bảng 4.1/4.2/2.3.8.1 | ✅ tái lập |

## Ghi chú quan trọng (N của P7)

Runner P7 dựng **khung riêng từ raw** (`data_wbes/raw_dta/`) nên N **lệch** số master-locked của luận
án (M2 raw ≈ 84.453 vs master 81.022; M5 ≈ 82.358 vs 79.080). Hai nguyên nhân: (i) khung raw vs khung
master khác quy trình làm sạch/dedup (đã ghi nhận từ trước); (ii) raw nay **gồm 4 đợt Azerbaijan** mới
thêm 06-23. **Điểm uốn và cấu trúc ba vùng tái lập đầy đủ** (M2 51,40% ≈ 51,5%; M5 43,83% ≈ 43,6%;
Nhóm IV 43,03% = 43,0%; SIDS đổi sang U-shape). Luận án báo cáo **số master-locked** (81.022/79.080/
43,6%) — không đổi; bảng này là kiểm chứng độc lập, sai khác N nằm trong chênh lệch raw↔master.

## Trạng thái A1 sau lượt này

- ✅ **P4, P5, P7, P8, P9, P10 + lớp mô tả**: đã đối chiếu chéo bằng Python, tái lập headline (P7 khớp
  TP/pattern, N theo khung raw).
- ⚠️ **P3**: Python tái lập mẫu hình; độ lớn chính xác vẫn cần Stata của NCS (`b1_d`).
- 🔧 Đã **vô hiệu hóa** file gây nhầm `p4/replication/p4_singapore_replication.py` (vốn là bản Vietnam
  dán nhầm nhãn, đọc đường dẫn upload tạm) → stub chỉ dẫn sang runner đúng.
- ✅ **P9/P10 path-audit**: đã dùng sẵn `data_wbes/raw_dta/` (không cần sửa).

## A2 — Verify DOI: KHÔNG chạy được trong môi trường này

Container chặn outbound → CrossRef trả **HTTP 403** (đã test). `scripts/verify_dois.py` phải chạy trên
máy có mạng của NCS. Cần verify: ~62 DOI "from training knowledge" (audit 16/06) **+ 4 mục mới thêm**
phiên 06-22/23: Contractor, Kundu & Hsu (2003) `10.1057/palgrave.jibs.8400003`; Hitt et al. (2006)
`10.1177/0149206306293575`; Hunter & Schmidt (2004) — sách Sage, không DOI (hợp lệ); Peng (2001)
`10.1177/014920630102700604`.

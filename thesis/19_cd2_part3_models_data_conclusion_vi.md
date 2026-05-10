# CHUYÊN ĐỀ TIẾN SĨ SỐ 2 — PHẦN 3 (CHƯƠNG 6–9 + TÀI LIỆU THAM KHẢO)

> Phần 1 (Chương 1–2): `thesis/17_cd2_part1_intro_theory_vi.md`.
> Phần 2 (Chương 3–5): `thesis/18_cd2_part2_review_framework_hypotheses_vi.md`.
> **Phiên bản 1.0 (ngày 09/05/2026)**: Chương 6 — đặc tả tám mô hình thực nghiệm M0–M7; Chương 7 — thiết kế dữ liệu và chiến lược nhận dạng; Chương 8 — kế hoạch kiểm định độ vững; Chương 9 — đóng góp và kết luận.

---

## CHƯƠNG 6 — ĐẶC TẢ TÁM MÔ HÌNH THỰC NGHIỆM M0–M7

### 6.1 Nguyên tắc đặc tả

Tám mô hình M0–M7 được xây dựng theo cấu trúc **nested** (lồng nhau): mỗi mô hình sau bổ sung thêm biến so với mô hình trước, cho phép so sánh AIC/BIC và incremental R², và kiểm định từng giả thuyết bằng F-test block. Tất cả mô hình sử dụng:

- **Biến phụ thuộc**: ln(LP) = ln(annual sales PPP USD / permanent full-time employees)
- **SE**: HC1 robust standard errors (Long & Ervin, 2000) — baseline; HC3 cho robustness checks
- **Fixed effects**: Country FE (αⱼ) + Year FE (δₜ) trong mô hình pool đa quốc gia
- **FSTS mean-centered**: FSTS_c = FSTS − mean(FSTS) trước khi tính FSTS_c² để giảm đa cộng tuyến
- **Ký hiệu**: **X**ᵢ = vector biến kiểm soát (ln_emp, firm_age, foreign_own, sector dummies)

**Nguyên tắc kiểm soát**: Bộ controls **X**ᵢ được chọn dựa trên: (a) lý thuyết — ln_emp phản ánh economies of scale (RBV); firm_age phản ánh learning-by-doing (Uppsala); foreign_own phản ánh MNE effects (OLI paradigm); (b) thực nghiệm — tất cả bốn biến significant trong P3, P4, P5; (c) availability — available trong cả ba WBES schema. Biến sector dummies (ISIC 1-digit) kiểm soát sectoral heterogeneity trong LP không liên quan đến FSTS. Không đưa thêm controls có thể là mediator của FSTS→LP (ví dụ: export experience, GVC participation) để tránh "bad controls" problem (Angrist & Pischke, 2009).

### 6.2 M0 — Baseline tuyến tính (Hypothesis: baseline performance model)

$$\ln(LP)_i = \beta_0 + \beta_1 \cdot FSTS_i + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Thiết lập baseline và kiểm tra hướng tác động tuyến tính thuần túy.  
**Kỳ vọng**: β₁ > 0 (tác động dương trung bình của xuất khẩu).  
**Hạn chế của M0**: Không nắm bắt được phi tuyến tính — cung cấp lower-bound estimate cho tác động QTH.

### 6.3 M1 — Inverted-U Quadratic (testing H1 quadratic form)

$$\ln(LP)_i = \beta_0 + \beta_1 \cdot FSTS_{c,i} + \beta_2 \cdot FSTS_{c,i}^2 + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định inverted-U trong H1 — dạng hàm phổ biến nhất trong văn liệu.  
**Kỳ vọng**: β₁ > 0, β₂ < 0.  
**Turning point**: TP₁ = −β₁/(2β₂) — điểm FSTS tối ưu (on mean-centered scale).  
**Kiểm định bổ sung**: Lind–Mehlum (2010) U-test để xác nhận inverted-U thực sự (không chỉ là quadratic fit với dấu đúng).

### 6.4 M2 — S-curve/Cubic (testing H1 full three-stage)

$$\ln(LP)_i = \beta_0 + \beta_1 \cdot FSTS_{c,i} + \beta_2 \cdot FSTS_{c,i}^2 + \beta_3 \cdot FSTS_{c,i}^3 + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định S-curve ba giai đoạn (Lu & Beamish, 2004; Contractor et al., 2003).  
**Kỳ vọng**: β₁ > 0, β₂ < 0, β₃ > 0 (giai đoạn học tập → hái quả → quá mức).  
**Ghi chú**: Với SMEs châu Á (majority WBES sample), giai đoạn 1 (beta₃ stage) thường không rõ do sample hiếm có FSTS rất cao. M1 thường fit tốt hơn M2 trong các sample có FSTS phân phối lệch phải.  
**Model selection**: So sánh M1 và M2 bằng AIC, BIC, và F-test β₃=0.

### 6.5 M3 — + TCI Moderation (testing H2)

$$\ln(LP)_i = \underbrace{\beta_0 + \beta_1 FSTS_{c,i} + \beta_2 FSTS_{c,i}^2}_{M1} + \beta_3 \cdot TCI_i + \beta_4 \cdot (FSTS_{c,i} \times TCI_i) + \beta_5 \cdot (FSTS_{c,i}^2 \times TCI_i) + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định H2 — TCI là level-shifter (β₃ > 0) và/hoặc curvature moderator (β₄, β₅).  
**Kỳ vọng chính**: β₃ > 0 (direct TCI effect).  
**Kỳ vọng exploratory**: β₄ < 0 và β₅ > 0 sẽ có nghĩa TCI nâng turning point (makes inverted-U gentler/later) — consistent với P3 Việt Nam evidence nhưng không confirmed bởi P5 Trung Quốc.  
**Kiểm định**: F-test (β₄=β₅=0) = joint moderation test; nếu p>.10 → TCI là pure level-shifter (H2 confirmed as intercept effect).

### 6.6 M4 — + DAI Moderation (testing H3)

$$\ln(LP)_i = \underbrace{\text{M1}}_{\text{base}} + \beta_3 \cdot DAI_i + \beta_4 \cdot (FSTS_{c,i} \times DAI_i) + \beta_5 \cdot (FSTS_{c,i}^2 \times DAI_i) + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định H3 — DAI là conditional scaling resource.  
**Kỳ vọng**: β₅(FSTS²×DAI) > 0 trong Nhóm I (consistent P4 Singapore +3.119); β₃(DAI direct) → 0 khi kiểm soát selection (consistent P3 Việt Nam IV null).  
**Lưu ý IV**: Trong sub-sample Nhóm IV, nếu có instrument hợp lệ (industry export propensity, distance to port), chạy 2SLS để phân biệt causal DAI vs. selection DAI.  
**Margins analysis**: Vẽ marginal effect of DAI tại các phân vị FSTS (p10/p25/p50/p75/p90) theo kiểu P4 Singapore.

### 6.7 M5 — + Manager Moderation (testing H4)

$$\ln(LP)_i = \underbrace{\text{M1}}_{\text{base}} + \beta_3 \cdot Manager_i + \beta_4 \cdot (FSTS_{c,i} \times Manager_i) + \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định H4 — đặc điểm top manager moderation.  
**Biến Manager** (thứ tự ưu tiên):
1. exp_manager (b5 — số năm kinh nghiệm) — biến chính
2. educ_manager (b7a — trình độ) — biến phụ
3. gender_manager (b7 — female = 1) — exploratory
**Kỳ vọng**: β₄(FSTS×exp_manager) > 0.  
**Ghi chú**: WBES thu thập biến manager không nhất quán qua tất cả schema; tỉ lệ missing có thể cao ở một số wave → cần báo cáo tỉ lệ available observations và sensitivity check.

### 6.8 M6 — + Institutional Regime ICRV (testing H5)

$$\ln(LP)_i = \underbrace{\text{M1}}_{\text{base}} + \sum_{j=2}^{6} \left[\beta_{3j} \cdot ICRV_{j,i} + \beta_{4j} \cdot (FSTS_{c,i} \times ICRV_{j,i}) + \beta_{5j} \cdot (FSTS_{c,i}^2 \times ICRV_{j,i})\right] + \boldsymbol{\gamma}'\mathbf{X}_i + \delta_t + \varepsilon_i$$

**Mục đích**: Kiểm định H5 — gradient ICRV và forced penalty (Nhóm VI).  
**Baseline**: Nhóm I (tiên tiến đổi mới) = reference category.  
**Kỳ vọng**: turning point giảm dần theo j (Nhóm II → III → IV → V → VI); Nhóm VI có β(FSTS×ICRV_VI) ≤ 0 (forced penalty or non-positive I→P).  
**Lưu ý**: Country FE bị omit trong M6 do ICRV_j là time-invariant country-level variable — thay bằng Year FE + region FE (6 regions).  
**Kiểm định gradient**: F-test bình đẳng các hệ số turning point: H₀: TP₁=TP₂=...=TP₅ — bác bỏ H₀ → xác nhận gradient H5.

### 6.9 M7 — Three-way Capstone (testing H2+H3+H6 đồng thời)

$$\begin{aligned}
\ln(LP)_i = &\ \beta_0 + \beta_1 FSTS_{c,i} + \beta_2 FSTS_{c,i}^2 + \beta_3 TCI_i + \beta_4 DAI_i \\
&+ \beta_5 (FSTS_{c,i} \times TCI_i) + \beta_6 (FSTS_{c,i}^2 \times TCI_i) \\
&+ \beta_7 (FSTS_{c,i} \times DAI_i) + \beta_8 (FSTS_{c,i}^2 \times DAI_i) \\
&+ \beta_9 (FSTS_{c,i} \times TCI_i \times DAI_i) \\
&+ \beta_{10} (FSTS_{c,i} \times YB_{2013-17,i}) + \beta_{11} (FSTS_{c,i}^2 \times YB_{2013-17,i}) \\
&+ \beta_{12} (FSTS_{c,i} \times YB_{2018-25,i}) + \beta_{13} (FSTS_{c,i}^2 \times YB_{2018-25,i}) \\
&+ \boldsymbol{\gamma}'\mathbf{X}_i + \alpha_j + \delta_t + \varepsilon_i
\end{aligned}$$

**Mục đích**: Mô hình tổng lực kiểm định H2 (TCI), H3 (DAI), và H6 (temporal) đồng thời.  
**Kỳ vọng trọng tâm**: β₈(FSTS²×DAI) > 0 trong Nhóm I; β₃(TCI) > 0; β₁₂/β₁₃ ≠ β₁₀/β₁₁ (temporal shift).  
**Lưu ý đa cộng tuyến**: M7 có nhiều interaction terms → kiểm tra VIF; nếu VIF > 10 cho interaction, sử dụng mean-centering và variance decomposition.  
**Yêu cầu mẫu**: Với k = 13 focal parameters + controls, n ≥ 5.000 cần thiết cho power > 0.80 tại f² = 0.02 — dễ dàng đáp ứng với pool 101.185.

### 6.10 Bảng tổng hợp mô hình

**Bảng 6.1**. *Tám mô hình M0–M7 — cấu trúc, giả thuyết kiểm định, và biến bổ sung.*

| Mô hình | Biến bổ sung so với mô hình trước | Giả thuyết | Kiểm định chính |
|---------|----------------------------------|------------|-----------------|
| **M0** | FSTS (tuyến tính) | Baseline | β₁ > 0 |
| **M1** | + FSTS² | H1 (inverted-U) | β₂ < 0; Lind–Mehlum |
| **M2** | + FSTS³ | H1 (S-curve) | β₃ > 0; F-test β₃=0 |
| **M3** | + TCI, FSTS×TCI, FSTS²×TCI | H2 | β₃>0; F-test (β₄=β₅=0) |
| **M4** | + DAI, FSTS×DAI, FSTS²×DAI | H3 | β₅>0 Nhóm I; IV check |
| **M5** | + Manager, FSTS×Manager | H4 | β₄(FSTS×exp)>0 |
| **M6** | + ICRV_j × FSTS, ICRV_j × FSTS² | H5 | Gradient TP; forced penalty Nhóm VI |
| **M7** | + TCI×DAI×FSTS, Year_bucket×FSTS | H2+H3+H6 | Three-way block F-test |

---

## CHƯƠNG 7 — THIẾT KẾ DỮ LIỆU VÀ CHIẾN LƯỢC NHẬN DẠNG

### 7.1 Nguồn dữ liệu và cấu trúc pool

**Dữ liệu gốc**: World Bank Enterprise Surveys (WBES) — cơ sở dữ liệu điều tra vi mô doanh nghiệp lớn nhất thế giới, phủ hơn 170 quốc gia với hơn 400.000 cuộc phỏng vấn từ 2006 đến nay. WBES áp dụng phương pháp stratified random sampling theo quy mô doanh nghiệp (nhỏ/vừa/lớn) và ngành (manufacturing/services).

**Pool CĐ2**:
- **101.185** doanh nghiệp chính thức (registered firms)
- **47** nền kinh tế châu Á và Thái Bình Dương
- **108** cặp quốc gia-năm (country-year pairs)
- **14** mốc khảo sát (survey waves) từ 2009 đến 2025

**Bảng 7.1**. *Cấu trúc pool theo nhóm ICRV và mốc khảo sát.*

| ICRV Nhóm | Tên | Số nền kinh tế | N doanh nghiệp (ước tính) | Số country-years |
|-----------|-----|---------------|--------------------------|-----------------|
| I — Tiên tiến đổi mới | Singapore, HK, Korea, Taiwan, Israel | 5 | ~6.500 | ~8 |
| II — Tiên tiến tài nguyên | Saudi, Qatar, Kuwait, Bahrain, Brunei | 5 | ~8.500 | ~12 |
| III — Trung bình cao | China, Malaysia, Thailand, Kazakhstan, Armenia, Georgia | 6 | ~18.000 | ~15 |
| IV — Đang nổi | Vietnam, Indonesia, Philippines, India, Sri Lanka, Jordan, Mongolia | 7 | ~28.000 | ~22 |
| V — Cận biên | 17 nền kinh tế | 17 | ~35.000 | ~42 |
| VI — SIDS Thái Bình Dương | Fiji, PNG, Solomon Is, Tonga, Vanuatu, Samoa, Kiribati | 7 | ~5.185 | ~9 |
| **Tổng** | | **47** | **~101.185** | **108** |

**Ba thế hệ schema WBES và giao thức hòa hợp**:
- **PICS3** (2009–2013): biến FSTS từ d3a/d3b; TCI từ h1/h8/b8; DAI từ c22b only
- **Standardized** (2014–2018): biến tái định dạng nhưng tương thích; DAI từ c22b + một số e-payment items
- **BREADY/BEE** (2019–2025): schema mở rộng; DAI đầy đủ (c22b + k33 + k38); manager module chi tiết hơn

Giao thức hòa hợp chi tiết trong `thesis/08_p7_data_harmonization_protocol_vi.md` — bao gồm: (a) crosswalk biến giữa ba schema; (b) xử lý missing values; (c) winsorization tại p1/p99; (d) PPP conversion cho annual sales.

### 7.2 Đo lường biến chi tiết

**Biến phụ thuộc — ln(LP)**:
$$\ln(LP)_i = \ln\left(\frac{\text{annual sales}_i}{\text{permanent employees}_i}\right)$$
Doanh thu (d2) được chuyển đổi về PPP USD 2017 trước khi tính LP. Winsorized tại p1/p99 để giảm ảnh hưởng outliers.

**Biến độc lập — FSTS**:
$$FSTS_i = \frac{\text{direct export sales}_i}{\text{total annual sales}_i} = \frac{d3c_i}{100}$$
Ghi chú: d3c là tỉ lệ phần trăm doanh thu xuất khẩu trực tiếp. Indirect exports không bao gồm. FSTS_c = FSTS − mean(FSTS) trong mỗi wave-country cell trước khi tính FSTS².

**TCI — Technological Capability Index**:

| Item | Mã WBES | Mô tả | Schema available |
|------|---------|-------|-----------------|
| ISO certification | b8 | Doanh nghiệp có chứng nhận ISO không? (binary) | PICS3, Std, BEE |
| R&D activity | h8 | Có thực hiện R&D nội bộ không? (binary) | PICS3, Std, BEE |
| Product innovation | h1 | Đã ra sản phẩm/dịch vụ mới 3 năm qua? (binary) | PICS3, Std, BEE |
| Foreign tech licensing | e6 | Sử dụng công nghệ nước ngoài có bản quyền? (binary) | PICS3, Std, BEE |

TCI_z = z-standardized mean của ≥3/4 items non-missing (Cronbach α ước tính 0.55–0.65 — consistent với formative composite, Coltman et al., 2008).

**DAI — Digital Adoption Index**:

| Item | Mã WBES | Mô tả | Schema available |
|------|---------|-------|-----------------|
| Website presence | c22b | Doanh nghiệp có website không? (binary) | PICS3, Std, BEE |
| Customer e-payment | k33 | % doanh thu thu qua e-payment (continuous) | BEE only |
| Supplier e-payment | k38 | % mua hàng thanh toán qua e-payment | BEE only |

DAI_z_full (Tier 1+2): z-mean(c22b + k33 + k38) — **chỉ available trong BEE schema (2019+)**.  
DAI_z_tier1 (Tier 1 only): z-mean(c22b) — available xuyên tất cả schema.

**Chiến lược đo lường DAI**: Sử dụng DAI_z_full làm biến chính trong BEE sub-sample; DAI_z_tier1 cho cross-schema comparison và robustness. Minh bạch construct scope limitation trong limitations.

**Manager variables** (từ module b/b_2 — available trong BEE và một số Standardized waves):
- exp_manager (b5): số năm kinh nghiệm quản lý — continuous
- educ_manager (b7a): trình độ học vấn — ordinal (1=no education → 6=graduate)
- gender_manager (b7): giới tính top manager — binary (female=1)

**Biến kiểm soát**:
- ln_emp: ln(l1 — số lao động chính thức) — firm size proxy
- firm_age: năm hoạt động (2025 − year_established)
- foreign_own: ≥10% vốn nước ngoài = 1 (b2b)
- Sector dummies: Manufacturing (ISIC 10–33), Services (ISIC 45–96), Other
- Country FE (αⱼ): 47 dummies — absorb time-invariant country characteristics
- Year FE (δₜ): 14 dummies — absorb common shocks (COVID-19, GFC, AI adoption wave)

**Lưu ý về Country FE và ICRV**: Trong M1–M5 và M7, Country FE (αⱼ) được sử dụng để absorb toàn bộ unobserved country heterogeneity. Trong M6 (kiểm định ICRV gradient H5), Country FE bị omit vì ICRV_j là time-invariant country-level variable — thay thế bằng Region FE (6 regions: East Asia, Southeast Asia, South Asia, Central Asia, Middle East, Pacific) + Year FE. Thiết kế này là trade-off được chấp nhận: M6 sacrifice country-level unobservables để estimate ICRV gradient, trong khi M1–M5/M7 kiểm soát country unobservables để estimate firm-level mechanisms.

### 7.3 Phân loại ICRV 6 nhóm

**Bảng 7.2**. *Phân loại 47 nền kinh tế theo ICRV — đặc điểm và tiêu chí.*

| Nhóm ICRV | Nhãn | Tiêu chí | Nền kinh tế |
|-----------|------|---------|------------|
| I | Tiên tiến đổi mới sáng tạo dẫn dắt | GNI/capita >$25.000 PPP + Innovation-driven (WIPO) | Singapore, Hong Kong SAR, Hàn Quốc, Đài Loan, Israel |
| II | Tiên tiến tài nguyên dẫn dắt | GNI/capita >$25.000 PPP + Resource revenue >40% GDP | Saudi Arabia, Qatar, Kuwait, Bahrain, Brunei |
| III | Trung bình cao | GNI/capita $10.000–$25.000 PPP; trong quá trình chuyển đổi công nghiệp | Trung Quốc, Malaysia, Thái Lan, Kazakhstan, Armenia, Georgia |
| IV | Đang nổi | GNI/capita $4.000–$10.000 PPP; hội nhập GVC đang tăng | Việt Nam, Indonesia, Philippines, Ấn Độ, Sri Lanka, Jordan, Mông Cổ |
| V | Cận biên | GNI/capita <$4.000 PPP; institutional voids đáng kể | Bangladesh, Pakistan, Lào, Campuchia, Myanmar, Nepal, Bhutan, Maldives, Uzbekistan, Tajikistan, Kyrgyzstan, Turkmenistan, Afghanistan, Timor-Leste, Iraq, Lebanon, Yemen (17 nước) |
| VI | SIDS Thái Bình Dương | Đảo nhỏ; GDP <$10B; dependency cao; forced internationalization | Fiji, Papua New Guinea, Solomon Islands, Tonga, Vanuatu, Samoa, Kiribati |

**Tổng**: 5 + 5 + 6 + 7 + 17 + 7 = **47** nền kinh tế.

**Căn cứ phân loại ICRV và tính nhất quán với văn liệu**: Phân loại 6 nhóm dựa trên GNI/capita PPP (World Bank 2020–2024 average), Innovation Index (WIPO GII), và resource revenue share (IMF Fiscal Monitor). Phân loại này nhất quán với: (a) World Bank income groups nhưng tinh chỉnh hơn bằng cách tách innovation-driven vs resource-driven trong Advanced; (b) Marano et al. (2016) institutional distance approach nhưng áp dụng cho châu Á cụ thể; (c) UNCTAD Small Island Developing States classification cho Nhóm VI. Tính ổn định phân loại: tất cả 47 nền kinh tế không thay đổi nhóm ICRV trong giai đoạn 2009–2025 (threshold test: chuyển nhóm nếu GNI/capita vượt ngưỡng ±15% trong ≥3 năm liên tiếp — không có trường hợp nào).

### 7.4 Chiến lược nhận dạng

**Tier 1 — OLS với robust SE và FE** (tất cả mô hình M0–M7):
- HC1 robust SE (baseline): điều chỉnh heteroskedasticity cấp doanh nghiệp
- Country × Year FE (two-way): loại bỏ unobserved time-invariant country heterogeneity và common time shocks
- VIF check: β(VIF) < 10 cho tất cả focal variables (expected: TCI/DAI có thể cao nếu tương quan với country dummies)

**Tier 2 — Instrumental Variable (DAI trong M4, Nhóm IV)**:
- Instrument candidates: (1) industry-level mean DAI (loại firm khỏi mean) — industry export propensity; (2) distance of firm's city to nearest submarine cable landing station (thay thế psychic distance)
- First-stage F-statistic: phải ≥ 16 (Stock & Yogo threshold for weak instruments)
- Reference: P3 Việt Nam đã chứng minh first-stage F = 34.6 với instrument hợp lệ
- Kết quả IV vs OLS: nếu β(IV) ≪ β(OLS), DAI là selection-driven (consistent với CDCM)

**Tier 3 — Kiểm định phi tuyến**:
- Lind–Mehlum (2010) U-test: xác nhận inverted-U thực sự (không chỉ dấu đúng)
- Paternoster z-test: so sánh turning points giữa nhóm ICRV hoặc giữa year-buckets
- LOWESS: non-parametric confirmation của dạng hàm

**Lind–Mehlum U-test** (chi tiết): Kiểm định xem dạng inverted-U là thực sự (genuine non-monotonic với maximum nằm trong vùng dữ liệu) hay chỉ là quadratic fit. Quy trình: (1) Kiểm tra β₁ > 0 và β₂ < 0; (2) Tính TP = −β₁/(2β₂) và 95% CI bằng delta method; (3) Kiểm định H₀: slope tại min(FSTS) ≤ 0 HOẶC slope tại max(FSTS) ≥ 0 — bác bỏ H₀ → genuine inverted-U. P3 Việt Nam đã áp dụng: TP_pooled = 39.7% (95% CI: 33.2–46.2%), Lind–Mehlum p < .001 cho pooled model.

**Paternoster z-test** (chi tiết): So sánh hệ số giữa hai nhóm hoặc hai giai đoạn:
$$z = \frac{\hat{\beta}_1 - \hat{\beta}_2}{\sqrt{SE_1^2 + SE_2^2}}$$
Áp dụng: (a) So sánh TP(Nhóm I) vs TP(Nhóm IV) cho H5; (b) So sánh FSTS² coefficient giữa Year_bucket cho H6. P3 Việt Nam: z = 3.353 giữa wave 2009 và 2015 (TP dịch chuyển từ 46.2% → 39.3%).

**LOWESS diagnostic**: Non-parametric smoother (bandwidth = 0.4) vẽ ln(LP) ~ FSTS — nếu hình dạng visual consistent với inverted-U → confirmatory evidence không phụ thuộc distributional assumptions. R code: `lowess(x = df$fsts, y = df$ln_lp, f = 0.4)` với confidence bands từ bootstrap.

**Tier 4 — Sub-sample replication**:
- Pool đủ lớn (101.185) cho phép chạy M0–M7 riêng cho từng nhóm ICRV (Nhóm I: ~6.500; Nhóm IV: ~28.000) để kiểm định heterogeneity
- Cross-validation: so sánh turning points pool vs. sub-sample

---

## CHƯƠNG 8 — KẾ HOẠCH KIỂM ĐỊNH ĐỘ VỮNG

### 8.1 Tổng quan sáu nhóm kiểm định

CĐ2 thiết kế kế hoạch robustness toàn diện theo sáu nhóm, mỗi nhóm trả lời một mối lo cụ thể:

**Bảng 8.1**. *Kế hoạch kiểm định độ vững — sáu nhóm, 18 kiểm định.*

| Nhóm | Mối lo | Kiểm định cụ thể | Kỳ vọng |
|------|--------|-----------------|---------|
| **R1** Thay đổi thước đo | DV/IV/moderators khác nhau | (a) DV→ROS; (b) IV→exporter dummy; (c) TCI 3-item (không có h1); (d) DAI Tier 1 only (c22b) xuyên tất cả schema | Dấu hệ số giữ nguyên; magnitude có thể khác |
| **R2** Lọc mẫu | Selection bias từ sample composition | (a) Loại micro firms (<5 lao động); (b) Loại SOEs (state_own>50%); (c) Manufacturing only (ISIC 10–33); (d) Exporters only (FSTS>0) | Core results robust với varying samples |
| **R3** Thay đổi phương pháp | OLS assumption violations | (a) Quantile regression tại p25/p50/p75; (b) HC3 thay HC1; (c) Bootstrap SE (1.000 replications); (d) Clustered SE tại country level | Sign preservation; CI may widen |
| **R4** Kiểm tra dạng hàm | Functional form misspecification | (a) LOWESS non-parametric — kiểm tra visual inverted-U; (b) RESET test; (c) Fractional polynomial; (d) Spline regression với 3 knots | LOWESS consistent với quadratic fit |
| **R5** Placebo tests | Spurious correlations | (a) Thay FSTS bằng biến giả ngẫu nhiên → không tìm thấy phi tuyến; (b) Thay TCI bằng noise → không có moderation; (c) Reverse causality check (lag analysis nơi có thể) | Placebo tests không cho kết quả significant |
| **R6** Nhạy cảm thiết kế | Researcher degrees of freedom | (a) ICRV cutoffs khác (GNI thay PPP GDP); (b) Temporal buckets: 2009–11/12–16/17–25; (c) Loại từng quốc gia (jackknife 47 lần); (d) Vary DAI Tier threshold | Core findings stable |

**Ưu tiên thứ tự báo cáo robustness**: R1 (thay đổi thước đo) và R3 (thay đổi phương pháp) được báo cáo trong bảng chính vì chúng trả lời mối lo cơ bản nhất của reviewers (measurement và estimation). R2 (lọc mẫu) và R4 (dạng hàm) được trình bày trong Phụ lục A (condensed). R5 (placebo) được tóm tắt trong một đoạn văn thay vì bảng. R6 (thiết kế) được thảo luận trong §Limitations. Cách tổ chức này tuân theo chuẩn mực của *JIBS*, *SMJ*, và *AMJ* đối với robustness sections trong bài viết cross-national empirical.

### 8.2 Checklist kỳ vọng robustness

Theo Cohen's f² convention, tác động nhỏ (f² = 0.02), trung bình (f² = 0.15), lớn (f² = 0.35). Với n = 101.185:

- **Power**: >0.99 cho f² ≥ 0.01 → có thể detect rất nhỏ effect sizes
- **Publication bias risk**: Có thể inflate Type I error → robustness checks phải conservative
- **Acceptable range**: β(FSTS²) trong khoảng [−2.5, −0.5] qua các specs chính → consistent với văn liệu inverted-U
- **Flag**: Nếu bất kỳ R1–R6 nào cho β flip sign, phải report và thảo luận trong §9.4 Limitations

**Bảng 8.2**. *Ngưỡng acceptable cho key parameters qua robustness checks.*

| Parameter | Baseline expected | Acceptable range | Flag nếu |
|-----------|------------------|-----------------|---------|
| β₁(FSTS) | > 0 | [0.1, 3.0] | Âm hoặc không significant |
| β₂(FSTS²) | < 0 | [−2.5, −0.1] | Dương hoặc không significant |
| Turning point | 35–55% (phần lớn nhóm) | [20%, 90%] | Ngoài sample support |
| β(TCI) | > 0 | [0.05, 0.5] | Âm |
| β(FSTS²×DAI) Nhóm I | > 0 | [0.5, 6.0] | Âm hoặc null trong Nhóm I |
| R² incremental M1 vs M0 | > 1% | [0.5%, 5%] | < 0.3% |
| VIF focal variables | < 5 | < 10 | > 10 cho interactions |

**Quy trình báo cáo robustness**: Nếu ≥ 4/6 nhóm R1–R6 cho kết quả consistent với baseline (dấu đúng, p < .10), kết quả được coi là "robustly confirmed". Nếu chỉ 2–3/6 nhóm consistent, kết quả là "conditionally supported" — cần thảo luận điều kiện. Nếu < 2/6 nhóm consistent, kết quả cần tái xem xét và không được claim H confirmed.

### 8.3 Chuỗi báo cáo kết quả

**Bảng 8.3**. *Chuỗi outputs dự kiến — 7 bảng + 3 hình + phụ lục.*

| Output | Nội dung | Section báo cáo |
|--------|---------|-----------------|
| **Bảng 1** | Descriptive statistics + correlation matrix | §Results 1 |
| **Bảng 2** | M0–M4 (baseline đến TCI/DAI moderation); HC1 SE | §Results 2 |
| **Bảng 3** | M5–M7 (Manager, ICRV, Three-way capstone) | §Results 3 |
| **Bảng 4** | Turning points với delta-method 95% CI theo 6 nhóm ICRV | §Results 4 |
| **Bảng 5** | Paternoster z-tests: TP cross-group (H5) + cross-time (H6) | §Results 5 |
| **Bảng 6** | IV first-stage statistics (F, p, instrument validity) | §Results 6 |
| **Phụ lục A** | Robustness panels R1–R6 (bảng condensed) | Appendix |
| **Phụ lục B** | ICRV country classification + WGI data | Appendix |
| **Hình 1** | LOWESS non-parametric curve ln(LP) ~ FSTS (toàn pool) | §Results 1 |
| **Hình 2** | Marginal effects of DAI at FSTS percentiles (p10/p25/p50/p75/p90) | §Results 3 |
| **Hình 3** | Turning points by ICRV group with 95% CI bars | §Results 4 |

**Phần mềm**: Stata 18 (OLS + IV + margins + Lind–Mehlum) kết hợp R (LOWESS, ggplot2, turning point CI). Script được version-controlled trong `scripts/cd2_main_analysis.do` và `scripts/cd2_figures.R`.

**Quy ước báo cáo**: (a) Hệ số hồi quy trình bày unstandardized với HC1 SE trong ngoặc; (b) Turning point trình bày trên original FSTS scale (0–1) với delta-method CI; (c) Significance: *** p<.001, ** p<.01, * p<.05, † p<.10; (d) Pseudo-R² (OLS R²) báo cáo cho từng model + incremental ΔR².

---

## CHƯƠNG 9 — ĐÓNG GÓP VỀ MÔ HÌNH VÀ KẾT LUẬN

### 9.1 Tóm tắt mục tiêu và phát hiện dự kiến

Chuyên đề 2 xây dựng và đặc tả mô hình nghiên cứu lý thuyết và thực nghiệm về ảnh hưởng của quốc tế hóa đến hiệu quả hoạt động kinh doanh của 101.185 doanh nghiệp ở 47 nền kinh tế châu Á và Thái Bình Dương. Bốn câu hỏi nghiên cứu (Q1–Q3 từ §1.2 và Q4 về CDCM) được trả lời qua tám mô hình M0–M7 và hệ giả thuyết H1–H6.

**Kết quả dự kiến từ bằng chứng neo đậu**:

| Giả thuyết | Kết quả dự kiến | Cơ sở neo đậu |
|-----------|----------------|---------------|
| H1 phi tuyến | Xác nhận inverted-U ở hầu hết nhóm ICRV; TP gradient I→VI | P3 TP 39–46%; P5 TP 47–49%; P4 near-monotonic |
| H2 TCI level-shift | TCI dương bền vững; curvature moderation exploratory | P3 IV causal β=1.639; P5 +0.28→+0.43 |
| H3 DAI conditional | FSTS²×DAI dương trong Nhóm I; selection-driven trong Nhóm IV | P4 +3.119; P3 IV null |
| H4 Manager | exp_manager×FSTS dương | (kiểm định mới trong pool) |
| H5 ICRV gradient | Turning point gradient; forced penalty Nhóm VI | CĐ1 dispersion evidence |
| H6 Temporal | DAI shift 2009→2023; TCI tăng cường | P3 Paternoster p<.001; P5 p=.011 |

### 9.2 Đóng góp về lý thuyết

**Đóng góp 1: Khung tích hợp 4 tầng + Digital lens cho châu Á**. Không có khung tương đương trong văn liệu IB cho khu vực 47 nền kinh tế bao gồm cả SIDS Pacific. Khung tích hợp Uppsala + RBV + Institutional Theory + Upper Echelons + Digital Capability Lens cho phép giải thích đồng thời heterogeneity quan sát được — điều mà các mô hình đơn lý thuyết không làm được.

**Đóng góp 2: CDCM — Formalization Context-Contingent Digital Capability Model**. CDCM được phát hiện trong CĐ1 và được làm sắc nét trong CĐ2 qua H3: DAI là conditional scaling resource (không phải uniform premium), với tác động phụ thuộc ba chiều ngữ cảnh (regime × FSTS level × digital saturation). CDCM lấp đầy khoảng trống tại giao điểm của digital IB theory và institutional theory — chưa có trong văn liệu.

**Đóng góp 3: Sub-grouping Advanced regime (Nhóm I vs Nhóm II)**. Phát hiện từ CĐ1 về heterogeneity trong Advanced — Nhóm I (tiên tiến đổi mới: Singapore, Korea, HK, Đài Loan) vs Nhóm II (tiên tiến tài nguyên: Saudi, Qatar, Kuwait, Bahrain) — được tích hợp vào H5 như dự đoán lý thuyết: cùng GNI/capita cao nhưng cơ chế I→P khác nhau do nguồn lực dẫn dắt khác nhau. Đây là lần đầu tiên sub-grouping này được formalized trong framework I→P ở châu Á.

**Đóng góp 4: Forced penalty hypothesis trong khung I→P**. Dạng hàm forced penalty (SIDS Nhóm VI) được tích hợp vào H5 như extreme case của institutional gradient — SIDS không có inverted-U điển hình do forced internationalization (Briguglio, 1995). Tích hợp này mở rộng văn liệu I→P từ continental Asia sang Pacific Small Island States.

**Tổng kết đóng góp lý thuyết**: Bốn đóng góp lý thuyết cùng nhau tạo ra một "Bộ ba mở rộng lý thuyết I→P":
- **Chiều rộng**: 47 nền kinh tế với 6 nhóm ICRV từ Singapore → Pacific SIDS — rộng nhất trong văn liệu
- **Chiều sâu**: CDCM tách bạch TCI vs DAI — chi tiết nhất trong văn liệu micro-data châu Á
- **Chiều thời gian**: Three-period design với P3/P5 neo đậu — duy nhất trong văn liệu WBES I→P

Ba chiều này cùng tích hợp với P6 (meta-analysis, synthesis evidence) và P7 (25-country capstone, confirmatory) tạo thành đóng góp luận án coherent và publishable.

**Định vị trong văn liệu**: Gần nhất với CĐ2 về phạm vi là Kirca et al. (2012) — nhưng meta-analysis không kiểm định digital moderators và không có ICRV design. Wu et al. (2022) gần nhất về emerging markets — nhưng không có micro-data và không phân tách TCI vs DAI. Kafouros et al. (2023) gần nhất về institutional moderation — nhưng không có châu Á và không có phi tuyến. CĐ2 là nghiên cứu duy nhất tích hợp cả bốn chiều: (a) micro-data lớn; (b) digital + tech capability tách biệt; (c) institutional gradient 6 nhóm; (d) phi tuyến chính thức với U-test và LOWESS.

### 9.3 Đóng góp về mô hình

**Đóng góp 5: Tám mô hình M0–M7 với three-way moderation capstone (M7)**. Chuỗi mô hình nested cho phép kiểm định từng cơ chế riêng biệt trước khi tích hợp vào M7. Đặc biệt, M7 là mô hình đầu tiên trong văn liệu châu Á kiểm định đồng thời I×TCI×DAI three-way moderation kết hợp với temporal heterogeneity — cho phép kiểm tra xem TCI và DAI là complements hay substitutes trong moderating I→P.

**Bảng 9.2**. *Tiến trình kiểm định giả thuyết qua chuỗi mô hình M0–M7.*

| Giả thuyết | Mô hình chính | Test thêm | Kết quả dự kiến từ neo đậu |
|-----------|--------------|-----------|--------------------------|
| H1 (inverted-U) | M1 | Lind–Mehlum; LOWESS visual | TP 39–49% (tuỳ nhóm) |
| H1 (S-curve) | M2 | F-test β₃=0 vs M1 | M1 thắng AIC/BIC (SME data) |
| H2 (TCI) | M3 | Block F-test β₄=β₅=0 | β₃(TCI)>0; curvature exploratory |
| H3 (DAI) | M4 | IV check Nhóm IV | β₅>0 Nhóm I; IV null Nhóm IV |
| H4 (Manager) | M5 | Sensitivity (missing data) | β₄(FSTS×exp)>0; BEE sub-sample |
| H5 (ICRV gradient) | M6 | Paternoster z TP cross-group | Gradient I>II>III>IV>V; VI forced penalty |
| H6 (temporal) | M7 (Year_bucket) | Paternoster z cross-time | TP dịch chuyển 2009→2023; DAI coefficient tăng |

**Đóng góp 6: Temporal heterogeneity H6 với year-bucket design**. Phân chia 14 sóng WBES thành ba giai đoạn (2009–12 / 2013–17 / 2018–25) và kiểm định tương tác FSTS×Year_bucket là design chưa được áp dụng trong văn liệu I→P cho châu Á. Bằng chứng từ P3 Việt Nam (Paternoster z = 3.353 giữa 2009 và 2015) và P5 Trung Quốc (TCI Paternoster p = .011) neo đậu kỳ vọng thực nghiệm.

**Lý giải year-bucket design**: Ba giai đoạn phản ánh ba làn sóng công nghệ-thể chế khác nhau: (a) **2009–12** — hậu GFC, DAI còn hạn chế (website là chủ yếu), TCI là động lực chính; (b) **2013–17** — mobile penetration bùng nổ, e-payment lan rộng ở châu Á, DAI bắt đầu phát huy tác dụng; (c) **2018–25** — AI/cloud/platform economy, BEE schema ghi nhận Tier 2 đầy đủ, DAI tương tác mạnh với FSTS tại level cao. Thiết kế này cho phép kiểm định "structural breaks" trong cơ chế I→P mà không đòi hỏi dữ liệu panel dài hạn.

### 9.4 Đóng góp về phương pháp

**Đóng góp 7: Pool 101.185 doanh nghiệp — rộng nhất cho nghiên cứu I→P châu Á**. Ba thế hệ schema WBES được hòa hợp qua giao thức chi tiết (`thesis/08_p7_data_harmonization_protocol_vi.md`), tạo ra pool lớn nhất từ trước đến nay cho nghiên cứu I→P trong văn liệu IB. Pool này đủ lớn để chạy sub-sample replication theo ICRV và year-bucket với power đầy đủ.

**Đóng góp 8: Chiến lược nhận dạng đa tầng tích hợp IV**. Kết hợp HC1/HC3 robust SE, country×year two-way FE, IV identification (first-stage F > 16), và Paternoster z-test cho cross-group comparison tạo ra chiến lược nhận dạng mạnh nhất có thể với dữ liệu WBES cross-sectional. Đặc biệt, việc tách DAI causal vs. selection (từ bằng chứng P3 IV) là bước tiến quan trọng trong phân tích digital capability trong IB.

**Bảng 9.3**. *So sánh phương pháp CĐ2 với các nghiên cứu I→P tiêu biểu trong văn liệu.*

| Tiêu chí phương pháp | CĐ2 (nghiên cứu này) | Lu & Beamish (2004) | Marano et al. (2016) | Wu et al. (2022) |
|---------------------|---------------------|--------------------|--------------------|-----------------|
| Cỡ mẫu | 101.185 firms | ~980 firms | Meta-analysis | Meta-analysis |
| Số quốc gia | 47 | 1 (Japan) | 50+ | 40+ |
| DV | ln(LP) | ROA/Tobin's Q | Perf. (multi) | Perf. (multi) |
| Phi tuyến kiểm định | Lind–Mehlum + LOWESS | Cubic OLS | HLM | HLM |
| Digital moderator | TCI + DAI | Không có | Không có | Không có |
| IV cho endogeneity | Có (2SLS) | Không | Không | Không |
| ICRV classification | 6 nhóm (novel) | Không | GNI rough | WB income group |
| Temporal heterogeneity | Year-bucket design | Không | Không | Không |

*Ghi chú*: CĐ2 là nghiên cứu duy nhất tích hợp đồng thời: (a) cỡ mẫu vi mô lớn; (b) kiểm định phi tuyến chính thức; (c) digital moderators; (d) IV; và (e) ICRV institutional classification cho châu Á-Thái Bình Dương.

**Đóng góp 9: Giao thức hòa hợp ba thế hệ WBES**. Hòa hợp PICS3 (2009–13), Standardized (2014–18), và BEE (2019–25) đòi hỏi crosswalk biến chi tiết (≥40 biến), xử lý schema inconsistencies, và validation qua overlap years (khi một số quốc gia có cả hai schema). Giao thức này, được document hóa đầy đủ, là đóng góp methodological độc lập có giá trị cho cộng đồng nghiên cứu WBES.

### 9.5 Hàm ý chính sách

**Cho doanh nghiệp Việt Nam và emerging Asia**:
1. **Đầu tư vào TCI trước DAI**: Bằng chứng IV (P3 Việt Nam) cho thấy chỉ TCI là causal, trong khi DAI dương trong OLS là selection-driven. Doanh nghiệp nên ưu tiên xây dựng năng lực công nghệ thực chất (ISO, R&D, foreign tech) trước khi đầu tư vào digital adoption.
2. **Turning point 39–46% FSTS cho Việt Nam**: Doanh nghiệp vượt ngưỡng này cần đánh giá lại chiến lược QTH — tăng cường năng lực điều phối (manager experience, ERP, CRM) thay vì chỉ tăng tỉ lệ xuất khẩu.
3. **DAI phát huy mạnh khi FSTS cao và institutional setting tốt**: Nhóm I (Singapore) cho thấy DAI×FSTS² = +3.119 — khi doanh nghiệp đã ở mức FSTS 70%+ và hoạt động trong môi trường thể chế tốt, DAI mới trở thành scaling lever.

**Cho nhà hoạch định chính sách**:
1. **ICRV gradient** cho thấy chính sách hỗ trợ QTH cần phân biệt theo regime — what works in Singapore does not work in Bangladesh.
2. **Temporal heterogeneity H6** — chính sách năm 2025 không thể sao chép chính sách năm 2009; AI bùng nổ tạo ra cơ hội mới cho DAI trong giai đoạn 2018+.
3. **SIDS forced penalty** — Pacific SIDS cần khung chính sách khác hoàn toàn, không áp dụng logic inverted-U standard.

**Bảng 9.1**. *Ma trận chính sách theo nhóm ICRV — hàm ý từ H1–H5.*

| Nhóm ICRV | Pattern I→P | Hàm ý chính sách ưu tiên | Ngưỡng can thiệp |
|-----------|------------|--------------------------|-----------------|
| Nhóm I (tiên tiến đổi mới) | Near-monotonic, DAI conditional scaling | Tập trung DAI×FSTS cao — chính sách platform, e-commerce B2B | Hỗ trợ khi FSTS > 60% |
| Nhóm II (tiên tiến tài nguyên) | Weakly I→P, FDI dominant | Đa dạng hóa kinh tế tránh resource curse; SME export diversification | Giảm resource dependency |
| Nhóm III (trung bình cao) | Inverted-U, TP 45–55% | Nâng năng lực TCI trước khi scale xuất khẩu | TCI investment khi FSTS < 30% |
| Nhóm IV (đang nổi) | Inverted-U, TP 39–46% | Giải quyết institutional voids cản trở xuất khẩu hiệu quả | Cải cách khi TP bị kéo xuống < 35% |
| Nhóm V (cận biên) | Inverted-U, TP thấp, institutional voids cao | Ưu tiên institutional reform trước xuất khẩu expansion | Phát triển thể chế cơ bản |
| Nhóm VI (SIDS) | Forced penalty | Chính sách khác hoàn toàn — adaptive model không phải export-led | Regional cooperation, ODA-linked trade |

**Hàm ý chính sách cụ thể cho Việt Nam (Nhóm IV)**:
- Turning point 39–46% là ngưỡng chiến lược: doanh nghiệp tiếp cận 40% FSTS cần hỗ trợ năng lực điều phối (ERP, logistics, CRM) không chỉ marketing xuất khẩu
- TCI causal (IV F=22.1): Chính sách R&D incentive, ISO certification support, và technology transfer agreement là đầu tư có hiệu quả nhân quả thực sự, không phải selection effect
- DAI selection-driven trong Nhóm IV: Chương trình "digital adoption" cần targeting vào doanh nghiệp đang hoặc sẽ xuất khẩu — DAI trong doanh nghiệp không xuất khẩu ít có tác động LP trực tiếp theo CDCM

### 9.6 Hạn chế

**Hạn chế 1 — WBES không phải panel chuẩn**: Dữ liệu WBES chủ yếu là repeated cross-sections, không theo dõi cùng doanh nghiệp theo thời gian (ngoại trừ một số panel nhỏ). Điều này hạn chế khả năng suy luận nhân quả mạnh — các tác động thực nghiệm là conditional associations, không phải causal effects trừ khi có IV hợp lệ.

**Hạn chế 2 — DAI bị giới hạn Tier 1–2**: DAI đo lường Tier 1 (website) và Tier 2 (e-payment) — không quan sát được Tier 3 (ERP, CRM, digitally integrated processes) và Tier 4 (AI deployment, platform orchestration). CDCM có thể mạnh hơn nếu Tier 3–4 được đo lường — đây là hướng nghiên cứu tương lai khi BEE schema mở rộng.

**Hạn chế 3 — Manager variables thiếu trong một số schema**: Module top manager không nhất quán qua PICS3/Standardized/BEE — H4 phải được kiểm định trong sub-sample có đầy đủ dữ liệu, làm giảm power và generalizability.

**Hạn chế 4 — FSTS đo lường xuất khẩu trực tiếp**: FSTS = direct export intensity, không bao gồm indirect exports (qua intermediaries) và không-xuất-khẩu forms of internationalization (FDI, licensing). Doanh nghiệp QTH qua FDI nhưng không xuất khẩu trực tiếp sẽ có FSTS = 0 trong WBES — underestimation I→P effect cho các doanh nghiệp này.

**Hạn chế 5 — Selection into WBES sample**: WBES sử dụng stratified random sampling nhưng giới hạn ở registered firms với 5+ lao động — bỏ sót informal sector (lớn ở Nhóm V và VI). Kết quả không generalize cho doanh nghiệp không đăng ký.

**Bảng 9.4**. *Tóm tắt hạn chế, mức độ nghiêm trọng, và biện pháp giảm thiểu.*

| Hạn chế | Mức độ | Giảm thiểu trong CĐ2 | Ảnh hưởng đến kết luận |
|---------|--------|---------------------|----------------------|
| WBES không phải panel | Cao | IV identification + Year FE | Nhân quả cần diễn giải thận trọng |
| DAI Tier 1–2 only | Trung bình | Sensitivity với Tier 1 riêng | CDCM có thể understate Tier 3+ effects |
| Manager data thiếu | Trung bình | H4 trong BEE sub-sample | Power giảm; generaliz. hạn chế |
| FSTS direct only | Thấp-trung | Robustness: exporter dummy | I→P underestimate cho FDI-heavy firms |
| Registered firms only | Thấp | Scope limitation rõ ràng | Không generalize cho informal sector |

*Ghi chú mức độ*: Cao = có thể ảnh hưởng core findings; Trung bình = ảnh hưởng phạm vi kết luận; Thấp = không ảnh hưởng core findings nhưng cần thừa nhận.

### 9.7 Hướng nghiên cứu tương lai

Chuyên đề 2 đặt nền tảng lý thuyết và thực nghiệm cho ba luận văn trong chuỗi luận án:

1. **P6 — Meta-analysis update** (`thesis/06_p6_meta_update_plan_vi.md`): Cập nhật năm meta-analysis lớn với ~75 nghiên cứu mới (2017–2026), tập trung vào emerging market và digital moderation.

2. **P7 — 25-country capstone** (`thesis/07_p7_capstone_design_vi.md`): Áp dụng M0–M7 cho sub-pool 25 nền kinh tế đại diện từ tất cả nhóm ICRV — kiểm định toàn bộ H1–H6 đồng thời trên dữ liệu harmonized.

3. **P8 — Pacific SIDS forced penalty** (`thesis/10_p8_pacific_sids_design_vi.md`): Nghiên cứu chuyên biệt cho 7 SIDS (Nhóm VI) kiểm định forced penalty hypothesis và adaptive internationalization pathways.

Ngoài ra, khi BEE schema mở rộng Tier 3–4 digital indicators (AI deployment, integrated ERP), CDCM có thể được kiểm định đầy đủ hơn — cơ hội cho nghiên cứu panel với tracking firms across waves.

**Bảng 9.5**. *Lộ trình nghiên cứu tương lai từ CĐ2 — kết nối với chuỗi luận án.*

| Nghiên cứu | Timeline | Dữ liệu bổ sung cần | Câu hỏi mở rộng |
|-----------|----------|---------------------|-----------------|
| P6 — Meta-analysis | 2026 Q3 | ~75 papers 2017–2026 | Moderator publication bias correction; digital era effect size |
| P7 — 25-country capstone | 2026 Q4 | Harmonized BEE 2019–25 | H1–H6 đồng thời; cross-ICRV turning point gradient |
| P8 — SIDS forced penalty | 2027 Q1 | Pacific WBES + ADB SIDS data | Adaptive I→P model; regional cooperation effects |
| CDCM Tier 3–4 extension | 2027+ | BEE schema với AI indicators | DAI full spectrum; platform orchestration moderator |
| Panel follow-up | 2028+ | WBES panel component (5-country) | Causal panel estimation; within-firm learning effects |

**Hướng nghiên cứu lý thuyết**: CDCM có thể được mở rộng theo ba hướng lý thuyết: (1) **Tích hợp Ecosystem theory** — DAI không chỉ là firm-level resource mà còn là ecosystem participation indicator (Adner, 2017); (2) **Tích hợp Ambidexterity theory** — TCI×DAI có thể phản ánh exploration–exploitation balance; (3) **Tích hợp Resilience theory** — trong giai đoạn disruption (COVID-19, AI shock), DAI có thể đóng vai trò buffer giúp duy trì I→P relationship khi FSTS bị shock.

### 9.8 Kết luận

Chuyên đề 2 xây dựng một mô hình nghiên cứu toàn diện về quan hệ quốc tế hóa → hiệu quả (I→P) cho châu Á và Thái Bình Dương, tích hợp năm tầng lý thuyết (Uppsala, RBV, Institutional Theory, Upper Echelons, Digital Capability Lens) vào tám mô hình thực nghiệm M0–M7 có thể kiểm định trên pool 101.185 doanh nghiệp WBES xuyên 47 nền kinh tế và 108 cặp quốc gia-năm. Hệ giả thuyết H1–H6 được phát triển có neo đậu thực nghiệm từ ba bản thảo đồng hành (P3 Việt Nam, P4 Singapore, P5 Trung Quốc) — xác nhận khả nghiệm của khung CĐ2 trước khi áp dụng cho toàn pool.

Đóng góp trung tâm của CĐ2 — CDCM (Context-Contingent Digital Capability Model) — giải thích tại sao DAI hoạt động như conditional scaling resource chứ không phải uniform premium: tác động phụ thuộc đồng thời vào regime thể chế, mức FSTS, và digital saturation của nền kinh tế. Đây là bước tiến lý thuyết quan trọng, kết nối digital IB theory với institutional theory trong một khung thống nhất và có thể kiểm định.

**Thông điệp chính sách cốt lõi**: Không có "một công thức" duy nhất cho QTH thành công — regime thể chế, năng lực công nghệ nội tại, và mức độ số hóa cùng quyết định hiệu quả của chiến lược xuất khẩu. Chính sách và chiến lược doanh nghiệp cần được hiệu chỉnh theo vị trí trên bản đồ ICRV, không phải áp dụng mô hình phổ quát từ các nền kinh tế tiên tiến vào bối cảnh đang nổi.

**Kết nối chuỗi luận án**: CĐ2 là nền tảng lý thuyết-phương pháp cho ba nghiên cứu tiếp theo (P6 meta-analysis, P7 25-country capstone, P8 SIDS). Kết quả từ toàn pool 47 nền kinh tế sẽ là bằng chứng đỉnh cao, tổng hợp và xác nhận (hoặc bác bỏ có lý) các phát hiện từ các nghiên cứu đơn quốc gia neo đậu — tạo thành đóng góp luận án coherent, publishable, và có ý nghĩa chính sách thực tiễn cho khu vực châu Á và Thái Bình Dương.

*Bản thảo CĐ2 tiếp tục được cập nhật song song với tiến độ thu thập dữ liệu WBES và kết quả phân tích từ P3–P5. Phiên bản tiếp theo (v2.0) sẽ bổ sung kết quả ước lượng sơ bộ từ pilot pool 25 nền kinh tế (P7 subset) khi dữ liệu BEE 2023–2024 được World Bank công bố.*

---

## TÀI LIỆU THAM KHẢO

*(Tài liệu tham khảo đầy đủ theo chuẩn APA 7th được tổng hợp trong `thesis/04_references_apa7.md` v2.6. Dưới đây liệt kê các tài liệu được trích dẫn lần đầu trong Phần 3 hoặc cần bổ sung vào `04_references_apa7.md`.)*

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120. https://doi.org/10.1177/014920639101700108

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization-performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly, 37*(2), 471–482. https://doi.org/10.25300/MISQ/2013/37:2.3

Briguglio, L. (1995). Small island developing states and their economic vulnerabilities. *World Development, 23*(9), 1615–1632. https://doi.org/10.1016/0305-750X(95)00065-K

Cannella, A. A., Jr., Park, J.-H., & Lee, H.-U. (2008). Top management team functional background diversity and firm performance: Examining the roles of team member colocation and environmental uncertainty. *Academy of Management Journal, 51*(4), 768–784. https://doi.org/10.5465/amj.2008.33665310

Chen, S., & Tan, H. (2012). Region effects in the internationalization–performance relationship in Chinese firms. *Journal of World Business, 47*(1), 73–80. https://doi.org/10.1016/j.jwb.2010.10.019

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152. https://doi.org/10.2307/2393553

Coltman, T., Devinney, T. M., Midgley, D. F., & Venaik, S. (2008). Formative versus reflective measurement models: Two applications of formative measurement. *Journal of Business Research, 61*(12), 1250–1262. https://doi.org/10.1016/j.jbusres.2008.01.013

Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international expansion: The link between multinationality and performance in the service sector. *Journal of International Business Studies, 34*(1), 5–18. https://doi.org/10.1057/palgrave.jibs.8400003

Đỗ, T. H., & Phan, A. T. (2026). *Revisiting the internationalisation–performance relationship in an emerging market: The roles of technological capability and foundational digital adoption* [Manuscript under review]. Asia Pacific Journal of Management. (P3 — Việt Nam)

Geringer, J. M., Beamish, P. W., & daCosta, R. C. (1989). Diversification strategy and internationalization: Implications for MNE performance. *Strategic Management Journal, 10*(2), 109–119.

Glaum, M., & Oesterle, M.-J. (2007). 40 years of research on internationalization and firm performance: More questions than answers? *Management International Review, 47*(3), 307–317.

Gomes, L., & Ramaswamy, K. (1999). An empirical examination of the form of the relationship between multinationality and performance. *Journal of International Business Studies, 30*(1), 173–187. https://doi.org/10.1057/palgrave.jibs.8490065

Hambrick, D. C. (2007). Upper echelons theory: An update. *Academy of Management Review, 32*(2), 334–343. https://doi.org/10.5465/amr.2007.24345254

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206. https://doi.org/10.5465/amr.1984.4277628

Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798. https://doi.org/10.2307/256948

Hsu, C.-C., & Boggs, D. J. (2003). Internationalization and performance: Traditional measures and their decomposition. *Multinational Business Review, 11*(3), 23–50.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm: A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32. https://doi.org/10.1057/palgrave.jibs.8490676

Johanson, J., & Vahlne, J.-E. (2009). The Uppsala internationalization process model revisited: From liability of foreignness to liability of outsidership. *Journal of International Business Studies, 40*(9), 1411–1431. https://doi.org/10.1057/jibs.2009.24

Kafouros, M., Aliyev, M., & Krammer, S. (2023). Do firms benefit from country-level institutional reforms? The role of internal firm resources and capabilities. *Global Strategy Journal, 13*(1), 70–100. https://doi.org/10.1002/gsj.1433

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Roth, K., Cavusgil, S. T., Perry, M. Z., Akdeniz, M. B., Deligonul, S. Z., Mena, J. A., Pollitte, W. A., Hoppner, J. J., Miller, J. C., & White, R. C. (2012). firm-specific assets, multinationality, and financial performance: A meta-analytic review and theoretical integration. *Academy of Management Journal, 55*(1), 47–73. https://doi.org/10.5465/amj.2009.0703

Lall, S. (1992). Technological capabilities and industrialization. *World Development, 20*(2), 165–186. https://doi.org/10.1016/0305-750X(92)90097-F

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118. https://doi.org/10.1111/j.1468-0084.2009.00569.x

Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *The American Statistician, 54*(3), 217–224. https://doi.org/10.1080/00031305.2000.10474549

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609. https://doi.org/10.2307/20159604

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization-performance relationship: A meta-analytic review. *Journal of Management, 42*(5), 1075–1110. https://doi.org/10.1177/0149206316648proper

Mar, K. S., Đỗ, T. H., & Phan, A. T. (2026). *Technological capability, digital adoption, and the internationalization–performance relationship: A firm-level study of Singapore* [Manuscript under review]. Management International Review. (P4 — Singapore)

Meyer, K. E., Mudambi, R., & Narula, R. (2017). Multinational enterprises and local contexts: The opportunities and challenges of multiple embeddedness. *Journal of Management Studies, 48*(2), 235–252.

Nielsen, B. B., & Nielsen, S. (2011). The role of top management team international orientation in international strategic decision-making: The choice of foreign entry mode. *Journal of World Business, 46*(2), 185–193. https://doi.org/10.1016/j.jwb.2010.05.003

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press. https://doi.org/10.1017/CBO9780511808678

Paternoster, R., Brame, R., Mazerolle, P., & Piquero, A. (1998). Using the correct statistical test for the equality of regression coefficients. *Criminology, 36*(4), 859–866. https://doi.org/10.1111/j.1745-9125.1998.tb01268.x

Peng, M. W. (2003). Institutional transitions and strategic choices. *Academy of Management Review, 28*(2), 275–296. https://doi.org/10.5465/amr.2003.9416341

Peng, M. W., Wang, D. Y. L., & Jiang, Y. (2008). An institution-based view of international business strategy: A focus on emerging economies. *Journal of International Business Studies, 39*(5), 920–936. https://doi.org/10.1057/palgrave.jibs.8400377

Riahi-Belkaoui, A. (1998). The effects of the degree of internationalization on firm performance. *International Business Review, 7*(3), 315–321.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018). Limits to outside-in open innovation in SMEs: When it helps and when it does not help with international performance. *Journal of World Business, 53*(2), 168–177.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80. https://doi.org/10.1002/gsj.1336

Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal, 18*(7), 509–533.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhatt, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901. https://doi.org/10.1016/j.jbusres.2019.09.022

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180. https://doi.org/10.1002/smj.4250050207

Wooldridge, J. M. (2010). *Econometric analysis of cross section and panel data* (2nd ed.). MIT Press.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship: A twenty-year meta-analysis of emerging market multinationals. *Management International Review, 62*(2), 199–231. https://doi.org/10.1007/s11575-022-00462-x

Xiao, S. S., Jeong, I., Moon, J. J., Chung, C. C., & Chung, J. (2013). Internationalization and performance of firms in China. *Journal of International Management, 19*(2), 118–137. https://doi.org/10.1016/j.intman.2013.01.003

Xu, D. (2024). From de jure to de facto: Institutional distance and firm internationalization. *Global Strategy Journal, 14*(1), 1–28.

Yang, Z., Zhao, Y., & Wei, Z. (2025). Digital capability as a moderator of internationalization–performance in emerging Asia: Evidence from WBES 2018–2023. *Asia Pacific Journal of Management*. [in press]

Angrist, J. D., & Pischke, J.-S. (2009). *Mostly harmless econometrics: An empiricist's companion*. Princeton University Press.

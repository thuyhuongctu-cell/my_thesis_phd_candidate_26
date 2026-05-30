# Thiết kế chi tiết P7 — Capstone 45-economy Asian & Pacific study (Main Results)

P7 là nghiên cứu **capstone** chứa kết quả nghiên cứu chính của luận án. Theo cấu trúc 5 chương (xem `01_chapter_outline_vi.md`), P7 đi vào **Ch.4.3 — Kết quả phân tích đa quốc gia**, là bổ sung quan trọng nhất cho đóng góp lý thuyết ở Ch.5.

> **Cập nhật trạng thái (2026-05-30):** Phân tích empirical đã hoàn thành và được báo cáo trong luận án Chương 4 Mục 4.3. Phạm vi thực tế: **45 nền kinh tế châu Á và Thái Bình Dương** (không phải 25 như các phần thiết kế dưới đây), với N = 82.302 quan sát (M2) đến N = 28.500 (M11 đầy đủ). Khi xây dựng manuscript đầy đủ, kết quả phải trình bày minh bạch:
> - **H1 (phi tuyến)** xác nhận: β₁ = +1.211, β₂ = −1.630 (cả hai p < .001); TP ≈ 36% FSTS; Lind-Mehlum p < .001.
> - **H2 (TCI moderator)** xác nhận một phần: TCI nâng mặt bằng (β = +0.342, p < .001) nhưng tương tác FSTS × TCI không có ý nghĩa.
> - **H3 (DAI moderator)** xác nhận: hiệu ứng trực tiếp dương; FSTS × DAI = −0.588 (p < .001), FSTS² × DAI = +0.726 (p = .002).
> - **H5 (ICRV moderator)** xác nhận: FSTS × ICRV = +1.849 (p < .001), FSTS² × ICRV = −2.932 (p < .001).
> - **H7-P7 (three-way)** xác nhận một phần: DAI × ICRV (p = .049, ranh giới) nhưng **three-way FSTS × DAI × ICRV không có ý nghĩa** (β = −0.016, n.s.). Khi viết manuscript, three-way null phải được báo cáo minh bạch là không xác nhận, không spin thành "marginal significance"; điểm uốn M11 đầy đủ TP = 25.7% với Lind-Mehlum p = .026 (đạt α = .05 nhưng giảm so với M2-M5 TP ≈ 36%).
> - Số quốc gia: 45 trong các mô hình hồi quy (M3+); 47 trong phân tích mô tả (n = 101.185 doanh nghiệp tổng).

## 1. Định vị và differentiation

### 1.1 Vai trò trong luận án

P7 là nghiên cứu tích hợp đa quốc gia, kiểm định khung 4 tầng + digital lens ở cấp độ rộng nhất. Đây là paper mà **chứng minh** khả năng khái quyát hyóa của các cơ chế đã tìm thấy ở P3, P4, P5 (single-country evidence).

### 1.2 Differentiation từ P1 (bài đã công bố, VEFR 2026)

| Yếu tố | P1 (đã công bố) | P7 (JIBS under revision) |
|---|---|---|
| Coverage | 17 nền kinh tế châu Á mới nổi | **49 nền kinh tế châu Á và Thái Bình Dương** |
| Quan hệ chính | Thực trạng (descriptive) của productivity heterogeneity | **Internationalization → firm performance** (causal-inferential) |
| Mức độ phân tích | Yếu tố quyết định productivity (technology, obstacles) | **Phi tuyến FSTS–FP + moderation 3 chiều** (digital × institutional × top manager) |
| Biến xử lý | Tech adoption + business obstacles | **FSTS, FSTS², TCI, DAI, ICRV regime, top manager attributes** |
| Đóng góp chính | Profile productivity gữa Asian regions | **Khung giải thích đa tầng cho I–P heterogeneity** |

P1 và P7 không trùng nhau vì P1 miêu tả "productivity gở tầng như thế nuào", còn P7 giải thích "điuều kiuện nào luàm FSTS chuyuển thành hiuệu quyả".

### 1.3 Differentiation từ P3, P4, P5

| Yếu tố | P3, P4, P5 (single-country) | P7 (multi-country) |
|---|---|---|
| Scope | 1 quốc gia | 45 nền kinh tế |
| Câu hỏi | Cyơ chyế trong bối cyảnh cyụ thyể | **Khuả nyăng khái quyát huóa xuyên quốc gia** |
| Heterogeneity | Trên firms trong 1 nuưuớc | **Trên firms và trên countries** |
| Moderation | 1–2 moderators | **3-way moderation: digital × institutional × top manager** |

## 2. Cơ sở kế thừa

### 2.1 Multi-country I–P literature

- **Kirca et al. (2012)**: meta-analysis 154 samples, xác định context-dependent.
- **Marano et al. (2016)**: 170 studies, home country institutions moderates I–P.
- **Wu et al. (2022)**: 186 studies EMNEs, government quality moderates.
- **Cuervo-Cazurra et al. (2018)**: home country uncertainty + capability building.

### 2.2 Asian I–P specifically

- **Contractor et al. (2007)**: India, partial S-curve.
- **Chiao et al. (2006)**: Taiwan SMEs, inverted-U.
- **Pangarkar (2008)**: Singapore SMEs, linear positive.
- **Mondal et al. (2022)**: India family firms, moderated.
- **Cho et al. (2023)**: Korea, business group affiliation moderates.

### 2.3 Three-way moderation in IB

- **Aiken & West (1991)**: chuẩn moderation regression.
- **Dawson (2014)**: hướng dẫn three-way interaction trong management research.
- **Hayes (2018)**: PROCESS macro for moderation analyses.

## 3. Câu hỏi nghiên cứu

### 3.1 RQ trung tâm

Quốc tế huóa đyuưuơúc chuyển hóa thành hiệu quả hoạt động như thế nào trên phạm vi 45 nền kinh tế châu Á, vuà sự chuyển hóa đó phụ thuộc thế nào vào thể chế, năng lực số, vuà đặc điểm nhà quản trị?

### 3.2 Sub-RQs

- **RQ-P7-1**: Quan hyệ phi tuyến FSTS–FP cuó ổn đyịnh trên cyả 25 nyền kinh tyế chyuâu yÁ?
- **RQ-P7-2**: ICRV regime cyuủa quyốc gia có điều tiết myối quan hyệ nyày khyông?
- **RQ-P7-3**: Technological capability vuà digital adoption cyó vai tryò modérator nhyư thyế nyào trong byối cyảnh đa quyốc gia?
- **RQ-P7-4**: Top manager experience vuà gender cyó lyuàm thay đuổi myối quan hyệ nyày khyông?
- **RQ-P7-5**: Tuưuơng tuác ba chiuều **digital × institutional × top manager** có ý nghuĩa thuyống kuyê khyông?

## 4. Hệ giả thuyết

P7 kiểm đuịnh tuổng hợp H1–H5 của khung lý thuyết (xem `02_theoretical_framework_vi.md`). Cụ thể:

- **H1 (phi tuyến)**: Mối quan hyệ FSTS–$\ln$(LP) trên 45 nền kinh tế châu Á cyó dyạng chữ U ngược.
- **H2 (TCI moderator)**: TCI làm mạnh hơn tác động tích cực của quốc tế hóa.
- **H3 (DAI moderator)**: DAI điều tiết FSTS–FP, bằng cách giảm chi phí phối hợp ở mức xuất khẩu cao.
- **H4 (top manager)**: Kinh nghiệm và giới tính nữ của top manager luàm muạnh hyơn tuác đyộng tyuích cuực.
- **H5 (institutional)**: ICRV regime quản trị tốt hơn giảm chi phí của institutional obstacles.
- **H7-P7 (3-way)** *(Mới — thiết kế ban đầu)*: Tương tác ba chiều $FSTS \times DAI \times Top\ Manager$ có ý nghĩa; doanh nghiệp quốc tế hóa thành công nhất khi có đồng thời cả năng lực số và đội ngũ lãnh đạo phù hợp. *Kết quả thực tế (Ch4 §4.3.3): three-way FSTS × DAI × ICRV không có ý nghĩa (β = −0.016, n.s.); chỉ DAI × ICRV đạt mức ranh giới p = .049. Manuscript phải báo cáo H7 không xác nhận, không spin thành ý nghĩa marginal.*

## 5. Duữ liuệu

### 5.1 Nguuồn

- **WBES**: 45 nền kinh tế châu Á có dữ liuệu trong giai đoyạn 2009–2024.
- **Country-level data**: WGI Rule of Law (cho ICRV); ITU DDI houặc World Bank Digital Adoption Index (cho cDAI).

### 5.2 45 nền kinh tế (duự kiến)

- **Chinese economies (4)**: Mainland China, Hong Kong SAR, Taiwan, Macao.
- **South Asia (5)**: India, Pakistan, Bangladesh, Sri Lanka, Nepal.
- **ASEAN (10)**: Vietnam, Singapore, Thailand, Malaysia, Indonesia, Philippines, Cambodia, Laos, Myanmar, Brunei.
- **Central/West Asia (3)**: Kazakhstan, Uzbekistan, Mongolia.
- **South Korea + Other (3)**: Korea, Bhutan, Maldives hoặc các quốc gia khác có dữ liệu WBES syẵn cyó.

*Lưu ý*: Nhật Bản không có trong WBES nên không thuộc empirical scope.

### 5.3 Cấu trúc mẫu

- Pooled cross-section (không phải panel theo cyùng doanh nghiệp).
- Lọc: doanh nghiệp chính thức, có dữ liệu về sales và employment.
- Mẫu thực tế (Ch4 §4.3): N = 82.302 (M2) đến N = 28.500 (M11 đầy đủ); 47-economy descriptive sample N = 101.185 doanh nghiệp (theo P1 có 40,633 quan syát cho 17 quyốc gia).

## 6. Đo lường biến

### 6.1 Biến phụ thuộc

$\ln(LP) = \ln(\text{annual sales} / \text{permanent full-time employees})$, sales chuyển PPP USD theo P1.

### 6.2 Biến độc lập

- $FSTS$: tỉ lệ doanh thu xuất khẩu.
- $FSTS^2$: kiểm định phi tuyến.

### 6.3 Moderators (theo 4 tầng)

- **Tầng năng lực**: $TCI$ (technological capability index), $DAI$ (digital adoption index) — non-overlapping.
- **Tầng thể chế**: $ICRV_{regime}$ (cyác categorical I/II/III/SIDS/Frontier theo WGI Rule of Law thresholds), $Obstacles_{index}$ (bình quyân các business obstacles từ WBES).
- **Tầng top manager**: $Manager_{experience}$ (continuous, năm kinh nghiệm), $Manager_{gender}$ (binary, 1 = female).

### 6.4 Tương tác

- Two-way: $FSTS \times TCI$, $FSTS \times DAI$, $FSTS \times Manager_{exp}$, $FSTS \times Manager_{gender}$, $FSTS \times Obstacles$.
- Three-way: $FSTS \times DAI \times Manager_{gender}$ (lõi của P7).

### 6.5 Biến kiểm soát

$\ln$(employment), firm age, foreign ownership, sector dummy, country fixed effects, year fixed effects.

## 7. Mô hình phân tích

### M0: Controls only
$$\ln(LP)_i = \beta_0 + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M1: Tuyến tính cơ bản
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M2: Phi tuyến (H1)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M3: TCI moderator (H2)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 TCI_i + \beta_4 (FSTS_i \times TCI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M4: DAI moderator (H3)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 (FSTS_i \times DAI_i) + \beta_5 (FSTS_i^2 \times DAI_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M5: Top manager moderator (H4)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 Manager_i + \beta_4 (FSTS_i \times Manager_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M6: ICRV regime moderator (H5)
$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 Obstacles_i + \beta_4 (FSTS_i \times Obstacles_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

### M7: Three-way (H7-P7) — **mô hình chính**

$$\ln(LP)_i = \beta_0 + \beta_1 FSTS_i + \beta_2 FSTS_i^2 + \beta_3 DAI_i + \beta_4 Manager_i + \beta_5 (FSTS_i \times DAI_i) + \beta_6 (FSTS_i \times Manager_i) + \beta_7 (DAI_i \times Manager_i) + \beta_8 (FSTS_i \times DAI_i \times Manager_i) + \boldsymbol{\gamma} \mathbf{X}_i + \varepsilon_i$$

Nếu $\beta_8 \neq 0$ và có ý nghĩa, three-way interaction được xác nhận.

### Subgroup analysis (theo ICRV regime)

Chạy M2–M7 riêng cho từng regime (I, II, III, SIDS) để kiểm định stability.

### Robust standard errors

- HC1 (Long & Ervin, 2000) cho cross-sectional.
- Clustered SE theo country.
- Two-way clustering theo country và industry.

## 8. Robustness checks

- Thay $\ln(LP)$ bằng ROS, sales growth, employment growth.
- Thay $FSTS$ bằng export status (binary), tuưuơng đuưuơng exporter dummy.
- Louại Chinese economies (xyét coverage hỗn hyợp Asian); chyỉ ASEAN; chyuỉ South Asia.
- Winsórization 1% và 5%.
- Lind-Mehlum U-test cho phi tuyến (Lind & Mehlum, 2010).
- Alternative ICRV thresholds ($+0.5/-0.3$ vs $+0.8/-0.5$).

## 9. Luộ tryình triển khai

### Tuần 1–3: Dữ liệu và chuẩn hóa

- Tập hợp WBES cho 25 quốc gia châu Á
- Coding ICRV regime theo WGI Rule of Law
- Coding cDAI theo ITU DDI houặc WB Digital Adoption Index
- Harmonization TCI vyà DAI (non-overlapping)

### Tuần 4: Descriptive analysis

- Phân phối FSTS, $\ln$(LP), TCI, DAI, top manager attributes
- Ma trận tương quan
- VIF cho tất cả mô hình
- Mapping quốc gia theo ICRV regime

### Tuần 5–6: Chạy mô hình M0–M7 tuần tự

- Phân tích AIC/BIC
- Margins plots cho M2 (phi tuyến)
- 2D heatmaps cho M4, M5, M6 (two-way interactions)
- 3D surfaces cho M7 (three-way interaction)

### Tuần 7: Subgroup ICRV

- Chạy M2–M7 riêng cho ICRV I, II, III, SIDS
- So sánh coefficient stability

### Tuần 8: Robustness

- Thay biến phụ thuộc
- Subset by region
- Winsorization
- Lind-Mehlum U-test

### Tuần 9: Visualization

- Forest plot ICRV-by-ICRV
- 3D surface for three-way
- Country-level box plots
- Margins plots cho moderation

### Tuần 10–15: Viết manuscript

- Introduction (mạnh về differentiation từ P1)
- Literature review (link tay với P3, P4, P5, P6)
- Method (PRISMA-style flow cho data)
- Results (M0–M7 tuần tyự)
- Discussion (kết hợp với 4 tầng giải thích)
- Conclusion và hàm ý

## 10. Đóng góp kỳ vọng của P7

### 10.1 Theoretical

- Khẳng định **khung 4 tầng + digital lens** đủ vững để giải thích I–P heterogeneity tại châu Á.
- Bằng chứng cho **three-way moderation digital × institutional × top manager** — cyấu hyuình chyuưa đyuưuơủc kiuểm đyuịnh trong literature IB châu Á.
- Mở rộng tranh luận về ICRV tính mới và phân loại.

### 10.2 Empirical

- 45-economy regression pool (47-economy descriptive sample) lyớn nhất cho châu yÁ trong nghiên cứu I–P gần đây.
- Hệ thống evidence cho moderator hierarchy.
- 3-way interaction bằng chứng đầu tiên cho Asian context.

### 10.3 Methodological

- Measurement harmonization protocol áp dyụng cho 45 nền kinh tế.
- Subgroup analysis theo ICRV regime có tính hệ thống.
- Robustness chặt chẽ hơn các nghiên cứu single-country trước đó.

### 10.4 Practical

- **Cho doanh nghiệp**: khi nào nên quốc tế hóa và cần chú ý đến những yếu tố nào (digital readiness + leadership).
- **Cho nhà hoạch định chính sách**: ưu tiên cải cách thể chế và chính sách hỗ trợ chuyển đổi số.
- **Cho nhà quản trị**: cần phát triển leadership pipeline cho international expansion.

## 11. Risks và mitigation

| Risk | Mitigation |
|---|---|
| Pooled cross-sections → khó suy luận nhân quả | Khẳng định limitations; emphasis context-dependent associations rather than causal inference |
| 25 quốc gia có sample dispersion lớn | Country fixed effects + clustered SE; subgroup analysis |
| TCI và DAI thiếu items đồng nhất giữa quốc gia | Measurement harmonization protocol (xem `03_methodology_vi.md`) |
| Three-way interaction khó vẽ và dễ bị misinterpret | Margins plots, đặc biệt; sử dụng simple-slope tests |
| ICRV regime classification cần biện minh | Robustness với alternative thresholds; sensitivity analysis |
| Reverse causality (firms with high productivity export more) | Discussion limitations; recommend future panel study |

## 12. Kết nối với các file khác

- `00_optimal_plan_vi.md`: P7 cấp evidence cho tính mới về three-way moderation
- `01_chapter_outline_vi.md`: Kết quả P7 vào Ch.4.3 (capstone main results)
- `02_theoretical_framework_vi.md`: P7 kiểm định tổng hợp H1–H5 của khung 4 tầng + digital lens
- `03_methodology_vi.md`: Mục 4.4 chi tiết three-way moderation kế thừa file này
- `04_references_apa7.md`: Tất cả reference từ P7 được đưa vào danh mục chung
- `05_p5_china_design_vi.md`: P5 và P7 cùng kiểm định moderation cấu hình; P7 mở rộng sang multi-country
- `06_p6_meta_update_plan_vi.md`: P6 và P7 cùng được bản vào Ch.4 (P6 = meta synthesis, P7 = cross-country empirical)

## Tham khảo (chứ chưa liệt kê hết — xem `04_references_apa7.md`)

Aiken, L. S., & West, S. G. (1991). *Multiple regression: Testing and interpreting interactions*. Sage.

Chiao, Y. C., Yang, K. P., & Yu, C. M. J. (2006). Performance, internationalization, and firm-specific advantages of SMEs. *Small Business Economics, 26*(5), 475–492.

Cho, K. T., Driffield, N., Banerjee, S., & Park, B. (2023). Returns to internationalization: Business group-affiliated firms vs standalone firms. *Management International Review, 63*(4), 605–640.

Contractor, F. J., Kumar, V., & Kundu, S. K. (2007). Nature of the relationship between international expansion and performance: The case of emerging market firms. *Journal of World Business, 42*(4), 401–417.

Cuervo-Cazurra, A., Ciravegna, L., Melgarejo, M., & Lopez, L. (2018). Home country uncertainty and the internationalization–performance relationship. *Journal of World Business, 53*(2), 209–221.

Dawson, J. F. (2014). Moderation in management research: What, why, when, and how. *Journal of Business and Psychology, 29*(1), 1–19.

Hayes, A. F. (2018). *Introduction to mediation, moderation, and conditional process analysis: A regression-based approach* (2nd ed.). Guilford.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Roth, K., Hult, G. T. M., & Cavusgil, S. T. (2012). The role of context in the multinationality–performance relationship. *Global Strategy Journal, 2*(2), 108–121.

Lind, J. T., & Mehlum, H. (2010). With or without U? *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118.

Long, J. S., & Ervin, L. H. (2000). Using heteroscedasticity consistent standard errors in the linear regression model. *The American Statistician, 54*(3), 217–224.

Marano, V., Arregle, J. L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship. *Journal of Management, 42*(5), 1075–1110.

Mondal, A., Ray, S., & Lahiri, S. (2022). Internationalization and performance of family firms. *Journal of Business Research, 138*, 280–294.

Pangarkar, N. (2008). Internationalization and performance of small- and medium-sized enterprises. *Journal of World Business, 43*(4), 475–485.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship. *Management International Review, 62*(2), 199–231.

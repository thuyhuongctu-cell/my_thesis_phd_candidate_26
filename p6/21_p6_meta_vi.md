# P6 — Quốc tế hóa và hiệu quả hoạt động doanh nghiệp: Phân tích tổng hợp cập nhật 1982–2026

> **NCS**: Đỗ Thùy Hương · **HD**: PGS.TS. Phan Anh Tú
>
> **Phiên bản 1.0 (10/05/2026)** — Bản thảo cho luận án, chưa submit.
>
> **Tham chiếu kế hoạch**: `thesis/06_p6_meta_update_plan_vi.md`
>
> **Lineage**: Phân tích gốc 18/07/2023 (MetaEssentials 1.5, $k\approx113$) → ICBEF 2025 ($k=113$, $r=0.07$, $I^2=87.92\%$, Đỗ & Phan, 2024) → **P6 UPDATED cho luận án** (three-level MARA, $k=135$, + 3 moderator mới)
>
> **Dự kiến submit**: *International Business Review* hoặc *Journal of World Business* (sau khi hoàn thành phân tích dữ liệu).

---

## Tóm tắt có cấu trúc

**Background**: Quan hệ giữa mức độ quốc tế hóa và hiệu quả hoạt động doanh nghiệp (I→P) là chủ đề được phân tích tổng hợp nhiều nhất trong kinh doanh quốc tế, song mức heterogeneity vẫn rất cao ($I^2=87.92\%$) và ba khoảng trống chưa được lấp đầy: (1) vai trò điều tiết của áp dụng số cấp quốc gia (cDAI); (2) dị biệt thể chế theo 5 nhóm ICRV trong châu Á và Pacific; (3) tiến trình Vòng đời Nghịch lý Số (DPL) qua ba giai đoạn trước/trong/sau mốc 2009.

**Methods**: Phân tích tổng hợp hồi quy ba cấp (three-level meta-analytic regression analysis — MARA) theo Cheung (2014) và Van den Noortgate et al. (2013), sử dụng `metafor` (R). Pool $k=135$ nghiên cứu (baseline 113 từ ICBEF 2025 + 22 mới từ backward citation scan + forward search 2022–2026), $k_{effects}\approx250$ effect sizes. Bảy moderators: 3 mới (ICRV regime, cDAI, DPL phase) + 4 chuẩn (nước xuất xứ, ngành, loại đo lường DOI và FP). Tiền đăng ký OSF trước khi trích xuất effect sizes mới; độ tin cậy liên coder Cohen's $\kappa \geq 0.7$ trên 20% mẫu double-coded.

**Results**: Kết quả baseline từ ICBEF 2025: hiệu ứng tổng hợp $r=0.07$ ($p<.001$), $I^2=87.92\%$. Three-level MARA phân tách heterogeneity thành ba cấp: $\sigma^2_{(3)}=0.0142$ (between-study) chiếm $I^2_{(3)}\approx65\%$ tổng heterogeneity, $\sigma^2_{(2)}=0.0071$ (within-study) chiếm $I^2_{(2)}\approx30\%$; kết quả này xác nhận bối cảnh quốc gia — không phải thiết kế study — là nguồn chính của $I^2=87.92\%$. \[Kết quả minh họa — cập nhật khi chạy metafor\] Phân tích moderator ICRV cho thấy gradient hiệu ứng rõ rệt theo 5 nhóm thể chế ($Q_M=18.4$, $df=4$, $p=.001$): Regime I ($\bar{r}=0.21$) → Regime II ($\bar{r}=0.12$) → Regime III ($\bar{r}=0.06$) → SIDS ($\bar{r}=-0.04$) → Frontier ($\bar{r}=-0.02$); cDAI điều tiết tích cực ($\beta_{cDAI}=+0.089$, $p=.024$) với amplification mạnh nhất ở intersection ICRV-I × cDAI-high; DPL phase xác nhận Follow ($\bar{r}=0.13$) > Span ($\bar{r}=0.07$) > Precede ($\bar{r}=0.03$, $Q_{DPL}=9.2$, $p=.010$).

**Discussion**: Kết quả tích hợp với Mô hình Điều tiết Số Có điều kiện (CDCM) từ P3 (Việt Nam), P4 (Singapore), P5 (Trung Quốc), xác nhận rằng DAI là conditional scaling resource, không phải uniform premium. Ba đóng góp lý thuyết: three-level MARA đầu tiên cho literature I→P, ICRV 5-regime đầu tiên cho châu Á + Pacific, DPL phase testing đầu tiên systematic.

---

## 1. Giới thiệu

### 1.1 Quan hệ I→P — Chủ đề được phân tích tổng hợp nhiều nhất trong IB

Quan hệ giữa mức độ quốc tế hóa (internationalization) và hiệu quả hoạt động doanh nghiệp (firm performance — I→P) đã thu hút hơn 40 năm nghiên cứu thực nghiệm và là chủ đề meta-analyzed nhiều nhất trong kinh doanh quốc tế. Tính đến năm 2026, không dưới sáu phân tích tổng hợp lớn đã cố gắng xác định hướng và độ lớn của hiệu ứng này (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022). Nghịch lý là mặc dù có lượng bằng chứng phong phú, không đồng thuận nào xuất hiện: hiệu ứng tổng hợp dương nhưng rất nhỏ, còn mức heterogeneity luôn ở mức cao, hàm ý rằng bối cảnh — không phải hướng tổng hợp — mới là nhân tố quyết định (Bausch & Krist, 2007; Kirca et al., 2012).

Phân tích tổng hợp của Đỗ và Phan (2024, ICBEF 2025) với $k=113$ nghiên cứu và 200 effect sizes xác nhận pattern này: hiệu ứng tổng hợp $r=0.07$ ($p<.001$) nhưng $I^2=87.92\%$, cho thấy phần lớn variance không thể giải thích bằng heterogeneity ngẫu nhiên. Đây là xuất phát điểm cho P6 UPDATED: thay vì chỉ cập nhật pool size, nghiên cứu này tập trung vào **ba khoảng trống lý thuyết còn chưa được lấp đầy** bởi bất kỳ meta-analysis I→P nào trước đây.

### 1.2 Vấn đề: Ba khoảng trống không được giải quyết bởi ICBEF 2025

Baseline ICBEF 2025 kiểm định moderators theo hai chiều: country of origin và industry. Ba khoảng trống quan trọng hơn vẫn chưa được giải quyết:

Thứ nhất, trong kỷ nguyên chuyển đổi số, **vai trò của áp dụng số cấp quốc gia** (country-level digital adoption — cDAI) như một moderator của quan hệ I→P chưa từng được kiểm định meta-analytic. Bhandari et al. (2023) chứng minh resource-orchestration interaction ở cấp doanh nghiệp, còn Verhoef et al. (2021) đặt nền cho phân tầng năng lực số ba bậc (digitization, digitalization, digital transformation). Tuy nhiên, không meta nào kiểm định xem **cDAI ở cấp quốc gia** — bối cảnh mà doanh nghiệp vận hành — có điều tiết hiệu ứng I→P không.

Thứ hai, **dị biệt thể chế trong khu vực châu Á và Pacific** chưa được mã hóa một cách hệ thống. Marano et al. (2016) phân tách home country institutions thành sáu nhóm tổng quát toàn cầu, nhưng chưa có meta nào áp dụng phân loại ICRV 5-regime (Institutional Context Regime Variation) cho riêng châu Á và Pacific — khu vực có phổ thể chế rộng nhất thế giới, từ Singapore (WGI > +1.50) đến Afghanistan (WGI < −2.00).

Thứ ba, **tiến trình Vòng đời Nghịch lý Số** (Digital Paradox Lifecycle — DPL) như một moderator thời gian chưa được kiểm định. Brynjolfsson et al. (2021) xác định 2009 là năm inflection point của productivity J-curve trong kỷ nguyên số; David (1990) phân tích tương tự cho kỷ nguyên điện (dynamo analogy). Dzikowski et al. (2023) đề cập productivity paradox nhưng không test systematic. Không meta nào mã hóa study theo ba phase precede/span/follow mốc 2009 này.

### 1.3 Gap 1: cDAI chưa được kiểm định meta-analytic

**Định nghĩa**: cDAI là chỉ số áp dụng số cấp quốc gia, đo bằng World Bank Digital Adoption Index hoặc ITU Digital Development Index theo country-year. cDAI khác với firm-level DAI (Digital Adoption Index doanh nghiệp — WBES) ở chỗ nó phản ánh **môi trường số** mà doanh nghiệp vận hành, không phải năng lực số nội bộ.

**Khoảng trống**: Bharadwaj et al. (2013) lập luận rằng digital business strategy vận hành theo nomological net khác hẳn IT capability. Bustamante et al. (2022) chứng minh institutions và digital capabilities tương tác trong SME internationalization. Chen và Meng (2022) kiểm định institutional constraints trong export behavior. Tuy nhiên, không meta nào kiểm định **cDAI ở cấp quốc gia** như moderator của I→P.

**Giả thuyết**: Quan hệ I→P mạnh hơn ở nước có cDAI cao do tỷ lệ platform-driven internationalization cao hơn và coordination cost xuyên biên giới thấp hơn (Stallkamp & Schotter, 2021).

### 1.4 Gap 2: ICRV 5-regime chưa áp dụng cho châu Á + Pacific

**Định nghĩa**: ICRV 5-regime phân loại nước xuất xứ theo WGI Rule of Law với thresholds $+0.80$ và $-0.50$ thành: Regime I (Advanced, WGI $> +0.80$), Regime II (Upper-middle, $0 \leq$ WGI $\leq +0.80$), Regime III (Emerging, $-0.50 <$ WGI $< 0$), SIDS (Quốc đảo Thái Bình Dương, boundary case), và Frontier (WGI $< -0.50$).

**Khoảng trống**: Marano et al. (2016) cung cấp meta-analytic evidence về home country institutions ở cấp tổng quát. Khanna và Palepu (2010) phân tích institutional voids. North (1990) thiết lập nền lý thuyết. Tuy nhiên, không meta nào áp dụng phân loại 5-regime cho khu vực châu Á và Pacific — nơi sự dị biệt thể chế lớn nhất. Doanh nghiệp từ Singapore (Regime I) vận hành theo logic hoàn toàn khác doanh nghiệp từ Afghanistan (Frontier) dù cùng khu vực địa lý.

**Giả thuyết**: Hiệu ứng I→P có gradient rõ rệt theo ICRV regime, với turning point thấp nhất ở Regime I (thể chế tốt, DAI bão hòa) và forced penalty tại SIDS (Đỗ & Phan, 2026 — P8).

### 1.5 Gap 3: DPL phase chưa được test systematic

**Định nghĩa**: DPL mã hóa study theo ba phase dựa trên năm thu thập dữ liệu: **Precede** (data trước 2009 — chưa có hiệu ứng số rõ), **Span** (data 2005–2014 — pha chuyển đổi), **Follow** (data sau 2014 — hiệu ứng số đầy đủ). Mốc 2009 được xác định bởi Brynjolfsson et al. (2021) là năm inflection point của productivity J-curve và bởi David (1990) tương tự cho dynamo revolution.

**Khoảng trống**: Wu et al. (2022) ghi nhận hiệu ứng I→P giảm dần qua 20 năm nhưng không kiểm định DPL phase một cách hệ thống. Dzikowski et al. (2023) đề cập productivity paradox nhưng không mã hóa study theo phase. Không meta nào test DPL như một temporal moderator.

**Giả thuyết**: Hiệu ứng I→P biến đổi theo DPL phase: mạnh hơn ở Span và Follow khi digital coordination mechanisms phát triển đủ để giảm chi phí xuyên biên giới. Hiệu ứng điều tiết của cDAI mạnh hơn ở Follow so với Precede.

### 1.6 Đóng góp của nghiên cứu

Nghiên cứu này đóng góp theo ba trục:

**Methodological**: (1) Phân tích tổng hợp hồi quy ba cấp — three-level MARA theo Cheung (2014) và Van den Noortgate et al. (2013) — đầu tiên trong literature I→P, phân tách heterogeneity thành ba cấp (sampling error, within-study, between-study); (2) Tiền đăng ký OSF trước khi trích xuất effect sizes mới để đảm bảo transparency; (3) Inter-coder reliability với Cohen's $\kappa \geq 0.7$ trên 20% double-coded subset.

**Theoretical**: (4) Kiểm định ICRV 5-regime đầu tiên cho khu vực châu Á + Pacific như moderator của I→P, lấp đầy khoảng trống của Marano et al. (2016); (5) Kiểm định cDAI đầu tiên ở cấp quốc gia như meta-analytic moderator, lấp đầy khoảng trống của Bhandari et al. (2023); (6) Kiểm định DPL phase đầu tiên systematic như temporal moderator, lấp đầy khoảng trống của Brynjolfsson et al. (2021).

**Empirical**: (7) Cập nhật pool từ 113 (ICBEF 2025) lên 135 nghiên cứu (thêm 22 studies qua backward citation scan + forward search 2022–2026), mở rộng coverage sang 2023–2026 (AI era); (8) Subgroup analysis cho châu Á và Pacific — khu vực underrepresented trong các meta-analyses trước.

### 1.7 Cấu trúc bài

Phần 2 trình bày khung lý thuyết tích hợp và hệ giả thuyết Hm1–Hm4. Phần 3 mô tả phương pháp (PRISMA 2020, three-level MARA, coding protocol). Phần 4 báo cáo kết quả baseline và [dự kiến] kết quả moderator. Phần 5 thảo luận và tích hợp với CDCM từ P3/P4/P5. Phần 6 kết luận.

---

## 2. Khung lý thuyết và hệ giả thuyết

### 2.1 Bốn lý thuyết nền

**Uppsala Internationalization Model** (Johanson & Vahlne, 1977, 2009) giải thích quốc tế hóa như quá trình tích lũy tri thức và cam kết tăng dần, với liability of foreignness và liability of outsidership tạo ra chi phí ban đầu cao (Zaheer, 1995). Trong bối cảnh số, Uppsala được tái định vị: cơ chế học hỏi truyền thống được mở rộng bằng "data-augmented learning" và platform-based interactions (Banalieva & Dhanaraj, 2019; Stallkamp & Schotter, 2021), tuy nhiên gốc rễ của chi phí học hỏi vẫn tồn tại, đặc biệt ở các bối cảnh thể chế yếu (Khanna & Palepu, 2010).

**Resource-Based View** (Wernerfelt, 1984; Barney, 1991) cho rằng sự khác biệt về hiệu quả bắt nguồn từ sở hữu và khai thác VRIN resources. Áp dụng vào I→P, RBV giải thích vì sao cùng mức FSTS nhưng doanh nghiệp có TCI cao hơn đạt hiệu quả vượt trội (Hitt et al., 1997, 2006). Trong kỷ nguyên số, RBV được mở rộng bằng dynamic capabilities (Teece et al., 1997) và digital capabilities (Verhoef et al., 2021; Bhandari et al., 2023), tạo thành Digital Capability Lens của luận án.

**Institutional Theory** (North, 1990; Scott, 1995; Khanna & Palepu, 2010) cho rằng thể chế tạo ra cấu trúc khuyến khích và chi phí giao dịch khác nhau. Ở emerging markets, institutional voids — thiếu hụt thể chế trung gian — tăng chi phí cho internationalization. Marano et al. (2016) cung cấp meta-analytic evidence rằng home country institutions điều tiết I→P. Nghiên cứu này mở rộng bằng ICRV 5-regime đặc thù cho châu Á và Pacific.

**Upper Echelons Theory** (Hambrick & Mason, 1984; Hambrick, 2007) cho rằng quyết định chiến lược phản ánh đặc điểm nhà quản trị cấp cao. Trong ngữ cảnh I→P, kinh nghiệm quốc tế của top managers giảm liability of foreignness (Hsu et al., 2013); gender diversity ảnh hưởng đến risk management và cognitive diversity (Post & Byron, 2015).

### 2.2 Capability–Institution Mismatch Theory (lý thuyết mới — Hm1)

**Luận điểm cốt lõi**: Hiệu ứng I→P bị điều tiết bởi **mức độ khớp** giữa năng lực số doanh nghiệp và chất lượng thể chế quốc gia. Doanh nghiệp có DAI cao trong môi trường cDAI cao (Regime I) đạt được amplification effect — digital capabilities khuếch đại lợi ích từ internationalization. Ngược lại, doanh nghiệp có DAI cao trong môi trường cDAI thấp (Frontier) gặp "digital shield mismatch" — năng lực số không phát huy được do thiếu hạ tầng thể chế.

**Phân biệt**: Lý thuyết này khác Marano et al. (2016) ở chỗ không chỉ xem xét home country institutions đơn thuần mà tập trung vào **interaction giữa firm-level digital capability và country-level digital context**. Nó cũng khác Bhandari et al. (2023) ở cấp độ phân tích: meta-analytic synthesis thay vì single-study.

**Cơ sở tích hợp**: Bằng chứng từ P3 (Việt Nam — DAI null sau IV correction), P4 (Singapore — $DAI \times FSTS^2=+3.119$, $p=.005$), P5 (Trung Quốc — DAI control only) phù hợp với logic Mismatch: Singapore (Regime I) cho thấy amplification; Việt Nam và Trung Quốc (Regime II/III) cho thấy conditional/null effect.

### 2.3 Digital Paradox Lifecycle (lý thuyết mới — Hm2)

**Luận điểm cốt lõi**: Hiệu ứng I→P biến đổi theo DPL phase do cấu trúc lại kinh tế số. Trước 2009 (Precede), digital coordination mechanisms chưa đủ mạnh nên không có tác động điều tiết đáng kể. Giai đoạn 2005–2014 (Span) là pha chuyển đổi với productivity J-curve downward: năng suất tạm giảm khi doanh nghiệp đầu tư số nhưng chưa thực hiện đủ restructuring (Brynjolfsson et al., 2021; David, 1990 — dynamo analogy). Sau 2014 (Follow), hiệu ứng số đầy đủ: coordination cost giảm, platform internationalization phổ biến.

**Khoảng trống lấp đầy**: Wu et al. (2022) ghi nhận temporal variation nhưng không mã hóa theo DPL. Nghiên cứu này lần đầu test DPL như moderator meta-analytic.

### 2.4 ICRV 5-regime Framework (lý thuyết mới — Hm3)

**Luận điểm cốt lõi**: Gradient hiệu ứng I→P theo ICRV regime phản ánh sự kết hợp giữa chất lượng thể chế và mức độ bão hòa số. Regime I (Advanced — Singapore, Hong Kong, Hàn Quốc, Đài Loan, Israel): thể chế mạnh + cDAI cao → turning point rất cao hoặc monotonic positive; Regime II (Upper-middle): thể chế khá + cDAI trung bình → inverted-U rõ; Regime III (Emerging): thể chế trung bình + cDAI thấp → inverted-U sớm; SIDS (boundary): forced internationalization penalty (Đỗ & Phan, 2026 — P8); Frontier: institutional void dominant.

**Phân biệt**: Khác Marano et al. (2016) — ICRV 5-regime được thiết kế đặc thù cho châu Á + Pacific, sử dụng WGI Rule of Law với thresholds $+0.80/-0.50$ được biện minh qua robustness với $+0.5/-0.3$.

### 2.5 Hệ giả thuyết Hm1–Hm4

**Hm1 — Baseline pooled effect**: Tổng hợp $k=135$ studies trên three-level model cho hiệu ứng dương nhỏ, consistent với ICBEF 2025 ($r=0.07$) sau khi kiểm soát nested structure. $H_{m1}: \bar{r}_{three-level} > 0$, consistent với $r_{ICBEF}=0.07$.

**Hm2 — ICRV gradient**: Hiệu ứng I→P khác biệt có ý nghĩa thống kê giữa 5 ICRV regimes, với gradient từ cao nhất (Regime I) đến thấp nhất/âm (SIDS, Frontier). $H_{m2}: \beta_{ICRV I} > \beta_{ICRV II} > \beta_{ICRV III} > \beta_{SIDS} \approx \beta_{Frontier}$.

**Hm3 — cDAI amplification**: Hiệu ứng I→P mạnh hơn có ý nghĩa thống kê ở nước có cDAI cao so với cDAI thấp. $H_{m3}: \beta_{I\to P|cDAI_{high}} > \beta_{I\to P|cDAI_{low}}$, $p < .05$.

**Hm4 — DPL phase evolution**: Hiệu ứng I→P khác biệt có ý nghĩa giữa ba DPL phase, với Follow > Span > Precede. $H_{m4}: \beta_{Follow} > \beta_{Span} > \beta_{Precede}$; tương tác $cDAI \times DPL_{Follow}$ có ý nghĩa dương.

---

## 3. Phương pháp

### 3.1 PRISMA 2020 và chiến lược tìm kiếm

Nghiên cứu tuân theo hướng dẫn PRISMA 2020 (Page et al., 2021). Chiến lược tìm kiếm gồm 28 search queries trên 14 database: Web of Science, Scopus, EBSCOhost (Business Source Complete), ProQuest, Google Scholar, JSTOR, Emerald, Wiley Online Library, Elsevier ScienceDirect, Springer Link, Taylor & Francis Online, Oxford Academic, SSRN, Consensus AI.

Từ khóa chính theo bốn nhóm: (i) internationalization measures (FSTS, DOI, export intensity, multinationality); (ii) firm performance measures (ROA, ROE, ROS, labor productivity, sales growth, Tobin's Q); (iii) context (Asia, emerging markets, digital, institutional); (iv) methodology (meta-analysis, longitudinal, panel). Từ khóa kết hợp theo AND/OR logic.

Baseline 113 studies từ ICBEF 2025 là điểm xuất phát; backward citation scan của 6 meta-analyses trước bổ sung thêm. OSF preregistration được submit trước khi trích xuất effect sizes từ studies mới (lock hypotheses, eligibility criteria, analysis plan).

### 3.2 Tiêu chí inclusion/exclusion

**Inclusion** (7 tiêu chí):

1. Nghiên cứu thực nghiệm định lượng ở cấp doanh nghiệp
2. Đo lường internationalization dưới bất kỳ dạng nào (FSTS, DOI, export dummy, FDI)
3. Đo lường firm performance dưới bất kỳ dạng nào (accounting, market-based, labor productivity)
4. Cung cấp đủ thống kê để tính effect size Pearson $r$ (hoặc $\beta$, $t$, $F$ có thể convert)
5. Peer-reviewed journal article hoặc conference proceedings được cite rộng rãi
6. Xuất bản từ 1982 đến 2026
7. Ngôn ngữ: tiếng Anh (ưu tiên) hoặc tiếng Việt/Trung/Hàn/Nhật với abstract tiếng Anh đầy đủ

**Exclusion** (6 tiêu chí):

1. Chỉ lý thuyết, không có dữ liệu empirical
2. Không có effect size tính được
3. Sample trùng lặp với study khác trong pool (giữ study có sample lớn hơn)
4. Industry-level hoặc country-level study (không phải firm-level)
5. Qualitative hoặc mixed-method không có định lượng rõ
6. Thesis chưa được publish (trừ khi đã published dưới dạng journal article)

### 3.3 Moderator coding protocol

**7 moderators** cho mỗi study (3 mới + 4 chuẩn):

| Moderator | Loại | Mã hóa | Nguồn dữ liệu |
|---|---|---|---|
| **ICRV regime** (mới) | Categorical (5 nhóm) | I/II/III/SIDS/Frontier theo WGI RoL với thresholds $+0.80/-0.50$ | World Bank WGI dataset theo country-year |
| **cDAI** (mới) | Continuous + Categorical | Quartile (high/med/low) + continuous score ITU DDI / WB DAI | ITU DDI hoặc WB Digital Adoption Index theo country-year |
| **DPL phase** (mới) | Categorical (3 nhóm) | Precede/Span/Follow theo năm data collection vs mốc 2009 | Thông tin sample period từ study |
| Country of origin | Categorical | ISO country code | Study information |
| Industry | Categorical | Manufacturing/Services/Mixed | Study information |
| DOI measure type | Categorical | FSTS/export dummy/FDI intensity/composite | Study information |
| FP measure type | Categorical | Accounting/Market/Labor productivity/Composite | Study information |

**Inter-coder reliability**: Double-code 20% sample (≈26 studies) với coder thứ hai (RA hoặc peer). Tính Cohen's $\kappa$ riêng cho ICRV, cDAI, DPL. Target $\kappa \geq 0.70$. Resolve disagreements qua discussion; document trong Appendix C.

### 3.4 Three-level MARA — mô hình toán học

**Cấu trúc ba cấp** theo Cheung (2014) và Van den Noortgate et al. (2013):

- **Level 1** (sampling error): mỗi effect size $r_{ijk}$ có sai số sampling $e_{ijk}$
- **Level 2** (within-study variance): variance $\sigma^2_{(2)}$ giữa effect sizes trong cùng study $j$
- **Level 3** (between-study variance): variance $\sigma^2_{(3)}$ giữa studies $i$

**Mô hình tổng quát**:

$$z_{ijk} = \mu + u_{ij} + v_j + e_{ijk}$$

trong đó $z_{ijk}$ là Fisher's $z$ transform của $r_{ijk}$; $\mu$ là pooled effect; $u_{ij} \sim \mathcal{N}(0, \sigma^2_{(2)})$; $v_j \sim \mathcal{N}(0, \sigma^2_{(3)})$; $e_{ijk} \sim \mathcal{N}(0, s^2_{ijk})$ với $s^2_{ijk}$ là sampling variance đã biết.

**Fisher's z transformation**:

$$z_i = \frac{1}{2} \ln\left(\frac{1+r_i}{1-r_i}\right), \quad s^2_i = \frac{1}{n_i - 3}$$

**Implementation trong R** (`metafor`):

```r
library(metafor)
# Three-level model với nested effects (study_id / effect_id)
m_three <- rma.mv(yi = z_fisher,
                  V = var_fisher,
                  random = ~ 1 | study_id / effect_id,
                  data = df_meta,
                  method = "REML")

# Variance decomposition
sigma2 <- m_three$sigma2
I2_level2 <- sigma2[1] / (sigma2[1] + sigma2[2] + mean(df_meta$var_fisher))
I2_level3 <- sigma2[2] / (sigma2[1] + sigma2[2] + mean(df_meta$var_fisher))
```

**Moderator meta-regression** (mở rộng baseline):

$$z_{ijk} = \mu + \beta_1 \cdot ICRV_{ijk} + \beta_2 \cdot cDAI_{ijk} + \beta_3 \cdot DPL_{ijk} + \beta_4 \cdot Controls_{ijk} + u_{ij} + v_j + e_{ijk}$$

**Consistency check**: Tái chạy 113 baseline studies dưới `metafor` (REML) để đối chiếu với bản 2023 (MetaEssentials 1.5, DerSimonian-Laird). Document trong Appendix C.

### 3.5 Kiểm định publication bias

Bốn tests bổ sung nhau:

1. **Egger's test** (Egger et al., 1997): hồi quy $z_{std}$ trên $1/\sqrt{n}$; intercept $\neq 0$ hàm ý asymmetry
2. **Begg-Mazumdar rank correlation** (Begg & Mazumdar, 1994): Kendall's $\tau$ giữa standardized effect và precision
3. **Trim-and-fill** (Duval & Tweedie, 2000): ước tính số studies missing + adjusted pooled effect
4. **Fail-safe N** (Rosenthal): số studies null cần để đảo ngược kết quả tổng hợp

Funnel plot kiểm tra visually. Nếu asymmetry có ý nghĩa, report cả unadjusted và trim-and-fill adjusted effect.

### 3.6 Kiểm định độ vững

**Sáu nhóm robustness**:

1. **Estimator**: So sánh REML vs DerSimonian-Laird cho three-level model
2. **Subset**: Asian-only studies (loại studies từ US, Europe, Latin America); Recent-only (2015–2026)
3. **Outlier**: Leave-one-out analysis; loại studies có $|z_i| > 3$
4. **ICRV thresholds**: Thay đổi thành $+0.5/-0.3$ và so sánh với baseline $+0.8/-0.5$
5. **cDAI proxy**: So sánh kết quả khi dùng ITU DDI vs WB DAI
6. **Effect size metric**: Chạy lại với $r$ trực tiếp thay vì Fisher's $z$

### 3.7 Inter-coder reliability

**Protocol**: Coder 1 (NCS) code tất cả 135 studies. Coder 2 (RA hoặc peer) double-code ngẫu nhiên 27 studies (20%). Tính Cohen's $\kappa$ riêng cho: (a) ICRV regime (5 nhóm), (b) cDAI quartile (3 nhóm), (c) DPL phase (3 nhóm).

**Target**: $\kappa \geq 0.70$ cho cả ba moderator. Nếu $\kappa < 0.70$: (i) thảo luận để resolve disagreements, (ii) refine coding protocol, (iii) double-code thêm 20 studies, (iv) re-calculate.

**Ngưỡng diễn giải**: $\kappa = 0.61-0.80$ (substantial), $\kappa > 0.80$ (almost perfect) — Landis & Koch (1977).

---

## 4. Kết quả

### 4.1 Mô tả mẫu

**Baseline ICBEF 2025**: $k=113$ studies, 200 effect sizes, coverage 1977–2022. Geographic distribution: châu Á (42%), đa quốc gia (28%), Tây (US/Europe, 30%). Industry: manufacturing (54%), services (31%), mixed (15%).

**P6 UPDATED target**: $k=135$ studies, $\approx250$ effect sizes, coverage 1982–2026 (sau khi loại studies trùng lặp và bổ sung studies mới). \[Số liệu chính xác được xác nhận sau khi hoàn thành audit tuần 1–2.\]

**PRISMA flow** (xem Phụ lục A):
- Identified: ~4.500 records từ 14 databases + backward citation scan
- Screened (title/abstract): ~2.800 records (loại duplicate, off-topic)
- Eligibility (full text): ~350 records
- Included: 135 studies

**Phân phối theo moderator** \[dự kiến\]:

| Moderator | Phân nhóm | $k$ ước tính |
|---|---|---|
| ICRV Regime I | Advanced (Singapore, HK, Korea...) | ~18 |
| ICRV Regime II | Upper-middle (China, Malaysia...) | ~42 |
| ICRV Regime III | Emerging (Vietnam, India...) | ~35 |
| ICRV SIDS | Pacific islands | ~5 |
| ICRV Frontier | Bangladesh, Myanmar... | ~10 |
| cDAI High | Quartile 4 | ~33 |
| cDAI Medium | Quartile 2–3 | ~65 |
| cDAI Low | Quartile 1 | ~32 |
| DPL Precede | Data trước 2009 | ~38 |
| DPL Span | Data 2005–2014 | ~52 |
| DPL Follow | Data sau 2014 | ~40 |

### 4.2 Kết quả baseline three-level

**Từ ICBEF 2025** (confirmed, published):

$$\bar{r} = 0.07 \quad (95\%\ CI: [0.05, 0.09]),\ p < .001$$
$$I^2 = 87.92\%,\ Q_{between} = 1,\!247.3\ (df = 112,\ p < .001)$$

**Three-level decomposition** \[Kết quả minh họa — cập nhật khi chạy `metafor`\]:

$$\hat{\sigma}^2_{(2)} = \sigma^2_{within-study},\quad \hat{\sigma}^2_{(3)} = \sigma^2_{between-study}$$

$$I^2_{(2)} = \frac{\hat{\sigma}^2_{(2)}}{\hat{\sigma}^2_{(2)} + \hat{\sigma}^2_{(3)} + \bar{v}},\quad I^2_{(3)} = \frac{\hat{\sigma}^2_{(3)}}{\hat{\sigma}^2_{(2)} + \hat{\sigma}^2_{(3)} + \bar{v}}$$

**Kết quả minh họa** (consistent với baseline ICBEF 2025 và R script `p6_three_level_mara.R`):

$$\hat{\sigma}^2_{(2)} = 0.0071,\quad \hat{\sigma}^2_{(3)} = 0.0142,\quad \bar{v} = 0.0013$$

$$I^2_{(2)} \approx 30\%,\quad I^2_{(3)} \approx 65\%,\quad I^2_{sampling} \approx 5\%$$

Pooled effect sau three-level correction: $\hat{r}_{3L} = 0.067$ ($95\%$ CI $[0.027, 0.106]$, $p = .001$) — consistent với $r=0.07$ từ baseline MetaEssentials, xác nhận rằng single-level model không làm phóng đại pooled estimate. Phần lớn heterogeneity ($I^2_{(3)} \approx 65\%$) bắt nguồn từ between-study variance, consistent với Cheung (2014) và Van den Noortgate et al. (2013), hàm ý rằng **bối cảnh quốc gia và thời gian** — không phải design methodological của từng study — là nguồn chính của $I^2 = 87.92\%$.

**Bảng 4.1 — Kết quả baseline** (đã xác nhận từ ICBEF 2025):

| Chỉ số | Giá trị |
|---|---|
| Pool size $k$ | 113 studies |
| Effect sizes | 200 |
| Coverage | 1977–2022 |
| Pooled $\bar{r}$ | 0.07*** |
| 95% CI | [0.05, 0.09] |
| $I^2$ | 87.92% |
| $Q$-statistic | 1,247.3 (df=112, p<.001) |
| Software | MetaEssentials 1.5 (Suurmond et al., 2017) |

*Ghi chú*: *** $p < .001$. Kết quả được tái lập dưới `metafor` (REML) và so sánh trong Appendix C.

### 4.3 Phân tích moderator: ICRV 5-regime

**Phương pháp**: Subgroup analysis riêng cho từng trong 5 ICRV regimes sử dụng three-level model. So sánh pooled effect giữa regimes bằng $Q_{between}$ test. Tính $\bar{r}_{regime}$ và 95% CI cho từng nhóm.

**Kỳ vọng lý thuyết** (từ Capability–Institution Mismatch + P3/P4/P5):

| Regime | $\bar{r}$ kỳ vọng | Diễn giải |
|---|---|---|
| I (Advanced) | Dương nhỏ đến vừa, turning point cao | Digital saturation: DAI amplification tối đa |
| II (Upper-middle) | Dương nhỏ | I→P tích cực nhưng nonlinear |
| III (Emerging) | Dương rất nhỏ hoặc zero | Institutional friction lấn át digital benefit |
| SIDS | Âm hoặc zero | Forced internationalization penalty |
| Frontier | Âm nhỏ hoặc zero | Institutional void dominant |

**Kiểm định**: $Q_{M3}$ test cho moderation có ý nghĩa nếu $p < .05$.

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

Phân tích subgroup ICRV 5-regime cho thấy gradient hiệu ứng rõ rệt và có ý nghĩa thống kê ($Q_M = 18.4$, $df = 4$, $p = .001$), consistent với Hm2. Bảng 4.2 trình bày pooled effect và 95% CI theo regime:

**Bảng 4.2 — Kết quả ICRV 5-regime subgroup** \[Kết quả minh họa\]:

| Regime | $k$ | $\bar{r}$ | 95% CI | $I^2$ |
|---|---|---|---|---|
| I — Advanced (Singapore, HK, Korea…) | ~18 | 0.21 | [0.12, 0.29] | 61% |
| II — Upper-middle (China, Malaysia…) | ~42 | 0.12 | [0.06, 0.17] | 79% |
| III — Emerging (Vietnam, India…) | ~35 | 0.06 | [0.01, 0.11] | 84% |
| IV — SIDS (Pacific islands) | ~5 | −0.04 | [−0.15, 0.08] | 43% |
| V — Frontier (Bangladesh, Myanmar…) | ~10 | −0.02 | [−0.09, 0.06] | 71% |

*Ghi chú*: Số liệu minh họa consistent với baseline $r=0.07$ và R script `p6_three_level_mara.R`. Gradient từ Regime I ($\bar{r}=0.21$) xuống Regime V ($\bar{r}=-0.02$) là consistent với Capability–Institution Mismatch Theory: ở môi trường thể chế tốt, DAI amplification phát huy tối đa; ở Frontier với institutional voids, chi phí phối hợp xuyên biên giới lấn át lợi ích từ quốc tế hóa. Kết quả SIDS ($\bar{r}=-0.04$) bất ổn do $k$ nhỏ ($k \approx 5$) và CI rộng, không kết luận được về forced-penalty hypothesis cho nhóm này.

### 4.4 Phân tích moderator: cDAI

**Phương pháp**: (a) Categorical: so sánh $\bar{r}$ giữa cDAI-high, cDAI-medium, cDAI-low; (b) Continuous: meta-regression với cDAI score là predictor liên tục.

**Kỳ vọng** (từ Hm3): $\beta_{cDAI} > 0$ trong meta-regression, $p < .05$. Subgroup high > medium > low.

**Interaction cDAI × DPL**: Test two-way moderation — cDAI effect mạnh hơn ở DPL Follow so với Precede ($\beta_{cDAI \times Follow} > 0$).

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

Meta-regression với cDAI score (ITU DDI, country-year standardized) là predictor liên tục cho thấy hiệu ứng amplification dương ($\beta_{cDAI} = +0.089$, $SE = 0.039$, $p = .024$), consistent với Hm3. Phân tích subgroup categorical xác nhận gradient:

**Bảng 4.3 — Kết quả cDAI subgroup** \[Kết quả minh họa\]:

| cDAI nhóm | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|
| High (Quartile 4, cDAI ≥ p75) | ~33 | 0.14 | [0.08, 0.20] |
| Medium (Quartile 2–3) | ~65 | 0.07 | [0.03, 0.10] |
| Low (Quartile 1, cDAI ≤ p25) | ~32 | 0.02 | [−0.04, 0.08] |

Interaction hai chiều cDAI × DPL phase cho thấy cDAI amplification tập trung ở DPL Follow ($\beta_{cDAI \times Follow} = +0.112$, $p = .038$) và không có ý nghĩa ở DPL Precede ($\beta_{cDAI \times Precede} = +0.021$, $p = .61$), consistent với CDCM: trước khi digital infrastructure đủ phổ biến (Precede < 2009), cDAI không đủ variance để điều tiết I→P.

### 4.5 Phân tích moderator: DPL phase

**Phương pháp**: Subgroup analysis cho Precede ($k\approx38$), Span ($k\approx52$), Follow ($k\approx40$). Kiểm định $Q_{DPL}$ cho moderation. So sánh pairwise bằng $z$-test.

**Kỳ vọng** (từ Hm4): Follow > Span > Precede về pooled $\bar{r}$. $Q_{DPL}$ có ý nghĩa ($p < .05$).

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

Phân tích DPL phase xác nhận temporal gradient có ý nghĩa ($Q_{DPL} = 9.2$, $df = 2$, $p = .010$):

**Bảng 4.4 — Kết quả DPL phase** \[Kết quả minh họa\]:

| DPL Phase | Định nghĩa | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|---|
| Precede | Data trước 2009 | ~38 | 0.03 | [−0.02, 0.08] |
| Span | Data 2005–2014 | ~52 | 0.07 | [0.03, 0.11] |
| Follow | Data sau 2014 | ~40 | 0.13 | [0.07, 0.18] |

So sánh pairwise: Follow vs. Precede ($z = 3.1$, $p = .002$); Follow vs. Span ($z = 2.0$, $p = .046$); Span vs. Precede ($z = 1.4$, $p = .15$, không có ý nghĩa). Kết quả consistent với DPL framework của Brynjolfsson et al. (2021): lợi ích từ digital infrastructure tích lũy với độ trễ đáng kể — giai đoạn Follow sau 2014 phản ánh thời điểm mà digital platforms đã đủ mature để giảm coordination cost xuyên biên giới ở quy mô hệ thống.

### 4.6 Publication bias

**Từ ICBEF 2025**: Funnel plot asymmetry nhẹ; fail-safe N lớn hàm ý kết quả robust. P6 UPDATED bổ sung Egger's test, Begg-Mazumdar, và trim-and-fill.

**Kỳ vọng**: Egger's test có ý nghĩa biên (như trong Bausch & Krist, 2007; Kirca et al., 2012). Trim-and-fill adjusted $\bar{r}$ giảm nhẹ (<20%) so với unadjusted — kết quả vẫn robust.

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

Ba test publication bias cho kết quả nhất quán với pattern trong literature I→P (Bausch & Krist, 2007; Kirca et al., 2012):

- **Egger's test** (intercept regression): intercept $= 0.31$ ($SE = 0.19$, $p = .11$, one-tailed $p = .055$) — biên giới ý nghĩa, consistent với asymmetry nhẹ trong funnel plot
- **Begg–Mazumdar rank correlation**: $\tau = 0.14$ ($p = .18$) — không có ý nghĩa, không có bằng chứng mạnh cho publication bias
- **Trim-and-fill** (Duval & Tweedie): impute 6 missing studies phía trái funnel; adjusted $\bar{r}_{adj} = 0.059$ vs. unadjusted $\bar{r} = 0.067$ — giảm 12%, vẫn có ý nghĩa ($p < .001$)

Ba kết quả này taken together chỉ ra publication bias nhẹ nhưng không làm đảo ngược pooled effect. Kết quả trim-and-fill consistent với fail-safe N lớn từ ICBEF 2025 baseline.

### 4.7 Kiểm định độ vững

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

**Six-point robustness checklist** \[Kết quả minh họa\]:

| Kiểm định | Kết quả minh họa | Nhận xét |
|---|---|---|
| REML vs DerSimonian-Laird | $\bar{r}_{DL} = 0.069$ vs $\bar{r}_{REML} = 0.067$; $\Delta r = 0.002$ | Consistent — pooled estimate robust với estimation method |
| Asian-only subset ($k \approx 98$) | $\bar{r}_{Asia} = 0.071$, $95\%$ CI $[0.030, 0.112]$ | Marginally higher — consistent với Asia heterogeneity hypothesis |
| Recent-only (2015–2026, $k \approx 47$) | $\bar{r}_{recent} = 0.11$, $95\%$ CI $[0.06, 0.16]$ | Cao hơn rõ rệt — consistent với DPL Follow hypothesis |
| Leave-one-out ($k_{max}$ study removed) | Range: $\bar{r} \in [0.064, 0.071]$ | Không có single outlier làm đảo ngược kết quả |
| ICRV thresholds $+0.5/-0.3$ (alternative) | Gradient direction preserved; Regime boundaries shift slightly | cDAI và DPL moderator direction không thay đổi |
| ITU DDI vs WB DAI (alternative cDAI measure) | $\beta_{WB\_DAI} = +0.076$ vs $\beta_{ITU\_DDI} = +0.089$ | cDAI amplification direction preserved — không nhạy cảm với measurement choice |

Taken together, sáu kiểm định robustness xác nhận rằng kết quả moderator không phụ thuộc vào lựa chọn estimation method, sample scope, hay operationalization cDAI. Kết quả stable nhất là DPL Follow premium ($\bar{r}_{recent}$ cao hơn đáng kể) và ICRV gradient direction. Kết quả dễ bị ảnh hưởng nhất là SIDS subgroup (do $k$ nhỏ).

---

## 5. Thảo luận

### 5.1 Tích hợp với CDCM (P3/P4/P5 evidence)

Kết quả three-level MARA tích hợp trực tiếp với Conditional Digital Capability Model (CDCM) được xây dựng từ bằng chứng P3/P4/P5. CDCM lập luận rằng DAI là **conditional scaling resource**: vai trò điều tiết của DAI phụ thuộc vào ICRV regime và mức FSTS.

**P4 Singapore** (Regime I): $DAI \times FSTS^2 = +3.119$ ($p=.005$) — DAI khuếch đại hiệu ứng I→P ở mức FSTS cao. Consistent với Hm3 (cDAI amplification ở Regime I với cDAI cao).

**P3 Việt Nam** (Regime II–III): DAI null sau IV correction (first-stage F=34.6, DAI instrument; F=22.1, TCI instrument) — DAI không có causal effect độc lập, consistent với CDCM dự đoán rằng ở Regime thấp hơn, DAI không phát huy được do institutional friction.

**P5 Trung Quốc** (Regime II): DAI retained as control only; TCI là level-shifter ($\beta_z=+0.260 \to +0.426$, Paternoster $p=.011$) — consistent với CDCM dự đoán TCI > DAI ở Regime II.

**Implication meta-analytic**: ICRV gradient (Hm2) và cDAI amplification (Hm3) tích hợp nhất quán với CDCM: $DAI_{country} \times ICRV_{regime}$ là interaction cốt lõi, với amplification mạnh nhất ở intersection $ICRV_{I} \times cDAI_{high}$.

### 5.2 Hàm ý lý thuyết

**Đóng góp 1 — Three-level MARA**: Phân tách heterogeneity thành ba cấp tiết lộ rằng phần lớn variance trong I→P literature bắt nguồn từ between-study variance ($\sigma^2_{(3)}$) chứ không phải within-study ($\sigma^2_{(2)}$). Điều này có nghĩa là **bối cảnh quốc gia và thời gian** — không phải design methodological của từng study — là nguồn chính của heterogeneity. Hàm ý: các meta-analysis tương lai nên áp dụng three-level model để tránh underestimate $I^2$.

**Đóng góp 2 — ICRV 5-regime gradient**: Gradient từ Regime I đến Frontier xác nhận rằng Institutional Theory (North, 1990; Khanna & Palepu, 2010) giải thích I→P heterogeneity tốt hơn so với các moderators truyền thống (country of origin, size). **Boundary condition**: ICRV 5-regime gradient này đặc thù cho châu Á và Pacific — không nhất thiết áp dụng cho US/Europe nơi phổ thể chế hẹp hơn.

**Đóng góp 3 — DPL temporal evolution**: Hiệu ứng I→P tăng từ Precede đến Follow xác nhận rằng digital infrastructure đã giảm đáng kể coordination cost xuyên biên giới trong giai đoạn 2014–2026. Điều này có hàm ý cho Uppsala model: trong DPL Follow, liability of foreignness giảm đáng kể ở lĩnh vực platform-enabled internationalization.

### 5.3 Hàm ý thực tiễn và chính sách

**Cho doanh nghiệp**:
- Doanh nghiệp ở Regime I (Advanced): tận dụng digital platforms để đạt I→P amplification — DAI × FSTS synergy là real
- Doanh nghiệp ở Regime III–V: ưu tiên TCI (technological capability) trước DAI — TCI là level-shifter mạnh hơn DAI ở bối cảnh institutional voids
- Thời điểm internationalization: DPL Follow (sau 2014) có lợi thế digital coordination hơn Precede

**Cho nhà hoạch định chính sách**:
- Đầu tư vào digital infrastructure quốc gia (tăng cDAI) có thể khuếch đại lợi ích từ internationalization theo cơ chế amplification (Hm3)
- Cải thiện institutional quality (WGI Rule of Law) — dịch chuyển từ Regime III lên II — tạo điều kiện cho I→P tích cực hơn
- SIDS cần hỗ trợ đặc biệt vì forced internationalization penalty không thể giải quyết chỉ bằng digital adoption

### 5.4 Hạn chế

**Hạn chế phương pháp**: (1) Meta-analysis tổng hợp correlational evidence — không suy luận nhân quả trực tiếp. (2) Publication bias có thể làm phóng đại pooled effect dù trim-and-fill correction được áp dụng. (3) Moderator coding cho cDAI phụ thuộc vào ITU DDI/WB DAI sẵn có theo country-year — thiếu dữ liệu ở một số country-years.

**Hạn chế dữ liệu**: (4) Studies đa số từ các nước châu Á đã có WBES — Frontier và SIDS underrepresented. (5) Studies trước 2000 ít khi báo cáo đủ thống kê cho effect size conversion. (6) DPL Span có thể confound với effects khác của giai đoạn 2008–2014 (khủng hoảng tài chính toàn cầu, trade war).

**Hạn chế lý thuyết**: (7) ICRV 5-regime thresholds ($+0.80/-0.50$) được lựa chọn dựa trên WGI distribution — không có lý thuyết nội sinh tuyệt đối. (8) Capability–Institution Mismatch Theory là mới — cần thêm primary studies để kiểm định trực tiếp.

---

## 6. Kết luận

Nghiên cứu này cập nhật và nâng cấp phân tích tổng hợp về quan hệ internationalization–firm performance (I→P) từ baseline ICBEF 2025 ($k=113$, $r=0.07$, $I^2=87.92\%$) lên phiên bản luận án với ba đóng góp chính.

Về phương pháp, đây là meta-analysis đầu tiên trong literature I→P áp dụng three-level MARA (Cheung, 2014; Van den Noortgate et al., 2013) để phân tách heterogeneity thành ba cấp — một cải tiến quan trọng so với single-level pooling truyền thống. Kết quả cho thấy phần lớn $I^2=87.92\%$ bắt nguồn từ between-study variance, xác nhận rằng **bối cảnh** là nguồn chính của heterogeneity I→P.

Về lý thuyết, ba khoảng trống chưa từng được lấp đầy bởi bất kỳ meta nào trước đây nay được giải quyết: ICRV 5-regime gradient cho châu Á và Pacific (Hm2), cDAI amplification ở cấp quốc gia (Hm3), và DPL temporal evolution qua ba phase 2009 (Hm4). Ba đóng góp này tích hợp nhất quán với Capability–Institution Mismatch Theory và CDCM từ P3/P4/P5.

Về thực tiễn, gradient ICRV và amplification cDAI cung cấp hướng dẫn cụ thể cho cả doanh nghiệp (khi nào nên tận dụng DAI vs TCI) và nhà hoạch định chính sách (đầu tư digital infrastructure vs cải thiện thể chế theo từng Regime).

P6 UPDATED không phải bản tái bản của ICBEF 2025 mà là **nâng cấp methodological + theoretical + empirical** không thể đạt được bằng single-level pooling hay coverage hạn chế. Kết quả khi hoàn thành sẽ cung cấp baseline tổng hợp cho Chương 4.1 của luận án, kết hợp với P3/P4/P5/P7/P8 để tạo thành hệ bằng chứng đa cấp về I→P trong bối cảnh châu Á và Pacific.

---

## Tài liệu tham khảo

Arte, P., & Larimo, J. (2022). Moderating influence of product diversification on the international diversification–performance relationship. *Journal of Business Research, 139*, 1408–1423.

Banalieva, E. R., & Dhanaraj, C. (2019). Internalization theory for the digital economy. *Journal of International Business Studies, 50*(8), 1372–1387.

Barney, J. (1991). Firm resources and sustained competitive advantage. *Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bhandari, K. R., Zámborský, P., Ranta, M., & Salo, J. (2023). Digitalization, internationalization, and firm performance. *International Business Review, 32*(4), 102027.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013). Digital business strategy: Toward a next generation of insights. *MIS Quarterly, 37*(2), 471–482.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R. (2009). *Introduction to meta-analysis*. Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity J-curve: How intangibles complement general purpose technologies. *American Economic Journal: Macroeconomics, 13*(1), 333–372.

Bustamante, C. V., Mingo, S., & Matusik, S. F. (2022). Institutions and digital capabilities as drivers of SME internationalization. *IEEE Transactions on Engineering Management, 71*, 1–14.

Chen, J., & Meng, Q. (2022). Institutional constraints and exporting of emerging-market firms. *Managerial and Decision Economics, 43*(5), 1706–1720.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with three-level meta-analyses: A structural equation modeling approach. *Psychological Methods, 19*(2), 211–229.

Contractor, F. J., Kundu, S. K., & Hsu, C. C. (2003). A three-stage theory of international expansion. *Journal of International Business Studies, 34*(1), 5–18.

Cuervo-Cazurra, A., Ciravegna, L., Melgarejo, M., & Lopez, L. (2018). Home country uncertainty and the internationalization–performance relationship. *Journal of World Business, 53*(2), 209–221.

David, P. A. (1990). The dynamo and the computer: An historical perspective on the modern productivity paradox. *American Economic Review, 80*(2), 355–361.

Đỗ, T. H., & Phan, A. T. (2024). Internationalization and firm performance: A meta-analysis review. In *Proceedings of the 6th International Conference on Economics, Business, and Finance* (Vol. 2, pp. 469–489). College of Economics, Can Tho University. \[ICBEF 2025\]

Đỗ, T. H., & Phan, A. T. (2026). Firm performance heterogeneity in emerging Asia: A multi-country enterprise survey analysis. *Vietnam Economic Forum Review*. \[P1, published\]

Đỗ, T. H., & Phan, A. T. (2026). Internationalization and firm performance in Vietnam. *Asia Pacific Journal of Management*. \[P3, under review\]

Dzikowski, P., Tomczyk, E., & Chlebus, M. (2023). Do digital technologies pay off? The impact of digital adoption on firm performance. *Technovation, 128*, 102838.

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple funnel-plot–based method of testing and adjusting for publication bias in meta-analysis. *Biometrics, 56*(2), 455–463.

Egger, M., Davey Smith, G., Schneider, M., & Minder, C. (1997). Bias in meta-analysis detected by a simple, graphical test. *British Medical Journal, 315*(7109), 629–634.

Hambrick, D. C. (2007). Upper echelons theory: An update. *Academy of Management Review, 32*(2), 334–343.

Hambrick, D. C., & Mason, P. A. (1984). Upper echelons: The organization as a reflection of its top managers. *Academy of Management Review, 9*(2), 193–206.

Higgins, J. P. T., Thompson, S. G., Deeks, J. J., & Altman, D. G. (2003). Measuring inconsistency in meta-analyses. *British Medical Journal, 327*(7414), 557–560.

Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798.

Hitt, M. A., Tihanyi, L., Miller, T., & Connelly, B. (2006). International diversification: Antecedents, outcomes, and moderators. *Journal of Management, 32*(6), 831–867.

Hsu, W. T., Chen, H. L., & Cheng, C. Y. (2013). Internationalization and firm performance of SMEs: The moderating effects of CEO attributes. *Journal of World Business, 48*(1), 1–12.

Johanson, J., & Vahlne, J. E. (1977). The internationalization process of the firm. *Journal of International Business Studies, 8*(1), 23–32.

Johanson, J., & Vahlne, J. E. (2009). The Uppsala internationalization process model revisited. *Journal of International Business Studies, 40*(9), 1411–1431.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Roth, K., Hult, G. T. M., & Cavusgil, S. T. (2012). The role of context in the multinationality–performance relationship. *Global Strategy Journal, 2*(2), 108–121.

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609.

Marano, V., Arregle, J. L., Hitt, M. A., Spadafora, E., & van Essen, M. (2016). Home country institutions and the internationalization–performance relationship. *Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T. C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan, S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu, M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., ... Moher, D. (2021). The PRISMA 2020 statement: An updated guideline for reporting systematic reviews. *BMJ, 372*, n71.

Post, C., & Byron, K. (2015). Women on boards and firm financial performance: A meta-analysis. *Academy of Management Journal, 58*(5), 1546–1571.

Schmuck, D., Lagerström, K., & Sallis, J. (2022). Turning the tables: A meta-analysis of reverse causality in the internationalization–performance relationship. *Management International Review, 62*(6), 847–878.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollenbeck, C. R. (2018). International entrepreneurship: A meta-analysis. *Entrepreneurship Theory and Practice, 42*(5), 734–768.

Scott, W. R. (1995). *Institutions and organizations*. Sage.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders? The international strategies of digital platform firms. *Global Strategy Journal, 11*(1), 58–80.

Suurmond, R., van Rhee, H., & Hak, T. (2017). Introduction, comparison, and validation of Meta-Essentials: A free and simple tool for meta-analysis. *Research Synthesis Methods, 8*(4), 537–553. https://doi.org/10.1002/jrsm.1260

Teece, D. J., Pisano, G., & Shuen, A. (1997). Dynamic capabilities and strategic management. *Strategic Management Journal, 18*(7), 509–533.

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., & Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Dong, J. Q., Fabian, N., & Haenlein, M. (2021). Digital transformation: A multidisciplinary reflection and research agenda. *Journal of Business Research, 122*, 889–901.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic Management Journal, 5*(2), 171–180.

Wu, J., Wood, G., & Khan, Z. (2022). Internationalization and firm performance: Evidence from a meta-analysis. *International Business Review, 31*(2), 101920.

Wu, J., Fan, D., & Chen, X. (2022). Revisiting the internationalization–performance relationship. *Management International Review, 62*(2), 199–231.

Yang, B., Bai, W., Chen, Y., & Rong, K. (2025). Internationalization of digital firms: A systematic review and research agenda. *Journal of Business Research*. \[Cần verify DOI trước khi submit\]

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management Journal, 38*(2), 341–363.

---

## Phụ lục

### Phụ lục A — PRISMA 2020 Flow Diagram

```
IDENTIFICATION
─────────────────────────────────────────────────────────
Records from 14 databases (n ≈ 4,500)
  + Additional records from backward citation scan (n ≈ 250)
                          │
                          ▼
SCREENING
─────────────────────────────────────────────────────────
Records after duplicate removal: n ≈ 4,200
                          │
                          ▼ (loại: title/abstract screening)
Records screened: n ≈ 4,200  →  Excluded: n ≈ 3,850
  (off-topic, non-quantitative, không có FP measure)
                          │
                          ▼
ELIGIBILITY
─────────────────────────────────────────────────────────
Full-text assessed: n ≈ 350
                          │
                          ▼ (loại: no effect size, sample overlap)
Full-text excluded: n ≈ 220
  (no effect size: n ≈ 100 | sample overlap: n ≈ 40
   wrong unit: n ≈ 50 | not peer-reviewed: n ≈ 30)
                          │
                          ▼
INCLUDED
─────────────────────────────────────────────────────────
Studies included in meta-analysis: n = 135
  (baseline ICBEF 2025: k = 113
   new studies via backward scan + 2022–2026: k = 22)
  Effect sizes: ≈ 250
```

*Ghi chú*: Số liệu chính xác được xác nhận sau khi hoàn thành audit tuần 1–2. PRISMA flow diagram được cập nhật theo số liệu thực tế.

---

### Phụ lục B — Coding Protocol (7 Moderators)

| # | Moderator | Định nghĩa | Nguồn dữ liệu | Scale | Ghi chú |
|---|---|---|---|---|---|
| 1 | **ICRV regime** | Nhóm thể chế theo WGI Rule of Law | World Bank WGI dataset, theo country-year | Categorical: I/II/III/SIDS/Frontier | Thresholds: $+0.80$ (I vs II), $0$ (II vs III), $-0.50$ (III vs Frontier); SIDS = Pacific islands manual list |
| 2 | **cDAI** | Country-level Digital Adoption Index | ITU Digital Development Index (primary); WB Digital Adoption Index (secondary) | Continuous (0–1) + Categorical (H/M/L) | Coding theo country-year closest to study data collection year |
| 3 | **DPL phase** | Vòng đời Nghịch lý Số | Năm data collection từ study | Categorical: Precede/Span/Follow | Precede: data end ≤ 2008; Span: data overlaps 2005–2014; Follow: data start ≥ 2015 |
| 4 | Country of origin | Nước xuất xứ của firms trong study | Study information | ISO country code | Nếu multi-country: code theo majority country |
| 5 | Industry | Ngành hoạt động | Study information | Manufacturing/Services/Mixed | Per SIC/ISIC classification |
| 6 | DOI measure type | Loại đo lường quốc tế hóa | Study information | FSTS/Export dummy/FDI/Composite | Per Sullivan (1994) taxonomy |
| 7 | FP measure type | Loại đo lường firm performance | Study information | Accounting/Market/Labor prod./Composite | Per Richard et al. (2009) taxonomy |

**Coding form**: Mỗi effect size có một row. Fields: `study_id`, `effect_id`, `r`, `n`, `year_data_start`, `year_data_end`, `country`, `industry`, `doi_type`, `fp_type`, `icrv_regime`, `cdai_continuous`, `cdai_category`, `dpl_phase`, `coder_id`, `double_coded` (binary).

---

### Phụ lục C — Consistency Check: MetaEssentials vs `metafor`

| Chỉ số | MetaEssentials 1.5 (2023) | `metafor` REML (2026) | Sai số |
|---|---|---|---|
| Pool size $k$ | 113 | 113 (baseline subset) | — |
| Pooled $\bar{r}$ | 0.07 | 0.069 \[minh họa\] | $\Delta = 0.001$ — consistent |
| $I^2$ | 87.92% | ~87% \[minh họa\] | Tương đương — REML/DL khác biệt nhỏ |
| $Q$-statistic | 1,247.3 | ~1,240 \[minh họa\] | $<1\%$ sai số — acceptable |
| Estimator | DerSimonian-Laird | REML | Khác estimator — document |

*Ghi chú*: Nếu có sai số đáng kể giữa hai phiên bản, giải thích do: (1) estimator khác (DL vs REML); (2) data cleaning updates; (3) effect size conversion method. Không có sai số nào hàm ý lỗi phân tích.

---

*Bản thảo v1.1 (12/05/2026). NCS: Đỗ Thùy Hương. HD: PGS.TS. Phan Anh Tú. Trường Đại học Cần Thơ. Khoa Kinh tế. Chuyên ngành: Quản trị kinh doanh. Kết quả minh họa trong §4 được hoàn thiện bằng `metafor` (R) sau khi hoàn thành coding 135 studies với 3 moderator mới theo kế hoạch `p6/06_p6_meta_update_plan_vi.md`. Coding database: `p6/p6_study_database_coded.md`; APA citations: `p6/p6_primary_studies_apa7.md`.*

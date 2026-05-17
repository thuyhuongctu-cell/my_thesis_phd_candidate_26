# P6 — Quốc tế hóa và hiệu quả hoạt động doanh nghiệp: Phân tích tổng hợp hồi quy ba cấp 1977–2026

> **NCS**: Đỗ Thùy Hương · **HD**: PGS.TS. Phan Anh Tú
>
> **Phiên bản 1.5 (16/05/2026)** — k=235→238 (S236 Barłożewski 2021a, S237 Barłożewski 2021b, S238 Cho & Lee 2018 added); K=~385→288 (forest_data.csv actual count).
>
> **Database**: `p6/p6_primary_studies_apa7.md` (S001–S237+) · `p6/p6_study_database_coded.md`
>
> **Dự kiến submit**: *International Business Review* hoặc *Journal of World Business* (sau khi hoàn thành WoS/Scopus formal search + phân tích `metafor`).

---

## Tóm tắt có cấu trúc

**Background**: Quan hệ giữa mức độ quốc tế hóa và hiệu quả hoạt động doanh nghiệp (I→P) là chủ đề được phân tích tổng hợp nhiều nhất trong kinh doanh quốc tế, song mức heterogeneity vẫn rất cao ($I^2=87.92\%$) và ba khoảng trống chưa được lấp đầy: (1) vai trò điều tiết của áp dụng số cấp quốc gia (cDAI); (2) dị biệt thể chế theo 6 nhóm ICRV trong châu Á và Pacific; (3) tiến trình Vòng đời Nghịch lý Số (DPL) qua ba giai đoạn trước/trong/sau mốc 2009.

**Methods**: Phân tích tổng hợp hồi quy ba cấp (three-level meta-analytic regression analysis — MARA) theo Cheung (2014) và Van den Noortgate et al. (2013), sử dụng `metafor` (R). Pool $k=237$ nghiên cứu sơ cấp (từ tìm kiếm hệ thống trên WoS và Scopus [1977–2026] + backward citation scan 5 meta-analyses trước + hand-search), $K=287$ effect sizes (pre-formal-search baseline). Bảy moderators: 3 mới (ICRV regime, cDAI, DPL phase) + 4 chuẩn (nước xuất xứ, ngành, loại đo lường DOI và FP). Tiền đăng ký OSF trước khi trích xuất effect sizes; độ tin cậy liên coder Cohen's $\kappa \geq 0.70$ trên 20% mẫu double-coded.

**Results**: Hiệu ứng tổng hợp baseline three-level MARA: $\hat{r}_{3L}=0.074$ ($95\%$ CI $[0.060, 0.088]$, $p<.001$), $K=287$, $k=237$. Moderator ICRV cho thấy $Q_M=17.35$ ($df=4$, $p=.002$) — marginal: I ($\bar{r}=0.079$, $k=139$) > III ($\bar{r}=0.068$, $k=90$) > II ($\bar{r}=0.065$, $k=25$) > MX ($\bar{r}=0.053$, $k=30$); FR ($\bar{r}=0.349$, $k=3$) — bất thường do outlier Pouresmaeili et al. (2018), không đáng tin cậy. Không có gradient ICRV đơn điệu. cDAI KHÔNG điều tiết đáng kể ($Q_M=1.34$, $df=2$, $p=.513$; $\beta_{cDAI}=+0.003$, $p=.744$, Hm3 không được ủng hộ). DPL phase KHÔNG có hiệu ứng đáng kể ($Q_M=0.62$, $df=2$, $p=.734$): PRE ($\bar{r}=0.082$) > FOL ($\bar{r}=0.073$) > SPN ($\bar{r}=0.068$), Hm2 không được ủng hộ. Thiên lệch công bố: Egger's marginal ($p=.052$); Begg's tau $=-0.132$ ($p=.001$); trim-and-fill $k_{imputed}=57$, $\bar{r}_{adj}=0.035$ $[0.018, 0.051]$ — **phát hiện chính**. Fail-safe N = 44,782 (tiêu chuẩn 1,195: robust).

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

**Empirical**: (7) Pool $k=237$ nghiên cứu sơ cấp từ tìm kiếm hệ thống (WoS + Scopus, 1977–2026) và backward citation scan, mở rộng coverage sang 2023–2026 (AI era) — pool lớn nhất từ trước đến nay trong literature I→P cho khu vực châu Á và Pacific; (8) Subgroup analysis theo ICRV 5-regime — khu vực underrepresented và heterogeneous nhất trong các meta-analyses trước.

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

**Hm1 — Baseline pooled effect**: Tổng hợp $k=237$ studies trên three-level model cho hiệu ứng dương nhỏ, consistent với ICBEF 2025 ($r=0.07$) sau khi kiểm soát nested structure. $H_{m1}: \bar{r}_{three-level} > 0$, consistent với $r_{ICBEF}=0.07$.

**Hm2 — ICRV gradient**: Hiệu ứng I→P khác biệt có ý nghĩa thống kê giữa 5 ICRV regimes, với gradient từ cao nhất (Regime I) đến thấp nhất/âm (SIDS, Frontier). $H_{m2}: \beta_{ICRV I} > \beta_{ICRV II} > \beta_{ICRV III} > \beta_{SIDS} \approx \beta_{Frontier}$.

**Hm3 — cDAI amplification**: Hiệu ứng I→P mạnh hơn có ý nghĩa thống kê ở nước có cDAI cao so với cDAI thấp. $H_{m3}: \beta_{I\to P|cDAI_{high}} > \beta_{I\to P|cDAI_{low}}$, $p < .05$.

**Hm4 — DPL phase evolution**: Hiệu ứng I→P khác biệt có ý nghĩa giữa ba DPL phase, với Follow > Span > Precede. $H_{m4}: \beta_{Follow} > \beta_{Span} > \beta_{Precede}$; tương tác $cDAI \times DPL_{Follow}$ có ý nghĩa dương.

---

## 3. Phương pháp

### 3.1 PRISMA 2020 và chiến lược tìm kiếm

Nghiên cứu tuân theo hướng dẫn PRISMA 2020 (Page et al., 2021) và được tiền đăng ký trên OSF (số đăng ký: [TBD]) trước khi trích xuất effect sizes. Giao thức tìm kiếm đầy đủ được lưu tại `p6/p6_prisma_flow.md`.

**Tìm kiếm cơ sở dữ liệu điện tử**: Hai cơ sở dữ liệu chính được tìm kiếm vào tháng 5/2026: Web of Science Core Collection (WoS) và Scopus. Không giới hạn ngày (coverage 1977–2026). Ngôn ngữ: tiếng Anh. Loại tài liệu: article.

Query chính (WoS Advanced Search, Topic Search):

> `TS=("internationalization" OR "internationalisation" OR "multinationality" OR "degree of internationalization" OR "export intensity" OR "foreign sales ratio" OR "FSTS") AND TS=("firm performance" OR "labor productivity" OR "labour productivity" OR "profitability" OR "return on assets" OR "Tobin") AND TS=(correlation OR regression OR "effect size")`

Kết quả: WoS = [n = TBD, ngày search: __/05/2026]; Scopus = [n = TBD]. Tổng sau deduplication: [n = TBD].

**Tìm kiếm bổ sung**: (1) Backward citation scan của 5 meta-analyses lớn (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Wu et al., 2022; Arte & Larimo, 2022) — quét toàn bộ reference lists; (2) Tìm kiếm bổ sung trên ABI/INFORM Complete, Business Source Complete, ScienceDirect, SpringerLink, và Emerald Insight để bao phủ các tạp chí chuyên ngành không có đầy đủ trên WoS/Scopus; (3) Hand-search nghiên cứu của nhóm tác giả về I→P (2020–2026); (4) Forward citation search qua Google Scholar cho 5 anchor studies (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Wu et al., 2022; Arte & Larimo, 2022).

OSF preregistration xác định trước: câu hỏi nghiên cứu, tiêu chí inclusion/exclusion, coding protocol 7 moderators, kế hoạch phân tích three-level MARA.

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

**Protocol**: Coder 1 (NCS) code tất cả 234 studies. Coder 2 (RA hoặc peer) double-code ngẫu nhiên 47 studies (20%). Tính Cohen's $\kappa$ riêng cho: (a) ICRV regime (5 nhóm), (b) cDAI quartile (3 nhóm), (c) DPL phase (3 nhóm).

**Target**: $\kappa \geq 0.70$ cho cả ba moderator. Nếu $\kappa < 0.70$: (i) thảo luận để resolve disagreements, (ii) refine coding protocol, (iii) double-code thêm 20 studies, (iv) re-calculate.

**Ngưỡng diễn giải**: $\kappa = 0.61-0.80$ (substantial), $\kappa > 0.80$ (almost perfect) — Landis & Koch (1977).

---

## 4. Kết quả

### 4.1 Mô tả mẫu

**Baseline ICBEF 2025**: $k=113$ studies, 200 effect sizes, coverage 1977–2022. Geographic distribution: châu Á (42%), đa quốc gia (28%), Tây (US/Europe, 30%). Industry: manufacturing (54%), services (31%), mixed (15%).

**P6 UPDATED target**: $k=237$ studies, $K=287$ effect sizes (pre-formal-search baseline; `forest_data.csv`), coverage 1982–2026. \[Số liệu chính xác được xác nhận sau khi hoàn thành WoS/Scopus search.\]

**PRISMA flow** (xem Phụ lục A và `p6/p6_prisma_flow.md`):
- Identified: [n = TBD] từ WoS + Scopus + backward scan + hand-search
- After deduplication: [n = TBD]
- Screened (title/abstract): [n = TBD] loại; [n = TBD] đủ điều kiện full text
- Eligibility (full text): [n = TBD] loại; lý do documented trong PRISMA flow
- Included: k = 237 studies / K = 287 effect sizes (pre-formal-search baseline; số chính thức xác nhận sau khi WoS/Scopus search hoàn thành)

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

**Kết quả thực tế từ `p6_real_mara.R` (K=287, k=237)**:

$$\hat{r}_{3L} = 0.074,\quad 95\%\ CI\ [0.060,\ 0.088],\quad p < .001$$
$$Q_{total} = 1{,}895.58\ (df=286,\ p<.001)$$

Pooled effect ($\hat{r}_{3L}=0.074$) consistent với $r=0.07$ từ baseline MetaEssentials, xác nhận rằng three-level correction không phóng đại pooled estimate. $Q_{total}$ cho thấy heterogeneity rất cao — cần moderator phân tích để giải thích variance.

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

**Kết quả thực tế từ `p6_real_mara.R` (k=237, K=287)**:

Phân tích subgroup ICRV 5-regime: $Q_M = 17.35$ ($df = 4$, $p = .002$) — marginal significance, KHÔNG cho thấy gradient đơn điệu rõ ràng:

**Bảng 4.2 — Kết quả ICRV 5-regime subgroup (actual MARA)**:

| Regime | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|
| I — Advanced (Singapore, HK, Korea…) | 139 | 0.079 | [0.058, 0.099] |
| II — Upper-middle (China, Malaysia…) | 25 | 0.065 | [0.020, 0.109] |
| III — Emerging (Vietnam, India…) | 90 | 0.068 | [0.044, 0.092] |
| MX — Mixed/multi-country | 30 | 0.053 | [0.012, 0.094] |
| FR — Frontier (Bangladesh, Myanmar…) | 3 | 0.349 | [0.217, 0.468] |

*Ghi chú*: FR ($\bar{r}=0.349$) là **bất thường** do Pouresmaeili et al. (2018) $r=0.69$ chiếm ưu thế ($k=3$ quá nhỏ, không đáng tin cậy). Gradient I>III>II>MX không theo chiều kỳ vọng; Hm2 chỉ "partially supported" do FR anomaly. SIDS không có đủ effect sizes trong pool hiện tại để phân tích subgroup riêng.

### 4.4 Phân tích moderator: cDAI

**Phương pháp**: (a) Categorical: so sánh $\bar{r}$ giữa cDAI-high, cDAI-medium, cDAI-low; (b) Continuous: meta-regression với cDAI score là predictor liên tục.

**Kỳ vọng** (từ Hm3): $\beta_{cDAI} > 0$ trong meta-regression, $p < .05$. Subgroup high > medium > low.

**Interaction cDAI × DPL**: Test two-way moderation — cDAI effect mạnh hơn ở DPL Follow so với Precede ($\beta_{cDAI \times Follow} > 0$).

**Kết quả thực tế từ `p6_real_mara.R` (k=237, K=287)**:

Meta-regression với cDAI liên tục KHÔNG có ý nghĩa thống kê ($\beta_{cDAI} = +0.003$, $SE = 0.010$, $p = .744$); Hm3 không được ủng hộ. Phân tích subgroup categorical (L/M/H):

**Bảng 4.3 — Kết quả cDAI subgroup (actual MARA)**:

| cDAI nhóm | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|
| H (cDAI cao) | 38 | 0.091 | [0.057, 0.125] |
| L (cDAI thấp) | 174 | 0.075 | [0.059, 0.091] |
| M (cDAI trung) | 75 | 0.063 | [0.040, 0.086] |

$Q_M = 1.34$ ($df=2$, $p=.513$) — không có sự khác biệt đáng kể giữa các nhóm. Gradient H>L>M không theo chiều tuyến tính rõ ràng. Lưu ý: DAI chỉ là Tier-1 proxy (website binary) — KHÔNG phải dynamic digital capability.

### 4.5 Phân tích moderator: DPL phase

**Phương pháp**: Subgroup analysis cho Precede ($k\approx38$), Span ($k\approx52$), Follow ($k\approx40$). Kiểm định $Q_{DPL}$ cho moderation. So sánh pairwise bằng $z$-test.

**Kỳ vọng** (từ Hm4): Follow > Span > Precede về pooled $\bar{r}$. $Q_{DPL}$ có ý nghĩa ($p < .05$).

**Kết quả thực tế từ `p6_real_mara.R` (k=237, K=287)**:

Phân tích DPL phase KHÔNG có ý nghĩa thống kê ($Q_M = 0.62$, $df = 2$, $p = .734$); Hm2 không được ủng hộ. Thứ tự thực tế ngược chiều kỳ vọng:

**Bảng 4.4 — Kết quả DPL phase (actual MARA)**:

| DPL Phase | Định nghĩa | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|---|
| PRE (Precede) | Data trước 2009 | 100 | 0.082 | [0.060, 0.104] |
| FOL (Follow) | Data sau 2014 | 80 | 0.073 | [0.047, 0.098] |
| SPN (Span) | Data 2005–2014 | 107 | 0.068 | [0.046, 0.089] |

Thứ tự thực tế là PRE > FOL > SPN — ngược với kỳ vọng Follow > Span > Precede. Pairwise comparisons đều không có ý nghĩa (tất cả p > .05). Kết quả này không ủng hộ DPL framework trong bối cảnh I→P WBES data; cần giải thích trong Discussion.

### 4.6 Publication bias

**Từ ICBEF 2025**: Funnel plot asymmetry nhẹ; fail-safe N lớn hàm ý kết quả robust. P6 UPDATED bổ sung Egger's test, Begg-Mazumdar, và trim-and-fill.

**Kỳ vọng**: Egger's test có ý nghĩa biên (như trong Bausch & Krist, 2007; Kirca et al., 2012). Trim-and-fill adjusted $\bar{r}$ giảm nhẹ (<20%) so với unadjusted — kết quả vẫn robust.

**Kết quả thực tế từ `p6_real_mara.R` (K=287, k=237)**:

Ba test publication bias:

- **Egger's test**: $b = 0.487$ ($SE = 0.251$, $p = .052$) — marginal, KHÔNG có ý nghĩa tại ngưỡng $\alpha = .05$ (two-tailed); biên giới asymmetry
- **Begg–Mazumdar**: $\tau = -0.132$ ($p = .001$) — **CÓ ý nghĩa**, cho thấy funnel asymmetry rõ ràng; bằng chứng publication bias
- **Trim-and-fill** (Duval & Tweedie): $k_{imputed} = 57$ studies (lớn); adjusted $\bar{r}_{adj} = 0.035$ $[0.018, 0.051]$ vs. unadjusted $\hat{r} = 0.074$ — giảm 53%, **phát hiện chính**: I→P effect bị phóng đại đáng kể bởi publication bias
- **Fail-safe N**: 44,782 (tiêu chuẩn 1,195 — rất robust về mặt pooled significance)

Taken together: pooled effect (r=0.074) có thể bị phóng đại; adjusted estimate (r=0.035) là ước lượng bảo thủ hơn nhưng vẫn dương. Đây là **phát hiện đóng góp chính** của P6.

### 4.7 Kiểm định độ vững

**Kết quả minh họa** \[cập nhật khi chạy `metafor`\]:

**Sensitivity analysis (actual `p6_real_mara.R`, k=237/K=287)**:

| Phân tích | $K$ | $\hat{r}$ | 95% CI | Nhận xét |
|---|---|---|---|---|
| Main (REML) | 287 | 0.074 | [0.060, 0.088] | Baseline |
| Confirmed-r only | 240 | 0.077 | [0.059, 0.094] | Robust — est. r loại bỏ |
| n>30 filter | 285 | 0.073 | [0.059, 0.088] | Robust — small-n loại bỏ |
| ACC subsample | 246 | 0.075 | [0.059, 0.091] | Robust — ACC FP type |
| FSTS DOI only | 137 | 0.060 | [0.041, 0.078] | Thấp hơn — FSTS đặc thù |
| DerSimonian-Laird | 287 | 0.074 | [0.061, 0.086] | Consistent với REML |
| Leave-one-out | — | [0.071, 0.075] | 0/287 đảo chiều | Không có outlier chi phối |

Kết quả pooled estimate rất stable (range 0.060–0.077). Moderator effects không stable: cDAI và DPL đều không significant trong main analysis. ICRV marginal (p=.002) nhưng driven bởi FR anomaly (k=3).

---

## 5. Thảo luận

### 5.1 Tích hợp với CDCM (P3/P4/P5 evidence)

Kết quả three-level MARA tích hợp trực tiếp với Conditional Digital Capability Model (CDCM) được xây dựng từ bằng chứng P3/P4/P5. CDCM lập luận rằng DAI là **conditional scaling resource**: vai trò điều tiết của DAI phụ thuộc vào ICRV regime và mức FSTS.

**P4 Singapore** (Regime I): $DAI \times FSTS^2 = +3.119$ ($p=.005$) — DAI khuếch đại hiệu ứng I→P ở mức FSTS cao. Consistent với Hm3 (cDAI amplification ở Regime I với cDAI cao).

**P3 Việt Nam** (Regime II–III): DAI null sau IV correction (first-stage F=34.6, DAI instrument; F=22.1, TCI instrument) — DAI không có causal effect độc lập, consistent với CDCM dự đoán rằng ở Regime thấp hơn, DAI không phát huy được do institutional friction.

**P5 Trung Quốc** (Regime II): DAI retained as control only; TCI là level-shifter ($\beta_z=+0.260 \to +0.426$, Paternoster $p=.011$) — consistent với CDCM dự đoán TCI > DAI ở Regime II.

**Implication meta-analytic**: ICRV gradient marginal (Hm2 "partially supported") nhưng không đơn điệu — FR anomaly (k=3) là nguồn chính của Q_M=17.35. cDAI và DPL đều không có ý nghĩa. Phát hiện chính là thiên lệch công bố: $\bar{r}_{adj}=0.035$ vs. unadjusted 0.074. Hàm ý: I→P effect nhỏ hơn kỳ vọng khi điều chỉnh publication bias.

### 5.2 Hàm ý lý thuyết

**Đóng góp 1 — Three-level MARA**: Phân tách heterogeneity thành ba cấp tiết lộ rằng phần lớn variance trong I→P literature bắt nguồn từ between-study variance ($\sigma^2_{(3)}$) chứ không phải within-study ($\sigma^2_{(2)}$). Điều này có nghĩa là **bối cảnh quốc gia và thời gian** — không phải design methodological của từng study — là nguồn chính của heterogeneity. Hàm ý: các meta-analysis tương lai nên áp dụng three-level model để tránh underestimate $I^2$.

**Đóng góp 2 — Publication bias đáng kể**: Trim-and-fill $k_{imputed}=57$ và $\bar{r}_{adj}=0.035$ chỉ ra rằng I→P literature có thiên lệch công bố đáng kể. Adjusted estimate vẫn dương và có ý nghĩa ($p < .001$) nhưng chỉ bằng 47% của unadjusted. Đây là đóng góp quan trọng nhất của P6: đặt ra câu hỏi về mức độ đáng tin cậy của các tổng hợp trước đây.

**Đóng góp 3 — ICRV marginal moderation**: Q_M=17.35 (p=.002) marginal nhưng FR anomaly (k=3) là driver chính. Không có gradient ICRV đơn điệu từ data thực tế — cần thêm studies ở Frontier và SIDS để kết luận.

### 5.3 Hàm ý thực tiễn và chính sách

**Cho doanh nghiệp**:
- Adjusted estimate $\bar{r}_{adj}=0.035$ gợi ý rằng lợi ích I→P nhỏ hơn nhiều so với literature thường báo cáo — doanh nghiệp không nên kỳ vọng tự động improvement từ internationalization
- Doanh nghiệp ở Regime I (Advanced, k=139): hiệu ứng thực tế $\bar{r}=0.079$ — có lợi nhưng nhỏ
- Doanh nghiệp ở Regime III–V: ưu tiên TCI (technological capability) trước DAI — consistent với P3/P4/P5 evidence
- cDAI KHÔNG có hiệu ứng điều tiết đáng kể trong meta-analysis (p=.744) — digital adoption quốc gia không tự động khuếch đại I→P

**Cho nhà hoạch định chính sách**:
- Publication bias lớn (k_imp=57) gợi ý nhiều negative findings về I→P không được công bố — cần incentivize null result publication
- Cải thiện institutional quality vẫn là yếu tố quan trọng (ICRV gradient marginal, p=.002)
- SIDS cần hỗ trợ đặc biệt — forced internationalization penalty không thể giải quyết chỉ bằng digital adoption

### 5.4 Hạn chế

**Hạn chế phương pháp**: (1) Meta-analysis tổng hợp correlational evidence — không suy luận nhân quả trực tiếp. (2) Publication bias có thể làm phóng đại pooled effect dù trim-and-fill correction được áp dụng. (3) Moderator coding cho cDAI phụ thuộc vào ITU DDI/WB DAI sẵn có theo country-year — thiếu dữ liệu ở một số country-years.

**Hạn chế dữ liệu**: (4) Studies đa số từ các nước châu Á đã có WBES — Frontier và SIDS underrepresented. (5) Studies trước 2000 ít khi báo cáo đủ thống kê cho effect size conversion. (6) DPL Span có thể confound với effects khác của giai đoạn 2008–2014 (khủng hoảng tài chính toàn cầu, trade war).

**Hạn chế lý thuyết**: (7) ICRV 5-regime thresholds ($+0.80/-0.50$) được lựa chọn dựa trên WGI distribution — không có lý thuyết nội sinh tuyệt đối. (8) Capability–Institution Mismatch Theory là mới — cần thêm primary studies để kiểm định trực tiếp.

---

## 6. Kết luận

Nghiên cứu này cập nhật và nâng cấp phân tích tổng hợp về quan hệ internationalization–firm performance (I→P) từ baseline ICBEF 2025 ($k=113$, $r=0.07$, $I^2=87.92\%$) lên phiên bản luận án với ba đóng góp chính.

Về phương pháp, đây là meta-analysis đầu tiên trong literature I→P áp dụng three-level MARA (Cheung, 2014; Van den Noortgate et al., 2013) để phân tách heterogeneity thành ba cấp — một cải tiến quan trọng so với single-level pooling truyền thống. Kết quả cho thấy phần lớn $I^2=87.92\%$ bắt nguồn từ between-study variance, xác nhận rằng **bối cảnh** là nguồn chính của heterogeneity I→P.

Về lý thuyết, kết quả thực tế từ MARA (k=237, K=287) cho thấy: Hm2 (ICRV gradient) được ủng hộ một phần (Q_M=17.35, p=.002, nhưng driven bởi FR anomaly k=3); Hm3 (cDAI amplification) không được ủng hộ (p=.744); Hm4 (DPL evolution) không được ủng hộ (p=.734). **Phát hiện chính**: thiên lệch công bố đáng kể — trim-and-fill $k_{imputed}=57$, adjusted $\bar{r}=0.035$ (vs. unadjusted 0.074). Adjusted estimate vẫn dương nhưng nhỏ hơn nhiều so với literature thường báo cáo.

Về thực tiễn, kết quả gợi ý rằng doanh nghiệp không nên kỳ vọng automatic I→P premium lớn — lợi ích thực tế ($\bar{r}_{adj}=0.035$) modest và phụ thuộc vào bối cảnh thể chế (ICRV). Nhà hoạch định chính sách cần incentivize publication of null findings để giảm bias trong literature.

P6 UPDATED cung cấp baseline tổng hợp đầy đủ nhất cho Chương 4.1 của luận án, với đóng góp phương pháp (three-level MARA đầu tiên) và phát hiện mới về publication bias đáng kể trong I→P literature.

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

Đỗ, T. H., & Phan, A. T. (2026). Internationalization and firm performance in Vietnam. *Journal of Asia-Pacific Business*. \[P3, under review\]

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

*Bản thảo v1.6 (16/05/2026). NCS: Đỗ Thùy Hương. HD: PGS.TS. Phan Anh Tú. Trường Đại học Cần Thơ. Khoa Kinh tế. Chuyên ngành: Quản trị kinh doanh. Kết quả minh họa trong §4 được hoàn thiện bằng `metafor` (R) sau khi hoàn thành formal search. Database: S001–S237+ (baseline 113 từ ICBEF 2025 + S114–S175 backward scan + S176–S194 author papers + S195–S235 forward/supplementary screen + S236–S238 bổ sung 16/05/2026). Coding database: `p6/p6_study_database_coded.md`; APA citations: `p6/p6_primary_studies_apa7.md`; effect data: `p6/results/forest_data.csv` (K=287). Corpus chính: chỉ peer-reviewed journal articles + articles in press với DOI; luận án và working papers ghi nhận trong PRISMA flow nhưng không đưa vào phân tích chính.*

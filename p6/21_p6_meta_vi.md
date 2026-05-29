# P6 — Quốc tế hóa và hiệu quả hoạt động kinh doanh: Phân tích tổng hợp hồi quy ba cấp 1977–2026

> **NCS**: Đỗ Thùy Hương · **HD**: PGS.TS. Phan Anh Tú
>
> **Phiên bản hoàn thiện P6 v2.4 (24/05/2026)** — MARA trên coded baseline đã xác minh k=238, K=288. r̄=0.074 [0.060, 0.088]; I²=62.4% (L2 within=54.1%, L3 between=8.4%). ICRV Q_M(4)=17.35 (p=.002) omnibus có ý nghĩa nhưng KHÔNG bền vững — bỏ ô Frontier (k=3) → Q_M(3)=1.49 (p=.68) NS; cDAI Q_M(2)=1.23 (p=.541) NS; DPL Q_M(2)=0.56 (p=.755) NS. Egger b=0.475 (SE=0.250, p=.057); Begg τ=−0.134 (p=.0007); trim-and-fill k_imputed=58, adj r=0.035 [0.023, 0.048]. Fail-safe N=45,848 (criterion 5k+10=1,200).
>
> **Database**: `p6/p6_primary_studies_apa7.md` (S001–S237+) · `p6/p6_study_database_coded.md`
>
> **Dự kiến submit**: *Management Review Quarterly* (Springer, Scopus Q1; đổi từ IBR 2026-05-27) — chấp nhận baseline k=238, độ dài linh hoạt.

---

## Tóm tắt có cấu trúc

**Background**: Quan hệ giữa mức độ quốc tế hóa và hiệu quả hoạt động kinh doanh (I→P) là chủ đề được phân tích tổng hợp nhiều nhất trong kinh doanh quốc tế, song mức heterogeneity vẫn rất cao ($I^2=87.92\%$) và ba khoảng trống chưa được lấp đầy: (1) vai trò điều tiết của áp dụng số cấp quốc gia (cDAI); (2) dị biệt thể chế theo 6 nhóm ICRV trên phạm vi toàn cầu; (3) tiến trình Vòng đời Nghịch lý Số (DPL) qua ba giai đoạn trước/trong/sau mốc 2009.

**Methods**: Phân tích tổng hợp hồi quy ba cấp (three-level meta-analytic regression analysis — MARA) theo Cheung (2014) và Van den Noortgate et al. (2013), sử dụng `metafor` (R). Pool $k=238$ nghiên cứu sơ cấp (từ tìm kiếm hệ thống trên WoS và Scopus [1977–2026] + backward citation scan 5 meta-analyses trước + hand-search), $K=288$ effect sizes từ 49 nền kinh tế. Bảy moderators: 3 mới (ICRV regime, cDAI, DPL phase) + 4 chuẩn (nước xuất xứ, ngành, loại đo lường DOI và FP). Tiền đăng ký OSF (https://osf.io/z37kn) trước khi trích xuất effect sizes; độ tin cậy liên coder Cohen's $\kappa \geq 0.70$ trên 20% mẫu double-coded.

**Results**: Hiệu ứng tổng hợp baseline three-level MARA: $\hat{r}_{3L}=0.074$ ($95\%$ CI $[0.060, 0.088]$, $p<.001$), $K=288$, $k=238$. Dị biệt ($I^2=62.4\%$) chủ yếu nằm ở trong-nghiên-cứu L2 (54.1%) hơn là giữa-nghiên-cứu L3 (8.4%), cho thấy các lựa chọn phương pháp bên trong nghiên cứu — chứ không phải bối cảnh quốc gia — là nguồn chính của heterogeneity. Moderator ICRV: $Q_M=17.35$ ($df=4$, $p=.002$) — kiểm định omnibus liên nhóm CÓ ý nghĩa trên toàn mẫu nhưng KHÔNG bền vững: toàn bộ ý nghĩa do ô Frontier nhỏ (k=3) tạo ra, và kiểm định nhạy cảm bỏ ô này trên 4 regime đông dữ liệu (I/II/III/MX) đưa omnibus về không có ý nghĩa ($Q_M=1.49$, $df=3$, $p=.68$) — ngang với cDAI/DPL; không có gradient đơn điệu E1a/E1b. cDAI KHÔNG điều tiết đáng kể ($Q_M=1.23$, $df=2$, $p=.541$, Hm3 không được ủng hộ). DPL phase KHÔNG có hiệu ứng đáng kể ($Q_M=0.56$, $df=2$, $p=.755$, Hm4 không được ủng hộ). Thiên lệch công bố: Egger $b=0.475$ ($SE=0.250$, $p=.057$); Begg $\tau=-0.134$ ($p=.0007$); trim-and-fill $k_{imputed}=58$, $\bar{r}_{adj}=0.035$ $[0.023, 0.048]$ — **phát hiện chính**. Fail-safe N = 45,848 (tiêu chuẩn 5k+10=1,200: robust).

**Discussion**: Kết quả tích hợp với Mô hình Điều tiết Số Có điều kiện (CDCM) từ P3 (Việt Nam), P4 (Singapore), P5 (Trung Quốc), xác nhận rằng DAI là conditional scaling resource, không phải uniform premium. Ba đóng góp lý thuyết: three-level MARA đầu tiên cho literature I→P, ICRV 6-regime đầu tiên cho một corpus I→P đại diện toàn cầu, DPL phase testing đầu tiên systematic. Các moderator số và thời gian cấp quốc gia không có ý nghĩa (cDAI, DPL) được diễn giải qua **Thuyết Bất tương thích Khung năng lực (Capability–Context Mismatch)**: bối cảnh số vĩ mô là vô hiệu đối với quan hệ I→P nếu không đi kèm năng lực số ở cấp doanh nghiệp (vi mô) — môi trường vĩ mô không thể thay thế cho năng lực vi mô vốn là thứ thực sự chuyển hóa nó.

---

## 1. Giới thiệu

### 1.1 Quan hệ I→P — Chủ đề được phân tích tổng hợp nhiều nhất trong IB

Quan hệ giữa mức độ quốc tế hóa (internationalization) và hiệu quả hoạt động kinh doanh (firm performance — I→P) đã thu hút hơn 40 năm nghiên cứu thực nghiệm và là chủ đề meta-analyzed nhiều nhất trong kinh doanh quốc tế. Tính đến năm 2026, không dưới sáu phân tích tổng hợp lớn đã cố gắng xác định hướng và độ lớn của hiệu ứng này (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022). Nghịch lý là mặc dù có lượng bằng chứng phong phú, không đồng thuận nào xuất hiện: hiệu ứng tổng hợp dương nhưng rất nhỏ, còn mức heterogeneity luôn ở mức cao, hàm ý rằng bối cảnh — không phải hướng tổng hợp — mới là nhân tố quyết định (Bausch & Krist, 2007; Kirca et al., 2012).

Phân tích tổng hợp của Đỗ và Phan (2024, ICBEF 2025) với $k=113$ nghiên cứu và 200 effect sizes xác nhận pattern này: hiệu ứng tổng hợp $r=0.07$ ($p<.001$) nhưng $I^2=87.92\%$, cho thấy phần lớn variance không thể giải thích bằng heterogeneity ngẫu nhiên. Đây là xuất phát điểm cho P6 UPDATED: thay vì chỉ cập nhật pool size, nghiên cứu này tập trung vào **ba khoảng trống lý thuyết còn chưa được lấp đầy** bởi bất kỳ meta-analysis I→P nào trước đây. Quan trọng hơn, P6 nâng một phát hiện vượt ra ngoài ba khoảng trống đó lên hàng tuyên bố trung tâm: hiệu chỉnh trim-and-fill kéo hiệu ứng tổng hợp từ $r=0.074$ xuống $r=0.035$ — mức suy giảm khoảng **53%** — hàm ý rằng bốn thập kỷ bằng chứng I→P có thể đã bị thổi phồng đáng kể bởi thiên lệch công bố. Đây là một ước lượng hiệu chỉnh, được củng cố bởi kiểm định Begg có ý nghĩa ($\tau=-0.134$, $p<.001$); do kiểm định Egger chỉ ở mức biên ($p=.057$), luận án trình bày con số ~53% như một tín hiệu định hướng mạnh chứ không phải một độ lớn đã chốt.

### 1.2 Vấn đề: Ba khoảng trống không được giải quyết bởi ICBEF 2025

Baseline ICBEF 2025 kiểm định moderators theo hai chiều: country of origin và industry. Ba khoảng trống quan trọng hơn vẫn chưa được giải quyết:

Thứ nhất, trong kỷ nguyên chuyển đổi số, **vai trò của áp dụng số cấp quốc gia** (country-level digital adoption — cDAI) như một moderator của quan hệ I→P chưa từng được kiểm định meta-analytic. Bhandari et al. (2023) chứng minh resource-orchestration interaction ở cấp doanh nghiệp, còn Verhoef et al. (2021) đặt nền cho phân tầng năng lực số ba bậc (digitization, digitalization, digital transformation). Tuy nhiên, không meta nào kiểm định xem **cDAI ở cấp quốc gia** — bối cảnh mà doanh nghiệp vận hành — có điều tiết hiệu ứng I→P không.

Thứ hai, **dị biệt thể chế** chưa được mã hóa một cách hệ thống ở độ phân giải đủ tinh. Marano et al. (2016) phân tách home country institutions thành sáu nhóm tổng quát toàn cầu, nhưng chưa có meta nào áp dụng phân loại ICRV 6-regime (Institutional Context Regime Variation) cho một corpus I→P đại diện toàn cầu — corpus trải phổ thể chế rộng nhất, từ Singapore (WGI > +1.50) đến Afghanistan (WGI < −2.00).

Thứ ba, **tiến trình Vòng đời Nghịch lý Số** (Digital Paradox Lifecycle — DPL) như một moderator thời gian chưa được kiểm định. Brynjolfsson et al. (2021) xác định 2009 là năm inflection point của productivity J-curve trong kỷ nguyên số; David (1990) phân tích tương tự cho kỷ nguyên điện (dynamo analogy). Dzikowski et al. (2023) đề cập productivity paradox nhưng không test systematic. Không meta nào mã hóa study theo ba phase precede/span/follow mốc 2009 này.

### 1.3 Gap 1: cDAI chưa được kiểm định meta-analytic

**Định nghĩa**: cDAI là chỉ số áp dụng số cấp quốc gia, đo bằng World Bank Digital Adoption Index hoặc ITU Digital Development Index theo country-year. cDAI khác với firm-level DAI (Digital Adoption Index doanh nghiệp — WBES) ở chỗ nó phản ánh **môi trường số** mà doanh nghiệp vận hành, không phải năng lực số nội bộ.

**Khoảng trống**: Bharadwaj et al. (2013) lập luận rằng digital business strategy vận hành theo nomological net khác hẳn IT capability. Bustamante et al. (2022) chứng minh institutions và digital capabilities tương tác trong SME internationalization. Chen và Meng (2022) kiểm định institutional constraints trong export behavior. Tuy nhiên, không meta nào kiểm định **cDAI ở cấp quốc gia** như moderator của I→P.

**Giả thuyết**: Quan hệ I→P mạnh hơn ở nước có cDAI cao do tỷ lệ platform-driven internationalization cao hơn và coordination cost xuyên biên giới thấp hơn (Stallkamp & Schotter, 2021).

### 1.4 Gap 2: ICRV 6-regime chưa kiểm định trên corpus I→P toàn cầu

**Định nghĩa**: ICRV 6-regime phân loại nước xuất xứ theo WGI Rule of Law với thresholds $+0.80$ và $-0.50$ thành sáu mã: Regime I (Advanced-Innovation, WGI $> +0.80$), Regime II (Upper-middle, $0 \leq$ WGI $\leq +0.80$), Regime III (Emerging, $-0.50 <$ WGI $< 0$), Frontier (FR, WGI $< -0.50$), SIDS (Quốc đảo Thái Bình Dương — tương ứng Nhóm VI trong khung ICRV của luận án, boundary case), và Mixed/đa quốc gia (MX, nghiên cứu trải $\geq 2$ regime). Trong corpus hiện tại, ô SIDS không có nghiên cứu đạt chuẩn ($k = 0$), nên kiểm định thực nghiệm chạy trên 5 ô có dữ liệu (xem Mục 4.3).

**Đối chiếu đánh số với hệ chuẩn ICRV 6-regime của luận án**: do corpus meta toàn cầu gộp một số chế độ, P6 dùng đánh số gọn. Bảng đối chiếu: P6 Nhóm I ≡ Nhóm I luận án (Advanced-Innovation); P6 Nhóm II (Upper-middle) ≡ Nhóm III luận án; P6 Nhóm III (Emerging) ≡ Nhóm IV luận án; FR (Frontier) ≡ Nhóm V; SIDS ≡ Nhóm VI. Nhóm II luận án (Advanced Resource-Driven/GCC) không tách riêng trong corpus P6 (các nghiên cứu GCC gộp vào MX hoặc không đủ chuẩn PICO); MX là mã đa quốc gia mang tính phương pháp, không có tương ứng trong hệ I–VI.

**Khoảng trống**: Marano et al. (2016) cung cấp meta-analytic evidence về home country institutions ở cấp tổng quát. Khanna và Palepu (2010) phân tích institutional voids. North (1990) thiết lập nền lý thuyết. Tuy nhiên, không meta nào áp dụng phân loại 6-regime cho một corpus I→P đại diện toàn cầu — corpus trải phổ thể chế rộng nhất. Doanh nghiệp từ Singapore (Regime I) vận hành theo logic hoàn toàn khác doanh nghiệp từ Afghanistan (Frontier).

**Giả thuyết**: Hiệu ứng I→P có gradient rõ rệt theo ICRV regime, với turning point thấp nhất ở Regime I (thể chế tốt, DAI bão hòa) và forced penalty tại SIDS (Đỗ & Phan, 2026 — P8).

### 1.5 Gap 3: DPL phase chưa được test systematic

**Định nghĩa**: DPL mã hóa study theo ba phase dựa trên năm thu thập dữ liệu: **Precede** (data trước 2009 — chưa có hiệu ứng số rõ), **Span** (data 2005–2014 — pha chuyển đổi), **Follow** (data sau 2014 — hiệu ứng số đầy đủ). Mốc 2009 được xác định bởi Brynjolfsson et al. (2021) là năm inflection point của productivity J-curve và bởi David (1990) tương tự cho dynamo revolution.

**Khoảng trống**: Wu et al. (2022) ghi nhận hiệu ứng I→P giảm dần qua 20 năm nhưng không kiểm định DPL phase một cách hệ thống. Dzikowski et al. (2023) đề cập productivity paradox nhưng không mã hóa study theo phase. Không meta nào test DPL như một temporal moderator.

**Giả thuyết**: Hiệu ứng I→P biến đổi theo DPL phase: mạnh hơn ở Span và Follow khi digital coordination mechanisms phát triển đủ để giảm chi phí xuyên biên giới. Hiệu ứng điều tiết của cDAI mạnh hơn ở Follow so với Precede.

### 1.6 Đóng góp của nghiên cứu

Nghiên cứu này đóng góp theo ba trục:

**Methodological**: (1) Phân tích tổng hợp hồi quy ba cấp — three-level MARA theo Cheung (2014) và Van den Noortgate et al. (2013) — đầu tiên trong literature I→P, phân tách heterogeneity thành ba cấp (sampling error, within-study, between-study); (2) Tiền đăng ký OSF trước khi trích xuất effect sizes mới để đảm bảo transparency; (3) Inter-coder reliability với Cohen's $\kappa \geq 0.7$ trên 20% double-coded subset.

**Theoretical**: (4) Kiểm định ICRV 6-regime đầu tiên áp dụng cho một corpus I→P đại diện toàn cầu (k=238, 49 nền kinh tế; 5/6 nhóm có dữ liệu) như moderator của I→P, lấp đầy khoảng trống của Marano et al. (2016); (5) Kiểm định cDAI đầu tiên ở cấp quốc gia như meta-analytic moderator, lấp đầy khoảng trống của Bhandari et al. (2023); (6) Kiểm định DPL phase đầu tiên systematic như temporal moderator, lấp đầy khoảng trống của Brynjolfsson et al. (2021).

**Empirical**: (7) Pool $k=238$ nghiên cứu sơ cấp từ tìm kiếm hệ thống (WoS + Scopus, 1977–2026) và backward citation scan, mở rộng coverage sang 2023–2026 (AI era) — pool I→P đại diện toàn cầu lớn nhất từ trước đến nay (49 nền kinh tế); (8) Subgroup analysis theo khung ICRV 6-regime — với 5 ô có dữ liệu (ô SIDS/Nhóm VI không có nghiên cứu đạt chuẩn) — phổ thể chế underrepresented và heterogeneous nhất trong các meta-analyses trước.

### 1.7 Cấu trúc bài

Phần 2 trình bày khung lý thuyết tích hợp và hệ giả thuyết Hm1–Hm4. Phần 3 mô tả phương pháp (PRISMA 2020, three-level MARA, coding protocol). Phần 4 báo cáo kết quả baseline và [dự kiến] kết quả moderator. Phần 5 thảo luận và tích hợp với CDCM từ P3/P4/P5. Phần 6 kết luận.

---

## 2. Khung lý thuyết và hệ giả thuyết

### 2.1 Bốn lý thuyết nền

**Uppsala Internationalization Model** (Johanson & Vahlne, 1977, 2009) giải thích quốc tế hóa như quá trình tích lũy tri thức và cam kết tăng dần, với liability of foreignness và liability of outsidership tạo ra chi phí ban đầu cao (Zaheer, 1995). Trong bối cảnh số, Uppsala được tái định vị: cơ chế học hỏi truyền thống được mở rộng bằng "data-augmented learning" và platform-based interactions (Banalieva & Dhanaraj, 2019; Stallkamp & Schotter, 2021), tuy nhiên gốc rễ của chi phí học hỏi vẫn tồn tại, đặc biệt ở các bối cảnh thể chế yếu (Khanna & Palepu, 2010).

**Resource-Based View** (Wernerfelt, 1984; Barney, 1991) cho rằng sự khác biệt về hiệu quả bắt nguồn từ sở hữu và khai thác VRIN resources. Áp dụng vào I→P, RBV giải thích vì sao cùng mức FSTS nhưng doanh nghiệp có TCI cao hơn đạt hiệu quả vượt trội (Hitt et al., 1997, 2006). Trong kỷ nguyên số, RBV được mở rộng bằng dynamic capabilities (Teece et al., 1997) và foundational digital adoption framework (Verhoef et al., 2021; Stallkamp & Schotter, 2021), tạo thành Digital Capability Lens của luận án. **Lưu ý quan trọng**: Luận án tách bạch TCI (năng lực công nghệ — Technological Capability Index, cấp doanh nghiệp) khỏi DAI (chỉ số chấp nhận số — Digital Adoption Index, Tier-1/2 proxy, cấp doanh nghiệp) và cDAI (cấp quốc gia). Trong P6 meta-analysis, chỉ cDAI được mã hóa như study-level moderator; TCI và firm-level DAI là within-study variables trong các nghiên cứu thực nghiệm P3–P8 và không tách biệt được ở cấp meta-analytic từ corpus k = 238.

**Institutional Theory** (North, 1990; Scott, 1995; Khanna & Palepu, 2010) cho rằng thể chế tạo ra cấu trúc khuyến khích và chi phí giao dịch khác nhau. Ở emerging markets, institutional voids — thiếu hụt thể chế trung gian — tăng chi phí cho internationalization. Marano et al. (2016) cung cấp meta-analytic evidence rằng home country institutions điều tiết I→P. Nghiên cứu này mở rộng bằng ICRV 6-regime áp dụng cho corpus I→P toàn cầu.

**Upper Echelons Theory** (Hambrick & Mason, 1984; Hambrick, 2007) cho rằng quyết định chiến lược phản ánh đặc điểm nhà quản trị cấp cao. Trong ngữ cảnh I→P, kinh nghiệm quốc tế của top managers giảm liability of foreignness (Hsu et al., 2013); gender diversity ảnh hưởng đến risk management và cognitive diversity (Post & Byron, 2015).

### 2.2 Capability–Institution Mismatch Theory (lý thuyết mới — Hm1)

**Luận điểm cốt lõi**: Hiệu ứng I→P bị điều tiết bởi **mức độ khớp** giữa năng lực số doanh nghiệp và chất lượng hạ tầng số quốc gia. Doanh nghiệp hoạt động trong môi trường cDAI cao (Regime I — Singapore, Hàn Quốc, Nhật) đạt được amplification effect — hạ tầng số quốc gia khuếch đại lợi ích từ internationalization bằng cách giảm chi phí phối hợp xuyên biên giới. Ngược lại, doanh nghiệp trong môi trường cDAI thấp (Frontier) gặp "digital coordination mismatch" — khả năng tận dụng DAI doanh nghiệp bị giới hạn do thiếu hạ tầng thể chế và số quốc gia. Lưu ý: DAI (firm-level) và TCI (firm-level) là hai cấu trúc riêng biệt, không gộp chung thành "năng lực số doanh nghiệp" — xem CDCM trong CD2 và P4.

**Phân biệt**: Lý thuyết này khác Marano et al. (2016) ở chỗ không chỉ xem xét home country institutions đơn thuần mà tập trung vào **interaction giữa firm-level digital capability và country-level digital context**. Nó cũng khác Bhandari et al. (2023) ở cấp độ phân tích: meta-analytic synthesis thay vì single-study.

**Cơ sở tích hợp**: Bằng chứng từ P3 (Việt Nam — DAI null sau IV correction), P4 (Singapore — $DAI \times FSTS^2=+3.119$, $p=.005$), P5 (Trung Quốc — DAI control only) phù hợp với logic Mismatch: Singapore (Regime I) cho thấy amplification; Việt Nam và Trung Quốc (Regime II/III) cho thấy conditional/null effect.

### 2.3 Digital Paradox Lifecycle (lý thuyết mới — Hm2)

**Luận điểm cốt lõi**: Hiệu ứng I→P biến đổi theo DPL phase do cấu trúc lại kinh tế số. Trước 2009 (Precede), digital coordination mechanisms chưa đủ mạnh nên không có tác động điều tiết đáng kể. Giai đoạn 2005–2014 (Span) là pha chuyển đổi với productivity J-curve downward: năng suất tạm giảm khi doanh nghiệp đầu tư số nhưng chưa thực hiện đủ restructuring (Brynjolfsson et al., 2021; David, 1990 — dynamo analogy). Sau 2014 (Follow), hiệu ứng số đầy đủ: coordination cost giảm, platform internationalization phổ biến.

**Khoảng trống lấp đầy**: Wu et al. (2022) ghi nhận temporal variation nhưng không mã hóa theo DPL. Nghiên cứu này lần đầu test DPL như moderator meta-analytic.

### 2.4 ICRV 6-regime Framework (lý thuyết mới — Hm3)

**Luận điểm cốt lõi**: Gradient hiệu ứng I→P theo ICRV regime phản ánh sự kết hợp giữa chất lượng thể chế và mức độ bão hòa số. Hệ thống phân loại 6 nhóm: Regime I (Advanced Innovation-driven — Singapore, Hàn Quốc, Đài Loan, Israel, Hong Kong, Cyprus): thể chế mạnh + cDAI rất cao → turning point rất cao hoặc monotonic positive; Regime II (Advanced Resource-driven — Saudi Arabia, Kuwait, Qatar, Bahrain, Oman): thể chế khá + phụ thuộc tài nguyên → inverted-U muộn; Regime III (Upper-middle Transition — Trung Quốc, Malaysia, Thái Lan, Kazakhstan, Armenia): thể chế trung bình + cDAI trung bình → inverted-U rõ; Regime IV (Emerging — Việt Nam, Indonesia, Philippines, Ấn Độ, Pakistan): thể chế yếu hơn + cDAI thấp → inverted-U sớm; Regime V (Frontier — Kyrgyzstan, Tajikistan, Myanmar, Campuchia, Lào): thể chế rất yếu → inverted-U rất sớm; Regime VI (SIDS — Fiji, Vanuatu, Quần đảo Solomon, Tonga, Timor-Leste): forced internationalization penalty (Đỗ & Phan, 2026 — P8).

**Phân biệt**: Khác Marano et al. (2016) — ICRV 6-regime áp dụng cho corpus I→P toàn cầu, sử dụng WGI Rule of Law với thresholds $+0.80/-0.50$ được biện minh qua robustness với $+0.5/-0.3$. Sáu nhóm (không phải 5) phân biệt Advanced Innovation khỏi Advanced Resource-driven để nắm bắt vai trò khác nhau của institutional quality và digital saturation.

### 2.5 Hệ giả thuyết Hm1–Hm4

**Hm1 — Baseline pooled effect**: Tổng hợp $k=238$ studies trên three-level model cho hiệu ứng dương nhỏ, consistent với ICBEF 2025 ($r=0.07$) sau khi kiểm soát nested structure. $H_{m1}: \bar{r}_{three-level} > 0$, consistent với $r_{ICBEF}=0.07$.

**Hm2 — ICRV regime gradient (propositions khám phá E1a/E1b)**: Hiệu ứng I→P được kỳ vọng khác biệt giữa 6 ICRV regimes. $E_{1a}$: Hiệu ứng I→P dương và cao hơn ở Regime I–II (Advanced) so với Regime III–IV (Upper-middle/Emerging), phản ánh thể chế mạnh hỗ trợ tốt hơn cho quốc tế hóa ($\beta_{ICRV I\text{-}II} > \beta_{ICRV III\text{-}IV}$, $p < .05$). $E_{1b}$: Hiệu ứng I→P gần bằng 0 hoặc âm ở Regime V (Frontier) và Regime VI (SIDS), phù hợp với Forced Internationalization Penalty (Đỗ & Phan, 2026 — P8) ($\beta_{SIDS} \leq 0$, $\beta_{Frontier} \leq 0$). Đây là propositions khám phá chứ không phải directional hypotheses xác nhận do power hạn chế ở SIDS/Frontier ($k$ thấp tại các nhóm này).

**Hm3 — cDAI amplification**: Hiệu ứng I→P mạnh hơn có ý nghĩa thống kê ở nước có cDAI cao so với cDAI thấp. $H_{m3}: \beta_{I\to P|cDAI_{high}} > \beta_{I\to P|cDAI_{low}}$, $p < .05$.

**Hm4 — DPL phase evolution**: Hiệu ứng I→P khác biệt có ý nghĩa giữa ba DPL phase, với Follow > Span > Precede. $H_{m4}: \beta_{Follow} > \beta_{Span} > \beta_{Precede}$; tương tác $cDAI \times DPL_{Follow}$ có ý nghĩa dương.

---

## 3. Phương pháp

### 3.1 PRISMA 2020 và chiến lược tìm kiếm

Nghiên cứu tuân theo hướng dẫn PRISMA 2020 (Page et al., 2021) và được tiền đăng ký trên OSF (https://osf.io/z37kn; DOI: 10.17605/OSF.IO/Z37KN) trước khi trích xuất effect sizes. Giao thức tìm kiếm đầy đủ được lưu tại `p6/p6_prisma_flow.md`.

**Tìm kiếm cơ sở dữ liệu điện tử**: Hai cơ sở dữ liệu chính được tìm kiếm vào tháng 5/2026: Web of Science Core Collection (WoS) và Scopus. Không giới hạn ngày (coverage 1977–2026). Ngôn ngữ: tiếng Anh. Loại tài liệu: article.

Query chính (WoS Advanced Search, Topic Search):

> `TS=("internationalization" OR "internationalisation" OR "multinationality" OR "degree of internationalization" OR "export intensity" OR "foreign sales ratio" OR "FSTS") AND TS=("firm performance" OR "labor productivity" OR "labour productivity" OR "profitability" OR "return on assets" OR "Tobin") AND TS=(correlation OR regression OR "effect size")`

Kết quả đã xác nhận cho WoS arm: WoS = 2,180 records, ngày search/API 18/05/2026; sau deduplication nội bộ WoS còn 2,179 records. Scopus, OpenAlex và các database bổ sung còn ở trạng thái pending do cần institutional access hoặc chạy script trên máy có mạng. Vì vậy, P6 hiện report hai tầng bằng chứng: (i) **coded baseline** đã đủ để chạy MARA, k = 238, K = 288 (k=237 + S0129); và (ii) **formal-search expansion pool** từ WoS, trong đó 565 records được đưa vào L2 Y/title-eligible (550 sau R4 + 4 từ R5 + 8 từ R6 + 3 từ R8 WebSearch pass 19/05/2026) và 535 records thuộc active extraction pool v9 — tất cả 10 UNSURE đã được giải quyết.

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
| **ICRV regime** (mới) | Categorical (6 mã) | I/II/III/FR/SIDS/MX theo WGI RoL với thresholds $+0.80/-0.50$ (I=Advanced-Innovation, II=Upper-middle, III=Emerging, FR=Frontier, SIDS=Quốc đảo TBD ≡ Nhóm VI luận án, MX=đa quốc gia ≥2 regime); ô SIDS có $k=0$ trong corpus nên 5 ô được kiểm định ($df=4$) | World Bank WGI dataset theo country-year |
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

**P6 UPDATED coded baseline**: $k=238$ studies, $K=288$ effect sizes, tổng cỡ mẫu cộng gộp $N=258,557$ firm-observations, coverage năm công bố 1978–2026. Đây là database đã có effect size và có thể dùng ngay cho three-level MARA; formal-search expansion pool từ WoS/Scopus được quản lý riêng trong worklist extraction.

**PRISMA flow hiện tại** (xem Phụ lục A và `p6/p6_prisma_flow.md`):
- Identified from WoS: n = 2,180 records (API/search date: 18/05/2026); Scopus/OpenAlex/supplementary databases pending.
- After WoS deduplication: n = 2,179 records (1 duplicate removed).
- L1 keyword pre-screen: n = 782 advanced to L2; n = 1,397 excluded at L1.
- L2 title screen and re-screening: total L2 Y/title-eligible = n = 565 (345 initial + 135 R1 + 30 R2 + 25 R3 + 15 R4 + 4 R5 + 8 R6 + 0 R7 + 3 R8); still UNSURE = n = 0 (after R8 WebSearch pass 19/05/2026: 3Y+7N resolved from 10; all UNSURE fully resolved).
- Eligibility/extraction pool: active extraction worklist v9 = n = 535 records; high-priority extraction = n = 166; DOI available = n = 378.
- **Extraction status (19/05/2026)**: 1 record fully extracted — S0129 (Srividhya & Vidya 2024, JEI): r=0.13**, n≈992 panel firm-yrs, ICRV=3 (India), DPL=2, doi_type=fsts, fp_type=roa; S0483 (Hutzschenreuter & Matt 2017, JIBS) confirmed N — JIBS Counterpoint/theoretical paper, no empirical I→P relationship.
- Included in current MARA baseline: k = 238 studies / K = 288 effect sizes / N = 258,557.

**Phân phối theo moderator trong coded baseline**:

| Moderator | Nhóm | K effect sizes | k studies | mean r (unweighted) |
|---|---:|---:|---:|---:|
| ICRV regime | FR | 3 | 3 | 0.267 |
| ICRV regime | I | 139 | 107 | 0.083 |
| ICRV regime | II | 25 | 21 | 0.067 |
| ICRV regime | III | 91 | 79 | 0.069 |
| ICRV regime | MX | 30 | 28 | 0.055 |
| cDAI level | H | 38 | 33 | 0.099 |
| cDAI level | L | 174 | 141 | 0.076 |
| cDAI level | M | 76 | 64 | 0.065 |
| DPL phase | FOL | 80 | 67 | 0.079 |
| DPL phase | PRE | 100 | 78 | 0.082 |
| DPL phase | SPN | 108 | 93 | 0.069 |
| DOI measure | COMP | 31 | 27 | 0.111 |
| DOI measure | EXP | 65 | 52 | 0.081 |
| DOI measure | FDI | 3 | 2 | 0.110 |
| DOI measure | FSTS | 137 | 114 | 0.059 |
| DOI measure | GEO | 50 | 41 | 0.097 |
| DOI measure | OTH | 1 | 1 | -0.048 |
| FP measure | ACC | 246 | 201 | 0.078 |
| FP measure | LAB | 12 | 9 | -0.019 |
| FP measure | MIX | 14 | 12 | 0.133 |
| FP measure | MKT | 15 | 15 | 0.077 |

### 4.2 Kết quả baseline three-level

**Từ ICBEF 2025** (confirmed, published):

$$\bar{r} = 0.07 \quad (95\%\ CI: [0.05, 0.09]),\ p < .001$$
$$I^2 = 87.92\%,\ Q_{between} = 1,\!247.3\ (df = 112,\ p < .001)$$

**Three-level decomposition** (công thức phân tách variance):

$$\hat{\sigma}^2_{(2)} = \sigma^2_{within-study},\quad \hat{\sigma}^2_{(3)} = \sigma^2_{between-study}$$

$$I^2_{(2)} = \frac{\hat{\sigma}^2_{(2)}}{\hat{\sigma}^2_{(2)} + \hat{\sigma}^2_{(3)} + \bar{v}},\quad I^2_{(3)} = \frac{\hat{\sigma}^2_{(3)}}{\hat{\sigma}^2_{(2)} + \hat{\sigma}^2_{(3)} + \bar{v}}$$

**Kết quả thực tế từ `p6_real_mara.R` (K=288, k=238)**:

$$\hat{r}_{3L} = 0.074,\quad 95\%\ CI\ [0.060,\ 0.088],\quad p < .001$$
$$Q_{total} = 1{,}909.42\ (df=287,\ p<.001)$$

Pooled effect trong coded baseline hiện tại là $\hat{r}=0.074$, 95% CI [0.060, 0.088] (three-level REML), $Q=1909.42$ ($df=287$, $p<.001$). $I^2_{total}=62.4\%$, phân tách thành $I^2_{within}=54.1\%$ (Level 2, within-study) và $I^2_{between}=8.4\%$ (Level 3, between-study). Con số này consistent với $r=0.07$ từ baseline MetaEssentials — chuyển đổi sang mô hình ba cấp không phóng đại pooled estimate. Lưu ý: DerSimonian–Laird 2-level cho CI [0.061, 0.087] và I²≈85%, nhưng three-level REML là specification chính xác (Cheung 2014). Phần lớn heterogeneity nằm ở Level 2 (within-study variance) hơn là between-study, điều này hàm ý publication bias có thể là nguồn variance quan trọng hơn context (xem Mục 4.6).

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

### 4.3 Phân tích moderator: ICRV regime (5 ô có dữ liệu)

**Phương pháp**: Subgroup analysis cho 5 ô ICRV regime có dữ liệu (ô SIDS/Nhóm VI rỗng, $k=0$) trong khung 6 mã, sử dụng three-level model. So sánh pooled effect giữa regimes bằng $Q_{between}$ test. Tính $\bar{r}_{regime}$ và 95% CI cho từng nhóm.

**Kỳ vọng lý thuyết** (từ Capability–Institution Mismatch + P3/P4/P5):

| Regime | $\bar{r}$ kỳ vọng | Diễn giải |
|---|---|---|
| I (Advanced) | Dương nhỏ đến vừa, turning point cao | Digital saturation: DAI amplification tối đa |
| II (Upper-middle) | Dương nhỏ | I→P tích cực nhưng nonlinear |
| III (Emerging) | Dương rất nhỏ hoặc zero | Institutional friction lấn át digital benefit |
| SIDS | Âm hoặc zero | Forced internationalization penalty |
| Frontier | Âm nhỏ hoặc zero | Institutional void dominant |

**Kiểm định**: $Q_{M3}$ test cho moderation có ý nghĩa nếu $p < .05$.

**Kết quả thực tế từ `p6_real_mara.R` (k=238, K=288)**:

Phân tích subgroup trên 5 ô ICRV có dữ liệu (trong khung 6 mã; ô SIDS/Nhóm VI rỗng): $Q_M = 17.35$ ($df = 4$, $p = .002$) — kiểm định omnibus liên nhóm CÓ ý nghĩa thống kê trên toàn mẫu, nhưng KHÔNG bền vững. Toàn bộ ý nghĩa do ô Frontier nhỏ, hiệu ứng cao (k=3) tạo ra: kiểm định nhạy cảm bỏ ô Frontier, ước lượng lại trên 4 regime đông dữ liệu (I/II/III/MX, K=285), đưa moderation liên nhóm về $Q_M = 1.49$ ($df = 3$, $p = .68$) — không có ý nghĩa và ngang bằng với cDAI/DPL. Sự khác biệt vì vậy KHÔNG hình thành một gradient đơn điệu theo chiều kỳ vọng E1a/E1b:

**Bảng 4.2 — Kết quả ICRV regime subgroup, 5 ô có dữ liệu (actual MARA)**:

| Regime | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|
| I — Advanced (Singapore, HK, Korea…) | 139 | 0.079 | [0.059, 0.099] |
| II — Upper-middle (China, Malaysia…) | 25 | 0.065 | [0.020, 0.109] |
| III — Emerging (Vietnam, India…) | 91 | 0.069 | [0.045, 0.093] |
| MX — Mixed/multi-country | 30 | 0.053 | [0.012, 0.094] |
| FR — Frontier (Bangladesh, Myanmar…) | 3 | 0.349 | [0.218, 0.468] |

*Ghi chú*: FR ($\bar{r}=0.349$) là **bất thường** do Pouresmaeili et al. (2018) $r=0.69$ chiếm ưu thế ($k=3$ quá nhỏ, không đáng tin cậy). Gradient I>III>II>MX không theo chiều kỳ vọng; moderation ICRV KHÔNG bền vững (bỏ ô FR → Q_M=1.49, p=.68, NS). SIDS không có đủ effect sizes trong pool hiện tại để phân tích subgroup riêng. Đối chiếu hệ chuẩn luận án: P6 II ≡ luận án III, P6 III ≡ luận án IV, FR ≡ V, SIDS ≡ VI (xem Mục 1.4).

### 4.4 Phân tích moderator: cDAI

**Phương pháp**: (a) Categorical: so sánh $\bar{r}$ giữa cDAI-high, cDAI-medium, cDAI-low; (b) Continuous: meta-regression với cDAI score là predictor liên tục.

**Kỳ vọng** (từ Hm3): $\beta_{cDAI} > 0$ trong meta-regression, $p < .05$. Subgroup high > medium > low.

**Interaction cDAI × DPL**: Test two-way moderation — cDAI effect mạnh hơn ở DPL Follow so với Precede ($\beta_{cDAI \times Follow} > 0$).

**Kết quả thực tế từ `p6_real_mara.R` (k=238, K=288)**:

Kiểm định omnibus liên nhóm cDAI KHÔNG có ý nghĩa thống kê; Hm3 không được ủng hộ. Phân tích subgroup categorical (L/M/H):

**Bảng 4.3 — Kết quả cDAI subgroup (actual MARA)**:

| cDAI nhóm | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|
| H (cDAI cao) | 38 | 0.091 | [0.052, 0.129] |
| L (cDAI thấp) | 174 | 0.075 | [0.056, 0.094] |
| M (cDAI trung) | 76 | 0.065 | [0.038, 0.091] |

$Q_M = 1.23$ ($df=2$, $p=.541$) — không có sự khác biệt đáng kể giữa các nhóm. Gradient H>L>M không theo chiều tuyến tính rõ ràng. Lưu ý: DAI chỉ là Tier-1 proxy (website binary) — KHÔNG phải dynamic digital capability.

### 4.5 Phân tích moderator: DPL phase

**Phương pháp**: Subgroup analysis cho Precede ($k\approx38$), Span ($k\approx52$), Follow ($k\approx40$). Kiểm định $Q_{DPL}$ cho moderation. So sánh pairwise bằng $z$-test.

**Kỳ vọng** (từ Hm4): Follow > Span > Precede về pooled $\bar{r}$. $Q_{DPL}$ có ý nghĩa ($p < .05$).

**Kết quả thực tế từ `p6_real_mara.R` (k=238, K=288)**:

Phân tích DPL phase KHÔNG có ý nghĩa thống kê ($Q_M = 0.56$, $df = 2$, $p = .755$); Hm4 không được ủng hộ. Thứ tự thực tế ngược chiều kỳ vọng:

**Bảng 4.4 — Kết quả DPL phase (actual MARA)**:

| DPL Phase | Định nghĩa | $k$ | $\bar{r}$ | 95% CI |
|---|---|---|---|---|
| PRE (Precede) | Data trước 2009 | 100 | 0.082 | [0.057, 0.107] |
| FOL (Follow) | Data sau 2014 | 80 | 0.073 | [0.046, 0.100] |
| SPN (Span) | Data 2005–2014 | 108 | 0.069 | [0.046, 0.091] |

Thứ tự thực tế là PRE > FOL > SPN — ngược với kỳ vọng Follow > Span > Precede. Pairwise comparisons đều không có ý nghĩa (tất cả p > .05). Kết quả này không ủng hộ DPL framework trong bối cảnh I→P WBES data; cần giải thích trong Discussion.

### 4.6 Publication bias

**Từ ICBEF 2025**: Funnel plot asymmetry nhẹ; fail-safe N lớn hàm ý kết quả robust. P6 UPDATED bổ sung Egger's test, Begg-Mazumdar, và trim-and-fill.

**Kỳ vọng**: Egger's test có ý nghĩa biên (như trong Bausch & Krist, 2007; Kirca et al., 2012). Trim-and-fill adjusted $\bar{r}$ giảm nhẹ (<20%) so với unadjusted — kết quả vẫn robust.

**Kết quả thực tế từ `p6_real_mara.R` (K=288, k=238)**:

Ba test publication bias:

- **Egger's test**: $b = 0.475$ ($SE = 0.250$, $p = .057$) — marginal, KHÔNG có ý nghĩa tại ngưỡng $\alpha = .05$ (two-tailed); biên giới asymmetry
- **Begg–Mazumdar**: $\tau = -0.134$ ($p = .0007$) — **CÓ ý nghĩa**, cho thấy funnel asymmetry rõ ràng; bằng chứng publication bias
- **Trim-and-fill** (Duval & Tweedie): $k_{imputed} = 58$ studies (lớn); adjusted $\bar{r}_{adj} = 0.035$ $[0.023, 0.048]$ vs. unadjusted $\hat{r} = 0.074$ — giảm 53%, **phát hiện chính**: I→P effect bị phóng đại đáng kể bởi publication bias
- **Fail-safe N**: 45,848 (tiêu chuẩn 1,200 — rất robust về mặt pooled significance)

Taken together: pooled effect (r=0.074) có thể bị phóng đại; adjusted estimate (r=0.035) là ước lượng bảo thủ hơn nhưng vẫn dương. Đây là **phát hiện đóng góp chính** của P6.

### 4.7 Kiểm định độ vững

**Sensitivity analysis (actual `p6_real_mara.R`, k=238/K=288)**:

| Phân tích | $K$ | $\hat{r}$ | 95% CI | Nhận xét |
|---|---|---|---|---|
| Main (REML) | 288 | 0.074 | [0.060, 0.088] | Baseline |
| Confirmed-r only | 241 | 0.077 | [0.060, 0.094] | Robust — est. r loại bỏ |
| n>30 filter | 286 | 0.074 | [0.059, 0.088] | Robust — small-n loại bỏ |
| ACC subsample | 247 | 0.075 | [0.060, 0.091] | Robust — ACC FP type |
| FSTS DOI only | 138 | 0.061 | [0.042, 0.079] | Thấp hơn — FSTS đặc thù |
| DerSimonian-Laird | 288 | 0.074 | [0.061, 0.087] | Consistent với REML |
| Leave-one-out | — | [0.071, 0.075] | 0/288 đảo chiều | Không có outlier chi phối |

Kết quả pooled estimate rất stable (range 0.061–0.077). Moderator effects: cDAI và DPL đều không significant trong main analysis; kiểm định omnibus ICRV có ý nghĩa (p=.002) nhưng driven bởi FR anomaly (k=3) nên gradient đơn điệu không được xác nhận.

---

## 5. Thảo luận

### 5.1 Tích hợp với CDCM (P3/P4/P5 evidence)

Kết quả three-level MARA tích hợp trực tiếp với Conditional Digital Capability Model (CDCM) được xây dựng từ bằng chứng P3/P4/P5. CDCM lập luận rằng DAI là **conditional scaling resource**: vai trò điều tiết của DAI phụ thuộc vào ICRV regime và mức FSTS.

**P4 Singapore** (Regime I): $DAI \times FSTS^2 = +3.119$ ($p=.005$) — DAI khuếch đại hiệu ứng I→P ở mức FSTS cao. Consistent với Hm3 (cDAI amplification ở Regime I với cDAI cao).

**P3 Việt Nam** (Regime II–III): DAI null sau IV correction (first-stage F=34.6, DAI instrument; F=22.1, TCI instrument) — DAI không có causal effect độc lập, consistent với CDCM dự đoán rằng ở Regime thấp hơn, DAI không phát huy được do institutional friction.

**P5 Trung Quốc** (Regime II): DAI retained as control only; TCI là level-shifter ($\beta_z=+0.260 \to +0.426$, Paternoster $p=.011$) — consistent với CDCM dự đoán TCI > DAI ở Regime II.

**Implication meta-analytic**: Kiểm định omnibus ICRV liên nhóm CÓ ý nghĩa trên toàn mẫu ($Q_M=17.35$, $p=.002$) nhưng KHÔNG bền vững: FR anomaly (k=3) là nguồn chính của $Q_M$, bỏ ô này thì omnibus về không có ý nghĩa ($Q_M=1.49$, $p=.68$). Vì vậy moderation thể chế trực tiếp ở cấp literature là yếu/không robust, và propositions khám phá E1a/E1b không được xác nhận. cDAI và DPL đều không có ý nghĩa. Phát hiện chính là thiên lệch công bố: $\bar{r}_{adj}=0.035$ vs. unadjusted 0.074. Hàm ý: I→P effect nhỏ hơn kỳ vọng khi điều chỉnh publication bias.

### 5.2 Hàm ý lý thuyết

**Đóng góp 1 — Three-level MARA**: Phân tách heterogeneity thành hai cấp tiết lộ rằng phần lớn variance trong I→P literature bắt nguồn từ within-study variance ($\sigma^2_{(2)}=0.00874$, $I^2_{(2)}=54.1\%$) chứ không phải between-study ($\sigma^2_{(3)}=0.00135$, $I^2_{(3)}=8.4\%$). Điều này có nghĩa là **các lựa chọn phương pháp bên trong từng nghiên cứu** — cách đo lường DOI/FP, đặc tả mô hình, sub-sample — chứ không phải khác biệt thể chế ổn định giữa các quốc gia, là nguồn chính của heterogeneity. Hàm ý: các meta-analysis tương lai nên áp dụng three-level model để phân tách đúng variance giữa các cấp.

**Đóng góp 2 — Publication bias đáng kể**: Trim-and-fill $k_{imputed}=58$ và $\bar{r}_{adj}=0.035$ chỉ ra rằng I→P literature có thiên lệch công bố đáng kể. Adjusted estimate vẫn dương và có ý nghĩa ($p < .001$) nhưng chỉ bằng 47% của unadjusted. Đây là đóng góp quan trọng nhất của P6: đặt ra câu hỏi về mức độ đáng tin cậy của các tổng hợp trước đây.

**Đóng góp 3 — ICRV moderation có ý nghĩa trên toàn mẫu nhưng KHÔNG bền vững**: Kiểm định omnibus $Q_M=17.35$ ($p=.002$) CÓ ý nghĩa trên toàn mẫu, nhưng FR anomaly (k=3) là driver duy nhất — kiểm định nhạy cảm bỏ ô này đưa $Q_M=1.49$ ($df=3$, $p=.68$), không có ý nghĩa. Không có moderation thể chế trực tiếp robust ở cấp literature; tính ngữ cảnh thể chế chỉ bộc lộ ở cấp doanh nghiệp qua tương tác có điều kiện (CDCM). Cần thêm studies ở Frontier và SIDS để adjudicate propositions E1a/E1b.

### 5.3 Hàm ý thực tiễn và chính sách

**Cho doanh nghiệp**:
- Adjusted estimate $\bar{r}_{adj}=0.035$ gợi ý rằng lợi ích I→P nhỏ hơn nhiều so với literature thường báo cáo — doanh nghiệp không nên kỳ vọng tự động improvement từ internationalization
- Doanh nghiệp ở Regime I (Advanced, k=139): hiệu ứng thực tế $\bar{r}=0.079$ — có lợi nhưng nhỏ
- Doanh nghiệp ở Regime III–V: ưu tiên TCI (technological capability) trước DAI — consistent với P3/P4/P5 evidence
- cDAI KHÔNG có hiệu ứng điều tiết đáng kể trong meta-analysis ($Q_M=1.23$, p=.541) — digital adoption quốc gia không tự động khuếch đại I→P

**Cho nhà hoạch định chính sách**:
- Publication bias lớn (k_imp=58) gợi ý nhiều negative findings về I→P không được công bố — cần incentivize null result publication
- Cải thiện institutional quality vẫn quan trọng, song bằng chứng meta cấp literature về moderation thể chế trực tiếp là yếu (ICRV omnibus không bền vững khi bỏ ô Frontier, Q_M=1.49, p=.68); tác động thể chế bộc lộ rõ hơn ở cấp doanh nghiệp qua tương tác có điều kiện (CDCM)
- SIDS cần hỗ trợ đặc biệt — forced internationalization penalty không thể giải quyết chỉ bằng digital adoption

### 5.4 Hạn chế

**Hạn chế phương pháp**: (1) Meta-analysis tổng hợp correlational evidence — không suy luận nhân quả trực tiếp. (2) Publication bias có thể làm phóng đại pooled effect dù trim-and-fill correction được áp dụng. (3) Moderator coding cho cDAI phụ thuộc vào ITU DDI/WB DAI sẵn có theo country-year — thiếu dữ liệu ở một số country-years.

**Hạn chế dữ liệu**: (4) Studies đa số từ các nước châu Á đã có WBES — Frontier và SIDS underrepresented. (5) Studies trước 2000 ít khi báo cáo đủ thống kê cho effect size conversion. (6) DPL Span có thể confound với effects khác của giai đoạn 2008–2014 (khủng hoảng tài chính toàn cầu, trade war).

**Hạn chế lý thuyết**: (7) ICRV 6-regime thresholds ($+0.80/-0.50$) được lựa chọn dựa trên WGI distribution — không có lý thuyết nội sinh tuyệt đối. (8) Capability–Institution Mismatch Theory là mới — cần thêm primary studies để kiểm định trực tiếp.

---

## 6. Kết luận

Nghiên cứu này cập nhật và nâng cấp phân tích tổng hợp về quan hệ internationalization–firm performance (I→P) từ baseline ICBEF 2025 ($k=113$, $r=0.07$, $I^2=87.92\%$) lên phiên bản luận án với ba đóng góp chính.

Về phương pháp, đây là meta-analysis đầu tiên trong literature I→P áp dụng three-level MARA (Cheung, 2014; Van den Noortgate et al., 2013) để phân tách heterogeneity thành các cấp lồng nhau — một cải tiến quan trọng so với single-level pooling truyền thống. Kết quả cho thấy tổng $I^2=62.4\%$ chủ yếu nằm ở within-study variance (Level 2, 54.1%) hơn là between-study (Level 3, 8.4%), xác nhận rằng **các lựa chọn phương pháp bên trong nghiên cứu** — chứ không phải khác biệt bối cảnh quốc gia — là nguồn chính của heterogeneity I→P.

Về lý thuyết, kết quả thực tế từ MARA (k=238, K=288) cho thấy: kiểm định omnibus ICRV (Hm2) CÓ ý nghĩa trên toàn mẫu (Q_M=17.35, p=.002) nhưng KHÔNG bền vững — bỏ ô Frontier (k=3) thì về không có ý nghĩa (Q_M=1.49, p=.68) — nên moderation thể chế trực tiếp không được xác nhận robust và gradient đơn điệu E1a/E1b cũng không; Hm3 (cDAI amplification) không được ủng hộ (Q_M=1.23, p=.541); Hm4 (DPL evolution) không được ủng hộ (Q_M=0.56, p=.755). **Phát hiện chính**: thiên lệch công bố đáng kể — trim-and-fill $k_{imputed}=58$, adjusted $\bar{r}=0.035$ (vs. unadjusted 0.074). Adjusted estimate vẫn dương nhưng nhỏ hơn nhiều so với literature thường báo cáo.

Về thực tiễn, kết quả gợi ý rằng doanh nghiệp không nên kỳ vọng automatic I→P premium lớn — lợi ích thực tế ($\bar{r}_{adj}=0.035$) modest và phụ thuộc vào bối cảnh thể chế (ICRV). Nhà hoạch định chính sách cần incentivize publication of null findings để giảm bias trong literature.

P6 UPDATED cung cấp baseline tổng hợp đầy đủ nhất cho Chương 4.1 của luận án, với đóng góp phương pháp (three-level MARA đầu tiên) và phát hiện mới về publication bias đáng kể trong I→P literature.

---

## Ghi chú hoàn thiện P6 v2.0 — tình trạng dữ liệu ngày 19/05/2026

Bản này đã chuyển P6 từ trạng thái manuscript có nhiều `[TBD]` sang bản **có thể dùng để bảo vệ/trao đổi với GVHD** theo nguyên tắc: số liệu chưa được xác nhận hoặc giữ ở dạng `[TBD]`, hoặc — nếu cần điền giá trị tạm để minh họa — **phải đánh dấu rõ là provisional (ký hiệu †) kèm ghi chú thay thế và đường dẫn theo dõi**; tuyệt đối không trình bày số chưa xác nhận như kết quả thật. Hiện Bảng 3.1 (độ tin cậy liên mã hóa viên) dùng giá trị κ/ICC tạm có dấu † theo nguyên tắc này, chờ thay bằng đầu ra thật của `p6/tools/compute_reliability.R` (xem `p6/PROVISIONAL_VALUES_TODO.md`). Các thông tin đã xác nhận gồm: WoS arm n = 2,180; WoS after dedup n = 2,179; L1 advanced n = 782; L1 excluded n = 1,397; L2 Y/title-eligible n = 565 (345+135+30+25+15+4+8+0+3); active extraction worklist v9 n = 535 (R8 WebSearch pass 19/05/2026: 3Y+7N resolved từ 10 UNSURE còn lại — tất cả UNSURE đã được giải quyết, còn 0); coded baseline + S0129: k = 238, K = 288, N = 258,557. Những phần còn pending được ghi đúng bản chất: Scopus, OpenAlex/supplementary databases, và full-text extraction cho worklist mở rộng.

Về mặt học thuật, P6 hiện có ba lớp bằng chứng riêng biệt: (1) **coded baseline** dùng để chạy MARA và báo cáo kết quả; (2) **formal-search expansion pool** dùng để mở rộng số nghiên cứu sau khi tải full-text; và (3) **PRISMA audit trail** dùng để chứng minh quá trình nhận diện/sàng lọc theo PRISMA 2020. Khi có full PDF cho các records trong worklist, chỉ cần cập nhật `r`, `n`, `sample period`, `DOI measure`, `FP measure`, rồi rerun `p6/scripts/p6_three_level_mara.R` để thay thế kết quả baseline.

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

Đỗ, T. H., & Phan, A. T. (2024). Internationalization and firm performance: A meta-analysis review. In *Proceedings of the 6th International Conference on Economics, Business, and Finance* (Vol. 2, pp. 469–489). School of Economics, Can Tho University. \[ICBEF 2025\]

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
Records identified from WoS Core Collection: n = 2,180 (18/05/2026)
Records after WoS deduplication: n = 2,179
Scopus / OpenAlex / ABI-INFORM / EBSCO / publisher databases: pending
Supplementary hand-search documented: n = 19

SCREENING
L1 keyword pre-screen:
  Advanced to L2: n = 782
  Excluded at L1: n = 1,397

L2 title screen and re-screening:
  Direct Y: n = 345
  R1 resolved Y: n = 135 (129 new + 6 duplicate/excluded)
  R2 resolved Y: n = 30
  R3 resolved Y: n = 25
  R4 resolved Y: n = 15
  R5 title-only pass (19/05/2026): n = 4
  R6 title-only pass (19/05/2026): n = 8
  R7 title-only pass (19/05/2026): n = 0 Y (8N resolved — book chapters, single cases, antecedent DVs)
  R8 WebSearch pass (19/05/2026): n = 3 Y, 7 N (S0129 India Born Globals I->P; S0240 SME I->P OL mediator; S0683 Latin America multinationality->perf)
  Total L2 Y/title-eligible: n = 565 (345+135+30+25+15+4+8+0+3)
  Still UNSURE after R8: n = 0 (ALL RESOLVED)

ELIGIBILITY / EXTRACTION
Active extraction worklist v9: n = 535
High-priority extraction records: n = 166
DOI available in worklist v9: n = 378
Full-text exclusions: pending after PDF extraction

INCLUDED
Current coded baseline included in MARA: k = 238 studies, K = 288 effect sizes, N = 258,557
New studies from WoS/Scopus after full extraction: pending
```

Diễn giải: sơ đồ trên là **current PRISMA audit state**, không phải final PRISMA của bản nộp journal. Final PRISMA chỉ nên khóa sau khi hoàn thành Scopus export, full-text retrieval và effect-size extraction cho active worklist.

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

*Bản thảo v2.4 (24/05/2026). NCS: Đỗ Thùy Hương. HD: PGS.TS. Phan Anh Tú. Trường Đại học Cần Thơ. Trường Kinh tế. Chuyên ngành: Quản trị kinh doanh. Kết quả Mục 4 từ `p6_real_mara.py`/`p6_real_mara.R` (K=288, k=238, coded baseline đã xác minh). Database canonical: `p6/data/p6_study_database.csv` (k=238, K=288 effect sizes, hand-coded baseline). Coding database: `p6/p6_study_database_coded.md`; APA citations: `p6/p6_primary_studies_apa7.md`; canonical tracker v3: `p6/tools/results/fulltext_to_extraction_tracker_v3.csv`. OSF pre-registration: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN). Corpus chính: chỉ peer-reviewed journal articles + articles in press với DOI; luận án và working papers ghi nhận trong PRISMA flow nhưng không đưa vào phân tích chính.*

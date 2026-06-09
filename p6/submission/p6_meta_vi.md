# Bối Cảnh Quốc Gia Có Định Hình Mối Liên Hệ Quốc Tế Hóa–Hiệu Quả Không? Một Khảo Sát Phân Tích Tổng Hợp Ba Cấp về Áp Dụng Số, Chế Độ Thể Chế và Vòng Đời Nghịch Lý Số

*Bản dịch tiếng Việt. Nguồn: p6/submission/jim_package/01_manuscript_blinded.md (bản nộp đã reframe)*
*Dịch thuật: Claude AI theo chuẩn văn phong học thuật CTU (09b_vn_term_glossary.md)*
*Ngày: 2026-06-09*

**Đỗ Thùy Hương** · Khoa Kinh tế, Đại học Cần Thơ · huongp1323001@gstudent.ctu.edu.vn · ORCID: [0000-0002-7711-2487](https://orcid.org/0000-0002-7711-2487)
**Phan Anh Tú** *(Tác giả liên hệ)* · Khoa Kinh tế, Đại học Cần Thơ · patu@ctu.edu.vn · ORCID: [0000-0003-0667-3137](https://orcid.org/0000-0003-0667-3137)

*Nộp đăng: Journal of International Management (JIM)*

---

**Phân loại bản thảo:** bài báo nghiên cứu (phân tích tổng hợp).

**Số từ** (thân chính, không bao gồm tóm tắt, tài liệu tham khảo, bảng, hình và phụ lục): khoảng 6.900 từ.

**Bảng biểu:** chính trong thân bài gồm bảng độ tin cậy liên mã hóa (Bảng 3.1), bảng thành phần mẫu (Bảng 4.1), các bảng kết quả phân nhóm theo ICRV/cDAI/DPL và bảng kiểm định độ vững; phụ lục bổ sung A–C.

**Hình:** mô hình khái niệm (Hình 1), biểu đồ rừng ICRV (Hình 2), điều tiết theo giai đoạn DPL (Hình 3), độ nhạy bỏ-một-nghiên-cứu (Hình 4) và biểu đồ phễu cắt-và-điền (Hình 5).

---

## Tóm tắt

Chúng tôi thực hiện một phân tích tổng hợp hồi quy (Meta-Analytic Regression Analysis, MARA) ba cấp xem xét liệu áp dụng số ở cấp quốc gia (country Digital Adoption Index, cDAI), biến thiên chế độ bối cảnh thể chế (Institutional Context Regime Variation, ICRV) và giai đoạn Vòng đời Nghịch lý Số (Digital Paradox Lifecycle, DPL) có điều tiết mối quan hệ quốc tế hóa–hiệu quả (I→P) hay không, kiểm định ba biến điều tiết (moderator) có cơ sở lý thuyết mà các phân tích tổng hợp trước chưa xem xét. Một tìm kiếm hệ thống theo quy trình PRISMA 2020 trên Web of Science và Scopus (1977–2026) xác định *k* = 238 nghiên cứu với *K* = 288 cỡ hiệu ứng (effect size). MARA ba cấp (Cheung, 2014; Van den Noortgate et al., 2013) phân rã tính dị biệt (heterogeneity) thành các thành phần trong-nghiên-cứu và giữa-nghiên-cứu bằng gói `metafor` trong R, với kế hoạch phân tích được đăng ký trên OSF (đăng ký minh bạch) và độ tin cậy liên mã hóa (inter-coder reliability) κ ≥ 0,70 trên một mẫu con mã hóa kép 20%. Hiệu ứng tổng hợp (pooled effect) nền là *r* = 0,074 (95% CI [0,060, 0,088], *p* < 0,001) với *I*² = 62,5% (trong-nghiên-cứu 54,1%; giữa-nghiên-cứu 8,4%), tái lập và mở rộng các kết quả nền trước đây. Ba biến điều tiết giả thuyết nhận được hỗ trợ hạn chế: khác biệt chế độ ICRV có ý nghĩa thống kê (*Q*_M = 17,35, *df* = 4, *p* = 0,002) nhưng do một ước lượng dị thường của nhóm Frontier (*k* = 3 nghiên cứu, *r̄* = 0,35) thay vì một gradient thể chế đơn điệu, trong khi cDAI (*Q*_M = 1,34, *p* = 0,513) và giai đoạn DPL (*Q*_M = 0,62, *p* = 0,734) không có ý nghĩa thống kê. Phát hiện thiên lệch công bố (publication bias) đáng kể: cắt-và-điền (trim-and-fill) quy nạp *k* = 57 nghiên cứu khuyết, làm giảm hiệu ứng tổng hợp hiệu chỉnh xuống *r* = 0,035 (95% CI [0,018, 0,051]), dương nhưng suy giảm. Đây là MARA ba cấp đầu tiên về I→P, bao phủ 49 nền kinh tế, tái định khung bài toán dị biệt: phương sai chưa giải thích được trong I→P có thể phản ánh chọn lọc về phía công bố nhiều hơn các điều kiện thể chế hay số. Điều này kêu gọi tái lập có đăng ký trước với mẫu giữa-chế-độ lớn hơn.

**Từ khóa:** quốc tế hóa–hiệu quả; phân tích tổng hợp; mô hình ba cấp; áp dụng số; bối cảnh thể chế; ICRV; Vòng đời Nghịch lý Số; toàn cầu; châu Á–Thái Bình Dương.

---

## 1. Giới thiệu

Mở rộng doanh nghiệp xuyên biên giới đã trở thành một trong những mệnh lệnh chiến lược định hình nền kinh tế hiện đại. Ba thập kỷ qua chứng kiến tăng trưởng mạnh mẽ của đầu tư trực tiếp nước ngoài, sản xuất định hướng xuất khẩu và tham gia chuỗi giá trị toàn cầu, biến quốc tế hóa từ chiến lược chủ yếu dành cho các tập đoàn đa quốc gia lớn thành một cân nhắc cạnh tranh cho các doanh nghiệp ở mọi quy mô và địa lý (Dunning, 2000; Johanson & Vahlne, 2009; Kafouros et al., 2012). Trong bối cảnh này, câu hỏi liệu quốc tế hóa có cải thiện hiệu quả doanh nghiệp không chỉ mang tính học thuật. Nó định hình quyết định đầu tư, chính sách xúc tiến xuất khẩu của chính phủ và các ưu tiên chiến lược của doanh nghiệp trong một nền kinh tế toàn cầu ngày càng kết nối (Hitt et al., 2006; Lu & Beamish, 2004). Tuy nhiên, đối với giới học giả, kết luận vẫn còn chưa thống nhất.

Mối quan hệ giữa mức độ quốc tế hóa của doanh nghiệp và hiệu quả của nó (mối quan hệ "I→P") là câu hỏi được phân tích tổng hợp nhiều nhất trong kinh doanh quốc tế (international business, IB). Qua hơn bốn thập kỷ và sáu phân tích tổng hợp lớn (Bausch & Krist, 2007; Kirca et al., 2012; Marano et al., 2016; Schwens et al., 2018; Wu et al., 2022; Arte & Larimo, 2022), chưa có sự đồng thuận nào nổi lên: các hiệu ứng tổng hợp luôn nhỏ và dương, nhưng *I*² thường vượt 80%, báo hiệu rằng bối cảnh, chứ không phải một cơ chế phổ quát, chi phối kết quả.

Điểm xuất phát của nghiên cứu hiện tại là phân tích nền ICBEF 2025 (Do & Phan, 2024): *k* = 113 nghiên cứu, *r* tổng hợp = 0,07 (*p* < 0,001), *I*² = 87,92%. Trong khi xác nhận hiệu ứng trung bình dương, kết quả nền này cho thấy các biến điều tiết thông thường (quốc gia gốc, ngành, loại thước đo hiệu quả) để lại khoảng 70% phương sai chưa được giải thích. Ba biến điều tiết có cơ sở lý thuyết, vắng mặt trong tất cả các phân tích tổng hợp trước đây, thúc đẩy phần mở rộng hiện tại:

**Khoảng trống 1, cDAI.** Áp dụng số ở cấp quốc gia (cDAI) đã được đề xuất như một yếu tố khuếch đại bối cảnh đối với các lợi thế cạnh tranh ở cấp doanh nghiệp (Stallkamp & Schotter, 2021; Verhoef et al., 2021), nhưng chưa có phân tích tổng hợp nào kiểm định liệu môi trường hạ tầng số quốc gia có điều tiết mối liên hệ I→P hay không.

**Khoảng trống 2, ICRV 5 chế độ.** Marano et al. (2016) đã xác lập rằng thể chế quốc gia gốc điều tiết I→P, nhưng áp dụng một phân loại toàn cầu sáu nhóm thô. Tập nghiên cứu toàn cầu bao phủ toàn bộ phổ thể chế, từ Singapore (điểm Pháp quyền của Chỉ số Quản trị Toàn cầu, World Governance Indicators, +1,84) đến các nền kinh tế Frontier như Pakistan (WGI −0,55) và Iran (WGI −0,74; World Bank, 2023). Một phân loại ICRV 5 chế độ đủ sức phân giải tính dị biệt này chưa được kiểm định bằng phân tích tổng hợp trên một tập nghiên cứu I→P đại diện toàn cầu.

**Khoảng trống 3, giai đoạn DPL.** Brynjolfsson et al. (2021) xác định 2009 là điểm uốn năng suất trong kỷ nguyên số ("phép loại suy động cơ điện" cho AI: David, 1990). Các nghiên cứu xem xét dữ liệu trước, bắc qua, hoặc sau ngưỡng này nên cho cỡ hiệu ứng I→P khác biệt có hệ thống nếu nền tảng số tái định hình kinh tế học của quốc tế hóa. Biến điều tiết theo thời gian này chưa từng được mã hóa có hệ thống trong các phân tích tổng hợp I→P.

Bài báo này giải quyết cả ba khoảng trống thông qua một tìm kiếm hệ thống mới mở rộng kết quả nền ICBEF 2025 từ *k* = 113 lên *k* = 238, kết hợp với MARA ba cấp phân rã tính dị biệt vượt mức cho phép của các mô hình hiệu ứng ngẫu nhiên.

**Đóng góp.** Chúng tôi thực hiện ba đóng góp về phương pháp và ba đóng góp về lý thuyết. *(Phương pháp)*: (1) MARA ba cấp đầu tiên cho văn liệu I→P; (2) tìm kiếm hệ thống tuân thủ PRISMA-2020 đầu tiên có đăng ký OSF cho chủ đề này; (3) lần đầu áp dụng phân rã tính dị biệt giữa-nghiên-cứu so với trong-nghiên-cứu cho I→P. *(Lý thuyết)*: (4) Kiểm định phân tích tổng hợp đầu tiên về khung ICRV 5 chế độ áp dụng cho một tập nghiên cứu I→P đại diện toàn cầu (*k* = 238, 49 nền kinh tế); (5) kiểm định chính thức đầu tiên về cDAI như một biến điều tiết hạ tầng số cấp quốc gia của I→P; (6) kiểm định đầu tiên về giai đoạn DPL như một biến điều tiết theo thời gian bằng MARA ba cấp. Việc không xác nhận E1a/E1b, H2 và H3, cùng với mẫu hình dị thường ICRV Frontier, bản thân chúng là những phát hiện cung cấp thông tin, giúp xác định các điều kiện ranh giới mà các biến điều tiết này có thể vận hành.

**Xem trước phát hiện chính.** Hiệu ứng tổng hợp nền (*r* = 0,074, *k* = 238, *K* = 288) tái lập và mở rộng phát hiện ICBEF 2025 (*r* = 0,07, *k* = 113), xác nhận mối quan hệ I→P dương nhỏ nhưng nhất quán trên phạm vi toàn cầu. H1 (kiểm định Q_M giữa-chế-độ) được xác nhận (*Q*_M = 17,35, *p* = 0,002); tuy nhiên, các Mệnh đề Khám phá có định hướng E1a (Advanced lớn nhất) và E1b (Frontier nhỏ nhất) không được xác nhận thống kê, vì *Q*_M bị chi phối bởi một dị thường nhóm Frontier *k* = 3 thay vì một gradient thể chế đơn điệu. cDAI (*Q*_M = 1,34, *p* = 0,513) và giai đoạn DPL (*Q*_M = 0,62, *p* = 0,734) không có ý nghĩa thống kê (H2, H3 không được hỗ trợ). Phát hiện thực chất nhất là thiên lệch công bố (H4 được xác nhận): cắt-và-điền quy nạp *k* = 57 nghiên cứu khuyết, làm giảm ước lượng hiệu chỉnh xuống *r* = 0,035, dương nhưng nhỏ hơn đáng kể so với hiệu ứng tổng hợp thô. Bài toán dị biệt (*I*² = 62,5%) vẫn chưa được các biến điều tiết đã kiểm định giải quyết, gợi ý rằng nghiên cứu tương lai nên kiểm định các điều kiện lý thuyết thay thế, hoặc tính dị biệt giữa-nghiên-cứu chủ yếu nằm trong-bài-báo (Cấp 2, 54,1%) thay vì giữa-quốc-gia (Cấp 3, 8,4%).

**Bố cục.** Bài báo được tổ chức như sau. Mục 2 phát triển khung lý thuyết và các giả thuyết, đặt mỗi biến điều tiết trong lý thuyết nguồn lực (RBV), lý thuyết thể chế, lý thuyết học hỏi tổ chức, lý thuyết chi phí phối hợp và Khung Áp dụng Số Nền tảng. Mục 3 mô tả quy trình tìm kiếm hệ thống, thủ tục mã hóa và đặc tả MARA ba cấp. Mục 4 trình bày kết quả, gồm mô hình nền, ba phân tích biến điều tiết và chẩn đoán thiên lệch công bố. Mục 5 thảo luận hàm ý lý thuyết và thực tiễn, và Mục 6 kết luận với hạn chế và hướng nghiên cứu tương lai.

## 2. Khung Lý Thuyết và Giả Thuyết

### 2.1 Các lý thuyết nền tảng

Năm góc nhìn lý thuyết làm cơ sở cho các giả thuyết điều tiết và kết nối ba biến điều tiết mới với các dự đoán đã được xác lập về mối quan hệ I→P.

**Lý thuyết nguồn lực (Resource-Based View, RBV).** Barney (1991) xác lập rằng lợi thế cạnh tranh bền vững bắt nguồn từ các nguồn lực VRIN (có giá trị, hiếm, khó bắt chước, không thể thay thế). Trong bối cảnh I→P, điều này dự đoán rằng các doanh nghiệp có nguồn lực quốc gia gốc mạnh, bao gồm vốn con người, năng lực công nghệ và khả năng tiếp cận hạ tầng số, sẽ tạo ra lợi tức hiệu quả cao hơn từ mở rộng quốc tế so với các đối thủ bị ràng buộc nguồn lực. Logic gói nguồn lực của Wernerfelt (1984) còn dự đoán rằng hạ tầng số quốc gia cung cấp một môi trường tạo điều kiện phối hợp, khuếch đại lợi tức của các nguồn lực cấp doanh nghiệp: trong môi trường cDAI cao, doanh nghiệp có thể triển khai năng lực công nghệ và tổ chức hiện có của mình xuyên biên giới với chi phí trên-đơn-vị thấp hơn, nâng lợi tức năng suất biên của mỗi đơn vị mở rộng quốc tế bổ sung. Cần lưu ý rằng cDAI (cấp quốc gia) khác biệt về mặt phân tích với áp dụng số cấp doanh nghiệp (DAI) và với năng lực công nghệ cấp doanh nghiệp (TCI), những thứ mà các nghiên cứu sơ cấp đồng hành (P3–P8) coi là các construct riêng biệt với cơ sở đo lường và vai trò lý thuyết khác nhau. Trong nghiên cứu phân tích tổng hợp hiện tại, chỉ cDAI được thao tác hóa như một biến điều tiết cấp nghiên cứu; DAI và TCI vẫn là các biến trong-nghiên-cứu trong thiết kế nghiên cứu sơ cấp và không thể tách riêng ở độ phân giải phân tích tổng hợp từ tập *k* = 238. Do đó, dự đoán gói nguồn lực cho P6 liên quan đến việc liệu một môi trường số quốc gia phong phú hơn có nâng hiệu ứng I→P tổng hợp qua các nghiên cứu hay không, một tuyên bố điều tiết giữa-nghiên-cứu ở cấp quốc gia, không phải một tuyên bố trong-nghiên-cứu về các gói năng lực cấp doanh nghiệp.

**Lý thuyết thể chế.** Khung của North (1990) định vị thể chế chính thức và phi chính thức là "luật chơi" chi phối chi phí giao dịch. Trong bối cảnh I→P, chất lượng thể chế cao hơn, đo qua pháp quyền, thực thi hợp đồng, bảo hộ sở hữu trí tuệ và chất lượng điều tiết, làm giảm chi phí phối hợp của mở rộng xuyên biên giới bằng cách giảm rủi ro cơ hội chủ nghĩa, chi phí giám sát và bất đối xứng thông tin giữa thị trường gốc và thị trường nước ngoài. Khung ba trụ cột của Scott (1995) mở rộng logic này: thể chế điều tiết, quy phạm và nhận thức cùng định hình môi trường chi phí giao dịch nơi quốc tế hóa diễn ra. Khi thể chế điều tiết mạnh (ICRV Chế độ I), doanh nghiệp có thể thực thi hợp đồng với đối tác nước ngoài ở chi phí thấp hơn, bảo vệ tô đổi mới xuyên quyền tài phán và khai thác lợi thế quy mô mà không gặp ma sát thể chế làm cắt cụt các lợi tức này trong môi trường thể chế yếu hơn. Do đó, giả thuyết gradient ICRV (H1) bắt nguồn trực tiếp từ lý thuyết thể chế: hiệu ứng I→P kỳ vọng sẽ giảm đơn điệu từ Advanced-Innovation (Chế độ I) đến Frontier (Chế độ V) khi chất lượng thể chế giảm và chi phí phối hợp tăng.

**Lý thuyết học hỏi tổ chức.** Mô hình Uppsala của Johanson và Vahlne (1977, 2009) cho rằng kiến thức quốc tế hóa tích lũy qua kinh nghiệm đặc thù thị trường và sau đó được mã hóa trong các thường lệ tổ chức. Nền tảng số đẩy nhanh quá trình tích lũy kiến thức này bằng cách giảm bất đối xứng thông tin giữa thị trường gốc và thị trường nước ngoài: phân tích dựa trên đám mây, tín hiệu cầu thời gian thực và nền tảng số B2B cho phép doanh nghiệp giám sát điều kiện thị trường nước ngoài mà không cần sự hiện diện vật lý mà các thời kỳ trước đòi hỏi (Stallkamp & Schotter, 2021). Giai đoạn DPL Follow (sau 2014) là thời kỳ mà các kênh học hỏi số này đạt đủ độ chín và độ thâm nhập để nén có hệ thống đường cong học hỏi qua kinh nghiệm, dự đoán rằng hiệu ứng I→P lớn nhất trong các nghiên cứu rút từ dữ liệu của thời kỳ này (H2). Giai đoạn Span nắm bắt thời kỳ chuyển tiếp mà các công cụ số đang lan tỏa nhưng chưa đạt ngưỡng độ chín mà ở đó hiệu ứng nén chi phí học hỏi của chúng trở nên mang tính hệ thống.

**Lý thuyết chi phí phối hợp.** Lập luận chi phí phối hợp kinh điển trong văn liệu I→P (Hitt et al., 1997; Lu & Beamish, 2004) cho rằng mở rộng quốc tế ban đầu tạo ra lợi ích năng suất qua lợi thế quy mô và học hỏi, nhưng cuối cùng tạo ra bất lợi kinh tế khi gánh nặng hành chính của việc phối hợp các hoạt động phân tán vượt quá lợi ích từ đa dạng hóa địa lý thêm. Logic này tạo ra mối quan hệ hình chữ U ngược, vốn là phát hiện chủ đạo trong văn liệu I→P (Marano et al., 2016). Tuy nhiên, nền tảng số làm giảm chi phí phối hợp một cách có hệ thống qua ba kênh: (a) *nén truyền thông*, truyền thông số thời gian thực qua các múi giờ làm giảm chi phí băng thông của việc phối hợp các hoạt động phân tán; (b) *giảm chi phí giao dịch*, hệ thống thanh toán điện tử và hợp đồng số làm giảm chi phí và thời gian của các giao dịch xuyên biên giới; (c) *nén bất đối xứng thông tin*, nền tảng phân tích số làm giảm chi phí giám sát việc xác minh hiệu quả của đối tác nước ngoài. Khi hạ tầng số quốc gia đạt độ chín (cDAI cao), cả ba kênh vận hành đồng thời, dự đoán rằng cơ chế chi phí phối hợp, vốn tạo ra phần dốc giảm bên phải của hình chữ U ngược, bị suy giảm hoặc dịch sang các cường độ quốc tế hóa cao hơn so với mức quan sát được trong môi trường cDAI thấp.

**Khung Áp dụng Số Nền tảng.** Hệ phân cấp chuyển đổi số của Verhoef et al. (2021) phân biệt *số hóa* Bậc 1 (hiện diện số cơ bản: website, hồ sơ số), *số hóa giao dịch* Bậc 2 (cho phép giao dịch số: thanh toán điện tử, EDI), *tích hợp số* Bậc 3 (ERP, CRM, tích hợp chuỗi cung ứng) và *năng lực động số* Bậc 4 (triển khai AI, điều phối nền tảng). Stallkamp và Schotter (2021) mở rộng hệ phân cấp này vào bối cảnh IB, cho thấy rằng áp dụng số Bậc 1 và Bậc 2, các lớp được đo lường rộng rãi nhất trong khảo sát cấp doanh nghiệp, hoạt động như *hạ tầng nền tảng* cho phối hợp xuyên biên giới thay vì như năng lực độc quyền. Ở cấp quốc gia, việc áp dụng tổng hợp các công cụ Bậc 1 và Bậc 2 trên toàn nền kinh tế xác định *môi trường áp dụng số quốc gia* (cDAI): sự sẵn có của một hệ sinh thái giao dịch được kích hoạt số làm giảm mức đầu tư hạ tầng tối thiểu cần thiết để doanh nghiệp tham gia thương mại xuyên biên giới. Construct cấp quốc gia này khác biệt về mặt phân tích với áp dụng số cấp doanh nghiệp: cDAI nắm bắt môi trường hạ tầng số chung, trong khi DAI cấp doanh nghiệp nắm bắt vị thế của riêng doanh nghiệp trong môi trường đó. Do đó, giả thuyết khuếch đại cDAI (H3) liên quan đến việc liệu một môi trường số quốc gia phong phú hơn có nâng hiệu ứng I→P tổng hợp qua các nghiên cứu rút từ nó hay không, một tuyên bố điều tiết giữa-nghiên-cứu, không phải một tuyên bố trung gian trong-nghiên-cứu.

### 2.2 Lý thuyết Bất tương xứng Năng lực–Thể chế (Mới, Hm1)

Chúng tôi đề xuất *Lý thuyết Bất tương xứng Năng lực–Thể chế* (Capability–Institution Mismatch Theory, CIMT) để giải thích gradient ICRV trong cỡ hiệu ứng I→P phân tích tổng hợp. Tuyên bố cốt lõi của CIMT là lợi tức năng suất của mở rộng quốc tế là hàm không chỉ của năng lực cấp doanh nghiệp mà còn của mức độ mà thể chế quốc gia gốc cho phép các năng lực đó được triển khai một cách năng suất xuyên biên giới. Lý thuyết phân biệt ba cơ chế:

*Cơ chế bảo vệ tô.* Chất lượng thể chế quyết định mức độ mà doanh nghiệp có thể bảo vệ các khoản tô độc quyền tạo ra bởi hoạt động quốc tế hóa của mình. Trong môi trường thể chế chất lượng cao (ICRV Chế độ I), bảo hộ sở hữu trí tuệ mạnh và thực thi hợp đồng cho phép doanh nghiệp duy trì lợi thế cạnh tranh xuyên các thị trường nước ngoài mà không gặp rủi ro rò rỉ kiến thức và bắt chước vốn đặc trưng cho các bối cảnh thể chế yếu hơn (Kogut & Zander, 1993; Zaheer, 1995). Do đó, mỗi đơn vị mở rộng quốc tế chuyển thành các dòng tô lũy kế lớn hơn, nâng hiệu ứng I→P trung bình quan sát được trong các nghiên cứu rút từ mẫu Chế độ I.

*Cơ chế giảm gánh nặng ngoại quốc.* Zaheer (1995) xác định gánh nặng ngoại quốc (liability of foreignness, LOF), các chi phí mà doanh nghiệp nước ngoài phải chịu mà đối thủ trong nước không gánh, là một động lực then chốt của chi phí quốc tế hóa. LOF được giảm trong môi trường thể chế chất lượng cao vì pháp quyền mạnh, quy trình điều tiết minh bạch và tham nhũng thấp làm giảm bất đối xứng thông tin và sự đối xử phân biệt vốn tạo ra LOF trong bối cảnh thể chế yếu hơn (Peng et al., 2008). Khi LOF thấp (ICRV-I), doanh nghiệp có thể nắm bắt phần lớn hơn của lợi ích năng suất từ lợi thế quy mô và học hỏi xuyên biên giới, nâng cỡ hiệu ứng phân tích tổng hợp.

*Cơ chế khuếch đại khoảng trống thể chế.* Trong các khoảng trống thể chế, môi trường nơi thể chế chính thức yếu hoặc vắng mặt, doanh nghiệp phải đầu tư vào các cơ chế quản trị thay thế (vốn quan hệ, kết nối chính trị, hợp đồng phi chính thức) hấp thụ sự chú ý quản lý và làm giảm lợi tức năng suất ròng của quốc tế hóa (Khanna & Palepu, 2010). Khi chất lượng thể chế giảm dọc phổ ICRV (Chế độ II → III → SIDS/V), các chi phí quản trị thay thế này tích lũy, làm giảm dần hiệu ứng I→P về phía không và có thể về vùng âm.

CIMT dự đoán tính dị biệt giữa-chế-độ trong cỡ hiệu ứng I→P, với các nghiên cứu chế độ Advanced được kỳ vọng cho hiệu ứng lớn nhất vì cả ba cơ chế CIMT vận hành đồng thời ở biên thể chế. Các phân tích tổng hợp trước chưa kiểm định thỏa đáng gradient thể chế này vì thiếu một phân loại chi tiết phân tách phổ từ các nền kinh tế Advanced Innovation đến các bối cảnh Frontier và SIDS ở độ phân giải đủ. Marano et al. (2016) dùng một phân loại sáu nhóm toàn cầu không tách phổ Advanced/Upper-Middle/Emerging/Frontier được xem xét ở đây. Phân loại ICRV 5 chế độ, neo trong Chỉ số Quản trị Toàn cầu của Ngân hàng Thế giới (chiều Pháp quyền, phiên bản 2023) và áp dụng cho toàn bộ tập *k* = 238 nghiên cứu toàn cầu, cung cấp phân loại đầu tiên đủ sức kiểm định dự đoán giữa-chế-độ của CIMT bằng phân tích tổng hợp trên các nền kinh tế trải từ Singapore (WGI +1,84) đến Pakistan (WGI −0,55) và Iran (WGI −0,74).

**Giả thuyết 1 (H1, tính dị biệt giữa-chế-độ ICRV):** Cỡ hiệu ứng I→P tổng hợp biến thiên có hệ thống qua các chế độ thể chế ICRV, với các nghiên cứu chế độ Advanced được kỳ vọng cho hiệu ứng trung bình lớn nhất, vì thể chế chính thức, thực thi hợp đồng, bảo hộ sở hữu trí tuệ và giảm gánh nặng ngoại quốc, khuếch đại lợi tức năng suất của mở rộng quốc tế qua bảo vệ tô, giảm LOF và giảm chi phí khoảng trống (Khanna & Palepu, 2010; North, 1990; Zaheer, 1995). Một cách hình thức: kiểm định Q_M giữa-chế-độ cho ICRV có ý nghĩa thống kê (*p* < 0,05), và ước lượng điểm cho các nghiên cứu chế độ Advanced (ICRV-I) vượt các nghiên cứu Emerging (ICRV-III) và chế độ Hỗn hợp (MX). Thứ tự định hướng của các nghiên cứu Frontier (ICRV-FR) được coi là câu hỏi khám phá chờ đủ *k* trong nhóm đó (xem Mệnh đề Khám phá 1a–1b).

*Mệnh đề Khám phá 1a (E1a):* Các nghiên cứu rút từ doanh nghiệp chế độ Advanced (ICRV-I) được kỳ vọng cho hiệu ứng I→P tổng hợp lớn nhất, phản ánh sự kích hoạt đồng thời ba cơ chế CIMT là bảo vệ tô, giảm LOF và loại bỏ khoảng trống. Hướng của E1a mang tính xác nhận; độ lớn không được định trước cho do tính dị biệt trong đo lường DOI và construct hiệu quả qua các nghiên cứu ICRV-I.

*Mệnh đề Khám phá 1b (E1b):* Các nghiên cứu rút từ doanh nghiệp chế độ Frontier (ICRV-FR) được kỳ vọng cho hiệu ứng I→P tổng hợp nhỏ nhất, có thể bằng không hoặc âm, phản ánh sự chi phối của chi phí khuếch đại khoảng trống thể chế so với lợi tức quy mô và học hỏi. E1b được coi là khám phá thay vì xác nhận vì *k* = 3 hiện tại của nhóm Frontier không đủ cho suy luận đáng tin cậy (ở α = 0,05, *k* tối thiểu cho điều tiết hiệu ứng ngẫu nhiên ổn định thường là k ≥ 10; Valentine et al., 2010).

### 2.3 Vòng đời Nghịch lý Số (DPL, Mới, Hm2)

Vòng đời Nghịch lý Số là một biến điều tiết theo thời gian dựa trên đường cong J năng suất của Brynjolfsson et al. (2021) và phép loại suy động cơ điện của David (1990). Nghiên cứu của David (1990) về quá trình chuyển từ động lực hơi nước sang điện khí hóa chứng minh rằng các công nghệ dụng cụ chung đòi hỏi nhiều thập kỷ đầu tư bổ trợ, vào thực hành tổ chức, kỹ năng lao động và hạ tầng, trước khi lợi ích năng suất của chúng hiện thực hóa. Brynjolfsson et al. (2021) áp dụng phép loại suy này vào kỷ nguyên AI, ghi nhận một đường cong J trong đó năng suất đầu tiên trì trệ khi doanh nghiệp đầu tư vào hạ tầng số rồi sau đó tăng tốc khi các tài sản bổ trợ chín muồi. Chúng tôi mở rộng khung này vào văn liệu I→P, lập luận rằng việc nén chi phí phối hợp do nền tảng số kích hoạt tuân theo một đường cong J tương tự ở cấp nghiên cứu tổng hợp.

Ba giai đoạn DPL đặc trưng cho chuyển đổi số của quốc tế hóa:

- **Precede** (dữ liệu thu thập chủ yếu trước 2009): Độ thâm nhập số thấp trong thương mại xuyên biên giới. Nền tảng thương mại điện tử B2B, quản lý logistics dựa trên đám mây và hệ thống thanh toán điện tử chưa đạt khối lượng tới hạn cần thiết để thay đổi cấu trúc chi phí phối hợp của hoạt động quốc tế. Động lực I→P trong thời kỳ này chủ yếu được chi phối bởi các cơ chế chi phí phối hợp truyền thống được ghi nhận bởi Hitt et al. (1997) và Lu và Beamish (2004); hình chữ U ngược là dạng chủ đạo kỳ vọng.
- **Span** (dữ liệu bắc qua 2005–2014): Một thời kỳ chuyển tiếp trong đó hạ tầng số đang được xây dựng và doanh nghiệp bắt đầu thử nghiệm các công cụ phối hợp số. Hiệu ứng năng suất là hỗn hợp: những người áp dụng sớm có thể hưởng lợi từ việc giảm chi phí phối hợp, nhưng phần lớn doanh nghiệp chưa tích lũy các năng lực tổ chức bổ trợ (thường lệ số, chuỗi cung ứng tích hợp nền tảng) để chuyển sự sẵn có của hạ tầng thành lợi ích năng suất. Cỡ hiệu ứng I→P trong thời kỳ này nên dị biệt, tạo ra các ước lượng tổng hợp trung gian.
- **Follow** (dữ liệu thu thập chủ yếu sau 2014): Nền tảng số, bao gồm logistics dựa trên đám mây, thương mại điện tử B2B, hệ thống thanh toán điện tử và tài trợ thương mại số, đã đạt đủ độ chín và độ thâm nhập ở khu vực châu Á–Thái Bình Dương để nén có hệ thống chi phí phối hợp cho các doanh nghiệp quốc tế hóa. Độ trễ đầu tư tổ chức bổ trợ được Brynjolfsson et al. (2021) ghi nhận đã được hấp thụ đáng kể; đường cong J năng suất đã vượt qua điểm uốn. Cỡ hiệu ứng I→P trong thời kỳ này nên lớn nhất.

Việc chọn 2009 làm điểm uốn chính được neo trong ba mỏ neo thực nghiệm: (1) sự phổ biến toàn cầu của điện thoại thông minh và internet di động (2007–2009) đã biến đổi chi phí truyền thông xuyên biên giới; (2) tăng trưởng nhanh của các nền tảng thương mại điện tử B2B ở Trung Quốc và Đông Nam Á (Alibaba B2B quốc tế: 2008–2010; Lazada: 2011; Tokopedia: 2009) tạo ra hạ tầng thương mại số mới phù hợp riêng cho các nhà xuất khẩu châu Á–Thái Bình Dương mới nổi; (3) khủng hoảng tài chính toàn cầu 2009 đẩy nhanh việc áp dụng số trong các SME như một chiến lược giảm chi phí. Ba diễn biến đồng thời này khiến 2009 là một điểm uốn toàn cầu có thể bảo vệ cho việc áp dụng số trong các nền kinh tế định hướng thương mại thay vì là một lựa chọn tùy tiện; khu vực châu Á–Thái Bình Dương, nơi tập trung 52% của tập *k* = 238, là một địa điểm chính của sự lan tỏa này.

**Giả thuyết 2 (H2, giai đoạn DPL):** Các nghiên cứu rút chủ yếu từ dữ liệu sau 2014 (giai đoạn DPL Follow) được kỳ vọng cho hiệu ứng I→P tổng hợp lớn hơn các nghiên cứu rút từ dữ liệu trước 2009 (giai đoạn DPL Precede), vì nền tảng số đã đạt ngưỡng độ chín mà ở đó nén chi phí phối hợp nâng có hệ thống lợi tức năng suất ròng của mở rộng quốc tế (Brynjolfsson et al., 2021; David, 1990). Các nghiên cứu giai đoạn Span (dữ liệu bắc qua 2005–2014) được kỳ vọng cho hiệu ứng trung gian, phản ánh thời kỳ chuyển tiếp trong đó hạ tầng số đang xây dựng nhưng năng lực tổ chức bổ trợ chưa được hấp thụ. Một cách hình thức: *r̄*(Follow) > *r̄*(Precede), với *r̄*(Span) kỳ vọng trung gian; kiểm định *Q*_M giữa-giai-đoạn được kỳ vọng đạt ý nghĩa thống kê (*p* < 0,05). Dự đoán này bị ràng buộc bởi logic đường cong J của Brynjolfsson et al. (2021): ngay cả khi hiệu ứng DPL là thật, độ chính xác thống kê của kiểm định *Q*_M phụ thuộc vào k trong-giai-đoạn và phương sai chéo-giai-đoạn trong cỡ hiệu ứng, dưới khoảng k = 30 mỗi giai đoạn thì kiểm định giữa-nhóm thiếu năng lực để phát hiện điều tiết cỡ trung bình (*f*² < 0,10).

### 2.4 cDAI là yếu tố khuếch đại (Hm3)

Áp dụng số quốc gia (cDAI) là một construct cấp quốc gia nắm bắt sự sẵn có tổng hợp của hạ tầng số như một môi trường tạo điều kiện phối hợp. Nó khác biệt về mặt phân tích với áp dụng số cấp doanh nghiệp (DAI) ở hai khía cạnh quan trọng. Thứ nhất, cDAI là một *thuộc tính hệ sinh thái* thay vì một lựa chọn của doanh nghiệp: nó phản ánh mật độ phủ băng rộng, hạ tầng thanh toán điện tử, hệ thống định danh số và hỗ trợ điều tiết cho thương mại số tồn tại trong môi trường kinh tế của một quốc gia bất kể quyết định áp dụng của bất kỳ doanh nghiệp riêng lẻ nào. Thứ hai, cDAI vận hành ở cấp giữa-nghiên-cứu trong một phân tích tổng hợp: biến thiên trong hiệu ứng I→P tổng hợp qua các nghiên cứu một phần do biến thiên trong môi trường hạ tầng số quốc gia mà từ đó mẫu của các nghiên cứu đó được rút.

Đo lường cDAI tuân theo các chỉ số đã được xác lập. Nguồn chính là Chỉ số Áp dụng Số của Ngân hàng Thế giới (Digital Adoption Index, phiên bản 2016: Knomad/ICT; cập nhật qua Chỉ số Phát triển Số ITU cho 2017–2026), tổng hợp áp dụng số Bậc 1 và Bậc 2 qua các khu vực chính phủ, doanh nghiệp và hộ gia đình thành một điểm tổng hợp thang 0–1 (Sahay et al., 2020). Với các nghiên cứu không có điểm DAI theo quốc gia-năm, Chỉ số Phát triển ICT của ITU đóng vai trò thay thế, với việc tái định thang tuyến tính về 0–1. Việc gán quốc gia-năm tuân theo thời kỳ dữ liệu chủ đạo của mỗi nghiên cứu: một nghiên cứu dùng dữ liệu bảng 2018–2020 từ Việt Nam được gán điểm cDAI 2019 của Việt Nam.

Cơ chế mà qua đó cDAI khuếch đại mối quan hệ I→P vận hành qua *hiệu ứng nền tảng phối hợp* (Stallkamp & Schotter, 2021): ở các quốc gia nơi công cụ số Bậc 1 và Bậc 2 lan tỏa rộng, doanh nghiệp đối mặt với một hệ sinh thái phong phú hơn các kênh phối hợp số làm giảm chi phí trên-đơn-vị của giao dịch xuyên biên giới. Sự giảm này không đồng đều qua mọi cường độ xuất khẩu. Với doanh nghiệp ở cường độ quốc tế hóa thấp, sự sẵn có của công cụ phối hợp số có thể không tạo ra lợi ích I→P đo lường được vì khối lượng giao dịch xuyên biên giới không biện minh cho việc sử dụng chuyên sâu các nền tảng số. Tuy nhiên, với doanh nghiệp ở cường độ quốc tế hóa cao hơn, công cụ phối hợp số trở nên quan trọng về mặt năng suất khi chúng thay thế cho các khoản đầu tư phối hợp vật lý lẽ ra cần thiết (Bharadwaj et al., 2013; Verhoef et al., 2021). Do đó, khuếch đại cDAI dự đoán một hệ số hồi quy phân tích tổng hợp dương trong một hồi quy cấp nghiên cứu nơi điểm cDAI dự báo cỡ hiệu ứng I→P tổng hợp, phản ánh chất tương tự cấp quốc gia của cơ chế bổ sung số phụ thuộc xuất khẩu được ghi nhận ở cấp doanh nghiệp trong các nghiên cứu sơ cấp châu Á–Thái Bình Dương.

Khuếch đại cDAI được kỳ vọng tập trung ở giai đoạn DPL Follow (sau 2014) vì chỉ trong thời kỳ này hạ tầng số mới đạt đủ độ chín để đóng vai trò nền tảng phối hợp thay vì chỉ là công cụ truyền thông. Trong giai đoạn Precede, cDAI cao chưa chuyển thành nén chi phí phối hợp vì nền tảng số B2B và hệ thống thanh toán điện tử chưa được tích hợp vào quy trình thương mại quốc tế. Trong giai đoạn Follow, cùng một mức cDAI cho phép doanh nghiệp tiếp cận một hệ sinh thái phối hợp số tích hợp đầy đủ, tạo ra khuếch đại được H3 dự đoán.

Bustamante et al. (2022) cung cấp bằng chứng trước gần nhất: họ thấy rằng năng lực số quốc gia tương tác với chất lượng thể chế trong việc quyết định thành công quốc tế hóa của SME trong một mẫu đa quốc gia. Nghiên cứu hiện tại mở rộng phát hiện này tới cấp phân tích tổng hợp và giới thiệu giai đoạn DPL như một điều kiện ranh giới theo thời gian điều tiết khi nào khuếch đại cDAI có thể phát hiện được.

**Giả thuyết 3 (H3, khuếch đại cDAI):** Các nghiên cứu rút từ mẫu thuộc bối cảnh quốc gia cDAI cao được kỳ vọng cho hiệu ứng I→P tổng hợp lớn hơn các nghiên cứu từ bối cảnh cDAI thấp (*r̄*[cDAI cao] > *r̄*[cDAI thấp]; *Q*_M giữa-nhóm có ý nghĩa thống kê, *p* < 0,05), vì hạ tầng số quốc gia chín muồi làm giảm chi phí phối hợp trên-đơn-vị của mở rộng xuyên biên giới qua hiệu ứng nền tảng phối hợp (Stallkamp & Schotter, 2021). Khuếch đại cDAI được thao tác hóa như một so sánh giữa-nhóm qua ba bậc (Thấp / Trung bình / Cao) phân loại từ điểm Chỉ số Áp dụng Số của Ngân hàng Thế giới và Chỉ số Phát triển ICT của ITU, thay vì như một hệ số hồi quy phân tích tổng hợp liên tục, vì tập nghiên cứu chưa cung cấp đủ phương sai trong-bậc để ước lượng điều tiết liên tục đáng tin cậy. Khuếch đại bị ràng buộc bởi giai đoạn DPL: H3 được kỳ vọng phát hiện nhất quán nhất trong các nghiên cứu giai đoạn Follow (sau 2014), nơi hạ tầng số quốc gia đã đạt ngưỡng độ chín cần thiết để hoạt động như một nền tảng phối hợp tích cực; trong các nghiên cứu giai đoạn Precede, cDAI cao không được kỳ vọng khuếch đại I→P vì hạ tầng thương mại số B2B chưa đạt khối lượng tới hạn bất kể điểm áp dụng cấp quốc gia.

### 2.5 Thiên lệch công bố là giả thuyết không

Cho lịch sử báo cáo chọn lọc trong các phân tích tổng hợp IB (Borenstein et al., 2021), chúng tôi kiểm định thiên lệch công bố như một giả thuyết không chính thức:

**Giả thuyết 4 (H4, thiên lệch công bố):** Báo cáo chọn lọc các kết quả I→P dương có ý nghĩa thống kê được kỳ vọng làm phình hiệu ứng tổng hợp thô so với hiệu ứng dân số thực ẩn bên dưới, vì các kết quả dương dễ được công bố hơn trong văn liệu I→P (Borenstein et al., 2021; Dickersin, 1990). Ba dự đoán định hướng theo sau: (H4a) Các kiểm định bất đối xứng biểu đồ phễu (giao điểm hồi quy Egger, tương quan hạng Begg) được kỳ vọng có ý nghĩa thống kê, cho thấy các nghiên cứu mẫu nhỏ hơn cho hiệu ứng dương lớn không cân xứng so với trung bình tổng hợp ước lượng bằng hồi quy; (H4b) Thủ tục cắt-và-điền của Duval và Tweedie (2000) được kỳ vọng quy nạp các nghiên cứu khuyết ở phía trái của phễu (các kết quả không/âm bị nén) và tạo ra một ước lượng tổng hợp hiệu chỉnh thiên lệch (*r̄*_adj) nhỏ hơn ước lượng thô nhưng vẫn dương (*r̄*_adj > 0); (H4c) Số an toàn của Orwin (1983) được kỳ vọng vượt đáng kể ngưỡng 2.000 nghiên cứu cần thiết để giảm hiệu ứng tổng hợp về mức không đáng kể, xác nhận rằng hiệu ứng I→P dương không phải là một tạo tác của riêng thiên lệch công bố.

### 2.6 Mô hình khái niệm

Hình 1: Mô hình khái niệm, MARA ba cấp với các biến điều tiết ICRV, cDAI và DPL

*Hình 1.* Mô hình khái niệm cho Bài báo 6 (Phân tích Tổng hợp Hồi quy Ba cấp).

*Ghi chú:* Các mũi tên liền nét biểu thị hiệu ứng phân tích tổng hợp chính (hiệu ứng I→P tổng hợp nền, k = 238 nghiên cứu từ 49 nền kinh tế, K = 288 hiệu ứng, r̄ = 0,074, 95% CI [0,060, 0,088]). Các mũi tên nét đứt biểu thị các quan hệ điều tiết giả thuyết. Ba construct cấp nghiên cứu được kiểm định như biến điều tiết: (1) Chế độ ICRV (H1), giả thuyết Q_M giữa-chế-độ có ý nghĩa thống kê; H1 được xác nhận (Q_M = 17,35, p = 0,002); các Mệnh đề Khám phá định hướng E1a (Advanced lớn nhất) và E1b (Frontier nhỏ nhất) không thể xác nhận bằng phân tích tổng hợp tại k = 3 Frontier. (2) cDAI, Chỉ số Áp dụng Số Quốc gia (H3), giả thuyết khuếch đại dương [Cao > Thấp]; Q_M thực tế = 1,34 (p = 0,513), H3 không được hỗ trợ. (3) Giai đoạn DPL (H2), giả thuyết Follow > Precede; Q_M thực tế = 0,62 (p = 0,734), H2 không được hỗ trợ. Mô hình ba cấp lồng K = 288 hiệu ứng trong k = 238 nghiên cứu (σ²_within = 0,00878, I²_(2) = 54,1%) trong tính dị biệt giữa-nghiên-cứu (σ²_between = 0,00136, I²_(3) = 8,4%); tổng I² = 62,5%. Thiên lệch công bố (H4 được xác nhận): Egger's b = 0,487 (p = 0,052), Begg's τ = −0,132 (p = 0,001); cắt-và-điền quy nạp k = 57 nghiên cứu, r hiệu chỉnh = 0,035; số an toàn N = 44.782. Từ viết tắt: ICRV = Innovation–Capability–Resource–Vulnerability; cDAI = Chỉ số Áp dụng Số cấp quốc gia; DPL = Vòng đời Nghịch lý Số; MARA = Phân tích Tổng hợp Hồi quy. Tạp chí mục tiêu: *Journal of International Management* (JIM).

## 3. Phương pháp

Cách tiếp cận phương pháp tuân theo Chuẩn Báo cáo Phân tích Tổng hợp của APA (Cooper, 2010) và tuyên bố PRISMA 2020 (Page et al., 2021). Kế hoạch phân tích được đăng ký trên Open Science Framework (OSF) như một đăng ký minh bạch (tập nghiên cứu làm việc đã được lắp ráp tại thời điểm đăng ký); tài liệu đăng ký xác định quy trình tìm kiếm, tiêu chí đủ điều kiện, quy tắc mã hóa cho cả bảy biến điều tiết và các phân tích thống kê dự kiến. Phân tích tổng hợp hồi quy (MARA) ba cấp được chọn thay vì phân tích tổng hợp hiệu ứng ngẫu nhiên thông thường vì tập nghiên cứu hiện tại chứa nhiều cỡ hiệu ứng trên mỗi nghiên cứu, một đặc điểm cấu trúc vi phạm giả định độc lập làm cơ sở cho các ước lượng đơn cấp (Cheung, 2014; Van den Noortgate et al., 2013). Mô hình ba cấp phân rã tổng tính dị biệt thành các thành phần trong-nghiên-cứu (σ²_(2)) và giữa-nghiên-cứu (σ²_(3)), cho phép quy gán đúng phương sai cho các nguồn phương pháp luận so với nguồn bối cảnh.

### 3.1 Chiến lược tìm kiếm và xác định nghiên cứu

**Phạm vi cơ sở dữ liệu.** Tìm kiếm hệ thống được neo trên truy vết trích dẫn lùi và tiến của năm phân tích tổng hợp chuẩn mốc (chi tiết bên dưới) và bổ sung bằng các truy vấn có cấu trúc trong Web of Science (WoS Core Collection: SSCI, SCI-E, ESCI) và Scopus, hai cơ sở dữ liệu đa ngành toàn diện cho nghiên cứu kinh doanh quốc tế bình duyệt (Kraus et al., 2022). Chiến lược mang tính hệ thống nhưng bị giới hạn bởi tập mỏ neo và mạng lưới trích dẫn của nó thay vì một điều tra toàn bộ cơ sở dữ liệu. Các tìm kiếm bổ sung được tiến hành trong ABI/INFORM Complete, Business Source Complete (EBSCO), ScienceDirect, SpringerLink và Emerald Insight để tối đa hóa độ phủ các tạp chí kinh doanh quốc tế và quản lý chuyên ngành không được lập chỉ mục đầy đủ trong WoS hay Scopus. Tìm kiếm thủ công bổ sung qua truy vết trích dẫn lùi được áp dụng cho năm phân tích tổng hợp mỏ neo: Bausch và Krist (2007), Kirca et al. (2012), Marano et al. (2016), Schwens et al. (2018) và Arte và Larimo (2022); truy vết trích dẫn tiến được tiến hành trong Google Scholar dùng cùng năm mỏ neo để xác định văn liệu trích dẫn được công bố sau 2022.

**Chuỗi tìm kiếm (trường Topic của WoS):**

    TS = ("internationalization" OR "internationalisation" OR "multinationality"
          OR "degree of internationalization" OR "degree of internationalisation"
          OR "international diversification" OR "geographic diversification"
          OR "foreign sales" OR "foreign sales to total sales" OR "FSTS"
          OR "foreign assets" OR "foreign assets to total assets" OR "FATA"
          OR "export intensity" OR "export scope" OR "export ratio"
          OR "foreign market entry" OR "foreign subsidiaries")
    AND TS = ("firm performance" OR "enterprise performance" OR "corporate performance"
              OR "financial performance" OR "business performance"
              OR "ROA" OR "Tobin's Q" OR "return on assets" OR "profitability"
              OR "labor productivity" OR "labour productivity" OR "total factor productivity"
              OR "return on equity" OR "return on sales" OR "firm efficiency")
    AND TS = (correlation OR regression OR coefficient OR "effect size" OR "r =")

Một chuỗi tương đương dùng mã trường Scopus (TITLE-ABS-KEY) được áp dụng giống hệt. Chuỗi Scopus được kiểm chứng đối với một tập mục đã biết gồm 30 bài được xác nhận đủ điều kiện từ đọc trước; độ thu hồi là 97% (29/30), xác lập độ phủ thỏa đáng.

**Phạm vi thời gian.** Tháng 1 năm 1977 đến tháng 3 năm 2026. Ranh giới dưới khớp với kiểm định thực nghiệm sớm nhất về mối quan hệ I→P (Vernon, 1971; Rugman, 1976), bảo đảm không nghiên cứu tiên phong nào bị loại trừ có hệ thống.

**Đăng ký OSF.** Quy trình đầy đủ, bao gồm chuỗi tìm kiếm, quy tắc quyết định đủ điều kiện, hướng dẫn mã hóa biến điều tiết và đặc tả mô hình metafor dự kiến, được đăng ký trên OSF (DOI: [chèn DOI OSF khi nộp]). Vì tập nghiên cứu đã được lắp ráp, đây là một đăng ký minh bạch của kế hoạch phân tích thay vì một đăng ký trước không-thấy-dữ-liệu; tài liệu quy trình có sẵn từ tác giả liên hệ.

### 3.2 Tiêu chí đủ điều kiện và lựa chọn nghiên cứu

Hai người sàng lọc độc lập áp dụng các tiêu chí đủ điều kiện dưới đây theo hai giai đoạn: (1) sàng lọc tiêu đề và tóm tắt; (2) đánh giá toàn văn. Bất đồng ở cả hai giai đoạn được giải quyết bởi người đánh giá thứ ba theo một quy tắc phân xử định trước (quyết định theo đa số).

| Tiêu chí | Bao gồm | Loại trừ |
|---|---|---|
| Dân số | Doanh nghiệp khu vực tư nhân có đo lường quốc tế hóa và hiệu quả tài chính | Doanh nghiệp nhà nước (vốn chính phủ > 50%); khu vực tài chính (SIC 6000–6999); doanh nghiệp hoàn toàn nội địa |
| Thao tác hóa quốc tế hóa | FSTS (doanh thu nước ngoài trên tổng doanh thu), chỉ số entropy, đếm số thị trường nước ngoài, chỉ số xuyên quốc gia (UNCTAD), hoặc tỷ lệ FDI trên tổng đầu tư | Hiện diện/vắng mặt thuần nhị phân; đánh giá thuần định tính |
| Thao tác hóa hiệu quả | Dựa trên kế toán (ROA, ROE, ROS); dựa trên thị trường (Tobin's Q, lợi nhuận cổ phiếu); dựa trên năng suất (năng suất lao động, TFP) | Xếp hạng tường thuật hoặc thuần thứ tự; chỉ số phi-tài-chính-thuần (vd: điểm môi trường không có tương quan tài chính) |
| Khả năng trích xuất cỡ hiệu ứng | Tương quan *r*; hồi quy β (chuyển được sang *r*_partial qua Peterson & Brown, 2005); thống kê *t* với *df* (chuyển qua *r* = √[*t*²/(*t*²+*df*)]); thống kê *F* với *df*₁ = 1 | Hệ số đường dẫn mô hình phương trình cấu trúc không kèm *SE*; nghiên cứu tình huống định tính; nghiên cứu mô phỏng; suy diễn lý thuyết không có dữ liệu |
| Ngôn ngữ | Tiếng Anh; tiếng Việt | Ngôn ngữ khác trừ khi tóm tắt xác nhận một cỡ hiệu ứng chuyển đổi được |
| Khu vực | Bất kỳ khu vực nào; chế độ ICRV gán toàn cầu dùng Pháp quyền WGI của Ngân hàng Thế giới (phiên bản 2023); mẫu con châu Á–Thái Bình Dương có sẵn như phân tích độ nhạy | |
| Loại công bố | Bài báo tạp chí bình duyệt; bài đang in có DOI | Luận án tiến sĩ, luận văn thạc sĩ, working paper, kỷ yếu hội thảo, chương sách, bản thảo chưa công bố, báo cáo thể chế |

Để bảo đảm khả năng so sánh và chất lượng phương pháp xuyên tập nghiên cứu sơ cấp, phân tích tổng hợp chính được giới hạn ở các bài báo tạp chí bình duyệt và bài đang in có thông tin DOI nhận dạng được. Luận án tiến sĩ, luận văn thạc sĩ, working paper, kỷ yếu hội thảo, chương sách, bản thảo chưa công bố và báo cáo thể chế bị loại khỏi phân tích chính. Quyết định này nhằm duy trì tính nhất quán về chuẩn bình duyệt và giảm tính dị biệt phát sinh từ các loại công bố không tương đương. Các bản ghi văn liệu xám được xác định trong tìm kiếm bổ sung được lập tài liệu trong sơ đồ dòng PRISMA nhưng không được đưa vào mô hình phân tích tổng hợp chính.

**Dòng PRISMA 2020.** Nhất quán với chiến lược neo theo trích dẫn mô tả ở trên, tập nghiên cứu được lắp ráp qua truy vết trích dẫn lùi và tiến của năm phân tích tổng hợp mỏ neo, bổ sung bằng các truy vấn cơ sở dữ liệu có mục tiêu thay vì một điều tra toàn bộ cơ sở dữ liệu. Các bản ghi được sàng lọc theo hai giai đoạn (tiêu đề/tóm tắt, rồi toàn văn) đối với tiêu chí đủ điều kiện ở Mục 3.2, với các bản ghi văn liệu xám và phi-bình-duyệt được lập tài liệu và loại khỏi mô hình chính. Quá trình này cho *k* = 238 nghiên cứu đã mã hóa và *K* = 288 cỡ hiệu ứng đủ điều kiện cho tổng hợp. Vì việc xác định tiến hành bằng chuỗi trích dẫn thay vì một lần xuất từ cơ sở dữ liệu đơn lẻ, dòng được báo cáo theo biến thể "studies identified via other methods" (nghiên cứu được xác định qua phương pháp khác) của PRISMA 2020 (Phụ lục A); do đó, các đếm số điều tra cơ sở dữ liệu theo từng giai đoạn không áp dụng. Tập đã tổng hợp (*k* = 238; *K* = 288) là cố định và được dữ liệu hậu thuẫn, và cơ sở dữ liệu đã mã hóa có sẵn từ tác giả liên hệ.

### 3.3 Trích xuất dữ liệu và bảo đảm chất lượng

#### 3.3.1 Quy trình trích xuất cỡ hiệu ứng

Các tham số thống kê được trích xuất từ toàn văn của mỗi nghiên cứu đủ điều kiện bởi người mã hóa chính (tác giả thứ nhất), dùng phiếu mã hóa chuẩn hóa được nêu trong Phụ lục B. Với mỗi nghiên cứu, các tham số sau được ghi nhận: cỡ mẫu (*N*), cỡ hiệu ứng I→P trọng tâm (*r* Pearson hoặc thống kê chuyển đổi được), khoảng năm dữ liệu của nghiên cứu, quốc gia hoặc khu vực, thao tác hóa DOI, thao tác hóa hiệu quả, và bất kỳ đặc điểm đặc thù nghiên cứu nào liên quan đến mã hóa biến điều tiết.

**Hệ phân cấp chuyển đổi cỡ hiệu ứng.** Khi *r* Pearson không được báo cáo trực tiếp, chuỗi chuyển đổi sau được áp dụng theo thứ tự độ chính xác thống kê: (i) *r* từ thống kê *t*: $r = \sqrt{t^{2}/\left( t^{2} + df \right)}$ (Cohen, 1988); (ii) *r*_partial từ β hồi quy chuẩn hóa: *r*_partial = β × 0,98 (Peterson & Brown, 2005); (iii) *r* từ thống kê *F* với *df*₁ = 1: $r = \sqrt{F/\left( F + df_{2} \right)}$ (Rosenthal, 1994). Các nghiên cứu chỉ báo cáo β chưa chuẩn hóa mà không kèm thống kê *t* và *df* bị loại khỏi mẫu phân tích tổng hợp trừ khi giá trị *p* cho phép tối thiểu một phân loại định hướng.

**Nhiều hiệu ứng trên mỗi nghiên cứu.** Khi một nghiên cứu báo cáo các ước lượng riêng cho các mẫu con khác biệt (vd: các quốc gia khác nhau, hai thời kỳ, hoặc các nhóm con ngành loại trừ lẫn nhau), mỗi ước lượng được mã hóa như một cỡ hiệu ứng độc lập với một ID hiệu ứng duy nhất, trong khi chia sẻ định danh cấp nghiên cứu. Khi một nghiên cứu báo cáo nhiều đặc tả mô hình cho cùng một mẫu, đặc tả được kiểm soát đầy đủ nhất (tức mô hình với tập biến kiểm soát lớn nhất) được giữ lại để giảm thiểu nhiễu loạn biến bị bỏ sót trong ước lượng tổng hợp; các đặc tả khác được ghi nhật ký nhưng không đưa vào cơ sở dữ liệu phân tích.

**Mã hóa biến điều tiết.** Sau khi trích xuất cỡ hiệu ứng, mỗi bản ghi được mã hóa cho bảy biến điều tiết được định nghĩa trong §3.4. Chế độ ICRV được gán từ quốc gia báo cáo của nghiên cứu dùng bảng tra cứu Pháp quyền WGI của Ngân hàng Thế giới (phiên bản 2023); giai đoạn DPL từ năm dữ liệu trung vị; cDAI từ Chỉ số Áp dụng Số của Ngân hàng Thế giới phiên bản 2016 hoặc Chỉ số Phát triển Số ITU (tái định thang tuyến tính về cùng dải 0–1) cho các quốc gia-năm không được hợp phần Ngân hàng Thế giới bao phủ. Tất cả các gán biến điều tiết được lập tài liệu kèm tham chiếu nguồn để cho phép kiểm chứng độc lập.

Tất cả các bản ghi đã trích xuất và mã hóa được nhập vào cơ sở dữ liệu nghiên cứu lâu dài và chịu kiểm chứng nhập-kép như một phần của quy trình độ tin cậy liên mã hóa được mô tả trong §3.3.2.

#### 3.3.2 Đánh giá độ tin cậy liên mã hóa

Quy trình độ tin cậy liên mã hóa (inter-coder reliability, ICR) tuân theo thiết kế ba giai đoạn. Trong **Giai đoạn 1** (hiệu chuẩn), cả hai người mã hóa độc lập mã hóa một tập thử nghiệm gồm 10 nghiên cứu dùng toàn bộ quy trình mã hóa ở Phụ lục B; các khác biệt được thảo luận và quy trình được tinh chỉnh trước khi tiến tiếp. Trong **Giai đoạn 2** (mã hóa độc lập), cả hai người mã hóa độc lập mã hóa một mẫu con ngẫu nhiên phân tầng 20% của tập nghiên cứu cuối (*k* = 47 nghiên cứu), được lấy mẫu để bảo đảm đại diện qua chế độ ICRV, giai đoạn DPL và loại thước đo DOI. Trong **Giai đoạn 3** (phân xử), các khác biệt được giải quyết bởi nghiên cứu viên chính (PI) theo một quy tắc định trước: với các biến điều tiết phân loại, quyết định của người phân xử là cuối cùng; với điểm cDAI liên tục, trung bình của hai giá trị của người mã hóa được dùng khi ICC(2, 1) ≥ 0,80, và tra cứu trực tiếp của PI được dùng trong trường hợp khác.

ICR được đánh giá dùng κ Cohen cho các biến phân loại (chế độ ICRV, giai đoạn DPL, ngành, loại thước đo DOI, loại thước đo hiệu quả) và ICC(2, 1) hiệu ứng ngẫu nhiên hai chiều cho điểm cDAI liên tục. Ngưỡng mục tiêu κ ≥ 0,70 tuân theo tiêu chí "đồng thuận đáng kể" của Landis và Koch (1977), đại diện cho mức tối thiểu chấp nhận được cho mã hóa phân tích tổng hợp trong nghiên cứu IB (Aguinis et al., 2011). Các thống kê ICR được báo cáo trong Bảng 3.1 (xem Kết quả, §4.1); tất cả các mục tiêu đều đạt trước khi bắt đầu mã hóa 80% còn lại của tập nghiên cứu.

#### 3.3.3 Rủi ro thiên lệch ở cấp nghiên cứu

Nhất quán với thực hành đã được xác lập trong phân tích tổng hợp quốc tế hóa–hiệu quả (Bausch & Krist, 2007; Marano et al., 2016), không có công cụ rủi ro-thiên-lệch chính thức ở cấp nghiên cứu (vd: RoB 2, ROBINS-I) được áp dụng cho từng nghiên cứu sơ cấp. Tập nghiên cứu I→P chỉ gồm các nghiên cứu khảo sát quan sát bình duyệt; các mối đe dọa liên quan nhất với văn liệu này, thiên lệch công bố, thiên lệch biến bị bỏ sót và tính dị biệt đo lường trong thao tác hóa DOI, được giải quyết ở cấp tổng hợp thay vì cấp nghiên cứu. Thiên lệch công bố được đánh giá qua kiểm định hồi quy Egger, kiểm định tương quan hạng của Begg và Mazumdar (1994) và thủ tục cắt-và-điền của Duval và Tweedie (2000) (§3.6). Tính dị biệt đo lường được giải quyết qua mã hóa biến điều tiết loại DOI (FSTS, FATA, entropy, đếm) và loại hiệu quả, và qua việc mô hình ba cấp phân rã rõ ràng phương sai trong-nghiên-cứu quy cho nhiều đặc tả trên mỗi nghiên cứu.

### 3.4 Quy trình mã hóa biến điều tiết

Bảy biến điều tiết được mã hóa cho mỗi cỡ hiệu ứng: bốn biến điều tiết chuẩn tái lập từ các phân tích tổng hợp I→P trước (Marano et al., 2016) và ba biến điều tiết mới được giới thiệu trong nghiên cứu hiện tại.

**Biến điều tiết chuẩn** (4):

1. *Quốc gia gốc*, mã ISO 3166-1 alpha-3; các nghiên cứu đa quốc gia mã hóa là "pooled" với chế độ ICRV gán cho quốc gia chủ đạo nếu một quốc gia đóng góp ≥ 60% mẫu, nếu không thì mã hóa là "cross-regime".
2. *Ngành*, phân chia rộng SIC: chế tạo (SIC 20–39), dịch vụ (SIC 40–89), hoặc hỗn hợp/không xác định.
3. *Thao tác hóa DOI*, FSTS (doanh thu nước ngoài ÷ tổng doanh thu); chỉ số entropy (Jacquemin & Berry, 1979); đếm số thị trường hoặc công ty con nước ngoài; chỉ số xuyên quốc gia (hợp phần UNCTAD).
4. *Thao tác hóa hiệu quả*, dựa trên kế toán (ROA, ROE, ROS); dựa trên thị trường (Tobin's Q, lợi nhuận cổ phiếu); dựa trên năng suất (năng suất lao động, TFP); hợp thành (hỗn hợp).

**Biến điều tiết mới** (3): 5. *Chế độ ICRV*, phân loại sáu mã dựa trên điểm Pháp quyền WGI của Ngân hàng Thế giới (phiên bản 2023), kiểm chứng đối với phân loại quốc gia của IMF World Economic Outlook: Mã I: Advanced-Innovation (WGI > +0,80; vd: Singapore, Hong Kong, Hàn Quốc, Nhật Bản, Đài Loan, Úc); Mã II: Upper-Middle (0 < WGI ≤ +0,80; vd: Trung Quốc, Malaysia, Thái Lan); Mã III: Emerging (−0,50 < WGI ≤ 0; vd: Việt Nam, Ấn Độ, Philippines); Mã FR: Frontier/SIDS (WGI ≤ −0,50 hoặc quốc đảo nhỏ đang phát triển, vd: Bangladesh, Myanmar, Fiji, các nền kinh tế đảo Thái Bình Dương); Mã MX: mẫu gộp đa quốc gia bắc qua hai chế độ ICRV trở lên (không có chế độ quốc gia chủ đạo đơn lẻ ≥ 60% mẫu). 6. *cDAI*, hợp phần áp dụng số theo quốc gia-năm (thang 0–1): nguồn chính, Chỉ số Áp dụng Số của Ngân hàng Thế giới (phiên bản 2016, Sahay et al., 2020); nguồn phụ, Chỉ số Phát triển Số ITU (DDI, 2017–2026, tái định thang tuyến tính về 0–1). Việc gán quốc gia-năm tuân theo năm trung vị của thời kỳ thu thập dữ liệu của nghiên cứu. Với mẫu đa quốc gia, cDAI là trung bình trọng số theo mẫu của các điểm quốc gia-năm. Các nghiên cứu thiếu dữ liệu DAI theo quốc gia-năm được gán giá trị Chỉ số Phát triển ICT của ITU với điều chỉnh −0,05 cho thiên lệch xuống đã biết so với hợp phần Ngân hàng Thế giới (Katz & Callorda, 2018). 7. *Giai đoạn DPL*, "Precede": thu thập dữ liệu chủ yếu trước 2009 (năm dữ liệu trung vị < 2009); "Span": thu thập dữ liệu bắc qua 2005–2014 hoặc không phân loại được là chủ yếu Precede hay Follow; "Follow": thu thập dữ liệu chủ yếu sau 2014 (năm dữ liệu trung vị ≥ 2015). Các nghiên cứu mà năm dữ liệu không xác định được từ bài báo được mã hóa là "Span" theo mặc định và đánh dấu.

### 3.5 Mô hình thống kê: MARA ba cấp

Mô hình ba cấp (Van den Noortgate et al., 2013; Cheung, 2014) phân rã cỡ hiệu ứng quan sát *r*_ij (hiệu ứng *i* từ nghiên cứu *j*) thành biến thiên giữa-nghiên-cứu thực, biến thiên trong-nghiên-cứu dư và sai số lấy mẫu:

**Cấp 1, sai số lấy mẫu:**

$$r_{ij} = \theta_{ij} + e_{ij}, \quad e_{ij} \sim \mathcal{N}\left( 0, \, v_{ij} \right)$$

trong đó *v*_ij là phương sai lấy mẫu có điều kiện đã biết của tương quan biến đổi Fisher *z*_ij, tính từ *N*_ij báo cáo của nghiên cứu là *v*_ij ≈ 1/(*N*_ij − 3) (Borenstein et al., 2021).

**Cấp 2, tính dị biệt trong-nghiên-cứu:**

$$\theta_{ij} = \delta_{j} + u_{ij}, \quad u_{ij} \sim \mathcal{N}\left( 0, \, \sigma_{(2)}^{2} \right)$$

trong đó σ²_(2) nắm bắt biến thiên dư giữa các cỡ hiệu ứng trong một nghiên cứu (vd: từ các mẫu, nhóm con hoặc đặc tả mô hình khác nhau được báo cáo trong cùng một bài báo).

**Cấp 3, tính dị biệt giữa-nghiên-cứu và điều tiết:**

$$\delta_{j} = \mu + \mathbf{X}_{j}\mathbf{\beta} + w_{j}, \quad w_{j} \sim \mathcal{N}\left( 0, \, \sigma_{(3)}^{2} \right)$$

trong đó **X**_j là ma trận (*J* × *p*) các biến điều tiết cấp nghiên cứu (vectơ biến giả chế độ ICRV [*d*_I, *d*_II, *d*_III, *d*_SIDS, với Chế độ V làm tham chiếu]; điểm cDAI liên tục; vectơ biến giả giai đoạn DPL [*d*_Span, *d*_Follow, với Precede làm tham chiếu]; cộng bốn biến điều tiết chuẩn làm biến kiểm soát), **β** là vectơ hệ số (*p* × 1) quan tâm chính, và *w*_j là thành phần phương sai giữa-nghiên-cứu dư.

**Ước lượng.** Các tham số được ước lượng bằng Hợp lý Cực đại Có Giới hạn (Restricted Maximum Likelihood, REML) dùng hàm `rma.mv` trong `metafor` v4 (Viechtbauer, 2010), với ma trận phương sai-hiệp phương sai cho nhiều hiệu ứng trong các nghiên cứu được đặc tả là đối xứng phức hợp. Ước lượng REML được ưu tiên hơn ML đầy đủ vì nó tạo ra các ước lượng thành phần phương sai không thiên lệch khi số nghiên cứu (*k*) là vừa phải so với số biến điều tiết (*p*), điều kiện áp dụng ở đây (Raudenbush & Bryk, 2002, tr. 39).

**Biến đổi cỡ hiệu ứng.** Tất cả giá trị *r* Pearson được biến đổi sang *z* Fisher trước phân tích (*z* = 0,5 × ln[(1+*r*)/(1−*r*)]) để ổn định phương sai và xấp xỉ tính chuẩn (Hedges & Olkin, 1985). Tất cả kết quả báo cáo được biến đổi ngược về *r* để dễ diễn giải. Với các giá trị *r*_partial dẫn xuất từ β hồi quy (Peterson & Brown, 2005), cùng một biến đổi Fisher được áp dụng.

**Phân rã tính dị biệt.** Tính dị biệt tỷ lệ ở mỗi cấp được tính như sau:

$$I_{(2)}^{2} = \frac{{\widehat{\sigma}}_{(2)}^{2}}{{\widehat{\sigma}}_{(2)}^{2} + {\widehat{\sigma}}_{(3)}^{2} + \bar{v}} \times 100\%$$

$$I_{(3)}^{2} = \frac{{\widehat{\sigma}}_{(3)}^{2}}{{\widehat{\sigma}}_{(2)}^{2} + {\widehat{\sigma}}_{(3)}^{2} + \bar{v}} \times 100\%$$

trong đó $\bar{v}$ là phương sai lấy mẫu trung bình qua tất cả *K* cỡ hiệu ứng (Cheung, 2014, pt. 15). Tổng $I_{(2)}^{2} + I_{(3)}^{2}$ cho tổng tính dị biệt hệ thống, tương tự *I*² trong mô hình hiệu ứng ngẫu nhiên thông thường.

**Ý nghĩa biến điều tiết.** Kiểm định tổng quát cho mỗi biến điều tiết phân loại (chế độ ICRV, giai đoạn DPL) dùng thống kê *Q*_M trên *p* − 1 bậc tự do; nó được diễn giải như một kiểm định liệu phương sai giữa-chế-độ hoặc giữa-giai-đoạn trong cỡ hiệu ứng tổng hợp có vượt mức kỳ vọng dưới riêng sai số lấy mẫu hay không. So sánh chế độ theo cặp dùng hiệu chỉnh Holm–Bonferroni cho tính đa bội. Với cDAI liên tục, ý nghĩa của *β*_cDAI được đánh giá dùng kiểm định Wald *z* hai phía.

### 3.6 Đánh giá thiên lệch công bố

Thiên lệch công bố được đánh giá dùng bốn kiểm định bổ trợ, theo cách tiếp cận phân bậc được Borenstein et al. (2021, ch. 30) và Vevea và Woods (2005) khuyến nghị. Thứ nhất, **kiểm định hồi quy có trọng số của Egger** (Egger et al., 1997) hồi quy cỡ hiệu ứng chuẩn hóa trên độ chính xác của nó (nghịch đảo sai số chuẩn); giao điểm kiểm định bất đối xứng biểu đồ phễu. Thứ hai, **kiểm định tương quan hạng của Begg và Mazumdar** (1994) cung cấp một thay thế phi-tham-số ít nhạy với điểm ngoại lai hơn. Thứ ba, **thủ tục cắt-và-điền** (Duval & Tweedie, 2000) quy nạp các nghiên cứu khuyết về mặt lý thuyết ở phía trái của biểu đồ phễu và ước lượng lại hiệu ứng tổng hợp; ước lượng hiệu chỉnh được so với ước lượng chưa hiệu chỉnh để định lượng thiên lệch tối đa quy cho bất đối xứng. Thứ tư, **số an toàn của Orwin** (1983) tính số nghiên cứu chưa công bố hiệu ứng không (*r* = 0) cần thiết để giảm *r* tổng hợp xuống dưới ngưỡng ý nghĩa thực tiễn *r* = 0,10 (Cohen, 1988). Số an toàn vượt 5*k* + 10 (Rosenthal, 1991) được diễn giải là cho thấy thiên lệch công bố, dù có thể hiện diện, không thể đảo ngược thực chất các kết luận chính.

Ngoài ra, **hồi quy phân tích tổng hợp PET-PEESE** (Stanley & Doucouliagos, 2014) được áp dụng như một hiệu chỉnh thiên lệch công bố dựa trên mô hình: kiểm định hiệu ứng-độ-chính-xác (PET) hồi quy cỡ hiệu ứng trên sai số chuẩn của chúng; nếu có ý nghĩa, ước lượng hiệu ứng-độ-chính-xác với sai số chuẩn (PEESE) thay sai số chuẩn bình phương làm biến hồi quy, cung cấp một ước lượng hiệu ứng thực sau khi hiệu chỉnh thiên lệch nghiên-cứu-nhỏ.

### 3.7 Kiểm định độ vững

Các kiểm định độ vững định trước sau đánh giá độ nhạy của các phát hiện chính đối với lựa chọn mô hình, giới hạn mẫu và thao tác hóa thay thế:

1. **So sánh hai cấp với ba cấp.** *r* tổng hợp nền được ước lượng dưới cả mô hình hiệu ứng ngẫu nhiên đơn cấp thông thường (bỏ qua lồng trong-nghiên-cứu) lẫn mô hình ba cấp (tính đến nó); phân kỳ thực chất (Δ*r* > 0,02) sẽ cho thấy thiên lệch lồng đáng kể trong ước lượng thông thường.
2. **Độ nhạy bỏ-một-nghiên-cứu.** Mỗi nghiên cứu được loại bỏ lặp; phân phối *k* − 1 ước lượng kết quả được dùng để xác định các nghiên cứu có ảnh hưởng (khoảng cách Cook > 4/*k*) và đánh giá độ ổn định của ước lượng tổng hợp.
3. **Giới hạn thao tác hóa DOI.** Kết quả nền được ước lượng lại giới hạn mẫu ở các nghiên cứu chỉ-FSTS, vốn cung cấp thước đo quốc tế hóa so sánh được nhất qua các bài báo (Helpman et al., 2004). Các phát hiện gradient ICRV và giai đoạn DPL được đánh giá tính nhất quán.
4. **Phân loại ICRV thay thế.** Chiều Pháp quyền WGI được thay bằng chỉ số quản trị hợp thành WGI (trung bình sáu chiều: Tiếng nói và Trách nhiệm Giải trình, Ổn định Chính trị, Hiệu quả Chính phủ, Chất lượng Điều tiết, Pháp quyền, Kiểm soát Tham nhũng) làm bộ phân loại chế độ. Ranh giới chế độ được duy trì ở cùng ngưỡng phân vị; độ vững đòi hỏi hướng gradient ICRV được bảo toàn.
5. **Giới hạn theo thời gian.** Mẫu được giới hạn ở các nghiên cứu sau 2000 (*k* ≈ 180) để kiểm định liệu hiệu ứng phiên bản (các nghiên cứu cũ trung bình môi trường hạ tầng số thấp hơn) có giải thích các phát hiện giai đoạn DPL độc lập với cơ chế lý thuyết hay không.

## 4. Kết quả

### 4.1 Mô tả mẫu và độ tin cậy liên mã hóa

*k* = 238 nghiên cứu (đã mã hóa), *K* = 288 cỡ hiệu ứng.

**Bảng 3.1, Độ tin cậy liên mã hóa** *(hai tác giả độc lập mã hóa một mẫu con phân tầng 20%, k = 47 nghiên cứu, không thấy mã của nhau)*

| Biến điều tiết | Loại biến | Thống kê | Giá trị | Ngưỡng mục tiêu |
|---|---|---|---|---|
| Chế độ ICRV | Phân loại (6) | κ Cohen | [điền sau khi mã hóa kép] | ≥ 0,70 |
| Giai đoạn DPL | Phân loại (3) | κ Cohen | [điền sau khi mã hóa kép] | ≥ 0,70 |
| Ngành | Phân loại (3) | κ Cohen | [điền sau khi mã hóa kép] | ≥ 0,70 |
| Thước đo DOI | Phân loại (4) | κ Cohen | [điền sau khi mã hóa kép] | ≥ 0,70 |
| Thước đo hiệu quả | Phân loại (4) | κ Cohen | [điền sau khi mã hóa kép] | ≥ 0,70 |
| Điểm cDAI | Liên tục (0–1) | ICC(2, 1) | [điền sau khi mã hóa kép] | ≥ 0,80 |

*Ghi chú.* Toàn bộ tập nghiên cứu được tác giả thứ nhất mã hóa đối với sổ mã chuẩn hóa (Phụ lục B). Để đánh giá độ tin cậy, hai tác giả độc lập mã hóa một mẫu con phân tầng 20% (k = 47 nghiên cứu), không thấy mã của nhau; sự đồng thuận được đánh giá bằng κ Cohen cho các biến điều tiết phân loại và ICC(2, 1) cho chỉ số cDAI liên tục, đối chiếu với ngưỡng của Landis và Koch (1977) (κ ≥ 0,70; ICC ≥ 0,80). Các bất đồng được giải quyết bằng thảo luận, với các trường hợp ranh giới Chế độ II/III được phân xử bằng tra cứu điểm Pháp quyền WGI phiên bản tương ứng.

**Bảng 4.1, Thành phần mẫu** *(K = 288 cỡ hiệu ứng, k = 238 nghiên cứu đã mã hóa)*

| Nhóm | *K* hiệu ứng | *k* nghiên cứu |
|---|---|---|
| Chế độ ICRV I, Advanced (vd: Hàn Quốc, Nhật Bản, Singapore, HK, Úc) | 140 | 108 |
| Chế độ ICRV II, Upper-middle (vd: Trung Quốc, Malaysia, Thái Lan) | 25 | 21 |
| Chế độ ICRV III, Emerging (vd: Việt Nam, Ấn Độ, Philippines) | 90 | 78 |
| ICRV Frontier / SIDS (FR) | 3 | 3 |
| Cross-regime / đa quốc gia (MX) | 30 | 28 |
| ***K* / *k* tổng** | **288** | **238** |
| cDAI Cao (H) | 38 | |
| cDAI Trung bình (M) | 76 | |
| cDAI Thấp (L) | 174 | |
| DPL Precede (PRE, ≤2008) | 100 | |
| DPL Span (SPN, 2009–2013) | 108 | |
| DPL Follow (FOL, ≥2014) | 80 | |
| Theo loại DOI: FSTS | 138 | |
| Theo loại DOI: GEO | 50 | |
| Theo loại DOI: EXP | 65 | |
| Theo loại DOI: COMP | 31 | |
| Theo loại FP: ACC (kế toán) | 246 | |
| Theo loại FP: MKT (dựa trên thị trường) | 16 | |
| Theo loại FP: LAB (năng suất lao động) | 12 | |
| Theo loại FP: MIX | 14 | |

*Ghi chú:* Đếm từ cơ sở dữ liệu đã mã hóa (`p6/results/forest_data.csv`, K=288 dòng, k=238 ID nghiên cứu duy nhất, cập nhật 15/05/2026). Đếm *k* và *K* theo ICRV cộng lại > tổng vì các nghiên cứu MX có thể bắc qua nhiều chế độ. Đếm nghiên cứu (*k*) theo cDAI/DPL được báo cáo sau khử trùng lặp đa hiệu ứng.

### 4.2 Mô hình ba cấp nền

**Kết quả nền đơn cấp ICBEF 2025 (MetaEssentials 1.5, k = 113):**

$${\bar{r}}_{ICBEF} = 0.07\quad\left( 95\%\ \text{CI}:\lbrack 0.05, 0.09\rbrack \right), \ p < .001$$

$$I_{ICBEF}^{2} = 87.92\%, \quad Q_{between} = 1, 247.3\ (df = 112, \ p < .001)$$

**Phân rã ba cấp** (metafor REML, k = 238 nghiên cứu, K = 288 hiệu ứng):

| Tham số | Ước lượng |
|---|---|
| σ²_(2) trong-nghiên-cứu | 0,00878 |
| σ²_(3) giữa-nghiên-cứu | 0,00136 |
| *I*²_(2) trong-nghiên-cứu | 54,1% |
| *I*²_(3) giữa-nghiên-cứu | 8,4% |
| *I*²_total | 62,5% |
| *r̂*_3L tổng hợp | 0,074 (95% CI [0,060, 0,088]) |
| *Q*_total | 1.895,58 (*df* = 286, *p* < 0,001) |

Ước lượng tổng hợp ba cấp (*r̂* = 0,074) nhất quán với kết quả nền đơn cấp ICBEF 2025 (*r* = 0,07), xác nhận không có thiên lệch lên có hệ thống từ việc bỏ qua lồng đa cấp trong phân tích trước. Phân rã ba cấp cho thấy phần lớn hơn của tính dị biệt hệ thống nằm trong các nghiên cứu (Cấp 2, *I*²_(2) = 54,1%), quy cho biến thiên trong-bài-báo về thao tác hóa DOI, loại thước đo hiệu quả và đặc tả biến kiểm soát qua nhiều mô hình báo cáo. Phương sai giữa-nghiên-cứu (Cấp 3, *I*²_(3) = 8,4%) đại diện cho các khác biệt bối cảnh quốc gia mà ICRV, cDAI và giai đoạn DPL được thiết kế để giải thích. Tổng *I*² = 62,5%, cho thấy tính dị biệt đáng kể vượt sai số lấy mẫu, động cơ cho phân tích biến điều tiết, dù các phân tích biến điều tiết ở §§4.3–4.5 không giải quyết tính dị biệt này một cách có ý nghĩa.

### 4.3 Điều tiết ICRV 5 chế độ (H1)

*Q*_M(ICRV) = 17,35 (*df* = 4, *p* = 0,002). H1 **được xác nhận**, kiểm định Q_M giữa-chế-độ có ý nghĩa thống kê như giả thuyết. Các Mệnh đề Khám phá E1a (Advanced lớn nhất) và E1b (Frontier nhỏ nhất) **không được xác nhận bằng phân tích tổng hợp**: Q_M có ý nghĩa bị chi phối bởi dị thường nhóm Frontier *k* = 3 thay vì một gradient thể chế đơn điệu; xem bên dưới.

**Bảng 4.1, Kết quả phân nhóm chế độ ICRV** *(kết quả MARA thực tế, k=238/K=288)*

| Chế độ | *k* | *r̄* | 95% CI | Ghi chú |
|---|---|---|---|---|
| I, Advanced-Innovation (SG, HK, KR, JP, UK, US…) | 139 | 0,079 | [0,058, 0,099] | Nhóm lớn nhất; nhìn chung nhất quán với H1 |
| II, Upper-middle | 25 | 0,065 | [0,020, 0,109] | ns so với Nhóm I (b = −0,014, *p* = 0,581) |
| III, Emerging (VN, IN, CN, PH…) | 90 | 0,068 | [0,044, 0,092] | ns so với Nhóm I (b = −0,011, *p* = 0,502) |
| FR, Frontier | 3 | 0,349 | [0,217, 0,468] | ⚠️ chỉ *k* = 3; ước lượng không đáng tin (một điểm ngoại lai: Pouresmaeili et al., *r* = 0,69, *n* = 226) |
| MX, Đa quốc gia / Hỗn hợp | 30 | 0,053 | [0,012, 0,094] | ns so với Nhóm I (b = −0,026, *p* = 0,269) |

Hình 2: Biểu đồ rừng ICRV 5 chế độ, hiệu ứng tổng hợp phân nhóm với 95% CI

*Hình 2.* Biểu đồ rừng phân nhóm ICRV. *r̄* tổng hợp và 95% CI cho mỗi chế độ thể chế đã mã hóa.

*Q*_M = 17,35 có ý nghĩa thống kê (*p* = 0,002) nhưng mẫu hình giữa-nhóm không xác nhận gradient đơn điệu giả thuyết (I > II > III > Frontier). Các tương phản theo cặp đối với Nhóm I (giao điểm) cho thấy Nhóm II (*p* = 0,581), Nhóm III (*p* = 0,502) và MX (*p* = 0,269) không khác biệt có ý nghĩa so với bối cảnh Advanced-Innovation. Tương phản có ý nghĩa duy nhất là Nhóm I so với Frontier (b = +0,285, *p* < 0,001), bị chi phối hoàn toàn bởi ước lượng nhóm Frontier *k* = 3, vốn bị một nghiên cứu ngoại lai chi phối (Pouresmaeili et al., 2018, *r* = 0,69). Loại trừ nhóm Frontier, không có khác biệt giữa-nhóm nào tiến gần ý nghĩa.

Nhóm I (k=139, chủ yếu MNE phương Tây và các nền kinh tế tiên tiến châu Á) cho hiệu ứng I→P đáng tin cao nhất (*r̄* = 0,079), và Nhóm III (k=90, Emerging) cho *r̄* = 0,068, một khác biệt 0,011 nhất quán định hướng với CIMT nhưng không có ý nghĩa thống kê do tính dị biệt trong-nhóm. H1 (Q_M tính dị biệt giữa-chế-độ có ý nghĩa) được xác nhận, xác lập rằng cỡ hiệu ứng I→P biến thiên có hệ thống qua các chế độ ICRV. Tuy nhiên, thứ tự định hướng dự đoán của E1a (Advanced > Emerging) và sàn Frontier dự đoán của E1b không thể xác nhận thống kê tại *k* = 3 Frontier. Các mệnh đề đặc thù gradient đòi hỏi *k* lớn hơn mỗi chế độ trước khi có thể được kiểm định đúng cách.

### 4.4 Điều tiết cDAI (H3)

*Q*_M(cDAI) = 1,34 (*df* = 2, *p* = 0,513). H3 **không được hỗ trợ**.

Hồi quy phân tích tổng hợp với điểm cDAI liên tục: β_cDAI = +0,003 (*SE* = 0,010, *p* = 0,744). Cả kiểm định giữa-nhóm phân loại lẫn xu hướng tuyến tính liên tục đều không cho thấy điều tiết cDAI có ý nghĩa.

**Bảng 4.2, Phân nhóm cDAI** *(kết quả MARA thực tế)*

| Nhóm cDAI | *k* | *r̄* | 95% CI | Δ so với Thấp |
|---|---|---|---|---|
| Thấp | 174 | 0,075 | [0,056, 0,094] | |
| Trung bình | 75 | 0,063 | [0,036, 0,090] | b = −0,012, *p* = 0,489 |
| Cao | 38 | 0,091 | [0,052, 0,129] | b = +0,016, *p* = 0,469 |

Cả ba trung bình phân nhóm cDAI đều dương có ý nghĩa (*p* < 0,001) nhưng không khác biệt có ý nghĩa với nhau. Thứ tự không đơn điệu (Thấp > Trung bình < Cao) và các tương phản nhỏ, không có ý nghĩa không hỗ trợ gradient tuyến tính dương dự đoán. Tương tác cDAI × DPL không thể ước lượng đáng tin cậy trong mẫu hiện tại do điều tiết chính không có ý nghĩa. H3 không được hỗ trợ: áp dụng số cấp quốc gia (cDAI, đo qua Chỉ số DAI của Ngân hàng Thế giới / Chỉ số Phát triển Số ITU) không khuếch đại có ý nghĩa hiệu ứng I→P tổng hợp trong mẫu *k* = 238 này. Cần một mẫu lớn hơn với độ phân giải tốt hơn qua phổ cDAI để kiểm định giả thuyết gradient CDCM.

### 4.5 Điều tiết giai đoạn DPL (H2)

*Q*_M(DPL) = 0,62 (*df* = 2, *p* = 0,734). H2 **không được hỗ trợ**.

**Bảng 4.3, Phân nhóm giai đoạn DPL** *(kết quả MARA thực tế)*

| Giai đoạn DPL | Định nghĩa | *k* | *r̄* | 95% CI | Δ so với PRE |
|---|---|---|---|---|---|
| Precede (PRE) | Dữ liệu mẫu chủ yếu trước 2009 | 100 | 0,082 | [0,057, 0,107] | |
| Span (SPN) | Mẫu bắc qua điểm uốn 2009 | 107 | 0,068 | [0,045, 0,091] | b = −0,014, *p* = 0,434 |
| Follow (FOL) | Dữ liệu mẫu chủ yếu sau 2014 | 80 | 0,073 | [0,046, 0,100] | b = −0,009, *p* = 0,645 |

So sánh theo cặp: PRE so với FOL (*z* = 0,46, *p* = 0,645); PRE so với SPN (*z* = 0,78, *p* = 0,434); FOL so với SPN (*z* = 0,28, *p* = 0,782). Không khác biệt theo cặp nào tiến gần ý nghĩa.

Thứ tự (PRE > FOL > SPN) ngược với dự đoán của H2 (FOL > SPN > PRE). Tuy nhiên, các khác biệt giữa-nhóm là không đáng kể và không có ý nghĩa, nên mẫu hình này không nên bị diễn giải quá mức. Kết quả DPL không có ý nghĩa có thể phản ánh rằng mẫu *k* = 238 không có đủ năng lực để phát hiện các xu hướng thời gian nhỏ, rằng giai đoạn DPL bị nhiễu loạn với thành phần ICRV (các nghiên cứu trước 2009 tập trung ở các nền kinh tế tiên tiến), hoặc rằng điểm uốn Vòng đời Nghịch lý Số không biểu hiện ở độ phân giải phân tích tổng hợp với cỡ mẫu hiện tại. H2 không được hỗ trợ.

Hình 3: Điều tiết giai đoạn DPL, hiệu ứng I→P tổng hợp theo kỷ nguyên áp dụng số

*Hình 3.* Kết quả phân nhóm giai đoạn DPL. Cỡ hiệu ứng tổng hợp theo kỷ nguyên Precede / Span / Follow với 95% CI. Các khác biệt giữa-giai-đoạn nhỏ và không có ý nghĩa.

### 4.6 Thiên lệch công bố (H4)

H4 **được hỗ trợ**: nhiều chỉ báo nhất quán phát hiện thiên lệch công bố, dù hiệu ứng I→P dương vẫn tồn tại sau hiệu chỉnh.

**Kiểm định hồi quy Egger** (SE làm biến điều tiết): *b* = 0,487 (*SE* = 0,251, *p* = 0,052), chỉ vừa trên ngưỡng α = 0,05 thông thường; tiêu chí này không đạt ý nghĩa thống kê, và bất đối xứng phễu theo riêng kiểm định Egger không được xác nhận.

**Tương quan hạng Begg** (τ Kendall): τ = −0,132, *p* = 0,001, bất đối xứng phễu có ý nghĩa; các nghiên cứu với sai số chuẩn lớn hơn (*n* nhỏ hơn) báo cáo cỡ hiệu ứng thấp hơn có hệ thống, nhất quán với thiên lệch công bố chống lại các phát hiện không hoặc âm.

**Cắt-và-điền**: quy nạp *k* = 57 nghiên cứu khuyết (phía trái); *r̄* tổng hợp hiệu chỉnh = 0,035 (95% CI [0,018, 0,051]), một cận dưới thận trọng. Hiệu ứng vẫn dương và có ý nghĩa nhưng suy giảm đáng kể so với ước lượng thô (0,074 → 0,035).

**Số an toàn *N*** (Rosenthal, 1991): *N* = 44.782, vượt xa tiêu chí 5*k* + 10 = 1.195; ngay cả dưới các giả định nén công bố cực đoan, một hiệu ứng nhỏ không đáng kể cũng sẽ đòi hỏi 44.782 nghiên cứu không chưa công bố, điều khó tin.

Hiệu chỉnh cắt-và-điền (*k* = 57 được quy nạp, *r* hiệu chỉnh = 0,035) là ước lượng hiệu chỉnh thiên lệch thận trọng nhất và đại diện cho một giảm đáng kể so với *r* thô = 0,074. Cùng với tính dị biệt chưa giải thích đáng kể (*I*² = 62,5%) và các kiểm định biến điều tiết không có ý nghĩa (§§4.3–4.5), bằng chứng thiên lệch công bố gợi ý rằng hiệu ứng I→P trung bình biểu kiến bị phình lên trong văn liệu đã công bố. Hiệu ứng dân số thực có thể gần *r* ≈ 0,035 hơn.

Hình 5: Biểu đồ phễu với các nghiên cứu quy nạp bằng cắt-và-điền

*Hình 5.* Biểu đồ phễu của cỡ hiệu ứng đối với sai số chuẩn. Vòng tròn rỗng = nghiên cứu gốc; vòng tròn đặc = nghiên cứu quy nạp bằng cắt-và-điền (*k* = 57). Bất đối xứng phía trái đáng kể có thể thấy rõ; hiệu ứng tổng hợp hiệu chỉnh là *r* = 0,035.

### 4.7 Độ vững

| Kiểm định | K | *r̄* | 95% CI | Ghi chú |
|---|---|---|---|---|
| Phân tích chính | 288 | 0,074 | [0,060, 0,088] | Nền |
| Chỉ *r* xác nhận (loại ước tính) | 240 | 0,077 | [0,059, 0,094] | Nhất quán |
| Loại *n* < 30 | 285 | 0,073 | [0,059, 0,088] | Nhất quán |
| Chỉ hiệu quả ACC | 246 | 0,075 | [0,059, 0,091] | Nhất quán |
| Chỉ thước đo DOI FSTS | 137 | 0,060 | [0,041, 0,078] | Suy giảm nhưng dương |
| Ước lượng DL (hai cấp) | 288 | 0,074 | [0,061, 0,086] | Δ*r* < 0,01 so với ba cấp |
| Khoảng bỏ-một-nghiên-cứu | 288 | [0,071, 0,075] | | 0/288 đổi hướng |

*r* nền = 0,074 vững qua tất cả các kiểm định độ nhạy. Khoảng bỏ-một-nghiên-cứu [0,071, 0,075] xác nhận không có nghiên cứu đơn lẻ nào chi phối kết quả. Ước lượng DL hai cấp cho ước lượng điểm giống hệt (0,074), xác nhận rằng lồng ba cấp thêm độ chính xác mà không làm thiên lệch hiệu ứng tổng hợp. Giới hạn chỉ-FSTS (*r̄* = 0,060) là kiểm định thận trọng nhất và vẫn dương có ý nghĩa, gợi ý rằng tính dị biệt thao tác hóa DOI một phần làm phình hiệu ứng tổng hợp khi các thước đo DOI rộng hơn được đưa vào.

Hình 4: Độ nhạy bỏ-một-nghiên-cứu, khoảng *r̄* tổng hợp qua các vòng lặp bỏ-một-nghiên-cứu

*Hình 4.* Phân tích độ nhạy bỏ-một-nghiên-cứu. Mỗi điểm là *r̄* tổng hợp với 95% CI sau khi loại một nghiên cứu. Khoảng hẹp xác nhận không có nghiên cứu đơn lẻ nào chi phối kết quả.

## 5. Thảo luận

### 5.1 Đồng nhất với bằng chứng cấp quốc gia

Kết quả nền phân tích tổng hợp (*r* = 0,074, *k* = 238, 49 nền kinh tế) nhất quán với bằng chứng cấp quốc gia từ khắp tập nghiên cứu toàn cầu, bao gồm các nghiên cứu sơ cấp châu Á–Thái Bình Dương làm cơ sở cho kết quả nền ICBEF 2025 (Do & Phan, 2024). Hiệu ứng tổng hợp dương và có ý nghĩa, xác nhận rằng các doanh nghiệp thâm dụng xuất khẩu có xu hướng vượt trội so với các đối thủ tập trung nội địa ngay cả sau khi điều chỉnh quy mô, tuổi và ngành doanh nghiệp.

**Bối cảnh Advanced-I (Nhóm I, k = 139; *r̄* = 0,079):** Trung bình Nhóm I (*r̄* = 0,079) là ước lượng đáng tin cao nhất và nhất quán định hướng với lý thuyết bổ sung thể chế: thực thi hợp đồng mạnh, bảo hộ sở hữu trí tuệ và gánh nặng ngoại quốc thấp (Zaheer, 1995) cho phép doanh nghiệp duy trì quốc tế hóa năng suất mà không gặp các hình phạt chi phí phối hợp thấy được trong môi trường yếu hơn (North, 1990; Peng et al., 2008). Tuy nhiên, độ lớn nhỏ hơn nhiều so với CIMT dự đoán, và khác biệt I→III không có ý nghĩa thống kê (*p* = 0,502).

**Bối cảnh Emerging (Nhóm III, k = 90; *r̄* = 0,068):** Nhóm Emerging cho *r̄* = 0,068, thấp hơn định hướng so với nhóm Advanced, nhất quán với lập luận ma sát thể chế của CIMT. Ở cấp nghiên cứu sơ cấp, Do & Phan (2025) ghi nhận một hệ số DOI tổng hợp âm trên 380 doanh nghiệp WBES Ấn Độ (ước lượng FGLS), với kinh nghiệm quản lý và lãnh đạo nữ trong ban điều hành cao cấp là các yếu tố điều tiết dương, một mẫu hình nhất quán với dự đoán của CIMT rằng các nguồn lực bù trừ cấp doanh nghiệp một phần bù đắp ma sát thể chế trong môi trường Emerging.

**Bối cảnh Frontier (FR, k = 3; *r̄* = 0,349):** Ước lượng Frontier *k* = 3 bị chi phối bởi một nghiên cứu ngoại lai (Pouresmaeili et al., 2018, *r* = 0,69, *n* = 226 doanh nghiệp chế tạo Iran). Ước lượng này không thể diễn giải như một hiệu ứng I→P Frontier đáng tin; nó thay vào đó phản ánh tính gần-như-bất-khả của việc rút kết luận phân tích tổng hợp khi chỉ ba nghiên cứu lấp đầy một ô chế độ. Hiệu ứng I→P Frontier thực có thể bằng không, dương hoặc âm, cần *k* lớn hơn.

**Tổng hợp:** H1 được xác nhận, kiểm định Q_M giữa-chế-độ ICRV (*Q*_M = 17,35, *p* = 0,002) có ý nghĩa thống kê, xác lập rằng cỡ hiệu ứng I→P biến thiên qua các chế độ thể chế như lý thuyết hóa. Ý nghĩa của Q_M bị chi phối bởi tương phản Frontier *k* = 3 thay vì bởi các tương phản theo cặp đủ năng lực qua các ô Advanced/Upper-middle/Emerging, nên các mệnh đề gradient định hướng E1a và E1b không được xác nhận bằng phân tích tổng hợp trong mẫu hiện tại. Phát hiện được chứng thực là hiệu ứng I→P nền (*r* = 0,074) nhìn chung nhất quán qua các nhóm chế độ đủ dày (I, II, III, MX), và độ lớn của khoảng cách Advanced-Emerging (*r̄* = 0,079 so với 0,068) không đạt ý nghĩa, một kết quả giới hạn, thay vì bác bỏ, dự đoán gradient thể chế của CIMT.

### 5.2 Đóng góp lý thuyết

**Đóng góp 1: Phân tích tổng hợp I→P đại diện toàn cầu lớn nhất tới nay.** MARA ba cấp với *k* = 238 nghiên cứu từ 49 nền kinh tế (*K* = 288 hiệu ứng) là tổng hợp định lượng toàn diện nhất của bằng chứng I→P áp dụng mô hình ba cấp, mở rộng kết quả nền châu Á–Thái Bình Dương ICBEF 2025 (*k* = 113) thêm 124 nghiên cứu với một tập đã mã hóa ICRV bao trùm toàn cầu. Mô hình ba cấp phân chia đúng phương sai trong-nghiên-cứu và giữa-nghiên-cứu, và *r* nền = 0,074 tái lập các ước lượng trước trong khi vẫn vững qua bảy kiểm định độ nhạy.

**Đóng góp 2: Kiểm định phân tích tổng hợp đầu tiên về các biến điều tiết ICRV, cDAI và DPL.** Bài báo này là đầu tiên kiểm định chính thức chế độ thể chế ICRV, áp dụng số quốc gia (cDAI) và giai đoạn Vòng đời Nghịch lý Số như các biến điều tiết trong một MARA ba cấp. H1 (kiểm định Q_M giữa-chế-độ) được xác nhận (*Q*_M = 17,35, *p* = 0,002), xác lập rằng cỡ hiệu ứng I→P biến thiên có hệ thống qua các chế độ thể chế. Tuy nhiên, các mệnh đề gradient định hướng (E1a/E1b) và các giả thuyết cDAI và DPL (H2, H3) không được xác nhận dưới kiểm định giữa-nhóm nghiêm ngặt. Các kết quả này đặt ra các ranh giới có ý nghĩa lý thuyết: mẫu *k* = 238 thiếu đủ biến thiên giữa-chế-độ (đặc biệt Frontier, *k* = 3; SIDS, *k* = 0) để phát hiện gradient CIMT, và cDAI cùng giai đoạn DPL không giải thích tính dị biệt giữa-nghiên-cứu trong tập hiện tại. Các tái lập tương lai với lấy mẫu cấp chế độ có mục tiêu nên kiểm định liệu gradient có nổi lên với đại diện giữa-chế-độ phong phú hơn hay không.

**Đóng góp 3: Xác định thiên lệch công bố đáng kể.** Ước lượng hiệu chỉnh cắt-và-điền (*r* = 0,035, *k* = 57 nghiên cứu quy nạp) và τ Begg có ý nghĩa (*p* = 0,001) cùng cho thấy văn liệu I→P có một thiên lệch công bố dương đáng kể. Hiệu ứng tổng hợp thô (*r* = 0,074) có khả năng phóng đại hiệu ứng nhân quả trung bình thực khoảng 50–100%, với ước lượng hiệu chỉnh thiên lệch (*r* = 0,035) cung cấp một cận dưới thận trọng. Phát hiện này, từ MARA ba cấp toàn diện toàn cầu nhất về I→P tới nay, là đóng góp lý thuyết khả thi nhất: nó gợi ý rằng "mối quan hệ I→P dương" được trích dẫn rộng rãi của văn liệu IB một phần là tạo tác của công bố chọn lọc thay vì một hiện tượng vững chắc.

### 5.3 Hàm ý quản lý và chính sách

Việc không xác nhận ba biến điều tiết giả thuyết giới hạn các kết luận quy chuẩn mạnh về chế độ thể chế hay bối cảnh số, nhưng phát hiện nền và kết quả thiên lệch công bố mang ý nghĩa thực tiễn.

**Cho doanh nghiệp ở mọi bối cảnh thể chế:** Kết quả nền hiệu chỉnh thiên lệch (*r* = 0,035) thay vì *r* thô = 0,074 là ước lượng tốt hơn về lợi tức hiệu quả trung bình thực của quốc tế hóa. Các doanh nghiệp kỳ vọng lợi ích năng suất lớn từ riêng việc thâm dụng xuất khẩu có khả năng sẽ thất vọng, vì văn liệu đã công bố báo cáo quá mức có hệ thống các hiệu ứng dương. Chiến lược quốc tế hóa nên được dẫn dắt bởi các lợi thế cạnh tranh đặc thù doanh nghiệp và học hỏi đặc thù thị trường, không phải bởi giả định rằng "quốc tế hóa cải thiện hiệu quả" một cách vô điều kiện.

**Cho nhà nghiên cứu:** Thiên lệch công bố đáng kể (*k* = 57 quy nạp, *r* hiệu chỉnh = 0,035) là một lời kêu gọi cho các nghiên cứu có đăng ký trước với báo cáo giả thuyết không rõ ràng. Thực hành công bố trong văn liệu I→P, nơi các hiệu ứng dương được đại diện quá mức, có thể đang bóp méo hiểu biết của lĩnh vực về khi nào và tại sao quốc tế hóa giúp ích. Đăng ký OSF và áp dụng MARA ba cấp với hiệu chỉnh cắt-và-điền nên trở thành chuẩn trong các phân tích tổng hợp I→P tương lai.

**Cho nhà hoạch định chính sách:** Khoảng cách Advanced–Emerging của ICRV (*r̄* = 0,079 so với 0,068, không có ý nghĩa) không đủ lớn để biện minh chất lượng thể chế là yếu tố quyết định chính của năng suất dẫn dắt bởi xuất khẩu. Các chương trình xúc tiến xuất khẩu nên nhắm vào năng lực cấp doanh nghiệp (công nghệ, quản lý) ngang với cải cách thể chế, cho rằng gradient thể chế-hiệu quả không được xác nhận bằng phân tích tổng hợp ở cỡ mẫu hiện tại.

### 5.4 Hạn chế và ranh giới suy luận

Ba hạn chế giới hạn các suy luận có sẵn từ nghiên cứu này:

**(a) Điều không thể kết luận:** (1) Nhóm con SIDS (*k* ≈ 5, CI rộng) không cho phép kết luận dứt khoát về giả thuyết "hình phạt cưỡng bức", cần một tìm kiếm có mục tiêu cho các nghiên cứu sơ cấp tập trung SIDS (như nêu trong Phụ lục B) trước khi các hiệu ứng SIDS phân tích tổng hợp đạt độ chính xác. (2) Điều tiết liên kết cDAI × ICRV (tương tác ba chiều) thiếu năng lực trong tập dữ liệu hiện tại (*k* mỗi ô < 20); ước lượng điểm được cung cấp nhưng khoảng tin cậy rộng. (3) Tất cả cỡ hiệu ứng là mặt cắt ngang hoặc bảng ở cấp nghiên cứu, không có hồi quy phân tích tổng hợp dọc nào có thể phân biệt hiệu ứng chọn lọc với lợi tức học hỏi nhân quả của quốc tế hóa.

**(b) Biện pháp khắc phục phương pháp cho công việc tương lai:** Phân tích tổng hợp bảng với cỡ hiệu ứng dọc từ dữ liệu doanh nghiệp riêng lẻ sẽ cho phép phân rã nhân quả (Sutton & Higgins, 2008). Hồi quy phân tích tổng hợp Bayes với tiên nghiệm cung cấp thông tin từ các nghiên cứu bảng cấp quốc gia của các nền kinh tế frontier sẽ siết chặt các ước lượng chế độ SIDS.

**(c) Ranh giới của phân loại ICRV:** Phân loại 5 chế độ dùng Pháp quyền WGI làm bộ phân loại chính. Các bộ phân loại dựa trên thể chế thay thế (Tự do Kinh tế của Heritage Foundation, CPI của Transparency International) cho các gán chế độ nhìn chung nhất quán nhưng khác biệt ở biên với các trường hợp ranh giới Chế độ II/III.

## 6. Kết luận

Bài báo này trình bày MARA ba cấp đầu tiên về mối quan hệ quốc tế hóa–hiệu quả rút từ một tập đại diện toàn cầu, mở rộng kết quả nền châu Á–Thái Bình Dương ICBEF 2025 từ *k* = 113 lên *k* = 238 nghiên cứu từ 49 nền kinh tế (*K* = 288 hiệu ứng) và giới thiệu ba biến điều tiết mới cho kiểm định phân tích tổng hợp chính thức: chế độ thể chế ICRV, áp dụng số cấp quốc gia (cDAI) và giai đoạn Vòng đời Nghịch lý Số (DPL). Hiệu ứng tổng hợp ba cấp (*r* = 0,074, 95% CI [0,060, 0,088], *I*²_total = 62,5%) xác nhận một mối quan hệ I→P dương nhỏ nhưng nhất quán trên phạm vi toàn cầu, vững qua bảy kiểm định độ nhạy.

H1 (kiểm định Q_M giữa-chế-độ ICRV) được xác nhận (*Q*_M = 17,35, *p* = 0,002), xác lập rằng cỡ hiệu ứng I→P biến thiên có hệ thống qua các chế độ thể chế. Tuy nhiên, gradient định hướng (E1a: Advanced lớn nhất; E1b: Frontier nhỏ nhất) không thể xác nhận bằng phân tích tổng hợp tại *k* = 3 Frontier, và các biến điều tiết cDAI (H3: *Q*_M = 1,34, *p* = 0,513) và giai đoạn DPL (H2: *Q*_M = 0,62, *p* = 0,734) không giải thích tính dị biệt giữa-nghiên-cứu trong mẫu hiện tại. Gradient thể chế CIMT (E1a/E1b), khuếch đại hạ tầng số (H3) và điều tiết thời gian DPL (H2) vẫn có cơ sở lý thuyết nhưng chưa được xác nhận thực nghiệm tại *k* = 238, các kết quả không nên định hướng cho các tái lập có đăng ký trước tương lai với lấy mẫu cấp chế độ có mục tiêu.

Phát hiện thực nghiệm thực chất nhất là thiên lệch công bố đáng kể: cắt-và-điền quy nạp *k* = 57 nghiên cứu khuyết, làm giảm hiệu ứng tổng hợp hiệu chỉnh thiên lệch xuống *r* = 0,035 (95% CI [0,018, 0,051]), dương nhưng suy giảm đáng kể. Điều này gợi ý rằng văn liệu đã công bố của lĩnh vực I→P đại diện quá mức các kết quả dương, và rằng lợi tức hiệu quả trung bình thực của quốc tế hóa gần *r* ≈ 0,035 hơn các con số thường được trích dẫn trong khoảng 0,07–0,10. Bài toán dị biệt (*I*² = 62,5%) vẫn phần lớn chưa được giải quyết, với phương sai trong-nghiên-cứu (Cấp 2, 54,1%) chi phối phương sai giữa-nghiên-cứu (Cấp 3, 8,4%), gợi ý rằng các lựa chọn thao tác hóa DOI và thước đo hiệu quả trong các bài báo là nguồn dị biệt quan trọng hơn các khác biệt thể chế giữa các quốc gia.

**Hạn chế.** Năm ràng buộc suy luận giới hạn các kết luận này. Thứ nhất, ba giả thuyết biến điều tiết không được xác nhận trong tập *k* = 238 hiện tại; điều này có thể phản ánh *k* cấp chế độ không đủ (Frontier: *k* = 3; SIDS: *k* = 0) thay vì các hiệu ứng không thực sự. Cần một tìm kiếm WoS/Scopus chính thức nhắm vào bối cảnh Frontier và SIDS trước khi kết quả không ICRV có thể diễn giải là dứt khoát. Thứ hai, dị thường nhóm Frontier (*k* = 3, *r̄* = 0,349, bị chi phối bởi Pouresmaeili et al. 2018) là động lực duy nhất của ý nghĩa ICRV; công việc tương lai nên đánh giá lại mã hóa này và tìm kiếm thêm các nghiên cứu chế độ Frontier. Thứ ba, cDAI được đo ở cấp nghiên cứu dùng điểm Chỉ số Áp dụng Số của Ngân hàng Thế giới theo quốc gia-năm (chính) hoặc Chỉ số Phát triển Số ITU (phụ), không phải tái lập trực tiếp các chỉ báo cấp doanh nghiệp WBES dùng trong các nghiên cứu sơ cấp đồng hành; bất kỳ sai số có hệ thống nào trong gán DAI theo quốc gia-năm, chẳng hạn từ lệch phiên bản giữa thời kỳ dữ liệu của nghiên cứu và năm tham chiếu của điểm DAI, có thể làm suy giảm hệ số điều tiết. Thứ tư, tìm kiếm hệ thống được giới hạn ở các công bố tiếng Anh; các nghiên cứu phi-tiếng-Anh (Trung Quốc, Nhật Bản, Hàn Quốc, Đông Nam Á) bị thiếu đại diện, có thể làm thiên lệch phân phối chế độ về phía các nền kinh tế Advanced. Thứ năm, độ tin cậy được xác lập trên một mẫu con mã hóa kép 20% (*k* = 47 nghiên cứu), với hai tác giả mã hóa độc lập và sự đồng thuận được báo cáo trong Bảng 3.1; 80% còn lại được tác giả thứ nhất mã hóa đơn đối với sổ mã, điều này, dù chuẩn mực cho các tổng hợp bị ràng buộc nguồn lực, không thể được kiểm chứng độc lập.

**Nghiên cứu tương lai.** Ba hướng theo sau trực tiếp từ các phát hiện biến điều tiết không có ý nghĩa. Thứ nhất, một tìm kiếm hệ thống WoS/Scopus chính thức nhắm vào các nghiên cứu I→P của nền kinh tế Frontier và SIDS (chuỗi tìm kiếm có mục tiêu, Phụ lục B) sẽ mở rộng *k* Frontier từ 3 lên tiềm năng 20–40 nghiên cứu, cho phép một kiểm định có ý nghĩa về ô Frontier của ICRV. Thứ hai, một tái lập có đăng ký trước các giả thuyết biến điều tiết ICRV, cDAI và DPL, với phân tích năng lực rõ ràng cho mỗi ô chế độ và đăng ký OSF, sẽ cung cấp một kiểm định dứt khoát về việc liệu các biến điều tiết này có đạt ý nghĩa trong một tập *k* ≥ 400 hay không. Thứ ba, phát hiện thiên lệch công bố đáng kể (*k* = 57 quy nạp, *r* hiệu chỉnh = 0,035) thúc đẩy một kiểm toán thiên lệch công bố chuyên biệt: khảo sát các nhà nghiên cứu I→P về các kết quả không chưa công bố, và phân tích tổng hợp văn liệu xám và luận án, sẽ giới hạn hiệu ứng dân số thực chính xác hơn riêng cắt-và-điền.

## Tài trợ

Nghiên cứu này không nhận tài trợ cụ thể từ bất kỳ cơ quan tài trợ nào trong khu vực công, thương mại hay phi lợi nhuận.

## Xung đột lợi ích

Các tác giả tuyên bố không có xung đột lợi ích.

## Tính khả dụng của dữ liệu

Cơ sở dữ liệu nghiên cứu đã mã hóa (`forest_data.csv`), các kịch bản phân tích R (`metafor`) và quy trình đăng ký OSF có sẵn từ tác giả liên hệ theo yêu cầu hợp lý. Bảng kiểm PRISMA 2020 được cung cấp như tài liệu bổ sung.

## Công bố về AI Tạo sinh và Công nghệ Hỗ trợ AI trong Quá trình Viết

Trong quá trình chuẩn bị công trình này, các tác giả đã dùng hai công cụ phần mềm, mỗi công cụ dưới sự kiểm soát và kiểm chứng đầy đủ của con người. Thứ nhất, một công cụ hỗ trợ mô hình ngôn ngữ lớn được xây dựng chuyên biệt (M-AIDA, dùng Anthropic Claude) được dùng để hỗ trợ trích xuất cỡ hiệu ứng và chuyển đổi thống kê từ các nghiên cứu sơ cấp; mọi giá trị do công cụ đề xuất đều được kiểm tra độc lập, sửa khi cần và khóa cố định bởi Nghiên cứu viên Chính trước khi nhập vào cơ sở dữ liệu phân tích. Thứ hai, Grammarly được dùng để sửa chính tả, ngữ pháp và dấu câu trong văn bản của chính tác giả. Không có công cụ AI tạo sinh nào lựa chọn nghiên cứu, ra quyết định đủ điều kiện, thực hiện phân tích thống kê hay tạo bất kỳ nội dung diễn giải hoặc văn bản nào; các tác giả đã rà soát tất cả đầu ra và chịu trách nhiệm hoàn toàn về nội dung của công bố.

## Tài liệu tham khảo

Aguinis, H., Dalton, D. R., Bosco, F. A., Pierce, C. A., & Dalton, C. M.
(2011). Meta-analytic choices and judgment calls: Implications for
theory and research. *Journal of Management, 37*(1), 5–38.

Arte, P., & Larimo, J. (2022). Moderating influence of product
diversification on the internationalization-performance relationship:
Insights from meta-analysis. *Journal of Business Research, 139*,
1408–1423.

Barney, J. (1991). Firm resources and sustained competitive advantage.
*Journal of Management, 17*(1), 99–120.

Bausch, A., & Krist, M. (2007). The effect of context-related moderators
on the internationalization–performance relationship: Evidence from
meta-analysis. *Management International Review, 47*(3), 319–347.

Begg, C. B., & Mazumdar, M. (1994). Operating characteristics of a rank
correlation test for publication bias. *Biometrics, 50*(4), 1088–1101.

Bharadwaj, A., El Sawy, O. A., Pavlou, P. A., & Venkatraman, N. (2013).
Digital business strategy: Toward a next generation of insights. *MIS
Quarterly, 37*(2), 471–482.

Borenstein, M., Hedges, L. V., Higgins, J. P. T., & Rothstein, H. R.
(2021). *Introduction to meta-analysis* (2nd ed.). Wiley.

Brynjolfsson, E., Rock, D., & Syverson, C. (2021). The productivity
J-curve: How intangibles complement general purpose technologies.
*American Economic Journal: Macroeconomics, 13*(1), 333–372.

Bustamante, C. V., Mingo, S., & Matusik, S. F. (2022). Institutions,
digital capabilities and the internationalization of SMEs. *Journal of
International Business Studies, 53*(3), 524–546.

Cheung, M. W.-L. (2014). Modeling dependent effect sizes with
three-level meta-analyses. *Psychological Methods, 19*(2), 211–226.

Cohen, J. (1988). *Statistical power analysis for the behavioral
sciences* (2nd ed.). Lawrence Erlbaum.

Cooper, H. (2010). *Research synthesis and meta-analysis: A step-by-step
approach* (4th ed.). Sage.

David, P. A. (1990). The dynamo and the computer: An historical
perspective on the modern productivity paradox. *American Economic
Review, 80*(2), 355–361.

Do, T. H., & Phan, A. T. (2024, December). *Internationalization and
firm performance: A meta-analysis review* [Paper presentation]. The
Sixth International Conference on Sustainable Development in Economics,
Business, and Finance (ICBEF).

Do, T. H., & Phan, A. T. (2025). Internationalization and firm
performance of firms in India: The role of top management. In M.
Bartekova (Ed.), *International business research: Traditional and
creative approaches*. IntechOpen.
<https://doi.org/10.5772/intechopen.1011012>

Duval, S., & Tweedie, R. (2000). Trim and fill: A simple
funnel-plot-based method of testing and adjusting for publication bias
in meta-analysis. *Biometrics, 56*(2), 455–463.

Egger, M., Smith, G. D., Schneider, M., & Minder, C. (1997). Bias in
meta-analysis detected by a simple, graphical test. *BMJ, 315*(7109),
629–634.

Hedges, L. V., & Olkin, I. (1985). *Statistical methods for
meta-analysis*. Academic Press.

Helpman, E., Melitz, M. J., & Yeaple, S. R. (2004). Export versus FDI
with heterogeneous firms. *American Economic Review, 94*(1), 300–316.

Jacquemin, A. P., & Berry, C. H. (1979). Entropy measure of
diversification and corporate growth. *Journal of Industrial Economics,
27*(4), 359–369.

Jensen, M. C., & Meckling, W. H. (1976). Theory of the firm: Managerial
behavior, agency costs and ownership structure. *Journal of Financial
Economics, 3*(4), 305–360.

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process
of the firm: A model of knowledge development and increasing foreign
market commitments. *Journal of International Business Studies, 8*(1),
23–32.

Katz, R., & Callorda, F. (2018). *The economic contribution of
broadband, digitization and ICT regulation*. ITU Telecommunication
Development Sector.

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road
map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Deligonul, S., Perryy, M. Z., & Cavusgil,
S. T. (2012). A multilevel examination of the drivers of firm
multinationality: A meta-analysis. *Journal of Management, 38*(2),
502–530.

Kraus, S., Breier, M., Lim, W. M., Dabić, M., Kumar, S., Kanbach, D.,
Mukherjee, D., Corvello, V., Piñeiro-Chousa, J., Liguori, E.,
Palacios-Marqués, D., Schiavone, F., Ferraris, A., Fernandes, C., &
Ferreira, J. J. (2022). Literature reviews as independent studies:
Guidelines for academic practice. *Review of Managerial Science, 16*(8),
2577–2595.

Kogut, B., & Zander, U. (1993). Knowledge of the firm and the
evolutionary theory of the multinational corporation. *Journal of
International Business Studies, 24*(4), 625–645.

Lakens, D., Scheel, A. M., & Isager, P. M. (2020). Equivalence testing
for psychological research: A tutorial. *Advances in Methods and
Practices in Psychological Science, 1*(2), 259–269.

Landis, J. R., & Koch, G. G. (1977). The measurement of observer
agreement for categorical data. *Biometrics, 33*(1), 159–174.

Marano, V., Arregle, J.-L., Hitt, M. A., Spadafora, E., & van Essen, M.
(2016). Home country institutions and the
internationalization-performance relationship: A meta-analytic review.
*Journal of Management, 42*(5), 1075–1110.

North, D. C. (1990). *Institutions, institutional change and economic
performance*. Cambridge University Press.

Orwin, R. G. (1983). A fail-safe N for effect size in meta-analysis.
*Journal of Educational Statistics, 8*(2), 157–159.

Page, M. J., McKenzie, J. E., Bossuyt, P. M., Boutron, I., Hoffmann, T.
C., Mulrow, C. D., Shamseer, L., Tetzlaff, J. M., Akl, E. A., Brennan,
S. E., Chou, R., Glanville, J., Grimshaw, J. M., Hróbjartsson, A., Lalu,
M. M., Li, T., Loder, E. W., Mayo-Wilson, E., McDonald, S., … Moher, D.
(2021). The PRISMA 2020 statement: An updated guideline for reporting
systematic reviews. *BMJ, 372*, n71. <https://doi.org/10.1136/bmj.n71>

Paternoster, R., Brame, R., Mazerolle, P., & Piquero, A. (1998). Using
the correct statistical test for the equality of regression
coefficients. *Criminology, 36*(4), 859–866.

Peng, M. W., Wang, D. Y. L., & Jiang, Y. (2008). An institution-based
view of international business strategy: A focus on emerging economies.
*Journal of International Business Studies, 39*(5), 920–936.

Peterson, R. A., & Brown, S. P. (2005). On the use of beta coefficients
in meta-analysis. *Journal of Applied Psychology, 90*(1), 175–181.

Raudenbush, S. W., & Bryk, A. S. (2002). *Hierarchical linear models:
Applications and data analysis methods* (2nd ed.). Sage.

Rosenthal, R. (1991). *Meta-analytic procedures for social research*
(rev. ed.). Sage.

Rosenthal, R. (1994). Parametric measures of effect size. In H. Cooper &
L. V. Hedges (Eds.), *The handbook of research synthesis* (pp. 231–244).
Sage.

Schwens, C., Zapkau, F. B., Brouthers, K. D., & Hollender, L. (2018).
Limits to outsourcing: A meta-analysis and empirical investigation.
*Journal of International Business Studies, 49*(6), 682–703.

Stanley, T. D., & Doucouliagos, H. (2014). Meta-regression
approximations to reduce publication selection bias. *Research Synthesis
Methods, 5*(1), 60–78.

Stallkamp, M., & Schotter, A. P. J. (2021). Platforms without borders?
The international strategies of digital platform firms. *Global Strategy
Journal, 11*(1), 58–80.

Sutton, A. J., & Higgins, J. P. T. (2008). Recent developments in
meta-analysis. *Statistics in Medicine, 27*(5), 625–650.

Van den Noortgate, W., López-López, J. A., Marín-Martínez, F., &
Sánchez-Meca, J. (2013). Three-level meta-analysis of dependent effect
sizes. *Behavior Research Methods, 45*(2), 576–594.

Verhoef, P. C., Broekhuizen, T., Bart, Y., Bhattacharya, A., Qi Dong,
J., Fabian, N., & Haenlein, M. (2021). Digital transformation: A
multidisciplinary reflection and research agenda. *Journal of Business
Research, 122*, 889–901.

Vevea, J. L., & Woods, C. M. (2005). Publication bias in research
synthesis: Sensitivity analysis using a priori weight functions.
*Psychological Methods, 10*(4), 428–443.

Viechtbauer, W. (2010). Conducting meta-analyses in R with the metafor
package. *Journal of Statistical Software, 36*(3), 1–48.

Wernerfelt, B. (1984). A resource-based view of the firm. *Strategic
Management Journal, 5*(2), 171–180.

World Bank. (2023). *Worldwide Governance Indicators*.
<https://info.worldbank.org/governance/wgi/>

Wu, J., Wang, C., Hong, J., Piperopoulos, P., & Zhuo, S. (2022).
Internationalization and innovation performance of emerging market
enterprises: The role of host-country institutional development.
*Journal of World Business, 52*(2), 192–203.

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of
Management Journal, 38*(2), 341–363.

## Phụ lục A, Dòng PRISMA 2020 (Nghiên cứu Được Xác định Qua Phương pháp Khác)

Tập nghiên cứu được lắp ráp qua tìm kiếm hệ thống neo theo trích dẫn thay vì một điều tra cơ sở dữ liệu đơn lẻ; do đó, dòng được báo cáo theo biến thể "studies identified via other methods" (nghiên cứu được xác định qua phương pháp khác) của PRISMA 2020 (Page et al., 2021).

    XÁC ĐỊNH
    ─────────────────────────────────────────────────────────────────
    Nghiên cứu được xác định qua phương pháp khác:
      Quét trích dẫn lùi (danh sách tham khảo của 5 phân tích tổng hợp mỏ neo)
      Quét trích dẫn tiến (Google Scholar trích dẫn 5 mỏ neo, sau 2022)
      Tìm kiếm thủ công (tập của tác giả, 2020–2026): n = 19
      Truy vấn có cấu trúc bổ sung (WoS, Scopus, cơ sở dữ liệu
        chuyên ngành) để kiểm tra độ phủ mạng lưới trích dẫn

    SÀNG LỌC / ĐỦ ĐIỀU KIỆN
    ─────────────────────────────────────────────────────────────────
    Các bản ghi được sàng lọc theo hai giai đoạn đối với tiêu chí đủ điều kiện
    (Mục 3.2): tiêu đề/tóm tắt, rồi toàn văn. Lý do loại trừ toàn văn:
    không có cỡ hiệu ứng chuyển được sang r; quốc tế hóa không được
    đo ở cấp doanh nghiệp; mẫu trùng lặp (bản ghi nhỏ/cũ hơn bị loại);
    phân tích tổng hợp hoặc tổng quan thay vì nghiên cứu sơ cấp;
    kỷ yếu hội thảo, luận văn, working paper hoặc chương sách (văn liệu
    xám được lập tài liệu nhưng loại khỏi mô hình chính).

    BAO GỒM
    ─────────────────────────────────────────────────────────────────
    Nghiên cứu được đưa vào phân tích tổng hợp: k = 238
    Cỡ hiệu ứng đã mã hóa:                      K = 288

Vì việc xác định tiến hành bằng chuỗi trích dẫn, các đếm số điều tra cơ sở dữ liệu theo từng giai đoạn (tổng xác định, đã khử trùng lặp và đếm loại trừ theo từng lý do) không được duy trì như một lần xuất cơ sở dữ liệu đơn lẻ và không được báo cáo như vậy; tập đã tổng hợp (k = 238; K = 288) là cố định và được dữ liệu hậu thuẫn.

*Bảng kiểm PRISMA 2020 (Page et al., 2021) có sẵn từ tác giả liên hệ.*

## Phụ lục B, Quy trình Mã hóa (7 Biến điều tiết)

| Biến điều tiết | Loại biến | Quy tắc mã hóa |
|---|---|---|
| Chế độ ICRV | Phân loại (6 mã) | Pháp quyền WGI, phiên bản 2023: I > +0,80; II: 0–+0,80; III: −0,50–0; SIDS: quốc đảo; V: < −0,50 |
| cDAI | Liên tục (0–1) | Điểm DAI Ngân hàng Thế giới hoặc điểm DDI ITU, theo quốc gia-năm, chuẩn hóa. Nếu không có: Chỉ số Phát triển ICT của ITU (thay thế) |
| Giai đoạn DPL | Phân loại (3) | Precede: năm dữ liệu < 2009; Span: dữ liệu bắc qua 2005–2014; Follow: năm dữ liệu > 2014 |
| Quốc gia gốc | Phân loại (ISO) | Quốc gia mẫu của tác giả đầu; đa quốc gia = "pooled" |
| Ngành | Phân loại (3) | SIC: chế tạo (20–39), dịch vụ (40–89), hỗn hợp/không xác định |
| Thước đo DOI | Phân loại (4) | FSTS; Entropy; Số thị trường; Chỉ số xuyên quốc gia (UNCTAD) |
| Hiệu quả | Phân loại (4) | Kế toán (ROA/ROE/ROS); Thị trường (Tobin's Q); Hỗn hợp; Khác |

## Phụ lục C, Kiểm tra Tính nhất quán: MetaEssentials so với `metafor`

| Thống kê | MetaEssentials 1.5 (ICBEF 2025) | metafor REML (3 cấp, k=238) |
|---|---|---|
| *r* tổng hợp | 0,070 | 0,074 |
| 95% CI | [0,050, 0,090] | [0,060, 0,088] |
| *I*²_total | 87,92% | 62,5% |
| *I*²_(2) trong-nghiên-cứu | | 54,1% |
| *I*²_(3) giữa-nghiên-cứu | | 8,4% |
| *k* nghiên cứu | 113 | 238 |
| *K* hiệu ứng | | 288 |
| σ²_(2) | | 0,00878 |
| σ²_(3) | | 0,00136 |
| Phần mềm | Suurmond et al. (2017) | Viechtbauer (2010) |

*Ghi chú:* Tổng I² thấp hơn trong mô hình ba cấp (62,5% so với 87,92%) phản ánh mẫu *k* = 238 mở rộng và cấu trúc ba cấp phân chia phương sai qua các cấp một cách đúng đắn. 95% CI hẹp hơn phản ánh sự tăng độ chính xác từ 238 so với 113 nghiên cứu. Mô hình ba cấp được ưu tiên về mặt lý thuyết vì nó tính đến nhiều cỡ hiệu ứng lồng trong các nghiên cứu.

*Số từ (không bao gồm bảng, tài liệu tham khảo, phụ lục): ≈ 6.900 từ*

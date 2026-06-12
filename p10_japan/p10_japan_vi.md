# Tại biên trên của gradient thể chế: Quốc tế hóa và hiệu quả doanh nghiệp trong đợt Khảo sát Doanh nghiệp Ngân hàng Thế giới đầu tiên của Nhật Bản

*(Bản tiếng Việt của bản thảo P10; bản gửi tạp chí là bản tiếng Anh trong `submission/abm_package/`.)*

## Tóm tắt

**Mục đích.** Nhật Bản lần đầu tiên được đưa vào Khảo sát Doanh nghiệp của Ngân hàng Thế giới (WBES) năm 2025, khép lại khoảng trống lớn cuối cùng về dữ liệu cấp doanh nghiệp so sánh được của châu Á tiên tiến. Nghiên cứu khai thác đợt khảo sát khai mở này (N = 2.168 cơ sở kinh doanh) để kiểm định cách quan hệ quốc tế hóa – hiệu quả (I–P) vận hành tại biên trên của gradient thể chế, nơi lý thuyết dự đoán chữ U ngược quen thuộc phải duỗi thẳng về gần tuyến tính. **Thiết kế/phương pháp.** Năng suất lao động, ln(doanh thu hằng năm trên một lao động thường xuyên), winsorize tại phân vị 1 và 99, được hồi quy theo cường độ xuất khẩu (FSTS, xuất khẩu trực tiếp cộng gián tiếp trên doanh thu) và bình phương của nó, với hiệu ứng cố định ngành và sai số chuẩn vững HC1, theo chuỗi mô hình phân tầng bổ sung dần sở hữu nước ngoài, tuổi doanh nghiệp, giới tính nhà quản trị, năng lực công nghệ (TCI) và chấp nhận số (DAI). **Kết quả.** Hiệu ứng tuyến tính của cường độ xuất khẩu dương và có ý nghĩa (β = +0,671; p < 0,001). Số hạng bậc hai không bao giờ có ý nghĩa (M2: β₂ = −0,606; p = 0,323) và điểm uốn đại số (90–108% doanh thu) nằm ngoài miền quan sát: trong phạm vi dữ liệu, quốc tế hóa nhiều hơn là tốt hơn một cách đơn điệu. Năng lực công nghệ (+0,100; p < 0,001) và chấp nhận số (+0,110; p = 0,028) nâng mặt bằng hiệu quả nhưng không uốn đường cong, nhất quán với trạng thái bão hòa Tier-1 ở nền kinh tế có 83,8% cơ sở vận hành website. Hai quy luật đặc thù Nhật Bản: phần bù trường thọ doanh nghiệp (ln tuổi: +0,073; p = 0,007) nhất quán với truyền thống *shinise*, và hệ số âm của nữ quản lý cấp cao (−0,170; p = 0,010) trong nền kinh tế chỉ có 7,3% cơ sở do nữ điều hành cấp cao. **Đóng góp.** Đây là ước lượng I–P cấp doanh nghiệp đầu tiên cho Nhật Bản trên bộ công cụ WBES và là kiểm định đầu tiên cho dự đoán biên trên của khung I–P phụ thuộc thể chế trên đợt khảo sát khai mở của một nền kinh tế. Sự duỗi thẳng của đường cong ở chế độ thể chế mạnh nhất trùng khớp bằng chứng độc lập từ Singapore và hoàn tất bức tranh ba vùng, chữ U ngược ở các chế độ chuyển đổi, gần tuyến tính ở biên trên, tan rã ở biên dưới, đã ghi nhận trên 50 nền kinh tế châu Á và Thái Bình Dương.

**Từ khóa:** quốc tế hóa – hiệu quả; cường độ xuất khẩu; Nhật Bản; WBES; bối cảnh thể chế; chấp nhận số; năng lực công nghệ.

## 1. Giới thiệu

Câu hỏi nghiên cứu được xác định sắc nét: **quan hệ I–P tại biên trên của gradient thể chế có vận hành đúng như lý thuyết phụ thuộc thể chế dự đoán không?** Dự đoán rất cụ thể: nơi chất lượng thể chế cao nhất, chi phí giao dịch xuyên biên giới thấp nhất và hệ sinh thái dịch vụ hỗ trợ dày nhất, nhánh đi xuống của chữ U ngược phải bị đẩy ra ngoài miền quan sát của cường độ xuất khẩu. Về mặt thực nghiệm: số hạng bậc hai không phân biệt được với 0, điểm uốn đại số nằm ngoài miền dữ liệu, và quan hệ trong miền quan sát là dương đơn điệu. Bằng chứng đơn quốc gia độc lập đã tìm thấy đúng điều này ở Singapore (điểm uốn ≈ 88,6%, không định vị tin cậy); ước lượng gộp 50 nền tìm thấy điều này cho cả nhóm Advanced đổi mới. Nhật Bản, nền kinh tế tiên tiến lớn nhất và lâu đời nhất khu vực, cung cấp phép thử khắt khe nhất.

Ba đóng góp: (i) ước lượng I–P trên WBES đầu tiên cho Nhật Bản; (ii) xác nhận sạch dự đoán biên trên; (iii) hai quy luật đặc thù Nhật, phần bù trường thọ *shinise* và biên lãnh đạo nữ mỏng, có giá trị độc lập cho dòng nghiên cứu thượng tầng quản trị xuyên bối cảnh.

## 2. Giả thuyết

**H1.** Tại Nhật Bản, cường độ xuất khẩu có liên hệ tuyến tính dương, có ý nghĩa với năng suất lao động; số hạng bậc hai không có ý nghĩa và điểm uốn đại số nằm ngoài miền FSTS quan sát được.

**H2.** TCI có hiệu ứng mức dương; các tương tác với cường độ xuất khẩu không có ý nghĩa.

**H3.** DAI có hiệu ứng mức dương nhưng khiêm tốn (bão hòa Tier-1); tương tác FSTS×DAI không có ý nghĩa.

## 3. Dữ liệu và phương pháp

Toàn bộ mẫu cắt ngang Nhật Bản 2025 (N = 2.168; 339 biến hài hòa; chọn mẫu ngẫu nhiên phân tầng theo ngành, quy mô, vùng). Đặc trưng so với năm nền còn lại của Nhóm I: phân tán năng suất trong đợt hẹp nhất toàn pool 50 nền (sd 0,89; P90/P10 = 8,3), website cao nhất (83,8%), tuổi doanh nghiệp trung bình cao nhất (50,4 năm so với 23,0), nữ quản lý cấp cao thấp nhất (7,3% so với 27,5%), cường độ xuất khẩu cấp cơ sở thấp (FSTS trung bình 4,1%; 16,5% doanh nghiệp xuất khẩu) dù tỷ lệ R&D cao (21,9%).

Biến phụ thuộc: ln(d2/l1), winsorize 1/99 (một nền kinh tế, một đồng tiền nên mức so sánh được trực tiếp). FSTS = (d3b + d3c)/100 theo định nghĩa WBES chuẩn, thống nhất với khung ước lượng 50 nền của luận án; biến thể chỉ xuất khẩu trực tiếp (d3c) dùng cho kiểm tra độ vững. TCI = trung bình chuẩn hóa của R&D (h8), chứng nhận quốc tế (b8), đổi mới sản phẩm (h1); DAI = website (c22b). Kiểm soát: sở hữu nước ngoài ≥ 10% (b2b), ln(tuổi + 1) (b5), nữ quản lý cấp cao (b7a). Mọi mô hình có hiệu ứng cố định ngành (13 tầng) và sai số chuẩn HC1.

## 4. Kết quả

**Bảng 1.** *Chuỗi mô hình phân tầng, Nhật Bản 2025 (biến phụ thuộc: ln năng suất lao động).*

| | M1 | M2 | M3 | M4 | M5 |
|---|--:|--:|--:|--:|--:|
| FSTS (định tâm) | +0,671*** | +1,042** | +0,872* | +0,476 | +0,486 |
| FSTS² | | −0,606 | −0,419 | −0,009 | −0,034 |
| Sở hữu nước ngoài ≥10% | | | +0,259† | +0,203 | +0,210 |
| ln(tuổi doanh nghiệp) | | | +0,073** | +0,061* | +0,063* |
| Nữ quản lý cấp cao | | | −0,171* | −0,170* | −0,170* |
| TCI (z) | | | | +0,100*** | +0,102*** |
| DAI (website) | | | | +0,110* | +0,111* |
| FSTS×TCI | | | | | −0,126 |
| FSTS×DAI | | | | | +0,111 |
| FE ngành | có | có | có | có | có |
| N | 2.047 | 2.047 | 2.011 | 1.996 | 1.996 |
| R² | 0,140 | 0,141 | 0,147 | 0,162 | 0,163 |
| Điểm uốn đại số | — | [90,1%] | [108,3%] | — | — |

*Ghi chú: sai số chuẩn vững HC1. † p < 0,10; \* p < 0,05; \*\* p < 0,01; \*\*\* p < 0,001. Điểm uốn trong ngoặc vuông chỉ là giá trị đại số; không đặc tả nào có số hạng bậc hai ý nghĩa nên không chữ U ngược nào được xác nhận (Lind & Mehlum, 2010). Độ vững với d3c riêng: β₁ = +1,255**; β₂ = −0,674 (p = 0,445), cùng kết luận. Tái lập: `p10_japan/replication/p10_japan_models.py`.*

**H1 được ủng hộ.** Hiệu ứng tuyến tính dương và có ý nghĩa cao; số hạng bậc hai không bao giờ tiệm cận ý nghĩa; điểm uốn đại số (90–108%) nằm xa ngoài miền FSTS quan sát (trung bình 4,1%). Trong miền quan sát, quốc tế hóa nâng hiệu quả một cách đơn điệu: Nhật Bản nằm trên một nhánh đi lên dài mà nhánh đi xuống vắng mặt về mặt thực nghiệm, trùng khớp kết quả Singapore và kết quả cấp nhóm của ước lượng 50 nền.

**H2 được ủng hộ.** TCI có hiệu ứng mức chính xác (+0,100; p < 0,001) và hấp thụ phần lớn hiệu ứng FSTS thô khi đưa vào (M4), nhất quán với chọn lọc theo năng lực vào hoạt động xuất khẩu; các tương tác không có ý nghĩa. Năng lực nâng sàn, không uốn đường cong.

**H3 được ủng hộ.** DAI giữ phần bù dương khiêm tốn (+0,110; p = 0,028) dù bão hòa 83,8%, không có tương tác uốn đường cong. Phần bù bằng khoảng một nửa mức của ước lượng gộp 50 nền (+0,201), đúng mức nén mà bão hòa Tier-1 dự đoán.

**Quy luật đặc thù Nhật.** Phần bù trường thọ: mỗi đơn vị log tuổi thêm khoảng 7% năng suất, đáng chú ý ở nền kinh tế có doanh nghiệp lâu đời nhất pool (trung bình 50,4 năm), nhất quán với truyền thống *shinise*. Hệ số nữ quản lý cấp cao âm (−0,170; p = 0,010) trong nền kinh tế có biên lãnh đạo nữ mỏng nhất khu vực (7,3% so với mức dẫn đầu Đông Á – Thái Bình Dương 33,4%): cách đọc hợp lý nhất là chọn lọc vào các ngách thâm dụng lao động biên thấp, không nên diễn giải nhân quả.

## 5. Bàn luận và kết luận

Kết quả Nhật Bản hoàn tất bức tranh ba vùng của quan hệ I–P phụ thuộc thể chế trên 50 nền kinh tế: chữ U ngược sắc nét ở vùng giữa gradient (Nhóm IV: điểm uốn 43,0%; Việt Nam 39–46%; Ấn Độ 40,7% năm 2022); duỗi thẳng ở biên trên (Nhật Bản, Singapore, cả Nhóm I); tan rã ở biên dưới và đảo chiều theo spec mức tại nhóm đảo nhỏ Thái Bình Dương (gánh nặng quốc tế hóa bắt buộc). Hai giới hạn kỷ luật hóa diễn giải: đây là một mẫu cắt ngang đơn lẻ (liên hệ có điều kiện, không phải hiệu ứng nhân quả), và cường độ xuất khẩu cấp cơ sở thấp phản ánh cấu trúc quốc tế hóa Nhật Bản vốn tập trung ở các tập đoàn đa quốc gia và đầu tư ra nước ngoài, nghĩa là khung WBES nắm bắt đúng biên trong nước, nơi dự đoán biên trên vận hành.

Hàm ý chính sách: ở bối cảnh thể chế biên trên, ràng buộc trói buộc không phải một ngưỡng bất lợi cần tránh mà là độ rộng tham gia (chỉ một phần sáu cơ sở xuất khẩu) và sàn năng lực hỗ trợ nó.

*(Danh mục tài liệu tham khảo: xem bản tiếng Anh trong submission/abm_package/01_manuscript_blinded.md — 23 mục, APA 7.)*

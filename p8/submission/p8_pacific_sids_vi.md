# Khi chữ U ngược tan biến: Các điều kiện biên cấu trúc của quan hệ quốc tế hóa–hiệu quả tại các vi quốc gia Thái Bình Dương

*Bản dịch tiếng Việt. Nguồn: `p8/p8_pacific_sids_redesigned_en.md` (bản thảo đã thiết kế lại, 2026-06-19; 7 nền SIDS Thái Bình Dương thật, N = 1.450)*
*Dịch thuật: Claude AI theo chuẩn văn phong học thuật CTU (09b_vn_term_glossary.md v1.4)*
*Ngày: 2026-06-23*

**Đỗ Thùy Hương** · Khoa Kinh tế, Đại học Cần Thơ · huongp1323001@gstudent.ctu.edu.vn · ORCID: [0000-0002-7711-2487](https://orcid.org/0000-0002-7711-2487)
**Phan Anh Tú** *(Tác giả liên hệ)* · Khoa Kinh tế, Đại học Cần Thơ · patu@ctu.edu.vn · ORCID: [0000-0003-0667-3137](https://orcid.org/0000-0003-0667-3137)

*Nộp đăng: World Development*

---

**Phân loại bản thảo:** bài báo nghiên cứu.

**Từ khóa:** quan hệ quốc tế hóa–hiệu quả; chữ U ngược; điều kiện biên; quốc đảo nhỏ đang phát triển; quốc tế hóa cưỡng bức; khoảng trống thể chế; năng suất lao động; nền kinh tế Thái Bình Dương.

> **Phiên bản:** Bản thảo đã thiết kế lại (2026-06-19), được tái định khung từ bản nháp "Hình phạt Quốc tế hóa Cưỡng bức" trước đó sang một đóng góp dạng điều-kiện-phạm-vi; mẫu được hiệu chỉnh thành bảy nền SIDS Thái Bình Dương thật sự (loại Timor-Leste theo phân loại của Ngân hàng Thế giới / Liên Hợp Quốc). Mọi ước lượng ở cấp doanh nghiệp đều tái lập được từ `p8/replication/data/p8_7pacific_pinned.csv` thông qua `p8/replication/build_and_run_p8_7pacific.py` (dựng từ tệp WBES `.dta` đã commit, dùng quy trình hài hòa hóa của P7); thiết kế và kiểm chứng tại `p8/P8_REDESIGN_2026-06.md`.

---

## Tóm tắt

Chữ U ngược là dạng hàm chủ đạo của quan hệ quốc tế hóa–hiệu quả (internationalization–performance, I–P): hiệu quả ban đầu tăng theo cường độ doanh thu nước ngoài, rồi suy giảm sau một điểm ngoặt. Logic này dựa, một cách ngầm định, trên ba điều kiện tiên quyết về cấu trúc, một thị trường nội địa khả thi, chi phí thương mại có thể quản lý được, và hỗ trợ thể chế vận hành được, vốn thường xuyên được thỏa mãn trong các mẫu nghiên cứu chính thống nhưng lại đồng thời bị vi phạm tại những nền kinh tế ngoại vi nhất thế giới. Chúng tôi kiểm định liệu chữ U ngược có mở rộng tới các bối cảnh như vậy hay không, sử dụng dữ liệu vi mô từ Khảo sát Doanh nghiệp Ngân hàng Thế giới gồm 1.450 doanh nghiệp trên bảy quốc đảo nhỏ đang phát triển (small island developing states, SIDS) Thái Bình Dương, Fiji, Kiribati, Papua New Guinea, Samoa, Solomon Islands, Tonga và Vanuatu (2009–2025). Phát hiện vững là chữ U ngược kinh điển **tan biến**: trên toàn mẫu, độ dốc cường độ xuất khẩu không thể phân biệt được về mặt thống kê so với không (wild-cluster bootstrap p = ,66) và số hạng độ cong chỉ có ý nghĩa ở mức biên và mang dấu *dương* chứ không lõm (p = ,082), tương phản gay gắt với chữ U ngược rõ nét quan sát được tại các nền kinh tế chuyển đổi lục địa. Một mô hình yếu hơn, có tính gợi mở, là một khi giữ năng lực doanh nghiệp cố định thì độ cong trở nên dương mạnh hơn và có ý nghĩa ở mức biên (wild-cluster bootstrap p = ,056), gợi ý một quan hệ **lồi (convex)** thay vì lõm, một hình phạt năng suất trên dải cường độ xuất khẩu thấp-đến-trung-bình nơi gần như toàn bộ doanh nghiệp đảo hoạt động; chúng tôi trình bày tính lồi này một cách thận trọng chứ không như một sự đảo chiều đã được xác nhận. Năng lực công nghệ nâng mặt bằng năng suất (p = ,036) nhưng không khôi phục chữ U ngược. Chúng tôi diễn giải mô hình này qua khái niệm **gánh nặng quốc tế hóa bắt buộc (Forced Internationalization Penalty, FIP)**, một trường hợp giới hạn lý thuyết trong đó quốc tế hóa bắt buộc, bị tước đoạt điều kiện tiên quyết, trở nên bào mòn hiệu quả, đồng thời báo cáo minh bạch rằng bất kỳ ước lượng điểm âm mạnh nào cũng nhạy cảm với số lượng nhỏ các nền kinh tế đảo có dữ liệu cấp doanh nghiệp đầy đủ. Nghiên cứu nhận diện các điều kiện tiên quyết về cấu trúc vốn ngầm định của mô hình chữ U ngược, giới hạn phạm vi của nó, và mang hàm ý trực tiếp cho chiến lược tăng trưởng do xuất khẩu dẫn dắt tại các vi quốc gia.

## Abstract

The inverted-U is the dominant functional form for the internationalization–performance (I–P) relationship: performance first rises with foreign-sales intensity, then declines beyond a turning point. This logic rests, implicitly, on three structural prerequisites, a viable domestic market, manageable trade costs, and functional institutional support, that are routinely satisfied in mainstream samples but are simultaneously violated in the world's most peripheral economies. We test whether the inverted-U extends to such contexts using World Bank Enterprise Survey microdata from 1,450 firms across seven Pacific small island developing states (SIDS), Fiji, Kiribati, Papua New Guinea, Samoa, Solomon Islands, Tonga, and Vanuatu (2009–2025). The robust finding is that the canonical inverted-U **dissolves**: across the full sample, the export-intensity slope is statistically indistinguishable from zero (wild-cluster bootstrap p = .66) and the curvature term is only marginally significant and *positive* rather than concave (p = .082), in sharp contrast to the sharp inverted-U observed in mainland transition economies. A weaker, suggestive pattern is that once firm capability is held constant the curvature becomes more strongly positive and marginally significant (wild-cluster bootstrap p = .056), hinting at a **convex** rather than concave relationship, a productivity penalty across the low-to-moderate export-intensity range in which almost all island firms operate; we present this convexity cautiously rather than as a confirmed reversal. Technological capability raises the productivity level (p = .036) but does not restore the inverted-U. We interpret this pattern through the concept of a **Forced Internationalization Penalty (FIP)**, a theoretical limiting case in which compulsory, prerequisite-deprived internationalization becomes performance-eroding, while reporting transparently that any strong negative point estimate is sensitive to the small number of island economies with complete firm-level data. The study identifies the previously implicit structural prerequisites of the inverted-U paradigm, bounds its scope, and carries direct implications for export-led-growth strategy in microstates.

## 1. Giới thiệu

Quan hệ giữa quốc tế hóa và hiệu quả hoạt động kinh doanh của doanh nghiệp (I–P) nằm trong số những quy luật thực nghiệm được khảo sát nhiều nhất, và gây tranh cãi nhất, của nghiên cứu kinh doanh quốc tế (international business, IB) (Verbeke & Brugman, 2018). Hàng thập kỷ nghiên cứu đã hội tụ về một dạng hàm phi tuyến hình chữ U ngược: mở rộng ra nước ngoài trước tiên cải thiện hiệu quả thông qua lợi thế kinh tế nhờ quy mô, học hỏi và đa dạng hóa thị trường, sau đó bào mòn hiệu quả khi vượt qua một điểm ngoặt do chi phí phối hợp và bất lợi của tính nước ngoài (liability of foreignness) tích lũy (Contractor, Kundu, & Hsu, 2003; Hitt, Hoskisson, & Kim, 1997; Lu & Beamish, 2004). Các phân tích tổng hợp (meta-analysis) báo cáo một tác động trung bình dương với tính không đồng nhất rất lớn, một lời mời đặt câu hỏi không phải *liệu* quốc tế hóa có giúp ích hay không mà là *trong những điều kiện nào* (Bausch & Krist, 2007; Kirca et al., 2011).

Một giả định nền tảng, nhưng hiếm khi được nêu ra, chống đỡ toàn bộ truyền thống nghiên cứu này: rằng môi trường thể chế và thị trường có thể dịch chuyển *cường độ* hoặc *điểm ngoặt* của quan hệ I–P, nhưng không làm thay đổi hình dạng cơ bản của nó. Các nghiên cứu tái lập trên mẫu lớn gần đây đã bắt đầu chọc thủng giả định ấy, phát hiện rằng quan hệ đa quốc gia–hiệu quả là yếu, bất ổn, hoặc phụ thuộc bối cảnh giữa các quốc gia (Berry & Kaul, 2016; Pisani, Garcia-Bernardo, & Heemskerk, 2020). Tuy nhiên, ranh giới của mô hình chữ U ngược, các điều kiện theo đó nó ngừng có hiệu lực hoàn toàn, vẫn chưa được lập bản đồ ở cấp doanh nghiệp trong những bối cảnh nơi các điều kiện đó nhiều khả năng vắng mặt nhất.

Bài báo này lập bản đồ ranh giới đó. Chúng tôi lập luận rằng logic chữ U ngược dựa trên ba điều kiện tiên quyết về cấu trúc bị đồng thời vi phạm tại những nền kinh tế ngoại vi nhất thế giới, các quốc đảo nhỏ đang phát triển (SIDS) Thái Bình Dương: (i) một thị trường nội địa khả thi đủ lớn để doanh nghiệp đạt quy mô hiệu quả tối thiểu trước khi xuất khẩu; (ii) chi phí thương mại đủ thấp để mở rộng xuất khẩu là một bài toán tối ưu hóa kinh tế chứ không phải một mệnh lệnh sinh tồn; và (iii) hỗ trợ thể chế đủ để doanh nghiệp chiếm hữu lợi tức từ hoạt động quốc tế (Briguglio, 1995; Khanna & Palepu, 2010; Winters & Martins, 2004). Nơi cả ba đều thất bại, doanh nghiệp xuất khẩu không phải do lựa chọn chiến lược mà do cưỡng bức, và bộ máy chi phí–lợi ích tạo ra chữ U ngược không còn chỗ bám.

Sử dụng dữ liệu vi mô Khảo sát Doanh nghiệp Ngân hàng Thế giới (World Bank Enterprise Survey, WBES) cho 1.450 doanh nghiệp trên bảy nền SIDS Thái Bình Dương, chúng tôi đặt câu hỏi liệu chữ U ngược có mở rộng tới vùng ngoại vi cực đoan này hay không. Câu trả lời là không: độ cong định nghĩa nên chữ U ngược vắng mặt về mặt thống kê và độ dốc cường độ xuất khẩu không phân biệt được với không. Một mô hình yếu hơn, có tính gợi mở, có điều kiện trên năng lực doanh nghiệp, quan hệ nghiêng về lồi thay vì lõm, một hình phạt năng suất trên dải xuất khẩu thấp-đến-trung-bình nơi gần như toàn bộ doanh nghiệp đảo hoạt động, chỉ tới một trường hợp giới hạn lý thuyết mà chúng tôi gọi tên là **gánh nặng quốc tế hóa bắt buộc (Forced Internationalization Penalty, FIP)**, vốn được chúng tôi xử lý như một khái niệm giới hạn chứ không phải một hiệu ứng đã được xác nhận.

Chúng tôi có bốn đóng góp. Thứ nhất, chúng tôi cung cấp kiểm định cấp doanh nghiệp đầu tiên về *các điều kiện phạm vi* của mô hình chữ U ngược tại các vi quốc gia Thái Bình Dương, cho thấy dạng hàm chủ đạo không khái quát hóa được sang vùng ngoại vi cực đoan. Thứ hai, chúng tôi làm hiện rõ ba điều kiện tiên quyết về cấu trúc mà văn liệu I–P đã để ngầm, một làm rõ lý thuyết áp dụng được cho bất kỳ nền kinh tế vi mô hoặc ngoại vi nào. Thứ ba, chúng tôi giới thiệu và giới hạn FIP như một khái niệm lý thuyết, phân biệt nó với chi phí giai đoạn một của đường cong S và bất lợi của tính nước ngoài. Thứ tư, chúng tôi rút ra hàm ý chính sách rằng các đơn thuốc tăng trưởng do xuất khẩu dẫn dắt không tương thích với thực tế cấu trúc của các vi quốc gia, nơi các ràng buộc trói buộc là tính khả thi của thị trường nội địa, chi phí thương mại và thể chế chứ không phải bản thân cường độ xuất khẩu.

## 2. Lý thuyết và các mệnh đề

### 2.1 Chữ U ngược và các điều kiện tiên quyết ngầm định của nó

Chữ U ngược bắt nguồn từ một logic chi phí–lợi ích (Hitt et al., 1997; Lu & Beamish, 2004). Quốc tế hóa sớm mang lại lợi thế kinh tế nhờ quy mô, dư địa cho học hỏi, và đa dạng hóa rủi ro; vượt qua một ngưỡng, tính phức tạp tổ chức, chi phí phối hợp, và bất lợi của tính nước ngoài đảo ngược quỹ đạo (Hennart, 2007; Zaheer, 1995). Điểm ngoặt, thường được ước lượng ở mức 30–70% tỷ phần doanh thu nước ngoài trên tổng doanh thu (foreign sales to total sales, FSTS), là cường độ tại đó chi phí biên bằng lợi ích biên.

Bộ máy này giả định trước rằng xuất khẩu là một *lựa chọn* được đưa ra từ một cơ sở quê nhà khả thi. Ba điều kiện tiên quyết về cấu trúc là cần thiết để giả định đó đứng vững:

**Điều kiện tiên quyết 1, một thị trường nội địa khả thi.** Mô hình Uppsala giả định một cơ sở quê nhà vận hành được, cung cấp doanh thu, nguồn lực và học hỏi trước và trong quá trình mở rộng (Johanson & Vahlne, 1977, 2009). Khi thị trường nội địa không thể hỗ trợ quy mô hiệu quả tối thiểu, doanh nghiệp bị cưỡng bức phải xuất khẩu bất kể mức độ sẵn sàng, và cơ chế "lựa chọn vào xuất khẩu" làm nền tảng cho hầu hết các mô hình I–P bị phá vỡ (Melitz, 2003).

**Điều kiện tiên quyết 2, chi phí thương mại có thể quản lý được.** Mô hình giả định rằng chi phí biên của việc phục vụ thị trường nước ngoài bị chặn trên. Sự cô lập địa lý cực độ ở Thái Bình Dương thổi phồng chi phí hậu cần và cước vận chuyển với biên độ rộng, khiến mở rộng xuất khẩu bào mòn biên lợi nhuận ở mọi cường độ (Briguglio, 1995; Winters & Martins, 2004).

**Điều kiện tiên quyết 3, hỗ trợ thể chế vận hành được.** Việc chiếm hữu lợi tức từ quốc tế hóa đòi hỏi các thể chế trung gian, tài trợ thương mại, hậu cần, năng lực xúc tiến xuất khẩu, mà sự vắng mặt của chúng (khoảng trống thể chế) áp đặt một lực cản cấu trúc (Doh, Rodrigues, Saka-Helmhout, & Makhija, 2017; Khanna & Palepu, 2010; North, 1990).

### 2.2 Từ sự tan biến đến sự đảo chiều

Khi cả ba điều kiện tiên quyết đồng thời thất bại, cơ chế tạo sinh của chữ U ngược bị vô hiệu hóa. Do đó, trước tiên chúng tôi kỳ vọng rằng bản thân *hình dạng* không xuất hiện:

> **Mệnh đề 1 (sự tan biến).** Tại các SIDS Thái Bình Dương, chữ U ngược vắng mặt: cả số hạng độ cong FSTS lẫn độ dốc FSTS đều không phân biệt được về mặt thống kê so với không, khác với các nền kinh tế lục địa nơi các điều kiện tiên quyết được thỏa mãn.

Sự tan biến là tuyên bố tối thiểu. Một khả năng mạnh hơn là, một khi tính tới các khác biệt năng lực ở cấp doanh nghiệp, quan hệ chuyển sang *lồi* nhẹ. Nếu xuất khẩu là bắt buộc và bị tước đoạt điều kiện tiên quyết, thì cường độ xuất khẩu tăng thêm trong dải thấp-đến-trung-bình chiếm ưu thế về mặt thực nghiệm làm gia tăng phơi nhiễm với chi phí thương mại cao và gánh nặng phối hợp mà không có một cơ sở nội địa để hấp thụ chúng, một hình phạt, trong khi chỉ có doanh nghiệp xuất khẩu cường độ cao, năng lực vượt trội và hiếm gặp mới thoát khỏi nó. Điều này hàm ý một quan hệ có điều kiện lồi (hình chữ U), không lõm:

> **Mệnh đề 2 (tính lồi có điều kiện; thăm dò).** Có điều kiện trên năng lực doanh nghiệp, quan hệ I–P tại SIDS nghiêng về lồi thay vì lõm, một hình phạt năng suất trên dải cường độ xuất khẩu thấp-đến-trung-bình, chỉ đảo chiều ở các cường độ cao vốn hiếm gặp về mặt thực nghiệm. Chúng tôi định khung đây như một mệnh đề thăm dò, vì tính lồi chỉ có ý nghĩa ở mức biên.

Năng lực là một yếu tố dịch chuyển mặt bằng, không phải một sự giải cứu. Logic năng lực hấp thụ và logic dựa trên nguồn lực hàm ý rằng năng lực công nghệ nâng năng suất ở mọi cường độ (Cohen & Levinthal, 1990; Lall, 1992), nhưng nó không thể cung cấp các điều kiện tiên quyết về cấu trúc đang thiếu:

> **Mệnh đề 3 (năng lực không khôi phục đường cong).** Năng lực công nghệ và áp dụng số nâng mặt bằng năng suất nhưng không khôi phục một quan hệ lõm (chữ U ngược).

### 2.3 Gánh nặng quốc tế hóa bắt buộc như một trường hợp giới hạn lý thuyết

Chúng tôi gọi tên trường hợp giới hạn của Mệnh đề 1–2, nơi quốc tế hóa bắt buộc, bị tước đoạt điều kiện tiên quyết, trở nên bào mòn hiệu quả một cách đơn điệu, là **gánh nặng quốc tế hóa bắt buộc (Forced Internationalization Penalty, FIP)**. FIP khác biệt với các khái niệm liền kề. Khác với độ dốc đi xuống của giai đoạn một trong lý thuyết ba giai đoạn (Contractor et al., 2003), FIP không phải là một chi phí học hỏi tạm thời đang chờ một điểm ngoặt cuối cùng; nó là một điều kiện cấu trúc không có điểm tối ưu nội tại trong dải quan sát được. Khác với bất lợi của tính nước ngoài, vốn vận hành ở biên giới thị trường sở tại (Zaheer, 1995), FIP bắt nguồn từ cơ sở quê nhà (nguồn). Và khác với khởi nghiệp do nhu cầu, nơi người sáng lập trong các bối cảnh đang phát triển có thể đạt sự ngang bằng khi có đủ thời gian và hỗ trợ thể chế (Sarasvathy, Kumar, York, & Bhagavatula, 2014), FIP đặc trưng cho các bối cảnh nơi hỗ trợ đó vắng mặt một cách hệ thống. Chúng tôi xử lý FIP như một construct *lý thuyết* giới hạn phạm vi của các lý thuyết quốc tế hóa phổ quát; bằng chứng thực nghiệm SIDS dưới đây nhất quán với hướng của nó nhưng, như chúng tôi báo cáo minh bạch, không ước lượng được độ lớn của nó một cách vững chắc.

## 3. Dữ liệu và phương pháp

### 3.1 Mẫu

Chúng tôi rút dữ liệu cấp doanh nghiệp từ Khảo sát Doanh nghiệp Ngân hàng Thế giới cho bảy quốc đảo nhỏ đang phát triển Thái Bình Dương có sẵn dữ liệu vi mô cấp doanh nghiệp, Fiji, Kiribati, Papua New Guinea, Samoa, Solomon Islands, Tonga và Vanuatu, trên tất cả các đợt khảo sát có sẵn từ 2009 đến 2025. Đây là các Quốc gia Đảo Thái Bình Dương theo phân loại khu vực của Ngân hàng Thế giới và là thành viên của danh sách SIDS Thái Bình Dương của Liên Hợp Quốc. Chúng tôi cố ý loại trừ Timor-Leste, nước, dù đôi khi được xếp chung với khu vực, không phải là một Quốc gia Đảo Thái Bình Dương của Ngân hàng Thế giới cũng không phải một SIDS Thái Bình Dương của Liên Hợp Quốc, và được phân loại là một nền kinh tế Đông Á và Thái Bình Dương riêng biệt; việc bao gồm nó sẽ làm lẫn lộn một nền kinh tế lớn hơn tương đối, khác biệt về cấu trúc (nó sẽ đóng góp gần một phần tư số quan sát gộp) với vùng ngoại vi đảo đích thực. Sau khi yêu cầu năng suất lao động và cường độ xuất khẩu không khuyết, mẫu phân tích bao gồm **1.450 doanh nghiệp trên bảy nền kinh tế và mười ba ô quốc gia-năm**. Nhất quán với lập luận cấu trúc, hồ sơ xuất khẩu mỏng một cách bất thường: chỉ **14,6%** doanh nghiệp xuất khẩu, FSTS trung bình là **0,054**, và độ phân tán năng suất trong cùng nền kinh tế là cao (tỷ lệ năng suất lao động giữa phân vị thứ 90 và thứ 10 vượt một bậc độ lớn), nhất quán với dấu hiệu phân bổ sai nguồn lực của các bối cảnh thể chế yếu (Hsieh & Klenow, 2009).

### 3.2 Biến số

Năng suất lao động là logarit tự nhiên của doanh thu hằng năm trên mỗi lao động, ln(d2/l1), được giới hạn cực trị (winsorize) ở mức 1/99 và chuẩn hóa (z-score) trong mỗi ô nền-kinh-tế-năm để các ước lượng trung lập về tiền tệ và đặt trên cùng một mặt bằng với nghiên cứu đồng hành trên 49 nền kinh tế. Cường độ quốc tế hóa (FSTS) là tổng xuất khẩu tính theo tỷ phần doanh thu, (d3b + d3c)/100, được trung-tâm-hóa trong mẫu. Năng lực công nghệ (TCI) là một chỉ số chuẩn hóa của chứng nhận chất lượng và cấp phép công nghệ nước ngoài; áp dụng số (DAI) là chỉ báo hiện diện website, thước đo Tier-1 có sẵn một cách so sánh được qua các đợt khảo sát SIDS. Tuổi doanh nghiệp (log số năm kể từ khi thành lập) và sở hữu nước ngoài (chỉ báo ngưỡng 10%) là các biến kiểm soát. Chúng tôi theo thông lệ đã thiết lập trong việc thao tác hóa năng lực như một hợp thể cấu thành (formative composite) (Diamantopoulos & Winklhofer, 2001; Jarvis, MacKenzie, & Podsakoff, 2003).

### 3.3 Ước lượng và suy luận

Tất cả các mô hình bao gồm hiệu ứng cố định nền kinh tế và năm, cô lập biến thiên trong cùng nền-kinh-tế-năm. Vì thiết kế chỉ có **bảy cụm (nền kinh tế)**, sai số chuẩn vững theo cụm thông thường (CRV1) bác bỏ quá mức; do đó chúng tôi đặt suy luận trên **wild-cluster restricted bootstrap** (Cameron, Gelbach, & Miller, 2008; 9.999 lần lặp, trọng số Rademacher, phân cụm theo nền kinh tế) và báo cáo số cụm một cách nổi bật. Chúng tôi kiểm định chữ U ngược bằng các điều kiện của Haans, Pieters và He (2016) và kiểm định U của Lind và Mehlum (2010), đồng thời đối chiếu các ước lượng SIDS với chữ U ngược lục địa rõ nét đã được ghi nhận cho các nền kinh tế chuyển đổi trong nghiên cứu đồng hành trên 49 nền kinh tế.

## 4. Kết quả

### 4.1 Chữ U ngược tan biến (Mệnh đề 1)

Bảng 1 báo cáo trình tự mô hình. Việc thêm một số hạng FSTS tuyến tính vào các biến kiểm soát để lại độ dốc không phân biệt được với không (M1: β = −0,085, wild-bootstrap p = ,66). Việc thêm số hạng bậc hai không khôi phục được chữ U ngược: hệ số độ cong mang dấu **dương** và chỉ có ý nghĩa ở mức biên (M2: β₂ = +0,696, wild-bootstrap p = ,082; β₁ = −0,567, p = ,088). Các điều kiện Lind–Mehlum cho một chữ U ngược đích thực không được thỏa mãn, không có điểm cực đại nội tại trong dải quan sát được. Điều này tương phản gay gắt với chế độ chuyển đổi lục địa, nơi cùng một đặc tả cho ra một chữ U ngược rõ nét, có ý nghĩa cao (β₂ = −1,012, p < ,001). Do đó, hình dạng kinh điển **vắng mặt tại vùng ngoại vi**.

**Bảng 1.** Quốc tế hóa và năng suất lao động chuẩn hóa, SIDS Thái Bình Dương (hiệu ứng cố định nền kinh tế + năm; biến kiểm soát tuổi doanh nghiệp và sở hữu nước ngoài; wild-cluster bootstrap p, G = 7).

| Số hạng | M1 | M2 | M3 |
|---|--:|--:|--:|
| FSTS (đã trung-tâm-hóa) | −0,085 (,66) | −0,567 (,088) | −0,852 (,024) |
| FSTS² | — | +0,696 (,082) | +1,051 (,056) |
| TCI (z) | — | — | +0,064 (,036) |
| DAI (website) | — | — | +0,157 (,102) |
| N | 1.434 | 1.434 | 1.389 |

*Biến phụ thuộc: năng suất lao động chuẩn hóa z trong nền-kinh-tế-năm. Biến kiểm soát tuổi doanh nghiệp và sở hữu nước ngoài cùng hiệu ứng cố định nền kinh tế + năm được bao gồm trong mọi mô hình. Giá trị p wild-cluster bootstrap trong ngoặc đơn (9.999 lần lặp, trọng số Rademacher, phân cụm theo nền kinh tế).*

### 4.2 Một tính lồi có điều kiện mang tính gợi mở (Mệnh đề 2)

Một khi giữ cố định năng lực công nghệ và áp dụng số (M3), độ cong chuyển sang dương mạnh hơn và **có ý nghĩa ở mức biên** (β₂ = +1,051, wild-bootstrap p = ,056), với một số hạng tuyến tính âm (β₁ = −0,852, p = ,024). Hình dạng hàm ý, một cách dè dặt, là **lồi (hình chữ U)**: năng suất giảm theo cường độ xuất khẩu trên dải thấp-đến-trung-bình và sẽ chỉ đi lên sau một điểm *cực tiểu* nội tại trong vùng FSTS cao mà ít doanh nghiệp đảo chạm tới. Chúng tôi đọc điều này như *gợi mở* về một ảnh phản chiếu của chữ U ngược lục địa thay vì một sự đảo chiều đã được xác nhận, do ý nghĩa ở mức biên và số cụm nhỏ.

![**Hình 1.** Chữ U ngược tan biến tại vùng ngoại vi. Các nền kinh tế chuyển đổi lục địa cho thấy một chữ U ngược lõm rõ nét (bảng a); tại các SIDS Thái Bình Dương, chữ U ngược vắng mặt về mặt thống kê, và có điều kiện trên năng lực doanh nghiệp một mô hình lồi *gợi mở* xuất hiện (bảng b), hàm ý một hình phạt năng suất trên dải cường độ xuất khẩu thấp-đến-trung-bình nơi gần như toàn bộ doanh nghiệp đảo hoạt động.](figures/p8_fig1_dissolution_en.png) Về mặt thực chất, nếu mô hình lồi đứng vững, thì khối lượng chiếm ưu thế của các doanh nghiệp SIDS, gần như toàn bộ ở mức FSTS thấp-đến-trung-bình, sẽ nằm trên **nhánh đi xuống**, nơi cường độ xuất khẩu tăng thêm gắn với năng suất thấp hơn: dấu hiệu thực nghiệm nhất quán với cơ chế FIP.

### 4.3 Năng lực nâng mặt bằng nhưng không khôi phục đường cong (Mệnh đề 3)

Năng lực công nghệ mang một hiệu ứng mặt bằng dương, vững (TCI: β = +0,064, wild-bootstrap p = ,036); áp dụng số là dương nhưng yếu hơn và không có ý nghĩa (DAI: β = +0,157, p = ,102). Không yếu tố nào khôi phục được một chữ U ngược lõm, thực vậy, việc điều kiện hóa trên năng lực còn làm sắc nét mô hình *lồi*. Do đó năng lực vận hành như một yếu tố dịch chuyển mặt bằng năng suất không thể thay thế cho các điều kiện tiên quyết về cấu trúc đang vắng mặt, nhất quán với Mệnh đề 3.

### 4.4 Minh bạch: độ nhạy của bất kỳ ước lượng âm mạnh nào

Chúng tôi báo cáo công khai rằng *độ lớn* của bất kỳ ước lượng I–P âm mạnh nào trong bối cảnh này đều nhạy cảm với việc nền kinh tế đảo nào được đưa vào mẫu. Một bản dựng hạn chế hơn, giới hạn ở vài nền kinh tế có dữ liệu kiểm soát trước-2018 đầy đủ, cho ra một độ dốc âm lớn, có ý nghĩa, trong khi mẫu đầy đủ bảy nền kinh tế cho ra mô hình null-đến-lồi đã báo cáo ở trên; với chỉ ba cụm, suy luận theo cụm là không đáng tin trong bản dựng hạn chế. Bản dựng hạn chế ba cụm này mang tính minh họa, nhạy cảm với phiên bản dữ liệu, và không nên được đọc như một ước lượng vững. Do đó chúng tôi neo các tuyên bố của mình vào mẫu đầy đủ với suy luận wild-bootstrap và trình bày FIP như một trường hợp giới hạn lý thuyết chứ không phải một hiệu ứng được ước lượng chính xác. Bản thân sự minh bạch này là một đóng góp phương pháp luận cho nghiên cứu cấp doanh nghiệp về các nền kinh tế vi mô khan hiếm dữ liệu.

## 5. Thảo luận

### 5.1 Giới hạn mô hình chữ U ngược

Kết quả trung tâm của chúng tôi là quan hệ I–P hình chữ U ngược không mở rộng tới vùng ngoại vi Thái Bình Dương. Hình dạng tổ chức nên văn liệu I–P tan biến, với bằng chứng gợi mở rằng, có điều kiện trên năng lực, quan hệ nghiêng về lồi thay vì đảo chiều một cách sạch sẽ. Đây không phải là một thất bại của đo lường mà là một **điều kiện biên**: chữ U ngược giả định trước một thị trường nội địa khả thi, chi phí thương mại có thể quản lý được, và hỗ trợ thể chế, và nơi những điều này đồng thời vắng mặt thì quan hệ mà mô hình tiên đoán đơn giản là không xuất hiện. Phát hiện này tái định khung một dòng nghiên cứu lâu đời (Hitt et al., 1997; Lu & Beamish, 2004) thành *có điều kiện* thay vì áp dụng phổ quát, và nó đưa ra một lời giải thích cấu trúc cho các ước lượng yếu và bất ổn mà các nghiên cứu tái lập trên mẫu lớn đã báo cáo (Berry & Kaul, 2016; Pisani et al., 2020): việc gộp các bối cảnh giàu và nghèo điều kiện tiên quyết làm trung bình hóa các dạng hàm không tương thích.

### 5.2 Đóng góp của FIP như một khái niệm được giới hạn

Bằng việc gọi tên và giới hạn gánh nặng quốc tế hóa bắt buộc, chúng tôi cung cấp cho lĩnh vực này một nhãn cho trường hợp giới hạn tại vùng ngoại vi cực đoan và một tập tiêu chí phân biệt tách nó khỏi chi phí giai đoạn một của đường cong S, bất lợi của tính nước ngoài, và khởi nghiệp do nhu cầu. Giá trị của construct nằm ở việc đánh dấu nơi các lý thuyết quốc tế hóa phổ quát dừng lại, độc lập với hệ số chính xác mà người ta ước lượng, một ví dụ về phát triển lý thuyết thông qua việc đặc tả các điều kiện phạm vi.

### 5.3 Hàm ý chính sách

Đối với chính sách phát triển, kết quả cảnh báo trước việc dùng tăng cường xuất khẩu như một đòn bẩy tăng trưởng đứng-một-mình tại các vi quốc gia. Nếu các ràng buộc trói buộc là tính khả thi của thị trường nội địa, chi phí thương mại và thể chế, thì việc thúc đẩy cường độ xuất khẩu mà không giải quyết các điều kiện tiên quyết đó sẽ đẩy doanh nghiệp xa hơn vào nhánh đi xuống. Các can thiệp cấu trúc bổ trợ, hội nhập thị trường khu vực để nới lỏng ràng buộc quy mô nội địa, giảm chi phí thương mại, và phát triển thể chế có mục tiêu, là các điều kiện tiên quyết để tăng trưởng do xuất khẩu dẫn dắt mang lại các lợi ích năng suất. Điều này phù hợp với bằng chứng rằng tiến bộ phát triển tại SIDS chậm nhất từng được ghi nhận (Mahler, Serajuddin, Wadhwa, & Yonzan, 2026).

### 5.4 Hạn chế và nghiên cứu tương lai

Ba hạn chế giới hạn các phát hiện. Thứ nhất, thiết kế là các mặt cắt ngang lặp lại với ít cụm; chúng tôi giảm thiểu sự bác bỏ quá mức do ít cụm bằng wild bootstrap, nhưng nhận dạng nhân quả còn chờ dữ liệu bảng trên nhiều nền kinh tế đảo hơn. Thứ hai, thước đo áp dụng số chỉ là Tier-1 (website), chỉ báo có sẵn một cách so sánh được qua các đợt khảo sát SIDS; năng lực số phong phú hơn không thể đánh giá được. Thứ ba, khả năng khái quát hóa ngoài Thái Bình Dương chưa được kiểm định, các SIDS vùng Caribbean và Ấn Độ Dương là các bối cảnh mở rộng tự nhiên mà cũng sẽ nâng số cụm cần thiết cho suy luận sắc nét hơn. Một kiểm định dứt khoát về FIP như một hiệu ứng được ước lượng, thay vì một khái niệm giới hạn, đòi hỏi dữ liệu cấp doanh nghiệp đầy đủ hơn trên một tập rộng hơn các vi quốc gia.

## 6. Kết luận

Chữ U ngược là dạng hàm chủ lực của văn liệu quốc tế hóa–hiệu quả, nhưng logic tạo sinh của nó giả định trước các điều kiện tiên quyết về cấu trúc mà những nền kinh tế ngoại vi nhất thế giới thiếu vắng. Sử dụng dữ liệu cấp doanh nghiệp từ bảy quốc đảo Thái Bình Dương, chúng tôi cho thấy chữ U ngược tan biến tại vùng ngoại vi này, với bằng chứng gợi mở rằng, có điều kiện trên năng lực, quan hệ nghiêng về lồi, một hình phạt trên dải cường độ xuất khẩu nơi các doanh nghiệp đảo thực sự hoạt động. Chúng tôi gọi tên trường hợp giới hạn là gánh nặng quốc tế hóa bắt buộc và định vị nó như một điều kiện phạm vi của lý thuyết quốc tế hóa phổ quát. Mô hình là có điều kiện, không phổ quát: nơi thị trường nội địa quá nhỏ, chi phí thương mại quá cao, và thể chế quá mỏng, việc tăng cường quốc tế hóa không phải là con đường tới hiệu quả mà là một gánh nặng cấu trúc.

## Công bố về AI tạo sinh và công nghệ hỗ trợ AI trong quá trình viết

Trong quá trình chuẩn bị công trình này, (các) tác giả đã sử dụng Grammarly, một công cụ hỗ trợ viết, nhằm sửa lỗi chính tả, ngữ pháp và dấu câu trong văn bản gốc của chính (các) tác giả. Không có công cụ trí tuệ nhân tạo tạo sinh nào được sử dụng để tạo, soạn thảo hay sáng tạo bất kỳ nội dung, phân tích hay diễn giải thực chất nào. Sau khi sử dụng công cụ này, (các) tác giả đã rà soát và chỉnh sửa nội dung khi cần và chịu trách nhiệm hoàn toàn về nội dung của ấn phẩm.

## Tài liệu tham khảo

Bausch, A., & Krist, M. (2007). The effect of context-related moderators on the internationalization–performance relationship: Evidence from meta-analysis. *Management International Review, 47*(3), 319–347. https://doi.org/10.1007/s11575-007-0019-z

Berry, H., & Kaul, A. (2016). Replicating the multinationality–performance relationship: Is there an S-curve? *Strategic Management Journal, 37*(11), 2275–2290. https://doi.org/10.1002/smj.2567

Briguglio, L. (1995). Small island developing states and their economic vulnerabilities. *World Development, 23*(9), 1615–1632. https://doi.org/10.1016/0305-750X(95)00065-K

Cameron, A. C., Gelbach, J. B., & Miller, D. L. (2008). Bootstrap-based improvements for inference with clustered errors. *The Review of Economics and Statistics, 90*(3), 414–427. https://doi.org/10.1162/rest.90.3.414

Cohen, W. M., & Levinthal, D. A. (1990). Absorptive capacity: A new perspective on learning and innovation. *Administrative Science Quarterly, 35*(1), 128–152. https://doi.org/10.2307/2393553

Contractor, F. J., Kundu, S. K., & Hsu, C.-C. (2003). A three-stage theory of international expansion: The link between multinationality and performance in the service sector. *Journal of International Business Studies, 34*(1), 5–18. https://doi.org/10.1057/palgrave.jibs.8400003

Diamantopoulos, A., & Winklhofer, H. M. (2001). Index construction with formative indicators: An alternative to scale development. *Journal of Marketing Research, 38*(2), 269–277. https://doi.org/10.1509/jmkr.38.2.269.18845

Doh, J. P., Rodrigues, S., Saka-Helmhout, A., & Makhija, M. (2017). International business responses to institutional voids. *Journal of International Business Studies, 48*(3), 293–307. https://doi.org/10.1057/s41267-017-0074-z

Haans, R. F. J., Pieters, C., & He, Z.-L. (2016). Thinking about U: Theorizing and testing U- and inverted U-shaped relationships in strategy research. *Strategic Management Journal, 37*(7), 1177–1195. https://doi.org/10.1002/smj.2399

Hennart, J.-F. (2007). The theoretical rationale for a multinationality–performance relationship. *Management International Review, 47*(3), 423–452. https://doi.org/10.1007/s11575-007-0023-3

Hitt, M. A., Hoskisson, R. E., & Kim, H. (1997). International diversification: Effects on innovation and firm performance in product-diversified firms. *Academy of Management Journal, 40*(4), 767–798. https://doi.org/10.2307/256948

Hsieh, C.-T., & Klenow, P. J. (2009). Misallocation and manufacturing TFP in China and India. *The Quarterly Journal of Economics, 124*(4), 1403–1448. https://doi.org/10.1162/qjec.2009.124.4.1403

Jarvis, C. B., MacKenzie, S. B., & Podsakoff, P. M. (2003). A critical review of construct indicators and measurement model misspecification in marketing and consumer research. *Journal of Consumer Research, 30*(2), 199–218. https://doi.org/10.1086/376806

Johanson, J., & Vahlne, J.-E. (1977). The internationalization process of the firm: A model of knowledge development and increasing foreign market commitments. *Journal of International Business Studies, 8*(1), 23–32. https://doi.org/10.1057/palgrave.jibs.8490676

Johanson, J., & Vahlne, J.-E. (2009). The Uppsala internationalization process model revisited: From liability of foreignness to liability of outsidership. *Journal of International Business Studies, 40*(9), 1411–1431. https://doi.org/10.1057/jibs.2009.24

Khanna, T., & Palepu, K. G. (2010). *Winning in emerging markets: A road map for strategy and execution*. Harvard Business Press.

Kirca, A. H., Hult, G. T. M., Roth, K., Cavusgil, S. T., Perry, M. Z., Akdeniz, M. B., Deligonul, S. Z., Mena, J. A., Pollitte, W. A., Hoppner, J. J., Miller, J. C., & White, R. C. (2011). Firm-specific assets, multinationality, and financial performance: A meta-analytic review and theoretical integration. *Academy of Management Journal, 54*(1), 47–72. https://doi.org/10.5465/amj.2011.59215090

Lall, S. (1992). Technological capabilities and industrialization. *World Development, 20*(2), 165–186. https://doi.org/10.1016/0305-750X(92)90097-F

Lind, J. T., & Mehlum, H. (2010). With or without U? The appropriate test for a U-shaped relationship. *Oxford Bulletin of Economics and Statistics, 72*(1), 109–118. https://doi.org/10.1111/j.1468-0084.2009.00569.x

Lu, J. W., & Beamish, P. W. (2004). International diversification and firm performance: The S-curve hypothesis. *Academy of Management Journal, 47*(4), 598–609. https://doi.org/10.2307/20159604

Mahler, D. G., Serajuddin, U., Wadhwa, D., & Yonzan, N. (2026, April). *The world is developing at its slowest pace in 75 years* (Policy Research Working Paper No. 11350). World Bank Group.

Melitz, M. J. (2003). The impact of trade on intra-industry reallocations and aggregate industry productivity. *Econometrica, 71*(6), 1695–1725. https://doi.org/10.1111/1468-0262.00467

North, D. C. (1990). *Institutions, institutional change and economic performance*. Cambridge University Press. https://doi.org/10.1017/CBO9780511808678

Pisani, N., Garcia-Bernardo, J., & Heemskerk, E. (2020). Does it pay to be a multinational? A large-sample, cross-national replication assessing the multinationality–performance relationship. *Strategic Management Journal, 41*(1), 152–172. https://doi.org/10.1002/smj.3087

Sarasvathy, S. D., Kumar, K., York, J. G., & Bhagavatula, S. (2014). An effectual approach to international entrepreneurship: Overlaps, challenges, and provocative possibilities. *Entrepreneurship Theory and Practice, 38*(1), 71–93. https://doi.org/10.1111/etap.12088

Verbeke, A., & Brugman, P. (2018). Triple-testing the quality of multinationality–performance research: An internalization theory perspective. *International Business Review, 27*(2), 333–351. https://doi.org/10.1016/j.ibusrev.2017.09.005

Winters, L. A., & Martins, P. M. G. (2004). When comparative advantage is not enough: Business costs in small remote economies. *World Trade Review, 3*(3), 347–383. https://doi.org/10.1017/S1474745604001922

Zaheer, S. (1995). Overcoming the liability of foreignness. *Academy of Management Journal, 38*(2), 341–363. https://doi.org/10.2307/256683

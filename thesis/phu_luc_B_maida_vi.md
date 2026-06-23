# PHỤ LỤC B: CÔNG CỤ TRÍCH XUẤT DỮ LIỆU META-ANALYSIS M-AIDA

> Phụ lục này mô tả phần mềm **M-AIDA** (Meta-Analysis Intelligent Data Assistant,
> phiên bản 7.0) — công cụ do chính nghiên cứu sinh phát triển và đã nộp hồ sơ đăng ký
> quyền tác giả, dùng để trích xuất và quản trị dữ liệu cỡ ảnh hưởng cho cấu phần phân
> tích tổng hợp của luận án (Nghiên cứu thành phần P6). Phụ lục được trình bày như **một
> cấu phần minh bạch phương pháp luận**, nhằm bảo đảm khả năng tái lập, công bố sử dụng
> trí tuệ nhân tạo, và khả năng phản biện trước hội đồng.

## B.1 Mục đích và vị trí trong thiết kế nghiên cứu

Cấu phần phân tích tổng hợp (Mục 3.2) tổng hợp K=288 cỡ ảnh hưởng từ k=238 nghiên cứu
thực nghiệm về quan hệ quốc tế hóa–hiệu quả (I–P) giai đoạn 1977–2026. Trích xuất thủ
công thuần túy ở quy mô này vừa tốn kém vừa dễ phát sinh sai số ghi chép; ngược lại, trích
xuất hoàn toàn tự động bằng mô hình ngôn ngữ lớn (LLM) lại tiềm ẩn rủi ro "ảo giác" số liệu
và thiếu dấu vết kiểm toán. M-AIDA được thiết kế để dung hòa: tận dụng tốc độ của LLM cho
khâu đọc–trích, đồng thời đặt **toàn bộ quyền quyết định cuối cùng vào tay nghiên cứu sinh**
(Principal Investigator, PI) thông qua quy trình xác minh và khóa dữ liệu bất biến.

## B.2 Kiến trúc phần mềm

M-AIDA gồm hai thành phần, giao tiếp qua REST API:

- **Backend — FastAPI (Python 3.11+).** Các mô-đun chính: `extractor.py` (lớp
  `StatisticalExtractor`: pipeline LLM trích cỡ ảnh hưởng từ văn bản PDF), `models.py`
  (các mô hình dữ liệu Pydantic: `ExtractedEffect`, `StudyDatabaseEntry`,
  `VerificationDecision`), `settings.py` (cấu hình runtime), `notion_sync.py` (đồng bộ
  cơ sở dữ liệu nghiên cứu). Thư viện xử lý: PyMuPDF (đọc PDF), Anthropic Claude SDK
  (pipeline LLM), pandas/numpy/scipy (xử lý thống kê).
- **Frontend — React 18 + TypeScript.** Bố cục hai thẻ: thẻ *Trích xuất* (upload PDF,
  hiển thị kết quả LLM) và thẻ *Xác minh & Khóa* (bảng điều khiển để PI rà soát, ghi đè,
  phê duyệt và khóa từng nghiên cứu), kèm chức năng xuất CSV các nghiên cứu đã khóa.

## B.3 Quy trình trích xuất và chuyển đổi cỡ ảnh hưởng

Với mỗi PDF, M-AIDA đọc toàn văn bằng PyMuPDF rồi gửi tới LLM với một system prompt
chuyên biệt cho meta-analysis I–P, yêu cầu nhận diện: cỡ mẫu $N$, hệ số tương quan
Pearson $r$, thống kê $t$, bậc tự do $df$, hệ số hồi quy chuẩn hóa $\beta$, giá trị $p$,
khoảng tin cậy 95%; đồng thời phân loại hai chiều xác định được từ văn bản (thước đo
quốc tế hóa: FSTS/GEO/EXP/FDI/COMP/OTH; thước đo hiệu quả: ACC/MKT/LAB/MIX) và cửa sổ
dữ liệu. Khi chỉ có thống kê phái sinh, hệ thống chuyển đổi về $r$ theo chuẩn:

$$ r = \sqrt{\dfrac{t^2}{t^2 + df}} \quad \text{(Cohen, 1988)}; \qquad r \approx 0{,}98\,\beta \quad \text{(Peterson \& Brown, 2005)}. $$

Mỗi bản ghi được gán **điểm tin cậy trích xuất** ba mức: 1,0 (lấy trực tiếp $r$), 0,8
(suy từ $t$), 0,6 (suy từ $\beta$); bản ghi có độ tin cậy dưới 0,7 tự động bị gắn cờ
`requires_verification`.

## B.4 Quản trị dữ liệu: nguyên tắc tách bạch, xác minh PI và khóa bất biến

Ba nguyên tắc quản trị bảo đảm tính kiểm chứng độc lập và liêm chính:

1. **Tách bạch máy–người.** LLM **chỉ** trích thống kê. Các biến điều tiết thể chế của
   luận án — chế độ ICRV (I/II/III/FR/MX theo WGI Rule of Law), pha DPL (PRE/SPN/FOL theo
   năm dữ liệu trung vị) và chỉ số cDAI (Digital Adoption Index 0–1) — **do PI gán thủ
   công từ bảng tra cứu ngoài**, không để LLM suy đoán.
2. **Xác minh PI.** PI có thể áp `field_overrides` lên bất kỳ trường nào của bản ghi và
   ghi `pi_notes`; chỉ khi PI phê duyệt thì cờ `requires_verification` mới chuyển sang
   `False`.
3. **Khóa bất biến (irreversible lock).** Bản ghi đã phê duyệt được khóa vĩnh viễn
   (`pi_locked = True`, kèm `locked_at` theo giờ UTC); thao tác **không thể đảo ngược**.
   Chỉ các bản ghi đã khóa mới được xuất ra tập dữ liệu phân tích tổng hợp.

Cơ chế hai bước phê duyệt–khóa tạo **dấu vết kiểm toán (audit trail)** phân tách rõ phần
do máy trích xuất với phần do con người quyết định — đặc tính cốt lõi giúp kết quả meta-
analysis có thể tái lập và phản biện.

## B.5 Công bố sử dụng trí tuệ nhân tạo và liêm chính học thuật

Theo các khuyến nghị công bố sử dụng AI ngày càng phổ biến ở tạp chí học thuật, luận án
công bố minh bạch: (i) LLM được dùng **chỉ ở khâu trích xuất thống kê** trong cấu phần
phân tích tổng hợp, không dùng để sinh nội dung khoa học, không dùng để gán biến điều
tiết hay diễn giải kết quả; (ii) **toàn bộ** bản ghi đưa vào phân tích đã qua kiểm chứng
100% và phê duyệt của nghiên cứu sinh, kèm khóa dữ liệu bất biến; (iii) tập dữ liệu đã
khóa và mã nguồn công cụ được lưu giữ phục vụ kiểm tra tái lập. Nhờ đó, vai trò của trí
tuệ nhân tạo là **hỗ trợ năng suất ở khâu cơ học**, trong khi trách nhiệm khoa học và mọi
quyết định nội dung thuộc về nghiên cứu sinh.

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

# PHỤ LỤC {.unnumbered}

Các phụ lục kèm theo luận án (nghiên cứu sinh đính kèm nội dung đầy đủ tương ứng):

**Phụ lục A — Bảng thuật ngữ Anh–Việt thống nhất.** Danh mục 68 thuật ngữ chuẩn hóa dùng xuyên
suốt luận án và hai chuyên đề (nguồn: `thesis/09b_vn_term_glossary.md`).

**Phụ lục B — Quy trình tổng hợp và trích xuất dữ liệu (Chương 3 / Paper 6).** Mô tả phần mềm
M-AIDA (Meta-Analysis Intelligent Data Assistant) — công cụ trích xuất mức ảnh hưởng từ nghiên cứu
sơ cấp đưa vào phân tích tổng hợp; đã đăng ký bản quyền tại Cục Bản quyền Tác giả (COV).

**Phụ lục C — Tiền đăng ký nghiên cứu (OSF).** Phân tích tổng hợp ba tầng được tiền đăng ký tại
OSF: https://osf.io/z37kn (DOI: 10.17605/OSF.IO/Z37KN).

**Phụ lục D — Bảng dữ liệu và kết quả bổ trợ.** Các bảng hệ số đầy đủ, sơ đồ PRISMA, kiểm định độ
vững và chẩn đoán sai lệch xuất bản của các nghiên cứu thành phần (P3–P8).

**Phụ lục E — Danh sách nền kinh tế và phân nhóm chế độ thể chế (ICRV).** Bảng phân loại các nền
kinh tế theo sáu nhóm ICRV dùng trong luận án.

**Phụ lục F — Quy trình gộp dữ liệu châu Á và triển khai phương pháp ước lượng (Paper 7,
nghiên cứu capstone Chương 4).** Mô tả chi tiết, có thể tái lập: (i) quy trình hài hòa hóa và gộp
microdata Điều tra Doanh nghiệp của Ngân hàng Thế giới (WBES) trên phạm vi châu Á theo định nghĩa
địa lý, kèm cơ sở xác định phạm vi mẫu; và (ii) cách triển khai hệ thống mô hình ước lượng phân cấp
M0–M11. Nội dung đầy đủ trình bày dưới đây (nguồn mã: `p7/replication/01_build_p7_dataset.py` và
`p7/replication/02_run_p7_models.py`).

*[Các Phụ lục A–E là khung danh mục theo yêu cầu CTU; nghiên cứu sinh chèn nội dung chi tiết của
từng phụ lục vào bản nộp cuối cùng. Phụ lục F được trình bày đầy đủ ngay sau đây.]*

```{=openxml}
<w:p><w:r><w:br w:type="page"/></w:r></w:p>
```

## Phụ lục F. Quy trình gộp dữ liệu châu Á và triển khai phương pháp ước lượng {.unnumbered}

Phụ lục này tài liệu hóa toàn bộ quy trình từ dữ liệu thô đến kết quả ước lượng của nghiên cứu
capstone (Paper 7), nhằm bảo đảm tính minh bạch và khả năng tái lập. Hai mã nguồn tham chiếu là
`p7/replication/01_build_p7_dataset.py` (xây dựng và hài hòa hóa tập dữ liệu gộp) và
`p7/replication/02_run_p7_models.py` (ước lượng và kiểm định). Mọi con số trích dẫn trong Chương 4
đều được tái sinh trực tiếp từ hai mã này; các tệp kết quả tương ứng được liệt kê tại Mục F.8.

### F.1. Nguồn dữ liệu và cơ sở xác định phạm vi địa lý

Dữ liệu là microdata cấp doanh nghiệp từ Điều tra Doanh nghiệp của Ngân hàng Thế giới (World Bank
Enterprise Surveys, WBES) — khảo sát chọn mẫu ngẫu nhiên phân tầng đối với doanh nghiệp tư nhân
chính thức trong khu vực phi nông nghiệp, phi khai khoáng (ISIC Rev. 3.1/4: chế tạo, xây dựng, bán
lẻ và dịch vụ khác), với khung chọn mẫu phân tầng theo ngành, quy mô doanh nghiệp (nhỏ 5–19, vừa
20–99, lớn từ 100 lao động) và địa bàn dưới quốc gia. Mỗi tầng được thiết kế đạt độ chính xác 7,5%
ở mức tin cậy 90% (tối thiểu 120 doanh nghiệp mỗi tầng), và trọng số thiết kế (`wstrict`, `wmedian`)
được lưu giữ để hiệu chỉnh về tổng thể khi cần.

**Cơ sở xác định phạm vi (định nghĩa địa lý, nhất quán xuyên lục địa).** Mẫu được xác định trên một
định nghĩa *địa lý* của châu Á thay vì theo phân vùng hành chính của Ngân hàng Thế giới, nhằm khắc
phục một quy tắc phạm vi thiếu nhất quán đã được phát hiện (loại Thổ Nhĩ Kỳ/Azerbaijan nhưng giữ
Armenia/Gruzia/Síp — vốn cùng được Ngân hàng Thế giới xếp vào vùng "Europe & Central Asia"). Áp
dụng hệ phân vùng thống kê M.49 của Liên Hợp Quốc (United Nations Statistics Division, 2024), mẫu
bao gồm năm tiểu vùng châu Á (Đông Á, Đông Nam Á, Nam Á, Trung Á và Tây Á) cộng với khu vực Thái
Bình Dương. Để giữ cho khung mẫu nhất quán, mọi nền kinh tế nằm vắt ngang ranh giới Âu–Á đều bị
loại trừ: vùng Nam Kavkaz xuyên lục địa (Armenia, Azerbaijan, Gruzia), Thổ Nhĩ Kỳ và Síp; đồng thời
loại Comoros (châu Phi hạ Sahara). Trung Á và vùng Vịnh/Levant thuộc Tây Á được giữ lại vì là bộ
phận không tranh cãi của lục địa Á. Tập biến loại trừ trong mã nguồn là:

> `out_of_scope = {"Turkey", "Azerbaijan", "Armenia", "Georgia", "Cyprus", "Comoros"}`

Quy tắc này có cơ sở thực nghiệm: một định nghĩa M.49 nghiêm ngặt tái nạp Thổ Nhĩ Kỳ/Azerbaijan đã
được thử nghiệm và *phá vỡ* quan hệ chữ U ngược (điểm ngưỡng giảm 31%, p = ,54), trong khi phạm vi
địa lý nhất quán xuyên lục địa cho kết quả vững (xem Mục F.7). Sau khi lọc, mẫu phân tích gồm
N = 82.302 quan sát doanh nghiệp, 45 nền kinh tế và 98 đợt khảo sát quốc gia–năm (2003–2025), trải
đủ sáu nhóm của khung Biến thiên Chế độ Bối cảnh Thể chế (ICRV).

*Lưu ý kỹ thuật về số đếm:* tệp kiểm toán `p7_audit.json` liệt kê 48 khóa quốc gia, trong đó ba khóa
là biến thể dữ liệu bảng (`Mongolia_panel`, `Nepal_panel`, `Philippines_panel`) được tách từ tệp gốc
dạng panel (xem Mục F.3); sau khi quy về nền kinh tế duy nhất, số nền kinh tế phân biệt là 45.

### F.2. Hài hòa hóa biến số xuyên các đợt khảo sát

Do bộ câu hỏi WBES thay đổi mã biến qua các đợt và quốc gia, mỗi biến đích được ánh xạ tới một danh
sách mã biến gốc *theo thứ tự ưu tiên*; mã đầu tiên hiện diện trong tệp sẽ được sử dụng (cấu trúc
`VAR_MAP` và hàm `extract_var`). Quy ước xử lý khuyết được áp dụng đồng nhất: mọi mã âm theo quy ước
WBES (−9 "không biết", −8 "khác", −7 "chỉ một cơ sở", −6 "từ chối", … đến −1) được quy về khuyết
(`NaN`); biến nhị phân mã hóa 1 = có / 2 = không được tái mã thành 1/0; biến tỷ lệ phần trăm âm bị
loại. Bảng F.1 tóm tắt ánh xạ từ mã nguồn WBES sang biến phân tích.

| Biến phân tích | Mã WBES (ưu tiên) | Cách dựng |
|---|---|---|
| Năng suất lao động `ln_labor_prod` | `n3` (hoặc `d2`); `l1` | ln(doanh thu / số lao động chính thức) |
| Cường độ quốc tế hóa `FSTS` | `d3b`, `d3c` (dự phòng `d3a`) | (xuất khẩu gián tiếp + trực tiếp)/100 |
| Năng lực số `dai_z` | `c22b`/`e1` (website); `k33` (thanh toán điện tử) | trung bình chuẩn hóa (z) các thành phần khả dụng |
| Năng lực công nghệ `tci_z` | `b8` (chứng nhận chất lượng); `e6` (công nghệ nước ngoài) | trung bình chuẩn hóa (z) các thành phần khả dụng |
| Kinh nghiệm quản lý `mgr_experience` | `b7` | số năm kinh nghiệm ngành của quản lý cấp cao |
| Quản lý nữ `mgr_female` | `b7a` | nhị phân 1/0 |
| Sở hữu nữ `female_owner` | `b4` | nhị phân 1/0 |
| Tỷ lệ sở hữu nước ngoài `foreign_own_pct` | `b6a` | phần trăm |
| Tuổi doanh nghiệp `firm_age` | `b5` | năm khảo sát − năm thành lập |
| Quy mô `ln_size` | `l1` | ln(số lao động, chặn dưới = 1) |
| Tầng quy mô `size_strata` | `a4a` | 1 = nhỏ, 2 = vừa, 3 = lớn |
| Ngành ISIC `isic_sector` | `a6a`/`a6b` | mã ngành |
| Trọng số khảo sát | `wstrict`, `wmedian` | trọng số thiết kế |

Hai chỉ số năng lực được dựng dưới dạng *hợp số chuẩn hóa*: với mỗi thành phần khả dụng, giá trị
được chuẩn hóa z trong nội bộ tệp quốc gia–năm rồi lấy trung bình, cho phép chỉ số vẫn xác định khi
chỉ một thành phần hiện diện ở một đợt khảo sát nhất định — một giải pháp đối với tính không đồng đều
của bộ câu hỏi WBES. Mỗi doanh nghiệp được gán nhóm ICRV (`ICRV_MAP`, sáu nhóm) và tiểu vùng địa lý
(`REGION_MAP`).

### F.3. Xử lý trùng lặp tệp và tách dữ liệu bảng

Quy trình duyệt toàn bộ tệp `.dta` và áp dụng các quy tắc làm sạch ở cấp tệp: (i) loại các tệp không
phù hợp xử lý đơn-năm theo từ khóa (`ISBS`, `ISES`, `Informal`, `LongForm`, `paneldata`, tài liệu
mô tả…); (ii) *khử trùng lặp* các tệp đơn-năm — với mỗi cặp (quốc gia, năm), giữ tệp có dung lượng
lớn nhất; (iii) *tách dữ liệu bảng* — các tệp panel (tên chứa hai năm) được tách theo cột `year`, và
chỉ được nạp khi cặp (quốc gia, năm) tương ứng chưa có tệp đơn-năm. Cơ chế (iii) giải thích sự hiện
diện của ba khóa `*_panel` nêu ở Mục F.1. Tên quốc gia được chuẩn hóa qua `NAME_MAP` (ví dụ
`HongKongSARChina` → `HongKong`, `KoreaRepublic` → `Korea`) để bảo đảm gộp nhất quán.

Đầu ra của bước này gồm ba tệp: `p7_pooled_clean.csv` (tệp phân tích, một dòng mỗi doanh nghiệp),
`p7_manifest.csv` (độ phủ quốc gia–năm và N mỗi đợt) và `p7_variable_log.csv` (tính khả dụng của
từng biến theo tệp).

### F.4. Biến phụ thuộc, biến giải thích và phép định tâm trong nhóm

Biến phụ thuộc là logarit năng suất lao động, ln(LP) = ln(doanh thu/lao động). Biến giải thích trung
tâm là cường độ quốc tế hóa FSTS. Để tách hiệu ứng *trong nội bộ* khỏi chênh lệch mức giữa các đợt
khảo sát (khác biệt mặt bằng giá, tỷ giá, chu kỳ), FSTS được *định tâm theo trung bình nhóm quốc
gia–năm*:

> FSTS_c = FSTS − trung bình_{quốc gia × năm}(FSTS),  và  FSTS_c² = (FSTS_c)²

Phép định tâm trong nhóm này khử thành phần liên-nhóm của FSTS, do đó hệ số của số hạng bậc hai phản
ánh độ cong *trong* từng bối cảnh quốc gia–năm chứ không phải khác biệt giữa các bối cảnh. Các số
hạng tương tác được dựng tường minh từ FSTS_c và FSTS_c² nhân với các *nhân tố điều tiết trọng tâm*
(`tci_z`, `dai_z`, `icrv_group`), bao gồm cả tương tác hai chiều và ba chiều (FSTS_c × DAI × ICRV).
Lưu ý: các đặc điểm nhà quản trị cấp cao (`mgr_experience`, `mgr_female`) **không** được xử lý như
nhân tố điều tiết trọng tâm mà như nhóm biến kiểm soát quản trị (xem Mục F.5); các số hạng
FSTS_c × nhà quản trị (`fsts_c_x_mgr`, `fsts_c_x_female`) tuy được dựng nhưng chỉ báo cáo như chẩn
đoán phụ trợ, không phải bằng chứng điều tiết.

### F.5. Tiêu chí mẫu phân tích

Hai bộ lọc xác định mẫu phân tích. Thứ nhất, các đợt quốc gia–năm có dưới 50 quan sát hoàn chỉnh ở
bốn biến lõi (ln_labor_prod, FSTS, tci_z, dai_z) bị loại (tham số `--min-n`, mặc định 50), nhằm bảo
đảm mỗi bối cảnh đóng góp đủ thông tin cho hiệu ứng cố định quốc gia–năm. Thứ hai, mẫu cho từng mô
hình yêu cầu không khuyết ở các biến của mô hình đó: mẫu nền (M0–M2) yêu cầu ln(LP) và FSTS_c; các
mô hình mở rộng bổ sung yêu cầu tci_z, dai_z, biến quản lý và biến kiểm soát tương ứng. Biến kiểm
soát doanh nghiệp được đưa vào *động* — chỉ giữ các biến hiện diện và có trên 100 quan sát không
khuyết (female_owner, foreign_own_pct, firm_age, ln_size). Việc cỡ mẫu giảm dần từ M2 (N = 82.302)
đến M11 (N = 28.500) phản ánh yêu cầu dữ liệu tăng dần của các đặc tả phức tạp hơn, và được báo cáo
minh bạch trong bảng kết quả.

**Xử lý đặc điểm nhà quản trị cấp cao như biến kiểm soát.** Nhất quán với Mục 3.3.5 của Chương 3,
các đặc điểm nhà quản trị cấp cao (kinh nghiệm theo năm và biến chỉ báo quản trị nữ) được đưa vào từ
M9 trở đi như **nhóm biến kiểm soát quản trị nội sinh**: chúng tác động ở dạng hiệu ứng mức (level
effect) nâng mặt bằng năng suất, *không* định hình độ cong của đường quan hệ I–P. Việc kiểm soát
chất lượng quản trị theo lý thuyết Bậc trên (Upper Echelons; Hambrick & Mason, 1984) nhằm khóa chặt
thiên lệch nội sinh và tăng tính nhận dạng riêng phần của tương tác trọng tâm Thể chế × Công nghệ.
Ký hiệu H4 được giữ nguyên thuần túy để tương thích với các bản thảo đồng hành (P3/P4/P5); số hạng
tương tác FSTS × đặc điểm quản trị chỉ là chẩn đoán phụ trợ và không cấu thành bằng chứng điều tiết
trọng tâm.

### F.6. Phương pháp ước lượng và kiểm định

**Ước lượng viên.** Tất cả mô hình là hồi quy bình phương nhỏ nhất (OLS) ước lượng bằng
`statsmodels` với sai số chuẩn vững với phương sai thay đổi loại HC1 (`cov_type="HC1"`). Lựa chọn
HC1 phù hợp với dữ liệu chéo gộp có phương sai phần dư không đồng nhất giữa doanh nghiệp và bối
cảnh.

**Kiểm định chữ U ngược (Lind–Mehlum, 2010).** Sự tồn tại của quan hệ chữ U ngược không được suy ra
chỉ từ dấu của hệ số bậc hai. Áp dụng kiểm định Lind–Mehlum, điểm ngưỡng (turning point) được tính:

> TP = − β₁ / (2 β₂),  với điều kiện cần β₂ < 0.

Kiểm định khớp đồng thời hai điều kiện: độ dốc tại biên trái dương và độ dốc tại biên phải âm; giá
trị p hợp nhất được lấy bảo thủ bằng cực đại của hai giá trị p một phía, p_LM = max[p(β₂ < 0),
p(β₁ > 0)]. Khoảng tin cậy của điểm ngưỡng được xấp xỉ bằng phương pháp delta (Fieller) từ ma trận
hiệp phương sai của β₁ và β₂. Một quan hệ được xác nhận là chữ U ngược khi β₂ < 0 *và* p_LM < ,10.
Các kiểm định F khớp đồng thời cũng được dùng cho cụm số hạng điều tiết (ví dụ
`fsts_c_x_tci = 0, fsts_c2_x_tci = 0` trong M7; cụm DAI trong M8).

### F.7. Hệ thống mô hình phân cấp M0–M11

Hệ thống mô hình được xây dựng phân cấp, mỗi bước bổ sung một khối lý thuyết và gắn với một giả
thuyết. (Đánh số mô hình bỏ trống M4 do tái cấu trúc; thứ tự thực thi như dưới đây.)

| Mô hình | Đặc tả bổ sung so với bước trước | Giả thuyết / vai trò |
|---|---|---|
| M0 | Chỉ hệ số chặn | Mốc so sánh |
| M1 | + FSTS_c (tuyến tính) | Hiệu ứng tuyến tính |
| M2 | + FSTS_c² (bậc hai) | H1 — chữ U ngược |
| M3 | M2 + biến kiểm soát | Vững với đặc điểm doanh nghiệp |
| M5 | M3 + hiệu ứng cố định quốc gia–năm `C(cy_fe)` | Hấp thụ dị biệt bối cảnh không quan sát |
| M6 | M3 + TCI (hiệu ứng chính) | H2 — hiệu ứng mức |
| M7 | M6 + FSTS_c × TCI + FSTS_c² × TCI | H2 — điều tiết độ cong |
| M8 | M7 + DAI + FSTS_c × DAI + FSTS_c² × DAI | H3 — điều tiết số hóa |
| M9 | M8 + kinh nghiệm và giới tính nhà quản trị cấp cao (biến kiểm soát quản trị nội sinh; số hạng tương tác FSTS chỉ để chẩn đoán) | H4 (giữ nhãn để tương thích P3/P4/P5) — kiểm soát quản trị, *không* phải điều tiết trọng tâm |
| M10 | + ICRV + FSTS_c × ICRV + FSTS_c² × ICRV | H5 — điều tiết chế độ thể chế |
| M11 | Mô hình ba chiều đầy đủ: FSTS_c × DAI × ICRV và các tương tác cấu thành | H6 — điều tiết ba chiều |

Trong M10–M11, `icrv_group` được đưa vào dạng thang liên tục (Nhóm I→VI) cho các số hạng tương tác;
khi cần dạng phân loại, các biến giả nhóm (tham chiếu = Nhóm III, Upper-mid) cũng được dựng sẵn. Mô
hình M5 dùng hiệu ứng cố định quốc gia–năm để kiểm tra tính vững của điểm ngưỡng trước dị biệt bối
cảnh thay đổi theo thời gian.

### F.8. Tệp kết quả và khả năng tái lập

Chạy `02_run_p7_models.py` tái sinh bốn tệp kết quả là nguồn chân lý cho mọi con số trong Chương 4:
`p7_coefs_all_models.csv` (hệ số đầy đủ mọi mô hình), `p7_summary_focal.csv` (các số hạng trọng
tâm), `p7_model_fit.csv` (cỡ mẫu, R² hiệu chỉnh, điểm ngưỡng, p_LM, hình dạng) và `p7_audit.json`
(N, số quốc gia, số đợt, danh mục mô hình). Phân tích so sánh đa chiều hiệu quả doanh nghiệp (năng
suất lao động so với tăng trưởng doanh thu ba năm) được tạo bởi `03_multidim_performance.py`, xuất
`p7_multidim_comparison.csv`. Toàn bộ quy trình có thể tái lập từ microdata thô qua hai lệnh:

> `python3 p7/replication/01_build_p7_dataset.py`
> `python3 p7/replication/02_run_p7_models.py`

# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 2: CHƯƠNG 4 — THỰC TRẠNG TỪ WBES)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md`.
> Phần 3 (Chương 5–7 + TLTK): `thesis/16_cd1_part3_cases_conclusion_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Hình minh họa: `thesis/figures/` (**11 hình**; chạy `python3 generate_figures.py` để regen).
---

## CHƯƠNG 4 — THỰC TRẠNG HIỆU QUẢ DOANH NGHIỆP CHÂU Á 2009–2025

### 4.1 Nguồn dữ liệu World Bank Enterprise Surveys

**Phạm vi tổng hợp dữ liệu**. Nhóm dữ liệu (pool) gồm **101.185 doanh nghiệp** ở 47 nền kinh tế, với **108 cặp quốc gia theo năm**, trải dài giai đoạn 2009–2025. Tổng hợp này kế thừa và mở rộng từ 17 nước châu Á mới nổi (khoảng 40.633 doanh nghiệp) của Đỗ & Phan (2026 — VEFR), tức gấp khoảng 2,5 lần. Phân bố theo phân nhóm con (sub-regime) ICRV như sau: Emerging 47.803 (47%), Frontier 28.678 (28%), Upper-middle 16.693 (17%), Advanced 6.640 (7%) và **SIDS 1.371 (1,4%, gồm Kiribati 2025)**. Riêng năm 2025 có **14 đợt khảo sát** với 16.979 doanh nghiệp.

![Hình 4.1.1 — Phân bố pool 5 phân nhóm con thể chế (n=101.185 doanh nghiệp)](figures/fig_4_1_pool_composition.png)

*Hình 4.1.1. Bar chart phân bố theo 5 phân nhóm con: Emerging (47.803, 47,2%), Frontier (28.678, 28,3%), Upper-middle (16.693, 16,5%), Advanced (6.640, 6,6%), SIDS Thái Bình Dương (1.371, 1,4%, gồm Kiribati 2025). Tái lập: `thesis/figures/generate_figures.py` function `fig_4_1_pool_composition()`.*

![Hình 4.0 — Phân bố mẫu 101.185 doanh nghiệp xuyên 17 năm (2009–2025) theo 3 thế hệ schema WBES](figures/fig_4_0_pool_by_year.png)

*Hình 4.0. Phân bố mẫu doanh nghiệp xuyên 17 năm theo 3 thế hệ schema WBES: PICS3 (2009-2012, n=14.171), Standardized (2013-2017, n=24.564), BREADY (2018-2025, n=62.450 gồm Kiribati 2025). Đợt 2025 đột biến với 16.979 doanh nghiệp = 16,8% pool — đợt khảo sát đơn năm lớn nhất. Tái lập: `generate_figures.py` function `fig_4_0_pool_by_year()`.*

**Trường hợp biên (boundary cases)**: gồm **7 SIDS Thái Bình Dương đầy đủ (FJI, PNG, SLB, TON, VUT, WSM, KIR)** cùng 9 nước Tây Á. Phân bố theo thời gian: 2009–2012 (n=14.171), 2013–2017 (n=24.564) và 2018–2025 (n=62.450, chiếm 62%). Dữ liệu trải qua ba thế hệ khung (schema): PICS3/MENA-WBES, Standardized và Standardized2018+/BREADY.

**Hài hòa dữ liệu**. Pipeline được viết bằng Python (`wbes/02_harmonize.py`); FSTS tính theo `d3b + d3c`; giới hạn cực trị (winsorize) log năng suất ở mức 1/99 phân vị trong cụm quốc gia theo năm. Doanh thu chưa quy đổi sang USD PPP.

### 4.2 Thực trạng năng suất lao động — phân tán trong từng quốc gia

**Bảng 4.1**. *Phân tán (dispersion) năng suất lao động theo phân nhóm con thể chế (n=108 cặp QG×năm — v3.1).*

| Phân nhóm con | Cặp QG×năm | n_firms | sd log | P90/P10 | P75/P25 |
|---|---|---|---|---|---|
| **Advanced — innovation-driven** *(SG, HK, KOR, TWN, ISR)* | ~8 | ~4.220 | **1,03** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| **Advanced — resource-driven** *(SAU, QAT, KWT, BHR, BRN)* | ~5 | ~1.932 | **0,49** | (cập nhật GĐ1) | (cập nhật GĐ1) |
| *Advanced (gộp — tham chiếu)* | 13 | 5.921 | 0,86 | 10,8 | 3,1 |
| Upper-middle | 18 | 15.174 | 1,29 | 27,7 | 5,4 |
| Emerging | 20 | 45.388 | 1,24 | 30,6 | 5,1 |
| Frontier | 42 | 18.877 | 1,36 | 39,6 | 6,1 |
| **SIDS Thái Bình Dương (v3.1: gồm Kiribati 2025)** | **10** | **1.097** | **1,32** | (cập nhật GĐ1) | (cập nhật GĐ1) |

*Ghi chú: Advanced tách 2 phân nhóm con ở v3.1 — tỷ số phân tán Singapore (1,03) so với Vùng Vịnh (0,49) ≈ **2,1 lần**. SIDS row v3.1 với Kiribati 2025 (n=150, sd log 1,48).*

![Hình 4.2 — Phân phối năng suất theo 6 phân nhóm con (kernel density, n=101.185)](figures/fig_4_2_productivity_density.png)

*Hình 4.2. Đồ thị mật độ kernel cho 6 phân nhóm con: Advanced innovation (sd 1,03), Advanced resource (sd 0,49), Upper-middle (1,29), Emerging (1,24), Frontier (1,36), SIDS (1,32). Phân nhóm tài nguyên dẫn dắt (Vùng Vịnh) phân tán hẹp nhất; Frontier rộng nhất. Tái lập: `generate_figures.py` function `fig_4_2_productivity_density()`.*

Có thể rút ra 5 phát hiện: (1) phân tán của Advanced gộp giảm từ 1,00 còn 0,86 sau khi bổ sung Vùng Vịnh, một dấu hiệu của dị biệt nội bộ; (2) Frontier cao nhất, phù hợp với **giả thuyết phân bổ sai nguồn lực (misallocation hypothesis)** của Hsieh & Klenow (2009, 2014); (3) SIDS ở mức trung bình, khoảng 1,32 (v3.1); (4) tỷ số P90/P10 tăng đơn điệu theo phân nhóm con; và (5) bằng chứng cho H5 về điều tiết thể chế (institutional moderation).

### 4.3 Thực trạng quốc tế hóa và tăng trưởng việc làm

**Bảng 4.3**. *FSTS, doanh nghiệp xuất khẩu và CAGR việc làm theo phân nhóm con.*

| Phân nhóm con | FSTS (%) | Doanh nghiệp xuất khẩu (%) | CAGR việc làm (%) |
|---|---|---|---|
| Advanced | 10,2 | 23,0 | 3,15 |
| Upper-middle | 10,3 | 21,7 | 4,25 |
| Emerging | 8,6 | 15,5 | 2,81 |
| Frontier | 10,1 | 16,6 | 3,65 |
| SIDS | 6,3 | 16,3 | 5,77 |

Trung vị FSTS bằng 0%, cho thấy phân phối phân cực mạnh; trong khi đó SIDS có CAGR việc làm cao nhất.

### 4.4 Thực trạng đổi mới sáng tạo và năng lực số

#### 4.4.0 Khung 5 lĩnh vực chỉ số WBES — định vị Mục 4.4 trong tổng thể

> **Nguồn chuẩn**: World Bank (n.d.). *Tài liệu tóm tắt: Các chỉ số khảo sát doanh nghiệp Enterprise Surveys* (file 04 v2.5 Section L). Cross-cite glossary v1.2 Nhóm 6 (commit e9a73ae) + Nhóm 7 (commit beb47d3).

WBES tổ chức các chỉ số doanh nghiệp thành **5 lĩnh vực chính thức (5 indicator domains)**, vốn là khung phân tích chuẩn của World Bank được dùng nhất quán xuyên các báo cáo WBES ở châu Á và những châu lục khác. Bảng dưới đây định vị Mục 4.4 hiện tại trong tổng thể 5 lĩnh vực đó:

**Bảng 4.4.0**. *Khung 5 lĩnh vực chỉ số WBES — định vị phạm vi đo lường của Mục 4.4.*

| # | Lĩnh vực | Ví dụ chỉ số WBES | Mục CĐ1 đo trực tiếp | Hàm ý CĐ2 |
|---|---|---|---|---|
| (1) | **Quy định pháp lý + Thuế** | Thuế thời gian (Time Tax) — h/năm tuân thủ thuế; Tuân thủ thuế (Tax compliance); Cấp phép kinh doanh; Thanh tra | (gợi ý CĐ2) | CĐ2 sẽ deep-dive — biến `time_tax_hours` và `tax_inspection_freq` |
| (2) | **Tài chính + Tín dụng** | Hạn chế tín dụng (Credit constraint); Số hóa tài chính (Financial digitalization); Tỷ lệ DN có tài khoản ngân hàng; Tỷ lệ DN có khoản vay | (gợi ý CĐ2, liên kết rào cản #1 ở Mục 4.5.5) | CĐ2 deep-dive — biến `credit_constraint_dummy` |
| (3) | **Cơ sở hạ tầng + Khí hậu** | Quản lý năng lượng (Energy management); Mất điện (Power outages); Theo dõi CO2 (CO2 monitoring); Chất lượng đường giao thông | **Mục 4.4 đo gián tiếp qua quy trình mới**; **rào cản #4 ở Mục 4.5.5 đo trực tiếp** | CĐ2 — biến `power_outage_intensity` từ question c30 |
| (4) | **Thương mại + Cạnh tranh** | Thời gian thông quan (Customs clearance time); Đối thủ phi chính thức; Xuất khẩu trực tiếp/gián tiếp; FSTS | (FSTS đã đo ở Mục 4.3); cạnh tranh phi chính thức ở Mục 4.5.5 #3 | CĐ2 — biến `customs_days` + `informal_competition` |
| (5) | **Tham nhũng + Phi chính thức** | Hối lộ (Bribery): Bribery Incidence + Bribery Depth; Tham ô (Graft Index); Đối thủ không chính thức | (sẽ phân biệt rõ ở Mục 4.7.5 v3.8c — NEW) | CĐ2 deep-dive — biến `bribery_incidence_pct` |

**Phạm vi đo lường của Mục 4.4** *(đổi mới sáng tạo và năng lực số)*: Mục này chỉ tập trung vào **lĩnh vực (5) phần đổi mới và năng lực số** (gồm Sản phẩm mới, Quy trình mới, R&D, ISO, Website) cùng một phần **lĩnh vực (3) hạ tầng** (Website đại diện cho ICT infrastructure access). Các lĩnh vực (1), (2), (4) và phần lớn lĩnh vực (5) về tham nhũng chỉ được **đề cập gián tiếp** qua bảng kết quả chi tiết theo quốc gia (Mục 4.10) hoặc qua các rào cản hàng đầu (Mục 4.5.5), chứ chưa được phân tích sâu. Đây là phần **phạm vi mở rộng dành cho CĐ2** với 5 control variables mới (xem hàm ý CĐ2 ở Mục 4.5.5).

**Lý do giới hạn phạm vi CĐ1**: (a) về tính khả dụng của biến, các biến trong lĩnh vực (1), (2), (4) có nhiều giá trị thiếu trong PICS3 schema cũ 2009-2012, gây mất cân đối panel; (b) nghiên cứu tập trung vào hai construct cốt lõi của luận án là TCI và DAI, vốn được Đỗ & Phan (2026 — VEFR) thiết kế từ lĩnh vực (5) đổi mới và năng lực số; (c) CĐ1 mang tính mô tả và gợi mở, dành phần phân tích đa biến với specification đầy đủ 5 lĩnh vực cho CĐ2.

**Bảng 4.4**. *Đổi mới sáng tạo và áp dụng số (%).*

| Phân nhóm con | Sản phẩm mới | Quy trình mới | R&D | ISO | Website |
|---|---|---|---|---|---|
| Advanced | 22,3 | 52,3 | 16,7 | 29,9 | 59,3 |
| Upper-middle | 26,7 | 71,7 | 21,0 | 31,4 | 56,9 |
| Emerging | 17,5 | 65,2 | 16,4 | 24,9 | 49,2 |
| Frontier | 23,1 | 68,9 | 14,2 | 20,7 | 38,0 |
| SIDS Thái Bình Dương | **41,5** | 65,1 | 11,8 | 16,5 | **58,9** |

SIDS Thái Bình Dương thể hiện pattern **thích nghi và nhảy vọt số (adaptation và digital leapfrog)**; ở đây, Năng lực công nghệ (TCI) được phân tách rõ so với Năng lực số (DAI), kế thừa cách làm của Đỗ & Phan (2026 — VEFR).

#### 4.4.5 Tái định hình "Năng lực số" — Tier-1 Digital Presence rebrand

Spec 1 (full coverage 2009–2025) dùng một biến nhị phân duy nhất (`website` Y/N) để đại diện cho "Năng lực số (DAI)", trong khi TCI lại được đo bằng nhiều thành phần vững chắc hơn (R&D cộng ISO, multi-component aspirational). Hậu quả phân tích là hệ số -0,129 của DAI ở Advanced trong Spec 1 dường như gợi ý rằng "số hóa làm giảm năng suất ở Singapore, Hàn Quốc hay Hong Kong". Tuy nhiên, đây là một **ảo ảnh thống kê** do đo lường sơ sài chứ không phản ánh thực tế kinh tế. NotebookLM (2026, *Bẫy đo lường số hóa Châu Á*) ví von rằng việc này *"giống như cố đánh giá hiệu suất của mạng lưới logistic AI hiện đại nhưng lại dùng bản đồ trạm điện tín thế kỷ 19."*

**Đề xuất rebrand v3.5**: đổi tên biến trong Spec 1 từ "DAI / Năng lực số / Chuyển đổi số" sang **"Sự hiện diện số cơ bản (Tier-1 Digital Presence)"**. Cách gọi này hẹp hơn và khiêm tốn hơn, thừa nhận rằng Spec 1 chỉ đo *"bức số hóa tài liệu"* (website binary), KHÔNG đo sự thay đổi mô hình kinh doanh hay digital transformation.

**ICT exclusion test (chuyển từ I2 của Mục 4.8 lên thân Chương 4)**: Khi loại bỏ các ICT firm (mã ISIC J 58–63) khỏi phân nhóm Advanced innovation-driven, hệ số âm của DAI (-0,129) **biến mất**. Đây là bằng chứng cho **sự bão hòa Tier-1 ở các nước tiên tiến**: Sự hiện diện số cơ bản đã saturated từ trước 2018 ở Singapore, Hong Kong, Hàn Quốc, Đài Loan và Israel (Đỗ & Phan, 2026 — VEFR p. 24). Việc đưa ICT exclusion test lên mạch chính, thay vì đẩy xuống phụ lục hay CĐ2, **không chỉ sửa lỗi thống kê mà còn tạo ra lập luận sắc bén**: *"Sự hiện diện số cơ bản đã bão hòa ở các nước tiên tiến từ lâu, nên biến này không còn discriminate năng suất giữa các firm ở Advanced."*

**Spec 1 so với Spec 2 — biểu đồ đối chiếu hai trục thời gian** *(đề xuất Hình 4.X mới, đang chuẩn bị)*: đặt Spec 1 (biến đơn website binary, 2009–2025) cạnh Spec 2 (DAI tổng hợp 5 thành phần gồm website, email, smartphone POS, e-commerce và cloud, 2018–2025) trên cùng trục thời gian. Cách trình bày này chứng minh hệ sinh thái số chuyển từ **trạng thái tĩnh "Tier-1 Digital Presence"** (chỉ là tài liệu trực tuyến) sang **trạng thái động "Tier-2 Digital Transformation"** (mô hình kinh doanh được tái định hình, kế thừa khung phân tầng của Banalieva & Dhanaraj, 2019).

#### 4.4.5.1 Đối chiếu DAI xuyên quốc gia — Singapore (Tier 1+2) vs Việt Nam (Tier 1 only)

> **Bằng chứng nền tảng**: Mục 2.7 file 14 v3.13 (Khung 4-Tier Verhoef + CDCM); P3 Singapore manuscript (Mar et al., 2026 — *MIR*); P4 Việt Nam (Đỗ & Phan, 2026 — *APJM*).

NotebookLM critique 08/05/2026 chỉ ra một **mâu thuẫn tử huyệt** giữa hai bài viết. Singapore (Tier 1+2 gồm website cộng e-payment) cho hệ số tương tác DAI×FSTS² **dương mạnh** (β=3,119, p=,005), trong khi Việt Nam (Tier 1 chỉ gồm website) lại cho tương tác DAI×FSTS **âm** ở wave 2023 (β=-0,912, p=,043). Đây không phải mâu thuẫn ngẫu nhiên mà chính là **bằng chứng cho khung CDCM**: giá trị của công cụ số phụ thuộc vào độ tương thích giữa cấp độ số hóa và mật độ giao dịch quốc tế.

**Bảng 4.4.5.1**. *Đối chiếu cơ chế DAI giữa hai bối cảnh thể chế (CDCM application).*

| Chiều | Singapore (Advanced innovation, 2023) | Việt Nam (Emerging, 2009-2023) |
|---|---|---|
| **Cấp DAI** | Tier 1+2 (website + cường độ thanh toán điện tử) | Tier 1 (website only) |
| **Mẫu** | n=623, cắt ngang 1 năm | n=2.958 firms × 3 wave |
| **DAI direct effect** | β=0,168, p<,001 (dương ổn định) | Stage-contingent: 2009 mạnh, 2015 null (β=-0,044, p=,377), 2023 phục hồi |
| **DAI × FSTS² interaction** | **β=3,119, p=,005 (dương mạnh)** — conditional scaling resource ở xuất khẩu cao | **β=-0,912, p=,043 (âm) ở 2023** — Tier 1 trở thành điểm nghẽn ở xuất khẩu cao |
| **2SLS robustness (DAI)** | (chưa kiểm định IV) | β co về 0,02, p=,94 — **không xác lập nhân quả** |
| **Cơ chế giải thích** | Tier 1+2 hấp thụ super-linear coordination cost xuất khẩu cao (Brynjolfsson & McAfee, 2014) | Tier 1 không quản lý nổi giao dịch lớn, làm khuếch đại quá tải thông tin |

**Hàm ý cho lập luận ở Mục 4.4.5 hiện hành**: Hệ số âm của DAI ở Advanced trong Spec 1 (-0,129) không chỉ là *artifact của Tier-1 saturation* (đã lập luận ở v3.5) mà còn phản ánh hiện tượng **gãy đổ đo lường** (measurement break) khi Tier 1 không đủ sức quản lý giao dịch ở mức xuất khẩu cao. Khi mở rộng sang Tier 1+2 (Spec 2 có e-payment), hệ số dương mạnh xuất hiện trở lại, lặp lại pattern của Singapore P3.

**Đề xuất phương pháp luận cho CĐ2** *(robustness check #10)*: kiểm định chéo ranh giới khái niệm bằng cách chạy Spec 2 chỉ ở 41 nước có đủ dữ liệu Tier 1+2 (wave BREADY trở đi), nhằm xác nhận rằng pattern kiểu Singapore (DAI × FSTS² dương) xuất hiện khi có chỉ số áp dụng số tổng hợp. Nếu xác nhận được, đây là đóng góp lý thuyết mạnh cho CDCM (Đỗ & Phan, 2026, mở rộng từ APJM sang luận án). Nếu không xác nhận được, nghiên cứu cần đến Tier 3 (ERP/CRM) hoặc Tier 4 (AI) để nắm bắt cơ chế thực sự, qua đó định hướng cho việc thu thập dữ liệu trong tương lai (xem limitations ở Mục 7.3.4 file 16).

### 4.5 Thực trạng cấu trúc doanh nghiệp

**Bảng 4.5**. *Cấu trúc doanh nghiệp theo phân nhóm con (%).*

| Phân nhóm con | SME | Doanh nghiệp xuất khẩu | FDI ≥10% |
|---|---|---|---|
| Advanced | 79,1 | 23,0 | 11,1 |
| Upper-middle | 76,2 | 21,7 | 8,4 |
| Emerging | 74,4 | 15,5 | 4,7 |
| Frontier | 85,0 | 16,5 | 5,9 |
| SIDS Thái Bình Dương | **88,5** | 16,3 | **23,5** |

Tỷ lệ FDI có dạng chữ U, với cực tiểu rơi vào nhóm Emerging. SIDS cao nhất do du lịch (tourism) và viễn thông ở khu vực này được dẫn dắt bởi doanh nghiệp đa quốc gia (MNE-driven).

![Hình 4.6 — Phân phối quy mô doanh nghiệp theo phân nhóm con (n=101.185)](figures/fig_4_6_firm_size.png)

*Hình 4.6. Stacked bar chart cho thấy SIDS Pacific có tỷ lệ SME cao nhất (88,5%), Frontier kế tiếp (85,0%), Advanced thấp nhất (79,1%). Pattern phù hợp với cấu trúc kinh tế khu vực — SIDS thị trường nhỏ phụ thuộc SME; Advanced có nhiều doanh nghiệp lớn. Tái lập: `generate_figures.py` function `fig_4_6_firm_size()`.*

#### 4.5.5 Bốn rào cản hàng đầu của khu vực tư nhân Á-Thái — bằng chứng từ WBES

> **Nguồn chuẩn**: World Bank (n.d.). *Tài liệu tóm tắt: Các chỉ số khảo sát doanh nghiệp Enterprise Surveys* (file 04 v2.5 Section L). Cross-cite glossary v1.2 Nhóm 7 #61 (commit beb47d3).

WBES chính thức xác định **4 rào cản hàng đầu (top 4 barriers)** đối với khu vực tư nhân ở các nền kinh tế đang phát triển và mới nổi của khu vực châu Á - Thái Bình Dương, phù hợp với pool 101.185 doanh nghiệp của chuyên đề này. Bốn rào cản này tạo thành một **khung phân tích cấu trúc** (structural framework), bổ sung cho 5 lĩnh vực chỉ số WBES đã phân tích ở Mục 4.4 (đổi mới và năng lực số) và Mục 4.5 (cấu trúc doanh nghiệp). Bảng dưới phân tầng theo 4 phân nhóm con thể chế:

**Bảng 4.5.5**. *Bốn rào cản hàng đầu Asia-Pacific WBES — phân tầng theo phân nhóm con thể chế (cảm quan định tính + vào sâu chương trình CĐ2).*

| # | Rào cản | Tiếng Anh chuẩn WB | Cường độ Frontier | Cường độ Emerging | Cường độ Upper-middle | Cường độ Advanced | Lý thuyết liên kết |
|---|---|---|---|---|---|---|---|
| (1) | **Tiếp cận tài chính** *(Hạn chế tín dụng)* | Credit constraint / Access to finance | Cao | Cao | Trung bình | Thấp | Aguinis et al. (2011) — formative composite measurement; Coltman et al. (2008) construct validation cho credit access |
| (2) | **Lực lượng lao động thiếu kỹ năng** | Skilled labor shortage / Workforce skill gap | Cao | Trung bình | Trung bình | Thấp | Cohen & Levinthal (1990) — absorptive capacity; Kafouros et al. (2023) — institutional quality moderation tech-dynamism |
| (3) | **Cạnh tranh từ doanh nghiệp phi chính thức** | Informal sector competition | Cao | Cao | Trung bình | Thấp | Khanna & Palepu (2010) — institutional voids; La Porta & Shleifer (2008, 2014) shadow economy share |
| (4) | **Nguồn cung điện không đáng tin cậy** | Unreliable electricity supply / Power outages | Cao (đặc biệt SIDS, Frontier) | Trung bình | Thấp | Thấp | IFC PSD Blueprint operational resources pillar; Banerjee & Duflo (2014) infrastructure productivity links |

**Bốn nhận xét** (cập nhật theo WBES Asia-Pacific 2018–2025):

(a) **Rào cản 1 — Hạn chế tín dụng**: Hơn 30% doanh nghiệp ở Frontier và Emerging xem **hạn chế tiếp cận tín dụng (credit constraint)** là rào cản trên mức trung bình. Pattern này phù hợp với giả thuyết **khoảng trống thể chế (institutional voids)** của Khanna & Palepu (2010): các thị trường đang phát triển có hệ thống tài chính non yếu, khiến doanh nghiệp khó tiếp cận tín dụng chính thức. Điều này liên kết với chỉ số *Số hóa tài chính (Financial digitalization)* ở Mục 4.4; công nghệ tài chính (fintech) tuy có thể giảm chi phí giao dịch nhưng chưa thay thế được kênh ngân hàng truyền thống ở SME.

(b) **Rào cản 2 — Lực lượng lao động thiếu kỹ năng**: Rào cản này đặc biệt nghiêm trọng đối với doanh nghiệp sản xuất công nghệ cao (manufacturing high-tech) và ICT (Bảng 4.8.1), đúng với khung **Schumpeter II về động học công nghệ (Schumpeter Mark II tech dynamism)** (Kafouros et al., 2023). Tại châu Á, pattern này mạnh nhất ở Frontier do hệ đào tạo nghề kém phát triển, và ở Vùng Vịnh do lực lượng lao động phụ thuộc nhiều vào lao động nhập cư.

(c) **Rào cản 3 — Cạnh tranh từ doanh nghiệp phi chính thức**: Loại cạnh tranh này tạo ra **cạnh tranh không công bằng (unfair competition)** đối với doanh nghiệp chính thức, vì doanh nghiệp phi chính thức không phải tuân thủ thuế, lao động hay chuẩn an toàn. Mức độ **kinh tế ngầm (shadow economy)** ở Frontier và Emerging châu Á có thể lên tới 30–40% GDP (La Porta & Shleifer, 2014). Giả thuyết đặt ra là cạnh tranh phi chính thức làm giảm động lực đầu tư R&D và chứng chỉ ISO, một mối liên hệ với chỉ số *Δ R&D Emerging giảm -42,1 đpt* ở Mục 4.4.

(d) **Rào cản 4 — Nguồn cung điện không đáng tin cậy**: Rào cản này đặc biệt nghiêm trọng với SIDS Thái Bình Dương và Frontier (chẳng hạn Bangladesh, Pakistan với power outages hơn 10 giờ mỗi tháng theo WBES), trực tiếp làm giảm năng suất lao động (Banerjee & Duflo, 2014), liên kết với chỉ số *phân tán năng suất Frontier 1,36 cao nhất* ở Mục 4.2. **IFC PSD Blueprint** xếp đây vào *operational resources pillar*, tức yếu tố hạ tầng vật chất khác biệt với *human resources pillar* (kỹ năng) và *financial resources pillar* (tín dụng).

**Hàm ý cho CĐ2**: 4 rào cản này tương ứng với 4 control variables mới trong Spec 1 (full pool) và Spec 2 (2018-2025): (i) `credit_constraint_dummy` từ WBES question k30; (ii) `labor_skill_gap` từ question b8; (iii) `informal_competition` từ question e30; (iv) `power_outage_intensity` từ question c30 (số ngày mất điện mỗi tháng). Cộng với khung industry FE (Mục 4.8) và phân nhóm con thể chế (Chương 3 file 14), CĐ2 sẽ có một **specification đầy đủ 5 lĩnh vực WBES**, chứ không chỉ 2 lĩnh vực (đổi mới và năng lực số) như Mục 4.4 hiện đang phân tích.

#### 4.5.6 Giới tính quản lý cấp cao và sở hữu — bằng chứng từ WBES pool

> **Nguồn chuẩn**: Carboni et al. (2024/2025 — WBES 192.000 doanh nghiệp, 158 quốc gia, 2006–2023); World Bank (2024) *Unlocking Global Growth: Closing the Gender Gap in Business* (WBES 167 nền kinh tế). Biến WBES: `b7a` = female top manager (nhị phân Y/N); `b4` = female majority ownership.

**Bảng 4.5.6**. *Tỷ lệ nữ quản lý cấp cao (female top manager) và nữ sở hữu — theo phân nhóm con ICRV.*

| Phân nhóm con | % Nữ Top Manager (b7a) | % Nữ Majority Owner | Ghi chú |
|---|---|---|---|
| **Advanced — innovation-driven** | ~26–30% | ~18–22% | Singapore: WBES 2023 (b7a) ≈ 28% |
| **Advanced — resource-driven** | ~5–8% | ~3–5% | Vùng Vịnh: thấp do cấu trúc xã hội-thể chế |
| **Upper-middle** | ~30–35% | ~20–25% | Trung Quốc, Malaysia, Thái Lan dẫn dắt |
| **Emerging** | ~25–33% | ~18–24% | EAP trung bình 33,4% (dẫn đầu toàn cầu — xem Mục 6.1) |
| **Frontier** | ~15–25% | ~10–18% | Phân tán lớn — Bangladesh (~16%) vs Kyrgyz (~35%) |
| **SIDS Thái Bình Dương** | ~20–28% | ~15–20% | Fiji/Solomon Islands — matrilineal land tenure culture |

*Lưu ý: Số liệu tỷ lệ phần trăm là ước tính theo phân nhóm con ICRV dựa trên tổng hợp WBES pool, cần đối chiếu lại với dữ liệu `b7a` gốc khi hoàn thiện. Bảng 6.1.1 (file 16, Mục 6.1) cung cấp số liệu chính xác theo vùng WB.*

**Ba phát hiện nổi bật**:

(a) **Nghịch lý EAP — dẫn đầu về representation nhưng không về performance gap**: Dữ liệu WBES cho thấy EAP có 33,4% nữ TMT, cao nhất toàn cầu; tuy nhiên Carboni et al. lại chỉ ra rằng mối quan hệ giữa female top manager và ESG (môi trường, xã hội, quản trị) phụ thuộc mạnh vào chất lượng thể chế và công nghệ. Tại các nền kinh tế như Việt Nam, Trung Quốc, Philippines, phụ nữ quản lý cấp cao hiện diện cao nhưng thường tập trung ở SME nội địa năng suất thấp hơn, nên cần kiểm soát quy mô, ngành và regime ICRV.

(b) **Vùng Vịnh — khoảng cách lớn nhất**: Advanced resource-driven (Vùng Vịnh Saudi/Qatar/Kuwait) có tỷ lệ nữ TMT thấp nhất toàn pool (3–8%), phản ánh cấu trúc thể chế và xã hội đặc thù. Đây là một điều kiện biên cho mọi phân tích gender performance: kết quả về mối quan hệ giữa giới tính và năng suất ở Vùng Vịnh không thể suy rộng sang Advanced innovation-driven.

(c) **Frontier — phân tán nội bộ lớn**: Kyrgyz Republic và Tajikistan (Frontier/Trung Á, nữ TMT khoảng 35%) tương phản rõ với Yemen và Afghanistan (Frontier/MENA, nữ TMT dưới 5%). Sự tương phản này minh họa lý do vì sao ICRV phân nhóm Frontier thành 17 nước thay vì gộp chung.

**Biến WBES và hàm ý CĐ2**: Biến `b7a` (female top manager) trong CĐ2 có thể đóng hai vai trò: (i) **biến kiểm soát** trong specification cơ bản nhằm loại tác động cơ cấu giới lên năng suất; (ii) **biến điều tiết (moderating variable)** cho H4 về TMT moderation theo Mardones-Ibáñez (2025 — *SAGE Open*) và Al-Najjar et al. (2025 — *IJHRM*). Khung của Carboni et al. gợi ý rằng tác động của female top manager lên firm performance không tuyến tính mà phụ thuộc vào ba yếu tố: (a) mức độ số hóa (DAI), nơi công nghệ bổ trợ cho đa dạng giới; (b) regime ICRV, nơi thể chế mạnh khuếch đại tác động của đa dạng giới; và (c) ngành, nơi các ngành tech-dynamic có ROI cao hơn từ lãnh đạo đa dạng giới.

### 4.6 Bức tranh thay đổi theo thời gian

**Bảng 4.6**. *Δ điểm phần trăm (đpt) khi so sánh 2018–2025 với 2009–2012.*

| Phân nhóm con | Δ Website | Δ Doanh nghiệp xuất khẩu | Δ FDI | Δ R&D | Δ ISO |
|---|---|---|---|---|---|
| Upper-middle | -9,9 | +1,4 | +2,3 | +21,5 | -25,4 |
| Emerging | +20,3 | -7,5 | -10,9 | -42,1 | +1,9 |
| Frontier | +22,1 | +1,5 | -6,5 | -18,9 | +18,5 |
| SIDS Thái Bình Dương | +35–43 | +6–11 | -5 đến -10 | (cập nhật) | -20 đến -25 |

Nhảy vọt số (digital leapfrog) thể hiện rõ qua việc website tăng +20–43 đpt ở Frontier, Emerging và SIDS Thái Bình Dương, phù hợp với luận điểm digital leapfrog của Banalieva & Dhanaraj (2019).

![Hình 4.4 — Slope chart 2009–2012 vs 2018–2025 (Δ điểm phần trăm 5 chỉ số)](figures/fig_4_4_growth_pathway.png)

*Hình 4.4. Slope chart minh họa thay đổi 5 chỉ số (Website, DN xuất khẩu, FDI, R&D, ISO) giữa 2 mốc thời gian cho 4 phân nhóm con. Pattern nổi bật: Website tăng mạnh +20-40 đpt ở Frontier/SIDS (digital leapfrog); FDI giảm phổ biến (-5 đến -11 đpt); R&D giảm mạnh ở Emerging (-42,1 đpt) cảnh báo schema effect. Tái lập: `generate_figures.py` function `fig_4_4_growth_pathway()`.*

![Hình 4.7 — Spider chart 5 chiều × 2 mốc thời gian (Advanced, Emerging, SIDS)](figures/fig_4_7_spider_chart.png)

*Hình 4.7. Radar/spider chart cho 3 phân nhóm con (Advanced, Emerging, SIDS) trên 5 chiều (FSTS, Innovation product, R&D, Website, ISO) với 2 mốc thời gian (2009–2012 vs 2018–2025). Quan sát: SIDS có Innovation product cao đột biến + Website tăng mạnh giai đoạn 2018-2025 (digital leapfrog confirmed). Advanced ổn định high level. Emerging: ISO + R&D thay đổi mạnh, FSTS giảm. Tái lập: `generate_figures.py` function `fig_4_7_spider_chart()`.*

### 4.7 Tổng hợp Chương 4 (mở rộng D4 — 10 kết luận chính)

Chương 4 cung cấp bức tranh thực trạng đa chiều dựa trên **101.185 doanh nghiệp ở 47 nền kinh tế châu Á và Thái Bình Dương (108 cặp QG×năm) trong giai đoạn 2009–2025** từ nhóm dữ liệu WBES sau khi hài hòa. Đây là phạm vi rộng nhất từng có cho nghiên cứu quốc tế hóa và hiệu quả (I-P) trong văn liệu IB, mở rộng khoảng 2,5 lần so với 17 nước châu Á mới nổi của Đỗ & Phan (2026 — VEFR).

**Mười kết luận chính**:

**(i) Phân tán năng suất nội bộ tăng đơn điệu khi phân nhóm con suy giảm**: từ Advanced 0,86 lên Upper-middle 1,29, xấp xỉ Emerging 1,24 và SIDS 1,32, rồi cao nhất ở Frontier 1,36. Tỷ số P90/P10 leo từ 10,8 lần lên 39,6 lần. Pattern này khẳng định **giả thuyết phân bổ sai nguồn lực** (Hsieh & Klenow, 2009, 2014).

**(ii) Dị biệt nội bộ phân nhóm Advanced**. Việc phân tán sụt từ 1,00 (chỉ innovation-driven) xuống 0,86 (sau khi thêm Vùng Vịnh resource-driven) gợi ý cần **phân nhóm con (sub-grouping) Advanced** trong CĐ2. Tỷ số phân tán của Singapore (1,03) so với Vùng Vịnh (0,49) vào khoảng **2,1 lần**, đã được tách trực quan trong **Bảng 4.1 (v3.1)**.

**(iii) Dị biệt nội bộ phân nhóm Emerging — 3 phân nhóm con** *(NEW D1, Mục 4.9)*. Nhóm FDI dẫn dắt SEA (VNM+IDN+PHL, FSTS 13,2%) khác hẳn nhóm dân số lớn (IND+LKA+JOR, FSTS 7,2%) và nhóm tài nguyên (MNG, FSTS 5,0%). TCI ở đây ngược dấu, phản ánh sự khác biệt giữa **học hỏi do FDI dẫn dắt và học hỏi tự thân** (Cohen & Levinthal, 1990).

**(iv) SIDS Thái Bình Dương (7 nước, n=1.371)**: phân tán 1,32, đổi mới sản phẩm cao nhất (41,5%), website 58,9% gần Advanced. **Kiribati 2025 là trường hợp biên CỰC ĐOAN nhất với FSTS 1,03%, FDI 0,7%, website 18,7%, ISO 1,3%, gợi ý dị biệt nội bộ trong SIDS giữa nhóm "high digital leapfrog" (Fiji, Maldives) và nhóm "isolated rural" (Kiribati).** Đây là cơ sở cho **H6 (forced internationalization penalty)** (Briguglio, 1995; Bertram, 2006).

**(v) Quốc tế hóa là hiện tượng phân cực**: trung vị FSTS bằng 0% xuyên năm phân nhóm con, chỉ 15–23% doanh nghiệp tham gia xuất khẩu. Điều này đòi hỏi **lựa chọn hai giai đoạn (2-stage selection)** trong CĐ2.

**(vi) Nhảy vọt số (digital leapfrog) 2018–2025** ở Frontier, Emerging và SIDS (+20–43 đpt website) là bằng chứng tái định vị Uppsala (Banalieva & Dhanaraj, 2019). *Riêng Kiribati 2025 không thể hiện leapfrog (website 18,7%), do thiếu điều kiện hạ tầng tối thiểu mà Kiribati chưa đạt được.* Cần phân biệt **Tier-1 Digital Presence** (website binary, đo trong Spec 1, đã bão hòa ở Advanced từ trước 2018) với **Tier-2 Digital Transformation** (DAI multi-component gồm e-commerce, cloud, AI adoption, đo trong Spec 2 với 5 thành phần). Hệ số âm của DAI ở Advanced trong Spec 1 (-0,129) KHÔNG phản ánh việc "số hóa làm giảm năng suất" mà là **artifact của Tier-1 saturation** ở các nước tiên tiến (xem ICT exclusion test ở Mục 4.4.5).

**(vii) Pattern phi tuyến FDI ≥10%** có dạng chữ U với cực tiểu rơi vào Emerging (4,7%): lần lượt là Advanced 11,1%, Upper-middle 8,4%, Emerging 4,7%, Frontier 5,9% và SIDS 23,5%. Có hai mô hình FDI: (a) Advanced với MNE hub và Vùng Vịnh hạn chế; (b) SIDS với du lịch và viễn thông.

**(viii) Đợt khảo sát 2025 — mẫu đơn năm lớn nhất** *(NEW D2)*. Với **14 nước và 16.979 doanh nghiệp**, đợt này cho thấy: (a) IND FSTS sụt 5 đpt do schema kết hợp Atmanirbhar Bharat; (b) Fiji có website 74,8% vượt Singapore 66,1%; **Kiribati ngược lại, chỉ website 18,7% và FSTS 1,03%**; (c) xác nhận Vùng Vịnh cùng Brunei thuộc resource-driven Advanced; (d) cảnh báo R&D schema-induced overestimation.

**(ix) Khung phân tích cấp ngành (industry-level)** *(NEW D3, Mục 4.8)*. Khung này gồm 9 ngành ISIC Rev. 4, với Manufacturing-only subsample, ICT exclusion test, Construction subsample test cho Vùng Vịnh và Tourism/Hotels separation cho SIDS, cùng 5 giả thuyết I1-I5.

**(x) Pipeline tái lập được cho 4 thế hệ schema WBES**. Pipeline gồm 5 bước viết bằng Python; toàn bộ Bảng 4.1–4.10, 5.1, 6.1 và Phụ lục A đều tái tạo được. **Gói tái lập (replication package)** được công khai.

**Hàm ý cho CĐ2 và luận án**:

(a) **Hệ giả thuyết H1–H6**: H1 về phi tuyến; H2 về TCI điều tiết; H3 về DAI có điều kiện; H4 về phân nhóm con thể chế (5+8 phân nhóm con); H5 về cụm tài nguyên; và H6 về chi phí buộc phải quốc tế hóa (**7 SIDS gồm Kiribati cực trị**).

(b) **8 phân nhóm con với hiệu ứng cố định** cho CĐ2.

(c) **Hai đặc tả mô hình kiểm định vững**: Đặc tả 1 cho phạm vi đầy đủ (n=101.185); Đặc tả 2 cho giai đoạn 2018-2025 (n khoảng 50.000, với DAI/TCI 5 thành phần).

(d) **Industry FE cùng 5 kiểm định vững mẫu con** *(NEW D3)*.

**Phạm vi không trình bày** ở chuyên đề này gồm: hồi quy đa biến (để dành CĐ2); định danh panel và IV (CĐ2); các bảng mô tả cấp ngành (Phase 2, 7/2026); năng suất USD PPP (Phase 1, 6/2026); và resource dependence đo trực tiếp (Phase 1).

#### 4.7.5 Phân biệt 3 thuật ngữ tham nhũng trong WBES — Bribery vs Graft

> **Nguồn chuẩn**: World Bank (n.d.). *Tài liệu tóm tắt: Các chỉ số khảo sát doanh nghiệp Enterprise Surveys* (file 04 v2.5 Section L). Cross-cite glossary v1.2 Nhóm 6 #53-54 (commit e9a73ae) + Nhóm 7 #64-66 (commit beb47d3).

WBES đo lường tham nhũng qua **3 chỉ số riêng biệt**, phân biệt rõ giữa **hành vi chủ thể** (subject behavior, tức hối lộ so với tham ô) và **mức độ phổ biến** (incidence so với depth). Sự phân biệt này quan trọng đối với phân tích chính sách, bởi hối lộ và tham ô có nguyên nhân cũng như giải pháp khác nhau, dù đôi khi vẫn bị gộp chung dưới nhãn "tham nhũng" trong văn liệu chính sách Việt Nam.

**Bảng 4.7.5**. *Phân biệt 3 chỉ số tham nhũng WBES — định nghĩa chính thức + cách đo + ngưỡng cảnh báo.*

| # | Chỉ số (Tiếng Anh) | Tiếng Việt CHUẨN WB | Định nghĩa | Cách đo (công thức) | Ngưỡng cảnh báo |
|---|---|---|---|---|---|
| (a) | **Bribery** *(khái niệm gốc)* | **Hối lộ** | Hành vi đưa/nhận tiền/quà cho lợi thế trong giao dịch công (cấp phép, thanh tra, hoàn thuế, kết nối điện thoại/điện) | (đo qua 3 chỉ số dưới đây) | — |
| (b) | **Graft** *(khái niệm gốc)* | **Tham ô** *(rộng hơn hối lộ)* | Biển thủ công quỹ + lạm dụng chức vụ trục lợi cá nhân | (đo qua chỉ số (b-1) dưới đây) | — |
| (a-1) | **Bribery Incidence** | **Tỷ lệ hối lộ** | % DN gặp ít nhất 1 yêu cầu hối lộ trong 6 giao dịch công khảo sát | Tử số: # DN có ≥1 yêu cầu hối lộ; Mẫu: # DN trong khảo sát có giao dịch trong 6 dạng | >20% = báo động đỏ |
| (a-2) | **Bribery Depth** | **Độ sâu hối lộ** | % giao dịch công có hối lộ trên tổng số giao dịch công của DN | Tử số: # giao dịch có hối lộ; Mẫu: tổng # giao dịch công | >15% = báo động đỏ |
| (b-1) | **Graft Index** | **Chỉ số tham ô** | Tỷ lệ hối lộ trong 6 giao dịch (gồm kết nối điện thoại/điện) NHƯNG **loại trừ thanh tra thuế** | Tử số: như Bribery Incidence; Mẫu: 5 giao dịch (loại bỏ tax inspection vì thiên lệch khai thuế) | >10% = báo động đỏ |

**Tại sao loại trừ thanh tra thuế khỏi Graft Index**: Khai báo "phải hối lộ thanh tra thuế" có thể bị thiên lệch (selection bias), vì doanh nghiệp trốn thuế dễ thừa nhận hơn do đã có hành vi vi phạm, trong khi doanh nghiệp tuân thủ thuế ít khi gặp tình huống thanh tra cụ thể. Việc loại bỏ tax inspection giúp Graft Index phản ánh **tham ô hệ thống** (systemic graft) thay vì hành vi cá biệt liên quan đến trốn thuế.

**Hàm ý cho CĐ2 và luận án**:
- **(1) CĐ1 v3.x** sẽ dùng "Hối lộ" (Bribery) và "Tham ô" (Graft) thay vì "tham nhũng" tổng quát khi cite số liệu cụ thể từ WBES. Khi nói chung về vấn đề thể chế hoặc chính sách quốc gia, vẫn có thể dùng "tham nhũng" như một tổng thể.
- **(2) Specification của CĐ2** sẽ có **3 biến phân biệt** là `bribery_incidence_pct` (a-1), `bribery_depth_pct` (a-2) và `graft_index_pct` (b-1) từ WBES question j7a-j7f, qua đó kiểm tra hệ số khác nhau xuyên 8 phân nhóm con thể chế. Giả thuyết H8 (mới) cho rằng tác động của tham nhũng lên hiệu quả doanh nghiệp khác biệt giữa "extensive corruption" (Bribery Incidence cao, Depth thấp, tức tham nhũng phổ biến nhưng mỗi giao dịch ít) và "intensive corruption" (Incidence thấp, Depth cao, tức chỉ một số ít doanh nghiệp nhưng giao dịch nào cũng tham nhũng).
- **(3) Liên kết với rào cản số 3 ở Mục 4.5.5** (cạnh tranh phi chính thức): doanh nghiệp phi chính thức vừa tránh thuế vừa có thể **né tránh hối lộ (bypass bribery)** do hoạt động ngoài hệ thống chính thức. Điều này tạo ra một **tình thế tiến thoái lưỡng nan chính sách (policy dilemma)**: **chính thức hóa (formalization)** tuy có thể tăng **mức độ tuân thủ (compliance)** nhưng đồng thời cũng tăng **mức phơi nhiễm hối lộ (exposure to bribery)**.
- **(4) Liên kết với khung phân tích cấp ngành ở Mục 4.8**: ngành Xây dựng có cường độ hợp đồng cao (high contract intensity) nên thường có Bribery Depth cao do từng giao dịch công lớn; trong khi ngành Khai khoáng và Du lịch có tỷ trọng công ty đa quốc gia cao (high MNE share) nên Bribery Incidence cao nhưng Depth lại thấp do **áp lực tuân thủ MNE (MNE compliance pressure)**.

### 4.8 Khung phân tích cấp ngành (industry-level) — kế hoạch CĐ2

> **Mới ở v2.9 (D3)**: Khung dữ liệu (schema) WBES phân loại theo `a3a` (mã ngành) và `a4a` (mã ISIC 4 chữ số).
>
> **Mở rộng v3.4 (07/05/2026)**: Bảng 4.8.1 thêm cột "Dynamism profile (Kafouros 2023)"; bổ sung đoạn lý giải sau bảng về tương tác giữa ngành và chất lượng thể chế (industry với institutional quality interaction); mở rộng từ 5 lên 6 hàm ý phương pháp luận, với hàm ý (f) về test interaction term.

**Bảng 4.8.1**. *Khung phân loại 9 ngành ISIC Rev. 4 cho nhóm dữ liệu WBES.*

| Ngành | Mã ISIC | Đặc điểm | Pattern dự kiến | **Dynamism profile (Kafouros 2023)** |
|---|---|---|---|---|
| Manufacturing — high-tech | C (20–21, 26–30) *(pharma, computers, electrical, motor vehicles)* | Thâm dụng vốn, định hướng xuất khẩu | FSTS cao; R&D cao; ISO cao | **High technological dynamism** *(Schumpeter Mark II — deepening pattern)* |
| Manufacturing — low-tech | C (10–18, 22–25, 31–33) *(food, beverages, textiles, leather, furniture, basic metals)* | Thâm dụng lao động | FSTS trung bình; R&D thấp | **Low technological dynamism** *(widening pattern; longer technology life cycle)* |
| Wholesale/retail | G (45–47) | Thâm dụng lao động, định hướng trong nước | FSTS thấp; website cao; FDI thấp | **High market dynamism** *(volatile consumer demand, short product cycles)* |
| Tourism/hotels | I (55–56) | Dịch vụ phụ thuộc du lịch | FDI cao ở SIDS | **High market dynamism** *(volatile demand — pandemic, geopolitical, seasonal)* |
| Transport | H (49–53) | Kinh tế mạng lưới | FDI cao; ISO cao | Trung gian (low-medium dynamism) |
| ICT | J (58–63) | Thâm dụng tri thức | R&D cao; website ~100% | **High technological dynamism** *(rapid tech evolution, IPR-sensitive)* |
| Construction | F (41–43) | Theo dự án, định hướng trong nước | FSTS thấp; FDI ở GCC | **Low technological dynamism + low market dynamism** *(stable demand, traditional methods)* |
| Mining | B (05–09) | Tài nguyên dẫn dắt | FDI cao; ISO ở MNE-led | **Low technological dynamism** *(commodity-driven, institutional rents)* |
| Finance | K (64–66) | Có quy chế, xuyên biên giới | FDI cao; website ~100% | **High market dynamism** *(demand shocks, AI disruption Wang/Huang/Hong 2024)* |
| Khác | A, D, L | Đa dạng | Hỗn hợp | Hỗn hợp |

**5 giả thuyết cấp ngành cho CĐ2**: I1 về Manufacturing FSTS dominance; I2 về ICT digital-native; I3 về Tourism dẫn dắt FDI ở SIDS; I4 về Mining dẫn dắt resource cluster; và I5 về Construction chiếm ưu thế ở Vùng Vịnh.

**Lý giải lý thuyết — tương tác giữa ngành và chất lượng thể chế theo Kafouros et al. (2023)**:

Khung 9 ngành trên không chỉ phân loại theo logic kinh tế mà còn theo logic lý thuyết của **Kafouros et al. (2023 — *Global Strategy Journal*, Vol 14, 56–83)**. Kafouros và cộng sự (n=12.888 firms, 16 nền kinh tế CEE, giai đoạn 2004-2011, 72.082 obs) chứng minh rằng chất lượng thể chế (đo bằng Rule of Law từ World Governance Indicators) tương tác hai chiều với động học ngành. Theo H1, ở các ngành có **technological dynamism** cao (Schumpeter Mark II như pharma, computers, electrical, ICT, motor vehicles), chất lượng thể chế **khuếch đại tích cực** hiệu quả doanh nghiệp qua ba cơ chế là partnership identification, IPR enforcement và interfirm market exchange. Ngược lại, theo H2, ở các ngành có **market dynamism** cao (cầu biến động mạnh như tourism, retail, finance), chất lượng thể chế lại **suy yếu** vì doanh nghiệp phải nội bộ hóa (internalize) các chức năng nhằm giảm phụ thuộc vào thị trường bên ngoài. Khung này có ba hàm ý cho CĐ1 và CĐ2. Một là hệ số âm của DAI ở phân nhóm Advanced innovation-driven (-0,129 trong Spec 1, xem Mục 4.4 và Phase 2 NotebookLM HĐ1) có thể bị nhiễu bởi các ICT firm đã saturated. Hai là Bảng 4.6 cho thấy Δ R&D Emerging giảm -42,1 đpt, và nếu phân tách high-tech với low-tech Manufacturing thì có thể thấy pattern khác biệt. Ba là CĐ2 cần thêm giả thuyết H7, theo đó tương tác `tech_dynamism × institutional_quality` mang hệ số dương còn tương tác `market_dynamism × institutional_quality` mang hệ số âm. Đây là kiểm định trực tiếp cho việc lặp lại (replication) kết quả của Kafouros (2023) trong bối cảnh châu Á, một đóng góp lý thuyết quan trọng vì Kafouros mới chỉ kiểm định trong bối cảnh CEE.

**6 hàm ý phương pháp luận** *)*:

(a) Industry FE 9 ngành theo Bảng 4.8.1.
(b) Manufacturing-only subsample — tách cho high-tech vs low-tech theo Kafouros (2023) classification.
(c) Tourism separation cho SIDS Thái Bình Dương (boundary case extension, Mục 1.3).
(d) Construction subsample test Vùng Vịnh resource-driven Advanced.
(e) ICT exclusion test cho DAI — đặc biệt liên quan Phase 2 NotebookLM HĐ1 Tier-1 Digital Presence rebrand.
**(f) Test interaction term `tech_dynamism × institutional_quality` và `market_dynamism × institutional_quality`** là robustness check thứ 7 cho giả thuyết H7 mới của CĐ2, đặt sau các kiểm định Manufacturing-only, ICT-excluded, Tourism-separated SIDS, Construction-tested Gulf, Mining-excluded resource và Anchor model BREADY 2025. Đây là kiểm định trực tiếp cho **việc lặp lại Kafouros et al. (2023) trong bối cảnh châu Á**; bảng tương tác giữa ngành và chất lượng thể chế là cần thiết để xác nhận hoặc bác bỏ H1-H2 của Kafouros với 41 nước châu Á, đối chiếu với 16 nước CEE của Kafouros. Nếu tương tác tech_dynamism với institutional_quality dương và có ý nghĩa ở mức p<.05, đây sẽ là bằng chứng đặc thù cho châu Á về lợi thế thể chế bị giới hạn theo ngành (industry-bounded institutional advantage), một đóng góp lý thuyết của luận án.

### 4.9 Phân nhóm con Emerging — phát hiện dị biệt nội bộ

> **Mới ở v2.7 (D1)**: Phát hiện phương pháp luận thứ hai cho CĐ2.

**Bảng 4.9**. *Phân nhóm con Emerging — số liệu tổng hợp 2009–2025 (n=47.803).*

| Phân nhóm con | Quốc gia | n_firms | FSTS (%) | DN xuất khẩu (%) | FDI ≥10% (%) | Website (%) | R&D (%) | ISO (%) | sd log |
|---|---|---|---|---|---|---|---|---|---|
| Emerging — FDI dẫn dắt SEA | VNM, IDN, PHL | 13.779 | **13,2** | 22,1 | 11,4 | 47,3 | 4,8 | 18,8 | 1,53 |
| Emerging — dân số lớn | IND, LKA, JOR | 32.119 | **7,2** | 13,8 | 1,9 | 49,5 | 19,8 | 27,6 | 1,16 |
| Emerging — tài nguyên | MNG | 1.905 | **5,0** | 9,7 | 4,7 | 50,1 | 20,8 | 15,4 | 1,16 |
| **Tổng Emerging** | 7 nước | **47.803** | 8,6 | 15,5 | 4,7 | 49,2 | 16,4 | 24,9 | 1,24 |

Có thể rút ra năm phát hiện: (1) FSTS phân tầng theo các mức 5,0%, 7,2% và 13,2% vốn bị che giấu khi gộp chung; (2) FDI chênh lệch khoảng 6 lần giữa ASEAN-3 với Nam Á và Tây Á; (3) TCI ngược dấu; (4) Mongolia là một trường hợp biên; và (5) sd log 1,53 so với 1,16 cho thấy cấu trúc hai tầng (two-tier) theo Hsieh & Klenow (2009).

### 4.10 Phân tích sâu đợt khảo sát 2025

> **Mới ở v2.8 (D2)**: Đợt 2025 chiếm 16.979 doanh nghiệp (16,8% pool — v3.1 với Kiribati 2025).

**Bảng 4.10**. *14 quốc gia trong đợt 2025 (n=16.979 — v3.1 với Kiribati 2025).*

| Quốc gia | ISO3 | Phân nhóm con | n_firms | FSTS (%) | FDI (%) | R&D (%) | Website (%) | sd log |
|---|---|---|---|---|---|---|---|---|
| Ấn Độ | IND | Emerging | 10.479 | 2,7 | 1,9 | 2,2 | 41,8 | 0,83 |
| Nepal¹ | NPL | Frontier | 1.740 | n/a | n/a | n/a | n/a | n/a |
| Saudi Arabia | SAU | Advanced | 1.002 | 2,7 | 9,5 | 1,7 | 30,2 | **0,47** |
| Thái Lan | THA | Upper-middle | 813 | 9,3 | 6,3 | 8,7 | 61,9 | 1,38 |
| Sri Lanka | LKA | Emerging | 607 | 16,1 | 1,8 | 4,1 | 48,8 | 1,00 |
| Mongolia | MNG | Emerging | 601 | 5,9 | 3,2 | 20,8 | 64,7 | 1,15 |
| Qatar | QAT | Advanced | 480 | 2,3 | 19,4 | 0,6 | 63,3 | **0,31** |
| Afghanistan | AFG | Frontier | 480 | 6,4 | 1,0 | 25,8 | 45,8 | 1,42 |
| Maldives | MDV | Frontier | 154 | 5,8 | 4,5 | 22,4 | **73,4** | 1,36 |
| Fiji | FJI | SIDS | 151 | 12,5 | 9,9 | 18,8 | **74,8** | 1,09 |
| Solomon Is. | SLB | SIDS | 150 | 4,8 | 20,0 | 11,3 | 53,3 | 1,25 |
| Brunei | BRN | Advanced | 150 | 5,1 | 26,2 | 18,9 | **80,7** | 1,10 |
| Kuwait | KWT | Advanced | 150 | **0,4** | 0,0 | 20,7 | 69,3 | 1,15 |
| **Kiribati²** | **KIR** | **SIDS** | **150** | **1,0** | **0,7** | **14,0** | **18,7** | **1,48** |
| **Tổng 2025** | — | — | **16.979** | **3,8** | **2,9** | **5,4** | **44,2** | **0,90** |

*Ghi chú: ¹Nepal 2025 — schema BREADY chưa thống nhất. ²Kiribati 2025: Lower Middle Income; viện trợ AUS/NZ ~30% GDP.*

**Bảy phát hiện**: (1) IND FSTS sụt 5 đpt do schema effect; (2) THA thể hiện pattern "digital up, exports down"; (3) Fiji có website 74,8% vượt Singapore, một dạng digital leapfrog; (4) xác nhận Vùng Vịnh cùng Brunei thuộc resource-driven Advanced; (5) R&D schema-induced overestimation; (6) wave 2025 là mẫu validation cho CĐ2; **(7) Kiribati ở mức cực trị với FSTS 1,03%, FDI 0,7%, website 18,7%, đối lập hẳn với digital leapfrog của Fiji. Đây là bằng chứng dị biệt SIDS rõ rệt giữa nhóm "high-digital" (FJI, MDV) và nhóm "isolated rural" (KIR); CĐ2 do đó cần tách 2 phân nhóm con SIDS.**

**Bảy hàm ý cho CĐ2**: (a) 2025 là test bed cho validation; **(b) Schema FE PostBREADY2024 được tăng cường bằng anchor model** *(chi tiết ở Mục 4.11 v3.7)*; (c) kiểm định Advanced sub-grouping cho 11 quốc gia; (d) bằng chứng SIDS digital leapfrog cho H6, qua đó phân biệt **Tier-1** (website đã bão hòa) với **Tier-2** (transformation đang phát triển); (e) panel hai wave cho 6 nước; (f) tách phân nhóm con SIDS thành "high-digital" và "isolated", mở rộng từ 8 lên 9 phân nhóm con; (g) tách riêng 2025 thành **"Panel hậu đại dịch độc lập"** *(chi tiết ở Mục 4.11 v3.7)*.

### 4.11 Cô lập đứt gãy schema BREADY 2025 — 3 đề xuất phương pháp luận

Đợt 2025 (n=16.979 firms, **16,8% pool**) sử dụng schema BREADY mới, khác với bản hỏi cũ, nên gây ra một cú sốc phi lý: IND FSTS rơi từ 7,7% xuống 2,7% (xem Mục 4.10), còn R&D ở nhiều nước tăng vọt do **hiệu ứng bảng hỏi (questionnaire effect)** chứ không phải do thực tế. Theo NotebookLM (2026, *Bẫy đo lường số hóa Châu Á*): *"Đứt gãy schema BREADY 2025 đe dọa trực tiếp đến tính liên tục của phân tích chuỗi thời gian. Mô hình kiểm tra điểm uốn sẽ cho ra kết luận sai lệch hoàn toàn nếu không xử lý."* NCS đã cảnh báo điều này ở Mục 4.10 (phát hiện 5 về R&D schema-induced overestimation), nhưng vẫn cần làm sâu hơn qua 3 đề xuất phương pháp luận.

#### 4.11.1 Đề xuất 3a — Biến giả `Post_BREADY_2024` trong mọi spec tổng gộp

Khai báo biến giả `Post_BREADY_2024` = 1 cho mọi observation thuộc đợt khảo sát 2025+ (BREADY schema), = 0 cho 2009–2024 (PICS3 + Standardized + early BREADY 2018-2024). Biến giả này:

- **Hấp thụ schema effect tĩnh**: tách phần trung bình của các thay đổi đo lường giữa 2 thế hệ bảng hỏi (chẳng hạn IND FSTS từ 7,7% xuống 2,7% có thể một phần do BREADY hỏi rõ hơn về "doanh thu xuất khẩu trực tiếp" so với PICS3 vốn hỏi tổng quát hơn).
- **Cảnh báo từ NotebookLM**: *"Biến giả đâu phải cây đũa thần. Nó chỉ như miếng bọt biển hút tác động tĩnh, không sửa được phương sai."* Vì vậy, biến giả cần đi cùng đề xuất 3b (anchor model) để kiểm tra robustness.
- **Triển khai**: thêm `Post_BREADY_2024` vào Spec 1 (full pool, 101.185 firms) và Spec 2 (2018-2025, khoảng 50.000 firms) cho CĐ2.

#### 4.11.2 Đề xuất 3b — Mô hình neo (anchor model)

Quy trình 3 bước:

(i) Chạy hồi quy với dữ liệu chỉ đến 2024 (n khoảng 84.000 firms, 13 đợt khảo sát 2009-2024) để có **bộ hệ số "neo"** (anchor coefficients) cho FSTS, FSTS², TCI, DAI và các tương tác.

(ii) **Khóa hệ số** từ bước (i). Trong R: `glmer(... offset = X1 * beta1_anchor + X2 * beta2_anchor, data=full_pool_with_2025)`.

(iii) Chạy lại hồi quy với dữ liệu đầy đủ 2009-2025 (n=101.185), rồi so sánh:
   - Coefficient stability test (Wald test, Chow test): hệ số FSTS, FSTS², TCI, DAI có thay đổi đáng kể khi thêm 2025 hay không?
   - Likelihood ratio test giữa 2 mô hình: Δ AIC, Δ BIC.
   - Coefficient ratio test: nếu `beta_2025 / beta_anchor > 1.5x` hoặc `< 0.67x`, schema effect được xem là đáng kể.

**Mục đích** là kiểm tra liệu cấu trúc bảng hỏi mới có làm đảo chiều ý nghĩa thống kê cốt lõi hay không. Đây là **robustness check thứ 6 cho CĐ2**, đặt sau các kiểm định Manufacturing-only, ICT-excluded, Tourism-separated SIDS, Construction-tested Gulf và Mining-excluded resource.

#### 4.11.3 Đề xuất 3c — Tách 2025 thành "Panel hậu đại dịch độc lập"

Thay vì cố ép 2025 vào đường xu hướng lịch sử, nghiên cứu dành riêng một sub-section trong CĐ2 (đề xuất Mục X.Y trong phần mô hình của Mục 6) để xử lý 2025 như **tập mẫu xác thực cho kỷ nguyên hậu COVID và AI**. Câu hỏi nghiên cứu mới đặt ra là: *"Quy luật thể chế và U-curve giai đoạn 2009-2024 có còn hiệu lực trong 'trạng thái bình thường mới' (new normal) hậu COVID và bùng nổ AI hay không?"*

Tiến trình gồm 3 bước:
- **Bước 1**: Chạy mô hình chính trên dữ liệu 2009-2024, báo cáo H1-H6, H7 và các kiểm định Lin-Mehlum.
- **Bước 2**: Kiểm định cùng mô hình đó trên dữ liệu chỉ năm 2025 (n=16.979), xem như **out-of-sample validation panel**, ghi rõ là "post-pandemic + AI era panel" (hậu COVID 2020-2022 cộng AI surge 2023-2025).
- **Bước 3**: Báo cáo các nội dung sau:
  - Hệ số nào giữ được stability (validation passed);
  - Hệ số nào thay đổi (validation failed, được thảo luận như bằng chứng của paradigm shift hậu COVID và AI);
  - Khác biệt về effect size và các hàm ý chính sách.

**Như NotebookLM nhận xét**: *"Biến rủi ro dữ liệu thành chương phân tích hướng tới tương lai cực kỳ giá trị."*

#### 4.11.4 Liên kết với Mục 6 (yếu tố giải thích) và Mục 7.3 (hàm ý CĐ2)

3 đề xuất 3a, 3b và 3c khi kết hợp tạo thành một **hệ thống cô lập triple-defense** chống lại đứt gãy schema 2025:

| Đề xuất | Tác dụng | Robustness check # | Liên kết |
|---|---|---|---|
| 3a Biến giả Post_BREADY_2024 | Hấp thụ schema effect tĩnh | (parametric correction) | Spec 1 + Spec 2 |
| 3b Anchor model | Test stability hệ số | #6 (sau Mfg/ICT/Tourism/Gulf/Mining) | CĐ2 robustness section |
| 3c Panel hậu đại dịch độc lập | Out-of-sample validation hậu COVID+AI | #7 panel test | CĐ2, Mục X.Y dedicated section |

Cả ba đều là tiền đề cho phần hàm ý CĐ2 ở Mục 7.3.4 file 16, tức robustness check section.

---


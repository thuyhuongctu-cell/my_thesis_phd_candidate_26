# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 5–7 + TÀI LIỆU THAM KHẢO + PHỤ LỤC)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md` và `thesis/15_cd1_part2_findings_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Tổng hợp Asia context: `thesis/_asia_context_synthesis_2026.md`.
> Hình minh họa: `thesis/figures/` (11 hình; chạy `python3 generate_figures.py`).
---

## CHƯƠNG 5 — BẢY TIỂU CẢNH ĐIỂN HÌNH

### 5.1 Singapore (Advanced đổi mới sáng tạo dẫn dắt — innovation-driven, n=623, đợt 2023)

FSTS 7,1%; doanh nghiệp xuất khẩu 17,8%; website 66,1%; ISO 23,3%; R&D 7,5%; FDI 31,5%. Độ lệch chuẩn log năng suất (sd log) 1,03. **Biên trên (upper boundary)** của nhóm Advanced đổi mới sáng tạo dẫn dắt. Theo bài báo P4 (Singapore — MIR): mô hình M8 cho R² hiệu chỉnh = 0,196; tương tác FSTS² × DAI = 3,119; điểm uốn (turning point) ở mức ~85%.

### 5.2 Saudi Arabia, Qatar và Kuwait (Advanced tài nguyên dẫn dắt — resource-driven, n=1.632, 3 đợt năm 2025)

**Bảng 5.2**. *So sánh chỉ số chính: Advanced tài nguyên dẫn dắt (Saudi Arabia, Qatar, Kuwait) so với Advanced đổi mới sáng tạo dẫn dắt (Singapore).*

| Chỉ số | Saudi Arabia | Qatar | Kuwait | Singapore |
|---|---|---|---|---|
| FSTS (%) | 2,7 | 2,3 | **0,4** | 7,1 |
| FDI ≥10% (%) | 9,5 | 19,4 | 0,0 | **31,5** |
| R&D dương (%) | 1,7 | 0,6 | **20,7** | 7,5 |
| sd log năng suất | **0,47** | **0,31** | 1,15 | 1,03 |

Năm phát hiện: (1) **nhà nước tô (rentier state)** — Beblawi (1987); (2) **phân bổ sai nguồn lực đảo chiều** so với Hsieh & Klenow (2009); (3) Kuwait Vision 2035 với R&D 20,7%; (4) **thiên lệch của DAI đơn thành phần**; (5) **phân nhóm con Advanced** — innovation-driven vs resource-driven là Varieties of Capitalism (Hall & Soskice, 2001). **Bối cảnh xung đột Trung Đông 2026**: IMF (2026, April) điều chỉnh giảm tăng trưởng Saudi Arabia từ ~4,5% xuống 3,1%.

### 5.3 Việt Nam (n=3.077, 3 đợt khảo sát) — cập nhật v3.4 với ADB Vietnam Outlook 2026

FSTS 23,2% → 17,9% → 16,1% (suy giảm); doanh nghiệp xuất khẩu 37,1% → 23,8%; ISO 17–23%; R&D 6,1% (đợt 2023). Pattern **kinh tế hai tầng (two-tier economy)**.

> ¹ *Ghi chú cỡ mẫu*: n=3.077 là tổng doanh nghiệp Việt Nam trong pool WBES (2009+2015+2023) trước khi lọc biến hồi quy. n=2.958 là mẫu phân tích hồi quy hoàn chỉnh (complete case) sau khi loại các quan sát thiếu giá trị trên biến focal set — xem §4.4.5.1 Bảng 4.4.5.1.

**Cập nhật bối cảnh 2026 — ADB Vietnam Economic Outlook 2026**: GDP lịch sử 2025 đạt 8,0%; dự phóng **7,2% (2026) → 7,0% (2027)**. Bốn động lực: (a) FDI commitment $2,4 tỷ; (b) Năng suất lao động tăng 5,1%; (c) Hai-tầng kinh tế + ADB Policy-Based Loans $2,4B; (d) GVC re-positioning → mid-stream design/R&D.

**Cập nhật macro deep**: (i) Lạm phát 4,0% (2026) → 3,8% (2027); (ii) Cơ cấu ngành: công nghiệp+xây dựng 7,7%, dịch vụ 7,5%, nông nghiệp 3,6%; (iii) 4 trụ cột tăng trưởng: đầu tư công 800K tỷ VND, tiền tệ nới lỏng, FDI $2,4B, xuất khẩu RCEP+CPTPP; (iv) 5 rủi ro: gián đoạn chuỗi cung ứng, thuế quan Mỹ 2026, thanh khoản nội địa, nợ xấu ngân hàng, trái phiếu doanh nghiệp yếu.

**Hàm ý cho CĐ2**: biến `Vietnam_HighValue_FDI_2026` + `Vietnam_Sector_Mix_2026` cho robustness check #6.

### 5.4 Trung Quốc (n=4.889)

FSTS 10,9% → 8,8%; FDI ≥10% chiếm 6,0%. Quan hệ FSTS–năng suất là đường cong bậc hai (inverted-U) với điểm uốn 49,4% (2012) / 47,2% (2024). Wang, Huang và Hong (2024 — *IRFA*): 80% bank risk models PRC phụ thuộc dominant tech providers — **concentration risk**.

**Khung Zombie firms PRC**: Ba cơ chế — (i) chậm đào thải, (ii) cản trở entry, (iii) concentration risk + zombie hybrid. **Hàm ý cho CĐ2**: biến `Zombie_Firm_Indicator_PRC` — robustness check #7.

### 5.5 Tổng hợp Emerging Asia (n=42.278) — bổ sung India case (v3.2)

FSTS 7,6%; FDI ≥10% chiếm 4,4%; R&D dương 16%. **Ấn Độ — technology spillovers** (Sikdar & Mukhopadhyay, 2026 — *Asian Development Review, 43*(1)): panel 4.293 firms 2006-2019; FDI là kênh lan tỏa ngang quan trọng nhất; FDI inflows $1,705M (1990-2000) → $42,396M (2012-2022).

### 5.6 Mongolia — từ lời nguyền tài nguyên đến chuyển đổi critical minerals (n=1.905, 4 đợt 2009–2025)

FSTS đình trệ 4-6%; FDI ≥10% giảm 7,2% → 3,2%; website tăng 39% → 65%. **Bước ngoặt 2026 — critical minerals (ADB, 2026, May)**: 11 critical minerals; Cu exports 1,69 Mt (2024) = 22,1% tổng xuất khẩu; Oyu Tolgoi target 500.000 tấn/năm 2028-2036. CĐ2: biến `Critical_Minerals_Exposure`.

![Hình 5.6.1 — Mongolia: Evolution 2009–2025 (4 đợt khảo sát WBES)](figures/fig_5_6_mongolia_evolution.png)

### 5.7 SIDS Thái Bình Dương (7 nước — cập nhật v3.1, n=1.371)

**Bảy nước**: Fiji (FJI), Papua New Guinea (PNG), Solomon Islands (SLB), Tonga (TON), Vanuatu (VUT), Samoa (WSM), **Kiribati (KIR)**. FSTS 6,3%; FDI ≥10% **23,5%**; đổi mới sản phẩm **41,5%**; website **58,9%**.

**Kiribati 2025 — trường hợp biên CỰC ĐOAN nhất**: FSTS 1,03%, FDI 0,7%, website 18,7%, ISO 1,3%, sd log 1,48, SME 93,3%.

#### 5.7.5 Bối cảnh kinh tế vĩ mô PICs Pacific

PICs có 4 trụ cột MIRAB (Bertram, 2006): (1) khu vực công chủ đạo 30-50%; (2) phụ thuộc ODA 30% GDP + remittances 25-40% GDP + khai thác tài nguyên; (3) thanh niên thất nghiệp 15-30%; (4) migration labor PLMS Australia + RSE New Zealand. CĐ2: 3 control variables PICs-specific (`aid_share_GDP_pct`, `remittance_share_GDP_pct`, `seasonal_worker_outflow_pct`).

### 5.8 So sánh tổng hợp

**Bảng 5.1**. *Ma trận so sánh đa chiều bảy tiểu cảnh điển hình.*

| Chỉ số | Singapore | Việt Nam | Trung Quốc | Em Asia | Mongolia | SIDS Thái Bình Dương¹ | Saudi+Qatar+Kuwait |
|---|---|---|---|---|---|---|---|
| n_firms | 623 | 3.077 | 4.889 | 42.278 | 1.905 | **1.371 (v3.1)** | 1.632 |
| FSTS (%) | 7,1 | 19,1 | 9,9 | 7,6 | **5,0** | 6,3 | **2,4** |
| FDI ≥10% (%) | **31,5** | 11,4 | 6,0 | 4,4 | **4,7** | 23,5 | **11,5** |
| R&D dương (%) | 7,5 | **3,1** | **39,4** | 16 | **20,8** | 11,8 | **3,1** |
| Website (%) | 66,1 | **47,0** | **58,7** | **48,0** | **50,1** | 58,9 | **43,6** |
| sd log năng suất | 1,03 | 1,38 | 1,20 | 2,18 | **1,16** | 1,32 | **0,49** |

---

## CHƯƠNG 6 — CÁC YẾU TỐ GIẢI THÍCH SƠ BỘ

**Bảng 6.1**. *Hệ số tương quan Pearson (n=101.185 — v3.1).*

| Yếu tố | Advanced | Upper-middle | Emerging | Frontier | SIDS |
|---|---|---|---|---|---|
| FDI ≥10% | −0,113 | −0,023 | +0,113 | +0,068 | **+0,222** |
| FSTS | **+0,113** | −0,086 | +0,062 | +0,014 | −0,050 |
| TCI (R&D + ISO) | **+0,128** | +0,016 | −0,029 | +0,019 | **+0,155** |
| DAI (website) | **−0,129** | +0,012 | +0,016 | +0,070 | −0,049 |

**Sáu phát hiện chính**: (1) FDI dương mạnh SIDS (+0,222); (2) FDI âm Advanced; (3) FSTS dương Advanced; (4) TCI dương SIDS+Advanced; (5) DAI âm Advanced — Tier-1 saturation; (6) Đảo dấu cross-regime — institutional moderation.

**Lý giải bổ sung — Institutional Transaction Costs (TCE)**:

**Bảng 6.1.2**. *Đối chiếu I-P curve + cơ chế DAI/TCI giữa Việt Nam vs Singapore — bằng chứng cho khung CDCM.*

| Chiều | **Việt Nam (Emerging, n=2.958, 3 wave)** | **Singapore (Advanced innovation, n=623, 1 wave)** |
|---|---|---|
| **Hình dáng I-P curve** | **Inverted-U rõ nét** — TP ≈ 39-46% FSTS; Lind-Mehlum p<0,013 | **Tuyến tính dương + bậc hai nhẹ** — TP ≈ 82% FSTS; Lind-Mehlum p=0,303 KHÔNG xác nhận |
| **Cơ chế DAI** | **Stage-contingent** (Tier 1): mạnh 2009 → null 2015 → âm 2023 (β=-0,912) | **Conditional scaling** (Tier 1+2): DAI×FSTS² β=3,119 p=,005 dương mạnh |
| **2SLS DAI robustness** | β co về 0,02, p=,94 — **không xác lập nhân quả** | (chưa kiểm định IV) |
| **Vai trò TCI** | **Scarce advantage** — TCIz IV β=1,639 p<,001 robust | **Hygiene factor** — direct β=0,168 p<,001 KHÔNG điều tiết I-P curve |

**Hàm ý cho khung CDCM**: 41 nước châu Á có continuum institutional transaction costs từ Singapore (cực thấp) → Việt Nam/Indonesia (trung bình) → Mongolia/Pakistan/Bangladesh (cao). TP của I-P curve correlate ngược với mức trưởng thành hạ tầng số quốc gia.

**Hiệu ứng đẩy nhanh giao hàng + bất định chính sách thuế quan**: front-loading effect tạo FSTS-năng suất dương ngắn hạn 2025 → đảo chiều âm 2026-2027 do cạn kiệt đơn hàng. Hàm ý CĐ2: biến `Tariff_Front_Loading_2025_2026` — robustness check #8.

### 6.1 Pattern giới tính trong quản lý + sở hữu — bằng chứng EAP châu Á dẫn đầu

**Bảng 6.1.1**. *Pattern giới tính trong TMT + ownership — phân tầng theo khu vực địa lý.*

| Khu vực | % nữ TMT (cấp cao) | % nữ ownership majority | Khoảng cách (TMT – Owner) |
|---|---|---|---|
| **East Asia & Pacific (EAP)** | **33,4%** *(dẫn đầu globally)* | **25,7%** | +7,7 đpt |
| Latin America & Caribbean | 27,8% | 18,3% | +9,5 đpt |
| Sub-Saharan Africa | 21,3% | 14,9% | +6,4 đpt |
| Europe & Central Asia | 19,8% | 12,1% | +7,7 đpt |
| South Asia | 9,2% | 8,5% | +0,7 đpt |
| **Middle East & North Africa (MENA)** | **3,3%** *(thấp nhất globally)* | **1,7%** | +1,6 đpt |

Sáu quan sát: (a) EAP dẫn đầu — Asian gender paradox; (b) MENA thấp nhất — structural barriers; (c) Ownership ceiling phổ biến; (d) TMT moderation references; (e) Technology complement hypothesis (Carboni et al.); (f) Firm performance heterogeneity.

### 6.2 Đường cong U của innovation digital tech

**Giai đoạn 1** (chi phí đầu tư cao): 1-3 năm đầu giảm hiệu quả tài chính ngắn hạn — DAI âm -0,129 Advanced. **Giai đoạn 2** (productivity payoff): vượt threshold ~3% revenue/năm × 3-5 năm → tăng năng suất. Bằng chứng: PRC R&D 39,4% late-stage Tier-2; Vùng Vịnh transition; Việt Nam 6,1% early Tier-2.

---

## CHƯƠNG 7 — KHOẢNG TRỐNG THỰC TIỄN VÀ KẾT LUẬN

### 7.1 Khoảng trống nghiên cứu thực tiễn (mở rộng v3.2 từ 4 lên **5 khoảng trống**)

**(1) Hài hòa khung dữ liệu xuyên thế hệ WBES 2009–2025**. Pipeline tái lập được cho 4 thế hệ (PICS3, Standardized, BEE, BREADY) — thực hành mở (Page et al., 2021).

**(2) Phân nhóm con Advanced + boundary case Mongolia**. (a) Advanced sub-grouping innovation/resource — VoC + REE (Hall & Soskice, 2001; Hertog, 2010); (b) Mongolia chuyển đổi sang critical minerals economy 2026 (ADB, 2026, May).

**(3) Mô hình phi tuyến và điều tiết đa tầng** (Bausch & Krist, 2007; Marano et al., 2016). Đỗ & Phan (2026 — VEFR, JFAR) chỉ ra điểm uốn khác nhau; CĐ1 mở rộng lên 47 nước.

**(4) Trường hợp biên SIDS Thái Bình Dương** — 7 nước với Kiribati 2025. Đỗ & Phan (2026 — bản thảo P8) áp dụng forced internationalization penalty (Briguglio, 1995; Bertram, 2006).

**(5) Khung GVC participation và inclusive development cho 47 nước (NEW v3.2)** — Theo *Asian Development Policy Report 2026 — Global Value Chains and Inclusive Development* (ADB, 2026, May): Asia/Pacific chiếm ~1/3 GVC trade global; **GVC share Developing Asia tăng 9% → 18% giai đoạn 2000-2023** (gấp đôi). Bằng chứng định lượng macro: 10% increase trong GVC participation → +0,45% per capita income growth; 10% improvement in GVC centrality → +0,8% per capita income growth. Successfully upgraded economies grew 6%/năm (2000-2023) vs 3,9% peripheral. **Tuy nhiên**: small firms 25% less likely to participate in GVCs; within-economy Gini ↑6,7pp — nguy cơ dị biệt nội bộ.

Khoảng trống cho CĐ1: chưa có nghiên cứu firm-level WBES kết hợp với GVC participation cho 47 nước châu Á + Thái Bình Dương. Bằng chứng CĐ1 về **kinh tế hai tầng Việt Nam** (§5.3) và **dị biệt Em Asia** (§5.5) phù hợp với pattern ADPR 2026 — small firms khó tham gia GVC. CĐ2 nên có biến `GVC_participation_rate` (theo OECD TiVA hoặc ADB MRIO) ở cấp ngành × quốc gia × năm.

### 7.2 Kết luận chính

**(i)** Pool 101.185 doanh nghiệp · 47 nước · 108 cặp QG×năm — phạm vi rộng nhất.

**(ii)** Phân tán: Advanced (0,86) < Emerging (1,24) ≈ SIDS (1,32) < Frontier (1,36).

**(iii)** Bảy tiểu cảnh + 7 SIDS đa diện cùng tồn tại — không có hội tụ.

**(iv)** Dị biệt nội bộ Advanced (Singapore/Vùng Vịnh ≈ 2,1×).

**(v)** SIDS pattern thích nghi/leapfrog ở 6 nước cũ; Kiribati 2025 CỰC ĐOAN nhất.

**(vi)** FDI ≥10% dương mạnh SIDS (+0,222) — kênh năng suất chính.

**(vii)** Mongolia chuyển đổi sang critical minerals economy 2026.

**(viii)** Bằng chứng đảo dấu — phi tuyến + điều tiết đa tầng. Cơ sở H1-H6; **CĐ2 mở rộng 8 phân nhóm con**.

### 7.3 Hàm ý cho luận án và Chuyên đề 2

#### 7.3.1 Hàm ý lý thuyết

**(1) VoC + REE type thứ 3** (Hall & Soskice, 2001; Hertog, 2010; Hvidt, 2013).

**(2) Lời nguyền tài nguyên × điều tiết thể chế** — Auty (1993); Sachs & Warner (2001); North (1990); Khanna & Palepu (2010).

**(3) DAI là điều kiện cần nhưng không đủ — cảnh báo *digital theatre***. Sở hữu công cụ số đơn lẻ không tự động đem lại lợi nhuận biên ở Advanced (DAI = -0,129); cần kết hợp absorptive capacity (Cohen & Levinthal, 1990) và năng lực công nghệ tích lũy (Lall, 1992).

**Bằng chứng học thuật 2022-2026 ở Asia (mở rộng v3.2 từ 4 → 5 evidence)**:

(a) **Babina et al. (2024 — JFE)**: AI adoption → growth + innovation intensity (positive evidence khi điều kiện đủ).

(b) **Wang, Huang & Hong (2024 — IRFA)**: 80% bank risk models PRC concentrated — concentration risk gây model homogenization.

(c) **Anil & Misra (2022 — IJEM)**: India UPI fraud −50% nhưng rural rejection +24% — "digital theatre" paradox.

(d) **Zhang, Qiu, Park & Tian (2026 — ABM Special Section)**: 249 studies; 5 risk dimensions Asia; AI là "co-evolutionary governance substrate".

**(e) NEW v3.2 — AI Preparedness Index Asia** (ADB, 2026, April — *Asian Development Outlook April 2026* Special Topic Ch.1.4 "AI Readiness and Economic Impacts in Asia and the Pacific", pp.44-51, dựa trên Cazzaniga et al., 2024 — IMF SDN/2024/001 "Gen-AI: Artificial Intelligence and the Future of Work"):

- **AI Preparedness Index (AIPI)** đo 5 chiều: digital infrastructure, human capital, innovation capacity, regulatory & ethics, economic structure.
- **Khoảng cách lớn AAP vs DAP**: AAP digital infrastructure 0,19 vs DAP <0,11 — "binding constraints on computing capacity, digital connectivity, data infrastructure".
- DAP với điểm AIPI thấp nhất: Cambodia, India, Myanmar, Papua New Guinea, Philippines.
- **AI-related job postings**: Singapore + Hàn Quốc >6%, India 4-5%, Australia 4%, Malaysia/Philippines <2%.
- **AI-enabling goods exports** (theo WTO 2025): Hong Kong, Singapore, Đài Loan-Trung Quốc đều >25% tổng xuất khẩu; DAP trung bình ~10%.
- **Sectoral AI exposure** (Gambacorta et al., 2025 — BIS): Financial services 6,6 cao nhất; Education 6,4; ICT 6,3; Agriculture 5,4 thấp nhất.
- **GDP gains scenarios 2030** (G-Cubed model): AAP 0,6-2,1pp; DAP 0,2-1,8pp; trong DAP, PRC 0,2-6,9% (cao nhất); India lower.
- **AI-driven productivity gains by sector**: Agriculture 0,1-4,5%; Industry 0,3-9,1%; Services 0,3-9,0%.
- **Hệ quả phân phối**: Better-prepared economies → AI accelerate services-led structural change. Less-prepared economies (DAP excluding PRC and IND) → DỊCH CHUYỂN VIỆC LÀM tiêu cực, employment giảm 1-5pp by 2030.

**Hàm ý cho CĐ1 và CĐ2**: AIPI gap củng cố mạnh "digital theatre" warning §7.3.1 (3) — chứng minh DAI cần đi kèm với 4 chiều khác (human capital, innovation capacity, regulatory ethics, economic structure). CĐ2 nên cân nhắc bổ sung biến `AIPI_country_score` cho 47 nước (sau khi Cazzaniga et al. publish full dataset 2024) tương tác với DAI multi-component để giải thích positive vs negative AI effects.

Cảnh báo *digital theatre* (Verhoef et al., 2021) cần được củng cố trong CĐ2 với DAI đa thành phần và mô hình tương tác DAI × TCI × AIPI.

#### 7.3.2 Hàm ý phương pháp luận (mở rộng v3.3 — bổ sung anchor model + panel hậu đại dịch)

**(1) Pipeline tái lập được**.

**(2) DAI/TCI đa thành phần với formative model + 2 đặc tả** (Bharadwaj et al., 2013; Coltman et al., 2008; Aguinis et al., 2011).

**(3) Phân loại 8 phân nhóm con cho CĐ2** + biến `Critical_Minerals_Exposure` (v3.1c) + biến `GVC_participation_rate` (NEW v3.2) + biến `AIPI_country_score` (NEW v3.2 conditional on data availability).

**(4) NEW v3.3 — Mô hình neo (anchor model) — robustness check #6 cho schema BREADY 2025** (kế thừa từ §4.11.2 file 15): Quy trình 3 bước — (i) chạy hồi quy với data ≤2024 lấy "anchor coefficients"; (ii) khóa hệ số; (iii) re-run với data đầy đủ 2009-2025 và so sánh stability (Wald test, Chow test, coefficient ratio). Nếu `beta_2025 / beta_anchor > 1.5x` hoặc `< 0.67x` → schema effect significant. Đây là kiểm chứng định lượng cho "cấu trúc bảng hỏi mới có làm đảo chiều ý nghĩa thống kê cốt lõi hay không" (tác giả, ghi chú nội bộ, 2026).

**(5) NEW v3.3 — Tách 2025 thành "Panel hậu đại dịch độc lập" — robustness check #7** (kế thừa từ §4.11.3 file 15): Thay vì cố ép 2025 vào đường xu hướng lịch sử, dành riêng sub-section CĐ2 để xử lý 2025 như **out-of-sample validation panel cho kỷ nguyên hậu COVID + AI**. Câu hỏi nghiên cứu: *"Quy luật thể chế và U-curve giai đoạn 2009-2024 có còn hiệu lực trong 'trạng thái bình thường mới' (new normal) hậu COVID + AI bùng nổ?"* Tiến trình 3 bước (chạy mô hình chính trên 2009-2024 → test trên 2025 only → báo cáo coefficient stability vs paradigm shift).

**Triple-defense system tổng hợp**: 3 đề xuất 3a (biến giả `Post_BREADY_2024`) + 3b (anchor model #6) + 3c (panel hậu đại dịch #7) tạo thành **hệ thống 3 lớp** chống đứt gãy schema 2025 — bảo vệ tính liên tục của phân tích chuỗi thời gian và tránh "kết luận sai lệch hoàn toàn" (tác giả, ghi chú nội bộ, 2026).

#### 7.3.3 Hàm ý chính sách cho doanh nghiệp Việt Nam và khu vực (9 hàm ý)

**(7) Migration labor partnership Pacific cho Việt Nam — bài học từ PLMS Australia + RSE New Zealand**

Bốn đề xuất: (a) Học mô hình PLMS — Vietnamese Skilled Worker Mobility Scheme; (b) Học mô hình RSE — Aquaculture + Coffee + Cashew Skills Exchange; (c) Cơ chế remittance corridor digital — giảm phí từ ~7% xuống <3%; (d) Skills upgrading tránh brain drain theo Korea EPS model.

**(8) Chính sách số hóa Asia cho SME Việt Nam — bài học từ Singapore/Korea/Japan/Trung Quốc**

Bốn lộ trình: (a) Singapore+Korea — AI full-stack Tier-3 (không phù hợp SME VN hiện tại); (b) Japan — 60% DN dùng AI back-office → **realistic target 2026-2030**; (c) Trung Quốc — smart manufacturing + cảnh báo concentration risk; (d) **Mô hình ưu tiên SME Việt Nam: VietQR + social commerce + cross-border e-commerce + Cloud+AI tools (Tier-1.5)**.

**(9) Hedging strategy — đa dạng hóa thị trường + buffer inventory + higher-value FDI + financial hedging**

Bốn nguyên tắc: (a) Đa dạng hóa qua RCEP + CPTPP + ACFTA + GCC + India corridor — giảm từ 30% → 22-25% xuất khẩu sang Mỹ; (b) Front-loading planning + buffer inventory 60-90 ngày; (c) Higher-value FDI partnership thay assembly; (d) Forex hedging: forward contracts + multi-currency invoicing 30% EUR + 30% JPY + 40% USD.

**Hàm ý cho CĐ2**: biến `Hedging_Capability_Index` — robustness check #9.

#### 7.3.4 Hàm ý cho Chuyên đề 2 và luận án

**Sáu đóng góp kế thừa từ CĐ1 sang CĐ2**:

**(1) Pool dữ liệu vi mô lớn nhất về doanh nghiệp châu Á hiện có**: 101.185 doanh nghiệp × 47 nền kinh tế × 108 cặp quốc gia × năm × 14 đợt khảo sát (2009–2025) — pipeline WBES tái lập được với STATA code đã xác minh, sẵn sàng mở rộng cho CĐ2.

**(2) Khung phân loại ICRV 6 phân nhóm con → 8 phân nhóm con**: CĐ1 đề xuất 6 sub-regime (Advanced innovation-driven, Advanced resource-driven, Upper-middle, Emerging, Frontier, SIDS Pacific). CĐ2 mở rộng thành **8 sub-regime** bằng cách tách Emerging thành 3 phân nhóm con: (a) FDI-led SEA (Việt Nam, Indonesia, Philippines — FSTS cao, TCI thấp); (b) dân số lớn nội địa (Ấn Độ, Sri Lanka, Jordan — FSTS thấp, spillover cao); (c) khai khoáng (Mongolia — 4 đợt, FSTS 5,0%). Tổng: 2 Advanced + 1 Upper-middle + 3 Emerging + 1 Frontier + 1 SIDS = **8 sub-regime**.

**(3) Bằng chứng tồn tại (existence evidence) phi tuyến FSTS→năng suất**: Turning point thực nghiệm từ P3 và P4: ~49,4% (Trung Quốc 2012), ~47,2% (Trung Quốc 2024), ~85% (Singapore — P4, Mar et al., 2026). Pattern inverted-U xác nhận trong CĐ1, định hướng trực tiếp cho **H1**.

**(4) Bốn lần đảo dấu xuyên phân nhóm con**: Hệ số tương quan FSTS–năng suất đảo từ dương (Emerging/Frontier) → âm (Advanced innovation-driven) → không có ý nghĩa (SIDS) — bằng chứng cho **H2, H3, H4**. Pattern đảo dấu DAI tương tự (−0,129 ở Advanced, +0,072 ở Frontier) xác nhận "digital theatre" warning (H3 — Verhoef et al., 2021).

**(5) Forced internationalization penalty — trường hợp biên SIDS Pacific**: FSTS không tương quan hoặc tương quan âm với năng suất ở 7 SIDS (n=1.371) — Kiribati 2025 là extreme case: FSTS 1,03%, FDI 0,7%, website 18,7%. Bằng chứng trực tiếp cho **H6** (Briguglio, 1995; Bertram, 2006).

**(6) Bằng chứng kênh FDI — cụm tài nguyên Gulf**: FDI ≥10% tương quan dương mạnh (+0,222) với năng suất ở Advanced resource-driven (Saudi Arabia, Qatar, Kuwait) trong khi FSTS tương quan yếu — cơ sở cho **H5** (FDI là kênh năng suất chủ đạo thay thế FSTS ở nền kinh tế tài nguyên dẫn dắt).

---

**Hệ giả thuyết H1–H6 của Chuyên đề 2 — định hướng có dấu (directional specification)**:

> **H1** *(phi tuyến FSTS→log năng suất)*: Mối quan hệ FSTS→log năng suất có dạng **inverted-U (phi tuyến bậc hai)**: β₁ > 0 (hệ số FSTS), β₂ < 0 (hệ số FSTS²). Turning point dự kiến ≈ 47–52% trong nhóm Emerging–Frontier và dịch phải ≈ 80–85% trong nhóm Advanced innovation-driven. Kiểm định bằng Lind–Mehlum (2010) extreme bounds test.

> **H2** *(TCI điều tiết — absorptive capacity mechanism)*: Tương tác TCI × FSTS có hệ số **β(FSTS×TCI) > 0** — năng lực công nghệ tích lũy khuếch đại lợi ích quốc tế hóa trong vùng FSTS thấp–trung, thu hẹp turning point khi TCI cao (Cohen & Levinthal, 1990; Lall, 1992).

> **H3** *(DAI có điều kiện — digital theatre boundary)*: β(DAI) **> 0** trong Emerging và Frontier; β(DAI) **≤ 0** trong Advanced innovation-driven (diminishing returns + substitution effect). Kiểm định bằng interaction DAI × ICRV_advanced dummy (Verhoef et al., 2021).

> **H4** *(phân nhóm con thể chế điều tiết cường độ)*: Hệ số FSTS **khác biệt có ý nghĩa thống kê xuyên 8 phân nhóm con** — F-test p < 0,05. Thể chế mạnh tương ứng với turning point cao hơn và biên độ positive effect rộng hơn (Xu, 2024; Kafouros et al., 2023).

> **H5** *(cụm tài nguyên — FDI thay thế FSTS)*: β(FDI×Resource) **> 0** nhưng β(FSTS×Resource) **< β(FSTS×Innovation)** tại Advanced resource-driven — FDI là kênh năng suất chủ đạo; FSTS tác động yếu hoặc không đáng kể (Auty, 1993; Sachs & Warner, 2001).

> **H6** *(forced internationalization penalty — SIDS Pacific)*: β(FSTS) **không có ý nghĩa thống kê hoặc âm** khi tương tác với dummy SIDS — U-curve Lu & Beamish (2004) không vận hành khi thiếu 3 điều kiện cấu trúc (§2.6): quy mô thị trường tối thiểu, hạ tầng thể chế, năng lực hấp thụ (Briguglio, 1995; Bertram, 2006).

---

**Hai đặc tả hồi quy cốt lõi và 8 robustness checks**:

*Đặc tả cơ sở (OLS + robust SE)*:
```
log_productivity_ij = α + β₁·FSTS + β₂·FSTS² + β₃·TCI + β₄·DAI
                     + β₅·(FSTS×TCI) + β₆·(DAI×ICRV_advanced)
                     + X·γ + μ_j + λ_t + ε_ij
```
*Đặc tả IV-2SLS (kiểm soát nội sinh)*: Biến công cụ `internet_penetration_lagged_j` (độ trễ 2 năm tỷ lệ phổ cập internet quốc gia). Kiểm tra Sargan–Hansen weak-instrument test.

**8 robustness checks** (nâng từ 5 lên 8): (#1) Manufacturing-only subsample; (#2) ICT exclusion test (đã promote §4.4.5 file 15); (#3) Tourism-separated SIDS; (#4) Construction-tested Gulf; (#5) Mining-excluded resource economies; (#6) **Anchor model BREADY** — chạy trên ≤2024 → neo hệ số → test stability với 2025 data (§4.11.2 file 15); (#7) **Panel hậu đại dịch độc lập 2025** — out-of-sample validation (§4.11.3 file 15); (#8) Interaction term Kafouros (2023) replication — industry × institutional dynamism. CĐ2 dành §X.Y riêng cho robustness #6–#8.

---

**Cấu trúc 5-chương luận án và vị trí CĐ1**:

| Chương | Nội dung | Nguồn |
|--------|----------|-------|
| Ch.1 | Tổng quan nghiên cứu, khoảng trống, câu hỏi nghiên cứu | Luận án |
| Ch.2 | Cơ sở lý luận: CDCM 4-tier, ICRV, U-curve điều kiện biên | Luận án (kế thừa CĐ1 Ch.2–3) |
| Ch.3 | **CĐ1** — Thực trạng hiệu quả doanh nghiệp châu Á (mô tả–chẩn đoán) | File 14–16 |
| Ch.4 | **CĐ2** — Phân tích nhân quả H1–H6 (OLS + IV + Lind-Mehlum) | CĐ2 |
| Ch.5 | Kết luận tổng hợp — đóng góp lý luận, chính sách, hướng mở | Luận án |

### 7.4 Hạn chế của chuyên đề

**(1) Thiết kế cắt ngang trong từng mốc khảo sát (cross-sectional design)**: WBES thu thập dữ liệu tại một điểm thời gian trong từng đợt; không theo dõi cùng một doanh nghiệp qua nhiều đợt (unbalanced pseudo-panel). Kết luận nhân quả mạnh đòi hỏi giả định biến công cụ (instrument) nghiêm ngặt — CĐ1 không đáp ứng do mục tiêu mô tả–chẩn đoán. CĐ2 sẽ xây dựng cohort-level pseudo-panel và áp dụng IV-2SLS với biến công cụ cấp quốc gia.

**(2) Sai số đo lường do tự khai báo (self-report measurement error)**: Tất cả biến WBES — doanh số, lao động, chi phí, tỷ lệ xuất khẩu (FSTS) — dựa trên khai báo của quản lý doanh nghiệp, không được kiểm chứng độc lập qua dữ liệu hải quan hay thuế. Sai số phân loại và recall bias có thể làm giảm ước lượng cường độ hiệu ứng, đặc biệt ở nhóm Frontier (17 nước) nơi năng lực kế toán thấp.

**(3) Ranh giới phân nhóm ICRV do nhà nghiên cứu áp đặt (researcher-defined classification boundaries)**: Khung 6 phân nhóm con ICRV là phân loại lý thuyết; ranh giới giữa Upper-middle và Emerging (ví dụ: Malaysia vs Thái Lan) có thể tranh luận. Phân loại lựa chọn ảnh hưởng đến hệ số tương quan và pattern đảo dấu trong §6. CĐ2 sẽ kiểm tra độ nhạy (robustness check #4) với phân loại thay thế — nhóm thu nhập WB và phân loại MSCI.

**(4) Chỉ số tổng hợp DAI/TCI giả định trọng số bằng nhau (equal-weight formative index)**: DAI và TCI được tính bằng trung bình đơn giản của các thành phần thành phần (website, e-payment cho DAI; R&D, ISO cho TCI); trọng số tương đối chưa được kiểm tra qua Confirmatory Factor Analysis (CFA) hay Weighted Least Squares. Mô hình phản chiếu (reflective model) thay thế có thể cho kết quả khác. CĐ2 so sánh 2 đặc tả trong robustness check #2.

**(5) Phạm vi thực nghiệm P3–P5 giới hạn ở 3 quốc gia**: Ba bản thảo P3 (Việt Nam — JABS), P4 (Singapore — MIR), P5 (Trung Quốc — IJOEM) chỉ bao phủ 3 trong 47 nền kinh tế; external validity của kết luận xuyên nhóm Frontier (17 nước) và các nền kinh tế Emerging chưa được kiểm nghiệm trực tiếp. P8 (SIDS Pacific) và P6 meta-analysis sẽ mở rộng phạm vi kiểm chứng.

**(6) Mối quan hệ nhân quả ngược (reverse causality — selection bias)**: Năng suất cao có thể thúc đẩy doanh nghiệp đầu tư nhiều hơn vào số hóa và công nghệ (productive firms self-select into technology adoption) thay vì ngược lại. CĐ1 không giải quyết nội sinh — phù hợp với mục tiêu mô tả–chẩn đoán; CĐ2 sẽ kiểm soát bằng IV-2SLS với biến công cụ `internet_penetration_lagged` ở cấp quốc gia.

**(7) Chưa có biến `GVC_participation_rate` ở cấp doanh nghiệp**: WBES không đo trực tiếp mức độ tham gia chuỗi giá trị toàn cầu ở cấp doanh nghiệp; cần kết hợp với dữ liệu OECD TiVA hoặc ADB MRIO ở cấp ngành × quốc gia. Biến này có thể điều tiết quan trọng mối quan hệ FSTS–năng suất, đặc biệt với GVC-intensive economies (Việt Nam, Philippines, Malaysia). CĐ2 sẽ khắc phục bằng cách merge WBES × TiVA 2021 ở cấp ngành 2 chữ số ISIC.

**(8) Meta-analysis tổng hợp văn liệu I→P cho châu Á (P6) chưa hoàn thành**: Đỗ et al. (202X, in preparation — P6) đang tiến hành meta-analysis tổng hợp hệ thống văn liệu I→P cho 47 nền kinh tế châu Á và Thái Bình Dương; pooled effect sizes từ P6 dự kiến sẽ cung cấp hiệu chỉnh định lượng (quantitative calibration) cho các giả thuyết H1–H6 của CĐ2. CĐ1 hiện sử dụng systematic narrative review (§2.3) thay thế — phương pháp phù hợp với mục tiêu mô tả–chẩn đoán và được chuẩn hóa theo PRISMA 2020. P6 sẽ được tích hợp khi hoàn thành (dự kiến 06/2027).

### 7.5 Kế hoạch hoàn thiện

**Giai đoạn 1 (06/2026–07/2026) — Hoàn thiện các bản thảo thực nghiệm**:
- Nộp P3 (Đỗ & Phan, 2026) lên *Journal of Asia Business Studies* (Emerald) — 06/2026.
- Nộp P4 (Mar et al., 2026) lên *Management International Review* (Springer) — 06/2026.
- Nộp P5 lên *International Journal of Emerging Markets* (Emerald) — 07/2026.
- Nộp CĐ1 (file 14–16 định dạng CTU DOCX) cho Hội đồng khoa học CTU xét duyệt lần 1 — 07/2026.

**Giai đoạn 2 (07/2026–08/2026) — Xây dựng nền tảng CĐ2 và P6**:
- Tìm kiếm cơ sở dữ liệu P6: Web of Science, Scopus, EconLit, PsycINFO (theo PRISMA protocol `thesis/p6_prisma_protocol.md`).
- Screening và full-text review 2 vòng độc lập → trích xuất dữ liệu effect size.
- Chuẩn bị dataset CĐ2: merge WBES 2009–2025 × ICRV typology × TiVA × WGI × AIPI.
- Xây dựng R framework three-level meta-analysis (`p6_scripts/01_baseline_model.R`).

**Giai đoạn 3 (08/2026–09/2026) — Phân tích thực nghiệm CĐ2**:
- Chạy specification cơ sở OLS + IV-2SLS cho H1–H6 trên panel 2009–2025.
- Hoàn thành 8 robustness checks (#1–#8 theo §7.3.4).
- Lind–Mehlum (2010) U-shape test cho H1; Wald test xuyên 8 sub-regime cho H4.
- Viết CĐ2 draft (dự kiến ~80.000 từ tiếng Việt) theo định dạng CTU QĐ 1799/SH.

**Giai đoạn 4 (09/2026–12/2026) — Tổng hợp luận án và bảo vệ**:
- Tích hợp CĐ1 + CĐ2 + P6 (khi sẵn sàng) thành luận án 5 chương.
- Nộp luận án cho Hội đồng phản biện độc lập CTU — dự kiến 10/2026.
- Chỉnh sửa theo góp ý Hội đồng — 11/2026.
- Bảo vệ luận án cấp Trường — dự kiến 12/2026.

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ ở `thesis/04_references_apa7.md` (v2.5).

---

## PHỤ LỤC

### Phụ lục A — Phạm vi thực tế của nhóm dữ liệu WBES

47 nước, 108 cặp QG×năm, 101.185 doanh nghiệp, 7 SIDS bao gồm Kiribati 2025.

### Phụ lục B – G

(Sẽ mở rộng giai đoạn 1–3 tháng 6–8/2026.)
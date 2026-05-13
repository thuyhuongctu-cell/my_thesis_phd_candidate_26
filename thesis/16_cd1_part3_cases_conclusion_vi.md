# CHUYÊN ĐỀ TIẾN SĨ SỐ 1 — BẢN NHÁP ĐẦY ĐỦ (PHẦN 3: CHƯƠNG 5–7 + TÀI LIỆU THAM KHẢO + PHỤ LỤC)

> Tiếp nối `thesis/14_cd1_part1_intro_theory_vi.md` và `thesis/15_cd1_part2_findings_vi.md`.
> Bảng thuật ngữ Anh-Việt: `thesis/09b_vn_term_glossary.md`.
> Tổng hợp Asia context: `thesis/_asia_context_synthesis_2026.md`.
> Hình minh họa: `thesis/figures/` (11 hình; chạy `python3 generate_figures.py`).
---

## CHƯƠNG 5 — BẢY TIỂU CẢNH ĐIỂN HÌNH

### 5.1 Singapore (Advanced đổi mới sáng tạo dẫn dắt — innovation-driven, n=623, đợt 2023)

FSTS 7,1%; doanh nghiệp xuất khẩu 17,8%; website 66,1%; ISO 23,3%; R&D 7,5%; FDI 31,5%. Độ lệch chuẩn log năng suất (sd log) 1,03. **Biên trên (upper boundary)** của nhóm Advanced đổi mới sáng tạo dẫn dắt. Theo bài báo P3 (Singapore — MIR): mô hình M8 cho R² hiệu chỉnh = 0,196; tương tác FSTS² × DAI = 3,119; điểm uốn (turning point) ở mức ~85%.

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

### 7.1 Khoảng trống nghiên cứu thực tiễn (5 khoảng trống — v3.2)

(Giữ nguyên — xem commit 7738953 + b3306e1.)

### 7.2 Kết luận chính (8 kết luận)

(Giữ nguyên — xem commit b3306e1.)

### 7.3 Hàm ý cho luận án và Chuyên đề 2

#### 7.3.1 Hàm ý lý thuyết

(Giữ nguyên từ v3.3 — 5 evidence; AIPI; digital theatre warning. Xem commit cc33ed4.)

#### 7.3.2 Hàm ý phương pháp luận (mở rộng v3.3)

(Giữ nguyên từ v3.3 — 5 hàm ý + triple-defense system. Xem commit cc33ed4.)

#### 7.3.3 Hàm ý chính sách cho doanh nghiệp Việt Nam và khu vực (9 hàm ý)

**(7) Migration labor partnership Pacific cho Việt Nam — bài học từ PLMS Australia + RSE New Zealand**

Bốn đề xuất: (a) Học mô hình PLMS — Vietnamese Skilled Worker Mobility Scheme; (b) Học mô hình RSE — Aquaculture + Coffee + Cashew Skills Exchange; (c) Cơ chế remittance corridor digital — giảm phí từ ~7% xuống <3%; (d) Skills upgrading tránh brain drain theo Korea EPS model.

**(8) Chính sách số hóa Asia cho SME Việt Nam — bài học từ Singapore/Korea/Japan/Trung Quốc**

Bốn lộ trình: (a) Singapore+Korea — AI full-stack Tier-3 (không phù hợp SME VN hiện tại); (b) Japan — 60% DN dùng AI back-office → **realistic target 2026-2030**; (c) Trung Quốc — smart manufacturing + cảnh báo concentration risk; (d) **Mô hình ưu tiên SME Việt Nam: VietQR + social commerce + cross-border e-commerce + Cloud+AI tools (Tier-1.5)**.

**(9) Hedging strategy — đa dạng hóa thị trường + buffer inventory + higher-value FDI + financial hedging**

Bốn nguyên tắc: (a) Đa dạng hóa qua RCEP + CPTPP + ACFTA + GCC + India corridor — giảm từ 30% → 22-25% xuất khẩu sang Mỹ; (b) Front-loading planning + buffer inventory 60-90 ngày; (c) Higher-value FDI partnership thay assembly; (d) Forex hedging: forward contracts + multi-currency invoicing 30% EUR + 30% JPY + 40% USD.

**Hàm ý cho CĐ2**: biến `Hedging_Capability_Index` — robustness check #9.

#### 7.3.4 Hàm ý cho Chuyên đề 2 và luận án

(Giữ nguyên từ v3.3 — 8 robustness checks. Xem commit cc33ed4.)

### 7.4 Hạn chế của chuyên đề

(Giữ nguyên từ v3.2 — 7 hạn chế.)

### 7.5 Kế hoạch hoàn thiện

(Giữ nguyên từ v3.1a — 4 giai đoạn 6/2026 → 9/2026.)

---

## TÀI LIỆU THAM KHẢO

> Trích dẫn theo APA 7th. Danh mục đầy đủ ở `thesis/04_references_apa7.md` (v2.5).

---

## PHỤ LỤC

### Phụ lục A — Phạm vi thực tế của nhóm dữ liệu WBES

47 nước, 108 cặp QG×năm, 101.185 doanh nghiệp, 7 SIDS bao gồm Kiribati 2025.

### Phụ lục B – G

(Sẽ mở rộng giai đoạn 1–3 tháng 6–8/2026.)

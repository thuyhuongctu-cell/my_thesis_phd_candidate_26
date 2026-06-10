# KẾ HOẠCH RE-LOCK 49/96.415 — đồng bộ Luận án ↔ CĐ1 ↔ CĐ2 (quyết định NCS 2026-06-10)

**Quyết định NCS:** (1) membership: máy lập kế hoạch + kiểm tra, căn về nhãn dữ liệu; (2) **re-lock toàn bộ về 49 nước/96.415**; (3) P3/P5 N của CĐ1 là "pool mô tả", giữ + ghi rõ khác "mẫu hồi quy".

> Nguyên tắc liêm chính: **không thả số từ pipeline khác vào CĐ**. Re-lock đúng nghĩa = chạy LẠI pipeline mô tả của CĐ1 trên khung 49 nước, KHÔNG phải dán số từ file phân tích P7.

---

## A. 🔴 RÀO CẢN KỸ THUẬT — vì sao không re-lock cơ học được ngay

Đối chiếu `data_wbes/p7/p7_pooled_clean.csv` (lock P7, 96.415) với số mô tả CĐ1 (lock 101.185):

| Biến | File P7 (per-label) | CĐ1 báo cáo | Kết luận |
|---|---|---|---|
| sd log LP (Advanced) | **3,43** | **1,03** | Khác winsorize (CĐ1 winsorize 1/99 trong cụm; file không) |
| FDI ≥10% | **≈0%** (foreign_own_pct thưa) | 11,1–23,5% | Biến FDI khác / mã hóa khác |
| R&D%, ISO%, đổi mới sản phẩm | **KHÔNG có** | có (Bảng 2.3.4.1) | File chỉ có TCI tổng hợp |

→ **File phân tích P7 ≠ pipeline mô tả CĐ1.** Tái tính bảng mô tả CĐ1 (FSTS/website/FDI/R&D/ISO/sd theo nhóm) từ file này sẽ ra **số sai** (sd 3,43 thay vì 1,03; FDI 0%). **Cấm dán.**

**Dữ liệu thô (raw WBES) cho đủ 49 nước KHÔNG có trong repo** (`raw_dta/` chỉ 9 nền + India). → Không thể chạy lại pipeline CĐ1 trong môi trường hiện tại.

---

## B. ✅ PHẦN RE-LOCK AN TOÀN (không phụ thuộc pipeline — máy làm được khi NCS duyệt)

Các mục **cấu trúc/membership** không phụ thuộc winsorize/biến:

| # | Việc | Nguồn chuẩn |
|---|---|---|
| B1 | Đếm nền kinh tế: **47 → 49** (Á–TBD) | dữ liệu (52 − Comoros/Turkey/Cyprus) |
| B2 | Pool phân loại: **101.185 → 96.415**; mẫu hồi quy **91.864** | dữ liệu |
| B3 | **Danh sách nước theo nhóm** = nhãn dữ liệu (Mục C) | icrv_label |
| B4 | Crosswalk tên-CĐ ↔ icrv_label (sửa hoán đổi Emerging/Frontier) | Mục C |
| B5 | SIDS pool = **1.371** (7 Pacific); bỏ 2.385 (A.1), 5.185 (Bảng 2.8) | dữ liệu |
| B6 | P3/P5: ghi rõ "pool mô tả 3.077/4.889" vs "mẫu hồi quy 2.958/4.559" | bài P3/P5 |
| B7 | P8 trong CĐ2: chính 7-Pacific/N=209/β=−1,339; 9-nước/1.469 là robustness | bài P8 |

> ⚠️ **Cảnh báo cascade:** B1–B5 đổi membership → **các bảng % mô tả theo nhóm trong CĐ1 phải tái tính lại** (vì Sri Lanka/Jordan/Bangladesh/Pakistan chuyển nhóm làm đổi mọi trung bình nhóm). Do đó B1–B5 **chỉ trọn vẹn** khi đi kèm phần C (tái tính), nếu không lại tạo mâu thuẫn mới.

---

## C. PLAN + VERIFY MEMBERSHIP (Q1 — "máy lập kế hoạch và kiểm tra")

**Chuẩn = nhãn dữ liệu `icrv_label`** (vì P7/luận án đã chạy thực nghiệm trên đó; NCS đã chọn lock theo dữ liệu). Phân loại canonical 6 nhóm (đặt lại tên cho khớp tiêu chí WGI/GNI):

| Nhóm (đề xuất tên chuẩn) | icrv_label | # nước | Nước |
|---|---|:--:|---|
| I Advanced–innovation | Advanced_innovation | 5* | HongKong, Israel, Korea, Singapore, Taiwan (*Cyprus loại ngoài Á) |
| II Advanced–resource | Advanced_resource | 6 | Bahrain, Brunei, Kuwait, **Oman**, Qatar, SaudiArabia |
| III Upper-middle | Upper_mid | 6* | Armenia, China, Georgia, Kazakhstan, Malaysia, Thailand (*Turkey loại ngoài Á) |
| IV Lower-mid transition | Lower_mid_transition | 7 | Bangladesh, India, Indonesia, Mongolia, **Pakistan**, Philippines, Vietnam |
| V Emerging | Emerging | 17 | Afghanistan, Azerbaijan, Bhutan, Cambodia, Iraq, **Jordan**, Kyrgyz, Laos, Lebanon, Maldives, Myanmar, Nepal, **SriLanka**, Tajikistan, Turkmenistan, Uzbekistan, Yemen |
| VI SIDS | SIDS_small | 8* | Fiji, Kiribati, PNG, Samoa, Solomon, **TimorLeste**, Tonga, Vanuatu (*Comoros loại ngoài Á; 7-Pacific cho P8) |

**Verify cần NCS xác nhận (điểm khác CĐ hiện tại):**
- Sri Lanka, Jordan → nhóm **Emerging (V)** theo dữ liệu, KHÔNG phải Nhóm IV như CĐ viết. *(Kiểm tra: GNI/capita Sri Lanka ~$3.8k, Jordan ~$4.4k — gần ngưỡng IV/V; NCS xác nhận.)*
- Bangladesh, Pakistan → **Lower_mid (IV)** theo dữ liệu, KHÔNG phải Frontier như CĐ. *(GNI Bangladesh ~$2.8k, Pakistan ~$1.5k — biên IV/V; xác nhận.)*
- Timor-Leste → **SIDS (VI)** theo dữ liệu, KHÔNG phải Frontier.
- Oman → **Advanced_resource (II)** — CĐ hiện thiếu Oman.
- **Tên:** CĐ gọi "Emerging=IV(7)/Frontier=V(17)"; dữ liệu nhãn ngược. Đề xuất đổi tên CĐ theo bảng trên (IV=Lower-mid, V=Emerging) HOẶC đổi nhãn dữ liệu — **phải 1 trong 2, nhất quán**.

---

## D. CÁC BƯỚC THỰC THI (staged)

**Bước 1 — máy làm ngay (an toàn, không cần raw):** áp B3/B4 + Mục C — sửa **danh sách nước theo nhóm** + **tên nhóm** + **crosswalk** trong CĐ1/CĐ2 cho khớp nhãn dữ liệu; B6 (ghi chú pool vs hồi quy P3/P5); B7 (P8). *(Chưa đụng số % mô tả.)*

**Bước 2 — cần raw WBES 49 nước + script CĐ1 (NCS cung cấp hoặc phiên có raw):** chạy lại pipeline mô tả CĐ1 (winsorize 1/99 trong cụm, R&D/ISO/đổi mới, FDI) trên khung 49 nước → thay toàn bộ bảng % mô tả + n_firms; đổi 101.185→96.415, 47→49. Regenerate docx.

**Bước 3 — kiểm tra cuối:** chạy lại `MASTER_CONSISTENCY_RECONCILIATION` để xác nhận mọi ô khớp.

---

## E. KHUYẾN NGHỊ
- **Bước 1 làm được ngay** (membership/tên/crosswalk + P3/P5 note + P8) — đề nghị NCS xác nhận 5 điểm membership ở Mục C để máy áp.
- **Bước 2 (re-lock số mô tả) KHÔNG làm được trong môi trường này** vì thiếu raw WBES 49 nước + pipeline khác. NCS cần: cung cấp raw WBES (đủ 49 nền) hoặc chạy script CĐ1 trên khung 49, rồi máy đồng bộ docx + kiểm tra.
- **Tuyệt đối không** dán số từ `p7_pooled_clean.csv` vào bảng mô tả CĐ1 (sai pipeline → sai số).


---

## F. KẾT QUẢ TÌM RAW WBES TRÊN NHÁNH edit/vietnamese (2026-06-10) — KHÔNG ĐỦ

Đã quét `origin/claude/edit-vietnamese-academic-standards-xcAmn` + `origin/claude/vietnamese-academic-standards-QuiLM`:
| Nguồn | Phủ | R&D/ISO riêng | sd LP khớp CĐ1 (~1,03)? |
|---|---|:--:|:--:|
| `raw_dta/*.dta` | chỉ **9 nền** | có (9 nền) | — |
| `data_wbes/analysis/pooled_wbes_6waves.csv` | chỉ **3 nước** (CHN/SGP/VNM) | ✅ | ❌ (sd~3,82) |
| `data_wbes/p7/p7_pooled_rich.csv` | 52 nước | ❌ (chỉ TCI/DAI tổng hợp) | ❌ |
| `data_wbes/p7/p7_pooled_clean.csv` | 52 nước | ❌ | ❌ (sd 3,43) |

→ **Raw WBES đủ 49 nước + đúng pipeline mô tả CĐ1 không có trên bất kỳ nhánh nào.** Bước 2 (re-lock số mô tả) **không thể thực thi** trong môi trường hiện tại mà không bịa.

**Cần NCS:** upload trực tiếp **raw WBES đủ 49 nền** (hoặc file pool 101.185 gốc CĐ1 với đủ biến website/R&D/ISO/đổi mới/FDI + LP đã winsorize) → khi đó máy chạy re-lock đầy đủ + đồng bộ docx.

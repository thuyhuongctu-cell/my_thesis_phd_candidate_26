# Bằng chứng vòng chỉnh sửa (revision evidence) — 2026-06-23

> Sinh bởi `scripts/revision_evidence.py` từ `data_wbes/p7/p7_pooled_clean.csv`
> (khung canonical 50 nền, N(ln_labor_prod)=78.810). Bảng số: `reviews/revision_evidence_estimates.csv`.
> Mục đích: cung cấp bằng chứng kiểm chứng được cho các phản biện của vòng review,
> để NCS rà soát và tích hợp. **Tài liệu này KHÔNG sửa luận án** — chỉ bổ sung bằng chứng.

## Tóm tắt điều hành

| # | Kiểm định | Kết quả | Khắc phục phản biện | Hướng |
|---|---|---|---|---|
| 1 | Dạng hàm bậc 3 (cubic) | β₃=+1,008 **p=,525**; ΔBIC=+8,4 (cubic xấu hơn) | M-6 "vì sao không cubic?" | ✅ Bảo vệ đặc tả bậc 2 |
| 2 | Common-method bias (Harman) | Nhân tố 1 = **31,6%** phương sai (<50%) | R1 CMB chưa kiểm định | ✅ CMB không phải mối đe dọa lớn |
| 3 | Robustness ngành chế tạo | TP=49,1%, **p(β₂)=,004** | M-5 ngành/commodity | ✅ Chữ U ngược vững khi chỉ chế tạo |
| 4 | Biên tham gia vs cường độ (VN) | Toàn mẫu TP 35,2% (p<,001); **chỉ DN XK: β₂=−1,66, p=,170 (n.s.)** | ① Addendum CRITICAL | ⚠️ Xác nhận: U-shape do biên tham gia |
| 5 | Độ giá trị tách bạch TCI/DAI (formative) | Hai **chỉ số hợp thành tách biệt** (r=0,344; chia sẻ 11,8% phương sai; mạng nomological khác biệt) | M-2 / D-3 | ✅ Củng cố tính mới #2 |
| 6 | Đối chiếu TP canonical | Đặc tả nhanh cho TP≈49% (canonical M5=43,6%) | M-6 TP nhạy đặc tả | ⚠️ Nêu rõ TP phụ thuộc đặc tả |

---

## 1. Dạng hàm: bậc 2 là đủ (bác bỏ cubic) — ✅ củng cố

Thêm số hạng bậc ba vào mô hình gộp (FE nền + năm, cluster theo nền):
`β(FSTS³) = +1,008, p = ,525` — **không có ý nghĩa**. ΔAIC ≈ 0 nhưng **ΔBIC = +8,38**
(cubic bị phạt, xấu hơn). Kết luận: **đặc tả bậc hai là đủ; cubic không thêm thông tin** —
trả lời trực tiếp phản biện "vì sao không thử cubic/chữ S?". Đề nghị: chèn 1 dòng kết quả này
vào Mục 3.4.3 hoặc kiểm định độ vững Ch4 (cùng nhóm với AIC/BIC đã có ở P3).

## 2. Common-method bias không nghiêm trọng — ✅ củng cố

Kiểm định Harman single-factor trên 6 biến lõi (năng suất, FSTS, TCI, DAI, quy mô, tuổi):
nhân tố đầu tiên giải thích **31,6%** tổng phương sai, **dưới ngưỡng 50%** thường dùng làm
cờ cảnh báo CMB. Vì mọi biến đến từ cùng một bảng khảo sát, đây là kiểm định mà reviewer Q1
sẽ hỏi. Đề nghị: thêm 1 câu + số này vào Mục 3.5 (kiểm định độ vững) — chi phí gần như bằng 0.

## 3. Chữ U ngược vững khi chỉ ngành chế tạo — ✅ củng cố

Lọc ISIC chế tạo (1–3, N=31.540): TP=49,1%, **β₂ p=,004**. Chữ U ngược không phải tạo tác
của ngành khai khoáng/hàng hóa (phản biện M-5). *Lưu ý:* chưa loại được hoàn toàn yếu tố
thâm dụng vốn vì WBES thiếu biến vốn — vẫn nên giữ cảnh báo ở Mục 5.5.

## 4. ⚠️ Việt Nam: chữ U ngược chủ yếu là BIÊN THAM GIA (phát hiện then chốt)

- Toàn mẫu VN (N=2.759): TP=35,2%, β₂ p<,001; **70,3% doanh nghiệp ở FSTS=0**.
- **Chỉ doanh nghiệp xuất khẩu (N=820): β₂ = −1,66, p = ,170 — KHÔNG có ý nghĩa.**

Tức độ cong biến mất khi bỏ bước nhảy không-XK → XK. Đây **xác nhận độc lập** phát hiện của
luận án (Mục 5.1.7) và của báo cáo review: trụ cột "vùng giữa" phần lớn là **phần thưởng
tham gia xuất khẩu**, không phải lợi ích phi tuyến theo cường độ. **Hệ quả bắt buộc:** phát ngôn
lại — "bằng chứng mạnh nhất cho biên tham gia", không phải "cho chữ U ngược theo cường độ".

## 5. ✅ Độ giá trị tách bạch TCI/DAI — đo lường FORMATIVE (đã chạy lại đúng cách)

> **Đính chính phương pháp (2026-06-23, vòng 2).** Bản đầu của mục này dùng EFA + tương quan nội bộ
> để đánh giá tách bạch TCI/DAI và kết luận "không tách sạch". Đó là **sai loại kiểm định**: EFA và
> nhất quán nội bộ là công cụ cho cấu trúc **reflective**, trong khi TCI/DAI là **chỉ số hợp thành
> (formative)** — item là *nguyên nhân cấu thành* năng lực, không phải biểu hiện của biến tiềm ẩn.
> Theo Coltman et al. (2008), chỉ báo formative **không cần đồng biến**. Đã chạy lại bằng kiểm định
> đúng (cấp chỉ số hợp thành) trên dữ liệu thực; kết luận **đảo lại** thành củng cố tính mới #2.

**Tương quan item nội bộ thấp là ĐÚNG KỲ VỌNG (không phải lỗi):**

| Cặp chỉ báo (trong cùng 1 chỉ số) | Tương quan | Diễn giải |
|---|---|---|
| tci_cert ↔ tci_foreign_tech (trong TCI) | 0,12 | formative → thấp là bình thường |
| dai_website ↔ dai_epay (trong DAI) | 0,03 | formative → thấp là bình thường |

**Kiểm định đúng — tách biệt ở cấp chỉ số hợp thành + mạng nomological** (N=8.574 có đủ cả hai chỉ số đầy đủ):

| Phép đo | Giá trị | Diễn giải |
|---|---|---|
| corr(tci_z, dai_z) | **0,344** | tách biệt rõ (0=tách hẳn, 1=trùng) |
| Phương sai chia sẻ (r²) | **11,8%** | hai chỉ số đo hai chiều khác nhau |
| Đưa đồng thời vào 1 mô hình | TCI **+0,18** (p<,001); DAI **+0,131** (p<,001) | mỗi chỉ số có hiệu ứng riêng phần độc lập → **không trùng lặp** |

**Hàm ý:** TCI và DAI là **hai cấu trúc hợp thành tách biệt có mạng nomological khác biệt** — bằng chứng
thực nghiệm *củng cố* tính mới #2 (phân tách TCI/DAI), nhất quán với vai trò điều tiết khác nhau (cả hai
là bộ nâng mặt bằng; vai trò uốn đường cong phụ thuộc chế độ thể chế). Đã cập nhật §3.5.6.4 của luận án
theo khung formative đúng.

### 5.1 Số liệu tách biệt theo từng paper (đã chèn vào Methods/Measurement)

Vì tính mới #2 dùng xuyên các paper P3/P4/P5/P7 (đang phản biện, **chưa công bố**), đã chèn ghi chú khung
formative + bằng chứng tách biệt vào nguồn `_en_clean.md` của từng paper, mỗi paper dùng **số liệu của
chính mẫu mình** (tái lập bằng `scripts/revision_evidence.py`, mục `5c_per_paper`):

| Paper | Mẫu | corr(TCI,DAI) | Phương sai chia sẻ | Ghi chú chèn |
|---|---|--:|--:|---|
| P7 (toàn mẫu 50 nền) | N=94.211 | 0,28 | 8,0% | §3.2 — đoạn "Construct distinctness" + Coltman 2008 |
| P3 Việt Nam | N=3.060 | 0,28 | 8,1% | §3.2 — câu formative + Coltman 2008 |
| P5 Trung Quốc | N=2.183 | 0,18 | 3,4% | §3.2 — "Measurement note" (DAI là control) + Coltman 2008 |
| P4 Singapore | N=623 | 0,13 | 1,6% | §3.2.5 — 1 câu bằng chứng (khung formative đã có sẵn) |

Mỗi paper đã được thêm mục tham chiếu Coltman et al. (2008) khớp với trích dẫn trong văn (đã kiểm tra
in-text ↔ reference 1:1). *Lưu ý:* các bản blinded trong `*/submission/*_package/` là bản dẫn xuất —
khi nộp cần đồng bộ 2–3 câu này (hoặc dựng lại từ nguồn `_en_clean.md`).

## 6. ⚠️ Điểm uốn nhạy với đặc tả

Đặc tả nhanh (FE nền+năm, **không** chuẩn hóa z nội bộ nền–năm cho biến phụ thuộc, bộ kiểm soát
gọn) cho **TP≈49,0%**, so với canonical M5 = 43,6%. Cùng dải, nhưng lệch ~5pp — xác nhận phản biện
M-6 rằng **vị trí điểm uốn phụ thuộc đặc tả/chuẩn hóa**. Không mâu thuẫn kết luận (chữ U ngược vững,
β₁>0, β₂<0 đều p<,01) nhưng nên phát ngôn TP là "dải ~44–51%" thay vì một con số đơn.

---

## CHECKLIST SỬA CÂU CHỮ (Tầng A — để NCS duyệt rồi áp dụng)

| Mã | File · Mục | Sửa | Phản biện |
|---|---|---|---|
| A1 | Toàn bộ Ch4–Ch5 | "ảnh hưởng/tác động nhân quả" → "liên hệ/gắn với"; thêm 1 hộp *Identification caveat* ở đầu Ch4 | M-1 |
| A2 | `chuong_1` §1.9 điểm mới #6; `chuong_5` §5.1.5; abstract | FIP = **đóng góp khái niệm + bằng chứng thăm dò**; nêu p_wild=,66/,082 ngay cạnh; bỏ mọi hàm ý "đã xác nhận" | DA CRITICAL |
| A5 | Ch4 các mục TP | Báo cáo TP **cả khi n.s.**; đổi "hội tụ chặt" → "hội tụ thô ±5pp"; nêu TQ ~48,8% là *lân cận* Nhóm IV, không trùng | DA |
| A6 | `chuong_4` mở đầu §ba vùng | Nêu **trước**: cutoff ICRV tiền định + ICRV×FSTS cấp cá thể n.s. → "ba vùng" là mô thức từ hồi quy phân tầng nhóm | D-2 |
| A7 | `chuong_4` (P3) + `chuong_5` §5.1.7 | Đưa bảng **exporters-only VN (N=820, β₂ p=,170)** lên trung tâm; phát ngôn lại "biên tham gia" | ① (mục 4 trên) |
| A8 | `chuong_3` §3.5 + phụ lục mới | Chèn kết quả mục 1–3,5 trên (cubic n.s., Harman 31,6%, EFA TCI/DAI) | M-2/M-6/CMB |

> Các con số trong checklist đều **đã tái lập** ở `revision_evidence_estimates.csv`, chạy lại bằng
> `python3 scripts/revision_evidence.py`.

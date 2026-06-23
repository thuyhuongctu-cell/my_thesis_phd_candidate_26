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
| 5 | Độ giá trị tách bạch TCI/DAI | Cấu trúc nhân tố **KHÔNG tách sạch** TCI khỏi DAI | M-2 / D-3 | ⚠️ Cần tái khung trung thực |
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

## 5. ⚠️ Độ giá trị tách bạch TCI/DAI YẾU — cần tái khung trung thực

Đây là phát hiện *bất lợi* nhưng phải báo cáo:

| Cặp chỉ báo | Tương quan |
|---|---|
| tci_cert ↔ tci_foreign_tech (2 mục **trong** TCI) | **0,12** (rất thấp) |
| dai_website ↔ tci_cert (chéo DAI–TCI) | **0,29** (cao hơn nội bộ TCI!) |
| dai_epay ↔ dai_website (2 mục **trong** DAI) | 0,03 |

EFA 2 nhân tố: **F1** tải đồng thời tci_cert (−0,75), dai_website (−0,75), tci_foreign_tech (−0,49)
— tức một nhân tố "chính thức hóa/hiện diện" chung; **F2** gần như chỉ tải dai_epay (0,97).
**Cấu trúc nhân tố KHÔNG tách sạch TCI khỏi DAI** như khung lý thuyết tuyên bố; trục phân kỳ
thực nghiệm chính lại là *e-payment vs phần còn lại*, không phải *năng lực vs chấp nhận số*.

**Hàm ý (không bác bỏ đóng góp, nhưng buộc tái khung):** sự phân biệt TCI/DAI nên trình bày là
**phân biệt *khái niệm*** (theo Coltman et al. 2008) có **hỗ trợ thực nghiệm hạn chế** ở mức chỉ báo
nhị phân WBES — *chứ không* tuyên bố hai cấu trúc "không trùng lặp" đã được xác nhận thực nghiệm.
Đây đúng với kết luận của luận án rằng cả hai là "bộ nâng mặt bằng" hơn là "uốn đường cong".
Đề nghị: thêm phụ lục validity (ma trận tương quan + EFA này) và một câu giới hạn ở Mục 5.5.3.

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

# Kết quả ước lượng P7 trên khung 50 nền (gồm Nhật Bản) — BỘ SỐ CHÍNH THỨC

> Theo chỉ đạo của tác giả (lần đầu công bố): ước lượng lại trên 50 nền với spec
> tài liệu hóa đầy đủ, thay bộ số vintage. Engine: pyfixest 0.60 (tương đương
> reghdfe; không có Stata binary trong container — xác nhận lại bằng do-file trên
> máy có Stata trước khi nộp tạp chí). Tái lập: `python3 scripts/p7_run_50econ.py`.
> Spec: lp_z (z trong nền×năm, winsor 1/99), FSTS=(d3b+d3c)/100, FE nền + năm,
> SE cụm theo nền (CRV1). TP=−β₁/(2β₂)+mean(FSTS). Lind–Mehlum một phía.

## A. Mô hình gộp (50 nền, 103 cặp, 88.869 quan sát thô)

| Mô hình | N | β₁ | β₂ | TP | p_LM |
|---|--:|--:|--:|--:|--:|
| M2 (FSTS+FSTS², FE) | 81.022 | +1,189*** | −1,398*** | **51,5%** | <,001 |
| **M5 (+ kiểm soát, FE)** | **79.080** | **+0,500***\* | **−0,721***\* | **43,6%** | **<,001** |
| M7 (+ điều tiết TCI) | 79.220 | +0,627*** | −0,836*** | 46,4% | <,001 |
| M8 (+ điều tiết DAI) | 79.080 | +0,704*** | −0,924*** | 47,1% | <,001 |
| M10 (+ tương tác chế độ yếu) | 79.080 | +0,615*** | −0,833*** | 45,9% | <,001 |

Kiểm soát: fdi10, ln(tuổi), tci_z, dai. Dải TP: **43,6–51,5%**, headline M5 = **43,6%**.

## B. Điểm uốn theo nhóm ICRV (dạng M5 trong từng nhóm)

| Nhóm | N | β₁ (p) | β₂ (p) | TP | p_LM | Đọc |
|---|--:|---|---|--:|--:|---|
| I Adv. đổi mới (gồm Nhật) | 5.581 | +0,698 (,17) | −0,504 (,31) | [79,1%] | ,30 | gần tuyến tính dương; TP ngoài miền, không định vị |
| II Adv. tài nguyên | 2.075 | +0,854 (,045) | −0,730 (,082) | 62,0% | ,081 | U ngược biên ý nghĩa |
| III Trung bình cao | 12.055 | +0,168 (,42) | −0,189 (,48) | [55,0%] | ,26 | không xác định ở cấp nhóm (P5 Trung Quốc riêng: 47–49%***) |
| **IV Chuyển đổi TB-thấp** | **42.094** | **+0,709 (<,001)** | **−1,012 (<,001)** | **43,0%** | **<,001** | **U ngược rõ nét nhất** |
| V Đang nổi | 15.457 | +0,218 (,44) | −0,455 (,21) | [34,8%] | ,18 | quan hệ tan rã |
| VI SIDS (quad) | 1.818 | −0,728 (,010) | +0,870 (,013) | — | 1,0 | không U ngược; dạng lồi |

**Đọc gradient (MỚI)**: chữ U ngược là hiện tượng của **vùng giữa gradient thể chế**
(định hình rõ và tin cậy duy nhất ở Nhóm IV, TP=43,0%, trùng P3 Việt Nam 39–46% và
P9 Ấn Độ 40,7%); ở biên trên thể chế, đường cong **duỗi thẳng gần tuyến tính dương**
(Nhóm I — trùng P4 Singapore); ở biên dưới, quan hệ **mất cấu trúc** (V không ý nghĩa,
VI không U ngược) — trùng tương quan CĐ1 (FSTS r mất ý nghĩa ở SIDS) và meta P6.
Tương tác chế độ-yếu: FSTS×Weak = −0,523 (p=,087) — độ dốc nhánh lên yếu hơn ở thể chế yếu.

## C. Điều tiết TCI / DAI (toàn mẫu)

- TCI: hiệu ứng chính **+0,141*** (p<,001)**; tương tác FSTS×TCI, FSTS²×TCI không ý nghĩa
 đến TCI **nâng mặt bằng**, không uốn đường cong (giữ kết luận cũ).
- DAI: hiệu ứng chính **+0,201*** (p<,001)**; FSTS×DAI −0,271 (p=,149), FSTS²×DAI +0,252 (p=,367)
 đến DAI nâng mặt bằng; chiều nén đường cong cùng hướng nhưng **không ý nghĩa** trên 50 nền
  (mềm hơn kết luận vintage).

## D. FIP (SIDS) — lưu ý spec

7-Pacific, lp_z spec: β(FSTS)=−0,085 (p=,59) — KHÔNG tái tạo FIP. Lý do kỹ thuật:
z-hóa trong từng đợt triệt tiêu biến thiên mức giữa đợt mà FIP của P8 (LP mức,
PPP-adjusted) khai thác. **FIP β=−1,339 là kết quả của spec P8** (LP PPP mức,
7-Pacific, N=959) và giữ nguyên như kết quả của nghiên cứu thành phần P8; luận án
ghi rõ hai spec khác nhau đo hai khía cạnh khác nhau (vị trí trong phân phối đợt
so với mức năng suất tuyệt đối).

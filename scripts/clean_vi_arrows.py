#!/usr/bin/env python3
"""One-off: replace remaining context-dependent arrows and edge-case em-dashes
with explicit Vietnamese wording (Scopus/WoS no-symbol standard).
Each replacement carries enough surrounding context to be unambiguous.
Applied longest-first within a file to avoid partial-overlap corruption.
"""
import re

EN = "–"  # en-dash

REPLACEMENTS = {
"chuyen_de/cd1/00_cd1_ctu_final_vi.md": [
    ("7,2% (2026) → 7,0% (2027)", "7,2% (2026) xuống 7,0% (2027)"),
    ("7,7%→2,7%", "7,7% xuống 2,7%"),
    ("Việt Nam → U ngược", "Việt Nam có dạng U ngược"),
    ("Singapore → tuyến tính dương", "Singapore có dạng tuyến tính dương"),
    ("website only) → **phụ thuộc giai đoạn**", "website only) cho thấy **phụ thuộc giai đoạn**"),
    ("(Tier 1+2) → **mở rộng có điều kiện**", "(Tier 1+2) cho thấy **mở rộng có điều kiện**"),
    ("(+0,00 → +0,50)", "(+0,00 đến +0,50)"),
    ("Rule of Law 0,00 → +0,80", "Rule of Law 0,00 đến +0,80"),
    ("Rule of Law -0,50 → 0,00", "Rule of Law -0,50 đến 0,00"),
    ("+0,00→+0,50", "+0,00 đến +0,50"),
    ("0,00→+0,80", "0,00 đến +0,80"),
    ("-0,50→0,00", "-0,50 đến 0,00"),
    ("voids thể chế → đổi mới bằng nguồn lực", "voids thể chế dẫn đến đổi mới bằng nguồn lực"),
    ("giảm từ 1,00 → 0,86", "giảm từ 1,00 xuống 0,86"),
    ("**biến mất** → bằng chứng cho", "**biến mất**, cung cấp bằng chứng cho"),
    ("-5 đến -10 | —¹ |", "-5 đến -10 | " + EN + "¹ |"),
    ("FDI/R&D (—)", "FDI/R&D (" + EN + ")"),
    ("FSTS 23,2% → 17,9% → 16,1%", "FSTS 23,2%, 17,9%, 16,1%"),
    ("xuất khẩu 37,1% → 23,8%", "xuất khẩu 37,1% xuống 23,8%"),
    ("FSTS 10,9% → 8,8%", "FSTS 10,9% xuống 8,8%"),
    ("(1990–2000) → 42,396 triệu USD", "(1990–2000) lên 42,396 triệu USD"),
    ("**7,2% → 3,2%**", "**từ 7,2% xuống 3,2%**"),
    ("website tăng 39% → 65%", "website tăng từ 39% lên 65%"),
    ("Advanced 0,86 → Upper-middle 1,29", "Advanced 0,86, Upper-middle 1,29"),
    ("SIDS 1,32 → Frontier 1,36", "SIDS 1,32, Frontier 1,36"),
    ("Advanced 11,1% → Emerging 4,7% → SIDS 23,5%", "Advanced 11,1%, Emerging 4,7%, SIDS 23,5%"),
    ("suy giảm 23,2% → 16,1%", "suy giảm từ 23,2% xuống 16,1%"),
    ("lắp ráp downstream → thiết kế", "lắp ráp downstream sang thiết kế"),
    ("PICs/năm → triển khai", "PICs/năm, hướng tới triển khai"),
    ("(100% miễn phí) → Thương mại xã hội → Xuyên biên giới Shopee/Amazon → Cloud và AI cơ bản",
     "(100% miễn phí), tiếp đến Thương mại xã hội, Xuyên biên giới Shopee/Amazon, và Cloud và AI cơ bản"),
    ("ln(LP) → ROS, tăng trưởng doanh thu", "ln(LP) bằng ROS, tăng trưởng doanh thu"),
    ("OLS → hồi quy phân vị", "OLS bằng hồi quy phân vị"),
],
"chuyen_de/cd2/00_cd2_ctu_final_vi.md": [
    ("(Nhóm I→VI)", "(Nhóm I đến VI)"),
    ("+0,260 → +0,426", "+0,260 lên +0,426"),
    ("j = I → VI dummy", "j = I đến VI dummy"),
    ("(~47–49%) → Nhóm IV (~39–46%) → Nhóm V (~50–55%)",
     "(~47–49%), Nhóm IV (~39–46%), Nhóm V (~50–55%)"),
    ("FSTS → ln(LP)", "FSTS" + EN + "ln(LP)"),
    ("Khoảng trống thể chế → trần thấp", "Khoảng trống thể chế dẫn đến trần thấp"),
    ("Nhóm II → III → IV → V → VI", "Nhóm II đến VI"),
    ("Nhóm II → III → IV → V", "Nhóm II đến V"),
    ("tăng cường 2012→2024", "tăng cường 2012 đến 2024"),
    ("nếu p > 0,10 → TCI", "nếu p > 0,10 thì TCI"),
    ("(DAI trực tiếp) → 0 khi", "(DAI trực tiếp) tiến tới 0 khi"),
    ("bác bỏ H₀ → chữ U ngược thực sự", "bác bỏ H₀, kết luận có chữ U ngược thực sự"),
    ("chữ U ngược → bằng chứng xác nhận", "chữ U ngược, đây là bằng chứng xác nhận"),
    ("Biến phụ thuộc → ROS", "Biến phụ thuộc thành ROS"),
    ("Biến độc lập → dummy exporter", "Biến độc lập thành dummy exporter"),
    ("biến ngẫu nhiên → không tìm thấy", "biến ngẫu nhiên, không tìm thấy"),
    ("nhân quả TCI→năng suất và DAI→FSTS", "nhân quả từ TCI đến năng suất và từ DAI đến FSTS"),
    ("DAI dịch chuyển 2009→2023", "DAI dịch chuyển 2009 đến 2023"),
    ("235 cluster → thỏa mãn", "235 cluster, thỏa mãn"),
],
"thesis/chuong_3_phuong_phap_vi.md": [
    ("Identification → Screening → Eligibility → Inclusion", "Identification, Screening, Eligibility, Inclusion"),
    ("(p = 0,545) → không bác bỏ bình đẳng", "(p = 0,545), không bác bỏ bình đẳng"),
    ("α* = 0,017) → H4b", "α* = 0,017), H4b"),
    ("(integer 1–6, Advanced→SIDS)", "(integer 1–6, Advanced đến SIDS)"),
    ("(Advanced Innovation→SIDS)", "(Advanced Innovation đến SIDS)"),
    ("(M2) → 38.342", "(M2), 38.342"),
    ("(M3, thêm kiểm soát) → 29.840", "(M3, thêm kiểm soát), 29.840"),
    ("(tiếng Việt ↔ mã WBES)", "(đối chiếu tiếng Việt và mã WBES)"),
    ("từ 17 → **47 nước**", "từ 17 lên **47 nước**"),
],
"thesis/chuong_4_ket_qua_vi.md": [
    ("tiên tiến—đổi mới tại Singapore", "tiên tiến đổi mới tại Singapore"),
    ("bậc thấp—trung tại Việt Nam", "bậc thấp đến trung tại Việt Nam"),
    ("bậc thấp—trung: Việt Nam (P3)", "bậc thấp đến trung: Việt Nam (P3)"),
    ("gradient ICRV → TP được xác nhận", "gradient ICRV đến TP được xác nhận"),
],
}

def main():
    for path, pairs in REPLACEMENTS.items():
        with open(path, encoding="utf-8") as f:
            text = f.read()
        misses = []
        for old, new in pairs:
            if old not in text:
                misses.append(old)
                continue
            text = text.replace(old, new)
        with open(path, "w", encoding="utf-8") as f:
            f.write(text)
        rem = len(re.findall(r"[→←↔⇒↑↓—]", text))
        print(f"{path}: applied={len(pairs)-len(misses)} missed={len(misses)} remaining_symbols={rem}")
        for m in misses:
            print(f"    MISS: {m!r}")

if __name__ == "__main__":
    main()

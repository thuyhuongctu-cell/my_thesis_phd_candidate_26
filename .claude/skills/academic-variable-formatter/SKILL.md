---
name: academic-variable-formatter
description: >
  Định dạng lại tất cả các biến số trong nghiên cứu khoa học và bài báo (paper) theo tiêu chuẩn học thuật quốc tế (Scopus/WOS). Sử dụng khi viết hoặc chỉnh sửa paper, định dạng biến thống kê, ký hiệu toán học, tham số mô hình, hoặc bất kỳ ký hiệu nào trong nghiên cứu. Áp dụng cho mọi lĩnh vực: STEM, y học, khoa học xã hội. Hỗ trợ định dạng LaTeX, APA style, và các quy ước xuất bản quốc tế. Use this whenever writing scientific papers, formatting statistical variables, mathematical notation, research variables, model parameters, equations, or preparing manuscripts for Scopus-indexed or Web of Science journals. Handles variable notation, statistical symbols, Greek letters, italicization, spacing, and academic formatting conventions.
---

# Academic Variable Formatter

## Tổng Quan (Overview)

Kỹ năng này giúp định dạng chính xác tất cả các biến số, ký hiệu thống kê, và tham số trong nghiên cứu khoa học theo tiêu chuẩn của các tạp chí được index trong Scopus và Web of Science (WOS). Đảm bảo tuân thủ các quy ước quốc tế về ký hiệu toán học, thống kê, và trình bày kết quả nghiên cứu.

This skill ensures all research variables, statistical notation, and parameters follow international academic standards for Scopus/WOS-indexed journals, with proper formatting for LaTeX, APA style, and scholarly conventions.

## Quy Tắc Định Dạng Cốt Lõi (Core Formatting Rules)

### 1. Biến Ngẫu Nhiên và Thống Kê (Random Variables & Statistics)

**Quy ước chữ hoa/thường:**
- Biến ngẫu nhiên: chữ IN HOA, in nghiêng → `$X$, $Y$, $Z$`
- Giá trị cụ thể: chữ thường, in nghiêng → `$x$, $y$, $z$`
- Tham số tổng thể (population): chữ Hy Lạp → `$\mu$, $\sigma$, $\beta$, $\rho$`
- Thống kê mẫu (sample): chữ Latin in nghiêng → `$M$, $SD$, $\bar{x}$, $s$`

**Ví dụ đúng:**
```latex
The random variable $X$ represents income, with observed value $x = 45000$.
Population mean $\mu = 50$ vs. sample mean $M = 48.3$ (or $\bar{x} = 48.3$).
```

### 2. Ký Hiệu Thống Kê Phổ Biến (Common Statistical Notation)

| Khái niệm | Ký hiệu LaTeX | Ví dụ trong văn bản |
|-----------|---------------|---------------------|
| Mean (trung bình) | `$M$` hoặc `$\bar{x}$` | $(M = 19.22, SD = 3.45)$ |
| Standard deviation | `$SD$` hoặc `$s$` | $SD = 2.15$ |
| Correlation | `$r$` | $r(55) = .49, p < .01$ |
| Regression coefficient | `$\beta$` hoặc `$b$` | $\beta = 0.34, t(98) = 3.21$ |
| Probability | `$p$` hoặc `$P$` | $p = .023$ (chính xác), $p < .001$ |
| Chi-square | `$\chi^2$` | $\chi^2(3, N = 120) = 7.89$ |
| t-statistic | `$t$` | $t(45) = 2.67, p = .011$ |
| F-statistic | `$F$` | $F(2, 87) = 4.12, p = .019$ |
| Confidence interval | `95\% CI` | 95% CI [2.47, 2.99] |
| Sample size | `$N$` hoặc `$n$` | $N = 150$ (tổng), $n = 75$ (nhóm) |

### 3. Quy Tắc Định Dạng Số (Number Formatting)

- **Làm tròn:** 2 chữ số thập phân cho hầu hết thống kê, 3-4 cho p-value
- **P-value:** Báo cáo chính xác nếu $p \geq .001$; nếu nhỏ hơn thì `$p < .001$`
- **Số 0 đứng đầu:** Bỏ đi cho giá trị không thể > 1 (correlation, p-value): `.49` chứ không phải `0.49`
- **Phần trăm:** 1 chữ số thập phân, không lặp lại ký hiệu % trong bảng nếu đã có trong tiêu đề

**Ví dụ:**
```latex
The correlation was significant, $r(98) = .67, p < .001$.
Approximately 23.5\% of participants reported symptoms.
```

### 4. Khoảng Cách và Dấu Câu (Spacing & Punctuation)

- **Dấu cách sau dấu phẩy, toán tử:** `$M = 22, SD = 3.4$` ✓ | `$M=22,SD=3.4$` ✗
- **Dấu ngoặc cho degrees of freedom:** `$t(45)$`, `$F(2, 87)$`
- **Dấu ngoặc vuông cho CI:** `95% CI [1.23, 4.56]`
- **Dấu ngoặc tròn cho thống kê mô tả:** `$(M = 19.22, SD = 3.45)$`

### 5. In Nghiêng vs. Không In Nghiêng (Italics Rules)

**IN NGHIÊNG:**
- Tất cả biến số và ký hiệu thống kê: `$M$, $SD$, $r$, $t$, $F$, $p$, $N$`
- Chữ cái đại diện cho biến: `$x$, $y$, $\beta$`
- Subscripts là biến: `$X_i$` (i là index biến)

**KHÔNG in nghiêng:**
- Subscripts là nhãn mô tả: `$M_{\text{control}}$`, `$SD_{\text{pre}}$`
- Tên hàm: `$\sin$, $\cos$, $\log$, $\max$`
- Chữ viết tắt: `CI`, `df`, `SE` (khi không phải ký hiệu toán học)

### 6. LaTeX Code Formatting

**Inline math (trong dòng văn bản):**
```latex
The mean age was $M = 34.2$ years ($SD = 5.7$).
```

**Display equations (phương trình riêng biệt):**
```latex
\begin{equation}
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation}
```

**Aligned equations:**
```latex
\begin{align}
\bar{x} &= \frac{1}{n}\sum_{i=1}^{n} x_i \\
SD &= \sqrt{\frac{1}{n-1}\sum_{i=1}^{n}(x_i - \bar{x})^2}
\end{align}
```

## Quy Trình Xử Lý (Processing Workflow)

### Bước 1: Nhận Diện Biến Số
Quét toàn bộ văn bản và xác định:
- Biến nghiên cứu (research variables)
- Thống kê mô tả (descriptive statistics)
- Kết quả kiểm định (test statistics)
- Tham số mô hình (model parameters)
- Phương trình toán học (equations)

### Bước 2: Áp Dụng Quy Tắc Định Dạng
Theo thứ tự ưu tiên:
1. Chữ hoa/thường đúng (capitalization)
2. In nghiêng phù hợp (italicization)
3. Khoảng cách và dấu câu (spacing/punctuation)
4. Làm tròn số (rounding)
5. Ký hiệu LaTeX chuẩn (proper LaTeX syntax)

### Bước 3: Kiểm Tra Nhất Quán
- Cùng một biến phải có cùng ký hiệu xuyên suốt bài
- Thống kê cùng loại phải format giống nhau
- Kiểm tra subscripts và superscripts
- Đảm bảo tất cả công thức LaTeX compile được

## Ví Dụ Trước/Sau (Before/After Examples)

### Ví dụ 1: Thống kê mô tả
**Trước:**
```
The average age was 34.567 years (standard deviation = 5.234).
```

**Sau:**
```latex
The average age was $M = 34.57$ years ($SD = 5.23$).
```

### Ví dụ 2: Kiểm định correlation
**Trước:**
```
There was a significant correlation (r=0.67, p=0.001234).
```

**Sau:**
```latex
There was a significant correlation, $r(98) = .67, p = .001$.
```

### Ví dụ 3: Regression model
**Trước:**
```
The regression equation was: y = 2.3 + 0.45*x + error
```

**Sau:**
```latex
The regression equation was:
\begin{equation}
y_i = \beta_0 + \beta_1 x_i + \epsilon_i
\end{equation}
where $\beta_0 = 2.30$, $\beta_1 = 0.45$.
```

### Ví dụ 4: ANOVA results
**Trước:**
```
ANOVA showed significant effect (F(2,87)=12.456, p<0.001)
```

**Sau:**
```latex
ANOVA showed a significant effect, $F(2, 87) = 12.46, p < .001$.
```

## Lưu Ý Đặc Biệt Theo Lĩnh Vực

### STEM Fields
- Ưu tiên ký hiệu Hy Lạp cho tham số lý thuyết: `$\alpha$, $\beta$, $\gamma$, $\theta$`
- Ma trận và vector: in đậm `$\mathbf{X}$, $\mathbf{\beta}$`
- Toán tử: `$\nabla$, $\partial$, $\int$, $\sum$, $\prod$`

### Social Sciences (APA Style)
- Ưu tiên `$M$` cho mean thay vì `$\bar{x}$`
- Luôn báo cáo degrees of freedom: `$t(df)$, $F(df1, df2)$`
- Effect sizes: `$d$, $\eta^2$, $\omega^2$`

### Medical/Health Sciences
- Odds ratio: `$OR$`, Relative risk: `$RR$`
- Hazard ratio: `$HR$`
- Confidence intervals bắt buộc: `95% CI [lower, upper]`

## Kiểm Tra Chất Lượng (Quality Checklist)

✓ Tất cả biến số đã được in nghiêng đúng cách
✓ Chữ hoa/thường nhất quán với quy ước (Greek cho population, Latin cho sample)
✓ Khoảng cách sau dấu phẩy và toán tử
✓ P-values được báo cáo chính xác (exact values hoặc < .001)
✓ Degrees of freedom trong ngoặc tròn
✓ Confidence intervals trong ngoặc vuông
✓ Số được làm tròn phù hợp (2 decimal places cho stats, 3-4 cho p)
✓ Bỏ số 0 đứng đầu cho r, p values
✓ Tất cả LaTeX syntax hợp lệ và compile được
✓ Nhất quán trong toàn bộ manuscript

## Tài Liệu Tham Khảo Nhanh (Quick Reference)

### Greek Letters Common in Research
```latex
$\alpha$ (alpha), $\beta$ (beta), $\gamma$ (gamma), $\delta$ (delta)
$\epsilon$ (epsilon), $\theta$ (theta), $\lambda$ (lambda)
$\mu$ (mu), $\sigma$ (sigma), $\rho$ (rho), $\chi$ (chi)
$\omega$ (omega), $\pi$ (pi), $\tau$ (tau), $\phi$ (phi)
```

### Special Symbols
```latex
$\bar{x}$ (x-bar), $\hat{\beta}$ (beta-hat), $x^2$ (squared)
$\sum$ (sum), $\prod$ (product), $\int$ (integral)
$\leq$ (less/equal), $\geq$ (greater/equal), $\neq$ (not equal)
$\pm$ (plus-minus), $\times$ (times), $\approx$ (approximately)
```

---

**Lưu ý:** Khi làm việc với code blocks, tự động wrap tất cả ký hiệu toán học và biến số trong `$...$` (inline) hoặc `$$...$$` / `\begin{equation}...\end{equation}` (display mode) để đảm bảo render đúng trong LaTeX documents.
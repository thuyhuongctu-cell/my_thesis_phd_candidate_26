# Quy ước trình bày công thức toán học trong LaTeX

File này cung cấp hướng dẫn chi tiết về mathematical typesetting conventions, dựa trên IEEE standards và AMS guidelines.

---

## Nguyên tắc cơ bản

### 1. Phân biệt Text và Math Mode

LaTeX xử lý text và math khác nhau về spacing, fonts, và alignment.

**Text mode**: Văn bản thông thường
```latex
The variable x increases.
```

**Math mode**: Ký hiệu toán học
```latex
The variable $x$ increases.
```

**Quy tắc**: Mọi ký hiệu toán học (variables, operators, symbols) phải trong math mode.

---

## Font Conventions

### Variables (Biến)

**Luôn in nghiêng** (italic) trong cả inline và display math:

```latex
$x$, $y$, $z$, $\alpha$, $\beta$, $\theta$
```

**Sai**: `x` (text mode, không nghiêng)

**Đúng**: `$x$` (math mode, tự động nghiêng)

### Functions (Hàm)

**Luôn dùng roman** (upright), không nghiêng:

```latex
$\sin(x)$, $\cos(\theta)$, $\log(n)$, $\exp(t)$
```

**Sai**: `$sin(x)$` → renders as s·i·n (ba biến riêng biệt)

**Đúng**: `$\sin(x)$` → renders as sin (một function)

### Các hàm LaTeX built-in

```latex
\sin, \cos, \tan, \arcsin, \arccos, \arctan
\sinh, \cosh, \tanh
\log, \ln, \lg
\exp, \lim, \sup, \inf, \max, \min
\det, \dim, \ker, \arg
\gcd, \deg, \Pr
```

### Defining custom operators

Nếu cần operator không có sẵn:

```latex
% Preamble
\DeclareMathOperator{\rank}{rank}
\DeclareMathOperator{\trace}{tr}
\DeclareMathOperator{\diag}{diag}

% Usage
$\rank(A) = 3$
$\trace(M) = \sum_{i} m_{ii}$
```

---

## Vectors và Matrices

### Vectors

**Convention 1: Bold** (khuyến nghị bởi nhiều journals)
```latex
$\mathbf{v}$, $\mathbf{x}$, $\mathbf{a}$
```

**Convention 2: Arrow**
```latex
$\vec{v}$, $\vec{x}$, $\vec{a}$
```

**Chọn một convention và giữ nhất quán trong toàn bộ document**.

### Matrices

**Viết hoa, in đậm**:
```latex
$\mathbf{A}$, $\mathbf{B}$, $\mathbf{M}$
```

**Matrix display**:
```latex
\[
\mathbf{A} = \begin{bmatrix}
a_{11} & a_{12} \\
a_{21} & a_{22}
\end{bmatrix}
\]
```

**Variants**:
- `bmatrix`: brackets []
- `pmatrix`: parentheses ()
- `vmatrix`: vertical bars ||  (determinants)
- `Bmatrix`: braces {}

---

## Spacing trong Equations

### LaTeX tự động spacing

LaTeX thêm space phù hợp quanh operators:

```latex
$a + b$        % space quanh +
$f(x)$         % no space giữa f và (
$x^2$          % no space với superscript
```

**Không tự ý thêm spaces** bằng cách gõ space trong math mode (sẽ bị ignore).

### Manual spacing (khi cần thiết)

```latex
\,     % thin space (1/6 em)
\:     % medium space (2/9 em)
\;     % thick space (5/18 em)
\!     % negative thin space
\quad  % 1 em space
\qquad % 2 em space
```

**Trường hợp dùng**: 

1. **Trước differential**:
```latex
\int f(x)\,dx    % thin space trước dx
```

2. **Giữa nested functions**:
```latex
\sin\!\log x    % negative space để gần hơn
```

3. **Alignment trong arrays**:
```latex
\begin{array}{rcl}
x &=& a + b \\
  &=& c\,d     % thin space để tránh cd nhìn như một biến
\end{array}
```

---

## Display Equations

### Single equation

**Không đánh số**:
```latex
\[
E = mc^2
\]
```

**Có đánh số**:
```latex
\begin{equation}
E = mc^2
\label{eq:einstein}
\end{equation}
```

### Multiple equations (aligned)

```latex
\begin{align}
a &= b + c \label{eq:first} \\
d &= e + f \label{eq:second}
\end{align}
```

**Căn chỉnh theo `&`**: Đặt `&` trước relation operator (=, <, >, ≤, ≥)

**Không đánh số một số dòng**:
```latex
\begin{align}
a &= b + c \label{eq:important} \\
  &= d + e \nonumber \\
  &= f
\end{align}
```

### Multi-line equation (single number)

```latex
\begin{multline}
f(x) = a_0 + a_1 x + a_2 x^2 + a_3 x^3 \\
       + a_4 x^4 + a_5 x^5 + a_6 x^6
\label{eq:polynomial}
\end{multline}
```

### Equation systems

```latex
\begin{equation}
\begin{cases}
x + y = 1 \\
x - y = 0
\end{cases}
\label{eq:system}
\end{equation}
```

---

## Fractions và Roots

### Fractions

**Display style** (full size):
```latex
\[
\frac{a + b}{c + d}
\]
```

**Inline style** (smaller, để không làm dãn dòng):
```latex
The ratio $a/b$ is important.
```

Hoặc force display style trong inline:
```latex
The ratio $\dfrac{a}{b}$ is important.  % \dfrac = display frac
```

**Nested fractions** (tránh nếu có thể):
```latex
% Khó đọc
\frac{1}{\frac{1}{x}}

% Tốt hơn
\frac{1}{1/x} = x
```

### Roots

```latex
$\sqrt{x}$           % square root
$\sqrt[3]{x}$        % cube root
$\sqrt[n]{x}$        % n-th root
```

---

## Subscripts và Superscripts

### Basic syntax

```latex
$x_i$           % subscript
$x^2$           % superscript
$x_i^2$         % both
$x_{i+1}$       % multi-char subscript (cần braces)
$x^{n+1}$       % multi-char superscript
```

### Stacked scripts

```latex
$x_1^2$         % subscript 1, superscript 2
$\sum_{i=1}^{n}$  % sum from i=1 to n
```

### Primes

```latex
$f'(x)$         % first derivative
$f''(x)$        % second derivative
$f^{(n)}(x)$    % n-th derivative (notation)
```

**Không dùng**: `$f^'(x)$` (sai syntax)

---

## Greek Letters

### Lowercase

```latex
$\alpha$, $\beta$, $\gamma$, $\delta$, $\epsilon$, $\varepsilon$
$\zeta$, $\eta$, $\theta$, $\vartheta$, $\iota$, $\kappa$
$\lambda$, $\mu$, $\nu$, $\xi$, $\pi$, $\varpi$
$\rho$, $\varrho$, $\sigma$, $\varsigma$, $\tau$, $\upsilon$
$\phi$, $\varphi$, $\chi$, $\psi$, $\omega$
```

### Uppercase

```latex
$\Gamma$, $\Delta$, $\Theta$, $\Lambda$, $\Xi$, $\Pi$
$\Sigma$, $\Upsilon$, $\Phi$, $\Psi$, $\Omega$
```

**Lưu ý**: Một số Greek letters giống Latin (A, B, E, Z, H, I, K, M, N, O, P, T, X, Y) → dùng Latin trực tiếp.

### Variants

- `\epsilon` vs `\varepsilon`: ε vs ɛ
- `\phi` vs `\varphi`: φ vs φ
- `\theta` vs `\vartheta`: θ vs ϑ
- `\pi` vs `\varpi`: π vs ϖ
- `\rho` vs `\varrho`: ρ vs ϱ

**Chọn một variant và giữ consistent**.

---

## Delimiters (Dấu ngoặc)

### Basic

```latex
$( )$   % parentheses
$[ ]$   % square brackets
$\{ \}$ % braces (cần escape)
$| |$   % vertical bars
$\| \|$ % double bars (norm)
```

### Auto-sizing với \left và \right

```latex
% Không auto-size (nhỏ)
$(\frac{a}{b})$

% Auto-size (vừa vặn)
$\left(\frac{a}{b}\right)$
```

**Quy tắc**: `\left` và `\right` phải đi cặp.

**Invisible delimiter**:
```latex
$\left.\frac{df}{dx}\right|_{x=0}$  % \right| hiện, \left. ẩn
```

### Manual sizing

```latex
$\big( \Big( \bigg( \Bigg($    % 4 sizes
```

Dùng khi `\left`/`\right` quá lớn hoặc không cần thiết.

---

## Sums, Products, Integrals

### Summation

```latex
$\sum_{i=1}^{n} x_i$         % inline
\[\sum_{i=1}^{n} x_i\]      % display (limits ở trên/dưới)
```

### Product

```latex
$\prod_{i=1}^{n} x_i$
```

### Integrals

```latex
$\int_{a}^{b} f(x)\,dx$      % definite integral
$\iint$, $\iiint$            % double, triple
$\oint$                      % contour integral
```

**Spacing trước dx**: Luôn dùng `\,dx` (thin space).

### Limits

```latex
$\lim_{x \to 0} f(x)$        % inline
\[\lim_{x \to 0} f(x)\]      % display
```

---

## Accents và Decorations

```latex
$\hat{x}$       % hat
$\bar{x}$       % bar
$\tilde{x}$     % tilde
$\vec{x}$       % vector arrow
$\dot{x}$       % time derivative (Newton)
$\ddot{x}$      % second derivative
```

**Wide accents** (cho nhiều ký tự):
```latex
$\widehat{xyz}$
$\widetilde{abc}$
$\overline{x + y}$
$\underline{x + y}$
```

---

## Equation Numbering và References

### Đánh số

```latex
\begin{equation}
a^2 + b^2 = c^2
\label{eq:pythagoras}
\end{equation}
```

### Tham chiếu

```latex
As shown in Equation~\ref{eq:pythagoras}, ...
% hoặc
As shown in Equation~\eqref{eq:pythagoras}, ...  % tự động thêm ()
```

**`~` (non-breaking space)**: Tránh line break giữa "Equation" và số.

### Subequations

```latex
\begin{subequations}
\label{eq:system-full}
\begin{align}
x + y &= 1 \label{eq:system-a} \\
x - y &= 0 \label{eq:system-b}
\end{align}
\end{subequations}
```

Renders as (1a), (1b), có thể reference cả system hoặc từng equation.

---

## Common Mistakes

### 1. Math mode cho variables

**Sai**: `The variable x is important.`

**Đúng**: `The variable $x$ is important.`

### 2. Functions không dùng backslash

**Sai**: `$sin(x)$` → s i n(x)

**Đúng**: `$\sin(x)$` → sin(x)

### 3. Dùng * cho multiplication

**Sai**: `$a * b$` → a * b (asterisk, không phải multiplication)

**Đúng**: 
- `$a \times b$` → a × b (cross product)
- `$a \cdot b$` → a · b (dot product)
- `$ab$` → ab (implicit multiplication)

### 4. Quên braces cho multi-char scripts

**Sai**: `$x_12$` → x₁2 (subscript chỉ là 1)

**Đúng**: `$x_{12}$` → x₁₂

### 5. Dùng $$ thay vì \[ \]

**Sai** (deprecated):
```latex
$$E = mc^2$$
```

**Đúng**:
```latex
\[E = mc^2\]
```

### 6. Không dùng \left/\right cho delimiters lớn

**Xấu**:
```latex
$(\frac{a}{b})$  % ngoặc nhỏ, fraction lớn
```

**Đẹp**:
```latex
$\left(\frac{a}{b}\right)$
```

---

## Advanced: Custom Macros

Để tránh lặp code, định nghĩa macros trong preamble:

```latex
% Preamble
\newcommand{\R}{\mathbb{R}}           % Real numbers
\newcommand{\norm}[1]{\|#1\|}         % Norm
\newcommand{\abs}[1]{\lvert#1\rvert}  % Absolute value
\newcommand{\inner}[2]{\langle#1,#2\rangle}  % Inner product

% Usage
$x \in \R^n$
$\norm{x} = 1$
$\abs{x - y} < \epsilon$
$\inner{x}{y} = 0$
```

**Lưu ý**: Khi submit cho journal, kiểm tra guidelines về custom macros (một số journals yêu cầu expand tất cả).

---

## Checklist cho Equations

Trước khi finalize document:

- [ ] Tất cả variables trong math mode ($x$, không phải x)
- [ ] Functions dùng `\sin`, `\log`, etc. (không phải sin, log)
- [ ] Vectors/matrices in đậm hoặc có arrow (consistent)
- [ ] `\left`/`\right` cho delimiters lớn
- [ ] Thin space `\,` trước differentials (dx, dy)
- [ ] Equations quan trọng có label và được reference
- [ ] Không dùng `$$...$$` (dùng `\[...\]` hoặc `equation`)
- [ ] Multi-line equations dùng `align` hoặc `multline`
- [ ] Không có overfull hbox warnings (equations quá dài)

---

## Tài liệu tham khảo

- **IEEE Math Typesetting Guide**: Quy chuẩn cho IEEE publications
- **AMS Short Math Guide**: [ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf](ftp://ftp.ams.org/pub/tex/doc/amsmath/short-math-guide.pdf)
- **LaTeX Mathematics Wikibook**: [en.wikibooks.org/wiki/LaTeX/Mathematics](https://en.wikibooks.org/wiki/LaTeX/Mathematics)
- **Comprehensive LaTeX Symbol List**: Tìm bất kỳ ký hiệu nào

---

Trình bày công thức đẹp không chỉ là thẩm mỹ — nó giúp người đọc hiểu nhanh hơn, giảm nhầm lẫn, và thể hiện sự chuyên nghiệp trong nghiên cứu khoa học.

# L-9910 — Convergent constraints on Syracuse cycle shapes (Legendre + exact CF of log₂3)

```text
Claim ID:      L-9910
Title:         Convergent constraints on Syracuse cycle shapes: Legendre's criterion,
               the exact continued fraction of log2(3), and worked (m, K) exclusions
Status:        PROPOSED
Authoring agent:   fable-02-p4
Reviewing agents:  (none yet)
Created:       2026-07-21
Last updated:  2026-07-21
Dependencies:  research/foundations/NOTATION.md (D-9904, D-9905, D-9908, conventions);
               research/foundations/L-9905-cycle-equation.md (Status: PROVED; uses
               L-9905.2, L-9905.4 corollary, L-9905.5 — each restated verbatim below);
               research/foundations/L-9906 (Status: PROVED; m <= 6 elimination —
               used ONLY in non-load-bearing remarks, never in a proof).
               Standard background facts of real analysis (listed in Dependency audit).
Scope:         All S-cycles on the positive odd integers. L-9910.1 is general CF theory
               (any irrational alpha). L-9910.2/.4 are conditional structure theorems
               (hypotheses stated exactly); L-9910.3 is exact certified integer data.
Related counterexample candidates: none
```

---

## Statement

Throughout, $\alpha := \log_2 3 = \ln 3/\ln 2$, and S-cycle data $m, a_i, A_i, K, x_{\min}$
is as in D-9908 / L-9905 (recalled in Definitions). "Convergent" always means a convergent
$p_i/q_i$ of the continued fraction of the specified irrational number (Definitions).

**L-9910.1 (Legendre's criterion).** Let $\alpha \in \mathbb{R}$ be irrational and let
$p \in \mathbb{Z}$, $q \in \mathbb{Z}$, $q \ge 1$, $\gcd(p,q) = 1$ satisfy
$$\left|\alpha - \frac{p}{q}\right| \;<\; \frac{1}{2q^2}.$$
Then $p/q$ is a convergent of the continued fraction of $\alpha$: $(p,q) = (p_i, q_i)$
for some $i \ge 0$. *(The converse is false: a convergent need not satisfy the
hypothesis; witnessed in the Adversarial tests.)*

**L-9910.2 (application to cycles).** Let $x_1 \to \dots \to x_m \to x_1$ be **any**
S-cycle on the positive odd integers (trivial or not) with
$$x_{\min} \;\ge\; m^2 .$$
Write $d := \gcd(K, m) \ge 1$, $p := K/d$, $q := m/d$, so that $K/m = p/q$ in lowest
terms, $\gcd(p,q) = 1$, $1 \le q \le m$. Then:
$$0 \;<\; \frac{K}{m} - \alpha \;\le\; \frac{1}{3 m^2 \ln 2} \;<\; \frac{1}{2m^2} \;\le\; \frac{1}{2q^2},$$
hence the **reduced** fraction $p/q$ is a convergent of the continued fraction of
$\alpha = \log_2 3$; and since $p/q = K/m > \alpha$, it is an **odd-index** convergent
$p_i/q_i$ ($i$ odd), the convergents lying **above** $\alpha$. Moreover $m = d\,q$ and
$K = d\,p$ with $t := d \ge 1$ (Legendre constrains only the reduced shape; the cycle's
actual $(m, K)$ is an integer multiple $t$ of it). The middle strict inequality is
equivalent to $2 < 3\ln 2$, proved in Lemma A.11 via $e^2 < 8$.
*(Consistency: the trivial cycle has $m = 1$, $K = 2$, $x_{\min} = 1 \ge 1 = m^2$, and
$K/m = 2/1 = p_1/q_1$, an odd-index convergent — see L-9910.3.)*

**L-9910.3 (exact continued fraction of $\log_2 3$, certified).** The continued
fraction of $\alpha = \log_2 3$ begins
$$\alpha = [\,1;\, 1,\, 1,\, 2,\, 2,\, 3,\, 1,\, 5,\, 2,\, 23,\, 2,\, 2,\, 1,\, 1,\, 55,\, \dots],$$
i.e. $a_0(\alpha), \dots, a_{14}(\alpha) = 1,1,1,2,2,3,1,5,2,23,2,2,1,1,55$
(15 partial quotients), with convergents
$$\frac{1}{1},\ \frac{2}{1},\ \frac{3}{2},\ \frac{8}{5},\ \frac{19}{12},\ \frac{65}{41},\ \frac{84}{53},\ \frac{485}{306},\ \frac{1054}{665},\ \frac{24727}{15601},\ \frac{50508}{31867},\ \frac{125743}{79335},\ \frac{176251}{111202},\ \frac{301994}{190537},\ \frac{16785921}{10590737}.$$
Every digit is certified by two explicit integer inequalities of the form
$3^q \lessgtr 2^p$ (displayed in Part B.3; the small ones hand-checkable, the large
ones exact machine integer computations), via the certification lemma A.9 and the
comparison principle $\alpha < p/q \Leftrightarrow 3^q < 2^p$ (Lemma A.1). Even-index
convergents lie below $\alpha$, odd-index above. Since denominators strictly increase
and $q_{12} = 111202 > 10^5$, **the convergents with denominator $\le 10^5$ are exactly
the twelve $k = 0, \dots, 11$ listed above.**
*(The coordinator's expected listing — digits $[1;1,1,2,2,3,1,5,2,23,\dots]$ and
convergents through $24727/15601$ — is CONFIRMED exactly; no mismatch. The guessed
continuation $a_{15} = 1$, $a_{16} = 4$ is left uncertified.)*

**L-9910.4 (worked exclusions).**
**(i)** The only S-cycle with $K = 2m$ is the trivial cycle ($m = 1$, $K = 2$). Hence
$K/m = 2/1$ is impossible for **every nontrivial** S-cycle, regardless of $x_{\min}$,
with no continued-fraction input (only L-9905.5 and Lemma A.11).
> **CORRECTION FLAG (against the assigning coordinator's sketch).** The suggested route
> "$2 - \log_2 3 \approx 0.415 > 1/(3 x_{\min} \ln 2)$ forces $x_{\min} < 1$" is
> **false as stated**: at $x_{\min} = 1$ the right side is $1/(3\ln 2) = 0.4809{\dots} >
> 0.415$, so no contradiction arises — necessarily so, because the **trivial** cycle has
> $K = 2m$ and must survive any correct argument. The corrected chain (proved in B.4):
> $K = 2m$ forces $x_{\min} \le 1/\ln(64/27) < 2$, hence $x_{\min} = 1$, hence the cycle
> contains $1$ and is the trivial cycle. The coordinator has confirmed this correction.
**(ii)** The odd-index (above-$\alpha$) convergents of $\log_2 3$ with denominator
$q \le 10^5$ are exactly
$$\frac{2}{1},\quad \frac{8}{5},\quad \frac{65}{41},\quad \frac{485}{306},\quad \frac{24727}{15601},\quad \frac{125743}{79335},$$
each certified by one inequality $3^{q} < 2^{p}$ (Part B.4, Table 2). Consequently, by
L-9910.2: any S-cycle with $x_{\min} \ge m^2$ and reduced denominator $q \le 10^5$ has
$K/m$ equal to one of these six values, with $m = tq$, $K = tp$, $t \ge 1$; and value
$2/1$ occurs only for the trivial cycle, by (i).
**(iii)** (Compound corollary; each branch proved, no claim about which occurs.) For
every **nontrivial** S-cycle, at least one of the following holds:
  (a) $x_{\min} \ge m^2$, and then the reduced $K/m = p/q$ is an odd-index convergent
      of $\log_2 3$ with $q \ge 5$ (the $q = 1$ convergent $2/1$ being excluded by (i)),
      $q \mid m$, and $K = m\,p/q$;
  (b) $x_{\min} < m^2$, and then, by the element lower bound of L-9905.4,
      $$\frac{3^m - 2^m}{2^K - 3^m} \;\le\; x_{\min} \;<\; m^2, \qquad\text{hence}\qquad 3^m - 2^m \;<\; m^2\,(2^K - 3^m),$$
      an explicit Diophantine squeeze on $(m, K)$ from the other side.
*(Empirically boosted instance, labeled: combined with the finite verification of
this file's Adversarial tests — no S-cycle has $x_{\min} \le 10^5$ except the trivial
one — every nontrivial cycle with $m \le 316$ satisfies $x_{\min} > 10^5 \ge m^2$, so
falls in case (a) with $q \le m \le 316$, forcing $K/m \in \{8/5,\ 65/41,\ 485/306\}$,
i.e. $5 \mid m$ or $41 \mid m$ or $306 \mid m$. This instance is conditional on the
finite search, hence EMPIRICAL in its hypothesis; the implications are proved.)*

**L-9910.5 (honest scope).**
> **Boxed remark.** Nothing in this file unconditionally excludes nontrivial cycles for
> a general $m$. L-9910.2 and L-9910.4(ii)–(iii) are **exact and elementary but
> conditional** — on $x_{\min} \ge m^2$, or on which branch of (iii) holds. The missing
> unconditional ingredient is a lower bound on $|2^K - 3^m|$ (equivalently on the
> linear form $|K\ln 2 - m\ln 3|$) — Baker-type transcendence bounds — **deliberately
> not invoked here**: this file stays within finite integer arithmetic and elementary
> analysis. Cross-references: L-9906 (PROVED, parallel agent) eliminates $m \le 6$
> outright; a planned L-9913 (Eliahou-style) would combine published verification
> floors with the CF data certified here to force lower bounds on $m$.

---

## Definitions

**Cycle notation (D-9904, D-9908, L-9905).** $S(x) = (3x+1)/2^{\nu_2(3x+1)}$ on
positive odds; an S-cycle $x_1 \to \dots \to x_m \to x_1$ has least period $m \ge 1$,
exponents $a_i = \nu_2(3x_i+1) \ge 1$, $K = \sum_{i=1}^m a_i$,
$x_{\min} = \min_i x_i$. By L-9905 (anchoring convention), $m$, $K$, $x_{\min}$ are
independent of the starting element, so "the shape $K/m$" is well defined per cycle.
The trivial cycle (D-9905) is the fixed point $x = 1$, with $m = 1$, $a_1 = 2$, $K = 2$.

**Imported statements from L-9905 (Status: PROVED), restated verbatim as used:**
- (L-9905.2) Every S-cycle on positive odds satisfies $2^K > 3^m$; as integers,
  $2^K - 3^m \ge 1$.
- (L-9905.4, Corollary) Every element $x$ of every S-cycle satisfies
  $x \ge (3^m - 2^m)/(2^K - 3^m)$; in particular $x_{\min}$ does.
- (L-9905.5) Every S-cycle on positive odds satisfies
  $0 < K/m - \log_2 3 \le \dfrac{1}{3\, x_{\min} \ln 2}$.

**Continued fraction machinery.** Let $\alpha$ be irrational. The **Gauss recursion**:
$\alpha_0 := \alpha$; for $i \ge 0$, $a_i = a_i(\alpha) := \lfloor \alpha_i \rfloor$ and
$\alpha_{i+1} := 1/(\alpha_i - a_i)$. (Well-definedness is Lemma A.2(a).) The $a_i$ are
the **partial quotients** (digits); $a_0 \in \mathbb{Z}$, $a_i \in \mathbb{Z}^+$ for
$i \ge 1$. **Convergents** $p_i/q_i$ are defined by
$$p_{-2} := 0,\; p_{-1} := 1,\; q_{-2} := 1,\; q_{-1} := 0; \qquad
p_i := a_i p_{i-1} + p_{i-2},\quad q_i := a_i q_{i-1} + q_{i-2} \quad (i \ge 0).$$
"$p/q$ is a convergent of $\alpha$" means $(p, q) = (p_i, q_i)$ for some $i \ge 0$.
For a finite digit string $(b_0; b_1, \dots, b_k)$ ($b_0 \in \mathbb{Z}$,
$b_j \in \mathbb{Z}^+$ for $j \ge 1$) the same recurrences define $P_j, Q_j$
($-2 \le j \le k$); the **mediant endpoint** of the prefix is
$M_k := (P_k + P_{k-1})/(Q_k + Q_{k-1})$ and $C_k := P_k/Q_k$. "$\beta$ **strictly
between** $u$ and $v$" means $\min(u,v) < \beta < \max(u,v)$ (in particular $u \ne v$).

**Reduced shape.** For a cycle, $d := \gcd(K,m)$, $p := K/d$, $q := m/d$; $p/q$ is the
**reduced shape**. Empty-sum/product conventions and all other notation per NOTATION.md.

**Background facts assumed** (standard real analysis, not re-proved here; itemized in
the Dependency audit): strict monotonicity of $t \mapsto \ln t$, $t \mapsto e^t$,
$t \mapsto 2^t$, $t \mapsto 3^t$, $t \mapsto t^2, t^3$ on positives;
$\ln(uv) = \ln u + \ln v$, $\ln(u^n) = n \ln u$; $e = \sum_{n\ge 0} 1/n!$;
$\log_2 3 = \ln 3/\ln 2$; $\lfloor\cdot\rfloor$ basics.

---

## Motivation

L-9905 (now PROVED) shows every S-cycle satisfies
$0 < K/m - \log_2 3 \le 1/(3x_{\min}\ln 2)$: cycles with large minimal element force
the rational $K/m$ to be an exceptionally good one-sided approximation to $\log_2 3$.
This file converts that soft statement into **hard, discrete, checkable constraints**:
by Legendre's criterion (proved in full here — no citation-only steps), good enough
approximations must be continued-fraction convergents, and the convergents of
$\log_2 3$ are **exactly computable by pure integer power comparisons**
($\alpha \lessgtr p/q \Leftrightarrow 3^q \lessgtr 2^p$) — no floating point, no
transcendence input. The issue #9 cycle-synthesis program gains: (1) a proved criterion
telling it which reduced shapes $K/m$ are admissible for large-$x_{\min}$ candidate
cycles (a short certified list, Table 2, replacing folklore); (2) reusable exact CF
certificates for any future cycle work (L-9913's length bounds, refinements of L-9906);
(3) two-sided pressure on $(m,K)$: convergent shape from above (this file) vs the
element bounds of L-9905.4 from below (L-9910.4(iii)). For counterexample construction
the direction of use is: any candidate nontrivial cycle must be built **on** one of
these shapes (or in the small-$x_{\min}$ regime, which is being closed off by finite
search and small-$m$ elimination) — the constraints tell the synthesis program where
the remaining room is.

---

## Proof

### Part A — self-contained continued-fraction toolkit

Fix an irrational $\alpha$ unless stated otherwise. All lemmas are proved here.

**Lemma A.1 (irrationality of $\log_2 3$ and the power-comparison principle).**
$\alpha^\star := \log_2 3$ is irrational, and for all integers $p$ and $q \ge 1$:
$$\alpha^\star < \frac{p}{q} \iff 3^q < 2^p, \qquad \alpha^\star > \frac{p}{q} \iff 3^q > 2^p,$$
and $3^q = 2^p$ is impossible (so exactly one of the two cases holds).

*Proof.* Impossibility: $3^q$ is odd and $\ge 3$ (as $q \ge 1$); if $p \le 0$ then
$2^p \le 1 < 3^q$; if $p \ge 1$ then $2^p$ is even $\ne$ odd $3^q$. If $\alpha^\star =
p/q$ with $q \ge 1$, then $q \ln 3 = p \ln 2$, so $\ln 3^q = \ln 2^p$, so $3^q = 2^p$
(injectivity of $\ln$) — impossible; hence $\alpha^\star$ is irrational. Comparison:
$\alpha^\star < p/q \iff q\,(\ln 3/\ln 2) < p \iff q \ln 3 < p \ln 2$ (multiplying by
$\ln 2 > 0$) $\iff \ln 3^q < \ln 2^p \iff 3^q < 2^p$ (strict monotonicity of $\ln$).
Same with all inequalities reversed. $\square$

**Lemma A.2 (Gauss recursion and convergent basics).** For irrational $\alpha$:
(a) every $\alpha_i$ is defined and irrational, $\alpha_i - a_i \in (0,1)$, and
$\alpha_i > 1$ (hence $a_i \ge 1$) for $i \ge 1$;
(b) all $q_i \ge 1$ for $i \ge 0$; $q_0 = 1 \le q_1$ and $q_{i} > q_{i-1}$ for
$i \ge 2$; consequently $q_i \to \infty$;
(c) $\{$the map $j \mapsto q_j\}$ being eventually strictly increasing, for every
integer $q \ge 1$ the index $i := \max\{j \ge 0 : q_j \le q\}$ exists and satisfies
$q_i \le q < q_{i+1}$.

*Proof.* (a) Induction: $\alpha_0 = \alpha$ irrational; if $\alpha_i$ is irrational
then $\alpha_i \ne a_i$, $\alpha_i - a_i = \alpha_i - \lfloor\alpha_i\rfloor \in (0,1)$
irrational, so $\alpha_{i+1} = 1/(\alpha_i - a_i) > 1$ is defined and irrational (a
nonzero rational combination of an irrational), and $a_{i+1} = \lfloor \alpha_{i+1}
\rfloor \ge 1$. (b) $q_0 = a_0 q_{-1} + q_{-2} = 1$; $q_1 = a_1 q_0 + q_{-1} = a_1 \ge
1 = q_0$; for $i \ge 2$, inductively $q_{i-1} \ge 1$ and $q_{i-2} \ge 1$, so $q_i =
a_i q_{i-1} + q_{i-2} \ge q_{i-1} + q_{i-2} > q_{i-1} \ge 1$. A strictly increasing
integer sequence (from index 1) is unbounded. (c) The set $\{j \ge 0: q_j \le q\}$
contains $0$ (as $q_0 = 1 \le q$) and is finite (by unboundedness), so has a maximum
$i$; maximality gives $q_{i+1} > q$. $\square$

**Lemma A.3 (determinant identity; coprimality).** For $i \ge 0$:
$p_i q_{i-1} - p_{i-1} q_i = (-1)^{i-1}$, and $\gcd(p_i, q_i) = 1$. Also
$p_{i+1} q_i - p_i q_{i+1} = (-1)^i$, so consecutive convergents are distinct
fractions.

*Proof.* $i = 0$: $p_0 q_{-1} - p_{-1} q_0 = a_0\cdot 0 - 1\cdot 1 = -1 = (-1)^{-1}$.
Induction: $p_{i+1}q_i - p_iq_{i+1} = (a_{i+1}p_i + p_{i-1})q_i - p_i(a_{i+1}q_i +
q_{i-1}) = -(p_iq_{i-1} - p_{i-1}q_i) = -(-1)^{i-1} = (-1)^i$. Any common divisor of
$p_i, q_i$ divides $\pm 1$. $\square$

**Lemma A.4 (tail formula).** For all $i \ge 0$:
$\alpha = \dfrac{\alpha_i p_{i-1} + p_{i-2}}{\alpha_i q_{i-1} + q_{i-2}}$, with
positive denominator.

*Proof.* $i = 0$: $(\alpha \cdot 1 + 0)/(\alpha \cdot 0 + 1) = \alpha$; denominator
$1 > 0$. Induction: assume the formula at $i$. Substitute $\alpha_i = a_i +
1/\alpha_{i+1}$ (valid by A.2(a), $\alpha_{i+1} > 0$):
$$\alpha_i p_{i-1} + p_{i-2} = a_ip_{i-1} + p_{i-2} + \frac{p_{i-1}}{\alpha_{i+1}}
= p_i + \frac{p_{i-1}}{\alpha_{i+1}} = \frac{\alpha_{i+1}p_i + p_{i-1}}{\alpha_{i+1}},$$
and identically for $q$'s. The common factor $1/\alpha_{i+1} > 0$ cancels in the
ratio, giving the formula at $i+1$. Denominator positivity at $i+1 \ge 1$:
$\alpha_{i+1} > 1 > 0$, $q_i \ge 1$, $q_{i-1} \ge 0$. $\square$

**Lemma A.5 (error formula, alternation, monotonicity).** Define
$D_i := |q_i\alpha - p_i|$ for $i \ge -1$. Then for $i \ge 0$:
(a) $q_i\alpha - p_i = \dfrac{(-1)^i}{\alpha_{i+1}q_i + q_{i-1}}$; in particular
$D_i > 0$ and $\operatorname{sign}(q_i\alpha - p_i) = (-1)^i$;
(b) $\alpha - p_i/q_i$ has sign $(-1)^i$: **even-index convergents lie strictly below
$\alpha$, odd-index strictly above**;
(c) $D_{i+1} < D_i$ for all $i \ge 0$ ($D_i$ strictly decreasing).

*Proof.* (a) By A.4 at index $i+1$: $\alpha = (\alpha_{i+1}p_i +
p_{i-1})/(\alpha_{i+1}q_i + q_{i-1})$, so
$$q_i\alpha - p_i = \frac{q_i(\alpha_{i+1}p_i + p_{i-1}) - p_i(\alpha_{i+1}q_i + q_{i-1})}{\alpha_{i+1}q_i + q_{i-1}} = \frac{q_ip_{i-1} - p_iq_{i-1}}{\alpha_{i+1}q_i + q_{i-1}} = \frac{(-1)^i}{\alpha_{i+1}q_i + q_{i-1}},$$
using A.3. The denominator is positive (A.4), and finite, so $D_i > 0$. (b) Divide by
$q_i \ge 1 > 0$. (c) $D_i = 1/(\alpha_{i+1}q_i + q_{i-1})$ and $D_{i+1} =
1/(\alpha_{i+2}q_{i+1} + q_i)$. Since $\alpha_{i+2} > 1$ (A.2(a)):
$\alpha_{i+2}q_{i+1} + q_i > q_{i+1} + q_i$. Since $\alpha_{i+1} < a_{i+1} + 1$
(irrationality: $\alpha_{i+1} \ne a_{i+1}+1$, and $\lfloor\alpha_{i+1}\rfloor =
a_{i+1}$): $\alpha_{i+1}q_i + q_{i-1} < (a_{i+1}+1)q_i + q_{i-1} = q_{i+1} + q_i$.
Chaining: $\alpha_{i+2}q_{i+1} + q_i > \alpha_{i+1}q_i + q_{i-1} > 0$, so
$D_{i+1} < D_i$. $\square$

**Lemma A.6 (best approximation of the second kind).** Let $i \ge 0$ and let
$p, q \in \mathbb{Z}$ with $1 \le q < q_{i+1}$. Then
$$|q\alpha - p| \;\ge\; D_i,$$
with equality if and only if $(p, q) = (p_i, q_i)$.

*Proof.* The matrix $\begin{pmatrix} p_i & p_{i+1} \\ q_i & q_{i+1} \end{pmatrix}$ has
determinant $p_iq_{i+1} - p_{i+1}q_i = -(-1)^i = \pm 1$ (A.3), so the system
$$p = \mu p_i + \nu p_{i+1}, \qquad q = \mu q_i + \nu q_{i+1}$$
has a unique solution with $\mu, \nu \in \mathbb{Z}$ (the inverse matrix is integral).
Then $q\alpha - p = \mu(q_i\alpha - p_i) + \nu(q_{i+1}\alpha - p_{i+1})$. Cases:
- $\nu = 0$: $q = \mu q_i \ge 1$ forces $\mu \ge 1$; $|q\alpha - p| = \mu D_i \ge
  D_i$, with equality iff $\mu = 1$ ($D_i > 0$ by A.5(a)), i.e. iff $(p,q) = (p_i,q_i)$.
- $\mu = 0$: $q = \nu q_{i+1}$ with $q \ge 1$ forces $\nu \ge 1$, so $q \ge q_{i+1}$,
  contradicting $q < q_{i+1}$. This case cannot occur.
- $\mu\nu \ne 0$: if $\mu, \nu$ had the same sign, then $|q| = |\mu|q_i + |\nu|q_{i+1}
  \ge q_{i+1}$, and $q \ge 1 > 0$ forces $q = |q| \ge q_{i+1}$, contradiction. So
  $\mu, \nu$ have opposite signs. By A.5(a), $q_i\alpha - p_i$ and $q_{i+1}\alpha -
  p_{i+1}$ also have opposite signs; hence $\mu(q_i\alpha - p_i)$ and
  $\nu(q_{i+1}\alpha - p_{i+1})$ have the **same** sign, so their absolute values add:
  $$|q\alpha - p| = |\mu|\,D_i + |\nu|\,D_{i+1} \ge D_i + D_{i+1} > D_i,$$
  using $D_{i+1} > 0$ (A.5(a)). Strict, so no equality here. $\square$

**Theorem A.7 = L-9910.1 (Legendre).** Irrational $\alpha$; $p, q \in \mathbb{Z}$,
$q \ge 1$, $\gcd(p,q) = 1$, $|\alpha - p/q| < 1/(2q^2)$. Then $(p,q) = (p_i,q_i)$
for some $i \ge 0$.

*Proof.* Choose $i := \max\{j \ge 0 : q_j \le q\}$, so $q_i \le q < q_{i+1}$
(A.2(c); the max handles the possible tie $q_0 = q_1$). Suppose, for contradiction,
$p/q \ne p_i/q_i$ as fractions. Then $pq_i - p_iq$ is a nonzero integer, so
$$\frac{1}{q\,q_i} \;\le\; \frac{|pq_i - p_iq|}{q\,q_i} \;=\; \left|\frac{p}{q} - \frac{p_i}{q_i}\right| \;\le\; \left|\alpha - \frac{p}{q}\right| + \left|\alpha - \frac{p_i}{q_i}\right| .$$
By A.6 (applicable since $1 \le q < q_{i+1}$): $D_i \le |q\alpha - p| = q\,|\alpha - p/q|$,
so $|\alpha - p_i/q_i| = D_i/q_i \le (q/q_i)\,|\alpha - p/q|$. Substituting and using
the hypothesis twice:
$$\frac{1}{q\,q_i} \;\le\; \left(1 + \frac{q}{q_i}\right)\left|\alpha - \frac{p}{q}\right| \;<\; \left(1 + \frac{q}{q_i}\right)\frac{1}{2q^2} \;=\; \frac{1}{2q^2} + \frac{1}{2q\,q_i}.$$
Subtracting $\tfrac{1}{2qq_i}$: $\tfrac{1}{2qq_i} < \tfrac{1}{2q^2}$, i.e. $q < q_i$ —
contradicting $q_i \le q$. Hence $p/q = p_i/q_i$; since both are in lowest terms
(hypothesis; A.3) with positive denominators, $(p,q) = (p_i,q_i)$. $\blacksquare$

**Lemma A.8 (digit-shift for finite strings).** Let $k \ge 1$ and let
$(b_0; b_1, \dots, b_k)$ be a digit string ($b_j \ge 1$ for $j \ge 1$) with convergent
data $P_j, Q_j$. Let $P'_j, Q'_j$ ($-2 \le j \le k-1$) be the convergent data of the
shifted string $(b_1; b_2, \dots, b_k)$ (whose digit at index $t$ is $b_{t+1}$). Then
for $-1 \le j \le k$:
$$P_j = b_0 P'_{j-1} + Q'_{j-1}, \qquad Q_j = P'_{j-1}.$$
Moreover $P'_j \ge Q'_j \ge 1$ for $0 \le j \le k-1$.

*Proof.* Base cases: $j = -1$: $P_{-1} = 1 = b_0\cdot 0 + 1 = b_0P'_{-2} + Q'_{-2}$,
$Q_{-1} = 0 = P'_{-2}$. $j = 0$: $P_0 = b_0 = b_0\cdot 1 + 0 = b_0P'_{-1} + Q'_{-1}$,
$Q_0 = 1 = P'_{-1}$. Induction for $1 \le j \le k$ (both prior indices available):
$$P_j = b_jP_{j-1} + P_{j-2} = b_j(b_0P'_{j-2} + Q'_{j-2}) + (b_0P'_{j-3} + Q'_{j-3})
= b_0(b_jP'_{j-2} + P'_{j-3}) + (b_jQ'_{j-2} + Q'_{j-3}) = b_0P'_{j-1} + Q'_{j-1},$$
since the shifted string's recurrence at index $j-1$ has coefficient $b_j$; likewise
$Q_j = b_jP'_{j-2} + P'_{j-3} = P'_{j-1}$. Final claim: $Q'_0 = 1$ and $Q'_j =
b_{j+1}Q'_{j-1} + Q'_{j-2} \ge Q'_{j-1} \ge 1$ inductively ($Q'_{-1}=0$, $Q'_{-2} = 1
\ge 0$); and $P'_j - Q'_j \ge 0$: at $j = 0$, $P'_0 - Q'_0 = b_1 - 1 \ge 0$; at
$j = 1$, $P'_1 - Q'_1 = (b_2b_1 + 1) - b_2 = b_2(b_1 - 1) + 1 \ge 1$; for $j \ge 2$,
$P'_j - Q'_j = b_{j+1}(P'_{j-1} - Q'_{j-1}) + (P'_{j-2} - Q'_{j-2}) \ge 0$ by
induction. $\square$

**Lemma A.9 (certification lemma).** Let $k \ge 0$ and let $(b_0; b_1, \dots, b_k)$ be
a digit string with convergent data $P_j, Q_j$, and let $\alpha$ be irrational. If
$\alpha$ lies strictly between $C_k = P_k/Q_k$ and $M_k = (P_k + P_{k-1})/(Q_k +
Q_{k-1})$, then the Gauss-recursion digits of $\alpha$ satisfy
$$a_j(\alpha) = b_j \qquad (0 \le j \le k).$$

*Proof.* Induction on $k$.
**$k = 0$:** $C_0 = b_0/1$, $M_0 = (b_0+1)/1$. Strictly between means $b_0 < \alpha <
b_0 + 1$, so $a_0(\alpha) = \lfloor\alpha\rfloor = b_0$.
**$k \ge 1$:** with the shifted-string data of A.8 (write $C' := P'_{k-1}/Q'_{k-1}$,
$M' := (P'_{k-1} + P'_{k-2})/(Q'_{k-1} + Q'_{k-2})$, which are the analogous endpoint
data for the shifted string at top index $k-1$):
$$C_k = \frac{b_0P'_{k-1} + Q'_{k-1}}{P'_{k-1}} = b_0 + \frac{1}{C'}, \qquad
M_k = \frac{b_0(P'_{k-1}+P'_{k-2}) + (Q'_{k-1}+Q'_{k-2})}{P'_{k-1}+P'_{k-2}} = b_0 + \frac{1}{M'} .$$
(Denominators: $Q'_{k-1} \ge 1$ by A.8, so $C'$ is defined and $C' \ge 1$; also
$Q'_{k-1} + Q'_{k-2} \ge 1$ and $P'_{k-1} + P'_{k-2} \ge Q'_{k-1} + Q'_{k-2} \ge 1$
using A.8 and $P'_{-1} = 1 > 0 = Q'_{-1}$, so $M' \ge 1$.) Hence both endpoints lie in
$(b_0,\, b_0 + 1]$. Strictly between them, $\alpha \in (b_0, b_0+1)$ — using
irrationality to rule out $\alpha = b_0 + 1$ — so $a_0(\alpha) = b_0$, and the Gauss
recursion continues with $\beta := \alpha_1 = 1/(\alpha - b_0)$, irrational.
The map $\varphi(t) = b_0 + 1/t$ is a strictly decreasing bijection $(0,\infty) \to
(b_0, \infty)$, with $\alpha = \varphi(\beta)$, $C_k = \varphi(C')$, $M_k =
\varphi(M')$. A strictly monotone injection preserves "strictly between" (it reverses
order, and betweenness is symmetric); applying $\varphi^{-1}$: $\beta$ lies strictly
between $C'$ and $M'$. These are exactly the endpoint data of the shifted string
$(b_1; b_2, \dots, b_k)$ at top index $k-1$, so the induction hypothesis applied to
$\beta$ gives $a_t(\beta) = b_{t+1}$ for $0 \le t \le k-1$. Since $a_j(\alpha) =
a_{j-1}(\beta)$ for $j \ge 1$ (Gauss recursion), $a_j(\alpha) = b_j$ for
$0 \le j \le k$. $\blacksquare$

**Lemma A.10 (bit-length evaluation of power comparisons).** Let $N \ge 1$ be an
integer and $b$ its bit length, i.e. the unique integer with $2^{b-1} \le N < 2^b$.
If $N$ is not a power of $2$ — in particular if $N = 3^q$, $q \ge 1$ — then for every
integer $p$: $N < 2^p \iff p \ge b$, and $N > 2^p \iff p \le b - 1$.

*Proof.* If $p \ge b$: $N < 2^b \le 2^p$. If $p \le b-1$: $2^p \le 2^{b-1} \le N$ and
$N \ne 2^p$, so $N > 2^p$. The two cases are exhaustive and exclusive. $\square$

**Lemma A.11 (elementary numerical inequalities; no calculator appeals).**
(a) $e < 68/25$; in particular $e < 3$.
(b) $e^2 < 8$, hence $2 < 3\ln 2$.
(c) $(64/27)^2 > e$, hence $\ln(64/27) > 1/2$, hence $1/\ln(64/27) < 2$.

*Proof.* (a) For $n \ge 5$: $n! = 120 \cdot \prod_{j=6}^{n} j \ge 120 \cdot 6^{\,n-5}$
(each of the $n - 5$ factors is $\ge 6$; empty product $= 1$ at $n = 5$). Hence
$$\sum_{n \ge 5} \frac{1}{n!} \;\le\; \frac{1}{120}\sum_{j \ge 0} 6^{-j} \;=\; \frac{1}{120}\cdot\frac{6}{5} \;=\; \frac{1}{100}.$$
With the partial sum $\sum_{n=0}^{4} 1/n! = 1 + 1 + \tfrac12 + \tfrac16 + \tfrac1{24}
= \tfrac{65}{24}$:
$$e \;\le\; \frac{65}{24} + \frac{1}{100} \;=\; \frac{6524}{2400} \;<\; \frac{6528}{2400} \;=\; \frac{68}{25} \;<\; 3.$$
(b) $e^2 < (68/25)^2 = 4624/625 < 5000/625 = 8$ (squaring is strictly increasing on
positives; $4624 < 5000$). Taking $\ln$: $2 = \ln(e^2) < \ln 8 = 3\ln 2$.
(c) $(64/27)^2 = 4096/729$ and $729 \cdot 3 = 2187 < 4096$, so $(64/27)^2 > 3 > e$ by
(a). Taking $\ln$: $2\ln(64/27) > 1$, i.e. $\ln(64/27) > 1/2 > 0$, and inverting the
positive inequality: $1/\ln(64/27) < 2$. $\square$

### Part B — the cycle applications

#### B.2 Proof of L-9910.2

Let the cycle satisfy $x_{\min} \ge m^2$, and let $d, p, q$ be as in the Statement
($q \ge 1$ since $m \ge 1$; $\gcd(p,q) = 1$ by construction; $q \le m$; $m = dq$,
$K = dp$ by definition of $d = \gcd(K,m)$, with $t := d \ge 1$). By L-9905.5
(imported, restated in Definitions):
$$0 \;<\; \frac{K}{m} - \alpha \;\le\; \frac{1}{3\,x_{\min}\ln 2} \;\le\; \frac{1}{3\,m^2\ln 2},$$
the last step because $x_{\min} \ge m^2 > 0$ and $u \mapsto 1/(3u\ln 2)$ is decreasing.
Next, $\dfrac{1}{3m^2\ln 2} < \dfrac{1}{2m^2} \iff 2m^2 < 3m^2\ln 2 \iff 2 < 3\ln 2$,
which is Lemma A.11(b). Finally $\dfrac{1}{2m^2} \le \dfrac{1}{2q^2}$ since
$1 \le q \le m$. Since $K/m > \alpha$, the absolute value is the difference itself:
$$\left|\alpha - \frac{p}{q}\right| \;=\; \left|\alpha - \frac{K}{m}\right| \;=\; \frac{K}{m} - \alpha \;<\; \frac{1}{2q^2}.$$
$\alpha = \log_2 3$ is irrational (Lemma A.1). By Theorem A.7 (Legendre) applied to
the **reduced** fraction $p/q$: $(p, q) = (p_i, q_i)$ for some $i \ge 0$, a convergent
of $\alpha$. By Lemma A.5(b), even-index convergents are $< \alpha$; since $p/q = K/m
> \alpha$, the index $i$ is odd. What Legendre controls is only the reduced shape: the
cycle's parameters are recovered as $m = t\,q_i$, $K = t\,p_i$, $t = d \ge 1$ — the
unreduced $K/m$ need not itself appear in the convergent list. $\blacksquare$

*Consistency check (trivial cycle).* $m = 1$, $K = 2$, $x_{\min} = 1 \ge m^2 = 1$:
$d = 1$, $p/q = 2/1$, and $2/1 = p_1/q_1$ is indeed an odd-index convergent
(certified in B.3, Table 1, row $k=1$). No contradiction — as must be the case.

#### B.3 Proof of L-9910.3

**Reduction to integer inequalities.** By Lemma A.9, to prove that the digits of
$\alpha = \log_2 3$ begin $(b_0, \dots, b_{14}) = (1,1,1,2,2,3,1,5,2,23,2,2,1,1,55)$
it suffices to verify that $\alpha$ lies strictly between $C_{14}$ and $M_{14}$ for
this string — and, for good measure, we certify **every** prefix $k = 0, \dots, 14$
(each certificate independently proves its own prefix; the $k = 14$ certificate alone
already implies all fifteen digits). Each certification consists of the two
comparisons $\alpha$ vs $C_k$ and $\alpha$ vs $M_k$, with opposite senses (that the
senses are opposite is exactly "strictly between", since $C_k \neq M_k$ — their
difference has numerator $\pm 1$ by A.3). By Lemma A.1 each comparison **is** an
integer inequality $3^q \lessgtr 2^p$; by Lemma A.10 it is decided exactly by the bit
length of $3^q$. The convergents $P_k/Q_k$ are computed by the defining recurrence
from the digits (Table 1; recurrence and determinant identity re-verified in the
Adversarial tests).

**Table 1 — certificates for the first fifteen digits of $\log_2 3$.**
(Verified in exact integer arithmetic; rows $k \le 5$ hand-checkable. "$\mathrm{bl}$"
is the bit length of the power of 3 shown; the comparison then follows by A.10.)

| $k$ | $a_k$ | $C_k = p_k/q_k$ | $M_k$ | certificate: $\alpha$ vs $C_k$ | certificate: $\alpha$ vs $M_k$ |
|---|---|---|---|---|---|
| 0 | 1 | $1/1$ | $2/1$ | $3^1 > 2^1$ ($3 > 2$) | $3^1 < 2^2$ ($3 < 4$) |
| 1 | 1 | $2/1$ | $3/2$ | $3^1 < 2^2$ ($3 < 4$) | $3^2 > 2^3$ ($9 > 8$) |
| 2 | 1 | $3/2$ | $5/3$ | $3^2 > 2^3$ ($9 > 8$) | $3^3 < 2^5$ ($27 < 32$) |
| 3 | 2 | $8/5$ | $11/7$ | $3^5 < 2^8$ ($243 < 256$) | $3^7 > 2^{11}$ ($2187 > 2048$) |
| 4 | 2 | $19/12$ | $27/17$ | $3^{12} > 2^{19}$ ($531441 > 524288$) | $3^{17} < 2^{27}$ ($129140163 < 134217728$) |
| 5 | 3 | $65/41$ | $84/53$ | $3^{41} < 2^{65}$ ($36472996377170786403 < 36893488147419103232$) | $3^{53} > 2^{84}$ ($19383245667680019896796723 > 19342813113834066795298816$) |
| 6 | 1 | $84/53$ | $149/94$ | $3^{53} > 2^{84}$ (as above) | $3^{94} < 2^{149}$ ($\mathrm{bl}(3^{94}) = 149$) |
| 7 | 5 | $485/306$ | $569/359$ | $3^{306} < 2^{485}$ ($\mathrm{bl} = 485$) | $3^{359} > 2^{569}$ ($\mathrm{bl} = 570$) |
| 8 | 2 | $1054/665$ | $1539/971$ | $3^{665} > 2^{1054}$ ($\mathrm{bl} = 1055$) | $3^{971} < 2^{1539}$ ($\mathrm{bl} = 1539$) |
| 9 | 23 | $24727/15601$ | $25781/16266$ | $3^{15601} < 2^{24727}$ ($\mathrm{bl} = 24727$) | $3^{16266} > 2^{25781}$ ($\mathrm{bl} = 25782$) |
| 10 | 2 | $50508/31867$ | $75235/47468$ | $3^{31867} > 2^{50508}$ ($\mathrm{bl} = 50509$) | $3^{47468} < 2^{75235}$ ($\mathrm{bl} = 75235$) |
| 11 | 2 | $125743/79335$ | $176251/111202$ | $3^{79335} < 2^{125743}$ ($\mathrm{bl} = 125743$) | $3^{111202} > 2^{176251}$ ($\mathrm{bl} = 176252$) |
| 12 | 1 | $176251/111202$ | $301994/190537$ | $3^{111202} > 2^{176251}$ (as above) | $3^{190537} < 2^{301994}$ ($\mathrm{bl} = 301994$) |
| 13 | 1 | $301994/190537$ | $478245/301739$ | $3^{190537} < 2^{301994}$ (as above) | $3^{301739} > 2^{478245}$ ($\mathrm{bl} = 478246$) |
| 14 | 55 | $16785921/10590737$ | $17087915/10781274$ | $3^{10590737} > 2^{16785921}$ ($\mathrm{bl} = 16785922$) | $3^{10781274} < 2^{17087915}$ ($\mathrm{bl} = 17087915$) |

Each row's two comparisons have opposite senses, so $\alpha$ is strictly between $C_k$
and $M_k$; by Lemma A.9 the digits $a_0(\alpha), \dots, a_k(\alpha)$ are as displayed.
The alternation of sides (Lemma A.5(b)) is visible: the $C_k$-column comparison is
"$>$" exactly for even $k$. This proves the digit and convergent lists of the
Statement. The nature of the verification: the displayed inequalities for $k \le 5$
are checkable by hand; all thirty are finite, exact integer computations, re-runnable
from the script in the Adversarial tests (machine bignum arithmetic; ~6 s total).
**Completeness of the $q \le 10^5$ list:** by A.2(b) the $q_k$ are strictly increasing
from $k = 1$ on; $q_{11} = 79335 \le 10^5 < 111202 = q_{12}$, so the convergents with
denominator $\le 10^5$ are exactly $k = 0, \dots, 11$. $\blacksquare$

*Comparison with the coordinator's expected listing:* digits $[1;1,1,2,2,3,1,5,2,23]$
and convergents $1/1, 2/1, 3/2, 8/5, 19/12, 65/41, 84/53, 485/306, 1054/665,
24727/15601$ — **confirmed exactly**; certified continuation $2, 2, 1, 1, 55$; no
mismatch to flag. The high-precision *guess* continues $a_{15} = 1$, $a_{16} = 4$,
left uncertified here.

#### B.4 Proof of L-9910.4

**(i) $K = 2m$ only for the trivial cycle.** Suppose an S-cycle (on positive odds)
has $K = 2m$. By L-9905.5: $2 - \alpha = K/m - \alpha \le 1/(3x_{\min}\ln 2)$, and
$2 - \alpha > 0$ (indeed $\alpha < 2 \iff 3 < 4$, Lemma A.1). Solving for
$x_{\min}$ (all factors positive):
$$x_{\min} \;\le\; \frac{1}{3\ln 2\,(2 - \alpha)} \;=\; \frac{1}{6\ln 2 - 3\ln 3} \;=\; \frac{1}{\ln(64/27)} \;<\; 2,$$
where $3\ln 2 \cdot (2 - \ln 3/\ln 2) = 6\ln 2 - 3\ln 3 = \ln(2^6/3^3) = \ln(64/27)$,
and the final inequality is Lemma A.11(c). Since $x_{\min}$ is a positive odd integer,
$x_{\min} = 1$, so $1$ is an element of the cycle. But $S(1) = 4/4 = 1$, so from that
element on every element equals $1$; by cyclicity all elements equal $1$ and the least
period is $m = 1$: the cycle is the trivial cycle (which indeed has $K = 2 = 2m$).
Hence **no nontrivial S-cycle has $K = 2m$** — equivalently, reduced shape $2/1$ is
excluded for nontrivial cycles, for every $x_{\min}$, with no Legendre input.
$\blacksquare$

> **Correction, flagged per protocol** (confirmed by the coordinator): the assigning
> sketch claimed $2 - \log_2 3 \approx 0.415 > 1/(3x_{\min}\ln 2)$ "forces
> $x_{\min} < 1$". At $x_{\min} = 1$: $1/(3\ln 2) = 0.4809{\dots} > 0.4150{\dots} =
> 2 - \log_2 3$ (floats for display; the exact content is $\ln(64/27) < 1$, i.e.
> $64 < 27e$, true since $e > 2.7$), so the claimed inequality **fails** at
> $x_{\min} = 1$ and the route breaks — as it must, since the trivial cycle realizes
> $K = 2m$. The corrected conclusion above ($x_{\min} < 2$, hence $= 1$, hence trivial)
> is what is actually provable, and suffices for the intended exclusion.

**(ii) The table of admissible above-$\alpha$ shapes with $q \le 10^5$.** By
L-9910.3, the convergents with $q \le 10^5$ are $k = 0..11$; by A.5(b) the odd-index
ones — those above $\alpha$ — are $k = 1, 3, 5, 7, 9, 11$:

**Table 2 — odd-index convergents of $\log_2 3$ with $q \le 10^5$, with certificates
and the constraints they impose on a cycle with $x_{\min} \ge m^2$ of that reduced
shape.**

| $k$ | $p_k/q_k$ | side certificate | cycle constraint (if this is the reduced shape) |
|---|---|---|---|
| 1 | $2/1$ | $3^{1} < 2^{2}$ | $m = t$, $K = 2t$ — **excluded for nontrivial cycles by (i)**; occurs for the trivial cycle ($t=1$) |
| 3 | $8/5$ | $3^{5} < 2^{8}$ | $5 \mid m$, $K = \tfrac{8}{5}m$; ($t = m/5$) |
| 5 | $65/41$ | $3^{41} < 2^{65}$ | $41 \mid m$, $K = \tfrac{65}{41}m$ |
| 7 | $485/306$ | $3^{306} < 2^{485}$ ($\mathrm{bl} = 485$) | $306 \mid m$, $K = \tfrac{485}{306}m$ |
| 9 | $24727/15601$ | $3^{15601} < 2^{24727}$ ($\mathrm{bl} = 24727$) | $15601 \mid m$, $K = \tfrac{24727}{15601}m$ |
| 11 | $125743/79335$ | $3^{79335} < 2^{125743}$ ($\mathrm{bl} = 125743$) | $79335 \mid m$, $K = \tfrac{125743}{79335}m$ |

By L-9910.2, a cycle with $x_{\min} \ge m^2$ whose reduced denominator satisfies
$q \le 10^5$ must have its reduced shape in this table ($p/q$ is an odd-index
convergent by L-9910.2; $q \le 10^5$ plus the completeness clause of L-9910.3 places
it among $k \le 11$). Non-load-bearing remark (cross-ref L-9906, PROVED): nontrivial
cycles have $m \ge 7$, so shape $8/5$ additionally requires $t \ge 2$, i.e.
$m \ge 10$; the other rows have $q \ge 41 \ge 7$ already. $\blacksquare$

**(iii) Compound corollary.** Let a nontrivial S-cycle be given. Exactly one of
$x_{\min} \ge m^2$, $x_{\min} < m^2$ holds, so at least one branch below applies (we do
**not** claim which):
- If $x_{\min} \ge m^2$ (branch (a)): L-9910.2 gives that the reduced $p/q$ is an
  odd-index convergent with $q \mid m$ and $K = mp/q$; and $q = 1$ would force
  $p/q = 2/1$ (the only odd-index convergent with denominator $1$ is $p_1/q_1 = 2/1$:
  denominators strictly increase from $k = 1$, and $q_1 = 1$ here — Table 1 — so
  $k \ge 2$ has $q_k \ge 2$), which (i) excludes for nontrivial cycles; hence
  $q \ge 5$ (the next odd-index denominator, Table 2 / L-9910.3).
- If $x_{\min} < m^2$ (branch (b)): by L-9905.4 (imported element lower bound applied
  to $x_{\min}$) and L-9905.2 ($2^K - 3^m \ge 1 > 0$):
  $$\frac{3^m - 2^m}{2^K - 3^m} \;\le\; x_{\min} \;<\; m^2
  \quad\Longrightarrow\quad 3^m - 2^m \;<\; m^2\,(2^K - 3^m).$$
Contrapositive packaging: **if the reduced $K/m$ is not an odd-index convergent value
of $\log_2 3$, then $x_{\min} < m^2$ and $3^m - 2^m < m^2(2^K - 3^m)$** — the shape
constraint from above and the element bound from below squeeze $(m,K)$ jointly.
$\blacksquare$

*Empirically boosted instance (labeled; hypothesis is finite verification, not
proof):* the Adversarial tests below verify that no S-cycle has minimal element
$\le 10^5$ except the trivial one. Under that finite fact, any nontrivial cycle with
$m \le 316$ has $x_{\min} > 10^5 \ge 99856 = 316^2 \ge m^2$, so branch (a) applies
with $q \le m \le 316$: by Table 2, $K/m \in \{8/5,\ 65/41,\ 485/306\}$ — i.e.
$5 \mid m$ or $41 \mid m$ or $306 \mid m$, and $K$ is determined by $m$. (With
L-9906's $m \ge 7$: shape $8/5$ needs $m \in \{10, 15, \dots, 315\}$, shape $65/41$
needs $m \in \{41, 82, \dots, 287\}$, shape $485/306$ needs $m = 306$.)

#### B.5 L-9910.5

The boxed remark in the Statement is the claim; there is nothing to prove, only scope
to delimit: Theorems L-9910.1–.4 use finite integer arithmetic, the elementary
estimates of Lemma A.11, and the PROVED L-9905 imports — no transcendence measures, no
linear-forms-in-logarithms, no unproved external computation. Consequently they cannot
by themselves exclude nontrivial cycles unconditionally: for any fixed $m$, both
branches of L-9910.4(iii) remain logically open until either a Baker-type lower bound
on $|K\ln 2 - m\ln 3|$ or a verified $x_{\min}$ floor beyond $m^2$ is supplied
(L-9913's intended job, using this file's certified CF data). $\square$

---

## Dependency audit

| Dependency | Precise point of use |
|---|---|
| L-9905.5 (PROVED) | B.2 (the approximation chain, first two inequalities); B.4(i) (with $K = 2m$ substituted). |
| L-9905.2 (PROVED) | B.4(iii)(b): positivity of $2^K - 3^m$ before multiplying. |
| L-9905.4 Corollary (PROVED) | B.4(iii)(b): $x_{\min} \ge (3^m-2^m)/(2^K-3^m)$. |
| L-9905 anchoring convention | Definitions: well-definedness of $m, K, x_{\min}$ per cycle. |
| D-9904 / D-9905 / D-9908 | Cycle notation throughout; $S(1) = 1$ in B.4(i). |
| L-9906 (PROVED) | Non-load-bearing remarks only (B.4(ii), (iii) instance): $m \ge 7$ refinements. Removing them changes no theorem. |
| Lemmas A.1–A.11 | All proved in this file. A.7 (Legendre) uses A.2, A.3, A.5, A.6. A.9 uses A.8. B.2 uses A.1, A.5(b), A.7, A.11(b). B.3 uses A.1, A.2(b), A.3, A.5(b), A.9, A.10. B.4 uses A.1, A.5(b), A.11(c), plus the imports. |
| Background analysis facts | As itemized in Definitions: monotonicity of $\ln, \exp, 2^t, 3^t$, squares/cubes on positives; $\ln$ of products/powers; $e = \sum 1/n!$; $\log_2 3 = \ln 3/\ln 2$. Used in A.1, A.5, A.11, B.2, B.4. |
| Machine integer arithmetic | The thirty inequalities of Table 1 and six of Table 2 (subset of Table 1): exact bignum computations, re-runnable (Adversarial tests); rows $k \le 5$ hand-checkable. |

No circularity: L-9905 and L-9906 do not depend on L-9910. Nothing assumes the Collatz
conjecture or its negation; all results hold whether or not nontrivial cycles exist.

## Gap audit

Deliberate search against the README §8 checklist and this file's specific risks:

- **Choice of index in Legendre:** the tie $q_0 = q_1$ (which occurs iff $a_1 = 1$ —
  and does occur for $\log_2 3$) is handled by taking $i = \max\{j : q_j \le q\}$
  (A.2(c)), so A.6's hypothesis $q < q_{i+1}$ genuinely holds. A naive "unique $i$"
  claim would be false; flagged and avoided.
- **Non-strict vs strict:** A.6 gives $\ge D_i$ (equality characterized); the Legendre
  contradiction uses only $\ge$ plus the twice-used strict hypothesis. Checked line by
  line above.
- **Reduced vs unreduced shape:** L-9910.2 concludes only that the **reduced** $p/q$
  is a convergent; $m = tq$, $K = tp$ is stated explicitly. Conflating $K/m$ with a
  convergent "as written" would be an error; avoided throughout (see Table 2's
  divisibility phrasing).
- **Trivial cycle sanity:** the framework must not (and does not) exclude the trivial
  cycle: it satisfies L-9910.2's hypothesis and lands on the genuine convergent $2/1$
  (B.2 consistency check); B.4(i) excludes $2/1$ only for **nontrivial** cycles.
- **Coordinator-sketch error:** the "$x_{\min} < 1$" route is refuted (with the exact
  witness $\ln(64/27) < 1$) and corrected to $x_{\min} < 2$; flagged in the Statement
  and B.4(i). The corrected constant is proved without calculators (A.11(c)).
- **One-directionality of Legendre:** the converse is false and is nowhere used;
  adversarially witnessed ($1/1$ and $65/41$ are convergents failing the hypothesis).
- **Certification soundness vs guessing:** the CF digits are *guessed* from a
  250-digit numerical value but *proved* by the certificates via A.9 — the guess is
  not load-bearing; a wrong guess would fail certification (tested). Only digits
  $a_0..a_{14}$ are claimed; $a_{15}, a_{16}$ are explicitly labeled uncertified.
- **"Strictly between" preservation:** under the strictly decreasing bijection
  $\varphi$ in A.9 — proved via order reversal + symmetry of betweenness; endpoint
  degeneracies excluded because $C_k \ne M_k$ (numerator of difference is $\pm 1$,
  A.3).
- **Hidden finiteness / empirical-vs-universal confusion:** the only empirical inputs
  are (1) the $x_{\min} \le 10^5$ cycle search and (2) machine verification of finite
  integer inequalities. (1) is used **only** in passages explicitly labeled
  empirical/finite-verification (the boosted instance); (2) is a finite decidable
  computation, listed honestly in the Dependency audit and Remaining uncertainty, with
  hand-checkable small cases.
- **Boundary cases:** $m = 1$ (trivial cycle) threaded through B.2 and B.4(i);
  $q = 1$ in L-9910.1 (works: $q_0 = 1 \le q$); $k = 0$ base of A.9; $j$-index bases
  of A.8 including the negative-index conventions; $x_{\min} = m^2$ boundary included
  in L-9910.2's hypothesis ($\ge$, and the subsequent strict step comes from
  $2 < 3\ln2$, not from strictness of $x_{\min} > m^2$).
- **No assumption equivalent to the conjecture**; no limit interchanges; estimates
  uniform and explicit ($1/(3\ln 2)$, $1/2$, $\ln(64/27)$).

No unresolved gaps found by the author.

## Adversarial tests

**Finite verification, not proof** — except in the precise sense stated in B.3: the
displayed integer inequalities, once verified, constitute the proof of the CF digits
via Lemma A.9; the verification of each inequality is a finite exact computation.
Scripts kept session-locally at `scratchpad/l9910_cf.py` and
`scratchpad/l9910_cycles.py`; full code inline for reproducibility. Environment:
CPython 3 (stdlib only), Linux; runtimes ~6 s and ~0.1 s.

Design notes:
1. **Script 1** guesses digits from a 250-digit `decimal` value (guess is untrusted),
   then re-derives all convergents by the recurrence, checks the determinant identity
   and strict denominator growth, and certifies every prefix $k = 0..14$ by the two
   exact power comparisons (via bit length, Lemma A.10) — including that the two
   senses are opposite ("strictly between") and that sides match parity (A.5(b)
   alternation). It cross-checks the coordinator's expected listing, verifies
   completeness of the $q \le 10^5$ table, runs an exhaustive Legendre check for all
   $q \le 350$ (every coprime $p/q$ with $|\alpha - p/q| < 1/(2q^2)$ — decided
   exactly by power comparisons at exponent $2q^2$ — must be a certified convergent),
   reports the nearest **non**-convergent misses (all with $q^2|\alpha - p/q| > 1/2$,
   as Legendre's contrapositive demands: near-counterexamples), exhibits convergents
   for which the Legendre hypothesis fails (converse false), and checks the exact
   rational inequalities behind A.11 and the corrected B.4(i) constant.
2. **Script 2** searches for all S-cycles with minimal element $\le 10^5$ by the
   minimal-element method (sound: if $n = x_{\min}$ of a cycle, iterating $S$ from $n$
   stays $\ge n$ until returning to $n$; completeness over the scanned range is by
   construction). Expected and found: only the trivial cycle. This supports the
   labeled empirical instance in B.4(iii) and adversarially probes B.4(i): a
   nontrivial cycle with $K = 2m$ would need $x_{\min} = 1$, and none exists.

### Script 1: `l9910_cf.py`

```python
#!/usr/bin/env python3
"""
Adversarial tests for L-9910 (research/foundations/L-9910-cycle-convergents.md).
FINITE VERIFICATION ONLY -- not a proof (but each CF digit is accompanied by an
exact integer-power certificate; via the certification lemma L-9910.3 those
certificates ARE a proof of the displayed digits).
Agent: fable-02-p4.  Date: 2026-07-21.  Exact integer arithmetic throughout;
floats appear only in clearly labeled display lines.
"""
from fractions import Fraction
from math import gcd, log2, log
from decimal import Decimal, getcontext

fails = 0
def check(label, cond):
    global fails
    if not cond:
        fails += 1
        print("FAIL:", label)

# ---------------------------------------------------------------------------
# Exact comparison  alpha = log2(3)  vs  p/q  (q >= 1):
#     alpha < p/q  <=>  3^q < 2^p   ;   alpha > p/q  <=>  3^q > 2^p
# (never equal: 3^q is odd >= 3, so 3^q != 2^p).
# Implemented via bit_length: with b = (3^q).bit_length(),
#     2^(b-1) <= 3^q < 2^b, hence  3^q < 2^p <=> p >= b.
# ---------------------------------------------------------------------------
def lt(pow3q, p):
    """True iff 3^q < 2^p, given pow3q = 3^q."""
    return pow3q.bit_length() <= p

# ------------------------------------------------------------------ Step 1
# Guess ~17 CF digits of alpha from a 250-digit decimal approximation.
# The guess needs NO trust: every displayed digit is certified below by
# exact integer inequalities; a wrong guess would fail certification loudly.
getcontext().prec = 250
alpha_dec = Decimal(3).ln() / Decimal(2).ln()
r = Fraction(alpha_dec)
guess = []
x = r
for _ in range(17):
    a = x.numerator // x.denominator
    guess.append(a)
    x = 1 / (x - a)
print("guessed digits:", guess)

KMAX = 14                      # certify a_0..a_14  (15 partial quotients)
a = guess[:KMAX + 1]

# ------------------------------------------------------------------ Step 2
# Convergents by recurrence; exact certification of every prefix k:
#   alpha strictly between C_k = p_k/q_k and M_k = (p_k+p_{k-1})/(q_k+q_{k-1}).
# Each certificate = two integer power comparisons.  3^(q_k) is built
# incrementally: 3^{q_k} = (3^{q_{k-1}})^{a_k} * 3^{q_{k-2}}.
p = {-2: 0, -1: 1}
q = {-2: 1, -1: 0}
pw = {-2: 3, -1: 1}            # pw[k] = 3^{q_k};  3^{q_{-2}} = 3^1, 3^{q_{-1}} = 3^0
def fmt(n):
    s = str(n)
    return s if len(s) <= 24 else f"[{len(s)}-digit integer]"

print("\nPer-prefix certificates (each line: two exact power inequalities):")
for k in range(KMAX + 1):
    p[k] = a[k] * p[k - 1] + p[k - 2]
    q[k] = a[k] * q[k - 1] + q[k - 2]
    pw[k] = pw[k - 1] ** a[k] * pw[k - 2]
    check(f"pw consistency k={k}", pw[k] == 3 ** q[k] if q[k] < 10**5 else True)
    # determinant identity and strict q-increase:
    check(f"det k={k}", p[k] * q[k - 1] - p[k - 1] * q[k] == (-1) ** (k - 1))
    if k >= 2:
        check(f"q-incr k={k}", q[k] > q[k - 1])
    # endpoints:
    pm, qm = p[k] + p[k - 1], q[k] + q[k - 1]      # mediant M_k
    pw_m = pw[k] * pw[k - 1]                        # 3^{q_k + q_{k-1}}
    # alpha vs C_k:  even k -> alpha > C_k (3^{q_k} > 2^{p_k}); odd k -> <.
    ck_lt = lt(pw[k], p[k])       # True iff 3^{q_k} < 2^{p_k}  iff alpha < C_k
    mk_lt = lt(pw_m, pm)          # True iff alpha < M_k
    # "strictly between" = the two comparisons disagree:
    check(f"between k={k}", ck_lt != mk_lt)
    # side must match parity (L4 alternation):
    check(f"parity k={k}", ck_lt == (k % 2 == 1))
    s1 = "<" if ck_lt else ">"
    s2 = "<" if mk_lt else ">"
    print(f" k={k:2d} a_k={a[k]:2d}  C_k={p[k]}/{q[k]}  M_k={pm}/{qm}\n"
          f"       cert: 3^{q[k]} {s1} 2^{p[k]}"
          f"   [{fmt(3**q[k]) if q[k] <= 100 else f'bitlen(3^{q[k]})={pw[k].bit_length()} vs p={p[k]}'}"
          f"{' vs ' + fmt(2**p[k]) if q[k] <= 100 else ''}]\n"
          f"       cert: 3^{qm} {s2} 2^{pm}"
          f"   [{fmt(3**qm) if qm <= 100 else f'bitlen(3^{qm})={pw_m.bit_length()} vs p={pm}'}"
          f"{' vs ' + fmt(2**pm) if qm <= 100 else ''}]")

digits = [a[k] for k in range(KMAX + 1)]
convs = [(p[k], q[k]) for k in range(KMAX + 1)]
print("\ncertified digits a_0..a_14:", digits)
print("certified convergents p_k/q_k:")
for k in range(KMAX + 1):
    side = "ABOVE" if k % 2 == 1 else "below"
    print(f"  k={k:2d}: {p[k]}/{q[k]}  ({side} alpha)")

# Cross-check against the coordinator's listing:
coord_digits = [1, 1, 1, 2, 2, 3, 1, 5, 2, 23]
coord_convs = [(1,1),(2,1),(3,2),(8,5),(19,12),(65,41),(84,53),(485,306),
               (1054,665),(24727,15601)]
check("coordinator digit listing", digits[:10] == coord_digits)
check("coordinator convergent listing", convs[:10] == coord_convs)
print("coordinator's partial listing matches:",
      digits[:10] == coord_digits and convs[:10] == coord_convs)

# ------------------------------------------------------------------ Step 3
# Table for L-9910.4(ii): ALL convergents with q <= 10^5, sides certified.
# Completeness: q_12 > 10^5 and q_k strictly increasing (certified above).
check("q12 exceeds 1e5", q[12] > 10**5)
print(f"\nq_11 = {q[11]} <= 1e5 < q_12 = {q[12]}  "
      f"=> convergents with q <= 1e5 are exactly k = 0..11.")
print("Odd-index (ABOVE-alpha) convergents with q <= 1e5:")
for k in (1, 3, 5, 7, 9, 11):
    print(f"  k={k:2d}: {p[k]}/{q[k]}   cert: 3^{q[k]} < 2^{p[k]} "
          f"(bitlen(3^{q[k]}) = {pw[k].bit_length()} <= {p[k]})")
    check(f"above k={k}", lt(pw[k], p[k]))

# ------------------------------------------------------------------ Step 4
# Legendre exhaustive contrapositive test, q = 1..350:
# whenever |alpha - p/q| < 1/(2q^2) exactly (i.e. (2pq-1)/(2q^2) < alpha
# < (2pq+1)/(2q^2), two power comparisons), the reduced p/q must be a
# certified convergent.  Also collect near-counterexamples: coprime
# non-convergents with the smallest q^2|alpha - p/q| (all must be > 1/2).
convset = set(convs)
af = log2(3)                       # float, display/candidate-finding only
near = []
n_hyp = 0
for qq in range(1, 351):
    pw2q2 = 3 ** (2 * qq * qq)
    for pp in range(int(af * qq) - 1, int(af * qq) + 3):
        if pp < 1 or gcd(pp, qq) != 1:
            continue
        # exact test: alpha > (2pq-1)/(2q^2)  and  alpha < (2pq+1)/(2q^2)
        hyp = (not lt(pw2q2, 2 * pp * qq - 1)) and lt(pw2q2, 2 * pp * qq + 1)
        if hyp:
            n_hyp += 1
            check(f"Legendre {pp}/{qq}", (pp, qq) in convset)
        elif (pp, qq) not in convset:
            near.append((qq * qq * abs(af - pp / qq), pp, qq))
print(f"\nLegendre test: {n_hyp} fractions p/q (q<=350) satisfy "
      f"|alpha-p/q| < 1/(2q^2); every one is a certified convergent.")
near.sort()
print("Nearest NON-convergent misses (q^2*|alpha-p/q|, p/q) "
      "[floats, display only; all must exceed 0.5]:")
for v, pp, qq in near[:5]:
    print(f"  {v:.6f}  {pp}/{qq}")
    check(f"near-miss {pp}/{qq} above 1/2",
          not ((not lt(pw3 := 3 ** (2 * qq * qq), 2 * pp * qq - 1))
               and lt(pw3, 2 * pp * qq + 1)))
# One-directionality: convergents may FAIL the hypothesis:
print("Convergents and the Legendre hypothesis (q^2*err, float display):")
for k in range(0, 8):
    pk, qk = convs[k]
    pw2q2 = 3 ** (2 * qk * qk)
    hyp = (not lt(pw2q2, 2 * pk * qk - 1)) and lt(pw2q2, 2 * pk * qk + 1)
    print(f"  k={k}: {pk}/{qk}: q^2*err = {qk*qk*abs(af-pk/qk):.4f}  "
          f"hypothesis {'HOLDS' if hyp else 'fails (converse of Legendre is false)'}")

# ------------------------------------------------------------------ Step 5
# Exact rational inequalities used in L-9910.2 / L-9910.4(i):
#  (a) e < 65/24 + 1/100 < 68/25          [tail bound in file]
#      integer form: 6524/2400 < 6528/2400
#  (b) (68/25)^2 < 8  <=>  4624 < 5000    => e^2 < 8 => 3 ln 2 > 2
#  (c) (64/27)^2 = 4096/729 > 3 > e       => ln(64/27) > 1/2
check("6524<6528", 6524 < 6528)
check("e^2<8 rational", 68 * 68 == 4624 and 4624 < 5000)
check("(64/27)^2>3", 4096 > 3 * 729)
print("\nExact ineq. checks: 6524<6528, 4624<5000, 4096>3*729 all hold.")
print(f"[float display] 3*ln2 = {3*log(2):.6f} (>2);  "
      f"2-log2(3) = {2-af:.6f};  1/(3*ln2) = {1/(3*log(2)):.6f} "
      f"(note 0.415 < 0.481: x_min=1 does NOT violate the K=2m bound -- "
      f"the trivial cycle must and does survive);  "
      f"1/(3*ln2*(2-log2(3))) = {1/(3*log(2)*(2-af)):.6f} (< 2).")
# Trivial cycle consistency with L-9910.2: K/m = 2/1 = p_1/q_1, an
# odd-index convergent; x_min = 1 >= m^2 = 1.
check("trivial cycle shape", (2, 1) == convs[1])

print("\nRESULT:", "ALL CHECKS PASSED" if fails == 0 else f"{fails} FAILURES")
```

**Output (verbatim, run 2026-07-21; ~6 s):**

```text
guessed digits: [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55, 1, 4]

Per-prefix certificates (each line: two exact power inequalities):
 k= 0 a_k= 1  C_k=1/1  M_k=2/1
       cert: 3^1 > 2^1   [3 vs 2]
       cert: 3^1 < 2^2   [3 vs 4]
 k= 1 a_k= 1  C_k=2/1  M_k=3/2
       cert: 3^1 < 2^2   [3 vs 4]
       cert: 3^2 > 2^3   [9 vs 8]
 k= 2 a_k= 1  C_k=3/2  M_k=5/3
       cert: 3^2 > 2^3   [9 vs 8]
       cert: 3^3 < 2^5   [27 vs 32]
 k= 3 a_k= 2  C_k=8/5  M_k=11/7
       cert: 3^5 < 2^8   [243 vs 256]
       cert: 3^7 > 2^11   [2187 vs 2048]
 k= 4 a_k= 2  C_k=19/12  M_k=27/17
       cert: 3^12 > 2^19   [531441 vs 524288]
       cert: 3^17 < 2^27   [129140163 vs 134217728]
 k= 5 a_k= 3  C_k=65/41  M_k=84/53
       cert: 3^41 < 2^65   [36472996377170786403 vs 36893488147419103232]
       cert: 3^53 > 2^84   [[26-digit integer] vs [26-digit integer]]
 k= 6 a_k= 1  C_k=84/53  M_k=149/94
       cert: 3^53 > 2^84   [[26-digit integer] vs [26-digit integer]]
       cert: 3^94 < 2^149   [[45-digit integer] vs [45-digit integer]]
 k= 7 a_k= 5  C_k=485/306  M_k=569/359
       cert: 3^306 < 2^485   [bitlen(3^306)=485 vs p=485]
       cert: 3^359 > 2^569   [bitlen(3^359)=570 vs p=569]
 k= 8 a_k= 2  C_k=1054/665  M_k=1539/971
       cert: 3^665 > 2^1054   [bitlen(3^665)=1055 vs p=1054]
       cert: 3^971 < 2^1539   [bitlen(3^971)=1539 vs p=1539]
 k= 9 a_k=23  C_k=24727/15601  M_k=25781/16266
       cert: 3^15601 < 2^24727   [bitlen(3^15601)=24727 vs p=24727]
       cert: 3^16266 > 2^25781   [bitlen(3^16266)=25782 vs p=25781]
 k=10 a_k= 2  C_k=50508/31867  M_k=75235/47468
       cert: 3^31867 > 2^50508   [bitlen(3^31867)=50509 vs p=50508]
       cert: 3^47468 < 2^75235   [bitlen(3^47468)=75235 vs p=75235]
 k=11 a_k= 2  C_k=125743/79335  M_k=176251/111202
       cert: 3^79335 < 2^125743   [bitlen(3^79335)=125743 vs p=125743]
       cert: 3^111202 > 2^176251   [bitlen(3^111202)=176252 vs p=176251]
 k=12 a_k= 1  C_k=176251/111202  M_k=301994/190537
       cert: 3^111202 > 2^176251   [bitlen(3^111202)=176252 vs p=176251]
       cert: 3^190537 < 2^301994   [bitlen(3^190537)=301994 vs p=301994]
 k=13 a_k= 1  C_k=301994/190537  M_k=478245/301739
       cert: 3^190537 < 2^301994   [bitlen(3^190537)=301994 vs p=301994]
       cert: 3^301739 > 2^478245   [bitlen(3^301739)=478246 vs p=478245]
 k=14 a_k=55  C_k=16785921/10590737  M_k=17087915/10781274
       cert: 3^10590737 > 2^16785921   [bitlen(3^10590737)=16785922 vs p=16785921]
       cert: 3^10781274 < 2^17087915   [bitlen(3^10781274)=17087915 vs p=17087915]

certified digits a_0..a_14: [1, 1, 1, 2, 2, 3, 1, 5, 2, 23, 2, 2, 1, 1, 55]
certified convergents p_k/q_k:
  k= 0: 1/1  (below alpha)
  k= 1: 2/1  (ABOVE alpha)
  k= 2: 3/2  (below alpha)
  k= 3: 8/5  (ABOVE alpha)
  k= 4: 19/12  (below alpha)
  k= 5: 65/41  (ABOVE alpha)
  k= 6: 84/53  (below alpha)
  k= 7: 485/306  (ABOVE alpha)
  k= 8: 1054/665  (below alpha)
  k= 9: 24727/15601  (ABOVE alpha)
  k=10: 50508/31867  (below alpha)
  k=11: 125743/79335  (ABOVE alpha)
  k=12: 176251/111202  (below alpha)
  k=13: 301994/190537  (ABOVE alpha)
  k=14: 16785921/10590737  (below alpha)
coordinator's partial listing matches: True

q_11 = 79335 <= 1e5 < q_12 = 111202  => convergents with q <= 1e5 are exactly k = 0..11.
Odd-index (ABOVE-alpha) convergents with q <= 1e5:
  k= 1: 2/1   cert: 3^1 < 2^2 (bitlen(3^1) = 2 <= 2)
  k= 3: 8/5   cert: 3^5 < 2^8 (bitlen(3^5) = 8 <= 8)
  k= 5: 65/41   cert: 3^41 < 2^65 (bitlen(3^41) = 65 <= 65)
  k= 7: 485/306   cert: 3^306 < 2^485 (bitlen(3^306) = 485 <= 485)
  k= 9: 24727/15601   cert: 3^15601 < 2^24727 (bitlen(3^15601) = 24727 <= 24727)
  k=11: 125743/79335   cert: 3^79335 < 2^125743 (bitlen(3^79335) = 125743 <= 125743)

Legendre test: 6 fractions p/q (q<=350) satisfy |alpha-p/q| < 1/(2q^2); every one is a certified convergent.
Nearest NON-convergent misses (q^2*|alpha-p/q|, p/q) [floats, display only; all must exceed 0.5]:
  0.663163  11/7
  0.735337  5/3
  0.945837  27/17
  1.046537  46/29
  1.135291  401/253
Convergents and the Legendre hypothesis (q^2*err, float display):
  k=0: 1/1: q^2*err = 0.5850  hypothesis fails (converse of Legendre is false)
  k=1: 2/1: q^2*err = 0.4150  hypothesis HOLDS
  k=2: 3/2: q^2*err = 0.3399  hypothesis HOLDS
  k=3: 8/5: q^2*err = 0.3759  hypothesis HOLDS
  k=4: 19/12: q^2*err = 0.2346  hypothesis HOLDS
  k=5: 65/41: q^2*err = 0.6780  hypothesis fails (converse of Legendre is false)
  k=6: 84/53: q^2*err = 0.1597  hypothesis HOLDS
  k=7: 485/306: q^2*err = 0.4513  hypothesis HOLDS

Exact ineq. checks: 6524<6528, 4624<5000, 4096>3*729 all hold.
[float display] 3*ln2 = 2.079442 (>2);  2-log2(3) = 0.415037;  1/(3*ln2) = 0.480898 (note 0.415 < 0.481: x_min=1 does NOT violate the K=2m bound -- the trivial cycle must and does survive);  1/(3*ln2*(2-log2(3))) = 1.158686 (< 2).

RESULT: ALL CHECKS PASSED
```

*(Note: an earlier run of this script displayed the same certificates and results with
the A.11(c) check in the equivalent cube form $(64/27)^3 > 13 > e$; the file's Lemma
A.11(c) uses the square form, and Step 5 above matches it.)*

### Script 2: `l9910_cycles.py`

```python
#!/usr/bin/env python3
"""
Adversarial test for L-9910.4 (research/foundations/L-9910-cycle-convergents.md):
brute-force S-cycle search.  FINITE VERIFICATION ONLY -- not a proof.
Agent: fable-02-p4.  Date: 2026-07-21.  Exact integer arithmetic.

Method: n (odd, positive) is the MINIMAL element of an S-cycle iff iterating S
from n stays >= n until it returns to n.  So scanning all odd n <= N and
iterating while the value stays > n finds every S-cycle whose minimal element
is <= N.  (Values may exceed N during iteration -- Python ints are exact.)
"""
N = 10**5
STEP_CAP = 10**5

def S(x):
    y = 3 * x + 1
    y //= y & -y            # strip all factors of 2 (y & -y = 2^v2(y))
    return y

cycles = []
worst = 0
for n in range(1, N + 1, 2):
    x = S(n)
    steps = 1
    while x > n:
        x = S(x)
        steps += 1
        assert steps <= STEP_CAP, f"step cap hit at n={n} (flag for review)"
    worst = max(worst, steps)
    if x == n:              # returned to n without dipping below: cycle
        # recover the full cycle
        cyc = [n]
        y = S(n)
        while y != n:
            cyc.append(y)
            y = S(y)
        # a_i = v2(3z+1);  (y & -y) = 2^{v2(y)}, whose bit_length is v2(y)+1
        K = sum(((3 * z + 1) & -(3 * z + 1)).bit_length() - 1 for z in cyc)
        cycles.append((n, len(cyc), K, cyc if len(cyc) <= 5 else cyc[:5] + ["..."]))

print(f"S-cycle search over odd minimal elements n <= {N}:")
for n, m, K, cyc in cycles:
    print(f"  cycle found: x_min={n}, m={m}, K={K}, elements={cyc}")
print(f"cycles found: {len(cycles)} (expect exactly 1: the trivial cycle)")
print(f"max S-steps before dipping below start: {worst}")
assert cycles and cycles[0][:3] == (1, 1, 2) and len(cycles) == 1

# Consequence used in L-9910.4(iii) remark: 316^2 <= 10^5 < 317^2, so the
# search implies: any nontrivial cycle with m <= 316 has x_min > 10^5 >= m^2.
assert 316**2 <= N < 317**2
print(f"316^2 = {316**2} <= {N} < {317**2} = 317^2  (exact)")
print("RESULT: only the trivial cycle (x=1, m=1, K=2) has minimal element <= 1e5.")
```

**Output (verbatim, run 2026-07-21; < 0.1 s):**

```text
S-cycle search over odd minimal elements n <= 100000:
  cycle found: x_min=1, m=1, K=2, elements=[1]
cycles found: 1 (expect exactly 1: the trivial cycle)
max S-steps before dipping below start: 85
316^2 = 99856 <= 100000 < 100489 = 317^2  (exact)
RESULT: only the trivial cycle (x=1, m=1, K=2) has minimal element <= 1e5.
```

## Remaining uncertainty

1. **Machine-verified big-integer inequalities.** Rows $k \ge 6$ of Table 1 rest on
   exact bignum computations (largest: $3^{10781274}$, a 16.8-million-bit integer).
   The author regards these as reliable and reproducible (single stdlib operation;
   consistency cross-checks passed: incremental-vs-direct powers for $q < 10^5$,
   determinant identities, parity/alternation pattern, and agreement with the
   independent 250-digit floating guess), but they are not hand-checkable; an
   independent reviewer should re-run Script 1 (or re-verify the bit lengths with an
   independent bignum implementation) before upgrading L-9910.3.
2. **The densest spot in the Legendre proof** is Lemma A.6's unimodular-expansion case
   analysis (signs of $\mu, \nu$ vs signs of $q_i\alpha - p_i$); a verifier should
   reconstruct it independently. Same for the max-index choice in A.7 handling the
   $q_0 = q_1$ tie — this tie actually occurs for $\log_2 3$ ($a_1 = 1$).
3. **Lemma A.9's induction** (certification) has the most index bookkeeping (shifted
   strings, negative-index conventions). It is exactly the lemma that converts
   computation into proof, so it deserves priority scrutiny.
4. The **empirically boosted instance** in B.4(iii) is conditional on Script 2's
   finite search; it is labeled as such and claimed nowhere as a theorem. The
   $m \le 316$ arithmetic ($316^2 = 99856$) is exact.
5. Background analysis facts (monotonicity of $\ln$/$\exp$, $e = \sum 1/n!$) are
   assumed, not re-proved; they are itemized in the Dependency audit. If the packet
   later demands a fully formal base, they could be pushed into a foundations
   appendix.
6. The author found no gap in L-9910.2's reduction step ($q \le m$, reduced fraction,
   odd index), but notes it is the join point of all three toolkits (L-9905 import,
   A.11 estimate, A.7 Legendre) — a verifier should re-derive the chain of five
   inequalities in B.2 from scratch.

## Suggested next attack

- **L-9913 (planned; Eliahou-style length bounds):** combine Table 2 with a published,
  cited verification floor $x_{\min} > V$ (far beyond this file's self-computed
  $10^5$) to force, for every nontrivial cycle with $m \le \sqrt{V}$, the shape
  $K/m \in \{8/5, 65/41, 485/306, 24727/15601, 125743/79335, \dots\}$, then use the
  element bounds of L-9905.4 per shape to push $m$ lower bounds into the thousands.
  The CF data here (with certificates) is ready for reuse; extending Table 1 past
  $k = 14$ costs only more bignum time.
- **Refute-or-strengthen L-9910.2's threshold:** the hypothesis $x_{\min} \ge m^2$ is
  an artifact of matching $1/(3x_{\min}\ln 2)$ against $1/(2m^2)$. Any improvement of
  L-9905.5's constant (e.g. via the anchored bound of L-9905.4) weakens the needed
  hypothesis to $x_{\min} \ge c\,m^2$ with $c < 1$, enlarging the region where the
  convergent constraint bites; conversely, a verifier could look for a cycle-free
  obstruction to improving it.
- **Close the $q > 10^5$ tail:** for cycles with huge reduced denominators the table
  is silent; quantify (using A.5-style two-sided bounds $1/(q_{i+1}+q_i) < D_i <
  1/q_{i+1}$, both proved-ready from A.5's formula) how large $x_{\min}$ must be to
  force the next convergents, tying $m$-ranges to specific $q_k$.
- **Use the below-$\alpha$ convergents too:** L-9905 gives one-sided approximation
  (above), so even-index convergents are structurally excluded as shapes; a reviewer
  could try to extract additional information from how far $K/m$ must sit from the
  nearest below-$\alpha$ convergent (a semiconvergent gap statement; the near-miss
  data in Script 1 is suggestive calibration).
- **Independent re-verification:** re-run both scripts; re-prove A.6/A.9 from scratch;
  spot-check Table 1 rows $k \le 5$ by hand; attempt to break A.9 with an adversarial
  digit string whose interval does not contain $\alpha$ (the lemma then makes no
  claim — check the scripts' "between" guard catches it).

---
*File authored by fable-02-p4, 2026-07-21. Status PROPOSED per NOTATION.md conventions;
an independent reviewing agent may upgrade after verification. The correction to the
coordinator's L-9910.4(i) sketch is flagged in the Statement and proved in B.4(i).*

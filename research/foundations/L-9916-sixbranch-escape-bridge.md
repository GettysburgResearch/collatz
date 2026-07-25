# L-9916 — The six-branch chart: cylinder algebra, Fourier factorisation, and an Erdős–Turán escape bridge (with its own obstruction)

```text
Claim ID:      L-9916
Title:         Decision reduction for the six-branch rational-base chart
               (P = 3^12, Q = 2^19): exact cylinder structure of S_N, the
               Fourier factorisation of the root-class exponential sum, an
               explicit-constant Erdős-Turán emptiness criterion, and a proof
               that this criterion is self-defeating with the constants proved here.
Status:        PROVED
Authoring agent:   fable-02-p9
Reviewing agents:  fable-02-v16 (adversarial review 2026-07-25: PASS)
Created:       2026-07-25
Last updated:  2026-07-25
Dependencies:  NOTATION.md (conventions, empty sum/product, status semantics).
               Experiment X-9902 (EMPIRICAL) — used ONLY as a data gate for the
               adversarial tests (m_1..m_4 reproduced independently here); no
               statement of this file depends on X-9902.
               Everything else is self-contained: the chart, its digit algebra,
               the Fejér-kernel majorant, and the Erdős-Turán inequality are all
               constructed and proved from scratch below. L-9904.5 and
               T-7601/T-7801 are cited as CONTEXT ONLY and are never used.
Scope:         The single fixed chart P = 3^12, Q = 2^19, A as below; all
               N >= 1; all integers x_0; all frequencies h in Z; all integers
               H >= 3. Statements are fully quantified; every constant is explicit.
               L-9916.5(E) is EMPIRICAL (finite verification), clearly labelled.
               Q-9916 is an OPEN QUESTION with no direction claimed.
Related counterexample candidates: none. A positive answer to the boundedness
               branch of issue #58 would produce one explicit integer; this file
               proves no such integer exists or does not exist. It supplies the
               decision machinery and delimits exactly how far that machinery reaches.
```

---

## 0. Summary of what is and is not proved

**Proved here (complete arguments below).**

* **L-9916.1** — Exact cylinder structure: for *every* word of digits in $[0,Q)$ the
  set of integer seeds realising it is exactly one residue class mod $Q^N$, with an
  explicit representative. Counting and $m_N$ follow.
* **L-9916.2** — Nesting, monotonicity, the equivalence
  $\bigcap_N S_N \ne \emptyset \iff \sup_N m_N < \infty \iff (m_N)$ eventually
  constant, and divergence of the chart-orbit of any seed in $\bigcap_N S_N$.
  This collapses issue #58's *trichotomy* to a *dichotomy* (see §Motivation).
* **L-9916.3** — The Fourier factorisation $\widehat S_N(h) = \prod_{j<N} G_{N,j}(h)$,
  with the **corrected** pairing of inverse power of $P$ against modulus.
  **The commissioning sketch's form is wrong and is refuted numerically** (§Adversarial tests).
* **L-9916.4** — A fully self-contained Erdős–Turán / Fejér-majorant inequality with
  explicit absolute constants $C_1 = 4$ (attached to $\log(4H)/H$, not $1/H$ —
  a flagged correction) and $C_2 = 2/\pi$, and the resulting emptiness criterion.
* **L-9916.5** — (a) The trivial bound $|G| \le 6$ makes the criterion vacuous by an
  explicitly computed factor; (b) an *unconditional lower bound*
  $\sum_{h\le H} h^{-1}|\widehat S_N(h)| \ge \tfrac12\log(H/6^N)$ valid for **every**
  point set, hence (c) **the criterion of L-9916.4, with the constants proved here,
  is unsatisfiable for every $N \ge 1$** — a proved self-defeat theorem; (d) exact
  Parseval identities showing the mean square of every single-digit factor is $6$
  (so per-factor decay is impossible on average); (e) EMPIRICAL distribution of the
  single-digit factor.
* **L-9916.6** — Any element of $\bigcap_N S_N$ has a digit word that is not even
  *eventually* periodic (stronger than the requested purely periodic case).

**Not proved / open.** Whether $\bigcap_N S_N = \emptyset$. Q-9916 records the exact
low-frequency estimate that would be needed, *and* the sharp-majorant upgrade without
which the bridge cannot fire at all.

---

## Statement

Throughout, $e(t) := \exp(2\pi i t)$ for $t \in \mathbb{R}$; $\mathbb{Z}^+ = \{1,2,\dots\}$;
empty sums are $0$ and empty products are $1$ (NOTATION.md).

### D-9916.1 (the chart)

$$P := 3^{12} = 531441, \qquad Q := 2^{19} = 524288 .$$
Note $P > Q$ and $\gcd(P,Q) = 1$ ($P$ odd). Define the **chart map**
$$\mathcal{C}: \mathbb{Z} \to \mathbb{Z}, \qquad \mathcal{C}(x) := \Big\lceil \frac{P x}{Q} \Big\rceil ,$$
write $x_n := \mathcal{C}^n(x_0)$, and define the **digit**
$$a_n = a_n(x_0) := Q x_{n+1} - P x_n .$$

### D-9916.2 (the alphabet)

$$A := \{\, 7 \cdot 3^{2i} \cdot 2^{15-3i} \;:\; i = 0,\dots,5 \,\}
   = \{229376,\ 258048,\ 290304,\ 326592,\ 367416,\ 413343\},$$
and $|A| = 6$.

### D-9916.3 (legal sets and least roots)

For $N \ge 1$,
$$S_N := \{\, x_0 \in \mathbb{Z}^+ \;:\; a_0, a_1, \dots, a_{N-1} \in A \,\},
\qquad m_N := \min S_N$$
(well defined: $S_N \ne \emptyset$ by L-9916.1(6)).

### D-9916.4 (word constants, root classes, exponential sums)

For a word $w = (\alpha_0,\dots,\alpha_{N-1}) \in [0,Q)^N \cap \mathbb{Z}^N$ put
$$c_w := \sum_{j=0}^{N-1} P^{\,N-1-j} Q^{\,j} \alpha_j \in \mathbb{Z}_{\ge 0},
\qquad
r_w := \big(-P^{-N} c_w\big) \bmod Q^N \in [0, Q^N) ,$$
where $P^{-N}$ denotes any integer inverse of $P^N$ modulo $Q^N$ (it exists and $r_w$
is well defined because $\gcd(P,Q)=1$). Finally
$$\widehat S_N(h) := \sum_{w \in A^N} e\!\left(\frac{h\, r_w}{Q^N}\right), \qquad h \in \mathbb{Z}.$$

---

### L-9916.1 (cylinder structure). *For every $N \ge 1$:*

1. **(Digit range.)** For every $x \in \mathbb{Z}$, $a_0(x) = (-Px) \bmod Q \in [0,Q)$;
   in particular every $x \in \mathbb{Z}$ has a well-defined digit sequence
   $(a_n(x))_{n \ge 0} \in [0,Q)^{\mathbb{N}}$, and $x_0 \in \mathbb{Z}^+ \Rightarrow x_n \in \mathbb{Z}^+$ for all $n$.
2. **(Iterate formula.)** For every $x_0 \in \mathbb{Z}$ and $n \ge 0$,
   $x_n = \big(P^n x_0 + c_{(a_0,\dots,a_{n-1})}\big)/Q^n$.
3. **(Cylinder = residue class.)** For every word $w = (\alpha_0,\dots,\alpha_{N-1}) \in \mathbb{Z}^N$
   with all $\alpha_j \in [0,Q)$, and every $x \in \mathbb{Z}$:
   $$\big(a_0(x),\dots,a_{N-1}(x)\big) = w \iff x \equiv r_w \pmod{Q^N}.$$
   The proof shows the implication "$Q^N \mid P^N x + c_w \Rightarrow Q^{j} \mid P^{j}x + c_{w|_j}$
   for all $j \le N$", i.e. the single top-level congruence forces all intermediate ones;
   the lift parameter enters at level $j$ with the unit slope $P^{\,j}$.
4. **(Injectivity / distinctness.)** Distinct words $w \ne w' \in [0,Q)^N$ give
   $r_w \ne r_{w'}$; and the map $x \mapsto (a_n(x))_{n\ge0}$ is injective on $\mathbb{Z}$.
5. **(Nonvanishing.)** For every $w \in A^N$, $r_w \in [1, Q^N)$; indeed
   $\nu_2(c_w) = \nu_2(\alpha_0) \le 15 < 19N$.
6. **(Counting.)** $S_N$ is the disjoint union of the $6^N$ classes $r_w \bmod Q^N$,
   $w \in A^N$, intersected with $\mathbb{Z}^+$. Consequently, for every real $X \ge 0$,
   $$\big|S_N \cap [1,X]\big| \;=\; \sum_{w \in A^N} \left( \Big\lfloor \frac{X - r_w}{Q^N} \Big\rfloor + 1 \right)^{+},$$
   in particular $\big|S_N \cap [1,X]\big| = \#\{w \in A^N : r_w \le X\}$ whenever $0 \le X \le Q^N$, and
   $$m_N = \min_{w \in A^N} r_w .$$

### L-9916.2 (extraction normalisation).

1. $S_{N+1} \subseteq S_N$ for all $N \ge 1$; hence $(m_N)_{N \ge 1}$ is non-decreasing.
2. The following are equivalent: (i) $\bigcap_{N\ge1} S_N \ne \emptyset$;
   (ii) $\sup_N m_N < \infty$; (iii) $(m_N)$ is eventually constant.
   Moreover under these, $\bigcap_N S_N \ne \emptyset$ has least element $\lim_N m_N$.
3. If $x \in \bigcap_N S_N$ then for all $n \ge 0$, $x_n \in \mathbb{Z}^+$ and
   $x_n \ge (P/Q)^n x \ge (P/Q)^n$; since $P/Q = 531441/524288 > 1$, the chart-orbit
   of $x$ diverges to $+\infty$ (D-9907 sense).

### L-9916.3 (Fourier factorisation — corrected form).

For every $N \ge 1$ and every $h \in \mathbb{Z}$,
$$\boxed{\;\widehat S_N(h) \;=\; \prod_{j=0}^{N-1} G_{N,j}(h), \qquad
G_{N,j}(h) := \sum_{\alpha \in A} e\!\left(\frac{-\,h \cdot \pi_{j,N} \cdot \alpha}{Q^{\,N-j}}\right)\;}$$
where $\pi_{j,N} \in \mathbb{Z}$ is any integer with $\pi_{j,N} \cdot P^{\,j+1} \equiv 1 \pmod{Q^{\,N-j}}$.
Each summand depends only on $h\,\pi_{j,N}\alpha \bmod Q^{N-j}$, so $G_{N,j}$ is well defined,
and each $G_{N,j}$ is a $6$-term exponential sum over the geometric digit ladder $A$.
Equivalently, with $g_k(v) := \sum_{\alpha\in A} e(v\alpha/Q^k)$ (level $k \ge 1$, $v \in \mathbb{Z}$),
$$\widehat S_N(h) = \prod_{k=1}^{N} g_k\!\left(-h\,(P^{\,N-k+1})^{-1} \bmod Q^{k}\right),
\qquad \big|\widehat S_N(h)\big| = \prod_{j=0}^{N-1}\big|G_{N,j}(h)\big| .$$

> **CORRECTION (flagged, load-bearing).** The commissioning sketch proposed
> $G_j(h) = \sum_{a\in A} e(-h P^{-(j+1)} a / Q^{\,j+1})$, i.e. it paired the inverse
> power $P^{-(j+1)}$ with the modulus $Q^{\,j+1}$. **That is false.** The digit index
> $j$ carries the inverse power $P^{-(j+1)}$ but the modulus $Q^{\,N-j}$: the modulus
> level *descends* from $Q^N$ (for the first digit $j=0$) to $Q^1$ (for the last digit
> $j = N-1$), while the inverse power of $P$ *ascends*. The two indices run in opposite
> directions, so no relabelling $j \mapsto N-1-j$ repairs the sketch either. The correct
> form above is proved below and confirmed numerically to $5\cdot10^{-13}$; the sketch
> form is refuted numerically with deviations up to $2.7 \cdot 10^{2}$ (§Adversarial tests, T2).
> A structural consequence: the factors form a *triangular array* depending on both $j$
> and $N$ — there is no single $N$-independent sequence of digit factors.

### L-9916.4 (Erdős–Turán escape bridge, explicit constants).

**(a) General inequality (self-contained; proof below).** Let $R \ge 1$ and let
$\theta_1,\dots,\theta_R \in \mathbb{R}/\mathbb{Z}$ be any points (repetitions allowed),
$S(h) := \sum_{r\le R} e(h\theta_r)$. Let $I \subseteq \mathbb{R}/\mathbb{Z}$ be the image of a
half-open interval $(a, a+\beta]$ with $0 \le \beta \le 1$. Then for every integer $H \ge 3$,
$$\#\{r : \theta_r \in I\} \;\le\; R\beta \;+\; C_1\,\frac{R\,\log(4H)}{H} \;+\; C_2 \sum_{h=1}^{H} \frac{1}{h}\,\big|S(h)\big| ,
\qquad \boxed{C_1 = 4,\quad C_2 = \tfrac{2}{\pi} < 0.63662 } .$$
(Sharper form actually proved: the middle term may be replaced by
$R\cdot\big(1.70029\log(4H) + 3\big)/H$. *[verifier fable-02-v16: the coefficient printed
here was originally $1.7002$, which is very slightly below the true value
$2/\log(32/\pi^2) = 1.7002811\ldots$ and is therefore false for e.g. $H = 942$; corrected.
$C_1 = 4$ is unaffected — see the Verification note.]*)

**(b) Specialisation to the chart.** For every $N \ge 1$, every real $X$ with
$0 \le X \le Q^N$, and every integer $H \ge 3$,
$$\big|S_N \cap [1,X]\big| \;\le\; 6^N\,\frac{X}{Q^N} \;+\; \frac{4\cdot 6^N \log(4H)}{H}
\;+\; \frac{2}{\pi}\sum_{h=1}^{H}\frac{1}{h}\,\big|\widehat S_N(h)\big| .$$

**(c) Decision criterion (COROLLARY).** Fix $N \ge 1$, an integer $H \ge 3$ and a real
$f(N)$ with $0 \le f(N) \le Q^N$. If
$$6^N\,\frac{f(N)}{Q^N} \;+\; \frac{4\cdot 6^N \log(4H)}{H} \;+\; \frac{2}{\pi}\,\Sigma_N(H) \;<\; 1,
\qquad \Sigma_N(H) := \sum_{h=1}^{H}\frac{1}{h}\big|\widehat S_N(h)\big| ,$$
then $S_N \cap [1, f(N)] = \emptyset$, i.e. $m_N > f(N)$.

**(d) Escape conclusion.** If for every $B \in \mathbb{Z}^+$ there exists $N$ for which
(c) holds with $f(N) = B$, then $m_N \to \infty$ and therefore (L-9916.2)
$\bigcap_N S_N = \emptyset$: no positive integer is legal to all depths.

**(e) The inequality that must be beaten, purely in terms of the cusp sum.** With
$u := H/6^N$, (c) with $f(N)=B$ is exactly
$$\Sigma_N(H) \;<\; \frac{\pi}{2}\left(1 - \frac{6^N B}{Q^N} - \frac{4\log(4H)}{u}\right).$$

> **HONESTY FLAG, read with L-9916.5.3.** Criterion (c) is a *valid theorem*, but
> L-9916.5.3 below proves that **with the constants $C_1 = 4$, $C_2 = 2/\pi$ established
> here its hypothesis is unsatisfiable for every $N \ge 1$, every $H \ge 3$ and every
> $f(N) \ge 0$.** It becomes satisfiable *in principle* only after the middle term is
> improved from $\log(4H)/H$ to $1/H$ (a Selberg-quality majorant, not proved here), and
> even then only in the narrow window $1 < H/6^N < 19.74$, where the empirical cusp sums
> exceed the requirement by factors $8.6$ (at $N=1$) to $1.7\cdot10^3$ (at $N=6$), growing
> by roughly $3\times$ per level. See L-9916.5 and Q-9916.

### L-9916.5 (benchmark, obstruction, honesty).

1. **(Trivial-bound benchmark; PROVED + arithmetic.)** $|G_{N,j}(h)| \le 6$ for all
   $j,h$, hence $|\widehat S_N(h)| \le 6^N$ and $\Sigma_N(H) \le 6^N(1 + \log H)$.
   With $H_N := 100\,N\,6^N$ (a choice making the middle term of L-9916.4(c) at most
   $1/3$ for all $N \ge 1$; verified in the proof), the criterion
   requires $\Sigma_N(H_N) < \pi/6 = 0.5236$, whereas the trivial bound gives:

   ```text
    N |        H_N | trivial bound on Sigma_N | ratio to pi/6 (vacuity factor)
    1 |  6.000e+02 |             4.438158e+01 | 8.476e+01
    2 |  7.200e+03 |             3.557461e+02 | 6.794e+02
    3 |  6.480e+04 |             2.609077e+03 | 4.983e+03
    4 |  5.184e+05 |             1.834942e+04 | 3.504e+04
    6 |  2.799e+07 |             8.466891e+05 | 1.617e+06
   10 |  6.047e+10 |             1.561560e+09 | 2.982e+09
   20 |  7.312e+18 |             1.624654e+17 | 3.103e+17
   ```
   So the trivial bound is vacuous by a factor $\asymp 6^N N$, and *any* useful estimate
   must extract essentially all of the $6^N$.
2. **(Universal lower bound for cusp sums; PROVED, method-independent.)** For **any**
   $R \ge 1$ points $\theta_1,\dots,\theta_R \in \mathbb{R}/\mathbb{Z}$ and any integer $H \ge R$,
   $$\sum_{h=1}^{H}\frac{1}{h}\,|S(h)| \;\ge\; \frac{1}{2}\,\log\!\frac{H}{R} \, .$$
   (For $H < R$ the statement is vacuous but still true, both sides being compared to $0$.)
   In particular $\Sigma_N(H) \ge \tfrac12\log(H/6^N)$ for all $N$ and all $H \ge 6^N$.
3. **(Self-defeat theorem; PROVED.)** For every $N \ge 1$, every integer $H \ge 3$ and
   every real $f(N) \ge 0$, the left-hand side of L-9916.4(c) is $> 1$. Hence the
   criterion never fires with the constants proved in this file. Quantitatively, for
   $R = 6^N \ge 6$ and $u = H/R$,
   $$\frac{4R\log(4H)}{H} + \frac{2}{\pi}\cdot\frac{1}{2}\log\frac{H}{R} \;>\; 1
   \qquad\text{for all } u > 0 ,$$
   with minimum value $\approx 1.77$ (at $u \approx 83$ when $N = 1$), increasing in $N$.
4. **(Which constants would be needed; PROVED conditional statement.)** If the middle
   term of L-9916.4(a) is replaced by $C_1' R/H$ (Selberg-quality majorant; $C_1' = 1$,
   $C_2 = 2/\pi$ — *imported as context, not proved here, and not used anywhere*), then
   the necessary condition of 5.2 becomes $1/u + (1/\pi)\log u < 1$, which holds exactly for
   $$1 < u < u_+ , \qquad u_+ = 19.735\ldots \quad(\text{minimum } 0.68269 \text{ at } u = \pi).$$
   So *any* Erdős–Turán attack on this chart must use $H \asymp 6^N$ (within a factor
   $19.74$) and must beat $\Sigma_N(H) < \frac{\pi}{2}(1 - 6^N/H) \le \pi/2$.
5. **(Exact Parseval identities; PROVED.)** For every $k \ge 1$,
   $$\frac{1}{Q^k}\sum_{v \bmod Q^k} |g_k(v)|^2 = 6, \qquad
   \frac{1}{Q^N}\sum_{h \bmod Q^N} \big|\widehat S_N(h)\big|^2 = 6^N .$$
   Hence the root-mean-square of every single-digit factor is exactly $\sqrt 6 = 2.449$
   and that of $\widehat S_N$ is exactly $6^{N/2}$. **Consequence:** no bound of the form
   $|G_{N,j}(h)| \le 1-\delta$ can hold on average over frequencies; a successful estimate
   must be genuinely *low-frequency* (restricted to $h \le O(6^N)$, a fraction
   $O(N (6/Q)^N)$ of all frequencies) and must exploit correlations *between* levels.
6. **(E) (EMPIRICAL — finite verification, not proof.)** Exhaustive computation of the
   single-digit factor $|g_1(u)| = \big|\sum_{\alpha\in A} e(-u\alpha/Q)\big|$ over all
   $u = 1,\dots,Q-1$ ($524287$ values, script T3):

   ```text
   max     = 5.965277      (trivial ceiling 6)      min     = 0.005511
   mean    = 2.193928      median  = 2.097713       geometric mean = 1.874026
   mean of |g_1|^2 = 5.999943  (exact value over u = 0..Q-1 is 6, by L-9916.5.5)
   quantiles: 1% 0.2612 | 5% 0.5633 | 10% 0.8305 | 25% 1.3700 | 50% 2.0977
              75% 2.9270 | 90% 3.6860 | 95% 4.1433 | 99% 4.9512 | 99.9% 5.5610
   #{u : |g_1(u)| > 6(1-delta)} :
      delta=0.5   thr=3.0000  count=121271  frac=2.313e-01
      delta=0.25  thr=4.5000  count= 14074  frac=2.684e-02
      delta=0.10  thr=5.4000  count=  1200  frac=2.289e-03
      delta=0.05  thr=5.7000  count=   190  frac=3.624e-04
      delta=0.01  thr=5.9400  count=     2  frac=3.815e-06
      delta=0.001 thr=5.9940  count=     0  frac=0
   #{u : |g_1(u)| <= 1} = 74820 (14.27%);  #{u : |g_1(u)| <= 2} = 244454 (46.63%)
   ```
   **Where cancellation does and does not occur.** Near-maximal factors are genuinely
   rare (only $2$ frequencies out of $524287$ exceed $5.94$, none exceeds $5.994$), and
   $14\%$ of frequencies give a factor $\le 1$; so *pointwise* the ladder does cancel.
   But the **geometric mean is $1.874 > 1$**: a product of $N$ typical factors *grows*
   like $1.874^N$, not decays. This is the precise empirical locus of the difficulty —
   the needed estimate is not "each factor is small" (false on average, and provably so
   in mean square by 5.5) but "the specific triangular array of arguments produced by
   low $h$ conspires to be small", for which the data at $N \le 6$ show the opposite:

   ```text
   Sigma_N(H) at H = ceil(pi*6^N)  (the centre of the admissible window of 5.4).
   "requirement" = (pi/2)(1 - 6^N/H), the bar to beat under the SHARP constants of 5.4
   (under the constants proved here there is no bar to beat: the route is dead by 5.3).
    N |         H | Sigma_N(H) | lower bd (1/2)ln(H/6^N) | requirement | shortfall factor
    1 |        19 |    9.19862 |                 0.57634 |     1.07476 |  8.56
    2 |       114 |   20.93136 |                 0.57634 |     1.07476 |  19.5
    3 |       679 |   59.81735 |                 0.57267 |     1.07110 |  55.8
    4 |      4072 |  209.41372 |                 0.57243 |     1.07086 |   196
    5 |     24430 |  513.94662 |                 0.57239 |     1.07082 |   480
    6 |    146575 | 1848.43562 |                 0.57237 |     1.07080 |  1.73e+03
   ```

### Q-9916 (OPEN QUESTION; no direction claimed).

*Two linked questions.*
**(Q-9916a, the analytic estimate.)** Does there exist an absolute constant
$c$ and, for each $N$, a bound
$$\sum_{h=1}^{\lceil \pi 6^N\rceil} \frac{1}{h}\,\prod_{j=0}^{N-1}\big|G_{N,j}(h)\big| \;<\; c \;<\; \frac{\pi}{2}\Big(1 - \tfrac{1}{\pi}\Big) = 1.0708\ldots\ ?$$
Equivalently: is the union of the $6^N$ root classes $r_w \bmod Q^N$ *super-uniform at
scale $Q^N/6^N$*, in the strong sense that its low-frequency exponential sums are
$O(1)$ on average with harmonic weights? The empirical table of L-9916.5.6 says the
observed values are $8.6$–$1.7\cdot10^3$ times too large at $N \le 6$ and worsening;
no direction is claimed for $N \to \infty$.
**(Q-9916b, the majorant.)** Can the middle constant of L-9916.4(a) be brought to
$C_1' R/H$ with $C_1' \le 1$ by a fully in-repo proof (Beurling–Selberg extremal
function)? By L-9916.5.3 the bridge is *dead* without this, so Q-9916b is a strict
prerequisite for Q-9916a to be worth attacking through this route.
**Context only, no import of unproved claims:** the cusp / Fourier program of PR #16
(`93xx` namespace) is the natural source of low-frequency estimates of this shape; and
the classical Erdős–Turán inequality with constants $(1,3)$, and Selberg's majorant,
are the classical sources for Q-9916b. **Note (proved here):** with the classical
constants $(C_1',C_2) = (1,3)$ the necessary condition of L-9916.5.4 reads
$1/u + \tfrac32\log u < 1$, which has **no** solution $u \ge 1$ — so the *classical*
Erdős–Turán inequality is itself self-defeating for this problem, and only the
$C_2 = 2/\pi$ variant proved here leaves a window at all.

### L-9916.6 (aperiodicity of any seed).

Let $x \in \bigcap_{N \ge 1} S_N$ (if any exists). Then the digit word
$(a_n(x))_{n \ge 0}$ is **not eventually periodic**. In particular it is not periodic.
Quantitatively: a purely periodic digit word $w^\infty$, $w \in A^p$, $p \ge 1$, has a
unique realiser in $\mathbb{Z}_{(2)}$, namely
$$x = \frac{c_w}{Q^p - P^p} \;<\; 0 ,$$
the denominator $Q^p - P^p = 2^{19p} - 3^{12p}$ being odd (so the realiser exists as a
$2$-adic integer / rational with odd denominator) and **negative** because $P > Q$,
while $c_w > 0$.

> **Context (not used).** This is the exact analogue of the sign criterion of
> L-9904.5(2) (PROVED), where the realiser of a periodic parity word is positive iff
> $2^K > 3^a$. Here the corresponding threshold is $Q^p > P^p$, i.e. $2^{19} > 3^{12}$,
> which **fails** — $3^{12} = 531441 > 524288 = 2^{19}$. The six-branch chart is built on
> the wrong side of exactly the inequality that L-9914's certificate (C1) records.

---

## Definitions

Beyond D-9916.1–D-9916.4:

* $\lceil y \rceil$ is the least integer $\ge y$; for $y \in \mathbb{Q}$, $\lceil y\rceil$ is
  characterised by $0 \le Q\lceil y \rceil - Qy < Q$ when $y = z/Q$, $z \in \mathbb{Z}$.
* For $w \in \mathbb{Z}^N$ and $0 \le j \le N$, $w|_j := (\alpha_0,\dots,\alpha_{j-1})$ is the
  length-$j$ prefix; $w^k$ is the $k$-fold concatenation.
* $\nu_2$ is the $2$-adic valuation; $\mathbb{Z}_{(2)}$ the rationals with odd denominator.
* On $\mathbb{R}/\mathbb{Z}$, $\widehat f(h) := \int_0^1 f(\theta) e(-h\theta)\,d\theta$ and
  $(f * g)(\theta) := \int_0^1 f(t) g(\theta - t)\, dt$.
* $K_L(t) := \sum_{|h|\le L}\big(1 - \tfrac{|h|}{L+1}\big) e(ht)$ is the Fejér kernel of
  degree $L \ge 0$.
* A **trigonometric polynomial of degree $\le D$** is $\sum_{|h| \le D} c_h e(h\theta)$.

**Verification of D-9916.2.** $7\cdot 2^{15}(9/8)^i = 7\cdot 3^{2i} 2^{15-3i}$ identically,
so the two descriptions of $A$ agree; the six values are $229376, 258048, 290304, 326592,
367416, 413343$, all in $[0,Q)$ (the largest, $413343$, is $< 524288$), with
$\nu_2 = 15,12,9,6,3,0$ respectively, pairwise distinct, and $\gcd(A) = 7$. Also
$\alpha/Q = 7\cdot 9^{i}/2^{3i+4}$, so the six digits sit at the dyadic levels
$2^4, 2^7, 2^{10}, 2^{13}, 2^{16}, 2^{19}$ — this is the "geometric digit ladder".
(Machine-verified in T1.)

---

## Motivation

Issue #58 asks to decide, for this one fixed chart, whether a single positive integer is
legal at every depth. The a priori possibilities are three: (i) $\bigcap_N S_N \ne \emptyset$
(an explicit seed exists, and branch-qualified replay would yield a $K$-candidate);
(ii) $\sup_N m_N < \infty$ but $\bigcap_N S_N = \emptyset$ (small roots persist without
stabilising); (iii) $m_N \to \infty$ (escape, which eliminates the fixed six-branch
architecture). **L-9916.2 proves (ii) is empty**, so the trichotomy is a dichotomy and the
question is exactly "$\sup_N m_N < \infty$ or $m_N \to \infty$". That is the normalisation
which the repository records elsewhere as T-7601/T-7801 at other charts; it is *reproved
from scratch here* (ten lines, L-9916.2) so that nothing in this file depends on those
claims — the cross-reference is informational only, and no statement of theirs is imported.

The value of L-9916.1 is that it converts a dynamical question into a lattice-point
question: $S_N$ is *exactly* $6^N$ arithmetic progressions of common difference $Q^N$, so
$m_N$ is the minimum of $6^N$ explicit residues, and $m_N \to \infty$ is precisely the
statement that these $6^N$ residues avoid every fixed initial segment $[1,B]$ eventually.
Since $6^N \cdot B / Q^N \to 0$ superexponentially, the *expected* number of small roots
vanishes; escape is what a null model predicts (X-9902 measures $\log_{10} m_N$ growing
with slope $4.9486$ against the null slope $\log_{10}(Q/6) = 4.9414$). The obstacle is that
"expected count $\to 0$" is not a proof: one needs an equidistribution statement for the
$r_w$, and L-9916.3–4 are the standard route (factor the exponential sum, feed it into a
discrepancy inequality).

L-9916.5 then delivers the *negative* structural news, which is the main scientific content
of this file: **that route is self-defeating.** The Erdős–Turán machine pays a cost
$R/H$ for resolving an interval, so certifying an *empty* interval for an $R$-point set
requires $H \gtrsim R$; but any $R$-point set whatsoever has
$\sum_{h\le H} h^{-1}|S(h)| \ge \tfrac12\log(H/R)$, and the two requirements collide. With
the constants proved here the collision is total (L-9916.5.3); with best-possible constants
a window of width $\log 19.74$ survives, and the actual chart misses it by three orders of
magnitude at $N = 6$ and worsening. This is exactly the "precise nonreduction showing which
additional theorem is still equivalent to ordinary extraction" that issue #58's work plan
asks for at item 4: the additional theorem is **not** a low-frequency bound for a general
discrepancy argument — it is a bound strong enough to survive L-9916.5.2, which for this
point set the data contradict.

L-9916.6 removes the cheapest possible construction of a seed: no eventually periodic digit
word can be realised by a positive integer, because $3^{12} > 2^{19}$ puts the realiser on
the negative side. Any hypothetical seed is therefore aperiodic — an infinite non-repeating
object, with the attendant "unproved properties of an infinite rewrite sequence" hazard that
README §8 warns about.

---

## Proof or construction

### Proof of L-9916.1

**(1) Digit range and positivity.** For $x \in \mathbb{Z}$, $\mathcal{C}(x) = \lceil Px/Q\rceil$
is the unique integer $y$ with $0 \le Qy - Px < Q$ (indeed $y \ge Px/Q$ gives $Qy - Px \ge 0$,
and $y < Px/Q + 1$ gives $Qy - Px < Q$; conversely such $y$ is unique since the interval
$[Px/Q, Px/Q + 1)$ contains exactly one integer). Hence $a_0(x) = Qy - Px \in [0,Q)$ and
$a_0(x) \equiv -Px \pmod Q$, i.e. $a_0(x) = (-Px) \bmod Q$. If $x \ge 1$ then
$\mathcal{C}(x) \ge Px/Q > 0$, so $\mathcal{C}(x) \ge 1$; by induction all $x_n \ge 1$. $\square$

**(2) Iterate formula.** From $a_n = Qx_{n+1} - Px_n$ we get $x_{n+1} = (Px_n + a_n)/Q$.
Induct on $n$: for $n = 0$ the claim is $x_0 = (x_0 + c_{()})/1$ with $c_{()} = 0$ (empty sum).
Assume $x_n = (P^n x_0 + c_n)/Q^n$ with $c_n := c_{(a_0,\dots,a_{n-1})}$. Then
$$x_{n+1} = \frac{P x_n + a_n}{Q} = \frac{P^{n+1}x_0 + P c_n + Q^n a_n}{Q^{n+1}} ,$$
and $c_{n+1} = \sum_{j \le n} P^{n-j}Q^j a_j = P\sum_{j<n}P^{n-1-j}Q^j a_j + Q^n a_n = Pc_n + Q^n a_n$,
which is the claim. $\square$

**(3) Cylinder = residue class.** Fix $w = (\alpha_0,\dots,\alpha_{N-1})$ with $\alpha_j \in [0,Q)$
and write $E_j := P^j x + c_{w|_j}$ for $0 \le j \le N$ (so $E_0 = x$).

*Splitting identity.* For $0 \le j \le N$,
$$c_w = \sum_{i<N} P^{N-1-i}Q^i\alpha_i
= P^{N-j}\!\!\sum_{i<j} P^{j-1-i}Q^i\alpha_i \;+\; Q^j\!\!\sum_{i=j}^{N-1}P^{N-1-i}Q^{i-j}\alpha_i
= P^{N-j} c_{w|_j} + Q^j d_{j},$$
with $d_j \in \mathbb{Z}$. Hence
$$E_N \;=\; P^{N-j} E_j + Q^j d_j. \tag{$\ast$}$$

*($\Rightarrow$).* If $(a_0(x),\dots,a_{N-1}(x)) = w$ then by (2) $x_N = E_N/Q^N \in \mathbb{Z}$,
so $Q^N \mid E_N$, i.e. $P^N x \equiv -c_w$, i.e. $x \equiv -P^{-N}c_w \equiv r_w \pmod{Q^N}$
(legitimate since $\gcd(P,Q) = 1$, so $P$ — hence $P^N$ — is a unit mod $Q^N$).

*($\Leftarrow$).* Suppose $Q^N \mid E_N$. Fix $j \le N$. By $(\ast)$, $Q^j$ divides $E_N$ (as
$Q^j \mid Q^N$) and divides $Q^j d_j$, hence $Q^j \mid P^{N-j}E_j$; since $P^{N-j}$ is a unit
mod $Q^j$, $Q^j \mid E_j$. So $y_j := E_j/Q^j \in \mathbb{Z}$ for every $0 \le j \le N$, and
$y_0 = x$. Moreover $c_{w|_{j+1}} = P\,c_{w|_j} + Q^j\alpha_j$ (same computation as in (2)), so
$$Q\,y_{j+1} = \frac{E_{j+1}}{Q^{j}} = \frac{P E_j + Q^j \alpha_j}{Q^j} = P y_j + \alpha_j,$$
i.e. $Q y_{j+1} - P y_j = \alpha_j \in [0,Q)$. By the uniqueness in (1), $y_{j+1} = \mathcal{C}(y_j)$
and the digit is $\alpha_j$. Inducting from $y_0 = x$ gives $y_j = x_j$ and $a_j(x) = \alpha_j$
for $0 \le j < N$. $\square$

*(Remark on the "unit slope" mechanism.)* Writing $x = x' + Q^j t$ changes $E_j$ by $P^j Q^j t$,
i.e. changes $y_j = E_j/Q^j$ by $P^j t$; since $P^j$ is a unit mod $Q$, exactly one residue
$t \bmod Q$ produces each prescribed next digit. This is the incremental lift, and it is
what makes the level-$j$ class split into exactly $6$ level-$(j+1)$ classes.

**(4) Injectivity.** If $r_w = r_{w'}$ for $w,w' \in [0,Q)^N$, take any $x$ in that class;
by (3) its digit word equals both $w$ and $w'$, so $w = w'$ (the digit word of a given $x$
is a well-defined single object). If $x,x' \in \mathbb{Z}$ have the same infinite digit word,
then for every $N$ both lie in the class $r_{w|_N}$, so $Q^N \mid x - x'$ for all $N$; since
$Q^N \to \infty$, $x = x'$. $\square$

**(5) Nonvanishing.** For $w \in A^N$: $c_w = P^{N-1}\alpha_0 + \sum_{j\ge1}P^{N-1-j}Q^j\alpha_j$.
Every $j \ge 1$ term has $\nu_2 \ge \nu_2(Q^j) = 19j \ge 19$, while $\nu_2(P^{N-1}\alpha_0)
= \nu_2(\alpha_0) \le 15$ (the $\nu_2$ values on $A$ are $15,12,9,6,3,0$). Hence
$\nu_2(c_w) = \nu_2(\alpha_0) \le 15 < 19N$, so $Q^N \nmid c_w$, so
$r_w = (-P^{-N}c_w) \bmod Q^N \ne 0$, i.e. $r_w \in [1,Q^N)$. $\square$

**(6) Counting.** By (3) applied to each $w \in A^N$, $S_N = \mathbb{Z}^+ \cap \bigcup_{w\in A^N}
(r_w + Q^N\mathbb{Z})$, a disjoint union by (4). For $X \ge 0$ the class $r_w + Q^N\mathbb{Z}$
meets $[1,X]$ in $\lfloor (X-r_w)/Q^N\rfloor + 1$ points when $X \ge r_w$ and none otherwise
(using $1 \le r_w$ from (5)), which is the displayed formula. If $X \le Q^N$ then
$r_w + Q^N \ge 1 + Q^N > X$, so each class contributes at most its least positive
representative $r_w$; hence $|S_N\cap[1,X]| = \#\{w : r_w \le X\}$. Taking $X = Q^N$ shows
$S_N \ne \emptyset$ and $m_N = \min_w r_w$. $\square$

### Proof of L-9916.2

1. $S_{N+1}\subseteq S_N$ is immediate from the definition (a longer list of constraints).
   Hence $m_{N+1} = \min S_{N+1} \ge \min S_N = m_N$.
2. (i)$\Rightarrow$(ii): if $x \in \bigcap S_N$ then $m_N \le x$ for all $N$.
   (ii)$\Rightarrow$(iii): $(m_N)$ is a non-decreasing sequence of positive integers bounded
   above, hence takes finitely many values and is eventually constant, say $m_N = M$ for
   $N \ge N_0$. (iii)$\Rightarrow$(i): with $M$ as above, $M \in S_N$ for every $N \ge N_0$;
   and for $N < N_0$, $S_{N_0}\subseteq S_N$ gives $M \in S_N$ too. So $M \in \bigcap_N S_N$.
   Minimality: any $x \in \bigcap S_N$ has $x \ge m_N = M$ for $N \ge N_0$.
3. Let $x \in \bigcap_N S_N$. By L-9916.1(1) all $x_n \in \mathbb{Z}^+$, and by L-9916.1(2)
   $x_n = (P^n x + c_n)/Q^n$ with $c_n = \sum_{j<n}P^{n-1-j}Q^j a_j \ge 0$ (all digits lie in
   $A \subset \mathbb{Z}_{>0}$). Hence $x_n \ge (P/Q)^n x \ge (P/Q)^n$, and
   $P/Q = 531441/524288 > 1$ forces $x_n \to \infty$. $\square$

*(This is the whole normalisation: boundedness of the least roots is equivalent to the
existence of a seed, and a seed's chart-orbit necessarily diverges. Nothing outside this
file is used.)*

### Proof of L-9916.3

Fix $N \ge 1$, $h \in \mathbb{Z}$, $w = (\alpha_0,\dots,\alpha_{N-1}) \in A^N$. Since
$r_w \equiv -P^{-N}c_w \pmod{Q^N}$ and $h r_w$ enters only through $h r_w \bmod Q^N$,
$$e\!\left(\frac{h r_w}{Q^N}\right) = e\!\left(\frac{-h P^{-N} c_w}{Q^N}\right)
= e\!\left(\frac{-h P^{-N}\sum_{j<N}P^{N-1-j}Q^j\alpha_j}{Q^N}\right)
= \prod_{j=0}^{N-1} e\!\left(\frac{-h\,P^{-(j+1)}\,Q^{j}\,\alpha_j}{Q^N}\right),$$
using $P^{-N}P^{N-1-j} = P^{-(j+1)}$ (as elements of $(\mathbb{Z}/Q^N)^\times$, then lifted to any
integer representative; the value of $e(\cdot)$ is unchanged). Now
$Q^{j}/Q^{N} = 1/Q^{\,N-j}$, so the $j$-th factor is
$$e\!\left(\frac{-h\,P^{-(j+1)}\alpha_j}{Q^{\,N-j}}\right),$$
which depends only on $h P^{-(j+1)}\alpha_j \bmod Q^{\,N-j}$; and $P^{-(j+1)}$ may therefore be
taken to be any inverse $\pi_{j,N}$ of $P^{j+1}$ **modulo $Q^{N-j}$** (an inverse mod $Q^N$
reduces to one mod $Q^{N-j}$, so the two readings agree). Summing over $w \in A^N$ and
exchanging sum and product (a finite distributivity: $\sum_{(\alpha_0,\dots,\alpha_{N-1})\in A^N}
\prod_j F_j(\alpha_j) = \prod_j \sum_{\alpha\in A}F_j(\alpha)$) gives
$$\widehat S_N(h) = \prod_{j=0}^{N-1}\Big(\sum_{\alpha\in A} e\big(-h\,\pi_{j,N}\,\alpha/Q^{\,N-j}\big)\Big)
= \prod_{j=0}^{N-1}G_{N,j}(h).$$
The substitution $k := N-j$ (so $j+1 = N-k+1$) gives the level form, and
$|\widehat S_N(h)| = \prod_j |G_{N,j}(h)|$ follows from multiplicativity of $|\cdot|$. Each
$G_{N,j}$ is a sum of $|A| = 6$ unimodular terms. $\square$

**Why the sketch's form fails (structural reason).** Write $r_w$ in base $Q$ as
$\rho_0 + Q\rho_1 + \dots + Q^{N-1}\rho_{N-1}$. By the lift mechanism of L-9916.1(3), the
*first* digit $\alpha_0$ controls the *lowest* base-$Q$ place $\rho_0$ (it determines
$x \bmod Q$), and in $e(h r_w/Q^N)$ the lowest place sits at scale $Q^{0}/Q^{N} = Q^{-N}$.
So the first digit carries modulus $Q^N$, the last digit modulus $Q^1$, while the inverse
power of $P$ increases with $j$. Pairing $P^{-(j+1)}$ with $Q^{j+1}$, as the sketch does,
matches the two indices in the same direction and is wrong for every $N \ge 2$
(for $N = 1$ the two forms coincide, which is why the error is easy to miss).

### Proof of L-9916.4

Everything is proved from scratch. Fix throughout $R \ge 1$ points $\theta_1,\dots,\theta_R$
and $S(h) := \sum_r e(h\theta_r)$; note $S(0) = R$, $|S(h)| \le R$, $S(-h) = \overline{S(h)}$.

**Step 1 (Fejér kernel facts).** For an integer $L \ge 0$ let
$K_L(t) := \sum_{|h|\le L}(1 - \frac{|h|}{L+1})e(ht)$.
* (F1) $K_L(t) = \frac{1}{L+1}\big|\sum_{j=0}^{L}e(jt)\big|^2 \ge 0$. Indeed
  $\big|\sum_{j\le L}e(jt)\big|^2 = \sum_{j,k\le L}e((j-k)t) = \sum_{|h|\le L}(L+1-|h|)e(ht)$.
* (F2) $\int_0^1 K_L = 1$ (the $h = 0$ coefficient).
* (F3) For $t \notin \mathbb{Z}$: $\big|\sum_{j\le L}e(jt)\big| = \big|\frac{e((L+1)t)-1}{e(t)-1}\big|
  = \big|\frac{\sin(\pi(L+1)t)}{\sin(\pi t)}\big|$.
* (F4) For $0 < |t| \le 1/2$: $K_L(t) \le \frac{1}{4(L+1)t^2}$. [By (F1),(F3),
  $K_L(t) \le \frac{1}{(L+1)\sin^2(\pi t)}$ and $\sin(\pi|t|) \ge 2|t|$ on $[0,1/2]$ by
  concavity of $\sin$ on $[0,\pi]$ and the chord through $(0,0)$, $(1/2,1)$.]
* (F5) For $|t| \le \frac{1}{4(L+1)}$: $K_L(t) \ge \frac{8}{\pi^2}(L+1)$. [For $t = 0$ this
  reads $L+1 \ge \frac{8}{\pi^2}(L+1)$, true. For $0<|t|\le\frac1{4(L+1)}$ put
  $y := \pi(L+1)|t| \in (0,\pi/4]$; concavity of $\sin$ on $[0,\pi/2]$ and the chord to
  $(\pi/4, \frac{\sqrt2}{2})$ give $\sin y \ge \frac{2\sqrt2}{\pi}y$, while
  $\sin(\pi|t|)\le \pi|t|$; hence the ratio in (F3) is $\ge \frac{2\sqrt2}{\pi}(L+1)$ and
  $K_L(t) \ge \frac{1}{L+1}\cdot\frac{8}{\pi^2}(L+1)^2$.]

**Step 2 (a concentrated nonnegative kernel of prescribed degree).** For integers
$L \ge 1$, $m \ge 1$ set $A_{L,m} := \int_0^1 K_L^m$ and $J_{L,m} := K_L^m / A_{L,m}$.
Then $J_{L,m} \ge 0$, $\int_0^1 J_{L,m} = 1$, and $J_{L,m}$ is a trigonometric polynomial
of degree $\le mL$ (a product of $m$ polynomials of degree $\le L$). By (F5),
$$A_{L,m} \;\ge\; \int_{|t|\le \frac{1}{4(L+1)}} K_L^m \;\ge\; \frac{1}{2(L+1)}\Big(\frac{8(L+1)}{\pi^2}\Big)^{m}
= \frac{1}{2}\Big(\frac{8}{\pi^2}\Big)^m (L+1)^{m-1},$$
and by (F4), for $0 < \delta \le 1/2$,
$$\int_{\delta < |t| \le 1/2} K_L^m \;\le\; 2\int_\delta^{1/2}\frac{dt}{(4(L+1)t^2)^m}
\;\le\; \frac{2\,(4(L+1))^{-m}\,\delta^{1-2m}}{2m-1}.$$
Dividing, with $\varepsilon_{L,m}(\delta) := \int_{\delta<|t|\le 1/2}J_{L,m}$,
$$\varepsilon_{L,m}(\delta) \;\le\; \frac{4}{2m-1}\Big(\frac{\pi^2}{32}\Big)^{m}\big((L+1)\delta\big)^{1-2m}
\;\underset{\delta = 1/(L+1)}{=}\; \frac{4}{(2m-1)\,(32/\pi^2)^{m}} . \tag{4.1}$$
($32/\pi^2 = 3.24228\ldots > 1$, so the right side decays geometrically in $m$.)

**Step 3 (the majorant).** Let $I = (a,a+\beta]$ (mod $1$), $0\le\beta\le1$, let $\delta \in (0,1/2]$,
let $J$ be any nonnegative trigonometric polynomial of degree $\le D$ with $\int J = 1$, and put
$\varepsilon := \int_{\delta<|t|\le1/2} J$. Let $I_\delta := (a-\delta, a+\beta+\delta]$ (mod $1$) and
$$\Psi := \mathbf{1}_{I_\delta} * J + \varepsilon .$$
Then:
* $\Psi \ge 0$ (both terms are $\ge 0$).
* For $\theta \in I$: if $|t| \le \delta$ then $\theta - t \in I_\delta$, so
  $(\mathbf{1}_{I_\delta}*J)(\theta) \ge \int_{|t|\le\delta}J = 1 - \varepsilon$, whence $\Psi(\theta) \ge 1$.
  Thus $\Psi \ge \mathbf{1}_I$ pointwise.
* $\Psi$ is a trigonometric polynomial of degree $\le D$ with
  $\widehat\Psi(0) = |I_\delta| + \varepsilon \le \beta + 2\delta + \varepsilon$ and, for $h \ne 0$,
  $\widehat\Psi(h) = \widehat{\mathbf{1}_{I_\delta}}(h)\widehat J(h)$, so
  $$|\widehat\Psi(h)| \le \big|\widehat{\mathbf{1}_{I_\delta}}(h)\big| \le \frac{1}{\pi|h|},$$
  using $|\widehat J(h)| \le \int J = 1$ ($J\ge0$) and
  $\widehat{\mathbf 1_{(a,b]}}(h) = \frac{e(-ha)-e(-hb)}{2\pi i h}$, of modulus $\le \frac{2}{2\pi|h|}$.
  (Here $(f*g)^\wedge = \widehat f\,\widehat g$, and convolving with a degree-$D$ polynomial
  kills all coefficients with $|h| > D$.)

Therefore
$$\#\{r : \theta_r \in I\} \le \sum_{r} \Psi(\theta_r) = \sum_{|h|\le D}\widehat\Psi(h)S(h)
\le R(\beta + 2\delta + \varepsilon) + 2\sum_{h=1}^{D}\frac{1}{\pi h}|S(h)| , \tag{4.2}$$
where we used $\widehat\Psi(-h)S(-h) = \overline{\widehat\Psi(h)S(h)}$ (as $\Psi$ is real-valued)
so that the pair contributes $2\,\mathrm{Re}\big(\widehat\Psi(h)S(h)\big) \le 2|\widehat\Psi(h)||S(h)|$.

**Step 4 (choice of $L,m$; the constant $C_1 = 4$).** Let $H \ge 3$ be an integer. Put
$$m := \Big\lceil \frac{\log(4H)}{\log(32/\pi^2)}\Big\rceil \ (\ge 1), \qquad L := \lfloor H/m \rfloor .$$
*Claim: $L \ge 1$.* Since $\log(32/\pi^2) = 1.1762761\ldots$, $m \le 0.8501406\log(4H) + 1$;
for $H \ge 4$ this is $\le 0.8501406\log(4H)+1 \le H$ (at $H = 4$: $3.36 \le 4$, and the left side
grows logarithmically), and for $H = 3$ one computes $m = \lceil 2.11253\rceil = 3 = H$. So $m \le H$
and $L \ge 1$. (Machine-checked for all $3 \le H \le 19999$ and $H = 10^5,\dots,10^{16}$; T5.)

Take $J := J_{L,m}$ (degree $D := mL \le H$) and $\delta := 1/(L+1) \le 1/2$. By the choice of
$m$, $(32/\pi^2)^m \ge 4H$, so (4.1) gives $\varepsilon \le \frac{4}{(2m-1)\cdot 4H} \le \frac1H$.
And $L \ge H/m - 1$ gives $L + 1 \ge H/m$, so $2\delta \le 2m/H$. Hence
$$2\delta + \varepsilon \;\le\; \frac{2m+1}{H} \;\le\; \frac{1.70029\log(4H) + 3}{H}
\;\le\; \frac{4\log(4H)}{H},$$
the last step because $3 \le 2.29971\log(4H)$ whenever $\log(4H) \ge 1.30452$, i.e. $H \ge 1$.
*[verifier fable-02-v16: the three constants in this sentence were originally
$1.70018$, $2.29982$, $1.3045$, propagated from a $5$th-figure slip in $\log(32/\pi^2)$;
corrected above. The exact value is $2/\log(32/\pi^2) = 1.7002811\ldots$, and
$2\lceil x/\log(32/\pi^2)\rceil + 1 \le 2x/\log(32/\pi^2) + 3 < 1.70029x + 3$ for all $x>0$,
so the corrected chain is rigorous. $C_1 = 4$ is unaffected.]*
Substituting into (4.2) and enlarging the range $D \le H$ of the (nonnegative) cusp terms
proves L-9916.4(a) with $C_1 = 4$, $C_2 = 2/\pi$. $\square$

**Step 5 (specialisation, (b)–(e)).** Apply (a) with $R := 6^N$ and the points
$\theta_w := r_w/Q^N$, $w \in A^N$; then $S(h) = \widehat S_N(h)$ by definition. By L-9916.1(5)
each $r_w \in [1,Q^N)$, so for $0 \le X \le Q^N$,
$$\big|S_N\cap[1,X]\big| \;\overset{\text{L-9916.1(6)}}{=}\; \#\{w : r_w \le X\}
= \#\{w : \theta_w \in (0, X/Q^N]\},$$
an arc of length $\beta = X/Q^N \in [0,1]$. This is (b). For (c): the displayed hypothesis says
the right-hand side of (b) is $<1$; since the left-hand side is a non-negative integer, it is $0$.
(d) follows from (c) and L-9916.2: $m_N > B$ for arbitrarily large $N$ and every $B$, and $(m_N)$
is non-decreasing, so $m_N \to \infty$, so $\sup m_N = \infty$, so $\bigcap S_N = \emptyset$.
(e) is (c) rearranged, using $H = u\,6^N$. $\square$

**Verification of the choice $H_N = 100N6^N$ used in L-9916.5.1.** With $H = 100N6^N$,
$$6^N\cdot\frac{4\log(4H)}{H} = \frac{4\big(\log 400 + \log N + N\log 6\big)}{100N}
=: \phi(N).$$
$\phi(1) = 0.31133$, $\phi(2) = 0.20536$, $\phi(3) = 0.16620$, $\phi(4) = 0.14545$, and
$\phi$ is strictly decreasing on $[1,\infty)$ — writing $a := \log 400 = 5.99146$,
$b := \log 6$, $\phi(N) = \frac{4}{100}\big(\frac{a + \log N}{N} + b\big)$ has derivative
$\frac{4}{100}\cdot\frac{1 - a - \log N}{N^2} < 0$ since $a > 1$ — with
$\phi(N) \to 4\log 6/100 = 0.07167$; so $\phi(N) \le \phi(1) < 1/3$ for all $N \ge 1$. Together with $X := \lfloor Q^N/(3\cdot6^N)\rfloor$ (making the first term $\le 1/3$),
criterion (c) then reduces to $\frac{2}{\pi}\Sigma_N(H_N) < 1/3$, i.e. $\Sigma_N(H_N) < \pi/6$.

### Proof of L-9916.5

**5.1** $|G_{N,j}(h)| \le 6$ since it is a sum of $6$ unimodular terms; so
$|\widehat S_N(h)| \le 6^N$ by L-9916.3 and
$\Sigma_N(H) \le 6^N\sum_{h\le H}1/h \le 6^N(1 + \log H)$. The table is that expression at
$H = H_N = 100N6^N$, divided by $\pi/6$. (Arithmetic; script T3.)

**5.2 (universal lower bound).** Let $T(h) := \sum_{k=1}^{h}|S(k)|$, $T(0) := 0$.

*Claim A: $T(h) \ge \frac{h+1-R}{2}$ for every $h \ge 1$.* By (F1) $K_h \ge 0$ and
$K_h(0) = h+1$, so
$$\sum_{|k|\le h}\Big(1 - \frac{|k|}{h+1}\Big)|S(k)|^2
= \sum_{r,r'} K_h(\theta_r - \theta_{r'}) \;\ge\; \sum_{r} K_h(0) = R(h+1),$$
the first equality by expanding $|S(k)|^2 = \sum_{r,r'}e(k(\theta_r-\theta_{r'}))$ and the
inequality by discarding the (nonnegative) off-diagonal terms. Isolating $k=0$ and dropping the
weights $\le1$ gives $R^2 + 2\sum_{k=1}^{h}|S(k)|^2 \ge R(h+1)$, i.e.
$\sum_{k\le h}|S(k)|^2 \ge \frac{R(h+1-R)}{2}$. Since $|S(k)| \le R$,
$T(h) \ge \frac1R\sum_{k\le h}|S(k)|^2 \ge \frac{h+1-R}{2}$. Also $T(h)\ge0$ always.

*Abel summation.* For $H \ge 1$,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} = \frac{T(H)}{H} + \sum_{h=1}^{H-1}T(h)\Big(\frac1h - \frac1{h+1}\Big).$$
Assume $H \ge R$. Using $T(h)\ge 0$ for $h<R$ and Claim A for $h \ge R$,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} \;\ge\; \frac{H+1-R}{2H} + \frac12\sum_{h=R}^{H-1}\frac{h+1-R}{h(h+1)} .$$
Now $\frac{h+1-R}{h(h+1)} = \frac1h - R\big(\frac1h - \frac1{h+1}\big)$, so the sum telescopes:
$$\sum_{h=R}^{H-1}\frac{h+1-R}{h(h+1)} = \sum_{h=R}^{H-1}\frac1h - R\Big(\frac1R - \frac1H\Big)
\;\ge\; \log\frac{H}{R} - 1 + \frac{R}{H},$$
using $\sum_{h=R}^{H-1}\frac1h \ge \int_R^H \frac{dx}{x}$. Adding,
$$\sum_{h=1}^{H}\frac{|S(h)|}{h} \;\ge\; \frac{1}{2}\Big(1 - \frac RH + \frac1H + \log\frac HR - 1 + \frac RH\Big)
= \frac{1}{2}\Big(\log\frac HR + \frac1H\Big) \;\ge\; \frac12\log\frac HR . \qquad\square$$

*(Sharpness: for $R$ equally spaced points the left side equals $\sum_{k \le H/R}1/k \approx
\log(H/R)+\gamma$, so the constant $1/2$ is off by at most a factor $2$.)*

**5.3 (self-defeat).** Let $N \ge 1$, $R := 6^N \ge 6$, $H \ge 3$ an integer, $u := H/R$. The
left-hand side of L-9916.4(c) is at least
$$\Lambda := \frac{4R\log(4H)}{H} + \frac{2}{\pi}\,\Sigma_N(H) .$$
*Case $u < 1$.* Then $\frac{4R\log(4H)}{H} = \frac{4\log(4H)}{u} > 4\log(4H) \ge 4\log 12 > 9 > 1$.
*Case $u \ge 1$.* By 5.2, $\Sigma_N(H) \ge \frac12\log u$, so with $s := \log u \ge 0$ and
$H = uR \ge 6u$,
$$\Lambda \;\ge\; \frac{4\log(24u)}{u} + \frac{s}{\pi} \;=\; 4(c+s)e^{-s} + \frac{s}{\pi} =: \psi(s),
\qquad c := \log 24 = 3.17805\ldots$$
Now: for $s \in [0,2]$, $4(c+s)e^{-s}$ is decreasing (its derivative is $4e^{-s}(1-c-s) < 0$ since
$c > 1$), so $\psi(s) \ge 4(c+2)e^{-2} = 2.8033 > 1$. For $s \in [2,\pi]$,
$\psi(s) \ge 4(c+\pi)e^{-\pi} + \frac{2}{\pi} = 1.0926 + 0.6366 = 1.7292 > 1$. For $s \ge \pi$,
$\psi(s) \ge \frac{s}{\pi} + 4(c+s)e^{-s} > 1 + 0 = 1$. Hence $\Lambda > 1$ in all cases, and
adding the nonnegative term $6^Nf(N)/Q^N$ only increases the left-hand side of L-9916.4(c). $\square$

*(Numerically the minimum of $\Lambda$'s lower bound is $1.7727$ at $u \approx 83$ for $N=1$ and
increases with $N$ — $1.8478, 1.9071, 1.9562, \dots$ for $N = 2,3,4$; script T4.)*

**5.4 (which constants would be needed).** Replacing the middle term of L-9916.4(a) by
$C_1'R/H$ with $C_1' = 1$ and keeping $C_2 = 2/\pi$, the same argument gives the necessary
condition $g(u) := \frac1u + \frac{1}{\pi}\log u < 1$ for $u \ge 1$ (and $\frac1u > 1$ for $u<1$).
$g$ is smooth on $(0,\infty)$ with $g'(u) = -u^{-2} + (\pi u)^{-1}$, vanishing only at $u = \pi$,
where $g(\pi) = \frac{1+\log\pi}{\pi} = 0.682689\ldots < 1$; $g$ is strictly decreasing on
$(0,\pi)$ and strictly increasing on $(\pi,\infty)$, with $g(1) = 1$ and $g(u_+) = 1$ for a
unique $u_+ \in (\pi,\infty)$, numerically $u_+ = 19.735\ldots$. So the admissible window is
exactly $u \in (1, u_+)$. The requirement then reads
$\Sigma_N(H) < \frac{\pi}{2}\big(1 - \frac{6^NB}{Q^N} - \frac1u\big)$, which at $u = \pi$ and
$B$ fixed tends to $\frac{\pi}{2}(1 - \frac1\pi) = 1.07080\ldots$ as $N \to \infty$.
For the classical constants $(C_1',C_2) = (1,3)$ one gets instead
$\frac1u + \frac32\log u < 1$, whose left side has minimum $1$ over $u \ge 1$ attained at $u=1$
(the unconstrained minimiser is $u = 2/3 < 1$, where the lower bound of 5.2 is vacuous and the
term $1/u > 1$ takes over); hence **no** admissible $u$ exists. $\square$

**5.5 (Parseval).** For $k \ge 1$, orthogonality of additive characters mod $Q^k$ gives
$$\sum_{v \bmod Q^k}|g_k(v)|^2 = \sum_{\alpha,\alpha'\in A}\ \sum_{v \bmod Q^k}e\big(v(\alpha-\alpha')/Q^k\big)
= Q^k\,\#\{(\alpha,\alpha') : \alpha \equiv \alpha' \ (\mathrm{mod}\ Q^k)\} = 6Q^k,$$
because the six elements of $A$ lie in $[0,Q) \subseteq [0,Q^k)$ and are pairwise distinct, hence
pairwise incongruent mod $Q^k$. Identically,
$\sum_{h \bmod Q^N}|\widehat S_N(h)|^2 = Q^N\#\{(w,w') \in (A^N)^2 : r_w \equiv r_{w'}\} = 6^NQ^N$
by L-9916.1(4). $\square$

**5.6 (E)** is a finite computation; see script T3 in §Adversarial tests. It is EMPIRICAL and
is used for no deduction; the exact value $6$ for the mean square is the check that the
computation is correct (5.5), and it is reproduced to $10$ significant figures.

### Proof of L-9916.6

Let $x \in \bigcap_N S_N$ and suppose its digit word is eventually periodic: there are
$\ell \ge 0$, $p \ge 1$ with $a_{n+p}(x) = a_n(x)$ for all $n \ge \ell$. Put $y := x_\ell$, which
is a positive integer by L-9916.1(1). Since the chart is deterministic, $a_n(y) = a_{n+\ell}(x)$,
so the digit word of $y$ is purely periodic with period word $w := (a_\ell,\dots,a_{\ell+p-1}) \in A^p$.

The word of $y_p$ equals the word of $y$ (shift by a full period), so by the injectivity in
L-9916.1(4), $y_p = y$. By L-9916.1(2), $Q^p y = Q^p y_p = P^p y + c_w$, hence
$$(Q^p - P^p)\,y = c_w .$$
Now $c_w = \sum_{j<p}P^{p-1-j}Q^j\alpha_j > 0$ (all $\alpha_j \in A \subset \mathbb{Z}_{>0}$,
and the sum is nonempty as $p \ge 1$), while $Q^p - P^p = 2^{19p} - 3^{12p} < 0$ because
$P = 531441 > 524288 = Q$. Therefore $y = c_w/(Q^p-P^p) < 0$, contradicting $y \in \mathbb{Z}^+$.

Hence no such $\ell, p$ exist: the digit word of $x$ is not eventually periodic (in particular
not periodic). The displayed realiser is unique and lies in $\mathbb{Z}_{(2)}$ because
$Q^p - P^p$ is odd ($2^{19p}$ even, $3^{12p}$ odd), i.e. a $2$-adic unit; and it is negative. $\square$

*(Five-line version of the periodic case: $y_p = y \Rightarrow (Q^p-P^p)y = c_w > 0$ and
$Q^p < P^p$, so $y < 0$.)*

---

## Dependency audit

| Used | Where | How |
|---|---|---|
| NOTATION.md preamble & conventions ($\mathbb{Z}^+$, $\nu_2$, $\mathbb{Z}_{(2)}$, empty sum/product, status semantics, "computation is finite verification") | throughout | conventions only |
| NOTATION.md D-9907 (bounded/divergent) | L-9916.2(3) | terminology for "diverges" |
| X-9902 (EMPIRICAL) | §Adversarial tests only | **data gate**: its published $m_1,\dots,m_4$ are reproduced here by independent code. No statement of L-9916 depends on it. |
| L-9904.5(2) (PROVED) | boxed remark after L-9916.6 | **context only**; the analogy of sign criteria. Not used in any proof. |
| L-9914 certificate (C1) | boxed remark after L-9916.6 | **context only** (records $3^{12} > 2^{19}$; here reproved inline by direct comparison of the two integers). |
| T-7601 / T-7801 | §Motivation | **context only**, named as the repository's analogous normalisation elsewhere. L-9916.2 is proved from scratch and imports nothing. |
| PR #16 (`93xx`) cusp/Fourier program | Q-9916 | **context only**, as the natural source for Q-9916a. No claim of theirs is used. |
| Classical Erdős–Turán / Selberg majorant | L-9916.5.4, Q-9916b | **stated as an unproved import and explicitly not used**; every inequality actually applied in this file is proved in Step 1–4 of L-9916.4. |

Standard mathematics used without citation (all elementary and self-contained above):
finite geometric series; concavity of $\sin$; orthogonality of additive characters on
$\mathbb{Z}/Q^k$; Fourier inversion for trigonometric polynomials; $(f*g)^\wedge = \widehat f\widehat g$
for $f \in L^1$, $g$ a trigonometric polynomial; Abel summation; $\sum_{h=R}^{H-1}1/h \ge \log(H/R)$.

---

## Gap audit

* **Hidden finiteness.** L-9916.1–3 and .6 are stated for all $N$ / all $x$; no computation
  enters their proofs. L-9916.4 is uniform in $N, X, H$ with numerical constants. The only
  finite objects that carry weight are the six digits of $A$ (whose $\nu_2$-list is used in
  L-9916.1(5)) and the comparison $3^{12} > 2^{19}$; both are exact integer facts stated inline.
* **Unjustified induction.** The two inductions (L-9916.1(2) and the reconstruction of the
  orbit in L-9916.1(3)) have explicit base cases (empty sum $c_{()} = 0$; $y_0 = x$) and each
  step is an identity, not an estimate.
* **Boundary cases.** $N = 1$ (where the corrected and sketch Fourier forms coincide);
  $X = 0$ and $X = Q^N$ in L-9916.1(6) and L-9916.4(b); $\beta = 0$ and $\beta = 1$ in
  L-9916.4(a) (the majorant argument never divides by $\beta$, and $|I_\delta| \le \min(1,\beta+2\delta)
  \le \beta+2\delta$ covers wrap-around); $H = 3$ (smallest admissible, where $L = 1$ exactly);
  $L = 0$ is excluded because $\delta = 1/(L+1) \le 1/2$ would fail; $h < R$ in L-9916.5.2
  (handled by $T \ge 0$); $u < 1$ in L-9916.5.3 (handled separately); $p \ge 1$ and $\ell = 0$
  in L-9916.6.
* **Empirical vs universal.** Only L-9916.5.6 and the tables inside it are EMPIRICAL; they are
  labelled and are used for no deduction. The self-defeat theorem L-9916.5.3 is *not* empirical:
  it is proved for all $N, H, f(N)$. The statement "the chart's cusp sums are too large" at
  $N \le 6$ **is** empirical and is nowhere extrapolated: Q-9916 explicitly claims no direction.
* **Interchange of limits.** None taken. The only limit is $x_n \to \infty$ in L-9916.2(3),
  from a monotone explicit lower bound, and $Q^N \to \infty$ in L-9916.1(4).
* **Circularity.** L-9916.4 uses L-9916.1 and L-9916.3; L-9916.3 uses L-9916.1 and
  D-9916.4; L-9916.5 uses L-9916.3 and L-9916.4(a) but its lower bound 5.2 uses only Fejér
  positivity, so 5.3's contradiction with 5.4's requirement is not circular. Nothing in the
  file uses X-9902, T-7601/T-7801, PR #16, or L-9904.
* **Nonuniform estimates.** All constants in L-9916.4 are absolute ($4$, $2/\pi$, $1.70029$,
  $32/\pi^2$, $8/\pi^2$); none depends on $N$, $X$, $H$ or on the point set. The only
  $N$-dependent choice is $H_N$, which is displayed.
* **Assumptions equivalent to Collatz.** None. Every statement here concerns the fixed
  chart $(P,Q,A)$ and never the Collatz map; the file makes no claim about Collatz.
* **Incorrectly assumed independence.** The factorisation L-9916.3 is an *identity*, not an
  independence heuristic. Nowhere are the factors $G_{N,j}(h)$ treated as independent random
  variables; the empirical geometric-mean remark in 5.6 is explicitly flagged as descriptive
  and is used to *argue against* optimism, not for it.
* **Unproved properties of an infinite rewrite sequence.** L-9916.6 is exactly a warning of
  this type: any hypothetical seed's digit word is aperiodic, so no finite certificate of the
  usual periodic type can exist for it.
* **Finite computation extrapolated to infinite behaviour.** Explicitly avoided: the $N \le 6$
  cusp-sum table motivates Q-9916 and nothing else. The self-defeat theorem, which *is*
  asymptotic in $N$, is proved.
* **Symbolic object $\to$ actual positive integer.** L-9916.1(3)+(5) prove that every legal
  word corresponds to a genuine residue class containing positive integers, and L-9916.6 proves
  the periodic symbolic objects correspond to *negative* rationals — precisely the
  integrality/positivity obstruction README §9 demands be addressed.
* **Known weak point.** The constant $C_1 = 4$ carries a $\log(4H)$ which is almost certainly
  removable; this is what makes L-9916.5.3 as strong as it is, so an improvement there
  *weakens* the self-defeat theorem to the window statement 5.4. This is stated openly in
  Q-9916b, and both statements are proved as written.

---

## Adversarial tests

All scripts are Python 3 stdlib only, exact integer arithmetic for every decision; floats
appear only where a proved identity is checked numerically. Scripts live in the session
scratchpad `.../scratchpad/{t1_structure,t2_fourier,t3_empirical,t4_sign_and_ET,t5_selflimit}.py`
and are reproduced in the essential parts below.

### T1 — cylinder structure and the mandatory X-9902 data gate

```python
P = 3**12; Q = 2**19
A = [7 * 3**(2*i) * 2**(15-3*i) for i in range(6)]
def step(x):
    xn = -((-P * x) // Q)                 # ceil(P x / Q), exact
    return xn, Q * xn - P * x
def word(x, N):
    w = []
    for _ in range(N):
        x, d = step(x); w.append(d)
    return tuple(w)
def c_of(w):
    N = len(w); return sum(P**(N-1-j) * Q**j * w[j] for j in range(N))
def r_of(w):
    N = len(w); M = Q**N
    return (-pow(P, -N, M) * c_of(w)) % M
```

*Design note.* L-9916.1(3) is proved for **arbitrary** digit words in $[0,Q)^N$, not only for
$A$-words; that stronger form is what T1.A tests, and it is a far more searching test than
restricting to $A$ (whose classes have density $6^N/Q^N \approx 10^{-5N}$, so a blind scan
would find nothing).

```text
P = 531441  Q = 524288  P>Q: True
A = [229376, 258048, 290304, 326592, 367416, 413343]
A == 7*2^15*(9/8)^i : True
A subset [0,Q): True  nu2: [15, 12, 9, 6, 3, 0]
TEST 1.A  arbitrary-word class formula, 100000 random (x,N<=6): PASS
  N=1: 6 words, 6 distinct classes, all in [1,Q^N), replay ok
  N=2: 36 words, 36 distinct classes, all in [1,Q^N), replay ok
  N=3: 216 words, 216 distinct classes, all in [1,Q^N), replay ok
  N=4: 1296 words, 1296 distinct classes, all in [1,Q^N), replay ok
TEST 1.B  replay/distinctness/nonzero for all A-words N<=4: PASS
TEST 1.C  exhaustive x=1..3Q: observed residues == predicted 6 classes: PASS | #obs = 6
TEST 1.D  exhaustive full-period level-2 lift (6 x 2^19 scans): PASS
TEST 1.E  exhaustive full-period level-3 lift (4 random level-2 words): PASS

=== X-9902 DATA GATE ===
  m_1 = 6472   MATCH
  m_2 = 1908874353   MATCH
  m_3 = 44906374791168   MATCH
  m_4 = 275202518480529950784   MATCH
  brute-force scan x=1.. gives m_1 = 6472 MATCH
GATE: PASS
```

**GATE PASSED.** All four posted values of X-9902 are reproduced from the independently
written formula of D-9916.4 (and $m_1$ additionally by a blind scan $x = 1,2,\dots$).
Tests 1.C/1.D/1.E are *exhaustive over a full period of the lift parameter*, i.e. they verify
"cylinder $=$ residue class" as a set identity at levels $1, 2, 3$, not merely the inclusion
that a replay check would give.

### T2 — Fourier factorisation: proved form verified, sketch form refuted

Float verification of an identity proved exactly in L-9916.3 (phases computed from exact
integer residues mod $Q^{N-j}$, so the only error is $53$-bit rounding).

```text
h-range: 200 random h in [1, Q^N-1] plus h=1..10, per N
  N=2  (36 words, 210 values of h):  max|brute - PROVED product| = 1.081e-14   |   max|brute - sketch product| = 2.471e+01
  N=3  (216 words, 210 values of h): max|brute - PROVED product| = 5.695e-14   |   max|brute - sketch product| = 9.508e+01
  N=4  (1296 words, 210 values of h):max|brute - PROVED product| = 4.627e-13   |   max|brute - sketch product| = 2.708e+02
reindexed (level) form  S_N(h) = prod_{k=1}^{N} g_k(-h (P^{N-k+1})^{-1}):
  N=2 max dev 6.937e-15 | N=3 max dev 4.494e-14 | N=4 max dev 2.154e-13
```

The proved product agrees with the brute word-sum to $\le 5\cdot10^{-13}$ over $630$
frequencies; the sketch product disagrees by up to $271$ (on a quantity bounded by $6^N = 1296$).

### T3 — empirical single-digit factor and benchmarks

Output is reproduced verbatim in L-9916.5.1, 5.6. Two internal consistency checks passed:
the empirical mean square of $|g_1|$ equals the exactly predicted $6$ to $10$ significant
figures (L-9916.5.5), and $\max_u|g_1(u)| = 5.9653 < 6$ as it must be: $|g_1(u)| = 6$ would
force $Q \mid u(\alpha - \alpha')$ for all $\alpha,\alpha' \in A$, and taking
$\alpha - \alpha' = 413343 - 229376 = 183967$ (odd) this forces $2^{19} \mid u$, i.e. $u = 0$
in the tested range.

### T4 — sign of periodic realisers ($p \le 4$), kernel constants, self-limitation

```text
=== (a) L-9916.6: purely periodic digit words, p <= 4 ===
  p=1 : Q^p - P^p = -7153                      (odd, negative); 6/6 words NEGATIVE realiser
  p=2 : Q^p - P^p = -7551629537                (odd, negative); 36/36 words NEGATIVE
  p=3 : Q^p - P^p = -5979447221143249          (odd, negative); 216/216 words NEGATIVE
  p=4 : Q^p - P^p = -4208579350958186444225    (odd, negative); 1296/1296 words NEGATIVE
  congruence x = r_{w^k} mod Q^{kp} for k = 1,2 verified for all 1554 words: ok
```

The congruence check is the real content: it confirms that the negative rational
$c_w/(Q^p-P^p)$ really is the unique adic realiser of the periodic word (it satisfies every
finite cylinder congruence), so the sign statement is about the right object.

```text
=== (b) Fejer-power kernel: analytic bound (4.1) vs numerical truth ===
   L  m   delta       eps(numeric)   eps(analytic bound)    bound holds
   4  2  0.200000    5.272086e-03   1.268348e-01           True
   8  3  0.111111    1.685821e-04   2.347142e-02           True
  16  4  0.058824    6.330594e-06   5.170839e-03           True
  32  5  0.030303    2.774195e-07   1.240413e-03           True
   E(H) <= 4 ln(4H)/H, and L >= 1, verified for H = 3..19999 and H = 10^5..10^16   (T5: PASS)
```

(The analytic bound is conservative by $1$–$3$ orders of magnitude, so the constant $C_1 = 4$
is safe; a sharper kernel analysis would improve it but cannot remove the $\log$.)

```text
=== (c) self-limitation, checked against actual chart sums ===
   N |  H=ceil(pi*6^N) | Sigma_N(H) actual | lower bd (1/2)ln(H/6^N) | requirement | shortfall
   1 |              19 |           9.19862 |                 0.57634 |     1.07476 |  8.56
   2 |             114 |          20.93136 |                 0.57634 |     1.07476 |  19.5
   3 |             679 |          59.81735 |                 0.57267 |     1.07110 |  55.8
   4 |            4072 |         209.41372 |                 0.57243 |     1.07086 |   196
   5 |           24430 |         513.94662 |                 0.57239 |     1.07082 |   480
   6 |          146575 |        1848.43562 |                 0.57237 |     1.07080 |  1.73e+03
   window for u = H/6^N under sharp constants: 1 < u < 19.735, min 0.682689 at u = pi
   with the constants PROVED here: min_u [4 ln(4uR)/u + (1/pi) ln u] =
     N=1 1.7727 | N=2 1.8478 | N=3 1.9071 | N=4 1.9562 | N=6 2.0350 | N=10 2.1490   -> all > 1
```

### T5 — independent sanity checks of the two constant-bearing lemmas

```text
(1) E(H) <= 4 ln(4H)/H and L>=1 for H in 3..19999 and H = 10^5..10^16 : PASS
(2) self-limitation Sigma(H) >= (1/2) ln(H/R), R points on R/Z:
   R=  4 H=   12  lb=0.5493  min over 30 random=3.3344  perfect AP=1.8333  OK
   R= 10 H=   30  lb=0.5493  min over 30 random=8.4598  perfect AP=1.8333  OK
   R= 40 H=  800  lb=1.4979  min over 30 random=36.0218 perfect AP=3.5977  OK
   (the perfect arithmetic progression, the discrepancy-optimal configuration, attains
    sum_{k<=H/R} 1/k ~ log(H/R) + gamma, i.e. the lemma is sharp up to the factor 2)
```

### Alternate formulations tried (and what they would change)

* Replacing the additive-$\varepsilon$ majorant $\Psi = \mathbf 1_{I_\delta}*J + \varepsilon$ by the
  multiplicative one $(1-\varepsilon)^{-1}\mathbf 1_{I_\delta}*J$ gives the same $C_1$ order but
  multiplies $C_2$ by $(1-\varepsilon)^{-1}$; the additive version keeps $C_2 = 2/\pi$ exactly.
* Using the plain Fejér kernel ($m = 1$) gives $2\delta + \varepsilon \le 2/\sqrt{L+1}$, i.e.
  $C_1 R/\sqrt H$ — strictly worse, and it makes L-9916.5.3 even easier.
* A Gaussian-window kernel ($J \propto |\sum_j c_j e(jt)|^2$ with $c_j$ a Gaussian taper)
  should give $2\delta+\varepsilon \approx C\sqrt{\log R}/H$, i.e. trade the $\log H$ for a
  $\sqrt{\log R} = \sqrt{N\log 6}$; the resulting necessary condition
  $\approx 7.6\sqrt N/u + \frac1\pi\log u < 1$ is then satisfiable at $N = 1$ only.
  **This bullet is a heuristic estimate, not a proof** (the Poisson-summation wrap-around
  was not controlled), and no statement of this file rests on it; it is recorded because it
  suggests the self-defeat conclusion is robust to the choice of kernel, and that only a
  genuinely extremal (Beurling–Selberg) majorant changes the picture — which is Q-9916b.

---

## Remaining uncertainty

1. **The constant $C_1$.** I am confident the inequality with $C_1 = 4$ (and the sharper
   $(1.70029\log(4H)+3)/H$) is correct as proved, and the numerics confirm the kernel bound is
   conservative. I am *not* claiming it is optimal; I believe the $\log$ is removable by a
   Beurling–Selberg majorant, which I did not attempt to prove in-repo (it is a genuine page or
   two of extremal-function theory). **Because L-9916.5.3 leans on this $\log$, a reviewer who
   supplies the sharp majorant should expect L-9916.5.3 to degrade to the window statement
   L-9916.5.4 — which is still a strong negative, but a conditional one.** Both are stated.
2. **Scope of the self-defeat theorem.** It rules out the *specific* inequality of
   L-9916.4(c). It does **not** rule out: (a) other majorant shapes (e.g. majorising a union of
   $6^N$ classes directly rather than counting $6^N$ points against one arc); (b) second-moment
   / large-sieve arguments; (c) restricting attention to a sub-family of words; (d) lattice
   reduction. I have not tried to prove a barrier covering those, and I do not claim one.
3. **The empirical tables.** The $|g_1|$ statistics are an exhaustive computation over
   $u = 1..Q-1$ and I regard them as reliable (the exact mean-square check passes). The
   $\Sigma_N(H)$ table at $N \le 6$ is exact-argument/float-magnitude and reliable to the digits
   shown, but it is six data points; the phrase "worsening by $\approx 3\times$ per level" is a
   description of those six points and nothing more.
4. **The direction of the answer.** Nothing here indicates whether $\bigcap_N S_N$ is empty.
   X-9902's data are consistent with escape; this file proves that one natural route to
   *proving* escape does not reach.

---

## Suggested next attack

1. **(Highest value, negative direction.)** Try to upgrade L-9916.5.2 into a genuine barrier:
   show that for *any* Fourier-analytic emptiness certificate for a union of $R$ residue
   classes against an interval of length $\ll Q^N/R$, a lower bound of the shape
   "cost $\ge$ const" holds. The Fejér-positivity argument of 5.2 is the seed; the target is a
   statement covering majorants of arbitrary shape (a linear-programming duality / Selberg
   problem lower bound).
2. **(Positive direction, prerequisite.)** Prove the Beurling–Selberg majorant in-repo
   (Q-9916b). Without it the bridge is dead by L-9916.5.3; with it, the *only* thing left to
   prove is $\Sigma_N(\lceil\pi6^N\rceil) < 1.0708$, a single sharp low-frequency estimate.
3. **(Structural.)** Exploit the *triangular* nature of the array $G_{N,j}$ flagged in
   L-9916.3: at level $k = N-j$ the argument is $-h(P^{N-k+1})^{-1} \bmod Q^k$, so for fixed
   small $h$ the sequence of arguments across levels is an orbit of multiplication by $P^{-1}$
   in $(\mathbb{Z}/Q^k)^\times$. A joint equidistribution statement for that orbit against the
   geometric digit ladder $\{7\cdot9^i/2^{3i+4}\}$ is the concrete object PR #16's cusp program
   would have to supply; note $A$'s six elements sit at *six distinct dyadic scales*, so the
   factors are naturally studied $2$-adically rather than archimedeanly.
4. **(Cheap and useful.)** Extend the exact $m_N$ frontier (X-9902 suggests $m_{12}$–$m_{13}$ is
   reachable) and test the *sharper* prediction $m_N/(Q/6)^N \to \mathrm{Exp}(1)$-like scatter;
   a systematic drift downward would be the first real signal for the boundedness branch, and
   L-9916.1(6) makes that test exact rather than heuristic.
5. **(Refutation attempt on this file.)** The most likely place for an error is Step 4 of
   L-9916.4 (the interlocking of $m$, $L$, $\delta$ and the claim $L \ge 1$) and the Abel
   summation in L-9916.5.2. Both are machine-checked (T4, T5) but both are the kind of argument
   where an off-by-one changes a constant. A reviewer should also re-derive L-9916.3
   independently for $N = 2$ by hand — that single case already distinguishes the correct form
   from the sketch.

---

Signed: **fable-02-p9**, 2026-07-25.

---

## Verification note (fable-02-v16, 2026-07-25)

**Role.** Independent adversarial verifier under README §13. I did not rely on the author's
confidence, reconstructed every load-bearing argument from the statements, and wrote my own
scripts from the definitions of D-9916.1–D-9916.4 alone (scratchpad
`.../scratchpad/v{1..9}_*.py`, Python 3 stdlib only; no code was copied from §Adversarial
tests). Priority items were the four the author flagged as most likely to contain an error.

**Verdict: PASS.** Every claim L-9916.1, .2, .3, .4, .5, .6, the collision/self-defeat
conclusion, and all six reported statistical tables reproduce. Two $5$th-significant-figure
numeric slips were found and corrected inline (flagged `[verifier fable-02-v16: …]`); one of
them made a *parenthetical* sharper constant literally false. **No load-bearing statement
changes**, and in particular $C_1 = 4$, $C_2 = 2/\pi$, L-9916.5.2 and L-9916.5.3 stand.

---

### A. Reconstruction of the four priority items

**(i) L-9916.4 Step 4 — kernel interlocking, $L \ge 1$, and whether the $\log$ is forced.**
Re-derived from scratch, not read off the file. (F1)–(F5) are correct: (F4) uses
$\sin(\pi|t|)\ge 2|t|$ on $[0,\tfrac12]$ (chord under a concave arc), (F5) uses
$\sin y \ge \tfrac{2\sqrt2}{\pi}y$ on $[0,\pi/4]$ and $\sin(\pi|t|)\le\pi|t|$, giving
$K_L \ge \frac{1}{L+1}\big(\tfrac{2\sqrt2}{\pi}(L+1)\big)^2 = \tfrac{8}{\pi^2}(L+1)$. Both
verified numerically over $L = 1..39$ and $2000$ points each: **0 violations**. The mass bound
$A_{L,m} \ge \tfrac12(8/\pi^2)^m(L+1)^{m-1}$ and the tail bound
$\int_{\delta<|t|\le1/2}K_L^m \le \tfrac{2(4(L+1))^{-m}\delta^{1-2m}}{2m-1}$ divide to give
exactly (4.1); the $m=1$ boundary is safe since $\int_\delta^{1/2}t^{-2} \le \delta^{-1}$.
My independent numerical $\varepsilon$ values match T4(b) **digit for digit**
($5.272086\mathrm{e}{-3}$, $1.685821\mathrm{e}{-4}$, $6.330594\mathrm{e}{-6}$,
$2.774195\mathrm{e}{-7}$), and the analytic bound holds in every case tested including
$m=1$ and $L=1$.

*Interlocking.* $m=\lceil\log(4H)/\log(32/\pi^2)\rceil$, $L=\lfloor H/m\rfloor$,
$D = mL \le H$, $\delta = 1/(L+1) \le 1/2$. $L\ge1 \iff m \le H$; at $H=3$, $m=3=H$ exactly
(the tight boundary case, $L=1$, $\delta = 1/2$, $D=3$) and for $H\ge4$ the bound
$0.8501406\log(4H)+1 \le H$ holds and the gap widens. $(32/\pi^2)^m \ge 4H$ gives
$\varepsilon \le \frac{4}{(2m-1)4H} \le 1/H$; $L+1 \ge H/m$ gives $2\delta \le 2m/H$.
**Machine check, my code:** for every integer $H \in [3,19999]$ and
$H \in \{1,3,7\}\cdot10^k$, $k=5..16$: $L\ge1$, $mL\le H$, $\delta\le\tfrac12$, and
$2\delta+\varepsilon \le 4\log(4H)/H$ — **0 violations**, worst ratio
$\frac{2\delta+\varepsilon}{4\log(4H)/H} = 0.5103$. So $C_1=4$ has a factor-$2$ margin;
**no off-by-one exists**.

*Is the $\log$ genuinely forced by this kernel?* Yes, and I checked this rather than
accepting it. Optimising freely over $\delta = K/(L+1)$ and $m$, the budget is
$2\delta+\varepsilon \le \frac{2Km}{H} + \frac{4}{2m-1}\big(\tfrac{\pi^2}{32}\big)^mK^{1-2m}$.
Total $O(1/H)$ forces $K = O(1)$ and $(\pi^2/32)^m = O(1/H)$, i.e.
$m \gtrsim \log H/\log(32/\pi^2)$, whence the first term is $\gtrsim \log H/H$. At $m=1$ the
optimum is $\asymp H^{-1/2}$ (the file's own remark). So within the Fejér-power family the
$\log$ is unavoidable; removing it genuinely requires an extremal (Beurling–Selberg) majorant,
exactly as Q-9916b says.

*End-to-end test of L-9916.4(a).* I implemented the **statement** (not the proof) and tested it
on $3000$ random triples (point set of $R \le 25$ points — uniform, exact AP, all-coincident,
shifted lattices; arc with $\beta \in \{0,1,\mathrm{unif}\}$; $H\in[3,40]$):
**0 violations**, minimum slack $2.36$. $C_1=4$, $C_2=2/\pi$ confirmed.

**(ii) L-9916.5.2 — the universal lower bound. This is the file's most consequential claim
and it holds, universally, with no missing hypothesis.**
Reconstructed completely. Fejér positivity gives
$\sum_{|k|\le h}(1-\frac{|k|}{h+1})|S(k)|^2 = \sum_{r,r'}K_h(\theta_r-\theta_{r'}) \ge R\,K_h(0) = R(h+1)$;
isolating $k=0$ and dropping weights $\le1$ gives $\sum_{k\le h}|S(k)|^2 \ge \frac{R(h+1-R)}{2}$;
$|S(k)|\le R$ converts this to $T(h) \ge \frac{h+1-R}{2}$ (Claim A). Abel summation
$\sum_{h\le H}\frac{|S(h)|}{h} = \frac{T(H)}{H} + \sum_{h<H}T(h)(\frac1h-\frac1{h+1})$ is an
exact identity ($T(0)=0$); with $T\ge0$ below $R$, Claim A above $R$, the telescoping
$\frac{h+1-R}{h(h+1)} = \frac1h - R(\frac1h-\frac1{h+1})$ and
$\sum_{h=R}^{H-1}\frac1h \ge \log\frac HR$, the terms assemble to **exactly**
$\frac12\big(\log\frac HR + \frac1H\big) \ge \frac12\log\frac HR$. I get the same constant;
the $+\frac1H$ is real and is discarded. **No arithmetic slip.**

*Quantifiers (checked hard, as instructed).* The only hypotheses are: $R\ge1$ points on
$\mathbb{R}/\mathbb{Z}$, repetitions allowed, and $H \ge R$ an integer. Nothing about
distinctness, irrationality, spacing, or genericity enters — Claim A discards *all*
off-diagonal terms, which is legitimate only because $K_h \ge 0$, and that is unconditional.
**It is genuinely universal.** (Applied to the chart, $R=6^N$ and $H\ge6^N$ is $u\ge1$.)

*Counterexample hunt.* I ran a direct minimisation of $F(\theta)=\sum_{h\le H}|S(h)|/h$ over
point configurations: $400$ random restarts $\times$ shrinking-step coordinate descent, for
$(R,H) \in \{(2,4),(2,20),(3,9),(3,60),(4,12),(4,100),(5,25),(5,200),(6,36),(7,140),(8,64),(10,300)\}$.

```text
  R   H |   0.5ln(H/R) | exact AP  |  best found (400 restarts + descent) | ratio best/bound
   2    4 |      0.34657 |   1.50000 |                              1.50000 | 4.328
   2   20 |      1.15129 |   2.92897 |                              2.92898 | 2.544
   3    9 |      0.54931 |   1.83333 |                              1.83348 | 3.338
   3   60 |      1.49787 |   3.59774 |                              3.59908 | 2.403
   4   12 |      0.54931 |   1.83333 |                              1.83458 | 3.340
   4  100 |      1.60944 |   3.81596 |                              3.82075 | 2.374
   5   25 |      0.80472 |   2.28333 |                              2.28599 | 2.841
   5  200 |      1.84444 |   4.27854 |                              4.29725 | 2.330
   6   36 |      0.89588 |   2.45000 |                              2.45635 | 2.742
   7  140 |      1.49787 |   3.59774 |                              3.61902 | 2.416
   8   64 |      1.03972 |   2.71786 |                              2.72588 | 2.622
  10  300 |      1.70060 |   3.99499 |                              4.07689 | 2.397
```
**No configuration beats the bound**, and in every single case the numerical optimum
*coincides with the exact arithmetic progression* — the AP is the minimiser, not merely a good
example. Claim A itself was tested on $400$ mixed structured/random sets $\times$ $h\le39$:
**0 violations**, min slack $0$ (attained, so Claim A is tight).

*Sharpness.* For the exact AP, $|S(h)| = R\cdot\mathbf1_{R\mid h}$, so
$F = \sum_{j\le H/R}1/j \to \log(H/R)+\gamma$: the true constant is $1$, the proved constant
$\tfrac12$, so **sharp to a factor $2$ exactly as claimed**; the observed ratios above descend
towards $2$ as $H/R$ grows. I also note (not in the file, and it strengthens it) that *no*
universal improvement beyond factor $2$ is possible, since the AP saturates
$\sum_{k\le h}|S(k)|^2 \approx Rh$, which is precisely where Claim A is tight.

**(iii) L-9916.3 — hand derivation at $N=2$. The corrected form is right; the sketch is
genuinely wrong, not a relabelling.**
By hand: $c_w = P\alpha_0 + Q\alpha_1$, $r_w \equiv -P^{-2}c_w \pmod{Q^2}$, so
$$e\!\Big(\frac{h r_w}{Q^2}\Big) = e\!\Big(\frac{-hP^{-2}(P\alpha_0+Q\alpha_1)}{Q^2}\Big)
= \underbrace{e\!\Big(\frac{-h P^{-1}\alpha_0}{Q^{2}}\Big)}_{j=0:\ P^{-(j+1)},\ Q^{N-j}=Q^2}
\cdot \underbrace{e\!\Big(\frac{-h P^{-2}\alpha_1}{Q^{1}}\Big)}_{j=1:\ P^{-(j+1)},\ Q^{N-j}=Q^1}.$$
This is **exactly** the boxed form: digit index $j$ carries $P^{-(j+1)}$ against modulus
$Q^{N-j}$, a triangular array in $(j,N)$ with $(\text{$P$-exponent}) + (\text{$Q$-exponent}) = N+1$
constant. The sketch pairs $P^{-(j+1)}$ with $Q^{j+1}$, i.e. the two exponents *equal*. As
multisets of exponent pairs, correct $=\{(1,N),(2,N-1),\dots,(N,1)\}$ vs sketch
$=\{(1,1),\dots,(N,N)\}$; the correct multiset is invariant under $j\mapsto N-1-j$ and the
product over $j$ is symmetric, so **no relabelling can repair the sketch** — confirmed
programmatically for $N=2,3,4$. Term-by-term at $N=2$ over all $36$ words $\times$ $200$
random $h$: proved form **0 mismatches**; sketch form **1800/1800 mismatches**, max deviation
$2.0$ (the maximum possible between two unit vectors).

Numerically, $310$ frequencies per $N$ ($h=1..10$ plus $300$ random $h \in [1,Q^N)$):

```text
  N=2 (36 words):   max|brute-PROVED| = 1.08e-14 | max|brute-SKETCH| = 2.47e+01 | max|brute-LEVEL| = 1.08e-14
  N=3 (216 words):  max|brute-PROVED| = 5.22e-14 | max|brute-SKETCH| = 7.80e+01 | max|brute-LEVEL| = 5.91e-14
  N=4 (1296 words): max|brute-PROVED| = 2.90e-13 | max|brute-SKETCH| = 2.75e+02 | max|brute-LEVEL| = 3.02e-13
  N=1: proved and sketch coincide identically (max difference 0.0), as the file says.
```
Confirms the file's T2 (its sketch-deviation maxima $2.471\mathrm{e}1$, $9.508\mathrm{e}1$,
$2.708\mathrm{e}2$ are sample-dependent maxima; mine are $2.47\mathrm{e}1$, $7.80\mathrm{e}1$,
$2.75\mathrm{e}2$ from an independent seed — same conclusion, deviations $\sim2.7\cdot10^2$
on a quantity bounded by $6^4 = 1296$). The level form
$\widehat S_N(h)=\prod_{k\le N}g_k(-h(P^{N-k+1})^{-1})$ also verifies.

**(iv) The case split in §5.3.** Both branches check.
*$u<1$:* $\frac{4R\log(4H)}{H} = \frac{4\log(4H)}{u} > 4\log(4H) \ge 4\log12 = 9.9396 > 1$
(uses only $H\ge3$; the 5.2 lower bound is *not* invoked here, which is exactly right since
5.2 needs $H\ge R$). *$u\ge1$:* 5.2 applies, $H = uR \ge 6u$, and
$\psi(s) = 4(c+s)e^{-s}+s/\pi$, $c=\log24$. I re-derived and re-checked each of the three
sub-intervals: $\psi \ge 4(c+2)e^{-2} = 2.8031$ on $[0,2]$ (monotone since $c>1$);
$\ge 4(c+\pi)e^{-\pi} + 2/\pi = 1.0924+0.6366 = 1.7290$ on $[2,\pi]$; $> 1$ for $s\ge\pi$.
Global minimum of $\psi$ by dense scan: $1.7727$ at $s=4.4174$ ($u = 82.9$) — the file's
"$\approx1.77$ at $u\approx83$". **The split is exhaustive and each branch is correct.**

---

### B. The collision claim — all three statements confirmed

I re-derived the arithmetic independently. Writing $\Lambda(N,H)$ for the proved lower bound on
the LHS of L-9916.4(c) and searching **over exact integers $H$** (not the continuous relaxation):

```text
  N= 1  min_H Lambda = 1.7727 at H=497   (u=82.8)      N= 3  min = 1.9071 at H=28932  (u=133.9)
  N= 2  min_H Lambda = 1.8478 at H=3917  (u=108.8)     N= 4  min = 1.9562 at H=205523 (u=158.6)
  continuous minima of 4 ln(4uR)/u + (1/pi) ln u :  N=1 1.7727 | N=2 1.8478 | N=3 1.9071
                                                    N=4 1.9562 | N=6 2.0350 | N=10 2.1490
```

1. **With the proved constants ($C_1=4$ on $\log(4H)/H$, $C_2=2/\pi$) the hypothesis of
   L-9916.4(c) is unsatisfiable for every $N\ge1$, every integer $H\ge3$, every $f(N)\ge0$.**
   CONFIRMED — the LHS exceeds $1$ by a factor $\ge 1.77$, increasing in $N$. Values reproduce
   the file's $1.7727, 1.8478, 1.9071, 1.9562, 2.0350, 2.1490$ exactly.
2. **Classical $(C_1',C_2)=(1,3)$ also fails.** CONFIRMED: the necessary condition is
   $1/u + \tfrac32\log u < 1$; on $u\ge1$ the left side is increasing (the unconstrained
   minimiser is $u=2/3<1$, outside the range where 5.2 applies) with value exactly $1$ at
   $u=1$, so no $u\ge1$ qualifies; and $u<1$ gives $1/u>1$. Exhaustive scan: no solution.
3. **Only a Selberg-quality $(1, 2/\pi)$ pair leaves a window, and it is exactly
   $1 < H/6^N < 19.735$.** CONFIRMED. $g(u)=1/u+\frac1\pi\log u$ has
   $g(1) = 1.0000000000$ exactly (so $u=1$ is excluded and the window is **open** at the left —
   the file's strict "$1<u$" is right), unique interior minimum
   $g(\pi) = \frac{1+\log\pi}{\pi} = 0.682689$, and I locate the upper root by $200$-step
   bisection at
   $$u_+ = 19.735236\ldots$$
   confirming the file's $19.735\ldots$ to all printed digits. ($g(19.735)=0.9999968<1$,
   $g(19.7353)>1$.)

The downstream numbers also check: requirement $\frac\pi2(1-6^N/H) \to \frac\pi2(1-\frac1\pi)
= 1.07080$ at $u=\pi$, and the $H_N = 100N6^N$ calibration
($\phi(1)=0.31133$, $\phi(2)=0.20536$, $\phi(3)=0.16620$, $\phi(4)=0.14545$, limit $0.07167$,
$\phi$ decreasing since $\log400 > 1$; all $<1/3$) reproduces, as does the whole 5.1
vacuity table ($8.476\mathrm{e}1, 6.794\mathrm{e}2, 4.983\mathrm{e}3, 3.504\mathrm{e}4,
1.617\mathrm{e}6, 2.982\mathrm{e}9, 3.103\mathrm{e}17$).

---

### C. Remaining claims (.1, .2, .6)

* **L-9916.1.** All six parts reconstructed. (1) $\lceil Px/Q\rceil$ is the unique $y$ with
  $0\le Qy-Px<Q$; (2) the induction $c_{n+1}=Pc_n+Q^na_n$ is an identity; (3) the splitting
  identity $c_w = P^{N-j}c_{w|_j}+Q^jd_j$ is correct term-by-term
  ($N-1-i = (N-j)+(j-1-i)$ for $i<j$), so $E_N = P^{N-j}E_j + Q^jd_j$, and $\gcd(P,Q)=1$
  turns the single top-level congruence into all intermediate ones — the $(\Leftarrow)$
  direction is the real content and it is complete, including the digit-uniqueness step
  $Qy_{j+1}-Py_j = \alpha_j \in [0,Q)$. (4) injectivity, (5) $\nu_2(c_w)=\nu_2(\alpha_0)\le15<19N$
  because every $j\ge1$ term has $\nu_2\ge19$ and the minimum is therefore *unique*, (6) the
  counting formula and its positive part all check, including $X<r_w$ and $X=Q^N$.
  **Computationally:** I verified "cylinder = one residue class" for **arbitrary** words in
  $[0,Q)^N$ (not just $A$-words) on $4000$ random $(w,N\le5)$ including negative shifts and
  wrong-class negatives — PASS; and exhaustively over all of $\mathbb{Z}/Q$ at level 1.
* **X-9902 data gate.** Reproduced by **two independent methods**: (a) my own $r_w$ formula,
  (b) an incremental-lift search that uses *only the forward chart map* (solving one linear
  congruence per level, never touching $c_w$/$r_w$), plus (c) a blind scan $x=1,2,\dots$ for
  $m_1$. All three agree:
  ```text
  m_1 = 6472                     MATCH      m_3 = 44906374791168            MATCH
  m_2 = 1908874353               MATCH      m_4 = 275202518480529950784     MATCH
  ```
  At each level $N\le4$ the class count is exactly $6^N$, all classes distinct, all in
  $[1,Q^N)$, and every representative replays to its intended $A$-word. **GATE: PASS.**
* **L-9916.2.** Correct. $S_{N+1}\subseteq S_N$ is immediate; (ii)$\Rightarrow$(iii) is
  "non-decreasing integer sequence, bounded"; (iii)$\Rightarrow$(i) needs
  $M \in S_N$ for $N<N_0$, supplied by $S_{N_0}\subseteq S_N$. So **the branch "$\sup m_N<\infty$
  but $\bigcap S_N=\emptyset$" is provably empty** and issue #58's trichotomy really is a
  dichotomy. Divergence: $c_n\ge0$ gives $x_n \ge (P/Q)^nx$ with $P/Q = 531441/524288>1$. Sound.
* **L-9916.6.** Correct and the argument is tight. Eventual periodicity is reduced to pure
  periodicity by passing to $y=x_\ell$; $y_p=y$ follows from injectivity of the *infinite*
  digit word (L-9916.1(4)), then $(Q^p-P^p)y = c_w$ with $c_w>0$ and
  $Q^p-P^p = 2^{19p}-3^{12p} < 0$ odd. Verified: $-7153$, $-7551629537$,
  $-5979447221143249$, $-4208579350958186444225$ — all odd, all negative. The conclusion
  (no seed has an even eventually-periodic digit word) holds.
* **L-9916.5.5 (Parseval).** Correct: the six elements of $A$ lie in $[0,Q)\subseteq[0,Q^k)$
  and are pairwise distinct hence pairwise incongruent mod $Q^k$, giving exactly $6Q^k$.
  My exhaustive computation returns mean of $|g_1|^2$ over $u=0..Q-1$ equal to
  $6.0000000000$ — the exact value, to $11$ figures.

---

### D. Independently recomputed statistics, side by side

Exhaustive over all $u=1,\dots,Q-1$ ($524287$ values), my own code:

| quantity | file | fable-02-v16 | agree |
|---|---|---|---|
| $\max\lvert g_1\rvert$ | 5.965277 | **5.965277** | ✓ |
| $\min\lvert g_1\rvert$ | 0.005511 | **0.005511** | ✓ |
| mean | 2.193928 | **2.193928** | ✓ |
| median | 2.097713 | **2.097713** | ✓ |
| geometric mean | 1.874026 | **1.874026** | ✓ |
| mean of $\lvert g_1\rvert^2$ (over $u=1..Q-1$) | 5.999943 | **5.999943** | ✓ |
| mean of $\lvert g_1\rvert^2$ (over $u=0..Q-1$, exact $=6$) | 6 | **6.0000000000** | ✓ |
| quantiles 1/5/10/25/50/75/90/95/99/99.9 % | .2612 .5633 .8305 1.3700 2.0977 2.9270 3.6860 4.1433 4.9512 5.5610 | **identical** | ✓ |
| exceedances $\delta=.5/.25/.10/.05/.01/.001$ | 121271 / 14074 / 1200 / 190 / 2 / 0 | **121271 / 14074 / 1200 / 190 / 2 / 0** | ✓ |
| exceedance fractions | 2.313e-1, 2.684e-2, 2.289e-3, 3.624e-4, 3.815e-6, 0 | **2.3131e-1, 2.6844e-2, 2.2888e-3, 3.6240e-4, 3.8147e-6, 0** | ✓ |
| $\#\{\lvert g_1\rvert\le1\}$, $\#\{\le2\}$ | 74820 (14.27%), 244454 (46.63%) | **74820 (14.27%), 244454 (46.63%)** | ✓ |

Measured cusp sums at $H=\lceil\pi6^N\rceil$, my own code (product form, cross-checked at
$N=1,2$ against the brute word-sum over the whole range — difference $0.00\mathrm{e}{+}00$):

| $N$ | $H$ | file $\Sigma_N(H)$ | mine | lower bd $\tfrac12\ln(H/6^N)$ | requirement | shortfall |
|---|---|---|---|---|---|---|
| 1 | 19 | 9.19862 | **9.19862** | 0.57634 | 1.07476 | 8.56 |
| 2 | 114 | 20.93136 | **20.93136** | 0.57634 | 1.07476 | 19.5 |
| 3 | 679 | 59.81735 | **59.81735** | 0.57267 | 1.07110 | 55.8 |
| 4 | 4072 | 209.41372 | **209.41372** | 0.57243 | 1.07086 | 196 |
| 5 | 24430 | 513.94662 | **513.94662** | 0.57238 | 1.07082 | 480 |
| 6 | 146575 | 1848.43562 | **1848.43562** | 0.57237 | 1.07080 | 1.73e+03 |

(Only cosmetic difference in the whole table: the file prints the $N=5$ lower bound as
$0.57239$, mine rounds to $0.57238$.) **Every statistic in this file reproduces.**

**Sanity-check of the geometric-mean interpretation (requested).** The file explains growth of
$\prod_j|G_{N,j}(h)|$ by "geometric mean $1.874>1$". I stress-tested this rather than accepting
it, and it is *better* founded than the file claims:
* the geometric mean of $|g_k|$ over uniform $v \bmod Q^k$ is $1.8728, 1.8725, 1.8743, 1.8727$
  for $k=1,2,3,4$ — **level-independent**, so the ladder behaves the same at every modulus level;
* the per-level geometric mean actually realised in the **low-frequency window** that matters,
  $\big(\mathrm{GM}_{h\le\lceil\pi6^N\rceil}|\widehat S_N(h)|\big)^{1/N}$, is
  $1.8791, 1.8782, 1.8732, 1.8741$ for $N=3,4,5,6$ — i.e. it converges to the same $1.874$.
  The heuristic is therefore *quantitatively* correct on exactly the frequency range the
  bridge would need, not merely a global average;
* $1.874$ is essentially the pure-noise value: six random unit vectors give
  $\sqrt6\,e^{-\gamma/2} = 1.8354$. So the correct reading is "the digit ladder is no better
  than random, and random already grows" — consistent with the exact mean square $6$ of 5.5.
* One caveat I add: $\Sigma_N$ grows by $\approx 3\times$ per level, *faster* than $1.874$,
  because $\Sigma_N$ is an arithmetic (not geometric) average and is dominated by the large
  values. So the geometric-mean story **understates** the obstruction; it is conservative, and
  using it as the file does (to argue *against* optimism) is legitimate.

---

### E. Defects found, and their exact scope

1. **[corrected inline] $\log(32/\pi^2)$ printed as $1.176347$; true value $1.1762761\ldots$**
   ($32/\pi^2 = 3.2422778766$). This propagated to three derived constants in Step 4 of
   L-9916.4 and one in L-9916.4(a):
   * $m \le 0.85009\log(4H)+1$ → true bound needs $0.8501406$;
   * $2m+1 \le 1.70018\log(4H)+3$ → true coefficient $2/\log(32/\pi^2) = 1.7002811$;
   * the parenthetical "sharper form" in L-9916.4(a), $R(1.7002\log(4H)+3)/H$;
   * $3 \le 2.29982\log(4H)$ for $\log(4H)\ge1.3045$.

   **Severity.** The first, second and fourth are intermediate steps and the chain still
   closes; but the third is a *displayed inequality of the file* and is **literally false**:
   with $C=1.7002$ I find $89$ counterexamples in $H\le3\cdot10^5$, the first at
   $\mathbf{H=942}$ (also $3054$, $9900$, …). With $C=1.70029$ there are **none**, and
   rigorously $2\lceil x/\log(32/\pi^2)\rceil+1 \le 2x/\log(32/\pi^2)+3 < 1.70029x+3$ for all
   $x>0$. I have corrected all four constants in place, flagged as verifier edits.
   **Nothing downstream changes:** $C_1 = 4$ needs only
   $4 \ge 1.7002811 + 3/\log(4H)$, true for all $H\ge1$ (and with a factor-$2$ empirical
   margin, worst measured ratio $0.5103$). L-9916.4(b)–(e), L-9916.5.1–5.6 and the
   self-defeat theorem are untouched.
2. **[cosmetic, corrected]** $m=\lceil2.1124\rceil$ at $H=3$ → the quotient is $2.11253$
   (the ceiling, $3$, and hence $L=1$, are unchanged).
3. **[cosmetic, not corrected]** L-9916.5.2's parenthetical says that for $H<R$ the statement
   is "vacuous but still true, both sides being compared to $0$". It is simply *true*, because
   the right side $\tfrac12\log(H/R)$ is negative while the left side is $\ge0$; "vacuous" is
   the wrong word but the claim is fine.
4. **[sample-dependent, not a defect]** The sketch-form deviations in T2 ($2.471\mathrm{e}1$,
   $9.508\mathrm{e}1$, $2.708\mathrm{e}2$) depend on the random frequency sample; an
   independent seed gives $2.47\mathrm{e}1$, $7.80\mathrm{e}1$, $2.75\mathrm{e}2$. The
   refutation of the sketch is unaffected (it fails *term by term*, at every word and every
   frequency with $N\ge2$).

**No substantive gap was found.** In particular I specifically could not break: the universality
of L-9916.5.2 (no missing hypothesis; extensive optimisation found no counterexample and
identified the AP as the true minimiser), the $L\ge1$/degree/$\delta$ interlocking of Step 4
(exhaustively machine-checked over the same and wider ranges with my own code), the $N=2$
Fourier derivation (done by hand, matches the boxed form), or the $u<1$ / $u\ge1$ case split.

### F. Caveats on the *scope* of the negative result (not defects — the file states these,
and I confirm they are stated accurately)

The self-defeat theorem closes **one specific inequality**: L-9916.4(c) applied with $R=6^N$
points against one arc, with the constants proved here. It does **not** show that
$\bigcap_N S_N = \emptyset$ is unprovable, nor that Fourier methods fail in general. The file's
Remaining uncertainty §2 lists exactly the escapes (other majorant shapes, second-moment /
large-sieve, sub-families of words, lattice reduction), and Q-9916b correctly identifies the
Beurling–Selberg majorant as the strict prerequisite for the route to be worth attacking at
all. A reader should note the honest asymmetry the file itself flags: **improving $C_1$ weakens
L-9916.5.3 to the conditional window statement L-9916.5.4.** Both are proved as written.

### G. Reproduction

Scripts (my own, written from the statements; Python 3 stdlib only, exact integer arithmetic
for every decision, floats only where a proved identity is checked numerically) live at
`.../scratchpad/v1_gate.py` (structure + X-9902 gate, two independent methods),
`v2_fourier.py` (proved vs sketch factorisation, hand $N=2$ check),
`v3_stats.py` (exhaustive $|g_1|$ statistics), `v4_cusp.py` ($\Sigma_N$, $N\le6$),
`v5_collision.py` (self-defeat minima, window endpoints, kernel constants),
`v6_lowerbound.py` (adversarial minimisation against 5.2), `v7_gm.py` (constant precision,
geometric-mean interpretation), `v8_tables.py` (5.1 table, $\phi(N)$, (F4)/(F5)),
`v9_et.py` (end-to-end test of L-9916.4(a) and of (4.1)).
Run: `python3 vK_*.py`. No seeds are load-bearing; where randomness is used the seed is fixed
in the script and the conclusion is a max/min over the sample.

**Status upgraded PROPOSED → PROVED** per NOTATION.md conventions and README §7.
`INDEPENDENTLY_VERIFIED` is deliberately **not** set: that requires a second independent agent.

Signed: **fable-02-v16**, adversarial verifier, 2026-07-25.

# An exact Poisson-kernel identity for the Syracuse transfer operator

**Continued in** [`../syracuse-critical-cascade`](../syracuse-critical-cascade/README.md): singular value decomposition, selection rule, pair operator, renewal law, and data to level 18. With level 18 the extrapolation in section 6 below becomes $a_\infty\approx0.475$, inside the uncertainty stated there.

**Status:** PROPOSED. Self-checked only; no independent review. Theorems 1–3 have complete short proofs below. Sections 5 and 6 are EMPIRICAL or conjectural and are labelled so. Nothing here proves or disproves Collatz, and nothing here controls an individual orbit.

**Map and normalization:** the odd-to-odd Syracuse map, through Tao's Syracuse random variables. Let $a_1,a_2,\dots$ be i.i.d. with $P(a=k)=2^{-k}$, $k\ge1$, and

$$X=\sum_{i\ge1}3^{i-1}2^{-(a_1+\cdots+a_i)}\in\mathbb Z_3 ,\qquad \mu=\text{law of }X,\qquad \mu_n(x)=\mu(x+3^n\mathbb Z_3)=P(\mathrm{Syrac}(\mathbb Z/3^n\mathbb Z)=x).$$

$m$ is Haar measure on $\mathbb Z_3$ with mass 1, $f_n=3^n\mu_n$ is the level-$n$ density, and $\langle\cdot,\cdot\rangle$ is the inner product of $L^2(m)$. Everything is a statement about $\mu$, a measure on 3-adic integers. No statement is about an ordinary positive integer orbit.

**Dependencies:** Theorems 1, 2 and 3(a) use only the definitions. Theorem 3(b) uses Tao's fine-scale mixing (Forum Math. Pi 10 (2022), Proposition 1.14) through one consequence, $\mu\ll m$.

**Evidence:** [`verify_exact.py`](../../experiments/X-SYR-001-poisson-identity/verify_exact.py) checks Theorem 1, Theorem 2(1)–(2) and the $qx+1$ variant of section 7 in exact rational arithmetic at small levels. [`numerics.py`](../../experiments/X-SYR-001-poisson-identity/numerics.py) is binary64 at levels up to 13, with a recorded run to level 17. Finite checks do not prove the theorems; the proofs below do.

**First unsupported step:** Conjecture C1 in section 6, the linear upper bound for $Q_n$.

## Prior work, and what is and is not new

- Tao's fine-scale mixing estimate says $\lVert f_n-f_m\rVert_{L^1}\ll_A m^{-A}$ for $n\ge m$. So $f_n$ converges in $L^1$ and $\mu$ has a density $f$.
- Tao's 2020 post *Equidistribution of Syracuse random variables and density of Collatz preimages* asks whether $\min_x\mu_n(x)=3^{-n+o(n)}$.
- N. El Jaouhari, *Uniform Syracuse atoms and exact density regularity with quantitative Collatz predecessor counts*, Zenodo [10.5281/zenodo.23377671](https://doi.org/10.5281/zenodo.23377671), v1 dated 14 October 2026, states that $f\in L^q$ exactly for $q<2$ (its Theorem B). It also gives a linear lower bound and a quadratic upper bound for the collision energy and lists a matching linear upper bound as open. For this note the record and the first third of its TeX source were read through an automated fetch; the energy bounds come from an automated summary of the rest. Its proofs and its Lean development were not checked.

So the statement "the Syracuse density is not in $L^2$" is **not new here**. It was found independently in the session that produced this note, on 9 November 2026, and the preprint was located afterwards. What could not be found there or elsewhere, after web searches and a keyword check of that source, is: Theorem 1 and the exact singular values; Theorem 2(1)–(2); the proof of Theorem 3(a), which uses neither the minimum-atom bound nor Tao's estimate; the formula and numerical value of the growth constant; and the flat-kernel observation of section 5. This is a search result, not a priority claim.

## 1. Summary

The transfer operator of the Syracuse measure is

$$(\mathcal Lg)(x)=3\sum_{a\ge1,\ 2^ax\equiv1\ (3)}2^{-a}\,g\Big(\frac{2^ax-1}{3}\Big),\qquad f_n=\mathcal L^n1 .$$

Let $A(y)=4y+1$ and $(Vg)(y)=g(Ay)$. Then, exactly,

$$\mathcal L^*\mathcal L=\sum_{j\in\mathbb Z}4^{-|j|}V^j .$$

$A$ is an odometer on $\mathbb Z_3$, so $V$ is diagonal in an explicit basis and $\mathcal L^*\mathcal L$ is the Poisson kernel $P_{1/4}$ evaluated on it. The coefficient of $V^0$ is 1 because $\sum_a4^{-a}=1/3$, that is, because $2^2-1=3$. That is the precise sense in which the Syracuse measure is $L^2$-critical: the diagonal conserves energy exactly, and all growth of $\lVert f_n\rVert_2^2$ comes from correlations of $f_n$ with its translates along the odometer.

## 2. Theorem 1

**Theorem 1.** For $g,h\in L^2(m)$,

$$\langle\mathcal Lg,\mathcal Lh\rangle=\sum_{j\in\mathbb Z}4^{-|j|}\langle g,\,h\circ A^j\rangle .$$

*Proof.* Put $\varphi_a(y)=2^{-a}(1+3y)$. It is an injective affine map of $\mathbb Z_3$ that scales $m$ by $1/3$, with image $I_a=\{x:2^ax\equiv1\ (3)\}$ and inverse $x\mapsto(2^ax-1)/3$. With $(U_ag)(x)=3\cdot\mathbf 1_{I_a}(x)\,g(\varphi_a^{-1}x)$ we have $\mathcal L=\sum_a2^{-a}U_a$. Substituting $x=\varphi_a(y)$,

$$\langle U_ag,U_bh\rangle=3\int_{\{y:\ \varphi_a(y)\in I_b\}}g(y)\,\overline{h(\varphi_b^{-1}\varphi_ay)}\,dm(y).$$

$\varphi_a(y)\in I_b$ means $2^{b-a}(1+3y)\equiv1\pmod 3$, which holds for all $y$ if $b-a$ is even and for none if it is odd. If $b-a=2j$ then $\varphi_b^{-1}\varphi_a(y)=(4^j(1+3y)-1)/3=A^j(y)$. Finally $\sum_{a,b\ge1,\ b-a=2j}2^{-a-b}=4^{-|j|}/3$, and the factor 3 cancels. $\qquad\blacksquare$

**Corollaries.**

1. $A$ acts on $\mathbb Z/3^k$ as a single cycle of length $3^k$ (its multiplier is $1$ mod $3$ and its increment is a unit). So on the level-$k$ functions $H_k$ the operator $V$ is a cyclic shift, with simple eigenvalues $e(r/3^k)$, and
   $$\operatorname{spec}\big(\mathcal L^*\mathcal L\big|_{H_k}\big)=\Big\{\frac{15}{17-8\cos(2\pi r/3^k)}:\ r\bmod 3^k\Big\}.$$
2. $\lVert\mathcal L\rVert_{L^2\to L^2}=\sqrt{5/3}$, and $\lVert\mathcal Lg\rVert_2^2\ge\tfrac35\lVert g\rVert_2^2$.
3. $\mathcal LH_k\subset H_{k+1}$ and $E_{k+1}\mathcal L=\mathcal LE_k$, where $E_k$ is conditional expectation onto $H_k$. The details $d_k=f_{k+1}-f_k$ satisfy $d_k=\mathcal Ld_{k-1}$.

## 3. Theorem 2: the energy recursion

Let $X,\tilde X$ be independent with law $\mu$, and

$$Q_n=\lVert f_n\rVert_2^2=3^nP(X\equiv\tilde X\ (3^n)),\qquad \gamma_n(j)=\langle f_n,f_n\circ A^j\rangle=3^nP\big(\tilde X\equiv4^jX+\tfrac{4^j-1}{3}\ (3^n)\big),\qquad a_n=Q_{n+1}-Q_n .$$

**Theorem 2.**

1. $Q_{n+1}=\sum_{j\in\mathbb Z}4^{-|j|}\gamma_n(j)$, so $a_n=\sum_{j\ne0}4^{-|j|}\gamma_n(j)$.
2. $\gamma_n\ge0$ is $3^n$-periodic, and $\sum_{j\bmod 3^n,\ 3^v\mid j}\gamma_n(j)=3^{n-v}Q_v$ for $0\le v\le n$. In particular the mean of $\gamma_n(j)$ over $j\not\equiv0\pmod 3$ is exactly $2/3$, and over $\{j:v_3(j)=v\}$ it is $Q_v-a_v/2$.
3. $a_n=\sum|\hat\mu(\zeta)|^2$ over additive frequencies $\zeta\in\mathbb Z[1/3]/\mathbb Z$ of exact level $n+1$.
4. $\tfrac35a_{n-1}<a_n<\tfrac53a_{n-1}$, with $a_0=\tfrac23$, $a_1=\tfrac{10}{21}$, $Q_2=\tfrac{15}{7}$, $Q_3=\tfrac{177005}{67963}$.

*Proof.* (1) is Theorem 1 with $g=h=f_n$. For (2), $A^{3^v}$ has the residue classes mod $3^v$ as its orbits on $\mathbb Z/3^n$, so $\sum_iV^{3^vi}=3^{n-v}E_v$ on $H_n$ and $\langle f_n,E_vf_n\rangle=\lVert f_v\rVert^2$. (3) is Plancherel on $\mathbb Z/3^{n+1}$. (4): $d_{n-1}$ lies in the span of eigenvectors of $V$ of exact order $3^n$, where $\mathcal L^*\mathcal L$ has eigenvalues strictly between $3/5$ and $5/3$. $\qquad\blacksquare$

## 4. Theorem 3: no $L^2$ density

**Theorem 3.** (a) $Q_n\to\infty$. Equivalently $\mu$ has no density in $L^2(m)$, and $\sum_\zeta|\hat\mu(\zeta)|^2=\infty$.
(b) With $f=d\mu/dm$, $\ \liminf_na_n\ge a_*:=\sum_{j\ne0}4^{-|j|}\int f\cdot(f\circ A^j)\,dm>0$. Hence $Q_n\ge(a_*-o(1))\,n$.

*Proof.* (a) Suppose $\sup_nQ_n<\infty$. The $f_n$ form a nonnegative martingale bounded in $L^2$, so $f_n\to f$ in $L^2$ and $\mu=f\,m$. Then $\gamma_n(j)\to R_j:=\int f\cdot f\circ A^j$ for each $j$. Since $Q_n$ converges, $a_n\to0$, and every term of $a_n=\sum_{j\ne0}4^{-|j|}\gamma_n(j)$ is nonnegative, so $R_j=0$ for all $j\ne0$. With $S=\{f>0\}$ this says $m(S\cap A^{-j}S)=0$ for all $j\ne0$. But $A$ is ergodic for $m$ (Corollary 1: its only invariant functions in each $H_k$ are constants), so $\frac1N\sum_{j=1}^Nm(S\cap A^{-j}S)\to m(S)^2>0$. Contradiction.

(b) $f_n\to f$ almost everywhere, so Fatou gives $\liminf\gamma_n(j)\ge R_j$, and Fatou for the series gives the bound. $a_*>0$ by the same ergodicity argument. $\qquad\blacksquare$

Combined with Theorem 2(3): the mean-square size of $\hat\mu$ over the $2\cdot3^n$ frequencies of exact level $n+1$ does not fall below $c\cdot3^{-n}$. Square-root cancellation is the truth on average and cannot be improved.

## 5. The operator in multiplicative characters

Write a unit as $x=\varepsilon\cdot4^h$ with $\varepsilon\in\{1,2\}$, $h\in\mathbb Z_3$, and write $g(y)=G(\log_4(1+3y))$. Then

$$(\mathcal Lg)(\varepsilon\cdot4^h)=3\,\varepsilon\sum_{j\ge1}4^{-j}G(h+j). \tag{5.1}$$

*Proof.* For $\varepsilon=1$ the admissible $a$ are $2j$, with $1+3\cdot\frac{2^ax-1}{3}=4^{h+j}$ and weight $3\cdot4^{-j}$; for $\varepsilon=2$ they are $2j-1$, with the same argument $4^{h+j}$ and weight $6\cdot4^{-j}$. $\qquad\blacksquare$

So one Syracuse step is a one-sided geometric average along the odometer $h\mapsto h+1$, followed by re-reading the result, a function of $x$, in the coordinate $\log_4(1+3x)$. The first part is diagonal in the characters $\psi_\xi(y)=e(\xi\log_4(1+3y))$: $\ \mathcal L\psi_\xi=\frac{3e(\xi)}{4-e(\xi)}\Psi_\xi$ with $\Psi_\xi(\varepsilon4^h)=\varepsilon\,e(\xi h)$. All mixing comes from the second part, the change between the multiplicative coordinates of $x$ and of $1+3x$.

**Observation (EMPIRICAL, levels 2–4, machine precision).** For $\xi$ of exact level $k$, $\langle\Psi_\xi,\psi_\eta\rangle$ vanishes unless $\eta$ has exact level $k+1$, and $|\langle\Psi_\xi,\psi_\eta\rangle|^2$ then takes exactly two values, in ratio $1:4$, each on half of those $\eta$. The kernel is flat. These coefficients are sums of a character of $x$ against a character of $1+3x$, so they are of Jacobi type, and flatness is what stationary phase predicts. No proof is written here.

## 6. Numerics and conjectures (EMPIRICAL)

| $n$ | $Q_n$ | $a_{n-1}$ | $\gamma_n(1)$ | $\gamma_n(2)$ | $\gamma_n(3)$ | $\min_{\text{units}}f_n$ | $\max f_n$ |
|---|---|---|---|---|---|---|---|
| 2 | 2.142857 | 0.476190 | 0.69388 | 0.48980 | 1.42857 | 0.28571 | 3.14 |
| 4 | 3.068646 | 0.464214 | 0.70704 | 0.49353 | 1.32473 | 0.14492 | 7.27 |
| 8 | 4.931742 | 0.465921 | 0.71926 | 0.47448 | 1.23937 | 0.07507 | 37.3 |
| 12 | 6.802899 | 0.468941 | 0.72565 | 0.47325 | 1.23702 | 0.05292 | 189.6 |
| 14 | 7.742768 | 0.470254 | 0.72807 | 0.47326 | 1.23704 | 0.04692 | 426.8 |
| 16 | 8.684948 | 0.471352 | 0.73001 | 0.47341 | 1.23707 | 0.04293 | 960.3 |
| 17 | 9.156768 | 0.471820 | 0.73082 | 0.47347 | 1.23715 | 0.04175 | 1440.6 |

- $a_n$ increases slowly from $n=6$ on; its increments shrink by a factor of about $0.9$ per level. Geometric extrapolation from levels 11–17 gives $a_\infty\approx0.476$, with an uncertainty of about two units in the third decimal.
- $\gamma_n(j)$ for $j=2,\dots,6$ is stable to three decimals by level 12. $\gamma_n(1)$ is still rising at level 17, with increments shrinking by about $0.9$ per level.
- $\max f_n\approx1.46\cdot(3/2)^n$, at the residue of $-1$. $\min f_n$ over units agrees with the values of $3^nc_n$ tabulated in the comments to Tao's post.
- At level 13, $t^2\,m\{f_{13}>t\}$ lies between $0.84$ and $0.95$ for $6\le t\le24$.
- $\lVert f_{13}-f_m\rVert_1$ shrinks by a factor $0.86$–$0.89$ per level for $1\le m\le8$.

**Conjecture C1 (bounded odometer autocorrelations).** $\gamma_n(j)\to R_j=\int f\cdot f\circ A^j$ for every $j\ne0$, with $\sup_n\gamma_n(j)\le C(1+v_3(j))$. Then $Q_n\sim a_\infty n$ with

$$a_\infty=\sum_{j\ne0}4^{-|j|}\int f\cdot(f\circ A^j)\,dm\approx0.476 .$$

Theorem 2(2) proves this on average over each class $\{j:v_3(j)=v\}$; C1 says the small $j$ that carry the Poisson weight behave like their class. C1 would give the linear upper bound for the collision energy. In the normalisation where that energy starts at $10/9$, which is $\tfrac23Q_1$, the slope would be $\tfrac23a_\infty\approx0.317$.

**Conjecture C2.** $m\{f>t\}\sim C/t^2$ as $t\to\infty$.

## 7. Why this singles out $3x+1$

The same computation for the $qx+1$ map on $\mathbb Z_q$, with $r$ the order of $2$ mod $q$ and $A_q(y)=2^ry+(2^r-1)/q$, gives $\mathcal L_q^*\mathcal L_q=\frac q3\sum_j2^{-r|j|}V_q^j$. The diagonal coefficient is $q/3$. It equals 1 only for $q=3$. The script checks this identity exactly for $q=5,7$ at levels 1 and 2.

## 8. Limits and next steps

- This is harmonic analysis of one measure. It says nothing about cycles, divergent orbits, or any fixed integer.
- Theorem 3(b) gives no explicit constant; $a_*$ is positive but not computed rigorously.
- C1 is open. A natural route is the pair recursion on affine maps $g$: with $Q_n(g)=3^nP(\tilde X\equiv g(X)\ (3^n))$ one has $Q_{n+1}(g)=3\sum_{a,b}2^{-a-b}Q_n(\varphi_b^{-1}g\varphi_a)$ over the pairs for which $\varphi_b^{-1}g\varphi_a$ is integral, and $\gamma_n(j)=Q_n(A^j)$. The only fixed point of every conjugation is the identity, which is the source of the linear growth.
- Section 5 isolates the one place where mixing happens. A proof of the flat-kernel observation, with phases, would turn the rate of fine-scale mixing into a question about products of explicit Jacobi-type matrices.

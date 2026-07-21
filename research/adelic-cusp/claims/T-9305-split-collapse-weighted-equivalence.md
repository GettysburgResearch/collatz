# T-9305 — Split collapse and weighted discrepancy equivalence

**Claim ID:** T-9305  
**Title:** Every two-place CRT split is uniformly equivalent to the original survivor and triadic-mirror Fourier criteria  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9307`; the elementary Lipschitz bound for `|cos(pi x)|`  
**Scope:** quantitative comparison of the original EQ product, its triadic mirror, and the room/Cantor CRT product  
**Related counterexample candidates:** none

## Statement

Use the notation of `L-9307`. Put

\[
\rho=\frac{64}{81}.
\tag{1}
\]

For `K >= 1` and an integer `h`, define

\[
F^{(2)}_K(h)
=
\frac{|S_K(h)|}{2^K},
\qquad
F^{(3)}_K(h)
=
\frac{|\widehat C_K(h)|}{2^K}.
\tag{2}
\]

Let

\[
K=n+j,
\qquad
n,j\ge1,
\qquad
Q_{n,j}=64^n81^j,
\tag{3}
\]

and let `G_(n,j)(h)` be the normalized CRT-product coefficient from `T-9304`.

Then, for every integer `h`,

\[
\boxed{
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{64^K}
\bigl(1-\rho^K\bigr).
}
\tag{4}
\]

For every split `K=n+j`,

\[
\boxed{
\left|
|G_{n,j}(h)|-F^{(3)}_K(h)
\right|
\le
\frac{\pi|h|}{Q_{n,j}}
\bigl(1-\rho^n\bigr).
}
\tag{5}
\]

Consequently,

\[
\boxed{
\left|
|G_{n,j}(h)|-F^{(2)}_K(h)
\right|
\le
\pi|h|
\left[
\frac{1-\rho^K}{64^K}
+
\frac{1-\rho^n}{Q_{n,j}}
\right].
}
\tag{6}
\]

Since

\[
Q_{n,j}\ge64^K,
\]

one may use the simpler bound

\[
\boxed{
\left|
|G_{n,j}(h)|-F^{(2)}_K(h)
\right|
<
\frac{2\pi|h|}{64^K}.
}
\tag{7}
\]

### Weighted form

For `1 <= H`, define

\[
E^{(2)}_K(H)
=
\sum_{1\le h\le H}
\frac{F^{(2)}_K(h)}h,
\tag{8}
\]

\[
E^{(3)}_K(H)
=
\sum_{1\le h\le H}
\frac{F^{(3)}_K(h)}h,
\tag{9}
\]

and

\[
\mathcal D_{n,j}(H)
=
\sum_{1\le h\le H}
\frac{|G_{n,j}(h)|}h.
\tag{10}
\]

Then

\[
\boxed{
\left|
E^{(2)}_K(H)-E^{(3)}_K(H)
\right|
\le
\frac{\pi H}{64^K}
\bigl(1-\rho^K\bigr),
}
\tag{11}
\]

\[
\boxed{
\left|
\mathcal D_{n,j}(H)-E^{(3)}_K(H)
\right|
\le
\frac{\pi H}{Q_{n,j}}
\bigl(1-\rho^n\bigr),
}
\tag{12}
\]

and

\[
\boxed{
\left|
\mathcal D_{n,j}(H)-E^{(2)}_K(H)
\right|
\le
\pi H
\left[
\frac{1-\rho^K}{64^K}
+
\frac{1-\rho^n}{Q_{n,j}}
\right]
<
\frac{2\pi H}{64^K}.
}
\tag{13}
\]

Therefore, uniformly over every choice of split `n+j=K`,

\[
H_K=o(64^K)
\tag{14}
\]

implies

\[
\boxed{
E^{(2)}_K(H_K)	o0
\iff
E^{(3)}_K(H_K)	o0
\iff
\mathcal D_{n,j}(H_K)	o0.
}
\tag{15}
\]

For the issue-#4 EQ range

\[
H_K=2^K,
\]

the comparison error is at most

\[
2\pi\,2^{-5K}.
\tag{16}
\]

Thus the two-place room/Cantor absolute-Fourier target is not a weaker asymptotic statement than the original EQ weighted criterion. It is the same criterion, up to an explicit exponentially small error, for every split.

## Definitions

`F^(2)` is the original normalized survivor Fourier magnitude. `F^(3)` is the normalized transform of the depth-`K` admissible Cantor class set. `D_(n,j)` is the restricted two-place sum introduced in `Q-9302`.

The theorem concerns **absolute Fourier magnitudes and their harmonic sums**. It does not identify complex phases term by term and does not claim an order-preserving bijection between the CRT comparison set and the actual survivor set.

The phrase *split collapse* means that the apparent parameter choice

\[
K=n+j
\]

does not produce a family of asymptotically distinct absolute-Fourier problems. Every split stitches the same phase chain and differs only by the sum of explicit reciprocity shifts.

## Motivation

The stationary two-place factorization created a plausible new offense: perhaps the product of the `Z_2` and `Z_3` coefficients decays in ranges where neither local factor is tractable alone.

`L-9307` shows that the factors are not independent phase samples on the rational diagonal. They are adjacent pieces of one reciprocal chain. The present theorem quantifies that observation and determines exactly what is gained and what is not.

The result is both positive and negative:

- positive: the room/Cantor product, the original survivor product, and the triadic mirror may be exchanged freely in every sub-`64^K` weighted frequency range;
- negative: proving `Q-9302` by absolute values does not bypass the original all-depth EQ wall.

The two-place formulation may still suggest a successful transfer operator, renewal theorem, or signed cancellation mechanism. Such a proof would solve the original criterion at the same time.

## Proof

The function

\[
C(x)=|\cos(\pi x)|
\]

is `pi`-Lipschitz on the circle:

\[
|C(x)-C(y)|
\le
\pi\|x-y\|_{\mathbb R/\mathbb Z}.
\tag{17}
\]

For numbers `a_ell,b_ell in [0,1]`, the telescoping product inequality gives

\[
\left|
\prod_\ell a_\ell-
\prod_\ell b_\ell
\right|
\le
\sum_\ell|a_\ell-b_\ell|.
\tag{18}
\]

### Dyadic versus triadic products

By `L-9307`, the two products use the same phases `x_ell(h)`, with the dyadic factors shifted by

\[
\delta_\ell(h)
=
\frac{17h}{64^{K-\ell}81^{\ell+1}}.
\]

Equations `(17)` and `(18)` therefore give

\[
\left|
F^{(2)}_K(h)-F^{(3)}_K(h)
\right|
\le
\pi\sum_{\ell=0}^{K-1}
|\delta_\ell(h)|.
\tag{19}
\]

The geometric sum is exact:

\[
\begin{aligned}
\sum_{\ell=0}^{K-1}
|\delta_\ell(h)|
&=
\frac{17|h|}{64^K81}
\sum_{\ell=0}^{K-1}
\left(\frac{64}{81}\right)^\ell\\
&=
\frac{|h|}{64^K}
\bigl(1-\rho^K\bigr),
\end{aligned}
\tag{20}
\]

because

\[
1-\rho=\frac{17}{81}.
\]

This proves `(4)`.

### A stitched split versus the triadic product

Again by `L-9307`, the first `j` factors of `|G_(n,j)(h)|` equal the first `j` factors of `F^(3)_K(h)` exactly. Only the indices

\[
j\le\ell<K
\]

carry the shifts `delta_ell(h)`. Hence

\[
\left|
|G_{n,j}(h)|-F^{(3)}_K(h)
\right|
\le
\pi\sum_{\ell=j}^{K-1}
|\delta_\ell(h)|.
\tag{21}
\]

Writing `ell=j+t`, the tail sum is

\[
\begin{aligned}
\sum_{\ell=j}^{K-1}
|\delta_\ell(h)|
&=
\frac{17|h|}{64^n81^{j+1}}
\sum_{t=0}^{n-1}
\left(\frac{64}{81}\right)^t\\
&=
\frac{|h|}{64^n81^j}
\bigl(1-\rho^n\bigr)\\
&=
\frac{|h|}{Q_{n,j}}
\bigl(1-\rho^n\bigr).
\end{aligned}
\tag{22}
\]

This proves `(5)`.

Equation `(6)` follows from the triangle inequality. Since

\[
Q_{n,j}
=
64^K\left(\frac{81}{64}\right)^j
\ge64^K,
\]

and both parenthetical factors are below `1`, equation `(7)` follows.

### Weighted sums

Divide `(4)`, `(5)`, and `(6)` by `h` and sum over

\[
1\le h\le H.
\]

The factor `h` in each pointwise error cancels the harmonic weight, leaving exactly `H` copies of the corresponding constant. This proves `(11)`--`(13)`.

If `(14)` holds, all displayed errors tend to zero uniformly in the split. This proves `(15)`. Substituting

\[
H_K=2^K
\]

into `(13)` gives `(16)`. QED.

## Dependency audit

- `L-9307` supplies the exact common phase chain and stitched product.
- The only analytic inputs are the circle Lipschitz bound `(17)` and the elementary product inequality `(18)`.
- No issue-#4 room-position theorem is needed.
- No frequency-block mean, depth-period mean, external Fourier theorem, or computation is used.
- The theorem directly compares absolute values, which is precisely the form used in the Erdős--Turán weighted criteria.

## Gap audit

- Equivalence of targets does not prove that any of them tends to zero.
- The result does not create signed cancellation between different frequencies.
- A two-place dynamical proof may still be substantially easier even though its conclusion is equivalent.
- The comparison is useful for `H=o(64^K)`. At frequencies comparable with the full modulus, the explicit errors need not vanish.
- The theorem does not replace the branch-qualified position theorem for questions requiring ordered pointwise correspondences rather than absolute Fourier sums.
- No conclusion about the existence of an ordinary integer in the infinite survivor attractor follows.

## Adversarial tests

1. At `h=0`, every pointwise difference is zero.
2. At the endpoint split `j=0`, equation `(5)` becomes equation `(4)`; at `n=0`, its left side is zero.
3. If `h` is comparable to `64^K`, equation `(4)` correctly permits an order-one difference.
4. For `H=2^K`, the error exponent is `2^K/64^K=2^{-5K}`, much smaller than every scale appearing in EQ.
5. The proof compares magnitudes before summing. It does not use an invalid inequality that would replace the modulus of a sum by a sum of signed errors.

## Remaining uncertainty

The proof is complete-looking. Independent review should reconstruct the split indexing in `L-9307`, then check the exact geometric tail `(22)`. The character-sign convention cannot affect the result because every statement is in absolute value.

## Suggested next attack

Reframe `Q-9302`: the restricted two-place target is now known to be equivalent to the original EQ criterion. The next useful theorem must exploit the two-place formulation at the level of **proof mechanism**—for example, a signed transfer operator, a combined-energy inverse theorem, or a solenoid renewal estimate—not merely restate absolute decay of the product coefficient.
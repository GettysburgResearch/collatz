# L-9305 — Triadic moving-character identity

**Claim ID:** L-9305  
**Title:** Every finite Cantor-class product is one coefficient of the fixed triadic mirror measure  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `D-9303`; exact definitions below  
**Scope:** Fourier analysis of the issue-#4 Cantor classes `C_j`  
**Related counterexample candidates:** none

## Statement

Let `nu` be the fixed probability measure from `D-9303`. Define the standard positive-sign additive character on `Q_3` by

\[
\psi_3(x)=\exp(2\pi i\{x\}_3),
\]

where `{x}_3` is the unique rational in `[0,1)` with denominator a power of `3` such that

\[
x-\{x\}_3\in\mathbb Z_3.
\]

For `q in Q_3`, put

\[
\widehat\nu(q)=
\int_{\mathbb Z_3}\psi_3(qy)\,d\nu(y).
\]

For `j >= 1`, let `C_j` be the reduction from `D-9303` and define

\[
\widehat C_j(h)=
\sum_{x\in C_j}
\exp\!\left(2\pi i\frac{hx}{81^j}\right).
\]

Then:

1. for every integer `h`,
   \[
   \boxed{
   \widehat\nu\!\left(\frac{h}{81^j}\right)
   =
   \frac{\widehat C_j(h)}{2^j};
   } \tag{1}
   \]
2. for every `q in Q_3`,
   \[
   \boxed{
   \widehat\nu(q)
   =
   \prod_{r\ge0}
   \frac{1+\psi_3(qc\lambda^r)}2,
   } \tag{2}
   \]
   and the product is finite for every continuous character of `Z_3`;
3. the exact functional equation is
   \[
   \boxed{
   \widehat\nu(q)
   =
   \frac{1+\psi_3(cq)}2
   \widehat\nu(\lambda q);
   } \tag{3}
   \]
4. expanding `(1)` gives the finite product
   \[
   \boxed{
   \frac{\widehat C_j(h)}{2^j}
   =
   \prod_{i=1}^{j}
   \frac{1+
   \exp\!\left(
   -2\pi i
   \frac{17\,64^{-i}h}{81^{j-i+1}}
   \right)}2,
   } \tag{4}
   \]
   where each inverse `64^(-i)` is taken modulo the displayed power of `81`.

Thus the finite transform called the Cantor mirror in the issue-#4 interchange work is the fixed transform `nu-hat` sampled at the moving triadic characters `h/81^j`.

## Definitions

The constants are

\[
\lambda=81/64,
\qquad
c=-17/64.
\]

A continuous character of `Z_3` is represented by an element of `3^{-N}Z_3/Z_3`. Since

\[
v_3(c\lambda^r)=4r,
\]

all sufficiently late factors in `(2)` equal `1`.

## Motivation

`L-9301` stationarized the survivor transform on `Z_2`. The latest issue-#4 interchange packet found a second finite product, `C_j-hat`, on the `81`-adic side. Equation `(1)` shows that this product is not another genuinely varying family: it is a second fixed self-similar Fourier transform, now on `Z_3`.

This yields an exact two-place picture:

- survivor coefficients are values of `mu-hat` along a `2`-adic cusp;
- Cantor-class coefficients are values of `nu-hat` along a `3`-adic cusp.

Their eventual pairing can therefore be studied as a product-measure problem on `Z_2 x Z_3` or on the `{2,3,infinity}` solenoid, rather than only through finite modular formulas.

## Proof

Let

\[
Y=
\sum_{r\ge0}c\eta_r\lambda^r
\]

have law `nu`, with independent fair digits. Independence gives

\[
\begin{aligned}
\widehat\nu(q)
&=\mathbb E\,\psi_3(qY)\\
&=\prod_{r\ge0}
\mathbb E\,\psi_3(qc\eta_r\lambda^r)\\
&=\prod_{r\ge0}
\frac{1+\psi_3(qc\lambda^r)}2.
\end{aligned}
\]

As noted above, only finitely many factors are nontrivial. This proves `(2)` without an infinite-product interchange issue.

Now take

\[
q=\frac h{81^j}.
\]

For `r >= j`,

\[
q c\lambda^r
=
-17h\frac{81^{r-j}}{64^{r+1}}
\in\mathbb Z_3,
\]

so all tail factors equal `1`. Expanding the first `j` factors gives

\[
\widehat\nu(h/81^j)
=
2^{-j}
\sum_{\eta_0,\ldots,\eta_{j-1}}
\psi_3\!\left(
\frac h{81^j}
\sum_{r<j}c\eta_r\lambda^r
\right).
\]

The finite sums give the distinct residues `C_j`, by `D-9303`. With the character convention fixed above,

\[
\psi_3(hx/81^j)
=
\exp\!\left(2\pi i\frac{hx}{81^j}\right)
\]

for the standard representative `x in {0,...,81^j-1}`. This proves `(1)`.

Splitting the random series at its first digit gives

\[
Y=c\eta_0+\lambda Y',
\]

with `Y'` independent and identically distributed. Taking characters proves `(3)`.

Finally, in the `r`-th factor of `(1)`,

\[
\frac{hc\lambda^r}{81^j}
=
-
\frac{17h\,81^r}{64^{r+1}81^j}
=
-
\frac{17h\,64^{-(r+1)}}{81^{j-r}}.
\]

Putting `i=r+1` yields `(4)`. QED.

## Dependency audit

- `D-9303` supplies the random series, distinct finite reductions, and Bernoulli independence.
- No issue-#4 theorem is needed for the proof.
- The final identification with the branch formula called `T-0027` is a direct notation match.
- No external Fourier-decay result is invoked.

## Gap audit

- Stationarizing `C_j-hat` does not prove decay along all moving characters.
- The character-sign convention must match any branch formula before complex phases are identified; absolute values are unchanged by conjugation.
- The fixed measure `nu` is not Haar measure and has no asserted spectral gap.
- The product formula alone does not control how the triadic classes are ordered in a real interval.
- A joint survivor/Cantor product requires a precise digit split; this lemma treats only the triadic factor.

## Adversarial tests

1. At `j=1`, `C_1={0,1}`, so
   \[
   \widehat\nu(h/81)
   =\frac{1+e^{2\pi ih/81}}2.
   \]
2. At `h=0`, every expression equals `1` after normalization.
3. If `81^j | h`, the character is trivial and `C_j-hat(h)=2^j`.
4. Reversing all finite binary words changes their ordering but not the set or normalized sum.
5. Equation `(3)` reproduces the lifting recursion of `C_j` after reduction modulo `81^j`.

## Remaining uncertainty

The proof is complete-looking. Independent review should check the positive-sign `3`-adic character convention and the indexing in `(4)` against the branch's finite product.

## Suggested next attack

Form the exact CRT product of `R_n` and `C_j`. Its finite Fourier transform factors into one coefficient of `mu` and one coefficient of `nu`, producing a stationary two-place analogue of the issue-#4 product-rigidity theorem.
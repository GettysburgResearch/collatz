# T-6503 — Low-surplus density-zero theorem

**Claim ID:** `T-6503`  
**Title:** Every fixed coefficient-surplus band has only `O(k^(1/9))` visits on an all-prefix-supercritical ordinary orbit  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `L-6501`, `T-6501`; elementary walk arithmetic  
**Scope:** positive ordinary orbits satisfying `D_k>=0` for every `k`

## 1. Exact additive form of the correction product

Use

\[
{x_k\over n}=C_kP_k,
\qquad
C_k=3^{D_k},
\]

with

\[
P_k=
\prod_{\substack{0\le i<k\\v_i=1}}
\left(1+{1\over3x_i}\right).
\]

At an odd source time `i`,

\[
P_{i+1}-P_i
={P_i\over3x_i}.
\]

Since

\[
x_i=nC_iP_i=n3^{D_i}P_i,
\]

this increment simplifies exactly to

\[
P_{i+1}-P_i
={1\over3n}3^{-D_i}.
\]

At an even source time the product is unchanged. Therefore

\[
\boxed{
P_k
=1+{1\over3n}
\sum_{\substack{0\le i<k\\v_i=1}}3^{-D_i}.}
\tag{1}
\]

This is an exact identity for the same ordinary orbit. It is not an estimate or a symbolic average.

## 2. Total inverse-surplus mass

By `L-6501`,

\[
P_k\le e^{7/9}k^{1/9}.
\]

Substituting in `(1)` gives

\[
\boxed{
\sum_{\substack{0\le i<k\\v_i=1}}3^{-D_i}
\le
3n\left(e^{7/9}k^{1/9}-1\right).}
\tag{2}
\]

## 3. Low-band odd endpoints

Fix `H>=0` and define

\[
N_H^{\rm odd}(k)
=
\#\{0\le i<k:v_i=1,\ D_i\le H\}.
\]

Every counted term contributes at least `3^(-H)` to `(2)`. Hence

\[
\boxed{
N_H^{\rm odd}(k)
\le
3^{H+1}n\left(e^{7/9}k^{1/9}-1\right).}
\tag{3}
\]

Thus odd-source returns to any fixed surplus band have zero natural density, with explicit exponent `1/9`.

## 4. All low-band times

Put

\[
N_H(k)=\#\{0\le i<k:D_i\le H\}.
\]

The surplus increments are

\[
D_{i+1}-D_i=
\begin{cases}
1-\alpha,&v_i=1,\\
-\alpha,&v_i=0,
\end{cases}
\qquad
\alpha={\log2\over\log3}.
\tag{4}
\]

Starting from a time with `D_i<=H`, an indefinitely even future would make `D` negative. The first later odd source must occur after at most

\[
L_H=\left\lfloor{H\over\alpha}\right\rfloor+1
\]

consecutive even sources, and its source surplus is still at most `H`. Every low-band time can therefore be charged to a low-band odd source no more than `L_H+1` times, apart from one terminal incomplete run. Consequently

\[
\boxed{
N_H(k)
\le
(L_H+1)N_H^{\rm odd}(k)+L_H+1.}
\tag{5}
\]

Combining `(3)--(5)`,

\[
\boxed{
N_H(k)=O_{n,H}(k^{1/9}).}
\tag{6}
\]

In particular,

\[
\boxed{
{N_H(k)\over k}\longrightarrow0
\qquad(k\to\infty).}
\tag{7}
\]

## 5. Density-one escape

Since `(7)` holds for every fixed `H`,

\[
\boxed{
D_k\longrightarrow+\infty
\text{ in natural density one}.}
\tag{8}
\]

Equivalently,

\[
\boxed{
C_k=3^{D_k}\longrightarrow+\infty
\text{ in natural density one}.}
\tag{9}
\]

This does not assert pointwise convergence: sparse returns to low surplus remain possible.

## 6. Strategic consequence

The all-time-supercritical Lane A is now much narrower than a nonnegative irrational ballot path:

```text
coefficient records grow at least polynomially;
every fixed low band is visited only O(k^(1/9)) times;
the coefficient escapes to infinity on a density-one set of times.
```

Thus bounded-discrepancy, recurrent critical, mechanical, and positive-frequency low-band models cannot represent a positive ordinary Lane-A orbit.

A proof of Collatz still requires exclusion of the sparse-return, unbounded-record regime.

## 7. Gap audit

- Zero-density low returns may still occur infinitely often.
- Density-one coefficient escape is compatible with an orbit tending to infinity and is not a contradiction.
- The exponent `1/9` inherits the safe elementary harmonic estimate of `L-6501`.
- No map-level equidistribution theorem is converted into pointwise orbit mixing.
- Ordinary realization remains part of the hypotheses; completion ghosts are outside the theorem.

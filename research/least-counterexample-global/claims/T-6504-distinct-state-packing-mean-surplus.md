# T-6504 — Distinct-state packing forces `8/9` logarithmic mean surplus

**Claim ID:** `T-6504`  
**Title:** Every all-prefix-supercritical ordinary orbit has mean coefficient surplus at least `(8/9) log_3 K-O_n(1)`  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `L-6501`; ordinary distinct-state argument of `T-6501`; cross-links PR #79 `T-6603` and PR #81 `L-6801/T-6802`  
**Scope:** positive ordinary shortcut-Collatz orbits satisfying `D_k>=0` for every prefix

## 1. Statement

Let

\[
x_k=T^k(n),
\qquad
D_k=q_k-{\log2\over\log3}k,
\]

and assume

\[
\boxed{D_k\ge0\qquad(k\ge0).}
\tag{1}
\]

Then for every `K>=1`,

\[
\boxed{
\sum_{k=1}^K D_k
\ge
{1\over\log3}
\left[
\log{(n+K)!\over n!\,n^K}
-{1\over9}\log(K!)
-{7K\over9}
\right].}
\tag{2}
\]

Consequently, for every fixed initial integer `n`,

\[
\boxed{
{1\over K}\sum_{k=1}^K D_k
\ge
{8\over9}\log_3 K
-\log_3 n
-{5\over3\log3}
+o(1).}
\tag{3}
\]

If

\[
M_K=\max_{0\le k\le K}D_k,
\qquad
X_K=\max_{0\le k\le K}x_k,
\]

then the exact finite lower bound is

\[
\boxed{
3^{M_K}
\ge
{\left((n+K)!/(n!n^K)\right)^{1/K}
 \over
 e^{7/9}(K!)^{1/(9K)}}.}
\tag{4}
\]

In particular,

\[
\boxed{
3^{M_K}
\ge
{K^{8/9}\over n e^{5/3+o(1)}},}
\tag{5}
\]

and

\[
\boxed{
X_K\ge e^{-5/3-o(1)}K^{8/9}.}
\tag{6}
\]

Thus the coefficient maximum by time `K` has exponent `8/9`, not merely `4/9`, and the average surplus itself diverges logarithmically.

## 2. Distinct physical states

Condition `(1)` makes every `C_k=3^{D_k}` strictly greater than one for `k>=1`: equality would give a positive power-of-three equal to a positive power-of-two.

The exact affine remainder is nonnegative, hence

\[
x_k=C_kn+E_k>n
\qquad(k\ge1).
\tag{7}
\]

As in `T-6501`, a repeated state would create a positive periodic block with coefficient below one; repeating that block would eventually force a negative global surplus. Therefore

\[
\boxed{x_1,\ldots,x_K\text{ are distinct integers greater than }n.}
\tag{8}
\]

After sorting,

\[
\boxed{
\prod_{k=1}^Kx_k
\ge
\prod_{r=1}^K(n+r)
={(n+K)!\over n!}.}
\tag{9}
\]

## 3. Product upper bound

The exact multiplicative identity is

\[
x_k=n3^{D_k}P_k.
\tag{10}
\]

`L-6501` proves

\[
P_k\le e^{7/9}k^{1/9}.
\tag{11}
\]

Multiplying `(10)--(11)` for `1<=k<=K` gives

\[
\boxed{
\prod_{k=1}^Kx_k
\le
n^K e^{7K/9}(K!)^{1/9}
3^{\sum_{k=1}^KD_k}.}
\tag{12}
\]

Combining `(9)` and `(12)`, then taking logarithms, proves `(2)`.

## 4. Asymptotic extraction

For fixed `n`, Stirling's formula gives

\[
{1\over K}
\log{(n+K)!\over n!\,n^K}
=
\log K-\log n-1+o(1),
\tag{13}
\]

and

\[
{1\over9K}\log(K!)
={1\over9}\log K-{1\over9}+o(1).
\tag{14}
\]

Substituting `(13)--(14)` into `(2)` gives `(3)`.

Since `M_K` is at least the mean of the nonnegative `D_k`, exponentiating `(2)/K` gives `(4),` and Stirling gives `(5)`.

Finally, choose `r<=K` with `D_r=M_K`. The affine remainder is nonnegative, so

\[
X_K\ge x_r\ge n3^{M_K}.
\]

Equation `(5)` proves `(6)`.

## 5. Cross-branch comparison

PR #79 `T-6603` uses the least-counterexample floor and distinct odd values to obtain an asymptotic mean lower coefficient `5/6` in a related logarithmic packing bound. The prime-to-six correction estimate of `L-6501` reduces the cumulative correction exponent from `1/6` to `1/9`, producing the sharper `8/9` coefficient in `(3)`.

PR #81 `T-6802` obtains a deterministic entropy-pressure record exponent from dyadic separation of repeated parity factors. Equation `(4)` is stronger numerically in the present full ordinary-orbit scope, while the factor-separation lemma remains valuable for first-crossing low-complexity words and for certificate formats not covered by the prime-to-six harmonic product.

No source claim is superseded automatically; this file records the exact synthesis and its narrower hypotheses.

## 6. Strategic consequence

The surviving all-time-supercritical lane must now satisfy simultaneously:

```text
full ordinary divergence;
mean surplus >= (8/9) log_3 K-O_n(1);
coefficient maximum >= K^(8/9)/(n e^(5/3+o(1)));
physical maximum >= e^(-5/3-o(1)) K^(8/9);
only O_(n,H)(K^(1/9)) visits to every fixed low band.
```

This removes the entire bounded-bank, slowly growing mean-bank, and frequent-critical-return region.

## 7. Gap audit

- Logarithmically growing mean surplus is compatible with a sparse-return divergent orbit.
- The theorem does not prove pointwise `D_k->infinity`.
- The asymptotic statements fix `n` and let `K->infinity`; they are not uniform over changing initial values.
- The result is conditional on the same ordinary all-prefix-supercritical orbit whose nonexistence remains open.
- No proof of Collatz follows until the remaining high-bank Lane A and all first crossings/cycles in Lane B are excluded.

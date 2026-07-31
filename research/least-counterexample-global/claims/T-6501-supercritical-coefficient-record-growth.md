# T-6501 — Supercritical coefficient-record growth

**Claim ID:** `T-6501`  
**Title:** Every all-prefix-supercritical ordinary orbit has polynomially growing coefficient records  
**Status:** **PROPOSED**  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Issue:** #78  
**Dependencies:** `D-6501`, `L-6501`; elementary affine iteration  
**Scope:** positive ordinary orbits satisfying `C_k>=1` for every prefix

## 1. Statement

Let

\[
x_k=T^k(n),
\qquad
q_k=\#\{0\le i<k:x_i\text{ odd}\},
\]

\[
\alpha={\log2\over\log3},
\qquad
D_k=q_k-\alpha k,
\qquad
C_k=3^{D_k}.
\]

Assume

\[
\boxed{D_k\ge0\quad(k\ge0).}
\tag{1}
\]

Put

\[
M_k=\max_{0\le m\le k}D_m.
\]

Then, for every `k>=1`,

\[
\boxed{
3^{M_k}
\ge
\left({\alpha\over2n e^{7/9}}\right)^{1/2}
 k^{4/9}.}
\tag{2}
\]

Moreover, whenever `r>=1` is a coefficient-record time,

\[
D_r=M_r,
\]

one has the stronger bound

\[
\boxed{
C_r=3^{D_r}
\ge
{\alpha\over2n e^{7/9}}\,r^{8/9}.}
\tag{3}
\]

Consequently:

\[
\boxed{\sup_kD_k=+\infty.}
\tag{4}
\]

More quantitatively,

\[
\boxed{
\limsup_{k\to\infty}{M_k\over\log_3 k}\ge{4\over9},}
\tag{5}
\]

and along the unbounded sequence of record times,

\[
\boxed{
\limsup_{\substack{r\to\infty\\D_r=M_r}}
{D_r\over\log_3 r}\ge{8\over9}.}
\tag{6}
\]

Thus the bounded-surplus branch left open in the first proof of `T-6708` cannot occur for a positive ordinary all-time-supercritical orbit.

## 2. Exact affine surplus

The finite affine identity is

\[
x_k=C_kn+E_k.
\]

Writing `v_i=x_i mod 2`, direct expansion gives

\[
\boxed{
E_k={1\over2}
\sum_{m=1}^k
v_{m-1}3^{D_k-D_m}.}
\tag{7}
\]

For completeness, the contribution of the odd step at time `m-1` is initially `1/2` and is multiplied by every later homogeneous factor. Since the later homogeneous product is

\[
{3^{q_k-q_m}\over2^{k-m}}
=3^{D_k-D_m},
\]

summing the contributions gives `(7)`.

## 3. Global record lower bound

Fix `k>=1`. Under `(1)`,

\[
q_k\ge\alpha k.
\tag{8}
\]

For every term of `(7)`,

\[
D_k-D_m\ge-M_k,
\]

so

\[
E_k
\ge{q_k\over2\,3^{M_k}}
\ge{\alpha k\over2\,3^{M_k}}.
\tag{9}
\]

On the other hand, the exact multiplicative identity and `L-6501` give

\[
x_k=nC_kP_k
\le n e^{7/9}3^{M_k}k^{1/9}.
\tag{10}
\]

Since `x_k>=E_k`, combining `(9)` and `(10)` yields

\[
{\alpha k\over2\,3^{M_k}}
\le n e^{7/9}3^{M_k}k^{1/9}.
\]

Therefore

\[
3^{2M_k}
\ge{\alpha\over2n e^{7/9}}k^{8/9},
\]

which proves `(2)`.

## 4. Record-time strengthening

Now let `r` be a record time. Then

\[
D_r-D_m\ge0
\qquad(1\le m\le r).
\]

Every nonzero term in `(7)` is at least `1/2`, and hence

\[
E_r\ge{q_r\over2}\ge{\alpha r\over2}.
\tag{11}
\]

Again using the product bound,

\[
x_r=nC_rP_r
\le n e^{7/9}C_r r^{1/9}.
\tag{12}
\]

Combining `x_r>=E_r` with `(11)--(12)` gives

\[
C_r
\ge{\alpha\over2n e^{7/9}}r^{8/9},
\]

which is `(3)`.

If there were only finitely many record times, `M_k` would be bounded, contradicting `(2)`. Thus record times are unbounded and `(4)--(6)` follow.

## 5. Strategic consequence

Branch-qualified `T-6709` says that an ordinary realization of Lane A tends to infinity. The present theorem adds a genuinely necessary arithmetic burden:

```text
not merely D_k >= 0;
not merely D_k unbounded;
but coefficient records at time r must satisfy C_r >= const(n)*r^(8/9).
```

In particular, no bounded-discrepancy, critical mechanical, Sturmian, or other bounded-surplus completion can be the parity sequence of a positive ordinary Lane-A orbit.

This removes an infinite structural sublane rather than a bounded list of prefixes.

## 6. Gap audit

- The theorem does not exclude unbounded coefficient surplus.
- The constant depends on the initial integer `n`; no uniform contradiction is claimed.
- The record lower law is necessary, not sufficient, for an ordinary divergent orbit.
- Symbolic words satisfying the same surplus inequality may still select nonordinary `2`-adic completions.
- No proof of Collatz follows until the remaining unbounded-record Lane A and all of Lane B are excluded.

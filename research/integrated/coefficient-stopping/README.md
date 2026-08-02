# IC-SC-001 — coefficient-supercritical divergence and SC* equivalence

## Status

- **Mathematical status:** `VERIFIED` in the stated scope.
- **Repository role:** accepted integrated reference after merged PR #84.
- **Proof residency:** local proof packet.
- **Open obligation:** `SC*` itself is not proved.
- **Collatz status:** classifies and reformulates one failure lane; does not exclude it.

## Setup

For the shortcut map

\[
T(n)=
\begin{cases}
n/2,&n\equiv0\pmod2,\\
(3n+1)/2,&n\equiv1\pmod2,
\end{cases}
\]

let

\[
v_i\equiv T^i(n)\pmod2,
\qquad
q_k(n)=\sum_{i=0}^{k-1}v_i,
\qquad
C_k(n)=\frac{3^{q_k(n)}}{2^k}.
\]

Define the coefficient stopping time

\[
\tau_c(n)=\min\{k\ge1:C_k(n)<1\},
\]

with `τ_c(n)=∞` if no such `k` exists.

For `N≥0`, define

\[
S_N=\{n\ge1:C_k(n)\ge1\text{ for every }1\le k\le N\},
\qquad
m_N=\min S_N.
\]

Finite parity-cylinder bijectivity makes every `S_N` nonempty: all-supercritical finite words exist, and each length-`N` word has a positive residue class modulo `2^N`.

## Theorem A — all-time coefficient supercriticality forces divergence

If a positive ordinary orbit satisfies

\[
C_k(n)\ge1
\qquad(k\ge1),
\]

then

\[
T^k(n)\to+\infty.
\]

The same holds for a shifted tail: if every coefficient prefix measured from some time `r` is at least one, then the orbit from time `r` tends to infinity.

### Exact surplus identity

Put

\[
\alpha=\frac{\log2}{\log3},
\qquad a=1-\alpha,
\qquad D_k=q_k-\alpha k.
\]

Then `C_k=3^{D_k}`, and the hypothesis is `D_k≥0` for all `k`. The increments are

\[
D_{k+1}-D_k=
\begin{cases}
a,&v_k=1,\\
-\alpha,&v_k=0.
\end{cases}
\]

Writing

\[
T^k(n)=3^{D_k}n+E_k,
\]

the finite affine identity gives

\[
\boxed{
E_k=\frac12\sum_{m=1}^k v_{m-1}3^{D_k-D_m}.
}
\]

All summands are nonnegative.

### Low-band renewal lemma

Fix `H>0`, and count low-band odd endpoints by

\[
N_H(k)=\#\{1\le m\le k:v_{m-1}=1\text{ and }D_m<H+a\}.
\]

If `D_k<H` for infinitely many `k`, then `N_H(k)→∞`.

#### Proof

Assume only finitely many odd endpoints satisfy `D_m<H+a`, and choose a time `K` after the last one. Take a later `r` with `D_r<H`. There must be a future odd step; otherwise repeated even increments `-α` would force `D_k<0`, contradicting all-time supercriticality.

Let `t≥r` be the first future odd step. Every step from `r` to `t-1` is even, so `D_t≤D_r<H`. The odd step ends at

\[
D_{t+1}=D_t+a<H+a,
\]

a forbidden later low-band odd endpoint. Contradiction. ∎

### Proof of divergence

Let `M>0`. Choose `H` with

\[
3^Hn>M.
\]

If there are only finitely many visits below `H`, then eventually `D_k≥H`, and

\[
T^k(n)\ge3^{D_k}n\ge3^Hn>M.
\]

If there are infinitely many visits below `H`, the low-band lemma gives `N_H(k)→∞`. Choose `K` such that for all `k≥K`,

\[
N_H(k)>2M3^{H+a}.
\]

For `k≥K`, either `D_k≥H`, giving the preceding multiplicative bound, or `D_k<H`. In the second case, every index counted by `N_H(k)` has `D_m<H+a` and `D_k≥0`, so

\[
3^{D_k-D_m}>3^{-(H+a)}.
\]

The exact remainder identity gives

\[
E_k\ge\frac12N_H(k)3^{-(H+a)}>M.
\]

Thus every sufficiently late iterate exceeds `M`. Since `M` was arbitrary, `T^k(n)→∞`. ∎

## Theorem B — inverse coefficient-stopping equivalence

For every integer `B≥1` and `N≥0`,

\[
\boxed{
m_N>B
\iff
\tau_c(n)\le N\text{ for every }1\le n\le B.}
\]

Consequently,

\[
\boxed{
m_N\to\infty
\iff
\tau_c(n)<\infty\text{ for every positive integer }n.}
\]

This is the exact repository meaning of `SC*`.

### Proof

By definition,

\[
n\in S_N
\iff
\tau_c(n)>N.
\]

Therefore `m_N>B` exactly when no `1≤n≤B` lies in `S_N`, which is exactly when every such `n` has `τ_c(n)≤N`.

The sets `S_N` are nested, so `(m_N)` is nondecreasing. If some fixed `n` has `τ_c(n)=∞`, then `n∈S_N` for every `N`, hence `m_N≤n` and source escape fails.

Conversely, if `m_N` does not tend to infinity, monotonicity makes it bounded. A bounded integer-valued nondecreasing sequence eventually stabilizes at some `n`. Then `n` lies in every sufficiently late `S_N`, and nestedness supplies membership in all earlier levels, so `τ_c(n)=∞`. ∎

## Finite convergence certificates transfer to source lower bounds

Suppose a certified computation proves that every `1≤n≤B` reaches `1` within at most `R(B)` shortcut steps. If `n>1` and `σ_1(n)` is a hitting time,

\[
1=T^{\sigma_1(n)}(n)=C_{\sigma_1(n)}(n)n+E_{\sigma_1(n)},
\qquad E_{\sigma_1(n)}\ge0,
\]

so

\[
C_{\sigma_1(n)}(n)\le1/n<1.
\]

For `n=1`, the word `10` gives coefficient `3/4<1`. Therefore

\[
m_N>B
\qquad
(N\ge\max\{2,R(B)\}).
\]

This is a finite lower bound on `m_N`, not a proof of cofinal escape unless a cofinal family of certified ranges and maximal hitting times is supplied.

## Fixed-source valuation form

For a length-`N` parity word `w` of weight `q`, write

\[
T_w(x)=\frac{3^q x+A_w}{2^N}.
\]

A fixed positive integer `n` realizes `w` through depth `N` exactly when

\[
v_2(3^qn+A_w)\ge N.
\]

Thus `SC*` is equivalently the statement:

> For every fixed positive integer `n`, the lengths of all-supercritical words realized from `n` are bounded.

A sufficient closing theorem is a finite function `Φ(n)` such that every all-supercritical word `w` realized from `n` satisfies

\[
|w|\le\Phi(n).
\]

## Why it matters

The two theorems separate classification from exclusion:

```text
T-6709:
    if one fixed positive ordinary source never crosses,
    its orbit diverges to +infinity;

T-6710:
    emptying all such fixed-source paths is exactly universal
    finite coefficient stopping;

missing:
    a fixed-source valuation or canonical-boundary inequality.
```

The result therefore identifies one precise possible Collatz failure lane and the exact theorem needed to close it.

## Boundaries and common misreadings

- The divergence theorem assumes one positive ordinary source. It does not extract one from symbolic data.
- It proves no uniform divergence rate and no monotonicity.
- It does not contradict Collatz; divergence is a possible failure mode.
- The equivalence does not prove `SC*`.
- A moving sequence of compatible sources is not a fixed-source proof.
- Endpoint accumulation and low-band estimates do not automatically control the canonical initial residue.
- Zero entropy, thinness, or a 2-adic completion does not imply emptiness.
- This packet does not include later unreviewed additions on the PR #77 branch.

## Provenance

Primary source: PR #77 at

```text
3efcbfb2e38f02b04eb6bba35eb258ec552d655c
```

Files:

```text
research/positive-coefficient-gate/T-6709-supercritical-implies-divergence.md
research/positive-coefficient-gate/T-6710-SC-star-inverse-stopping-equivalence.md
research/positive-coefficient-gate/L-6711-canonical-low-band-source-endpoint-bound.md
```

Source author: `gpt56-positive-review-01`.

Independent review:

```text
reports/gpt56-complexity-01/2026-08-01-pre-public-review-76-77-79.md
@ 046eeda2268b4ac1b90a9618a4ed2460a111a0e5
```

Verdict: `VERIFIED WITH FIXES`, including terminology and provenance corrections. The review reconstructed the symbolic arguments; no large computation is a proof dependency.

## Next missing step

Prove a source-dependent upper bound on

\[
v_2(3^{q(w)}n+A_w)
\]

for every fixed positive `n` and every all-supercritical word `w`. A successful result should immediately be translated into an explicit lower bound for `m_N`.

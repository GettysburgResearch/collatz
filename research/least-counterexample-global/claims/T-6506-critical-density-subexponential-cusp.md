# T-6506 — An ordinary all-supercritical orbit must return to the critical density and to subexponential height

**Claim ID:** `T-6506`  
**Status:** `PROPOSED / SOURCE-DEPENDENT`  
**Authoring agent:** `gpt56-positive-02` (`GPT-5.6 Pro`)  
**Created:** 2026-07-31  
**Dependencies:** local `L-6501`, `T-6503`, `T-6504`; López--Stoll, *The 3x+1 Periodicity Conjecture in R*, arXiv:2101.12747, Theorem 1  
**Scope:** positive ordinary, nonperiodic, all-prefix coefficient-supercritical trajectories  
**Related candidates:** none

## 1. Statement

Let `n` be a positive ordinary integer whose shortcut-Collatz orbit is infinite and nonperiodic. Put

\[
q_k=\#\{0\le i<k:T^i(n)\text{ is odd}\},
\]

\[
\alpha={\log2\over\log3},
\qquad
D_k=q_k-\alpha k.
\]

Assume

\[
\boxed{D_k\ge0\qquad(k\ge1).}
\tag{1}
\]

Then, subject to the cited López--Stoll theorem in exactly this normalization,

\[
\boxed{
\liminf_{k\to\infty}{D_k\over k}=0.}
\tag{2}
\]

In particular no positive ordinary Lane-A orbit can satisfy a uniform positive linear drift

\[
D_k\ge\varepsilon k
\]

for all sufficiently large `k`.

Combine `(2)` with the exact local correction bound

\[
P_k\le e^{7/9}k^{1/9},
\qquad
T^k(n)=n\,3^{D_k}P_k.
\tag{3}
\]

There is a sequence `k_j -> infinity` such that

\[
\boxed{
{\log T^{k_j}(n)\over k_j}\longrightarrow0.}
\tag{4}
\]

Thus the orbit, although branch-qualifiably forced to tend to `+infinity`, returns at arbitrarily late times to **subexponential height in elapsed time**.

Together with local `T-6503` and `T-6504`, every such orbit simultaneously satisfies

\[
{1\over K}\sum_{k=1}^{K}D_k
\ge {8\over9}\log_3K-O_n(1),
\tag{5}
\]

\[
D_k\to+\infty\quad\text{in natural density one},
\tag{6}
\]

while still obeying the critical-boundary recurrence `(2)`.

## 2. Source specialization

López--Stoll Theorem 1 states, in the paper's parity-vector notation, that if a rational `2`-adic integer has a divergent, noncyclic trajectory, then

\[
\liminf_{k\to\infty}{q_k\over k}
={\log2\over\log3}.
\tag{7}
\]

An ordinary integer is a rational `2`-adic integer. Under `(1)`,

\[
{q_k\over k}=\alpha+{D_k\over k}\ge\alpha.
\]

Substituting `(7)` gives `(2)` immediately.

The source is used only for this critical-density equality. The local logarithmic mean, correction product, and density-zero low-band statements are independent exact ordinary-orbit arguments.

## 3. Subexponential cusp subsequence

Choose `k_j -> infinity` with

\[
D_{k_j}/k_j\to0.
\]

From `(3)`,

\[
\log T^{k_j}(n)
\le
\log n+{7\over9}+{1\over9}\log k_j
+(\log3)D_{k_j}.
\]

Divide by `k_j`. Every term on the right tends to zero, proving `(4)`.

## 4. The resulting oscillatory profile

The theorem forces three scales at once.

1. **Logarithmic mean bank.** Equation `(5)` says the average surplus diverges at least logarithmically.
2. **Sparse fixed-band returns.** Equation `(6)` and `T-6503` say every fixed band is visited only `O(K^(1/9))` times through time `K`.
3. **Critical relative dips.** Equation `(2)` says the surplus nevertheless falls below `epsilon k` infinitely often for every `epsilon>0`.

Therefore a surviving Lane-A orbit is neither a bounded-discrepancy path nor a uniformly positive-drift path. It must alternate between increasingly large coefficient banks and sublinear relative dips, while its physical values at a subsequence remain subexponential in time.

## 5. Why this matters

The four scalar estimates already present in PR #80 do not by themselves force `(2)`. The critical-density source theorem adds genuinely ordinary-rational information: a symbolic path with positive linear surplus cannot be the parity vector of an ordinary nonperiodic Collatz orbit.

This removes the full linear-drift sector of Lane A, including every path with

\[
\liminf q_k/k>\alpha.
\]

It does not remove logarithmically or otherwise sublinearly banked paths.

## 6. Dependency audit

- `L-6501` supplies `(3)`.
- `T-6503` and `T-6504` supply `(5)--(6)`.
- The source theorem is imported only in the form `(7)` and requires independent primary-source reconstruction before status promotion.
- No real-series value is identified with a `2`-adic limit.
- No eventual periodicity or finite-state assumption is made.

## 7. Gap audit

- The profile `(2),(5),(6)` is internally consistent; it is not yet a contradiction.
- A subexponential cusp subsequence may coexist with arbitrarily large excursions between those times.
- Almost-all descent theorems do not automatically eliminate one such exceptional orbit.
- The theorem assumes the orbit is ordinary. It does not extract an integer from an abstract parity word.

## 8. Suggested next attack

At the cusp times `k_j`, combine the two small canonical boundaries

\[
r_{k_j}=n,
\qquad
s_{k_j}=T^{k_j}(n)=\exp(o(k_j))
\]

with the complete `2`-adic/`3`-adic exponent-code equation. A proof that no all-prefix-supercritical word has both canonical boundary rates zero would close Lane A. Kramer's 2026 `2`--`3`--infinity diagnostic identifies precisely this target but currently supplies only necessary rates and finite experiments, not the missing lower bound.

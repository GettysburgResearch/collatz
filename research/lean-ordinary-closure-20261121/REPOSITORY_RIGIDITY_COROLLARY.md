# Exact repository consequences of the linear-block atom floor

## Status

These are written analytic corollaries of `LINEAR_BLOCK_ATOM_FLOOR.md`, using the existing repository comparison and coercivity statements at the frozen commits below. The new arithmetic word-injectivity premise is separately Lean checked. The analytic derivation, Tao's theorem, and the repository analytic implications are not represented as kernel-checked Lean dependencies here.

The conclusion is a finite-energy rigidity theorem. **The energy finiteness hypothesis remains unproved for a hypothetical nonconstant Collatz label.**

## 1. Fixed predecessor moments and ordinary components

For the ordinary shortcut map `T`, let

\[
\mathcal P(a)=\{n>0:\exists t\ge0,\ T^t n=a\}.
\]

The companion note proves that every positive ternary-unit target has positive lower logarithmic predecessor density:

\[
\liminf_{X\to\infty}\frac1{\log X}
\sum_{n\le X,\ n\in\mathcal P(a)}\frac1n>0
\qquad(3\nmid a). \tag{PLOG}
\]

Consequently, for every real `s <= 1`,

\[
\sum_{n\in\mathcal P(a)}n^{-s}=+\infty,
\tag{PM}
\]

because `n^(-s) >= 1/n` for positive integers `n`. The energy corollaries below use only `0 < s <= 1`.

The restriction `3` not dividing the target is genuine: if `3|a`, its direct predecessor set can consist only of doubling ancestors. Every ordinary component nevertheless contains a positive ternary unit. Starting from a positive multiple of three, remove all factors of two; the next shortcut step from the resulting odd integer is a ternary unit. Thus every nonempty ordinary component, and every nonempty invariant label class, has the logarithmic mass property (PLOG) and the moment property (PM).

## 2. Five energy and its complete hypotheses

Let `(Y,d)` be any metric space and let `f : N_(>0) -> Y` obey

\[
f(Tn)=f(n)\quad\text{for every positive }n.
\]

There is no boundedness hypothesis on the original metric label and no probability, density, or genericity hypothesis on its values. Define exactly the PR163 five energy

\[
E_5(s;f)=
\sum_{\substack{x>0\\x\text{ odd},\ 3\nmid x}}
x^{-s}d(f(5x),f(x)).
\]

All sums are nonnegative extended sums. No queries at odd multiples of three are included. The associated full tripling energy is

\[
D_3(s;f)=\sum_{n>0}n^{-s}d(f(3n),f(n)).
\]

At PR163 commit `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`,
`research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1 proves

\[
D_3(s;f)\le
\frac{248(7153/21)^s}{(1-2^{-s})^2}E_5(s;f)
\qquad(s>0).
\tag{FE1}
\]

Its harmonic constant can be replaced by `10000`. This is a comparison with five energy on the right; no reverse implication is used.

## 3. Subcritical rigidity for every `0 < s < 1`

Assume `0 < s < 1` and `E_5(s;f) < infinity`. Suppose two values are separated, say `D=d(f(a),f(b))>0`. The scalar label

\[
h(n)=\min\{d(f(n),f(a)),D\}
\]

is invariant, bounded, nonnegative, and 1-Lipschitz as a function of `f(n)`. Hence its five and tripling defects are bounded by those of `f`. FE1 gives finite tripling energy for `h`.

PR155 OD3, at commit `92f499b9d340d1ff8cc643c3eef3477d61b477c1`,
`research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`,
then supplies a real constant `c_h` with

\[
\sum_{n>0}|h(n)-c_h|n^{-s}<\infty.
\]

At least one of `|c_h|` and `|D-c_h|` is at least `D/2`. On the ordinary component of the corresponding source `a` or `b`, invariance makes this scalar difference constant and positive. Property (PM) contradicts the displayed finite sum. Therefore `f` is constant.

This discharges the predecessor-moment premise in **PR163 Section 4, “Subcritical coercivity,” for every `0 < s < 1`**. In particular it replaces the prior restriction to the source-qualified Krasikov--Lagarias moment at `s=0.84`. It also permits the critical retained-sieve exponent `rho=0.949955527...` to be used in a rigidity implication, if the missing full energy bound and any necessary propagation are proved.

## 4. Harmonic rigidity: logarithmic mass suffices

Assume `E_5(1;f) < infinity` and again form the separating bounded scalar label `h`. FE1 gives finite harmonic tripling energy. PR155 at the same commit,
`research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md`, Section 1, equations (E1)--(E3), gives a constant `c_h` such that

\[
a_k=2^{-k}\sum_{2^k\le n<2^{k+1}}|h(n)-c_h|\longrightarrow0.
\tag{4.1}
\]

This centered shell conclusion follows from the profile `L^1` convergence for bounded real labels; the Boolean specialization is not required. It implies

\[
\frac1{\log X}\sum_{n\le X}\frac{|h(n)-c_h|}{n}
\longrightarrow0.
\tag{4.2}
\]

Indeed, the reciprocal sum in dyadic shell `k` is at most `a_k`. Summing through `floor(log_2 X)` and applying the elementary Cesaro limit to `a_k -> 0` proves (4.2).

As above, at least one of the two separated ordinary components has `|h-c_h| >= D/2` throughout. It contains a positive ternary-unit target and all of that target's predecessors. Property (PLOG) contradicts (4.2). Therefore `f` is constant.

This replaces the **named positive-natural-lower-density hypothesis PD in PR163 Section 4, “Harmonic finite-energy rigidity,” equation (10)** by the newly proved, weaker sufficient property (PLOG). Mere divergence of harmonic predecessor mass would not suffice for this argument; the valuation cutoff in Section 6 of the companion note is essential to obtain the logarithmic lower density.

Combining Sections 3 and 4 gives the exact corollary

\[
\boxed{0<s\le1,\quad E_5(s;f)<\infty
\quad\Longrightarrow\quad f\text{ is constant}.}
\tag{RIGIDITY}
\]

The hypotheses are positivity of the integer domain, ordinary shortcut invariance, an actual metric, a positive exponent at most one, and finite five energy on the specified odd-unit domain. No external component-density hypothesis remains; the analytic dependencies listed in Section 6 remain.

For the shortest dependency chain of (RIGIDITY), the separate subcritical argument can be omitted: `x^(-1) <= x^(-s)` when `x >= 1` and `s <= 1`, so `E_5(1;f) <= E_5(s;f)`. The harmonic result alone proves all of (RIGIDITY). Section 3 is retained to identify explicitly the older KL premise that has been discharged, but OD3 is not an additional necessary input to the final corollary.

## 5. Exact impact on PR167 and the remaining obligations

At PR167 commit `e83cc8b35ad614c616df7c00318cc9645a174c34`,
`research/least-failure-closure-20261121/CLOSING_ENERGY_INTERFACES.md`:

- **CI3, equations (13)--(14):** the full source-weighted residual charge sum is still unproved. The present theorem does not establish its finiteness.
- **CI4, equations (17)--(20):** the actual discarded-index positive row recursion is unchanged. The incoming weighted column bound (19), or an actual-label substitute, is still unproved.
- **CI4, propagation paragraph:** finite directed adjacent energy has still not been shown to imply finite five energy. The zero-defect equivalence does not provide this missing comparison.
- **CI4, last paragraph:** once a valid five-energy bound is established at any exponent in `[rho,1]`, the former separate KL/PD rigidity premise can now be discharged by (RIGIDITY). The retained critical moment at `rho` alone is still only a retained-set estimate, not the full energy bound.

Thus this work closes a distributional input to the existing finite-energy strategy. It does not close its all-source analytic estimate, does not assert any cycle exclusion, and does not prove Collatz.

## 6. Frozen dependency ledger

| Input | Frozen source | Role |
|---|---|---|
| Fine-scale Syracuse mixing | Tao 2022, DOI `10.1017/fmp.2022.8`, Prop. 1.14, (1.26)--(1.27), consistency (1.23) | Only imported non-elementary theorem in the new atom-floor derivation |
| Selected-word strategy and weighted fixed-total count | El Jaouhari October 2026, DOI `10.5281/zenodo.23377671`, attributed through rStation paper 10 v2 Appendix A | Credited method; the counting proof and new linear block schedule are written in full locally |
| Five-to-tripling comparison | PR163 `051237135a34ae7d4b973ee5fcf5da04ded6f0fc`, `research/deep-reverse-closure-20261120/FIVE_SLICE_ENERGY.md`, FE1 | Converts finite specified five energy to finite full tripling energy |
| Subcritical coercivity (optional alternate proof) | PR155 `92f499b9d340d1ff8cc643c3eef3477d61b477c1`, `research/gemini-dirichlet-global-20261120/ORDINARY_DIRICHLET_COERCIVITY.md`, OD3 | Identifies the discharged older KL premise; not needed for (RIGIDITY), which follows from the harmonic case by monotonicity |
| Harmonic profile limit | Same PR155 commit, `research/gemini-dirichlet-global-20261120/ENDPOINT_BOUNDARY.md`, Section 1 | Finite harmonic tripling energy gives centered shell means tending to zero |
| Interface being strengthened | PR167 `e83cc8b35ad614c616df7c00318cc9645a174c34`, `research/least-failure-closure-20261121/CLOSING_ENERGY_INTERFACES.md`, CI3--CI4 | Separates the now-discharged predecessor premise from the unresolved energy/propagation estimates |

The underlying finite ordinary variation input to PR155 remains its stated repository dependency; its reconstruction and PR146 source hashes are in Section 8 of the pinned OD note. This checkpoint does not rerun or relabel that earlier verification.

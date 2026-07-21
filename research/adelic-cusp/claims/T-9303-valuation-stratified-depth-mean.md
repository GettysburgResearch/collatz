# T-9303 — Valuation-stratified depth-period decay

**Claim ID:** T-9303  
**Title:** Every fixed-frequency depth period contracts after the exact `3`-adic valuation loss  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9304`; the elementary cosine-grid lemma proved below  
**Scope:** fixed-frequency averaging over depth periods for the `64 -> 81` Fourier product  
**Related counterexample candidates:** none

## Statement

For `K >= 1` and a positive integer `theta`, write

\[
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}.
\]

For `m >= 0`, put

\[
P_m=9\cdot81^m.
\]

Let

\[
J=\{K_0,K_0+1,\ldots,K_0+P_m-1\}
\]

be any complete consecutive depth period satisfying

\[
K_0>m,
\qquad
17\theta<64^{K_0-m}. \tag{1}
\]

Define

\[
e(\theta)=
\left\lceil\frac{v_3(\theta)}4\right\rceil,
\qquad
L_m(\theta)=\max\{0,m+1-e(\theta)\}. \tag{2}
\]

Then

\[
\boxed{
\frac1{P_m}\sum_{K\in J}F_K(\theta)
\le
2^{-L_m(\theta)/2}
+
\frac{\pi\theta}{64^{K_0}}.
} \tag{3}
\]

The exponent loss in `(2)` is necessary at the level of the reciprocal-phase proof: if `81^d | theta`, the first `d` reciprocal phases are identically zero.

In particular, for each fixed `theta != 0`, once `m >= e(theta)`, the mean over **every** complete `P_m`-period decays exponentially in `m`, uniformly in the period's starting point subject to `(1)`.

## Definitions

The quantity `e(theta)` counts complete base-`81` phase levels consumed by the `3`-adic valuation of `theta`. If `v_3(theta)=4d`, exactly `d` levels are lost. If

\[
v_3(\theta)=4d+r,
\qquad r\in\{1,2,3\},
\]

then `d` levels are identically zero and the first remaining level is discarded because its grid can be valuation-degenerate; every later level still supplies a uniform contraction.

## Motivation

The issue-#4 depth-average argument says that `64^{-K}` runs through an arithmetic-progression subgroup modulo powers of `81`. That mechanism is correct, but the phrase “the Markov decomposition applies verbatim for every theta” hides a valuation exception: multiplication by `theta` can collapse the first several grids.

For example, at the reciprocal-phase level:

- `theta=81` makes the first phase identically zero over a `9`-depth period;
- `theta=9`, `m=0` gives the constant first-factor average
  \[
  |\cos(\pi/9)|\approx0.93969,
  \]
  not the claimed universal `2/pi+1/9` contraction.

These examples do not by themselves refute a bound for the **full** product, because deeper factors may contract. They do refute the unqualified first-`m+1`-factor proof. The theorem below repairs the proof exactly and is strong enough for the density-one synthesis in `T-9302`.

## Cosine-grid lemma

For every integer `q >= 2` and every real `phi`,

\[
\boxed{
\frac1q\sum_{j=0}^{q-1}
|\cos\pi(\phi+j/q)|
\le\frac1{\sqrt2}.
} \tag{4}
\]

Indeed, Cauchy--Schwarz gives

\[
\left(
\frac1q\sum_j|\cos\pi(\phi+j/q)|
\right)^2
\le
\frac1q\sum_j\cos^2\pi(\phi+j/q).
\]

Since

\[
\cos^2 x=\frac{1+\cos2x}{2}
\]

and the nontrivial `q`-th roots of unity sum to zero,

\[
\frac1q\sum_j\cos^2\pi(\phi+j/q)=\frac12.
\]

This proves `(4)`.

## Proof

### Step 1: truncate the product and remove the reciprocity errors

For `0 <= t <= m`, use the notation of `L-9304` and define

\[
P_{K,m}(\theta)
=
\prod_{t=0}^{m}
\left|
\cos\!\left(
\pi\frac{q_{K,t}(\theta)}{81^{t+1}}
\right)
\right|.
\]

Dropping all factors after level `m` can only increase the product. Equation `L-9304(4)`, the fact that `|cos(pi x)|` is `pi`-Lipschitz, and the standard telescoping bound for products of numbers in `[0,1]` give

\[
F_K(\theta)
\le
P_{K,m}(\theta)
+
\pi\sum_{t=0}^{m}
\frac{17\theta}{81^{t+1}64^{K-t}}.
\]

The geometric sum is bounded by

\[
\sum_{t=0}^{m}
\frac{17\theta}{81^{t+1}64^{K-t}}
\le
\frac{\theta}{64^K}. \tag{5}
\]

Therefore

\[
F_K(\theta)
\le
P_{K,m}(\theta)+\frac{\pi\theta}{64^K}. \tag{6}
\]

It remains to average the exact reciprocal product.

### Step 2: remove complete powers of 81 from the frequency

Write

\[
v_3(\theta)=4d+r,
\qquad r\in\{0,1,2,3\},
\qquad
\theta=81^d\theta_0.
\]

By `L-9304(8)`, the first `d` factors in `P_(K,m)(theta)` are `1`, and the remaining product is the same reciprocal product for `theta_0`, with both depth and level indices shifted by `d`.

If `d>m`, there is no active factor and the required reciprocal-product bound is `1`.

Assume `d<=m` and put

\[
M=m-d.
\]

The reduced vector is periodic with period `P_M`, while

\[
P_m=81^dP_M.
\]

Thus averaging over any `P_m` consecutive depths repeats the reduced complete period exactly `81^d` times. We may therefore assume from now on that `81` does not divide `theta` and prove:

\[
\operatorname{mean}_K P_{K,M}(\theta)
\le
\begin{cases}
2^{-(M+1)/2},&3\nmid\theta,\\[1mm]
2^{-M/2},&3\mid\theta.
\end{cases} \tag{7}
\]

### Step 3: expose the subgroup digits one level at a time

By `L-9304(7)`, over a complete period

\[
V_K=64^{-K}\pmod{81^{M+1}}
\]

is uniform on

\[
1+9\mathbb Z/81^{M+1}\mathbb Z.
\]

The phase at level `t` is

\[
q_{K,t}(\theta)
\equiv
-17\theta64^tV_K
\pmod{81^{t+1}}. \tag{8}
\]

#### Unit case

Suppose `3` does not divide `theta`.

At level `t=0`, the nine possible values of `V_K mod 81` form one coset of `9Z/81Z`. Multiplication by the unit `-17 theta` permutes that coset. The normalized phases therefore form an equally spaced `9`-point grid, so their conditional mean factor is at most `2^(-1/2)` by `(4)`.

For `t>=1`, condition on `V_K mod 81^t`. Its `81` lifts modulo `81^(t+1)` are

\[
V_K+k81^t,
\qquad 0\le k<81.
\]

All earlier phases are fixed. By `(8)`, the new normalized phase changes by

\[
\frac{-17\theta64^t k}{81}
\pmod1.
\]

The coefficient is a unit modulo `81`, so this is an equally spaced `81`-point grid. Conditional averaging charges another factor at most `2^(-1/2)`.

Iterating the conditional expectation from level `0` through level `M` proves the first line of `(7)`.

#### Residually divisible case

Now suppose

\[
v_3(\theta)=r\in\{1,2,3\}.
\]

Discard the level-`0` factor, bounding it by `1`. At every level `t>=1`, the same `81` lifts change the normalized phase by

\[
\frac{3^r u k}{81}
\pmod1
\]

for a unit `u`. This multiset consists of

\[
81/3^r\in\{27,9,3\}
\]

equally spaced points, each repeated `3^r` times. The conditional mean is again at most `2^(-1/2)` by `(4)`. There are `M` such levels, proving the second line of `(7)`.

Combining the two cases gives

\[
\operatorname{mean}_{K\in J}P_{K,m}(\theta)
\le
2^{-L_m(\theta)/2}. \tag{9}
\]

Finally average `(6)` over `J`. Since every `K in J` is at least `K_0`,

\[
\operatorname{mean}_{K\in J}
\frac{\pi\theta}{64^K}
\le
\frac{\pi\theta}{64^{K_0}}.
\]

Together with `(9)`, this proves `(3)`. QED.

## Dependency audit

- `L-9304` supplies the exact reciprocal phase, its period, and the `81`-valuation shift.
- The only analytic input is Cauchy--Schwarz and the exact second moment of an equally spaced cosine grid.
- No issue-#4 depth-block theorem is assumed.
- No independence between different depths is assumed; the proof averages a finite subgroup exactly.
- No computation is used.

## Gap audit

- The theorem is an average over complete periods, not a pointwise bound in `K`.
- The error term is kept explicitly. It is negligible in `T-9302` because its depth annuli begin at `9*81^m`, but it must not be dropped in shallow applications.
- Frequencies with large `v_3(theta)` lose contraction levels. Uniformly pretending otherwise is invalid.
- The result does not imply all-depth EQ; exceptional depths may remain infinite.
- The `1/sqrt(2)` constant is convenient and rigorous, not claimed optimal. Exact grid means are usually closer to `2/pi`.

## Adversarial tests

1. `theta=81^d`: the exponent is `max(0,m+1-d)`, exactly reflecting the first `d` zero reciprocal phases.
2. `theta=9`, `m=0`: `e(theta)=1`, so the theorem charges no contraction and correctly avoids the false first-factor bound.
3. `theta` prime to `3`: every one of the `m+1` levels is charged.
4. Starting the period at `K_0+1` merely cyclically permutes the subgroup orbit; the estimate is unchanged.
5. The proof still works when the full product contains a zero factor: dropping deeper factors and using upper bounds remains valid.

## Remaining uncertainty

The proof is complete-looking. Independent review should focus on the filtration argument in Step 3, especially the distinction between the initial `9`-point subgroup and the later `81`-lift fibers.

## Suggested next attack

Sum `(3)` over a growing low-frequency window by grouping frequencies according to `ceil(v_3(theta)/4)`. The rarity of highly divisible frequencies exactly compensates for their lost contraction levels. `T-9302` performs that summation.
# T-9302 — Density-one full EQ from frequency blocks and exact depth periods

**Claim ID:** T-9302  
**Title:** A frequency-block mean plus valuation-stratified depth periods implies the complete EQ Fourier criterion on density-one depths  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9302`, `T-9303`; the explicit frequency-block hypothesis below  
**Scope:** density-one synthesis for the issue-#4 EQ target  
**Related counterexample candidates:** none

## Statement

For `K >= 1` and `1 <= theta <= 2^K`, let

\[
F_K(\theta)=\frac{|S_K(\theta)|}{2^K}
\]

and

\[
E_K=
\sum_{1\le\theta\le2^K}
\frac{F_K(\theta)}\theta.
\]

Assume the following frequency-block estimate.

### Frequency-block mean `(FBM)`

There is a constant

\[
\frac1{81}<a<1
\]

such that, for every `K`, every `r >= 0` with `81^r <= 2^K`, and every interval `I` of exactly `81^r` consecutive frequencies contained in `{1,...,2^K}`,

\[
\frac1{81^r}
\sum_{\theta\in I}F_K(\theta)
\le a^r. \tag{FBM}
\]

Put

\[
b=2^{-1/2},
\qquad
\gamma=-\log_{81}b
=\log_{81}\sqrt2
\approx0.0788662192. \tag{1}
\]

Then, for every fixed

\[
0<\alpha<\gamma,
\]

there is a set `G` of positive integers of natural density `1` such that

\[
\boxed{
E_K\longrightarrow0
\quad\text{as }K\longrightarrow\infty,\ K\in G.
} \tag{2}
\]

More quantitatively, let

\[
P_m=9\cdot81^m,
\qquad
\mathcal I_m=[P_m,P_{m+1})\cap\mathbb Z,
\qquad
c=\frac{\gamma-\alpha}{2}>0. \tag{3}
\]

There is a constant `C_0` depending only on `alpha` such that, for every sufficiently large `m`, all but at most a

\[
C_0 81^{-cm}
\]

fraction of depths `K in I_m` satisfy

\[
\boxed{
E_K
\le
C_0 81^{-cm}
+
C_a a^{\lfloor\alpha m\rfloor},
} \tag{4}
\]

where `C_a` is the explicit shell constant from `L-9302`.

Only `(FBM)` remains a branch-qualified external input. The depth-period estimate used here is proved self-contained in `T-9303`; no uniform-in-`theta` version of issue #4's Theorem 12 is assumed.

## Definitions

A set `G` has natural density `1` when

\[
\lim_{N\to\infty}
\frac{|G\cap\{1,\ldots,N\}|}{N}=1.
\]

The low-frequency argument uses the stronger unweighted quantity

\[
G_m(K)=
\sum_{1\le\theta\le H_m}F_K(\theta),
\qquad
H_m=\lfloor81^{\alpha m}\rfloor. \tag{5}
\]

The frequency-block hypothesis is stated with all quantifiers visible. The intended branch-qualified source is the result called Theorem 11 in issue #4's `EQ.md`, whose text explicitly says “every full block.” This packet does not promote that source claim.

## Motivation

The first version of this claim assumed a depth-block bound uniform in `theta`. Auditing the source proof exposed a hidden `3`-adic valuation loss: a frequency divisible by `81^d` has `d` reciprocal phases equal to zero, and a residual factor divisible by `3`, `9`, or `27` collapses the initial grid.

`T-9303` repairs the depth argument with the exact loss

\[
\left\lceil\frac{v_3(\theta)}4\right\rceil.
\]

At first this appears dangerous for a growing frequency window. The key observation is that such frequencies are exponentially rare: losing one contraction level requires roughly four extra factors of `3`, a density cost of `1/81`, while regaining that contraction costs only `sqrt(2)`. Since

\[
\frac{\sqrt2}{81}<1,
\]

the valuation strata sum absolutely. The density-one theorem not only survives; its admissible exponent improves from the earlier conditional `0.06615` to `0.078866...`.

## Proof

### Step 1: valuation-stratified mean of the low-frequency mass

Fix a large `m`, and take any one of the `80` consecutive blocks `J` of length `P_m` that tile `I_m`.

For `theta >= 1`, define

\[
e(\theta)=
\left\lceil\frac{v_3(\theta)}4\right\rceil.
\]

Because `theta <= H_m` and `alpha < 1`, one has

\[
e(\theta)\le m
\]

for all sufficiently large `m`.

Every block `J` begins at a depth at least `P_m`. Thus the size condition in `T-9303` holds for every `theta <= H_m` once `m` is large. That theorem gives

\[
\frac1{|J|}
\sum_{K\in J}F_K(\theta)
\le
b^{m+1-e(\theta)}
+
\frac{\pi\theta}{64^{P_m}}. \tag{6}
\]

We now sum the main term over valuation strata.

There are at most `H_m` frequencies with `e(theta)=0`. For every `e >= 1`, the condition `e(theta)=e` implies

\[
v_3(\theta)\ge4e-3,
\]

so the number of such frequencies is at most

\[
\frac{H_m}{3^{4e-3}}
=
\frac{27H_m}{81^e}. \tag{7}
\]

Consequently

\[
\begin{aligned}
\sum_{1\le\theta\le H_m}
 b^{m+1-e(\theta)}
&\le
H_m b^{m+1}
\left[
1+27\sum_{e\ge1}
\left(\frac{b^{-1}}{81}\right)^e
\right]\\
&=C_v H_m b^{m+1}, \tag{8}
\end{aligned}
\]

where

\[
C_v
=
1+
27\frac{\sqrt2/81}{1-\sqrt2/81}
<1.48. \tag{9}
\]

The total reciprocity error in `(6)` satisfies

\[
\sum_{1\le\theta\le H_m}
\frac{\pi\theta}{64^{P_m}}
\le
\frac{\pi H_m(H_m+1)}{2\,64^{P_m}}. \tag{10}
\]

This is superexponentially smaller than the main term in `m`. Absorbing it into the constant, there is an absolute `C_1` such that

\[
\frac1{|J|}
\sum_{K\in J}G_m(K)
\le
C_1 H_m b^{m+1}. \tag{11}
\]

Since

\[
H_m\le81^{\alpha m},
\qquad
b^m=81^{-\gamma m},
\]

we obtain

\[
\frac1{|J|}
\sum_{K\in J}G_m(K)
\le
C_1 81^{-(\gamma-\alpha)m}
=C_1 81^{-2cm}. \tag{12}
\]

### Step 2: most depths have small total low-frequency mass

Apply Markov's inequality to `G_m(K)` with threshold

\[
C_0 81^{-cm},
\qquad
C_0=\sqrt{C_1}.
\]

Equation `(12)` shows that the fraction of depths in `J` violating

\[
G_m(K)\le C_0 81^{-cm} \tag{13}
\]

is at most

\[
C_0 81^{-cm}. \tag{14}
\]

The annulus `I_m` is the disjoint union of exactly `80` such blocks, because

\[
P_{m+1}-P_m=80P_m.
\]

The same exceptional fraction therefore holds in the whole annulus.

For every good depth,

\[
\sum_{1\le\theta\le H_m}
\frac{F_K(\theta)}\theta
\le
G_m(K)
\le
C_0 81^{-cm}. \tag{15}
\]

### Step 3: the frequency-block mean removes the high tail

Put

\[
M_m=\lfloor\alpha m\rfloor.
\]

For all sufficiently large `m`,

\[
81^{M_m}\le H_m<2^K.
\]

The frequencies above `H_m` are a subset of those above `81^(M_m)`. Applying `L-9302` with `(FBM)` gives

\[
\begin{aligned}
\sum_{H_m<\theta\le2^K}
\frac{F_K(\theta)}\theta
&\le
\sum_{81^{M_m}\le\theta\le2^K}
\frac{F_K(\theta)}\theta\\
&\le
C_a a^{M_m}. \tag{16}
\end{aligned}
\]

Combining `(15)` and `(16)` proves `(4)`.

### Step 4: natural density

Let `B_m` be the bad depths in `I_m`. From `(14)`,

\[
|B_m|
\le
C_0|I_m|81^{-cm}
=
80C_0P_m81^{-cm}. \tag{17}
\]

Up to the endpoint `P_(M+1)`, the total number of bad depths is bounded by a geometric sum

\[
\sum_{m\le M}O(81^{(1-c)m})
=O(81^{(1-c)M}).
\]

Dividing by

\[
P_{M+1}=9\cdot81^{M+1}
\]

gives `O(81^(-cM))`, which tends to zero. Intermediate endpoints change only the constant. Hence the union of the good depths has natural density `1`, and `(4)` implies `(2)`. QED.

## Dependency audit

- `T-9303` supplies the complete-period mean with the exact `v_3(theta)` loss and explicit error.
- The geometric valuation sum `(8)` is new to this theorem.
- `L-9302` converts `(FBM)` into the high-frequency harmonic tail.
- `(FBM)` is the only branch-qualified mathematical input.
- Markov's inequality and geometric-series counting prove the density statement.
- No independence between frequencies or depths is assumed.

## Gap audit

- This remains conditional on `(FBM)` until the frequency-block theorem is independently reconstructed or imported.
- Density-one convergence is not all-depth convergence. The exceptional set may contain an infinite structured sequence and could still contain an M1 witness.
- The valuation-stratified depth theorem controls a sum for most depths; it does not provide a pointwise maximum for every depth.
- The exponent `gamma` is a union-bound exponent, not claimed optimal.
- The tiny reciprocity errors are bounded rather than silently removed.
- The conclusion is the weighted EQ Fourier criterion, not nonexistence of an ordinary integer in the infinite survivor attractor.

## Adversarial tests

1. **Valuation loss cannot be omitted.** Frequencies `theta=81^d` have `d` initial zero reciprocal phases.
2. **Rarity compensates loss.** The ratio between successive valuation-stratum contributions is at most `sqrt(2)/81`, strictly below `1`.
3. **Endpoint exponent.** If `alpha=gamma`, the low-frequency mean in `(12)` need not decay; the strict inequality is necessary for this proof.
4. **Arbitrary block alignment.** `T-9303` works on every complete period, so the `80`-block tiling is legitimate.
5. **No maximum/average confusion.** The proof obtains a small total low-frequency mass for most depths, which is stronger than simultaneous pointwise smallness on those depths.

## Remaining uncertainty

The implication is complete-looking. Independent review should first reconstruct `T-9303`, then verify the arbitrary-consecutive-block quantifier in `(FBM)` and the final incomplete-shell estimate in `L-9302`.

## Suggested next attack

The density-one exceptional set is now produced without an unverified depth input. Study its cross-scale structure: if a depth is bad in several adjacent annuli, the valuation-stratified proof forces a coherent family of low-frequency phase grids. An inverse theorem for that coherence could upgrade density-one EQ toward all-depth EQ.
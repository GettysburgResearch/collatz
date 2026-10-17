# T-9309 — Unconditional density-one full EQ

**Claim ID:** T-9309  
**Title:** The complete weighted EQ criterion holds on a natural-density-one set of depths without external average hypotheses  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9303`, `T-9308`; elementary valuation stratification and Markov's inequality  
**Scope:** unconditional density-one quantitative near-emptiness for the `64 -> 81` survivor subsystem  
**Related counterexample candidates:** none

## Statement

For

\[
F_K(h)=\frac{|S_K(h)|}{2^K},
\]

define the complete weighted EQ sum

\[
E_K=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h.
\tag{1}
\]

Put

\[
b=2^{-1/2},
\qquad
\gamma_0=-\log_{81}b
=
\log_{81}\sqrt2.
\tag{2}
\]

Let `delta>0` be the uniform harmonic-tail exponent from `T-9308`.

For every fixed

\[
0<\alpha<\gamma_0,
\tag{3}
\]

there exists a set `G` of positive integers of natural density `1` such that

\[
\boxed{
E_K\longrightarrow0
\quad\text{as }K\to\infty,\ K\in G.
}
\tag{4}
\]

More quantitatively, define

\[
P_m=9\cdot81^m,
\qquad
\mathcal I_m=[P_m,P_{m+1})\cap\mathbb Z,
\tag{5}
\]

\[
H_m=\lfloor81^{\alpha m}\rfloor,
\qquad
c=\frac{\gamma_0-\alpha}{2}>0.
\tag{6}
\]

There are absolute constants `C_0,C_1` such that, for every sufficiently large `m`, all but at most a

\[
\boxed{
C_0 81^{-cm}
}
\tag{7}
\]

fraction of depths `K in I_m` satisfy

\[
\boxed{
E_K
\le
C_0 81^{-cm}
+
C_1 81^{-\alpha\delta m}
+
\pi2^{-5K}.
}
\tag{8}
\]

The right-hand side tends to zero exponentially in `m`.

No branch-qualified frequency-block mean, issue-#4 depth theorem, external Fourier-decay theorem, or computation is assumed.

### Optimized displayed rate

Choosing

\[
\alpha_*
=
\frac{\gamma_0}{1+2\delta}
\tag{9}
\]

balances the two exponents:

\[
\frac{\gamma_0-\alpha_*}{2}
=
\alpha_*\delta
=
\frac{\gamma_0\delta}{1+2\delta}.
\tag{10}
\]

No optimality is claimed; this simply gives one explicit common decay rate.

## Definitions

A set `G` has natural density `1` when

\[
\lim_{N\to\infty}
\frac{|G\cap\{1,\ldots,N\}|}{N}
=1.
\]

The low-frequency mass is

\[
\mathcal L_m(K)
=
\sum_{1\le h\le H_m}F_K(h).
\tag{11}
\]

This unweighted quantity dominates the weighted low-frequency part of `E_K` and is convenient for depth averaging.

`T-9309` supersedes the role of conditional `T-9302`: its low-frequency depth argument is valuation-stratified as before, but `T-9308` now supplies the high-frequency tail unconditionally.

## Motivation

The first density-one synthesis required two branch-qualified average inputs. The valuation audit replaced the depth input by self-contained `T-9303`, leaving only the frequency-block theorem to remove high frequencies.

`T-9308` removes that final dependency. It proves a uniform high-frequency harmonic tail from exact lift-digit entropy. The two self-contained ingredients fit perfectly:

- `T-9303` controls a slowly growing low-frequency window for most depths;
- `T-9308` controls every frequency above that window at every depth.

The result is the first complete weighted EQ theorem in the packet with no external mathematical hypothesis, albeit only along density-one depths.

This is a quantitative near-emptiness statement for finite survivors. It does not rule out one exceptional infinite ordinary integer and does not resolve Collatz.

## Proof

### Step 1: tile each depth annulus by complete periods

The annulus

\[
\mathcal I_m=[P_m,P_{m+1})
\]

has length

\[
P_{m+1}-P_m
=80P_m.
\]

Hence it is the disjoint union of exactly `80` consecutive blocks `J` of length `P_m`.

Fix one such block.

### Step 2: average the low-frequency mass by valuation strata

For an integer `h>=1`, put

\[
e(h)=
\left\lceil
\frac{v_3(h)}4
\right\rceil.
\tag{12}
\]

Every block `J` begins at depth at least `P_m`. For all sufficiently large `m` and every `h<=H_m`, the size condition of `T-9303` holds. Therefore

\[
\frac1{|J|}
\sum_{K\in J}F_K(h)
\le
b^{m+1-e(h)}
+
\frac{\pi h}{64^{P_m}}.
\tag{13}
\]

For `e>=1`, the condition `e(h)=e` implies

\[
v_3(h)\ge4e-3.
\]

Thus the number of `h<=H_m` in that stratum is at most

\[
\frac{27H_m}{81^e}.
\tag{14}
\]

Summing the main term of `(13)` gives

\[
\begin{aligned}
\sum_{h\le H_m}
b^{m+1-e(h)}
&\le
H_m b^{m+1}
\left[
1+27\sum_{e\ge1}
\left(
\frac{b^{-1}}{81}
\right)^e
\right]\\
&=
C_v H_m b^{m+1},
\end{aligned}
\tag{15}
\]

where

\[
C_v
=
1+27
\frac{\sqrt2/81}{1-\sqrt2/81}
<1.48.
\tag{16}
\]

The total reciprocity error satisfies

\[
\sum_{h\le H_m}
\frac{\pi h}{64^{P_m}}
\le
\frac{\pi H_m(H_m+1)}{2\,64^{P_m}},
\tag{17}
\]

which is superexponentially smaller than the main term in `m`.

Consequently, for an absolute `C_2`,

\[
\frac1{|J|}
\sum_{K\in J}\mathcal L_m(K)
\le
C_2H_m b^m.
\tag{18}
\]

Since

\[
H_m\le81^{\alpha m},
\qquad
b^m=81^{-\gamma_0m},
\]

we obtain

\[
\boxed{
\frac1{|J|}
\sum_{K\in J}\mathcal L_m(K)
\le
C_2 81^{-(\gamma_0-\alpha)m}
=
C_2 81^{-2cm}.
}
\tag{19}
\]

### Step 3: most depths have small low-frequency mass

Apply Markov's inequality to `mathcal L_m(K)` with threshold

\[
C_0 81^{-cm},
\qquad
C_0=\sqrt{C_2}.
\]

Equation `(19)` shows that the fraction of depths in `J` violating

\[
\mathcal L_m(K)
\le
C_0 81^{-cm}
\tag{20}
\]

is at most

\[
C_0 81^{-cm}.
\tag{21}
\]

The same fraction bound holds in the union of the `80` equal blocks, hence throughout `I_m`.

For every good depth,

\[
\sum_{1\le h<H_m}
\frac{F_K(h)}h
\le
\mathcal L_m(K)
\le
C_0 81^{-cm}.
\tag{22}
\]

### Step 4: remove the high-frequency tail unconditionally

Apply `T-9308` with cutoff `M=H_m`. It gives

\[
\sum_{H_m\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}H_m^{-\delta}
+
\pi2^{-5K}.
\tag{23}
\]

For sufficiently large `m`,

\[
H_m
\ge
\frac12 81^{\alpha m},
\]

so

\[
H_m^{-\delta}
\le
2^\delta81^{-\alpha\delta m}.
\tag{24}
\]

Combining `(22)`--`(24)` proves `(8)` after absorbing `2^delta` into `C_1`.

### Step 5: natural density

Let `B_m` be the bad depths in `I_m`. By `(21)`,

\[
|B_m|
\le
C_0|I_m|81^{-cm}
=
80C_0P_m81^{-cm}.
\tag{25}
\]

Up to `P_(M+1)`, the total number of bad depths is at most

\[
\sum_{m\le M}
O(81^{(1-c)m})
=
O(81^{(1-c)M}).
\]

Dividing by

\[
P_{M+1}=9\cdot81^{M+1}
\]

gives `O(81^(-cM))`, which tends to zero. Intermediate endpoints change only the constant. Thus the good depths have natural density `1`, and `(8)` proves `(4)`. QED.

## Dependency audit

- `T-9303` supplies the valuation-stratified complete-period mean.
- `T-9308` supplies the uniform harmonic high-frequency tail.
- The valuation count and Markov/density arguments are reproduced in full.
- No issue-#4 frequency-block theorem is used.
- No external result or computation is used.

## Gap audit

- Density-one convergence is not all-depth convergence.
- The exceptional depth set can be infinite and may contain an M1 witness.
- The exponents are crude and not claimed optimal.
- The theorem proves a Fourier discrepancy criterion for finite survivor sets, not nonexistence of an infinite ordinary survivor.
- The result depends on the positive `delta` from `T-9308`; improving constants does not remove the exceptional depths.

## Adversarial tests

1. If `alpha=gamma_0`, the averaged low mass no longer decays; strict inequality in `(3)` is necessary for this proof.
2. Frequencies with large `v_3` lose depth contractions, but their strata are summable because `sqrt(2)/81<1`.
3. The high tail holds at every depth, so no independence between the low-depth and high-frequency arguments is assumed.
4. The `80`-period tiling is exact.
5. A depth can remain bad at infinitely many scales without contradicting density one; the theorem makes no stronger claim.

## Remaining uncertainty

The proof is complete-looking. Independent review should prioritize `T-9307` and `T-9308`, because they are the new ingredients that remove the external frequency-block hypothesis. The valuation/density part was already isolated in the earlier conditional theorem.

## Suggested next attack

Study the exceptional depths produced by `(20)` across adjacent scales. If one depth is bad for many `m`, it supports a coherent family of low-energy lift-prefix residue classes. Combining `L-9309`, `R-9301`, and the entropy bound should expose a finite carry-template obstruction and may upgrade density-one EQ toward all-depth EQ.
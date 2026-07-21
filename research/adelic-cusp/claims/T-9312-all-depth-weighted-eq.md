# T-9312 — All-depth complete weighted EQ

**Claim ID:** T-9312  
**Title:** The complete weighted Fourier criterion converges to zero at every depth  
**Status:** PROPOSED  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `T-9311`, `T-9308`; elementary harmonic summation  
**Scope:** full all-depth EQ criterion for the `64 -> 81` survivor subsystem  
**Related counterexample candidates:** none

## 1. Statement

For

\[
F_K(h)=\frac{|S_K(h)|}{2^K},
\]

define

\[
E_K
=
\sum_{1\le h\le2^K}
\frac{F_K(h)}h.
\tag{1}
\]

Then

\[
\boxed{
E_K\longrightarrow0
\qquad(K\to\infty)
}
\tag{2}
\]

with no exceptional sequence of depths.

More quantitatively, let

\[
b_*
=
\frac{2}{21314\log(1+\log64/\log(81/64))}
>0
\tag{3}
\]

be the pointwise exponent from `T-9311`, and let `delta>0` and `C_tail` be the uniform tail constants from `T-9308`.

There are absolute constants `C_0,C_1` and `K_0` such that, for every `K>=K_0`,

\[
\boxed{
E_K
\le
C_0
(1+\log K)
\left(
\frac{\log K}{K}
\right)^{b_*}
+
C_1K^{-\delta}
+
\pi2^{-5K}.
}
\tag{4}
\]

Every term on the right tends to zero.

## 2. Proof

Split the weighted sum at the growing cutoff

\[
M_K=K.
\tag{5}
\]

For sufficiently large `K`, one has

\[
81\le K\le2^K.
\]

### Low-frequency part

Apply `T-9311(12)` with polynomial exponent `R=1`. There is an absolute constant `C_0` such that

\[
\max_{1\le h<K}F_K(h)
\le
C_0
\left(
\frac{\log K}{K}
\right)^{b_*}
\tag{6}
\]

for every sufficiently large `K`.

Therefore

\[
\begin{aligned}
\sum_{1\le h<K}
\frac{F_K(h)}h
&\le
C_0
\left(
\frac{\log K}{K}
\right)^{b_*}
\sum_{1\le h<K}\frac1h\\
&\le
C_0
(1+\log K)
\left(
\frac{\log K}{K}
\right)^{b_*}.
\end{aligned}
\tag{7}
\]

Because `b_*>0`, the last expression tends to zero.

### High-frequency part

Apply `T-9308` with cutoff `M=K`. It gives, uniformly at every depth,

\[
\sum_{K\le h\le2^K}
\frac{F_K(h)}h
\le
C_{\rm tail}K^{-\delta}
+
\pi2^{-5K}.
\tag{8}
\]

Adding `(7)` and `(8)` proves `(4)` and hence `(2)`. QED.

## 3. What has changed

The former theorem chain split the problem into:

1. a uniform high-frequency harmonic tail, already closed by `T-9308`;
2. harmonic control of sparse low-energy classes near the origin, formerly `C-9301`.

`L-9310` and `T-9311` replace the second item by a deterministic pointwise theorem. The low-energy classes cannot remain exceptional for long because their signed phase chain has integral carries. Long stretches without a nonzero carry violate completion-height separation. The resulting pointwise decay is weak but uniform, and harmonic weighting needs only a positive exponent.

Thus the all-depth proof does not require:

- a Borel--Cantelli interchange;
- closure of the inverse-limit room tower at a finite modulus;
- a frequency-block mean;
- a depth average;
- an external self-similar Fourier-decay theorem;
- or an ordinary-integer realization hypothesis.

The tower and density theorems remain valuable independent descriptions and review cross-checks, but they are no longer the logical obstruction to weighted EQ.

## 4. Relationship to issue #4

Within this packet, equation `(2)` is the exact complete weighted EQ target.

Issue #4 records branch-qualified downstream consequences through its Erdős--Turán and survivor-counting interfaces. Subject to independent reconstruction and integration of those interfaces, `T-9312` upgrades the previous density-one fair-window equidistribution and minimal-survivor law to **every depth**.

No downstream issue-#4 claim is silently promoted in this file. The cross-branch consequence remains `PROPOSED` until the ledgers and notation are reconciled.

## 5. Relationship to the Collatz counterexample objective

The theorem is a strong all-depth quantitative near-emptiness result for finite survivor sets. It does **not** by itself settle whether the infinite `2`-adic survivor attractor contains one exceptional ordinary positive integer.

That direct existence problem remains `Q-9301`:

\[
\Phi(\Omega)\cap\mathcal I.
\]

A single ordinary-integer survivor may be compatible with very strong finite-depth equidistribution. Therefore this theorem does not construct a Collatz counterexample, prove that none exists, or resolve the Collatz conjecture.

## Dependency audit

- `T-9311` supplies pointwise decay throughout the polynomial low window at every depth.
- `T-9308` supplies the harmonic tail above any growing cutoff at every depth.
- The proof uses only the elementary bound for a harmonic sum.
- `T-9303`, `T-9309`, and `T-9310` are not dependencies; they provide independent averaged and uniform-density cross-checks.
- No branch-qualified issue-#4 theorem is needed to establish equation `(2)` itself.
- No computation or external theorem is used.

## Gap audit

- Every load-bearing claim remains `PROPOSED` pending independent reconstruction.
- The numerical exponent is tiny, so the displayed finite-depth bound is not intended for practical computation.
- The theorem closes weighted EQ, not the separate ordinary-integer intersection problem.
- Any claim about minimal survivors or ordinary Collatz trajectories additionally requires the exact issue-#4 translation to be checked.

## Adversarial tests

1. The low cutoff grows only polynomially, so `T-9311` supplies more than enough pointwise control.
2. The high tail begins at the same cutoff, leaving no frequency gap.
3. The point `h=0` never enters the Erdős--Turán sum.
4. Frequencies with large powers of `64` are already included in `T-9311` through exact shallower-copy reduction.
5. No independence between the low-frequency and high-frequency arguments is assumed.

## Remaining uncertainty

The proof of this file is elementary once its two inputs are accepted. Independent review should therefore concentrate on:

1. `L-9310` — integral carries and zero-run height rigidity;
2. `T-9311` — the pointwise Fourier translation;
3. `T-9307` / `T-9308` — the entropy-to-tail chain.

## Suggested next attack

With weighted EQ proposed at every depth, shift the main research frontier to the ordinary-integer section. Combine:

- `D-9302`'s adelic integer-section formulation;
- PR #20's repetition-complexity lower bound;
- the general completion-height mechanism of `L-9310`;
- and the issue-#4 chart congruences.

The next decisive theorem should force any hypothetical ordinary survivor to carry incompatible amounts of symbolic novelty and arithmetic height.
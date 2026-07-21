# C-9301 — Logarithmic cusp scattering

**Claim ID:** C-9301  
**Title:** Every polynomially small numerator encounters logarithmically many uniformly nondegenerate phases  
**Status:** IDEA  
**Authoring agent:** `gpt56-pro-04`  
**Reviewing agents:** none  
**Created:** 2026-07-21  
**Last updated:** 2026-07-21  
**Dependencies:** `L-9301`, `T-9301`  
**Scope:** proposed all-depth closure lemma for the issue-#4 EQ target  
**Related counterexample candidates:** none

## Statement

For `K >= 1`, `1 <= theta <= 2^K`, and `0 <= t < K`, put

\[
M_{K,t}=64^{K-t}.
\]

Let `s_(K,t)(theta)` be the unique signed integer representative in

\[
\left(-\frac{M_{K,t}}2,\frac{M_{K,t}}2\right]
\]

satisfying

\[
\boxed{
 s_{K,t}(\theta)
 \equiv17\theta\,81^{-(t+1)}
 \pmod{M_{K,t}}.
} \tag{1}
\]

Equivalently, the `t`-th factor in `L-9301` has absolute value

\[
\left|
\cos\!\left(
 \pi\frac{s_{K,t}(\theta)}{M_{K,t}}
\right)
\right|.
\]

### Conjecture

There exist constants

\[
A>0,
\qquad
c>0,
\qquad
0<\delta<\frac12,
\qquad
K_0,
\]

such that, for every `K >= K_0` and every integer

\[
1\le\theta\le K^A,
\]

the scattering set

\[
\mathcal B_{K,\theta}(\delta)
 =\left\{
 0\le t<K:
 |s_{K,t}(\theta)|
 \ge\delta M_{K,t}
 \right\}
\]

satisfies

\[
\boxed{
|\mathcal B_{K,\theta}(\delta)|
\ge c\log K.
} \tag{2}
\]

Any proof of `(2)` implies the polynomial-window maximal estimate `(PWM)` in `T-9301`, and hence—assuming the independently verified frequency-block mean—full all-depth EQ.

## Definitions

A phase is *delta-degenerate* when

\[
|s_{K,t}(\theta)|<\delta M_{K,t};
\]

it is *delta-scattered* otherwise. The signed representative measures distance to the nearest integer, so both ends of the unit interval are treated as the same degeneracy.

Only `c log K` scattered positions are requested. A positive density of scattered positions would be vastly stronger than necessary.

## Motivation

By `L-9301`,

\[
F_K(\theta)
=\prod_{t=0}^{K-1}
\left|
\cos\!\left(
 \pi\frac{s_{K,t}(\theta)}{M_{K,t}}
\right)
\right|.
\]

The issue-#4 cascade lemmas control coherent runs of very small signed representatives but leave scattered near-degeneracies. The weighted-shell reduction `T-9301` changes the target: it is no longer necessary to prove random-looking behavior at a positive fraction of all `K` levels or for exponentially many frequencies. It is enough to force logarithmically many decisive losses for polynomially many low-height numerators.

This is intended as the flagship theory problem of the packet.

## Proof of the claimed consequence

Assume `(2)`. At every scattered position,

\[
\left|
\cos\!\left(
 \pi\frac{s_{K,t}(\theta)}{M_{K,t}}
\right)
\right|
\le\cos(\pi\delta)<1.
\]

Every other factor is at most `1`. Therefore

\[
F_K(\theta)
\le\cos(\pi\delta)^{c\log K}.
\]

Set

\[
b=-c\log(\cos(\pi\delta))>0.
\]

Using natural logarithms,

\[
\cos(\pi\delta)^{c\log K}
=K^{-b}.
\]

Thus, uniformly for `1 <= theta <= K^A`,

\[
F_K(\theta)\le K^{-b},
\]

which is exactly `(PWM)` from `T-9301`. QED for the implication; the scattering statement itself remains open.

## Exact carry reformulation

For every `t`, congruence `(1)` is equivalent to an integer equation

\[
\boxed{
17\theta
=81^{t+1}s_{K,t}(\theta)
 +64^{K-t}m_{K,t}(\theta)
} \tag{3}
\]

for a unique integer carry `m_(K,t)(theta)` after the signed representative is fixed.

Adjacent representatives obey

\[
\boxed{
 s_{K,t}(\theta)
 \equiv81s_{K,t+1}(\theta)
 \pmod{64^{K-t-1}}.
} \tag{4}
\]

Thus a hypothetical failure of `(2)` is not an arbitrary collection of lucky cosine factors. It is a long low-height chain of exact `{2,3}`-unit relations with very few macroscopic representatives.

Equations `(3)` and `(4)` are proposed as the arithmetic entry point for a proof.

## Dependency audit

- `L-9301` supplies the exact cosine product.
- `T-9301` proves that the resulting polynomial-window decay is sufficient for EQ under the frequency block mean.
- Equations `(3)` and `(4)` follow directly from modular inversion; no probabilistic model is used.
- No existing cascade theorem is assumed in the conjecture, although those results may be useful in a proof.

## Gap audit

- The conjecture is unproved and may fail on a sparse sequence of depths and numerators.
- Average block decay does not imply `(2)` for every numerator.
- Existing bounds on the length of a single degenerate run do not automatically give logarithmically many scattered positions; degeneracies could be separated.
- A computation through any finite depth cannot establish the uniform quantifiers.
- The constants may need to be extremely small. Their numerical size is irrelevant to the qualitative implication.
- Failure of this sufficient condition would not refute EQ; products can decay through many moderately nondegenerate factors without any fixed `delta` threshold meeting `(2)`.

## Adversarial tests

1. Frequencies divisible by `64^j` satisfy the exact reduction
   \[
   F_K(64^j\theta)=F_{K-j}(\theta).
   \]
   Any proposed proof must survive this self-similarity rather than assuming every numerator is odd.
2. A long initial exact cascade may consume `O(log K)` levels for polynomial `theta`; the desired scattered positions may have to occur later.
3. The trivial frequency `theta=0` has no scattered positions and is explicitly excluded.
4. Near the final levels, `M_(K,t)` is small. A proof that uses only those levels risks producing at most a bounded number of losses and cannot establish `(2)`.

## Remaining uncertainty

The strongest uncertainty is whether a fixed threshold `delta` can be uniform in `K`, or whether the correct theorem must use a multiscale loss such as

\[
\sum_t
\left\|\frac{s_{K,t}}{M_{K,t}}\right\|^2
\ge c\log K.
\]

That quadratic-energy version would also imply polynomial product decay and may be more stable under scattered near-misses.

## Suggested next attack

Prove an **exceptional-frequency amplification lemma**: if one low-height `theta` has fewer than `c log K` scattered phases, then a full interval of nearby numerators inherits enough of the same phase pattern to violate the frequency-block mean. If local amplification loses too much at fine scales, use equations `(3)` and `(4)` to classify the exact carry tree before applying the block estimate.

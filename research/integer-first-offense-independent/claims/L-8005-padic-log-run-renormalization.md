# L-8005 — The divisible-seven run core is an exact 2-adic logarithmic renormalization

**Claim ID:** `L-8005`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `L-8002` and `L-8004`; elementary `2`-adic logarithm and LTE  
**Scope:** legal maximal-run transitions in the invariant `7|z` subchart

## 1. Setup

In the invariant divisible-seven chart of `L-8004`, write a section state as

\[
 z=7\,2^{3r}v,
 \qquad r\ge0,
 \qquad v>0\text{ odd}.
\tag{1}
\]

A completed macro of current run length `r` and next run length `s` obeys

\[
\boxed{
2^{4+3s}v^+=9^{r+1}v+1.}
\tag{2}
\]

The current and next `B`-legality conditions imply

\[
-v\in1+8\mathbf Z_2,
\qquad
-v^+\in1+8\mathbf Z_2.
\tag{3}
\]

## 2. Base-nine logarithm coordinate

The map

\[
\mathbf Z_2\longrightarrow1+8\mathbf Z_2,
\qquad
\alpha\longmapsto9^\alpha
\tag{4}
\]

is a continuous group isomorphism. Denote its inverse by

\[
\log_9:1+8\mathbf Z_2\longrightarrow\mathbf Z_2.
\tag{5}
\]

For a legal core put

\[
\boxed{\alpha=\log_9(-v).}
\tag{6}
\]

Then every legal transition `(2)` satisfies

\[
\boxed{
\nu_2(\alpha+r+1)=1+3s.}
\tag{7}
\]

In particular,

\[
\boxed{
s\ge5
\quad\Longleftrightarrow\quad
\alpha\equiv-r-1\pmod {2^{16}}}
\tag{8}
\]

along a legal trajectory.

Thus the pointwise run-five condition is one fixed-depth Hensel ball in the logarithmic coordinate, not a large collection of unrelated congruences in the ordinary core.

## 3. Exact renormalization map

Put

\[
 w=\alpha+r+1.
\tag{9}
\]

For nonzero `w in Z_2`, define the normalized unit

\[
\boxed{
\mathcal U(w)
=
\frac{9^w-1}{2^{3+\nu_2(w)}}.}
\tag{10}
\]

For every legal transition, `(7)` makes `(10)` integral and `(2)` gives

\[
\boxed{-v^+=\mathcal U(w).}
\tag{11}
\]

Consequently the next logarithmic coordinate is

\[
\boxed{
\alpha^+
=
\log_9\!\left(
\mathcal U(\alpha+r+1)
\right).}
\tag{12}
\]

Equations `(7)` and `(12)` are an exact `2`-adic Gauss/renormalization form of the ordinary run-core map:

```text
current integer core v
 -> logarithmic coordinate alpha=log_9(-v)
 -> return depth s=(v2(alpha+r+1)-1)/3
 -> normalized unit U(alpha+r+1)
 -> next coordinate alpha+.
```

No ordinary integrality conclusion is inferred from this coordinate change; it is an exact reformulation of an already legal integer transition.

## Proof

### The base-nine isomorphism

The `2`-adic logarithm is an isomorphism

\[
\log:(1+8\mathbf Z_2,\cdot)
\longrightarrow(8\mathbf Z_2,+).
\]

Moreover

\[
\log 9=\log(1+8)=8\cdot u
\]

for a `2`-adic unit `u`, because the first logarithm term has valuation `3` and every later term has strictly larger valuation. Hence multiplication by `log 9` identifies `Z_2` with `8Z_2`, proving `(4)--(5)`.

### Legality gives the logarithm domain

Immediately before the `B` edge ending the current run, the divisible-seven core is `7*9^r*v`. The branch condition is

\[
7\,9^r v\equiv1\pmod {16}.
\]

Since `7^(-1)=7 mod16` and `9^2=1 mod16`, this gives

\[
v\equiv
\begin{cases}
7\pmod {16},&r\text{ even},\\
15\pmod {16},&r\text{ odd}.
\end{cases}
\]

Therefore `-v` is congruent to `9` or `1 modulo 16`, proving the first part of `(3)`. The same argument at the next run proves it for `v^+`.

### Valuation identity

By `(6)`, `v=-9^alpha`. Therefore `(2)` becomes

\[
2^{4+3s}v^+
=1-9^{\alpha+r+1}
=1-9^w.
\tag{13}
\]

For every nonzero `w in Z_2`,

\[
\boxed{\nu_2(9^w-1)=3+\nu_2(w).}
\tag{14}
\]

For nonzero ordinary integers this is the standard lifting-the-exponent identity. For general `w in Z_2`, write `w=2^a u` with `u` a `2`-adic unit, approximate `u` by odd positive integers, and pass to the limit; equivalently apply the logarithm isomorphism, since `nu_2(log(9^w))=nu_2(w)+3` and `log` preserves valuation on `1+8Z_2`.

Taking valuations in `(13)` and using `(14)` gives

\[
4+3s=3+\nu_2(w),
\]

which is `(7)`. Formula `(8)` follows because `s>=5` is equivalent to `nu_2(w)>=16`.

Finally, multiply `(13)` by `-1` and divide by the exact power from `(7)`:

\[
-v^+
=
\frac{9^w-1}{2^{4+3s}}
=
\frac{9^w-1}{2^{3+\nu_2(w)}}
=
\mathcal U(w).
\]

This proves `(11)`. By `(3)`, the right side lies in `1+8Z_2` on every legal transition, so applying `log_9` proves `(12)`. ∎

## Strategic consequence

The all-highway construction can now be attacked in a fixed `2`-adic coordinate. Instead of searching directly for huge ordinary cores satisfying changing congruences, search for an ordinary core whose logarithmic orbit repeatedly enters the balls

\[
\alpha_j\equiv-r_j-1\pmod {2^{16}}
\]

and whose normalized-unit update `(12)` preserves an inductive class.

Two concrete avenues are now separated:

1. **constructive Hensel route:** find a finite ordinary family for which `(12)` maps one prescribed ball into another and for which the inverse logarithm remains a negative ordinary unit `-v`;
2. **negative complexity route:** prove that every eventually periodic, automatic, or low-state itinerary of the renormalization selects a nonordinary `2`-adic core.

The first route is the counterexample offense; the second prevents the search from repeating already excluded completion ghosts.

## Gap audit

- `alpha` is generally a genuine `2`-adic integer, not an ordinary exponent.
- A periodic or invariant `alpha` orbit does not imply that `v=-9^alpha` is an ordinary positive integer.
- Formula `(8)` is stated along legal trajectories; divisibility alone does not replace the next physical branch condition.
- The lemma supplies no forever-defined seed.
- The coordinate change does not evade the ordinary-marker boundary; it exposes the exact Hensel quantity that must be controlled.

## Suggested next attack

Compute the first several exact sections of `(12)` on the two legal residue classes of `v modulo 16`, and search for a finite union of logarithmic balls that:

- is mapped into itself by the normalized-unit update;
- forces the nine-run resource condition of `T-8003` rather than the stronger all-run-five condition;
- contains the logarithm of at least one explicit negative ordinary unit `-v`;
- and carries a proof that ordinary finite support is preserved rather than only `2`-adic compatibility.
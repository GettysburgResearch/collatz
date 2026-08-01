# L-6810 — A first-crossing near-return cannot shadow its own parity tail

**Claim ID:** `L-6810`  
**Status:** **PROPOSED**  
**Agent:** `gpt56-positive-entropy-01` (`GPT-5.6 Pro`)  
**Issue:** #75  
**Date:** 2026-07-31  
**Last updated:** 2026-07-31  
**Dependencies:** `L-6801`, `L-6807`, `L-6812`  
**Scope:** canonical non-descending first crossings  
**Counterexample status:** none

## 1. Statement

Let `w` be a coefficient-first-crossing word of length `j` and weight `q`
whose canonical source does not descend. Write

\[
T^j(r)=r+\Delta,
\qquad
0\le\Delta<q/3
\tag{1}
\]

as in `L-6812`.

Let `ell` be the common-prefix length of the parity sequence beginning at `r`
and the parity sequence beginning at the near-return state `r+Delta`:

\[
\ell
=
\max\left\{
L\ge0:
T^t(r)\equiv T^t(r+\Delta)\pmod2
\text{ for }0\le t<L
\right\}.
\tag{2}
\]

Then

\[
\boxed{2^\ell\mid\Delta.}
\tag{3}
\]

Consequently:

```text
Delta=0:
  the two states coincide and the word is an exact positive cycle return;

Delta>0:
  ell <= v_2(Delta) <= floor(log_2 Delta) < log_2(q/3) < log_2(j/3).
```

Thus every acyclic delayed-crossing obstruction changes parity branch from
its own initial itinerary within logarithmic depth after the near-return.

## 2. Proof

By definition of `ell`, the two ordinary starting states

\[
r,
\qquad
r+\Delta
\]

realize the same length-`ell` parity factor. Apply `L-6801` to these two
occurrences. Their difference is exactly `Delta`, so

\[
2^\ell\mid(r+\Delta-r)=\Delta,
\]

which proves `(3)`.

If `Delta>0`, divisibility implies

\[
\ell\le v_2(\Delta)\le\lfloor\log_2\Delta\rfloor.
\]

The displacement bound in `L-6812` gives `Delta<q/3`, completing the claim.
If `Delta=0`, equation `(1)` is an exact return.

## 3. Endpoint separation after the common factor

Let the shared length-`ell` factor have weight `s`. Subtracting its two
affine formulas gives the stronger exact relation

\[
\boxed{
T^\ell(r+\Delta)-T^\ell(r)
=
3^s\frac{\Delta}{2^\ell}.}
\tag{4}
\]

At the maximal common-prefix length, the integer `Delta/2^ell` is odd.
Hence the two endpoint states separate by one odd multiple of `3^s`, and the
next parity bits differ.

This is a simultaneous dyadic/triadic separation statement attached to the
same physical near-return.

## 4. Structural consequence

Combine `L-6810` with `T-6809`:

```text
relative to the mechanical extremizer:
  first departure occurs within (42.9+o(1)) log_2 j bits;

relative to its own shifted tail after the near-return:
  first departure occurs within log_2(q/3) bits.
```

A surviving acyclic first-crossing obstruction must therefore create two
independent early branch changes:

1. one at the beginning of the original word, away from the maximum-remainder
   mechanical path;
2. one immediately after the near-return, away from its own initial path.

It cannot close by a long symbolic echo of either path.

## 5. Gap audit

- Early symbolic divergence does not itself force physical descent.
- The case `Delta=0` is exactly the positive-cycle alternative.
- The theorem does not bound later returns or prove mixing.
- It does not solve the full-denominator congruence.
- No CST or Collatz proof is claimed.

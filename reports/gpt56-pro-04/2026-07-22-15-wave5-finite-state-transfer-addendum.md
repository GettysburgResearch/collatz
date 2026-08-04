# Agent report addendum — finite-state source encoding transfer

**Agent:** `gpt56-pro-04`  
**Issue:** #15  
**Branch:** `agent/gpt56-pro-04/15-adelic-cusp-fourier`  
**Date:** 2026-07-22  
**Parent report:** `2026-07-22-15-wave5-recurrence-source-bridge.md`

## Purpose

`L-9315` handles source equality words that are non-erasing morphic images of Thue--Morse. A literature source may instead describe its sign language through a genuinely stateful sequential transducer.

`L-9316` supplies that missing transfer.

## The synchronization theorem

Let a deterministic sequential transducer have:

- `Q` states;
- nonempty transition outputs;
- output lengths between `a` and `b` per input symbol.

At Thue--Morse scale `L=2^m`, among input block starts

\[
0,L,2L,\ldots,(2Q+1)L
\]

there are exactly `Q+1` occurrences of the same block `mu^m(1)`. Two of those occurrences enter the same transducer state.

Because the machine is deterministic, those identical input blocks emit identical output factors. Their output length `ell_m` and second output start `T_m` obey

\[
\ell_m\ge aL,
\qquad
T_m\le c_0+b(2Q+1)L,
\]

where `c_0` is a fixed initial-output length.

Thus the ordinary recurrence cone excludes the output whenever

\[
\boxed{
a>\log_{64}(81/64)b(2Q+1).}
\]

Equivalently,

\[
\boxed{
\frac ba
<
\frac1{(2Q+1)\log_{64}(81/64)}.
}
\]

## Letter-to-letter consequence

For `a=b=1`, the inequality holds for every

\[
\boxed{Q\le8.}
\]

Therefore no output of an at-most-eight-state deterministic letter-to-letter transducer on any shifted or complemented Thue--Morse input can have an eventual-zero nearest-integer cylinder tail.

This covers stateful sign conventions that are not morphisms.

## Source-acquisition workflow

When the full Dubickas equality language is obtained, test presentations in increasing generality:

```text
coding
  -> apply T-9316 directly;

non-erasing morphism
  -> apply L-9315 and its 8.8274 distortion threshold;

sequential transducer
  -> count Q, bound a,b, apply L-9316;

more general finite relation
  -> a new synchronization theorem is required.
```

This prevents unnecessary source-specific proofs when the equality language already lies in a standard finite-state image class.

## Status boundary

- `L-9316` is `PROPOSED` pending independent reconstruction.
- The theorem is a sufficient state/distortion criterion, not an all-transducer result.
- No exact Dubickas transducer is asserted before full-source acquisition.
- No ordinary survivor, Collatz counterexample, cycle, or resolution is claimed.

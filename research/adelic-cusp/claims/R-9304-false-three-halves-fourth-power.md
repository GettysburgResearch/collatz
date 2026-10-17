# R-9304 — Refutation of the four-phase `3/2` schedule

**Claim ID:** R-9304  
**Title:** `81/64` is not the fourth power of `3/2`; the former four-phase schedule is invalid  
**Status:** REFUTED / CORRECTED BY `L-9312`  
**Authoring agent:** `gpt56-pro-04`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Scope:** the former version of `L-9312` and the phase portion of `X-9304`

## Refuted assertion

The former claim used

\[
\frac{81}{64}=\left(\frac32\right)^4.
\]

This is false because

\[
\left(\frac32\right)^4=\frac{81}{16},
\]

whereas

\[
\boxed{
\frac{81}{64}=\left(\frac98\right)^2.
}
\]

Consequently, the displayed four-phase neighborhoods for

\[
\xi(3/2)^m
\]

were not consequences of the centered `81/64` orbit.

## Exact scope of the correction

The following artifacts are invalid in their former form and must not be used:

1. the former Sections 2--7 of `L-9312`;
2. the former `four-phase 3/2 schedule` assertion in `X-9304`;
3. any prose claiming that the full `3/2` orbit is sampled between successive
   `81/64` powers.

The corrected `L-9312` proves instead an exact square-root lift to `9/8` and a
paired `8 -> 9` binary chart.

## Claims not affected

The refuted identity is not used in the proofs of:

- `T-9315`, the centered rational-power equivalence;
- `L-9313`, the full real error shift and arithmetic-cylinder criterion;
- `L-9314`, the appended nearest-integer block formula;
- `T-9316`, the recurrence cone and Thue--Morse nonstabilization;
- `L-9315` and `L-9316`, the morphic and sequential transfer lemmas;
- `T-9317`, the conditional source threshold/equality bridge;
- `T-9318`, the factor-complexity barrier;
- the Fourier chain through `T-9312`;
- the fixed-room/minimum chain `T-9313`--`T-9314`.

Those claims use the ratio `81/64` directly and have separate dependency
chains.

## Correct replacement

Set

\[
\zeta=8\xi.
\]

Then

\[
\zeta(9/8)^{2n}=8\xi(81/64)^n,
\qquad
\zeta(9/8)^{2n+1}=9\xi(81/64)^n.
\]

The exact ordinary lift is the `8 -> 9` chart

\[
8X_{m+1}=9X_m-f_m
\]

with duplicated digits

\[
f_{2n}=f_{2n+1}.
\]

This replacement is proved in the corrected `L-9312`.

## Process lesson

Algebraic factorizations used to introduce intermediate dynamical phases must
be checked as exact integer identities before any symbolic, computational, or
literature bridge is built on them. Finite replay of a formula derived from a
false identity can still pass if it checks an unrelated enlarged interval; such
a replay is not validation of the claimed factorization.

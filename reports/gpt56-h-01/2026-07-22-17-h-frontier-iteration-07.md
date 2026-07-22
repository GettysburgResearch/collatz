# Session report — H frontier iteration 07

**Agent:** `gpt56-h-01`  
**Issue:** `#17`  
**Branch:** `agent/gpt56-h-01/17-h-exact-frontier`  
**Date:** 2026-07-22  
**Status:** active research; no proof or counterexample to H

## Objective

Attempt to close the final subcritical ordinary-ghost regime after iterations
04--06 had:

- reduced ordinary survival to stabilization of exact cylinders;
- eliminated the positive exponential mode, subject to a Yu-theorem audit;
- produced a centered two-place renewal equation;
- found an integral renewal height;
- and shown that every large valuation forces a later unbounded rounded deficit
  and odd-core reset.

The immediate question was whether those reset events can be converted into a
finite trap or a quantitative prime-support contradiction.

## Repository work inspected

The iteration used the exact interfaces in:

- PR #19 iterations 03--06;
- PR #13 literature waves 5--6, especially the two-place logarithmic-form and
  proper-subsum checklist;
- PR #34's proposed H renewal/core claims as a cross-check only.

Every statement admitted to the H packet was rederived in its notation.  No
cross-branch theorem was silently promoted.

## New proposed results

### `L-9519` — exact rounded-deficit pressure

For

\[
s_n=\lceil cr_n\rceil-r_{n+1}=d_n-o_n,
\qquad c=\log9/\log8,
\]

and `h_n=log_8 u_n`, the exact identity is

\[
h_{n+1}-h_n=s_n-\theta_n-\delta_n,
\]

where `theta_n in [0,1)` and the positive toll has the uniform bound

\[
\log_8(5/4)\le\delta_n<\log_8(4/3).
\]

Consequences:

- rounded-critical runs contract `u` by at least the factor `4/5` per step;
- cumulative positive deficit has a universal linear lower bound;
- a deficit `d` expands the core by more than `(3/4)8^(d-1)`;
- on the post-Yu subcritical ray, every large `r_n` forces a later deficit at
  least `(c-1)r_n` and an exponentially large core reset.

### `L-9520` — successive-renewal compatibility

At an interior renewal,

\[
3^aX+1=8^RU,
\qquad
4^bY+1=9^RU,
\]

and hence

\[
8^R4^bY-9^R3^aX=9^R-8^R.
\]

This yields:

\[
\gcd(U,XY)=1,
\qquad
\gcd(X,Y)\mid9^R-8^R,
\]

and every shared prime power pays a multiplicative-order condition dividing
`R`.

Writing `F=Y/gcd(X,Y)` gives the exact local alternative

\[
U<4^bF:
\]

either

\[
b\ge\tfrac14\log_2U
\]

or

\[
F>\sqrt U.
\]

Thus a large central core must be paid for by a long zero room or a large
primitive forward bridge factor.

### `T-9513` — fixed bridge-prime support is finite

The central equation normalizes to

\[
-4^bY+3^a(9/8)^RX+(9/8)^R=1.
\]

For a fixed finite support set, the three terms lie in one finite-rank
multiplicative group.  Every proper vanishing subsum is excluded by sign or by
opposite `2`-adic valuations.  The standard nondegenerate S-unit theorem gives
only finitely many triples, and each triple recovers the full central state.
An infinite nonperiodic chain therefore cannot remain in one finite bridge
prime alphabet.

Globally new prime powers in `W_k` divide the primitive forward factors `F_k`,
so both

\[
\sum_k\log P_k^{new}
\]

and

\[
\sum_k\log F_k
\]

diverge.

### `T-9514` — final structural dichotomy

Subject to the audited Yu specialization, any nonperiodic survivor is
subcritical and lies in one of two branches:

1. **bounded letters:** a nonperiodic finite-alphabet ghost code with infinitely
   many fresh bridge primes;
2. **unbounded letters:** unbounded deficits, exponential core resets, and at
   every large renewal either a long zero room or a large primitive factor.

This is a complete structural split, not a contradiction.

### `R-9504` and `Q-9508`

`R-9504` records the scale-compatibility obstruction: unweighted fresh-prime
mass and real pressure alone can coexist with the discounted core budget.

`Q-9508` isolates the two exact closure targets:

- prove a discounted fresh-mass lower bound on the unbounded branch;
- prove finite-alphabet nonstabilization on the bounded branch.

The stronger direct alternative remains `nu_K -> infinity`.

## Why the result is not yet complete

The new prime theorem is qualitative.  It proves infinitely many globally new
bridge factors, but not that they appear early enough to violate

\[
\sum_n c^{-n}\log u_n<\infty.
\]

An increasingly delayed sequence of fresh primes is still scale-compatible.
Likewise, bounded letters do not imply finite prime support or eventual
periodicity.

Calling either observation a contradiction would repeat the exact
cross-completion/height mistake documented elsewhere in the repository.

## Exact remaining theorem

A complete proof may now take any of the following forms:

1. prove the monotone ordinary-section minimum `nu_K` diverges;
2. prove every nonperiodic finite-alphabet ghost has infinitely many nonzero
   extension carries;
3. prove globally fresh bridge mass has a discounted lower bound incompatible
   with the exact core budget;
4. construct an integral renewal potential that contracts into a finite legal
   trap.

## Files

- `research/h-frontier/claims/ITERATION_07.md`
- `research/h-frontier/CLAIM_INVENTORY.md`
- this report

## Integrity boundary

No finite computation, density estimate, dimension bound, or qualitative
S-unit finiteness statement is treated as exclusion of one ordinary positive
integer.  No H survivor or Collatz counterexample is constructed.

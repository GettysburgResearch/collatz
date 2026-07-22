# Q-9702 — Exclude or construct an infinite cap-correction chain

**Claim ID:** `Q-9702`  
**Title:** Decide the zero-quotient tail of PR #3's corrected 256-stage system  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9703`; PR #3 `T-0025`, `T-0027`, `T-0030` interfaces  
**Scope:** arbitrary infinite directives of corrected 256-transition stage words  
**Related counterexample candidates:** none

## Exact open interface

For an admissible stage word `w_m`, let

\[
R_m(w_m)
\]

be the canonical complete-stage correction and let

\[
S_m(w_m)
\]

be its canonical cap. `T-9703` proves that every ordinary nonnegative infinite
stage trajectory must eventually satisfy

\[
\boxed{
S_m(w_m)=R_{m+1}(w_{m+1})}
\tag{1}
\]

at every scale. Conversely, equality (1) makes

\[
z_m=R_m(w_m)
\]

an exact nonnegative residual tail.

The full stage ordinary-integer question is therefore reduced to one of the
following mutually exclusive outcomes.

### Negative target

Prove, uniformly over every admissible infinite stage directive, that

\[
S_m(w_m)\ne R_{m+1}(w_{m+1})
\]

for infinitely many `m`. By `T-9703`, no ordinary infinite stage trajectory
then exists, and the cumulative initial residue blocks are nonzero infinitely
often.

### Positive target

Construct stage words by one finite symbolic rule such that (1) holds forever
from some explicit scale. Supply:

1. one exact finite positive ordinary initialization;
2. direct replay of every local tower and connector block;
3. positivity of every physical state;
4. proof that the finite rule is defined forever;
5. justified growth or permanent avoidance of the terminal cycle;
6. an independent exact replay verifier.

Only then would a `K-####` candidate be appropriate.

## Tiny-target form

Every hypothetical equality in the eventual tail satisfies

\[
0\le R_{m+1}=S_m<3^{A_m},
\]

while the next correction is normally chosen modulo `2^(D_(m+1))`. Quantitatively,

\[
\log_2\frac{R_{m+1}}{2^{D_{m+1}}}
<
-\frac{22173699}{5248}2^m+\frac{1024}{41}.
\tag{2}
\]

Thus a positive result must hit an exponentially tiny initial interval of the
next complete cylinder at every late scale. A negative result need not control
the full quotient anymore; it only has to exclude this cap-sized target.

## Relevant repository work

### PR #3 ordinary bulk

`T-0030` gives the finite forward sequence

\[
V_{m+1}=V_m+2^{m+1}V_m^2.
\]

This removes a preloaded-logarithm objection but does not identify `V_m` with a
stage correction or cap. A useful next calculation is to express

\[
R_m,\ S_m,\ C_m
\]

relative to `V_m` and test whether equality (1) forces an impossible bounded
coefficient, or instead reveals a self-feeding affine ansatz.

### PR #32 / PR #16 completion height

PR #32 independently reconstructed the carry-height chain through `ADEL/T-9312`.
Its method suggests looking for a nonzero ordinary numerator created by a long
run of equalities (1), whose dyadic divisibility grows at the next-stage rate
while its global height is bounded by the cap estimate (2).

### PR #20 periodic tails

`T-9414` and `T-9415` exclude eventually periodic positive increment tails of
period at most three in a different active-stack system. They do not directly
apply to (1). They indicate that a first exact subtarget should be an eventual
periodicity theorem for normalized cap-correction data, followed by a native
height calculation rather than a mere analogy.

### Issue #29 unpublished synthesis note

The issue comment reports a related `Theta(K^2)` completion-height pressure for
an eventually-zero active-cylinder tail. Its files are not published and are
not a dependency. The useful independently reconstructible principle is:
eventual zero blocks must be converted into a displayed nonzero numerator and a
height bound, not inferred from compatible 2-adic series alone.

## First falsifiable attacks

1. **One- and two-stage elimination.** Compute exact `R_m,S_m` for structured
   stage words and look for a type-independent residue or sign obstruction to
   (1). Any sampled failure is evidence only; a discovered identity must be
   proved symbolically.
2. **Normalized offset recurrence.** Use the scale-squaring laws for `A_m,D_m`
   and seek a finite recurrence for `C_m(w_m)` modulo the cap scale `3^(A_(m-1))`.
3. **Bulk-affine ansatz.** Substitute `z_m=alpha_m V_m+beta_m` into the
   zero-quotient equations and solve the exact coefficient conditions.
4. **Completion-height numerator.** Compose `L` equations (1), clear every
   binary denominator, and compare the resulting nonzero numerator with the
   tiny-target height (2).
5. **Finite-control collapse test.** Freeze an eventually periodic normalized
   stage-word rule and determine whether scale squaring turns (1) into a fixed
   exponential-polynomial equation amenable to the PR #3 `T-0021` obstruction.

## Failure conditions

- treating `R_(m+1)<3^(A_m)` as proof that equality is impossible;
- extrapolating from finitely many stage words;
- replacing equality (1) by agreement modulo a shorter prefix;
- preloading an infinite logarithm or cap sequence;
- constructing a residual tail without one finite marked ordinary start;
- claiming growth from bit-length surplus without exact membership and replay.

## Current status

Open. `T-9703` removes the unbounded free quotient from every hypothetical
ordinary tail, but neither excludes nor constructs the cap-correction chain.

# Q-9702 — Exclude or construct an infinite cap-correction chain

**Claim ID:** `Q-9702`  
**Title:** Decide the zero-quotient tail of PR #3's corrected 256-stage system  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-cylinder-01`  
**Created:** 2026-07-22  
**Last updated:** 2026-07-22  
**Dependencies:** `T-9703`, `T-9704`; PR #3 `T-0025`, `T-0027`, `T-0030` interfaces  
**Scope:** arbitrary infinite directives of corrected 256-transition stage words  
**Related counterexample candidates:** none

## Exact open interface

For an admissible stage word `w_m`, let `R_m(w_m)` be the canonical complete
stage correction and `S_m(w_m)` its canonical cap. `T-9703` proves that every
ordinary nonnegative infinite stage trajectory must eventually satisfy

\[
\boxed{S_m(w_m)=R_{m+1}(w_{m+1})}
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

## Height-collapse form

`T-9704` proves that every hypothetical equality tail satisfies

\[
\log_2(R_m+257)
<
\log_2(R_M+257)
+rac{161341}{10496}(2^m-2^M)
+rac{1024}{41}(m-M).
\tag{2}
\]

Against the complete cylinder precision

\[
D_m=\frac{1085579}{256}2^m+2816,
\]

this gives

\[
\boxed{
\limsup_{m\to\infty}
\frac{\log_2(R_m+257)}{D_m}
\le
\frac{161341}{44508739}
<\frac1{275}.}
\tag{3}
\]

Thus a surviving ordinary correction uses asymptotically less than `0.363%` of
its dyadic cylinder. Equivalently,

\[
\log_2\frac{R_m+257}{2^{D_m}}
<
-\frac{22173699}{5248}2^m+O_M(m).
\tag{4}
\]

This is much stronger than the first cap-only bound

\[
0\le R_{m+1}=S_m<3^{A_m}.
\]

A negative result now has a completion-height factor greater than 275 available,
provided it identifies a structured nonzero numerator, p-adic logarithmic form,
or algebraic approximant. The short representative alone is not a contradiction.

## Relevant repository work

### PR #3 ordinary bulk

`T-0030` gives the finite forward sequence

\[
V_{m+1}=V_m+2^{m+1}V_m^2.
\]

This removes a preloaded-logarithm objection but does not identify `V_m` with a
stage correction or cap. A useful calculation is to express

\[
R_m,\ S_m,\ C_m
\]

relative to `V_m` and test whether equality (1) forces an impossible bounded
coefficient, or reveals a self-feeding affine ansatz.

### PR #32 / PR #16 completion height

PR #32 independently reconstructed the carry-height chain through `ADEL/T-9312`.
Its method suggests looking for a nonzero ordinary numerator created by a long
run of equalities (1). Bound (3) leaves far more precision than ordinary height,
so even a moderately inefficient native product-formula reduction could close
the negative side.

### PR #20 periodic tails

`T-9414` and `T-9415` exclude eventually periodic positive increment tails of
period at most three in a different active-stack system. They do not directly
apply to (1). They indicate that an exact subtarget should be a native fixed
stage-word or eventually periodic cap-chain theorem, followed by a height
calculation rather than analogy.

### PR #13 logarithmic interface

`LIT-KTHM-0030` identifies the moving connector bulk as a divided p-adic
exponential converging to `-(7/4)log_2(3)`. A promising negative route is to
express each fixed normalized stage word's correction equation as a finite
p-adic exponential/logarithmic form and combine a source-appropriate lower bound
with the factor-275 height gap in (3).

### Issue #29 unpublished synthesis note

The issue comment reports related completion-height pressure for an
eventually-zero active-cylinder tail. Its files are not published and are not a
dependency. The independently reconstructed principle is the same one enforced
here: eventual zero blocks must produce a displayed nonzero numerator and a
global height bound, not merely a compatible 2-adic series.

## First falsifiable attacks

1. **Fixed stage-word logarithmic form.** For one normalized stage word `W`,
   derive `R_m(W)` from the finite Newton/logarithm compiler and exhibit the
   exact nonzero p-adic expression whose valuation is `D_m` while its height is
   bounded by (2). Then make the constants uniform over the finite stage-word
   alphabet.
2. **One- and two-stage elimination.** Compute exact `R_m,S_m` for structured
   words only as a conjecture generator; prove any discovered sign, residue, or
   common-factor obstruction symbolically.
3. **Normalized offset recurrence.** Use scale squaring to seek a finite
   recurrence for `C_m(W)` modulo the cap-chain height scale, not the full
   `2^(D_m)` workspace.
4. **Bulk-affine ansatz.** Substitute `z_m=alpha_mV_m+beta_m` into (1) and solve
   the exact finite coefficient equations. A positive hit must still be tied to
   one marked finite initialization.
5. **Eventual finite-control tail.** Freeze an eventually periodic normalized
   stage-word rule and test whether scale squaring gives a nondegenerate
   exponential-polynomial or p-adic analytic equation with only finitely many
   solutions.
6. **Long-run numerator.** Compose `L` equalities (1), clear all binary radices,
   and compare the resulting numerator against the global bound (3), checking
   nonvanishing before invoking any product formula.

## Failure conditions

- treating a short representative as proof that equality is impossible;
- extrapolating from finitely many stage words;
- replacing equality (1) by agreement modulo a shorter prefix;
- preloading an infinite logarithm or cap sequence;
- invoking a p-adic theorem without matching its exact height and algebraicity
  hypotheses;
- constructing a residual tail without one finite marked ordinary start;
- claiming growth from bit-length surplus without exact membership and replay.

## Current status

Open. `T-9703` removes the unbounded free quotient and `T-9704` gives a
factor-greater-than-275 completion-height gap. Neither theorem excludes nor
constructs the cap-correction chain.

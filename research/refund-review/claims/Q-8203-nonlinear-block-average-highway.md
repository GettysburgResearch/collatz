# Q-8203 — Nonlinear block-average ordinary highway

**Claim ID:** `Q-8203`  
**Title:** Construct one ordinary run-core path with nonlinear schedule and exact nine-run resource  
**Status:** `IDEA / PRIMARY POSITIVE TARGET`  
**Authoring agent:** `gpt56-refund-01`  
**Created:** 2026-07-23  
**Dependencies:** frozen PR #51 `L-8002`, `L-8004`, `L-8005`, `T-8003`; `R-8202`  
**Scope:** the divisible-seven `+1` negative-three-cycle chart  
**Related counterexample candidates:** none

## Exact target

Construct one positive odd ordinary core `v_0` whose deterministic maximal-run orbit

\[
2^{4+3r_{n+1}}v_{n+1}=9^{r_n+1}v_n+1
\]

is defined forever and, from some index `J`, obeys

\[
\boxed{
\sum_{h=0}^{8}r_{J+9m+h}\ge44
\qquad(m\ge0).}
\tag{1}
\]

By PR #51 `T-8003`, `(1)` makes the physical section states strictly grow every nine macros and gives an unconditional divergent Collatz orbit.

## Required nonlinearity

`R-8202` proves that every eventually affine schedule

\[
r_n=R+dn,\qquad d\ge1,
\]

selects an irrational core. Eventually periodic schedules are separately completion ghosts. Therefore a successful schedule must be genuinely non-eventually-affine.

This is not merely a presentation requirement: affine quadratic exponent sums collapse to one scalar Tschakaloff value and are excluded by a primary-source value theorem.

## Exact logarithmic coordinate

PR #51 `L-8005` gives the legal run coordinate

\[
\alpha_n=\log_9(-v_n)\in\mathbf Z_2
\]

and

\[
\nu_2(\alpha_n+r_n+1)=1+3r_{n+1}.
\]

The next coordinate is the exact normalized-unit map

\[
\alpha_{n+1}
=
\log_9\left(
{9^{\alpha_n+r_n+1}-1
 \over2^{3+\nu_2(\alpha_n+r_n+1)}}
\right).
\]

A positive construction should therefore use a nonlinear arithmetic invariant in this coordinate rather than prescribe a low-complexity run word externally.

## Finite proof state

A viable certificate may retain:

```text
current ordinary core v,
current run r,
logarithmic residue alpha mod 2^h,
position 0,...,8 in the resource window,
resource total capped at 44,
changing-modulus top quotient,
canonical most-significant closure.
```

The logarithmic coordinate is proof instrumentation; the actual witness must remain the written ordinary integer `v` and its physical Collatz replay.

## Positive acceptance gate

A complete answer must provide:

1. one explicit positive odd `v_0`;
2. exact all-time run-core integrality;
3. the next-`B` legality gate at every macro;
4. the window invariant `(1)`;
5. direct physical shortcut-Collatz replay;
6. an independent verifier.

No symbolic directive, `2`-adic fixed point, modular lasso, or unbounded finite prefix qualifies.

## Suggested attack

Search for a finite union of logarithmic Hensel balls whose normalized-unit images:

- return to the union;
- carry a nine-phase resource counter reaching 44;
- contain the logarithm of at least one negative ordinary unit `-v`;
- and prove ordinary finite support/top closure, not merely `2`-adic invariance.

A negative result should isolate the first exact obstruction: source irrationality, forced eventual affinity, a missing top carry, or failure of the 44-resource window.

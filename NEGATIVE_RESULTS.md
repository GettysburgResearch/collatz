# Negative and cautionary results

Last updated: 2026-07-21

## N-0001 — A periodic parity string may define only a 2-adic rational

The periodic shortcut parity word

\[
(100)^\omega
\]

formally reconstructs the 2-adic rational \(1/5\), which lies on the cycle

\[
\frac15\to\frac45\to\frac25\to\frac15.
\]

This is a genuine cycle of the 2-adic extension, not a positive-integer Collatz counterexample.

**Consequence:** an infinite rewrite loop is insufficient until its starting word is proved finite and canonical.

## N-0002 — Arbitrarily long finite admissibility is not infinite closure

`L-0002` and `L-0004` give parameterized finite-horizon stacks. Taking larger parameters does not select one fixed finite integer with infinitely many steps.

**Consequence:** local stack amplification is universal and cannot be treated as near-resolution by itself.

## N-0003 — Local expansion can be lost during boundary repair

Pre-repository exploratory work found locally expanding rewrite gadgets whose exact repair phases became subcritical.

**Consequence:** every proposed grammar must account for the multiplier of the full regeneration cycle.

## N-0004 — A nontrivial induced orbit cannot have eventually periodic digits

`T-0003` rules out eventually periodic least-digit itineraries for any nontrivial ordinary-integer induced orbit.

**Consequence:** fixed-period travelling stacks and purely periodic carry tilings cannot solve finite closure.

## N-0005 — The high-order boundary grows at the ratio N/M, not N

For an infinite induced orbit,

\[
A_t=C(N/M)^t+O(1).
\]

Hence base-\(M\) word length grows with slope

\[
\log_M(N/M).
\]

**Consequence:** grammars must track a slowly moving, aperiodic boundary.

## N-0006 — Consecutive width understates the available alphabet

Sparse fibers and inverse-signature codes are much richer than consecutive collision runs.

**Consequence:** searches and theorems should operate on full fibers or codes, not intervals alone.

## N-0007 — Unbounded alphabet cardinality is not finite closure

`T-0005` proves exponentially unbounded mildly supercritical fiber cardinality without producing an infinite orbit.

**Consequence:** record size is no longer a meaningful proxy for distance to a counterexample.

## N-0008 — A common odd tail changes drift, not the branching core

The finite CRT odd tail can make an inverse code supercritical while preserving branch count and inverse-root offsets exactly.

**Consequence:** the tail is a drift resource, not a free vertical-boundary repair parameter.

## N-0009 — Preserving fixed geometry is not growing geometry

`T-0006` embeds any finite collision alphabet into arbitrarily large supercritical fibers while preserving:

- every already witnessed modular projection;
- every consecutive subblock;
- the entire original difference set;
- any finite collection of local arithmetic patterns.

This is a strict strengthening of cardinality growth, but the preserved useful scale remains fixed while a hypothetical orbit's finite boundary grows without bound.

**Consequence:** neither arbitrary precision nor preservation of a fixed finite relay library is sufficient by itself. The next theorem must make closure-relevant geometry grow with construction depth, reinterpret sparse tensor offsets as a finite moving-boundary address system, or establish a vertical relay that is genuinely scale independent.
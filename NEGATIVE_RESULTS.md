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

This is a genuine cycle of the 2-adic extension, not a positive-integer Collatz counterexample. The left-infinite binary expansion is not eventually zero.

Consequence: an infinite rewrite loop is insufficient until its starting word is proved finite and canonical.

## N-0002 — Arbitrarily long finite admissibility is not infinite closure

`L-0002` proves a family with \(9m+1\) forced induced-map steps for every finite \(m\). Taking larger \(m\) does not select one fixed finite integer with infinitely many steps.

Consequence: a successful proof needs a finite regeneration induction, not an unbounded sequence of unrelated finite prefixes.

## N-0003 — Local expansion can be lost during boundary repair

Pre-repository exploratory work found locally expanding rewrite gadgets associated with negative rational cycles whose exact repair phases became subcritical. Those derivations have not yet been imported as formal claims and should not be relied upon.

Consequence: every proposed grammar must account for the multiplier of the full regeneration cycle, including all carry and boundary-repair phases.

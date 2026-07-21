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

This is a genuine cycle of the 2-adic extension, not a positive-integer Collatz
counterexample. The left-infinite binary expansion is not eventually zero.

**Consequence:** an infinite rewrite loop is insufficient until its starting
word is proved finite and canonical.

## N-0002 — Arbitrarily long finite admissibility is not infinite closure

`L-0002` proves a family with \(9m+1\) forced induced-map steps for every finite
\(m\). `L-0004` now shows that analogous finite-horizon stacks exist for every
nontrivial collision fiber.

Taking larger \(m\) does not select one fixed finite integer with infinitely
many steps.

**Consequence:** local stack amplification is universal and therefore cannot be
treated as near-resolution by itself. A successful proof needs finite vertical
regeneration.

## N-0003 — Local expansion can be lost during boundary repair

Pre-repository exploratory work found locally expanding rewrite gadgets
associated with negative rational cycles whose exact repair phases became
subcritical. Those derivations have not yet been imported as formal claims and
should not be relied upon.

**Consequence:** every proposed grammar must account for the multiplier of the
full regeneration cycle, including all carry and boundary-repair phases.

## N-0004 — A nontrivial induced orbit cannot have eventually periodic digits

`T-0003` proves that if an ordinary integer \(A_0\ge M\) followed an infinite
orbit of

\[
H_D(MB+d)=NB+d,
\]

then its admissible least-digit itinerary could not be eventually periodic. An
eventually periodic itinerary makes the exact 2-adic coding series rational;
the same rational real sum lies below \(M\), contradicting \(A_0\ge M\).

**Consequence:** fixed-period travelling stacks, periodic phase schedules, and
purely periodic carry tilings cannot by themselves give the required finite
integer. A successful finite grammar must generate genuine aperiodicity.

## N-0005 — The high-order boundary grows at the ratio N/M, not N

For an infinite induced orbit,

\[
A_t=C(N/M)^t+O(1).
\]

Hence base-\(M\) word length grows with slope

\[
\log_M(N/M),
\]

not \(\log_M N\).

**Consequence:** macro grammars should be designed around a slowly moving,
aperiodic boundary. Any heuristic that allocates roughly one new base digit per
step is using the wrong scale.

## N-0006 — Consecutive width understates the available alphabet

Searching only maximal consecutive runs misses valid sparse collision fibers.
At depth 22 the best consecutive width found previously is much smaller than
the complete fiber cardinality 18 in `O-0004`.

**Consequence:** collision searches and theorems should operate on full level
sets or inverse-signature codes, not intervals alone.

## N-0007 — Unbounded alphabet cardinality is not finite closure

`T-0005` proves that mildly supercritical collision fibers have exponentially
unbounded cardinality. The proof is entirely finite and does not construct one
infinite induced orbit.

**Consequence:** record fiber size is no longer a meaningful proxy for distance
to a counterexample. The relevant objectives are structured digit geometry,
precision surplus, vertical carry relays, run-length cofactor closure, and the
ordinary finite high-order boundary.

## N-0008 — A common odd tail changes drift, not the branching core

The CRT odd-tail construction can make an inverse collision code
supercritical without changing its number of branches. Different representatives
of the same CRT class shift inputs by a full input radix and outputs by a full
output multiplier, leaving the reduced chart unchanged.

**Consequence:** the common tail is a controlled drift resource, not a free
parameter for repairing the lifting congruence or vertical boundary.

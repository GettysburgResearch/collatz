# Negative and cautionary results

Last updated: 2026-07-21

## N-0001 — A periodic parity string may define only a 2-adic rational

The periodic shortcut parity word

\[
(100)^\omega
\]

formally reconstructs the 2-adic rational \(1/5\), not a positive-integer counterexample.

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

For an infinite stationary induced orbit,

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

**Consequence:** searches and theorems should operate on full fibers, codes, or negative return languages—not intervals alone.

## N-0007 — Unbounded alphabet cardinality is not finite closure

`T-0005` proves exponentially unbounded mildly supercritical fiber cardinality without producing an infinite orbit.

**Consequence:** record size is no longer a meaningful proxy for distance to a counterexample.

## N-0008 — A common odd tail changes drift, not the branching core

The finite CRT odd tail can make an inverse code supercritical while preserving branch count and inverse-root offsets exactly.

**Consequence:** the tail is a drift resource, not a free vertical-boundary repair parameter.

## N-0009 — Preserving fixed geometry is not growing geometry

`T-0006` embeds any finite collision alphabet into arbitrarily large supercritical fibers while preserving its existing modular projections, consecutive subblocks, difference set, and finite local patterns.

The useful scale remains fixed while a hypothetical orbit's boundary grows.

**Consequence:** arbitrary precision and preservation of a fixed relay library are insufficient by themselves.

## N-0010 — A finite complete one-target all-supercritical renewal code is impossible

`T-0009` proves the following. Let finitely many negative templates return to one target \(-v\), and suppose their dyadic cylinders cover every sufficiently large ordinary quotient. The finite union is clopen in \(\mathbb Z_2\) and contains a dense set, so it also contains the target quotient \(q=v\).

The branch covering \(q=v\) must satisfy

\[
u=2^Lv,\qquad a=0,\]

and is therefore the all-even contracting return with multiplier \(2^{-L}\).

**Consequence:** an all-expanding construction cannot be a finite complete stationary return table around one target. It must use an infinite but finitely generated renewal language, a proper survivor set, several targets, or compensated subcritical edges.

## N-0011 — Long common drift tails can destroy normalized control width

`L-0011` gives the exact aspect ratio after appending a common all-odd tail of length \(k\):

\[
\Delta_k
=
\frac{W/2^L}{2^k(\lambda_k-1)},
\]

where \(W\) is the unchanged core offset diameter and \(\lambda_k\) is the final expansion ratio.

If \(\lambda_k\ge1+arepsilon\), then

\[
\Delta_k<2^{-k}/arepsilon.
\]

**Consequence:** branching and drift are algebraically separable but not geometrically independent. Long post-merger tails can make the stationary real rounding window exponentially narrow.

## N-0012 — Rich symbolic geometry can coexist with a microscopic real window

`O-0006` records:

```text
O-0001: 2 branches,   aspect ~= 5.88e-2
O-0005: 339 branches, aspect ~= 3.26e-9
```

The complete-dyadic-projection examples fall to aspect ratio about `4.72e-264` by `b=5`.

By `T-0010`, an infinite stationary orbit must trap one fractional-part orbit \(\{C(N/M)^t\}\) in an arc of precisely this normalized width.

**Consequence:** branch count, low-order modular correction, and real control width are separate resources and may move in opposite directions.

## N-0013 — Positive local edges do not replace a graph-cycle audit

In a multi-target return grammar, some local edges may be contracting. `T-0013` shows that what matters asymptotically is the multiplier of every directed grammar cycle, together with a phase-potential certificate.

**Consequence:** neither rejecting every locally subcritical edge nor accepting a graph because its favored cycle expands is sound. The full selected graph must have positive cycle mean, or arithmetic constraints must prove that nonpositive cycles are unreachable.

# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`  
Active draft PR: `#3`

## Q-0001 — Finite-boundary regeneration

Status: `IDEA` / central open target  
Dependencies: `T-0002`, `T-0003`, `T-0004`

For at least one supercritical collision fiber, construct one ordinary finite
integer \(A_0\) in the required lifting congruence class such that every
iterate of

\[
H_D(MB+d)=NB+d,
\qquad d\in D,
\]

remains admissible.

A valid solution must prove infinite behavior from one finite starting word.
The following are insufficient by themselves:

- arbitrarily long finite trajectories;
- compatible residues modulo \(M^k\) for every fixed \(k\);
- a periodic or aperiodic point in \(\mathbb Z_2\);
- a spatially periodic carry tiling;
- a numerical trajectory checked to any finite height.

Two equivalent construction targets are now available:

1. a finite vertical macro-tile grammar with a finite high-order boundary; or
2. a finite family of run-length/cofactor schemas closed under `T-0004`.

## Q-0002 — Analytic growth of complete collision fibers

Status: `IDEA`  
Dependencies: `L-0003`, `X-0002`

Are the cardinalities of supercritical collision fibers unbounded?

`X-0002` finds maximum cardinalities

```text
2, 3, 4, 5, 8, 12, 18
```

at increasing depths through `L=22`, but this is finite evidence.

Use the exact recursion

\[
(a_L,s_L)\longmapsto(a_{L+1},s_{L+1})
\]

from `L-0003` to construct an explicit infinite coalescence family. Desired
control parameters include:

- fiber cardinality and internal digit geometry;
- odd-step density \(a/L\);
- expansion margin \(3^a/2^L\);
- lifting modulus \(3^a-2^L\);
- short carry cycles and vertical relay quality;
- compatibility with other fibers under chart transitions.

The objective is structured, reusable alphabets, not record cardinality alone.

## Q-0003 — Carry grammar for the width-three chart

Status: `IDEA`  
Dependencies: `O-0002`, `L-0004`

For

\[
H(512B+d)=729B+d,
\qquad d\in\{0,1,2\},
\]

classify short carry macro-tiles and determine whether they combine into a
finite vertically regenerative grammar.

One exact local tile is

\[
R_1L_{361}L_0\longrightarrow L_2L_2R_1.
\]

It returns the carry after only two columns and emits admissible digits, but a
direct stack of this tile fails on the next vertical normalization. The next
target is a relay of several tiles rather than repetition of one tile.

## Q-0004 — Multi-chart transition groupoid

Status: `IDEA`  
Dependencies: `T-0002`, `O-0001`--`O-0004`

Construct exact finite bridges among different collision charts. A successful
cycle may let one chart repair the finite boundary produced by another while
retaining net expansion.

A bridge must record:

- source and target affine lifting coordinates;
- source and target congruence classes;
- the exact finite Collatz word realizing the bridge;
- the transformation of every free integer parameter;
- positivity and integrality on the full stated domain;
- the net effect on the run-length skeleton and finite boundary.

## Q-0005 — Finite versus adic closure criterion

Status: `IDEA`  
Dependencies: `T-0003`

`T-0003` gives the exact coding

\[
A_0=\frac{N-M}{N}\sum_{t\ge0}d_t\left(\frac MN\right)^t
\]

inside \(\mathbb Q_2\). Develop a directly usable criterion deciding when a
finitely generated admissible itinerary represents an ordinary nonnegative
integer rather than a nonordinary `2`-adic point.

The theorem already rules out eventually periodic digit itineraries for any
nontrivial orbit. The remaining target should cover aperiodic morphic,
substitutional, or `S`-adic sequences and expose an explicit finite-boundary
condition.

## Q-0006 — Independent verification

Status: `IDEA`

Reconstruct the active contribution without relying on its author's
confidence:

- check chronological parity orientation;
- check `L-0001` and the table recursion `L-0003`;
- reproduce the complete depth-22 fiber enumeration;
- check the arbitrary-fiber conjugacy `T-0002`;
- check the direction of every carry rule in `L-0004`;
- check the two-topology argument in `T-0003`;
- check both directions of the run-length equivalence `T-0004`;
- identify the first unsupported inference, if any.

## Q-0007 — Vertical macro-tile closure

Status: `IDEA`  
Dependencies: `L-0004`, `T-0003`

The local mixed-radix rule is

\[
Nx+c=Mq+e.
\]

A closed horizontal carry path gives a pumpable tile

\[
R_cX\longrightarrow ER_c.
\]

Construct a finite collection of such tiles whose emitted rows can be parsed
as controlled input rows at later times, while the high-order boundary remains
finite and follows the aperiodic growth rate

\[
\log_M(N/M).
\]

This is a two-dimensional finite-tiling problem with one moving boundary. Pure
horizontal periodicity produces only an adic object and does not solve it.

## Q-0008 — Parameterized `S`-unit skeleton schemas

Status: `IDEA`  
Dependencies: `T-0004`

Find a finite family of positive-integer schemas closed under

\[
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1}.
\]

A successful family must:

- keep \(d_k\) in one or more collision alphabets;
- keep \(C_k\) positive and not divisible by the active input radix;
- generate an infinite, genuinely aperiodic exponent schedule;
- preserve or transition between the required lifting congruences;
- arise from one finite initial triple \((d_0,u_0,C_0)\).

Promising mechanisms include two-length continued-fraction schedules,
cofactor substitutions, and controlled chart changes. Isolated solutions of
one congruence do not count unless they close uniformly under iteration.

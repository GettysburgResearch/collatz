# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`  
Active draft PR: `#3`

## Q-0001 — Finite-boundary regeneration

Status: `IDEA` / central open target  
Dependencies: `T-0002`, `T-0003`, `T-0004`, `T-0005`

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
- a numerical trajectory checked to any finite height;
- an alphabet whose cardinality tends to infinity.

Two equivalent construction targets remain:

1. a finite vertical macro-tile grammar with a finite high-order boundary; or
2. a finite family of run-length/cofactor schemas closed under `T-0004`.

## Q-0002 — Analytic growth of collision fibers

Status: `PROPOSED RESOLUTION` by `T-0005`  
Dependencies: `L-0005`, `T-0005`

The original question asked whether supercritical collision-fiber
cardinalities are unbounded. `T-0005` proves the stronger lower bound

\[
|D_m|
\ge
\left\lceil\frac{\binom{3m}{m}}{3^m}\right\rceil
\sim
\frac{\sqrt3}{2\sqrt{\pi m}}
\left(\frac94\right)^m,
\]

while keeping the expansion factor in \((1,3/2]\).

The proof uses equal inverse-signature parity classes for branching and a CRT
all-odd tail for drift. This resolution remains `PROPOSED` until independent
review.

The former optimization part of the question has moved to `Q-0009`: build
alphabets with closure-relevant internal geometry, not merely large
cardinality.

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
direct stack of this tile fails on the next vertical normalization. The target
is a relay of several tiles rather than repetition of one tile.

## Q-0004 — Multi-chart transition groupoid

Status: `IDEA`  
Dependencies: `T-0002`, `O-0001`--`O-0005`

Construct exact finite bridges among different collision charts. `T-0005`
adds a systematic family of charts built from one branching code and different
common tails. A successful cycle may let one chart repair the finite boundary
produced by another while retaining net expansion.

A bridge must record:

- source and target affine lifting coordinates;
- source and target congruence classes;
- the exact finite Collatz word realizing the transition;
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
integer rather than a nonordinary 2-adic point.

The theorem already rules out eventually periodic digit itineraries for any
nontrivial orbit. The remaining target should cover aperiodic morphic,
substitutional, code-composed, or `S`-adic sequences and expose an explicit
finite-boundary condition.

## Q-0006 — Independent verification

Status: `IDEA`

Reconstruct the active contribution without relying on its author's
confidence:

- check chronological parity orientation;
- check `L-0001`, `L-0003`, and `L-0005`;
- reproduce `X-0001` through `X-0003`;
- check the arbitrary-fiber conjugacy `T-0002`;
- check the direction of every carry rule in `L-0004`;
- check the two-topology argument in `T-0003`;
- check both directions of the run-length equivalence `T-0004`;
- reconstruct the pigeonhole, CRT, positivity, and lifting steps in `T-0005`;
- identify the first unsupported inference, if any.

## Q-0007 — Vertical macro-tile closure

Status: `IDEA`  
Dependencies: `L-0004`, `T-0003`, `O-0005`

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

`O-0005` supplies a 339-symbol chart with full projection modulo 16 and a long
interval in its difference set. Determine whether this produces genuinely new
vertical relays rather than only more horizontal cycles.

## Q-0008 — Parameterized `S`-unit skeleton schemas

Status: `IDEA`  
Dependencies: `T-0004`, `O-0005`

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

The difference interval in `O-0005` makes bounded right-hand corrections much
less scarce. Convert that flexibility into a uniform cofactor relay rather
than isolated solutions.

## Q-0009 — Structured collision codes and closure-quality geometry

Status: `IDEA` / primary new design problem  
Dependencies: `L-0006`, `T-0005`, `O-0005`

`T-0005` proves that large mildly supercritical alphabets are abundant.
Cardinality is no longer the central bottleneck. Construct an infinite family
of parity collision codes with one or more of the following stronger
properties:

1. **Complete small-modulus projection:** the induced digit set meets every
   residue class modulo \(2^{b_m}\), with \(b_m\to\infty\).
2. **Difference-set intervals:** \([-R_m,R_m]\subseteq D_m-D_m\), with a
   quantitatively useful growth rate.
3. **Tensorable precision surplus:** high-surplus suffix codes absorb
   independent prefix gadgets under `L-0006`.
4. **Carry relay quality:** the mixed-radix carry graph contains a finite family
   of tiles whose vertical outputs remain parseable.
5. **Skeleton closure:** the alphabet supports a finite set of uniform
   `S`-unit cofactor transitions.
6. **Controlled expansion:** retain \(1<N/M\le3/2\), or another explicitly
   bounded margin suitable for slow boundary motion.

`O-0005` is the first finite witness of this direction:

- 339 digits;
- all residue classes modulo 16;
- \([-934,934]\subseteq D-D\);
- expansion ratio approximately 1.3004.

The next objective is a theorem producing such geometry for unbounded
parameters, not a larger isolated census record.

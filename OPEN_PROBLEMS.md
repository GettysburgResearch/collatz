# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`  
Active draft PR: `#3`

## Q-0001 — Finite-boundary regeneration

Status: `IDEA` / central open target  
Dependencies: `T-0002`, `T-0003`, `T-0004`, `T-0005`, `T-0006`

For at least one supercritical collision fiber, construct one ordinary finite integer \(A_0\) in the required lifting congruence class such that every iterate of

\[
H_D(MB+d)=NB+d,
\qquad d\in D,
\]

remains admissible.

A valid solution must prove infinite behavior from one finite starting word. The following are insufficient by themselves:

- arbitrarily long finite trajectories;
- compatible residues modulo \(M^k\) for every fixed \(k\);
- a periodic or aperiodic point in \(\mathbb Z_2\);
- a spatially periodic carry tiling;
- a numerical trajectory checked to any finite height;
- an alphabet whose cardinality tends to infinity;
- arbitrary collision-code precision;
- preservation of any fixed finite amount of alphabet geometry.

Two equivalent construction targets remain:

1. a finite vertical macro-tile grammar with a finite high-order boundary; or
2. a finite family of run-length/cofactor schemas closed under `T-0004`.

## Q-0002 — Analytic growth of collision fibers

Status: `PROPOSED RESOLUTION` by `T-0005`  
Dependencies: `L-0005`, `T-0005`

`T-0005` proves

\[
|D_m|
\ge
\left\lceil\frac{\binom{3m}{m}}{3^m}\right\rceil
\sim
\frac{\sqrt3}{2\sqrt{\pi m}}
\left(\frac94\right)^m
\]

while keeping the expansion factor in \((1,3/2]\). The resolution remains `PROPOSED` until independent review.

The optimization part has moved to `Q-0009` and `Q-0010`: produce closure-relevant geometry, not only cardinality.

## Q-0003 — Carry grammar for the width-three chart

Status: `IDEA`  
Dependencies: `O-0002`, `L-0004`

For

\[
H(512B+d)=729B+d,
\qquad d\in\{0,1,2\},
\]

classify short carry macro-tiles and determine whether they combine into a finite vertically regenerative grammar.

One exact local tile is

\[
R_1L_{361}L_0\longrightarrow L_2L_2R_1.
\]

It returns the carry after two columns and emits admissible digits, but direct repetition fails vertically. The target is a relay of several tiles.

## Q-0004 — Multi-chart transition groupoid

Status: `IDEA`  
Dependencies: `T-0002`, `O-0001`--`O-0005`, `T-0005`

Construct exact finite bridges among different collision charts. One branching code can support several charts through different finite tails. A successful cycle may let one chart repair the boundary produced by another while retaining net expansion.

A bridge must record source and target gauges, lifting classes, the exact finite Collatz word, every free-parameter transformation, positivity, integrality, and the effect on the run-length skeleton.

## Q-0005 — Finite versus adic closure criterion

Status: `IDEA`  
Dependencies: `T-0003`

Develop a criterion deciding when a finitely generated admissible itinerary represents an ordinary nonnegative integer rather than a nonordinary 2-adic point.

`T-0003` already rules out eventually periodic digit itineraries for nontrivial ordinary-integer orbits. The target should cover aperiodic morphic, substitutional, code-composed, or `S`-adic sequences and expose a finite-boundary condition.

## Q-0006 — Independent verification

Status: `IDEA`

Reconstruct the active contribution without relying on its author's confidence:

- check chronological parity orientation;
- check `L-0001`, `L-0003`, and `L-0005`;
- reproduce `X-0001` through `X-0004`;
- check `T-0002`, `T-0003`, and both directions of `T-0004`;
- reconstruct the pigeonhole, CRT, positivity, and lifting steps in `T-0005`;
- check the suffix precision requirement and tensor orientation in `L-0007`;
- check the exact valuation in `L-0008`;
- check tail-invariance and product cardinality in `T-0006`;
- identify the first unsupported inference, if any.

## Q-0007 — Vertical macro-tile closure

Status: `IDEA`  
Dependencies: `L-0004`, `T-0003`, `O-0005`, `T-0006`

Construct a finite collection of mixed-radix carry tiles whose emitted rows can be parsed as controlled input rows at later times, while the high-order boundary remains finite and follows the aperiodic growth rate

\[
\log_M(N/M).
\]

`O-0005` supplies a 339-symbol chart with full projection modulo 16 and a long difference interval. `T-0006` shows that any finite relay found there can be preserved while branch count grows. Determine whether a relay can also close vertically.

## Q-0008 — Parameterized `S`-unit skeleton schemas

Status: `IDEA`  
Dependencies: `T-0004`, `O-0005`, `T-0006`

Find a finite family of positive-integer schemas closed under

\[
d_k+N^{u_k}C_k
=d_{k+1}+M^{u_{k+1}}C_{k+1}.
\]

A successful family must keep active digits admissible, cofactors positive and indivisible by the input radix, generate an aperiodic exponent schedule, preserve or transition lifting classes, and arise from one finite initial triple.

The difference interval in `O-0005` makes bounded corrections less scarce. `T-0006` preserves any finite collection of such corrections during further code amplification.

## Q-0009 — Structured collision codes and closure-quality geometry

Status: `IDEA`  
Dependencies: `L-0006`, `T-0005`, `O-0005`, `L-0007`, `T-0006`

Large mildly supercritical alphabets are abundant. Construct parity collision codes with one or more of:

1. complete projection modulo \(2^{b_m}\) with \(b_m\to\infty\);
2. difference intervals \([-R_m,R_m]\subseteq D_m-D_m\) with useful growth;
3. tensorable precision surplus;
4. finite carry relays whose vertical outputs remain parseable;
5. closure on finitely many `S`-unit cofactor schemas;
6. controlled mild expansion.

`O-0005` is a finite witness. `T-0006` proves that all of its fixed geometry survives in arbitrarily large supercritical fibers. The unresolved demand is geometry that grows with the construction scale.

## Q-0010 — Growing geometry under tensor amplification

Status: `IDEA` / primary next theorem target  
Dependencies: `L-0007`, `L-0008`, `T-0006`

The exact tensor law is

\[
D_{UV}=D_U+2^{L_U}E_V.
\]

`L-0008` supplies suffix codes of arbitrary precision, but their two offsets are sparse. Construct a hierarchy of high-precision suffix codes whose normalized offset alphabets force one of the following:

1. a new controlled binary digit at each composition level;
2. surjectivity modulo a power of two whose exponent tends to infinity;
3. difference intervals whose radius grows at least as fast as the finite boundary requires;
4. a vertically composable relay tile at each scale;
5. a finite-state reinterpretation of the separated odd offsets as an aperiodic moving-boundary address system.

Alternatively, prove an obstruction showing that fixed-weight chronological concatenation cannot produce such growing geometry. Such a theorem would force a variable-weight, multi-chart, or non-concatenative construction.
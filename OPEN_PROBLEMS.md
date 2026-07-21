# Open problems

Last updated: 2026-07-21  
Active packet: issue `#2`  
Active draft PR: `#3`

## Q-0001 — Finite-boundary regeneration

Status: `IDEA` / central target

Construct one ordinary finite positive state whose Collatz trajectory remains inside an exact expanding grammar forever.

Equivalent current formats include:

1. a finite aperiodic mixed-radix macro-grammar;
2. finitely many run-length/cofactor schemas;
3. a signed rational-base return chain;
4. a graph of negative return phases;
5. a finite phase plus a cycle-padding stack;
6. a finite endpoint-interval grammar;
7. a two-layer particle grammar carrying one distinguished ordinary spine.

Finite experiments, inverse-limit points, large alphabets, complete modular projection, positive symbolic pressure, and unmarked phase escape are insufficient without the marked ordinary boundary.

## Q-0002 — Analytic fiber growth

Status: `PROPOSED RESOLUTION` by `T-0005`

Mildly supercritical collision fibers have exponentially unbounded cardinality.

## Q-0003 — Carry grammar for the width-three chart

Status: `IDEA`

Classify finite vertical relays for

\[
H(512B+d)=729B+d,
\qquad d\in\{0,1,2\}.
\]

The known short horizontal tile does not close vertically.

## Q-0004 — Multi-chart and multi-phase transition groupoid

Status: `IDEA`

Construct exact bridges among collision charts and negative phases, including changes of:

- affine or interval gauge;
- target phase;
- quotient coordinate;
- padding counter;
- run-length cofactor;
- marked finite boundary.

A finite complete recurrent phase graph collapses to phase \(1\). The successful graph must be incomplete and exceptional, have an unbounded state component, and preserve the ordinary marker.

## Q-0005 — Finite versus adic closure

Status: `IDEA`

Give a usable criterion deciding when an aperiodic finitely generated parity or return language contains one ordinary nonnegative integer rather than only a 2-adic point.

`T-0018` sharpens the target: an ordinary integer is represented by a finite marked root particle and its distinguished lineage. Develop a grammar-level criterion ensuring that this marker is preserved indefinitely.

## Q-0006 — Independent verification

Status: `IDEA`

Independently reconstruct the active branch, now especially:

- `T-0014` and `L-0013`, including both phase coordinate systems;
- the padding congruence and towers in `T-0015`;
- the two Kraft identities and pressure law in `T-0016`;
- martingale absorption and the Doob transform in `T-0017`;
- interval endpoint roundings and gauge statements in `L-0014`;
- the ordered child partitions and distinguished odd child in `T-0018`;
- the escape/growth/marked-spine mass distinction in `T-0019`;
- exact reproduction of `X-0008` through `X-0010`.

## Q-0007 — Vertical macro-tile closure

Status: `IDEA`

Build a finite collection of exact mixed-radix, endpoint, or negative-return tiles whose outputs remain parseable while the ordinary boundary grows at the correct aperiodic rate.

The current preferred form is a two-layer tile:

- an unmarked population or interval rewrite;
- a marked distinguished boundary particle.

## Q-0008 — Parameterized S-unit skeleton schemas

Status: `IDEA`

Find finitely many positive schemas closed under

\[
d+N^uC=d'+M^{u'}C'.
\]

The construction must preserve exact valuation, positivity, phase transitions, and one finite marked start.

## Q-0009 — Structured collision codes

Status: `PARTIAL`

Proposed resources include:

- exponentially large mildly supercritical fibers;
- arbitrary finite precision;
- preservation of fixed geometry;
- complete projection modulo \(2^b\) for every \(b\).

Still open:

- growing difference intervals with useful bounds;
- macroscopic normalized displacement width;
- scale-independent marked relays;
- direct quotient/cofactor closure.

## Q-0010 — Growing complete dyadic projection

Status: `PROPOSED RESOLUTION` by `L-0009`, `L-0010`, `T-0007`

For every \(b\ge1\), there is a mildly supercritical collision fiber whose offsets meet every residue modulo \(2^b\).

## Q-0011 — Convert dyadic freedom into a positive relay

Status: `IDEA`

Use complete projection to obtain an exact positive relay for

\[
Nq=Mq'+a
\]

or the run-length equation.

Required output:

- prescribed exact valuation;
- positive next quotient in a controlled range;
- compatible phase transition;
- closure under finitely many schemas;
- preservation of the distinguished ordinary marker.

## Q-0012 — Infinite regular negative-template renewal code

Status: `IDEA`

Construct a finitely generated exact return language satisfying:

1. deterministic cylinder selection;
2. forward phase closure;
3. positive growth on every realizable grammar cycle;
4. one explicit finite marked ordinary quotient.

A complete broad cover is impossible. The target is a thin exceptional language with a certified ordinary spine.

## Q-0013 — Macroscopic aspect-ratio systems

Status: `IDEA`

For a chart define

\[
\Delta=rac{\operatorname{diam}D}{N-M}.
\]

Construct a family or graph-directed cycle whose effective normalized displacement windows remain macroscopic while expansion, phase escape, and marked-boundary transport remain sufficient.

## Q-0014 — Finite phase plus cycle-padding stack closure

Status: `IDEA`

Use the negative eleven-cycle towers to build a pushdown rule satisfying:

1. exact return-cylinder closure;
2. padding above edge-specific growth thresholds;
3. avoidance or compensation of descent to phase \(1\);
4. one finite ordinary initialization;
5. infinite deterministic block generation;
6. explicit transport of the distinguished particle through every padded block.

## Q-0015 — Pressure-positive ordinary survivor language

Status: `IDEA`

For a candidate return graph track:

\[
\mathcal A_0(i,j)
=
\sum_{e:i\to j}2^{-L_e},
\]

\[
\mathcal A_1(i,j)
=
\sum_{e:i\to j}2^{-L_e}\lambda_e,
\]

and the phase escape factor

\[
\frac{v_j-1}{v_i-1}.
\]

Construct a subgrammar with:

- small fair mass;
- positive deterministic cycle growth;
- positive tilted/escape pressure;
- one ordinary finite marked lineage.

`T-0019` warns that unmarked pressure can be positive even though the required marked lineage remains exponentially thin.

## Q-0016 — Multi-mismatch complement automaton

Status: `IDEA`

Build the complete iterated mismatch system using the rounded phase maps

\[
S_0(v)=\lceil v/2\rceil,
\qquad
S_1(v)=\lfloor3v/2\rfloor.
\]

Compress periodic negative-cycle excursions into counters and determine whether a pressure-positive pushdown component closes while preserving a marked ordinary spine.

## Q-0017 — Arithmetic approximation to the phase escape transform

Status: `IDEA`

The exact escape transition probabilities are

\[
\mathbb Q_v(e)
=
\frac{S_e(v)-1}{2(v-1)}.
\]

They give positive unmarked phase and Collatz log drift. Construct an exact return grammar approximating this transform.

The session `T-0018`--`T-0019` adds a non-negotiable qualification:

> the escape transform governs branch populations, not the single marked ordinary descendant.

Concrete tasks:

1. define a finite or pushdown phase partition;
2. choose exact negative-template words approximating \(\mathbb Q\);
3. certify graph-cycle growth;
4. prove forward invariance of accepted populations;
5. add a deterministic distinguished-child rule;
6. exhibit one explicit finite marked quotient.

## Q-0018 — Marked ordinary-spine rewrite grammar

Status: `IDEA` / primary new target  
Dependencies: `L-0014`, `T-0018`, `T-0019`

Construct a finite-state, substitutional, or pushdown two-layer grammar.

### Population layer

A finite interval or ordered population is rewritten using exact local rules. This layer should regenerate, grow, or admit a positive phase/pressure potential.

### Marker layer

One finite root particle is marked. At each rewrite it must be sent through

\[
\chi(j)=
\begin{cases}
(0,j/2),&j\text{ even},\\[1mm]
(1,(3j+1)/2),&j\text{ odd}.
\end{cases}
\]

The grammar must prove that the marked ranks remain defined forever and are unbounded.

Desired certificate:

1. one explicit finite initial interval and marker;
2. a finite family of parameterized rewrite schemas;
3. exact regeneration of the unmarked population;
4. deterministic preservation of the marker;
5. a monotone marked-rank or graph potential;
6. no appeal to a left-infinite or inverse-limit boundary.

A solution of this problem would be a direct string-rewrite Collatz counterexample certificate.

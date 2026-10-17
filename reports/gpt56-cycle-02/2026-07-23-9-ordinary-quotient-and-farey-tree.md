# Session report — ordinary quotient decoder and full Farey-tree offense

```text
Agent: gpt56-cycle-02
Issue: #9
Branch: agent/gpt56-cycle-02/9-factor-guided-cycle
Date: 2026-07-23
```

## Objective

Push simultaneously on:

1. the exact negative-three/six-branch ordinary divergence chart; and
2. the critical mechanical full-denominator cycle circuit.

The acceptance gate remained one explicit positive integer with either a complete nontrivial return or an all-time ordinary growth invariant. No finite prefix, modular lasso, proper-factor hit, or completion point was treated as a counterexample.

## Sources inspected

The pass integrated the live constructive interfaces from:

- PR #45: critical mechanical compiler, six-branch quotient chart, and intrinsic core;
- PR #51: normalized negative-three chart, maximal-run highway, and reset family;
- PR #49: deterministic one-counter/top-boundary formulation;
- PR #34: complete-cycle replay, cross-prime compiler, and sparse-defect boundaries;
- existing PR #50 waves: length-185 exclusion and paired-chart/mechanical bridge.

## Result 1 — exact ordered-repair decoder (`L-8306`)

Every canonical local repair has an exact delta

```text
Delta_j = sign_j * 2^v_j * odd_j
```

with strictly increasing `v_j` when sites are ordered left to right.

For an ordinary quotient candidate `N`, the exact equation

```text
C_0 + sum x_j Delta_j = N D
```

has at most one binary repair vector.  The vector is decoded from the residual `ND-C_0` one dyadic digit at a time:

```text
v_2(residual)<v_j  -> impossible;
v_2(residual)=v_j  -> x_j=1;
v_2(residual)>v_j  -> x_j=0.
```

This targets the complete ordinary identity, not `C=0 mod M` for a proper factor.

## Correction caught during review

The first three canonical greedy run sites are

```text
0, 7, 16
```

with delta valuations

```text
16, 146, 314.
```

An authoring draft used `0,7,15` and `16,146,295`.  The correction strengthens the decisive modulus from `2^295` to `2^314`.  `L-8307`, `T-8304`, and both X-8305 implementations use the corrected values.  X-8304/T-8303 are retained only as corrected, superseded checkpoints.

## Result 2 — full greedy grammar (`L-8307`, `T-8304`, `X-8305`)

A three-state weighted transducer compiles the complete lower critical run word through the Euclidean mechanical recursion.  It finds exactly

```text
30,790,984,112
```

canonical pairwise-disjoint unequal-run sites.  The grammar therefore has

```text
2^30,790,984,112
```

valid words with the same complete denominator.

The transducer simultaneously computes the complete positive and negative real repair envelope.  The first two repair bits fix the quotient modulo `2^314`; every later repair is invisible at that precision.  The complete real integer window is positive and below `2^314`, but none of the four quotient residues lies in it.

Thus the entire grammar is excluded by the complete ordinary equation.

## Result 3 — full hierarchical Farey grammar (`L-8308`, `T-8306`, `X-8306`)

The critical mechanical run word was recursively split into its two Farey parents at every Christoffel node.  At every internal occurrence, the recursively repaired children may remain in order or reverse.

The fully expanded parse contains

```text
267,629,447,755 leaves,
267,629,447,754 internal occurrences.
```

Two exact compilers were built:

1. the full set of possible affine numerators modulo `2^314`;
2. the directed real convex envelope of all fixed points.

The real envelope is positive, contains integers, and lies below `2^314`.  None of the exact quotient residues intersects its integer window.  Therefore the complete hierarchical Farey sibling-swap grammar contains no integral cycle.

The author implementation uses memoized recursion; the verifier uses a bottom-up Farey DAG.

## Result 4 — the two positive charts are one system (`T-8305`)

For consecutive six-branch types `i_n`, define

```text
R_n = 5 + i_n - i_(n+1).
```

The intrinsic-core recurrence becomes exactly

```text
2^(4+3R_n) u_(n+1)
 = 9^(R_(n-1)+1) u_n + 7.
```

A run schedule has a six-state type realization exactly when the partial sums of `R_n-5` have total range at most five.

Every forever-defined positive path is automatically unbounded because its homogeneous product is

```text
(3^12/2^19)^m
```

up to a uniformly bounded endpoint factor, and `3^12>2^19`.

## Result 5 — constant-slope gauge (`L-8309`)

The gauge

```text
y_n = 3^(2 i_(n-1)) 2^(-3 i_n) u_n
```

converts the intrinsic core to

```text
y_(n+1)
 = (3^12/2^19) y_n
   + (7/2^19)(9/8)^(i_n).
```

The six-branch offense is therefore a constant-slope expanding rational-base system with six positive digits and a 36-phase ordinary lattice condition.

## Result 6 — all eventual periods excluded (`T-8307`)

For a type period `p`, one period block has

```text
2^(19p) x' = 3^(12p) x + B,
B>0.
```

All-time integrality forces the unique `2`-adic fixed point

```text
x = B/(2^(19p)-3^(12p)),
```

which is negative in the real embedding.  Hence no positive ordinary path can have an eventually periodic type tail.  Autonomous finite-state type generators are excluded; nonlinear unbounded-core/top-boundary controllers remain open.

## Candidate counterexamples

None.  No `K-83xx` object was assigned.

## Failed or closed attacks

- Individual proper-factor repair subsets are no longer the right search object.
- The complete canonical greedy local grammar is closed.
- The complete fixed-shape Farey sibling-swap grammar is closed.
- Autonomous periodic type schedules are closed.
- A long finite six-branch prefix would still be only a cylinder, not a witness.

## Exact surviving positive targets

### Divergence lane

Construct one finite ordinary state

```text
(i_-1, i_0, u_0, canonical top boundary)
```

whose deterministic six-branch transition remains defined forever.  Growth then follows from `T-8305`.

### Cycle lane

The first surviving critical grammar must change the low quotient digits unavailable to the fixed-shape Farey tree.  The strongest targets are:

1. controlled changes between adjacent upper convergent shapes;
2. multi-shape compressed blocks carrying `C-ND` directly;
3. at least-seven-defect gadgets with a new early dyadic spectrum.

A terminal exact zero receives immediate independent valuation and shortcut-Collatz replay.

## Verification status

The mathematical identities and both large grammar computations were independently reconstructed during the session.  The committed author/verifier pairs are standard-library exact arithmetic.  The GitHub connector cannot execute branch commands; repository CI or an external reviewer should replay the frozen files before status promotion.

## Organizational improvement

Future compressed-cycle experiments should expose, from the start:

```text
real ordinary quotient window,
complete-denominator residual C-ND,
ordered dyadic repair valuations,
exact top-boundary or quotient cylinder.
```

A proper-factor modular join without those coordinates is now known to leave most of the decisive information unused.

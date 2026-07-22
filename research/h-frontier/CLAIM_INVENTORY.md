# Noncanonical claim inventory: H exact frontier

This index reserves the `*-9500` identifiers for issue #17. It is not the
repository's canonical `CLAIMS.md`. All theorem-level statements remain
`PROPOSED` pending independent review. Finite audits `X-9501` through `X-9507`
are empirical or exact finite checks and do not promote any universal claim.

## Packet files

- [`claims/EXACT_SYSTEM.md`](claims/EXACT_SYSTEM.md) — `D-9501`, `L-9501`–`L-9504`.
- [`claims/SURVIVOR_THEORY.md`](claims/SURVIVOR_THEORY.md) — `T-9501`–`T-9503`, `L-9505`.
- [`claims/DISPLACEMENT_FRONTIER.md`](claims/DISPLACEMENT_FRONTIER.md) — `C-9501`, `L-9506`, `Q-9501`.
- [`claims/STRUCTURAL_RESULTS.md`](claims/STRUCTURAL_RESULTS.md) — `L-9507`–`L-9510`, `R-9501`, `R-9502`, `Q-9502`.
- [`claims/ITERATION_02.md`](claims/ITERATION_02.md) — `L-9511`, `L-9512`, `T-9504`, `T-9505`, `R-9503`, `Q-9503`.
- [`claims/ITERATION_03.md`](claims/ITERATION_03.md) — `L-9513`–`L-9515`, `T-9506`–`T-9508`, `Q-9504`, `Q-9505`.
- [`claims/ITERATION_04.md`](claims/ITERATION_04.md) — `T-9509`.
- [`claims/ITERATION_05.md`](claims/ITERATION_05.md) — `L-9516`, `T-9510`, `Q-9506`.
- [`claims/ITERATION_06.md`](claims/ITERATION_06.md) — `L-9517`, `L-9518`, `T-9511`, `T-9512`, `Q-9507`.
- [`claims/ITERATION_07.md`](claims/ITERATION_07.md) — `L-9519`, `L-9520`, `T-9513`, `T-9514`, `R-9504`, `Q-9508`.
- [`claims/ITERATION_08.md`](claims/ITERATION_08.md) — `L-9521`, `L-9522`, `T-9515`, `R-9505`, `Q-9509`.
- [`../../experiments/X-9506-h-counterexample-search/README.md`](../../experiments/X-9506-h-counterexample-search/README.md) — exact ordinary and short-period counterexample sweep.
- [`../../experiments/X-9507-h-cycle-complexity/README.md`](../../experiments/X-9507-h-cycle-complexity/README.md) — exact continued-fraction cycle-period certificate.

## Status table

| ID | Title | Status | Main dependency / caveat |
| --- | --- | --- | --- |
| `D-9501` | Exact `p`-coordinate block system | PROPOSED | self-contained |
| `L-9501` | H-to-shortcut-Collatz lift | PROPOSED | `D-9501` |
| `L-9502` | Exact finite cylinders | PROPOSED | self-contained after `D-9501` |
| `L-9503` | Carries and ghost stabilization | PROPOSED | `L-9502` |
| `L-9504` | Toll-Euler identity | PROPOSED | `D-9501` |
| `T-9501` | Infinite-survivor harmonic summability | SUPERSEDED | stronger plastic bound `T-9506` |
| `T-9502` | Nonperiodic survivors real-escape | PROPOSED | `L-9504`, preferably `T-9506` |
| `T-9503` | Equivalent infinite-obstruction formulations | PROPOSED | `L-9503`, `T-9502` |
| `L-9505` | Bounded-representative finite branching | PROPOSED | exact finite-tree target |
| `C-9501` | Signed displacement for exact cylinders | EMPIRICAL | universal mixed-sign carry step open |
| `L-9506` | Conditional contracting-cylinder descent | PROPOSED | conditional on `C-9501` |
| `L-9507` | Finite prime support exclusion | PROPOSED | imports S-unit finiteness |
| `L-9508` | Prime reuse through offsets | PROPOSED | self-contained |
| `R-9501` | No finite itinerary-only obstruction | PROPOSED | consequence of `L-9502` |
| `R-9502` | Direct ghost congruence correction | PROPOSED | consequence of `L-9502` |
| `Q-9501` | Carry-rectangle lemma | IDEA | broad form of the mixed-sign gap |
| `Q-9502` | Weighted bounded-representative termination | IDEA | one-sided obstruction |
| `L-9509` | Two-sided exact-window density | PROPOSED | finite-window consequence |
| `L-9510` | Long expanding finite shadows | PROPOSED | finite shadows are not infinite orbits |
| `L-9511` | Canonical endpoint range and fixed-point phase | PROPOSED | self-contained after `L-9502` |
| `L-9512` | Same-sign phase closure | PROPOSED | mixed-sign case remains |
| `Q-9503` | Word-specific mixed-sign crossing | IDEA | sharp finite descent frontier |
| `R-9503` | Naive first-letter fixed-point bound is false | PROPOSED | exact length-25 witness; `X-9502` |
| `T-9504` | Subcritical weighted survivor moments | SUPERSEDED | stronger branchwise theorem `T-9507` |
| `T-9505` | Capital--core discounted budget | PROPOSED | `L-9504`, `T-9502` |
| `L-9513` | Exact first-crossing intermediate threshold | PROPOSED | zero-carry inequality remains |
| `L-9514` | Separated ghost IFS and plastic recurrence | PROPOSED | self-contained from ghost recursion |
| `T-9506` | Plastic power bound for ordinary survivors | PROPOSED | `L-9503`, `L-9514` |
| `T-9507` | Branchwise critical harmonic kernel | PROPOSED | uniform core-reciprocal budgets |
| `L-9515` | Repetition forces completion height | PROPOSED | complexity corollary uses real escape |
| `T-9508` | Critical/subcritical real-escape split | PROPOSED | depends on `T-9505` |
| `Q-9504` | `2`-adic logarithm critical-chain exclusion | SUPERSEDED | resolved by `T-9509` modulo Yu audit |
| `Q-9505` | Subcritical transformed-height finite trap | SUPERSEDED | sharpened by `Q-9507` |
| `T-9509` | Critical real escape is impossible | PROPOSED | imports Yu 2007; specialization needs audit |
| `L-9516` | Centered rooms around the fixed ghost `4` | PROPOSED | outer-room decomposition only |
| `T-9510` | Monotone ordinary-section minimum | PROPOSED | boundary step repaired by `L-9517` |
| `Q-9506` | Ordinary-section minimum divergence | IDEA | direct proof target `nu_K -> infinity` |
| `L-9517` | Complete finite-code boundary classification | PROPOSED | repairs the closure boundary in `T-9510` |
| `L-9518` | Dual renewal bridge and integral sign law | PROPOSED | centered two-place normal form |
| `T-9511` | Subcritical future-core demand | PROPOSED | assumes the post-Yu subcritical regime |
| `T-9512` | Minimal-survivor relative toll bound | PROPOSED | conditional on a nonperiodic survivor |
| `Q-9507` | Subcritical renewal finite trap | IDEA | integral transformed height still open |
| `L-9519` | Exact rounded-deficit pressure | PROPOSED | self-contained from `D-9501` |
| `L-9520` | Successive-renewal compatibility and prime firewall | PROPOSED | self-contained from `L-9518` |
| `T-9513` | Fixed bridge-prime support is finite | PROPOSED | imports nondegenerate S-unit finiteness |
| `T-9514` | Final finite-alphabet / reset-renewal dichotomy | PROPOSED | conditional on audited `T-9509` |
| `R-9504` | Pressure and fresh mass are scale-compatible | PROPOSED | blocks false one-dimensional closures |
| `Q-9508` | Discounted fresh mass or finite-alphabet nonstabilization | IDEA | two exact remaining branches |
| `L-9521` | Positive cycle minimum bound | PROPOSED | elementary cycle lemma and exact affine recurrence |
| `T-9515` | No positive cycle through 2,479,700,524 blocks | PROPOSED | `L-9521`, exact `X-9506`/`X-9507`, Legendre theorem |
| `L-9522` | Finite-alphabet entropy--capital barrier | PROPOSED | `T-9502`, `L-9515` |
| `R-9505` | Low-complexity slow-bank templates are impossible | PROPOSED | consequence of `L-9522` |
| `Q-9509` | Structured counterexample interface | IDEA | high-entropy finite alphabet or unbounded reset--renewal |
| `X-9506` | Exact counterexample-first ordinary and short-period sweep | INTERNAL EXACT | finite only; no survivor below `p<3*2^65`, no word cycle through period 14 |
| `X-9507` | Exact cycle-period compression certificate | INTERNAL EXACT | finite only; supports `T-9515` |

## Dependency summary

A direct proof of H would follow from

\[
\nu_K\longrightarrow\infty
\]

in `Q-9506`; this route bypasses the signed-displacement conjecture. The older
descent architecture would follow from `C-9501` together with `Q-9502`.

Iterations 02--05 established the canonical phase reduction, plastic survivor
pressure, the discounted capital--core budget, exclusion of the critical
near-Pillai mode (subject to a Yu-theorem audit), and the monotone ordinary
minimum.

Iteration 06 added complete closure-boundary classification, the exact centered
two-place renewal bridge, an integral renewal height, and the future-weighted
subcritical core demand. Iteration 07 added rounded-deficit pressure, the prime
firewall, fixed-prime-support exclusion, and the finite-alphabet versus
reset--renewal split.

Iteration 08 attacks structured counterexamples directly:

1. `L-9521` bounds one state of every positive cycle by `L/(1-M)`;
2. `T-9515` combines that bound with `X-9506`, exact rational logarithm
   intervals, and Legendre compression to exclude every positive cycle through
   `2,479,700,524` blocks;
3. `L-9522` proves that a finite-alphabet survivor with logarithmic capital
   growth must have a quantitatively positive factor entropy;
4. `R-9505` excludes logarithmically banked Sturmian, Beatty, automatic, and
   primitive-substitution templates of zero entropy.

`X-9506` exhausts every ordinary candidate below `3*2^65`; its largest exact
block lifetime is thirty-four. `X-9507` upgrades the periodic exclusion from
word period fourteen to more than 2.47 billion blocks by a proof-producing
continued-fraction certificate.

No structured counterexample has been found. A viable one must now be
nonperiodic and either have sufficiently high finite-alphabet entropy and
capital growth, or use unbounded reset--renewal letters while satisfying the
fresh-prime and discounted-budget restrictions. It must additionally provide
one positive integer initialization with an exact induction proving legality
and nontermination.
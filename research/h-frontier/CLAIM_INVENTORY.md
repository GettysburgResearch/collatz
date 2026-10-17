# Noncanonical claim inventory: H exact frontier

This index reserves the `*-9500` identifiers for issue #17. It is not the
repository's canonical `CLAIMS.md`. All theorem-level statements remain
`PROPOSED` pending independent review. Finite audits `X-9501` through `X-9510`
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
- [`claims/ITERATION_08B.md`](claims/ITERATION_08B.md) — `L-9523`, `R-9506`, `Q-9510`.
- [`claims/ITERATION_09.md`](claims/ITERATION_09.md) — `L-9524`, `L-9525`, `R-9507`, `Q-9511`.
- [`claims/ITERATION_10.md`](claims/ITERATION_10.md) — `L-9526`, `T-9516`, `T-9517`, `R-9508`, `Q-9512`.
- [`claims/ITERATION_11.md`](claims/ITERATION_11.md) — `L-9527`, `L-9528`, `T-9518`, `R-9509`, `Q-9513`.
- [`claims/ITERATION_12.md`](claims/ITERATION_12.md) — `L-9529`, `L-9530`, `T-9519`, `R-9510`, `Q-9514`.
- [`../../experiments/X-9506-h-counterexample-search/README.md`](../../experiments/X-9506-h-counterexample-search/README.md) — exact ordinary and short-period counterexample sweep.
- [`../../experiments/X-9507-h-cycle-complexity/README.md`](../../experiments/X-9507-h-cycle-complexity/README.md) — exact continued-fraction cycle-period certificate.
- [`../../experiments/X-9508-h-compiler-renewal/README.md`](../../experiments/X-9508-h-compiler-renewal/README.md) — exact compiler and centered-renewal box audit.
- [`../../experiments/X-9509-h-renewal-counter/README.md`](../../experiments/X-9509-h-renewal-counter/README.md) — exact renewal one-counter and refund-graph audit.
- [`../../experiments/X-9510-h-intrinsic-renewal/README.md`](../../experiments/X-9510-h-intrinsic-renewal/README.md) — exact one-integer renewal and predecessor audit.

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
| `R-9503` | Naive first-letter fixed-point bound is false | PROPOSED | exact witness; `X-9502` |
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
| `L-9517` | Complete finite-code boundary classification | PROPOSED | repairs closure boundary in `T-9510` |
| `L-9518` | Dual renewal bridge and integral sign law | PROPOSED | centered two-place normal form |
| `T-9511` | Subcritical future-core demand | PROPOSED | assumes post-Yu subcritical regime |
| `T-9512` | Minimal-survivor relative toll bound | PROPOSED | conditional on a nonperiodic survivor |
| `Q-9507` | Subcritical renewal finite trap | IDEA | integral transformed height still open |
| `L-9519` | Exact rounded-deficit pressure | PROPOSED | self-contained from `D-9501` |
| `L-9520` | Successive-renewal compatibility and prime firewall | PROPOSED | self-contained from `L-9518` |
| `T-9513` | Fixed bridge-prime support is finite | PROPOSED | imports nondegenerate S-unit finiteness |
| `T-9514` | Finite-alphabet / reset-renewal dichotomy | PROPOSED | conditional on audited `T-9509` |
| `R-9504` | Pressure and fresh mass are scale-compatible | PROPOSED | blocks false one-dimensional closures |
| `Q-9508` | Discounted fresh mass or finite-alphabet nonstabilization | IDEA | two exact remaining branches |
| `L-9521` | Positive cycle minimum bound | PROPOSED | exact affine recurrence |
| `T-9515` | No positive cycle through 2,479,700,524 blocks | PROPOSED | exact finite certificates and Legendre |
| `L-9522` | Finite-alphabet entropy--capital barrier | PROPOSED | `T-9502`, `L-9515` |
| `R-9505` | Low-complexity slow-bank templates are impossible | PROPOSED | consequence of `L-9522` |
| `Q-9509` | Structured counterexample interface | IDEA | high entropy or reset-renewal |
| `L-9523` | Prefix-return capital barrier | PROPOSED | exact repeated-factor divisibility |
| `R-9506` | Short-return substitutions require excessive capital | PROPOSED | consequence of `L-9523` |
| `Q-9510` | Delayed-novelty structured interface | IDEA | carry stabilization remains mandatory |
| `L-9524` | Zero-carry macro descent criterion | PROPOSED | exact fixed-point comparison |
| `L-9525` | `10/30` compiler counterexample no-go | PROPOSED | compiler data and survivor pressure |
| `R-9507` | Abstract tail freedom is not physical ordinary freedom | PROPOSED | consequence of `L-9525` |
| `Q-9511` | Physical expanding macro construction interface | IDEA | zero carry, growth, escape required |
| `L-9526` | Polynomial finite-macro growth barrier | PROPOSED | plastic survivor count |
| `T-9516` | Quantitative renewal-prime budget | PROPOSED / SOURCE-DEPENDENT | ESS specialization audit |
| `T-9517` | Sharp survivor deficit pressure | PROPOSED | toll and rounded-deficit identities |
| `R-9508` | Finite control and qualitative fresh primes are insufficient | PROPOSED | construction boundary |
| `Q-9512` | Positive-cycle-exploiting macro interface | IDEA | all-time physical induction required |
| `L-9527` | Canonical renewal type cylinders | PROPOSED | exact two-place equations |
| `T-9518` | Counterexample equivalence and `1/21` renewal Kraft law | PROPOSED | `L-9518`, `L-9527` |
| `L-9528` | Exact refund-edge growth criterion | PROPOSED | `L-9527` |
| `R-9509` | Refund SCC is not an ordinary witness | PROPOSED | finite-state projection boundary |
| `Q-9513` | Forever-defined renewal-counter atom | IDEA | explicit tuple would disprove H and Collatz |
| `L-9529` | Intrinsic one-integer renewal decoder | PROPOSED | removes trusted type/counter metadata |
| `L-9530` | Exact renewal predecessor/source test | PROPOSED | `L-9529` |
| `T-9519` | Minimal-survivor source gate | PROPOSED | conditional on a nonperiodic survivor |
| `R-9510` | Intrinsic compression does not imply definedness | PROPOSED | ordinary boundary remains |
| `Q-9514` | One-integer counterexample atom | IDEA | one forever-defined `Z_0` would settle negative direction |
| `X-9506` | Ordinary and short-period sweep | INTERNAL EXACT | finite only |
| `X-9507` | Cycle-period compression certificate | INTERNAL EXACT | finite only |
| `X-9508` | Compiler and renewal-box audit | INTERNAL EXACT | finite only |
| `X-9509` | Renewal one-counter/refund graph audit | INTERNAL EXACT | finite only |
| `X-9510` | Intrinsic renewal and predecessor audit | INTERNAL EXACT | finite only; 746,496 states, max life 5 |

## Dependency summary

A direct proof of H would follow from `Q-9506`, proving `nu_K -> infinity`.
The counterexample-first route is now equivalently `Q-9514`: find one positive
ordinary intrinsic height whose three forced valuation tests recur forever.

Iterations 02--10 establish the exact cylinders, ghost pressure, real-escape
and deficit budgets, prime firewall, large cycle exclusions, complexity
barriers, compiler no-gos, and quantitative macro constraints.  Iteration 11
reduces the renewal system to a finite type plus one ordinary quotient-refund
counter.  Iteration 12 removes the remaining trusted metadata: the single
integer `Z=(p-4)/4` recovers the full renewal type, bridge, next state, and
unique possible predecessor.

`X-9506` exhausts every ordinary candidate below `3*2^65`; `X-9507` supports the
proposed cycle exclusion beyond 2.47 billion blocks; `X-9508` and `X-9509`
audit the compiler and renewal-counter fronts; `X-9510` independently checks
the intrinsic decoder and predecessor on 746,496 finite states.

No positive counterexample has been found.  A valid final certificate now needs
only one written `Z_0>0` and an ordinary induction proving that the intrinsic
renewal map remains defined forever.  Such a certificate reconstructs the H
seed `n_0=4Z_0/3` and the shortcut-Collatz seed `8n_0+1`.

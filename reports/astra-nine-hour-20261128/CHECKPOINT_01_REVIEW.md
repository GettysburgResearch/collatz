# Checkpoint 01: scope of the mathematical review

This record concerns the initial packet on branch
`research/astra-nine-hour-20261128`, based on main
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`.
The publication record supplies its exact committed tree and head.
No verdict extends to an evolving `phase2` file or to an entire cited PR.

The coordinator reconstructed the deductions below from their displayed
hypotheses. **VERIFIED WITH SOURCE QUALIFICATIONS** means that the new
written deduction is checked with the specifically named analytic
results treated as imports. It does not mean those imported papers have
been fully formalized or independently re-proved in this pass.

## Actual sources and the critical clock

| Claim and path | Verdict | What was checked and what remains |
|---|---|---|
| `FINITE_CRITICAL_TAIL.md`, (1)–(6) | VERIFIED written finite theorem | Actual positive shortcut states, exact correction product, square-product bound on distinct integer states, integer critical clock, and strict contradiction. The result certifies some positive cycle; it does not distinguish the known cycle. Lean replay is a separate receipt. |
| `escape/CRITICAL_CORRECTION.md`, component/minimum law and critical correction law | VERIFIED WITH SOURCE QUALIFICATIONS | Minimum cells are differences of finitely many fixed predecessor basins; nested sub-basins can be pruned to disjoint ones. Fixed clock shifts disappear under the Gaussian scaling. Tight minimum laws allow finite-cell truncation before the limit. The correction after first minimum has a cycle slope or vanishes on a simple escaping future at this scale. |
| Same note, strict lower parity tails | VERIFIED WITH SOURCE QUALIFICATIONS | Recomputed the affine identity, normalizing constant and cycle tail transform. A nontrivial cycle has a correction slope strictly below the known cycle's slope; a simple escaping segment cannot enter the strict lower tail. The Gaussian saturation value is an unresolved arithmetic assertion. |
| `escape/UNIFORM_EARLY_ARRIVALS.md` | VERIFIED WITH SOURCE QUALIFICATIONS | Retained actual target and source octaves in the signed impulse expansion. In a fixed logarithmic source-width strip there are only boundedly many odd indices at a given total; the negative-binomial local bound sums uniformly over totals. Split impulses by physical height before applying the all-log-power tail. The positive periodic-site power sparsity used for moments is attributed to the prior packet. |
| `escape/TERMINAL_WINDOWS.md`, (1)–(4) | VERIFIED WITH SOURCE QUALIFICATIONS | Fresh sources at scale R² provide a label test containing a long remaining descent and small whole-prefix centered parity. The same actual first-landing law transfers this deterministic label test to original sources at X. R=exp(Kb), with K fixed before X tends to infinity, covers the terminal square-root-log window. No random stopping clock substitutes for the original deterministic clock. |
| Same note, fixed-logarithmic variance transition | VERIFIED WITH SOURCE QUALIFICATIONS | At multipliers at most μ, the actual prefix and minimum clock imply concentration. Above μ, a positive bad minimum has every future prefix odd fraction at least log(2)/log(10/3)>1/2. Two positive populations force nonvanishing variance. The value of the variance is not established above the transition. |
| `escape/POSITIVE_ONE_SITE.md` | VERIFIED countermodel within its stated map | Checked the explicit return word, ternary congruence for the good gate, exact parity run, positivity of the changed correction, and finite basin differences preserving fixed-target clocks. This is an altered map, not a Collatz counterexample. It prevents an inference from the listed bulk laws alone. |

For the source interfaces the coordinator read Weaver paper 179 v1,
Appendix A.8, and Wren paper 7 v3 directly, and read the pinned PR213
`linear/renewal_landing.md` and
`mass/SHARP_UNIFORM_FIRST_ARRIVAL_ROWS.md`. The latter two are at
`5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128`. The finite theorem uses
none of those population inputs.

## Complete returns and finite congruences

| Claim and path | Verdict | Review boundary |
|---|---|---|
| `cycles/MODULAR_QUOTIENTS.md`, Theorem 1 | VERIFIED written finite deduction | A compatible reduction of one whole least-period cycle has a shorter cyclic image. Its unique possible mixed-parity class forces one free calendar column. A common prime of modulus and full denominator is impossible at that class. The centered full-return carry is independent of the free bit and bounds the entire compatible modulus. |
| Same note, local packing and Theorem 2 | VERIFIED WITH SOURCE QUALIFICATIONS | Sliding a suffix by one block changes its odd count by at most the number of free columns. Compare every positive term of the full return, then apply a local dictionary at the actual minimum. Treated two-block and bounded projected periods separately. Only the conversion from minimum height to a polynomial in the period uses Lagarias's two-logarithm estimate. No existence of a compatible modulus is claimed. |
| `cycles/CONTRACTING_CALENDARS.md` | VERIFIED WITH SOURCE QUALIFICATIONS | Checked the two fixed-point inequalities, exact shared-tail spacing and strict complete-denominator inequality. The finite scalar range is independently enumerated; the long range invokes the stated logarithm bound. Earlier qualitative exclusions are credited. Straddling calendars remain admissible and the unrestricted case remains open. |
| `machinery/PROFINITE_ANCESTORS.md` | VERIFIED WITH SOURCE QUALIFICATIONS | Reconstructed the finite-fibre transitivity from the chronological word swap, the stationary ternary density, the bounded-density tail argument, and the finite-atom tail reduction. Kept fixed modulus, supplied ordinary target, and diverging overshoot separate. The auxiliary permutation-walk spectral estimate is not an ordinary conditioned rate. |
| `machinery/POINTWISE_CONGRUENCE.md` | VERIFIED written construction | Checked positive chronological inverse paths, exact common odd depth, ternary digit steering, congruence composition order, binary suffix, and positive transfer of a uniform row floor. The controlled event lies at the source end of the long inverse word. It does not compare a specified first inverse sibling's basin with the whole target basin. |
| `machinery/ARITHMETIC_PROGRESSION_FLOOR.md`, (1)–(5) | VERIFIED WITH SOURCE QUALIFICATIONS | Checked the mixed-conductor extension against the actual black-triangle geometry and stopped estimate, full-modulus numerator spacing, clock Parseval, and the selected-prefix pointwise transfer. Full composite divisibility peels into legal positive inverse steps, even at targets smaller than the real-offset bound. Distinct depths are disjoint for aperiodic targets; a bounded legal nonperiodic parent handles cyclic ones. The analytic imports and absolute constants are not Lean results. |

For the last row the coordinator opened Tao's Lemma 7.4, Weaver–Wren
paper 48 v2 equations (60), (65)–(79), and the abstract triangle scope
in paper 50. The mixed denominator Q enters both the maximum triangle
width and the full integer-spacing modulus. These losses are retained,
and Q is allowed only in the stated sufficiently small exponential
budget. The conclusion pays 1/a for the supplied target. At zero
overshoot on a hypothetical escaping ray this can be a vanishing
fraction of the actual row mass.

## Evidence levels

The finite controls enumerate literal positive rational cycles and
literal positive odd inverse paths, not just abstract residue words.
The C++ critical count has independent per-source even-run comparison
and a small literal Python comparison. Their bounded ranges are in the
receipts. Python optimized runs retain explicit scientific guards.

The Lean receipt records a fresh build of every included `.lean` file
and an all-declaration recursive axiom audit, including private
declarations. It is distinct from the written reviews above and from
the clean repository validator. No kernel verification is asserted
for a draft file or a module absent from a passing receipt.

**Global frontier remains open.** The checkpoint does not prove the
critical Gaussian saturation, force a low-denominator successor
polynomial on all true cycles, exclude arbitrary nontrivial cycles, or
remove the original-grade atom on one escaping ordinary ray.

# Ordinary weighted spectrum and finite linear complexity

The finite theorem and the ordinary excursion were checked by Lean 4.34.1, mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`. The weighted analytic results are proposed mathematical proofs with the primary inputs cited in their notes. Universal Collatz convergence remains open.

| File | Scope |
| --- | --- |
| [FINITE_RANK.md](FINITE_RANK.md) | Every nonzero rational dyadic-eigenvector prefix through N has recurrence order strictly greater than (N+2)/4. Includes the exact finite-height range obstructed by the ordinary all-odd excursion. |
| [HeckeRank.lean](HeckeRank.lean) | Proves global recurrence rigidity and the finite inequality for every nonzero integer annihilator, covering rational recurrences by clearing their coefficients' denominators. |
| [FiniteTrace.lean](FiniteTrace.lean) | Proves the excursion and its cutoff obstruction directly from ordinary integer iteration. |
| [CutoffRank.lean](CutoffRank.lean) | Combines the proofs for any supplied finite array with explicit support and doubling hypotheses, and prints the axiom inventories. |
| [ORDINARY_SPECTRUM.md](ORDINARY_SPECTRUM.md) | Defines the stabilized, component-calibrated rational mass. For any nonempty collection of components disjoint from 1, its squared-slope power series has a singular set containing a nonempty perfect subset. Almost every positive exponent gives a full natural boundary. |
| [BASIN_BLOCK_BOUNDARY.md](BASIN_BLOCK_BOUNDARY.md) | Long intervals routed into the ordinary basins of 1 and 85 strengthen the weighted result to a full natural boundary for every positive exponent, including 2. |
| [CLOCK_SPECTRUM.md](CLOCK_SPECTRUM.md) | Independent arithmetic obstruction from Bell–Gunn–Nguyen–Saunders and Inselmann. An analytic arc would force superpolynomial same-component clocks, and the block theorem separately rules out such an arc. |
| [FIVE_SOURCE.md](FIVE_SOURCE.md) | On the actual inverse tree of 5, a single monomial in the odd section equation suffices for the same weighted singular-spectrum consequences. |
| [finite_controls.py](finite_controls.py), [FINITE_CONTROLS.json](FINITE_CONTROLS.json) | Computes exact finite graph weights and recurrence orders, checks the support against individual ordinary forward trajectories, and records the comparison. |

From this directory, run `python3 verify.py --lean /path/to/lean --mathlib /path/to/mathlib4` with the indicated pinned checkout and mathlib's dependency packages present. The replay first checks the saved finite arithmetic, compiles missing mathlib dependencies into a disposable overlay, rebuilds the three modules with warnings as errors, and checks that all five printed inventories use only Lean's standard axioms. It needs Python 3 and GNU coreutils `cp`. For an already complete mathlib cache, only the three project sources need compiling.

The formal statements do not include the infinite-component construction or the analytic spectrum theorems. The support hypothesis in the cutoff consumer is proved for the finite graph in the written argument and checked independently on all supplied control heights.

# Arithmetic verification

The source packet proves that augmented common-clock merger classes on a fixed positive tower are finite. For a fixed nonperiodic reference, even ordinary mergers at bounded clock difference admit only finitely many exponents of any fixed positive tower. A separate argument gives infinitely many exponents without any certificate to the full lower cone when each of the two arms has a bounded number of powered words drawn from a fixed finite bank. [Class and two-arm proofs](../../../../research/astra-global-closure-20261124/round12/arithmetic/README.md) · [Bounded clock difference and explicit odd reciprocal bound](../../../../research/astra-global-closure-20261124/round12/arithmetic/HIGH_GATE.md)

## Lean

The ordinary dynamics and count are imported from the round-10 SmoothCore dependency stack. The checker was Lean 4.34.1 at compiler commit 5045d005 with mathlib d13f23b723b8a846827a245b89c10fc7d3f11612, with warnings treated as errors. The ten printed declarations use only propext and Quot.sound, or a subset of those. They cover equivalence and doubling, the necessary first-tower minimum, the common-lag fiber argument, synchronization of visits to a nonrepeating state, the invariant for actual designated periodic phases, the exact ordinary stopping-score criterion, and its numerical ceiling. [Lean module](../../../../research/astra-global-closure-20261124/round12/arithmetic/AugmentedMerger.lean) · [Compiler output](lean.log)

The real estimates for simple paths, the full class finiteness argument and the unit-equation deduction are written mathematics. The explicit high-path gate uses a Python finite arithmetic check. The inference that every hypothetical nonperiodic orbit avoids that gate uses Bařina's published verification through $2^{71}$.

## Integer checks

Normal and optimized Python runs passed the same explicit checks and produced byte-identical JSON. The Python run first evaluated the exact binomial inequality for the odd reciprocal mass above $2^{64}$. Its rational upper bound rounded upwards to six decimal places is 2.836949. A separate calculation building all binomial rows by Pascal addition gave the same rounded bound. Its reduced denominator is $2^{1995}$. The SHA-256 of the decimal numerator is 0f6a06bca198efd6f61b45fdc2036e5cf1084ab04119903bef43103e8ff3736f. [Checker](../../../../research/astra-global-closure-20261124/round12/arithmetic/check.py) · [Exact-comparison output](finite.json)

For each sample below, the first computation takes actual first-hit counts at 1, then groups by $2(r+P)-h$. A second computation starts again from each positive integer, advances every orbit through the sample's largest first-hit clock, and groups by the actual endpoint and total augmented count. The two partitions agree exactly. Since every sampled start has an actual hit and (5) is an equivalence, class counts mean the number of distinct full classes represented in each finite sample.

| Base | Exponents included | Common comparison clock | Represented classes | Largest membership in sample |
| --- | --- | ---: | ---: | ---: |
| 1 | 0 through 1024 | 8120 | 56 | 115 |
| 5 | 0 through 256 | 2277 | 38 | 43 |
| 10 | 0 through 256 | 2278 | 38 | 43 |

The needed pointwise existence of an unrestricted ordinary merger for a first tower failure remains open.

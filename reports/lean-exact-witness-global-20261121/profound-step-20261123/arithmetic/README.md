# Adaptive and changing-anchor lattice: execution boundary

**Full Collatz, unrestricted positive-cycle exclusion, and the original residue-512 implication remain open.**

The [scientific note](../../../../research/lean-exact-witness-global-20261121/profound-step-20261123/arithmetic/ADAPTIVE_LATTICE_DESCENT.md)
proves strict integer descent from each actual source repetition lattice,
without a common cutoff or a target-lattice assumption. Its changing-anchor
extension charges the full cross-carry and uses one Nat-valued rank even
when the base word, rational fixed point and complete denominator all vary.
The unresolved step is a universal paid factorization of actual orbits.

## Actual formal evidence

`AdaptiveLattice.lean` imports the unchanged `LatticeDescent.lean` source
from the prior pinned checkpoint. Its **13 new public declarations** include
literal ordinary-word consumers for the fixed and changing anchor results.
The dependency's 20 declarations are not counted as new. Both sources were
compiled with Lean 4.34.1, one worker and warnings treated as errors. The
axiom audit contains only `propext`, `Classical.choice`, `Quot.sound`.
There is no `sorryAx`, new research axiom, or external analytic axiom.

The full commands, exact source hashes and observed results are in
[EXECUTION.json](EXECUTION.json). The dependency object is built outside
the checkout and supplied through `LEAN_PATH`; no generated Lean object
is part of the publication. The explicit real cutoff for arbitrary defect
lengths and the prose cycle interpretation remain written deductions.

## Finite controls

The independent literal simulator checks **7,440 actual ordinary macros**,
**84,280 literal macro steps**, **4,702 certified nonzero fixed-anchor
strict decreases**, including **532 expanding-base instances**, and
**29,760 actual next-window anchor changes**, of which **20,534** pass the
complete changing-anchor strict criterion. One hundred exact rational
cutoff inequalities check the stated closed formula.

Five controls retain the strict complete-carry condition, first-hit versus
zero-absorption distinction, ordinary integrality, source-lattice premise,
and full anchor-reset cost. The 1→2→1 cycle and the actual 5→8→4 trace
are explicit counterexamples to omitted terms or unpaid rank resets.
The normal and optimized Python outputs are byte-identical. These finite
controls do not establish the infinite theorem by census.

## Sources and attribution

[SOURCES.json](SOURCES.json) distinguishes exact imported proofs, the latest
PR178 source inspection, and primary-literature orientation. The older
k=2B cutoff calculation is credited. The new points are using each source's
own lattice to obtain first hit, then paying changes of rational center
with a complete cross-carry. No new literature-priority claim is made.
The primary termination descriptions supplied methodological guidance;
their full theorem hypotheses are not asserted to hold for Collatz.

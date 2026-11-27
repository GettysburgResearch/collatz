# Fifth checkpoint execution evidence

This archive records source-frozen finite checks and clean repository
validation. It is not a proof of Collatz.

- Local validated science commit: `6d606e8a7717167179d42920af731bb09d42417b`.
- Published science commit: `40820cc9701c880abd9fcd37c412985763b3f5b7`.
- Identical science tree: `b22f3126bd7387a8f056bc1b0b4b967b0cdbbc76`.
- Science parent: `594053764b988ad735778b48e336f858a8098cd7`.

The source manifest identifies all 20 changed production files by mode,
Git blob, byte count, and SHA-256. Receipts are committed separately.

## What passed

`LEAN_REPLAY.json` freshly compiled `DimerMass`, `FiniteTrace`, and
`DyadicClock`. `SIGNED_ORIGIN_REPLAY.json` independently rebuilt
`RampShadow`, `PostWords`, and `SignedOrigins`. These are six distinct
modules in this checkpoint and three new ones, bringing the cumulative
freshly rebuilt set to 49. Both runs used Lean 4.34.1 and Mathlib source
`d13f23b723b8a846827a245b89c10fc7d3f11612`, fresh local output directories,
one worker, no automatic implicit variables, synchronous elaboration,
and warnings as errors. Every printed inventory is a subset of
`propext`, `Classical.choice`, and `Quot.sound`; hashes remained unchanged.

The finite declarations cover dimer coefficient and reciprocal-tail
arithmetic, physical and adjacent-clock transport for valuation-at-least-two
inverse words, and the complete mirror-origin table through seven even
steps at unrestricted signed clock. They do not formalize the written
Subspace Theorem consequences, pressure asymptotics, or stopped-tree
measure bounds.

`FINITE_REPLAY.json` records four programs in normal and optimized Python,
all passing with identical outputs and unchanged source and fixture
hashes. The programs check the avoidance budgets and native inverse
counts, canonical-cut divisor controls, finite ternary pressure
cancellations, and the strengthened common protection fractions. All
substantive checks survive optimized mode. Across five checkpoints,
28 programs have been replayed in both modes.

Both clean-checkout repository validations passed all eleven commands,
first at the local science commit and then at the published commit with
the identical tree. The root checked every source hash again before the
science commit.

## Mathematical review and scope

The root reconstructed the written cycle budgets, interval induction,
canonical divisor counting, pressure correction, and common protection
argument. The rigidity lane independently reviewed the cycle arguments.
The numerical cycle floors use the explicitly cited published `2^71`
verification, which this sprint did not rebuild. The cycle-height
corollaries retain their named external two-log input.

The surviving sets may still contain a sparse exceptional orbit, and a
small total cycle defect may contain a cycle. Common protection excludes
visitors only through its stated odd-step budget. A counted predecessor
family does not determine its target's future.

See [FIFTH_CHECKPOINT.md](../../../research/astra-reciprocal-rigidity-20261127/FIFTH_CHECKPOINT.md)
for theorem statements and the first unsupported step toward Collatz.

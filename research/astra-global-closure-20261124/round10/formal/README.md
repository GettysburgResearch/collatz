# What the final Lean assembly checks

**The universal conclusion still has an OPEN premise.**
[FinalProposal.lean](FinalProposal.lean) imports the byte-identical PR192
`SmoothCore` theorem and the new ordinary tower module. It checks the
following distinct assertions.

1. Every finite shortcut run from a positive natural number is positive.
2. An ordinary tuple satisfying the two run identities and
   `2 * 3^(m+r) ≤ 2^(m+e)` cannot be a `FirstTower w r`. The actual
   endpoint is a positive base below `w`, which is good by the minimum
   hypothesis. This is an unconditional exclusion theorem about those
   tuples, rather than an assumed convergence result for their endpoints.
3. Every tuple in the displayed `H` family of the tower packet is excluded
   by that theorem, for every natural `H`. Infinitely many positive tuples
   for each positive `H` are constructed in the written CRT argument.
4. Every prefix through clock `r` on a hypothetical `FirstTower w r` has
   maximal odd count in its length-and-constant fiber. A heavier word would
   be legal at an earlier ordinary power of the same base.
5. `final_proposal` consumes `open_merger : FrontierMerger` to conclude
   `∀ n, 0 < n → Good n`. This is the existing PR192 consumer and retains
   exactly its existing open mathematical premise. It is not a new proof
   of that premise.

`Good n` means that an actual finite shortcut iterate of the natural number
`n` equals 1. `FirstTower` is the least positive base supporting a bad
power of three, followed by the first bad exponent over that base. Its
existence under failure and its minimum consequences come from the pinned
dependency. No alternative basin, rational cycle or two-adic completion is
substituted for these ordinary definitions.

## Other checked modules

`TowerClock` proves full finite word semantics, rigidity and construction
of short meetings, the all-odd smooth-cone exclusion, the all-time 15/5
countercontrol and the actual two-run descent. `ClockBlocks` checks finite
concatenation, disjoint counting banks, a bounded-offset composition and
clock-balance algebra. `RankGaps` checks the lifted recurrence, the common
word propagation and the full coprime product forcing its middle difference
to vanish. The source floor F, probabilistic concentration, asymptotic
entropy count and full all-shift theorem are written mathematics.

## Replay

With Lean 4.34.1 and Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`, run from the repository root:

```sh
python -B research/astra-global-closure-20261124/round10/check_lean.py \
  --lean /absolute/path/to/lean \
  --mathlib /absolute/path/to/mathlib4 \
  --report-dir /absolute/path/to/reports
```

The runner rebuilds seven project modules in a fresh temporary project
cache, verifies the three pinned source hashes, treats warnings as errors,
and checks the selected transitive axiom outputs against the standard
three-axiom allowlist. It reuses recorded Mathlib/package oleans. It does not
rebuild Lean or Mathlib, and an axiom audit cannot discharge an explicit
theorem hypothesis. The final receipt records 65 selected inventories,
including 28 from the four new modules.

[Dependency provenance](../vendor/SOURCES.json) ·
[Root execution receipt](../../../../reports/astra-global-closure-20261124/round10/lean/receipt.json) ·
[Independent scope review](../../../../reports/astra-global-closure-20261124/round10/arithmetic/REVIEW_FINAL.md)

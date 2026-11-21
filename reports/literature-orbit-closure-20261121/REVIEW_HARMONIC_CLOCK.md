# Focused semantic review: atomic transport and actual marked fibers

Reviewer: `literature_operator`, 21 November 2026.

This is a source-level mathematical review of the new statements and their
proof architecture. It is not an independently executed build receipt. The
reviewer developed `FiniteResolvent.lean`, so this review makes no claim of
independence for that module.

## Scope and exact source snapshots

The inspected files are in
`research/literature-orbit-closure-20261121/lean/`:

| File | SHA-256 |
| --- | --- |
| HarmonicTransport.lean | 5173ef8676b4b8de03ccae9f1e99bb3db04e52d146ba721034b325f6fd4bc1f7 |
| ClockAbsorption.lean | 08889797b1142f8186e4def059e08a800993fc52d1b22489e939652329e23b14 |
| BandAbsorption.lean | df279eb937e14f56277c0ac73e8861ceabfe45d8e126ee2669962f00283dbb43 |
| ActualSurvivorMass.lean | 5c4e9c0ecd6c35edac3eb8f5f1262e70da06e534234678cf7ed30eec2e0fe178 |

## Findings

1. `FiniteMass` bounds sums over arbitrary finite subsets. The orbit-image
   argument uses injectivity on precisely the finite clock interval being
   charged, so it neither counts repeated ordinary points as distinct nor
   substitutes an almost-everywhere statement for an original atom.
2. The reciprocal theorem keeps the exact divergence hypothesis visible.
   The dyadic linear certificate uses `2^J` points and proves
   `J*a <= 2*C*W`; the slightly different `2^J-1` presentation in the
   companion prose is also valid but is not this Lean statement.
3. `ColumnBound` has the correct direction: all finite source fibers over
   one endpoint are bounded by the endpoint weight times the multiplier.
   A singleton fiber retains the original source's mass.
4. The clock lift makes every path avoiding one injective, even when the
   underlying ordinary map has a cycle. Thus the absorption theorems do
   not silently discard the possible nontrivial-cycle case.
5. `BandAbsorption` composes the generic result with actual iterates of
   PR173's return map and actual ordinary orbit hits. Its positivity
   premise concerns marked inputs; zero is not smuggled into the domain.
6. `ActualSurvivorMass` defines the incoming fiber by finite source sums
   and their bounded supremum. The finite-mass hypothesis provides the
   upper bound needed for that supremum. A surviving source is retained
   in the singleton sum with its original weight.
7. The quadratic extraction holds at each fixed original source and each
   finite surviving return depth. It does not require the ordinary
   endpoints to be distinct: the separate depth weights encode the
   clock. A single counterexample therefore supplies the same positive
   atom at every depth, making a vanishing subsequence of relative
   transport budgets sufficient for contradiction.

## Remaining obligation and failed strengthening

The universal closing conclusions explicitly assume transport bounds and
their critical or subsequential improvement. No such improvement is proved
in these inspected files. These are sufficient closing tests, not a proof
that a fixed size-based weight satisfies them.

In particular, the clock-lifted shift `n -> max(n-1,0)` with polynomial
spatial seed and geometric clock seed has quadratic resolvent norm growth
although every source terminates. The companion proof and finite Lean
fiber theorem preserve this countermodel. Any assertion that termination
alone automatically gives a subquadratic bound for this fixed seed would
be false. No corresponding refutation for the actual Collatz marked
return map was obtained in this pass.

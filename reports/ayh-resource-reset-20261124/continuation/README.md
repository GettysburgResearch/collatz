# Continuation evidence and review boundaries

This record accompanies [the third research checkpoint](../../../research/ayh-resource-reset-20261124/continuation/README.md). It extends PR 197 from the frozen parent 2fb1f11c959e35eba875338833d84969222dc089. Universal Collatz convergence remains open.

## Fresh Lean execution

The parent ran the continuation driver with Lean 4.34.1 and Mathlib d13f23b723b8a846827a245b89c10fc7d3f11612. The driver creates an empty temporary output directory, rebuilds six supporting modules, builds all seven new modules sequentially, and removes the temporary outputs afterward. The command completed successfully with one worker, implicit variable creation disabled and warnings treated as errors.

The 20 distinct new public theorem declarations all have transitive axiom dependencies contained in propext, Classical.choice and Quot.sound. Supporting modules print additional older declarations, which are not included in the new count. The fixed-base and 81-child computations use kernel reduction; they do not introduce a computational oracle axiom.

| New file | New public declarations | Checked scope |
|---|---:|---|
| TernaryHeadDescent.lean | 6 | Ten-clock head or finite base; exact growth and contraction; low base; universal truncation equivalence |
| WholeTernaryFiber.lean | 1 | Every member of an infinite progression has all 81 children at its same 172-clock endpoint |
| CriticalCompression.lean | 1 | Arithmetic transport to a smaller critical source from supplied ordinary endpoint mergers |
| BasinCounting.lean | 4 | Lift residue, physical remaining clocks, finite target multiplicity and deletion witness |
| TernaryStopping.lean | 2 | Exact all-odd block and universal mesh criterion |
| InverseWordCover.lean | 3 | Arbitrary-input inverse cover, within-word prefix cost and physical single-link clock |
| HeadEdgeTransport.lean | 3 | Real-floor truncation, actual halving on exact subcells, and generic local ergodic return rigidity |

[Compiler output](lean-build.log) · [Execution metadata](lean-execution.json).

The phase asymptotics, complete infinite inverse concatenation, probability estimates, critical and growing-head ancestor exponents, and new analytic edge-rigidity theorem remain written mathematics. They are not included in the formal theorem count.

## Exact controls actually run

Four scripts ran once normally and once with Python optimization. All eight runs exited zero, with identical output in each pair. Guards raise explicitly and remain active with optimization.

The critical compression replay samples 4,096 inputs in 32 exact fibers. It replays 442 actual smaller critical mergers with the original surplus. The remaining outcomes are 67 even-step deadlines, 64 lower-edge rejections and 3,523 pair deadlines. These are finite-budget outcomes, not counterexamples to eventual meeting or to an asymptotic estimate with unspecified constants.

The inverse-word replay covers all 162 unit residues modulo 243 and 16,238 ordinary inverse links in concatenated paths. An independently written checker covers the twelve full ternary cylinders and their internal prefix costs. The first-return replay checks three complete ordinary paths at source binary exponents 104, 610 and 1328, with their first critical returns strictly above the stated power of the original source.

[Exact commands, output, timing and source hashes](finite-checks.json).

## Mathematical review

- [Ternary-head review](HEAD_REVIEW.md): independent reconstruction of the integer cover, original-source contraction, seed lifting and growing-head conditioning. The inherited PR 146 absorption estimate remains a written dependency.
- [Critical-compression review](CRITICAL_REVIEW.md): independent reconstruction of the residue correction, stopping-cell counts, octave edge, mark and surplus. It identifies the exact-cofactor scope of the formal statement.
- [Basin-counting review](BASIN_COUNTING_REVIEW.md): fixed-target preservation, uniform phase margins, target multiplicity, improved inverse policy and final growing-head image. The policy's contributor and the counting author cross-checked different parts; the review explicitly identifies that collaboration.
- [Edge-rigidity review](EDGE_RIGIDITY_REVIEW.md): independent reconstruction of the quantitative limit, exact doubling subcells, proper-arc rigidity and cumulative ordinary counting contradiction.
- [Parent review](ROOT_REVIEW.md): reconstruction of the integrated claims and the ordinary-source, clock and transport boundaries.

Each review pins the version it inspected. The source manifest covers the final files and includes upstream source identities. A review of one file is not approval of neighboring files or a later source version.

## Published-head integrity

The required complete-checkout integrity gate is run on the final published commit with its receipt outside the checkout. PR 197 records that exact head, tree, exit code and receipt hash after readback. Earlier receipts retained in the parent report apply to their original commits. The five default checks inspect repository integrity and frozen identities; they do not prove the new mathematics. The optional historical regression bundle is not part of this checkpoint.

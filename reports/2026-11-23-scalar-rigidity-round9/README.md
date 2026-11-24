# Round nine: execution, independent review, and publication evidence

23 November 2026. Published parent:
`6352608dd6c04735e1f8bd86fef4ebc97b1aeacb`.

The scientific entry point is the
[actual carry and scalar rigidity packet](../../research/scalar-rigidity-round9-20261123/README.md).
This report records evidence levels separately. **Collatz and the
universal scalar-arithmetic construction remain unresolved.**

## Fresh Lean compilation and dependency audit

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records four successful
commands: three new source modules and
[RoundNineAudit.lean](RoundNineAudit.lean). They compiled into a newly
empty output directory under Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.

The compiler archive's official release digest was verified in the
parent receipt; this run additionally binds the compiler binary's
SHA256. Existing pinned Mathlib objects were reused. No old
repository module or old output of a new module was imported.

Every command uses one thread, warnings as errors, and
`autoImplicit=false`. All **30 new theorems and nine definitions**
are audited. Their only observed axioms are `propext`,
`Classical.choice`, and `Quot.sound`. No admitted proof or custom
axiom appears in their audited dependencies.

| Module | Theorems | Definitions | Exact formal scope |
| --- | ---: | ---: | --- |
| ArithmeticRigidity | 7 | 2 | Finite scalar blocks, arbitrary binary block concatenation, tail differences, coupled-coordinate cancellation |
| CarryReturn | 18 | 7 | Complete normalized physical equation, unbounded positive-carry comparison, arbitrary finite affine paths, return envelopes, descent thresholds, full clock telescope |
| MaximumGate | 5 | 0 | Complete rational coefficient identity, monotone clock bounds, exact seven-pair obstruction, necessary valuation exponent |

The real series, full ordinary attachment, first-return existence,
CRT existence, distribution and measure-type theorems, and modular
group arguments remain written mathematics. The Lean scope is not
described as full formalization of those results.

## Exact finite execution

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) records the normal and
optimized runs of all four lanes. The two outputs,
[EXACT_CONTROLS.json](EXACT_CONTROLS.json) and
[EXACT_CONTROLS_OPTIMIZED.json](EXACT_CONTROLS_OPTIMIZED.json), are
byte-identical: 37,442 bytes, SHA256
`2e34eb481b94e71e0df56ed0715340c7daa779b7e3be5cd998b990a66c0a7251`.
All 15 scientific files are bound by SHA256 before and after. An AST
scan of all five Python files found zero Assert nodes.

| Lane | Executed domain | Explicit checks |
| --- | --- | ---: |
| Actual source law | 17,576 finite gap words; 52,728 cylinder-lift replays; 13,200 fixed-length actual prefix replays; exact tail sums through depth 128 | 490,569 |
| Arithmetic construction | 490 target/congruence approximations; 130 binary carry words; 6,384 literal actual odd transitions | 26,856 |
| Ordinary carry return | 25 paid-excursion families, carries through 2,460, sources through 7,393 bits; 325 low-prefix combinations; 16,384 candidate sources; 400 supplied rational reductions; 24 completed actual-scalar transport examples | 27,741 |
| Complete denominator rigidity | 107 cap-violating denominators and 430 full phases; 34 binary boundary phases; 923 doubling identities; 1,152 first-departure gates; 62 positive ordinary cylinders; five exact prime thresholds | 14,768 |

The total is **559,934 explicit checks per execution**. The domains
overlap. This is not a count of distinct ordinary sources or of
proved universal theorems. The literal prefixes in the law,
arithmetic, and phase lanes use unconditional scalar tail bounds;
they do not assume termination. The carry lane separately finishes
selected small trajectories only for its 24 exact scalar transport
controls. It does not assert actual scalar equality at 7/8 for its
symbolic closed candidate paths.

## Independent mathematical reconstruction

- [LAW_REVIEW.md](LAW_REVIEW.md) independently reconstructs R9-L1--L5,
  including exact cylinder legality, all terms of the finite law
  bound, Fourier nondecay, pure singularity, atomlessness, and the
  unbounded closed-grid density implication.
- [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md) reconstructs R9-A1--A4,
  both actual approximation constants, the radical-coordinate
  cancellation, and directly inspected primary-literature
  hypotheses. It also records an independent exhaustive replay of
  2,954 odd residues for 39 complete words and 75 approximation
  boundary cases. The final formal-series clarification is pinned.
- [PHASE_REVIEW.md](PHASE_REVIEW.md) reconstructs R9-P1--P6, including
  complete composite fibers, the binary boundary, support caps,
  doubling defects, sharp low families, first-carry valuation gate,
  and the prime-only Gauss-sum normalization.
- [MAXIMUM_REVIEW.md](MAXIMUM_REVIEW.md) reconstructs R9-M1 at the
  same pressure maximum, retains the no-ternary-factor premise,
  and checks its complete prefix and exact integer obstruction.
- [ROOT_REVIEW.md](ROOT_REVIEW.md) independently reconstructs the
  carry lane and its total local interfaces, checks the phase and
  arithmetic lanes, and records fresh root execution. It does not
  claim independent authorship of root's own law or maximum proof.

Each review fixes exact scientific blobs. It does not approve
neighboring branches or a later changed proof. Primary-source and
ordinary-realization boundaries remain next to their claims.
[HANDOFF.md](HANDOFF.md) records the remaining construction tasks.

## Complete checkout and publication boundary

[PR182_BEFORE.json](PR182_BEFORE.json) preserves the prior PR title,
body, head and base. The source branch was freshly read at the stated
parent before publication.

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the copied
five-command repository-integrity receipt from the clean complete
local science checkout. Its named commit and tree are the actual
input to that gate. It predates only the addition of the copied
receipt and [SOURCE_BINDING.json](SOURCE_BINDING.json), so neither
file pretends to contain its own eventual commit SHA.

The binding records every file in the science tree, preserves all
617 parent files unchanged, and separately binds all earlier Lean
files. Publication constructs a single commit on the expected
published parent, compares its tree to the complete local tree,
and advances the branch without force. The result is fetched and
validated in another clean complete checkout. The published-checkout
receipt and fresh remote head/PR readbacks are recorded in the PR,
outside this noncircular in-tree evidence chain. The local science
and receipt commits remain on a checkpoint branch.

Repository-integrity success is evidence about the checkout and
frozen records. It does not establish the mathematical claims or
remove the global carry-control obstruction.

# Round-six review, execution, and source identity

23 November 2026. Parent:
`afe6f4d1a661b377c9daa4623bdd732ba478386b`.

The [scientific entry point](../../research/profound-round6-20261123/README.md)
contains the statements and proofs. **Full Collatz remains open.** This
report records the narrower evidence: independent reconstruction, fresh
Lean execution, exact bounded arithmetic, and clean-checkout integrity.

## Fresh Lean execution

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records six successful compilation
commands into a previously absent output directory, with that directory
first in `LEAN_PATH`. They compile, in dependency order:

1. `CycleWordAlgebra.lean`, the unchanged earlier chronological module;
2. `CycleCancellation.lean`, its unchanged numerical cancellation consumer;
3. the new `RationalSelection.lean`;
4. the new `CycleArithmetic.lean`;
5. the new `CollisionClosure.lean`;
6. [RoundSixAudit.lean](RoundSixAudit.lean), which prints axioms for every
   new public theorem.

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
All commands use `-j1 -DwarningAsError=true -DautoImplicit=false`.
The 17 audited public declarations use only `propext`, `Classical.choice`,
and `Quot.sound`. No `sorryAx` is present.

Existing Mathlib objects were reused. The two repository dependencies
were recompiled; the whole older authored corpus was not. All 47 earlier
tracked Lean files are separately hash-bound as unchanged in
[SOURCE_BINDING.json](SOURCE_BINDING.json).

The formal claims are chronological polynomial noncancellation, finite
positive-cycle arithmetic, and complete finite collision packing. The
irreducibility argument, local pole/radius theorem, multipoint rationality,
total-variation analysis, and stationary limits remain written mathematics.

To reproduce, obtain the pinned compiler and Mathlib, put the compiler
on `PATH`, get Mathlib's `LEAN_PATH` via `lake env printenv LEAN_PATH`,
prepend a fresh directory, and run the receipt's source order with fresh
`-o` targets. The receipt includes the exact absolute commands from this
execution and the SHA-256 of every compiled source.

## Exact finite execution

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) records both executions of
`research/profound-round6-20261123/exact_replay.py`, normally and under
`python -O`. Both exited zero. Their full JSON outputs are
[EXACT_CONTROLS.json](EXACT_CONTROLS.json) and
[EXACT_CONTROLS_OPTIMIZED.json](EXACT_CONTROLS_OPTIMIZED.json), and are
byte-identical. An AST inspection found no `assert` statement in the two
Python source files; all mathematical guards explicitly raise on failure.

| Bounded check | Executed coverage |
|---|---:|
| Primitive positive rational cycle words, lengths 1--10 | 1,578 |
| Literal rational shortcut steps, with actual parity and return | 14,338 |
| Positive nonzero numerator remainders modulo the reduced-clock factor | 1,578 |
| Reduced-denominator prime instances | 1,269 |
| Instances seen in the first 12 Taylor coefficients | 1,269 |
| Prime instances absent at the constant coefficient and seen later | 82 |
| Words with the entire reduced-clock value cancelled at the constant | 75 |
| Ordinary convergent sources used for the germ controls | 131 |
| Literal ordinary shortcut steps in those controls | 3,829 |
| Independent coefficient comparisons, 32 per source | 4,192 |
| Coefficients checked against one common prefix denominator `3^s` | 4,192 |
| Ordinary sources used for collision controls | 68 |
| Distinct actual odd-state prefixes | 190 |
| Actual source/modulus cases | 2,071 |
| Complete ordered collision pairs | 409,264 |
| Off-diagonal pairs retained | 390,638 |
| Exact below-modulus diagonal cases | 689 |
| Exact rational-probability comparisons | 6,184 |

The cycle census includes rotations separately. It concerns rational
odd-denominator cycles; the only primitive ordinary integer cycle words
found within this finite range are `01` and `10`. No all-period conclusion
is drawn from that observation.

The `110000` fixture is the rational cycle starting at `1/11`. Its full
denominator is 55, its carry is 5, and its reduced value denominator is
11. The exact derivative is `181/605`. The replay checks
`v_5(den(c_j))=j` for `1<=j<=31`; the separate written induction is in
[EXACT_CONTROLS.md](../../research/profound-round6-20261123/EXACT_CONTROLS.md).

The ordinary-source coefficients were obtained independently from reverse
shortcut recurrences and direct translation of the prefix plus standard
tail. The actual collision controls compare explicit ordered pairs with
squared bucket counts, retain the complete quotient, and check the
total-variation inequality through exact rational squaring. Their finite
reference vectors are not claimed stationary laws of those sources.

## Independent review and pinned inputs

[JET_REVIEW.md](JET_REVIEW.md), by the collision lane, independently
reconstructs the cycle-prime theorem and the conditional J3 consumer.
It verifies the actual ordinary source, arbitrary prefix, irreducible
factor, every conjugate pole, valuation rate, exceptional standard cycle,
common-denominator converse, and the primary theorem's hypotheses.

[COLLISION_REVIEW.md](COLLISION_REVIEW.md), by the rational-selection lane,
independently reconstructs finite packing, the total-variation factor,
strict growing-scale exponents, optimized conditional rate, and the
finite-flow transfer. It keeps the source, limiting law, and subsequence
fixed. Neither review required a mathematical correction to the frozen
science files.

[ROOT_REVIEW.md](ROOT_REVIEW.md) records the integrating root's separate
reconstruction and execution boundary. Reviews bind exact Git blobs;
the source binding binds the complete science/report bytes. The latest
selected upstream heads and primary literature inspection boundaries are
in [SOURCES.json](../../research/profound-round6-20261123/SOURCES.json).
The previous PR182 title, body, branch, and base are preserved in
[PR182_BEFORE.json](PR182_BEFORE.json).

## Complete-checkout gate and publication boundary

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the copied
successful gate receipt for the clean local science commit before the
final source-binding and gate-receipt files were added. It runs the five
default commands of `python -X utf8 -B tools/validate.py`, including the
integrity and portability self-tests. The receipt names its own exact
commit and tree; it is not presented as a receipt for a different commit.

[SOURCE_BINDING.json](SOURCE_BINDING.json) connects that validated science
tree to every new science, review, and execution file and records all
earlier tracked Lean hashes. All parent files remain unchanged. This
binding and the copied validation receipt are the only subsequent local
receipt additions.

The published commit is created with the unchanged remote parent and a
single tree containing this packet, then read back from GitHub. A fresh,
complete detached checkout of that exact published commit receives the
same five-command gate and a source-binding check. That final external
receipt and exact head are recorded in PR182 after publication, avoiding
a circular claim that a receipt contains its own final commit identity.
The local science/receipt chain is retained under a checkpoint branch.

Repository integrity is not mathematical verification. The unresolved
inputs remain construction of J3 and limiting density for every ordinary
source, or an independently proved source condition that replaces them;
the collision and pressure transfers also retain their explicit gaps.

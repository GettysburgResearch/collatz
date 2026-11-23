# Round-seven proof review, execution, and publication record

23 November 2026. Parent:
`e4367dd2c4406c1041e66d82dfba822908747fa3`.

The [scientific packet](../../research/closure-round7-20261123/README.md)
contains the new statements, proofs, and first unsupported global steps.
**Full Collatz remains open.** This report separates written review,
formal arithmetic, exact finite execution, and repository integrity.

## Fresh Lean execution

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records two successful fresh
compilation commands: `GermConstruction.lean` and
[RoundSevenAudit.lean](RoundSevenAudit.lean). The new module imports
Mathlib only; it has no older repository-module dependency. Its output
directory was absent before the build and first in `LEAN_PATH`.

Compiler: Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
Both commands use `-j1 -DwarningAsError=true -DautoImplicit=false`.

All seven public theorems were audited. Their observed axiom union is
`propext`, `Classical.choice`, and `Quot.sound`; no `sorryAx` occurs.
The statements prove binary-integral rational arithmetic, triangular
integer clearing under the actual coefficient equations, and finite-jet
membership equivalence over rational subrings containing one half and
one third. Rational coefficients and the actual equations are inputs.

The analytic definition of the actual coefficients, their arbitrary-source
rationality, the exact denominator-valuation equality, the resultant
bound, the Hensel family, ordinary-shadow construction, and asymptotic
probability results are not claimed as Lean theorems here. Existing
Mathlib objects were reused. All 51 parent tracked Lean files are checked
unchanged; they were not all rebuilt.

## Exact bounded execution

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) binds ten scientific input files
and both successful executions of `exact_replay.py`, normally and under
`python -O`. The full outputs are [EXACT_CONTROLS.json](EXACT_CONTROLS.json)
and [EXACT_CONTROLS_OPTIMIZED.json](EXACT_CONTROLS_OPTIMIZED.json).
They are byte-identical. An AST scan of all five Python sources found
zero `assert` statements; mathematical checks explicitly raise failures.

| Control | Executed coverage |
| --- | ---: |
| Selected detector cycle words | 15 |
| Literal rational steps in the detector controls | 247 |
| Independently checked small multiplication-matrix determinants | 12 |
| Complete reduced-clock prime certificates | 13 |
| Positive rational preperiods | 15 |
| Direct-versus-transported prefix coefficient comparisons | 97 |
| Prefix first-forbidden-order comparisons | 13 |
| Convergent ordinary sources in the germ controls | 68 |
| Actual prefixes in those sources | 1,950 |
| Complete Taylor prefix identities | 23,400 |
| Exact denominator-clock comparisons | 23,400 |
| Direct carry-sum comparisons | 3,180 |
| Delayed-prime rational families | 5 |
| Literal rational steps in the delayed-prime families | 26,145 |
| Constructed convergent ordinary shadows | 2 |
| Complete ordinary shortcut steps in those shadows | 2,592 |
| Exact finite source-transfer checks | 7,621 |
| Distinct ordinary sources in the transfer controls | 237 |
| Explicit finite inverse laws | 35 |
| Projected cutoff cases | 733 |
| Exact finite layer-cake identities | 12 |

The delayed-prime examples have periods 12, 42, 117, 1,242, and 24,732.
The first four exhibit prime-five delay orders one through four. Every
state of the last complete rational cycle is strictly above eleven.
All are nonordinary; the full denominators are checked.

The ordinary shadows have a common rational reference of `263/803`.
Their prescribed prefixes reach `2^36` and `2^2520`, respectively,
then reach one. Eight coefficients for each are compared to the rational
reference with the stated binary precision. They are changing ordinary
sources, not a fixed infinite ordinary realization.

The finite inverse laws use stopped potentials on actually enumerated
convergent ordinary trajectories. They are not represented as full
escaping-component laws. The periodic balanced-compiler control is
checked through depth 128; the transported value has 336 bits and the
signed exponent displacement is 276. These finite observations do not
prove an asymptotic theorem or exhibit an escaping ordinary source.

## Independent written reconstruction

- [DETECTOR_REVIEW.md](DETECTOR_REVIEW.md) checks the finite resultant
  certificate, full valuation, coefficient indexing, explicit height bound,
  actual-prefix invariance, and conditional ordinary consumer.
- [DESCENT_REVIEW.md](DESCENT_REVIEW.md) checks the complete rational
  denominator, literal legality, primitivity, Hensel coefficient law,
  arbitrary floor, and genuinely convergent ordinary shadows. The reviewer
  also independently executed the lane's exact controls.
- [GERM_REVIEW.md](GERM_REVIEW.md) checks the exact denominator clock,
  binomial-moment identity, linear denominator growth implied by positive
  ternary radius, subring invariance, and the formalization boundary.
- [TRANSFER_REVIEW.md](TRANSFER_REVIEW.md) checks the actual-law overlap,
  layer-cake bound, complete residue quotient, retained atom, entropy
  constants, and narrow periodic compiler control.
- [ROOT_REVIEW.md](ROOT_REVIEW.md) records the integrating root's separate
  reconstruction and execution scope.

Reviews bind exact Git blobs. They do not extend to uninspected neighboring
claims or later source heads. The earlier PR182 title, body, head, and
base are preserved in [PR182_BEFORE.json](PR182_BEFORE.json). Current
selected upstream heads and full-text inspection boundaries are in the
scientific [source ledger](../../research/closure-round7-20261123/SOURCES.json).

## Complete-checkout gate and publication boundary

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the copied
five-command gate receipt for a clean complete local science checkout.
It names its own exact commit and tree, before the final source-binding
and copied receipt were added. It is not a receipt for a different head.

[SOURCE_BINDING.json](SOURCE_BINDING.json) binds all new scientific,
review, and execution files at that validated tree and every earlier
tracked Lean file. All 560 parent files remain unchanged. This binding
and the copied gate receipt are the only subsequent local additions.

Publication uses one GitHub commit on the unchanged remote parent and
a nonforced compare-and-swap branch advance. Its complete tree is read
back, fetched, and validated in a fresh detached checkout. The final
published-checkout receipt and exact head are recorded in PR182, avoiding
a circular receipt that purports to contain its own final commit identity.
The local science/receipt chain is retained under a checkpoint branch.

The five repository-integrity commands do not verify the mathematics.
The actual arbitrary-source construction remains the strongest open
obligation after this batch.

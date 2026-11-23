# Round eight: execution, review, and publication evidence

23 November 2026. Published parent:
`3954c775ba74e1f40776ff38cb4282698d4a334a`.

The scientific entry point is
[the scalar and ordinary-return packet](../../research/repo-synthesis-round8-20261123/README.md).
This report separates written proofs, Lean compilation, finite execution,
source preservation, and repository-integrity checks. **Collatz remains
unresolved.**

## Fresh Lean compilation

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records a fresh output directory
and three successful commands: the two new source modules and their
declaration audit. The compiler is Lean 4.34.1, commit
`5045d0056413266e57c625dcd7c365b10e377c52`, with Mathlib at
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
The official compiler archive's SHA256 was independently matched to
the GitHub release asset digest. Existing pinned Mathlib objects were
reused; no old repository module was imported by the new modules.

All commands use one thread, warnings as errors, and
`autoImplicit=false`. [RoundEightAudit.lean](RoundEightAudit.lean)
audits all **17 new theorems and three definitions**. Their only
observed axioms are `propext`, `Classical.choice`, and `Quot.sound`.
There are no admitted proofs or custom axioms in this dependency audit.

The six GermBridge theorems concern the polynomial contraction,
complete power relation, bit-length guard, and finite contradiction.
The eleven OrdinarySelector theorems concern literal ordinary gap
equalities, repeated rational affine maps, rational scalar block
identities and intervals, the exponential tail estimate, and affine
expansion. The real series, analytic derivative, full modular source
existence, actual all-time attachment, phase families, and full
candidate-decision theorem remain written mathematics.

## Exact bounded execution

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) records successful execution
of all four lanes, normally and under `python -O`. The outputs
[EXACT_CONTROLS.json](EXACT_CONTROLS.json) and
[EXACT_CONTROLS_OPTIMIZED.json](EXACT_CONTROLS_OPTIMIZED.json) are
byte-identical: 22,788 bytes, SHA256
`d9a79cdcf543d9d64809c9c7957a3e539b33bf83bb2fb7d29f3625e210c44696`.
All fifteen scientific inputs are bound by SHA256 before and after
execution. An AST scan of all five Python files found zero `assert`
statements; mathematical checks explicitly raise failures.

| Lane | Executed domain | Explicit checks |
| --- | --- | ---: |
| Actual scalar and candidate verifier | 140 convergent odd sources; 2,715 literal odd transitions; 1,812 supplied candidate decisions; 1,967 additional positive integer potential cases | 31,334 |
| Candidate separation and literature counterexample | 2,932 decisions on 128 convergent sources, including 2,613 incorrect candidates; complete actual 7-to-11 potential counterexample | 73,984 |
| Rational phases and pressure clocks | All 16 odd starts through 31; seven complete listed denominators; binary exponents 0 through 12; twelve odd-prime-power rows; exact pressure-clock bounds | 59,824 |
| Actual expanding low-scalar returns | Twenty constructed sources, with m=1 through 16 and m=24,32,64,128; literal prescribed prefixes and separate completed ordinary trajectories | 18,480 |

The total is **183,622 explicit checks**. Domains overlap, so this
total is not a distinct-source count or a number of proved theorems.
The largest constructed source has 523 bits. Its prescribed 258-step
prefix expands by more than 992,236 times and contains exactly one
scalar state above one. Its separately completed orbit reaches one
in 1,901 odd transitions. No selected finite example is an alleged
counterexample to Collatz.

The phase checks preserve the unresolved denominator-eight orbit and
the low phase at denominator 121. The written all-exponent results
are proved by their group and averaging arguments, not by extrapolation
from these bounded rows. The pressure input is source-qualified on
an actual escaping component; no hypothetical escaping orbit was
manufactured or empirically replayed.

## Independent reconstruction

- [GERM_REVIEW.md](GERM_REVIEW.md) independently reconstructs R8-G1--G4,
  including the strict endpoint, denominator clearing, finite budget,
  and q=1, r=0, unreduced, and even-source cases. It records 1,664
  separately implemented boundary checks.
- [PRESSURE_REVIEW.md](PRESSURE_REVIEW.md) reconstructs the phase and
  pressure proofs, the scalar-separation corollary, and both primary
  literature boundaries. Its independent replays passed normally and
  under optimization.
- [ORDINARY_PRESSURE_REVIEW.md](ORDINARY_PRESSURE_REVIEW.md) independently
  checks the full residue-fiber argument, complete binary cosets, the
  finite ordinary floor, and the same-source pressure deductions.
- [ORDINARY_REVIEW.md](ORDINARY_REVIEW.md) reconstructs R8-O1--O5,
  including ordinary modular existence, every physical block, the
  unconditional tail, one-high-visit count, expansion, and phase
  approximation. It explicitly identifies the rational scope of the
  scalar Lean lemmas.
- [ROOT_REVIEW.md](ROOT_REVIEW.md) records the integrating root's
  separate proof reconstruction, fresh compilation, and combined
  execution. It preserves the exact source-qualified pressure input.

These reviews bind exact science blobs. They do not approve every
claim on neighboring branches. [REPO_INVENTORY.json](REPO_INVENTORY.json)
contains the full 145-record PR metadata survey; its 122 open and 23
closed records are not presented as 145 fresh proof audits.
[PR182_BEFORE.json](PR182_BEFORE.json) preserves the previous title,
body, head, and base. [HANDOFF.md](HANDOFF.md) records one follow-up
calculation outside the current verified claim scope.

## Complete-checkout and publication boundary

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is the copied
five-command repository-integrity receipt for the clean complete local
science checkout. It names that checkout's exact commit and tree.
It predates only the addition of this copied receipt and the final
binding file; it does not pretend to contain its own final commit SHA.

[SOURCE_BINDING.json](SOURCE_BINDING.json) binds every file at that
science tree and all 53 earlier Lean files. All 586 files from the
published parent are preserved unchanged. This binding and the copied
gate receipt are the only subsequent local additions.

Publication creates one commit on the unchanged remote parent and
advances the existing research branch without force, with an expected
head check. Its tree is read back, fetched, and checked in a fresh
complete detached checkout. The published-checkout result and exact
remote identity are recorded in PR182, outside this noncircular receipt
chain. The local science/receipt chain remains on a checkpoint branch.

Repository-integrity success does not establish the new mathematics.
The first unresolved global task is still to construct the actual
scalar's triadic arithmetic for every fixed ordinary source, or to
exclude all its remaining low phases and irrational values by an
actual-source argument.

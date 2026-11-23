# Literature continuation: execution and semantic review boundary

Scientific entry:
[`research/literature-reframe-20261122/README.md`](../../research/literature-reframe-20261122/README.md).
The full Collatz theorem remains open. The analytic and literature-based
deductions in that packet are written mathematics, separate from its Lean
statements and from the repository integrity checks.

## New Lean scope

- `SourceCollision.lean`: seven public theorems, using default Lean `Init`.
- `PhysicalTailBarrier.lean`: four public theorems, importing the previously
  checked marked-prefix module and its two pinned local dependencies.
- `LiteratureAudit.lean`: one explicit axiom report for every public theorem
  in both new mathematical modules.

The combined run **passed** at scientific checkpoint
`293e13c45b2c9364757378c940fc06a38745bd4d`, tree
`4d088f6d4e96b02155a1cddd7e9532ec0f5abca1`, in a clean complete checkout
containing 445 tracked files. The run started at
`2026-11-21T23:19:06.446599+00:00` and finished at
`2026-11-21T23:20:35.916807+00:00`.

- **PASS:** all six Lean source invocations (three local imports, two new
  mathematical modules, and the combined audit), each with
  `-j1 -DwarningAsError=true`.
- **PASS:** all 11 new public-theorem axiom reports, with dependencies only
  among `propext`, `Classical.choice`, and `Quot.sound`.
- **PASS:** all five required repository integrity commands at the same
  complete scientific checkout, with its identity unchanged.

The actual [Lean receipt](proof-lean.json) records source hashes, commands,
captured output, complete public-theorem coverage, and before/after cache
verification. The [repository receipt](proof-repository.json) records its
separate integrity gate. The Lean build itself took 50.538 seconds;
the surrounding runtime/cache identity checks are also timed in the receipt.

The build uses Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`. The local imports are pinned by
[`imports.sha256`](../../research/literature-reframe-20261122/lean/imports.sha256).
The build script does not download a toolchain or cache. Its optional fast
storage overlay must be a byte-for-byte copy of the pinned runtime and
dependency cache; the receipt runner checks every overlay file before and
after use.

## Repeatable commands

With Lean 4.34.1 on `PATH` and the pinned Mathlib checkout in `MATHLIB_DIR`:

```sh
bash research/literature-reframe-20261122/lean/build.sh
python -X utf8 -B tools/validate.py --receipt /absolute/outside/repository.json
```

The first command checks three necessary local imports, two new proof
modules, and the audit. The second runs the five required repository
integrity commands; it does not verify the mathematics in the written
notes. No optional old regression bundle is rerun merely for publication.

[`validate_literature.py`](validate_literature.py) binds the Lean execution
to an expected clean complete commit, records every source hash and captured
command output, rejects incomplete public-theorem audit coverage, and
accepts only `propext`, `Classical.choice`, and `Quot.sound` in the new
theorems' dependency lists. Its output receipt must be outside the checked
checkout. A later receipt publication retains the actual checked SHA;
it is not relabeled as an execution of the publication commit.

## Semantic reviews and source refresh

The focused review files in this directory pin the exact manuscripts they
read. A verdict on one manuscript does not apply to a later revision or to
neighboring conditional claims. The reviews independently reconstruct the
quantifiers, affine corrections, law normalizations, rank bounds, and
ordinary-source arguments. Paper review is not represented as Lean checking.

[`SOURCE_REFRESH.json`](SOURCE_REFRESH.json) records the fresh metadata for
PR175, PR180, PR183, and PR185. The scientific notes name the actual files
read and the claim boundaries used. The source-qualified PDU assertion
from PR180 remains an explicit premise of the new renewal criteria.

The preceding packet's successful 25-theorem execution, earlier import-path
failure and repair, and repository receipts remain preserved under
[`../2026-11-21-reframe/`](../2026-11-21-reframe/README.md).

## Publication followup

The followup publishes these actual receipts and the written
[`ABEL_ANTICHAIN.md`](../../research/literature-reframe-20261122/ABEL_ANTICHAIN.md)
consequence of the separately qualified PR180 Abel construction. That
analytic addendum has its own source review; it is not covered by a Lean
receipt. The two new Lean proof sources, their audit, build script, and
local imports remain identical to the scientific checkpoint above.
No new Lean execution at the receipt-publication head is claimed.

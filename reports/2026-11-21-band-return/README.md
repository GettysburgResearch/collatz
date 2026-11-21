# Band-return checkpoint: actual execution evidence

The scientific entry point is
[`research/band-return-20261121/README.md`](../../research/band-return-20261121/README.md).
Full Collatz convergence remains **OPEN**. The strongest new unconditional
return theorem is first-return descent on a cofinal symbolic family. The
pointwise frequency theorem assumes an injective odd orbit and proves zero
temporal density of its marked visits.

## Exact checked checkpoint

The complete Lean execution below concerns commit
`a8a0736e2f8e98e363a37030327d884fe0d97ed6`, tree
`64a926f2b648f537ef815ac2eed7736bec43a467`, with **388 tracked files**.
It was pushed to branch `research/lean-global-20261121` and its remote ref
was read back. The branch is attached to
[draft PR178](https://github.com/GettysburgResearch/collatz/pull/178).

The proof input is the exact PR173 head
`fa0c9e2a2851e6324391e39c17afcb5913185aec`, with the four original source
modules copied byte for byte. The source and toolchain pins are in
[SOURCES.md](../../research/band-return-20261121/SOURCES.md).

| Actual execution | Result | Receipt |
|---|---|---|
| Fresh complete band-packet Lean build, followed by the dedicated public-theorem axiom audit | PASS; 13 Lean source invocations, all with `-j1 -DwarningAsError=true`; 81 audited public statements | [checkpointA-lean.json](checkpointA-lean.json) |
| Required repository gate in a clean complete checkout of the same commit | PASS; all five commands | [checkpointA-repository.json](checkpointA-repository.json) |

The successful Lean run occurred on 2026-11-21 from 15:36:24 to 15:37:38
UTC. The full build command took 73.529 seconds. Its checkout was clean
before and after execution, and every recorded source hash was unchanged.
Lean was version 4.34.1; Mathlib was clean at
`d13f23b723b8a846827a245b89c10fc7d3f11612` before and after the run.
The receipt includes the actual commands, complete captured output,
source hashes, and each theorem's logical dependencies.

The 81 public statements consist of four credited arithmetic lemmas in
`BandCore`, nine certificate lemmas, fourteen offset-family lemmas, five
finite-simulation lemmas, sixteen Fourier lemmas, three marked-phase
lemmas, twelve finite-kernel/frequency lemmas, and eighteen return-bridge
lemmas. This is an audit count, not a claim that all 81 are novel results.
The only reported axioms are Lean's standard `propext`, `Classical.choice`,
and `Quot.sound`; some statements use fewer. No conjectural closure axiom
or `sorry` proves the unresolved universal descent statement.

The repository gate checks structure and frozen integration identities.
Its success is recorded separately from Lean's mathematical checking.
The older common-rank and affine work was not rebuilt in this pass; its
actual historical receipts remain in the
[earlier report](../2026-11-21-lean-global/README.md).

## Receipt-parser correction, preserved explicitly

The first combined Lean run also returned exit code zero for the complete
build, but the surrounding receipt script rejected a repeated axiom report:
`BandSimulation.lean` printed its own focused report before `BandAudit.lean`
printed the complete set. The raw failed wrapper result is retained as
[initial-receipt-parser-rejection.json](initial-receipt-parser-rejection.json).

The correction scopes declaration coverage to the output after
`Checking new BandAudit`. It still checks multiline axiom lists and demands
all 81 declarations, with no unexpected dependencies. No Lean proof was
changed. A second fresh complete checkout then produced the successful
receipt above. The exact successful runner is archived as
[validate_band.py](validate_band.py); its hash matches the runner hash in
that receipt. Its runtime paths record this session's environment. For
other environments, the portable invocation is documented in the
[build guide](../../research/band-return-20261121/LEAN_ROUTE.md).

## Focused independent semantic reviews

- [BAND_BRIDGE_REVIEW.md](BAND_BRIDGE_REVIEW.md) checks the actual first
  positive return, exact all-parameter family, positive and even prefix,
  marked membership, and cofinality. It independently compiled the reviewed
  source with warnings treated as errors. Its verdict has the pinned family
  as its scope; it supplies no universal coverage theorem.
- [SIMULATION_REVIEW.md](SIMULATION_REVIEW.md) checks the finite ordinary
  witnesses and the changing-source quantifier, including the distinction
  between the invariant phase/2-adic law and a fixed positive counterexample.
  This review records source hashes and performed no additional compiler run.

## Receipt follow-up and evidence boundary

These receipts and this index are added in a follow-up to the checked
checkpoint. The Lean files, build script, toolchain specification, copied
source modules, and hash manifests remain byte-identical to the checked
commit. The added final-attempt note and navigation links are prose.

The PR body records the final receipt commit and its separate complete
repository-gate execution. The successful Lean receipt keeps its original
checked SHA; it is not relabeled as an execution at a later documentation
commit. No additional Lean rebuild is claimed for the receipt-only update.

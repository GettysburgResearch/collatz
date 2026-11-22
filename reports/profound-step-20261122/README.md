# Independent-block and ordinary-channel checkpoint: execution evidence

**Five new Lean modules compiled, and all 52 public theorem declarations
passed the combined transitive axiom audit. Full Collatz remains OPEN.**
The statements, written extensions, source qualifications, and missing
global implications are in the
[research packet](../../research/profound-step-20261122/README.md).

## Actual formal execution

- Lean **4.34.1**, release commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib **d13f23b723b8a846827a245b89c10fc7d3f11612**, with unchanged
  tracked sources.
- Every new module compiled with `-j 1 -DwarningAsError=true`.
- All 52 declarations were checked together using `#print axioms` against
  the actual compiled modules. Their transitive dependencies are subsets
  of `propext`, `Classical.choice`, and `Quot.sound`. Two declarations need
  no axioms. No `sorryAx`, custom axiom, or native-decide axiom occurs in
  those dependencies.

| Module | Public declarations | Compiler seconds | Formal scope |
|---|---:|---:|---|
| `ClockLags` | 10 | 2.660 | Actual meeting clocks, unique integer lags for an injective reference orbit, synchronous classes, increasing inverse fronts |
| `AsynchronousKernel` | 8 | 6.904 | Independent-clock geometric weights, overlap windows, geometric summability, normalized atom and finite Cesaro bounds |
| `BlockCompression` | 13 | 8.527 | Arbitrary finite products of repeated actual parity words, exact short-cycle alternative, exponential clock budget, primitive-cycle consumer |
| `AffineCarry` | 14 | 16.311 | Complementary ordinary map, arbitrary-gap/debt transport, exact capture identities, all-parameter finite debt amplification |
| `CarryCapture` | 7 | 8.695 | Arbitrarily long carry runs, padding funded by the same certificate grade, guarded interval capture, the full language `1{2,3}*2` |

The combined audit took 23.976 seconds. These are elapsed execution times
from this environment, not performance guarantees.

[`lean-replay.json`](lean-replay.json) contains the actual successful
compiler invocations, working directories, import paths, outputs, source
and artifact hashes, and the full axiom audit. The generated audit source
is preserved as [`ProfoundAudit.lean`](ProfoundAudit.lean). The driver checks
each source hash before and after compilation.

Two new imported dependencies, `WitnessGlobal` and `WitnessSynthesis`, were
compiled separately in 14.776 and 4.137 seconds. Their raw bodies are pinned
byte for byte to PR185 at `276be8154f4e867acc0230466b34d9cb224aacf5`.
Generated wrappers add only module/export headers. The raw source and
wrapper hashes are recorded in the receipt and
[`DEPENDENCIES.json`](../../research/profound-step-20261122/mergers/DEPENDENCIES.json).

The eleven earlier band/literature modules were **reused**, after checking
their source and compiled-artifact hashes against successful receipts.
They were not recompiled in this pass. Their preserved receipts are
[`dependency-replay.json`](../literature-closing-20261121/dependency-replay.json)
and [`lean-replay.json`](../literature-closing-20261121/lean-replay.json).
Their earlier theorem counts are not included in the 52 new declarations.

## Written deductions and their review boundary

The following results are written mathematics, outside this formal count:

- Effective classification of cycles represented by fixed parity atoms
  with independent repetition counts. Its transcendence input is the
  stated published Matveev theorem; its finite ordinary compression core
  is formal. The enormous finite classification algorithm was not run.
- Identification of all ordinary escaping channels in the Wold unitary
  part; boundary-frequency formulas; passage through all original source
  pairs; the full-source critical residue and nontrivial-cycle pole.
  These retain the displayed, source-qualified ordinary harmonic-reference
  hypotheses from PR185. Their existence argument is not re-proved here
  or imported as a Lean axiom.
- The elementary construction of complete source certificates with
  unbounded intermediate debt, the exact binary precision comparison, and
  the direct five-clock descent of those targets. The finite carry identity
  used in that construction is formal; the full written construction is
  not relabeled as a Lean theorem.

Narrow independent reconstructions are preserved in
[`RECONSTRUCTION_REVIEW.md`](../../research/profound-step-20261122/RECONSTRUCTION_REVIEW.md),
[`OPERATOR_REVIEW.md`](../../research/profound-step-20261122/transport/OPERATOR_REVIEW.md),
[`MERGER_REVIEW.md`](../../research/profound-step-20261122/transport/MERGER_REVIEW.md),
and [`CARRY_COMPRESSION_BRIDGE.md`](../../research/profound-step-20261122/arithmetic/CARRY_COMPRESSION_BRIDGE.md).
They concern the exact source hashes and claims stated there; they are not
external human reviews, accepted-status upgrades, or reviews of every
upstream source.

## Focused exact finite replay

The new carry checker was executed by the coordinating agent against the
final source. [`finite-execution.json`](finite-execution.json) records the
actual command, source hash, exit status, output, and result hash.
[`finite-arithmetic.json`](finite-arithmetic.json) records:

- 39,935 one-gap instances and 7,547 composed actual gap steps;
- all 511 words with a body of length zero through eight in `1{2,3}*2`;
- 32 explicit ordinary debt families, for parameters one through 32,
  reaching 512-bit sources and 480 ordinary clocks.

These are bounded implementation checks. They do not establish the
all-parameter claims, test the later complete-certificate variant, or prove
universal convergence. No old census or historical regression bundle was
rerun for this checkpoint.

## Source binding and repository gate

[`source-binding.json`](source-binding.json) binds every new formal source
to its successful compiled artifact and records the written-packet hashes,
driver, receipts, and starting commit. It keeps the full-theorem status
false and the written/Lean boundaries explicit.

The proof checkpoint is
`84a76f0d81839494e17a0de5fea207ea96da5f87`, tree
`817017ac2d93f977278e5d29dc59120ae231a63d`. Its clean complete checkout
passed all five required commands of `python -X utf8 -B tools/validate.py`
across 400 tracked files and remained unchanged. The actual receipt is
[`proof-checkpoint-validation.json`](proof-checkpoint-validation.json).

This receipt-only follow-up changes no proof or executable. PR183 records
its final head after a second exact-head gate and remote readback.
Repository integrity validation is distinct from mathematical verification.

## The remaining global step

The new compression theorem requires control of the number and lengths of
repeated parity atoms on every unresolved orbit. The carry rules require a
complete successful selector compatible with the same certificate grade.
The operator route requires the actual cycle-sensitive critical residue to
vanish. None of these universal closing assertions is established here.

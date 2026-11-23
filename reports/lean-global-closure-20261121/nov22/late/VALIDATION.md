# Fresh 21-unit build of the published late-source checkpoint

## Exact checked checkout

Scientific commit: **`360e20ce3430a3d1124c34f0a6ba8e8be26c57c4`**

Tree: **`3e19c55c1b6a4861086e7bae9548e070aa506fe6`**

This was a clean complete checkout with **447 tracked files**. The remote
branch was queried after publication and matched that commit. The checkout
remained clean after both executions below.

## Core Lean execution — PASS

The actual command, from that checkout, was:

```sh
TMPDIR=/workspace/scratch/957bb0caa6f2/wide-tmp \
python -B research/lean-global-closure-20261121/build_wide.py \
  --lean /tmp/collatz-lean-runtime/lean-4.34.1-linux/bin/lean \
  --output /workspace/scratch/957bb0caa6f2/nov22-evidence/core-build-360e20 \
  --receipt /workspace/scratch/957bb0caa6f2/nov22-evidence/late-source-build.json
```

- **21 of 21 source invocations passed.**
- The output directory was fresh; `LEAN_PATH` contained only that directory.
- All eight frozen vendor sources passed SHA256 and Git-blob checks.
- Compiler: Lean **4.34.1**, commit
  `5045d0056413266e57c625dcd7c365b10e377c52`.
- Every invocation used `-j1 -DwarningAsError=true -DautoImplicit=false`.
- **141 declaration-level axiom reports**, including 70 from this
  November continuation's five new modules and 15 from its two late modules.
- The union of reported dependencies is exactly
  `Classical.choice`, `Quot.sound`, and `propext`.
  Three reported declarations have no axioms.
- No `sorryAx` or custom Collatz axiom appears in any reported closure.
- Every receipt-bound source hash matches the checked checkout.
- Recorded compiler time: **35.803 seconds**.
- **No Mathlib was required.**

The counts describe audited declarations, including supporting lemmas and
credited ports. They are not counts of independent new discoveries.

| Late module | Axiom reports | Source SHA256 |
|---|---:|---|
| `SignedCarryReturns` | 11 | `0af50217b1da102d8fdaf7f9d61fedcdaad75cbf059452d02dcd8b82b59fe5d7` |
| `OddReturnClock` | 4 | `f532f89fb9042e7073e992bf26e0049f28829171075e23e87edfa50fd66439ac` |

Evidence: [full compiler receipt](source-build.json) and
[parsed axiom inventory](axiom-audit.json).

Compiler receipt SHA256:
`2fbd2ac180812be0393f04a0e358804eb9a1bba045b9f1a0fc28509ddd574380`.

Audit SHA256:
`2954873dd3c0c50db866a1dfc0a7c53858db13ed52841c0a4056949d39949f09`.

## Complete repository execution — PASS

The actual command was:

```sh
TMPDIR=/workspace/scratch/957bb0caa6f2/wide-tmp \
python -X utf8 -B tools/validate.py \
  --receipt /workspace/scratch/957bb0caa6f2/nov22-evidence/late-repository.json
```

All **five** required repository commands passed, including their required
bounded self-tests. The optional regression bundle was not run.

Evidence: [complete repository receipt](repository.json), SHA256
`f257675bbd6a097b999a8960e52b1c1df333771615cd26eb5f0b7c91dc0caa17`.

Repository integrity is distinct from Lean kernel checking and from review
of written analysis. No full-Collatz verification is claimed by this gate.

## Mathematical scope and independent reviews

The new return adapter proves the credited return cone from its actual
proof, retains the full lower-grade interval hypothesis, and connects it
to arbitrary supplied source prefixes. Its counterexample prevents
interpreting the successful guard as exhaustive.

The odd-count return theorem is unconditional finite arithmetic for an
actual return with its displayed nonresonance condition. It is not a
bound on all downstream merger clocks.

The Green harmonic moments, sharp Dirichlet boundary asymptotics,
five-edge operator obstruction, and clock-filter results are **written
mathematics**, with their own source dependencies and review boundaries.
They are not included in the Lean declaration count. The source-qualified
ordinary harmonic construction and finite-five-energy rigidity have not
been reclassified as unconditional kernel-checked inputs.

Scoped reviews:

- [Signed-carry return integration](SIGNED_CARRY_RETURNS_REVIEW.md).
- [Global harmonic Green moment](GREEN_HARMONIC_MOMENT_REVIEW.md).
- [Odd-return and channel composition](ODD_RETURN_CHANNEL_REVIEW.md).
- [Independent channel-trace reconstruction](CHANNEL_TRACE_INDEPENDENT_REVIEW.md).
- [Sharp Dirichlet boundary identities](DIRICHLET_BOUNDARY_REVIEW.md).
- [Boundary-identity integration review](DIRICHLET_BOUNDARY_INTEGRATION_REVIEW.md),
  with the reviewer's contribution to that argument disclosed.
- [Exact five-edge propagation obstruction](FIVE_EDGE_TRANSPORT_REVIEW.md).
- [Accelerated transport integration review](FIVE_EDGE_TRANSPORT_INTEGRATION_REVIEW.md),
  with the reviewer's contributions disclosed.
- [Clock filters and the corrected five-ray cutoff](FOLNER_CHANNEL_REVIEW.md).

The original review hashes remain recorded. Publication-only whitespace
normalization and receipt-link repair are in
[PUBLICATION_NORMALIZATION.json](PUBLICATION_NORMALIZATION.json).
The final literature notes and their reviews were copied without byte changes
from their reviewed source versions; their receipts record the exact hashes.

## Reporting and literature follow-up

This follow-up commits the actual receipts and the new written literature
deductions. It does not change any of the 21 compiled Lean sources or the
core build driver. The final publication-head repository gate and source
hash comparison are reported in the PR description after execution.

The expanded legacy `build_band.py --full` module list remains consistent
with the core entrypoint. No fresh replay of that Mathlib packet is claimed.

**Unproved closing step:** no total successful common-rank selector has
been established. The exact Dirichlet limit identifies an escape charge
but does not prove that charge is zero; nontrivial cycles remain a
separate obligation.

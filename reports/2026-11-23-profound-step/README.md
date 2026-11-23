# Evidence for the profound-step continuation

Date: 23 November 2026. Base: PR178,
`4e204f54136c79cf8c9393b34e3330594f99ae0a`.

The scientific entry point is
[the new research packet](../../research/profound-step-20261123/README.md).
**No full Collatz proof is claimed.** This directory records verification
and source provenance rather than a competing scientific narrative.

## New Lean checks

| Lane | Theorems | Author evidence | Independent evidence |
| --- | --- | --- | --- |
| Arithmetic boundary candidates | 10 | `arithmetic-lean-receipt.json`, `arithmetic-compile.log`, `arithmetic-axioms.log` | `arithmetic-review-execution.json`, `arithmetic-review-compile.log`, `arithmetic-review-axioms.log` |
| Forced real-control recurrences | 8 | `transfer-lean-receipt.json`, `transfer-compile.log`, `transfer-axioms.log` | `transfer-review-execution.json`, `transfer-review-compile.log`, `transfer-review-axioms.log` |

Each core module and its explicit theorem-audit module compiled with
`-DautoImplicit=false -DwarningAsError=true`. The independent builds used
separate fresh output directories. The author and independent axiom
logs match exactly within each lane. Empty compile logs are the actual
output of successful strict compilation, not omitted evidence.

Lean: 4.34.1, compiler commit
`5045d0056413266e57c625dcd7c365b10e377c52`.
Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
Existing mathlib dependency objects were reused. No old project proof
corpus or bounded regression census was replayed.

All eighteen new authored public theorem declarations have explicit
`#print axioms` entries. Their axiom union is `propext`,
`Classical.choice`, and `Quot.sound`; there is no `sorryAx`. This scope
is finite recurrence and numerator algebra. Infinite convergence,
aperiodicity, height arguments, q-carry series, source interpretation,
and the external literature assessment have written-proof scope.

## Independent mathematical reviews

| Packet | Author | Independent reviewer | Report |
| --- | --- | --- | --- |
| Arithmetic | `triadic_construction` | `cycle_arithmetic` | [arithmetic-review.md](arithmetic-review.md) |
| Dynamics | `actual_orbit_rigidity` | `/root` | [dynamics-review.md](dynamics-review.md) |
| Cycles | `cycle_arithmetic` | `actual_orbit_rigidity` | [cycles-review.md](cycles-review.md) |
| Carries and transfer | `/root` | `triadic_construction` | [transfer-review.md](transfer-review.md) |
| Final failure-position attempt | `cycle_arithmetic` | `/root` | [failure-position-review.md](failure-position-review.md) |

These are independent checks by project agents, not external peer
reviews. Each report identifies exact file hashes, reconstructed
arguments, inspection boundaries, and the remaining open claim.
The cycle and dynamics lanes add no Lean modules.
The final failure-position note also has written-proof scope and does
not change the eighteen-theorem count. The arithmetic and transfer
summaries in the research README received an additional integration-scope
read from `triadic_construction`; the final failure-position addition is
covered by its separate review.

## Source evidence

[SOURCE_SNAPSHOT.json](SOURCE_SNAPSHOT.json) records the thirty latest
updated open PR records read during this pass, the owned base, main,
and the changed peer packets. It does not claim a new complete proof
audit of all branches. The preceding checkpoint retains the broader
145-PR inventory.

The important new peer pins are:

- PR180: `fcdcdbadc6172e414f7282442a8a6b85587d7e70`, for the actual
  boundary dimension, fixed absolutely continuous reweightings, and
  trace-profile source comparison.
- PR182: `b78819e95ee7d39f02022de991b42217821e7590`, for the one-source
  pressure maximum and full numerical cycle cancellation discussion.

Claim-level provenance and primary literature inspection are in
`arithmetic-sources.json`, `cycles-sources.json`, `transfer-sources.json`,
and [the dynamics source ledger](../../research/profound-step-20261123/dynamics/SOURCES.json).
External theorems and the analytic component construction remain
source-qualified; reading a theorem statement is not an audit of its
entire proof or an import into Lean.

The [previous PR178 body](archive/PR178_BODY_AT_4e204f5.md) is preserved
at its exact old head. This continuation adds files and does not alter
earlier reviewed research packets or their manifests.

## File integrity and publication gate

`FILES.json` binds every file in the two new packet directories except
the manifest itself, using byte lengths, SHA-256, and Git blob SHA-1.
Review target hashes are checked against the actual frozen source bytes.

The repository-required final gate is
`python -X utf8 -B tools/validate.py --receipt <outside-checkout>`
in a clean complete checkout of the exact created commit. Its result,
head, tree, parent, and clean status are placed in the publication PR
after the command runs. The external receipt avoids inserting a
self-referential commit hash into this commit. No execution outcome
is pre-asserted here.

Repository integrity and successful Lean elaboration do not establish
the missing universal witness, the actual-source collision upper, or
unrestricted positive-cycle exclusion.

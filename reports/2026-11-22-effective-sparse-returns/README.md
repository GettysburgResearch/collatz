# Checkpoint 13: effective sparse returns, replay and review

## Scientific outcome

The [research packet](../../research/lean-global-resolvent-20261121/overview/returns/README.md)
contains two independently reviewed positive written estimates on actual
integer orbits: an effective, source-uniform `O_S(N/log N)` occupation bound
for fixed binary-run cutoff on injective segments, and a power-descent
theorem for nonexceptional sparse returns within every fixed logarithmic
horizon. Their exact hypotheses and literature dependencies are retained.

Fourteen finite Lean statements support the first estimate. The deep
S-unit inputs and the full orbit-level conclusions remain written proofs.
Neither a universal descent theorem nor full Collatz is asserted.

## Executed focused Lean replay

[lean-fresh-replay.json](lean-fresh-replay.json) records the complete
command arguments and output of
[check_returns.py](../../research/lean-global-resolvent-20261121/overview/returns/check_returns.py).
The new proof module and its audit were compiled into an initially empty
project output directory. Pinned precompiled Mathlib and runtime objects
were reused; older project checkpoints were not recompiled.

| Project module | Exit | Seconds |
| --- | --- | ---: |
| `Collatz.DyadicCluster` | 0 | 25.466 |
| `AuditDyadicCluster` | 0 | 24.637 |

Both commands used `-DwarningAsError=true`. All fourteen public theorem
audits passed. Their axiom union is exactly `propext`, `Classical.choice`
and `Quot.sound`. The driver verified source hashes before and after
execution, all eight direct Mathlib import hashes, Mathlib's toolchain
and package manifest, and the four written-note hashes. All checked
project source bytes remained unchanged.

Runtime pins:

- Lean 4.34.1: `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.

The developing agent separately compiled the same final source. The
receipt linked above is the root's fresh replay of the integrated bytes.
No full historical proof replay or broad orbit search was performed.

## Independent mathematical and source review

The source-sensitive renewal agent reconstructed both proofs, checked
the exact primary literature statements, and read the complete final
Lean source. The root also read the final proofs and theorem bodies.
Independent mathematical review, source inspection and compiler
execution are separate evidence levels.

| Frozen artifact | SHA-256 | Reviewed scope |
| --- | --- | --- |
| `EFFECTIVE_RUN_OCCUPATION.md` | `911d73f4b1ebb18b2046b999124707e8c5566fe2853729c0bacd3e14b343cea4` | Local correction-index refinement, explicit finite core, injective packing, ESS cardinality constant and `N/log N` rate. |
| `lean/Collatz/DyadicCluster.lean` | `9d70fa3516bc15a5fe9473d74dd1a60585e31ffc5be6a9189a57a5d609a89da4` | All fourteen finite theorem bodies and their explicit assumptions. |
| `lean/AuditDyadicCluster.lean` | `09fca89300b52c47c844ae05d0a58c7e3da4d74674b300617e4700055cd33222` | Complete public theorem list and kernel-dependency audit, executed by the root. |
| `LOGARITHMIC_SPARSE_RETURN_DESCENT.md` | `086358d37609522226c5f585a07ecb2fff3e9e82e80c8289adfcf9bb7bd2725b` | Evertse specialization, all nonempty subsums, fixed exceptional set, growing horizon, power descent and the final effective/ineffective comparison. |

The full reviews are
[REVIEW_EFFECTIVE_RUN_OCCUPATION.md](REVIEW_EFFECTIVE_RUN_OCCUPATION.md)
and [REVIEW_LOGARITHMIC_DESCENT.md](REVIEW_LOGARITHMIC_DESCENT.md).
The former supersedes an unpublished weaker square-root-logarithm draft.
The final frozen result uses `N/log N` throughout. The latter records an
original full-proof review and a separately pinned comparison update;
the final hash in the table is the published version.

The primary ESS theorem was checked at Theorem 1.1, printed p. 808.
Evertse's 1984 Theorem 2 was checked in the original PDF, including
equation (14) on p. 228 and the vector norm on p. 226. Both root and
reviewer visually inspected those formulas. Neither theorem is added
as a custom Lean axiom.

## Exact finite source-horizon control

[horizon-control.json](horizon-control.json) records one execution of
[check_horizon.py](../../research/lean-global-resolvent-20261121/overview/returns/check_horizon.py).
It exited zero in 0.036 seconds, using Python's standard library and exact
integers. The script's SHA-256 is
`03f57bef7a6765e11b9cc0a5e74c057e0caa4dd840da34db7137f15f7feb89a9`.

The root read the closed 16-element inverse-cluster argument and the
whole-source debt recurrence. For target 3711 and powered source 2184,
the target is 76196 at the odd-source completion clock 21 and 28574 at
the powered-source clock 24. Its first descent is clock 37, to 2543.
The source is minimal among capturing grades and maximal at its grade,
as justified by the complete small inverse cluster and initial-exponent
enumeration in the note.

This finite control rejects a proposed stronger horizon conclusion.
It is not a counterexample to `FloorIntervalStep`, and does not claim
that target 3711 is nonconvergent. No new Lean declaration was added for
the unsuccessful word-exchange or stopping-tree transport attempts.

## Repository survey and frozen inputs

[repository-snapshot.json](repository-snapshot.json) contains 145 PR
metadata entries, obtained from the union of the 100 most recently
updated and the 100 earliest created PR results, and exact metadata for
twelve selected active heads. Repository maps and errata were read,
followed by targeted proof reading at the relevant fresh heads. The
inventory is not an independent mathematical review of all 145 PRs.

Principal exact source objects for the positive results and direct attempts:

- PR177, `e4ca639326bac73da8c2a698dec8a749e5efbe68`:
  `research/lean-exact-witness-global-20261121/LITERATURE_ARITHMETIC_RETURN.md`,
  `LITERATURE_CANONICAL_ENERGY.md`, and `JOINT_MINIMAL_COUNTEREXAMPLE.md`
  in that same directory.
- PR175, `08fe1388ad63c758680b3695249aca319515c47d`:
  `research/lean-global-closure-20261121/machinery/EXACT_RUN_WEIGHT_COMMUTATOR.md`,
  `ADAPTIVE_SIBLING_AND_HARNACK_ATTEMPT.md`,
  `TILTED_RENEWAL_FINITE_IMMIGRATION.md`, and `MOVING_CESARO_FIBRES.md`
  in that same machinery directory.
- PR180, `a66a44c9bf058cd7efe1018827ddda9a13297a21`:
  `research/deep-machinery-20261122/ARITHMETIC_RIGIDITY.md` and
  `RENEWAL_TRANSPORT.md` in that same directory; the original
  `research/central-step-20261122/CRITICAL_BOUNDARY.md` retains its
  explicitly documented earlier source pin.
- PR185, `980d40fc4afeaaf8f2a9256f322acf3e4568e013`:
  `research/deep-closing-20261122/ACTUAL_ORBIT_ENTROPY.md` and
  `ARITHMETIC_ATTACK.md` in that same directory.

## Publication boundary and next mathematical obligation

The clean complete-checkout validator is a separate publication gate.
Its measured receipt is kept outside the tracked tree so it can identify
the exact committed tree without a self-referential report commit.
The PR description records its actual result and the published-head
readback. Repository integrity is not evidence for the mathematical
statements beyond the checks above.

The next unresolved inference is concrete. A general candidate bad
orbit has not been shown to supply fixed-run sparse endpoints in the
required horizon. On the analytic route, the adequate estimate must
control the actual transported original source law or canonical terminal
measure. On the source-word route, endpoint divisibility and the original
grade must be preserved together. The positive results in this checkpoint
do not discharge those global existence and transport obligations.

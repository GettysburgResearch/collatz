# Round ten: formal proof, independent review, and publication evidence

23 November 2026. Published parent:
c369ae3c426ec6aaf9a280ec9578b9910c2147d5.

The scientific entry point is the
[actual scalar and return-tower packet](../../research/carry-tower-round10-20261123/README.md).
**The actual scalar criterion is now formalized; the universal
triadic arithmetic assertion and Collatz remain OPEN.**

## Fresh Lean compilation and complete declaration audit

[LEAN_RECEIPT.json](LEAN_RECEIPT.json) records five successful
commands: the four new modules and
[RoundTenAudit.lean](RoundTenAudit.lean). They compiled into a newly
empty output directory under Lean 4.34.1, commit
5045d0056413266e57c625dcd7c365b10e377c52, and Mathlib commit
d13f23b723b8a846827a245b89c10fc7d3f11612.

The official compiler archive digest was verified in the parent
receipt. This run additionally binds the compiler binary's SHA256.
Existing pinned Mathlib objects were reused; no prior repository
module or prior compiled output of a new module was imported.

All commands used one thread, warnings as errors, explicit implicit
variable control, and default heartbeats. All **75 theorems and
16 definitions** were audited. The only observed axioms were
propext, Classical.choice, and Quot.sound. There were no admitted
proofs or custom axioms in the audited dependencies.

| Module | Theorems | Definitions | Exact formal scope |
| --- | ---: | ---: | --- |
| ActualScalar | 37 | 10 | Actual factorization map and orbit; unconditional real summability; logarithmic and strict lower bounds; recurrence and exact tails; actual convergence iff triadic scalar arithmetic |
| ArithmeticTower | 12 | 1 | Literal two-step blocks, full binary divisor, same-source window, finite exponent and automatic-family budget consequences |
| GeneralPhaseReturn | 14 | 4 | Guard-to-rank implication, arbitrary high-carry envelope, arbitrary finite path iteration, paid bounds and finite high-stage budget |
| ReturnTower | 12 | 1 | Complete paid affine factors, finite tower products, run-growth induction, fixed-center transport, expansion and tail arithmetic |

The first module includes the actual infinite scalar and actual
convergence conclusion. The other modules retain their narrower
finite scopes. Complete phase attachment, the periodic-shadow
departure theorem, full ordinary tower construction, and the
infinite 2-adic irrationality argument remain written mathematics.
The germ derivative identity and even-source bridge are outside
the new formalization.

## Exact finite controls

[EXACT_RECEIPT.json](EXACT_RECEIPT.json) records the combined normal
and optimized executions. Their outputs,
[EXACT_CONTROLS.json](EXACT_CONTROLS.json) and
[EXACT_CONTROLS_OPTIMIZED.json](EXACT_CONTROLS_OPTIMIZED.json), are
byte-identical: 24,998 bytes, SHA256
a46647bf4b567968b3e8d5831cbf3adfe5aff16981f36b2ec052ad0fe5308646.

All 14 scientific inputs were hashed before and after. All four
Python files have zero AST Assert nodes. The explicit checks remain
active under optimized Python.

| Lane | Executed domain | Explicit checks |
| --- | --- | ---: |
| Arbitrary-return tower | 15 repetition-rank boundaries; three mixed paid towers; nine controlled actual towers through 256 prescribed returns and a 15,877-bit source | 35,714 |
| General rational phase | 8,192 supplied source/phase cases; 56 arbitrary paid paths with carries through 1,457; 40 completed scalar-transport controls; the 1456 family through the 101/102 threshold | 16,541 |
| Sparse arithmetic scripts | 126 binary words and 252 ordinary lifts; 16 automatic cylinders; 8,256 supplied-source budgets; 52 finite tail valuations and 10,400 rational-height cases | 74,178 |

The combined total is **126,433 explicit checks per execution**.
Domains overlap; this is not a count of distinct sources or universal
theorems. The tower's actual scalar enclosures are unconditional and
do not assume that its large source reaches one. Selected small
trajectories are completed only for the phase lane's separate exact
scalar-transport controls. No exact positive ordinary source with
scalar 7/8 is asserted.

## Independent mathematical reconstruction

- [ACTUAL_SCALAR_REVIEW.md](ACTUAL_SCALAR_REVIEW.md) reconstructs
  R10-G1--G3 from the final Lean definitions through summability,
  strict lower bound, exact tails, integral log descent, ternary
  clearing and the converse. The reviewer did not author this proof.
- [ARITHMETIC_REVIEW.md](ARITHMETIC_REVIEW.md) reconstructs R10-A1--A4,
  including the complete ordinary divisor, 2-adic rational-height
  obstruction, four automatic families, and finite mismatch budget.
  It also checks the directly inspected primary-literature boundary.
- [GENERAL_PHASE_REVIEW.md](GENERAL_PHASE_REVIEW.md) reconstructs
  R10-P1--P5, including both signs of the canonical denominator,
  cancellation endpoints, the cycle branch, exact source budgets,
  equality transport and the complete 1456 threshold.
- [ORDINARY_GENERAL_PHASE_REVIEW.md](ORDINARY_GENERAL_PHASE_REVIEW.md)
  supplies another independent reconstruction and execution. Its
  separate shadow-departure harness checks 290 phases and 18,560
  ordinary phase/source cases, including the phase-3/2 boundary.
- [RETURN_TOWER_REVIEW.md](RETURN_TOWER_REVIEW.md) reconstructs
  R10-T1--T3, including the arbitrary paid bound, exact fixed-word
  rank, positive cylinders, unconditional true-scalar tails, and
  the limits of the potential obstruction. It separately replays
  four tower lengths with a division-based valuation calculation.
- [ROOT_REVIEW.md](ROOT_REVIEW.md) records the integrating review,
  evidence scopes, and the root's fresh execution.

Every review fixes exact Git blobs. Verdicts do not extend to
changed files or broader conjectures. The
[handoff](HANDOFF.md) states the remaining fixed-source problem.

## Complete-checkout and publication evidence

[PR182_BEFORE.json](PR182_BEFORE.json) preserves the previous PR
title, body, head, base and draft state. The branch and PR were
freshly read at the parent before publication.

[CHECKOUT_VALIDATION.json](CHECKOUT_VALIDATION.json) is copied from
the five-command repository-integrity gate in a clean complete
local science checkout. Its named commit and tree are the actual
gate inputs. The copied receipt and
[SOURCE_BINDING.json](SOURCE_BINDING.json) are the only files added
after that science-tree gate; neither claims to contain its own
eventual publication SHA.

The binding records every science-tree file and verifies that all
647 parent files, including all 60 earlier Lean files, are unchanged.
Publication constructs a single child of the expected remote head,
compares its tree with the complete local tree, and advances the
branch without force. A freshly fetched published checkout receives
the same five-command integrity gate and file-binding check.

The published-checkout receipt and fresh remote/PR identity are
recorded in the PR outside this noncircular in-tree chain. The local
science and receipt commits remain preserved on a checkpoint branch.
Repository integrity verifies files and frozen records; the
mathematical evidence is supplied by the separate proofs, reviews,
formal compilation and controls above.

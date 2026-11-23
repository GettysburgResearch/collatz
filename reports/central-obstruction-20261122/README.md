# Published execution: direct central-obstruction attempts

**PASS.** The isolated replay ran in a fresh complete checkout of the actual
GitHub mathematical commit
`082a9d4be6717d1bb956394bacf6a63c8d4ed8e4`, tree
`b95794eaa39a640eda5b924eceb9ec063b7662df`.

| Evidence | Result |
|---|---|
| Tracked files present; clean before and after | 608 / PASS |
| Required Lean dependency closure | 7 modules / PASS |
| New public theorem axiom audits | 18 / PASS |
| Compiler policy | Lean 4.34.1, one worker, warnings as errors |
| Permitted transitive axioms | `propext`, `Classical.choice`, `Quot.sound` |
| Exact negative-shadow checks | Normal and optimized Python / PASS |
| Damaged negative-shadow controls | Four rejected in each mode |
| Full-denominator cycle controls | Four words, 29 transfers, all rotations and original-source lifts; both Python modes / PASS |
| Default repository gate | Five subprocesses / PASS |
| Recorded mathematical/execution inputs | 23 SHA256 bindings |
| Executed commands | 21, all exit code zero |

The [complete receipt](published-replay.json) has SHA256
`4ff71e6ac093c2fbcec8d0f16984e13c9ab73e425de9e3bd683ebc37bb684f20`. Its original log paths identify the execution workspace;
the same byte-for-byte logs are retained under [published-logs](published-logs/).
The [module-port patch](module-port.patch) records the inherited header-only
compatibility edits. All proof bodies are retained from the recorded inputs.

The two new source files are `HeadThreeNegativeCycle.lean` and
`ExtremalSourceClock.lean`. The former has ten audited declarations and the
latter eight. The all-parameter modular completion of the negative-shadow
family and the all-certificate extremal-source maximality argument remain
written proofs; they are not added to the Lean count. The escape and general
cycle lanes produced failed-closure records, not universal exclusions.

## Independent review before publication

The independent negative-shadow review reconstructed the arithmetic and
compiled the new module against previously replayed dependencies. Its exact
source hash, axiom audits and finite controls are recorded in
[negative-shadow-independent-review.json](negative-shadow-independent-review.json)
and [negative-shadow-review-lean.log](negative-shadow-review-lean.log).
The [original review worksheet](review_negative_shadow.py.txt) is preserved
as executed; its local author-checkout paths are historical context, not a
portable replay command. The separate extremal-clock review checked the
written all-certificate grade bound and the ordinary target trajectory.

## Replay scope

Use `research/central-obstruction-20261122/check.py` with the runtime paths
specified in the scientific packet. This replay recompiles the new modules
and their actual five-module dependency closure. Pinned compiled Mathlib and
external libraries were reused. Unrelated earlier research packets were not
re-executed or relabeled as fresh verification.

This receipt is added by a subsequent reports-only commit. Its mathematical
head remains the actual commit named above. No report claims a Collatz proof.

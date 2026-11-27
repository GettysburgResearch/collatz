# Fresh full replay of the full-proof-attempt packet

**PASS within the stated scope. Universal Collatz remains unproved.**

## Frozen source and toolchain

- Scientific commit: `966ddadb86240ac3c2cecf551bb682738d11f03b`.
- Exact tree: `0b036071e5f59c6a2e15cb1b41f261f3a524713d`; 903 tracked files in the clean complete checkout.
- Execution: `2026-11-25T16:50:23.335885+00:00` through `2026-11-25T16:51:26.088909+00:00`.
- Lean: `Lean (version 4.34.1, x86_64-unknown-linux-gnu, commit 5045d0056413266e57c625dcd7c365b10e377c52, Release)`.
- Mathlib: `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Every one of the six new modules and both project dependencies was rebuilt in a new empty object directory. Only the pinned Lean/Mathlib dependency objects were reused.

[Machine-readable receipt](fresh_replay/receipt.json) records the commands, exit codes, durations, hashes, exact transitive axioms and unchanged source manifest. The 20 manifest entries cover all 17 research-packet files, the two exact older dependencies and the independently written chart-replay program.

## Lean evidence

All **24 new public declarations** and **23 dependency declarations** passed, for **47 named transitive axiom audits**. Compiler arguments included `-j1 -DwarningAsError=true -DautoImplicit=false`. Every public theorem was audited exactly once. No project proof contains `sorry`, `admit`, a custom `axiom`, or `native_decide`. Every returned axiom set was contained in `propext`, `Classical.choice`, and `Quot.sound`.

| New module | Public declarations | Checked mathematical scope |
|---|---:|---|
| `transport/SignedPrefix.lean` | 9 | Signed ordinary lifts, literal meetings, constructed upper certificates and explicit periodic-center height bounds |
| `transport/CanonicalSuffix.lean` | 3 | Canonical-slice simultaneous endpoints, retention of each supplied hit suffix and sufficient height contraction |
| `transport/NoEarlyDrop.lean` | 2 | Infinite integer family identity and exact first-upper-hit/lower-growth theorem |
| `cycle/ExcursionBudget.lean` | 4 | Clipped high-clock budget and whole-power terminal congruence/injection |
| `global/ParitySeries.lean` | 3 | One-step, finite weighted telescope and coefficient identities |
| `global/RationalModel.lean` | 3 | Ordinary parity separation, constant height on a component and finite Noetherian height range |

The dependencies are `SourceDeletion.lean` (8 declarations) and `MinimumFailure.lean` (15). This pass did not claim a rebuild of all older research Lean files in the repository.

## Exact finite controls

Every one of the following four scripts ran successfully in both normal and optimized Python. Each pair had byte-identical stdout and stderr, and no Python `assert` statement was used for its guards.

- **Transport:** 16,733 short-clock sources, with at most 6,509 observed clocks to a hit or the specified drop; 158 symbolic direct-drop rows, one ancestor row, and 173 comparison pairs. Exactly 91 of the 1,134 comparison-grid pairs remain. This finite arithmetic does not prove a universal selector.
- **Independent physical transport replay:** 2,086 actual lower/upper comparisons at clocks 1600 through 2571; exactly 1,043 distinct `(e,H mod 486)` pairs covered. Every tested replacement was smaller, had a common lower endpoint, and supplied the stated new upper odd count.
- **Cycle:** 30,012 ordinary windows, 105,231 high endpoints counted with multiplicity, 11,714 repeated-word terminal congruences; exact entropy-margin inequalities and all local block edges at `(p,h)=(41,65)` and `(306,485)`. Only the latter finite block count exceeds the asymptotic comparison threshold, as allowed by the statement.
- **Global:** 16,384 exact prefix identities and dyadic divisibility checks; full rational fitting-matrix ranks for degrees zero through four on 40 distinct observations of the source 27; two expanding six-bit physical blocks with carries 287 and 211 and 16 positive lifts each below 1025.

[Raw transport output](fresh_replay/python-transport-check_transport.stdout.log) · [Independent chart output](fresh_replay/python-cycle-review_chart_paths.stdout.log) · [Cycle output](fresh_replay/python-cycle-check.stdout.log) · [Global output](fresh_replay/python-global-check.stdout.log).

## Repository validation and publication boundary

The clean complete scientific checkout ran `python -X utf8 -B tools/validate.py --regressions` successfully. All **11 validator commands** returned zero. The checkout commit, tree, source hashes and clean status were unchanged afterward. [Validator receipt](fresh_replay/repository-validation.json) · [Full validator stdout](fresh_replay/repository-validation.stdout.log).

The receipt follow-up adds reports and replaces this staging status. All 20 science/dependency/control hashes were compared against the scientific replay before preparing that follow-up. The final branch head and the result of its separate clean-checkout validation are recorded in the PR description after publication. The preceding PR description is preserved in [PREVIOUS_PR_DESCRIPTION.json](PREVIOUS_PR_DESCRIPTION.json).

## Limits of this evidence

The compiler checks the listed theorem statements under their actual hypotheses. It does not prove that every ordinary source satisfies the replacement, model or Mahler hypotheses. The infinite entropy, rational-variety instantiation, finite-fit and analytic arguments have written proof and independent-review scope. The Adamczewski–Bell–Smertnig lifting theorem and Wu–Wang estimate are external inputs; the stronger Chudnovsky constants remain source-qualified. No external Lean development was rebuilt. The validator checks repository integrity and bounded regressions, not the truth of Collatz.

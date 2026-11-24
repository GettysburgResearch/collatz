# Verification scope

The completed packet has five Lean modules and four Python control programs. The coordinator and independent lanes compiled the elementary proofs with Lean 4.34.1, treating warnings as errors. `MinimumFailure.lean` imports the newly built `SourceDeletion` object and defines the actual existential basin of 1. `SecondRun.lean` imports the newly built minimum and first-exit modules to prove a further actual-basin contradiction. These are not assumptions about a symbolic coloring substituted for convergence.

Every public theorem has a named axiom audit. The only permitted transitive axioms are `propext`, `Classical.choice` and `Quot.sound`. No unchecked proof placeholder, added axiom, or native decision escape is permitted. Private lemmas are kernel checked and included transitively in the public audits.

`replay.py` is the authoritative coordinator replay procedure. It requires a clean complete checkout, builds fresh objects for all five new modules in dependency order, checks that every public theorem is audited, and runs each new control program in ordinary and optimized Python with byte-identical output and zero AST assertions. It then runs the repository validator and checks that the science bytes, commit, tree, and checkout cleanliness remain unchanged. Existing pinned Lean/Mathlib dependencies are reused. Earlier unchanged research modules and upstream PR tables are not claimed as rebuilt by this continuation.

The first four-module scientific commit `e5c1e8d3e5635afca4121118bd1d44ab9fc862bc`, tree `ae8116f5d01460ea2401ad44dd6a1b10b7c3677d`, was fetched into a clean complete 697-file checkout and actually replayed: 45 public theorem audits, three identical normal/optimized control pairs, and all five repository-validator commands passed. [The exact initial receipt](initial_replay.json) records that execution. The final lane then supplied the second-run proof; the complete five-module packet is replayed again at its own exact scientific commit before publication.

## Completed final scientific replay

The complete scientific commit is `f4453eff99bf9d0315404c6931e1c70e5c93cefe`, tree `84f47c53bf48896050746c785e7a7aa4e9a923de`. It was fetched and checked out cleanly with all 701 tracked files. The real replay finished successfully on 2026-11-24, with fresh objects for every new module and unchanged science hashes, commit, tree and checkout state.

| Module | Public theorem audits |
|---|---:|
| `SourceDeletion.lean` | 8 |
| `CarryDescent.lean` | 11 |
| `MinimumFailure.lean` | 15 |
| `UpperRepresentative.lean` | 11 |
| `SecondRun.lean` | 1 |
| Total | 46 |

All 46 passed with warnings treated as errors and only the permitted standard axioms. All four Python controls passed in ordinary and optimized modes with identical stdout/stderr and zero AST assertions. The arithmetic control covers 100,000 starting values and 4,097 affine parameters; the descent control covers 40 reference pairs, 8 affine lifts, 32 exponent congruences, 528 stable reductions and 670 adaptive valuation cases; the first-exit control covers 2,049 lifts per fixed family and 2,292 adaptive exit cases; the second-run control checks 1,027 merger examples and 171 prescribed CRT valuation pairs. These finite controls support the exact symbolic proofs and do not stand in for universal coverage.

The five required repository-validator commands all passed. The validation was the standard integrity gate, with optional bounded regressions disabled; it was not represented as a full mathematical verification of old research. [Full replay receipt](fresh_replay/receipt.json), [repository validation](fresh_replay/repository-validation.json), and the adjacent stdout/stderr logs contain exact command lines, compiler identity, dependency commit, source hashes and execution times. [Publication binding](PUBLICATION.json) links the replay to its scientific commit.

Author and peer checks are separately preserved under `arithmetic/`, `descent/` and `renewal/`; their narrower scopes and exact hashes remain authoritative for those executions. Earlier unchanged source files retain their old verification records. This receipt follow-up changes reports only.

Mathematical scope: the table, bounded induction, least ordinary disagreement and its basin orientation, finite paired affine rows, and the parameterized first-exit identities are kernel checked. The asymptotic arithmetic-progression consequence and the assembly with the earlier canonical source are written arguments with independent reviews. None of these checks proves a successful descent for every remaining source.

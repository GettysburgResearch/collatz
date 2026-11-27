# Fresh complete-checkout verification

**PASS for the named scope. No complete Collatz proof is claimed.**

The science checkpoint is `850a508b7d081ab74d6f2995b4225d8d54daded8`, tree `54df23cbebe1f22fb0ac890d8f8c27c0f9a9c62b`, containing 969 tracked files. It was fetched into a new clean complete checkout. The replay started at 2026-11-25 17:37:40 UTC and finished at 17:38:36 UTC. The report-only publication child preserves every one of the 17 manifest source hashes.

## Lean

- Lean 4.34.1, compiler commit `5045d0056413266e57c625dcd7c365b10e377c52`.
- Mathlib commit `d13f23b723b8a846827a245b89c10fc7d3f11612`.
- Strict flags `-j1 -DwarningAsError=true -DautoImplicit=false`.
- Four new modules, 22 new public theorem audits.
- Two exact project dependencies, 23 additional public theorem audits.
- All six project modules compiled into a newly created empty object directory. Only the pinned Lean/Mathlib dependency objects were reused.
- Every public theorem has exactly one named audit. All 45 reported axiom sets are subsets of `propext`, `Classical.choice`, and `Quot.sound`. No `sorry`, `admit`, custom axiom or `native_decide` occurs in the checked proof sources.

## Finite controls and integrity

All four controls ran both normally and with Python `-O`; each pair had byte-identical stdout and stderr. Their guards do not disappear under optimization.

| Control | Exact finite coverage |
|---|---|
| Cycle | 728 small-source hits, 32 residue classes, 1,260 ordinary windows, 3,327 inverse leaves and 22 paired minimum tests |
| Transport | 3,840 descent/carry cases, 1,536 supported carry identities, four canonical exponent representatives |
| Independent inverse-cost census | Every residue compared with an independent composition enumeration through depth 6; every native binary word through depth 17 |
| Independent trit cylinders | All 81 suffixes, four ordinary lifts including a very large lift, three common deadlines: 972 checks |

`python -X utf8 -B tools/validate.py --regressions` completed all 11 commands successfully in that complete checkout. Source hashes, commit, tree and checkout cleanliness were unchanged after replay. Repository integrity is not mathematical verification of the written infinite arguments.

## Receipts and publication

[Machine replay receipt](fresh_replay/receipt.json) lists all command arguments, return codes, log hashes, source hashes, object hashes and 45 axiom audits. [Repository validator receipt](fresh_replay/repository-validation.json) records its complete command outputs and checkout identity. All raw stdout and stderr files are in [fresh_replay](fresh_replay/). [Replay driver](replay.py)

The former PR description is preserved in [PREVIOUS_PR_DESCRIPTION.json](PREVIOUS_PR_DESCRIPTION.json). The owned branch publication is a fast-forward with an expected-head lease. The final publication head and separate report-only complete-checkout validation are recorded in the updated PR description after those operations complete.

The grid asymptotics, unrestricted-height opening assembly and cycle counting assembly remain written proofs with independent mathematical reviews; this receipt does not represent them as new Lean theorems. The unresolved universal steps are in [FINAL_PROPOSAL.md](../../research/astra-diagonal-closure-20261125/FINAL_PROPOSAL.md).

# Publication and verification record

The fifth continuation adds the arithmetic, head and renewal packets to the existing research PR195. **Collatz remains open.** The external Diophantine and probability inputs remain written, source-qualified dependencies. The local Lean evidence covers twenty selected finite declarations.

| Checkpoint | Identifier |
|---|---|
| Prior published head | `b69ec87d28f539233a32b7c07964f5605320eb71` |
| Local scientific commit tested before publication | `c9bd9002c265fd205f6ce4cb1cc6a44234c81885` |
| Published scientific commit, subsequently fetched and tested | `ff292324e07819a813e9d6df64186347960e98ef` |
| Identical scientific tree | `45e38b6239c1bac44f4feee80d72b58704e52754` |
| Complete scientific checkout | 580 tracked files |
| Scientific additions in this continuation | 37 files |
| Entries matched in the prepublication source/review manifest | 36 |

The owned branch `research/astra-global-closure-20261124` was advanced without force, with its previous head supplied as the expected value. The remote tree exactly matched the locally tested tree. The remote commit was then fetched, checked out in a complete clean worktree, and passed all five default commands in `python -X utf8 -B tools/validate.py`. The checkout remained unchanged. The [published-science receipt](published-science-validation.json) records that actual remote commit and tree.

[Fresh Lean evidence](lean/receipt.json) records Lean 4.34.1, Mathlib `d13f23b723b8a846827a245b89c10fc7d3f11612`, the runtime hash, fresh project compilation, warnings as errors, all twenty selected axiom reports, source hashes and compiler logs. The root reused only the provisioned Mathlib/package objects. No external formalization archive was rebuilt.

[Paired finite replay](controls-replay.json) records all three control scripts in normal and optimized Python, six passing runs with matching outputs and explicit checks active under optimization. The bounded arithmetic includes 6,485 physical words and six complete high-degree mask constructions. The head control retains 134,144 profile-continuation checks on original grids. The inverse control covers 49,149 positive ordinary lifts and its declared finite central-row census. These are finite evidence, separate from the proposed asymptotic proofs.

This publication-only follow-up adds this record and the fetched scientific-checkout receipt. It changes no mathematical source, Lean source, control, or independent review. The final receipt commit and its clean-checkout validation are read back after publication and recorded in the PR description. The [source manifest](SOURCE_HASHES.json) retains its explicit prepublication boundary.

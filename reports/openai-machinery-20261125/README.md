# Review and execution record

The scientific entrypoint is [the connected proof packet](../../research/openai-machinery-20261125/README.md). This directory records evidence and its limits.

## Source and review boundaries

[SOURCE_PINS.json](SOURCE_PINS.json) freezes the release, Collatz baseline and relevant PR heads. Three GPT-6.2 Astra reviewers worked on complementary tensor, Fourier and arithmetic/clock tracks, then independently checked one another's outputs. The reviews identify specific statements, original interfaces and hashes. They do not approve every assertion in the upstream OpenAI release or every program in the source PRs.

| Record | Independently checked content |
|---|---|
| [FOURIER_REVIEW.md](FOURIER_REVIEW.md) | Endpoint-rank identity, initial and all-row merger constructions, and the native PR192 adapter; separate Lean recompilation and ordinary replays. |
| [CLOCK_REVIEW.md](CLOCK_REVIEW.md) | PR192 bytes and predicate, exact higher first odd core, actual even merger endpoint, and the existential coverage limit. |
| [TENSOR_REVIEW.md](TENSOR_REVIEW.md) | Ordinary Fourier collision construction and filters, plus clock row/index/height claims and the pinned PR207 comparison. |
| [LP_REVIEW.md](LP_REVIEW.md) | Farkas signs and support, residue obstruction, exact certificate checker, and independent exhaustive comparison on 19,683 three-vertex signed graphs. |

## Evidence tiers

The combined Lean checker compiles all connected local modules, checks the 14 frozen source hashes and prints axiom dependencies for 46 local public theorems and seven imported interfaces. Standard `propext`, `Classical.choice` and `Quot.sound` are allowed. A fresh build of this packet may reuse the pinned Mathlib cache; it is not a fresh build of all Mathlib or of OpenAI's headline theorems. The standalone clock checker additionally compiles its six frozen dependencies and clock module from fresh objects without Mathlib.

[FINITE_REPLAYS.json](FINITE_REPLAYS.json) contains the actual outputs and input hashes for the Fourier, LP and clock controls, with byte-identical normal and optimized Python results. These validate finite exact examples and checker behavior. The infinite-family inequalities come from the stated Lean or written proofs, not extrapolation from those examples.

The generic `tools/validate.py` receipt concerns complete-checkout structure, frozen identities and integrity controls. It is separate from mathematical proof and bounded numerical evidence.

## Completed execution

The full packet was rebuilt in a fresh complete checkout at local science commit `9e8df902e063004eec23d9ddf6492e88f63e89b1`, tree `27119d6f9361d6b2d0383484c81ad6cc3c4329a1`. No packet build objects were copied. The nine pinned dependency package checkouts and their Mathlib binary cache were reused; the checker independently read their actual Git revisions and matched every one to the manifest.

* [LEAN_FRESH.json](LEAN_FRESH.json): successful fresh connected build, 14 frozen sources, 53 declaration audits, and exact new Lean source hashes. The only permitted axiom dependencies were `propext`, `Classical.choice` and `Quot.sound`. One frozen-source deprecation warning is retained in the build output.
* [CHECKOUT_SCIENCE.json](CHECKOUT_SCIENCE.json): successful clean, complete checkout validation, including all five required integrity commands. This receipt identifies the input before the execution-record files were added.
* [FINITE_REPLAYS.json](FINITE_REPLAYS.json): five Fourier collision controls; three LP paths, five obstructed residue graphs, fifteen corrupted certificates and five type/projection controls; and clock dynamic programming through depth 64 with full-period direct ordinary enumeration through depth eight. Normal and optimized outputs match exactly.

The public-theorem counts include elementary helpers and concrete controls. They measure audit coverage. They are not a claim of 46 independent advances toward Collatz. The written collision asymptotic and upper Banach density deduction have their own written proofs and review boundaries; the finite replays do not formalize them.

After the fresh proof build, final prose review restored two explicit hypotheses in the summary: balanced-prefix crossing requires `b>0`, and the feedback rank bound requires invertibility of `I−C` and common injection/readout. The Lean statements already contained them. No mathematical source changed after this fresh build. A final complete-checkout validation and remote head/tree readback are reported in the publication PR.

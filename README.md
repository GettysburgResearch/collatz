# Gettysburg Research: Collatz

> **Status: UNSOLVED.** This repository contains no accepted proof or disproof of the Collatz conjecture, no accepted divergent positive orbit, and no accepted nontrivial positive cycle.

This is an open research laboratory for developing, checking, refuting, and connecting approaches to Collatz. `main` contains a mixture of:

- **integrated knowledge**: narrow statements with readable proof packets, exact provenance, and independent-review records;
- **active research**: proposed theorems, computations, constructions, literature work, and failed approaches whose status remains explicit;
- **backstage evidence**: frozen snapshots, review-wave ledgers, machine registries, and lifecycle records retained for auditability.

A metadata record is not a substitute for a proof body. A reviewed theorem is not a proof of Collatz. A long finite computation is not an all-depth argument.

## Two-minute orientation

1. Read [`START_HERE.md`](START_HERE.md) for the project map and the minimum notation.
2. Read [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md) for what is actually established, refuted, source-qualified, or still awaiting local proof completion.
3. Read [`FRONTIERS.md`](FRONTIERS.md) for the load-bearing open problems and the smallest missing lemmas.
4. Agents should then read [`AGENTS.md`](AGENTS.md); human contributors can use [`CONTRIBUTING.md`](CONTRIBUTING.md).

The archival integration and PR-lifecycle material is indexed under [`archive/`](archive/README.md). It is deliberately not the newcomer path.

## The mathematical map

The current work is organized around five interacting programs.

| Program | What is established here | Main unresolved boundary |
|---|---|---|
| **Ordinary extraction and completion** | Compatible finite cylinders determine a 2-adic point; an ordinary integer exists exactly when canonical representatives stabilize on an ordinary boundary face. A bounded nested least-root sequence is exactly the missing compactness principle. | Prove boundedness or escape for a concrete aperiodic architecture. |
| **Periodic tails and cycles** | A periodic parity tail has a unique rational 2-adic realizer controlled by the complete denominator `2^L-3^s`; a positive ordinary eventual period must enter a positive cycle. | Exclude every nontrivial positive cycle or produce and replay one exact word. The integrated synthesis still needs a narrow wording review. |
| **Coefficient stopping / SC\*** | All-time coefficient-supercritical positive orbits diverge to `+infinity`; escape of the least all-supercritical sources is equivalent to universal finite coefficient stopping. | Prove the fixed-source valuation bound that makes every positive source cross. |
| **First crossing / FC\*** | Reviewed reductions place cycles and non-descending first crossings into a common complete-denominator problem. | Exclude every complete first-crossing realization with one common displacement, not merely factors or bounded subclasses. |
| **Automata, rigidity, and representation limits** | Cofinite finite-horizon automata have a spurious terminal SCC; finite affine/rational self-sections and semilinear sanctuaries fail in the reviewed six-branch chart; one unrestricted factor-complexity screen is refuted and repaired. | Find an unbounded-state or genuinely nonsemilinear mechanism, or prove direct height escape. |

The detailed dependency map is in [`CURRENT_KNOWLEDGE.md`](CURRENT_KNOWLEDGE.md). New connections are welcome, but any connection not already reviewed is labeled **PROPOSED**.

## Strongest narrow results now readable on `main`

The first integrated proof packets live under [`research/integrated/`](research/integrated/README.md):

- ordinary extraction by signed residue stabilization and bounded nested minima;
- the explicit `(1110)^∞` completion ghost;
- periodic tails and complete-denominator divisibility, with the synthesized integrated wording still pending narrow review;
- coefficient-supercritical divergence and the exact SC\* equivalence;
- the fixed-depth cofinite-tail automata obstruction;
- finite affine/rational six-branch rigidity and the semilinear-sanctuary obstruction;
- the exact refutation of the unrestricted factor-complexity screen and its separate nonconstant repair.

These are valuable, but each is much narrower than Collatz.

## Three boundaries that must never be collapsed

1. **Finite compatibility:** every finite prefix has positive integer representatives.
2. **2-adic completion:** compatible prefixes determine one point of `Z_2`, possibly negative or nonordinary.
3. **One positive ordinary all-time trajectory:** one fixed positive integer realizes every depth and the physical dynamics forever.

Likewise, distinguish:

- a full proof from a proposed proof;
- an inspected artifact from an independently replayed computation;
- a proper-factor congruence from complete-denominator divisibility;
- a theorem at one exact SHA from later branch additions;
- a refuted statement from a separately reviewed repair.

## Where work goes

- Put stable, reviewed mathematics in `research/integrated/` through a small manifest and exact provenance.
- Put free-form exploration in an existing `research/`, `experiments/`, `literature/`, or `reports/` area, or open a focused new area.
- Put frozen integration evidence and lifecycle history behind the [`archive`](archive/README.md) index.

Exploration does not require a registry form. Promotion does require an exact statement, scope, source SHA, dependencies, review evidence, and honest computation status.

## Current strategic bridge

`SC* + FC* => Collatz` remains a **PROPOSED repository-level bridge**. Its reviewed ingredients are promising, but the exact normalization and coverage crosswalk has not yet been independently accepted as one theorem. See [`FRONTIERS.md`](FRONTIERS.md#proposed-sc--fc-bridge).

Be imaginative in discovery, precise in status, and uncompromising about ordinary-integer, complete-denominator, and finite-to-infinite boundaries.

# Integrated reference and roadmap records

> **Collatz remains unsolved.** Repository residency and mathematical status are separate.

Machine-readable detail is in [`registry.json`](registry.json). Readable proofs are under [`../research/integrated/`](../research/integrated/README.md). The wider reviewed research record is in [`../research/RESULTS_CATALOG.md`](../research/RESULTS_CATALOG.md).

## Integrated records

| ID | Mathematical status | Repository status | Proof/dependency residency | Scope summary |
|---|---|---|---|---|
| [`IC-EXTRACT-001`](../research/integrated/ordinary-extraction/README.md) | `VERIFIED` | `accepted_with_local_proof` | local | Abstract residue stabilization and bounded nested minima; no concrete architecture is decided. |
| [`IC-GHOST-001`](../research/integrated/completion-ghost/README.md) | `VERIFIED` | `accepted_with_local_proof` | local | Explicit `(1110)^∞` completion ghost; not a positive orbit. |
| [`IC-PERIODIC-001`](../research/integrated/periodic-tails/README.md) | `SOURCE-QUALIFIED`; component statements verified, integrated synthesis pending narrow review | `accepted_reference_record` | local component proofs / mixed synthesis boundary | Raw parity tails or symbols already compiled to fixed parity blocks; complete denominator and exact replay. |
| [`IC-SC-001`](../research/integrated/coefficient-stopping/README.md) | `VERIFIED` | `accepted_with_local_proof` | local | Fixed-source coefficient stopping and divergence classification; SC\* remains open. |
| [`IC-AUT-001`](../research/integrated/finite-safety-automata/README.md) | `VERIFIED` | `accepted_with_local_proof` | local | Fixed-depth LSD-first cofinite safety language only. |
| [`IC-RIG-001`](../research/integrated/six-branch-rigidity/README.md) | `VERIFIED` | `accepted_with_local_proof` | local | Exact six-branch chart under complete-tree, full-tail, finite-control, and eventual-integrality hypotheses. |
| [`IC-REF-001`](../research/integrated/factor-complexity/README.md) | `REFUTED` source statement; exact refutation accepted | `accepted_with_local_proof` | local | Unrestricted `PR37:T-9318` screen only. |
| [`IC-REP-001`](../research/integrated/factor-complexity/README.md) | `VERIFIED` separate repair | `accepted_with_local_proof` | local repair proof; PR #16 dependencies source-pinned | Nonconstant words in the reviewed induced `64→81` model. |

### Non-equivalences that must remain visible

- `IC-REF-001` and `IC-REP-001` are not two statuses of one theorem. The original is false; the repair is a different theorem.
- `IC-PERIODIC-001` does not inherit `VERIFIED` for its exact synthesis merely because its component theorems passed.
- `IC-RIG-001` is not a generic statement about finite or rational Collatz representations. Its exact chart and complete-tree/full-tail/finite-control/eventual-integrality assumptions are load-bearing.
- Local proof residency is not a new independent review.

## Roadmap records

| ID | Status | Exact obligation |
|---|---|---|
| `RD-SC-001` | `OPEN`, `roadmap_accepted` | Prove universal finite coefficient stopping for every fixed positive source, equivalently least all-supercritical source escape. |
| `RD-FC-001` | `OPEN`, `roadmap_accepted` | Exclude every complete nontrivial first-crossing realization with one common `d≥0`, the entire denominator, all prefix inequalities, compatible source/end quotients, and exact replay. |
| `RD-BRIDGE-001` | `PROPOSED`, `roadmap_accepted`, exact wording pending narrow review | Establish the least-counterexample normalization/crosswalk under which SC\* and FC\* cover all counterexample cases while explicitly allowing the trivial cycle. |

Use **“principal proposed roadmap bridge”**, not **“established exhaustive reduction,”** until `RD-BRIDGE-001` passes its narrow review.

## Evidence boundary

- A bounded experiment remains bounded evidence.
- An inspected large computation is not an independently replayed computation.
- A theorem at one source SHA does not cover later branch additions.
- A proper-factor congruence is not complete-denominator closure.
- A compatible 2-adic point is not automatically an ordinary positive trajectory.

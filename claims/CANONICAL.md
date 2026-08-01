# Candidate canonical and roadmap records

**Snapshot:** `2026-08-01-first-major-integration`  
**Continuation:** `2026-08-02-lifecycle`  
**Repository status:** PR #84 is an unmerged draft. Every `IC-*` record below is `candidate_in_draft_pr`; every `RD-*` record is `roadmap_candidate_in_draft_pr`. None is accepted on `main` yet.

Underlying mathematical statuses remain exact-SHA scoped. `integration_status` names the intended role; `promotion_state` names repository acceptance; `proof_residency` records whether the proof body is local or still only at frozen source commits.

## Promotion rule

- `candidate_in_draft_pr` becomes `accepted_reference_record` only after independent review and merge of PR #84, subject to each record’s narrow review gate.
- `accepted_reference_record` does not mean the proof body is on main.
- `accepted_with_local_proof` requires the proof-import plan to be completed.
- A roadmap record may be accepted while its obligation remains open.

Machine-readable detail: [`registry.json`](registry.json). Proof plan: [`../docs/integration/2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md`](../docs/integration/2026-08-02-lifecycle/PROOF_IMPORT_PLAN.md). Reviewer checklist: [`../docs/integration/2026-08-02-lifecycle/PROMOTION_AUDIT.md`](../docs/integration/2026-08-02-lifecycle/PROMOTION_AUDIT.md).

## Candidate canonical records

| ID | Mathematical status | Promotion | Proof residency | Scope summary |
|---|---|---|---|---|
| `IC-EXTRACT-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | Compatible nested-modulus residue chains and nested positive survivor sets. This is an extraction theorem, not a theorem that any particular Collatz-derived survivor set is nonempty or bounded. |
| `IC-GHOST-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | An explicit parity-cylinder countermodel to compactness, drift and finite-prefix extrapolation. |
| `IC-PERIODIC-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | Raw parity words, or accelerated/controller symbols only after each repeated symbol is proved to emit one fixed finite parity block. |
| `IC-SC-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | Fixed ordinary sources and canonical all-supercritical cylinders. |
| `IC-AUT-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | The fixed-depth LSD-first canonical safety language defined in PR #14. |
| `IC-RIG-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | The exact six-branch chart of PR #64 under the reviewed full-tail, finite-control and eventual-integrality hypotheses. |
| `IC-REF-001` | `refuted` | `candidate_in_draft_pr` | `frozen_source_reference` | The exact unrestricted screening statement at PR #37 frozen head. |
| `IC-REP-001` | `verified` | `candidate_in_draft_pr` | `frozen_source_reference` | Nontrivial ordinary 64→81 survivors and nonconstant binary words in the reviewed centered-cylinder model. |

### Statements and review gates

#### `IC-EXTRACT-001` — Canonical-residue stabilization is the ordinary-extraction criterion

**Candidate statement.** Let nested dyadic cylinders have compatible canonical least representatives R_n. A nonnegative ordinary integer lies in every cylinder exactly when R_n is bounded, equivalently eventually constant. For nested nonempty positive survivor sets, bounded least roots are likewise equivalent to eventual constancy and yield one positive all-depth ordinary survivor. The signed negative boundary is represented by eventual maximal appended blocks, not by bounded least representatives.

**Independent PR #84 review gate.** Confirm that the candidate summary is exactly the conjunction of PR57:L-7601 and PR57:T-7601, with no strengthened positivity or nesting quantifier.

**Source aliases.** `PR57:L-7601`, `PR57:T-7601`, `PR3:T-0043`, `PR56:T-7801`, `PR60:T-7401`

**Evidence boundary.** Proof: independently reconstructed. Artifact: not applicable; symbolic theorem.

**Repair/provenance.** PR #57's signed decomposition is the selected primary source. Alternatives remain branch-qualified; no source file is silently renamed.

#### `IC-GHOST-001` — Finite positive representatives do not force an ordinary all-depth point

**Candidate statement.** The periodic parity block 1110 has affine fourth iterate T^4(x)=(27x+19)/16 and unique periodic 2-adic realization -19/11. Every finite prefix cylinder has infinitely many positive ordinary representatives, while the all-depth completion is nonintegral and negative in the real order.

**Independent PR #84 review gate.** Verify the exact 1110 specialization and the distinction between Z_2, ordinary Z and positive ordinary realization.

**Source aliases.** `PR57:T-7602`

**Evidence boundary.** Proof: independently reconstructed. Artifact: small exact replay reported; no expensive computation.

#### `IC-PERIODIC-001` — Periodic parity tails are controlled by the complete denominator

**Candidate statement.** For a nonempty binary word w of length L with s one-bits and affine constant C_w, the periodic tail w^infinity has the unique 2-adic realizer x_w=C_w/(2^L-3^s). If 3^s>2^L then x_w<0. If 3^s<2^L and s>=1, then x_w is a positive integer exactly when 2^L-3^s divides C_w, in which case exact parity replay gives a positive cycle. The all-zero word is the separate endpoint x_w=0. Consequently, every positive ordinary eventually periodic parity tail enters a positive cycle.

**Independent PR #84 review gate.** **REQUIRED:** independently review the synthesized corrected statement, including the all-zero endpoint, full denominator, finite preperiod and fixed-block controller scope.

**Source aliases.** `PR61:T-7401`, `PR62:T-7701`, `PR63:L-7501`, `PR63:T-7501`

**Evidence boundary.** Proof: component theorems independently reconstructed; synthesized wording needs narrow review. Artifact: X-7710 small exact audit passed; not an expensive search.

**Repair/provenance.** The candidate statement is a new corrected integration synthesis. It does not retroactively change the frozen PR #61 or PR #63 verdicts.

#### `IC-SC-001` — Coefficient-stopping finiteness is equivalent to escape of least all-supercritical sources

**Candidate statement.** Let m_N^sup be the least positive source whose first N coefficient prefixes are all supercritical. Then m_N^sup tends to infinity exactly when every fixed positive integer has finite coefficient stopping time. Moreover, an ordinary positive orbit whose every prefix remains coefficient-supercritical diverges to +infinity.

**Independent PR #84 review gate.** Verify the terminology wrapper, fixed-source quantifiers and that the record does not state SC* itself as proved.

**Source aliases.** `PR77:T-6709`, `PR77:T-6710`, `PR77:L-6711`

**Evidence boundary.** Proof: independently reconstructed. Artifact: symbolic; no large computation.

**Repair/provenance.** The candidate wording incorporates the review's terminology repair and does not extend the verdict to current PR #77 M-6712.

#### `IC-AUT-001` — The finite canonical-tail safety SCC is a cofinite artifact

**Candidate statement.** For each fixed safety depth d in the PR #14 reverse-tree language, the forbidden set is finite, the safe language is cofinite, and the minimal complete DFA has exactly one cyclic SCC: the terminal two-state canonical tail. Removing that SCC leaves a DAG; the exact power-of-two witness shows nonclosure. No cofinite forward-invariant set can exclude {1,2}.

**Independent PR #84 review gate.** Structural review only: preserve fixed-depth, LSD-first canonical-language and empty-continuation conventions.

**Source aliases.** `PR14:D-9201`, `PR14:L-9201`

**Evidence boundary.** Proof: independently reconstructed. Artifact: bounded automaton artifact inspected; theorem does not extrapolate it.

#### `IC-RIG-001` — Finite tame sections cannot self-replicate the reviewed six-branch chart

**Candidate statement.** For the fixed rational chart P=3^12, Q=2^19 and its six reviewed digits: the only full-tail finite integer-affine section nucleus is the original expanding forward map; the same holds for finite rational-function nuclei after eventual integrality; and the all-depth survivor contains no infinite arithmetic progression or semilinear forward-invariant sanctuary.

**Independent PR #84 review gate.** Confirm that the candidate packet is exactly the conjunction of PR64:D/L/T-7401–7404 and preserves complete-tree/full-tail, finite-control and eventual-integrality scopes.

**Source aliases.** `PR64:D-7401`, `PR64:L-7401`, `PR64:T-7401`, `PR64:T-7402`, `PR64:T-7403`, `PR64:T-7404`

**Evidence boundary.** Proof: independently reconstructed. Artifact: small exact table checks; no expensive computation.

**Repair/provenance.** IC-RIG-001 resolves collisions with unrelated T-7401 claims without renaming or erasing source IDs.

#### `IC-REF-001` — Universal itinerary factor-complexity barrier is false

**Candidate statement.** The original PR #37 T-9318 claim, asserted for every itinerary, is false: the constant words 0^infinity and 1^infinity select the ordinary completion 0 while having factor complexity one.

**Independent PR #84 review gate.** Verify that T-9318 remains preserved as refuted and that the exact constant-word counterexamples, not a finite scan, carry the proof.

**Source aliases.** `PR37:T-9318`, `PR37:R-9304`

**Evidence boundary.** Proof: explicit exact counterexamples independently checked. Artifact: finite scan is corroboration only; not required.

**Repair/provenance.** The refutation remains permanently visible and is not overwritten by the repaired theorem.

#### `IC-REP-001` — Nonconstant itinerary factor-complexity barrier

**Candidate statement.** For the reviewed 64→81 section, put delta=log_64(81/64). A nontrivial ordinary survivor with initial room A_0>=2 and itinerary e satisfies p_e(n)>(n-log_64 A_0)/delta for every n>=1, hence liminf p_e(n)/n>=1/delta. More generally, a nonconstant binary word with liminf p_v(n)/n<1/delta cannot have eventually zero nearest-integer cylinder blocks.

**Independent PR #84 review gate.** Verify the PR #16 dependency pins, nonconstant hypothesis, strict slope inequality and induced 64→81 scope.

**Source aliases.** `PR37:T-9319`

**Evidence boundary.** Proof: independently reconstructed. Artifact: not required.

**Repair/provenance.** This is a distinct theorem with an added nonconstancy hypothesis. It does not retroactively verify PR37:T-9318.

## Roadmap records

| ID | Mathematical status | Promotion | Obligation |
|---|---|---|---|
| `RD-SC-001` | `open` | `roadmap_candidate_in_draft_pr` | Prove universal fixed-source coefficient stopping, equivalently escape of the least all-supercritical sources. |
| `RD-FC-001` | `open` | `roadmap_candidate_in_draft_pr` | Exclude every complete first-crossing canonical realization, including nontrivial positive cycles and acyclic near-returns, with the complete denominator and one common displacement. |
| `RD-BRIDGE-001` | `proposed` | `roadmap_candidate_in_draft_pr` | Independently establish the exact least-counterexample normalization/crosswalk under which SC* and FC* imply Collatz. |

### Bridge boundary

`RD-BRIDGE-001` is a proposed normalization/crosswalk theorem. Its components have reviewed sources, but the combined implication has not yet received independent review. Until that happens, use **“principal proposed roadmap bridge”**, not **“established logically exhaustive reduction.”**

See [`SC_FC_BRIDGE.md`](../docs/integration/2026-08-02-lifecycle/SC_FC_BRIDGE.md).

## What these records do not say

- Collatz remains unsolved.
- SC* is not proved.
- FC* is not proved.
- PR #84 has not independently reviewed itself.
- A frozen-source proof reference is not yet a durable local proof import.
- A finite artifact, inspected checker or bounded replay is not an all-depth theorem.

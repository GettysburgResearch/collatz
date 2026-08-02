# Integrated proof packets

Merged PR #84 accepted the initial `IC-*` statements as repository reference records. Draft PR #85 introduces the readable proof packets below on its branch. They become physically resident on `main` only if this draft is later reviewed and merged.

The packets are extracted from exact reviewed source commits rather than imported through whole branch histories. Adding a local proof body is an information and durability action; it is not a new independent mathematical review.

Each packet records:

- the precise statement and scope;
- a proof or exact proof extract;
- dependencies and notation;
- why the result matters;
- finite, ordinary, 2-adic, and all-depth boundaries;
- known failed strengthenings and common misreadings;
- exact source PR, commit, files, and review evidence;
- the next missing lemma.

Source authorship and branch-local claim IDs are preserved. A repaired theorem never overwrites a refuted original.

## Initial layer

| Packet | Integrated records | Status on draft PR #85 |
|---|---|---|
| [`ordinary-extraction/`](ordinary-extraction/README.md) | `IC-EXTRACT-001` | accepted reference; local proof packet proposed for main |
| [`completion-ghost/`](completion-ghost/README.md) | `IC-GHOST-001` | accepted reference; local proof packet proposed for main |
| [`periodic-tails/`](periodic-tails/README.md) | `IC-PERIODIC-001` | accepted reference; local component proof packet; integrated synthesis pending narrow review |
| [`coefficient-stopping/`](coefficient-stopping/README.md) | `IC-SC-001` | accepted reference; local proof packet proposed for main |
| [`finite-safety-automata/`](finite-safety-automata/README.md) | `IC-AUT-001` | accepted reference; local proof packet proposed for main |
| [`six-branch-rigidity/`](six-branch-rigidity/README.md) | `IC-RIG-001` | accepted reference; local proof packet proposed for main |
| [`factor-complexity/`](factor-complexity/README.md) | `IC-REF-001`, `IC-REP-001` | accepted references; local packet; PR #16 dependencies remain source-pinned |

## Status rule

“Local proof packet” means the proof is readable on the current branch. Until PR #85 merges, it does not mean the proof body is resident on `main`. It also does not imply that every dependency is local, that later source-branch additions were reviewed, or that the theorem is stronger than its exact stated scope.

The periodic packet is deliberately exceptional: its component source theorems were reviewed, but the exact integrated synthesis still requires one narrow independent review. The packet carries that warning prominently.

## Machine registry

The machine-readable records remain in [`../../claims/registry/`](../../claims/registry/). The registry tracks mathematical status, integration role, repository acceptance, proof residency on this branch, sources, and review evidence. It is a provenance layer, not the primary exposition.

## Adding another packet

A new integrated packet should be small enough to review as a coherent theorem unit. Copy source text exactly when possible; otherwise explain every editorial synthesis. Include a manifest-like provenance section and do not silently broaden the reviewed statement.

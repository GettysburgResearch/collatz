# Integrated proof packets

These are the readable mathematical spine of the repository. Each packet preserves exact source and review provenance, scope, proof or proof extract, common misreadings, and the next missing lemma.

| Packet | Records | Durable status |
|---|---|---|
| [`ordinary-extraction/`](ordinary-extraction/README.md) | `IC-EXTRACT-001` | `VERIFIED`; accepted with local proof |
| [`completion-ghost/`](completion-ghost/README.md) | `IC-GHOST-001` | `VERIFIED`; accepted with local proof |
| [`periodic-tails/`](periodic-tails/README.md) | `IC-PERIODIC-001` | `SOURCE-QUALIFIED`; component statements verified at exact SHAs; exact synthesis pending narrow review |
| [`coefficient-stopping/`](coefficient-stopping/README.md) | `IC-SC-001` | `VERIFIED`; accepted with local proof; SC\* remains open |
| [`finite-safety-automata/`](finite-safety-automata/README.md) | `IC-AUT-001` | `VERIFIED`; accepted with local proof |
| [`six-branch-rigidity/`](six-branch-rigidity/README.md) | `IC-RIG-001` | `VERIFIED` only for the exact six-branch complete-tree/full-tail/finite-control/eventual-integrality scopes |
| [`factor-complexity/`](factor-complexity/README.md) | `IC-REF-001`, `IC-REP-001` | accepted exact refutation plus separate `VERIFIED` repair; PR #16 dependencies remain source-pinned |

A local packet is not a new independent review. A packet may remain non-self-contained when a load-bearing dependency is pinned to an exact source SHA; that dependency must be listed precisely.

The wider reviewed repository is not reduced to these records. See [`../RESULTS_CATALOG.md`](../RESULTS_CATALOG.md) for centered/adelic, H, cycle, refund, pulse, least-counterexample, rewrite, control, and audit families still outside the resident spine.

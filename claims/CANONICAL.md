# Integrated reference and roadmap records

The records below were accepted onto `main` by merged PR #84. Acceptance means the repository selected these statements as stable reference points with exact provenance. It does **not** mean that they prove Collatz, that every proof dependency is local, or that an open roadmap obligation is solved.

Draft PR #85 introduces the linked local proof packets on its branch. They become physically resident on `main` only if this draft is reviewed and merged. Copying a reviewed proof locally is an information and durability action, not a new independent mathematical review.

Readable mathematics proposed by #85 lives under [`../research/integrated/`](../research/integrated/README.md). Machine metadata lives in [`registry/`](registry/) and is intended for integrators and tooling rather than first-time readers.

## Four separate questions

Every record distinguishes:

1. **mathematical status** — verified, proposed, open, refuted, or source-qualified;
2. **integration role** — canonical reference, roadmap, deferred, or historical;
3. **repository acceptance** — accepted on `main` or still selected only in a draft;
4. **proof residency** — local proof packet, frozen source reference, or open obligation.

For example, `IC-PERIODIC-001` is an accepted reference with a proof packet proposed by #85, while its exact integrated synthesis still needs a narrow independent review. `RD-SC-001` is an accepted roadmap obligation whose mathematics remains open.

## Integrated reference layer

| ID | Reference statement | Mathematical status | Proof residency on #85 | Important qualification |
|---|---|---|---|---|
| [`IC-EXTRACT-001`](../research/integrated/ordinary-extraction/README.md) | Ordinary extraction is canonical residue stabilization; nested positive extraction is bounded least-root stabilization. | verified | local packet proposed for main | Does not decide any concrete architecture. |
| [`IC-GHOST-001`](../research/integrated/completion-ghost/README.md) | `(1110)^∞` is a supercritical 2-adic completion ghost with every finite prefix positively realizable. | verified | local packet proposed for main | It is not a positive orbit or counterexample. |
| [`IC-PERIODIC-001`](../research/integrated/periodic-tails/README.md) | Periodic parity tails are controlled by the complete denominator `2^L-3^s`; positive ordinary eventual periods cycle. | reviewed components | local component packet | **Integrated synthesis pending narrow review.** |
| [`IC-SC-001`](../research/integrated/coefficient-stopping/README.md) | All-supercritical positive orbits diverge; least-source escape is equivalent to universal finite coefficient stopping. | verified | local packet proposed for main | SC* itself remains open. |
| [`IC-AUT-001`](../research/integrated/finite-safety-automata/README.md) | The terminal SCC of each fixed-depth cofinite safety automaton is a canonical-language artifact. | verified | local packet proposed for main | Does not exclude every regular sanctuary. |
| [`IC-RIG-001`](../research/integrated/six-branch-rigidity/README.md) | Finite affine/rational complete-tree sections and semilinear sanctuaries fail in the reviewed six-branch chart. | verified | local packet proposed for main | Least-root boundedness versus escape remains open. |
| [`IC-REF-001`](../research/integrated/factor-complexity/README.md) | The unrestricted low-factor-complexity nonstabilization screen is false. | refuted | local packet proposed for main | Exact counterexamples are the two constant words. |
| [`IC-REP-001`](../research/integrated/factor-complexity/README.md) | The nonconstant `64→81` repair gives a factor-complexity slope barrier. | verified | local packet with source-pinned dependencies | Does not apply to every Collatz trajectory. |

## Roadmap layer

| ID | Obligation | Repository status | Mathematical status |
|---|---|---|---|
| [`RD-SC-001`](../FRONTIERS.md#sc-universal-fixed-source-coefficient-stopping) | Prove universal finite coefficient stopping, equivalently escape of least all-supercritical sources. | accepted roadmap | open |
| [`RD-FC-001`](../FRONTIERS.md#fc-complete-first-crossing-exclusion) | Exclude every complete first-crossing realization with one common displacement and the complete denominator. | accepted roadmap | open |
| [`RD-BRIDGE-001`](../FRONTIERS.md#proposed-sc--fc-bridge) | Verify the exact least-counterexample crosswalk under which SC* and FC* imply Collatz. | accepted roadmap | proposed; pending narrow review |

## Repair discipline

The factor-complexity history is the model:

```text
PR37:T-9318
    remains refuted

PR37:R-9304
    preserves exact counterexamples

PR37:T-9319
    is a separately numbered nonconstant repair
```

A repair never retroactively verifies its source. Alternative proofs and colliding source IDs remain branch-qualified.

## Evidence discipline

The following are not interchangeable:

- proof independently reconstructed;
- proof body copied locally;
- artifact inspected;
- checker executed;
- artifact regenerated;
- large computation independently replayed;
- computation not replayed.

The local packets say exactly which occurred. A finite artifact is not promoted into an all-depth conclusion merely because its file is present.

## What is still missing

- SC* is not proved.
- FC* is not proved.
- The SC*/FC* bridge is not independently accepted as one theorem.
- The periodic integrated synthesis still needs its narrow review.
- No nontrivial positive cycle or divergent positive seed is accepted.
- Many reviewed results outside this initial layer still have source-resident proof bodies.

For the full scientific synthesis, read [`../CURRENT_KNOWLEDGE.md`](../CURRENT_KNOWLEDGE.md). For exact open obligations, read [`../FRONTIERS.md`](../FRONTIERS.md). Historical review and lifecycle evidence is indexed under [`../archive/`](../archive/README.md).

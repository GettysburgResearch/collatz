# Session report: issue #8 sink-stripped safety quotients

- **Agent:** `gpt56-sol-01`
- **Issue:** `#8` safety-automata/PDR widening path
- **Branch:** `cursor/sink-stripped-pdr-8f0f`
- **Pull request:** `#14`

## Starting hypothesis

The recurring SCCs of minimized finite-horizon safety automata might expose a
small quotient suitable for PDR-style widening into a regular Collatz
sanctuary.

## Approaches attempted

1. Read the repository protocol and inspected all active draft research
   branches and pull requests.
2. Selected issue #8's explicitly unclaimed safety-automata handoff.
3. Reconstructed each finite safety language independently from the integer
   reverse tree of `{1,2}`, without importing draft PR #12's transducer code.
4. Derived the residual languages reached beyond the finite forbidden trie.
5. Proved a cofinite-tail obstruction and an exact one-step nonclosure
   witness.
6. Implemented trie construction, exact DFA minimization, iterative SCC
   decomposition, tail stripping, and boundary profiling.
7. Added direct-orbit, reverse-tree, DFA, noncanonical-word, SCC, independent
   Kahn-cycle, and published-count tests.
8. Ran two adversarial reviews, corrected quantifiers and the scope of the
   widening conclusion, replaced recursive SCC traversal, capped the measured
   implementation at depth 32, and clarified reporting fields.
9. Replayed the corrected experiment and froze its output.

GitHub's available integration denied direct issue reads/comments, so an issue
claim comment could not be posted. Draft PR #14 and this report provide the
durable independent-attempt record.

## New results

### Proposed mathematical result

`L-9201` establishes:

- every fixed-depth safety language `S_d` is cofinite, with forbidden maximum
  `2^(d+1)`;
- its minimal canonical LSD-first DFA has one cyclic SCC, the universal
  two-state canonical tail;
- removing that tail leaves a DAG;
- `2^(d+2) -> 2^(d+1)` is an exact one-step failure of invariance;
- no cofinite set can be a forward-invariant sanctuary excluding `{1,2}`.

The corrected synthesis consequence is conditional on eventual reachability:
merely retaining an isomorphic two-state SCC does not imply cofiniteness.
Accepting every sufficiently long canonical word does.

### Exact finite computation

`X-9201` passed 11 tests and computed depths `0` through `32`.

At depth 32:

- forbidden starts: `35,664`;
- maximum forbidden start: `2^33 = 8,589,934,592`;
- raw DFA states before minimization: `112,474`;
- minimal states: `2,161`;
- canonical-tail states: `2`;
- boundary states: `2,159`;
- maximum shortest boundary-to-tail distance: `8`.

Every tested sink-stripped boundary was acyclic. The independent construction
reproduced draft PR #12's 21 minimal-state counts through depth 20.

Environment-independent summary digest:

```text
31b2c4ea38196c609383bdaa267669727df72a50074c6b2343a4355bd3486b9f
```

## Candidate counterexamples

None. There is no `K-####`, regular sanctuary, divergent orbit, or nontrivial
cycle.

## Failed approaches

- Raw within-depth SCC mining fails structurally: the only cyclic SCC is the
  cofinite canonical tail guaranteed by finite checking.
- Treating that tail as a candidate recurrent core fails because eventual
  acceptance of every long word includes all large powers of two.
- Running the current cumulative-set/trie implementation beyond depth 32 was
  rejected after memory-growth review; deeper runs need a streaming,
  bottom-up residual construction first.

These are method-specific failures, not evidence for Collatz convergence.

## Potential errors

- `L-9201` is complete-looking but remains `PROPOSED`; neither adversarial
  review produced a separately committed reconstruction.
- The experiment's generator and most tests share Python primitives. An
  independent audit separately used forward scanning, bottom-up residual
  construction, random-DFA distinguishability, and multiple hash seeds only
  through smaller depths.
- Boundary DAGs may have useful inter-depth embeddings even though each
  individual boundary is acyclic.
- The depth-32 distance profile is finite data and is not conjectured to
  stabilize.

## Files changed

- `research/safety-quotient/README.md`
- `research/safety-quotient/claims/D-9201-finite-safety-language.md`
- `research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md`
- `research/safety-quotient/claims/O-9201-sink-stripped-depth-32.md`
- `experiments/X-9201-sink-stripped-safety/README.md`
- `experiments/X-9201-sink-stripped-safety/run.py`
- `experiments/X-9201-sink-stripped-safety/test_run.py`
- `experiments/X-9201-sink-stripped-safety/results/summary.json`
- this report

## Claims affected

- `D-9201` — new, `PROPOSED`
- `L-9201` — new, `PROPOSED`
- `X-9201` — new, `EMPIRICAL`
- `O-9201` — new, `EMPIRICAL`

The isolated `92xx` namespace avoids collisions with draft PR #12's `91xx`
regular-sanctuary packet.

## Recommended next actions

1. Independently reconstruct `L-9201`, especially the empty-continuation
   residual argument.
2. Replace trie minimization with bottom-up residual hash-consing and stream
   reverse levels before extending past depth 32.
3. Define canonical, state-label-independent embeddings between boundary DAGs
   at consecutive depths.
4. Mine recurring inter-depth motifs and compose them with a genuinely
   recurrent guard whose decoded integer set has infinite complement.
5. Submit every learned candidate immediately to an independent exact
   one-step closure verifier.

## Organizational improvement ideas

Finite-horizon automata should explicitly tag components caused by cofinite
tails, threshold guards, padding conventions, or other bounded-cutoff
artifacts. Learning tasks should strip or veto those components before ranking
candidate invariants. Reports should distinguish in-session review from a
durable independently committed verifier.

## Handoff

```text
HANDOFF FROM: gpt56-sol-01
HANDOFF TO: automata learner / independent verifier
CURRENT CLAIM OR CANDIDATE: L-9201; no candidate
BLOCKING STEP: define inter-depth boundary-DAG embeddings
FILES TO READ: research/safety-quotient/claims/L-9201-cofinite-tail-obstruction.md;
  experiments/X-9201-sink-stripped-safety/run.py;
  experiments/X-9201-sink-stripped-safety/results/summary.json
FAILED ATTEMPTS: raw within-depth SCC mining; cofinite-tail widening
MOST PROMISING NEXT MOVE: bottom-up canonical boundary fingerprints across depth
MAIN RISK: recurring finite motifs still fail exact one-step closure
POSSIBLE ORGANIZATIONAL IMPROVEMENT: tag finite-cutoff automaton artifacts
```

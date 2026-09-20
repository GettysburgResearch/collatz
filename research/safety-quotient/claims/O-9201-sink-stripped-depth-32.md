Claim ID: O-9201  
Title: Exact sink-stripped safety profiles through depth 32  
Status: EMPIRICAL  
Authoring agent: gpt56-sol-01  
Reviewing agents: none committed  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9201; experiment X-9201  
Scope: shortcut safety depths 0 through 32 inclusive  
Related counterexample candidates: none

## Statement

Exact Python-integer computation in `X-9201` produced a minimal safety DFA at
every depth from `0` through `32`. At every tested depth:

- the terminal canonical tail has exactly two states;
- stripping that tail leaves an acyclic directed graph;
- the power-of-two pair from `L-9201` is accepted/rejected as claimed.

At depth `32`, the finite reverse tree contains `35,664` forbidden starts. Its
maximum is `2^33 = 8,589,934,592`. The independently constructed minimal DFA
has `2,161` states: two canonical-tail states and `2,159` boundary states.
Every boundary state reaches the tail in at most eight transitions along a
shortest route.

The experiment also independently reproduced the depth-0-through-20 minimal
state counts published by draft PR #12:

```text
4, 5, 6, 8, 9, 12, 15, 18, 21, 30, 36, 42, 46, 54, 63,
75, 92, 116, 143, 179, 217
```

The environment-independent summary digest is:

```text
31b2c4ea38196c609383bdaa267669727df72a50074c6b2343a4355bd3486b9f
```

## Definitions

Definitions are in `D-9201`. “Depth 32” inspects orbit states at times
`0,1,...,32`, not 32 transitions after the initial state.

## Motivation

The calculation checks the proof-guided sink-stripping implementation and
provides compact boundary profiles for the next inter-depth learning pass.
Agreement with an independently implemented draft-PR baseline reduces the
risk of a shared transducer bug because `X-9201` instead enumerates the finite
integer reverse tree directly.

## Proof or construction

Run:

```bash
cd experiments/X-9201-sink-stripped-safety
python3 -B -m unittest -v test_run.py
python3 -B run.py --max-depth 32
```

The exact output is frozen in `results/summary.json`. The script:

1. enumerates shortcut preimages of `{1,2}`;
2. constructs the finite-exception trie plus canonical tail;
3. minimizes by partition refinement;
4. decomposes the result into strongly connected components;
5. computes reverse-BFS distances to the tail;
6. verifies direct orbit membership for the explicit nonclosure witness.

## Dependency audit

- `D-9201` supplies definitions.
- `run.py` is the executable source of the observation.
- Draft PR #12 supplies only the 21 comparison values; no code from that
  branch is imported.
- `L-9201` is not needed to generate the rows. The computation checks its
  finite instances.

## Gap audit

- The depth-32 cutoff is finite.
- A boundary DAG profile is not an infinite orbit or inductive language.
- Agreement between two programs on state counts does not independently
  verify every general claim in draft PR #12.
- The two adversarial reviews occurred in-session; neither is represented by
  a separately committed verifier and neither promotes `L-9201`.

## Adversarial tests

Eleven tests cover:

- exact preimages and initial reverse-tree levels;
- direct iteration versus reverse-tree membership;
- direct iteration versus minimized-DFA membership;
- raw noncanonical-word rejection;
- all 21 published comparison counts;
- SCC-based tail uniqueness;
- independent Kahn detection of boundary acyclicity;
- power-of-two nonclosure witnesses;
- cofinite-threshold samples.

An independent code audit additionally reconstructed small cases by forward
scanning and bottom-up residual minimization, checked DFA hashes through depth
12, tested minimization on random DFAs, and found no incorrect result.

## Remaining uncertainty

The empirical data say nothing about stabilization as depth tends to infinity.
The observed maximum shortest tail distance of eight at depth 32 may grow
later and is not conjectured to be bounded.

## Suggested next attack

Canonicalize the sink-stripped boundary DAGs as rooted, edge-labeled objects
and search for embeddings from depth `d` to `d+1`. Any recurring motif should
be used only to propose a non-cofinite recurrent guard, then checked by an
exact one-step closure verifier.

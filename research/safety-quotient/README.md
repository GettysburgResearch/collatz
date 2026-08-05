# Sink-Stripped Safety Quotients

Agent: `gpt56-sol-01`  
Issue: `#8`  
Status: active independent path  
Counterexample status: none

## Contribution

This packet audits the proposed use of finite-horizon safety automata as
examples for automata learning or PDR-style widening.

The central correction is simple but structural: every fixed-depth safety
language is cofinite. Its minimal DFA therefore has an inevitable recurrent
two-state component reached by all sufficiently long canonical words. That
eventual acceptance cannot be retained by a safe forward-invariant language
because it includes all sufficiently large powers of two.

The correct finite object to study is the **sink-stripped boundary DAG**.
Useful recurrence, if any, must occur between boundary DAGs at successive
depths or after adding a guard whose decoded integer set has infinite
complement. It cannot appear as a nontrivial SCC inside one finite
approximant.

## Inventory

| ID | Status | Description |
|---|---|---|
| `D-9201` | `PROPOSED` | finite safety languages and canonical tail |
| `L-9201` | `PROPOSED` | cofinite-tail obstruction and boundary acyclicity |
| `X-9201` | `EMPIRICAL` after replay | exact sink-stripped profiles |
| `O-9201` | `EMPIRICAL` | frozen depth-0-through-32 observation |

Files:

- `claims/D-9201-finite-safety-language.md`
- `claims/L-9201-cofinite-tail-obstruction.md`
- `claims/O-9201-sink-stripped-depth-32.md`
- `../../experiments/X-9201-sink-stripped-safety/`

The `92xx` namespace is isolated from draft PR #12's `91xx` regular-sanctuary
claims. An integrator may cross-index it later; IDs should not be silently
renumbered.

## Relationship to the counterexample objective

A nonempty regular language closed under the shortcut map and avoiding
`{1,2}` would be a finite counterexample certificate. Finite safety
approximants are necessary supersets of any such language, but `L-9201` shows
that their obvious recurrent component is unusable. Sink stripping prevents a
learner from promoting that finite-horizon artifact and narrows synthesis to
languages whose decoded positive-integer sets have infinite complement.

No candidate language or Collatz counterexample is supplied.

## Next interface

Construct canonical embeddings or bisimulation-like fingerprints between
successive boundary DAGs. A learned motif must be paired with a recurrent
non-cofinite core and checked for exact one-step closure; finite-depth
stability alone is never sufficient.

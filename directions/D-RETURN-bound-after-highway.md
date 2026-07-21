# Direction: Return bounds after odd-run highways (handoff)

Suggested issue title: `Prove return / descent bounds after long odd-run Collatz highways`

```text
Status: IDEA
Proposal class: unclaimed research direction
Authoring agent: grok45-01
Created: 2026-07-21
Related: O-0111, O-0112
```

## Pitch

`O-0111`/`O-0112` show that length-\(k\) odd-runs produce enormous peaks but
empirically return to \(\{1,2\}\). If one can prove a uniform descent lemma
*after* a density-1 odd block — e.g. that \(T^{k+r}(n)<n\) for some
\(r=O(k)\) on the residue class of \(1^k\) — then pure highway certificates
die. Conversely, a single residue class violating all such bounds is a
divergence candidate.

## Why hand off

This packet's EV shifts to proving the 2-adic/3-adic ledgers' consequences
and mixed \(v_2\)/\(v_3\) constructions; a dedicated analytic return-bound
attack is a clean separate claim.

## Falsification

An explicit infinite family of odd-run seeds with first-below-start time
growing faster than any proved bound, or a divergent orbit.

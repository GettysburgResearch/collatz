# Ordinary entrance law: evidence and scope

23 November 2026. Full Collatz, sibling Harnack and the residue-512
implication remain open.

The scientific manuscript is
[ORDINARY_ENTRANCE_LAW.md](../../../../research/lean-exact-witness-global-20261121/profound-step-20261123/pressure/ORDINARY_ENTRANCE_LAW.md).
Exact source pins and external theorem uses are in [SOURCES.json](SOURCES.json).
The actual author executions are in [REPLAY.json](REPLAY.json).

## New written results

- The full inverse Green potential defines a killed ordinary sampler.
  It terminates almost surely with the exact predecessor-pressure terminal
  law. This is termination of the inverse sampler, not forward Collatz.
- As the root moves along the unchanged escaping ray, terminal laws
  converge in total variation to one fixed ordinary source law. The
  lifetime minus the root index converges jointly to a well-defined integer
  merge phase, retaining the ordinary endpoint.
- Complete basin-root summability yields finite total root variation of
  these laws, including finite Hellinger length at s=2, and critical Renyi
  entropy of the complete first-entry code.
- The balanced sibling transport has an exact exponential-tilt density,
  fractional overlaps, directed relative entropy, and a variational
  characterization over finite sets of actual ordinary sources.
- An anchored control keeps the empty-address cost zero and gives
  uniformly integrable transported densities and merging normalized laws,
  while the partition function tends to zero. Its scope is an abstract
  probability control, not an actual Collatz construction.

The ordinary arithmetic upper bound for the cost-plus-entropy objective
is not proved. The manuscript identifies that first unsupported step
without substituting an independent source law.

## Formal result actually compiled

`EntranceLaw.lean` has **nine public statements**: five exact phase/clock
lemmas, transformed path telescoping, the terminal killing factor, finite
row normalization, and normalized-tilt scaling invariance. The first
phase lemma is axiom-free; all other audit outputs use only subsets of
`propext`, `Classical.choice`, and `Quot.sound`.

The final unchanged module was compiled with
`-j 1 -DwarningAsError=true` using Lean 4.34.1 and pinned Mathlib
`d13f23b723b8a846827a245b89c10fc7d3f11612`.
[The complete strict audit output](lean-strict-audit.log) is retained.
No countable probability, real-power limit, entropy theorem or full
Collatz theorem is silently included in this finite module.

## Exact finite controls actually executed

The final checker passed normally and under `-O`, with byte-identical
outputs in [normal.json](normal.json) and [optimized.json](optimized.json).

| Control | Count |
|---|---:|
| Complete finite ordinary inverse-tree cases | 10 |
| Terminal atoms compared by independent enumeration/recursion | 3,410 |
| Exact balanced transport-density atoms | 3,410 |
| Normalized-tilt rescaling atoms | 13,640 |
| Fractional-moment inequalities | 10 |
| Literal ordinary phase hits | 1,939, from 469 ordinary sources |
| Finite source-conditioning identities | 7 |
| Anchored uniform-integrability bounds | 48 |
| Finite entropy versus chronological index controls | 32 |

The controls reject ten omitted-killing rows, ten lost-source sums, one
wrong signed-cost orientation, and the phase-uniqueness inference on a
periodic ray. A two-state transient-matrix calculation also rejects the
terminal-state denominator printed in Vigon's Proposition 3.3; the
correct starting-state denominator is independently derived in EL3.

The finite trees use convergent ordinary roots. Generic finite
conditioning weights and the anchored probability control are explicitly
separated from the escaping-component r weights. No hypothetical
escaping trajectory is claimed to have been numerically instantiated.

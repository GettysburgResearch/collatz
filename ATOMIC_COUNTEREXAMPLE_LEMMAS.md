# Atomic counterexample lemmas and questions

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36](https://github.com/gfreund123/collatz/issues/36)  
**Purpose:** standalone handoff problems whose successful positive resolution yields a Collatz disproof, or whose negative resolution decisively closes a major counterexample path  
**Status:** all `ACL-*` items below are open formulations, not repository claims

## 1. Conventions

Let

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

A **positive-resolution atom** is marked `P`: proving it as stated supplies a counterexample, perhaps after one separately named companion atom.

A **decisive-filter atom** is marked `N`: proving it closes a major construction route or reduces it to a smaller named class. These are useful, but do not themselves prove Collatz false.

A good submission for any atom must include:

1. exact quantifiers and frozen notation;
2. the dependency claims and their source commits;
3. a proof or a finite independently replayable certificate;
4. explicit positivity, integrality, and physical-transition checks;
5. a statement of the exact full-conjecture implication.

## Catalogue files

- [`cartography/ATOMS_FINITE_COLLISION.md`](cartography/ATOMS_FINITE_COLLISION.md) — finite cycle/sanctuary certificates and collision-architecture escape/exclusion atoms.
- [`cartography/ATOMS_CENTERED_H_RESONANCE.md`](cartography/ATOMS_CENTERED_H_RESONANCE.md) — centered \(64\to81\), H, and conditioned-resonance atoms.
- [`cartography/ATOMS_EQUIVALENT_SHARED.md`](cartography/ATOMS_EQUIVALENT_SHARED.md) — component, coverage, spectral, transport, and shared master lemmas.

## 10. Suggested ownership packets

| Packet | Atoms | Reason |
|---|---|---|
| finite-cycle packet | `P001–P002` | bounded, proof-producing, shortest path |
| collision escape packet | `P010–P015`, `N016–N018` | frozen class proposed closed; define the minimal escape |
| native centered packet | `P020–P021`, `N022–N025` | exact M1 boundary without invalid bridge |
| H renewal packet | `P030–P031`, `N032–N033` | shared shrinking-room/fresh-prime structure |
| finite sanctuary packet | `P003`, `P072` | integer-first finite/inductive certificates |
| component extraction packet | `P050–P055`, `N054` | makes analytic reformulations nonvacuous |
| shared theorem packet | `N070–N071` | cross-lane synthesis with maximal leverage |

## 11. Acceptance rule

No atom is complete merely because all finite prefixes exist, a \(2\)-adic limit is unique, a real shadow is positive, a measure is nonzero, a solver times out, a spectral approximation is suggestive, or a control map diverges.

For a disproof atom, the final line must identify an ordinary positive integer or an exact equivalent witness and prove the implication to the standard map.

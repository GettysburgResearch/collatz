# Atomic counterexample lemmas and questions

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36](https://github.com/gfreund123/collatz/issues/36)  
**Purpose:** standalone handoff problems whose positive resolution supplies a Collatz disproof, or whose negative resolution decisively closes a major construction path  
**Status:** `ACL-*` items are cartography formulations unless a file explicitly marks one `RESOLVED`

## 1. Conventions

Let

\[
T(n)=
\begin{cases}
n/2,&n\text{ even},\\
(3n+1)/2,&n\text{ odd}.
\end{cases}
\]

A **positive-resolution atom** is marked `P`. Proving it as stated supplies a counterexample, perhaps after one separately named companion atom.

A **decisive-filter atom** is marked `N`. Proving it closes or sharply classifies a construction route; it does not itself disprove Collatz unless it explicitly outputs the positive alternative.

Every accepted positive atom must include:

1. exact quantifiers and frozen notation;
2. dependency claims and source commits;
3. a proof or independently replayable finite certificate;
4. explicit positivity, integrality, exact valuations, and physical-transition checks;
5. the exact implication to the standard shortcut map.

## 2. Catalogue files

- [`cartography/ATOMS_FINITE_COLLISION.md`](cartography/ATOMS_FINITE_COLLISION.md) — finite cycles, sanctuary, and frozen collision escape/exclusion.
- [`cartography/ATOMS_CENTERED_H_RESONANCE.md`](cartography/ATOMS_CENTERED_H_RESONANCE.md) — centered \(64\to81\), H, and resonance.
- [`cartography/ATOMS_EQUIVALENT_SHARED.md`](cartography/ATOMS_EQUIVALENT_SHARED.md) — component, coverage, spectral, and shared lemmas.
- [`cartography/ATOMS_PASS_2.md`](cartography/ATOMS_PASS_2.md) — cross-cycle, endpoint-product, and completion-safe determinant atoms.
- [`cartography/ATOMS_PASS_3_REVIEWED.md`](cartography/ATOMS_PASS_3_REVIEWED.md) — quotient refund, critical distributed pulses, centered top-boundary, phase-1 reduction, and H delayed novelty.

## 3. Pass-3 identifier correction

The canonical linear-height refund atom is:

```text
ACL-P036.
```

The first pass-3 publication accidentally duplicated it as `ACL-P038`. `ACL-P038` is retired and is not a separate research problem.

`ACL-N074`, the `(8,13)` prime-233 packet, is recorded as resolved negatively.

## 4. Current positive frontier

| Packet | Atoms | Final certificate |
|---|---|---|
| critical cycles | `P001`, `P037`, `P039` | positive odd cycle and exact replay |
| sanctuary | `P003`, `P072` | DFA closure avoiding trivial cycle |
| quotient refund | `P036` | explicit positive expanding ordinary invariant |
| cross-cycle | `P019` with `N019`, `N079` | finite return or multi-phase nontermination |
| centered | `P020`, `P021`, `N026`, `N077` | eventually-zero ordinary tail or explicit forced-tail seed |
| H | `P030`, `P031`, `P035`, `N034`, `N080` | positive infinite H orbit |
| equivalent witnesses | `P050`–`P055` | third component, deficit, or faithful spectral support |

## 5. Highest-leverage decisive filters

| Atom | Question |
|---|---|
| `N016` / `N073` / `N078` | maximal finite-type almost-\(S\)-unit boundary and frozen-source integration |
| `N075` | does a distributed-pulse grammar have growing cross-prime essential rank? |
| `N076` | is quotient refund causal at the most-significant boundary? |
| `N077` | can the centered forced-tail one-counter system be closed positively or trapped negatively? |
| `N079` | does cross-cycle continuation genuinely leave phase 1 infinitely often? |
| `N080` | can H delayed novelty/reset renewal satisfy every ordinary and arithmetic budget? |

## 6. Acceptance rule

No atom is complete merely because:

- all finite prefixes exist;
- a \(2\)-adic limit is unique;
- a real shadow is positive;
- a measure is nonzero;
- a solver times out;
- a spectral approximation is suggestive;
- a quotient transition expands for large free lifts;
- or a numerator vanishes modulo a proper denominator factor.

For a disproof atom, the final line must identify an ordinary positive integer or an exact equivalent witness and prove the implication to the standard map.

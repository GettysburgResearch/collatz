# Atomic counterexample lemmas and questions

**Agent:** `gpt56-cartographer-01`  
**Issue:** [#36](https://github.com/gfreund123/collatz/issues/36)  
**Purpose:** standalone handoff problems whose positive resolution yields a Collatz disproof, or whose negative resolution decisively closes a major counterexample path  
**Status:** all `ACL-*` items are open formulations, not repository claims

## Conventions

A positive-resolution atom is marked `P`. A decisive-filter atom is marked `N`.

Every completed atom must provide exact quantifiers, source commits, positivity and integrality checks, physical-transition replay, and the exact implication to the standard map. Finite compatibility, a unique `Z_2` point, a real room, entropy, measure, or a long orbit prefix is not sufficient.

## Catalogue files

- [`cartography/ATOMS_FINITE_COLLISION.md`](cartography/ATOMS_FINITE_COLLISION.md) — cycle/sanctuary certificates and fixed collision escape/exclusion atoms.
- [`cartography/ATOMS_CENTERED_H_RESONANCE.md`](cartography/ATOMS_CENTERED_H_RESONANCE.md) — centered `64→81`, H, and conditioned-resonance atoms.
- [`cartography/ATOMS_EQUIVALENT_SHARED.md`](cartography/ATOMS_EQUIVALENT_SHARED.md) — component, coverage, spectral, transport, and shared master lemmas.
- [`cartography/ATOMS_PASS_2.md`](cartography/ATOMS_PASS_2.md) — cross-cycle handoff, deterministic centered safety, H endpoint-product, all-fixed-period, and maximality atoms added by the second pass.

## Suggested ownership packets after pass 2

| Packet | Atoms | Current reason |
|---|---|---|
| proof-producing cycle search | `P001–P002` | shortest finite route; issue #9 now staffed |
| regular sanctuary | `P003`, `P072` | finite integer-first certificate |
| fixed-type exclusion verification | `N016`, `N073` | `T-9831` proposes a general boundary; independent maximality audit needed |
| cross-cycle ordinary spine | `P019`, `N019` | first physical exit from frozen stage family; requires net-resource theorem |
| native centered safety | `P020–P021`, `N022–N026` | core recurrence now independently verified |
| completion-safe fixed periods | `N024–N027` | exact target is block common content / cubic outside-prime gcd |
| H endpoint-product packet | `P030–P035`, `N032–N034` | iteration 7 and `L-9903` reduce the frontier to one quantitative gate |
| component extraction | `P050–P055`, `N054` | analytic reformulations remain nonvacuous only with support extraction |
| shared architecture theorem | `N070–N073` | classify fixed-type exclusion versus growing/cross-cycle escape |

## Acceptance rule

For any `P` atom, the final line must identify one ordinary positive integer or an exact equivalent witness and prove why it falsifies Collatz. For any `N` atom, the final line must name the exact family closed and list the hypotheses a successor must violate.

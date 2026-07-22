# Q-8701 — Height-augmented proof-carrying PDR

**Claim ID:** `Q-8701`  
**Type:** open construction problem  
**Status:** `IDEA`  
**Authoring agent:** `gpt56-pdr-01`  
**Issue:** #40  
**Dependencies:** `D-8701`, `L-8701`, `T-8701`, `R-8701`

## Exact target

Construct one proof-carrying abstraction of the forced-tail base-64 transducer that includes the ordinary top boundary and proves one of the following.

### Constructive outcome

Produce an explicit finite seed `(B_0,e_0)` with `B_0>0` and an inductive certificate that every exact transition is legal. By `L-8701`, the orbit is then strictly increasing and divergent. After the issue-#4 chart translation is independently replayed, this would be a Collatz counterexample candidate requiring adversarial verification.

### Exclusion outcome

Produce an inductive invariant or ranking certificate proving that every canonical finite base-64 word eventually reaches a forbidden low residue. This would close the centered ordinary section, not the full Collatz conjecture.

## Recommended state

The exact multiplier transducer needs only

```text
current sign digit e,
previous input digit a_(j-1),
carry k in {0,...,17},
finite-control state for the proposed regular language,
one unbounded top/length counter.
```

A residue-only state is forbidden by `R-8701`. The certificate checker must verify:

1. low-digit legality;
2. every local base-64 output equation;
3. carry propagation and flush;
4. canonical most-significant nonzero digit;
5. closure or ranking at the unbounded top boundary;
6. concretization to one finite ordinary integer.

## Current computational boundary

`X-8701` finds no positive seed beyond four forced steps below `B<=10^6`. This is bounded evidence only. The exact cylinder minima already known in PR #16 show that long finite shadows exist at much larger heights.

No `K-####` candidate is assigned until a concrete seed and all-time certificate exist.

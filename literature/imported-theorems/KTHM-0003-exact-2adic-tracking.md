# KTHM-0003 — Exact loss of one `2`-adic digit per shortcut step

**Source:** finite-cylinder consequence of Terras's encoding. [@Terras1976]  
**Proof status:** complete  
**Maps to:** `CLAUDE/L-0004`; supports finite steering audits throughout both collision branches

## Statement

Let `x,y∈Z` and `f=v_2(x-y)<∞`. Then:

1. the parities of `T^j(x)` and `T^j(y)` agree for `0≤j<f`;
2. for every `0≤j≤f`,
   \[
   v_2(T^j(x)-T^j(y))=f-j.
   \]

Equivalently, agreement modulo `2^f` supplies exactly `f` common parity decisions and no additional `2`-adic precision is created before those decisions are exhausted.

## Proof

At any stage with positive valuation, the two current values have the same parity. If they are even, their next difference is `(u-v)/2`; if they are odd, it is `3(u-v)/2`. Multiplication by the odd number `3` does not change `v_2`, while division by `2` decreases it by one. Induct on the step number until the valuation reaches zero. ∎

## Scope limitation

After step `f`, the next parities may agree accidentally. The theorem says the originally certified precision is exhausted, not that later coincidence is impossible.

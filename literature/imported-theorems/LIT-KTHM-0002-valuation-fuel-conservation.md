# LIT-KTHM-0002 — exact 2-adic loss along a common parity prefix

**Source:** corollary of [@Terras1976], Theorem 1.2
**Inspection:** full text
**Proof status:** reconstructed complete proof

## Statement

Let `x,y` be distinct integers and let `f=v_2(x-y)≥0`. Then:

1. `x` and `y` have the same first `f` parity bits under the shortcut map `T`;
2. for every `0≤j≤f`,

```text
v_2(T^j(x)-T^j(y)) = f-j.                         (1)
```

In particular, common 2-adic tracking depth falls by exactly one at each common-parity step and is not created during that prefix.

## Proof

Because `x≡y mod 2^f`, `LIT-KTHM-0001` says their first `f` parity bits agree. Let `s_j` be the number of odd bits among the first `j` common bits. Applying the same affine-cylinder formula to both inputs and subtracting yields

```text
T^j(x)-T^j(y) = 3^(s_j)(x-y)/2^j.
```

The factor `3^(s_j)` is odd, so

```text
v_2(T^j(x)-T^j(y)) = v_2(x-y)-j = f-j.
```

This proves (1). At `j=f`, the two states differ by an odd number, so their next parities are opposite; the common prefix is exactly of length `f`. ∎

## Native mappings

- `CLAUDE/L-0004`: **KNOWN — COROLLARY**; “fuel conservation” is a useful native name for this exact valuation identity.
- All CRT steering and finite-prefix constructions that rely on tracking depth.

## Non-applications

Finite tracking depth says nothing about the existence of one ordinary integer realizing infinitely many independently prescribed prefixes.

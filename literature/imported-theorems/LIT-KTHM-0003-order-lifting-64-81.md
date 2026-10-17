# LIT-KTHM-0003 — exact multiplicative orders for 64 and 81

**Source:** standard lifting-the-exponent lemma (LTE); no specialized external theorem required
**Proof status:** complete proof
**External status:** FOLKLORE / STANDARD

## Statement

For every integer `k≥1`,

```text
ord_(81^k)(64) = 3^(4k-2) = 9*81^(k-1).           (1)
```

Furthermore,

```text
<64> mod 81^k = {x mod 81^k : x≡1 mod 9}.         (2)
```

For every integer `j≥4`,

```text
ord_(2^j)(81) = 2^(j-4).                           (3)
```

## Proof

### Order of 64 modulo powers of 81

Since `64≡1 mod 3` and `v_3(64-1)=v_3(63)=2`, odd-prime LTE gives, for every `n≥1`,

```text
v_3(64^n-1) = v_3(64-1)+v_3(n) = 2+v_3(n).       (4)
```

The congruence `64^n≡1 mod 81^k=3^(4k)` holds exactly when

```text
2+v_3(n) ≥ 4k.
```

The least positive such `n` is `3^(4k-2)`, proving (1).

Every power of `64` is `1 mod 9`, so the generated subgroup is contained in the right side of (2). The set of units congruent to `1 mod 9` has cardinality

```text
81^k/9 = 3^(4k-2),
```

which equals the order in (1). The inclusion is therefore equality.

### Order of 81 modulo powers of two

We have `81≡1 mod 16`. If `n` is odd, factorization or LTE gives

```text
v_2(81^n-1)=v_2(81-1)=4.
```

If `n` is even, 2-adic LTE gives

```text
v_2(81^n-1)
 = v_2(81-1)+v_2(81+1)+v_2(n)-1
 = 4+1+v_2(n)-1
 = 4+v_2(n).                                      (5)
```

For `j≥5`, congruence modulo `2^j` therefore requires `v_2(n)≥j-4`, and the least positive choice is `n=2^(j-4)`. At `j=4`, `81≡1 mod16` already, so the same formula gives order `1`. This proves (3). ∎

## Native mappings

- `CLAUDE/L-0013`: (2) is the complete subgroup/topological-generation statement at every finite level.
- `CLAUDE/T-0019`: (1) and (3) close the branch's missing all-level proof.
- Schedule-demand periodicity and stack-gadget lengths in `H64.md`.

## Review note

The native claim should state the range `j≥4` for (3). For `j<4`, the order is also `1`, while the expression `2^(j-4)` is not an integer.

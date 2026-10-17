# LIT-KTHM-0001 — affine parity cylinders and residue bijection

**Sources:** [@Terras1976], Theorems 1.1–1.2; [@Everett1976], Theorem 1
**Inspection:** full text
**Proof status:** reconstructed complete proof in repository notation

## Statement

Let

```text
T(n) = n/2               if n is even,
       (3n+1)/2           if n is odd.
```

Fix a binary word `e=(e_0,...,e_{L-1})` and put

```text
s_j = e_0+...+e_{j-1},   s_0=0.
```

There is a nonnegative integer

```text
B(e) = sum_{j=0}^{L-1} e_j 2^j 3^(s_L-s_{j+1})
```

such that every integer whose first `L` parity bits are `e` satisfies

```text
T^L(n) = (3^(s_L) n + B(e))/2^L.                 (1)
```

Moreover, every word `e∈{0,1}^L` is realized by exactly one residue class modulo `2^L`. Hence the map

```text
n mod 2^L  ->  first L parity bits of n
```

is a bijection.

## Proof

Write one step uniformly as

```text
T(x) = (3^e x + e)/2
```

when `x` has parity `e∈{0,1}`. Suppose after `j` prescribed steps

```text
T^j(n) = (3^(s_j)n+B_j)/2^j.
```

If the next parity is `e_j`, then

```text
T^(j+1)(n)
 = (3^e_j T^j(n)+e_j)/2
 = (3^(s_j+e_j)n + 3^e_j B_j + e_j 2^j)/2^(j+1).
```

Thus `B_{j+1}=3^e_j B_j+e_j2^j`. Starting from `B_0=0` and expanding the recurrence gives the displayed sum for `B(e)` and proves (1).

It remains to prove the residue bijection. Use induction on `L`. The empty word has one residue modulo `1`. Suppose a word `e` of length `L` is realized by exactly one class `r mod 2^L`. The two lifts are `r` and `r+2^L` modulo `2^(L+1)`. Formula (1) gives

```text
T^L(r+2^L) - T^L(r) = 3^(s_L),
```

an odd number. Therefore the two lifted states have opposite parity. Exactly one lift appends parity `0`, and exactly one appends parity `1`. This constructs a unique residue for each word of length `L+1`. Since both sets have cardinality `2^(L+1)`, the map is bijective. ∎

## Native mappings

- `PR3/L-0001`: **KNOWN — EXACT**.
- `PR3/L-0005`: inversion of a fixed word uses this theorem as substrate.
- `CLAUDE/D-0001`, `CLAUDE/L-0001`, and `CLAUDE/T-0021`.

## Non-applications

The theorem does not say that two distinct parity cylinders have the same endpoint. Collision fibers, signature classes, and induced radix maps require additional native algebra.

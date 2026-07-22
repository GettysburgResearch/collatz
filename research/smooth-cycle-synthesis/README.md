# Critical-scale smooth-cycle synthesis

**Agent:** `gpt56-complexity-01`  
**Issue:** #41  
**Status:** theorem-level claims are `PROPOSED`; no counterexample candidate

## Objective

Produce a finite, unconditional positive Collatz-cycle certificate.  For an
accelerated valuation word

```text
a=(a_0,...,a_(k-1)),
a_i>=1,
A_j=sum_(i<j)a_i,
A=A_k,
```

the affine constant is

```text
C(a)=sum_(j=0)^(k-1) 3^(k-1-j) 2^A_j,
D(k,A)=2^A-3^k.
```

A complete hit requires

```text
D>0,
D|C,
n_0=C/D in Z_(>0),
```

followed by independent replay of every exact valuation and the return to
`n_0`.

## Frontier correction

The first exploratory scan at hundreds of odd steps was not a valid candidate
search.  Every positive cycle obeys the exact product identity

```text
2^A/3^k=product_i(1+1/(3n_i)).
```

A verified lower bound `n_i>X` therefore forces

```text
0<A/k-log_2(3)<=log_2(1+1/(3X)).
```

Together with the local-minimum and verified-range literature, the serious
search begins at the continued-fraction scale, not at `k=O(10^2)`.  The packet
keeps all small smooth-denominator computations as controls only.

## Exact contributions

### `L-8401` — critical cycle product

The product identity and its height consequence are proved directly from the
accelerated equations.  It supplies the mandatory `(A,k)` gate for every
candidate grammar.

### `L-8402` — local block replacement and rotation

A fixed-length, fixed-sum replacement changes only the internal prefix terms of
`C`.  For a two-letter replacement `(x,y)->(y,x)` at position `u`,

```text
Delta C
 =3^(k-u-2) 2^A_u (2^y-2^x).
```

The same lemma proves that `D|C` is invariant under cyclic rotation.

### `L-8403` — Euclidean mechanical-word compiler

For lower and upper mechanical words with `p` ones and total length `q`, a
noncommutative Euclidean recursion evaluates any monoid product in `O(log q)`
recursive levels.  Applied to affine summaries, it compiles trillion-symbol
balanced valuation words without expansion.

### `O-8401` / `X-8401` — critical-scale adversarial candidate

The frozen target has

```text
k=3,149,971,404,836,
A=4,992,586,555,009.
```

A lower mechanical `{1,2}` valuation word is altered by 43 disjoint adjacent
swaps.  The resulting word:

- has `1,307,356,254,653` cyclic local minima;
- passes five exact denominator factors whose product is
  `1,465,129,870,107,858,983`;
- but has a rigorously enclosed fixed point ending in
  `.9975283539...`, at distance more than `0.0024716460` from the next integer.

It is therefore **not** a cycle.  This is a proof-producing failure record, not
a `K-####` object.

## Current target

The next constructive step must preserve the critical `(A,k)` gate while
escaping the single balanced mechanical skeleton.  The intended hierarchy is:

```text
mechanical SLP
 -> proof-carrying disjoint block replacements
 -> factor/modulus lifting
 -> directed real fixed-point filter
 -> exact full-denominator identity
 -> independent valuation replay.
```

A complete result requires the final full-denominator identity.  Passing a
large smooth component or approaching an integer in the real embedding is not
enough.

## Review order

1. `claims/L-8401-critical-cycle-product.md`
2. `claims/L-8402-block-replacement-rotation.md`
3. `claims/L-8403-mechanical-monoid-compiler.md`
4. `claims/O-8401-critical-mechanical-near-candidate.md`
5. `experiments/X-8401-critical-mechanical-cycle/run.py`
6. `experiments/X-8401-critical-mechanical-cycle/results/canonical.json`
7. session report under `reports/gpt56-complexity-01/`

## Honest status

No positive cycle, divergent orbit, sanctuary, or unconditional Collatz
counterexample was found.  No such claim should be inferred from the compressed
word length, the local-minimum count, or partial denominator divisibility.
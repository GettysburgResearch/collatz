# Critical-scale cycle synthesis and pulse-fiber offense

**Agent:** `gpt56-complexity-01`  
**Issue:** #41  
**Draft PR:** #45  
**Status:** theorem-level claims are `PROPOSED`; no counterexample candidate

## Objective

Produce an unconditional Collatz counterexample in one of the two finite,
independently replayable forms:

```text
A. one nontrivial positive accelerated cycle; or
B. one explicit positive ordinary seed with a proved unbounded exact block path.
```

For an accelerated valuation word

```text
a=(a_0,...,a_(k-1)),
a_i>=1,
A_j=sum_(i<j)a_i,
A=A_k,
```

the affine constant and denominator are

```text
C(a)=sum_(j=0)^(k-1)3^(k-1-j)2^A_j,
D(k,A)=2^A-3^k.
```

A complete cycle hit requires

```text
D>0,
D|C,
n_0=C/D in Z_(>0),
```

followed by independent replay of every exact valuation and the return to
`n_0`.

## I. Exact finite-cycle architecture

### `L-8401` — critical cycle product

Every positive cycle obeys

```text
2^A/3^k=product_i(1+1/(3n_i)).
```

A state lower bound therefore forces an exceptionally narrow upper rational
approximation to `log_2 3`. This corrected the original small-`k` search design:
the serious cycle search lives at the continued-fraction scale.

### `L-8402` — local block replacement and rotation

A fixed-length, fixed-sum replacement changes only the internal prefix terms of
`C`. For an adjacent swap `(x,y)->(y,x)` at position `u`,

```text
Delta C=3^(k-u-2)2^A_u(2^y-2^x).
```

The same lemma proves that complete divisibility is invariant under cyclic
rotation.

### `L-8403` — Euclidean mechanical compiler

Lower and upper rational mechanical words can be evaluated in any associative,
possibly noncommutative monoid by a Euclidean recursion. Exact affine summaries
of trillion-symbol balanced valuation words are therefore compiled in
`O(log k)` recursive levels without expanding the word.

### `L-8404` — residue decoder and block carry graph

For fixed `(k,A)`, a residue

```text
R=C(w) mod 2^A
```

determines at most one positive valuation word. Recursively,

```text
a_0=v_2([R-3^(k-1)]_(2^A)),
```

and division exposes the tail residue. This replaces a composition census of
size `binomial(A-1,k-1)` by one deterministic residue inversion.

For a proposed cycle state `n`, block-boundary carries satisfy an exact affine
integer graph. A zero-return path followed by valuation replay is a finite cycle
certificate.

### `O-8401` / `X-8401` — rejected trillion-step near-candidate

The frozen target

```text
k=3,149,971,404,836,
A=4,992,586,555,009
```

uses a lower mechanical `{1,2}` word and 43 disjoint adjacent swaps. It has
`1,307,356,254,653` cyclic local minima and passes five denominator factors
whose product is

```text
1,465,129,870,107,858,983.
```

A completion-safe real interval nevertheless places its fixed point at
`.9975283539...`, more than `0.0024716460` below the next integer. It is not a
cycle and has no candidate identifier.

### `T-8401` / `X-8402` — exact exclusion through 50,000 odd states

For a cycle of length `k` and minimum `n`,

```text
2^A n^k <= (3n+1)^k.
```

An exact multiprecision endpoint certificate proves that every cycle with
`k<=50,000` has

```text
n<=1,447,682,232.
```

Two independently written C++ programs then check all `723,841,113` odd
possible minima from `7` through that endpoint. Every one reaches a smaller odd
state; there are zero returns. Thus every nontrivial positive accelerated cycle
has more than `50,000` odd states.

This is a self-contained repository bound, not a claim of a world record against
all external cycle literature and counting conventions.

## II. Exact divergent-orbit architecture

### `L-8405` — fixed-weight pulse collision fibers

In the ordinary coordinate

```text
n=-5+2h,
```

the negative-three-cycle supplies two exact two-odd-step letters:

```text
A: h=8q    -> 9q,     valuations (1,2),
B: h=3+16q -> 3+9q,   valuations (2,2).
```

Every word of length `L` with exactly `b` pulses has the common radix data

```text
M=2^(3L+b),
N=9^L,
M F_w(h)=N h+C_w.
```

The `binomial(L,b)` words have distinct exact domain digits and form one
physical partial radix chart

```text
F_w(Mq+d_w)=Nq+e_w.
```

The branch word can be decoded from a residue without listing the entire fiber.

### `T-8402` — arbitrarily near-critical supercritical fibers

Put

```text
theta=log_2(9/8).
```

The fixed-weight chart is supercritical exactly when `b/L<theta`. Elementary
rational approximation supplies infinitely many pairs with

```text
9^L/2^(3L+b) -> 1 from above,
```

while `binomial(L,b)` grows exponentially.

Explicit shapes include:

```text
(L,b)=(6,1):     6 branches,       2^19 < 9^6;
(L,b)=(53,9):    4,431,613,550 branches, 2^168 < 9^53;
(L,b)=(665,113): a 433-bit branch count, 2^2108 < 9^665.
```

Any nontrivial ordinary integer surviving one such chart forever produces a
strictly increasing, unbounded physical Collatz trajectory. No additional
growth lemma would be needed.

### `X-8403` — exact fiber audit

The verifier reconstructs and physically replays every branch for `(6,1)`,
`(12,2)`, and `(18,3)`. It freezes the complete six-branch table and the least
positive cylinders through depth eight. The minimum grows from `19,416` to a
`129`-bit integer in that bounded range; this is evidence only.

## Primary open targets

### `Q-8401` — complete finite cycle identity

Construct one primitive compressed word satisfying

```text
C(w)=n(2^A-3^k)
```

for a positive integer `n`, then replay every valuation and the return. Passing
a proper denominator component or a near-integer real filter is not enough.

### `Q-8402` — ordinary path in a pulse fiber

Construct one finite `h_0>3` and a proof-carrying top-boundary invariant showing
that it remains in one supercritical fixed-weight chart forever. This is the
constant-modulus sibling of PR #51's run-core quotient and PR #49's
changing-height complement counter.

The positive architecture shared by all three is:

```text
one exact cylinder
+ one finite ordinary quotient
+ odd multiplicative refund
+ all-time definedness as the sole existence gap.
```

A fixed residue lasso or compatible `Z_2` point is not an ordinary witness.

## Verification artifacts

```text
X-8401  mechanical near-candidate and real rejection
X-8402  50,000-length product window and complete first-drop audit
X-8403  negative-three-cycle fixed-weight fibers and finite minima
```

Canonical SHA-256 values:

```text
X-8401: 7f9c69b95598326f9593ad5fb59f222e0c2355c31ac9c28ac49b882d041171b6
X-8402: 498e9c76fcd351ab25289f4c486b88757a0adc117ec0eecb2959d2c68d637e89
X-8403: b85bb5ee0e4ef2c59af21edfa7e689cff1ad71a7e8a2a2db055754341918c4bd
```

## Review order

1. `claims/L-8404-block-carry-decoder.md`
2. `claims/T-8401-no-positive-cycle-through-50000.md`
3. `experiments/X-8402-minimum-cycle-decoder/`
4. `claims/L-8405-negative-three-cycle-fixed-weight-fiber.md`
5. `claims/T-8402-near-critical-pulse-fiber-counterexample.md`
6. `experiments/X-8403-negative-three-cycle-fibers/`
7. `claims/L-8401-critical-cycle-product.md`
8. `claims/L-8402-block-replacement-rotation.md`
9. `claims/L-8403-mechanical-monoid-compiler.md`
10. `Q-8401-full-denominator-circuit.md` and `Q-8402-pulse-fiber-ordinary-path.md`

## Honest status

No positive cycle, divergent ordinary orbit, sanctuary, or unconditional Collatz
counterexample has yet passed the complete certificate gate. The packet now
contains both a strengthened finite-cycle offense and an explicit family of
near-critical expanding physical charts; the unresolved step is one ordinary
all-time realization, not another compatible finite prefix.

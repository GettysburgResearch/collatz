# L-9405 — Demand tree isometry and six-bit lift law

Claim ID: L-9405  
Title: The stack demand map is a scaled `2`-adic isometry onto the full demand coset  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: D-9403  
Scope: all integer stage parameters and their `Z_2` completion  
Related counterexample candidates: issue #4 stack frontier; no `K-####` candidate

## Statement

Let

```text
D(m)=17*81^(-(9m+2))-81^(-1).
```

For distinct ordinary integers `m,n`,

```text
v_2(D(n)-D(m)) = 4 + v_2(n-m).                 (1)
```

Moreover,

```text
D(m) in 16*Z_2.                                (2)
```

Consequently `D/16` extends to a bijective isometry

```text
D/16 : Z_2 -> Z_2,                              (3)
```

and `D` is a scaled isometry from `Z_2` onto `16*Z_2`.

For every base-`64` depth `j>=1`, with

```text
P_j=2^(6j-4),
```

we have

```text
D_j(m)=D_j(n)  iff  m=n mod P_j,                (4)
```

and

```text
{D_j(m): m mod P_j}
  = {r mod 64^j: r=0 mod 16}.                   (5)
```

Finally, every demand class at depth `j` has exactly `64` stage lifts to depth
`j+1`, and those lifts produce all `64` possible next base-`64` digits exactly
once.  Equivalently:

> one additional base-`64` demand digit is a permutation of exactly six new
> binary digits of the stage parameter.

This is the **six-bit lift law**.

## Proof

For `h=n-m != 0`,

```text
D(n)-D(m)
 = 17*81^(-2)*(81^(-9n)-81^(-9m)).              (6)
```

Every factor outside the parenthesis is odd.  Factoring an odd power of `81`
reduces the valuation to

```text
v_2(81^(9h)-1).                                 (7)
```

The elementary lifting identity for `81` is

```text
v_2(81^(9h)-1)=4+v_2(h).                        (8)
```

Indeed, if `h` is odd, the valuation is `v_2(81-1)=4`.  If `h` is even, the
standard factorization/LTE identity gives

```text
v_2(81^(9h)-1)
 = v_2(80)+v_2(82)+v_2(9h)-1
 = 4+1+v_2(h)-1.
```

This proves (1).

Since `81=1 mod 16`, all its positive and negative powers are `1 mod 16`.
Therefore

```text
D(m)=17-1=0 mod 16,
```

which proves (2).

For each `k>=0`, equation (1) says that the map

```text
m mod 2^k  ->  D(m)/16 mod 2^k
```

is injective.  Domain and codomain both have `2^k` elements, so it is a
bijection.  Passing through the compatible inverse system proves (3).

Take `k=6j-4`.  Multiplying the quotient statement by `16` yields (4) and
(5).  At the next depth, the `64` lifts

```text
m + a*P_j,  0<=a<64,
```

are pairwise distinct modulo `P_(j+1)=64P_j`, and their demands all reduce to
the same depth-`j` residue.  Because there are exactly `64` possible new
base-`64` digits, they realize each one exactly once.  This proves the lift
law. **QED**

## Consequences

1. The exact demand distribution over a complete stage period is uniform on
   the forced coset `16*Z/64^j Z`.
2. The exact period `2^(6j-4)` follows from isometry, not merely from an order
   upper bound.
3. Demand precision is not compressed by the stack arithmetic: every new
   base-`64` digit carries six newly distinguishable stage bits.

## Dependency audit

Only D-9403 and the displayed elementary valuation identity are used.  No
finite computation, automaticity theorem, Fourier theorem, or unmerged claim
is a proof dependency.

## Gap audit

- Uniformity of the demand map does **not** imply statistical independence
  from a supply stream evaluated at the same stage.
- A counter program can compute the demanded residue algorithmically without
  storing an explicit table of all classes.  The lemma is a distinguishability
  theorem, not an unconditional circuit lower bound.
- The image is the full coset modulo every finite depth, but this alone does
  not produce an ordinary infinite stack trajectory.

## Adversarial tests

`X-9403` exhausts the demand permutations through depth `3`, verifies the full
`64`-child lift law from depths `1` and `2`, and checks the valuation formula on
complete and deterministic sampled pair sets.

## Remaining uncertainty

Independent reconstruction is pending.  The principal application question is
how much of this exact stage information an actively steered context can carry
forward from one stack level to the next.

## Suggested next attack

Write the active stack transition as a map on

```text
(stage class, demand lift digit, high quotient)
```

and determine whether the high quotient can replay the six-bit lift law at
unbounded depth without being preloaded as an inverse-limit object.

# L-8802 — Shared-branch dyadic fuel loss

Claim ID: L-8802  
Title: One shortcut step consumes exactly one bit of `2`-adic agreement  
Status: PROPOSED  
Authoring agent: `gpt56-drift-01`  
Reviewing agents: none  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: D-8801  
Scope: every odd `a >= 3`; every distinct positive pair on the same branch  
Related counterexample candidates: issue #26; active residue-cylinder and precision-fuel programs

## Statement

Let `a>=3` be odd, and let `x!=y` be positive integers with the same parity.
Then

```text
v_2(T_a(x)-T_a(y)) = v_2(x-y)-1.
```

More generally, if two distinct inputs follow the same length-`L` parity word,
then

```text
v_2(T_a^L(x)-T_a^L(y)) = v_2(x-y)-L.
```

The right-hand side is nonnegative because sharing `L` physical branches forces
`x congruent y (mod 2^L)`.

## Definitions

`v_2` is the usual `2`-adic valuation of a nonzero integer. “Same branch” means
both inputs are even or both are odd at the step being compared.

## Motivation

Many repository arguments track a finite reserve of common dyadic precision.
This lemma shows that the basic one-bit loss is entirely format-driven: it does
not distinguish `3x+1` from the positive-drift `5x+1` control universe. Any
stronger impossibility result must use regeneration, chart arithmetic, height,
or another non-universal input.

## Proof or construction

Because `x` and `y` have the same parity, `x-y` is even.

If both are even, then

```text
T_a(x)-T_a(y) = (x-y)/2.
```

If both are odd, then

```text
T_a(x)-T_a(y) = a*(x-y)/2.
```

Since `a` is odd, multiplication by `a` does not change the `2`-adic valuation.
In either case division by `2` lowers it by exactly one.

For a common word of length `L`, apply the one-step identity successively. The
iterated values remain distinct because every branch is affine with nonzero
slope. This gives the displayed length-`L` formula. Conversely, before each of
the `L` shared steps the difference must be even, so the initial valuation is
at least `L`. **QED**

## Dependency audit

Only the two branch formulas in D-8801 and oddness of `a` are used.

## Gap audit

- `x=y` is excluded because `v_2(0)` is not finite.
- Inputs with different current parity do not satisfy the statement.
- The lemma describes loss along a fixed shared prefix. It says nothing by
  itself about whether a symbolic construction can replenish precision between
  prefixes.
- Exact finite-prefix agreement is not an infinite-orbit certificate.

## Adversarial tests

X-8801 checks every same-parity pair

```text
1 <= x < y <= 256
```

for `a in {3,5,7,9}`, totaling 65,024 exact checks.

## Remaining uncertainty

None known in the elementary valuation identity. Independent reconstruction is
pending.

## Suggested next attack

Define a connector’s **net fuel balance** as generated dyadic precision minus
its physical branch length. Prove either a replenishing connector family for
the phases in T-8802 or a finite-state negative balance theorem.

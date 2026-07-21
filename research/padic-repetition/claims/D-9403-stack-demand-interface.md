# D-9403 — Stack demand and stationary supply interface

Claim ID: D-9403  
Title: Exact `64 -> 81` stack demand, stationary supply, and matching maps  
Status: — (definition; frozen for this packet)  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: none  
Scope: the exact same-stage unsteered interface isolated in issue #4's stack program  
Related counterexample candidates: issue #4 M1 and stack frontier; no `K-####` candidate

## Source interface

Put

```text
q = 81^9.
```

The exact stack identity uses stage height `m` and block length `9m+1`.
The regeneration congruence for the context variable, reduced to any fixed
base-`64` depth, is represented by the `2`-adic integer

```text
D(m)
  = 17*81^(-(9m+2)) - 81^(-1)
  = 17*81^(-2)*q^(-m) - 81^(-1).
```

For an ordinary context parameter `x`, the corresponding unsteered amplifier
supply at the same stage is

```text
S_x(m) = 81^(9m)*(81x+1) = q^m*(81x+1).
```

The stationary mismatch is

```text
F_x(m) = S_x(m)-D(m).
```

These are exactly the two quantities compared in the conditioned
supply/demand experiment of issue #4.  This packet studies their full finite
quotient structure rather than sampled valuations.

## Finite-depth reductions

For `j>=1`, define

```text
D_j(m) = D(m) mod 64^j,
F_(x,j)(m) = F_x(m) mod 64^j.
```

All negative powers of `81` are interpreted using the inverse of `81` modulo
`64^j`; the definitions are therefore exact integer residue computations.

The stage modulus associated with depth `j` is

```text
P_j = 2^(6j-4).
```

## Stationary matching context

Solving the formal equation

```text
F_x(m)=0
```

for `x` gives

```text
X(m)
  = 17*81^(-(18m+3))
    -81^(-(9m+2))
    -81^(-1).
```

Thus `x=X(m)` is the unique stationary context attached to stage parameter
`m` in the `2`-adic matching locus.

## Extension to `Z_2`

The formulas are initially defined for ordinary integers `m`.  L-9405 and
T-9407 prove exact valuation identities, so each map extends uniquely and
continuously to `m in Z_2`.  No real exponentiation by a `2`-adic exponent is
assumed; the extension is obtained from compatible finite quotient maps.

## Interpretation boundary

This definition freezes only the **stationary same-stage unsteered**
supply/demand comparison.  An actively steered stack changes both the context
and the target height after every stage.  Results about `F_x(m)` do not, by
themselves, rule out that nonstationary construction.

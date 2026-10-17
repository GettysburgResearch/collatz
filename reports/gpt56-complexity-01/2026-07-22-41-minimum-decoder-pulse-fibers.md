# Session report — minimum decoder and near-critical pulse fibers

**Agent:** `gpt56-complexity-01`  
**Issue:** #41  
**Branch:** `agent/gpt56-complexity-01/41-smooth-cycle-synthesis`  
**Draft PR:** #45  
**Date:** 2026-07-22  
**Status:** no counterexample candidate; theorem-level claims remain `PROPOSED`

## Objective

Refocus the packet on a complete unconditional Collatz counterexample while
continuing to record exact partial results. Two finite certificate routes were
pursued in parallel:

```text
1. positive cycle:
   find one word with D>0 and D|C;

2. divergent ordinary path:
   find one finite ordinary marker in an exact supercritical physical chart.
```

## Repository sweep

The live cycle and constructive packets were re-read before choosing the next
work:

- issue #9 / PR #42: complete positive-cycle windows through 27 odd terms and a
  large low-complexity `(41,65)` census;
- PR #34: exact primitive-root, cross-prime, centered-defect, and support-floor
  reductions;
- PR #47 / PR #51: one-pulse, distributed-pulse, sparse-defect, and
  negative-cycle ordinary chart work;
- PR #49: a changing-height quotient-refund map where one forever-defined
  complement counter would already give an unbounded physical orbit;
- PR #44: the top-boundary warning that fixed-modulus lassos are completion
  ghosts unless finite support is proved.

The sweep confirmed that the shortest acceptable endpoint remains either one
finite positive cycle identity or one finite ordinary quotient with an all-time
inductive legality proof.

## 1. Exact valuation-block decoder

`L-8404` was added first. For fixed block length `k`, total valuation `A`, and
residue

```text
R=C(w) mod 2^A,
```

the first valuation is forced by

```text
a_0=v_2([R-3^(k-1)]_(2^A)).
```

Dividing exposes the tail residue. Thus each residue encodes at most one
positive valuation word, replacing an exponential composition census by one
linear decoder.

The same lemma gives an exact carry graph around a proposed cycle state. A
zero-carry return, followed by the standard valuation replay, is a complete
finite cycle certificate.

## 2. Exact cycle exclusion through 50,000 odd states

`T-8401` and `X-8402` combine the cycle-minimum product inequality

```text
2^A n^k <= (3n+1)^k
```

with a complete first-drop audit.

The exact product-window endpoint is

```text
N_*=1,447,682,232.
```

It passes the weakest product window at exactly

```text
k=47,468,
A=75,235,
```

and `N_*+1` fails at every `1<=k<=50,000`.

Both exact implementations then check every odd integer

```text
7<=n<=N_*,
```

`723,841,113` candidates. Every one reaches a smaller odd integer. The longest
first drop is `251` accelerated steps, first attained by

```text
1,200,991,791,
```

which reaches `1,064,232,949` below its start. All intermediate values fit in
`62` bits.

Authoring replay times were approximately six seconds for `run.cpp` and eight
seconds for the independently written parallel verifier on the available
container. Runtime is not part of the theorem.

Canonical JSON SHA-256:

```text
498e9c76fcd351ab25289f4c486b88757a0adc117ec0eecb2959d2c68d637e89
```

The conclusion is a self-contained repository exclusion through `50,000` odd
states. It is not presented as a world record against all external conventions.

## 3. Fixed-weight pulse collision fibers

The exact negative-three-cycle chart was then regrouped by pulse count. In the
ordinary coordinate `n=-5+2h`, the two letters are

```text
A: h=8q    -> 9q,     valuations (1,2),
B: h=3+16q -> 3+9q,   valuations (2,2).
```

For every length-`L`, pulse-`b` word,

```text
M=2^(3L+b),
N=9^L,
M F_w(h)=N h+C_w.
```

All `binomial(L,b)` words have distinct exact domain digits and share the common
radix map

```text
F_w(Mq+d_w)=Nq+e_w.
```

This is committed as `L-8405`.

## 4. Near-critical expanding family

`T-8402` uses

```text
theta=log_2(9/8).
```

The chart is supercritical exactly when `b/L<theta`. Rational approximation to
`theta` yields infinitely many charts with

```text
N/M -> 1 from above
```

while their exact branch counts remain exponential.

Frozen examples:

```text
(L,b)=(6,1):
  M=2^19,
  N=9^6,
  6 branches;

(L,b)=(53,9):
  M=2^168,
  N=9^53,
  4,431,613,550 branches;

(L,b)=(665,113):
  M=2^2108,
  N=9^665,
  433-bit branch count.
```

Every branch is a physical Collatz block. One nontrivial ordinary infinite path
in any supercritical chart is strictly increasing and therefore an
unconditional divergent Collatz seed.

## 5. Exact finite chart audit

`X-8403` reconstructs and physically replays all branches for

```text
(6,1), (12,2), (18,3).
```

It freezes the complete six-branch digit table and the exact least positive
cylinders through depth eight. The least cylinder grows

```text
19,416
 -> ...
 -> 544877977737345069246758429064839928000
```

and reaches `129` bits at depth eight. This is bounded evidence only.

Canonical JSON SHA-256:

```text
b85bb5ee0e4ef2c59af21edfa7e689cff1ad71a7e8a2a2db055754341918c4bd
```

## 6. Cross-program synthesis

The fixed-weight chart and the live run-core/complement-counter maps share the
same constructive skeleton:

```text
one exact cylinder
+ one finite ordinary quotient
+ one odd multiplicative refund
+ infinite definedness as the sole positive gap.
```

The new `Q-8402` freezes a proof-carrying ordinary-path target. A finite-state
residue lasso is explicitly insufficient; the certificate must preserve the
canonical most-significant boundary of the finite integer quotient.

PR #51's run-five highway gives a smaller changing-modulus laboratory. PR #49
supplies a second map with automatic quotient doubling. A top-boundary lemma for
one architecture should be transported to the other two.

## Files added

```text
research/smooth-cycle-synthesis/claims/T-8401-no-positive-cycle-through-50000.md
experiments/X-8402-minimum-cycle-decoder/README.md
experiments/X-8402-minimum-cycle-decoder/run.cpp
experiments/X-8402-minimum-cycle-decoder/verify.cpp
experiments/X-8402-minimum-cycle-decoder/results/canonical.json

research/smooth-cycle-synthesis/claims/L-8405-negative-three-cycle-fixed-weight-fiber.md
research/smooth-cycle-synthesis/claims/T-8402-near-critical-pulse-fiber-counterexample.md
research/smooth-cycle-synthesis/Q-8402-pulse-fiber-ordinary-path.md
experiments/X-8403-negative-three-cycle-fibers/README.md
experiments/X-8403-negative-three-cycle-fibers/run.py
experiments/X-8403-negative-three-cycle-fibers/results/canonical.json
```

The packet README was rewritten to expose both the finite-cycle and divergent
ordinary-path routes.

## Failed or bounded attempts retained honestly

- No cycle residue decoded in the exact finite range.
- The six-branch least cylinders did not stabilize through depth eight.
- No finite ordinary quotient invariant was found for the pulse chart,
  run-core map, or changing-height refund map.
- The growing branch fibers are not treated as ordinary realization.
- The reset-highway families in PR #51 give unbounded finite depth with changing
  seeds, not one infinite orbit.

## Exact current frontier

```text
Cycle route:
  construct C(w)=n(2^A-3^k) beyond the new finite floor.

Divergence route:
  construct one finite ordinary quotient whose multiplicative-refund map is
  defined forever and whose top boundary is generated, not preloaded.
```

No positive cycle, divergent ordinary orbit, sanctuary, or unconditional Collatz
counterexample was completed in this session. The new work sharpens both finite
certificate routes and creates an arbitrarily near-critical physical offense
with an explicit ordinary realization target.

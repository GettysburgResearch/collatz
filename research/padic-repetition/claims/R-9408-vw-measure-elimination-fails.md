# R-9408 — The published nine-phase measure does not support one-phase elimination

Claim ID: `R-9408`  
Title: Väänänen–Wallisser's quantitative exponent is larger than the scalar phase exponent at every admitted dimension  
Status: `PROPOSED / SOURCE-DEPENDENT METHOD CLOSURE`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9412`, `L-9413`, `L-9414`; Väänänen–Wallisser (1991), Theorem 1  
Scope: the one-phase elimination route for extending the source theorem beyond period nine  
Related counterexample candidates: none

## Published quantitative exponent

In the notation of `L-9412`, put

```text
gamma=1-log(64)/log(81).
```

Väänänen–Wallisser Theorem 1 gives, for every admitted dimension `D` and every
`epsilon>0`,

```text
|a_0+sum_(j=1)^D a_j f_R(y_j)|_2
 > C H^(-theta(gamma,D)-epsilon),
```

where

```text
theta(gamma,D)
 =1+(2D-1+sqrt(1+4D^2))
      /(2-gamma*(2D+1+sqrt(1+4D^2))).                 (1)
```

Since `|x|_2=2^(-v_2(x))`, this is exactly the valuation-height convention of
`L-9414` with

```text
omega_D=theta(gamma,D).                               (2)
```

No reciprocal or subtraction from one is involved in this translation.

## Exact comparison with the scalar phase exponent

The scalar Padé family of `L-9413` has

```text
tau=9/log_2(81).                                      (3)
```

Because `81>64=2^6`,

```text
tau<3/2.                                              (4)
```

For every admitted `D>=1`, the numerator in (1) is positive and the
denominator is positive. Moreover the numerator increases with `D`, while the
denominator decreases. Hence

```text
theta(gamma,D)>=theta(gamma,1).
```

Since `gamma>0`,

```text
theta(gamma,1)
 =1+(1+sqrt(5))/(2-gamma*(3+sqrt(5)))
 >1+(1+sqrt(5))/2
 =(3+sqrt(5))/2
 >5/2.                                                (5)
```

Combining (4)--(5),

```text
boxed:
omega_D=theta(gamma,D)>tau
```

for every dimension admitted by the source theorem, in particular for `D=9`.

Numerically,

```text
tau       =1.419591945535779...,
omega_1   =2.882180476090809...,
omega_9   =2318.657271150344... .                     (6)
```

The explosion at dimension nine reflects proximity to the source cutoff
`gamma=Gamma(9)`.

## Refuted inference

The following proposed extension is unavailable:

> Combine the published nine-phase linear-independence measure with the scalar
> Padé exponent of the tenth phase and apply `L-9414`.

`L-9414` requires `tau>omega_9`; the exact source formula gives the reverse
inequality by more than three orders of magnitude.

The same published measure cannot bootstrap the source theorem one phase at a
time from any smaller admitted dimension, because already `omega_1>tau`.

## What is not refuted

- irrationality of any period-ten stack value;
- a sharper nine-phase measure specialized to the native points;
- a special-vector construction that does not demand a uniform measure in all coefficient directions;
- the two-dimensional triangular `q`-difference route;
- direct combined-moment Padé or phase-sensitive Hermite–Padé;
- period-uniform estimates for the balanced S-adic directive.

## Dependency and source audit

- Formula (1) is transcribed from the fully supplied Väänänen–Wallisser paper.
- `L-9412` supplies the native parameter `gamma` and the admitted dimensions.
- `L-9413` supplies the scalar exponent `tau`.
- `L-9414` supplies the abstract elimination criterion.
- The comparison (4)--(5) is elementary and does not use floating-point arithmetic.

## Gap audit

This is a method-closure theorem, not a statement that the published measure is
optimal. Its constants depend on controlling every integer coefficient vector.
The native period-ten target is one special vector and may admit a far smaller
exponent.

## Adversarial tests

`X-9412` evaluates (1) for all dimensions `1,...,9`, verifies positivity of the
denominator, and checks the exact symbolic inequalities (4)--(5).

## Suggested next attack

Remove Route A from the load-bearing period-ten program. Concentrate on the
native homogeneous order-two `q`-difference equation obtained by eliminating
the polynomial inhomogeneity, or on Padé approximants to the combined moment
sequence. Any external theorem must be checked against the actual two-place
height parameter rather than inferred from the qualitative word
`q-functional`.
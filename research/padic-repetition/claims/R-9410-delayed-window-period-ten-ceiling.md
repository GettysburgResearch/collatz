# R-9410 — Delayed-window Padé still stops before period ten

Claim ID: `R-9410`  
Title: The fully optimized delayed equal-phase Gaussian-binomial family remains below the rationality threshold at period ten  
Status: `PROPOSED METHOD CLOSURE`  
Authoring agent: `gpt56-complexity-01`  
Created: 2026-07-22  
Last updated: 2026-07-22  
Dependencies: `L-9418`; elementary exact inequalities  
Scope: the complete one-denominator delayed-window family of `L-9418`  
Related counterexample candidates: none

## Delayed-family exponent

For displayed period `r` and asymptotic delay ratio

```text
M/n -> alpha,
alpha>=r,
```

`L-9418` gives

```text
mu_r^delay(alpha)
 =log_81(64)*f_r(alpha),                              (1)
```

where

```text
f_r(alpha)
 =[((alpha+1)^2-r)/(alpha^2+r)].                     (2)
```

The optimizer is

```text
alpha_r^*
 =(2r-1+sqrt(4r^2+1))/2.                             (3)
```

The optimized values are above one through period nine. This file proves that
period ten is below one for **every** real delay, without relying on decimal
optimization.

## Statement — exact period-ten ceiling

For every real `alpha`,

```text
boxed:
f_10(alpha)<263/250.                                 (4)
```

Also,

```text
boxed:
log_81(64)<19/20.                                    (5)
```

Consequently every delayed-window approximant family at period ten satisfies

```text
boxed:
mu_10^delay(alpha)
 <(19/20)(263/250)
 =4997/5000
 <1.                                                  (6)
```

Thus no choice of delayed cancellation window in `L-9418` proves irrationality
at period ten through the elementary rational-target threshold.

## Proof

At `r=10`, equation (2) is

```text
f_10(alpha)
 =(alpha^2+2alpha-9)/(alpha^2+10).                    (7)
```

Subtracting from the proposed upper bound gives

```text
263/250-f_10(alpha)
 =[13alpha^2-500alpha+4880]
  /[250(alpha^2+10)].                                 (8)
```

The numerator quadratic has positive leading coefficient and discriminant

```text
500^2-4*13*4880=-3760<0.                             (9)
```

It is therefore positive for every real `alpha`, proving (4).

The exact integer inequality

```text
64^20<81^19                                          (10)
```

proves (5). Combining (4), (5), and

```text
19*263=4997,
20*250=5000
```

gives (6). **QED**

## Why extra consecutive denominator degree is not a new escape

The root product of `L-9418` uses degree `D=rn` to cancel `n` consecutive blocks
in each of `r` phases. If the same consecutive root interval is enlarged, every
additional group of `r` roots automatically cancels one more complete block.
After reparametrizing by the actual cancellation length, this is again the same
family. It is not an independent degree-versus-window parameter.

Therefore (6) is the boundary of the full consecutive delayed root-product
architecture, not merely one arbitrary choice `D=rn` inside a larger unused
class.

## Quantitative location of the boundary

The exact optimizer (3) gives, numerically,

```text
max_alpha mu_9^delay(alpha)
 =1.000431470180016...,

max_alpha mu_10^delay(alpha)
 =0.994896616714958... .                              (11)
```

The decimals are orientation only. The theorem-level statements are the exact
period-nine certificate in `T-9422` and the exact period-ten ceiling (6).

## Refuted shortcut

The following proposed repair is closed:

> Keep one equal-phase Gaussian-binomial denominator, preserve its degree, and
> move the simultaneous zero window farther into the tail until period ten
> crosses exponent one.

Moving the window is a genuine improvement and closes periods four through nine
natively, but the exact global-height balance in (6) prevents it from reaching
ten.

## What remains open

This result does not exclude:

1. cancellation of the **combined** native coefficient sequence rather than all
   phases separately;
2. a Padé system for the homogeneous order-two `q`-difference equation in
   `L-9415`;
3. phase-sensitive Hermite--Padé or symbolic maximal-minor factors;
4. a quadratic common factor after exact numerator/denominator clearing;
5. a completion-height determinant using the ordinary nearest-integer or carry
   coordinates;
6. irrationality of period ten or the balanced nonperiodic directive.

## Dependency audit

- `L-9418` supplies the exact family and exponent formula.
- The proof of (4)--(6) uses only elementary rational inequalities.
- No numerical optimizer, external theorem, or experiment is a dependency.

## Adversarial tests

`X-9413` evaluates the optimized exponent through period fifteen and freezes
(8)--(10), including the exact final bound `4997/5000`.

## Suggested next attack

Abandon one-denominator equal-phase window placement as the load-bearing
period-ten route. The next approximant must reduce the intrinsic dimension from
ten, cancel the combined moment sequence directly, or exhibit a genuine
reduced-height factor.
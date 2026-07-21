# T-9415 — Eventually short-period stack directives are irrational

Claim ID: T-9415  
Title: Finite steering cannot repair a periodic tail of period at most three  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9408, T-9414  
Scope: every positive increment directive eventually periodic with a repeating block of length at most three  
Related counterexample candidates: issue #4 periodic stack frontier; no `K-####` candidate

## Statement

Let

```text
d_1,d_2,d_3,...
```

be positive integer height increments. Suppose that for some finite word `U`
and some nonempty positive word `W` with

```text
1<=|W|<=3,
```

the directive is

```text
U W W W W ... .                                    (1)
```

Then for every starting height `m>=0`,

```text
Theta(m;U W^infinity) notin Q.                      (2)
```

Consequently the associated formal stack context is irrational and cannot be
an ordinary integer.

Thus an arbitrary finite CRT-steering prefix cannot turn a constant,
period-two, or period-three tail into an ordinary infinite stack tower.

## Proof

Let the finite prefix have transfer data

```text
S(U), e(U), P_U.
```

L-9408 gives the exact identity

```text
Theta(m;U W^infinity)
 =P_U(T^(9m))
  +T^[e(U)]T^[9m|U|]
   Theta(m+S(U);W^infinity).                        (3)
```

The first term and the coefficient of the final tail are rational, and the
coefficient is nonzero. T-9414 gives

```text
Theta(m+S(U);W^infinity) notin Q                    (4)
```

because `1<=|W|<=3`.

If the left side of (3) were rational, solving (3) for the final tail would
contradict (4). This proves (2).

L-9407 translates the tail value to the initial context by another nonzero
rational affine map, so the context is irrational as well. **QED**

## Relationship to T-9413

T-9413 is the special case `|W|=1`. The present theorem adds all eventually
period-two and eventually period-three tails, including arbitrary finite
preconditioning or steering before the periodic regime begins.

## Dependency audit

- L-9408 supplies the exact finite-prefix transfer identity.
- T-9414 supplies irrationality of the repeating tail.
- No finite experiment or external theorem is a proof dependency.

## Gap audit

- The period is the length of the chosen repeating word. A shorter true period
  should be used when available.
- A tail of minimal period four or more is not covered.
- An eventually periodic result does not apply to the genuinely nonperiodic
  balanced `17/18` directive.
- Irrationality excludes ordinary contexts but does not prove transcendence.

## Adversarial tests

`X-9406` verifies the finite-prefix transfer calculus, while `X-9408` verifies
the period-two and period-three Padé interfaces. Finite checks are not proof of
the universal statement.

## Remaining uncertainty

The next periodic target is minimal period four. The true S-adic frontier then
requires limits of changing standard words rather than one fixed block.

## Suggested next attack

Search the period-four common denominators for systematic reduced-height
cancellation. The current universal exponent is only `0.006286...` below one,
so a small asymptotic gcd gain would propagate through this theorem to every
eventually period-four directive.
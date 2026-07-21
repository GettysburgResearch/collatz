# T-9413 — Eventually constant stack directives are `2`-adically irrational

Claim ID: T-9413  
Title: A finite steering prefix cannot turn a constant-increment tail into an ordinary stack context  
Status: PROPOSED  
Authoring agent: `gpt56-complexity-01`  
Reviewing agents: none  
Created: 2026-07-21  
Last updated: 2026-07-21  
Dependencies: L-9408, T-9412  
Scope: every height-increment directive that is eventually constant  
Related counterexample candidates: issue #4 stack frontier; no `K-####` candidate

## Statement

Let

```text
d_1,d_2,d_3,...
```

be positive integer stack-height increments. Suppose there are integers

```text
r>=0,
d>=1
```

such that

```text
d_t=d  for every t>r.                               (1)
```

Then for every starting height `m>=0`, the sparse tail value

```text
Theta(m;d_1d_2...)
```

of L-9408 is irrational in `Q_2`. Consequently the associated formal stack
context from L-9407 is not rational and in particular is not an ordinary
integer.

## Proof

Let

```text
U=d_1...d_r
```

be the finite exceptional prefix, with the empty word allowed when `r=0`.
L-9408 gives the exact transfer identity

```text
Theta(m; U ddd...)
 =P_U(T^(9m))
  +T^e(U)*T^(9m|U|)*Theta(m+S(U); ddd...).          (2)
```

Every coefficient outside the final tail in (2) is rational and the scaling
factor

```text
T^e(U)*T^(9m|U|)
```

is a nonzero rational number. T-9412 proves

```text
Theta(m+S(U); ddd...) notin Q.                      (3)
```

If the left side of (2) were rational, solving (2) for the final tail would
contradict (3). Thus the full value is irrational.

L-9407 expresses the initial stack context as a fixed nonzero rational affine
transform of this tail value. Therefore the context is irrational as well.
**QED**

## Interpretation

Finite CRT steering before a constant tail cannot repair the ordinary-section
obstruction. The irrationality is stable under every finite prefix of arbitrary
positive height changes.

This is stronger than testing a periodic tail after a bounded number of stages:
it gives one proof for all finite prefixes simultaneously.

## Dependency audit

- L-9408 supplies the finite-prefix transfer identity.
- T-9412 supplies irrationality of the constant tail.
- No finite experiment or external theorem is a proof dependency.

## Gap audit

- “Eventually constant” concerns height increments, not the emitted binary
  digits or contexts.
- The theorem does not cover a periodic tail of period greater than one.
- The finite prefix may be arbitrary but must have finite length.
- Irrationality excludes an ordinary context but does not prove
  transcendence.

## Adversarial tests

`X-9407` verifies the underlying constant tails. The finite-prefix identity is
already tested exhaustively by `X-9406` through the transfer calculus.

## Remaining uncertainty

The next periodic class is a nonconstant finite word `W` repeated forever. Its
value is a finite combination of partial-theta components at shifted arguments;
a simultaneous Hermite–Padé construction is needed.

## Suggested next attack

Generalize L-9409 from one scalar component to the finite phase vector of
`W^infinity`, preserving an approximation exponent greater than one after
common-denominator reduction.
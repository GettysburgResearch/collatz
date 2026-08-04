# L-9401 — Exact height of an eventually periodic code

Claim ID: L-9401
Title: Odd-denominator height bound for periodic continuation
Status: PROPOSED
Authoring agent: `gpt56-complexity-01`
Reviewing agents: none
Created: 2026-07-21
Last updated: 2026-07-21
Dependencies: D-9401
Scope: all finite binary prefixes and nonempty binary periods
Related counterexample candidates: issue #4 M1; no `K-####` candidate

## Statement

Let `u = u_0...u_(r-1)` be a binary word of length `r >= 0`, let
`v = v_0...v_(s-1)` be a nonempty binary word of length `s >= 1`, and let

```text
eta = u v v v ... .
```

Define

```text
Y = Phi(eta).
```

Then `Y` is rational.  If `Y = p/q` in lowest terms with `q > 0`, then

```text
q is odd,
q divides 81^r * (81^s - 64^s),
q < 81^(r+s),
0 <= Y <= 1  in the real embedding.
```

More explicitly, put

```text
U = sum_(i=0)^(r-1) u_i * 64^i * 81^(r-1-i),
V = sum_(j=0)^(s-1) v_j * 64^j * 81^(s-1-j),
```

with `U = 0` when `r = 0`.  Then

```text
Y = 17 * ( U*(81^s - 64^s) + 64^r*V )
    / ( 81^r * (81^s - 64^s) ).
```

## Proof

The finite prefix contributes

```text
(17/81) * sum_(i<r) u_i*(64/81)^i = 17U/81^r.
```

The periodic tail is a geometric series:

```text
(17/81) * (64/81)^r
  * [ sum_(j<s) v_j*(64/81)^j ]
  / [ 1 - (64/81)^s ]
= 17*64^r*V / [81^r*(81^s - 64^s)].
```

Adding the two terms gives the displayed formula.

The displayed denominator

```text
D = 81^r * (81^s - 64^s)
```

is odd, because `81^s` is odd and `64^s` is even.  Reduction can only make
the denominator divide `D`, so the reduced denominator `q` is odd.  Also

```text
0 < 81^s - 64^s < 81^s,
```

hence

```text
q <= D < 81^(r+s).
```

Finally, the same eventually periodic geometric series converges in the
real absolute value and has binary digits between `0` and `1`.  Therefore

```text
0 <= Y
   <= (17/81) * sum_(n>=0) (64/81)^n
   = 1.
```

This is an identity of one rational number evaluated in two completions, not
an identification of the real and `2`-adic limits of an arbitrary
nonperiodic code.  **QED**

## Dependency audit

Only the definition of `Phi` in D-9401 and the finite geometric-series
identity are used.

## Gap audit

- The period must be nonempty (`s >= 1`).
- The prefix may be empty; the convention `U = 0` handles `r = 0`.
- No assertion is made that the displayed denominator is reduced.
- The strict height bound is `q < 81^(r+s)`, not `<=`.
- The real bound applies because `eta` is eventually periodic, so its sum is
  the same rational in both completions.

## Adversarial tests

`X-9401` exhausts all prefix/period pairs with `r <= 6`, `s <= 6`, checks
the formula against direct `Fraction` summation, checks oddness and the
strict height bound, and includes the empty-prefix and all-zero/all-one
boundary cases.

## Remaining uncertainty

None known in the elementary algebra.  Independent reconstruction is still
required before status promotion.

## Suggested next attack

Look for systematic cancellation in `D` forced by chart classes modulo `17`
or by balanced directive words.  Any smaller uniform height exponent would
strengthen `T-9401` and `T-9402`.

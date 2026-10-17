# L-8003 — Explicit ordinary reset highways of unbounded finite depth

**Claim ID:** `L-8003`  
**Status:** `PROPOSED`  
**Agent:** `gpt56-pulse-01`  
**Issue:** #46  
**Date:** 2026-07-23  
**Dependencies:** local `O-8001`; elementary LTE  
**Scope:** exact finite positive paths in the negative-three-cycle pulse chart

## 1. Closed family

For every positive multiple `m` of `6`, define

\[
 \boxed{
 z_m=\frac{2^{m+4}-7}{9},
 \qquad
 n_m=6z_m-5.}
\tag{1}
\]

Then `z_m` and `n_m` are positive integers, and the exact chart path from
`z_m` begins

\[
 \boxed{
 z_m\xrightarrow{B}2^m
 \xrightarrow{A^{m/3}}9^{m/3}.}
\tag{2}
\]

After reaching `9^(m/3)`, the path has a completely explicit maximal string of
additional `B` edges.

Put

\[
 d=m/3,
 \qquad
 k(d)=\left\lfloor\frac{3+\nu_2(d)}4\right\rfloor.
\tag{3}
\]

Then exactly `k(d)` consecutive `B` edges are legal, and for
`0<=j<=k(d)` their values are

\[
 \boxed{
 B^j(9^d)
 =1+\frac{9^j(9^d-1)}{16^j}.}
\tag{4}
\]

Consequently `n_m` has a certified positive shortcut-Collatz prefix of at
least

\[
 \boxed{1+\frac m3+k(m/3)}
\tag{5}
\]

complete pulse-chart blocks. In particular, exact ordinary survival depth in
this chart is unbounded.

This is a finite-prefix theorem only. Every member checked so far eventually
leaves the chart.

## 2. Proof of the reset identity

Since `m` is a multiple of `6`,

\[
 2^{m+4}\equiv2^4\equiv7\pmod9,
\]

so `z_m` is integral. Modulo `16`,

\[
 z_m\equiv-7\cdot9^{-1}\equiv1\pmod {16},
\]

and hence the first edge is `B`. Direct substitution gives

\[
 B(z_m)=\frac{9z_m+7}{16}=2^m.
\tag{6}
\]

Every `A` edge removes exactly three powers of two and multiplies the odd core
by `9`. Because `m/3` is an integer,

\[
 A^{m/3}(2^m)=9^{m/3},
\]

proving (2).

## 3. Exact consecutive-B length

The branch `B` is centered at its fixed point `1`:

\[
 \boxed{B(x)-1=\frac9{16}(x-1).}
\tag{7}
\]

Iterating (7) gives (4). A `B` edge is legal precisely when its input is
`1 mod 16`; therefore the number of consecutive legal `B` edges beginning at
`9^d` is

\[
 \left\lfloor\frac{\nu_2(9^d-1)}4\right\rfloor.
\tag{8}
\]

Here `d` is even. LTE gives

\[
 \boxed{\nu_2(9^d-1)=3+\nu_2(d),}
\tag{9}
\]

which proves (3).

## 4. Exact condition for the highway to re-enter `A`

Write

\[
 d=2^s t,
 \qquad t\text{ odd},
\]

and let `k=k(d)`. After the maximal `B` string, the state is

\[
 x=1+9^k\frac{9^d-1}{2^{4k}}.
\tag{10}
\]

It can enter branch `A` exactly when

\[
 \boxed{
 s\equiv1\pmod4
 \quad\text{and}\quad
 t\equiv3\pmod8.}
\tag{11}
\]

### Proof

The difference `x-1` has valuation

\[
 3+s-4k\in\{0,1,2,3\}.
\]

If that valuation is positive, `x` is odd and neither another `B` nor an `A`
edge is available. Thus `A` can resume only when `3+s-4k=0`, equivalently
`s congruent 1 mod 4`.

For `s>=1`, the binomial expansion of `(1+8)^d` gives

\[
 \frac{9^d-1}{2^{3+s}}\equiv t+4\pmod8.
\tag{12}
\]

Since `9^k congruent 1 mod 8`, equation (10) is divisible by `8` exactly when
`t+4 congruent 7 mod 8`, i.e. `t congruent 3 mod 8`. This proves (11). ∎

The first nontrivial example is `m=18`: after the reset and six `A` edges, one
`B` edge produces an `A`-divisible state. It survives one further `A` edge
before leaving the chart.

## 5. Why this matters for the infinite target

The family proves that failure of bounded searches is not evidence for a
uniform finite trap. It supplies explicit ordinary roots with arbitrarily long
physical prefixes and exposes the exact next arithmetic resource:

\[
 \nu_2\left(
 1+9^k\frac{9^d-1}{2^{4k}}
 \right).
\]

Choosing successive binary digits of `d` can force longer later `A` runs. The
remaining question is whether this Hensel process can be generated forever by
one finite ordinary state rather than by a nonordinary 2-adic exponent.

## 6. Gap audit

- Unbounded finite depth does not imply an infinite orbit.
- The parameter `m` changes from one finite witness to the next; there is no
  single integer common to the family.
- The real and 2-adic evaluations of a limiting exponent must not be
  identified.
- Equation (11) guarantees at least one new `A` edge, not an infinite highway.

## 7. Suggested next attack

Use (10)–(12) as a Hensel compiler. At each re-entry, retain the exact odd
quotient after removing the forced power of two. Derive its next-bit recurrence
and test whether the source exponent can refund its own growing top boundary.
The exact run-core quotient map in `L-8002` is the canonical target language.
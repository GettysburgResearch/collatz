# Formal arithmetic core: homogeneous repunit cancellation

This module supplies the decisive coprimality lemma for the adjacent
unbounded congruence-packet construction. It is separate from the
written scalar-boundary and Taylor-germ arguments, which are not
formalized here.

For natural bases `P,Q`, define

\[
U_0(P,Q)=0,\qquad U_{n+1}(P,Q)=P U_n(P,Q)+Q^n.
\]

`repunit_eq_sum` proves that this is exactly

\[
U_n(P,Q)=\sum_{j=0}^{n-1}P^jQ^{n-1-j}.
\]

The central checked theorem is

\[
\boxed{\gcd(U_m(P,Q),U_n(P,Q))
       =U_{\gcd(m,n)}(P,Q)\quad\text{when }\gcd(P,Q)=1.}
\]

It includes zero indices and needs no order or positivity assumption
on the bases beyond their stated coprimality. In particular, coprime
indices give coprime repunits; that conclusion is proved, not assumed.

## Proof mechanism

The addition identity

\[
U_{m+n}=P^m U_n+Q^n U_m
\]

and `gcd(P,U_m)=1` for `m>0` imply
`gcd(U_m,U_(m+n))=gcd(U_m,U_n)`. Iterating this equality removes any
multiple of `m` from the second index. Lean's Euclidean gcd induction
then proves the full identity.

For `P>Q`, the module also proves the exact numerical quotient

\[
U_n(P,Q)=\frac{P^n-Q^n}{P-Q},
\]

and, for `P>=Q`, the full numerical identity

\[
\gcd(P^m-Q^m,P^n-Q^n)=P^{\gcd(m,n)}-Q^{\gcd(m,n)}.
\]

No replacement by a subset of prime factors occurs.

## Interfaces used by the packet construction

For coprime `X,Y` and any natural `r`,
`coprime_powered_repunit` proves that coprime `m,n` give coprime
`U_m(X^r,Y^r)` and `U_n(X^r,Y^r)`.

For positive `r,n`, `powered_repunit_coprime_base` proves
`gcd(U_n(X^r,Y^r),X*Y)=1`. The positivity of `r` is retained; at
`r=0` the repunit is `n`, so that stronger base claim would be false
in general.

The finite-source Collatz realization, the full packet carry, and the
final denominator separation belong to the adjacent written arithmetic
argument. They are not assumed or concluded by this algebraic module.

## Validation

`HomogeneousRepunits.lean` contains 17 proved theorem declarations.
`HomogeneousRepunitsAudit.lean` audits all 17 and the definition itself.
The final receipt records a fresh strict build, source hashes before
and after compilation, the exact Lean/Mathlib versions, and all axiom
output. No precompiled object of this authored module is reused in
that final build.

The files and proof boundary are bound by
`reports/2026-11-23-literature-push/rigidity-repunits-*`.

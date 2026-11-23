# Independent review of the primitive cyclotomic family

Date: 2026-11-22.
Reviewed file: `zero_atom_attack/CYCLOTOMIC_ZERO_FIBER.md`, equations
(N1)--(N17), with emphasis on the all-parameter family (N6)--(N17).

**Verdict: the written all-parameter exclusion is sound in the stated
domain.** It excludes this structured family; it does not supply an
unrestricted cycle theorem. No earlier finite Collatz census or previously
verified finite Collatz module was rerun for this review.

## 1. Legal positions and primitivity

For `b>=1`, `a-b>=2`, the consecutive within-block gaps are one, while
the cyclic boundary gaps are

\[
c_j=a-b+1+k_{j+1}-k_j\ge1.
\]

The smallest difference is `-2`. The last one position is
`11a+b+1 <= 12a-1`, so every position lies in the asserted range.
This includes the limiting case `a-b=2`.

The support of gaps different from one is nonempty and lies wholly in
the congruence class `b-1 modulo b`. A period of the cyclic gap sequence
must preserve that support, hence is a multiple of `b`. If its quotient
is `h`, then periodicity of the boundary differences makes
`k_(j+h)-k_j` constant in `j`. Summing over the twelve indices makes that
constant zero. Thus the period must also preserve `k`.

The two positions where `k=2` are exactly `{5,11}`. A nontrivial
translation of this pair can only be by six, and `k_0 != k_6` rules out
that translation. Thus the least gap period is exactly `12b`. Any
nontrivial binary-word period translates the one at zero to another one
and consequently induces a nontrivial period of the cyclic gap sequence.
It is therefore excluded. The least binary-word period is `12a`.

When `a-b=2`, the boundary from index 11 to index 0 has gap one; this does
not affect the argument, since the support of the other nonunit gaps is
still nonempty and is still in the one residue class modulo `b`. The
case `b=1` is also covered.

## 2. The full cyclotomic factor is retained

The coefficients of `(Y^4-Y^2+1)T(Y)` are, in increasing degree,

```
1, 1, 2, 2, 1, 4, 2, 1, 1, 2, 2, 4.
```

These are exactly `2^(k_j)`. Grouping the original word polynomial by
`i=bj+r` gives

\[
Q_w(X)=H_b(X)\sum_j2^{aj+k_j}X^{b(11-j)}
      =H_b(X)2^{11a}R^*(X^b/2^a).
\]

Since the twelfth cyclotomic polynomial is reciprocal, its homogenized
factor is exactly

\[
G_{a,b}(X)=X^{4b}-2^{2a}X^{2b}+2^{4a}.
\]

The denominator identity follows from
`Y^12-1=(Y^6-1)(Y^2+1)(Y^4-Y^2+1)`. Evaluating at `X=3`, with
`s=2^a`, `t=3^b`, gives the signs in (N12) exactly:

\[
D=G(s^6-t^6)(s^2+t^2),\qquad
C=(t-2^b)G B(t,s).
\]

There is no division by a cyclotomic factor that was not also exhibited
in the numerator. Integrality is indeed equivalent to
`D' | (t-2^b)B`.

## 3. Bezout certificate and its arithmetic consequence

I independently multiplied the two listed integer polynomials against
`f` and `Tstar`, without invoking the supplied checker. The complete
coefficient vector of their sum is

```
805, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0.
```

The two products have total degree fourteen. Homogenizing therefore
gives exactly `-U_h D' + V_h B = 805 s^14`, including the minus sign
because `s^8 f(t/s)=-D'`.

`D'` is odd and `s` is a power of two. Thus any common divisor of `D'`
and `B` divides `805`, not merely `805 s^14`. If `d=gcd(D',B)`, divisibility
by `D'` would imply `D'/d | t-2^b`, and hence

\[
D'\le805(t-2^b)<805t.
\]

On the other hand, `s>t>=3` implies `s-t>=1`, so

\[
s^6-t^6\ge6t^5,\qquad s^2+t^2\ge2t^2,
\]

and `D'>=12t^7>805t`, since `12*3^6>805`. This verifies the complete
all-parameter contradiction, including its smallest allowed `t`.

## 4. Preliminary lift and scope

The coprime lift (N1) also checks: if `pr+As=1`, then the image
`2^r 3^s` has p-th power `2` and A-th power `3` modulo the whole
denominator. Conversely the localized quotient has
`alpha=2^r 3^s`. The exponents in (N2) produce
`P_w(alpha)=C/3^(p-1)` in that quotient. The warning in (N3) is correct:
when the exponent gcd is greater than one, that single-field norm does
not retain the full original denominator.

The family consequently proves a real failure of the unrestricted
nonzero-norm proposal even for primitive parity words, and repairs it for
this entire parameter domain. The constant `805` is supplied by this
specific fixed residual polynomial. No uniform bound on the corresponding
certificate for arbitrary parity words has been established. The review
supports the stated family exclusion and its stated limitation equally.

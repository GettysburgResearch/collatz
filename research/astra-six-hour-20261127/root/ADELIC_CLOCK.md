# The actual clock series and the adelic capacity test

This is a direct test of arithmetic algebraicity machinery on one ordinary
trajectory. It does not establish algebraicity, periodicity, or convergence.
The input is the actual cumulative binary clock, with all places kept.

Let `a_i=U^i(a)` be a positive odd orbit, `A_0=0`, and
`A_(i+1)-A_i=v₂(3*a_i+1)`. Consider the single formal series

\[
                  F_a(z)=\sum_{i\ge0}2^{A_i}z^i\in\mathbb Z[[z]].
\]

The edge identity gives, for every `n`,

\[
 P_n:=2^{A_n}3^{-n}a_n
       =a+\frac13\sum_{i<n}2^{A_i}3^{-i}.                 \tag{1}
\]

As a 2-adic number `P_n` tends to zero, since `a_n` is odd and
`A_n>=n`. Thus the series converges at `z=1/3` in `Q₂` and has the
**rational 2-adic value**

\[
                          F_a(1/3)=-3a.                 \tag{2}
\]

On a hypothetical escaping positive orbit, the retained reciprocal bound on
distinct-state paths gives `P_n` increasing to a finite `P(a)>a`. In the real
completion the very same formal series then converges absolutely at `1/3`,
with value `3*(P(a)-a)>0`. These are evaluations in different completions;
they are not equal real numbers. The reciprocal input is the one used in
[the corrected-height construction](../escape/GRADED_CORRECTION_SETS.md).

## Exact radii at every place

Put `lambda_minus=liminf A_i/i` and `lambda_plus=limsup A_i/i`.
Both are finite: the positive edge inequality `3*a_i+1<=4*a_i` gives
`A_i<=2*i+log₂(a)`. The Cauchy–Hadamard formulas give

\[
 R_\infty=2^{-\lambda_+},\qquad R_2=2^{\lambda_-},
 \qquad R_p=1\quad(p\ne2).
\]

Consequently the product of all the available disk radii is

\[
                         \prod_v R_v=2^{\lambda_--\lambda_+}\le1.       \tag{3}
\]

If the clock slope exists, the product is exactly one. No assumed positive
speed of escape changes this equality. Replacing `z` by a nonzero rational
multiple of `z` also does not change the product, by the product formula.
For example, placing the factors `3^(-i)` in the coefficients expands the
real radius by three and shrinks the 3-adic radius by three.

The arithmetic rationality criterion of Bost–Chambert-Loir, Theorem 7.9
and Example 7.10, applies to suitable meromorphic continuation domains with
**strictly positive** capacitary degree; in the disk case its strict condition
is `product R_v>1`. The coefficients here supply the integral formal model
and local analyticity, but (3) does not supply that strict condition.
Analytic continuation to larger domains, possibly not disks, would be new
information. The rational value (2) is at a point already inside the
2-adic convergence disk, so it does not by itself enlarge the domain.
[Bost and Chambert-Loir, *Analytic curves in algebraic varieties over number
fields*, §§6–7](https://arxiv.org/abs/math/0702593).

## A positive lower bound at the mixed truncation scale

The real error in (1) cannot gain a strict exponential factor at these
particular truncations. Its first omitted term already gives

\[
 P(a)-P_n\ge 2^{A_n}3^{-n-1},\qquad
 3^n2^{-A_n}|P(a)-P_n|\ge\frac13.                         \tag{4}
\]

Thus the exact 2-adic approximation and the real tail meet at the scale in
(4), including on the arithmetic clean blocks from
[the physical-height shadow theorem](../global/HEIGHT_SHADOWS.md).
The latter theorem does not improve this positive tail estimate.

Taking powers of (1) yields additional telescoping identities, but not
independent interpolation data. Indeed, for every positive integer `m`,

\[
 \sum_{i<n}(P_{i+1}^m-P_i^m)=P_n^m-a^m.
\]

Their limits are `P(a)^m-a^m` over the reals and `-a^m` over `Q₂`.
As a generating function in a new sufficiently small variable `t`, they give
respectively

\[
 \frac1{1-tP(a)}-\frac1{1-ta},\qquad
 1-\frac1{1-ta}.
\]

This calculation retains the unknown real endpoint. It does not provide a
common rational jet that can be substituted into an algebraicity theorem.
The remaining proposed use of that machinery would require a proved
continuation or interpolation estimate beyond (1)–(4).

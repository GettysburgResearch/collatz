# A residual recurrence controls the entire two-adic normalization

Date: 2026-11-23. **Status: written exact lattice and height deductions.
The minimum-height closing estimate remains OPEN.**

Keep the actual odd-cycle notation of `INTEGER_RESIDUAL_DEGREE.md`.
This note refines the risk24 observation that making the normalized
orbit coefficients algebraically integral costs the maximum state `M`.
The cost is already attained in **every window of `d` consecutive odd
positions**, where `d` is the residual polynomial degree. Consequently
`M/m` is at most exponential in `d`. The bound does not reduce that cost
to a quantity sublinear in `d`, which the attempted closing argument
would need.

## 1. The normalized recurrence has integral coefficients and unit constant

Extend `s_(j+p)=s_j+A` and `x_(j+p)=x_j` to all integer indices, and put

\[
 u_j=2^{s_j},\qquad v_j=2^{s_j}x_j,\qquad
 r=2^{A/p},\qquad b_j=v_j/r^j.
\tag{RL1}
\]

Both `u_j` and `v_j` have minimal characteristic polynomial `F_0`.
For completeness, their generating functions have denominator `F_0`
and respective numerator polynomials `Q_0` and
`J=(Q_0+x_0F_0)/(X-3)`. At every root `lambda` of `F_0`,
`J(lambda)=Q_0(lambda)/(lambda-3)` is nonzero, so neither denominator
has an additional cancellation. This is the exact recurrence interface
proved in the risk24 Hankel note, not a new holonomicity claim.

Let `K=Q(r)` and `O_K` be its ring of integers. The normalized
characteristic polynomial

\[
 P(Y)=r^{-d}F_0(rY)
\tag{RL2}
\]

has coefficients in `K`, and its roots are roots of unity. Each
coefficient, being an elementary symmetric sum of roots of unity, is
an algebraic integer. Its constant coefficient is a root of unity up
to sign and is therefore a unit of `O_K`.

Thus `P` is a monic recurrence for the periodic sequence `b_j`, with
coefficients in `O_K` and invertible constant term. Forward and backward
recurrence imply that, for every integer `t`,

\[
 \boxed{
 \sum_{j\in\mathbb Z}O_K b_j
 =\sum_{j=t}^{t+d-1}O_K b_j.
 }
\tag{RL3}
\]

These are fractional ideals in `K`; periodicity makes the left side
finitely generated. This retains the actual normalized orbit
coefficients, not just their resultant. Forward recurrence and
periodicity alone would already suffice for the equality; the unit
constant also gives the backward formulation directly.

## 2. The two-adic deficit appears in every degree-sized window

Normalize every valuation above two by `v(2)=1`. Every actual `x_j`
is odd, so

\[
 v(b_j)=s_j-\frac{Aj}{p}=:t_j.
\tag{RL4}
\]

This value is the same at every prime of `K` above two. Taking the
valuation of the fractional ideals in (RL3) gives

\[
 \boxed{
 \min_{0\le j<p}t_j
 =\min_{t\le j<t+d}t_j\quad\text{for every integer }t.
 }
\tag{RL5}
\]

In particular the indices attaining the minimum form a cyclic set with
no gap exceeding `d`. This is an exact recurrence constraint on the
original gap word. It is stronger than merely saying that the full
period contains the maximum normalization deficit.

At other rational primes the `b_j` are integral. Therefore, when the
word is rotated to its minimum `x_0=m`, the least nonnegative integer
`kappa` making every `2^kappa b_j` an algebraic integer is

\[
 \kappa=\left\lceil-\min_{0\le j<p}t_j\right\rceil.
\tag{RL6}
\]

Since `s_j>=j`, (RL5) applied to `0,...,d-1` proves

\[
 \boxed{
 0\le\kappa\le
 \left\lceil\left(\frac Ap-1\right)(d-1)\right\rceil.
 }
\tag{RL7}
\]

No largest-state height was assumed to derive this bound. It follows
from the complete residual recurrence and the exact odd valuations.

## 3. Quantified maximum-state cost

Put

\[
 E_j=\sum_{i<j}\log\left(1+\frac1{3x_i}\right),\qquad E_p=\Lambda.
\]

Telescoping the actual edges gives, for `0<=j<p`,

\[
 b_j=m\exp(E_j-j\Lambda/p),
 \qquad
 x_j=m\exp(E_j-j\Lambda/p)2^{-t_j}.
\tag{RL8}
\]

Both `E_j` and `j Lambda/p` lie in `[0,Lambda]`. Combining (RL5)
with `t_j>=-(A/p-1)(d-1)` gives the whole-cycle amplitude bound

\[
 \boxed{
 \frac Mm\le e^\Lambda
 \left(\frac r2\right)^{d-1}.
 }
\tag{RL9}
\]

The earlier exact comparison remains

\[
 M e^{-\Lambda}\le m2^\kappa<2M e^\Lambda.
\tag{RL10}
\]

Thus the natural algebraically integral coefficient height is bounded
by a multiple of `m exp(Lambda)(r/2)^(d-1)`, but can still cost an
exponential in `d`. On actual integer cycles `r<=3+1/m<=4`; at large
minimum, its exponential base approaches `3/2`.

The interval `0,...,d-1` may be started anywhere. Thus a variant of
(RL9), with that start's state in place of `m`, holds after every
rotation, with the same `r,d,Lambda`.

There is also a slightly sharper form with fixed exponential base.
Choose `j<d` attaining the minimum of `t_j`. For any `k`, the difference
`log(b_k/b_j)=(E_k-E_j)-(k-j)Lambda/p` lies in `[-Lambda,Lambda]`,
using monotonicity of `E` and reversing the indices if necessary.
Hence `x_k<=exp(Lambda)x_j`. Actual gaps are at least one, so
`x_j+1<=(3/2)^j(m+1)`. Therefore

\[
 \boxed{
 M\le e^\Lambda\big((3/2)^{d-1}(m+1)-1\big).
 }
\tag{RL9a}
\]

The normalized maximum-state cost still has base `3/2`; no sublinear
cost in `d` follows.

## 4. A full positive rational control attains the deficit bound

For arbitrary integers `A>p>=2` with `2^A>3^p`, take gaps

\[
 (\underbrace{1,\ldots,1}_{p-1},A-p+1).
\tag{RL11}
\]

Then

\[
 Q(X)=\frac{X^p-2^p}{X-2},\qquad
 F(X)=X^p-2^A,\qquad \gcd(F,Q)=1,
\tag{RL12}
\]

because a common root would have both `p`th powers `2^p` and `2^A`.
Thus `d=p`. The positive rational closing value is

\[
 m_0=\frac{3^p-2^p}{2^A-3^p},
 \qquad
 x_j=(3/2)^j(m_0+1)-1\quad(0\le j<p).
\tag{RL13}
\]

It is the minimum. The word is primitive, since it has a unique gap
different from one. All its states are odd rationals with odd common
denominator, and the exact branch word is legal. For a rational cycle
write `kappa_2=ceil(-min_j t_j)` for the **two-adic deficit only**.
A power of two cannot clear its nontrivial odd denominator, so this is
not the full-integrality clearing exponent defined for integer cycles
in (RL6). Here `s_j=j`, so

\[
 \boxed{
 \kappa_2=\left\lceil\left(\frac Ap-1\right)(d-1)\right\rceil.
 }
\tag{RL14}
\]

The two-adic upper bound is attained. For the concrete control `p=8,A=13`,
`m_0=6305/1631>3`, and `kappa_2=5`; its odd denominator 1631 persists.
This is not an integer cycle; it
shows that positivity, a minimum above one, and the full residual
recurrence do not make the normalization cost disappear.

There are arbitrarily large such positive rational controls with minimum
above one: choose `(A,p)` among the upper continued-fraction convergents
of `log_2 3`. Then `A=ceil(p log_2 3)` eventually, `Lambda=O(1/p)`,
and (RL13) gives `m_0` tending to infinity. It is also polynomially
bounded in `p` by the same fixed two-logarithm theorem. Along them
`kappa_2/d -> log_2 3-1`. Hence an `o(d)` bound for the two-adic
deficit cannot
follow from those rational-word hypotheses alone. Any integral-specific
improvement must use the absence of the remaining odd denominator.

## 5. Small odd denominator does not bound the same-fiber gcd by height

A separate exact control tests a tempting final shortcut. The following
17 numerators, each divided by five, form one positive rational cycle:

```
187, 283, 427, 643, 967, 1453, 1091, 1639, 2461,
1847, 2773, 2081, 781, 587, 883, 1327, 1993
```

Its successive odd gaps are

```
1, 1, 1, 1, 1, 2, 1, 1, 2, 1, 2, 3, 2, 1, 1, 1, 5
```

Every edge is checked by the integer identity
`3 y_i+5=2^(a_i)y_(i+1)`. Since `p=17,A=27` are coprime,
`F=X^17-2^27` is irreducible by the constant-term argument in (IR13),
so `G=1` and `d=17`. The exact evaluation data are

\[
 D_{\rm pol}=5{,}077{,}565,\quad C=189{,}900{,}931,\quad
 q=5,\quad
 \gcd(D_{\rm pol},Q_0(3))=1{,}015{,}513.
\tag{RL15}
\]

But `m=187/5`, `M=2773/5`, and the largest reduced numerator is only
2773. The same-fiber gcd is therefore much larger than both the maximum
state and the maximum reduced-numerator height. No wrong conjugate or
missing denominator component is involved.

This is a direct rational control, not a counterexample to an
integer-specific theorem. It rules out bounding the final gcd by `M`
or by the largest reduced numerator using only positivity, the residual
recurrence, and a small odd denominator. No novelty is claimed for the
underlying rational cycle.

## 6. What the lattice result does not close

The integer-cycle theorem in the companion note gives `log m=O(log d)`
and `p<=C d^B` for fixed absolute constants. Equation (RL9) then permits

\[
 \log M\le O(\log d)+\Lambda+(d-1)\log(r/2),
\]

which remains linear in `d`. The coefficient-height cost has been
quantified; it has not become small enough to contradict exponential
residual-denominator growth. Nor is (RL3) an independent family of
distinguished-fiber vanishing conditions: it describes the same actual
recurrence module exactly.

Primitivity of the integer polynomial `J`, its small leading coefficient
`m`, the annulus (IR6), and the lattice identity (RL3) are compatible
with the estimates proved here. An upper bound for `d` in terms of
`log m`, or a strict full-fiber gcd estimate, still requires an additional
argument. No such bound is asserted.

The exact controls are shared with `check_integer_residual_degree.py`.
No algebraic number field numerical approximation, floating root
calculation, or bounded cycle census is needed to check the identities
listed there. The infinite fractional-ideal argument is a written proof.

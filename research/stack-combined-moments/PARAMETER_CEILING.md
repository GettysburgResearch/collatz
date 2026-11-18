# An exact ceiling for the single-window residual estimates

**PROPOSED method boundary.** The maximal-minor height bound and adjacent-sample residual root count of commit `52b98238146d1784fa8aef378cbc9f7ed762dd51`, `research/stack-shift-residual/PROOF.md`, can reach period 587. Optimizing their free coefficient count, delay and row center cannot reach 588. This concerns the stated estimates. Smaller actual minors, additional divisibility, a different auxiliary equation or a second window could change the answer.

Let $\rho=\log_{81}64$, $\delta=1-\rho$, and take D and M asymptotic respectively to $dn$ and $mn$, $m\ge d>1$. Use row center $\mu=M+\theta n$ in $g_k=\lfloor a(\mu k-k^2/2)\rfloor$. Allow any $0\le\theta\le1$. The integer kernel bound in units $an^2\log81$ is
$$
 h(d,\theta)=\frac{d/4-1/12}{d-1}+(\theta-1/2)^2.
$$
Indeed the sum of row spans has leading multiplier $d[\theta^2+(1-\theta)^2]/2$. In each of the two complementary common-minor divisor estimates the injection into distinct columns gains $[\theta^3+(1-\theta)^3]/6$, by the rearrangement argument on the two groups of rows of lengths asymptotic to $\theta n$ and $(1-\theta)n$. The real maximum-term bound and two prime divisors together subtract twice this latter multiplier, as in the cited proof. Division by $d-1$ and elementary simplification yield the formula.

Write $t=s/n+m$ for the shifted grid coordinate. The forced-identity positive margin from those estimates is
$$
 -\delta t^2/2+\rho t+\rho/2-
       (\rho+\delta\theta)d-h(d,\theta)>0.                         \tag{1}
$$
Here the first omitted tail degree costs $(1-\theta)d$ in the 2-adic estimate and the denominator exponent costs $\theta d$. Translating by m leaves the width unchanged; truncating to nonnegative s can only reduce it. The residual after removing the zero at the origin has at most $D-n+O(r)$ degrees, so the asymptotic window width divided by $d-1$ is the upper limit of the sufficient period ratio from this root count.

For fixed d, maximizing the left side of (1) over even unrestricted real $\theta$ gives $\theta=1/2-\delta d/2$. Put $x=d-1>0$. The squared discriminant parameter under the square root in the two t roots is at most
$$
 B=\rho-\delta(1+\rho)(1+x)-\delta/2-\frac{\delta}{3x}
       +\frac{\delta^3}{2}(1+x)^2 .
$$
If positive, the possible window width is at most $2\sqrt B/\delta$. The strict inequality $2\sqrt B/\delta<588x$ follows from positivity on $x>0$ of the cubic
$$
 \left(588^2\delta^2/4-\delta^3/2\right)x^3+
 [\delta(1+\rho)-\delta^3]x^2+
 [-\rho+\delta(1+\rho)+\delta/2-\delta^3/2]x+\delta/3.
$$
For a small exact certificate set $l=9463946/10^7$, $u=9463947/10^7$, $e=1-u$, $f=1-l$. A coefficientwise lower cubic has coefficients, in descending order,
$$
 A=588^2e^2/4-f^3/2,\quad B'=e(1+l)-f^3,\quad
 C=-u+e(1+l)+e/2-f^3/2,\quad D'=e/3.
$$
Its cubic discriminant $18AB'CD'-4(B')^3D'+(B'C)^2-4AC^3-27(AD')^2$ is negative, while $A,D'>0$. The unique real root is therefore negative. Rational arithmetic for these signs and for $l<\rho<u$ is given in the accompanying checker. This gives a strict upper ceiling, with the published period-587 parameter choice providing the matching integer lower bound.

Moving the center outside the window does not improve these same estimates. For $\theta<0$ the divisor-adjusted height becomes $h(d,1/2)+1/4-\theta$, and for $\theta>1$ it becomes $h(d,1/2)+\theta-3/4$ by the same single-group rearrangement. The tail loss is $d\max(1-\theta,0)$ and denominator cost $d\max(\theta,0)$. The resulting margin increases up to zero from the left and decreases beyond one. This comparison is needed only when the chosen exponent shifts define a valid integer construction; it adds no new admissible edge cases.

## Comparison with the scalar published q-difference criterion

Amou, Matala-aho and Väänänen treat the equation $z^s f(qz)=a(z)Cf(z)+b(z)$ at a finite or infinite place. Our scalar shift has $s=r$, $a=1$, $q=(64/81)^{9S}$ and constant nonzero $C$. Their Theorem 5.1 requires positivity of $B(\tau)-\ell A(\tau)$ at its prescribed sample, where $\ell=\log(81)/\log(64)$. For the scalar dimension $m=1$, equations (5.2)–(5.3) and Section 9 give
$$
A(\tau)=r\tau^2/2+\tau+K,\quad
B(\tau)=r\tau^2/2+(2-\delta)\tau,\quad
K=1/2+((2-\delta)^3-1)/(6\delta),\qquad 0<\delta<1.
$$
[Amou, Matala-aho and Väänänen, Acta Arithmetica 127 (2007), 309–335](https://www.impan.pl/shop/en/publication/transaction/download/product/83675)

For every $r\ge2$ these formulas give a negative margin at every $\tau>0$. Indeed $\ell>21/20$ by $81^{20}>64^{21}$. If $2-\delta\le\ell$ every term of the margin is nonpositive. Otherwise positivity would require $(2-\delta-\ell)^2>2rK\ell(\ell-1)$ by the quadratic discriminant. Already at $r=2$ and $\ell_0=21/20$ the opposite inequality holds. The polynomial
$$
1200\delta\big[4K\ell_0(\ell_0-1)-(2-\delta-\ell_0)^2\big]
=-1242\delta^3+2532\delta^2-1461\delta+294
$$
has positive cubic Bernstein coefficients on both halves of the unit interval. In increasing Bernstein index they are $(294,101/2,18,165/4)$ and $(165/4,129/2,287/2,123)$. Increasing $\ell_0$ to $\ell$ strengthens the inequality in the case under consideration. Thus this direct use of the published theorem supplies no further periods.

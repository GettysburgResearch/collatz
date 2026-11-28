# The nearest positive representative above the stationary real coordinate

**Written consequence of the single-scale pole theorem.** Let $(R,Z)$
have the joint stationary Collatz affine law, $q=3^k$, and let $J_k$ be
the smallest positive odd integer strictly above $R$ with
$J_k\equiv Z\bmod q$. Let $d_{\rm esc}$ be the ordinary relative
odd natural density of sources never reaching any positive cycle.
With $u_k=k^{-1/5}$,

$$
 \lim_{k\to\infty}\frac{3^k}{k}\,
 \mathbb E\frac1{J_k^{u_k}(J_k-R)^{1-u_k}}
    =\frac{\log3}{2}+\frac{\log(4/3)}2\,d_{\rm esc}.                      \tag{1}
$$

This differs from the pure ternary moment in
[Weaver 176 v1, Theorem 1 and (6)](https://rstation.ai/problems/collatz/papers/176/v1):
its excess coefficient is the actual escape density, without a
survival factor along the escaping sources. We have no upper bound
by the uniform coefficient for either moment.

## Conductor increment

Write $\rho_k(a)=q\Pr(Z\equiv a\bmod q)$, extended on all positive
odds, including zero values at nonunits. Put $\delta=\tfrac12\log(4/3)$,
$s=1-u$, $0<u<1$, and use the $H_k(a,s)$, $w(a)$, $c(a)$ of the
[single-scale theorem](SINGLE_SCALE_POLE.md). At fixed $k,u$ the
[real concentration bound](UNBOUNDED_CONDUCTOR_TRACE.md) gives

$$
 H_k(a,s)-\rho_k(a)/a
   =O_{k,u}(a^{-5/4}+a^{-2}(1+\log a)^2).                                \tag{2}
$$

In fact one drops the ternary indicator when bounding the difference
of the local test and one. Use the same three-way split as in the cited
note, then multiply by $q/a$. The fixed-$k$ periodic profile has
ordinary mean one on the odds. Thus the limit

$$
 L_k(s)=\lim_{M\to\infty}\left(\sum_{a\le M,\ a\ {\rm odd}}H_k(a,s)
                                      -\tfrac12\log M\right)
$$

exists. In the exact recurrence, cutting the output at $M$ sums over
$U(y)\le M$. The difference between this cut and $y\le M$ for
$H_k(y,s)$ has the same limit as for $\rho_k(y)/y$, by the summable
error (2) and pointwise eventual inclusion in both cuts.
Weaver's fixed-depth arithmetic flux establishes that limit as $\delta$:
gap $e$ has CRT mean $2^{-(e+1)}$ on all integers and cutoff ratio
$2^e/3$. The tail is uniformly summable in the iterated limit by
the progression bound directly following his (6). Also
$\sum_y(1-c(y)^u)H_k(y,s)$ converges absolutely at fixed $k,u$.
Consequently

$$
 L_{k+1}(s)-L_k(s)=\delta-\sum_{y\ {\rm odd}}(1-c(y)^u)H_k(y,s).           \tag{3}
$$

Since $0<w(y)\le\log(4/3)$, we have
$1-c(y)^u=uw(y)(1+O(u))$ uniformly. The real bound at conductor one
gives $L_1(s)=O(1+u^{-4})$: subtract $\rho_1(a)/a$ before summation,
using the quantitative terminal-factor estimate in the single-scale
note. Sum (3) from $1$ to $k-1$, with $u=u_k$ held fixed through the
sum. The pole theorem applies unchanged along this sequence because
$u_k\downarrow0$ and $(k-1)u_k^4\to\infty$. It yields

$$
                         L_k(1-u_k)/k\longrightarrow\delta d_{\rm esc}.   \tag{4}
$$

## Taking one positive representative

Conditional on $(R,Z)$, the nonzero terms in the cutoff sum start at
$J=J_k\in(R,R+2q]$ and continue at $a_j=J+2qj$, $j\ge0$.
Their values are $q a_j^{-u}(a_j-R)^{u-1}$. For $j\ge1$,

$$
                    \frac{1}{2j+J/q}\ \le\
  q a_j^{-u}(a_j-R)^{u-1}\ \le\ \frac1{2j}.
$$

The sum over all $j\ge1$ of the difference between the two bounds is
$O(1+\log(1+J/(2q)))$, by comparison with the integral of their
difference. For $M\to\infty$ and a fixed sample, the harmonic upper
bound through $j\le(M-J)/(2q)$ minus $\tfrac12\log(M/(2q))$ tends
to $\gamma/2$. Its cutoff absolute error is bounded by
$C(1+\log(1+J/(2q)))$ for all $M\ge2q$, including $M<J$.
For example, if $J\le M/2$ the final harmonic index is comparable
to $M/(2q)$ up to absolute additive constants; if $J>M/2$ the
normalizer is itself $O(1+\log(1+J/(2q)))$. This common majorant
is integrable uniformly in $k$ because $J\le R+2q$ and the stationary
real marginal has a finite positive fractional moment.

The $j=0$ term has finite expectation at fixed $k,u$. To see
this directly, sum over $a=J$. For $a\le4q$ use the local interval
bound, which is integrable against the pole of order $1-u$.
For $a>4q$, $a-2q\le R<a$ and a dyadic partition of the relative
deficit starts at $O(q/a)$. The bound (3) in the real concentration
note shows that this sum is bounded by a constant depending on $k,u$
times $\sum_a a^{-2}(1+\log a)^5$, which converges. Equivalently,
subtract the dominated tail sum from the already convergent finite
part and use monotone convergence for the first term. We obtain

$$
 L_k(s)=\mathbb E\!\left[qJ_k^{-u}(J_k-R)^{u-1}\right]
                            -\tfrac12\log(2q)+O(1),                       \tag{5}
$$

where the $O(1)$ is absolute simultaneously in $k$ and $0<u<1$.
Equations (4) and (5) prove (1).

Weak equidistribution of normalized representatives controls bounded
tests. A logarithm's worth of successive short intervals contributes
to (1). A uniform upper estimate for that native singular moment
remains the step needed to rule out escape.

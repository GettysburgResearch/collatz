# Nonlinear polynomial values on a single ordinary Collatz path

**Status — proposed elementary finite theorem.** Let $f\in\mathbb Z[X]$
be nonconstant and have no rational root. On any $N\ge3$ distinct
consecutive positive native shortcut states $x_0,\ldots,x_{N-1}$,
choose one set $S$ of at most $r\ge1$ primes. For each fixed
$0<\epsilon<1$, with the prime-to-pool part $R_S$ of an integer
as in [C1](SHIFTED_COFACTORS.md),
$$
 \#\{t<N:R_S(f(x_t))<|f(x_t)|^{1-\epsilon}\}
 \ \ll_{f,\epsilon}\ \sqrt N+r+
       {r(1+\ln(2r))N\over\ln N}.                                   \tag{P1}
$$
This is uniform in the source, the values of the primes, and a
pool selected after observing the whole segment. In particular
the exceptional fraction tends to zero for
$r\ln(2r)=o(\ln N)$. The same finite result holds on the $N$
distinct native phases of one primitive positive cycle. A finite
family without rational roots is handled simultaneously by a
union bound.

For fixed positive integers $r,s$, there is also a uniform bound
$$
 \#\{t<N:|f(x_t)|\in \bigcup_{j=1}^s a_j\Gamma\}
       \ll_{f,r,s} N^{r/(r+1)}                                      \tag{P2}
$$
when $f$ is irreducible over $\mathbb Q$ of degree at least two,
the $a_j$ are arbitrary positive rationals, and $\Gamma$ is an
arbitrary multiplicative subgroup of positive rationals of rank
at most $r$. All these choices may depend on the segment. This
concerns values of a fixed nonlinear polynomial at actual orbit
states. It does not presume multiplicative independence of the
states themselves.

## The return determinant

First take $f$ irreducible of degree $d\ge2$. Between times
$i<j$ the native word $w$ of length $l=j-i$ sends
$x_i$ to $(A x_i+C)/B=x_j$ with $A=3^b$, $B=2^l$,
$0\le C\le3^l-2^l$. Set
$$
 g_w(X)=B^df((AX+C)/B)\in\mathbb Z[X],\qquad
 U_w=\operatorname{Res}(f,g_w).
$$
There is an effective $c_f$ with
$$
 0<|U_w|\le e^{c_f l},\qquad
     \gcd(f(x_i),f(x_j))\mid U_w .                                   \tag{P3}
$$
Indeed, a zero resultant would make one root of $f$ a root of
$g_w$. By irreducibility $f$ would divide $g_w$ over $\mathbb Q$.
The injective affine map $(AX+C)/B$ would therefore permute the
entire finite set of $d$ distinct complex roots. A positive power
of this affine map would fix that entire set. Its slope is
$(3^b/2^l)^k\ne1$ for every $k\ge1$, whereas an affine map
fixing two distinct complex numbers is the identity. This proves
nonvanishing, even when the word consists entirely of even or
entirely of odd letters.

The coefficients of $g_w$ are at most $C_f3^{dl}$ in absolute
value by its binomial expansion. The determinant formula for
the Sylvester matrix bounds the nonzero integer $U_w$ as in (P3).
For divisibility use the adjugate of the integer Sylvester map
$(u,v)\mapsto uf+vg_w$ from two degree-$<d$ polynomials to
polynomials of degree $<2d$. It writes $U_w$ itself as such an
integer combination, up to sign. At $x_i$ its second term is
a multiple of $g_w(x_i)=B^df(x_j)$, proving the assertion at
all primes, including two. [Sylvester determinant and common
factors, Stacks Project, example 10.143.12](https://stacks.math.columbia.edu/tag/00UA)

For $f(X)=X^2+1$ the return integer in (P3) is explicitly
$(C^2+B^2-A^2)^2+4A^2C^2$. Both terms can vanish only if
$C=0$ and $A=B$, which is impossible. In contrast, a linear
polynomial can have a genuine periodic rational root and an
identically zero return integer. Those specific returns necessitate
the periodic-piece argument in C1.

## Counting the polynomial values

Put $V_p(t)=v_p(f(x_t))\ln p$. Consecutive indices with
$V_p(t)\ge a>0$ are at least $a/c_f$ apart by (P3): both
values share $p^{\lceil a/\ln p\rceil}$. There are at most
$1+c_fN/a$ hits. Remove one index of maximal valuation per
selected prime, deleting at most $r$ indices in total. For each
$p\in S$ the remaining tail count is at most $c_fN/a$.

Here are the details that allow the pool to grow. For a threshold
$Q>0$, put $a=Q/(2r)$. Values $V_p\le a$ can contribute at most
$Q/2$ to their sum. The count of times with some $V_p>Q$ is at
most $r c_fN/Q$. At all other remaining times the sum of
$V_p\,1_{\{a<V_p\le Q\}}$ over times, for each prime separately,
is at most
$$
 a\,\#\{V_p>a\}+\int_a^Q\#\{V_p>u\}\,du
      \ \le\ c_fN(1+\ln(2r)).
$$
Markov's inequality now bounds the number with $\sum_p V_p>Q$
by $O(r(1+\ln(2r))N/Q)$ plus the deleted indices. Distinctness
allows at most $\sqrt N+O_f(1)$ times with $x_t\le\sqrt N$
or in any fixed preliminary range. On all remaining times
$\ln|f(x_t)|\ge c'_f\ln N$ for large $N$, by polynomial growth.
Take $Q=\epsilon c'_f\ln N$ to prove (P1) for the irreducible
factor, enlarging the constant for bounded $N$.

For a general polynomial with no rational root, factor it over
$\mathbb Q$ into primitive integral irreducible factors of degree
at least two, multiplicities, and a nonzero content. Apply the
preceding result to each factor with tolerance $\epsilon/2$.
The fixed content contributes only a bounded log-smooth factor.
As $|f(x)|\to\infty$, the simultaneous estimates therefore imply
the stated $\epsilon$ test outside a fixed range. This proves (P1).

For (P2), in the group generated by sampled ratios within each
assigned coset, choose at most $r$ prime coordinates giving an
injective projection of its rational valuation-vector span.
Such coordinates exist by ordinary finite-dimensional linear
algebra on the finitely many sampled ratios. In a given coset
these coordinates uniquely determine each sampled polynomial
value. Apart from $O_f(1)$ initial integer arguments, $|f(x)|$
is strictly increasing in the positive argument, so equal values
have at most a bounded total contribution from exceptions.
For any $B_0\ge1$, discard the at most $r(1+c_fN/B_0)$ times
where a chosen log-valuation exceeds $B_0$, by the return bound.
The remaining integer valuation vectors have at most
$(1+B_0/\ln2)^r$ possibilities per coset. Taking
$B_0=N^{1/(r+1)}$ gives (P2). This proof counts group rank and
allows generators with arbitrarily large support.

The return-tail, weak summation, and choice of coordinate primes
are adaptations of Weaver's [Paper 138/v1, §§2,6](https://rstation.ai/problems/collatz/papers/138).
That source treats the unshifted odd states. The nonvanishing
affine return resultant is the additional input for nonlinear
orbit observables here. For arbitrary fixed nonzero polynomials,
combine the nonlinear factor estimate with (C1) for the rational
linear roots in $\mathbb Z_2$. A rational root outside $\mathbb Z_2$
cannot be a fixed point of any nonempty native word, whose
denominator divides the odd integer $2^l-3^b$; its linear
resultant is therefore nonzero as well. After absorbing fixed
contents and tolerances, one obtains the same lower native
fraction $\log_3 2$ as (C1) for arbitrary finite polynomial
families on a genuine escape, with bounded-size adaptive pools.
A pool containing all prime factors of one value may depend
on the clock; the theorems allow one bounded pool per segment.

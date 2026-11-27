# Height forces more than logarithmic squareclass rank

**PROPOSED written theorem, with a separate finite weighted-counting kernel.**
This combines the ordinary Pell spacing proved in
[the return-packing note](arithmetic/PELL_RETURN_PACKING.md) with the sizes of
the prime coordinates that encode a squareclass space. It applies to a finite
set of actual positive odd sources, whether or not they lie on one orbit.
The polynomial-height consequences below retain that additional hypothesis.

Let `U(x)=(3x+1)/2^v₂(3x+1)`. Let `A` be a nonempty set of `N` distinct
positive odd integers at most `X`, and let `r` be the affine dimension over
`F₂` of the classes `[x U(x)]`, `x in A`, modulo positive rational squares.
Put `rho=97+56 sqrt(3)`. For every real `0<sigma<1`,

\[
 N\le\left(1+\frac{\log X}{\log\rho}\right)
       (12X^2)^\sigma
       \exp\!\left(\frac{(r+1)^{1-\sigma}}{1-\sigma}\right).       \tag{1}
\]

In particular, along any such finite populations with `N -> infinity` and
`X <= N^(B+o(1))`, for a fixed finite `B>=1`,

\[
 \boxed{\quad
  \liminf\frac{\log(r+1)}{\log\log N}\ge\frac{2B}{2B-1}.
 \quad}                                                         \tag{2}
\]

This is a superlogarithmic rank bound. It improves the logarithmic bound
only in the stated polynomial-height regime. It neither proves that an
arbitrary escaping orbit has polynomial height nor supplies an upper bound
on its squareclass rank.

## Prime pivots retain their ordinary size

For every source let

\[
 D_x=\operatorname{sf}(3x(3x+1)).
\]

This is a squarefree positive integer, at most `12X^2`. For an actual odd
edge with exponent `a`,

\[
 [D_x]=[3]+[xU(x)]+(a\bmod2)[2].
\]

The discriminant classes therefore belong to an affine space of dimension
`R<=r+1`. Their squarefree representatives are unique. Choose `R` prime
coordinates on which the direction space has full rank. Projection onto
these coordinates is injective on the entire affine space. This is ordinary
row reduction over `F₂` on a finite-support basis; the translation does not
alter injectivity. Write the distinct pivot primes in increasing order as
`p_1,...,p_R`. They satisfy `p_j>=j+1`.

If a discriminant projects to the subset `J` of its nonzero pivot coordinates,
then `product_{j in J} p_j` divides that discriminant. Consequently the number
`K` of distinct discriminants in this population satisfies

\[
 \begin{aligned}
 K
 &\le \#\{J\subseteq\{1,\ldots,R\}:\prod_{j\in J}p_j\le12X^2\} \\
 &\le (12X^2)^\sigma
             \prod_{j=1}^R(1+p_j^{-\sigma}) .                    \tag{3}
 \end{aligned}
\]

For the second inequality, each admissible subset contributes at least
one to `(12X^2)^sigma product p_j^(-sigma)`. Sum over admissible subsets,
enlarge to all subsets, and expand the finite product. This is an
elementary weighted count, without a distribution assumption on prime
divisors. In particular it remains valid when the affine space is selected
after the entire ordinary population is known.

Using `log(1+u)<=u`, the integral estimate for `sum j^(-sigma)`, and `R<=r+1`
gives

\[
 \log\prod_{j=1}^R(1+p_j^{-\sigma})
 \le\sum_{j=1}^R j^{-\sigma}
 \le\frac{R^{1-\sigma}}{1-\sigma}
 \le\frac{(r+1)^{1-\sigma}}{1-\sigma}.                            \tag{4}
\]

For `R=0` the product is one and the middle sum is empty. Distinct ordinary
odd sources sharing a discriminant have successive height ratios strictly
greater than `rho`. Hence each discriminant appears at most
`1+log X/log rho` times among sources in `[1,X]`. Multiply (3) by this
bound and use (4) to obtain (1).

The integer nature of the pivot primes matters. Replacing them by abstract
independent symbols of weight one would lose (3), leaving only the weaker
bound by the number `2^R` of all masks.

## The asymptotic exponent

Fix `sigma<1/(2B)`. Taking logarithms in (1), using
`log X <= (B+o(1))log N`, and observing that the logarithm of the Pell
multiplicity factor is `O(log log N)`, yields

\[
 \liminf\frac{(r+1)^{1-\sigma}}{\log N}
       \ge(1-\sigma)(1-2B\sigma)>0.                              \tag{5}
\]

Thus the lower limit in (2) is at least `1/(1-sigma)`. Let the fixed
parameter `sigma` increase to `1/(2B)`. This proves (2); it does not exchange
a varying parameter with an unproved uniform error term. Equivalently, for
every fixed `epsilon>0`, eventually

\[
 r+1\ge(\log N)^{2B/(2B-1)-\epsilon}.
\]

For an injective ordinary prefix one may apply this to all its odd
departures, or to an arbitrary subset of departures below a prescribed
height. Only the chosen sources must fit the height bound. Their successors
are the actual successors, and no rank condition is imposed on omitted
states. On a primitive ordinary cycle the sources are distinct, so the
same statement applies with `N` its odd period.

## The repository's bounded cycle branch

For the positive primitive cycles in the earlier binary physical band
`M <= (16s+7)/3`, the quoted input
`mu(log_2 3)<=3` implies `M<=P^(3+o(1))`. For completeness, multiplication
of the actual odd edges gives

\[
 0< A/P-\log_2 3
   =\frac1{P\log2}\sum_i\log(1+1/(3x_i))
   \le\frac1{3s\log2}.
\]

An irrationality exponent at most three gives, for each fixed
`epsilon>0`, a positive lower bound of order `P^(-3-epsilon)` for the left
side at all sufficiently large denominators. Reduction of `A/P` only
strengthens this lower bound; finitely many smaller reduced denominators
are excluded once the difference tends to zero. Thus `s<=P^(3+o(1))`, and
the physical-band bound transfers this to `M`.

Equation (2) therefore yields the source-qualified consequence

\[
 \boxed{\qquad r+1\ge(\log P)^{6/5-o(1)}.\qquad}                 \tag{6}
\]

The Diophantine input is Chudnovsky's October 2026 preprint,
*Irrationality exponents of logarithmic numbers: Values, quotients, and
graded approximation*, Theorem 11.1. Its proof archive is not replayed here.
The unconditional theorem of this note is (1), and (2) assumes its displayed
height relation. Formula (6) retains the named external input and the same
physical-band hypotheses as the repository's earlier height use.
[Primary preprint](https://arxiv.org/html/2610.28079v1#S11) ·
[Earlier exact scope](../six-hour-20261127/arithmetic/MICROSCOPIC_JOINING.md).

## Formal boundary and remaining step

`WeightedMasks.lean` checks the finite positive weighted-subset inequality
used in (3), including an arbitrary injective encoding into masks. Prime
pivot selection, Pell spacing, real powers, the asymptotic passage, and the
quoted Diophantine result remain written mathematics with the dependencies
above. No complete cycle exclusion follows: a sufficiently large-rank
cycle is compatible with (1)–(6). Closing this route requires a conflicting
upper rank bound or another consequence of the full chronological cycle.

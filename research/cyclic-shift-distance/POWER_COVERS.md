# Quantitative bounds for arbitrary covers by word powers

**PROPOSED, source-qualified for the polynomial minimum estimate.** Let
a primitive positive ordinary shortcut cycle of length L>=2 have any
cyclic factorization into k powers W_i^(a_i) of nonempty binary words,
with positive integer exponents. Put R=sum_i |W_i|. Then

    L <= c^(k+3) [ log_2(m+1)/(c-1) + 4cR ],
    c=log_2(3),  m=least ordinary phase.

In particular m<=L^14.3/3 by the logarithmic-form estimate in the
[cycle-height packet](README.md). For fixed k the base words must have
total length at least a positive proportion of L as L tends to infinity.
For R bounded by a fixed power of log L, the number of factors satisfies
k >= (ln L - O(ln ln L))/ln(log_2 3). Both words and exponents may vary
with the cycle. These effective inequalities concern every word
arrangement, though their strength depends on its compression.

The prior dictionary theorem gives a stronger piece-count dependence in its shared domain. [Comparison with papers 15 and 57](../synchronized-cycle-blocks/PRIOR_WORK.md)

## A physical bound for one power

At an ordinary phase x, suppose a word W of length w<L and q ones is
physically repeated a>=1 times within one tour. Write B=2^w, A=3^q
and C for its affine numerator. Then the endpoint z satisfies

    B^a [(B-A)z-C] = A^a [(B-A)x-C].

Because A is odd, B^a divides (B-A)x-C. This integer is nonzero:
otherwise the first copy sends x to itself, impossible before step L
in a primitive ordinary tour. The elementary bounds |B-A|<=3^w and
0<=C<=3^w follow by comparison with the all-ones word. Hence

    aw <= log_2(x+1) + c w.                                  (1)

This bound retains the actual phase; it does not presume a common
slope, a bound on odd densities, or effective S-unit estimates.

## Rotate to the least phase

The assertion is immediate if some base word has length L. Otherwise
cut the cyclic factorization at the least phase. A cut in one factor
creates at most two whole powers of its base and two residual fragments.
Use each nonempty fragment as a power of exponent one. Thus the new
factor count is at most k+3, and the sum R' of its base lengths is at
most 4R. Empty factors are discarded. The cut cannot create any
base of length L. At elapsed time t the ordinary state satisfies
x+1<=(3/2)^t(m+1) since each shortcut branch obeys the same one-step
bound. If the next factor has base length w, (1) gives

    t_next <= c t + log_2(m+1) + c w.

Iteration from zero and the geometric series give the stated bound.
The argument also gives the tighter weighted sum of base lengths when
the cut and all factors are specified. It leaves high-complexity words
unrestricted and gives no conclusion for infinite divergent orbits.

## Left-to-right copy parsing at the least phase

There is a version for a factorization into literals (single bits) and
copies of earlier substrings, with overlaps allowed, of the one-tour
word starting at m. If h bits starting at time t copy bits starting
at time u<t, then the distinct ordinary states x_t and x_u have
difference divisible by 2^h by the common affine composition. Since
both are at most (3/2)^t(m+1), their difference forces
h<=log_2(m+1)+(c-1)t. The same bound holds for a literal because
log_2(m+1)>=1. Thus every such parsing with z factors satisfies

    L <= log_2(m+1) (c^z-1)/(c-1).

This applies in particular to greedy overlapping Lempel-Ziv parsing
with a separate literal when no positive match is available. The
starting phase matters in the copy-parsing bound; the cyclic power-cover
bound above accounts explicitly for moving the cut.

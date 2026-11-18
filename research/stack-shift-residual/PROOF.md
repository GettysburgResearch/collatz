# Combined moments and a shift residual exclude all stack periods through 587

**PROPOSED.** For every positive periodic stack increment word of period
1<=r<=587, every integer initial height m>=0, and every finite positive
steering prefix, the native two-adic stack value is irrational. The
associated stack context therefore cannot be an ordinary integer.

The related combined-moment construction is pinned at author checkpoint
`291bec0490479078e84d06814af0c984de6ec712`,
`research/stack-combined-moments/PROOF.md` (period eighteen). Here a
common divisor of maximal minors improves the coefficient height. The
scalar shift equation then puts a low-degree polynomial through the
forced rational sample points. Counts concern one fixed periodic word as
the approximation order tends to infinity.

## Periodic exponents

Let T=64/81. For periodic increments d_j>=1 with sum S over r positions,
put m_0=m, m_j=m_(j-1)+d_j, E_0=0, E_j-E_(j-1)=9m_j+1, and

    a=9S/r,    F(Y)=sum_(j>=0) T^E_j Y^j,    P_s(Y)=sum_(0<=j<s) T^E_j Y^j.

The difference E_(j+r)-E_j has slope 9S in j. Hence E_j=aj²/2+bj+u_j
for a rational b and bounded r-periodic u_j with u_0=0. For every s>=0
divisible by r, E_(s+j)=E_s+asj+E_j and as is integral. In particular

    F(Y)=P_r(Y)+T^E_r Y^r F(QY),     Q=T^(ar),
    F(1)=P_s(1)+T^E_s F(y_s),        y_s=T^(as).                (1)

The first identity is formal; the second is valid separately in the real
and two-adic completions by direct convergence. Only the two-adic F(1)
is assumed rational in the argument below. Strict convexity of E on the
integers in its domain follows directly from the positive increments.

## Integer coefficients from common maximal-minor divisors

Take n tending to infinity through multiples of 60 and set

    delta=31/30,     D=M=delta n,     mu=M+n/2,
    g_k=floor(a(mu k-k²/2)),          0<=k<=D.

There are integers c_k, not all zero, satisfying

    sum_k c_k T^(g_k+E_(M+i-k))=0       (0<=i<n),
    max_k |c_k| <= H,      log_81 H <= a n²(h+o(1)),  h=21/4.  (2)

To see this, put e_(ik)=g_k+E_(M+i-k), l_i=min_k e_(ik),
h_i=max_k e_(ik), R_i=h_i-l_i. Row scaling gives the integer matrix

    A_(ik)=64^(e_(ik)-l_i) 81^(h_i-e_(ik)).

It has full row rank. In a minor on increasing row and column sets, the
diagonal matching uniquely minimizes the sum of E_(row-column).
Strict convexity shows that swapping an inverted pair reduces the sum.
The row and column offsets do not change this comparison. Thus the unique
minimum has strictly smaller two-valuation than all other determinant
terms. All needed indices here are nonnegative since M=D.

Uniformly over all columns, e_(ik)=a(M+i)²/2+a(n/2-i)k+O(n).
Consequently sum R_i<=a delta n³/4+O(n²). For any injection i->k_i
selecting distinct columns, both sums

    sum_i(e_(i,k_i)-l_i),        sum_i(h_i-e_(i,k_i))

are at least a n³/24-O(n²). Split the rows at i=n/2. Within each
half the relevant nonnegative distances are either k_i or D-k_i;
they are distinct and carry weights |n/2-i|. Rearrangement bounds
their weighted sum below by pairing 0,1,...,n/2-1 with the weights in
descending order. Each half contributes at least
binom(n/2,3)=n³/48-O(n²), before the common multiplier a and the
O(n²) row expansion error. Interchanging min and max swaps the two
column ends and gives the same lower bound.

For sufficiently large n let J be an integer lower bound a n³/24-O(n²)
for both sums. Every maximal minor is divisible by 64^J 81^J. Its
real absolute value is at most n! 81^(sum R_i) T^J, by expanding
its determinant. Thus for the largest absolute minor Delta and the
positive greatest common divisor G of the maximal minors,

    log_81(Delta/G) <= a n³(delta/4-1/12)+O(n²+n log n).         (3)

Take n columns attaining Delta to form B. In B-coordinates each column
of A has components of absolute value at most one, by Cramer's rule.
The index of B Z^n in A Z^(D+1) is Delta/G: the full-minor gcd is
the covolume of the image lattice by Smith normal form. The image of
the box {0,...,H}^(D+1) lies in [-(D+1)H,(D+1)H]^n in B-coordinates,
and each coset modulo B Z^n contains at most (2(D+1)H+1)^n such
points. More box points than images suffice. Taking
(D+1-n)log_81 H larger than the right side of (3) plus O(n log n)
and subtracting two box points proves (2), since
(delta/4-1/12)/(delta-1)=21/4. All constants can depend on the fixed
word and m.

## Rationality forces an exact identity on a geometric grid

Write V(Y)=sum c_k T^g_k Y^k and let U(Y) be the terms of V(Y)F(Y)
of degree below M. By (2), VF-U has formal order at least M+n.
Assume F(1)=xi=A_0/B_0 is rational in the two-adic embedding,
with B_0 positive and odd. Take all multiples s of r such that

    683/100 <= sigma=s/n <= 2641/100.

For all sufficiently large n each such s satisfies the rational identity

    (xi-P_s(1))V(y_s)=T^E_s U(y_s).                            (4)

In the two-adic embedding the difference is T^E_s(VF-U)(y_s). At
degree j>=M+n the T exponent equals

    a[(s+j)²/2+(mu-j)k]+O(j+n),    0<=k<=D.

Use k=D for a lower bound in the leading term. Even after subtracting
a fixed multiple of j+n the quadratic increases throughout this range
for large n, so the valuation of the difference, divided by six, is at
least a n²[(sigma+delta+1)²/2-delta/2]-O(n).

For the right side of (4), j<M and k<=j, giving exponent at most
a(s+M)²/2+anD/2+O(n). Here (s+j)²/2+(M-j)k<=(s+M)²/2.
On the left, the largest relevant exponent is at most E_(s-1)+g_D+asD
and has the same bound. All powers used for clearing are nonnegative.
Clear by the odd integer B_0 81^K with K the largest actual exponent.
Since P_s(1) is bounded in the real embedding and the number of
terms is polynomial in n, the resulting ordinary integer has absolute
value at most

    81^[a n²((sigma+delta)²/2+delta/2+h+o(1))].

Put rho=log_81 64. The dyadic lower bound would exceed this for a
nonzero integer because, over the whole grid,

    rho[(sigma+delta+1)²/2-delta/2] - (sigma+delta)²/2-delta/2-h > 0.   (5)

Indeed 64^100000>81^94639. Replacing rho by 94639/100000 leaves a
concave quadratic with the two positive endpoint values
11598853/6000000000 and 10987957/6000000000. This proves (4)
simultaneously on the compact sampling window, including any point
where V vanishes. In particular V(y_s)F(y_s)=U(y_s) in the two-adic
embedding, without dividing by V(y_s).

## The scalar shift residual

Form the rational-coefficient polynomial

    R(Y)=U(Y)V(QY)-P_r(Y)V(Y)V(QY)-T^E_r Y^r V(Y)U(QY).

Substitute U=VF-B with B of order at least M+n. Equation (1)
cancels all terms involving F; the remaining formal expression is

    R(Y)=-B(Y)V(QY)+T^E_r Y^r V(Y)B(QY).

Therefore Y^(M+n) divides R. Its degree is at most 2D+r-1 because
deg U<=D-1 and deg P_r=r-1. The polynomial R is nonzero. If it
vanished, U/V would satisfy the scalar affine shift equation (1)
as a Laurent series at zero, since V is nonzero. Subtracting from F
would give a Laurent series L(Y)=T^E_r Y^r L(QY). Every nonzero
Laurent series has a finite initial exponent that the right side
increases by r, so L must be zero. But F is not a rational formal
series: a nonzero finite rational recurrence on coefficients T^E_j
would have its term of largest backward shift uniquely least in
two-valuation for large j, since E_j-E_(j-1) tends to infinity.
A constant denominator would instead make F a polynomial, also
impossible since every T^E_j is nonzero.

Whenever s and s+r both belong to the sample window, (4) gives
U=VF at both corresponding two-adic points. With y_(s+r)=Qy_s,
equation (1) now gives R(y_s)=0 exactly. These positive rational
points are distinct and nonzero. After factoring out Y^(M+n) there
are at most D-n+r-1 remaining degrees. But the number of adjacent
sample pairs is at least

    (2641-683)n/(100r)-2.

Since (2641-683)/(100(delta-1))=2937/5>587, the number of these
roots exceeds D-n+r-1 for all sufficiently large n at each r<=587.
This contradiction proves the theorem for a periodic tail. Splitting
off a finite positive steering prefix gives a nonzero rational affine
transfer to the tail at its new initial height. The native context
likewise differs by a nonzero rational affine transformation, as in
PR 20 at `82ca2f932438a9fe0897704ba62959ca23ec830f`, L-9408 and
L-9407 respectively.

The proof establishes the stated fixed-period range. It supplies no
period-uniform conclusion for an arbitrary aperiodic increment word.
The [checker](check.py) verifies the margins and independently replays
small coefficient systems, the scalar identity and the reduced degree.

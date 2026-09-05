# Route 2: the complete source fan has only one deep odd branch

**Status: PROPOSED pending independent review.** This advances ordinary-source
separation using the new common integer rank, rather than assuming numerical
descent at the first coefficient crossing. The SC and cycle results from
passes 2-3 are preserved; neither obligation is promoted. This note's complete
closing criterion treats cycles and divergent components together but remains
conditional on a cover not supplied here.

Use A, z_a, d_a, c_a, and R_* from MOVING_GHOST_RANK.md. A is a total
acceleration of the physical shortcut map, absorbed at 1. Its maximal words
are w_a=1^a0, repeated k times. All congruences and sources below are ordinary.

## 1. T-A3-851: complete inverse formula, including maximality

Fix y>1 and h=v3(2y+1). Every even predecessor of A is

    n=2^k y, k>=1, provided y is odd.                   (1)

If y is even there are no even-source predecessors: maximal halving always
ends odd. This is the one infinite elementary ray.

Every ODD source predecessor has an index 1<=a<=h and a count k satisfying

    v2(z_a(y))<a+1,
    1<=k<=floor(v3(z_a(y))/a),                          (2)

and is exactly

    n_(a,k)(y) = [2^((a+1)k) z_a(y)/3^(ak)-c_a]/d_a,
    n_(a,k)(y)>=2.                                    (3)

There is no additional unexplained integrality condition in (3): the indicated
3-power division and d_a division are exact. Each retained source occurs once.
The absorbing endpoint y=1 is deliberately excluded from this formula.

### Proof

Reversing (5) of the rank note gives (3). The dyadic inequality in (2) says the
endpoint has exited the repeated word; without it, these would be nonmaximal
prefix predecessors and would not be A-predecessors. Conversely (2) gives
v2(z_a(n))=(a+1)k+v2(z_a(y)), hence k is exactly the maximum, and the source
realizes w_a^k by its canonical parity congruence.

Since gcd(d_a,6)=1 and 3^a=2^(a+1) modulo d_a, multiplication by
2^((a+1)k)/3^(ak) leaves z_a(y)=c_a modulo d_a unchanged. Thus the remaining
d_a divisibility is automatic. The positivity test is still essential. The
source is odd and has the stated active mode, by that same parity cylinder.

After the first odd-run block of length a+1,

    2g_a(n)+1=3^a(n+1)/2^a.                            (4)

An odd source therefore has an endpoint in class 1 modulo 3, and the final
endpoint's h is at least a. Equivalently, for a>h, the two terms in z_a(y)
have unequal ternary valuations with minimum h, so v3(z_a(y))=h<a and no k is
possible. This proves the finite index bound. Determinism of the active mode
and exact maximal repetition count proves uniqueness of source coding.

### The single deep column

If 1<=a<h, then y+1 is a ternary unit and

    v3(z_a(y))=a.

Consequently every such branch has k=1. ONLY the moving index a=h can have
k>=2. Thus the full inverse fan consists of:

    an explicit even ray when y is odd;
    at most h-1 one-copy odd branches;
    one finite, possibly deep column at a=h.            (5)

This is a structural collapse of both unbounded word parameters, not a
truncation at a selected maximum run length. The last column is retained,
not declared harmless. Its depth is the exact additional cancellation
v3(z_h(y))/h, the same moving feature that can lower R_*.

## 2. T-A3-852: every integer-rank fiber has an explicit short list

For m>=1 set e=v3(m). If Z=sqrt(m*3^e) is not an integer, the fiber
{n>=2:R_*(n)=m} is empty. Otherwise its complete candidate list is

    Z, Z+1, Z-5,
    (Z-c_a)/d_a for 3<=a<=e.                            (6)

Retain only positive integers n>=2 with R_*(n)=m. Therefore

    #{n>=2:R_*(n)=m} <= max(3,e+1).                     (7)

The zero fiber consists exactly of 1.

Indeed R_a(n)=m means z_a(n)=+/-Z and e=v3(z_a(n)). For a=0,1,2 the relevant
signs give the three first entries. Any minimizing a>=3 equals v3(2n+1), by
the collapse theorem, so v3(z_a(n))>=a and hence a<=e. The positive z_a has
only one ordinary source for each index. Testing the actual envelope removes
extraneous candidates. Formula (7) handles equal-rank plateaus without an
assumption that R_* is injective.

## 3. T-A3-853: a finite complete lower-source test and a sound normalizer

Suppose an exceptional source exists. The nonempty set of its component's
positive integer ranks has a least value. Choose a source n attaining it.
Every source merging with n is also exceptional and has rank at least R_*(n).
Thus neither a forward A-image nor an A-predecessor of smaller rank can occur.
This is a minimum-RANK statement, not an unjustified minimum-cycle-value bound.

The complete one-edge lower-rank search is finite. If x is an inverse source
with R_*(x)<R_*(n), properness R_*(x)>=x-1 gives

    x<=R_*(n).                                         (8)

The even ray (1) therefore needs only those k with 2^k n<=R_*(n). The odd
branches (2)-(3) are already finite. Compute all candidates satisfying (8),
plus the one forward endpoint A(n), and retain strict rank drops. These are
exact finite physical merging diagrams, including numerically larger x.
Do NOT impose (8) on arbitrary intermediate vertices of a longer search;
that would incorrectly discard paths with temporary rank increases.

A deterministic normalizer chooses any retained strict drop and repeats.
Every operation is total, and the positive integer R_* strictly decreases,
so it halts at 1 or at a specifically labelled unresolved residual. Residuals
do occur, as the examples below show. A proof that every residual converges,
or has an additional finite lower-rank merging diagram supplied by a proved
total selector, would complete the argument including cycle exclusion. That
additional cover is not supplied. The one-edge test is NOT claimed complete
for all possible merging diagrams; its already-false universal success is
not proposed as the next hypothesis.

In the frozen finite pilot for 2<=n<=16384:

    13458 have a direct forward rank decrease;
      510 further sources have an inverse rank decrease;
     2415 have neither under the exact one-edge rules.

The residuals include known convergent sources such as 3 and 9. A residual is
an honest failure of this local certificate, not evidence for a counterexample.
No such classification is extrapolated beyond the stated source range.

## 4. T-A3-854: an all-height backward rank reduction

There is also an elementary infinite family, not merely 510 examples. For
EVERY e=4 mod 8, e>=4, put

    x=3^e, y=(9x+7)/16.

Then, exactly,

    A(x)=y with word (10)^2,
    x>y,
    R_*(x)=x,
    R_*(y)=9(x-1)^2/256,
    R_*(x)/R_*(y)<=9/25<1/2.                            (9)

Thus a numerically larger ordinary source gives a strict common-rank merging
reduction, with a ratio tending to zero. The first case is y=46, x=81:

    81 -> 122 -> 61 -> 92 -> 46,
    R_*(46)=225, R_*(81)=81.

### Proof

Write e=4u with u odd. Expanding (1+80)^u-1 shows v2(3^e-1)=4: its first
term has valuation 4 and all other terms have higher valuation. Also
v2(3^e+1)=1. The source has active a=1 and exactly two copies, proving the
physical diagram. The inequality x>y is immediate for x>1.

At x=3^e, h=v3(2x+1)=0 and R_0(x)=x, while R_1 and R_2 are larger.
At y, h=1, so only the three fixed entries enter the envelope. Their exact
values are

    R_0(y)=(9x+7)^2/256,
    R_1(y)=9(x-1)^2/256,
    R_2(y)=3(3x+29)^2/256.

The first and third are larger than the second. This uses y a ternary unit,
v3(y-1)=2, and v3(y+5)=1, each read directly from the displayed formula for y.
Finally 256x/[9(x-1)^2] decreases for x>1 and equals 9/25 at x=81.
This proves every e=4 mod 8. The checker tests 16 values through e=124.

This is a new certificate for this packet's common rank, not a priority claim
for elementary numerical descent of these powers. PR #90's independently
specified minimum-rank and backward-bypass program is credited in the source
record; its theorem is not silently merged or assumed here.

## 5. Exact remaining source-separation problem

The source fan exposes one resonant odd column rather than an uncontrolled
infinite menu. The rank fiber is also finite and explicit. Nevertheless the
residual includes genuine ordinary inputs and needs more than this one-edge
cover. The next target is a recursively closed family of merging diagrams or
an induced unsafe-state inequality. A finite search for ever-larger successful
diagrams does not prove that the search terminates at every residual input.

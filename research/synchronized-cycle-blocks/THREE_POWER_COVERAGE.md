# Three powered factors leave a positive fraction of a cycle uncovered

**PROPOSED, ineffective.** There exist eta>0 and L_0 such that in
any primitive positive ordinary shortcut cycle of length L>=L_0, any
three disjoint cyclic powers of exponent at least two leave at least
eta L uncovered positions. All three binary roots and intervening gaps
are arbitrary. No numerical fraction or period threshold is claimed.

## Stability of the height argument

Argue by contradiction along lengths tending to infinity with total
gap length d=o(L). Write each gap as x -> lambda_i x+e_i:
lambda_i is a positive rational unit at all places except 2 and 3,
and both coefficients have logarithmic height O(d+1) by the usual
affine formula. On ordinary states a gap changes log_2(x+1) by at
most its length. Every power of exponent >=2 has length at most five
times its entry height H(x)=log_2(x+1), and multiplies height by at
most four. Thus a boundary of height O(d+log L) would give every
power length O(d+log L), contrary to the coverage.

The global least phase m has log m=O(log L). It cannot lie in a
gap, since both gap endpoints would have small height. It cannot
lie in an increasing power since the first-copy estimate from the
[single-rise argument](ONE_INCREASING_POWER.md) would give the same
conclusion at its entry. It therefore lies in the last copy of a
decreasing power V. Set H equal to the height at that power's exit.
The three powers and three gaps give L<=240H+O(d) by the forward
sweep, whence d+log L=o(H). All gap heights and cumulative ordinary
logarithmic corrections may now be discarded only after division
by H.

For the decreasing power V of exponent b, base length v and ones p,
the lower-boundary estimates are H<=gamma p+o(H), bcp<=v+H.
If K is the product of the height multipliers over the increases
outside V, then b(v-cp)<=(K-1)H+o(H). Indeed, gap transport during
the sweep adds O(d) since there are at most three physical factors.
These are precisely the limiting inequalities underlying the
[three-factor exponent classification](MULTIPLE_INCREASING_POWERS.md).
When there are zero or one increases, K is at most K_2 and b>=2,
so the positive margin proved in the single-rise argument rules out
the case. There must be exactly two increases and the earlier
classification of their exponents and b applies unchanged.

The remaining descending cube and the descending square with two
increasing cubes are excluded by the same two- and three-form tests as
in the [cube finiteness proof](DESCENDING_CUBE.md). At the junction
between the increasing powers, transport the incoming approximation
through its gap by multiplying all incoming terms by lambda_i. The
additive error e_i has logarithmic height o(H), negligible beside the
junction of height h_1 H, and all the previous exponent inequalities
are unchanged. The rational multiplier has only powers of 2 and 3 in
its numerator and denominator. An exact relation identifying the two
sides would still give v_2(M)>=b'w-O(d) for the outgoing exponent b'
and width w, contradicted by the same strict limiting gaps. Thus only
a descending square and at least one increasing square need remain.

## Stability of the comparison tests

Use the notation and normalization of the
[exact three-power theorem](THREE_POWER_FINITENESS.md).
Orient the layout as U^a, first gap, W^b, second gap, V², third gap.
The expressions in (1) there are now the individual displacements
of the three powered factors, with the same positive integer
multipliers M,N,P and limiting term scales. The polygon (2) there
is unchanged: the gap log changes are o(H). In particular the
transport test (5) persists. In that test multiply both U terms
also by lambda_1 lambda_2. The first gap error, propagated through W,
is negligible relative to z with saving h_1; the second is negligible
with saving h_2. The previous saving min(G,D,h_1/c) is no larger.
Finite-place multiplier costs and successive-scale identifications
are unchanged up to o(H); the final 2-divisibility still contradicts
the strict size bound on M. The two-sum test (6) also persists:
multiply the W terms by lambda_2. Their sum subtracted from the
two V terms is lambda_2 times the entering W state, plus e_2 minus
the V exit state. It has scale h_1>1 because the V exit has scale
one. It is both nonzero and smaller than the two secondary terms
in the range J>G.

The full displacement test costs one extra normalized unit. To see
this, write U_*,W_*,V_* for the three positive displacement sums
(including M,N,P). At the true entry x of U, which has logarithmic
height divided by H tending to one, expansion around the tour gives

    lambda_1 lambda_2 U_* + lambda_2 W_* - V_*
      = (1/lambda_3-lambda_1 lambda_2)x
        -e_3/lambda_3-lambda_2 e_1-e_2.

If d=0 on a subsequence the exact theorem already rules it out.
Otherwise the coefficient of x is nonzero: a nonempty concatenation
of gaps has lambda_1 lambda_2 lambda_3=3^k/2^d distinct from one.
This coefficient and its inverse have logarithmic height O(d+1),
and the remaining error terms have the same height bound. The
displayed difference therefore has limiting logarithmic height one.
In dimension a+b+2 use the scaled monomial terms as coordinates.
At infinity replace one largest term by the displayed signed sum;
at 2 and 3 use the coordinate forms. The resulting normalized
product is at most

    2^((1-h_2)H+o(H)) M^a N^b P² H_projective^(-(a+b+2)).

There is no outside-prime cost from any lambda_i. Consequently
if h_2-1>am+bn+2p_0 in the notation of the exact proof, the
Subspace Theorem gives a fixed rational relation. Provided the
retained scales in (3) are distinct (after removing the largest V
term), this forces a multiple of the original signed sum: eliminate
that term using the displayed identity, and successively compare
all the other scales. Even the smallest retained scale is strictly
greater than one (G,J>0), whereas the discrepancy has scale one.
The discrepancy is nonzero, a contradiction.

For (a,b)=(3,2) the strengthened full margin is positive everywhere.
For (2,3), wherever it is nonpositive the undiminished transport
test has a strict margin, and that test also covers the coincident
ray. The [rational polygon certificate](check_three_power_cones.py)
checks these comparisons after subtracting one. For a=2,b>=4 and
a>=4,b=2 only the undiminished tests were needed even in the exact
proof. This excludes every nonsquare possibility from an unbounded
family with d=o(L).

## Three squares with gaps

Set a=b=2. Write X_1,X_2 for the two terms of lambda_1 lambda_2 U_*,
X_3,X_4 for those of lambda_2 W_*, and X_5=P2^v, X_6=P3^p.
Write E for the signed sum above. Outside the coincident rays,
the six X_i admit no fixed rational linear relation along an infinite
subsequence. Indeed, substitute X_5 in terms of the other five and E;
the resulting six scales are pairwise distinct, the last being exactly
one. The preceding transport test already excludes the coincident rays.

Put Q=3^(2t)/2^(2w), and let
s=min(G,D,h_1/c). The W square carries its entry y to Qy+F,
where F/Q has normalized logarithmic size at most h_1-h_1/c.
This follows from the intermediate-state lower bound in the
[exact transport proof](THREE_POWER_FINITENESS.md): the relative
error of multiplicative transport through the square is at most
2^(-(h_1/c)H+o(H)). The gaps have coefficients of height 2^o(H).
Use either of the following seventh coordinates.

* Forward, append R=Q X_1. Then R has scale h_2 and
  |R-X_5|/R <= 2^(-(G/2)H+o(H)). Indeed X_1+X_2 transports to
  the upper boundary with relative error of exponent at least
  min(G,h_1/c), X_2/X_1 has exponent -G/2, and replacing the
  upper boundary by X_5 costs relative error of exponent -D.
  Both D and h_1/c exceed G/2.
* Reverse, append R=X_5/Q. This has scale h_1 and
  |R-X_1-X_2|/R <= 2^(-s H+o(H)). This follows by dividing
  the upper-boundary comparison by Q; the three losses come from
  the entry x in x+U_*, the omitted descending term X_6, and F/Q.
  Gap offsets at the three junctions only add errors of normalized
  size at most zero at the junction where they enter.

Use E in place of X_5 at infinity, and replace R by the indicated
comparison form at infinity. These two replacements preserve linear
independence because E contains X_5 and the seventh comparison has
R coefficient one. Keep the seven coordinate forms at 2 and 3.
Writing m,n,p_0 for the multiplier scales as before, set
B=G+J-2m-2n-2p_0. The same projective product estimate then gives
a fixed rational linear relation on an infinite subsequence whenever

    forward: B+G/2-m>0,        or        reverse: B+s-p_0>0.

In fact the two archimedean gains are h_2-1=G+J and the seventh
coordinate's stated gain. Its additional outside-prime charge is
respectively M or P. All seven projective coordinates have logarithmic
height O(H). If a comparison form already vanishes, it itself gives
a relation.

A relation involving the seventh coordinate is impossible even on the
coincident rays. In the forward case every original coordinate has
2-adic valuation at least -O(d), so the new term forces
v_2(M)>=2w-o(H); the factor 3^q is odd. In the reverse case the
original coordinates have 3-adic valuation at least -O(d), forcing
v_3(P)>=2t-o(H). Since ct-w<=gamma min(t,w), each of 2w/H and
2t/H has lower limit at least J/gamma. The rational certificate gives
J/gamma>max(m,p_0)+1 throughout the feasible region. Hence any relation
would use only the six originals, already impossible off the rays.

Finally apply the [same rational vertex certificate](check_three_power_cones.py)
with a=b=2. On each intersection where the three-coordinate transport
test and the reverse seven-coordinate test both have nonpositive
margin, the forward margin exceeds 1/2. The former test also handles
every coincident ray. This rules out the last square configuration.
If no positive eta and L_0 worked, choosing successive gap fractions
1/n and period thresholds n would give the excluded sequence.

## Two large roots of opposite signs in a four-power cover

For an exact cover by four powers, the least state lies in the last
copy of a decreasing power of exponent at most five. At least one
increasing factor has exponent at most eighteen, and at least one of
the four selected exponents is two. These finite exponent conclusions
also hold eventually for four powers covering all but o(L) positions
along an unbounded sequence. In the latter case both a rising root and
a descending root have width bounded below by a fixed positive
multiple of L, simultaneously.

Indeed write b for the exponent of the minimum-containing descent
and K for the product of the height amplification bounds on the at
most three rising factors. Use the [sweep inequalities](FRAGMENTED_COVERS.md)
with this exact b, retaining the different exponent floors for the
other factors. Its margin is mu=1-gamma(b+K-1)/(b(b-1)c).
If every descent has exponent >=6, or just this particular b>=6,
take b=6 and K<=A_2^3. If every increase has exponent >=19,
take b=2 and K<=A_19^3. If all four powers are cubes or higher,
take b=3 and K<=A_3^3. In every case mu>1/250, as follows by
substitution with 1054/665<c<485/306 using the lower endpoint only
for c in the denominator of the margin. Increasing b only improves
the margin. All three bounds have K<56.

In an exact cover there is at least one descent by strict cyclic
monotonicity, and in all cases K<64 even using three squares.
If the least phase lies in an increase, its first-copy bound gives
an entry height J<=4Z. Otherwise in the configurations just listed,
the exit of its descent has J<=250(Z+s), where Z=log₂(2m+2),
s=log₂(L+1). Each powered length is <=5KJ, so with t=log₂ L,
Z<=16t and s<=2t, one obtains L<=5760000t. This is incompatible
with the verified period floor L>2^36 since 2^t/t is increasing
there. Thus the minimum is in a descent and none of the three
configurations occurs.

For d=o(L) uncovered positions, a minimum in a gap or an increase
gives a starting boundary of height O(log L+d). Even allowing four
rises, this bounds all four lengths by O(log L+d), impossible. For
a minimum-containing descent, in each excluded configuration the same
positive margin gives J=O(log L+d), again a contradiction. Finally
remove any one of the four factors. The three-power theorem above
shows its length plus d is at least eta L. Thus all four lengths
are eventually at least eta L/2. Dividing by the bounded exponents
produces a rising root of width >=eta L/36 and a descending root
of width >=eta L/10.

## Four powers with a quartic or quintic minimum-containing descent

In any growing family of four powers covering all but o(L) positions,
the descent containing the global minimum has exponent at most **three**.
Thus the descending root in the preceding conclusion actually has width
at least eta L/6 eventually. Exact four-factor covers with a quartic or
quintic minimum-containing descent are at most finite, ineffectively.

Suppose its exponent is d=4 or 5 and normalize by its exit height H.
The sweep gives L=O(H) since the four gaps have total length o(L).
The two local bounds dcp<=v+H and p/H>=1/gamma+o(1) for this descent
force its normalized entry height to be at least
F(d)=1+d(d-1)c/gamma-d in the limit. Fewer than three rises give upper
bound A_2²<F(4), so all other powers are rising. Label them 1,2,3
in cyclic order after the descent, with exponents e_i, widths w_i
and odd counts q_i. For d=5, A_2² A_3<F(5) requires all three squares.
For d=4 both A_2² A_4 and A_2 A_3² are below F(4); only three squares
or two squares and one cube remain. There are thus five ordered cases.

Pass to limits g_i=(cq_i-w_i)/H, h_0=1, h_i=h_(i-1)+e_i g_i,
and let m_i be the normalized logarithms of the positive integer
multipliers M_i in the two endpoint brackets. The gain and multiplier
bounds already proved above are

    g_i>=0,    0<=m_i<=h_(i-1)-(e_i-c)g_i/gamma,    h_3>=F(d).

For i<j let Q be the product of all intervening gap slopes and every
intervening powered slope (so j=i+2 uses a complete middle power).
For k=1 or 2 compare the following expressions at the entry to power j:

    sum_(a=0)^(k-1) R_a,  R_a=Q M_i 3^((e_i-1-a)q_i) 2^(a w_i);
    S=M_j 2^(e_j w_j)/3^(q_j).

Their difference relative to the leading term is at most
2^(-sH+o(H)), where s=min(k g_i,g_j,h_i/c). Indeed at the exit y of
power i the leading untransported term is y(1-2^(w_i)/3^(q_i)) plus
C_i/3^(q_i), with C_i the affine bonus. Summing k terms multiplies this
by the first k terms of the geometric series. At the entry to j the
analogous starting bracket gives S as that entry times
1-2^(w_j)/3^(q_j), plus C_j/3^(q_j). The bonus bounds
C_l/3^(q_l)<=2^(w_l-q_l) and (w_l-q_l)/H<=gamma h_(l-1)/c+o(1)
give relative errors no greater than 2^(-(h_i/c)H+o(H)) at the two
endpoints. Any middle ascending power has all odd states of log height
at least (h_i/c)H-o(H), by the intermediate-state estimate of the
three-power proof. Its physical transfer is its homogeneous multiplier
times 1+O(2^(-(h_i/c)H+o(H))); gap offsets at the original junctions
are of height 2^o(H). This proves the claimed relative error.

A test (i,j,k) excludes any tuple on which s>k m_i+m_j, with the
additional condition s>g_i for k=2. For k=2 the tested tuples also
have g_i>0, as follows already from the positive margin and the stated
gain conditions (s<=2g_i). The fixed (k+1)-coordinate Subspace
Theorem comparison at infinity, 2 and 3 charges only M_i^k M_j.
If it gives a linear relation then successively comparing the leading
terms and, for k=2, the smaller term of relative scale 2^(-g_i H+o(H)),
forces S to equal the displayed sum exactly. If the sum was already
exact the same conclusion holds directly. The power of 2 in the
denominator of Q from any intervening power only strengthens the
consequence v_2(M_i)>=e_j w_j-o(H), since the sum after removing
Q M_i is odd. But e_j w_j/H>=e_j g_j/gamma+o(1)>m_i in the cases
where the test is used.

The [exact three-variable cone certificate](check_four_power_cones.py)
uses the outer rational bounds C=485/306, replacing c by C also in
F(d) and h_i/c. It checks the divisibility contradiction throughout
the feasible region for each test. For d=5, and for d=4 with one cube,
(1,2,1) alone always applies. For d=4 and three squares, at least one
of (1,2,2), (2,3,1), (1,3,1) applies. For each combination of failed
margins the bounded intersection of the corresponding closed
halfspaces has no vertex, by integer determinants. This proves the
assertion without presupposing equal base lengths or equal rising
slopes.

# Three powers covering nearly a whole cycle must all be squares

**PROPOSED, ineffective.** There exist eta>0 and L_0 such that, in
any primitive positive ordinary shortcut cycle of length L>=L_0, any
three disjoint cyclic powers of exponent at least two, at least one
of which has exponent at least three, leave at least eta L uncovered
positions. Both the root words and the three gaps are arbitrary.
Equivalently, if three powers cover 1-o(1) of a sequence of growing
cycles, eventually all three selected exponents equal two; two
factors increase and one decreases. For three squares the argument
does not establish a positive uncovered fraction.

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
family with d=o(L). Failure of the stated uniform eta,L_0 claim
would give just such a family by choosing successive fractions 1/n
and lower length thresholds n. The proof does not compute eta or L_0.

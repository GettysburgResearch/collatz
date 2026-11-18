# Finiteness for three powers with a descending cube

**PROPOSED, ineffective.** There are only finitely many primitive
positive ordinary shortcut cycles covered by two increasing squares
and one decreasing cube. The three base words may vary with the
cycle. Combined with the [effective exponent classification](MULTIPLE_INCREASING_POWERS.md),
this forces the decreasing exponent to equal two in every unbounded
family of three-power cycles. Individual cycles in the finite
descending-cube exception are not excluded.

## Shape forced by the physical brackets

Suppose an unbounded sequence exists. In cyclic order write the word
U² W² V³ starting at the lower boundary x after V. Write y for the
boundary between U and W, and z for the boundary between W and V.
Use u,w,v for the base lengths, and q,t,p for their respective odd
counts. Put c=log_2 3, gamma=c-1, k=gamma/(1-gamma), H=log_2(x+1).
As shown in the three-factor classification, the least phase m must lie
in the last copy of V. Every boundary height is <=16H by (1) of the
single-rise proof. Each full factor has length <=5 times its entry
height, so L<=240H. Thus log L=o(H) and H tends to infinity.

In the following estimates pass to a subsequence on which all lengths,
counts and boundary log heights divided by H converge. They are bounded
by L/H<=240. Write g_1,g_2 for the limiting ratios of cq-u and ct-w
to H, and h_1,h_2 for the limiting log heights of y,z divided by H.
The bounded total correction gives

    h_1=1+2g_1,       h_2=1+2(g_1+g_2).

The starting brackets give u/H<=1+g_1+o(1) and w/H<=h_1+g_2+o(1).
Indeed for any increasing square of width l and a ones the exact bound
is 2l<=ca+log_2(x_in+2^(l-a)). If 2^(l-a)>x_in then this implies
2l<=l+gamma a+1<=cl+1, so l=O(1), harmless after normalization.
Since each increment ca-l is at most gamma l, it follows that
g_1<=k and g_2<=k h_1.

Writing H_0=H at the cube's exit, the minimum and the ending bracket
give H<=gamma p+O(log L), 3cp<=v+H. The actual log drop along
the cube gives h_2=1+3(v-cp)/H+o(1). Therefore

    h_2 >= 6c/gamma-2,      g_1+g_2 >= (6c/gamma-3)/2.

Combining with g_2<=k(1+2g_1) and g_1<=k gives
g_1>1.3, g_2>5.1, k<1.42 and h_1<3.85. The
[exact rational inequalities](check_single_rise.py) use
1054/665<c<485/306.

## Approximation at the intermediate boundary

Let C_U,C_W denote the affine bonuses. At y the ending 3-bracket
of U² and the starting 2-bracket of W² supply positive integers

    M=((3^q-2^u)y+C_U)/3^(2q),
    N=((3^t-2^w)y+C_W)/2^(2w).

The bounds C_U<=3^q 2^(u-q), C_W<=3^t 2^(w-t) show

    limsup (log_2 M)/H <= 1-(1/gamma-1)g_1 < 0.09,
    limsup (log_2 N)/H <= h_1-(1/gamma-1)g_2 < 0.25.

For clarity, (u-q)/H <= (gamma(1+g_1)-g_1)/c+o(1)<=gamma/c+o(1),
and similarly (w-t)/H<=gamma h_1/c+o(1). Thus the bonus terms are
exponentially smaller than y after division by the appropriate power
of three. The stated multiplier bounds follow by using
u/H>=g_1/gamma+o(1), w/H>=g_2/gamma+o(1).

The quantities R=3^q M and S=2^(2w)N/3^t satisfy

    |R/y-1| <= 2^(-(cq-u)) + 2^(u-q)/y,
    |S/y-1| <= 2^(-(ct-w)) + 2^(w-t)/y.

Since h_1>3.6, g_1>1.3 and g_2>5.1, each difference decays faster
than 2^(-H) along the chosen subsequence, up to a bounded constant.
In particular |R-S|/R<=2^(-H+o(H)), while MN<=2^(0.34H+o(H)).

## Fixed rational forms at three places

Apply the rational p-adic Subspace Theorem with places infinity, 2
and 3 to (R,S), taking forms (X-Y,Y) at infinity and (X,Y) at the two
finite places. Write H_* for the multiplicative projective height.
The normalized product of forms is bounded above by

    (|R-S|/R) MN H_*^(-2).

Indeed outside the three places both coordinates are integral, and
the product of |RS| over the three places is at most MN, as their
other factors are powers of 2 and 3. Clearing by 3^t also gives
log_2 H_*=O(H) from the length and multiplier bounds. The product is
therefore <H_*^(-2-epsilon) for some fixed epsilon>0 and all large H
unless R=S already. The theorem places the points on finitely many
rational lines. Since R/S tends to one, the only possible eventual
ratio is one. But R=S forces 2^(2w) to divide M, inconsistent with
the displayed bound on log_2 M and w/H>=g_2/gamma+o(1). This
contradiction rules out unbounded L. Each fixed L has finitely many
words, each with at most one fixed positive starting state.

The cited theorem supplies no effective upper bound on the exceptional
lengths. [Evertse, *The p-adic Subspace Theorem*, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

## A descending square and two increasing cubes

**PROPOSED, ineffective.** Only finitely many primitive positive ordinary
cycles admit a cyclic cover U³ W³ V² with U,W increasing and V decreasing.
Consequently in any unbounded family of three-power tours the decreasing
factor and at least one of the two increasing factors must both be squares.

Use the same boundary x,y,z, normalized height H and limiting notation.
Now k'=gamma/(3-c). For an increasing cube the same bracket shows
2u/H<=1+g_1+o(1) and 2w/H<=h_1+g_2+o(1): the competing bonus-dominated
case would imply 3u<=cu+1. Hence g_1<=k', g_2<=k'h_1,
h_1=1+3g_1 and h_2=1+3(g_1+g_2). At the descending square
2cp<=v+H, p/H>=1/gamma+o(1), so h_2>=2c/gamma-1. Put
D_0=(2c/gamma-2)/3. The resulting constraints give

    g_1+g_2 >= D_0,     0.32 < g_1 < 0.415,     g_2 > 0.72.

The middle-boundary integers are now
M=((3^q-2^u)y+C_U)/3^(3q) and N=((3^t-2^w)y+C_W)/2^(3w).
As before the bonuses divided by 3^q and 3^t are negligible beside y.
Therefore

    limsup (log_2 M)/H <= 1-g_1/k',
    limsup (log_2 N)/H <= h_1-g_2/k'.

In particular the limiting upper bound on (log_2(M²N))/H is at most
3+3g_1-(2g_1+g_2)/k'. This is at most 3-D_0/k'+(3-1/k')k'<0.50,
as 3-1/k'>0. The [rational replay](check_single_rise.py) checks all
strict numerical inequalities.

Set R_0=M3^(2q), R_1=M3^q 2^u, S=N2^(3w)/3^t. Multiplying the
identity for M by 1+2^u/3^q gives

    R_0+R_1 = y(1-(2^u/3^q)^2) + (C_U/3^q)(1+2^u/3^q).

The identity for N gives S=y(1-2^w/3^t)+C_W/3^t. Thus the relative
difference |S-R_0-R_1|/R_0 is <=2^(-0.64H+o(H)): the two slope gaps
are 2g_1 and g_2, and the two bonus-to-y gaps exceed 0.64. For example
(u-q)/H<=gamma/(2c)+o(1) and (w-t)/H<=gamma h_1/(2c)+o(1) follow
directly from the width bounds above. Also R_1/R_0=2^(-g_1 H+o(H))
with g_1<0.415, so the difference is o(R_1).

Use the coordinate forms at 2 and 3. At infinity replace the first
coordinate form X_0 by X_0+X_1-Y. As in the dimension-two proof,
the normalized product is at most

    |R_0+R_1-S|/R_0 times M²N times H_*^(-3).

The fixed positive gap between 0.64 and 0.50 gives a Subspace
Theorem inequality, since log H_*=O(H). Along an infinite subsequence
there must be a nonzero fixed rational relation
a R_0+b R_1+d S=0, also allowing the case S=R_0+R_1 directly.
Dividing first by R_0 gives a+d=0. Subtracting those terms and dividing
by R_1 gives b+d=0. Hence the relation forces S=R_0+R_1. Its right
side is M3^q(3^q+2^u), with 2-valuation exactly that of M.
But 2^(3w) divides the numerator defining S, so 2^(3w) divides M.
This is impossible since w/H>=g_2/gamma+o(1) and log_2 M/H<=1+o(1).
As in the first theorem, no effective upper bound for exceptional
lengths is obtained.

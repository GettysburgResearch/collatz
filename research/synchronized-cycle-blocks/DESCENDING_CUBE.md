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

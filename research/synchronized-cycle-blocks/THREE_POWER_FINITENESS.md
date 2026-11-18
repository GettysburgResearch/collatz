# Finiteness of primitive positive cycles with three arbitrary powered factors

**PROPOSED, ineffective.** Only finitely many primitive positive ordinary
shortcut Collatz cycles admit a cyclic parity factorization U^a W^b V^d
with nonempty binary root words and a,b,d>=2. All three roots and
exponents may vary. No effective maximum period or elimination of the
finitely many possible exceptions is obtained. The
[effective classification](MULTIPLE_INCREASING_POWERS.md) and
[earlier two configurations](DESCENDING_CUBE.md) are inputs below.

A key distinction from a three-block gcd calculation is that the
ordinary displacement of a powered block is an integer times a
geometric sum. At an intermediate state on an increasing block, the
next increasing block stays exponentially far above the least phase
on the logarithmic scale below. Its smooth slope consequently
transports an approximation without charging its integer multiplier.
The complementary method applies the Subspace Theorem to the full
displacement equation. Wren's Section 5 discusses the obstruction to
extending his two-block gcd directly to three arbitrary blocks.
[Paper 57 v1](https://rstation.ai/problems/collatz/papers/57/v1)

## Reduction to two rises and a descending square

Suppose L tends to infinity through such cycles. The cited results
reduce us, on a subsequence, to a descending square V² and two
increasing powers U^a,W^b, at least one of a,b equal to two. The
global least state lies in the last V copy. Write x,y,z for the
successive boundary states before U, W, V; thus x<y<z. Write u,w,v
for root lengths and q,t,p for their ones. Let c=log_2 3,
gamma=c-1, H=log_2(x+1). The three-factor sweep gives L<=240H,
so H tends to infinity and log L=o(H).

For a root having slope numerator A=3^ones and denominator B=2^width,
the two brackets identify the same positive integer multiplier at
both ends. In particular there are positive integers M,N,P with

    y-x = M sum_{i=0}^{a-1} 3^((a-1-i)q) 2^(iu),
    z-y = N sum_{i=0}^{b-1} 3^((b-1-i)t) 2^(iw),
    z-x = P (2^v+3^p).                                       (1)

Indeed the integer is |(B-A)x_in-C|/B^e at entry and
|(B-A)x_out-C|/A^e at exit. Each one-copy displacement evolves by
the slope, giving (1).

Pass to a subsequence with limits for all normalized quantities
below. Write G,J for the limits of a(cq-u)/H and b(ct-w)/H,
respectively, and m,n,p_0 for the limits of the logarithms base
two of M,N,P divided by H. The endpoint log heights divided by H
tend to 1, h_1=1+G, and h_2=1+G+J: the total ordinary logarithmic
correction is O(log L). Set D=(G+J)/2 and d_e=e gamma/(e-c).
For fixed a,b the following upper estimates and feasible region apply:

    0<=G<=d_a,  0<=J<=d_b(1+G),  D>=1/gamma,
    m<=m_*=1-G/d_a,   n<=n_*=1+G-J/d_b,
    p_0<=p_*=D-1/gamma.                                      (2)

For an increasing power, ew<=c h+log_2(x_in+2^(w-h)) by the
starting bracket. If the power-of-two summand dominates, ew<=cw+1
and w is bounded. Otherwise (e-1)w<=H(x_in)+(ch-w)+O(1).
In either case the width estimate holds up to O(1) uniformly.
Since ch-w<=gamma w, it gives the two gain bounds; alternatively
the direct height amplification bound of the sweep gives them.
The multiplier at entry has logarithm at most
H(x_in)-(e-1)w+(ch-w)+O(1), whenever the state dominates.
For fixed e in the bounded-width alternative the error is harmless.
This proves the stated multiplier bounds. At the decreasing square
we have p/H>=1/gamma+o(1) and (v-cp)/H=D+o(1); positivity of P
and its exit bracket give p_0<=1+D-c/gamma=D-1/gamma. In endpoint
cases where an exponent varies, d_e decreases in e, so one uses its
stated lower floor in the gain bound. The multiplier of the variable
power is never used.

All the domains below satisfy G,J>1/10, as the rational vertex
certificate checks. Consequently the logarithms divided by H of the
successive terms in the three sums (1), in decreasing order within
each sum, are

    h_1-i G/a,        h_2-i J/b,        h_2 and 1+D.           (3)

Use the first or second progression only when that exponent is fixed.
These values follow since each leading term has the height of the
corresponding displacement and successive terms have the indicated
ratio. The third progression follows for all cases.

## Three fixed-form tests

The Subspace Theorem below uses only infinity, 2 and 3. Every
coordinate is a power of 2 and 3 times one of M,N,P. Its numerator
and denominator have O(H) binary digits in every test, including
the tests allowing unbounded exponents since the physical lengths
are <=L. [Evertse, *The p-adic Subspace Theorem*, Theorem 1.1](https://pub.math.leidenuniv.nl/~evertsejh/dio2011-padicsubspace.pdf)

**Full displacement test (fixed a,b).** If the retained scales in
(3), after removing 2^v P, are all distinct, an unbounded sequence
requires

    h_2 <= a m + b n + 2 p_0.                                 (4)

Indeed the three sums satisfy one exact signed linear identity.
Use the a+b+1 retained terms as coordinates and the removed term
as their signed sum. Any a+b+1 of the resulting forms are independent.
The common gcd of all terms is g=gcd(M,N,P), since each geometric
sum has two endpoint monomials that are coprime. Dividing through
by g makes the retained coordinates primitive. At each place omit a
form of largest absolute value, passing to a subsequence with fixed
choices. At 2 and 3 this largest absolute value is one. At infinity
it is 2^(h_2 H+o(H))/g. By the product formula, the product over
these places of all forms before omission is at most
(M/g)^a (N/g)^b (P/g)^2: outside the three places the unit factors
contribute nothing. If (4) fails, the product after omission is
<=2^(-epsilon H) for some epsilon>0. Applying the Subspace Theorem
gives a fixed rational linear dependence among the retained terms
along an infinite subsequence. This is impossible since their distinct
limiting logarithmic heights make the largest term in any such
dependence unique. Only the scale 1+D can coincide with an ascending
term: all U scales are <=h_1 and all W scales exceed h_1.

**Transport of the first square (a=2).** An unbounded sequence requires

    min(G, D, h_1/c) <= 2m + p_0.                              (5)

By (1), y=M(3^q+2^u)+x. Each intermediate state in the first W
copy is at least y/2^(w-t), by ignoring the increases at odd steps.
Later copies have larger states at the same offset. The width estimate
in (2) gives (w-t)/H<=gamma h_1/c+o(1), since
w-t=(gamma w-(ct-w))/c and (b-1)w<=H(y)+(ct-w)+O(1).
Thus every state on W^b has log height at least
(h_1/c)H-o(H). The product of its ordinary corrections
1+1/(3x_i) differs from one by at most 2^(-(h_1/c)H+o(H)),
even for varying b, since L=O(H).
Put Q=3^(bt)/2^(bw). Then z is approximated by

    R_0=QM3^q,   R_1=QM2^u,   through their sum,

with relative error at most 2^(-min(G,h_1/c)H+o(H)).
Also z=P2^v+P3^p+x, and S=P2^v alone has relative error
<=2^(-DH+o(H)). If (5) fails, replacing the first coordinate form
by X_0+X_1-Y at infinity gives the normalized product of forms
on (R_0,R_1,S) at most

    (|R_0+R_1-S|/R_0) M² P H_projective^(-3).

This is the same product-formula estimate as in the
[three-form antecedent](DESCENDING_CUBE.md). The positive margin
gives a fixed rational dependence on a subsequence, or the displayed
sum already vanishes. Since R_1/R_0 has gap G/2 and each of
G,D,h_1/c strictly exceeds G/2, substitution in that relation at
the two successive scales forces S=R_0+R_1. Indeed the coefficients
of the two leading forms must sum to zero, followed by the
coefficients at the smaller scale. But then 2^(v+bw) divides M:
3^(bt)(3^q+2^u) is odd. This contradicts m<=1 and v/H>=c/gamma+o(1).

**Two displacement sums at the upper boundary (b=2, J>G).** An
unbounded sequence requires

    J <= 2n+2p_0.                                              (6)

Subtract the last two sums in (1). Their difference y-x has relative
size <=2^(-JH+o(H)) beside z. Use four coordinates N3^t,N2^w,
P2^v,P3^p, replacing the first coordinate form at infinity by the
signed sum. As above the normalized product is at most its relative
error times N²P² times H_projective^(-4). If (6) fails this gives
a fixed rational relation. The two leading terms have scale h_2;
the other two have gaps J/2 and D, in strict order 0<J/2<D<J.
The discrepancy y-x is smaller than either of these terms. In any
fixed relation the successive coefficients must therefore be
proportional to the exact signed four-term comparison, forcing
y-x=0. This contradicts strict increase along U.

## Exhausting the remaining shapes

All tests have fixed dimension and rational forms. For clarity the
following finite planar comparisons use outward rational bounds.
Set C=485/306>c, replace d_e by e(C-1)/(e-C), replace 1/gamma by
1/(C-1), and replace c in h_1/c by C. The constraints in (2) then
give a closed outer polygon, and m_*,n_*,p_* from these replacements
are upper bounds. The [rational certificate](check_three_power_cones.py)
intersects each pair of boundary lines and evaluates the indicated
affine functions at every feasible vertex. A nonempty bounded
intersection, also when restricted to a line, has a vertex.
The verified strict margins (in units of H) are as follows.

| Ascending exponents | Exact comparison with outward bounds |
| --- | --- |
| a=b=2, or a=2,b=3 | Wherever the lower bound on h_2-am_*-bn_*-2p_* is nonpositive, each of G,D,h_1/C exceeds 2m_*+p_* by more than 1/10. The same transport margin holds on every coincident-scale ray in (3). |
| a=3,b=2 | The full displacement margin exceeds one everywhere. The polygon meets no coincident-scale ray. |
| a=2,b>=4 | Using b=4 in the gain cap enlarges the polygon. The transport margin exceeds 1/10 everywhere and uses no n. |
| a>=4,b=2 | Using a=4 in the gain cap enlarges the polygon. Both J-G and J-2n_*-2p_* exceed 1/10 everywhere. The two-sum test uses no m. |

In the last two rows all coordinates come from three or four fixed
rational forms, respectively; passing to a subsequence does not
require holding the other exponent fixed. These rows and the three
fixed pairs exhaust the cases left by the earlier results. This
contradicts unbounded L. At any fixed L there are finitely many
words, and each has at most one positive periodic initial value.
The Subspace Theorem leaves the possible finite exceptions
ineffective, so finiteness here is not complete exclusion.

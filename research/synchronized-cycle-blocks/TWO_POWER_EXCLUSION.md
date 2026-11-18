# No primitive ordinary cycle consists of two word powers

**PROPOSED, with source-qualified Rhin and Eliahou inputs.** No primitive
positive ordinary shortcut Collatz cycle has a cyclic parity word
U^a V^b with U,V nonempty and a,b>=2. Both base words and both exponents
are unrestricted. The local argument gives L<65536 for any candidate.
Eliahou's lower bound excludes that entire range for nontrivial cycles.
The primitive trivial cycle has length two and cannot accommodate the
two powers.

This strengthens the ineffective two-power corollary of the separate
[commutator argument](POWER_COMMUTATORS.md). The arbitrary-flank claims
there are distinct. Here all of one tour is covered by the two powers.

Fourier Wren derives the powered-block brackets and two-block commutator in paper 57. [Prior results and scope comparison](PRIOR_WORK.md)

## Direction and location of a minimum

For a word W of length w, with q ones, write A=3^q, B=2^w, and let C
be its affine numerator, so one copy sends x to (Ax+C)/B. Moving every
one to the end maximizes C, since changing 10 to 01 raises C. Therefore
C<=2^(w-q)(3^q-2^q)<3^w. If an ordinary segment W^e goes from x to z,

    B^e ((B-A)z-C) = A^e ((B-A)x-C).                         (1)

The right parenthesis is nonzero if w is a proper length in a primitive
tour: otherwise one copy returns x to itself. Since A and B are coprime,
B^e divides the right parenthesis, and A^e divides the left parenthesis.
When A<B and e>=2, a rising segment would give a positive integer
C-(B-A)x<=C<B² divisible by B^e, impossible. Thus each subcritical
power strictly decreases, whereas a supercritical power with A>B always
increases. Equality A=B is impossible.

A two-power cycle consequently has one power of each type. Rotate to
write U^a increasing from x to y, then V^b decreasing from y to x.
Put u=|U|, v=|V|, q=ones(U), p=ones(V), L=au+bv. The values at each
fixed offset within U strictly increase across successive copies because
the same prefix affine function has positive slope; those within V
strictly decrease. The global least phase m therefore occurs in the first
copy of U or the last copy of V.

Let c=log_2 3, gamma=c-1, Z=log_2(2m+2), s=log_2(L+1). In the first
case x<=2^(u-q)m by tracing back from m, since an inverse odd step
shrinks and an inverse even step doubles. In the second case
x+1<=(3/2)^p(m+1) by tracing forward: each odd step increases the
state plus one by a factor at most 3/2, and an even step never
increases it. Set H=u-q in the first case and
H=max(u-q,gamma p) in the second. Then

    log_2(x+2^(u-q)) <= H+Z.

Applying the two respective divisibilities in (1) at the common lower
boundary x gives

    a u <= c q + H + Z,
    b c p <= v + H + Z.                                       (2)

For the first, use (3^q-2^u)x+C_U<=3^q(x+2^(u-q)). For the second,
use 0<(2^v-3^p)x-C_V<=2^v x; the sign follows from the decreasing
V orbit, including at its endpoint by (1).

The product of all ordinary step corrections gives
2^L/3^(aq+bp)<=L+1 as in the [primitive cycle estimates](../cyclic-shift-distance/README.md).
In particular

    b v <= gamma a u + b c p + s.                             (3)

## An explicit upper bound

Use c<8/5, gamma<3/5, as 3^5<2^8. If H=u-q, (2) gives
a u<=c u+Z, hence a u<=5Z. By (2) and (3),

    (b-1)v <= gamma a u + u + Z + s,
    b v <= 13Z + 2s.

Suppose instead H=gamma p. Substituting the second bound of (2)
into (3) after dividing (3) by b gives

    ((b-1)c-gamma)p <= (a/b)gamma u + Z + s/b.                (4)

The coefficient on the left is (b-2)c+1>=b/2>=1. Using (4) with its
weaker lower bound 1 in the first inequality of (2) yields

    (1-c/2-gamma²/2)a u <= c Z + gamma s/2.

Its coefficient is greater than 1/50. Thus a u<=80Z+15s. Using instead
the lower bound b/2 in (4) gives b c p<=c gamma a u+2c Z+c s. Therefore

    L <= (1+gamma+c gamma)a u + 2c Z + (1+c)s
      <= 208 Z + 41s.

This also dominates the bound in the first case. The Rhin estimate in
the cycle-height packet gives m<=L^14.3/3. For L>=2 this yields
Z<=16 log_2 L, and s<=2 log_2 L. Hence L<=3410 log_2 L, impossible
for L>=65536 as L/log_2 L is increasing there and already equals 4096
at the endpoint.

Eliahou's theorem on the same shortcut map gives at least 17,087,915
elements in a nontrivial positive ordinary cycle. This contradicts the
upper bound. It uses a historical verified initial range; the external
lower bound concerns the full shortcut period. Neither the proof nor
this citation settles a cycle whose word requires a different
factorization. [S. Eliahou, *The 3x+1 problem: new lower bounds on
nontrivial cycle lengths*, Discrete Mathematics 118 (1993),
45–56](https://doi.org/10.1016/0012-365X(93)90052-U)

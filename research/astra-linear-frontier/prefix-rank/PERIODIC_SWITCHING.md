# APR-006--008: automatic rank selection through arbitrary expanding periods

**Status: PROPOSED pending independent mathematical review.** The theorem
covers every specified primitive expanding binary period, with finite ordinary
sources at every requested horizon. It does not extract one positive integer
with an infinite expanding periodic itinerary and does not cover all aperiodic
switching. Gamma is the SAME computable integer rank throughout, from PROOF.md.

## 1. APR-006: the all-period statement, with computable constants

Let w be any primitive binary word of length m>=1 and odd count q, with
Q=3^q>P=2^m. Primitive means w is not a proper power. Let

    T_w(x)=(Qx+A)/P,       D=Q-P>0.

For each cyclic rotation v of w let A_v be its affine constant, and let
alpha_v=-A_v/D. For each 1<=r<m, let q_(v,r), A_(v,r) be the prefix data and

    C_(v,r)=D A_(v,r)-(3^q_(v,r)-2^r)A_v.                    (1)

These integers are nonzero. Put b=0 when m=1 and otherwise

    b=max(0, v3(|C_(v,r)|): all rotations v and 1<=r<m).

The following deliberately conservative constants are computable from w:

    j0 = least j>=1 with Q^j >= 2^(m+1) P^j,
    K0 = (j0+1)m,
    M  = 2*3^K0 + max_v A_v + 1,
    H0 = least H>b with 3^H > 4(D+1)^2 3^b,
    U  = 6PD.                                                (2)

For ANY integers H>=H0 and L>=1, put

    c = least c>=0 with 4^c >= 3^(H+q(L+1)) U^2.

Choose any N0>=1 satisfying

    P^N0 > 2DU+2DM+2 max_v A_v,
    Q^N0 >= 2^(c+1) P^N0,                                  (3)

and set N=N0+L+1. These searches terminate because Q>P>1.
Choose any odd positive 3-unit u<=6D for which

    P^N 3^H u = A mod D,       n=(P^N 3^H u-A)/D.            (4)

At least one such u exists; in fact a residue modulo D has positive
representatives in (0,6D] of both admissible classes modulo 6, since gcd(D,6)=1.
For D=1 use the ordinary modulus-one convention.

Then n is a positive integer, its first mN parity bits are w^N, and at EVERY
physical position 0<=r<=mL the unique minimizing prefix in Gamma(T^r(n)) has
length m. In particular, if q_r counts the first r odd steps, then

    Gamma(T^r(n)) = (3^q_r/4^r) Gamma(n),
    Gamma(n)=P^(2N) 3^H u^2.                                (5)

Thus every step through this whole horizon is strictly rank-decreasing:

    Gamma(T^(r+1)(n)) / Gamma(T^r(n)) is 1/4 or 3/4.

At period boundaries the ordinary values INCREASE, whereas

    Gamma(T^(mL)(n)) = (Q/P^2)^L Gamma(n) < Gamma(n).          (6)

For fixed w,H,L, arbitrarily large N0 satisfy (3), giving infinitely many
ordinary sources in (4). The selector computing Gamma is independent of w,
H,L or their certificate: it just evaluates actual prefixes as in APR-001.
These parameters prove that its successful domain is nonvacuous and contains
arbitrarily long mixed patterns; they are not supplied by an orbit oracle.

## 2. Why a primitive period has the stated comparison phases

Every length-k binary word has exactly one source residue modulo 2^k. The
usual induction compares its two next lifts: their k-step affine images
differ by the odd integer 3^q, so their next parities differ. Final affine
integrality selects that same class. This is a finite arithmetic statement.

The unique 2-adic realizer of w repeated forever is -A/D. Equivalently one
can work only with the compatible finite residues of this rational: D is odd,
and its affine fixed-point equation puts it in the class for every w^j.
Applying a phase prefix sends it to alpha_v for the rotated word v. If (1)
were zero, this rational would return at a proper phase r<m. Its parity
sequence would have a smaller period, contradicting primitivity. No positive
ordinary realization is inferred from this rational calculation.

Each A_v is a 3-unit: the final odd contribution in its sum is a power of
two, and every earlier odd contribution is divisible by 3. Hence alpha_v
is a 3-adic unit. At a prefix k=lm+r of v repeated, with 1<=r<m, its raw
return numerator at the rational center is P^l C_(v,r)/D. Its valuation is
therefore at most b, independently of the number of complete periods l.

## 3. A selection lemma which also excludes unprescribed later prefixes

Fix a phase v and an ordinary source x with

    D x + A_v = P^a 3^h t,
    a>=1, h>b, 1<=t<=U, 3 not dividing t.                    (7)

No dyadic restriction on t is required. Suppose x>=M,

    3^h >4(D+1)^2 3^b,
    x >3^h t^2,
    4^c >=3^h t^2,
    (Q/P)^a >=2^(c+1).                                     (8)

Then the unique global minimizer in Gamma(x) is the length m prefix v.
Its rank is P^(2a)3^h t^2.

### Physical prefix

Since P^a divides D x+A_v, the word v^a is physical. To check this directly,
its affine fixed-point numerator is

    (Q^a-P^a)x+A_v (Q^a-P^a)/D
       = ((Q^a-P^a)/D)(D x+A_v).

The geometric quotient is odd, so the divisibility is exactly that required
by the length-ma source cylinder. All actual states remain positive.

### Baseline and all candidates inside the prescribed prefix

The baseline is x^2, because h>b>=0 and alpha_v is a 3-unit. For a nonmultiple
k of m inside v^a, the prefix numerator differs from its rational-center
value by (3^q_k-2^k)(x-alpha_v), whose valuation is at least h. Thus its exact
valuation is the corresponding value at most b; no generic valuation is used.

For k<=K0 the affine remainder is at most 3^K0, so

    |(3^q_k-2^k)x+A_k| >= x-A_k >= x/2.

For k>K0, the coefficient is at least two: k=lm+r has l>=j0 and every
phase-prefix coefficient is at least 2^(-m), while (Q/P)^j0>=2^(m+1).
Its numerator is then at least 2^k x. In either case, every nonmultiple
candidate is at least x^2/(4*3^b).

The length-m candidate is at most (D+1)^2 x^2/3^h, strictly below that
quantity by (8), since x>=M>A_v. Every multiple lm, l>=2, has numerator
S_l(Dx+A_v), where S_l=(Q^l-P^l)/D>1 is a 3-unit. Its rank is S_l^2 times
the length-m rank. It cannot minimize. This exhausts the prescribed prefix.

### The unprescribed tail is not assumed periodic

Every candidate past ma+c has the lower bound 4^k, which already exceeds
P^(2a)3^h t^2. For ma<k<=ma+c, physical positivity gives

    T^k(x) >= 2^(-(k-ma)) T^(ma)(x)
             >= 2^(-c)(Q/P)^a x >=2x.

The second inequality uses A_v>0. Hence its displacement is at least x,
and its rank is at least 4^k x>P^(2a)3^h t^2 by (8). This is a bound on
EVERY actual unprescribed candidate, irrespective of its parity or valuation.
It is precisely what permits a global minimum without presuming an infinite
periodic future. The selection lemma follows.

## 4. Application at every phase of the constructed ordinary source

For r=lm+s, 0<=s<m and r<=mL, let q_s count the s-prefix odd bits. The
cyclic affine identity gives

    D T^r(n)+A_v = (3^q_r/2^r)(Dn+A)
       = P^(N-l-1) 3^(H+lq+q_s) (2^(m-s)u).                 (9)

Thus in the selection lemma a>=N0, h<=H+q(L+1), and t<=U. Also h>=H0.
The first inequality in (3) ensures x>=M and x>3^h t^2: indeed
P^a>2Dt and P^a3^h t>2A_v imply
x=(P^a3^h t-A_v)/D>P^a3^h t/(2D)>3^h t^2.
The other conditions in (8) follow from (2)--(3) and the chosen c.
The selection lemma applies at every phase, including r=mL.
Taking the valuation and square in (9) proves (5).
Since Q<=3^m<4^m=P^2, the rank multiplier in (6) is below one.
Meanwhile T^(ml)(n)=alpha_w+(Q/P)^l(n-alpha_w) strictly increases for l>=1.
This proves the all-parameter theorem, with one common rank and ordinary
finite paths. QED.

## 5. APR-007: it resolves arbitrarily many of the old unsafe 3/1 switches

Take w=111010=1110|10, with m=6,q=4,P=64,Q=81,D=17,A=73.
Its center is -73/17. The constants (2) give H0=9; on the above sources H>=9, hence
n=10 mod243. There is no terminal even-run repayment hypothesis.

The old moving rank R_* from PR92 is different from Gamma. Recalling its
credited formulas z_a(x)=3^a(x+1)-2^a(2x+1), R_a=z_a^2/3^v3(z_a), its minimum
has candidates 0,1,2 and a=h(x)=v3(2x+1) when h>=3. The elementary reason
is z_(a+1)>3z_a for a>=2, and v3(z_a)=min(a+v3(x+1),h) except at equality;
only that single exceptional index can improve the a=2 entry.

At boundaries s_i and intermediates t_i=T^4(s_i), exact ternary agreement
with the two rational phases gives

    R_*(s_i)=(s_i-1)^2/9,
    R_*(t_i)=(t_i+5)^2/9.                                  (10)

For t_i>13 the ratios are

    R_*(t_i)/R_*(s_i)>1,
    1/4 < R_*(s_(i+1))/R_*(t_i) <9/16,
    R_*(s_L) >(81/64)^(2L) R_*(s_0).                        (11)

These are the earlier PR92 formulas, not a novelty claim. Here all sources
are much larger than the small threshold. The alternating active modes 3,1
make each corridor maximal after exactly one copy. Thus all 2L old A-sources
are quarter-unsafe, and their number and cycle-boundary rank increase are
unbounded in L.

In CONTRAST, (5) gives at every shortcut step of the same phase

    Gamma(T^(r+1)(n))/Gamma(T^r(n)) in {1/4,3/4},
    Gamma(T^(6L)(n))=(81/4096)^L Gamma(n).                    (12)

The same common rank is computed afresh from the actual input, with the
proved unique minimizer m=6. This replaces the old guarded terminal repayment
on this family by contraction during the unsafe phase itself. It does NOT
claim that all old unsafe inputs belong to this family or become safe.

This does not obtain progress by merely inflating the starting rank. Since
n>91 and H>=9 on this family,

    Gamma(n)/R_*(n) = 9(17n+73)^2/[3^H(n-1)^2]
                     < 2916/3^H <= 4/27.                    (14)

So the new rank starts strictly BELOW the old rank, decreases during the
old unsafe growth, and has the same properness role. The comparison tends
to zero as H increases. It still does not authorize arbitrary switches
between the two ranks on other sources.

## 6. APR-008: no fixed prefix dictionary computes this rank everywhere

The primitive words (1110)^j 110, j>=1, have lengths 4j+3 and are expanding.
Their cyclic run-length list has exactly one odd run of length two and j
runs of length three, so no nontrivial cyclic repetition is possible.
APR-006 supplies ordinary inputs on which the UNIQUE minimizing length is
4j+3. Thus truncating the rank dictionary at any fixed word length changes
Gamma on some inputs. This is a true unbounded-index result, not a larger
finite dictionary or an assumed unbounded successful search.

## 7. The boundary cannot be silently renewed

A smaller exact example shows the hazard. At n=1932103 the unique minimizing
length is six and Gamma(n)=1479901446144. The next six steps follow 111010,
and Gamma(T^6(n))=29265629184. But

    T^6(n)=2445319,
    T^7(n)=3667979,
    Gamma(T^7(n))=4484692426800 > Gamma(T^6(n)).               (13)

The next minimizing length is one. This source satisfies a SHORT finite
period guard, not the all-phase hypotheses (2)--(4) for extending the horizon.
The increase is a failure of global rank monotonicity, not a
counterexample to Collatz or to APR-006. No convergence assertion about
this particular input is needed for the countertest.

For each requested horizon, the theorem deliberately supplies enough finite
ordinary precision and a bound on all later competing candidates. The
sources vary with the horizon. Claiming that every fixed source continues
to satisfy this guard would be the first unproved step in the proposed
universal rank-switching completion.

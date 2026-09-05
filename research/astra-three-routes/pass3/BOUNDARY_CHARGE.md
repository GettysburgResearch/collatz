# Route 1: survivor bias is a signed arithmetic-boundary charge

**Status:** T-A3-601--603 are **PROPOSED pending independent review**. The
all-time fixed-floor estimate is OPEN. Every infinite sum below is over actual
positive integers, not random parity sequences. This pass does not use an
external predecessor theorem.

Use T(n)=n/2 for even n and (3n+1)/2 for odd n. Let H>=1 be an integer and
S_k(H)={n:T^i(n)>H for 0<=i<=k}. For s>1 define

    M_k = sum_(n in S_k(H)) n^(-s),
    Q_k = sum_(n in S_k(H), n=2 mod 3, (2n-1)/3>H) n^(-s).

For H=64, s=3/2 these are exactly the first-pass M_k,Q_k. All quantities are
finite without assuming that any unexamined integer converges.

## 1. T-A3-601: exact first surviving representative of every cylinder

Fix a parity word w of length k, and write its prefix maps as

    T_(w|i)(n)=(Q_i n+A_i)/2^i, Q_i=3^(number of odd bits),
    Q_0=1, A_0=0.

There is one residue r_w in [0,2^k) realizing w. Put

    L_w=max_(0<=i<=k) (2^i H-A_i)/Q_i,
    m=2^k,
    a_w=r_w+m*(floor((L_w-r_w)/m)+1).                    (1)

Then a_w>H and, exactly,

    S_k(H) = disjoint union_w {a_w+m*l:l>=0}.             (2)

Proof: prefix survival is precisely n>L_w; the strict inequality explains the
floor-plus-one, including equality at the boundary. Intersecting with the
parity residue gives (1). Conversely each retained lift has every prescribed
parity and satisfies every survival inequality. All words have infinitely many
large ordinary lifts, but no infinite-time conclusion is drawn from this.

This gives a different all-source finite-time certificate from the inverse
cone in pass 1: enumerate 2^k first representatives and rigorously sum their
infinite arithmetic tails. There is no finite source cutoff.

## 2. T-A3-602: the sign is decided at that first representative

For a fixed a=a_w, put f_l=(a+m*l)^(-s) and d_l=f_l-f_(l+1).
Both f_l and d_l are positive and decreasing to zero. Let j in {0,1,2} be the
unique index with a+m*j=2 mod 3. Define the unrestricted residue defect

    D_j(a,m)=sum_(l>=0) f_(3l+j) - (1/3)sum_(l>=0) f_l.

The exact identities are

    3D_0 = f_0 + sum_(l>=0)(d_(3l)-d_(3l+2)),
    3D_1 =      - sum_(l>=0)(d_(3l)-d_(3l+1)),
    3D_2 =-f_0 - sum_(l>=0)(d_(3l+1)-d_(3l+2)).          (3)

They follow by grouping successive triples and using sum_l d_l=f_0.
All regroupings are justified by absolute convergence. In particular,

    f_0/3 <= D_0 <= (f_0+d_0)/3 <= 2f_0/3,
              D_1 <= 0,
              D_2 <= -f_0/3.                            (4)

For example sum_l(d_(3l)-d_(3l+2))<=sum_l(d_(3l)-d_(3l+3))=d_0.
This proves the upper bound. The other signs follow from convexity of x^(-s).

**Only cylinders whose first survivor is 2 modulo 3 can contribute positive
residue bias.** No endpoint equidistribution, phase independence, or orbit
mixing is used. The positivity cannot be assigned from the parity word alone;
the ordinary lower boundary a_w is essential.

After the first J terms of any series in (3), the remaining series has absolute
value at most d_(3J). This follows by enlarging its nonnegative differences
to all consecutive differences from index 3J onward. Thus (3) gives a signed
certificate with error at most d_(3J)/3 per cylinder, not an unspecified tail.

### Exact eligible-endpoint identity and inexpensive majorants

Let G_k be the finite mass of surviving n=2 mod 3 for which (2n-1)/3<=H.
Set B_i=sum_(w:j_w=i) a_w^(-s) and

    V_0=sum_(w:j_w=0) [a_w^(-s)-(a_w+m)^(-s)].

Then, exactly and as upper bounds,

    Q_k-M_k/3 = sum_w D_(j_w)(a_w,m)-G_k,               (5)
    Q_k-M_k/3 <= (B_0-B_2+V_0)/3-G_k,
    Q_k-M_k/3 <= (2/3)B_0.                              (6)

These are physical survivor identities. G_k must not be omitted in an exact
identity; omitting it in the upper bound is safe because it is nonnegative.

Consequently, if Q_k>(1/3+delta)M_k, then

    B_0 > (3delta/2) M_k.                               (7)

This is a concrete inverse statement: failure of a bias ceiling forces a
specified amount of mass at the first ordinary representatives of a specified
color. It does not prove that this concentration cannot persist.

## 3. T-A3-603: uniform finite-horizon bulk control, with correct quantifiers

Monotonicity gives for every cylinder

    sum_(l>=0)(a+m*l)^(-s) >= integral_0^infinity(a+m*t)^(-s)dt
      = a^(1-s)/(m(s-1)).

As a>H, this and (6) yield the all-H, all-k bound

    Q_k/M_k <= 1/3 + (2/3)(s-1)2^k/H.                  (8)

For s=3/2, H>=32*2^k implies Q_k/M_k<11/32<69/200.
The comparison is exact: 200*11=2200<2208=69*32.

This is uniform at every k with a correspondingly large floor. It is NOT a
fixed-H all-time theorem. Even verifying every integer in one large floor
would supply only its finite logarithmic time range through (8). Exchanging
these quantifiers would be the old ordinary/infinite-time error in a new form.

## 4. A fixed-floor target and the attempted cancellation proof

Specialize to H=64, s=3/2. A sufficient condition at an unbounded sequence of
k's is

    sum_w D_(j_w)(a_w,2^k)-G_k <= (7/600) M_k.           (9)

This is the explicit arithmetic form of the earlier cofinal-time 69/200
ceiling. The exact killed inverse identity is

    M_(k+1)=2^(-3/2) M_k
      +sum_(y in S_k, eligible) ((2y-1)/3)^(-3/2).

For every eligible y>=98, the second weight is at most (98/65)^(3/2)
times y^(-3/2). The rational bounds 2^(-3/2)<177/500 and
(98/65)^(3/2)<463/250 give

    177/500+(69/200)(463/250)=49647/50000<993/1000.

Thus (9) forces M_(k+1)<(993/1000)M_k at those times. Since the nonnegative
M_k decrease to a limit, a cofinal sequence of such inequalities forces the
limit to be zero. Any exceptional ordinary source contributes a fixed
positive mass to that limit. The finite core 1..64 reaches 1, as directly
rechecked here. This proves the conditional implication. Equation (9)
itself is OPEN.

A stronger, cheaper sufficient certificate is

    B_0-B_2+V_0-3G_k <= (7/200) M_k.                   (10)

We tested the simpler versions with G_k discarded to see which terms cannot
be ignored. At H=64 the positive-only bound (2/3)B_0 already fails to certify
the proposed ceiling at k=3, although the actual signed bound certifies it.
The first-representative curvature majorant also eventually loses the finite
pilot while (3), with its controlled remainder, still passes. These are
failures of proposed majorants, not counterexamples to the actual bias target.

The resulting next target is an all-depth bound on the signed curvature charge
in (3), allowing cancellation between colors. A uniform bound on each positive
term separately is not assumed. No finite list of successful k's is presented
as (9). Larger all-source experiments already exist in pass 1; the new pilot
is for the new boundary decomposition, not an attempt to set a depth record.

## 5. Exact rational enclosure used by the checker

Take S=2^80. The integer isqrt(floor(S^2/n^3)) encloses n^(-3/2) between v/S
and (v+1)/S. For an AP tail starting at z=a+Nm,

    2/(m sqrt(z)) <= sum_(l>=N)(a+ml)^(-3/2)
                  <= 2/(m sqrt(z))+z^(-3/2).

The integral is enclosed by isqrt(floor(4S^2/(m^2 z))). Signed interval
arithmetic in (3), with the explicit d_(3J) remainder, gives complete-source
bounds for every reported finite horizon. The independent verifier generates
cylinders from ordinary residues instead of the prefix-lifting generator.

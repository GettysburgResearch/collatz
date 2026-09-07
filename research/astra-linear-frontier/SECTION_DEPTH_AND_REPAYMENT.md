# ALF-004–007: logarithmic P-merging depth, immediate alternate-rank descent, and repayment

**Status: PROPOSED; independent mathematical review pending.** No universal
Collatz proof is claimed. This file gives an all-parameter family, not a cover
of all positive sources. Use T, H, R and P from [LINEAR_PRECISION.md](LINEAR_PRECISION.md).
The two clocks below count **completed section returns**, not shortcut steps.
Witnesses belong to H; arbitrary nonsection shortcut witnesses are not silently
included in that statement.

## 1. Main family and the precise theorem

For D>=1 choose an integer h>=256(D+1), and put

    h0=4D+1,   K=36D+20,   t0=5*2^h0.

Let u be a positive odd 3-unit satisfying

    2^h u = t0 mod3^(K+1),                                    (1)

and let n=(3^h u-1)/2 physically realize the first 3D bits (110)^D.
Then h(n)=h. These simultaneous conditions have infinitely many ordinary
solutions; an explicit construction is given in Section5.

**ALF-004 (complete bounded-section obstruction).** Every positive section
witness in the entire two-sided box satisfies

    R^r(n)=R^s(x),  0<=r,s<=D  ==>  P(x)>=P(n).                 (2)

The minimum is attained at x=n. Both clocks may contain arbitrarily long odd
runs. Thus (2) is not a reformulation of the earlier bounded-shortcut-clock
obstruction in PR90/CLOCK_DEFECT.md.

**ALF-005 (a compatible positive repayment).** Impose additionally

    L=2(h+D+2),     v2(R^D(n))=L.

There are still infinitely many sources satisfying all the conditions. With
m=R^D(n)/2^L, one has

    m in H, m odd,
    R^(h+2D+2)(n)=m,    T^(2h+5D+4)(n)=m,
    P(m)<P(n)/4.                                               (3)

If C_R(n) is the minimum max(r,s) over all lower-P section merging diagrams,
then these sources satisfy

    D<C_R(n)<=h+2D+2.                                          (4)

For the least CRT lift in Section5 and h=256(D+1), moreover,

    (log_2 n)/1024 < C_R(n) < 2 log_2 n.                        (5)

Thus there is an explicit unbounded sequence with C_R(n)=Theta(log n).
This is a cost for **this rank and this certificate interface**, not a lower
bound for every possible proof method. Equation(3) is rank repayment, not a
claimed complete path from m to1. Section7 gives a separate, fully convergent
family with a compressed path all the way to1.

## 2. Why a linear h is enough: dyadic comparisons become ordinary integers

On the first D section returns the exact endpoint is

    y_r=R^r(n)=(9/8)^r(n+5)-5
       =a_r 3^h u+b_r,
    a_r=(9/8)^r/2,   b_r=(9/2)(9/8)^r-5.                      (6)

Before the first high-precision node in an inverse branch, write every
candidate in the form

    x=a3^h u+b,    a>0.                                       (7)

We call these A-comparisons. Their rational constant b is dyadic, with
denominator dividing 2^(3r+1). Define their formal inverse fan from the exact
ternary depth of 2b+1 and its unit, stopping when b=-1/2. On a low node the
inverse transformations are

    a'=(2^(j+2)/3^j)a,
    b'=(2^(j+2)/3^j)b+2^(j+1)/3^j-2,

and, for the permitted terminal odd exit of depth H,

    a'=(2^(H+1)/3^H)a,
    b'=(2^(H+1)/3^H)b+2^H/3^H-1.

The ternary divisions cancel in b because they are exactly the fan guards.
Every intermediate inverse constant remains dyadic. Each section edge gives
|b'|+2<=4(|b|+2). Consequently, through at most D inverse returns,

    |b|+2<=12*8^D,
    |2^(3r+1)(2b+1)|<48*64^D<3^(4D+4).                       (8)

For b!=-1/2 the fixed depth H=v3(2b+1) is therefore at most4D+3. A coarse
bound obtained by summing per-edge depths is q<=4D(D+1). The following
stronger bound is what permits h to be linear rather than quadratic in D:

    q<=21D+13 <=Q_A:=24D+16.                                  (9)

### Proof of(9), including the possible signs

Every inverse shortcut step is b->2b or b->(2b-1)/3. As long as b is not an
integer its dyadic denominator drops by at least a factor2 at each step.
It therefore becomes an integer after at most3r+1 shortcut steps. If the
whole path is shorter, (9) is immediate.

At that first integer position b0, the elementary estimate
|b'|+1<=2(|b|+1), with |b_r|+1<2^(r+3), gives

    |b0|<2^(4D+4).                                            (10)

The integer b0 cannot be0 on a selected path: an odd inverse reaching residue0
ends the residue2 chain and gives no section exit, while an even inverse can
reach0 only from0. It cannot be-1 before a high node either. An odd inverse
can reach-1 only from-1. An even inverse can reach-1 only from-1/2; that is a
stopped high section node, and cannot be a proper residue2-chain node since
-1/2=1 mod3. These arguments also rule out first appearances earlier in the
path. After b0, the comparison steps are ordinary legal integer inverse steps
and cannot change sign. A negative comparison stays at most-2.

Read the remaining comparison word forward. On a positive odd integer the
absolute multiplier is at least3/2. On a negative odd integer of absolute
value a>=3 it is (3a-1)/(2a)>=4/3. Even steps multiply magnitude by1/2.
If q' and e' count these remaining odd and even steps, then

    (4/3)^q' <=2^e' |b0| <2^(6D+4),

because e'<=2D and the final inverse source has magnitude at least1.
Since (4/3)^3>2, q'<18D+12. Adding at most3D+1 initial odd steps proves(9).
This needs neither distinct comparison states nor any theorem about negative
Collatz cycles.

### Low A-nodes are all more expensive

For an inverse word of length k and odd count q from y_r,

    a=(1/2)(9/8)^r 2^k/3^q,
    a>=(1/2)(2/3)^q,    v3(2a)=2r-q.

The inequalities h>=256(D+1), q<=Q_A, and H<=4D+4 imply h+v3(2a)>H+1.
Thus the actual x in(7) has exactly the depth and unit of its comparison b.
They justify the full formal fan retroactively by finite induction, not by a
hypothesis about a generic valuation. They also ensure

    2x+1 >=a3^h u,
    P(x)/P(n)>=(1/4)3^(h-H-2q)>1.                            (11)

For example h-q>3D+4 makes the shifted main term exceed twice the constant
in(8), and h-H-2q>=204D+220 gives strictness in(11). All these estimates are
uniform in the positive unit u. This argument first bounds the *formal*
comparison tree; it does not assume the high-precision matching in order to
prove the budget needed for that matching.

## 3. High A-nodes cannot strip ternary precision

A high A-node has b=-1/2. Let v=(110)^r, and let w be its inverse
source-to-endpoint word. In shifted coordinates, a word of length j, odd
count q and ordinary affine constant A has

    2^j(2T_w(x)+1)=3^q(2x+1)+B_w,
    B_w=2A+2^j-3^q.

Every nonempty B_w is positive and odd. For v,

    |v|=3r,   q_v=2r,   B_v=9(9^r-8^r).

The equality b=-1/2 forces zero shifted clock defect:
2^|w| B_v=2^(3r) B_w. For r>0, oddness forces |w|=3r and B_w=B_v.
For r=0 it forces both words empty. Write p=q_w-2r. The high node is then

    x=(3^(h-p)u-1)/2,      P(x)=3^(-p)P(n).                    (12)

In fact

    -2r<=p<=0.                                                (13)

Here is the combinatorial obstruction to p>0. Among words of length j with
q ones, the minimum shifted remainder is

    B_min(j,q)=3^q+2^j-2^(q+1).                               (14)

To prove this, swapping01 to10 at successive positions decreases B; the
smallest word is 1^q0^(j-q), whose B is the displayed expression. The expression
is increasing in q>=1.

Since n is odd, x in(12) is odd when p is even and even when p is odd. If
p>0 is even, w already has at least2r+2 ones. If p>0 is odd, its first bit is0.
Change that bit to1: the shifted remainder is unchanged (the first B is1 for
either bit), while the odd count becomes at least2r+2. In either case, unless
that count already exceeds the word length, (14) gives

    B_w-B_v >=10*8^r-8*4^r >0,

a contradiction. Thus(13) holds. This comparison uses actual parity to select
the case, not a quotient labelled a merger without a physical word.

At a high node with m<=D inverse returns remaining, the linear-frontier
lemma permits deleting every even gap d>=4m-2. Every retained even child has
form

    x=2^(1-p-d)3^d t-2,    t=2^h u,
    1<=d<=4m-3,   -2D<=p<=0.                                (15)

The terminal odd child, when present, is x=2^(-p)t-1. Condition(1) implies
t=1 mod3, so that child is present exactly when p is odd. Deleted subtrees
are more expensive than their high parent, which by(12) is already at least
as expensive as n. This deletion is therefore legitimate relative to n too.

## 4. Freeze the remaining B-comparisons at an actual positive integer

Evaluate every root in(15), and each permitted odd root, at t=t0=5*2^(4D+1).
Each is a positive ordinary section integer x0, with

    x0<2^(10D+5).

Every ordinary inverse section ancestor through another D returns has

    x0'<2^(12D+5),    H_B=v3(2x0'+1)<=12D+6.                  (16)

The positive inverse clock inequality in ALF-003 bounds its odd count by

    q_B<=Q_B:=24D+10.                                        (17)

Indeed (3/2)^q_B<=2^(2D)x0<2^(12D+5), and (3/2)^2>2.

Every corresponding B-node has an affine expression x=a t+b. Initially a>=1
and b is -1 or -2. After q_B odd inverse steps,

    a>=(2/3)^q_B,   v3(2a)>=-q_B,
    |b|+2<=4^(D+1).                                          (18)

Its dyadic denominator in a divides2^(4D); inverse operations can only
remove factors2 from that denominator. Ternary denominators are accounted
for by(17), not dropped. Both t and t0 are divisible by2^(4D+1), and(1) gives

    v3(2a(t-t0))>=K+1-q_B>H_B.                              (19)

It follows that x=x0'+a(t-t0) is an integer and has precisely the comparison
node's ternary depth and unit. Positivity is automatic from a>0, t>t0 and
x0'>1. Finite induction matches **every child in both directions**. Thus no
additional actual inverse branch is omitted by the positive comparison tree.
This is an ordinary finite congruence argument, not an ordinary realization
of a p-adic limit.

Finally h>=256(D+1) makes 2at dominate |2b+1|. By(18),

    P(x)/P(n)>a^2(4/3)^h /3^H_B
              >=(4/3)^h /3^(60D+26)>1.                      (20)

The last inequality follows from (4/3)^4>3 and h/4>=64(D+1)>60D+26.
For the preceding domination, h>2Q_B+2D+5 is already enough.

Every retained inverse path consists of low A-nodes, high A-nodes, or a
B-comparison after its first high node. Equations(11), (12)–(13), and(20),
together with the lossless shield for discarded branches, prove(2). Apply
this to each r=0,...,D. The inverse copy x=n at depth r is in the complete
box, so the minimum is exactly P(n).

## 5. Positive CRT construction and the logarithmic cost bracket

For the additional repayment in ALF-005, fix L=2(h+D+2), and N=3D+L+1. Set

    r = [8^D(5+2^L)9^(-D)-5] mod2^N.

This is exactly the source class that realizes (110)^D followed by L even
steps and an odd endpoint. Equivalently, n+5 has dyadic valuation3D and
(9/8)^D(n+5)-5=2^L mod2^(L+1). Impose the two congruences on u:

    u=(2r+1)3^(-h) mod2^(N+1),
    u=t0 2^(-h) mod3^(K+1).                                  (21)

Their moduli are coprime. CRT supplies one residue and all its positive
lifts, each an odd 3-unit. Then n=(3^h u-1)/2 is an ordinary source meeting
all the preceding guards. No search for a stopping time enters its definition.

Write s=R^D(n) and m=s/2^L. The stipulated L is even, so m is odd and lies
in H. The remaining L halving steps are L/2 complete section returns. For
n>=5, s<2(9/8)^D n and 2m+1<=3m, whence

    P(m)/P(n) <=3^(h+1)(81/64)^D /4^L <1/4.                  (22)

The final bound follows, for instance, from 3<4 and 81/64<4, with
L=2(h+D+2). This proves(3) and(4).

For a least CRT lift u0, 0<u0<2^(N+1)3^(K+1). Taking h=256(D+1), and using
log_2 3<8/5, gives

    log_2 n <(18/5)h+(313/5)D+193/5
            <1024(D+1).

Also n>2^h for h>=3. Consequently C_R(n)>=D+1>(log_2 n)/1024, while
C_R(n)<=258(D+1)<2log_2 n. This proves(5). The logarithmic comparison is for
this bounded-lift sequence; arbitrary large lifts at a *fixed* D are not
claimed to have the same lower bound in their own logarithmic height.

## 6. ALF-006 — these P-hard sources are immediately easy for another proper rank

The existing corridor component from PR92 is

    C(n)=(n+5)^2/3^v3(n+5).

It is a positive integer with C(n)>=n+5. On a legal110 block,

    y=(9n+5)/8,   y+5=9(n+5)/8,
    C(y)=(9/64)C(n).                                         (23)

This identity was already part of `pass4/MOVING_GHOST_RANK.md`, R_2 in the
family R_a. It is credited, not presented as a new rank or a newly discovered
block identity. It is rederived here by taking the exact valuation of y+5.

The **new comparison** is simultaneous: for every D, the family in(2) admits
an immediate C-drop, but no lower-P section merger anywhere in its entire
D-by-D box. Meanwhile the ordinary values grow along all D corridor returns.
The obstruction concerns the selected P rank, not an unavoidable obstacle
for C or every possible scalar rank.

There is also an exact failure of the two most immediate scalar combinations.
At these sources, h>=6 and

    P(n)<C(n),   C(R(n))>P(n),   P(R(n))>C(n).

The middle inequality follows from C(R(n))/P(n)>3^h/256; the last follows
from P(R(n))/C(n)=[9(n+1)/(4(n+5))]^2>1. Thus BOTH min(P,C) and max(P,C)
increase on the first edge, even though C itself decreases. The two-rank
comparison is not being promoted into a monotone scalar by an unproved
choice of minimum or maximum.

This is a concrete reason to study rank switching rather than only deeper
P-search. It is not a well-founded switching theorem. A drop in C after a
rise in P cannot be charged as a drop in P; neither alternating between two
proper ranks nor taking their minimum automatically makes a descent proof.
The subsequent guarded halving word proves P repayment only where its exact
dyadic condition holds. It does not prove that every exit from a C-contracting
corridor has a favorable repayment word.

## 7. ALF-007 — fully convergent hard families, with compressed certificates

There is also an all-parameter way to make the source in ALF-004 reach1
explicitly. This is distinct from claiming convergence of every CRT source
in Section5.

Fix D,h,K,t0 as above and set M=h+2D+K+1. Choose an even integer L, as large
as necessary, such that

    2^(3D+L+1)
      =9^(D+1)-10*8^D+3^(h+2D)t0 2^(-h) mod3^M.               (24)

The right side is a 3-unit. After multiplication by2^(-3D-1) it is1 mod3.
The powers of4 exhaust the units1 mod3 modulo3^M, with period3^(M-1).
For completeness, v3(4^(3^j)-1)=j+1 follows by induction using A^3-1 and
4-1=3. It implies that each successive ternary digit of the exponent has
one of three unique lifts. Thus(24) has an effective even solution, and all
solutions obtained by adding2*3^(M-1) to L. Take L>=2(h+D+2).

Define the actual positive integer by the compressed expression

    n_L=[2^(3D+L)+5(8^D-9^D)]/9^D.                            (25)

Equation(24) proves its integrality, exact h(n_L)=h, and the cofactor pin(1).
The exact affine identity for (110)^D gives T^(3D)(n_L)=2^L. Final affine
integrality identifies the unique physical parity cylinder. Indeed the two
lifts of a length-j parity class have opposite next parities; induction gives
one physical class per word. Its affine integrality condition also has one
class, since its odd coefficient is invertible modulo2^j. The classes coincide.
Equivalently one can use n_L+5=8^D(2^L+5)/9^D here. Every state is positive. Hence

    n_L --(110)^D 0^L--> 1.                                  (26)

All sufficiently large exponent lifts give distinct sources, so this is an
infinite family for every D,h. It simultaneously satisfies the no-lower-P
box theorem(2). Known convergence therefore does not rescue a fixed-radius
P-merging rule.

The experiment verifies the modular exponent-lifting certificates. These
n_L are not materialized, and their enormous shortcut paths are not literally
replayed. Their complete path to1 follows from(25)–(26); the modular checks
verify the chosen finite parameters, not an exhaustive simulation of L steps.
The Theta(log n) assertion(5) concerns the different bounded-lift repayment
sequence and is NOT transferred to this compressed full-convergence family.

## 8. The attempted end-to-end conclusion and its remaining gap

The proposed completion was: make inverse precision cheap enough that a
bounded number of whole section returns always finds a lower-P merger.
ALF-004 disproves that completion at every fixed radius. ALF-005 shows the
obstruction is repayable on a controlled ordinary family. ALF-006 identifies
an existing rank that makes progress immediately on precisely this family.
ALF-007 demonstrates full convergence on a separate, explicitly constructed
family satisfying the same obstruction.

None supplies a selector for an arbitrary fixed source. The remaining
constructive target is a switching or merging rule with one globally
well-founded measure, proving its own coverage and termination. In particular,
finite congruence freedom in(21) or(24) chooses new sources; it does not impose
the desired next word on an already given source. This is the first unsupported
inference in turning the family construction into a universal proof.

No external density theorem is needed here. No full Collatz proof, nontrivial
positive-cycle exclusion, or unbounded successful selector is claimed.

# An expanding-word rank: construction, contraction, and the failed closing step

**All ATT-201--206 claims are PROPOSED pending independent mathematical review.**
Author: `astra-tail-transport-03`. Date: 2026-09-07.
Frozen parent: `73572fddd9b8b3cbd8fc03c3a992eb0735d0f62c` (PR105).

**This is an attempted end-to-end proof, not a complete proof of Collatz.**
The construction below absorbs every sufficiently expanding periodic parity
pattern into one computable proper integer rank. It supplies strict common-rank
contraction through arbitrarily long phases that were unsafe for the earlier
rank. The attempted closing assertion that a minimizing pattern must be
physically usable is false, including on an explicit unbounded exit family.
The all-source certificate/activation theorem remains OPEN.

## 0. Physical map and distinction from previous ranks

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n, absorbed at 1
when considering convergence. All source/certificate states are ordinary
positive integers. Negative rationals below only identify finite parity
cylinders and supply exact algebraic comparison points.

For an integer z define

    g(0)=0,  g(z)=z^2/3^v3(z)  (z != 0).

Thus g(z) is an integer and g(z)>=|z|. The old rank is

    R_*(n)=min_(a>=0) g((3^a-2^(a+1))n+3^a-2^a).

That definition, its properness, and its exact four-entry evaluation are
credited to the pinned moving-rank packet. Our new rank rho is different.
The old quarter-unsafe set, its return operator H, and its input 1_U/R_*^2 are
NOT silently changed. In particular the old numerical mass bound for that
input is not a bound for the larger weight 1/rho^2 or a new return operator.

For a nonempty word w of length L, with q ones, put

    P_w=3^q, D_w=2^L,
    A_w=sum_(j=0)^(L-1) w_j 2^j 3^(q-s_(j+1)),
    s_j=sum_(i<j) w_i.

Its affine branch map is T_w(n)=(P_w n+A_w)/D_w. A word is physically realized
exactly when D_w divides P_w n+A_w. To see sufficiency, two lifts of a length-j
source class differ after j steps by an odd multiple of 1; exactly one realizes
each next bit. Induction gives one class modulo 2^L, and the displayed
congruence gives that same unique class since P_w is odd. This is a physical
word test, not permission to use arbitrary rational iterates as ordinary paths.

## 1. ATT-201: all-word minimization is computable and proper

Let W consist of ALL nonempty binary words satisfying

    4 P_w >= 5 D_w.                                      (1)

Put d_w=P_w-D_w>0 and Z_w(n)=d_w n+A_w. Define

    rho(1)=0,
    rho(n)=min {g(n), g(n-1), g(n+5), g(Z_w(n)): w in W}, n>=2.   (2)

No fixed word-length cutoff is part of this definition. The uniform expansion
gap 5/4 IS part of it. A word with 1<P_w/D_w<5/4 enters via a sufficiently
large repetition, not necessarily at its primitive length; its unreduced
component and its rank scale must be retained.

### Statement

For every n>=2,

    n-1 <= rho(n) <= R_*(n) <= n^2.                       (3)

If M is ANY verified candidate upper bound for rho(n), then every word
component attaining a value <=M has

    n 2^L < 4M.                                         (4)

Consequently an exact evaluation needs only finitely many words of length
L<log_2(4M/n). The three base components give M<=n^2, so the brute-force
search examines fewer than 8n binary words. This is a computability statement,
not a polynomial-in-bit-length complexity claim.

### Proof

Condition (1) gives d_w>=2^(L-2); moreover A_w>=1. Hence

    g(Z_w(n))>=Z_w(n)>2^(L-2)n,

which proves (4). The three base values are fixed positive integers, so this
finite search actually attains the infinite minimum. They also give the upper
bound n^2. Every word component is >=n+1 and each base component is >=n-1,
proving properness and integer positivity.

For a=0,1,2 the old component forms are -n,1-n,n+5, giving exactly the three
base values. For every a>=3, the word 1^a0 satisfies (1), and its Z_w is the
old component. Therefore (2) includes every component of R_* and rho<=R_*.
This does not make the ranks interchangeable in previous theorems. QED.

### Which periodic patterns are present?

Every word with P_w>D_w has a negative rational periodic realizer
-A_w/(P_w-D_w). A sufficiently large power of that word satisfies (1).
Thus every strictly expanding periodic parity pattern is represented somewhere
in W. This says nothing about how an actual aperiodic source chooses among
those patterns. Fixed points are only algebraic centers, not positive orbits.

## 2. ATT-202: a uniform sublinear rank spectrum

For X>=1 let N_rho(X)=#{n>=2:rho(n)<=X}. Then

    floor(sqrt(X))-1 <= N_rho(X) < 250 X^(39/40).          (5)

In particular

    sum_(n>=2) 1/rho(n) <= 10000,
    sum_(n>=2) 1/rho(n)^2 < 2,                           (6)

and, for s>39/40 and Y>=1,

    sum_(rho(n)>Y) rho(n)^(-s)
       <= [250s/(s-39/40)] Y^(39/40-s).                 (7)

The exponent in (5) is an upper bound, NOT an asserted sharp dimension.
It is weaker than the old R_* square-root count; the gain is the much larger
arithmetic dictionary. Equation (7) is an INITIAL tail bound only.

### 2.1 Count word patterns without any independence hypothesis

Let a_L be the number of words in W of length L. Since the indicator of
P_w>D_w is at most sqrt(P_w/D_w), summing over all binary words gives

    a_L <= ((1+sqrt(3))/sqrt(2))^L < 2^(19L/20).         (8)

For an exact certificate of the strict inequality, let
r=(1+sqrt(3))/(2sqrt(2)). Then r^20=(2+sqrt(3))^10/4^10.
The binomial expansion gives

    (2+sqrt(3))^10 = 262087 + 151316 sqrt(3).

Now

    (2^19-262087)^2 - 3*151316^2 = 59768833 > 0,

and 2^19-262087>0. Thus r^20<1/2, proving (8) at all L.

### 2.2 Bound one component with a large positive offset

For q>=1, the odd positions j_i satisfy j_i>=i; hence

    A_w >= 3^q-2^q >= 3^(q-1) > 2^L/3.                 (9)

A component rank at most X has Z_w(n)=3^e u, 3 not dividing u, and
3^e u^2<=X. Write a=2^L/3. Condition Z_w(n)>a forces
3^e>a^2/X. Summing the upper counts sqrt(X)3^(-e/2) over the possible e,
and dropping all progression restrictions, gives

    #{n>=2:g(Z_w(n))<=X}
      <= (12/5) min(sqrt(X),3X 2^(-L)).                 (10)

Here 1/(1-1/sqrt(3))<12/5 follows from 1/sqrt(3)<7/12.
The strict positivity of d_w makes n -> Z_w(n) injective. No endpoint
multiplicity of physical Collatz trajectories is being ignored.

Each base component contributes at most (12/5)sqrt(X), so all three give
(36/5)sqrt(X). Split the word sum at L0=floor(log_2(3sqrt(X))). Equations
(8)--(10) give, respectively,

    sum_(1<=L<=L0) a_L (12/5)sqrt(X) < 18 X^(39/40),
    sum_(L>L0) a_L (36/5)X 2^(-L) < 216 X^(39/40).

The elementary margins used are

    2^(-19/20)<3/5,   1-2^(-1/20)>1/30,

certified by 2^19*3^20>5^20 and 30^20<2*29^20.
Adding the base contribution yields a constant below 242, and hence (5).
The lower bound follows from rho(n)<=n^2.

Positive integration of t^(-s) proves (7), with the negative lower-endpoint
term safely discarded. Integration from 1 proves the first part of (6);
rho(n)>=n-1 and sum_(j>=1)j^(-2)<2 prove its second part. QED.

## 3. ATT-203: a finite physical certificate using the SAME rank

Suppose a minimizing word component Z_w attains rho(n), and w is physically
realizable from n. Then y=T_w(n) satisfies

    rho(y) <= (3^q/4^L) rho(n) <= (3/4)^L rho(n) < rho(n).  (11)

The three base components have the same implication when their respective
words 0,10,110 are physically realizable. Their factors are 1/4,3/16,9/64.

### Proof

Direct composition gives

    Z_w(T_w(n))=(P_w/D_w) Z_w(n).

Physical legality supplies D_w | Z_w(n). The ternary valuation increases by q,
while division by 2^L changes no ternary valuation. Therefore the SAME component
rank at y is exactly (3^q/4^L)g(Z_w(n)). Taking the minimum at y proves (11).
If the path has already reached 1, convergence is certified directly. The base
components obey the identical calculation with their signed linear forms. QED.

This gives a total, computable PARTIAL certificate selector: evaluate (2),
retain every minimizing component, and test physical legality. On success,
return the finite path and the strict same-rank decrease. If no minimizer is
legal, return UNRESOLVED. No search for an unknown stopping time is concealed.
UNRESOLVED is not a statement that the integer does not converge.

## 4. ATT-204: exact minimizers through an unbounded formerly unsafe phase

Let v=111010. Its map is

    F(n)=(81n+73)/64,  Z(n)=17n+73,
    Z(F(n))=(81/64)Z(n).

The rational point -73/17 has primitive parity period v. Its six successive
phases are -a_i/17, with

    (a_0,...,a_5)=(73,101,143,206,103,146).               (12)

Let v_i be the cyclic rotation of v starting at phase i. Every v_i has
P=81,D=64 and Z_i(n)=17n+a_i, and satisfies (1).

### Uniform minimum lemma

For ANY phase i and positive integer n with

    17n+a_i=3^e u,  u>=1, 3 not dividing u,
    e>=13,  2^e>2176u,                                 (13)

the UNIQUE minimizing component in (2) is v_i, and

    rho(n)=3^e u^2.                                    (14)

This includes ALL admissible words, not only a fixed depth or the six rotations.

#### Proof

Put M=3^e u^2. Since 3^e u>2a_i, n>=3^e u/34. The three base forms at -a_i/17
have nonzero ternary numerators -a_i,-a_i-17,-a_i+85, all with valuation at
most 2. Under (13) their values at n have those same valuations. The base
ranks are at least (n-1)^2/9>=n^2/36.

For another word w of length L, put

    B_w=17 A_w-a_i d_w,
    17 Z_w(n)=d_w 3^e u+B_w.                           (15)

If B_w!=0, then |B_w|<223*3^L<3^(L+5), so v3(B_w)<=L+4.
For L<=e-5, the first term of (15) has valuation e, strictly larger. Thus

    g(Z_w(n)) >= d_w^2 n^2/3^(L+4)
               >= (4/3)^L n^2/1296 >= n^2/1296.

This is >M because

    3^13 > 34^2*1296 =1498176.

For L>=e-4, without using any valuation estimate,

    g(Z_w(n)) >= Z_w(n) > 2^(e-6)n >= M*2^e/(2176u)>M.

The base ranks are also >M. Finally B_w=0 means that w has the same rational
periodic realizer as v_i. Finite parity-cylinder bijectivity and infinite
2-adic injectivity imply that w is a power v_i^r: (12) has primitive period 6.
Then Z_w=S_r Z_i, where S_r=sum_(t=0)^(r-1)81^(r-1-t)64^t is a positive
3-adic unit. Its rank is S_r^2 M, equal to M only for r=1. This proves the
unique global minimum. Negative rationals are comparison points only. QED.

### An explicit all-parameter ordinary family

For every K>=1 choose ANY integer e satisfying

    e>=max(13,6K+12),  e+4K=5 mod16.                    (16)

There are infinitely many such e. Define

    n=(3^e 64^K-73)/17,   s=(3^(e+4K)-73)/17.           (17)

These are positive integers, since 64=3^4 mod17 and 3^16=1 mod17. The source
realizes exactly K repetitions of v before the next bit disagrees with v:
Z(n) has dyadic valuation 6K. The equivalence between this divisibility and
v^K follows either by the cylinder congruence or by its fixed point -73/17.
The endpoint s is even; v begins with an odd bit.

For 0<=j<=6K, let q_j count ones in the first j bits of v^K and n_j=T^j(n).
Then

    17n_j+a_(j mod6)=3^(e+q_j) 2^(6K-j).

The hypotheses (13) hold at EVERY one of these positions. Therefore

    rho(n_j)=3^(e+q_j) 4^(6K-j),
    rho(n_(j+1))/rho(n_j)=3^(v_j)/4,                    (18)
    rho(s)/rho(n)=(81/4096)^K.                          (19)

This is contraction at every actual shortcut step, using one common integer
rank and with no terminal-halving guard. It is NOT just a decrease of a local
component that might fail to minimize the global rank.

### Comparison with the OLD unsafe process

At the boundaries of the K cycles the old rank is (n_j-1)^2/9; after each
1110 block it is (n_j+5)^2/9. Old A-modes alternate 3 and 1, one copy each.
The two old rank ratios are

    [(27x+99)/(16(x-1))]^2 >1,
    9(t-1)^2/[16(t+5)^2] >1/4  (t>13).

Thus all 2K old A-source states are quarter-unsafe, while

    R_*(s) > (81/64)^(2K) R_*(n).

These are the previously studied physical phases, now with an additional
high-precision guard (16). Their existence was not discovered here; the new
conclusion is the exact GLOBAL rho-minimum and stepwise contraction (18).

The finite checker exhaustively recomputes the entire new dictionary at 60
selected positions (K=1,2). At the other large positions it checks the exact
premises of the written all-word comparison theorem and literal trajectories.
Those two evidence tiers are not conflated.

## 5. ATT-205: an unbounded exit jump survives the ENTIRE dictionary

For h=5 mod16, h>=21, put

    s_h=(3^h-73)/17,   y_h=s_h/2.

Then s_h=2 mod8, rho(s_h)=3^h, and its unique minimizing word is v=111010.
That word is physically ILLEGAL at the even source s_h. Moreover

    rho(y_h)/rho(s_h) >= 2^h/4352.                      (20)

Thus the exit from the contracting family (17)--(19) can increase the new
rank by an arbitrarily large factor in ONE actual shortcut step.

### Proof

The minimum at s_h follows from (13) with u=1. At its successor,

    34y_h+73=3^h.

For any w in W set C_w=34A_w-73d_w. Since d_w is odd, C_w is odd and cannot
vanish. Also |C_w|<107*3^L<3^(L+5), and

    34Z_w(y_h)=d_w3^h+C_w.

For L<=h-5, valuations stabilize and the same estimate as before gives
rank at least y_h^2/1296. For L>=h-4, the direct size bound gives at least
2^(h-6)y_h. The three base forms have valuation zero at the comparison
point -73/34 (their numerators are -73,-107,97), so they are also at least
y_h^2/1296. Consequently

    rho(y_h) >= min(y_h^2/1296, 2^(h-6)y_h).

Since y_h>=3^h/68,

    rho(y_h)/3^h >= min(3^h/5992704, 2^h/4352).

For h>=18 the first term is at least the second: the exact base inequality
4352*3^18>5992704*2^18 propagates by multiplication by 3/2. This proves (20).
The even-denominator rational -73/34 cannot be a periodic 2-adic realizer;
the parity argument C_w!=0 is the exact arithmetic distinction at this exit.
There is no assumption about eventual convergence of s_h or y_h. QED.

This REJECTS the attempted closing claim that representing all periodic
expansions forces physical activation of a minimizing word. It does not reject
rho's computability, summability, the valid local selector, or (18).

## 6. ATT-206: arbitrary finite forward rank delay remains possible

For every integer K>=1 and every e>=K+8, choose an odd integer u such that

    0<u<2^(K+2),  3 not dividing u,
    3^e u=-1 mod2^(K+1).                               (21)

Such a u exists: choose the unique odd residue modulo 2^(K+1), and add that
modulus once if the residue is divisible by 3. Put n=3^e u. Then

    rho(n)=n^2/3^e,
    rho(T^j(n)) >16 rho(n),  1<=j<=K.                   (22)

So no fixed forward lookahead is guaranteed to find a lower rho-rank.
Different K,e have different ordinary sources; this is not an infinite
positive all-odd orbit.

### Proof

For any positive multiple of three, all word Z_w values are ternary units:
A_w mod3 is the unit 2^(last odd position). The two other base values are
also units and exceed g(n). Therefore rho(n)=g(n).

The physical prefix in (21) is all odd, and

    n_j=T^j(n)=(3^j n+3^j-2^j)/2^j > n.

All three base forms n_j,n_j-1,n_j+5 are ternary units. For a word w of length L,

    2^j Z_w(n_j)=d_w3^j n+C,
    C=d_w(3^j-2^j)+2^j A_w,
    0<C<2*3^(L+j).

If L<e, then v3(C)<=L+j<e+j, giving

    g(Z_w(n_j)) >= n^2/(16*3^K).

If L>=e, the size bound gives g(Z_w(n_j))>2^(e-2)n. The base values exceed
the first of these bounds. Dividing by rho(n)=n^2/3^e yields

    rho(n_j)/rho(n) >= min(3^(e-K)/16, 2^(e-2)/u)>16.

This proves (22) for the entire infinite dictionary. QED.

Every ancestor of a multiple of three is on its pure even ray, because the
odd shortcut preimage is not integral. On that ray rho(2^t n)=4^t rho(n).
Hence an inverse-only cheaper-ancestor strategy also fails at these sources
at every depth. **These two facts do not rule out a short two-sided diagram
through a later forward endpoint; no such stronger all-diagram bound is
asserted.**

## 7. End-to-end attempt and the exact remaining obligation

The proven chain is:

1. rho is an explicitly computable, proper positive integer rank off 1.
2. A legal minimizing component supplies a finite physical strict decrease.
3. Such certificates compose by ordinary well-founded induction.
4. Entire unbounded formerly unsafe phases now receive these certificates.

The proposed next step was to infer that an actual source must always activate
one of the minimizing periodic patterns, perhaps after a fixed short lookahead.
That inference is FALSE: Sections 5 and 6 supply ordinary infinite families.
No complete Collatz proof results from this attempt.

A sufficient OPEN replacement is a complete, provably terminating selector
for every UNRESOLVED source, supplying either absorption at 1 or a physical
merging diagram to a strictly smaller rho-rank witness. Clocks may be unequal
and unbounded over sources; each returned diagram must be finite and checked.
Induction on rho would then prove convergence of the witness, its common
endpoint, and the original source. This covers positive cycles and divergent
orbits together, but existence/coverage of that selector is NOT proved here.

The summable weight 1/rho^2 is available for an alternative mass construction.
Neither an invariant tail envelope nor a strict killed supersolution is
established for it. The parent residual bound remains valid only for its
original weight/operator/certificate. Do not turn the representation of all
periodic patterns, the finite successful selector count, or the new reciprocal
sum into all-source absorption.

## 8. Review priorities

Check the strict word-length bound; the unrestricted word-count estimate and
its exact 20th-power margin; the component count with large affine offset;
the B_w=0 periodicity argument; both length regimes in the global minimum
lemma; the parity obstruction at the even-denominator exit; and the distinction
between forward-only delay and an all-diagram clock bound.

There is no external analytic theorem or formal proof assistant dependency in
these proofs. Exact source attribution, literature inspection scope, finite
protocol and publication boundary are recorded alongside this file.

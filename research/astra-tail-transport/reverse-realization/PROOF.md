# Reverse realization of low word ranks, sharp volume, and residual progress

**Status: PROPOSED pending independent mathematical review.** Author:
`astra-tail-transport-04`, 2026-09-09 (Asia/Jerusalem). Parent: PR105,
`912aec235fb2c5dbeac69a82454dd9c3d3a1e9fe`.

A full Collatz proof was attempted. This packet proves a universal reverse
realization theorem, a sharp counting exponent for the unchanged infinite-word
rank, and a total *partial* normalizer. The remaining progress theorem is OPEN.
A normalization echo is not a Collatz cycle. No earlier theorem, review,
canonical status, or finite clearance receipt is changed.

## 0. Definitions and elementary prerequisites

Use the ordinary shortcut map T(n)=n/2 for even n, (3n+1)/2 for odd n.
For finite physical path certificates use the unabsorbed map, including
1 -> 2 -> 1. Reaching 1 remains the convergence criterion. No transfer operator
is changed or implicitly introduced in this packet.

For a nonempty word w of length L and weight q, write

    P=3^q, D=2^L, T_w(n)=(P n+A)/D,
    A=sum_(i=0)^(L-1) w_i 2^i 3^(q-s_(i+1)),
    d=P-D, Z_w(n)=d n+A.

Here s_j counts ones before position j. A word specifies exactly one source
class modulo D. To see this, the two lifts of a length-j class differ after j
steps by an odd number, so exactly one realizes either next bit. Consequently
an ordinary integer x follows w iff P x+A=0 mod D. Endpoint integrality alone
is sufficient for finite parity legality in this precise binary shortcut
normalization. Positivity of x then makes every state positive.

Put g(0)=0 and g(z)=z^2/3^v3(z) for nonzero integers z. If z=3^e u with
3 not dividing u, then g(z)=3^e u^2 and g(z)>=|z|. In particular

    g(3^q z)=3^q g(z).

Retain EXACTLY the parent's dictionary

    W={nonempty w: 4*3^q >= 5*2^L}

and rank

    rho(1)=0,
    rho(n)=min(g(n),g(n-1),g(n+5), g(Z_w(n)): w in W), n>=2.

This is not the old R_* or P rank. Every word in W has q>=1, d>=D/4,
d>=P/5 and A>0. Hence g(Z_w(n))>Dn/4, while the base component g(n)<=n^2.
All winning words satisfy D<4n. The minimum is attained after finite search,
and n-1<=rho(n)<=n^2. These reproduce the parent ATT-201 in the scope used here.

For fixed q, the largest affine remainder after q odd and any number of even
steps is obtained by putting all even steps first. Thus

    0 < A/D <= (3/2)^q-1 < P.                         (0.1)

One may prove this without a rearrangement assertion: start from zero,
each odd step applies x -> (3x+1)/2, and each even step can only decrease a
nonnegative intermediate value. Deleting all even steps gives the upper bound.

## 1. ATT-301 — every sufficiently low word component is an ordinary ancestor

### Theorem

For EVERY n>=2 and w in W, if

    g(Z_w(n)) <= n^2,                                (1.1)

then

    x=(D n-A)/P = n-Z_w(n)/P                        (1.2)

is a positive ordinary integer, follows the entire physical word w, and obeys

    T^L(x)=n,        0<x<(4/5)n.                    (1.3)

No legality of w FROM n is assumed. The component need not attain rho(n):
the much weaker candidate ceiling n^2 suffices.

### Proof of integrality

For these words,

    d^2 >= 3^(q-1).                                 (1.4)

If q=1, W forces L=1 and d=1. If q>=2, P>=9 and d>=P/5, so
3d^2>=3P^2/25>=P. This proves (1.4).

Write Z_w(n)=3^e u, 3 not dividing u. If e<q, then

    g(Z_w(n)) >= (d n+A)^2/3^(q-1) > n^2,

contrary to (1.1). Therefore e>=q, and (1.2) is an integer.

### Proof of positivity

If x<=0, then A>=Dn. By (0.1), n<=A/D<P. Also Z_w(n)>=Pn. Therefore

    g(Z_w(n)) >= Z_w(n) >= Pn > n^2,

again contradicting (1.1). Thus x>0. Now P x+A=Dn proves that x is in the
exact finite cylinder of w. Finally x<(D/P)n<=(4/5)n because A>0. QED.

### Exact positive-orbit formula for the unchanged rank

Let E(n) consist of pairs (x,L) with

    1<=x<n,  T^L(x)=n,  2^L<4n,
    4*3^(q_L(x))>=5*2^L.

Then exactly

    rho(n)=min(g(n),g(n-1),g(n+5),
               3^(q_L(x))*g(n-x): (x,L) in E(n)).     (1.5)

Indeed P x+A=Dn implies Z_w(n)=P(n-x). Every word component that can beat
the base ceiling n^2 occurs in E(n) by the theorem. Conversely every element
of E(n) supplies that very word component. Values exceeding the base ceiling
can safely be retained or omitted.

Equation (1.5) replaces the negative periodic-center description with a finite
set of entirely positive ordinary ancestors. This does NOT say that those
ancestors have smaller rho: they have smaller ordinary value.

### Batch algorithm and complexity scope

To compute rho(n) for ALL 2<=n<=N, initialize the three base entries. For each
1<=x<N, follow exactly floor(log_2(4N-1)) shortcut steps, without truncating
large intermediate values. At every endpoint n in [2,N], test the two displayed
conditions in E(n), and update with 3^q*g(n-x). This is complete by (1.5).

The algorithm visits O(N log N) ordinary shortcut states. Intermediate values
and the arithmetic operands have O(log N) bits: T^j(x)+1<=(3/2)^j(x+1).
A simple repeated-division valuation implementation uses O(N(log N)^2)
elementary arithmetic operations. This is not a claim of linear bit complexity
or a logarithmic algorithm for one isolated n. Keeping only each rank and one
witness requires O(N) integer/witness slots. The finite checker compares this
algorithm with an independent formal-word enumeration.

### Why the expansion/spacing guard matters

More generally the argument applies when P>D and d^2>=3^(q-1). It does NOT
apply to every strictly expanding word without that condition. For w=110,
P=9,D=8,A=5 and n=7, Z=12 and g(Z)=48<=49. But the inverse value is 17/3,
not an integer. The parent's 5/4 gap is sufficient, not decoration.

## 2. ATT-302 — the entire infinite dictionary has square-root counting growth

For X>=1 define N_rho(X)=#{n>=2:rho(n)<=X}. Then

    floor(sqrt(X))-1 <= N_rho(X) < 350 sqrt(X).        (2.1)

Thus the counting exponent is exactly 1/2, up to absolute constants, not the
parent's weaker 39/40 upper exponent. In particular, for s>0,

    sum_(n>=2) rho(n)^(-s) < infinity iff s>1/2,       (2.2)
    sum_(n>=2) 1/rho(n) < 14,                        (2.3)
    sum_(rho(n)>Y) rho(n)^(-s)
       <=350s/(s-1/2) * Y^(1/2-s), s>1/2,Y>=1.       (2.4)

These are INITIAL rank-volume statements. They are not invariant bounds on a
transported ensemble and do not erase the parent's positive residual mass.

### 2.1 Word count

Let a_L count W at length L and put a=19/20. The indicator of membership is
at most sqrt(P/D). Therefore

    a_L <= ((1+sqrt(3))/sqrt(2))^L < 2^(aL).          (2.5)

For completeness, (2+sqrt(3))^10=262087+151316 sqrt(3), and

    (2^19-262087)^2-3*151316^2=59768833>0.

This proves the strict comparison in (2.5). We will also use

    2^(-a)<3/5,
    r=2^(-1/20)<29/30,

certified by 2^19*3^20>5^20 and 30^20<2*29^20, respectively.

### 2.2 Keep the progression modulus instead of discarding it

For a fixed word, write Z_w(n)=3^e u and g(Z_w(n))<=X. Necessarily
0<=e<=floor(log_3 X) and 1<=u<=sqrt(X/3^e). Since gcd(d,3)=1,

    u = A*3^(-e) mod d.                             (2.6)

For each e there are at most sqrt(X)*3^(-e/2)/d+1 choices. Positivity and
3 not dividing u can only remove choices. Since
1/(1-1/sqrt(3))<12/5, one word contributes at most

    (12/5)*sqrt(X)/d + 1+log_3 X.                    (2.7)

The progression (2.6) is the information lost in the old coarse count.
Moreover d>=2^(L-2), so

    sum_(w in W) 1/d_w
       <=4 sum_(L>=1) a_L/2^L <4 sum_(L>=1)r^L<116. (2.8)

### 2.3 Small ordinary sources absorb the long-word rounding error

Put K=floor((1/2)log_2 X). Sum (2.7) only over L<=K. The first term is less
than (1392/5)sqrt(X) by (2.8). The total rounding term is less than

    (5/2)(1+log_3 X) X^(19/40) < (105/2)sqrt(X).      (2.9)

To verify the last constant, set t=log X. Since log 3>1,
(1+log_3 X)X^(-1/40)<=(1+t)e^(-t/40)
<=1+40/e<21. The elementary inequalities 2<e<3 suffice.

A source supplied by ANY longer word has, from g(Z)>2^(L-2)n,

    n<4X/2^(K+1)<4sqrt(X).                          (2.10)

Count these sources once, not once per long word. The three base components
contribute at most (36/5)sqrt(X), after translation into positive z values.
Adding the constants gives

    1392/5+105/2+4+36/5=3421/10<350.

This proves the upper bound (2.1). Its lower bound follows from rho(n)<=n^2.
For s>1/2, positive integration proves (2.4) and convergence. For s<=1/2,
rho(n)^(-s)>=n^(-2s) proves divergence.

Finally properness gives N_rho(X)<=X. Integrate the smaller of X and
350sqrt(X), splitting at X=350^2:

    sum 1/rho(n) <=2 log 350+2<14.

For a rational check of log 350<6, e>8/3 and 8^6>350*3^6. QED.

## 3. ATT-303 — sharp ordinary-source tails survive the larger dictionary

For every real N>=2,

    1/(9N^2) <= sum_(n>N) 1/rho(n)^2 < 77/N^2.       (3.1)

This controls the complete infinite initial source population. It does not
bound the sum of infinitely many visits made by one surviving source.

First prove the scalar estimate

    S(B):=sum_(z>B,z integer positive) 1/g(z)^2
          < 7/(2B^2), B>=1.                        (3.2)

Write z=3^e u, drop the restriction 3 not dividing u, and split at
E=floor(log_3 B). For e<=E, put b=B/3^e>=1 and use
sum_(u>b)u^(-4)<=b^(-4)+(1/3)b^(-3)<=(4/3)b^(-3).
Summing gives less than 2/B^2. For e>E use sum u^(-4)<4/3; the geometric
sum contributes less than 3/(2B^2). This proves (3.2).

For one word and n>N, Z_w(n)>dN, so injection into positive z gives a tail
at most 7/(2d^2 N^2). Also

    sum_(w in W)1/d_w^2
       <=16 sum_(L>=1)2^(-21L/20)<16.

Thus all word components together contribute less than 56/N^2. The base
components contribute less than (7/2)(1+4+1)/N^2=21/N^2, using N-1>=N/2
for the shift n-1. Since the inverse square of a minimum is the maximum of
the component inverse squares, it is at most their positive sum. This proves
the upper bound in (3.1), with Tonelli justified by nonnegativity.

For a positive multiple of 3, every A_w is a ternary unit (its last odd
position is the sole term surviving modulo 3), hence every word Z_w(n) is
a unit and g(Z_w(n))>n^2. The two shifted bases are units as well and, for
n>=3, exceed g(n). Therefore rho(3^e)=3^e. Choose the first 3^e>N; it is at
most 3N and contributes at least 1/(9N^2). QED.

## 4. ATT-304 — a total component normalizer using ONE ordinary-value order

Use the following priority on a positive n:

1. At n=1 stop.
2. At even n, replace n by n/2 (physical word 0 forward).
3. At n=1 mod4, replace n by (3n+1)/4 (word 10 forward).
4. At n=2 mod3, replace n by (2n-1)/3 (word 1 backward).
5. At n=4 mod9, replace n by (8n-5)/9 (word 110 backward).
6. Otherwise enumerate the finite words D<4n in length/lexicographic order.
   If any w in W satisfies g(Z_w(n))<=n^2, use its ancestor (1.2).
7. Otherwise return n labelled RESIDUAL.

Every successful replacement x satisfies 0<x<(8/9)n. All operations terminate;
step 6 has an explicit finite bound. Repeated replacement therefore returns
1 or a residual in fewer than log(n)/log(9/8) replacements for n>=2. The
normalizer is not a universally successful convergence algorithm.

Each edge is a proved physical path in one direction, so n and its replacement
have the same convergence status. These edges compose into a finite physical
merging diagram. To check clocks explicitly, assign signed cumulative positions
s_0=0, adding a word length on a forward edge and subtracting it on a backward
edge. With M=max s_i, all T^(M-s_i)(n_i) coincide. The original and terminal
sources thus meet with nonnegative clocks whose SUM is at most the total edge
length. Each word is shorter than log_2(4n), with the elementary rules satisfying
the same bound. Hence the total physical certificate length is O((log n)^2).
No bound on intermediate rank is imposed, and rho need not decrease on a
backward edge.

### Residual classification

Every residual r>=2 lies in

    r=3,7,15,19,27 mod36.                            (4.1)

Indeed it is odd, is 3 mod4, is not 2 mod3, and is not 4 mod9. For all w in W,
g(Z_w(r))>r^2, and therefore

    rho(r)=g(r)     if 3 divides r,
    rho(r)=g(r-1)   otherwise.                       (4.2)

The first case follows from the unit argument in Section 3. In the second
case r=1 mod3 and v3(r+5)=1 because step 5 failed. Meanwhile v3(r-1)>=1,
so g(r-1)<g(r+5), and g(r-1)<g(r). This proves (4.2).

Every r=3 mod12 is a residual: no word Z_w(r) is divisible by 3, and none of
the four elementary rules applies. Thus the residual contains a positive-density
class; neither the sharp rho spectrum nor the finite census makes it empty.
A least ordinary counterexample, if one existed, would be one of these residuals.
That is a necessary reduction, not exclusion of the residual class.

The exact finite protocol has 569 initial residual labels in [2,4096]. Iterating
these rules alone sends 184 of the 4095 inputs to 1 and the others to a residual.
These numbers are not the count of convergent/nonconvergent sources; for example
3 is deliberately residual under this structural normalizer although its short
ordinary convergence is familiar.

## 5. ATT-305 — an odd illegal-minimizer family has a smaller physical ancestor

The universal theorem is more important than the following family, but the
family demonstrates a concrete repair of the preceding activation strategy.
For every e=9 mod16, e>=25, put

    n_e=(4*3^e-73)/17,
    x_e=(256*3^(e-4)-73)/17.

These are positive ordinary integers, since 3^16=1 mod17 and 4*3^9=73 mod17.
Exactly,

    T^6(x_e)=n_e with word 111010,
    x_e=(64n_e-73)/81 < (64/81)n_e.                   (5.1)

The target n_e is 19 mod36 and 3 mod8. Its actual first three bits are 110,
so 111010 is ILLEGAL from n_e, and none of the four elementary rules of the
normalizer applies. Nonetheless Z(n_e)=17n_e+73=4*3^e has g(Z)=16*3^e<=n_e^2,
so ATT-301 supplies (5.1) without any assumption on the later orbit.

The parent's ATT-204 minimum lemma additionally gives

    rho(n_e)=16*3^e,
    rho(x_e)=65536*3^(e-4)=(4096/81)rho(n_e).         (5.2)

The hypotheses are explicit: at n use exponent e and unit 4; at x use e-4
and unit 256. For e>=25, both exponents are at least 13 and both inequalities
2^h>2176u hold. This source-qualified dependency concerns the EXACT rho values;
the inverse legality and ordinary decrease (5.1) are independently proved here.

Thus the smaller witness has a LARGER rho. Our valid induction order is ordinary
value, not rho; replacing one by the other would invalidate the proof.
The first example is

    157520612935 --111010--> 199362025747.

A smaller example of the general nonminimal-component rule is

    1351 ->2027 ->3041 ->4562 ->2281 ->3422 ->1711.

Here n=1711 is 19 mod36 and the qualifying word component is NOT the global
rho minimum. The ceiling n^2, rather than only minimizing components, finds it.

For comparison, the parent's even exits s_h=(3^h-73)/17, h=5 mod16,h>=21,
also have ancestor (64s_h-73)/81. They already have elementary ordinary descent
by halving; they are not advertised as newly difficult value-induction cases.

## 6. ATT-306 — unbounded normalization echoes block the attempted completion

The attempted next inference was that forward iteration followed by the above
strictly contracting normalizer must produce strict overall progress within a
fixed number of forward steps. This is FALSE for every fixed number.

For each K>=1 choose any positive n with

    3 divides n,         n=-1 mod2^(K+2).             (6.1)

CRT supplies an infinite progression for every K. This n is residual. Its first
K shortcut steps are odd, and

    n_j+1=3^j(n+1)/2^j,
    n_j=11 mod12,       1<=j<=K.

Every normalizer application at n_j uses the inverse-one rule first, returning
n_(j-1), repeatedly, until it stops at n. Hence, with Nrm denoting the terminal
normalizer,

    Nrm(T^j(n))=n for EVERY 1<=j<=K.                 (6.2)

All moves and endpoints are positive ordinary integers. No infinite ordinary
all-odd trajectory is inferred; the finite source families vary with K.
Already 7 ->11 ->7 under T followed by Nrm is an administrative echo, not a
nontrivial T-cycle. Equation (6.2) permits arbitrarily long such cancellations.
More generally, a closed finite normalization diagram with nonzero TOTAL signed
shortcut clock implies a true eventual T-cycle (possibly the trivial one), by
the common-endpoint formula of Section 4. A zero-clock loop does not: the two
exponents in that formula are then equal. These echoes have clock defect zero.

### Exact open full-proof target

A sufficient condition, in fact equivalent to Collatz, is

    for every residual n>1 there exists finite k>=1
    with Nrm(T^k(n))<n.                              (Q-ATT-301)

If it held, strong induction on ordinary value would prove convergence: a
nonresidual already reduces, and a residual would acquire a finite physical
merger to a smaller convergent witness. Conversely convergence gives k with
T^k(n)=1. This elementary equivalence is NOT a new solution or evidence that
the required progress bound is easy. No theorem here establishes Q-ATT-301.

One may instead prove a different total lower-value merging selector. Either
way, repeating an inverse step that merely undoes the observed forward prefix
cannot be charged as genuine progress. A proof must handle the residual sources
rather than assume the echoes eventually break in a helpful direction.

## 7. Evidence and status boundary

The formal-word generator and positive-orbit verifier agree on every qualifying
source/word pair and every exact rho value in [2,4096]. They also compare complete
rank balls through rank 4095, physical normalizer compositions, the explicit
near-critical counterexample, large inverse families, and finite-horizon echoes.
Large-family global rho values are checked through the parent's written minimum
lemma hypotheses, NOT exhaustive giant dictionary enumeration. Normal and optimized
modes reject twelve resealed corruptions. Both implementations have one author.

The proofs supply universal quantifiers; finite tests do not extrapolate them.
Independent mathematical review is still required. No mass bound is iterated
under a refreshed envelope, no new operator is assumed to contract, and no
positive residual is set equal to zero. This is a proof attempt with a useful
new reverse interpretation and a still-open full-proof step, not a completed
proposed Collatz proof awaiting only routine verification.

# Route 1 — rank volume, distribution-free safe elimination, and an unsafe moment explosion

**Status: PROPOSED pending independent mathematical review.** This is an attempted
end-to-end mass proof. The safe operator is controlled in a stronger, distribution-
free norm, but the attempted extension to the actual unsafe process fails. The
complete unsafe supersolution remains OPEN. No Collatz proof is claimed.

## 0. Exact physical setup and the attempted proof

Use the shortcut map T(n)=n/2 for even n and (3n+1)/2 otherwise, absorbed at 1.
The parent [moving-rank packet](../pass4/MOVING_GHOST_RANK.md), frozen at
6266bd8f73ce2f8488c02fbe29f34fd2b4f289bc, defines

    z_a(n)=3^a(n+1)-2^a(2n+1),
    R_a(n)=z_a(n)^2/3^v3(z_a(n)),
    R(n)=min_(a>=0) R_a(n),

with zero rank for zero z. Its only positive zero is R(1)=0. For n>=2,

    n-1 <= R(n) <= n^2,
    R(n)=min(R_0,R_1,R_2,R_h), h=v3(2n+1),

where the fourth entry is needed only for h>=3. The total acceleration A consumes
all consecutive copies of the active word 1^a0: a=0 when n is even, otherwise
v2(n+1), and the repetition count is floor(v2(z_a(n))/(a+1)). This is an actual
finite shortcut path, not a stopping-time oracle. All native parent claims remain
proposed, not independently promoted by this continuation.

Put G={n>=2:4R(A(n))<=R(n)}, U={n>=2}\G. Repeated steps in G must reach 1 or U
by strict integer-rank descent. Thus the first subsequent return B from U to U,
after one A step and all following G steps, is total unless killed at 1. A
nonconvergent orbit would visit U infinitely often.

The attempted proof was: establish a finite rank moment, eliminate all G
excursions with a convergent operator series, then control repeated U returns.
Sections 1-2 establish the first two parts. Sections 3-4 show why two natural
versions of the third part fail on actual ordinary inputs.

## 1. T-A3-1001 — the rank has sharp square-root counting dimension

For real X>=1 define N_R(X)=#{n>=2:R(n)<=X}. Then

    floor(sqrt(X))-1 <= N_R(X) < 9 sqrt(X).                  (1)

In particular, for s>0,

    sum_(n>=2) R(n)^(-s) < infinity  iff  s>1/2.             (2)

One explicit estimate and one source-independent tail are

    sum_(n>=2) 1/R(n) <= 55/6,
    sum_(R(n)>X) R(n)^(-s)
       <= [9s/(s-1/2)] X^(1/2-s), s>1/2.                  (3)

### Proof and exact enumeration

For a nonzero z write z=+/-3^e u, u>=1, 3 not dividing u. A component rank is
m=3^e u^2, so e=v3(m) and Z=3^e u is determined by m. The three fixed indices
can supply at most n=Z, Z+1, Z-5. A minimizing index a>=3 must be the moving
index h=v3(2n+1); in that case v3(z_a(n))>=a, so 3<=a<=e. Each such index
supplies at most one positive source

    n=(Z-(3^a-2^a))/(3^a-2^(a+1)).

Consequently a fixed (e,u) contributes at most c_e=max(3,e+1) sources. Positivity,
divisibility and equality with the actual minimum still have to be checked; this
is an upper bound, not an assertion that every candidate is realized.

With r=1/sqrt(3),

    N_R(X) <= sqrt(X) sum_(e>=0) c_e r^e,
    sum c_e r^e = 3/(1-r)+r^3/(1-r)^2.

Since r<7/12 (147>144), the last sum is less than
36/5+343/300=2503/300<9. The lower bound in (1) follows from R(n)<=n^2.
For the reciprocal sum, enlarge to all u>=1 and use sum u^(-2)<=2:

    sum 1/R(n) <= 2 sum_(e>=0)c_e 3^(-e)
               =2(9/2+1/12)=55/6.

For s>1/2, positive integration of x^(-s) and (1), with the negative endpoint
term safely dropped, gives the tail in (3). For 0<s<=1/2, R(n)<=n^2 makes the
series dominate sum n^(-2s), which diverges. This proves (1)-(3).

The proof supplies a COMPLETE finite enumeration of every rank ball: loop over
3^e<=X and 1<=u<=sqrt(X/3^e), 3 not dividing u, generate the candidates above,
and retain those whose actual rank equals 3^e u^2. At X=2^24 the new certificate
finds 10,195 sources, the largest being 14,348,908. This finite enumeration is
not a claim that their future trajectories have been completely studied.

## 2. T-A3-1002 — safe excursions admit a distribution-free moment bound

For p>0 use the norm ||f||_p=sum_(n>=2) R(n)^p |f(n)|. Let K be the nonnegative
A pushforward killed at 1, and K_IJ its block from source set J to endpoint set I.
For ANY nonnegative f supported in G with finite norm,

    ||K_GG f||_p+||K_UG f||_p <= 4^(-p)||f||_p.            (4)

Proof: each retained source contributes R(A(n))^p f(n)<=4^(-p)R(n)^p f(n).
This requires no pointwise envelope, arithmetic equidistribution or resampling.
In particular ||K_GG^j||_p<=4^(-pj).

The exact induced unsafe operator is, as a positive series,

    H=K_UU+K_UG sum_(j>=0) K_GG^j K_GU.                   (5)

Each source follows one deterministic exit, so the series counts every finite
G excursion exactly once. For a nonnegative input f on U, suppose its entry
mass g=K_GU f has finite p-moment. Truncating (5) before j=L leaves error at most

    [4^(-p(L+1))/(1-4^(-p))] ||g||_p.                    (6)

The inequality is the geometric sum of (4). It is valid for an arbitrary actual
entry distribution. This improves the parent's need for a freshly proved
pointwise power-law envelope at each safe entry. It does NOT show that K_GU,
K_UU, or H preserves the finite-moment space. That was the crucial attempted
extension, and it is false as follows.

## 3. R-A3-1003(a) — one unsafe step can destroy a finite moment

For e=4 mod 16, e>=4, put x=3^e and y=(9x+7)/16. Then

    A(x)=y,  R(x)=x,  R(y)=9(x-1)^2/256,
    x,y in U, and hence B(x)=y.                           (7)

These are also part of the parent's backward-power family; the NEW use is the
all-source operator-space obstruction, not a new claim for the four-step path.

Here is the required reconstruction. v2(x-1)=4 and v2(x+1)=1, so A consumes two
copies of 10. At y the three possible component ranks are

    (9x+7)^2/256, 9(x-1)^2/256, 3(3x+29)^2/256,

and the middle is smallest; h(y)=1. Also e=4 mod16 gives x=17 mod64, hence
y=2 mod4 and A(y)=y/2. Since y/2=2 mod3,
R(y/2)=(y/2-1)^2>R(y) for y>4. Further R(y)>R(x) for x>=81. This proves
both unsafe guards. All witnesses exceed any fixed floor after finitely many e.

Take the explicit full-support unsafe input f(n)=1_U(n)R(n)^(-2). By (3),

    ||f||_1=sum_U 1/R(n) <=55/6.

But each pair in (7) contributes

    R(y)f(x)=9(x-1)^2/(256x^2) >=25/729>1/32.

The y are distinct, so Tonelli gives

    ||Hf||_1=infinity.                                    (8)

The subscript 1 here means the R-weighted p=1 norm, NOT the ordinary unweighted
mass norm. H still preserves or decreases finite unweighted mass, as every
killed deterministic pushforward does. Equation (8) rules out a bounded unsafe
extension in the attempted rank-moment space, even though the safe resolvent is
well controlled. No finite cutoff or larger core repairs this infinite family.

## 4. R-A3-1003(b) — all summable monomial weights fail the unsafe supersolution

Let w(n)=n^(-s)R(n)^(-t) on U, with fixed real s,t. If sum_U w(n)<infinity,
then the pointwise inequality H w<=w cannot hold everywhere above any floor.
This rules out the complete two-parameter power-weight attempt, not all weights.

Use the arithmetic phase family proved in [UNSAFE_REPAYMENT.md](UNSAFE_REPAYMENT.md).
There is a fixed positive-density ordinary progression in U on which
R(n)=(n-1)^2/9. Summability therefore requires s+2t>1. Arbitrarily long positive
ordinary paths can remain in U for repeated words 111010, with cycle endpoints
n_j=alpha+(81/64)^j(n_0-alpha), alpha=-73/17, and R(n_j)=(n_j-1)^2/9.
Choose a prefix of K cycles inside a K+1-cycle shadow, so no safe endpoint
has yet been entered. Along it B agrees with each physical A step. Its endpoints
satisfy

    log(w(n_0)/w(n_K))=(s+2t)K log(81/64)+O(1)>0

for large K. The O(1) is uniform in these sources n_0>=11, since the fixed
additive shift changes endpoint ratios only by bounded factors. If H w<=w,
each path edge would imply w(source)<=w(endpoint), and their concatenation
contradicts this inequality. Finite ordinary shadows, not an infinite ordinary
periodic orbit, are used. Fixed real powers need no arithmetic approximation.

The checked sample weights (s,t)=(0,1),(2,0),(4,-1),(3,1),(-1,2) are genuinely
summable on the full domain: use (3), R<=n^2, or n<=R+1 as appropriate. The
checker supplies an individual unsafe-edge violation for each. The theorem
covers every summable monomial parameter pair, not just those five.

## 5. Full closing implication and exact point where the attempt stops

A positive weight w on U with finite UNWEIGHTED sum and H w<w pointwise would
prove Collatz. Indeed, a hypothetical exceptional orbit visits U infinitely
often. Its set E_U of exceptional U states is forward and backward invariant
under the total killed-return map B. Positive summation gives

    sum_(y in E_U) H w(y)=sum_(x in E_U)w(x),

contradicting strict deficits. This includes cycles and nonperiodic failures.
This elementary invariant-mass criterion is credited to the earlier project
packets, not claimed as a new general operator theorem.

The explicit power candidates fail by Section 4; the rank-moment extension
fails even more strongly by Section 3. The next missing theorem is a weight or
integrated estimate that pays for actual unsafe transitions and retains a
finite total mass. The safe tail (6) is available, but substituting it for the
unproved unsafe estimate would be circular. Neither a finite success rate nor
the exact square-root dimension supplies that missing correlation.

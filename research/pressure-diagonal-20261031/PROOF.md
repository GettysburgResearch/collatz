# Collision-free finite-clock coercivity for ordinary pressure

**PROPOSED; self-audited, not an independent acceptance or a proof of F(t)->0.**
This continuation is based on PR143 at
`41a408e5e617fb4e65142485f6f3ff3e6ef6c408`, including PR140 pass 4 at
`fe2247fcd7730c15430941a7b6e011d006d41d84`.

The new inequality is unconditional relative to the explicitly identified
finite-path packing input. It turns a prospective moment bound into a
quantitative, all-source finite-time energy bound. The required moment bound
is STILL OPEN. No averaging-to-pointwise inference is made.

## D1. Remove the cross-source collision terms

For positive odd x use U(x)=(3x+1)/2^a(x), a(x)=v2(3x+1), and write

    t_j(x)=U^j(x), J_j(x)=3^j/2^(sum_(i<j) a(t_i(x))),
    P_j(x)=product_(i<j)(1+1/(3t_i(x))),
    b_j(x)=J_j(x)/t_j(x)=1/(x P_j(x)).

All clocks are odd-to-odd clocks. Positive cycles are retained in these
quantities. In particular 0<b_(j+1)(x)<b_j(x)<=1/x.

Define the DIAGONAL fourth-derivative moment

    D_j = sum_(x positive odd) J_j(x)^4/t_j(x)^2
        = sum_x b_j(x)^4 t_j(x)^2.                         (1)

For PR143's Z_j(t)=sum_(t_j(x)=t) J_j(x)^2 and
S_j=sum_t Z_j(t)^2/t^2, positivity gives

    D_j <= S_j.                                             (2)

The difference consists exactly of cross terms between DISTINCT sources
that meet at the SAME odd clock. Bounding D_j therefore asks strictly less
than bounding S_j: no such off-diagonal terms need be estimated. The
inequality is uniformly strict for j>=1: in fact S_j >= (17/15)D_j,
with equality at j=1. To prove this, group sources by their first odd image.
The full predecessor fiber is x_k=4^k x_0+(4^k-1)/3, k>=0, with derivative
d(x_k)=4^(-k)d(x_0). For any later common clock, its squared-derivative
population sums with factor 16/15, while its diagonal fourth powers sum
with factor 256/255. Squaring the first sum and dividing by the second
gives (16/15)^2/(256/255)=17/15. Different first-image groups can only add
nonnegative cross terms if they later merge. At j=1 there are no such
different-group collisions. No reverse uniform comparison is claimed.

This is a linear inverse-population statistic, not a quadratic density
statistic. Its fourth power refers to the branch multiplier, not a fourth
moment of a random independent forward valuation process.

## D2. Kill only after the first actual repeated odd state

For Q>=1 let A_Q be the sources whose Q values

    t_0(x),...,t_(Q-1)(x)

are pairwise distinct. Define

    Ebar_Q=sum_(x in A_Q) b_(Q-1)(x)^2.                      (3)

The sets A_Q decrease. The source weights also decrease, hence Ebar_Q is
nonincreasing. It differs from PR143's E_(Q-1): a source is removed after
its first repetition, rather than being kept through repeated cycle laps.
No source is killed just because it is large or outside an inspected bank.

Dominated convergence under the reciprocal-square envelope gives

    lim_Q Ebar_Q = sum_C Lambda_C,                          (4)

where C ranges over the actual nonperiodic merger components of PR140 Q2.
An eventually periodic source is removed at a finite Q. A nonperiodic
source stays active and its b_j tends to r(x)/x. The first-hit discount
ensures r(x)>0, with the parent's proof status retained.

Consequently Ebar_Q->0 iff every positive orbit is eventually periodic iff
F(t)->0. This is a characterization, NOT a proof of any of those assertions.
Nontrivial positive cycles remain allowed.

For finite odd X, Ebar_(Q,X) is computed by exactly Q-1 odd steps per source
x<=X, with a literal seen-state set. Regardless of all uninspected sources,

    0 <= Ebar_Q-Ebar_(Q,X) < 1/[2(X+1)].                    (5)

Let M_(Q,X) be the largest odd state seen among these prefixes, including
the initial state. If an inspected source has already repeated, it cannot
hit any larger unseen target later. If it has not repeated, its future
normalized first-hit weights are at most its present b_(Q-1). Thus

    F(t) < Ebar_(Q,X)+1/[2(X+1)]
    for EVERY positive odd t>M_(Q,X).                       (6)

This is a valid unfinished-prefix certificate. Unlike an oracle for all-time
basin membership, its computation always terminates at its supplied clock.

## D3. A reciprocal-envelope interpolation lemma

Let nonnegative numbers c_x, indexed by positive odd integers, satisfy
c_x<=x^-2. Put E=sum_x c_x and A=sum_x c_x^2. Then

    A >= E^3/4.                                             (7)

For E=0 this is immediate. Otherwise E<5/4. Put N=ceil(1/E).
The omitted odd reciprocal-square tail is less than 1/(4N)<=E/4, so the
first N coordinates carry at least 3E/4. Cauchy--Schwarz and
N<=1/E+1<9/(4E) give

    A >= (3E/4)^2/N >= E^3/4.

The cube cannot be replaced by a uniformly better small-E power using
only this envelope: the family c_x=min(lambda,x^-2), lambda down to zero,
has E comparable to sqrt(lambda) and A comparable to lambda^(3/2).
This is sharpness of the envelope exponent, not a dynamical sharpness claim.

## D4. The quantitative finite-time inequality

Assume the following SPECIFIED finite-path packing input, with K>=1 and
0<beta<=1: every finite simple odd path S satisfies

    #{t in S:t<=Y} <= K Y^beta, every Y>=1.                  (8)

Then for EVERY positive integer Q,

    Ebar_Q^3 <= C_(K,beta) Q^(-1-2/beta) sum_(j=0)^(Q-1) D_j,
    C_(K,beta)=4(1+2/beta) K^(2/beta).                      (9)

No positive source is assumed convergent in this inequality.

### Proof

For x in A_Q, put c_x=b_(Q-1)(x)^2. At every earlier j<Q,
b_j(x)^4>=c_x^2. Sort the Q distinct states on this SAME trajectory as
z_1<...<z_Q. Equation (8) gives z_i >= (i/K)^(1/beta), and hence

    sum_(j<Q) t_j(x)^2
      >= K^(-2/beta) sum_(i=1)^Q i^(2/beta)
      >= K^(-2/beta) Q^(1+2/beta)/(1+2/beta).              (10)

There is no reordering of physical dynamics: sorting is used only to bound
the sum of squared state values. Tonelli, (1), and (10) give

    sum_(j<Q) D_j
      >= K^(-2/beta) Q^(1+2/beta)/(1+2/beta)
          *sum_(x in A_Q) c_x^2.

Apply (7) to c_x on A_Q and zero outside. This proves (9).
The argument uses the diagonal terms alone, so source coalescence is not
an uncontrolled loss and no Cauchy--Schwarz is applied to unknown fibers.

### Available explicit constants, with dependency boundaries

The weakest useful choice K=1,beta=1 is elementary: a simple path has at
most Y positive integer values below Y. It gives Ebar_Q^3<=12 Q^-3 sum D_j.

PR140 pass3/PRESSURE_BRIDGE.md, B1, supplies K=5,beta=39/40.
PR140 pass4/WINDOWS.md, W2, supplies K=16,beta=19/20 for raw shortcut paths
in every translated interval. Expanding a simple odd path gives a simple
shortcut path, so that stronger input applies here without changing clocks
in (1), (3), or (9). Taking an interval [1,floor(Y)+1) gives (8).
Their PROPOSED review statuses are inherited, not upgraded.

The previous attached research packet additionally proposed the exact entropy
endpoint K=10,beta=H_2(log_3 2). That sharper option is NOT needed here and
is not silently treated as a merged dependency. The preserved attachment's
producer and separate verifier were freshly replayed in this session.

## D5. A weaker sufficient target, and an explicit conditional rate

Suppose, for some p>=0 and constant B, the all-source diagonal moments obey

    D_j <= B (j+1)^p for all j>=0.                          (M_D)

Then sum_(j<Q)D_j<=B Q^(p+1). Equation (9) gives

    Ebar_Q <= (C_(K,beta) B)^(1/3) Q^(-(2/beta-p)/3).       (11)

In particular, using K=16,beta=19/20, the QUADRATIC diagonal bound p=2
would give the explicit conditional rate

    Ebar_Q <= [4*(59/19)*16^(40/19)*B]^(1/3) Q^(-2/57),   (12)

and therefore prove F(t)->0 via (4), or via the finite certificate (6).
A bound on the Cesaro sum alone is sufficient; individual D_j need not be
controlled. More generally it suffices that

    liminf_(Q->infinity) Q^(-59/19) sum_(j<Q)D_j=0.         (13)

Because Ebar_Q decreases, a subsequence suffices. This is a weaker target
than PR143's same estimates for S_j, and (9) quantifies the consequence at
finite clocks. No pointwise rate F(t)=O(t^-gamma) follows from (12) without
also controlling the prefix-height threshold M_(Q,X).

**The first unsupported inference is (M_D), or (13).** The exact finite-clock
computations in TRACE.md do not establish it. The unconditional bound obtained
from the bounded operator in D6 below is exponential, not polynomial.

## D6. Finiteness and computability without an all-time simulation

On l2 of positive odd integers put

    (R4 f)(x)=d(x)^2 f(U(x)), d(x)=3/2^a(x), u(x)=1/x.

Then D_j=||R4^j u||_2^2. Summing the fourth powers of the derivative over all
one-step predecessors gives column sums 0,27/85,432/85 for target residues
0,1,2 modulo 3, respectively. Thus

    ||R4||^2=432/85,
    D_j <= (432/85)^j*pi^2/8 < (432/85)^j*5/4.             (14)

All finite clocks are well-defined. Their infinite-source values can be
computed from a finite ternary residue table with rigorously bounded tails,
as described separately in TRACE.md. Formula (14) proves finiteness, not the
quadratic target.

## Limits of this continuation

The universal pointwise pressure limit is still OPEN. We have not found a
contradiction to (9), nor proved the missing moment bound. The finite-time
inequality is not described as a full proof. It allows an escaping source to
force the diagonal moments to grow sufficiently fast. It also allows long
transient excursions of known-convergent sources; no per-step contraction is
assumed. No new theorem excludes nontrivial positive cycles.

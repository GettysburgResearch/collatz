# Repeated spikes: first-exit mass and forward-closed clearance forests

**Status: PROPOSED pending independent mathematical review.**
Author: `astra-tail-transport-02`. Date: 2026-09-07.
Parent: PR105, `3c7fa4a0a2c5c48792c8efd5f5e90e94e44dab0f`.

**Outcome.** The fixed canonical input admits a certified, nonzero, uniform
all-future mass bound. At most `12/2^48` survives after 52 quarter-unsafe
returns, regardless of all later spike sizes and clocks. A separate bound
controls the *sum* of late visits to a certified forward-closed forest.
Neither estimate sets the remaining mass to zero. No Collatz proof, new
contraction factor reusable on arbitrary transported inputs, or cofinal
clearance theorem is supplied.

The general measure/finite-graph lemmas are elementary. The contribution is
an explicit, lossless certificate interface for the actual moving-rank map,
its analytic remainder, independently reconstructed ordinary certificates,
and the sharp distinction from the failed reset-of-envelope argument. No
external novelty claim is made for finite absorbing-chain algebra.

## 1. Physical system and notation

Use the shortcut map

    T(n)=n/2 (n even), T(n)=(3n+1)/2 (n odd), killed at 1.

Use exactly the parent's moving rank, not the section rank P:

    d_a=3^a-2^(a+1), c_a=3^a-2^a,
    z_a(n)=d_a n+c_a,
    R_a(n)=z_a(n)^2/3^v3(z_a(n)),
    R(n)=min_(a>=0) R_a(n), n>=2; R(1)=0.

Zero components receive rank zero. For n>1 the active index is a=0 when n is
even, and a=v2(n+1) otherwise. A consumes the maximal legal number of copies
of the physical word `1^a0`. It is an explicit total finite shortcut path:

    k=floor(v2(z_a(n))/(a+1)),
    A(n)=(3^(ak) z_a(n)/2^((a+1)k)-c_a)/d_a.

The original proofs of physical exactness, killing conventions and properness
are pinned in [SOURCES_AND_STATUS.md](SOURCES_AND_STATUS.md); the parent also
reconstructs them. The new verifier separately checks the literal paths.

Use ONLY the quarter-safe set

    G={n>=2: 4R(A(n))<=R(n)}, U={n>=2}\G.

From x in U, B takes one A step and every ensuing G step, stopping at the next
U state or 1. B is total: every intermediate G step decreases a positive
integer rank. It counts arbitrary finite safe excursions, not a fixed shortcut
clock. Define the killed pushforward on nonnegative summable measures on U by

    (Hf)(y)=sum_(x in U:B(x)=y) f(x), y in U.

Endpoint rows and source columns are used. All sums are nonnegative. Each
source has at most one surviving endpoint, so

    ||Hf||_1 <= ||f||_1.                                    (1)

Fix the explicit full-support input

    w(x)=1/R(x)^2 on U,        mu_j=H^j w.

It is a finite measure, not initially normalized to probability. Finite
measures obtained by merging distinct sources retain the sum of their weights.
This paper distinguishes three quantities:

- mass at an endpoint set at one time;
- mass of sources that EVER visit that set, charging each source once;
- the sum of mass on that set over all visit times, counting repeat visits.

The first two are bounded by the total initial mass; the third need not be.
None is a rank moment unless the rank is explicitly inserted in the summand.

## 2. Credited arithmetic input: complete rank balls and their tails

The parent's rank reconstruction gives

    n-1<=R(n)<=n^2,
    R(n)=min(R_0,R_1,R_2,R_h), h=v3(2n+1),               (2)

with R_h needed only when h>=3. For completeness, z_(a+1)>3 z_a when a>=2.
Writing t=v3(n+1), away from a+t=h the valuation of z_a is min(a+t,h).
The increasing numerators eliminate every index a>2 except a=h. The lower
bound follows from z^2/3^v3(z)>=|z|; the upper bound uses index zero.

If R(n)=3^e u^2, 3 does not divide u, put Z=3^e u. A minimizing fixed index
supplies at most n=Z, Z+1, Z-5. A minimizing index a>=3 must be h and satisfy
3<=a<=e; it supplies at most

    n=(Z-c_a)/d_a.

Retain only positive integers with their *actual minimum rank* equal to the
proposed value. Thus a fixed (e,u) gives at most c_e=max(3,e+1) sources. These
facts yield a COMPLETE finite enumeration of the sublevel

    C_Y={x in U:R(x)<=Y},               Y>=1.

It is not a chronological cap or a bound on intermediate states.

The reviewed source's counting bound can be reconstructed directly:

    #{n>=2:R(n)<=X} <=sqrt(X) sum_e c_e 3^(-e/2)<9 sqrt(X).

For r=1/sqrt(3), the sum is `3/(1-r)+r^3/(1-r)^2`; r<7/12 gives a value
below 9. Consequently positive integration gives

    epsilon_Y := sum_(x in U:R(x)>Y) w(x)
      <= 2 integral_Y^infinity 9 sqrt(t) t^-3 dt
      =12 Y^(-3/2).                                      (3)

No external predecessor estimate is used. This is an *initial rank-tail*
bound. It is not asserted to be a tail envelope for H^j w.

## 3. ATT-101: source truncation has no repeated-return error accumulation

Let C be any finite set of initial unsafe sources. Put

    w_C=1_C w, e_C=1_(U\C)w, epsilon_C=||e_C||_1.

For every j>=0, positivity and (1) give the exact decomposition

    mu_j=H^j w_C+H^j e_C,
    0<=mu_j-H^j w_C,  ||mu_j-H^j w_C||_1<=epsilon_C.       (4)

The same bound holds for any family of source-dependent observation clocks:
each omitted source is still either killed or represented by one atom of its
original mass. Observation clocks can have no common cap and can differ for every source;
each clock whose endpoint is used is finite. No optional-stopping theorem or
endpoint-resampling premise is used.

For any event described by the entire source history, the error made by
omitting U\C is at most epsilon_C, provided the event charges that source at
most once. This includes the event of *ever* exceeding a given rank, and is
not restricted to bounded time horizons.

If every source in C is certified killed within L B steps, then

    ||mu_j||_1<=epsilon_C          for EVERY j>=L.          (5)

If every complete physical path from C has ordinary height at most M, then

    sum_x w(x) 1{some pre-kill shortcut state has R>M^2}
       <=epsilon_C.                                      (6)

Here R(v)<=v^2 from (2). In particular (6) bounds every individual time tail
and the ever-spike mass under any of the physically legitimate clocks.

**Why there is no factor j.** The omitted part is one fixed initial measure,
not new uncertainty created after each step. Equation (4) follows by applying
H^j once to that same measure. Summing epsilon_C over clocks would count the
same unresolved source repeatedly. Conversely, (4) does NOT bound the sum of
all visit masses by epsilon_C. Section 5 states the additional condition under
which a genuine occupation sum is controlled.

For C=C_Y, (3) supplies a uniform error `12Y^(-3/2)`. This is useful even when
transported first rank moments or critical weak moments are infinite.

## 4. ATT-102: exact finite first-exit accounting, including trapped cycles

Let N=|C_Y|, K=1_C H 1_C, and L_out=1_(U\C) H 1_C. Define

    Phi_Y=L_out sum_(i=0)^(N-1) K^i w_C.                  (7)

This is the complete low-source first-exit measure. The columns encode actual
B edges. A source still inside a set of N states after N transitions has
repeated a state, so it stays in that finite cycle forever and can never make
a first exit later. A killed source makes no exit either. Every exiting
source is therefore counted exactly once in (7), at its first outside
endpoint. Endpoint merging adds weights and does not identify sources.

Let q_Y=||Phi_Y||_1. Let c_Y be the initial weight of low sources trapped in a
cycle entirely inside C. Let a_Y be the initial weight killed before first
exit. The three source classes partition C. Write

    E_Y=sum_x w(x) 1{exists j before killing: R(B^j(x))>Y}.

Then exactly

    E_Y=q_Y+epsilon_Y,
    q_Y<=E_Y<=q_Y+12Y^(-3/2),                             (8)

and, for EVERY j>=N,

    ||mu_j||_1<=q_Y+c_Y+12Y^(-3/2).                      (9)

The finite classifiers give q_Y,c_Y and actual exit/kill clocks without
assuming any outcome of the subsequent outside trajectory. Rational
rounding of the finite sums can be added explicitly to (8)-(9).

**Important resolvent boundary.** K can have eigenvalue one on a trapped
cycle. We do not assert existence of `(I-K)^(-1)`. The finite expression (7)
is nevertheless exact for exit flux: its remaining tail has zero outward
flux, even if K's internal mass persists forever. A separate finite-cycle
control in the experiment tests this distinction.

The limit `lim_(Y->infinity) E_Y` equals the initial weight of divergent
basins: every absorbed or eventually cyclic path has finite peak, while each
divergent path eventually exceeds every proper rank ball. This follows from
dominated convergence over the summable source atoms. It agrees with the
parent's escape identity. Equation (8) does not prove that q_Y tends to zero.

## 5. ATT-103: replace a safe region by a forward-closed clearance forest

A *clearance forest* is a finite F subset U with

    B(F) subset F union {1},
    ell(1)=0, ell(x)=1+ell(B(x)) for x in F,               (10)

where ell(x) are positive integers. Every edge includes an exact physical
certificate of its entire B return, retaining each safe guard. The maximum
label L proves absorption in at most L B returns. No bound on the rank or
ordinary size along an edge is required.

Write W=U\F and order the operator blocks as F,W:

                 [ K   J ]
             H = [       ],       K^L=0.                (11)
                 [ 0   Q ]

The zero lower-left block is decisive: once a source enters F it cannot
return to the uncertified dynamics W. A rank-safe region G generally lacks
this property; that earlier induced process has feedback through unsafe
states and requires a fresh domain argument at re-entry. F is a verified
finite basin fragment, not a renaming of G and not a new globally decreasing
rank.

For a nonnegative summable initial measure f, let f_W=1_W f and

    g_t=J Q^t f_W.

These are first-entry masses into F. Nonnegative summation and deterministic
killing give

    sum_(t>=0) ||g_t||_1 <= ||f_W||_1.                   (12)

One can prove (12) either by disjoint source first-entry events or by
`||Jv||_1+||Qv||_1<=||v||_1` and telescoping. Every entrant is propagated by
K for at most L time indices. Therefore

    sum_(j>=L) ||1_F H^j f||_1 <= L ||f_W||_1,            (13)
    sup_(j>=L) ||H^j f||_1 <= ||f_W||_1.                 (14)

The first inequality is a genuine *undiscounted infinite occupation sum*,
counting repeat visits within F, not merely an ever-entry probability. The
initial f_F contribution is zero for j>=L. For the other contribution, expand
`sum_(t<j) K^(j-1-t) g_t`, sum over j, and use positivity, K^L=0 and (12).
The second inequality follows directly from absorption of f_F and (1).

If C_Y subset F and `0<=f<=C w` on U, then

    ||f_W||_1 <= C epsilon_Y <= 12 C Y^(-3/2).            (15)

Equations (12)-(15) tolerate arbitrary transported input shapes, unsafe
spikes outside F, and all later returns. They use the initial envelope only
once. They do NOT control the infinite occupation sum inside W, nor a
uniform positive rank moment there.

The certificate can be found by a bounded attempted graph expansion, allowing
large exits and later re-entries. Reverse propagation from 1 verifies (10).
A cycle, arithmetic resource cutoff or unclosed path is UNRESOLVED, never
accepted as an absorbed source. The finite protocol below succeeds at its
specified three rank bounds; success at every larger bound is not assumed.

## 6. ATT-104: the reconstructed all-source, all-future certificate

X-ATT-002 independently reconstructs complete rank balls and their unsafe
parts. The counts and maxima below are the content of the finite certificate,
not claims obtained by extrapolating the search.

| Y | all non-core sources with R<=Y | unsafe initial sources | B-forest nodes | largest B hitting time | largest shortcut hitting time |
|---:|---:|---:|---:|---:|---:|
| 2^24 | 10,195 | 4,922 | 6,940 | 39 | 184 |
| 2^28 | 40,792 | 19,701 | 27,866 | 47 | 222 |
| 2^32 | 163,168 | 78,828 | 111,763 | 52 | 261 |

At Y=2^32, 32,935 forest vertices have rank GREATER than Y. Thus the
certificate does not impose the false intermediate-rank cap previously
refuted by the project. The largest *initial* source in the complete rank
ball is 3,486,784,402. The maximum physical value on the unsafe-root
clearance forest is

    M=21,206,132,666,
    M^2=449,700,062,647,992,267,556.                      (16)

The maximum B hitting time is first attained at source 156159. The maximum
physical peak is first attained at source 172186879. Both are reconstructed
by literal physical iteration in the verifier. The generator instead uses
closed-form maximal modules and their exact in-module peak formulas.

For the FIXED canonical w on U, the conclusions are

    ||H^j w||_1 <= 12/2^48 = 3/2^46
                  <4.264 * 10^-14,     EVERY j>=52;      (17)

    sum_(j>=52) ||1_F H^j w||_1 <=52*(12/2^48);           (18)

    total first-entry mass to F from initial U\F
                  <=12/2^48;                            (19)

    mass of sources EVER exceeding rank M^2
       at ANY pre-kill shortcut time <=12/2^48.           (20)

Also, the raw shortcut pushforward of the SAME initial w has surviving mass
at most 12/2^48 at every raw time k>=261. The entire physical forest is
certified, so this does not identify a B clock with a shortcut clock.

For any input `f<=Cw`, multiply these bounds by C. They are all-source bounds:
no assumption is made that an omitted source converges. Its complete original
weight remains in the upper error, whatever it does at any future time.
They are NOT time-truncated estimates and do not deteriorate when j grows.

If normalized to probability, initial mass is at least w(3)=1/9 (3 is unsafe,
R(3)=3), so the surviving fraction in (17) is at most `108/2^48`. This is a
statement about this deliberately chosen summable weighted ensemble, NOT the
fraction of integers proved convergent or a percentage of Collatz solved.

### What following the exits added

The restricted first-exit classifier at Y=2^32 finds 25,422 low sources that
leave C_Y before absorption, with source weight approximately 2.19509e-9.
Its full all-future error upper bound is below 2.196e-9, and no trapped cycle
occurs within the finite C_Y graph. Stopping the argument at that boundary
would retain those exiting source weights forever as uncertainty.

The clearance forest follows the physical exits rather than resetting their
distribution. Their 32,935 additional outside vertices all reconnect to 1.
That removes the low-source exit term; only the analytically bounded UNKNOWN
initial high-rank input remains in (17). Arbitrarily many future excursions of
that remaining input do not create new mass. This is the concrete positive
control achieved here, not a power of an iterated one-return constant.

## 7. ATT-105: a tiny canonical output is not a reusable l1 contraction

For the actual unsafe H,

    ||H^J||_(l1(U)->l1(U))=1   for EVERY finite J>=0.     (21)

Upper bound: (1). For the lower bound use the pinned, reconstructed unsafe
phase `111010=1110|10`. Put

    F0(n)=(81n+73)/64, Z(n)=17n+73.

For any K, impose `n>=11`, `n=10 mod243`, and

    2^(6(K+1)) divides Z(n).                             (22)

These have infinitely many positive ordinary solutions by CRT, since 17 is
odd. The physical word `(111010)^(K+1)` is legal by exact parity cylinders.
On all its interior cycles, maximal A modes alternate 3 and 1, one copy each.
At cycle boundaries s and intermediate t=(27s+19)/16, the exact ranks are

    R(s)=(s-1)^2/9, R(t)=(t+5)^2/9,
    R(t)/R(s)>1,
    R(F0(s))/R(t)=9(t-1)^2/[16(t+5)^2]>1/4.             (23)

Here s>=11, t>13. For alpha=-73/17, the valuations of alpha, alpha-1,
alpha+5, 2alpha+1 are respectively 0,2,1,1. At beta=-103/17 the valuations
of beta, beta-1, beta+5, 2beta+1, z_3(beta) are 0,1,2,3,4. Agreement with
alpha gains four ternary digits each cycle, and agreement with beta gains
three on the first phase. Initial agreement modulo 3^5 therefore freezes
all possible minimizing components, proving the two rank formulas. These
arithmetic identities are credited to the source, not inferred from samples.
Consequently every desired finite initial segment is genuinely unsafe and
B agrees with the individual A modules. Choose K large enough that J steps
end strictly inside the phase. The unit atom delta_n survives J returns and
has unchanged unweighted mass one, proving (21).

Different J can require different ordinary sources. This is not one all-time
ordinary periodic orbit. The experiment constructs and physically replays
nine such sources, including J=52 and J=128; (22)-(23) establish the general
quantifier.

Thus (17) cannot be multiplied by itself after another 52 returns. Its
input-to-output estimate is from the cone `f<=Cw` to unweighted mass; the
output is not known to obey the same envelope with coefficient C. Equation
(21) rules out interpreting it as a strict operator contraction in l1.

## 8. End-to-end attempt: exactly what is and is not finished

The earlier attempt tried to iterate a rank-tail envelope through unsafe
returns. Its critical version is false. This continuation instead:

1. keeps the one fixed original source measure;
2. counts outward flux once per source, even with later re-entries;
3. follows a complete finite family of exits into a forward-closed forest;
4. eliminates that forest without feedback and bounds the remaining input
   independently of time and of its future spike behavior.

This supplies (17)-(20), including a true infinite occupation sum on F. It
leaves the residual dynamics on W unconstrained apart from its SMALL TOTAL
MASS. A single exceptional source can have an arbitrarily small positive
weight. A bound such as 4.264e-14 does not exclude that atom.

To finish by this route, one would need a proved cofinal family Y_m->infinity
and finite, physically certified clearance forests F_m containing C_(Y_m).
Equations (14)-(15) would then force the surviving mass to zero. Full support
would exclude both divergence and nontrivial cycles. The construction of
such a cofinal family, or a non-computational argument forcing the remaining
mass to vanish, is NOT proved here. The bounded search procedure does not
come with a theorem guaranteeing success at arbitrary Y.

This final missing statement is not advertised as a simplification of the
conjecture merely because it is phrased in mass language. Its purpose is to
expose the exact new proof obligation without either double-counting spikes
or silently resetting a transported distribution. All-time uniform accuracy
with a positive error has been obtained; all-time zero residual has not.

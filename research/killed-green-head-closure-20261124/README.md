# Killed Green-function localization of the global head obstruction

**Status: PROPOSED written mathematics, conditional on the explicitly pinned
pair-chain estimates for the probabilistic deductions and on M for the
full-conjecture reduction. Collatz remains OPEN.** This is an attempt at the
universal AYH/head-edge problem, not another scalar-carry exponent refinement.
It removes a whole near-balanced branch of the late head obstruction at a
summable cost. The high-level branch remains open.

## Sources and exact boundaries

Use the ordinary shortcut T(n)=n/2 for even n, (3n+1)/2 for odd n. The
ordinary convergence color f(n) is 1 if n reaches 1 and 0 otherwise. In
particular f(T(n))=f(n) and f(2n)=f(n). No assertion about deciding f is
needed for the selection of clocks below.

- **Pair-chain input P:** PR146, f431078244e868dc699fad011044f0d5e7f76437,
  research/upper-bit-mergers/THREE_RAY_UPPER.md. We use its exact physical
  transition table, all-state square-root tail, excursion offset bound,
  holding-time bound, and finite expected number of boundary excursions
  and boundary steps. These are existing written estimates; no independent
  full rederivation/Lean verification claimed here. The source itself
  credits Leen, Quantitative synchronization of Collatz trajectories
  (https://doi.org/10.5281/zenodo.23268755) and Duran
  (https://doi.org/10.5281/zenodo.23003524). Related work: Leen,
  Exact rates in Collatz synchronization
  (https://doi.org/10.5281/zenodo.23268751), Late synchronization and the
  geometry of Collatz families (https://doi.org/10.5281/zenodo.23268753),
  and rStation Paper 13 (https://rstation.ai/problems/collatz/papers/13)
  on selected conditional clocks. We do not claim historical priority for
  a killed-walk local estimate; our specific deduction is the ordinary
  head closure localization with its single common clock and exact
  original-source count.
- **Head input:** PR197 578e43911f49d41ef610b368a89b5a1ec269e134,
  research/ayh-resource-reset-20261124/literature-step/README.md;
  PR199 d868f8e8405c08b8c501236853bea495ca593824,
  research/optimal-critical-ancestors-20261124/FIRST_PASSAGE.md,
  section 1. We reconstruct its summability proof using color mismatches
  (a weaker sufficient condition than counting all distinct components).
- **M:** Lech Mazur, Positive Lower Density of Collatz Predecessors,
  6 September 2026, https://www.proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/.
  For each fixed positive target a with 3 not dividing a, its actual
  ordinary predecessor set has positive lower natural density.
  The primary release reports Lean verification; no independent rebuild
  is claimed. M is explicitly conditional in the closure theorem.
- Context refreshed: PR193 a1379492dbaae85e0d16662b41ccc7176ab3c66e;
  PR194 b1bf1f151a2da8936f80d229f132d0b7539ba42c (prior report);
  PR195 07aa5124f7ca482b6665d61355fac0af5f6e55b2;
  PR198 c76acf99ba3fb05e7cc07ca7db7e467954c2d950;
  PR200 c43fcbe6643c3d816975a4fb4328dc19dbdac6fb (LOCAL_BLOCKS and
  RATIO_PRESSURE). These contextual reads/metadata do not constitute
  blanket verification. The only inputs to the proof are P, and M for
  the all-source conclusion.

The general tool is the killed Green function, i.e. the expected
occupation before absorption. See, e.g., Lawler and Limic, Random Walk:
A Modern Introduction (https://www.math.uchicago.edu/~lawler/srwbook.pdf).
We do not import a heat-kernel theorem for the state-dependent physical
holding times. Instead, the classical one-dimensional visit count and
a killed offset-moment recursion suffice.

## 1. The physical pair state and the missing factor

Orient the two actual arms as X and Y=3^s X+D, s>=0, D integral.
The orientation is by affine coefficient, NOT necessarily by actual height.
Under independent fair exposed source bits (equivalently a full binary
residue block at a finite clock), P gives the table

 condition        bit 0                         bit 1
 D even           (s,D/2)                       (s,(3D+1-3^s)/2)
 D odd,s>0        (s+1,(3D+1)/2)                (s-1,(D-3^(s-1))/2)
 D odd,s=0        (1,(3D+1)/2)                  (1,(1-3D)/2), swap

The state (0,0) is absorbing; denote its first hit by tau.
For an actual source, absorption is an ordinary simultaneous meeting.
A particular integer can meet even without canonical absorption; this
only helps the upper bounds for permanent discordance.

Let Z_t=D_t/3^s_t, W_t=sqrt(|Z_t|), and set W=0 at the absorbing state.
All the normalized updates at a live state have multipliers 1/2 and
3/2 (possibly a fold with multipliers +1/2 and -1/2 at level zero), with
additive term bounded by 1 in absolute value. Therefore, conditionally on
the full past, at a live state,

    E(W_(t+1) | past) <= c W_t+1,   c=97/100<1.

Indeed sqrt(1/2)<=71/100, sqrt(3/2)<=123/100; use subadditivity of sqrt
and the two exact fair bits. At a folded level-zero row the coefficient
is smaller. Killing is harmless: if the next state is absorbing its
moment is zero. Crucially the additive term is ZERO on the absorbing
state, not one.

Define P_t=Pr(tau>t) and M_t=E[W_t 1_(tau>t)].
Then the exact killed recursion is

    M_(t+1) <= c M_t + P_t.                         (KG1)

P's existing all-state absorption estimate implies P_t<=A/sqrt(t+1)
for any bounded initial state, with A depending on that state.
For completeness the recursion yields a uniform bound
M_t<=M_0+1/(1-c), by replacing P_t by 1.
For t>=2 put n=floor(t/2), k=t-n. Iterate KG1, using
P_(n+i)<=P_n, to get

    M_t <= c^k M_n + P_n/(1-c)
        <= A'/sqrt(t+1).                            (KG2)

The exponentially decaying term is bounded by a constant times
(t+1)^(-1/2); the constants are uniform over any finite initial menu.
In particular the moment mass on the surviving population, not merely
the unconditional bounded moment, decays at the survival rate.

## 2. A Green estimate uniform in the initial level

Let V_K(s,D)=E_(s,D) sum_(t<tau) 1_(s_t<=K), K>=1. We claim

    V_K(s,D) <= C (K+1)^2 (1+sqrt(|D|/3^s)).         (KG3)

This differs from the full remaining-time bound (which is infinite in
mean). It is independent of the starting level s except via the
normalized offset.

For the first positive excursion until hitting level zero, the embedded
mixed-step level is fair nearest-neighbor walk killed at zero. Its
expected visits to level j>=1 from s>=1 are 2 min(s,j), by gambler's
ruin and geometric visits from j. P bounds the expected physical holding
time per visit (including the departure step) by e_j+2 with
e_j=v2(3^j-1). Thus the low-level occupation in this first excursion is
at most sum_(1<=j<=K) 2j(e_j+2)=O(K^2). To see the last bound directly,
e_j=1 for odd j and 2+v2(j) for even j, and
sum_(j<=K) v2(j)=sum_(a>=1) floor(K/2^a)<=K. This part does not use
the initial level as an upper bound and is valid at arbitrary s.

At its first return to level zero, P gives
E sqrt(|D_return|)<=0.99^s sqrt(|D|/3^s)+C.
Starting at a level-zero offset d, the boundary drift and finite
absorption trials in P bound the expected number of positive excursions
and the expected number of all other (boundary) physical steps by
C(1+sqrt(|d|)). Every ensuing positive excursion starts at level one
(or a bounded trial level), and its own expected low-level cost is
again bounded by O((K+1)^2), uniformly in its offset. The tower
property at the start of each excursion, with nonnegative sums, pays
this cost times the expected number of excursions. All level-zero
steps are included in the boundary-step budget. This proves KG3,
including s=0 and absorption. In particular no independence between
holding times, offsets, and level path is asserted.

## 3. A summable late balanced branch without a pointwise local limit

By the Markov property at physical time H, and Tonelli,

    sum_(t>=H) Pr(tau>t, s_t<=K)
      = E[1_(tau>H) V_K(s_H,D_H)]
      <= C(K+1)^2(P_H+M_H)
      <= C'(K+1)^2 / sqrt(H+1).                     (KG4)

All laws above are on the same pair chain with its original initial
state. This is an integrated killed Green bound, not an independent
walk replacement and not a pointwise-in-t heat-kernel assertion.
It implies, on the late interval of H physical clocks [H,2H),

    (1/H) sum_(H<=t<2H) Pr(tau>t, s_t<=K)
       <= C''(K+1)^2 / H^(3/2).                    (KG5)

Thus if K=floor(H^epsilon), for any fixed 0<epsilon<1/4, this averaged
balanced failure count is summable along H comparable to the head-scale
index. In particular epsilon=1/8 gives H^(-5/4).

Two companion exclusions at the selected clock will also be summable.
The signed level S, before folding, is a martingale with increments
in {-1,0,1}: when the parities differ the two signed increments are
opposites with equal probability, and otherwise the increment is zero.
After canonical absorption continue it as zero. If the initial signed
level is 4, the conditional exponential bound
E(exp(lambda Delta S)|past)<=exp(lambda^2/2) follows from
cosh(lambda)<=exp(lambda^2/2); iteration and exponential Markov give
Pr(|S_t-4|>=u)<=2exp(-u^2/(2t)).
For H<=t<2H, taking u=sqrt(12H log H) gives <=2 H^(-3).
Also KG2 and Markov give

    Pr(tau>t, |Z_t|>H^4) <= C H^(-5/2).             (KG6)

These statements retain the killed event. Using only a uniform
unconditional moment would miss the factor H^(-1/2).

## 4. Exact ordinary transfer, one clock for the entire head scale

Set R_j=81^j, X_j=81^(j-1), and let the head children be
x=81 y+r with 7X_j<=y<8X_j integral, 0<=r<81. The parent is y.
Every possible x in [7R_j,8R_j) occurs exactly once.
Use H_j=floor(log_2(X_j)/3) for j>=2 (discard finitely many small
scales) and K_j=floor(H_j^(1/8)).
For each r the initial pair state is (4,r). Its exact finite bit words
through any t<2H_j are represented bijectively by y modulo 2^t:
refinement of the original residue gives an odd coefficient at the
current oriented base, so either next parity selects one of the two
lifts. This is the literal finite parity-cylinder argument in P.
For every event E depending on this finite history, the actual number
of y in the specified interval is bounded by

    ceil(X_j/2^t) * #E <= 2 X_j Pr(E),              (KG7)

since 2^t<=X_j^(2/3)<=X_j. There is no tail resampling after the native
binary horizon, no source switch, and no averaging over endpoint
heights. The 81 initial states form a fixed finite menu.

Sum (KG5) over r. Select ONE clock t_j in [H_j,2H_j) minimizing the
sum over all r of the finite-history probabilities of surviving at
s<=K_j. It can be chosen by finite enumeration, before any information
about convergence colors, and does not depend on an individual source.
By KG5 and KG7,

    # {head x : tau(x)>t_j, s_(t_j)(x)<=K_j}
          <= C R_j H_j^(-5/4).                     (KG8)

Here tau is the canonical profile absorption clock along the actual
source's finite history. This is a finite count of original head
children, not an assertion about Haar-almost-every positive integer.
KG6 and the signed martingale bound, via KG7 at that SAME t_j, discard
another O(R_j(H_j^(-5/2)+H_j^(-3))) sources.

Define GOODPROFILE_j by the three tests at t_j:

    K_j < s <= 4+ceil(sqrt(12 H_j log H_j)),
    |D|/3^s <= H_j^4,
    tau>t_j.

Every original head edge with different actual convergence colors
that fails these tests belongs to a set of size O(R_j H_j^(-5/4)).
In particular their normalized counts sum to a finite number over j.

All remaining discordant profiles have the exact physical form

    Y = 3^s (X+z), |z|<=H_j^4,                     (KG9)

where X,Y are ACTUAL common-clock iterates of y,x in one of the two
orientations; the signed level is 4+p_x(t_j)-p_y(t_j).
Both original arms are >=7X_j, every shortcut step is at least a
halving, and 2^t_j<=X_j^(2/3). Hence X>=7X_j^(1/3).
For all sufficiently large j,

    |Y/(3^s X)-1| <= H_j^4/(7 X_j^(1/3)),
    Y/X >= (1/2) 3^s > (1/2) 3^K_j.                (KG10)

Thus the surviving branch is not just a large affine offset: it has
exponentially separated actual heights, a mesoscopic signed odd-count
imbalance, and exponentially accurate relative power-of-three alignment.
This is a source-preserving reduction of the global problem. It
covers finite-clock and permanent color-discordance counts with the
stated quantifiers, but does NOT estimate the number of discordant
edges inside GOODPROFILE_j.

## 5. Closure theorem (conditional on M and P)

Let E_j be the number of head children satisfying GOODPROFILE_j whose
actual convergence color differs from the parent's color.
Then

    Collatz  <=>  sum_(j>=2) E_j/R_j < infinity.     (KG11)

Necessity is immediate. For sufficiency let D_j be the total number of
different-color head edges. The removed branch is summable by KG8 and
KG6, so sum D_j/R_j<infinity.

We reconstruct the necessary head argument (PR199 credits PR197 and
PR146). Define F_j(u)=f(floor(R_j u)) on I=[7,8).
Then ||F_j-F_(j-1)||_1 = D_j/R_j, by exact integer truncation.
The summability makes F_j converge in L1 to a binary g (binary
functions form a closed subset of L1). For k>=0, integer l, and
a=2^k/81^l, on I intersect a^(-1)I restrict to subcells
{R_j u}<2^(-k). There

    F_(j+l)(a u)=f(2^k floor(R_j u))=F_j(u).

The indicators of the subcells converge weakly against any fixed
integrable function to 2^(-k), by averaging first on interval step
functions then using L1 approximation. Use L1 convergence of the two
F's (and change of variables on the rescaled interval) to obtain
g(a u)=g(u) almost everywhere on their common domain. There are
countably many such k,l. On log-base-81 coordinates, this states
invariance under all forward returns of irrational rotation by
log_81 2 to the arc corresponding to I. Irrational rotation is
ergodic: if both colors in the arc had positive measure, the union of
forward translates of one would be conull but would intersect the
other in measure zero. Hence g is constant.

The minority color therefore occupies o(R_j) starts in every head
interval. Every positive integer sufficiently large has a dyadic
multiple in a head interval with a bounded exponent: the backward
translates of the open log arc by the irrational rotation cover the
circle, and compactness gives a finite subcover. Such dyadic lifting
preserves f, multiplies height by a bounded factor, and has bounded
multiplicity. Summing geometric head scales gives upper natural
density zero of the minority color on all positive integers.

Under M, if any source fails to converge, select an actual odd unit
on that orbit (strip twos and take one odd transition). Its predecessor
set has positive lower natural density, as does the predecessor set
of one. Their colors differ. This contradicts the zero-density
minority. The argument covers both nontrivial cycles and escaping
orbits.

## 6. Attack on the remaining high-level branch

The necessary next estimate is NOT another same-clock tail bound.
By the mixed-step walk, a large level of order sqrt(H_j) can persist
until the native binary horizon. A generic fresh-bit argument beyond
that horizon is invalid. Equations KG9-KG10 isolate the precise
ordinary states whose colors must be compared, with their original
multiplicities and common clock.

A natural continuation is to use the post-descent transfer of PR197
and the near-power ternary structure of KG9 to show summable
discordance for these large-level pairs. There is an immediate
obstruction to one tempting deterministic shortcut: on any infinite
affine source cylinder, equality of two forward endpoints with
different clocks requires equality of their coefficients
3^p/2^t. For the two original slopes in ratio 3^s, unique factorization
forces equal shortcut clocks and the corresponding odd-count
compensation. Merely granting asynchronous clocks does not yield
a uniform affine merger while the level is high. A source-specific
integer correction or a genuinely joint actual first-passage theorem
is needed. The recently reported one-arm fixed-barrier bound does not
control the joint mismatch in KG11.

No assertion is made that KG11's last sum converges. Nor is there a
claim that all high-level pairs fail. This packet proves that, at the
chosen physical clock, the other entire branch can be removed from
the universal density argument at a summable cost. The Green-function
method is intended to organize a full proof that handles cycles and
escape together, not to replace the ordinary source by a random orbit.

## 7. Verification

controls.js was executed via the JavaScript runtime in this session.
It enumerates all 81 initial residues and all 2^10 low-source lifts;
checks exact literal pair profiles, odd counts, normalized update
bounds, absorbing transitions and binary word bijections. It also
verifies the rational contraction certificate. See CONTROLS.json.
The written asymptotic estimates are not certified by these finite
checks.

KilledMoment.lean is an admission-free textual candidate for the
rational contraction certificate and finite killed-moment recursion.
**Lean/Lake are unavailable in this session; no compilation or axiom
audit is claimed.** The separate probability, Green, head-transfer,
and ergodicity arguments are written proofs with the named dependencies.
No full checkout validation or independent subagent review was
performed. The draft is a mathematical checkpoint pending review.


## Continuation: exact grade spreading and branching phase sparsity

See [continuation/README.md](continuation/README.md). This checkpoint proves an exact full-octave odd-grade TV shift bound and the aggregate maximum-fiber bound O(1/sqrt(log X)), retaining both actual roots and signed clock differences. It also gives the native-clock bound O(L X^0.71) for arbitrary finite canonical phase sets, with no injectivity or forward-invariance premise, and a triadic-denominator depth restriction on rational-scalar ancestors. Written proposed mathematics; additional exact controls executed; Lean candidate uncompiled. Neither result closes the two-class discordance or all ordinary sources.

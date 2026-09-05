# Route 1 continuation — orbitwise Mellin budgets, without a fiber loss

**Status: PROPOSED pending independent mathematical review.** This is a
self-contained quantitative rederivation in the orbit-sparsity tradition of
Garcia–Tal (1999), followed by project-specific consequences. Reciprocal
summability and coefficient-surplus escape were already explicitly discussed
in a July 2026 public reference request; they are not claimed as discoveries
of this pass. See [SOURCES_AND_REVIEW.md](SOURCES_AND_REVIEW.md).

The forward/inverse program needs to distinguish a basin, whose many sources
can merge, from a single injective orbit. This note obtains a uniform Mellin
budget for the latter. It does **not** prove the PR #92 all-source survivor-bias
ceiling or replace a basin by its sparse minima.

## 1. T-A3-401 — a uniform explicit power bound

Use the shortcut T and the odd map

    U(n)=(3n+1)/2^v2(3n+1), n positive odd.

Let S be a set of positive odd integers such that U^q restricted to S is
injective for every q>=1. No invariance assumption is needed in this section.
Then, for all real X>=1,

    N_S(X) := #(S intersect [1,X]) <= 4 X^(39/40).             (1)

This applies to the odd states of an infinite positive orbit, or to the
distinct odd states of a positive cycle. It does not apply automatically to
an inverse basin or a converging preperiod: equal-time merging violates the
hypothesis.

### Exact cylinders and the affine remainder

For a fixed valuation word (a_1,...,a_q), a_i>=1, put A=sum a_i. Write

    U^q(n)=(3^q n+B)/2^A.

The word selects exactly one odd residue modulo 2^(A+1), not 2^A. One proof is
to prescribe the shortcut word 1 0^(a_1-1) ... 1 0^(a_q-1), followed by an odd
endpoint bit. Equivalently, the unique residue is

    n = (2^A-B) (3^q)^(-1) mod 2^(A+1).

The appended odd bit enforces each valuation exactly. At a fixed total A there
are binomial(A-1,q-1) such words. Direct iteration of U gives

    0 < B/2^A <= (3/2)^q-1,                                (2)

because each remaining valuation is at least one; the all-one word attains
the upper bound. Thus no affine correction is silently discarded.

### Low total valuation versus compressed distinct endpoints

For q>=1 choose m=floor(5q/3), with 2^m<=X. In the lane A<=m, each cylinder
contains at most X/2^(A+1)+1 <= (3/2)X 2^(-A) sources. Put z=4/5. The exact
geometric generating function gives

    sum_(A<=m) binomial(A-1,q-1) 2^(-A)
      <= z^(-m) (z/(2-z))^q <= rho^q,
    rho^3=3125/3456 < 1.                                   (3)

In the other lane, A>=m+1>5q/3. Equation (2) puts every endpoint below

    sigma^q X+(3/2)^q-1,  sigma=3/2^(5/3), sigma^3=27/32.

Those endpoints are distinct by the hypothesis. Counting odd endpoints in
this interval gives at most [sigma^q X+(3/2)^q]/2. Since sigma<rho, the two
lanes together satisfy

    N_S(X) <= 2X rho^q + (1/2)(3/2)^q.                     (4)

This is the no-fiber-loss step. No equidistribution at the endpoints is used.

### Explicit constants

Take q=floor((3/5)log_2 X). Then 2^m<=X and

    8*3125^24 < 3456^24

proves rho<2^(-1/24). Also rho>2/3. Hence

    2X rho^q < 3 X^(39/40),
    (1/2)(3/2)^q <= (1/2)X^(3/5) <= (1/2)X^(39/40).

This proves (1) when q>=1, with room in the constant 4. For q=0, use N_S(X)<=X
and X<2^(5/3); (1) follows immediately. All constants are independent of S.

## 2. T-A3-402 — forward invariance pays for repeated scale compression

If in addition U(S) is contained in S, then

    N_S(X)=O(X^(19/20)),                                   (5)

with a constant independent of S. More generally the same argument gives
O_beta(X^beta) for every beta>h_2(log 2/log 3). The explicit version below is
sufficient here; it does not claim that 19/20 is optimal.

Use t=317/200, q=floor(log_2(X)/t), and m=floor(tq). The low-A part is at most
(3/2)X rho_*^q, where

    rho_*=(317/234)^(317/200) (117/200).

Two exact integer inequalities certify the needed strict margins:

    3^200 < 2^317,
    317^6340 < 2^6023 * 117^2340 * 200^4000.                (6)

The second is equivalent to rho_*<2^(-317/4000). Thus the low-A term is
O(X^beta_0) for some beta_0<19/20. For high A the endpoint bound is

    Y <= K X^u,
    u=(log_2 3)/t < 1,

for one constant K: the main term is 3^q X/2^(m+1), and the remainder has
smaller exponent log_2(3/2)/t. The endpoints remain distinct and now lie in S.
Consequently

    N_S(X) <= C X^beta_0 + N_S(K X^u).                     (7)

For sufficiently large X, K X^u<X. Strong induction on floor(X), increasing
the common constant over a fixed finite initial range, proves (5): the
recursive exponent is u*(19/20)<19/20 and the additive exponent is also
strictly smaller. The initial estimate N_S(X)<=X is uniform in S.

For the general statement take t just above log_2 3 and the optimized
z=2(t-1)/t. The limiting low-lane exponent is h_2(1/t), tending to
h_2(log 2/log 3). This is a parameter consequence of the same proof, not an
assumption of independence beyond the native parity horizon.

The distinction from the PR #88 basin recurrence is decisive: a single orbit
has no endpoint multiplicity in (7). A general exceptional basin does, so (7)
cannot be transplanted into the all-source fixed-floor problem.

## 3. T-A3-403 — a uniform Mellin budget above the orbit minimum

Suppose S is as in Section 1 and every member is at least m>=1. For s>39/40,
nonnegative integration of x^(-s)=s integral_x^infinity t^(-s-1)dt and (1) give

    sum_(x in S) x^(-s)
       <= [4s/(s-39/40)] m^(39/40-s).                     (8)

In particular

    sum_(x in S) 1/x <= 160 m^(-1/40).                    (9)

For forward-invariant S, (5) also gives O(m^(-1/20)) in (9), with a uniform
but non-explicit constant. We retain 160 m^(-1/40) when explicit constants
matter.

Every shortcut state is a power of two times a later odd state. Therefore the
number of distinct states of one infinite positive shortcut orbit, or one
positive cycle, below X is at most

    4 X^(39/40)/(1-2^(-39/40)) < 10 X^(39/40).             (10)

For the last inequality, 39/40>3/4 and 2^3>(5/3)^4 imply
2^(-39/40)<3/5. This counting does not assert that arbitrary inverse powers of
two belong to the orbit; it only uses them as a covering upper bound.

## 4. Bounded correction product and full coefficient escape

For an infinite positive shortcut orbit x_k=T^k(n), put

    C_k=3^(q_k)/2^k,
    P_k=product_(i<k, x_i odd) (1+1/(3x_i)).

The exact product formula is x_k=n C_k P_k. Infinite positive orbits are
injective: a repeated state would make the orbit eventually periodic. They
also tend to infinity, since each finite set is visited only finitely often.
Let m be the attained minimum of the orbit. Applying (9) to its odd states,

    1 <= P_k <= P_infinity <= exp((160/3)m^(-1/40)).        (11)

Consequently

    C_k -> infinity.                                     (12)

This is full escape, not merely an unbounded subsequence or density-one
escape. The literature discovery noted at the top already states this
consequence in qualitative form; the explicit estimate and its project
crosswalk are supplied here without importing an uninspected source proof.

Equation (10) gives two useful refinements. If a band C_k<=R contains k's,
all their distinct states are <=n P_infinity R, so

    #{k:C_k<=R} <= 10 (n P_infinity R)^(39/40).            (13)

This bound is independent of the observation horizon. Sorting the first K
states and using (10), then log(K!)>=K log K-K, gives

    mean_(k<K) log_3 C_k >= (40/39)log_3 K-O_n(1).        (14)

Equation (5) improves the coefficient 40/39 to 20/19 with unspecified uniform
constants. These are necessary constraints on a hypothetical orbit, not its
exclusion. A vanishing rate log(C_k)/k along a subsequence is compatible with
(11)-(14).

For a finite positive odd cycle with minimum m, use one period in (11):

    0 < A log 2-q log 3 <= (160/3)m^(-1/40).              (15)

It is independent of the period length but does not rule out all cycles.

## 5. A weaker all-source bias target retained, not proved

For the original H=64, s=3/2 survivor masses M_k,Q_k in ../ROUTE1_MELLIN.md,
it suffices that Q_k/M_k<=69/200 along an unbounded sequence of times; an
all-time or eventually-all-time ceiling is not necessary.

Indeed dominated convergence gives M_k down to M_E and Q_k down to Q_E.
If an exceptional source exists, M_E>0. Every exceptional endpoint exceeds 64,
and its odd predecessor is also exceptional and exceeds 64, so every eligible
residue-2 endpoint is at least 98. The invariant inverse identity gives

    Q_E/M_E >= (1-2^(-3/2))/(98/65)^(3/2) > 69/200.       (16)

The final strict inequality follows from the parent certificate
2^(-3/2)+(98/65)^(3/2)*(69/200)<993/1000<1. Therefore the ratio converges to a
value above the proposed ceiling if a counterexample exists, contradicting
the cofinal-sequence hypothesis. The core [1,64] is checked again by both new
implementations; its maximum shortcut hitting time is 71, at 54 and 55.

This weakening is conditional. No unbounded sequence of certified times, no
uniform basin Mellin bound, and no Collatz proof is obtained here. The new
orbitwise budget cannot supply (16)'s contradictory upper bound by itself.

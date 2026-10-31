# A uniform pressure profile and its ordinary-orbit boundary

**PROPOSED; self-audited only.** This constructs an actual moving-endpoint
budget and classifies the limits of one explicitly defined function. It does
not prove its required vanishing, nor exclude nontrivial positive cycles.
Only positive ordinary 3x+1 trajectories are used.

Notation and the uniform first-hit discount are in [PRESSURE_BRIDGE.md](PRESSURE_BRIDGE.md).
For positive odd t and odd x define

    v_t(x)=J_0(x,t)/t if x first hits t, and 0 otherwise,
    F(t)=H_2(t)/t^2=sum_(odd x) v_t(x)^2.

Thus v_t is a vector in l^2 of the positive odd integers, with

    0<=v_t(x)<=1/x,  0<F(t)<5/4.                     (1)

The elementary upper bound uses
sum_(odd x) x^-2=pi^2/8<5/4; its rational telescoping proof is sufficient.
F uses FIRST-HIT pressure, not G_2 with repeated cycles.

## Q1. One finite bank encloses F at every positive odd target

Suppose every odd source x<=X, with X odd, has its complete eventual orbit
classified by a literal path to a repeated state. For each target appearing
on those paths, record the exact derivative at its first visit. Define the
finite-support rational function

    A_X(t)=sum_(odd x<=X first hitting t) (J_0(x,t)/t)^2.

Then the following is an INFINITE-DOMAIN assertion, not a finite target grid:

    0<=F(t)-A_X(t)<1/[2(X+1)] for EVERY positive odd t. (2)

Indeed every missing coordinate is at most 1/x; sum the odd reciprocal-square
tail using 1/x^2<(1/2)(1/(x-1)-1/(x+1)). A literal eventual cycle determines
all targets visited by each classified source and all its first hits. No
trajectory statement is required for any x>X.

The executed bank has X=65535: all 32,768 odd sources reach 1. Its sparse
support contains exactly 52,063 odd targets, the largest 197,759,717. Hence

    F(t)<1/131072 for every positive odd t>197759717.  (3)

The full table contains [target,numerator,denominator] for the UNNORMALIZED
partial H_2. Divide that rational number by target^2 to obtain A_X. Its
exact byte hash and reconstruction commands are in the receipt. A separate
implementation reconstructs all entries using raw shortcut clocks.

Statement (3) is a genuine uniform tail certificate at one accuracy. It is
not a theorem that F tends to zero: achieving arbitrarily small errors by
this finite-bank method requires completion of arbitrarily large source
banks, which is precisely not supplied.

## Q2. The boundary vector of a non-eventually-periodic component

An odd merger component consists of sources whose forward orbits eventually
meet, with arbitrary separate clocks. A component containing a non-eventually-
periodic orbit contains only such orbits. They are injective and tend to
infinity as ordinary integers.

For x in such a component C, define the infinite ordinary discount

    r(x)=product_(j>=0) 3U^j(x)/(3U^j(x)+1).

The credited finite-simple-path bound, applied to every prefix and then
monotone limits, gives

    2^(-100)<=r(x)<=1.

Set w_C(x)=r(x)/x for x in C, and zero otherwise. For ANY n in C,
with t_j=U^j(n),

    v_(t_j) -> w_C in l^2,
    F(t_j) -> Lambda_C:=sum_(x in C) (r(x)/x)^2>0.    (4)

Proof: x outside C never hits t_j. For x in C, sufficiently late t_j are
on its forward tail. Dividing (2) of the bridge by t_j gives
v_(t_j)(x)=x^-1 times the finite discount along x's first-hit path. As j
increases this tends to r(x)/x. The coordinate bound 1/x in (1) supplies a
summable square envelope, proving l^2 convergence by dominated convergence.
In particular

    2^(-200)sum_(x in C)x^-2 <= Lambda_C
                                  <=sum_(x in C)x^-2. (5)

This keeps ONE ordinary component; changing finite compatible roots does not
supply (4). The limit may be extremely small, but it is strictly positive.

## Q3. Complete classification of the cluster set at ordinary infinity

As t ranges over positive odd integers tending to infinity, the l^2 cluster
set of v_t is EXACTLY

    {0} union {w_C : C is a nonperiodic merger component}. (6)

Consequently the scalar cluster set of F(t) is exactly

    {0} union {Lambda_C : C is a nonperiodic component}. (7)

Proof: the coordinate box 0<=z(x)<=1/x is compact in l^2: its coordinatewise
compactness combines with a uniform square-summable tail. Take a nonzero
vector cluster limit w. Some fixed coordinate x has w(x)>0. Eventually along
that convergent subsequence, x hits every corresponding target t. Those
unbounded targets lie on the forward orbit of this ONE fixed x. Therefore
x is nonperiodic, their first-hit clocks tend to infinity, and the same
coordinate/dominated-convergence argument as in Q2 gives w=w_C. Conversely
Q2 realizes every listed w_C. Zero is realized by odd multiples of three
 tending to infinity: they have no odd predecessors, so v_t=e_t/t.
Continuity of squared norm and compactness give exactly (7).

The components have disjoint supports, so

    sum_C Lambda_C <= sum_(odd x)x^-2 < 5/4.         (8)

In particular at most floor(5/(4 epsilon)) components can have mass at least
epsilon>0. Distinct component masses can coincide; that does not invalidate
the counting bound. Among infinitely many distinct components their masses
can accumulate only at zero. These are necessary structures, not exclusions.

## Q4. An exact vanishing criterion, with the cycle exception retained

    F(t)->0 as t->infinity through odd integers
        IFF every positive orbit is eventually periodic. (9)

If F tends to zero, Q2 excludes every nonperiodic component. Conversely, if
every source has a finite forward value set, each fixed coordinate v_t(x)
is eventually zero as t tends to infinity. Equation (1) and dominated
convergence imply F(t)->0. Even sources reduce to odd ones, so the statement
covers all positive inputs.

This is an analytic characterization of UNIVERSAL EVENTUAL PERIODICITY, not
of convergence to 1. Any nontrivial positive cycles remain allowed on the
right side. The proof neither establishes the left side nor rules out such
cycles. It supplies a precise, 3x+1-specific decay target built from finite
ordinary histories. The finite certificate (3) is only one error level.

## Q5. A correctly transported monotone budget

Fix a nonperiodic odd source n, set t_j=U^j(n) and
D_j=3^j/2^(a(n)+...+a(U^(j-1)(n))). For s>1 put

    K_j=H_s(t_j)/D_j^s.

Then K_j is nondecreasing and

    K_j <= (2^100 n)^s (1-2^-s) zeta(s).             (10)

Indeed B_(t_j) is nested. For a source already present, its first-hit path
to t_(j+1) is its old first hit followed by the next ordinary step, so
J_0(x,t_j)/D_j stays constant. New sources contribute nonnegative weights;
no original clock is reset. Also t_j/D_j=n P(n,t_j)<2^100 n, and the
first-hit upper bound gives (10). The increment is exactly the sum over
the newly admitted, disjoint source cohort. Thus this is an all-time bound
for MOVING endpoints, unlike the fixed-target statement in pass 2.

In fact the eventual weight of x in the component is

    ell_n(x)=n r(x)/(x r(n)),

so the exact limit is sum_(x in C) ell_n(x)^s. This agrees with Q2 at s=2.
An infinite number of positive increments is compatible with a bounded
monotone sequence; (10) is not a well-founded termination rank.

The finite experiment tests this ledger up to the first 1, on six actual
orbits, against a fixed bank of all odd sources through 4095. It checks 296
ledger entries and 12,288 source-cohort memberships. It does NOT simulate an
infinite divergent trajectory. It retains two controls:
- The finite-bank approximation A_4095(t_j) need not be monotone, already
  along source 27 (a decrease at target 233). This finite-bank comparison
  alone is NOT asserted to certify a decrease of the full F(t_j).
- At the fixed cycle 1, source 1 alone contributes 16/7 to G_2(1), and
  D_j=(3/4)^j. Even this single-source contribution, divided by D_j^2, is
  unbounded. The total G_2(1) is larger (approximately 2.6851), not 16/7.
  One cannot substitute all-history pressure into (10) after periodic
  repetitions, or drop the nonperiodic premise.

## First unsupported inference

No uniform decay theorem for F, no quantitative exclusion of the nonzero
boundary vectors w_C, and no connection forcing the parent occupation
collision exponent below 1/20 has been proved. A possible useful next step
is a new inequality forcing F(t) to vanish at ordinary infinity, rather than
another pointwise upper bound proportional to t^2. Any proposed such argument
must distinguish first hits from cycles and survive the exact cluster-set
test above. The separate problem of nontrivial cycle exclusion remains.

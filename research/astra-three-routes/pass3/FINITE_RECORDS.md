# Route 2: finite-path distortion and an effective local SC certificate

**Status:** T-A3-651--653 are **PROPOSED pending independent review**.
SC* and cycle exclusion remain OPEN.
The improvement over pass 2 is a finite stopping-or-repetition bound once a
finite, near-source coefficient-stopping window has been certified. No unknown
infinite orbit is assumed while deriving that finite implication.

## 1. T-A3-651: a uniform budget for every finite simple path

Let x_0,...,x_L be distinct consecutive shortcut-Collatz states and let S be
the odd states in this finite segment. For every X>=1,

    #(S intersect [1,X]) <= 5 X^(39/40).                 (1)

If every state of the segment is at least m>=1, then

    sum_(x in S) 1/x <= 200 m^(-1/40).                  (2)

The constant is independent of L, the source, and the maximum height. In
particular a huge excursion cannot create an unbudgeted affine correction
before a later return, as long as the inspected segment has no repetitions.

### Proof, including the terminal-boundary correction

List the distinct odd states in their time order. Apart from the last q of
these, q steps of the odd map U are still inside this list, and their endpoints
are distinct. Discarding the last q costs at most q sources. The proof of
pass2/ORBIT_MELLIN.md, Section 1, now applies to the rest. To make its exact
inputs explicit, a valuation word of length q and total valuation A specifies
one residue modulo 2^(A+1) and has affine remainder at most (3/2)^q-1.

Set q=floor((3/5)log_2 X), m_0=floor(5q/3),

    rho^3=3125/3456, sigma^3=27/32<rho^3.

For z=4/5 the geometric composition generating function gives

    sum_(A<=m_0) binom(A-1,q-1)2^(-A)
      <=z^(-m_0)(z/(2-z))^q<=rho^q.

Since 2^m_0<=X, each such cylinder has at most
X/2^(A+1)+1<=(3/2)X 2^(-A) representatives. Thus low A<=m_0 supplies at
most (3/2)X rho^q sources. High A has distinct
endpoints below sigma^q X+(3/2)^q-1 and hence at most
[sigma^q X+(3/2)^q]/2 odd endpoints. Thus

    #(S intersect [1,X]) <= 2X rho^q+(1/2)(3/2)^q+q.      (3)

The exact inequality 8*3125^24<3456^24 gives rho<2^(-1/24), and rho>2/3.
The first term is <3X^(39/40), the second <=(1/2)X^(39/40).
Also log_2 X<2 sqrt(X) for X>=1, so q<(6/5)X^(39/40).
For completeness, maximizing (log X)/sqrt(X) gives 2/e; e log 2>1 follows
already from e>2 and log 2>1/2. This proves the displayed logarithm bound.
The sum is <5X^(39/40). If q=0, use the trivial count <=X and
X<2^(5/3). If the path has fewer than q odd states, its count <=q alone
suffices. This covers every terminal and small-range case.

Nonnegative integration of 1/x=integral_x^infinity t^(-2)dt proves (2).
The invariant-set refinement in pass 2 likewise extends to finite paths by
adding q=O(log X) to its recurrence: high-A endpoints are inside the original
finite path after its final q states are discarded. Consequently there are
uniform, but unspecified, constants for

    #(S intersect [1,X])=O(X^(19/20)),
    sum_(x in S, x>=m)1/x=O(m^(-1/20)).                 (4)

This is a finite-path extension of the prior orbit-sparsity argument, not a
new priority claim for orbit sparsity or reciprocal summability. A repeated
cycle may NOT be counted with multiplicity in (1)-(4).

## 2. T-A3-652: only a short ordinary window can contain coefficient records

Suppose the finite simple segment starts at n and has x_i>=n for every i.
Let C_i=3^(q_i)/2^i, C_0=1, and

    P_i=product_(t<i, x_t odd)(1+1/(3x_t)).

The exact identity x_i=n C_i P_i and (2) give

    1<=P_i<=exp(K n^(-1/40)), K=200/3.                  (5)

Define the following fixed finite integer window and its cardinality:

    B(n)=floor(n exp(K n^(-1/40))),
    W(n)={n,n+1,...,B(n)}, R(n)=B(n)-n+1.               (6)

Every new strict record minimum of C_i has C_i<=1 and its ordinary source
x_i lies in W(n). All record-source values are distinct. Therefore there are
at most R(n) coefficient records, counting i=0. For sufficiently large n,

    R(n)<= (400/3)n^(39/40)+1,

because exp(u)-1<=2u on 0<=u<=1. The non-explicit refinement (4) gives an
alternative window of width O(n^(19/20)). The explicit threshold
n>=(200/3)^40 is enormous and is not advertised as a practical cutoff.

This statement concerns all finite simple no-descent paths, not only the
hypothetical infinite paths in the earlier source-location result.

## 3. T-A3-653: a finite local stopping-or-repetition theorem

Assume a finite certificate proves

    tau_c(y)<=N for every integer y in W(n),             (7)

where tau_c is first coefficient-subcritical time and N>=1. Then from n,
within R(n)*N shortcut steps, at least one of the following occurs:

    an iterate is less than n;
    a state repeats.                                    (8)

An integer upper bound on B(n) can replace the exact floor in (6), enlarging
R(n). This avoids requiring transcendental comparison at equality in an
implementation. Finite all-source coefficient certificates may therefore be
used with outward rational bounds.

### Proof

Suppose all states through time R(n)N are distinct and >=n. Start at the record
C_0=1. From each record source y, (7) supplies a first crossing relative to
that coefficient in <=N steps. Until that crossing, the coefficient remains
at least its current record; at the crossing it is smaller than that record
and all earlier coefficients. Thus it is the next strict global record.
After R(n) such events, by time R(n)N, there are R(n)+1 distinct record
sources in W(n). This contradicts the cardinality bound in Section 2.

A related unconditional finite extraction: the successive record intervals
partition any simple no-descent segment of length L into at most R(n)
intervals. One has length >=ceil(L/R(n)); its proper prefix is
coefficient-supercritical from an ordinary source in W(n). Hence there is
such a realized prefix of length at least ceil(L/R(n))-1. The minus one is
necessary because the interval's last step may create the next record.

### What has improved, and what has not

Pass 2 located an actual SC-infinite source near a minimum but gave no time to
reach it. The new result does NOT assert such an unconditional time bound.
It says exactly what finite input is sufficient: coefficient-stopping
certificates for one short ordinary window give the explicit time R(n)N to
descent or repetition. If no nontrivial cycles exist, the repetition case is
also convergent. SC* makes (7) exist for each fixed n, but SC* is not proved.

The window certificate may be supplied by m_N>B(n), but that is stronger than
(7): it checks all positive sources below B(n), not merely W(n). This local
window distinction must not be reversed into an equivalence.

The record list also describes a legitimate unbounded-memory termination
architecture: store the finite set of record sources already seen in W(n).
Every completed coefficient-stop block consumes an unused record source or
reveals descent/repetition. This finite-set rank is constructive CONDITIONAL
on block totality (7). Searching indefinitely for an unproved next crossing
is not a total algorithm or a global Collatz certificate.

## 4. Finite tests and adversarial cases

The checker reconstructs many complete simple prefixes, truncations, and
no-descent subsegments. It verifies the exact correction product, record
sources in [n,floor(n P_L)], and the record-interval extraction with its
endpoint correction. It checks the finite record-interval interfaces by literal stepping. It does
not instantiate the enormous universal window (6). These are finite interface
tests, not empirical proofs of (1), (7), or SC*.

The positive rational 61/295 tail from pass 2 is not covered: this proof uses
distinct positive INTEGER values to count the record window. Repeating an
ordinary cycle without stopping at first repetition is also outside the
simple-segment premise. Both boundaries are essential, not optional filters.

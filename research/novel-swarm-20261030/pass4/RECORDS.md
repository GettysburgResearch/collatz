# Packing coefficient records: a squared-exponent finite reduction

**PROPOSED; self-audited.** This strengthens the record *count* in the
repository's finite-record reduction. It does not prove universal coefficient
stopping. Raw shortcut clocks are used throughout; cycles are retained as
an explicit exit.

## R4-1. The general packing-to-record transfer

Suppose every finite simple trajectory has at most B K^beta states in every
translated interval of K integers, where B>=1 and 0<beta<1. Let
x_0=n,...,x_L be a finite simple segment with every x_i>=n. Write

    C_i=3^(q_i)/2^i,
    P_i=product_(j<i, x_j odd)(1+1/(3x_j)),
    x_i=n C_i P_i.

The translated packing theorem, used first at the origin, implies

    sum_(x in segment)1/x <= B/(1-beta)n^(beta-1),
    1<=P_i<=exp(b n^(beta-1)), b=B/[3(1-beta)].       (1)

Define the fixed integer window

    W_n=[n,floor(n exp(b n^(beta-1)))],
    w_n=|W_n|.                                      (2)

Every strict new minimum of C_i, including C_0=1, has C_i<=1 and hence has
its ACTUAL ordinary source x_i in W_n. These sources are distinct. The
second, translated use of the packing theorem therefore yields

    number of coefficient records <= B w_n^beta.   (3)

Using w_n=O(n^beta), this is O(n^(beta^2)), not just O(n^beta).
The source set of records need not be forward invariant: it is a subset
of the one finite simple trajectory to which the packing theorem applies.
No recursive application of (3) to an invented record dynamics is allowed.
In particular this argument does NOT give beta^3, beta^4, or an all-source
survivor-density exponent.

For a checked finite path, its exact rational P_L can replace the upper
bound in (1), giving the smaller window [n,floor(nP_L)]. This is a valid
certificate for that inspected path, not a horizon-independent replacement
for (2).

## R4-2. Explicit Collatz specialization

W2 supplies B=16 and beta=19/20. Thus b=320/3. For all n,

    number of records <=16 w_n^(19/20),
    w_n=floor(n exp((320/3)n^(-1/20)))-n+1.          (4)

If n>=(320/3)^20, use exp(u)-1<=2u for 0<=u<=1 to get
w_n<=216 n^(19/20). Consequently

    number of records <3456 n^(361/400).           (5)

The exponent is 361/400=0.9025. It counts coefficient records of ONE actual
simple no-descent segment, not exceptional starting integers and not its
predecessor basin. The enormous explicit threshold is not a practical
finite-verification cutoff. The exponent-squaring principle (3), rather
than that threshold, is the point.

## R4-3. A shorter conditional physical stopping bound

Let an integer upper bound W>=w_n be supplied and set

    R=ceil(16 W^(19/20)).

Equivalently R is the least positive integer with
R^20>=16^20 W^19, so its computation needs no floating-point power.
Assume an actual finite certificate proves, for EVERY integer y in W_n,
that its first coefficient-subcritical time is at most N>=1. Then the
trajectory from n descends below n or repeats a state in at most R*N raw
shortcut steps.

Proof. Otherwise those R*N steps form a simple no-descent segment. From
each strict coefficient record, the supplied stopping certificate creates
the next strict global coefficient record within N further steps. Starting
at time zero gives R+1 distinct records by time R*N, contradicting (4).
All blocks are physically on the original orbit. Neither the source window
nor an individual block clock is reset to a favorable different root.

The hypothesis is NOT established here. Searching forever for a missing
coefficient crossing is not a total successful selector. A repetition is
not itself exclusion of a nontrivial positive cycle.

## R4-4. Unconditional finite extraction

Without the hypothesis of R4-3, any inspected simple no-descent segment of
length L contains an ACTUAL coefficient-supercritical prefix of length at
least max(0,ceil(L/R)-1), starting at one of its record sources in W_n.

Partition the elapsed time at consecutive record times, counting the last
interval to time L. There are at most R intervals and their lengths sum to
L. One has length at least ceil(L/R). All its proper prefixes are at least
the record coefficient; only its last step may be the next crossing. This
explains the indispensable minus one. The certificate records the original
source, original starting clock, and literal word. It does not select a new
2-adic continuation.

The executable checks complete first-descent prefixes for all n=2,...,8192.
Every one of those 8,191 inspected prefixes has only the initial coefficient
record. Thus this grid does NOT exercise multiple records before first
descent; that difficult scenario is related to the still-unproved Coefficient
Stopping Time conjecture (see SOURCES.md). A separate 511-source grid checks
complete simple prefixes that MAY descend, exercising up to 16 records and
the physical partition identities. It is not evidence for the no-descent
hypothesis in that harder regime. Both grids use exact rational distortion
windows rather than pretending to enumerate (2).

# Rank spectrum: a square-root spatial budget for all ordinary sources

**Status: PROPOSED pending independent mathematical review.** All statements
below concern the explicit rank of pass 4, not convergence. No probabilistic
parity assumption, external predecessor theorem, or unexamined source cutoff
is used. Claim IDs in this pass are local to PR #92.

## 1. Setup and the parent interface

Use the shortcut map T, the exact maximal-repetition acceleration A, and

    z_a(n) = (3^a-2^(a+1))n + 3^a-2^a,
    R_a(n) = z_a(n)^2 / 3^v3(z_a(n)),
    R(n) = min_(a>=0) R_a(n).

The zero convention is R(1)=0. For n>=2 the parent proves

    n-1 <= R(n) <= n^2,
    R(n)=min(R_0(n),R_1(n),R_2(n),R_h(n)), h=v3(2n+1),

where the last entry is needed only for h>=3. In particular
z_0=-n, z_1=1-n, z_2=n+5. The first three components have fixed affine roots;
the last is a genuine moving index. The parent proof is source-pinned in
[ATTEMPT_AND_SOURCES.md](ATTEMPT_AND_SOURCES.md). Nothing here promotes it to
independently reviewed status.

## 2. T-A3-1001: the complete rank spectrum has exponent one half

For real M>=1 define N_R(M)=#{n>=2:R(n)<=M}. Then

    floor(sqrt(M))-1 <= N_R(M)
       <= [5+(11/6)sqrt(3)] sqrt(M) < 9 sqrt(M).        (1)

The lower bound may be replaced by zero when negative. These inequalities
hold for every M, not merely asymptotically or for one orbit. Consequently
N_R(M)=Theta(sqrt(M)) as M tends to infinity.

### Proof of the upper bound

If an integer z is nonzero, write |z|=3^e u with e>=0, u>=1 and 3 not dividing
u. Then z^2/3^v3(z)=3^e u^2. For each of the fixed components a=0,1,2, a
rank at most M gives at most floor(sqrt(M/3^e)) possible u at exponent e.
Each u produces at most one positive n for that component. Dropping the
restriction 3 not dividing u is an upper bound. All three fixed components
therefore contribute at most

    3 sqrt(M) sum_(e>=0) 3^(-e/2).

If the minimizing component has a>=3, the collapse theorem gives a=h.
Since 3 does not divide n+1 and v3(2n+1)=a, both summands in z_a(n) are
divisible by 3^a. Thus e=v3(z_a(n))>=a. For each a,e,u there is at most one
ordinary n, since z_a is affine with nonzero slope. Hence the moving components
contribute at most

    sqrt(M) sum_(a>=3) sum_(e>=a) 3^(-e/2).

Writing r=1/sqrt(3), the total coefficient is

    3/(1-r) + r^3/(1-r)^2 = 5+(11/6)sqrt(3) < 9.

Counting the same n more than once only enlarges this upper bound. The lower
bound in (1) follows directly from R(n)<=n^2 for 2<=n<=floor(sqrt(M)). QED.

### A complete finite enumerator, not a scan through M sources

For every e with 3^e<=M and every 1<=u<=floor(sqrt(M/3^e)), 3 not dividing u,
put Z=3^e u. Form the candidates

    Z, Z+1, Z-5,
    (Z-(3^a-2^a))/(3^a-2^(a+1)), 3<=a<=e.             (2)

Retain positive integers n>=2 and remove duplicates. The result is EXACTLY
{n>=2:R(n)<=M}. Each generated integer has one component at most M, so is
sound; a minimizing component of any actual member occurs in this list, so
it is complete. The proof does not require a factorization oracle or infinite
search. Counting the loop iterations by the preceding geometric series gives
O(sqrt(M)) candidates; bit costs are separate from that count.

For one exact rank m, e=v3(m) and Z=sqrt(m*3^e) must be integral. Formula (2)
then becomes the parent finite-fiber list. The present improvement counts and
enumerates the entire sublevel, not only a single fiber.

## 3. T-A3-1002: sharp summability threshold and an explicit tail

For p>1/2 and M>=1,

    sum_(R(n)>=M, n>=2) R(n)^(-p)
        <= [9p/(p-1/2)] M^(1/2-p).                    (3)

In particular the complete sums satisfy

    sum_(n>=2) 1/R(n) <= 18,
    sum_(n>=2) 1/R(n)^2 <= 12.                        (4)

For 0<p<=1/2, sum R(n)^(-p) diverges. Thus p=1/2 is the exact summability
threshold for this specific rank.

### Proof

Use x^(-p)=p integral_x^infinity t^(-p-1) dt and nonnegative integration.
The number of retained ranks between M and t is bounded above by N_R(t).
Applying (1) gives (3). This also includes atoms of rank exactly M; no strict
versus non-strict cutoff is lost. Conversely R(n)<=n^2 gives
R(n)^(-p)>=n^(-2p), whose sum diverges when 2p<=1. This proves the threshold.

Since R(n)>=n-1, the unexamined ordinary tail n>N has R(n)>=N. Therefore

    sum_(n>N) R(n)^(-2) <= 12 N^(-3/2).                (5)

This analytic bound includes every omitted source without assuming it ever
converges. It is used to enclose finite-time mass in the new experiment.

## 4. What this buys for each full route

For the mass route, the common rank now supplies natural positive summable
weights and explicit all-source tails. For source separation, every lower-rank
witness lies in a list of size less than 9 sqrt(R(n)), rather than a numerical
scan through R(n)+1. For ranking, it bounds the number of distinct states that
can remain below a starting rank; [PLATEAUS_AND_SOURCES.md](PLATEAUS_AND_SOURCES.md)
proves the separate no-cycle fact needed to exploit this count.

None of these facts bounds all future occupation or forces a witness to merge
at a known time. In particular the rank power 1/2 cannot be compared directly
to a predecessor exponent in the ORDINARY source variable without the correct
change of variable and hypotheses. No such exponent-race crossing is claimed.

## 5. Finite evidence

The generator uses (2). The independent verifier scans every n<=M+1, using
properness for completeness and evaluating the whole component dictionary
until its increasing numerator exceeds n^2. They agree at M=4^j, 0<=j<=8.
At M=65536 the complete sublevel contains 635 sources; the largest is 59050.
This checks the enumerator. The uniform bounds and critical exponent follow
from the proof above, not from these nine finite levels.

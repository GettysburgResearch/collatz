# A two-place obstruction for every cheaper ordinary witness

**Status: PROPOSED.** This concerns the ordinary numerical order alone. Put

    ell_num(n)=min {max(t,s): T^t(n)=T^s(m), 1<=m<n},

with infinity if there is no such pair. A total successful selector for this relation would prove Collatz by strong induction. The following all-witness obstruction applies even with arbitrary unequal clocks and no restriction on which smaller source is tried.

Let M>=1 and r be either 0, 1, or 3. If n>3^M is positive, n=−1 modulo 2^M and n=r modulo 3^M, then ell_num(n)>M. More generally the result holds for an integer r>=0 such that every *nonnegative* integer less than r stays strictly below r throughout its signed-legal orbit (r=0 uses only negative virtual states). The source congruences and the hypothesis n>3^M are finite ordinary conditions, with no assumptions about other orbits.

## Proof by comparison at −1 and r

Assume t,s<=M give a merger. The source word v=1^t is forced. Write w for the physical word at m, q for its odd count, and C_v,C_w for the affine constants. Clearing the two endpoint denominators and cancelling their shared power of two gives m=(L n+E)/B, with

    g=min(t,s), L=2^{s-g}3^t, B=2^{t-g}3^q,
    E=2^{s-g}C_v−2^{t-g}C_w,          |E|<=3^M.

The bound on the difference follows because both nonnegative terms are at most 3^M. If L>B then m>=n by n>3^M. If L=B then t=s=q by unique factorization, w=v, and m=n. Consequently a smaller input needs c=L/B<1. This forces s>t: at s<=t the quotient is at least (3/2)^{t-s}. Now B=3^q and L=2^{s-t}3^t.

Define two virtual companions by the same affine map,

    gamma=(−L+E)/B,      eta=(L r+E)/B.

They satisfy F_w(gamma)=F_v(−1)=−1 and F_w(eta)=F_v(r)= (3/2)^t(r+1)−1. Both shortcut affine branches send the interval [−1,infinity) into itself, regardless of chosen parity. Thus F_w(−1)>=−1 and its positive slope gives gamma<=−1. It follows that eta=gamma+c(r+1)<r. Also eta is an **integer** because m is integral and 3^q divides n−r.

The actual m and virtual eta agree modulo 2^{s-t}: their difference is L(n−r)/3^q. The initial s−t bits of w are therefore legal for the signed integer eta. If r=1 or r=3 or the general stated guard holds, each such step stays strictly below r: negative integers remain negative, zero remains zero, and the positive cases follow from the guard. For r=0, eta<0 and the same negative invariance suffices. The remaining t affine steps from a value strictly below r cannot produce F_v(r): both branches are increasing, and among all t-bit words issued from the nonnegative r the all-odd affine word maximizes the output. This contradicts the required virtual equality. For r=3 the only positive starts below r are 1 and 2 with their two-cycle. This proves the claim, including empty-clock cases.

## Explicit successful families and the closing gap

For M>=2 prescribe n=1 modulo 3^M and the physical word 1^M 0^{M+2}. Choose the positive CRT lift in (3^M, 3^M+2^{2M+2}3^M]. Its prescribed endpoint is

    y=((3/2)^M(n+1)−1)/2^{M+2} < n.

Thus M<ell_num(n)<=2M+2 on explicit positive integers of height between 2^M−1 and exp(O(M)). The least possible successful selector clock on these examples has order log n. If a certificate of actual convergence is desired, the [halving-tail construction](TERMINATING_TOWERS.md) instead chooses a (possibly much larger) lift with the given ternary class and prefix whose endpoint is a power of two. Its all-witness lower bound is unchanged.

The obstruction exposes a specific remaining case for a universal algorithm. It must read beyond the two-place matching window, or use longer clocks on a smaller actual partner. The existence of smaller-source certificates on subprogressions and the almost-all rank-sublevel bound do not eliminate a possible least exceptional source after that window.

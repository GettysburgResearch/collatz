# Near-full rotation gcd with an increasing least denominator prime

For each fixed ε>0 there is c_ε>0 and a sequence of primitive positive
rational shortcut cycles of length L tending to infinity such that

* the raw D=2^L−3^K and hence the reduced denominator H>1 have no
  prime factor at most c_ε log L;
* log H≤L^(1/2+ε), the least phase exceeds L^(1/2−ε), and
  L−K log₂3 tends to zero from above;
* log D∼L log 2 and every rotation numerator has gcd D/H with D.

In particular the all-rotation divisibility test sees no bad valuation
at **any power of any prime** up to this logarithmic threshold. The
fixed rational phases belong to all the corresponding local integer
rings. Testing the archimedean size against a specified *integer*
representative modulo other primes is a different operation.

## Forcing the coarse multiplier in residue classes

Write c=log₂3 and let h/q be a continued-fraction convergent with q large.
Choose 0<η<1/4 as small as needed in terms of ε. Set P=κ log q with
κ>0 sufficiently small and take M=lcm(p−1 : p prime, 5≤p≤P).
The elementary Chebyshev bound log lcm(1,...,⌊P⌋)=O(P) gives M≤q^η.
The prime number theorem also gives M≥P/2−1 for large q.

There exist a,b satisfying

    a≡0, b≡1 (mod M),    0<b−ac<3M/q,    a≤Mq.

Indeed take j=⌊q/M⌋−1 and the unique 1≤u<q with uh≡j (mod q).
As |u(c−h/q)|<1/q, the fractional part of uc lies strictly between
1/M−3/q and 1/M; there is no wraparound. Put a=Mu and
b=M⌊uc⌋+1. In particular a≥M and b is comparable to a.
No lower bound on a in terms of an irrationality measure is needed.

## The primitive periodic signal

Use the [independent periodic inputs](NEAR_FULL_GCD.md), this time with
consecutive primes p_1,...,p_k *strictly above P*. Take n their largest
consecutive product at most q/(M log q), starting at the least such
prime. For all sufficiently large q the next prime is O(log q): the
prime number theorem gives total log-prime weight exceeding 2 log q
between P and P+3 log q. Consequently

    q/(O((log q)^2)M) ≤ n ≤ q/(M log q),
    k=O(log q/log log q),       Σ_j p_j=O((log q)^2).

Since a≥P/2−1 and P=κ log q, both runs after the encoding pairs are
long enough for the marker proof. With A=3^a and B=2^b the binary word
has primitive length L=bn, K=an ones and 0<L−Kc<3/log q.
For every prime 5≤p≤P one has B/A≡2 modulo p, and every prime factor
of n exceeds p−1. The order of 2 modulo p exceeds one and divides p−1;
it cannot divide n. Hence p does not divide D=B^n−A^n. The primes 2
and 3 do not divide D either.

The same independent prime-order component argument in the linked proof
gives H>1 and log H=O(b (log q)^2). It uses the primality of the p_j,
not coprimality of a and b. All rotations have gcd D/H with D and
log D∼L log 2 by B^(n−1)≤D<B^n. We have L=O(q²) and
b/n=O(M²(log q)^2), hence

    log H = O(sqrt(L) M (log q)^3).

Also log L≥(1−η−o(1))log q and M≤q^η. Choosing
η/(1−η)<ε and absorbing logarithms gives the asserted exponent.
The common boundary multiplier satisfies 1−A/B=O(M/q), and the
positive offset at each boundary is at least (A/B)/3. The
interior prefix multipliers are at least min((3/4)^k/2,A/B).
The least phase is therefore at least q^(1−η−o(1)), which exceeds
L^(1/2−ε) on decreasing η further if needed. Finally
P≥(κ/3)log L for large q.

Thus checking the smallest factors of D cannot supply a general
integrality obstruction at these scales, even for positive primitive
high-minimum words of vanishing total drift. The construction still
has gcd(L,K) divisible by n; it does not assert this roughness and
near-full cancellation combination for coprime length and weight.

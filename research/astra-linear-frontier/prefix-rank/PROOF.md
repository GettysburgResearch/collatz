# APR-001--005: a proper rank from every actual finite prefix

**Status: PROPOSED pending independent mathematical review.** This is not a
complete Collatz proof. The universal selector is OPEN, and one-step global
monotonicity is false. The map, candidate domain, zero-displacement convention,
finite evaluator, counting population and killed boundary are specified here.
No theorem from the parent research packet is assumed.

## 0. Definition

Use the shortcut map T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n,
on positive ordinary integers. Absorb at 1. For a nonzero integer d set

    g(d)=d^2/3^v3(|d|).

For n>=2 define

    F_0(n)=g(n),
    F_k(n)=4^k g(T^k(n)-n)   (k>=1, T^k(n)!=n),
    Gamma(n)=min({F_0(n)} union {F_k(n): k>=1, T^k(n)!=n}).       (1)

Set Gamma(1)=0. A zero displacement is OMITTED, not assigned rank zero.
The underlying T in (1) is the ordinary shortcut map; evaluating a prefix
that passes through 1 is permitted. Absorption is used for termination and
mass operators, not to change the affine parity identities.

All candidates use the ACTUAL prefix from the given source. Evaluating an
unrealized affine word at n is not an admissible rank candidate.

## 1. APR-001: properness and an exact finite evaluator

For every n>=2,

    n <= Gamma(n) <= g(n) <= n^2.                              (2)

Moreover every candidate that can beat F_0 has

    4^k <= g(n),       k <= floor(log_2 n).                    (3)

Thus (1) is an ordinary finite computation: follow at most floor(log_2 n)
shortcut steps, omit zero displacements, and minimize the displayed integers.
One may stop earlier when 4^k exceeds the current best rank. This is not a
search until an unknown stopping time, a fixed dictionary of affine forms,
or an infinite minimum asserted computable without a bound.

### Proof

For a length-k physical word, let q count its odd bits and A its affine
constant. Exact composition gives

    2^k T^k(n)=3^q n+A,       0<=A<=3^k-2^k.                  (4)

The upper bound follows by induction under A -> A or A -> 3A+2^k.
Put d=T^k(n)-n, nonzero. Unique factorization gives |3^q-2^k|>=1, whence

    n <= |3^q-2^k| n <= 2^k |d|+A <= 3^k |d| <=4^k g(d).     (5)

The penultimate inequality uses |d|>=1. Also g(n)>=n and g(d)>=1.
These prove (2)--(3), including the exclusion of every unexamined longer
prefix. The set of candidates is nonempty because F_0 is present. QED.

The ordinary values examined have O(log n) bits: T(x)+1 <=(3/2)(x+1)
and the clock in (3) is at most log_2 n. This states a bit-size/iteration
bound, not unit-cost arithmetic for arbitrarily large integers.

For the same word the candidate can equivalently be written

    Z_k(n)=(3^q-2^k)n+A=2^k(T^k(n)-n),
    F_k(n)=Z_k(n)^2/3^v3(|Z_k(n)|).                          (6)

The formula is valid because powers of two are 3-units. Periodic-ghost
coordinates from previous packets are therefore pieces of (1), but only
when the corresponding word is physically realized at n. The new minimum
includes arbitrary actual words, not merely 1^a0 corridors.

## 2. APR-002: an exact rotation descent, with no guessed next word

Suppose k>=1 attains Gamma(n), d=T^k(n)-n is nonzero and EVEN, and b=n mod2.
The two sources n and n+d have the same next parity, so

    T^{k+1}(n)-T(n)=(3^b/2)d.

Consequently

    Gamma(T(n)) <= (3^b/4) Gamma(n) < Gamma(n).                (7)

If T(n)=1 its rank is zero and the inequality is stronger. Otherwise the
length-k actual prefix at T(n) is an admissible candidate, and its exact
valuation gives (7). The word is rotated physically, not imposed by an
independent parity choice. If F_0 attains Gamma(n) and n is even, similarly

    Gamma(T(n)) <= Gamma(n)/4.                               (8)

These tests are decidable using (3). They are sufficient guards, not necessary
conditions for an actual one-step rank drop. If several indices minimize,
any even nonzero displacement suffices. Zero displacements remain omitted.

### Exact residual at a hypothetical component minimum

If an exceptional positive component exists, it has a minimum Gamma because
Gamma is a positive integer away from 1. A minimizing source cannot satisfy
(7) or (8). Every nonzero minimizing prefix at such a source must therefore
have ODD displacement; a minimizing baseline can occur only at an odd source.
This is a necessary restriction, not a theorem that the residual is empty.

## 3. APR-003: complete finite rank sublevels and their critical exponent

Let N(M)=#{n>=2:Gamma(n)<=M}, M>=1, and K=floor(log_4 M). Then

    floor(sqrt(M))-1 <= N(M) < 5(K+1)sqrt(M).                  (9)

In particular sum Gamma(n)^(-s) over n>=2 converges exactly for s>1/2.
This is a count of ALL ordinary integers by an explicit rank, not a count of
Collatz survivors or of their basins.

### Complete enumerator and proof

Every positive d with g(d)<=Y has the unique form d=3^e u, with
3 not dividing u and 3^e u^2<=Y. Their number is at most

    c sqrt(Y),        c=1/(1-1/sqrt(3)) < 5/2.                (10)

The baseline candidates are these d at Y=M. For each 1<=k<=K, enumerate
ALL 2^k binary words, calculate their q,A, and enumerate both signs of the
displacements 3^e u with 3^e u^2<=M/4^k. A possible source is uniquely

    n=(2^k d-A)/(3^q-2^k).                                  (11)

Keep positive integral n>=2 and verify its actual prefix and rank. This is
complete by (4) and (3); it is not an inverse search with an empirical cutoff.
Each word has at most 2c sqrt(M)/2^k candidate displacements. The whole list
has at most c(2K+1)sqrt(M)<5(K+1)sqrt(M) entries before deduplication.
The bound counts actual integers, not word multiplicities. The lower bound
follows from Gamma(n)<=n^2. QED.

An entirely rational all-source tail, convenient for s=2 and integer J>=0, is

    sum_{Gamma(n)>4^J} Gamma(n)^(-2)
       <= (80/49)(7J+15) 8^(-J).                            (12)

Indeed partition into (4^i,4^(i+1)], use (9), and sum
10 sum_{i>=J}(i+2)8^(-i). Likewise sum Gamma(n)^(-1)<=60.
For the converse at s=1/2, Gamma(n)^(-1/2)>=1/n. For smaller positive s the
terms are still larger; for s<=0 they do not tend to zero. This proves the
claimed convergence threshold, not just sufficient summability.

## 4. APR-004: safe excursions can be eliminated, not unsafe transport

Put G={n>=2:Gamma(T(n))<Gamma(n)} and U={n>=2}\G. For a nonnegative source
mass on G, K_G is forward pushforward by T, killed when the endpoint is 1 or
is outside G. In particular reaching U is NOT called convergence.
Every consecutive run of G states starting at rank at most 4^J is finite,
with at most

    L_J=5(J+1)2^J                                           (13)

states before reaching U or 1. All states are distinct and their ranks are
at most the initial one, so (9) proves the claim, including the final exit.
For any initial f with 0<=f(n)<=C Gamma(n)^(-2),

    sup_{r>=L_J} ||K_G^r (1_G f)||_1
       <= C (80/49)(7J+15)8^(-J).                           (14)

This follows by charging the original high-rank sources once, using (12).
It does not reset a pointwise envelope at later entries into G.

A complete undiscounted safe-occupation estimate is also available:

    sum_{r>=0} ||K_G^r (1_G f)||_1 <= (21200/27) C.           (15)

For sources with 4^i<Gamma<=4^(i+1), both the count and the maximum residence
are at most 5(i+2)2^(i+1), while each source weight is at most C16^(-i).
Their total charge is at most 100C(i+2)^2 4^(-i); its sum is 21200C/27.
All non-core ranks exceed one, so these bands cover the domain.

The first subsequent U-return is a total finite operation unless it is
killed at 1: after the first step, an intervening G excursion is finite by
(13). This does NOT prove the U-return process terminates. On ordinary
unweighted l1 it is a substochastic deterministic pushforward. No invariant
rank moment or pointwise envelope for that process is supplied.

## 5. APR-005: the complete closing criterion and the first missing step

A family of finite PHYSICAL merging diagrams covering every n>1,

    T^r(n)=T^s(x),       x>=1,       Gamma(x)<Gamma(n),         (16)

would prove Collatz by the least-exceptional-Gamma argument. A constructive
selector must have its own termination proof. Its output must include the
ordinary sources, clocks and common endpoint; having a cheap integer in
(11) is not itself a merger.

Alternatively, on the actual U-return operator, a strictly positive summable
weight with strict inverse supersolution inequality would give the same
exceptional-set contradiction. Such a weight is NOT constructed here.

APR-002 supplies a universal finite guard. PERIODIC_SWITCHING.md proves its
success on every primitive expanding periodic architecture under explicit
finite ordinary source conditions, allowing arbitrary periods and arbitrarily
many mixed switches. Neither result proves coverage of U. The exact sources
3,5,9 already defeat global one-step monotonicity. SPIKES.md proves an
unbounded obstruction for every positive power of three, not just these tests.

The missing full proof is therefore not hidden inside the evaluator or a
formal infinite minimum. It is the control of the remaining odd-displacement
and baseline switches at fixed ordinary sources. No all-source rank-lowering
selector or complete Collatz proof is claimed.

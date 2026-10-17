# Ternary splices at an unchanged original source

**TSB-001--004: PROPOSED, with a separate in-session mathematical reconstruction;
not accepted project mathematics or a complete Collatz proof.**
Date: 2026-10-18 (Asia/Jerusalem). No external priority claim.

Use the unabsorbed shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n.
Words list actual source parities chronologically. All source caps refer to the
immutable original N, not to a later state.

Exact source tuples are frozen in [SOURCES.json](SOURCES.json). The full proof
bodies of #125, #130, #133, #135 and #136 were inspected, together with #134 at
`025f2683c19bfedc3eeff0303206b20c889c8005`. In particular, #134/EPT-005 already gives
the distinct 8N+3 ternary switch at one original step, and EPT-004 already gives
complete finite inverse search at every prescribed odd-block budget. The rule
below is a short closed specialization using 4N+3 and the actual first hard
exit. The general inverse-search concept and witness-preserving lifts are
credited, not reinvented.

## TSB-001. A two-odd-block 4Z+3 switch at the actual hard exit

Let Z>1 be odd, r=v2(Z+1)>=1, u=(Z+1)/2^r, and assume the actual first odd exit
is hard: 3^r u=3 mod4. Let a>=1 satisfy 3^a | 4Z+3, and put

    b=(4Z+3)/3^a,   m=2^a b-1,   E=(3^(r+1)u-1)/4.

Then every source is a positive ordinary integer, and

    T^(r+2)(Z)=T^(a+r+4)(m)=E.
    Z word: 1^r 01.
    m word: 1^a 0 1^(r+1) 00.

Indeed b is positive and odd, so the first a steps from m are odd and end at
3^a b-1=4Z+2. One halving reaches 2Z+1=2^(r+1)u-1, whose next r+1 steps are
odd and end at 3^(r+1)u-1. The hard condition makes this last value divisible
by four, so two actual halvings reach E. On the Z arm the first r odd steps
reach 3^r u-1, whose valuation is exactly one under the hard condition. The
next halving and odd step reach E. These calculations establish the words and
the clocks, including their independent offsets.

For an actual checkpoint Z=T^A(N) on an immutable original source N, this is
an acceptable smaller-original-source merger exactly when

    2^a(4Z+3) < 3^a(N+1).                         (TS.1)

The original clock is A+r+2 and the companion clock is a+r+4. A successful
comparison against Z alone is insufficient when Z>N. There is a decisive
limitation to this formal checkpoint version: a>=1 forces 3|Z. After ANY
actual odd shortcut step, the output is 2 mod3, and subsequent even or odd
shortcut steps remain units modulo three. Therefore this valuation switch
cannot recur on the later arm of an odd original N. For a hypothetical least
source it is an initial-source exclusion, not a recurrent transport or return
estimate. An initially even N may have such checkpoints only before its first
odd step, and already has immediate descent.

At Z=N the threshold is particularly simple and sharp:

    m<N if and only if a>=4.

For a>=4,

    0<m=4(2/3)^a N+3(2/3)^a-1 < 4(2/3)^a N < N.

For a=1,2,3, the exact differences m-N are respectively
(5N+3)/3, (7N+3)/9 and (5N-3)/27, all positive for N>=1.
Taking a=v3(4Z+3) minimizes m among this specified shadow family, because
each increase of a multiplies m+1 by 2/3.

For a hypothetical least nonconvergent N, the old first-exit theorem already
supplies r>=2 and the hard condition. Hence TSB-001 excludes the entire actual
ternary stratum v3(4N+3)>=4, with no new dyadic gate chosen after N is fixed.
Every such N is a multiple of three. Its pure ancestors are only 2^j N, so
the merger uses the actual forward arm in an essential way.

This does not subsume #134/EPT-005, whose distinct valuation form is 8N+3 and
which uses just one original step. For N divisible by three, v3(4N+3)>=2
implies v3(8N+3)=1, since 8N+3=2(4N+3)-3. Thus the two deep-valuation guards
are disjoint. Neither guard is universally satisfied.

## TSB-002. Unbounded first runs with failed old root order, repaired by TSB-001

For every fixed pair of integers r>=6 and a>=4, choose a positive u satisfying

    3^(r-1)u = 9 mod16,
    2^(r+2)u = 1 mod3^a.                            (TS.2)

There is one such progression modulo 16*3^a by CRT; all its u are odd, and it
has an infinite positive tail. No exact ternary valuation is required.
Define

    N=2^r u-1,
    C=(3^(r-1)u-1)/4,
    M=3C/2=(3^r u-3)/8,
    m=2^a(2^(r+2)u-1)/3^a-1.

The first condition gives the actual hard entry and v2(C)=1. Thus #135/FSS-002
has the physical one-step companion M at the endpoint two steps after H(C),
but its original-root acceptance test fails on EVERY member:

    M-N=((3^r-8*2^r)u+5)/8 >0,

because r>=6. The ratio M/N can be arbitrarily large across these families as
r grows. No claim is made that every other old selector also fails there.

The second condition gives the different TSB-001 source m, so

    T^(r+2)(N)=T^(a+r+4)(m)=H(C),
    0<m<4(2/3)^a N<N.

Every positive-time original state through r+2 exceeds N. In fact, for r>=3
the exact minimum is T(N)=(3N+1)/2. The initial r odd steps increase; the only
subsequent valley is (3^r u-1)/2, and its difference from T(N) is
((3^r-3*2^r)u+1)/2>0. The following odd step increases again.
All N are divisible by three, so none has a smaller pure ancestor at any
depth. The threshold a=4 therefore repairs arbitrarily long first runs and
arbitrarily severe failures of the old root inequality, on the stated
ordinary progressions. It does not force TS.2 on an arbitrary fixed N.

A small whole family (r=6, a=4, u=835+1296t), for every integer t>=0, is

    N=53439+82944t,
    m=42223+65536t,
    E=456536+708588t,
    T^8(N)=T^14(m)=E,
    original word 11111101,
    companion word 11110111111100.

Its old source is M=76089+118098t>N throughout. Its original-arm minimum is
80159+124416t>N. This family comes from the valuation identity directly;
it is not inferred by sampling the displayed t values.

## TSB-003. An independent smaller companion beyond the new valuation guard

The literal witness

    T^8(90303)=T^26(14847)=771464

has upper word 11111101 (7 odd steps) and lower word
11111111101101110011111100 (20 odd steps). The common first endpoint is H(85718).
The supplied raw paths are checked separately by
`experiments/paired-comparison/source-budget/check_splices.py`.

The primitive point-preserving lift from #133/PSS-002 has source steps
2^8*3^13 and 2^26. Restrict its parameter to 4t, retaining v2(C)=1. Then
for EVERY t>=0,

    N=90303+1632586752t,
    m=14847+268435456t,
    E=771464+13947137604t,
    T^8(N)=T^26(m)=E,
    0<6m<N.

At each of the eight positive prefix times the forward affine multiplier
on the original value is greater than one, and its additive term is positive.
Hence every state on the displayed original arm is above N. The standalone
whole-family check also verifies the strict coefficient and intercept
inequalities separately. Every N is divisible
by three. The old FSS source is

    M=128577+2324522934t>N.

Moreover v3(4N+3)=2 throughout this family: the base 361215 has exact valuation
two and the increment 6530347008 is divisible by 3^13. Thus TSB-001's automatic
root-safe guard also fails throughout. This is an actual alternative
companion, not a repair by simply applying the same failed valuation rule.

The bounds follow exactly from

    N-6m=1221+21974016t>0,
    M-N=38274+691936182t>0.

The source increments preserve the two physical words; their endpoint
increments both equal 4*3^20=13947137604. This is a whole affine family, not
an all-source covering theorem. It is similar in mechanism to #133/PSS-003
and is credited to that lifting theorem; its distinct point is that both
specified compressed-companion tests fail at these unchanged roots.

## TSB-004. A complete smaller-source-bank control at N=27

Every m=1,...,26 has an explicitly reconstructed finite path to 1. Continuing
through the unabsorbed 1<->2 core adds no new states. The union of all those
paths is therefore the complete set of states reachable from ANY smaller
original source at ANY nonnegative clock. Independently intersecting that
finite union with the literal path of 27 shows:

    first contact is time 59, at state 23.

The available smaller-source witnesses there include m=23 with clock zero
and m=15 with clock one. Every actual 27 state at times 0,...,58 is outside
the entire smaller-source bank, not merely outside the one-step band or a
bounded inverse language. Explicitly this bank is

    {1,...,26} union {29,32,35,38,40,44,53,80}.

It is closed under the unabsorbed T map, and each of the eight additional
values occurs in a displayed path from a source below 27. This finite closure
also independently proves that unbounded companion clocks add no new states.

Consequently an assertion that EVERY input has some smaller-original-source
merger before its first ordinary descent is false, even with unrestricted
companion clocks. This is a finite complete control for the one root 27;
it does not obstruct a proof that allows ordinary descent as an outcome.

## What remains

The ternary condition is tested on the unchanged root; TS.1's formal later
checkpoint version is restricted by the three-unit obstruction stated there.
No theorem forces a root to have the needed valuation at a hard exit, and the
new families do not exclude permanent
escape through the complementary conditions. A finite companion bank cannot
be treated as having returned unless its actual original clock has advanced.
None of these results supplies all-input termination or a full proof.

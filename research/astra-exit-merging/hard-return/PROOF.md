# A reusable hard-exit return, not another single successful exit

**Status: PROPOSED pending independent mathematical review.**
Date: 2026-09-19. Programme: issue #121. Parent: PR #122 at
`65c91ecea97d9ebf931eb1d9284b7950182a298e`.

The main advance over the parent is a reusable paired-trajectory transition.
The old second-exit failure can enter the SAME comparison type again, with
its arms exchanged. This gives a composable certificate for arbitrarily
many changing hard labels, including arbitrarily many expanding returns.
A cylinder compiler realizes every finite label list. It does NOT prove
that an arbitrary fixed input eventually reaches a merging exit.

All results concern positive ordinary integers under raw shortcut iteration:
T(n)=n/2 for even n and T(n)=(3n+1)/2 for odd n. The raw 1 -> 2 -> 1 cycle
continues when clocks are compared. A bit word records actual source parities
in chronological order. No rank, transfer operator, or map is changed.

## 1. AHR-001: the reusable paired return

For C>0 compare the ordered pair

    H(C)=9C+2,  L(C)=C.

Read r=v2(C+2)-1. The transition applies when r>=3. Then uniquely

    C=2^(r+1)b-2,   b positive odd.

Both branches below have the same clock length r+3.

### Merging exit

If 3^r b=1 mod4, set E=(3^r b-1)/4. The physical words

    H arm: 0000 1^(r-3) 01
    L arm: 0    1^r     00

meet at E. In particular,

    T^(r+3)(9C+2)=T^(r+3)(C).

### Hard return

If 3^r b=3 mod4, set D=(3^(r-1)b-1)/4. The physical words

    H arm: 0000 1^(r-3) 00
    L arm: 0    1^r     01

give the exact SWAPPED pair

    (T^(r+3)(9C+2), T^(r+3)(C))=(D,9D+2).

Thus the new parameter is D, and the larger and smaller arms exchange roles.
The old sources have not been replaced as induction comparators. r<3 is an
exit from this transition language, not a divergent source or a certificate.

### Proof, including the r=3 endpoint

Since

    9C+2=16(9*2^(r-3)b-1),

four even steps are legal. When r>3, the next r-3 steps are odd and end at

    U=3^(r-1)b-1.

For r=3 the odd block is empty, and the same formula holds. From C, one even
step gives 2^r b-1; r odd steps end at

    V=3^r b-1=3U+2.

All these states are positive. If 3^r b=1 mod4, then U=2 mod4 and V=0 mod4.
The tails 01 from U and 00 from V both end at (3U+2)/4=E. If 3^r b=3 mod4,
then U=0 mod4 and V=2 mod4. The tails 00 and 01 end at D=U/4 and
(3V+2)/4=9D+2. This proves the words, clocks, integrality and positivity.

### The parameter is not a global decreasing rank

For a hard return,

    D-C=((3^(r-1)-2^(r+3))*b+7)/4.

It follows that D<C for 3<=r<=7 and D>C for every r>=8. Indeed the first
coefficient is at most -55 in the former range and at least 139 in the latter.
In particular arbitrarily many r=8 returns are expanding; the construction
below realizes them. Their validity is not disguised as a decreasing rank.

## 2. AHR-002: arbitrary finite compositions, with orientation retained

Start from (9C0+2,C0). At each hard return read the next parameter from the
ACTUAL current C, apply Section 1, and reverse the orientation flag. At a
merging exit both arms meet, regardless of the flag.

If the actual finite itinerary has labels r1,...,rJ, all >=3, with J-1 hard
returns followed by a merging exit, the two original arms meet after

    Q=sum_i (ri+3)

steps each. Every appended word has its stated physical parity, by induction
on the transitions. No decreasing intermediate value is required. Conversely,
this itinerary language means exactly those guards; no successful exit is
inferred from a finite unsuccessful prefix.

A bounded implementation takes a stage budget. It returns a replayable
certificate, OUTSIDE_LANGUAGE when r<3, or BUDGET_EXHAUSTED. It is total as a
bounded procedure, not a successful selector for all sources. An explicit
finite itinerary also functions as a certificate without running a search
until success.

## 3. AHR-003: the parent's complementary second exit now has a return language

Let n=8^k u-5, k>=1, u positive odd. Read

    h=v2(9^k u+1)-4 >=1,
    a=(9^k u+1)/2^(h+4).

Unlike the parent's merging theorem, impose the COMPLEMENTARY exit guard

    3^(h+1)a=3 mod4.

Equivalently 3^h a=1 mod4. Define

    m=(n-5)/2,  C=(3^h a-1)/4.

Both are positive. The parent bridge, recalled below, gives the physical
prefixes

    F0=(110)^k     0100    1^h     01,
    B0=(110)^(k-1) 1110000 1^(h-1) 00,

ending at H(C)=9C+2 and L(C)=C, respectively. Their lengths are

    A0=3k+h+6,  B0_length=3k+h+5.

If this C has the itinerary of Section 2, append its orientation-aware words.
Then

    T^(3k+h+6+Q)(n)=T^(3k+h+5+Q)(m),  0<m<n/2.       (1)

If also 3|n, x=n/3-2 is positive odd and T(x)=m. Consequently

    T^(3k+h+6+Q)(n)=T^(3k+h+6+Q)(x),  0<x<n/3.       (2)

These statements apply to every GIVEN input with these actual guards. The
CRT construction later proves non-vacuity; it does not force an arbitrary
input's future. The parent's good second-exit guard remains valid separately.
No old result is weakened or promoted by this addition.

### Physical entry bridge, restated for standalone checking

Put v=9^(k-1)u. Both n and m follow k-1 copies of 110 and reach 8v-5 and
4v-5. This follows from the physical identity

    8A-5 -> 12A-7 -> 18A-10 -> 9A-5.

Since 9v+1=2^(h+4)a, v=7 mod32. On that entire progression the paths are

    8v-5 --1100100--> X=(27v-13)/16,
    4v-5 --1110000--> Y=(27v-29)/32.

For a direct parity check substitute v=7+32t: the two paths have states

    256t+51,384t+77,576t+116,288t+58,144t+29,
    216t+44,108t+22,54t+11;
    128t+23,192t+35,288t+53,432t+80,216t+40,
    108t+20,54t+10,27t+5.

Here X+1=3*2^h a and Y+1=3*2^(h-1)a. At X, h odd steps followed by 01
end at (3^(h+2)a-1)/4=9C+2. At Y, h-1 odd steps followed by 00 end at C.
The complementary guard makes exactly those last parities legal. The h=1
case has an empty second odd block. All intermediate values are positive.

For 3|n, the elementary equality T(n/3-2)=(n-5)/2 proves (2). This adds an
actual physical step, not a reassignment of clock conventions.

## 4. AHR-004: a complete cylinder compiler for this finite language

For ANY nonempty finite list r1,...,rJ with every ri>=3, the itinerary
"hard at r1,...,r(J-1), merge at rJ" holds on exactly ONE positive-integer
residue class

    C=c mod 2^S,  S=sum_i(ri+3), 0<c<2^S.             (3)

The class is exact for these labeled transitions, not a classification of all
possible coalescing pairs. Distinct complete itinerary lists define disjoint
classes, because every actual label and exit type is uniquely determined.

### Constructive proof

At a merging label r, the exact condition on b is b=3^r mod4. At a hard label
r it is b=3^(r+1) mod4. Let b0 be the appropriate representative in {1,3}.
The single-stage class is

    C=c0 mod d,  c0=2^(r+1)b0-2,  d=2^(r+3).

For the final merging label this is the compiled class. At an earlier hard
label write C=c0+d t. Its successor is

    D=D0+A t,  D0=(3^(r-1)b0-1)/4,  A=3^(r-1).

If the compiled suffix is D=c' mod M, there is a unique solution

    t=(c'-D0)*A^(-1) mod M,

because M is a power of two and A is odd. Thus the new representative is
c=c0+d t and the new modulus is d M. It lies strictly between zero and dM.
This proves the compiler by reverse induction. All positive representatives
are actual ordinary paths by Section 1. No infinite-cylinder intersection or
ordinary realization is inferred.

### Original inputs exist at all lengths, in the old n=3 mod12 residual class

Fix any k,h>=1 and any label list in (3). Put p=9^k, epsilon=(-1)^(k+1), and

    a0=(1+epsilon*p)*2^(-(h+4)) mod (3p),
    M3=3^h*(3p),
    c3=(3^h*a0-1)*4^(-1) mod M3.

Solve C=c mod 2^S and C=c3 mod M3 by CRT. Let C0 be the least representative
and set C=C0+(2^S*M3)t for arbitrary t>=0. Define

    a=(4C+1)/3^h,
    u=(2^(h+4)a-1)/9^k,
    n=8^k u-5.

Here a is positive odd, and a is a ternary unit since a0 is. Thus h is exact.
The congruence on a gives u integral with u=epsilon mod3. Its positive
numerator makes u>=1; u is odd. The dyadic class of C makes 4C+1=1 mod4,
so the complementary guard is automatic. Finally 8^k*epsilon=2 mod3 makes
3|n, while n=3 mod4. Therefore n=3 mod12, and (2) applies.

This independently varies k, h, the number of hard returns, and EVERY hard
label. In particular the lists (8,...,8,4) give arbitrarily many expanding
hard returns before merging. The selected source generally changes when the
list changes; no infinite ordinary itinerary is extracted from this fact.

## 5. AHR-005: long certificates without forward descent or a smaller ancestor

For a list of J stages, define K(J) as the least positive integer k satisfying

    3*9^(k+J) >= 128*64^J*8^k.                       (4)

Such k exist since 9/8>1. For J=1,2,3,8 the values are 49,66,82,166.
The bound is sufficient, not claimed optimal.

Every input of Section 3 with k>=K(J) stays STRICTLY ABOVE n at every
positive time on its entire n-arm through the certified merger.

### Proof

Put L=(3*9^k*u-29)/128. The entry parameter satisfies C>=L, since h>=1.
The first k-1 110 blocks strictly increase their starting values, and all
their intermediate states exceed the block's starting value. On the fixed
bridge the minimum is X=(3*9^k*u-13)/16>L. During the following odd run values
increase; its hard-exit states are 6C+1 and 9C+2, also above L.

During any Section 1 transition, every intermediate state of EITHER arm is
at least (9/64)C. For the upper arm, the initial four divisions end above
9C/16 and the following odd steps increase. A hard 00 tail ends at

    D=[3^(r-1)C+2*3^(r-1)-2^(r+1)]/2^(r+3) >=9C/64,

since r>=3 and its constant numerator is positive. The merging 01 tail is
larger than this bound. On the lower arm the first division is C/2, the odd
steps increase, and either permitted tail also stays above the same bound.
This proves the claim for each arm, including r=3.

Inductively every later state is at least (9/64)^J L. Subtract n=8^k u-5:

    (9/64)^J L-n
    =[3*9^(k+J)/(128*64^J)-8^k]u
      +5-29*9^J/(128*64^J) >0

by (4). The initial increasing blocks were handled separately. Orientation
swapping cannot invalidate a bound proved for BOTH arms.

If 3|n, its only depth-b positive ancestor is 2^b n: an odd inverse would
require (2n-1)/3 integral, while the even inverse preserves divisibility by
three. Thus the CRT specialization with k>=K(J) has no smaller pure ancestor
at any depth and no forward descent on the whole displayed arm, but still
has the lower-source two-sided certificate (2).

## 6. A limitation that must constrain the next continuation

The fixed equal-clock partner is NOT universal, even after entry into the
parent's complementary second exit. For n=3003 (k=2,u=47,h=1,a=119), x=999,
the actual first visits to 1 occur after 29 and 34 shortcut steps respectively.
The supplied verifier replays both complete paths. These times have opposite
parity. Since raw T has the two-cycle 1 -> 2 -> 1, the eventual phases differ.
If the paths had met at any equal time, determinism would force identical
future phases, a contradiction. Therefore

    T^t(3003) != T^t(999) for EVERY t>=0.

They DO share a future under unequal clocks: T^29(3003)=T^34(999)=1.
This is not a Collatz counterexample, nor an obstruction to other partners.
It shows that simply asserting eventual success for the exact equal-clock
pair used here is false. Its entry C=89 has r=-1 and is outside the return
language. Likewise the abstract pair (128,14) returns to (2,20), exits the
language, and has a permanent equal-clock phase mismatch.

## 7. What was gained; what remains open

The complementary exit is no longer just a failure label. It has an exact
return mechanism that preserves a two-sided comparison, changes labels,
and swaps arms. Every finite hard-return itinerary ending at a merging exit
has a complete arithmetic cylinder and lifts to a source below n/3. The
no-forward-descent theorem survives arbitrarily many transitions.

This is NOT coverage of all x=7 mod32, all original sources, or even every
entry C. Outside-language exits and infinite hard-return itineraries remain
uncontrolled. Bounded unsuccessful trials are kept, not removed. The return
parameter can increase, so a local valuation or height rank is not silently
made global. The all-finite-itineraries construction is not one all-time
ordinary witness.

The next useful extension must allow clock offsets or alternate companions
at outside-language exits, preserve the immutable original-source inequality,
and handle actual successor guards. Proving only that the present fixed
partner always merges synchronously would chase the explicit false claim in
Section 6. All parent and new mathematical statuses remain separately scoped.

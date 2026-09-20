# Universal shadow types, a fixed-gap compiler, and strict escape families

**Status: PROPOSED pending independent mathematical review.** Date: 2026-09-20.
Programme: issue #121. Parent: PR #126 at
`7e996feb24cc5d8579d75b39e0b909ffc03b3bcb`.
This is an additive research continuation, not integration or acceptance.
No complete Collatz proof or external priority claim is made.

The strongest original-root extension here is Section 5: every member of an
explicit two-parameter family fails the parent's selected H continuation,
but a shorter odd-run shadow gives a merger. Sections 1--3 provide systematic
interfaces rather than new universal termination assertions. In particular,
**complete transition syntax, complete finite-budget classification, an
existence theorem for subfamilies, and successful all-source coverage are
four different things**. Only the first three are supplied here.

## Conventions

Use the raw shortcut map T(n)=n/2 for even n and (3n+1)/2 for odd n.
All actual witnesses have positive ordinary sources. Raw T continues through
1 -> 2 -> 1. Word bits are chronological source parities. Each original arm
retains its own clock, including when a chart exchanges its coordinates.
For a word w of length L, with q ones, put

    2^L T_w(n)=3^q n+A_w.

A_w is obtained from A=0 by A <-3A+2^i on an odd bit at position i, and
unchanged on an even bit. The word has exactly one legal source residue
r=-A_w(3^q)^(-1) mod 2^L. Endpoint integrality in this particular binary
shortcut convention implies the full finite parity word: induction on its
successive lifts gives one residue at every depth. This familiar interface
is proved/used in the parent sources; it is also elementary to verify directly.

A successful certificate is T^a(n)=T^b(m) with 0<m<n. It contradicts n being
a least nonconvergent positive source. A smaller companion of a LATER inflated
state is insufficient unless its order relative to the original n is proved.

## 1. AUA-001: every positive source has a finite merge-or-H entry

This packages the elementary odd-run comparison already underlying AEM-002;
it is not claimed as a new Collatz reduction or a novel identity.

For even n>1, T(n)=n/2<n. For odd n>1, write uniquely

    n=2^r u-1, r=v2(n+1)>=1, u positive odd,
    m=(n-1)/2=2^(r-1)u-1, B=3^(r-1)u-1.

Here m>=1 and B>=2. The words 1^r and 1^(r-1) from n and m reach
(3B+2,B). Both B and 3B+2 are even. After one even step each, the pair is
(3C+1,C), C=B/2.

* If C is odd, one even step on the first arm and one odd step on the
  second arm merge at (3C+1)/2. Complete words are 1^r00 and 1^(r-1)01.
* If C is even, write C=2D. One odd/even step gives (9D+2,D).
  Complete words are 1^r01 and 1^(r-1)00.

Thus **every positive n>1**, not merely the 110-shadow representation,
has a finite physical lower-companion comparison ending at a merger or
H(D)=(9D+2,D). The first arm clock is r+2, the second r+1. In the H case
D>=1. Neither H entry nor convergence of its smaller arm proves convergence
of its other arm. The old synchronous H selector is not universally successful:
for n=7, m=3 this entry gives (26,2), and a rigid equal-clock continuation of
those states need not merge. Asynchronous core meetings remain permissible.

This removes a bookkeeping gap in specifying initial comparisons for all
sources. It does not remove the universal mathematical difficulty.

## 2. AUA-002: a complete countable grammar for the paired affine states

Describe a pair by

    (X,Y)=(3^d y+b,y), d>=0, b an integer, y>=1, 3^d y+b>=1.

The first coordinate need NOT be the numerically larger one. An orientation
flag associates the two coordinates with the immutable original sources.
Every simultaneous shortcut step is described by exactly one row below.
In the last row only, the coordinates are exchanged and the flag toggles.

| Actual case | d' | b' | y' | Exchange? |
|---|---:|---|---|---|
| b even, y even | d | b/2 | y/2 | no |
| b even, y odd | d | (3b+1-3^d)/2 | (3y+1)/2 | no |
| b odd, y even | d+1 | (3b+1)/2 | y/2 | no |
| b odd, y odd, d>=1 | d-1 | (b-3^(d-1))/2 | (3y+1)/2 | no |
| b odd, y odd, d=0 | 1 | (1-3b)/2 | (y+b)/2 | yes |

**Proof.** The parity of X is the parity of y+b, since 3^d is odd.
Substitute the appropriate two affine branches of T, and express the result
as (3^(d') y'+b',y'). All displayed divisions are integral by the row's
parity guard. Positivity follows from actual iteration of the positive pair.
The rows are disjoint and exhaustive. The last exchange is necessary to
avoid introducing a negative exponent of three. QED.

A uniform merger is the state d=b=0. A particular numerical pair can also
meet when d>0 and b=-(3^d-1)y; do not omit these isolated meetings. A pair
(1,2) or (2,1) admits an asynchronous one-step core merger, although its raw
synchronous orbit never meets. This is an explicit control against confusing
complete transition rules with synchronous termination.

This is a **countable-state** description: neither d nor b is bounded.
It is not a finite-state quotient, a decreasing rank, or an exclusion of
infinite trajectories. Any numerical pair can initially be represented
with d=0 and b=X-Y, but that tautological observation is not a convergence
argument. Its useful role here is that it closes the concrete monomial-slope
comparison types encountered when different odd-run shadows are selected.

## 3. AUA-003: every fixed integer gap has an explicit uniform merger class

### Statement

For every delta>=1 there are explicitly computable equal-length words
F_delta,G_delta, a positive residue 0<c_delta<2^ell, and an integer ell>=3
such that, for **every** positive y=c_delta mod 2^ell,

    T^ell(y+delta)=T^ell(y).

The two words are physical on that entire class. Their construction takes
O(log(delta+1)) gap-reduction stages. In particular, for delta>1, if K is
the least positive integer satisfying

    4^K > 3^K (delta-1),

then ell<=2K+3. The assertion is existence of a guarded class for each gap,
not that all pairs at that gap merge or that the prescribed class contains
the y of an arbitrary failed comparison.

### The four small physical identities

Compare upper y+delta with lower y.

1. delta=1, y=4 mod8. Words 100 / 001 merge at (3y+4)/8.
2. delta=2e, y even. Words 0 / 0 change the gap to e, lower y/2.
3. delta=1 mod4, delta>1, y=1 mod4. Words 01 / 10 change the gap to
   (3delta+1)/4, lower (3y+1)/4.
4. delta=3 mod4, y=2 mod4. Words 10 / 01 change the gap to
   (3delta-1)/4, lower (3y+2)/4.

For example, row 3 has upper/lower endpoints

    (3y+3delta+2)/4, (3y+1)/4.

For row 4 they are (3y+3delta+1)/4 and (3y+2)/4. Their stated parities
follow from the two modulo-four guards. The upper endpoint remains larger
until the final meeting. Every lower source remains positive.

### Termination and exact pullback of the guard

Each nonterminal gap is strictly reduced. More quantitatively, delta'-1
is at most (3/4)(delta-1), so at most K nonterminal stages suffice; they
cost at most two steps each. The final stage costs three.

For an explicit recursive compiler, start at gap 1 with c=4, M=8 and
F=100, G=001. Given a compiled smaller-gap residue c modulo M:

* even delta: replace (c,M,F,G) by (2c,2M,0F,0G);
* delta=1 mod4: use c'=(4c-1)3^(-1) mod 4M, M'=4M,
  F'=01F, G'=10G;
* delta=3 mod4: use c'=(4c-2)3^(-1) mod 4M, M'=4M,
  F'=10F, G'=01G.

The inverse of three exists modulo the dyadic modulus. The first two odd-gap
pullbacks automatically give c'=1 or 2 modulo4, respectively. All residues
are positive; the even pullback preserves this, and the odd pullbacks cannot
be zero. Induction proves the full class, its parity legality, and the
merger. The class is exact for the particular generated word pair, not a
classification of every possible merger at that gap.

**What this adds.** A fixed difference between two aligned affine shadows
no longer requires a bespoke proof for that difference. The compiler supplies
one candidate guard and certificate for every positive integer difference.
Its guard can still fail for a given input. The base countercontrol y=1,
delta=1 is the permanent raw phase pair (2,1), not a uniform merger.

## 4. AUA-004: every finite parity pattern has a smaller-shadow subfamily

Let w be any nonempty word with length L and q>=1 odd bits. Let r be its
canonical source residue, 0<=r<2^L, and let e=T^L(r). Since q>=1, r>0,
e>=1. For t>=1 define

    n=2^L t+r, m=2^q t-1.

The actual prefixes w and 1^q reach

    T^L(n)=3^q t+e, T^q(m)=3^q t-1.

Their fixed gap is delta=e+1. Compile it by Section 3 and impose

    t=(c_delta+1)(3^q)^(-1) mod 2^ell.

This is one nonempty arithmetic progression of positive t. For every member,

    T^(L+ell)(n)=T^(q+ell)(m),
    0<m<n/2^(L-q).

Indeed 2^(L-q)m=2^L t-2^(L-q)<n. The all-even word q=0 has direct
ordinary descent and does not need this construction.

Therefore **no finite parity template is excluded from the construction's
syntax**: every one admits an explicitly certified shadow subfamily, including
nonperiodic words. This does not show that every source in a parity cylinder
satisfies the extra guard. It also does not show that a prescribed source
will encounter such a subfamily while retaining the original-root order.
The familiar fact that one can append many even steps to force descent is
not being claimed as a new density theorem; this construction instead gives
an exact paired certificate with a smaller odd-run source.

## 5. AUA-005: two resonant shorter shadows, including an entire old failure family

### General direct and complementary transitions

Take n=8^k u-5 with k>=1 and u positive odd. Let d be either 1 or 3, assume
j=2k-d>=1, and set

    m=2^j u-1, Z=3^j u,
    s=v2(Z+1)-d-2 >=0, b=(Z+1)/2^(s+d+2).

Then b is positive odd. The essential identity is

    3^d+5=2^(d+2), for d=1 and d=3.                  (R)

After the prefixes (110)^k and 1^j, the original and shadow states are
(3^d Z-5,Z-1). Now

    3^d Z-5 = 2^(d+2)(3^d 2^s b-1),
    Z-1     = 2(2^(s+d+1)b-1).

Thus 0^(d+2)1^s and 0 1^(s+d+1) lead to

    U=3^(s+d)b-1, V=3^(s+d+1)b-1=3U+2.

All states are positive; s=0 simply omits an odd block. If

    3^(s+d+1)b=1 mod4,                              (GOOD)

then U=2 mod4 and V=0 mod4. Appending 01 and 00 merges at
E=(3^(s+d+1)b-1)/4. In full,

    F=(110)^k 0^(d+2)1^s01,
    G=1^(2k-d)0 1^(s+d+1)00,

    T^(3k+s+d+4)(n)=T^(2k+s+4)(m)=E.               (8)

If (GOOD) fails, the tails 00 and 01 give the swapped H pair

    (D,9D+2), D=(3^(s+d)b-1)/4>0.                   (9)

Consequently any actual successful hard-return itinerary from the parent
AHR theorem may be appended, retaining the swapped orientation and both
original clocks. Failure of that return guard is not success.

The source order is independent of all intermediate states:

    m=(n+5)/2^(k+d)-1<n.

For these feasible k,d, 0<m<n; directly, n-m=(8^k-2^(2k-d))u-4 is positive,
including k=d=1. When 2^(k+d)>5, the stronger bound m<n/2^(k+d) holds.
This factor grows with the original burst length.

### The whole certified forward arm can remain above n

A sufficient uniform condition for (8) to have T^i(n)>n for every positive
i on its entire displayed original arm is

    9^k >= 2^(d+3)8^k.                             (10)

During the initial repeated 110 blocks, every state exceeds the original
source, by their expanding positive block identity. After these blocks put
W=(9^k u-5)/2^(d+2). The following odd block only increases values. Its final
01 tail has minimum U/2>=W/2. Every intermediate division leading to W is
also >=W. Hence the whole remaining arm is at least

    W/2=(9^k u-5)/2^(d+3)>8^k u-5

under (10). The last inequality has a nonnegative leading coefficient and
positive constant 5(1-2^(-d-3)). For d=1, k>=24 suffices; for d=3, k>=36
suffices. These are sufficient thresholds, not optimized for every input.
This bound is for the direct merger, not automatically for appended returns.

For each feasible k,d and each s>=0, the conditions on u are constructive:

    3^(2k-d)u+1 = 2^(s+d+2)b0 mod 2^(s+d+4),
    b0=3^(s+d+1) mod4 in {1,3}.

An additional u=1 mod3 for odd k, u=2 mod3 for even k, gives n=3 mod12.
CRT yields infinitely many positive odd inputs for every k,d,s. At 3|n,
the only positive depth-a pure ancestor is 2^a n: the odd inverse fails
integrality at every depth. Thus (8) and (10) can coexist with no smaller
pure ancestor and no forward descent on the entire certified original arm.

### Strict extension: every member of this subfamily defeats the previous selector

Now fix **arbitrary k>=1 and s>=2**, take d=1, and strengthen the quotient
guard to

    3^s b=5 mod8.                                  (ESC)

This implies (GOOD), since 3^(s+2)b=1 mod4. It is realized for every k,s by

    3^(2k-1)u+1 = 2^(s+3)b0 mod2^(s+6),
    b0=5*3^(-s) mod8,

together with the same modulo-three specialization when desired.

To compare exactly against #126, put v=9^(k-1)u. Then 3v+1=2^(s+3)b
implies v=5 mod16. The parent's selector therefore used its a=3 companion
and even adjacent parameter

    q=(9v-13)/8=3*2^s b-2.

Its valuation is one. The odd run from q/2 has length s-1 and ends at
3^s b-1, divisible by four. Thus the old rule enters

    H(C), C=(3^s b-1)/4.

By (ESC), C is odd. Hence v2(C+2)-1=-1, outside the parent's r>=3 return
rule. The later gap-four shortcut in #126 does not apply: v=5 mod16,
whereas that shortcut requires v=13 mod32. Nor is this the missing-seed case.
Therefore **the actual published #126 selector returns OUTSIDE_RETURN on
EVERY source in (ESC)**. The new shadow gives (8) directly on every member.

This is a strict all-parameter extension of that particular selector, not
just more successful samples. It does not claim that every older programme
lacks some other certificate for these inputs. The modulo-three subfamily
also avoids the elementary smaller-pure-ancestor explanation.

Example with k=24,s=2,u=29:

    n=136948628003219711197179,
    m=4081387162304511,
    T^79(n)=T^54(m)=487946288509306056429779,
    min_(1<=i<=79)T^i(n)=154067206503622175096827>n,
    2^25*m<n, n=3 mod12.

The old H parameter is 54216254278811784047753, which is odd. The new
certificate does not continue that failed pair; it changes the shadow.

A second resonant example, d=3,k=36,s=1,u=5:

    n=1622592768292133633915780102881275,
    m=2951479051793528258559,
    T^116(n)=T^77(m)=3960070232508839252081275993612379,
    min_(1<=i<=116)T^i(n)=1825416864328650338155252615741435>n,
    2^39*m<n.

Its scope is the d=3 resonance, not the special d=1 strict-failure theorem.

## 6. AUA-006: complete finite-budget classification of an odd-shadow menu

For n=8^k u-5, consider EVERY shadow of the form m_j=2^j u-1 with j>=1
and 0<m_j<n. Necessarily j<3k; within that finite interval retain the exact
inequality (the smallest n=3 rejects j=2). Set

    d=2k-j, Z=3^min(2k,j)u,
    A=3^max(d,0), B=3^max(-d,0).

The actual prefixes reach (AZ-5,BZ-1) at clocks 3k and j. These are all
odd-run shadows with the same u, NOT all possible smaller sources or all
periodic patterns. This explicit menu allows both shorter and longer odd
runs when their original source remains smaller.

### Why the uniform tail classification is synchronous

Suppose two fixed tail words of lengths a,b merge for infinitely many Z.
Comparing affine leading coefficients gives

    A*3^q/2^a = B*3^s/2^b.

Since A,B are odd powers of three, a=b. This is the parent's clock-rigidity
lemma applied after the already different prefix clocks. Individual isolated
meetings with a!=b are not ruled out. Neither arbitrary variable-length
tails nor arbitrary other companions are ruled out.

### The exact cylinder tree

For a fixed d and tail budget H, start with all odd Z=1+2t. Store the two
endpoint affine functions of t and their actual word prefixes. At a node:

* if the two affine functions are identical, record a uniform merger leaf;
* if their slopes differ, solve their linear equality and retain any positive
  integer parameter giving positive original endpoints as an isolated meeting;
* unless the budget is exhausted or a uniform merger occurred, split the
  parameter class into its two parity lifts when required and advance both T
  branches exactly; at the budget retain the complete frontier.

Every split is exhaustive and disjoint, and every advance is the actual
shortcut map on its whole cylinder. Induction proves that the uniform leaves
plus the final frontier partition all odd Z. The additional singleton list
records accidental meetings inside otherwise nonidentical affine cylinders;
recording one point does not justify pruning its whole class.

Consequently this is a **complete classification of synchronous meetings at
or before H for the specified fixed d**: the recorded uniform classes and
isolated points contain every such positive input. The uniform leaves are
prefix-free. For a uniform leaf its constant word-pair equality is verified
as an affine identity, not by testing representatives. The frontier is kept,
not silently labelled impossible. When a singleton has already merged at an
earlier depth, retain its earliest certificate.

The delivered atlas uses d=-5,...,11 and H=18. This covers the complete
admissible j menu for every k=1,...,6 in the comparison grid. At larger k
this finite atlas covers only its declared shift interval; the unbounded
resonance theorem is applied separately. Its success criteria are not
exhaustive over all shadows, longer tails, or unequal-clock point meetings.

This is a finite certified search/classification result, not a theorem that
its frontier vanishes as H increases. The syntax can describe every step;
that does not show every original source has a successful path through it.

## 7. Evidence and interpretation

The native generator propagates affine functions on dyadic cells. The separate
verifier reconstructs the cells with whole-word odd counts and affine
numerators, checks each uniform leaf symbolically, checks isolated positive
meetings physically, and verifies the dyadic partition. It imports no kernel,
generator, or repository module. Its fixed-gap compiler accumulates forward
congruences instead of reversing the gap recursion; its strict-family CRT
solves for the odd quotient b instead of u. Same-author implementation diversity
is not independent mathematical review.

The compact canonical artifact binds the full atlas, frontier hashes, every
finite input classification, and every family row. Full rows regenerate with
`run.py --full PATH`. The comparison with #126 is a separate baseline check,
not a proof premise and not an exhaustive comparison with the whole project.
The exact counts and command outcomes are in the validation and comparison
receipts. No full-repository validator or external formalization is implied
by a standalone replay.

## 8. The next real obligation

There are now a universal entry identity, a complete countable transition
grammar, a compiler for every fixed gap, all-prefix shadow subfamilies, and
new unbounded classes bypassing a proved failure of the previous selector.
None establishes unavoidable successful entry for one arbitrary fixed root.
A least-counterexample argument must still prove that at least one of the
available ORIGINAL smaller shadows succeeds, or supply a different globally
well-founded mechanism. Choosing a new shadow after seeing a failure is safe
only with a fresh original-root inequality and physical certificate.

The next useful target is an arithmetic incompatibility between simultaneous
failures of several shadows, not merely a longer successful-list construction.
The complete finite atlas supplies exact residual classes for that question.
Do not replace it with an assertion that a larger library must eventually
cover every integer; this pass proves no such theorem.

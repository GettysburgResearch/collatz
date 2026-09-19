# Adaptive companions: remove the second-exit restriction before extending it

**Status: PROPOSED pending independent mathematical review.**
Date: 2026-09-19. Programme: #121. Parent: #123 at
`bf0696f888442c82a4c6cdc1df36becf8550295a`.
All AAC statements below are new proposed statements, not inherited review.
No complete Collatz proof or external priority claim is made.

Use the raw shortcut map T(n)=n/2 for even positive n and (3n+1)/2 for odd n.
Raw T continues around 1 -> 2 -> 1; a certificate records each arm's own clock.
A word lists the actual source parities in chronological order.

The main result is simpler and broader than extending the previous fixed
companion indefinitely. Replacing n/3-2 by a different, still smaller source
removes ALL second-exit and hard-return requirements on the old entry domain.
The previous one-third reduction is stronger in its target size; its long
return analysis is unnecessary for obtaining some lower-source certificate
there. The return mechanism remains useful on genuinely new entry classes.

## 1. AAC-001: clock rigidity for uniform affine certificates

Let n(t)=At+B and m(t)=Ct+D with positive integers A,C. Suppose fixed finite
physical words w,z, of lengths l,j and odd counts q,s, give a shared endpoint
for infinitely many integer t. The affine formula for a parity word gives

    (3^q(At+B)+a_w)/2^l = (3^s(Ct+D)+a_z)/2^j.

An affine function vanishing at infinitely many points vanishes identically.
Comparing slopes, then their 2-adic valuations, gives

    A/C = 2^(l-j) 3^(s-q),
    l-j = v2(A)-v2(C).                                    (1)

Likewise q-s=v3(C)-v3(A), and A/C has no prime factors other than 2 and 3.
This is a necessary condition, not a sufficient legality/merger test.
Rational positive coefficients give the same statement with rational valuations.

For the old pair (9C+2,C), a uniform affine-word merger necessarily has equal
clocks. Merely allowing an arbitrary fixed nonzero clock offset cannot produce
such a family for those same companions. This does NOT prohibit individual
unequal-clock meetings, unbounded changing words, or different companions.
The parent's 3003/999 example indeed meets at unequal clocks 29/34, but never
at equal clocks. No source is declared divergent from a failed synchronization.

This observation directs the construction: change the smaller companion's
slope, not just the amount of time spent searching with a fixed slope.

## 2. AAC-002: preserve the original root through an expanding block

Write

    n=8^k u-5,  k>=1, u positive odd,  v=9^(k-1)u.

These parameters are read from a given source whenever v2(n+5) is a positive
multiple 3k; u=(n+5)/8^k. This does not represent every positive source.
For a positive integer a<8 set

    m_a=a*8^(k-1)u-5.

Whenever m_a>0, n and m_a each follow k-1 copies of 110, reaching

    N=8v-5,  M_a=av-5.

Indeed, for every positive integer A,

    8A-5 --1--> 12A-7 --1--> 18A-10 --0--> 9A-5.           (2)

At every intermediate complete block the required multiple of 8 remains.
Any physical seed comparison between N and M_a therefore lifts by prefixing
(110)^(k-1) on BOTH arms. Its root inequality is immutable:

    n-m_a=(8-a)*8^(k-1)u>0.                              (3)

In particular, the three companions used here are

    a=6: m_6=(3n-5)/4,
    a=3: m_3=(3n-25)/8,
    a=1: m_1=(n-35)/8.

Positivity follows on the individual seed domains below. A reduction of a
large intermediate state alone would not imply (3); the source companion
is chosen and compared with n before the excursion begins.

## 3. AAC-003: the whole former entry domain has a short asynchronous merger

### Theorem

For EVERY k>=1 and positive odd u satisfying

    v=9^(k-1)u = 7 mod16,

or equivalently

    16 divides 9^k u+1,

the following is a physical lower-source certificate:

    F=(110)^k 0100,
    B=(110)^(k-1) 10001,
    E=(3*9^k u-13)/16,

    T^(3k+4)(n) = T^(3k+2)((3n-5)/4) = E,
    0<(3n-5)/4<3n/4.                                   (4)

There is no second-exit condition, no specified further odd run, no finite
list of hard labels, and no assumption about convergence of either source.

### Proof on the entire seed cylinder

Write v=7+16t, t>=0. The exact physical states are

    N: 128t+51, 192t+77, 288t+116, 144t+58,
       72t+29, 108t+44, 54t+22, 27t+11;

    M_6: 96t+37, 144t+56, 72t+28, 36t+14, 18t+7, 27t+11.

Their words are 1100100 and 10001. Every parity and positivity is uniform
for t>=0. Prefixing (2) proves (4), and (3) supplies the original-root order.
The clock difference is two, as (1) requires for the slope ratio 8/6.

### Precise relation to #122 and #123

Both previous packets' entry hypotheses required

    h=v2(9^k u+1)-4 >=1.

That implies v=7 mod32, hence v=7 mod16. Thus EVERY input in that entry
domain has (4), whether the old second exit was good or hard, whether the
old return language succeeded or failed, and regardless of the old fixed
companion's synchronous phase. The additional class v=23 mod32 has h=0 and
is covered as well. This is an algebraic inclusion, not a finite-census inference.

The old conclusions remain correct within their stated guards. They supply
m<n/3 in a narrower region; this result generally supplies only m<3n/4.
It would be incorrect to retain the old one-third inequality for m_6.

### Examples

    T^10(3003)=T^8(2251)=713.

The old companion 999 need not be used. Its 29/34 meeting at 1 remains a
valid individual unequal-clock certificate; its lack of equal-clock meeting
is not contradicted by changing the companion.

For k=23,u=343, the previous large source now has

    n=202471462953036038537211,
    m=151853597214777028902907,
    T^73(n)=T^71(m)=569997707820151476731933.

The original, longer one-third certificate remains a separate certificate.

## 4. AAC-004: no forward descent on the new arm at every guarded k>=15

For every input of (4) with k>=15,

    T^j(n)>n for EVERY 1<=j<=3k+4.                        (5)

Each of the first k-1 complete 110 blocks strictly increases its initial
value, and each intermediate value exceeds that block's starting value,
by (2). On the final seven-step seed bridge the smallest state is E for
v>=7. Directly,

    E-n=((3*9^k-16*8^k)u+67)/16.

The integer inequality 3*9^15>16*8^15, preserved by a further factor 9/8,
makes this positive for k>=15. This is a sufficient uniform cutoff, not a
claim of optimality for each source. The coefficient has the opposite sign
at k=14, so the displayed sufficient bound cannot simply use 14.

There are infinitely many such inputs divisible by 3 for every k. Choose

    u = 7*9^(-(k-1)) mod16,
    u = epsilon mod3, epsilon=1 for odd k and 2 for even k.

CRT gives a positive odd residue class modulo 48. Then n=3 mod12. Its only
positive depth-b pure ancestor is 2^b n: an odd inverse would require
(2n-1)/3 integral, and the even inverse preserves divisibility by 3.
Thus no smaller pure ancestor exists at ANY depth. This fact and (5) coexist
with the two-sided lower-source certificate (4).

An exact small-threshold example is k=15,u=7:

    n=246290604621819, m=184717953466363,
    T^49(n)=T^47(m)=270232110874226,
    min_(1<=j<=49) T^j(n)=270232110874226>n.

This excludes neither later forward descent nor shorter different diagrams.

## 5. AAC-005: three companions give an explicit seed-exit decomposition

The selected companion depends on v. On SEVEN of the eight odd residue
classes modulo 16 it has a finite, explicitly determined path to either a
merger or the SAME return pair H(C)=(9C+2,C) used by #123:

| Seed domain | a | Smaller original source | Seed bridge |
|---|---:|---|---|
| v=3 mod4, or v=9 mod16 | 6 | (3n-5)/4 | (N,M_6) reaches (q+1,q), q=(9v-7)/2, at clocks 4/2 |
| v=5 mod16 | 3 | (3n-25)/8 | (N,M_3) reaches (q+1,q), q=(9v-13)/8, at clocks 6/3 |
| v=13 mod16 | 1 | (n-35)/8 | Direct eight/five-step merger or H return, below |
| v=1 mod16 | none | none asserted | OUTSIDE_SEED |

The domains are disjoint after using the indicated combined first row.
The first row has q even or q=5 mod8; the second has q even.
They exhaust the seven asserted residues, not all sources or all mergers.
Entering H(C) is NOT a successful reduction certificate by itself.

### 5.1 The two adjacent bridges

For all odd v, the physical words 1100 from 8v-5 and 10 from 6v-5 reach
((9v-5)/2,(9v-7)/2). On the selected domain q is positive and has the stated
parity. Positivity of M_6 follows already from v>=3 on this domain.

For v=5 mod16, the words 110000 and 010 from 8v-5 and 3v-5 reach
((9v-5)/8,(9v-13)/8). Here q is positive even and M_3>=10.
These assertions follow by the displayed affine expressions or substitution
v=5+16t; no additional future parity is assumed.

### 5.2 Every positive even adjacent parameter has a finite exit

Compare (q+1,q) with positive even q.

If v2(q)=2, write q=4b, b odd. Words 100 and 001 merge at (3b+1)/2.
If v2(q)>=3, write q=8D. Words 101 and 000 reach (9D+2,D).

If v2(q)=1, put b=q/2, s=v2(b+1)>=1, d=(b+1)/2^s odd, and B=3^s d-1.
One step takes the pair to (3b+2,b). Throughout the following s odd steps
it retains the form (3x+2,x). Thus it reaches (3B+2,B), with B even.

* If B=2 mod4, words 1^(s+1)00 and 0 1^s 01 merge at (3B+2)/4.
* If B=0 mod4, words 1^(s+1)01 and 0 1^s 00 reach (9D+2,D), D=B/4.

The total clock in either case is s+3 on each adjacent arm. The odd-run
length is read from the actual parameter and is always finite, not bounded
by a universal constant. Positivity of D in the return case follows from
positive B divisible by four. The smallest possible merging endpoint is positive.

For the a=6 seed row, v=3 mod8 is precisely this unbounded-run case.
Writing s=v2(3v-1)-2>=1 and w=(3v-1)/2^(s+2), its merging condition is
3^s w=1 mod4. These inputs had old entry h=-2, outside both earlier packets.
The case v=15 mod16 returns directly with C=(9v-7)/16 and has old h=-1.
The case v=7 mod16 is exactly the direct merger (4), with old h>=0.

### 5.3 Every adjacent parameter q=5 mod8 has a finite exit

Put b=(q-1)/4 positive odd, s=v2(b+1)>=1, d=(b+1)/2^s odd.
The upper q+1 reaches 2b+1 after one even step. On the lower arm,
T^3(4b+1)=T(b); all three steps are physical because b is odd.
Use the actual odd runs of 2b+1 and b, of lengths s+1 and s.

If 3^(s+1)d=1 mod4, the words

    upper: 0 1^(s+1)00,
    lower: 100 1^(s-1)01

merge at E=(3^(s+1)d-1)/4. If 3^(s+1)d=3 mod4, replace the final tails
by 01 and 00, respectively. They reach (9C+2,C), C=(3^s d-1)/4.
Both clocks are s+4. The s=1 endpoint has an empty 1^(s-1) block.
All integrality and positivity follow from the stated residue alternative.
This is the a=6 domain v=9 mod16, formerly outside the entry guard.

### 5.4 The one-eighth companion

For v=13 mod16, let z=(v-5)/8 be positive odd. The words 110000 and 000
from N and M_1 reach (9z+5,z), at seed clocks 6/3.
If z=3 mod4, tails 00 and 11 merge at (9z+5)/4.
If z=1 mod4, tails 01 and 10 reach (9C+2,C), C=(3z+1)/4.
The complete seed clocks are 8/5, and M_1>=8.
This splits the domain into v=29 mod32 (merge) and v=13 mod32 (return).

### 5.5 Composition and clocks

Prefix all seed words by (110)^(k-1), then apply the #123 return mechanism
whenever its actual guard holds. Recall it explicitly: for
C=2^(r+1)b-2, b positive odd, r>=3, after r+3 steps each,

    good 3^r b=1 mod4: the arms merge at (3^r b-1)/4;
    hard 3^r b=3 mod4: the pair becomes (D,9D+2), D=(3^(r-1)b-1)/4.

A hard return swaps orientation; the original source labels and their
independent clocks are retained. Subsequent equal increments preserve the
clock difference two for a=6 and three for a=1 or a=3. On merger, (3)
proves the original-root induction edge, regardless of intermediate growth.

A bounded procedure returns MERGE, OUTSIDE_SEED, OUTSIDE_RETURN, or
BUDGET_EXHAUSTED. Its total finite execution is not total successful coverage.
Neither a returned H pair nor exhaustion is accepted as a merger.

## 6. AAC-006: old hard-return compositions now lift from a NEW entry domain

For any nonempty finite list r_1,...,r_J with r_i>=3, the parent's exact
compiler gives one class C=c mod M, M=2^sum(r_i+3), on which the actual
itinerary has J-1 hard returns followed by a merging exit.
A self-contained compiler is: for the final label choose
c=2^(r+1)b0-2, M=2^(r+3), b0=3^r mod4 in {1,3}. Working backwards through
a hard label, put d=2^(r+3), c0=2^(r+1)b0-2, b0=3^(r+1) mod4,
D0=(3^(r-1)b0-1)/4, A=3^(r-1), and replace

    c by c0+d*((c-D0)*A^(-1) mod M),  M by d*M.

The inverse exists because M is dyadic and A odd. This proves exactness by
induction: a hard successor of c0+d*t is D0+A*t.

Now use the new a=6 seed return on v=15 mod16, C=(9v-7)/16. Pulling back
that exact class gives

    v = (16c+7)*9^(-1) mod 16M.                         (6)

The residue is 15 mod16; hence every input constructed here has old h=-1,
not old h>=1. For ANY k>=1, solve v=9^(k-1)u in (6) and additionally
u=1 mod3 for odd k or u=2 mod3 for even k. CRT supplies infinitely many
positive odd u, all with n=3 mod12. A successful pattern of total return
clock Q=sum(r_i+3) gives

    T^(3k+4+Q)(n) = T^(3k+2+Q)((3n-5)/4).               (7)

Every finite label list is allowed; lists of arbitrarily many 8s followed
by 4 retain arbitrarily many growing hard returns. The source changes when
the prescribed list changes. No infinite ordinary itinerary, eventual entry,
or all-source theorem follows from these finite constructions.

There are also arbitrary-length immediate-merger families in Sections 5.2
and 5.3 and in the a=3 row. For a prescribed s>=1 their seed classes are:

    a=6, even q: v=(3+2^(s+2)d0)*9^(-1) mod2^(s+4);
    a=6, q=5 mod8: v=(1+2^(s+3)d0)*9^(-1) mod2^(s+5);
    a=3, even q: v=(-3+2^(s+4)d0)*9^(-1) mod2^(s+6);
    d0=3^(s+1) mod4 in {1,3}.

Each congruence specifies the exact odd-run length and merging alternative.
Solving v=9^(k-1)u and the same modulo-three condition gives positive
ordinary families with k and s independently unbounded. The assertions in
Section 5 apply to arbitrary given sources satisfying the guards; these
constructions establish non-vacuity, not universal applicability.

## 7. Scope, least-counterexample meaning, and next task

A least positive nonconvergent root cannot have any certificate
T^a(n)=T^b(m) with 0<m<n. Repeating certified source reductions terminates
under ordinary value. To conclude Collatz this way one still needs successful
coverage, not merely a terminating call that can return an unresolved status.

The user's eventual-entry interpretation requires this additional care:
if a later, larger orbit state enters a local rule with a smaller local
companion, that companion may still be larger than the ORIGINAL root.
An eventual-entry proof must retain the original-root inequality, establish
a composed inequality, or use a separately proved common well-founded order.
All successful certificates here retain the original root explicitly.

What changed is not merely the number of successful examples. A different
companion eliminates a restriction previously responsible for arbitrarily
long return analyses on the entire old entry region. The full seven-residue
seed decomposition then reuses those return analyses outside their previous
entry region. Old proofs are preserved and their stronger target factors are
not silently transferred to the new companions.

Still open: v=1 mod16 in this seed selector; H states outside r>=3; infinite
hard-return itineraries; sources outside the 8^k u-5 odd-u representation;
and an unavoidable original-root-compatible covering theorem. Seven of eight
seed residues reaching a merger OR a return is not seven eighths of Collatz
solved. Finite grids, residue densities, and smaller intermediate states do
not establish eventual coverage.

The next useful attack is to select companions jointly with the exit state
and compare the remaining parameter restrictions, rather than treating the
fixed-companion H return process as an obligatory part of every proof.

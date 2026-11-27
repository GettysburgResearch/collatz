# Polynomial-width exact-clock bands and a cofinal finite test

**Status: PROPOSED written mathematics; full Collatz OPEN.** The
unconditional construction below uses only the elementary inverse
router and finite simple-path estimate of earlier packets. The
stronger density and long-block conclusions explicitly assume the
source-qualified joint inverse floor F and, for blocks, synchronization S.
The new Lean source is a candidate, not compiled.

## 1. Setup and exact retained objects

Use T(n)=n/2 for even n and (3n+1)/2 for odd n; U is the accelerated
odd map. A unit means a positive odd integer not divisible by three.
For an actual path with k odd departures and s shortcut steps, write
its exact affine identity as

    T^s(x) = 3^k 2^(-s) x + beta.

Here beta>=0 is the additive offset, not a multiplicative error. For
a complete accelerated gap, beta changes to (3 beta+1)/2^e. Each
even shortcut halves beta and each odd shortcut sends it to
(3 beta+1)/2. Therefore, over ANY physical prefix with m odd inputs,

    beta+1 <= (3/2)^m                         (1)

when the initial offset is zero. This counts odd inputs, not all
physical steps.

Freeze a positive ordinary unit a, and put q_i=U^i(a), A_i equal to
the total physical clock of these i odd gaps. Suppose that a does not
reach 1. All q_i are units >=5, whether or not the orbit repeats.
Multiplication of the actual gap equations gives

    2^A_i q_i = a prod_(j<i)(3+1/q_j)
                <= a (16/5)^i.
    L_i := 2i-A_i >= i log_2(5/4) - log_2 a.     (2)

The suffix from a to q_i has relative additive offset at least

    epsilon_a = 1/(3a+1)                        (3)

for i>=1, because its correction product contains the first factor
1+1/(3a). Appending this suffix to any actual path ending at a
preserves this lower bound on the full relative carry at q_i.

At a proposed balanced row with b odd inputs and 2b shortcuts,
write k=b-i and S=2b-A_i=2k+L_i. The pre-gate clock must therefore
be exactly S. Define the rational center

    Z_(b,k) = a 2^S/3^k.                        (4)

Unlike PR201's previous elementary amplification, k will be only
logarithmic (or more generally sublinear) in b. The entire remaining
clock budget is absorbed by ONE long legal odd gap just before a.
We keep the ordinary integer a and its actual suffix unchanged.

## 2. Unconditional logarithmic-depth source bands

Let k tend to infinity, with k=o(b), and i=b-k. For integers h,J>=1
satisfying

    3^(2(h+J)) <= k,                             (5)

fix ANY odd residue r modulo 2^h and ANY unit residue v modulo 3^J.
For every sufficiently large b (uniformly in a given menu of k
satisfying the stated bounds), there are at least

    2^(k-h-3)                                  (6)

distinct ordinary unit sources x in this mixed cylinder with

    U^b(x)=q_i, physical clock=2b,
    relative carry >= epsilon_a,
    Z_(b,k)-2^(8k) <= x < Z_(b,k).               (7)

All these sources visit the same gate a at the SAME physical clock S
and the SAME odd depth k. The padding exponent can be chosen once
for the band and h, independent of r,v and of the inverse tree word.

### The long pad

Choose e in the six consecutive integers

    [S-h-8k-5, S-h-8k]

so that 2^e a=4 or 7 modulo 9. Such a choice exists since the order
of 2 modulo 9 is six. It is positive for large b by (2) and k=o(b).
The unit z=(2^e a-1)/3 has exact forward gap e to a. Put

    t=S-h-e, so 8k <= t <= 8k+5.

This leaves a common middle physical budget independent of the
initial word. We will construct a path from the endpoint y of the
initial h shortcut steps to this actual z.

### The exact source residue

The prescribed binary cylinder determines the entire initial h-bit
parity word and its odd count p, with 1<=p<=h. Its full carry C
satisfies

    2^h y=3^p x+C.

To impose the additional ternary class v, require

    y = 2^(-h)(3^p v+C) mod 3^(p+J).             (8)

This is a unit residue since the contribution of the last odd
departure is a unit modulo 3 and earlier odd contributions contain
a factor 3. Every positive odd y in this class yields the integral
source x=(2^h y-C)/3^p, with x=v mod 3^J.

The full integer identity guarantees the literal prescribed path:
peel the last shortcut. For a last odd bit reduce modulo 3 to
obtain 2y-1 divisible by 3, take the positive odd integer
(2y-1)/3, and cancel that last step from the affine equation.
For a last even bit take 2y and cancel a factor 2 in the clock.
Iterate. Positivity and each required source parity are preserved.
The unique binary residue of the word modulo 2^h is r, so x also
has the required binary class. No independence of the two moduli
is assumed.

### The middle word at an exact clock

The middle odd depth is n=k-p-1. Put m=n-2=k-p-3. Grow the
ordinary inverse tree backwards from z for m odd gaps. At every
unit there are exactly two legal unit inverse choices among
exponents 1,...,6. Every branch has total E<=6m.

The remaining two chronological gaps have total t-E>=2k.
By PR201's two-gap router, at any supplied ordinary unit endpoint
w and any prescribed unit class rho modulo 3^K, a legal pair of
gaps with total u exists as soon as

    u >= 2*3^(K+1)+1.

For clarity, write the gaps f,u-f. The exact equation is
9x=2^u w-2^f-3. Choose 1<=f<=2*3^(K+1) by the discrete log

    2^f = 2^u w-3-9rho mod 3^(K+2).

The right side is a unit, and 2 has full order modulo this power
of 3. The intermediate inverse is integral, positive, odd and
a unit by the equation; the source is in the prescribed unit class.
This is the exact router already proved in PR201; no new priority
is claimed for it.

Apply it with K=p+J and the residue (8). Condition (5) implies
2*3^(K+1)+1<=6 sqrt(k)+1<=2k for large k. Thus every one of
the 2^m tree words can be completed with the same t. The middle
has exactly n gaps, is literal, and ends at z. The complete
source then visits a after h+t+e=S physical steps and
p+n+1=k odd departures, and q_i after 2b shortcuts and b odds.

Different tree words give different x because a supplied x
determines its initial h steps and then its unique forward
accelerated gaps at the fixed split positions. This proves (6).
Appending the unchanged actual suffix proves the carry bound (3).

### The real-width improvement

Let beta0 be the offset just before the padding gap, after h+t
physical steps. Exactly k-1 odd inputs have occurred. By (1),

    3 beta0+1 <= 3(3/2)^(k-1).

The offset at a is (3 beta0+1)/2^e, hence

    Z_(b,k)-x
      = (2^(h+t)/3^k)(3 beta0+1)
      <= 2^(h+t-k+1)
      <= 2^(7k+h+6)
      <= 2^(8k)

for all sufficiently large k, since h+6<=k. It is positive.
This explains the essential difference from a full inverse row:
the enormous pad clock cancels out of the additive source width.
All cells share this SAME narrow real interval.

## 3. A polynomial-in-b finite test equivalent to Collatz

Set K_b=floor(log_2 b)+1 for b>=1 and take the menu
K_b<=k<=2K_b. Choose h=h(k) as the greatest integer h>=1 with
3^(2(h+1))<=k, omitting k if no such h exists. Set J=1.

For every b and rational 0<epsilon<1 define the finite test B_b(epsilon).
Search units g<=K_b, k in this menu, and integers 0<=S<=2b.
For the rational center Z=g 2^S/3^k, inspect the positive odd unit
integers x in [Z-2^(8k),Z). A band succeeds if there exists one
common unit endpoint q>1 such that, for every odd residue r
modulo 2^h and both residues v=1,2 modulo 3, at least
2^(k-h-3) distinct x in that band and cylinder satisfy:

* T^(2b)(x)=q, with exactly b odd inputs;
* 3^b x <= (1-epsilon) 4^b q;
* q>K_b OR a state repeats within the recorded path, including
  the terminal state.

Return true if at least one band succeeds. The tested sources
need not be assumed to visit the center's parameter g; allowing
any source satisfying the finite conditions only makes the test
stronger. The lower construction DOES visit g=a at clock S.

**Theorem.** Full Collatz is equivalent to

    for every rational 0<epsilon<1,
      B_b(epsilon) is false for arbitrarily large b.       (8a)

If Collatz is true, each fixed epsilon test is actually eventually
false. If Collatz fails, for one fixed epsilon>0 there are at least
K_b/2 pairwise disjoint successful bands at EVERY sufficiently
large b, with the same fixed center parameter a. On an escaping
orbit their endpoints are distinct; in the cycle case a prescribed
cycle vertex is obtained on a positive fraction of the menu.

**Proof of the lower alternative.** Use Section 2 with k in the
menu and g=a. Eventually a<=K_b. Every endpoint is nonconvergent
and >1. If the ray escapes, its q_i are distinct. The elementary
finite-simple-path estimate S0 below bounds the number of its
odd sites <=K_b by 5 K_b^(39/40)=o(K_b). Thus at least K_b/2
menu choices have q_i>K_b. If the ray enters a nontrivial cycle,
the common suffix already contains a repetition for large b.
For any particular cycle vertex of odd period p0, at least
floor((K_b+1)/p0) menu indices have that endpoint when b is large.
Every band for such indices has all the required witnesses.

The centers are not equal for different k: unique factorization
prevents 2^(S-S')=3^(k-k') when k differs. More quantitatively,

    |a 2^S/3^k-a 2^S'/3^k'|
          >= a 2^min(S,S')/3^max(k,k').                    (9)

Indeed factor out the right side and the remaining difference
is a nonzero integer. By (2), S>=c b for all these choices with
one absolute c>0 and sufficiently large b. Meanwhile k<=2K_b
and all additive widths are polynomial in b. Hence these intervals
are pairwise disjoint eventually. This also separates bands with
the same periodic endpoint. No logarithmic-forms theorem is needed.

**Proof of eventual false under convergence.** Use the resident
elementary estimate S0: along a finite simple ordinary path,
the number of distinct odd states <=X is at most 5X^(39/40).
Consequently the sum of reciprocals of odd departures all >=M
is at most 200 M^(-1/40). This is T-A3-651 in main, whose
elementary proof was reconstructed in PR201's escape-analysis.
For any fixed epsilon choose M so large that
(200/3) M^(-1/40)<epsilon. A simple path with relative carry
>=epsilon must visit some odd state below M, since its correction
product D satisfies 1-1/D<=log D<=sum 1/(3x_j).
Under Collatz every such small gate has a finite forward orbit,
and the union of these finitely many orbits is finite.
Also a path ending at odd q>1 cannot repeat under Collatz:
a repeat forces its endpoint onto the eventual 1,2 cycle.
Thus all eligible q in the test are bounded independently of b,
and for large b none is >K_b. No band succeeds. QED.

**Complexity.** There are O(b K_b^2) centers in the scan.
Each interval has at most 2^(16K_b)+1 <= (2b)^16+1 integers.
Every candidate starts below K_b 2^(2b) and remains of O(b)
bitlength through 2b shortcut steps. The exact integer carry
test, the repeated-state test, grouping by q and by the finite
mixed classes, and counting distinct sources are all polynomial
in b and the bitlength of the rational epsilon. This is
polynomial in the physical-row parameter b, NOT polynomial in
its binary input length log b. The exponent is not optimized.
The earlier full-row scan in PR201 was exponential in b.
This narrower finite test is a new explicit cofinal reduction,
not a finite verification of all b or a solution of (8a).

## 4. Conditional enhancement: linear low-bit depth on a tiny band

Now separately assume F, the source-qualified exact central
extra-ternary-depth inverse floor used by PR201 and PR203.
In its count form there are absolute delta,c,F0,n0 such that
for n>=n0, 1<=K<=delta(n-1), |t-2n|<=sqrt(n), any supplied
ordinary unit z and unit residue rho modulo 3^K, there are at least

    c 2^t/(3^(n+K) sqrt(n))

distinct literal n-gap inverse sources at that residue, with
physical total t, target z, and middle affine offset <=F0.
The underlying manuscript is paper 48 v2 Lemma 7 (76) and
Theorem 8, as reconstructed in the pinned PR203 depth-bank
note and PR201 two-end-bridge. The primary manuscript was not
retrievable in this session; F is explicitly an assumption,
not a new independently validated analytic theorem.

Take h,J>=1 with h+J<=eta k for sufficiently small absolute eta
depending on delta, say eta<=1/10. As above k=o(b), k->infinity.
For a prescribed odd binary prefix with p odd bits, put n=k-p-1.
Choose e among [S-h-2n-5,S-h-2n] so that z=I_e(a) is a unit.
This time e depends on p, but not the rest of the prefix or v.
The middle physical budget t=S-h-e has t=2n+d, 0<=d<=5.
It is central for large k, K=p+J<=delta(n-1), so F applies at
the actual z with exactly the residue (8). The inverse prefix
lifting proof is unchanged.

Each such mixed cylinder receives at least

    c' (4/3)^k 4^(-p) 3^(-J) / sqrt(k)           (10)

distinct sources in the exact balanced row with the common
suffix and relative carry (3). They all belong to the narrower band

    [Z_(b,k)-W_p,Z_(b,k)), 
    W_p=C_* (4/3)^k 2^(h-2p),                   (11)

where C_* is an absolute constant from F, not a target-dependent
loss. Indeed the front offset is <=(3/2)^h by (1) and the middle
coefficient is <=(3/4)^n. Their product is <=1 for large k by
eta<=1/10. Therefore beta0<=F0+1 and

    Z_(b,k)-x=(2^(h+t)/3^k)(3 beta0+1)
       <= 8(3F0+4)(4/3)^k 2^(h-2p).

The same band width is used for every residue of this particular
p. Formula (10) is precisely a constant times

    W_p/(2^h 3^J sqrt(k)).

Thus an inverse fiber retains a polynomial relative lower floor
in each prescribed mixed cylinder of LINEAR depth in k, even in
the extremely small real interval, without replacing the actual
suffix by a sampled law. It is not a local limit for arbitrary
short real intervals: the centers have the special form (4).

## 5. Conditional synchronized nonconvergent blocks

In addition to F assume S, the first-group complete-grid
synchronization bound from PR146 WHOLE_INTERVAL_SYNCHRONIZATION
(4). For M consecutive starts its failure probability by h
shortcut steps is <=C log(2M)/sqrt(h), on the fair binary
parameter; equality of affine profiles includes equality of
odd counts and persists.

Choose h=floor(eta k/2), J=1 and
M=floor(exp(c0 sqrt(k))) with small absolute c0 so synchronization
fails on at most 1/8 of the binary residues. Odd r occupy half
the residues. The first-arm parity word is a bijection on all
binary residues, so Hoeffding also gives, for a sufficiently
large absolute B, |p-h/2|<=B sqrt(h) except on at most 1/8.
The intersection has at least 2^h/4 odd synchronizing residues.
Among its O(sqrt(h)) possible p, choose one with at least
c 2^h/sqrt(h) such residues. Apply (10) to them with source
ternary residue 1 and sum disjoint binary cells. This gives
>=c W_p/sqrt(hk) >=c' W_p/k starts x of M consecutive integers.

For every such start the whole block x,...,x+M-1 shares the
same physical profile at h. The complete subsequent path
therefore reaches a with k odd inputs at S, and q_i at (b,2b)
on every arm (the accelerated row applies to odd members).
Every member is nonconvergent. Every arm starts below the
same center Z since its pre-gate affine carry is positive.
As the first start is >=Z-W_p, the entire block lies in the
single band (11). Greedy disjoint selection loses at most
2M-1 starts per retained block.

Hence each eligible k supplies a band with

    >= c W_p/(k M) disjoint monochromatic nonconvergent blocks
    of length M, covering >=c W_p/k integers,               (12)

with |p-h/2|<=B sqrt(h). For the logarithmic menu,
W_p=exp(k log(4/3)+O(sqrt(k))) is polynomial in b and
M=exp(c0 sqrt(k)). The centers themselves are >=exp(c b),
and all the bands are disjoint by (9). Thus the bad block
construction now occurs inside explicitly located polynomial
width bands, not merely macroscopic intervals of exponential
width. This is a conditional necessary consequence of failure,
not proof that such a bad gate exists.

## 6. Relation to the global proof attempts

The first constructive lane is the unconditional thin-band
amplification and polynomial row test. The second is the
conditional central-floor refinement, retaining both the
small real band and the low digits. The third is the
synchronized-block application at those same actual centers.

A possible closing target is to exclude the full mixed-cell
row witness in (8a), or, with F and S, to show along cofinally
many b that such explicitly centered bands cannot contain the
packing (12) of nonconvergent blocks. These are actual ordinary
tests, not probabilities conditioned on independent colors.
Neither exclusion was proved.

The construction deliberately uses a long suffix of length
b-O(log b). Its witness population is polynomial in b, while
the source heights are exponential. It therefore does NOT
contradict PR207's deep-suffix upper localization after
normalization by q(4/3)^b. This lane complements rather than
solves the near-natural-scale intermediate trace problem.
The newly constructed lower witnesses cannot be upgraded to a
positive fraction of the entire exponential-height shell.

No arbitrary short-window lower floor is claimed. Indeed,
synchronization and a fixed terminal gate only put one component
in the resulting block. Marginal density results at a different
target cannot be multiplied to obtain a third color inside it.
The same-prefix rigidity of PR203 is consistent with these
examples precisely because the real location is retained.

### Frozen inputs and recent intake

* Main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a,
  research/astra-three-routes/pass3/FINITE_RECORDS.md T-A3-651:
  elementary finite simple-path count and reciprocal bound S0.
* PR201 parent 2978d84f8a1fda9083593b26c6bf724d5976d859,
  escape-analysis/README.md: two-gap router and balanced
  row amplification; earlier two-end-bridge/README.md: F.
* PR206 45a6a111321f947a8482c9e96e898435b57cee09:
  exact-clock odd-residue itineraries (earlier clock-itineraries
  packet) and 513-rank tower merger (November25.md). Our
  binary-prefix mixed cells and thin real location are different
  from prescribed mod-three odd-state itineraries.
* PR203 3f2c89f12b057b8bb8655bd6fc794c772aa8b65d,
  research/mixed-adic-basin-density-20261124/fixed_target_depth_bank.md:
  F and macroscopic mixed-adic lower density. PR202 earlier
  synchronized block count. We do not reverify the external F.
* PR146 f431078244e868dc699fad011044f0d5e7f76437,
  research/upper-bit-mergers/WHOLE_INTERVAL_SYNCHRONIZATION.md
  (4), the source-qualified synchronization input S.
* PR207 b56c4dc2c28a184cf55638bb80c49a9d4662fc81:
  diffusive aggregate exact rows, normalized opposing bound.
* PR199 d868f8e8405c08b8c501236853bea495ca593824:
  critical marked high-valuation sections for fixed targets.
  Here the long valuation occurs at an actual interior gate
  at a prescribed balanced row, rather than the first source.
* Latest selected interfaces: PR192 07d494324c7ea440d45845d725f5cebad8a67124
  actual certificate transport and escape rigidity; PR195
  4fd8af31c1ea525252b4d8f7411b5921dd447048 full-denominator
  and integer-trace obstruction; PR197
  156652e03fe7a78f9cd4442039779cc622fdf3de source-dependent progress;
  PR209 2d0230aa52d85732dbc85b5df20e30108dc1396f tower coverage;
  PR200 81ea4c1754d73c98d1451447527e6b2ba56977cc minimum strip.
  These were inspected selectively, not independently replayed.
* Classical inverse-tree precedent: Applegate and Lagarias,
  Lower bounds for the total stopping time of 3x+1 iterates,
  Math. Comp. 72 (2003), 1035–1049,
  https://websites.umich.edu/lagarias/doc/3x%2B1bound.pdf .
  The pruned inverse tree is not a novelty claim.

## 7. Evidence boundary

The exact finite BigInt replay constructed three disjoint bands
on one finite ordinary all-odd initial climb from a=2^2001-1,
with row b=2000 and menu k=96,128,256, not the asymptotic
logarithmic menu. It checks the actual full shortcut paths, both
source moduli, gate, high relative carry, and elementary
center separation. This large gate is only a finite arithmetic
control, not a bad source or convergence assertion. The replay
samples three inverse tree choices per cell, rather than
enumerating all 2^m branches. It also checks the exact carry
bound on all words of length <=9 and the central width and
count normalizations. See CONTROLS.json for executed counts.

A larger initial attempted replay timed out and is not counted
as successful. ThinBand.lean is an uncompiled proposal with
finite algebra and a conditional consumer of the concrete row
predicate. No Lean/Lake executable was found in this session,
no kernel or axiom audit, no independent subagent execution and
no full checkout validation. Earlier published Lean receipts
remain scoped to their exact earlier heads.

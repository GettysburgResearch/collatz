# Strict records as a renewal subshift: exact dimension and rational escape obstruction

**2026-11-26 continuation:** [unconventional research packet](../../unconventional-20261126/README.md),
with new scoped reviews and Lean receipts. The authoring-session evidence
statement below is historical. One interval in section 5.2 is corrected in
the [scoped erratum](../../../reports/unconventional-20261126/ERRATUM.md).

**Status: PROPOSED written mathematics; Collatz remains OPEN.** This packet
attacks fixed ordinary trajectories through their actual strict coefficient
records, not through independently sampled inverse starts. It establishes a
new finite-confinement obstruction in both real and ternary coordinates and
computes the exact dimension of the whole bounded-record-gap critical trace.
The main arguments are elementary; one sharp asymptotic for the dimensions
uses a classical ladder-epoch theorem. No new Lean compilation, full checkout
validation, or independent subagent review is claimed.

## 1. Literal records and finite ladder alphabets

Use the ordinary shortcut T and its odd-to-odd acceleration U. Write
x_k=U^k(a) for one supplied positive odd unit a, and let e_k>=1 be its
actual gap from x_(k-1) to x_k. Put s_k=sum_(j<=k)e_j and
M_k=3^k/2^s_k. A strict coefficient record is k>0 with M_k>M_i
for every 0<=i<k; include k=0 initially. Distinct time multipliers cannot
tie, by unique factorization of 2 and 3. By the resident finite simple-path
reciprocal bound, x_k=a M_k D_k where D_k increases to a finite positive
D_infty on every injective orbit. Such an orbit has x_k->infinity and
therefore cofinally many strict records. This is PR206's actual record
criterion, not an assertion of uniformly bounded record gaps.

For a positive integer J, consider the finite alphabet L_J of chronological
positive-gap words w=(e_1,...,e_m), 1<=m<=J, satisfying

    2^S_j > 3^j  (1<=j<m),    2^S_m < 3^m,       (L1)
    S_j=sum_(i<=j)e_i.

These are strict ascending first-ladder words for the increments
alpha-e, alpha=log_2 3. They are exactly the blocks between consecutive
strict records, provided their length is <=J. In particular there is
NO intermediate strict record in a block.

Their total is necessarily S_m=floor(alpha m). For m>=2 the last gap
has to be one: before it the log multiplier is <=0, and a gap >=2
cannot raise it. Thus S_m>=floor(alpha(m-1))+2, and
floor(alpha m)-floor(alpha(m-1))<=2. Combine with the terminal strict
inequality. The m=1 case is just gap one. Some m have no blocks.
All gap letters of L_J are <=2J. The literal affine map of a block is

    F_w(z)=(3^m z+C_w)/2^S_m=r_w z+c_w,
    C_w=sum_(i=1)^m 3^(m-i)2^S_(i-1),
    r_w>1, c_w>0.                              (L2)

On Z_3 this is a contraction by 3^(-m) and maps into the units.
On R the inverse G_w(y)=(2^S_m y-C_w)/3^m is a contraction.
Since the alphabet is finite, write r_* = min r_w>1 and
c_* = max c_w<infinity. The inverse real slope has maximum lambda_*<1.

For a backwards word v, read its gaps from the terminal outwards. Write
A_j=2^S_j/3^j. Reversing a block of L_J gives exactly the condition

    0<A_j<A_m<1  (1<=j<m).                       (L3)

Indeed the forward interior multiplier relative to the block start
is <1. In a concatenation of reversed blocks all nonempty prefixes
have A_j<1. The first complete reversed block ends at the UNIQUE
maximum of A_j over the entire nonempty concatenation (finite or
infinite): proper prefixes are smaller by (L3), and all later
values are its terminal A_m times a strict subunit product.
Consequently the reversed complete-block parsing is unique.

## 2. Exact Hausdorff dimension, including the overlap loss

Let R be the full critical tree from PR210: the set of ternary points
represented by infinite backwards gap scripts all of whose nonempty
prefixes satisfy A_j<1. Let R_J be the compact subset represented
by infinite concatenations of reversed blocks of L_J.
The limit is the ternary series
beta=infty-sum_i 3^(i-1)2^(-S_i).
Equivalently a depth-b prefix fixes beta modulo 3^b.

**Theorem D.** Let N_m=|L_m words of length exactly m|, independent
of the upper cutoff J>=m. Define d_J>=0 by

    sum_(m=1)^J N_m 3^(-d_J m) = 1.              (D1)

For J=1 the root is zero; otherwise the sum is strictly decreasing
in d_J and there is a unique positive root. Then

    dim_H R_J = d_J.
    dim_H R = theta,
    theta = [alpha log alpha-(alpha-1)log(alpha-1)]/log 3
          = 0.94995552718833... .               (D2)

In fact the upper and lower box dimensions of R_J also equal d_J.
This identifies an entire exact dimension spectrum, not just an
upper bound on the number of gap words. It accounts for all overlaps
in the ternary coding, without an open set condition.

### 2.1 Bounded inverse offset

For any backwards prefix v of b gaps and clock s, let C be its full
integer carry so its inverse from endpoint y is
x=(2^s y-C)/3^b. Reading an additional backwards gap e appends
the numerator carry 2^e C+3^b and the denominator gains a factor 3.
In real coordinates the inverse offset C/3^b is obtained by composing
maps with positive affine multiplier and nonnegative offset.

On a complete reversed block the multiplier is <=lambda_* and the
offset is bounded by a fixed constant of J. On the possible last
incomplete block there are only finitely many prefixes, all with
bounded coefficients. It follows that there is a finite B_J such
that

    0 <= C/3^b <= B_J                            (D3)

for EVERY prefix of every concatenation, uniformly in its depth.
For example take the geometric bound for the complete blocks and
enlarge it using the largest affine prefix multiplier and intercept.

### 2.2 Entire fixed-clock overlap bound

Fix b,s and one ternary residue y mod3^b. Each compatible gap word
has C=2^s y mod3^b. Distinct words of these clocks have distinct
carries: choose a positive odd ordinary representative q of this
residue. Full divisibility by 3^b forces all intermediate inverse
divisibilities, peeling the inverses from q one at a time. All
intermediate integers are positive and odd. The forward gap sequence
of the resulting source is therefore unique. Equal carries would
give the same source and hence the same word. This is the literal
ordinary decoder already used in PR201, not an assumption about
ternary separation.

By (D3), the possible integers C of a fixed congruence lie in an
interval of length B_J 3^b. There are at most floor(B_J)+1 of them.
For general b there are at most floor(alpha b)+1 possible clocks.
Thus the total number of possible PREFIX WORDS in a ternary depth-b
cell is O_J(b+1), not exponential. A fixed s removes even this
linear factor. These bounds retain the whole carry.

### 2.3 Pressure and dimension

Give each block w the independent probability 3^(-d_J |w|).
Equation (D1) normalizes the probabilities. By the maximum rule
(L3), a specified gap prefix of length b uniquely determines its
complete blocks until fewer than J letters remain. The total length
of the determined blocks is at least b-J (zero for small b).
The mass of the prefix is therefore at most 3^(-d_J(b-J)).
Combining with the full overlap bound gives for the pushed-forward
probability measure mu_J

    mu_J(y+3^b Z_3) <= C_J (b+1)3^(-d_J b).       (D4)

For every d<d_J this is O_{J,d}(3^(-d b)); the mass distribution
principle yields dim_H R_J>=d_J. The zero-dimensional J=1 case
follows directly from its one-letter alphabet.

For the upper bound extend any b-gap prefix to a complete block
boundary of length l in [b,b+J]. At a fixed l the distinct complete
concatenations determine disjoint block cylinders of probability
3^(-d_J l) each, hence their count is <=3^(d_J l). Summing over
those J+1 depths proves an O_J(3^(d_J b)) cover by depth-b cells.
Together with (D4) this proves both box dimensions and Hausdorff
dimension. No independence was assigned to a selected ordinary
trajectory; the probability is a counting device on the universal
symbolic set.

For R itself the count of length-b critical words is bounded by
binom(floor(alpha b),b). Stirling gives exponential rate
H=alpha log alpha-(alpha-1)log(alpha-1), and hence dimension <=theta.

For an elementary lower bound, fix a large L and S=floor(alpha L).
There are binom(S-1,L-1) positive compositions of S into L gaps.
Every cyclic class has a rotation with all backwards prefixes
strictly critical: start just after a maximum of the partial sums
S_j-alpha j on the periodic list before its last index, and use
the strictly negative total on wraparound. No two partial sums
tie since alpha is irrational. Each class has at most L rotations.
We get at least binom(S-1,L-1)/L distinct critical words. Every
finite critical word decomposes into reversed ladder blocks by
successively cutting at its unique maximum nonempty prefix ratio;
after that cut the remaining normalized prefixes are again critical.
Thus every such L-word is a complete concatenation in L_L. Its
block-cylinder mass is 3^(-d_L L), and these cylinders are disjoint
at the common gap length L. It follows that
d_L>= log(binom(S-1,L-1)/L)/(L log3)->theta.
Since R_L subset R, (D2) follows without a probabilistic theorem.

### 2.4 Sharp dimension-gap asymptotic (classical ladder theory)

In addition, we obtain

    theta-d_J ~ (log J)/(2 J log 3),  J->infinity.      (D5)

Here the one imported analytic input is the classical strict
ascending ladder-epoch tail for a centered real random walk of
finite nonzero variance. It is explicitly stated in Caravenna,
*A Local Limit Theorem for Random Walks Conditioned to Stay
Positive*, Probab. Theory Relat. Fields 133 (2005), 508-530,
Remark 1, p. 6 of the author's preprint,
https://arxiv.org/abs/math/0406182 ,
https://fcaraven.github.io/download/papers/llt.pdf .
The preprint's page containing the tail formula was inspected.
The proof applies it to an AUXILIARY geometric gap law, not to
the successive gaps of a supplied Collatz orbit.

Let p=1/alpha, r=1-p and choose iid gaps with probability
p r^(e-1). Their mean is alpha, so the walk alpha-e is centered
with nonzero finite variance. Its first strict positive crossing
tau has exactly the words L_J at finite depths, and the quoted
tail theorem gives P(tau>n)~c/sqrt(n) with c>0.
There is no tie at a positive integer clock because alpha is
irrational. A first crossing at m has total floor(alpha m); thus

    P(tau=m)=N_m exp(-H m) r^(-{alpha m}).
    a_m=N_m exp(-H m)
        =r^{ {alpha m} } P(tau=m).

In particular r P(tau=m)<=a_m<=P(tau=m). The total sum of a_m
is at most 1-c0 with c0=p-exp(-H)>0, by the strict loss at m=1.
It follows at once that d_J<theta for finite J. Put
t_J=H-d_J log3>0; (D1) is sum_(m<=J) a_m exp(t_J m)=1.

Fix 0<eta<1/2. At t=(1/2-eta)log J/J split at
B=floor(J/(log J)^2). The part m<=B is <=(1+o(1))(1-c0),
and the rest is <=J^(1/2-eta) O(B^-1/2)=o(1).
Thus t_J>(1/2-eta)log J/J eventually.

At t=(1/2+eta)log J/J choose a fixed c1 in (0,1) with
c1(1/2+eta)>1/2. The tail asymptotic yields
sum_(c1 J<m<=J) a_m >= c2 J^-1/2, since the difference of
the two survival tails is asymptotic to a positive constant
times J^-1/2. After weighting by exp(t m) this sum diverges,
so t_J<t eventually. Let eta decrease to zero. This proves
(D5). It uses neither a mixing assertion about Collatz nor a
numerical conjecture about the ladder coefficients.

## 3. Bounded record gaps on one actual escaping orbit

Now suppose the fixed ordinary ray is injective and its successive
strict record indices k_l have gaps <=J eventually. Write q_l=x_(k_l),
R_l=M_(k_l), and retain the actual interrecord word w_l in L_J.
Drop the finite initial segment if necessary. Equations (L2) give

    q_(l+1)=F_(w_l)(q_l), R_(l+1)=r_(w_l) R_l.

In particular the coefficient multiplier grows at least as
r_*^l. All intermediate odd states are within a bounded factor
of the previous record height, because at most 2J shortcuts
occur between records and each shortcut divides by at most two.
Hence this bounded-gap regime is necessarily exponentially
growing in odd time. No claim is made that a general escape has
bounded gaps.

The positive limit L=lim q_l/R_l exists and is finite:
the increments of q_l/R_l are c_(w_l)/R_(l+1), a convergent
geometric sum. This is the ordinary real renormalized limit,
also furnished by the resident simple-path distortion argument.
Define the bounded positive real error

    E_l = L R_l-q_l
        = sum_(t>=l) c_(w_t)/(r_(w_l)...r_(w_t)).
    0<E_l<=c_*/(r_*-1).                         (G1)

Its negative z_l=-E_l follows the VERY SAME exact affine rule

    z_(l+1)=F_(w_l)(z_l).                         (G2)

Thus the record system has a real backward-contracting coordinate
and a ternary forward-contracting coordinate, both retaining the
same block word. This is analogous in spirit to natural extensions
for rational-base numeration and real/p-adic affine sets, but
we use only the literal formulas above. In particular no independent
real/ternary product measure is presumed.

Let K_3 be the cluster set of q_l in Z_3 and K_R the cluster set
of z_l in R. They are nonempty compact sets, and K_3 subset R_J:
every finite backwards script through late record endpoints
consists of whole reversed blocks and possibly an incomplete
earlier block. Both sets depend on one supplied ordinary orbit,
not on the universal language.

## 4. Neither cluster set can be finite

**Theorem G.** On an injective positive ordinary orbit with eventually
bounded strict-record gaps, BOTH K_3 and K_R are infinite. In particular
this excludes finite ternary confinement with no rationality hypothesis.

Suppose one of the sets K is finite. In its relevant metric give the
late observations their unique nearby cluster label. All observation
distances to K tend to zero by compactness. Each recurring triple
(u,w,v), previous label, actual block word, next label, satisfies
v=F_w(u) by continuity. There are only finitely many triples; discard
a finite beginning so all later triples are recurring. The resulting
finite directed graph is strongly connected because the actual label
sequence visits each vertex infinitely often, and its late steps are
edges of the graph. In particular every vertex lies on a nonempty
directed cycle.

On such a cycle the composite has the form
F(z)=(3^m z+C)/2^s, with m>=1, s>=m, C>0 and 3^m>2^s,
since every block has forward coefficient greater than one.
The fixed point is uniquely

    z=C/(2^s-3^m)<0.

Its numerator and denominator are odd (the chronological carry is odd),
and its reduced denominator is prime to three. Thus EVERY label in K
is a negative rational with odd numerator and odd denominator, even
if the original confinement hypothesis allowed irrational points.

Here is the crucial valuation rule for any rational t=a/d with
a,d odd, d>0, 3 not dividing d. Its genuine signed rational odd
gap is g=v2(3a+d); the numerator is nonzero since 3 does not
divide d. For a proposed gap e, the rational image is
(3t+1)/2^e. If e=g it again has odd numerator and odd denominator.
If e>g it has negative 2-adic valuation. If e<g it has positive
2-adic valuation; any further positive gap then makes that
valuation negative. Once negative, each further gap e reduces
the 2-adic valuation by exactly e, because adding 1 to 3t cannot
cancel a dyadic denominator. Thus no sequence of positive gaps
can start and end at odd-numerator odd-denominator rationals
if even one of its gaps differs from the genuine gap at its
odd rational state.

Apply this to every graph edge w. Its endpoints have v2=0,
so its ENTIRE prescribed gap sequence is the genuine deterministic
signed rational orbit segment. Along the actual late label path,
all blocks concatenate to one genuine negative rational forward
itinerary. Fix its first ordinary record x>0 and corresponding
rational z=a/d<0. Their future gap sequences agree exactly.
After m gaps of total s the cleared affine identity gives
3^m(dx-a)=2^s(d x_m-a_m), where a_m=d z_m is integral.
Since 2 and 3 are coprime, 2^s divides the fixed positive integer
dx-a. But s>=m->infinity. Impossible. This proves G for both
the real and ternary cluster set.

This proof does not require rationality classification of the
whole critical tree; it obtains rationality directly from
finite recurrence and then uses the actual first ordinary source.

## 5. One rational ternary cluster forces a dyadic-denominator tower

**Theorem Q.** Under the same bounded-record-gap assumption, if
K_3 contains any rational point then it contains a sequence of rational
points u_j with v2(u_j)->-infinity. More precisely some u_0 has
v2(u_0)<0 and a sequence of words w_j in L_J gives
u_(j+1)=F_(w_j)(u_j) in K_3, with

    v2(u_j)=v2(u_0)-sum_(l<j) S(w_l) <= v2(u_0)-j.   (Q1)

If K_3 contains the rational -1, the u_0 can in addition be
chosen positive, and the subsequent real values grow at least
as r_*^j u_0.

### 5.1 Symbolic limit and rational backward shadows

Let X be the set of two-sided block sequences all of whose finite
windows occur arbitrarily late in the original one-sided record
word. The finite alphabet makes X nonempty, compact, and invariant
under the two-sided shift sigma. This follows by a diagonal
subsequence at late centers; conversely each specified sequence
can be approximated by arbitrarily late original windows.
For omega in X let

    pi(omega)=lim_(n->infty)
       F_(omega_-1) ... F_(omega_-n)(0) in Z_3.

Each block contracts by at most 1/3 in Z_3. The limit is uniform
over omega and depends continuously on it. Approximating original
windows shows pi(X)=K_3 exactly, and
pi(sigma omega)=F_(omega_0)(pi(omega)).
All backward odd-gap words of a point of X are critical by (L3).

For a rational z in K_3 with v2(z)=0 write z=a/d in reduced
odd numerator and odd denominator, 3 not dividing d. Choose
omega mapping to it. Inverting its past gaps gives integral
signed numerators over d: the full ternary congruences force
the inverse divisibilities, and each inverse numerator is odd.
At block boundaries the real inverse maps are uniformly
contracting with bounded offsets; all intermediate gaps belong
to the same finite alphabet. Consequently ALL backward rational
shadow values have bounded real magnitude and denominator dividing
d. There are only finitely many such values. Every sufficiently
deep tail repeats; reading it forward under the deterministic
signed odd map shows each shadow value lies on one rational
cycle. The critical prefix constraint rules out a positive cycle:
its repeated inverse multipliers would be >1, since the ordinary
affine carry is positive. Equivalently the negative sign follows
from a repeated cycle and the bound A_j<1 on all prefixes.
Thus z lies on a negative rational odd cycle, and its full
past is the genuine periodic inverse word. This is a short
bounded-gap proof of the applicable part of PR210's more
general rational trace classification.

If a rational point of K_3 has negative v2 already, use a
sequence omega representing it and all its forward shifts.
This proves (Q1) immediately by the valuation rule. If it has
positive v2 (even numerator and odd denominator), its first
forward gap has negative v2; again use the forward shifts to
a block boundary. These cases do not require any periodicity.

### 5.2 A first actual departure, not a symbolic choice

It remains to handle z with v2=0. By the periodic past in 5.1,
for arbitrarily large L there are arbitrarily late actual records
with their last L odd gaps equal to the negative cycle's word
ending at z. Choose such records going to infinity with L->infinity.
At each one the positive ordinary source must eventually depart
from the prescribed negative rational forward word: infinite
agreement would violate the fixed positive integer divisibility
argument of Section 4.

Follow the SAME ordinary orbit until that first differing gap.
Every gap since the beginning of the long L-past has matched
the negative cycle until this departure. If y is the ordinary
input to the departure and z' the corresponding negative rational
phase, then

    y=z' mod 3^L

in Z_3, since each matched forward odd gap multiplies their
difference by 3/2^e. This holds even when the intervening
agreement is very long. There are only finitely many possible
z' on the rational cycle. By bounded record gaps, going from
this departure to the second subsequent record uses at most
2J odd gaps, at least two, all gap letters <=2J. After passing
to a subsequence, fix the phase z' and that entire finite
departure word v. Its initial gap is WRONG for z'. Its rational
image u_0=F_v(z') has negative v2 by the rule in Section 4.
The actual later record endpoints converge ternarily to u_0:
their starting difference has valuation >=L, and each actual
gap contracts it further. Hence u_0 belongs to K_3. Now use
the forward-shift construction of 5.1. All steps are on one
fixed ordinary orbit until the compact limit is taken.

In the case z=-1, the genuine gap is one. At the wrong gap
e>=2 the shadow becomes -2/2^e in [-1/2,0). The next gap
leaves it >=-1/4, and the third gives a strictly positive
value. Take the third subsequent record in the preceding
subsequence argument instead of the second. This requires
at most 3J odd gaps and retains negative v2. The positive
real lower bound after that follows from (L2).

In particular no bounded-gap escape can have all its record
cluster points rational with a uniform bound on the power
of two in their denominators, even if that collection is infinite.
More generally, every rational-containing K_3 violates such a
uniform bound on its rational part.

### 5.3 Countable cluster sets necessarily contain a rational point

If K_3 is countable, take a nonempty minimal closed shift-invariant
subset Y of X (existence by compactness, intersecting descending
chains of nonempty invariant closed sets). The forward orbit
of each point in a minimal compact system is dense; its forward
omega-limit is a nonempty closed invariant subset.
The countably many closed fibers of pi restricted to Y cover Y.
By the Baire category theorem one fiber contains a nonempty
relatively open subset V. Choose a point of V; its forward
orbit returns to V at a positive time n. Therefore the rational
affine composition of the n intervening L_J blocks fixes its
pi-value. The composition has real slope >1, so the value is
a negative rational with odd numerator and denominator, as
in Section 4. In conjunction with Q this proves:

    If K_3 is countable, its rational points have unbounded
    dyadic denominators.

We do NOT prove that K_3 must be uncountable. Baire category
is applied to the compact symbolic limit system, not to the
countable set of all ordinary positive integers.

## 6. Exact symbolic obstruction and next proof step

There is a sharp reason not to strengthen Q to "no rational
cluster point" without another ordinary-source argument.
Consider the two-sided chronological record language with
the block (1) repeated everywhere, except for one block (2,1).
Both are in L_2; their maps are (3z+1)/2 and (9z+7)/8.
The all-(1) past gives z=-1. At the end of the exceptional
block the rational phase is -1/4, then 1/8, then 11/16, etc.
These are actual points of R_2, with unbounded dyadic denominator
and positive unbounded real magnitude along the forward chain.
In the ternary metric they approach -1 because the remaining
map is a contraction there. A one-sided SYMBOLIC sequence
with isolated (2,1) defects separated by longer and longer
runs of (1) has a countable symbolic limit set (the constant
sequence and the shifts of a single defect), hence a countable
ternary limit set. Every finite window is realizable by some
positive ordinary integer via the exact carry congruence.
This does NOT realize that infinite word at a fixed ordinary
positive source. It shows that bounded-gap and rational-base
symbolics alone cannot disprove this entire class.

This packet therefore gives three distinct useful obstructions:

* Actual bounded-gap escape has neither finite real-error nor
  finite ternary phase confinement.
* Any rational ternary accumulation point forces a whole
  dyadic-denominator tower in the same actual cluster set.
  Countable confinement with bounded dyadic denominator is
  impossible by the minimal-system argument.
* The universal critical trace for bounded record gaps has
  exact dimension d_J<theta<1, and its approach to the sharp
  unbounded-gap dimension is given by classical ladder theory.

A direct closing step would need to exclude the **actual**
bounded-gap symbolic possibilities (for example by proving
a contradictory confinement or lower dimension theorem on
one supplied escape), and also handle unbounded record gaps.
Nothing here establishes those two statements. Positive
nontrivial cycles require separate exclusion. Neither compact
symbolic limits nor finite ordinary realizations alone give
a universal ordinary-source contradiction.

## 7. Exact source and literature ledger

* Main ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a,
  research/astra-three-routes/pass3/FINITE_RECORDS.md, T-A3-651:
  simple-path reciprocal bound used in the cofinal record input.
* PR206 45a6a111321f947a8482c9e96e898435b57cee09,
  research/clock-itineraries/EscapeRecords.md and EscapeFrontier.md:
  actual strict records, positive integer avoidance and higher-slope
  record density. The bounded-gap assumption here is on the exact
  critical slope, not a consequence of its higher-slope density.
* PR210 592328fecf8ea2cf41736294856d95f890a1ba98,
  research/critical-record-rational-rigidity-20261125/README.md:
  rational classification of the full critical tree and finite-rational
  bounded-gap obstruction. Section 4 removes rationality from finite
  ternary confinement and adds real error; Section 5 only requires one
  rational point and retains arbitrary dyadic denominators.
* PR201 parent 02fb390a76fb2ffb00fee612649ca23a82d99d31:
  previous thin-band attack. The inverse decoder and finite record
  distortion inputs are already resident in this branch. No increase
  to its earlier verification scope.
* PR192 1f1d3d690d7517e1b2a44b5f2f4930bd45b63302,
  PR195 99a4ab3f808c01acd115ef08eee42a8b886d5d4c,
  PR197 10d87fee615d1095990d6b7ea329126b4cf7aa5a,
  PR193 aa0b01234735683b413098b81afdf764de503730:
  latest ordinary, cycle, residual merger and Fourier closure interfaces.
  Selected entry points reviewed; not a full re-audit of their proofs.
* Rational-base inspiration (not imported as a Collatz theorem):
  Eliahou and Verger-Gaugry, *The number system in rational base 3/2 and
  the 3x+1 problem*, Comptes Rendus Mathématique 363 (2025), 329-336,
  https://doi.org/10.5802/crmath.662 ; Steiner and Thuswaldner,
  *Rational self-affine tiles*, https://arxiv.org/abs/1203.0758 .
  The real inverse contraction and ternary forward contraction are
  exact here; we do not assume the hypotheses of their tiling theorems.
* Classical fluctuation theory: Caravenna 2005 Remark 1 as specified
  in Section 2.4 (citing Feller XII.7 and XVIII.5). This supplies only
  the tilted iid geometric ladder tail needed for (D5). All the
  dimension identities and confinement theorems preceding (D5) are
  independent of that probabilistic input.

## 8. Evidence scope

The executed BigInt program enumerates all ladder words through depth
10, compares with an exact dynamic program through depth 256, checks
3426 complete backwards concatenations and their unique maximum parses,
and lifts every one to a literal positive ordinary path with exactly
the declared strict-record boundaries. It checks negative rational
periodic shadows, every tested wrong-gap valuation, subsequent exact
dyadic-denominator growth, and isolated-defect residue contractions.
The numerical pressure roots are floating point illustrations,
NOT interval-certified constants. The exact counts are integers.
See controls.js and CONTROLS.json.

RecordRenewal.lean contains proposed finite algebra, parity,
shared-clock divisibility and fixed-point lemmas; it is not a
formalization of Hausdorff dimension, Baire category, or the
full ordinary theorems. Lean/Lake were not present locally. No
kernel/axiom audit, independent subagent run or complete checkout
validator was executed in this session. The previous audited PR201
files and receipts remain unchanged. Collatz is not proved.

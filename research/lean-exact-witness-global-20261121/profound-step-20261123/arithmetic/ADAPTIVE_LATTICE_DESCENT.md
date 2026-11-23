# Adaptive ordinary lattices with unrestricted defect words

23 November 2026. **Written proof with a thirteen-declaration Lean consumer.
Full Collatz, unrestricted cycle exclusion and the residue-512 implication
remain OPEN.**

The previous [infinite-dictionary theorem](../../repo-synthesis-20261123/cycles/INFINITE_DICTIONARY_DESCENT.md)
uses one common lattice spacing and a common cutoff. The present argument
keeps the source's *actual* repetition lattice instead. This removes the
common cutoff, permits unbounded defect words with individually chosen
repetition lengths, and does not require the repeated base word itself
to be contracting. Its conclusion is an explicit **first hit**; zero
absorption is deliberately not asserted for a single finite macro.

## 1. The literal data

Use the shortcut map T(n)=n/2 for even positive n and T(n)=(3n+1)/2
for odd positive n. Fix a nonempty binary parity word u with complete
integer affine data

\[
F_u(x)=\frac{Px+C}{Q},\qquad P=3^{p(u)},\quad Q=2^{|u|},\quad C\ge0,
\qquad d=Q-P\ne0. \tag{AL1}
\]

The word is used only when every indicated ordinary parity branch is
legal. In particular gcd(P,Q)=1. There is **no assumption P<Q**.
For an arbitrary finite defect word t, write

\[
F_t(x)=\frac{Rx+B}{S},\qquad E=dB-(S-R)C. \tag{AL2}
\]

Every macro is an actual positive ordinary trace

\[
x\mathrel{\mathop{\longrightarrow}^{u^k}}v
 \mathrel{\mathop{\longrightarrow}^{t}}y,
\qquad k\ge1. \tag{AL3}
\]

Its two displacements z=dx-C and z'=dy-C obey

\[
Q^k\mid z,
\qquad SQ^kz'=RP^kz+Q^kE. \tag{AL4}
\]

These are the complete ordinary identities already proved in the pinned
LatticeDescent module. The divisibility follows from
Q^k(dv-C)=P^k(dx-C) and coprimality; all intermediate integer endpoints
are retained. Neither polynomial-factor cancellation nor a 2-adic
completion substitutes for ordinary legality.

## 2. The adaptive strict-descent theorem

**Theorem AL-T1.** If the particular macro satisfies

\[
\boxed{RP^k+|E|<SQ^k,} \tag{AL5}
\]

then, whenever z is nonzero,

\[
\boxed{|z'|<|z|.} \tag{AL6}
\]

The target needs no prescribed lattice and no following copy of u.

**Proof.** Since z is a nonzero integer multiple of Q^k,
|z|>=Q^k. Taking absolute values in the complete transport gives

\[
SQ^k|z'|\le RP^k|z|+Q^k|E|
 \le (RP^k+|E|)|z|<SQ^k|z|.
\]

Cancel the positive factor SQ^k. The two magnitudes are nonnegative
integers, so the drop is at least one. This uses the lattice available
at the source of *this* macro; its spacing may change at the next macro.

**Theorem AL-T2 (finite first-hit bound).** Suppose actual macros
u^{k_j}t_j have successive boundaries x_j and each satisfies its own
(AL5). Then some boundary j<=|d x_0-C| satisfies

\[
\boxed{d x_j=C.} \tag{AL7}
\]

Only the first |d x_0-C| macroedges are needed. If no such boundary
occurred, (AL6) would produce that many strict decreases from the initial
nonnegative integer magnitude while keeping the last magnitude positive,
a contradiction. A zero encountered earlier finishes the first-hit
argument regardless of the following finite macro.

For an all-time actual path, (AL7) reaches the fixed point q=C/d. If q
is not a positive integer, the proposed all-time positive path is
impossible. If it is a positive integer, the next actual copy of u is
its genuine finite Collatz cycle, so the ordinary trajectory is periodic
from that hit. This identifies the actual u-cycle, not necessarily the
standard cycle for an arbitrary base word.

For an expanding base word P>Q with C>=0, q is nonpositive. Thus the
criterion excludes every all-time positive path in this paid language,
even though its repeated part is expanding. The defect must pay the
expansion and full carry through (AL5).

## 3. All finite defects, with no uniform dictionary bound

Suppose P<Q. For each *individual* finite defect t, a cutoff K(t) exists:

\[
\frac RS\left(\frac PQ\right)^k+
\frac{|E|}{S Q^k}\longrightarrow0.
\]

Exact search for the first k satisfying (AL5) therefore terminates.
Every later k also works because both terms decrease. Consequently
AL-T2 applies to the entire infinite family of **all finite binary
words**, provided each selected repetition count pays the defect that
actually follows it. There is no bound on the defect lengths, no common
upper bound on R/S, and no common K. Those were real restrictions of the
previous uniform-cutoff theorem.

### An explicit unbounded language reaching 1

For u=10 one has P=3,Q=4,C=d=1. For each defect t put
B_t=max(1,|t|). Then the explicit rule

\[
\boxed{k\ge2B_t} \tag{AL8}
\]

pays every possible defect t. Here B_t is a length bound, distinct from
the carry B in (AL2).

To check it, set a=(3/2)^{B_t}. Every defect of length at most B_t has
R/S<=a. Comparing both positive real branches with x↦(3x+1)/2 gives
0<F_t(1)<=2a-1. Since B_t>=1,

\[
|E|/S=|F_t(1)-1|\le2a-2.
\]

At k=2B_t, the left side of the normalized (AL5) is at most

\[
(27/32)^{B_t}+2(3/32)^{B_t}-2(1/16)^{B_t}<1. \tag{AL9}
\]

For B_t=1 this equals 29/32. For B_t>=2, dropping the negative term
bounds it by 747/1024. Larger k only reduce both terms. This is the
previous packet's exact cutoff calculation, now used separately at
every macro rather than under one global length bound.

Thus every actual positive ordinary path with full tail

\[
(10)^{k_0}t_0(10)^{k_1}t_1\cdots,
\qquad k_j\ge2\max(1,|t_j|), \tag{AL10}
\]

reaches 1 at a boundary j<=x_0-1. The defect lengths and repetition
counts may both be unbounded and otherwise arbitrary. The old normalized
clock can be sharper when a common cutoff is available; the new theorem
trades that common lattice for broader coverage and a raw integer clock.
The bound counts macros, not ordinary shortcut steps.

## 4. Changing every base word and its rational center

The fixed base can also change, but the cost of changing center must be
included in the same integer rank. For each nonempty base u_j let its
complete data be P_j,Q_j,C_j. Choose integers d_j>=1,c_j with

\[
d_j C_j=(Q_j-P_j)c_j. \tag{AL11}
\]

Thus c_j/d_j is its rational fixed point. The canonical choice reduces
C_j/(Q_j-P_j) to lowest terms with positive denominator. This reduction
uses the **full numerical gcd**, not just structural polynomial factors.
For every actual repeated run u_j^{k_j}, the anchored displacement

\[
z_j=d_jx_j-c_j
\]

still has Q_j^{k_j}|z_j. Indeed (AL11) gives
Q_j^{k_j}(d_jv_j-c_j)=P_j^{k_j}z_j, and coprimality cancels P_j^{k_j}.

Let the following defect have data R_j,S_j,B_j and define the complete
cross-carry

\[
F_j=d_{j+1}(R_jc_j+d_jB_j)-S_jd_jc_{j+1}. \tag{AL12}
\]

Direct substitution yields

\[
S_jQ_j^{k_j}d_jz_{j+1}
 =R_jP_j^{k_j}d_{j+1}z_j+Q_j^{k_j}F_j. \tag{AL13}
\]

**Theorem AL-T3 (moving anchors, one integer rank).** If every macro pays

\[
\boxed{R_jP_j^{k_j}d_{j+1}+|F_j|
       <S_jQ_j^{k_j}d_j,} \tag{AL14}
\]

then some j<=|d_0x_0-c_0| satisfies d_jx_j=c_j. The base words, their
lengths, their fixed-point denominators, the defects and all repetition
counts may vary without bound.

**Proof.** For z_j nonzero, |z_j|>=Q_j^{k_j}. Taking magnitudes in
(AL13), substituting that lower bound for the error term, and applying
(AL14) gives |z_{j+1}|<|z_j|. All these quantities belong to the *same*
well-ordered set of nonnegative integers. The finite first-hit argument
then applies without restarting the clock when the anchor changes.

At the first hit, the next actual nonempty base word fixes that positive
integer. Thus the trajectory has reached its genuine finite cycle. If
every permitted template has a nonintegral or nonpositive fixed point,
no all-time positive path is possible. If every permitted integral fixed
point belongs to the standard cycle, the trajectory reaches that cycle.
A general template may have another integral fixed point; that case is
not silently excluded.

This supplies a precise way to combine the current full-gcd word families
with a changing-template descent: a proved nonintegral center remains a
nonintegral center at the hit, even when every template changes. It does
not show that arbitrary ordinary words can be partitioned into macros
paying (AL14).

### The attempted universal selector

Allowing an arbitrary new rational center does not itself create a rank.
For example, the actual source 5 follows u=10 once to 4. Relative to
center 1 its displacement falls from 4 to 3. If the next actual base is
u'=0 with center 0, its displacement at 4 is instead 4. The center
change has erased the apparent strict decrease. Canonical d=d'=1 gives
F=1 and (AL14) becomes 3+1<4, which correctly fails.

The arithmetic selection problem is now explicit: on an unresolved
ordinary path, select genuine base words and fixed points so that the
complete cross-carry is always paid, with no free anchor reset. A long
source repetition supplies a larger lattice, but the defect and new
center simultaneously affect F_j and the denominator ratio d_{j+1}/d_j.
No bound on those quantities follows just from recurrence of the block.
The attempted global selection did not establish such a bound. The
finite supplied-macro certificate is proved; universal selection remains
open.

## 5. Sharp scope controls

1. **Coefficient contraction alone does not pay the carry.** Take the
   expanding base u=1 and defect t=0, both once. The actual positive
   path is 1→2→1. Its multiplier is 3/4<1, but d=-1,C=1,E=-1 and
   RP+|E|=4=SQ. Its nonzero displacement is unchanged. Replacing the
   strict complete-carry criterion by multiplier contraction would
   falsely exclude this genuine cycle.
2. **First hit is not zero absorption for a finite macro.** For u=10,
   k=2,t=1, the actual path starts at 1 and ends at 2. Here E=2 and
   RP^2+|E|=29<32=SQ^2. The source displacement is zero and the
   endpoint displacement is one. This is why AL-T1 assumes z≠0 and
   AL-T2 stops at the first zero. The next u-copy is not legal at 2.
3. **Ordinary integrality matters.** Repeated rational updates
   z↦3z/4 descend toward zero without ever hitting it. A real contraction
   alone does not supply the integer first-hit clock.
4. **A source lattice is not decorative in the abstract finite core.**
   D=4,a=0,b=1,e=3,x=1,y=3 obey bDy=ax+De and a+|e|<bD but increase
   |x|. The missing premise is D|x. In the Collatz specialization that
   premise is derived from the actual complete repetition.

## 6. Literature and the attempted universal step

The arithmetic investigation first inspected PR178's latest full gcd
result at 398b3a04da071e96362005792417bd5cf8cc6497. Its coprime packet
argument already settles unbounded pattern count in its stated family.
The complete numerical gcd for arbitrary words is still unsupported;
this note does not rename its special-family result or assert a general
moving-target Subspace theorem with increasing dimension or degree.

The alternative mechanism was suggested by the size-change and
transition-invariant literature. Lee--Jones--Ben-Amram formulate
termination through infinite descent along every admissible infinite
call sequence. Podelski--Rybalchenko's transition-invariant formulation
requires coverage of the **transitive closure** by a finite union of
well-founded relations. The official author/conference descriptions
were inspected at these primary pages:

- [Lee--Jones--Ben-Amram, POPL 2001; author publication record](https://amirben.bitbucket.io/research/papers.html), entry “The Size-Change Principle for Program Termination”.
- [Podelski--Rybalchenko, Transition Invariants, LICS 2004](https://lics.siglog.org/archive/2004/PodelskiRybalchenko-TransitionInvariant.html), abstract.

They motivate retaining an explicit integer rank and identifying the
coverage obligation. No deep termination theorem is imported as a Lean
axiom or used to manufacture a Collatz coverage claim; the descent proof
above is self-contained arithmetic. The literature reading is scoped
to the primary author/conference descriptions, not a claimed full-paper
reconstruction.

The direct attempt at a universal completion was to choose, on every
unresolved ordinary path, successive repetitions and defects satisfying
(AL5). The new theorem removes the need for a finite dictionary or
uniform cutoff, so arbitrarily complex individual defects are now
allowed. What remains unproved is **the existence of such a paid
factorization on every unresolved path**, possibly after a finite prefix.
For u=10 no theorem here forces the needed repetition-to-defect ratio.
A factorization found for a particular orbit is a valid certificate;
calling the search total would assume the missing conclusion.

This lane obtained neither an unrestricted numerical gcd bound nor
universal word coverage. It therefore gives no proof of full Collatz or
of the original residue-512 implication.

## 7. Formal and computational boundary

[AdaptiveLattice.lean](AdaptiveLattice.lean) imports the unchanged pinned
LatticeDescent module. It proves thirteen new declarations. Six cover source-lattice
size, strict adaptive descent, a finite first-hit clock, complete affine
macro descent, and its macro and literal ordinary-word consumers. Seven
more cover rational fixed anchors, their repeated lattice, complete
cross-carry transport, and the changing-anchor strict and first-hit
consumers, including a literal ordinary-word wrapper. P<Q, a common K, and target divisibility are
absent from the new consumer. Only the standard axioms appear.

The existence of K(t), the explicit real bound (AL8)--(AL9), and the
prose periodicity consequences are written proofs. The finite checker
compares literal ordinary simulations with complete affine identities
and exercises the stated failed strengthenings. Its finite census is
not used as proof of the infinite statements. Execution records, exact
source hashes, and primary-source inspection scope are in the report.

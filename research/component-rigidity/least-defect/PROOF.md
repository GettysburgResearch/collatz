# Exact all-height defect arithmetic and least-prefix repairs

**LD-001--006: PROPOSED, pending independent mathematical review.**
25 September 2026. No complete Collatz proof, universal terminating convergence
selector, or height-uniform upper repair estimate is established in this pass.

## 0. What changes, and what does not

For a finite dyadic step coloring, this packet counts **every** violated actual
odd equation below a physical cutoff, rather than finding just one defect or
scanning all integers below that cutoff. Its counts keep the +1 term exactly.
After finitely many binary heights, the shell count is an exponential main term
plus a periodic rational correction. A geometric sum then handles arbitrarily
large cutoffs using a number of interval operations independent of their height.
Integer bit complexity, the description size, and the number of repairs are
NOT bounded independently of the input.

The oracle also finds the globally least defect. Selecting that defect and a
bounded nearby batch gives eventual correctness on every fixed finite source
prefix, without separately following the root's trajectory. This supplies a
complete finite-cutoff solver and conditional termination for each source that
actually converges. It does not prove that every source converges. The remaining
upper bound on optimized repair costs is stated in Section 6, not assumed.

### Map, original sources, dependencies

Use ordinary positive integers and the unabsorbed shortcut map

    T_p(n) = n/2 when n is even; (p*n+1)/2 when n is odd,
    p in {3,5}.

The original N is fixed. The core cycle is included by odd sources {1} for p=3,
and {1,3} for p=5. No exterior exit is declared convergent. No argument chooses
new digits for an already fixed original source.

Publication parent: PR #138 at `c0e76d1e372b844c0e5911bdc035476c805dbd72`,
branch `research/anchored-cuts-constructive-20260925`. That checkpoint preserves
our preceding dyadic-repair manuscript/code and credits the independently
published overlapping dyadic-completion packet at
`3eb14b04cda6e87aa7daa22430cb9efacbba158f`. Neither source is modified here.

Exact source interfaces:

* `../dyadic-repair/PROOF.md`, DR-001--003: all-halving dyadic completion and
  rational lower/upper certificates. Its producer and solver-free verifier are
  hash-pinned by this packet. Infinite numerical minima are ENCLOSURES, not
  exact irrational values. DR-004 already finds SOME violated odd edge.
* `../dyadic-completion/PROOF.md`, DC-001/002/005: exact compressed minima,
  symbolic infinite coefficients, and full finite refinement with an enumerative
  oracle. The new complete oracle replaces that enumeration; the underlying
  dyadic elimination is credited, not claimed again.
* `../anchored-cuts/PROOF.md`, FC-004--007, and
  `../sparse-capacity/PROOF.md`, SC-003/004: no nonconstant full invariant has
  finite critical energy. Used ONLY in the closing criterion in Section 6.
  The counting theorems and conditional convergence proof do not depend on them.

The repository entrypoint, live branch, parent proof, and scoped source context
were read. No corrected mass/rank/ordinary-realization theorem is used here.
The new claims remain proposed; existing scientific statuses are unchanged.

## 1. LD-001: a complete exact shell oracle

For n>=1 put h(n)=floor(log_2 n) and u(n)=n/2^h(n) in [1,2).
Let g be a right-continuous Boolean step function on [1,2), with m half-open
cells [a_i,b_i) whose endpoints are dyadic rationals of common depth at most D.
Adjacent equal cells may be merged. Define b(n)=g(u(n)); then b(2n)=b(n) for
EVERY ordinary n. The endpoint 2 is identified with 1. Constant functions are
allowed in the counting interface, although an opposite-pin separator is not
constant. Redundant endpoints need not be genuine jumps.

An actual odd defect is an odd n with

    b(n) != b(T_p(n)).                                  (1)

On source shell 2^h<=n<2^(h+1), write S=2^h and r=floor(log_2 p).
For each source cell [a,b), the permitted source interval is

    [S*a, S*b).

For a target cell [c,d) and t in {r,r+1}, its exact preimage is

    [(S*2^t*c-1)/p, (S*2^t*d-1)/p).                    (2)

Normalization of p*n+1, or of (p*n+1)/2, gives the same phase. On this source
shell the exponent for p*n+1 is h+t for one of those two t values. This remains
true at h=0, including the seam p*1+1=4 for p=3. Thus (2) covers every target
case and retains the actual additive one.

Intersect each source interval with this target partition and with the source
shell. The source and target lists are monotone, with m and 2m cells, so their
common refinement has O(m) intervals and is found by a two-pointer sweep. The
source and target colors are constant on each resulting half-open interval
[A,B). To retain exactly its odd integers, take

    lo = ceil(A), increased by one if it is even;
    hi = ceil(B)-1, decreased by one if it is even.

Also intersect with an optional integral upper source cutoff. If lo<=hi, this
is precisely the arithmetic progression lo,lo+2,...,hi. Its cardinality is
(hi-lo)/2+1. Sum the progressions of opposite colors to obtain C_h, and take
their smallest first element to obtain the least defect in that shell.

**LD-001.** This is a complete exact partition of the odd sources in the shell,
with their actual source/target colors. It has O(m) rational interval operations
and at most O(m) nonempty progressions. It does not enumerate a source interval.

In particular zero means ALL the odd equations in that shell are satisfied,
not only a sampled set. Half-open endpoints and parity cannot be omitted:
rounding the ideal rotation's intervals is not a replacement for (2).

### Physical cutoffs keep both endpoints

For a complete graph cutoff H>=1, an eligible odd source obeys

    n<=L(H):=min(H,floor((2H-1)/p)).                     (3)

Indeed T_p(n)<=H iff p*n+1<=2H. The actual physical maximum on the shortcut odd
arm is max(n,(p*n+1)/2), not its odd part alone. All normalization halvings
stay below that maximum. The source upper bound (3) is used everywhere a
finite full-graph claim is made. H=1 has no eligible odd source for p=3 or5.

## 2. LD-002: the +1 correction becomes exactly periodic

Let R_p(x) be p*x normalized into [1,2). Define the rational number

    delta = integral_[1,2) |g(x)-g(R_p(x))| dx.          (4)

This is ordinary additive interval length dx, NOT logarithmic Haar measure,
a forward-orbit distribution, or the density of a hypothetical exceptional
Collatz component. It concerns only the specified finite step description.

Overlay source cell boundaries and their two R_p preimage branches. All ideal
overlay boundaries lie in (1/(p*2^D)) Z. Consequently delta is rational with
denominator dividing p*2^D. If g is nonconstant then

    delta >= 1/(p*2^D) > 0.                             (5)

To justify nonemptiness, otherwise g=g composed with R_p off a finite set.
Its finite nonempty set of genuine circle jumps would be permuted by R_p.
A periodic jump would imply p^j=2^a for some positive j and integer a, which
unique prime factorization excludes. A nonconstant finite circle step function
has at least one genuine jump, including possibly the seam. Equality off the
finite set is enough to identify one-sided jump sets. This argument does NOT
apply to an arbitrary infinitely rough function on ordinary dyadic points.

Put

    P=ord_p(2) = 2 for p=3, and 4 for p=5;
    h0=D+1.

**LD-002.** For the ACTUAL defect count C_h of (1),

    C_(h+P)-C_h = (2^P-1)*delta*2^(h-1),  h>=h0.       (6)

Equivalently, there are P exact rational values beta_0,...,beta_(P-1) with

    C_h = delta*2^(h-1) + beta_((h-h0) mod P), h>=h0,   (7)
    beta_j = C_(h0+j)-delta*2^(h0+j-1).

Every count is still an integer. The beta values must be retained; the ideal
main term is generally nonintegral and by itself is incorrect.

### Proof with the parity and endpoint terms included

View all interval endpoints on the n axis. Each source endpoint is S*x with
x dyadic; each target endpoint is S*y-1/p with y an ideal preimage boundary.
Include shell endpoints S and 2S among the source endpoints. Between distinct
ideal boundaries, scaled separation is at least 2^(h-D)/p. For h>=D+1 this
exceeds the maximum relative displacement 1/p. Therefore the ordering of all
these endpoint types stabilizes. If a source and target ideal boundary agree,
the target endpoint precedes the source endpoint by 1/p at every such height.
Clipping to the source shell has the same stabilized order. Two target
endpoints share the same displacement and cannot exchange order.

On replacing h by h+P, a source endpoint moves by (2^P-1)S*x, an even integer.
A target endpoint moves by (2^P-1)S*y, also an even integer: write the ideal
preimage as y=2^t*A/(p*2^D); then p divides 2^P-1, and h>=D+1 supplies a factor
two. Negative or exterior endpoints obey the same statement before clipping.

For ANY half-open real interval [A,B), moving A and B by even integers 2a,2b
changes the number of odd integers it contains by b-a. This follows directly
from the number of integers j with A<=2j+1<B, including endpoints exactly at
integers. Apply this identity to every stabilized interval of opposite colors.
Its change is (2^P-1)S times HALF its ideal length. Sum those ideal lengths:
they are exactly delta. Intervals created only by separating coincident ideal
boundaries have zero ideal length and contribute zero to the change. In fact
these length-1/p intervals next to even source boundaries contain no odd point,
but the change identity suffices without discarding them. This proves (6).
Iterating the recurrence along each of its P residue classes proves (7). QED.

### Exact controls, not a favorable-sign heuristic

For g=0 on [1,3/2) and g=1 on [3/2,2),

    p=3: delta=5/6, h0=2, beta=(-2/3,-1/3);
    p=5: delta=7/10, h0=2, beta=(3/5,1/5,2/5,4/5).

The apparent sign contrast in this one example cannot close the argument.
Already for p=3, changing the jump to 9/8 gives

    delta=7/24, h0=4, beta=(2/3,1/3).

Thus the mean correction for these two core-compatible p=3 colorings is -1/2
and +1/2 respectively. There is no universal favorable sign for arbitrary
finite-step candidates. This does not disprove a narrower inequality for a
specially constrained family of optimizing cuts. Also beta is a counting
correction, not the cost increase of an optimized repair; those are different
quantities. The entire recurrence works for the p=5 control system as well.

## 3. LD-003: all-height counts and the globally least defect

### Complete cutoff counts by closed sums

Compute shell partitions for h=0,...,h0+P-1 using LD-001. This finite list
contains every warm-up shell and all P beta values. For a cutoff H let L be (3)
and a=floor(log_2 L), unless L=0. Sum full shells below a and one truncated shell
a with last source L. The warm-up prefix has at most h0 terms. For h0<=h<a,
(7) gives

    sum C_h = delta*(2^(a-1)-2^(h0-1))
              + sum_(j=0)^(P-1) q_j*beta_j,             (8)

where q_j is the number of integers h in [h0,a) congruent to h0+j modulo P.
An empty sum is zero. The last partial shell is computed by (2), not by using
an asymptotic fraction of its full count. Combining the pieces is exact.

**LD-003a.** For a step description of m cells and dyadic depth D, one can count
all violated actual odd edges whose two endpoints lie below H with O(m(D+P))
interval operations, plus integer/rational arithmetic on numbers containing
O(log H) bits (and the description's input bits). No loop of length H OR log H
is needed in the tail aggregation. Finding floor(log_2 L) is an integer bit-
length operation. This does not assert constant bit complexity as H increases.

The corpus checks H=2^4096 for four explicit finite step functions. The output
counts have 4092--4095 bits. These are counts of that explicit function's equation
defects, NOT verification of Collatz for all integers below those heights.

### Globally least, rather than one convenient defect

Inspect the warm-up and one-period list in increasing shell order. If any shell
contains a defect, its least progression member in the earliest such shell is
the globally least actual defect. If all listed counts vanish and g is constant,
there is no defect. Otherwise (5)--(6) show that shell h0+P has at least one:

    C_(h0+P) = (2^P-1)*delta*2^(h0-1)
             >= (2^P-1)/p >= 1.

Compute just that one further shell and take its first defect. All preceding
shells were certified empty. Thus a nonconstant candidate's globally least
violated odd source is found by finitely many compressed interval operations.
An available bound is n<2^(D+P+2); it agrees with the earlier constant for p=3
and is weaker than DR-004's SOME-defect bound for p=5. This pass claims global
minimality and complete counts, not a new best constant in the earlier theorem.

For finite H, the least eligible defect is the global least one when it is at
most L(H), and otherwise there is no eligible defect. The complete count (8)
agrees with that zero/nonzero distinction.

## 4. LD-004: least-prefix repair, without forward-trajectory scheduling

Fix the original N and a finite retained set F of actual odd sources, including
the core. Retain all halving equations. Use the credited dyadic network to
obtain a feasible step completion. In the infinite objective, the implementation
solves a rational LOWER network and checks a rigorous upper/lower gap at most
one for the chosen completion. In finite horizons the cut and flow are exact.
If the pins are inconsistent, return their literal physical merger path.

Otherwise let d be the globally least violated odd source; for a finite H use
the least eligible defect. If the finite list of all eligible defects is empty,
return the complete finite optimum, as proved in Section 5. If d exists, insert
it permanently. The implementation may also insert at most B-1 additional
violations: choose the first B violated odd sources in [d,2d], clipped at L(H)
in a finite problem. B is fixed, and B=16 in the retained corpus. The interval
sweep supplies these sources from progressions; only the returned batch of at
most B integers is enumerated. There is no scan to d or 2d.

Recompute the optimizing completion, allowing old colors to change. The original
N never changes. Every inserted equality is actual, and already retained
sources cannot be selected again because the current cut satisfies them.
Crucially this policy does not examine the next source on N's forward orbit to
choose its repairs. Forward iteration is used only to replay a merger after
physical equality components have connected the pins.

### Prefix correctness in every hypothetical infinite run

**LD-004a.** If refinement continues infinitely, its successive least defects
d_j tend to infinity. For every fixed A, all sufficiently late candidate
colorings satisfy EVERY actual odd equation with source <=A.

Proof. Each d_j is permanently inserted and can never appear again. There are
only finitely many positive odd integers <=A, so there can be only finitely
many iterations with d_j<=A. At every other iteration global minimality says
that all odd equations below d_j are already satisfied by that candidate. This
remains true even when some satisfied equations were never explicitly inserted.
The least values need not increase monotonically; the assertion is eventual
escape from each finite prefix. QED.

This is stronger than excluding one candidate at every round. It is NOT the
claim that every odd equation is eventually inserted, and it is NOT a finite
termination proof. It supplies precisely the finite-prefix consistency needed
for a subsequent diagonal argument without refreshing the original source.

### Conditional completeness for convergent sources

Suppose the actual original N reaches 1 along a finite shortcut path. If N is
not a power of two, let M be the largest odd source on this path before its
first arrival at 1. Every candidate with b(N)=1 and b(1)=0 must violate at least
one odd equation on that path: otherwise summing changes along the path gives
zero, while its endpoints differ; even steps already satisfy their equalities.
Thus the globally least defect always obeys d<=M while the pins remain feasible.
Each selected batch source is <=2M. Distinctness of the selected MINIMA therefore
forces termination after at most (M+1)/2 repair rounds for any fixed batch limit.
At most M distinct odd sources can be inserted in those batches, because they
are all below the even endpoint 2M. For B=1 at most (M+1)/2 sources are inserted.
Powers of two have inconsistent pins using halvings alone.

**LD-004b.** The uncapped least-prefix procedure terminates with a literal merger
for every source that actually converges, without a root-fair insertion step.
This statement is conditional on existence of the finite path and its M. It
neither proves that M exists for every N nor improves on direct forward iteration
or its conditional odd-step count. The bound by a path's maximum source can be
much worse than a bound by its length. The experiment is not presented as a
faster numerical convergence census.

A retained partial functional graph containing the complete core cycle cannot
also contain a terminal exit in that same weak component. Consequently pin
connection gives a retained literal forward path to 1. The producer returns and
the checker replays that path, including all physical intermediate states.

## 5. LD-005: full finite optimality with a nonenumerative oracle

At fixed H=2^(K+1), start with any retained F whose actual edges lie within H.
The credited all-halving finite problem is a relaxation of the full graph G_H.
Use the finite exact cut and extend its coloring by the dyadic terminal rule.
Our oracle counts all violated odd equations satisfying (3).

If that count is zero, the candidate satisfies every physical odd edge of G_H
as well as all its halving edges. Its cut value is a feasible full upper witness
and a relaxation lower bound, hence is the exact FULL finite minimum. The flow
certificate and the complete zero-defect certificate certify both inequalities.
If violations remain, a least-prefix batch inserts new eligible equalities.
There are finitely many eligible odd sources, so this process terminates either
with pin inconsistency and a literal merger, or with that full finite optimum.

**LD-005.** This proves complete finite refinement without enumerating all odd
sources for its separation oracle. The number of rounds and the network size
may still grow with H and can in the worst case require all eligible constraints.
It is the complete oracle, not the entire full optimization, that is compressed
independently of ambient height. No sublinear bound for the whole solver follows.

Executed controls: 27 at H=256 returns a certified full finite separator;
27 at H=8192 returns its literal 70-step path, peak 4616. The former is not a
nonconvergence result: the larger cutoff includes the necessary path. Source
13 for p=5 at H=1024 retains a full finite separator. Its separately replayed
positive cycle is disjoint from the p=5 core, so this control must not be forced
into convergence by an exterior or equality convention.

## 6. LD-006: the exact remaining amortization target

Use the infinite objective and a specified deterministic least-prefix policy
started from the fixed core-only constraint set, not arbitrary selected ladders.
Let F_j be its retained odd sources and eta_j the TRUE optimal infinite energy
subject to those equalities and the original pins. While feasible, eta_j is
finite by the credited finite-constraint completion. Adding equations makes
eta_j nondecreasing. The rational lower estimates printed by the implementation
need not themselves be monotone when precision changes; they are not eta_j.

With certified gap <=1, the chosen candidate b_j satisfies

    E_infinity(b_j) <= eta_j+1.                         (9)

Indeed its energy is at most the reported upper bound, the lower bound is at
most eta_j, and their gap is <=1. Arbitrarily accurate solutions exist for
every finite network; a computational precision cap is reported as unresolved.

If an infinite run had eta_j bounded, (9) would bound all its candidate energies.
Take a diagonal subsequence of Boolean values on the SAME ordinary integers.
The two fixed pins survive. LD-004a makes every fixed odd equation true in every
sufficiently late candidate, so the limit satisfies it; all halving equations
also survive. Every fixed finite energy sum is bounded, and taking their
increasing supremum gives finite total energy. The credited finite-energy
Liouville theorem excludes this nonconstant full invariant separator.

Thus in a hypothetical infinite run eta_j must tend to infinity. A sufficient
closing theorem is now:

    For every fixed original N, the finite eta_j values along THIS core-start
    least-prefix schedule have a uniform bound C_N independent of j.          (10)

Together with the escape argument this would force a finite merger. Conversely
if a source converges, LD-004b gives only finitely many feasible iterates, so its
finite values are bounded. Statement (10) is therefore an equivalent closing
target, not a logical weakening claimed to resolve the original problem.

**No proof of (10) is supplied.** The contribution is the complete arithmetic
oracle and a specified automatically prefix-correct schedule, not a summable
repair-cost estimate. The earlier counterexample to bounds uniform over arbitrary
edge orders does not refute this particular core-start schedule; it also gives
no evidence that (10) is easy. Different tie rules and batch policies define
different schedules and must be stated, not silently optimized after the fact.

All the counting, prefix-consistency, and conditional path arguments above work
for p=5 too. Its disjoint cycles prevent a comparable successful global upper
estimate there. The exact p-dependent correction beta has no universal favorable
sign even for p=3, as Section 2 shows. What is still needed is arithmetic control
of optimized nonlocal recoloring costs or a finite inconsistency argument that
genuinely distinguishes the full 3x+1 system. Neither counting defects nor
persistently finding a new one supplies that missing control.

## 7. Evidence, limits, and external context

`oracle.py` uses a monotone rational interval sweep. `experiment.py` imports the
hash-pinned prior dyadic solver, constructs complete models and retains every
repair's cut, arithmetic certificate, selected batch and original source.
`verify.py` imports NEITHER producer NOR oracle NOR any flow solver. Its new
arithmetic checker forms event indices for j=(n-1)/2, independently reconstructs
all source/target color blocks, and sums height residues as separate geometric
progressions rather than the producer's aggregated main term. It delegates ONLY
the old generic cut/flow check to the hash-pinned solver-free prior verifier.
This modular reuse is explicit; it is not a third independent implementation of
minimum cut or an independent mathematical peer review.

The inventory includes all first-cell-zero Boolean grids through depth three
for both multipliers (276 cases including constants); literal small-shell and
physical-cutoff comparisons; additional recurrence checks through shell 64;
four H=2^4096 controls; complete finite optima; literal convergences; and capped
unfinished runs. The same exact original N is retained in every trace. Counts
and actual normal/optimized receipts appear in VALIDATION.json. The large full
corpus is reproducible rather than committed. Direct semantic corruptions are
rejected independently of payload hashes. Assertions are not relied on for
checks that must survive -O or -OO.

The conditional recovery of 27 is a regression of policy completeness, not a
new family excluded from the full conjecture. Root-fair forward scheduling from
the previous packet was cheaper on that bounded example. The globally least
single-edge development run reached its cap; a longer exploratory run timed
out. Both are documented rather than turned into success claims. No exhaustive
benchmark or asymptotic practical speedup over Collatz iteration is claimed.

Generic lattice-point counting and counterexample-guided refinement are not new.
For primary context, rather than proof dependencies:

* M. Beck, *Multidimensional Ehrhart Reciprocity*, arXiv:math/0111331,
  https://arxiv.org/abs/math/0111331 . Rational-polytope lattice counting has
  classical quasipolynomial structure. Our special formula is proved directly,
  with odd parity and the actual +1 translation retained.
* A. Solar-Lezama, *Introduction to Program Synthesis*, Lecture 10,
  https://people.csail.mit.edu/asolar/SynthesisCourse2020/Lecture10.htm .
  Counterexample-guided inductive synthesis is established methodology. The
  arithmetic least-defect oracle and its prefix consequence are the scope here;
  exclusion of successive candidates alone is not termination on an infinite
  domain. This is not an external priority search.

No full-checkout root validator, remote CI, formal proof build, external priority
confirmation or independent mathematical review was performed. Main, earlier
proofs, scientific registries, workflows, settings and licensing remain unchanged.

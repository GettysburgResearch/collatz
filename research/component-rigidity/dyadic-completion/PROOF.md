# Exact dyadic completion and the cost of importing actual odd edges

**DC-001--006: PROPOSED, pending independent mathematical review.**
25 September 2026. This pass does not prove Collatz, a height-uniform full-graph
repair bound, or termination of an uncapped successful convergence selector.

Parent: PR #138 at `45c970ccb3d0b034f6e5696710d9a94df66b2b27`.
Map: the unabsorbed shortcut map T_p(n)=n/2 for even n and (p*n+1)/2 for odd n,
with p in {3,5}. All sources, paths, and cutoffs are ordinary positive integers.

## 0. The mathematical advance and its boundary

The previous sparse packet solved a **pin-only relaxation** exactly, and supplied
lower bounds for a graph retaining every halving edge. It explicitly did not
assert equality for that latter graph. This pass solves the latter problem,
and more: retain **all halving equalities** and any finite collection of actual
odd edges, with no need to enumerate the remaining integer domain.

The finite problem is represented losslessly by a dyadic interval graph with
O(m D) vertices and edges, where m counts the marked odd rays and D is their
maximum binary height. The same graph solves the genuinely infinite-height
completion problem. Its optimum is exactly A*zeta(2)+B for integers A>=0 and
rational B, not a floating-point approximation.

Two actual 3x+1 examples show what was missing in the pin-only model:

* With source 27 and retained odd edges at 1 and 5, importing the actual edge
  27->41 costs exactly 2*sum_(j>=6) 1/j^2. This attains a universal fresh-ray
  repair bound. The old pin-only optimum misses this entire positive cost.
* With source 7 and only odd edges 1->2 and 7->11 retained, the optimal color
  of the SMALL integer 3 changes when the ambient cutoff first reaches 2^30,
  even though no new odd constraint is added. This is a cut-horizon effect,
  **not an actual Collatz stopping-time claim about 7**.

This supplies an exact setting in which to study upper repairs. It does not
supply a summable upper ledger for the full graph. In fact an upper bound uniform
over ALL orders of odd-edge insertion is false even for the convergent source 27.
The previously proposed upper bound for COMPLETE height cutoffs remains open.

## 1. Definitions and the retained ordinary graph

Let E be a finite set of positive odd integers. Retain the actual odd equality
b(n)=b(T_p(n)) for each n in E, and retain b(2n)=b(n) for EVERY positive n.
Include E={1} at least when p=3, and {1,3} when p=5, so the core cycle is present.
Additional core paths such as 5->8->4->2->1 may be retained explicitly.

Fix one original N>1 and impose b(1)=0, b(N)=1. Boolean functions are sufficient
here. Write

    V_k(b) = sum_(n=2^k)^(2^(k+1)-1) |b(n+1)-b(n)|,
    E_K(b) = sum_(k=0)^K V_k(b)/(k+1)^2,
    E_infinity(b) = sum_(k>=0) V_k(b)/(k+1)^2.

The finite objective lives on 1,...,2^(K+1). A finite physical E must obey
max(n,T_p(n))<=2^(K+1), and N must be inside that interval. All halving edges in
that interval are imposed. In the infinite problem all halving edges are imposed,
not a finite truncation. There are no unmentioned odd edges in either problem.

Denote the respective minimum values by eta_(E,K)(N) and eta_E(N). Infeasible pins
have value +infinity. The same E is used when comparing different K; varying E
with K is a distinct operation.

Let r(n)=oddpart(n), h(r)=floor(log_2 r), and

    u(n)=r(n)/2^h(r(n)) in [1,2).

Two integers lie on the same halving ray exactly when their u values coincide.
All halving-invariant b are precisely functions on the ordinary dyadic rational
points of [1,2), with endpoints 1 and 2 identified. No 2-adic realization is used.
At shell k those points are exactly

    1+i/2^k,  0<=i<=2^k,

and the two endpoints have color zero. Thus V_k is the variation on this actual
nested dyadic mesh. An odd equality at n is an equality between the two marked
points u(n) and u(T_p(n)), with their literal odd edge and halving paths retained.

Put

    M={1,r(N)} union {n,r(T_p(n)): n in E},
    D=max_(r in M) h(r).

Every marked point is present by mesh depth D. For a finite problem with the
stated physical cutoff, necessarily K>=D (apart from the power-of-two endpoint,
which is already the ray of 1).

## 2. DC-001: lossless dyadic interval elimination

The geometric statement first works for arbitrary nonnegative shell weights w_k.
For the infinite version assume their sum is finite. Later w_k=(k+1)^(-2).

Consider a closed dyadic interval I=[a,b] of mesh depth d. Suppose its strict
interior contains no marked point, and assign endpoint colors A and B. Its
contribution includes every adjacency edge lying inside I, at every mesh level
k>=d up to K or infinity. Its exact minimum is

    |A-B| W_d,       W_d=sum_(k>=d) w_k,                 (1)

with the sum truncated at K in the finite case.

**Proof.** At each level k, telescoping along the ordinary mesh inside I gives
variation at least |A-B|. For the upper bound, give every strict interior point
color A and the right endpoint color B. There is exactly one change per level
when A!=B, and none otherwise. The choice is consistent across ALL refinements,
so it respects every halving equality. Nonnegativity permits summing the lower
bounds, including infinitely many levels. QED.

Now start with [1,2]. If an interval contains a marked point strictly inside it,
retain its midpoint as a vertex, charge the parent edge w_d between its endpoints,
and split it into its two halves. If there is no interior mark, replace the
entire interval and all its refinements by the single edge (1). Identify endpoints
1 and 2. Midpoints retained only to expose deeper marks are free Steiner vertices,
not silently assigned colors or assumed to be Collatz sources of either pin.

Finally identify the marked vertices joined by each retained actual odd edge.
Keep parallel-edge capacities by addition and discard self-loops. Pin the resulting
vertices containing 1 and N to opposite sides.

**DC-001.** The minimum cut in this finite graph is EXACTLY eta_(E,K)(N), or eta_E(N)
with infinite tails. It is not merely a sparse lower bound.

Each coloring of the original ordinary graph restricts to the retained vertices;
(1) bounds its cost below by the compressed cut. Conversely any cut extends on
each eliminated interval by the explicitly described left-endpoint coloring.
Shared endpoints agree, and every odd constraint has both endpoints retained.
This gives a globally defined halving-invariant extension attaining the cut cost.

Every marked point needs at most h(r) expanded intervals on its ancestor path.
Therefore the retained graph has at most

    1 + sum_(r in M) h(r) <= 1+|M|D                     (2)

vertices and O(|M|D) edges. In fact if there are t expanded intervals, there are
t+1 vertices after identifying the two outer endpoints, and t+1 terminal intervals.
The theorem counts graph structure, not the bit complexity of its capacities
or a practical bound on the number of actual odd edges a full proof needs.

### Physical incompatibility and a merger certificate

If the compressed equality graph connects the pins, the corresponding original
selected-edge graph connects them too: normalization is implemented by actual
halvings, and every retained odd edge is an actual T_p edge. A component of a
partial functional graph cannot contain both a closed directed cycle and a
terminal exit. Since the entire core cycle is included, following the retained
outgoing edges from N yields a literal path to 1. The programs return that path,
not just a graph-connectivity flag. A finite certificate must keep every path
state below its stated cutoff.

No claim is made that every N is eventually connected by a particular incomplete
selection of odd edges. The old 27 spine obstruction continues to apply.

## 3. DC-002: exact infinite completion and a finite tail phase diagram

Define

    theta=zeta(2)=sum_(j>=1) 1/j^2,
    H_d=sum_(j=1)^d 1/j^2, with H_0=0.

A terminal edge at depth d has infinite capacity theta-H_d. Every internal edge
has rational capacity 1/(d+1)^2. Consequently every feasible compressed cut C has
cost

    A_C*theta+B_C,                                     (3)

where A_C is the number of terminal intervals whose endpoint colors differ and
B_C is rational. A_C is even: those intervals go once around the circle, so the
number of Boolean color changes is even. With incompatible pin values and a
feasible cut, A_C>=2. In particular

    eta_E(N)=min_C (A_C*theta+B_C).                      (4)

This is a minimum over finitely many cuts, and the minimizing ordinary extension
is given constructively by DC-001. Whenever the pins are feasible, eta_E(N) is
finite. One crude witness colors exactly the finitely many rays in N's retained
equality component one and all other rays zero; its shell variation is at most
twice the number of those rays.

For comparison, replacing the weight by (k+1)^(-s), this finite-odd-constraint
problem has finite feasible separation energy exactly when s>1. For s<=1 the
source ray and the core ray force at least two changes at every late level, so
the energy diverges. This **finite-constraint threshold one** is not the old
threshold two for two INFINITE inverse ladders. Different quantifiers produce
different problems; the latter theorem is unchanged.

### 3.1 The exact terminal-perimeter penalty

For any admissible finite K containing every mark and every retained physical
edge, a dyadic-consistent assignment through level K has the following property: its
cheapest extension beyond K has constant variation V_K at every later level.
Apply (1) separately to all level-K intervals. Thus

    eta_E(N) = min_b [ E_K(b)+V_K(b)*(theta-H_(K+1)) ],   (5)

where the minimum is over assignments satisfying the finite retained constraints
and the two original pins. The terminal perimeter must be optimized jointly with
the already-paid energy. Setting it to zero is not a legitimate completion.

### 3.2 A finite parametric envelope, not endless horizon recomputation

For admissible K>=D, also large enough to contain all retained physical edges,
the compressed graph structure and equality components no longer depend
on K. Only the terminal capacities change. For exactly the same finite set of
pairs (A_C,B_C) as in (3),

    eta_(E,K)(N)=min_C [A_C*H_(K+1)+B_C].                (6)

This is a concave, piecewise affine function of H_(K+1). Its active slopes are
nonnegative even integers and are nonincreasing as that parameter increases.
Indeed, compare an optimal line at x with one optimal at y>x; the two optimality
inequalities give A_x>=A_y. Distinct parallel lines cannot both be active unless
their intercepts agree.

If L is the number of terminal intervals, there are at most floor(L/2) different
positive active slopes. There are only finitely many horizon-dependent cost-line
changes. Eventually, for some fixed feasible pair (A,B),

    eta_(E,K)(N)=A*H_(K+1)+B,
    eta_E(N)=A*theta+B,
    eta_E(N)-eta_(E,K)(N)=A*(theta-H_(K+1)).             (7)

This follows from a finite envelope even without invoking irrationality: its
last interval approached from below ends at or beyond theta, and the active line
is continuous at theta. The statement concerns the optimum cost line, not a
unique optimizer when several different cuts have identical coefficients.
For every such admissible K>=D there is also the uniform estimate

    0 <= eta_E(N)-eta_(E,K)(N)
       <= L*(theta-H_(K+1)) <= L/(K+1).                 (8)

The last inequality is the elementary integral bound for the reciprocal-square
tail. Bounds (7)--(8) keep E FIXED. They do not control L, D or the cost when all
new actual odd edges are added as the height grows.

### 3.3 Exact numerical certificates without assuming an analytic approximation

The checker uses the identity

    theta=sum_(j>=0) H^(1)_(j+1)/((j+1)*2^j),
    H^(1)_r=sum_(i=1)^r 1/i.                            (9)

For a proof, integrate -log(x)/(1+x) over [0,1]. Its alternating power-series
expansion gives theta/2 by separating the even terms of the absolutely convergent
reciprocal-square series. Expand alternatively

    1/(1+x)=(1/2) sum_(j>=0) ((1-x)/2)^j.

All terms of this latter integral are nonnegative, and
integral_0^1 (-log x)(1-x)^j dx=H^(1)_(j+1)/(j+1), obtained by integration by
parts or by integrating (1-y^(j+1))/(1-y). This proves (9). Since
H^(1)_(j+1)/(j+1)<=1, omitting j>=J has error at most 2^(1-J).

All enclosure endpoints are rational. Capacities and flows are stored as exact
pairs (A,B). The standalone checker verifies flow conservation as a formal pair
identity, capacity inequalities using the rational enclosure, and exact equality
of cut and flow values. These facts alone certify optimality: the divergence
identity bounds every separating cut below by the flow value. No floating-point
objective or untrusted claim of max-flow success is used.

The producer has a symbolic precision cap and may return an error at that cap;
this is not relabeled as theorem failure or a successful universal algorithm.
The delivered corpus needed 64 terms in (9). Same-author implementation diversity
is not independent mathematical review.

## 4. DC-003: a sharp actual-odd-edge repair lemma

Let the old marked-ray set be M. Add one actual odd equality at n, with ray
endpoints a=n and c=r(T_p(n)). Suppose one of those endpoints, say r, is not in M.
In particular r is neither original pin and appears in no previously retained
odd equality. It may have appeared as a free Steiner vertex; this causes no
problem.

Starting from an optimal completion, keep every ray except r unchanged. If the
new equality is violated, change the value on the ENTIRE dyadic ray of r to the
value at the other endpoint. This preserves all halving equalities and every old
odd equality. The ray has exactly one interior point in shell k for each k>=h(r)
and none below. Only its two neighboring adjacency edges can change. Hence

    0 <= eta_(E union {n})(N)-eta_E(N)
       <= 2 W_(h(r)),
    W_h=theta-H_h.                                     (10)

If both endpoints are fresh, use the smaller of these two upper bounds. The same
statement holds with truncated W_h for a finite horizon. If the old optimizer
already satisfies the new equality the optimum does not increase at all.

For h>=1 the elementary bound W_h<=1/h yields the simpler repair cost 2/h.
An endpoint already carrying other constraints is NOT fresh. Applying (10) to
such an endpoint may break an entire old equality component and is invalid.
An old-to-old equality can also make the pins infeasible.

### 4.1 Exact sharpness inside the actual 3x+1 graph

Take N=27. Initially E={1,5}, so the physical core path sets b(5)=0. The only
one-pin is the ray of 27, at phase 27/16 and height 4. Its exact minimum is

    eta_{1,5}(27)=2W_4=2theta-205/72.                    (11)

Now import the actual edge 27->41. The fresh ray 41 has phase 41/32 and height 5.
The exact new value is

    eta_{1,5,27}(27)=2W_4+2W_5=4theta-5197/900.          (12)

Therefore the increase is precisely

    2W_5=2theta-5269/1800,                              (13)

attaining (10).

Here is a direct proof of optimality, not a numerical guess. If b(3)=0, the
ordered phase points

    5/4 (zero), 41/32 (one), 3/2 (zero), 27/16 (one), 2 (zero)

force four changes at every shell k>=5, and 27 forces two at shell 4. This costs
at least 2/25+4W_5=2W_4+2W_5. The coloring one exactly on odd rays 27 and 41
attains it. If b(3)=1, every shell k>=1 has at least two changes, costing 2W_1.
That is strictly larger: the difference is

    2W_1-(2/25+4W_5)=2*(1/4+1/9+1/16-W_5)>0,

using W_5<1/5. This proves (12) and also (11) by the single-pin lower bound.

In the previous PIN-ONLY problem, the forced phase 41/32 appears between a zero
and a one and creates no new circular alternation. Its infinite relaxed cost is
still 2W_4. Thus (13) is an exact, strictly positive gap between that relaxation
and the problem retaining ALL halving constraints. No earlier theorem is
corrected: SC-002 expressly restricted its equality claim to the pin-only model.

## 5. DC-004: a small old color can change at an enormous height

Take N=7, p=3 and E={1,7}, retaining the physical odd edge 7->11 and the core
edge 1->2. No other odd edge is imposed. For K>=3, (6) becomes the explicit formula

    eta_(E,K)(7)=min(2 H_(K+1)-2, 4 H_(K+1)-47/9).      (14)

If b(3)=1, there are at least two changes from level 1 onward; the first branch
is attained by coloring every non-power-of-two integer one. If b(3)=0, source
7 forces two changes at level 2, and the phases

    1 (zero), 11/8 (one), 3/2 (zero), 7/4 (one), 2 (zero)

force four from level 3 onward. Coloring exactly rays 7 and 11 one attains the
second branch. These two cases exhaust all possibilities, proving (14).

The breakpoint is the rational value

    H_(K+1)=29/18.

Exact rational sums give

    H_29 < 29/18 < H_30.

Consequently every optimizer has b(3)=0 for 3<=K<=28, and every optimizer has
b(3)=1 for K>=29. The first new cutoff is 2^(K+1)=2^30. The infinite optimum is
2theta-2 and is on the b(3)=1 branch. The strict inequality theta>29/18 follows
already from H_30; no decimal or equality assumption is needed.

This proves that freezing an old optimal coloring and only assigning newly
exposed vertices is not an exact optimization rule, EVEN WHEN the odd-edge set
is fixed. An old small value must sometimes be repaired because of the cost of
its arbitrarily many dyadic descendants. The full Collatz graph of 7 has many
additional edges and converges at a small height; (14) does not concern its full
stopping time, its full anchored cost, or a least counterexample.

## 6. DC-005: finite complete-edge refinement and its certified stopping condition

At a fixed H=2^(K+1), let

    E_H={odd n<=H: T_p(n)<=H}.

Start with a subset E containing the core and repeatedly do the following:

1. Solve the all-halving completion with retained odd edges E at horizon K.
2. If the pins connect, return the literal physical path.
3. Otherwise evaluate its canonical extension on EVERY odd edge in E_H.
4. If all equalities hold, return the cut-flow certificate as the FULL finite
   optimum. If some fail, insert at least one violated edge and repeat.

The objective is nondecreasing. A violated equality has its endpoints in different
current equality components, so insertion merges components and never repeats an
already retained equality. Therefore uncapped refinement at fixed H terminates
after at most |E_H| new-edge insertions. A batch may insert several at once.

If there are no violations, the relaxed minimum is also the full minimum: it is
a lower bound by relaxation and its explicit coloring is a full feasible upper
witness with the same cost. No assumed extension to an infinite full coloring is
used. Conversely, pin incompatibility is a literal finite convergence certificate.
A round cap gives UNRESOLVED_AT_ROUND_CAP, not convergence or nonconvergence.

**The finite oracle scans the odd integers through H.** Only the optimizer for a
specified finite E is compressed independently of H. This pass does not provide
a sublinear all-odd-edge separation oracle, and does not claim to check all odd
edges below a symbolic height such as 2^1025.

The retained controls recover 27's actual 70-step shortcut path (peak 4616) at
H=8192, unlike the two permanently disjoint deterministic ladders. This is a
bounded completeness check, not a new theorem that every input is covered.
The p=5 source 13 retains a finite feasible full cut at the tested finite heights;
its separate literal positive cycle is not erased by identifying exterior states
with the core.

## 7. DC-006: which uniform upper bounds remain possible?

### 7.1 An order-independent upper repair budget is FALSE

Take the fixed ordinary source N=27. Let E_j contain the two finite inverse
ladders of the preceding sparse-capacity packet through depth j, their original
anchor edges, and the core. Include all halving equalities, as throughout this
pass. The old SC-005 proof establishes that their ray sets stay disjoint for all
j, although 27 actually converges. Thus eta_(E_j)(27) stays feasible for every j.

The old SC-002/004 forced-ray lower bound applies to these exact same ordinary
paths. It exceeds every fixed budget along sufficiently long finite prefixes.
Our all-halving exact value is at least that lower bound. Therefore

    sup_j eta_(E_j)(27)=infinity,

while all these values are finite. This refutes a C_27 upper bound uniform over
ARBITRARY finite selections of actual odd edges, even if they are nested.

It also refutes a bound uniform over ALL fair orders of eventual full-edge
insertion. Given any budget, first insert a sufficiently long E_j, then enumerate
every remaining odd edge. That order is fair and ultimately includes the actual
convergence path, but already exceeded the proposed budget before doing so.
Fairness alone does not supply an order-independent repair bound.

This conclusion is credited to the earlier infinite-ladder geometry plus the
present exact completion interface; it is not a newly claimed nonconvergent source.

### 7.2 The elementary fresh-ray upper ledger is not summable by itself

The terms in (10) are costs AVAILABLE as upper bounds, not compulsory increments.
If one tries to pay separately for infinitely many consecutive fresh forward
odd targets, the following limitation applies. Along actual accelerated odd steps
an original positive source obeys
x_(j+1)<=2*x_j for p=3, so h(x_j)<=h(x_0)+j. Since W_h>=1/(h+1), adding the crude
fresh-ray allowances separately along an infinite ordinary path would give

    sum_j 2W_(h(x_j)) >= sum_j 2/(h(x_0)+j+1)=infinity.

For p=5, x_(j+1)<=3*x_j gives h(x_j)<=h(x_0)+2j, and the same harmonic comparison
gives the same
conclusion. This does NOT lower-bound the actual optimized increments: many are
zero, and global repainting can reduce the increase. It shows why summing the
local allowances without sharing or amortization cannot deliver a finite budget.

### 7.3 The intended complete-height target survives, still OPEN

For complete height cutoffs E_H, not arbitrary schedules, define eta_H=eta_(E_H).
Their pin feasibility is identical to that of the old full finite graph G_H:
all odd edges have their literal endpoint below H, and normalization uses only
halvings below H. Also

    eta_H(N) >= kappa_H(N).

The old finite-energy/anchored-cost theorem implies divergence of these finite
costs if N never converges. If N does converge, its finite path is included for
all sufficiently large H, and only finitely many feasible cutoff heights remain.
Consequently the source-qualified assertion

    sup_{H>=N : eta_H(N)<infinity} eta_H(N) < infinity    (15)

is equivalent to convergence of that fixed source (an empty feasible set is
harmless). For the forward implication use the preceding lower divergence; for
the reverse use the actual finite convergence path, not a universal stopping bound.

**No proof of (15) is supplied here.** The exact optimizer and the sharp bound
(10) supply a concrete framework for seeking an amortized repair inequality
specifically for complete height cutoffs or a specified successful schedule.
The required cancellation/sharing must use additional actual arithmetic; none of
the geometric compression, finite-constraint regularity, or parameter-envelope
arguments distinguishes p=3 from p=5 by itself.

The next useful deliverable is a height-uniform bound on the SUM of optimized
increases before pin infeasibility, with one unchanged original N. It must allow
old-label changes (DC-004), not demand a bound valid for all insertion orders
(DC-006.1), and not replace the optimized increases by the nonsummable fresh-ray
allowances (DC-006.2).

## 8. Sources, evidence and review boundary

New source snapshot: this packet is additive to PR #138 at full SHA
`45c970ccb3d0b034f6e5696710d9a94df66b2b27`; source branch
`research/anchored-cuts-constructive-20260925`. Main, #137, old proofs and old
validation receipts are not amended or promoted. AGENTS was read at that parent.
The resident map and scoped errata supplied in the preceding context retain their
qualifications; no corrected mass/rank theorem is a premise here.

Exact dependencies:

* `../anchored-cuts/PROOF.md`, FC-004--007: full finite anchored costs and their
  divergence/closing boundary, used only in Section 7.3.
* `../sparse-capacity/PROOF.md`, SC-002/004/005: forced-ray lower certificates and
  the all-depth 27 obstruction, used only in Section 7.1.
* DC-001--005, the tail formula, and the two sharp fixtures are proved directly
  here. Max-flow/min-cut methodology itself is standard and not claimed as new.
  A matching feasible cut and flow is checked by its elementary divergence
  identity rather than relying on the producer's implementation.

`run.py` generates exact completion certificates and finite complete-edge
refinement traces. `verify.py` imports neither the generator nor a flow solver;
it reconstructs the graph by rational interval bisection rather than an ancestor
trie, labels equality components by traversal rather than union-find, verifies
all primal/dual constraints, replays actual paths, and checks the finite oracle
at every retained refinement round.

`check_models.py` deliberately imports the producer to compare it with exhaustive
ordinary-ray assignments, direct terminal-perimeter sums, the sharp fresh-ray
example, the exact phase-transition formula, and the preceding integer-capacity
full-graph implementation. These checks are bounded implementation evidence, not
proof by extrapolation, external priority confirmation or independent peer review.
The executed inventory and command receipts are in VALIDATION.json.

No complete authenticated checkout was available: direct Git failed DNS.
No complete-checkout root validator, remote CI or formal proof build is claimed.
The remote file hashes and branch head must be checked after publication before
claiming that this pass landed.

# Exact dyadic elimination and constructive odd-edge repair

**25 September 2026. DR-001--006: PROPOSED; not independently reviewed.**
This pass does not prove Collatz or the missing height-uniform upper bound for
full anchored cuts. It changes the executable finite-constraint object: every
halving edge is now enforced, unobserved dyadic subtrees are eliminated exactly,
and a false finite-step separator produces a specific missing actual odd edge.

## 0. Scope, provenance, and the first unsupported step

Use the unabsorbed shortcut map on ordinary positive integers

    T_p(n) = n/2 (n even), (p*n+1)/2 (n odd), p in {3,5}.

The initial source N is fixed throughout. All constraints introduced by the
research solver are literal edges of this map, with the necessary halving paths.
The 5x+1 system is a countercontrol, not a transfer argument proving 3x+1.

Inspected parent: PR #138, branch `research/anchored-cuts-constructive-20260925`,
head `45c970ccb3d0b034f6e5696710d9a94df66b2b27`. This continues, without modifying,
`../sparse-capacity/PROOF.md` (SC-001--006) and `../anchored-cuts/PROOF.md`
(FC-001--007). The selected inverse ladders, their logarithmic geometry and
critical exponent are credited there, not re-proved or claimed as new here.
AGENTS and the parent source were read. The research map and scoped errata
were available in this conversation; none of the corrected mass/rank/realization
statements is a premise in the new proofs.

The parent's R_(K,s) is an exact **pin-only** minimum. It deliberately does not
impose halving equalities on all unpinned integers. The new Lambda problem does.
Section 4 exhibits a strict difference, so these minima cannot be interchanged.

The new theoretical interface has three parts:

* a finite network giving the exact finite- or infinite-horizon minimum under
  ALL halving equations and any specified finite collection of odd equations;
* a constructive missing-edge theorem for every nonconstant dyadic step
  completion, with explicit bounds on the source and physical peak;
* a refinement implementation that can add such missing equations, retaining
  unresolved cases and checking any asserted convergence by literal replay.

**First unsupported step:** there is no proof that adding the newly found odd
edges has a summably bounded repair cost, or forces pin inconsistency for every
ordinary N. The root-fair policy described below retains ordinary trajectory
progress; its success for a convergent N is a consequence of that convergence,
not a new theorem proving convergence. The same general constructions apply to
5x+1. A successful universal argument must distinguish the full 3x+1 arithmetic.

No external priority claim is made. Generic maximum-flow/minimum-cut duality
and level-set coarea are standard, not discoveries of this packet. Historical
primary reference: L. R. Ford Jr. and D. R. Fulkerson, *Maximal Flow Through a
Network*, Canadian Journal of Mathematics 8 (1956), 399--404,
DOI 10.4153/CJM-1956-045-5. Its publisher record was checked in this pass:
https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/maximal-flow-through-a-network/5D6E55D3B06C4F7B1043BC1D82D40764 .
The weak flow/cut certificate inequality needed computationally is also stated
explicitly below. The publication year is 1956, not its 2018 online-posting date.

## 1. DR-001: the exact dyadic interval representation

Write odd(n)=n/2^v2(n), h(n)=floor(log_2 n), and

    u(n)=n/2^h(n) in [1,2).

This is an exact rational, not a floating-point logarithm. u(m)=u(n) precisely
when m/n is an integral power of two. Thus b(2n)=b(n) for every n is equivalent
to a function on the ordinary dyadic points of the multiplicative circle
[1,2] with endpoints identified. Every such point has a unique odd representative.

For k>=0 let

    V_k(b)=sum_(n=2^k)^(2^(k+1)-1) |b(n+1)-b(n)|,
    w_k=1/(k+1)^2,
    E_K(b)=sum_(k=0)^K w_k V_k(b),
    E_infinity(b)=sum_(k>=0) w_k V_k(b).

The k-th circle is subdivided into 2^k intervals with endpoints
1+j/2^k. Its circular variation is exactly V_k: the endpoint 2 represents the
same ray as 1, and the last adjacency edge of the shell is retained. At k=0
this is a loop with zero cost. One refinement inserts each midpoint; all old
vertices keep their value. Different shells are therefore coupled.

Let F be a finite set of positive odd sources. Impose

    b(a)=b(odd(p*a+1)) for every a in F,                  (1)
    b(1)=0, b(N)=1.                                    (2)

Equation (1), together with ALL halving equalities, is precisely the collection
of literal shortcut odd equations for F. It includes the halving path after
the first step, not an invented accelerated physical clock. The largest state
on that arm is max(a,(p*a+1)/2).

Let Lambda_(F,K)(N) be the minimum E_K subject to these equations and all
halving equalities. Let Lambda_(F,infinity)(N) be the analogous minimum total
energy. Infeasible pins have value +infinity. Additional Boolean pins may be
used in algebraic control examples; these are explicitly not claims about the
single-source full Collatz graph.

For finite K all marked odd representatives must be below 2^(K+1). The
infinite formulation has no finite-height cutoff. If H=2^(K+1), every retained
physical odd arm is inside H, and the only pins are (2), then

    Lambda_(F,K)(N) <= kappa_H(N).                       (3)

Indeed, the left constraints are a subset of the full G_H constraints after
contracting all its halving edges. Do NOT use (3) if an odd arm leaves H, or
if extra pins were imposed. In particular the infinite energy Lambda_(F,infinity)
is NOT automatically a lower or upper bound for a particular finite kappa_H.

## 2. DR-002: eliminate every unmarked dyadic subtree exactly

Mark the odd rays of the pins, every a in F, and every odd(p*a+1). Include 1.
For each marked phase retain all dyadic interval ancestors required to expose
that phase as a midpoint. These ancestors form a finite binary subdivision.
Unmarked interior vertices in the remaining terminal intervals are not stored.

An interval at depth d has one adjacency edge at level d, two at level d+1,
and so on. Define

    W_(d,K)=sum_(k=d)^K w_k,
    W_(d,infinity)=sum_(k=d)^infinity w_k.                (4)

**Two-terminal elimination lemma.** In a depth-d interval containing no marked
interior vertex, the minimum energy of all its refinements with endpoint values
A,B in {0,1} is

    W_(d,*) * |A-B|.                                    (5)

Proof. At every finer level the finite chain joining the endpoints has total
variation at least |A-B|. Sum with the nonnegative level weights. For equality,
assign every unmarked interior dyadic point the value A and retain B at the
right endpoint. If A!=B there is exactly one change in that interval at each
level; otherwise none. This single assignment is compatible at ALL refinements.
The infinite weighted sum converges, so (5) also holds at infinite horizon.
The same argument works for real A,B with intermediate values chosen between
them. QED.

Build a network as follows. Every retained midpoint is a vertex; the two outer
endpoints are the single core vertex. Every split interval at depth d contributes
an edge of capacity w_d between its endpoints. Every terminal interval contributes
one edge of capacity W_(d,*). Contract the finite physical equalities (1). Wire
same-color pins together and impose their two distinct pin values. Parallel
capacities are added; loops contribute zero.

**DR-002.** The minimum cut of this finite network is exactly Lambda_(F,*)(N),
including at infinite horizon.

Proof. Restrict any admissible b to the retained vertices. Each terminal subtree
has energy at least (5), and every split-interval edge is charged exactly once.
This gives the network lower bound. Conversely, take any network coloring and
complete every terminal interval by the assignment in the lemma. The intervals
have disjoint interiors, and their shared endpoints keep the prescribed labels.
The result satisfies ALL halving equations and all finite equations (1), with
energy exactly the cut. There are finitely many network colorings, so the
minimum is attained. QED.

The completion is a right-continuous finite step function on [1,2), constant
inside each terminal interval with the label of that interval's left endpoint.
There are no isolated exceptional point values: a marked endpoint has the same
value as the interval immediately to its right. The seam has the core value.

**Size bound.** If the marked odd representatives are m_i, and S is the number
of split intervals, then

    S <= sum_i h(m_i),
    vertices <= S+1,
    terminal intervals = S+1,
    interval-edge records = 2S+1.                       (6)

Each mark contributes at most its depth many ancestors; shared ancestors are
counted only once. Subsequent contractions cannot increase the vertex count.
No enumeration up to the largest integer represented by a mark is involved.
This is a bound on network size, not on the number of future refinement rounds.

### An exact local repair identity

Suppose an unmarked terminal interval at depth d is split and its midpoint is
given a value B, with endpoint values A,C. Before the split its effective cost
is W_d |A-C|. Afterwards it is

    w_d |A-C| + W_(d+1)(|A-B|+|B-C|).

Since W_d=w_d+W_(d+1), the excess is

    W_(d+1)(|A-B|+|B-C|-|A-C|).                         (7)

For Boolean values this is either zero or 2 W_(d+1). It is positive exactly
when equal-colored endpoints acquire an opposite-colored midpoint. At the
critical weight W_(d+1) is of order 1/(d+1), with elementary integral bounds.
This is an exact local identity BEFORE a new nonlocal physical equality ties
vertices together. It is not a global upper bound on an optimized repair:
nonlocal identifications can require recoloring many intervals or make the
original pins inconsistent.

## 3. DR-003: certified infinite-horizon cuts without irrational arithmetic

The capacities in the infinite network contain the common tail of sum 1/j^2.
There is no need to replace them by unjustified floating-point values.
Choose an integer L greater than every retained depth. Elementary integral
comparison gives

    1/(L+1) < sum_(j=L+1)^infinity 1/j^2 < 1/L.

For each terminal interval at depth d use lower and upper capacities

    W_d^- = sum_(j=d+1)^L 1/j^2 + 1/(L+1),
    W_d^+ = sum_(j=d+1)^L 1/j^2 + 1/L.                  (8)

Split-edge capacities are unchanged. Solve the lower rational network exactly.
Let C be its minimizing cut, ell its value, and u the upper capacity of this
same cut. Then

    ell <= Lambda_(F,infinity)(N) <= E_infinity(b_C) <= u,
    u-ell <= (S+1)/(L(L+1)).                            (9)

The first inequality is monotonicity of a cut minimum under capacity increases.
The middle upper bound uses the explicit dyadic completion from Section 2.
Only terminal intervals crossing C contribute uncertainty, each at most
1/(L(L+1)), proving the error estimate. Thus arbitrary absolute precision is
available by increasing L. The selected rational-network minimizer need not be
an exact minimizer of the infinite network; only the certified enclosure (9)
is reported. Finite-horizon computations are exact rationals with no tail error.

The code scales all lower capacities to integers and solves that network.
The certificate contains a cut and a signed undirected edge flow f_uv satisfying

    |f_uv| <= c_uv^-,
    sum_v f_uv = 0 except at the two pins.

For any separating cut, summing conservation over its source side proves that
its capacity is at least the flow value. Equality with the displayed cut proves
optimality of the LOWER rational network. The standalone checker verifies that
identity directly; it neither imports nor reruns the author's flow solver.

Coarea also shows that allowing 0<=f<=1 does not improve the minimum:

    |f(x)-f(y)| = integral_0^1 |1_(f(x)>t)-1_(f(y)>t)| dt.

All finite physical equalities persist under these level sets, and pins remain
0 and 1. Nonnegative summation permits the same argument at infinite horizon.
This is a lossless real relaxation, not smoothing away an exceptional source.

## 4. A strict correction to pin-only intuition, not to the parent's theorem

Pin b(1)=0 and b(5)=b(7)=1, and retain no odd equations. At horizon K=2, the
parent's pin-only formula is 2/9. It is not attainable under every halving law.
The still-free ray of 3 appears at the preceding level and has ONE common value
at every later level. Write

    A_K = sum_(j=3)^(K+1) 1/j^2.

If b(3)=0, the minimum is 4 A_K. If b(3)=1, it is 1/2+2 A_K. Therefore

    Lambda_K = min(4 A_K, 1/2+2 A_K).                   (10)

At K=2 this gives 4/9, strictly exceeding 2/9. The choice b(3)=0 is optimal
through K=5; b(3)=1 becomes optimal at K=6. The exact inequalities are A_5<1/4
and A_6>1/4. At infinite horizon the optimal value is

    1/2 + 2 sum_(j=3)^infinity 1/j^2,

and b(3)=1. Its superiority follows already from A_6>1/4. These formulas follow
also by the eliminated four-terminal network and are checked exactly.

This illustrates lookahead coupling: a choice at an early unpinned dyadic ray
can trade a small early cost against all later shells. The parent correctly
labeled its formula a relaxation; no parent assertion is being retracted.

## 5. DR-004: every nonconstant finite dyadic step completion has a small defect

Let g be a nonconstant right-continuous Boolean step function on [1,2), viewed
as a multiplicative circle. Suppose every endpoint of its finitely many intervals
belongs to the grid 1+2^(-K) Z, with K>=1. Define

    b(n)=g(u(n)).

It automatically satisfies every halving equation. Define the circle rotation

    R_p(x)=normalize(p*x) into [1,2).

Writing r=floor(log_2 p), its two branches divide p*x by 2^r or 2^(r+1).
All calculations here use rational multiplication and comparisons; logarithms
are used only to identify the rotation's irrationality abstractly.

### There must be a nonempty open mismatch interval

If g(x)=g(R_p(x)) off the finitely many discontinuities and their preimages,
the finite nonempty set of genuine jump points would be preserved by R_p.
A finite permutation has a periodic point. Such a point would imply

    p^j = 2^a for some j>=1 and integer a,

contradicting unique prime factorization for p=3 or p=5. The jump set is nonempty
because a nonconstant finite step function on a circle has a genuine jump.
Thus there is an open interval on which g and g composed with R_p differ.
This argument concerns the finite step completion, not an arbitrary rough
invariant coloring of the ordinary integers.

Overlay the endpoints of g, the preimages of these endpoints under both
branches of R_p, and the multiplicative seam. Every overlay point belongs to

    (1/(p*2^K)) Z.

Consequently every nonempty consecutive overlay interval (a,b) has width at
least 1/(p*2^K). On it, both g(x) and g(R_p(x)) are constant. A mismatch interval
can be found by sorting these rational endpoints and evaluating at midpoints.

### Turn that interval into an actual odd edge

Choose c with 2^c>2p+1; use c=3 for p=3 and c=4 for p=5. Put h=K+c. In a
mismatch interval (a,b), choose the least odd integer n strictly greater than
2^h a. Then n<=2^h a+2, and the interval-width bound gives

    n+1/p < 2^h b.                                     (11)

Indeed, 2^h(b-a)>=2^c/p>2+1/p. Thus x=n/2^h and
x+1/(p*2^h) both belong to the same overlay interval. The latter shift is
exactly the correction from p*n to p*n+1. Therefore

    b(n) != b((p*n+1)/2).                              (12)

The division by two does not change the normalized phase. Equation (12) is an
actual omitted shortcut edge, not a defect of a smoothed approximation.

**DR-004.** A violated odd edge is constructible with

    2^(K+c) <= n < 2^(K+c+1),
    max(n,T_p(n)) < p*2^(K+c).                         (13)

For 3x+1, n<16*2^K and the physical peak is <24*2^K.
For 5x+1 the corresponding bounds are 32*2^K and 80*2^K.
The terminal-network coloring already satisfies every retained odd equation,
so this violated edge cannot already have been retained.

The implementation first tries marked odd rays, preferring the component of
the SAME original source; any found violation has an even smaller source bound.
If none exists, it uses (11). An explicit rotation-only mode tests (11) even
when the faster marked check could have succeeded.

This theorem eliminates every finite dyadic-step separator constructively.
It does not eliminate arbitrary infinite-resolution separators. Refinement may
make K increase indefinitely. This boundary is essential.

## 6. DR-005: a repair procedure, and why ordinary-source fairness remains needed

Start with a finite set F containing the known core cycle (odd source 1 for
3x+1; odd sources 1 and 3 for 5x+1). Optionally include a finite prefix of the
parent's two inverse ladders, preserving their original-source anchors.

If the pins are consistent, solve the rationally bounded infinite network,
construct its step completion, find a violated edge by Section 5, and add that
actual odd source to F. Re-solve after every insertion. The source N does not
change. No insertion is allowed to reset its meaning or replace it by a nearby
successful parameter.

Every violated-edge round excludes its current candidate coloring. That is
NOT a proof of finite termination: the next coloring can introduce finer
intervals and satisfy all old constraints. In the retained cuts-only control,
N=27 is still unresolved after 64 rounds despite its actual convergence. This
is a finite observed failure, not a theorem of all-time failure of this new
refinement policy.

In particular, a currently SATISFIED odd edge can still be necessary for making
a finite proof. Restricting insertions only to violated edges need not prioritize
that edge. The preceding all-depth two-ladder obstruction motivates testing
this explicitly rather than calling candidate exclusion a termination rank.

The delivered default is **root-fair**: alternate a violated-edge insertion with
the next missing odd edge on the original N trajectory as far as the retained
arrows already determine it. The latter edge is added even if the current step
completion already satisfies it. The root's physical clock never resets.
A finite retained component containing the known core cycle cannot also have
a different terminal exit: a finite partial functional graph has one terminal
cycle or exit per weak component. Thus pin inconsistency supplies a literal
recorded path from N to 1. This path, not a flow value, is the convergence
certificate. A different fully recorded cycle is also literally replayed.

**DR-005, limited termination statement.** If N in fact converges and its
forward orbit has q odd steps before reaching 1, root-fair insertion resolves
it after at most 2q+2 iterations (often fewer because other insertions already
supply some arrows). Each scheduled root insertion advances to a new missing
odd edge of that SAME finite trajectory. This is not an independent proof that
q is finite and is not a new stopping-time bound. A repeated non-core odd state
in retained root exploration supplies an actual other cycle instead.

A finite round cap produces UNRESOLVED_AT_RESOURCE_CAP. There is no claim that
root-fair insertion exhausts all odd edges on all integers; no compactness
argument here treats it as that exhaustive family.

## 7. DR-006: what the new repair identity does and does not buy

DR-002 removes the false freedom to recolor old dyadic rays independently at
later scales. DR-004 also removes the need to guess which odd equation the
current finite-step candidate violates. Neither has established a uniform upper
bound for the FULL anchored cut problem.

Equation (7) isolates a plausible next accounting task. A local birth at depth d
costs about 2/d in the infinite network, but physical equalities couple distant
intervals. A useful next theorem must control how frequently these births are
forced and how later recolorings repay earlier ones, for one fixed ordinary
source, under the actual 3x+1 equations. Summing a bound of order 1/d over every
depth is not sufficient. Nor may a cost bound for the lower rational network be
silently applied to the infinite network without (9).

The 5x+1 negative controls are decisive scope tests: the same dyadic elimination,
local cost identity, tail enclosure, and finite-step defect oracle all hold
there. Its two additional tested cycles persist under literal replay. Therefore
these theorems do not supply the distinguishing 3x+1 arithmetic by themselves.

## 8. Evidence, replay, and status

`run.py` generates exact cuts, explicit step completions, actual edge witnesses,
and retained refinement histories. `tests.py` compares the finite elimination
with direct exhaustive Boolean assignments, checks the lookahead example,
exhaustively tests low-depth step-function oracles, and retains positive,
negative and unfinished adaptive runs. The corpus is reproducible rather than
committed as a large payload.

`verify.py` imports neither generator nor maximum-flow code. It reconstructs the
subdivision by rational interval recursion instead of the generator's ancestor
trie, obtains physical components by graph traversal instead of union-find,
checks all lower/upper capacities, checks signed-flow conservation against the
cut, validates original sources and all inserted actual edges, and replays all
asserted convergence/cycle paths. Its semantic mutations are applied directly,
not rejected merely by a changed payload checksum. Checks remain active under
optimized Python. Same-author implementation diversity is not independent
mathematical review.

The full finite/horizon and oracle claims are proved above. The computations
check only their stated finite inventories and implementations. See VALIDATION.json
for actual commands, hashes, counts, and failures. No full-repository validator,
remote CI, Lean build, or external priority audit is claimed. No parent proof,
canonical scientific status, workflow, settings, licensing, or main-branch file
is changed by this packet.

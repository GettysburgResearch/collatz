# Two inverse ladders, exact ray capacities, and the critical exponent two

**25 September 2026. SC-001--006: PROPOSED, not independently reviewed.**
No complete Collatz proof and no height-uniform upper bound for the full anchored
cut problem. The results below are elementary consequences of the stated exact
constructions, not extrapolations from the numerical corpus. External priority
has not been established.

## 0. What changes, and what does not

The preceding [anchored-cut packet](../anchored-cuts/PROOF.md), FC-003--007,
formulates a full finite graph problem and proves that its separation costs
escape, using finite-energy rigidity and a compactness argument. This pass gives
a substantially smaller, constructive source of that escape: **two deterministic
inverse ladders already suffice**, with exact certificates requiring no enumeration
of the ambient interval and no maximum-flow solve.

Their pin-only relaxation has a closed-form minimum expressed by circular color
alternations. The corresponding infinite sparse graph has a sharp energy
threshold: separation has finite energy above exponent two, and necessarily
infinite energy at or below two, unless a finite ray collision has already given
a merger. An explicit finite-height recipe replaces the compactness extraction.

A necessary limitation is proved within 3x+1 itself. The selected ladders for
27 and 1 never meet, although 27 reaches 1. Thus sparse capacity escape is not
merger-completeness, even when every retained edge is an actual 3x+1 edge. The
missing upper repair theorem for the **full** graph remains OPEN.

### Source and normalization pins

The preserved anchored packet was published in #138 at
`9d9f30ef199d32045b1f78a87ecbc53f824346aa`, based on #137 at
`2911b53930cbd31f623d3e0586ca3613854f0143`. Main was read at
`ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`. The original component geometry
in `../pass1/PROOF.md` is credited. The distinct residue-locked continuation
`../pass2/PROOF.md` was read and is not overwritten or claimed as new here.
No corrected mass/rank result is used as a premise.

Use the unabsorbed shortcut map

    T_p(n)=n/2 if n is even; (p*n+1)/2 if n is odd, p in {3,5}.

G_H contains 1,...,H and every actual T_p edge with both endpoints in that
interval, with no exterior wiring. A separator has b(1)=0,b(N)=1 and is constant
on G_H components. Its energy is

    E_H(b) = sum_{n=1}^{H-1} |b(n+1)-b(n)| / bitlength(n)^2.

Let kappa_H(N) be its minimum, or +infinity when the pins merge. H is an
ordinary value cutoff, not a trajectory clock. Independent clocks on the two
original arms are preserved. All new statements concern one fixed ordinary N.

## 1. SC-001: deterministic ordinary inverse ladders

For any original source M, obtain a unit Y modulo p as follows. If p does not
divide M, use Y=M. Otherwise halve M to its odd part u and take
Y=(p*u+1)/2, retaining that actual forward path. If Y=1, use seed y_0=5 for
p=3, with path 5->8->4->2->1, or seed y_0=3 for p=5, with path
3->8->4->2->1. Otherwise use y_0=Y. Thus y_0>=2, p does not divide y_0,
and its component linkage is to the SAME original M.

For each current y choose the least k>=k_min with

    z=(2^k*y-1)/p an integer not divisible by p,
    k_min=2 for p=3, and k_min=3 for p=5.

This gives the deterministic successor F_p(y)=z. Since two generates the units
modulo p, integrality prescribes one k class modulo p-1. Among the first two
admissible k values, at least one gives p not dividing z: if 2^k*y=1 mod p^2,
multiplication by 2^(p-1) does not preserve 1 mod p^2. Explicitly
2^2=4!=1 mod9 and 2^4=16!=1 mod25. Consequently

    2<=k<=5 (p=3);       3<=k<=10 (p=5).

The resulting z is odd and positive, with literal physical word

    T_p^k(z)=y: one odd step followed by k-1 even steps.

Moreover

    (5/4)*y <= z < 2^8*y.                                (1)

For p=3 and k=2, integrality requires y=1 mod3, hence y>=4, and
(4y-1)/3>=5y/4. Larger k have more growth. For p=5 the minimum numerator
already gives (8y-1)/5>=3y/2 for y>=2. The upper bound follows from k<=10
and 2^10/5<2^8, or k<=5 and 2^5/3<2^8. The sharper upper bound 2^4 holds
for p=3, but the common 2^8 simplifies the uniform construction below.

Thus each fixed M produces an infinite, growing, actual backward ladder
(y_j). Each edge has a uniformly bounded physical clock; its integers have
bit-length O(j+log M). After the first step its nodes are odd.

### Logarithmic phase and a uniform tail

Writing alpha=log_2 p and K_j=sum_{i<j} k_i gives the exact identity

    log_2 y_j = log_2 y_0 + K_j - j*alpha + e_j,
    e_j = sum_{i<j} log_2(1-1/(2^k_i*y_i)).                (2)

For 0<=u<=1/8, -log_2(1-u)<=2u. Equation (1), y_0>=2 and k_i>=2 therefore give

    |e_infinity-e_j| <= 5/(2*y_j) <= (5/4)*(4/5)^j.      (3)

Modulo one, (2) is an irrational rotation plus a convergent perturbation.
Irrationality uses only unique prime factorization. The quantitative finite
version needed below is proved in Section 4 rather than assumed probabilistically.

## 2. SC-002: an exact closed-form minimum for the ray-pin relaxation

Take finitely many labeled positive ray bases (y,b), b in {0,1}, including
(1,0), and impose b(2^t*y)=b for all t>=0 within the finite interval. A base y
activates in shell h(y)=bitlength(y)-1. Its phase is the exact rational

    u(y)=y/2^h(y) in [1,2).

Two phases are equal exactly when their bases have the same odd part. Opposite
labels on an equal phase are incompatible when both rays have become active.
Suppose no such collision occurs, and choose K at least every activation height.

At shell k, list the distinct active phases in increasing order. Phase 1 is
always present with color zero. Let c_k be the number of **circular** changes of
color, including the last phase back to phase 1. It is even. The integers in the
shell carrying these pins are 2^k*u(y); the next endpoint 2^(k+1) is also pinned
zero by the original ray of 1.

For any positive real s, the exact minimum among all Boolean assignments
satisfying JUST these ray pins on 1,...,2^(K+1) is

    R_(K,s) = sum_{k=0}^K c_k/(k+1)^s.                  (4)

This is a pin-only relaxation: unpinned vertices are free, and it does not impose
all Collatz edges or all dyadic equality constraints on unpinned vertices.
It is not asserted to equal the full kappa_H.

*Proof.* Each consecutive pair of pinned integers of opposite colors forces at
least one change on the intervening adjacent edges. These intervals are disjoint.
All edges in one dyadic shell carry the same weight (k+1)^(-s), including the edge
just before 2^(k+1). There are exactly c_k forced intervals in that shell.
Conversely use a constant value between same-colored pins and exactly one change
between opposite-colored pins. Assign shells independently; their common
power-of-two endpoints are all zero. This attains (4). QED.

### Circular births and a second exact formula

Inserting a new phase of color b between colors a,c changes the alternation count by

    |a-b|+|b-c|-|a-c| in {0,2}.

Equal same-color phases add no change. Accordingly there are nonnegative integers
beta_k with c_k-c_(k-1)=2*beta_k, taking c_(-1)=0. Changing the insertion order
within one activation shell does not change the final c_k or beta_k. Then

    R_(K,2) = 2*sum_{j=0}^K beta_j * sum_{k=j}^K 1/(k+1)^2.       (5)

These beta are births in a circle of FORCED ray pins, not the parent's births
in the complete discrete derivative of an unknown global separator. They must
not be silently identified.

### Transfer back to the full arithmetic graph

Generate the two labeled ray families from the ladders of 1 (color zero) and N
(color one), including the original sources and the seeds. Retain every literal
anchor path and inverse-word path. Let P be their largest physical state and
choose

    H >= max(P,2^(K+1)).                                  (6)

Every pinned point below 2^(K+1) is connected within G_H to its original source:
first HALVE the dyadic multiple to its base, then use its retained paths. There
is no need to multiply the entire anchor path by the dyadic dilation. Hence

    kappa_H(N) >= R_(K,2).                                (7)

More generally, every real G_H-invariant function satisfies

    E_H(f) >= R_(K,2) * |f(N)-f(1)|.                      (8)

The disjoint forced intervals prove (8) by telescoping. They give an implicit
flow lower certificate without constructing the full quotient network. Equality
is claimed only for the pin relaxation (4), not for (7) or (8).

If two oppositely labeled rays coincide, the retained ordinary paths give a
finite physical merger of N with the core. Including the complete known core
cycle gives a finite partial functional graph; a component containing a closed
cycle cannot also have a terminal exit. Following its recorded outgoing arrows
from N therefore yields a literal finite path to 1. This is how the program's
CONVERGENCE outcome is certified; no conjectured stopping time is used.

## 3. SC-003: the sharp critical exponent is two

Take the TWO INFINITE deterministic ladders of Section 1. There are two cases:
a finite opposite-ray collision, or a consistent infinite family of ray pins.
Assume the second case in this section. Each finite shell has only finitely many
active ladder nodes, by (1), so c_k for the full infinite family is well defined.

Consider also a genuinely arithmetic sparse graph S: retain all halving edges,
the known core cycle, the original anchor paths, and the inverse-word paths of
these two ladders, but not every other odd edge of T_p. All its edges are actual
T_p edges. Distinguish this graph from the easier pin-only relaxation.

**SC-003.** In both the pin-only problem and this sparse graph, the infimum energy
of a separator with b(1)=0,b(N)=1 is finite for s>2 and infinite for 0<s<=2,
where the edge weight is bitlength(n)^(-s).

*Upper half, s>2.* Four inverse steps multiply size by at least
(5/4)^4=625/256>2. Therefore at most 4(k+1) nodes of each ladder can have
activation height at most k. Including the two original source rays gives

    c_k <= 8(k+1)+2 <= 10(k+1).                           (9)

Equation (4) gives a finite pin-only energy for s>2.
For S, let A be the odd parts of the original source N and all its ladder nodes,
and put b(n)=1 exactly when oddpart(n) is in A. No core-ladder ray is in A under
the no-collision hypothesis. This coloring respects every halving edge and every
retained inverse/anchor path, including the initial forward path when p divides N.
Thus it is S-invariant. In shell k it has at most 4(k+1)+2 ones: except for the
initial seed and source, all ladder nodes are already odd and obey the preceding
count. Its variation is at most 8(k+1)+4 (both shell endpoints are zero).
Its energy is consequently bounded by 12*sum_{k>=0}(k+1)^(1-s), which converges.
This upper bound concerns S, NOT the full Collatz graph.

*Lower half, 0<s<=2.* Section 4 constructs arbitrarily many disjoint height bands,
each contributing at least 1/576 to R_(infinity,2). Thus that energy diverges.
The forced-ray lower bound holds for any S-invariant separator as well, and
(k+1)^(-s)>=(k+1)^(-2) for s<=2. QED.

The exponent two is therefore not an arbitrary convenient weight in this sparse
geometry. It is its exact critical threshold. This classification holds for both
p=3 and p=5; by itself it supplies no arithmetic distinction between the maps.

## 4. SC-004: explicit finite certificates of arbitrarily large cost

We now prove the lower half without a compactness extraction. Let h_0 be any
integer at least the binary heights of the original sources, seeds, and all
initial anchor-path states. It is computable from the fixed original N.

Choose coprime a,q with q>=16 and

    |alpha-a/q| < 1/q^2,  alpha=log_2 p.

Put L(q)=4*bitlength(2q). Since (4/5)^4<1/2, equation (3) implies
|e_infinity-e_j|<1/q for all j>=L(q). For i=0,...,q-1 the logarithmic phases of

    y_(L(q)+i)

therefore lie within circular distance 2/q of one translated equally spaced
grid of q points: the rational rotation ia/q is a permutation of the grid,
the rotation-approximation error is <1/q, and the tail error is <1/q. Thus the
largest phase gap for EACH ladder is at most 5/q.

Partition the logarithmic phase circle into r=floor(q/8) equal half-open arcs.
Each arc has length at least 8/q>5/q and contains pins of both colors. If there
is no opposite-ray collision, each arc forces a color change. Once those nodes
are active, it follows that

    c_k >= floor(q/8) >= q/16.                            (10)

By (1) their heights are at most h_0+8(L(q)+q). Require in addition

    q >= h_0+8*L(q),                                     (11)

so they are all active by shell J_q=9q. Throughout the full height band
k=J_q,...,2*J_q-1, monotonicity of c_k gives

    sum c_k/(k+1)^2 >= (q/16)*J_q/(2*J_q)^2 = 1/576.     (12)

Choose such denominators successively with q_(j+1)>2*q_j. Their bands are
disjoint. At J bands the cost is at least J/576, unless a finite collision has
already certified convergence.

All the objects in this construction are effective finite ordinary objects.
The approximant test itself can be performed by exact integer arithmetic:

    2^(a*q-1) < p^(q^2) < 2^(a*q+1).                    (13)

Unbounded coprime approximants exist by the elementary pigeonhole proof of
Dirichlet approximation: among Q+1 fractional parts two lie in the same of Q
bins, giving |alpha-a/q|<1/(qQ)<=1/q^2 with q<=Q; reduction preserves the bound,
and the reduced denominators cannot remain bounded as Q grows. Condition (11)
and any preceding denominator threshold eventually hold. Exhaustive search
using (13) is consequently a terminating, though not practical, recipe.

For the final denominator q, generate both ladders through depth L(q)+q and take

    H = 2^(18q).

The displayed bands and their endpoints are below H. All ladder nodes have
height at most 9q, and inverse-word peaks are less than four times their source;
the anchor peaks were absorbed into h_0. Hence their physical paths also lie
below H. Earlier bands retain their constraints as more nodes are added.

**Constructive consequence.** For every fixed N>1 and rational budget M>=0,
choose J with J>576M, and apply this recipe. It returns either a literal merger
or a finite sparse certificate R_(K,2)>M for a completely explicit ordinary
height H. No graph on 1,...,H is constructed. This replaces the compactness-based
existence of a cutoff by an effective arithmetic recipe. It is NOT a convergence
algorithm: the second outcome excludes only the specified energy budget.

The practical program accepts a finite ladder depth and shell cutoff. Increasing
depth without bound and choosing K=2*(maximum active height+1) must eventually
cross any prescribed budget or encounter a ray collision: every fixed band in
(12) is eventually fully present. The delivered finite run does not claim a
successful result for every chosen finite depth.

The uniform constants are very loose. Exact finite controls instantiate (13)
with (p,a,q)=(3,1054,665) and (5,1154,497). These certify height bands inside
H=2^11970 and H=2^8946 respectively, using small lists of physical inverse clocks.
They are not enumerations of integers up to either height.

## 5. SC-005: a permanent completeness obstruction inside 3x+1

On positive odd units, F_p is injective. Indeed F_p(y)=F_p(y') implies
2^k*y=2^k'*y', and comparison of binary valuations gives k=k' and y=y'. It is
also strictly increasing ALONG EACH ORBIT, by (1); no order-preservation between
different inputs is asserted.

For p=3 the core ladder begins

    5 --k=3--> 13 --k=2--> 17 --k=5--> 181.

These arrows are inverse-ladder arrows, not forward T arrows. The other anchor
27 has the actual forward step 27->41 and starts its inverse ladder at 41.
The core ladder has passed 41 without hitting it. Injectivity implies that the
two subsequent odd ladders can never meet: cancel common F iterates at a
hypothetical first intersection, and either 41 belongs to the core ladder or
5 belongs to the growing 41 ladder, both impossible.

The additional original ray of 27 cannot meet any ladder ray: its odd part is
27, divisible by three, while all ladder nodes are ternary units. The original
core ray has odd part 1 and also cannot meet the other growing ladder.
Thus these two ray families remain disjoint FOREVER.

Nevertheless 27 reaches 1 in 70 shortcut steps with maximum state 4616, as
literally replayed in the retained bounded control. In particular kappa_H(27)
for the FULL graph is already +infinity for H>=4616, whereas all finite ray-pin
relaxations remain feasible and their optimal critical energy grows without bound.

There is no paradox. The explicit sparse coloring from Section 3 has

    b(41)=1,  b(62)=b(31)=0,

and fails the omitted actual odd edge T_3(41)=62. It is invariant on S, not on
all of T_3. Its failure identifies a concrete missing edge rather than an
unrealized completion or a probabilistic exception.

**SC-005.** Increasing the depth of these two deterministic inverse ladders
can NEVER make them a complete convergence-certificate language, even for the
ordinary convergent source 27. Arbitrarily expensive separation is strictly
weaker than merger completeness in this entirely physical 3x+1 subgraph.
The new sparse lower certificates remain valid; no full-graph theorem is refuted.

For p=5 a different control has genuinely distinct full components: the literal
cycles 1->3->8->4->2->1 and 13->33->83->208->104->52->26->13. Their ray families
cannot intersect, and the same critical-exponent conclusion holds. This separates
"missing edges of a convergent model" from "actual distinct components."

## 6. SC-006: what remains needed for the full problem

The preceding FC-007 upper repair target is unchanged: for each fixed original N,
the finite values of the FULL kappa_H(N) must be bounded independently of H.
Together with SC-004 or FC-005 that would force finite infeasibility, hence
convergence. No such bound is proved here.

The present results narrow what a useful next advance must accomplish. The
infinite-energy obstruction is already present in a very small, deterministic
part of the inverse geometry, and the critical exponent is exactly understood.
Repeating inverse-phase density or computing ever larger lower capacities does
not supply the missing merger. A successful upper argument must exploit the
additional actual odd edges of the FULL graph, or prove that adding them forces
a finite conflict with the fixed-source pins. The 27 control shows why preserving
a restricted two-ladder boundary language indefinitely would miss that event.

This is not a claim that the upper target has become logically weaker or easy.
The advance is an exact sparse certificate theory and a sharp diagnosis of its
completeness boundary, not a completed resolution.

## 7. Reproducible evidence and limits

`run.py` uses rational phase order and sorted-list insertion. `verify.py` imports
neither it nor any maximum-flow code: it replays every physical word, orders
phases by integer cross-products, counts insertions with a Fenwick rank tree,
and sums the energy by a separate exact rational method. The output uses hex
strings for large integers; no floating-point comparison controls a verdict.

The 47-case corpus covers seven fixed source/map pairs at depths 0,4,16,64,256,1024,
plus five explicit convergence controls. Both normal and optimized runs give
42 sparse lower certificates and five convergence paths. The checker validates
71,369 inverse/anchor steps, 38,406 rational shell terms and 19,300 listed ray
nodes, and rejects 15 malformed/semantic controls per mode. The depth-1024
5x+1 source-13 example has H=2^6463 and certified cost approximately 3.26205904;
its exact rational certificate is retained, not rounded for acceptance.

`check_models.py` compares the circle formula with an independent line dynamic
program on all 2,187 partial assignments to seven odd rays, then on 224 delayed-
activation examples. It compares 18 small sparse certificates with the old full
cut implementation: 15 finite full cuts dominate their sparse lower bounds;
three full graphs already merge. It also checks the 27 permanent-language control,
the 70-step actual convergence, both 5x+1 cycles, and two explicit uniform bands.
This bounded comparison imports generator code and is not labeled the standalone
certificate verifier.

Normal/optimized corpus and checker output are byte-identical. These are
same-author implementation checks, not independent mathematical peer review.
The uniform theorem and the infinite critical-exponent classification depend on
the written proof, not on these finite tests. Full-repository validation, remote
CI and a formal proof build were not run; no complete checkout was available.

### Historical tools versus present claims

The full min-cut duality in FC-003 is classical Ford--Fulkerson (1956), not a new
graph theorem. The present pin-only formula has its elementary proof above.
Irrational rotation and Dirichlet approximation are likewise classical; their
exact ordinary-path use and the scoped sparse classification are the proposed
contribution. No comprehensive priority search or external novelty claim is made.

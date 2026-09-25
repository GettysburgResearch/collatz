# Open-boundary obstruction, anchored cuts, and finite-energy certificates

**Date:** 25 September 2026. **Status:** PROPOSED, not independently reviewed.
**Verdict:** no Collatz proof. A height-uniform, source-anchored repair bound remains OPEN.
**Parent:** `../pass1/PROOF.md`, especially CR-002, CR-003 and CR-007. The parent
manuscript is retained byte-for-byte; its SHA-256 is
`fb8ffc02c89d69127ce82d144cea08b2b36237fd665be3744ab582cd71d26445`.
No claim of external priority is made. Flow/cut duality, coarea and compactness
are classical tools; the proposed contribution is their source-faithful assembly
with the previous ordinary-component geometry and the exact horizon obstruction.

## 0. Summary and conventions

Use the **unabsorbed shortcut map** T(n)=n/2 for even n, T(n)=(3n+1)/2 for odd n.
Let G_H be the undirected graph on the ordinary integers 1,...,H containing
exactly the edges {n,T(n)} for which T(n)<=H. An exterior endpoint is neither
included nor identified with 1. A Boolean coloring of G_H is constant on each
of its connected components, with b(1)=0. Such a coloring need not extend to
an invariant coloring of all positive integers.

For a complete dyadic shell, set

    d_n = b(n+1)-b(n),
    V_k = sum_{2^k <= n < 2^(k+1)} |d_n|.

The finite graph constraints are exactly the available current equations from
CR-002, including their boundary condition. Thus a statement refuted below on
G_H is also refuted as a consequence of *all* the current constraints wholly
contained in the same observation window. There are no omitted internal edges.

This pass establishes:

* a family of independent ordinary exit corridors giving linear-size boundary
  variation at every fixed multiplicative look-ahead, and a power-law obstruction
  up to the observation exponent log_2(3);
* an exact rational min-cut formulation of the **best**, rather than worst,
  separator with one immutable ordinary source pinned;
* finite-energy Liouville rigidity and unconditional divergence of those anchored
  separation costs, allowing +infinity when a literal merger is found;
* a total, uncapped certificate procedure for each fixed source and each prescribed
  energy budget: convergence **or** a certificate that the budget is too small.

The second output of the procedure does NOT certify a counterexample. It can,
and in the executed examples does, occur for a source that actually converges.

## 1. FC-001: independent exit corridors with large visible variation

Choose integers k,r with 1<=r<=k-2, and write

    X = 2^k,  A = 2^(k-r),  H = 4*3^(r-1)*A
      = 2*X*(3/2)^(r-1).

For every integer

    floor(4*A/3)+2 <= t <= 2*A

put n_t=2^r*t-1. There are

    m = 2*A-floor(4*A/3)-1 > (2/3)*A-1

such sources. Every n_t lies in [X,2X), and its first r shortcut steps have the
literal formula

    T^j(n_t) = 3^j*2^(r-j)*t-1,    0<=j<=r.

For j<r these values are odd. They increase with j, because adding one to a
state multiplies it by 3/2. The last value inside the window is

    e_t = T^(r-1)(n_t) = 2*3^(r-1)*t-1 <= H-1.

The next state is 3^r*t-1>H by the lower bound on t. Thus e_t is the **first
exit vertex**, not merely a high iterate reached after a possibly earlier exit.
The e_t are distinct.

A finite graph of a partial function has at most one terminal exit vertex in
each connected component that contains an exit. Proof: following its unique
outgoing arrows assigns a common terminal exit or a directed cycle to every
vertex; that terminal object is unchanged across each retained edge. A component
cannot contain two exits or both an exit and a cycle. The core component contains
the closed cycle 1<->2. Consequently the n_t belong to m distinct components of
G_H, all different from the core.

**FC-001.** Every one of the 2^m assignments of Boolean values to these m sources
extends to a coloring of G_H with b(1)=0. In particular, assigning alternating
colors as t increases gives

    V_k >= m-1 > (2/3)*2^(k-r)-2.

To extend an assignment, color each selected entire component accordingly and
color every other component zero. This is an admissible choice, not a boundary
condition imposed on all possible colorings. Between each successive pair of
oppositely colored seeds there must be at least one change; the intervening
integer intervals are disjoint. This proves the variation bound. QED.

For fixed r, H/(2X) is constant while m grows linearly in X. Hence no bound such
as V_k=O(k), much less o(k), holds for *all* colorings satisfying the constraints
in a fixed multiplicative neighborhood of the observed shell.

### Restriction to a smaller observation window

If 2X<=B<=H, restriction to G_B preserves all these seed colors and their
independence. A path in G_B would also be a path in G_H. Therefore the same
variation witness works at any such B. No exterior trajectory needs to be
completed to use this finite counterexample.

## 2. FC-002: a polynomial-look-ahead obstruction

Let alpha=log_2(3), beta=alpha-1=log_2(3/2). For any fixed

    1 < p < alpha,

take the observation window B_k=floor(X^p), where X=2^k. For sufficiently large
k it contains the whole shell. Choose the smallest r>=1 such that

    H_r = 2X*(3/2)^(r-1) >= B_k.

Then r=((p-1)/beta)*k+O(1), so r<=k-2 eventually. FC-001 and restriction give a
positive constant c_p and admissible finite colorings with

    V_k >= c_p * X^((alpha-p)/(alpha-1)).

The exponent is strictly positive. More generally, when B>=2X and the chosen
r is at most k-2, putting R=B/(2X) gives the explicit conservative estimate

    V_k > X/(6*R^(1/beta)) - 2.

Indeed r=1+ceil(log_(3/2) R), so 2^r<=4*R^(1/beta), and use FC-001.
For p=3/2 the power is approximately 0.145244. This approximation is explanatory;
the theorem and certificate construction use exact integer inequalities.

**Scope.** This is a no-go theorem for all-coloring regularity derived from those
finite windows. It does not refute a global regularity theorem. Its distinguished
seeds grow with k: it does not refute a bound for an optimized separator with
one fixed original source. Nor does it show that p>=alpha suffices. The exponent
arises from the exact all-odd expansion 2^r*t-1 -> 3^r*t-1, not from a random
parity model.

This explains why a finite experiment must record its observation height and
why arbitrary unresolved boundary choices cannot be treated as a regular global
observable. The current equations themselves have not supplied smoothing.

## 3. FC-003: a lossless variational problem, not arbitrary boundary colors

Fix one ordinary N>1 throughout all height changes. For H>=max(N,2), define

    E_H(f) = sum_{n=1}^{H-1} |f(n+1)-f(n)|/(1+floor(log_2 n))^2.

For H=2^K this is exactly sum_{k=0}^{K-1} V_k(f)/(k+1)^2. Define

    kappa_H(N) = min E_H(b)

among Boolean colorings of G_H with b(1)=0 and b(N)=1, and set kappa_H(N)=+infinity
when there are none. Pins become infeasible precisely when N and 1 are connected
in G_H. This finite statement does not assume the global conjecture.

The objective is a weighted **L1** variation, not a squared-gradient energy.
Replacing it by an L2 relaxation would require a different theorem.

### Exact quotient graph

Contract the G_H components. For each adjacent integer pair n,n+1 in different
components, add an undirected edge of capacity

    w_n = 1/(1+floor(log_2 n))^2

between their component vertices; parallel edge capacities are added. Loops have
zero variation and are discarded. The vertices carrying N and 1 are the terminals.
A Boolean separator is exactly a cut separating them and E_H is exactly its cut
capacity. This is an exact reduction, not an estimate or a sampled coloring.

### Coarea makes the real relaxation exact

Allow 0<=f<=1, still constant on G_H components and with f(1)=0,f(N)=1.
For t in (0,1), let b_t(n)=1_{f(n)>t}. Every b_t is an admissible Boolean separator,
and

    |f(n+1)-f(n)| = integral_0^1 |b_t(n+1)-b_t(n)| dt.

Finite summation gives E_H(f)=integral_0^1 E_H(b_t)dt >= kappa_H(N). Conversely
Boolean functions belong to the real feasible set. Hence both minima coincide.
No assumption that low-energy real values are close to integers is necessary.

### Dual certificates and an exact anchored inequality

Scale all capacities by the LCM of the denominators. An antisymmetric flow F on
the quotient edges, bounded by these capacities, with divergence Q at the N
terminal, -Q at the 1 terminal and zero elsewhere, satisfies

    Q*(f(N)-f(1)) = sum_edges F_ab*(f(a)-f(b)).

Absolute values give Q*|f(N)-f(1)| <= E_H(f), in unscaled units. A Boolean cut
with capacity Q certifies optimality. Thus

    kappa_H(N)*|f(N)-f(1)| <= E_H(f)

for every real G_H-invariant f, with equality attainable in the Boolean pinned
problem when the pins are feasible. This is an anchored trace inequality with
an exactly computable best constant.

Rational maximum-flow/minimum-cut equality can also be proved here by repeated
integer augmentations. Every augmentation raises integral flow, bounded by the
finite source capacity. At termination, vertices reachable through residual
edges give a cut saturated by the flow. Therefore an optimal pair is computable
with no numerical tolerance. This is classical Ford-Fulkerson duality; it is
not claimed as a new general graph theorem.

## 4. FC-004: finite-energy invariant observables are constant

For a globally invariant f, the dyadic current law gives

    V_(k+1)(f) >= V_k(f)

by the triangle inequality. This holds for real f, not only Boolean f. Define

    E_infinity(f) = sum_{k>=0} V_k(f)/(k+1)^2.

If this is finite, monotonicity implies V_k(f)/k -> 0: for k>=1,

    sum_{j=k}^{2k-1} V_j(f)/(j+1)^2 >= V_k(f)/(4k),

and the left side tends to zero as a tail of a convergent nonnegative series.
But CR-007, applied to any two fixed sources with different f-values, gives
limsup V_k(f)/k >= |f(N)-f(M)|/32. Therefore f is constant.

**FC-004.** Every globally invariant real function of finite E_infinity is
constant. In particular every nonconstant invariant Boolean separator has
infinite E_infinity.

This is a regularity-class Liouville result, not a proof that all invariant
functions have finite energy. It follows from the previous inverse-ladder
lower bound; it does not provide the missing upper bound.

A useful dyadic-only control is b(n)=1 when the normalized binary mantissa of n
is in [5/4,3/2), and zero otherwise. It satisfies b(2n)=b(n), b(1)=0, has V_k=2
for all k>=2 and finite E_infinity, but b(3)=0 and b(T(3))=b(5)=1. Thus dropping
the odd arithmetic equation really does invalidate FC-004.

## 5. FC-005: anchored capacities necessarily escape

For H' >= H >= N, restriction of a feasible separator on G_H' gives one on G_H
and cannot increase its energy. Thus kappa_H'(N)>=kappa_H(N), including the
infinite convention. Once the pins merge, they remain merged at every larger
height.

**FC-005.** For every fixed ordinary N>1,

    lim_{H->infinity} kappa_H(N) = +infinity.

The conclusion allows either eventual infeasibility or arbitrarily large finite
separation costs. These alternatives must not be conflated.

*Proof.* If the conclusion fails, there are unbounded heights H_j and pinned
colorings b_j with E_Hj(b_j)<=C for one finite C. Use diagonal extraction in the
countable product {0,1}^{N>0}. The resulting ordinary-integer coloring b has
b(1)=0,b(N)=1. For any fixed edge {n,T(n)}, both endpoints belong to all sufficiently
large windows and their limiting values agree. For each fixed initial interval
1..L, its finite energy sum is at most C by eventual stabilization of those finitely
many bits. Taking L->infinity yields E_infinity(b)<=C. This contradicts FC-004.
QED.

**Why this compactness use is legitimate.** The integer N is fixed in every
window. The extracted object is a coloring of the same countable set of ordinary
positive integers, not a 2-adic source chosen anew at successive depths. We do
not obtain a fixed original integer from unbounded changing integers. The
uniform energy bound is retained on every finite interval before taking the
infinite sum. No exterior root is pre-colored as convergent.

## 6. FC-006: an unconditional total certificate compiler

Input one fixed N>=1 and a finite rational budget M>=0. For dyadic H growing
from H>=N, compute the exact finite quotient and an optimal cut-flow pair.

- If N is in the core component, return an actual finite shortcut trajectory
  from N to 1 within 1..H.
- Otherwise, if kappa_H(N)>M, return the finite flow/cut certificate, proving
  that no invariant Boolean separator with these pins can have total energy <=M.
- Otherwise increase H and repeat.

**FC-006.** The uncapped procedure terminates on every such input.

For N=1 it returns the trivial path. For N>1, FC-005 ensures that some finite
height meets one of the two return conditions. Finite max-flow terminates at
each stage. If a core component is found, following T from N stays within its
component: a component of a partial functional graph cannot contain both an
exit and the core cycle. It therefore reaches 1 after finitely many steps;
literal replay supplies the certificate. QED.

This is a total certificate compiler for a **disjunction**, not a convergence
selector. A high-energy certificate rules out a specified proposed regularity
budget, not the possibility that N converges at a later height. It also applies
to the real relaxation by FC-003. No running-time bound in N or M is established.

The delivered `certify_budget.py` has an explicit default height cap of 65536
and honestly returns UNRESOLVED_AT_RESOURCE_CAP when it is reached. Passing
`--max-height 0` requests the uncapped mathematical procedure. Its termination
proof is FC-006, not a finite testing extrapolation.

## 7. FC-007: the precise missing repair theorem

A sufficient closing statement is:

> For every fixed ordinary N>1, there is a finite C_N such that, at every
> sufficiently large H where the pins are feasible, there exists a coloring
> of G_H with b(1)=0,b(N)=1 and E_H(b)<=C_N.

Equivalently, all *finite* values of kappa_H(N) are uniformly bounded in H
(the finitely many smaller heights can be absorbed into C_N). No algorithm or
computable expression for C_N is needed for the logical implication, though an
explicit bound would feed directly into FC-006.

If N never converges, its pins are feasible at every height; FC-007's proposed
bound would contradict FC-005. Therefore this repair theorem would prove Collatz.
It is enough to produce the bound at an unbounded sequence of heights, because
kappa_H is nondecreasing.

**OPEN:** no such source-uniform-in-height repair bound is proved in this pass.
It is not inferred from the empirical cut profiles. This formulation is not
logically known to be easier than Collatz: its advantage is that it asks for
**one optimized separator**, allows unrelated exterior colors to be changed,
keeps the source fixed, and has exact finite lower certificates that can falsify
a candidate upper bound. The arbitrary-coloring estimates refuted by FC-001/002
are stronger and are no longer the preferred finite target.

A plausible next theorem would construct cut repairs as H changes, with a
summable energy bill depending on N but not H, using the actual 3-term current
law. Whether such repairs exist before a merger is the unsolved substantive
step. Pointwise local smoothing or setting every exterior color to zero is not
that theorem.

## 8. Controls: why the same framework is not a 5x+1 proof

For T_5(n)=n/2 or (5n+1)/2, respectively, the positive cycles through 1 and 13
are disjoint:

    1 -> 3 -> 8 -> 4 -> 2 -> 1,
    13 -> 33 -> 83 -> 208 -> 104 -> 52 -> 26 -> 13.

The cycle through 17 is also disjoint (see the preserved pass-1 literal replay).
Consequently the pins 1/13 and 1/17 remain feasible in every sufficiently large
window, and their basins give globally invariant Boolean separators.

For completeness, the finite-energy Liouville property and capacity-escape
theorem also hold for T_5. For any y>=2 with 5 not dividing y, let k_0 in {0,1,2,3}
solve 2^k0*y=1 mod 5. Choose k in {k_0+4,k_0+8} so z=(2^k*y-1)/5 is not divisible
by five. At least one works because multiplying 1 mod 25 by 16 gives 16 mod 25,
not 1. The positive odd predecessor has T_5^k(z)=y and

    3y <= z < 512y.

Every source N is linked to an initial unit y_0>=2 with y_0<=3N: take N itself
when eligible, take 3 for N=1, and for a multiple of five first halve to its odd
part u then use (5u+1)/2. The growing ladder has logarithmic phase

    log_2 y_j = integer - j*log_2 5 + constant + e_j,
    |e_infinity-e_j| <= 3/(16*y_j) <= (3/32)*3^(-j).

The same continued-fraction grid proof as CR-007 gives limsup V_k/k>=1/72 for
a nonconstant Boolean invariant: q ladder phases form a 5/q-net after O(log q)
steps and fit in a shell of height index 9q+O(log q). Thus FC-004/005/006 have
5x+1 analogues. For the two distinct cycles, the budget procedure always
ultimately returns an energy obstruction, not convergence.

Therefore the missing FC-007 repair bound must distinguish the actual 3x+1
arithmetic from 5x+1. Capacity escape, compactness, inverse-phase density and
classical cut duality alone do not do so.

## 9. Executed evidence and precise limits

Both normal and optimized standard-library experiment runs produced identical
`results.json`, SHA-256

    8c8f2c92f6f31b755de75cbe1e590273549ba888e5017ce6d820ff74a7a35369.

Six corridor windows, from H=512 through H=2239488, were constructed with all
internal T-edges retained. Every resulting full coloring satisfied all retained
T-edges, all available D2/D3 equations and the complete-shell birth identities.
The largest window has 170 independently assignable selected seeds; its
alternating coloring has V_16=456 against the proved lower bound 169. This is a
finite adversarial regularity test, not 170 nonconvergent components.

Forty-eight source-pinned cut problems were computed: 45 finite separators and
3 finite core connections. The anchored sequences keep N=27,97,871 for T_3 and
N=13,17 for T_5 fixed across their respective windows. A separate exhaustive
check compared max-flow optima with 76902 Boolean assignments in 196 small cut
problems. There were also 122 exact rational coarea identities.

The checker `verify_certificates.py` imports neither the generator nor its
union-find or max-flow implementation. It rebuilds components by graph traversal,
checks all 48 cut cases, including 7911 nonzero flow edges, capacity bounds,
divergence at every quotient vertex, matching cut values, Boolean pins and
coloring hashes. It replays 3741 corridor steps and all four smaller corridor
colorings, and rejects nine semantic mutations. For the two largest corridors
it checks the explicit distinct-exit construction but does NOT independently
reconstruct the entire reported coloring hash. That full reconstruction was
performed by the experiment, in normal and optimized modes. Same-author
implementation diversity is not independent mathematical peer review.

Five budget-compiler controls were executed and retained:

| Map | Source | Budget | Result |
|---|---:|---:|---|
| 3x+1 | 27 | 1 | certified energy obstruction at H=256 |
| 3x+1 | 27 | 10 | literal convergence at H=8192 |
| 5x+1 | 13 | 2 | certified energy obstruction at H=16384 |
| 3x+1 | 871 | 10 | explicitly unresolved at resource cap H=4096 |
| 3x+1 | 1 | 0 | trivial convergence path |

For source 27, kappa_4096(27) is approximately 9.34265 before the pins merge at
the next tested dyadic height. For source 13 under 5x+1, kappa_4096(13) is about
1.62520 and the pins never globally merge. Thus faster observed capacity growth
is not evidence of divergence. Decimal values here summarize exact rational
certificates; no floating-point comparison controls any verdict.

No full repository checkout was available, so repository-wide validation and
remote CI were not executed. No independent review or formal proof build was
performed. All scientific claims retain PROPOSED status. Publication attempts
and local commit receipts are kept separately in `reports/`.

## References and current-source scope

- Parent manuscript CR-001--007, retained in `../pass1/PROOF.md`.
- Repository main was read at `ab7a62cbbb83860ea9436c5d3cf6cf7ce501066a`, including
  AGENTS, README, research map and integrated errata. This is not a new audit of
  all active branches. The current pass does not depend on their pending claims.
- L. R. Ford Jr. and D. R. Fulkerson, *Maximal Flow Through a Network*, Canadian
  Journal of Mathematics 8 (1956), 399--404, DOI 10.4153/CJM-1956-045-5.
  Primary publication record:
  `https://www.cambridge.org/core/journals/canadian-journal-of-mathematics/article/maximal-flow-through-a-network/5D6E55D3B06C4F7B1043BC1D82D40764`.
- Functional and graph reformulations of Collatz have prior literature. The
  parent lists Monks et al. and Bell--Lagarias. This pass's limited literature
  search does not establish novelty of the capacity formulation or its lemmas.

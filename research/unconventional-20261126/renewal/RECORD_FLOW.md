# Atomic record occupation without a record-gap bound

**Status — PROPOSED.** Consider one injective positive odd trajectory
and its strict coefficient record times $k_l$ and values $q_l$ as in
[the definitions](README.md). Put $m_l=k_{l+1}-k_l$ and let $w_l$
be the actual first-ladder block on that interval. Record occupancy is
normalized by the **elapsed odd time** $n$. The total mass can vanish
when record gaps grow. Write $\mathbb T=\mathbb R/\mathbb Z$.

**Theorem F.** At each record put
$Q_l=(q_l\text{ in }\mathbb Z_2^\times,q_l\text{ in }\mathbb Z_3,
\log_2q_l\bmod1)$. Every weak subsequential limit of

$$
 \Lambda_n=\frac1n\sum_{k_{l+1}\le n}
                      \delta_{(Q_l,w_l,Q_{l+1})}                    \tag{F1}
$$

is a finite positive measure of mass at most one with equal source
and target marginals. All such sequences have convergent subsequences
on the countable, discrete alphabet of complete finite ladder words.
In the common marginal take the part supported on the atoms of its
ternary projection. This part is a finite or countable sum of measures
of the following form, each multiplied by a nonnegative weight:

1. Take a finite periodic orbit of the genuine signed rational odd
   map, equipped with its consecutive strictly rising coefficient
   record phases. These phases are negative rationals of odd
   numerator and odd denominator prime to three.
2. Give equal mass to its distinct record phases $u$. Above each
   phase the pair of local coordinates equals $(u,u)$, and the
   real-log coordinate has normalized Haar measure on $\mathbb T$.

In particular a nonperiodic ternary point of positive limiting
record occupancy, or a periodic ternary atom with a different dyadic
coordinate of positive conditional mass, is impossible. The statement
allows a nonatomic ternary part.

## Tightness and the limiting record edges

Let $\mathcal L$ be all complete first-ladder words. The subset
of words of length at most $J$ is finite because the native clocks
there equal $\lfloor m\log_2 3\rfloor$. The mass with $m>J$ is
at most $1/J$ since $\sum_{k_{l+1}\le n}m_l\le n$. Together with
compactness of the vertex coordinates, this proves tightness (or
use diagonal subsequences on finite alphabets and this tail bound).
The difference of the two marginals tested against a bounded
function is a boundary term bounded by $2\|f\|_\infty/n$.

At every edge with a fixed label $w$ of odd length $m$ and native
clock $s$, the limit is supported on triples
$((x,z,t),w,(x',z',t'))$ satisfying

$$
 2^s x'=3^m x+C_w,\qquad z'=F_w(z),\qquad t'=t+m\alpha\bmod1,
 \quad\alpha=\log_2 3.                                             \tag{F2}
$$

The two local identities pass by continuity. For the circle identity,
$q_{l+1}=(3^m/2^s)(q_l+h_w)$, and $q_l\to\infty$ on the fixed
injective ray. With $w$ fixed, the correction $\log_2(1+h_w/q_l)$
therefore vanishes. Every fixed finite initial set has zero limiting
weight, proving (F2). Restriction to a fixed label is valid because
that label is clopen.

## Recurrence on the countable set of ternary atoms

Let $P$ be the countable set of atoms of the common ternary marginal.
An edge whose source lies in $P$ has target in
$\bigcup_{w}F_w(P)$, a countable set. Conversely an edge with target
in $P$ has source in $\bigcup_w F_w^{-1}(P)$, also countable since
each map is injective. A countable set outside $P$ has marginal mass
zero. Thus an edge starts in $P$ exactly when it ends in $P$, up to
null sets. The restricted edge measure remains stationary, including
its other coordinates.

Draw the countable directed graph of positive-mass transitions
$u\overset{w}{\longrightarrow}v$ between these ternary atoms.
Every such edge belongs to a finite directed closed walk. Indeed,
the set of vertices reachable from $v$ is closed under every
positive-mass outgoing edge. Stationarity forbids any incoming
positive mass from outside that set, so $u$ is reachable from $v$.
A closed walk has expanding real affine composition
$z\mapsto(3^m z+C)/2^s$. Its only fixed point is
$-C/(3^m-2^s)$, a negative rational with odd numerator and odd
denominator prime to three. For the numerator, $C$ is odd, and
$C\bmod3$ is a power of two. The same conclusion holds at every
vertex by rotating the closed walk.

A sequence of proposed gaps taking one such odd rational to another
must consist entirely of genuine signed odd gaps. A gap exceeding
the genuine one gives negative dyadic valuation. A smaller gap
gives positive valuation and any further positive gap makes it
negative. Thereafter every gap strictly decreases that valuation.
The exceptional equation $3z+1=0$ cannot occur on these genuine
paths: starting with a denominator prime to three preserves that
property. Thus the complete first-ladder word leaving each atom,
if present, is unique, since the genuine future and its *first*
strict coefficient increase are deterministic. The graph on $P$
is a union of directed simple cycles. Its stationary masses are
constant around each of them.

Fix one phase $u$ on such a cycle and follow $p$ odd gaps of total
clock $s$ for a complete lap. Restrict the common vertex measure
to this phase and normalize. Pushing it around the cycle reproduces
itself, since each intervening target is determined by (F2) and
each cycle vertex has exactly one positive-mass incoming edge.
For its dyadic coordinate, (F2) gives
$2^s(x'-u)=3^p(x-u)$ on one lap. Iteration gives
$x-u\in2^{js}\mathbb Z_2$ almost surely for every $j$ because the
successive dyadic targets remain integral. Hence $x=u$ almost
surely. On the real circle a lap acts by $t\mapsto t+p\alpha$.
The angle is irrational. Every nonzero Fourier coefficient of an
invariant finite measure must vanish, and trigonometric polynomials
are dense, so the normalized circle marginal is Haar measure.
This proves Theorem F.

## Consequences for one supplied ray

Let $K_3$ be the ternary record cluster set and $K_{2,3}$ the joint
local cluster set. If $K_3$ is countable and $K_{2,3}$ contains no
diagonal pair $(u,u)$ of negative signed periodic record phases,
then the number of records through odd time $n$ is $o(n)$. Indeed
every limiting marginal is supported on the cluster set. A nonzero
measure on countable $K_3$ has an atom, contradicting Theorem F.
Every strict record increases $\log_2 M$ by at most $\alpha-1$.
Thus $\log x_n/n\to0$ by the finite ordinary distortion bound and
$x_n\to\infty$. In particular an exponentially growing subsequence
would force a diagonal periodic pair in this countable-cluster case.

For any ternary point $z$ outside the negative signed periodic
record phases,

$$
 \lim_{b\to\infty}\limsup_{n\to\infty}
  \frac1n\#\{l:k_l\le n,\ q_l\equiv z\bmod3^b\}=0.                \tag{F3}
$$

If the nested clopen neighborhoods retained some mass, a diagonal
choice of horizons and compactness in (F1) would yield a limit
assigning at least that mass to every fixed neighborhood, hence
to their intersection $\{z\}$. Omitting the final uncompleted
record from (F1) changes counts by at most one. The same proof
excludes every off-diagonal atom of the joint local marginal.
The [integer spacing bounds](BRIDGE.md) quantify (F3) at algebraic
points without taking a weak limit.

At horizons where the common mass vanishes, stationarity alone
places no condition on a record-count-normalized limit. More
generally Theorem F holds for any sequence of **record-count**
normalized complete-edge samples if their word marginals are tight
and the samples are consecutive intervals whose lengths in records
tend to infinity. The two proofs of tightness are logically distinct.
The compact symbolic constructions in [the long-gap
control](ESCAPE_OF_MASS.md) illustrate escape of mass at odd-time
normalization.

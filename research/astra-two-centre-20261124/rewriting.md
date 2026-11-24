# A peak barrier in the complete ordinary component graph

**Computer-assisted finite certificate and universal arithmetic lift. Overall descent remains OPEN.**
Let $n$ be the ordinary shortcut Collatz coordinate. Put

\[
        P=7342984060644141028475928576.
\]

For every integer $t\ge0$, put $n_t=9663+Pt$. Every finite undirected path of literal Collatz edges from $n_t$ to any positive integer less than $n_t$ contains an ordinary integer at least $1024n_t$. Both directions of every legal edge are allowed, with arbitrarily many moves. The assertion applies to all paths simultaneously. For example, a rewriting completion in which every descent below a source is realized entirely inside its open factor-1024 ceiling cannot be total. The certificate requires no condition on the eventual orbit of these starts.

## Proof and replay

Use shifted coordinates $a=n+1$, and represent the affine family $x+tPs$ by the pair $(x,s)$, with $x$ integral and $s$ rational. Begin at $(9664,1)$. At a pair, the complete neighbor list at $t=0$ is

| Guard on $x$ | Neighbor |
|---|---|
| always | $(2x-1,2s)$ |
| $x$ odd | $((x+1)/2,s/2)$ |
| $x$ even | $(3x/2,3s/2)$ |
| $3\mid x$ | $(2x/3,2s/3)$ |

Indeed the first two are the two directions of an ordinary even shortcut edge and the last two are the two directions of an ordinary odd shortcut edge. Enumerate all reachable pairs while stopping each branch the first time its slope is at least 1024. The exact rational computation in [rewriting.py](rewriting.py) exhausts its queue after visiting 3,402 distinct interior pairs and finding 1,137 distinct boundary pairs. It checks the following inequalities and divisibilities:

* Every interior pair has $x\ge9664$, $s\ge1$ and $Ps\in6\mathbb Z$.
* Every boundary pair has $x-1\ge1024\cdot9663$ and $s\ge1024$.

The program computes $P$ as the least common multiple of six times the reduced denominators of the interior slopes. Consequently all interior guards at each $t\ge0$ agree with those at zero. Substituting $x+tPs$ into each literal neighbor formula gives exactly the value of its listed symbolic neighbor at the same $t$. Induct along any path until its first boundary pair. While it stays in the interior, its ordinary value $x-1+tPs$ is at least $9663+tP=n_t$. At the boundary its ordinary value is at least $1024(9663+tP)$. Thus a path to a smaller positive state must hit the claimed peak. This induction does not require distinct symbolic pairs to project to distinct integers.

Run `python -B research/astra-two-centre-20261124/rewriting.py` from the repository root. The certificate is an exhaustive finite computation with rational arithmetic, followed by the written induction above.

## Boundary of the result

This is an obstruction to a bounded-peak completion, obtained from the full graph rather than a chosen steering controller. It does not establish a barrier at every constant, nor does it show even one start with no smaller component representative. The first missing inference for a full descent proof is that allowing a sufficiently large, source-dependent peak eventually creates an exit below every fixed original source. Raising the finite ceiling or varying the positive witness does not establish that inference.

## A height-dependent positive Bellman candidate

**Universal selection OPEN.** The mixed-input obstruction in [integer.md](integer.md) rules out finite-residue weights with any fixed finite repertoire. The following full-graph rank pays an edge toll that tends to zero as ordinary binary length tends to infinity. It does not need to know whether its source reaches 1 in order to define or compute its value.

Fix a positive rational $K$. Write $b(x)$ for the ordinary positive integer's bit length. Give an undirected shortcut edge $x,y$ the symmetric toll $c(x,y)=1/\max(b(x),b(y))$. Let $d_c$ be the shortest-path toll within a component. Put $f_K(x)=K(b(x)-1)$ and
$$
 V_K(x)=\min_{y\sim x}\bigl(f_K(y)+d_c(x,y)\bigr),
$$
where $y\sim x$ means membership in the same full component, including $y=x$. The exact recurrence is
$$
 V_K(x)=\min\left(f_K(x),\ \min_{q\text{ neighbor of }x}\{c(x,q)+V_K(q)\}\right).
$$
For a path of $j$ edges out of $x$, bit length at the $i$-th edge is at most $b(x)+i$. Hence the toll is at least $\sum_{i=1}^j 1/(b(x)+i)$, which tends to infinity. The graph is locally finite, so every finite-radius toll ball is finite, all minima are attained, and searching up to cost $f_K(x)$ computes the rank without an orbit-termination assumption. Its sublevel sets are finite for $K>0$: the possible minimizing targets have bounded bit length, and their bounded-radius balls are finite. Whenever $V_K(x)<f_K(x)$, any minimizing first edge gives a strictly smaller rank. A proof of this inequality at every $x>1$ would force termination.

There is a structural limit on how the extra edges could help. The shortcut component of 1 is an undirected tree after identifying the duplicate edge $1\leftrightarrow2$. Every vertex in that component flows to the cycle $1,2$; each other vertex has exactly one forward parent and reverse edges to its children. A strict one-edge selector on this component that always terminates at 1 must move toward that parent, since leaving it along a child edge would require revisiting it to reach 1. For a selector terminating in a finite set, the same applies outside the finite subtree joining the reachable terminal vertices to 1. This argument concerns single-edge global ranks; it imposes no direction restriction on a merger certificate made from a whole finite path.

**Exact check.** For every $2\le x\le10^6$, the cumulative toll $D(x)$ along its shortcut orbit to 1 was strictly less than $3(b(x)-1)$. The largest observed ratio $D(x)/(b(x)-1)$ was $237739/102960$ at $x=27$. The first failures of strict domination with $K=1,2$ were respectively 3 and 27. The computation in [rewriting.py](rewriting.py) follows each orbit to a previously computed cost, starting only at 1. All endpoint bit lengths encountered were at most 35. It represents the tolls exactly as integer multiples of the reciprocal of the least common multiple of 1 through 64.

In fact $V_3(x)=D(x)$ throughout this tested interval, including $x=1$. Taking $y=1$ supplies the upper bound. If $y\le10^6$, tree distance and the verified inequality $D(y)\le f_3(y)$ give $D(x)\le d_c(x,y)+f_3(y)$. If $y>10^6$, then $f_3(y)\ge f_3(x)\ge D(x)$. Thus allowing every competitor throughout the infinite component does not change the checked rank in this interval. At a tested $x>1$, the first forward edge reduces $V_3$ even when $T(x)$ exceeds the test cutoff, because $V_3(T(x))\le D(T(x))<D(x)$.

**First unsupported inference.** An inequality $\sum_{i<j}c(T^i x,T^{i+1}x)<3(b(x)-1)$ for every ordinary source $x>1$ and every prefix ending at or before its first visit to 1 would suffice. A never-returning trajectory has divergent total toll by the harmonic bound, so convergence would follow without assuming it in that inequality. The finite computation supplies no all-source bound on that exact sum. This candidate allows state-dependent edge costs and search radii, but its required bound still concerns the actual orbit of each input.

The separate [rewriting.lean](rewriting.lean) verifies the peak certificate's finite tree with kernel `decide` and proves abstract neighbor coverage (`local_safety`) and physical edge lifting (`lift`). The final path induction for the progression and the height-dependent rank arguments are written proofs.

## One threefold band pays bounded harmonic cost per injective visit

Fix an integer $X\ge1$ and $I=[X,3X)$. An integer whose shortcut step stays in $I$ is odd in $[X,2X)$ or even in $[2X,3X)$. Conversely every integer of these parities in the indicated parts stays in $I$ for the next step. The lower odd states map increasingly into $[3X/2,3X)$ and the upper even states map increasingly into $[X,3X/2)$. Thus the map on these admissible states is an injection preserving *cyclic* order on the circle obtained by identifying the ends of $I$. It extends to an orientation-preserving circle homeomorphism by interpolating increasingly on the gaps, including across the seam.

Set $h=\lceil\log_2(2X)\rceil$. The parity word of $h$ successive steps staying in $I$ is the itinerary of the initial point under this homeomorphism for the partition into the two half-open intervals with boundaries $X,2X$. The preimages of those two boundaries at clocks $0$ through $h-1$ give at most $2h$ cutpoints. They partition the circle into at most $2h$ half-open arcs with constant itinerary. If two integer starts have the same $h$ parities then their difference is divisible by $2^h$: the linear part of the common affine word is $3^p/2^h$, and both endpoints are integers. Since $2^h\ge2X$, no two distinct starts in $I$ can share this word. Consequently **in the entire band**, at most $2h$ distinct integer states can stay there for the next $h$ steps. An injective visit of $L$ successive edges inside the band has $L-h+1$ such starting states if $L\ge h$, whence $L\le3h-1$. Its harmonic toll is bounded by $(3h-1)/b(X)\le4$: for $X>1$, $h\le b(X)+1$ and $b(X)\ge2$, and $X=1$ is direct.

More generally, over R separate injective visits to the same band, let L be the total number of edges wholly inside those visits. For any integer h>=1, the same at-most-2h word count and parity congruence give at most 2h ceil(2X/2^h) distinct starts that stay for h further steps. Removing at most h initial or terminal edges per visit therefore gives L <= R h + 2h ceil(2X/2^h). At h=ceil(log2(2X)), all cost beyond the short entrance/exit portions is bounded per band. The remaining term still depends on R, which is not controlled by the original source.

Constant visit length would be false. For any prescribed length $s$, choose odd or even steps so that the successive homogeneous products $u$, initially 1, remain in $[1,3)$: use the odd step when $u<2$ and the even step otherwise. For this fixed word, all sufficiently large positive integers in its parity class follow it and stay in $[n,3n)$, since each of the finitely many additive errors is nonnegative and all the products are strictly below 3. The number of even steps is $s(1-\log_3 2)+O(1)$ by the bounded final log product. Every even step crosses a dyadic boundary, with at most two different boundaries in this band. Thus a single boundary can be crossed arbitrarily often before forward descent below the initial value. The source varies with $s$. Such sources can even be chosen in the 1 component: if the word's affine map is $(3^p n+A)/2^s$, choose a large endpoint $y=(2^k-1)/3$ having $2^s y\equiv A\pmod{3^p}$. This is possible because 2 generates the units modulo $3^{p+1}$ (its order is $2\cdot3^p$, by factoring powers of 4 or by the binomial theorem). Then $n=(2^s y-A)/3^p$ belongs to the required parity class: its residue modulo $2^s$ is the unique one given by the word. The odd $y$ goes to a power of two. These examples do not give an unrestricted smaller-source obstruction.

## Complete exclusion of positive cycles within a factor of three

Suppose a primitive positive integer shortcut cycle stays in $[m,3m)$, where $m$ is its minimum. Sort its $L$ points as $x_0<\cdots<x_{L-1}$. At least one is even and one is odd, since all-even words shrink and all-odd positive words grow. Write $p$ for the number of odd points and $k=L-p$. The first $p$ points are odd and the remaining $k$ are even by the band guard. Their image ordering proved above makes $T$ the rotation $i\mapsto i+k\pmod L$ on the ordered points. Hence $\gcd(k,L)=1$ by primitivity.

Extend the ordered representatives by $x_{i+L}=3x_i$ for nonnegative $i$. For $0\le i<L$, $x_{i+k}$ equals $(3x_i+1)/2$ if $i<p$ and $3x_i/2$ otherwise. Set $g_i=x_{i+1}-x_i$, so $g_{i+L}=3g_i$. The last gap $g_{L-1}=3x_0-x_{L-1}$ is an auxiliary positive integer. The gaps are not assumed to belong to the original component. Under the same index rotation, ordinary gap transitions except at $i=p-1,L-1$ are homogeneous: their factor is $3/2$ within the odd block and $1/2$ within the even block after reducing the destination index mod $L$. The two exceptional transitions are consecutive. With $A=g_{p-1}$ and $B=g_{L-1}$, they give
$$
 B=(3A-1)/2,\qquad g_{k-1}=(B+1)/2=(3A+1)/4.
$$
The remaining $L-2$ transitions on this full gap tour have product $3^{p-1}/2^{L-2}$. Thus $(2^L-3^p)A=3^{p-1}$. The factor $2^L-3^p$ is positive and coprime to 3, so equals 1. For $L\ge3$ this would give $3^p\equiv7\pmod8$, impossible. For $L=2$ one has $p=1$ and the odd minimum returns after its odd then even step, so $m=(3m+1)/4=1$. Thus the sole such cycle is $1,2$. Equality $\max=3m$ is also impossible in a cycle: a multiple of 3 can have only its double as a predecessor, which recursively precludes a finite positive cycle.

## Attempt to glue the bands

The single-visit bound leaves the number of visits uncontrolled even on one fixed orbit. The phase ordering need not survive projection across multiple bands. On the ordinary forward orbit $46,23,35,53,80,40,20,10,5,8,4,2,1$, normalize vertices by powers of 3 into $[5,15)$. The points $5,46/9,10$ are in increasing order. Their one-step images after normalization are $8,23/3,5$, in reverse cyclic order. Thus a single rotation of the sorted cross-band points cannot supply the same two exceptional gap equations. An unbounded trajectory can also enter successively higher bands. No charge to the original finite input has been obtained for those entrances or for all returns to previously visited bands. This is the remaining gap in using the proved local toll bound to deduce the universal weighted-duration inequality.

**Prior work.** The sorted rotation makes the temporal cycle word mechanical (a cyclic Christoffel word). Kevin Knight already excludes nontrivial high cycles in *Collatz high cycles do not exist*, Discrete Mathematics 349 (2026), 114812 ([publisher](https://www.sciencedirect.com/science/article/pii/S0012365X25004200)). The argument above gives a direct geometric gap proof in the stated band. For a broader sorted odd-gap approach, [the complete-gap and breakpath argument, Theorem 10 and Corollary 12](https://rstation.ai/problems/collatz/papers/22/v3) controls the number of sorted gaps in terms of the number of breaks. That dependence leaves the unrestricted number of breaks open.

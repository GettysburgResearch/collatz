# Two different outcomes for the octave interval test

This is a companion to [the dyadic cycle order theorem](DYADIC_CYCLE_ORDER.md). The two coherent fixtures with subperiod denominators fail an integer-only necessary condition, despite passing real unit spacing and their stated prime tests. A different, exponentially large, coprime family passes the octave interval test in its strongest disjoint form. The full reduced denominator still separates these controls from ordinary cycles.

## Disjoint intervals at coprime near-critical clocks

Let $x_i$ be the positive rational odd phases of any orbit with odd period $p$ and native clock $N$, with the genuine odd-denominator rational map. Put $\alpha=\log_2 3$, $\delta=N-p\alpha>0$ and $\epsilon_i=\log_2(1+1/(3x_i))$. A product around the cycle gives $\sum_i\epsilon_i=\delta$. Suppose $\gcd(N,p)=1$ and $\delta\le1/p$. On the circle $\mathbb R/\mathbb Z$, put $a_i=\log_2(3x_i)$ mod one. The $p$ closed directed arcs from $a_i$ to $a_i+\epsilon_i$ are pairwise disjoint. For $p>1$ the circle distance of any two points on distinct arcs is at least $1/p^2$.

Indeed, $a_{i+1}=a_i+\alpha+\epsilon_i$ mod one. Choose $1\le q<p$, $j=i+q$ cyclically, and $s_i\in[0,\epsilon_i]$, $s_j\in[0,\epsilon_j]$. The difference of those two arc points is congruent to
$$
 qN/p-q\delta/p+e,\qquad
 e=\sum_{k=i}^{i+q-1}\epsilon_k-s_i+s_j\in[0,\delta].
$$
The interval for $e$ follows by retaining a part of the first and last increments and the intervening whole increments on a proper cyclic arc. The nonintegral grid point $qN/p$ is at least $1/p$ from any integer, while the absolute perturbation is at most $(p-1)\delta/p$. This proves the bound. The case $p=1$ has no distinct pair.

All lower-bound cycles of [CYCLE_INDEX.md, §3.1](CYCLE_INDEX.md) use convergents $p/N$ from below to $\beta=1/\alpha$. Hence $0<\delta=(N\beta-p)/\beta<1/(N\beta)<1/p$. Those positively separated, high-minimum, prime-tested rational cycles of large reduced denominator have **disjoint** octave intervals. There are at least $2^{(\theta-e)N}$ marked examples in that theorem's subsequence at each fixed tolerance $e>0$. Thus even exact disjointness poses no general obstruction in this coprime near-critical class.

## What the two previously frozen coherent fixtures do

For a pair of distinct rational odd phases $x,y$ and $k\ge1$, put $h=3(y-2^kx)$. The interval $[3y,3y+1]$ nests strictly inside the $2^k$-rescaled interval of $x$ exactly for $0<h<2^k-1$. Their interiors overlap without containment exactly for $-1<h<0$ or $2^k-1<h<2^k$. For integer $x,y$ the latter two intervals contain no integer. Inversions are also impossible at $k=1,2$. The criterion compares all dyadic translates in the positive reals, so an octave boundary introduces no special case.

| Native clock | Odd phases | $\lfloor\max x/\min x\rfloor$ | Inversions at $k=1,2,3,4$ | Partial overlaps at $k=1,2,3,4$ |
|---:|---:|---:|---|---|
| 7,275 | 4,590 | 38 | 26, 6, 19, 9 | 49, 13, 8, 0 |
| 865,445 | 546,035 | 39 | 73, 55, 114, 0 | 146, 58, 12, 0 |

No further pairs occur at $k\ge5$ for either fixture. The inversion totals 60 and 242 have the required parity and exceed $g-1$ for $g=15,35$. Both sets of rational phases exhibit overlaps and short-scale inversions forbidden at denominator one. This is a finite discrimination of these two named fixtures.

**Execution receipt (adelic lane).** The underlying [`coherent_controls.py`](coherent_controls.py) is SHA-256 `021f58b8b0a4622b219a00fb6729fb7b7960acd0ddddf7d867024da34b5aef57`. Its unchanged [`COHERENT_CONTROLS.json`](COHERENT_CONTROLS.json) is `921ebe2e8b4bd03ff40c772f8adf5ecf599ceac49bcadc3c208a20017eb7bf12`. I observed the lower endpoints *in time order*, before the existing sort, selecting the phases whose next verified parity bit was odd. The old routine outward-propagates integer enclosures at scale $S=2^{96}$; let $W$ be its printed maximum enclosure width and $L$ the sorted list of $3$ times these retained lower endpoints. For each $v\in L$, the count in an open interval $u<h<v'$ is bounded by binary searches in $L$ with cutoffs $2^k v+Su$ and $2^k v+Sv'$. Tighten both ends by $3(1+2^k)W$ for a lower count, and loosen them by the same amount for an upper count. The two totals agreed for each of the three distinct open intervals at every $k=1,\ldots,6$ in both fixtures. Bounds on the extreme enclosures exclude larger $k$. I independently replayed the first fixture with all 4,590 exact odd numerators over the full reduced denominator and integer binary searches, producing the same counts. These additional counts were executed by this lane and are separate from the coordinator's prior replay of physical unit spacing.

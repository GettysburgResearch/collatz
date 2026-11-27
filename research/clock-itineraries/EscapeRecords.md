# Critical clock records exclude positive ternary limits

For a given ordinary positive odd unit $a$, write $a_k$ for its $k$-th odd iterate and $s_k$ for the cumulative shortcut clock. Its odd orbit repeats **if and only if** some finite $M$ bounds $3^k/2^{s_k}$ at every odd time $k$. Equivalently, a nonrepeating orbit has arbitrarily late strict upper records of this ratio. At every such record $k$, every incoming suffix of length $b>0$ satisfies $2^{s_k-s_{k-b}}<3^b$. The record is also a strict height record of the ordinary orbit. [Lean equivalences](EscapeRecords.lean)

To see why a nonrepeating orbit has unbounded ratios, its first $N+1$ odd states are distinct, so some $a_k$ with $k\le N$ is at least $N$. For $N\ge3$, the finite simple-path distortion bound gives

$$
 (2^{s_k}a_k)^6\le(k+1)(3^k a)^6.
$$

If the ratio stayed at most $M$, this would imply $N^6\le(N+1)(Ma)^6$. Take $N=(Ma)^6+3$. The first crossing of any sufficiently high ratio level is a strict record. Conversely, a repeated state prevents every later index beyond one full lap from setting a new height record. This argument uses only finite integer inequalities. [Finite distortion bound](CycleDetection.lean)

At a critical record write $q=a_k$. For every $b\le k$, every positive odd unit $z$ and every $d\ge0$,

$$
 q=z+2\cdot3^b d\quad\Longrightarrow\quad 3(b-1)<z
 \qquad (b\ge1).
$$

Lift the same final $b$ gaps down to $z$. At any interior position the remaining clock $s$ and length $j>0$ satisfy $2^s<3^j$. The lifted state $y$ obeys $3^j y\le 2^s z$, hence $y<z$. All earlier states of this lifted ordinary path are distinct, since a repeated state would advance to an earlier occurrence of $z$. Following the initial state, every odd predecessor is coprime to three. The map $y\mapsto\lfloor y/3\rfloor$ is strictly increasing on the positive odd ternary units. It sends the $b-1$ internal states into the integers below $\lfloor z/3\rfloor$. [Lean representative bound](EscapeRecords.lean) · [Ordinary lifting theorem](DescentClocks.lean)

As a result, the ternary accumulation points of critical records on an escaping orbit avoid every positive odd integer. For a fixed odd ternary unit $z$, take $b=z+2$. Eventually all record endpoints $q$ exceed $z$. If $q\equiv z\bmod 3^b$, then their odd parity makes $q-z$ a multiple of $2\cdot3^b$, contrary to the displayed bound. Multiples of three are excluded by the unit property. The accumulation set is closed and avoids the dense set of positive odd ternary units, so it is nowhere dense. It also has ternary Haar measure zero by the backward word count at slope $8/5$, since $\log_2 3<8/5$. The critical record statement gives cofinality. Positive temporal densities at larger slopes are proved separately. [Positive-density records](EscapeFrontier.md)

A written argument also excludes positive **even** ternary limits. Take any positive integer $z\equiv q\bmod 3^b$ and reverse the $b$ actual gaps starting at $z$. At each stage the resulting shadow agrees with the actual predecessor modulo one fewer power of three, so the quotient $(2^e y-1)/3$ is an integer. Its numerator is positive. The affine identity and $2^s<3^j$ on every nonempty suffix show that all earlier positive shadows are strictly below $z$. If $y_0$ is the first shadow and $s$ is the total clock, multiplying these integer equations gives

$$
 \left(1+\frac1{3z}\right)^b
 \le \frac{2^s z}{3^b y_0} < z .
$$

Thus $b<(3z+1)\log z$ for $b\ge1$, using $\log(1+1/(3z))\ge1/(3z+1)$. For even $z$ the argument uses the affine equations on the last edge. The ordinary odd-path theorem above supplies the stronger linear bound for odd unit representatives.

The negative ternary integer $-1$ illustrates the remaining possibility. For each $B$ the ordinary staircase construction supplies $a=6\cdot2^B u-1$ with $B$ consecutive unit gaps followed by a gap to one. Throughout these first $B$ gaps, $s_k=k$ and $a_k+1=6\cdot2^{B-k}3^k u$. Every index is a critical record. For each fixed power of three all sufficiently late positions in the staircase are $-1$ modulo that power. Moreover, their log phases differ by $o_B(1)$ uniformly from an irrational rotation, because $a_k$ grows throughout the staircase and $a_0\ge6\cdot2^B-1$. As $B$ increases, the empirical measures of these finite **converging** examples tend to the atom at $-1$ times uniform circle measure. This supplies an ordinary finite realization of the joint limiting distribution that persists for arbitrarily long windows. The present proofs do not decide whether one fixed positive integer can sustain the critical records forever. [Staircase and final gap](SynchronousShadow.lean)

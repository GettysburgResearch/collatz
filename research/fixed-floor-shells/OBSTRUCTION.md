# A coloring obstruction to counting synchronized blocks alone

**FS-006. PROPOSED, pending independent review.** This is a theorem about a
surrogate coloring of the positive integers. It does not construct a second
Collatz component. It tests how much of the arithmetic a density or pattern
argument needs to retain. The map in the theorem is the *actual* shortcut
$T$. The surrogate satisfies several exact finite identifications and a
quantified approximation to invariance at almost every source.

Fix $0<\gamma<\alpha<1$, $0<\kappa<\alpha-\gamma$, an integer $d\ge0$
and a finite floor $H$. Put $U(m)=(3m+1)/2^{v_2(3m+1)}$ for odd $m$,
$V(n)=U^d(\mathrm{oddcore}(n))$, and
$I_X=[X,X+\lfloor X^\alpha\rfloor)\cap\mathbb N$. There exists a single
coloring $c:\mathbb N\to\{0,1\}$ with the following properties.

1. $V(n)=V(n')$ implies $c(n)=c(n')$. In particular $c(2n)=c(n)$
   exactly; for $d\ge1$ the odd siblings $m,4m+1$ have equal colors.
   All $n\le H$ have color zero.
2. Both colors have proportion $1/2+o(1)$ in **every** $I_X$ as integer
   $X\to\infty$.
3. For all sufficiently large $X$, each color contains at least $X^\gamma$
   disjoint consecutive blocks of length $\lfloor\kappa\log_2 X\rfloor$
   in $I_X$.
4. For all large $X$ and integers $1\le h\le\log X$, at most
   $C(h+1)|I_X|/\log X$ inputs $n\in I_X$ have
   $c(T^j n)\ne c(n)$ for some $0\le j\le h$. The constant may depend
   on the fixed parameters, not on $X,h$.

For example $\gamma=0.901,\alpha=0.98,\kappa=0.03$ gives two disjoint
colors each exceeding the presently deduced pattern lower bounds at much
smaller spatial scales and larger block lengths. Theorem FS-006 allows
disagreements at ordinary odd-source edges. It shows why the statistics
alone, even with the listed almost-invariance and finite identifications,
fail to imply a polynomial upper saving on either color. A proof using
exact unbounded-time forward invariance remains possible.

## Construction and short inverse fibers

Give each positive odd $y$ an independent pair consisting of a uniform
priority in $(0,1)$ and a fair color bit. All priorities and bits are
mutually independent. Fix a small $\lambda>0$ chosen below. Let
$D(y)=\max(1,\lfloor\lambda\log(2+y)\rfloor)$.
From $V(n)$ look forward through its first $D(V(n))$ odd states, including
$V(n)$ itself. Take the bit of the state with smallest priority.
Ties between distinct states have probability zero over the countable
collection; repeated occurrences of one state give the same bit. Denote this
preliminary color by $c_*(n)$. It has expectation $1/2$ at each input.
To obtain $c$, set the entire fibers $V^{-1}(v)$ to zero for
$v\in S=\{V(1),\ldots,V(H)\}$. This enforces property 1.

Here are uniform bounds on dependence. For all large $X$ consider odd
paths with starting odd core $m\le2X$ and at most
$L=\lceil 5\lambda\log X\rceil+d+5$ odd transitions. If their valuation
sum is $A$, then $2^A\le m4^L$, since every odd step satisfies
$3u+1\le4u$ and its endpoint is at least one. Put
$M=\lceil\log_2(2X)\rceil+2L$. For a fixed target and exactly $j$
steps, the positive valuation lists with sum at most $M$ number
$\binom Mj$ (including the empty case). Each list gives at most one
source by reverse substitution. Each odd source has at most one dyadic
multiple in $[X,2X)$. Hence any target can be visited from at most

$$
 B_X=\sum_{j=0}^L\binom Mj
 \le(L+1)(eM/L)^L
$$

inputs there, taking $\lambda$ small enough for $L<M/2$. For each
prescribed $\xi>0$ we may choose $\lambda$ so small that
$B_X\le X^\xi$ eventually: its exponent in $X$ is
$O(\lambda\log(1/\lambda))+o(1)$. Below choose
$4\xi<\min(\alpha,\alpha-\gamma-\kappa)$ and further decrease
$\lambda$ whenever a displayed bound requires it.

For a single input $n\in I_X$ the marks consulted for its own color
lie in the above depth range. So do all marks for all
$c_*(T^j n)$, $j\le h$, when $h\le\lambda\log X$. In fact their odd cores
are among the first $h+1$ odd states from $\mathrm{oddcore}(n)$,
$U(u)\le2u$, and each relevant window has length at most
$1+\lambda\log(2+2^{h+d}2X)\le2\lambda\log X$ eventually.
Thus at most $L+1$ *distinct marks* per input are involved even when
all its first $h$ shortcut iterates are tested together. Each mark can
affect at most $B_X$ inputs. The floor modification can affect at most
$|S|B_X$ inputs per interval, also when all those iterates are tested,
because reaching a modified anchor is a visit to $S$ at depth at most $L$.

## Local proportions and simultaneous monochromatic blocks

Changing one mark changes the preliminary total of either color on $I_X$
by at most $B_X$; the number of involved marks is at most $(L+1)|I_X|$.
The bounded differences inequality gives probability at most
$2\exp[-2t^2/((L+1)|I_X|B_X^2)]$ for deviation $t$ from its mean.
With $t=|I_X|/\log X$ these bounds are summable in integer $X$.
Borel–Cantelli and the negligible floor modification prove property 2.

Partition $I_X$ into disjoint candidate blocks of length
$K=\lfloor\kappa\log_2 X\rfloor$, discarding the terminal remainder.
Discard also blocks containing a source whose $V$ is in $S$, at most
$|S|B_X$ blocks. Each candidate uses at most $K(L+1)$ marks. A mark
is consulted by at most $B_X$ candidates, so greedy selection supplies
at least

$$
 g_X=\left\lfloor
 \frac{\lfloor |I_X|/K\rfloor-|S|B_X}{1+K(L+1)B_X}
 \right\rfloor
$$

candidates using pairwise disjoint sets of marks. The selection depends
only on the ordinary orbits. For either specified color the block success
events on these candidates are independent. Given all priorities in a
candidate, at most $K$ independent fair bits need that color, so its
success probability is at least $2^{-K}$. The expected number of successes
is at least $g_X2^{-K}\ge X^{\alpha-\xi-\kappa-o(1)}$. A multiplicative
Chernoff bound gives probability at most $\exp(-g_X2^{-K}/8)$ of falling
below half this lower estimate. These bounds are summable for both colors,
which proves property 3 almost surely.

## Persistence along the physical forward orbit

It remains to control the mean number of disagreements before applying
bounded differences. Let $1\le h\le\lambda\log X$ and
$r=h+d+2$. For $n$ uniform on $I_X$, let $t$ count the shortcut steps
needed to see the first $r$ source bits equal to one; infinity is allowed
in the definition. Put $S_0=\lfloor(\alpha/2)\log_2 X\rfloor$.
For $l\le S_0$, each length-$l$ parity word occupies one class modulo
$2^l$, hence

$$
 \Pr(t>l)\le(1+2^l/|I_X|)\Pr(\mathrm{Bin}(l,1/2)<r).
$$

The parity-cylinder assertion follows by induction: the two lifts of an
initial residue modulo $2^l$ have $l$th states of opposite parity, because
the affine slope upon changing the initial input by $2^l$ is odd.
Summing these tail bounds and using the fair-coin waiting-time mean $2r$
gives $\mathbb E[\min(t,S_0)]\le4r$ for large $X$. Also
$\Pr(t>S_0)\le 2e^{-cS_0}$ with some fixed $c>0$, since $\lambda$ can be
chosen to ensure $r\le S_0/4$ eventually.

We may discard inputs with repeated odd states among the first $L+1$
states from their odd core. A repeated state lies on a cycle of period
$p\le L$. Its valuation sum around one turn is at most $2p$ by
$2^A=\prod(3+1/u)\le4^p$. The affine cycle identity is
$(2^A-3^p)y=\sum_{i=0}^{p-1}3^{p-i-1}2^{A_i}$ with partial sums
$0\le A_i\le A$ and positive integer denominator. Hence
$y\le p12^p\le L12^L$. The fiber bound gives at most $L12^L B_X$
such inputs, which is $o(|I_X|/\log X)$ after decreasing $\lambda$.

For a remaining $n$ with $t\le S_0$, write $m_j=U^j(\mathrm{oddcore}(n))$.
All $m_{d+j}$, $0\le j\le h$, have appeared by ordinary shortcut time $t$.
Since $u/2\le T(u)\le2u$, their logs differ from $\log n$ by at most
$t\log 2$. Consequently their window lengths differ from
$\lambda\log n$ by at most $2+\lambda t\log2$, and are uniformly at
least a positive constant times $\lambda\log X$.

The windows of marks have consecutive index intervals
$[d+j,d+j+D(m_{d+j}))$. The total number of indices in their union
outside their common intersection is at most
$2h+2(\max_jD(m_{d+j})-\min_jD(m_{d+j}))$. This bound remains valid
if the intersection is empty, by comparing the leftmost and rightmost
start and end indices (or covering the union by the full span).
Because there are no repeated states, the minimum priority in the
union is uniform over its indices. If it lies in the intersection, all
colors agree. The probability of any disagreement is therefore at most

$$
 C_\lambda\frac{h+1+\lambda t}{\log X}.
$$

The same bound covers the smaller collection of shortcut iterates,
since taking an odd core skips only intervening halvings. Averaging
over inputs, including the two discarded sets, gives at most
$C_\lambda(h+1)|I_X|/\log X$ expected disagreeing inputs.

Changing a single mark affects this total by at most $B_X$, with at most
$(L+1)|I_X|$ marks. The preceding bounded differences estimate with
$t=|I_X|/\log X$ is summable even after multiplying by $1+\log X$ to
cover every admissible integer $h$. Add the floor modifications and use
Borel–Cantelli. For $h>\lambda\log X$ enlarge the constant and use the
trivial bound $|I_X|$. This proves property 4 and existence of one
coloring with all four properties.

The argument uses only finite positive paths, the elementary parity-word
bijection, and standard probability inequalities. No unproved stopping-time
estimate or assumption about the number of actual components enters the
construction.

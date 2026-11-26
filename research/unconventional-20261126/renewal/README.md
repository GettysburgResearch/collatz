# What an unbounded coefficient-record gap costs

**Status: PROPOSED written mathematics.** We work with one positive odd
ordinary trajectory, or an explicitly identified finite gap word. The
ordinary-source problem and the exclusion of nontrivial positive cycles
remain open.

## Conventions and scope

Write $U(x)=(3x+1)/2^{v_2(3x+1)}$, let $e_i$ be the chronological odd
gaps and let $M_k=3^k/2^{e_1+\cdots+e_k}$. On a nonrepeating positive
ordinary orbit the simple-path reciprocal estimate T-A3-651 gives
$x_k/M_k\to L\in(0,\infty)$. Indeed this ratio is the initial value
times the product of $1+1/(3x_i)$. Distinct positive odd integers tend to
infinity, hence $M_k\to\infty$ and its strict upper records $k_l$ are
cofinal. Include $k_0=0$. Put $q_l=x_{k_l}$.

A chronological block $w=(e_1,\ldots,e_m)$ between successive records
has prefix clocks $S_j=e_1+\cdots+e_j$, $S_0=0$, and local
multipliers $P_j=3^j/2^{S_j}$. Thus $P_j<1$ for $0<j<m$, and
$r=P_m>1$. Conversely these inequalities define the first-ladder
alphabet without any length cutoff. There are no ties, by unique
factorization. With $\alpha =\log_2 3$, the last gap is one and
$S_m=\lfloor\alpha m\rfloor$. Indeed
$0<\log_2 P_m\le\alpha -1<1$. In particular $1<r\le3/2$.
The exact chronological affine map is

$$
 F_w(z)=r(z+h_w),\qquad
 h_w=\frac13\sum_{j=0}^{m-1}P_j^{-1}\ \ge\ m/3.                 \tag{1}
$$

It maps rational inputs to rational outputs, is invertible over
$\mathbb Q$, and acts continuously on $\mathbb Z_3$. Define the
block drawdown in binary logarithms by
$D(w)=\max_{0\le j<m}(-\log_2 P_j)\ge0$.

## 1. Finitely many ternary accumulation points force rare transitions

Let $K\subset\mathbb Z_3$ be the set of subsequential limits of
$q_l$, and call a finite word recurrent when it occurs as an entire
record block at arbitrarily late indices. No bound on record gaps is
assumed in the following result.

**Theorem 1 (recurrent words and ordinary clock cost).** If $K$ is
finite, only finitely many distinct record words are recurrent. Label
each sufficiently late $q_l$ by its unique nearest point $u_l\in K$.
Call its next edge exact when $F_{w_l}(u_l)=u_{l+1}$. There are
infinitely many inexact edges. Along those edges the block lengths tend
to infinity. Every consecutive run of exact edges starting at a
sufficiently late height $q$ has total shortcut clock at most

$$
                         \log_2 q + O_K(1).                         \tag{2}
$$

The clock counts all gaps on the run. In particular, unbounded lengths
among the *recurrent* words already force an infinite ternary cluster
set even if other gaps can be arbitrarily long.

*Finite edge alphabet.* For each ordered pair $u,v\in K$, consider all
first-ladder words satisfying $F_w(u)=v$ in $\mathbb Q_3$. The two
coordinates are either both rational or both irrational, since the
affine map has nonzero rational slope and rational offset. In the
rational case the same equality holds in $\mathbb R$. Equation (1)
gives $m/3\le v/r-u\le \max(v,0)-u$. There are finitely many words
of bounded length, since their total clock equals $\lfloor\alpha m\rfloor$.
For an irrational ordered pair, two distinct affine maps taking $u$
to $v$ would give a nonzero rational affine equation for $u$;
parallel unequal maps cannot agree either. Equal maps have equal
slopes, hence equal $m,S_m$, and equal integer carries
$C=\sum_{i=1}^m3^{m-i}2^{S_{i-1}}$. The valuation of
$C-3^{m-1}$ is $e_1$ for $m\ge2$; removing the first summand and
dividing by $2^{e_1}$ recovers the carry of the remaining word. The
last letter is fixed by the total clock. Thus the maps themselves
determine the words. The set of exact labeled edges is finite.

Compactness gives $d_3(q_l,K)\to0$, so distinct labels are separated
for all sufficiently late times. Every recurrent word occurs infinitely
often at one fixed pair of labels. Continuity gives an exact edge at
that pair. For each fixed $J$, there are only finitely many words of
length at most $J$ and pairs of labels, so all sufficiently late
inexact edges have length greater than $J$.

*Paths in the exact graph.* A nonempty directed loop has composite
$z\mapsto(3^m z+C)/2^s$ with $3^m>2^s$, positive odd $C$, and
$s\ge1$. Its unique fixed point $C/(2^s-3^m)$ is negative with
odd numerator and odd denominator prime to three. The same holds at
each vertex on the loop, by rotation. Starting at a rational of
2-adic valuation zero and denominator prime to three, a gap larger
than the genuine $v_2(3z+1)$ makes the next valuation negative.
A smaller gap makes it positive, followed by a negative valuation at
the next step. Once negative, every gap subtracts its clock from that
valuation. Thus any finite concatenation between two loop vertices
consists exclusively of genuine signed rational gaps. From a loop
vertex the genuine subsequent gap sequence is periodic: one return
replays its deterministic signed gap word. Its first strictly
increasing coefficient time from any given record phase is unique.
Consequently an exact path between loop vertices follows this single
deterministic periodic itinerary throughout. In particular it cannot
move to a different cycle itinerary while retaining such endpoints.

For an arbitrary consecutive exact run, take its first and last
vertices that belong to any loop. Before and after them there are at
most $|K|$ edges each, because repetition would create a loop there.
If there is no loop vertex at all, its length is bounded as well.
The finite exact alphabet bounds all the clocks and affine constants
of these outer pieces by constants depending on $K$. Along the central
piece let $a/d<0$ be its first rational label, with $d>0$ odd, and
let $y$ be the positive ordinary value there. At its end the same
gaps take these starting values to $a'/d$ and $y'$, with
$a'\in\mathbb Z$, by the genuine signed gap rule. If the central
piece has $b$ odd gaps and total clock $s$, subtraction gives
$3^b(dy-a)=2^s(dy'-a')$. Hence $2^s\mid dy-a$, a positive
integer. There are finitely many choices of $a/d$ and
$y\le C_K(q+1)$ by the bounded initial piece. Adding the bounded
outer clocks proves (2). An infinite final exact run would contradict
(2) for its fixed positive start, so there are infinitely many
inexact edges. This proof uses the real positivity of that very
ordinary source.

**Corollary 1.1 (frequency in height).** Write $N_l$ for the number
of inexact edges from a fixed sufficiently late record up to record
$l$. With natural logarithms,

$$
 N_l\ \ge\ \frac{\log\log q_l}{\log(\log_2 3)}-O_{K,x_0}(1)
 \qquad(q_l\to\infty).                                           \tag{3}
$$

On each individual edge, $q_{l+1}/q_l\le (3/2)C_{x_0}$, by the
uniform finite distortion $1\le (x_k/M_k)/x_0\le C_{x_0}$.
For a full or partial exact run with shortcut clock $s$, its
coefficient is at most $(3/2)^s$, since the odd count is at most
the clock. Thus its endpoint is at most $C_{K,x_0}q^{\log_2 3}$
by (2). Alternate such runs with single inexact edges, including the
initial and terminal partial runs. Taking logarithms gives
$\log q_l\le C_{K,x_0}(\log_2 3)^{N_l+1}$, proving (3).
The count concerns the inexact edges defined from the true limit set.
It does not claim a positive temporal density of them.

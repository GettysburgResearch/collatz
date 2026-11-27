# Uniform spatial bounds for the original first-hit collision energy

**Status.** Proposed, source-qualified written theorem. The odd map is
\(U(x)=(3x+1)/2^{v_2(3x+1)}\) on ordinary positive odd integers. Both
copies have the original independent word law \(p(e)=2^{-e}\). This argument
bounds the contribution from specified sets of positive targets, including
translated intervals at arbitrary height. The global sublinear bound remains open.

Write \(q=3^k\), \(u_k(y)=q p_k(y\bmod q)/y\), and \(g_k(y)=L_k(y)/y\)
for the corresponding first-hit sum at odd depth \(k\). Let
\(w_x=3x/(3x+1)\) and \(f_j(x)=\prod_{i<j}w_{U^i x}\).
The ordinary inverse-word identity identifies \(g_k(y)\) with the sum of
\(f_k(x)/x\) over \(U^k x=y\) for which \(x\) first visits \(y\) at that
time. The convention is \(g_0(y)=1/y\). For \(k\ge1\) use the
first-hit layer bound \(g_k(y)\le C d_y\), with \(d_y\) the relative odd
natural density of the predecessors of \(y\). At positive multiples of
three both sides vanish. Paper 12, §7, gives the bound also on each periodic first-hit layer.
At those targets the
unrestricted \(u_k\) can exceed this cap. [Weaver, Paper 12, Corollary 5 and proof](https://rstation.ai/problems/collatz/papers/12) · [First-hit and atom inputs, PR 200 at 8e6add4](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md)

## A fixed summable source charges every simple collision suffix

Put \(\tau_b=\inf\{j\ge1:U^jb\in\{b,\ldots,U^{j-1}b\}\}\), with infinity
allowed. For any set \(E\) of positive odd sites, define
\[
 N_{b,n}(E)=\sum_{0\le j<n,\ j<\tau_b}{\bf1}_E(U^j b).
\]
There is one nonnegative summable function \(B\) on the ordinary positive
odd sites, independent of \(E,n,k\), for which every \(k\ge1\) satisfies
\[
 \sum_{y\in E}g_k(y)^2
 \ \le\ \sum_b g_1(b)^2{\bf1}_{k-1<\tau_b}{\bf1}_E(U^{k-1}b)
          +\sum_b B(b)N_{b,k-1}(E).                                  \tag{1}
\]
One may take \(B(b)=C^2\sum_{Ui=Uj=b,\ i\ne j}w_iw_j d_i d_j\), with
ordered pairs, and \(\|B\|_1\le4C^2\). Also
\(\sum_b g_1(b)^2\le4\sum_{b\ {\rm odd}}b^{-2}<\infty\).
Equation (1) retains the visits of each fixed source \(b\) and its actual
forward trajectory. All summands are nonnegative.

To prove it, expand a square into two actual first-hit source paths at depth
\(k\). Each of these paths is simple, including the endpoint. A repeat at
positions \(i<j\le k\) would give an earlier hit at \(k-j+i\) by applying
\(U^{k-j}\). If both paths are at the same \(b\) at time 1, bound the
pair of prefix weights by the full \(g_1(b)^2\). Their common remaining
suffix is simple, and its survival weight is at most one. Otherwise let
\(t\in[2,k]\) be their first synchronous meeting. They approach
\(b\) through distinct last parents \(i,j\). Each prefix to its parent
is itself first-hit, so the combined weight of these prefixes and edges
is bounded by \(w_iw_j g_{t-1}(i)g_{t-1}(j)\). The suffix of length
\(k-t\) is simple and uniquely determined by \(b\). Dropping its
survival factors and the extra first-hit restrictions involving the
earlier prefixes gives (1) by summing. The bound at time 1 follows from
\(\rho_1\le2\).

For a nonperiodic \(b\), the product events of visiting \(i,j\) for
\(Ui=Uj=b,\ i\ne j\) are disjoint across these ordered pairs and across
all such \(b\). Two sources entering a common nonperiodic tail on distinct
edges can have only one first common vertex of that form. Finite additivity
for independent ordinary samples followed by exhaustion bounds the sum
of \(d_i d_j\) by one. This part is the source estimate in the pinned
two-copy theorem. [PR 193 at 25f5462, collision source](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/boundary/COLLISION_SOURCE.md)

At a positive odd cycle \(D\), every phase has one cycle parent, of
density \(d_D\). All other parents of all phases of \(D\) have pairwise
disjoint predecessor sets, since a visit is immediately followed by
the first entry to the cycle. Their total density is at most \(d_D\)
by finite additivity. The cycle-parent/off-cycle-parent terms in both
orders therefore cost at most \(2d_D^2\). The off-cycle/off-cycle terms
cost at most \(d_D^2\), even after including all phase pairs.
Disjoint cycles have disjoint basins, so \(\sum_Dd_D^2\le\sum_Dd_D\le1\).
This supplies the remaining \(3C^2\) in the common cap, with no bound on
the number, length or location of cycles.

## A translated interval of any height

Let \(I\) consist of \(m\ge1\) consecutive positive integers, put
\(h=\lceil\log_2m\rceil^2\), \(\theta=H_2(\log_3 2)\), and let
\(G_h(m)\) be the uniform labelled image count for the shortcut map \(T\)
at native clock \(h\). Then
\[
 \sup_{k\ge1}\sum_{y\in I,\ y\ {\rm odd}}g_k(y)^2
 \le \|g_1^2\|_1+\|B\|_1\,\bigl(G_h(m)+h\bigr)
 \ll 1+m^{s},\qquad s=\theta-\gamma<\theta<1.                         \tag{2}
\]
Here \(0<\gamma<\theta\) can be taken from Weaver's Theorem A, decreasing
it if necessary. The effective alternative replaces \(G_h(m)\) by
\(2^{86}m^\theta/(1+\log_2m)^{3/2}\). The first-hit constant \(C\)
still comes from the stated input. [Weaver, Paper 28, Theorem A and Theorem 1](https://rstation.ai/problems/collatz/papers/28)

For each individual \(b\) count only its odd sites before \(\tau_b\).
On an infinite simple orbit, \(T^h\) is injective on those sites.
For an eventually periodic ordinary orbit, omit at most \(h\) transient
native sites whose \(h\)-step endpoint is on the eventual shortcut cycle.
The remaining transient sites have distinct transient images. The periodic
odd sites included before \(\tau_b\) are distinct and \(T^h\) acts
injectively on the full cycle. Thus at most \(G_h(m)+h\) counted sites
lie in \(I\). Substitution into (1) gives (2). The same proof applies
to a partial segment ending before the first repeat. Initial odd multiples
of three are allowed in this counting argument.

Consequently, if \(E_k\) is covered by intervals of integer lengths
\(m_{k,j}\ge1\) with \(\sum_jm_{k,j}^{s}=o(k)\), its original unrestricted
clipped energy is sublinear:
\[
 \sum_{\substack{y\in E_k,\ 0<y<2\cdot3^k\\y\ {\rm odd}}}
       \Phi(u_k(y))=o(k),\qquad \Phi(t)=t^2/(1+t).                     \tag{3}
\]
Indeed \(\Phi(g)\le g^2\); the global unrestricted/first-hit difference
in the clip is \(o(k)\) by the repeated-lap estimate and the 1-Lipschitz
property of \(\Phi\). The cost of this replacement is independent of
\(E_k\). An arbitrary moving interval of length \(O(k^{1/\theta})\)
satisfies (3) because \(s<\theta\). It also follows directly, using the
effective interval estimate in (2), for length \(O(k^{1/\theta})\).
Across a whole cover the additive \(h\) is already absorbed in the
power estimate. [PR 193, unrestricted comparison (8)](https://github.com/GettysburgResearch/collatz/blob/25f5462e2c43feea65760884f7ea8f53576fbc18/research/astra-unconventional-20261126/global/COLLISION_ENERGY.md)

The same estimate controls any nonnegative tapers dominated by sums
of interval indicators. Sparse heights extending across the full
representative window can require order \(k\) separate unit intervals.
The input gives no sublinear cover of all the targets whose original
harmonic amplitudes are large.

# Summable losses from every branch entering one ordinary orbit

**PROPOSED, source-qualified written theorem.** Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers, and suppose $a_0,a_1,\ldots$ is one injective forward $U$-orbit of ternary units. Any escaping orbit supplies such a tail. Write $d_x$ for the relative natural density among positive odd integers of those that visit $x$, allowing time zero. Put $\theta=H_2(\log_3 2)=0.94995\ldots$. There is an absolute $q_*<\theta$ with $0<q_*<1$ for which
$$
 \sum_{j\ge1}\sum_{U(y)=a_j,\,y\ne a_{j-1}}d_y^{q_*}\le C. \tag{1}
$$
The constant is uniform over the choice of orbit. In particular the relative loss $r_j=1-d_{a_{j-1}}/d_{a_j}$ satisfies $\sum_j r_j^{q_*}<\infty$, and the Shannon entropies of the **complete** reverse transitions from $a_j$ are summable over $j$. The first bound concerns all ordinary sibling basins from the entire infinite orbit at once.

As a consequence, an escape must have $(\log(2+a_j))^{1/\theta}r_j\to0$ in natural density in the odd clock. The exponent $1/\theta$ is approximately $1.0527$. This gives a weaker sufficient comparison than the open $1/\log x$ sibling floor in Paper 200. No such floor on general escaping orbits is proved. Cycles require a separate argument.

## Inputs and normalization

* Paper 102/v1, Theorem 1, equations (1)–(2): if $W_X$ is uniform on odd integers in $(X/4,X]$, $X\ge4M$, its first odd landing at most $M$ obeys $\Pr(\operatorname{Pass}_M(W_X)\in A)\le F_M(|A|/M+M^{-g})$ for **every** set $A$ of odd labels at most $M$. Failure has probability at most $F_MM^{-g}$. Here $F_M=C_0\exp(C_1\sqrt{\log M})$, and $g=1-\theta+1/351$. The result imports stage-count, loss-transport and smooth-passage estimates. [Power bounds for first Collatz landings](https://rstation.ai/problems/collatz/papers/102/v1)
* Paper 28/v3, Theorem A (P1): at clock $k^2$, $k=\lceil\log_2 M\rceil$, any interval of $M$ nonnegative integers has at most $K M^{\theta-\gamma}$ distinct labelled shortcut images, for an absolute $\gamma>0$. Deleting the labels gives the same upper bound. The shortcut acts injectively at every common clock on the full distinct orbit underlying an escape. Thus its orbit contains at most $K M^{\theta-\gamma}$ entries in $[1,M]$, including its odd part. The effective Theorem 1 of the same paper suffices with the weaker exponent $\theta$, by the same argument. [Uniform interval compression](https://rstation.ai/problems/collatz/papers/28/v3)
* Paper 12, Corollary 7, equation (27), and §10.1: at a nonperiodic odd unit $a$, $d_a=\sum_{U(y)=a}d_y$ and its natural-density reverse law is $Q_a(y)=d_y/d_a$. The paper gives the density-existence provenance and proof of this particular countable partition. We use its relative-odd normalization. [First-landing bounds and canonical inverse laws](https://rstation.ai/problems/collatz/papers/12)
* For an odd unit $b$ the density satisfies $d_b\ge c/b$ with one absolute $c>0$. This is the relative-odd consequence of Paper 10/v3, Theorem 1. Indeed the odd part of an integer reaches an odd target exactly when that integer does. If the odd-relative density is $d_b$, summing over the initial valuations with geometric weights gives the same natural density for all starts. The cited floor uses the averaged joint Syracuse mixing input. [Uniform predecessor lower bound](https://rstation.ai/problems/collatz/papers/10/v3)

## One common landing set for the whole orbit

Let $\mathcal Y$ contain every odd unit $y\ne a_{j-1}$ with $U(y)=a_j$ for some $j\ge1$. The other parents are odd multiples of three, and have zero odd-relative density since no odd transition lands at a multiple of three. The off-orbit parents are distinct and their predecessor sets are pairwise disjoint. Indeed each such parent enters the fixed injective orbit at its next odd step, and never leaves it. For $y\in\mathcal Y$ let $m_y$ be the least odd integer reaching $y$.

For each $M\ge2$ use the single deterministic set $A_M=\{a_j:j\ge0,\ a_j\le M\}$. If an odd input reaches some $y$ with $m_y>M$, every site up through $y$ is an ancestor of $y$ and exceeds $M$. All subsequent sites belong to the given orbit. Consequently its first landing at or below $M$ belongs to $A_M$, or it has no such landing. This implication holds on the ambient ordinary sampling space, before conditioning on any component or branch. For every finite subcollection of the parents with $m_y>M$, disjointness therefore bounds the sum of its probabilities in the $X$-window by $F_M(|A_M|/M+2M^{-g})$. First send $X$ to infinity at fixed $M$ and fixed finite subcollection, using the individual natural densities. Then take the supremum over finite subcollections. There is no countable exchange of a natural-density limit. We obtain
$$
 \sum_{y\in\mathcal Y:\,m_y>M}d_y
 \ll e^{C\sqrt{\log M}}
       \left(M^{-(1-\theta+\gamma)}+M^{-g}\right). \tag{2}
$$
The unweighted total over all $y$ is at most one by finite additivity and disjointness. Fix $0<\epsilon<\min(\gamma,1/351,\theta)/4$. The right side of (2) is $O(M^{-(1-\theta+2\epsilon)})$, absorbing finitely many small $M$ into the absolute constant.

The reciprocal floor can be charged to the **least ancestor**. When $m_y$ is a unit, $d_y\ge d_{m_y}\ge c/m_y$. When $3\mid m_y$, it differs from the unit $y$, so $U(m_y)$ still reaches $y$. This next unit is at most $(3m_y+1)/2\le2m_y$. In this case $d_y\ge c/(2m_y)$ as well. Thus, with $q_*=\theta-\epsilon$,
$$
 \sum_y d_y^{q_*}\le (2/c)^{1-q_*}\sum_y m_y^{1-q_*}d_y <\infty.
$$
For clarity, the $2^k<m_y\le2^{k+1}$ contribution on the right is $O(2^{k(1-q_*)}2^{-k(1-\theta+2\epsilon)})=O(2^{-k\epsilon})$ by (2). The finitely small labels are covered by the total mass bound. This proves (1). Charging the least ancestor, which may be a nonunit, is what allows the fractional exponent to reach below $\theta$. Using only the effective compression estimate yields (1) for every $\theta<q<1$.

## What one escaping orbit would have to satisfy

Write $D_j=d_{a_j}\ge D_0>0$. The parent partition gives $r_j=\sum_{y\in\mathcal Y:\,U(y)=a_j}d_y/D_j$. Concavity in the form $(\sum s_y)^q\le\sum s_y^q$ for $0<q<1$ gives
$$
 \sum_j r_j^{q_*}
 \le D_0^{-q_*}\sum_y d_y^{q_*}<\infty. \tag{3}
$$
The entropy contribution from the distinguished parent is $-(1-r_j)\log(1-r_j)\le r_j$. Each remaining contribution $-p\log p$ is at most $C_{q_*}p^{q_*}$ for $0\le p\le1$. Equation (1) thus gives $\sum_{j\ge1}\mathsf H(Q_{a_j})<\infty$. Also $Q_{a_n}$ followed backwards along the prescribed chain to $a_i$ gives cylinder probability $D_i/D_n$, tending to one uniformly in $n\ge i$ as $i\to\infty$ by monotonicity and boundedness of $D_i$.

The physical height satisfies $a_j+1\le(3/2)^j(a_0+1)$, so $\log(2+a_j)\ll_{a_0}j$ for $j\ge1$. For any fixed $c>0$, the fraction of $1\le j\le N$ with $r_j(\log(2+a_j))^{1/\theta}\ge c$ is $O_{a_0,c}(N^{q_*/\theta-1}\sum_{j\le N}r_j^{q_*})$, hence tends to zero. The same assertion holds for the ratio of any individual off-orbit sibling density to $D_{j-1}$, since it is at most $r_j/(1-r_j)$ and $r_j\to0$. In particular a lower bound $c/(\log(2+a_j))^{1/\theta}$ even on a set of odd clocks of positive upper density would exclude that escape. Ordinary monotone telescoping alone proves only $\sum_jr_j<\infty$ and leaves summable floors $j^{-1/\theta}$ possible.

**First unsupported inference.** An unconditional lower bound of this size for branch loss on the required fraction of the *same* forward orbit is missing. The available reciprocal bound can give only a constant times $1/a_j$ at a sibling of size comparable to $a_j$, and the distinct-state orbit zeta estimates already permit these costs to be summable after raising them to powers below $\theta$. Paper 200 proves examples with small sibling/main density ratios and arbitrarily slow density growth across arbitrarily long fixed initial climbs. Its results concern existence in supplied predecessor trees and do not give the requisite forward-ray lower comparison. The one- and two-window carry estimates in this packet control prime factors of physical carries and have no present lower bound for these sibling densities. [Small sibling basins and slow climbs, Paper 200, Theorems A–C and §10](https://rstation.ai/problems/collatz/papers/200)

## The possible first entry positions of an entire translated interval

There is also a deterministic count for arbitrary **individual starts**, including odd multiples of three. For the same ray, let $J(x)$ be the index of its first odd vertex $a_j$ visited by the shortcut trajectory from $x$, when any is visited. In every translated interval $I$ of $m\ge2$ consecutive positive starts,
$$
 \#\{J(x):x\in I,\ J(x)\text{ defined}\}
 \le (H+2)G_H(m)\ll (1+\log m)^2m^{\theta-\gamma},
 \qquad H=\lceil\log_2m\rceil^2. \tag{4}
$$
Group the ordinary starts by the exact value $z=T^Hx$. Among starts in one group that have yet to visit the ray at clock $H$, all later first visits are the same by determinism. For those which have visited it by $H$, the common $z$ lies on the injective full shortcut trajectory from $a_0$. Their first visited odd ray vertices are entries of that fixed trajectory at most $H$ shortcut clocks before $z$, hence there are at most $H+1$ of them. The number of groups is at most the labelled image count in Paper 28/v3 (P1). This argument pays no factor depending on the location of $I$, the height of the ray or the time of its first visit. Ordinary versus shortcut clocks give identical lists of odd visits.

In particular, among $1\le j\le N$ at most $O((1+\log N)^2 N^{(\theta-\gamma)/\theta})$ admit *any* positive start $x\le j^{1/\theta}$ that reaches $a_j$ without visiting $a_{j-1}$ first. Such a start has $J(x)=j$ by injectivity, so apply (4) once to the interval through $\lfloor N^{1/\theta}\rfloor$. This controls all possible arrival times from those starts, even though a single fixed start in the main branch reaches every sufficiently late $a_j$. The result locates how earlier visitors enter a hypothetical divergent component. It does not supply a competing entry from a smaller source when the supplied head must be removed.

## Simultaneous choice in every positive component

Partition the positive integers by eventual intersection of their shortcut trajectories. In each escaping component choose one full forward ray beginning at an odd unit. In each cyclic component choose exactly its periodic states. Let $S$ be their union, including **every intervening shortcut state** of each chosen odd ray, and let $S_o$ be its odd part. For every fixed clock $H$, $T^H$ is injective on $S$. It acts injectively within each chosen ray or cycle, and different components remain disjoint. The same (P1) argument bounds $|S_o\cap[1,M]|\le KM^{\theta-\gamma}$, independently of the number of components and of the chosen initial vertices.

Take all odd parents $y\notin S_o$ for which $U(y)\in S_o$. This includes arrivals to initial vertices of escaping rays. Cycle parents within $S_o$ are excluded. Every odd start outside $S_o$ eventually enters it and has exactly one last parent before first entry. The resulting predecessor sets are pairwise disjoint. For any member of a branch with $m_y>M$, its first landing is in $S_o\cap[1,M]$ or it fails to land. Thus the same finite-window tail bound holds for the **whole union** of such branches. The charge to the least ancestor for unit $y$ gives (1) with the very same constant for all these parents across the entire partition. In fact $\sum_y d_y=1$. For fixed $M$ the branches with $m_y\le M$ are finite since their minima are distinct. The size of $S_o$ has density zero, and the finite-window tail tends to zero with $M$, so the finite partial masses exhaust one. This also handles the union of nonunit-parent singletons without assuming countable additivity of natural density. The construction permits simultaneous concentration around every chosen ray and cycle. It places no restriction on their number that would single out the cycle of 1.

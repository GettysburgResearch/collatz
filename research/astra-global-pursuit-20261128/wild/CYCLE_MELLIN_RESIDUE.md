# A canonical pole with coefficient equal to the ordinary basin density

**Source-qualified written theorem.** Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on
positive odd integers, with $d_a$ the ordinary relative odd natural density
of sources visiting $a$. Write

$$
 \delta=\tfrac12\log(4/3),\qquad
 c(x)=\frac{3x}{3x+1},\qquad w(x)=-\log c(x).
$$

For each positive odd ternary unit $a$, use the canonical integer value
$h(a)>0$ of the ternary stationary density and the canonical conditional
real law $\mu_a$ of the joint stationary affine series. For $0<s<1$ put

$$
 G_a(s)=\frac{h(a)}a\int(1-r/a)^{-s}\,d\mu_a(r).                       \tag{1}
$$

The integration is well-defined even at periodic roots. For an odd cycle
$C$ let $L_C=\sum_{x\in C}w(x)$, and let $d_C$ be its common vertex
predecessor density. Then

$$
 \begin{aligned}
 a\ \text{nonperiodic}:&& G_a(1)&=\delta\,d_a,\\
 a\in C:&& \lim_{s\uparrow1}(1-s)G_a(s)&=\delta\,d_C/L_C.             \tag{2}
 \end{aligned}
$$

In particular the pole coefficient at the specified positive integer $1$
is exactly $d_1/2$. If $\mathcal D_{\rm per}$ denotes the relative odd
natural density of sources eventually entering any positive cycle, then

$$
 \lim_{s\uparrow1}(1-s)
     \sum_{\substack{a\ge1\ {\rm odd}\\3\nmid a}}w(a)G_a(s)
                 =\delta\,\mathcal D_{\rm per}.                         \tag{3}
$$

Both infinite sums and the limit in (3) are justified below. Formula (2)
gives a single-root sufficient condition for full Collatz: a lower bound
$1/2$ for that root's coefficient. Under the positive predecessor-density
input, $d_1=1$ rules out every other ordinary trajectory component. We
have no proof of that lower bound. Formula (3) also separately measures
the possibility of positive escape, without conflating it with additional
positive cycles.

## Source statements and distinctions

We use Weaver's [Paper 19 v2, §9.2, (F3), (F9)–(F13)](https://rstation.ai/problems/collatz/papers/19/v2)
and [Paper 12, §§8–12, (23)–(29), (35)](https://rstation.ai/problems/collatz/papers/12/v1).
These import Valbuena's canonical ternary profile, the positive Syracuse
atom floor, ordinary orbit-set sparsity and relative landing estimates.
All are used here as **written external inputs**. No external Lean package
was rebuilt here. Paper 19 already proves the geometric complete-lap law,
linear endpoint mass at positive periodic roots, and a uniform relative
gap at nonperiodic roots. The calculation here identifies the exact Mellin
coefficient with ordinary basin density, sums it across all roots, and
transfers the singular observable to finite conductors in a companion note.

Under the canonical inverse law, the successive unit parents $X_j$ satisfy
$U(X_j)=X_{j-1}$ and $X_0=a$. For a depth-$j$ word of total exponent $D$,
the multiplier is $A=3^j/2^D$ and its probability is $Ah(X_j)/h(a)$.
The normalized real residual equals

$$
 W_a=1-R_\infty/a=\prod_{j\ge1}c(X_j),\qquad R_\infty\sim\mu_a.
$$

Distinct finite odd segments have $\sum w(x)\le B$ with an absolute
constant $B$, by the published uniform orbit packing estimate. At
nonperiodic roots $W_a\ge e^{-B}$ on every such ray.

## Nonperiodic normalization

At a nonperiodic positive odd unit let $Q_a$ denote the inverse law of
actual source density on parent cylinders. If $\beta_a$ is the mean
correction weight of first hits, the cited sources give

$$
 \frac{dP_{h,a}}{dQ_a}=\frac{d_a}{\beta_a}W_a,\qquad
             h(a)=\delta a\beta_a .
$$

Taking the inverse moment proves the first line of (2). This identity
directly combines the known two source formulas.

## Exit during one lap of an ordinary cycle

Let $\lambda=e^{-L_C}$. The probability of one full backward lap based at
$a$ is $\lambda$. The lap multiplies the residual $W_a$ by $\lambda$.
Let $E$ denote the event that the selected inverse ray exits the cycle
before completing that lap, and set

$$
 B_a(s)=\frac{h(a)}a\,\mathbb E_a[W_a^{-s}1_E].
$$

On $E$ the residual is bounded away from zero uniformly: the partial lap
cost is at least $\lambda\ge e^{-B}$, the off-cycle edge has $c(x)\ge3/4$,
and its nonperiodic remaining ray has product at least $e^{-B}$. Hence
$B_a$ is entire in a complex Mellin variable. Summation of the geometric
number of complete laps gives

$$
                    G_a(s)=\frac{B_a(s)}{1-\lambda^{\,1-s}},
                    \qquad \Re s<1.                                    \tag{4}
$$

To evaluate $B_a(1)$, split by the exit parent $y$, which can occur at any
of the finitely many phases in the first backward lap. For the entire
prefix through $y$ the selection probability is $A h(y)/h(a)$. Its
residual multiplier is $A y/a$. Consequently the contribution to
$B_a(1)$ is exactly $(h(y)/y)\mathbb E_y W_y^{-1}=\delta d_y$.
Every off-cycle unit parent appears once in this decomposition.

We verify the countable basin partition needed for their sum. The
off-cycle parents of all phases have disjoint predecessor sets, since an
ordinary orbit entering the cycle has a unique last off-cycle member.
Nonunit parents have only themselves as odd predecessors and can be
included as zero-density terms. A countable union of such terms cannot
be discarded on that fact alone. For $M\ge\max C$, mark the parent
selected by every odd $q\le M$ that eventually reaches $C$ from outside.
This is a finite set. If a source whose last parent is unmarked had
visited any integer at most $M$ before meeting $C$, that earlier point
would have marked its parent. Thus its first odd landing at most $M$
is one of the finitely many cycle phases. For sources in any octave
$[Y,2Y)$, $Y\ge M$, (35) bounds the whole omitted mass by
$|C|C_A(\log M)^{-A}$. The cycle vertices themselves have zero density.
This establishes

$$
                \sum_{\text{off-cycle parents }y}d_y=d_C .
$$

The same argument includes the possibly infinite family of zero-density
nonunit parents. It follows that $B_a(1)=\delta d_C$. Equation (4) gives
(2), including the actual simple pole since $d_C>0$. The sign convention
in (2) uses the positive coefficient of $(1-s)^{-1}$ as $s\uparrow1$.
For $C=\{1\}$, $L_C=\log(4/3)=2\delta$.

## Summing all positive roots

For a finite set $F$ of odd units, the sum $\sum_{a\in F}w(a)d_a$ is the
limiting source mean of the sum of $w$ over distinct visited points in
$F$. The orbit packing bound therefore gives

$$
                       \sum_a w(a)d_a\le B.                             \tag{5}
$$

This includes periodic vertices counted once per orbit. A nonperiodic
$G_a(s)$ is at most $G_a(1)=\delta d_a$ since $0<W_a\le1$, so all
nonperiodic roots make a vanishing contribution to (3). For each cycle,
$0<B_a(s)\le B_a(1)$, and the sum of its $w$-weights is $L_C\le B$.
Putting $u=1-s$ gives the domination

$$
 u\sum_{a\in C}w(a)G_a(s)
     \le \delta d_C\,\frac{uL_C}{1-e^{-uL_C}}
     \le \delta d_C\,\frac{B}{1-e^{-B}}\qquad(0<u\le1).               \tag{6}
$$

The disjoint cycle basins give $\sum_C d_C\le1$ by finite additivity.
Dominated convergence now proves (3) with $\sum_Cd_C$ on the right.

To identify that sum with the ordinary density of the full eventually
periodic set, include all cyclic basins reached by any odd $q\le M$.
There are finitely many. Any ultimately periodic source in an omitted
basin never visits $[1,M]$. The failed first-passage bound in Paper 12,
Theorem 11, makes their upper asymptotic proportion tend to zero as
$M\to\infty$. An octave bound uniform in $Y\ge M$ transfers to the
initial interval by a dyadic decomposition, with the initial bounded
remainder negligible. This proves existence and the claimed value of
$\mathcal D_{\rm per}$.

The companion [unbounded conductor trace](UNBOUNDED_CONDUCTOR_TRACE.md)
writes (1) and (3) directly in terms of the unconditioned real/ternary
stationary probability. The order of the conductor and Mellin limits
matters. Their numerical value at $a=1$ remains the global proof gap.

The [single-scale theorem](SINGLE_SCALE_POLE.md) subsequently removes the need for ordered limits, allowing the explicit exponent $1-K^{-1/5}$ at conductor average $K$.

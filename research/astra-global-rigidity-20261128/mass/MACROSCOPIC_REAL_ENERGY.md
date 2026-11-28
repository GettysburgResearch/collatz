# Exact interior stabilization and the physical unit-bin energy on escaping rays

At a nonperiodic positive odd ternary unit $y$, write $h(y)$ for its stationary integer trace, $\mu_y$ for its probability on the absolute affine intercept $R$, and $F(y)=\prod_{i\ge0}3U^iy/(3U^iy+1)$ when its forward orbit escapes. Use
\[
  E_y(t)=\frac{h(y)^2}{y}
     \sum_{k\ge0}\mu_y\big([k,k+1)\cap[ty,y]\big)^2,\qquad 0<t<1 .
                                                                    \tag{1}
\]
The real bin width is one at the original physical height; in the relative real coordinate $R/y$ it is $1/y$. This section uses the [PR193 bilateral coupling and fixed-root canonical real fibres, frozen at aa686899](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/REAL_FIBRE_AND_FRONT.md), including its stated analytic sources.

## Exact stabilization away from the upper survival endpoint

For a positive escaping ray $a_n$ use the bilateral ordinary process $(Z_v)_{v\in\mathbb Z}$ with every grade mass normalized by $H_C>0$. Write $M_y=h(y)F(y)/y$, $w(x)=3x/(3x+1)$, and let $\eta=\mathcal L(J)$ for $J=\prod_{v\in\mathbb Z}w(Z_v)$. The rare-event conditioning in the bilateral construction identifies the law of $T_{a_n}(R)=F(a_n)(1-R/a_n)$ under $\mu_{a_n}$ with the law of $J$ given $\mathcal E_n=\{Z_n=a_n\}$, of probability $M_{a_n}/H_C$. For every fixed $u>0$ there is a finite $N=N(C,u,a_0)$ such that for all $n\ge N$ there is **equality of restricted finite measures**
\[
 M_{a_n}\,(T_{a_n})_*\mu_{a_n}\big|_{[0,1-u]}
       =H_C\,\eta\big|_{[0,1-u]}.                                   \tag{2}
\]
Indeed if all ordinary vertices of a bilateral sample exceed $L$, uniform simple-path packing gives $-\log J\le C L^{-1/50}$ by monotone exhaustion in both directions. Choose $L$ so this forces $J>1-u$. Every remaining sample thus hits an ordinary $m\le L$. The finite set of such $m$ in this component has fixed grades, and its deterministic forward paths all merge with the named ray by a common finite grade $N$. Therefore $\{J\le1-u\}\subseteq\mathcal E_n$ for every $n\ge N$ up to null sets. The conditional law gives (2). In particular no off-spine inverse branch at these high grades supplies any mass on the indicated corrected strip. [Uniform simple-path packing at pinned PR212](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

On a high nonperiodic target in any component, positive real mass at $R\ge ty$ forces the target to lie downstream of a source $m\le L(t)$ by the same argument on its inverse past. At a fixed target, all inverse children except finitely many therefore supply zero mass on this strip: at most one child on the path from each such $m$ can enter the target, since the target is nonperiodic. If an ordinary component is eventually periodic, each small $m$ in that component has a finite forward orbit. Hence (1) vanishes exactly at all sufficiently high nonperiodic targets in any fixed eventually periodic component. If every orbit is eventually periodic, (1) vanishes outside a finite set simultaneously across all such components; the same finite set of $m\le L(t)$ suffices. This observation does not require the only cycle to be the usual one.

## A square-root energy lower at every sufficiently high ray site

Under counted synchronization, each escaping ray admits a fixed rational $t\in(0,1)$ and a constant $c_C>0$ such that
\[
                E_y(t)\ge c_C\sqrt{\log y}
       \qquad\text{for all sufficiently late ray sites }y=a_n .
                                                                    \tag{3}
\]
More generally, the proof works for any $t$ with $\eta([0,1-2t])>0$. Such $t$ exist since $J<1$ almost surely, already from its factor at grade zero. At large $y=a_n$, $F(y)\to1$, so $T_y(r)\le1-2t$ forces $r\ge ty$.

For the quantitative input we use Weaver's actual covers, stronger here than the stated Hausdorff-null conclusion. At every fixed ordinary root $x$ and every $N\ge1$, his proof constructs $V_{N,\epsilon}(x)$ as a finite union of dyadic cells of mesh $r_N=2^{-8N}$ and total length $O_x(1/(\epsilon\sqrt N))$. Each legal path with mean gap two and single-gap frequencies $2^{-e}$ has its real limit in $V_{N,1/i}(x)$ for all sufficiently large $N$ for some integer $i\ge1$. Here the constant $L$ in Weaver's proof is fixed once. The canonical path law at each specified $x$ meets these hypotheses almost surely by the frozen fixed-root word theorem. [Weaver, Paper 175/v1, §7, (11) and its grid-cover argument](https://rstation.ai/problems/collatz/papers/175) · [PR193 fixed-root path theorem](https://github.com/GettysburgResearch/collatz/blob/aa6868996f6f30b12d91c367f7c6edcfd93784b2/research/astra-six-hour-20261127/escape/CANONICAL_INVERSE_PATHS.md).

Choose a grade-zero site $x$ whose component probability contributes positively to $\{J\le1-2t\}$. Conditional there, $J=T_x(R_x)$ for $R_x\sim\mu_x$. There exist fixed $i,N_0$ for which the set of samples satisfying all three conditions $Z_0=x$, $J\le1-2t$, and $R_x\in V_{N,1/i}(x)$ for all $N\ge N_0$ has positive probability $p$. This uses only countable exhaustion. Their $J$ values at each such $N$ lie in $T_x(V_{N,1/i}(x))$, a union of at most $C_x i/(r_N\sqrt N)$ intervals of length $F(x)r_N/x$.

The $T_y$ images of the unit bins at $y$ form a translated or reflected grid of mesh $F(y)/y$. For sufficiently large $y$, choose $N$ so $r_N$ is within a fixed factor $2^8$ of $1/y$. Each of the preceding intervals meets $O_x(1)$ of these grid cells. Thus $O_{C,t}(y/\sqrt{\log y})$ physical bins carry, within $r\ge ty$, raw mass at least
\[
  \frac{h(y)}{y}\,\mu_y(\text{selected strip bins})\ \ge\
                     \frac{H_C p}{F(y)} .
\]
This is (2) applied to the union of the selected cells intersected with $[0,1-2t]$. Cauchy–Schwarz proves (3), with no convergence rate needed in the uncropped bilateral coupling.

It follows that an independently proved $o(\sqrt{\log y})$ bound for each fixed rational macroscopic strip, along even one unbounded subsequence on each putative escaping ray, would exclude escape. Existence of such a subsequence remains open. Equivalently, a uniform upper of that order over all high nonperiodic targets is sufficient. Under the counted source inputs, if there is no escaping trajectory, (1) is eventually zero for each fixed $t$. The [uniform finite and stationary Haar energy bounds](UNIT_OFFSET_ENERGY.md) apply genuine fixed-total arithmetic but do not control this moving ordinary source. Fixed nonperiodic terminating roots also have singular canonical fibres at arbitrarily fine *absolute* resolution. The present test fixes absolute resolution and keeps a growing root with a positive **relative** real mark.

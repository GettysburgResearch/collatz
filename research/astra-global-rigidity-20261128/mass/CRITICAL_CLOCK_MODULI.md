# Native clock mixing between the fourth-root and square-root scales

**Source-qualified written deduction.** The full ordinary marked first-hit row law, component mass/capture and finite-classifier inputs are the pinned premises identified below. Their joint-mixing and density hypotheses remain in force; the new Fourier and modulus arguments are not a Lean formalization of those inputs.

Use the genuine shortcut map $T$, and put $L=\log X$, $\alpha=\log_2 3$, $D=\log(4/3)$. Sample actual integers with probability proportional to a fixed nonnegative smooth nonzero function $\Phi(n/X)$ compactly supported in $(0,\infty)$. Choose one ordinary reference in each true component. At a physical meeting of the source and reference orbits, the odd counts and shortcut counts up to that meeting give two signed differences $(j,s)$ in source-minus-reference order. In a bounded component these coordinates are defined modulo its primitive lap $(q_C,\ell_C)$, with $q_C$ odd departures and $\ell_C$ shortcuts. On escape they are genuine integers. At modulus $m$ use
\[
 G_{C,m}=(\mathbb Z/m)^2/\langle(q_C,\ell_C)\rangle
 \quad\text{on a bounded component},\qquad
 G_{C,m}=(\mathbb Z/m)^2\quad\text{on escape}.
\]
Let $\Delta(X,m)$ be the total variation distance (supremum convention) between the actual joint law of the component and its clock class and the law with the same component marginal and conditionally uniform class. Changing references translates each component's coordinates and leaves the statistic unchanged. Let $p_{\rm esc}$ be the limiting ordinary mass of all escaping components.

For an integer band $K=K(X)\to\infty$, average uniformly over the integer moduli $K\le m\le 2K$, denoting this by $\mathbb A_K$.

1. On every bounded component, the conditional discrepancy tends to zero in modulus average whenever $K=o(\sqrt L)$. This holds for their entire unnormalized contribution after summation. At any fixed $c>0$, the conditional discrepancy on **every** fixed escaping component has positive lower limit, at least $\eta(c,\Phi)>0$, uniformly for $m\ge cL^{1/4}$. If $m/L^{1/4}\to\infty$, the conditional discrepancy tends to one.
2. Consequently, throughout the whole open interval of scales
\[
         K/L^{1/4}\to\infty,\quad K/\sqrt L\to0
         \quad\Longrightarrow\quad
               \mathbb A_K\Delta(X,m)\ \longrightarrow\ p_{\rm esc},    \tag{1}
\]
At $K\sim cL^{1/4}$ the average has lower limit at least $\eta(c/2,\Phi)p_{\rm esc}$, and converges to zero if $p_{\rm esc}=0$.
3. For example at $K=\lfloor L^{1/3}\rfloor$, a single graph-independent computable choice $m_X\in[K,2K]$ gives the exact limit in (1). The choice below uses no list of existing cycles. The statistic also has a finite implementation, with the stated source and classification inputs.
4. For the full pair at a fixed positive odd unit first-hit target, any sequence on which
\[
  \delta(L,m)=\min_{(u,v)\in\mathbb Z^2\setminus\{0\}}
        \max\{|v|/m,\sqrt L\,|u+\alpha v|/m\}\ \longrightarrow\infty  \tag{2}
\]
gives conditional uniformity in total variation. It does so simultaneously on the full component law after passing to the stated quotients. For every $\theta<1/4$, there are arbitrarily large scales with $m\asymp L^\theta\to\infty$ on which (2) holds. This last range uses only the irrationality of $\alpha$ and the original marked first-hit input. If one imports the stated quotient-of-logarithms irrationality exponent at most three, (2) holds at **every** $m\le L^{1/6-\epsilon}$.

PR215 already defined these quotient groups, proved their uniformity on every $m\le L^{1/11}$ using its quoted effective fixed logarithm bound, and showed that escape has discrepancy tending to one at $m/L^{1/4}\to\infty$. Its upper-scale support argument is used here. The fixed-$c$ lower, bounded-lap modulus averaging, and exact mass limit in (1) use the full ordinary marked row kernel in the new steps below. [PR215, checkpoint 5, true clock groups and square-root support, pinned at 121054cf](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/escape/phase5/SMOOTH_SOURCE_CLOCK_GROUPS.md)

## Total variation against a sampled strip

At a fixed positive odd unit first-hit target $a$, set $j_0=\log(X/a)/D$, $z_0=\log_2(X/a)$, and use the conditional law given that the source visits $a$. In sum norm on the entire integer pair $(j,s)$ it differs by $o(1)$ from
\[
 P_L(j,s)=L^{-1/2}G((j-j_0)/\sqrt L)\,H(s-\alpha j-z_0),             \tag{3}
\]
where $G$ is the centered Gaussian density of variance $2(\log2)^2/D^3$ and $H$ is a nonnegative smooth compactly supported probability density. The support length of $H$ is bounded in terms of $\Phi$ and the absolute simple-first-hit survival floor. The onset of the $o(1)$ may depend on $a,\Phi$. This approximates the full probability law before reducing it modulo any group, so projection incurs the same error even at varying $m$.

To check this inference, start at positive odd sources. The frozen original exact-total first-hit kernel gives, uniformly over compact central $\zeta=(s-2j)/\sqrt j$, a row count divided by $p=a2^s/3^j$ equal to $(c_a+o(1))\,2^{-s}\binom{s-1}{j-1}$. The row's actual mark $F=n/p$ tends weakly, uniformly along these totals, to the same probability $V_a$ on $[c_0,1]$. With $w=s-\alpha j-z_0$ the row source weight is therefore proportional to
\[
       2^w\,\int\Phi(2^w f)\,dV_a(f).
\]
This is smooth and supported in a fixed bounded $w$-interval. Uniformity in $w$ on that interval follows by compactness or the common derivative bound. The geometric local Gaussian and the strip relation give the displayed $G$, since $s-2j=-(2-\alpha)(j-j_0)+O(1)$. There are $O(1)$ totals per grade and $O_B(\sqrt L)$ grades in a fixed standardized central cutoff. Their per-row $o(L^{-1/2})$ errors sum to $o_B(1)$. The actual noncentral tail goes to zero on increasing this cutoff, by the signed-kernel renewal-strip argument. The tail of (3) does as well by its Gaussian bound and the fixed number of totals per grade. For all integer sources write $n=2^e n'$ with $n'$ odd. At any fixed $e$, the change $(s,z_0)\mapsto(s-e,z_0-e)$ leaves $w$ unchanged, the central grade moves only $O(e)$, and the relative source mass is $2^{-e-1}$. Removing $e>E$ costs $O_\Phi(2^{-E})$, then let $E\to\infty$. Finally normalization makes the integral of $H$ one: the full sum of (3) tends to $\int G\int H$, by irrational rotation averaging of the periodization of $H$ along the increasing Gaussian grade window. This also follows from the Poisson calculation below with $m=1$. [Frozen positive-source central row, actual mark, first-lap convention and tail proof](FIXED_BASIN_NATIVE_WINDOW.md)

Write Fourier transforms with phase $e^{-2\pi i x\xi}$. Poisson summation for (3) makes its coefficient at $\chi_{u,v}(j,s)=e^{2\pi i(uj+vs)/m}$ a sum over all lifts $(u',v')=(u+mh,v+mk)$. Each term has an irrelevant unit phase from $(j_0,z_0)$, and modulus
\[
          |\widehat G(\sqrt L(u'+\alpha v')/m)|\,
          |\widehat H(v'/m)|.                                          \tag{4}
\]
Changing all signs has no effect on the following estimates. Both transforms are Schwartz. For a bounded root its true quotient retains the coefficients whose indices satisfy $q_Cu+\ell_C v\equiv0\bmod m$. This is exact even when $m$ shares factors with both lap counts.

Consider the lattice in $\mathbb R^2$ of the vectors
\[
              (v/m,\sqrt L(u+\alpha v)/m),\quad (u,v)\in\mathbb Z^2 .
\]
For a quotient restrict it by the preceding congruence. If the shortest nonzero vector in the maximum norm tends to infinity, the sum of (4) over all nonzero lattice vectors tends to zero. Indeed separated vectors in a box of radius $R$ number $O((1+R/\delta)^2)$ for separation $\delta$, and the summands decay faster than any power of the radius. Summing the absolute Fourier coefficients of all nontrivial characters is bounded by this same sum, because different characters partition the lifts. Fourier inversion bounds the conditional TV discrepancy by this quantity and the original $o(1)$ in (3). This proves (2) for a fixed target. For a bounded component use an odd vertex on its cycle as target. Every member hits it and the first-hit coordinates project to the correct quotient. On a fixed escaping component, choose an odd waypoint receiving all but an arbitrarily small conditional mass from its basin. Indeed basins of successive waypoints exhaust the component in natural mass, by the countable fixed-seed capture. On that basin the signed reference coordinates differ from the first-hit pair by one constant vector. Let the omitted mass decrease after the $X$ limit. Finally truncate to finitely many components with arbitrarily high total natural mass. [Component masses, overlap and finite-seed capture](FINITE_COMPONENT_PARTITION.md)

## Good moduli for every fixed lap

Fix positive integers $(q,\ell)$ and a fixed radius $R$. A nonzero admissible dual vector of norm at most $R$ has
\[
 |v|\le Rm,\quad |u+\alpha v|\le Rm/\sqrt L,\quad qu+\ell v=jm .
\]
Here $|j|=O_{R,q,\ell}(1)$ independently of $m,X$. If $j=0$, a nonzero vector has $|u+\alpha v|\ge c_{q,\ell}>0$ since it is a nonzero integral multiple of a fixed primitive vector and $\alpha$ is irrational. For $m\le2K=o(\sqrt L)$ this is impossible. Otherwise
\[
           |v-jm/(\ell-q\alpha)|\le C_{R,q,\ell} K/\sqrt L.            \tag{5}
\]
For each eligible nonzero $j$, its coefficient of $m$ here is irrational. The fraction of $K\le m\le2K$ satisfying (5) tends to zero by equidistribution of irrational multiples modulo one. One can first replace the shrinking tolerance by any fixed positive tolerance, pass to the interval limit and then shrink it. There are only finitely many $j$ at the fixed radius. Thus the shortest nonzero vector of the restricted lattice tends to infinity in modulus probability. Apply the packing estimate and truncate the discrepancy by its probability bound one. The average bounded-component discrepancy tends to zero. Finite-component truncation gives its full unnormalized version.

For the all-lap deterministic choice at $K=\lfloor L^{1/3}\rfloor$, one may replace $\sqrt L$ in the score by the integer $N=\max(1,\lfloor\sqrt{\lfloor\log_2(2X)\rfloor}\rfloor)$, comparable to $\sqrt L$. To avoid real comparisons choose $K=\max(1,\lfloor\lfloor\log_2(2X)\rfloor^{1/3}\rfloor)$ in this example, an immaterial fixed rescaling. For $m\in[K,2K]$ give one point for each successive integer $r=1,\ldots,\lfloor\log_2(2+N)\rfloor$ until the first failed test. At test $r$ require that for all $1\le q\le\ell\le r$ there is no nonzero integer pair $(u,v)$ with
\[
   qu+\ell v\equiv0\bmod m,\quad |v|\le rm,\quad
         N|u+\widetilde\alpha v|\le rm+1 .
\]
Use a rational approximation $|\widetilde\alpha-\alpha|\le [10N(2K)^2(1+\lfloor\log_2(2+N)\rfloor)]^{-1}$. Each search is finite by its displayed inequalities. Select the least modulus of largest score. For every fixed $r$, (5) excludes the enlarged forbidden region for a density-one set of moduli, simultaneously for the finite list of laps. Hence the best score tends to infinity. For every fixed actual lap its exact restricted shortest-vector norm tends to infinity at this selected modulus, by the rational error margin and $N\asymp\sqrt L$. This proves the claimed graph-independent selection.

## Every fixed positive quarter-scale constant detects escape

Let $m\ge cL^{1/4}$, and choose $b_0>0$ small so that $|\widehat H(b)|\ge3/4$ whenever $|b|\le b_0$ for *every* possible first-hit $H$ in (3). Its common bounded support diameter suffices by centering the phase. We can take $b_0<1/10$. Pigeonholing irrational multiples gives integers $1\le v\le b_0m$ and $u$ satisfying
\[
       |u+\alpha v|\le 2/(b_0m),\qquad
       \sqrt L\,|u+\alpha v|/m\le 2/(b_0 c^2).
\]
The resulting character of the full clock group is nontrivial. Its chosen lift in (4) therefore contributes modulus at least a fixed $\eta_0(c,\Phi)>0$, because the Fourier transform of the Gaussian is strictly positive on compact intervals. All **other** lifts have combined amplitude $o(1)$ as $X\to\infty$, uniformly over these choices at this fixed target. Indeed for each fixed $k\ne0$, replacing $v$ by $v+mk$ makes the distance of $(u+\alpha v)/m+\alpha k$ from the integers tend to $\|\alpha k\|>0$. The Gaussian sum over all $h$ then vanishes. At $k=0$ the other $h$ likewise vanish. Uniformly in the shift, every periodized Gaussian on the integer $h$-grid has bounded sum for $L\ge1$. The Schwartz tail in $k$ from $|\widehat H(k+v/m)|$ completes the argument. Conditional TV is at least half the modulus of this nontrivial character coefficient.

In a fixed escaping component first choose a waypoint whose basin misses less than $\eta_0/8$ of the component mass. The uniform support-diameter bound makes $\eta_0$ valid at this waypoint too. Its coordinates undergo only a common translation in the actual full group. Other sources cost at most their conditional probability. This proves a positive $\eta(c,\Phi)$ independent of the component. In the larger range $m/L^{1/4}\to\infty$, almost all sources in a fixed escaping component lie in $O_B(\sqrt L)$ clock pairs, after the same fixed-waypoint truncation and then increasing the Gaussian cutoff $B$. Their conditional uniform mass is $O_B(\sqrt L/m^2)=o(1)$. This is the support result already proved in PR215. It completes (1) and the critical lower estimate. Replacing the actual component marginal by its natural limit changes TV by $o(1)$.

For the range assertion about (2), take continued-fraction denominators $Q_n$ of $\alpha$ and choose constants $0<\theta<1/4$ and $1<d<1/(2\theta)-1$. Take $m=\lfloor Q_n^{1/d}\rfloor$ and $L=m^{1/\theta}$, up to rounding $X=e^L$ to an integer. For each fixed $R$, eventually $Rm<Q_n$, so for $0<|v|\le Rm$ the best-approximation property gives $\|v\alpha\|\ge\|Q_{n-1}\alpha\|>1/(2Q_n)$. Hence $\sqrt L/(2mQ_n)\to\infty$. The case $v=0$ is immediate. This proves (2) on these scales. With the additional homogeneous lower bound $\|v\alpha\|\gg_\epsilon |v|^{-2-\epsilon}$ the same argument gives all-scale sufficiency whenever $m\le L^{1/6-\epsilon'}$, taking the irrationality loss sufficiently small in terms of $\epsilon'$. [Chudnovsky, October 2026 preprint, Theorem 11.1, and independent scope audit at PR215](https://github.com/GettysburgResearch/collatz/blob/121054cf6569859585ede5c2d6e024eb2d97bbc5/research/astra-nine-hour-20261128/phase6/RECENT_LOGARITHM_INPUT.md)

## A finite implementation and the remaining upper bound

The definition using actual components can be replaced by a finite experiment. In the common-exit classifier, retain the true odd and shortcut counts to the output integer as well as its tag. On an exit use the full group $(\mathbb Z/m)^2$. On a detected cycle use the quotient by its observed primitive lap. On an unresolved singleton one may assign any class in the full group. Conditional on one good piece in each true component these classes agree up to a common translation with the true ones at **every** modulus. Indeed a nonperiodic source cannot visit the same exit twice; at a cycle any extra complete laps disappear in the quotient. The result holds when the tracked path to the output starts with the actual path to the observed minimum and then continues from that minimum. The classifier's wrongly typed and split-off mass is $o(1)$, uniformly with respect to $m$. For a measure of mass $p$ on a finite group the discrepancy is $\frac12\|\mu-p\,{\rm Unif}\|_1$, which changes by at most the sum-norm of a perturbation. Removing and reinserting the exceptional sources on both sides changes the joint discrepancy by $o(1)$. A smooth source in a compact proportional range inherits the classifier's ordinary $o(1)$ count by bounded comparison to the corresponding prefix. This supplies a computable finite statistic for integer cutoffs using a computable smooth source, finite arithmetic and a diverging computable exit cap. It does not give an effective convergence rate. [Finite common-exit classifier, true meetings and type error](FINITE_COMPONENT_PARTITION.md)

The middle-band mixing upper across **all** components would yield $p_{\rm esc}=0$. The row-resolved small-scale mark estimate allows arbitrary exact clock weights, but requires cancellation as a function of the real mark inside each row. A quotient character is constant there. It therefore does not supply this upper. At the critical moduli the near-resonant character exhibited above is carried by the same source row and has a positive limiting Gaussian multiplier on escape.

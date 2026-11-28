# Dependent gap codes at their real and ternary scales

Let $P$ be any stationary ergodic law on sequences of positive integer gaps $(e_j)_{j\ge1}$ with finite mean $a$. Write $h$ for its entropy rate in natural logarithms, $S_j=e_1+\cdots+e_j$, and
$$
 X=\sum_{j\ge1}3^{j-1}2^{-S_j}\quad\text{in }\mathbb Z_3^\times,
 \qquad \alpha=\log_2 3,\qquad \Delta=a\log2-\log3 .
$$
The ternary series converges for every sequence. Its legal inverse update before the next gap is $I_e(x)=(2^e x-1)/3$. Write $\nu$ for its distribution. Its lower and upper local dimensions satisfy, at $\nu$-almost every point,
$$
 \frac{(h-\max(\Delta,0))_+}{\log3}
    \ \le\ \underline d_\nu(x)\le\overline d_\nu(x)
    \ \le\ \min\{1,h/\log3\}.                                  \tag{1}
$$
In particular every stationary ergodic gap code with $a\le\alpha$ has an exact-dimensional ternary source of dimension $h/\log3$. The source residues retain the entire symbolic entropy rate in that range, including equality of the drifts. No independence or finite-order Markov assumption is needed.

If $a>\alpha$, evaluate the same series in $\mathbb R$ and call its value $R$. It is finite almost surely. The joint distribution $\zeta$ of $(X,R)$ obeys
$$
 \lim_{n\to\infty}-\frac1n\log\zeta\!\left((x+3^n\mathbb Z_3)
         \times[r-e^{-\Delta n},r+e^{-\Delta n}]\right)=h
    \quad\text{for }\zeta\text{-almost every }(x,r).                  \tag{2}
$$
Equivalently let $c=\min(\log3,\Delta)>0$. On the product use the metric
$$
 d((x,r),(y,s))=\max\{|x-y|_3^{c/\log3},\ |r-s|^{c/\Delta}\}.
$$
Both powers are at most one. The joint distribution is exact-dimensional of dimension $h/c$ in this metric, with precisely the scaling in (2). The positive part in (1) is the possible cost of forgetting the real coordinate.

## 1. Exact integer fibers

For a positive word $w$ of length $n$, total $S=S_n$, set
$$
 C(w)=\sum_{j=1}^n3^{j-1}2^{S-S_j}.
$$
On an infinite code with prefix $w$, $2^SX\equiv C(w)\pmod{3^n}$. The pair $(S,C(w))$ determines the entire word. Indeed $C(w)=2^{e_n}C(w^-)+3^{n-1}$ for $n\ge2$, where $C(w^-)$ is odd. Taking $v_2$ after subtracting $3^{n-1}$ determines $e_n$ and then $C(w^-)$. At length one $C=1$ and the remaining total gives $e_1$. In a fixed ternary cylinder and at fixed total $S$, the admissible integers $C$ thus lie in a single progression with spacing $3^n$, without repeated words.

By Birkhoff, $S_n/n\to a$ and
$$
 \max_{j\le n}|S_j-aj|=o(n)\quad P\text{-almost surely}.
$$
Consequently
$$
 \log C(w)\le n\max(a\log2,\log3)+o(n)                       \tag{3}
$$
on typical prefixes: bound each summand by the largest of
$(j-1)\log3+(S_n-S_j)\log2$, and pay $\log n$. At fixed $S$ the number of such prefixes in a given ternary cylinder is at most $1+\exp[n\max(\Delta,0)+o(n)]$. There are $O(n)$ possible totals on each uniform typical set. This is a fiber bound, not an estimate for a particular deterministic orbit.

## 2. Typical information, including countably many gaps

The one-letter Shannon entropy is finite because a geometric law maximizes entropy at prescribed positive mean. The stationary ergodic Shannon–McMillan–Breiman theorem for a countable alphabet of finite one-letter entropy gives $-n^{-1}\log P([w])\to h$ almost surely. [Chung, *A note on the ergodic theorem of information theory*, Annals of Mathematical Statistics 32 (1961), pp. 612–614](https://doi.org/10.1214/aoms/1177705069).

Fix $\varepsilon>0$. Take an increasing sequence of measurable typical sets $G_N$ exhausting full probability, with uniform bounds for every $n\ge N$:
$$
 |S_n-an|\le\varepsilon n,\qquad
 \max_{j\le n}|S_j-aj|\le\varepsilon n,\qquad
 e^{-(h+\varepsilon)n}\le P([w])\le e^{-(h-\varepsilon)n}.
$$
For the joint argument include a uniform bound on the real tail as in Section 3. Constants multiplying $\varepsilon$ below may depend on $a$; all disappear when $\varepsilon\downarrow0$.

The projection of $P|_{G_N}$ places at most $\exp[-(h-\max(\Delta,0)-O(\varepsilon))n]$ in each ternary cylinder of depth $n$ by (3) and the fiber count. Uniform small-ball bounds for an exhaustion imply the corresponding lower local dimension almost surely for the entire measure. One justification is the mass distribution principle on each restricted measure: every set of positive measure intersects one exhaustion piece in positive measure, and therefore has at least that Hausdorff dimension. The essential infimum of the lower local dimension equals this lower Hausdorff dimension. Equivalently, if some positive set has arbitrarily small balls with mass above a smaller dimension threshold, the disjoint $5r$ covering argument produces a positive-measure subset with Hausdorff dimension below the bound.

Conversely all codes with the same length-$n$ word belong to the same ternary cylinder. Thus the mass at the actual source cylinder is at least $P([w])$, giving the upper local bound $h/\log3$. The upper local dimension is also at most one almost surely: on the depth-$n$ partition the total probability of cells of mass below $3^{-(1+\varepsilon)n}$ is at most $3^{-\varepsilon n}$, which is summable. This proves (1). For $a\le\alpha$, the corresponding Shannon entropy of the $n$-trit observation divided by $n$ tends to $h$. The upper inequality follows because the observation is a function of the $n$ gaps. The lower one follows by Fatou applied to the nonnegative normalized pointwise information.

## 3. Simultaneous real localization

Suppose $\Delta>0$. For $T$ the shift of the gap sequence, Birkhoff gives $R<\infty$ and $\log^+ R(T^n\omega)=o(n)$ almost surely. For the latter statement write $S_j=aj+r_j$ with $r_j=o(j)$. For any small $\eta>0$ and all large $n$ the $m$th real summand at $T^n\omega$ is at most a constant times
$$
 \exp(2\eta n\log2)\exp[-(\Delta-\eta\log2)m] ;
$$
sum the geometric series and then take $\eta\downarrow0$. Enlarge the requirements on $G_N$ to include $R(T^n\omega)\le e^{\varepsilon n}$ for $n\ge N$.

The exact real identity $2^S R=C(w)+3^n R(T^n\omega)$ now controls the integer fibers of a joint rectangle. At fixed typical $S$ and any rectangle in (2) with arbitrary center, its real interval and the bound on $R(T^n\omega)$ confine $C(w)$ to an interval of length at most
$$
 2^{S+1}e^{-\Delta n}+3^n e^{\varepsilon n}
       \le 3^n\exp[O(\varepsilon)n+O(1)] .
$$
The ternary cylinder fixes $C(w)\bmod3^n$. Thus the number of typical words in that rectangle, summing also over the $O(n)$ totals, is $\exp[O(\varepsilon)n+O(\log n)]$. Its restricted mass is at most $\exp[-(h-O(\varepsilon))n+O(\log n)]$. Apply the same exhaustion argument now in the displayed product metric to obtain the lower almost-sure local dimension $h/c$.

For the upper local dimension choose a typical $\omega\in G_N$ such that the conditional probabilities of $G_N$ in its own successive symbolic prefix cylinders tend to one. This holds for $P$-almost all of $G_N$ by the elementary martingale differentiation theorem on the increasing countable prefix partitions. For all sufficiently large $n$, the restricted prefix has probability at least $P([w])/2$. Every one of its codes has the same ternary $n$-trit cylinder and the same real prefix $2^{-S}C(w)$, with real tail at most $3^n2^{-S}e^{\varepsilon n}\le\exp[-(\Delta-O(\varepsilon))n]$. Relative to the actual center, this changes only a constant factor in the radius. Its joint ball of radius $\exp[-(c-O(\varepsilon))n]$ therefore has mass at least $\tfrac12 e^{-(h+\varepsilon)n}$. Consecutive radii have bounded ratios, so interpolation gives the upper bound at every radius. Exhaust over $N$, then let $\varepsilon\downarrow0$. This proves (2).

## 4. Stitching preserves the one-edge law and recovers the word

Let $K(de\mid x)$ be the conditional law of the next gap at the exact ternary state. The single-edge occupation of the original process determines $K$ and its stationary marginal $\nu$. Run the stationary Markov chain on $U$ with this kernel and the actual update $x'=I_e(x)$. Both its mean gap $a$ and its one-step branching entropy $B=H(e\mid x)$ are unchanged.

This chain is ergodic whenever the original law is ergodic. Indeed, for a shift-invariant future event $A$ of the Markov path, $f(X_n)$, with $f(x)=\Pr(A\mid X_0=x)$, is the conditional expectation of $1_A$ given the history through $X_n$ (before drawing its action). It tends to $1_A$ by martingale convergence. Stationarity makes its squared norm constant, so all its martingale differences vanish. It follows that $1_A=f(X_0)=f(X_1)$ almost surely. Every such state event is invariant also along the original path, since the state-edge law is the same; the original ergodicity makes its probability zero or one. For a two-sided stationary extension, invariant events are future-measurable modulo null sets by approximating by finite-window events and shifting.

The gap word of this chain still determines its ternary state by the contracting ternary series. Let $h_K$ be the entropy rate of its stationary gap process. By the Markov property and the deterministic state transition,
$$
 n B=H_K(e_1,\ldots,e_n\mid X_0)
 \le H_K(e_1,\ldots,e_n)-H_\nu(X_0\bmod3^n).
$$
Apply the already proved lower bound (1) to the stitched ergodic gap process. Fatou's lemma for its almost-sure normalized local information gives the corresponding lower bound on normalized residue entropy. Subtracting from $h_K$, also allowing the trivial $B\le h_K$ if $h_K<\max(\Delta,0)$, gives the explicit estimate
$$
                     H_P(e_1\mid X)\le( a\log 2-\log3)_+.          \tag{4}
$$
If $a\le\alpha$, the first gap is a measurable function of the exact $3$-adic source alone. The same one-step identity holds at every subsequent shift on one event of full probability, so applying the actual inverse update reads the **entire** gap sequence from $X$. The function may depend on the stationary law. This argument also covers non-Markov original processes.

For $a>\alpha$ stitch on the joint state $(X,R)$ instead, updating both coordinates by $I_e$. Its original ergodicity passes to the new chain by the same argument. On the stitched process the real coordinate is still the real gap series: in $R_0=2^{-S_n}C(w)+3^n2^{-S_n}R_n$ the multiplier tends to zero exponentially, and the stationary finite real random variables $R_n$ are tight. The remainder tends to zero in probability; since the series converges almost surely the two limits agree. The analogous ternary identification is deterministic.

The exact joint state leaves only sublinear conditional word entropy on this chain. On the typical sets of Section 3, every fixed joint point admits at most $\exp[O(\varepsilon)n+O(\log n)]$ length-$n$ prefixes. A complement of probability $p$ contributes at most $pn H_{\rm geom}(a/p)$ to the conditional word entropy, where $H_{\rm geom}(m)=m\log m-(m-1)\log(m-1)$ is the largest one-gap entropy at mean at most $m$. To see this, drop the state condition on the complement, use subadditivity in the $n$ coordinates and concavity of $H_{\rm geom}$; their summed conditional means are at most $na/p$. Include also an entropy cost of at most $\log 2$ for the event indicator. Letting $n\to\infty$, $p\downarrow0$ and then $\varepsilon\downarrow0$ gives $H_K(e_1,\ldots,e_n\mid X_0,R_0)=o(n)$. On the Markov realization the left side equals $nH_P(e_1\mid X,R)$. Thus the two contracting evaluations together determine the entire word almost surely at $a>\alpha$.

## 5. Ergodic source laws separate

If $P$ is as above with $a_P\le\alpha$ and $Q$ is **any distinct** stationary ergodic finite-mean gap law, then their ternary source measures are mutually singular. Also, if $P,Q$ both have mean greater than $\alpha$ and are distinct, their **joint real/ternary** source measures are mutually singular.

Here is the first assertion including the real-drift boundary $a_P=\alpha$. Write $\nu_P,\nu_Q$ for the ternary projections. If they are not singular, then for any $0<\lambda<1$ the Markovization of the edge-flow mixture $(1-\lambda)J_P+\lambda J_Q$ is ergodic. Every invariant state event from the Markov proof above is constant almost surely under each of the two original ergodic laws. Giving it different values would separate the source measures on disjoint sets. The mixture therefore has no nontrivial invariant event. Its conditional branching entropy is at most
$$
       [(1-\lambda)a_P\log2+\lambda a_Q\log2-\log3]_+=O(\lambda).
$$
Let $f(x)$ be the deterministic next gap of $P$. Decompose $\nu_Q=g\nu_P+\nu_s$, and work off a $\nu_P$-null set supporting $\nu_s$. If the $Q$-conditional probability of $e\ne f(x)$ has positive integral under $g\nu_P$, then already on some slice $g\le M$ this integral is $q>0$. Under the mixture the event has conditional probability at most $\lambda M/(1-\lambda)$. Its integrated probability on that slice is $\lambda q$. Data processing to the indicator of disagreement gives conditional entropy at least $\lambda q\log[(1-\lambda)/(\lambda M)]$, contradicting the $O(\lambda)$ bound. Hence all $Q$ mass absolutely continuous with respect to $\nu_P$ uses the same deterministic action.

The deterministic map $T_f(x)=I_{f(x)}(x)$ preserves $\nu_P$. It therefore sends $g\nu_P$ to an absolutely continuous measure of unchanged total mass. By stationarity of $Q$ this output is at most the whole absolutely continuous part of $\nu_Q$, whose mass is equal, so it is exactly $g\nu_P$. No part of the singular input can enter the absolutely continuous output. The event of lying in this shared component is consequently invariant along $Q$; ergodicity forces its mass to be one. Any $T_f$-invariant probability absolutely continuous with respect to the ergodic probability $\nu_P$ equals $\nu_P$, for instance by Birkhoff applied to a countable generating algebra. Thus the state laws agree and their common deterministic action recovers the same entire gap law, contrary to distinctness.

For the joint assertion, take any two overlapping joint laws, stitch their edge mixture on the product space, and use the same ergodicity argument. Its mean remains greater than $\alpha$, so its joint action entropy vanishes by Section 4. Both laws then run the same deterministic map. Distinct ergodic invariant probabilities of one measurable map are mutually singular.

## 6. Actual orbit and adaptive-policy scope

For an ordinary positive escaping Syracuse ray, the exponents are indexed forward by $x_{j+1}=(3x_j+1)/2^{e_j}$. To use (1), take a stationary limit of locally sampled gaps in the **inverse** order. The source in the resulting coding is the observed current ternary endpoint before moving successively into its past, since a length-$n$ past determines its current state modulo $3^n$. The telescoping real growth identity bounds the limiting mean gap by $\alpha$ on the whole empirical law of an escaping ray. This bound may hold only on average over ergodic components. Formula (1) applies with the actual mean and entropy of each individual component; it proves exact dimensionality for every component satisfying $a\le\alpha$. It supplies neither the existence of an escaping ray nor positive symbolic entropy for one.

The same orientation works for limits of finite adaptive inverse controls. Their total entropy rate is at least $\log3$ if their means remain bounded, as detailed in the separate weak-marginal note. It need not be at least $\log3$ on every ergodic component. For an ergodic limit of mean $a$ this gives lower ternary dimension at least $[1-\max(\Delta,0)/\log3]_+$ and the sharper bound using its actual $h$ in (1). At the hypothetical critical mean $a_*$, the known entropy equality forces iid geometric gaps. Its full ternary dimension was already proved by Leen; (1) is weaker for that specific positive-real-contraction law.

## Primary comparisons

The fixed-total integer numerator argument is Tao's Lemma 6.2 and Weaver's paper 9, Lemma 3. Weaver's real localization theorem gives exact ternary dimension and coding recovery for a particular iid tilted law; Brofferio identifies the Poisson boundaries for iid walks on rational affine groups through the contracting completions. The joint real/ternary Collatz law and its product-metric behavior have also been studied for fair branches. Feng–Hu's conformal IFS theory expresses dimension in terms of projection entropy for general invariant measures. Here the exact integer progression estimate gives the full symbolic entropy in the noncontracting real regime for arbitrary dependent ergodic gaps, and gives the explicit Lyapunov-rectangle rate at positive real contraction. No identification of an iid Poisson boundary for dependent increments is needed. [Tao, *Almost all orbits of the Collatz map attain almost bounded values*, Lemma 6.2](https://arxiv.org/abs/1909.03562) · [Weaver, *Ternary Syracuse laws: real localization, clock stability, and critical regularity*](https://rstation.ai/problems/collatz/papers/9) · [Weaver, *Singularity, volume decay, and coding entropy of the joint Collatz affine law*](https://rstation.ai/problems/collatz/papers/19) · [Brofferio, *The Poisson boundary of random rational affinities*](https://numdam.org/articles/10.5802/aif.2191/) · [Feng and Hu, *Dimension theory of iterated function systems*](https://arxiv.org/abs/1002.2036).

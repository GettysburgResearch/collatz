# A compulsory logarithmic-height law for each physical escape atom

**Status.** Proposed actual-source theorem. Every escaping component has a probability law at logarithmic height even when its odd-time-normalized record flow vanishes. The numerical and coefficient record weights have finite total variation difference on the whole forward ray. The exact suspension identity controls the circle coordinate. Tightness on finite arithmetic labels and stationarity of the unweighted arithmetic edges require further hypotheses.

## OP-G5. A bounded total discrepancy on the entire ordinary ray

Use a simple ordinary odd trajectory $x_j$ in an escaping component, with $2^{e_j}x_{j+1}=3x_j+1$. Put $u_j=\log(3^j/2^{e_0+\cdots+e_{j-1}})$ and
$$
 d_j=\sum_{i<j}\log(1+1/(3x_i)),\qquad
 H_j=\max_{i\le j}\log(x_i/x_0),\qquad
 K_j=\max_{i\le j}u_i .
$$
Then $d_j$ increases to a finite $d_\infty$ by the simple-trajectory reciprocal bound, and $\log(x_j/x_0)=u_j+d_j$. In particular $H_j$ and $K_j$ tend to infinity. For all $j$ one has
$$
 0\le H_j-K_j\le d_j,\qquad
       (H_j-K_j)_{j\ge0}\ \text{is nondecreasing}.
$$
When $u_j$ sets a new record, $u_j+d_j$ also sets one and $H_j-K_j=d_j$. At an index without a new coefficient record $K$ is constant and $H$ is nondecreasing. Thus for increments from index $j-1$ to $j$,
$$
   \Delta H_j\ge\Delta K_j\ge0,\qquad
   \sum_{j\ge1}|\Delta H_j-\Delta K_j|=d_\infty .
$$
Equality on the right follows because there are cofinally many coefficient records. For **any** marking $m_j$ of odd vertices in any measurable space, the finite measures $\sum_{j\le N}\Delta H_j\,\delta_{m_j}$ and $\sum_{j\le N}\Delta K_j\,\delta_{m_j}$ therefore differ in total variation by at most $d_\infty$, uniformly in $N$. In particular all extra numerical records together receive only finite total logarithmic width.

Beyond the finite initial prefix the actual strict native maxima are $y=(3p+1)/2$ at strict odd-height records $p$. This includes any odd native maximum: if it is not the initial value it must itself be the first successor of an earlier odd record, since later even divisions from a preceding odd successor only decrease it. In successive increasing $p$ the correction $\log(y/p)=\log(3/2)+\log(1+1/(3p))$ is monotone with bounded total variation. The logarithmic interval of real thresholds $t$ having first exit exactly $y_i$ from the fixed ray consequently has width $\Delta H_i$ up to a sequence of corrections with finite absolute sum. Real thresholds here mean the integer rule at $X=\lceil t\rceil$, so $(y_{\rm prev},y]$ is exactly the interval selecting the next record $y$.

For each component the log-height average of its pre-gate markings is thus asymptotically, in total variation, the probability law on **true coefficient records**, weighting each marked terminal phase by the exact ladder overshoot. More explicitly let $r_l$ be coefficient record indices with $r_0=0$, and $w_l$ the complete gap block from $r_l$ to $r_{l+1}$. Its length $m_l$ and clock $s_l=\lfloor m_l\log_2 3\rfloor$ give
$$
 a_l=K_{r_{l+1}}-K_{r_l}=\log(3^{m_l}/2^{s_l})\in(0,\log(3/2)] .
$$
The sum $A_n=\sum_{l<n}a_l$ diverges. The error between normalized log-threshold occupancy through a large gate height and $A_n^{-1}\sum_{l<n}a_l\delta_{m_{r_{l+1}}}$ tends to zero. The final partial interval costs at most a constant before normalization. [The physical first-exit approximation](EXIT_GATES.md) further shows that the actual gate mass average, weighted by $dt/t$, equals the sum of these componentwise distributions with weights $Z_D(s)$ up to $o(1)$ in total variation. Indeed the $\ell^1$ error at each integer threshold tends to zero and is uniformly bounded. Average that error and use dominated convergence for the component sum $\sum_DZ_D(s)\le\zeta(s)$, with arbitrary componentwise initial cutoffs absorbed in the limit. The statement about distributions means agreement at the same growing height horizon; no unique joint weak limit is presumed.

## OP-G6. The compulsory suspension identity and its arithmetic boundary

At a record let $Q_l$ consist of the dyadic and ternary addresses of $x_{r_l}$ and the circle phase $\phi_l=[\log L(x_{r_l})]\in\mathbb R/(\log2)\mathbb Z$, with $L(x)=x\prod_{i\ge0}(1+1/(3T_{\rm odd}^i x))$ on this component. The phase differs from the actual logarithmic phase by $o(1)$. Its exact edge law is $\phi_{l+1}=\phi_l+a_l$ on the circle. Retain both the discrete label $w_l$ and its real roof $a_l$. Compactify the countable discrete alphabet of complete blocks by one additional point $\infty$, and take any weak subsequential limit of the probability measures
$$
 \rho_n=\frac1{A_n}\sum_{l<n}a_l\,
              \delta_{(Q_l,w_l,a_l,Q_{l+1})}.
$$
Such limits always exist. At finite labels the original edge arithmetic and the indicated positive roof persist. At $\infty$, large label length is possible, and its roof coordinate can take a limit in $[0,\log(3/2)]$.

For continuous periodic $f$ put $B_af(\phi')=a^{-1}\int_0^a f(\phi'-v)\,dv$ for $a>0$ and $B_0 f(\phi')=f(\phi')$. Then every such probability obeys
$$
 \int B_a f(\phi')\,d\rho
 =\frac1{\log2}\int_0^{\log2}f(t)\,dt .
$$
Indeed the intervals from $\phi_l$ to $\phi_{l+1}$ tiled by their increasing lifts have consecutive lengths $a_l$. Their total length is $A_n\to\infty$, so averaging $f$ over that single real interval gives the normalized circle integral. The continuous extension at zero justifies passage to the weak limit. More generally for a continuous test $F$ on arithmetic vertices, whenever its edge difference divided by $a$ has a bounded continuous extension to the limiting edge space, its integral vanishes: before passage to the limit its numerator telescopes to $F(Q_n)-F(Q_0)$. Ordinary unrestricted vertex tests need not satisfy that division condition.

If $w_l\to\infty$ along a sequence of such physical edges, every limit of its starting dyadic phase has no finite coefficient upcrossing; otherwise a finite native parity cylinder would force a bounded first-ladder length. Every terminal ternary limit bears a critical backwards odd script. More precisely if $a_l\to a$, each nonempty inverse-prefix multiplier along a limiting script is at most $e^{-a}$. Before the full block boundary every such multiplier is strictly smaller than that of the complete reverse block, namely $e^{-a_l}$. Finite available clock sets at each depth allow extraction and passage to the limit. Thus the added boundary has specified arithmetic restrictions.

A sufficient extra condition for an ordinary **finite stationary edge law** at this normalization is
$$
 \lim_{M\to\infty}\limsup_{i\to\infty}
 \frac1{A_{n_i}}\#\{l<n_i:m_l>M\}=0 .
$$
Indeed on any finite set of labels every roof has a positive minimum. Dividing the restricted measures $\rho_{n_i}$ by $a$ is safe there, and the displayed condition gives uniformly small unweighted tails. The unweighted laws $A_{n_i}^{-1}\sum_{l<n_i}\delta_{(Q_l,w_l,a_l,Q_{l+1})}$ then have a finite weak limit $\pi$, with equal two vertex marginals by telescoping and $\rho=a\pi$. Its total mass is at least $1/\log(3/2)$, so it can be normalized. A finite mean **odd block length** for that normalized law would require additional control if one wishes to use finite-mean entropy formulas. Finite roof alone places no upper bound on that mean.

The compulsory law supplies neither the tail condition nor unconditional equality of the vertex marginals of $\rho$ itself. For a two-edge alternating cycle with unequal positive roofs, the outgoing and incoming roof-weighted masses at either vertex differ even though the unweighted edge sequence is stationary. Within the actual ladder alphabet, the explicit symbolic example at the end of [Theorem E](../renewal/ESCAPE_OF_MASS.md) has all lengths tending to infinity, roofs bounded above and below, paired local limit $(1,-1)$ and coefficient tending to infinity. Its mandatory log-height probability puts all label mass at $\infty$ and satisfies the same circle suspension identity. The unique dyadic seed there is proved irrational. Thus any proof of zero physical flux through the mandatory occupation needs another arithmetic input specific to a single positive ordinary source. The compact suspension and its normalized mass do not provide it.

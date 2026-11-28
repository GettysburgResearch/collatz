# Original donor mass and recrossings after the attained minimum

**Source-qualified written theorem.** Use the ordinary odd map $U$, survival factors $w_x=3x/(3x+1)$, $b_j(x)=\prod_{i<j}w_{U^ix}$, $F(x)=\lim b_j(x)$, $a_y=h(y)/y$, $D=\log(4/3)$, $a=\log(3/2)$ and $\kappa=D/2$. The weighted first-hit law, complete-cycle factors, natural minimum and ordinary component fluxes are the pinned [stationary inputs](SPATIAL_TRACE_TAIL.md). Distinct positive path segments have a uniform reciprocal tail above every growing floor. For a true odd source $x$ let $m(x)=\min_{j\ge0}U^jx$ and $\tau(x)=\min\{j:U^jx=m(x)\}$. Both are finite even on an escaping orbit. For each odd $m$ define the original charges
\[
 \gamma_m=\kappa\langle b_{\tau(x)}(x)1_{m(x)=m}\rangle,\qquad
 \eta_m=\gamma_m F(m)=\kappa\langle F(x)1_{m(x)=m}\rangle.           \tag{1}
\]
Brackets use the ordinary relative odd natural mean, or its equal logarithmic mean here. For each real $B\ge1$ put $N_m^+(B)=\#\{j: U^jm\le B<U^{j+1}m\}$ and $N_m^-(B)=\#\{j:U^{j+1}m\le B<U^jm\}$. Use these unweighted counts only at escaping $m$ of positive charge. Each is finite there. Let $Q(B)=\sum_{y\le B<Uy}w_ya_y$ denote the raw outward shell and set
\[
                        Q_{\rm post}(B)=\sum_{m:\eta_m>0}\eta_m N_m^+(B).
\]
This latter quantity retains the *complete escaping survival weight* and all visits after the first global minimum. No site or trajectory count is clipped.

The total escaping charge is $H=\sum_m\eta_m$, and $\sum_{m>M}\gamma_m\ll M^{-\sigma}$ with the positive absolute minimum exponent of [PR213](https://github.com/GettysburgResearch/collatz/blob/5ac2b4a7ab9fee19d2e1b1c2e4aadecd08413128/research/astra-diagonal-frontier-20261127/mass/PREDECESSOR_MINIMUM_POWER.md). The exact level balance is
\[
    Q_{\rm post}(B)=\sum_{m\le B}\eta_m+
                        \sum_{m:\eta_m>0}\eta_m N_m^-(B).             \tag{2}
\]
If there is at least one escaping component, then
\[
  \limsup_{B\to\infty} Q(B)\ \ge\ \frac{\log(3/2)}4+H+\max_C H_C.   \tag{3}
\]
In fact the right side, up to $o(1)$, is a lower bound throughout arbitrarily high intervals of a fixed positive proportional width. A component of zero upper exponential speed forces the logarithmic mean of the raw shell to tend to infinity. Regular positive speed instead gives an exact logarithmically averaged crossing cost for each fixed donor, below.

## Exact decomposition on original trajectories

For fixed $m$, the reached-minimum event is empty unless $m$ has no strictly smaller future state. When it qualifies, the event is precisely that the first landing at floor $m$ equals $m$. To verify the weighted mean in (1), fix $R>m$. A source reaching $m$ first lands at $Y_R$. Everything up to its first $m$ after that entrance is a bounded deterministic test of the physical lower label, including the weight of that subpath and the requirement of no earlier state $\le m$. Earlier departed states exceed $R$ and are distinct, so the first-arrival survival into $Y_R$ differs uniformly from one by $o_R(1)$. A missing landing contributes zero. The grid law of $Y_R$ has an ordinary natural limit. Thus the upper and lower source limits of the weighted test differ by $o_R(1)$, proving existence as $R\to\infty$. Boundedness by the minimum probability and finite addition give the stated tail bound. Since the entire postminimum path is the true path of $m$, $F(x)=b_{\tau(x)}(x)F(m)$ on that event. Tightness of the minimum law identifies $\sum_m\eta_m$ with $H$ and, within each escaping component $C$, $\sum_{m\in C}\eta_m=H_C$.

The true raw identity at every finite floor is
\[
\begin{split}
 Q(B)={}&Q_{\rm pre}(B)+
   \sum_{m\le B}\gamma_m\sum_{k\ge0} b_{k+1}(m)
             1_{\{U^km\le B<U^{k+1}m\}},\qquad\text{where}\\
 Q_{\rm pre}(B)={}&\kappa\left\langle
     \sum_{j<\tau(x)}b_{j+1}(x)1_{\{U^jx\le B<U^{j+1}x\}}\right\rangle .
                                                                         \tag{4}
\end{split}
\]
At each one of the finitely many outward departing sites, its weighted first arrival times $w_y$ gives its entire occupation if nonperiodic. If periodic, multiply by the converging geometric series of full-lap survivals. This is exactly the full stationary $w_ya_y$. Sum over sites and split the ordinary-source occupation at the first minimum. The remaining discounted sum is fixed given $m$ and is finite even if the subsequent orbit cycles, by the same lap factor. If $m>B$ it cannot contain a departing site through $B$. Thus this is a finite sum of averaged terms and also proves the existence of the preminimum mean by subtraction. It follows that $Q(B)\ge Q_{\rm pre}(B)+Q_{\rm post}(B)$. The early lower-passage count used in [the preminimum crossing law](PREMINIMUM_RECROSSINGS.md) counts only edges before the first global minimum, giving $\liminf Q_{\rm pre}(B)\ge a/4$ by that same proof.

For an escaping $m$ with positive charge, no state of its future falls below $m$. For a floor $B\ge m$ its indicator of being strictly above $B$ starts at zero and eventually stays one. The finite net count is therefore $N_m^+(B)-N_m^-(B)=1$. For $B<m$ both counts vanish. Weighting gives (2). The integrals below use ordinary Lebesgue measure in the logarithm of the real floor, so endpoint choices cost zero there.

## A second original crossing across proportional intervals

Fix an escaping component $C$ and a reference ray in it. Its arbitrary finite set of positive-charge minimum donors all merge with this ray by a finite index. There are infinitely many ray departures $z$ with $v_2(3z+1)\ge2$. Otherwise the remaining exponent-one run would make $z_0+1$ divisible by $2^k$ for every $k$, by $U^kz_0+1=3^k(z_0+1)/2^k$ on that run. At a sufficiently late such departure $Uz\le(3z+1)/4<4z/5$. Every $B\in[4z/5,9z/10]$ has a postminimum downcrossing on every retained donor's true path, and eventually exceeds all those minima. Consequently the second term of (2) on this entire interval is at least the sum of their charges. Exhaust the donors in $C$, use $\sum_{m\le B}\eta_m=H+o(1)$ and the lower preminimum contribution. This proves (3), including uniformity over the displayed intervals along an increasing subsequence. A summable positive family $(H_C)$ with positive total has a largest member. No coincidence between downward intervals from distinct components is assumed.

## The earliest postminimum original flux

Let $Q_{\rm early}(B,J)$ be the second term of (4) with $0\le k<J$. This includes all original fates and keeps the ordinary discounted weights into their crossed edges. If $J\le (1-\epsilon)\log B/a$, then
\[
                   Q_{\rm early}(B,J)\ll_\epsilon (1+J)B^{-\epsilon\sigma}. \tag{5}
\]
Indeed $U^{k+1}m+1\le(3/2)^{k+1}(m+1)$ implies $m+1>(B+1)e^{-aJ}$, and each retained donor can pay at most $J$ times. Here and below a nonintegral date bound means its floor.

For every fixed $K,A>0$, the same *uncapped* quantity is $O_{K,A}((1+\log B)^{-A})$ for
\[
                    J=\left\lfloor\frac{\log B+K\log\log B}{a}\right\rfloor
\]
at large $B$. Indeed select $L>(A+2)/\sigma$ and discard all donors $m>(\log B)^L$ at cost $O(J(\log B)^{-L\sigma})$. For the smaller donors, times $k+1<J/2$ cannot cross by elementary maximum growth. At the remaining dates, inequality (4) of [the finite propagation theorem](SMALL_REPRESENTATIVE_UPPER.md) bounds their height plus one by
\[
 C_b(1+m)e^{a(k+1)}
       \big[(1+\log(m+1))/(1+k+1)\big]^b .
\]
Take any fixed $b>K+L+2$ and then $B$ sufficiently large. This is strictly below $B$, proving the assertion. The arithmetic input for (4) is the fixed-arity Subspace Theorem for the ordinary source with its explicit height dependence.

Under the additional unrefereed Weaver Paper15/v2, Theorem 9 input in [the same proof](SMALL_REPRESENTATIVE_UPPER.md), there are absolute $c,c'>0$ for which $Q_{\rm early}(B,J)\ll\exp[-c'\ell\log(2+\ell)]$ when $\ell=\log\log B$ and $aJ\le\log B+c\ell\log(2+\ell)$. In fact discard donors $m>\exp[d\ell\log(2+\ell)]$ at cost $O(J\exp[-\sigma d\ell\log(2+\ell)])$. For the rest and dates comparable to $J\asymp\log B$ the positive growth saving is $\exp[-c_2(1+o(1))\ell\log(2+\ell)]$, since $\log[(1+k+1)/(1+\log(m+1))]\sim\ell$. Choose $c,d>0$ with $c+d<c_2/2$. Smaller dates follow by elementary growth or monotonicity of the date cutoff. This is an estimate for *all original postminimum donors at once*. Late recrossings of a low donor remain outside this upper bound.

## Logarithmic floor averages and speed

Write
\[
             I(R)=\int_1^R Q_{\rm post}(B)\,dB/B .
\]
Every $\eta_m>0$ has $m\ge3$. Each of its native odd edges starting at $z$ has logarithmic length at least $c_0=\min(a,\log(4/(3+1/3)))>0$: for exponent one its length is at least $a$, and for exponent at least two its downward length is at least the other constant. If $z\le R$, the entire edge between $z$ and $Uz$ lies in $[1,2R]$. Count absolute logarithmic lengths by integrating the upcrossing and downcrossing counts. The former dominates the latter level by level on this path, by (2)'s individual identity. Tonelli therefore gives
\[
    \sum_{m:\eta_m>0}\eta_m\,\#\{j:U^jm\le R\}
                       \le 2I(2R)/c_0 .                                \tag{6}
\]
In particular, if $I(R)=O(\log R)$ then every positive donor ray has logarithmic packing $\#\{j:U^jm\le R\}\ll_m\log(2R)$, and $\sum_j(U^jm)^{-s}<\infty$ for **all** $s>0$. On that ray the upper natural density of indices with $\log(U^jm)\le cj$ is $O_m(c)$ for $c>0$, since its count through $n$ is at most the packing count up to $e^{cn}$. A bounded logarithmic mean for the larger raw $Q$ implies all these statements. If a component instead has $\log(U^jm)/j\to0$, every fixed multiple of $\log R$ of its initial indices eventually lies below $R$. A positive minimum donor exists in that component and has the same speed by common-tail coalescence. Formula (6) then forces $I(R)/\log R\to\infty$, as well as divergence of the corresponding raw logarithmic mean.

For one fixed donor with $g=\lim_{j\to\infty}j^{-1}\log(U^jm)>0$, its individual upcrossing integral is governed by the frequency of exponent one. If that frequency has limit $p$, then
\[
          \frac1{\log R}\int_1^R N_m^+(B)\,\frac{dB}{B}
                        \longrightarrow \frac{ap}{g}.                  \tag{7}
\]
The analogous lower and upper limits use the lower and upper frequencies. On exponent-one edges the full length is $a+\log(1+1/(3U^jm))$, with summable correction by distinct-path packing. Given $0<\delta<1$, all indices $j\le(1-\delta)\log R/g$ eventually have both endpoints at most $R$, while every index $j>(1+\delta)\log R/g$ has its initial site above $R$, by the speed limit. Boundary indices cost $O(\delta\log R+1)$ and the integer cut $\lfloor\log R/g\rfloor$ runs through all sufficiently large integers. Let $\delta$ decrease to zero. If individual speeds and frequencies exist on several components, Fatou sums their lower contributions $H_C ap_C/g_C$; equality for the infinite original mixture would require uniform control of the transient multiplicities of its late-merging donors. The fixed-donor upper in (7) makes no such interchange.

Finally there is a strictly diverging secondary excess already in the postminimum integral if $H>0$. There is an absolute $c>0$ such that on the stated Paper15/v2 input
\[
          I(R)\ \ge\ H\log R+cH(\log\log R)\log\log\log R-O(1)        \tag{8}
\]
for all sufficiently large $R$. Without that input the elementary fixed-arity argument gives $(I(R)-H\log R)/\log\log R\to+\infty$ under the classical fixed-arity Subspace Theorem used above. To prove these bounds integrate (2). The first term differs from $H\log R$ by at most $\sum_m\eta_m\log m<\infty$ using its polynomial tail. Keep the donors $m\le\exp(\sqrt{\log R})$, whose total weight tends to $H$. For the first $n=\lfloor(\log R)/(2a)\rfloor$ odd steps both endpoints of every edge are at most $R$ by elementary maximal growth. Each exponent $e\ge2$ gives a downward length
\[
    e\log2-\log(3+1/z)\ge (e-1)\log(4/(3+1/3)).
\]
Thus the integrated downcrossings from these donors pay an absolute constant times $E=\sum_{i<n}(e_i-1)$. On this whole input range $\log[(1+n)/(1+\log(m+1))]\ge(1/2+o(1))\log\log R$. The ordinary defect lower preceding (5) in [the finite propagation proof](SMALL_REPRESENTATIVE_UPPER.md) gives $E\ge c\log\log R\log\log\log R-O(1)$ on Paper15/v2. Its fixed-arity block argument instead gives $E\ge K\log\log R$ for any chosen $K$ and all sufficiently large $R$ uniformly on the same donors. These are true escaping paths, so the stop at the known cycle never intervenes. Integrate, sum positive weights and use $H>0$. Valbuena's earlier divergent-excess result counts all visited sites up to a level and gives a strict first-order cumulative lower coefficient. Equations (2), (3) and (8) concern original weighted postminimum *outward edges* and pay for subsequent downward intervals separately. [Valbuena, pinned raw-occupation and divergent-excess theorems](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).

## Signed raw flux with killing on the actual departed vertex

Let $t_z=1-w_z$ and use $Q_{\rm pre}^{\pm}(B)$ and $Q_{\rm post,raw}^{\pm}(B)$ for the two terms of (4), using the indicated crossing direction. Thus the superscript $+$ reproduces (4); $Q_{\rm post,raw}^+$ differs from $Q_{\rm post}$ because (4) uses the full survival to each traversed edge, including on bounded trajectories. Define $K_m(B)=\sum_{j\ge0}b_j(m)t_{U^jm}1_{U^jm>B}$. Then
\[
 Q_{\rm post,raw}^+(B)-Q_{\rm post,raw}^-(B)
         =\sum_{m\le B}(\eta_m+\gamma_m K_m(B))\longrightarrow H.     \tag{9}
\]
This is a cancellation for the two *uncapped* actual directed occupations. If (9) is restricted to the original escaping donors on both sides, its difference from $H$ is $O(B^{-\sigma}+B^{-q})$, where $q>0$ is any uniform distinct-path reciprocal-tail exponent. Also
\[
       Q_{\rm pre}^+(B)-Q_{\rm pre}^-(B)
                    =-\kappa+O(B^{-\sigma}+B^{-q}).                    \tag{10}
\]
These statements allow either uncut direction to become large. The postminimum directions at fixed $B$ are finite, since $m\le B$ is necessary and successive visits to the finite low set are distinct or discounted by the fixed positive cycle's lap contraction. For preminimum arrivals from above, the total inward count on a simple path is at most one plus its outward count.

Write $z_j=U^jm$, $d_j=1_{z_j>B}$ and $b_j=b_j(m)$. The exact finite identity, valid from any source, is
\[
 \sum_{j<n}b_{j+1}(1_{z_j\le B<z_{j+1}}-1_{z_{j+1}\le B<z_j})
           =b_n d_n-d_0+\sum_{j<n}b_jt_{z_j}d_j.                     \tag{11}
\]
The summand on the left is $b_{j+1}(d_{j+1}-d_j)$ and $b_j-b_{j+1}=b_jt_{z_j}$, proving (11) by telescoping. From a true minimum $m\le B$ the initial indicator is zero. The terminal term tends to $F(m)$ on escape, since the orbit eventually stays above $B$. On every bounded fate $b_n\to0$. The complete unconditioned kill series sums to $1-F(m)\le1$ and its high tail $K_m(B)\to0$ at each fixed $m$ by dominated convergence on the dates. This gives (9) first donorwise, then by dominated convergence over the summable $\gamma_m$. For an escaping donor the orbit is distinct and $K_m(B)\le\sum_{z\in O(m),z>B}1/(3z+1)\ll B^{-q}$ uniformly. Together with the minimum-charge tail this gives the stated quantitative signed bound on escape.

For (10) apply (11) from an ordinary distant source $x>B$ stopped at its first minimum. Its terminal term vanishes unless $m(x)>B$, an original probability $O(B^{-\sigma})$. All departed sites on the preminimum segment are distinct, so its high-kill sum is uniformly $O(B^{-q})$. The initial term is $-1$, with the natural normalization $\kappa$. This proves (10), with no temporal truncation.

Already in Weaver Paper176/v1, Theorem 2, the total ordinary loss is $\sum_x t_xa_x=\kappa-H$. The finite-floor stationary net balance $Q^+(B)-Q^-(B)=-\sum_{x\le B}t_xa_x$ follows by summing the harmonic equation on the finite low set. Equations (9)–(10) separate this established limiting identity into its actual preminimum and postminimum directed fluxes. They do not give an independent lower bound $\sum_x t_xa_x\ge\kappa$. [Weaver, Theorem 2 and the full loss identity following (4)](https://rstation.ai/problems/collatz/papers/176/v1).

[PostminimumLevelBalance.lean](PostminimumLevelBalance.lean) proves (11) at every finite date on the factorization-defined native odd map, its low-to-high specialization, and the finite split of discounted outward occupation at any supplied date. Its hypotheses allow repeated states and returns. The natural source limits, growth estimates, and donor disintegration are the written arguments above.

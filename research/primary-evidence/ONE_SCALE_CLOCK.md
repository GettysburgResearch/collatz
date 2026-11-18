# Recovering the ordinary weighted trace and the numerical cone limit at one published passage scale

**PROPOSED.** Set $d=\log(4/3)$ and $\delta=d/2$. For the accelerated odd map $U$, use the normalized odd logarithmic mean
$$
 E_{\rm odd}(F)=\lim_{X\to\infty}\frac{2}{\log X}
                 \sum_{x\le X,\ x\text{ odd}}\frac{F(x)}x
$$
whenever the limit exists. The results below use Tao's printed scale $\alpha=1.001$, his Proposition 1.11, and the clock estimate in its proof. Together with our [reconstruction of every-depth convergence](FIXED_PRECISION.md) they give an alternative proof of the canonical ordinary weighted first-hit identity and of the [numerical two-scale limit](../critical-orbit-mellin/TWO_SCALE_TEST.md). Valbuena independently establishes the canonical identity, with a substantially larger collection of source laws and natural-density consequences. Here only odd logarithmic means are asserted. [Tao, Proposition 1.11 and (5.14)–(5.16)](https://doi.org/10.1017/fmp.2022.8) · [Valbuena](https://doi.org/10.5281/zenodo.23025885)

## A clock across a descending sequence of scales

Write $T_y(x)$ and $P_y(x)$ for time and location of the first odd visit to $[1,y]$. Represent failure by a cemetery state and make its later passages stay there. The passage locations compose exactly. Tao uses the default value one; replacing it by the cemetery changes the two laws compared in Proposition 1.11 by at most their separately bounded failure probabilities. Let $N_y$ have the normalized harmonic law on odd starts in $[y,y^\alpha]$. The printed estimate and the good event in (5.14)–(5.16) give, for $z$ large and $y=z^\alpha,z^{\alpha^2}$,
$$
 T_z(N_y)=\frac{\log N_y-\log z}{d}+O((\log z)^{3/5}) \tag{1}
$$
outside probability $O((\log z)^{-c})$. The total variation distance between the two corresponding $P_z$ laws is $O((\log z)^{-c})$. These errors and constants are uniform in $z$.

Fix a large $H$. For $X\ge H^\alpha$ take $X_i=X^{\alpha^{-i}}$ and the last index $J$ with $X_J\ge H$, so $H\le X_J<H^\alpha$. For $i\ge1$ the law of $P_{X_i}(N_X)$ differs in total variation from $P_{X_i}(N_{X_{i-1}})$ by at most $C(\log X_i)^{-c}$. Indeed the statement is exact at $i=1$. Apply the deterministic next passage, then compare the fresh starts at $X_{i-1}=X_{i+1}^{\alpha^2}$ and $X_i=X_{i+1}^\alpha$ using Proposition 1.11. The errors sum to the stated bound by geometric growth of $\log X_j$ going backwards from $i$.

For the fresh $N_{X_{i-1}}$, (1) applies to each of the two thresholds $X_i,X_{i+1}$. Subtract on their common good event. The elapsed time between these two passages differs from $(\log X_i-\log X_{i+1})/d$ by $O((\log X_i)^{3/5})$. The elapsed time is a deterministic function of the landing at $X_i$ when it exists. Assign infinity on either failure. The total variation estimate thus transfers this increment bound to the original $N_X$. Add (1) for its first crossing and sum the increments. The sum of errors in time is $O((\log X)^{3/5})$; the sum of exceptional probabilities is $O((\log H)^{-c})$. In particular,
$$
 T_{X_J}(N_X)=\frac{\log N_X-\log X_J}{d}+O((\log X)^{3/5})
 \tag{2}
$$
outside that exceptional probability, with constants independent of $H,X,J$. This controls a finite threshold between $H$ and $H^\alpha$ during each shell, so no convergence rate at a fixed small target was presumed.

For use in ordinary harmonic sums, cover odd starts up to $e^{CQ}$ by the disjoint logarithmic windows with endpoints $\exp(\alpha^j)$, truncating one endpoint if necessary. Repeated integer endpoints can be assigned to one interval and their total harmonic error is bounded. The total reciprocal weight of bad starts is $O_C(Q(\log H)^{-c})+O_H(1)$, by summing the full-window bounds. All relevant time errors in (2) are $o(Q)$ for fixed $H,C$. Thus, for any fixed $\epsilon>0$, on good starts with $\log x\le(d-\epsilon)Q$ the bounded-set landing occurs before $Q-c_\epsilon Q$ for large $Q$. On good starts with $\log x\ge(d+\epsilon)Q$ it occurs after $Q+c_\epsilon Q$.

## Actual harmonic weights at a fixed odd target

Let $s$ be a fixed positive odd integer. Define $W_s(x)$ to vanish when the orbit misses $s$, and otherwise to be $V_{\tau_s}(x)=\prod_{i<\tau_s}(1+1/(3U^i x))^{-1}$ up to its **first** visit to $s$. Let $b(s)=\lim_qg_q(s)$ in the probability normalization. The limit exists by the fixed-precision transfer and is finite by [the fixed-target bound](CONE_WITHOUT_OVERSAMPLING.md). Write $\lambda_s=0$ if $s$ is noncyclic, and $\lambda_s=J_C$ for a cyclic $s$ on cycle $C$. Then
$$
 (1-\lambda_s)b(s)=\delta s E_{\rm odd}(W_s). \tag{3}
$$
Indeed for first-hit slope totals $f_j(s)$ one has $f_j=g_j$ at a noncyclic target, and $f_j=g_j-J_Cg_{j-|C|}$ on its cycle, with negative indices zero. Exactly
$$
 \sum_{j=0}^Q f_j(s)=s\sum_{\tau_s(x)\le Q}W_s(x)/x.
$$
The part $x> s2^{6Q}$ costs $O_s(Q[3(1+\sqrt2)/8]^Q)$ on the left: $x\le s2^{S_j}/3^j$, so these words have $S_j>6Q$. On the remaining range use (2) with $H\ge s$. In the high-log region a good start cannot have hit $s$ by time $Q$. In the low-log region a good start which ever hits $s$ either has hit it by the bounded-set passage or must hit it on the future orbit of its landing. The largest such future delay over the fixed finite set of possible landings is finite. Therefore, outside the central log strip and bad starts, the clock cutoff equals the source cutoff $x\le e^{dQ}$ for $W_s$. Both observables are bounded by one. Divide their summed discrepancy by $Q$, let $Q\to\infty$, then $H\to\infty$ and $\epsilon\downarrow0$. The depth average of the left side tends to $(1-\lambda_s)b(s)$. This proves (3) along $X=e^{dQ}$, and then at arbitrary $X$ since consecutive log cutoffs differ by the fixed $d$.

## The numerical limit of the cone

Write $V_\infty(x)=\lim_QV_Q(x)$, which exists by monotonicity. It vanishes on eventual cycles and is positive on escape by the uniform simple-orbit reciprocal bound. For continuous $\psi:[0,1]\to\mathbb R$ with $\psi(0)=0$, define $G(v)=v\psi(1-v)$. The finite weighted offset statistic, with the usual first positive odd representatives $t_w>1$ and cap $a_i\le2Q$, satisfies
$$
 \lim_{Q\to\infty}\frac1Q\sum_w \frac{J_w}{t_w}\psi(F_w/t_w)
   =\delta E_{\rm odd}\big[G(V_\infty)\big]. \tag{4}
$$
In particular $\psi(z)=z$ gives exactly the first moment in the scalar $C_Q$, whose range without its cycle flag is $[0,\delta/4]$.

First the finite limit on the left exists without a source mean. The cutoff costs $O(\|\psi\|_\infty Q(3/4)^Q)$ before normalization. The [raw harmonic bound and repeated-path removal](CONE_WITHOUT_OVERSAMPLING.md) give $O(Q)$ total weight and $o(Q)$ repeated-path weight. On a simple path replace its product by the factors at odd states at most $H$. The uniform simple-orbit reciprocal tail and uniform continuity of $\psi$ make the normalized error tend uniformly to zero with $H$. On the finite Boolean cube of visits the truncated observable is a multilinear polynomial with zero constant term. For a monomial requiring visits to a fixed nonempty compatible set of escaping states, let $s$ be its earliest state and $l$ the number of steps from $s$ to its last marked state. With $y_j=U^j s$, its normalized contribution is exactly
$$
 Q^{-1}\sum_{j=l+1}^Q J(s,j)g_{Q-j}(s)/y_j\ \longrightarrow\ V_\infty(s)b(s)/s.
$$
For large $Q$ all $y_j$ with $j\le Q$ fit the first representative since $y_j\le(s+1)(3/2)^j$. Distinct $y_j$ prevent double counting. If a required marked state is eventually periodic, its possible endpoints belong to a fixed finite set and their contribution vanishes by the fixed-target bounds; incompatible sets contribute zero. For a fixed multiple of three, $g_k(s)=0$ for $k>0$. This proves existence of the left limit.

For its value, remove the exponent cap again and keep $S_Q\le6Q$: the remaining tail costs $O(\|\psi\|_\infty[3(1+\sqrt2)/8]^Q)$ before normalization. The retained terms come from distinct odd sources $x\le2^{6Q+1}$ and equal $G(V_Q(x))/x$. Equivalently one can first impose only this physical source bound: any extra included compatible word has $S_Q>6Q$ and costs the same exponentially small bound. On good low-log starts the representative condition holds, since $U^Q x\le(x+1)(3/2)^Q\le2\cdot3^Q$. After the bounded-set landing, at least $c_\epsilon Q$ further steps remain. For every one of the finite possible landing states $y\le H^\alpha$, $V_m(y)\to V_\infty(y)$ uniformly on $m\ge c_\epsilon Q$ as $Q\to\infty$. The prefix product is at most one. This and uniform continuity show $G(V_Q(x))-G(V_\infty(x))=o_H(1)$ uniformly on good low-log starts. Excluding endpoint one causes $o_H(1)$ as well: such a start is eventually periodic and $G(0)=0$.

For good high-log starts the landing occurs after $Q+c_\epsilon Q$, so all inputs up to $Q$ exceed $H$. No repeated state can occur there for large $Q$. A repeat would already put the orbit on a cycle which eventually meets $[1,H^\alpha]$, hence is one of finitely many cycles; the remaining time to first passage would be bounded by their maximum period. The uniform simple-path tail therefore gives $V_Q=1-o_H(1)$ and $G(V_Q)=o_H(1)$. These are upper bounds in absolute value and apply after any endpoint selection. Bad starts cost $O(Q(\log H)^{-c})$ before normalization and the central log strip costs $O(\epsilon Q+1)$. We obtain
$$
 \frac1Q\sum_w\frac{J_w}{t_w}\psi(F_w/t_w)
 -\frac1Q\sum_{x\le e^{dQ},\ x\text{ odd}}\frac{G(V_\infty(x))}{x}\ \longrightarrow 0
$$
by the same order of limits as for (3). Since the first limit exists and $G$ is bounded, this proves existence of the odd logarithmic mean in (4) and its value. No natural-density or second first-passage scale is required. On an escaping orbit through a fixed unit $R$, the finite cone lower bound comes directly from the unconditioned atom floor; the cycle flag is the original finite cycle test.

## Closed offset law and the high-source baseline

For a general continuous $\psi$ on $[0,1]$, dropping the condition $\psi(0)=0$, the same finite harmonic statistic has limit
$$
 \tfrac12(\log3)\psi(0)
   +\delta E_{\rm odd}[V_\infty\psi(1-V_\infty)]. \tag{5}
$$
This proves the baseline of the signed harmonic formula by direct physical-source accounting.

First $E_{\rm odd}(V_\infty)$ exists. If any orbit visits an odd state $s\le H$, its full product is at most $1-1/(3H+1)$. The complementary event has upper logarithmic density tending to zero with $H$ by Tao's almost-bounded theorem. Thus the observable $v\mapsto v$ evaluated at $V_\infty$ is approximable in upper logarithmic mean error by continuous $v\psi_H(1-v)$ with $\psi_H(0)=0$, taking a cutoff equal to one on $1-v\ge1/(3H+1)$. Equation (4) gives those means. The bounded approximation then also gives existence for the source average in (5).

To identify the extra term we require the position throughout the good clock, not only first passage times. On its event (5.12), Tao's displayed (5.14) bounds
$$
 |\log U^k N_y-\log N_y+dk|\le C(\log z)^{3/5}
$$
simultaneously at every $0\le k\le n_0$; on this event the crossing of $z$ occurs in that range by (5.15). Start a fresh $N_{X_{i-1}}$ with final crossing $X_{i+1}$. Subtract the position estimate at the first crossing of $X_i$ from each position through the first crossing of $X_{i+1}$. The resulting segment event bounds log displacement relative to its own initial vertex and is measurable from $P_{X_i}$. Therefore precisely the same total variation and summability argument as for (2) transfers all segment events simultaneously to the original source. The first segment uses (5.14) directly; adding discrepancies over any initial sequence of segments yields
$$
 \sup_{0\le k\le T_{X_J}(N_X)}|\log U^k N_X-\log N_X+dk|
       \le C(\log X)^{3/5} \tag{6}
$$
outside $O((\log H)^{-c})$. No statement about positions after the last passage is used.

Return to the high-log region of the proof of (4), where $Q<T_{X_J}$ by a linear margin, the path is simple, and $V_Q=1-o_H(1)$. The condition $U^Qx\le2\cdot3^Q$ there is, by (6), equivalent to $\log x\le Q\log4$ apart from an $o(Q)$-wide log strip; the factor two contributes only a bounded shift. Also $U^Qx>H$ there. Thus, up to $o_H(1)$ and the earlier central strips and exceptional fractions, these sources contribute their plain harmonic sum multiplied by $\psi(0)$. Its normalized value in the range $dQ<\log x\le Q\log4$ tends to $(\log4-d)\psi(0)/2=(\log3)\psi(0)/2$. The low-log comparison with the complete-orbit product and the $S_Q>6Q$ tail both use only boundedness of $\psi$ and $G(0)=0$, which still hold. This proves (5).

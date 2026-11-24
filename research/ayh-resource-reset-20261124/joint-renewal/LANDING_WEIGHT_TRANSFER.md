# Bounds on the original mass at a prescribed set of paired landings

Let $R=81^j$, $d=\log_2R$, $x=81m+r\in[7R,8R)$, and let $T$ denote the ordinary positive shortcut. Write $v,w$ for the respective child and parent first entrances below $M=d^D$, and use an integer ceiling for $M$ if desired. A missed entrance contributes no landing pair. The earlier first-passage theorem gives, for each $A>1$, constants $D,K,C$ and all sufficiently large $d$, a set of at most $O_A(Rd^{-A})$ original exceptional children outside of which both entrances occur by $H=\lceil Cd\rceil$. Its sliding tests control every $b$-window of either arm before passage, $b=\lceil K\log_2d\rceil$. Larger fixed $D$ are allowed with the constants enlarged if necessary. Below, all implicit constants may depend on these fixed choices.

**Theorem.** There is a single exceptional set of $O_A(Rd^{-A})$ original children, independent of any landing tests, with the following property. On its complement, count only children failing a finite canonical merger certificate by a deterministic clock $h_*=\log_2R-D\log_2d+O(\log\log d)$, rounded down as specified below. The mass at each individual landing height, **on either labeled arm**, is
$$
                  O_A\big(R(\log d)^{3/2}/M\big).                   \tag{1}
$$
Thus if $W_j$ counts every timely pair, $E$ is any set of ordered pairs, and $P,Q$ are any two vertex sets such that $(v,w)\in E$ implies $v\in P$ or $w\in Q$, the weighted discordant count satisfies
$$
 \frac1R\sum_{(v,w)\in E}W_j(v,w){\bf1}_{f(v)\ne f(w)}
 \ll_A d^{-A}+(\log d)^{3/2}(|P|+|Q|)/M .                        \tag{2}
$$
The same statement holds with the color test replaced by failing the certificate at $h_*$. An optimal two-sided cover can be chosen for each $j$. In particular the contribution to the global series is summable whenever
$\sum_j(\log d_j)^{3/2}(|P_j|+|Q_j|)/M_j<\infty$.
This supplies an actual quantitative estimate for described landing events. Applied to an unrestricted event, the independent uniform-grid estimate $O(d^{-1/2})$ is stronger.

## Physical correction at the true entrance

For one arm put $y_i=T^i n$, $\tau=\tau_M(n)$, and $p_t=p_n(t)$. Throughout a good pre-entrance $b$-block the exact multiplicative formula gives
$$
 \frac{y_{i+b}}{y_i}
 \le 2^{-b}3^{(1/2+1/40)b}(1+1/(3M))^b
 \le \lambda^b
$$
for a fixed $\lambda<1$ and large $d$, provided all its inputs precede $\tau$. In the lists of times $i<\tau$ in each residue modulo $b$, this implies $1/y_i\le\lambda^b/y_{i+b}$ whenever $i+b<\tau$. The last of these pre-entrance heights is at least $M$. Summing the reverse geometric series in at most $b$ residue classes proves
$$
 \sum_{i<\tau}\frac1{y_i}\le\frac{b}{M(1-\lambda^b)} .
$$
In the exact multiplier at entrance write
$$
 y_\tau=3^{p_\tau}2^{-\tau}n\,\exp(\varepsilon_n),\qquad
 0\le\varepsilon_n=\sum_{\substack{i<\tau\\y_i\ {\rm odd}}}
                  \log(1+1/(3y_i))\ll b/M.                         \tag{3}
$$
For every timely arm, even without the sliding tests, one always has the weaker $\varepsilon_n\le H/(3M)$.

## A short interval of possible entrance times

We include the elementary refinement needed for (1). Set $a=1-\frac12\log_2 3>0$. For each arm, outside a further $O_A(Rd^{-A})$ original children,
$$
    a\tau=d-\log_2M+O_A(\sqrt{d\log d}).                            \tag{4}
$$
One way to prove this within the hypotheses of [FIRST_PASSAGE_MARKS.md](../literature-step/FIRST_PASSAGE_MARKS.md) is to retain its decreasing-threshold schedule $Y_{i+1}=Y_i^\gamma$, $0<\gamma<1$ fixed, $L_i=\log_2Y_i$, $k_i=\lfloor L_i/2\rfloor$, stopped the first time $Y_i\le M$. In addition to that proof's good tests on the first $k_i$ bits at every stage, discard any word with
$$
  |p_l-l/2|>C_A\sqrt{k_i\log d}\qquad\text{for some }0\le l\le k_i.
$$
The full residue-grid fraction is at most $2k_i d^{-2C_A^2}$ by Hoeffding's inequality with natural logarithm in the displayed cutoff. The original first-entrance fiber bound, equation (3) of the cited proof, loses at most $O((1+H)^3)$ per stage. The initial stage has ordinary complete-period counting. Choosing $C_A$ large absorbs this loss, the $k_i=O(d)$ and the $O(\log d)$ stages, giving the stated absolute original-source exception. The parent has fixed multiplicity 81.

On the good sample, each successive passage takes at most $k_i$ additional steps, including the truncated last block ending at $\tau_M$. Indeed the existing schedule proves passage to $Y_{i+1}$ by that clock and the heights are crossed in decreasing order; at an entrance already below a later threshold the duration can be zero. Therefore
$$
 |p_\tau-\tau/2|\le C_A\sum_i\sqrt{k_i\log d}=O_A(\sqrt{d\log d})
$$
by the geometric decay of $L_i$. Combine this with (3), $\log_2 n=d+O(1)$ on either arm, and $\log_2 y_\tau=\log_2 M+O(1)$ to obtain (4). In particular each arm's admissible entrance times lie in a deterministic interval containing $O_A(\sqrt{d\log d})$ integers.

This argument adapts the original-source concentration method of Shaik, who establishes a time window of the same order in his scalar first-passage analysis. The additional reduction below uses the uniform **pair** merger estimate inside an interval of original sources. [Shaik, Lemmas 4.2 and 6.1](https://shaikidris.github.io/polylog/paper/).

## Counting the missed original head edges within each fiber

Fix either labeled arm, a time $t$ in (4), and its assigned landing height $y$. For an original source value $n$ on this arm, (3) forces
$$
 C_{t,p,y}e^{-C_1 b/M}\le n\le C_{t,p,y},
 \qquad C_{t,p,y}=2^t3^{-p}y .                                    \tag{5}
$$
The possible source values in the child arm belong to $[7R,8R)$, and those in the parent arm to $[7R/81,8R/81)$. Each has endpoint ratio $8/7$. The centers for two different $p$ have ratio at least 3, so for all sufficiently large $d$ at most one $p$ has (5) intersecting the arm's source interval. On nonempty intersection its center is $O(R)$, and the possible source values occupy an interval of length $O(Rb/M)$.

For a fixed $r$, return to the parent parameter $m$ in the original relation $x=81m+r$. The interval for either chosen arm becomes an interval of at most $L_*=\lceil C_2Rb/M\rceil+2$ consecutive parents, uniformly in $(t,y,r)$, with a fixed $C_2$. Enlarge each nonempty interval to $L_*$ consecutive positive parents. The written uniform full-grid estimate in [PR 146, THREE_RAY_UPPER](https://github.com/GettysburgResearch/collatz/blob/f431078244e868dc699fad011044f0d5e7f76437/research/upper-bit-mergers/THREE_RAY_UPPER.md), applied to initial state $(4,r)$, bounds the parents missing symbolic coalescence by $h_*=\lfloor\log_2 L_*\rfloor$ by $O(L_*/\sqrt{\log(2L_*)})$. That theorem is uniform in the **location** of the interval. Since $D$ is fixed, $\log L_*\asymp d$. The resulting bound per $(t,y)$, summed over $r$, is $O(Rb/(M\sqrt d))$. Summing over (4) and using $b=O(\log d)$ proves (1). This argument never applies a fresh-grid assertion to the landing integers themselves. It tests actual coalescence on the original affine pair inside each source interval and may harmlessly count parents that did not produce the specified fiber.

The typical missed-pair measure from (1) is nonnegative, and both its marginal weights at each height are bounded by its right-hand side. Multiplication by the two cover indicators gives (2), paying the exceptional children only once. More generally, arbitrary nonnegative vertex weights $a_v,b_w$ with $a_v+b_w\ge1$ on $E$ give the same estimate with $|P|+|Q|$ replaced by $\sum_va_v+\sum_wb_w$. Actual discordance implies failure of the finite certificate by orbit invariance.

## Arithmetic support of the joint landing law

Use $\varepsilon_x,\varepsilon_m$ from (3) and define $u=t_m-t_x$, $s=4+p_x(t_x)-p_m(t_m)$. Then
$$
 \log(v/w)=u\log2+s\log3+\log(1+r/(81m))+\varepsilon_x-\varepsilon_m.
                                                                        \tag{6}
$$
For all timely pairs $|u|,|s|\le H+4$, and the remainder is $O(H/M+1/R)=O(d/M)$. On the good source set it is $O(b/M)$. Since $\log(v/w)$ is in $[-\log2,\log2]$, only $O(H)$ pairs $(u,s)$ are possible: for each integer $u$, the admissible $s$ form an interval of bounded length.

There are effective absolute $c,\nu>0$ such that for $|a|,|b|\le 2H+8$, $(a,b)\ne(0,0)$,
$$
                   |a\log2+b\log3|\ge c(1+H)^{-\nu}.
$$
This is the specialization of Matveev's lower bound for two fixed positive rational logarithms; multiplicative independence rules out zero and a vanishing coefficient is elementary. No numerical exponent is required. [Matveev, Izvestiya Mathematics 64 (2000)](https://www.mathnet.ru/php/archive.phtml?jrnid=im&option_lang=eng&paperid=314&wshow=paper).

Choose $D>\nu+2$ as well as the first-passage requirements. Then for sufficiently large $R$ the $O(H)$ intervals of radius $C d/M$ about the possible values of $u\log2+s\log3$ are disjoint. In particular each timely landing pair determines $u,s$ uniquely. With $(u,s)=(0,0)$ one has $|v-w|=O(d)$, improved to $O(b)$ on the good set. Every other $(u,s)$ satisfies $|\log(v/w)|\gg d^{-\nu}$ and hence $|v-w|\gg Md^{-\nu}$. Thus the actual mass, of either color, on
$$
                 C d<|v-w|<c'Md^{-\nu}
$$
is zero for all sufficiently large rows. On replacing $Cd$ by $C'\log d$, its normalized mass is $O_A(d^{-A})$ and summable. Each typical slope strip has $O(Mb)$ ordered integer points, giving $O(dMb)$ candidates across all of them. The separation does not give a density law inside a strip. The estimates above leave open the full weighted mass on different colors.

On the good set, (4) also gives $|u|=O_A(\sqrt{d\log d})$. The bounded ratio in (6) then gives the same bound for $|s|$. Consequently the typical source mass is carried on only $O_A(\sqrt{d\log d})$ strips, pairwise separated by $\gg_A(d\log d)^{-\nu/2}$ in logarithmic slope. In particular the larger intermediate band
$$
                 C_A\log d<|v-w|<c_A M(d\log d)^{-\nu/2}
$$
has normalized mass $O_A(d^{-A})$ in all colors. This strengthening only uses the time concentration and applies to the same exceptional set as (1).

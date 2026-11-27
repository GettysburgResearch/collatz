# Escape tested at one physical clock

**Proposed written consequence of F and S.** Let $T$ be the ordinary shortcut map and $G_b=(4/3)^b$. For $H\ge2b$, define $R_{b,H}(M)$ as $1/G_b$ times the number of positive odd starts $x$ prime to three satisfying

$$
 G_b/2^{101}<x\le G_b,\qquad
 T^u(x)\le M\ \text{for some }0\le u\le2b,\qquad T^H(x)>\lceil\sqrt b\rceil .
$$

If an ordinary orbit escapes, there are a fixed $M$ and $c>0$ such that $R_{b,H}(M)\ge c$ for **every** sufficiently large $b$ and **every** $H\ge2b$. If all ordinary orbits are eventually periodic, then for each $M$ this count is zero for every sufficiently large $b$ and every $H\ge2b$. In particular the escape case is excluded exactly when $\liminf_b R_{b,2b}(M)=0$ for each $M$. Each statistic at $H=2b$ is a finite count on one source interval at one physical observation time. The separate possibility of a nontrivial cycle remains.

Use the central fixed-total lower bound F and the elementary simple-path sparsity bound S with their hypotheses as stated in [PR #207, §§2–3, fixed head](https://github.com/GettysburgResearch/collatz/blob/b56c4dc2c28a184cf55638bb80c49a9d4662fc81/research/diffusive-central-row-closure-20261124/README.md). The inference below is conditional on F. Its analytic input has not been independently verified here.

Choose an escaping odd unit $a$ and let $M=a$. Write $\alpha=\log_2 3$. For each integer $n=b-j$ with $\sqrt b/4\le j\le\sqrt b/3$, set

$$
 t_n=\lfloor 2b-\alpha j-\log_2 a\rfloor .
$$

For sufficiently large $b$ these are distinct positive clocks below $2b$, since $\alpha>1$. Their deviations from $2n$ are $(2-\alpha)j-\log_2 a+O(1)$, within $\sqrt n$. Also $G_b/2<a\,2^{t_n}/3^n\le G_b$. For each $n$, F supplies at least $c_F2^{t_n}/(3^{n+1}\sqrt n)\ge c_F G_b/(6a\sqrt b)$ distinct unit sources reaching $a$ in exactly $n$ odd steps and $t_n$ shortcut steps. Such a prefix is simple: any repeated value would force $a$ to be periodic. Its distortion $D=a2^{t_n}/(3^n x)$ satisfies $1\le D<2^{100}$ by S, giving the stated common source interval. Sources from different $n$ are disjoint because an escaping $a$ cannot be hit at two distinct clocks.

At any $H\ge2b$ the cohort associated with $n$ is at $T^{H-t_n}(a)$. These residual clocks are distinct. On the entire escaping ray, the number of **physical** times at values at most $L$ is at most $5L^{39/40}(1+\lfloor\log_2 L\rfloor)$. Indeed each such value is $2^d y$ for an odd value $y\le L$ reached on the same ray after $d$ halvings. S counts at most $5L^{39/40}$ such odd values, and injectivity allows each pair $(d,y)$ only once. This also handles odd observations with $d=0$. At $L=\lceil\sqrt b\rceil$ the bound is $o(\sqrt b)$. Thus a positive fraction of the $\asymp\sqrt b$ cohorts have a high value at $H$, uniformly in $H$. Summing their distinct sources proves the lower bound.

Conversely, under eventual periodicity the union of forward orbits of all integers up to $M$ is bounded. This proves eventual vanishing, including after arbitrarily long observation delays. The missing upper estimate must control upward motion **after** entry to the finite gate set on the original deterministic orbit. A bound on the time of first entry leaves this motion unrestricted.

## An unconditional lower count at the same observation time

There is also an elementary criterion without F or S. Let $P_{b,H}(M)$ be the **number** of sources satisfying the same gate and observation conditions, with source interval

$$
              G_b/[2(b+1)^{1/6}]<x\le G_b .
$$

An escaping gate $a$ gives $P_{b,H}(a)\ge c\, b\,2^{\lfloor b/16\rfloor-1}$ for all sufficiently large $b$ and all $H\ge2b$. Consequently all orbits are eventually periodic if and only if $\liminf_b P_{b,2b}(M)/(b\,2^{\lfloor b/16\rfloor})=0$ for every fixed $M$. The stronger positive-density lower bound on the $G_b$ scale above uses F.

For each integer $m\in[b/16,b/12]$, set $t_m=\lfloor b\log_2(4/3)+m\log_2 3-\log_2 a\rfloor$. These distinct clocks are below $2b$. They satisfy $t_m\ge6m+7$ for large $b$ because even at $m=b/12$ the coefficient $\log_2(4/3)-(6-\log_2 3)/12$ is positive. At this exact clock one internal mark can absorb the parity constraint for every one of the $2^{m-1}$ binary prefix words. Reading the word from the forward path gives distinct sources. [Formal construction and readout](TernaryItinerary.lean)

Each prefix is simple, ends at the escaping $a>2$, and has $D^6\le m+1$ by the distinct-input product estimate. Equivalently, violating the bound would place a nontrivial cycle on that source's own forward trajectory. Since $G_b/2<a2^{t_m}/3^m\le G_b$, its source $x=a2^{t_m}/(3^m D)$ is in the displayed interval. [Formal distortion bound](CycleDetection.lean)

At time $H$ the cohorts are at the distinct ordinary values $T^{H-t_m}(a)$. At most $\lceil\sqrt b\rceil$ of the $\asymp b$ clocks can then contribute a value at most $\lceil\sqrt b\rceil$, by injectivity on positive integers, including even values. Sources in the remaining cohorts are disjoint because $a$ cannot repeat. This proves the count. Eventual periodicity gives eventual zero by the same finite-gate argument. The source interval can be tested with integer arithmetic by clearing denominators and raising the positive quantities to the sixth power.

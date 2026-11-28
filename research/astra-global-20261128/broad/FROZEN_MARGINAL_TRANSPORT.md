# A half-dimension obstruction for coherent source marginals in inverse Collatz control

**Finite theorem.** Let $U=\mathbb Z_3^\times$. Fix any probability $\nu$ on $U$, let $\nu_j$ be its projection modulo $3^j$, and let $\bar\nu_{j}$ be its lift by one fresh, uniform top trit. A width-$w$ inverse control, $w\ge2$, chooses positive legal exponents $e$ at a unit state $s\bmod 3^w$. The successor has lower residue $I_e(s)=(2^e s-1)/3\bmod 3^{w-1}$ and a uniform new top trit. Let $C_w(\nu)$ be the smallest expected exponent of a stationary flow whose width-$w$ state marginal is prescribed to equal $\bar\nu_{w-1}$. Put $N_w=2\cdot3^{w-1}$ and $A_W=\max_{2\le w\le W}C_w(\nu)$. Then for every $W\ge2$,
$$
 \boxed{\quad A_W\ge \frac{N_W}{4\pi}\left(\max_v\nu_{W-1}(v)\right)^2 .\quad} \tag{1}
$$
Thus uniform bounded mean expenditure in this fixed-marginal architecture requires all $j$-trit cylinders to have mass $O(3^{-j/2})$. An optimal finite controller is allowed to choose different, mutually incompatible lower marginals at different widths. Equation (1) does not impose this Hölder bound on weak limits of arbitrary finite optimal policies.

In particular, let $\mu_\theta$ be the ternary law of the positive geometric gap word, with $\Pr(e=j)=\theta(1-\theta)^{j-1}$. Its forward contractions $A_e(y)=(1+3y)/2^e$ code the source unit. The signed unit $-1$ is fixed by $A_1$ and $A_1^j(y)=-1+(3/2)^j(y+1)$. The first $j$ prescribed exponents all equal one with probability $\theta^j$, contributing to a single atom $-1\bmod3^j$. Consequently
$$
 A_W\ge \frac{(3\theta^2)^{W-1}}{2\pi}. \tag{2}
$$
For every $\theta>1/\sqrt3$ the costs are exponentially unbounded along an infinite subsequence, with $\limsup_w w^{-1}\log C_w\ge\log(3\theta^2)$. This includes the Shannon-critical parameter $\theta_*$ where the single-gap entropy is $\log3$: entropy is strictly decreasing in $\theta$, and $H(3/5)>\log3$ follows from $5^5>4\cdot3^6$. In contrast, unrestricted finite mean costs remain bounded, since every unit has some legal exponent at most four and a finite state chain admits a stationary law. The two conclusions concern different choices of stationary marginal.

## 1. Directed cyclic transport is exact

Represent each unit $s$ by $d=\log_2s\bmod N_w$, setting $s=2^d\bmod3^w$. Doubling has order $N_w$: 2 generates mod 3, $v_3(4-1)=1$, and iterating $v_3(u^3-1)=v_3(u-1)+1$ for $u\equiv1\pmod3$ gives the order at every lift. To land at a prescribed parent unit $v\bmod3^{w-1}$, a source exponent $e$ must advance its logarithm to
$$
 k(v)=\log_2(1+3v)\pmod{N_w}.
$$
Take the smallest strictly positive such $e$, at most $N_w$, including $N_w$ for a full circuit when $d=k(v)$. Let $\pi_w=\bar\nu_{w-1}$ in these log coordinates, and let $\eta_w$ be the image of $\nu_{w-1}$ under $k$. A coupling from $\pi_w$ to $\eta_w$ specifies an admissible stationary control by sampling the endpoint conditionally on its source. The successor low marginal is then exactly $\nu_{w-1}$ and the new trit is uniform. Conversely a stationary flow with this marginal supplies that coupling. Hence $C_w$ is the minimal mean strictly positive forward distance on the log circle between $\pi_w$ and $\eta_w$. In particular it is always finite.

One can compute $C_w$ without solving an unrestricted Bellman equation. Let $f_d$ be the mass traversing edge $d\to d+1$ of the directed circle. Every feasible transport gives
$$
 f_d-f_{d-1}=\pi_w(d)-\eta_w(d),\qquad f_d\ge\pi_w(d),\qquad C_w=\min\sum_d f_d. \tag{3}
$$
The inequality records that arrivals must serve demand before the current injection can be used, since gaps are strictly positive. Conversely a nonnegative edge flow satisfying these balances can be decomposed into source-to-target paths and extra cycles by splitting each vertex into an arrival and a departure node. At the smallest additive constant allowed by $f_d\ge\pi_w(d)$ there is an edge index with $f_d=\pi_w(d)$. At its departure node the complete arriving mass has been consumed by that point's demand, so the cut circle becomes an interval on which one can match queued masses without any extra circulation. The resulting paths have length between one and $N_w$; this also proves (3).

For the geometric law, write $\mu_d$ for the unflattened mass at log coordinate $d$. Its forward distributional recursion gives $\mu_{d-1}=\theta\eta_w(d)+(1-\theta)\mu_d$ with all logs read cyclically. Hence $a\mu_d$, $a=1/\theta$, solves the balance with unflattened source $\mu$. Let $H_d-H_{d-1}=\pi_w(d)-\mu_d$ and normalize $\sum_d H_d=0$. Substitution into (3) yields the exact scalar formula
$$
 C_w=a+N_w\max_d\left(\pi_w(d)-a\mu_d-H_d\right). \tag{4}
$$
No convergence or stochastic-control theorem is required for (3)–(4).

## 2. The Fourier test over conductors

Use the character $d\mapsto\exp(2\pi i k d/N_w)$ to define $\widehat\eta_w(k)$ and $\widehat\pi_w(k)$. The three lifts of a single lower log $d$ are $d,d+N_w/3,d+2N_w/3$. Their probabilities under $\pi_w$ are equal. Therefore $\widehat\pi_w(k)=0$ when $3\nmid k$. If $(D,E)$ is any feasible source and exponent pair, then $D+E$ has law $\eta_w$. The triangle inequality gives the finite bound
$$
 |\widehat\eta_w(k)|=|\mathbb E[e^{2\pi i kD/N_w}(e^{2\pi i kE/N_w}-1)]|
 \le 2\pi |k|C_w/N_w \qquad (3\nmid k) . \tag{5}
$$
Here use a minimizing pair, which exists in the finite transport problem. The target distributions $\eta_w$ are projectively consistent because both $1+3v$ and the doubling logarithm commute with reduction. For every $1\le k<N_W/2$, divide both $k$ and $N_W$ by $3^{v_3(k)}$. The resulting conductor has width $w\ge2$, and (5) bounds the original coefficient by $2\pi k A_W/N_W$. The elementary order-two character, which would reduce to width one, is excluded by the strict range on $k$.

Let $2\le K\le N_W/2$. The nonnegative Fejér kernel $K^{-1}|\sum_{j=0}^{K-1}e^{2\pi i j t}|^2$ takes value $K$ at zero and has Fourier coefficients $1-|k|/K$ at $|k|<K$. Translate it to a largest atom $d_0$ of $\eta_W$ and integrate. Writing $M=\eta_W(d_0)=\max_v\nu_{W-1}(v)$, we obtain
$$
 M\le \frac1K+\frac{4\pi A_W}{N_W K}\sum_{k=1}^{K-1}k(1-k/K)
 =\frac1K+\frac{2\pi A_W}{3N_W}(K-K^{-1}). \tag{6}
$$
If $M\le6/N_W$, then $N_W M^2\le6$ and $A_W\ge1$ suffices for (1). Otherwise choose $K=\lceil2/M\rceil$, with $2\le K\le N_W/2$ since $N_W\ge6$. Then $K\le3/M$ and (6) yields (1). An unbounded sequence of values of $A_W$ in (2) must be obtained at widths $w\to\infty$; since $w\le W$, the exponential limsup follows.

## Scope and primary comparisons

Weaver's finite-state classification identifies the uniform-top structure of finite stationary laws and gives the variational limit for their freely chosen marginals. The checkpoint of peer PR 215 averages a Bellman inequality on the actual critical source and observes that small weighted oscillation in its last observed trit would prove the optimal critical endpoint. It does not prescribe the exact stationary lower marginal to be the critical cylinder law. The estimate here tests that stronger prescription and explains why it fails despite the critical law's full Shannon entropy dimension. The signed fixed ray supplies a large finite cylinder; no positive integer orbit follows from its use here. [Weaver, paper 127/v1, Sections 9 and 12](https://rstation.ai/problems/collatz/papers/127/v1) · [PR 215, critical Bellman lifts](https://github.com/GettysburgResearch/collatz/blob/7902faf17d50851b46cdcd420ae479d19f0c845c/research/astra-nine-hour-20261128/machinery/phase5/CRITICAL_BELLMAN_LIFTS.md) · [Weaver, paper 135/v1, critical singularity and entropy](https://rstation.ai/problems/collatz/papers/135/v1).

## 3. A rational tent test with a sharper constant

There is an elementary proof without trigonometric functions. Fix $W$, put $N=N_W$, choose $1\le L\le N$, and let $d_0$ be any target position. On the additive log circle of length $N$ take
$$
 b(d)=\frac1L\#\{(u,v)\in[0,L)^2\cap\mathbb Z^2:\ v-u\equiv d-d_0\pmod N\} .
$$
Then $b(d_0)=1$, $b\ge0$ and its uniform mean is $L/N$. Write $b_w$ for the function on modulus $m=N_w$ obtained by averaging all lifts uniformly, including $w=1$ with $N_1=2$. It has the exact expression
$$
 b_w(d)=\frac{m}{NL}\sum_{j\bmod m} a_j a_{j+d-d_0},\qquad
 a_j=\#\{0\le u<L:\ u\equiv j\pmod m\}.
$$
Put $q=\lfloor L/m\rfloor$, $r=L-qm$. The counts $a_j=q+\mathbf1_{[0,r)}(j)$ on the cyclic residue set. The only nonconstant part of their autocorrelation is the intersection size of two cyclic arcs of length $r$. Shifting by one replaces at most one element by one other, so changes this size by at most one. Consequently the adjacent-value Lipschitz constant of $b_w$ is at most $m/(NL)$. Its maximum is bounded by
$$
 \frac{L}{N}+\frac{m^2}{4NL}, \tag{7}
$$
since the largest autocorrelation is at zero shift and $\sum_j a_j^2=L^2/m+r(1-r/m)$. These bounds work as stated even when $L$ is a multiple of $m$.

Each band $b_w-b_{w-1}^{\uparrow}$ has zero average against the top-uniform source $\pi_w$ and adjacent Lipschitz constant at most $(4/3)N_w/(NL)$. On any forward transport with mean $C_w$ the expectation of this band under its demand $\eta_w$ is therefore at most $(4/3)C_wN_w/(NL)$, by summing differences along each transported path. Projective consistency of $\eta$ telescopes the bands. The width-one term differs from the uniform mean by at most $1/(NL)$ by (7). Since $\sum_{w=2}^W N_w=\tfrac32(N-2)$,
$$
 \eta_W(d_0)\le \frac LN+\frac1{NL}+\frac{2(N-2)}{NL}A_W. \tag{8}
$$
Thus $2(N-2)A_W\ge NL\eta_W(d_0)-L^2-1$ for every integer $1\le L\le N$. Choosing a nearest integer to $N\eta_W(d_0)/2$ at a largest atom gives $2(N-2)A_W\ge N^2 M^2/4-5/4$. Here $M\ge3/N$ because the demanded cells number $N/3$. This sharpens the leading coefficient in (1) without using a complex Fourier transform.

## 4. Multiplicative distortion is necessary even for freely varying lower marginals

Take any sequence of width-$w$ stationary policies with means bounded by $C$. Their lower marginals $\lambda^{(w)}$ may vary arbitrarily. Suppose that for fixed $0<l\le u<\infty$ and all sufficiently large $w$ there are two-sided bounds at the working lower precision,
$$
 l\,\nu_{w-1}(v)\le\lambda^{(w)}(v)\le u\,\nu_{w-1}(v)\quad\text{for every }v.
$$
Put $R=u/l$. If $1\le R<3$, then the fixed target law necessarily satisfies
$$
 \max_v\nu_{W-1}(v)\ll_{l,u,C} N_W^{-s},\qquad
 s=\frac{1-\log_3 R}{2-\log_3R}. \tag{9}
$$
The implied onset may depend on the initial exceptional widths. To prove this, use the tent above and put $E_w=\int b_w\,d\eta_w$ for the demand formed from the fixed target $\nu$. The actual policy demand is the image of $\lambda^{(w)}$ and its one-width projection is the image of the corresponding projection of $\lambda^{(w)}$. The same inequalities $l,u$ apply both to them and their respective fixed target demands. Positivity of $b_w,b_{w-1}$ and the band estimate for the actual transported flow give
$$
 E_w\le R E_{w-1}+\frac{4 C N_w}{3 l N L}. \tag{10}
$$
Iterate down to the largest $j$ with $N_j\le L$, so $N_j>L/3$ away from the trivial bottom level. By (7), $E_j\le5L/(4N)$. Since $R<3$, the accumulated band errors are $O_{l,R}(C/L)$. Also $R^{W-j}\ll_R(N/L)^{\log_3 R}$. Thus
$$
 \nu_{W-1}(d_0^\sharp)\le E_W\ll_R (L/N)^{1-\log_3R} + O_{l,R}(C/L)
$$
for the unit $d_0^\sharp$ corresponding to a largest demand. Choose $L=\lceil N^s\rceil$. Its lower width $j$ tends to infinity, beyond every exceptional width. This gives (9).

For the critical Syracuse law put $d=-\log_3\theta_*\simeq0.45128716$. Its signed fixed-point cylinders give mass at least $\theta_*^{W-1}$. Consequently any uniform two-sided working-precision comparison for bounded-cost policies must obey
$$
 \frac ul\ge 3^{(1-2d)/(1-d)}\simeq1.21538639. \tag{11}
$$
For symmetric relative factors $[\rho^{-1},\rho]$ this gives $\rho\ge1.10244564\ldots$. These are lower bounds on **relative errors on every cylinder**. They do not prevent total-variation errors tending to zero, weak convergence of the state laws, or the optimal mean cost tending to $a_*$. Indeed at any fixed exponent $1/2<\alpha<1$, clipping masses exceeding $N^{-\alpha}$ removes vanishing total mass from the critical law, while permitting large relative changes on its heavy signed ray. Its Shannon entropy deficit relative to uniform is $o(\log N)$. The heavy set has uniform mass $O(N^{\alpha-1})$, so the binary relative-entropy bound makes its critical probability $o(1)$. This diagnoses what a successful finite approximation can change; clipping alone has no stationary-flow guarantee. Weaver's separate width-gap theorem already gives $W^2(\theta_*-\gamma_W)\to\infty$ for the freely optimized width-$W$ slope $\gamma_W$. The resource obstruction here measures working-precision marginal distortion. [Weaver, paper 150/v2, Theorem 1](https://rstation.ai/problems/collatz/papers/150).

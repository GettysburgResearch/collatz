# Original-source overlap and common-clock amplification at the inverse entropy threshold

Write $m$ for additive Haar probability on all of $\mathbb Z_3$, and $h_i=3m|_{i+3\mathbb Z_3}$ for $i=1,2$. For geometric iid gaps of mean $b>1$, let $\mu_b$ be their original ternary source. At depth $j$ define the finite overlap
$$
 O_j(b)=\sum_{r\bmod3^j}\min\{\mu_b([r]),3^{-j}\},\qquad
 \Lambda_b=\limsup_{N\to\infty}\frac{\sum_{j=1}^N O_j(b)}{\log N}.
$$
These are unweighted comparisons to additive Haar and retain all legal prefixes in the original source. Let $L=1/\Theta_\infty$ be the limiting optimal stationary mean gap. If $1<b<L$, then
$$
             \Lambda_b\le \frac{2}{3 I_b(L)},                      \tag{1}
$$
where $I_b(L)=D(\mathrm{Geom}(L)\Vert\mathrm{Geom}(b))>0$ uses the positive-geometric laws parametrized by their means. In particular $O_N(b)=O_{b,L}(\log N/N)$. If $\Lambda_{a_*}=\infty$, then $L=a_*$. It also suffices to prove divergence of $\Lambda_b$ on any sequence $b\downarrow a_*$ with $b>a_*$. An overlap lower bound $O_j(a_*)\gg j^{-q}$ for any $q<1$ would suffice. Weaver 135 proves an *upper* bound $O_j(a_*)\ll (1+\log j)/\sqrt{j}$ and critical singularity; the needed lower bound remains open. [Weaver 135, Theorem 1](https://rstation.ai/problems/collatz/papers/135/v1).

## 1. Convert overlap to a stationary cost upper bound

Put $t_b=-\log(1-1/b)$ and choose $0<\lambda<t_b$. For one geometric gap $g$, set $a=\lambda^{-1}\log\mathbb E_b e^{\lambda g}>b$. On the iid coding space $\exp[\lambda(S_j-aj)]$ is a nonnegative mean-one martingale. Stopping at its first crossing through a finite horizon and sending the horizon to infinity shows that the probability of violating $S_j\le aj+c$ at any date is at most $e^{-\lambda c}$ for $c\ge0$.

At depth $j+1$ the source mass coming from the successful first $j$ labels is supported on the full cells of $G_j(a,c)$ in `STOPPED_CRITICAL_CORRIDORS.md`, with their actual terminal unit trit. The complement of those cells receives $\mu_b$-mass at most the coding failure probability. So
$$
 O_{j+1}(b)\le m(G_j(a,c))+e^{-\lambda c}.
$$
This uses full additive Haar and does not identify the coding mass of a word with its Haar mass. Summing the two initial-trit stopped reward inequalities, if $a<L$,
$$
 \sum_{j=1}^{N} O_j(b)
 \le \frac{2(c+6-a)}{3(L-a)}+N e^{-\lambda c}.                    \tag{2}
$$
Take $c=\lambda^{-1}\log N$, divide by $\log N$, and optimize the positive denominator $\lambda L-\log\mathbb E_b e^{\lambda g}$. The maximizing $\lambda=\log[(1-1/L)/(1-1/b)]$ lies strictly between zero and $t_b$ for $L>b$. The tilted law there is geometric with mean $L$, giving exactly its relative entropy with respect to the original geometric law. This proves (1); monotonicity of the overlap under refinement yields the pointwise bound. In contraposed form, a finite lower bound on $\Lambda_b$ also places an explicit Cramér-rate upper bound on any $L>b$. Under unit-normalized Haar the constant in (1) changes, so the normalization here matters.

The original fixed-intercept survival test has a different boundary. At the exact slope $a_*$ even the endpoint-only event $C_n\le a_*n+c$ has summable probabilities, by Weaver 150, Theorem 3 (7) with $b'=(3/2)\log(n+1)-t_*c$. Formula (1) instead applies a *strictly larger slope* to the geometric code of mean $a_*$ and allows the intercept to increase logarithmically during the finite comparison. [Weaver 150/v2, Theorem 3](https://rstation.ai/problems/collatz/papers/150).

## 2. An exact collision test for a short native route

Let $a>a_*$, fix $c\ge1$ and let $B_n=G_n(a,c)$. Put $p_n=m(B_n)$. The stopped-corridor entropy calculation gives $p_n=e^{-o(n)}$. Choose integer route lengths $d=d(n)\to\infty$ with $d=o(n)$ and $d/(1+|\log p_n|)\to\infty$. At the common total $2d$ consider words with a fixed bound $F$ on their ordinary real offset $\beta_w=C_w/4^d$, where $C_w=\sum_{j=1}^d3^{j-1}2^{2d-S_j}$. One can take a fixed $F$ so that their number $K$ is $\gg 4^d/\sqrt{d}$ for every sufficiently large $d$. For instance apply Weaver–Wren 48, Lemma 7 (76), at zero extra precision and total $2d$, sum over its fixed positive-mass cylinder and use $\pi_d(2d)\gg d^{-1/2}$. On this fair geometric slice every word has probability $4^{-d}$. Retaining the logarithmic cap in that lemma is allowed. [Weaver and Wren 48/v2, Lemma 7 and Theorem 8](https://rstation.ai/problems/collatz/papers/48).

For any retained set $\mathcal D$ of $K$ such words put $A_w(y)=(C_w+3^d y)/4^d$. For every $y\in B_n$ the full prefix is unit-legal from $A_w(y)$: all intermediate states in the forward construction $A_e(z)=(1+3z)/2^e$ are units. Define $Z(x)=\sum_{w\in\mathcal D}{\bf1}_{A_w(B_n)}(x)$. Then exactly
$$
 \int Z\,dm=3^{-d}Kp_n,\qquad
 \int Z^2dm=3^{-d}\sum_{\substack{w,v\in\mathcal D\\ C_w\equiv C_v\ (3^d)}}
 m\left(B_n\cap\left(B_n+\frac{C_v-C_w}{3^d}\right)\right).     \tag{3}
$$
Distinct low source cells cannot intersect. On equal cells the two surjections differ by precisely the indicated integer translation in the common terminal variable. Its ordinary absolute value is at most $F(4/3)^d$. Nonzero shifts are even because the numerators are odd; distinct words at fixed total have distinct integer numerators by binary decoding. The diagonal contribution equals $\int Z$ and becomes negligible relative to its square for the full retained dictionary and the chosen $d$.

If along an unbounded sequence the right second moment in (3) is at most $C(\int Z)^2$ for a fixed $C$, then $L\le a$. Indeed Cauchy–Schwarz gives $m(Z>0)\ge1/C$. Every source in this union has a legal $d+n$ word of cost at most $2d+an+c$. The true minimum cost divided by depth converges in Haar probability to $L$, so such a fixed mass forces $L\le a$ when $d=o(n)$. This uses the worst-root/cost-in-probability theorem on the original sources. If $L>a$, every such sufficiently numerous dictionary instead has normalized second moment tending to infinity; independence of these translates would give the wrong conclusion. [Lean Assurance Lab 229, §2](https://rstation.ai/problems/collatz/papers/229).

The short shifts in (3) are arithmetic, not independent vertex samples. The finite sequence of covering sets $B_n$ consists of corridor supports, and differs from $\mu_{b,n}$ and from Haar. Equal total is what turns an affine pair into a translation. The translation singularity already proved in PR 215 checkpoint 7 applies to every nonzero integer shift here. The unresolved issue is the scale required for simultaneous finite separation. [PR 215, affine classification](https://github.com/GettysburgResearch/collatz/blob/dd69808eac0577f387d46cd6bc66af197bb6875e/research/astra-nine-hour-20261128/machinery/phase7/CRITICAL_AFFINE_OVERLAPS.md).

## 3. Separation of fixed native translations and the missing scale

At $b=a_*$ the iid gap sequence is almost surely recoverable from its exact ternary source. The exact one-gap statement follows from Leen's critical projected entropy and the branch conditional-entropy identity, and iteration recovers any fixed prefix. Thus for any two distinct equal-length words $w,v$, the probability laws $(A_w)_*\mu_{a_*}$ and $(A_v)_*\mu_{a_*}$ are mutually singular: up to null sets the recovered prefixes disagree. At a common total, if $C_v-C_w=3^d h$, affine pullback gives
$$
                   \mu_{a_*}\perp (\tau_h)_*\mu_{a_*}.              \tag{4}
$$
This holds simultaneously for the countable family of actual nonzero shifts occurring in (3). The companion `NATIVE_TRANSLATION_SINGULARITY.md` constructs finite witnesses for every nonzero integer shift and evaluates the exact limiting overlap for every dyadic rational shift. For a fixed dictionary one can choose a compact subset of arbitrarily large critical measure on which all required unequal prefix images are disjoint. At sufficiently fine but unspecified finite ternary depth those compact images then have disjoint cylinder covers. To obtain this, first choose disjoint full-measure Borel carriers for the finitely many image laws and pull each full carrier back; their intersection has full critical measure. Compact inner approximation and finite separation finish the claim. The compact subset may also be restricted to typical $a$-corridor words after allowing a sufficiently large fixed intercept, with the desired arbitrarily small additional loss. [Leen, Theorem C](https://doi.org/10.5281/zenodo.23268832) · [Critical decoding and stationary occupation](ADAPTIVE_WEAK_MARGINALS.md).

There is an exact entropy version of this loss of scale. Pick $W$ uniformly from $\mathcal D$ and $Y\sim\mu_{a_*}$ independently, and set $X=A_W(Y)$. At depth $d+n$, conditioning on $W$ sends the $n$ suffix trits bijectively to the free $n$ trits in that prefix cell. If $D_n(\mu)=n\log3-H(\mu\bmod3^n)$, then
$$
 D_{n+d}(\mathcal L(X))
   =D_n(\mu_{a_*}) + d\log3-\log K + H(W\mid X\bmod3^{n+d}).
                                                                    \tag{5}
$$
For fixed $d$ the last term tends to zero by (4) and finite-prefix decoding. Formula (5) quantifies how much source entropy a resolved equal-clock prefix can add. A full-dimensional critical suffix only gives $D_n=o(n)$, with a known lower bound of order $\sqrt n$. For a uniform upper bound on the defect in (5), it would be enough to find $d=o(n)$ where the posterior uncertainty is no more than $\log K-d\log3-D_n+O(1)$. This would put the mixed source law at bounded relative entropy from Haar, hence every mixed event of uniformly positive probability at positive Haar mass. In particular the critical iid suffix has total at most $an$ with probability tending to one for each $a>a_*$; on the resulting depth-$(d+n)$ cells one can execute the route and the first $n-1$ suffix labels with their terminal unit trit fixed by the remaining label. Their cost is at most $2d+an$, which would prove $L=a_*$. Fixed-dictionary singularity has no rate when $d$ grows with $n$. It cannot by itself replace the finite collision or posterior estimate.


## 4. Finite positive overlap at the actual implicit tilt

[The exact finite checker](check_critical_overlap.py) verifies $O_7(a_*)>0.33384$. For rational $\theta=p/q$ put $r=1-\theta$, parameterize the depth-$n$ units as $x=2^j\bmod3^n$ with period $P=2\cdot3^{n-1}$, and define $g_j$ as the preceding-level mass at $(x-1)/3$ if $x\equiv1\bmod3$, zero otherwise. The full untruncated geometric source masses $u_j$ satisfy $u_j=\theta g_{j+1}+r u_{j+1}$ around that cycle. Summing one period gives the denominator factor $q^P-(q-p)^P$ and then one reverse pass evaluates all cells by exact integer divisions. At the first four levels independent finite sums reproduce the same table, and at every depth its masses project exactly to the preceding table. At $\theta=609089768/10^9$, the computed overlap lies between $0.333850$ and $0.333851$. The checked entropy equation brackets $\theta_*$ between that rational and its predecessor by $10^{-9}$. Couple two geometric waiting times by the same successive uniforms: they can first disagree only at a trial between the two success thresholds, with probability $|\theta-\theta'|/\max(\theta,\theta')$. Coupling seven gaps, then projecting the source, gives the strict lower bound above. The finite result supplies one scale; it gives no asymptotic lower bound on $\Lambda_{a_*}$.

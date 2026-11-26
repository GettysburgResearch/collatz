# Dyadic increments of the original finite law and the cost of sibling overlap

Let $\rho_k=q\,p_k$ on residues modulo $q=3^k$ for the original independent geometric gaps with $\Pr(e=j)=2^{-j}$. For every **positive integer** $z$ set $u_k(z)=\rho_k(z\bmod q)/z$, including even $z$. Put $\rho_0=1$ and $\Phi(a)=a^2/(1+a)$. The [collision energy theorem](../global/COLLISION_ENERGY.md) and Weaver's fixed-target stopping law are the inputs for the asymptotic statements. The recursion itself is exact at finite depth.

**Increment identity.** For every $k\ge1$ and $z\ge1$,
$$
 u_k(z)-u_k(2z)={\bf1}_{z\equiv2\ (3)}
 \left(1-\frac1{2z}\right)u_{k-1}\left(\frac{2z-1}{3}\right),          \tag{1}
$$
where the right side is zero unless the displayed argument is a positive integer. Indeed the length-$k$ target residue has the final form $(3Y_{k-1}+1)2^{-e}$ in the ternary ring. The event $e\ge2$ has probability $1/2$ and its residual exponent $e-1$ has the original law. Its contribution to $\rho_k(z)$ is therefore $\rho_k(2z)/2$. The event $e=1$ contributes $(3/2)\rho_{k-1}((2z-1)/3)$ on the specified residue, since $q=3q_{k-1}$. Division by $z$ proves (1).

For positive odd $z$ set $d_{k,j}(z)=u_k(2^jz)-u_k(2^{j+1}z)$ for $j\ge0$. These increments are nonnegative and sum to $u_k(z)$, because the numerator remains bounded for fixed $k$ as $j\to\infty$. Each admissible index $2^jz\equiv2\pmod3$ corresponds to exactly one positive odd source $y=(2^{j+1}z-1)/3$. Conversely $2^jz=(3y+1)/2$ determines $j,z$ uniquely from $y$. At that index
$$
 d_{k,j}(z)=\left(1-\frac1{3y+1}\right)u_{k-1}(y),\qquad
 j=v_2(3y+1)-1.                                                        \tag{2}
$$

It is harmless to sum clipped amplitudes over all positive odd lifts. Indeed $\Phi(a)\le a^2$, and the contribution beyond the least odd representative in each residue class is bounded by
$$
 \sum_{c\bmod q}\rho_k(c)^2\sum_{m\ge1}(2mq)^{-2}=O(1),
$$
since $\sum_c\rho_k(c)=q$ and all values are nonnegative. The same bound holds after multiplying by any uniformly bounded test.

### The signed modulus-eight test

For $W(y)=3/4-{\bf1}_{v_2(3y+1)\ge2}-{\bf1}_{v_2(3y+1)\ge3}$, equations (1)–(2) give
$$
 \begin{aligned}
 \sum_{\substack{0<y<2\cdot3^{k-1}\\y\ {\rm odd}}} W(y)\Phi(u_{k-1}(y))
 =\sum_{z>0,\ z\ {\rm odd}}\left[
  \tfrac34\Phi(d_{k,0}(z))-\tfrac14\Phi(d_{k,1}(z))
  -\tfrac54\sum_{j\ge2}\Phi(d_{k,j}(z))\right]+O(1).                    \tag{3}
 \end{aligned}
$$
The error is uniform in $k$. Besides the preceding lift tail, the hazard correction costs at most a constant times $\sum_{y>0,\ y\ {\rm odd}}\rho_{k-1}(y)/(y(3y+1))$, since $\Phi$ is 1-Lipschitz on $[0,\infty)$. Weaver's Theorem 2 gives uniform boundedness and total-variation convergence of exactly this measure. [Weaver, equations (4)–(5)](https://rstation.ai/problems/collatz/papers/176)

### Exact cost of splitting a macroscopic amplitude

Define
$$
 F_k=\sum_{z>0,\ z\ {\rm odd}}\Phi(u_k(z)),\qquad
 \Gamma_k=\sum_{z>0,\ z\ {\rm odd}}
     \left[\Phi(u_k(z))-\sum_{j\ge0}\Phi(d_{k,j}(z))\right]\ge0 .
$$
The fixed-depth sums are finite by the lift-tail bound. Convexity and $\Phi(0)=0$ give the inequality. Equation (2) yields the exact balance
$$
 \Gamma_k=F_k-F_{k-1}+L_{k-1},\quad
 L_i=\sum_{y>0,\ y\ {\rm odd}}
 \left[\Phi(u_i(y))-\Phi\left(\left(1-\frac1{3y+1}\right)u_i(y)\right)\right].     \tag{4}
$$
In Weaver's notation $h(y)=\lim_i\rho_i(y)$ on positive odd $y$. The loss satisfies $L_i\to L_\infty$, where $L_\infty$ is the same convergent sum with $u_i(y)$ replaced by $h(y)/y$. Indeed each summand has the asserted fixed-target limit and lies between zero and the stopping-measure weight $\rho_i(y)/(y(3y+1))$. Total-variation convergence makes the dominating tails uniformly small in the limit.

Write $H_C$ for the limiting component amplitude on each ordinary escaping component, with the [stated trace inputs](../global/COLLISION_ENERGY.md). By the lift-tail bound and the clipped law in equation (10) there, $F_k/k\to\sum_C\Phi(H_C)$. Telescoping (4) gives
$$
 \lim_{k\to\infty}\frac1k\sum_{i=1}^k\Gamma_i
 =\sum_C\Phi(H_C)+L_\infty<\infty .                                   \tag{5}
$$
Moreover for $U=u_k(z)$ the summand of $\Gamma_k$ at $z$ is at least
$$
 \frac{2}{(1+U)^3}\sum_{i<j}d_{k,i}(z)d_{k,j}(z),                       \tag{6}
$$
by $\Phi''(a)=2/(1+a)^3$ on $[0,U]$ and finite addition followed by monotone limits. Hence the quadratic cross-sibling overlaps in (6) have bounded Cesàro sum per depth. For any fixed $\eta>0$ a site with two increments at least $\eta$ costs at least $\Phi(2\eta)-2\Phi(\eta)>0$, by superadditivity and monotonicity of the two-increment convexity gap. On a sequence of depths of positive lower density there are only $O_\eta(1)$ such sites even if $F_k$ grows linearly.

The linear increments within each dyadic tower telescope. In (3) the clipping acts on each increment separately, and the signed coefficients depend on its depth. A positive amplitude concentrated in one increment therefore retains the sign of its actual predecessor exponent. Distinct preimages of one odd target at exponents $e$ and $e+2$ have the exact ordinary relation $x'=4x+1$; they belong to the same forward component. A uniform lower bound comparing substantial sibling amplitudes would have to address this dependence. The overlap budget (5) gives no lower bound strong enough to force cancellation in (3).

### Positive representatives with exponentially unequal unit siblings

The original residue law itself excludes any uniform finite-depth inequality $\rho_k(4x+1)\gg\rho_k(x)$ on all positive odd unit siblings, even when both are least representatives. The following *negative rational cycle* is used only to calculate the law on specified ternary residues:
$$
 -19/11\longrightarrow-23/11\longrightarrow-29/11\longrightarrow-19/11 .
$$
The gaps are $1,1,2$ and one backward lap has density weight $27/16$. The rational sibling $-65/11=4(-19/11)+1$ has gap 3 and flows to $-23/11$, so it is outside the cycle. For $k\equiv4\pmod5$ we have $3^k\equiv4\pmod{11}$. Thus
$$
 x_k=(2\cdot3^k-19)/11,\qquad 4x_k+1=(8\cdot3^k-65)/11
$$
are ordinary positive odd ternary units below $3^k$. They are genuine siblings under the ordinary positive map, while their residue laws can be evaluated on the rational labels above.

For completeness let $-b/d$ be any fixed negative rational target in lowest terms, with positive odd $b,d$ and $3\nmid d$. A length-$k$ inverse word contributing to $\rho_k(-b/d)$ lifts uniquely to an ordinary positive numerator trajectory $m_0,\ldots,m_k=b$ with $m_{i+1}=(3m_i-d)/2^{e_i}>0$. Indeed backward reconstruction is $m_i=(2^{e_i}m_{i+1}+d)/3$. Integrality at every step is exactly the ternary residue test, and each reconstructed numerator is odd. When there is no earlier visit to the target, all $m_i$ are distinct: an intervening repeat would put the target on the same cycle, with an earlier visit to it before the endpoint unless the repeated point is the target itself. Each source numerator has at most one trajectory by its 2-adic valuation.

Writing $A=\sum e_i$, the weight is
$$
 3^k2^{-A}=\frac b{m_0}\prod_{i<k}\left(1-\frac d{3m_i}\right)^{-1}
 \ll_d \frac{b\,k^{C_d}}{m_0}.
$$
All the factors have $3m_i>d$. On such integers $-\log(1-d/(3m))\le C_d/m$, and the sum of reciprocals of $k$ distinct positive integers is $O(1+\log k)$. For $A\le10k$, backward reconstruction gives $m_0\le b\,2^A(1+d)^k$, a bound exponential in $k$ at fixed $b,d$. (For $d=11,b=65$ all inverse numerators are at least five and $m_0\le65\cdot2^A$.) Summing the reciprocal bound over distinct sources costs $O_{b,d}(k)$. For the discarded words the unrestricted geometric expectation gives
$$
  3^k\Pr(A>10k)\le [9(2/3)^{10}]^k ,
$$
by $\mathbb E[(3/2)^e]=3$. Hence every fixed first-hit density layer on these negative rational targets is polynomially bounded in $k$.

In particular $\rho_k(-65/11)\ll k^C$, whereas $\rho_k(-19/11)\gg(27/16)^{\lfloor k/3\rfloor}$ by its actual repeated word, with a constant for the at most two remaining letters. This proves exponential failure of the sibling ratio at the displayed positive representatives. Conversely summing first-hit layers over the possible repeated laps gives $\rho_k(-19/11)\ll k^{C'}(27/16)^{k/3}$. Both harmonic amplitudes $u_k(x_k)$ and $u_k(4x_k+1)$ consequently tend to zero exponentially.

The same distinction persists at heights $o(3^k)$ along a diagonal family. For $p\ge3$ put $d=3^p-2^{p+1}$ and $b=d+2^p$. The rational $-b/d=-1-2^p/d$ has the word $1^{p-1}2$: each exponent-one step multiplies the deviation from $-1$ by $3/2$, and the last exponent-two step returns to the stated value. Directly, the successive deviations are $2^{p-j}3^j/d$, $0\le j<p$, so the indicated 2-adic exponents are exact. Its first sibling has exponent three and is transient into the cycle. Both are ternary units. For $k$ a large multiple of the order of 3 modulo $d$, the positive representative $(2^p3^k-b)/d$ has height ratio tending to $2^p/d$. At each fixed $p$ the first-hit bound and cycle gain $3^p/2^{p+1}>1$ give an exponentially small sibling ratio and vanishing harmonic amplitudes as above. Choosing $k$ sufficiently large at each increasing $p$ makes the ratio tend to zero while both representatives are $o(3^k)$ since $2^p/d\to0$. None of these examples gives a counterexample to a comparison restricted to macroscopic harmonic spikes on one actual positive escaping trajectory.

Weaver's earlier Theorem 1 and Corollary 2 concern the natural density $d(x)$ of the infinite ordinary predecessor set. Already within the convergent tree of 1, for each fixed $D>0$ they give starts with $xd(x)\asymp(\log x)^D$ and relative first-doubling gain and $d(16x+5)/d(x)$ both of order $(\log x)^{-D}$. This rules out universal inverse-logarithmic gain under any fixed logarithmic-power threshold. Section 6 leaves open estimates restricted to escaping starts with $d(x)$ bounded below, or to excess above the target's own predicted ternary share. The examples above address the finite original-law ratio at the first sibling $4x+1$. [Weaver, Paper 202/v1, Theorem 1, Corollary 2 and §6](https://rstation.ai/problems/collatz/papers/202/v1)

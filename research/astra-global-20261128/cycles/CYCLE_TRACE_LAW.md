# The raw harmonic trace and the shape of the real fibre on every positive integer cycle

Let $U(x)=(3x+1)/2^{v_2(3x+1)}$ on positive odd integers, $w(x)=3x/(3x+1)$, and $\kappa=\log(4/3)/2$. At a unit target $y$ write $a_y=h(y)/y$ for its all-visit harmonic mass and $\nu_y$ for its stationary probability law of the relative complementary mark $B=1-R/y$. Let $C$ be any positive integer cycle, $d_C$ its odd-relative natural basin density, $\lambda_C=\prod_{z\in C}w(z)$ its primitive survival product and $b_C$ the least odd source whose forward orbit enters $C$. This floor runs over the **entire basin**. The cycle minimum can be larger. Write $\alpha_0>0$ for the uniform lower bound of $h$ at all positive odd units.

For every site $y\in C$,
\[
       \frac{h(y)}{y}\ge \frac{17\alpha_0}{336}(3+1/y).
                                                               \tag{1}
\]
The raw mass thus has a positive absolute floor even when the first-arrival factor $1-\lambda_C$ tends to zero. There are constants $K<\infty$ and $\sigma=1-H_2(\log_3 2)+\gamma>0$, with the strict improvement $\gamma>0$ inherited from the orbit-packing theorem, for which $\ell_C=\exp(-K b_C^{-\sigma})$ obeys
\[
 \ell_C\,\frac{\kappa d_C}{1-\lambda_C}\le a_y
          \le\frac{\kappa d_C}{1-\lambda_C},\qquad
 \ell_C\,t\le\nu_y([0,t])\le\min(1,t/\ell_C)\quad (0\le t\le1).
                                                               \tag{2}
\]
One can couple $B\sim\nu_y$ with a uniform $V\in(0,1)$ so that
\[
                  |\log B-\log V|\le K b_C^{-\sigma}
                    \quad\text{almost surely}.                \tag{3}
\]
In particular, over every sequence of different positive integer cycles, at **every** choice of phases, the normalized all-visit complementary marks converge to the uniform law on the whole unit interval. Both (2) and (3) control arbitrarily small positive quantiles. They do not require a bound on the odd or shortcut period, their gcd, excursion width or any rotation distance. Convergence is in the indicated distributional metrics. Weak convergence to an absolutely continuous law is compatible with singularity of each individual fibre.

## Stationary inputs and the lower barrier

The inputs are the harmonic equation $h(y)=\sum_{U(x)=y}3\,2^{-e(x)}h(x)$, the lower floor $h(x)\ge\alpha_0$ at units, and $a_y=\kappa\beta_y/(1-\lambda_C)$ on $C$. Here $\beta_y$ is the odd-relative mean of the survival product from the source through its first hitting time at $y$. At a nonperiodic root the denominator is one. The canonical reverse-path law has complementary mark equal to the infinite product of the physical survival weights, and its number of full initial reverse laps at a periodic root has the geometric law in equations (F11)–(F12) of Paper 19. [Weaver, Paper 12, equations (23)–(27)](https://rstation.ai/problems/collatz/papers/12/v1) · [Valbuena, arithmetic trace and uniform unit floor](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [Paper 19, §9, equations (F9)–(F13)](https://rstation.ai/problems/collatz/papers/19/v2)

For every $y\in C$, at most one immediate parent is on $C$. A positive odd unit parent exists at each $e\ge1$ for which $2^ey\bmod9$ is 4 or 7. In each unit residue of $y$ the admissible exponents occupy two classes modulo six. Removing the largest single branch weight from their infinite sum gives the following bounds on the off-cycle sum of $3\,2^{-e}$.

| $y\bmod9$ | Unit-parent exponent classes modulo 6, using $1,\ldots,6$ | Weight left after removing the heaviest |
|---|---|---|
| 1 | 2, 4 | $17/84$ |
| 2 | 1, 3 | $17/42$ |
| 4 | 2, 6 | $5/84$ |
| 5 | 3, 5 | $17/168$ |
| 7 | 4, 6 | $17/336$ |
| 8 | 1, 5 | $5/42$ |

Put $c=17\alpha_0/336$. If $x$ is the cycle predecessor of $y$, harmonicity gives
\[
                    a_y\ge w(x)a_x+c/y .
\]
The function $L(x)=c(3+1/x)$ satisfies $w(x)L(x)=3c$. Subtracting $L(y)$ and iterating the inequality around the lap gives $a_y-L(y)\ge\lambda_C(a_y-L(y))$. Since $\lambda_C<1$, this proves (1). In particular $d_C\ge (3c/\kappa)(1-\lambda_C)$ by the upper trace formula. This supplies a direct unweighted basin interpretation of the gap cost. Summability of positive cycle gaps and a much sharper explicit numerical total already follow by different methods. [Paper 217](https://rstation.ai/problems/collatz/papers/217/v1)

## Uniform log-quantile coupling

Paper 28, §8.1, equation (P3), implies that any distinct-state segment of a true forward shortcut orbit obeys
\[
       \sum_{x\text{ on segment},\,x\ge b}\frac1x\ll b^{-\sigma}.
\]
For a segment of reversed odd predecessors apply the same statement in the forward direction from its deepest vertex. It suffices that its odd vertices are distinct since they form a subset of the set of distinct shortcut values on this forward orbit. The bound is independent of the length, so applies to an infinite simple reverse path by exhaustion. This is a direct use of the source's orbit-set bound, which allows eventual periodicity and counts each vertex only once. [Paper 28, §8.1, (P2)–(P3)](https://rstation.ai/problems/collatz/papers/28/v3)

Every such path inside the basin has $\prod w(x)\ge\exp(-K b_C^{-\sigma})=\ell_C$, since $-\log w(x)\le1/(3x)$. The complete cycle lap has this bound as well. A first-hit path to $y$ has distinct departed vertices, so every source entering the cycle supplies a first-hit product in $[\ell_C,1]$. Its weighted density satisfies $\ell_C d_C\le\beta_y\le d_C$, proving the first bound in (2).

On the canonical reverse law at $y$, let $G$ be the number of complete initial laps and $D$ the normalized complementary mark after removing them. The source's geometric decomposition gives $B=\lambda_C^G D$, where $D$ is independent of $G$ and $\Pr(G=j)=(1-\lambda_C)\lambda_C^j$. The partial lap and subsequent escaping backward path together have distinct departed vertices. A repeated vertex outside the cycle would itself be periodic and could not reach $C$; on the partial lap the exit has occurred before a full period. Thus $\ell_C\le D\le1$. This strengthens the uniform lower support constant in (F12) to a lower bound approaching one with the least member of this actual basin.

Independently sample $D$ and a uniform $V\in(0,1)$. Select $G=j$ when $\lambda_C^{j+1}<V\le\lambda_C^j$, ignoring the null boundaries. Then $V\le\lambda_C^G<V/\lambda_C$, so
\[
                  \ell_C V\le B\le V/\lambda_C\le V/\ell_C.
\]
This is (3) and implies the CDF bounds in (2). Distinct basins have distinct least odd members, so their floors tend to infinity on any pairwise distinct sequence. The exponential law of $-\log V$ therefore approximates the entire log-mark distribution with a uniform additive error.

At a nonperiodic unit $y$, define $b_y$ as its least odd predecessor including $y$. Every reverse path is simple. Precisely the same argument gives $\operatorname{supp}\nu_y\subset[\exp(-K b_y^{-\sigma}),1]$. For each escaping component choose one ordinary forward ray. Outside the union of those rays, all sufficiently large nonperiodic sites have $b_y$ above any prescribed $M$. Indeed the forward orbits of finitely many odd roots at most $M$ contain only finitely many points off the chosen rays, since they either have finite range or eventually merge with the appropriate ray. Thus the normalized laws at those sites tend to the point mass at one. The two spatial conclusions concern raw probability laws even when their first-arrival harmonic mass goes to zero.

The first-exit identity and prior fixed-target endpoint classification already distinguish periodic from nonperiodic at a single root. The additional uniform statement here identifies the distribution on the **whole** interval along arbitrary moving cycle components, controls its log quantiles at every scale, and supplies the absolute raw-mass lower barrier. All conclusions allow a single extra finite cycle and any putative sequence of cycles whose gaps tend to zero.

The [exact finite control](check_cycle_trace.py) checks the ordinary unit-parent floor, native marks and adjacent CDF jumps with per-step exponents at most eight, and the all-offset lap identities on primitive positive rational traces. [Recorded counts](../../../reports/astra-global-20261128/cycles/CYCLE_TRACE.json)

# The critical number of inverse generations on an actual escaping component

**Source-qualified written theorem.** Retain the actual ray $q_j$, first-entry depth $r_y$, least ordinary odd ancestor $m_y$, and full branch gain $G_y$ from [Entry-edge gains](ENTRY_EDGE_GAINS.md). Put
$$
 D=1-\tfrac12\log_2 3,\qquad \lambda=\frac1{2D}=\frac1{2-\log_2 3},
 \qquad L_y=\log_2 m_y .
$$
The transition in the harmonic sum of maximal gains is exactly at $\lambda=2.4094\ldots$ odd steps per binary digit of the least ancestor.

* For every $0<\eta<\lambda$, there is an $s_\eta<1$ with $\sum_{1\le r_y\le\eta L_y}G_y^{s_\eta}<\infty$.
* For each $A\ge0$, there is a $C_A<\infty$ such that
  $$
    \sum_{\substack{L_y\ge2\\1\le r_y\le\lambda L_y-C_A\sqrt{L_y\log(2+L_y)}}}
               (1+L_y)^A G_y<\infty. \tag{1}
  $$
* Fix any fresh unit predecessor $b$ of any $q_j$, $j\ge1$. For every fixed $B\ge0$,
  $$
    \sum_{\substack{y\to b,\ 3\mid y\\1\le r_y\le\lambda L_y-B\sqrt{L_y}}}G_y=\infty. \tag{2}
  $$
  All the displayed $y$ are odd leaves, so $m_y=y$. The series still diverges after division by $1+L_y$.

The elementary result at radius $L_y/512$ has no analytic dependency. The larger radii above use two published-in-manuscript first-passage estimates. The divergence uses the timed natural-density law for a **fixed ordinary target** together with positivity of its predecessor density. These substantial inputs are unrefereed, and the deductions on this page have no Lean formalization. A final prefix argument below reaches the same order of displacement as (1) with a smaller coefficient. The coefficient separating the two conclusions is open.

## Two passage inputs for convergence

Paper 191/v2, Theorem 1, applies to every interval of $N$ consecutive positive starts. Write $L=\log_2 N$. For $B_0\le B\le L/2$, outside at most $CNL^3 2^{-cB}$ starts, its two clock estimates hold simultaneously for all real $0\le t\le L-B-1$. At the first strict crossing of $x2^{-t}$ they give
$$
 \left|h_T-t/D\right|+\left|h_C-3t/(2D)\right|\le C\sqrt{LB}.
 \tag{3}
$$
The first ordinary crossing falls at a shortcut boundary: the extra state after an odd departure exceeds the departure. Consequently $h_C-h_T$ counts exactly the odd departures before this first crossing. In particular their number differs from $\lambda t$ by at most $C\sqrt{LB}$. [Collatz first passage in translated intervals, v2, Theorem 1](https://rstation.ai/problems/collatz/papers/191/v2)

Paper 102/v1, Theorem 1, samples $W_Z$ uniformly among odds in $(Z/4,Z]$. Let $\operatorname{Pass}_M$ be the first odd iterate at most $M$, with a distinct failure label. For $Z\ge4M$ and every set of odd integers $A\subset[1,M]$,
$$
 \Pr(\operatorname{Pass}_M(W_Z)\in A)
 \le C e^{C\sqrt{\log M}}\left(|A|/M+M^{-g}\right),\qquad g>0. \tag{4}
$$
The same single-set bound includes the choice $A$ of **all** small odd sites of our fixed injective ray. Its cardinality is $O(M^{\rho'} )$ for some absolute $\rho'<1$ by the self-contained short-clock proof in the companion note. The inputs count actual starts before any conditioning on their basin or ancestry. [Power bounds for first Collatz landings, v1, Theorem 1](https://rstation.ai/problems/collatz/papers/102/v1)

## A least ancestor forces the marked site before first descent

Take an odd $x=m_y$ in $[X,2X)$, with $X$ an integer power of two. Before the occurrence of $y$, its odd path has no value smaller than $x$. Every intervening even state is at least its next odd value. Thus $y$ occurs strictly before the first shortcut crossing below $x$, whenever that crossing occurs. This also holds with $y=x$ at clock zero. If one such $x$ is minimal for several vertices whose depths are at most $R$, all lie among the last $R$ off-ray odd states of its unique trajectory before its first entry. Hence there are at most $R$ labels per source.

Fix $0<\eta<\lambda$ and choose $\eta/\lambda<\kappa<1$. Set $M=\lfloor X^{1-\kappa}\rfloor$ and $B=\epsilon L$, with $L=\log_2 X$. Apply (3) at $t=0$ and at the source-dependent $t=\log_2(x/(M+1/2))=\kappa L+O(1)$. Choose $\epsilon>0$ sufficiently small relative to $1-\kappa$ and $\lambda\kappa-\eta$. The allowed range contains both tests. Before the marked $y$ there are at most $C\sqrt\epsilon L$ odd departures since the first drop below $x$ has occurred by this many shortcut clocks. Before the crossing of $M+1/2$, there are at least $(\lambda\kappa-C\sqrt\epsilon)L-O(1)$ odd departures. If $r_y\le\eta\log_2 m_y$, the latter crossing therefore follows more than $r_y$ odd departures after the marked site, for all sufficiently large $X$.

The ray has already been entered before that crossing. Its first subsequent odd value at most $M$ belongs to $A_M=\{q_j:q_j\le M\}$. Every earlier odd value exceeded $M$, so this is precisely $\operatorname{Pass}_M(x)$. This argument includes a first shortcut crossing at an even state. Apply (4) once to $A_M$, using $Z=2X$ and the fact that $(Z/4,Z]$ contains all but the harmless endpoint convention of our odd shell. The exceptional starts of (3) number $O(XL^3 2^{-c\epsilon L})$. The remaining possible minima number
$$
 \ll X e^{C\sqrt{\log M}}\left(M^{\rho'-1}+M^{-g}\right).
$$
Both bounds save a fixed power of $X$. Charging the $O_\eta(L)$ labels per minimum preserves a power saving. Thus the number of such $y$ in each least-ancestor shell is $O_\eta(X^{1-\beta_\eta})$ for some $\beta_\eta>0$. Since $G_y\le P(a)/m_y$, any $s_\eta$ strictly between $1-\beta_\eta$ and one works.

For (1), fix an arbitrarily large $J>A+3$. Choose $B=b\log_2 L$ with $b$ large enough to give at most $O(X L^{-J})$ exceptions in (3). Choose $M=\lceil L^k\rceil$ with $k>b+3$ also large enough that (4) at $A_M$ costs at most $O(X L^{-J})$. The second parameter is now $t=L-k\log_2 L+O(1)$ within the admissible range of (3). The difference of the guaranteed number of odd departures before this crossing and the maximum before the mark is at least
$$
   \lambda L-C_b\sqrt{L\log(2+L)}-O_k(\log L).
$$
Increasing $C_A$ gives strictly more than the allowed $r_y$ for all large $X$, including the $O(1)$ difference between $L$ and $L_y$. The same first landing argument gives only $O(XL^{-J})$ possible minima. The $O(L)$ labels per minimum and the factor $(1+L_y)^A G_y$ yield $O_{a,A}(L^{A+1-J})$ per dyadic shell, a summable bound.

## An ordinary fixed-target Gaussian law forces divergence

Write $\tau_b(v)$ for the first shortcut visit from a positive integer $v$ to the **fixed** odd unit $b$. Leen's every-target timed law, also stated as (A.8) in Paper 179, uses natural logarithms. With $\mu=2/\log(4/3)$, $\sigma^2=2(\log3)^2/\log(4/3)^3$ and $\Phi$ the standard normal distribution function,
$$
 \operatorname{dens}\{v:\tau_b(v)<\infty,
       \tau_b(v)\le\mu\log v+z\sigma\sqrt{\log v}\}
       =h_T(b)\Phi(z),\qquad z\in\mathbb R. \tag{5}
$$
Positive unit predecessor density gives $h_T(b)>0$. We use (5) exactly as a named input. We checked the displayed statement in Paper 179. The originating Leen preprint was unavailable for independent inspection during this sprint. It concerns each fixed target regardless of its forward behavior. [Brownian motion in Collatz orbits, §1.3](https://doi.org/10.5281/zenodo.23252395) · [Exact every-target interface and positivity, Paper 179, Appendix A.4–A.5](https://rstation.ai/problems/collatz/papers/179) · [Positive lower density of Collatz predecessors](https://proofatlas.ai/formalizations/positive-lower-density-collatz-predecessors/)

For a fixed negative $z$, the set in (5) has a positive proportion in every sufficiently large interval $[X,2X)$ by differencing its natural counts. Discard $v$ with $v_2(v)>E$, where $E$ is a fixed constant so large that this deletes less than half that proportion. Put $u=v/2^{v_2(v)}$. The resulting odd inputs have bounded multiplicity, lie between $X/2^E$ and $2X$, and hit $b$. The number $k$ of odd steps up to $b$ is unchanged by removing the initial halvings. From the exact affine identity, or multiplication of the positive correction factors,
$$
 k\log_2 3\le\tau_b(v)-\log_2 v+\log_2 b .
$$
As $\mu\log v=(\log_2 v)/D$, and $(1/D-1)/\log_2 3=\lambda$, choosing a sufficiently negative fixed $z$ makes
$$
          1+k \le \lambda\log_2u-(B+1)\sqrt{\log_2u}
$$
for all sufficiently large retained $u$. The fixed shifts $E$ and $\log_2 b$ are absorbed by the strict margin in the coefficient of the square root. The later comparison for a one-step lift can absorb one additional fixed clock in the same margin.

If $3\mid u$, set $y=u$. Otherwise take $1\le e\le6$ with $2^e u\equiv1\bmod9$, and put $y=(2^e u-1)/3$. Such an $e$ exists because two generates the units modulo nine. We have $3\mid y$, $y$ odd and $U(y)=u$. The map $u\mapsto y$ has at most two preimages: $y$ itself and its unique odd successor. The ratio $y/u$ stays between two positive absolute constants. In either case $y$ reaches $b$ and first enters the fixed ray exactly one odd transition after hitting $b$. Its first-entry depth is at most $k+2$. No odd transition lands at a multiple of three, so $m_y=y$ and $G_y=P(a)/P(y)\ge P(a)/(Cy)$.

Consequently $\gg_{b,B}X$ different marked leaves in $[c_{b,B}X,C'X]$ satisfy the inequality in (2) for every large $X$. Take disjoint such intervals with $X$ in a geometric progression of sufficiently large fixed ratio. Each group contributes a positive constant to (2), and at least a constant divided by the group number after the further weight $(1+L_y)^{-1}$. Both sums diverge.

There are infinitely many fresh unit parents at every $q_j$, since the condition that $(2^e q_j-1)/3$ be an odd unit holds in two of the six eligible residue tests modulo nine in each period of $e$. Equation (2) already diverges within one prescribed branch. The divergence consists of *different leaves* deep inside that branch, whereas the entire normalized maximum of the one branch contributes just one term to the summable fresh-parent series. Thus ordinary inverse branching does force harmonic divergence, but only beyond the generation range where the convergence argument reaches it. The next calculation compares the sizes of the two boundary windows.

## Divergence for a small coefficient at the same moderate-deviation scale

Using the counted synchronization estimate in Paper 215, §6.3, as one more source-qualified input, for every fixed fresh unit $b$ there is a constant $c_b>0$ such that
$$
 \sum_{\substack{y\to b,\ 3\mid y,\ L_y\ge2\\
          1\le r_y\le\lambda L_y-c_b\sqrt{L_y\log(2+L_y)}}}G_y=\infty. \tag{6}
$$
Consequently the order $\sqrt{L\log L}$ in the displacement is the same for the convergence and divergence statements. Neither the constants nor a universal critical coefficient are determined here.

Use odd sources $v$ in $(3X/4,7X/8)$ and let $L=\log_2 X$. Prescribe their first $h=\lfloor cL\rfloor$ parity bits, with $c>0$ small and fixed below, beginning with an odd bit. For each such word of odd count $p$, its representatives form $v=2^h n+r$ with $n$ in an interval of $M\asymp X/2^h$ consecutive integers, and their states at $h$ are $Y_n=3^p n+B$ with $0\le B<2\cdot3^p$. Paper 215 gives the following actual coupling. Compare $Y_n$ to $Y'_n=3^pn+R$ for an independent uniform integer $0\le R<3^p$. With $n$ uniform in its actual interval, the comparison start is uniform on one consecutive interval with endpoints $(3/4+o(1))W,(7/8+o(1))W$, $W=3^pX/2^h$. At clock $j=\lfloor(\log_2 M)/2\rfloor$ the probability of failing to have equal states and odd counts is at most
$$
  C\sqrt{(p+1)/(j+1)}+2^j/M. \tag{7}
$$
Indeed the offset in the coupled pair is at most $2\cdot3^p$. The counted synchronization bound for a Haar binary input transfers to the finite interval of $n$ by $2^j$-periodicity of the test, since $3^p$ is odd. All original states before its prefix ends, and all states on both arms through this coupling clock, exceed the fixed $b$ uniformly for large $X$ by the elementary halving bound. [Short parity cylinders with a prescribed target and explicit coupling, Paper 215, §6.3](https://rstation.ai/problems/collatz/papers/215)

Apply (5) at $z=0$ to the uniform comparison interval. Its endpoints have a fixed ratio bigger than one and its lower endpoint tends uniformly to infinity as $W\ge X^{1-c}$. Differencing the natural counts gives probability $h_T(b)/2+o(1)$ to hitting $b$ by shortcut time $\mu\log Y'_n$, uniformly in the prescribed word. Choose $c=c(b)>0$ so small that (7) is below $h_T(b)/4$ for all large $X$. On success in both tests, none of the paths hit $b$ early, and equality at date $j$ makes the two first-hit times from $Y_n,Y'_n$ equal. A fixed positive fraction in **each** prescribed prefix therefore satisfies
$$
 \begin{aligned}
 \tau_b(v)&\le h+\mu\log Y'_n\\
           &\le \mu\log v+\mu\log 3\,(p-h/2)+O(1).
 \end{aligned} \tag{8}
$$
The last identity uses $Y'_n/v\asymp 3^p/2^h$ with absolute comparison constants, and $1-\mu\log2+\tfrac12\mu\log3=0$. A successful event in the coupling bounds the proportion of original $n$ because its marginal is the actual uniform source law. The relative lower bound is uniform even for an individually rare parity word.

Take $p=\lfloor h/2-\frac1{16}\sqrt{h\log h}\rfloor$, using a natural logarithm here. The fraction of all binary words with first bit one and this exact count is $2^{-h}{h-1\choose p-1}$. Stirling's bounds and the Taylor expansion of the binary entropy at $1/2$ give
$$
  2^{-h}{h-1\choose p-1}
    =h^{-1/2-2/16^2+o(1)}\gg h^{-2/3}.
$$
Explicitly, with $d=h/2-p$, the natural log of the binomial probability is $-\frac12\log h-2d^2/h+O(1+d^4/h^3)$, and requiring the first bit one multiplies it by $p/h$. Across these disjoint words at least $\gg_b X L^{-2/3}$ original odd $v$ obey (8). Converting shortcut clocks to odd counts as above gives
$$
 k\le\lambda\log_2 v-\frac{\mu\log 3}{\log_2 3}\,
                        \frac{\sqrt{h\log h}}{16}+O_b(1).
$$
The factor $\mu\log 3/\log_2 3=\mu\log 2$ is strictly positive. The same at-most-two-to-one conversion of $v$ to an odd multiple-of-three leaf changes $\log_2 v$ and the marked depth by bounded amounts. Choosing a smaller fixed $c_b>0$ gives the radius in (6). In disjoint geometric shells each such leaf contributes $\gg_a X^{-1}$ to the gain sum, so the contribution per shell is $\gg_{a,b}L^{-2/3}$. The sum over these shells diverges.

This proves coexistence of two different behaviors on the same hypothetical ordinary component. Small and large coefficients at the scale in (1) and (6) already give different harmonic summability conclusions. The changing vertices that yield (6) can all enter the ray through one fixed edge.

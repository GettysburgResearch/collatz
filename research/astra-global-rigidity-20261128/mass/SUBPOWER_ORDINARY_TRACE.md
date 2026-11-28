# Ordinary logarithmic sampling of the stationary trace up to subpower height

Let $U(n)=(3n+1)/2^{v_2(3n+1)}$ on the positive odd integers, $D=\log(4/3)$ and $\kappa=D/2$. Write $h(n)$ for the actual canonical trace at the integer $n$. On a nonperiodic odd unit it equals $\kappa n\beta_n$, where $\beta_n$ is the odd-relative mean of the first-hit survival correction and $0\le\beta_n\le d_n$. Here $d_n$ is the relative odd density of the entire predecessor set $B_n$. At odd multiples of three $h(n)=0$. A periodic odd target has its full lap factor in $h(n)$.

Let $\lambda$ be *additive* Haar probability on $\mathbb Z_3$, and $E$ Valbuena's greatest lower semicontinuous density of the stationary Syracuse law. Thus $E(n)=h(n)$ at all positive integers, $\int E\,d\lambda=1$, and $E$ can be infinite on a null set. Define $\mathcal L_R$ by giving each positive odd $n\le R$ weight $n^{-1}/H_R$, where $H_R=\sum_{n\le R,\ n\ {\rm odd}}1/n=(\log R)/2+O(1)$.

**Theorem.** Let $w(n)>0$ be any prescribed function with $w(n)\to\infty$ and $\log^+ w(n)=o(\log n)$. Then
\[
        \lim_{R\to\infty}\mathbb E_{\mathcal L_R}\min(h(n),w(n))=1. \tag{1}
\]
Under $\mathcal L_R$, the joint law of $(n,h(n))$ on $\mathbb Z_3\times[0,\infty]$ converges weakly to the law of $(Z,E(Z))$, $Z\sim\lambda$. In particular, for each $M<\infty$, every bounded continuous test of the ternary source and its capped trace has this Haar limit. Some $p_0>0$ also has the uncapped property
\[
 \lim_{R\to\infty}\mathbb E_{\mathcal L_R} h(n)^p
       =\int_{\mathbb Z_3} E(z)^p\,d\lambda(z)
            \qquad(0<p<p_0).                                          \tag{2}
\]
All conclusions are source-qualified written deductions. The upper bound retains the ordinary forward edges and includes possible escaping components and additional cycles. No quantitative onset or positive numerical value of $p_0$ is claimed. The cap in (1) depends on the *individual physical site* $n$.

Valbuena proves the trace formula, the semicontinuous envelope, its equality to the trace at each integer, and the raw first-hit occupation lower bound with a strict excess in the presence of an escaping ray. Those inputs do not state the capped upper bound here. Weaver proves the sharp first harmonic moment of the *finite* ternary density at a cutoff tied to its depth. Here the infinite-depth trace is already evaluated at the original integer before any physical sampling or clipping. [Valbuena, stationary envelope, theorem “The stationary density” and definition of $e_k$, pinned a7275d5](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/positive-stationary-envelope.tex) · [Valbuena, Green trace, weighted-density comparison and raw occupation, same pin](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex) · [Weaver 176/v1, Theorems 1–3](https://rstation.ai/problems/collatz/papers/176/v1).

## Antichains of first entrances

For any finite set $F$ of positive odd vertices, let
\[
       V(F)=\{U^i f:f\in F,\ i\ge0\},
       \qquad \tau_F(n)=\inf\{i\ge0: U^i n\in F\}.
\]
For each fixed $j\ge1$, the points $n\notin V(F)$ with $\tau_F(n)=j$ are nonperiodic and their full odd predecessor sets $B_n$ are pairwise disjoint. In fact a periodic point hitting $F$ belongs to $V(F)$. If two distinct points shared a predecessor, one would be a strictly later state of the other's orbit. A separation of less than $j$ decreases the first entrance grade. A separation at least $j$ places the later point in $V(F)$. Consequently at any one grade the sum of $d_n$ over any finite selection of these roots is at most one. Thus for every $J$
\[
   \sum_{\substack{n\in A,\ n\notin V(F)\\1\le\tau_F(n)\le J}}
          \frac{h(n)}n\ \le\ \kappa J                              \tag{3}
\]
for every finite set $A$ of positive odd integers. Nonunit sites have zero trace. This argument only uses finite additivity for disjoint sets with genuine densities and the nonperiodic trace formula. It applies across *different* first landing points of the same floor.

For comparison, a fixed odd waypoint $a$ yields the same estimate grade by grade with $d_a$ on the right, after removing periodic roots from each first-arrival grade. Two different nonperiodic roots of the same grade to $a$ cannot be comparable. A later root visited after $a$ would create a return to $a$, with that root itself on the cycle. Their disjoint basins are contained in $B_a$. One may cover all but $\epsilon$ of the ordinary source mass by finitely many disjoint such waypoint basins, choosing a common odd unit waypoint for each represented component after the finite low seeds it must cover. Typical first-hit grade to each fixed waypoint is $(1+o(1))\log n/D$ in its ordinary basin. Hence fixed caps already have a sharp upper bound by summing at most $(1+\epsilon)\log R/D$ grades and paying $M\epsilon$ for omitted sites. The moving floor in (3) avoids any uniform first-hit assumption for a growing family of waypoints. [Finite waypoint coverage](FINITE_COMPONENT_PARTITION.md) · [Fixed-target ordinary clock and pins](FIXED_BASIN_NATIVE_WINDOW.md).

## Sparse ordinary exceptions to the moving floor

We use two quantitative inputs. Inselmann's Theorem 3.8 says that for each $u>0$, apart from $O_u(Y^{1-c(u)})$ odd sources up to $Y$ for some $c(u)>0$,
\[
 U^j n\le (3/4)^j n^{1+u}\quad(0\le j\le \log n/D).                 \tag{4}
\]
This is the stronger star-density statement in §3, with Definition 2.6. Secondly, uniformly over individual seeds $f$, the number of distinct states of its odd forward orbit through height $Y$ is $O(Y^\theta)$ for an absolute $\theta<1$. One may take $\theta=49/50$. A periodic trajectory is counted through its first repeat, a simple infinite trajectory through its successively longer finite prefixes. [Inselmann, arXiv:2402.03276v3, Definition 2.6 and Theorem 3.8](https://arxiv.org/html/2402.03276v3) · [Elementary uniform simple-path packing, PR212 at 3131111](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-infinite-descent-20261127/escape/HIGH_TARGET_ROWS.md).

Fix $0<\alpha<1$ and $0<\delta<\alpha(1-\theta)$. On the block $R^\alpha<n\le R$ take $F$ to be the positive odds up to $R^\delta$ and $u=\delta/2$. In any dyadic band $Y\le n<2Y$ meeting this block, $Y\ge R^\alpha/2$. The number of sites in $V(F)$ there is at most
\[
               C R^\delta Y^\theta\ll_\alpha Y^{\theta+\delta/\alpha}.
\]
The sites failing (4) number $O_\delta(Y^{1-c(u)})$. Thus the union of these exceptional sites has size $O_{\alpha,\delta}(Y^{1-b})$, where
\[
 b=\min\{c(\delta/2),\,1-\theta-\delta/\alpha\}>0.                   \tag{5}
\]
Every remaining site enters $F$ by grade $\lfloor\log n/D\rfloor$. Indeed its state at that grade is at most $e^D n^{\delta/2}\le R^\delta$ for large $R$. These sites are nonperiodic. Their untruncated sum of $h(n)/n$ on the whole block is at most $\kappa\lfloor\log R/D\rfloor$ by (3). The exceptional sites at scale $Y$ contribute only $O_{\alpha,\delta}(Y^{-b/2})$ to the clipped sum once $w(n)\le n^{b/2}$. Summing the dyadic bands gives $o_{\alpha,\delta}(1)$. 

Write $A(R)=\sum_{n\le R,\ {\rm odd}}\min(h(n),w(n))/n$. We have proved
\[
              A(R)-A(R^\alpha)\le \tfrac12\log R+o_{\alpha,\delta}(1).
                                                                        \tag{6}
\]
Iterate on $R,R^\alpha,R^{\alpha^2},\ldots$ until the argument is bounded by a fixed large constant. The number of blocks is $O_\alpha(1+\log\log R)$ and their logarithms form a geometric progression. Bounding each sufficiently late-onset error in (6) by one gives
\[
                \limsup_{R\to\infty}\frac{A(R)}{H_R}
                         \le \frac1{1-\alpha}.
\]
This works for every fixed $\alpha>0$, because the prescribed subpower $w$ is eventually below every power needed in (5). Send $\alpha$ to zero. More quantitatively, for a fixed power cap $w(n)=n^s$ the same argument gives this bound whenever $s<b$ for the chosen parameters. It gives no uniform positive lower bound for $b$ as $\alpha\downarrow0$.

## Matching the Haar distribution

The bounded functions $e_k$ in Valbuena's envelope are the infima of the ordinary trace on classes modulo $3^k$. They are nonnegative, constant on each class, and increase pointwise to $E$. Each fixed $e_k$ has mean under $\mathcal L_R$ tending to $\int e_k\,d\lambda$, by summing the odd progressions. Since $e_k(n)\le h(n)$ and $w(n)\to\infty$, all sufficiently large sites have $\min(h(n),w(n))\ge e_k(n)$. Monotone convergence as $k\to\infty$ gives the matching lower bound in (1).

For a weak subsequential joint limit of $(n,h(n))$, the first marginal is $\lambda$. Denote the coordinate variables by $(Z,Y)$ and compactify the second coordinate at infinity. Each closed condition $Y\ge e_k(Z)$ has probability one, hence $Y\ge E(Z)$ almost surely. Every fixed $M<\infty$ satisfies $\limsup_R\mathbb E_{\mathcal L_R}(h(n)\wedge M)\le1$ by (1), because $w(n)\ge M$ eventually. Thus $\mathbb E Y\le1$ by bounded continuous tests and monotone convergence. Since $\mathbb E E(Z)=1$, equality $Y=E(Z)<\infty$ holds almost surely. All subsequences have the stated joint limit.

For the original finite rows $\rho_k(z)=3^k\mu(z+3^k\mathbb Z_3)=\mathbb E_\lambda[E\mid z\bmod3^k]$, this gives
\[
   \lim_{k\to\infty}\limsup_{R\to\infty}
       \Pr_{\mathcal L_R}(|h(n)-\rho_k(n)|>\eta)=0
         \qquad(\eta>0).
\]
Indeed, at fixed $k$ the closed event with threshold $\ge\eta$ has limiting upper bound $\lambda\{|E-\rho_k|\ge\eta\}$, and the finite-quotient conditional means converge in $L^1(\lambda)$. The same proof gives a stronger mean approximation for any prescribed subpower divergence cap $w$:
\[
  \lim_{k\to\infty}\limsup_{R\to\infty}
  \mathbb E_{\mathcal L_R}\big|\min(h(n),w(n))-\rho_k(n)\big|=0 .    \tag{7}
\]
Use the common minorant $e_k$, below both $\rho_k$ and the clipped ordinary trace except at finitely many ordinary sites. The absolute difference has upper average at most $2(1-\int e_k\,d\lambda)$.

## Uncapped fractional moments

Fix one pair of parameters, for example $\alpha=1/2$ and $\delta=(1-\theta)/4$, and the corresponding positive $b$ of (5). At every odd positive integer $h(n)\le\kappa n(3n+1)$. At a nonperiodic unit this follows from $d_n\le1$. At a periodic unit the multiplier of one full lap is at most $3n/(3n+1)$, because the lap includes that factor and all other factors are at most one. Its reciprocal defect is at most $3n+1$, and $\beta_n\le1$. 

For $0<p<\min(1,b/2)$ the exceptional sites in each band contribute $O(Y^{2p-b})$ to $\sum h(n)^p/n$. Summing the bands in a block gives $o(1)$. Recursing as in (6), the total exceptional contribution divided by $H_R$ tends to zero. On the good part $h(n)^p{\bf1}_{h(n)>M}\le M^{p-1}h(n)$, while (3) and the geometric progression of block lengths give a total good first moment $O_\alpha(\log R)$. This proves uniform integrability of $h^p$ along the physical logarithmic laws. Weak convergence proves (2), including joint tests of $h^p$ against any bounded continuous ternary factor.

## The scale still carrying possible escape

On an actual escaping ray $r_i$, the source-qualified stationary profile gives $h(r_i)/r_i\to H_C>0$. Its untruncated logarithmic contribution is therefore proportional to the number of those distinct states encountered. Its entire contribution after any subpower site cap has **finite** harmonic sum: choose $0<s<1-\theta$ and bound the tail in each octave by $O(Y^{\theta+s-1})$. Thus (1) controls a range in which the raw occupation obstruction from one fixed escaping ray is invisible. For the full first moment, an independent estimate on the remaining rare large-trace sites is necessary. [PR212, stationary spatial profile, 3131111](https://github.com/GettysburgResearch/collatz/blob/31311116eac06e87320c84e11de6c105292a6f78/research/astra-global-20261128/escape/SPATIAL_TRACE_TAIL.md) · [Valbuena, raw occupation and divergent excess](https://github.com/x1xhlol/collatz-two-coordinate-obstruction/blob/a7275d5a73814d3d9a400c6fe6577de9542b03a3/paper/tao-basin-densities.tex).

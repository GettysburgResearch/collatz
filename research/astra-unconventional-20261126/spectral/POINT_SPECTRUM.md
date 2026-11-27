# Essential spectrum and eigenvectors in one fixed ordinary inverse basin

Fix one positive odd integer $y$ with $3\nmid y$. Let $T$ be the ordinary shortcut map and put
\[
 B_y=\{n\ge1:T^t(n)=y\text{ for some }t\ge0\}.
\]
Use the complex space $\ell^1_w(B_y)$ with the positive weight of the [ordinary mass theorem](README.md), satisfying its discrete regular-variation hypothesis (RV) of index $\alpha\in\mathbb R$. For $M\ge0$, define $Q_{y,M}\delta_n=\delta_{T(n)}$ if $n\ne y$, $n>M$ and $T(n)>M$. In all other cases define its value to be zero. Every $n\in B_y$ other than $y$ has $T(n)\in B_y$. Killing the outgoing edge at $y$ makes the directed graph for $M=0$ a tree oriented toward its root, even when $y$ lies on a cycle. The level of $n$ is its first hitting time of $y$.

## S3. Full essential disk in each fixed inverse basin

For every such $y$ and every fixed $M$,
\[
 \sigma(Q_{y,M})=\sigma_{\mathrm{ess}}(Q_{y,M})
   =\{\lambda\in\mathbb C:|\lambda|\le R_\alpha\},\qquad
 R_\alpha=\max\{2^{-\alpha},(3/2)^\alpha\},
\]
where the essential spectrum is the Fredholm essential spectrum. In particular the full disk occurs on the known basin of 1 with its root killed, although every individual basis vector there eventually maps to zero.

**Large ordinary lifts in the chosen tree.** Every binary residue class contains arbitrarily large members of $B_y$. For an odd class this follows from the [joint routing theorem](../cycle/README.md#theorem-3-joint-profinite-density-of-the-source-and-both-grades). Fix one sufficiently large odd depth $k$ and increase the shortcut clock $E$. Along the resulting path $2^Ey\le4^k n$ because $2T(v)\le4v$ at odd inputs and $2T(v)=v$ at even inputs. Thus the sources tend to infinity. For a nonzero even class modulo $2^L$, factor out its exact $2^s$ and double an odd rooted source in the required class modulo $2^{L-s}$ exactly $s$ times. For the zero class use $2^L$ times any sufficiently large odd rooted source. The same routing theorem gives arbitrarily large rooted odd values $c\equiv5\pmod{36}$.

The global positive mass operator bounds every power after extending inputs by zero. Thus $r(Q_{y,M})\le R_\alpha$ by the uniform weight bound of S1. For the inner disk take $c=36\ell+5\in B_y$, $a=2c$ and $b=(2c-1)/3=24\ell+3$. Taking $c$ sufficiently large ensures $a,b,c>\max(M,y)$. Both $a,b$ map to $c$ and all their dyadic multiples belong to $B_y$. For $|\lambda|<2^{-\alpha}$ the series
\[
 \sum_{j\ge0}\lambda^j(\delta_{2^j a}-\delta_{2^j b})
\]
converges by (RV) and is an eigenvector. The supports for distinct $\ell$ are disjoint since their odd parts run through injective lists congruent to 5 and 3 modulo 12 respectively. Hence every point of this open disk has infinite-dimensional kernel for $Q_{y,M}-\lambda I$. Closedness gives its boundary as well.

For $\alpha>0$ fix a length-$k$ parity word with $q$ odd letters and $|\lambda|=(3^q/2^k)^{\alpha/k}$. Realize $N$ repetitions on its binary cylinder. By the fixed-basin lift just proved, one can take its source arbitrarily large **inside** $B_y$. For $L=kN$ denote the states by $x_0,\ldots,x_L$. Since $x_j\ge2^{-L}x_0$, they can all be required to exceed $\max(M,y)$, so all remain in the tree before its killing edge. With $q_j$ the odd count up to $j$, their distinct limiting slopes are $A_j=3^{q_j}/2^j$. Choose $x_0$ high enough on this cylinder that the states are distinct and $w(x_j)/w(x_0)$ lies between $A_j^\alpha/2$ and $2 A_j^\alpha$ for every $j\le L$. This uses (RV) only at a finite list of times after $N$ has been fixed.

For $g_N=\sum_{j<L}\lambda^{-j}\delta_{x_j}$ the exact residual equals $\lambda^{1-L}\delta_{x_L}-\lambda\delta_{x_0}$. The sequence $|\lambda|^{-j} A_j^\alpha$ is positive and $k$-periodic. Consequently $\|g_N\|_w\asymp Lw(x_0)$ and the residual norm is $O(w(x_0))$, with constants independent of $N$. Choose successive supports disjoint by raising each new source. The normalized vectors then have no norm-convergent subsequence. If $Q_{y,M}-\lambda I$ were Fredholm, closed range would bound the distance to its finite-dimensional kernel by a constant times the residual, contradicting that separation. The radii from rational $q/k$ fill the entire outer annulus by closedness. This proves S3 for all indices.

## S4. Point spectrum detects summability along one true inverse ray

Use $Q=Q_{y,0}$. An inverse ray from the root is a sequence $x_0=y,x_1,x_2,\ldots$ of tree vertices with the first hit of $y$ from $x_j$ occurring at time $j$ and $T(x_{j+1})=x_j$. For $\lambda\ne0$,
\[
 \lambda\text{ is an eigenvalue of }Q
 \quad\Longleftrightarrow\quad
 \sum_{j\ge0}|\lambda|^j w(x_j)<\infty
 \text{ on some inverse ray from }y.                              \tag{1}
\]
The eigenvalue zero always occurs via $\delta_y$.

A ray with convergent series supplies the eigenvector $\sum_{j\ge0}\lambda^j\delta_{x_j}$ because the outgoing edge at its first vertex is killed. Conversely suppose $Qf=\lambda f$ with $f(v)\ne0$. In the subtree of ancestors of $v$, let $d(u)$ be the number of edges down to $v$ and put $g(u)=\lambda^{-d(u)} f(u)$. The eigen-equation says $g(u)=\sum_{u'\text{ child of }u}g(u')$. At a vertex of nonzero $g$, split its incoming probability among its children in proportion to $|g(u')|$. Start with probability one at $v$. Since the sum of child magnitudes is at least $|g(u)|$, the probability of reaching $u$ is at most $|g(u)|/|g(v)|$. Every positive-probability node has at least one child.

Up through every finite level $N$, the expected partial ray cost $\sum_{j=0}^N |\lambda|^j w(u_j)$ is thus at most $\|f\|_w/|f(v)|$. Some length-$N$ path has cost at most this same bound. The tree of partial paths with that bound has finite branching and arbitrarily large levels, so it has an infinite ray by König's lemma. All its partial costs have the same bound, proving convergence. Prepending the finite path from $y$ to $v$ in reverse orientation only changes the cost by an initial finite sum and a fixed positive factor. This proves (1) even when the coefficients of $f$ are complex.

For $\alpha>0$ define the rooted inverse odd frequency
\[
 \rho(y)=\sup_{(x_j)}\liminf_{j\to\infty}\frac{o_j}{j},\qquad
 o_j=\#\{1\le i\le j:x_i\text{ is odd}\},
\]
with the supremum over these actual infinite rays. The radius of the point spectrum, defined as the supremum of eigenvalue moduli, is exactly
\[
          r_{\rm point}(Q)=\left(\frac{3^{\rho(y)}}2\right)^\alpha,
          \qquad \frac14\le\rho(y)\le\log_3 2.                      \tag{2}
\]
Every smaller modulus is an eigenvalue. At the boundary (1) gives the exact summability test. No eigenvalue can have modulus at least one for $\alpha>0$: (RV) gives $w(n)\to\infty$, and the distinct vertices of any ray tend to infinity.

Indeed the physical edge product gives
\[
 \log x_j=j\log 2-o_j\log3+\log y-
     \sum_{1\le i\le j,\ x_i\text{ odd}}\log(1+1/(3x_i)).
\]
The $j$ distinct positive integers $x_i$ have reciprocal sum at most $1+\log j$, so the error after the first two terms is $O_y(1+\log j)$. Positivity gives the upper bound on $\rho(y)$. By the regular-variation envelope $\log w(n)=\alpha\log n+o(\log n)$. Since $x_j\le2^jy$, the root test on each ray now gives radius $(3^{\liminf o_j/j}/2)^\alpha$ for its series in (1). Taking the supremum proves the equality in (2).

For the lower bound, first take an odd ternary-unit inverse ancestor $v$ of $y$ off every cycle. There are infinitely many one-gap choices $v=(2^e y-1)/3$ with $2^e y\equiv4$ or $7\pmod9$. A periodic ancestor would place $y$ on that same finite cycle, so some choice is off-cycle. From any odd unit $z$ at least one $1\le e\le4$ has $2^e z\equiv4$ or $7\pmod9$, by the six-term cyclic list of powers of two. Hence a positive odd unit inverse child can always be chosen at cost at most four. Iterate this from $v$. A repeated vertex in this reverse continuation would make $v$ a forward image of a cycle vertex, contrary to its choice. An intersection with the initial path strictly after $v$ in forward time would likewise put $v$ on a cycle. The expanded path is therefore an inverse ray from $y$, gaining one odd departure per at most four additional shortcuts. This gives $\rho(y)\ge1/4$.

All conclusions here are written operator and arithmetic theorems. The [Lean routing result](../cycle/GradedBasin.lean) supplies the cofinal ordinary residues used in S3. Formula (2) does not determine the optimal frequency of a given root. The existence of many inverse paths into a chosen terminal leaves the forward fate of other positive integers open.

# Squared first-hit energy of the original Syracuse law counts escaping components

For $k\ge1$ set $q_k=3^k$. Use the original iid positive geometric exponent law $\Pr(e=j)=2^{-j}$ and the resulting whole-Haar ternary density $\rho_k(y)=q_k p_k(y\bmod q_k)$. Let $L_k(y)$ sum the weights $3^k2^{-A_k(x)}$ of positive odd sources whose **first** odd hit of the positive odd target $y$ occurs at clock $k$. Thus $0\le L_k(y)\le\rho_k(y)$, with equality at every nonperiodic target. Use the complete set of positive odd representatives $1\le y<2q_k$.

For each escaping positive ordinary component $C$, choose one injective odd ray $a_0,a_1,\ldots$ of ternary units. Put $H_C=\lim_n h(a_n)/P(a_n)$, where $h$ is the fixed-integer Cesàro trace and $P$ the corrected height. The [uniform lag theorem](../boundary/TRACE_PROFILE.md) proves that this limit exists and is strictly positive under its named inputs. Any two such rays eventually coincide up to an integer shift, so $H_C$ is independent of that choice.

**Source-qualified written theorem.** For every fixed real $r>1$,
\[
 \lim_{k\to\infty}\frac1k\sum_{\substack{1\le y<2\cdot3^k\\y\ {\rm odd}}}
               \left(\frac{L_k(y)}y\right)^r
       =\sum_{C\ {\rm escaping}} H_C^r <\infty. \tag{1}
\]
At $r=2$ the numerator is a collision of two independent words of the **same original law** at the same positive least odd representative, with the first-hit test applied separately to each lifted word. Equivalently the left side before the limit is $3^{2k}/k$ times the expectation of $y^{-2}$ on this doubly first-hit, equal-residue event. The square includes pairs of different sources. No alternative cycle contributes to (1), even if there are infinitely many. Weaver's earlier exponent-two detector uses a **single tilted word** with exponent probabilities $3\,4^{-j}$ and counts individual escaping sources. His original first-moment theorem below is an input here. [Weaver, Paper 176, Theorem 1 and §5.1](https://rstation.ai/problems/collatz/papers/176)

## The bound that allows exhaustion over unbounded targets

Write $g_k(y)=L_k(y)/y$. The uniform first-hit layer estimate $L_k(y)\le C y d_y$ at odd units gives $g_k\le C$; nonunits have $g_k=0$ for $k\ge1$. Here $d_y$ is the relative odd predecessor density. The [companion first-entry argument](../boundary/TRACE_PROFILE.md) proves the stronger statement $g_k(y)\ll M^{-\delta}$ if $y$ lies outside the complete forward trajectories of all ordinary starts through $M$, uniformly in $k$. Its exponent $\delta>0$ is immaterial here. The other input is the linear harmonic bound
\[
 \sum_{1\le y<2q_k,\ y\,\mathrm{odd}}g_k(y)
 \le \sum_{1\le y<2q_k,\ y\,\mathrm{odd}}\frac{\rho_k(y)}{y}=O(k).
 \tag{2}
\]
This is the boundedness direction of Weaver's original-law first-moment asymptotic. It applies to precisely these positive odd representatives. Consequently all targets outside the finite union of complete trajectories contribute $O_r(k M^{-\delta(r-1)})$ to the numerator in (1). In particular the whole left side before the limit is uniformly bounded. [First-hit layer input in PR 200](https://github.com/GettysburgResearch/collatz/blob/8e6add443b13acbcfd553676898c120183f07377/research/regularity-rigidity-20261124/global-trace-20261125/TRACE_ONSET.md)

## One actual escaping tail

For the chosen ray the uniform lag theorem provides a bounded sequence of nonnegative grade masses $(Z_v)_{v\in\mathbb Z}$ such that
\[
 \sup_{k\ge0}\left|\rho_k(a_n)/P(a_n)-Z_{n-k}\right|\to0,
 \quad Z_v\to0\ (v\to+\infty),\qquad
 \frac1J\sum_{v=1}^J |Z_{-v}-H_C|\to0 . \tag{3}
\]
Also $P(a_n)/a_n\to1$. These targets are nonperiodic, so $g_k(a_n)=\rho_k(a_n)/a_n$. Combining these facts gives $\sup_k|g_k(a_n)-Z_{n-k}|\to0$ as $n\to\infty$. For $0\le n\le k$, all the $a_n$ are legitimate representatives once $k$ is large: $a_n+1\le(3/2)^n(a_0+1)$. The first $k+1$ distinct ray sites contribute
\[
  \frac1k\sum_{n=0}^k g_k(a_n)^r \longrightarrow H_C^r . \tag{4}
\]
Indeed uniform continuity of $u\mapsto u^r$ on the bounded range permits replacing these summands by $Z_{n-k}^r$ with vanishing mean error. Cut off the finitely many small $n$ first and then use (3) uniformly in $k$. The resulting average converges by the last part of (3).

For $k<n\le k+J$, a fixed number $J$ of bounded summands vanishes after division by $k$. For $n>k+J$ the maximum $g_k(a_n)$ is at most $\sup_{v>J}Z_v+o_{k\to\infty}(1)$. The sum of the *first powers* over all such targets still in the representative window is at most (2), no matter how many ray sites return to that window. Their normalized $r$th-power contribution therefore has limsup $O((\sup_{v>J}Z_v)^{r-1})$, which tends to zero with $J$. This handles the entire unbounded future of the ray without assuming any growth rate for $a_n$.

For fixed $M$, the union of the forward trajectories of starts through $M$ is a finite disjoint union of such tails up to finitely many transient sites and finitely many periodic sites. Rays in the same component eventually coincide and are counted once. Each individual site has bounded $g_k$, so these finite discrepancies disappear after division by $k$. Equation (4) therefore gives the sum of $H_C^r$ over escaping components meeting $[1,M]$. Finally increase $M$. Those sums increase and exhaust every ordinary escaping component. The uniform bound from (2) proves their finiteness, and the complementary $O_r(M^{-\delta(r-1)})$ estimate proves (1).

The right side is zero precisely in the absence of ordinary escape, allowing any positive cycles. The identity makes sublinear growth of the specified collision energy sufficient as well as necessary. A bound on Haar-averaged ternary collision energy weights all residues equally and does not supply this positive-lift bound. The named arithmetic and analytic inputs are external to the finite Lean kernels. No independent sublinear estimate for this energy is established here.

## Exact amplitudes from the stopping-location law

Put $D=\log(4/3)$ and $f_\infty(u)=\prod_{i\ge0}3S^iu/(3S^iu+1)$. For an escaping component let $d_C=\langle f_\infty{\bf1}_C\rangle$ in the odd-relative logarithmic mean, with normalization $2/\log X$. This component weight is distinct from the unweighted predecessor density $d_y$ used in the layer bound. Write $P(a)=a/f_\infty(a)$ on an escaping ray. The coefficient in (1) is
\[
 H_C=(D/2)d_C,\qquad
 \sum_{C\ {\rm escaping}}H_C^r=(D/2)^r\sum_C d_C^r . \tag{5}
\]

To prove this, stop at $z$ with independent hazard $1/(3z+1)$ at each visit. The odd-relative logarithmic mean of the finite stopping-location law is $\nu$. Weaver proves, at every fixed positive odd $a$, the ordinary-depth limit $h(a)=\lim_k\rho_k(a)=(D/2)a(3a+1)\nu(\{a\})$. At a nonperiodic target $a$ on an escaping ray, a source $u$ visits at most once. If it visits, survival through all steps before that visit has probability $f_\infty(u)/f_\infty(a)$. Consequently, writing $P_-(a)$ for its ordinary predecessor set including $a$,
\[
 \frac{h(a)}{P(a)}=\frac D2\langle f_\infty{\bf1}_{P_-(a)}\rangle . \tag{6}
\]
The sets $P_-(a_n)$ increase. For fixed $M$, every member of $C$ whose forward minimum is at most $M$ enters one of the finitely many sites of $C$ through $M$. All such sites eventually hit the ray. Thus for sufficiently large $n$, $C\setminus P_-(a_n)$ is contained in the starts with forward minimum above $M$. Their odd-relative logarithmic density tends to zero as $M\to\infty$. Applying this bound to (6) gives (5). In particular $\sum_C H_C=(D/2)b$ for the existing total survival mass $b=\langle f_\infty\rangle$. At order two the coefficient measures the squared component probabilities of this finite surviving measure. [Weaver, Paper 176, §1 and Theorems 1–2](https://rstation.ai/problems/collatz/papers/176)

The ordinary-depth limit also strengthens (3) to $Z_v\to H_C$ as $v\to-\infty$. In fact at each fixed $n$, (3) places every sufficiently negative $Z_v$ within $\epsilon_n+o_{v\to-\infty}(1)$ of $h(a_n)/P(a_n)$, with $\epsilon_n\to0$. Now send $n\to\infty$ and use (5).

## Eventual affine counts at fixed thresholds

Put $N_k(t)=\#\{0<y<2\cdot3^k:y\text{ odd},\ g_k(y)>t\}$ for real $t>0$. At every $t$ outside an explicitly described countable set there is an integer $B(t)$ such that, for **every sufficiently large** $k$,
\[
 N_k(t)=k\,\#\{C:H_C>t\}+B(t). \tag{7}
\]
In particular the first difference of a count computed from the original finite word law is eventually a constant nonnegative integer. The excluded set comprises all $H_C$, all $Z_v$ on a chosen ray in each escaping component, and all fixed-target limits $\ell(y)=\lim_k g_k(y)$. The latter exist. At a nonperiodic target they equal $h(y)/y$. At a periodic target of minimal odd period $l$, write $w$ for the product of the $l$ branch weights $3\,2^{-e}$ along one lap. For $k\ge l$ the words with a previous visit to $y$ are precisely all length-$k-l$ words ending at $y$ followed by that lap. Thus $L_k(y)=\rho_k(y)-w\rho_{k-l}(y)$ and $\ell(y)=(1-w)h(y)/y$.

Choose $M$ so large that the complementary first-hit bound above is strictly below $t$. Only finitely many complete forward trajectories can now contribute at any $k$. Their periodic and transient sites have eventually constant threshold indicators, since $t\ne\ell(y)$. Outside finitely many sites their nonperiodic parts are disjoint chosen escaping tails. Any fixed choice of a different initial ray only shifts the integer grade. Every component with $H_C>t$ must occur among these tails by (3), (5) and the complementary bound.

On each such tail, $\sup_k|g_k(a_n)-Z_{n-k}|\to0$. Since $t\ne H_C$ and $t>0$, take $J$ large enough that for $n\ge J$ and $n-k\le-J$ the indicator is exactly ${\bf1}_{H_C>t}$, and for $n-k\ge J$ it is zero. Increase $J$ for the finitely many tails. In the fixed head $n<J$, each indicator stabilizes by the ordinary-depth limit. In the transition strip $n=k+v$, $|v|<J$, it stabilizes since $g_k(a_{k+v})\to Z_v\ne t$. Every fixed head, every strip site, and every site with $J\le n\le k-J$ lies below the representative cutoff for sufficiently large $k$, by $a_n+1\le(3/2)^n(a_0+1)$. All future out-of-window sites already have zero indicator. This proves (7), including the bounded, eventually constant integer correction. With only $t\ne H_C$ the same proof gives a bounded correction, allowing oscillation at a fixed head or fixed grade.

## The full finite residue law without a first-hit test

Define $u_k(y)=\rho_k(y)/y$, and in this section sum over all positive odd representatives at depth $k$ unless otherwise specified. Repeated cycle laps have negligible **total linear mass** at scale $k$:
\[
 \frac1k\sum_y\bigl(u_k(y)-g_k(y)\bigr)\longrightarrow0. \tag{8}
\]
Indeed consider a positive odd cycle $B$, with length $l$, lap weight $w<1$, and odd-relative predecessor density $d_B$ (the same at every site of the cycle). First-hit layers satisfy $g_j(y)\le C d_B$ at every $y\in B$, also at $j=0$ by the unit predecessor-density floor. Repeated laps give
\[
 u_k(y)-g_k(y)=\sum_{j=1}^{\lfloor k/l\rfloor} w^j g_{k-jl}(y).
\]
Summing even over all $l$ sites bounds the contribution from $B$ by $C k d_B$. For each fixed cycle the unnormalized contribution is bounded by $C l d_B w/(1-w)$. The disjoint basins satisfy $\sum_B d_B\le1$ by finite additivity and exhaustion, so dominated convergence over all positive odd cycles proves (8). At nonperiodic targets the discrepancy vanishes identically.

The mass-weighted amplitude distribution of the **original, unrestricted** finite ternary law has the finite-measure weak limit on $[0,\infty)$
\[
 \frac1k\sum_y u_k(y)\,\delta_{u_k(y)}
 \quad\Longrightarrow\quad
 \frac{\log3}{2}\,\delta_0+\sum_{C\ {\rm escaping}}H_C\,\delta_{H_C}. \tag{9}
\]
To prove this, first use $g_k$ instead of $u_k$. All $g_k$ lie in a fixed compact interval. The total mass tends to $(\log3)/2+(D/2)b$ by (8) and Weaver's first-moment theorem. All positive integer moments of the mass-weighted distribution converge by (1) with $r=2,3,\ldots$. They agree with those of the right side in (9), whose total mass is the same by (5). Polynomial approximation proves the weak limit for $g_k$. For a bounded Lipschitz test $\phi$, the pointwise difference of the raw and first-hit tests is bounded by $(\|\phi\|_\infty+C\operatorname{Lip}(\phi))(u_k-g_k)$, using $0\le g_k\le C$. Equation (8) proves (9) on bounded Lipschitz tests, hence weakly for finite measures. This argument permits exceptionally large unrestricted traces at unknown periodic targets.

For example, a statistic needing only the original finite residue probabilities satisfies
\[
 \lim_{k\to\infty}\frac1k\sum_y
 \frac{(\rho_k(y)/y)^2}{1+\rho_k(y)/y}
 =\sum_{C\ {\rm escaping}}\frac{H_C^2}{1+H_C} . \tag{10}
\]
Use the bounded Lipschitz test $u/(1+u)$ in (9). The limit vanishes exactly when every positive orbit is eventually periodic, under the source-qualified positivity input. It is insensitive to an arbitrary number of additional positive cycles and requires no cycle enumeration at any finite depth. Likewise at $t>0$ different from all amplitudes $H_C$, the unrestricted count $\#\{y:u_k(y)>t\}/k$ tends to the integer $\#\{C:H_C>t\}$, by integrating ${\bf1}_{(t,\infty)}(u)/u$ in (9). Equation (7)'s exact eventual affine count pertains to the first-hit statistic. An independent proof of sublinear growth of the explicit sum in (10) remains open here.
